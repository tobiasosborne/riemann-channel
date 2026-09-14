# Reviewer claude:opus-5.  T4.5a: rebuild the certified tensors, check chi_e, chi_o, str E^n, JW Fock norms.
import sys, itertools
import numpy as np
sys.path.insert(0,'scripts')
from fractions import Fraction as F

base_text="0.26071183 -0.77630597 0.1256142 0.57129743 0.23357458 -0.48921698 -1.34760956 -0.05591677 -0.94940643 -0.38739751 -0.67840262 -1.61862569 0.09572017 -0.36950433 -0.80102781 0.32500101 -1.0690133 -0.50378403 0.0903946 -0.85610066 -0.89848953 -0.00971177 -0.9517933 -0.63028434 0.30058661 1.43919288 0.38038457 -1.21909557".split()
sel=[18,15,11,19,14,2,22,4,3]
active=['0.0903946022326197086918581936003652642108422681757834121198569509935751292079285209190880028',
 '0.325001015712151197553026743073611383028909263869300480901353211781331926553983584722142652',
 '-1.61862568848573412561085612335033964354282729706378489347434769629526938804341538871295182',
 '-0.856100671883734631506405289461842300801039252464833047343784570879130428726933907333213827',
 '-0.80102781481057057826927943665335609983310469191396383065095317561795085119201793039066329',
 '0.125614201299343247797946104304359812581511668431930091377412797232085492448163457526247418',
 '-0.951793304521566588362992674206553375775973049960369410863894719514069329407054372830229032',
 '0.233574566527024915170370648357379441749679527579971848850435885749412325417262635189600452',
 '0.571297437238715211680159923446246584732241927298292338354479377560643476028340257150472248']
pos=[(s,i,j) for s in range(3) for i in range(3) for j in range(3) if (s<2)==((i==0)==(j==0))]
print("positions (species,row,col):", pos)
x=[float(v) for v in base_text]
for l,v in zip(sel,active): x[l]=float(v)
As=[np.zeros((3,3),complex) for _ in range(3)]
for l,(s,i,j) in enumerate(pos): As[s][i,j]=x[2*l]+1j*x[2*l+1]
print("\nspecies 0 (even):\n",np.round(As[0],6)); print("species 1 (even):\n",np.round(As[1],6)); print("species 2 (odd):\n",np.round(As[2],6))
assert np.allclose(As[0][0,1:],0) and np.allclose(As[0][1:,0],0), "species 0 not even"
assert np.allclose(As[1][0,1:],0) and np.allclose(As[1][1:,0],0), "species 1 not even"
assert abs(As[2][0,0])==0 and np.allclose(As[2][1:,1:],0), "species 2 not odd"

E=sum(np.kron(A,A.conj()) for A in As)
P=np.array([1.,-1.,-1.]); G=np.kron(P,P)
ev=np.where(G==1)[0]; od=np.where(G==-1)[0]
Ee=E[np.ix_(ev,ev)]; Eo=E[np.ix_(od,od)]
print("\nchi_e coefficients (should be z^5 -6z^4 +5z^3 = [1,-6,5,0,0,0]):", np.round(np.poly(Ee).real,10), " imag max", np.max(np.abs(np.poly(Ee).imag)))
print("chi_o coefficients (should be [1,-3,7,-15,25]):", np.round(np.poly(Eo).real,10), " imag max", np.max(np.abs(np.poly(Eo).imag)))
print("even spec:", np.round(np.sort_complex(np.linalg.eigvals(Ee)),10))
print("odd  spec:", np.round(np.sort_complex(np.linalg.eigvals(Eo)),8))
print("target Frobenius roots:", np.round(np.sort_complex(np.roots([1,-3,7,-15,25])),8))
print("|odd eig|^2 (Ramanujan, should all be 5):", np.round(np.abs(np.linalg.eigvals(Eo))**2,10))
al=np.roots([1,-3,7,-15,25])
print("\n n :  str E^n            N_n = 1+5^n-p_n      rel err")
for n in range(1,13):
    st=complex(np.sum(G*np.diag(np.linalg.matrix_power(E,n))))
    Nn=1+5.0**n-np.sum(al**n).real
    print(f" {n:2d}: {st.real:22.10f}  {Nn:22.10f}   {abs(st-Nn)/abs(Nn):.2e}  (im {st.imag:.1e})")
# H-TWIST word check
Pm=np.diag(P)
for n in range(1,6):
    st=complex(np.sum(G*np.diag(np.linalg.matrix_power(E,n))))
    rhs=sum(abs(np.trace(Pm@np.linalg.multi_dot([As[i] for i in w]) if n>1 else Pm@As[w[0]]))**2 for w in itertools.product(range(3),repeat=n))
    print(f"  word check n={n}: str E^n {st.real:.9f} vs sum_w |Tr(P A_w)|^2 {rhs:.9f}")
# normality?
print("\n||[E,E*]|| =", np.linalg.norm(E@E.conj().T-E.conj().T@E), "  (T4.5a makes no normality claim)")
# Jordan-Wigner explicit Fock vector
import cmps_parity_supertrace as cps
D=3; P3=np.diag([1.0,-1.0,-1.0]).astype(complex)
Q=As[0]-np.eye(D); Rs=[As[1], As[2], np.zeros((D,D),complex)]
print("\nJordan-Wigner lattice model (species0 -> 1+Q, species1 -> boson R, species2 -> fermion R):")
for n in (2,3,4,5):
    cre=cps.creation_ops(n)
    psiP=cps.mps_state(n,1.0,Q,Rs,P3,cre)
    nP=np.vdot(psiP,psiP).real
    Nn=1+5.0**n-np.sum(al**n).real
    T=cps.translation_op(n,antiperiodic=False)
    print(f"  n={n}: ||Psi_P||^2 = {nP:.9f}   N_n = {Nn:.9f}  diff {nP-Nn:.2e};  periodic-translation resid {np.linalg.norm(T@psiP-psiP):.1e}")
