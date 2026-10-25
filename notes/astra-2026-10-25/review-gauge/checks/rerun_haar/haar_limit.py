#!/usr/bin/env python3
"""Exact fixed root moments approaching tree moments; supplemental H3 check."""
from haar_common import graph, matching_d, x, root_report
import sympy as sp
import json
from pathlib import Path

def root_moments(p, maxk):
    n=p.degree();c=p.all_coeffs();s=[sp.Integer(n)]
    for k in range(1,maxk+1):
        v=sum(c[j]*s[k-j] for j in range(1,min(k,n+1)))
        if k<=n:v+=k*c[k]
        s.append(-v)
    return [v/n for v in s]

def tree_moments(degree, maxk):
    counts={0:1};out=[1]
    for k in range(1,maxk+1):
        nxt={}
        for r,c in counts.items():
            nxt[r+1]=nxt.get(r+1,0)+c*(degree if r==0 else degree-1)
            if r:nxt[r-1]=nxt.get(r-1,0)+c
        counts=nxt;out.append(counts.get(0,0))
    return out

def main():
    ks=[2,4,6,8,10,12];tree=tree_moments(3,12)
    print('EXACT root moments of p_K4,U(d), orders',ks)
    print('3-regular tree:',[tree[k] for k in ks])
    for d in [1,2,4,8,16]:
        p=matching_d(graph('K4'),d);mom=root_moments(p,12)
        print('d=',d,'degree=',p.degree(),'moments=',[mom[k] for k in ks],flush=True)
        assert mom[2]==3 and mom[4]==15 and mom[6]==87-sp.Rational(6,d)
    p=matching_d(graph('Petersen'),3)
    root_report(p,2,'Petersen U3 exact HPS 3-matching')
    Path(__file__).with_name('output_limit.json').write_text(json.dumps({'Petersen':{'U3':[str(c) for c in p.all_coeffs()]}},indent=2)+'\n')
    print('PASS: moment identities and exact real-root isolation; convergence itself is proved in astra-proofs.md.')

if __name__=='__main__':main()
