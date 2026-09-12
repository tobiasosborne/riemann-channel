"""REFUTE-lane check of the determinant square-class step T7.3<1>2:
with R_n = ker P(S), D = det(A|R_n) in an F_q-basis of R_n, verify
    D^2 = det(C|R_n),   D^q = det(S|R_n) D,   hence D^{q-1} = det(S|R_n) = delta_n,
including the characteristic-divisible cases q | n.  Also re-derives T7.5's
worked examples (q=3 a=(2,1) n=1 and q=5 a=(1,1) n=2) and its table."""
import itertools, numpy as np, sympy as sp
FAIL=[]
def chk(n, ok, d=""):
    print(("  [PASS] " if ok else "  [FAIL] ")+n+("   "+d if d else ""))
    if not ok: FAIL.append(n)
def polmulmod(a,b,f,q):
    n=len(f)-1; r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b): r[i+j]=(r[i+j]+x*y)%q
    for k in range(len(r)-1,n-1,-1):
        c=r[k]
        if c:
            r[k]=0
            for j in range(n+1): r[k-n+j]=(r[k-n+j]-c*f[j])%q
    return tuple((r+[0]*n)[:n])
_I={}
def irreducible(q,n):
    if (q,n) in _I: return _I[(q,n)]
    if n==1: return (0,1)
    z=sp.symbols('z')
    for tail in itertools.product(range(q),repeat=n):
        co=list(tail)+[1]; P=sp.Poly(list(reversed(co)),z,modulus=q)
        if P.degree()==n and P.is_irreducible: _I[(q,n)]=tuple(co); return tuple(co)
class FF:
    def __init__(s,q,n): s.q,s.n,s.f=q,n,irreducible(q,n); s.one=tuple([1]+[0]*(n-1)); s.zero=tuple([0]*n)
    def mul(s,a,b): return polmulmod(list(a),list(b),s.f,s.q)
    def add(s,a,b): return tuple((x+y)%s.q for x,y in zip(a,b))
    def neg(s,a): return tuple((-x)%s.q for x in a)
    def sc(s,c,a): return tuple((c*x)%s.q for x in a)
    def pw(s,a,e):
        r=s.one
        while e:
            if e&1: r=s.mul(r,a)
            a=s.mul(a,a); e>>=1
        return r
    def inv(s,a): return s.pw(a,s.q**s.n-2)
    def frob(s,a,k=1): return s.pw(a,s.q**k)
    def trace(s,a):
        t=s.zero
        for i in range(s.n): t=s.add(t,s.frob(a,i))
        assert all(x==0 for x in t[1:]); return t[0]
    def elems(s): return [tuple(c) for c in itertools.product(range(s.q),repeat=s.n)]
def det_modp(M,p):
    A=[[int(x)%p for x in r] for r in M]; n=len(A); d=1
    for c in range(n):
        pr=next((i for i in range(c,n) if A[i][c]%p), None)
        if pr is None: return 0
        if pr!=c: A[c],A[pr]=A[pr],A[c]; d=(-d)%p
        d=(d*A[c][c])%p; iv=pow(A[c][c],p-2,p); A[c]=[(x*iv)%p for x in A[c]]
        for i in range(c+1,n):
            if A[i][c]%p:
                f=A[i][c]; A[i]=[(x-f*y)%p for x,y in zip(A[i],A[c])]
    return d%p
