# Reviewer claude:opus-5: T4.4 numbers, and T4.1 index conventions against a direct E = sum A (x) conj A.
import numpy as np, itertools
# T4.4 base change
a,b,q = 3,7,5
ap = a*a-2*b; bp = b*b-2*a*(q*a)+2*q*q
print("T4.4: a'=",ap," b'=",bp," q'^2=",q**4, " -> z^4 - (a')z^3 + b' z^2 - q' a' z + q'^2 =",
      np.poly1d([1,-ap,bp,-25*ap,625]))
r2=np.roots([1,-3,7,-15,25])**2
print("  direct: char poly of squared roots:", np.round(np.poly(r2).real,6))
print("  N_n over F_25, n=1..6:", [int(round(1+25**n-sum((r2**n).real))) for n in range(1,7)])
print("  (astra claims 31, 619, 15991, 390739, 9759526, 244128859)")
print("  N_n over F_5 , n=1..6:", [int(round(1+5**n-sum((np.roots([1,-3,7,-15,25])**n).real))) for n in range(1,7)])

# T4.1 conventions: build random 1|2 tensors, compare block formulas (4.1),(4.2) with direct E.
rng=np.random.default_rng(5)
S,Fo=2,2
aa=[rng.normal()+1j*rng.normal() for _ in range(S)]
BB=[rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)) for _ in range(S)]
cc=[rng.normal(size=(1,2))+1j*rng.normal(size=(1,2)) for _ in range(Fo)]
dd=[rng.normal(size=(2,1))+1j*rng.normal(size=(2,1)) for _ in range(Fo)]
As=[]
for s in range(S):
    A=np.zeros((3,3),complex); A[0,0]=aa[s]; A[1:,1:]=BB[s]; As.append(A)
for f in range(Fo):
    A=np.zeros((3,3),complex); A[0,1:]=cc[f]; A[1:,0:1]=dd[f]; As.append(A)
E=sum(np.kron(A,A.conj()) for A in As)
P=np.array([1.,-1.,-1.]); G=np.kron(P,P)
ev=np.where(G==1)[0]; od=np.where(G==-1)[0]
print("\n  even indices", ev, " odd indices", od)
M=sum(aa[s]*BB[s].conj() for s in range(S))
N=sum(dd[f].conj()@cc[f] for f in range(Fo))
Eo_pred=np.block([[M,N],[N.conj(),M.conj()]])
print("  (4.1) odd block residual:", np.linalg.norm(E[np.ix_(od,od)]-Eo_pred))
t=sum(abs(x)**2 for x in aa)
u=sum(np.kron(cc[f],cc[f].conj()) for f in range(Fo))         # 1x4 row
v=sum(np.kron(dd[f],dd[f].conj()) for f in range(Fo))         # 4x1 col
W=sum(np.kron(BB[s],BB[s].conj()) for s in range(S))
Ee_pred=np.block([[np.array([[t]]),u],[v,W]])
print("  (4.2) even block residual:", np.linalg.norm(E[np.ix_(ev,ev)]-Ee_pred))
# H-TWIST check: str E^n == sum_words |Tr(P A_{s1}...A_{sn})|^2
Pm=np.diag(P)
for n in range(1,6):
    lhs=complex(np.sum(G*np.diag(np.linalg.matrix_power(E,n))))
    rhs=sum(abs(np.trace(Pm@np.linalg.multi_dot([As[i] for i in w]) if n>1 else Pm@As[w[0]]))**2
            for w in itertools.product(range(len(As)),repeat=n))
    print(f"  n={n}: str E^n = {lhs.real:.10f} (im {lhs.imag:.1e})   sum_w |Tr(P A_w)|^2 = {rhs:.10f}")
