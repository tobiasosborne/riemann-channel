#!/usr/bin/env python3
"""Extra genus-six test of J2'': the triangular prism, and an explicit witness.
All finite-field calculations (including log/exp lookup tables) are exact.
"""
import json
from collections import deque
import networkx as nx
import numpy as np
import sympy as S
from census_lookup import HERE,SOURCE,label_from_coeff,counts_from_coeff,coeff_from_counts
from lowgenus import Field

def enumerate_prism():
    G=nx.circular_ladder_graph(3);edges=sorted(tuple(sorted(e)) for e in G.edges())
    tree=list(nx.bfs_edges(G,0));tree_set={tuple(sorted(e)) for e in tree}
    cot=[e for e in edges if e not in tree_set]
    autos=list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
    def matrix(mask):
        A=S.zeros(6)
        for e in edges:A[e[0],e[1]]=A[e[1],e[0]]=-1 if e in cot and mask>>cot.index(e)&1 else 1
        return A
    def normalize(A):
        gauge={0:1}
        for a,b in tree:gauge[b]=gauge[a]*int(A[a,b])
        return sum(1<<j for j,(a,b) in enumerate(cot) if gauge[a]*gauge[b]*A[a,b]<0)
    labels={line.split('|')[0] for line in (SOURCE/'lmfdbgenus6_curves_F2.txt').read_text().splitlines()}
    print('PRISM edges',edges,'BFS tree',tree,'cotree',cot,'automorphisms',len(autos),flush=True)
    remaining=set(range(16));rows=[];x,t=S.symbols('x T')
    while remaining:
        mask=min(remaining);A=matrix(mask)
        orbit={normalize(A.extract([a[i] for i in range(6)],[a[i] for i in range(6)])) for a in autos}
        remaining-=orbit
        minors=[int((8*S.eye(6)-A*A)[:i,:i].det()) for i in range(1,7)]
        if not all(m>0 for m in minors):continue
        chi=A.charpoly(x).as_expr();P=S.Poly(S.cancel(t**6*chi.subs(x,(1+2*t*t)/t)),t)
        c=[int(P.nth(i)) for i in range(13)];N=counts_from_coeff(c,31)
        aa=[sum(int(S.mobius(k//d))*N[d-1] for d in S.divisors(k))//k for k in range(1,32)]
        lab=label_from_coeff(c)
        r=dict(mask=mask,orbit=sorted(orbit),A=[[int(v) for v in row] for row in A.tolist()],band_minors=minors,real_polynomial=str(S.factor(chi)),
               coeff=c,label=lab,N=N,closed_points=aa,p_rank=max(i for i,v in enumerate(c) if v%2),
               verdict='YES' if lab in labels else 'NO',negative_closed=[(k,a) for k,a in enumerate(aa,1) if a<0])
        print('ORBIT',json.dumps(r),flush=True);rows.append(r)
    return rows

def witness_counts():
    out=[]
    for k in range(1,13):
        F=Field(k);order=F.q-1;primes=list(S.factorint(order))
        generator=next(a for a in range(1,F.q) if all(F.power(a,order//int(p))!=1 for p in primes))
        exp=np.zeros(2*order,dtype=np.int32);log=np.zeros(F.q,dtype=np.int32);v=1
        for i in range(order):exp[i]=v;log[v]=i;v=F.mul(v,generator)
        assert v==1 and len(set(exp[:order]))==order
        exp[order:]=exp[:order]
        y=np.arange(F.q,dtype=np.int32)
        def mulsc(a,arr):
            if not a:return np.zeros_like(arr)
            vals=exp[log[a]+log[arr]].copy();vals[arr==0]=0;return vals
        y2=exp[(2*log[y])%order].copy();y2[0]=0
        y4=exp[(4*log[y])%order].copy();y4[0]=0
        y5=exp[(5*log[y])%order].copy();y5[0]=0
        affine=0
        for x in range(F.q):
            x2=F.mul(x,x);x4=F.mul(x2,x2);x5=F.mul(x4,x)
            vals=y5^y4^mulsc(x^1,y2)^mulsc(x4^x2^1,y)^(x5^x2)
            affine+=int(np.count_nonzero(vals==0))
        infinity=int(np.count_nonzero((1^y^y5)==0))
        out.append(affine+infinity)
        print('PRISM WITNESS k',k,'affine',affine,'infinity',infinity,'N',out[-1],flush=True)
    return out

def main():
    rows=enumerate_prism()
    x,y,z=S.symbols('X Y Z')
    f=x**5+x**4*y+y**5+y**4*z+x*x*y*z*z+x*y*y*z*z+x*x*z**3+y*y*z**3+y*z**4
    for var in [x,y,z]:
        vs=[v for v in [x,y,z] if v!=var];ff=f.subs(var,1)
        assert list(S.groebner([ff]+[S.diff(ff,v) for v in vs],*vs,modulus=2))==[1]
    print('PRISM plane quintic geometric smoothness: 3 unit Groebner ideals; genus=(5-1)(5-2)/2=6',flush=True)
    N=witness_counts();r=next(r for r in rows if r['mask']==6)
    assert N==r['N'][:12] and coeff_from_counts(N[:6])==r['coeff']
    print('PRISM witness polynomial',r['coeff'],'label',r['label'],'2-rank',r['p_rank'],flush=True)
    (HERE/'output_prism.json.txt').write_text(json.dumps(dict(orbits=rows,witness=str(f),counts=N),indent=2)+'\n')

if __name__=='__main__':main()
