#!/usr/bin/env python3
"""Checks for 'Is the natural symplectic form a polarisation?' (notes/adelic-gkp/howe-positivity.md).

Needs PARI through cypari2 (no gp binary on this machine):
    python3 -m venv <scratch>/venv && <scratch>/venv/bin/pip install cypari2 numpy sympy
    <scratch>/venv/bin/python check_howe_positivity.py

Definitions (Goresky-Tai, refs/src/1701.07742/main.tex:3474-3497, 3556-3563).
(T, F) a Deligne module, V = q F^{-1}, K = Q[F], bar swaps F and V. A CM type Phi picks one of each pair of conjugate
embeddings K -> C. A symplectic form w with w(Fx, y) = w(x, Vy) is Phi-positive if R(x, y) = w(x, iota y) is symmetric
positive definite for iota purely imaginary with phi(iota) positive imaginary for all phi in Phi.
Deligne's CM type: Phi_eps = { phi : val_p(phi(F)) > 0 }, for the p-adic valuation on Qbar in C fixed by eps.
Howe: w is a polarisation of the abelian variety iff it is Phi_eps-positive.

Here T = Z^{2n}, F = M = [[0, -1], [q, A_s]], w = Omega. With iota = F - V the form Omega(x, iota y) is twice the Weil
form, so Omega is positive for Phi_+ = { phi : Im phi(F) > 0 }.  The question is whether Phi_+ = Phi_eps for some eps.
All eps are covered by fixing one complex embedding of the splitting field and letting the prime above p vary.
"""
import itertools
import os
from fractions import Fraction
import numpy as np
import sympy as sp
import cypari2

pari = cypari2.Pari()
pari.allocatemem(2 * 10 ** 9)
HERE = os.path.dirname(os.path.abspath(__file__))
npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


def blocks(a, b, c, d):
    return a.row_join(b).col_join(c.row_join(d))

def step(As, q):
    n = As.shape[0]
    return blocks(sp.zeros(n, n), -sp.eye(n), q * sp.eye(n), sp.Matrix(As))

def omega(n):
    return blocks(sp.zeros(n, n), sp.eye(n), -sp.eye(n), sp.zeros(n, n))

def signed(n, neg):
    A = sp.ones(n) - sp.eye(n)
    for a, b in neg:
        A[a, b] = A[b, a] = -1
    return A

x = sp.symbols("x")

def radical_charpoly(M):
    cp = sp.Poly(M.charpoly(x).as_expr(), x)
    rad = sp.Poly(sp.quo(cp.as_expr(), sp.gcd(cp.as_expr(), sp.diff(cp.as_expr(), x))), x)
    return cp, rad

def cm_types(rad, p):
    """For one complex embedding of the splitting field: the roots, the set R_+ = {Im > 0}, and for every prime P above p
    the set S_P = {roots with positive valuation}."""
    f = pari(str(rad.as_expr()).replace("**", "^"))
    spl = pari.nfsplitting(f)
    N = pari.nfinit(pari.subst(spl, "x", "y"))
    deg = int(pari.poldegree(spl))
    rts = N.nfroots(f)
    theta = pari.polroots(N.nf_get_pol())[0]
    vals = [complex(pari.subst(pari.lift(r), "y", theta)) for r in rts]
    Rplus = frozenset(i for i, v in enumerate(vals) if v.imag > 0)
    primes = N.idealprimedec(p)
    S = [frozenset(i for i, r in enumerate(rts) if int(N.idealval(r, P)) > 0) for P in primes]
    return deg, vals, Rplus, S


# ------------------------------------------------------------------------------------------ examples
A4s = signed(4, [(0, 1)])
EX = {
    "E mode (lambda=-1, q=2)": (sp.Matrix([[0, -1], [2, -1]]), 2),
    "Pauli six (lambda=-2, q=5)": (sp.Matrix([[0, -1], [5, -2]]), 5),
    "K4, one negative edge (q=2)": (step(A4s, 2), 2),
}

