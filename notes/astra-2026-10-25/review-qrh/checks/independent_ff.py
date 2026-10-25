"""Brute-force F7 residue fields, local factorization and exact Gauss sums.

Unlike the lane's resultant/Pellet family code, factor every modulus and
evaluate characters by exponentiation in each residue field. No lane imports.
Gauss comparisons are exact in Z[zeta_42], for ALL squarefree monics deg<=3.
"""
from itertools import product
from collections import Counter
from functools import lru_cache
from fractions import Fraction as F
import sympy as sp

q=7
logs={pow(3,j,7):j for j in range(6)}
PAIR=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))

def trim(a):
    a=list(a)
    while a and not a[-1]:a.pop()
    return tuple(a)

def divrem(a,b):
    a=list(trim(a));b=trim(b);out=[0]*max(0,len(a)-len(b)+1)
    while a and len(a)>=len(b):
        k=len(a)-len(b);c=a[-1]*pow(b[-1],-1,q)%q;out[k]=c
        for j,v in enumerate(b):a[k+j]=(a[k+j]-c*v)%q
        a=list(trim(a))
    return trim(out),tuple(a)

def mul(a,b):
    if not a or not b:return ()
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%q
    return trim(c)

def power(a,k,P):
    out=(1,);a=divrem(a,P)[1]
    while k:
        if k&1:out=divrem(mul(out,a),P)[1]
        a=divrem(mul(a,a),P)[1];k//=2
    return out

def factor(n):
    # For degree <=3, remove all linear roots. Remaining degree 2 or 3
    # with no roots is irreducible.
    f=n;out=[]
    for c in range(q):
        P=(c,1)
        while len(f)>1:
            v,r=divrem(f,P)
            if r:break
            out.append(P);f=v
    if len(f)>1:out.append(f)
    return out

