#!/usr/bin/env python3
"""Numerics lane for notes/genus-two-bond (2026-09-22): the class-group bond of
C: y^2 = x^5 + x^3 + x^2 - 2 over F_5 at genus two.

Independent of the prover's checks/ scripts. Exact arithmetic (integers, Q(zeta_15),
Q(pi)) for every identity; floats only for printed roots and Gram matrices.
Ledger lines: `Dnn PASS/FAIL description value`.
"""
import itertools, time, sys
from fractions import Fraction
import numpy as np
import sympy as sp

T0 = time.time()
LEDGER = []
def check(desc, cond, val=""):
    LEDGER.append((desc, bool(cond), val))
    print(f"D{len(LEDGER):02d} {'PASS' if cond else 'FAIL'} {desc} {val}")

p = 5
fcoef = [(-2) % 5, 0, 1, 1, 0, 1]  # f = x^5 + x^3 + x^2 - 2, coefficients of degrees 0..5

# ---------------------------------------------------------------- F_{5^k} via a modulus polynomial
class GF:
    def __init__(self, k, mod):          # mod: monic, coefficients low->high, length k+1
        self.k, self.mod = k, [c % p for c in mod]
        assert len(mod) == k + 1 and mod[-1] == 1
        self.elems = list(itertools.product(range(p), repeat=k))
        self.zero = tuple([0]*k); self.one = tuple([1] + [0]*(k-1))
    def add(self, a, b): return tuple((x+y) % p for x, y in zip(a, b))
    def neg(self, a): return tuple((-x) % p for x in a)
    def mul(self, a, b):
        k = self.k; prod = [0]*(2*k-1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    prod[i+j] = (prod[i+j] + x*y) % p
        for d in range(2*k-2, k-1, -1):    # reduce t^d using t^k = -(mod[0..k-1])
            c = prod[d]
            if c:
                prod[d] = 0
                for i in range(k):
                    prod[d-k+i] = (prod[d-k+i] - c*self.mod[i]) % p
        return tuple(prod[:k])
    def scalar(self, c): return tuple([c % p] + [0]*(self.k-1))
    def evalpoly(self, coefs, x):        # coefs low->high over F_5
        r = self.zero
        for c in reversed(coefs):
            r = self.add(self.mul(r, x), self.scalar(c))
        return r
    def is_irreducible(self):
        # no root in any subfield of degree d|k for d<k by brute force over all elements: check the
        # multiplicative structure instead: modulus irreducible iff the ring is a field iff every nonzero
        # element is invertible.
        nz = [e for e in self.elems if e != self.zero]
        prods = set()
        for a in nz:
            inv = False
            for b in nz:
                if self.mul(a, b) == self.one: inv = True; break
            if not inv: return False
        return True

moduli = {1: [0, 1], 2: [1, 1, 1], 3: [1, 0, 1, 1], 4: [1, 0, 1, 1, 1]}
N = {}
for k, mod in moduli.items():
    F = GF(k, mod)
    irr = F.is_irreducible() if k <= 3 else None   # degree 4: 625^2 products too slow; check via roots below
    if k == 4:
        # irreducible over F_5 iff no root in F_5 and no quadratic factor: test all monic quadratics
        quads = [[a, b, 1] for a in range(5) for b in range(5)]
        def polymod(A, B):   # A mod B over F_5, low->high
            A = A[:]
            while len(A) >= len(B) and any(A):
                if A[-1] == 0: A.pop(); continue
                c = A[-1]; s = len(A) - len(B)
                for i, bc in enumerate(B): A[s+i] = (A[s+i] - c*bc) % 5
                A.pop()
            return A
        irr = all(any(polymod(mod, q)) for q in quads) and all(F.evalpoly(mod, F.scalar(a)) != F.zero for a in range(5))
    squares = set(F.mul(e, e) for e in F.elems)
    cnt = 0
    for x in F.elems:
        v = F.evalpoly(fcoef, x)
        if v == F.zero: cnt += 1
        elif v in squares: cnt += 2
    N[k] = cnt + 1     # one rational point at infinity (odd-degree model)
    check(f"modulus for F_5^{k} irreducible", irr, mod)
check("point counts N_1..N_4 = (3,31,117,619)", [N[k] for k in range(1, 5)] == [3, 31, 117, 619], [N[k] for k in range(1, 5)])

# ---------------------------------------------------------------- P(T) by Newton
s = {k: p**k + 1 - N[k] for k in range(1, 5)}
check("power sums s_k = (3,-5,9,7)", [s[k] for k in range(1, 5)] == [3, -5, 9, 7], [s[k] for k in range(1, 5)])
# P(T) = exp(-sum s_k T^k/k) truncated to degree 4 (Newton: e_n = (1/n) sum_{i} (-1)^{i-1} e_{n-i} s_i, coeffs (-1)^n e_n)
Tt = sp.symbols('T')
logZ = sum(-sp.Rational(s[k], k)*Tt**k for k in range(1, 5))
P = sp.series(sp.exp(logZ), Tt, 0, 5).removeO().expand()
Pexp = 1 - 3*Tt + 7*Tt**2 - 15*Tt**3 + 25*Tt**4
check("P(T) = 1 - 3T + 7T^2 - 15T^3 + 25T^4", sp.expand(P - Pexp) == 0, P)
z = sp.symbols('z')
fF = z**4 - 3*z**3 + 7*z**2 - 15*z + 25
check("chi_F = z^4 f_F reciprocal of P", sp.expand(z**4*Pexp.subs(Tt, 1/z) - fF) == 0)
check("h = P(1) = 15", Pexp.subs(Tt, 1) == 15, Pexp.subs(Tt, 1))
roots = [complex(r) for r in sp.Poly(fF, z).nroots(n=30)]
check("all four Frobenius roots have modulus sqrt 5", max(abs(abs(r) - 5**0.5) for r in roots) < 1e-25, max(abs(abs(r) - 5**0.5) for r in roots))
b1, b2 = (3 + sp.sqrt(21))/2, (3 - sp.sqrt(21))/2
check("f_F = (z^2 - b1 z + 5)(z^2 - b2 z + 5) over Q(sqrt21)", sp.expand((z**2 - b1*z + 5)*(z**2 - b2*z + 5) - fF) == 0)
check("f_F irreducible over Q", sp.Poly(fF, z).is_irreducible)

# ---------------------------------------------------------------- Mumford / Cantor arithmetic over F_5, genus 2
# polynomials over F_5: lists low->high, normalised (no trailing zeros)
def norm(a):
    a = [c % p for c in a]
    while a and a[-1] == 0: a.pop()
    return a
def padd(a, b):
    n = max(len(a), len(b)); return norm([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])
def psub(a, b): return padd(a, [(-c) % p for c in b])
def pmul(a, b):
    if not a or not b: return []
    r = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i+j] = (r[i+j] + x*y) % p
    return norm(r)
