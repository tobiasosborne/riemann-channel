#!/usr/bin/env python3
"""claude:opus REFUTE review of RTP-2 lane D (2026-09-26). FLOATING post-processing only.
Independent refit from outputs/rtp2_dirichlet_*_axisN_x*.txt (EIG lines = certified eigenvalue
balls rounded to 12 digits by the driver). Checks: completeness of each file, tail of eps_N,
slopes, three-point (b, c) fits, the '0.7% of 4 pi' claim, the 1/q law, parity, N_sat vs D1b,
and the X=1 control identity shift log(q2/q1)."""
import re, glob, math
import numpy as np
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'outputs'
Ds = [-4, -3, 5, 8, -7, 12, -20, 21, 13, -8]
LN10 = math.log(10); FOURPI = 4 * math.pi; R0 = FOURPI / LN10

def parse(D, x):
    f = OUT / f'rtp2_dirichlet_D{D}_axisN_x{x}.txt'
    s = f.read_text()
    eig = {}
    for m in re.finditer(r'^EIG x=\S+ X=\S+ N=(\d+) epsE=(\S+) epsO=(\S+) parity=(-?\d)', s, re.M):
        eig[int(m.group(1))] = (float(m.group(2)), float(m.group(3)), int(m.group(4)))
    ctl = {}
    for m in re.finditer(r'^CONTROL x=\S+ N=(\d+) minE=(\S+) minO=(\S+) negE=(\d+) posE=\d+ negO=(\d+)', s, re.M):
        ctl[int(m.group(1))] = (float(m.group(2)), float(m.group(3)), int(m.group(4)), int(m.group(5)))
    sat = {m.group(1): int(m.group(2)) for m in re.finditer(r'^SAT block=(\w+) N=(\d+)', s, re.M)}
    done = re.search(r'^# checks: (\d+) run, (\d+) failed', s, re.M)
    fails = len(re.findall(r'CHECK FAIL', s))
    comp = len(re.findall(r'^COMP ', s, re.M))
    ray = bool(re.search(r'^RAY_TOTAL', s, re.M))
    return dict(eig=eig, ctl=ctl, sat=sat, done=done.groups() if done else None, fails=fails, comp=comp, ray=ray)

data = {(D, x): parse(D, x) for D in Ds for x in (13, 25, 50)}
Nfin = {13: 200, 25: 260, 50: 420}

print('== 1. completeness of axisN files')
for (D, x), d in data.items():
    if x != 50: 
        if not d['done'] or d['done'][1] != '0': print('INCOMPLETE', D, x, d['done'])
        continue
    print(f'D={D:4d} x=50 checks_line={d["done"]} CHECK_FAIL_lines={d["fails"]} RAY_TOTAL={d["ray"]} COMP_lines={d["comp"]} EIG_N={sorted(d["eig"])}')

print('\n== 2. tail of eps_E(N) (interlacing: eps_N nonincreasing, so final-N values are UPPER bounds)')
tail = {}
for (D, x), d in sorted(data.items()):
    Ns = sorted(d['eig']); e = [d['eig'][n][0] for n in Ns]
    mono = all(e[i+1] <= e[i] for i in range(len(e)-1))
    # log-log local exponent of the decrement between last three points: eps(N) = e_inf + A N^-p
    n1, n2, n3 = Ns[-3:]; e1, e2, e3 = e[-3:]
    # solve for p from (e1-e2)/(e2-e3) = (n1^-p - n2^-p)/(n2^-p - n3^-p)
    r = (e1 - e2) / (e2 - e3)
    f = lambda p: (n1**-p - n2**-p) / (n2**-p - n3**-p) - r
    ps = np.linspace(0.05, 6, 6000); vals = [f(p) for p in ps]
    p = None
    for i in range(len(ps)-1):
        if vals[i] * vals[i+1] < 0: p = ps[i]; break
    if p is not None:
        A = (e2 - e3) / (n2**-p - n3**-p); einf = e3 - A * n3**-p
        extra = math.log10(e3 / einf) if einf > 0 else float('nan')
    else:
        einf = float('nan'); extra = float('nan')
    tail[(D, x)] = (e3, einf, extra, p)
    print(f'D={D:4d} x={x:2d} N={Ns} monotone={mono} last ratios={[round(e[i]/e[i+1],4) for i in range(len(e)-1)][-3:]}'
          f' p_fit={p if p is None else round(p,2)} extrapolated extra digits below final N={extra:.3f}')

