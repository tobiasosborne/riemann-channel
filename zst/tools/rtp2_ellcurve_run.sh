#!/usr/bin/env bash
# Author codex:gpt-6-astra. Reproduce lane E; no reference zeros in forms.
# JOBS=12; CURVES='11a1 14a1 37a1'; PHASES='axisN,axisx,long,spectra'.
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
out="${1:-$here/../outputs}"
checks="$here/../notes/rtp-round-2/ellcurve/checks"
mkdir -p "$out" "$checks/runlogs"
make -C "$here" build/rtp2_ellcurve
export RTP2_E_BIN="$here/build/rtp2_ellcurve" RTP2_E_OUT="$out" RTP2_E_CHECKS="$checks"
cd "$here/.."
python3 - <<'PY'
import concurrent.futures, os, subprocess, sys, time
from pathlib import Path
curves=os.environ.get('CURVES','11a1 14a1 37a1').split()
phases=os.environ.get('PHASES','axisN,axisx,long,spectra').split(',')
B=os.environ['RTP2_E_BIN'];out=Path(os.environ['RTP2_E_OUT']);logs=Path(os.environ['RTP2_E_CHECKS'])/'runlogs'
tasks=[]
if 'axisN' in phases:
    for x,m,p,cp in [(13,200,1000,700),(25,260,1800,1200),(50,420,4200,2400)]:
        for c in curves:
            tasks.append((f'{c}_axisN_x{x}',['--curve',c,'--x',x,'--Nmax',m,'--prec',p,'--cprec',cp,'--cmp','20,40,60,120,200']))
if 'axisx' in phases:
    for c in curves:
        for n,xm,p in [(60,50,2700),(120,25,1800)]:
            tasks.append((f'{c}_axisx_ccm_N{n}',['--curve',c,'--mode','axisx','--N',n,'--xmax',xm,'--prec',p]))
if 'long' in phases and '11a1' in curves:
    tasks.append(('11a1_axisx_ccm_N200',['--curve','11a1','--mode','axisx','--N',200,'--xmax',100,'--prec',2700]))
    tasks.append(('11a1_axisN_x100',['--curve','11a1','--x',100,'--Nmax',420,'--prec',2700,'--cprec',1800,'--cmp','60,120,200']))
if 'spectra' in phases:
    for c in [c for c in curves if c!='37a1']:
        for x in [13,25,50]:
            tasks.append((f'{c}_spectra_x{x}',['--curve',c,'--mode','spectra','--x',x,'--N',60]))
def run(task):
    name,args=task;t=time.monotonic()
    with (out/f'rtp2_ellcurve_{name}.txt').open('w') as f,(logs/f'{name}.log').open('w') as e:
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
if failed: print('FAILED: '+', '.join(failed),file=sys.stderr)
sys.exit(bool(failed))
PY
