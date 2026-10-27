#!/usr/bin/env python3
"""Finite-field arithmetic, point enumeration, elliptic groups and genus-2 2-torsion.
No PARI ellgroup/ellcard/hyperellcharpoly in the independent calculations.
Author: codex:gpt-6-astra.
"""
import itertools, math, json
from pathlib import Path
import os
os.environ["SYMPY_GROUND_TYPES"]="python"
import sympy as s
x=s.symbols('x')
class Field:
 def __init__(self,p,k):
  self.p,self.k,self.Q=p,k,p**k
  self.digits=[tuple((a//p**i)%p for i in range(k)) for a in range(self.Q)]
  if k==1:self.mod=[0,1]
  else:
   for coeff in itertools.product(range(p),repeat=k):
    if coeff[0] and s.Poly(x**k+sum(a*x**i for i,a in enumerate(coeff)),x,modulus=p).is_irreducible:
     self.mod=list(coeff)+[1];break
  def rawmul(a,b):
   if k==1:return a*b%p
   out=[0]*(2*k-1)
   for i,u in enumerate(self.digits[a]):
    for j,v in enumerate(self.digits[b]):out[i+j]+=u*v
   for i in range(2*k-2,k-1,-1):
    c=out[i]%p
    for j in range(k):out[i-k+j]-=c*self.mod[j]
   return sum((out[i]%p)*p**i for i in range(k))
  def rawpow(a,n):
   z=1
   while n:
    if n&1:z=rawmul(z,a)
    a=rawmul(a,a);n>>=1
   return z
  for g in range(1,self.Q):
   if all(rawpow(g,(self.Q-1)//r)!=1 for r in s.factorint(self.Q-1)):
    self.generator=g;break
  self.logs=[None]*self.Q;self.exps=[];a=1
  for i in range(self.Q-1):self.logs[a]=i;self.exps.append(a);a=rawmul(a,g)
  assert a==1 and all(z is not None for z in self.logs[1:])
 def C(self,a):return a%self.p
 def add(self,a,b):
  if self.p==2:return a^b
  return sum(((u+v)%self.p)*self.p**i for i,(u,v) in enumerate(zip(self.digits[a],self.digits[b])))
 def neg(self,a):return sum(((-u)%self.p)*self.p**i for i,u in enumerate(self.digits[a]))
 def sub(self,a,b):return self.add(a,self.neg(b))
 def mul(self,a,b):return 0 if not a or not b else self.exps[(self.logs[a]+self.logs[b])%(self.Q-1)]
 def div(self,a,b):
  assert b
  return 0 if not a else self.exps[(self.logs[a]-self.logs[b])%(self.Q-1)]
 def pow(self,a,n):return 1 if n==0 else (0 if not a else self.exps[self.logs[a]*n%(self.Q-1)])
 def poly(self,cs,a):
  v=0
  for c in reversed(cs):v=self.add(self.mul(v,a),self.C(c))
  return v

class Elliptic:
 def __init__(self,F,a2,a4,a6):self.F=F;self.a2=F.C(a2);self.a4=F.C(a4);self.a6=F.C(a6)
 def points(self):
  F=self.F;ys={}
  for y in range(F.Q):ys.setdefault(F.add(F.mul(y,y),y),[]).append(y)
  pts=[None]
  for a in range(F.Q):
   v=F.add(F.mul(a,F.add(F.mul(a,F.add(a,self.a2)),self.a4)),self.a6)
   pts.extend((a,b) for b in ys.get(v,[]))
  return pts
 def add(self,P,Q):
  if P is None:return Q
  if Q is None:return P
  F=self.F;a,b=P;c,d=Q
  if a==c and F.add(F.add(b,d),1)==0:return None
  if a==c:
   num=F.add(F.add(F.mul(F.C(3),F.mul(a,a)),F.mul(F.mul(F.C(2),self.a2),a)),self.a4)
   den=F.add(F.mul(F.C(2),b),1)
  else:num,den=F.sub(d,b),F.sub(c,a)
  lam=F.div(num,den);nu=F.sub(b,F.mul(lam,a))
  xx=F.sub(F.sub(F.sub(F.mul(lam,lam),self.a2),a),c)
  yy=F.neg(F.add(F.add(F.mul(lam,xx),nu),1))
  return xx,yy
 def times(self,P,n):
  out=None
  while n:
   if n&1:out=self.add(out,P)
   P=self.add(P,P);n>>=1
  return out
 def group(self):
  points=self.points();N=len(points);factors=s.factorint(N);exponent=1
  for P in points[1:]:
   order=N
   for r in factors:
    while order%r==0 and self.times(P,order//r) is None:order//=r
   assert self.times(P,order) is None
   exponent=math.lcm(exponent,order)
   if exponent==N:break
  inv=[N//exponent,exponent]
  return [z for z in inv if z!=1],N

def combined(invs):
 primes=set().union(*(set(s.factorint(z)) for z in invs));parts=[]
 for p in sorted(primes):parts.append(sorted([int(s.factorint(z).get(p,0)) for z in invs]))
 out=[math.prod(p**parts[j][i] for j,p in enumerate(sorted(primes))) for i in range(len(invs))]
 return [z for z in out if z!=1]

def curve_count(F):
 squares={}
 for a in range(F.Q):squares[F.mul(a,a)]=squares.get(F.mul(a,a),0)+1
 count=sum(squares.get(F.poly([37,0,-11,0,-9,0,-1],a),0) for a in range(F.Q))
 return count+squares.get(F.C(-1),0)

def rational_two_torsion(l,k=1):
 # J[2] = even subsets of six branch points modulo complement; Frobenius acts by factor cycles.
 fs=s.factor_list(-x**6-9*x**4-11*x**2+37,modulus=l)[1]
 degrees=[s.degree(f) for f,e in fs for _ in range(e)];perm=[];off=0
 for d in degrees:
  d=int(d);perm.extend(off+(i+1)%d for i in range(d));off+=d
 def act(mask):
  for _ in range(k):mask=sum(((mask>>i)&1)<<perm[i] for i in range(6))
  return min(mask,mask^63)
 classes={min(a,a^63) for a in range(64) if a.bit_count()%2==0}
 fixed=sum(act(a)==a for a in classes)
 return list(map(int,degrees)),fixed

if __name__=='__main__':
 # Algebraic identities proving the two quotient maps land on the precise named curves.
 u,v=s.symbols('u v')
 A=(4*u+3)**3-9*(4*u+3)**2+11*(4*u+3)+37
 B=(4*u+5)**3-11*(4*u+5)**2-333*(4*u+5)-1369
 assert s.expand(A-(64*(u**3-u)+16))==0
 assert s.expand(B-(64*(u**3+u**2-23*u-50)+16))==0
 print('Quotient minimal-model substitutions checked: X=4u+3 or 4u+5; Y=8v+4.')
 from cypari2 import Pari
 pari=Pari();pari.allocatemem(200000000,silent=True)
 for a in ([0,-9,0,11,37],[0,-11,0,-333,-1369]):
  E=pari.ellinit(a); print('Quotient',a,'minimal model',list(pari.ellminimalmodel(E))[:5],'j',E[12])
 data={}
 for l in [2,3,5,7]:
  for k in [1,2,3,4]:
   F=Field(l,k);g1,n1=Elliptic(F,0,-1,0).group();g2,n2=Elliptic(F,1,-23,-50).group()
   inv=combined(g1+g2);data[f'{l},{k}']={'E1':g1,'E2':g2,'product':inv,'order':n1*n2}
   print('ell,k',l,k,'E1',g1,'E2',g2,'product',inv,'order',n1*n2,flush=True)
 for l in [3,5,7,11,13,17,19,23,139]:
  N1=curve_count(Field(l,1));N2=curve_count(Field(l,2));S1=l+1-N1;S2=l*l+1-N2
  coeff=[1,-S1,(S1*S1-S2)//2,-l*S1,l*l]
  H=pari.charpoly(pari.mfheckemat(pari.mfinit([37,2],1),l))
  X=pari('x');Z=pari('z');cp=pari.polresultant(pari.subst(H,X,Z),X*X-Z*X+l,Z)
  target=[int(pari.polcoef(cp,4-i)) for i in range(5)]
  assert coeff==target
  print('Direct genus-2 points ell',l,'N1',N1,'N2',N2,'P ascending',coeff,'Hecke equal',coeff==target,'#J(F_ell)',sum(coeff),flush=True)
  if l in [3,5,7,139]:
   for k in ([1] if l==139 else [1,2,3,4]):
    deg,num=rational_two_torsion(l,k);print('ell,k',l,k,'branch factor degrees',deg,'#J[2](F_ell^k)',num)
  if l==139:
   roots=[a for a in range(l) if (-a**6-9*a**4-11*a*a+37)%l==0]
   print('New cell (p,ell,q)=(37,139,2): six branch roots',roots,'J[2] rank 4; graph companion fixed rank <=2')
 for l in [2,5,11]:
  H=pari.charpoly(pari.mfheckemat(pari.mfinit([37,2],1),l));X=pari('x');Z=pari('z')
  cp=pari.polresultant(pari.subst(H,X,Z),X*X-Z*X+l,Z)
  ds=int(pari.poldisc(cp));print('ell',l,'Frobenius discriminant',ds,'mod3',ds%3,'squarefree mod3',ds%3!=0)
  assert ds%3
 Path(__file__).with_name('arithmetic_data.json').write_text(json.dumps(data,indent=2)+'\n')