def efin(D, x): return data[(D, x)]['eig'][Nfin[x]][0]
def s(D, a, b, fn=efin): return (math.log10(fn(D, a)) - math.log10(fn(D, b))) / (b - a)

print('\n== 3. slopes (digits per unit x, final N), q*slope(13-50), q*slope(25-50)')
rows = []
for D in Ds:
    q = abs(D); k = int(D < 0)
    s1, s2, s3 = s(D, 13, 25), s(D, 25, 50), s(D, 13, 50)
    rows.append((D, q, k, s1, s2, s3))
    print(f'D={D:4d} q={q:2d} kappa={k} s13-25={s1:.6f} s25-50={s2:.6f} s13-50={s3:.6f} q*s13-25={q*s1:.4f} q*s25-50={q*s2:.4f} q*s13-50={q*s3:.4f}  (4pi/ln10={R0:.4f})')

print('\n== 4. three-point interpolation log eps = a + b log(x/q) - c x/q ; c/(4pi) ; sensitivity')
def fit3(D, fn=efin):
    q = abs(D); X = np.array([13, 25, 50.]); u = X / q
    y = np.log([fn(D, x) for x in (13, 25, 50)])
    M = np.column_stack([np.ones(3), np.log(u), -u])
    a, b, c = np.linalg.solve(M, y); return b, c / FOURPI
for D in Ds:
    b, c = fit3(D)
    # sensitivity 1: x=50 value lowered by the extrapolated remaining tail (section 2)
    ex50 = tail[(D, 50)][2]; ex13 = tail[(D, 13)][2]; ex25 = tail[(D, 25)][2]
    def fn_ext(DD, x):
        e = efin(DD, x); ex = {13: ex13, 25: ex25, 50: ex50}[x]
        return e * 10**(-ex) if ex == ex else e
    b2, c2 = fit3(D, fn_ext)
    # sensitivity 2: use N=120 / 180 / 260 (previous sampled N) instead of final N
    prevN = {13: 120, 25: 180, 50: 260}
    b3, c3 = fit3(D, lambda DD, x: data[(DD, x)]['eig'][prevN[x]][0])
    print(f'D={D:4d} b={b:8.4f} c/4pi={c:.5f} dev={100*(c-1):+.2f}% | tail-extrapolated: b={b2:.3f} c/4pi={c2:.5f} | prev-N: b={b3:.3f} c/4pi={c3:.5f}')
cs = [fit3(D)[1] for D in Ds]
print('within 0.7% of 4pi:', [D for D, c in zip(Ds, cs) if abs(c-1) <= 0.007], ' within 1%:', [D for D, c in zip(Ds, cs) if abs(c-1) <= 0.01])

print('\n== 5. fixed c = 4 pi, fitted b per D from least squares over 3 points (residual shows curvature misfit)')
for D in Ds:
    q = abs(D); X = np.array([13, 25, 50.]); u = X / q
    y = np.log([efin(D, x) for x in (13, 25, 50)]) + FOURPI * u
    M = np.column_stack([np.ones(3), np.log(u)]); (a, b), res, *_ = np.linalg.lstsq(M, y, rcond=None)
    r = y - M @ np.array([a, b])
    print(f'D={D:4d} b(c=4pi)={b:.4f} max residual={np.max(np.abs(r))/LN10:.4f} digits')

