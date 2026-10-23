#!/usr/bin/env python3
"""Exact polynomial arithmetic and complete finite row families, q=7,13.

No zeros/RH used in the family calculation. Direct rows use integer pairs in
Z[zeta_6]. Long complete families are summed EXACTLY by residue orthogonality,
not sampled and not literally enumerated. Short-row h limits are printed.
Dependencies: numpy, numba, python-flint, sympy, mpmath.
Run with python3 checks/qrh_ff_family.py from the lane directory.
"""
from pathlib import Path
from math import comb, log
from fractions import Fraction
import sys
import numpy as np
from numba import njit, prange, set_num_threads
from flint import nmod_poly
import sympy as sp
import mpmath as mp

set_num_threads(4)
WIDTH = 9
PAIR = np.array([(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)],dtype=np.int64)


class Tee:
    def __init__(self,file): self.file=file
    def write(self,s): sys.__stdout__.write(s); self.file.write(s)
    def flush(self):
        sys.__stdout__.flush()
        if not self.file.closed: self.file.flush()


@njit(cache=True)
def power(a,n,q):
    r=1
    while n:
        if n&1: r=r*a%q
        a=a*a%q; n//=2
    return r


@njit(cache=True)
def degree(a):
    k=len(a)-1
    while k>=0 and a[k]==0: k-=1
    return k


@njit(cache=True)
def resultant(a,b,q,inv):
    f,g=a.copy(),b.copy()
    m,n=degree(f),degree(g)
    if n<0: return 0
    ans=1
    while n>0:
        if m<n:
            if (m*n)&1: ans=(-ans)%q
            f,g=g,f; m,n=n,m
            continue
        r=f.copy()
        for k in range(m,n-1,-1):
            c=r[k]*inv[g[n]]%q
            for j in range(n+1): r[k-n+j]=(r[k-n+j]-c*g[j])%q
        d=degree(r)
        if d<0: return 0
        if (m*n)&1: ans=(-ans)%q
        ans=ans*power(g[n],m-d,q)%q
        f,g=g,r; m,n=n,d
    return ans*power(g[0],m,q)%q


@njit(cache=True)
def decode(i,q,D,monic=True):
    a=np.zeros(WIDTH,dtype=np.int64)
    for k in range(D): a[k]=i%q; i//=q
    if monic: a[D]=1
    return a


