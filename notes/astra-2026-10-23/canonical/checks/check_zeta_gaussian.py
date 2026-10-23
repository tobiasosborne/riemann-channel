#!/usr/bin/env python3
"""60-digit prime-only Gaussian limit and N extension; explicit prime-tail bound.
Gaussian is a supplementary noncompact limit, not the finite-support main experiment.
The infinite pole integral is analytic; arch tail and omitted primes are bounded.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from functools import lru_cache
import mpmath as mp
import numpy as np
mp.mp.dps=60


@lru_cache(maxsize=2)
def powers(X):
    s=np.ones(X+1,bool); s[:2]=False
    for k in range(2,int(X**.5)+1):
        if s[k]: s[k*k::k]=False
    out=[]
    for p in np.flatnonzero(s):
        v=int(p)
        while v<=X: out.append((v,int(p))); v*=int(p)
    return out


def entry(p,j,tau):
    t=j*mp.log(p); U=t+20*tau; X=int(mp.floor(mp.exp(U)))
    h=lambda x:tau*mp.sqrt(mp.pi)*mp.exp(-x*x/(4*tau*tau))
    pole=4*mp.pi*tau*tau*mp.exp(tau*tau/4)*mp.cosh(t/2)
    prime=mp.mpf(0)
    for n,ell in powers(X):
        v=mp.log(n)
        prime+=mp.log(ell)/mp.sqrt(n)*(h(v-t)+h(-v-t))
    h0=h(t)
    def af(x):
        if not x: return h0/2
        return (h(x-t)+h(-x-t)-2*mp.exp(-x/2)*h0)/(mp.exp(x/2)*(-mp.expm1(-2*x)))
    br=sorted(set([mp.mpf(0),U]+[x for x in [t-12*tau,t-6*tau,t,t+6*tau,t+12*tau] if 0<x<U]))
    arch=(mp.log(4*mp.pi)+mp.euler)*h0+mp.quad(af,br)-h0*mp.log(1/mp.tanh(U/2))
    # Sum <= f(X)+int_X^infinity f(x) dx when f decreases, using Lambda(n)<=log(n).
    a=mp.log(X); tail=mp.mpf(0)
    for center in [t,-t]:
        b=center+tau*tau
        integ=tau*mp.sqrt(mp.pi)*mp.exp(center/2+tau*tau/4)*(2*tau*tau*mp.exp(-(a-b)**2/(4*tau*tau))+b*tau*mp.sqrt(mp.pi)*mp.erfc((a-b)/(2*tau)))
        point=mp.log(X)/mp.sqrt(X)*h(a-center)
        # use a positive loose bound for b<0 to avoid cancellation
        if integ<0: integ=abs(integ)
        tail+=point+integ
        b=center-tau*tau
        tail+=tau*tau*mp.pi*mp.exp(-center/2+tau*tau/4)*mp.erfc((U-b)/(2*tau))/(1-mp.exp(-2*U))
    return pole-prime-arch,tail,X


def schur(c):
    phi=[mp.mpf(1)]; h=c[0]; aa=[]; products=[mp.mpf(1)]
    for k in range(len(c)-1):
        a=sum(phi[j]*c[j+1] for j in range(len(phi)))/h; aa.append(a)
        h*=1-a*a; products.append(h/c[0])
        phi=[x-a*y for x,y in zip([0]+phi,phi[::-1]+[0])]
    return aa,products


def main():
    saved={}
    for tau,p,N in [(mp.mpf('.1'),2,16),(mp.mpf('.1'),3,8),(mp.mpf('.1'),5,6),(mp.mpf('.1'),7,6),(mp.mpf('.04'),2,4),(mp.mpf('.07'),2,4)]:
        data=[entry(p,j,tau) for j in range(N+1)]
        c=[x[0] for x in data]; aa,pp=schur(c)
        if tau==mp.mpf('.1'): saved[p]=c[:5]
        err=max(x[1] for x in data)
        print('GAUSSIAN tau=',tau,'p=',p,'N=',N,'Xmax=',max(x[2] for x in data),flush=True)
        print('c0..2',*[mp.nstr(x,30) for x in c[:3]])
        print('alpha',*[mp.nstr(x,25) for x in aa])
        print('product',[(n,mp.nstr(pp[n],25)) for n in [2,4,6,8,10,12,14,16] if n<=N])
        print('moment tail upper bound',mp.nstr(err,8),'min pivot factor',mp.nstr(min(1-a*a for a in aa),12),flush=True)
        assert all(abs(a)<1 for a in aa)
    mp.mp.dps=80
    differences=[]
    for p,c in saved.items():
        refined=[entry(p,j,mp.mpf('.1'))[0] for j in range(5)]
        differences.extend(abs(a-b) for a,b in zip(c,refined))
    print('80-digit reintegration first five moments at all four primes: max difference',mp.nstr(max(differences),12))
    assert max(differences)<mp.mpf('1e-50')
    print('PASS prime-only Gaussian refinements; tail bounds exclude omitted primes and arch tail only, quadrature uses 60 digits')


if __name__=='__main__': main()
