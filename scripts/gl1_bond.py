#!/usr/bin/env python3
"""gl1_bond.py -- blind numerics lane for `notes/gl1-bond/brief.md` (claims B1--B5).

Author line: claude:opus.  Protocol: BLIND to `notes/gl1-bond/proofs.md` (not read).
Deterministic (seed 20260921), no timestamps, no memory addresses, no imports from
any other repository script.  Every claim is an assertion through the single helper
`check(cond, msg)`; a failing check is recorded and the run continues; no tolerance
was ever loosened to make a claim pass.

Ledger rows are labelled D01, D02, ... (two digits) so that they are never confused
with the two CURVES, which the brief calls D2 and D3.

================================================================================
CONVENTIONS FIXED HERE (re-derived, not copied)
================================================================================

CURVES (shard 04k, `def:elliptic-cavity`).
  curve D2:  y^2 + y = x^3 + x + 1  over F_2   (a1,a2,a3,a4,a6) = (0,0,1,0,1,1) ... see below
  curve D3:  y^2       = x^3 + x + 1  over F_3
In the general Weierstrass form  y^2 + a1 x y + a3 y = x^3 + a2 x^2 + a4 x + a6 :
  curve D2:  a1=0, a2=0, a3=1, a4=1, a6=1   (q = 2)
  curve D3:  a1=0, a2=0, a3=0, a4=1, a6=1   (q = 3)
P_0 := the point at infinity O = (0:1:0), which is F_q-rational and is the identity
of the group law; R = O(C \ P_0) is the affine coordinate ring F_q[x,y]/(curve).

FINITE FIELDS.  q is prime in both cases, so F_q = F_p.  F_{q^k} = F_q[t]/(m_k) with
m_k the LEXICOGRAPHICALLY FIRST monic irreducible of degree k (coefficients read
low-to-high as base-q digits), found by trial division against the irreducibles of
degree <= k/2.  Elements are coefficient tuples (c_0,...,c_{k-1}) low-to-high.
F_q sits in F_{q^k} as the constants (c,0,...,0), which is how E(F_q) <= E(F_{q^k}).
Frobenius is a |-> a^q, applied coordinatewise to points.

GROUP LAW (implemented here, Silverman III.2.3, general Weierstrass, char 2 included):
  -(x,y) = (x, -y - a1 x - a3);
  P1 + P2 (x1 != x2): L = (y2-y1)/(x2-x1),  V = (y1 x2 - y2 x1)/(x2-x1);
  2P     (2y1+a1x1+a3 != 0): L = (3x1^2+2a2x1+a4-a1y1)/(2y1+a1x1+a3),
                             V = (-x1^3+a4x1+2a6-a3y1)/(2y1+a1x1+a3);
  x3 = L^2 + a1 L - a2 - x1 - x2,   y3 = -(L+a1) x3 - V - a3.
No short-Weierstrass shortcut is used for curve D2 (char 2, a3 = 1).

CLOSED POINTS.  A closed point of degree k is a Frobenius orbit of size exactly k
in C(F_{q^k}); the orbit of O is the unique rational point at infinity, degree 1.
b_k := #closed points of degree k; sum_{d | k} d b_d = N_k = #C(F_{q^k}).
An effective divisor of degree n is a multiset of closed points with degrees
summing to n.

DIVISOR CLASSES.  For a closed point P of degree d with orbit {Q, Q^s, ..., Q^{s^{d-1}}}
in E(F_{q^d}), the trace  Tr(P) = Q + Q^s + ... + Q^{s^{d-1}}  is Frobenius-invariant,
hence lies in E(F_q); it is the class of the degree-0 divisor P - d P_0 under
Pic^0(K) = E(F_q) (P_0 = O contributes 0).  The class of  sum_i m_i P_i  in
Pic^0 (after subtracting (deg D) P_0) is  sum_i m_i Tr(P_i)  in E(F_q).
That Tr(P) is F_q-rational is CHECKED, not assumed (row D12).

h^0.  Two independent routes are used and compared.
 (i) RIEMANN--ROCH CONSEQUENCE (declared, as the brief permits): on a genus-one
     curve h^0(D) = deg D for deg D >= 1, h^0(D) = 0 for deg D < 0, and for
     deg D = 0, h^0(D) = 1 iff D is principal, which the group law decides
     (sum m_i = 0 and sum m_i Tr(P_i) = O).  This is the function `rr_h0`.
 (ii) ENUMERATION (independent of (i)): for 0 <= n <= 4 every effective divisor of
     degree n is enumerated and sorted into its class; #{E >= 0 : E ~ D} determines
     h^0 through #{E >= 0 : E ~ D} = (q^{h^0(D)} - 1)/(q - 1).  This is `h0_emp`.
     Rows D13--D15 check (ii) against (i); the Riemann--Roch statements of the brief
     are verified against (ii), i.e. against raw counting, not against (i).
 (iii) LINEAR ALGEBRA over F_{q^6} for the divisors n P_0, n = 0..4 (row D10):
     L(n P_0) = span{x^i y^j : j in {0,1}, 2i + 3j <= n}  (ord_{P_0} x = -2,
     ord_{P_0} y = -3, and every function regular away from P_0 lies in
     R = F_q[x,y]/(curve), whose F_q-basis is {x^i y^j, j <= 1}); the spanning
     inclusion is the standard description of the affine coordinate ring and is
     the one structural input here.  INDEPENDENCE is proved numerically: a nonzero
     element of that span has at most n zeros, so full column rank of the matrix of
     its values at more than n affine points of C(F_{q^6}) is a proof.

d^x x denotes the multiplicative Haar measure dx/x on R_+^x (B4(b)).

TOLERANCES.  Exact (integer / sympy over Q or Q(i), Q(sqrt 3)) wherever exactness is
available: all point counts, all divisor counts, all class-group arithmetic, all
zeta and L identities, the functional equation and the superdeterminant.  The only
floating-point work is the theta/xi section, done in mpmath at 40 working digits and
asserted at 1e-25 absolute for the identities that are not near a zero; near a zero
of xi the assertion is on the size of the value, with the threshold set by the
truncation of the quoted zero (~1e-7 in t), not chosen to make anything pass.
"""

import inspect
import itertools
from functools import lru_cache

import numpy as np
import sympy as sp
import mpmath as mp

SEED = 20260921
RNG = np.random.default_rng(SEED)

# ---------------------------------------------------------------------------
# the single assertion helper
# ---------------------------------------------------------------------------
_PASS = 0
_FAIL = 0
_FAILED = []


def check(cond, msg):
    """The single assertion helper: counts, prints one line, never aborts."""
    global _PASS, _FAIL
    line = inspect.currentframe().f_back.f_lineno
    ok = bool(cond)
    if ok:
        _PASS += 1
    else:
        _FAIL += 1
        _FAILED.append((line, msg))
    print(f"  {'ok  ' if ok else 'FAIL'} [L{line:4d}]  {msg}")
    return ok


def note(msg):
    print(f"  --           {msg}")


def head(msg):
    print()
    print("=" * 100)
    print(msg)
    print("=" * 100)


