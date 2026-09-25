#!/usr/bin/env python3
"""Author: codex:gpt-6-astra. Exact F_5 lattice enumeration; writes graph_data.py and prints checks."""
import numpy as np
from itertools import product
from fractions import Fraction
from collections import Counter
import time
Q=5
B=48
N=2*B+1

def series_mul(a,b):
    return np.convolve(a,b)[:2*B+20]%5
M=2*B+20
u=np.zeros(M,dtype=np.int64)
u[2]=1
for _ in range(M//2):
    u2=series_mul(u,u); u3=series_mul(u2,u); u5=series_mul(u3,u2)
    v=np.zeros(M,dtype=np.int64);v[0]=1
    v=(v+u2+u3-2*u5)%5
    u=np.concatenate((np.zeros(2,dtype=np.int64),v[:-2]))
f=u[2:]
X=np.zeros(M,dtype=np.int64); X[0]=1
for n in range(1,M):
    X[n]=-sum(int(f[i])*int(X[n-i]) for i in range(1,min(n+1,len(f))))%5

def sh(a,k):
    out=np.zeros_like(a)
    if k>=0:
        if k<N:out[k:]=a[:N-k]
    elif -k<N:out[:k]=a[-k:]
    return out

def coeff(a):return tuple((i-B,int(c)) for i,c in enumerate(a) if c)
def mulpoly(a,p):
    r=np.zeros_like(a)
    for k,c in p:r=(r+c*sh(a,k))%5
    return r

def addpoly(p,k,c):
    d=dict(p);d[k]=(d.get(k,0)+c)%5
    return tuple(sorted((j,v) for j,v in d.items() if v))

# basis of R=F5[x]+y F5[x], ordered by pole order at infinity.
RB=[];EV=[];PO=[]
for pole in range(B//2+1):
    if pole%2==0:
        power=pole//2; a=np.zeros(M,dtype=np.int64);a[0]=1
        for _ in range(power):a=series_mul(a,X)
    elif pole>=5:
        power=(pole-5)//2+2; a=np.zeros(M,dtype=np.int64);a[0]=1
        for _ in range(power):a=series_mul(a,X)
    else:continue
    r=np.zeros(N,dtype=np.int64)
    for i in range(N):
        j=i-B+pole
        if 0<=j<len(a):r[i]=a[j]
    RB.append(r);EV.append(1);PO.append(pole) # x=y=1 at P_+
RB=np.array(RB).T

def nullspace(A):
    A=A.copy()%5
    nr,nc=A.shape;r=0;piv=[]
    for j in range(nc):
        ix=np.flatnonzero(A[r:,j])
        if not len(ix):continue
        i=r+int(ix[0]);A[[r,i]]=A[[i,r]]
        A[r]=(A[r]*pow(int(A[r,j]),-1,5))%5
        factors=A[:,j].copy();factors[r]=0
        A=(A-factors[:,None]*A[r])%5
        piv.append(j);r+=1
        if r==nr:break
    free=[j for j in range(nc) if j not in piv]
    H=np.zeros((nc,len(free)),dtype=np.int64)
    for k,j in enumerate(free):
        H[j,k]=1
        H[piv,k]=-A[:r,j]%5
    return H

def hom(g,h,shift=None,fibre=False):
    n,p=g;m,v=h
    if shift is None:
        if (n-m)%2:return None,None
        l=(n-m)//2
    else:l=shift
    vp=p[0][0] if p else 1000;vv=v[0][0] if v else 1000
    bounds=[l+min(m,vv)-n,l+min(m-n+vp,vv-n+vp,vv),l-n,l+min(vp-n,0)]
    # b includes the direct h_11*B_12 term of valuation m.
    bounds[1]=l+min(m,m-n+vp,vv-n+vp,vv)
    dims=[sum(t<=-b for t in PO) if b<=0 else 0 for b in bounds]
    assert min(bounds)>=-B//2,(g,h,bounds)
    dim=sum(dims);A=np.zeros((4*N,dim),dtype=np.int64);V=np.zeros((4,dim),dtype=np.int64)
    F=np.zeros((4,dim),dtype=np.int64)
    offset=0
    for entry,d in enumerate(dims):
        for j in range(d):
            a=RB[:,j]
            z=np.zeros(N,dtype=np.int64)
            # four conditions: ct^n, cu+d, (a-vc)t^n, (a-vc)u+b-vd.
            r=[z.copy() for _ in range(4)]
            if entry==0:r[2]=sh(a,n);r[3]=mulpoly(a,p)
            if entry==1:r[3]=a
            if entry==2:
                r[0]=sh(a,n);r[1]=mulpoly(a,p)
                va=mulpoly(a,v);r[2]=-sh(va,n);r[3]=-mulpoly(va,p)
            if entry==3:r[1]=a;r[3]=-mulpoly(a,v)
            for k,threshold in enumerate((l,l,l+m,l+m)):
                F[k,offset+j]=r[k][B+threshold] if 0<=B+threshold<N else 0
                rr=r[k].copy();rr[max(0,B+threshold):]=0
                A[k*N:(k+1)*N,offset+j]=rr
            V[entry,offset+j]=1
        offset+=d
    H=nullspace(A)
    return H,(F[[2,3,0,1]]@H%5 if fibre else V@H%5)

def invertible_exists(V):
    if V is None:return False
    def det(a):return (a[0]*a[3]-a[1]*a[2])%5
    for i in range(V.shape[1]):
        if det(V[:,i]):return True
        for j in range(i):
            if det(V[:,i]+V[:,j]):return True
    return False

def aut(g):
    H,V=hom(g,g)
    # independent columns in the evaluation image, at most dimension four.
    span=[np.zeros(4,dtype=np.int64)];seen={tuple(span[0])}
    for w in V.T:
        if tuple(w) not in seen:
            span=[(a+c*w)%5 for a in span for c in range(5)]
            seen={tuple(a) for a in span}
    units=sum((a[0]*a[3]-a[1]*a[2])%5!=0 for a in span)
    return int(units*5**H.shape[1]//len(span)),H.shape[1]

def neigh(g):
    n,p=g
    return [(n-1,tuple((k,c) for k,c in p if k<n-1))]+[(n+1,addpoly(p,n,a)) for a in range(5)]

def signature(g):
    s,d=aut(g)
    # h^0 of E(k infinity) in the trivial-away-infinity determinant normalization.
    # Hom(O^2,g) contains two copies of H0; l chosen so degree is fixed by parity.
    n,p=g
    hs=[]
    for k in (0,1,2):
        H,_=hom((0,()),g,shift=-(n//2)-k)
        hs.append(H.shape[1]//2)
    return (g[0]%2,s,d,tuple(hs))

def main():
    start=time.time();vs=[];sigs=[];buckets={};adj=[];cache={}
    def identify(g):
        if g in cache:return cache[g]
        sig=signature(g)
        for i in buckets.get(sig,[]):
            H,V=hom(g,vs[i])
            if invertible_exists(V):cache[g]=i;return i
        i=len(vs);vs.append(g);sigs.append(sig);adj.append(None)
        buckets.setdefault(sig,[]).append(i);cache[g]=i
        return i
    identify((0,()))
    i=0
    while i<len(vs):
        if sigs[i][1]<2000:
            adj[i]=Counter(identify(g) for g in neigh(vs[i]))
        if i%10==0:print('PROGRESS',i,len(vs),'seconds',round(time.time()-start,1),flush=True)
        i+=1
    tails=[i for i,s in enumerate(sigs) if s[1]>=2000]
    for i in tails:
        inward=[j for j,a in enumerate(adj) if a is not None and i in a]
        assert len(inward)==1,(i,inward)
        adj[i]=Counter({inward[0]:5})
    for i,a in enumerate(adj):
        for j,w in a.items():
            assert Fraction(w,sigs[i][1])==Fraction(adj[j][i],sigs[j][1]),(i,j,w,adj[j][i],sigs[i],sigs[j])
    edges=[]
    for i,g in enumerate(vs):
        if i in tails:continue
        H,F=hom(g,g,fibre=True)
        span=[np.zeros(4,dtype=np.int64)];seen={tuple(span[0])}
        for w in F.T:
            if tuple(w) not in seen:
                span=[(a+c*w)%5 for a in span for c in range(5)]
                seen={tuple(a) for a in span}
        units=[a for a in span if (a[0]*a[3]-a[1]*a[2])%5]
        lines=[(1,0)]+[(a,1) for a in range(5)]
        unseen=set(range(6));ns=[cache[x] for x in neigh(g)]
        while unseen:
            k=min(unseen);x,y=lines[k];orbit=set()
            for a in units:
                xx=(a[0]*x+a[1]*y)%5;yy=(a[2]*x+a[3]*y)%5
                orbit.add(0 if yy==0 else 1+int(xx*pow(int(yy),-1,5)%5))
            assert len({ns[k] for k in orbit})==1
            unseen-=orbit;j=ns[k]
            if i<j:edges.append((i,j,sigs[i][1]//len(orbit)))
    print('EDGES =',repr(edges))
    print('VERTICES =',repr(vs))
    print('STABILISERS =',repr([s[1] for s in sigs]))
    print('SIGNATURES =',repr(sigs))
    print('ADJACENCY =',repr([dict(a) for a in adj]))
    print('TAILS =',repr(tails))
    mass=sum(Fraction(1,s[1]) for s in sigs)+sum(Fraction(1,4*sigs[i][1]) for i in tails)
    print('MASS',mass,'COUNTS',len(vs),sum(len(a) for a in adj)//2,'TAILS',len(tails))
    # Save a Python data module, the only durable scratch format authorized.
    from pathlib import Path
    out=Path(__file__).with_name('graph_data.py')
    out.write_text('# Author: codex:gpt-6-astra\n'+''.join(k+' = '+repr(v)+'\n' for k,v in [('VERTICES',vs),('STABILISERS',[s[1] for s in sigs]),('ADJACENCY',[dict(a) for a in adj]),('TAILS',tails),('EDGES',edges)]))
    print('ALL ASSERTIONS PASSED',time.time()-start)
if __name__=='__main__':main()
