#!/usr/bin/env python3
"""Checks for 'The three ingredients for zeta: what exists on Connes's cokernel' (notes/adelic-gkp/zeta-ingredients.md), lane G.

Conventions (analytic.md, conventions line; adelic-gkp.md section 10).  u = log x.  For a test function h(u),
F_h(s) = int h(u) e^{(s-1/2)u} du, h^*(u) = conj h(-u), g = h1 * h2^*, ghat(s) = F_1(s) conj F_2(1 - conj s).
Weil's form  Z(h1,h2) = sum_rho ghat(rho) = Pole - Prime - Arch  (explicit formula), with
  Pole  = ghat(0) + ghat(1),
  Prime = sum_n Lambda(n) n^{-1/2} (g(log n) + g(-log n)),
  Arch  = (log 4 pi + gamma_E) g(0) + int_0^U [g(u) + g(-u) - 2 e^{-u/2} g(0)] / (e^{u/2} - e^{-3u/2}) du - g(0) log coth(U/2)
for g supported in [-U, U] (Weil's archimedean term, from memory; validated in A2 against the zeros).
Window model (the notebook's CCM window form): h supported in [0, L], L = log x, basis e_n = e^{i w_n u}/sqrt(L),
w_n = 2 pi n / L, n = -N..N.  G_N[m,n] = Z(e_m, e_n) (real symmetric).  Pole part P_N, local part Loc = Prime + Arch.
Step: the normalised translation (U_a h)(u) = h(u - a) (unitary in L^2(du); the unnormalised dilation x -> a x has
multiplier a), compressed to the window: M_N = P_N chi U_a.

Sections: A zeros and the explicit formula; B the window form (against the notebook's reviewer helper, the zeros, the
Loewner identity); C inertia (item 3; high precision through the helper); D the compressed prime-2 dilation (item 2);
E the spectral (cokernel) model and the Omega question.

Needs numpy, sympy, mpmath, and notes/reviews/scratch_rtp2_grid_common.py (the REFUTE reviewer's CCM window helper).
Run from anywhere:  python3 check_zeta_ingredients.py > output_zeta_ingredients.txt   (about 30 s)
"""
import os
import sys
import time
from functools import lru_cache

import numpy as np
import mpmath as mp
from sympy import primerange

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'notes', 'reviews'))
from scratch_rtp2_grid_common import ab_true  # noqa: E402

T0 = time.time()
npass = nfail = 0
EG = 0.5772156649015329


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


# ---------------------------------------------------------------------------------------------------------------
# explicit formula machinery
@lru_cache(None)
def _lg(n):
    return np.polynomial.legendre.leggauss(n)


def gl(a, b, n):
    x, w = _lg(n)
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w


@lru_cache(None)
def vm(X):
    """(log n, Lambda(n)/sqrt(n)) for prime powers n <= X."""
    out = []
    for p in primerange(2, int(X) + 1):
        pk = p
        while pk <= X:
            out.append((pk, np.log(p)))
            pk *= p
    out.sort()
    n = np.array([o[0] for o in out], float)
    return np.log(n), np.array([o[1] for o in out]) / np.sqrt(n)


def weil_generic(g, U, nq=6000):
    """Z for g supported in [-U, U] (callable, vectorised, complex allowed); returns (value, parts)."""
    u, w = gl(0, U, nq)
    gp, gm = g(u), g(-u)
    g0 = g(np.array([0.0]))[0]
    pole = np.sum(w * (gp * np.exp(-u / 2) + gm * np.exp(u / 2))) + np.sum(w * (gp * np.exp(u / 2) + gm * np.exp(-u / 2)))
    lu, wt = vm(int(np.exp(U)))
    sel = lu < U
    prime = np.sum(wt[sel] * (g(lu[sel]) + g(-lu[sel])))
    arch = ((np.log(4 * np.pi) + EG) * g0 + np.sum(w * (gp + gm - 2 * np.exp(-u / 2) * g0) / (np.exp(u / 2) - np.exp(-1.5 * u)))
            - g0 * np.log(1 / np.tanh(U / 2)))
    return pole - prime - arch, dict(pole=pole, prime=prime, arch=arch)


