#!/usr/bin/env python3
"""Discrete (Ihara-zeta) analogue of Connes-Consani-Moscovici, "Zeta spectral triples"
(arXiv:2511.22755), for finite graphs.  Companion of notes/zeta-spectral-triples/ccm_proto.py.

Pipeline (the CCM pipeline with the group R replaced by Z and the window [lambda^-1,lambda]
replaced by the lag window {-M..M}):

  graph G  ->  Hashimoto operator B  ->  N_k = Tr B^k  ->  rescaled trace sequence
  t_k = N_k q^{-k/2} minus the trivial divisor  ->  Weil form = Toeplitz matrix
  T_{jj'} = t^{nt}_{j-j'} on the window  ->  minimal eigenpair (eps_M, xi)  ->
  xi-hat(z) = sum_j xi_j z^j  ->  its roots vs the nontrivial Hashimoto points mu/sqrt q.

Everything is cross-checked: Ihara-Bass, N_k against a direct prime-cycle enumeration,
the Hashimoto spectrum against the Ihara-Bass prediction, the trace-route trace sequence
against the direct sum over the retained divisor, and each perturbed-operator variant
against the exact determinant identity.

Two variants of the CCM perturbed operator reproduce Lemma `key` exactly (see
lanes/numerics.md): the multiplicative one, D = shift and eta = delta at the window edge, which is
the companion matrix of z^M xi-hat(z) and a (tau - eps)-isometry; and the additive one on the
Cayley nodes lambda_n = tan(pi n/K) with eta_n = (-1)^n sec(pi n/K) read off from the rank-two
displacement, which is (tau - eps)-selfadjoint and returns the angles as theta = 2 arctan s.
eta = all-ones fails in every basis.

Usage:   python3 notes/zeta-spectral-triples/ihara/ihara_proto.py [--graph NAME] [--M m] [--dps d]
Default: every object, M = 0..5 (longer for the non-Ramanujan ones), dps = 40; runs in ~21 s.
"""
import argparse
import itertools
import sys
from fractions import Fraction

import numpy as np
import sympy as sp
from mpmath import mp

# ----------------------------------------------------------------------------- utilities

def ns(x, n=8):
    return mp.nstr(x, n)

def PF(ok):
    return "PASS" if ok else "FAIL"

FAILURES = []

def check(tag, ok, msg):
    """An identity that must hold; a violation is a bug."""
    if not ok:
        FAILURES.append(tag + ": " + msg)
    print(f"  [{PF(ok)}] {tag}: {msg}")


def obs(tag, ok, msg):
    """A hypothesis that may legitimately fail (Ramanujan, even-simple): observation only."""
    print(f"  [{'YES' if ok else 'NO ':}] {tag}: {msg}")

# ----------------------------------------------------------------------------- graphs

def lcf(n, shifts):
    """LCF notation: the n-cycle 0-1-...-(n-1)-0 plus chords i -- i+shifts[i mod len]."""
    E = set()
    for i in range(n):
        E.add(frozenset((i, (i + 1) % n)))
    for i in range(n):
        j = (i + shifts[i % len(shifts)]) % n
        E.add(frozenset((i, j)))
    return sorted(tuple(sorted(e)) for e in E)

def necklace(nblocks):
    """Cubic 'necklace': nblocks copies of K4 minus an edge, joined in a cycle.
    Block i has vertices 4i..4i+3; p=4i, q=4i+1 are the two degree-2 vertices."""
    E = []
    for i in range(nblocks):
        p, q, r, s = 4 * i, 4 * i + 1, 4 * i + 2, 4 * i + 3
        E += [(p, r), (p, s), (q, r), (q, s), (r, s)]      # K4 on {p,q,r,s} minus {p,q}
    for i in range(nblocks):
        E.append(tuple(sorted((4 * i + 1, 4 * ((i + 1) % nblocks)))))   # q_i -- p_{i+1}
    return sorted(set(tuple(sorted(e)) for e in E))

GRAPHS = {
    "k4":       (4,  [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]),
    "cube":     (8,  [(a, a ^ (1 << b)) for a in range(8) for b in range(3) if a < a ^ (1 << b)]),
    "petersen": (10, [(i, (i + 1) % 5) for i in range(5)]
                     + [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
                     + [(i, i + 5) for i in range(5)]),
    "k33":      (6,  [(i, j) for i in range(3) for j in range(3, 6)]),
    "heawood":  (14, lcf(14, [5, -5])),
    "pappus":   (18, lcf(18, [5, 7, -7, 7, -7, -5])),
    "necklace2": (8,  necklace(2)),
    "necklace3": (12, necklace(3)),
    "necklace6": (24, necklace(6)),
    "twok4":    (8,  [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3),
                      (4, 5), (4, 6), (4, 7), (5, 6), (5, 7), (6, 7)]),
    "tri_pendant": (5, [(0, 1), (1, 2), (0, 2), (2, 3), (3, 4)]),
    "dumbbell":    (6, [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5), (2, 3)]),
}

# objects whose interesting regime needs a longer window than the default scan
MSCAN_EXTRA = {"necklace6": 14, "necklace3": 7, "necklace2": 7, "dumbbell": 10, "twok4": 7}


def adjacency(nv, edges):
    A = np.zeros((nv, nv), dtype=np.int64)
    for u, v in edges:
        A[u, v] += 1
        A[v, u] += 1
    return A

def hashimoto(nv, edges):
    """B[e,f] = 1 iff e=(a,b), f=(b,c) with c != a.  Returns (B, directed edge list)."""
    de = []
    for u, v in edges:
        de.append((u, v))
        de.append((v, u))
    m = len(de)
    B = np.zeros((m, m), dtype=np.int64)
    for i, (a, b) in enumerate(de):
        for j, (c, d) in enumerate(de):
            if c == b and d != a:
                B[i, j] = 1
    return B, de

# -------------------------------------------------------------- checks on the graph side

def check_ihara_bass(nv, edges, A, B, seed=20260918):
    """det(1-uB) = (1-u^2)^{|E|-|V|} det(I - Au + Q u^2), Q = diag(deg-1)."""
    rng = np.random.default_rng(seed)
    deg = A.sum(axis=1)
    Q = np.diag(deg - 1).astype(float)
    g = len(edges) - nv
    worst = 0.0
    for _ in range(3):
        u = complex(rng.uniform(-0.4, 0.4), rng.uniform(-0.4, 0.4))
        lhs = np.linalg.det(np.eye(len(B)) - u * B)
        rhs = (1 - u * u) ** g * np.linalg.det(np.eye(nv) - A * u + Q * u * u)
        worst = max(worst, abs(lhs - rhs) / max(1.0, abs(lhs)))
    return worst

