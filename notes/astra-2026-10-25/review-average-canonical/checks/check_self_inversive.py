#!/usr/bin/env python3
"""Small integer/Gaussian-integer self-inversive search via an exact Cayley transform.
For even degrees the central coefficient is zero here; the full allowed central
range is covered separately in check_algebra.py.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import sympy as s
x,z=s.symbols('x z');count=Counter();lines=[]
for g in range(4,9):
 k=(g-1)//2
 for a0 in range(1,4):
  for tail in product(range(a0+1),repeat=k):
   p=(a0,)+tail
   if any(p[j]<p[j+1] for j in range(k)):continue
   for phase,scale in [(1,1),(-1,-s.I),(s.I,1-s.I),(-s.I,1+s.I)]:
    b=[s.Integer(0)]*(g+1)
    for j,v in enumerate(p):b[j]+=v;b[g-j]+=phase*v
    C=s.Poly(s.expand(scale*sum(b[j]*(x+s.I)**j*(x-s.I)**(g-j) for j in range(g+1))),x,domain=s.QQ)
    nr=sum(mult*factor.count_roots(-s.oo,s.oo) for factor,mult in C.sqf_list()[1])
    assert nr==C.degree(),(g,p,phase,C)
    count[g,str(phase)]+=1
for key,n in sorted(count.items()):lines.append(f'degree,phase={key} cases={n} off_circle=0')
lines.append(f'TOTAL self-inversive cases={sum(count.values())}; Cayley polynomials all real-rooted exactly; missing degree counts z=1 roots.')
print('\n'.join(lines));Path(__file__).with_name('output_self_inversive.txt').write_text('\n'.join(lines)+'\n')
