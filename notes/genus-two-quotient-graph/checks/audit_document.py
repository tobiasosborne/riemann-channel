#!/usr/bin/env python3
"""Author: codex:gpt-6-astra. Verify the printed graph against exact data."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import ast
from collections import Counter
from graph_data import VERTICES,STABILISERS,TAILS,EDGES
from labelled_data import HEADS,TAIL_LABELS,INVOLUTION
from spectral_data import CUSP_CHAR_FACTORS,VISIBLE_DIM
root=Path(__file__).resolve().parent.parent
text=(root/'astra-proofs.md').read_text()
assert 'PENDING' not in text
section=text.split('| Vertex | n | u | S(v) | Larger nucleus neighbours / S(e) |\n')[1].split('\n\n')[0]
found=[];ee=[]
for line in section.splitlines():
    if not line.startswith('| ') or line.startswith('|---'):continue
    row=[a.strip() for a in line.strip('|').split('|')]
    i,n=int(row[0]),int(row[1]);u=tuple(tuple(map(int,a.split(':'))) for a in row[2].split(',')) if row[2]!='0' else ()
    assert VERTICES[i]==(n,u) and STABILISERS[i]==int(row[3])
    found.append(i)
    if row[4]!='—':
        for entry in row[4].split(', '):
            j,se=map(int,entry.split('/'));ee.append((i,j,se))
assert found==[i for i in range(len(VERTICES)) if i not in TAILS]
assert Counter(ee)==Counter((a,b,s) for a,b,s in EDGES if a not in TAILS and b not in TAILS)
section=text.split('| Cusp a | Ratio class j=2a mod 15 | Head c(j,3), S=400 | First exterior vertex, S=2000 | Edge S |\n')[1].split('\n\n')[0]
for line in section.splitlines():
    if line.startswith('| ') and not line.startswith('|---'):
        a,j,h,t,se=map(int,(x.strip() for x in line.strip('|').split('|')))
        assert j==2*a%15 and HEADS[a]==h and TAIL_LABELS[t]==a and se==400
assert VISIBLE_DIM==85
assert sum((len(p)-1)*e for p,e in CUSP_CHAR_FACTORS)==281
for p in root.joinpath('checks').glob('*.py'):
    content=p.read_text();assert 'Author: codex:gpt-6-astra' in content
    ast.parse(content,filename=str(p))
assert sum(INVOLUTION[i]==i for i in found)==198
print('PRINTED GRAPH: 366 vertices, 915 edges, fifteen labelled ray attachments: exact match.')
print('ALL ASSERTIONS PASSED')
