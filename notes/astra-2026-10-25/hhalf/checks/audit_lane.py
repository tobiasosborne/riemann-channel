#!/usr/bin/env python3
"""Read-only comparison of previous saved outputs; independent F_9 enumeration."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import re,hashlib,ast,json
import numpy as np
from exact_core import field,raw_series,old
from common import matrix_monics,monics
HERE=Path(__file__).parent
PRIOR=HERE.parents[2]/'astra-2026-10-23'/'average'/'checks'

def brute9(g):
    K=field(9);d=2*g+1;polys=matrix_monics(9,d)
    keep=np.array([K.poly(tuple(map(int,row))).is_squarefree() for row in polys]);polys=polys[keep]
    H=len(polys);assert H==9**d-9**(d-1)
    els=K.elements
    add=np.array([[K.codes[tuple(map(int,(a+b).to_list()))] for b in els] for a in els])
    mul=np.array([[K.codes[tuple(map(int,(a*b).to_list()))] for b in els] for a in els])
    neg=np.array([K.codes[tuple(map(int,(-a).to_list()))] for a in els])
    bound=2;co=np.zeros((bound+1,H),dtype=np.int64);co[0]=1
    for r in range(1,bound+1):
        for p in monics(9,r):
            P=K.poly(p)
            if not P.is_irreducible():continue
            vals=[]
            for code in range(9**r):
                a=K.poly(tuple((code//9**j)%9 for j in range(r)))
                v=a.pow_mod((9**r-1)//2,P)
                vals.append(0 if not v else 1 if v.constant_coefficient()==K.K.one() else -1)
            aa=polys.copy()
            for i in range(d,r-1,-1):
                c=aa[:,i].copy()
                for j in range(r):aa[:,i-r+j]=add[aa[:,i-r+j],neg[mul[c,p[j]]]]
            codes=(aa[:,:r]*np.array([9**j for j in range(r)])).sum(axis=1)
            chi=np.array(vals,dtype=np.int64)[codes]
            for n in range(r,bound+1):co[n]+=chi*co[n-r]
    return H,[F(int(row.sum()),H) for row in co]

def main():
    with (HERE/'output_audit_lane.txt').open('w') as log:
        def emit(s):print(s,flush=True);print(s,file=log,flush=True)
        for p in (HERE/'reproduced').glob('*.py'):
            src=PRIOR/p.name
            assert p.read_bytes()==src.read_bytes()
            emit(f'prior_source_unchanged_copy={p.name} sha256={hashlib.sha256(src.read_bytes()).hexdigest()}')
        # Exact printed algebra only; timings and floating roots are not compared bitwise.
        patterns={
            'hyperelliptic':r'^(q=\d+ g=\d+ d=|  A2 \(|  exact H-half|  raw_Dirichlet)',
            'extended':r'^(q=\d+ g=\d+ average=|  H-half=|even q=)',
            'cubic':r'^(q=\d+ d=|  whole_curve_average=|  whole_curve_exact)',
            'level':r'^(q=\d+ d=|  sum_of_completed|  exact_order=)',
            'audit':r'^(full-direct|Eq7 |cubic direct|common-vacuum counterexample:)',
        }
        for name,pat in patterns.items():
            before=(PRIOR/f'output_{name}.txt').read_text();after=(HERE/'reproduced'/f'output_{name}.txt').read_text()
            x=[s for s in before.splitlines() if re.search(pat,s)];y=[s for s in after.splitlines() if re.search(pat,s)]
            assert x==y,(name,x,y)
            assert after.splitlines()[-1].startswith('ALL ')
            emit(f'prior_{name}_rerun exact_lines_compared={len(x)} identical=True completed=True')
        for g in [1,2]:
            H,co=brute9(g);d=2*g+1
            exact=[F(1)]+[F(int(raw_series(9,n,d)[0][d]),H) for n in [1,2]]
            assert co==exact
            emit(f'independent_F9 g={g} D_degree={d} squarefree_count={H} direct_Euler_coefficients={co} agrees_dual=True')
        # Independently rerun optimized reductions against the unoptimized saved series.
        rows=(HERE/'output_dual_validation.txt').read_text().splitlines()
        checked=0
        for i,line in enumerate(rows):
            z=re.match(r'q (\d+) m (\d+) saved_matches',line)
            if not z:continue
            q,m=map(int,z.groups());want=ast.literal_eval(rows[i+1].removeprefix('series '))
            got=raw_series(q,2*m,len(want)-1)[0]
            assert [int(got[j]) for j in range(len(want))]==want,(q,m)
            checked+=1
        emit(f'optimized_dual_vs_original_dual_series={checked} exact_full_series_agreements=True')
        for q,d in [(3,7),(3,8),(5,5),(7,5)]:
            K=field(q);count=0
            for h in monics(q,d):
                if any(e!=1 for _,e in K.factors(h)):continue
                assert K.primitive_L(h)==old.quadratic_L(q,h)
                count+=1
                if count==100:break
            emit(f'primitive_L_Euler_vs_direct_Jacobi q={q} degree={d} checked={count} exact=True')
        checked=0
        for q,n in [(3,1),(3,3),(3,5),(3,7),(5,3),(5,5)]:
            c,_=raw_series(q,n,12)
            for d in [8,10,12]:
                sq,ns=old.a2_coefficient(q,d,n)
                assert F(int(c[d]),q**d-q**(d-1))==sq+ns,(q,n,d)
                checked+=1
        emit(f'odd_raw_scaling_cancellation_vs_original_A2={checked} exact=True')
        caches={int(p.stem.split('_m')[1]):json.loads(p.read_text()) for p in HERE.glob('series_q3_m*.json')}
        checks=0
        for m,c in sorted(caches.items()):
            assert c[0]==3**(2*m) and all(x==0 for x in c[1:2*m+1])
            for g in range(m,2*m):
                d=2*g+1
                if d>=len(c):continue
                low=g-m
                target=2*3**(2*g) if low==0 else caches[low][d]
                assert c[d]==3**(2*m-g)*target,(m,g)
                checks+=1
        emit(f'large_series_full_family_functional_equation_checks={checks} all=True; degree_vanishing_all=True')
        for p in HERE.rglob('*.py'):ast.parse(p.read_text(),filename=str(p))
        emit('ALL PRIOR EXACT OUTPUTS REPRODUCED; F9 DIRECT ENUMERATION AGREES; ALL SOURCES PARSE.')
if __name__=='__main__':main()
