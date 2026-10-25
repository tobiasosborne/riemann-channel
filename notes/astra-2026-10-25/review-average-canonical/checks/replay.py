#!/usr/bin/env python3
"""Replay unchanged input scripts from local copies, never write to input lanes."""
from pathlib import Path
import subprocess, concurrent.futures, os, time
H=Path(__file__).resolve().parent
os.environ['PYTHONDONTWRITEBYTECODE']='1'
os.environ['OPENBLAS_NUM_THREADS']='1'
def run(lane,script,out):
    p=H/('replay_'+lane); t=time.monotonic()
    with (p/('stdout_'+script+'.txt')).open('w') as f:
        r=subprocess.run(['python3','-B',str(p/(script+'.py'))],stdout=f,stderr=subprocess.STDOUT)
    if out: (p/out).write_bytes((p/('stdout_'+script+'.txt')).read_bytes())
    s=f'{lane}/{script}: exit={r.returncode} seconds={time.monotonic()-t:.1f}'
    print(s,flush=True)
    return s
def average():
    return [run('average',s,None) for s in ['avg_hyperelliptic','avg_cubic','avg_level','audit_identities','avg_extended','summarize_outputs']]
def characters():
    return [run('canonical','check_ff_all','output_ff_summary.txt'),run('canonical','check_ff_examples','output_ff_examples.txt')]
def graph():return [run('canonical','check_graph','output_graph.txt')]
def zeta():
    return [run('canonical','check_zeta','output_zeta.txt'),run('canonical','check_zeta_gaussian','output_zeta_gaussian.txt')]
if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        rows=list(pool.map(lambda f:f(),[average,characters,graph,zeta]))
    (H/'output_replay.txt').write_text('\n'.join(s for row in rows for s in row)+'\n')
