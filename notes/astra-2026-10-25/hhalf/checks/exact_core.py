"""Exact dual Euler extraction. All coefficients are integers until final division.

The dual reconstruction formula is derived in astra-proofs.md; it enumerates
monic f of degree <= m-1 to obtain the raw coefficient of u^(2m).
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from functools import lru_cache
from math import comb
from itertools import combinations
from fractions import Fraction
from flint import fmpz_poly, nmod_poly, fq_default_ctx, fq_default_poly_ctx
sys.path.insert(0,str(Path(__file__).parent/'reproduced'))
import common as old

@lru_cache(None)
def divisors(n):return tuple(i for i in range(1,n+1) if n%i==0)
@lru_cache(None)
def prime_count(q,n):return (q**n-sum(d*prime_count(q,d) for d in divisors(n) if d<n))//n

class Field:
    def __init__(self,q):
        self.q=q
        if q==9:
            self.K=fq_default_ctx(3,2,'a');self.R=fq_default_poly_ctx(self.K)
            self.elements=[self.K(i%3)+(i//3)*self.K.gen() for i in range(9)]
            self.codes={tuple(int(c) for c in v.to_list()):i for i,v in enumerate(self.elements)}
    def poly(self,a):
        if self.q==9:return self.R([self.elements[i] for i in a])
        return nmod_poly(list(a),self.q)
    def tup(self,f):
        if self.q==9:return tuple(self.codes[tuple(int(c) for c in v.to_list())] for v in f)
        return tuple(map(int,f))
    @lru_cache(None)
    def factors(self,a):return tuple(sorted((self.tup(p),int(e)) for p,e in self.poly(a).factor()[1]))
    def mul(self,a,b):return self.tup(self.poly(a)*self.poly(b))
    @lru_cache(maxsize=100000)
    def jacobi(self,a,b):
        if self.q!=9:return old.jacobi(self.q,a,b)
        v=1
        for p,e in self.factors(b):
            x=self.poly(a).pow_mod((9**(len(p)-1)-1)//2,self.poly(p))
            if not x:return 0
            if e%2 and x.constant_coefficient()!=self.K.one():v=-v
        return v
    @lru_cache(None)
    def primitive_L(self,h):
        if len(h)==1:return ()
        d=len(h)-1;g=(d-1)//2
        if self.q!=9 and g>=2:
            low=[1]+[0]*g;hp=self.poly(h)
            for r,P in prime_moduli(self.q,g):
                v=int(hp.resultant(P));v=pow(v,(self.q-1)//2,self.q)
                chi=0 if v==0 else 1 if v==1 else -1
                for j in range(r,g+1):low[j]+=chi*low[j-r]
        else:
            low=[sum(self.jacobi(f,h) for f in old.monics(self.q,j)) for j in range(g+1)]
        if d%2==0:low=[sum(low[:j+1]) for j in range(g+1)]
        full=list(map(int,old.complete_quadratic(self.q,g,low)))
        if d%2==0:full=[full[0]]+[full[j]-full[j-1] for j in range(1,len(full))]+[-full[-1]]
        return tuple(full)
    @lru_cache(None)
    def character_data(self,f,nmax):
        """Numbers of primes with character +1,-1 through nmax, including imprimitive zeros."""
        fs=self.factors(f);h=(1,);zeros=[0]*(nmax+1)
        for p,e in fs:
            if len(p)-1<=nmax:zeros[len(p)-1]+=1
            if e%2:h=self.mul(h,p)
        if h==(1,):
            return tuple((prime_count(self.q,r)-zeros[r],0) for r in range(1,nmax+1))
        ell=list(self.primitive_L(h))
        for p,e in fs:
            if e%2==0:
                r=len(p)-1;c=-self.jacobi(p,h)
                ell=old.series_factor(ell+[0]*r,r,c)
        # coefficients of z L'/L = sum_k C_k z^k
        ck=[0]*(nmax+1)
        for k in range(1,nmax+1):
            ck[k]=(k*ell[k] if k<len(ell) else 0)-sum(ell[j]*ck[k-j] for j in range(1,min(k,len(ell)-1)+1))
        dif=[0]*(nmax+1);out=[]
        for r in range(1,nmax+1):
            total=prime_count(self.q,r)-zeros[r]
            raw=ck[r]-sum(k*((prime_count(self.q,k)-zeros[k]) if (r//k)%2==0 else dif[k]) for k in divisors(r) if k<r)
            assert raw%r==0
            dif[r]=raw//r
            assert (total+dif[r])%2==0 and abs(dif[r])<=total,(self.q,f,r,total,dif[r])
            out.append(((total+dif[r])//2,(total-dif[r])//2))
        return tuple(out)

@lru_cache(None)
def prime_moduli(q,g):
    return tuple((r,nmod_poly(list(p),q)) for r in range(1,g+1) for p in old.irreducibles(q,r))

@lru_cache(None)
def field(q):return Field(q)

@lru_cache(None)
def inverse_factor(r,power,degree,sign=1):
    """(1-sign*v^r)^(-power), truncated, power >=0."""
    a=[0]*(degree+1);a[0]=1
    if power:
        for k in range(1,degree//r+1):a[k*r]=comb(power+k-1,k)*sign**k
    return fmpz_poly(a)

def truncmul(a,b,N):return (a*b).truncate(N+1)

@lru_cache(None)
def signed_choose(plus,minus,k):
    return sum((-1)**j*comb(minus,j)*comb(plus,k-j) for j in range(max(0,k-plus),min(k,minus)+1))

@lru_cache(maxsize=20000)
def weighted_squarefree(H,V,counts,special):
    """[z^H] product (1+chi(P)z^r/(1-v^r)); special primes omit denominator."""
    counts=[list(x) for x in counts]
    for r,c in special:
        if c:counts[r-1][int(c<0)]-=1
    a=[fmpz_poly([1])]+[fmpz_poly([]) for _ in range(H)]
    for r,(plus,minus) in enumerate(counts,1):
        assert min(plus,minus)>=0
        if r>H:break
        terms=[]
        for k in range(1,H//r+1):
            ck=signed_choose(plus,minus,k)
            if ck:terms.append((k*r,ck*inverse_factor(r,k,V)))
        if not terms:continue
        b=list(a)
        for n in range(H+1):
            for shift,pol in terms:
                if shift<=n and a[n-shift]:b[n]+=truncmul(a[n-shift],pol,V)
        a=b
    for r,c in special:
        if c:
            for n in range(H,r-1,-1):a[n]+=c*a[n-r]
    return a[H]

@lru_cache(None)
def square_series(q,m,D):
    a=[fmpz_poly([1])]+[fmpz_poly([]) for _ in range(m)]
    for r in range(1,m+1):
        N=prime_count(q,r);terms=[]
        for k in range(1,m//r+1):
            pol=fmpz_poly([])
            for j in range(1,min(k,N)+1):pol+=comb(N,j)*comb(k-1,j-1)*inverse_factor(r,j,D,-1)
            terms.append((k*r,pol))
        b=list(a)
        for n in range(m+1):
            for shift,pol in terms:
                if shift<=n and a[n-shift]:b[n]+=truncmul(a[n-shift],pol,D)
        a=b
    sf=fmpz_poly([1,q]+[q**d-q**(d-1) for d in range(2,D+1)])
    return truncmul(a[m],sf,D)

@lru_cache(None)
def reconstruction(q,H,j):
    if H%2:
        r=(H-1)//2;out=[0]*H;out[j]=1
        if j<r:out[2*r-j]=q**(r-j)
        return tuple(out)
    r=H//2;out=[0]*H
    for i in range(j,r):out[i]+=1
    for i in range(j,r-1):out[H-2-i]+=q**(r-1-i)
    return tuple([out[0]]+[out[i]-out[i-1] for i in range(1,H)])

def nonsquare_series(q,m,D,verbose=False,n=None):
    if n is None:n=2*m
    K=field(q);V=D//2;out=[0]*(D+1);jobs={}
    characteristic=3 if q==9 else q
    # Translation orbits: normalize one nonzero-degree linear coefficient.
    # Accumulate common Euler-product keys before expensive series evaluation.
    for A in range((n-1)//2+1):
        H=n-2*A
        normalize_a=(A%characteristic!=0)
        for a in old.monics(q,A):
            if normalize_a and a[-2]!=0:continue
            aps=tuple(p for p,e in K.factors(a))
            den=fmpz_poly([1])
            for p in aps:den=truncmul(den,inverse_factor(len(p)-1,1,V),V)
            for size in range(len(aps)+1):
                for subset in combinations(aps,size):
                    b=(1,)
                    for p in subset:b=K.mul(b,p)
                    shift=len(b)-1;mu=(-1)**size
                    for j in range((H-1)//2+1):
                        if H%2 and (j+shift)%2:continue  # nonsquare scaling cancels the full orbit
                        rec=reconstruction(q,H,j)
                        normalize_f=(not normalize_a and j%characteristic!=0)
                        orbit=q if normalize_a or normalize_f else 1
                        mult=[0]*(D+1)
                        for k,c in enumerate(rec):
                            if c and k+shift<=D:mult[k+shift]+=orbit*mu*c*(-1 if q%4==3 and H*(j+shift)%2 else 1)
                        for k in range(D,1,-1):mult[k]-=q*mult[k-2]
                        den_t=fmpz_poly([int(den[k//2]) if k%2==0 else 0 for k in range(D+1)])
                        pol=truncmul(fmpz_poly(mult),den_t,D)
                        for f in old.monics(q,j):
                            if normalize_f and f[-2]!=0:continue
                            F=K.mul(f,b)
                            counts=K.character_data(F,H)
                            special=tuple(sorted((len(p)-1,K.jacobi(p,F)) for p in aps if len(p)-1<=H))
                            # h has even degree: simultaneously reverse odd-degree signs.
                            if H%2==0:
                                alt=tuple((mi,pl) if r%2 else (pl,mi) for r,(pl,mi) in enumerate(counts,1))
                                asp=tuple(sorted((r,-c if r%2 else c) for r,c in special))
                                if (alt,asp)<(counts,special):counts,special=alt,asp
                            key=(H,counts,special)
                            jobs[key]=jobs.get(key,fmpz_poly([]))+pol
        if verbose:print(f'  q={q} m={m} A={A} grouped_jobs={len(jobs)}',flush=True)
    if verbose:print(f"  nonzero_jobs={sum(bool(p) for p in jobs.values())}/{len(jobs)}",flush=True)
    for (H,counts,special),pol in jobs.items():
        if not pol:continue
        S=weighted_squarefree(H,V,counts,special)
        St=fmpz_poly([int(S[k//2]) if k%2==0 else 0 for k in range(D+1)])
        total=truncmul(pol,St,D)
        for k in range(D+1):out[k]+=int(total[k])
    if q%4==3 and n%2:out=[c*(-1)**k for k,c in enumerate(out)]
    return fmpz_poly(out),len(jobs)

def coefficient_series(q,m,D,verbose=False):
    ns,jobs=nonsquare_series(q,m,D,verbose)
    return square_series(q,m,D)+ns,jobs

def raw_series(q,n,D,verbose=False):
    if n==0:return fmpz_poly([1,q]+[q**d-q**(d-1) for d in range(2,D+1)]),0
    ns,jobs=nonsquare_series(q,n//2,D,verbose,n)
    if n%2==0:ns+=square_series(q,n//2,D)
    return ns,jobs
