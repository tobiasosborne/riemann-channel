#!/usr/bin/env python3
"""Checks for 'Is the prime-dilation residual an artefact of the window?' (notes/adelic-gkp/window-similitude.md), lane R.

Normalised model.  u = log x.  A test function h(u) has hat h(g) = int h(u) e^{i g u} du.  The zero sum over the first
K critical zeros (K = 1000 unless stated; data/zeros3000.npy) is
    Z_K(h, k) = sum_{gamma = +-gamma_1..+-gamma_K} hat h(gamma) conj(hat k(gamma)).
The dilation x -> p x is the translation (U_t h)(u) = h(u - t), t = log p; hat(U_t h)(g) = e^{i g t} hat h(g).
In a finite basis b_i with Z-Gram A_ij = Z(b_j, b_i) (so Z(h, h) = c^dag A c), a compression M of U_t gives the
similitude defect R = M^dag A M - A.  Best-c residual: lane G's ||M^dag A M - c A||_F / ||A||_F with c fitted.
Interior fraction: order the right singular vectors of M (L2-orthonormal basis) by leakage, take the largest k with
||Q_k^dag R Q_k||_2 <= 1e-6 ||A||_2, report k / n.

Sections: A the model and its translation invariance; B the three bases (hard window / Hermite / Gaussian frame);
C the Gram matrix of translates (Toeplitz) against the prime side; D Omega_D = Z(., D^{-1} .) without B.
numpy + mpmath only.  Run:  python3 check_window_similitude.py > output_window_similitude.txt   (about 40 s)
"""
import os
import time

os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('OMP_NUM_THREADS', '1')
import numpy as np  # noqa: E402
import mpmath as mp  # noqa: E402

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
ZEROS = np.load(os.path.join(ROOT, 'data', 'zeros3000.npy'))
K = 1000
GAM = np.concatenate([ZEROS[:K], -ZEROS[:K]])
LOG2 = np.log(2)
EG = 0.5772156649015329
npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


# ---------------------------------------------------------------------------------------------------------------
# quadrature, primes, Weil's explicit formula (lane G's archimedean term; validated in C2 against the zeros)
_X40, _W40 = np.polynomial.legendre.leggauss(40)


def cgl(breaks, hmax=0.05):
    """composite Gauss-Legendre on panels of width <= hmax between sorted breakpoints."""
    br = np.unique(np.asarray(breaks, float))
    us, ws = [], []
    for lo, hi in zip(br[:-1], br[1:]):
        e = np.linspace(lo, hi, max(1, int(np.ceil((hi - lo) / hmax))) + 1)
        for l2, h2 in zip(e[:-1], e[1:]):
            us.append(0.5 * (h2 - l2) * _X40 + 0.5 * (h2 + l2))
            ws.append(0.5 * (h2 - l2) * _W40)
    return np.concatenate(us), np.concatenate(ws)


