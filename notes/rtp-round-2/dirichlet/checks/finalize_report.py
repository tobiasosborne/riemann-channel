#!/usr/bin/env python3
"""Author codex:gpt-6-astra. Finish the report only after every scheduled file passes.
Reproducible floating analysis; preserves the prediction written before all experiments.
"""
from pathlib import Path
import re,subprocess,sys,hashlib,json
import mpmath as mp
mp.mp.dps=60
P=Path(__file__).resolve().parent;ROOT=P.parents[3];OUT=ROOT/'outputs'
Ds=[-4,-3,5,8,-7,12,-20,21,13,-8];core=Ds[:6]
def read(p):
    out={}
    for line in p.read_text().splitlines():
        f=dict(re.findall(r'(\w+)=(\[[^]]*\]|[^\s]+)',line))
        if f:out.setdefault(line.split()[0],[]).append(f)
    return out
files=sorted(OUT.glob('rtp2_dirichlet_D*.txt'));assert len(files)==52
counts=[]
for p in files:
    m=re.search(r'# checks: (\d+) run, (\d+) failed',p.read_text())
    assert m and m[2]=='0',f'Not complete/passing: {p.name}'
    counts.append(int(m[1]))
assert len(list(P.glob('reference_prefix_D*.txt')))==10
assert all('FIRST_POSITIVE_HARDY_Z_CERTIFIED=1' in p.read_text() for p in P.glob('reference_prefix_D*.txt'))
assert 'FAIL' not in (P/'make-check-final.txt').read_text()
assert (P/'make-check-final.txt').read_text().count(': PASS')>=12
r=subprocess.run([sys.executable,str(P/'audit_outputs.py')],capture_output=True,text=True,cwd=ROOT)
(P/'audit_outputs.txt').write_text(r.stdout+r.stderr);assert r.returncode==0,r.stdout+r.stderr
subprocess.run([sys.executable,str(P/'publish_tables.py')],check=True,cwd=ROOT)
subprocess.run([sys.executable,str(P/'plot_rates.py')],check=True,cwd=ROOT)
(OUT/'rtp2_dirichlet_summary.txt').write_text((P/'summary.md').read_text())
data={}
for D in Ds:
    for x,N in [(13,200),(25,260),(50,420)]:
        d=read(OUT/f'rtp2_dirichlet_D{D}_axisN_x{x}.txt')
        e=next(r for r in d['EIG'] if int(r['N'])==N)
        c=next(r for r in d['COMP'] if int(r['N'])==N)
        assert e['parity']=='1' and all(r['parity']=='1' for r in d['EIG'])
        data[D,x]=(d,e,c)
def f(v,n=6):return mp.nstr(v,n)
def s(D,key='epsE',a=13,b=50):
    idx=2 if key=='error' else 1
    return mp.log10(mp.mpf(data[D,a][idx][key])/mp.mpf(data[D,b][idx][key]))/(b-a)
def spread(ds):return max(s(D) for D in ds)-min(s(D) for D in ds)
rates={D:s(D) for D in Ds};lo=min(rates,key=rates.get);hi=max(rates,key=rates.get)
fits={}
for D in Ds:
    ys=[mp.mpf(x)/abs(D) for x in [13,25,50]]
    z=mp.matrix([mp.log(mp.mpf(data[D,x][1]['epsE'])) for x in [13,25,50]])
    a,b,c=mp.lu_solve(mp.matrix([[1,mp.log(y),-y] for y in ys]),z)
    fits[D]=(a,b,c/(4*mp.pi))
K=mp.log10(mp.mpf(50)/13)/37
corrected={D:abs(D)*(s(D)+(1+int(D<0))*K) for D in Ds}
rawq={D:abs(D)*s(D) for D in Ds}
widths=[mp.mpf(data[D,x][0]['ROW'][-1]['rj']) for D in Ds for x in [13,25,50]]
tails=[]
for D in Ds:
    es=sorted(data[D,50][0]['EIG'],key=lambda r:int(r['N']))
    tails.append(mp.mpf(es[-2]['epsE'])/mp.mpf(es[-1]['epsE']))
errdiff=max(abs(s(D)-s(D,'error')) for D in Ds)
coeff=[]
for D in Ds:
    ss=next(r for r in data[D,50][0]['SAT'] if r['block']=='full')
    coeff.append((D,abs(D)*mp.mpf(ss['N'])/(50*mp.log(50))))
