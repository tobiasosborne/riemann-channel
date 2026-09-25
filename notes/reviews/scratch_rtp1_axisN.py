#!/usr/bin/env python3
"""REFUTE lane R, RTP-1 (claude:opus, 2026-09-24).  Claim C2 (and the C1 centre question) recomputed
independently: reviewer's (a_n, b_n) (scratch_rtp1_ab.py) + reviewer's ball LDL^T (scratch_rtp1_linalg.py).
Per x in {13, 25, 50}: log det of the window on |n| <= N (even+odd), and of the even block alone, for all N;
argmin; Delta I_N; the structured admissible interval of b_{N+1} at selected N from three exact evaluations
of the (exactly quadratic) Schur complements; joint MaxEnt point vs interval centre; eps_N at saturated N
by inverse iteration + certified inertia bracket; COMPARISON STEP (zeros used here only): |z_1 - gamma_1|.
Usage: python3 scratch_rtp1_axisN.py X   (X = 13, 25 or 50).  Deterministic."""
import sys, math
from flint import arb, acb, ctx
import mpmath as mp
sys.path.insert(0, __import__('os').path.dirname(__file__))
import scratch_rtp1_ab as AB, scratch_rtp1_linalg as LA

NCHK = [0, 0]
def check(c, m):
    NCHK[0] += 1; NCHK[1] += (not c); print(('PASS ' if c else 'FAIL ') + m, flush=True)

X = int(sys.argv[1])
cfg = {13: (1000, 200, [10, 20, 40, 55, 60, 80, 120], 120, [10, 30, 56, 60, 100]),
       25: (1800, 260, [50, 134, 150, 260], 260, [20, 100, 134, 150, 200]),
       50: (4200, 420, [200, 352, 360], 360, [50, 300, 352, 380])}[X]
prec, Nmax, _, Nsat_eps, Nint = cfg
ctx.prec = prec
L = arb(X).log()
a, b = AB.ab_total(L, Nmax + 1, AB.von_mangoldt_table(X), prec)
E, O = LA.ldl_pivots(prec, a, b)
check(all(e[1] == 1 for e in E) and all(o[1] == 1 for o in O), f'x={X}: every LDL pivot of even (size {Nmax+2}) and odd block certified positive; worst accuracy {min(min(e[2] for e in E), min(o[2] for o in O))} bits')
# log det on |n| <= N: even pivots 0..N, odd pivots 1..N
cumE = [0.0]; s = 0.0
ld_even = []; ld_full = []
sE = 0.0; sO = 0.0
for N in range(0, Nmax + 2):
    sE += E[N][0]
    if N >= 1: sO += O[N - 1][0]
    ld_even.append(sE); ld_full.append(sE + sO)
Nf = min(range(1, Nmax + 1), key=lambda N: ld_full[N])
Ne = min(range(1, Nmax + 1), key=lambda N: ld_even[N])
print(f'x={X}: argmin_N log det(|n|<=N) = {Nf} (value {ld_full[Nf]:.2f}); argmin of the EVEN block alone = {Ne} (value {ld_even[Ne]:.2f})')
print(f'   N/x = {Nf/X:.3f}, N/(x log x) = {Nf/(X*math.log(X)):.3f}; even-block argmin/(x log x) = {Ne/(X*math.log(X)):.3f}')
lane = {13: 56, 25: 134, 50: 352}[X]
check(Nf == lane, f'x={X}: argmin of the full-window log det equals lane A1 value {lane}')
# Delta I_N = log(d_e/s_e) + log(d_o/s_o), j = N+1
def dI(N):
    j = N + 1
    de = float((a[j] + b[j] / j).mid()); do = float((a[j] - b[j] / j).mid())
    return math.log(de) - E[j][0] + math.log(do) - O[j - 1][0]
peak = max(range(1, Nmax), key=dI)
print(f'x={X}: max_N Delta I_N = {dI(peak):.2f} at N = {peak}; Delta I at N = 1,10,50,100: ' + ', '.join(f'{dI(N):.3f}' for N in (1, 10, 50, 100) if N < Nmax))
lastrows = [dI(N) for N in range(Nmax - 100, Nmax)]
print(f'   mean Delta I over the last 100 rows = {sum(lastrows)/100:.3f}')
# structured interval of b_{N+1} (joint, and centre vs joint MaxEnt), exact quadratic from 3 evaluations
def schur_last(N, bnew):
    bb = list(b[:N + 2]); bb[N + 1] = bnew
    e2, o2 = LA.ldl_pivots(prec, a[:N + 2], bb)
    return (e2[N + 1][1] * math.exp(0) , e2[N + 1][0], e2[N+1][1]), (o2[N][0], o2[N][1])
def schur_vals(N, beta):
    bb = list(b[:N + 2]); bb[N + 1] = b[N + 1] + arb(beta)
    out = LA.run(prec, a[:N + 2], bb, 'ldl')
    # need signed pivot values with precision: re-derive from log and sign
    ev = od = None
    for line in out.splitlines():
        t = line.split()
        if t[0] == 'E' and int(t[1]) == N + 1: ev = mp.mpf(t[3]) * mp.e ** mp.mpf(t[2])
        if t[0] == 'O' and int(t[1]) == N + 1: od = mp.mpf(t[3]) * mp.e ** mp.mpf(t[2])
    return ev, od