def weil_pair_seg(nu1, nu2, ell, nq=6000):
    """Z(h1, h2) for h_i = exp(i nu_i v) 1_[0,ell](v) (unnormalised), from the closed form of g = h1 * h2^*."""
    D = nu1 - nu2

    def g(u):
        u = np.asarray(u, float)
        lo = np.maximum(0, u)
        hi = np.minimum(ell, ell + u)
        if abs(D) < 1e-13:
            I = np.maximum(hi - lo, 0).astype(complex)
        else:
            I = np.where(hi > lo, (np.exp(1j * D * hi) - np.exp(1j * D * lo)) / (1j * D), 0)
        return np.exp(1j * nu2 * u) * I
    return weil_generic(g, ell, nq)[0]


def window_parts(L, N, nq=4000):
    """CCM window form on [0, L] in the basis e_n, split into pole / prime / arch (Z = pole - prime - arch).
    Diagonal: functional of g_nn = (1 - |u|/L) e^{i w u}; off-diagonal: g_mn = sgn(u)(e^{i w_n u} - e^{i w_m u})/(i (w_m - w_n) L)."""
    idx = np.arange(-N, N + 1)
    om = 2 * np.pi * idx / L
    u, w = gl(0, L, nq)
    lu, wt = vm(int(np.exp(L)))
    sel = lu < L
    lu, wt = lu[sel], wt[sel]
    C = np.cos(np.outer(om, u))
    S = np.sin(np.outer(om, u))
    ker = 1 / (np.exp(u / 2) - np.exp(-1.5 * u))
    A = {'pole': C @ (w * (1 - u / L) * 4 * np.cosh(u / 2)),
         'prime': np.cos(np.outer(om, lu)) @ (wt * 2 * (1 - lu / L)),
         'arch': (np.log(4 * np.pi) + EG) - np.log(1 / np.tanh(L / 2)) + (2 * C * (1 - u / L) - 2 * np.exp(-u / 2)) @ (w * ker)}
    B = {'pole': S @ (w * 4 * np.cosh(u / 2)),
         'prime': np.sin(np.outer(om, lu)) @ (wt * 2),
         'arch': S @ (w * 2 * ker)}
    out = {}
    dO = om[None, :] - om[:, None]
    for k in A:
        b = B[k]
        with np.errstate(divide='ignore', invalid='ignore'):
            M = (b[None, :] - b[:, None]) / (-dO * L)
        M[np.arange(len(idx)), np.arange(len(idx))] = A[k]
        out[k] = M
    return idx, om, out


def window_Z(L, N, nq=4000):
    idx, om, p = window_parts(L, N, nq)
    return idx, om, p['pole'] - p['prime'] - p['arch'], p


def Fwin(s, om, L):
    """F_m(s) for e_m on [0, L] (w_m L in 2 pi Z)."""
    s = np.asarray(s, complex)
    z = s - 0.5 + 1j * om
    with np.errstate(divide='ignore', invalid='ignore'):
        v = (np.exp((s - 0.5) * L) - 1) / z
    return np.where(np.abs(z) < 1e-14, L, v) / np.sqrt(L)


def shift_matrix(om, L, a):
    """compressed translation: M[m,n] = <e_m, chi_[0,L] U_a e_n>_{L^2}."""
    dn = om[None, :] - om[:, None]
    with np.errstate(divide='ignore', invalid='ignore'):
        M = (1 - np.exp(1j * dn * a)) / (1j * dn * L)
    np.fill_diagonal(M, (L - a) / L)
    return M * np.exp(-1j * om[None, :] * a)


def best_c(R, G):
    c = np.real(np.vdot(G, R)) / np.real(np.vdot(G, G))
    return c, np.linalg.norm(R - c * G) / np.linalg.norm(G)


