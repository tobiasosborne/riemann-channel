#!/usr/bin/env python3
"""Exact cycle obstructions from exterior-character Gram matrices. No sampling."""
from collections import Counter
from itertools import combinations
from math import comb
import sympy as s
x,t,z=s.symbols('x t z')

def su2_exteriors(b):
    weights=list(range(b,-b-1,-2));out=[]
    for k in range(b+2):
        w=Counter(sum(c) for c in combinations(weights,k))
        dec={j:w[j]-w[j+2] for j in range(max(w),-1,-1) if w[j]-w[j+2]>0}
        assert sum((j+1)*m for j,m in dec.items())==comb(b+1,k)
        out.append(dec)
    return out

def gram_u2(b,central_nonzero=True):
    dec=su2_exteriors(b);d=b+1
    return s.Matrix(d+1,d+1,lambda a,c: 0 if central_nonzero and a!=c else sum(m*dec[c].get(j,0) for j,m in dec[a].items()))

def from_gram(H):
    d=H.rows-1
    la=s.expand(sum((-1)**(a+b)*H[a,b]*z**(d-a-b) for a in range(d+1) for b in range(d+1)))
    p=s.expand(la).coeff(z,0)
    for k in range(1,d+1):
        assert la.coeff(z,k)==la.coeff(z,-k)
        p+=la.coeff(z,k)*2*s.chebyshevt(k,t/2)
    return s.Poly(s.expand(p),t)

def info(p):
    intervals=s.polys.polytools.intervals(p,eps=s.Rational(1,10**12))
    rr=sum(m for _,m in intervals)
    band=sum(m for (a,b),m in intervals if a>=-2 and b<=2)
    return rr,band

def main():
    print('F(t)=E det(t-rho(g)-rho(g)*); Phi_C_l=F(2T_l(x/2)). Exact rational Sturm isolation.')
    for b in range(1,11):
        for central in [True]+([False] if b%2==0 else []):
            H=gram_u2(b,central);p=from_gram(H)
            print(f'b={b}, d={b+1}, central_nonzero={central}, P1={H==s.eye(b+2)}')
            print('exterior SU2 decompositions',su2_exteriors(b))
            print('F(t)=',s.factor(p.as_expr()),' real,band=',info(p))
            if b<=5:
                cp=s.Poly(p.as_expr().subs(t,x**3-3*x),x)
                print('C3=',cp.as_expr(),' real roots=',sum(m for _,m in s.polys.polytools.intervals(cp)))
    H=s.eye(4);H[0,3]=H[3,0]=1
    p=from_gram(H)
    print('SU3:',p.as_expr(),'discriminant=',s.discriminant(p.as_expr(),t),'real,band=',info(p))
    H[1,2]=H[2,1]=1
    print('SO3:',s.factor(from_gram(H).as_expr()))
    y=s.Symbol('y')
    print('U2 Sym5 reduced cubic discriminant=',s.discriminant(y**3-5*y**2+8*y-3,y))
    # A concrete failed raw balanced second-design test for S3 standard.
    chars=[(1,2),(3,0),(2,-1)]
    print('S3 standard E|chi|^4=',s.Rational(sum(n*c**4 for n,c in chars),6),' U2 value=2')

if __name__=='__main__':main()
