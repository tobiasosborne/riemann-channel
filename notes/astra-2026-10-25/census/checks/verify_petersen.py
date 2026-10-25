#!/usr/bin/env python3
"""Independent direct fiber count of y^3=x^12+x^9+x^6+x^3+1.
No C++ search routines, projective-orbit counting, or stored census counts
are used to produce the counts. A histogram enumerates every y in each field.
"""
import json
from collections import Counter
import sympy as S
from census_lookup import HERE,FLUX,coeff_from_counts,counts_from_coeff
from lowgenus import Field,pmul,gcd,deriv

def main():
    r=next(r for r in json.loads(FLUX.read_text()) if r['graph']=='Petersen' and r['mask']==22)
    f=sum(1<<i for i in [0,3,6,9,12])
    assert gcd(f,deriv(f))==1
    print('f bitmask',f,'derivative bitmask',deriv(f),'gcd(f,f_prime)=1')
    N=[]
    for k in range(1,13):
        F=Field(k)
        cubes=Counter(F.mul(F.mul(y,y),y) for y in range(F.q))
        affine=0
        for x in range(F.q):
            # Horner in s=x^3, independent of search monomial evaluation.
            s=F.mul(F.mul(x,x),x)
            v=1
            for _ in range(4):v=F.mul(v,s)^1
            affine+=cubes[v]
        infinity=cubes[1] # w=y/x^4, w^3=1 at t=1/x=0.
        N.append(affine+infinity)
        print('k',k,'modulus',F.mod,'affine',affine,'infinity',infinity,'total',N[-1])
    c=coeff_from_counts(N[:10])
    assert c==r['weil_coefficients']
    assert N==counts_from_coeff(c,12)==[r['N'][str(k)] for k in range(1,13)]
    t=S.Symbol('T')
    P=sum(c[i]*t**i for i in range(21))
    assert S.expand(P-(1+2*t*t)**4*(1-t*t+4*t**4)**3)==0
    print('N1..12',N)
    print('P(T)',S.factor(P))
    print('coefficient vector',c)
    print('2-rank',max(i for i,a in enumerate(c) if a%2))
    print('Smoothness: f squarefree; infinity w^3=1 has nonzero derivative w^2.')
    print('Geometric irreducibility: f has simple roots, hence is not a cube over algebraic closure.')
    print('Tame Riemann-Hurwitz: 12 branch points of index 3, infinity unramified; 2g-2=-6+24=18; g=10.')
    (HERE/'output_petersen_witness.json.txt').write_text(json.dumps(dict(equation='y^3=x^12+x^9+x^6+x^3+1',N=N,coeff=c,genus=10),indent=2)+'\n')

if __name__=='__main__':main()
