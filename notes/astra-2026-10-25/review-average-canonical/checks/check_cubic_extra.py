#!/usr/bin/env python3
"""Independent full cubic Dirichlet sums for all requested cover cells.
No FE, no Euler factors; direct residue norms for each coefficient and curve product.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
from flint import nmod_poly
import sympy as s
H=Path(__file__).resolve().parent;lines=[]
def emit(*a):v=' '.join(map(str,a));print(v,flush=True);lines.append(v);(H/'output_cubic_extra.txt').write_text('\n'.join(lines)+'\n')
for q in [7,13]:
 gen=next(g for g in range(2,q) if len({pow(g,j,q) for j in range(q-1)})==q-1)
 table=[(0,0)]*q
 for j in range(q-1):table[pow(gen,j,q)]=[(1,0),(0,1),(-1,-1)][j%3]
 mon=[[nmod_poly(list(c)+( [1]),q) for c in product(range(q),repeat=n)] for n in range(5)]
 for d in range(1,5):
  raw=[[0,0] for _ in range(d)];cd=d-int(d%3==0);whole=[0]*(2*cd-1);comp=[[0,0] for _ in range(cd)];count=0
  for D in mon[d]:
   if D.gcd(D.derivative()).degree()!=0:continue
   co=[]
   for n in range(d):
    a=b=0
    for f in mon[n]:
     v=table[int(D.resultant(f))];a+=v[0];b+=v[1]
    co.append((a,b));raw[n][0]+=a;raw[n][1]+=b
   if d%3==0:
    assert sum(a for a,b in co)==sum(b for a,b in co)==0
    co=[(sum(a for a,b in co[:n+1]),sum(b for a,b in co[:n+1])) for n in range(cd)]
   for n,(a,b) in enumerate(co):comp[n][0]+=a;comp[n][1]+=b
   for i,(a,b) in enumerate(co):
    for j,(c,e) in enumerate(co):whole[i+j]+=a*(c-e)+b*e
   count+=1
  assert all(b==0 for a,b in raw+comp)
  raw=[F(a,count) for a,b in raw];comp=[F(a,count) for a,b in comp];whole=[F(a,count) for a in whole]
  emit('q=',q,'d=',d,'H=',count,'raw=',raw,'completed=',comp,'whole=',whole)
  if d==3:assert comp==[1,1] and whole==[1,2,q]
  if d==4:assert comp==[1,0,0,q] and whole==[1,0,q-1+F(1,q),2*q,q*q-q+1,0,q**3]
  g=(len(whole)-1)//2
  if g:
   x=s.symbols('x');S=[s.Integer(2),x]
   for k in range(2,g+1):S.append(s.expand(x*S[-1]-q*S[-2]))
   R=s.Poly(s.Rational(whole[g])+sum(s.Rational(whole[i])*S[g-i] for i in range(g)),x)
   # Independent exact real-root intervals, used only for whole curves, not isotypic factors.
   iv=R.intervals(eps=s.Rational(1,10**12));assert sum(m for _,m in iv)==g and all(max(a*a,b*b)<4*q for (a,b),m in iv)
   emit('whole curve band certificate R=',R.as_expr(),'PASS')
emit('ALL direct cubic sums and whole-curve certificates PASS')
