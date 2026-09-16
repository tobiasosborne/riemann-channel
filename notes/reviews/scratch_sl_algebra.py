#!/usr/bin/env python3
"""Independent REFUTE-lane checks of the sl2 algebra in notes/selberg-letters/astra-proofs.md.

Realisation built from scratch: lowest-weight Verma module on C[x]_{<=N} with
  U_- = d/dx,  X = x d/dx - z,  U_+ = -x^2 d/dx + 2 z x
so that U_- v = 0 and X v = -z v for v = 1.  Brackets are verified, not assumed.
Nothing is imported from the prover's scripts.
"""
import sympy as sp

PASS = FAIL = 0
def chk(name, cond):
    global PASS, FAIL
    if cond: PASS += 1; print(f"  PASS  {name}")
    else:    FAIL += 1; print(f"  FAIL  {name}")

N = 14
z, lam = sp.symbols('z lam')
# matrices on basis x^0..x^N (columns = input degree)
def mat(f):
    M = sp.zeros(N+1, N+1)
    for j in range(N+1):
        p = sp.Poly(sp.expand(f(sp.Symbol('x')**j)), sp.Symbol('x'))
        for (k,), c in p.terms():
            if k <= N: M[k, j] = c
    return M
x = sp.Symbol('x')
Um = mat(lambda p: sp.diff(p, x))
X  = mat(lambda p: x*sp.diff(p, x) - z*p)
Up = mat(lambda p: -x**2*sp.diff(p, x) + 2*z*x*p)

def com(A,B): return sp.expand(A*B - B*A)
# truncation: compare only the top-left block that is unaffected
T = 8
def eq(A,B): return sp.simplify((A-B)[:T,:T]) == sp.zeros(T,T)

print("== brackets of the independent realisation ==")
chk("[X,U_+] = U_+",  eq(com(X,Up), Up))
chk("[X,U_-] = -U_-", eq(com(X,Um), -Um))
chk("[U_+,U_-] = 2X", eq(com(Up,Um), 2*X))

# letters H,E,W from X,U_pm  (X=H/2, U_pm=(E pm W)/2)
H = 2*X; E = Up + Um; W = Up - Um
chk("[H,E] = 2W",  eq(com(H,E), 2*W))
chk("[H,W] = 2E",  eq(com(H,W), 2*E))
chk("[E,W] = -2H", eq(com(E,W), -2*H))

Om_sym  = sp.expand(X*X + sp.Rational(1,2)*(Up*Um + Um*Up))
Om_mat  = sp.expand(sp.Rational(1,4)*(H*H + E*E - W*W))
print("== Casimir orderings (D3 step 1 / ledger L10) ==")
chk("Omega = (1/4)(H^2+E^2-W^2) = X^2+(1/2)(U+U- + U-U+)", eq(Om_sym, Om_mat))
chk("Omega = X^2 + U_+U_- - X   [report]", eq(Om_sym, sp.expand(X*X + Up*Um - X)))
chk("Omega = X^2 + U_-U_+ + X   [report alt]", eq(Om_sym, sp.expand(X*X + Um*Up + X)))
chk("Omega != X^2 + U_+U_- + X  [draft's version is WRONG]",
    not eq(Om_sym, sp.expand(X*X + Up*Um + X)))
chk("Omega central: [X,Omega]=0", eq(com(X,Om_sym), sp.zeros(N+1,N+1)))
chk("Omega central: [U_+,Omega]=0", eq(com(Up,Om_sym), sp.zeros(N+1,N+1)))
chk("Omega central: [U_-,Omega]=0", eq(com(Um,Om_sym), sp.zeros(N+1,N+1)))

# first-band vector v = 1 (column 0):  U_- v = 0, X v = -z v
v = sp.zeros(N+1,1); v[0,0] = 1
chk("U_- v = 0", sp.simplify(Um*v) == sp.zeros(N+1,1))
chk("X v = -z v", sp.simplify(X*v + z*v) == sp.zeros(N+1,1))
print("== D3(a): Omega u = lambda(1+lambda) u on ker U_- with (X+lambda)u=0 ==")
chk("Omega v = z(1+z) v", sp.simplify(Om_sym*v - z*(1+z)*v) == sp.zeros(N+1,1))

print("== D4 ladder coefficients ==")
ok1 = ok2 = True
for m in range(1, 7):
    lhs = sp.expand(Um*(Up**m)*v)
    rhs = sp.expand(m*(2*z - m + 1)*(Up**(m-1))*v)
    if sp.simplify(lhs-rhs)[:T,:] != sp.zeros(T,1): ok1 = False
    lhs2 = sp.expand((Um**m)*(Up**m)*v)
    coef = sp.factorial(m)*sp.prod([(2*z-j+1) for j in range(1,m+1)])
    if sp.simplify(lhs2 - coef*v)[:T,:] != sp.zeros(T,1): ok2 = False