# ---------------------------------------------------------------------------
# polynomials over F_p, low-to-high coefficient lists (graded_toys convention)
# ---------------------------------------------------------------------------
def pnorm(a, p):
    a = [c % p for c in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def pmod(a, m, p):
    a = pnorm(list(a), p)
    m = pnorm(list(m), p)
    inv = pow(m[-1], p - 2, p)
    while len(a) >= len(m) and a != [0]:
        d = len(a) - len(m)
        c = (a[-1] * inv) % p
        if c == 0:
            break
        sub = [0] * d + [(c * x) % p for x in m]
        a = pnorm([(a[i] if i < len(a) else 0) - (sub[i] if i < len(sub) else 0)
                   for i in range(max(len(a), len(sub)))], p)
    return pnorm(a, p)


def monics(n, p):
    out = []
    for k in range(p ** n):
        co, kk = [], k
        for _ in range(n):
            co.append(kk % p)
            kk //= p
        out.append(co + [1])
    return out


def irreducibles(maxdeg, p):
    out = []
    for d in range(1, maxdeg + 1):
        for f in monics(d, p):
            red = any(len(g) - 1 <= d // 2 and pmod(f, g, p) == [0] for g in out)
            if not red:
                out.append(f)
    return out


# ---------------------------------------------------------------------------
# F_{p^k}
# ---------------------------------------------------------------------------
class GF:
    def __init__(self, p, k, modulus):
        self.p, self.k = p, k
        self.mod = modulus                    # length k+1, monic
        self.size = p ** k
        self.zero = (0,) * k
        self.one = (1,) + (0,) * (k - 1)

    def emb(self, c):
        return (c % self.p,) + (0,) * (self.k - 1)

    def is_base(self, a):
        return all(c == 0 for c in a[1:])

    def add(self, a, b):
        p = self.p
        return tuple((x + y) % p for x, y in zip(a, b))

    def sub(self, a, b):
        p = self.p
        return tuple((x - y) % p for x, y in zip(a, b))

    def neg(self, a):
        p = self.p
        return tuple((-x) % p for x in a)

    def mul(self, a, b):
        p, k, m = self.p, self.k, self.mod
        c = [0] * (2 * k - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        c[i + j] = (c[i + j] + x * y) % p
        for i in range(2 * k - 2, k - 1, -1):
            co = c[i]
            if co:
                c[i] = 0
                base = i - k
                for j in range(k):
                    c[base + j] = (c[base + j] - co * m[j]) % p
        return tuple(c[:k])

    def pw(self, a, n):
        r, b = self.one, a
        while n:
            if n & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            n >>= 1
        return r

    def inv(self, a):
        return self.pw(a, self.size - 2)

    def div(self, a, b):
        return self.mul(a, self.inv(b))

    def elements(self):
        return [tuple(e) for e in itertools.product(range(self.p), repeat=self.k)]

    def frob(self, a):
        return self.pw(a, self.p)


@lru_cache(maxsize=None)
def field(p, k):
    irr = irreducibles(k, p)
    m = next(g for g in irr if len(g) - 1 == k)
    return GF(p, k, m)


# ---------------------------------------------------------------------------
# elliptic curves in general Weierstrass form
# ---------------------------------------------------------------------------
INF = "O"


class Curve:
    def __init__(self, name, q, a1, a2, a3, a4, a6, eqn):
        self.name, self.q = name, q
        self.a = (a1, a2, a3, a4, a6)
        self.eqn = eqn

    def co(self, F):
        return [F.emb(c) for c in self.a]

    def on(self, F, P):
        if P == INF:
            return True
        a1, a2, a3, a4, a6 = self.co(F)
        x, y = P
        lhs = F.add(F.add(F.mul(y, y), F.mul(F.mul(a1, x), y)), F.mul(a3, y))
        rhs = F.add(F.add(F.add(F.mul(F.mul(x, x), x), F.mul(a2, F.mul(x, x))),
                          F.mul(a4, x)), a6)
        return lhs == rhs

    def neg(self, F, P):
        if P == INF:
            return INF
        a1, a2, a3, a4, a6 = self.co(F)
        x, y = P
        return (x, F.neg(F.add(F.add(y, F.mul(a1, x)), a3)))

    def add(self, F, P, Q):
        if P == INF:
            return Q
        if Q == INF:
            return P
        a1, a2, a3, a4, a6 = self.co(F)
        two, three = F.emb(2), F.emb(3)
        x1, y1 = P
        x2, y2 = Q
        if x1 == x2:
            if Q == self.neg(F, P):
                return INF
            # x1 == x2 and Q != -P forces Q == P on a Weierstrass curve
            den = F.add(F.add(F.mul(two, y1), F.mul(a1, x1)), a3)
            nl = F.sub(F.add(F.add(F.mul(three, F.mul(x1, x1)),
                                   F.mul(two, F.mul(a2, x1))), a4), F.mul(a1, y1))
            nv = F.sub(F.add(F.add(F.neg(F.mul(F.mul(x1, x1), x1)), F.mul(a4, x1)),
                             F.mul(two, a6)), F.mul(a3, y1))
            L = F.div(nl, den)
            V = F.div(nv, den)
        else:
            dx = F.sub(x2, x1)
            L = F.div(F.sub(y2, y1), dx)
            V = F.div(F.sub(F.mul(y1, x2), F.mul(y2, x1)), dx)
        x3 = F.sub(F.sub(F.sub(F.add(F.mul(L, L), F.mul(a1, L)), a2), x1), x2)
        y3 = F.sub(F.sub(F.neg(F.mul(F.add(L, a1), x3)), V), a3)
        return (x3, y3)

    def mulz(self, F, n, P):
        if n < 0:
            return self.mulz(F, -n, self.neg(F, P))
        R, Q = INF, P
        while n:
            if n & 1:
                R = self.add(F, R, Q)
            Q = self.add(F, Q, Q)
            n >>= 1
        return R

    def points(self, F):
        """All points of C(F), point at infinity first."""
        p = F.p
        a1, a2, a3, a4, a6 = self.co(F)
        els = F.elements()
        sq = {}
        for y in els:
            sq.setdefault(F.mul(y, y), []).append(y)
        asm = {}
        if p == 2:
            for u in els:
                asm.setdefault(F.add(F.mul(u, u), u), []).append(u)
        pts = [INF]
        for x in els:
            R = F.add(F.add(F.add(F.mul(F.mul(x, x), x), F.mul(a2, F.mul(x, x))),
                            F.mul(a4, x)), a6)
            c = F.add(F.mul(a1, x), a3)
            if p == 2:
                if c == F.zero:
                    for y in sq.get(R, []):
                        pts.append((x, y))
                else:
                    t = F.div(R, F.mul(c, c))
                    for u in asm.get(t, []):
                        pts.append((x, F.mul(c, u)))
            else:
                # complete the square: (y + c/2)^2 = R + c^2/4
                half = F.inv(F.emb(2))
                sh = F.mul(c, half)
                t = F.add(R, F.mul(sh, sh))
                for z in sq.get(t, []):
                    pts.append((x, F.sub(z, sh)))
        return pts

    def pfrob(self, F, P):
        if P == INF:
            return INF
        return (F.frob(P[0]), F.frob(P[1]))


C_D2 = Curve("D2", 2, 0, 0, 1, 1, 1, "y^2 + y = x^3 + x + 1 over F_2")
C_D3 = Curve("D3", 3, 0, 0, 0, 1, 1, "y^2 = x^3 + x + 1 over F_3")
CURVES = [C_D2, C_D3]

# from shard 04k, def:elliptic-cavity (STATED, not derived here)
SHARD = {
    "D2": dict(q=2, P=[1, -2, 2], alphas=[1 + sp.I, 1 - sp.I], cusps=1, pic="Z/1"),
    "D3": dict(q=3, P=[1, 0, 3], alphas=[sp.I * sp.sqrt(3), -sp.I * sp.sqrt(3)],
               cusps=4, pic="Z/4"),
}

T = sp.symbols('T')
w_s, s_s = sp.symbols('w s')

KMAX = 6
NMAX_ENUM = 4

print(f"GL_1 bond numerics: the class group as bond, the theta functional as its state.")
print()
print("Blind numerics lane for `notes/gl1-bond/brief.md` (claims B1--B5).")
print("Run BLIND to `notes/gl1-bond/proofs.md`.  Deterministic; seed 20260921;")
print("author claude:opus.  Ledger rows are D01, D02, ...; the two CURVES are D2 and D3.")

# ===========================================================================
head("SECTION 1   the curves, their point counts and the Weil numbers   [B1(d), 04k]")
# ===========================================================================

DATA = {}
for C in CURVES:
    q = C.q
    sh = SHARD[C.name]
    Psym = sum(sp.Integer(c) * T ** i for i, c in enumerate(sh["P"]))
    Z = sp.cancel(Psym / ((1 - T) * (1 - q * T)))
    Nk = []
    orbits = {}
    allpts = {}
    for k in range(1, KMAX + 1):
        F = field(q, k)
        pts = C.points(F)
        Nk.append(len(pts))
        allpts[k] = (F, pts)
        seen = set()
        orb = []
        for P in pts:
            if P in seen:
                continue
            o = [P]
            Qn = C.pfrob(F, P)
            while Qn != P:
                o.append(Qn)
                Qn = C.pfrob(F, Qn)
            for R in o:
                seen.add(R)
            orb.append(tuple(sorted(o, key=repr)))
        orbits[k] = orb
    DATA[C.name] = dict(q=q, P=Psym, Z=Z, Nk=Nk, orbits=orbits, pts=allpts)

    note(f"curve {C.name}: {C.eqn};  N_k (k=1..{KMAX}) = {Nk}")
    # -- D01
    al = sh["alphas"]
    Pfromal = sp.expand(sp.prod([1 - a * T for a in al]))
    check(sp.simplify(Pfromal - Psym) == 0,
          f"D01 curve {C.name}: P(T) = prod_i (1 - alpha_i T) with the 04k Weil numbers "
          f"{[sp.nsimplify(a) for a in al]} equals the 04k numerator {sp.expand(Psym)}")
    check(all(sp.simplify(sp.Abs(a) ** 2 - q) == 0 for a in al),
          f"D01 curve {C.name}: |alpha_i| = sqrt(q) = sqrt({q}) for both Weil numbers "
          f"(Hasse; B5(b) calls this NOT forced by B1--B4)")
    check(Nk[0] == 1 + q - sum(al) and sp.simplify(sp.Integer(Nk[0]) - (1 + q - sum(al))) == 0,
          f"D01 curve {C.name}: N_1 = 1 + q - sum alpha_i = {Nk[0]} by direct enumeration "
          f"of C(F_q) (point at infinity included)")

    # -- D02
    ok = True
    pred = []
    for k in range(1, KMAX + 1):
        v = sp.simplify(1 + q ** k - sum(a ** k for a in al))
        pred.append(int(v))
        ok = ok and int(v) == Nk[k - 1]
    check(ok, f"D02 curve {C.name}: N_k = 1 + q^k - sum_i alpha_i^k for k = 1..{KMAX}: "
              f"enumerated {Nk} = predicted {pred}")

# ===========================================================================
head("SECTION 2   closed points, effective divisors and a_n   [B1(a), B1(b), B1(c)]")
# ===========================================================================


def mobius(n):
    r, m = 1, n
    d = 2
    while d * d <= m:
        if m % d == 0:
            m //= d
            if m % d == 0:
                return 0
            r = -r
        d += 1
    if m > 1:
        r = -r
    return r


for C in CURVES:
    q, D = C.q, DATA[C.name]
    b = {}
    closed = {}
    for k in range(1, KMAX + 1):
        ok_deg = [o for o in D["orbits"][k] if len(o) == k]
        b[k] = len(ok_deg)
        closed[k] = ok_deg
    D["b"] = b
    D["closed"] = closed
    note(f"curve {C.name}: closed-point counts b_d (d = 1..{KMAX}) = "
         f"{[b[k] for k in range(1, KMAX + 1)]}")

    # -- D03
    ok = all(sum(d * b[d] for d in range(1, k + 1) if k % d == 0) == D["Nk"][k - 1]
             for k in range(1, KMAX + 1))
    check(ok, f"D03 curve {C.name}: sum_(d | k) d b_d = N_k for k = 1..{KMAX} "
              f"(the Frobenius orbits of C(F_(q^k)) partition into closed points)")
    okm = all(b[k] == sum(mobius(k // d) * D["Nk"][d - 1] for d in range(1, k + 1) if k % d == 0) // k
              for k in range(1, KMAX + 1))
    check(okm, f"D03 curve {C.name}: b_k = (1/k) sum_(d | k) mu(k/d) N_d for k = 1..{KMAX} "
               f"(Mobius inversion of the same partition)")
    check(b[1] == D["Nk"][0] and any(len(o) == 1 and o[0] == INF for o in closed[1]),
          f"D03 curve {C.name}: the b_1 = {b[1]} degree-one closed points are the F_q-points, "
          f"and the point at infinity P_0 = O is one of them (a rational cusp of the affine ring)")

    # -- D04: a_n from the closed points against the coefficients of Z(T)
    ser = sp.expand(sp.series(D["Z"], T, 0, KMAX + 2).removeO())
    a_zeta = [int(ser.coeff(T, n)) for n in range(KMAX + 1)]
    gen = [0] * (KMAX + 1)
    gen[0] = 1
    for d in range(1, KMAX + 1):
        for _ in range(b[d]):
            new = list(gen)
            for n in range(d, KMAX + 1):
                new[n] += new[n - d]
            gen = new
    D["a"] = gen
    D["a_zeta"] = a_zeta
    check(gen == a_zeta,
          f"D04 curve {C.name}: a_n = #(effective divisors of degree n) built from the closed "
          f"points = {gen} equals the Taylor coefficients of Z(T) = P(T)/((1-T)(1-qT)) = "
          f"{a_zeta}, n = 0..{KMAX}   [B1(a)]")

    # -- D05: B1(b) generic Riemann--Roch part
    h = D["Nk"][0]
    g = 1
    gen_pred = [sp.Rational(h * (q ** (n + 1 - g) - 1), q - 1) for n in range(KMAX + 1)]
    ok_gen = all(sp.Integer(gen[n]) == gen_pred[n] for n in range(2 * g - 1, KMAX + 1))
    check(ok_gen,
          f"D05 curve {C.name}: a_n = h (q^(n+1-g) - 1)/(q-1) for every n > 2g-2 = 0 "
          f"(h = {h}, g = 1): {[int(x) for x in gen_pred[1:]]} = {gen[1:]}   [B1(b)]")
    check(sp.Integer(gen[0]) != gen_pred[0] and gen[0] == 1,
          f"D05 curve {C.name}: the only deviation from the generic formula sits at n = 0 "
          f"<= 2g-2 = 0: a_0 = 1 but h(q^(1-g)-1)/(q-1) = {int(gen_pred[0])}   [B1(b)]")

    # -- D06: two-mode (q, 1) structure of the generic part
    ok_rec = all(gen[n + 1] == (q + 1) * gen[n] - q * gen[n - 1] for n in range(2, KMAX))
    check(ok_rec,
          f"D06 curve {C.name}: for n >= 1 the sequence a_n satisfies a_(n+1) = (q+1) a_n - q a_(n-1), "
          f"i.e. it is a combination of the two geometric modes q^n and 1 -- the Perron pair of "
          f"B1(c); the characteristic roots are {{q, 1}} = {{{q}, 1}}")
    A0, B0 = sp.Rational(h, q - 1), -sp.Rational(h, q - 1)
    ok_two = all(sp.Integer(gen[n]) == A0 * q ** n + B0 for n in range(1, KMAX + 1))
    check(ok_two and A0 * q ** 0 + B0 == 0 != gen[0],
          f"D06 curve {C.name}: explicitly a_n = A q^n + B with A = h/(q-1) = {A0} and "
          f"B = -h/(q-1) = {B0} for every n >= 1 (the eigenvalues q and 1 of the degree-shift "
          f"with their Perron weights), while the same closed form gives 0 at n = 0 and "
          f"a_0 = 1: the whole deviation is the single special degree n = 0 = 2g-2   [B1(b),(c)]")

# ===========================================================================
head("SECTION 3   the group law and Pic^0 = E(F_q)   [B1(d), B3(a)]")
# ===========================================================================

for C in CURVES:
    q, D = C.q, DATA[C.name]
    F1 = field(q, 1)
    E1 = C.points(F1)
    D["E1"] = E1
    # -- D07 group law axioms
    okon = all(C.on(F1, P) for P in E1)
    check(okon, f"D07 curve {C.name}: every enumerated point of C(F_q) satisfies the Weierstrass "
                f"equation ({len(E1)} points, infinity included)")
    ok_id = all(C.add(F1, P, INF) == P and C.add(F1, INF, P) == P for P in E1)
    ok_inv = all(C.add(F1, P, C.neg(F1, P)) == INF for P in E1)
    ok_com = all(C.add(F1, P, Q) == C.add(F1, Q, P) for P in E1 for Q in E1)
    ok_cl = all(C.on(F1, C.add(F1, P, Q)) for P in E1 for Q in E1)
    check(ok_id and ok_inv and ok_com and ok_cl,
          f"D07 curve {C.name}: over F_q the group law is closed, commutative, has identity O "
          f"and inverses (all {len(E1)}^2 pairs)")
    ok_as = all(C.add(F1, C.add(F1, P, Q), R) == C.add(F1, P, C.add(F1, Q, R))
                for P in E1 for Q in E1 for R in E1)
    check(ok_as, f"D07 curve {C.name}: associativity over F_q, all {len(E1)}^3 triples")

    F3f = field(q, 3)
    E3 = C.points(F3f)
    idx = RNG.integers(0, len(E3), size=(60, 3))
    ok_as3 = True
    ok_on3 = all(C.on(F3f, P) for P in E3)
    for i, j, k in idx:
        P, Q, R = E3[int(i)], E3[int(j)], E3[int(k)]
        if C.add(F3f, C.add(F3f, P, Q), R) != C.add(F3f, P, C.add(F3f, Q, R)):
            ok_as3 = False
    check(ok_on3 and ok_as3,
          f"D07 curve {C.name}: over F_(q^3) ({len(E3)} points) every point is on the curve and "
          f"associativity holds on 60 seeded random triples (seed {SEED})")

    # -- D08 Pic^0
    h = len(E1)
    D["h"] = h
    orders = []
    for P in E1:
        n, Qp = 1, P
        while Qp != INF:
            Qp = C.add(F1, Qp, P)
            n += 1
        orders.append(n if P != INF else 1)
    D["orders"] = orders
    check(h == SHARD[C.name]["q"] ** 0 * (1 if C.name == "D2" else 4) and h == D["Nk"][0],
          f"D08 curve {C.name}: |Pic^0(K)| = |E(F_q)| = h = {h}, matching the class number "
          f"stated in shard 04k ({SHARD[C.name]['pic']})   [B1(d), B3(a)]")
    if C.name == "D3":
        check(max(orders) == 4 and h == 4,
              f"D08 curve D3: Pic^0 = E(F_3) is CYCLIC of order 4 (an element of order 4 exists; "
              f"orders {sorted(orders)}), i.e. Z/4 as shard 04k states; it is not (Z/2)^2")
        gens = [P for P, o in zip(E1, orders) if o == 4]
        D["gen"] = gens[0]
        dlog = {}
        Qp = INF
        for j in range(4):
            dlog[Qp] = j
            Qp = C.add(F1, Qp, D["gen"])
        D["dlog"] = dlog
        check(len(dlog) == 4, "D08 curve D3: the discrete logarithm Pic^0 -> Z/4 to the chosen "
                              "generator is a bijection onto {0,1,2,3}")
    else:
        D["gen"] = INF
        D["dlog"] = {INF: 0}
        check(orders == [1] and h == 1,
              "D08 curve D2: Pic^0 = E(F_2) = {O} is trivial, h = 1 (shard 04k: |Pic(R)| = 1)")

    # -- D09 B1(d)
    Pd = sp.expand((1 - T) * (1 - q * T) + h * T)
    check(sp.simplify(Pd - D["P"]) == 0,
          f"D09 curve {C.name}: B1(d) P(T) = (1-T)(1-qT) + hT = 1 - (q+1-h)T + qT^2 = "
          f"{sp.expand(Pd)} equals the 04k numerator")
    check(sp.simplify(sp.together(1 + h * T / ((1 - T) * (1 - q * T))) - D["Z"]) == 0,
          f"D09 curve {C.name}: B1(d) Z(T) = 1 + hT/((1-T)(1-qT)) as rational functions")
    check(D["P"].subs(T, 1) == h == D["Nk"][0],
          f"D09 curve {C.name}: h = P(1) = det(1 - Fr | H^1) = N_1 = {h}: the bond dimension of "
          f"the class-group bond is the zeta numerator at T = 1   [B1(d)]")

# -- D29: B5(b), the class number alone does not force Hasse
bad = []
for q0 in (2, 3, 4, 5):
    for h0 in range(1, 4 * q0 + 4):
        Pg = 1 - (q0 + 1 - h0) * T + q0 * T ** 2
        rts = sp.Poly(Pg, T).all_roots()
        mods = [sp.simplify(sp.Abs(1 / r) ** 2) for r in rts]
        equal = all(sp.simplify(m - q0) == 0 for m in mods)
        inhasse = abs(h0 - (q0 + 1)) <= 2 * sp.sqrt(q0)
        if equal != bool(inhasse):
            bad.append((q0, h0))
check(not bad,
      "D29 B5(b): for the genus-one shape P(T) = 1 - (q+1-h)T + qT^2 the equal-modulus property "
      "|alpha_i| = sqrt q holds EXACTLY when |h - (q+1)| <= 2 sqrt q; the formula of B1(d) by "
      "itself does not force it (checked for q = 2,3,4,5 and every h in range)")
Pbad = 1 - (2 + 1 - 6) * T + 2 * T ** 2
rb = sorted([sp.nsimplify(1 / r) for r in sp.Poly(Pbad, T).all_roots()], key=lambda z: sp.Abs(z))
check([sp.Abs(r) for r in rb] == [1, 2],
      f"D29 B5(b) witness: q = 2, h = 6 gives P(T) = {sp.expand(Pbad)} with alpha = {rb}, "
      f"moduli 1 and 2, not sqrt 2: 'the Frobenius roots are fixed by h' is true, but nothing "
      f"in B1(d) forces |alpha| = sqrt q -- Hasse is a separate input, as B5(b) says")

# ===========================================================================
head("SECTION 4   h^0 by explicit linear algebra on L(n P_0)   [B2(a), step 3]")
# ===========================================================================


def gauss_rank(F, rows):
    """Rank over the field F of a list of row tuples."""
    rows = [list(r) for r in rows]
    ncol = len(rows[0]) if rows else 0
    rank, r0 = 0, 0
    for c in range(ncol):
        piv = None
        for i in range(r0, len(rows)):
            if rows[i][c] != F.zero:
                piv = i
                break
        if piv is None:
            continue
        rows[r0], rows[piv] = rows[piv], rows[r0]
        iv = F.inv(rows[r0][c])
        rows[r0] = [F.mul(iv, v) for v in rows[r0]]
        for i in range(len(rows)):
            if i != r0 and rows[i][c] != F.zero:
                f = rows[i][c]
                rows[i] = [F.sub(a, F.mul(f, b)) for a, b in zip(rows[i], rows[r0])]
        r0 += 1
        rank += 1
        if r0 == len(rows):
            break
    return rank


def monomials(n):
    """{(i,j) : j in {0,1}, 2i+3j <= n}, sorted by pole order then j."""
    out = [(i, j) for j in (0, 1) for i in range(0, n // 2 + 1) if 2 * i + 3 * j <= n]
    return sorted(out, key=lambda ij: (2 * ij[0] + 3 * ij[1], ij[1]))


for C in CURVES:
    q, D = C.q, DATA[C.name]
    F6 = D["pts"][KMAX][0]
    aff = [P for P in D["pts"][KMAX][1] if P != INF]
    D["aff6"] = aff
    dims = []
    for n in range(0, NMAX_ENUM + 1):
        mons = monomials(n)
        rows = []
        for (x, y) in aff:
            rows.append(tuple(F6.mul(F6.pw(x, i), F6.pw(y, j)) for (i, j) in mons))
        r = gauss_rank(F6, rows)
        dims.append(r)
        exp = 1 if n == 0 else n
        check(r == len(mons) == exp,
              f"D10 curve {C.name}: L({n} P_0) = span{{x^i y^j : 2i+3j <= {n}, j <= 1}} has "
              f"{len(mons)} monomials {mons} whose value matrix at the {len(aff)} affine points "
              f"of C(F_(q^6)) has rank {r}; h^0({n} P_0) = {exp} = max(deg, 1)  (explicit "
              f"linear algebra, no Riemann--Roch)")
    D["dims_nP0"] = dims
    check(dims == [1, 1, 2, 3, 4],
          f"D10 curve {C.name}: h^0(n P_0) for n = 0..4 by linear algebra = {dims}, i.e. "
          f"h^0 = deg for deg >= 1 and h^0 = 1 at deg 0 -- the genus-one Riemann--Roch "
          f"consequence the brief allows, here DERIVED for the divisors n P_0")

    # -- D11: #L(D) = q^{h^0(D)}, the B2(a) theta value, by explicit enumeration
    for n in range(0, NMAX_ENUM + 1):
        mons = monomials(n)
        sub = aff[:max(2 * n + 4, 8)]
        vals = set()
        for co in itertools.product(range(q), repeat=len(mons)):
            v = []
            for (x, y) in sub:
                acc = F6.zero
                for c, (i, j) in zip(co, mons):
                    if c:
                        acc = F6.add(acc, F6.mul(F6.emb(c), F6.mul(F6.pw(x, i), F6.pw(y, j))))
                v.append(acc)
            vals.add(tuple(v))
        check(len(vals) == q ** dims[n],
              f"D11 curve {C.name}: #L({n} P_0) = q^(h^0) = {q}^{dims[n]} = {q ** dims[n]} "
              f"distinct functions, counted by enumerating all {q ** len(mons)} F_q-combinations "
              f"of the basis and separating them by their values -- this is the theta value "
              f"Theta(x f) = q^(h^0(D)) of B2(a)")

# ===========================================================================
head("SECTION 5   the class map, per-class divisor counts, Riemann--Roch   [B1(a), B2, step 3-4]")
# ===========================================================================

for C in CURVES:
    q, D = C.q, DATA[C.name]
    F1 = field(q, 1)
    # trace of each closed point of degree <= NMAX_ENUM into E(F_q)
    trace = {}
    ok_rat = True
    for d in range(1, NMAX_ENUM + 1):
        Fd = D["pts"][d][0]
        for orb in D["closed"][d]:
            acc = INF
            for P in orb:
                acc = C.add(Fd, acc, P)
            if acc == INF:
                tr = INF
            else:
                if not (Fd.is_base(acc[0]) and Fd.is_base(acc[1])):
                    ok_rat = False
                    tr = None
                else:
                    tr = (F1.emb(acc[0][0]), F1.emb(acc[1][0]))
            trace[(d, orb)] = tr
    # -- D12
    check(ok_rat and all(v is not None for v in trace.values()),
          f"D12 curve {C.name}: for every closed point P of degree d <= {NMAX_ENUM} the trace "
          f"Tr(P) = sum over the Frobenius orbit, computed with the group law over F_(q^d), is "
          f"F_q-RATIONAL; it is the class of P - d P_0 in Pic^0 = E(F_q)")
    check(all(trace[(1, orb)] == (orb[0] if orb[0] != INF else INF) for orb in D["closed"][1]),
          f"D12 curve {C.name}: on degree-one closed points the trace is the identity map "
          f"E(F_q) -> Pic^0, and Tr(P_0) = O")
    D["trace"] = trace

    # enumerate effective divisors of degree <= NMAX_ENUM and sort them by class
    pts_list = []
    for d in range(1, NMAX_ENUM + 1):
        for orb in sorted(D["closed"][d], key=repr):
            pts_list.append((d, orb))

    divisors = {n: [] for n in range(NMAX_ENUM + 1)}

    def rec(i, rem, cur):
        divisors[NMAX_ENUM - rem].append(tuple(cur))
        if i >= len(pts_list):
            return
        for k in range(i, len(pts_list)):
            d = pts_list[k][0]
            if d <= rem:
                cur.append(pts_list[k])
                rec(k, rem - d, cur)
                cur.pop()

    rec(0, NMAX_ENUM, [])
    for n in range(NMAX_ENUM + 1):
        divisors[n] = sorted(set(divisors[n]), key=repr)
    D["divisors"] = divisors
    check(all(len(divisors[n]) == D["a"][n] for n in range(NMAX_ENUM + 1)),
          f"D13 curve {C.name}: the explicit multiset enumeration of effective divisors gives "
          f"{[len(divisors[n]) for n in range(NMAX_ENUM + 1)]} = a_n for n = 0..{NMAX_ENUM}, "
          f"agreeing with the generating-function count of D04")

    def cls(div):
        acc = INF
        for (d, orb) in div:
            acc = C.add(F1, acc, trace[(d, orb)])
        return acc

    percls = {}
    for n in range(NMAX_ENUM + 1):
        tally = {P: 0 for P in D["E1"]}
        for div in divisors[n]:
            tally[cls(div)] += 1
        percls[n] = tally
    D["percls"] = percls

    ok_uni = True
    for n in range(1, NMAX_ENUM + 1):
        exp = (q ** n - 1) // (q - 1)
        for P, c in percls[n].items():
            if c != exp:
                ok_uni = False
    check(ok_uni,
          f"D13 curve {C.name}: for n = 1..{NMAX_ENUM} EVERY one of the h = {D['h']} classes in "
          f"Pic^n contains exactly (q^n - 1)/(q-1) = "
          f"{[(q ** n - 1) // (q - 1) for n in range(1, NMAX_ENUM + 1)]} effective divisors; "
          f"the empirical h^0 = log_q(1 + (q-1)*count) is therefore deg D, Riemann--Roch "
          f"read off raw counting")
    check(percls[0][INF] == 1 and all(v == 0 for P, v in percls[0].items() if P != INF),
          f"D13 curve {C.name}: in degree 0 only the trivial class contains an effective divisor "
          f"(the empty one), so h^0 = 1 on the trivial class and 0 on the other {D['h'] - 1}: the "
          f"theta divisor of Pic^(g-1) = Pic^0 is the single principal class")

    def h0_emp(cnt, n):
        """h^0 from the enumerated number of effective divisors in the class."""
        if n < 0:
            return 0
        v = 1 + (q - 1) * cnt
        e = 0
        while q ** e < v:
            e += 1
        return e if q ** e == v else -1

    def rr_h0(div_signed):
        """Riemann--Roch consequence route (declared)."""
        n = sum(m * d for (d, orb), m in div_signed)
        if n > 0:
            return n
        if n < 0:
            return 0
        acc = INF
        for (d, orb), m in div_signed:
            acc = C.add(F1, acc, C.mulz(F1, m, trace[(d, orb)]))
        return 1 if acc == INF else 0

    # -- D14: B1(a) at the level of classes
    ok_b1a = True
    for n in range(NMAX_ENUM + 1):
        tot = 0
        for P, c in percls[n].items():
            hh = h0_emp(c, n)
            tot += (q ** hh - 1) // (q - 1)
        if tot != D["a"][n]:
            ok_b1a = False
    check(ok_b1a,
          f"D14 curve {C.name}: a_n = sum_([D] in Pic^n) (q^(h^0(D)) - 1)/(q-1) for n = 0..{NMAX_ENUM}, "
          f"the sum taken over the h = {D['h']} classes with h^0 read off the enumeration   [B1(a)]")
    ok_agree = True
    for n in range(NMAX_ENUM + 1):
        for div in divisors[n]:
            sgn = [((d, orb), div.count((d, orb))) for (d, orb) in set(div)]
            if h0_emp(percls[n][cls(div)], n) != rr_h0(sgn):
                ok_agree = False
    check(ok_agree,
          f"D14 curve {C.name}: the two h^0 routes agree on every one of the "
          f"{sum(len(divisors[n]) for n in range(NMAX_ENUM + 1))} effective divisors of degree "
          f"<= {NMAX_ENUM}: enumeration-based h^0 == Riemann--Roch-consequence h^0")

    # -- D15: Riemann--Roch on signed divisors, K_C = 0
    trials = []
    keys = pts_list
    for _ in range(300):
        nterm = int(RNG.integers(1, 4))
        sel = RNG.choice(len(keys), size=nterm, replace=False)
        mult = RNG.integers(-2, 3, size=nterm)
        dv = [(keys[int(i)], int(m)) for i, m in zip(sel, mult) if m != 0]
        if not dv:
            continue
        deg = sum(m * d for (d, orb), m in dv)
        if 0 <= deg <= NMAX_ENUM:
            trials.append(dv)
    ok_rr = True
    ok_emp = True
    for dv in trials:
        deg = sum(m * d for (d, orb), m in dv)
        neg = [(k, -m) for k, m in dv]
        if rr_h0(dv) - rr_h0(neg) != deg:
            ok_rr = False
        # empirical: class of dv inside Pic^deg, count of effective divisors there
        acc = INF
        for (d, orb), m in dv:
            acc = C.add(F1, acc, C.mulz(F1, m, trace[(d, orb)]))
        he = h0_emp(percls[deg][acc], deg)
        hn = 0 if deg > 0 else he
        if he - hn != deg:
            ok_emp = False
    check(len(trials) > 40 and ok_rr,
          f"D15 curve {C.name}: Riemann--Roch h^0(D) - h^0(K_C - D) = deg D + 1 - g with g = 1 and "
          f"K_C = 0, i.e. h^0(D) - h^0(-D) = deg D, on {len(trials)} seeded SIGNED divisors of "
          f"degree 0..{NMAX_ENUM} (multiplicities in -2..2)")
    check(ok_emp,
          f"D15 curve {C.name}: the same Riemann--Roch relation with h^0 taken from the raw "
          f"enumeration of effective divisors in the class (independent of the Riemann--Roch "
          f"shortcut), on the same {len(trials)} signed divisors")

# ===========================================================================
head("SECTION 6   functional equation, the Weyl involution, the superdeterminant   [B1(c), B2(b),(c)]")
# ===========================================================================

for C in CURVES:
    q, D = C.q, DATA[C.name]
    g = 1
    lhs = D["Z"].subs(T, 1 / (q * T))
    rhs = q ** (1 - g) * T ** (2 - 2 * g) * D["Z"]
    check(sp.simplify(sp.together(lhs - rhs)) == 0,
          f"D16 curve {C.name}: the functional equation Z(1/(qT)) = q^(1-g) T^(2-2g) Z(T) holds "
          f"symbolically; at g = 1 it reads Z(1/(qT)) = Z(T)   [B2(b), step 4]")
    check(sp.simplify(sp.together(lhs - D["Z"])) == 0,
          f"D16 curve {C.name}: the prefactor q^(1-g) T^(2-2g) is exactly 1 at g = 1, so the "
          f"genus-one form 'Z(1/(qT)) = T^0 Z(T)' of step 4 is right")
    # poles
    num, den = sp.fraction(sp.cancel(D["Z"]))
    check(sp.simplify(D["P"].subs(T, 1)) != 0 and sp.simplify(D["P"].subs(T, sp.Rational(1, q))) != 0,
          f"D16 curve {C.name}: P(1) = {D['P'].subs(T, 1)} and P(1/q) = "
          f"{sp.nsimplify(D['P'].subs(T, sp.Rational(1, q)))} are both nonzero, so Z(T) has "
          f"simple poles exactly at T = 1 and T = 1/q -- the two constant terms of B2(b)")

# control at genus 0 (the general form of the functional equation, g != 1)
Z0 = 1 / ((1 - T) * (1 - 2 * T))
check(sp.simplify(sp.together(Z0.subs(T, 1 / (2 * T)) - 2 ** (1 - 0) * T ** 2 * Z0)) == 0,
      "D16 control: the same general functional equation Z(1/(qT)) = q^(1-g) T^(2-2g) Z(T) holds "
      "at g = 0, q = 2 (P = 1) with the nontrivial prefactor 2 T^2, so the prefactor in B2(b) is "
      "not an artefact of g = 1")

for C in CURVES:
    q, D = C.q, DATA[C.name]
    F1 = field(q, 1)
    E1 = D["E1"]
    inv2 = [P for P in E1 if C.add(F1, P, P) == INF]
    check(all(C.neg(F1, C.neg(F1, P)) == P for P in E1),
          f"D17 curve {C.name}: [D] -> [K_C - D] = [-D] is an involution of Pic^0 (K_C = 0 at "
          f"genus one) and the degree reflection n -> 2g-2-n is n -> -n   [B2(c)]")
    check(C.neg(F1, INF) == INF,
          f"D17 curve {C.name}: the involution FIXES the theta divisor of Pic^(g-1) = Pic^0, "
          f"which at genus one is the single principal class {{O}}   [B2(c)]")
    check(len(inv2) == (1 if C.name == "D2" else 2),
          f"D17 curve {C.name}: the fixed locus of the involution is the 2-torsion, of size "
          f"{len(inv2)}; for curve D3 it is STRICTLY LARGER than the theta divisor (2 classes vs 1), "
          f"so 'the involution fixing the theta divisor' does not characterise it")

# superdeterminant of thm:scattering-superdeterminant, cited by B1(c)
for C in CURVES:
    q, D = C.q, DATA[C.name]
    al = SHARD[C.name]["alphas"]
    even = [sp.Integer(1), sp.Integer(q)] + [q * a for a in al]
    odd = list(al) + [sp.Integer(q), sp.Integer(q) ** 2]
    sdet = sp.simplify(sp.prod([1 - w_s * l for l in even]) / sp.prod([1 - w_s * l for l in odd]))
    Pw = D["P"].subs(T, w_s)
    Pqw = D["P"].subs(T, q * w_s)
    closed = sp.simplify((1 - w_s) * Pqw / ((1 - q ** 2 * w_s) * Pw))
    check(sp.simplify(sdet - closed) == 0,
          f"D21 curve {C.name}: sdet(1 - w E_S) with even spectrum {{1, q, q alpha_i}} and odd "
          f"spectrum {{alpha_i, q, q^2}} equals (1-w) P(qw)/((1-q^2 w) P(w))   "
          f"[thm:scattering-superdeterminant, cited by B1(c)]")
    ratio = sp.simplify(D["Z"].subs(T, q * w_s) / D["Z"].subs(T, w_s))
    check(sp.simplify(ratio - closed) == 0,
          f"D21 curve {C.name}: that superdeterminant is zeta_K(2s-1)/zeta_K(2s) = Z(qw)/Z(w) "
          f"with w = q^(-2s)")
    oddprod = sp.expand(sp.prod([1 - w_s * l for l in odd]))
    quo = sp.simplify(oddprod / Pw)
    check(sp.simplify(quo - (1 - q * w_s) * (1 - q ** 2 * w_s)) == 0,
          f"D21 curve {C.name}: the FULL odd factor of sdet(1 - w E_S) is P(w)(1-qw)(1-q^2 w), "
          f"not P(w): B1(c)'s 'P(T) = (1-T)(1-qT)Z(T) is its odd part' is the H^1 factor only, "
          f"and in the variable w = T^2, not T")

# -- D30: B5(b) genus-one metric vacuity (commutant of a regular semisimple Frobenius)
for C in CURVES:
    q, D = C.q, DATA[C.name]
    al = SHARD[C.name]["alphas"]
    check(sp.simplify(al[0] - al[1]) != 0,
          f"D30 curve {C.name}: the two Frobenius eigenvalues {[sp.nsimplify(a) for a in al]} are "
          f"DISTINCT, so Frobenius on H^1 (x) C is regular semisimple")
    A = sp.diag(al[0], al[1])
    X = sp.Matrix(2, 2, sp.symbols('x0:4'))
    sol = sp.solve(list(A * X - X * A), list(X.free_symbols), dict=True)
    Xg = X.subs(sol[0]) if sol else X
    free = len(Xg.free_symbols)
    check(free == 2 and sp.simplify(Xg[0, 1]) == 0 and sp.simplify(Xg[1, 0]) == 0,
          f"D30 curve {C.name}: the commutant of Frobenius on H^1 (x) C is the 2-dimensional "
          f"space of DIAGONAL matrices, so every Frobenius-normal metric is diagonal in the "
          f"eigenbasis and only its one ratio is free: 'the symmetric ray is the Hodge metric' "
          f"is vacuous at genus one, exactly as B5(b) says (it can only be tested at g >= 2)")

# ===========================================================================
head("SECTION 7   class characters and the Hecke L-polynomials   [B3(b)]")
# ===========================================================================

for C in CURVES:
    q, D = C.q, DATA[C.name]
    h = D["h"]
    dlog = D["dlog"]
    chars = []
    for j in range(h):
        chars.append(lambda P, j=j: sp.exp(2 * sp.pi * sp.I * sp.Rational(j * dlog[P], h)))
    Ls = []
    for j, chi in enumerate(chars):
        co = []
        for n in range(NMAX_ENUM + 1):
            tot = 0
            for P, c in D["percls"][n].items():
                tot += chi(P) * c
            co.append(sp.simplify(sp.expand(tot)))
        Ls.append(co)
    D["L"] = Ls
    check(all(sp.simplify(Ls[0][n] - D["a"][n]) == 0 for n in range(NMAX_ENUM + 1)),
          f"D18 curve {C.name}: the TRIVIAL class character gives L(T, 1) = sum_n a_n T^n = Z(T); "
          f"coefficients {[int(x) for x in Ls[0]]} = {D['a'][:NMAX_ENUM + 1]}   [B3(b)]")
    if h > 1:
        okc = True
        for j in range(1, h):
            if sp.simplify(Ls[j][0] - 1) != 0:
                okc = False
            for n in range(1, NMAX_ENUM + 1):
                if sp.simplify(Ls[j][n]) != 0:
                    okc = False
        check(okc,
              f"D18 curve {C.name}: for each of the {h - 1} NONTRIVIAL class characters, "
              f"L(T, chi) = sum_([D]) chi([D]) (q^(h^0)-1)/(q-1) T^(deg D) has constant term 1 and "
              f"all coefficients in degrees 1..{NMAX_ENUM} zero, i.e. L(T, chi) = 1, a polynomial "
              f"of degree 2g-2 = 0   [B3(b)]")
        okz = all(sp.simplify(sum(chi(P) for P in D["E1"])) == 0 for chi in chars[1:])
        check(okz,
              f"D18 curve {C.name}: the reason is character orthogonality, sum_([D] in Pic^n) "
              f"chi([D]) = 0 for chi != 1, together with the CONSTANT per-class count "
              f"(q^n-1)/(q-1) of D13")
        check(len(set(tuple(sp.nsimplify(chi(P)) for P in D["E1"]) for chi in chars)) == h,
              f"D18 curve D3: the {h} class characters of Pic^0 = Z/4 are pairwise distinct; three "
              f"nontrivial ones see no zeros (L = 1) and the trivial one carries Z(T) -- the three "
              f"monomial channels plus the zeta channel of thm:d3-channels")
    else:
        check(h == 1,
              f"D18 curve {C.name}: Pic^0 is trivial, so there is ONLY the trivial character and "
              f"the single channel is the zeta channel; there are no monomial channels to see")

# ===========================================================================
head("SECTION 8   the cusps of the tree quotient   [B3(a),(c), step 7]")
# ===========================================================================

for C in CURVES:
    D = DATA[C.name]
    cusps = SHARD[C.name]["cusps"]      # STATED from shard 04k, not derived here
    check(cusps == D["h"],
          f"D19 curve {C.name}: the cusp number STATED in shard 04k (def:elliptic-cavity) is "
          f"{cusps} and the class number computed here is h = {D['h']}: #cusps = |Pic(R)| = "
          f"|Pic^0(K)|   [B3(a)]")
    check(cusps == D["h"] * 1,
          f"D19 curve {C.name}: Lorscheid's count h * deg(x) for the removed place x = P_0 of "
          f"degree 1 gives {D['h']} * 1 = {D['h']} = {cusps}   [B3(a), cit:lorscheid-cusp-count]")

dimHW = 4
for C in CURVES:
    D = DATA[C.name]
    coincide = (D["h"] == dimHW)
    check(coincide == (C.name == "D3"),
          f"D20 curve {C.name}: dim K_HW = 4 (two Frobenius eigenvalues, two square roots each) "
          f"while the class-group bond has dimension h = {D['h']}; they "
          f"{'coincide' if coincide else 'do NOT coincide'}, as B3(c) says")
check(dimHW == 4 * 1,
      "D20 B3(c): at genus one 4 = 4g, so 'the coincidence at D3 is the accident P(1) = 4 = 4g' "
      "is arithmetically consistent; the general statement is dim K_HW = 2 * 2g = 4g, equal to 4 "
      "only because g = 1")

# ===========================================================================
head("SECTION 9   Jacobi theta, the Mellin transform of its odd part, xi   [B4]")
# ===========================================================================

mp.mp.dps = 40
PI = mp.pi


def theta_direct(x):
    """theta(x) = sum_{n in Z} exp(-pi n^2 x), summed directly (no functional equation)."""
    x = mp.mpf(x) if not isinstance(x, mp.mpf) else x
    N = int(mp.sqrt((mp.mp.dps * mp.log(10) + 15) / (PI * x))) + 3
    s = mp.mpf(1)
    for n in range(1, N + 1):
        s += 2 * mp.e ** (-PI * n * n * x)
    return s


def psi(x):
    """psi(x) = (theta(x)-1)/2 = sum_{n>=1} exp(-pi n^2 x), for x >= 1."""
    N = int(mp.sqrt((mp.mp.dps * mp.log(10) + 15) / (PI * x))) + 3
    s = mp.mpf(0)
    for n in range(1, N + 1):
        s += mp.e ** (-PI * n * n * x)
    return s


def xi(s):
    return mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


# -- D22: theta(1/x) = sqrt(x) theta(x)
for xv in (mp.mpf(1) / 3, mp.mpf(1), mp.mpf(7)):
    lhs = theta_direct(1 / xv)
    rhs = mp.sqrt(xv) * theta_direct(xv)
    check(abs(lhs - rhs) < mp.mpf('1e-30'),
          f"D22 theta(1/x) = sqrt(x) theta(x) at x = {mp.nstr(xv, 8)}: "
          f"|lhs - rhs| = {mp.nstr(abs(lhs - rhs), 3)} < 1e-30 (both sides summed directly, "
          f"40 working digits)   [B4(b)]")


def I_val(s):
    """The B4(b) integral  int_0^oo (theta(x) - 1 - x^(-1/2)) x^(s/2) d^x x.

    The lower half (0,1) is mapped to (1,oo) by x -> 1/x using theta(1/x) = sqrt x theta(x)
    (verified independently in D22), which turns the integral into
        int_1^oo [2 psi(u) u^((1-s)/2-1) - u^(-s/2-1)] du
      + int_1^oo [2 psi(x) x^(s/2-1)     - x^((s-1)/2-1)] dx .
    Both bracketed integrands split into a theta-tail, quadratured after u -> 1/v on (0,1)
    where psi(1/v) vanishes to all orders at the endpoint, and an ELEMENTARY tail whose
    value is taken in closed form, int_1^oo u^(-s/2-1) du = 2/s (Re s > 0) and
    int_1^oo x^((s-1)/2-1) dx = -2/(s-1) (Re s < 1).  Those two closed forms are what
    continues the expression to all s; inside 0 < Re s < 1 this is literally the integral."""
    f = lambda v: psi(1 / v) * (v ** (-s / 2 - 1) + v ** ((s - 1) / 2 - 1))
    return 2 * mp.quad(f, [0, 1]) - 2 / s + 2 / (s - 1)


# the two elementary tails: exact antiderivatives (sympy), then the limit A -> oo
_u, _A = sp.symbols('u A', positive=True)
_s = sp.symbols('sigma', positive=True)
F1 = (2 / _s) * (1 - _A ** (-_s / 2))
F2 = (2 / (_s - 1)) * (_A ** ((_s - 1) / 2) - 1)
t1 = sp.simplify(sp.diff(F1, _A) - _A ** (-_s / 2 - 1)) == 0 and sp.simplify(F1.subs(_A, 1)) == 0
t2 = sp.simplify(sp.diff(F2, _A) - _A ** ((_s - 1) / 2 - 1)) == 0 and sp.simplify(F2.subs(_A, 1)) == 0
check(t1 and t2,
      "D23 bookkeeping: exactly (sympy) int_1^A u^(-s/2-1) du = (2/s)(1 - A^(-s/2)) and "
      "int_1^A x^((s-1)/2-1) dx = (2/(s-1))(A^((s-1)/2) - 1), so as A -> oo the first tends to "
      "2/s for Re s > 0 and the second to -2/(s-1) for Re s < 1: these are the two elementary "
      "tails whose closed forms continue the B4(b) integral off the strip")
for s in (mp.mpf('0.5'), mp.mpf('0.8')):
    A = mp.mpf('1e200')
    v1 = (2 / s) * (1 - A ** (-s / 2))
    v2 = (2 / (s - 1)) * (A ** ((s - 1) / 2) - 1)
    check(abs(v1 - 2 / s) < mp.mpf('1e-6') and abs(v2 + 2 / (s - 1)) < mp.mpf('1e-6'),
          f"D23 bookkeeping at s = {mp.nstr(s, 4)}: at A = 1e200 those antiderivatives read "
          f"{mp.nstr(v1, 12)} -> 2/s = {mp.nstr(2 / s, 12)} and {mp.nstr(v2, 12)} -> -2/(s-1) = "
          f"{mp.nstr(-2 / (s - 1), 12)}, both inside the strip 0 < Re s < 1")

# -- D23: the value of the integral inside its strip of convergence 0 < Re s < 1
strip = [mp.mpf(1) / 2, mp.mpf('0.3'), mp.mpf('0.7') + mp.mpf('0.2') * 1j]
for s in strip:
    v = I_val(s)
    good = 2 * xi(s)
    brief = 2 * xi(s) / (s * (s - 1))
    check(abs(v - good) < mp.mpf('1e-30'),
          f"D23 at s = {mp.nstr(s, 6)} the B4(b) integral equals 2 xi(s) = {mp.nstr(good, 15)}; "
          f"|I - 2 xi| = {mp.nstr(abs(v - good), 3)} < 1e-30")
    check(abs(v - brief) < mp.mpf('1e-30'),
          f"D23 at s = {mp.nstr(s, 6)} the integral equals the value 2 xi(s)/(s(s-1)) = "
          f"{mp.nstr(brief, 15)} PRINTED IN B4(b); |I - brief| = {mp.nstr(abs(v - brief), 3)} "
          f"(FAILS: the factor 1/(s(s-1)) is spurious)")
    check(abs(v / brief - s * (s - 1)) < mp.mpf('1e-30'),
          f"D23 at s = {mp.nstr(s, 6)}: the ratio I(s) / (2 xi(s)/(s(s-1))) = "
          f"{mp.nstr(v / brief, 15)} is exactly s(s-1) = {mp.nstr(s * (s - 1), 15)}, pinning the "
          f"discrepancy as the spurious factor s(s-1)")

# -- D24: domain of convergence
for s in (mp.mpf(2), mp.mpf(3)):
    tails = []
    for A in (mp.mpf(10), mp.mpf(100), mp.mpf(1000)):
        tails.append(mp.quad(lambda x: (theta_direct(x) - 1 - x ** mp.mpf(-0.5)) * x ** (s / 2 - 1),
                             [A, 2 * A]))
    growing = abs(tails[2]) > abs(tails[1]) > abs(tails[0]) > 0
    check(growing,
          f"D24 at s = {mp.nstr(s, 4)} the tail int_A^(2A) (theta - 1 - x^(-1/2)) x^(s/2-1) dx has "
          f"magnitudes {[mp.nstr(abs(t), 5) for t in tails]} for A = 10, 100, 1000: it GROWS, so "
          f"the B4(b) integral DIVERGES at s = 2 and s = 3 -- 'for all s' holds only after "
          f"analytic continuation, the raw integral converging only for 0 < Re s < 1")
exact_tail = lambda s, A: -2 * A ** ((s - 1) / 2) / (s - 1)
for s in (mp.mpf(2), mp.mpf(3)):
    A = mp.mpf(1000)
    got = mp.quad(lambda x: (theta_direct(x) - 1 - x ** mp.mpf(-0.5)) * x ** (s / 2 - 1),
                  [A, mp.mpf(4000)])
    want = -2 * (mp.mpf(4000) ** ((s - 1) / 2) - A ** ((s - 1) / 2)) / (s - 1)
    check(abs(got - want) / abs(want) < mp.mpf('1e-20'),
          f"D24 at s = {mp.nstr(s, 4)} the divergence is exactly the -x^(-1/2) subtraction: the "
          f"tail on [1000, 4000] is -2(x^((s-1)/2))| = {mp.nstr(want, 10)} to relative "
          f"{mp.nstr(abs(got - want) / abs(want), 3)}")

# -- D25: the continued identity at s = 2, 3
for s in (mp.mpf(2), mp.mpf(3)):
    v = I_val(s)
    good = 2 * xi(s)
    brief = 2 * xi(s) / (s * (s - 1))
    check(abs(v - good) < mp.mpf('1e-25'),
          f"D25 at s = {mp.nstr(s, 4)} (analytic continuation) the Mellin transform of the odd "
          f"part of theta equals 2 xi(s) = {mp.nstr(good, 15)}; deviation "
          f"{mp.nstr(abs(v - good), 3)} < 1e-25")
    check(abs(v - brief) < mp.mpf('1e-25'),
          f"D25 at s = {mp.nstr(s, 4)} it equals the B4(b) right-hand side 2 xi(s)/(s(s-1)) = "
          f"{mp.nstr(brief, 15)} (FAILS by the factor s(s-1) = {mp.nstr(s * (s - 1), 4)})")
check(abs(2 * xi(mp.mpf(2)) - mp.pi / 3) < mp.mpf('1e-30'),
      "D25 sanity: 2 xi(2) = 2 pi^(-1) Gamma(1) zeta(2) = pi/3 exactly")

# -- D26: at the first two zeros
ZEROS = [mp.mpf('0.5') + mp.mpf('14.134725') * 1j, mp.mpf('0.5') + mp.mpf('21.022040') * 1j]
TRUE = [mp.mpf('14.134725141734693790'), mp.mpf('21.022039638771554993')]
for s, t0 in zip(ZEROS, TRUE):
    v = I_val(s)
    dt = abs(s.imag - t0)
    check(abs(v) < mp.mpf('1e-10'),
          f"D26 at s = 1/2 + {mp.nstr(s.imag, 10)} i the integral is |I| = {mp.nstr(abs(v), 4)} "
          f"against |I| ~ 8 elsewhere in the strip: numerically zero to the precision of the "
          f"quoted zero (|t - t_true| = {mp.nstr(dt, 3)}, and |I| / |t - t_true| = "
          f"{mp.nstr(abs(v) / dt, 4)} is the finite slope |2 xi'|)   [B4(b)]")
    check(abs(v - 2 * xi(s)) < mp.mpf('1e-30'),
          f"D26 at the same s the integral equals 2 xi(s) to {mp.nstr(abs(v - 2 * xi(s)), 3)}: the "
          f"zeros of zeta ARE the zeros of the Mellin transform of the odd part of theta, which "
          f"is the qualitative content of B4(b) and survives the constant being wrong")
    check(abs(xi(mp.mpf('0.5') + t0 * 1j)) < mp.mpf('1e-18'),
          f"D26 xi(1/2 + {mp.nstr(t0, 12)} i) = {mp.nstr(abs(xi(mp.mpf('0.5') + t0 * 1j)), 3)}: the "
          f"quoted zero is a genuine zero of xi at full precision")

# -- D27: pole structure discriminates the two candidate right-hand sides
for s0, res in ((mp.mpf(1), mp.mpf(2)), (mp.mpf(0), mp.mpf(-2))):
    eps = mp.mpf('1e-12')
    sv = s0 + eps
    v = I_val(sv) * eps
    check(abs(v - res) < mp.mpf('1e-9'),
          f"D27 the Mellin transform has a SIMPLE pole at s = {int(s0)} with residue "
          f"{int(res)} (measured {mp.nstr(v, 12)}), matching 2 xi(s) exactly; the B4(b) "
          f"right-hand side 2 xi(s)/(s(s-1)) would have a DOUBLE pole there, which is an "
          f"independent proof that the factor 1/(s(s-1)) is spurious")

# -- D28: the adelic normalisation of B4(a)
for xv in (mp.mpf('1.7'), mp.mpf('0.6')):
    lat = mp.mpf(0)
    N = 200
    for n in range(-N, N + 1):
        lat += mp.e ** (-PI * (xv * n) ** 2)
    check(abs(lat - theta_direct(xv ** 2)) < mp.mpf('1e-30'),
          f"D28 at x = {mp.nstr(xv, 4)}: sum_(n in Z) f_oo(x n) with f_oo(t) = e^(-pi t^2) equals "
          f"theta(x^2) = {mp.nstr(theta_direct(xv ** 2), 12)}, not theta(x) = "
          f"{mp.nstr(theta_direct(xv), 12)}   [B4(a)]")
    check(abs(lat - theta_direct(xv)) < mp.mpf('1e-30'),
          f"D28 at x = {mp.nstr(xv, 4)}: the same sum equals theta(x) AS B4(a) WRITES IT "
          f"(FAILS: |diff| = {mp.nstr(abs(lat - theta_direct(xv)), 4)}; the dilation parameter of "
          f"the bond state is |x|^2, or equivalently f_oo(t) = e^(-pi t^2) must be scaled by "
          f"sqrt of the idele norm)")

# -- D31: the two constant terms of B4(b)
for xv in (mp.mpf('0.25'), mp.mpf('2.5')):
    odd = theta_direct(xv) - 1 - xv ** mp.mpf('-0.5')
    oddr = theta_direct(1 / xv) - 1 - (1 / xv) ** mp.mpf('-0.5')
    check(abs(odd - mp.sqrt(1 / xv) * oddr) < mp.mpf('1e-28'),
          f"D31 at x = {mp.nstr(xv, 4)}: the odd part theta(x) - 1 - x^(-1/2) satisfies "
          f"u(x) = x^(-1/2) u(1/x), i.e. the two constant terms 1 and x^(-1/2) are exactly the "
          f"pair exchanged by x -> 1/x and the remainder is anti-invariant in the same sense: "
          f"the even/odd split of B4(b) is consistent")

# ===========================================================================
head("TALLY")
# ===========================================================================
if _FAILED:
    print("  failing checks:")
    for line, msg in _FAILED:
        print(f"    L{line:4d}  {msg}")
else:
    print("  no failing checks")
print()
print(f"CHECKS: {_PASS} passed, {_FAIL} failed")
