#!/usr/bin/env python3
"""Exact transport and Bass moment checks. Author: codex:gpt-6-astra."""
from pathlib import Path
import contextlib
import io
import numpy as np
from scipy.sparse import csr_matrix, eye

# Execute only the construction prefix, before costly homology and spectral checks.
source = Path('scripts/lps_square_complex.py').read_text()
prefix = source.split('NE = NE_H + NE_V')[0]
ns = {}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix, 'scripts/lps_square_complex.py:construction-prefix', 'exec'), ns)
N = ns['NE_H']; edges = []
for bd in ns['SQUARES']:
    h = [(e,s) for e,s in bd.items() if e < N]
    assert len(h) == 2
    (a,sa),(b,sb) = h
    edges.append((a,b,-sa*sb))
row=[]; col=[]; sig=[]
for a,b,s in edges:
    row += [a,b]; col += [b,a]; sig += [s,s]
T = csr_matrix((np.array(sig,dtype=np.int64),(row,col)),shape=(N,N))
W = csr_matrix((np.ones(len(sig),dtype=np.int64),(row,col)),shape=(N,N))
assert (W.sum(1) == 18).all()
z = np.array([ns['EPS13'][g] for g,a in ns['C13']],dtype=np.int64)
assert (T.toarray() == -z[:,None]*W.toarray()*z[None,:]).all()
print('vertices, unoriented edges, directed arcs:',N,len(edges),len(row))
print('max unsigned adjacency entry:',W.max(),'loops:',W.diagonal().sum())
print('canonical signed negative edges:',sum(s<0 for a,b,s in edges))

def moments(A, excess):
    m=A.shape[0]; prev=2*eye(m,dtype=np.int64,format='csr'); cur=A.copy()
    out=[]
    for n in range(1,7):
        out.append(int(cur.diagonal().sum())+excess*(1+(-1)**n))
        prev,cur=cur,A@cur-17*prev
    return out
v=moments(csr_matrix(ns['A17']),960)
e=moments(T,6720)
w=moments(W,6720)
assert all(e[n-1] == (-1)**n*w[n-1] for n in range(1,7))
print('n Bv Be Bunsigned TrEven TrOdd TrE StrE N')
for n,(a,b,c) in enumerate(zip(v,e,w),1):
    print(n,a,b,c,2*c,2*b,2*(c+b),2*(c-b),a-b+5760*(1+(-1)**n))
print('full sector dimensions:',2*len(row)**2,'each')
print('diagonal sector dimensions:',2*len(row),'each')
print('coherence zero dimensions:',2*len(row)*(len(row)-1),'each')
print('Kraus rank:',17*len(row))

# Full arc incidence (still sparse), for the departure-weight gauge convention.
tails=[]; heads=[]; signs=[]
for a,b,s in edges:
    tails += [a,b]; heads += [b,a]; signs += [s,s]
tails=np.array(tails); heads=np.array(heads); signs=np.array(signs,dtype=np.int64)
r=len(tails); outgoing=[[] for _ in range(N)]
for i,a in enumerate(tails): outgoing[a].append(i)
cr=[]; cc=[]
for i,b in enumerate(heads):
    for j in outgoing[b]:
        if j != (i ^ 1): cr.append(j); cc.append(i)
C=csr_matrix((np.ones(len(cr),dtype=np.int64),(cr,cc)),shape=(r,r))
B=C.multiply(signs[None,:]).tocsr()
da=z[tails]
assert np.all(da[np.array(cr)]*signs[np.array(cc)]*da[np.array(cc)] == -1)
assert not C.multiply(C.T).nnz
assert int(C.sum()) == 257040
print('arc gauge verified with tail signs; Tr E^2=0, HS squared norm=',4*C.nnz)
print('X-letter canonical signed predecessor sums:',sorted(set((C@signs).tolist())))

# Local Kraus register-coherence identity, including a non-generic P letter.
P2=np.diag([1.,-1.]); XX=np.array([[0.,1.],[1.,0.]])
reg=np.zeros((3,3)); reg[2,0]=1.
AA=np.kron(P2,reg)
for k in range(3):
    for l in range(3):
        unit=np.zeros((3,3)); unit[k,l]=1.
        expected=np.zeros((6,6))
        if k==l==0:
            out=np.zeros((3,3)); out[2,2]=1.
            expected=np.kron(P2@XX@P2,out)
        assert np.array_equal(AA@np.kron(XX,unit)@AA.T,expected)
print('local exact P-letter register-coherence identities passed')

# Exact full-vertex companion intertwiner; restriction to K is in the proof.
from scipy.sparse import bmat
L=csr_matrix((np.concatenate((np.ones(r,dtype=np.int64),-signs)),
              (np.concatenate((np.arange(r),np.arange(r))),
               np.concatenate((tails,N+heads)))),shape=(r,2*N))
I=eye(N,dtype=np.int64,format='csr')
F=bmat([[T,-17*I],[I,None]],format='csr')
err=B@L-L@F; err.eliminate_zeros(); assert not err.nnz
err=L.T@L-bmat([[18*I,-T],[-T,18*I]],format='csr')
err.eliminate_zeros(); assert not err.nnz
print('exact Bass intertwiner and its HS pullback metric passed')