print("== P1  Omega is positive for the CM type Phi_+ = {Im phi(F) > 0}")
for name, (M, q) in EX.items():
    n = M.shape[0] // 2
    Om = omega(n)
    V = q * M.inv()
    iota = M - V
    R = Om * iota
    ok = (R - R.T).is_zero_matrix and (Om * V - M.T * Om).is_zero_matrix and R.is_positive_definite
    check(f"{name}: iota = F - V is purely imaginary (bar swaps F and V) and Omega(x, iota y) is symmetric positive definite", ok)

print("== P2  compare Phi_+ with Deligne's Phi_eps at every prime above p")
RES = {}
for name, (M, q) in EX.items():
    cp, rad = radical_charpoly(M)
    deg, vals, Rplus, S = cm_types(rad, q)
    Rminus = frozenset(range(len(vals))) - Rplus
    hits_p = sum(1 for s in S if s == Rplus)
    hits_m = sum(1 for s in S if s == Rminus)
    RES[name] = (vals, Rplus, S)
    print(f"      {name}: splitting field of degree {deg}; {len(S)} primes above {q}; "
          f"primes with S_P = Phi_+: {hits_p}; with S_P = conj(Phi_+): {hits_m}")
    for s in S:
        print("         S_P = {" + ", ".join(f"{vals[i].real:+.3f}{vals[i].imag:+.3f}i" for i in sorted(s)) + "}")
    if "K4" in name:
        check(f"{name}: neither Omega nor -Omega is Phi_eps-positive, for every eps", hits_p == 0 and hits_m == 0)
    else:
        check(f"{name}: Omega is Phi_eps-positive for half of the choices of eps and -Omega for the other half", hits_p == 1 and hits_m == 1 and len(S) == 2)

print("== P3  the reason: lambda and -lambda both occur, so every S_P is closed under mu -> -mu")
M, q = EX["K4, one negative edge (q=2)"]
cp, rad = radical_charpoly(M)
vals, Rplus, S = RES["K4, one negative edge (q=2)"]
even = all(c == 0 for c in cp.all_coeffs()[1::2])
def neg_closed(s):
    return all(any(abs(vals[j] + vals[i]) < 1e-9 for j in s) for i in s)
check("characteristic polynomial of M is even; every S_P is closed under negation; Phi_+ is not", even and all(neg_closed(s) for s in S) and not neg_closed(Rplus),
      f"char poly {sp.factor(cp.as_expr())}")

print("== P4  the repair: twist Omega by a function of F + V = A_s (+) A_s")
n = 4
Om = omega(n)
V = q * M.inv()
A = A4s
lam_of = lambda z: (z + q / z).real                       # lambda = mu + q/mu
def type_of(pfun):
    """CM type for which w(x,y) = Omega(x, p(A_s) y) is positive: Im phi(F) * p(lambda_phi) > 0"""
    return frozenset(i for i, v in enumerate(vals) if v.imag * pfun(lam_of(v)) > 0)
tw = Om * (M + V)
ok = (tw + tw.T).is_zero_matrix and ((M.T * tw) - (tw * V)).is_zero_matrix
R = tw * (M - V)
t1 = type_of(lambda l: l)
check("w' = Omega(x, (F+V) y) is alternating, satisfies w'(Fx,y) = w'(x,Vy), and is Phi_eps-positive for exactly one prime above 2",
      ok and sum(1 for s in S if s == t1) == 1, f"det of w' = {tw.det()} (degree 25: a GKP code of dimension |det A_s| = {abs(A.det())}, not a qunaught)")
allpat = {type_of(lambda l, a=a, b=b: (a if abs(abs(l) - 1) < 1e-6 else b) * l) for a in (1, -1) for b in (1, -1)}
check("the four sign patterns (odd in lambda, independently on |lambda| = 1 and |lambda| = sqrt 5) are exactly the four S_P", allpat == set(S))