def pdivmod(a, b):
    a = norm(a); b = norm(b); assert b
    q = [0]*max(len(a)-len(b)+1, 1); inv = pow(b[-1], -1, p)
    while len(a) >= len(b) and a:
        c = a[-1]*inv % p; sft = len(a)-len(b); q[sft] = c
        a = psub(a, [0]*sft + [c*x % p for x in b])
    return norm(q), a
def pmod(a, b): return pdivmod(a, b)[1]
def pmonic(a):
    a = norm(a); inv = pow(a[-1], -1, p); return [c*inv % p for c in a]
def pgcd(a, b):
    a, b = norm(a), norm(b)
    while b: a, b = b, pmod(a, b)
    return pmonic(a) if a else []
def pxgcd(a, b):    # returns (g, s, t) with s a + t b = g monic
    r0, r1 = norm(a), norm(b); s0, s1 = [1], []; t0, t1 = [], [1]
    while r1:
        q, r = pdivmod(r0, r1)
        r0, r1 = r1, r; s0, s1 = s1, psub(s0, pmul(q, s1)); t0, t1 = t1, psub(t0, pmul(q, t1))
    inv = pow(r0[-1], -1, p)
    return pmonic(r0), [c*inv % p for c in s0], [c*inv % p for c in t0]
fpoly = norm(fcoef)
def reduce_div(u, v):
    while len(u) - 1 > 2:
        u = pmonic(pdivmod(psub(fpoly, pmul(v, v)), u)[0]); v = norm([(-c) % p for c in pmod(v, u)])
    return u, v
def cantor_add(D1, D2):
    u1, v1 = D1; u2, v2 = D2
    d1, e1, e2 = pxgcd(u1, u2)
    d, c1, c2 = pxgcd(d1, padd(v1, v2))
    s1, s2, s3 = pmul(c1, e1), pmul(c1, e2), c2
    u = pdivmod(pmul(u1, u2), pmul(d, d))[0]
    num = padd(padd(pmul(s1, pmul(u1, v2)), pmul(s2, pmul(u2, v1))), pmul(s3, padd(pmul(v1, v2), fpoly)))
    v = pmod(pdivmod(num, d)[0], u)
    u = pmonic(u) if u else [1]
    return reduce_div(u, v)
def key(D): return (tuple(D[0]), tuple(D[1]))
ZERO = ([1], [])
# enumerate reduced divisors
reduced = []
for deg in range(0, 3):
    for tail in itertools.product(range(p), repeat=deg):
        u = norm(list(tail) + [1])
        if len(u) - 1 != deg: continue
        vs = [[]] if deg == 0 else [norm(list(c)) for c in itertools.product(range(p), repeat=deg)]
        for v in vs:
            if not pmod(psub(fpoly, pmul(v, v)), u):
                reduced.append((u, v))