def nullspace(M,p):
    A=[[int(x)%p for x in r] for r in M]; m=len(A); n=len(A[0]); piv=[]; r=0
    for c in range(n):
        pr=next((i for i in range(r,m) if A[i][c]%p), None)
        if pr is None: continue
        A[r],A[pr]=A[pr],A[r]; iv=pow(A[r][c],p-2,p); A[r]=[(x*iv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%p:
                f=A[i][c]; A[i]=[(x-f*y)%p for x,y in zip(A[i],A[r])]
        piv.append(c); r+=1
    out=[]
    for fc in [c for c in range(n) if c not in piv]:
        v=[0]*n; v[fc]=1
        for i,c in enumerate(piv): v[c]=(-A[i][fc])%p
        out.append(v)
    return out
def Smat(n): return [[1 if j==(i+1)%n else 0 for j in range(n)] for i in range(n)]
def Pmat(a,n,q):
    i2=pow(2,q-2,q); S=np.array(Smat(n)); M=np.zeros((n,n),dtype=int)
    for j,aj in enumerate(a):
        M=(M+aj*i2*((np.linalg.matrix_power(S,j)%q)+(np.linalg.matrix_power(S.T,j)%q)))%q
    return M.tolist()
def detS_R(a,n,q):
    B=nullspace(Pmat(a,n,q),q)
    if not B: return 1,0,B
    d=len(B); S=np.array(Smat(n))
    Bm=np.array(B).T%q
    rows=None
    for R in itertools.combinations(range(n),d):
        if det_modp([[int(Bm[r][j]) for j in range(d)] for r in R],q)!=0: rows=R;break
    sub=[[int(Bm[r][j]) for j in range(d)] for r in rows]
    subinv=sp.Matrix(sub).inv_mod(q).tolist()
    cols=[]
    for v in B:
        w=(S@np.array(v))%q
        cols.append([sum(subinv[i][k]*int(w[rows[k]]) for k in range(d))%q for i in range(d)])
    Sr=[[cols[j][i] for j in range(d)] for i in range(d)]
    dt=det_modp(Sr,q)
    return (1 if dt==1 else -1), d, B

print("T7.3<1>2  D = det(A|R_n):  D^2 = det(C|R_n),  D^q = det(S|R_n) D")
for (q,a,n) in [(3,[1,1],2),(3,[1,1],6),(3,[2,1],3),(3,[0,1,1],6),(3,[0,1,1],9),
                (5,[1,1],2),(5,[1,1],5),(5,[0,1,1],4),(7,[1,1],2),(3,[2,1],1),(3,[2,1],4)]:
    F=FF(q,n)
    th=next(c for c in F.elems() if det_modp([[F.frob(c,i)[k] for k in range(n)] for i in range(n)],q)!=0)
    A=[[F.frob(th,(r+i)%n) for i in range(n)] for r in range(n)]
    cc=[F.trace(F.mul(th,F.frob(th,m))) for m in range(n)]
    C=[[cc[(k-i)%n] for k in range(n)] for i in range(n)]
    dS,d,B = detS_R(a,n,q)
    if d==0:
        chk(f"  q={q} a={a} n={n}: R_n = 0, delta_n = 1 by convention", dS==1); continue
    Bm=np.array(B).T%q
    rows=next(R for R in itertools.combinations(range(n),d)
              if det_modp([[int(Bm[r][j]) for j in range(d)] for r in R],q)!=0)
    sub=[[int(Bm[r][j]) for j in range(d)] for r in rows]
    subinvq=sp.Matrix(sub).inv_mod(q).tolist()
    def restrict(Mrows):   # Mrows: n x n over F_{q^n}; returns the d x d matrix on R_n
        out=[[None]*d for _ in range(d)]
        for j,v in enumerate(B):
            w=[]
            for r_ in range(n):
                s_=F.zero
                for i in range(n): s_=F.add(s_,F.sc(v[i],Mrows[r_][i]))
                w.append(s_)
            co=[]
            for i in range(d):
                s_=F.zero
                for k in range(d): s_=F.add(s_,F.sc(int(subinvq[i][k]),w[rows[k]]))
                co.append(s_)
            # verify invariance
            for r_ in range(n):
                s_=F.zero
                for i in range(d): s_=F.add(s_,F.sc(int(Bm[r_][i]),co[i]))
                assert s_==w[r_], "not invariant"
            for i in range(d): out[i][j]=co[i]
        return out
    def detFF(M):
        M=[r[:] for r in M]; k=len(M); det=F.one
        for c in range(k):
            pr=next((i for i in range(c,k) if any(M[i][c])), None)
            if pr is None: return F.zero
            if pr!=c: M[c],M[pr]=M[pr],M[c]; det=F.neg(det)
            det=F.mul(det,M[c][c]); iv=F.inv(M[c][c]); M[c]=[F.mul(iv,x) for x in M[c]]
            for i in range(c+1,k):
                if any(M[i][c]):
                    f_=M[i][c]; M[i]=[F.add(x,F.neg(F.mul(f_,y))) for x,y in zip(M[i],M[c])]
        return det
    D=detFF(restrict(A))
    Cff=[[tuple([C[i][k]%q]+[0]*(n-1)) for k in range(n)] for i in range(n)]
    detC=detFF(restrict(Cff))
    ok1 = F.mul(D,D)==detC
    ok2 = F.frob(D)==F.sc(dS%q, D)
    chk(f"  q={q} a={a} n={n} (q|n: {n%q==0}, dim R_n={d}): D^2=det(C|R_n) and D^q=det(S|R_n) D",
        ok1 and ok2, f"delta_n = det(S|R_n) = {dS:+d}")

print("\nT7.5  the two worked counterexamples and the table, recomputed")
def S_n(q,n,a):
    F=FF(q,n); tot=0j
    for x in F.elems():
        g=F.zero
        for j,aj in enumerate(a):
            if aj: g=F.add(g,F.sc(aj,F.mul(x,F.frob(x,j))))
        tot+=np.exp(2j*np.pi*F.trace(g)/q)
    return tot
def transfer(q,a):
    J=len(a)-1
    if J==0: return np.array([[sum(np.exp(2j*np.pi*(a[0]*x*x%q)/q) for x in range(q))]])
    st=[tuple(c) for c in itertools.product(range(q),repeat=J)]; idx={s:i for i,s in enumerate(st)}
    E=np.zeros((q**J,q**J),complex)
    for s in st:
        for x in range(q):
            ph=(a[0]*x*x+sum(a[j]*s[J-j]*x for j in range(1,J+1)))%q
            E[idx[s[1:]+(x,)],idx[s]]+=np.exp(2j*np.pi*ph/q)
    return E
TAB=[(3,[2,1],1),(3,[2,1],2),(3,[1,1],2),(3,[1,1],6),(3,[0,1,1],6),(5,[1,1],2)]
for (q,a,n) in TAB:
    s=S_n(q,n,a); t=np.trace(np.linalg.matrix_power(transfer(q,a),n))
    dS,d,_=detS_R(a,n,q)
    print(f"    q={q} a={tuple(a)} n={n}:  S_n = {s.real:+9.4f}{s.imag:+9.4f}i   t_n = {t.real:+9.4f}{t.imag:+9.4f}i   d_n = {d}   delta_n = {dS:+d}")
    chk(f"  table row q={q} a={a} n={n} obeys (7.4)", abs(s-((-1)**(n-1))*dS*t)<1e-8*max(1,abs(s)))
print("    (astra's table: 3,(2,1),1 -> 3,3,1 | 3,(2,1),2 -> 3i sqrt3, -3i sqrt3, 1 | 3,(1,1),2 -> 3i sqrt3, 3i sqrt3, 1 |")
print("     3,(1,1),6 -> 81, -81, 2 | 3,(0,1,1),6 -> -81 i sqrt3 both, 3 | 5,(1,1),2 -> 5 sqrt5 both, 1;  3 sqrt3 = %.4f, 81 sqrt3 = %.4f, 5 sqrt5 = %.4f)"%(3*np.sqrt(3),81*np.sqrt(3),5*np.sqrt(5)))
print("\n==== FAILURES:", FAIL if FAIL else "none")
