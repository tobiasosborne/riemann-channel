"""REFUTE lane scratch script (claude:opus).  Written from the STATEMENTS of
notes/complex-zeta/astra-proofs.md only; nothing imported from scripts/.

EXACT checks (integer arithmetic; polynomial identities verified by exact
evaluation at deg+1 distinct integers, which is a proof for bounded degree):
  T0.1   ordered geodesic flow operator
  T2.1/T2.2  T_k = S_k R_k - F_k  and  det(I-zT_k) = det K_k . det(I-z R_k K_k^-1 S_k)
  T2.3   Bass for arbitrary graphs
  T2.4   tetrahedron boundary: T_1 = 0, det(I+uT_2) = (1-u^4)^6
  T4.1   block incidence matrix D_k(z): two Schur evaluations
  T7.2   C_3, filled triangle, octahedron rows
"""
import itertools, random
from fractions import Fraction
import sympy as sp
u = sp.Symbol('u')

# ------------------------------------------------------------ integer det
def bareiss(M):
    """exact determinant of a list-of-lists integer matrix (Bareiss)."""
    A=[row[:] for row in M]; n=len(A)
    if n==0: return 1
    sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            piv=None
            for i in range(k+1,n):
                if A[i][k]!=0: piv=i; break
            if piv is None: return 0
            A[k],A[piv]=A[piv],A[k]; sign=-sign
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*A[k][k]-A[i][k]*A[k][j])//prev
            A[i][k]=0
        prev=A[k][k]
    return sign*A[n-1][n-1]

