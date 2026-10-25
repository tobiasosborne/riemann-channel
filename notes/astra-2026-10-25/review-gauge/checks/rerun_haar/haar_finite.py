#!/usr/bin/env python3
"""Exact finite Haar averages via determinant-relevant exterior moments.

Q8, 2T (untwisted), 2O defining = SU2 cycle-square formula.
S3 standard, 2T two nontrivial character twists = HPS 2-matching.
A5 both 3D irreps = SO3 defining = A4 rotations: exact integer sum over
A4^g, reduced by simultaneous conjugation. No Monte Carlo or rounding.
Run: python3 checks/haar_finite.py [--graphs K4 K33 cube Petersen]
"""
import argparse
import itertools
import time
import json
from pathlib import Path
import numpy as np
import sympy as sp
import flint
from haar_common import graph, tree_edges, matching_d, su2_average, root_report, x

def a4_matrices():
    # Tetrahedral rotations: diagonal even sign changes times cyclic coordinate permutations.
    mats=[]
    for shift in range(3):
        for signs in itertools.product([1,-1],repeat=3):
            if np.prod(signs)==1:
                M=np.zeros((3,3),dtype=int)
                for j in range(3):M[(j+shift)%3,j]=signs[j]
                mats.append(M)
    assert len(mats)==12
    return mats

def orbit_tuples(mats,g):
    keys={tuple(M.flat):i for i,M in enumerate(mats)}
    conj=[[keys[tuple((S@M@S.T).flat)] for M in mats] for S in mats]
    def rec(prefix,stab,weight):
        if len(prefix)==g:
            yield prefix,weight
            return
        remaining=set(range(len(mats)))
        while remaining:
            a=min(remaining);orbit={conj[s][a] for s in stab}
            remaining-=orbit
            yield from rec(prefix+[a],[s for s in stab if conj[s][a]==a],weight*len(orbit))
    yield from rec([],list(range(len(mats))),1)

def so3_average_exact(G):
    mats=a4_matrices();tree,cot=tree_edges(G);N=3*len(G)
    A=np.zeros((N,N),dtype=int)
    for u,v in tree:
        A[3*u:3*u+3,3*v:3*v+3]=np.eye(3,dtype=int)
        A[3*v:3*v+3,3*u:3*u+3]=np.eye(3,dtype=int)
    total=[0]*(N+1);weight_sum=0;terms=0;t0=time.monotonic()
    for ids,w in orbit_tuples(mats,len(cot)):
        for (u,v),j in zip(cot,ids):
            A[3*u:3*u+3,3*v:3*v+3]=mats[j]
            A[3*v:3*v+3,3*u:3*u+3]=mats[j].T
        cp=flint.fmpz_mat(A.tolist()).charpoly().coeffs()
        for k,c in enumerate(cp):total[k]+=w*int(c)
        weight_sum+=w;terms+=1
    assert weight_sum==12**len(cot)
    print(f'A4 exact orbit reduction: {terms} representatives, weight {weight_sum}; elapsed {time.monotonic()-t0:.2f}s',flush=True)
    return sp.Poly(sum(sp.Rational(c,weight_sum)*x**i for i,c in enumerate(total)),x)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--graphs',nargs='+',default=['K4','K33','cube','Petersen'])
    args=ap.parse_args()
    print('EXACT finite sums reduced using exterior-power matrix coefficients; no assumed RH.')
    print('2T has three faithful 2D irreps: only the untwisted one has image in SU(2).')
    print('A5 two 3D irreps share exterior moment tensors with A4 rotations and SO(3).')
    records={}
    for name in args.graphs:
        G=graph(name);n=len(G);m=G.number_of_edges();g=m-n+1;q=next(iter(dict(G.degree()).values()))-1
        print(f'\nGRAPH {name}: n={n}, m={m}, g={g}, q={q}',flush=True)
        su,stats=su2_average(G)
        print('cycle census',stats)
        root_report(su,q,'Q8(2) = 2T(2,untwisted) = 2O(2,defining) = SU2(2)')
        assert stats['spanning_cycle_collections']>0
        print('EXACT positivity lower bound for all real x:',stats['spanning_cycle_collections'])
        u=matching_d(G,2)
        root_report(u,q,'S3(standard 2) = 2T(2,twist1) = 2T(2,twist2) = U2')
        so=so3_average_exact(G)
        root_report(so,q,'A5(3) = A5(3-prime) = A4(3) = SU2(spin1)')
        records[name]={kind:[str(c) for c in p.all_coeffs()] for kind,p in [('SU2-half',su),('U2',u),('SU2-spin1',so)]}
    Path(__file__).with_name('output_finite.json').write_text(json.dumps(records,indent=2)+'\n')
    print('\nPASS: all polynomials computed in exact rational arithmetic; root verdicts use rational isolation.')

if __name__=='__main__':main()
