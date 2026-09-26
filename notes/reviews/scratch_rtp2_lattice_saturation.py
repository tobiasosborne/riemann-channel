#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane L (claude:opus, 2026-09-26): the saturation cutoffs N_sat of L4 recomputed.
The Loewner blocks at cutoff N are leading principal submatrices of the N = 200 blocks (entries depend only on (i, j)),
so one mpmath Cholesky of each N = 200 block gives log det at every N <= 200 as prefix sums of 2 log L_ii.
Argmin over N in 0..200 of the full-window log det (even + odd block)."""
import sys, os
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scratch_rtp2_lattice_common as C
NCHK = [0, 0]
def check(c, msg):
    NCHK[0] += 1; NCHK[1] += (not c); print(('PASS ' if c else 'FAIL ') + msg, flush=True)
LANE = {13: (56, '-1291.66479754'), 17: (83, '-2327.52380683'), 19: (94, '-2962.4013567'), 23: (123, '-4460.94482505'), 25: (134, '-5328.60049077')}
xs = [int(v) for v in sys.argv[1:]] or [13, 17, 25]
mp.mp.dps = 210
for x in xs:
    a, b, rad = C.zst_ab(x, 200, x)
    E, O = C.blocks([mp.mpf(s) for s in a], [mp.mpf(s) for s in b], 200)
    LE = mp.cholesky(E); LO = mp.cholesky(O)
    pe = [2 * mp.log(LE[i, i]) for i in range(201)]; po = [2 * mp.log(LO[i, i]) for i in range(200)]
    ld = []; se = mp.mpf(0); so = mp.mpf(0)
    for N in range(201):
        se += pe[N]
        if N >= 1: so += po[N - 1]
        ld.append(se + so)
    Nst = min(range(201), key=lambda N: ld[N])
    ln, lv = LANE[x]
    check(Nst == ln and abs(ld[Nst] - mp.mpf(lv)) < 1e-6, f'x={x}: argmin_N log det = {Nst} (lane {ln}), log det {mp.nstr(ld[Nst], 12)} (lane {lv}); neighbours {mp.nstr(ld[Nst-1]-ld[Nst], 3)}, {mp.nstr(ld[Nst+1]-ld[Nst], 3)}')
print(f'# checks: {NCHK[0]} run, {NCHK[1]} failed')