def full_mp(a, b, N):
    idx = list(range(-N, N + 1))
    n = len(idx)
    Q = mp.matrix(n, n)
    A = lambda j: a[abs(j)]
    B = lambda j: b[j] if j >= 0 else -b[-j]
    for r, j in enumerate(idx):
        for c, k in enumerate(idx):
            Q[r, c] = A(j) if j == k else (B(j) - B(k)) / (j - k)
    return Q


def F_mp(s, m, L):
    return (mp.exp((s - mp.mpf(1) / 2) * L) - 1) / (s - mp.mpf(1) / 2 + 2j * mp.pi * m / L) / mp.sqrt(L)


def pole_mp(x, N):
    L = mp.log(x)
    idx = list(range(-N, N + 1))
    n = len(idx)
    P = mp.matrix(n, n)
    for r, j in enumerate(idx):
        for c, k in enumerate(idx):
            P[r, c] = mp.re(F_mp(0, j, L) * mp.conj(F_mp(1, k, L)) + F_mp(1, j, L) * mp.conj(F_mp(0, k, L)))
    return P


def inertia_mp(M, tol):
    e = sorted(mp.eigsy(M)[0])
    return sum(1 for v in e if v > tol), sum(1 for v in e if v < -tol), sum(1 for v in e if abs(v) <= tol), e


zeros = np.load(os.path.join(ROOT, 'data', 'zeros3000.npy'))

# ===============================================================================================================
print("== A. Zeros and the explicit formula")
mp.mp.dps = 20
zz = [float(mp.im(mp.zetazero(k))) for k in (1, 2, 3)]
check("A1 data/zeros3000.npy agrees with mpmath zetazero(1..3); 3000 ordinates up to 3533.33",
      max(abs(zz[i] - zeros[i]) for i in range(3)) < 1e-10 and len(zeros) == 3000,
      f"gamma_1 = {zeros[0]:.12f}")
for s in (0.15, 0.25, 0.4):
    g = lambda u, s=s: np.exp(-u ** 2 / (2 * s * s))
    zero_side = 2 * np.sum(s * np.sqrt(2 * np.pi) * np.exp(-s * s * zeros ** 2 / 2))
    val, parts = weil_generic(g, 12 * s + 4)
    check(f"A2 explicit formula, Gaussian g = exp(-u^2/2s^2), s = {s}: zero side (3000 zeros) = Pole - Prime - Arch",
          abs(zero_side - val) < 1e-9,
          f"zeros {zero_side:.12e}, primes {val:.12e}, diff {abs(zero_side - val):.1e}; prime part {parts['prime']:.3e}")

# ===============================================================================================================
print("\n== B. The window form G_N (CCM model, [0, L], L = log x)")
x, N = 13, 10
L = np.log(x)
idx, om, G, parts = window_Z(L, N)
mp.mp.dps = 30
a_, b_ = ab_true(x, N)
Qh = np.array([[float(v) for v in row] for row in full_mp(a_, b_, N).tolist()])
check("B1 G_N from the explicit formula equals the notebook's CCM window form (reviewer helper ab_true, x = 13, N = 10)",
      np.max(np.abs(G - Qh)) < 1e-10, f"max |diff| = {np.max(np.abs(G - Qh)):.1e}, max |G| = {np.max(np.abs(G)):.3f}")
f0, f1 = Fwin(0, om, L), Fwin(1, om, L)
P2 = np.real(np.outer(f0, f1.conj()) + np.outer(f1, f0.conj()))
eP = np.linalg.eigvalsh(parts['pole'])
check("B2 pole part = F(0)F(1)^+ + F(1)F(0)^+ (the two constant terms of the comb): rank 2, signature (1,1)",
      np.max(np.abs(P2 - parts['pole'])) < 1e-10 and np.sum(eP > 1e-9) == 1 and np.sum(eP < -1e-9) == 1,
      f"eigenvalues {eP[0]:.4f}, {eP[-1]:.4f}")
