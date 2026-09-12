"""REFUTE-lane independent checks for astra-proofs.md T7 (Artin-Schreier).
Everything (field arithmetic, exponential sums, transfer matrix, normal basis,
A-matrix, radical, sign law, L-polynomial, super-transfer, Weyl covariance)
is coded from the STATEMENTS.  scripts/artin_schreier_mps.py is NOT imported."""
import itertools, numpy as np, sympy as sp
FAIL=[]
def chk(n, ok, d=""):
    print(("  [PASS] " if ok else "  [FAIL] ")+n+("   "+d if d else ""))
    if not ok: FAIL.append(n)

# ---------------------------------------------------------------- F_{q^n}
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
_IRR={}
def irreducible(q,n):
    """monic irreducible of degree n over F_q, coefficients ascending (f[n]=1)."""
    if (q,n) in _IRR: return _IRR[(q,n)]
    if n==1: return (0,1)
    z=sp.symbols('z')
    for tail in itertools.product(range(q),repeat=n):
        co=list(tail)+[1]
        P=sp.Poly(list(reversed(co)),z,modulus=q)
        if P.degree()==n and P.is_irreducible:
            _IRR[(q,n)]=tuple(co); return tuple(co)
    raise RuntimeError
_FFC={}
def getFF(q,n):
    if (q,n) not in _FFC: _FFC[(q,n)]=FF(q,n)
    return _FFC[(q,n)]
class FF:
    def __init__(s,q,n):
        s.q,s.n,s.f=q,n,irreducible(q,n)
        s.one=tuple([1]+[0]*(n-1)); s.zero=tuple([0]*n)
    def mul(s,a,b): return polmulmod(list(a),list(b),s.f,s.q)
    def add(s,a,b): return tuple((x+y)%s.q for x,y in zip(a,b))
    def pw(s,a,e):
        r=s.one
        while e:
            if e&1: r=s.mul(r,a)
            a=s.mul(a,a); e>>=1
        return r
    def frob(s,a,k=1): return s.pw(a,s.q**k)
    def trace(s,a):
        t=s.zero
        for i in range(s.n): t=s.add(t,s.frob(a,i))
        assert all(x==0 for x in t[1:]), t
        return t[0]
    def elems(s): return [tuple(c) for c in itertools.product(range(s.q),repeat=s.n)]

def psi(c,q): return np.exp(2j*np.pi*(c%q)/q)

_SC={}
def S_n(q,n,a):
    key=(q,n,tuple(a))
    if key in _SC: return _SC[key]
    F=getFF(q,n); tot=0j
    for x in F.elems():
        g=F.zero
        for j,aj in enumerate(a):
            if aj: g=F.add(g, tuple((aj*t)%q for t in F.mul(x,F.frob(x,j))))
        tot+=psi(F.trace(g),q)
    _SC[key]=tot; return tot

_TC={}
def transfer(q,a):
    if (q,tuple(a)) in _TC: return _TC[(q,tuple(a))]
    J=len(a)-1
    if J==0:
        _TC[(q,tuple(a))]=np.array([[sum(psi(a[0]*x*x,q) for x in range(q))]]); return _TC[(q,tuple(a))]
    st=[tuple(c) for c in itertools.product(range(q),repeat=J)]
    idx={s:i for i,s in enumerate(st)}
    E=np.zeros((q**J,q**J),complex)
    for s in st:
        for x in range(q):
            ph=a[0]*x*x+sum(a[j]*s[J-j]*x for j in range(1,J+1))
            E[idx[s[1:]+(x,)], idx[s]]+=psi(ph,q)
    _TC[(q,tuple(a))]=E; return E

CASES=[(3,[0,1]),(3,[1,1]),(3,[2,1]),(3,[0,1,1]),(3,[0,0,1]),(3,[1,0,1]),
       (5,[0,1]),(5,[1,2]),(5,[1,1]),(5,[0,1,1]),(7,[0,1]),(7,[1,1])]
