#!/usr/bin/env python3
"""Direct norm/resultant character sums, orthogonality solves, exact level characters."""
from pathlib import Path
from itertools import product
from math import gcd
from collections import defaultdict
import sympy as s
from flint import nmod_poly
H=Path(__file__).resolve().parent;lines=[];x,Z,u=s.symbols('x Z u')
def emit(*a):v=' '.join(map(str,a));lines.append(v);print(v,flush=True)
def monics(q,n):return [tuple(c)+(1,) for c in product(range(q),repeat=n)]
def resultant(f,a,q):
 # Integral Sylvester determinant, reduced only at the end.
 return int(s.resultant(sum(v*x**i for i,v in enumerate(f)),sum(v*x**i for i,v in enumerate(a)),x))%q
def alphas(co,q):
 d=len(co)-1;c={0:s.Integer(d)}
 log=s.series(-u*s.diff(sum(v*u**i for i,v in enumerate(co)),u)/sum(v*u**i for i,v in enumerate(co)),u,0,d+1).removeO().expand()
 for k in range(1,d+1):c[k]=s.simplify(log.coeff(u,k)/s.sqrt(q)**k);c[-k]=s.conjugate(c[k])
 out=[]
 for degree in range(1,d+1):
  T=s.Matrix(degree,degree,lambda k,j:c[j-k]);rhs=s.Matrix([-c[degree-k] for k in range(degree)])
  b=T.inv()*rhs;a=s.simplify(-s.conjugate(b[0]));out.append(a)
  if s.simplify(a*s.conjugate(a))==1:break
 return c,out
for f,conj,even in [((1,1,0,1),False,False),((1,0,0,0,1),True,True)]:
 vals={0:0,1:1,2:s.I,4:-1,3:-s.I}
 if conj:vals={k:s.conjugate(v) for k,v in vals.items()}
 raw=[s.expand(sum(vals[resultant(f,a,5)] for a in monics(5,n))) for n in range(len(f)-1)]
 co=[s.expand(sum(raw[:n+1])) for n in range(len(raw)-1)] if even else raw
 c,aa=alphas(co,5)
 emit('q=5 f=',f,'raw=',raw,'completed=',co,'moments=',c,'alpha=',aa,'first_norm2=',s.simplify(aa[0]*s.conjugate(aa[0])))
 if even:assert s.expand(co[1]**2-4*co[2])==0
 else:assert co==[1,-2+s.I,3-4*s.I] and s.simplify(aa[0]*s.conjugate(aa[0]))==s.Rational(1,4)
# Quadratic counterexamples: independent full sums, even high coefficients direct.
q=3
for f in [(0,2,1,2,1,1),(1,0,0,0,2,1),(0,2,0,0,0,1),(0,2,1,1,2,1)]:
 fp=nmod_poly(list(f),q);assert fp.gcd(fp.derivative()).degree()==0
 def chi(a):v=int(fp.resultant(nmod_poly(list(a),q)));return (0,1,-1)[v]
 raw=[sum(chi(a) for a in monics(q,n)) for n in range(5)];c,aa=alphas(raw,q)
 prime2=sum(chi(a) for a in monics(q,2) if nmod_poly(list(a),q).factor()[1]==[(nmod_poly(list(a),q),1)])
 sf2=sum(chi(a) for a in monics(q,2) if (lambda p:p.gcd(p.derivative()).degree()==0)(nmod_poly(list(a),q)))
 sq=sum(chi(a)**2 for a in monics(q,1))
 emit('quadratic f=',f,'L=',raw,'prime sums=',(raw[1],prime2),'squarefree=',(raw[1],sf2),'linear_square_sum=',sq,'W=',s.Rational(raw[-1],9),'alpha=',aa)
# Fq^2 explicit pair multiplication; evaluate every nontrivial character, then group by order.
for q,r in [(3,1),(5,2)]:
 Q=q*q;M=Q-1
 def mul(a,b):return ((a[0]*b[0]-r*a[1]*b[1])%q,(a[0]*b[1]+a[1]*b[0])%q)
 for gen in product(range(q),repeat=2):
  logs={};v=(1,0)
  while v not in logs and v!=(0,0):logs[v]=len(logs);v=mul(v,gen)
  if len(logs)==M:break
 cycl=s.Poly(s.cyclotomic_poly(M,Z),Z)
 def red(p):return s.rem(p,cycl.as_expr(),Z).expand()
 rows=defaultdict(list);rawsum=0;compsum=0
 for j in range(1,M):
  a1=red(sum(Z**((j*logs[(a,1)])%M) for a in range(q)))
  even=j%(q-1)==0;raw=1+a1*u;comp=1 if even else raw
  if even:assert a1==-1
  rows[M//gcd(M,j)].append((raw,comp));rawsum+=raw;compsum+=comp
 emit('level q=',q,'f=x^2+',r,'generator=',gen,'raw_sum=',s.expand(rawsum),'completed_sum=',s.expand(compsum))
 for N,vals in sorted(rows.items()):
  avg=s.expand(s.Rational(1,len(vals))*sum(a for a,b in vals));comp=s.expand(s.Rational(1,len(vals))*sum(b for a,b in vals))
  ram=sum(sum(k*s.mobius(N//k) for k in s.divisors(gcd(N,logs[(a,1)]))) for a in range(q))
  assert s.simplify(avg-(1+s.Rational(ram,int(s.totient(N)))*u))==0
  emit('order=',N,'count=',len(vals),'raw_average=',avg,'completed_average=',comp,'Ramanujan PASS')
(H/'output_characters_independent.txt').write_text('\n'.join(lines)+'\n')
