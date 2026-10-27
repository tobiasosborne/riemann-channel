#!/usr/bin/env python3
"""LPS graphs by projective quaternion enumeration, sparse Hashimoto traces.

Different construction from the author's matrix splitting/BFS. Vertices are all
projective invertible quaternions of the appropriate norm square class. Trace
counts use an actual CSR Hashimoto operator. Prime counts use formal Euler
factor extraction, not Mobius inversion. Word checks use meet-in-the-middle.
"""
from collections import defaultdict, deque
from fractions import Fraction
from itertools import product
import math, time
import numpy as np
from scipy.sparse import csr_matrix
from scipy.linalg import eigvalsh
from scipy.sparse.linalg import eigsh

def mul(x,y):
    # Hamilton product from scalar/vector dot and vector cross products.
    a,*v=x;b,*w=y
    cross=(v[1]*w[2]-v[2]*w[1],v[2]*w[0]-v[0]*w[2],v[0]*w[1]-v[1]*w[0])
    return (a*b-sum(u*z for u,z in zip(v,w)),*(a*w[i]+b*v[i]+cross[i] for i in range(3)))

def canon(x,r):
    x=tuple(a%r for a in x)
    c=next(a for a in x if a)
    return tuple(a*pow(c,-1,r)%r for a in x)

GENS=[(1,0,0,2),(1,0,0,-2),(1,0,2,0),(1,0,-2,0),(1,2,0,0),(1,-2,0,0)]

