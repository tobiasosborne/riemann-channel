#!/usr/bin/env python3
"""RTP-2 follow-up: the conductor exponent alpha in log10 eps ~ a_C - k sqrt(x)/C^alpha (claude:opus, 2026-09-26).

Reads only the EIG lines of outputs/rtp2_ellconductors_*.txt (certified minima of the even and odd blocks of
the elliptic Weil form, lane-E driver, --compare 0: no zero of any L-function is read or used anywhere).
The global minimum at each knot is min(epsE, epsO); its parity flag is audited against the two minima.
Deterministic (the bootstrap uses a fixed seed).

Data sets
  S16   the 16 listed curves 11a1 ... 36a1, N = 60, knots 13 <= x <= 50 (16 knots each)
  S19   S16 + 50a1, 67a1, 109a1 (the same window; z = sqrt(x/C) < 1 at many knots for the extras)
  MZ    matched phase-space window: knots with z = sqrt(x/C) in [sqrt(13/11), sqrt(50/11)] from the matchz runs
        (x up to round(50 C/11), capped at 250; 11a1 from its N = 60 run)
Models (per data set; digits = log10)
  M1  log10 eps = a_c - k sqrt(x)/C^alpha                 (per-curve intercepts; common k, alpha)
  M2  log10 eps = a   - k sqrt(x)/C^alpha                 (common intercept)
  M3  log10 eps = a_c + b log10 x - k sqrt(x)/C^alpha     (per-curve intercepts; common b, k, alpha)
  M4  log10 eps = a   + b log10 x - k sqrt(x)/C^alpha     (common intercept and b)
alpha: grid profile (step 0.001); intervals: (i) Gaussian profile likelihood, n log(RSS/RSS_min) <= 3.84 (assumes
iid residuals; the residuals are correlated along x, so this is too narrow and is printed as a lower bound on the
uncertainty); (ii) curve bootstrap (curves resampled with replacement, 2000 draws, percentile 95 %), which treats
curve-to-curve arithmetic differences as the noise; (iii) leave-one-curve-out range; (iv) the review's descriptive
window RMS <= 1.1 x min; (v) between-curve regression log s_c = log k - alpha log C of the per-curve sqrt(x)
slopes s_c, OLS standard error and t interval.
"""
import re, sys
from pathlib import Path
import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'outputs'
LISTED = ['11a1', '14a1', '15a1', '17a1', '19a1', '20a1', '21a1', '24a1', '26a1', '27a1', '30a1', '32a1',
          '33a1', '34a1', '35a1', '36a1']
EXTRA = ['50a1', '67a1', '109a1']
cond = lambda c: int(re.match(r'\d+', c).group())
KV = re.compile(r'(\w+)=(\[[^\]]*\]|\S+)')
checks = fails = 0
def check(ok, msg):
    global checks, fails
    checks += 1
    if not ok: fails += 1; print('FAIL', msg)

def num(s):
    """certified 12-digit value, or the midpoint of a printed ball (flagged)"""
    if s.startswith('['):
        return float(s.strip('[]').split('+/-')[0]), False
    return float(s), True

def eig(fn):
    out = {}; text = fn.read_text()
    check(re.search(r'# checks: \d+ run, 0 failed', text) is not None, f'{fn.name}: driver checks all passed')
    check('COMPARISON STEP skipped' in text and 'REFERENCE ' not in text and 'COMP ' not in text,
          f'{fn.name}: comparison step skipped, no reference zero read')
    for l in text.splitlines():
        if l.startswith('EIG '):
            d = dict(KV.findall(l)); x = float(d['x'])
            (e, ce), (o, co) = num(d['epsE']), num(d['epsO']); p = int(d['parity'])
            check((p == 1) == (e < o) and (p == -1) == (o < e), f'{fn.name} x={x}: parity flag agrees with block minima')
            out[x] = dict(e=e, o=o, par=p, cert=(ce and co), negE=int(d['negE']), negO=int(d['negO']))
    return out

def load(curves, suffix, sel):
    data = {}
    for c in curves:
        fn = OUT / f'rtp2_ellconductors_{c}_axisx_ccm_{suffix(c)}.txt'
        if not fn.exists(): print(f'# missing {fn.name}'); continue
        E = eig(fn); C = cond(c)
        xs = np.array(sorted(x for x in E if sel(x, C)))
        data[c] = dict(C=C, x=xs, y=np.log10([min(E[x]['e'], E[x]['o']) for x in xs]),
                       par=np.array([E[x]['par'] for x in xs]), cert=all(E[x]['cert'] for x in xs),
                       all=E)
    return data

