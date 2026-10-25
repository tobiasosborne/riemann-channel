#!/usr/bin/env python3
"""Exact short-row means. Integer pairs in Z[zeta_6]; no RH input.
Use --audit first, --table for all cells. 12 Numba worker threads.
The pair-Poisson route uses signed divisor norms, not a single dual norm.
"""
from pathlib import Path
import os
HERE=Path(__file__).resolve().parent
os.environ.setdefault('NUMBA_CACHE_DIR',str(HERE/'numba_cache'))
import sys, time, argparse, json
from fractions import Fraction
from math import log, comb
import numpy as np
from numba import njit, prange, set_num_threads
set_num_threads(12)
W=8
PAIR=np.array([(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)],np.int64)

@njit(cache=True)
def power(a,n,q):
    r=1
    while n:
        if n&1:r=r*a%q
        a=a*a%q;n//=2
    return r

@njit(cache=True)
def decode(i,q,d):
    a=np.zeros(W,np.int64)
    for j in range(d):a[j]=i%q;i//=q
    a[d]=1
    return a

@njit(cache=True)
def resultant(a,m,b,n,q,inv):
    if m==0:return power(a[0],n,q)
    if n==0:return power(b[0],m,q)
    if n==1:
        r=0;x=(-b[0]*inv[b[1]])%q
        for j in range(m,-1,-1):r=(r*x+a[j])%q
        r=r*power(b[1],m,q)%q
        return (-r)%q if m&1 else r
    f=a.copy();g=b.copy();ans=1
    while n>0:
        if m<n:
            if (m*n)&1:ans=(-ans)%q
            f,g=g,f;m,n=n,m
        lead=g[n]
        for k in range(m,n-1,-1):
            c=f[k]*inv[lead]%q
            for j in range(n+1):f[k-n+j]=(f[k-n+j]-c*g[j])%q
        d=n-1
        while d>=0 and f[d]==0:d-=1
        if d<0:return 0
        if (m*n)&1:ans=(-ans)%q
        ans=ans*power(lead,m-d,q)%q
        f,g=g,f;m,n=n,d
    return ans*power(g[0],m,q)%q

@njit(cache=True)
def multiply(a,da,b,db,q):
    c=np.zeros(W,np.int64)
    for i in range(da+1):
        for j in range(db+1):c[i+j]=(c[i+j]+a[i]*b[j])%q
    return c

@njit(cache=True)
def encode(a,d,q):
    r=0
    for j in range(d-1,-1,-1):r=r*q+a[j]
    return r

def tables(q):
    gen=next(g for g in range(2,q) if len({pow(g,k,q) for k in range(q-1)})==q-1)
    ex=np.full(q,-1,np.int64);eta=np.zeros(q,np.int64)
    for k in range(q-1):ex[pow(gen,k,q)]=k%6;eta[pow(gen,k,q)]=(-1)**k
    inv=np.array([0]+[pow(k,-1,q) for k in range(1,q)],np.int64)
    f=np.zeros(W,np.int64);f[0]=1 if q==7 else 5;f[1]=f[3]=1
    return ex,eta,inv,f

