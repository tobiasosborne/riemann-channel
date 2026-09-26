#!/usr/bin/env python3
"""Author codex:gpt-6-astra. COMPARISON ONLY: certify each first positive Hardy-Z index.
Interval exclusion before the root neighborhood, derivative exclusion inside it.
This is a critical-line zero certificate; it makes no assumption about off-line zeros.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess
P=Path(__file__).resolve().parent
ROOT=P.parents[3]
subprocess.run(['cc','-O2','-std=c11','-DREF_MAIN',str(P/'reference.c'),'-lflint','-lmpfr','-lgmp','-lm','-o',str(P/'reference')],check=True)
def run(D):
    r=subprocess.run([str(P/'reference'),str(D),'800','prefix'],capture_output=True,text=True,cwd=ROOT)
    (P/f'reference_prefix_D{D}.txt').write_text(r.stdout+r.stderr)
    return D,r.returncode
with ThreadPoolExecutor(max_workers=10) as pool:
    results=list(pool.map(run,[-4,-3,5,8,-7,12,-20,21,13,-8]))
for D,rc in results:print(f'D={D}: first positive Hardy-Z certificate '+('PASS' if rc==0 else 'FAIL'))
assert all(rc==0 for D,rc in results)