# ---------------------------------------------------------------- fitting machinery
# At fixed alpha the regressor sqrt(x)/C^alpha is each curve's sqrt(x) times C^-alpha, so every sum entering the
# normal equations is a curve statistic times a power of C^-alpha. The RSS profile over the alpha grid and over
# bootstrap multiplicities m_c (a curve drawn m_c times contributes m_c times its statistics; with per-curve
# intercepts each copy keeps its own intercept) is then closed-form. Checked against a direct lstsq fit below.
GRID = np.round(np.arange(-0.5, 1.5001, 0.001), 3)

def cstats(data, curves):
    T = {k: [] for k in ('n', 'C', 'u', 'y', 'l', 'uu', 'yy', 'll', 'uy', 'ul', 'ly', 'cuu', 'cyy', 'cll', 'cuy', 'cul', 'cly')}
    for c in curves:
        d = data[c]; u = np.sqrt(d['x']); y = d['y']; l = np.log10(d['x'])
        T['n'].append(len(u)); T['C'].append(d['C'])
        for k, v in (('u', u), ('y', y), ('l', l)): T[k].append(v.sum())
        for k, a, b in (('uu', u, u), ('yy', y, y), ('ll', l, l), ('uy', u, y), ('ul', u, l), ('ly', l, y)):
            T[k].append((a * b).sum()); T['c' + k].append(((a - a.mean()) * (b - b.mean())).sum())
    return {k: np.array(v, float) for k, v in T.items()}

def solve_profile(T, alphas, m=None, common_a=False, with_b=False):
    """RSS, k, b over alphas (vector) for multiplicities m (vector over curves, or matrix draws x curves)"""
    m = np.ones_like(T['n']) if m is None else m
    m = np.atleast_2d(m)                                    # draws x curves
    w = T['C'][None, :] ** (-np.asarray(alphas)[:, None])   # alphas x curves: C^-alpha
    S = lambda key, pw: (m[:, None, :] * (w[None, :, :] ** pw) * T[key][None, None, :]).sum(-1)   # draws x alphas
    if not common_a:
        Syy = S('cyy', 0); Suu = S('cuu', 2); Suy = S('cuy', 1)
        if not with_b:
            k = -Suy / Suu; rss = Syy - Suy**2 / Suu; b = None
        else:
            Sll = S('cll', 0); Sul = S('cul', 1); Sly = S('cly', 0)
            # regressors (l, -u): [[Sll, -Sul], [-Sul, Suu]] (b, k) = (Sly, -Suy)
            det = Sll * Suu - Sul**2
            b = (Suu * Sly - Sul * Suy) / det; k = (-Sll * Suy + Sul * Sly) / det
            rss = Syy - (b * Sly - k * Suy)
    else:
        n = S('n', 0); Sy = S('y', 0); Su = S('u', 1); Syy = S('yy', 0) - Sy**2 / n
        Suu = S('uu', 2) - Su**2 / n; Suy = S('uy', 1) - Su * Sy / n
        if not with_b:
            k = -Suy / Suu; rss = Syy - Suy**2 / Suu; b = None
        else:
            Sl = S('l', 0); Sll = S('ll', 0) - Sl**2 / n; Sul = S('ul', 1) - Su * Sl / n; Sly = S('ly', 0) - Sl * Sy / n
            det = Sll * Suu - Sul**2
            b = (Suu * Sly - Sul * Suy) / det; k = (-Sll * Suy + Sul * Sly) / det
            rss = Syy - (b * Sly - k * Suy)
    return rss, k, b

