#!/usr/bin/env python3
"""Independent spectral-projector MUBs and residue-sampled compression matrices.

No code is imported from the reviewed lane. Unlike its eigensolver construction,
MUB columns here come from character projectors. Unlike its diagonal ball test,
the trace test constructs every matrix entry by sampling fine residue classes.
"""
from fractions import Fraction as F
from itertools import combinations
import numpy as np
from scipy.sparse import coo_matrix

def val(x, p):
    x = F(x)
    if not x: return float('inf')
    r, s, v = abs(x.numerator), x.denominator, 0
    while r % p == 0: r //= p; v += 1
    while s % p == 0: s //= p; v -= 1
    return v

def displacement(p, u, j, sign=1):
    z = np.exp(2j*np.pi/p)
    T = np.zeros((p,p), complex)
    for x in range(p):
        T[x,(x+u)%p] = z**((j*x+sign*pow(2,-1,p)*u*j)%p)
    return T

def mub_check(p):
    z = np.exp(2j*np.pi/p)
    bases = []
    labels = [(0,1)] + [(1,c) for c in range(p)]
    print('\nMUB p =', p, 'construction = character projectors')
    for u,j in labels:
        S = displacement(p,u,j)
        powers = [np.linalg.matrix_power(S,r) for r in range(p)]
        cols=[]
        for k in range(p):
            P = sum(z**((-k*r)%p)*powers[r] for r in range(p))/p
            c = P[:,np.argmax(np.linalg.norm(P,axis=0))]
            c = c / np.linalg.norm(c)
            first = np.flatnonzero(abs(c)>1e-9)[0]
            c *= abs(c[first])/c[first]
            assert np.linalg.norm(S@c-z**k*c)<1e-12
            cols.append(c)
        B = np.column_stack(cols)
        bases.append(B)
        print('line', (u,j), 'basis columns =\n', np.round(B,10))
        print('within Gram =\n',np.round(B.conj().T@B,12))
        assert np.allclose(B.conj().T@B,np.eye(p),atol=1e-12)
    worst = 0.
    for i,j in combinations(range(p+1),2):
        G=abs(bases[i].conj().T@bases[j])**2
        print('cross squared Gram', labels[i], labels[j], '=\n',np.round(G,12))
        worst=max(worst,float(np.max(abs(G-1/p))))
    print('maximum MUB error:',format(worst,'.3e'))
    assert worst<1e-12
    for sign in [1,-1]:
        S = displacement(p,1,1,sign)
        err=np.linalg.norm(S@S-displacement(p,2,2,sign))
        print('Weyl sign',sign,'squared-generator residual',format(err,'.12g'))
        assert (err<1e-12)==(sign==1)
    # Nonzero symplectic cocycle: omega((1,0),(0,1)) = +1.
    lhs=displacement(p,1,0)@displacement(p,0,1)
    rhs=z**pow(2,-1,p)*displacement(p,1,1)
    print('positive symmetric cocycle residual',np.linalg.norm(lhs-rhs))
    assert np.linalg.norm(lhs-rhs)<1e-12

def compression_counts(p,n,a):
    """H entries are exact counts/p^h, C=P_n D_a P_n = p^(-v(a)/2) H.

    e_C=p^(n/2)1_(C/p^n+p^n Z_p), C mod N=p^(2n).
    Integrate over x=(C+N t)/p^n, t mod p^h, h=max(-v(a),0).
    For each residue, a*x is either outside the support or in one basis coset.
    This is an exact integration: the indicators are constant on these cells.
    """
    a=F(a); v=val(a,p); h=max(-v,0); N=p**(2*n); Q=N*p**h
    unit=a/(F(p)**v)
    r=unit.numerator*pow(unit.denominator,-1,Q)%Q if Q>1 else 0
    rows=[]; cols=[]
    for C in range(N):
        for t in range(p**h):
            b=r*(C+N*t)
            if v>=0:
                D=(p**v*b)%N
            else:
                if b%p**h: continue
                D=(b//p**h)%N
            rows.append(C); cols.append(D)
    H=coo_matrix((np.ones(len(rows),dtype=np.int64),(rows,cols)),shape=(N,N)).tocsr()
    return H,p**h,v

def trace_check():
    print('\nFINITE COMPRESSION MATRICES ON Z/p^(2n)')
    count=0
    for p in [3,5]:
        cases=[F(1),F(p),F(p*p),F(1,p),F(1,p*p),F(2),F(p+2,p),F(1+p),F(1+p**2),F(1+p**3),F(1+p**5),F(1-p),F(-1)]
        for n in range(3):
            for a in cases:
                H,den,v=compression_counts(p,n,a)
                rational=F(int(H.diagonal().sum()),den)
                r=val(1-a,p)
                predicted=F(p)**min(r,2*n)
                assert rational==predicted,(p,n,a,rational,predicted)
                value=float(rational)*p**(-v/2)
                count+=1
                print(f'p={p} n={n} a={a} v(a)={v} v(1-a)={r} dim={p**(2*n)} nnz={H.nnz} trace/|a|^.5={rational} trace={value:.12g} correct=True')
                if p==3 and n==1 and a in [F(3),F(1,3),F(28)]:
                    print('matrix / |a|^.5 = counts /',den,'\n',H.toarray())
            H,den,v=compression_counts(p,n,F(p))
            G,gd,gv=compression_counts(p,n,F(1,p))
            A=H.toarray()*p**(-v/2)/den
            B=G.toarray()*p**(-gv/2)/gd
            assert np.allclose(A.T,B)
            defect=np.linalg.norm(A@B-np.eye(len(A)))
            print('compression multiplicativity defect ||C(p)C(1/p)-I||_F =',format(defect,'.12g'))
            assert defect>0.1
    print('exact trace cases passed =',count)
    # Reproduce the lane's notable p=5,n=3 cases without its trace formula.
    for a in [F(126),F(1,25),F(1)]:
        H,d,v=compression_counts(5,3,a)
        print('p=5 n=3 a=',a,'trace=',float(F(int(H.diagonal().sum()),d))*5**(-v/2))
    print('identity rank vs proposed Connes term, h(1)=1, Lambda=p^n:')
    for n in [0,1,2,3]:
        print('p=5 n=',n,'rank=',5**(2*n),'2 log Lambda=',2*n*np.log(5))
    print('integrated unit-group trace by finite permutation fixed-point enumeration:')
    for p in [3,5]:
        for n in [0,1,2]:
            N=p**(2*n)
            units=[a for a in range(N) if a%p] if N>1 else [0]
            total=sum(sum((a*C-C)%N==0 for C in range(N)) for a in units)
            average=F(total,len(units))
            print('p=',p,'n=',n,'average Tr(C(a)) over units=',average,'prediction 2n+1=',2*n+1,'log(p)-normalized average=',float(average)*np.log(p))
            assert average==2*n+1

if __name__=='__main__':
    np.set_printoptions(linewidth=200,precision=12,suppress=True)
    for p in [3,5,7]: mub_check(p)
    trace_check()
    print('ALL INDEPENDENT MUB AND TRACE CHECKS PASSED')
