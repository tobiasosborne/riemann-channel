# Independent check (claude:fable-5.1) of Theorem T4.3: explicit 1|2 tensors, 5 even + 4 odd letters, for q >= 16.
import numpy as np, sys
def build(q, pi1, pi2):
    t=(q+1)/2; w=(q+1)/4; h=(q-1)/(2*np.sqrt(2))
    D=np.diag([pi1,pi2]); B0=D/np.sqrt(t)
    b0=B0.reshape(-1,1)            # row-major vec
    nu=(b0.conj().T@b0)[0,0].real
    assert w>=nu-1e-12, (w,nu)
    S=np.sqrt(w)*np.eye(4)+((np.sqrt(w-nu)-np.sqrt(w))/nu)*(b0@b0.conj().T)
    R=w*np.eye(4)-b0@b0.conj().T
    assert np.allclose(S@S,R)
    Bs=[B0]+[ (S@np.eye(4)[:,l]).reshape(2,2) for l in range(4)]
    As=[]
    A=np.zeros((3,3),complex); A[0,0]=np.sqrt(t); A[1:,1:]=B0; As.append(A)
    for l in range(1,5):
        A=np.zeros((3,3),complex); A[1:,1:]=Bs[l]; As.append(A)
    for j in range(2):
        A=np.zeros((3,3),complex); A[0,1+j]=np.sqrt(h); As.append(A)
        A=np.zeros((3,3),complex); A[1+j,0]=np.sqrt(h); As.append(A)
    return As
def check(q, pi1, pi2, N=8):
    As=build(q,pi1,pi2)
    E=sum(np.kron(A,A.conj()) for A in As)
    par=np.array([1,-1,-1]); G=np.kron(par,par)
    ev=np.where(G==1)[0]; od=np.where(G==-1)[0]
    le=np.sort_complex(np.linalg.eigvals(E[np.ix_(ev,ev)])); lo=np.sort_complex(np.linalg.eigvals(E[np.ix_(od,od)]))
    target=[1+q**n-(pi1**n+pi2**n+np.conj(pi1)**n+np.conj(pi2)**n) for n in range(1,N+1)]
    st=[np.trace(G[:,None]*np.linalg.matrix_power(E,n)) for n in range(1,N+1)]
    err=max(abs(a-b)/abs(b) for a,b in zip(st,target))
    normal=np.linalg.norm(E@E.conj().T-E.conj().T@E)
    print(f"q={q}: even eig {np.round(le,6)}; odd eig {np.round(lo,5)}; max rel err str-N_n (n<=8) {err:.1e}; normality {normal:.1e}")
    return err<1e-10
# the F_25 base change of the F_5 genus-2 curve: pi_j^2 with pi from z^4-3z^3+7z^2-15z+25
r=np.roots([1,-3,7,-15,25]); reps=[]
for a in r:
    if not any(abs(np.conj(a)-b)<1e-8 for b in reps): reps.append(a)
ok=check(25, reps[0]**2, reps[1]**2)
ok&=check(17, np.sqrt(17)*np.exp(0.3j), np.sqrt(17)*np.exp(2.1j))
ok&=check(16, 4*np.exp(1.0j), 4*np.exp(-2.5j))
try:
    build(13, np.sqrt(13)*np.exp(0.3j), np.sqrt(13)*np.exp(2.1j)); print("q=13: built (unexpected)")
except AssertionError as e: print("q=13: construction fails as predicted (w < nu):", e)
print("T4.3 check:", "PASS" if ok else "FAIL")