# Recorded wall interval of the data files, not included in byte-reproducible raw stdout.
births=[int(subprocess.check_output(['stat','-c','%W',str(p)],text=True)) for p in files]
wall=(max(p.stat().st_mtime for p in files)-min(births))/60 if min(births)>0 else None
p=P.parent/'astra-proofs.md';report=p.read_text()
report=report[:report.index('\n## D6.')]
report=report.replace('## Correction ledger (incremental)','## Correction ledger')
report=report.replace('## D4. Runs (incremental)','## D4. Completed runs')
report=report.replace('The x=50 extension is attempted for all ten characters; eigenvalues at several N will test convergence beyond the determinant minimum.', 'The x=50 extension completed for all ten characters; eigenvalues at several N quantify the remaining tail beyond the determinant minimum.')
report=report.replace('| planned files |','| completed files |')
report=report.replace('## D5. Extraction conventions (tables appended as runs finish)','## D5. Results and extraction conventions')
report=report.replace('both will appear in the table.','both appear in the table.')
validation=f'''\n**NUMERICAL D4 (final validation).** All 52 final files pass: {sum(counts)} driver checks, zero failed. The final unchanged-library `make -C zst check` passes all 12 test executables. `checks/audit_outputs.txt` records the independent structural/floating audit; `checks/bytecheck.txt` records three representative full outputs, each rerun byte-identically. The first-positive-Hardy-Z index is independently certified for all ten characters. The two development failures were corrected and replayed; they remain archived under checks. The initial suite log still records those historical failures, while every released file ends with zero failed checks.\n'''
if wall is not None:validation+=f'\nThe interval from creation of the first run file to completion of the last is approximately {wall:.1f} minutes, including the replays (filesystem timestamps, not embedded in raw outputs).\n'
a='<!-- D4_VALIDATION_BEGIN -->';b='<!-- D4_VALIDATION_END -->'
if a in report:report=report[:report.index(a)]+report[report.index(b)+len(b):]
report=report.replace('\n## D5.',a+'\n'+validation+b+'\n\n## D5.',1)
ledger=f'''\n5. **REFUTED numerically.** The raw-x rate is not character-independent: the 13–50 spread is {f(spread(core))} digits/x for the six required characters and {f(spread(Ds))} for all ten. Conductor changes the leading scale; it cannot be relegated to a multiplicative amplitude in an unscaled exp(-4pi x) law.
6. **SHARPENED.** The determinant argmin is not a precision criterion for eps. At x=50 the coefficient q N_sat/(x log x) ranges from {f(min(v for _,v in coeff))} to {f(max(v for _,v in coeff))}; a universal factor 1.7 is too crude, particularly when x/q is small. Finite-N tails and both block argmins are reported separately.
7. **PROVED correction to A1.1'(4).** The nonnegative structured log-determinant difference is the gain of MaxEnt over truth, not the gain of truth over MaxEnt.
8. **SHARPENED.** The prime-free Dirichlet control includes log q I and need not be indefinite. D=-20 is positive on every window by D2c. Odd global minima do occur in the fixed-L partial forms, so even-only diagnostics can be badly misleading.
'''
a='<!-- D_LEDGER_RUN_BEGIN -->';b='<!-- D_LEDGER_RUN_END -->'
if a in report:report=report[:report.index(a)]+report[report.index(b)+len(b):]
report=report.replace('\n## D1.',a+'\n'+ledger+b+'\n\n## D1.',1)
verdict=f'''
## D6. Verdict

**REFUTED numerically on the tested range: a character-independent exp(-4pi x) law.** For saturated finite-N proxies, the 13–50 even-minimum slopes range from {f(rates[lo])} (D={lo}) to {f(rates[hi])} (D={hi}) decimal digits per x, a spread of {f(spread(Ds))}; the six required characters alone have spread {f(spread(core))}. Zeta's corrected round-1 value is 5.37857. This difference is much larger than the residual resolution effects: increasing N from 260 to 420 at x=50 changes eps by factors between {f(min(tails))} and {f(max(tails))}. All complete CCM cases have certified even global minima; both block rates are tabulated. These statements are finite computations, not asymptotic theorems or GRH assumptions. All derived rates and fits in this section are **floating**.

**NUMERICAL support for the conductor-aware prediction D1a.** The simplest explanation consistent with the family is exp(-4pi x/q), multiplied by a character-dependent prefactor. A three-point fit `log eps=a+b log(x/q)-c x/q` gives c/(4pi) between {f(min(fits[D][2] for D in core))} and {f(max(fits[D][2] for D in core))} for the required six, and between {f(min(v[2] for v in fits.values()))} and {f(max(v[2] for v in fits.values()))} for all ten. Three points interpolate three parameters, so this is a consistency check, not a proved asymptotic law. The fitted normalized coefficients still differ: these data support the conductor scale, not an exactly common finite-window rate. The least asymptotic windows are x/q=13/20 and 13/21; the extra q=13 case also shows visible curvature beyond a simple power times exponential. These discrepancies are retained in the fit table.

**NUMERICAL parity and prefactor evidence.** At q=8, the 13–50 slopes are {f(s(8))} for kappa=0 and {f(s(-8))} for kappa=1, a difference {f(s(8)-s(-8))}. The fitted powers are {f(fits[8][1])} and {f(fits[-8][1])}. This is consistent with different lowest prolate sectors, not a new leading exponential determined by parity. The post-run heuristic b=1+kappa, motivated by the lowest-sector powers 1/2 and 3/2 plus an extra square-root normalization factor, puts the corrected quantities `q[s+(1+kappa) log10(50/13)/37]` in [{f(min(corrected.values()))}, {f(max(corrected.values()))}], around 4pi/log(10)={f(4*mp.pi/mp.log(10))}. This exact power was **not** preregistered in D1, and remains OPEN. The fitted b and c are strongly correlated, and the finite-N tail is not an infinite-N error bound; these fits do not establish a universal polynomial prefactor. The amplitudes A_fixed vary with the character; no formula for them is established. Zeta's h0/h4 pole-cancelling ansatz is a different sector (defect power 9/2); its reported eps/defect ratios 10.4,14.4,20.2 are themselves close to a square-root factor in x.

![Floating conductor-rate comparison; the power corrections are heuristic.](checks/conductor_rates.png)

[Standalone PDF figure](checks/conductor_rates.pdf).

**NUMERICAL comparison and controls.** The maximum difference between an eps slope and its first-zero-error slope over 13–50 is {f(errdiff)} digits/x. The error/eps ratio is character-dependent and changes slowly across these windows, as the certified COMPARISON table shows. Conductor explains the dominant variation; these data do not identify an independent law in the first-zero height. For example gamma_1(chi_5)>gamma_1(chi_-4), but chi_5 converges more slowly. The joint Schur half-widths across all final-N samples lie between {f(min(widths))} and {f(max(widths))}, and therefore do not exhibit the eigenvalue's exponential contraction. The Rayleigh tables certify the archimedean/prime cancellation in the actual minimizing block. In the fixed-L runs, every proper cutoff is indefinite until 49 enters; at X=47 the global minimum is odd for both D=-4 and D=5.

**SHARPENED interpretation of D1b and the notebook question.** The N_sat shift is downward with conductor on the predicted x log x/q scale, with substantial finite-window and parity corrections. At x=50, zeta has N_sat=352, chi_-4 has 80, chi_5 has 60, and chi_21 has 10. The claim that arithmetic sets only the floor while the same unscaled window sets a universal rate is not supported. A conductor-rescaled prolate mechanism is supported by these data and by twisted Poisson summation, but remains OPEN as a theorem about the Weil minimizer. The conductor and the prime comb are linked within this family; this experiment does not separately vary them. It therefore neither proves that detailed prime fluctuations set the exponential nor rules out a kinematic explanation after the conductor-dependent Fourier rescaling.

## Numerical checks for the blind lane

**NUMERICAL, certified rounded eigenvalues; the slope is floating.** Reproduce these independently from the named prime-side driver, without supplying reference zeros to the form:

| D | x | N | eps_E | eps_O | global minimum |
|---|---|---|---|---|---|
'''
for D,x in [(-4,13),(5,25),(-4,50)]:
    e=data[D,x][1];verdict+=f"| {D} | {x} | {e['N']} | {e['epsE']} | {e['epsO']} | even |\n"