@njit(cache=True)
def build_columns(q,D,f,inv,eta):
    ns=np.zeros((q**D,WIDTH),dtype=np.int64)
    weights=np.zeros(q**D,dtype=np.int64)
    mus=np.zeros(q**D,dtype=np.int64)
    for i in range(q**D):
        n=decode(i,q,D)
        deriv=np.zeros(WIDTH,dtype=np.int64)
        for j in range(1,D+1): deriv[j-1]=j*n[j]%q
        disc=resultant(n,deriv,q,inv)
        if (D*(D-1)//2)&1: disc=(-disc)%q
        mu=eta[disc]*((-1)**D)
        nu=eta[resultant(f,n,q,inv)]
        ns[i]=n; mus[i]=mu; weights[i]=mu*nu
    return ns,weights,mus


@njit(cache=True,parallel=True)
def rows_at_degree(q,d,ns,weights,inv,exps):
    values=np.zeros((q**d,2),dtype=np.int64)
    for i in prange(q**d):
        u=decode(i,q,d)
        a,b=0,0
        for j in range(len(weights)):
            if weights[j]==0: continue
            r=resultant(ns[j],u,q,inv)
            if r:
                e=exps[r]
                a+=weights[j]*PAIR[e,0]; b+=weights[j]*PAIR[e,1]
        values[i,0]=a; values[i,1]=b
    return values


@njit(cache=True)
def one_row(u,q,ns,weights,inv,exps):
    a,b=0,0
    for j in range(len(weights)):
        if weights[j]:
            r=resultant(ns[j],u,q,inv)
            if r:
                a+=weights[j]*PAIR[exps[r],0]; b+=weights[j]*PAIR[exps[r],1]
    return a,b


def array(poly):
    x=np.zeros(WIDTH,dtype=np.int64)
    for i,c in enumerate(poly): x[i]=int(c)
    return x


def tables(q):
    gen=int(sp.primitive_root(q))
    exps=np.full(q,-1,dtype=np.int64)
    eta=np.zeros(q,dtype=np.int64)
    for k in range(q-1):
        r=pow(gen,k,q); exps[r]=k%6; eta[r]=(-1)**k
    inv=np.array([0]+[pow(k,-1,q) for k in range(1,q)],dtype=np.int64)
    return gen,exps,eta,inv


def conductor(q):
    for c in range(1,q):
        p=nmod_poly([c,1,0,1],q)
        if len(p.factor()[1])==1 and p.factor()[1][0][1]==1 and p.factor()[1][0][0].degree()==3:
            return p
    raise RuntimeError('no irreducible cubic found')


def complete_weight(q,D):
    # f is one irreducible cubic. |nu|^2 deletes just that prime.
    a=[1]+[0]*D
    for d in range(1,D+1):
        number=sum(int(sp.mobius(k))*q**(d//k) for k in sp.divisors(d))//d-(d==3)
        b=[0]*(D+1)
        for k in range(min(number,D//d)+1):
            w=comb(number,k)*(q**d-1)**k
            for j in range(D-k*d+1): b[j+k*d]+=a[j]*w
        a=b
    return a[D]


def gauss_checks(q,exps,eta,inv):
    """Exact cyclotomic remainders, not a floating tolerance check."""
    x=sp.Symbol('x'); M=6*q
    phi=sp.Poly(sp.cyclotomic_poly(M,x),x,domain=sp.ZZ)
    def cyclo(hist):
        return sp.Poly.from_dict({(int(k),):int(v) for k,v in enumerate(hist) if v},x,domain=sp.ZZ).rem(phi)
    def tau(j):
        h=[0]*M
        for c in range(1,q): h[(q*j*int(exps[c])+6*c)%M]+=1
        return cyclo(h)
    tau1,tau2=tau(-1),tau(2)
    checked=0
    for D in range(1,4):
        ns,w,mus=build_columns(q,D,array(conductor(q)),inv,eta)
        choices=list(range(min(q**D,12)))+[q**D-1]
        for ix in choices:
            if not mus[ix]: continue
            n=ns[ix]; mu=int(mus[ix])
            gs={}
            for j in [-1,2]:
                hist=[0]*M
                for a in range(q**D):
                    v=decode(a,q,D,False)
                    r=int(resultant(n,v,q,inv))
                    if r: hist[(q*j*int(exps[r])+6*int(v[D-1]))%M]+=1
                gs[j]=cyclo(hist)
            # Unnormalized: mu G_-1 tau_2^D = (-1)^D eta(sign) tau_-1^D G_2.
            sign=(-1)**D*int(eta[(-1)**(D*(D-1)//2)%q])
            assert (mu*gs[-1]*(tau2**D)-sign*(tau1**D)*gs[2]).rem(phi).is_zero
            # Direct Hasse-Davenport / discriminant formula for G_2.
            deriv=np.zeros(WIDTH,dtype=np.int64)
            for k in range(1,D+1): deriv[k-1]=k*n[k]%q
            R=int(resultant(n,deriv,q,inv)); exponent=2*int(exps[R])%6
            rhs=mu*(-1)**D*sp.Poly(x**(q*exponent),x)*(tau2**D)
            assert (gs[2]-rhs).rem(phi).is_zero
            checked+=1
    print(f'GAUSS exact cyclotomic checks={checked} (D<=3); absorption and discriminant formula PASS')


def main():
    print('EXACT ARITHMETIC: F_q[t], integer pairs in Z[zeta_6], integer mean squares.')
    print('Rows include zero and all leading coefficients; h means degree <=h, row count=q^(h+1).')
    print('nu is the quadratic character of an explicitly printed irreducible cubic f.')
    print('Direct h limits: q7 [2,3,4,5,4]; q13 [2,3,4,3,2] for D=1..5.')
    print('All D=1..5 also use the EXACT complete-residue formula at h=2D-1 and h=2D.')
    print('These long-row values do not test H-MS at h~D for D=4,5 at q13.')
    for q in [7,13]:
        gen,exps,eta,inv=tables(q)
        fp=conductor(q); f=array(fp)
        print(f'\nFIELD q={q}, generator={gen}, conductor f={fp}, nu(n)=(n/f)_2')
        L=[1]
        for d in [1,2]:
            L.append(sum(int(eta[resultant(f,decode(i,q,d),q,inv)]) for i in range(q**d)))
        print('L coefficients (constant first), computed from characters=',L)
        series=[1]
        for D in range(1,6):
            series.append(-sum(L[j]*series[D-j] for j in range(1,min(2,D)+1)))
            ns,weights,mus=build_columns(q,D,f,inv,eta)
            assert int(weights.sum())==series[D]
            # Cross-check Pellet sign and resultant via a separate factorization implementation.
            for ix in list(range(min(q**D,20)))+[q**D-1]:
                p=nmod_poly([int(c) for c in ns[ix,:D+1]],q)
                factors=p.factor()[1]
                mu=0 if any(e>1 for _,e in factors) else (-1)**len(factors)
                assert mu==int(mus[ix])
                assert int(resultant(f,ns[ix],q,inv))==int(fp.resultant(p))
            sf_count=int(np.count_nonzero(mus))
            assert sf_count==(q if D==1 else q**D-q**(D-1))
            print(f'D={D} squarefree_columns={sf_count} A1={series[D]} formal_inverse_check=PASS')
            hmax=([2,3,4,5,4] if q==7 else [2,3,4,3,2])[D-1]
            total=0
            for h in range(hmax+1):
                values=rows_at_degree(q,h,ns,weights,inv,exps)
                total+=(q-1)*sum(int(a)**2+int(a)*int(b)+int(b)**2 for a,b in values)
                prediction=q**(D+h)
                exp=(log(total,q)-h)/D if total else float('-inf')
                print(f'DIRECT D={D} h={h} rows={q**(h+1)} S={total} S/q^(D+h)={Fraction(total,prediction)} ratio_per_row={Fraction(total,q*prediction)} beta=(log_q(S)-h)/D={exp:.9f} beta_per_row={exp-1/D:.9f}')
                if h>=2*D-1:
                    assert total==q**(h+1-D)*complete_weight(q,D)
            # Check each of the q degree-one prime amplifiers, whose sixth powers have degree 6.
            for c in range(q):
                pp=nmod_poly([c,1],q)
                row=one_row(array(pp**6),q,ns,weights,inv,exps)
                removed=sum(int(weights[i]) for i in range(len(weights)) if int(resultant(ns[i],array(pp),q,inv))==0)
                assert row==(series[D]-removed,0)
            print(f'AMPLIFIER D={D}: all {q} linear primes p, exact A_(p^6)=A1-removed PASS')
            for h in [2*D-1,2*D]:
                W=complete_weight(q,D)
                S=q**(h+1-D)*W
                print(f'COMPLETE D={D} h={h} rows={q**(h+1)} weighted_diagonal={W} S={S} S/q^(D+h)={Fraction(S,q**(D+h))} ratio_per_row={Fraction(S,q**(D+h+1))} beta={(log(S,q)-h)/D:.9f} beta_per_row={(log(S,q)-h-1)/D:.9f}')
        gauss_checks(q,exps,eta,inv)
        print('COMPARISON STEP ONLY: zeros of L, AFTER all family calculations; mpmath 80 digits.')
        mp.mp.dps=80
        roots=mp.polyroots(list(reversed(L)),maxsteps=100)
        for z in roots:
            print('root=',mp.nstr(z,45),'modulus=',mp.nstr(abs(z),45),'polynomial_residual=',mp.nstr(abs(sum(c*z**i for i,c in enumerate(L))),8))
        print('Weil radius=',mp.nstr(1/mp.sqrt(q),45),'11/12 disk radius=',mp.nstr(mp.power(q,-mp.mpf(11)/12),45))
        # For this quadratic, exact discriminant<0 and leading coefficient q certify the moduli.
        print('Exact comparison certificate: L2=q:',L[2]==q,'quadratic discriminant=',L[1]**2-4*L[2])
        assert L[2]==q and L[1]**2-4*q<0
    print('PASS. Short-row H-MS remains unproved; finite tables are not asymptotic estimates.')


if __name__=='__main__':
    with Path(__file__).with_name('output_ff.txt').open('w') as out:
        sys.stdout=Tee(out)
        main()
        sys.stdout=sys.__stdout__