def graph(r):
    bip=pow(5,(r-1)//2,r)!=1
    vertices=[]
    for first in range(4):
        for tail in product(range(r),repeat=3-first):
            x=(0,)*first+(1,)+tail
            norm=sum(c*c for c in x)%r
            if norm and (bip or pow(norm,(r-1)//2,r)==1):vertices.append(x)
    ix={x:i for i,x in enumerate(vertices)}
    adj=np.array([[ix[canon(mul(x,g),r)] for g in GENS] for x in vertices],dtype=np.int64)
    n=len(adj);root=ix[(1,0,0,0)]
    assert all(len(set(row))==6 and i not in row for i,row in enumerate(adj))
    A=csr_matrix((np.ones(n*6,dtype=np.int64),(np.repeat(np.arange(n),6),adj.ravel())),shape=(n,n))
    assert (A-A.T).nnz==0
    colors={root:0};queue=deque([root]);isbip=True
    while queue:
        v=queue.popleft()
        for w in adj[v]:
            if w not in colors:colors[w]=1-colors[v];queue.append(w)
            elif colors[w]==colors[v]:isbip=False
    assert len(colors)==n and isbip==bip
    # Directed edge (v,s) ends at adj[v,s]; inverse generator is s xor 1.
    rows=[];cols=[]
    for v in range(n):
        for s in range(6):
            for t in range(6):
                if t!=(s^1):rows.append(6*v+s);cols.append(6*int(adj[v,s])+t)
    B=csr_matrix((np.ones(len(rows),dtype=np.int64),(rows,cols)),shape=(6*n,6*n))
    return n,A,B,root,bip

def sparse_counts(B,n,root,K=8,full=False):
    counts=np.zeros(K,dtype=np.int64)
    indices=np.arange(6*n) if full else np.arange(6*root,6*root+6)
    for off in range(0,len(indices),48):
        batch=indices[off:off+48]
        U=np.zeros((6*n,len(batch)),dtype=np.int64)
        U[batch,np.arange(len(batch))]=1
        for k in range(K):
            U=B@U
            counts[k]+=U[batch,np.arange(len(batch))].sum()
    return counts if full else counts*n

def euler_primes(counts):
    # zeta'=zeta sum_{k>=1} N_k u^(k-1), then remove (1-u^d)^(-pi_d).
    K=len(counts);z=[Fraction(1)]+[Fraction(0)]*K
    for k in range(1,K+1):z[k]=sum(int(counts[j-1])*z[k-j] for j in range(1,k+1))/k
    pi=[];work=z[:]
    for d in range(1,K+1):
        exponent=work[d]
        assert exponent.denominator==1 and exponent>=0
        c=int(exponent);pi.append(c)
        factor={j*d:Fraction((-1)**j*math.comb(c,j)) for j in range(min(c,K//d)+1)}
        work=[sum(work[k-j]*v for j,v in factor.items() if j<=k) for k in range(K+1)]
    assert work==[1]+[0]*K
    return pi

def half_words(length):
    state=[((),(1,0,0,0))]
    for _ in range(length):
        state=[(w+(j,),mul(q,g)) for w,q in state for j,g in enumerate(GENS) if not w or j!=(w[-1]^1)]
    return state

def vp(n,p):
    if n==0:return 1000000
    v=0
    while n%p==0:n//=p;v+=1
    return v

def word_check():
    print('\nMEET-IN-THE-MIDDLE INTEGER QUATERNION CHECK r=11')
    for k in [6,7,8]:
        left=half_words(k//2);right=half_words(k-k//2);lookup=defaultdict(list)
        for w,q in right:lookup[canon(q,11)].append((w,q))
        types=defaultdict(list)
        for w,q in left:
            conjugate=(q[0],-q[1],-q[2],-q[3])
            for z,h in lookup[canon(conjugate,11)]:
                if z[0]==(w[-1]^1):continue
                result=mul(q,h)
                assert sum(x*x for x in result)==5**k
                ell=max(k-2*vp(2*result[0],5),0)
                tail=z[-1]==(w[0]^1)
                types[tail].append(ell)
                if not tail:assert ell==k
        print('k=',k,'tailless=',len(types[False]),'ell_values=',sorted(set(types[False])),'tailed=',len(types[True]),'tailed_ell_values=',sorted(set(types[True])))
    q=(1,0,0,0)
    for _ in range(6):q=mul(q,(1,0,0,-2))
    print('(1-2k)^6 =',q,'trace=',2*q[0],'norm=',sum(c*c for c in q))
    lookup=defaultdict(list)
    for w,q in half_words(5):lookup[canon(q,29)].append((w,q))
    witnesses=[]
    for w,q in half_words(4):
        conjugate=(q[0],-q[1],-q[2],-q[3])
        for z,h in lookup[canon(conjugate,29)]:
            if z[0]==(w[-1]^1) or z[-1]==(w[0]^1):continue
            witnesses.append((w+z,mul(q,h)))
    print('r=29 length-9 tailless identity words=',len(witnesses),'first witness=',witnesses[0],'N9=',12180*len(witnesses))
    assert len(witnesses)==216

def main():
    start=time.monotonic()
    for r in [11,13,29]:
        n,A,B,root,bip=graph(r)
        print('\nX^{5,%d} n=%d degree=6 bipartite=%s B_shape=%s B_nnz=%d'%(r,n,bip,B.shape,B.nnz),flush=True)
        K=12 if r==29 else 8
        # Full trace for 660 vertices; translation reduction for the larger two.
        counts=sparse_counts(B,n,root,K,full=(r==11))
        if r==11:assert np.array_equal(counts,sparse_counts(B,n,root,K))
        primes=euler_primes(counts)
        print('N_k=',counts.tolist(),'prime_cycle_counts=',primes,flush=True)
        if r==29:
            extremes=eigsh(A.astype(float),k=10,which='LM',return_eigenvectors=False,tol=1e-12)
            non=extremes[abs(abs(extremes)-6)>1e-8]
            print('largest nontrivial |lambda|=',float(max(abs(non))),'first nonzero N length=',next((k for k,c in enumerate(counts,1) if c),None),'claimed girth bound 2 log_5 n=',2*math.log(n,5),flush=True)
            continue
        ev=eigvalsh(A.toarray().astype(float),check_finite=False,driver='evr')
        non=ev[abs(ev-6)>1e-8]
        if bip:non=non[abs(non+6)>1e-8]
        # Use the normalized Chebyshev recurrence, not complex square roots.
        S0=2*np.ones(len(non));S1=non/np.sqrt(5);lhs=[]
        for k in range(1,9):
            if k==1:S=S1
            else:S=(non/np.sqrt(5))*S1-S0;S0,S1=S1,S
            lhs.append(float(S.sum()))
        errors=[];baderrors=[]
        for k in range(1,9):
            orbit=sum(d*primes[d-1]*5**(-k/2) for d in range(1,k+1) if k%d==0)
            T=5**(k/2)+5**(-k/2)
            bad=orbit-n*4*5**(-k/2)*(k%2==0)-T
            correct=bad-bip*((-1)**k)*T
            errors.append(lhs[k-1]-correct);baderrors.append(lhs[k-1]-bad)
            print('k=',k,'spectral=',format(lhs[k-1],'.12g'),'orbit_weight_sum=',format(orbit,'.12g'),'correct_residual=',format(errors[-1],'.3e'),'Theorem4.3_residual=',format(baderrors[-1],'.12g'))
        print('largest nontrivial |lambda|=',float(max(abs(non))),'max_correct_residual=',max(abs(x) for x in errors),'max_printed_Theorem4.3_residual=',max(abs(x) for x in baderrors),flush=True)
        assert max(abs(x) for x in errors)<1e-8
    word_check()
    print('ALL INDEPENDENT LPS CHECKS PASSED; seconds=',time.monotonic()-start)

if __name__=='__main__':main()