@lru_cache(None)
def local_table(P):
    d=len(P)-1;out={}
    for a in product(range(q),repeat=d):
        t=trim(a)
        if not t:out[t]=None;continue
        v=power(t,(q**d-1)//6,P)
        assert len(v)==1
        out[t]=logs[v[0]]
    return out

def char_exp(u,factors):
    e=0
    for P in factors:
        a=local_table(P)[divrem(u,P)[1]]
        if a is None:return None
        e+=a
    return e%6

def monics(D):return (tuple(a)+(1,) for a in product(range(q),repeat=D))

def mu(n):
    fs=factor(n)
    return 0 if len(set(fs))!=len(fs) else (-1)**len(fs)

f=(1,1,0,1)
assert factor(f)==[f]
columns=[]
for n in monics(2):
    fs=factor(n);m=mu(n);e=char_exp(n,[f])
    nu=0 if e is None else (-1)**e
    if m:columns.append((n,fs,m*nu))
assert len(columns)==42
W=sum(__import__('math').prod(q**(len(P)-1)-1 for P in fs) for n,fs,w in columns if w)
print('F7 D=2 squarefree columns=',len(columns),'weighted diagonal=',W)

def row(u):
    a=b=0
    for n,fs,w in columns:
        e=char_exp(u,fs)
        if e is not None:a+=w*PAIR[e][0];b+=w*PAIR[e][1]
    return a,b

# Literal enumeration includes zero and all q-1 leading coefficients.
S=0
for h in range(5):
    for a in product(range(q),repeat=h):
        for lc in range(1,q):
            v,w=row(a+(lc,));S+=v*v+v*w+w*w
    predicted=F(q)**(h+1-2)*W
    print('h=',h,'rows=',q**(h+1),'S=',S,'complete formula=',predicted,'agrees=',S==predicted)
    if h>=3:assert S==predicted
print('u=0 row=',row(()),'A1=',row((1,)))
for c in range(7):
    p=(c,1);p6=(1,)
    for _ in range(6):p6=mul(p6,p)
    deletion=sum(w for n,fs,w in columns if p in fs)
    A=row(p6);B=row((1,))
    assert A==(B[0]-deletion,0)
    shorter=sum((-1)*((-1)**char_exp(P,[f])) for P in monics(1) if P!=p)
    # Exact two-scale identity; shorter sum is A_{p^6}(1).
    nu_p=(-1)**char_exp(p,[f])
    assert B[0]==A[0]-nu_p*shorter
    print('linear p=',p,'A_p6=',A,'deleted=',deletion,'two-scale identity=PASS')
for k in range(1,7):
    pi=sum(int(sp.mobius(d))*7**(k//d) for d in sp.divisors(k))//k
    print('pi_7(',k,')=',pi,'ratio to 7^k/k=',F(pi*k,7**k))
small=list(monics(1))+list(monics(2));reciprocity=0
for a in small:
    for b in small:
        ab=char_exp(a,factor(b));ba=char_exp(b,factor(a))
        if ab is None:
            assert ba is None
            continue
        assert (ab-ba-3*((q-1)//6)*(len(a)-1)*(len(b)-1))%6==0
        reciprocity+=1
print('power-reciprocity coprime ordered pairs deg<=2:',reciprocity)

# Exact cyclotomic ring represented by degree<12 integer coefficient tuples.
z=sp.Symbol('z');Phi=sp.Poly(sp.cyclotomic_poly(42,z),z)
ph=[int(Phi.nth(i)) for i in range(13)]
def reduce(a):
    a=list(a)+[0]*max(0,12-len(a))
    for k in range(len(a)-1,11,-1):
        c=a[k]
        for j in range(13):a[k-12+j]-=c*ph[j]
    return tuple(a[:12])
def times(a,b):
    out=[0]*23
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return reduce(out)
one=(1,)+(0,)*11
def cpow(a,k):
    out=one
    for _ in range(k):out=times(out,a)
    return out
def phase(e):
    a=[0]*42;a[e%42]=1;return reduce(a)
T={j:reduce([sum(1 for c in range(1,q) if (7*j*logs[c]+6*c)%42==e) for e in range(42)]) for j in range(1,6)}
checks=0;absorb=0;types=Counter();wrong_HD=0;wrong_disc=0
for D in range(1,4):
    count=0
    for n in monics(D):
        fs=factor(n)
        if len(set(fs))!=len(fs):continue
        count+=1;m=(-1)**len(fs);typ=tuple(sorted(len(P)-1 for P in fs));types[typ]+=1
        deriv=tuple(i*n[i]%q for i in range(1,D+1))
        R=1
        for P in fs:
            v=power(divrem(deriv,P)[1],(q**(len(P)-1)-1)//(q-1),P)
            assert len(v)==1 and v[0]
            R=R*v[0]%q
        # Res(n,n') is product of n' at roots, not the discriminant itself.
        disc=((-1)**(D*(D-1)//2)*R)%q
        assert (-1)**logs[disc]==(-1)**D*m
        hist={j:[0]*42 for j in range(1,6)}
        for a in product(range(q),repeat=D):
            e=char_exp(trim(a),fs)
            if e is None:continue
            for j in range(1,6):hist[j][(7*j*e+6*a[-1])%42]+=1
        G={j:reduce(hist[j]) for j in range(1,6)}
        for j in range(1,6):
            base=times(phase(7*j*logs[R]),cpow(T[j],D))
            rhs=tuple(m*(-1)**D*c for c in base)
            assert G[j]==rhs,(n,j,G[j],rhs)
            wrong_HD+=G[j]!=base
            wrong=tuple(m*(-1)**D*c for c in times(phase(7*j*logs[disc]),cpow(T[j],D)))
            wrong_disc+=G[j]!=wrong
            checks+=1
        lhs=tuple(m*c for c in times(G[5],cpow(T[2],D)))
        sgn=(-1)**D*(-1)**logs[(-1)**(D*(D-1)//2)%q]
        rhs=tuple(sgn*c for c in times(cpow(T[5],D),G[2]))
        assert lhs==rhs
        absorb+=1
    print('Gauss degree=',D,'all squarefree monics=',count,'characters per modulus=5')
print('factorization types=',dict(sorted(types.items())))
print('exact Gauss comparisons=',checks,'absorption comparisons=',absorb)
print('omitting Hasse-Davenport sign fails=',wrong_HD,'using disc in place of Res fails=',wrong_disc)
print('unit modulus n=1: five Gauss formulas and absorption are the one-term identity 1=1')
print('PASS: all computations exact; Gauss normalization q^(-D/2) cancels on both sides.')
