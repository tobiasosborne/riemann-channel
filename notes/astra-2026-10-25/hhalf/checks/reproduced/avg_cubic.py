#!/usr/bin/env python3
"""Exact Z[omega] averages for monic squarefree y^3=D, q=7,13, d<=4.

Also prints the average of the WHOLE curve numerator, distinct from an isotypic L.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from common import *


def generator(q):
    return next(a for a in range(2,q) if len({pow(a,j,q) for j in range(q-1)})==q-1)


@lru_cache(None)
def cubic_table(q,p):
    r=len(p)-1
    mu=pow(generator(q),(q-1)//3,q)
    log={pow(mu,j,q):j for j in range(3)}
    mod=nmod_poly(list(p),q)
    tab=[]
    for code in range(q**r):
        a=nmod_poly([(code//q**i)%q for i in range(r)],q)
        v=a.pow_mod((q**r-1)//3,mod)
        if not v:
            tab.append(-1)
        else:
            assert v.degree()==0
            tab.append(log[int(v[0])])
    return np.array(tab,dtype=np.int64)


def mul_phase(a,b,phase):
    return np.where(phase==0,a,np.where(phase==1,-b,np.where(phase==2,b-a,0))),np.where(phase==0,b,np.where(phase==1,a-b,np.where(phase==2,-a,0)))


def cubic(q,d):
    polys=matrix_monics(q,d)[squarefree_mask(q,d)]
    count=len(polys)
    ca=np.zeros((d,count),dtype=np.int64);cb=ca.copy();ca[0]=1
    for r in range(1,d):
        for p in irreducibles(q,r):
            phase=cubic_table(q,p)[residue_codes(q,polys,p)]
            for n in range(r,d):
                aa,bb=mul_phase(ca[n-r],cb[n-r],phase)
                ca[n]+=aa;cb[n]+=bb
    raw_a=[F(int(row.sum()),count) for row in ca]
    raw_b=[F(int(row.sum()),count) for row in cb]
    if d%3==0:
        assert np.all(ca.sum(axis=0)==0) and np.all(cb.sum(axis=0)==0)
        ca=np.cumsum(ca,axis=0)[:-1];cb=np.cumsum(cb,axis=0)[:-1]
    avg_a=[F(int(row.sum()),count) for row in ca]
    avg_b=[F(int(row.sum()),count) for row in cb]
    assert not any(raw_b) and not any(avg_b), 'Full ensemble should be conjugation invariant.'
    curve=[]
    for n in range(2*len(ca)-1):
        val=0;imag=0
        for i in range(len(ca)):
            j=n-i
            if 0<=j<len(ca):
                val+=int((ca[i]*(ca[j]-cb[j])+cb[i]*cb[j]).sum())
                imag+=int((-ca[i]*cb[j]+cb[i]*(ca[j]-cb[j])+cb[i]*cb[j]).sum())
        assert imag==0
        curve.append(F(val,count))
    return count,raw_a,avg_a,curve


def main():
    with Path(__file__).with_name('output_cubic.txt').open('w') as f:
        def emit(s):print(s,flush=True);print(s,file=f,flush=True)
        emit('Cubic character from the product residue symbol; omega^2+omega+1=0. Exact coefficient pairs.')
        for q in [7,13]:
            for d in range(1,5):
                count,raw,comp,curve=cubic(q,d)
                emit(f'q={q} d={d} H={count} raw={expr(raw)} completed_isotypic={expr(comp)} expected_degree={d-1-int(d%3==0)}')
                root_report(comp,q,f'isotypic q={q} d={d}',emit)
                emit(f'  whole_curve_average={expr(curve)}')
                r,iv=sturm_curve_certificate(curve,q)
                emit(f'  whole_curve_exact_Sturm_band=True R(x)={r}')
                root_report(curve,q,f'whole curve q={q} d={d}',emit)
                if d==3:assert comp==[1,1]
        emit('ALL EXACT CUBIC ENUMERATIONS COMPLETE.')


if __name__=='__main__':main()