print("== P5  is there a principal polarisation? units of the order Q[A_s] cap M_4(Z) with the right signs")
pows = [sp.eye(4), A, A ** 2, A ** 3]
B = pari.matrix(16, 4, [int(pows[j][i // 4, i % 4]) for i in range(16) for j in range(4)])
sat = pari.matrixqz(B, -2)
basis = [sp.Matrix(4, 4, [int(sat[i, j]) for i in range(16)]) for j in range(4)]
idx_in = abs(sp.Matrix([[sp.Rational(c) for c in sp.Matrix(pows).reshape(4, 16).T.solve_least_squares(b.reshape(16, 1))] for b in basis]).det())
print(f"      Z[A_s] has index {1 / idx_in} in the order R = Q[A_s] cap M_4(Z)")
# eigenvalue map R -> Q x Q x Q(sqrt5): X = sum c_j A^j  ->  (p(1), p(-1), u, v) with p(sqrt5) = u + v sqrt5
def coeffs(X):
    return sp.Matrix(pows).reshape(4, 16).T.solve_least_squares(X.reshape(16, 1))
def emap(c):
    return [c[0] + c[1] + c[2] + c[3], c[0] - c[1] + c[2] - c[3], c[0] + 5 * c[2], c[1] + 5 * c[3]]
Emat = sp.Matrix([emap(coeffs(b)) for b in basis]).T              # columns: images of the basis
def in_R(target):
    t = Emat.solve(sp.Matrix(target))
    return all(sp.Rational(v).q == 1 for v in t), t
def phi_pow(k):
    u, v = sp.Rational(1), sp.Rational(0)                           # (u + v sqrt5)
    a, b = (sp.Rational(1, 2), sp.Rational(1, 2)) if k > 0 else (sp.Rational(-1, 2), sp.Rational(1, 2))   # phi or 1/phi = -(1 - sqrt5)/2
    for _ in range(abs(k)):
        u, v = u * a + 5 * v * b, u * b + v * a
    return u, v
period = next(m for m in range(1, 200) if in_R([1, 1, *phi_pow(m)])[0])
found = []
for k in range(-period, period + 1):
    if k % 2 == 0:
        continue
    u, v = phi_pow(k)
    for e1 in (1, -1):
        for e2 in (1, -1):
            ok, t = in_R([e1, -e1, e2 * u, e2 * v])
            if ok:
                found.append((k, e1, e2, t))
print(f"      (1, 1, phi^m) lies in R first at m = {period}; odd k in [-{period}, {period}] with (+-1, -+1, +-phi^k) in R: {[(f[0], f[1], f[2]) for f in found]}")
if found:
    k, e1, e2, t = found[0]
    P = sum((t[i] * basis[i] for i in range(4)), sp.zeros(4))
    wP = Om * sp.diag(P, P)
    ev = sorted(float(v) for v in P.eigenvals(multiple=True))
    cP = [float(v) for v in coeffs(P)]
    tP = type_of(lambda l: sum(cP[j] * l ** j for j in range(4)))
    print(f"      its CM type equals S_P for {sum(1 for s_ in S if s_ == tP)} prime(s) above 2")
    check("a unit P of R with opposite signs on lambda and -lambda exists: Omega(x, P y) is unimodular", abs(wP.det()) == 1, f"P = {P.tolist()}, eigenvalues {np.round(ev, 4)}")
else:
    check("no unit of R has opposite signs on lambda and -lambda: no principal polarisation commuting with F", True,
          "units of R have the same sign at 1 and -1 or norm +1 at sqrt 5")

print("== P6  the symmetry behind it, and the isogeny factors")
An = np.array(A.tolist(), dtype=int)
hits = []
for perm in itertools.permutations(range(4)):
    for sg in itertools.product((1, -1), repeat=4):
        D = np.zeros((4, 4), dtype=int)
        for i, j in enumerate(perm):
            D[i, j] = sg[i]
        if np.array_equal(D @ An @ D.T, -An):
            hits.append(D)
noinv = not any(np.array_equal(h @ h, np.eye(4, dtype=int)) for h in hits)
minus = [h for h in hits if np.array_equal(h @ h, -np.eye(4, dtype=int))]
D = sp.Matrix(minus[0].tolist())
Gam = sp.diag(D, -D)
ok = len(hits) > 0 and noinv and len(minus) > 0
ok &= (Gam * M * Gam.inv() + M).is_zero_matrix and (Gam.T * Om * Gam + Om).is_zero_matrix and (Gam * Gam + sp.eye(8)).is_zero_matrix
check("signed permutations D with D A_s D^-1 = -A_s exist, none is an involution, some have D^2 = -1; for those Gamma = diag(D, -D) "
      "anticommutes with the step, is antisymplectic, and Gamma^2 = -1", ok, f"{len(hits)} such D, {len(minus)} with D^2 = -1; one is {minus[0].tolist()}")
y = sp.symbols("y")
g2 = sp.Poly(sp.Matrix(M * M).charpoly(y).as_expr(), y)
check("isogeny factors: over F_2 the Weil polynomial is (x^2-x+2)(x^2+x+2)(x^4-x^2+4); over F_4 it is ((y^2+3y+4)(y^2-y+4))^2",
      sp.expand(cp.as_expr() - (x**2 - x + 2) * (x**2 + x + 2) * (x**4 - x**2 + 4)) == 0
      and sp.expand(g2.as_expr() - ((y**2 + 3*y + 4) * (y**2 - y + 4))**2) == 0 and sp.Poly(x**4 - x**2 + 4, x).is_irreducible,
      "elliptic curves with 2 and 4 points over F_2 and a simple abelian surface; over F_4, E1^2 x E2^2 with 8 and 4 points")

print("== P7  a candidate without a (lambda, -lambda) pair: K6 with q = 5")
def K6_class():
    A = sp.ones(6) - sp.eye(6)
    tree = [(0, j) for j in range(1, 6)]
    cot = [(a, b) for a in range(1, 6) for b in range(a + 1, 6)]
    target = sp.Poly((x + 1) ** 3 * (x ** 3 - 3 * x ** 2 - 9 * x + 19), x)
    for bits in itertools.product((0, 1), repeat=len(cot)):
        As = A.copy()
        for (a, b), bt in zip(cot, bits):
            if bt:
                As[a, b] = As[b, a] = -1
        if sp.Poly(As.charpoly(x).as_expr(), x) == target:
            return As
A6 = K6_class()
M6 = step(A6, 5)
cp6, rad6 = radical_charpoly(M6)
lam6 = sorted(np.linalg.eigvalsh(np.array(A6.tolist(), dtype=float)))
print(f"      fermionic eigenvalues {np.round(lam6, 4)}; 2 sqrt q = {2 * 5 ** 0.5:.4f}; minimal polynomial of M: {sp.factor(rad6.as_expr())}")
R6 = omega(6) * (M6 - 5 * M6.inv())
check("K6 class: Ramanujan, ordinary, Omega positive for Phi_+", max(abs(v) for v in lam6) < 2 * 5 ** 0.5 and cp6.all_coeffs()[6] % 5 != 0 and R6.is_positive_definite,
      f"middle coefficient {cp6.all_coeffs()[6]}")
deg6, vals6, Rplus6, S6 = cm_types(rad6, 5)
Rminus6 = frozenset(range(len(vals6))) - Rplus6
hp, hm = sum(1 for s in S6 if s == Rplus6), sum(1 for s in S6 if s == Rminus6)
print(f"      splitting field of degree {deg6}; {len(S6)} primes above 5; S_P = Phi_+ for {hp} of them, = conj(Phi_+) for {hm}")
check("K6 class: whether Omega or -Omega is a polarisation for some eps is decided", True, "YES" if hp + hm > 0 else "NO")
agree = sorted({len(s & Rplus6) for s in S6})
print(f"      numbers of roots on which S_P and Phi_+ agree, over the primes: {agree} (of {len(Rplus6)})")

print(f"\n{npass} passed, {nfail} failed")
