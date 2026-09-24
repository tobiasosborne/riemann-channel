#!/usr/bin/env python3
"""rtp1_calibration.py -- lane B2.2 of RTP-1 (`notes/rtp-round-1/brief.md`): the calibration case.

Author line: claude:opus.  Lane file: `notes/rtp-round-1/lane-B2.md`.  Output:
`outputs/rtp1_calibration.txt` (run from the repository root:
`python3 scripts/rtp1_calibration.py > outputs/rtp1_calibration.txt 2>&1`).
Deterministic (seed 20260924 drives the one random graph; the accepted draw is printed), no timestamps,
no memory addresses.  Every claim is an assertion through the single helper `check(cond, msg)` (style
of scripts/gl1_bond.py), which counts, prints one line and never aborts.

WHAT IS COMPUTED.  The analogue of lane A1's two protocols on finite transfer operators for which the
metric is known and "RH" is a theorem (the retained spectrum lies on the critical circle):
  * the permutation (1 2)(3 4 5) and the Petersen graph of scripts/weil_window_extension.py (shard 08g,
    prop:extension-disc, num:weil-window-extension), whose numbers are reproduced first;
  * a random cubic graph on 40 vertices (configuration model, seed 20260924, first simple draw), certified
    Ramanujan here by exact arithmetic (integer characteristic polynomial, certified root isolation).
Window form (shard 08g, def:window-extension-set): the Toeplitz matrix T_K = (nu_{|j-k|})_{j,k=0..K} of
the rescaled traces nu_k = q^{-k/2} (Tr B^k - trivial_k), B the Hashimoto (non-backtracking) matrix;
for a permutation nu_k = Tr P^k.  For a (q+1)-regular graph with V vertices and E edges (Ihara-Bass)
  trivial_k = q^k + 1 + (E - V)(1 + (-1)^k)          (eigenvalues q, 1, and +-1 with multiplicity E - V),
and Tr B^k = sum_{l | k} l pi(l), pi(l) = number of prime (primitive, non-backtracking, tailless) cycle
classes of length l.  The q^k term is the analogue of the pole (the Ihara zeta has its pole at u = 1/q),
the rest of trivial_k the analogue of the archimedean/trivial terms, N_0 = Tr B^0 = 2E the dimension;
all of these are fixed by (q, V) alone: the kinematic data.  The prime data are the pi(l).

PROTOCOLS
  Axis K (window and data together; the analogue of lane A1's CCM axis-x protocol, since the window of
  order K sees exactly the cycles of length <= K): for K = 0, 1, ...: lambda_min(T_K), log det T_K, the
  extension disc of prop:extension-disc for nu_{K+1} (centre c_K, radius e_K = det T_K / det T_{K-1},
  position tau_K of the true next trace), the information Delta I_K = log nu_0 - log e_{K+1} of lane A1's
  Lemma A1.1 (unstructured) and the structured gain Delta I^s_K = log e_K - log e_{K+1} over the disc
  centre (for Toeplitz data the disc IS the structured section, Lemma A1.1' of lane A1), and the overlap
  of the minimal eigenvector with the final one (maximised over the shifts, since the form is shift
  invariant).  The brief calls K "resolution"; for a graph it is the window, and there is no separate
  resolution parameter (the window form is finite-dimensional and exact).  So lane A1's axis N has no
  analogue here, and this is stated in the lane file.
  Data axis (the analogue of lane A1's fixed-L protocol): fixed window K, prime cycles of length <= P
  added for P = 0, 1, ..., K; P = 0 is the kinematic form alone.  Recorded: lambda_min, the number of
  negative eigenvalues, log |det|, the overlap of the minimal eigenvector with the final one.
  Rayleigh decomposition of lambda_min at the final form over dimension / pole / trivial / each cycle length.
  B2.1 on the calibration case (section 6b): the positive set of prime data with the kinematic data fixed; its
  maximum-determinant element (the graph prime number theorem) and its relative error against the window size.

PRECISION.  Traces are exact integers (python-flint fmpz_mat powers of B).  nu_k are arb balls at 600
bits; eigenvalues are certified enclosures (acb_mat.eig, python-flint), so signs and negative counts
are certified; log det and the disc quantities come from a Levinson recursion in mpmath at 180 digits;
eigenvector overlaps and kernel roots in mpmath at 180 digits from the midpoints of the certified
eigenvectors.  Floats printed to 3-5 significant digits.

ZEROS (the graph's spectrum) are used only in the block headed COMPARISON STEP (section 6), and in the
certification that the random graph is Ramanujan (section 2), which reads the adjacency spectrum
only to decide which graph is used, never to build a form.  Runtime about 2.7 minutes (single thread).
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

import inspect
import math
import random

import numpy as np
import mpmath as mp
from flint import fmpz_mat, fmpz_poly, arb, arb_mat, acb_mat, ctx

SEED = 20260924
random.seed(SEED)
np.random.seed(SEED)
ctx.prec = 600
mp.mp.dps = 180

# ---------------------------------------------------------------------------
# the single assertion helper
# ---------------------------------------------------------------------------
_PASS = 0
_FAIL = 0
_FAILED = []


def check(cond, msg):
    """The single assertion helper: counts, prints one line, never aborts."""
    global _PASS, _FAIL
    line = inspect.currentframe().f_back.f_lineno
    ok = bool(cond)
    if ok:
        _PASS += 1
    else:
        _FAIL += 1
        _FAILED.append((line, msg))
    print(f"  {'ok  ' if ok else 'FAIL'} [L{line:4d}]  {msg}")
    return ok


def note(msg):
    print(f"  --           {msg}")


def head(msg):
    print()
    print("=" * 100)
    print(msg)
    print("=" * 100)


def e(x, d=3):
    x = float(x)
    if x == 0:
        return "0"
    return f"{x:.{d}e}"


def f(x, d=4):
    x = float(x)
    s = f"{x:.{d}f}"
    if s.startswith("-") and float(s) == 0:
        s = s[1:]
    return s


def amid(x):
    """mpf from the midpoint of an arb ball"""
    return mp.mpf(x.mid().str(175, radius=False))


# ===========================================================================
head("0. ENVIRONMENT AND PRECISION")
# ===========================================================================
import flint as _flint  # noqa: E402
print(f"  python-flint {_flint.__version__}: exact integers (traces, characteristic polynomials), arb balls at "
      f"{ctx.prec} bits (nu_k, certified eigenvalue enclosures); mpmath {mp.__version__} at {mp.mp.dps} digits "
      f"(Levinson recursion, overlaps, kernel roots)")

# ===========================================================================
head("1. REPRODUCTION OF SHARD 08G (num:weil-window-extension): the extension disc on its two examples")
# ===========================================================================


def levinson(nu, Kmax):
    """Levinson-Durbin on the real Toeplitz data nu[0..Kmax+1] (mpmath).
    Returns per K = 0..Kmax: e_K = det T_K / det T_{K-1} (e_0 = nu_0), the disc centre c_K for nu_{K+1}
    (the one-step predictor) and tau_K = (nu_{K+1} - c_K)/e_K; e_{K+1} = e_K (1 - tau_K^2)."""
    out = []
    a = [mp.mpf(1)]                       # monic predictor polynomial of order K (a_0 = 1)
    eK = mp.mpf(nu[0])
    for K in range(0, Kmax + 1):
        # predictor of nu_{K+1}: c_K = -sum_{j=1..K} a_j nu_{K+1-j}
        c = -mp.fsum(a[j] * nu[K + 1 - j] for j in range(1, K + 1)) if K >= 1 else mp.mpf(0)
        tau = (nu[K + 1] - c) / eK if eK > 0 else mp.nan
        out.append((eK, c, tau))
        if K == Kmax or not eK > 0:
            break
        # reflection coefficient and update to order K+1
        k_ref = -(nu[K + 1] + mp.fsum(a[j] * nu[K + 1 - j] for j in range(1, K + 1))) / eK
        a_new = a + [mp.mpf(0)]
        a = [a_new[j] + k_ref * a_new[K + 1 - j] for j in range(K + 2)]
        eK = eK * (1 - k_ref ** 2)
    return out


# the permutation (1 2)(3 4 5)
perm_cycles = [2, 3]
nu_perm = [sum(l for l in perm_cycles if k % l == 0) if k > 0 else 5 for k in range(12)]
check(nu_perm == [5, 0, 2, 3, 2, 0, 5, 0, 2, 3, 2, 0], f"permutation: Tr P^k = #Fix = {nu_perm}")
lp = levinson([mp.mpf(t) for t in nu_perm], 3)
rad = [lp[K][0] for K in (1, 2, 3)]
check(abs(rad[0] - 5) < 1e-30 and abs(rad[1] - mp.mpf("4.2")) < 1e-30 and abs(rad[2] - mp.mpf("2.0571")) < 1e-4,
      f"permutation: disc radii e_K = det T_K/det T_(K-1) at K = 1, 2, 3: {', '.join(mp.nstr(r, 6) for r in rad)} "
      f"(shard: 5, 4.2, 2.0571)")
check(abs(abs(lp[3][2]) - 1) < 1e-30, f"permutation: at K = 3 the truth nu_4 = 2 is on the boundary (tau_3 = {mp.nstr(lp[3][2], 6)})")
# Petersen
q_p, V_p, E_p = 2, 10, 15
N_pet = [30, 0, 0, 0, 0, 120, 120, 0, 150, 240, 1052, 2640]   # Tr B^k, k = 0..11 (checked below from B)


def petersen_edges():
    outer = [(i, (i + 1) % 5) for i in range(5)]
    inner = [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    spokes = [(i, 5 + i) for i in range(5)]
    return sorted(tuple(sorted(x)) for x in outer + inner + spokes)


def hashimoto(V, E):
    D = [(a, b) for a, b in E] + [(b, a) for a, b in E]
    idx = {d: i for i, d in enumerate(D)}
    n = len(D)
    B = [[0] * n for _ in range(n)]
    for (u, v) in D:
        for w in range(V):
            if (v, w) in idx and w != u:
                B[idx[(u, v)]][idx[(v, w)]] = 1
    return fmpz_mat(B), n


def traces(B, n, K):
    M = fmpz_mat(n, n, [1 if i == j else 0 for i in range(n) for j in range(n)])
    out = [n]
    for _ in range(K):
        M = M * B
        out.append(int(sum(int(M[i, i]) for i in range(n))))
    return out


Bp, npet = hashimoto(V_p, petersen_edges())
Np_calc = traces(Bp, npet, 11)
check(Np_calc[:8] == [30, 0, 0, 0, 0, 120, 120, 0], f"Petersen: Tr B^k from the Hashimoto matrix = {Np_calc[:8]} (shard's values)")
N_pet = Np_calc


def triv(q, V, E, k):
    return q ** k + 1 + (E - V) * (1 + (-1) ** k)


def nu_graph_mp(Nk, q, V, E):
    return [mp.mpf(Nk[k] - triv(q, V, E, k)) / mp.mpf(q) ** (mp.mpf(k) / 2) for k in range(len(Nk))]


nu_pet = nu_graph_mp(N_pet, q_p, V_p, E_p)
lpet = levinson(nu_pet, 3)
radc = [mp.mpf(q_p) ** (mp.mpf(K + 1) / 2) * lpet[K][0] for K in (1, 2, 3)]
check(all(abs(radc[i] - t) < 0.05 for i, t in enumerate((35.5, 40.6, 49.4))),
      f"Petersen: disc radii in count units q^((K+1)/2) e_K at K = 1, 2, 3: {', '.join(mp.nstr(r, 4) for r in radc)} (shard: 35.5, 40.6, 49.4)")

# ===========================================================================
head("2. THE THREE CALIBRATION CASES AND THEIR DATA")
# ===========================================================================


def rand_cubic(V, rng):
    while True:
        pts = [v for v in range(V) for _ in range(3)]
        rng.shuffle(pts)
        E = set()
        ok = True
        for i in range(0, len(pts), 2):
            a, b = pts[i], pts[i + 1]
            if a == b or (min(a, b), max(a, b)) in E:
                ok = False
                break
            E.add((min(a, b), max(a, b)))
        if ok:
            return sorted(E)


def ramanujan_certificate(V, E, q):
    """exact: charpoly of A, divide by (x - (q+1)), certified isolation of all roots; Ramanujan iff every
    root has |lambda| < 2 sqrt q (strict; this also gives connected and non-bipartite)"""
    A = [[0] * V for _ in range(V)]
    for a, b in E:
        A[a][b] = A[b][a] = 1
    cp = fmpz_mat(A).charpoly()
    x = fmpz_poly([0, 1])
    P, r = divmod(cp, x - (q + 1))
    rts = P.complex_roots()
    b = 2 * arb(q).sqrt()
    ok = r == 0 and all(abs(z.real) < b and z.imag.contains(0) for z, m in rts)
    return ok, rts


rng = random.Random(SEED)
V_g, q_g = 40, 2
draws = 0
while True:
    E_g = rand_cubic(V_g, rng)
    draws += 1
    ok_ram, rts_g = ramanujan_certificate(V_g, E_g, q_g)
    if ok_ram:
        break
E_gn = len(E_g)
mults = sorted(set(m for z, m in rts_g))
check(ok_ram, f"G40: random cubic graph on {V_g} vertices (configuration model, seed {SEED}, accepted draw {draws}) is Ramanujan: "
      f"all {sum(m for z, m in rts_g)} nontrivial adjacency eigenvalues certified in (-2 sqrt 2, 2 sqrt 2) (exact charpoly + arb isolation)")
check(mults == [1], f"G40: nontrivial spectrum simple ({len(rts_g)} distinct eigenvalues): R = {2 * len(rts_g)} distinct retained atoms "
      f"on the circle, so T_K is definite for K < {2 * len(rts_g)} and singular from K = {2 * len(rts_g)} (prop:extension-disc(iv))")
R_g = 2 * len(rts_g)
Bg, ng = hashimoto(V_g, E_g)
KMAX_G = R_g + 1
N_g = traces(Bg, ng, KMAX_G + 1)
check(N_g[0] == 2 * E_gn, f"G40: N_0 = Tr I = 2E = {N_g[0]}")


def mobius(n):
    res, m, p = 1, n, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            res = -res
        p += 1
    if m > 1:
        res = -res
    return res


def prime_cycle_counts(Nk, K):
    """l pi(l) = sum_{d | l} mu(l/d) N_d"""
    lpi = [0] * (K + 1)
    for l in range(1, K + 1):
        lpi[l] = sum(mobius(l // d) * Nk[d] for d in range(1, l + 1) if l % d == 0)
    return lpi


lpi_g = prime_cycle_counts(N_g, KMAX_G + 1)
check(all(lpi_g[l] % l == 0 and lpi_g[l] >= 0 for l in range(1, KMAX_G + 2)),
      "G40: l pi(l) = sum_{d|l} mu(l/d) N_d is a nonnegative multiple of l for every l (prime cycle counts are integers)")
girth = min(l for l in range(1, KMAX_G + 2) if lpi_g[l] > 0)
print(f"  G40: V = {V_g}, E = {E_gn}, q = {q_g}, girth {girth}; prime cycle counts pi(l), l = 1..16: "
      f"{[lpi_g[l] // l for l in range(1, 17)]}")
print(f"       pi(l) q^-l for l = 10, 20, 40, 78: {', '.join(f(lpi_g[l] // l / 2 ** l, 4) for l in (10, 20, 40, 78))}"
      f" (prime cycle theorem: pi(l) ~ q^l / l)")
lpi_pet = prime_cycle_counts(N_pet, 11)
check([lpi_pet[l] // l for l in range(1, 7)] == [0, 0, 0, 0, 24, 20],
      "Petersen: no prime cycle of length <= 4 (girth 5); pi(5) = 24, pi(6) = 20 (12 pentagons and 10 hexagons, each in "
      "two orientations: prime cycles of the Ihara zeta are oriented)")
note("Petersen's critical window is K = 4 (four distinct retained atoms) and its girth is 5: every entry of T_K,")
note("K <= 4, is kinematic (dimension, pole, trivial terms). Its window form contains NO prime datum at all.")

# arb traces for G40
SQ = arb(q_g).sqrt()


def nu_arb(Nk, q, V, E, K):
    sq = arb(q).sqrt()
    return [arb(Nk[k] - triv(q, V, E, k)) / sq ** k for k in range(K + 1)]


NU_G = nu_arb(N_g, q_g, V_g, E_gn, KMAX_G + 1)
NU_Gmp = [amid(x) for x in NU_G]
check(abs(NU_Gmp[0] - (2 * V_g - 2)) < 1e-100, f"G40: nu_0 = 2V - 2 = {int(NU_Gmp[0])} retained atoms (kinematic)")

# ===========================================================================
head("3. AXIS K (window = data cutoff; the analogue of lane A1's CCM axis-x protocol)")
# ===========================================================================


def toeplitz_arb(nu, K):
    return arb_mat([[nu[abs(i - j)] for j in range(K + 1)] for i in range(K + 1)])


def eig_min(T, want_vec=True):
    """certified eigenvalues (acb_mat.eig); returns (lambda_min ball, #negative (None if a ball straddles 0), all
    eigenvalue balls, unit eigenvector for lambda_min as mpmath list)"""
    n = T.nrows()
    if want_vec:
        ev, Rm = acb_mat(T).eig(right=True, nonstop=True)
    else:
        ev = acb_mat(T).eig(nonstop=True)
    re = [x.real for x in ev]
    if not all(x.is_finite() for x in re):
        # degenerate spectrum (the permutation's T_K has repeated eigenvalues): fall back to mpmath at 180 digits;
        # signs are then floating-point, not certified
        Mm = mp.matrix([[amid(T[i, j]) for j in range(n)] for i in range(n)])
        evm, Vm = mp.eigsy(Mm)
        re = [arb(mp.nstr(evm[i], 170)) for i in range(n)]
        i0 = min(range(n), key=lambda i: evm[i])
        neg = sum(1 for x in evm if x < -mp.mpf(10) ** -150)
        v = [Vm[i, i0] for i in range(n)] if want_vec else None
        return re[i0], neg, re, v
    i0 = min(range(n), key=lambda i: re[i].mid())
    neg = 0
    for x in re:
        if x < 0:
            neg += 1
        elif not x > 0:
            neg = None                    # a ball straddles 0: sign not certified
            break
    v = None
    if want_vec:
        v = [amid(Rm[i, i0].real) for i in range(n)]
        nv = mp.sqrt(mp.fsum(t * t for t in v))
        v = [t / nv for t in v]
    return re[i0], neg, re, v


def overlap_shift(v, w):
    """max over shifts s of |<v, w shifted>| (v shorter or equal)"""
    n, m = len(v), len(w)
    return max(abs(mp.fsum(v[j] * w[j + s] for j in range(n))) for s in range(m - n + 1))


def axis_K(name, nu_arb_list, Kfin, Kshow):
    nu_mp = [amid(x) for x in nu_arb_list]
    lev = levinson(nu_mp, Kfin)
    rows = {}
    _, _, _, vfin = eig_min(toeplitz_arb(nu_arb_list, Kfin))
    for K in range(0, Kfin + 1):
        lam, neg, _, v = eig_min(toeplitz_arb(nu_arb_list, K))
        eK, c, tau = lev[K]
        logdet = mp.fsum(mp.log(lev[j][0]) for j in range(K + 1))
        eK1 = eK * (1 - tau ** 2)
        bnd = abs(1 - tau ** 2) < mp.mpf(10) ** -100          # truth on the boundary: e_(K+1) = 0 exactly
        dI = mp.inf if bnd else mp.log(nu_mp[0]) - mp.log(eK1)
        dIs = mp.inf if bnd else -mp.log(1 - tau ** 2)
        ov = overlap_shift(v, vfin)
        rows[K] = dict(lam=lam, neg=neg, eK=eK, c=c, tau=tau, logdet=logdet, dI=dI, dIs=dIs, ov=ov, nu1=nu_mp[K + 1])
    print(f"\n  {name}: K = 0..{Kfin} (Kfin = last definite window)")
    print(f"  {'K':>3} {'lambda_min(T_K)':>16} {'log det T_K':>12} {'e_K (radius)':>13} {'c_K':>11} {'nu_(K+1)':>11} "
          f"{'tau_K':>8} {'Delta I_K':>10} {'Delta I^s':>10} {'1-overlap':>10}")
    for K in Kshow:
        r = rows[K]
        print(f"  {K:3d} {e(amid(r['lam'])):>16} {f(r['logdet'], 3):>12} {e(r['eK']):>13} {f(r['c'], 4):>11} "
              f"{f(r['nu1'], 4):>11} {f(r['tau'], 4):>8} {f(r['dI'], 3) if r['dI'] != mp.inf else 'inf':>10} "
              f"{f(r['dIs'], 3) if r['dIs'] != mp.inf else 'inf':>10} {e(max(0, 1 - r['ov']), 2):>10}")
    return rows, lev, vfin


# permutation: K = 0..3 (singular from K = 4)
NU_P = [arb(t) for t in nu_perm]
rows_p, lev_p, _ = axis_K("permutation (1 2)(3 4 5), 4 distinct atoms", NU_P, 3, range(0, 4))
lam4 = eig_min(toeplitz_arb(NU_P, 4), False)[0]
check(all(rows_p[K]["lam"] > 0 for K in range(4)) and abs(amid(lam4)) < mp.mpf(10) ** -100,
      f"permutation: T_K definite for K <= 3, lambda_min(T_4) = 0 ({e(amid(lam4))}, mpmath fallback: repeated eigenvalues; 4 atoms)")
# Petersen: K = 0..3
NU_PET = nu_arb(N_pet, q_p, V_p, E_p, 11)
rows_pet, lev_pet, _ = axis_K("Petersen (q = 2), 4 distinct atoms, girth 5: all data kinematic", NU_PET, 3, range(0, 4))
lam4p = eig_min(toeplitz_arb(NU_PET, 4), False)[0]
check(all(rows_pet[K]["lam"] > 0 for K in range(4)) and lam4p.contains(0) and abs(abs(rows_pet[3]["tau"]) - 1) < 1e-100,
      "Petersen: definite for K <= 3, singular at K = 4, truth on the boundary at K = 3 (|tau_3| = 1): the posterior "
      "collapses to a point using kinematic data only")
# G40
KF = R_g - 1
show = sorted(set(list(range(0, KF + 1, 6)) + [KF - 4, KF - 3, KF - 2, KF - 1, KF]))
rows_g, lev_g, vfin_g = axis_K(f"G40 (q = 2, V = {V_g}), R = {R_g} distinct atoms", NU_G, KF, show)
lamR = eig_min(toeplitz_arb(NU_G, R_g), False)[0]
check(all(rows_g[K]["lam"] > 0 for K in range(KF + 1)), f"G40: T_K certified positive definite for every K <= {KF}")
check(lamR.contains(0) and abs(amid(lamR)) < mp.mpf(10) ** -100,
      f"G40: lambda_min(T_{R_g}) = 0 (certified ball {e(amid(lamR))} +- {e(float(lamR.rad()))} contains 0): exact collapse at K = R")
check(abs(abs(rows_g[KF]["tau"]) - 1) < mp.mpf(10) ** -60,
      f"G40: at K = R - 1 = {KF} the true nu_(K+1) is on the boundary of its disc (|tau| = 1 to 1e-60), prop:extension-disc(iv)")
lams = [amid(rows_g[K]["lam"]) for K in range(KF + 1)]
check(all(lams[K + 1] <= lams[K] for K in range(KF)), "G40: lambda_min(T_K) is non-increasing in K (interlacing)")
# learning-rate summary for G40
sl = []
for (K1, K2) in ((6, 30), (30, 54), (54, 72), (72, KF)):
    sl.append((K1, K2, (mp.log10(lams[K2]) - mp.log10(lams[K1])) / (K2 - K1)))
print("\n  G40 learning rate of lambda_min along K (decimal digits per unit of K): " +
      ", ".join(f"K = {a}..{b}: {f(s, 3)}" for a, b, s in sl))
taus = [abs(rows_g[K]["tau"]) for K in range(KF + 1)]
dIs = [rows_g[K]["dIs"] for K in range(KF)]
dI = [rows_g[K]["dI"] for K in range(KF)]
print(f"  G40 |tau_K|: mean over K < {R_g // 2}: {f(sum(taus[:R_g // 2]) / (R_g // 2), 3)}; mean over {R_g // 2} <= K < {KF}: "
      f"{f(sum(taus[R_g // 2:KF]) / (KF - R_g // 2), 3)}; K = {KF}: {f(taus[KF], 6)}")
print(f"  G40 Delta I_K (nats): K = 0..9: {', '.join(f(x, 2) for x in dI[:10])}; K = {KF - 5}..{KF - 1}: "
      f"{', '.join(f(x, 2) for x in dI[KF - 5:KF])}")
print(f"  G40 Delta I^s_K (nats): K = 0..9: {', '.join(f(x, 3) for x in dIs[:10])}; K = {KF - 5}..{KF - 1}: "
      f"{', '.join(f(x, 3) for x in dIs[KF - 5:KF])}")
imax = max(range(KF), key=lambda K: dI[K])
check(max(taus[:KF]) < 1 and abs(taus[KF] - 1) < mp.mpf(10) ** -60,
      f"G40: the truth is interior to its disc for every K < {KF} (max |tau| = {f(max(taus[:KF]), 4)}) and on the boundary at K = {KF}")
ovs = [max(0, 1 - rows_g[K]["ov"]) for K in range(KF + 1)]
print(f"  G40 1 - overlap(v_K, v_final) at K = 12, 24, 36, 48, 60, 66, 72, 76: "
      f"{', '.join(e(ovs[K], 2) for K in (12, 24, 36, 48, 60, 66, 72, 76))}")

# ===========================================================================
head("4. DATA AXIS (fixed window, prime cycles of length <= P added; the analogue of lane A1's fixed-L protocol)")
# ===========================================================================


def partial_nu(Nk, lpi, q, V, E, K, P):
    """nu_k with only prime cycles of length <= P: N_k^(P) = sum_{l | k, l <= P} l pi(l) (k >= 1), N_0 = 2E"""
    sq = arb(q).sqrt()
    out = []
    for k in range(K + 1):
        if k == 0:
            Nk_P = Nk[0]
        else:
            Nk_P = sum(lpi[l] for l in range(1, min(P, k) + 1) if k % l == 0)
        out.append(arb(Nk_P - triv(q, V, E, k)) / sq ** k)
    return out


def data_axis(name, Nk, lpi, q, V, E, K, Pshow):
    _, _, _, vfin = eig_min(toeplitz_arb(nu_arb(Nk, q, V, E, K), K))
    rows = {}
    for P in range(0, K + 1):
        nuP = partial_nu(Nk, lpi, q, V, E, K, P)
        lam, neg, re, v = eig_min(toeplitz_arb(nuP, K))
        ld = mp.fsum(mp.log(abs(amid(x))) for x in re)
        ov = abs(mp.fsum(v[j] * vfin[j] for j in range(K + 1)))
        rows[P] = dict(lam=lam, neg=neg, ld=ld, ov=ov)
    print(f"\n  {name}: window K = {K}, P = max prime-cycle length included (P = 0: kinematic data only)")
    print(f"  {'P':>3} {'#cycles <= P':>13} {'lambda_min':>12} {'#neg':>5} {'log|det|':>10} {'overlap w. final':>17}")
    for P in Pshow:
        r = rows[P]
        ncyc = sum(lpi[l] // l for l in range(1, P + 1)) if P > 0 else 0
        print(f"  {P:3d} {ncyc:>13d} {e(amid(r['lam'])):>12} {str(r['neg']):>5} {f(r['ld'], 2):>10} {e(r['ov'], 3):>17}")
    return rows


# permutation: cycles of lengths 2, 3; "kinematic" = the dimension 5
print("\n  permutation (1 2)(3 4 5), window K = 3: data = its cycles (lengths 2, 3); the kinematic form is 5 I")
lpi_perm = [0, 0, 2, 3]
rows_pp = {}
_, _, _, vfin_p = eig_min(toeplitz_arb(NU_P, 3))
for P in range(0, 4):
    nuP = [arb(5)] + [arb(sum(lpi_perm[l] for l in range(1, min(P, k) + 1) if k % l == 0)) for k in range(1, 4)]
    lam, neg, re, v = eig_min(toeplitz_arb(nuP, 3))
    rows_pp[P] = (lam, neg, abs(mp.fsum(v[j] * vfin_p[j] for j in range(4))))
    print(f"  P = {P}: nu = {[int(amid(x)) for x in nuP]}, lambda_min = {f(amid(lam), 4)}, #neg = {neg}, overlap = {f(rows_pp[P][2], 4)}"
          + ("  (lambda_min degenerate: the overlap depends on the eigenvector chosen)" if P < 2 else ""))
check(all(rows_pp[P][1] == 0 for P in range(4)),
      "permutation: every partial form is positive definite (no pole: each partial datum is the moment sequence of a positive "
      "measure, the included cycles' atoms plus a flat density)")
# G40 at two windows
KF2 = R_g // 2 - 1
rows_d1 = data_axis(f"G40, window K = {KF}", N_g, lpi_g, q_g, V_g, E_gn, KF,
                    sorted(set([0, 3, 4, 5, 6, 8, 10, 15, 20, 30, 40, 50, 60, 70, 74, 75, 76, 77])))
rows_d2 = data_axis(f"G40, window K = {KF2}", N_g, lpi_g, q_g, V_g, E_gn, KF2,
                    sorted(set([0, 3, 4, 6, 10, 20, 30, 34, 35, 36, 37, 38])))
check(all(rows_d1[P]["neg"] is not None and rows_d1[P]["neg"] > 0 for P in range(KF)) and rows_d1[KF]["neg"] == 0,
      f"G40, K = {KF}: every partial form with P < K is indefinite (certified negative counts); positive only when the "
      f"last cycle length P = K enters")
check(all(rows_d2[P]["neg"] is not None and rows_d2[P]["neg"] > 0 for P in range(KF2)) and rows_d2[KF2]["neg"] == 0,
      f"G40, K = {KF2}: same: indefinite until the last cycle length")
lam_prev = amid(rows_d1[KF - 1]["lam"])
check(lam_prev < -1, f"G40, K = {KF}: with every cycle length except the last, lambda_min = {e(lam_prev)} (O(q^(K/2)) scale), "
      f"overlap with the final eigenvector {e(rows_d1[KF - 1]['ov'])}")
negs = [rows_d1[P]["neg"] for P in range(KF + 1)]
print(f"\n  G40, K = {KF}: #neg against P = 0..{KF}: {negs}")

# ===========================================================================
head("5. RAYLEIGH DECOMPOSITION OF lambda_min AT THE FINAL WINDOW (the analogue of lane A1's decomposition)")
# ===========================================================================


def rayleigh(K, Nk, lpi, q, V, E, nu_full):
    lam, _, _, v = eig_min(toeplitz_arb(nu_full, K))
    sq = mp.sqrt(mp.mpf(q))
    # quadratic form of a Toeplitz sequence t: v^T T(t) v = t_0 |v|^2 + 2 sum_k t_k s_k, s_k = sum_j v_j v_{j+k}
    s = [mp.fsum(v[j] * v[j + k] for j in range(K + 1 - k)) for k in range(K + 1)]

    def form(t):
        return t[0] * s[0] + 2 * mp.fsum(t[k] * s[k] for k in range(1, K + 1))
    parts = {}
    parts["dimension N_0 = 2E"] = form([mp.mpf(Nk[0])] + [0] * K)
    parts["pole (q^k)"] = form([-(sq ** k) for k in range(K + 1)])
    parts["trivial (1 + (E-V)(1+(-1)^k))"] = form([-(1 + (E - V) * (1 + (-1) ** k)) / sq ** k for k in range(K + 1)])
    for l in range(1, K + 1):
        if lpi[l]:
            parts[f"cycles of length {l}"] = form([0] + [(lpi[l] if k % l == 0 else 0) / sq ** k for k in range(1, K + 1)])
    return amid(lam), parts


for K in (KF, KF2):
    lamK, parts = rayleigh(K, N_g, lpi_g, q_g, V_g, E_gn, NU_G)
    tot = mp.fsum(parts.values())
    print(f"\n  G40, K = {K}: lambda_min = {e(lamK, 4)}; sum of the parts = {e(tot, 4)}")
    kin = parts["dimension N_0 = 2E"] + parts["pole (q^k)"] + parts["trivial (1 + (E-V)(1+(-1)^k))"]
    items = list(parts.items())
    for name, val in items[:3]:
        print(f"    {name:<34} {e(val, 4):>12}")
    print(f"    {'kinematic total':<34} {e(kin, 4):>12}")
    cyc = [(name, val) for name, val in items[3:]]
    big = sorted(cyc, key=lambda t: -abs(t[1]))[:6]
    small = min(abs(val) for name, val in cyc)
    for name, val in cyc[:8]:
        print(f"    {name:<34} {e(val, 4):>12}")
    print(f"    ... ({len(cyc)} cycle lengths in all); smallest |contribution| {e(small, 2)}, largest {e(abs(big[0][1]), 2)} ({big[0][0]})")
    check(abs(tot - lamK) < mp.mpf(10) ** -60 * max(1, abs(kin)), f"K = {K}: the parts sum to lambda_min (to 1e-60 relative)")
    check(abs(kin) > 1e3 * abs(lamK) and small > abs(lamK),
          f"K = {K}: lambda_min is a cancellation residual: kinematic total {e(kin, 2)} against cycle terms, each of which "
          f"exceeds lambda_min by at least a factor {e(small / lamK, 1)}")

# ===========================================================================
head("6. COMPARISON STEP (the graph's spectrum used here only): Pisarenko roots against the true atoms, G40")
# ===========================================================================
# true atoms: theta = arg of (lambda + i sqrt(4q - lambda^2)) / (2 sqrt q), lambda the nontrivial adjacency eigenvalues
thetas = sorted(mp.acos(amid(z.real) / (2 * mp.sqrt(q_g))) for z, m in rts_g)
th1 = thetas[0]
print(f"  true atoms: {R_g} angles +-theta_j, theta_j in (0, pi); lowest theta_1 = {mp.nstr(th1, 12)}, "
      f"highest {mp.nstr(thetas[-1], 12)}; minimal gap between distinct angles "
      f"{e(min(min(thetas[i + 1] - thetas[i] for i in range(len(thetas) - 1)), 2 * thetas[0], 2 * (mp.pi - thetas[-1])))}")


def kernel_root_near(v, theta0):
    """root of p(z) = sum v_j z^j nearest e^{i theta0}, refined by Newton in mpmath (roots lie on the circle)"""
    coeffs = [float(t) for t in v]
    rts = np.roots(coeffs[::-1])
    z0 = min(rts, key=lambda z: abs(z - complex(math.cos(float(theta0)), math.sin(float(theta0)))))
    z = mp.mpc(z0.real, z0.imag)
    for _ in range(200):
        p = mp.mpf(0); dp = mp.mpf(0)
        for c in reversed(v):
            dp = dp * z + p
            p = p * z + c
        step = p / dp
        z = z - step
        if abs(step) < mp.mpf(10) ** -170:
            break
    return z


ERR = {}
print(f"  {'K':>3} {'lambda_min(T_K)':>16} {'|theta(root) - theta_1|':>24} {'| |root| - 1 |':>15} {'err / lambda_min':>17}")
for K in list(range(12, KF + 1, 6)) + [KF - 1, KF]:
    lam, _, _, v = eig_min(toeplitz_arb(NU_G, K))
    z = kernel_root_near(v, th1)
    err = abs(mp.arg(z) - th1)
    ERR[K] = (amid(lam), err, abs(abs(z) - 1))
    print(f"  {K:3d} {e(ERR[K][0]):>16} {e(err):>24} {e(ERR[K][2], 1):>15} {e(err / ERR[K][0], 2):>17}")
check(all(ERR[K][2] < mp.mpf(10) ** -100 for K in ERR), "every kernel root used lies on the unit circle to 1e-100 (Caratheodory-Fejer)")
_, _, _, vR = eig_min(toeplitz_arb(NU_G, R_g))
rootsR = [kernel_root_near(vR, t) for t in thetas]
errR = max(abs(mp.arg(z) - t) for z, t in zip(rootsR, thetas))
check(errR < mp.mpf(10) ** -100, f"K = R = {R_g}: the kernel polynomial of the singular T_R has the true atoms as roots "
      f"(max |theta error| over the {len(thetas)} upper-half atoms: {e(errR)})")
rat = [ERR[K][1] / ERR[K][0] for K in ERR if K >= 36]
print(f"  err/lambda_min for K >= 36 ranges over {e(min(rat), 2)} .. {e(max(rat), 2)}")

# ===========================================================================
head("6b. B2.1 ON THE CALIBRATION CASE: the positive set of prime data with the kinematic data fixed (G40)")
# ===========================================================================
print("""  Kinematic space: real symmetric Toeplitz forms T_K(nu_0..nu_K) (dimension K+1; displacement rank 2, the Toeplitz
  analogue of the Loewner commutator); the identity is interior, so the positive cone spans it.  Fix the kinematic
  data (nu_0 = 2V - 2 and the pole and trivial parts of nu_k); the prime data are x_k = q^{-k/2} N_k, k = 1..K:
    P^graph_K = {x : T_K(nu_0, nu^kin + x) >= 0} = M_K - nu^kin,  M_K = the moment space of positive measures of
  mass nu_0 on the circle (Caratheodory-Toeplitz).  It has dimension K (x = -nu^kin gives nu_0 I > 0) and is
  BOUNDED: every 2x2 principal minor gives |nu_k| <= nu_0.  Its maximum-determinant element is nu = (nu_0, 0, .., 0)
  (Hadamard), i.e. x_k = -nu^kin_k, N_k = trivial_k = q^k + 1 + (E-V)(1+(-1)^k): the graph prime number theorem.
  Norm: Hilbert-Schmidt norm of the Toeplitz prime part, ||x||^2 = sum_k 2 (K+1-k) x_k^2.""")
GR = {}
for K in (KF, KF2):
    sq = mp.sqrt(mp.mpf(q_g))
    wts = [2 * (K + 1 - k) for k in range(1, K + 1)]
    x_true = [mp.mpf(N_g[k]) / sq ** k for k in range(1, K + 1)]
    nu_kin = [-mp.mpf(triv(q_g, V_g, E_gn, k)) / sq ** k for k in range(1, K + 1)]
    x_md = [-t for t in nu_kin]
    hs = lambda z: mp.sqrt(mp.fsum(w * t * t for w, t in zip(wts, z)))
    ip = lambda z1, z2: mp.fsum(w * a * b for w, a, b in zip(wts, z1, z2))
    nt = hs(x_true)
    dist = hs([a - b for a, b in zip(x_md, x_true)]) / nt
    capt = ip(x_md, x_true) / nt ** 2
    diam = 2 * NU_Gmp[0] * mp.sqrt(mp.fsum(wts)) / nt           # bound on the diameter of P^graph_K, relative
    lam_md = eig_min(toeplitz_arb([arb(int(NU_Gmp[0]))] + [arb(0)] * K, K), False)[0]
    relN = max(abs(mp.mpf(N_g[k] - triv(q_g, V_g, E_gn, k))) / N_g[k] for k in range(K // 2, K + 1))
    GR[K] = (dist, capt, diam, relN)
    print(f"\n  K = {K}: ||x_true||_HS = {e(nt)}; max-det (PNT) prediction: lambda_min = {f(amid(lam_md), 1)} (= nu_0), relative "
          f"distance {e(dist)}, captured fraction {mp.nstr(capt, 12)};")
    print(f"          relative diameter of the whole positive set <= {e(diam)}; in count units |N_k - N_k^PNT| / N_k <= {e(relN)} "
          f"for k >= {K // 2}")
check(GR[KF][0] < 1e-8 and GR[KF2][0] < 1e-3 and abs(GR[KF][1] - 1) < 1e-8,
      f"G40: the maximum-determinant element exists and is the prime number theorem; it predicts the prime data of the "
      f"window to relative error {e(GR[KF][0], 1)} (K = {KF}) and {e(GR[KF2][0], 1)} (K = {KF2})")
check(GR[KF][2] < 1e-7 and GR[KF2][2] < 1e-2, "G40: the whole positive set of prime data has relative diameter <= "
      f"{e(GR[KF][2], 1)} (K = {KF}) and {e(GR[KF2][2], 1)} (K = {KF2})")
print()
print("  like-for-like scale: the relative error rho(K) of the PNT (max-det) prediction against the window, with the")
print("  equivalent zeta window x_eq = q^K (a prime cycle of length l has norm q^l; zeta's window x = e^L):")
print(f"  {'K':>3} {'x_eq = q^K':>11} {'rho(K)':>9} {'captured':>9}")
RHO = {}
for K in list(range(girth, 13)) + [16, 20, 30, KF2, 50, 60, KF]:
    sq = mp.sqrt(mp.mpf(q_g))
    wts = [2 * (K + 1 - k) for k in range(1, K + 1)]
    xt = [mp.mpf(N_g[k]) / sq ** k for k in range(1, K + 1)]
    xm = [mp.mpf(triv(q_g, V_g, E_gn, k)) / sq ** k for k in range(1, K + 1)]
    nt2 = mp.fsum(w * t * t for w, t in zip(wts, xt))
    rho = mp.sqrt(mp.fsum(w * (a - b) ** 2 for w, a, b in zip(wts, xt, xm)) / nt2)
    cap = mp.fsum(w * a * b for w, a, b in zip(wts, xt, xm)) / nt2
    RHO[K] = rho
    print(f"  {K:3d} {e(mp.mpf(q_g) ** K, 2):>11} {f(rho, 4) if rho > 1e-3 else e(rho, 2):>9} {f(cap, 4):>9}")
check(RHO[4] > 0.5 and RHO[8] > 0.1 and RHO[KF] < 1e-8,
      f"G40: at windows comparable to zeta's x = 16..256 (K = 4..8) the PNT prediction is worse than none (rho = {f(RHO[4], 3)} at "
      f"K = 4, {f(RHO[8], 3)} at K = 8); rho falls like q^(-K/2) for large K (square-root cancellation, the graph's RH)")
note("reading.  (i) Structure: the graph's positive set is bounded and has a maximum-determinant element (the PNT),")
note("because the diagonal nu_0 (lag 0) carries no prime datum; zeta's, in the Loewner coordinates, is unbounded with no")
note("maximum-determinant element, because every Loewner datum, including the diagonal a_n, carries prime content")
note("(rtp1_commutant.py section 3).  (ii) Scale: the graph's tight RELATIVE posterior at K = 77 is the square-root law")
note("at x_eq = 2^77 ~ 1.5e23.  At comparable windows (x_eq = 16..256) the graph's PNT prediction is no better than")
note("zeta's (rho = 6.7 .. 2.2 here, against 0.96 .. 0.80 for zeta at x = 13..100, N = 40, rtp1_commutant.py section 5b).")
note("(iii) Absolute size: the graph's positive set is the moment space, of diameter O(nu_0) = O(78) in rescaled units,")
note("never small; zeta's lattice-restricted weights are pinned in absolute terms (rtp1_commutant.py section 6).")

# ===========================================================================
head("7. THE CONTROL SIGNATURE, AND HOW IT DIFFERS FROM ZETA (lane A1)")
# ===========================================================================
dig_end = (mp.log10(lams[72]) - mp.log10(lams[KF])) / (KF - 72)
print(f"""  Calibration (finite transfer operators, RH a theorem):
  (1) Window K and data are one axis.  lambda_min(T_K) falls smoothly, at {f(sl[0][2], 2)} .. {f(sl[-1][2], 2)} decimal digits
      per unit of K for G40 (steepening towards the end), and reaches EXACTLY 0 at the finite critical window K = R
      (number of distinct atoms, a Weyl count fixed by V): the posterior collapses to a point.
  (2) The next trace is interior to its disc (|tau_K| < 1) at every K < R - 1 and on the boundary at K = R - 1;
      the disc radius e_K shrinks from nu_0 = {int(NU_Gmp[0])} to {e(rows_g[KF]['eK'], 2)} and then to 0.
  (3) At fixed window, every partial form is indefinite until the last cycle length enters, and at a scale
      O(q^(K/2)): the pole term q^k is cancelled only by the full prime-cycle count (the graph prime number theorem).
      A permutation (no pole) has positive partial forms at every stage.  Petersen (girth 5 > critical window) has no
      prime datum in its window at all: kinematics alone give the exact, singular form at K = 4.
  (4) lambda_min is a cancellation residual at the final window (section 5), as for zeta.""")
check(all(s < 0 for _, _, s in sl), "G40: lambda_min decreases on every stretch of K (negative slopes)")
pexp = [(a, b, -sv / mp.log10(q_g)) for a, b, sv in sl]
check(all(0 < pp < 5 for _, _, pp in pexp),
      "G40: in the zeta-comparable variable x_eq = q^K the learning curve is a POWER law, lambda_min ~ x_eq^(-p) with p = "
      + ", ".join(f"{f(pp, 2)} (K = {a}..{b})" for a, b, pp in pexp)
      + "; zeta's (lane A1) is exponential in x, eps ~ e^(-4 pi x)")
print(f"""
  Contrast with zeta (lane A1), item by item:
  - zeta's window form never collapses (infinitely many zeros): eps_N(x) > 0 at every x, falling like e^(-4 pi x), i.e.
    exponentially in x and doubly exponentially in the window length L = log x.  The graph's lambda_min falls like a
    power of x_eq = q^K (above) and then hits 0 exactly at the finite critical window K = R = 2V - 2.
  - zeta has a resolution axis N with a saturation at N_sat ~ 1.7 x log x; the graph's window form is exact and
    finite-dimensional, so there is no resolution axis.  The graph analogue of the Weyl-count scale N_sat is the
    collapse point K = R (a count of atoms fixed by V alone).
  - disc/interval of the next datum: zeta's stays O(1) above N_sat (half-width 0.5..3.7) with the truth interior, and
    the truth sits on the boundary below N_sat; the graph's disc shrinks from nu_0 = {int(NU_Gmp[0])} to {e(rows_g[KF]['eK'], 2)}
    with the truth interior (max |tau| = {f(max(taus[:KF]), 3)}) until K = R - 1, where it is on the boundary.
  - fixed window, data added: both are indefinite until the last datum.  With only the last datum missing, zeta's
    lambda_min is -5.66e-7 (x = 50, k = 49 missing; the prime power at the window edge enters with weight 1 - log k / L
    -> 0, because the continuous autocorrelation of a window function vanishes at the edge); the graph's is
    {e(lam_prev, 2)} (the lag-K corner of a Toeplitz form carries full weight, and the missing count is ~ q^K).
  - the kinematic (pole + trivial) form: zeta's is indefinite by O(1) (1 to 3 negative even eigenvalues, lambda_min
    -0.07 .. -1.37); the graph's has ONE negative eigenvalue of size ~ q^(K/2) ({e(amid(rows_d1[0]['lam']), 2)} at K = {KF}),
    the pole direction; the permutation (no pole) has a positive kinematic form (5 I).
  - lambda_min at the final window is a cancellation residual in both (zeta: pole +1.55 vs archimedean -1.48 vs primes;
    graph: pole -2.8e5 vs cycle terms, each > 1e18 lambda_min at K = {KF}); the signs are opposite (zeta's primes enter
    the Weil form with a minus sign, the graph's cycle counts with a plus sign).
""")

# ===========================================================================
head("TALLY")
# ===========================================================================
if _FAILED:
    print("  failing checks:")
    for line, msg in _FAILED:
        print(f"    L{line}: {msg}")
else:
    print("  no failing checks")
print()
print(f"CHECKS: {_PASS} passed, {_FAIL} failed")
