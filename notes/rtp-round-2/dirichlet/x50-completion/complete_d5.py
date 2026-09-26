#!/usr/bin/env python3
"""Author claude:opus, 2026-09-26. Completion of lane D's D5 tables after the five x=50 reruns.
Runs the lane's own checks/summary.py (codex:gpt-6-astra) on the 52 complete outputs, applies the
REFUTE review's D5 corrections (captions, zeta R1 label, D=13 sentence), and appends FLOATING
analyses computed here independently of the review's script: q x slope per character with the
through-origin k/q fit, the pooled fit (one exponent c, one power of x/q per parity, one amplitude
per character), per-character powers with c = 4 pi fixed, N_sat against D1b, and the tail exponents.
Writes x50-completion/d5_tables.md and replaces the D5_TABLES block of astra-proofs.md.
Every eigenvalue is a rounded certified ball from the driver; everything derived here is FLOATING."""
import math, re, subprocess, sys
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent; LANE = HERE.parent; ROOT = LANE.parents[2]; OUT = ROOT/'outputs'
Ds = [-4, -3, 5, 8, -7, 12, -20, 21, 13, -8]; XS = (13, 25, 50); NF = {13: 200, 25: 260, 50: 420}
LN10 = math.log(10); FOURPI = 4*math.pi; R0 = FOURPI/LN10

s = subprocess.check_output([sys.executable, str(LANE/'checks/summary.py')], text=True)
body = s[s.index('# D5. Saturation'):].replace('# D5. Saturation', '### Saturation').replace('\n# ', '\n### ')

# --- review corrections inside the generated block
old5 = 'This is a three-point interpolation, not a validated asymptotic expansion.'
new5 = old5 + (' It has no residual; b and c are strongly correlated (tail-extrapolated inputs move c/(4pi) by up to 0.003 and b by up to 0.28). '
       'Pooled over all 30 final-N points with one c, one b per parity and one amplitude per character: c/(4pi) = 1.0039, rms 0.043 digits; '
       'for x/q >= 1 only, 1.0019, rms 0.036; the same model in raw x has rms 6.8 digits (`notes/reviews/scratch_rtp2_dirichlet_refit.py`, section 10).'
       ' *[Correction 5 of the REFUTE review, inserted by claude:opus; the pooled numbers are reproduced on the complete outputs below.]*')
assert body.count(old5) == 1; body = body.replace(old5, new5)
body = body.replace('| zeta R1 | 50 | 360 |', '| zeta R1 (unconverged, N=360) | 50 | 360 |')
body = body.replace('| zeta R1 | 5.33922 |', '| zeta R1 (x=50 at N=360: not used) | 5.33922 |')
anchor = '### FLOATING conductor scaling and polynomial fit'
body = body.replace(anchor, ('D=13 is the only character whose 25–50 slope (0.409726) is below its 13–25 slope (0.412255). '
    '*[Correction 4 of the REFUTE review, sentence inserted by claude:opus.]* The zeta row at x=50, N=360 is not converged '
    '(N_sat=352; N=360 to 420 lowers eps by a factor 8.1), so the zeta 13–50 slope to use is the review row, 5.37857 '
    '*[review D5(d), claude:opus]*.\n\n') + anchor)

# --- independent parsing of the certified EIG/SAT/COMP lines
def parse(D, x):
    t = (OUT/f'rtp2_dirichlet_D{D}_axisN_x{x}.txt').read_text()
    assert re.search(r'^# checks: \d+ run, 0 failed$', t, re.M), (D, x)
    eig = {int(m[1]): (float(m[2]), float(m[3])) for m in re.finditer(r'^EIG x=\S+ X=\S+ N=(\d+) epsE=(\S+) epsO=(\S+) parity=1 ', t, re.M)}
    sat = {m[1]: int(m[2]) for m in re.finditer(r'^SAT block=(\w+) N=(\d+)', t, re.M)}
    comp = {int(m[1]): float(m[2]) for m in re.finditer(r'^COMP x=\S+ X=\S+ N=(\d+) .* error=(\S+) ', t, re.M)}
    return eig, sat, comp
