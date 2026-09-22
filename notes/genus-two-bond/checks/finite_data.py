#!/usr/bin/env python3
"""Author: codex:gpt-6-astra. Exact finite data; prints only, writes no files."""
from itertools import product
from collections import Counter
import sympy as s
import numpy as np
x,T,z=s.symbols('x T z')
def P(a): return s.Poly(a,x, modulus=5)
f=P(x**5+x**3+x**2-2)
assert s.gcd(f,f.diff())==P(1)
class Field:
    def __init__(self,k):
        self.k=k
        self.mod=next(tuple(c)+(1,) for c in product(range(5),repeat=k) if P(sum(c[i]*x**i for i in range(k))+x**k).is_irreducible)
        self.el=list(product(range(5),repeat=k))
        self.zero=(0,)*k
    def c(self,n): return (n%5,)+(0,)*(self.k-1)
    def add(self,a,b): return tuple((v+w)%5 for v,w in zip(a,b))
    def mul(self,a,b):
        k=self.k; c=[0]*(2*k-1)
        for i in range(k):
            for j in range(k): c[i+j]+=a[i]*b[j]
        for i in range(2*k-2,k-1,-1):
            for j in range(k): c[i-k+j]-=c[i]*self.mod[j]
        return tuple(v%5 for v in c[:k])
    def pw(self,a,n):
        out=self.c(1)
        while n:
            if n&1: out=self.mul(out,a)
            a=self.mul(a,a); n//=2
        return out
    def val(self,a):
        return self.add(self.add(self.add(self.pw(a,5),self.pw(a,3)),self.pw(a,2)),self.c(-2))
def key(D): return tuple(tuple(int(t)%5 for t in p.all_coeffs()) for p in D)
def red(u,v):
    u=u.monic(); v=v%u
    while u.degree()>2:
        u=((f-v*v).exquo(u)).monic(); v=(-v)%u
    return u,v
O=(P(1),P(0))
def add(A,B):
    u1,v1=A;u2,v2=B
    a,b,d1=s.gcdex(u1,u2)
    c,d,g=s.gcdex(d1,v1+v2)
    u=(u1*u2).exquo(g*g)
    v=(c*a*u1*v2+c*b*u2*v1+d*(v1*v2+f)).exquo(g)%u
    return red(u,v)
def main():
    counts=[]
    for k in range(1,5):
        F=Field(k); squares=Counter(F.mul(a,a) for a in F.el)
        n=1+sum(squares[F.val(a)] for a in F.el);counts.append(n)
        print('FIELD',k,F.mod,'N',n)
    assert counts==[3,31,117,619]
    ps=[5**k+1-counts[k-1] for k in range(1,5)]
    co=[s.Integer(1)]
    for n in range(1,5):co.append(-sum(co[n-j]*ps[j-1] for j in range(1,n+1))/n)
    pol=sum(co[n]*T**n for n in range(5));print('POWER SUMS',ps,'P',pol)
    pts=[(a,b) for a,b in product(range(5),repeat=2) if (b*b-int(f.eval(a)))%5==0]
    print('RATIONAL',pts,'infinity')
    G=(P(x-pts[0][0]),P(pts[0][1])); Ds=[O]
    for n in range(1,16): Ds.append(add(Ds[-1],G))
    assert key(Ds[15])==key(O) and len({key(D) for D in Ds[:15]})==15
    allDs=[]
    for d0 in range(3):
        for uc in product(range(5),repeat=d0):
            u=P(x**d0+sum(uc[i]*x**i for i in range(d0)))
            for vc in product(range(5),repeat=d0):
                v=P(sum(vc[i]*x**i for i in range(d0)))
                if (f-v*v)%u==P(0): allDs.append((u,v))
    assert {key(D) for D in allDs}=={key(D) for D in Ds[:15]}
    for n,(u,v) in enumerate(Ds[:15]): print('CLASS',n,str(u.as_expr()),str(v.as_expr()),'h0',int(n==0),int(n in (0,1,14)),1+int(n==0))
    for a,b in product(range(15),repeat=2): assert key(add(Ds[a],Ds[b]))==key(Ds[(a+b)%15])
    print('Z coeffs',[s.expand(s.series(pol/((1-T)*(1-5*T)),T,0,8).removeO()).coeff(T,n) for n in range(8)])
    for k in range(1,15):
        a=1+2*np.cos(2*np.pi*k/15)
        roots=np.roots([5,a,1]);print('CHAR',k,'a',format(a,'.12f'),'T roots',roots)
        assert all(abs(abs(v)-1/np.sqrt(5))<1e-12 for v in roots)
    W=s.cyclotomic_poly(15,z)
    Q=s.Poly(1,z)
    for k in range(1,15): Q=(Q*s.Poly(1+(1+z**k+z**(15-k))*T+5*T*T,z)).rem(s.Poly(W,z))
    Q=s.Poly(s.expand(Q.as_expr()),T)
    print('NONTRIVIAL PRODUCT',Q.as_expr())
    print('COVER P',s.expand(pol*Q.as_expr()))
    for d0 in [3,5,15]:
        Q0=s.Poly(1,z)
        for k in range(1,15):
            if 15//s.gcd(k,15)==d0: Q0=(Q0*s.Poly(1+(1+z**k+z**(15-k))*T+5*T*T,z)).rem(s.Poly(W,z))
        print('ORDER',d0,'PRODUCT',s.factor(Q0.as_expr()))
    Fpol=z**4-3*z**3+7*z*z-15*z+25
    print('DISC',s.discriminant(Fpol,z),'F roots',s.nroots(Fpol))
    print('ALL ASSERTIONS PASSED')
if __name__=='__main__':main()