x5, N5 = 13, 5
L5 = np.log(x5)
idx5, om5, G5, _ = window_Z(L5, N5)
Fz = np.array([Fwin(0.5 + 1j * gm, om5, L5) for gm in np.concatenate([zeros, -zeros])])   # rows: zeros
Gz = np.real(Fz.T @ Fz.conj())
T = zeros[-1]
tail = 2 / (np.pi * L5) * (np.log(T / (2 * np.pi)) + 1) / T
dd = np.diag(G5 - Gz)
check("B3 zero side (3000 critical zeros, sum F_m(rho) conj F_n(rho)) against the prime side: the diagonal deficit is positive and "
      "below the Riemann-von Mangoldt tail estimate 2(log(T/2pi)+1)/(pi L T)",
      np.all(dd > 0) and np.all(dd < 1.5 * tail) and np.max(np.abs(G5 - Gz)) < 1.5 * tail,
      f"max |G - G_zeros| = {np.max(np.abs(G5 - Gz)):.2e}, tail estimate {tail:.2e}")
mm, nn = np.meshgrid(idx5, idx5, indexing='ij')
i0 = N5
lw = (mm - nn) * Gz - (mm * Gz[:, i0][:, None] - nn * Gz[:, i0][None, :])
check("B4 Loewner identity (m-n) G[m,n] = m G[m,0] - n G[n,0] holds for the zero-side matrix built term by term "
      "(each critical zero's rank-one form is skew for the squeeze generator D)",
      np.max(np.abs(lw)) < 1e-12 * np.max(np.abs(Gz)), f"max defect {np.max(np.abs(lw)):.1e}")
x20, N20 = 13, 20
idx20, om20, G20, _ = window_Z(np.log(x20), N20)
nz = idx20 != 0
Tm = np.zeros((len(idx20), len(idx20)), complex)            # D^{-1} e_n = (e_n - e_0)/(i w_n) on mean-zero functions
for j, n_ in enumerate(idx20):
    if n_ != 0:
        Tm[j, j] = 1 / (1j * om20[j])
        Tm[N20, j] = -1 / (1j * om20[j])
Om = (G20 @ Tm.conj())[np.ix_(nz, nz)]                      # Omega_N(h, k) = G_N(h, D^{-1} k) on W^0 = {mean zero}
check("B5 Omega_N(h,k) := G_N(h, D^{-1}k) is anti-Hermitian on the 2N-dimensional mean-zero window space (x = 13, N = 20): "
      "the infinitesimal step is an exact similitude on every window (notebook C3.2, restricted to the kernel of the boundary covector)",
      np.max(np.abs(Om + Om.conj().T)) < 1e-12 * np.max(np.abs(Om)),
      f"max |Om + Om^+| = {np.max(np.abs(Om + Om.conj().T)):.1e}, max |Om| = {np.max(np.abs(Om)):.2f}")

# ===============================================================================================================
print("\n== C. Item 3: inertia of the window form, the pole plane, and synthetic off-line pairs (mpmath, helper data)")
for (xx, NN, dps) in [(13, 5, 40), (13, 10, 50), (13, 15, 60)]:
    mp.mp.dps = dps
    a_, b_ = ab_true(xx, NN)
    H = full_mp(a_, b_, NN)
    P = pole_mp(xx, NN)
    n = 2 * NN + 1
    tol = mp.mpf(10) ** (-(dps - 8))
    iZ = inertia_mp(H, tol)
    iP = inertia_mp(P, tol)
    iM = inertia_mp(H - P, tol)
    iPl = inertia_mp(H + P, tol)
    ok = (iZ[:3] == (n, 0, 0) and iP[:3] == (1, 1, n - 2) and iM[:3] == (n - 1, 1, 0) and iPl[:3] == (n - 1, 1, 0))
    check(f"C1 x = {xx}, N = {NN} ({dps} digits): Z_N > 0; pole form P_N signature (1,1); Z_N - P_N (= -Loc) and Z_N + P_N each have "
          f"inertia (n-1, 1, 0), n = {n}",
          ok, f"min eig Z = {mp.nstr(iZ[3][0], 3)}; negative eig of Z-P = {mp.nstr(iM[3][0], 5)}, of Z+P = {mp.nstr(iPl[3][0], 5)}; "
              f"next eig of Z-P = {mp.nstr(iM[3][1], 3)}")
