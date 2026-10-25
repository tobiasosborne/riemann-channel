#!/usr/bin/env python3
"""Independent checks using full Dirichlet sums, not midpoint reconstruction.

Also checks the stated symbolic formulas and the common-vacuum obstruction.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from common import *
from avg_hyperelliptic import brute,formula
from avg_cubic import cubic,generator


def main():
    with Path(__file__).with_name('output_audit.txt').open('w') as f:
        def emit(s):print(s,flush=True);print(s,file=f,flush=True)
        for q,g,even in [(3,1,False),(3,2,False),(5,1,False),(5,2,False),(3,1,True)]:
            d=2*g+1+even
            hs=[]
            mask=squarefree_mask(q,d)
            for i,D in enumerate(monics(q,d)):
                dp=nmod_poly(list(D),q)
                is_sf=dp.gcd(dp.derivative()).degree()==0
                assert bool(mask[i])==is_sf
                if is_sf:hs.append(D)
            sums=[0]*d
            for n in range(d):
                fs=list(monics(q,n))
                sums[n]=sum(jacobi(q,A,D) for D in hs for A in fs)
            a=[F(v,len(hs)) for v in sums]
            if even:
                assert sum(a)==0
                a=[sum(a[:k+1]) for k in range(d-1)]
            _,b=brute(q,g,even)
            c,_=formula(q,g,even,full=True)
            assert a==b==c
            emit(f'full-direct-Jacobi q={q} g={g} even={even} H={len(hs)} P={expr(a)} agrees_with_brute_Euler_and_full_A2=True')
        for q in [3,5,7,11,13]:
            for g in range(1,11):
                delta=q if g%2 else -1
                b1=F(q,q+1)+F(1,q**(2*g))*(F(1,q+1)+F((q-1)*g-1+delta,2))
                direct=sum(a2_coefficient(q,2*g+1,2))/q
                assert b1==direct
                assert b1==1 if g==1 else 0<b1<1
            for g in [1,2]:
                a,_=formula(q,g,even=True)
                if g==1:
                    expect=[F(1),1-F(1,q*q),F(q)]
                else:
                    A=1-F(1,q**4);B=q+F(1,q)-F(1,q*q)-F(1,q**3)
                    expect=[F(1),A,B,q*A,F(q*q)]
                assert a==expect
                sturm_curve_certificate(a,q)
            emit(f'Eq7 g=1..10 and even genera 1,2 exact formulas pass for q={q}')
        for q,d in [(7,3),(7,4)]:
            mask=squarefree_mask(q,d)
            Ds=[D for i,D in enumerate(monics(q,d)) if mask[i]]
            gg=generator(q)
            logs={pow(gg,j,q):j%3 for j in range(q-1)}
            sums=[]
            for n in range(d):
                counts=[0,0,0]
                for D in Ds:
                    mod=nmod_poly(list(D),q)
                    for a in monics(q,n):
                        norm=int(mod.resultant(nmod_poly(list(a),q)))
                        if norm:counts[logs[norm]]+=1
                sums.append((F(counts[0]-counts[2],len(Ds)),F(counts[1]-counts[2],len(Ds))))
            _,raw,comp,curve=cubic(q,d)
            assert [x for x,y in sums]==raw and not any(y for x,y in sums)
            emit(f'cubic direct-resultant q={q} d={d} raw={expr(raw)} completed={expr(comp)} agrees_with_Euler=True')
        z=sp.Symbol('z')
        common=sp.expand(((1-z)**4+(1+z)**4)/2)
        assert common==1+6*z*z+z**4
        emit(f'common-vacuum counterexample: average of det(I-zI_4), det(I+zI_4) = {common}; radii=sqrt(2)-1,sqrt(2)+1')
        root_report([1,0,6,0,1],1,'common vacuum',emit)
        emit('ALL INDEPENDENT AUDITS PASS.')


if __name__=='__main__':main()
