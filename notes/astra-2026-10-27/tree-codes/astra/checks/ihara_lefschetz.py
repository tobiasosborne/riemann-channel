#!/usr/bin/env python3
"""Local flat traces and exact Ihara counts, including a quaternionic quotient."""
from fractions import Fraction
import math
import numpy as np
import sympy as sp


def vp(x,p):
    x=Fraction(x)
    if not x:
        return float('inf')
    n,d=x.numerator,x.denominator
    v=0
    while n%p==0:
        n//=p
        v+=1
    while d%p==0:
        d//=p
        v-=1
    return v


def power(p,n):
    return Fraction(p)**n


def tau_squared(a,p):
    assert a != 1
    return power(p,-vp(a,p)+2*vp(1-a,p))


def compression_trace_squared(a,p,R=1,N=2):
    # Orthonormal indicators of cosets in p^-R Z_p / p^N Z_p.
    a=Fraction(a)
    va=vp(a,p)
    count=0
    for j in range(p**(R+N)):
        c=Fraction(j,p**R)
        if vp(c-c/a,p)>=min(N,N-va):
            count+=1
    return count*count*power(p,-va+2*N-2*max(N,N-va)),count


def local_checks():
    print('LOCAL FLAT TRACES: exact squared values and finite-rank compression traces')
    for p in (3,5):
        for a in (Fraction(1,p*p),Fraction(1,p),Fraction(p),Fraction(p*p),Fraction(1+p)):
            exact=tau_squared(a,p)
            compressed,count=compression_trace_squared(a,p)
            assert compressed==exact
            print(f'p={p}, a={a}, tau(a)^2={exact}, tau(a)={math.sqrt(exact):.17g}, compression fixed cosets={count}, compressed trace^2={compressed}')
    print('T4b counterexample: p=3, gamma=diag(1,9), length=2, actual Clifford D_3')
    print(f'actual Clifford flat trace={math.sqrt(Fraction(1,3)):.17g}; graph orbit weight={Fraction(1,3)}; auxiliary boundary D_9 trace={math.sqrt(Fraction(1,9)):.17g}')
    print('Squared actual Clifford trace equals graph weight: 1/3. D_9 acts on the original tree with length 4, not 2.')
    mats3=[(1,0,0,3),(3,0,0,1),(2,1,1,2),(2,-1,-1,2)]
    lines=[]
    for s in mats3:
        col=(s[0]%3,s[2]%3) if (s[0]%3,s[2]%3)!=(0,0) else (s[1]%3,s[3]%3)
        z=next(x for x in col if x)
        lines.append(tuple((x*pow(z,-1,3))%3 for x in col))
    assert len(set(lines))==4
    print('Cocompact counterexample lattice at p=3: g1=diag(1,3), g2=[[2,1],[1,2]]; image lines of g1,g1^-1,g2,g2^-1=',lines)
    print('Four distinct neighbours prove a free simply transitive tree action. In its index-2 even-word subgroup, g1^2 is primitive of length 2.')


def matmul(a,b,q):
    return ((a[0]*b[0]+a[1]*b[2])%q,(a[0]*b[1]+a[1]*b[3])%q,
            (a[2]*b[0]+a[3]*b[2])%q,(a[2]*b[1]+a[3]*b[3])%q)


def canon(a,q):
    t=next(x for x in a if x%q)
    inv=pow(t,-1,q)
    return tuple((x*inv)%q for x in a)


