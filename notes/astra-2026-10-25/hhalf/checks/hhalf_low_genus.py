#!/usr/bin/env python3
"""Universal genus <=7 proof by exact polynomial interpolation.
Polynomiality and degree bounds are proved in astra-proofs.md, not inferred
from these samples. 22 nodes determine degree <=21 polynomials exactly.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import sympy as sp
from exact_core import raw_series

def main():
    q=sp.Symbol('q');x=sp.Symbol('x');D=15
    nodes=list(sp.primerange(3,84));assert len(nodes)==22
    with Path(__file__).with_name('output_low_genus.txt').open('w') as log:
        def emit(s):print(s,flush=True);print(s,file=log,flush=True)
        data={}
        for p in nodes+[89,97,9]:
            data[p]={n:list(raw_series(int(p),n,D)[0]) for n in [2,4,6]}
            emit(f'node={p} exact_series='+repr({n:list(map(int,v)) for n,v in data[p].items()}))
        # Newton interpolation, exact QQ.
        def interpolate(vals):
            dd=list(map(sp.Rational,vals));ans=sp.Integer(0);prod=sp.Integer(1)
            for k in range(len(nodes)):
                ans+=dd[0]*prod;prod*=q-nodes[k]
                dd=[(dd[j+1]-dd[j])/(nodes[j+k+1]-nodes[j]) for j in range(len(dd)-1)]
            return sp.Poly(ans,q)
        for g in range(1,8):
            d=2*g+1;prev=sp.Poly((q-1)*q**(d-1),q)
            for m in range(1,g//2+1):
                n=2*m;P=interpolate([int(data[p][n][d]) for p in nodes])
                assert P.degree()<=d+n
                for p in [89,97,9]:assert P.eval(p)==int(data[p][n][d])
                gap=sp.Poly(q*prev.as_expr()-P.as_expr(),q)
                ps=sp.Poly(P.as_expr().subs(q,x+3),x)
                gs=sp.Poly(gap.as_expr().subs(q,x+3),x)
                assert all(c>=0 for c in ps.all_coeffs()) and ps.eval(0)>0
                assert all(c>=0 for c in gs.all_coeffs()) and gs.eval(0)>0
                emit(f'g={g} m={m} b_m={sp.factor(P.as_expr()/((q-1)*q**(d-1+m)))}')
                emit(f'  gap_numerator={sp.factor(gap.as_expr())}; shifted_coefficients_ascending={list(reversed(gs.all_coeffs()))}; strict_gap=True positive_b=True')
                prev=P
        emit('PROVED: H-HALF AND A1 FOR ALL ODD PRIME POWERS q AND g=1..7 (g=1 has empty inequality).')
if __name__=='__main__':main()
