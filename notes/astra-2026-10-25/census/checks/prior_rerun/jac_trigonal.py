#!/usr/bin/env python3
"""Independent exhaustive targeted genus-4 nonhyperelliptic check over F2.

Every canonical model is Q=C=0 in P3, with Q one of the three printed
quadrics. Cubics modulo Q times linear forms form a 16-dimensional F2
space. A Walsh transform computes exact point counts of all 65536 cubics
on each quadric, without smoothness assumptions. For a target match only,
the Jacobian criterion on all four affine charts certifies smoothness by
Groebner basis over F2 (unit ideal). This is NOT a classification of lattices.
"""
import contextlib
import itertools
from pathlib import Path
import json
import numpy as np
import sympy as S
from jac_hyperelliptic import F2Field

HERE=Path(__file__).resolve().parent
X=S.symbols('X Y Z T')
MON=[a for a in itertools.product(range(4),repeat=4) if sum(a)==3]
QUAD=[[(1,1,0,0),(0,0,1,1)],
      [(1,1,0,0),(0,0,2,0),(0,0,1,1),(0,0,0,2)],
      [(1,1,0,0),(0,0,2,0)]]

def expression(monomials):
    return sum(S.prod(x**a for x,a in zip(X,m)) for m in monomials)

def cubic_basis(Q):
    rows=[]
    for j in range(4):
        ms=[tuple(a+(i==j) for i,a in enumerate(m)) for m in Q]
        v=sum(1<<MON.index(m) for m in ms)
        for r in rows: v=min(v,v^r)
        assert v
        rows.append(v); rows.sort(reverse=True)
    pivots={v.bit_length()-1 for v in rows}
    return [m for i,m in enumerate(MON) if i not in pivots]

def projective_points(q):
    for first in range(4):
        for tail in itertools.product(range(q),repeat=3-first):
            yield (0,)*first+(1,)+tail

def evaluate(m,pt,field):
    a=1
    for v,e in zip(pt,m): a=field.mul(a,field.power(v,e))
    return a

def xor_sum(values):
    a=0
    for v in values: a^=v
    return a

def all_counts(Q,basis,k):
    field=F2Field(k); size=1<<len(basis)
    wt=np.zeros(size,dtype=np.int64); surface=0
    for pt in projective_points(field.q):
        if xor_sum(evaluate(m,pt,field) for m in Q): continue
        surface+=1
        vals=[evaluate(m,pt,field) for m in basis]
        # Each coordinate in F_{2^k} gives one binary linear condition.
        rows=[sum(1<<i for i,v in enumerate(vals) if v>>j&1) for j in range(k)]
        span={0}
        for r in rows: span|={v^r for v in tuple(span)}
        factor=(1<<k)//len(span)
        for v in span: wt[v]+=factor
    stride=1
    while stride<size:
        blocks=wt.reshape(-1,2*stride)
        a=blocks[:,:stride].copy(); b=blocks[:,stride:].copy()
        blocks[:,:stride]=a+b; blocks[:,stride:]=a-b
        stride*=2
    assert np.all(wt%(1<<k)==0)
    result=wt//(1<<k)
    assert result[0]==surface
    return result,surface

def smooth(Q,C):
    minors=[S.diff(Q,X[i])*S.diff(C,X[j])-S.diff(Q,X[j])*S.diff(C,X[i])
            for i in range(4) for j in range(i+1,4)]
    for j in range(4):
        polys=[S.Poly(f.subs(X[j],1),*[v for i,v in enumerate(X) if i!=j],modulus=2).as_expr()
               for f in [Q,C]+minors]
        gb=S.groebner(polys,*[v for i,v in enumerate(X) if i!=j],modulus=2)
        if list(gb)!=[1]: return False
    return True

def main():
    target=[3,9,9,29]; hits=[]
    for qi,Q in enumerate(QUAD,1):
        basis=cubic_basis(Q); assert len(basis)==16
        keep=np.ones(1<<16,dtype=bool)
        print(f'Q{qi}={expression(Q)} cubic quotient dimension={len(basis)}',flush=True)
        for k,N in enumerate(target,1):
            count,surface=all_counts(Q,basis,k)
            keep &= count==N
            print(f'  k={k} quadric_points={surface}; target={N}; surviving cubic classes={int(keep.sum())}',flush=True)
        masks=np.nonzero(keep)[0].tolist()
        for mask in masks:
            C=expression([m for i,m in enumerate(basis) if mask>>i&1])
            ok=smooth(expression(Q),C)
            if ok: hits.append(dict(quadric=qi,mask=mask,Q=str(expression(Q)),C=str(C),counts=target))
        print(f'  smooth matches={sum(h["quadric"]==qi for h in hits)}',flush=True)
    print('TOTAL smooth canonical equations='+str(len(hits)))
    if hits: print('WITNESS '+str(hits[0]))
    (HERE/'output_trigonal.json.txt').write_text(json.dumps(hits,indent=2)+'\n')

if __name__=='__main__':
    with (HERE/'output_trigonal.txt').open('w') as f,contextlib.redirect_stdout(f): main()
    print((HERE/'output_trigonal.txt').read_text())