def fit(data, curves, alpha, common_a=False, with_b=False):
    """direct lstsq fit at one alpha (for residuals, and as a check of the closed form)"""
    X, Y, G, Lx = [], [], [], []
    for i, c in enumerate(curves):
        d = data[c]; X += list(np.sqrt(d['x']) / d['C']**alpha); Y += list(d['y']); G += [i] * len(d['x']); Lx += list(np.log10(d['x']))
    X, Y, G, Lx = map(np.array, (X, Y, G, Lx))
    cols = [np.ones_like(X)] if common_a else [(G == i).astype(float) for i in range(len(curves))]
    if with_b: cols.append(Lx)
    cols.append(-X); A = np.vstack(cols).T
    co, *_ = np.linalg.lstsq(A, Y, rcond=None); r = Y - A @ co
    return dict(k=co[-1], b=(co[-2] if with_b else None), rss=float(r @ r), n=len(Y), rms=float(np.sqrt(np.mean(r**2))),
                mx=float(np.max(np.abs(r))), res=r)

def refine(rss_row):
    i = int(np.argmin(rss_row))
    if 0 < i < len(GRID) - 1:
        y0, y1, y2 = rss_row[i - 1], rss_row[i], rss_row[i + 1]; den = y0 - 2 * y1 + y2
        return GRID[i] + (0.5 * 0.001 * (y0 - y2) / den if den > 0 else 0.0), i
    return GRID[i], i

def report_model(name, data, curves, boot=2000, **kw):
    T = cstats(data, curves)
    rss, kk, bb = solve_profile(T, GRID, **kw); rss = rss[0]
    a, i = refine(rss); f = fit(data, curves, a, **kw); n = f['n']
    check(abs(f['rss'] - solve_profile(T, [a], **kw)[0][0, 0]) < 1e-9 * max(1, f['rss']), f'{name}: closed-form RSS equals direct lstsq')
    f0, f5, f1 = (fit(data, curves, g, **kw) for g in (0.0, 0.5, 1.0))
    pl = GRID[n * np.log(rss / rss.min()) <= 3.84]
    win = GRID[np.sqrt(rss / n) <= 1.1 * np.sqrt(rss.min() / n)]
    loo = []
    for j in range(len(curves)):
        mm = np.ones(len(curves)); mm[j] = 0; loo.append(refine(solve_profile(T, GRID, m=mm, **kw)[0][0])[0])
    rng = np.random.default_rng(20260926)
    M = np.stack([np.bincount(rng.integers(0, len(curves), len(curves)), minlength=len(curves)) for _ in range(boot)]).astype(float)
    M = M[(M > 0).sum(1) >= 3]
    R = solve_profile(T, GRID, m=M, **kw)[0]
    bs = np.array([refine(r)[0] for r in R])
    edge = np.mean((np.argmin(R, 1) == 0) | (np.argmin(R, 1) == len(GRID) - 1))
    q = np.percentile(bs, [2.5, 97.5])
    print(f'{name}: {len(curves)} curves, {n} points; best alpha {a:.4f}; k {f["k"]:.5f}' +
          (f', b {f["b"]:.4f}' if f['b'] is not None else '') + f'; RMS {f["rms"]:.5f} max {f["mx"]:.4f}')
    print(f'   RMS at alpha = 0 / 1/2 / 1: {f0["rms"]:.5f} / {f5["rms"]:.5f} / {f1["rms"]:.5f}; '
          f'k at 1/2: {f5["k"]:.5f}' + (f', b at 1/2: {f5["b"]:.4f}' if f5['b'] is not None else ''))
    print(f'   (i) Gaussian profile 95 % (iid; too narrow): [{pl.min():.3f}, {pl.max():.3f}]; '
          f'(ii) curve bootstrap 95 % ({len(bs)} draws; at grid edge {edge:.3f}): [{q[0]:.3f}, {q[1]:.3f}], median {np.median(bs):.3f}; '
          f'(iii) leave-one-out: [{min(loo):.3f}, {max(loo):.3f}]; (iv) RMS <= 1.1 x min: [{win.min():.3f}, {win.max():.3f}]')
    print(f'   alpha = 1/2 inside the bootstrap interval: {bool(q[0] <= 0.5 <= q[1])}; n log(RSS(1/2)/RSS_min) = {n*np.log(f5["rss"]/rss.min()):.2f}')
    return dict(a=a, f=f, f5=f5, boot=q, pl=(pl.min(), pl.max()), loo=(min(loo), max(loo)), win=(win.min(), win.max()), bs=bs)