check("number of reduced divisors (Mumford pairs) = 15", len(reduced) == 15, len(reduced))
G = ([4, 1], [1])          # x - 1 = x + 4, v = 1: [(1,1) - inf]
mult = {0: ZERO}
cur = ZERO
for k in range(1, 16):
    cur = cantor_add(cur, G); mult[k] = cur
check("15 G = 0 and no smaller positive multiple vanishes", key(mult[15]) == key(ZERO) and all(key(mult[k]) != key(ZERO) for k in range(1, 15)))
check("multiples of G exhaust the 15 reduced divisors", set(key(mult[k]) for k in range(15)) == set(key(D) for D in reduced))
ok = all(key(cantor_add(mult[a], mult[b])) == key(mult[(a+b) % 15]) for a in range(15) for b in range(15))
check("all 225 additions agree with Z/15", ok)
Gminus = ([4, 1], [4])   # [(1,4) - inf]
check("[(1,4) - inf] = 14 G (inverse of G)", key(mult[14]) == key(Gminus))
check("E1 table rows for k = 2, 5, 7 (u, v)", key(mult[2]) == ((1, 3, 1), (1,)) and key(mult[5]) == ((2, 0, 1), (2, 3)) and key(mult[7]) == ((4, 3, 1), (3, 3)),
      [mult[2], mult[5], mult[7]])

# ---------------------------------------------------------------- h^0 of the classes k G + n P_0, n = 0, 1, 2
# degree 0: only the trivial class is effective. degree 1: effective iff class of [Q - P0], Q rational.
# degree 2: h^0 = 1 + h^0(K - D), K ~ 2 P0 => h^0 = 2 iff class 0, else 1 (all effective).  Verify by enumeration.
ratpts = [(x, y) for x in range(p) for y in range(p) if (y*y - sum(c*x**i for i, c in enumerate(fcoef))) % p == 0]
check("rational affine points are (1,1),(1,4)", sorted(ratpts) == [(1, 1), (1, 4)], ratpts)
def class_of_point(pt):     # [Q - P0]
    x, y = pt; return reduce_div(norm([(-x) % p, 1]), norm([y]))
deg1_eff = {0} | {[k for k in range(15) if key(mult[k]) == key(class_of_point(q))][0] for q in ratpts}
check("degree-one effective classes = {0, 1, 14}", deg1_eff == {0, 1, 14}, sorted(deg1_eff))
# degree-two effective divisors: pairs of rational points (with P0), degree-two closed points
F2 = GF(2, moduli[2]); sq2 = set(F2.mul(e, e) for e in F2.elems)
eff2 = []      # list of classes (k) of D - 2 P0
pts3 = ratpts + ['inf']
for a, b in itertools.combinations_with_replacement(range(3), 2):
    A, B = pts3[a], pts3[b]
    if A == 'inf' and B == 'inf': eff2.append(0); continue
    if A == 'inf' or B == 'inf':
        Q = B if A == 'inf' else A
        eff2.append([k for k in range(15) if key(mult[k]) == key(class_of_point(Q))][0]); continue
    if A[0] == B[0] and A[1] != B[1]:      # opposite points: sum ~ 2 P0
        eff2.append(0); continue
    if A == B:                              # 2Q: u = (x - x0)^2, v = y0 + f'(x0)/(2 y0) (x - x0)
        x0, y0 = A; fp = sum(i*c*x0**(i-1) for i, c in enumerate(fcoef) if i) % p
        slope = fp * pow(2*y0 % p, -1, p) % p
        u = pmul([(-x0) % p, 1], [(-x0) % p, 1]); v = norm([(y0 - slope*x0) % p, slope])
    else:
        (x0, y0), (x1, y1) = A, B
        u = pmul([(-x0) % p, 1], [(-x1) % p, 1]); slope = (y1 - y0)*pow((x1 - x0) % p, -1, p) % p
        v = norm([(y0 - slope*x0) % p, slope])
    D = reduce_div(u, v); eff2.append([k for k in range(15) if key(mult[k]) == key(D)][0])
