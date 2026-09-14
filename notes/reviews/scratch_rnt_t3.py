# Reviewer claude:opus-5. Independent checks of T3.1-T3.3 and ledger item 18.
import numpy as np
rng = np.random.default_rng(7)

def E_blocks(as_, Bs):
    """even tensors A_s = a_s (+) B_s on C^{m|k}; return S+, S-, M, and the full E, Gamma."""
    m = as_[0].shape[0]; k = Bs[0].shape[0]
    Sp = sum(np.kron(a, a.conj()) for a in as_)
    Sm = sum(np.kron(B, B.conj()) for B in Bs)
    M  = sum(np.kron(a, B.conj()) for a, B in zip(as_, Bs))
    As = [np.block([[a, np.zeros((m,k))],[np.zeros((k,m)), B]]) for a,B in zip(as_,Bs)]
    E  = sum(np.kron(A, A.conj()) for A in As)
    P  = np.diag([1.0]*m + [-1.0]*k)
    G  = np.kron(np.diag(P), np.diag(P))
    return Sp, Sm, M, E, G

print("=== C1: Tr(sum A (x) conj A) = sum |Tr A|^2, not sum ||A||_HS^2 ===")
for trial in range(4):
    D = rng.integers(2,5)
    As = [rng.normal(size=(D,D)) + 1j*rng.normal(size=(D,D)) for _ in range(3)]
    lhs = sum(np.trace(np.kron(A, A.conj())) for A in As)
    r1  = sum(abs(np.trace(A))**2 for A in As)
    r2  = sum(np.linalg.norm(A,'fro')**2 for A in As)
    print(f"  D={D}: Tr E = {lhs.real:.6f}  sum|TrA|^2 = {r1:.6f}  sum||A||_HS^2 = {r2:.6f}")

print("\n=== C2: T3.1 <1>5 Pauli-diagonal counterexample to the DRAFTED bound ===")
a = np.diag([1.0,-1.0]); B = np.diag([1.0,-1.0])
Sp, Sm, M, E, G = E_blocks([a],[B])
odd = np.where(G==-1)[0]; ev = np.where(G==1)[0]
mu_odd = np.linalg.eigvals(E[np.ix_(odd,odd)])
print("  Tr S+ =", np.trace(Sp).real, " Tr S- =", np.trace(Sm).real)
print("  sum_odd |mu|^2 =", float(np.sum(np.abs(mu_odd)**2)),
      "  drafted RHS 2 Tr(S+)Tr(S-) =", float(2*np.trace(Sp).real*np.trace(Sm).real))
print("  repaired RHS 2 tau+ tau- =", float(2*np.linalg.norm(a,'fro')**2*np.linalg.norm(B,'fro')**2))
print("  2||M||_HS^2 =", float(2*np.linalg.norm(M,'fro')**2))
print("  => drafted bound FALSE (8 <= 0 fails); repaired bound holds.")

print("\n=== C3: (3.1),(3.2),(3.4) on random instances (m,k up to 3, 4 species) ===")
bad = 0
for trial in range(300):
    m = int(rng.integers(1,4)); k = int(rng.integers(1,4)); S = int(rng.integers(1,5))
    as_ = [rng.normal(size=(m,m))+1j*rng.normal(size=(m,m)) for _ in range(S)]
    Bs  = [rng.normal(size=(k,k))+1j*rng.normal(size=(k,k)) for _ in range(S)]
    Sp, Sm, M, E, G = E_blocks(as_, Bs)
    odd = np.where(G==-1)[0]
    mu = np.linalg.eigvals(E[np.ix_(odd,odd)])
    tp = sum(np.linalg.norm(a,'fro')**2 for a in as_); tm = sum(np.linalg.norm(B,'fro')**2 for B in Bs)
    ok31 = np.sum(np.abs(mu)**2) <= 2*np.linalg.norm(M,'fro')**2 + 1e-8 <= 2*tp*tm + 1e-8
    ok32 = np.linalg.norm(M,'fro')**2 <= np.linalg.norm(Sp,'fro')*np.linalg.norm(Sm,'fro') + 1e-8
    ok34 = all(abs(np.trace(np.linalg.matrix_power(M,n)))**2 <=
               np.trace(np.linalg.matrix_power(Sp,n)).real*np.trace(np.linalg.matrix_power(Sm,n)).real + 1e-6
               for n in range(1,7))
    okodd = np.allclose(np.sort_complex(np.linalg.eigvals(E[np.ix_(odd,odd)])),
                        np.sort_complex(np.concatenate([np.linalg.eigvals(M), np.linalg.eigvals(M.conj())])))
    if not (ok31 and ok32 and ok34 and okodd): bad += 1; print("  FAIL", m,k,S, ok31, ok32, ok34, okodd)
