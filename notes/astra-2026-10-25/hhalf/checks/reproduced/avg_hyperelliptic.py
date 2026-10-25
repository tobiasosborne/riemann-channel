#!/usr/bin/env python3
"""Enumerate every squarefree D; exact coefficients from small-prime Euler factors.

Run: python3 notes/astra-2026-10-23/average/checks/avg_hyperelliptic.py
No individual RH assumption: coefficients above genus use only the functional equation.
Independent A2 evaluation uses lower-conductor Jacobi sums and Euler series extraction.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import time
from common import *


def brute(q,g,even=False):
    d=2*g+(2 if even else 1)
    polys=matrix_monics(q,d)[squarefree_mask(q,d)]
    count=len(polys)
    coef=np.zeros((g+1,count),dtype=np.int64)
    coef[0]=1
    for r in range(1,g+1):
        for p in irreducibles(q,r):
            chi=quadratic_table(q,p)[residue_codes(q,polys,p)]
            if q%4==3 and d*r%2:
                chi=-chi
            # ascending recurrence multiplies by the Euler factor (1-chi*u^r)^-1
            for n in range(r,g+1):
                coef[n]+=chi*coef[n-r]
    if even:
        coef=np.cumsum(coef,axis=0)
    low=[F(int(row.sum()),count) for row in coef]
    return count,complete_quadratic(q,g,low)


def formula(q,g,even=False,full=False):
    d=2*g+(2 if even else 1)
    bound=d-1 if full else g
    terms=[a2_coefficient(q,d,n) if (even or n%2==0) else (F(0),F(0)) for n in range(bound+1)]
    low=[s+r for s,r in terms]
    if even:
        low=[sum(low[:i+1]) for i in range(len(low))]
        if full:
            assert low[-1]==0
            low.pop()
    if full:
        assert low==complete_quadratic(q,g,low[:g+1])
        return low,terms
    return complete_quadratic(q,g,low),terms


def main():
    path=Path(__file__).with_name('output_hyperelliptic.txt')
    with path.open('w') as f:
        def emit(s):
            print(s,flush=True);print(s,file=f,flush=True)
        emit('Exact enumeration, A2 Euler-product formula, and functional equation; roots refined at 80 decimal digits.')
        for even in [False,True]:
            for q in [3,5,7]:
                for g in ([1,2] if even else [1,2,3]):
                    start=time.monotonic()
                    count,b=brute(q,g,even)
                    a,terms=formula(q,g,even,full=True)
                    assert a==b,(q,g,a,b)
                    emit(f'q={q} g={g} d={2*g+1+even} H={count} completed_average={expr(a)} A2_agrees=True')
                    emit(f'  A2 (square,nonsquare) coefficients through raw degree d-1: {terms}')
                    if not even:
                        half=[a[2*m]/q**m for m in range(g//2+1)]
                        if g%2==0:half[-1]/=2
                        assert all(half[i]>=half[i+1]>0 for i in range(len(half)-1))
                        emit(f'  exact H-half certificate={half}')
                    root_report(a,q,f'q={q} g={g} even={even}',emit)
                    if even:
                        raw=[a[0]]+[a[i]-a[i-1] for i in range(1,len(a))]+[-a[-1]]
                        emit(f'  raw_Dirichlet_average={expr(raw)}; additional root u=1, |u|sqrt(q)={math.sqrt(q):.12f}')
                    emit(f'  seconds={time.monotonic()-start:.3f}')
        emit('ALL REQUESTED ENUMERATIONS AND INDEPENDENT A2 COMPARISONS PASS.')


if __name__=='__main__':
    main()
