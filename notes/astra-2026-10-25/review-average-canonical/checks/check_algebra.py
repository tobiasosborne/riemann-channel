#!/usr/bin/env python3
"""Independent direct resultant sums, local products, and exact half-polynomial search."""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
from collections import Counter
import sympy as s
from flint import nmod_poly
H=Path(__file__).resolve().parent
u,t,z,y=s.symbols('u t z y')
def monics(q,n):return [tuple(c)+(1,) for c in product(range(q),repeat=n)]
def poly(q,a):return nmod_poly(list(a),q)
def sf(q,a):p=poly(q,a);return p.gcd(p.derivative()).degree()==0
def factors(q,a):return [tuple(map(int,p)) for p,e in poly(q,a).factor()[1]]
def jac(q,a,b):
 if len(b)==1:return 1
 v=int(poly(q,b).resultant(poly(q,a)));r=pow(v,(q-1)//2,q)
 return 0 if r==0 else (1 if r==1 else -1)
def emit(*args):line=' '.join(map(str,args));print(line,flush=True);lines.append(line)
lines=[]
# Formula (1), including h=1, overlapping a,h and nontrivial reciprocity signs.
q=3; cases=0; signcases=0
for d in [2,3,4,5]:
 Ds=[D for D in monics(q,d) if sf(q,D)]
 for hd in range(4):
  for h in monics(q,hd):
   if hd and not sf(q,h):continue
   raw=1/(1-q*t) if not hd else sum(sum(jac(q,A,h) for A in monics(q,n))*t**n for n in range(hd))
   base=raw*(1-q*t*t)
   for P in factors(q,h):base/=1-t**(2*(len(P)-1))
   for ad in range(2):
    for a in monics(q,ad):
     expr=base
     for P in factors(q,a):
      if poly(q,h)%poly(q,P):expr/=1+jac(q,P,h)*t**(len(P)-1)
     value=(-1)**(d*hd)*s.expand(s.series(expr,t,0,d+1).removeO()).coeff(t,d)
     direct=sum(jac(q,tuple(map(int,poly(q,a)**2*poly(q,h))),D) for D in Ds)
     assert value==direct,(d,a,h,value,direct)
     cases+=1;signcases+=int(d*hd%2==1 and direct!=0)
emit('Euler (1)-(2) direct checks:',cases,'nonzero negative reciprocity-sign cases:',signcases)
# Equation (5): direct pairs versus finite bivariate local product; no use of (1).
d,m=5,2;Ds=[D for D in monics(q,d) if sf(q,D)];As=monics(q,m)
count=sum(poly(q,D).gcd(poly(q,a)).degree()==0 for D in Ds for a in As)
series={(0,0):1}
for r in range(1,max(d,m)+1):
 for P in monics(q,r):
  if poly(q,P).factor()[1]!=[(poly(q,P),1)]:continue
  local={(0,0):1}
  if r<=d:local[r,0]=1
  for j in range(1,m//r+1):local[0,j*r]=1
  nxt=Counter()
  for (a,b),v in series.items():
   for (c,e),w in local.items():
    if a+c<=d and b+e<=m:nxt[a+c,b+e]+=v*w
  series=nxt
assert count==series[d,m]
emit('Euler (5) q=3 d=5 m=2 pair_count=',count,'density=',F(count,len(Ds)*q**m))
# All small integer H-half examples, normalized by p0. Exact Sturm, not float roots.
tested=Counter();weak=Counter()
for g in range(4,9):
 k=g//2
 for a0 in range(1,6):
  for rest in product(range(11),repeat=k):
   half=(a0,)+rest
   P=list(map(F,half))
   if g%2==0:P[-1]/=2
   if any(P[j]<P[j+1] for j in range(k)):continue
   b=list(half)+list(half[:-1] if g%2==0 else half)[::-1]
   B=sum(v*z**j for j,v in enumerate(b))
   if g%2:B=s.div(B,1+z,z)[0]
   bb=s.Poly(B,z);ell=bb.degree()//2
   S=[s.Integer(2),y]
   for j in range(2,ell+1):S.append(s.expand(y*S[-1]-S[-2]))
   R=s.Poly(bb.nth(ell)+sum(bb.nth(ell-j)*S[j] for j in range(1,ell+1)),y)
   cnt=sum(mult*factor.count_roots(-2,2) for factor,mult in R.sqf_list()[1])
   assert cnt==ell,(g,b,R,cnt)
   tested[g]+=1;weak[g]+=int(P[0]==P[1])
emit('H-half exact degree 4..8 search (integer b0=1..5):',dict(tested),'weak p0=p1 controls:',dict(weak),'off_circle=0')
B=1+3*z*z+z**4
emit('Warning if even central coefficient is omitted: B=',B,'first coefficients [1,0]; y-polynomial=',y*y+1,'off_circle=True; H-half FAILS [1,0,3/2]')
# All-q low-genus symbolic identities and the induction slack.
qv,g=s.symbols('q g',integer=True,positive=True)
slack=qv**4-1-(qv*qv-1)*s.Rational(3,2)
emit('b1 bracket bound base slack=',s.factor(slack),'induction increment=',s.factor((qv*qv-1)*((qv*qv-1)*g+qv*qv)/2))
for q in [3,5,7,9,11,25]:
 vals=[]
 for g in range(1,31):
  b1=F(q,q+1)+F(1,q**(2*g))*(F(1,q+1)+F((q-1)*g-1+(q if g%2 else -1),2))
  assert b1==1 if g==1 else 0<b1<1
  if g<=3:vals.append(b1)
 emit('Eq7 q=',q,'g=1,2,3:',vals,'inequality g=2..30 PASS')
# Cubic all squarefree degree-three moduli, one fixed norm-symbol and its conjugate.
q=7;Ds=[D for D in monics(q,3) if sf(q,D)];normlog={pow(3,j,7):j%3 for j in range(6)}
raw=[0,0,0];comp=[0,0];whole=[0,0,0];hist=Counter()
for D in Ds:
 co=[]
 for n in range(3):
  counts=Counter()
  for a in monics(q,n):
   v=int(poly(q,D).resultant(poly(q,a)))
   if v:counts[normlog[v]]+=1
  co.append((counts[0]-counts[2],counts[1]-counts[2]))
 assert co[0]==(1,0) and tuple(sum(c[j] for c in co) for j in [0,1])==(0,0)
 a,b=1+co[1][0],co[1][1];hist[a,b]+=1
 for n in range(3):raw[n]+=co[n][0]
 assert sum(c[1] for c in co)==0
 comp[0]+=1;comp[1]+=a
 whole[0]+=1;whole[1]+=2*a-b;whole[2]+=a*a-a*b+b*b
assert sum(b*count for (a,b),count in hist.items())==0
emit('cubic q=7 d=3 H=',len(Ds),'one-symbol raw=',[F(v,len(Ds)) for v in raw],'completed=',[F(v,len(Ds)) for v in comp],'whole=',[F(v,len(Ds)) for v in whole])
emit('cubic completed linear coefficient histogram (a+b*omega):',sorted(hist.items()))
# Common-vacuum obstruction.
emit('vacuum average=',s.expand(((1-z)**4+(1+z)**4)/2),'root radii=sqrt(2)-1,sqrt(2)+1')
(H/'output_algebra.txt').write_text('\n'.join(lines)+'\n')