print("  failures:", bad, "/300  (odd block = M (+) conj M also verified)")

print("\n=== C4: T3.2 word formula s_pm(n) = sum_w |Tr a_w|^2 ===")
import itertools
m=k=2; S=2
as_ = [rng.normal(size=(m,m))+1j*rng.normal(size=(m,m)) for _ in range(S)]
Bs  = [rng.normal(size=(k,k))+1j*rng.normal(size=(k,k)) for _ in range(S)]
Sp,Sm,M,E,G = E_blocks(as_,Bs)
for n in range(1,5):
    wp = sum(abs(np.trace(np.linalg.multi_dot([as_[i] for i in w]) if n>1 else as_[w[0]]))**2
             for w in itertools.product(range(S), repeat=n))
    tm_ = sum(np.trace(np.linalg.multi_dot([as_[i] for i in w]) if n>1 else as_[w[0]])*
              np.conj(np.trace(np.linalg.multi_dot([Bs[i] for i in w]) if n>1 else Bs[w[0]]))
              for w in itertools.product(range(S), repeat=n))
    print(f"  n={n}: Tr S+^n = {np.trace(np.linalg.matrix_power(Sp,n)).real:.8f} vs word sum {wp:.8f};"
          f"  Tr M^n - word = {abs(np.trace(np.linalg.matrix_power(M,n))-tm_):.2e}")

print("\n=== C5: T3.3 <1>1 - can both 1 and q sit in one even block? ===")
print("  If S- is nilpotent then s_-(n)=0 for all n>=1, so by (3.4) Tr M^n=0 for all n,")
print("  so M is nilpotent and the odd spectrum is empty.  Numeric spot check:")
q=5.0
a0 = np.array([[1.0]]); a1=np.array([[0.0]])
B0 = np.array([[0,1.0],[0,0]]); B1=np.array([[0,0],[0,0]])   # S- nilpotent
Sp,Sm,M,E,G = E_blocks([a0,a1],[B0,B1])
print("   nilpotent S- : spec S- =", np.round(np.linalg.eigvals(Sm),12),
      " spec M =", np.round(np.linalg.eigvals(M),12))

print("\n=== C6: T3.3 <1>5 counterexamples ===")
pi = 1+2j; q = abs(pi)**2
N = np.zeros((2,2)); N[0,1]=1.0
B0 = np.zeros((3,3),complex); B0[0,0]=pi
B1 = np.zeros((3,3),complex); B1[1:,1:] = N
Sp,Sm,M,E,G = E_blocks([np.array([[1.0+0j]]), np.array([[0.0+0j]])],[B0,B1])
ev=np.where(G==1)[0]; od=np.where(G==-1)[0]
print("  (a) m=1,k=3: even nonzero spec =",
      np.round(np.sort_complex(np.linalg.eigvals(E[np.ix_(ev,ev)]))[-3:],10))
print("      odd nonzero spec =", np.round([z for z in np.linalg.eigvals(E[np.ix_(od,od)]) if abs(z)>1e-9],10))
print("      B_1 != 0 while a_1 = 0 :", np.linalg.norm(B1)>0)
b = 0.7
B0 = np.array([[pi, b],[0,0]],dtype=complex)
Sp,Sm,M,E,G = E_blocks([np.array([[1.0+0j]])],[B0])
ev=np.where(G==1)[0]; od=np.where(G==-1)[0]
print("  (b) m=1,k=2: even spec =", np.round(np.sort_complex(np.linalg.eigvals(E[np.ix_(ev,ev)])),10))
print("      odd spec =", np.round(np.sort_complex(np.linalg.eigvals(E[np.ix_(od,od)])),10))
print("      M normal? ", np.allclose(M@M.conj().T, M.conj().T@M), " ||[M,M*]|| =", np.linalg.norm(M@M.conj().T-M.conj().T@M))
print("      str E^n vs N_n:", [ (float(np.real(np.sum(G*np.diag(np.linalg.matrix_power(E,n))))), float(1+q**n-2*np.real(pi**n))) for n in range(1,5)])

print("\n=== C7: Cesaro step of T3.3 <1>3 ===")
for g,betas in [(1,[np.exp(0.7j)]), (2,[np.exp(0.7j),np.exp(2.3j)]), (2,[np.exp(0.7j)]*2), (3,[np.exp(0.7j),np.exp(2.3j),np.exp(4.1j)])]:
    Nn=200000
    av = np.mean([abs(sum(b**n for b in betas))**2 for n in range(1,Nn+1)])
    print(f"  g={g} distinct={len(set(np.round(betas,9)))}: Cesaro mean = {av:.6f}  (sum m_i^2 = "
          f"{sum(c*c for c in __import__('collections').Counter(np.round(betas,9)).values())})  bound 1 -> g<=1")