def prime_cycle_table(B, kmax):
    """N_k = Tr B^k from a direct enumeration of closed non-backtracking cyclic walks,
    and the prime-cycle decomposition N_k = sum_{d|k} d * (#prime cycles of length d)."""
    m = len(B)
    succ = [[j for j in range(m) if B[i, j]] for i in range(m)]
    prim = {}
    counts = {}
    for k in range(1, kmax + 1):
        total = 0
        nprim = 0
        for e0 in range(m):
            stack = [(e0, [e0])]
            while stack:
                e, path = stack.pop()
                if len(path) == k:
                    if B[e, e0]:
                        total += 1
                        if is_primitive(path):
                            nprim += 1
                    continue
                for f in succ[e]:
                    stack.append((f, path + [f]))
        counts[k] = total
        assert nprim % k == 0
        prim[k] = nprim // k
    return counts, prim

def is_primitive(seq):
    k = len(seq)
    for d in range(1, k):
        if k % d == 0 and seq == seq[:d] * (k // d):
            return False
    return True

def trace_powers(B, kmax):
    """Exact integer Tr B^k, k = 0..kmax (int64; guarded)."""
    m = len(B)
    P = np.eye(m, dtype=np.int64)
    out = [m]
    for _ in range(kmax):
        P = P @ B
        if np.abs(P).max() > 2 ** 60:
            raise OverflowError("int64 overflow in Tr B^k")
        out.append(int(np.trace(P)))
    return out

# ------------------------------------------------------------------- spectral bookkeeping

def integer_charpoly_roots(Mint):
    """Distinct roots (mpmath) with multiplicities of the characteristic polynomial of an
    integer matrix, via exact factorisation (so multiplicities are exact)."""
    x = sp.Symbol("x")
    p = sp.Poly(sp.Matrix(Mint.tolist()).charpoly(x).as_expr(), x)
    coeff, facs = sp.factor_list(p)
    out = []
    for f, mult in facs:
        c = [mp.mpf(int(z)) for z in sp.Poly(f, x).all_coeffs()]
        if len(c) == 2:
            rts = [-c[1] / c[0]]
        else:
            rts = mp.polyroots(c, maxsteps=200, extraprec=200)
        for r in rts:
            out.append((mp.mpc(r), mult))
    return out

class Divisor:
    """The data the construction consumes: a critical radius, a trivial multiset and a
    retained multiset of points (value, multiplicity), plus an optional exact trace route."""

    def __init__(self, name, critr, trivial, retained, traces=None, note=""):
        self.name = name
        self.critr = critr
        self.trivial = trivial
        self.retained = retained
        self.traces = traces          # exact Tr B^k, k = 0..kmax  (or None)
        self.note = note
        pts = {}
        for v, m in retained:
            key = (mp.nstr(mp.re(v), 20), mp.nstr(mp.im(v), 20))
            if key in pts:
                pts[key] = (pts[key][0], pts[key][1] + m)
            else:
                pts[key] = (v, m)
        self.distinct = list(pts.values())
        self.R = len(self.distinct)
        self.size = sum(m for _, m in retained)

    def t_direct(self, k):
        """sum over the retained multiset of (v/critr)^{|k|}."""
        s = mp.mpc(0)
        for v, m in self.retained:
            s += m * (v / self.critr) ** abs(k)
        return s

    def t_trace(self, k):
        """(Tr B^{|k|}) critr^{-|k|} minus the trivial part (even extension)."""
        k = abs(k)
        s = mp.mpf(self.traces[k]) / self.critr ** k
        for v, m in self.trivial:
            s -= m * (v / self.critr) ** k
        return s

def regular_divisor(name, nv, edges, A, B, traces):
    """Trivial divisor for a (q+1)-regular graph: {q, 1} from lambda = q+1, {-q,-1} if
    bipartite, and +-1 with multiplicity |E|-|V| each from the (1-u^2)^{|E|-|V|} factor."""
    deg = int(A.sum(axis=1)[0])
    q = deg - 1
    g = len(edges) - nv
    critr = mp.sqrt(q)
    lam = integer_charpoly_roots(A)
    bip = any(abs(v + (q + 1)) < mp.mpf("1e-20") for v, _ in lam)
    trivial = [(mp.mpc(q), 1), (mp.mpc(1), 1)]
    if g:
        trivial += [(mp.mpc(1), g), (mp.mpc(-1), g)]
    if bip:
        trivial += [(mp.mpc(-q), 1), (mp.mpc(-1), 1)]
    retained = []
    for v, m in lam:
        mm = m
        if abs(v - (q + 1)) < mp.mpf("1e-20"):
            mm -= 1                      # exactly ONE Perron eigenvalue is trivial
        if bip and abs(v + (q + 1)) < mp.mpf("1e-20"):
            mm -= 1
        if mm <= 0:
            continue
        d = mp.sqrt(v * v - 4 * q)
        retained.append(((v + d) / 2, mm))
        retained.append(((v - d) / 2, mm))
    return Divisor(name, critr, trivial, retained, traces,
                   note=f"({q}+1)-regular, bipartite={bip}, g=|E|-|V|={g}"), q, bip, lam

def irregular_divisor(name, nv, edges, B, traces):
    """No single q.  Stark-Terras: R_G = 1/rho(B); use critr = sqrt(rho(B)) (the geometric
    mean of the trivial pair {rho(B), 1}).  Trivial = {rho(B), 1} u {+-1}^{|E|-|V|}."""
    mu = integer_charpoly_roots(B)
    rho = max((abs(v) for v, _ in mu))
    critr = mp.sqrt(rho)
    g = len(edges) - nv
    trivial = [(mp.mpc(rho), 1), (mp.mpc(1), 1)]
    if g:
        trivial += [(mp.mpc(1), g), (mp.mpc(-1), g)]
    rem = []
    for v, m in mu:
        rem.append([v, m])
    for tv, tm in trivial:
        left = tm
        for r in rem:
            if left and abs(r[0] - tv) < mp.mpf("1e-18"):
                d = min(left, r[1])
                r[1] -= d
                left -= d
        if left:
            raise RuntimeError(f"trivial point {tv} not found in spec(B)")
    retained = [(v, m) for v, m in rem if m]
    return Divisor(name, critr, trivial, retained, traces,
                   note=f"irregular, rho(B)={ns(rho,10)}, R_G=1/rho, critr=sqrt(rho), g={g}")

def curve_divisor(name, q, numer):
    """Graded / curve case: Z(u) = P(u)/((1-u)(1-qu)), P(u) = prod(1 - alpha_i u).
    Retained = the ZEROS alpha_i; the Weil form is (trivial) - (rings)."""
    # P(u) = sum_i numer[i] u^i = prod_i (1 - alpha_i u); numer is given LOW -> HIGH in u, so
    # the alpha are the roots of sum_i numer[i] a^{d-i}: the same coefficient list read HIGH->LOW.
    alphas = mp.polyroots([mp.mpf(c) for c in numer], maxsteps=200, extraprec=200)
    retained = [(mp.mpc(a), 1) for a in alphas]
    trivial = [(mp.mpc(1), 1), (mp.mpc(q), 1)]
    div = Divisor(name, mp.sqrt(q), trivial, retained, None,
                  note=f"curve zeta, q={q}, numerator {numer} (u-coefficients low->high reversed)")
    div.curve_q = q
    div.curve_numer = numer
    return div

# ------------------------------------------------------------------ the Weil form (Toeplitz)

def poly_roots_of(xi, K):
    """Roots of xi-hat(z) = sum_{j=-M}^{M} xi_j z^j, i.e. of the degree-2M polynomial
    z^M xi-hat(z) whose coefficient vector, highest degree first, is xi_M ... xi_{-M}."""
    coeffs = [xi[K - 1 - i] for i in range(K)]
    while len(coeffs) > 1 and abs(coeffs[0]) < mp.mpf(10) ** (-mp.dps + 12):
        coeffs = coeffs[1:]
    if len(coeffs) <= 1:
        return []
    return mp.polyroots(coeffs, maxsteps=500, extraprec=500)


def point_err(true_z, roots):
    """max over the distinct retained points of the distance to the nearest root of xi-hat."""
    if not true_z or not roots:
        return None
    return float(max(min(abs(complex(z) - complex(r)) for r in roots) for z in true_z))


def toeplitz(tvals, M):
    K = 2 * M + 1
    T = mp.matrix(K, K)
    for i in range(K):
        for j in range(K):
            T[i, j] = tvals[abs(i - j)]
    return T

def even_odd_blocks(tvals, M):
    """c_0 = e_0, c_j = (e_j+e_{-j})/sqrt2 ; d_j = (e_j-e_{-j})/sqrt2."""
    E = mp.matrix(M + 1, M + 1)
    E[0, 0] = tvals[0]
    for j in range(1, M + 1):
        E[0, j] = E[j, 0] = mp.sqrt(2) * tvals[j]
        for i in range(1, M + 1):
            E[i, j] = tvals[abs(i - j)] + tvals[i + j]
    O = mp.matrix(M, M) if M else mp.matrix(0, 0)
    for i in range(1, M + 1):
        for j in range(1, M + 1):
            O[i - 1, j - 1] = tvals[abs(i - j)] - tvals[i + j]
    return E, O

def dft_matrix(M):
    K = 2 * M + 1
    F = mp.matrix(K, K)
    for ni in range(K):
        n = ni - M
        for ji in range(K):
            j = ji - M
            F[ni, ji] = mp.exp(2j * mp.pi * n * j / K) / mp.sqrt(K)
    return F

def mat_rank_svals(Amp):
    A = np.array([[complex(Amp[i, j]) for j in range(Amp.cols)] for i in range(Amp.rows)])
    s = np.linalg.svd(A, compute_uv=False)
    return s

def to_np(Amp):
    return np.array([[complex(Amp[i, j]) for j in range(Amp.cols)] for i in range(Amp.rows)])

def mp_from_np(A):
    r, c = A.shape
    out = mp.matrix(r, c)
    for i in range(r):
        for j in range(c):
            out[i, j] = mp.mpc(A[i, j])
    return out

def herm(Amp):
    out = mp.matrix(Amp.cols, Amp.rows)
    for i in range(Amp.rows):
        for j in range(Amp.cols):
            out[j, i] = mp.conj(Amp[i, j])
    return out

def fnorm(Amp):
    s = mp.mpf(0)
    for i in range(Amp.rows):
        for j in range(Amp.cols):
            s += abs(Amp[i, j]) ** 2
    return mp.sqrt(s)

# ---------------------------------------------------------------- the perturbed operators

def shift_matrices(M):
    K = 2 * M + 1
    S = mp.matrix(K, K)
    Z = mp.matrix(K, K)
    for i in range(K - 1):
        S[i + 1, i] = 1
        Z[i + 1, i] = 1
    Z[0, K - 1] = 1
    return S, Z

def variant_operators(M, F):
    """Returns dict name -> (A, description) with A a K x K mpmath matrix, plus the eta dict."""
    K = 2 * M + 1
    S, Z = shift_matrices(M)
    Fh = herm(F)
    Dth = mp.matrix(K, K)
    Dtan = mp.matrix(K, K)
    Dz = mp.matrix(K, K)
    for ni in range(K):
        n = ni - M
        Dth[ni, ni] = 2 * mp.pi * n / K
        Dtan[ni, ni] = mp.tan(mp.pi * n / K)
        Dz[ni, ni] = mp.exp(2j * mp.pi * n / K)
    ops = {
        "S":    (S, "nilpotent forward shift, position basis"),
        "Zc":   (Z, "cyclic forward shift = diag(z_n) in DFT basis"),
        "Dth":  (Fh * Dth * F, "diag(2 pi n/K) in DFT basis"),
        "Dtan": (Fh * Dtan * F, "diag(tan(pi n/K)) in DFT basis (Cayley nodes)"),
    }
    etas = {}
    e_top = mp.matrix(K, 1); e_top[K - 1] = 1
    e_bot = mp.matrix(K, 1); e_bot[0] = 1
    ones = mp.matrix(K, 1)
    for i in range(K):
        ones[i] = 1
    dftones = Fh * ones
    cay = mp.matrix(K, 1)
    for ni in range(K):
        n = ni - M
        # eta_n = (1 - i tan(pi n/K)) z_n^{-M} = (-1)^n / cos(pi n/K); this is the second vector
        # of the rank-two decomposition of the additive displacement (s_n - s_m) tau_nm.
        cay[ni] = (1 - 1j * mp.tan(mp.pi * n / K)) * mp.exp(-2j * mp.pi * n * M / K)
    etas["top"] = (e_top, "delta at the top window edge j=+M")
    etas["bot"] = (e_bot, "delta at the bottom window edge j=-M")
    etas["ones"] = (ones, "all-ones in the position basis")
    etas["dftones"] = (dftones, "all-ones in the DFT basis (= sqrt(K) delta at j=0)")
    etas["cayley"] = (Fh * cay, "(-1)^n sec(pi n/K) in the DFT basis (displacement eta)")
    return ops, etas

VARIANTS = [
    ("a1", "S",    "top",     "mult., companion"),
    ("a2", "Zc",   "top",     "mult., cyclic"),
    ("a3", "Zc",   "ones",    "task (a): cyclic shift, eta = all ones (position)"),
    ("b",  "Dth",  "dftones", "task (b): D = diag(2 pi n/K), eta = all ones (DFT)"),
    ("c1", "Dtan", "dftones", "CvS prop:finmain literal: D = diag(tan), eta = all ones (DFT)"),
    ("c2", "Dtan", "cayley",  "D = diag(tan), eta from the displacement"),
    ("d",  "Zc",   "dftones", "mult. with eta = all ones (DFT)"),
]

def target_map(opname, z):
    """Where a root z of xi-hat should sit in the spectrum of A''."""
    if opname in ("S", "Zc"):
        return complex(z)
    if opname == "Dth":
        return complex(np.angle(complex(z)))
    return complex(-1j * (complex(z) - 1) / (complex(z) + 1))      # Cayley s = -i(z-1)/(z+1)


def multiset_dist(a, b):
    """max over a of the distance to the nearest element of b (both lists of complex)."""
    if not a or not b:
        return None
    return max(min(abs(x - y) for y in b) for x in a)


def run_variants(M, T, eps, xi, true_angles, roots, ops, etas, verbose=True):
    """xi: K x 1 mpmath column (minimal eigenvector of T); roots: roots of xi-hat (mpmath)."""
    K = 2 * M + 1
    Tq = mp.matrix(K, K)
    for i in range(K):
        for j in range(K):
            Tq[i, j] = T[i, j] - (eps if i == j else 0)
    nTq = fnorm(Tq)
    tiny = mp.mpf(10) ** (-mp.dps + 8)
    rows = []
    for tag, opname, etaname, desc in VARIANTS:
        A, _ = ops[opname]
        eta, _ = etas[etaname]
        ip = mp.mpc(0)
        for i in range(K):
            ip += mp.conj(eta[i]) * xi[i]
        if abs(ip) < tiny:
            rows.append((tag, desc, "<eta|xi> = 0, no normalisation", None, None, None, None, None))
            continue
        x = mp.matrix(K, 1)
        for i in range(K):
            x[i] = xi[i] / ip                              # <eta|x> = 1
        Ax = A * x
        Ap = mp.matrix(K, K)
        for i in range(K):
            for j in range(K):
                Ap[i, j] = A[i, j] - Ax[i] * mp.conj(eta[j])
        r0 = fnorm(Ap * x)
        TA = Tq * Ap
        sa = fnorm(TA - herm(TA)) / max(fnorm(TA), tiny)
        iso = fnorm(herm(Ap) * Tq * Ap - Tq) / max(nTq, tiny)
        ev = sorted(np.linalg.eigvals(to_np(Ap)), key=lambda z: abs(z))
        ev = ev[1:]                                        # drop the forced zero eigenvalue
        tgt = [target_map(opname, r) for r in roots]
        dR = multiset_dist(tgt, ev)                        # Lemma key (iii): spec(A'') = roots
        if opname in ("S", "Zc"):
            got = [np.angle(z) for z in ev if abs(abs(z) - 1) < 1e-6]
            offt = sum(1 for z in ev if abs(abs(z) - 1) >= 1e-6)
        elif opname == "Dth":
            got = [z.real for z in ev if abs(z.imag) < 1e-6]
            offt = sum(1 for z in ev if abs(z.imag) >= 1e-6)
        else:
            got = [2 * np.arctan(z.real) for z in ev if abs(z.imag) < 1e-6]
            offt = sum(1 for z in ev if abs(z.imag) >= 1e-6)
        err = angle_match(true_angles, got)
        rows.append((tag, desc, None, float(r0), float(sa), float(iso),
                     (err, offt, len(ev)), dR))
    if verbose:
        print("    tag operator / eta                                     |A'xi|   T-selfadj T-isometry"
              " spec(A'') vs   ang.err  off")
        print("                                                                                       "
              " roots(xi-hat)")
        for tag, desc, skip, r0, sa, iso, m, dR in rows:
            if skip:
                print(f"    {tag:<3} {desc:<48} {skip}")
                continue
            err, offt, nev = m
            es = "  n/a   " if err is None else f"{err:.2e}"
            ds = "  n/a   " if dR is None else f"{dR:.2e}"
            print(f"    {tag:<3} {desc:<48} {r0:.1e}  {sa:.2e}  {iso:.2e}  {ds}      {es} {offt}/{nev}")
    return rows


def angle_match(true_angles, got):
    """max over true angles of the distance to the nearest recovered angle (mod 2pi)."""
    if not true_angles or not got:
        return None
    worst = 0.0
    for a in true_angles:
        d = min(abs((a - g + np.pi) % (2 * np.pi) - np.pi) for g in got)
        worst = max(worst, d)
    return worst

# ------------------------------------------------------------------------------ main pass

def analyse(div, Mlist, structure_at=None, verbose=True):
    print(f"\n--- divisor: retained multiset size {div.size}, distinct points R = {div.R}, "
          f"critical radius {ns(div.critr,10)}")
    print(f"    {div.note}")
    on = sum(1 for v, m in div.distinct if abs(abs(v) / div.critr - 1) < mp.mpf("1e-18"))
    obs("Ramanujan (every retained point on |mu| = critr)", on == div.R,
        f"{on} of {div.R} distinct retained points on the critical circle")
    for v, m in sorted(div.distinct, key=lambda p: (float(mp.arg(p[0])), float(abs(p[0])))):
        z = v / div.critr
        print(f"      mu = {ns(mp.re(v),10)} {'+' if mp.im(v)>=0 else '-'} {ns(abs(mp.im(v)),10)}i"
              f"   |mu|/critr = {ns(abs(z),10)}   arg = {ns(mp.arg(z),10)}   mult {m}")

    kmax = 2 * max(Mlist) + 2
    # trace route vs direct route
    if div.traces is not None:
        worst = mp.mpf(0)
        for k in range(kmax + 1):
            worst = max(worst, abs(div.t_trace(k) - mp.re(div.t_direct(k))))
        check("t^nt from Tr B^k vs direct sum over retained divisor",
              worst < mp.mpf(10) ** (-mp.dps + 10),
              f"max_k<={kmax} |diff| = {ns(worst,3)}")
    tvals = [mp.re(div.t_direct(k)) for k in range(kmax + 1)]
    imax = max(abs(mp.im(div.t_direct(k))) for k in range(kmax + 1))
    check("t^nt real (retained divisor closed under conjugation)",
          imax < mp.mpf(10) ** (-mp.dps + 10), f"max |Im t_k| = {ns(imax,3)}")
    # reciprocal closure: sum v^{-k} == sum v^{k}
    haszero = any(abs(v) < mp.mpf("1e-30") for v, m in div.retained)
    if haszero:
        obs("functional equation mu -> critr^2/mu on the retained divisor", False,
            "the retained divisor contains mu = 0 (a graph with a tail), so the reciprocal "
            "map is undefined: the literal two-sided sum does not exist")
    else:
        worst = mp.mpf(0)
        for k in range(1, kmax + 1):
            acc = mp.mpc(0)
            for v, m in div.retained:
                acc += m * (v / div.critr) ** (-k)
            worst = max(worst, abs(acc - div.t_direct(k)))
        obs("functional equation: sum (mu/critr)^{-k} = sum (mu/critr)^{k} (so even extension "
            "= Hermitian extension = literal two-sided sum)",
            worst < mp.mpf(10) ** (-mp.dps + 10), f"max_k |diff| = {ns(worst,3)}")

    true_angles = [float(mp.arg(v / div.critr)) for v, m in div.distinct
                   if abs(abs(v / div.critr) - 1) < 1e-12]

    true_z = [v / div.critr for v, m in div.distinct]
    print(f"\n    M   K  regime    eps_M            eps_even       eps_odd      kdim par(xi) "
          f"|z|=1  ang.err(xi)  ang.err(even)  pt.err(xi)  pt.err(ker)")
    scan = []
    for M in Mlist:
        K = 2 * M + 1
        T = toeplitz(tvals, M)
        E, O = even_odd_blocks(tvals, M)
        evT, UT = mp.eigsy(T)
        ev = sorted([evT[i] for i in range(K)])
        eps = ev[0]
        gap = ev[1] - ev[0] if K > 1 else mp.mpf("nan")
        scale = max(abs(x) for x in ev)
        tol = max(scale, mp.mpf(1)) * mp.mpf(10) ** (-mp.dps + 12)
        kdim = sum(1 for x in ev if abs(x) < tol)
        idx = min(range(K), key=lambda i: evT[i])
        xi = mp.matrix(K, 1)
        for i in range(K):
            xi[i] = UT[i, idx]
        # parity
        pe = mp.mpf(0); po = mp.mpf(0)
        for i in range(K):
            pe += abs(xi[i] - xi[K - 1 - i]) ** 2
            po += abs(xi[i] + xi[K - 1 - i]) ** 2
        pres = mp.sqrt(min(pe, po))
        nrm = mp.sqrt(sum(abs(xi[i]) ** 2 for i in range(K)))
        parity = ("even" if pe < po else "odd") if pres < nrm * mp.mpf("1e-8") else "MIXED"

        roots = poly_roots_of(xi, K)
        onc = [r for r in roots if abs(abs(r) - 1) < mp.mpf("1e-8")]
        got = [float(mp.arg(r)) for r in onc]
        err = angle_match(true_angles, got)
        reg = ("under" if K < div.R else "exact-rk" if K == div.R
               else "critical" if K == div.R + 1 else "over")
        perr = point_err(true_z, roots)
        # the kernel vector (eigenvalue closest to zero): equals xi only when T >= 0
        jk = min(range(K), key=lambda i: abs(evT[i]))
        xik = mp.matrix(K, 1)
        for i in range(K):
            xik[i] = UT[i, jk]
        rk = poly_roots_of(xik, K)
        kerr = point_err(true_z, rk)
        # CCM work blockwise: the minimal eigenvector of the EVEN block, lifted
        evE, UE = mp.eigsy(E)
        je = min(range(M + 1), key=lambda i: evE[i])
        xie = mp.matrix(K, 1)
        xie[M] = UE[0, je]
        for j in range(1, M + 1):
            xie[M + j] = xie[M - j] = UE[j, je] / mp.sqrt(2)
        re_ = poly_roots_of(xie, K)
        eerr = angle_match(true_angles,
                           [float(mp.arg(r)) for r in re_ if abs(abs(r) - 1) < mp.mpf("1e-8")])
        evO = sorted(mp.eigsy(O, eigvals_only=True)) if M else []
        f3 = lambda v: ("   n/a  " if v is None else f"{v:.3e}")
        print(f"    {M} {K:3d}  {reg:<8} {ns(eps,8):>15} {ns(min(evE),7):>14} "
              f"{ns(min(evO),7) if evO else 'n/a':>13}  {kdim:^4} {parity:<5}  "
              f"{len(onc):>2}/{len(roots):<3} {f3(err)}    {f3(eerr)}     {f3(perr)}   {f3(kerr)}")
        scan.append(dict(M=M, K=K, regime=reg, eps=eps, gap=gap, kdim=kdim, parity=parity,
                         T=T, xi=xi, roots=roots, err=err, perr=perr, kerr=kerr, ev=ev,
                         xik=xik, rootsk=rk, evkzero=evT[jk], xie=xie, eerr=eerr,
                         evE=sorted(evE), evO=evO))
    # even/odd block check and Cantoni-Butler
    for s in scan:
        M, K = s["M"], s["K"]
        allev = sorted(s["evE"] + s["evO"])
        d = max(abs(a - b) for a, b in zip(allev, s["ev"]))
        if M == structure_at:
            check(f"M={M}: spec(T) = spec(even block) u spec(odd block) (Cantoni-Butler)",
                  d < mp.mpf(10) ** (-mp.dps + 12), f"max |diff| = {ns(d,3)}")
            lo_e = s["evE"][0]
            lo_o = s["evO"][0] if s["evO"] else mp.mpf("inf")
            obs(f"M={M}: even-simple (CCM Def. even-simple: min spec T is simple and even)",
                lo_e <= lo_o and (len(s["evE"]) < 2 or abs(s["evE"][1] - lo_e) > 1e-12),
                f"min even = {ns(lo_e,6)}, min odd = {ns(lo_o,6)}, "
                f"2nd even = {ns(s['evE'][1],6) if len(s['evE'])>1 else 'n/a'}")
    return scan, tvals, true_angles

def structure_checks(M, T, tvals):
    """Displacement ranks: position basis (Toeplitz) and DFT basis (Loewner)."""
    K = 2 * M + 1
    F = dft_matrix(M)
    Fh = herm(F)
    S, Z = shift_matrices(M)
    tau = F * T * Fh
    d1 = T - Z * T * herm(Z)
    d2 = herm(Z) * T * Z - T
    s1 = mat_rank_svals(d1)
    s2 = mat_rank_svals(d2)
    check(f"M={M}: T - Z T Z^* has rank 2 (Toeplitz displacement, cyclic shift)",
          s1[2] < 1e-9 * max(s1[0], 1), f"singular values {s1[0]:.3e} {s1[1]:.3e} {s1[2]:.3e}")
    check(f"M={M}: Z^* T Z - T has rank 2",
          s2[2] < 1e-9 * max(s2[0], 1), f"singular values {s2[0]:.3e} {s2[1]:.3e} {s2[2]:.3e}")
    G = mp.matrix(K, K)
    H = mp.matrix(K, K)
    W = mp.matrix(K, K)
    for ni in range(K):
        n = ni - M
        zn = mp.exp(2j * mp.pi * n / K)
        sn = mp.tan(mp.pi * n / K)
        for mi in range(K):
            m = mi - M
            zm = mp.exp(2j * mp.pi * m / K)
            sm = mp.tan(mp.pi * m / K)
            G[ni, mi] = (zn - zm) * tau[ni, mi]
            H[ni, mi] = (sn - sm) * tau[ni, mi]
            W[ni, mi] = 2 * mp.pi * (n - m) / K * tau[ni, mi]
    sg = mat_rank_svals(G)
    sh = mat_rank_svals(H)
    sw = mat_rank_svals(W)
    obs(f"M={M}: (2 pi n/K - 2 pi m/K) tau_nm has rank 2 (would make tau Loewner for the LINEAR "
        f"nodes of variant (b))", (len(sw) < 3 or sw[2] < 1e-9 * max(sw[0], 1)),
        f"singular values {sw[0]:.3e} {sw[1]:.3e} " + (f"{sw[2]:.3e}" if len(sw) > 2 else ""))
    check(f"M={M}: (z_n - z_m) tau_nm has rank 2 (multiplicative Loewner in the DFT basis)",
          sg[2] < 1e-9 * max(sg[0], 1), f"singular values {sg[0]:.3e} {sg[1]:.3e} {sg[2]:.3e}")
    check(f"M={M}: (tan(pi n/K) - tan(pi m/K)) tau_nm has rank 2 (additive Loewner, Cayley nodes)",
          sh[2] < 1e-9 * max(sh[0], 1), f"singular values {sh[0]:.3e} {sh[1]:.3e} {sh[2]:.3e}")
    # is the second vector of the rank-two anti-Hermitian H proportional to all-ones?
    A = to_np(H)
    U, sv, Vh = np.linalg.svd(A)
    basis = Vh[:2].conj().T          # column space of H^* ; span{U,V} of |U><V| - |V><U|
    ones = np.ones(K) / np.sqrt(K)
    proj = basis @ (basis.conj().T @ ones)
    resid = np.linalg.norm(ones - proj)
    cay = np.array([complex((1 - 1j * mp.tan(mp.pi * (n - M) / K))
                            * mp.exp(-2j * mp.pi * (n - M) * M / K)) for n in range(K)])
    cay = cay / np.linalg.norm(cay)
    residc = np.linalg.norm(cay - basis @ (basis.conj().T @ cay))
    print(f"  [info] M={M}: distance to span(U,V) of the rank-2 additive displacement: "
          f"all-ones {resid:.3e}, (-1)^n sec(pi n/K) {residc:.3e}")
    return F


def lemma_key_checks(M, T0, eps, tvals, xi, F):
    """The two hypotheses of CCM Lemma key in their discrete form, for T = tau - eps (which is
    again Toeplitz, is >= 0, and kills xi: lags >= 1 are unchanged, only t_0 is shifted)."""
    K = 2 * M + 1
    T = mp.matrix(K, K)
    for i in range(K):
        for j in range(K):
            T[i, j] = T0[i, j] - (eps if i == j else 0)
    nrm = mp.sqrt(sum(abs(T[i, j]) ** 2 for i in range(K) for j in range(K)))
    res = fnorm(T * xi) / max(nrm, mp.mpf(10) ** (-mp.dps))
    if res > mp.mpf("1e-12"):
        print(f"  [info] M={M}: (tau - eps) xi != 0 (residual {ns(res,3)}); "
              f"Lemma key hypotheses do not apply, only the determinant identity does.")
        return
    S, Z = shift_matrices(M)
    nx = mp.sqrt(sum(abs(xi[i]) ** 2 for i in range(K)))
    if abs(xi[K - 1]) < nx * mp.mpf("1e-12"):
        obs(f"M={M}: CCM normalisation <eta|xi> = 1 available for the multiplicative variant",
            False, f"xi_M = {ns(xi[K-1],3)} vanishes (degenerate kernel), so D' = D - |D xi><eta| "
                   f"is undefined for eta = delta at the window edge")
        return
    # (a) multiplicative:  T S xi = -c,  c_j = t_{M+1-j}
    x = mp.matrix(K, 1)
    for i in range(K):
        x[i] = xi[i] / xi[K - 1]                       # normalise xi_M = <e_top|xi> = 1
    c = mp.matrix(K, 1)
    for i in range(K):
        c[i] = tvals[K - i]                            # beta_j = t_{M+1-j}, j = -M..M
    d = fnorm(T * (S * x) + c) / max(fnorm(c), fnorm(T))
    obs(f"M={M}: Lemma key (i), multiplicative: (tau-eps) S xi = -beta, beta_j = t_(M+1-j) "
        f"(needs the lag t_(2M+1), one beyond the window, so it holds only when xi-hat "
        f"vanishes on the divisor itself)", d < mp.mpf("1e-12"), f"relative residual {ns(d,3)}")
    # (b) additive (Cayley nodes): with beta := -Q D xi and eta the displacement vector,
    #     does D Q - Q D = |beta><eta| - |eta><beta| hold exactly?
    Fh = herm(F)
    tau = F * T * Fh                                   # T is already tau - eps here
    D = mp.matrix(K, K)
    eta = mp.matrix(K, 1)
    for ni in range(K):
        n = ni - M
        D[ni, ni] = mp.tan(mp.pi * n / K)
        eta[ni] = (1 - 1j * mp.tan(mp.pi * n / K)) * mp.exp(-2j * mp.pi * n * M / K)
    xh = F * xi
    ip = mp.mpc(0)
    for i in range(K):
        ip += mp.conj(eta[i]) * xh[i]
    if abs(ip) < nx * mp.mpf("1e-12"):
        obs(f"M={M}: CCM normalisation <eta|xi> = 1 available for the additive/Cayley variant",
            False, f"<eta|xi> = {ns(abs(ip),3)} vanishes: eta is even under gamma and xi is odd, "
                   f"so the whole additive family (a3, b, c1, c2, d) is undefined")
        return
    for i in range(K):
        xh[i] = xh[i] / ip                              # <eta|xi> = 1
    beta = -(tau * (D * xh))
    H = D * tau - tau * D
    R = mp.matrix(K, K)
    for i in range(K):
        for j in range(K):
            R[i, j] = H[i, j] - (beta[i] * mp.conj(eta[j]) - eta[i] * mp.conj(beta[j]))
    d2 = fnorm(R) / max(fnorm(H), fnorm(tau))
    check(f"M={M}: Lemma key (i), additive/Cayley: D tauq - tauq D = |beta><eta| - |eta><beta| "
          f"with beta = -tauq D xi, tauq = tau - eps",
          d2 < mp.mpf("1e-12"), f"relative residual {ns(d2,3)}")
    bx = mp.mpc(0)
    for i in range(K):
        bx += mp.conj(beta[i]) * xh[i]
    check(f"M={M}: <beta|xi> = 0 (CCM's parity hypothesis, additive/Cayley variant)",
          abs(bx) < mp.mpf("1e-12") * max(fnorm(beta), mp.mpf(1)), f"|<beta|xi>| = {ns(abs(bx),3)}")
    # everything downstream of Lemma key: TD' Hermitian, i.e. D'' selfadjoint for tau - eps
    Dp = mp.matrix(K, K)
    Dx = D * xh
    for i in range(K):
        for j in range(K):
            Dp[i, j] = D[i, j] - Dx[i] * mp.conj(eta[j])
    TD = tau * Dp
    d3 = fnorm(TD - herm(TD)) / max(fnorm(TD), fnorm(tau))
    check(f"M={M}: Lemma key (ii), additive/Cayley: (tau - eps) D' is Hermitian, so D'' is "
          f"selfadjoint on the quotient", d3 < mp.mpf("1e-12"), f"relative residual {ns(d3,3)}")
    # (c) task variant (a): cyclic shift with eta = all ones has a xi-independent spectrum
    ones = mp.matrix(K, 1)
    for i in range(K):
        ones[i] = 1
    sm = mp.mpc(0)
    for i in range(K):
        sm += xi[i]
    if abs(sm) > mp.mpf("1e-20"):
        y = mp.matrix(K, 1)
        for i in range(K):
            y[i] = xi[i] / sm
        Zy = Z * y
        Ap = mp.matrix(K, K)
        for i in range(K):
            for j in range(K):
                Ap[i, j] = Z[i, j] - Zy[i]
        ev = sorted(np.linalg.eigvals(to_np(Ap)), key=lambda z: abs(z))[1:]
        pred = [complex(mp.exp(2j * mp.pi * n / K)) for n in range(1, K)]
        dd = multiset_dist(pred, ev)
        check(f"M={M}: variant (a3) spectrum is the nontrivial K-th roots of unity, "
              f"independent of xi",
              dd < 1e-9, f"max distance {dd:.3e} (so eta = all-ones in the position basis "
                         f"carries no information)")

# ---------------------------------------------------------------------------------- driver

def run_object(name, Mlist, dps, do_variants=True):
    print("\n" + "=" * 100)
    print(f"OBJECT: {name}")
    print("=" * 100)
    if name == "pauli":
        # P(u) = 1 + 2u + 5u^2 = prod(1 - alpha u) => alpha^2 + 2 alpha + 5 = 0, alpha = -1 +- 2i
        div = curve_divisor("pauli", 5, [1, 2, 5])
        print("  Pauli-qubit / elliptic-curve-over-F_5 zeta  Z(u) = (1+2u+5u^2)/((1-u)(1-5u))")
        print("  graded sign: retained points are ZEROS, Weil form = (trivial) - (rings),")
        print("  t^nt_k = q^{k/2} + q^{-k/2} - N_k q^{-k/2},  N_n = 1 + q^n - sum alpha^n.")
        Ns = []
        for n in range(0, 2 * max(Mlist) + 3):
            s = mp.mpc(0)
            for a, m in div.retained:
                s += m * a ** n
            Ns.append(1 + mp.mpf(5) ** n - mp.re(s))
        print("  ring norms N_n, n=1..6:", [ns(Ns[n], 8) for n in range(1, 7)])
        check("N_1 = 8 (the elliptic curve over F_5 has 8 points, a_5 = -2)",
              abs(Ns[1] - 8) < mp.mpf("1e-20"), f"N_1 = {ns(Ns[1],10)}")
        # cross-check the sequence built from N_n against the direct sum
        worst = mp.mpf(0)
        for k in range(0, 2 * max(Mlist) + 2):
            lhs = mp.mpf(5) ** (mp.mpf(k) / 2) + mp.mpf(5) ** (-mp.mpf(k) / 2) - Ns[k] * mp.mpf(5) ** (-mp.mpf(k) / 2)
            worst = max(worst, abs(lhs - mp.re(div.t_direct(k))))
        check("t^nt from the ring norms vs the direct sum over the zeros",
              worst < mp.mpf(10) ** (-mp.dps + 10), f"max_k |diff| = {ns(worst,3)}")
        scan, tvals, true_angles = analyse(div, Mlist, structure_at=1)
    else:
        nv, edges = GRAPHS[name]
        A = adjacency(nv, edges)
        B, de = hashimoto(nv, edges)
        deg = A.sum(axis=1)
        regular = len(set(deg.tolist())) == 1
        print(f"  |V| = {nv}, |E| = {len(edges)}, degrees {sorted(set(deg.tolist()))}, "
              f"|directed edges| = {len(de)}, regular = {regular}")
        w = check_ihara_bass(nv, edges, A, B)
        check("Ihara-Bass det(1-uB) = (1-u^2)^{|E|-|V|} det(I - Au + Qu^2) at 3 random u",
              w < 1e-8, f"max relative error = {w:.3e}")
        kmax = 2 * max(Mlist) + 2
        traces = trace_powers(B, kmax)
        if len(edges) <= 21:
            kc = min(7, kmax)
            counts, prim = prime_cycle_table(B, kc)
            ok = all(counts[k] == traces[k] for k in range(1, kc + 1))
            check("N_k = Tr B^k vs direct enumeration of closed non-backtracking cyclic walks",
                  ok, f"k=1..{kc}: {[counts[k] for k in range(1,kc+1)]} vs "
                      f"{[traces[k] for k in range(1,kc+1)]}")
            ok2 = all(traces[k] == sum(d * prim[d] for d in range(1, k + 1) if k % d == 0)
                      for k in range(1, kc + 1))
            check("N_k = sum_{d | k} d * (#prime cycles of length d)", ok2,
                  f"prime cycle counts by length 1..{kc}: {[prim[k] for k in range(1,kc+1)]}")
        if regular:
            div, q, bip, lam = regular_divisor(name, nv, edges, A, B, traces)
            # lambda_2 = max |lambda| over the NONTRIVIAL multiset: one copy of q+1 (and one of
            # -(q+1) if bipartite) is trivial; any further copy is a nontrivial eigenvalue.
            rest = []
            for v, m in lam:
                mm = m - (1 if abs(v - (q + 1)) < mp.mpf("1e-20") else 0) \
                       - (1 if (bip and abs(v + (q + 1)) < mp.mpf("1e-20")) else 0)
                if mm > 0:
                    rest.append(abs(float(mp.re(v))))
            lam2 = max(rest) if rest else 0.0
            print(f"  adjacency spectrum: "
                  + ", ".join(f"{ns(mp.re(v),8)}^{m}" for v, m in
                              sorted(lam, key=lambda p: -float(mp.re(p[0])))))
            print(f"  max |lambda| over the nontrivial multiset = {lam2:.8f},  "
                  f"2 sqrt q = {float(2*mp.sqrt(q)):.8f}  -> "
                  f"{'Ramanujan' if lam2 <= float(2*mp.sqrt(q))+1e-12 else 'NOT Ramanujan'}")
        else:
            div = irregular_divisor(name, nv, edges, B, traces)
        # Hashimoto spectrum cross-check
        pred = []
        for v, m in div.trivial + div.retained:
            pred += [complex(v)] * m
        got = np.linalg.eigvals(B.astype(float))
        pred.sort(key=lambda z: (round(z.real, 8), round(z.imag, 8)))
        gl = sorted(got, key=lambda z: (round(z.real, 8), round(z.imag, 8)))
        d = max(abs(a - b) for a, b in zip(pred, gl)) if len(pred) == len(gl) else float("inf")
        check("spec(B) = trivial u retained (Ihara-Bass prediction vs numpy eig(B))",
              d < 1e-7, f"{len(pred)} vs {len(gl)} eigenvalues, max deviation = {d:.3e}")
        scan, tvals, true_angles = analyse(div, Mlist, structure_at=(div.R // 2))

    precision_probe(div, tvals, scan)
    # structure + variants at the critical window (and one over-resolved window)
    if do_variants:
        Mcrit = div.R // 2
        targets = [s for s in scan if s["M"] in (Mcrit, Mcrit + 1, max(1, Mcrit - 1))]
        for s in targets:
            M = s["M"]
            if M == 0:
                continue
            print(f"\n  -- structure and perturbed-operator variants at M = {M} "
                  f"(K = {s['K']}, regime {s['regime']}, eps = {ns(s['eps'],6)})")
            F = structure_checks(M, s["T"], tvals)
            lemma_key_checks(M, s["T"], s["eps"], tvals, s["xi"], F)
            ops, etas = variant_operators(M, F)
            run_variants(M, s["T"], s["eps"], s["xi"], true_angles, s["roots"], ops, etas)
            if s["parity"] != "even":
                print(f"    (xi_min is {s['parity']}; CCM diagonalise the even block, so repeat "
                      f"with the minimal EVEN eigenvector, eps_even = {ns(min(s['evE']),6)})")
                run_variants(M, s["T"], min(s["evE"]), s["xie"], true_angles,
                             poly_roots_of(s["xie"], s["K"]), ops, etas)
    return div, scan


def offcircle_block_probe(rs=(1.2, -1.2, 1.6, -1.6), Ms=(1, 2, 3, 4, 5)):
    """A single off-circle reciprocal pair {r, 1/r} (times critr), nothing else: which parity
    block of the Toeplitz form carries the negative eigenvalue?"""
    print("    a single off-circle reciprocal pair {x, 1/x}, t_k = x^|k| + x^-|k|:")
    print("    (B(f,f) = 2 f^(x) f^(1/x); f even => f^(1/z) = f^(z) => B >= 0, f odd => B <= 0,")
    print("     so an off-circle pair makes the ODD block negative and leaves the even block PSD)")
    print("      x       M   eps_even        eps_odd       block carrying min")
    for x in rs:
        for M in Ms:
            tv = [mp.mpf(x) ** k + mp.mpf(x) ** (-k) for k in range(2 * M + 2)]
            E, O = even_odd_blocks(tv, M)
            ee = min(mp.eigsy(E, eigvals_only=True))
            eo = min(mp.eigsy(O, eigvals_only=True)) if M else mp.mpf("inf")
            print(f"      {x:<6}  {M}  {ns(ee,8):>14}  {ns(eo,8):>13}   "
                  f"{'even' if ee <= eo else 'odd'}")


def precision_probe(div, tvals, scan):
    """Repeat the Toeplitz eigenproblem in float64 and compare with the mpmath result, to say
    where double precision is enough and where it is not."""
    print("    double (float64) vs mpmath for the same windows:")
    print("      M    eps(mpmath)        eps(float64)      |d eps|    max |d root|   cond(T)")
    for s in scan:
        M, K = s["M"], s["K"]
        if M == 0:
            continue
        T = np.array([[float(tvals[abs(i - j)]) for j in range(K)] for i in range(K)])
        w, V = np.linalg.eigh(T)
        xi = V[:, 0]
        r64 = np.roots(xi[::-1]) if abs(xi[-1]) > 1e-13 else np.array([])
        rmp = [complex(r) for r in s["roots"]]
        dr = max(min(abs(a - b) for b in r64) for a in rmp) if (len(r64) and rmp) \
            else float("nan")
        cond = abs(w).max() / max(abs(w).min(), 1e-300)
        print(f"      {M:<4} {ns(s['eps'],9):>16} {w[0]:>17.9e}  {abs(float(s['eps']) - w[0]):.2e}"
              f"   {dr:.3e}     {cond:.2e}")


def pisarenko_test(ntrial=200, seed=20260918):
    """The discrete analogue of CCM's reality theorem, tested on arbitrary real even Toeplitz
    matrices (no positivity, no divisor): the minimal eigenvector's polynomial z^M xi-hat(z)
    has all 2M roots on the unit circle, and S'' = its companion matrix is a (T - eps)-isometry."""
    rng = np.random.default_rng(seed)
    worst_r = 0.0
    worst_i = 0.0
    nskip = 0
    for _ in range(ntrial):
        M = int(rng.integers(1, 7))
        K = 2 * M + 1
        t = rng.normal(size=K + 1)
        T = np.array([[t[abs(i - j)] for j in range(K)] for i in range(K)])
        w, V = np.linalg.eigh(T)
        xi = V[:, 0]
        if abs(xi[-1]) < 1e-9:
            nskip += 1
            continue
        xi = xi / xi[-1]
        r = np.roots(xi[::-1])
        worst_r = max(worst_r, float(np.max(np.abs(np.abs(r) - 1))))
        S = np.diag(np.ones(K - 1), -1)
        Ap = S - np.outer(S @ xi, np.eye(K)[K - 1])
        Tq = T - w[0] * np.eye(K)
        worst_i = max(worst_i, float(np.linalg.norm(Ap.T @ Tq @ Ap - Tq) / np.linalg.norm(Tq)))
    check("randomised: for an ARBITRARY real even Toeplitz T (no positivity, no divisor) the "
          "minimal eigenvector's polynomial has all roots on |z| = 1",
          worst_r < 1e-8, f"{ntrial} trials ({nskip} skipped for xi_M = 0), "
                          f"max ||root| - 1| = {worst_r:.3e}")
    check("randomised: S'^T (T - eps) S' = T - eps (the multiplicative Lemma key, which needs "
          "only Toeplitz structure and (T-eps) xi = 0)",
          worst_i < 1e-8, f"max relative residual = {worst_i:.3e}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--graph", default=None)
    ap.add_argument("--M", type=int, default=None)
    ap.add_argument("--dps", type=int, default=40)
    ap.add_argument("--Mmax", type=int, default=5)
    args = ap.parse_args()
    mp.dps = args.dps
    names = [args.graph] if args.graph else (list(GRAPHS.keys()) + ["pauli"])
    Mlist = [args.M] if args.M is not None else list(range(0, args.Mmax + 1))
    print(f"ihara_proto: discrete CCM construction for Ihara zetas. dps = {mp.dps}, "
          f"windows M = {Mlist}")
    print("Convention: window {-M..M}, K = 2M+1, T_{jj'} = t^nt_{j-j'}, "
          "t^nt_k = sum_retained (mu/critr)^{|k|} (even = Hermitian = literal two-sided).")
    print("\n--- generic sanity tests, no graph involved ---")
    pisarenko_test()
    offcircle_block_probe()
    for nm in names:
        try:
            ml = Mlist
            if args.M is None and nm in MSCAN_EXTRA:
                ml = list(range(0, max(args.Mmax, MSCAN_EXTRA[nm]) + 1))
            run_object(nm, ml, args.dps)
        except Exception as exc:              # keep the log going
            import traceback
            print(f"  [FAIL] {nm}: {exc}")
            traceback.print_exc()
            FAILURES.append(f"{nm}: {exc}")
    print("\n" + "=" * 100)
    if FAILURES:
        print(f"{len(FAILURES)} FAILING CHECKS:")
        for f in FAILURES:
            print("  -", f)
    else:
        print("all checks PASS")

if __name__ == "__main__":
    main()