def L(M):  return [[int(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]
def addt(A,B,t): return [[A[i][j]+t*B[i][j] for j in range(len(A))] for i in range(len(A))]

def polyvals(A,B,deg):
    """values of det(A + t B) at t = 0..deg (exact integers)."""
    return [bareiss(addt(A,B,t)) for t in range(deg+1)]

def interp(vals, var):
    pts=[(sp.Integer(i), sp.Integer(v)) for i,v in enumerate(vals)]
    return sp.expand(sp.interpolate(pts,var))

# ------------------------------------------------------------- complexes
class Cplx:
    def __init__(self, faces):
        F=set()
        for f in faces:
            f=frozenset(f)
            for r in range(1,len(f)+1):
                for s in itertools.combinations(sorted(f),r): F.add(frozenset(s))
        self.F=F; self.d=max(len(f) for f in F)-1
        self.verts=sorted({v for f in F if len(f)==1 for v in f})
        self.Om={}
        for k in range(self.d+1):
            st=[]
            for f in F:
                if len(f)==k+1: st.extend(itertools.permutations(sorted(f)))
            self.Om[k]=sorted(st)
        self.idx={k:{s:i for i,s in enumerate(self.Om[k])} for k in self.Om}
    def f(self,k): return sum(1 for x in self.F if len(x)==k+1)
    def chi(self): return sum((-1)**k*self.f(k) for k in range(self.d+1))
    def n(self,k): return len(self.Om[k]) if 0<=k<=self.d else 0

def T(X,k):
    M=sp.zeros(X.n(k),X.n(k))
    for s in X.Om[k]:
        i=X.idx[k][s]
        for w in X.verts:
            if w in s: continue
            if frozenset(s[1:]+(w,)) not in X.F: continue
            if frozenset(s+(w,)) in X.F: continue
            M[X.idx[k][s[1:]+(w,)],i]+=1
    return M
def Rm(X,k):
    M=sp.zeros(X.n(k-1),X.n(k))
    for s in X.Om[k]: M[X.idx[k-1][s[1:]],X.idx[k][s]]+=1
    return M
def Sm(X,k):
    M=sp.zeros(X.n(k),X.n(k-1))
    for s in X.Om[k-1]:
        for w in X.verts:
            if w in s or frozenset(s+(w,)) not in X.F: continue
            M[X.idx[k][s+(w,)],X.idx[k-1][s]]+=1
    return M
def Cm(X,k):
    M=sp.zeros(X.n(k),X.n(k))
    for s in X.Om[k]: M[X.idx[k][s[1:]+(s[0],)],X.idx[k][s]]+=1
    return M
def Fm(X,k):
    Fk=Cm(X,k)
    if k+1<=X.d and X.n(k+1)>0: Fk=Fk+Rm(X,k+1)*Sm(X,k+1)
    return Fk

def detIz(M,deg=None):
    """values of det(I - t M) for t=0..deg (deg defaults to dim)."""
    n=M.rows
    if n==0: return [1]
    if deg is None: deg=n
    return polyvals(L(sp.eye(n)), L(-M), deg)

# ------------------------------------------------------------- the checks
def check(X,name):
    print(f"   [{name}] f={[X.f(k) for k in range(X.d+1)]} chi={X.chi()} "
          f"dimH={[X.n(k) for k in range(X.d+1)]}")
    allok=True
    for k in range(1,X.d+1):
        if X.n(k)==0: continue
        Tk,Rk,Sk,Fk=T(X,k),Rm(X,k),Sm(X,k),Fm(X,k)
        alg=(Tk-(Sk*Rk-Fk)).is_zero_matrix
        nkm,nk,nkp=Rk.rows,Tk.rows,X.n(k+1)
        N=nkm+nk+nkp
        A=sp.zeros(N,N); B=sp.zeros(N,N)
        A[0:nkm,0:nkm]=sp.eye(nkm); A[0:nkm,nkm:nkm+nk]=-Rk
        A[nkm:nkm+nk,nkm:nkm+nk]=sp.eye(nk)
        B[nkm:nkm+nk,0:nkm]=-Sk; B[nkm:nkm+nk,nkm:nkm+nk]=Cm(X,k)
        if nkp:
            Rk1,Sk1=Rm(X,k+1),Sm(X,k+1)
            A[nkm+nk:,nkm:nkm+nk]=-Sk1; A[nkm+nk:,nkm+nk:]=sp.eye(nkp)
            B[nkm:nkm+nk,nkm+nk:]=Rk1
        deg=N
        blk=polyvals(L(A),L(B),deg); lhs=detIz(Tk,deg)
        bok = blk==lhs
        # Schur factorisation det(I-zT) = det K . det(I - z R K^-1 S), exact at sample z
        sok=True; pts=[]
        for t in [2,3,5,7,11,13]:
            Kt=sp.eye(nk)+sp.Integer(t)*Fk
            dK=bareiss(L(Kt))
            if dK==0: continue
            Mt=sp.eye(nkm)-sp.Integer(t)*Rk*Kt.inv()*Sk
            lt=bareiss(addt(L(sp.eye(nk)),L(-Tk),t))
            if sp.Rational(dK)*Mt.det()!=sp.Integer(lt): sok=False
            pts.append(t)
        print(f"      k={k} dimH_k={nk:3d}: T_k=S_kR_k-F_k {alg} | T4.1 block det "
              f"(deg<={deg}) {bok} | detK*detM at z={pts} {sok}")
        allok=allok and alg and bok and sok
    return allok

def show(X,name,claims=None):
    print(f"\n-- {name}: f={[X.f(k) for k in range(X.d+1)]} chi={X.chi()}")
    for k in range(1,X.d+1):
        s=(-1)**(k+1); n=X.n(k)
        if n==0: continue
        Tk=T(X,k)
        if n<=26:
            p=interp(polyvals(L(sp.eye(n)),L(-s*Tk),n), u)
            print(f"     det(I - s_{k} u T_{k}) = {sp.factor(p)}   [dim H_{k}={n}, T_{k}=0? {Tk.is_zero_matrix}]")
        else:
            print(f"     [dim H_{k}={n}] T_{k}=0? {Tk.is_zero_matrix}")
        if claims and k in claims:
            cl=claims[k]
            vals=polyvals(L(sp.eye(n)),L(-s*Tk),n)
            ok=all(sp.Integer(vals[t])==sp.Integer(cl.subs(u,t)) for t in range(n+1))
            print(f"        claimed {sp.factor(cl)}  -> exact match over {n+1} points: {ok}")

if __name__=="__main__":
    C3=Cplx([(0,1),(1,2),(0,2)])
    show(C3,"C_3 graph (T7.2 row 1)",{1:(1-u**3)**2}); print("  ",check(C3,"C_3"))
    D2=Cplx([(0,1,2)])
    show(D2,"filled triangle Delta^2 (T7.2 row 2)",{1:sp.Integer(1),2:sp.Integer(1)})
    n1=D2.n(1); n2=D2.n(2)
    print("     T7.2<1>1: det K_1(u) =",
          sp.factor(interp(polyvals(L(sp.eye(n1)),L(Fm(D2,1)),n1),u)),
          "; det K_2(-u) =",
          sp.factor(interp(polyvals(L(sp.eye(n2)),L(-Fm(D2,2)),n2),u)))
    print("  ",check(D2,"Delta^2"))
    bd=Cplx(list(itertools.combinations(range(4),3)))
    show(bd,"boundary of tetrahedron (T2.4 / T7.2 row 3)",
         {1:sp.Integer(1),2:(1-u**4)**6}); print("  ",check(bd,"dDelta^3"))
    pairs=[(0,1),(2,3),(4,5)]
    tri=[t for t in itertools.combinations(range(6),3) if all(not set(p)<=set(t) for p in pairs)]
    oc=Cplx(tri)
    show(oc,"octahedron = clique cplx of K_{2,2,2} (T7.2 <1>3)",
         {1:(1-u**4)**6,2:(1-u**6)**8}); print("  ",check(oc,"octahedron"))
    fd=Cplx([(0,1,2,3)]); show(fd,"filled tetrahedron Delta^3 (T7.2<1>2)")

    print("\n== T2.3 Bass for random graphs (exact)")
    random.seed(7)
    for tr in range(6):
        nv=random.randint(4,7)
        E=[e for e in itertools.combinations(range(nv),2) if random.random()<0.6]
        if len(E)<2: continue
        G=Cplx(E+[(v,) for v in range(nv)])
        A=sp.zeros(nv,nv); Dg=sp.zeros(nv,nv)
        for (a,b) in E: A[a,b]+=1; A[b,a]+=1
        for v in range(nv): Dg[v,v]=sum(A[v,:])
        n=G.n(1); vals=detIz(T(G,1),n)
        rhs=sp.expand((1-u**2)**(G.f(1)-G.f(0))*(sp.eye(nv)-u*A+u**2*(Dg-sp.eye(nv))).det())
        ok=all(sp.Integer(vals[t])==sp.Integer(rhs.subs(u,t)) for t in range(n+1))
        print(f"   nv={nv} |E|={len(E)} (f1-f0={G.f(1)-G.f(0)}): Bass exact {ok}")

    print("\n== T2.2 / T4.1 on random 2- and 3-complexes (exact)")
    random.seed(11); done=0; tr=0
    while done<7 and tr<80:
        tr+=1
        nv=random.choice([5,6,7]); dim=random.choice([2,2,3])
        cells=[c for c in itertools.combinations(range(nv),dim+1) if random.random()<0.4]
        extra=[e for e in itertools.combinations(range(nv),2) if random.random()<0.3]
        if not cells: continue
        X=Cplx(cells+extra+[(v,) for v in range(nv)])
        if sum(X.n(k) for k in range(X.d+1))>170: continue
        done+=1
        r=check(X,f"random{done} nv={nv} d={X.d}")
        print(f"      => {'ALL OK' if r else '*** FAILURE ***'}")
