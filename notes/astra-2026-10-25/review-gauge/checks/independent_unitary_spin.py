#!/usr/bin/env python3
"""Independent differential-operator, line-graph, and Sym^3 checks."""
from collections import defaultdict
from math import comb, factorial, sqrt
import itertools as it
import json
from pathlib import Path
import flint
import mpmath as mp
import networkx as nx
import numpy as np
import sympy as s
x=s.Symbol('x')

def differential_average(G,d):
    # Apply product_e sum_k (-D_u D_v)^k/[k! (d)_k] to product_v z_v^d.
    # As soon as z_v is no longer differentiated, substitute z_v=x.
    # This computes by vertex elimination and coalesces monomials; no edge-
    # multiplicity tuples or lane functions are enumerated.
    fall=lambda a,k: factorial(a)//factorial(a-k)
    states={((d,)*len(G),0):flint.fmpq(1)}
    for u in range(len(G)):
        for v in sorted(w for w in G[u] if w>u):
            nxt=defaultdict(flint.fmpq)
            for (powers,deg),c in states.items():
                for k in range(min(powers[0],powers[v-u])+1):
                    pp=list(powers);pp[0]-=k;pp[v-u]-=k
                    w=flint.fmpq((-1)**k*fall(powers[0],k)*fall(powers[v-u],k),factorial(k)*fall(d,k))
                    nxt[tuple(pp),deg]+=c*w
            states=dict(nxt)
        nxt=defaultdict(flint.fmpq)
        for (powers,deg),c in states.items():nxt[powers[1:],deg+powers[0]]+=c
        states=dict(nxt)
        print('differential elimination vertex',u,'states',len(states),flush=True)
    p=s.Poly(sum(s.Rational(str(c))*x**deg for (powers,deg),c in states.items()),x)
    print('Petersen U3 differential polynomial:',p.as_expr(),flush=True)
    intervals=s.polys.polytools.intervals(p,eps=s.Rational(1,10**35))
    assert len(intervals)==30 and all(m==1 and max(a*a,b*b)<8 for (a,b),m in intervals)
    a,b=intervals[-1][0]
    print('Petersen U3 largest root rational interval:',a,b)
    print('Petersen U3 largest root midpoint:',s.N((a+b)/2,35))
    expected=json.loads(Path(__file__).with_name('rerun_haar').joinpath('output_limit.json').read_text())['Petersen']['U3']
    assert [str(c) for c in p.all_coeffs()]==expected

def sixth_moment():
    d=s.symbols('d',positive=True,integer=True);N=4*d;M=6*d;r=3
    C=lambda z,k:s.sympify(s.prod(z-j for j in range(k)))/factorial(k)
    # m3 = #independent triples in the line graph. A line-graph triangle
    # comes from either a 3-star or a base triangle. Every base triangle
    # has expected one closed lift, hence E triangles=4, for every d.
    m1=M;m2=C(M,2)-N*C(r,2)
    m3=C(M,3)-N*C(r,2)*(M-2)+M*C(2*(r-1),2)-N*C(r,3)-4
    p2=2*m1;p4=s.expand(m1*p2-4*m2)
    p6=s.expand(m1*p4-m2*p2+6*m3)
    ans=s.simplify(p6/N)
    print('K4 U(d) sixth normalized moment from line-graph independent triples:',ans)
    print('K4 U16 sixth normalized moment:',ans.subs(d,16))
    assert ans==87-6/d and ans.subs(d,16)==s.Rational(693,8)

