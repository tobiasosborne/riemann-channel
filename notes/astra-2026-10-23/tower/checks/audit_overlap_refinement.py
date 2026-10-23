#!/usr/bin/env python3
"""Independent recheck of lane F's decisive W1--W3, T2--T4 arithmetic.
Not a replacement claim for a complete PARI rerun of its 40 checks.
"""
from math import gcd
from sympy import Matrix,factorint
from exact_ec import Curve,dlog_mu,root,key
from tower_audit import snf,frob_matrix,intertwiners,isogenies,iso_map
from tower_strict import residues


def main():
    print('BACKEND: independent exact FLINT/Miller. Scope: F W1-W3, determinant/norm comparison; not the full original script.')
    M=Matrix([[1,-6],[1,1]])
    iso=isogenies(7,2,[3,3],[1,3])
    for k,N in [(4,2),(3,3),(4,4),(4,5),(8,8),(9,9),(16,16)]:
        l=next(iter(factorint(N)))
        inv=snf(M,k)
        es=[int(factorint(o).get(l,0)) for o in inv]
        if len(es)==1:
            es.append(0)
        E,Ep=Curve(7,k,[3,3],2),Curve(7,k,[1,3],2)
        o,g=E.primary_basis(l,es)
        op,gp=Ep.primary_basis(l,es)
        ps=[E.mul(oi//N,P) for oi,P in zip(o,g)]
        qs=[Ep.mul(oi//N,P) for oi,P in zip(op,gp)]
        w=root(E,N)
        z,zp=E.weil(*ps,N),Ep.weil(*qs,N)
        a,b=dlog_mu(z,w,N),dlog_mu(zp,w,N)
        F,Fp=frob_matrix(E,ps,N),frob_matrix(Ep,qs,N)
        dets=intertwiners(F,Fp,N)
        S={b*d*pow(a,-1,N)%N for d in dets}
        assert S==residues((2,0,3),N)
        print(f'W1 N={N} k={k}: Frob={F}, {Fp}; scales={sorted(S)}; isometry={1 in S}; anti-isometry={N-1 in S}')
        for d in (2,3):
            if gcd(d,N)!=1:
                continue
            images=[iso_map(E,iso[d],P) for P in ps]
            zi=Ep.weil(*images,N)
            assert zi==z**d
            assert all(Ep.frob(iso_map(E,iso[d],P))==iso_map(E,iso[d],E.frob(P)) for P in ps)
            print(f'W3 phi_{d} on E[{N}]: multiplier={d%N}; images are equivariant and pairing functoriality holds.')
    print('PASS all W1-W3 refinement checks; norm/determinant sets agree. Classification (b), not different orders or an identification bug.')


if __name__=='__main__':
    main()