def between(data, curves, label, show=False):
    """per-curve sqrt(x) slopes and the regression log s = log k - alpha log C"""
    s, lC = [], []
    for c in curves:
        d = data[c]; A = np.vstack([np.ones_like(d['x']), np.sqrt(d['x'])]).T
        co, *_ = np.linalg.lstsq(A, d['y'], rcond=None); s.append(-co[1]); lC.append(np.log(d['C']))
    s, lC = np.array(s), np.array(lC)
    r = stats.linregress(lC, np.log(s)); t = stats.t.ppf(0.975, len(s) - 2)
    print(f'{label}: log s_c = {r.intercept:.4f} - alpha log C: alpha = {-r.slope:.4f} +/- {r.stderr:.4f} (s.e.); '
          f'95 % t interval [{-r.slope - t*r.stderr:.3f}, {-r.slope + t*r.stderr:.3f}]; r^2 = {r.rvalue**2:.3f}; '
          f'k = exp(intercept) = {np.exp(r.intercept):.4f} digits per sqrt(x)/C^alpha')
    if show:
        res = np.log(s) - (r.intercept + r.slope * lC)
        sf = lambda C: all(e == 1 for e in _fac(C).values())
        print('   per-curve residual of log s_c (percent; + = faster than the fitted law); reduction: semistable (S) or additive somewhere (A)')
        print('   ' + ', '.join(f'{c} {"S" if sf(data[c]["C"]) else "A"} {100*v:+.1f}' for c, v in zip(curves, res)))
        a_ = np.array([not sf(data[c]['C']) for c in curves])
        if a_.any() and (~a_).any():
            print(f'   mean residual: semistable {100*res[~a_].mean():+.2f} % ({(~a_).sum()}), additive {100*res[a_].mean():+.2f} % ({a_.sum()})')
    return -r.slope, r.stderr, t

