#!/usr/bin/env python3
"""metric_blocker_checks.py -- checks for notes/weil-bond-analytic/analytic.md (author line: claude:fable-5.1, 2026-10-01).

Uses the REFUTE reviewer's window helpers (notes/reviews/scratch_rtp2_grid_common.py: pole + archimedean + prime
(a_n, b_n) of the CCM window form, checked there against zst to 1e-50) and the pole-only data of
scripts/rtp2_blind_recovery.py.  No zero of zeta enters any check except the comparison table in C3 (labelled).

A  Pontryagin index of the pole-free (local) window form: H = full window form, P = pole part, H - P = local
   (archimedean + primes).  Certificate: Cholesky of H succeeds at the working precision (H > 0, hence
   ind_-(H - P) <= ind_-(-P) = 1) and an explicit witness v with v^T (H - P) v < 0 (hence = 1).
   Also: P has rank two, signature (1, 1); H - P >= 0 on the kernel of either isotropic functional of P.
B  CCM approximant moments versus xi: sigma_2k(window) = sum over the window roots (frequency 2 pi s / L, both
   signs) of root^(-2k), read off the Taylor series of log P_N at 0 (Newton sums; no root finding), against
   sigma_2k(Xi) = -2k [t^2k] log Xi(t), Xi(t) = xi(1/2 + i t), computed from xi by mpmath (no zeros used).
   Also the Laguerre-Polya growth bound |P(z)| <= P(0) exp(sigma_2 |z|^2 / 2) at sample complex points.
C  The window spectrum (x = 13, N = 30): all 2N roots real (eigenvalues of D' = D - |D xi><eta|) and the
   comparison table with the first zeros (comparison only).

Run from the repo root:  python3 notes/weil-bond-analytic/checks/metric_blocker_checks.py > notes/weil-bond-analytic/checks/output.txt
Runtime about 4 minutes (the x = 25 case is at 180 digits).
"""
import sys, os, inspect
import mpmath as mp
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'notes', 'reviews')); sys.path.insert(0, os.path.join(ROOT, 'scripts'))
os.chdir(ROOT)
from scratch_rtp2_grid_common import ab_true            # noqa: E402
from rtp2_blind_recovery import pole_ab                  # noqa: E402

_P = _F = 0
def check(cond, msg):
    global _P, _F
    ok = bool(cond); _P += ok; _F += (not ok)
    print(('PASS ' if ok else 'FAIL ') + f'[l{inspect.currentframe().f_back.f_lineno}] ' + msg)

def full(a, b, N):
    idx = list(range(-N, N + 1)); n = len(idx); Q = mp.matrix(n, n)
    A = lambda j: a[abs(j)]; B = lambda j: b[j] if j >= 0 else -b[-j]
    for r, j in enumerate(idx):
        for c, k in enumerate(idx):
            Q[r, c] = A(j) if j == k else (B(j) - B(k)) / (j - k)
    return Q

def Xi(t):
    s = mp.mpf(1) / 2 + 1j * t
    return mp.re(s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s))