@njit(cache=True,parallel=True)
def build(q,d,f,ex,eta,inv):
    ns=np.empty((q**d,W),np.int64);mu=np.zeros(q**d,np.int64)
    nu=np.zeros(q**d,np.int64);phase=np.full(q**d,-1,np.int64)
    for i in prange(q**d):
        n=decode(i,q,d);ns[i]=n
        if d==0:mu[i]=nu[i]=1;phase[i]=0;continue
        der=np.zeros(W,np.int64)
        for j in range(1,d+1):der[j-1]=j*n[j]%q
        dd=d-1
        while dd>=0 and der[dd]==0:dd-=1
        R=0 if dd<0 else resultant(n,d,der,dd,q,inv)
        if R:
            sign=-1 if (d*(d-1)//2)&1 else 1
            mu[i]=(-1)**d*eta[R*sign%q];phase[i]=ex[R]
        nu[i]=eta[resultant(f,3,n,d,q,inv)]
    return ns,mu,nu,phase

@njit(cache=True)
def divisor_lists(q,d,allns,allmu,offset):
    count=np.zeros(q**d,np.int64)
    divs=np.zeros((q**d,2**d),np.int32)
    for l in range(d+1):
        for i in range(q**l):
            if not allmu[l][i]:continue
            ell=allns[l][i]
            for j in range(q**(d-l)):
                if not allmu[d-l][j]:continue
                n=multiply(ell,l,allns[d-l][j],d-l,q)
                ix=encode(n,d,q)
                if allmu[d][ix]:
                    divs[ix,count[ix]]=offset[l]+i;count[ix]+=1
    return divs,count

@njit(cache=True)
def divisor_degree_totals(d,mu,nu,divs,dc,flatmu,flatdeg):
    totals=np.zeros(d+1,np.int64)
    for i in range(len(mu)):
        if not(mu[i] and nu[i]):continue
        for j in range(dc[i]):
            k=divs[i,j];totals[flatdeg[k]]+=flatmu[k]
    return totals

class Field:
    def __init__(self,q,D):
        assert (q==7 and 0<=D<=7) or (q==13 and 0<=D<=5), 'enumeration and int64 audit cover q=7,D<=7 and q=13,D<=5'
        self.q=q;self.D=D;self.ex,self.eta,self.inv,self.f=tables(q)
        self.ns=[];self.mu=[];self.nu=[];self.phase=[];self.divs=[];self.dc=[]
        self.offset=np.array([sum(q**j for j in range(d)) for d in range(D+2)],np.int64)
        for d in range(D+1):
            n,m,v,p=build(q,d,self.f,self.ex,self.eta,self.inv)
            self.ns.append(n);self.mu.append(m);self.nu.append(v);self.phase.append(p)
        from numba.typed import List
        N=List(self.ns);M=List(self.mu)
        for d in range(D+1):
            dv,dc=divisor_lists(q,d,N,M,self.offset);self.divs.append(dv);self.dc.append(dc)
        self.flatmu=np.concatenate(self.mu)
        self.flatns=np.concatenate(self.ns)
        self.flatdeg=np.concatenate([np.full(q**d,d,np.int64) for d in range(D+1)])
        self.flatnu=np.concatenate(self.nu)
        self._diag={}
    def diagonal_masks(self,d):
        if d not in self._diag:
            self._diag[d]=list(map(int,divisor_degree_totals(d,self.mu[d],self.nu[d],self.divs[d],self.dc[d],self.flatmu,self.flatdeg)))
        return self._diag[d]
    def diagonal_weight(self,d):
        # phi(n) = sum_{k|n} mu(k) q^(d-deg k)
        return sum(c*self.q**(d-k) for k,c in enumerate(self.diagonal_masks(d)))

@njit(cache=True,parallel=True)
def direct_degree(q,D,h,ns,mu,nu,inv,ex):
    out=np.zeros(q**h,np.int64)
    for iv in prange(q**h):
        v=decode(iv,q,h);a=0;b=0
        for i in range(len(mu)):
            if not(mu[i] and nu[i]):continue
            r=resultant(ns[i],D,v,h,q,inv)
            if r:
                e=ex[r];a+=mu[i]*nu[i]*PAIR[e,0];b+=mu[i]*nu[i]*PAIR[e,1]
        out[iv]=a*a+a*b+b*b
    return out

@njit(cache=True)
def direct_value(q,D,u,h,ns,mu,nu,inv,ex):
    out=np.zeros(2,np.int64)
    for i in range(len(mu)):
        if not(mu[i] and nu[i]):continue
        r=resultant(ns[i],D,u,h,q,inv)
        if r:out+=mu[i]*nu[i]*PAIR[ex[r]]
    return out

@njit(cache=True)
def selected_columns(q,d,g,G,k,K,ns,mu,nu,phase,ex,inv):
    coeff=np.full(len(mu),-1,np.int64)
    for i in range(len(mu)):
        if not(mu[i] and nu[i]):continue
        if G and not resultant(ns[i],d,g,G,q,inv):continue
        r=resultant(ns[i],d,k,K,q,inv)
        if r:coeff[i]=(phase[i]+ex[r]+(0 if nu[i]==1 else 3))%6
    return coeff

@njit(cache=True,parallel=True)
def dual_degree(q,d,r,ns,coeff,divs,dc,flatmu,inv,ex):
    """Sum_l mu(l)|sum_{l|a}F_a(v)|^2 per monic v, entirely int64."""
    out=np.zeros(q**r,np.int64)
    nd=len(flatmu)
    for iv in prange(q**r):
        v=decode(iv,q,r);sa=np.zeros(nd,np.int64);sb=np.zeros(nd,np.int64)
        for i in range(len(coeff)):
            e=coeff[i]
            if e<0:continue
            z=resultant(ns[i],d,v,r,q,inv)
            if not z:continue
            ee=(e-ex[z])%6;a=PAIR[ee,0];b=PAIR[ee,1]
            for j in range(dc[i]):
                k=divs[i,j];sa[k]+=a;sb[k]+=b
        total=0
        for j in range(nd):total+=flatmu[j]*(sa[j]*sa[j]+sa[j]*sb[j]+sb[j]*sb[j])
        out[iv]=total
    return out

def poisson(F,D,hmin,verbose=True):
    q=F.q
    assert D>=1 and hmin>=0
    weight=F.diagonal_weight(D)
    totals={h:(q**(h+1-D)*weight if h>=D-1 else sum(c*q**max(h-k+1,0) for k,c in enumerate(F.diagonal_masks(D)))) for h in range(hmin,2*D+1)}
    for G in range(min(D,max(0,2*D-hmin-1))):
        d=D-G
        for ig in range(q**G):
            if not(F.mu[G][ig] and F.nu[G][ig]):continue
            g=F.ns[G][ig]
            for ik in F.divs[G][ig,:F.dc[G][ig]]:
                K=int(F.flatdeg[ik]);k=F.flatns[ik];rmax=min(2*d-2,2*d-hmin+K-2)
                if rmax<0:continue
                coeff=selected_columns(q,d,g,G,k,K,F.ns[d],F.mu[d],F.nu[d],F.phase[d],F.ex,F.inv)
                prefix=0
                for r in range(rmax+1):
                    t=time.monotonic()
                    vals=dual_degree(q,d,r,F.ns[d],coeff,F.divs[d],F.dc[d],F.flatmu[:F.offset[d+1]],F.inv,F.ex)
                    value=(q-1)*sum(map(int,vals));prefix+=value
                    h=2*d+K-2-r
                    if h>=hmin:
                        exponent=h-K+1-d
                        scale=q**exponent if exponent>=0 else Fraction(1,q**(-exponent))
                        totals[h]+=int(F.flatmu[ik])*scale*prefix
                    if verbose and G==0:
                        print(f'DUAL q={q} D={D} g=1 k=1 r={r} signed_shell={value} signed_prefix={prefix} seconds={time.monotonic()-t:.3f}',flush=True)
                # For h with larger dual ball than rmax there is none; h>=2d+K-1 has zero.
        if verbose:print(f'POISSON_STAGE q={q} D={D} gcd_degree={G} done',flush=True)
    for h,s in totals.items():
        assert Fraction(s).denominator==1,(D,h,s)
        totals[h]=int(s)
    return totals

def audit():
    for q in (7,13):
        F=Field(q,3)
        print('FIELD',q,'f=',list(map(int,F.f[:4])),flush=True)
        for D in (1,2,3):
            direct={};s=0
            for h in range(2*D+1 if D<=2 else D+2):
                if h>=2*D-1:s=q**(h+1-D)*F.diagonal_weight(D)
                else:s+=(q-1)*sum(map(int,direct_degree(q,D,h,F.ns[D],F.mu[D],F.nu[D],F.inv,F.ex)))
                direct[h]=s
            dual=poisson(F,D,0,False)
            for h in set(direct)&set(dual):assert direct[h]==dual[h],(q,D,h,direct[h],dual[h])
            print('AUDIT',q,D,'DIRECT',direct,'POISSON',dual,'PASS',flush=True)
    print('AUDIT PASS: independent direct rows agree with the signed divisor-norm Poisson formula.')

def full_table(reuse=False):
    """Recompute by default; --reuse explicitly assembles saved exact certificates."""
    from shortrow_reconstruct import run as reconstruct
    allcells={}; lines=['| q | D | h | S (exact) | S/q^(D+h+1) (exact) | c_D |','|---:|---:|---:|---:|---:|---:|']
    for q,Dmax,hmax in [(7,6,5),(13,5,5)]:
        fn=HERE/f'cells_{q}_reconstruct.json'
        rec=json.loads(fn.read_text()) if reuse and fn.exists() else reconstruct(q,Dmax,hmax)
        F=Field(q,Dmax)
        allcells[f'{q},0,0']=q
        line=f'| {q} | 0 | 0 | {q} | 1 | undefined |'
        lines.append(line);print(line,flush=True)
        for D in range(1,Dmax+1):
            fn=HERE/f'cells_{q}_{D}_poisson.json'
            po={int(h):int(s) for h,s in json.loads(fn.read_text()).items()} if reuse and fn.exists() else poisson(F,D,D)
            fn.write_text(json.dumps(po,indent=2)+'\n')
            for h in range(2*D+1):
                key=f'{D},{h}'
                if key in rec and h in po:assert int(rec[key])==po[h],(q,D,h,rec[key],po[h])
                s=int(rec[key]) if key in rec else po[h]
                allcells[f'{q},{D},{h}']=s
                ratio=Fraction(s,q**(D+h+1));c=log(float(ratio),q)/D
                line=f'| {q} | {D} | {h} | {s} | {ratio} | {c:.12f} |'
                lines.append(line);print(line,flush=True)
        # Exact comparison to every saved Q2 mean-square cell.
        import re
        old=(HERE.parents[2]/'astra-2026-10-23/qrh-transpose/checks/output_ff.txt').read_text()
        block=old.split(f'FIELD q={q},')[1].split('FIELD q=')[0]
        checked=0
        for D,h,s in re.findall(r'(?:DIRECT|COMPLETE) D=(\d+) h=(\d+).*? S=(\d+)',block):
            assert allcells[f'{q},{D},{h}']==int(s);checked+=1
        print(f'Q2_CELL_COMPARISON q={q} checked={checked} PASS',flush=True)
    (HERE/'cells_all.json').write_text(json.dumps(allcells,indent=2)+'\n')
    (HERE/'table_all.md').write_text('\n'.join(lines)+'\n')
    glines=['| q | D | target ϑ | h=floor((1+ϑ)D) | actual h/D−1 | exact R | log_q(R)/D |','|---:|---:|---:|---:|---:|---:|---:|']
    for q,Dmax in [(7,6),(13,5)]:
        for D in range(1,Dmax+1):
            for j in range(6):
                h=(5+j)*D//5;s=allcells[f'{q},{D},{h}'];R=Fraction(s,q**(D+h+1))
                line=f'| {q} | {D} | {Fraction(j,5)} | {h} | {Fraction(h-D,D)} | {R} | {log(float(R),q)/D:.12f} |'
                glines.append(line);print('GROWTH',line,flush=True)
    (HERE/'table_growth.md').write_text('\n'.join(glines)+'\n')
    for q,Dmax in [(7,6),(13,5)]:
        vals=[(Fraction(allcells[f'{q},{D},{h}'],q**(D+h+1)),D,h) for D in range(1,Dmax+1) for h in range(D,2*D+1)]
        print('EXACT_RANGE',q,'min_R,D,h=',min(vals),'max_R,D,h=',max(vals),flush=True)
        for D in range(1,Dmax+1):
            h=D;s=allcells[f'{q},{D},{h}'];R=Fraction(s,q**(D+h+1))
            print(f'CRITICAL q={q} D={D} h={h} R={R} qR={q*R} c={log(float(R),q)/D:.12f} beta={1+log(float(R),q)/D:.12f}',flush=True)
    q=13;D=5;h=5;F=Field(q,D);delta=q**(h+1-D)*F.diagonal_weight(D);s=allcells[f'{q},{D},{h}']
    print('MISSING_CELL_DIAGONAL',delta,'OFF_DIAGONAL',s-delta,'S',s,flush=True)
    print('TABLE PASS: every requested cell computed, overlaps and all Q2 cells agree. No asymptotic assertion follows from a finite table.',flush=True)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--audit',action='store_true');ap.add_argument('--poisson',nargs=3,type=int,metavar=('q','D','hmin'));ap.add_argument('--table',action='store_true');ap.add_argument('--reuse',action='store_true');args=ap.parse_args()
    if args.audit:audit()
    elif args.poisson:
        q,D,h=args.poisson;t=time.monotonic();F=Field(q,D);print('BUILD seconds',time.monotonic()-t,flush=True)
        result=poisson(F,D,h)
        for h,s in result.items():print(f'CELL q={q} D={D} h={h} S={s} R={Fraction(s,q**(D+h+1))} c={log(s/q**(D+h+1),q)/D:.12f}',flush=True)
        (HERE/f'cells_{q}_{D}_poisson.json').write_text(json.dumps(result,indent=2)+'\n')
        print('TOTAL_SECONDS',time.monotonic()-t,flush=True)
    else:full_table(args.reuse)
if __name__=='__main__':main()
