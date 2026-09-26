#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane L (claude:opus, 2026-09-26): prop:rtp-lattice-maxdet made concrete at x = 13, N = 20.
The lattice max-det optimizer w_MD = argmax log det(H0 + T(w)) (unique by L1 + strict concavity) found by damped Newton
in mpmath at 160 digits, started at the truth w*; reported as a displacement from w* relative to the full SDP box
(scratch_rtp2_lattice_box.py: n=2 box [-1.230985e-25, +1.746976e-28], n=12 box [-3.3696767e-5, +1.5329272e-5]).
No zeros used."""
import sys, os
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scratch_rtp2_lattice_common as C
mp.mp.dps = 160
X, N = 13, 20
H0, T, W, HT, NS, _ = C.setup(X, N)
m = len(NS)
Hs = C.combine(H0, T, W)
d = [mp.mpf(0)] * m
def logdet(Hb):
    s = mp.mpf(0)
    for M in Hb:
        try: L = mp.cholesky(M)
        except Exception: return None
        for i in range(M.rows):
            if not L[i, i] > 0: return None
            s += 2 * mp.log(L[i, i])
    return s
for it in range(200):
    Hb = C.combine(Hs, T, d)
    P = [[mp.inverse(Hb[p]) * T[k][p] for k in range(m)] for p in (0, 1)]
    g = mp.matrix([sum(sum(P[p][k][i, i] for i in range(Hb[p].rows)) for p in (0, 1)) for k in range(m)])
    Hm = mp.matrix(m, m)
    for a in range(m):
        for b in range(a, m):
            Hm[a, b] = Hm[b, a] = -sum(mp.fsum(P[p][a][i, j] * P[p][b][j, i] for i in range(Hb[p].rows) for j in range(Hb[p].rows)) for p in (0, 1))
    st = mp.lu_solve(-Hm, g); dec = mp.fsum(g[k] * st[k] for k in range(m))
    f0 = logdet(Hb); t = mp.mpf(1)
    while True:
        dn = [d[k] + t * st[k] for k in range(m)]; f1 = logdet(C.combine(Hs, T, dn))
        if f1 is not None and f1 >= f0 + t * dec / 4: break
        t /= 2
    d = dn
    if dec < mp.mpf(10) ** -120: break
Hb = C.combine(Hs, T, d)
print(f'Newton iterations {it + 1}; log det at truth {mp.nstr(logdet(Hs), 15)}, at the max-det optimizer {mp.nstr(logdet(Hb), 15)}; gain {mp.nstr(logdet(Hb) - logdet(Hs), 6)}')
print(f'lambda_min at optimizer: {mp.nstr(min(mp.eigsy(Hb[p], eigvals_only=True)[0] for p in (0, 1)), 6)} (truth: {mp.nstr(min(mp.eigsy(Hs[p], eigvals_only=True)[0] for p in (0, 1)), 6)})')
BOX = {2: ('-1.230985e-25', '1.7469763e-28'), 6: ('-5.4882492e-18', '2.4529541e-19'), 12: ('-3.3696767e-5', '1.5329272e-5')}
for k, n in enumerate(NS):
    s = f'   n={n:2d}: w_MD - w* = {mp.nstr(d[k], 6)}'
    if n in BOX:
        lo, hi = mp.mpf(BOX[n][0]), mp.mpf(BOX[n][1]); s += f'   (SDP box [{BOX[n][0]}, {BOX[n][1]}]; position in box {mp.nstr((d[k] - lo) / (hi - lo), 4)})'
    print(s)