mp.mp.dps = 50
xx, NN = 13, 10
a_, b_ = ab_true(xx, NN)
H = full_mp(a_, b_, NN)
P = pole_mp(xx, NN)
Lm = mp.log(xx)
n = 2 * NN + 1
for beta, g0 in [(0.75, 5.0), (0.6, 14.134725)]:
    rhos = [mp.mpc(beta, g0), mp.mpc(beta, -g0), mp.mpc(1 - beta, g0), mp.mpc(1 - beta, -g0)]
    Q4 = mp.matrix(n, n)
    for r, j in enumerate(range(-NN, NN + 1)):
        for c, k in enumerate(range(-NN, NN + 1)):
            Q4[r, c] = mp.re(sum(F_mp(rho, j, Lm) * mp.conj(F_mp(1 - mp.conj(rho), k, Lm)) for rho in rhos))
    tol = mp.mpf(10) ** -42
    i1 = inertia_mp(H + Q4, tol)
    i2 = inertia_mp(H + Q4 - P, tol)
    check(f"C2 a synthetic off-line quartet rho = {beta} +- {g0} i (two pairs rho, 1 - conj rho) added to Z_N (x = 13, N = 10): "
          "negative index 2 for Z + Q, 3 for Z + Q - P (one hyperbolic plane per off-line pair, plus the pole plane)",
          i1[1] == 2 and i2[1] == 3, f"negative eigenvalues of Z + Q: {[mp.nstr(v, 3) for v in i1[3][:2]]}")