print('\n== 6. power law slope ~ q^-p (13-50 slopes, 10 characters; +zeta q=1 at 5.37857 from review N=420)')
q = np.array([abs(D) for D in Ds], float); sl = np.array([r[5] for r in rows])
P = np.polyfit(np.log(q), np.log(sl), 1); print(f'10 chars: slope ~ q^({P[0]:.4f}), q*slope at q=1 -> {math.exp(P[1]):.4f}')
q2 = np.append(q, 1.0); sl2 = np.append(sl, 5.37857)
P2 = np.polyfit(np.log(q2), np.log(sl2), 1); print(f'with zeta : slope ~ q^({P2[0]:.4f}), prefactor {math.exp(P2[1]):.4f}')
small = q <= 8; P3 = np.polyfit(np.log(q[small]), np.log(sl[small]), 1); print(f'q<=8 only: slope ~ q^({P3[0]:.4f})')
sl25 = np.array([r[4] for r in rows]); P4 = np.polyfit(np.log(q), np.log(sl25), 1); print(f'25-50 slopes: slope ~ q^({P4[0]:.4f}), q*slope(q=1) {math.exp(P4[1]):.4f}')
# alternatives: slope ~ 1/log-conductor? test q vs sqrt(q) vs log q via R^2 of linear fits of slope against 1/q, 1/sqrt q
for name, g in [('1/q', 1/q), ('1/sqrt(q)', q**-0.5), ('1/log(q)', 1/np.log(q))]:
    A = np.column_stack([g]); coef, res, *_ = np.linalg.lstsq(A, sl, rcond=None)
    rms = math.sqrt(np.mean((sl - A @ coef)**2)); print(f'  through-origin fit slope = k*{name}: k={coef[0]:.4f} rms={rms:.4f} digits/x')

print('\n== 7. parity at matched conductor q=8 (kappa=0: D=8, kappa=1: D=-8)')
for x0, x1 in [(13, 25), (25, 50), (13, 50)]:
    print(f'  {x0}-{x1}: D=8 {s(8,x0,x1):.5f}  D=-8 {s(-8,x0,x1):.5f}  diff {s(8,x0,x1)-s(-8,x0,x1):+.5f}')
print('  eps_E ratio D=-8/D=8 at x=13,25,50:', [round(efin(-8,x)/efin(8,x),5) for x in (13,25,50)])
# residuals of q*slope(25-50) by kappa
for k in (0, 1):
    v = [q_*s2 for (D, q_, kk, s1, s2, s3) in rows if kk == k]
    print(f'  kappa={k}: q*slope25-50 values {np.round(v,3)}')

print('\n== 8. N_sat (full) vs D1b prediction 1.7 x log x / q')
for D in Ds:
    out = []
    for x in (13, 25, 50):
        ns = data[(D, x)]['sat'].get('full'); pred = 1.7 * x * math.log(x) / abs(D)
        out.append(f'x={x}: {ns} vs {pred:.1f}')
    print(f'D={D:4d} ' + ' | '.join(out))

print('\n== 9. X=1 control: minE differences at x=13, N=200 vs log(q2/q1) within each kappa')
for k, ref in [(0, 5), (1, -4)]:
    base = data[(ref, 13)]['ctl'][200][0]
    for D in Ds:
        if int(D < 0) != k or D == ref: continue
        dif = data[(D, 13)]['ctl'][200][0] - base
        print(f'  kappa={k}: D={D:4d} minE-minE(D={ref}) = {dif:.10f}  log(q/q0) = {math.log(abs(D)/abs(ref)):.10f}')
print('  control inertia (negE/negO) at x=50, N=420:', {D: data[(D, 50)]['ctl'].get(420, None) and data[(D,50)]['ctl'][420][2:] for D in Ds})

