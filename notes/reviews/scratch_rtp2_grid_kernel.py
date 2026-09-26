#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane G (claude:opus, 2026-09-26). G5 near-kernel profiles, recomputed independently.

x = 13, N = 60: reviewer's H_true (scratch_rtp2_grid_common.py, pole+arch+atoms, no zst) at 140 digits; even and
odd blocks diagonalised by mpmath eigsy; eight smallest eigenpairs; q_v(t) = -v^T T(t) v evaluated through the
reviewer's block-adjoint moment coefficients (scratch_rtp2_grid_farkas.py) on the 255-point L/256 grid and at the
eight prime powers; sign crossings refined by bisection. Compared with the lane's near_kernel.json.
Also: lambda_min of H_true at x=13, N=20 (lane: 1.56610785511e-39) and of the eigenvector cost v^T H0 v, which is
the only thing a near-null vector says about the atoms: int q_v dmu* = v^T H0 v - lambda.
"""
import sys, json
import mpmath as mp
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from scratch_rtp2_grid_common import ab0, ab_true, blocks, phi, atoms, LANE
from scratch_rtp2_grid_farkas import co_even, co_odd

COUNT = [0, 0]
def check(c, m):
    COUNT[0] += 1; COUNT[1] += (not c); print(('PASS ' if c else 'FAIL ') + m, flush=True)

def smallest(x, N, k):
    a, b = ab_true(x, N)
    E, O = blocks(a, b, N)
    out = []
    for par, B in ((0, E), (1, O)):
        ev, Q = mp.eigsy(B)
        for i in range(B.rows):
            out.append((ev[i], par, [Q[r, i] for r in range(B.rows)]))
    out.sort(key=lambda r: r[0])
    return out[:k]

def qfun(par, c, N):
    A, B = (co_even if par == 0 else co_odd)(c, N)
    def q(t):
        f = phi(N, t)
        return -(mp.fsum(A[n] * f[n] for n in range(N + 1)) + mp.fsum(B[n] * f[N + n] for n in range(1, N + 1)))
    return q, A, B

if __name__ == '__main__':
    mp.mp.dps = 80
    lm20 = smallest(13, 20, 1)[0][0]
    check(abs(lm20 / mp.mpf('1.56610785511e-39') - 1) < 1e-9, f'x=13 N=20: lambda_min(H_true) = {mp.nstr(lm20, 12)} (lane 1.56610785511e-39)')
    mp.mp.dps = 140
    N = 60; x = 13; L = mp.log(13); M = 256
    lane = json.loads((LANE / 'near_kernel.json').read_text())
    vecs = smallest(x, N, 8)
    a0, b0 = ab0(x, N)
    pts = [(n, t) for n, t, w in atoms(x)]
    total = 0; hits = 0
    for i, (lam, par, c) in enumerate(vecs):
        q, A, B = qfun(par, c, N)
        vals = [q(mp.mpf(j) / M) for j in range(1, M)]
        roots = []
        for j in range(M - 2):
            if vals[j] * vals[j + 1] < 0:
                lo, hi = mp.mpf(j + 1) / M, mp.mpf(j + 2) / M
                for _ in range(120):
                    mid = (lo + hi) / 2
                    if q(lo) * q(mid) <= 0: hi = mid
                    else: lo = mid
                roots.append((lo + hi) / 2 * L)
        near = sum(1 for r in roots if min(abs(r - t * L) for _, t in pts) <= L / M)
        total += len(roots); hits += near
        cost = mp.fsum(A[n] * a0[n] for n in range(N + 1)) + mp.fsum(B[n] * b0[n] for n in range(1, N + 1))
        integral = mp.fsum(w * q(t) for n, t, w in atoms(x))
        lv = lane[i]
        agree = abs(lam / mp.mpf(lv['eigenvalue']) - 1) < 1e-10 and len(roots) == len(lv['zeros_y']) and \
            all(abs(r - mp.mpf(z)) < 1e-20 for r, z in zip(roots, lv['zeros_y'])) and par == lv['parity']
        check(agree, f'vector {i}: eigenvalue {mp.nstr(lam, 6)}, parity {par}, {len(roots)} crossings (lane {len(lv["zeros_y"])}), '
                     f'{near} within h of a prime power; min q on grid {mp.nstr(min(vals), 3)}; '
                     f'v^T H0 v = {mp.nstr(cost, 6)} = int q dmu* + lambda (check {mp.nstr(cost - integral - lam, 3)})')
        if i == 0:
            print('  q_0 at log 2, log 3, log 11:', [mp.nstr(q(mp.log(n) / L), 18) for n in (2, 3, 11)])
        if i == 1:
            print('  first root of q_1:', mp.nstr(roots[0], 24))
    check(total == 32 and hits == 0, f'G5: {total} detected crossings over the eight vectors, {hits} within h of a prime power')
    print(f'# checks: {COUNT[0]} run, {COUNT[1]} failed')