# ===============================================================================================================
print("\n== D. Item 2: the prime-2 dilation compressed to the window")
a = np.log(2)
K = 3
rows = []
for xx in (13, 100):
    LL = np.log(xx)
    idxK = np.arange(-K, K + 1)
    omK = 2 * np.pi * idxK / LL
    _, _, GK, _ = window_Z(LL, K)
    G0 = np.array([[weil_pair_seg(omK[i], omK[j], LL) / LL for j in range(2 * K + 1)] for i in range(2 * K + 1)])
    check(f"D1 x = {xx}: the generic explicit-formula route (closed-form g, any frequencies) reproduces G_K on the lattice frequencies",
          np.max(np.abs(G0 - GK)) < 1e-9, f"max diff {np.max(np.abs(G0 - GK)):.1e}")
    Rinf = np.array([[weil_pair_seg(omK[i], omK[j], LL - a) / LL for j in range(2 * K + 1)] for i in range(2 * K + 1)])
    cinf, rinf = best_c(Rinf, GK)
    res = []
    for NN in (5, 10, 20, 40, 80, 160):
        idx_, om_, G_, _ = window_Z(LL, NN)
        M = shift_matrix(om_, LL, a)
        R = M.T @ G_ @ M.conj()                       # G(M h, M k) = h^T (M^T G conj M) conj k
        c, r = best_c(R, G_)
        sel = np.abs(idx_) <= K
        RK = R[np.ix_(sel, sel)]
        cK, rK = best_c(RK, G_[np.ix_(sel, sel)])
        sv = np.linalg.svd(M, compute_uv=False)
        res.append((NN, len(idx_), c, r, cK, rK, np.max(np.abs(RK - Rinf)), int(np.sum(sv < 0.5)), len(idx_) * a / LL))
        print(f"      x = {xx:4d} N = {NN:3d}: whole window best c = {c:.4f}, residual {r:.4f} | modes |n| <= {K}: c = {cK:.4f}, "
              f"residual {rK:.4f}, distance to the cut limit {res[-1][6]:.2e} | #(sing. values of M_N < 1/2) = {res[-1][7]}, "
              f"n log2 / L = {res[-1][8]:.1f}")
    rows.append((xx, rinf, cinf, res))
    check(f"D2 x = {xx}: on the whole window the best-c residual of M^T G M = c G stays above 0.35 for N = 5..160 (does not shrink)",
          all(rr[3] > 0.35 for rr in res), f"residuals {[round(float(rr[3]), 3) for rr in res]}")
    dist = [rr[6] for rr in res]
    check(f"D3 x = {xx}: on the low modes |n| <= {K} the pulled-back form converges as N grows to the cut limit "
          f"W(chi U e_m, chi U e_n) (a window of length L - log 2), whose best-c residual is {rinf:.3f} (c = {cinf:.3f}): a nonzero limit",
          all(dist[i + 1] < dist[i] for i in range(len(dist) - 1)) and dist[-1] < 3e-3 and rinf > 0.3,
          f"distances {[f'{d:.1e}' for d in dist]}")
    check(f"D4 x = {xx}: the number of singular values of M_N below 1/2 is n log 2 / L to within 1 (the window loses that "
          "fraction of its dimension per step; M_N is never invertible in the limit)",
          all(abs(rr[7] - rr[8]) <= 1.0 for rr in res), f"{[(rr[7], round(float(rr[8]), 1)) for rr in res]}")
    # subspace supported away from the edge
    l0 = LL - a
    nus = [0.0, 2 * np.pi / l0, -2 * np.pi / l0, 4 * np.pi / l0]
    uu, ww = gl(0, LL, 6000)
    Hs = np.array([np.where(uu < l0, np.sin(np.pi * uu / l0) ** 4, 0) * np.exp(1j * nu * uu) for nu in nus])
    sres = []
    for NN in (20, 40, 80, 160):
        idx_, om_, G_, _ = window_Z(LL, NN)
        E = np.exp(1j * np.outer(om_, uu)) / np.sqrt(LL)
        Cc = (Hs * ww) @ E.conj().T
        M = shift_matrix(om_, LL, a)
        Gs = Cc @ G_ @ Cc.conj().T
        MC = (M @ Cc.T).T
        Rs = MC @ G_ @ MC.conj().T
        sres.append(np.linalg.norm(Rs - Gs) / np.linalg.norm(Gs))
    check(f"D5 x = {xx}: on the 4-dim subspace of smooth functions supported in [0, L - log 2], M^T G M = G (c = 1, normalised; "
          "c = 2 unnormalised) with residual -> 0 as N grows (translation invariance survives compression away from the edge)",
          all(sres[i + 1] < sres[i] for i in range(len(sres) - 1)) and sres[-1] < 1e-6,
          f"residuals at c = 1, N = 20, 40, 80, 160: {[f'{v:.1e}' for v in sres]}")
check("D6 the cut-limit residual does not decrease from x = 13 (log2/L = 0.27) to x = 100 (log2/L = 0.15): the defect is an edge "
      "effect of size O(1) on Fourier modes, not a fraction log p / L",
      rows[1][1] > 0.8 * rows[0][1], f"cut-limit residuals {rows[0][1]:.3f}, {rows[1][1]:.3f}")

# ===============================================================================================================
print("\n== E. The spectral (cokernel) model and the Omega question")
gam = zeros
for p in (2, 3, 5):
    wts = np.sqrt(p) * np.sin(gam * np.log(p))
    fneg = np.mean(wts < 0)
    check(f"E1 p = {p}: the lane-E Weil form (1/2) Omega_FE(M_p - V_p) of the dilation by p, on the first 3000 critical modes, "
          "has weights sqrt(p) sin(gamma log p) relative to Weil's form: indefinite",
          0.4 < fneg < 0.6, f"fraction of negative weights {fneg:.3f}")
