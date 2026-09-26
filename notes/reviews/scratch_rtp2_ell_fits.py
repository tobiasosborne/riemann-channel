#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane E (claude:opus, 2026-09-26).  Independent refit of log10 eps from the lane's
committed output files (parsing only the EIG / COMP lines; no lane script imported).  Deterministic.
Fits: per curve against x, sqrt x, sqrt(x/C), x^p (free p), log x (power law); three-parameter
a + b ln z - k z; joint common slope in sqrt(x)/C^alpha with separate intercepts (alpha profiled),
with and without the rank-one curve 37a1 (its GLOBAL, odd, minimum) as a third conductor.
COMPARISON STEP: the first-zero errors (COMP lines, PARI zeros) are read only in the block so labelled."""
import re, numpy as np
from scipy.optimize import least_squares, minimize_scalar
R = '/home/tobiasosborne/Projects/riemann-channel/outputs/'
C = {'11a1': 11, '14a1': 14, '37a1': 37}
def eig(fn):
    out = {}
    for l in open(R + fn):
        if l.startswith('EIG '):
            d = dict(kv.split('=') for kv in l.split()[1:])
            x = float(d['x']); par = int(d['parity'])
            e, o = float(d['epsE']), float(d['epsO'])
            out[x] = (e, o, par)
    return out
def comp(fn):
    out = {}
    for l in open(R + fn):
        if l.startswith('COMP ') and 'error=' in l:
            d = dict(kv.split('=') for kv in l.split()[1:] if '=' in kv)
            out[float(d['x'])] = float(d['error'])
    return out
def lin(X, y):
    A = np.vstack([np.ones_like(X), X]).T
    c, *_ = np.linalg.lstsq(A, y, rcond=None); r = y - A @ c
    return c, np.sqrt(np.mean(r**2)), np.max(np.abs(r))
checks = 0; fails = 0
def check(cond, msg):
    global checks, fails
    checks += 1
    if not cond: fails += 1; print('FAIL', msg)
sets = {('11a1', 60): 'rtp2_ellcurve_11a1_axisx_ccm_N60.txt', ('14a1', 60): 'rtp2_ellcurve_14a1_axisx_ccm_N60.txt',
        ('11a1', 120): 'rtp2_ellcurve_11a1_axisx_ccm_N120.txt', ('14a1', 120): 'rtp2_ellcurve_14a1_axisx_ccm_N120.txt',
        ('11a1', 200): 'rtp2_ellcurve_11a1_axisx_ccm_N200.txt',
        ('37a1', 60): 'rtp2_ellcurve_37a1_axisx_ccm_N60.txt', ('37a1', 120): 'rtp2_ellcurve_37a1_axisx_ccm_N120.txt'}
data = {}
for (c, N), fn in sets.items():
    E = eig(fn); xs = sorted(x for x in E if x >= 13)
    # parity audit: use the GLOBAL minimum (the block that carries it)
    glob = np.array([min(E[x][0], E[x][1]) for x in xs])
    pars = [E[x][2] for x in xs]
    for x in xs:
        e, o, p = E[x]
        check((p == 1) == (e < o) and (p == -1) == (o < e), f'parity flag agrees with block minima {c} N={N} x={x}')
    data[(c, N)] = (np.array(xs), np.log10(glob), pars)
    print(f'{c} N={N}: {len(xs)} knots x>=13, parities {sorted(set(pars))}')
print('\n== per-curve fits of log10(global eps) (digits; slope = digits gained per unit variable)')
lane = {('11a1', 60): (0.2805567, 0.2995184, 3.072212, 0.08788969), ('11a1', 120): (0.3711897, 0.1078897, 3.225089, 0.03522068),
        ('11a1', 200): (0.2270742, 0.7290918, 3.148805, 0.1221076), ('14a1', 60): (0.2441695, 0.2913558, 2.676512, 0.07435942),
        ('14a1', 120): (0.3162483, 0.0339899, 2.737282, 0.08013304)}
for key, (x, y, _) in data.items():
    c, N = key
    cx, rx, mx = lin(x, y); cs, rs, ms = lin(np.sqrt(x), y); cl, rl, ml = lin(np.log(x), y)
    cxl, rxl, mxl = lin(x / np.log(x), y)
    def rp(p): return lin(x**p, y)[1]
    pb = minimize_scalar(rp, bounds=(0.05, 1.5), method='bounded')
    print(f'{c} N={N} range {x[0]:.0f}-{x[-1]:.0f}: x slope {-cx[1]:.6f} rms {rx:.4f} max {mx:.4f} | sqrt x slope {-cs[1]:.6f} '
          f'(per sqrt(x/C) {-cs[1]*np.sqrt(C[c]):.5f}) rms {rs:.4f} max {ms:.4f} | x/log x rms {rxl:.4f} | power law rms {rl:.4f} | best x^p p={pb.x:.3f} rms {pb.fun:.4f}')
    if key in lane:
        a, b, s, d = lane[key]
        check(abs(-cx[1] - a) < 5e-6 and abs(rx - b) < 5e-6 and abs(-cs[1] - s) < 5e-5 and abs(rs - d) < 5e-6, f'lane fit row {key} reproduced')
print('\n== three-parameter ln eps = a + b ln z - k z, z = sqrt(x/C); and at fixed k = 8 pi, 4 pi')
for key, (x, y, _) in data.items():
    c, N = key; z = np.sqrt(x / C[c]); ly = y * np.log(10)
    A = np.vstack([np.ones_like(z), np.log(z), -z]).T
    co, *_ = np.linalg.lstsq(A, ly, rcond=None); r = (ly - A @ co) / np.log(10)
    cond = np.linalg.cond(A)
    res = []
    for k in (8 * np.pi, 4 * np.pi):
        A2 = np.vstack([np.ones_like(z), np.log(z)]).T; c2, *_ = np.linalg.lstsq(A2, ly + k * z, rcond=None)
        r2 = (ly + k * z - A2 @ c2) / np.log(10); res.append((c2[1], np.sqrt(np.mean(r2**2))))
    # k/(8pi) profile: range of k with rms within 10% of the optimum
    ks = np.linspace(0.3, 2.5, 441) * 8 * np.pi; rr = []
    for k in ks:
        A2 = np.vstack([np.ones_like(z), np.log(z)]).T; c2, *_ = np.linalg.lstsq(A2, ly + k * z, rcond=None)
        rr.append(np.sqrt(np.mean(((ly + k * z - A2 @ c2) / np.log(10))**2)))
    rr = np.array(rr); ok = ks[rr <= 1.10 * rr.min()] / (8 * np.pi)
    print(f'{c} N={N}: z in [{z[0]:.3f},{z[-1]:.3f}] free b={co[1]:.4f} k/8pi={co[2]/(8*np.pi):.4f} rms {np.sqrt(np.mean(r**2)):.5f} '
          f'(design cond {cond:.0f}); k=8pi: b={res[0][0]:.4f} rms {res[0][1]:.5f}; k=4pi: b={res[1][0]:.3f} rms {res[1][1]:.5f}; '
          f'k/8pi with rms <= 1.1 x min: [{ok.min():.3f}, {ok.max():.3f}]')
print('\n== joint common slope in sqrt(x)/C^alpha, separate intercepts (N = 60, x in [13, 50])')
def joint(curves, alpha, N=60):
    X = []; Y = []; G = []
    for i, c in enumerate(curves):
        x, y, _ = data[(c, N)]; X += list(np.sqrt(x) / C[c]**alpha); Y += list(y); G += [i] * len(x)
    X = np.array(X); Y = np.array(Y); G = np.array(G)
    A = np.zeros((len(X), len(curves) + 1)); A[np.arange(len(X)), G] = 1; A[:, -1] = X
    co, *_ = np.linalg.lstsq(A, Y, rcond=None); r = Y - A @ co
    return -co[-1], np.sqrt(np.mean(r**2)), np.max(np.abs(r)), len(X)
for curves in (['11a1', '14a1'], ['11a1', '14a1', '37a1']):
    for a in (0.0, 0.5, 1.0):
        s, rm, mx, n = joint(curves, a)
        print(f'{"+".join(curves)} alpha={a}: common slope {s:.5f} rms {rm:.5f} max {mx:.5f} points {n}')
    ab = minimize_scalar(lambda a: joint(curves, a)[1], bounds=(-1, 2), method='bounded')
    al = np.linspace(-0.5, 1.5, 2001); rr = np.array([joint(curves, a)[1] for a in al])
    within = al[rr <= 1.10 * rr.min()]
    print(f'   best alpha {ab.x:.4f} rms {ab.fun:.5f}; alpha with rms <= 1.1 x min: [{within.min():.3f}, {within.max():.3f}]')
    if curves == ['11a1', '14a1']:
        s0, r0, _, _ = joint(curves, 0.0); s5, r5, _, _ = joint(curves, 0.5)
        check(abs(r0 - 0.2290725) < 5e-6 and abs(r5 - 0.08568873) < 5e-7 and abs(s5 - 10.11247) < 5e-5, 'lane shared-slope table reproduced')
print('\n== conductor exponent implied by per-curve sqrt(x) slopes: alpha = ln(s11/s14)/ln(14/11)')
for N in (60, 120):
    s11 = -lin(np.sqrt(data[('11a1', N)][0]), data[('11a1', N)][1])[0][1]
    s14 = -lin(np.sqrt(data[('14a1', N)][0]), data[('14a1', N)][1])[0][1]
    print(f'N={N}: s11={s11:.5f} s14={s14:.5f} ratio {s11/s14:.5f} (sqrt(14/11)={np.sqrt(14/11):.5f}) -> alpha={np.log(s11/s14)/np.log(14/11):.4f}; '
          f'ln14/ln11={np.log(14)/np.log(11):.5f}')
    for c in ('37a1',):
        s = -lin(np.sqrt(data[(c, N)][0]), data[(c, N)][1])[0][1]
        print(f'   37a1 global (odd) slope per sqrt x {s:.5f}; per sqrt(x/37) {s*np.sqrt(37):.4f}; alpha(11a1->37a1)={np.log(s11/s)/np.log(37/11):.4f}, alpha(14a1->37a1)={np.log(s14/s)/np.log(37/14):.4f}')
print('\n== sub-range sqrt-slopes (digits per sqrt(x/C)) for 11a1 N=200: stability of the local rate')
x, y, _ = data[('11a1', 200)]
for lo, hi in ((13, 25), (25, 50), (50, 100), (13, 50), (53, 100), (13, 100)):
    m = (x >= lo) & (x <= hi); s = -lin(np.sqrt(x[m] / 11), y[m])[0][1]
    print(f'   {lo}-{hi}: {s:.4f}  ({m.sum()} knots)')
print('\n== COMPARISON STEP (PARI zeros; approximate): first-zero error fits, 11a1 N=200')
E = comp('rtp2_ellcurve_11a1_axisx_ccm_N200.txt'); xs = np.array(sorted(k for k in E if k >= 13)); ye = np.log10([E[k] for k in xs])
cx, rx, _ = lin(xs, ye); cs, rs, _ = lin(np.sqrt(xs / 11), ye)
print(f'error: x slope {-cx[1]:.6f} rms {rx:.6f}; sqrt(x/11) slope {-cs[1]:.5f} rms {rs:.6f}')
check(abs(rx - 0.6435573) < 5e-6 and abs(rs - 0.1471212) < 5e-6, 'lane error-fit row reproduced')

print('\n== (added) local rate drift, 11a1 N=200: sub-range slopes per z with OLS standard errors, and what the')
print('   E1b form ln eps = a + b ln z - 8 pi z (b fitted on all 28 knots) implies on the same sub-ranges')
x, y, _ = data[('11a1', 200)]; z = np.sqrt(x / 11); ly = y * np.log(10)
A2 = np.vstack([np.ones_like(z), np.log(z)]).T; c8, *_ = np.linalg.lstsq(A2, ly + 8 * np.pi * z, rcond=None)
model = (A2 @ c8 - 8 * np.pi * z) / np.log(10); res = y - model
for lo, hi in ((13, 25), (25, 50), (50, 100), (13, 32), (32, 64), (64, 100)):
    m = (x >= lo) & (x <= hi); Z = z[m]; A = np.vstack([np.ones_like(Z), Z]).T
    co, *_ = np.linalg.lstsq(A, y[m], rcond=None); r = y[m] - A @ co; dof = max(m.sum() - 2, 1)
    se = np.sqrt(np.sum(r**2) / dof / np.sum((Z - Z.mean())**2))
    cm, *_ = np.linalg.lstsq(A, model[m], rcond=None)
    print(f'   {lo:>3}-{hi:<3} z {Z[0]:.2f}-{Z[-1]:.2f}: data {-co[1]:.3f} +/- {se:.3f} digits/z; E1b(8pi, b={c8[1]:.2f}) model {-cm[1]:.3f}; mean residual {res[m].mean():+.3f}')
lag1 = np.corrcoef(res[:-1], res[1:])[0, 1]
print(f'   residual lag-1 autocorrelation of the k=8pi fit: {lag1:.3f}; sign runs: {1 + int(np.sum(np.sign(res[1:]) != np.sign(res[:-1])))} over {len(res)} knots')
print('   residuals by knot (x: digits):', ' '.join(f'{int(a)}:{b:+.2f}' for a, b in zip(x, res)))
# prime vs prime-power knots
pp = np.array([all(int(a) % d for d in range(2, int(a**.5) + 1)) for a in x])
print(f'   mean residual at prime knots {res[pp].mean():+.3f} ({pp.sum()}), at proper prime powers / endpoint {res[~pp].mean():+.3f} ({(~pp).sum()})')

print('\n== (added) joint fits with a common algebraic prefactor: ln eps_c = a_c + b ln z - k z, z = sqrt(x)/C^alpha,')
print('   common (b, k), separate intercepts a_c; N = 60, x in [13, 50]; alpha profiled')
def joint_pref(curves, alpha, N=60):
    X = []; Y = []; G = []
    for i, c in enumerate(curves):
        x, y, _ = data[(c, N)]; X += list(np.sqrt(x) / C[c]**alpha); Y += list(y * np.log(10)); G += [i] * len(x)
    X = np.array(X); Y = np.array(Y); G = np.array(G)
    A = np.zeros((len(X), len(curves) + 2)); A[np.arange(len(X)), G] = 1; A[:, -2] = np.log(X); A[:, -1] = -X
    co, *_ = np.linalg.lstsq(A, Y, rcond=None); r = (Y - A @ co) / np.log(10)
    return co[-2], co[-1], np.sqrt(np.mean(r**2))
for curves in (['11a1', '14a1'], ['11a1', '14a1', '37a1']):
    al = np.linspace(-0.5, 1.5, 2001); rr = np.array([joint_pref(curves, a)[2] for a in al]); i = int(np.argmin(rr))
    within = al[rr <= 1.10 * rr.min()]
    b5, k5, r5 = joint_pref(curves, 0.5); b0, k0, r0 = joint_pref(curves, 0.0)
    print(f'{"+".join(curves)}: best alpha {al[i]:.3f} rms {rr[i]:.5f}; alpha window (rms <= 1.1 x min) [{within.min():.3f}, {within.max():.3f}]; '
          f'alpha=0.5: b={b5:.3f} k/8pi={k5/(8*np.pi):.4f} rms {r5:.5f}; alpha=0: rms {r0:.5f}')

print('\n== (added) window of the free power p in log10 eps = a - s x^p (rms <= 1.1 x min)')
for key in (('11a1', 200), ('11a1', 60), ('14a1', 60), ('37a1', 60)):
    x, y, _ = data[key]; ps = np.linspace(0.05, 1.5, 1451); rr = np.array([lin(x**p, y)[1] for p in ps])
    w = ps[rr <= 1.10 * rr.min()]
    print(f'   {key[0]} N={key[1]}: best p {ps[np.argmin(rr)]:.3f}, window [{w.min():.3f}, {w.max():.3f}]; rms at p=1/2 {lin(np.sqrt(x), y)[1]:.4f}, at p=1 {lin(x, y)[1]:.4f}')

print('\n== (added) lane D shape check (read-only): global minimum of real Dirichlet L, best power p in log10 eps = a - s x^p')
for D in ('D-4', 'D-3', 'D5'):
    for N in (60, 120):
        E = eig(f'rtp2_dirichlet_{D}_axisx_ccm_N{N}.txt'); xs = np.array(sorted(k for k in E if k >= 13))
        yy = np.log10([min(E[k][0], E[k][1]) for k in xs]); ps = np.linspace(0.2, 1.5, 131)
        print(f'   {D} N={N} {xs[0]:.0f}-{xs[-1]:.0f}: best p {ps[int(np.argmin([lin(xs**p, yy)[1] for p in ps]))]:.2f}; '
              f'rms x {lin(xs, yy)[1]:.4f}, rms sqrt x {lin(np.sqrt(xs), yy)[1]:.4f}')
print(f'\n# checks: {checks} run, {fails} failed')
