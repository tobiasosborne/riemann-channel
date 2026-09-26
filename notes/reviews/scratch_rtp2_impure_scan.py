#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane I (claude:opus, 2026-09-26): attempt to break "no Schmidt defect > 0.1".
EXPLORATORY LOCATOR: uses the lane's own float64 kernel (scripts/rtp2_impure_bumps.FastKernel/build) only to
locate candidate widths quickly; every width reported as a finding is re-evaluated by the reviewer's independent
real-space implementation (scratch_rtp2_impure_gram.py).  Strategy: the ground gap of G falls to 1e-5..1e-6;
an avoided crossing inside one reflection-parity sector would mix two near-product vectors and could spike the
defect between grid points.  We scan 4001-point grids, then refine every local gap minimum by bounded minimisation
and record the defect at the minimum and its neighbourhood."""
import sys, os, math, json
import numpy as np
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(root, 'scripts'))
import rtp2_impure_bumps as L
from scipy.optimize import minimize_scalar
ker = L.FastKernel(128)
def ev(S, A, d):
    b = L.build(ker, S, A, d); w, V = np.linalg.eigh(b['G']); v = V[:, 0]
    par = float(v @ v[::-1])
    par1 = float(V[:, 1] @ V[:, 1][::-1])
    return w, v, L.schmidt(v, S, A), par, par1
out = {}
for S, A in (((2, 3), 2), ((2, 3), 3), ((2, 3, 5), 2)):
    start = L.thresholds(S, A)['all']['delta']
    grid = np.geomspace(start, .345, 4001)
    rec = []
    for d in grid:
        w, v, df, par, par1 = ev(S, A, float(d)); rec.append((float(d), float(w[1] - w[0]), df, par, par1, float(w[0])))
    gaps = np.array([r[1] for r in rec]); dfs = np.array([r[2] for r in rec])
    i = int(np.argmax(dfs))
    print(f'{S} A={A}: 4001-grid max defect {dfs[i]:.6f} at delta {rec[i][0]:.8f}; min gap {gaps.min():.3e}')
    # local minima of the gap where the two lowest states share parity (a genuine avoided crossing)
    mins = [j for j in range(1, len(rec) - 1) if gaps[j] < gaps[j - 1] and gaps[j] < gaps[j + 1]]
    best = (dfs[i], rec[i][0])
    for j in mins:
        same = rec[j][3] * rec[j][4] > 0
        res = minimize_scalar(lambda d: ev(S, A, d)[0][1] - ev(S, A, d)[0][0], bounds=(rec[j - 1][0], rec[j + 1][0]), method='bounded', options={'xatol': 1e-13})
        dm = float(res.x); w, v, df, par, par1 = ev(S, A, dm)
        loc = [ev(S, A, dm * (1 + t))[2] for t in (-1e-6, -1e-8, 1e-8, 1e-6)]
        print(f'   gap min at delta {dm:.12f}: gap {w[1]-w[0]:.3e}, lambda {w[0]:.3e}, parities {par:+.0f}/{par1:+.0f} ({"same" if same else "different"}), defect {df:.6f}, nearby {[round(x, 6) for x in loc]}')
        m = max([df] + loc)
        if m > best[0]: best = (m, dm)
    out[str((S, A))] = dict(max_defect=float(best[0]), at=best[1], n_gap_minima=len(mins))
    print('SCAN ' + json.dumps(out[str((S, A))]), flush=True)
