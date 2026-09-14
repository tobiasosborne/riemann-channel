# Reviewer claude:opus-5. Independent rebuild of T4.3 from (4.5)-(4.6), and the C^{1|g} extension.
import numpy as np
np.set_printoptions(suppress=True, linewidth=200)

def build(q, pis, check=True):
    """T4.3 / its C^{1|g} extension, rebuilt from the displayed formulas only."""
    g = len(pis)
    t = (q+1)/2.0; w = (q+1)/(2.0*g); h = (q-1)/(2.0*np.sqrt(g))
    D = np.diag(pis); B0 = D/np.sqrt(t)
    b0 = B0.reshape(-1,1)                       # row-major vec, T4.1 convention
    nu = float((b0.conj().T@b0).real)
    if check and w < nu - 1e-12: raise ValueError(f"R not PSD: w={w} < nu={nu}")
    S = np.sqrt(w)*np.eye(g*g) + ((np.sqrt(max(w-nu,0))-np.sqrt(w))/nu)*(b0@b0.conj().T)
    R = w*np.eye(g*g) - b0@b0.conj().T
    assert np.allclose(S@S, R, atol=1e-9), "S^2 != R"
    Bs = [B0] + [ (S[:,l]).reshape(g,g) for l in range(g*g) ]
    d = 1+g; As = []
    A = np.zeros((d,d),complex); A[0,0]=np.sqrt(t); A[1:,1:]=Bs[0]; As.append(A)
    for l in range(1,g*g+1):
        A = np.zeros((d,d),complex); A[1:,1:]=Bs[l]; As.append(A)
    for j in range(g):
        A = np.zeros((d,d),complex); A[0,1+j]=np.sqrt(h); As.append(A)
        A = np.zeros((d,d),complex); A[1+j,0]=np.sqrt(h); As.append(A)
    return As, R, dict(t=t,w=w,h=h,nu=nu,neven=g*g+1,nodd=2*g)

def report(q, pis, nmax=12, label=""):
    g=len(pis); As,R,p = build(q,pis)
    E = sum(np.kron(A,A.conj()) for A in As)
    P = np.array([1.]+[-1.]*g); G = np.kron(P,P)
    ev=np.where(G==1)[0]; od=np.where(G==-1)[0]
    Ee=E[np.ix_(ev,ev)]; Eo=E[np.ix_(od,od)]
    le=np.linalg.eigvals(Ee); lo=np.linalg.eigvals(Eo)
    Dt=np.diag(list(np.conj(pis))+list(pis))
    target=[1+q**n-sum(pi**n+np.conj(pi)**n for pi in pis) for n in range(1,nmax+1)]
    st=[complex(np.sum(G*np.diag(np.linalg.matrix_power(E,n)))) for n in range(1,nmax+1)]
    err=max(abs(a-b)/abs(b) for a,b in zip(st,target))
    print(f"{label} q={q} g={g}: letters {p['neven']} even + {p['nodd']} odd; w={p['w']:.4f} nu={p['nu']:.4f} minspec(R)={np.linalg.eigvalsh((R+R.conj().T)/2).min():.6f}")
    print(f"   even spec {np.round(np.sort_complex(le),8)}")
    print(f"   odd spec  {np.round(np.sort_complex(lo),6)}  =? diag(conj D, D) {np.round(np.sort_complex(np.diag(Dt)),6)}")
    print(f"   Eo - diag(conjD,D) resid {np.linalg.norm(Eo-Dt):.2e}; normality ||[E,E*]|| {np.linalg.norm(E@E.conj().T-E.conj().T@E):.2e}; Ee hermitian resid {np.linalg.norm(Ee-Ee.conj().T):.2e}")
    print(f"   max rel err  str E^n vs N_n, n<={nmax}: {err:.2e}")
    # depolarising identity (4.7)
    Bs=[A[1:,1:] for A in As[:p['neven']]]
    X=np.random.default_rng(3).normal(size=(g,g))+1j*np.random.default_rng(4).normal(size=(g,g))
    dep=sum(B@X@B.conj().T for B in Bs)-p['w']*np.trace(X)*np.eye(g)
    print(f"   depolarising (4.7) residual {np.linalg.norm(dep):.2e}")
    return err

print("--- (a) q=25, the F_25 base change of the F_5 curve (T4.4) ---")
r=np.roots([1,-3,7,-15,25]); reps=[]
for a in r:
    if not any(abs(np.conj(a)-b)<1e-8 for b in reps): reps.append(a)
pis25=[reps[0]**2, reps[1]**2]
print("   roots of z^4-3z^3+7z^2-15z+25:", np.round(r,6), " |.|^2 =", np.round(np.abs(r)**2,10))
print("   squared reps (q=25):", np.round(pis25,8), " char poly of {pi^2, conj}:", np.round(np.poly(list(pis25)+[np.conj(z) for z in pis25]).real,8))
report(25, pis25, label="  ")

print("\n--- (b) generic q>=16 with random unit-modulus phases ---")
rng=np.random.default_rng(2026)
for q in [16,17,19,23,25,27,32,49,10**4]:
    ph=rng.uniform(0,2*np.pi,2); pis=[np.sqrt(q)*np.exp(1j*ph[0]), np.sqrt(q)*np.exp(1j*ph[1])]
    report(q,pis,nmax=10,label="  ")

print("\n--- (c) the boundary q+1 >= 4 sqrt q ---")
for q in [4,5,7,8,9,11,13,13.928,13.929,16]:
    try:
        build(q,[np.sqrt(q)*np.exp(0.3j), np.sqrt(q)*np.exp(2.1j)])
        print(f"   q={q}: R PSD, construction OK   (q+1={q+1:.4f} vs 4 sqrt q={4*np.sqrt(q):.4f})")
    except ValueError as e:
        print(f"   q={q}: FAILS as predicted      (q+1={q+1:.4f} vs 4 sqrt q={4*np.sqrt(q):.4f})  [{e}]")
print("   7+4 sqrt 3 =", 7+4*np.sqrt(3))

print("\n--- (d) C^{1|g} extension, g=3: t=(q+1)/2, w=(q+1)/(2g), h=(q-1)/(2 sqrt g), q+1>=2 g sqrt q ---")
for q in [25,31,32,37,41,49,64,121]:
    pis=[np.sqrt(q)*np.exp(1j*x) for x in [0.4,1.9,3.7]]
    try: report(q,pis,nmax=9,label="  ")
    except ValueError as e: print(f"   q={q}: fails (q+1={q+1} vs 2g sqrt q={6*np.sqrt(q):.4f})  [{e}]")
print("   threshold for g=3: q >= (3+2 sqrt 2)^2 =", (3+2*np.sqrt(2))**2)
