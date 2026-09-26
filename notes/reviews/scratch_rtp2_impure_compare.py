#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane I (claude:opus, 2026-09-26): I6 COMPARISON STEP (zeros used only here).
Prime side: raw (unnormalised) Weil entries at delta = 0.1, ratios 6 and 8, from the reviewer's real-space
implementation (scratch_rtp2_impure_gram.entry: 2D archimedean integral, all prime powers).  Zero side:
Z_M = 2 sum_{j<=M} cos(gamma_j log r) phihat(gamma_j)^2, phihat by mpmath quadrature split into 64 panels;
ordinates from data/zeros3000.npy, spot-checked against mpmath.zetazero."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np, mpmath as mp
from multiprocessing import Pool
import scratch_rtp2_impure_gram as g
mp.mp.dps = 30
NC = [0, 0]
def check(c, m):
    NC[0] += 1; NC[1] += (not c); print(('PASS ' if c else 'FAIL ') + m, flush=True)
d = mp.mpf('0.1')
def phihat(gam):
    gam = mp.mpf(gam); pts = [-d + 2 * d * k / 64 for k in range(65)]
    return 2 * mp.quad(lambda x: g.phi(x, d) * mp.cos(gam * x), pts[32:])
if __name__ == '__main__':
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    zs = np.load(os.path.join(root, 'data/zeros3000.npy'))[:2000]
    spot = {1: zs[0], 100: zs[99], 2000: zs[1999]}
    dev = max(abs(mp.im(mp.zetazero(k)) - mp.mpf(float(v))) for k, v in spot.items())
    check(dev < 1e-9, f'cached ordinates agree with mpmath.zetazero at n = 1, 100, 2000 to {mp.nstr(dev,3)}')
    with Pool(64) as pool:
        ph = pool.map(phihat, [float(z) for z in zs], chunksize=8)
        ent = dict(pool.map(g.entry, [(6, 1, '0.1', (2, 3), 3), (8, 1, '0.1', (2, 3), 3)]))
    rep = {6: ('0.00471668172766817', [2.6584e-7, 3.1473e-6, 5.6532e-8, 2.4842e-11]), 8: ('0.00109526807815369', [6.4975e-6, 2.7906e-6, 3.0848e-8, 1.2282e-10])}
    for r in (6, 8):
        po, ar, prime = ent[(r, 1, '0.1')]
        val = po - ar - mp.fsum(v for _, _, v in prime.values())
        ks = sorted(prime)
        terms = [2 * mp.cos(mp.mpf(float(z)) * mp.log(r)) * p ** 2 for z, p in zip(zs, ph)]
        cum = []; s = mp.mpf(0)
        for t in terms: s += t; cum.append(s)
        Ms = [10, 30, 100, 300, 1000, 2000]
        errs = [abs(val - cum[M - 1]) for M in Ms]
        print(f'  r={r}: prime side {mp.nstr(val, 20)} (active prime powers {ks}); errors vs M={Ms}: {[mp.nstr(e, 5) for e in errs]}')
        check(abs(val - mp.mpf(rep[r][0])) < 1e-15 and errs[-1] < 1e-13 and all(abs(e - x) < 1e-3 * x for e, x in zip(errs[:4], rep[r][1])),
              f'r={r}: prime side matches report {rep[r][0]}; 2000-zero sum agrees to {mp.nstr(errs[-1],3)}; M=10..300 errors match the report table')
    print(f'# checks: {NC[0]} run, {NC[1]} failed')
