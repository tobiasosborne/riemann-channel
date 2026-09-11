"""Weil–LPS quantum expanders.

For an odd prime p and an LPS parameter q ≡ 1 (mod 4) with q a square mod p:
  1. the q+1 integer quaternions of norm q (a0 > 0 odd, a1,a2,a3 even),
  2. their images in SL2(F_p) via a splitting of the Hamilton quaternions,
  3. the Weil representation W of SL2(F_p) on C^p, built numerically from the
     Fourier, chirp and dilation unitaries and CHECKED via the intertwining
     relation Ad(W(g)) T(v) ∝ T(g v) for every generator,
  4. the channel Phi_q(rho) = (1/(q+1)) sum_s W(s) rho W(s)^†,
  5. spectra of the Cayley graph of SL2(F_p) and of Phi_q, Ramanujan checks,
     Harrow containment, Hecke relations, commutation across q, joint spectra,
     and the quantum Ihara zeta.
Usage: python3 scripts/weil_lps.py p q [q2]
"""
import sys, itertools, collections, numpy as np
import scipy.sparse as sp, scipy.sparse.linalg as spl

# ---------- quaternions of norm n with the LPS sign normalisation ----------
def lps_quaternions(n):
    out=[]; r=int(np.sqrt(n))+1
    for a0 in range(1,r+1,2):
        for a1 in range(-2*((r+1)//2),r+1,2):
            for a2 in range(-2*((r+1)//2),r+1,2):
                for a3 in range(-2*((r+1)//2),r+1,2):
                    if a0*a0+a1*a1+a2*a2+a3*a3==n: out.append((a0,a1,a2,a3))
    return out

def conj(a): return (a[0],-a[1],-a[2],-a[3])

# ---------- splitting H -> M2(F_p) ----------
def split_matrices(p):
    for x in range(p):
        for y in range(p):
            if (x*x+y*y+1)%p==0:
                I=np.array([[x,y],[y,-x]])%p; J=np.array([[0,1],[-1,0]])%p
                return I,J
def quat_to_gl2(a,p,I,J):
    a0,a1,a2,a3=a; K=(I@J)%p
    return (a0*np.eye(2,dtype=int)+a1*I+a2*J+a3*K)%p
def sqrt_mod(n,p):
    for s in range(1,p):
        if (s*s-n)%p==0: return s
    raise ValueError('not a square')
def inv_mod(a,p): return pow(int(a),p-2,p)
def det2(g,p): return int(g[0,0]*g[1,1]-g[0,1]*g[1,0])%p
def mat_mod(g,p): return np.array(g,dtype=int)%p
def key(g): return tuple(int(v) for v in np.array(g).flatten())

# ---------- Heisenberg operators on C^p ----------
def heis(p):
    psi=np.exp(2j*np.pi*np.arange(p)/p)
    X=np.roll(np.eye(p),1,axis=0)          # (Xf)(x)=f(x-1)
    Z=np.diag(psi)
    return X,Z
def T_op(u,v,X,Z): return np.linalg.matrix_power(X,u%X.shape[0])@np.linalg.matrix_power(Z,v%X.shape[0])

def read_symplectic(U,p,X,Z,tol=1e-8):
    """Find g in SL2(F_p) with U T(e_i) U^† ∝ T(g e_i); columns of g are images of (1,0),(0,1)."""
    cols=[]
    for B in (X,Z):
        A=U@B@U.conj().T; found=None
        for u in range(p):
            for v in range(p):
                C=T_op(u,v,X,Z); ph=np.trace(C.conj().T@A)/p
                if abs(ph)>1-tol and np.linalg.norm(A-ph*C)<tol*p: found=(u,v); break
            if found: break
        if found is None: raise RuntimeError('not a Weyl-covariant unitary')
        cols.append(found)
    g=np.array([[cols[0][0],cols[1][0]],[cols[0][1],cols[1][1]]])%p
    assert det2(g,p)==1, g
    return g

def weil_generators(p):
    X,Z=heis(p); psi=lambda t: np.exp(2j*np.pi*(t%p)/p)
    x=np.arange(p)
    F=np.array([[psi(a*b) for b in x] for a in x])/np.sqrt(p)
    inv2=inv_mod(2,p)
    M=np.diag([psi(inv2*t*t) for t in x])                 # chirp
    # dilation by a generator a of F_p^*: (D f)(x)=f(a^{-1} x)
    a=next(g for g in range(2,p) if len({pow(g,k,p) for k in range(1,p)})==p-1)
    D=np.zeros((p,p),complex)
    ainv=inv_mod(a,p)
    for t in x: D[t,(ainv*t)%p]=1
    gens={'F':F,'M':M,'D':D}
    symp={k:read_symplectic(U,p,X,Z) for k,U in gens.items()}
    return gens,symp,X,Z

def weil_rep_table(p):
    """BFS over SL2(F_p) in the generators; returns dict g -> unitary W(g) (projective)."""
    gens,symp,X,Z=weil_generators(p)
    start=np.eye(2,dtype=int); table={key(start):np.eye(p,dtype=complex)}
    frontier=[start]
    while frontier:
        new=[]
        for g in frontier:
            Wg=table[key(g)]
            for k,s in symp.items():
                h=mat_mod(s@g,p)          # apply generator after g: symplectic of U_k W(g) is s·g
                if key(h) not in table:
                    table[key(h)]=gens[k]@Wg; new.append(h)
        frontier=new
    assert len(table)==p*(p*p-1), (len(table),p*(p*p-1))
    return table,X,Z

def check_intertwiner(W,g,p,X,Z):
    """max over basis v of || Ad(W) T(v) - phase T(g v) ||"""
    err=0.0
    for (u,v) in ((1,0),(0,1),(1,1)):
        gv=(g@np.array([u,v]))%p
        A=W@T_op(u,v,X,Z)@W.conj().T; C=T_op(int(gv[0]),int(gv[1]),X,Z)
        ph=np.trace(C.conj().T@A)/p; err=max(err,np.linalg.norm(A-ph*C),abs(abs(ph)-1))
    return err

# ---------- SL2(F_p) enumeration and Cayley graph ----------
def psl2_canon(g,p):
    """representative of {g,-g}: first nonzero entry in 1..(p-1)/2"""
    k=key(g); 
    for v in k:
        if v!=0:
            return k if v<=(p-1)//2 else key(mat_mod(-np.array(g),p))
def sl2_elements(p):
    els=[]
    for a,b,c,d in itertools.product(range(p),repeat=4):
        if (a*d-b*c)%p==1: els.append((a,b,c,d))
    return els
def psl2_elements(p):
    return sorted({psl2_canon(np.array(e).reshape(2,2),p) for e in sl2_elements(p)})
def cayley_adjacency(p,S):
    """Cayley graph of PSL2(F_p) with generating set S (matrices in SL2)"""
    els=psl2_elements(p); idx={e:i for i,e in enumerate(els)}; n=len(els)
    rows=[];cols=[]
    for i,e in enumerate(els):
        g=np.array(e).reshape(2,2)
        for s in S:
            h=psl2_canon(mat_mod(g@s,p),p); rows.append(i); cols.append(idx[h])
    A=sp.csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(n,n))
    return A

def parity_blocks(p):
    """orthonormal bases of even and odd functions on F_p"""
    h=(p-1)//2; Be=np.zeros((p,h+1)); Bo=np.zeros((p,h))
    Be[0,0]=1
    for k in range(1,h+1):
        Be[k,k]=Be[p-k,k]=1/np.sqrt(2); Bo[k,k-1]=1/np.sqrt(2); Bo[p-k,k-1]=-1/np.sqrt(2)
    return Be,Bo

def superop(Ws):
    p=Ws[0].shape[0]; E=np.zeros((p*p,p*p),complex)
    for W in Ws: E+=np.kron(W.conj(),W)
    return E/len(Ws)

# ---------- main ----------
def build(p,q,table,X,Z,I,J):
    Q=lps_quaternions(q); assert len(Q)==q+1, (q,len(Q))
    s=sqrt_mod(q,p); sinv=inv_mod(s,p)
    S=[mat_mod(sinv*quat_to_gl2(a,p,I,J),p) for a in Q]
    for a,g in zip(Q,S):
        assert det2(g,p)==1
        ginv=mat_mod(sinv*quat_to_gl2(conj(a),p,I,J),p)
        assert key(mat_mod(g@ginv,p))==key(np.eye(2,dtype=int))
    keys=[key(g) for g in S]; assert len(set(keys))==q+1, 'generators not distinct'
    Ws=[table[k] for k in keys]
    err=max(check_intertwiner(W,g,p,X,Z) for W,g in zip(Ws,S))
    return Q,S,Ws,err

def report(p,q,table,X,Z,I,J,dense_limit=5000):
    Q,S,Ws,err=build(p,q,table,X,Z,I,J)
    print(f'\n===== p={p}, q={q}:  |S|={len(S)} generators in SL2(F_{p}); Weil intertwiner error {err:.1e}')
    bound=2*np.sqrt(q)
    # Cayley graph of SL2(F_p)
    A=cayley_adjacency(p,S); n=A.shape[0]
    if n<=dense_limit:
        ev=np.linalg.eigvalsh(A.toarray()); ev=np.sort(ev)
        lam2=ev[-2]; lammin=ev[0]; spec=ev
    else:
        hi=spl.eigsh(A,k=4,which='LA',return_eigenvectors=False); lo=spl.eigsh(A,k=3,which='SA',return_eigenvectors=False)
        hi=np.sort(hi); lam2=hi[-2]; lammin=np.min(lo); spec=None
    print(f'Cayley graph on PSL2(F_{p}): n={n}, lambda_1={ (spec[-1] if spec is not None else hi[-1]):.6f} (q+1={q+1}), lambda_2={lam2:.6f}, lambda_min={lammin:.6f}, bound 2sqrt(q)={bound:.6f}  -> Ramanujan: {lam2<=bound+1e-9 and lammin>=-bound-1e-9}')
    # channels on the two irreducible Weil blocks (even: dim (p+1)/2, odd: dim (p-1)/2)
    Be,Bo=parity_blocks(p); out={}
    for name,B in (('even',Be),('odd',Bo)):
        Wb=[B.T@W@B for W in Ws]
        uerr=max(np.linalg.norm(Wq@Wq.conj().T-np.eye(B.shape[1])) for Wq in Wb)
        E=superop(Wb); herm=np.linalg.norm(E-E.conj().T)
        w,V=np.linalg.eigh((E+E.conj().T)/2); w=np.sort(w)[::-1]
        top=w[0]; second=w[1]*(q+1); lowest=w[-1]*(q+1)
        ram=second<=bound+1e-9 and lowest>=-bound-1e-9
        print(f'Channel Phi_q^{name} on M_{B.shape[1]}: block unitarity dev {uerr:.1e}, HS-hermitian dev {herm:.1e}; top {top:.6f} (mult {np.sum(abs(w-1)<1e-9)}); (q+1)*lambda_2={second:.6f}, (q+1)*lambda_min={lowest:.6f}, bound {bound:.6f}  -> Ramanujan quantum expander: {ram}')
        vals=np.round(w*(q+1),6); cnt=collections.Counter(vals)
        print(f'   spectrum (adjacency units) x multiplicity: {sorted(cnt.items(),key=lambda t:-t[0])}')
        if spec is not None:
            d=max(min(abs(spec-v)) for v in vals)
            print(f'   Harrow containment in the PSL2 Cayley spectrum: max distance = {d:.1e}')
        mods=set()
        for lam in cnt:
            if abs(lam-(q+1))<1e-6: continue
            r=np.roots([1,-lam,q]); mods.update(np.round(abs(r),6))
        print(f'   quantum Ihara zeta: nontrivial |mu| values = {sorted(mods)}  (RH <=> all equal sqrt(q)={np.sqrt(q):.6f})')
        out[name]=(E,w,Wb)
    return Q,S,Ws,out

if __name__=='__main__':
    p=int(sys.argv[1]); qs=[int(a) for a in sys.argv[2:]]
    I,J=split_matrices(p); K=(I@J)%p
    assert key(mat_mod(I@I,p))==key(mat_mod(-np.eye(2,dtype=int),p)) and key(mat_mod(I@J+J@I,p))==key(np.zeros((2,2),int))
    table,X,Z=weil_rep_table(p)
    print(f'Weil representation table for SL2(F_{p}) built: {len(table)} elements')
    results={}
    for q in qs: results[q]=report(p,q,table,X,Z,I,J)
    # Hecke relations and commutation
    for q in qs:
        Q,S,Ws,out=results[q]
        Sq2=[mat_mod(inv_mod(q,p)*quat_to_gl2(a,p,I,J),p) for a in lps_quaternions(q*q)]   # norm q^2, scaled by q^{-1}
        A=cayley_adjacency(p,S); A2=cayley_adjacency(p,Sq2)
        print(f'Hecke relation A_q^2 - q I = A_(q^2):  |A_q^2 - qI - A_(q^2)| = {abs(A@A-q*sp.eye(A.shape[0])-A2).max():.1e}   (|norm-q^2 set| = {len(Sq2)}, expect q^2+q+1 = {q*q+q+1})')
    if len(qs)==2:
        q1,q2=qs
        for blk in ('even','odd'):
            E1,E2=results[q1][3][blk][0],results[q2][3][blk][0]
            print(f'\nCommutation [Phi_{q1}^{blk}, Phi_{q2}^{blk}]: ||E1E2 - E2E1|| = {np.linalg.norm(E1@E2-E2@E1):.1e}')
        E1,E2=results[q1][3]['even'][0],results[q2][3]['even'][0]
        s12=sqrt_mod(q1*q2,p); S12=[mat_mod(inv_mod(s12,p)*quat_to_gl2(a,p,I,J),p) for a in lps_quaternions(q1*q2)]
        A1=cayley_adjacency(p,results[q1][1]); A2=cayley_adjacency(p,results[q2][1]); A12=cayley_adjacency(p,S12)
        print(f'Hecke multiplicativity A_q1 A_q2 = A_(q1 q2): residual {abs(A1@A2-A12).max():.1e}  (|norm q1q2 set|={len(S12)}, expect {(q1+1)*(q2+1)})')
        # joint spectrum via a generic combination
        H=(E1+E1.conj().T)/2+np.pi*(E2+E2.conj().T)/2
        w,V=np.linalg.eigh(H)
        a1=np.real(np.einsum('ij,jk,ki->i',V.conj().T,E1,V))*(q1+1); a2=np.real(np.einsum('ij,jk,ki->i',V.conj().T,E2,V))*(q2+1)
        pairs=collections.Counter(zip(np.round(a1,5),np.round(a2,5)))
        print(f'Joint spectrum on the even block (a_{q1}, a_{q2}) with multiplicities, adjacency units (bounds 2sqrt: {2*np.sqrt(q1):.4f}, {2*np.sqrt(q2):.4f}):')
        for (x,y),m in sorted(pairs.items(),key=lambda t:-t[0][0]): print(f'   ({x:+.5f}, {y:+.5f})  x{m}')