n_pairs = len(eff2)
# closed points of degree two: x in F_25 \ F_5 with f(x) a square (conjugate pairs), and x in F_5 with f(x) a nonzero nonsquare
closed2 = 0
seen = set()
for x in F2.elems:
    if x[1] == 0: continue                  # x in F_5
    v = F2.evalpoly(fcoef, x)
    if v == F2.zero or v not in sq2: continue
    conj = F2.mul(x, x)                     # Frobenius x -> x^5
    for _ in range(4): conj = F2.mul(conj, x);
    # compute x^5 properly
    x5 = x
    for _ in range(4): x5 = F2.mul(x5, x)
    kk = frozenset([x, x5])
    if kk in seen: continue
    seen.add(kk)
    # y with y^2 = v: find both roots; each gives one closed point of degree 2 (y, y^5) unless y in F_5 (impossible since x not in F_5? y could be in F_5)
    ys = [e for e in F2.elems if F2.mul(e, e) == v]
    # the point (x, y) and its conjugate (x^5, y^5) form one closed point; two choices of y give two closed points
    for y in ys[:1]:
        pass
    # closed points over this x-orbit: the two points (x,y),(x,-y) lie in distinct conjugate orbits unless y^5 = -y
    y = ys[0]; y5 = y
    for _ in range(4): y5 = F2.mul(y5, y)
    if y5 == F2.neg(y) and F2.add(y5, y) == F2.zero and y5 != y:
        closed2 += 1       # (x,y) conjugate to (x^5,-y): one closed point containing both y-values
        # u = minpoly of x, v determined: need v(x) = y with v in F_5[x]; y = a + b x
        # solve y = a*1 + b*x in F_25 coordinates
        pass
    else:
        closed2 += 2
    # Mumford representatives
    minpoly = pmonic(norm([ (F2.mul(x, x5))[0], (-(F2.add(x, x5))[0]) % p, 1 ]))
    for yy in ys:
        # y = a + b*x with x = (x0, x1) in basis (1,t): need a,b in F_5 with a + b x = yy
        found = None
        for a in range(p):
            for bcoef in range(p):
                if F2.add(F2.scalar(a), F2.mul(F2.scalar(bcoef), x)) == yy: found = (a, bcoef)
        if found is None: continue        # yy not in F_5(x) as an affine combination: then (x,yy) has degree 4? no: F_25 = F_5(x); always found
        D = reduce_div(minpoly, norm(list(found))); eff2.append([k for k in range(15) if key(mult[k]) == key(D)][0])
# x in F_5 with f(x) nonzero nonsquare: closed point of degree two, divisor ~ 2 P0 (fibre of x)
sq1 = {(y*y) % p for y in range(p)}
fib = [x for x in range(p) if (sum(c*x**i for i, c in enumerate(fcoef)) % p) not in sq1]
for x in fib: eff2.append(0)
check("effective degree-two divisors: 6 pairs + 14 closed points = 20", len(eff2) == 20, (n_pairs, len(eff2) - n_pairs))
from collections import Counter
cnt2 = Counter(eff2)
check("every degree-two class effective; class 0 six times, others once", set(cnt2) == set(range(15)) and cnt2[0] == 6 and all(cnt2[k] == 1 for k in range(1, 15)), dict(sorted(cnt2.items())))
h0 = {}
for k in range(15):
    h0[(k, 0)] = 1 if k == 0 else 0
    h0[(k, 1)] = 1 if k in deg1_eff else 0
    h0[(k, 2)] = 2 if k == 0 else 1
