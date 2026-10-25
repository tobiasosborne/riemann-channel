#!/usr/bin/env python3
"""Exhaust ALL primitive characters of ALL monic moduli deg 1..4 over F_3,F_5.
Includes reducible and non-squarefree (wild) moduli. Build unit-group generators,
sum each character over monics from scratch, then Newton/Levinson. No L zeros.
Every character and all its alpha values are printed to output_ff_all.txt.
Summary and problematic near-termination checks go to stdout.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import itertools as it
from collections import Counter
from functools import lru_cache
from math import lcm, prod, sqrt
from pathlib import Path
import numpy as np
import sympy as sy
import mpmath as mp
HERE=Path(__file__).resolve().parent


def trim(a):
    a=list(a)
    while a and a[-1]==0: a.pop()
    return tuple(a)
def monics(q,d): return (tuple(a)+(1,) for a in it.product(range(q),repeat=d))
def mul(a,b,q):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%q
    return trim(c)
def div(a,b,q):
    a=list(a); c=[0]*max(0,len(a)-len(b)+1)
    for i in range(len(a)-len(b),-1,-1):
        t=a[i+len(b)-1]*pow(b[-1],-1,q)%q; c[i]=t
        for j,x in enumerate(b): a[i+j]=(a[i+j]-t*x)%q
    return trim(c),trim(a[:len(b)-1])
def mod(a,b,q): return div(a,b,q)[1]
def enc(a,q): return sum(v*q**i for i,v in enumerate(a))
def dec(x,q,d):
    a=[]
    for _ in range(d): a.append(x%q); x//=q
    return trim(a)
def power(a,n,f,q):
    r=(1,)
    while n:
        if n&1: r=mod(mul(r,a,q),f,q)
        a=mod(mul(a,a,q),f,q); n//=2
    return r
def factor(f,q,primes):
    ans=[]; rem=f
    for P in primes:
        if len(P)>len(rem): break
        e=0
        while len(rem)>=len(P) and not mod(rem,P,q): rem=div(rem,P,q)[0]; e+=1
        if e: ans.append((P,e))
    assert rem==(1,)
    return ans


@lru_cache(None)
def local(q,P,e):
    f=(1,)
    for _ in range(e): f=mul(f,P,q)
    d=len(f)-1; Q=q**(len(P)-1); order=(Q-1)*Q**(e-1)
    # Teichmuller lift: raise a residue generator to Q^(e-1), killing p-part.
    for a in it.product(range(q),repeat=len(P)-1):
        a=trim(a)
        if a and all(power(a,(Q-1)//ell,P,q)!=(1,) for ell in sy.factorint(Q-1)):
            gen=power(a,Q**(e-1),f,q); break
    gens=[gen]; orders=[Q-1]
    tab={}; x=(1,)
    for j in range(Q-1): tab[x]=(j,); x=mod(mul(x,gen,q),f,q)
    assert x==(1,) and len(tab)==Q-1
    # Principal units: greedily choose a maximal-order direct cyclic factor.
    candidates=[]
    for a in it.product(range(q),repeat=d):
        a=trim(a)
        if mod(a,P,q)!=(1,): continue
        x=a; o=1
        while x!=(1,): x=mod(mul(x,a,q),f,q); o+=1
        candidates.append((o,a))
    for o,a in sorted(candidates,reverse=True):
        if len(tab)==order: break
        powers=[(1,)]
        for j in range(1,o): powers.append(mod(mul(powers[-1],a,q),f,q))
        if any(x in tab for x in powers[1:]): continue
        old=tab; tab={}
        for x,coord in old.items():
            for j,y in enumerate(powers): tab[mod(mul(x,y,q),f,q)]=coord+(j,)
        gens.append(a); orders.append(o)
    assert len(tab)==order
    params=np.array(list(it.product(*[range(o) for o in orders])),dtype=np.int64)
    D=lcm(*orders); scales=np.array([D//o for o in orders])
    if e==1:
        primitive=np.any(params!=0,axis=1)
    else:
        prev=(1,)
        for _ in range(e-1): prev=mul(prev,P,q)
        kernel=[]
        for a in it.product(range(q),repeat=len(P)-1):
            h=list(mul(trim(a),prev,q))
            if not h: h=[0]
            h[0]=(h[0]+1)%q
            kernel.append(tab[trim(h)])
        primitive=np.any((params@(np.array(kernel)*scales).T)%D!=0,axis=1)
    return f,tuple(gens),tuple(orders),tab,params[primitive]


def fmt(z):
    z=complex(z)
    if abs(z.imag)<2e-10: return f'{z.real:.11g}'
    return f'{z.real:.11g}{z.imag:+.11g}i'


def calc_alpha(co,q):
    d=len(co)-1
    if d==0: return [],0,0
    c=[complex(d)]
    for k in range(1,d+1):
        v=-k*co[k]
        for j in range(1,k): v-=co[j]*c[k-j]*q**((k-j)/2)
        c.append(v/q**(k/2))
    phi=np.array([1+0j]); h=d; aa=[]; minmargin=1.
    for k in range(d):
        a=np.conj(np.dot(phi,c[1:k+2]))/h; aa.append(a)
        r=1-abs(a)**2
        if abs(r)<2e-8: return aa,0,minmargin
        if r < -2e-8: return aa,abs(r),minmargin
        minmargin=min(minmargin,r)
        phi=np.r_[0,phi]-np.conj(a)*np.r_[np.conj(phi[::-1]),0]
        h*=r
    return aa,abs(1-abs(aa[-1])**2),minmargin


def high_precision(exps,D,masks,even,q):
    mp.mp.dps=75
    roots=[mp.exp(2j*mp.pi*k/D) for k in range(D)]
    coeff=[]
    for mask in masks:
        count=Counter(int(x) for x in exps[mask] if x>=0)
        coeff.append(sum(n*roots[k] for k,n in count.items()))
    if even: coeff=list(it.accumulate(coeff))[:-1]
    d=len(coeff)-1
    if not d: return [],coeff,0
    c=[mp.mpf(d)]
    for k in range(1,d+1):
        v=-k*coeff[k]-sum(coeff[j]*c[k-j]*mp.mpf(q)**(mp.mpf(k-j)/2) for j in range(1,k))
        c.append(v/mp.mpf(q)**(mp.mpf(k)/2))
    phi=[mp.mpc(1)]; h=mp.mpf(d); aa=[]
    for k in range(d):
        a=mp.conj(sum(phi[j]*c[j+1] for j in range(len(phi))))/h; aa.append(a)
        r=1-abs(a)**2
        if abs(r)<mp.mpf('1e-60'): return aa,coeff,abs(r)
        assert r>0,(coeff,aa)
        phi=[x-mp.conj(a)*y for x,y in zip([0]+phi,[mp.conj(x) for x in phi[::-1]]+[0])]
        h*=r
    raise AssertionError(('no terminal',coeff,aa))


def main():
    totals=Counter(); rankstats=Counter(); err=0.; margin=1.; repeats=[]; small=[]
    collisions={}; collision=None; sqcollisions={}; sqcollision=None
    prime_power_err=0.; minsep=1.; hpchecks=0
    with (HERE/'output_ff_all.txt').open('w') as out:
        out.write('q | f coefficients ascending | local generators and orders in # modulus lines | character tuple | parity | completed Lambda coefficients ascending | alpha (terminal included)\n')
        for q in [3,5]:
            primes=[]
            for d in range(1,5):
                for f in monics(q,d):
                    if not any(not mod(f,P,q) for P in primes if 2*(len(P)-1)<=d): primes.append(f)
            primes.sort(key=lambda P:(len(P),P))
            for d in range(1,5):
                mon=[a for k in range(d) for a in monics(q,k)]
                degrees=np.array([len(a)-1 for a in mon])
                masks=[degrees==k for k in range(d)]
                # For aggregate-data ambiguity tests, prime indicators of degree 1..3.
                isprime=np.array([a in primes for a in mon])
                issquarefree=np.array([not any(not mod(a,mul(P,P,q),q) for P in primes if 2*(len(P)-1)<=len(a)-1) for a in mon])
                for f in monics(q,d):
                    fac=factor(f,q,primes); loc=[local(q,P,e) for P,e in fac]
                    orders=sum((list(l[2]) for l in loc),[]); D=lcm(*orders)
                    params=np.array([sum((tuple(x) for x in pp),()) for pp in it.product(*[l[4] for l in loc])],dtype=np.int64)
                    if not len(params): continue
                    coords=[]; unit=np.ones(len(mon),bool); const=[]
                    for modulus,gens,oo,tab,pp in loc:
                        arr=[]
                        for i,a in enumerate(mon):
                            coo=tab.get(mod(a,modulus,q)); unit[i]&=coo is not None
                            arr.append(coo if coo is not None else (0,)*len(oo))
                        coords.append(np.array(arr))
                        const.extend(tab[(2,)]) # 2 generates F_3^*,F_5^*.
                    coords=np.concatenate(coords,axis=1)
                    scales=np.array([D//o for o in orders],dtype=np.int64)
                    exps=(params@(coords*scales).T)%D; exps[:,~unit]=-1
                    values=np.exp(2j*np.pi*exps/D); values[:,~unit]=0
                    even=(params@(np.array(const)*scales))%D==0
                    sums=np.column_stack([values[:,mask].sum(axis=1) for mask in masks])
                    prime_sums=np.column_stack([values[:,(degrees==k)&isprime].sum(axis=1) for k in range(1,d)]) if d>1 else np.empty((len(params),0))
                    square_sums=np.column_stack([values[:,(degrees==k)&issquarefree].sum(axis=1) for k in range(1,d)]) if d>1 else np.empty((len(params),0))
                    # Euler log coefficients from all individual prime values, including powers.
                    for k in range(1,d):
                        logc=np.zeros(len(params),complex)
                        for ell in range(1,k+1):
                            if k%ell==0: logc+=ell*(values[:,(degrees==ell)&isprime]**(k//ell)).sum(axis=1)
                        # Coefficient identity k S_k=sum_{j<=k} logc_j S_{k-j} checked below.
                        if k==1: logs=[]
                        logs.append(logc)
                        rhs=sum(logs[j-1]*sums[:,k-j] for j in range(1,k+1))
                        prime_power_err=max(prime_power_err,float(np.max(np.abs(k*sums[:,k]-rhs))))
                    out.write(f'# modulus q={q} f={f} local='+repr([(l[0],l[1],l[2]) for l in loc])+'\n')
                    for row,param in enumerate(params):
                        co=sums[row].copy(); ev=bool(even[row])
                        if ev:
                            assert abs(co.sum())<1e-9
                            co=np.cumsum(co)[:-1]
                        aa,er,mar=calc_alpha(co,q); deg=len(co)-1
                        W=co[-1]/q**(deg/2)
                        fe=max(abs(co[j]/q**(j/2)-W*np.conj(co[deg-j])/q**((deg-j)/2)) for j in range(deg+1))
                        err=max(err,er,fe,abs(abs(W)-1))
                        if deg: margin=min(margin,mar)
                        rank=len(aa); totals[q,d]+=1; rankstats[q,d,deg,rank]+=1
                        desc=(q,f,tuple(int(x) for x in param),ev)
                        if rank<deg or (deg and mar<1e-5) or (d==3 and len(small)<5):
                            hp,hco,he=high_precision(exps[row],D,masks,ev,q); hpchecks+=1
                            assert len(hp)==rank
                            if rank<deg and len(repeats)<8: repeats.append((desc,[fmt(x) for x in co],[fmt(x) for x in hp],mp.nstr(he,4)))
                            if d==3 and len(small)<5: small.append((desc,[fmt(x) for x in co],[fmt(x) for x in hp]))
                        if deg==3:
                            # Equal q, degree, W and unweighted prime/squarefree sums through 2.
                            quant=lambda vals:tuple((round(complex(z).real,8),round(complex(z).imag,8)) for z in vals)
                            key=(q,quant([W,*prime_sums[row,:2]]))
                            val=(desc,[fmt(x) for x in co],[fmt(x) for x in aa],aa[1])
                            if key in collisions and abs(val[-1]-collisions[key][-1])>1e-6 and collision is None:
                                collision=(key,collisions[key][:-1],val[:-1])
                            collisions[key]=val
                            key=(q,quant([W,*square_sums[row,:2]]))
                            if key in sqcollisions and abs(val[-1]-sqcollisions[key][-1])>1e-6 and sqcollision is None:
                                sqcollision=(key,sqcollisions[key][:-1],val[:-1])
                            sqcollisions[key]=val
                        out.write(f'{q} | {f} | {tuple(param.tolist())} | {"even" if ev else "odd"} | '+','.join(fmt(x) for x in co)+' | '+','.join(fmt(x) for x in aa)+'\n')
                expected=q*q-2*q if d==1 else (q-1)**2*q**(2*d-2)
                assert totals[q,d]==expected,(q,d,totals[q,d],expected)
                print('CENSUS',q,d,'primitive=',totals[q,d],flush=True)
    print('TOTAL',sum(totals.values()),'all primitive, including wild')
    print('RANK COUNTS (q, conductor degree, completed degree, support rank):')
    for k,v in sorted(rankstats.items()): print(k,v)
    print('max numerical FE/terminal defect',err,'min nonterminal pivot factor',margin)
    print('max Euler log coefficient identity defect',prime_power_err)
    print('75-digit recomputations',hpchecks)
    print('REPEATED',repeats)
    print('SMALL',small)
    print('PRIME AGGREGATE COLLISION',collision)
    print('SQUAREFREE AGGREGATE COLLISION',sqcollision)
    assert err<2e-7 and prime_power_err<1e-8
    print('PASS exhaustive conductor counts, Euler identities, FE, Schur disks and terminal boundary')


if __name__=='__main__': main()