def _fac(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0: f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

# ---------------------------------------------------------------- main
if __name__ == '__main__':
    sel_std = lambda x, C: 13 <= x <= 50
    D60 = load(LISTED + EXTRA, lambda c: 'N60', lambda x, C: True)
    print('== certified data: parity and inertia audit (all knots x = 2..50, N = 60)')
    odd_curves = []
    for c, d in D60.items():
        E = d['all']; xs = sorted(E)
        odd = [x for x in xs if E[x]['par'] == -1]; indef = [x for x in xs if E[x]['negE'] or E[x]['negO']]
        odd13 = [x for x in odd if x >= 13]
        if odd13: odd_curves.append(c)
        print(f'   {c:>5} C={d["C"]:>3}: parity odd at x = {odd if odd else "none"}; indefinite knots {indef if indef else "none"}; '
              f'all 12-digit certified: {all(E[x]["cert"] for x in xs)}')
    print(f'   curves with an odd global minimum at some knot 13 <= x <= 50 (dropped from fits): {odd_curves if odd_curves else "none"}')

    data = {c: {**d, **{k: v[(d['x'] >= 13) & (d['x'] <= 50)] for k, v in d.items() if k in ('x', 'y', 'par')}}
            for c, d in D60.items()}
    S16 = [c for c in LISTED if c in data and c not in odd_curves]
    S19 = S16 + [c for c in EXTRA if c in data and c not in odd_curves]

    print('\n== table: log10 of the certified global minimum eps (N = 60) at x = 13, 25, 50; per-curve slopes on 13 <= x <= 50')
    print('   curve   C   eps(13)          eps(25)          eps(50)          digits/sqrt(x)  digits/unit S_max  RMS(sqrt x)  RMS(x)   best p')
    rows = {}
    for c in S19:
        d = data[c]; x, y = d['x'], d['y']; E = d['all']
        A = np.vstack([np.ones_like(x), np.sqrt(x)]).T; co, *_ = np.linalg.lstsq(A, y, rcond=None); rs = np.sqrt(np.mean((y - A @ co)**2))
        S = 2 * np.sqrt(x / d['C']); A2 = np.vstack([np.ones_like(S), S]).T; c2, *_ = np.linalg.lstsq(A2, y, rcond=None)
        A3 = np.vstack([np.ones_like(x), x]).T; c3, *_ = np.linalg.lstsq(A3, y, rcond=None); rx = np.sqrt(np.mean((y - A3 @ c3)**2))
        ps = np.linspace(0.05, 1.5, 1451); pr = [np.sqrt(np.mean((y - np.vstack([np.ones_like(x), x**p]).T @ np.linalg.lstsq(np.vstack([np.ones_like(x), x**p]).T, y, rcond=None)[0])**2)) for p in ps]
        g = lambda xx: min(E[xx]['e'], E[xx]['o'])
        rows[c] = dict(s=-co[1], sS=-c2[1])
        print(f'   {c:>5} {d["C"]:>3}  {g(13.0):.9e}  {g(25.0):.9e}  {g(50.0):.9e}  {-co[1]:>12.5f}  {-c2[1]:>15.5f}  {rs:>11.5f}  {rx:.5f}  {ps[int(np.argmin(pr))]:.3f}')
    check(abs(rows['11a1']['s'] - 3.072212) < 5e-6, '11a1 N=60 sqrt(x) slope reproduces lane E (3.072212)')
    check(abs(rows['14a1']['s'] - 2.676512) < 5e-6, '14a1 N=60 sqrt(x) slope reproduces lane E (2.676512)')
    sS = np.array([rows[c]['sS'] for c in S16])
    print(f'   digits per unit S_max over the 16 listed curves: mean {sS.mean():.3f}, s.d. {sS.std(ddof=1):.3f}, range [{sS.min():.3f}, {sS.max():.3f}]; '
          f'4 pi / ln 10 = {4*np.pi/np.log(10):.4f}; review range for other objects 4.3-5.4')

    print('\n== joint fits, S16 (N = 60, 13 <= x <= 50)')
    R = {}
    R['S16M1'] = report_model('M1 per-curve a_c', data, S16)
    R['S16M2'] = report_model('M2 common a', data, S16, common_a=True)
    R['S16M3'] = report_model('M3 per-curve a_c + common b log10 x', data, S16, with_b=True)
    R['S16M4'] = report_model('M4 common a + common b log10 x', data, S16, common_a=True, with_b=True)
    between(data, S16, 'between-curve regression, S16', show=True)
    print('\n== joint fits, S19 = S16 + 50a1, 67a1, 109a1 (same window; the extras sit at z = sqrt(x/C) < 1 over much of it)')
    R['S19M1'] = report_model('M1 per-curve a_c', data, S19)
    R['S19M3'] = report_model('M3 per-curve a_c + common b log10 x', data, S19, with_b=True)
    between(data, S19, 'between-curve regression, S19')

    # ---------------------------------------------------------------- matched phase-space window
    zlo, zhi = np.sqrt(13 / 11), np.sqrt(50 / 11)
    MZ = load([c for c in LISTED + EXTRA if c != '11a1'], lambda c: 'N60_matchz', lambda x, C: True)
    MZ['11a1'] = D60['11a1']
    mz = {}
    for c, d in MZ.items():
        E = d['all']; C = d['C']
        xs = np.array(sorted(x for x in E if zlo - 1e-12 <= np.sqrt(x / C) <= zhi + 1e-12))
        if c in odd_curves or any(E[x]['par'] == -1 for x in xs):
            print(f'# matched window: {c} has an odd global minimum; dropped'); continue
        mz[c] = dict(C=C, x=xs, y=np.log10([min(E[x]['e'], E[x]['o']) for x in xs]), all=E)
    if len(mz) >= 4:
        M16 = [c for c in LISTED if c in mz]; M19 = M16 + [c for c in EXTRA if c in mz]
        print(f'\n== matched window z = sqrt(x/C) in [{zlo:.4f}, {zhi:.4f}] (x in [13 C/11, 50 C/11], capped at 250)')
        print('   curve   C  xmax  knots  z range         digits/unit S_max  digits/sqrt(x)   eps at the largest knot')
        for c in M19:
            d = mz[c]; x, y = d['x'], d['y']; S = 2 * np.sqrt(x / d['C'])
            c2 = np.linalg.lstsq(np.vstack([np.ones_like(S), S]).T, y, rcond=None)[0]
            c1 = np.linalg.lstsq(np.vstack([np.ones_like(x), np.sqrt(x)]).T, y, rcond=None)[0]
            print(f'   {c:>5} {d["C"]:>3} {x[-1]:>5.0f} {len(x):>6}  [{np.sqrt(x[0]/d["C"]):.3f}, {np.sqrt(x[-1]/d["C"]):.3f}]  {-c2[1]:>15.5f}  {-c1[1]:>13.5f}   {10**y[-1]:.6e}')
        sM = np.array([-np.linalg.lstsq(np.vstack([np.ones(len(mz[c]['x'])), 2*np.sqrt(mz[c]['x']/mz[c]['C'])]).T, mz[c]['y'], rcond=None)[0][1] for c in M16])
        print(f'   matched window, digits per unit S_max over {len(M16)} listed curves: mean {sM.mean():.3f}, s.d. {sM.std(ddof=1):.3f}, range [{sM.min():.3f}, {sM.max():.3f}]')
        R['MZ16M1'] = report_model('MZ M1 per-curve a_c', mz, M16)
        R['MZ16M2'] = report_model('MZ M2 common a', mz, M16, common_a=True)
        R['MZ16M3'] = report_model('MZ M3 per-curve a_c + common b log10 x', mz, M16, with_b=True)
        between(mz, M16, 'between-curve regression, matched window, 16 listed', show=True)
        if len(M19) > len(M16):
            R['MZ19M1'] = report_model('MZ M1 with extras', mz, M19)
            between(mz, M19, 'between-curve regression, matched window, with extras')

    # ---------------------------------------------------------------- N = 120 saturation
    print('\n== saturation: N = 120 against N = 60 at the same knots (certified minima)')
    for c in ['11a1', '17a1', '26a1', '36a1']:
        fn = OUT / f'rtp2_ellconductors_{c}_axisx_ccm_N120.txt'
        if not fn.exists(): print(f'   {c}: N = 120 file missing'); continue
        E1 = eig(fn); E0 = D60[c]['all']; xs = sorted(x for x in E1 if 13 <= x <= 50)
        rel = [abs(min(E0[x]['e'], E0[x]['o']) / min(E1[x]['e'], E1[x]['o']) - 1) for x in xs]
        mono = all(min(E1[x]['e'], E1[x]['o']) <= min(E0[x]['e'], E0[x]['o']) for x in xs)
        check(mono, f'{c}: N = 120 minimum <= N = 60 minimum at every knot (nested truncations)')
        y1 = np.log10([min(E1[x]['e'], E1[x]['o']) for x in xs]); xa = np.array(xs)
        s1 = -np.linalg.lstsq(np.vstack([np.ones_like(xa), np.sqrt(xa)]).T, y1, rcond=None)[0][1]
        print(f'   {c}: max relative change of eps from N = 60 to 120 over 13..50: {max(rel):.3e} (at x = {xs[int(np.argmax(rel))]:.0f}); '
              f'sqrt(x) slope N = 120: {s1:.6f} vs N = 60: {rows[c]["s"]:.6f}; digits per unit S_max N = 120: {s1*np.sqrt(cond(c))/2:.5f} vs N = 60: {rows[c]["sS"]:.5f}')
    print('\n== saturation at the top of the matched window: single-knot N = 120 and N = 200 against N = 60 (certified minima)')
    for c in ['11a1', '20a1', '27a1', '36a1', '50a1', '67a1']:
        xm = min(250, round(50 * cond(c) / 11)); e = {}
        src = OUT / (f'rtp2_ellconductors_{c}_axisx_ccm_N60.txt' if xm <= 50 else f'rtp2_ellconductors_{c}_axisx_ccm_N60_matchz.txt')
        E = eig(src); e[60] = min(E[float(xm)]['e'], E[float(xm)]['o'])
        for n in (120, 200):
            fn = OUT / f'rtp2_ellconductors_{c}_point_x{xm}_N{n}.txt'
            if fn.exists():
                P = eig(fn); e[n] = min(P[float(xm)]['e'], P[float(xm)]['o'])
                check(P[float(xm)]['par'] == 1, f'{c} x={xm} N={n}: even global minimum')
        if len(e) < 3: print(f'   {c} x = {xm}: point files missing'); continue
        check(e[200] <= e[120] <= e[60], f'{c} x={xm}: eps non-increasing in N')
        print(f'   {c} x = {xm} (z = {np.sqrt(xm/cond(c)):.3f}): eps N=60 {e[60]:.9e}, N=120 {e[120]:.9e}, N=200 {e[200]:.9e}; '
              f'log10(eps60/eps200) = {np.log10(e[60]/e[200]):.4f} digits, log10(eps120/eps200) = {np.log10(e[120]/e[200]):.5f}')
    print(f'\n# checks: {checks} run, {fails} failed')
    sys.exit(bool(fails))
