#!/usr/bin/env bash
# Author codex:gpt-6-astra. Regenerate the RTP-2 lane-D suite; no timings on stdout.
# Usage: zst/tools/rtp2_dirichlet_run.sh [output-directory]
# JOBS=12 by default. DS may override the character list for a reproduction subset.
# X50_ALL=1 includes every character at x=50 (set 0 for just -4 and 5).
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
out="${1:-$here/../outputs}"
checks="$here/../notes/rtp-round-2/dirichlet/checks"
mkdir -p "$out" "$checks/runlogs"
make -C "$here" build/rtp2_dirichlet >/dev/null
export RTP2_BIN="$here/build/rtp2_dirichlet" RTP2_OUT="$out" RTP2_CHECKS="$checks"
cd "$here/.."
python3 - <<'PY'
import concurrent.futures, os, subprocess, sys
from pathlib import Path
Ds=list(map(int,os.environ.get('DS','-4 -3 5 8 -7 12 -20 21 13 -8').split()))
B=os.environ['RTP2_BIN'];out=Path(os.environ['RTP2_OUT']);logs=Path(os.environ['RTP2_CHECKS'])/'runlogs'
jobs=int(os.environ.get('JOBS','12'))
def run(task):
    name,args=task
    with (out/f'rtp2_dirichlet_{name}.txt').open('w') as f, (logs/f'{name}.log').open('w') as err:
        r=subprocess.run([B,*map(str,args)],stdout=f,stderr=err)
    print(f'{name}: exit={r.returncode}',flush=True)
    return r.returncode
stages=[]
for x,m,p,cp,cmp in [(13,200,1000,700,'20,40,80,120'),(25,260,1800,1200,'40,80,120,180')]:
    stages.append([(f'D{D}_axisN_x{x}',['--D',D,'--mode','axisN','--x',x,'--Nmax',m,'--prec',p,'--cprec',cp,'--cmp',cmp]) for D in Ds])
stages.append([(f'D{D}_axisx_ccm_N{N}',['--D',D,'--mode','axisx','--N',N,'--xmax',xm,'--prec',p]) for D in Ds for N,xm,p in [(60,50,2700),(120,25,1800)] ]+
 [(f'D{D}_axisx_fixedL_N60',['--D',D,'--mode','axisx','--N',60,'--xmax',50,'--prec',2700,'--fixedL',1]) for D in [-4,5] if D in Ds])
large=Ds if os.environ.get('X50_ALL','1')=='1' else [D for D in [-4,5] if D in Ds]
stages.append([(f'D{D}_axisN_x50',['--D',D,'--mode','axisN','--x',50,'--Nmax',420,'--prec',4200,'--cprec',2400,'--cmp','80,160,260']) for D in large])
failed=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as pool:
    for stage in stages:
        for task,rc in zip(stage,pool.map(run,stage)):
            if rc: failed.append(task[0])
if failed: print('FAILED: '+', '.join(failed),file=sys.stderr)
sys.exit(bool(failed))
PY
