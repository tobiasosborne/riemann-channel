#!/usr/bin/env python3
"""Exact exterior-kernel contraction for U(1)Sp(4), also U(2) Sym^3.
Lambda^2 C4 = C J + W5. Its kernel is P1 tensor P1 + P5 tensor P5/5.
Other exterior powers are irreducible, and scalar weights separate degrees.
No sampling, interpolation, or raw finite-design substitution.
"""
import sys
sys.dont_write_bytecode=True
from functools import lru_cache
from fractions import Fraction as Q
from itertools import combinations
import sympy as s
import networkx as nx
from irreps_scan import matching_dp,graph,report,x

subs={k:list(combinations(range(4),k)) for k in range(5)}
J=[(0,1),(2,3)]

def sign(seq):return (-1)**sum(seq[i]>seq[j] for i in range(4) for j in range(i+1,4))

@lru_cache(None)
def vertex(types):
    # types=(k, whether endpoint matrix is P_J); I otherwise.
    degree=sum(k for k,p in types)
    if degree>4:return Q(0)
    ans=Q(0)
    def rec(j,rows,cols,ur,uc,weight):
        nonlocal ans
        if j==len(types):
            if ur!=uc:return
            free=tuple(i for i in range(4) if i not in ur)
            ans+=weight*sign(free+rows)*sign(free+cols)
            return
        k,p=types[j]
        for R in J if p else subs[k]:
            if set(R)&ur:continue
            for C in J if p else [R]:
                if set(C)&uc:continue
                rec(j+1,rows+R,cols+C,ur|set(R),uc|set(C),weight*(Q(1,2) if p else 1))
    rec(0,(),(),set(),set(),Q(1))
    return ans

# Terms (k, endpoint-a projector flag, endpoint-b projector flag, coefficient).
EDGE=[(0,0,0,Q(1)),(1,0,0,Q(1,4)),(3,0,0,Q(1,4)),(4,0,0,Q(1)),
      (2,0,0,Q(1,5)),(2,0,1,Q(-1,5)),(2,1,0,Q(-1,5)),(2,1,1,Q(6,5))]

def average(G,p1=False):
    G=nx.convert_node_labels_to_integers(G);n=len(G);edges=sorted(G.edges());loads=[0]*n;types=[[] for _ in G];tot={}
    choices=[(k,0,0,Q(1,int(s.binomial(4,k)))) for k in range(5)] if p1 else EDGE
    def rec(j,K,weight):
        if j==len(edges):
            for ts in types:
                weight*=vertex(tuple(sorted(ts)))
                if not weight:return
            deg=4*n-2*K;tot[deg]=tot.get(deg,Q(0))+(-1)**K*weight
            return
        u,v=edges[j]
        for k,a,b,c in choices:
            if loads[u]+k>4 or loads[v]+k>4:continue
            loads[u]+=k;loads[v]+=k;types[u].append((k,a));types[v].append((k,b))
            rec(j+1,K+k,weight*c)
            loads[u]-=k;loads[v]-=k;types[u].pop();types[v].pop()
    rec(0,0,Q(1))
    return s.Poly(sum(s.Rational(c.numerator,c.denominator)*x**i for i,c in tot.items()),x)

def main():
    for name,G in [('path3',nx.path_graph(3)),('C3',graph('C3')),('C4',nx.cycle_graph(4)),('K4',graph('K4')),('diamond',nx.complete_graph(4))]:
        if name=='diamond':G.remove_edge(0,1)
        print('\nGRAPH',name,flush=True)
        p=average(G);mu=matching_dp(G,4)
        assert average(G,p1=True)==mu
        if name=='path3':assert p==s.Poly((x**3-2*x)**4,x)
        if name in ['C3','C4']:
            D=2*s.chebyshevt(len(G),x/2)
            assert p==s.Poly((D**2-1)*(D**2-2),x)
        print('mu4=',mu.as_expr(),flush=True)
        report(p,1 if name in ['C3','C4'] else 2,mu)
    print('PASS tree, cycle Gram and P1 contraction controls.',flush=True)

if __name__=='__main__':main()