data = {(D, x): parse(D, x) for D in Ds for x in XS}
ef = lambda D, x: data[D, x][0][NF[x]][0]
sl = lambda D, a, b: (math.log10(ef(D, a)) - math.log10(ef(D, b)))/(b - a)
out = ['### FLOATING q × slope per character (claude:opus, complete outputs)\n',
       'q × slope in decimal digits per unit x/q; 4π/ln10 = %.4f. Final-N values (certified upper bounds on the infinite-N eps).\n' % R0,
       '| D | q | kappa | slope 13–50 | q×slope 13–25 | q×slope 25–50 | q×slope 13–50 | x/q at x=13 |', '|---|---|---|---|---|---|---|---|']
for D in Ds:
    q = abs(D)
    out.append(f'| {D} | {q} | {int(D<0)} | {sl(D,13,50):.6f} | {q*sl(D,13,25):.4f} | {q*sl(D,25,50):.4f} | {q*sl(D,13,50):.4f} | {13/q:.3f} |')
qv = np.array([abs(D) for D in Ds], float); sv = np.array([sl(D, 13, 50) for D in Ds])
fits = []
for name, g in [('k/q', 1/qv), ('k/sqrt q', qv**-0.5), ('k/log q', 1/np.log(qv))]:
    k = float(np.dot(g, sv)/np.dot(g, g)); fits.append(f'{name}: k = {k:.4f}, rms {math.sqrt(np.mean((sv-k*g)**2)):.4f}')
p1 = np.polyfit(np.log(qv), np.log(sv), 1); p2 = np.polyfit(np.log(np.append(qv, 1)), np.log(np.append(sv, 5.37857)), 1)
out.append('\nThrough-origin fits of the ten 13–50 slopes (digits per unit x): ' + '; '.join(fits) +
           f'. Free power law: slope ∝ q^{p1[0]:.3f} (ten characters), q^{p2[0]:.3f} with zeta (q=1, review value 5.37857). '
           f'q × slope(13–50) range [{(qv*sv).min():.3f}, {(qv*sv).max():.3f}]. FLOATING.\n')

def pooled(model, mask):
    M, y = [], []
    for D in Ds:
        for x in XS:
            if not mask(D, x): continue
            q = abs(D); u = x/q; k = int(D < 0); r = [float(DD == D) for DD in Ds]
            if model == 'common c, b per parity': r += [math.log(u)*(k == 0), math.log(u)*(k == 1), -u]
            elif model == 'c = 4pi fixed, b per parity': r += [math.log(u)*(k == 0), math.log(u)*(k == 1)]
            elif model == 'common c, b per character': r += [math.log(u)*(DD == D) for DD in Ds] + [-u]
            elif model == 'raw x: common c, b per parity': r += [math.log(x)*(k == 0), math.log(x)*(k == 1), -x]
            M.append(r); y.append(math.log(ef(D, x)) + (FOURPI*u if 'fixed' in model else 0.0))
    M = np.array(M); y = np.array(y); c, *_ = np.linalg.lstsq(M, y, rcond=None); res = (y - M@c)/LN10
    return c, math.sqrt(np.mean(res**2)), np.abs(res).max(), len(y), M.shape[1]
out += ['### FLOATING pooled fit over the 30 final-N points (claude:opus, complete outputs)\n',
        'Model log eps = a_D + b_kappa log(x/q) − c x/q (one amplitude per character). Residuals in decimal digits.\n',
        '| model | points | parameters | c/(4π) | b(kappa=0) | b(kappa=1) | rms | max |', '|---|---|---|---|---|---|---|---|']
for model in ['common c, b per parity', 'c = 4pi fixed, b per parity', 'common c, b per character', 'raw x: common c, b per parity']:
    for lab, mask in [('all 30', lambda D, x: True), ('x/q ≥ 1', lambda D, x: x/abs(D) >= 1)]:
        c, rms, mx, n, p = pooled(model, mask)
        cc = f'{c[-1]/FOURPI:.5f}' if 'common c' in model else '1 (fixed)'
        b0, b1 = (f'{c[10]:.3f}', f'{c[11]:.3f}') if 'parity' in model else ('per D', 'per D')
        out.append(f'| {model} [{lab}] | {n} | {p} | {cc} | {b0} | {b1} | {rms:.4f} | {mx:.4f} |')
