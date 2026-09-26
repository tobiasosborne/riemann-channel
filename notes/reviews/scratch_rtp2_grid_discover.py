#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane G (claude:opus, 2026-09-26). Point (d): does positivity discover the positions
HONESTLY? A blind coarse-to-fine experiment.

Input: pole + archimedean data H0 only (reviewer's own, no zst), the window, H-SIGN. No prime position, no true
eigenvector, no true weight enters the computation. Level 0: uniform interior grid t_j = j/M. Solve
    max_{w >= 0} lambda_min(H0 + sum_j w_j T(t_j))        (= -tau*, the lane's proposed relaxation)
by Kelley cutting planes (scratch_rtp2_grid_blind.py). Level-0 clusters = maximal runs of support points
(w_j > 1e-4 * total mass) separated by at most 2.01 h. Level k >= 1: new grid = union over the previous support
points of 17 points at spacing h_k = h_{k-1}/8 centred on them; cuts warm-started from the previous level's
active cuts; mass is grouped by the nearest level-0 cluster centroid (so a cluster that splits during an
unconverged solve is still reported as one group).
COMPARISON (after solving, not input): group masses against Lambda(n)/sqrt n and group centroids against log n.
Float64; Kelley is not run to convergence at the refined levels: the bracket [lb, ub] on max lambda_min is
printed and is the honest measure of how far each level is from its optimum.
"""
import sys
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from scratch_rtp2_grid_blind import setup, kelley
from scratch_rtp2_grid_common import prime_powers

COUNT = [0, 0]
def check(c, m):
    COUNT[0] += 1; COUNT[1] += (not c); print(('PASS ' if c else 'FAIL ') + m, flush=True)

def runs(ts, w, gap):
    idx = np.argsort(ts); ts, w = ts[idx], w[idx]; keep = w > 1e-4 * w.sum()
    out = []; cur = []
    for t, wj, k in zip(ts, w, keep):
        if not k: continue
        if cur and t - cur[-1][0] > gap: out.append(cur); cur = []
        cur.append((t, wj))
    if cur: out.append(cur)
    return [(sum(t * wj for t, wj in c) / sum(wj for _, wj in c), sum(wj for _, wj in c), len(c)) for c in out]

def grouped(ts, w, centres):
    g = np.argmin(np.abs(ts[:, None] - np.array(centres)[None, :]), axis=1)
    out = []
    for k in range(len(centres)):
        m = w[g == k].sum(); out.append(((ts[g == k] * w[g == k]).sum() / m if m > 0 else np.nan, m))
    return out

def compare(x, groups):
    L = np.log(x); truth = [(np.log(n) / L, np.log(p) / np.sqrt(n), n) for n, p in prime_powers(x)]
    res = []
    for c, m in groups:
        tt, wt, n = min(truth, key=lambda r: abs(r[0] - c)); res.append((n, (c - tt) * L, m / wt - 1))
    return res

def run(x, N, M0, levels, iters=(500, 900), level0=None):
    ts = np.arange(1, M0) / M0; h = 1.0 / M0; L = np.log(x); warm = (); out = []
    for lev in range(levels + 1):
        P = setup(x, N, ts)
        kw = dict(per=8, tol=1e-14, rel=1e-3) if (lev > 0 or level0 is None) else level0
        res = kelley(P, iters=iters[min(lev, 1)], warm=warm, **kw)
        w = res['w']
        if lev == 0:
            cl = runs(ts, w, 2.01 * h); centres = [c for c, _, _ in cl]
            groups = [(c, m) for c, m, _ in cl]; npts = [k for _, _, k in cl]
        else:
            groups = grouped(ts, w, centres); npts = None
        cmp_ = compare(x, groups)
        out.append((lev, h * L, res['lb'], res['ub'], cmp_))
        print(f'x={x} N={N} level {lev}: h={h*L:.3e}, grid {len(ts)} pts, max lambda_min in [{res["lb"]:.4e}, {res["ub"]:.4e}] '
              f'({res["iters"]} rounds), {len(groups)} groups, total mass {w.sum():.10f}', flush=True)
        print('   COMPARISON (n, centroid - log n, mass/(Lambda(n)/sqrt n) - 1' + (', #pts' if npts else '') + '): ' +
              '; '.join(f'({n}, {d:+.2e}, {r:+.2e}' + (f', {npts[i]})' if npts else ')') for i, (n, d, r) in enumerate(cmp_)), flush=True)
        if lev == levels: break
        sup = ts[w > 1e-4 * w.sum()]; h = h / 8; warm = res['active']
        ts = np.unique(np.concatenate([s + h * np.arange(-8, 9) for s in sup])); ts = ts[(ts > 0) & (ts < 1)]
    return out

if __name__ == '__main__':
    if '--x25' not in sys.argv:
        rep = run(13, 20, 256, 2)
        lev0 = rep[0]
        check(sorted(n for n, _, _ in lev0[4]) == [2, 3, 4, 5, 7, 8, 9, 11] and all(abs(d) < lev0[1] for _, d, _ in lev0[4]),
              'x=13 N=20 blind level 0 (uniform L/256 grid): exactly eight clusters, one per visible prime power, every centroid within h of log n, no mass elsewhere')
        for lev, h, lb, ub, c in rep[1:]:
            print(f'   level {lev}: max |centroid - log n| = {max(abs(d) for _, d, _ in c):.2e}, max relative mass error = {max(abs(r) for _, _, r in c):.2e}, '
                  f'bracket gap {ub - lb:.2e}')
        last = rep[-1][4]
        check(all(abs(d) < 1e-6 for n, d, _ in last if n <= 7) and max(abs(d) for _, d, _ in last) < 1e-3,
              'x=13 blind refinement, level 2: log 2..log 7 within 1e-6, every visible prime power within 1e-3 (log 11, next to the edge, worst)')
    # x = 25, level 0 only, with the settings that converge here (absolute tolerance, 6 cuts per block per round)
    rep25 = run(25, 60, 128, 0, level0=dict(per=6, tol=1e-9))
    ns = sorted(n for n, _, _ in rep25[0][4])
    check(16 not in ns and all(abs(d) < rep25[0][1] for _, d, _ in rep25[0][4]),
          f'x=25 N=60 blind level 0 (L/128 grid): {len(ns)} clusters at {ns}, every centroid within h of a prime power; log 16 and log 17 (2.4 h apart) not separated')
    print(f'# checks: {COUNT[0]} run, {COUNT[1]} failed')
