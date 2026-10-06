#!/usr/bin/env python3
"""Checks for 'A Dirichlet character of F_q(t)' (notes/adelic-gkp/ff-dirichlet.md), lane J, 2026-10-06.

K = F_q(t), q = p prime, A = F_q[t]. f = prod P_i (monic irreducible, distinct), chi = prod_i (./P_i)_N, the N-th power-residue symbol,
(a/P)_N = a^((Q-1)/N) mod P in mu_N(F_q), sent to C by g_q^j -> exp(2 pi i j/(q-1)) for a fixed generator g_q of F_q^x.
L(u, chi) = sum_{m monic} chi(m) u^deg m; Lambda = L (chi odd, i.e. non-trivial on F_q^x) or L/(1-u) (chi even).
Additive character: psi = prod_v psi_v, psi_v(x) = psi0(Res_v(x dt)), psi0(a) = exp(2 pi i a/p); trivial on K by the residue theorem.
  finite v: psi_v unramified (d_v = 0), psi_P(a/P) = psi0(coef of t^(deg P - 1) in a mod P);
  v = inf (pi = 1/t, dt = -pi^-2 dpi): psi_inf(x) = psi0(-x_1), conductor P^2, d_inf = -2.
Self-dual measures: vol(O_v) = q_v^(-d_v/2): 1 at finite places, q at infinity. Gate F Phi(y) = int Phi(x) psi(xy) dx; squeeze D_c f(x) = |c|^(1/2) f(cx).
Idele character: chi_Q(uniformiser) = chi(Q) at unramified Q; chi_P = conj(chi_i) on O_P^x at P_i | f; chi_inf = chi on F_q^x, chi_inf(1/t) = 1.
Local states: Phi_P = chi_i 1_(O_P^x) (charged), Phi_inf = conj(chi_inf) 1_(O^x) (odd) or 1_(O_inf) (even), 1_(O_v) elsewhere (qunaught, phase 1).
Lattice: E = Q(zeta_N)[x]/(P_chi), P_chi(x) = x^n Lambda(1/x); R = Z[zeta_N][F, V] with V = q/F; sigma: zeta -> 1/zeta, F -> V;
Omega_+(x, y) = Tr_(E/Q)(x sigma(y)/(V - F)) (the form of cone-bridge.md); Weil form 1/2 Omega(x, (F - V) y).
Needs python-flint, mpmath, numpy, sympy, PARI/GP (/usr/bin/gp). Runs in well under two minutes.
"""
import itertools
import math
import subprocess
from fractions import Fraction as Fr

import flint
import mpmath as mp
import numpy as np

mp.mp.dps = 50

def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a

def pmul(a, b, p):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] = (r[i + j] + x * y) % p
    return trim(r)

def pmod(a, m, p):            # m monic
    a = [x % p for x in a]
    dm = len(m) - 1
    for i in range(len(a) - 1, dm - 1, -1):
        c = a[i]
        if c:
            for j in range(dm + 1):
                a[i - dm + j] = (a[i - dm + j] - c * m[j]) % p
    return trim(a[:dm])

def monics(k, p):
    for digs in itertools.product(range(p), repeat=k):
        yield list(digs) + [1]

