#!/usr/bin/env python3
"""Record reproducibility and compare independently enumerated groups with all saved product cells."""
from pathlib import Path
import hashlib,json,re
here=Path(__file__).resolve().parent;src=here.parents[1]/'fable/checks'
for name in ('pizer_graph','pizer_quotient','label_lattice'):
 original=(src/(name+'.py')).read_bytes();copy=(here/'rerun'/(name+'.py')).read_bytes()
 output=(here/'rerun'/((('stdout_' if name=='pizer_quotient' else 'output_')+name)+'.txt')).read_bytes()
 saved=(src/('output_'+name+'.txt')).read_bytes()
 assert original==copy and output==saved
 print(name,'source byte-identical:',original==copy,'saved output byte-identical:',output==saved,'source SHA256',hashlib.sha256(original).hexdigest())
data=json.loads((here/'arithmetic_data.json').read_text());p=l=None;count=0
for line in (src/'output_label_lattice.txt').read_text().splitlines():
 m=re.search(r'==== p = (\d+)',line)
 if m:p=int(m[1])
 m=re.search(r'-- l = (\d+)',line)
 if m:l=int(m[1])
 m=re.search(r'k = (\d+):.*E1 x E2 as SNF = (\[.*?\])',line)
 if m and p==37:
  k=int(m[1]);expected=json.loads(m[2]);actual=data[f'{l},{k}']['product'];assert actual==expected
  print('independent elliptic product matches saved',l,k,actual);count+=1
assert count==16
out=(here/'output_independent_matrices.txt').read_text()
assert out.count('SNF p,ell,k')==48 and out.count('Hashimoto p,ell')==12 and out.count('P1 p,ell')==20
assert 'Traceback' not in out
for name in ['independent_arithmetic','independent_theta']:
 assert 'Traceback' not in (here/('output_'+name+'.txt')).read_text()
print('Counts: 20 Brandt/Hecke checks; 12 independent Hashimoto polynomials; 48 independent Smith forms; 16 independently enumerated elliptic products.')