def quaternion_graph():
    q=3
    Id=(1,0,0,1)
    I=(0,1,2,0)
    J=(1,1,1,2)
    K=matmul(I,J,q)
    negId=(2,0,0,2)
    assert matmul(I,I,q)==matmul(J,J,q)==matmul(K,K,q)==negId
    assert matmul(I,J,q)==tuple((-x)%q for x in matmul(J,I,q))
    gens=[canon(tuple((Id[i]+sign*2*h[i])%q for i in range(4)),q) for h in (I,J,K) for sign in (1,-1)]
    assert len(set(gens))==6 and Id not in gens
    group=[Id]
    index={Id:0}
    for g in group:
        for s in gens:
            h=canon(matmul(g,s,q),q)
            if h not in index:
                index[h]=len(group)
                group.append(h)
    A=np.zeros((len(group),len(group)),dtype=np.int64)
    for g in group:
        for s in gens:
            A[index[g],index[canon(matmul(g,s,q),q)]]+=1
    assert len(group)==24 and np.array_equal(A,A.T)
    assert A.max()==1 and np.trace(A)==0 and np.all(A.sum(axis=1)==6)
    print('\nARITHMETIC CONGRUENCE QUOTIENT: p=5, reduction q=3, PGL2(F3)')
    print('Quaternion images I,J,K=',I,J,K)
    print('Six generators 1 +/- 2I, 1 +/- 2J, 1 +/- 2K (projectively normalised)=',gens)
    print('Generated group order=',len(group),'generator determinants mod 3=',[(s[0]*s[3]-s[1]*s[2])%3 for s in gens])
    orders=[]
    for s in gens:
        z=Id
        for order in range(1,25):
            z=canon(matmul(z,s,q),q)
            if z==Id:
                orders.append(order)
                break
    assert orders==[4]*6
    real,imag=1,0
    for _ in range(4):
        real,imag=real-2*imag,2*real+imag
    assert (real,imag)==(-7,-24)
    norm=real*real+imag*imag
    lift_trace=Fraction(2*real,25)
    length=-2*vp(lift_trace,5)
    assert norm==5**4 and length==4
    actual_trace_sq=tau_squared(Fraction(5**(length//2)),5)
    actual_trace=Fraction(math.isqrt(actual_trace_sq.numerator),math.isqrt(actual_trace_sq.denominator))
    graph_weight=power(5,-length//2)
    assert actual_trace==Fraction(1,5) and graph_weight==Fraction(1,25)
    print('Generator orders in PGL2(F3)=',orders)
    print('Arithmetic prime cycle (1+2i)^4=',(real,imag,0,0),'; norm=',norm)
    print('SL2 lift trace=',lift_trace,'valuation=',vp(lift_trace,5),'; eigenvalue valuations=',(-length//2,length//2))
    print(f'This element is primitive in the congruence kernel, length={length}; actual Clifford flat trace={actual_trace}={float(actual_trace)}, graph weight={graph_weight}={float(graph_weight)}.')
    # The six distinct neighbour images at the p=5 base vertex.
    # Choose i in Z_5 with i=2 mod 5, j=[[0,1],[-1,0]], k=ij.
    mats5=[(0,0,0,2),(2,0,0,0),(1,2,3,1),(1,3,2,1),(1,4,4,1),(1,1,1,1)]
    images=[]
    for s in mats5:
        col=(s[0],s[2]) if (s[0],s[2])!=(0,0) else (s[1],s[3])
        z=next(x for x in col if x)
        images.append(tuple((x*pow(z,-1,5))%5 for x in col))
    assert len(set(images))==6
    print('p=5 generator image lines mod 5=',images,'; all 6 neighbours distinct')
    return A


def graph_checks(name,A,p,bipartite):
    n=len(A)
    edge_list=[(i,j) for i in range(n) for j in range(n) if A[i,j]]
    E=len(edge_list)//2
    B=np.zeros((2*E,2*E),dtype=np.int64)
    for i,(a,b) in enumerate(edge_list):
        for j,(c,d) in enumerate(edge_list):
            if b==c and d!=a:
                B[i,j]=1
    assert np.all(B.sum(axis=1)==p)
    print(f'\nGRAPH {name}: p={p}, vertices={n}, undirected edges={E}, B size={len(B)}, bipartite={bipartite}')
    t,u=sp.symbols('t u')
    char=sp.Poly(sp.Matrix(A.tolist()).charpoly(t).as_expr(),t)
    factors=sp.factor_list(char.as_expr())[1]
    print('Exact adjacency characteristic polynomial=',sp.factor(char.as_expr()))
    # det(I-Au+pu^2) from the exact characteristic polynomial, not B.
    Q=sp.Poly(sp.expand(sum(c*(1+p*u*u)**(n-i)*u**i for i,c in enumerate(char.all_coeffs()))),u)
    bass=sp.Poly((1-u*u)**(E-n)*Q.as_expr(),u)
    print('Ihara-Bass reciprocal zeta factorisation=',sp.factor(bass.as_expr()))
    # Coefficient extraction from -u D'(u)/D(u) gives N_k independently of B.
    coeff=[int(bass.nth(k)) for k in range(9)]
    counts_bass=[0]*9
    for k in range(1,9):
        counts_bass[k]=-k*coeff[k]-sum(coeff[j]*counts_bass[k-j] for j in range(1,k))
    eigen=np.linalg.eigvalsh(A.astype(float))
    nontrivial=[x for x in eigen if abs(x-(p+1))>1e-8 and (not bipartite or abs(x+(p+1))>1e-8)]
    parameters=[z for x in nontrivial for z in np.roots([1,-x/math.sqrt(p),1])]
    print('Numerical adjacency eigenvalues=',np.array2string(eigen,precision=10,max_line_width=160))
    print('Nontrivial max absolute adjacency eigenvalue=',f'{max(abs(x) for x in nontrivial):.17g}', 'Ramanujan band=',f'{2*math.sqrt(p):.17g}')
    N=[0]*9
    P=[0]*9
    BB=np.eye(len(B),dtype=np.int64)
    max_error=0.0
    for k in range(1,9):
        BB=BB@B
        N[k]=int(np.trace(BB))
        assert N[k]==counts_bass[k]
        numerator=sum(int(sp.mobius(d))*counts_bass[k//d] for d in sp.divisors(k))
        assert numerator%k==0
        P[k]=numerator//k
        orbit=math.fsum(d*P[d]*p**(-k/2) for d in sp.divisors(k))
        assert abs(orbit-N[k]*p**(-k/2))<1e-10
        trivial=(1+(-1)**k if bipartite else 1)*(p**(k/2)+p**(-k/2))
        tree=n*(p-1)*p**(-k/2)*(k%2==0)
        rhs=orbit-trivial-tree
        lhs=sum(z**k for z in parameters)
        err=abs(lhs-rhs)
        max_error=max(max_error,err)
        assert err<1e-9
        print(f'k={k}: Tr(B^k)={N[k]}, Bass N_k={counts_bass[k]}, primitive P_k={P[k]}, orbit={orbit:.17g}, C_spectrum={lhs.real:.17g}{lhs.imag:+.3g}j, C_formula={rhs:.17g}, residual={err:.3g}')
    print('SUMMARY N_1..N_8=',N[1:])
    print('SUMMARY P_1..P_8=',P[1:])
    print(f'max explicit-formula residual={max_error:.18g}; float tolerance=1e-9; counts and polynomials exact')
    # All orbit weights are affine-boundary flat traces, tau(p^k)=p^(-k/2).
    for k in range(1,9):
        assert tau_squared(Fraction(p**k),p)==power(p,-k)


if __name__=='__main__':
    local_checks()
    A=quaternion_graph()
    graph_checks('quaternion PGL2(F3) quotient',A,5,True)
    graph_checks('K5 (general regular graph comparison)',np.ones((5,5),dtype=np.int64)-np.eye(5,dtype=np.int64),3,False)