def mangoldt(X):
    """(log n, Lambda(n)/sqrt n) for prime powers n <= X."""
    X = int(X)
    s = np.ones(X + 1, bool)
    s[:2] = False
    for i in range(2, int(X ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    n, lam = [], []
    for p in np.nonzero(s)[0]:
        q = int(p)
        while q <= X:
            n.append(q)
            lam.append(np.log(p))
            q *= int(p)
    n = np.array(n, float)
    o = np.argsort(n)
    return np.log(n[o]), np.array(lam)[o] / np.sqrt(n[o])


def weil_ef(p, U, kinks=()):
    """sum over all nontrivial zeros of phat(rho), for a pair function p supported in [-U, U]:
    Pole - Prime - Arch (explicit formula; no zeros used)."""
    ks = [k for k in kinks if -U < k < U]
    u, w = cgl([-U, 0.0, U] + ks)
    pole = np.sum(w * p(u) * 2 * np.cosh(u / 2))
    lu, wt = mangoldt(np.exp(U))
    sel = lu < U
    prime = np.sum(wt[sel] * (p(lu[sel]) + p(-lu[sel])))
    up, wp = cgl([0.0, U] + [abs(k) for k in ks])
    p0 = p(np.array([0.0]))[0]
    arch = ((np.log(4 * np.pi) + EG) * p0
            + np.sum(wp * (p(up) + p(-up) - 2 * np.exp(-up / 2) * p0) / (np.exp(up / 2) - np.exp(-1.5 * up)))
            - p0 * np.log(1 / np.tanh(U / 2)))
    return pole - prime - arch


# ---------------------------------------------------------------------------------------------------------------
# similitude diagnostics
def gram(F):
    return F.conj().T @ F


def best_c(R, A):
    c = np.real(np.vdot(A, R)) / np.real(np.vdot(A, A))
    return c, np.linalg.norm(R - c * A) / np.linalg.norm(A)


def interior(M, A, tol=1e-6):
    _, s, Vh = np.linalg.svd(M)
    Q = Vh.conj().T                      # singular values descending = leakage ascending
    RQ = Q.conj().T @ (M.conj().T @ A @ M - A) @ Q
    nA = np.linalg.norm(A, 2)

    def r(k):
        return np.linalg.norm(RQ[:k, :k], 2) / nA if k > 0 else 0.0
    lo, hi = 0, len(s)
    if r(hi) <= tol:
        return hi
    while hi - lo > 1:
        mid = (lo + hi) // 2
        lo, hi = (mid, hi) if r(mid) <= tol else (lo, mid)
    return lo


def lead_res(M, A, r=10):
    _, V = np.linalg.eigh(A)
    Q = V[:, -r:]
    return np.linalg.norm(Q.conj().T @ (M.conj().T @ A @ M - A) @ Q, 2) / np.linalg.norm(Q.conj().T @ A @ Q, 2)


def herm(n, x):
    P = np.zeros((n, len(x)))
    P[0] = np.pi ** -0.25 * np.exp(-x ** 2 / 2)
    if n > 1:
        P[1] = np.sqrt(2) * x * P[0]
    for k in range(2, n):
        P[k] = np.sqrt(2 / k) * x * P[k - 1] - np.sqrt((k - 1) / k) * P[k - 2]
    return P


def basis_a(L, n, a=LOG2):
    """lane G's hard window [0, L], e_m = e^{i w_m u}/sqrt L, |m| <= N, n = 2N + 1; exact transforms and exact
    compressed translation M = P_N chi U_a."""
    N = (n - 1) // 2
    idx = np.arange(-N, N + 1)
    om = 2 * np.pi * idx / L
    F = (np.exp(1j * GAM[:, None] * L) - 1) / (1j * (GAM[:, None] + om[None, :]) * np.sqrt(L))
    dn = om[None, :] - om[:, None]
    with np.errstate(divide='ignore', invalid='ignore'):
        M = (1 - np.exp(1j * dn * a)) / (1j * dn * L)
    np.fill_diagonal(M, (L - a) / L)
    return F, M * np.exp(-1j * om[None, :] * a), np.abs(idx) <= 3


def basis_b(L, n, a=LOG2):
    """smooth window: Hermite functions psi_k(u/s)/sqrt s, k < n (Gaussian times polynomial), effective support
    |u| <= s sqrt(2n) =: L/2.  hat = sqrt(2 pi s) i^k psi_k(s g); M = <psi_j, U_a psi_k> on a fine grid."""
    s = L / (2 * np.sqrt(2 * n))
    k = np.arange(n)
    F = np.sqrt(2 * np.pi * s) * (1j) ** k[None, :] * herm(n, s * GAM).T
    X = np.sqrt(2 * n) + a / s + 12
    x = np.arange(-X, X, 0.01)
    M = (herm(n, x) * 0.01) @ herm(n, x - a / s).T
    return F, M, k < 7


def basis_c(L, m, a=LOG2):
    """coherent-state frame: g_j(u) = exp(-(u - j d)^2 / 2 sig^2), d = a/m, sig = d, j < J = L/d.
    Translation by a is the index shift j -> j + m.  Returns the frame-coordinate data and an L2-orthonormalised copy."""
    d = a / m
    sig = d
    J = int(round(L / d))
    j = np.arange(J)
    F = sig * np.sqrt(2 * np.pi) * np.exp(-sig ** 2 * GAM[:, None] ** 2 / 2) * np.exp(1j * GAM[:, None] * j[None, :] * d)
    A = gram(F)
    S = np.zeros((J, J))
    S[np.arange(m, J), np.arange(J - m)] = 1.0
    jj = j[:, None] - j[None, :]
    G2 = sig * np.sqrt(np.pi) * np.exp(-(jj * d) ** 2 / (4 * sig ** 2))
    T2 = sig * np.sqrt(np.pi) * np.exp(-((jj - m) * d) ** 2 / (4 * sig ** 2))     # <g_j, U g_k> = <g_j, g_{k+m}>
    w, V = np.linalg.eigh(G2)
    W = V / np.sqrt(w)
    return J, A, S, W.T @ T2 @ W, W.T @ A @ W


# ===============================================================================================================
print("== A. The zero-sum model; translation is unitary for it")
check("A1 zeros file: 3000 increasing ordinates, gamma_1 = 14.134725..., K = 1000 used (gamma_1000 = %.4f)" % ZEROS[K - 1],
      ZEROS.shape == (3000,) and np.all(np.diff(ZEROS) > 0) and abs(ZEROS[0] - 14.134725141734693) < 1e-12)
rng = np.random.default_rng(7)
cen, wid, coef = rng.uniform(-1, 1, 6), rng.uniform(0.05, 0.3, 6), rng.normal(size=6)
frq = rng.uniform(-30, 30, 6)


def hrand(u):
    return np.sum(coef[:, None] * np.exp(-(u[None, :] - cen[:, None]) ** 2 / (2 * wid[:, None] ** 2))
                  * np.exp(1j * frq[:, None] * u[None, :]), axis=0)


uq, wq = cgl([-2.5, 6.0], 0.02)


def ft(f):                      # transform at the 2K ordinates by quadrature, in chunks
    return np.concatenate([(np.exp(1j * np.outer(GAM[i:i + 250], uq)) * wq) @ f for i in range(0, len(GAM), 250)])


Fh = ft(hrand(uq))
zh = np.sum(np.abs(Fh) ** 2)
errs = []
for t in (LOG2, np.log(3), np.log(5) * 2, 0.37):
    Ft = ft(hrand(uq - t))        # transform of U_t h by its own quadrature
    errs.append(abs(np.sum(np.abs(Ft) ** 2) - zh) / zh)
check("A2 Z_K(U_t h) = Z_K(h) for a random smooth h and t = log 2, log 3, 2 log 5, 0.37 (transforms by independent quadrature)",
      max(errs) < 1e-11, f"max relative difference {max(errs):.1e}")
L0, n0 = np.log(13), 41
Fa, Ma, _ = basis_a(L0, n0)
uu, ww = cgl([0.0, L0], 0.01)
ix = [0, 17, 40]
E = np.exp(1j * np.outer(2 * np.pi * np.arange(-20, 21)[ix] / L0, uu)) / np.sqrt(L0)
Fq = (np.exp(1j * np.outer(GAM[[0, 5, 999, 1500]], uu)) * ww) @ E.T
uu2, ww2 = cgl([0.0, LOG2, L0], 0.01)
E2 = np.exp(1j * np.outer(2 * np.pi * np.arange(-20, 21) / L0, uu2)) / np.sqrt(L0)
Esh = np.where(uu2 >= LOG2, 1, 0) * np.exp(1j * np.outer(2 * np.pi * np.arange(-20, 21) / L0, uu2 - LOG2)) / np.sqrt(L0)
Mq = (E2.conj() * ww2) @ Esh.T
check("A3 hard window: closed-form transforms and the closed-form compressed translation M = P chi U_log2 agree with quadrature",
      np.max(np.abs(Fq - Fa[np.ix_([0, 5, 999, 1500], ix)])) < 1e-10 and np.max(np.abs(Mq - Ma)) < 1e-12,
      f"transform {np.max(np.abs(Fq - Fa[np.ix_([0, 5, 999, 1500], ix)])):.1e}, M {np.max(np.abs(Mq - Ma)):.1e}")
s0, nH = 0.2, 30
xg = np.arange(-30, 30, 0.002)
PH = herm(nH, xg / s0) / np.sqrt(s0)
FHq = (np.exp(1j * np.outer(GAM[[0, 3, 40]], xg)) * 0.002) @ PH.T
FHc = np.sqrt(2 * np.pi * s0) * (1j) ** np.arange(nH)[None, :] * herm(nH, s0 * GAM[[0, 3, 40]]).T
check("A4 Hermite basis: hat(psi_k(u/s)/sqrt s)(g) = sqrt(2 pi s) i^k psi_k(s g), and the psi_k are orthonormal on the grid",
      np.max(np.abs(FHq - FHc)) < 1e-10 and np.max(np.abs((PH * 0.002) @ PH.T - np.eye(nH))) < 1e-12,
      f"{np.max(np.abs(FHq - FHc)):.1e}")

# ===============================================================================================================
print(f"      [{time.time() - T0:.0f} s]")
print("\n== B. The compressed translation by log 2 in three bases")
Ls = [np.log(13), np.log(100), 8.0, 16.0, 32.0]
rows = {}
def diag_ab(fb, L, n, lead=True):
    F, M, low = fb(L, n)
    A = gram(F)
    R = M.conj().T @ A @ M
    c, r = best_c(R, A)
    _, rl = best_c(R[np.ix_(low, low)], A[np.ix_(low, low)])
    rw = np.linalg.norm((R - A)[np.ix_(low, low)], 2) / np.linalg.norm(A, 2)
    return dict(c=c, r=r, rl=rl, rw=rw, frac=interior(M, A) / n, lead=lead_res(M, A) if lead else np.nan)


for L in Ls:
    for n in ((81, 321) if L < 20 else (321,)):      # n = 81 at L = 32 has bandwidth 7.9 < gamma_1: excluded
        for nm, fb in (('a', basis_a), ('b', basis_b)):
            rows[(nm, L, n)] = diag_ab(fb, L, n)
    J, A, S, Mo, Ao = basis_c(L, 16)
    R = S.T @ A @ S - A
    ii = np.arange(J - 16)
    c, r = best_c(S.T @ A @ S, A)
    rows[('c', L, J)] = dict(c=c, r=r, rin=np.max(np.abs(R[np.ix_(ii, ii)])) / np.max(np.abs(A)), J=J,
                            frac=(J - 16) / J, fracL2=interior(Mo, Ao) / J)
for nm, fb in (('a', basis_a), ('b', basis_b)):
    rows[(nm, 16.0, 641)] = diag_ab(fb, 16.0, 641, lead=False)
print("      low block: |n| <= 3 in (a), k < 7 in (b); 'own' = lane G's best-c residual on the block, 'whole' = ||R_low||_2 / ||A||_2")
print("      basis  L      n    best c   residual  low: own / whole       interior frac  1 - log2/L  leading-10 res")
for key in sorted(rows, key=lambda k: (k[0], k[1], k[2])):
    v = rows[key]
    nm, L, n = key
    if nm == 'c':
        print(f"      c   {L:6.2f} {n:5d}   {v['c']:.3f}    {v['r']:.3f}     interior block {v['rin']:.1e}   {v['frac']:.3f} "
              f"(L2 compression {v['fracL2']:.3f})  {1 - LOG2 / L:.3f}")
    else:
        print(f"      {nm}   {L:6.2f} {n:5d}   {v['c']:.3f}    {v['r']:.3f}     {v['rl']:.1e} / {v['rw']:.1e}      {v['frac']:.3f}         "
              f"{1 - LOG2 / L:.3f}       {v['lead']:.2e}")
ra = [rows[('a', L, 321)] for L in Ls]
check("B1 (a) the zero-sum model reproduces lane G's whole-window residuals (full Weil form, N = 160): 0.464 at x = 13, 0.433 at x = 100",
      abs(ra[0]['r'] - 0.464) < 0.01 and abs(ra[1]['r'] - 0.433) < 0.01, f"{ra[0]['r']:.3f}, {ra[1]['r']:.3f}")
check("B2 (a) on the low Fourier modes |n| <= 3 lane G's best-c residual on the block is O(1) (> 0.25) at every L from log 13 to 32 "
      "and both n: the hard edge is in every mode (against the whole form the block's defect shrinks with L, as its share of the form does)",
      all(v['rl'] > 0.25 for k, v in rows.items() if k[0] == 'a'),
      f"own {[round(float(rows[('a', L, 321)]['rl']), 2) for L in Ls]}, whole {[float('%.1e' % rows[('a', L, 321)]['rw']) for L in Ls]}")
check("B3 (a) the interior fraction (residual <= 1e-6) increases with L and lies in [1 - log2/L - 0.04, 1 - log2/L] at n = 321",
      all(ra[i + 1]['frac'] > ra[i]['frac'] for i in range(len(Ls) - 1))
      and all(1 - LOG2 / L - 0.04 <= v['frac'] <= 1 - LOG2 / L for L, v in zip(Ls, ra)),
      f"{[round(float(v['frac']), 3) for v in ra]} against {[round(float(1 - LOG2 / L), 3) for L in Ls]}")
rb = [rows[('b', L, 321)] for L in Ls]
check("B4 (b) smooth window: on the first 7 Hermite functions the residual is below 1e-12 of the whole form at every L for n >= 321 "
      "(at n = 81 the largest is 1.1e-6, at L = log 13 where s sqrt(14) is comparable to log 2)",
      all(v['rw'] < 1e-12 for k, v in rows.items() if k[0] == 'b' and k[2] >= 321),
      f"max over n >= 321: {max(v['rw'] for k, v in rows.items() if k[0] == 'b' and k[2] >= 321):.1e}; "
      f"over n = 81: {max(v['rw'] for k, v in rows.items() if k[0] == 'b' and k[2] == 81):.1e}")
check("B5 (b) the interior fraction increases with L, within 0.05 of the phase-space estimate 1 - (4/pi) log2/L (n = 321)",
      all(rb[i + 1]['frac'] > rb[i]['frac'] for i in range(len(Ls) - 1))
      and all(abs(v['frac'] - (1 - 4 / np.pi * LOG2 / L)) < 0.05 for L, v in zip(Ls, rb)),
      f"{[round(float(v['frac']), 3) for v in rb]} against {[round(float(1 - 4 / np.pi * LOG2 / L), 3) for L in Ls]}")
rc = [rows[[k for k in rows if k[0] == 'c' and k[1] == L][0]] for L in Ls]
check("B6 (c) Gaussian frame, d = log2/16: M^T G M = G exactly on the interior frame elements (all but the last m = 16), "
      "so the interior fraction is exactly 1 - m/J = 1 - log2/L; the L2-orthogonal compression agrees there",
      all(v['rin'] < 1e-12 for v in rc) and all(v['fracL2'] >= v['frac'] - 1e-12 for v in rc),
      f"interior-block residual max {max(v['rin'] for v in rc):.1e}; fractions {[round(float(v['frac']), 3) for v in rc]}")
check("B7 the whole-space best-c residual of the frame shift, which is exact on the interior, matches the hard window's at every L "
      "(within 0.04): the 'residual near 0.4' measures the edge share, not a failure of the dilation",
      all(abs(vc['r'] - va['r']) < 0.04 for vc, va in zip(rc, ra)),
      f"frame {[round(float(v['r']), 3) for v in rc]}, hard window {[round(float(v['r']), 3) for v in ra]}")
sc = {nm: [round(float(v['r'] * np.sqrt(L / LOG2)), 2) for L, v in zip(Ls, vv)] for nm, vv in (('a', ra), ('b', rb), ('c', rc))}
check("B8 the whole-space residual decreases from L = log 100 to 32 in all three bases, like (log2/L)^(1/2): "
      "residual * sqrt(L/log2) stays in [0.85, 1.7] (n = 321)",
      all(all(v[i + 1]['r'] < v[i]['r'] for i in range(1, len(Ls) - 1)) for v in (ra, rb, rc))
      and all(0.85 <= x <= 1.7 for vv in sc.values() for x in vv), f"{sc}")
check("B9 the residual is not an N effect: at L = 16, n = 321 -> 641 changes the whole-space residual by < 0.01 in (a) and (b)",
      abs(rows[('a', 16.0, 641)]['r'] - rows[('a', 16.0, 321)]['r']) < 0.01 and abs(rows[('b', 16.0, 641)]['r'] - rows[('b', 16.0, 321)]['r']) < 0.01,
      f"(a) {rows[('a', 16.0, 321)]['r']:.3f} -> {rows[('a', 16.0, 641)]['r']:.3f}; (b) {rows[('b', 16.0, 321)]['r']:.3f} -> {rows[('b', 16.0, 641)]['r']:.3f}")
check("B10 the leading 10 eigenvectors of the windowed form are not interior in (a) or (b): their residual is > 0.05 at every L "
      "and falls from L = log 13 to 32 (they fill the window, so they carry the edge share)",
      all(v['lead'] > 0.05 for v in ra + rb) and ra[-1]['lead'] < ra[0]['lead'] and rb[-1]['lead'] < rb[0]['lead'],
      f"(a) {[round(float(v['lead']), 2) for v in ra]}, (b) {[round(float(v['lead']), 2) for v in rb]}")

# ===============================================================================================================
print(f"      [{time.time() - T0:.0f} s]")
print("\n== C. The Gram matrix of translates by log 2 is Toeplitz, and its entries are the prime side's windowed Weil form")
Jt = 8
tau = 0.1


def gauss_hat2(g):          # |hat h|^2 for h(u) = exp(-u^2 / 2 tau^2)
    return 2 * np.pi * tau ** 2 * np.exp(-tau ** 2 * g ** 2)


def dyad_hat2(g):           # |hat h|^2 for h = 1_[0, log 2] (x in [1, 2])
    return 4 * np.sin(g * LOG2 / 2) ** 2 / g ** 2


def gram_translates(hat2, Kz):
    g = np.concatenate([ZEROS[:Kz], -ZEROS[:Kz]])
    F = np.sqrt(hat2(g))[:, None] * np.exp(1j * np.outer(g, np.arange(Jt + 1) * LOG2))
    return gram(F)


def nu_ef_gauss(d):
    t = d * LOG2
    return weil_ef(lambda u: tau * np.sqrt(np.pi) * np.exp(-(u - t) ** 2 / (4 * tau ** 2)), t + 16 * tau, [t])


def nu_ef_dyad(d):
    t = d * LOG2
    return weil_ef(lambda u: np.maximum(LOG2 - np.abs(u - t), 0.0), t + LOG2, [t - LOG2, t, t + LOG2])


def toep(nu):
    n = len(nu)
    return np.array([[nu[abs(i - j)] for j in range(n)] for i in range(n)])


Gg = gram_translates(gauss_hat2, K)
Gd = gram_translates(dyad_hat2, K)
tdev = max(np.max(np.abs(G[1:, 1:] - G[:-1, :-1])) / np.max(np.abs(G)) for G in (Gg, Gd))
check("C1 the zero-sum Gram matrix of the translates h(. - j log 2), j = 0..8, is Toeplitz (Gaussian and dyadic window): "
      "this is translation unitarity, i.e. the shift j -> j+1 is an exact similitude on the interior block",
      tdev < 1e-14, f"max |G[j+1,k+1] - G[j,k]| / max|G| = {tdev:.1e}")
nug = np.array([nu_ef_gauss(d) for d in range(Jt + 1)])
errg = np.max(np.abs(Gg[:, 0].real - nug)) / abs(nug[0])
check("C2 Gaussian window (tau = 0.1): the Toeplitz entries nu_d = Z(h, U_{d log 2} h), d = 0..8, from 1000 zeros equal the "
      "explicit formula (pole - primes - archimedean, no zeros used)", errg < 1e-12,
      f"max relative difference {errg:.1e} (about {int(-np.log10(errg))} digits); nu_0..2 = {nug[0]:.6e}, {nug[1]:.6e}, {nug[2]:.6e}")
nud = np.array([nu_ef_dyad(d) for d in range(Jt + 1)])


def smooth_tail(d, Kz):
    """Riemann-von Mangoldt density (1/2pi) log(g/2pi) above the K-th zero, applied to 2 |hat h|^2 cos(g d log 2)."""
    T = ZEROS[Kz - 1] + np.pi / np.log(ZEROS[Kz - 1] / (2 * np.pi))

    def I(s):
        if s == 0:
            return (np.log(T / (2 * np.pi)) + 1) / T
        f = np.log(T / (2 * np.pi)) / T ** 2
        fp = (1 - 2 * np.log(T / (2 * np.pi))) / T ** 3
        return -np.sin(s * T) * f / s - np.cos(s * T) * fp / s ** 2
    t = d * LOG2
    return (8 / (2 * np.pi)) * (0.5 * I(t) - 0.25 * I(t + LOG2) - 0.25 * I(abs(t - LOG2)))


print("      dyadic window h = 1_[0, log 2]: |zero sum - explicit formula| (raw / with smooth tail)")
dyrows = []
for Kz in (500, 1000, 3000):
    nz = gram_translates(dyad_hat2, Kz)[:, 0].real
    raw = np.abs(nz - nud)
    cor = np.abs(nz + np.array([smooth_tail(d, Kz) for d in range(Jt + 1)]) - nud)
    dyrows.append((Kz, raw, cor))
    print(f"      K = {Kz:4d}: d = 0: {raw[0]:.2e} / {cor[0]:.2e};  d = 1: {raw[1]:.2e} / {cor[1]:.2e};  "
          f"max over d = 2..8: {raw[2:].max():.2e} / {cor[2:].max():.2e}   (nu_0 = {nud[0]:.5f})")
check("C3 dyadic window: the zero sum converges to the explicit-formula entries as K = 500, 1000, 3000; on d = 0, 1 the error is the "
      "smooth Riemann-von Mangoldt tail (removing it leaves < 15% of the raw error); for d >= 2 the raw error is < 4e-5",
      all(dyrows[i + 1][1][0] < dyrows[i][1][0] for i in range(2))
      and all(r[2][dd] < 0.15 * r[1][dd] for r in dyrows for dd in (0, 1)) and all(r[1][2:].max() < 4e-5 for r in dyrows),
      f"relative error on nu_0 at K = 1000: raw {dyrows[1][1][0] / nud[0]:.1e}, after tail {dyrows[1][2][0] / nud[0]:.1e}")
evg = np.linalg.eigvalsh(toep(nug))
evd = np.linalg.eigvalsh(toep(nud))
check("C4 the 9 x 9 Toeplitz matrices built from the prime side alone are positive definite (Weil positivity on the span of the "
      "translates), with the zero-sum Gram matrix as its spectral model", evg.min() > 0 and evd.min() > 0,
      f"Gaussian: eigenvalues in [{evg.min():.2e}, {evg.max():.2e}]; dyadic: [{evd.min():.2e}, {evd.max():.2e}]")
thetas = np.array([0.6, 1.9])                  # a genus-two curve: Frobenius angles +-theta_1, +-theta_2
nuc = np.array([np.sum(2 * np.cos(dd * thetas)) for dd in range(Jt + 1)])
evc = np.linalg.eigvalsh(toep(nuc))
rk = lambda ev: int(np.sum(ev > 1e-10 * ev.max()))
check("C5 rank: a curve's Toeplitz form (trace sequence of 2g = 4 Frobenius angles) has rank 4 on every window of length >= 4; "
      "zeta's has full rank 9 (atoms gamma log 2 mod 2 pi, infinitely many)",
      rk(evc) == 4 and rk(evd) == 9 and rk(evg) == 9, f"ranks {rk(evc)}, dyadic {rk(evd)}, Gaussian {rk(evg)}")

# ===============================================================================================================
print(f"      [{time.time() - T0:.0f} s]")
print("\n== D. Omega_D(h, g) = Z(h, D^{-1} g) as a pairing on test functions")
tD, E1, E2, cc = 0.2, 15.0, 22.0, 0.3


def hD(u):                     # odd => mean zero
    return np.exp(-u ** 2 / (2 * tD ** 2)) * np.sin(E1 * u)


def gD(u):
    return np.exp(-(u - cc) ** 2 / (2 * tD ** 2)) * np.sin(E2 * (u - cc))


def hat_sin(g, E, c):           # transform of exp(-(u-c)^2/2t^2) sin(E (u-c))
    return np.exp(1j * g * c) * tD * np.sqrt(2 * np.pi) * (np.exp(-tD ** 2 * (g + E) ** 2 / 2) - np.exp(-tD ** 2 * (g - E) ** 2 / 2)) / 2j


Hh, Hg = hat_sin(GAM, E1, 0.0), hat_sin(GAM, E2, cc)
om_zero = np.sum(Hh * np.conj(Hg) / (1j * GAM))
print(f"      Omega_D(h, g) from the zero sum, K = 1000: {om_zero.real:+.12e} (imaginary part {om_zero.imag:.1e})")
dx = 0.001
xs = np.arange(-3.0, 3.0 + dx / 2, dx)
corr = np.correlate(hD(xs), gD(xs), mode='full') * dx       # c(x) = int h(u) g(u - x) du
xc = (np.arange(len(corr)) - (len(xs) - 1)) * dx
Kx = np.zeros_like(xc)
for gm in ZEROS[:K]:
    Kx += 2 * np.sin(gm * xc) / gm
om_kernel = np.sum(corr * Kx) * dx
check("D1 kernel formula: Omega_D(h, g) = int int h(u) conj g(v) K(u - v) du dv with the odd kernel K(x) = sum_{gamma>0} 2 sin(gamma x)/gamma "
      "= (C * sgn/2)(x), C = sum_gamma e^{i gamma x} the zero distribution", abs(om_kernel - om_zero) < 1e-10 * abs(om_zero),
      f"kernel {om_kernel:+.12e}, |diff| {abs(om_kernel - om_zero):.1e}")
mp.mp.dps = 20


def Hg_anti(u):                 # (H * g)(u) = int_{-inf}^u g, closed form through the complex error function
    out = []
    for v in u:
        w = (mp.mpf(float(v)) - cc - 1j * tD ** 2 * E2) / (tD * mp.sqrt(2))
        out.append(float(mp.im(tD * mp.sqrt(mp.pi / 2) * mp.exp(-tD ** 2 * E2 ** 2 / 2) * (1 + mp.erf(w)))))
    return np.array(out)


ua, wa = cgl([cc - 2.0, cc + 2.0], 0.02)
kv = Hg_anti(ua)
uq2, wq2 = cgl([cc - 2.0, cc + 2.0], 0.02)
gnum = np.array([np.sum(wq2[uq2 <= v] * gD(uq2[uq2 <= v])) for v in ua[::97]])
check("D2a the closed form of the antiderivative H * g (H the Heaviside function) is right: it vanishes at both ends "
      "(g has mean zero, so H * g = (sgn/2) * g) and matches direct integration", abs(kv[0]) < 1e-12 and abs(kv[-1]) < 1e-12
      and np.max(np.abs(gnum - kv[::97])) < 2e-3, f"ends {kv[0]:.1e}, {kv[-1]:.1e}")
Hk = (np.exp(1j * np.outer(GAM, ua)) * wa) @ kv
om_anti = np.sum(Hh * np.conj(Hk))
check("D2b Omega_D(h, g) = Z_K(h, H * g): the zero-sum form against the antiderivative, transformed by quadrature",
      abs(om_anti - om_zero) < 1e-9 * abs(om_zero), f"{om_anti.real:+.12e}, |diff| {abs(om_anti - om_zero):.1e}")
gq = np.arange(-400, 400, 0.25)                  # pair function p = h * (H*g)^* via its transform (no zeros used)


def pair_fn(Ha, Hb):
    with np.errstate(divide='ignore', invalid='ignore'):
        ph = Ha(gq) * np.conj(1j * Hb(gq) / gq)       # hat(H*k) = i hat k / g
    ph[np.abs(gq) < 1e-12] = Ha(np.array([1e-9]))[0] * np.conj(1j * Hb(np.array([1e-9]))[0] / 1e-9)
    return lambda u: np.real((np.exp(-1j * np.outer(np.atleast_1d(u), gq)) @ ph) * 0.25 / (2 * np.pi))


p_hg = pair_fn(lambda g: hat_sin(g, E1, 0.0), lambda g: hat_sin(g, E2, cc))
p_gh = pair_fn(lambda g: hat_sin(g, E2, cc), lambda g: hat_sin(g, E1, 0.0))
om_ef = weil_ef(p_hg, 3.5)
om_ef_rev = weil_ef(p_gh, 3.5)
check("D3 Omega_D(h, g) = B(h, H * g) computed from the prime side (explicit formula on the pair function of h and H * g) equals "
      "the zero sum over 1000 zeros", abs(om_ef - om_zero.real) < 1e-9 * abs(om_zero), f"explicit formula {om_ef:+.12e}, |diff| {abs(om_ef - om_zero.real):.1e}")
check("D4 antisymmetry from the prime side alone: Omega_D(h, g) + Omega_D(g, h) = 0 for real mean-zero h, g (the Loewner identity "
      "of lane G B5, on the line instead of the window)", abs(om_ef + om_ef_rev) < 1e-9 * abs(om_ef),
      f"{om_ef:+.6e} + ({om_ef_rev:+.6e}) = {om_ef + om_ef_rev:.1e}")

sgK = 0.005                                       # K * Gaussian(sigma): the zero sum converges (gamma_K sigma = 7)
x1, x2 = np.log(2.5), np.log(34.5)              # mid-gap points, >= 14 sigma from every prime power
Ks = [np.sum(2 * np.sin(ZEROS[:K] * x) / ZEROS[:K] * np.exp(-sgK ** 2 * ZEROS[:K] ** 2 / 2)) for x in (x1, x2)]
lu_, wt_ = mangoldt(40)
stair = np.sum(wt_[(lu_ > x1) & (lu_ < x2)])
uy, wy = cgl([x1, x2], 0.05)
smooth = 4 * np.sinh(x2 / 2) - 4 * np.sinh(x1 / 2) - np.sum(wy / (np.exp(uy / 2) - np.exp(-1.5 * uy)))
check("D5 the kernel of Omega_D is the integrated Weil distribution, K' = W: for 0 < x1 < x2, K(x2) - K(x1) = [4 sinh(x/2)] - "
      "sum_{x1 < log n < x2} Lambda(n)/sqrt n - int dx/(e^{x/2} - e^{-3x/2}); its prime part is the weighted Chebyshev staircase "
      "(x1 = log 2.5, x2 = log 34.5, zero side smoothed at sigma = 0.005)", abs((Ks[1] - Ks[0]) - (smooth - stair)) < 1e-3,
      f"zeros {Ks[1] - Ks[0]:+.6f}, primes {smooth - stair:+.6f} (staircase {stair:.6f}), |diff| {abs((Ks[1] - Ks[0]) - (smooth - stair)):.1e}")

print(f"\n{npass} of {npass + nfail} pass" + ("" if nfail == 0 else f"  ({nfail} FAIL)") + f"   [{time.time() - T0:.0f} s]")
