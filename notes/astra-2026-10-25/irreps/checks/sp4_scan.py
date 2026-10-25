#!/usr/bin/env python3
"""Cycle expansion for conformal Sp4, proved in astra-proofs.md §3."""
import sys
sys.dont_write_bytecode=True
from functools import lru_cache
import argparse,re
from pathlib import Path
import sympy as s
import networkx as nx
from irreps_scan import matching_dp,graph,cycles,x,report

def sp4_cycle(G):
    G=nx.convert_node_labels_to_integers(G)
    masks=[sum(1<<v for v in c) for c in cycles(G)]
    @lru_cache(None)
    def rem(mask):return matching_dp(G.subgraph([v for v in G if not mask>>v&1]),4)
    p=s.Poly(0,x)
    def rec(start,mask):
        nonlocal p
        p+=rem(mask)
        for j in range(start,len(masks)):
            if not mask&masks[j]:rec(j+1,mask|masks[j])
    rec(0,0)
    return p

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--atlas',type=int,default=0);ap.add_argument('--summarize',nargs='+');args=ap.parse_args()
    if args.summarize:
        for filename in args.summarize:
            raw=Path(filename).read_text()
            counts=re.findall(r'real_count= (\d+) degree= (\d+)',raw)
            print(filename,'completed_graphs=',len(counts),'all_real=',all(a==b for a,b in counts),'completed_scan=',raw.rstrip().endswith('DONE exact cycle formula scan.'))
        return
    cases=[('K5',nx.complete_graph(5)),('K33',graph('K33')),('cube',graph('cube')),('Petersen',graph('Petersen'))]
    if args.atlas:
        cases=[(f'atlas_{i}',G) for i,G in enumerate(nx.graph_atlas_g()) if 3<=len(G)<=args.atlas and nx.is_connected(G) and G.number_of_edges()>=len(G)]
    for name,G in cases:
        print('\nGRAPH',name,'nodes=',len(G),'edges=',list(G.edges()),flush=True)
        p=sp4_cycle(G)
        # Sturm total with multiplicity; no decimal root finder.
        real=sum(m for _,m in s.polys.polytools.intervals(p))
        print('Phi=',p.as_expr(),'real_count=',real,'degree=',p.degree(),flush=True)
        if real!=p.degree():
            print('COUNTEREXAMPLE',name,flush=True)
            if args.atlas:return
    print('DONE exact cycle formula scan.',flush=True)

if __name__=='__main__':main()
