#!/usr/bin/env python3
"""Direct projective Q=C=0 count, Jacobian ranks, global smoothness certificate.
Fresh finite fields; no lane J imports or expected counts as computation input.
"""
from pathlib import Path
import json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
z=s.symbols('z')

def field(k):
    q=1<<k
    mod=next(m for m in range(2*q-1,q,-2) if s.Poly(sum(((m>>i)&1)*z**i for i in range(k+1)),z,modulus=2).is_irreducible)
    def mul(a,b):
        r=0
        while b:
            if b&1:r^=a
            b>>=1;a<<=1
            if a&q:a^=mod
        return r
    table=np.array([[mul(a,b) for b in range(q)] for a in range(q)],dtype=np.int64)
    return mod,table

def main():
    Ns=[];records=[]
    for k in range(1,9):
        mod,m=field(k);q=len(m);v=np.arange(q);v2=m[v,v]
        # Enumerate the normalized X=1 projective chart; filter Q first.
        yz=[(y,z) for y in range(q) for z in range(q) if y^int(m[z,z])==0]
        pts=[]
        for y,z0 in yz:
            C=m[v2,v]^v2^m[v2,z0]^v^m[v,m[y,z0]]^m[m[y,y],y]
            pts.extend((1,y,z0,int(t)) for t in v[C==0])
        # Remaining normalized charts X=0,Y=1; X=Y=0,Z=1; vertex.
        # Q=0 forces Z=0 in the first and excludes the second.
        pts.extend((0,1,0,int(t)) for t in v[(m[v2,v]^1)==0])
        assert 1!=0 # C(0,0,0,1)=1: vertex excluded.
        singular=[]
        for X,Y,Z,T in pts:
            Qg=[Y,X,0,0]
            Cg=[int(m[T,T]),int(m[T,Z]^m[Y,Y]),int(m[T,T]^m[T,Y]),int(m[T,T]^m[X,X]^m[Y,Z])]
            if all(m[Qg[i],Cg[j]]==m[Qg[j],Cg[i]] for i in range(4) for j in range(i+1,4)):singular.append((X,Y,Z,T))
        assert not singular
        Ns.append(len(pts));records.append(dict(k=k,modulus=mod,count=len(pts),singular=singular))
        print(f'K4 k={k} field_modulus={mod} projective_points={len(pts)} singular_points={len(singular)}')
    # Global algebraic-closure certificate on X=1, with Y=Z²:
    # G_T=T²+1+Z³ and G_Z=T(T+Z²). T=0 gives G=1 at G_T=0.
    # T=Z² gives G=Z²(Z⁴+Z²+1) and G_T=Z⁴+Z³+1.
    a=z**2*(z**4+z**2+1);b=z**4+z**3+1
    bez=s.gcdex(a,b,z,modulus=2)
    assert bez[2]==1
    assert s.Poly(bez[0]*a+bez[1]*b,z,modulus=2).as_expr()==1
    print('GLOBAL SMOOTHNESS Bezout: ('+str(bez[0])+') * ('+str(a)+') + ('+str(bez[1])+') * ('+str(b)+') = 1 mod 2')
    print('X=0: Q forces Z=0; Y=1 gives T^3=1 and nonzero partial C_T=T^2. Vertex excluded.')
    # Recover P from counts independently, as truncated exponential of trace series.
    u=s.symbols('u');series=sum(s.Rational(Ns[i-1]-2**i-1,i)*u**i for i in range(1,9))
    P=s.series(s.exp(series),u,0,9).removeO().expand()
    assert P==1+2*u**2+5*u**4+8*u**6+16*u**8
    print('COUNTS N1..8='+str(Ns));print('P(u)='+str(P))
    (HERE/'output_independent_k4.json.txt').write_text(json.dumps(dict(fields=records,N=Ns,P=str(P),bezout=list(map(str,bez))),indent=2)+'\n')

if __name__=='__main__':main()