bfix = {}
for D in Ds:
    q = abs(D); u = np.array(XS, float)/q; y = np.log([ef(D, x) for x in XS]) + FOURPI*u
    A = np.column_stack([np.ones(3), np.log(u)]); bfix[D] = float(np.linalg.lstsq(A, y, rcond=None)[0][1])
k0 = [bfix[D] for D in Ds if D > 0]; k1 = [bfix[D] for D in Ds if D < 0]
out.append('\nPer-character power of x/q with c = 4π fixed (least squares over the three windows): ' +
           ', '.join(f'D={D}: {bfix[D]:.3f}' for D in Ds) +
           f'. Range {min(k0):.2f}–{max(k0):.2f} (mean {np.mean(k0):.2f}) for kappa=0, {min(k1):.2f}–{max(k1):.2f} (mean {np.mean(k1):.2f}) for kappa=1. '
           'Parity at q=8: eps(D=-8)/eps(D=8) = ' + ', '.join(f'{ef(-8,x)/ef(8,x):.1f}' for x in XS) + ' at x = 13, 25, 50. FLOATING.\n')
out += ['### N_sat (full window) against the D1b heuristic 1.7 x log x / q\n', '| D | x=13 | x=25 | x=50 |', '|---|---|---|---|']
for D in Ds:
    out.append(f'| {D} | ' + ' | '.join(f'{data[D,x][1]["full"]} vs {1.7*x*math.log(x)/abs(D):.1f}' for x in XS) + ' |')
out += ['\n### FLOATING tail diagnosis: local exponent −d ln eps/d ln N on the sampled steps from N=80\n',
        'eps_N is nonincreasing in N (interlacing), so every final-N value is a certified upper bound on the infinite-N value. '
        '"not decreasing" marks points not shown to be in a convergent tail.\n', '| D | x | N | exponents | last-step digits | flag |', '|---|---|---|---|---|---|']
flags = []
for D in Ds:
    for x in XS:
        e = data[D, x][0]; Ns = sorted(n for n in e if n >= 80); v = [e[n][0] for n in Ns]
        loc = [math.log(v[i]/v[i+1])/math.log(Ns[i+1]/Ns[i]) for i in range(len(Ns)-1)]
        fl = 'not decreasing' if len(loc) >= 2 and loc[-1] >= loc[-2] else ''
        if fl: flags.append((D, x))
        out.append(f'| {D} | {x} | {",".join(map(str,Ns))} | {", ".join(f"{t:.3f}" for t in loc)} | {math.log10(v[-2]/v[-1]):.3f} | {fl} |')
cmpd = max(abs(sl(D,13,50) - (math.log10(data[D,13][2][200]) - math.log10(data[D,50][2][420]))/37) for D in Ds)
out.append(f'\nNot shown in a decreasing tail: {", ".join(f"D={D} x={x}" for D,x in flags)}. '
           f'Largest |eps slope − first-zero-error slope| over 13–50, all ten characters (COMPARISON): {cmpd:.4f} digits per unit x.\n')
block = body.rstrip() + '\n\n' + '\n'.join(out) + '\n'
(HERE/'d5_tables.md').write_text(block)
p = LANE/'astra-proofs.md'; r = p.read_text(); a, b = '<!-- D5_TABLES_BEGIN -->', '<!-- D5_TABLES_END -->'
i, j = r.index(a), r.index(b) + len(b)
p.write_text(r[:i] + a + '\n*[D5 tables regenerated by claude:opus on 2026-09-26 from the 52 complete outputs with `x50-completion/complete_d5.py`, which runs the lane\'s `checks/summary.py` and appends the analyses after "x50 determinant and precision audit".]*\n\n' + block + '\n' + b + r[j:])
print('ok', len(block), 'chars; flags', flags, 'cmpd', round(cmpd, 4))
