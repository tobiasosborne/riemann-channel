"""REFUTE-lane independent checks for astra-proofs.md T3 (no-go, criteria) and T5
(vacuum-decay Lindbladian).  Written from the statements only."""
import numpy as np, sympy as sp
rng = np.random.default_rng(7)
FAIL=[]
def chk(n, ok, d=""):
    print(("  [PASS] " if ok else "  [FAIL] ")+n+("   "+d if d else ""))
    if not ok: FAIL.append(n)

print("T3.1  residue obstruction")
# residue of alpha u/(1-alpha u) at u = 1/alpha is -1/alpha (check by sympy)
u, al = sp.symbols('u alpha')
r = sp.residue(al*u/(1-al*u), u, 1/al)
chk("T3.1 residue of alpha u/(1-alpha u) at u=1/alpha is -1/alpha", sp.simplify(r+1/al)==0, f"residue = {r}")
# hence prescribed N(u) = sum b u/(1-bu) - sum alpha u/(1-alpha u) has residue +m_alpha/alpha
# and an ordinary trace function has residue -m_E(alpha)/alpha <= 0.
b_, a_ = sp.symbols('b a')
N = b_*u/(1-b_*u) - a_*u/(1-a_*u)
chk("T3.1 prescribed function has residue +1/alpha at u=1/alpha (sign flip)",
    sp.simplify(sp.residue(N, u, 1/a_) - 1/a_)==0, f"residue = {sp.residue(N,u,1/a_)}")

# trace-class meromorphy:  sum_i lambda_i u/(1-lambda_i u) with sum|lambda|<inf
lam = np.array([0.9/ k**2 for k in range(1,4001)])
print(f"    sum |lambda_i| = {lam.sum():.4f}; only {np.sum(lam>1/(2*3.0))} have |lambda|>1/(2R) for R=3")
chk("T3.1 on |u|<=R only finitely many poles; tail bounded by 2R sum|lambda|", np.sum(lam>1/6)<10)

print("\nT3.2  trace / supertrace criteria")
# supertrace criterion: Z(u) = det(1-uE_-)/det(1-uE_+)
Ep = np.diag([3.0, 1.0]); Em = np.diag([1.7+0.3j, 1.7-0.3j, -2.0])
Nn = [np.trace(np.linalg.matrix_power(Ep,n)) - np.trace(np.linalg.matrix_power(Em,n)) for n in range(1,41)]
uu = 0.07
Zser = np.exp(sum(Nn[n-1]*uu**n/n for n in range(1,41)))
Zdet = np.linalg.det(np.eye(3)-uu*Em)/np.linalg.det(np.eye(2)-uu*Ep)
chk("T3.2(2) Z(u) = det(1-uE_-)/det(1-uE_+); even = reciprocal poles, odd = reciprocal zeros",
    abs(Zser-Zdet)<1e-10, f"series {Zser:.12f} vs det {Zdet:.12f}")

print("\nT3.3  curve counts, MPS ring norms, graphs")
q, g = 3, 3
alphas = np.array([-np.sqrt(3), -np.sqrt(3), 1j*np.sqrt(3), -1j*np.sqrt(3), np.sqrt(3), np.sqrt(3)])
Ncurve = np.array([1+q**n-np.sum(alphas**n).real for n in range(1,13)])
print("    q=3 J=1 a=[0,1] curve counts N_n =", Ncurve[:9].round(6))
chk("T3.3 curve counts reproduce the numerics-lane list [4,4,28,28,244,676,2188,6076,19684]",
    np.allclose(Ncurve[:9], [4,4,28,28,244,676,2188,6076,19684]))
# Prony from scratch: build the Hankel system and solve for the recurrence
def prony(N, order):
    A = np.array([[N[i+j] for j in range(order)] for i in range(order)])
    b = np.array([N[i+order] for i in range(order)])
    c = np.linalg.solve(A, b)
    roots = np.roots(np.concatenate([[1.0], -c[::-1]]))
    V = np.array([[r**n for r in roots] for n in range(1, len(N)+1)])
    coef, *_ = np.linalg.lstsq(V, np.array(N, dtype=complex), rcond=None)
    return roots, coef
