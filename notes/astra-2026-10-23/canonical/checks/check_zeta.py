#!/usr/bin/env python3
"""Prime-only compact C-infinity windows. Reimplements lane R's explicit formula.
No zero files or zero-finding calls. Outputs compare two independent discretizations.
L is support length of g; shifts j log p occupy a window of length L+N log p.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from functools import lru_cache
from pathlib import Path
import numpy as np
from scipy.signal import fftconvolve
from scipy.interpolate import CubicSpline
from scipy.linalg import toeplitz
from numpy.polynomial.legendre import leggauss
HERE=Path(__file__).resolve().parent


def cutoff(x):
    a=np.abs(x); ans=np.ones_like(a)
    ans[a>=1]=0; use=(a>.5)&(a<1); t=2*a[use]-1
    v=np.exp(-1/(1-t)); w=np.exp(-1/t)
    ans[use]=v/(v+w)
    return ans


def pair_function(L,tau,res,shape='gaussian'):
    u=np.linspace(-L/2,L/2,res+1); du=L/res
    if shape=='gaussian': g=np.exp(-u*u/(2*tau*tau))*cutoff(2*u/L)
    else:
        x=2*u/L; g=np.zeros_like(x); use=np.abs(x)<1
        g[use]=np.exp(1-1/(1-x[use]**2))
    h=fftconvolve(g,g[::-1],mode='full')*du
    h=(h+h[::-1])/2
    f=CubicSpline(np.linspace(-L,L,2*res+1),h,bc_type='clamped',extrapolate=False)
    def out(x):
        x=np.asarray(x); ans=np.zeros_like(x,dtype=float); use=np.abs(x)<L
        ans[use]=f(x[use]); return ans
    return out


@lru_cache(maxsize=4)
def mangoldt(X):
    X=int(X); sieve=np.ones(X+1,bool); sieve[:2]=False
    for p in range(2,int(X**.5)+1):
        if sieve[p]: sieve[p*p::p]=False
    primes=np.flatnonzero(sieve); vals=[]; w=[]
    for p in primes[primes<=int(X**.5)]:
        n=int(p)**2
        while n<=X: vals.append(n); w.append(np.log(float(p))/np.sqrt(n)); n*=int(p)
    logs=np.r_[np.log(primes.astype(float)),np.log(np.array(vals,dtype=float))]
    weights=np.r_[np.log(primes.astype(float))/np.sqrt(primes),w]
    return logs,weights


def integrate(f,breaks,ng=32):
    x,w=leggauss(ng); total=np.longdouble(0)
    breaks=sorted(set(float(v) for v in breaks))
    for a,b in zip(breaks[:-1],breaks[1:]):
        for l,r in zip(np.linspace(a,b,max(2,int(np.ceil((b-a)/.08))+1))[:-1],np.linspace(a,b,max(2,int(np.ceil((b-a)/.08))+1))[1:]):
            t=(l+r)/2+(r-l)/2*x
            total+=np.sum((r-l)/2*w*f(t),dtype=np.longdouble)
    return float(total)


def weil(h,L,t,ng=32):
    U=L+abs(t); h0=float(h(np.array([-t]))[0])
    def pair(x): return h(x-t)
    pole=integrate(lambda x:pair(x)*2*np.cosh(x/2),[-U,t-L,t,t+L,U],ng)
    logs,weights=mangoldt(int(np.floor(np.exp(U))))
    prime=float(np.sum(weights*(pair(logs)+pair(-logs)),dtype=np.longdouble))
    def af(x):
        # expm1 avoids cancellation in the denominator.
        return (pair(x)+pair(-x)-2*np.exp(-x/2)*h0)/(np.exp(x/2)*(-np.expm1(-2*x)))
    br=[0,U]+[x for x in [abs(t-L),abs(t),abs(t+L),L/2] if 0<x<U]
    arch=(np.log(4*np.pi)+np.euler_gamma)*h0+integrate(af,br,ng)-h0*np.log(1/np.tanh(U/2))
    return pole-prime-arch


def schur(c):
    phi=np.array([1.]); h=c[0]; aa=[]; hh=[h]
    for k in range(len(c)-1):
        a=np.dot(phi,c[1:k+2])/h; aa.append(a)
        phi=np.r_[0,phi]-a*np.r_[phi[::-1],0]
        h*=1-a*a; hh.append(h)
    return np.array(aa),np.array(hh)/c[0]


def main():
    rows=[]; maxdef=0.
    specs=[(L,.1,'gaussian') for L in [.4,.8,1.2,1.6,2.4]]
    specs +=[(1.6,tau,'gaussian') for tau in [.04,.07]]+[(.4,0,'bump'),(.8,0,'bump')]
    for L,tau,shape in specs:
        hs=[pair_function(L,tau,4096,shape),pair_function(L,tau,8192,shape)]
        for p in [2,3,5,7]:
            N=8
            cs=[np.array([weil(h,L,j*np.log(p),ng) for j in range(N+1)]) for h,ng in zip(hs,[32,48])]
            aas,prods=zip(*[schur(c) for c in cs]); c=cs[1]; aa=aas[1]; pp=prods[1]
            err=float(np.max(np.abs(cs[0]-c))); aerr=float(np.max(np.abs(aas[0]-aa)))
            mineig=float(np.linalg.eigvalsh(toeplitz(c))[0]); defect=0.
            # Gram entries depend only on (j-k)log p; exact Toeplitz, no clipping.
            # Re-evaluate a pair using literal differences, exposing float defects.
            for j,k in [(2,1),(5,3),(8,5)]:
                v=weil(hs[1],L,j*np.log(p)-k*np.log(p),48)
                defect=max(defect,abs(v-c[j-k]))
            maxdef=max(maxdef,defect)
            print(f'ROW shape={shape} L={L:g} tau={tau:g} p={p} N={N}',flush=True)
            print(' moments='+','.join(f'{x:.15g}' for x in c))
            print(' alpha='+','.join(f'{x:.12g}' for x in aa))
            print(' products N=2,4,6,8 '+','.join(f'{pp[n]:.12g}' for n in [2,4,6,8]))
            print(f' diagnostics moment_delta={err:.3g} alpha_delta={aerr:.3g} min_eig={mineig:.8g} entry_toeplitz_defect={defect:.3g}',flush=True)
            rows.append([shape,L,tau,p,*aa,*pp[[2,4,6,8]],err,aerr,mineig,defect])
    print('MAX entry Toeplitz numerical defect',maxdef)
    with (HERE/'output_zeta_table.txt').open('w') as f:
        f.write('shape L tau p alpha0..7 product2,4,6,8 moment_delta alpha_delta min_eig toeplitz_defect\n')
        for r in rows: f.write(' '.join(str(x) for x in r)+'\n')


if __name__=='__main__': main()