print('\n== 10. pooled least squares over all 30 final-N points (FLOATING)')
def pooled(model, mask=lambda D, x: True):
    rows_, y = [], []
    pts = [(D, x) for D in Ds for x in (13, 25, 50) if mask(D, x)]
    for D, x in pts:
        q_ = abs(D); u = x / q_; k = int(D < 0)
        r = [1.0 if DD == D else 0.0 for DD in Ds]          # a_D
        if model == 'x/q, b_kappa, common c':
            r += [math.log(u) if k == 0 else 0.0, math.log(u) if k == 1 else 0.0, -u]
        elif model == 'x/q, b_D, common c':
            r += [math.log(u) if DD == D else 0.0 for DD in Ds] + [-u]
        elif model == 'x/q, b_kappa, c=4pi fixed':
            r += [math.log(u) if k == 0 else 0.0, math.log(u) if k == 1 else 0.0]
        elif model == 'raw x, b_kappa, common c':
            r += [math.log(x) if k == 0 else 0.0, math.log(x) if k == 1 else 0.0, -x]
        rows_.append(r)
        yy = math.log(efin(D, x)) + (FOURPI * u if model.endswith('fixed') else 0.0)
        y.append(yy)
    M = np.array(rows_); y = np.array(y)
    coef, *_ = np.linalg.lstsq(M, y, rcond=None); res = (y - M @ coef) / LN10
    return coef, math.sqrt(np.mean(res**2)), np.max(np.abs(res)), len(y), M.shape[1]
for model in ['x/q, b_kappa, common c', 'x/q, b_D, common c', 'x/q, b_kappa, c=4pi fixed', 'raw x, b_kappa, common c']:
    for lab, mask in [('all 30', lambda D, x: True), ('x/q>=1 only', lambda D, x: x / abs(D) >= 1)]:
        coef, rms, mx, n, p = pooled(model, mask)
        extra = ''
        if 'common c' in model: extra = f' c/4pi={coef[-1]/FOURPI:.5f}'
        if 'b_kappa' in model: extra += f' b(kappa=0)={coef[len(Ds)]:.3f} b(kappa=1)={coef[len(Ds)+1]:.3f}'
        print(f'  {model:28s} [{lab:11s}] n={n} params={p} rms={rms:.4f} max={mx:.4f} digits{extra}')

print('\n== 11. zeta (q=1) with c = 4 pi fixed: local power b from round-1 values (x=13 N=200, x=25 N=260, x=50 N=420 review)')
z = {13: 2.85407e-59, 25: 2.42562e-123, 50: 2.80881e-258}
g = {x: math.log(v) + FOURPI * x for x, v in z.items()}
print(f'  b(13-25)={(g[25]-g[13])/math.log(25/13):.3f}  b(25-50)={(g[50]-g[25])/math.log(50/25):.3f}  (CCM h0/h4 sector: 9/2)')
print('  zeta x=50: N_sat=352, N=360 -> 420 changes eps by factor', round(2.26934e-257/2.80881e-258, 2), '(characters: <= 1.15 from N=260 to 420)')

print('\n== 12. alternative organiser: first-zero height gamma_1 (COMPARISON data, used only here) vs conductor q')
g1 = {}
for D in Ds:
    m = re.search(r'^REFERENCE D=\S+ gamma1=(\S+)', (OUT / f'rtp2_dirichlet_D{D}_axisN_x13.txt').read_text(), re.M)
    g1[D] = float(m.group(1))
G = np.array([g1[D] for D in Ds]); Q = np.array([abs(D) for D in Ds], float); S = np.array([r[5] for r in rows])
for name, v in [('q', Q), ('gamma_1', G)]:
    P_ = np.polyfit(np.log(v), np.log(S), 1); r_ = np.log(S) - np.polyval(P_, np.log(v))
    print(f'  log slope13-50 vs log {name}: exponent {P_[0]:.3f}, rms residual {math.sqrt(np.mean(r_**2)):.4f} (natural-log units)')

print('\n== 13. local log-log exponent -dln(eps_E)/dln(N) on the last two sampled steps (tail regime diagnosis)')
for (D, x), d in sorted(data.items()):
    Ns = sorted(n for n in d['eig'] if n >= 80) if x == 50 else sorted(n for n in d['eig'] if n >= 80)
    e = [d['eig'][n][0] for n in Ns]
    loc = [math.log(e[i]/e[i+1]) / math.log(Ns[i+1]/Ns[i]) for i in range(len(Ns)-1)]
    flag = 'NOT decreasing' if len(loc) >= 2 and loc[-1] >= loc[-2] else ''
    print(f'  D={D:4d} x={x:2d} N={Ns} exponents={[round(v,3) for v in loc]} {flag}')
