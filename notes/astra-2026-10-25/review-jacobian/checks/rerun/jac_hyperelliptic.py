#!/usr/bin/env python3
"""Complete genus-4 hyperelliptic census over F2, including isomorphisms.

Binary integers encode polynomials, low bit = constant coefficient. Models
y^2+h*y=f, deg(h)<=5, deg(f)<=10, are reduced by y -> y+r (deg r<=5)
and PGL(2,F2). Smoothness is checked on both affine charts. Point counting
is exact over F2,F4,F8,F16; Newton identities recover the L-polynomial.
The JSON output is a multiset weighted by F2-isomorphism classes, not raw
equations. Run python3 checks/jac_hyperelliptic.py.
"""
import contextlib
from collections import Counter
from functools import lru_cache
import itertools
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent

def pmul(a,b):
    ans=0
    while b:
        if b&1: ans^=a
        a<<=1; b>>=1
    return ans

def pmod(a,b):
    while a and a.bit_length()>=b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a

def gcd(a,b):
    while b: a,b=b,pmod(a,b)
    return a

def derivative(a):
    return sum(1<<(i-1) for i in range(1,a.bit_length(),2) if a>>i&1)

def smooth(h,f,g):
    if not h: return False
    dh,df=derivative(h),derivative(f)
    if gcd(h,pmul(df,df)^pmul(pmul(dh,dh),f))!=1: return False
    if h>>(g+1)&1: return True
    return bool(((f>>(2*g+1))&1) ^ (((f>>(2*g+2))&1)*((h>>g)&1)))

@lru_cache(None)
def shifts(h,g):
    return tuple(sorted({pmul(r,r)^pmul(h,r) for r in range(1<<(g+2))}))

def minshift(h,f,g):
    return min(f^v for v in shifts(h,g))

GL2=[(a,b,c,d) for a,b,c,d in itertools.product((0,1),repeat=4) if a*d^b*c]

@lru_cache(None)
def transform_basis(degree,mat):
    a,b,c,d=mat
    X,Y=(a<<1)|b,(c<<1)|d
    px=[1]; py=[1]
    for _ in range(degree): px.append(pmul(px[-1],X)); py.append(pmul(py[-1],Y))
    return tuple(pmul(px[i],py[degree-i]) for i in range(degree+1))

def transform(f,degree,mat):
    ans=0
    for i,v in enumerate(transform_basis(degree,mat)):
        if f>>i&1: ans^=v
    return ans

def canonical(h,f,g):
    pairs=[]
    for mat in GL2:
        H=transform(h,g+1,mat); F=transform(f,2*g+2,mat)
        pairs.append((H,minshift(H,F,g)))
    return min(pairs)

class F2Field:
    def __init__(self,k):
        # All verified irreducible (degrees <=10 used for sampling).
        mods={1:3,2:7,3:11,4:19,5:37,6:67,7:131,8:283,9:515,10:1033}
        self.k=k; self.q=1<<k; self.mod=mods[k]
        # Validate irreducibility using repeated Frobenius and gcd.
        a=2
        for j in range(1,k+1):
            a=pmod(pmul(a,a),self.mod)
            if j<=k//2: assert gcd(a^2,self.mod)==1
        assert a==pmod(2,self.mod)
        self.table=[[self.mul(i,j) for j in range(self.q)] for i in range(self.q)] if k<=5 else None
    def mul(self,a,b): return pmod(pmul(a,b),self.mod)
    def power(self,a,n):
        ans=1
        while n:
            if n&1: ans=self.mul(ans,a)
            a=self.mul(a,a); n>>=1
        return ans
    def eval(self,f,a):
        ans=0
        for i in range(f.bit_length()-1,-1,-1):
            ans=self.mul(ans,a)^((f>>i)&1)
        return ans
    def trace(self,a):
        ans=0
        for _ in range(self.k): ans^=a; a=self.mul(a,a)
        assert ans in (0,1)
        return ans
    def solutions(self,h,f):
        if not h: return 1
        z=self.mul(f,self.power(h,2*self.q-4))
        return 2 if self.trace(z)==0 else 0

def point_counts(h,f,g,fields):
    out=[]
    for field in fields:
        out.append(sum(field.solutions(field.eval(h,a),field.eval(f,a)) for a in range(field.q))
                   +field.solutions((h>>(g+1))&1,(f>>(2*g+2))&1))
    return out

def lpoly_from_counts(N,p,g):
    traces=[0]+[p**k+1-N[k-1] for k in range(1,g+1)]
    c=[1]
    for k in range(1,g+1):
        a=-sum(c[k-i]*traces[i] for i in range(1,k+1))
        assert a%k==0
        c.append(a//k)
    c += [p**(k-g)*c[2*g-k] for k in range(g+1,2*g+1)]
    return c

def enumerate_g4():
    g=4; models=set(); raw=0; reduced=0
    for h in range(1,1<<(g+2)):
        seen=set()
        for f in range(1<<(2*g+3)):
            if f in seen: continue
            orb={f^v for v in shifts(h,g)}; seen.update(orb)
            if not smooth(h,f,g): continue
            raw+=len(orb); reduced+=1
            models.add(canonical(h,f,g))
    fields=[F2Field(k) for k in range(1,5)]
    records=[]; hist=Counter()
    flux=json.loads((HERE/'output_fluxes.json.txt').read_text())
    target=next(r['weil_coefficients'] for r in flux if r['graph']=='K4' and r['ramanujan'])
    for h,f in sorted(models):
        assert smooth(h,f,4)
        N=point_counts(h,f,4,fields); P=lpoly_from_counts(N,2,4)
        hist[tuple(P)]+=1
        records.append(dict(h=h,f=f,N=N,L=P))
    print(f'F2 genus4 raw smooth models={raw}; y-shift classes={reduced}; isomorphism classes={len(models)}')
    print(f'distinct L-polynomials={len(hist)}')
    print('N1 histogram='+str(sorted(Counter(r['N'][0] for r in records).items())))
    hits=[r for r in records if r['L']==target]
    print('K4 L coefficients low-to-high='+str(target))
    print('K4 matching isomorphism classes='+str(len(hits)))
    for r in hits: print('K4 MATCH '+str(r))
    for P,m in sorted(hist.items()): print(f'L={list(P)} multiplicity={m}')
    (HERE/'output_hyperelliptic.json.txt').write_text(json.dumps(records,indent=2)+'\n')
    # An independent published census check, not used to select any equation.
    assert len(models)==264
    assert sorted(Counter(r['N'][0] for r in records).items())==[(0,9),(1,32),(2,58),(3,66),(4,58),(5,32),(6,9)]
    return records

if __name__=='__main__':
    with (HERE/'output_hyperelliptic.txt').open('w') as f,contextlib.redirect_stdout(f):
        enumerate_g4()
    print('\n'.join((HERE/'output_hyperelliptic.txt').read_text().splitlines()[:12]))