def case(x, N, dps):
    mp.mp.dps = dps
    print(f'\n## x = {x}, N = {N}, dps = {dps}')
    L = mp.log(x); n = 2 * N + 1; idx = list(range(-N, N + 1))
    at, bt = ab_true(x, N); ap, bp = pole_ab(x, N)
    H = full(at, bt, N); P = full(ap, bp, N); Lc = H - P
    # ---- A
    try:
        mp.cholesky(H); ok = True
    except ZeroDivisionError:
        ok = False
    except ValueError:
        ok = False
    check(ok, f'A1 x={x} N={N}: Cholesky of the full window form succeeds at {dps} digits (H > 0)')
    eP, VP = mp.eigsy(P)
    nz = sorted([e for e in eP if abs(e) > mp.mpf(10) ** (-dps // 2)])
    check(len(nz) == 2 and nz[0] < 0 < nz[1], f'A2 pole form: rank 2, signature (1,1), eigenvalues {mp.nstr(nz[0], 6)}, {mp.nstr(nz[1], 6)}')
    kp = max(range(n), key=lambda i: eP[i]); km = min(range(n), key=lambda i: eP[i])
    vp = VP[:, kp]; vm = VP[:, km]
    wit = (vp.T * Lc * vp)[0]
    check(wit < 0, f'A3 witness: v_+^T (H - P) v_+ = {mp.nstr(wit, 8)} < 0; with A1-A2 the local form has negative index exactly 1')
    sp, sm = mp.sqrt(eP[kp]), mp.sqrt(-eP[km])
    fa = (sp * vp + sm * vm) / mp.sqrt(2); fb = (sp * vp - sm * vm) / mp.sqrt(2)
    rec = fa * fb.T + fb * fa.T
    check(mp.mnorm(rec - P, 1) < mp.mpf(10) ** (-dps // 2), 'A4 P = a b^T + b a^T with the two isotropic functionals a, b (real)')
    for name, f in (('a', fa), ('b', fb)):
        # orthonormal basis of ker f^T: Householder-free, via eigenvectors of I - f f^T/|f|^2
        Pf = mp.eye(n) - f * f.T / (f.T * f)[0]
        ev, V = mp.eigsy(Pf)
        Bk = mp.matrix(n, n - 1); c = 0
        for i in range(n):
            if ev[i] > mp.mpf(1) / 2:
                for r in range(n): Bk[r, c] = V[r, i]
                c += 1
        M = Bk.T * Lc * Bk
        try:
            mp.cholesky(M + mp.eye(n - 1) * mp.mpf(10) ** (-dps + 10)); okk = True
        except (ZeroDivisionError, ValueError):
            okk = False
        check(okk, f'A5 local form restricted to ker {name} is >= -1e-{dps-10} (Cholesky of the shifted restriction)')
    # ---- B
    u = mp.matrix([1] * n)
    for _ in range(6):
        u = mp.lu_solve(H, u); u = u / mp.norm(u)
    lam = (u.T * H * u)[0]
    check(lam > 0, f'B0 lambda_min(H) ~ {mp.nstr(lam, 5)} (inverse iteration)')
    xi = [u[r] for r in range(n)]
    def Pt(t):
        s = L * t / (2 * mp.pi); tot = mp.mpf(0)
        for r, j in enumerate(idx):
            pr = mp.mpf(1)
            for k in idx:
                if k != j: pr *= (k - s)
            tot += xi[r] * pr
        return tot
    c = mp.taylor(lambda t: mp.log(Pt(t)), 0, 8)
    d = mp.taylor(lambda t: mp.log(Xi(t)), 0, 8)
    check(abs(c[1]) + abs(c[3]) < mp.mpf(10) ** -10, f'B1 log P_N is even at 0 (odd coefficients {mp.nstr(c[1], 2)}, {mp.nstr(c[3], 2)})')
    sig = {}
    for kk in (2, 4, 6, 8):
        w = -kk * c[kk]; z = -kk * d[kk]; sig[kk] = (w, z)
        print(f'     sigma_{kk}: window {mp.nstr(w, 12):>20}   Xi {mp.nstr(z, 12):>20}   rel.err {mp.nstr(abs(w / z - 1), 3)}')
    T = 2 * mp.pi * N / L
    tail = (mp.log(T / (2 * mp.pi)) + 1) / (mp.pi * T)
    check(0 < sig[2][0] < sig[2][1], f'B2 sigma_2(window) = {mp.nstr(sig[2][0], 6)} in (0, sigma_2(Xi) = {mp.nstr(sig[2][1], 6)}); deficit {mp.nstr(sig[2][1] - sig[2][0], 3)} vs Riemann-von Mangoldt tail above the cutoff T = 2 pi N / L = {mp.nstr(T, 5)}: {mp.nstr(tail, 3)}')
    check(abs(sig[4][0] / sig[4][1] - 1) > abs(sig[8][0] / sig[8][1] - 1), 'B3 relative error of sigma_2k decreases with k (tail-dominated)')
    s2 = sig[2][0]; P0 = Pt(0); worst = mp.mpf(0)
    for zc in (mp.mpc(3, 2), mp.mpc(0, 5), mp.mpc(10, 10), mp.mpc(-7, 1)):
        ratio = abs(Pt(zc)) / (abs(P0) * mp.exp(s2 * abs(zc) ** 2 / 2)); worst = max(worst, ratio)
    check(worst <= 1, f'B4 LP growth bound |P(z)| <= P(0) exp(sigma_2|z|^2/2) at four complex points (max ratio {mp.nstr(worst, 4)})')
    return xi, idx, L

def spectrum_table(x=13, N=30, dps=60):
    print(f'\n## C: the window spectrum, x = {x}, N = {N}')
    mp.mp.dps = dps
    n = 2 * N + 1; idx = list(range(-N, N + 1)); L = mp.log(x)
    a, b = ab_true(x, N); H = full(a, b, N)
    u = mp.matrix([1] * n)
    for _ in range(6):
        u = mp.lu_solve(H, u); u = u / mp.norm(u)
    xi = [u[r] for r in range(n)]; eta = mp.fsum(xi); xi = [v / eta for v in xi]
    mp.mp.dps = 50
    Dp = mp.matrix(n, n)
    for r, j in enumerate(idx):
        for c, k in enumerate(idx):
            Dp[r, c] = (j if r == c else 0) - j * xi[r]
    ev = mp.eig(Dp, left=False, right=False)
    check(max(abs(mp.im(e)) for e in ev) < mp.mpf(10) ** -20, f'C1 spectrum of D\' real (max |Im| {mp.nstr(max(abs(mp.im(e)) for e in ev), 3)}); D\' xi = 0 accounts for the extra eigenvalue')
    pos = sorted([2 * mp.pi * mp.re(e) / L for e in ev if mp.re(e) > mp.mpf(10) ** -20])
    check(len(pos) == N, f'C2 {len(pos)} positive frequencies (expected N = {N})')
    print('     comparison only (zeros used here and nowhere else):')
    for i, z in enumerate(pos):
        if i < 8 or i in (9, 14, 19, 24, N - 1):
            g = mp.im(mp.zetazero(i + 1))
            print(f'     {i+1:3d}  window {mp.nstr(z, 15):>20}   gamma {mp.nstr(g, 15):>20}   diff {mp.nstr(z - g, 3)}')
    print(f'     frequency cutoff 2 pi N / L = {mp.nstr(2 * mp.pi * N / L, 5)}; unresolved roots escape upward')

if __name__ == '__main__':
    for x, N, dps in ((13, 20, 60), (13, 40, 60), (13, 56, 60), (25, 60, 180)):
        case(x, N, dps)
    spectrum_table()
    print(f'\n# checks: {_P + _F} run, {_F} failed')
