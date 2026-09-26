#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane G (claude:opus, 2026-09-26). A BLIND grid experiment and an independent
infeasibility certificate that uses no prime position and no eigenvector of the true form.

Problem (only pole + archimedean data H0 and a grid of positions; H-SIGN):
    tau*(grid, N) = - max_{w >= 0 on grid} lambda_min( H0 + sum_j w_j T(t_j) ).
tau* > 0  <=>  the grid set is empty (the lane's G4 statement); tau* is the smallest uniform relaxation
H(w) >= -tau I that makes the grid feasible (the lane's proposed next experiment).
Method: Kelley cutting planes (HiGHS LP: max s s.t. u_k^T H(w) u_k >= s over the generated cuts, w >= 0),
cuts = lowest eigenvectors of the current iterate H(w); starting cut e_0 (the constant test). The LP value
is an UPPER bound on max lambda_min (its dual is a PSD Z = sum y_k u_k u_k^T with tr Z = 1,
tr(Z T(t_j)) <= 0), the iterate's lambda_min a LOWER bound. Float64 throughout; the upper-bound certificate
is re-verified in mpmath at 40 digits with the rigorous constant-test repair of scratch_rtp2_grid_farkas.py.
Then: where does the blind maximiser put its mass? (compared with log n only AFTER solving).
"""
import sys, json
import numpy as np
import mpmath as mp
from scipy.optimize import linprog
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from scratch_rtp2_grid_common import ab0, phi, blocks_np, atom_blocks_np, prime_powers
from scratch_rtp2_grid_farkas import co_even, co_odd

COUNT = [0, 0]
def check(c, m):
    COUNT[0] += 1; COUNT[1] += (not c); print(('PASS ' if c else 'FAIL ') + m, flush=True)

def setup(x, N, ts):
    with mp.workdps(30):
        a0, b0 = ab0(x, N)
    E0, O0 = blocks_np([float(v) for v in a0], [float(v) for v in b0], N)
    TE, TO = atom_blocks_np(N, ts)
    return dict(x=x, N=N, ts=np.asarray(ts, float), E0=E0, O0=O0, TE=TE, TO=TO, a0=a0, b0=b0)

def lam_min(P, w):
    E = P['E0'] + np.tensordot(w, P['TE'], 1); O = P['O0'] + np.tensordot(w, P['TO'], 1)
    le, ve = np.linalg.eigh(E); lo, vo = np.linalg.eigh(O)
    return min(le[0], lo[0]), (le, ve, lo, vo)

def kelley(P, iters=400, per=4, tol=1e-11, rel=None, prune=False, warm=()):
    """rel: stop when ub - lb < rel*|ub| (for small tau*); prune: drop cuts inactive in the LP dual.
    A HiGHS failure (status != 0) stops the iteration and returns the last solved LP."""
    J = len(P['ts']); cuts = []
    def add(par, u):
        T = P['TE'] if par == 0 else P['TO']; H = P['E0'] if par == 0 else P['O0']
        cuts.append((par, u, float(u @ H @ u), np.einsum('i,jik,k->j', u, T, u)))
    add(0, np.eye(P['N'] + 1)[0])
    for par, u in warm: add(par, u)
    best = (-np.inf, None); ub = np.inf; last = None
    for it in range(iters):
        A = np.array([np.concatenate([-g, [1.0]]) for _, _, _, g in cuts]); b = np.array([c for _, _, c, _ in cuts])
        cobj = np.zeros(J + 1); cobj[-1] = -1
        r = linprog(cobj, A_ub=A, b_ub=b, bounds=[(0, None)] * J + [(None, None)], method='highs')
        if r.status != 0:
            assert last is not None, r.message
            break
        last = (r, list(cuts))
        w = r.x[:J]; ub = -r.fun
        lm, (le, ve, lo, vo) = lam_min(P, w)
        if lm > best[0]: best = (lm, w.copy())
        gap = ub - best[0]
        if gap < tol * max(1.0, abs(ub)) or (rel is not None and gap < rel * abs(ub)): break
        if prune:
            y = -r.ineqlin.marginals
            cuts = [c for c, yk in zip(cuts, y) if yk > 1e-14] or cuts[:1]
        for k in range(min(per, len(le))): add(0, ve[:, k])
        for k in range(min(per, len(lo))): add(1, vo[:, k])
    r, cuts_used = last
    y = -r.ineqlin.marginals          # duals >= 0 of the cut rows
    return dict(ub=-r.fun, lb=best[0], w=best[1], y=y, cuts=cuts_used, iters=it + 1,
                active=[(c[0], c[1]) for c, yk in zip(cuts_used, y) if yk > 1e-14])

def certify(P, res, dps=40):
    """rebuild Z = sum y_k u_k u_k^T from the float cuts (exact as binary floats), verify in mpmath."""
    x, N, ts = P['x'], P['N'], P['ts']
    with mp.workdps(dps):
        a0, b0 = ab0(x, N)
        coA = [mp.mpf(0)] * (N + 1); coB = [mp.mpf(0)] * (N + 1)
        for yk, (par, u, _, _) in zip(res['y'], res['cuts']):
            if yk <= 0: continue
            c = [mp.mpf(float(v)) for v in u]
            A, B = (co_even if par == 0 else co_odd)(c, N)
            for n in range(N + 1):
                coA[n] += mp.mpf(float(yk)) * A[n]; coB[n] += mp.mpf(float(yk)) * B[n]
        cost = mp.fsum(coA[n] * a0[n] for n in range(N + 1)) + mp.fsum(coB[n] * b0[n] for n in range(1, N + 1))
        rho = mp.mpf(0)
        for t in ts:
            t = mp.mpf(float(t)); f = phi(N, t)
            q = mp.fsum(coA[n] * f[n] for n in range(N + 1)) + mp.fsum(coB[n] * f[N + n] for n in range(1, N + 1))
            rho = max(rho, (q + mp.mpf(10) ** -30) / (2 * (1 - t)))
        rep = cost + rho * a0[0] + mp.mpf(10) ** -30
        return cost, rho, rep

def support_report(P, w, thresh_frac=1e-3):
    L = np.log(P['x']); ys = P['ts'] * L
    pp = [(n, np.log(n)) for n, _ in prime_powers(P['x'])]
    tot = w.sum(); big = [(ys[j], w[j]) for j in range(len(w)) if w[j] > thresh_frac * tot]
    out = []
    for y, wj in big:
        n, ly = min(pp, key=lambda q: abs(q[1] - y))
        out.append((round(y, 4), round(wj, 5), n, round(y - ly, 4)))
    return tot, out

if __name__ == '__main__':
    x = 13; L = np.log(13)
    results = {}
    # 1. uniform grids at N = 20: blind tau*, independent certificate, where the maximiser sits
    for M in (64, 128, 256):
        ts = np.arange(1, M) / M
        P = setup(x, 20, ts); res = kelley(P)
        cost, rho, rep = certify(P, res)
        tot, sup = support_report(P, res['w'])
        print(f'BLIND x=13 N=20 M={M}: max lambda_min in [{res["lb"]:.6e}, {res["ub"]:.6e}] after {res["iters"]} rounds; '
              f'mass {tot:.6f}; support (y, w, nearest prime power, offset): {sup}')
        check(rep < 0, f'x=13 N=20 M={M}: reviewer-generated certificate (no prime positions, no true eigenvectors) '
                       f'certifies emptiness: tr(ZH0)={mp.nstr(cost,8)}, repaired {mp.nstr(rep,8)}; tau* >= {-float(rep):.4e}')
        results[M] = (res['lb'], res['ub'])
    # 2. grid containing the exact positions (union with log n, n=2..12): must be feasible (truth lies on it)
    ts = np.concatenate([np.arange(1, 64) / 64, [np.log(n) / L for n in range(2, 13)]])
    P = setup(x, 20, ts); res = kelley(P, iters=300)
    print(f'UNION x=13 N=20 M=64+11: max lambda_min in [{res["lb"]:.3e}, {res["ub"]:.3e}] after {res["iters"]} rounds')
    check(res['ub'] > -1e-12, 'union grid (contains log n): no negative upper bound, consistent with feasibility of the truth')
    # the truth itself on the union grid: lambda_min(H0 + T(w*)) in float64 is at rounding level (true value 1.6e-39)
    wstar = np.zeros(len(ts))
    for n, p in prime_powers(13):
        wstar[63 + n - 2] = np.log(p) / np.sqrt(n)
    lm, _ = lam_min(P, wstar)
    check(abs(lm) < 1e-12, f'truth on the union grid: float64 lambda_min = {lm:.2e} (rounding level; mpmath value in scratch_rtp2_grid_kernel.py)')
    # 3. onset in N: the smallest N at which each uniform grid becomes empty (blind; float certificate re-verified)
    for M in (64, 128, 256):
        ts = np.arange(1, M) / M; onset = None; row = []
        for N in range(1, 21):
            P = setup(x, N, ts); res = kelley(P, iters=300)
            row.append((N, res['ub']))
            if res['ub'] < -1e-9:
                cost, rho, rep = certify(P, res)
                if rep < 0:
                    onset = N; break
        print(f'ONSET M={M}: ' + ', '.join(f'N={n}: ub={u:.3e}' for n, u in row))
        check(onset is not None, f'x=13 M={M}: first N with a certified empty uniform grid = {onset}')
        results[f'onset{M}'] = onset
    # 4. shifted uniform grid at N=20: offset h/2 (positions (j+1/2)/M)
    for M in (64, 128, 256):
        ts = (np.arange(0, M) + 0.5) / M
        P = setup(x, 20, ts); res = kelley(P)
        cost, rho, rep = certify(P, res)
        tot, sup = support_report(P, res['w'])
        print(f'SHIFTED x=13 N=20 M={M} (offset h/2): max lambda_min in [{res["lb"]:.6e}, {res["ub"]:.6e}]; support: {sup}')
        check(rep < 0, f'shifted grid M={M}: also certified empty, tau* >= {-float(rep):.4e}')
    print(f'# checks: {COUNT[0]} run, {COUNT[1]} failed')
