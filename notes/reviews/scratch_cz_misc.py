"""REFUTE lane scratch script (claude:opus).  Written from the STATEMENTS only.
T3.1 sign law, T5.4, T6.2<1>4/<1>6, T6.3<1>2, T6.5, T6.6, T1.2/T1.4 arithmetic."""
import itertools
import sympy as sp
u=sp.Symbol('u'); q=sp.Symbol('q',positive=True)

print("== T3.1: log Z_ord = sum_m (u^m/m) sum_k s_k^{m+1} Tr(T_k^m)  (exact, octahedron)")
pairs=[(0,1),(2,3),(4,5)]
tri=[t for t in itertools.combinations(range(6),3) if all(not set(p)<=set(t) for p in pairs)]
F=set()
for t in tri:
    for r in range(1,4):
        for s in itertools.combinations(t,r): F.add(frozenset(s))
def Om(k): return sorted([p for f in F if len(f)==k+1 for p in itertools.permutations(sorted(f))])
def Tk(k):
    st=Om(k); ii={s:i for i,s in enumerate(st)}; M=sp.zeros(len(st),len(st))
    for s in st:
        for w in range(6):
            if w in s or frozenset(s[1:]+(w,)) not in F or frozenset(s+(w,)) in F: continue
            M[ii[s[1:]+(w,)],ii[s]]+=1
    return M
T1,T2=Tk(1),Tk(2)
Z=sp.series(sp.log((1-u**6)**8/(1-u**4)**6),u,0,13).removeO()   # log Z_ord
lhs=[sp.Rational(sp.expand(Z).coeff(u,m)) for m in range(1,13)]
P1,P2=sp.eye(T1.rows),sp.eye(T2.rows)
rhs=[]
for m in range(1,13):
    P1=P1*T1; P2=P2*T2
    s1,s2=1,-1
    rhs.append(sp.Rational(s1**(m+1)*P1.trace()+s2**(m+1)*P2.trace(),m))
print("   coefficients match for m=1..12:", lhs==rhs)
print("   (a sign s_k^m instead of s_k^{m+1} would give:",
      [sp.Rational((1)**m*0,1) for _ in range(0)] or "mismatch at odd m", ")")
bad=[sp.Rational(1**m*(sp.eye(T1.rows)).trace()*0,1) for m in range(0)]
# explicit wrong-sign variant
P1,P2=sp.eye(T1.rows),sp.eye(T2.rows); wrong=[]
for m in range(1,13):
    P1=P1*T1; P2=P2*T2
    wrong.append(sp.Rational(1**m*P1.trace()+(-1)**m*P2.trace(),m))
print("   wrong-sign variant s_k^m matches:", wrong==lhs)

print("\n== T5.4: (1-u)/(1-2u)")
ser=sp.series((1-u)/(1-2*u),u,0,10).removeO()
print("   Taylor coefficients:", [sp.expand(ser).coeff(u,m) for m in range(10)],
      " all >= 0:", all(sp.expand(ser).coeff(u,m)>=0 for m in range(10)))
lg=sp.series(sp.log((1-u)/(1-2*u)),u,0,10).removeO()
print("   log coefficients m*c_m:", [sp.simplify(m*sp.expand(lg).coeff(u,m)) for m in range(1,10)],
      " = 2^m-1:", all(sp.simplify(m*sp.expand(lg).coeff(u,m)-(2**m-1))==0 for m in range(1,10)))
print("   reduced numerator nonconstant:", sp.cancel((1-u)/(1-2*u)))

print("\n== T6.2 <1>4: sum_k (-1)^k q^{k(k-1)/2} lambda_k u^k = prod_j (1 - q^{(n-1)/2} z_j u)")
for n in (3,4,5):
    zs=sp.symbols(f'z1:{n+1}')
    lhs=sum((-1)**k*q**sp.Rational(k*(k-1),2)*q**sp.Rational(k*(n-k),2)
            *sp.symmetric_poly(k,*zs)*u**k for k in range(n+1))
    rhs=sp.prod([1-q**sp.Rational(n-1,2)*zj*u for zj in zs])
    # impose e_n = prod z_j = 1
    d=sp.simplify(sp.expand(lhs-rhs).subs(sp.prod(zs),1))
    d=sp.simplify(sp.expand(lhs-rhs+ (-1)**n*q**sp.Rational(n*(n-1),2)*q**0*0))
    diff=sp.simplify(sp.expand(lhs-rhs))
    # difference must vanish once prod z = 1
    diff=sp.simplify(diff.subs(zs[-1], 1/sp.prod(zs[:-1])))
    print(f"   n={n}: identity holds on prod z_j = 1:", sp.simplify(sp.expand(diff))==0)