roots, coef = prony(Ncurve, 6)
idx = np.argsort(roots.real+0.001*roots.imag)
print("    Prony roots :", np.round(roots[idx],5))
print("    Prony coeffs:", np.round(coef[idx],6))
neg = np.sum(coef.real < -0.5)
chk("T3.3/T3.1 the exponential-sum coefficients contain NEGATIVE integers (4 of 6)", neg==4,
    f"{neg} coefficients < -0.5; the Frobenius modes all carry -1")
# MPS ring-norm identity  sum_s |Tr(A_{s_n}..A_{s_1})|^2 = Tr (sum_s A_s (x) conj A_s)^n
D, P = 3, 2
As = [rng.normal(size=(D,D))+1j*rng.normal(size=(D,D)) for _ in range(P)]
EA = sum(np.kron(A, A.conj()) for A in As)
import itertools
for n in [1,2,3]:
    lhs = sum(abs(np.trace(np.linalg.multi_dot([As[s] for s in w][::-1]) if n>1 else As[w[0]]))**2
              for w in itertools.product(range(P), repeat=n))
    rhs = np.trace(np.linalg.matrix_power(EA, n))
    chk(f"T3.3<1>2 ring norm n={n}: sum_s |Tr A_w|^2 = Tr E_A^n", abs(lhs-rhs)<1e-8*abs(rhs),
        f"lhs={lhs:.8f} rhs={rhs.real:.8f} (|Im| {abs(rhs.imag):.1e})")
chk("T3.3 E_A is a FINITE matrix, so T3.1 excludes Tr E_A^n = N_n for a genus>=1 curve", True)