lam2 = 2 ** (0.5 + 1j * gam)
Bw = np.ones_like(gam)
Om2 = 2 * Bw / np.conj(lam2 - 2 / lam2)                      # Omega_2(x,y) = 2 B(x, (M - V)^{-1} y) on the diagonal
W2 = 0.5 * Om2 * np.conj(lam2 - 2 / lam2)
check("E2 Omega_p := 2 B (M_p - V_p)^{-1} (diagonal in evaluation coordinates) is anti-Hermitian, compatible "
      "(|p^rho|^2 = p), and its Weil form is B exactly; its weights 1/(sqrt p sin(gamma log p)) have small divisors",
      np.max(np.abs(Om2.real) / np.abs(Om2)) < 1e-8 and np.max(np.abs(np.abs(lam2) ** 2 - 2)) < 1e-12
      and np.max(np.abs(W2 - Bw)) < 1e-12,
      f"max |weight| over 3000 zeros = {np.max(np.abs(Om2)):.1f} (min |sin(gamma log 2)| = {np.min(np.abs(np.sin(gam * np.log(2)))):.2e})")
ratio = (np.sqrt(2) * np.sin(gam * np.log(2))) / (np.sqrt(3) * np.sin(gam * np.log(3)))
check("E3 no single compatible Omega makes B the Weil form of both p = 2 and p = 3: that needs sqrt2 sin(g log2) / (sqrt3 sin(g log3)) "
      "constant over the zeros, and it is not",
      np.std(ratio[:200]) > 0.5 * np.mean(np.abs(ratio[:200])),
      f"ratio over the first 5 zeros {np.round(ratio[:5], 3).tolist()}")
t = 1e-6
inf = np.sign(gam) * np.sin(gam * t) / t
check("E4 infinitesimal step: (1/2t) Omega_FE(e^{tD} - e^{-tD}) -> Omega_FE(., D .), weights |gamma| (positive); "
      "relative to Omega_D := B(., D^{-1} .) the Williamson weights of B are |gamma| (the analogue of Im alpha_j)",
      np.max(np.abs(inf / gam - 1)) < 1e-5 and np.all(inf > 0), f"weights for the first three zeros {np.round(inf[:3], 4).tolist()}")
rng = np.random.default_rng(7)
q = 2.0
n = 6
A0 = rng.standard_normal((n, n))
Gr = A0 @ A0.T + n * np.eye(n)
th = [0.7, 1.9, 2.6]
Rot = np.zeros((n, n))
for i, tt in enumerate(th):
    Rot[2 * i:2 * i + 2, 2 * i:2 * i + 2] = [[np.cos(tt), -np.sin(tt)], [np.sin(tt), np.cos(tt)]]
ev, U_ = np.linalg.eigh(Gr)
Gh = U_ @ np.diag(np.sqrt(ev)) @ U_.T
Mr = np.sqrt(q) * np.linalg.inv(Gh) @ Rot @ Gh
Vr = q * np.linalg.inv(Mr)
Omr = 2 * Gr @ np.linalg.inv(Mr - Vr)
check("E5 Proposition 1 (random real example, q = 2, n = 6): if M^T G M = q G and M - V is invertible, then Omega := 2 G (M - V)^{-1} "
      "is alternating, compatible (M^T Omega M = q Omega), and (1/2) Omega (M - V) = G",
      np.allclose(Mr.T @ Gr @ Mr, q * Gr) and np.allclose(Omr, -Omr.T) and np.allclose(Mr.T @ Omr @ Mr, q * Omr)
      and np.allclose(0.5 * Omr @ (Mr - Vr), Gr))

print(f"\n{npass} of {npass + nfail} pass" + ("" if nfail == 0 else f"  ({nfail} FAIL)") + f"   [{time.time() - T0:.0f} s]")