def exact_spin_triangle():
    t,D=s.symbols('t D')
    raw=s.Poly((D-t)**2*(D-(t**3-3*t))**2,t)
    avg=0
    for (k,),c in raw.terms():
        if k%2==0:avg+=c*s.catalan(k//2)
    p=s.Poly(s.expand(avg.subs(D,x**3-3*x)),x)
    print('C3 spin 3/2 exact SU2 Weyl integration:',p.as_expr())
    print('C3 spin 3/2 polynomial in D=x^3-3x:',s.expand(avg))
    print('C3 spin 3/2 exact real-root count:',s.polys.polytools.count_roots(p,-s.oo,s.oo))
    roots=s.nroots(p,n=30,maxsteps=1000)
    print('C3 spin 3/2 roots:',[str(z) for z in roots])

def sym3(U):
    out=np.zeros(U.shape[:-2]+(4,4),complex)
    for k,l in it.product(range(4),repeat=2):
        for a in range(4-l):
            b=k-a
            if 0<=b<=l:
                out[...,k,l]+=sqrt(comb(3,l)/comb(3,k))*comb(3-l,a)*comb(l,b)*U[...,0,0]**(3-l-a)*U[...,1,0]**a*U[...,0,1]**(l-b)*U[...,1,1]**b
    return out

def spin_k4(samples=100000):
    rng=np.random.default_rng(20261025);n=16
    total=np.zeros(n+1,dtype=np.longdouble);total2=total.copy();halves=[]
    max_pair_gap=0.;max_unitarity=0.
    for step in range(samples//1000):
        z=rng.normal(size=(1000,3,4));z/=np.linalg.norm(z,axis=-1,keepdims=True)
        a,b,c,e=np.moveaxis(z,-1,0);U=np.empty((1000,3,2,2),complex)
        U[...,0,0]=a+1j*b;U[...,0,1]=c+1j*e;U[...,1,0]=-c+1j*e;U[...,1,1]=a-1j*b
        V=sym3(U);max_unitarity=max(max_unitarity,float(np.max(np.abs(V@V.conj().swapaxes(-1,-2)-np.eye(4)))))
        A=np.zeros((1000,16,16),complex)
        for j,(u,v) in enumerate([(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]):
            B=np.broadcast_to(np.eye(4),(1000,4,4)) if j<3 else V[:,j-3]
            A[:,4*u:4*u+4,4*v:4*v+4]=B;A[:,4*v:4*v+4,4*u:4*u+4]=B.conj().swapaxes(-1,-2)
        ev=np.linalg.eigvalsh(A);max_pair_gap=max(max_pair_gap,float(np.max(np.abs(ev[:,::2]-ev[:,1::2]))))
        coeff=np.zeros((1000,n+1),np.longdouble);coeff[:,0]=1
        for j in range(n):coeff[:,1:j+2]-=ev[:,j,None].astype(np.longdouble)*coeff[:,:j+1].copy()
        coeff[:,1::2]=0 # unbiased -I symmetry
        coeff[:,0]=1;coeff[:,2]=-24
        total+=coeff.sum(axis=0);total2+=(coeff*coeff).sum(axis=0)
        if step==samples//2000-1:halves.append(total.copy()/(samples//2))
    mean=total/samples;se=np.sqrt(np.maximum(0,(total2-samples*mean*mean)/(samples*(samples-1))))
    halves.append(2*mean-halves[0])
    print('K4 spin 3/2 NUMERICAL samples',samples,'seed 20261025; double eigensolves, longdouble coefficient accumulation')
    print('max representation unitarity residual',max_unitarity,'max Kramers pair gap',max_pair_gap)
    print('coefficients descending:',list(map(float,mean)))
    print('pointwise coefficient standard errors:',list(map(float,se)))
    roots=np.roots(np.asarray(mean,float));z=max(roots,key=lambda z:abs(z.imag))
    print('root with largest |imag|:',z)
    for j,m in enumerate(halves):
        rts=np.roots(np.asarray(m,float));print('independent half',j,'nearest root',min(rts,key=lambda w:abs(w-z)))
    print('NUMERICAL only: root estimates are not certified; quaternionic proof supplies exact non-real-root existence.')

if __name__=='__main__':
    sixth_moment();exact_spin_triangle();differential_average(nx.petersen_graph(),3);spin_k4()