def is_irred(f, p):
    d = len(f) - 1
    for k in range(1, d // 2 + 1):
        for g in monics(k, p):
            if not pmod(f, g, p):
                return False
    return True

def irreducibles(k, p):
    return [f for f in monics(k, p) if is_irred(f, p)]

def fq_gen(p):
    for g in range(2, p + 1):
        if g % p and len({pow(g, i, p) for i in range(p - 1)}) == p - 1:
            return g % p
    return 1   # p = 2

class Place:
    """the finite place P (monic irreducible over F_p): log table of (A/P)^x and the N-th power residue symbol"""
    def __init__(self, P, p, N):
        self.P, self.p, self.N = P, p, N
        self.k = len(P) - 1
        self.Q = p ** self.k
        g_q = fq_gen(p)
        self.logq = {pow(g_q, i, p): i for i in range(p - 1)}
        for cand in itertools.product(range(p), repeat=self.k):
            c = trim(cand)
            if not c:
                continue
            tab, x = {}, [1]
            for e in range(self.Q - 1):
                key = tuple(x + [0] * (self.k - len(x)))
                if key in tab:
                    break
                tab[key] = e
                x = pmod(pmul(x, c, p), P, p)
            if len(tab) == self.Q - 1:
                self.log, self.gamma = tab, c
                break
        # gamma^((Q-1)/(q-1)) is a generator of F_q^x: its discrete log l0 w.r.t. g_q
        e = (self.Q - 1) // (p - 1)
        c0 = None
        for key, ee in tab.items():
            if ee == e:
                c0 = key[0]
        assert all(v == 0 for v in [k for k, ee in tab.items() if ee == e][0][1:])
        self.l0 = self.logq[c0]
        assert (self.p - 1) % N == 0

    def key(self, a):
        r = pmod(a, self.P, self.p)
        return tuple(r + [0] * (self.k - len(r)))

    def chi(self, a):
        """exponent e with (a/P)_N = zeta_N^e under g_q^j -> exp(2 pi i j/(q-1)); None if P | a"""
        kk = self.key(a)
        if not any(kk):
            return None
        return (self.l0 * self.log[kk]) % self.N

class Char:
    """chi = prod_i (./P_i)_N^{s_i} on (A/f)^x, f = prod P_i"""
    def __init__(self, Ps, p, N, s=None):
        self.p, self.N = p, N
        self.places = [Place(P, p, N) for P in Ps]
        self.s = s or [1] * len(Ps)
        f = [1]
        for P in Ps:
            f = pmul(f, P, p)
        self.f, self.d = f, len(f) - 1

    def comp(self, i, a):
        e = self.places[i].chi(a)
        return None if e is None else (self.s[i] * e) % self.N

    def __call__(self, a):
        tot = 0
        for i in range(len(self.places)):
            e = self.comp(i, a)
            if e is None:
                return None
            tot += e
        return tot % self.N

    def power(self, j):
        c = Char([pl.P for pl in self.places], self.p, self.N, [(j * s) % self.N for s in self.s])
        return c

def zN(e, N):
    return mp.expjpi(mp.mpf(2) * e / N)

def psi0(a, p):
    return mp.expjpi(mp.mpf(2) * (a % p) / p)

# ---------------- L-function data ----------------
def Lcounts(chi, kmax):
    """S_k as count vectors over exponents mod N, k = 0..kmax"""
    p, N = chi.p, chi.N
    out = []
    for k in range(kmax + 1):
        cnt = [0] * N
        for m in monics(k, p):
            e = chi(m)
            if e is not None:
                cnt[e] += 1
        out.append(cnt)
    return out

def euler_counts(chi, kmax):
    """coefficients of prod_{Q monic irred, Q not | f} (1 - chi(Q) u^deg Q)^-1 to u^kmax, as complex mp numbers"""
    N, p = chi.N, chi.p
    coef = [mp.mpc(1)] + [mp.mpc(0)] * kmax
    for k in range(1, kmax + 1):
        for Qp in irreducibles(k, p):
            e = chi(Qp)
            if e is None:
                continue
            z = zN(e, N)
            # multiply by 1/(1 - z u^k) = sum z^j u^{jk}
            new = coef[:]
            for i in range(kmax + 1):
                j = 1
                while i + j * k <= kmax:
                    new[i + j * k] += coef[i] * z ** j
                    j += 1
            coef = new
    return coef

def cval(cnt, N):
    return mp.fsum([c * zN(e, N) for e, c in enumerate(cnt)]) if N > 2 else mp.mpc(cnt[0] - cnt[1])

def is_even(chi):
    return all(chi([c]) == 0 for c in range(1, chi.p))

def Lambda_counts(chi):
    """the completed L (L for odd chi, L/(1-u) for even chi) as exact count vectors (integers, may be negative)"""
    S = Lcounts(chi, chi.d - 1)
    if is_even(chi):
        out, acc = [], [0] * chi.N
        for cnt in S[:-1]:
            acc = [a + b for a, b in zip(acc, cnt)]
            out.append(acc[:])
        return out, S
    return S, S

def gauss_global(chi):
    """G(chi) = sum_{a mod f} chi(a) psi0(coef of t^{d-1} in a)"""
    p, d, N = chi.p, chi.d, chi.N
    G = mp.mpc(0)
    for digs in itertools.product(range(p), repeat=d):
        a = trim(list(digs))
        e = chi(a) if a else None
        if e is None:
            continue
        G += zN(e, N) * psi0(digs[d - 1], p)
    return G

def gauss_local(chi, i):
    """G_i = sum_{x mod P_i} chi_i(x) psi0(coef of t^{k_i-1} in x): the gate-phase Gauss sum at P_i"""
    pl = chi.places[i]
    p, N, k = chi.p, chi.N, pl.k
    G = mp.mpc(0)
    for digs in itertools.product(range(p), repeat=k):
        a = trim(list(digs))
        if not a:
            continue
        G += zN(chi.comp(i, a), N) * psi0(digs[k - 1], p)
    return G

def gauss_inf(chi):
    """g = sum_{c in F_q^x} chi(c) psi0(c)"""
    return mp.fsum([zN(chi([c]), chi.N) * psi0(c, chi.p) for c in range(1, chi.p)])

# ---------------- local gate phases ----------------

def local_phase_P(chi, i):
    """eps_P(1/2) = chi_P(P) * G_i / sqrt(Q), with chi_P(P) = prod_{j != i} chi_j(P_i) (product formula)"""
    pl = chi.places[i]
    e = 0
    for j in range(len(chi.places)):
        if j != i:
            e += chi.comp(j, pl.P)
    lam = gauss_local(chi, i) / mp.sqrt(pl.Q)
    return zN(e % chi.N, chi.N) * lam, lam, e % chi.N

def local_phase_inf(chi):
    if is_even(chi):
        return mp.mpc(1)
    return mp.conj(gauss_inf(chi)) / mp.sqrt(chi.p)

def fourier_P_direct(chi, i):
    """F Phi on the shell P^{-1}/O by direct summation, Phi = chi_i * 1_{O^x} (vol O_P = 1, psi_P(x/P) = psi0(coef_{k-1}(x mod P))).
    Returns max |F Phi(b/P) - lam * D_P Phi^vee (b/P)| over all b, with D_P Phi^vee(b/P) = Q^{-1/2} conj(chi_i(b))."""
    pl = chi.places[i]
    p, N, k, Q = chi.p, chi.N, pl.k, pl.Q
    digs = np.array(list(itertools.product(range(p), repeat=k)), dtype=np.int64)   # Q x k, digit j = coeff of t^j
    # Hankel form: coef_{k-1}(t^{a+b} mod P)
    H = np.zeros((k, k), dtype=np.int64)
    for a in range(k):
        for b in range(k):
            r = pmod([0] * (a + b) + [1], pl.P, p)
            r = r + [0] * (k - len(r))
            H[a, b] = r[k - 1]
    E = (digs @ H @ digs.T) % p
    chiv = np.zeros(Q, dtype=complex)
    for idx, dg in enumerate(digs):
        a = trim(list(dg))
        if a:
            chiv[idx] = np.exp(2j * np.pi * chi.comp(i, a) / N)
    FPhi = (np.exp(2j * np.pi * E / p) @ chiv) / Q          # vol(x + P) = 1/Q
    lam = complex(gauss_local(chi, i)) / math.sqrt(Q)
    target = lam * np.conj(chiv) / math.sqrt(Q)               # D_P Phi^vee(b/P) = |P|^{1/2} Phi^vee(b), Phi^vee = conj(chi_i) 1_{O^x}
    return float(np.max(np.abs(FPhi - target))), float(abs(FPhi[0]))

def fourier_inf_direct(chi):
    """F Phi_inf on P^{-1}/P^3 by direct summation over x in O/P^3 (vol O_inf = q), psi_inf(x) = psi0(-x_1) (residue of x dt, dt = -pi^-2 dpi).
    odd chi: Phi = conj(chi_inf) 1_{O^x}; target lam * D_{1/pi} Phi^vee, D_{1/pi}Phi^vee(y) = sqrt(q) chi(y_1) 1_{v(y)=1}.
    even chi: Phi = 1_O; target D_{pi^-2} 1_O = q 1_{P^2}."""
    p, N = chi.p, chi.N
    odd = not is_even(chi)
    X = np.array(list(itertools.product(range(p), repeat=3)), dtype=np.int64)      # x0,x1,x2
    Y = np.array(list(itertools.product(range(p), repeat=4)), dtype=np.int64)      # y_-1, y0, y1, y2
    coef1 = (np.outer(X[:, 0], Y[:, 2]) + np.outer(X[:, 1], Y[:, 1]) + np.outer(X[:, 2], Y[:, 0])) % p
    chic = {c: np.exp(2j * np.pi * chi([c]) / N) for c in range(1, p)}
    Phi = np.array([(np.conj(chic[x0]) if x0 else 0) if odd else 1 for x0 in X[:, 0]], dtype=complex)
    FPhi = (Phi @ np.exp(-2j * np.pi * coef1 / p)) * p / p ** 3
    if odd:
        lam = complex(local_phase_inf(chi))
        target = np.array([lam * math.sqrt(p) * chic[y[2]] if (y[0] == 0 and y[1] == 0 and y[2]) else 0 for y in Y])
    else:
        target = np.array([p if (y[0] == 0 and y[1] == 0 and y[2] == 0) else 0 for y in Y], dtype=complex)
    return float(np.max(np.abs(FPhi - target)))

def tate_ratio_P(chi, i, s):
    """Z(F Phi, chi_P^{-1}, 1-s) / Z(Phi, chi_P, s) from the shell values: Q^{1-s} chi_P(P) mean_u[F Phi(u/P) chi_i(u)].
    F Phi(u/P) is recomputed by its own finite sum for each u; the mean is over the first 41 units u (the summand is constant in u)."""
    pl = chi.places[i]
    Q, N = pl.Q, chi.N
    G = gauss_local(chi, i)
    eps, lam, e = local_phase_P(chi, i)
    tot = mp.mpc(0)
    cnt = 0
    for digs in itertools.product(range(chi.p), repeat=pl.k):
        u = trim(list(digs))
        if not u:
            continue
        cu = chi.comp(i, u)
        FPhi = mp.mpc(0)
        for digs2 in itertools.product(range(chi.p), repeat=pl.k):
            x = trim(list(digs2))
            if not x:
                continue
            xu = pmod(pmul(x, u, chi.p), pl.P, chi.p)
            c = xu[pl.k - 1] if len(xu) >= pl.k else 0
            FPhi += zN(chi.comp(i, x), N) * psi0(c, chi.p)
        FPhi /= Q
        tot += FPhi * zN(cu, N)
        cnt += 1
        if cnt > 40:
            break
    return mp.power(Q, 1 - s) * zN(e, N) * tot / cnt

def tate_ratio_inf(chi, s):
    p = chi.p
    if is_even(chi):
        # Phi = 1_O, F Phi = q 1_{P^2}; ratio * L(s)/L(1-s), L(s) = 1/(1 - q^-s), chi_inf(pi) = 1
        Z1 = 1 / (1 - mp.power(p, -s))
        Z2 = p * mp.power(p, -2 * (1 - s)) / (1 - mp.power(p, -(1 - s)))
        return (Z2 / Z1) * (Z1 / (1 / (1 - mp.power(p, -(1 - s)))))
    g = gauss_inf(chi)
    # F Phi(pi u) = chi(-u0) conj... computed by the finite sum, mean over u0 of F Phi(pi u0) conj(chi(u0))
    tot = mp.mpc(0)
    for u0 in range(1, p):
        FPhi = mp.fsum([mp.conj(zN(chi([x0]), chi.N)) * psi0(-x0 * u0, p) for x0 in range(1, p)])
        tot += FPhi * mp.conj(zN(chi([u0]), chi.N))
    return mp.power(p, -(1 - s)) * tot / (p - 1)

# ---------------- the lattice (Deligne module) ----------------

def cyclo(N):
    import sympy
    return [int(c) for c in reversed(sympy.Poly(sympy.cyclotomic_poly(N, sympy.Symbol('z'))).all_coeffs())]

def reduce_cyc(cnt, N):
    """sum cnt[e] zeta^e as an integer vector of length phi(N) (basis 1, zeta, ..)"""
    Phi = cyclo(N)
    ph = len(Phi) - 1
    a = list(cnt) + [0] * max(0, ph - len(cnt))
    for i in range(len(a) - 1, ph - 1, -1):
        c = a[i]
        if c:
            for j in range(ph + 1):
                a[i - ph + j] -= c * Phi[j]
    return a[:ph]

def mat_power(M, k):
    D = M.nrows()
    R = flint.fmpq_mat(D, D, [1 if i == j else 0 for i in range(D) for j in range(D)])
    for _ in range(k):
        R = R * M
    return R

def ident(D):
    return flint.fmpq_mat(D, D, [1 if i == j else 0 for i in range(D) for j in range(D)])

def trace(M):
    return sum((M[i, i] for i in range(M.nrows())), flint.fmpq(0))

class Lattice:
    """E = Q(zeta_N)[x]/(P_chi), basis zeta^a x^b (index b*phi + a); R = Z[zeta][F,V] by HNF; sigma: zeta -> 1/zeta, F -> V = q/F"""
    def __init__(self, coeffs, N, q):
        # coeffs[k] = c_k in Z[zeta] (integer vectors), Lambda(u) = sum c_k u^k, P_chi(x) = sum c_k x^{n-k}
        self.N, self.q = N, q
        Phi = cyclo(N)
        ph = len(Phi) - 1
        n = len(coeffs) - 1
        self.n, self.ph, self.D = n, ph, n * ph
        D = self.D
        Zp = [[0] * ph for _ in range(ph)]          # multiplication by zeta on Z[zeta]
        for a in range(ph):
            if a + 1 < ph:
                Zp[a + 1][a] = 1
            else:
                for j in range(ph):
                    Zp[j][a] = -Phi[j]
        self.Zp = flint.fmpq_mat(Zp)
        def mult_by(c):                            # c in Z[zeta] as matrix on Z[zeta]
            R = flint.fmpq_mat(ph, ph)
            for j, cj in enumerate(c):
                R = R + cj * mat_power(self.Zp, j)
            return R
        Mz = [[0] * D for _ in range(D)]
        MF = [[0] * D for _ in range(D)]
        for b in range(n):
            for a in range(ph):
                for a2 in range(ph):
                    Mz[b * ph + a2][b * ph + a] = int(self.Zp[a2, a])
            if b + 1 < n:
                for a in range(ph):
                    MF[(b + 1) * ph + a][b * ph + a] = 1
            else:
                for b2 in range(n):
                    C = mult_by(coeffs[n - b2])
                    for a in range(ph):
                        for a2 in range(ph):
                            MF[b2 * ph + a2][b * ph + a] = -int(C[a2, a])
        self.Mz, self.MF = flint.fmpq_mat(Mz), flint.fmpq_mat(MF)
        self.MV = q * self.MF.inv()
        self.Mzi = self.Mz.inv()
        e0 = flint.fmpq_mat(D, 1, [1] + [0] * (D - 1))
        self.e0 = e0
        # sigma
        cols = []
        for b in range(n):
            for a in range(ph):
                cols.append(mat_power(self.Mzi, a) * mat_power(self.MV, b) * e0)
        self.S = flint.fmpq_mat(D, D, [cols[j][i, 0] for i in range(D) for j in range(D)])
        # the order R = Z[zeta][F, V]
        gens = []
        for a in range(ph):
            for b in range(n + 1):
                for c in range(n + 1):
                    v = mat_power(self.Mz, a) * mat_power(self.MF, b) * mat_power(self.MV, c) * e0
                    gens.append([v[i, 0] for i in range(D)])
        den = 1
        for g in gens:
            for x in g:
                den = den * x.q // math.gcd(den, int(x.q))
        rows = flint.fmpz_mat([[int(x * den) for x in g] for g in gens]).hnf()
        basis = [[rows[i, j] for j in range(D)] for i in range(rows.nrows()) if any(rows[i, j] != 0 for j in range(D))]
        assert len(basis) == D
        self.B = flint.fmpq_mat(D, D, [flint.fmpq(basis[j][i], den) for i in range(D) for j in range(D)])
        self.Bi = self.B.inv()
        self.index = 1 / abs(self.B.det())                 # [R : Z[zeta][F]]
        # forms in the power basis
        mats = []
        for b in range(n):
            for a in range(ph):
                mats.append(mat_power(self.Mz, a) * mat_power(self.MF, b))
        smats = []
        for b in range(n):
            for a in range(ph):
                smats.append(mat_power(self.Mzi, a) * mat_power(self.MV, b))
        Delta = (self.MV - self.MF).inv()
        self.Tsig = flint.fmpq_mat(D, D, [trace(mats[i] * smats[j]) for i in range(D) for j in range(D)])
        self.Om = flint.fmpq_mat(D, D, [trace(mats[i] * smats[j] * Delta) for i in range(D) for j in range(D)])

    def in_R(self, M):
        X = self.Bi * M * self.B
        return all(X[i, j].q == 1 for i in range(self.D) for j in range(self.D)), X


# =================================================================================================
npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


def gp(script):
    r = subprocess.run(["gp", "-q", "-f"], input="default(colors,\"no\");\n" + script + "\nquit\n",
                       capture_output=True, text=True, timeout=300)
    out = {}
    for line in r.stdout.splitlines():
        if line.startswith("@"):
            k, v = line[1:].split(" ", 1)
            out[k] = v.strip()
    return out


def digits(err):
    return -math.log10(max(float(err), 1e-300))


def pstr(P):
    terms = []
    for i in range(len(P) - 1, -1, -1):
        if P[i]:
            c = "" if (P[i] == 1 and i > 0) else (str(P[i]) + ("*" if i > 0 else ""))
            terms.append(c + ("t^%d" % i if i > 1 else ("t" if i == 1 else "")))
    return "+".join(terms)


def zstr(v, N):
    """integer vector in Z[zeta_N] as a string (z = zeta_N)"""
    if N == 2:
        return str(v[0])
    parts = []
    for j, c in enumerate(v):
        if c:
            parts.append(("%d" % c) + ("" if j == 0 else ("z" if j == 1 else "z^%d" % j)))
    return "(" + "+".join(parts).replace("+-", "-") + ")" if parts else "0"


EXAMPLES = [
    # label, q, N, list of P_i (low -> high), predicted c in y^N = c f
    ("X1", 5, 4, [[1, 1, 0, 1]], -1),
    ("X2", 5, 4, [[0, 1], [2, 0, 1]], -1),
    ("X3", 7, 3, [[1, 0, 0, 1, 1]], 1),
    ("X4", 7, 3, [[1, 1, 0, 1]], 1),
    ("X5", 7, 2, [[1, 1, 0, 1]], -1),
    ("X6", 3, 2, [[1, 0, 1, 1, 1]], 1),
]

DATA = {}
print("== A  the L-functions L(u, chi) = sum over monic m of chi(m) u^deg m: degree, Euler product, RH, functional equation, Gauss sum")
for lab, q, N, Ps, c_pred in EXAMPLES:
    chi = Char(Ps, q, N)
    d, even = chi.d, is_even(chi)
    for P in Ps:
        assert is_irred(P, q)
    S = Lcounts(chi, d + 1)
    Sv = [cval(x, N) for x in S]
    Lam, _ = Lambda_counts(chi)
    co = [reduce_cyc(x, N) for x in Lam]
    c = [cval(x, N) for x in Lam]
    n = len(c) - 1
    vanish = max(abs(Sv[d]), abs(Sv[d + 1])) < 1e-40
    if even:
        degok = abs(mp.fsum(Sv[:d])) < 1e-40 and abs(c[n]) > 0.5 and n == d - 2
    else:
        degok = abs(Sv[d - 1]) > 0.5 and n == d - 1
    desc = "even (trivial on F_q^x), Lambda = L/(1-u)" if even else "odd (non-trivial on F_q^x), Lambda = L"
    fstr = "*".join("(" + pstr(P) + ")" for P in Ps)
    check(f"A1 {lab} q={q}, N={N}, f={fstr} (deg {d}): chi = power-residue symbol is {desc}; S_d = S_(d+1) = 0, Lambda a polynomial of degree {n}",
          vanish and degok, "Lambda coefficients in Z[z]: " + ", ".join(zstr(v, N) for v in co))
    eu = euler_counts(chi, d)
    erre = max(abs(eu[k] - Sv[k]) for k in range(d + 1))
    check(f"A2 {lab} the Euler product over monic irreducibles Q prime to f, prod (1 - chi(Q) u^deg Q)^-1, equals the sum over monics to u^{d}",
          erre < 1e-40, f"max error {mp.nstr(erre, 3)}")
    roots = mp.polyroots([c[k] for k in range(n + 1)], maxsteps=200, extraprec=200) if n > 1 else [-c[1]]
    # roots of P_chi(x) = sum c_k x^(n-k)  (reciprocal roots alpha of Lambda)
    rh = max(abs(abs(r) - mp.sqrt(q)) for r in roots)
    check(f"A3 {lab} RH: the {n} reciprocal roots alpha of Lambda have |alpha| = sqrt(q)",
          rh < 1e-40, "|alpha|/sqrt q - 1 <= " + mp.nstr(rh / mp.sqrt(q), 3) + "; arg(alpha)/pi = " + ", ".join(mp.nstr(mp.arg(r) / mp.pi, 6) for r in roots))
    WL = c[n] / mp.power(q, mp.mpf(n) / 2)
    fe = lambda W: max(abs(c[k] - W * mp.power(q, k - mp.mpf(n) / 2) * mp.conj(c[n - k])) for k in range(n + 1)) / mp.power(q, mp.mpf(n) / 2)
    G = gauss_global(chi)
    g = gauss_inf(chi)
    WG = G / mp.power(q, mp.mpf(d) / 2) if even else (G / mp.power(q, mp.mpf(d) / 2)) / (g / mp.sqrt(q))
    check(f"A4 {lab} functional equation Lambda(u) = W (sqrt(q) u)^{n} conj(Lambda)(1/(qu)) with W = (top coefficient)/q^(n/2); fails with -W",
          fe(WL) < 1e-40 and fe(-WL) > 0.1 and abs(abs(WL) - 1) < 1e-40,
          f"W = {mp.nstr(WL, 15)}, |W| - 1 = {mp.nstr(abs(WL) - 1, 2)}; residual {mp.nstr(fe(WL), 2)} ({'exact' if fe(WL) == 0 else '%.0f digits' % digits(fe(WL))}); with -W {mp.nstr(fe(-WL), 3)}")
    gtxt = "G(chi)/q^(d/2)" if even else "[G(chi)/q^(d/2)] / [g(chi|F_q^x)/sqrt q]"
    check(f"A5 {lab} root number from Gauss sums, W = {gtxt}, G(chi) = sum_(a mod f) chi(a) psi0(coef_(d-1) a), g = sum_(c in F_q^x) chi(c) psi0(c)",
          abs(WG - WL) < 1e-40, f"G = {mp.nstr(G, 12)} (|G|^2 = {mp.nstr(abs(G) ** 2, 12)}), W_G - W = {mp.nstr(abs(WG - WL), 2)} ({digits(abs(WG - WL)):.0f} digits)")
    DATA[lab] = dict(chi=chi, q=q, N=N, d=d, even=even, n=n, co=co, c=c, WL=WL, roots=roots, c_pred=c_pred, Ps=Ps)

print("== B  the gate phases: local Fourier gate on the local states, local epsilon factors, product = W")
for lab in DATA:
    D_ = DATA[lab]
    chi, q, N, n = D_["chi"], D_["q"], D_["N"], D_["n"]
    eps, Nexp = [], 0
    for i, pl in enumerate(chi.places):
        err, at0 = fourier_P_direct(chi, i)
        e, lam, echi = local_phase_P(chi, i)
        rat = [tate_ratio_P(chi, i, s) / (e * mp.power(pl.Q, mp.mpf(0.5) - s)) - 1 for s in (mp.mpf(0.5), mp.mpc(0.3, 0.7), mp.mpc(1.7, -0.4))]
        check(f"B1 {lab} place P = {pstr(pl.P)} (Q = {pl.Q}): F(chi_P 1_(O^x)) = lam_P D_P(conj chi_P 1_(O^x)) on P^-1/O, lam_P = G_P/sqrt Q; "
              f"Tate ratio = eps_P N_P^(1/2-s), N_P = Q",
              err < 1e-12 and max(abs(r) for r in rat) < 1e-40,
              f"Fourier residual {err:.1e}; lam_P = {mp.nstr(lam, 10)}, chi_P(P) = z^{echi}, eps_P = {mp.nstr(e, 10)}; Tate residual {mp.nstr(max(abs(r) for r in rat), 2)}")
        eps.append(e)
        Nexp += pl.k
    errinf = fourier_inf_direct(chi)
    einf = local_phase_inf(chi)
    ainf = 0 if D_["even"] else 1
    rat = [tate_ratio_inf(chi, s) / (einf * mp.power(q, (ainf - 2) * (mp.mpf(0.5) - s))) - 1 for s in (mp.mpf(0.5), mp.mpc(0.3, 0.7), mp.mpc(1.7, -0.4))]
    if D_["even"]:
        txt = "qunaught 1_O: F 1_O = D_(pi^-2) 1_O (squeeze by the different of dt), eps_inf = chi_inf(pi^-2) = 1, N_inf = q^-2"
    else:
        txt = "charged conj(chi_inf) 1_(O^x): F Phi = lam_inf D_(1/pi) Phi^vee, eps_inf = conj(g)/sqrt q, N_inf = q^-1"
    check(f"B2 {lab} place inf ({'unramified' if D_['even'] else 'tamely ramified'}): {txt}",
          errinf < 1e-12 and max(abs(r) for r in rat) < 1e-40,
          f"Fourier residual on P^-1/P^3 {errinf:.1e}; eps_inf = {mp.nstr(einf, 10)}; Tate residual {mp.nstr(max(abs(r) for r in rat), 2)}")
    eps.append(einf)
    Nexp += ainf - 2
    W = mp.fprod(eps)
    dW = abs(W - D_["WL"])
    check(f"B3 {lab} product of the local phases = W from the L-polynomial; conductor exponent sum_v (a_v + d_v) deg v = deg f + a_inf - 2 = {Nexp} = deg Lambda",
          dW < 1e-40 and Nexp == n, "phases " + " * ".join(mp.nstr(e, 8) for e in eps) + f" = {mp.nstr(W, 12)}; |prod - W| = {mp.nstr(dW, 2)} ({digits(dW):.0f} digits)")
    c = D_["c"]
    Lam = lambda u, cc: mp.fsum([cc[k] * mp.power(u, k) for k in range(n + 1)])
    cb = [mp.conj(x) for x in c]
    errs = [abs(Lam(u, c) - W * mp.power(mp.sqrt(q) * u, n) * Lam(1 / (q * u), cb)) / abs(Lam(u, c)) for u in (mp.mpc(0.3, 0.2), mp.mpc(-0.7, 0.45), mp.mpc(0.11, -1.3))]
    check(f"B4 {lab} Tate's global functional equation assembled from local data: Lambda(u) = (prod eps_v) (sqrt q u)^(sum log_q N_v) conj(Lambda)(1/(qu)) at 3 points",
          max(errs) < 1e-40, f"max relative error {mp.nstr(max(errs), 2)}")
    DATA[lab]["eps"] = eps

# composite case: CRT factorisation of the global Gauss sum
chi = DATA["X2"]["chi"]
G = gauss_global(chi)
G1, G2 = gauss_local(chi, 0), gauss_local(chi, 1)
P1, P2 = chi.places[0].P, chi.places[1].P
fac = zN(chi.comp(0, P2) + chi.comp(1, P1), 4) * G1 * G2
check("B5 X2 the global Gauss sum factorises over the two charged places: G(chi) = chi_1(P_2) chi_2(P_1) G_1 G_2; the factors chi_j(P_i) are the values chi_(P_i)(P_i) of the "
      "ramified local characters on their own uniformisers (product formula)", abs(G - fac) < 1e-40,
      f"G = {mp.nstr(G, 12)}, product {mp.nstr(fac, 12)}")

# the place at infinity of X1 against the quartic Dirichlet character mod 5 (gate-phases.md D3)
chi = DATA["X1"]["chi"]
tauD = mp.fsum([zN({1: 0, 2: 1, 4: 2, 3: 3}[c], 4) * mp.expjpi(mp.mpf(2) * c / 5) for c in range(1, 5)])   # chi_D(2) = i
WD = tauD / (mp.mpc(0, 1) * mp.sqrt(5))
restr = [chi([c]) for c in range(1, 5)]
check("B8 X1 chi restricted to F_5^x is conj(chi_D), chi_D the quartic Dirichlet character mod 5 with chi_D(2) = i; eps_inf(X1) = conj(g)/sqrt 5 = -tau(chi_D)/sqrt 5 = -i W(chi_D), "
      "W(chi_D) = tau(chi_D)/(i sqrt 5) the root number over Q", restr == [0, 3, 1, 2] and abs(DATA["X1"]["eps"][-1] + mp.mpc(0, 1) * WD) < 1e-40 and abs(WD - mp.mpc(0.85065080835, 0.52573111212)) < 1e-9,
      f"chi(c) = z^{restr} for c = 1..4; W(chi_D) = {mp.nstr(WD, 12)}; eps_inf = {mp.nstr(DATA['X1']['eps'][-1], 12)}")

# census
print("== B'  census: every monic irreducible f (and every product deg 1 x deg 2 for q = 5, N = 4); chi = power-residue symbol")
import random
random.seed(1)
census = [(5, 4, 3, None), (5, 4, 4, None), (7, 3, 3, None), (7, 3, 4, 60), (7, 2, 3, None), (3, 2, 4, None), (5, 2, 3, None)]
for q, N, d, samp in census:
    Fs = irreducibles(d, q)
    if samp:
        Fs = random.sample(Fs, samp)
    worst, rhw, cnt_even, nW = 0, 0, 0, set()
    for f in Fs:
        chi = Char([f], q, N)
        Lam, _ = Lambda_counts(chi)
        c = [cval(x, N) for x in Lam]
        n = len(c) - 1
        WL = c[n] / mp.power(q, mp.mpf(n) / 2)
        W = local_phase_P(chi, 0)[0] * local_phase_inf(chi)
        worst = max(worst, abs(W - WL))
        roots = mp.polyroots(c, maxsteps=200, extraprec=100) if n > 1 else [-c[1]]
        rhw = max([rhw] + [abs(abs(r) - mp.sqrt(q)) for r in roots])
        cnt_even += is_even(chi)
        nW.add(mp.nstr(WL, 6))
    check(f"B6 census q={q}, N={N}, deg f={d}: {len(Fs)} irreducible f{' (random sample)' if samp else ''}; RH and prod_v eps_v = W for every one",
          worst < 1e-40 and rhw < 1e-40, f"{cnt_even} even, {len(Fs) - cnt_even} odd; max |prod eps - W| {mp.nstr(worst, 2)}; max ||alpha| - sqrt q| {mp.nstr(rhw, 2)}; {len(nW)} distinct W")
worst, cnt = 0, 0
for P1 in irreducibles(1, 5):
    for P2 in irreducibles(2, 5):
        chi = Char([P1, P2], 5, 4)
        Lam, _ = Lambda_counts(chi)
        c = [cval(x, 4) for x in Lam]
        n = len(c) - 1
        WL = c[n] / mp.power(5, mp.mpf(n) / 2)
        W = local_phase_P(chi, 0)[0] * local_phase_P(chi, 1)[0] * local_phase_inf(chi)
        Wnaive = local_phase_P(chi, 0)[1] * local_phase_P(chi, 1)[1] * local_phase_inf(chi)
        worst = max(worst, abs(W - WL))
        cnt += abs(Wnaive - WL) > 1e-20
check("B7 census q=5, N=4, f = P_1 P_2 (deg 1 x deg 2), 50 pairs: prod eps_v = W for all; dropping the factors chi_(P_i)(P_i) breaks it for some",
      worst < 1e-40 and cnt > 0, f"max |prod eps - W| {mp.nstr(worst, 2)}; without chi_P(P): wrong for {cnt} of 50")

print("== C  the lattice: R = Z[zeta][F, V] in E = Q(zeta)[x]/(P_chi), sigma, Omega_+ = Tr(x sigma(y)/(V - F)), Weil form, vacuum")
for lab in DATA:
    D_ = DATA[lab]
    q, N, n, co = D_["q"], D_["N"], D_["n"], D_["co"]
    L = Lattice(co, N, q)
    D = L.D
    okF, MR = L.in_R(L.MF)
    okV, VR = L.in_R(L.MV)
    okz, ZR = L.in_R(L.Mz)
    comp_ok = all(L.MV[i, j].q == 1 for i in range(D) for j in range(D))
    WL = D_["WL"]
    Wtxt = mp.nstr(WL, 8)
    check(f"C1 {lab} rank {n} over Z[z_{N}], {D} over Z: F, V = qF^-1 and zeta preserve R; MV = q on R; companion lattice Z[z][F] V-stable: {comp_ok}; [R : Z[z][F]] = {L.index}",
          okF and okV and okz and (MR * VR == q * ident(D)) and ((L.index == 1) == comp_ok), f"W = {Wtxt}")
    sig_ok = (L.S * L.MF * L.S.inv() == L.MV) and (L.S * L.Mz * L.S.inv() == L.Mzi) and (L.S * L.S == ident(D))
    check(f"C2 {lab} sigma: zeta -> zeta^-1, F -> V is a well-defined involutive ring automorphism of E (this is the functional equation)", sig_ok)
    Om = L.Om
    alt = Om.transpose() == -Om and all(Om[i, i] == 0 for i in range(D))
    simil = L.MF.transpose() * Om * L.MF == q * Om
    zinv = L.Mz.transpose() * Om * L.Mz == Om
    OmR = L.B.transpose() * Om * L.B
    den = 1
    for i in range(D):
        for j in range(D):
            den = den * OmR[i, j].q // math.gcd(den, int(OmR[i, j].q))
    OmI = [[int(OmR[i, j] * den) for j in range(D)] for i in range(D)]
    gg = 0
    for row in OmI:
        for x in row:
            gg = math.gcd(gg, x)
    OmI = [[x // gg for x in row] for row in OmI]
    snf = flint.fmpz_mat(OmI).snf()
    inv = [int(snf[i, i]) for i in range(D)]
    check(f"C3 {lab} Omega_+ is alternating, zeta-invariant, a q-similitude of F; on R its denominator is {den}; the primitive integral multiple has elementary divisors {inv}",
          alt and simil and zinv, f"det = {math.prod(inv)}")
    weil = Om * (L.MF - L.MV) == L.Tsig
    lead = []
    for k in range(1, D + 1):
        sub = flint.fmpq_mat(k, k, [L.Tsig[i, j] for i in range(k) for j in range(k)])
        lead.append(sub.det())
    posdef = all(x > 0 for x in lead)
    check(f"C4 {lab} Weil form 1/2 Omega_+(x, (F - V) y) = 1/2 Tr_(E/Q)(x sigma(y)) exactly, and it is positive definite (exact leading minors)",
          weil and posdef, "minors " + ", ".join(str(x) for x in lead))
    # sigma = complex conjugation in every embedding: |alpha|^2 = q for all Galois conjugates
    # numerical vacuum in the basis of R
    M = np.array([[float(MR[i, j]) for j in range(D)] for i in range(D)])
    V = np.array([[float(VR[i, j]) for j in range(D)] for i in range(D)])
    Z = np.array([[float(ZR[i, j]) for j in range(D)] for i in range(D)])
    Omn = np.array(OmI, dtype=float)
    A = M + V
    ev, P = np.linalg.eig(A)
    band = float(np.max(np.abs(ev.imag))) < 1e-9 and float(np.max(np.abs(ev.real))) < 2 * math.sqrt(q)
    fA = (P @ np.diag((4 * q - ev ** 2) ** -0.5) @ np.linalg.inv(P)).real
    J = (M - V) @ fA
    G_ = Omn @ J
    e1 = np.max(np.abs(J @ J + np.eye(D)))
    e2 = max(np.max(np.abs(J @ M - M @ J)), np.max(np.abs(J @ Z - Z @ J)))
    e3 = np.max(np.abs(G_ - G_.T))
    mineig = float(np.min(np.linalg.eigvalsh((G_ + G_.T) / 2)))
    check(f"C5 {lab} vacuum J = (F - V)(4q - (F+V)^2)^(-1/2) on R: spectrum of F+V real in (-2 sqrt q, 2 sqrt q); J^2 = -1, JF = FJ, J zeta = zeta J, Omega J symmetric positive",
          band and e1 < 1e-9 and e2 < 1e-9 and e3 < 1e-9 and mineig > 0,
          f"|J^2+1| {e1:.1e}, commutators {e2:.1e}, asym {e3:.1e}, min eig of Omega J {mineig:.3g}")
    # charpoly over Z = product of Galois conjugates; ordinary?
    cp = L.MF.charpoly()
    cpl = [int(cp.coeffs()[k]) for k in range(D + 1)]          # low -> high
    prod = [mp.mpc(1)]
    jlist = [j for j in range(1, N) if math.gcd(j, N) == 1] if N > 1 else [1]
    for j in jlist:
        chij = D_["chi"].power(j)
        Lj, _ = Lambda_counts(chij)
        cj = [cval(x, N) for x in Lj]
        Pj = list(reversed(cj))                                 # low -> high in x
        new = [mp.mpc(0)] * (len(prod) + len(Pj) - 1)
        for a_, x in enumerate(prod):
            for b_, y in enumerate(Pj):
                new[a_ + b_] += x * y
        prod = new
    perr = max(abs(prod[k] - cpl[k]) for k in range(D + 1))
    mid = cpl[D // 2]
    p_ = q
    check(f"C6 {lab} charpoly_Z(F) on R = prod over j in (Z/N)^x of P_(chi^j) (each L(u, chi^j) recomputed from its own character sums): {cpl[::-1]}; "
          f"middle coefficient {mid} {'prime to' if mid % p_ else 'divisible by'} p = {p_}",
          perr < 1e-30, f"ordinary: {mid % p_ != 0}; residual {mp.nstr(perr, 2)}")
    DATA[lab].update(L=L, cp=cpl, OmI=OmI, inv=inv)

# control: a polynomial with the functional equation but without RH
Lc = Lattice([[1], [-6], [5]], 2, 5)
lead = [Lc.Tsig[0, 0], Lc.Tsig.det()]
check("C7 control: x^2 - 6x + 5 (roots 1 and 5, q = 5; functional equation yes, RH no): sigma still exists, Omega_+ still a similitude, but Tr(x sigma(y)) is indefinite",
      (Lc.S * Lc.MF * Lc.S.inv() == Lc.MV) and (Lc.MF.transpose() * Lc.Om * Lc.MF == 5 * Lc.Om) and not (lead[0] > 0 and lead[1] > 0),
      f"leading minors {lead[0]}, {lead[1]}")

# the root number is the normalised determinant of the step on the chi-part
worst = 0
for lab in DATA:
    D_ = DATA[lab]
    detF = mp.fprod(D_["roots"])
    worst = max(worst, abs((-1) ** D_["n"] * detF / mp.power(D_["q"], mp.mpf(D_["n"]) / 2) - D_["WL"]))
check("C8 all six: W = (-1)^n det_(Q(zeta))(F) / q^(n/2), the root number is the phase of the determinant of the step on the chi-part; over Z the determinant is q^(D/2)",
      worst < 1e-40 and all(abs(int(DATA[l]["L"].MF.det())) == DATA[l]["q"] ** (DATA[l]["L"].D // 2) for l in DATA), f"max error {mp.nstr(worst, 2)}")

print("== D  the cover y^N = c f(t): its zeta numerator is the product of the L(u, chi^j), j = 1..N-1; the chi-part is a factor")


def count_points(q, N, f, cc, r):
    F = flint.fq_default_ctx(q, r)
    Qr = q ** r
    e = (Qr - 1) // N
    tot = 0
    for dg in itertools.product(range(q), repeat=r):
        t = F(list(dg))
        w = F(0)
        for coef in reversed(f):
            w = w * t + F(coef)
        w = w * F(cc % q)
        if w.is_zero():
            tot += 1
        elif (w ** e).is_one():
            tot += N
    d = len(f) - 1
    if d % N == 0:
        u = F(cc % q)
        tot += N if (u ** e).is_one() else 0
    elif math.gcd(d, N) == 1:
        tot += 1
    return tot


def numerator_from_counts(q, g, Ns):
    s = [None] + [q ** r + 1 - Ns[r - 1] for r in range(1, g + 1)]
    e = [Fr(1)]
    for k in range(1, g + 1):
        e.append(sum(((-1) ** (i - 1)) * e[k - i] * s[i] for i in range(1, k + 1)) / k)
    a = [((-1) ** k) * e[k] for k in range(g + 1)]                # P(u) = sum a_k u^k
    full = a + [None] * g
    for k in range(g + 1, 2 * g + 1):
        full[k] = q ** (k - g) * a[2 * g - k]
    return [int(x) for x in full]


def prod_all_chars(D_):
    N, chi = D_["N"], D_["chi"]
    prod = [mp.mpc(1)]
    for j in range(1, N):
        Lj, _ = Lambda_counts(chi.power(j))
        cj = [cval(x, N) for x in Lj]
        new = [mp.mpc(0)] * (len(prod) + len(cj) - 1)
        for a_, x in enumerate(prod):
            for b_, y in enumerate(cj):
                new[a_ + b_] += x * y
        prod = new
    return prod


def polydiv_exact(a, b):          # integer polys low -> high; returns (quotient, remainder) over Q
    a = [Fr(x) for x in a]
    qd = [Fr(0)] * (len(a) - len(b) + 1)
    for i in range(len(a) - len(b), -1, -1):
        qd[i] = a[i + len(b) - 1] / b[-1]
        for j in range(len(b)):
            a[i + j] -= qd[i] * b[j]
    return qd, a


for lab in DATA:
    D_ = DATA[lab]
    q, N, d, f = D_["q"], D_["N"], D_["d"], D_["chi"].f
    g = (N - 1) * (d - 2) // 2 if d % N == 0 else (N - 1) * (d - 1) // 2
    prod = prod_all_chars(D_)
    target = [int(mp.nint(x.real)) for x in prod]
    tdev = max(abs(x - y) for x, y in zip(prod, target))
    res = {}
    for cc in (D_["c_pred"], D_["c_pred"] * fq_gen(q)):          # control: times a non-N-th power (an unramified twist)
        if N == 2:
            o = gp(f"P=hyperellcharpoly(Mod({cc % q},{q})*({pstr(f).replace('t', 'x')})); print(\"@cp \",Vec(P));")
            cpv = [int(x) for x in o["cp"].strip("[]").split(",")]
            num = cpv                                             # charpoly x^2g + ... = coefficients of the numerator, reversed order
        else:
            Ns = [count_points(q, N, f, cc, r) for r in range(1, g + 1)]
            num = numerator_from_counts(q, g, Ns)
        res[cc] = num
    ok_pred = res[D_["c_pred"]] == target
    other = [k for k in res if k != D_["c_pred"]][0]
    ok_other = res[other] != target
    # chi-part divides: charpoly of F on R (Z-polynomial, x-form) divides the x-form numerator
    numx = list(reversed(res[D_["c_pred"]]))                       # low -> high in x
    qd, rem = polydiv_exact(numx, D_["cp"])
    divides = all(x == 0 for x in rem)
    how = "hyperellcharpoly" if N == 2 else f"point counts over F_(q^r), r <= {g}"
    check(f"D1 {lab} cover y^{N} = {D_['c_pred']}*f, genus {g} ({how}): zeta numerator = prod_(j=1..{N - 1}) Lambda(u, chi^j) = {target}; "
          f"with c = {other % q} (a non-{N}-th power times the predicted c) it is not (the twist u -> zeta u)",
          ok_pred and ok_other and tdev < 1e-30, f"c = {other % q} gives {res[other]}")
    check(f"D2 {lab} the chi-part (charpoly of F on R, degree {D_['L'].D}) divides the numerator: the lattice is H_1 of a factor of Jac(y^{N} = {D_['c_pred']} f) of dimension {D_['L'].D // 2}",
          divides, "cofactor " + str([int(x) for x in qd]))

# N = 4: the chi^2-part is the elliptic curve y^2 = c f
for lab in ("X1", "X2"):
    D_ = DATA[lab]
    chi2 = D_["chi"].power(2)
    L2, _ = Lambda_counts(chi2)
    c2 = [int(cval(x, 4).real) for x in L2]
    o = gp(f"P=hyperellcharpoly(Mod({D_['c_pred'] % 5},5)*({pstr(D_['chi'].f).replace('t', 'x')})); print(\"@cp \",Vec(P));")
    cpv = [int(x) for x in o["cp"].strip("[]").split(",")]
    check(f"D3 {lab} the quadratic character chi^2 gives the elliptic curve y^2 = {D_['c_pred']}*f: Lambda(u, chi^2) = {c2}, hyperellcharpoly {cpv}",
          cpv == c2)

# the phases cancel in the zeta of the cover
txt, worst = [], 0
for lab in DATA:
    D_ = DATA[lab]
    Ws = []
    for j in range(1, D_["N"]):
        Lj, _ = Lambda_counts(D_["chi"].power(j))
        cj = [cval(x, D_["N"]) for x in Lj]
        Ws.append(cj[-1] / mp.power(D_["q"], mp.mpf(len(cj) - 1) / 2))
    worst = max(worst, abs(mp.fprod(Ws) - 1))
    txt.append(lab + ": " + " * ".join(mp.nstr(w, 6) for w in Ws))
check("D4 all six: prod_(j=1..N-1) W(chi^j) = 1, the root number of the cover's zeta (a curve: +1); the phases of the chi-parts cancel in the product",
      worst < 1e-40, "; ".join(txt) + f"; max |prod - 1| {mp.nstr(worst, 2)}")

print(f"\n{npass} of {npass + nfail} pass")
