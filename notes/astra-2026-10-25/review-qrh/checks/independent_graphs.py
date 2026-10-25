"""Exact vertex-permutation enumeration, distinct from the lanes' prime DFS.

Enumerate det(I-z A_s+q z^2 I) as a Laurent polynomial, then use Bass.
Unsigned counts come independently from rational power-series division.
No numerical eigenvalues, RH, or imports from the lanes.
"""
from itertools import permutations, product
from collections import defaultdict, deque
from fractions import Fraction as F
from math import comb, gcd


def setup(n,edges):
    edges=sorted(edges); adj=[[] for _ in range(n)]
    for a,b in edges: adj[a].append(b);adj[b].append(a)
    seen={0}; queue=deque([0]); tree=set()
    while queue:
        a=queue.popleft()
        for b in sorted(adj[a]):
            if b not in seen:
                seen.add(b);queue.append(b);tree.add(tuple(sorted((a,b))))
    return adj,[e for e in edges if e not in tree]


def determinant(n,edges):
    adj,chords=setup(n,edges); g=len(chords);q=len(adj[0])-1
    Q=defaultdict(int); m=len(edges)
    for pi in permutations(range(n)):
        if any(pi[i]!=i and pi[i] not in adj[i] for i in range(n)): continue
        fixed=sum(pi[i]==i for i in range(n));moving=n-fixed
        inv=sum(pi[i]>pi[j] for i in range(n) for j in range(i+1,n))
        hom=[0]*g
        for i,j in enumerate(pi):
            if i==j:continue
            e=tuple(sorted((i,j)))
            if e in chords:hom[chords.index(e)]+=1 if i<j else -1
        assert all(abs(a)<=1 for a in hom)
        for k in range(fixed+1):
            for l in range(m-n+1):
                Q[(moving+2*k+2*l,tuple(hom))]+=(-1)**(inv+moving+l)*comb(fixed,k)*q**k*comb(m-n,l)
    Q={k:v for k,v in Q.items() if v}
    return Q,chords


def sampled_gram(Q,N,weights):
    a=defaultdict(int)
    for (d,h),v in Q.items():
        if d in weights:a[tuple(x%N for x in h)]+=weights[d]*v
    return sum(v*v for v in a.values())


def haar(Q,weights):
    a=defaultdict(int)
    for (d,h),v in Q.items():
        if d in weights:a[h]+=weights[d]*v
    return sum(v*v for v in a.values())


def flux_poly(Q,s):
    out=[0]*(1+max(d for d,h in Q))
    for (d,h),v in Q.items():out[d]+=v*(-1 if sum(a*b for a,b in zip(h,s))%2 else 1)
    return out


def unsigned(Q,s,cap=16):
    den=flux_poly(Q,s);num=flux_poly(Q,(0,)*len(s));out=[1]+[0]*cap
    for d in range(1,cap+1):
        out[d]=(num[d//2] if d%2==0 and d//2<len(num) else 0)-sum(den[j]*out[d-j] for j in range(1,min(d,len(den)-1)+1))
    return out


def projected_counts(Q,cap=16):
    # Integral two-dimensional homology, exact formal series Q(z^2,x^2)/Q(z,x).
    a=[defaultdict(int) for _ in range(cap+1)]
    for (d,h),v in Q.items():a[d][h[:2]]+=v
    a=[{h:v for h,v in c.items() if v} for c in a]
    C=[defaultdict(int) for _ in range(cap+1)];C[0][(0,0)]=1
    for d in range(1,cap+1):
        if d%2==0:
            for h,v in a[d//2].items():C[d][tuple(2*x for x in h)]+=v
        for j in range(1,d+1):
            for h,v in a[j].items():
                for k,w in C[d-j].items():C[d][tuple(x+y for x,y in zip(h,k))]-=v*w
        C[d]={h:v for h,v in C[d].items() if v}
        assert all(v>=0 for v in C[d].values())
    return C


graphs=[('K4',4,[(i,j) for i in range(4) for j in range(i+1,4)]),
        ('cube',8,[(0,1),(0,3),(0,4),(1,2),(1,7),(2,3),(2,6),(3,5),(4,5),(4,7),(5,6),(6,7)])]
for name,n,edges in graphs:
    Q,chords=determinant(n,edges);g=len(chords);top=2*len(edges)
    print(name,'chords=',chords,'Laurent monomials=',len(Q),'degree=',top)
    print('degree: Haar, N=2, N=3, N=4, N=5 (all normalized)')
    for d in range(top+2):
        row=[haar(Q,{d:1})]+[sampled_gram(Q,N,{d:1}) for N in (2,3,4,5)]
        assert row[0]==row[2]==row[3]==row[4]
        print(d,':',row)
    weights={d:2**d for d in range(top+1)}
    row=[haar(Q,weights)]+[sampled_gram(Q,N,weights) for N in (2,3,4,5)]
    assert row[0]==row[2]==row[3]==row[4]
    print('mixed coefficients F=sum 2^d a_d:',row)
    C=unsigned(Q,(0,)*g);print('unsigned total C0..16:',C)
    if name=='cube':
        assert all(C[d]==0 for d in range(1,17,2))
        continue
    for D in (12,13):
        ms=2**g*sampled_gram(Q,2,{D:1});diag=2**g*C[D]
        print('K4 D=',D,'S=',ms,'diagonal=',diag,'offdiagonal=',ms-diag)
    for s in product(range(2),repeat=3):
        cs=unsigned(Q,s);nums=[(C[D]+cs[D])//2 for D in (13,16)]
        assert all((C[D]+cs[D])%2==0 for D in (13,16))
        print('flux=',s,'counts D13,D16=',nums,'fractions=',[F(num,C[D]) for num,D in zip(nums,(13,16))])
    assert F((C[16]+unsigned(Q,(0,0,1))[16])//2,C[16])==F(845,1701)
    print('Q0 coefficients:',flux_poly(Q,(0,0,0)))
    print('Q0(1/2)=',sum(F(v,2**d) for d,v in enumerate(flux_poly(Q,(0,0,0)))))
    assert sum(F(v,2**d) for d,v in enumerate(flux_poly(Q,(0,0,0))))==0
    P=projected_counts(Q)
    for D in (8,12,16):
        total=sum(P[D].values());zero=P[D].get((0,0),0)
        cov=[[F(sum(v*h[i]*h[j] for h,v in P[D].items()),total*D) for j in range(2)] for i in range(2)]
        print('projected surface D=',D,'zero=',zero,'total=',total,'D*Pr0=',F(D*zero,total),'Cov/D=',cov)
for N in (2,3,6,7,12):
    rows=list(product(range(N),repeat=2));image={(6*a%N,6*b%N) for a,b in rows}
    kernel=sum(6*a%N==6*b%N==0 for a,b in rows)
    assert kernel==gcd(6,N)**2
    print('surface N=',N,'rows=',N*N,'distinct=',len(image),'kernel=',kernel)
print('PASS: exact integer permutation enumeration and series division.')
