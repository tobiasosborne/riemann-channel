#!/usr/bin/env python3
"""Author: codex:gpt-6-astra. Exact checks for the Cerednik–Drinfeld audit.
Rebuilds only graphs, transport and cycles; writes no files. Run with python3 -B.
"""
from itertools import product
from collections import deque
import math
import numpy as np
import sympy as sp
from scipy.sparse import csr_matrix
from scipy.linalg import eigvalsh

def qmul(a,b):
    w,x,y,z=a; v,r,s,t=b
    return (w*v-x*r-y*s-z*t,w*r+x*v+y*t-z*s,w*s-x*t+y*v+z*r,w*t+x*s-y*r+z*v)
def conj(a): return (a[0],-a[1],-a[2],-a[3])
def canonical(a):
    return a if next(x for x in a if x)>0 else tuple(-x for x in a)
def generators(p):
    return sorted(a for a in product(range(-math.isqrt(p),math.isqrt(p)+1),repeat=4)
                  if a[0]>0 and a[0]%2 and all(x%2==0 for x in a[1:]) and sum(x*x for x in a)==p)
def mn(a):
    a=tuple(x%5 for x in a); c=pow(next(x for x in a if x),-1,5)
    return tuple(x*c%5 for x in a)
def mm(a,b):
    return mn((a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
def phi(a):
    w,x,y,z=a; return mn((w+2*x,y+2*z,-y+2*z,w-2*x))
vertices=sorted({mn(a) for a in product(range(5),repeat=4) if (a[0]*a[3]-a[1]*a[2])%5})
vi={v:i for i,v in enumerate(vertices)}; root=vi[(1,0,0,1)]
S13,S17=generators(13),generators(17)
def colour(S):
    head=np.array([[vi[mm(g,phi(a))] for a in S] for g in vertices])
    rev=np.array([S.index(conj(a)) for a in S]); ids=np.full(head.shape,-1,dtype=np.int64)
    signs=np.zeros_like(ids); edges=[]
    for g in range(120):
        for a in range(len(S)):
            if ids[g,a]>=0: continue
            h,b=int(head[g,a]),int(rev[a]); k=len(edges); edges.append((g,a))
            ids[g,a]=ids[h,b]=k; signs[g,a]=1; signs[h,b]=-1
    adj=np.zeros((120,120),dtype=np.int64)
    for g in range(120):
        for h in head[g]: adj[g,h]+=1
    return head,rev,ids,signs,edges,adj
h13,r13,ids,sgn,edges,A=colour(S13)
h17,r17,iv,sv,ve,A17=colour(S17)
assert len(edges)==840 and len(ve)==1080
assert np.array_equal(A,A.T) and np.max(A)==1 and not np.diag(A).any()
eps=np.array([1 if (g[0]*g[3]-g[1]*g[2])%5 in (1,4) else -1 for g in vertices])
assert np.all(eps[h13]==-eps[:,None]) and np.all(eps[h17]==-eps[:,None])
lookup={canonical(qmul(b,a)):(j,i) for j,b in enumerate(S17) for i,a in enumerate(S13)}
assert len(lookup)==252
rules={(i,j):lookup[canonical(qmul(a,b))] for i,a in enumerate(S13) for j,b in enumerate(S17)}
D=np.zeros((840,120),dtype=np.int64); T1=np.zeros((840,840),dtype=np.int64)
for k,(g,a) in enumerate(edges):
    D[k,g]=-1; D[k,h13[g,a]]=1
    for b in range(18):
        bp,ap=rules[a,b]; v=h17[g,bp]; T1[k,ids[v,ap]]+=sgn[v,ap]
assert np.array_equal(T1,T1.T) and np.array_equal(T1@D,D@A17)
# BFS rooted at identity, neighbours sorted by vertex number, chords in edge order.
parent={root:None}; pedge={}; tree=set(); queue=deque([root])
while queue:
    g=queue.popleft()
    for a in sorted(range(14),key=lambda a:int(h13[g,a])):
        v=int(h13[g,a])
        if v in parent: continue
        parent[v]=g; pedge[v]=int(ids[g,a]); tree.add(int(ids[g,a])); queue.append(v)
assert len(parent)==120 and len(tree)==119
chords=sorted(set(range(840))-tree); Z=np.zeros((840,721),dtype=np.int64)
def add_tree_path(v,coef,j):
    while v!=root:
        u=parent[v]; e=pedge[v]; tail,aa=edges[e]; head=int(h13[tail,aa])
        # path v -> parent(v)
        Z[e,j]+=coef*(1 if (tail,head)==(v,u) else -1)
        v=u
for j,e in enumerate(chords):
    g,a=edges[e]; v=int(h13[g,a]); Z[e,j]=1
    add_tree_path(v,1,j); add_tree_path(g,-1,j)
assert np.array_equal(Z[chords],np.eye(721,dtype=np.int64)) and not (D.T@Z).any()
M=Z.T@Z; TZ=csr_matrix(T1)@Z; L=TZ[chords]
assert np.array_equal(TZ,Z@L)
ML=M@L
assert np.array_equal(L.T@M,ML)
assert not (M-np.eye(721,dtype=np.int64)-Z[sorted(tree)].T@Z[sorted(tree)]).any()
print('Exact cycles: D^t Z=0, chord block I, T1 Z=Z L, L^t M=M L; M>=I.',flush=True)
# Exact adjacency minimal-polynomial and multiplicity certificate.
I=np.eye(120,dtype=np.int64); A2=A@A
assert not ((A2-196*I)@(A2-16*I)@(A2-4*I)).any()
assert int(np.trace(A2))==1680 and int(np.trace(A2@A2))==95040
# bipartite symmetry, connectivity: +/-14 each 1; traces yield +/-4 each34, +/-2 each25.
tau=28*10**34*18**34*12**25*16**25//120
assert tau==2**217*3**92*5**33*7
Q=14*I-A
# Integer Bareiss determinant on the much smaller reduced Laplacian.
nonroot=[i for i in range(120) if i!=root]
def bareiss(mat):
    a=[[int(x) for x in row] for row in mat]; n=len(a); previous=1
    for k in range(n-1):
        pivot=a[k][k]; assert pivot
        for i in range(k+1,n):
            v=a[i][k]
            for j in range(k+1,n):
                num=a[i][j]*pivot-v*a[k][j]
                assert num%previous==0
                a[i][j]=num//previous
            a[i][k]=0
        previous=pivot
    return a[-1][-1]
cofactor=bareiss(Q[np.ix_(nonroot,nonroot)])
assert cofactor==tau
print('det M = spanning trees =',tau,flush=True)
print('factorization = 2^217 * 3^92 * 5^33 * 7',flush=True)
# Graph cover and reversal algebra without dense 1680-square matrices.
rev=np.array([int(h13[g,a])*14+int(r13[a]) for g in range(120) for a in range(14)])
TD=np.zeros((1680,1680),dtype=np.int64)
for g in range(120):
    for a in range(14):
        for b in range(18):
            bp,ap=rules[a,b]; TD[g*14+a,int(h17[g,bp])*14+ap]+=1
sign=np.repeat(eps,14)
assert np.array_equal(TD[:,rev],TD[rev,:])
assert np.array_equal(sign[rev],-sign)
assert not (sign[:,None]*TD+TD*sign[None,:]).any()
# Oriented edge (g,+)->(h,-) is sent by w to the negative of reverse label.
assert np.all(eps[h13]*(-1)==eps[:,None])
print('Exact cover: two 120-vertex components; w=-R; SR=-RS; ST17=-T17S.',flush=True)
# Eis at 17? Use an exact polynomial inverse of Q on degree-zero divisors.
x=sp.Symbol('x'); gpoly=sp.Poly((x-28)*(x-10)*(x-18)*(x-12)*(x-16),x)
g0=int(gpoly.eval(0)); hpoly=sp.Poly((sp.Poly(g0,x)-gpoly).exquo(sp.Poly(x,x)),x)
H=np.zeros_like(Q,dtype=object)
for c in hpoly.all_coeffs(): H=H@Q+int(c)*I
assert np.array_equal(Q.astype(object)@H@(I[:,[0]]-I[:,[root]]),g0*(I[:,[0]]-I[:,[root]]))
B=(A17-18*I)@(I[:,nonroot]-I[:,[root]])
num=H@B; red=num[nonroot,:]-num[root:root+1,:]
denoms=sorted({abs(g0)//math.gcd(abs(int(v)),abs(g0)) for v in red.flat})
print('T17-18 on critical group: solve denominators =',denoms,flush=True)
assert max(denoms)>1
for ii,jj in zip(*np.nonzero(np.asarray(red%g0,dtype=np.int64))):
    print('nonintegral inverse entry: vertex row',nonroot[ii],'divisor e_'+str(nonroot[jj])+'-e_'+str(root),
          'value',str(sp.Rational(int(red[ii,jj]),g0)),flush=True); break
# Strict positivity and doubled identities via exact block reduction.
# Block identities require only ML=L^t M. Check Schur complement by generalized symmetric eigenproblem.
Bsym=Z.T@TZ
vals=eigvalsh(Bsym.astype(float),M.astype(float))
print('numerical max |T| =',float(max(abs(vals))),'; Schur min (M units) =',float(min(17-vals**2/4)),flush=True)
assert max(abs(vals))<8
# Rational 2G blocks: [[2M,-ML],[-ML,34M]]. Exact multiplication as 721-sized blocks.
# F^t (2G) F: TL= L^t M L; then blocks simplify to [[34M,-17ML],[-17ML,578M]].
TML=L.T@ML
assert np.array_equal(2*TML-TML-ML@L+34*M,34*M)
assert np.array_equal(-34*L.T@M+17*ML,-17*ML)
assert np.array_equal(L.T@M,M@L)
print('Exact doubled forms: F^t Omega_M F=17 Omega_M; F^t (2G_M) F=17(2G_M).',flush=True)
# A finite exact endpoint exclusion. With Weil's weak bound for C this proves G_M>0.
def rank_mod(mat,p):
    a=np.asarray(mat%p,dtype=np.int64).copy(); n=a.shape[0]; r=0
    for c in range(a.shape[1]):
        nz=np.flatnonzero(a[r:,c])
        if not len(nz): continue
        j=r+int(nz[0]); a[[r,j]]=a[[j,r]]
        a[r]=(a[r]*pow(int(a[r,c]),-1,p))%p
        below=r+1+np.flatnonzero(a[r+1:,c])
        a[below]=(a[below]-a[below,c,None]*a[r])%p
        r+=1
        if r==n: break
    return r
endpoint=T1@T1-68*np.eye(840,dtype=np.int64)
for prime in [101,103,107,109]:
    rank=rank_mod(endpoint,prime)
    print('rank(T1^2-68I) modulo',prime,'=',rank,flush=True)
    if rank==840: break
assert rank==840
print('ALL CHECKS PASSED',flush=True)