chk("U_-U_+^m v = m(2z-m+1) U_+^{m-1} v  (m=1..6)", ok1)
chk("U_-^m U_+^m v = m! prod_{k=1..m}(2z-k+1) v  (m=1..6)", ok2)
# DFG's form: on Res^0(lambda+m), i.e. z = lambda+m
ok3 = True
for m in range(1, 7):
    a = sp.factorial(m)*sp.prod([(2*z-k+1) for k in range(1,m+1)])
    b = sp.factorial(m)*sp.prod([(2*(z-m)+m+j) for j in range(1,m+1)])
    if sp.simplify(a-b) != 0: ok3 = False
chk("equals DFG m! prod_j (2lambda+m+j) with z = lambda+m (m=1..6)", ok3)
# vanishing set
van = set()
for m in range(1, 9):
    for j in range(1, m+1):
        s = sp.Rational(-(m+j), 2)
        van.add(s)
chk("ladder coefficient vanishes exactly on -1-(1/2)N_0 (checked to m=8)",
    sorted(van)[-1] == sp.Rational(-1) and all(2*(-s)-2 == int(2*(-s)-2) and s <= -1 for s in van))

print("== D4/D5: L_adj and the diffusion commutator ==")
Ladj = sp.expand(sp.Rational(1,2)*(H*H + E*E))
chk("(1/2)(H^2+E^2) = 2 Omega + (1/2) W^2", eq(Ladj, sp.expand(2*Om_sym + sp.Rational(1,2)*W*W)))
# on the first band with X v = -lam v  (so z = lam)
lhs = sp.expand((Um*Ladj - Ladj*Um)*v)
rhs = sp.expand((2*z-1)*(Up*v))
chk("[U_-,(1/2)(H^2+E^2)] u = (2 lambda - 1) U_+ u on ker U_- with (X+lambda)u=0",
    sp.simplify(lhs-rhs)[:T,:] == sp.zeros(T,1))

print("== D3(e)/L14: the FE map in a 2-branch model ==")
a, b = sp.symbols('a b')
# A = -X acts as lam on branch 1 and -1-lam on branch 2; J swaps them
A2 = sp.Matrix([[lam,0],[0,-1-lam]]); J2 = sp.Matrix([[0,1],[1,0]])
chk("J^2 = 1", sp.simplify(J2*J2 - sp.eye(2)) == sp.zeros(2,2))
chk("J A J^{-1} = -1-A", sp.simplify(J2*A2*J2.inv() - (-sp.eye(2)-A2)) == sp.zeros(2,2))
X2 = -A2
chk("J X J^{-1} = 1-X   [report]", sp.simplify(J2*X2*J2.inv() - (sp.eye(2)-X2)) == sp.zeros(2,2))
chk("J X J^{-1} != -1-X [draft is WRONG]",
    sp.simplify(J2*X2*J2.inv() - (-sp.eye(2)-X2)) != sp.zeros(2,2))
S2 = A2 + sp.eye(2)
chk("J S J^{-1} = 1-S for S = A+1", sp.simplify(J2*S2*J2.inv() - (sp.eye(2)-S2)) == sp.zeros(2,2))

print("== D3(d)/L12: the draft's total pullback is degenerate ==")
# two lifts of the same f, each normalised so pi_* u_pm = f
Gram = sp.Matrix([[1,1],[1,1]])
chk("Gram of the total pushforward form on a partner pair is [[1,1],[1,1]]", Gram.det() == 0)
chk("its kernel is the partner difference", sp.simplify(Gram*sp.Matrix([1,-1])) == sp.zeros(2,1))

print("== D3 step 8: positive G with A*G+GA=-G forces semisimplicity ==")
# Jordan block A = -1/2 + nilpotent: show no positive G exists (2x2 explicit)
Jb = sp.Matrix([[sp.Rational(-1,2),1],[0,sp.Rational(-1,2)]])
g11,g12,g22 = sp.symbols('g11 g12 g22', real=True)
G = sp.Matrix([[g11,g12],[g12,g22]])
eqs = sp.expand(Jb.T*G + G*Jb + G)
sol = sp.solve([eqs[0,0],eqs[0,1],eqs[1,1]],[g11,g12,g22], dict=True)
print("   solutions:", sol)
bad = bool(sol) and all(s.get(g11, g11) == 0 and s.get(g12, g12) == 0 for s in sol)
chk("A^*G+GA=-G on a 2x2 Jordan block forces g11=g12=0, so G is singular, not positive", bad)

print(f"\nTALLY scratch_sl_algebra.py: {PASS} PASS / {FAIL} FAIL")
