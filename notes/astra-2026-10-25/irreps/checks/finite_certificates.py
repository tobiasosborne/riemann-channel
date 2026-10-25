#!/usr/bin/env python3
"""Independent exact finite sums: S4 triples and Delta(27) <= SU3.

Delta27 is NOT asserted to be a raw unitary design. Its exterior powers are
(1,V,V*,1), with V,V* distinct irreducibles, exactly the SU3 kernels.
Cyclotomic arithmetic Q(omega) is implemented by integer restriction of
scalars. Each Hermitian characteristic polynomial is rational integral;
its restriction is its square, verified exactly for every summand.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import itertools
import numpy as np
import sympy as sp
import flint
from irreps_scan import matching_dp,sud_average,graph,x
H=Path(__file__).resolve().parents[3]/'astra-2026-10-23'/'haar'/'checks'
sys.path.insert(0,str(H))
from haar_common import tree_edges
from haar_finite import so3_average_exact


def s4_mats(twist):
    mats=[]
    for p in itertools.permutations(range(4)):
        sign=(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        M=np.zeros((3,3),dtype=int)
        for j in range(3):
            v=np.zeros(4,dtype=int);v[p[j]]+=1;v[p[3]]-=1
            M[:,j]=v[:3]*(sign if twist else 1)
        mats.append(M)
    return mats


def group_data(mats):
    keys={tuple(M.flat):i for i,M in enumerate(mats)}
    identity=keys[tuple(np.eye(len(mats[0]),dtype=int).flat)]
    mult=[[keys[tuple((M@N).flat)] for N in mats] for M in mats]
    inv=[row.index(identity) for row in mult]
    conj=[[mult[mult[s][a]][inv[s]] for a in range(len(mats))] for s in range(len(mats))]
    return inv,conj


def orbit_tuples(conj,g):
    size=len(conj)
    def rec(ids,stab,w):
        if len(ids)==g:
            yield ids,w;return
        unseen=set(range(size))
        while unseen:
            a=min(unseen);orb={conj[s][a] for s in stab};unseen-=orb
            yield from rec(ids+[a],[s for s in stab if conj[s][a]==a],w*len(orb))
    yield from rec([],list(range(size)),1)


def sqrt_monic_integer(high):
    d=(len(high)-1)//2;r=[1]
    for k in range(1,d+1):
        a=high[k]-sum(r[j]*r[k-j] for j in range(1,k))
        assert a%2==0;r.append(a//2)
    # FLINT polynomial square certificate, at every tuple.
    assert flint.fmpz_poly(r[::-1])**2==flint.fmpz_poly(high[::-1])
    return r[::-1]


def finite_average(G,mats,restrict_degree=1):
    inv,conj=group_data(mats);tree,cot=tree_edges(G);d=len(mats[0]);n=len(G)
    A=np.zeros((n*d,n*d),dtype=int)
    for u,v in tree:
        A[d*u:d*(u+1),d*v:d*(v+1)]=np.eye(d,dtype=int)
        A[d*v:d*(v+1),d*u:d*(u+1)]=np.eye(d,dtype=int)
    total=[0]*(n*d//restrict_degree+1);weight=terms=0
    for ids,w in orbit_tuples(conj,len(cot)):
        for (u,v),a in zip(cot,ids):
            A[d*u:d*(u+1),d*v:d*(v+1)]=mats[a]
            A[d*v:d*(v+1),d*u:d*(u+1)]=mats[inv[a]]
        co=list(map(int,flint.fmpz_mat(A.tolist()).charpoly().coeffs()))
        if restrict_degree==2:co=sqrt_monic_integer(co[::-1])
        for i,c in enumerate(co):total[i]+=w*c
        weight+=w;terms+=1
    assert weight==len(mats)**len(cot)
    print('group_order=',len(mats),'orbit_reps=',terms,'weight=',weight,flush=True)
    return sp.Poly(sum(sp.Rational(c,weight)*x**i for i,c in enumerate(total)),x)


def delta27_mats():
    omega=np.array([[0,-1],[1,-1]],dtype=int)
    powers=[np.eye(2,dtype=int),omega,omega@omega]
    mats=[]
    for r,a,b in itertools.product(range(3),repeat=3):
        M=np.zeros((6,6),dtype=int)
        for j in range(3):M[2*((j+r)%3):2*((j+r)%3)+2,2*j:2*j+2]=powers[(a*j+b)%3]
        mats.append(M)
    return mats


def main():
    G=graph('K4')
    for twist in [False,True]:
        p=finite_average(G,s4_mats(twist))
        target=so3_average_exact(G) if twist else matching_dp(G,3)
        assert p==target
        print('S4 standard twist_by_sign=',twist,'Phi=',p.as_expr(),flush=True)
    for name in ['C3','K4']:
        G=graph(name);p=finite_average(G,delta27_mats(),2)
        assert p==sud_average(G,3)[0]
        print('Delta27=SU3 on',name,'Phi=',p.as_expr(),flush=True)
    print('PASS independent exact finite sums; every cyclotomic restriction square verified.',flush=True)

if __name__=='__main__':main()
