#!/usr/bin/env python3
"""COMPARISON ONLY, author codex:gpt-6-astra.
Generate missing reference first zeros using reference.c's Hardy-Z isolation.
Two precisions must overlap. Append 40-digit guesses in the legacy format only
when --append is specified; retain rigorous root balls separately under checks/.
The index 'first' is from a 1/16 sign scan, not a global zero-count certificate.
"""
from pathlib import Path
import re,subprocess,sys
import mpmath as mp
ROOT=Path(__file__).resolve().parents[4]
CHECKS=Path(__file__).resolve().parent
subprocess.run(['cc','-O2','-std=c11','-DREF_MAIN',str(CHECKS/'reference.c'),'-lflint','-lmpfr','-lgmp','-lm','-o',str(CHECKS/'reference')],check=True)
mp.mp.dps=350
ref=ROOT/'zst/tests/data/dirichlet_ref.txt'
old=ref.read_text(); additions=[]
for D in [-7,-20,21]:
    balls=[]
    for prec in [800,1200]:
        s=subprocess.check_output([str(CHECKS/'reference'),str(D),str(prec)],cwd=ROOT,text=True)
        (CHECKS/f'reference_D{D}_p{prec}.txt').write_text(s)
        m=re.search(r'zero 1 \[([^ ]+) \+/- ([^]]+)\]',s)
        assert m, s
        balls.append(tuple(map(mp.mpf,m.groups())))
    (a,r),(b,t)=balls
    assert abs(a-b)<=r+t, f'D={D}: enclosures disagree'
    guess=mp.nstr(b,40)
    additions.append(f'chi {D} {abs(D)} {int(D<0)}\nzero 1 {guess}\nend\n')
    print(f'D={D}: two certified root enclosures overlap; first-index scan; seed={guess}')
if '--append' in sys.argv:
    new=''
    for D,block in zip([-7,-20,21],additions):
        if not re.search(rf'^chi {D} ',old,re.M):new+=block
    if new:
        with ref.open('a') as f:
            f.write('\n# RTP-2 COMPARISON seeds: checks/generate_references.py, FLINT Hardy Z, 2026-09-26.\n# 40-digit midpoints; certified enclosures and two-precision checks retained in lane checks/.\n# First-index identification from sign scan (not a certified global zero count).\n'+new)
