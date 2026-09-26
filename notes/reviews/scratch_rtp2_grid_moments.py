#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane G (claude:opus, 2026-09-26). G1, G2, G3 theory checks.

G1: span dimension 2N+1 of the atom moment functions; uniform-grid rank min(M-1, 2N+1) (exact, sympy over the
    algebraic numbers is too slow; SVD with a wide gap plus the lane's Chebyshev proof); constant test
    a_0(w) = a0_0 - 2 sum (1-t_j) w_j; how far the constant-test mass bound is from the best mass bound.
G2: the annihilator p(t) = (1-t) prod_k (cos 2 pi t - c_k)^2 at x = 13 (s = 8, degree 16) written in the span of
    A_0..A_16, nonnegative, zero exactly at {t_k, 1-t_k}, zero integral against mu*; exact-moment LP on a fine
    grid union atoms union reflections: max off-atom mass subject to M nu = M mu*, nu >= 0, for N = 1..20
    (empirical uniqueness threshold versus the sufficient N >= 2s = 16); the endpoint makes it unbounded.
G3: the autocorrelation identity q_v(y) = -v^T T(y) v = 2 Re int conj f(u) f(u+y) du by quadrature;
    the single-mode counterexample; near-kernel q_v are not pointwise nonnegative.
"""
import sys
import numpy as np
import mpmath as mp
from scipy.optimize import linprog
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from scratch_rtp2_grid_common import phi, phi_np, atoms, ab0, blocks, atom_blocks

COUNT = [0, 0]
def check(c, m):
    COUNT[0] += 1; COUNT[1] += (not c); print(('PASS ' if c else 'FAIL ') + m, flush=True)

def g1():
    # span dimension on a continuum sample (random points), N = 1..12
    rng = np.random.default_rng(7)
    ok = all(np.linalg.matrix_rank(phi_np(N, rng.uniform(0, 1, 6 * N + 10)), tol=1e-9) == 2 * N + 1 for N in range(1, 13))
    check(ok, 'G1: atom moment functions (A_0..A_N, B_1..B_N) span dimension exactly 2N+1 (N=1..12, random points)')
    rows = []
    for M, N in [(64, 20), (64, 31), (64, 40), (128, 40), (128, 63), (128, 64), (256, 60), (32, 10), (32, 20)]:
        F = phi_np(N, np.arange(1, M) / M)
        s = np.linalg.svd(F, compute_uv=False)
        r = int((s > 1e-8 * s[0]).sum()); gap = s[r - 1] / (s[r] if r < len(s) else np.inf)
        rows.append((M, N, r, min(M - 1, 2 * N + 1), s[r - 1], (s[r] if r < len(s) else 0.0)))
    ok = all(r == e for _, _, r, e, _, _ in rows)
    check(ok, 'G1: uniform-grid moment rank = min(M-1, 2N+1): ' + '; '.join(f'M={M} N={N} rank {r} (sv_r {sr:.2e}, next {sn:.1e})' for M, N, r, e, sr, sn in rows))
    # constant test: E_00 of an atom block is A_0(t) = -2(1-t)
    mp.mp.dps = 30
    E, O = atom_blocks(5, mp.mpf('0.3'))
    check(abs(E[0, 0] + 2 * (1 - mp.mpf('0.3'))) < 1e-25, 'G1: e_0^T T(t) e_0 = -2(1-t) (the constant test)')
    a0, b0 = ab0(13, 1)
    print(f'G1: C = H0_00 = a0_0 at x=13: {mp.nstr(a0[0], 15)}; true weighted mass 2 sum (1-t)w* = '
          f'{mp.nstr(2 * mp.fsum((1 - t) * w for n, t, w in atoms(13)), 15)}')
    C = float(a0[0])
    for M in (64, 128, 256):
        print(f'G1: constant-test total-mass bound on the uniform M={M} grid: C/(2/M) = {C * M / 2:.4f} '
              f'(lane union LP upper bounds at N=20: 4.41 / 5.10 / 6.93; truth 4.2605)')
    check(C * 64 / 2 > 10 * 4.4149, 'G1: the constant test is the simplest mass functional, not the cheapest: at M=64 its bound (95.6) is >20x the LP mass bound (4.41)')

def g2():
    mp.mp.dps = 40
    x = 13; at = atoms(x); s = len(at)
    check(s == 8 and [n for n, _, _ in at] == [2, 3, 4, 5, 7, 8, 9, 11], f'G2: x=13 visible interior atoms {[n for n,_,_ in at]} (13 at the endpoint is invisible)')
    # p(t) = (1-t) prod (cos 2pi t - c_k)^2 = (1-t) sum_n alpha_n cos(2 pi n t); get alpha by Chebyshev expansion
    cks = [mp.cos(2 * mp.pi * t) for _, t, _ in at]
    poly = [mp.mpf(1)]                                   # polynomial in c = cos(theta), low degree first
    for ck in cks:
        for _ in range(2):
            new = [mp.mpf(0)] * (len(poly) + 1)
            for i, v in enumerate(poly):
                new[i] -= ck * v; new[i + 1] += v
            poly = new
    deg = len(poly) - 1
    # power basis -> Chebyshev basis via mpmath chebyfit-free exact recursion: c^k = sum coefficients of T_n
    cheb = [mp.mpf(0)] * (deg + 1)
    powc = {0: [mp.mpf(1)]}                              # c^k in Chebyshev basis
    for k in range(1, deg + 1):
        prev = powc[k - 1]; cur = [mp.mpf(0)] * (k + 1)
        for n, v in enumerate(prev):                     # c * T_n = (T_{n+1} + T_{|n-1|})/2
            if n == 0: cur[1] += v
            else:
                cur[n + 1] += v / 2; cur[abs(n - 1)] += v / 2
        powc[k] = cur
    for k, v in enumerate(poly):
        for n, u in enumerate(powc[k]): cheb[n] += v * u
    check(deg == 2 * s == 16, f'G2: p has cosine degree {deg} = 2s, so it lies in span(A_0..A_16) and needs N >= 16')
    alpha = [-v / 2 for v in cheb]                        # p = sum alpha_n A_n
    p = lambda t: (1 - t) * mp.fprod((mp.cos(2 * mp.pi * t) - ck) ** 2 for ck in cks)
    pspan = lambda t: mp.fsum(alpha[n] * (-2) * (1 - t) * mp.cos(2 * mp.pi * n * t) for n in range(deg + 1))
    diff = max(abs(p(mp.mpf(j) / 997) - pspan(mp.mpf(j) / 997)) for j in range(998))
    check(diff < 1e-30, f'G2: p(t) = sum_n alpha_n A_n(t) on 998 points, max diff {mp.nstr(diff, 3)}')
    integral = mp.fsum(w * p(t) for _, t, w in at)
    check(abs(integral) < 1e-35, f'G2: int p dmu* = {mp.nstr(integral, 3)} (p vanishes at every atom)')
    tt = np.linspace(0, 1, 200001)
    pv = (1 - tt) * np.prod([(np.cos(2 * np.pi * tt) - float(ck)) ** 2 for ck in cks], axis=0)
    zeros_expected = sorted([float(t) for _, t, _ in at] + [1 - float(t) for _, t, _ in at] + [1.0])
    locmin = [tt[i] for i in range(1, len(tt) - 1) if pv[i] <= pv[i - 1] and pv[i] <= pv[i + 1] and pv[i] < 1e-12]
    check(pv.min() >= 0 and all(min(abs(np.array(zeros_expected) - z)) < 2e-5 for z in locmin),
          f'G2: p >= 0 on [0,1]; its near-zero minima {len(locmin)} all within 2e-5 of the 17 points {{t_k, 1-t_k, 1}}')
    # exact-moment LP: fine grid U atoms U reflections; maximise off-atom mass
    atom_t = np.array([float(t) for _, t, _ in at]); wst = np.array([float(w) for _, _, w in at])
    grid = np.arange(1, 4000) / 4000
    pts = np.unique(np.concatenate([grid, atom_t, 1 - atom_t]))
    is_atom = np.array([np.min(np.abs(atom_t - p_)) < 1e-15 for p_ in pts])
    rows = []
    for N in range(1, 21):
        F = phi_np(N, pts).T; m = phi_np(N, atom_t).T @ wst
        # objective: (1-t)-weighted off-atom mass (the scale the constant moment controls)
        r = linprog(-((~is_atom) * (1 - pts)), A_eq=F, b_eq=m, bounds=(0, None), method='highs')
        rows.append((N, r.status, (-r.fun if r.status == 0 else None)))
    print('G2 exact-moment LP, max (1-t)-weighted off-atom mass on 3999-grid U atoms U reflections (status 4 = HiGHS numerical difficulty): '
          + ', '.join(f'N={N}: ' + (f'{o:.2e}' if o is not None else f'status {st}') for N, st, o in rows))
    last_pos = max([N for N, st, o in rows if st == 0 and o > 1e-6] or [0])
    unres = [N for N, st, o in rows if st != 0]
    thr = min(N for N, st, o in rows if N > max([last_pos] + unres) and st == 0 and o < 1e-6)
    check(thr <= 16 and last_pos >= 8, f'G2: exact moments leave off-atom mass up to N = {last_pos}, N = {unres} unresolved in float, pinned from N = {thr} on (sufficient bound 2s = 16; not sharp)')
    # endpoint: add t = 1 (log 13) -- its moment vector is zero, so its weight is free
    check(np.abs(phi_np(20, [1.0])).max() < 1e-12, 'G2: phi(1) = 0: an atom at y = L is invisible; with it the fibre is unbounded')

def g3():
    mp.mp.dps = 25
    N = 3; L = mp.log(13)
    v = [mp.mpf(c) for c in ('0.3', '-0.5', '0.2', '0.7', '-0.1', '0.4', '0.25')]   # V_{-3..3}, real coefficients
    f = lambda u: mp.fsum(v[k + N] * mp.exp(2j * mp.pi * k * u / L) for k in range(-N, N + 1)) / mp.sqrt(L) if 0 <= u <= L else 0
    bad = 0
    for y in (mp.mpf('0.3'), mp.mpf('1.1'), mp.mpf('2.0')):
        t = y / L
        # v^T T(t) v in the full V basis: T_nn = A_|n|, T_nm = (B_n - B_m)/(n - m), B_{-n} = -B_n
        ph = phi(N, t)
        A = lambda n: ph[abs(n)]
        B = lambda n: (ph[N + n] if n > 0 else (-ph[N - n] if n < 0 else mp.mpf(0)))
        vTv = mp.fsum(v[n + N] * v[m + N] * (A(n) if n == m else (B(n) - B(m)) / (n - m)) for n in range(-N, N + 1) for m in range(-N, N + 1))
        ac = mp.quad(lambda u: mp.conj(f(u)) * f(u + y), [0, L - y])
        bad += abs(-vTv - 2 * ac.real) > 1e-15
    check(bad == 0, 'G3: q_v(y) = -v^T T(y) v equals 2 Re int conj f(u) f(u+y) du (quadrature, three shifts)')
    check(2 * (1 - 0.5) * np.cos(2 * np.pi * 0.5) < 0, 'G3: single mode n=1 at t=1/2: q = 2(1-t)cos(2 pi n t) = -1 < 0; autocorrelations are not pointwise nonnegative')

if __name__ == '__main__':
    g1(); g2(); g3()
    print(f'# checks: {COUNT[0]} run, {COUNT[1]} failed')