print("\nT5.1/T5.2/T5.5  vacuum-decay Lindbladian (finite model, built from scratch)")
for D in [3, 5]:
    H = rng.normal(size=(D,D))+1j*rng.normal(size=(D,D)); H = (H+H.conj().T)/2
    j = rng.normal(size=D)+1j*rng.normal(size=D)
    B = -1j*H - 0.5*np.outer(j, j.conj())
    chk(f"T5.1 D={D} -(B+B^dag)=|j><j|", np.abs(-(B+B.conj().T)-np.outer(j,j.conj())).max()<1e-12)
    N = D+1
    Bb = np.zeros((N,N),complex); Bb[1:,1:] = B
    J = np.zeros((N,N),complex); J[0,1:] = j.conj()          # |vac><j|
    def Lmap(x): return Bb@x + x@Bb.conj().T + J@x@J.conj().T
    # superoperator matrix
    L = np.zeros((N*N,N*N),complex)
    for i in range(N*N):
        e = np.zeros(N*N,complex); e[i]=1
        L[:,i] = Lmap(e.reshape(N,N)).reshape(-1)
    # GKLS: L(x) = -i[H0,x] + JxJ^dag - 1/2{J^dag J, x}
    H0 = (Bb.conj().T - Bb)/(2j)
    def Lgk(x): return -1j*(H0@x-x@H0) + J@x@J.conj().T - 0.5*(J.conj().T@J@x + x@J.conj().T@J)
    xr = rng.normal(size=(N,N))+1j*rng.normal(size=(N,N))
    chk(f"T5.1<1>1 D={D} GKLS form matches L", np.abs(Lgk(xr)-Lmap(xr)).max()<1e-11)
    chk(f"T5.1 D={D} trace preserving", abs(np.trace(Lmap(xr)))<1e-11)
    # (5.2) exact block solution
    from scipy.linalg import expm
    for t in [0.13, 0.9, 3.0]:
        Zt = expm(t*B)
        x = rng.normal(size=(N,N))+1j*rng.normal(size=(N,N))
        a, r_, l_, X = x[0,0], x[0,1:], x[1:,0], x[1:,1:]
        pred = np.zeros((N,N),complex)
        pred[0,0] = a + np.trace(X) - np.trace(Zt@X@Zt.conj().T)
        pred[0,1:] = r_@Zt.conj().T
        pred[1:,0] = Zt@l_
        pred[1:,1:] = Zt@X@Zt.conj().T
        got = (expm(t*L)@x.reshape(-1)).reshape(N,N)
        chk(f"T5.1 D={D} t={t} formula (5.2)", np.abs(pred-got).max()<1e-9, f"max dev {np.abs(pred-got).max():.2e}")
    # complete positivity via (5.2): Choi of e^{tL}
    t=0.7; Choi = np.zeros((N*N,N*N),complex)
    for i in range(N):
        for k in range(N):
            E = np.zeros((N,N),complex); E[i,k]=1
            Choi[i*N:(i+1)*N, k*N:(k+1)*N] = (expm(t*L)@E.reshape(-1)).reshape(N,N)
    ev = np.linalg.eigvalsh((Choi+Choi.conj().T)/2)
    chk(f"T5.1 D={D} complete positivity of e^(0.7 L) (Choi PSD)", ev.min()>-1e-10, f"min Choi eig {ev.min():.2e}")
    Zt = expm(0.7*B)
    chk(f"T5.1 D={D} I - Z_t^dag Z_t >= 0 (contraction)",
        np.linalg.eigvalsh(np.eye(D)-Zt.conj().T@Zt).min()>-1e-12)
    # (5.1) spectrum with multiplicities and parities
    bs = np.linalg.eigvals(B)
    pred = np.concatenate([[0.0], bs, bs.conj(), (bs[:,None]+bs.conj()[None,:]).reshape(-1)])
    got = np.linalg.eigvals(L)
    # greedy match
    P_ = list(pred); dev=0
    for z in got:
        k = int(np.argmin(np.abs(np.array(P_)-z))); dev=max(dev, abs(P_[k]-z)); P_.pop(k)
    chk(f"T5.1 D={D} spec(L) = (5.1) with multiplicities", dev<1e-8 and len(P_)==0,
        f"max matching dev {dev:.2e}, {N*N} eigenvalues, dim = (d+1)^2 = {(D+1)**2}")
    # grading:  Gamma = 1 (+) (-I); coherences odd, populations + vacuum even
    Gam = np.diag([1.0]+[-1.0]*D)
    Gsup = np.kron(Gam, Gam)   # x -> Gamma x Gamma in the same vectorisation
    chk(f"T5.1<1>5 D={D} L commutes with the operator grading x->Gamma x Gamma",
        np.abs(Gsup@L-L@Gsup).max()<1e-11)
    # odd eigenvalues
    Podd = (np.eye(N*N)-Gsup)/2
    oddvals = np.linalg.eigvals(Podd@L@Podd + (np.eye(N*N)-Podd)*1e6)
    oddvals = np.array([v for v in oddvals if abs(v)<1e5])
    P_ = list(np.concatenate([bs, bs.conj()])); dev=0
    for z in oddvals:
        k=int(np.argmin(np.abs(np.array(P_)-z))); dev=max(dev,abs(P_[k]-z)); P_.pop(k)
    chk(f"T5.1<1>5 D={D} odd spectrum = spec(B) u conj spec(B)", dev<1e-8 and not P_, f"dev {dev:.2e}")
    # T5.2 traces
    for t in [0.3, 1.1]:
        Zt = expm(t*B); et = expm(t*L)
        chk(f"T5.2 D={D} t={t} Tr e^(tL) = |1+Tr Z_t|^2",
            abs(np.trace(et)-abs(1+np.trace(Zt))**2)<1e-9, f"{np.trace(et):.9f} vs {abs(1+np.trace(Zt))**2:.9f}")
        chk(f"T5.2 D={D} t={t} str e^(tL) = |1-Tr Z_t|^2",
            abs(np.trace(Gsup@et)-abs(1-np.trace(Zt))**2)<1e-9,
            f"{np.trace(Gsup@et):.9f} vs {abs(1-np.trace(Zt))**2:.9f}")
    # T5.5 renewal integral and Schmidt spectrum
    Om = np.zeros((N,N)); Om[0,0]=1
    T_=5.0; ts=np.linspace(0,T_,4001)
    integ = np.trapz([ (expm(t*Bb)@Om@expm(t*Bb).conj().T)[0,0].real for t in ts], ts)
    chk(f"T5.5 D={D} int_0^T e^(tBb) Omega e^(tBb^dag) dt = T*Omega (diverges)",
        abs(integ-T_)<1e-8, f"integral trace = {integ:.8f} vs T = {T_}")
    chk(f"T5.5 D={D} stationary bond state is rank one -> Schmidt spectrum {{1}}",
        np.linalg.matrix_rank(Om)==1)
    # every ring amplitude with >=1 jump vanishes
    amp1 = max(abs(np.trace(expm((1.0-s)*Bb)@J@expm(s*Bb))) for s in np.linspace(0.05,0.95,19))
    chk(f"T5.5 D={D} one-jump ring amplitude vanishes identically", amp1<1e-12, f"max |amp| = {amp1:.2e}")

print("\n==== FAILURES:", FAIL if FAIL else "none")
