#!/usr/bin/env bash
# Author claude:opus, 2026-09-26. RTP-2 follow-up to lane E: the conductor exponent alpha.
# Runs the lane-E driver (tools/rtp2_ellcurve.c, unchanged protocol) in the axis-x CCM mode on rank-zero
# curves read from notes/rtp-round-2/ellcurve-conductors/ell_ref_ext.txt (--ref), with --compare 0:
# the COMPARISON STEP is skipped, no zero of any L-function is read or used. Outputs have no timestamps
# (timings go to the run logs only) and are byte-reproducible.
# Env: CURVES (default: the 19 curves below), PHASES='n60,n120,matchz', JOBS=24, RESUME=1 reuses completed files.
# matchz: the same protocol on the matched phase-space window z = sqrt(x/C) in [sqrt(13/11), sqrt(50/11)], i.e.
# xmax = round(50 C/11) capped at 250 (the driver's limit); knots below 13 C/11 are computed but not used in the fit.
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
out="${1:-$here/../outputs}"
lane="$here/../notes/rtp-round-2/ellcurve-conductors"
mkdir -p "$out" "$lane/checks/runlogs"
make -C "$here" build/rtp2_ellcurve
export RC_BIN="$here/build/rtp2_ellcurve" RC_OUT="$out" RC_LOGS="$lane/checks/runlogs" RC_REF="$lane/ell_ref_ext.txt"
cd "$here/.."
python3 - <<'PY'
import concurrent.futures, os, re, subprocess, sys, time
from pathlib import Path
curves=os.environ.get('CURVES','11a1 14a1 15a1 17a1 19a1 20a1 21a1 24a1 26a1 27a1 30a1 32a1 33a1 34a1 35a1 36a1 50a1 67a1 109a1').split()
phases=os.environ.get('PHASES','n60,n120,matchz').split(',')
B=os.environ['RC_BIN'];out=Path(os.environ['RC_OUT']);logs=Path(os.environ['RC_LOGS']);ref=os.environ['RC_REF']
tasks=[]
if 'n120' in phases:   # saturation check on four conductors (started first: the longest jobs)
    for c in [c for c in ['11a1','17a1','26a1','36a1'] if c in curves]:
        tasks.append((f'{c}_axisx_ccm_N120',['--curve',c,'--ref',ref,'--compare',0,'--mode','axisx','--N',120,'--xmax',50,'--prec',3200]))
if 'n60' in phases:    # the lane-E axis-x protocol: N = 60, knots = prime powers <= 50 and x = 50, 2700 bits
    for c in curves:
        tasks.append((f'{c}_axisx_ccm_N60',['--curve',c,'--ref',ref,'--compare',0,'--mode','axisx','--N',60,'--xmax',50,'--prec',2700]))
if 'matchz' in phases:
    for c in curves:
        C=int(re.match(r'\d+',c).group()); xm=min(250,round(50*C/11))
        if xm>50: tasks.append((f'{c}_axisx_ccm_N60_matchz',['--curve',c,'--ref',ref,'--compare',0,'--mode','axisx','--N',60,'--xmax',xm,'--prec',2700]))
if 'satpts' in phases:
    for c in [c for c in ['11a1','20a1','27a1','36a1','50a1','67a1'] if c in curves]:
        C=int(re.match(r'\d+',c).group()); xm=min(250,round(50*C/11))
        for n in (120,200):
            tasks.append((f'{c}_point_x{xm}_N{n}',['--curve',c,'--ref',ref,'--compare',0,'--mode','point','--N',n,'--xmax',xm,'--prec',2000,'--control-cap',120]))
def run(task):
    name,args=task;t=time.monotonic();target=out/f'rtp2_ellconductors_{name}.txt'
    if os.environ.get('RESUME','0')=='1' and target.exists() and re.search(r'# checks: \d+ run, 0 failed',target.read_text()):
        print(f'{name}: completed, reused',flush=True);return 0
    with target.open('w') as f,(logs/f'{name}.log').open('w') as e:
        try: rc=subprocess.run([B,*map(str,args)],stdout=f,stderr=e,timeout=7200).returncode
        except subprocess.TimeoutExpired: rc=124
        e.write(f'wall_seconds={time.monotonic()-t:.3f}\n')
    print(f'{name}: exit={rc} wall={time.monotonic()-t:.1f}s',flush=True);return rc
with concurrent.futures.ThreadPoolExecutor(max_workers=int(os.environ.get('JOBS','24'))) as pool:
    results=list(pool.map(run,tasks))
failed=[t[0] for t,rc in zip(tasks,results) if rc]
if failed: print('FAILED: '+', '.join(failed),file=sys.stderr)
sys.exit(bool(failed))
PY
