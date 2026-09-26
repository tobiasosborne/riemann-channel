#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane E (claude:opus, 2026-09-26).  Question (c): what the archimedean-only controls'
inertia can and cannot say about the rate.  (1) The turning frequency t0 where the elliptic symbol
h_C(t) = log(C/4pi^2) + 2 Re psi(1+it) changes sign is x-INDEPENDENT; the H-RATE turning frequency T* where
h_C(T*) = log x (T* ~ 2 pi sqrt(x/C)) is x-dependent.  (2) Mode counts omega_n = 2 pi n / log x below t0, against the
lane's certified control inertia (CONTROL lines).  (3) Inertia vs rate across objects (lane tables).
(4) The lemma C > 4 pi^2 e^{2 gamma}: the symbol minimum and the value of the threshold.  Deterministic."""
import mpmath as mp, re, glob
mp.mp.dps = 30
h = lambda C, t: mp.log(C / (4 * mp.pi**2)) + 2 * mp.re(mp.digamma(1 + 1j * t))
R = '/home/tobiasosborne/Projects/riemann-channel/outputs/'
checks = fails = 0
def check(ok, msg):
    global checks, fails
    checks += 1; fails += (not ok); print(('ok  ' if ok else 'FAIL') + ' ' + msg)
thr = 4 * mp.pi**2 * mp.e**(2 * mp.euler)
print('threshold 4 pi^2 e^{2 gamma} =', mp.nstr(thr, 10), '; min_t h_C(t) = h_C(0) = log(C/4pi^2) - 2 gamma')
for C in (11, 14, 37, 389):
    t0 = mp.findroot(lambda t: h(C, t), 3) if h(C, 0) < 0 else None
    print(f'C={C}: h_C(0) = {mp.nstr(h(C, 0), 8)}; sign-change frequency t0 = {mp.nstr(t0, 8) if t0 else "none (symbol positive)"}')
    for x in (13, 25, 50, 100):
        Ts = mp.findroot(lambda t: h(C, t) - mp.log(x), 2 * mp.pi * mp.sqrt(x / C))
        L = mp.log(x); nE = nO = None
        if t0:
            nE = sum(1 for n in range(0, 400) if 2 * mp.pi * n / L < t0); nO = sum(1 for n in range(1, 400) if 2 * mp.pi * n / L < t0)
        print(f'   x={x}: T*(h=log x) = {mp.nstr(Ts, 8)} vs 2 pi sqrt(x/C) = {mp.nstr(2*mp.pi*mp.sqrt(mp.mpf(x)/C), 8)}; modes below t0: E {nE}, O {nO}')
# certified control inertia from the lane's files
for c in ('11a1', '14a1', '37a1'):
    for fn in sorted(glob.glob(R + f'rtp2_ellcurve_{c}_axisN_x*.txt')):
        for l in open(fn):
            if l.startswith('CONTROL '):
                d = dict(kv.split('=') for kv in l.split()[1:]); print(f'{c}: x={d["x"]} N={d["N"]} negE={d["negE"]} negO={d["negO"]} minE={d["minE"]} minO={d["minO"]}')
check(h(389, 0) > 0 and h(37, 0) < 0 and h(11, 0) < 0, 'symbol positive for C = 389, negative at t = 0 for C = 11, 37')
t = open(R + 'rtp2_ellcurve_389a1_record.txt').read()
m = re.search(r'CONTROL x=13 N=60 minE=(\S+) minO=(\S+) negE=(\d+)', t)
check(float(m[1]) >= float(h(389, 0)) - 1e-9 and float(m[2]) >= float(h(389, 0)) - 1e-9 and m[3] == '0', f'389a1 control minima {m[1]}, {m[2]} >= h_389(0) = {mp.nstr(h(389,0),8)}')
# inertia vs rate (lane tables; x = 13, N = 60 controls; digits per unit x over 13-25)
rows = [('11a1', '1/0', 0.3747556, 2 * mp.sqrt(1 / mp.mpf(11))), ('chi_-4', '1/0', 1.3182, None), ('14a1', '1/0', 0.3112178, None), ('zeta', '3/2', 5.33922, None)]
print('control inertia E/O at x=13 vs digits/x over 13-25:', [(r[0], r[1], r[2]) for r in rows])
print(f'# checks: {checks} run, {fails} failed')