verdict+=f'''
One saturation check: D=-4,x=50, N_sat(full/even/odd)=80/80/80, uniquely over 1..420; logdet=-1287.1115063921. One slope: D=-4,13–50 gives {f(s(-4),10)} digits/x from the N=200 and 420 values. One control inertia: D=-3,x=13,N=200,X=1 has (negative,zero,positive)=(1,0,200) in E and (1,0,199) in O; its minima are -0.738305349543 and -0.0885009571702.

Reproduction:

```sh
make -C zst build/rtp2_dirichlet
zst/tools/rtp2_dirichlet_run.sh
python3 notes/rtp-round-2/dirichlet/checks/first_zero_prefix.py
python3 notes/rtp-round-2/dirichlet/checks/audit_outputs.py
python3 notes/rtp-round-2/dirichlet/checks/summary.py
python3 notes/rtp-round-2/dirichlet/checks/plot_rates.py
```

`DS`, `PHASES=x13,x25,axisx,x50`, `JOBS` and `X50_ALL` restrict or parallelize a reproduction. The default suite uses all ten characters and all three windows. `--prec` remains 4200 at x=50, with eigenpair precision 2400; D=12,x=25 uses eigenpair precision 1400. The reference-generation program and its two-precision enclosures are in checks; the three missing character records were appended to the reference fixture under the brief's explicit exception. No git command was run and no library source/include behavior was changed.

## What this changes in the notebook

**SHARPENED `obs:rtp-round-1-reading`(iii), shard 08i.** Its statement that round 1 alone did not decide the rate's origin was correct. The proposed discriminating experiment now rejects a character-independent raw-x rate: the leading scale is consistent with x/|D|. Keep the distinction between the Schur envelope and the small-eigenvalue/zero-error channel. Replace any inference “same window implies the same exp(-4pi x) rate, arithmetic only the floor” by the conductor-aware numerical finding and the OPEN prolate explanation above.

**NUMERICAL / SHARPENED.** `lem:bordering-interval` is unchanged without poles (PROVED D2); the mechanisms underlying `num:rtp-dilation-channel` are extended numerically: the Schur half-width does not follow eps; the comparison error tracks eps; and N saturation is a Weyl-count effect. The coefficient 1.7 and a determinant argmin as an eigenvalue-convergence criterion require qualification. The fixed-window partial forms can have odd minima, and their prime-free control need not be indefinite. Round 1's zeta numerical statements remain intact; no zeta run or shard was changed here.

**One next experiment (OPEN).** Compare the characters at matched y=x/|D|, with N doubled until the measured tail is controlled, and test whether `eps/[y^(1+kappa) exp(-4pi y)]` stabilizes. Include the matched-conductor pair D=8,-8 and the larger-conductor cases whose present y is too small. This would distinguish a shared conductor-rescaled prolate exponent and parity power from residual character-dependent curvature, using zeros only in the labelled comparison.
'''
report+=verdict;p.write_text(report)
(P.parent/'progress.txt').write_text(f'''DONE D1: predictions recorded before runs; source prefactor checked; conductor-aware alternative tested.
DONE D2: pole-free bordering lemma and conductor/parity control comparisons proved.
DONE D3: driver and run script; independent minima, parity, intervals, certified reference roots and first-index checks.
DONE D4: 52 final files, {sum(counts)} checks, zero failed; all 12 library tests pass; three representative byte reproductions.
DONE D5: all tables, floating fits/slopes, controls, Rayleigh and Schur data, zeta comparison, plot and audit complete.
DONE D6: raw-x universality refuted numerically; conductor-scaled prolate interpretation supported but OPEN; blind checks and notebook implications written.
''')
manifest={'author':'codex:gpt-6-astra','files':{},'driver_checks':sum(counts),'driver_failures':0}
for pp in files+[ROOT/'zst/tools/rtp2_dirichlet.c',ROOT/'zst/tools/rtp2_dirichlet_run.sh',ROOT/'zst/tests/data/dirichlet_ref.txt',ROOT/'zst/build/libzst.a',ROOT/'zst/Makefile',P/'reference.c',P/'summary.py',P/'first_zero_prefix.py',P/'plot_rates.py']:
    manifest['files'][str(pp.relative_to(ROOT))]=hashlib.sha256(pp.read_bytes()).hexdigest()
(P/'manifest.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
print(f'Final report written: {sum(counts)} checks in 52 files; all passed.')
