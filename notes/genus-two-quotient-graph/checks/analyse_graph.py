#!/usr/bin/env python3
"""Author: codex:gpt-6-astra. Label cusps; certify graph and scattering."""
import sys
sys.dont_write_bytecode=True
import numpy as np
import sympy as sp
from collections import Counter
from fractions import Fraction
from pathlib import Path
from itertools import product
import enumerate_graph as eg
from graph_data import VERTICES,STABILISERS,ADJACENCY,TAILS,EDGES
x=sp.Symbol('x')
def P(a):return sp.Poly(a,x,modulus=5)
f=P(x**5+x**3+x**2-2)
def red(u,v):
    u=u.monic();v=v%u
    while u.degree()>2:u,v=((f-v*v).exquo(u)).monic(),v;v=(-v)%u
    return u,v

def add(A,B):
    u,v=A;u1,v1=B
    a,b,d=sp.gcdex(u,u1);c,e,h=sp.gcdex(d,v+v1)
    return red((u*u1).exquo(h*h),(c*a*u*v1+c*b*u1*v+e*(v*v1+f)).exquo(h))
def key(D):return tuple(tuple(int(a)%5 for a in p.all_coeffs()) for p in D)
Ds=[(P(1),P(0))]
for _ in range(14):Ds.append(add(Ds[-1],(P(x-1),P(1))))