mp.mp.dps = 30
for N in Nint:
    if N + 1 > Nmax: continue
    h = mp.mpf('1e-3')
    v = [schur_vals(N, bt) for bt in (-h, 0, h)]
    res = {}
    for k, name in ((0, 'e'), (1, 'o')):
        sm, s0, sp = v[0][k], v[1][k], v[2][k]
        C = -(sp + sm - 2 * s0) / (2 * h * h); l = (sp - sm) / (2 * h)
        bstar = l / (2 * C); sstar = s0 + l * l / (4 * C); r = mp.sqrt(sstar / C)
        res[name] = (bstar, r, s0, C, l)
    lo = max(res['e'][0] - res['e'][1], res['o'][0] - res['o'][1]); hi = min(res['e'][0] + res['e'][1], res['o'][0] + res['o'][1])
    mid = (lo + hi) / 2; rj = (hi - lo) / 2
    tau = (0 - mid) / rj
    f = lambda bt: mp.log(res['e'][2] + res['e'][4] * bt - res['e'][3] * bt ** 2) + mp.log(res['o'][2] + res['o'][4] * bt - res['o'][3] * bt ** 2)
    # joint maximiser of log s_e + log s_o on (lo,hi): golden section
    x0, x1 = lo + (hi - lo) * mp.mpf('1e-12'), hi - (hi - lo) * mp.mpf('1e-12')
    for _ in range(200):
        m1 = x0 + (x1 - x0) * mp.mpf(0.381966); m2 = x1 - (x1 - x0) * mp.mpf(0.381966)
        if f(m1) < f(m2): x0 = m1
        else: x1 = m2
    bme = (x0 + x1) / 2
    print(f'x={X} N={N}: r_e={mp.nstr(res["e"][1],4)} r_o={mp.nstr(res["o"][1],4)} r_joint={mp.nstr(rj,4)} tau_joint={mp.nstr(tau,4)}'
          f' | joint MaxEnt offset from joint-interval centre = {mp.nstr((bme-mid)/rj,4)} half-widths; dIs = {mp.nstr(f(bme)-f(0),4)}')
# certified eps at saturated N (and the other selected N)
for N in cfg[2]:
    if N > Nmax: continue
    lam, resid, v = LA.eig_even(prec, a[:N + 1], b[:N + 1], '0', 5, int(prec * 0.3) - 20)
    mid = mp.mpf(lam.strip('[').split()[0])
    br = LA.inertia(prec, a[:N + 1], b[:N + 1], [mp.nstr(mid * (1 - mp.mpf('1e-6')), 30), mp.nstr(mid * (1 + mp.mpf('1e-6')), 30)])
    ok = br[0]['negE'] == 0 and br[0]['undE'] == 0 and br[1]['negE'] == 1 and br[1]['undE'] == 0 and br[1]['negO'] == 0 and br[1]['undO'] == 0
    check(ok, f'x={X} N={N}: eps_N = {mp.nstr(mid, 6)} certified to rel 1e-6 by inertia (even: 0 neg below, 1 neg above; odd: 0 neg above) -> even-simple and minimal')
    if N == Nsat_eps:
        # COMPARISON STEP (zeros of zeta used here only): first zero of the secular function
        mp.mp.dps = int(prec * 0.3) - 40
        xi = [mp.mpf(v[0])] + [mp.mpf(t) / mp.sqrt(2) for t in v[1:]]
        Lm = mp.log(X)
        g = lambda s_: -xi[0] / s_ + 2 * s_ * mp.fsum(xi[j] / (j * j - s_ * s_) for j in range(1, len(xi)))
        ctx.prec = prec
        gam1 = mp.mpf(acb.zeta_zero(1).imag.mid().str(int(prec * 0.3) - 30, radius=False))
        s0 = gam1 * Lm / (2 * mp.pi)
        sr = mp.findroot(g, s0, tol=mp.mpf(10) ** (-(mp.mp.dps - 20)))
        z1 = 2 * mp.pi * sr / Lm
        err = abs(z1 - gam1)
        print(f'# COMPARISON STEP x={X} N={N}: |z_1 - gamma_1| = {mp.nstr(err, 6)} ; ratio to eps_N = {mp.nstr(err / mid, 5)}')
        mp.mp.dps = 30
print(f'# checks: {NCHK[0]} run, {NCHK[1]} failed')
# ---- appended: convergence of eps_N in N beyond the quoted "saturated" N (does the 5.34-5.36 slope carry an N bias?) ----
if len(sys.argv) > 2 and sys.argv[2] == 'tail':
    for N in {13: [200], 25: [260], 50: [400, 420]}[X]:
        lam, resid, v = LA.eig_even(prec, a[:N + 1], b[:N + 1], '0', 5, 50)
        mid = mp.mpf(lam.strip('[').split()[0])
        print(f'x={X} N={N}: eps_N = {mp.nstr(mid, 6)} (uncertified tail value, inverse iteration residual {resid})')
