"""REFUTE lane, 2026-10-06. Independent brute force of curve-bridge.md §3 on E1: y^2+xy=x^3+1 over F_2.
h^0(nO - E) by F_2-linear algebra on L(nO) = <x^i (2i<=n), x^i y (2i+3<=n)>, compared with Riemann-Roch + Abel-Jacobi.
F_4 = {0,1,w,w^2} coded 0,1,2,3 (w^2=w+1). Written from the statements only."""
import itertools
add=lambda a,b:a^b
def mul(a,b):
    r=0
    for i in range(2):
        if (b>>i)&1: r^=a<<i
    if r&4: r^=0b111
    return r
def inv(a): return [None,1,3,2][a]
def pw(a,k):
    r=1
    for _ in range(k): r=mul(r,a)
    return r
pts=[(x,y) for x in range(4) for y in range(4) if add(add(mul(y,y),mul(x,y)), add(pw(x,3),1))==0]
O=None
def neg(P): return None if P is None else (P[0],add(P[1],P[0]))
def ecadd(P,Q):
    if P is None: return Q
    if Q is None: return P
    if P==neg(Q): return None
    x1,y1=P; x2,y2=Q
    if P==Q: lam=mul(add(mul(x1,x1),y1),inv(x1))
    else: lam=mul(add(y2,y1),inv(add(x2,x1)))
    x3=add(add(add(mul(lam,lam),lam),x1),x2)          # a1=1,a2=0
    y3=add(mul(add(lam,1),x3),add(y1,mul(lam,x1)))    # -(lam+a1)x3 - nu, char 2
    return (x3,y3)
frob=lambda P:(mul(P[0],P[0]),mul(P[1],P[1]))
rat=[P for P in pts if frob(P)==P]
deg2=[]
for P in pts:
    if frob(P)!=P and not any(P in pl for pl in deg2): deg2.append((P,frob(P)))
print('E1(F_2) affine:',rat,' #E(F_2) =',len(rat)+1,'; degree-2 places:',len(deg2), ' #E(F_4)=',len(pts)+1)
def h0(n, E):
    # basis functions
    B=[('x',i) for i in range(0,n//2+1) if 2*i<=n]+[('xy',i) for i in range(0,n) if 2*i+3<=n]
    if n<0: return 0
    ev=lambda f,P: pw(P[0],f[1]) if f[0]=='x' else mul(pw(P[0],f[1]),P[1])
    rows=[]   # F_2 conditions: each F_4 value gives 2 bits
    for P in E:
        vals=[ev(f,P) for f in B]
        for bit in range(2): rows.append([(v>>bit)&1 for v in vals])
    # rank over F_2
    m=[r[:] for r in rows]; rank=0; ncol=len(B)
    for c in range(ncol):
        piv=next((i for i in range(rank,len(m)) if m[i][c]),None)
        if piv is None: continue
        m[rank],m[piv]=m[piv],m[rank]
        for i in range(len(m)):
            if i!=rank and m[i][c]: m[i]=[a^b for a,b in zip(m[i],m[rank])]
        rank+=1
    return ncol-rank
ntest=0; bad=0
places=[(P,) for P in rat]+deg2
for n in range(-1,7):
    for k in range(0,len(places)+1):
        for Es in itertools.combinations(places,k):
            dE=sum(len(p) for p in Es)
            if dE>n+1: continue
            pts_E=[P for p in Es for P in p]
            got=h0(n,pts_E) if n>=0 else 0
            d=n-dE
            if d>0: pred=d
            elif d<0: pred=0
            else:
                s=None
                for P in pts_E: s=ecadd(s,P)
                pred=1 if s is None else 0
            ntest+=1; bad+=(got!=pred)
print(f'{ntest} divisors nO-E (n=-1..6, E reduced, places of degree <=2): mismatches with RR + Abel-Jacobi: {bad}')
print('h0(nO), n=-1..6:',[h0(n,[]) if n>=0 else 0 for n in range(-1,7)])