def as_functions(g,hcol):
    n,p=g;vp=p[0][0] if p else 1000
    bounds=[min(n,vp)-n,min(n,vp,2*vp-n),-n,min(vp-n,0)]
    dims=[sum(t<=-b for t in eg.PO) if b<=0 else 0 for b in bounds]
    out=[];off=0
    for d in dims:
        a=P(0);b=P(0)
        for j in range(d):
            po=eg.PO[j];co=int(hcol[off+j])
            if po%2==0:a+=P(co*x**(po//2))
            else:b+=P(co*x**((po-5)//2))
        out.append((a,b));off+=d
    assert off==len(hcol)
    return out

def ideal_class(a,b):
    # columns of the two generators and their y-multiples over F5[x].
    gens=[a,(a[1]*f,a[0]),b,(b[1]*f,b[0])]
    w=P(0);v=P(0)
    for aa,bb in gens:
        if bb.is_zero:continue
        if w.is_zero:
            z=pow(int(bb.LC())%5,-1,5);w=bb.mul_ground(z);v=aa.mul_ground(z)
        else:
            s,t,d=sp.gcdex(w,bb);w=d;v=s*v+t*aa
    assert not w.is_zero
    u=P(0)
    for aa,bb in gens:u=sp.gcd(u,aa-bb.exquo(w)*v)
    u=u.monic();v=v%u
    U=u.exquo(w);V=-v.exquo(w)
    assert (f-V*V)%U==P(0)
    D=red(U,V)
    return next(i for i,d in enumerate(Ds) if key(d)==key(D))

def cusp_label(i):
    g=VERTICES[i];H,V=eg.hom(g,g)
    tr=(V[0]+V[3])%5
    Z=eg.nullspace(tr[None,:]);HH=H@Z%5;VV=V@Z%5
    candidates=[np.eye(HH.shape[1],dtype=np.int64)[:,j] for j in range(HH.shape[1])]
    candidates += [a+c*b for j,a in enumerate(candidates.copy()) for b in candidates[:j] for c in range(1,5)]
    for co in candidates:
        v=VV@co%5
        if (v[0]*v[3]-v[1]*v[2])%5:continue
        a,b,c,d=as_functions(g,HH@co%5)
        if any(not v.is_zero for v in a+c):return ideal_class(a,c)
        return ideal_class(b,d)
    raise AssertionError('nilpotent missing')

def main():
    labels={i:cusp_label(i) for i in TAILS}
    assert set(labels.values())==set(range(15)),labels
    print('TAIL LABELS maximal-subline a =',labels,flush=True)
    heads={a:next(iter(ADJACENCY[i])) for i,a in labels.items()}
    print('HEADS =',heads,flush=True)
    n=len(VERTICES)
    ee=Counter(EDGES)
    for i in range(n):
        deg=sum(STABILISERS[i]//s for a,b,s in EDGES if i in (a,b))
        assert deg==5 if i in TAILS else deg==6,(i,deg)
    core=[i for i in range(n) if i not in TAILS];ix={v:i for i,v in enumerate(core)}
    edges=[(a,b,s) for a,b,s in EDGES if a in ix and b in ix]
    print('CORE',len(core),'EDGES',len(edges),'MULTIPLE',sum(v-1 for v in Counter((a,b) for a,b,s in edges).values()),flush=True)
    print('STABILISER COUNTS',dict(sorted(Counter(STABILISERS[i] for i in core).items())),flush=True)
    mass=sum(Fraction(1,STABILISERS[i]) for i in core)+Fraction(15,1600)
    me=sum(Fraction(1,s) for a,b,s in edges)+Fraction(15,320)
    print('MASS',mass,'EDGE MASS',me,'EULER',mass-me,flush=True)
    assert mass==Fraction(4637,64) and me==3*mass
    A=np.zeros((len(core),len(core)),dtype=np.int64)
    for a,b,s in edges:A[ix[a],ix[b]]+=STABILISERS[a]//s;A[ix[b],ix[a]]+=STABILISERS[b]//s
    ss=np.array([STABILISERS[i] for i in core]);TX=A*np.sqrt(ss[None,:]/ss[:,None])/np.sqrt(5)
    assert np.max(abs(TX-TX.T))<1e-12
    W=np.zeros((len(core),15))
    for a,h in heads.items():W[ix[h],a]=1
    C=W@W.T
    F=np.exp(-2j*np.pi*np.arange(15)[:,None]*np.arange(15)[None,:]/15)/np.sqrt(15)
    PI=np.eye(15)[(-np.arange(15))%15]
    def Pz(t):return 1-3*t+7*t*t-15*t**3+25*t**4
    def expected(z):
        t=z*z
        m=[z**6/5*Pz(t)/Pz(t/5)*(1-t/5)/(1-5*t)]
        m += [z**6/5*(1+(1+2*np.cos(2*np.pi*k/15))*t+5*t*t)/(1+(1+2*np.cos(2*np.pi*k/15))*t/5+t*t/5) for k in range(1,15)]
        return F.conj().T@np.diag(m)@F@PI,np.array(m)
    for z in [0.3,0.6,0.8+0.2j,np.exp(0.7j)]:
        Gamma=W.T@np.linalg.solve((z+1/z)*np.eye(len(core))-TX,W)
        S=np.linalg.solve(z*Gamma-np.eye(15),np.eye(15)-Gamma/z)
        ES,m=expected(z)
        print('SCATTER',z,'MAX ERROR',np.max(abs(S-ES)),'HANKEL',np.max(abs(S-S[0][(np.arange(15)[:,None]+np.arange(15)[None,:])%15])),flush=True)
        print('FIRST ROW',repr(S[0].tolist()),flush=True)
        print('M',repr(m.tolist()),flush=True)
        signp,lp=np.linalg.slogdet((1+z*z)*np.eye(len(core))-z*TX-C)
        signt,lt=np.linalg.slogdet((1+z*z)*np.eye(len(core))-z*TX-z*z*C)
        det=-signp/signt*np.exp(lp-lt)
        print('DET',np.linalg.det(S),'P/PTILDE',det,'FACTORED',-np.prod(m),flush=True)
        assert np.max(abs(S-ES))<1e-9
        assert abs(np.linalg.det(S)/det-1)<1e-8
    # Geometry: y -> -y gives t -> -t, then reduce by constant row scaling.
    keys={g:i for i,g in enumerate(VERTICES)};perm=[]
    sigs=[eg.signature(g) for g in VERTICES]
    for i,(n,p) in enumerate(VERTICES):
        pp=tuple((k,c*(1 if k%2==0 else -1)%5) for k,c in p)
        if pp:
            cc=pow(pp[0][1],-1,5);pp=tuple((k,c*cc%5) for k,c in pp)
        g=(n,pp)
        if g in keys:j=keys[g]
        else:
            sig=eg.signature(g)
            j=next(j for j in range(len(VERTICES)) if sigs[j]==sig and eg.invertible_exists(eg.hom(g,VERTICES[j])[1]))
        perm.append(j)
    assert all(perm[perm[i]]==i for i in range(len(VERTICES)))
    assert Counter((min(perm[a],perm[b]),max(perm[a],perm[b]),s) for a,b,s in EDGES)==Counter(EDGES)
    assert all(perm[heads[a]]==heads[-a%15] for a in heads)
    print('INVOLUTION =',perm,flush=True)
    out=Path(__file__).with_name('labelled_data.py')
    out.write_text('# Author: codex:gpt-6-astra\n'+''.join(k+' = '+repr(v)+'\n' for k,v in [('HEADS',heads),('TAIL_LABELS',labels),('INVOLUTION',perm)]))
    autom=[]
    for a,b,c in product(range(1,5),range(5),range(1,5)):
        if P(f.as_expr().subs(x,a*x+b)-c*c*f.as_expr()).is_zero:autom.append((a,b,c))
    assert autom==[(1,0,1),(1,0,4)]
    print('POINTED CURVE AUTOMORPHISMS',autom)
    print('ALL ASSERTIONS PASSED')
if __name__=='__main__':main()
