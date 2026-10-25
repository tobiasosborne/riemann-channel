#!/usr/bin/env python3
"""Newton sums per member vs exact prime-power/character Euler formula.
Normalized even traces are rational; odd trace sums vanish exactly.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0,str(Path(__file__).parent/'reproduced'))
from common import *

def member_coefficients(q,g):
    d=2*g+1;ps=matrix_monics(q,d)[squarefree_mask(q,d)];H=len(ps)
    a=np.zeros((2*g+1,H),dtype=np.int64);a[0]=1
    for r in range(1,g+1):
        for p in irreducibles(q,r):
            ch=quadratic_table(q,p)[residue_codes(q,ps,p)]
            if q%4==3 and r%2:ch=-ch
            for n in range(r,g+1):a[n]+=ch*a[n-r]
    for n in range(g):a[2*g-n]=q**(g-n)*a[n]
    return a

def trace_exact(q,g,n):
    if n%2:return F(0),F(0),F(0)
    d=2*g+1;H=q**d-q**(d-1);sq=ns=0
    for r in range(1,n+1):
        if n%r:continue
        if (n//r)%2==0:
            v=series_factor([q**k for k in range(d+1)],2,-q)
            v=series_factor(v,r,1,True)
            sq+=r*len(irreducibles(q,r))*v[d]
        else:
            for p in irreducibles(q,r):
                ell=quadratic_L(q,p)
                v=list(ell)+[0]*max(0,d+1-len(ell));v=v[:d+1]
                v=series_factor(v,2*r,-1,True)
                v=series_factor(v,2,-q)
                ns+=r*v[d]
    return F(-(sq+ns),H*q**(n//2)),F(-sq,H*q**(n//2)),F(-ns,H*q**(n//2))

def main():
    with Path(__file__).with_name('output_hhalf_rudnick.txt').open('w') as log:
        def emit(s):print(s,flush=True);print(s,file=log,flush=True)
        for q,g in [(3,1),(3,2),(3,3),(5,1),(5,2),(7,1)]:
            a=member_coefficients(q,g);H=a.shape[1];power=np.zeros_like(a)
            for n in range(1,2*g+1):
                power[n]=-n*a[n]-sum(a[j]*power[n-j] for j in range(1,n))
                brute=F(int(power[n].sum()),H*q**(n//2))
                if n%2:assert brute==0
                closed,sq,ns=trace_exact(q,g,n)
                assert brute==closed,(q,g,n,brute,closed)
                emit(f'q={q} g={g} n={n} mean_normalized_trace={closed} square={sq} nonsquare={ns} enumeration_agrees=True')
            t1sq=F(int((a[1]**2).sum()),H*q)
            mean_a2=F(int(a[2].sum()),H*q)
            fake=-trace_exact(q,g,2)[0]/2
            assert mean_a2==fake+t1sq/2
            emit(f'q={q} g={g} [z^2]mean_det={mean_a2} [z^2]exp_mean_log={fake} mean_trace1_squared={t1sq}; discrepancy={mean_a2-fake}')
        emit('ALL EXACT PRIME-POWER FORMULAS MATCH ENUMERATION. SINGLE TRACES DO NOT DETERMINE THE AVERAGED DETERMINANT.')
if __name__=='__main__':main()