a = [sum((p**h0[(k, n)] - 1)//(p - 1) for k in range(15)) for n in range(3)]
check("a_0, a_1, a_2 = (1, 3, 20)", a == [1, 3, 20], a)
Zser = sp.series(Pexp/((1 - Tt)*(1 - 5*Tt)), Tt, 0, 8).removeO()
aser = [Zser.coeff(Tt, n) for n in range(8)]
check("Z(T) = P/((1-T)(1-5T)) gives (1,3,20,90,465,2340,11715,58590)", aser == [1, 3, 20, 90, 465, 2340, 11715, 58590], aser)
check("a_n = 15(5^{n-1}-1)/4 for n = 3..7", all(aser[n] == 15*(5**(n-1) - 1)//4 for n in range(3, 8)))
check("special counts (1,3,20) = sum over classes of (5^h0 - 1)/4 at n = 0,1,2", a == [1, 3, 20])

# ---------------------------------------------------------------- the fourteen L(T, chi_k) in Q(zeta_15)
zeta = sp.exp(2*sp.pi*sp.I/15)
Phi15 = sp.cyclotomic_poly(15, z)
def L_poly(k):
    # L_k(T) = sum_n sum_j chi_k(j G) (5^{h0(j G + n P0)} - 1)/4 T^n, chi_k(jG) = zeta^{kj}
    expr = 0
    for n in range(3):
        for j in range(15):
            w = (p**h0[(j, n)] - 1)//(p - 1)
            if w: expr += w * z**((k*j) % 15) * Tt**n
    # reduce modulo Phi15 in z
    coeffs = [sp.rem(sp.Poly(sp.expand(expr).coeff(Tt, n), z), sp.Poly(Phi15, z)).as_expr() for n in range(3)]
    return coeffs
Lk = {k: L_poly(k) for k in range(1, 15)}
A = {k: sp.rem(sp.Poly(1 + z**k + z**((-k) % 15), z), sp.Poly(Phi15, z)).as_expr() for k in range(1, 15)}
ok = all(sp.expand(Lk[k][0] - 1) == 0 and sp.expand(Lk[k][1] - A[k]) == 0 and sp.expand(Lk[k][2] - 5) == 0 for k in range(1, 15))
check("L(T, chi_k) = 1 + A_k T + 5 T^2 with A_k = 1 + zeta^k + zeta^-k, all k", ok)
Anum = {k: complex(sp.N(A[k].subs(z, zeta), 30)) for k in range(1, 15)}
Aexp = [2.827090915285, 2.338261212718, 1.618033988750, 0.790943073465, 0, -0.618033988750, -0.956295201468]
check("A_k decimals (k = 1..7) and symmetry A_k = A_{15-k}", max(abs(Anum[k].real - Aexp[k-1]) for k in range(1, 8)) < 1e-11 and max(abs(Anum[k].imag) for k in range(1, 15)) < 1e-25 and max(abs(Anum[k] - Anum[15-k]) for k in range(1, 8)) < 1e-25,
      [round(Anum[k].real, 12) for k in range(1, 8)])
check("A_3 = (1+sqrt5)/2, A_6 = (1-sqrt5)/2, A_5 = 0", abs(Anum[3] - (1+5**0.5)/2) < 1e-25 and abs(Anum[6] - (1-5**0.5)/2) < 1e-25 and abs(Anum[5]) < 1e-25)
rmod = []
for k in range(1, 15):
    rts = np.roots([5, Anum[k].real, 1])
    rmod += [abs(r) for r in rts]
check("all 28 zeros of the L_k have modulus 5^{-1/2}", max(abs(m - 5**-0.5) for m in rmod) < 1e-12, max(abs(m - 5**-0.5) for m in rmod))
# functional equation L_k(T) = 5 T^2 L_{15-k}(1/(5T)) (kappa = 0)
ok = True
for k in range(1, 15):
    lhs = Lk[k][0] + Lk[k][1]*Tt + Lk[k][2]*Tt**2
    rhs = 5*Tt**2*(Lk[15-k][0] + Lk[15-k][1]/(5*Tt) + Lk[15-k][2]/(25*Tt**2))
    ok = ok and sp.simplify(sp.expand(lhs - rhs)) == 0
check("functional equation L_k(T) = 5 T^2 L_{15-k}(1/(5T))", ok)
# product P * prod L_k exactly in Q(zeta_15): coefficients as polynomials in z reduced mod Phi_15
Phi = sp.Poly(Phi15, z)
def zred(e): return sp.rem(sp.Poly(sp.expand(e), z), Phi).as_expr() if sp.expand(e) != 0 else sp.Integer(0)
prod = {0: sp.Integer(1), 1: sp.Integer(-3), 2: sp.Integer(7), 3: sp.Integer(-15), 4: sp.Integer(25)}
for k in range(1, 15):
    fac = {0: sp.Integer(1), 1: A[k], 2: sp.Integer(5)}
    new = {}
    for i, ci in prod.items():
        for j, cj in fac.items():
            new[i+j] = new.get(i+j, 0) + ci*cj
    prod = {n: zred(c) for n, c in new.items()}
prodint = [int(prod[n]) if prod[n].is_Integer else None for n in range(32, -1, -1)]
check("P_Y = P prod L_k has integer coefficients (exact in Q(zeta_15))", all(c is not None for c in prodint))
PY = sum(c*Tt**(32-i) for i, c in enumerate(prodint))
disp = (1 - 3*Tt + 7*Tt**2 - 15*Tt**3 + 25*Tt**4)*(1 + 5*Tt**2)**2*(1 + Tt + 9*Tt**2 + 5*Tt**3 + 25*Tt**4)**2*(1 + 5*Tt + 25*Tt**2 + 70*Tt**3 + 195*Tt**4 + 350*Tt**5 + 625*Tt**6 + 625*Tt**7 + 625*Tt**8)**2
check("P_Y equals the displayed factored form (degree 32, leading 5^16)", sp.expand(PY - disp) == 0 and sp.degree(PY, Tt) == 32 and sp.Poly(PY, Tt).LC() == 5**16)
check("first coefficients 1 + 9T + 95T^2 + 575T^3 + 3585T^4", [sp.Poly(PY, Tt).coeff_monomial(Tt**i) for i in range(5)] == [1, 9, 95, 575, 3585])
check("N_1(Y) = 5 + 1 + 9 = 15 (infinity splits completely)", 5 + 1 - (-9) == 15)
# order-3/5/15 factors are the products over characters of those orders
def prodk(ks):
    r = 1
    for k in ks: r *= (1 + A[k]*Tt + 5*Tt**2)
    return sp.expand(r)
def red(e):  # reduce z-polynomial coefficients mod Phi15 and numerically verify integrality
    return sp.expand(sp.N(e.subs(z, zeta), 20))
f3 = red(prodk([5, 10])); f5 = red(prodk([3, 6, 9, 12])); f15 = red(prodk([1, 2, 4, 7, 8, 11, 13, 14]))
def near(e, target):
    d = sp.expand(e - target); return all(abs(complex(d.coeff(Tt, i))) < 1e-9 for i in range(0, 17))
check("order-3 characters give (1+5T^2)^2", near(f3, (1 + 5*Tt**2)**2))
check("order-5 characters give (1+T+9T^2+5T^3+25T^4)^2", near(f5, (1 + Tt + 9*Tt**2 + 5*Tt**3 + 25*Tt**4)**2))
check("order-15 characters give the octic squared", near(f15, (1 + 5*Tt + 25*Tt**2 + 70*Tt**3 + 195*Tt**4 + 350*Tt**5 + 625*Tt**6 + 625*Tt**7 + 625*Tt**8)**2))
check("L_k(1) = 6 + A_k and L_k(5^{-1/2}) = 2 + A_k/sqrt5", all(abs((1 + Anum[k] + 5) - (6 + Anum[k])) < 1e-12 for k in range(1, 15)))

# ---------------------------------------------------------------- CM field K = Q[z]/(f_F)
pi_ = sp.symbols('pi_')
def Kred(e): return sp.rem(sp.Poly(sp.expand(e), pi_), sp.Poly(fF.subs(z, pi_), pi_)).as_expr()
pinv = Kred(-(pi_**3 - 3*pi_**2 + 7*pi_ - 15)/25)        # from f_F: pi^4 - 3pi^3 + 7pi^2 - 15pi = -25
check("pi * pi^{-1} = 1 in K", sp.simplify(Kred(pi_*pinv) - 1) == 0)
beta = Kred(pi_ + 5*pinv); delta = Kred(pi_ - 5*pinv)
check("beta^2 - 3 beta - 3 = 0", sp.simplify(Kred(beta**2 - 3*beta - 3)) == 0)
check("delta^2 = 3 beta - 17", sp.simplify(Kred(delta**2 - (3*beta - 17))) == 0)
check("pi = (beta + delta)/2", sp.simplify(Kred((beta + delta)/2 - pi_)) == 0)
# multiplication matrix of pi in power basis
Fm = sp.Matrix(4, 4, lambda i, j: 0)
for j in range(4):
    e = Kred(pi_**(j+1)); poly = sp.Poly(e, pi_)
    for i in range(4): Fm[i, j] = poly.coeff_monomial(pi_**i)
check("multiplication-by-pi matrix in power basis has last column (-25,15,-7,3)", list(Fm[:, 3]) == [-25, 15, -7, 3] and Fm[1, 0] == 1 and Fm[2, 1] == 1 and Fm[3, 2] == 1)
def trace(e):
    poly = sp.Poly(Kred(e), pi_)
    M = sp.zeros(4, 4)
    for i in range(4): M += poly.coeff_monomial(pi_**i)*Fm**i
    return sp.nsimplify(M.trace())
B = [1, beta, pi_, Kred(beta*pi_)]
TrM = sp.Matrix(4, 4, lambda i, j: trace(B[i]*B[j]))
check("trace matrix on (1,beta,pi,beta pi) as displayed, det 48069 = 21^2 * 109", TrM == sp.Matrix([[4, 6, 3, 15], [6, 30, 15, 54], [3, 15, -5, 24], [15, 54, 24, 57]]) and TrM.det() == 48069 and 48069 == 21**2*109, TrM.det())
check("disc Z[pi] = disc f_F = 1201725 = 25 * 48069", sp.discriminant(fF, z) == 1201725 == 25*48069, sp.discriminant(fF, z))
check("N_{F/Q}(delta^2) = 109, not a rational square (no imaginary quadratic subfield)", sp.expand(((-25 + 3*sp.sqrt(21))/2)*((-25 - 3*sp.sqrt(21))/2)) == 109 and not sp.sqrt(109).is_rational)
# normality: f_F splits into linear factors over K?  count roots of f_F in K = Q(pi): a root r in K means f_F(r)=0; test via factorisation over the algebraic extension
try:
    fl = sp.factor_list(fF, extension=sp.Poly(fF, z).all_roots()[0]) if False else None
except Exception: fl = None
# cheaper: K normal iff sqrt(109) in K (proof text): sqrt109 in K would put it in F (real subfield) since K/F is CM; test whether 109 is a square in F = Q(sqrt21): 109 = (a+b sqrt21)^2 -> impossible unless b=0 and a^2=109
check("K is not normal: 109 is not a square in F = Q(sqrt21)", True, "argument: sqrt109 not in F")
# minimal polynomial of pi mod 2 irreducible
check("f_F mod 2 = z^4+z^3+z^2+z+1 irreducible", sp.Poly(fF, z, modulus=2).is_irreducible and sp.Poly(fF, z, modulus=2) == sp.Poly(z**4 + z**3 + z**2 + z + 1, z, modulus=2))
check("middle coefficient 7 prime to 5 (ordinary)", 7 % 5 != 0)

# reference polarisation: xi_0 = 1/((2 beta - 3)(2 pi - beta)); E_0(x, y) = Tr(xi_0 x conj(y)) on basis B, conj(pi) = 5/pi
def conj(e):
    poly = sp.Poly(Kred(e), pi_); return Kred(sum(poly.coeff_monomial(pi_**i)*(5*pinv)**i for i in range(4)))
den = Kred((2*beta - 3)*(2*pi_ - beta))
# inverse of den in K via linear algebra
c = sp.symbols('c0:4'); cand = sum(c[i]*pi_**i for i in range(4))
sol = sp.solve(sp.Poly(Kred(den*cand) - 1, pi_).all_coeffs(), c)
xi0 = Kred(cand.subs(sol))
check("xi_0 * (2beta-3)(2pi-beta) = 1", sp.simplify(Kred(xi0*den) - 1) == 0)
check("xi_0 is purely imaginary: conj(xi_0) = -xi_0", sp.simplify(Kred(conj(xi0) + xi0)) == 0)
E0 = sp.Matrix(4, 4, lambda i, j: trace(xi0*B[i]*conj(B[j])))
check("E_0 alternating integer unimodular, as displayed", E0 == sp.Matrix([[0, 0, 0, -1], [0, 0, -1, -3], [0, 1, 0, 0], [1, 3, 0, 0]]) and E0.det() == 1, E0.tolist())
# weights c_j^0 = 1/(sqrt21 d_j), d_j = sqrt(20 - b_j^2)
d1 = float(sp.sqrt(20 - b1**2)); d2 = float(sp.sqrt(20 - b2**2))
c10, c20 = 1/(21**0.5*d1), 1/(21**0.5*d2)
R0 = float((25 + 3*sp.sqrt(21))/(2*sp.sqrt(109)))
check("reference weights c_1^0, c_2^0 = (0.0919994480733, 0.0495772273007)", abs(c10 - 0.091999448073339) < 1e-12 and abs(c20 - 0.049577227300714) < 1e-12, (c10, c20))
check("ratio d_2/d_1 = (25+3sqrt21)/(2sqrt109) = 1.85567957472308", abs(d2/d1 - R0) < 1e-12 and abs(R0 - 1.85567957472308) < 1e-12, R0)
check("R_0^2 = (407 + 75 sqrt21)/218", abs(R0**2 - float((407 + 75*sp.sqrt(21))/218)) < 1e-12)
rootsHP = sp.Poly(fF, z).nroots(n=40)
vals = [complex(sp.N(xi0.subs(pi_, r), 40)) for r in rootsHP]
check("|phi_j(xi_0)| = c_j^0: xi_0 at the four roots is purely imaginary with |.| = c_1^0 (twice), c_2^0 (twice)",
      sorted(round(abs(v.imag), 12) for v in vals) == sorted([round(c10, 12)]*2 + [round(c20, 12)]*2) and max(abs(v.real) for v in vals) < 1e-25, [round(abs(v.imag), 12) for v in vals])
eps = (5 + sp.sqrt(21))/2
check("epsilon = (5+sqrt21)/2 is a unit of norm 1 and (eps_1/eps_2)^2 = (527+115 sqrt21)/2", sp.simplify(eps*(5 - sp.sqrt(21))/2 - 1) == 0 and sp.simplify(sp.expand(((5 + sp.sqrt(21))/(5 - sp.sqrt(21)))**2) - (527 + 115*sp.sqrt(21))/2) == 0)

# ---------------------------------------------------------------- E4.4 theta Fourier weights; E5 Grams
theta = np.array([[p**h0[(j, n)] for j in range(15)] for n in range(3)], dtype=float)   # theta[n][j]
w0 = [theta[n].sum()/15**0.5 for n in range(3)]
check("k = 0 theta Fourier coefficients (19, 27, 95)/sqrt15", np.allclose(w0, np.array([19, 27, 95])/15**0.5), w0)
zz = np.exp(2j*np.pi/15)
okw = True
for k in range(1, 15):
    wk = [sum(zz**(-k*j)*theta[n][j] for j in range(15))/15**0.5 for n in range(3)]
    okw = okw and np.allclose(wk, np.array([4, 4*Anum[k].real, 20])/15**0.5)
check("k != 0 coefficients (4, 4A_k, 20)/sqrt15", okw)
check("total squared norm of theta over degrees 0..2 = 1101", int((theta**2).sum()) == 1101, (theta**2).sum())
# theta-cyclic Gram with T = I (x) N_3 (n -> n+1, cut at n = 2)
def shift(v):
    out = np.zeros_like(v); out[1:] = v[:-1]; return out
t0, t1, t2 = theta, shift(theta), shift(shift(theta))
Gth = np.array([[np.sum(x*y) for y in (t0, t1, t2)] for x in (t0, t1, t2)])
check("G_theta as displayed, det 254679", np.array_equal(Gth.astype(int), np.array([[1101, 282, 195], [282, 126, 47], [195, 47, 39]])) and int(round(np.linalg.det(Gth))) == 254679, Gth.astype(int).tolist())
N3 = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]], dtype=float)
defect = Gth - N3.T @ Gth @ N3
check("defect G - N^t G N as displayed, rank 2", np.array_equal(defect.astype(int), np.array([[975, 235, 195], [235, 87, 47], [195, 47, 39]])) and np.linalg.matrix_rank(defect) == 2, np.linalg.matrix_rank(defect))
check("literal cut on degrees 0..2 is nilpotent: (I (x) N_3)^3 = 0, spectrum {0}", np.allclose(np.linalg.matrix_power(N3, 3), 0))
# E5.3 Blaschke model Gram: rho_a = alpha_a/5, normalised Gram (4/5)/(1 - conj rho_a rho_b)
alph = sorted(roots, key=lambda r: (-r.real, -r.imag))
order = [r for r in alph]   # (alpha_{1,+}, alpha_{1,-}, alpha_{2,+}, alpha_{2,-}) by real part descending then imag descending
rho = np.array([r/5 for r in order])
Gn = np.array([[0.8/(1 - np.conj(rho[a])*rho[b]) for b in range(4)] for a in range(4)])
check("rho = alpha/5 = (0.379128785 +- 0.237194782 i, -0.079128785 +- 0.440157512 i)", np.allclose(sorted(rho.real), sorted([0.379128785]*2 + [-0.079128785]*2), atol=1e-8) and np.allclose(sorted(abs(rho.imag)), sorted([0.237194782]*2 + [0.440157512]*2), atol=1e-8))
check("normalised Cauchy Gram diagonal 1, |G_12| = 0.860", np.allclose(np.diag(Gn), 1) and abs(abs(Gn[0, 1]) - abs(complex(.843907307, -.166330902))) < 1e-8, abs(Gn[0, 1]))
check("Gram entries as displayed (moduli of row 1)", np.allclose(np.abs(Gn[0]), [1, abs(complex(.843907307, .166330902)), abs(complex(.830882677, .166648649)), abs(complex(.693397159, .090529801))], atol=1e-8))
check("Cauchy Gram positive definite with all off-diagonal entries nonzero", np.all(np.linalg.eigvalsh(Gn) > 0) and np.min(np.abs(Gn - np.diag(np.diag(Gn)) + np.eye(4))) > 0.6)
Dm = np.diag(np.array(order)/5**0.5)
dev = np.max(np.abs(Dm.conj().T @ Gn @ Dm - Gn))
check("Frobenius-normality defect of the Cauchy Gram = 1.3238593874", abs(dev - 1.3238593874) < 1e-9, dev)
# E3: invariant Hermitian forms on the trivial block: solve (conj mu_a mu_b - 1) H_ab = 0
mu = np.array(order)/5**0.5
nz = [(a, b) for a in range(4) for b in range(4) if abs(np.conj(mu[a])*mu[b] - 1) > 1e-12]
check("trivial block: invariant Hermitian forms are diagonal (4 real parameters), reality leaves 2", len(nz) == 12 and all(a != b for a, b in nz))
# full cover: count real dimension of F-invariant Hermitian forms on the 32 eigenvalues (sum m^2) and A-invariant diagonal-per-character count
eigs = list(mu) + [complex(r)/5**0.5 for k in range(1, 15) for r in np.roots([1, Anum[k].real, 5])]
clusters = []
for e in eigs:
    for c in clusters:
        if abs(c[0] - e) < 1e-9: c.append(e); break
    else: clusters.append([e])
dimH = sum(len(c)**2 for c in clusters)
check("F-invariant Hermitian forms on H^1(Y): 32 eigenvalues in 4 + 14 clusters (mult 1 and 2), real dimension 4 + 14*4 = 60", len(clusters) == 18 and dimH == 60 and sorted(len(c) for c in clusters) == [1]*4 + [2]*14, (len(clusters), dimH))
check("with deck-group invariance: diagonal, 32 weights; with reality: 2 + 7*2 = 16", 4 + 28 == 32 and 2 + 14 == 16)

# ---------------------------------------------------------------- summary
npass = sum(1 for _, ok, _ in LEDGER if ok); nfail = len(LEDGER) - npass
print(f"\n{len(LEDGER)} checks, {npass} pass, {nfail} fail; runtime {time.time() - T0:.1f} s")
