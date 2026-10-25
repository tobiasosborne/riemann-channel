#!/usr/bin/env python3
"""Exact averages on C3, K4, K33, cube, Petersen.

New SU(d) saturated-cycle contraction, independent matching DP, and exact A4
finite sums for SO3. Q8/2T/2O use the proved common exterior kernels; S3/S4,
O(d), scalar and specified U2 irreps use the proved P1 kernels. No finite
unitary-design claim is made. Root verdicts use rational Sturm isolation.
Lane H modules are read-only inputs, imported without bytecode writes.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,json,itertools,time
from functools import lru_cache
from fractions import Fraction
from math import factorial
import sympy as sp
import networkx as nx
ROOT=Path(__file__).resolve().parents[3]
H=ROOT/'astra-2026-10-23'/'haar'/'checks'
sys.path.insert(0,str(H))
from haar_common import graph,cycles,su2_average
from haar_finite import so3_average_exact
x=sp.Symbol('x')

# Independent vertex-elimination capacity DP for HPS multiplicity formula.
def matching_dp(G,d):
    nodes=sorted(G);idx={v:i for i,v in enumerate(nodes)};n=len(nodes)
    adj=[sorted(idx[w] for w in G[v] if idx[w]>i) for i,v in enumerate(nodes)]
    falling=[factorial(d)//factorial(d-k) for k in range(d+1)]
    @lru_cache(None)
    def rec(v,loads):
        if v==n:return (Fraction(1),)
        out={}
        def choose(j,left,ls,k,den):
            if j==len(adj[v]):
                fac=Fraction(falling[d-left],den)
                tail=rec(v+1,tuple(ls[1:]))
                for a,c in enumerate(tail):out[k+a]=out.get(k+a,0)+fac*c
                return
            w=adj[v][j];p=w-v
            for r in range(min(left,d-ls[p])+1):
                ls[p]+=r
                choose(j+1,left-r,ls,k+r,den*factorial(r)*falling[r])
                ls[p]-=r
        choose(0,d-loads[0],list(loads),0,1)
        return tuple(out.get(k,Fraction(0)) for k in range(max(out)+1))
    co=rec(0,(0,)*n)
    return sp.Poly(sum((-1)**k*sp.Rational(c.numerator,c.denominator)*x**(n*d-2*k) for k,c in enumerate(co)),x)

def sud_average(G,d):
    cs=cycles(G);masks=[sum(1<<v for v in c) for c in cs]
    @lru_cache(None)
    def remainder(mask):
        return matching_dp(G.subgraph([v for v in G if not mask>>v&1]),d)
    out=sp.Poly(0,x);counts={}
    def rec(start,mask,c):
        nonlocal out
        out+=remainder(mask).mul_ground((2*(-1)**d)**c)
        counts[c]=counts.get(c,0)+1
        for j in range(start,len(cs)):
            if not(mask&masks[j]):rec(j+1,mask|masks[j],c+1)
    rec(0,0,0)
    return out,counts

def report(p,q,ref):
    intervals=sp.polys.polytools.intervals(p,eps=sp.Rational(1,10**16))
    real=sum(m for _,m in intervals);inside=0
    # Exact endpoints +/-sqrt(4q); boundary roots handled symbolically.
    boundary=sp.Poly(x*x-4*q,x)
    for (a,b),m in intervals:
        if max(a*a,b*b)<=4*q:inside+=m
        elif p.rem(boundary).is_zero and (a*a-4*q)*(b*b-4*q)<=0:inside+=m
    row={'degree':p.degree(),'real':real,'in_band':inside,'real_rooted':real==p.degree(),
         'all_in_band':inside==p.degree(),'equals_mu_d':p==ref,'coefficients':[str(c) for c in p.all_coeffs()]}
    print('Phi =',p.as_expr(),flush=True)
    print('EXACT', {k:v for k,v in row.items() if k!='coefficients'},flush=True)
    return row

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--graphs',nargs='+',default=['C3','K4','K33','cube','Petersen']);args=ap.parse_args()
    print('Exact rational arithmetic; rational Sturm isolation; no RH assumed.',flush=True)
    records={}
    old=json.loads((H/'output_finite.json').read_text())
    for name in args.graphs:
        t0=time.monotonic();G=graph(name);q=next(iter(dict(G.degree()).values()))-1
        print('\nGRAPH',name,'n=',len(G),'m=',G.number_of_edges(),'g=',G.number_of_edges()-len(G)+1,'q=',q,flush=True)
        records[name]={};mu={d:matching_dp(G,d) for d in [1,2,3]}
        cases=[('nontrivial U1, ZN(N>=2), Sn sign',1,mu[1]),
               ('U2 defining; S3 standard; dihedral irreducible doublets; twisted 2T',2,mu[2]),
               ('U3; O3; S4 standard; U2 det^a Sym2 (a!=-1)',3,mu[3])]
        su2,counts=sud_average(G,2)
        assert su2==su2_average(G)[0]
        cases.append(('SU2 doublet; Q8; untwisted 2T; defining 2O',2,su2))
        su3,counts3=sud_average(G,3)
        print('Unoriented vertex-disjoint cycle-collection counts by size:',counts3,flush=True)
        cases.append(('SU3 defining',3,su3))
        so3=so3_average_exact(G)
        cases.append(('SO3; SU2 spin1; A5 both triples; S4 standard times sign',3,so3))
        for label,d,p in cases:
            print('\nREP',label,flush=True);records[name][label]=report(p,q,mu[d])
        if name in old:
            for key,p in [('SU2-half',su2),('U2',mu[2]),('SU2-spin1',so3)]:
                assert [str(c) for c in p.all_coeffs()]==old[name][key]
            print('Lane H saved finite coefficients reproduced exactly for all three families.',flush=True)
        if name=='C3':
            D=x**3-3*x
            assert mu[3]==sp.Poly(D**3-2*D,x)
            assert su3==sp.Poly(D**3-2*D-2,x)
            assert so3==sp.Poly(D**3-2*D-4,x)
        print('elapsed_seconds=',round(time.monotonic()-t0,3),flush=True)
        filename='output_scan.json' if args.graphs==['C3','K4','K33','cube','Petersen'] else 'output_scan_'+'_'.join(args.graphs)+'.json'
        Path(__file__).with_name(filename).write_text(json.dumps(records,indent=2)+'\n')
    print('\nPASS exact comparisons and all asserted polynomial identities.',flush=True)

if __name__=='__main__':main()
