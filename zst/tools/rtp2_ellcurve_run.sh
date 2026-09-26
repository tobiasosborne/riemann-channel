#!/usr/bin/env bash
# Author codex:gpt-6-astra. Reproduce lane E; no reference zeros in forms.
# RESUME=1 skips completed files. JOBS=12; CURVES='11a1 14a1 37a1'; PHASES='axisN,axisx,long,spectra'.
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
out="${1:-$here/../outputs}"
checks="$here/../notes/rtp-round-2/ellcurve/checks"
mkdir -p "$out" "$checks/runlogs"
make -C "$here" build/rtp2_ellcurve
export RTP2_E_BIN="$here/build/rtp2_ellcurve" RTP2_E_OUT="$out" RTP2_E_CHECKS="$checks"
cd "$here/.."
python3 - <<'PY'
import concurrent.futures, os, subprocess, sys, time, re
from pathlib import Path
curves=os.environ.get('CURVES','11a1 14a1 37a1').split()
phases=os.environ.get('PHASES','axisN,axisx,long,spectra').split(',')
B=os.environ['RTP2_E_BIN'];out=Path(os.environ['RTP2_E_OUT']);logs=Path(os.environ['RTP2_E_CHECKS'])/'runlogs'
tasks=[]
if 'axisN' in phases:
    for x,m,p,cp in [(13,200,1000,700),(25,260,1800,1200),(50,420,1000,700)]:
        for c in curves:
            tasks.append((f'{c}_axisN_x{x}',['--curve',c,'--x',x,'--Nmax',m,'--prec',p,'--cprec',cp,'--cmp','20,40,60,120,200','--control-cap',(120 if x==50 else 0)]))
if 'axisN' in phases and '37a1' in curves:
    tasks.append(('389a1_record',['--curve','389a1','--mode','point','--N',60,'--xmax',13,'--prec',700]))
if 'axisx' in phases:
    for c in curves:
        for n,xm,p in [(60,50,2700),(120,25,1800)]:
            tasks.append((f'{c}_axisx_ccm_N{n}',['--curve',c,'--mode','axisx','--N',n,'--xmax',xm,'--prec',p]))
if 'long' in phases and '11a1' in curves:
    def prime_power(n):
        for p in range(2,n+1):
            if any(p%d==0 for d in range(2,int(p**.5)+1)):continue
            k=p
            while k<n:k*=p
            if k==n:return True
        return False
    long_knots=[x for x in range(2,101) if prime_power(x) or x==100]
    for x in long_knots:
        tasks.append((f'point_11a1_N200_x{x}',['--curve','11a1','--mode','point','--N',200,'--xmax',x,'--prec',1000,'--control-cap',120]))
    tasks.append(('11a1_axisN_x100',['--curve','11a1','--x',100,'--Nmax',420,'--prec',1400,'--cprec',1000,'--cmp','60,120,200','--control-cap',120]))
if 'spectra' in phases:
    for c in [c for c in curves if c!='37a1']:
        for x in [13,25,50]:
            tasks.append((f'{c}_spectra_x{x}',['--curve',c,'--mode','spectra','--x',x,'--N',60]))
def run(task):
    name,args=task;t=time.monotonic()
    target=(logs.parent/'points'/f'{name}.txt') if name.startswith('point_') else (out/f'rtp2_ellcurve_{name}.txt')
    target.parent.mkdir(parents=True,exist_ok=True)
    if os.environ.get('RESUME','0')=='1' and target.exists() and re.search(r'# checks: \d+ run, 0 failed',target.read_text()):
        print(f'{name}: completed, reused',flush=True);return 0
    with target.open('w') as f,(logs/f'{name}.log').open('w') as e:
        try:
            r=subprocess.run([B,*map(str,args)],stdout=f,stderr=e,timeout=4500)
            rc=r.returncode
        except subprocess.TimeoutExpired: rc=124
        e.write(f'wall_seconds={time.monotonic()-t:.3f}\n')
    print(f'{name}: exit={rc} wall={time.monotonic()-t:.1f}s',flush=True)
    return rc
with concurrent.futures.ThreadPoolExecutor(max_workers=int(os.environ.get('JOBS','12'))) as pool:
    results=list(pool.map(run,tasks))
failed=[task[0] for task,rc in zip(tasks,results) if rc]
if 'long' in phases and '11a1' in curves and not any(n.startswith('point_') for n in failed):
    # The same fixed N and CCM form at independent windows. Coefficient overlaps
    # are not retained across processes; do not label within-point overlap=1 as one.
    dest=out/'rtp2_ellcurve_11a1_axisx_ccm_N200.txt';total=0
    with dest.open('w') as f:
        f.write('# rtp2_ellcurve parallel CCM axis x; N=200; prec=1000; independent window points\n')
        f.write('# No cross-window overlap is computed. Controls are in the axisN and spectra files.\n')
        for x in long_knots:
            text=(logs.parent/'points'/f'point_11a1_N200_x{x}.txt').read_text()
            m=re.search(r'# checks: (\d+) run, (\d+) failed',text)
            if not m or int(m[2]):raise RuntimeError(f'incomplete point x={x}')
            total+=int(m[1]);f.write(f'# POINT x={x}\n')
            for line in text.splitlines():
                if line.startswith(('EIG ','KNOT ')):f.write(line+'\n')
                if x==100 and line.startswith(('RAY ','RAY_TOTAL ')):f.write(line+'\n')
        f.write('# COMPARISON STEP: approximate PARI references used only below\n')
        for x in long_knots:
            for line in (logs.parent/'points'/f'point_11a1_N200_x{x}.txt').read_text().splitlines():
                if line.startswith(('REFERENCE ','COMP ')):f.write(line+'\n')
        f.write(f'# checks: {total} run, 0 failed\n')
if failed: print('FAILED: '+', '.join(failed),file=sys.stderr)
sys.exit(bool(failed))
PY
