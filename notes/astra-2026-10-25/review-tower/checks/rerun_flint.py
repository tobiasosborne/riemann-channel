#!/usr/bin/env python3
"""Run the five unchanged lane-T checks; write only in this review directory."""
from pathlib import Path
import concurrent.futures, difflib, hashlib, os, subprocess, sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SRC=ROOT/'notes/astra-2026-10-23/tower/checks'
CASES=[('tower_audit','audit'),('tower_strict','strict'),('replay_tower_flint','tower_flint'),('replay_cm_flint','cm_flint'),('audit_overlap_refinement','overlap_refinement')]
def run(case):
    script,name=case
    out=HERE/f'output_rerun_{name}.txt'
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
    with out.open('w') as f:
        p=subprocess.run([sys.executable,str(SRC/f'{script}.py')],stdout=f,stderr=subprocess.STDOUT,env=env)
    old=(SRC/f'output_{name}.txt').read_text().splitlines()
    new=out.read_text().splitlines()
    # Only reported elapsed seconds are nondeterministic.
    import re
    norm=lambda ls:[re.sub(r'\(\d+\.\d+ s\)', '(TIME s)',s) for s in ls]
    delta=list(difflib.unified_diff(norm(old),norm(new),fromfile='saved',tofile='rerun',lineterm=''))
    (HERE/f'diff_{name}.txt').write_text('\n'.join(delta)+'\n')
    return f'{script}: exit={p.returncode}, saved_lines={len(old)}, rerun_lines={len(new)}, exact_except_elapsed={not delta}, sha256={hashlib.sha256((SRC/f"{script}.py").read_bytes()).hexdigest()}'
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
    for row in ex.map(run,CASES): print(row,flush=True)