print("\n== T6.2 <1>6: |S_1| = q^2+q+1 vs tempered bound 3q")
print("   q^2+q+1 - 3q = (q-1)^2 > 0 for q>1:",
      sp.simplify(sp.expand((q**2+q+1)-3*q)-(q-1)**2)==0)
print("   q=3: 13 > 9 :", 13>9)

print("\n== T6.3 <1>2: Cay(Z/28, {+-1,+-3})")
lam=[2*sp.cos(2*sp.pi*j/28)+2*sp.cos(6*sp.pi*j/28) for j in range(28)]
v=[sp.N(x,12) for x in lam]
print("   spectrum (sorted desc):", sorted(set(round(float(x),6) for x in v),reverse=True)[:6])
j1=sp.N(lam[1],12); print("   j=1 eigenvalue =", j1, " 2*sqrt(3) =", sp.N(2*sp.sqrt(3),12),
      " exceeds:", j1>sp.N(2*sp.sqrt(3),12))
print("   is it 2cos(pi/14)+2cos(3pi/14)?",
      sp.simplify(lam[1]-(2*sp.cos(sp.pi/14)+2*sp.cos(3*sp.pi/14)))==0)
print("   bipartite (all generators odd):", all(g%2==1 for g in [1,27,3,25]),
      "; triangles s+t in S?:", any(((a+b)%28) in {1,27,3,25} for a in [1,27,3,25] for b in [1,27,3,25]))
print("   astra's rigorous bound 171/49 > 2 sqrt 3:", sp.Rational(171,49)**2 > 12,
      " and eigenvalue > 171/49:", j1>sp.N(sp.Rational(171,49),12))

print("\n== T6.5 <1>1: p_a(u) = -q^3 u^3 conj(p_a(1/(q^2 conj u)))")
a=sp.symbols('a'); ab=sp.symbols('abar')
pa=1-a*u+q*ab*u**2-q**3*u**3
# conj(p_a(w)) with w=1/(q^2 ubar):  swap a<->abar and u_bar -> u
conj_expr=1-ab/(q**2*u)+a/(q**3*u**2)-1/(q**3*u**3)
print("   identity:", sp.simplify(sp.expand(-q**3*u**3*conj_expr - pa))==0)
print("   fixed circle of u -> q^-2/conj(u): |u| = q^-1 :",
      sp.simplify(sp.sqrt(q**(-2)))==1/q)
print("== T6.5 <1>4: type-(e) chamber radii {q^-1/2 (x1), q^-1/4 (x2)}")
print("   fix both radii needs c = q^-1 and c = q^-1/2 simultaneously -> impossible for q>1")
print("   swap radii needs multiplicities 1 == 2 -> impossible")

print("\n== T6.6: positive definiteness of nu_m = sum (mu_j/r)^m")
import numpy as np
def pd(mus,r,M=40):
    nu=[sum((np.array(mus)/r)**m).sum() if False else sum((m_/r)**m for m_ in mus) for m in range(0,M+1)]
    nu=np.array(nu,dtype=complex)
    Tz=np.zeros((M+1,M+1),dtype=complex)
    for i in range(M+1):
        for j in range(M+1):
            k=i-j
            Tz[i,j]= nu[k] if k>=0 else np.conj(nu[-k])
    return np.linalg.eigvalsh((Tz+Tz.conj().T)/2).min()
inside=[0.9*np.exp(1j*0.3),0.5,-0.7,1.0]
outside=[1.3*np.exp(1j*0.3),0.5,-0.7]
print("   all |mu|<=r : min Toeplitz eigenvalue =", round(pd(inside,1.0),8), "(>= 0 expected)")
print("   one |mu|>r  : min Toeplitz eigenvalue =", round(pd(outside,1.0),6), "(< 0 expected)")

print("\n== T1.2 / T1.4 arithmetic")
def chis(fv):
    chi=sum((-1)**i*f for i,f in enumerate(fv))
    co=sum((-1)**i*sp.factorial(i+1)*f for i,f in enumerate(fv))
    cp=sum((-1)**i*(i+1)*f for i,f in enumerate(fv))
    return chi,co,cp
print("   edge Delta^1 f=(2,1):", chis([2,1]), " (chi, chi_ord, chi_pt) -- astra: 1, 0, 0")
print("   Delta^2   f=(3,3,1):", chis([3,3,1]), " -- astra: chi=1, chi_ord=3, chi_pt=0")
print("   one-edge graph Laplacian nonzero eigenvalue:",
      sorted(sp.Matrix([[1,-1],[-1,1]]).eigenvals().keys()))