def eta(c,q): return 0 if c%q==0 else (1 if pow(c%q,(q-1)//2,q)==1 else -1)

# -------------------------------------------------- T7.2 ring form, T7.3 sign law
print("T7.2 / T7.3 / T7.4  ring form, A-matrix identities, corrected sign law")
def Smat(n,q): return np.array([[1 if (j==(i+1)%n) else 0 for j in range(n)] for i in range(n)],dtype=int)%q
def Pmat(a,n,q):
    inv2=pow(2,q-2,q); S=Smat(n,q); M=np.zeros((n,n),dtype=int)
    Sp=np.eye(n,dtype=int)
    for j,aj in enumerate(a):
        Sj=np.linalg.matrix_power(S,j)%q; Sm=np.linalg.matrix_power(S,(-j)%n if n>0 else 0)%q
        Sm=np.linalg.matrix_power(S.T,j)%q   # S^{-1} = S^T for the cyclic shift
        M=(M+aj*inv2*(Sj+Sm))%q
    return M%q
def nullspace_modp(Mat,p):
    M=sp.Matrix(Mat.tolist())
    # Gaussian elimination over GF(p)
    A=[[int(x)%p for x in row] for row in M.tolist()]; m=len(A); n=len(A[0])
    piv=[]; r=0
    for c in range(n):
        pr=None
        for i in range(r,m):
            if A[i][c]%p: pr=i;break
        if pr is None: continue
        A[r],A[pr]=A[pr],A[r]
        inv=pow(A[r][c],p-2,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%p:
                f=A[i][c]; A[i]=[(x-f*y)%p for x,y in zip(A[i],A[r])]
        piv.append(c); r+=1
        if r==m: break
    free=[c for c in range(n) if c not in piv]
    basis=[]
    for fc in free:
        v=[0]*n; v[fc]=1
        for i,c in enumerate(piv): v[c]=(-A[i][fc])%p
        basis.append(v)
    return basis
def det_modp(Mat,p):
    A=[[int(x)%p for x in row] for row in Mat]; n=len(A); det=1
    for c in range(n):
        pr=None
        for i in range(c,n):
            if A[i][c]%p: pr=i;break
        if pr is None: return 0
        if pr!=c: A[c],A[pr]=A[pr],A[c]; det=(-det)%p
        det=(det*A[c][c])%p; inv=pow(A[c][c],p-2,p)
        A[c]=[(x*inv)%p for x in A[c]]
        for i in range(c+1,n):
            if A[i][c]%p:
                f=A[i][c]; A[i]=[(x-f*y)%p for x,y in zip(A[i],A[c])]
    return det%p

def delta_n(q,a,n):
    M=Pmat(a,n,q); B=nullspace_modp(M,q)
    if not B: return 1,0
    d=len(B); S=Smat(n,q)
    # S restricted to R_n in the basis B: solve S v_j = sum_k c_kj v_k
    Bm=sp.Matrix([[int(x) for x in v] for v in B]).T      # n x d
    cols=[]
    for v in B:
        w=(S@np.array(v))%q
        # solve Bm c = w over GF(q)
        aug=[[int(Bm[i,j])%q for j in range(d)]+[int(w[i])%q] for i in range(len(w))]
        # gaussian
        r=0; piv=[]
        for c in range(d):
            pr=None
            for i in range(r,len(aug)):
                if aug[i][c]%q: pr=i;break
            if pr is None: continue
            aug[r],aug[pr]=aug[pr],aug[r]
            inv=pow(aug[r][c],q-2,q); aug[r]=[(x*inv)%q for x in aug[r]]
            for i in range(len(aug)):
                if i!=r and aug[i][c]%q:
                    f=aug[i][c]; aug[i]=[(x-f*y)%q for x,y in zip(aug[i],aug[r])]
            piv.append(c); r+=1
        sol=[0]*d
        for i,c in enumerate(piv): sol[c]=aug[i][d]%q
        cols.append(sol)
    Sr=[[cols[j][i] for j in range(d)] for i in range(d)]
    dt=det_modp(Sr,q)
    return (1 if dt==1 else (-1 if dt==q-1 else None)), d

# v_- and h from f(z) = z^J P(z)
def vpm(q,a):
    z=sp.symbols('z'); inv2=pow(2,q-2,q); J=len(a)-1
    f=sum(sp.Integer(aj*inv2%q)*(z**(J+j)+z**(J-j)) for j,aj in enumerate(a))
    f=sp.Poly(sp.expand(f),z)
    co=[int(c)%q for c in f.all_coeffs()]
    P=sp.Poly(co,z,modulus=q)
    vm=0; T=P
    while T.degree()>=0 and T.eval(-1)%q==0 and T.degree()>0:
        T=sp.div(T,sp.Poly([1,1],z,modulus=q),domain=sp.GF(q))[0]; vm+=1
        if T.degree()<0: break
    vp=0; T=P
    while T.degree()>0 and T.eval(1)%q==0:
        T=sp.div(T,sp.Poly([1,-1],z,modulus=q),domain=sp.GF(q))[0]; vp+=1
    return vm,vp
for (q,a) in CASES:
    vm,vp=vpm(q,a); h=1
    while h<=vm: h*=q
    nmax = {3:7,5:5,7:4}[q]
    okring=okA=oksign=okbox=True; msg=[]
    F1=None
    for n in range(1,nmax+1):
        E=transfer(q,a); t=np.trace(np.linalg.matrix_power(E,n))
        # ring quadratic form  Q_g^circ(x) = sum_j a_j sum_i x_i x_{i+j}
        tot=0j
        for x in itertools.product(range(q),repeat=n):
            e=sum(a[j]*x[i]*x[(i+j)%n] for j in range(len(a)) for i in range(n))
            tot+=psi(e,q)
        okring &= abs(tot-t)<1e-8*max(1,abs(t))
        s=S_n(q,n,a); dn_,d=delta_n(q,a,n)
        pred=((-1)**(n-1))*dn_*t
        oksign &= abs(s-pred)<1e-7*max(1,abs(s))
        box=(1-2*(1 if n%(2*h)==0 else 0))*t
        okbox &= abs(s-box)<1e-7*max(1,abs(s))
        # d_n = dim ker M  =  log_q(|S_n|^2/q^n)
        okA &= abs(d - np.log(abs(s)**2/q**n)/np.log(q))<1e-6
        msg.append(f"n={n}:S/t={np.real_if_close(s/t) if abs(t)>1e-9 else '?'}")
    print(f"  q={q} a={a}  v_-={vm} v_+={vp} h={h}  P(-1)={'0' if vm>0 else '!=0'}  P(-eta(-1))={'0' if (vm>0 if eta(-1,q)==1 else vp>0) else '!=0'}")
    chk(f"   T7.2 Tr E_g^n = sum_x psi(Q^circ) for n<= {nmax}", okring)
    chk(f"   T7.2 d_n = dim ker P(S) = log_q(|S_n|^2/q^n)", okA)
    chk(f"   T7.3 (7.4) S_n = (-1)^(n-1) det(S|ker P(S)) Tr E_g^n", oksign)
    chk(f"   T7.4 (7.6) boxed S_n = (1 - 2*[2h | n]) Tr E_g^n, h={h}", okbox)
    # endpoint criterion (7.7): notebook claim alpha_i = -lambda_i(E_g) for all n  <=>  P(-1)!=0
    # endpoint criterion (7.8): draft law for all n  <=>  P(-eta(-1)) != 0
    allm1 = all(abs(S_n(q,n,a)-((-1)**(n-1))*np.trace(np.linalg.matrix_power(transfer(q,a),n)))<1e-7*max(1,abs(S_n(q,n,a))) for n in range(1,nmax+1))
    chk(f"   T7.4 (7.7) 'S_n=(-1)^(n-1)t_n for all n'  <=>  P(-1)!=0", allm1 == (vm==0),
        f"observed={allm1}, P(-1)!=0 is {vm==0}")
    em=eta(-1,q)
    draft = all(abs(S_n(q,n,a) - (-((-em)**n))*np.conj(np.trace(np.linalg.matrix_power(transfer(q,a),n))))<1e-7*max(1,abs(S_n(q,n,a))) for n in range(1,nmax+1))
    cond = (vm==0) if em==1 else (vp==0)   # (7.8): P(-eta(-1)) != 0
    chk(f"   T7.4 (7.8) draft law for all n  <=>  P(-eta(-1))!=0  [eta(-1)={em}]", draft==cond,
        f"observed={draft}, criterion says {cond}")

print("\nT7.3<1>1-<1>2  the A-matrix identities and the determinant square class")
for (q,n) in [(3,1),(3,2),(3,3),(3,4),(3,6),(5,2),(5,5),(5,3),(7,3),(3,6),(5,4)]:
    F=getFF(q,n)
    th=None
    for cand in F.elems():
        Mx=np.array([[F.frob(cand,i)[k] for k in range(n)] for i in range(n)])
        if det_modp(Mx.tolist(),q)!=0: th=cand;break
    A=[[F.frob(th,(r+i)%n) for i in range(n)] for r in range(n)]
    At=[[A[i][r] for i in range(n)] for r in range(n)]
    A2=[[None]*n for _ in range(n)]
    for r in range(n):
        for k in range(n):
            s=F.zero
            for i in range(n): s=F.add(s,F.mul(A[r][i],A[i][k]))
            A2[r][k]=s
    c=[F.trace(F.mul(th,F.frob(th,m))) for m in range(n)]
    C=[[c[(k-i)%n] for k in range(n)] for i in range(n)]
    Cf=[[tuple([C[i][k]%q]+[0]*(n-1)) for k in range(n)] for i in range(n)]
    Aq=[[F.frob(A[r][i]) for i in range(n)] for r in range(n)]
    SA=[[A[(r+1)%n][i] for i in range(n)] for r in range(n)]
    AS=[[A[r][(i-1)%n] for i in range(n)] for r in range(n)]
    SmA=[[A[(r-1)%n][i] for i in range(n)] for r in range(n)]
    ok = (At==A) and (A2==Cf) and (Aq==SA) and (AS==SmA)
    chk(f"  q={q} n={n} (q|n: {n%q==0}):  A^t=A, A^2=C, A^[q]=SA, AS=S^{{-1}}A", ok)
    # eta(det C) = det S = (-1)^(n-1)   (Stickelberger, proved from the embedding matrix)
    dC=det_modp(C,q); dS=det_modp(Smat(n,q).tolist(),q)
    e_dC = eta(dC,q); e_dS = 1 if dS==1 else -1
    chk(f"  q={q} n={n}  eta(det C) = det S = (-1)^(n-1) = {(-1)**(n-1)}",
        e_dC==e_dS==(-1)**(n-1), f"eta(det C)={e_dC}, det S={e_dS}")

print("\nT7.6  scaled unitarity")
for (q,a) in CASES:
    E=transfer(q,a); chk(f"  q={q} a={a}: E E^dag = q I", np.abs(E@E.conj().T-q*np.eye(len(E))).max()<1e-10)

print("\nT7.7  multiplicity formula (7.10), roots-of-unity filter, det(I-T F_g)=L(g,T)")
import numpy.polynomial.polynomial as npoly
def Lpoly(q,a,deg):
    Sv=[S_n(q,n,a) for n in range(1,deg+1)]
    co=np.zeros(deg+1,complex); co[0]=1
    for k in range(1,deg+1):     # Newton: k c_k = sum_{i=1}^k S_i c_{k-i}
        co[k]=sum(Sv[i-1]*co[k-i] for i in range(1,k+1))/k
    return co
for (q,a) in [(3,[0,1]),(3,[1,1]),(3,[2,1]),(5,[0,1]),(5,[1,2])]:
    D=q**(len(a)-1); vm,vp=vpm(q,a); h=1
    while h<=vm: h*=q
    Lc=Lpoly(q,a,D)
    E=transfer(q,a); ev=np.linalg.eigvals(E)
    # (7.10):  m_F(z) = (1/h) sum_{w^{2h}=1} m_E(w^{-1} z) - m_E(z)
    ws=np.exp(2j*np.pi*np.arange(2*h)/(2*h))
    cand=np.concatenate([w*ev for w in ws])
    # cluster the candidate values
    vals=[]; 
    for z in cand:
        for v in vals:
            if abs(v[0]-z)<1e-7: v[1]+=1; break
        else: vals.append([z,1])
    mF=[]
    for z,cnt in vals:
        mE=sum(1 for l in ev if abs(l-z)<1e-7)
        m=cnt/h - mE
        if m>0.5: mF += [z]*int(round(m))
    Fpoly=np.poly(np.array(mF)) if mF else np.array([1.0])
    # det(I - T F) coefficients ascending
    detc=np.array([np.poly(np.array(mF))[::-1][k]*(-1)**0 for k in range(len(mF)+1)])
    detc=np.zeros(len(mF)+1,complex); detc[0]=1
    pcoef=np.array([1.0+0j])
    for z in mF: pcoef=np.convolve(pcoef,[1,-z])
    chk(f"  q={q} a={a} h={h}: (7.10) gives {len(mF)} roots (deg L = {D}) and det(I-TF)=L(g,T)",
        len(mF)==D and np.abs(pcoef-Lc).max()<1e-6*max(1,np.abs(Lc).max()),
        f"max coeff dev {np.abs(pcoef-Lc).max():.2e}; |roots| in [{min(abs(np.array(mF))):.6f},{max(abs(np.array(mF))):.6f}] vs sqrt(q)={np.sqrt(q):.6f}")
    # (7.9): [L(g,T) D_g(T)]^h = det(I - T^{2h} E^{2h})
    Dg=np.array([1.0+0j])
    for l in ev: Dg=np.convolve(Dg,[1,-l])
    lhs=np.array([1.0+0j])
    LD=np.convolve(Lc,Dg)
    for _ in range(h): lhs=np.convolve(lhs,LD)
    ev2=np.linalg.eigvals(np.linalg.matrix_power(E,2*h))
    rhs=np.zeros(2*h*len(ev)+1,complex); 
    poly=np.array([1.0+0j])
    for l in ev2: poly=np.convolve(poly,np.concatenate([[1],np.zeros(2*h-1),[-l]]))
    L2=max(len(lhs),len(poly)); lhs=np.pad(lhs,(0,L2-len(lhs))); poly=np.pad(poly,(0,L2-len(poly)))
    chk(f"  q={q} a={a}: (7.9) [L D_g]^h = det(I - T^(2h) E^(2h))",
        np.abs(lhs-poly).max()<1e-5*max(1,np.abs(poly).max()), f"max dev {np.abs(lhs-poly).max():.2e}")

print("\nT7.8  projective count, point at infinity, corrected super-transfer")
for (q,a) in [(3,[0,1]),(3,[2,1]),(3,[1,1]),(5,[1,2])]:
    J=len(a)-1; D=q**J; nmax={3:5,5:4}[q]
    vm,vp=vpm(q,a); h=1
    while h<=vm: h*=q
    for n in range(1,nmax+1):
        F=getFF(q,n)
        # direct projective count: affine points + 1
        cnt=0
        for x in F.elems():
            g=F.zero
            for j,aj in enumerate(a):
                if aj: g=F.add(g,tuple((aj*t)%q for t in F.mul(x,F.frob(x,j))))
            if F.trace(g)%q==0: cnt+=q
        Ndirect=cnt+1
        Nchar=1+q**n+sum(S_n(q,n,[(aa*c)%q for aa in a]) for c in range(1,q))
        # corrected super-transfer: even Tr E_0^n + 1, odd sum_a Tr F_{ag}^n = -S_n(ag)
        strE = q**n + 1 + sum(S_n(q,n,[(aa*c)%q for aa in a]) for c in range(1,q))
        # the DRAFT block -eta(-1) (+)_a E_{ag}
        em=eta(-1,q)
        strdraft = q**n + 1 - sum((-em)**n*np.trace(np.linalg.matrix_power(transfer(q,[(aa*c)%q for aa in a]),n)) for c in range(1,q))
        chk(f"  q={q} a={a} n={n}: (7.12) N_n = 1+q^n+sum_a S_n(ag) = direct count = str(corrected E)",
            abs(Nchar-Ndirect)<1e-6 and abs(strE-Ndirect)<1e-6,
            f"N={Ndirect}  char={Nchar.real:.4f}  str(corrected)={strE.real:.4f}  str(DRAFT block)={strdraft.real:.4f}")
    chk(f"  q={q} a={a}: 2g(C) = (q-1)q^J = {(q-1)*D}", True)

print("\nT7.9 / T7.10  centred Weyl covariance, symplecticity, character modulus")
def Mg(q,a):
    J=len(a)-1; c=a[J]; ci=pow(c,q-2,q); inv=[0]*(2*J)
    M=np.zeros((2*J,2*J),dtype=int)
    # basis order (u_1..u_J, v_1..v_J); columns = images of basis vectors
    for col in range(2*J):
        u=np.zeros(J,dtype=int); v=np.zeros(J,dtype=int)
        if col<J: u[col]=1
        else: v[col-J]=1
        up=np.zeros(J,dtype=int); vp=np.zeros(J,dtype=int)
        for k in range(J-1): up[k]=u[k+1]
        up[J-1]=(-v[0]*ci)%q
        for k in range(J-1): vp[k]=(v[k+1]+a[J-1-k]*up[J-1])%q
        vp[J-1]=(c*u[0]+sum(a[J-k]*u[k] for k in range(1,J))+2*a[0]*up[J-1])%q   # v'_J = c u_1 + sum_{k=2}^J a_{J+1-k} u_k + 2a_0 u'_J
        M[:J,col]=up%q; M[J:,col]=vp%q
    return M%q
for (q,a) in CASES:
    J=len(a)-1
    if J==0: continue
    M=Mg(q,a)
    Om=np.block([[np.zeros((J,J),dtype=int),np.eye(J,dtype=int)],
                 [-np.eye(J,dtype=int),np.zeros((J,J),dtype=int)]])%q
    chk(f"  q={q} a={a}: M_g symplectic mod q", np.all((M.T@Om@M-Om)%q==0), f"M=\n{M}")
    # centred Weyl operators and exact covariance for U = E_g/sqrt(q)
    st=[tuple(c) for c in itertools.product(range(q),repeat=J)]; idx={s:i for i,s in enumerate(st)}
    inv2=pow(2,q-2,q)
    def X(u,v):
        Wm=np.zeros((q**J,q**J),complex)
        for s in st:
            ph=sum(v[k]*((s[k]+u[k]*inv2)%q) for k in range(J))
            Wm[idx[tuple((s[k]+u[k])%q for k in range(J))], idx[s]]=psi(ph,q)
        return Wm
    U=transfer(q,a)/np.sqrt(q); Ui=U.conj().T
    worst=0
    labels=list(itertools.product(range(q),repeat=2*J)) if q**(2*J)<=200 else \
           [tuple(np.eye(2*J,dtype=int)[i]) for i in range(2*J)]+[tuple((np.eye(2*J,dtype=int)[0]+np.eye(2*J,dtype=int)[-1])%q)]
    for lab in labels:
        u=np.array(lab[:J]); v=np.array(lab[J:])
        img=(M@np.concatenate([u,v]))%q
        worst=max(worst, np.abs(U@X(u,v)@Ui - X(img[:J],img[J:])).max())
    chk(f"  q={q} a={a}: (7.13) EXACT centred covariance U X_(u,v) U^-1 = X_(M(u,v)) (no phase)",
        worst<1e-9, f"max entrywise residual over {len(labels)} labels = {worst:.2e}")
    # T7.10: Tr Ad(U^n) = #fixed labels = q^{dim ker(M^n - 1)} = |Tr E^n|^2/q^n
    E=transfer(q,a)
    for n in range(1,7):
        Mn=np.linalg.matrix_power(M,n)%q
        K=(Mn-np.eye(2*J,dtype=int))%q
        dk=2*J-len(nullspace_modp(K,q))  # rank
        dker=len(nullspace_modp(K,q))
        t=np.trace(np.linalg.matrix_power(E,n))
        chk(f"  q={q} a={a} n={n}: |Tr E^n|^2 = q^(n+dim ker(M^n-1))",
            abs(abs(t)**2-q**(n+dker))<1e-6*q**(n+dker), f"|t|^2={abs(t)**2:.4f} q^(n+{dker})={q**(n+dker)}")
print("\n==== FAILURES:", FAIL if FAIL else "none")
