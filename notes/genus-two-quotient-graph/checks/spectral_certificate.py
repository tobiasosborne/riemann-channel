#!/usr/bin/env python3
"""Author: codex:gpt-6-astra. Exact characteristic and visibility certificates."""
import sys
sys.dont_write_bytecode=True
import numpy as np
import sympy as sp
from flint import fmpz_mat, fmpz_poly, fmpq_mat, fmpq
from graph_data import VERTICES,STABILISERS,TAILS,EDGES
from pathlib import Path
from fractions import Fraction
core=[i for i in range(len(VERTICES)) if i not in TAILS];ix={v:i for i,v in enumerate(core)}
heads=sorted({next(a for a,b,s in EDGES if b==t) for t in TAILS})
n=len(core)
A=[[0]*n for _ in range(n)]
for a,b,s in EDGES:
    if a in ix and b in ix:
        A[ix[a]][ix[b]]+=STABILISERS[a]//s;A[ix[b]][ix[a]]+=STABILISERS[b]//s
AA=fmpz_mat(A)
print('CHARPOLY START',flush=True)
cp=AA.charpoly();print('CORE CHAR FACTOR DEGREES',[(p.degree(),e) for p,e in cp.factor()[1]],flush=True)
# Select an exact integral Krylov basis, using a modular echelon test.
prime=1000003
basis=[];pivots=[];reduced=[];queue=[]
for h in heads:
    v=[0]*n;v[ix[h]]=1;queue.append(v)
count=0
while count<len(queue):
    v=queue[count];count+=1
    r=np.array([int(a%prime) for a in v],dtype=np.int64)
    for p,b in zip(pivots,reduced):r=(r-r[p]*b)%prime
    pos=np.flatnonzero(r)
    if not len(pos):continue
    p=int(pos[0]);r=r*pow(int(r[p]),-1,prime)%prime
    pivots.append(p);reduced.append(r);basis.append(v)
    av=[sum(A[i][j]*v[j] for j in range(n) if A[i][j]) for i in range(n)]
    queue.append(av)
d=len(basis);print('KRYLOV MODULAR RANK',d,flush=True)
K=fmpq_mat([[v[i] for v in basis] for i in range(n)])
KP=fmpq_mat([[v[i] for v in basis] for i in pivots])
AK=fmpq_mat(A)*K
B=KP.inv()*fmpq_mat([[AK[i,j] for j in range(d)] for i in pivots])
assert K*B==AK
print('EXACT INVARIANT KRYLOV DIMENSION',d,flush=True)
bp=B.charpoly()
bpi=fmpz_poly([int(c) for c in bp.coeffs()])
assert all(c.denominator==1 for c in bp.coeffs())
cc,rem=divmod(cp,bpi);assert rem==0
print('VISIBLE CHAR FACTORS',bpi.factor(),flush=True)
print('CUSP CHAR FACTOR DEGREES',[(p.degree(),e) for p,e in cc.factor()[1]],flush=True)
# Formula for the visible determinant from scalar Fourier eigenchannels.
x,t,a,r=sp.symbols('x t a r')
PP=lambda t:1-3*t+7*t*t-15*t**3+25*t**4
D0=sp.Poly(sp.expand(25*(1-5*t)*PP(t/5)+t**4*(5-t)*PP(t)),t).exquo(sp.Poly(t-1,t))
cheb=[2,r]
for k in range(2,5):cheb.append(sp.expand(r*cheb[-1]-cheb[-2]))
vv=D0.nth(4)+sum(D0.nth(4+k)*cheb[k] for k in range(1,5))
c0=sp.Poly(sp.expand(vv.subs(r,x*x/5-2)),x).monic().as_expr()
print('TRIVIAL VISIBLE CHAR',c0,flush=True)
r0=x*x/5-2
cplus=sp.expand(25*(5*r0**3+a*r0**2-14*r0-2*a))
cminus=sp.expand(5*x*(5*r0**2+a*r0-4))
H=a*(a*a-a-1)*(a**4-5*a**3+5*a*a+5*a-5)
expected=sp.Poly(c0*sp.resultant(H,cplus*cminus,a),x)
assert [int(v) for v in reversed(expected.all_coeffs())]==[int(v) for v in bpi.coeffs()]
print('FOURIER VISIBLE CHAR EXACT MATCH',flush=True)
# Save compact factor coefficient lists, low to high.
fac=[([int(c) for c in p.coeffs()],int(e)) for p,e in cc.factor()[1]]
Path(__file__).with_name('spectral_data.py').write_text('# Author: codex:gpt-6-astra\nCUSP_CHAR_FACTORS = '+repr(fac)+'\nVISIBLE_DIM = '+str(d)+'\n')
# Two exact rational evaluations of the full p / ptilde identity and predicted determinant.
PY=lambda t:PP(t)*(1+5*t*t)**2*(1+t+9*t*t+5*t**3+25*t**4)**2*(1+5*t+25*t*t+70*t**3+195*t**4+350*t**5+625*t**6+625*t**7+625*t**8)**2
def fq(a):
    return fmpq(a.numerator,a.denominator) if isinstance(a,Fraction) else fmpq(a)
for s in [Fraction(1,10),Fraction(1,3)]:
    # z=sqrt(5)*s; use similarity to A, hence rational entries.
    z2=5*s*s
    MM=fmpq_mat([[fq(-s*A[i][j]+(1+z2 if i==j else 0)) for j in range(n)] for i in range(n)])
    Num=fmpq_mat(MM);Den=fmpq_mat(MM)
    for h in heads:Num[ix[h],ix[h]]-=1;Den[ix[h],ix[h]]-=fq(z2)
    dv=Num.det()/Den.det()
    ep=(z2**45/Fraction(5**15))*Fraction(PY(z2),PY(z2/5))*(1-z2/5)/(1-5*z2)
    assert dv==fq(ep)
    # Evaluate the complete monic factorisation, including invisible cusp factors.
    dc=Fraction(1)
    for coeffs,e in fac:
        # All odd powers pair in even polynomials, except powers of x.
        deg=len(coeffs)-1
        # D_f=z^deg / 5^(deg/2) f(sqrt5*(z+1/z)); z=sqrt5*s.
        val=sum(Fraction(c)*s**deg*(5*s+1/s)**k for k,c in enumerate(coeffs))
        # 5^(deg/2) cancels z^deg, leaving s^deg.
        dc*=val**e
    pb=z2**45/Fraction(5**16)*(z2-5)*(z2-1)**7*PY(z2)
    assert Num.det()==fq(pb*dc)
    print('EXACT P AND DET CHECK',str(s),'PASSED',flush=True)
print('ALL ASSERTIONS PASSED',flush=True)
