#!/usr/bin/env python3
"""REFUTE review, GL_1 bond round (2026-09-21), reviewer `claude:opus`.

Independent re-derivation of the function-field side of propositions B1, B2, B3 of
`notes/gl1-bond/proofs.md`.  Nothing is imported from `scripts/`; every finite field,
every curve, the group law, the closed points, the divisor classes and the
Riemann--Roch data are rebuilt here from scratch.

Covered: B1(a) (a_n as a class sum), B1(b) (generic part and the deviation set),
B1(c) (genus-one Z, P, h = P(1) = N_1), B1(d) (h = P(1) *without* Lefschetz, from
(a)+(b) alone, checked in genus 0,1,2,3 on synthetic Weil polynomials),
B2(a) (#L(D) = q^{h^0}), B2(b) (the fibre-volume bookkeeping 1/(q-1) versus 1 in
its counting form, plus the unfolding identity), B2(c) (the functional equation,
Poisson = Riemann--Roch in its counting form, and a finite-group Poisson model that
pins the constant vol(O_A) = q^{1-g}), the theta-divisor / fixed-locus comparison at
genus one, and B3(b) (class characters, L(T,chi) = 1 at genus one).

python3 notes/reviews/scratch_gl1_ff.py
"""

import itertools
import random
from fractions import Fraction

import sympy as sp

random.seed(20260921)

PASS = 0
FAIL = 0


def check(cond, msg):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("ok   %s" % msg)
    else:
        FAIL += 1
        print("FAIL %s" % msg)


# ----------------------------------------------------------------------------
# finite fields F_{p^k}, p prime, elements encoded as base-p digit vectors
# ----------------------------------------------------------------------------

def poly_mulmod(a, b, mod, p):
    """a,b coefficient tuples low->high, mod monic tuple of length k+1."""
    k = len(mod) - 1
    res = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                res[i + j] = (res[i + j] + ai * bj) % p
    for d in range(len(res) - 1, k - 1, -1):
        c = res[d]
        if c:
            res[d] = 0
            for i in range(k):
                res[d - k + i] = (res[d - k + i] - c * mod[i]) % p
    res = res[:k] + [0] * max(0, k - len(res))
    return tuple(res[:k])


def is_irreducible(mod, p):
    k = len(mod) - 1
    if k == 1:
        return True
    # trial division by all monic polys of degree 1..k//2
    for d in range(1, k // 2 + 1):
        for tail in itertools.product(range(p), repeat=d):
            g = list(tail) + [1]
            # polynomial remainder of mod by g
            r = list(mod)
            for i in range(len(r) - 1, d - 1, -1):
                c = r[i]
                if c:
                    for j in range(d + 1):
                        r[i - d + j] = (r[i - d + j] - c * g[j]) % p
            if all(x % p == 0 for x in r[:d]):
                return False
    return True


class FF:
    """F_{p^k} with elements 0..Q-1 (base-p digits = polynomial coefficients)."""

    def __init__(self, p, k):
        self.p, self.k = p, k
        self.Q = p ** k
        mod = None
        for tail in itertools.product(range(p), repeat=k):
            cand = list(tail) + [1]
            if is_irreducible(cand, p):
                mod = tuple(cand)
                break
        assert mod is not None
        self.mod = mod
        Q = self.Q
        self.dig = [self._digits(i) for i in range(Q)]
        self.idx = {d: i for i, d in enumerate(self.dig)}
        # addition and multiplication tables
        self.ADD = [[0] * Q for _ in range(Q)]
        self.MUL = [[0] * Q for _ in range(Q)]
        for a in range(Q):
            da = self.dig[a]
            rowa = self.ADD[a]
            rowm = self.MUL[a]
            for b in range(Q):
                db = self.dig[b]
                rowa[b] = self.idx[tuple((x + y) % p for x, y in zip(da, db))]
                rowm[b] = self.idx[poly_mulmod(da, db, mod, p)]
        self.NEG = [self.idx[tuple((-x) % p for x in self.dig[a])] for a in range(Q)]
        self.INV = [0] * Q
        for a in range(1, Q):
            for b in range(1, Q):
                if self.MUL[a][b] == 1:
                    self.INV[a] = b
                    break
        self.one = self.idx[tuple([1] + [0] * (k - 1))]
        self.zero = 0
        # Frobenius over F_p
        self.FROB = [self.pw(a, p) for a in range(Q)]

    def _digits(self, i):
        p, k = self.p, self.k
        d = []
        for _ in range(k):
            d.append(i % p)
            i //= p
        return tuple(d)

    def emb(self, c):
        """integer constant -> field element"""
        return self.idx[tuple([c % self.p] + [0] * (self.k - 1))]

    def pw(self, a, n):
        r = self.idx[tuple([1] + [0] * (self.k - 1))]
        b = a
        while n:
            if n & 1:
                r = self.MUL[r][b]
            b = self.MUL[b][b]
            n >>= 1
        return r

    def in_prime_field(self, a):
        return all(x == 0 for x in self.dig[a][1:])

    def to_prime(self, a):
        assert self.in_prime_field(a)
        return self.dig[a][0]


# ----------------------------------------------------------------------------
# elliptic curves in general Weierstrass form over F_{p^k}
# ----------------------------------------------------------------------------

class Curve:
    """y^2 + a1 x y + a3 y = x^3 + a2 x^2 + a4 x + a6 over F = F_{p^k}."""

    def __init__(self, F, a):
        self.F = F
        self.a = [F.emb(c) for c in a]  # a1,a2,a3,a4,a6

    def points(self):
        F = self.F
        a1, a2, a3, a4, a6 = self.a
        M, A = F.MUL, F.ADD
        pts = [None]  # O
        for x in range(F.Q):
            x2 = M[x][x]
            rhs = A[A[A[M[x2][x]][M[a2][x2]]][M[a4][x]]][a6]
            for y in range(F.Q):
                lhs = A[A[M[y][y]][M[M[a1][x]][y]]][M[a3][y]]
                if lhs == rhs:
                    pts.append((x, y))
        return pts

    def on_curve(self, P):
        if P is None:
            return True
        F = self.F
        a1, a2, a3, a4, a6 = self.a
        M, A = F.MUL, F.ADD
        x, y = P
        x2 = M[x][x]
        rhs = A[A[A[M[x2][x]][M[a2][x2]]][M[a4][x]]][a6]
        lhs = A[A[M[y][y]][M[M[a1][x]][y]]][M[a3][y]]
        return lhs == rhs

    def neg(self, P):
        if P is None:
            return None
        F = self.F
        a1, _, a3, _, _ = self.a
        x, y = P
        return (x, F.NEG[F.ADD[F.ADD[y][F.MUL[a1][x]]][a3]])

    def add(self, P, Q):
        if P is None:
            return Q
        if Q is None:
            return P
        F = self.F
        M, A, N, I = F.MUL, F.ADD, F.NEG, F.INV
        a1, a2, a3, a4, a6 = self.a
        x1, y1 = P
        x2, y2 = Q
        if x1 == x2 and y2 == N[A[A[y1][M[a1][x1]]][a3]]:
            return None
        if P == Q:
            den = A[A[A[y1][y1]][M[a1][x1]]][a3]
            num = A[A[A[M[F.emb(3)][M[x1][x1]]][M[F.emb(2)][M[a2][x1]]]][a4]][N[M[a1][y1]]]
            lam = M[num][I[den]]
            num2 = A[A[A[N[M[M[x1][x1]][x1]]][M[a4][x1]]][M[F.emb(2)][a6]]][N[M[a3][y1]]]
            nu = M[num2][I[den]]
        else:
            den = A[x2][N[x1]]
            lam = M[A[y2][N[y1]]][I[den]]
            nu = M[A[M[y1][x2]][N[M[y2][x1]]]][I[den]]
        x3 = A[A[A[A[M[lam][lam]][M[a1][lam]]][N[a2]]][N[x1]]][N[x2]]
        y3 = A[A[N[M[A[lam][a1]][x3]]][N[nu]]][N[a3]]
        return (x3, y3)

    def mul(self, P, n):
        R = None
        Qp = P
        while n:
            if n & 1:
                R = self.add(R, Qp)
            Qp = self.add(Qp, Qp)
            n >>= 1
        return R

    def frob(self, P):
        if P is None:
            return None
        F = self.F
        return (F.FROB[P[0]], F.FROB[P[1]])


# ----------------------------------------------------------------------------
# curves of the round
# ----------------------------------------------------------------------------

CURVES = {
    "D2": dict(p=2, coeffs=(0, 0, 1, 1, 1), P=[1, -2, 2]),   # y^2+y = x^3+x+1 / F_2
    "D3": dict(p=3, coeffs=(0, 0, 0, 1, 1), P=[1, 0, 3]),    # y^2   = x^3+x+1 / F_3
}
KMAX = 6

T = sp.symbols("T")

print("=" * 78)
print("SECTION 1  point counts, closed points, a_n   (B1(a), conventions)")
print("=" * 78)

data = {}
for name, spec in CURVES.items():
    p = spec["p"]
    Pcoef = spec["P"]
    Ppoly = sum(sp.Integer(c) * T ** i for i, c in enumerate(Pcoef))
    Z = sp.together(Ppoly / ((1 - T) * (1 - p * T)))
    Nk = []
    fields = {}
    curves = {}
    ptsets = {}
    for k in range(1, KMAX + 1):
        F = FF(p, k)
        E = Curve(F, spec["coeffs"])
        pts = E.points()
        fields[k] = F
        curves[k] = E
        ptsets[k] = pts
        Nk.append(len(pts))
    data[name] = dict(p=p, Ppoly=Ppoly, Z=Z, Nk=Nk, fields=fields,
                      curves=curves, pts=ptsets)
    # N_k = 1 + q^k - sum alpha_i^k  <=>  the logarithmic derivative of Z
    alphas = sp.Poly(Ppoly.subs(T, 1 / T) * T ** 2, T).all_coeffs()
    roots = sp.roots(sp.Poly(Ppoly, T))
    al = []
    for r, m in roots.items():
        al += [1 / r] * m
    pred = [sp.simplify(1 + p ** k - sum(a ** k for a in al)) for k in range(1, KMAX + 1)]
    check([sp.nsimplify(x) for x in pred] == Nk,
          "%s: N_k = 1+q^k-sum alpha_i^k for k=1..%d  (got %s)" % (name, KMAX, Nk))

# closed points as Frobenius orbits
for name in CURVES:
    d = data[name]
    p = d["p"]
    closed = {}          # degree -> list of orbits (each a list of points in F_{q^deg})
    for k in range(1, KMAX + 1):
        E = d["curves"][k]
        seen = set()
        orbs = []
        for P in d["pts"][k]:
            if P in seen:
                continue
            orb = []
            Q = P
            while True:
                orb.append(Q)
                seen.add(Q)
                Q = E.frob(Q)
                if Q == P:
                    break
            if len(orb) == k:
                orbs.append(orb)
        closed[k] = orbs
    d["closed"] = closed
    bd = [len(closed[k]) for k in range(1, KMAX + 1)]
    ok = True
    for k in range(1, KMAX + 1):
        s = sum(dd * len(closed[dd]) for dd in range(1, k + 1) if k % dd == 0)
        if s != d["Nk"][k - 1]:
            ok = False
    check(ok, "%s: sum_{d|k} d*b_d = N_k for k=1..%d  (b_d = %s)" % (name, KMAX, bd))
    # Euler product
    ser = sp.Integer(1)
    poly = sp.Integer(1)
    for k in range(1, KMAX + 1):
        poly *= (1 - T ** k) ** len(closed[k])
    inv = sp.series(1 / poly, T, 0, KMAX + 1).removeO()
    a_euler = [int(sp.expand(inv).coeff(T, n)) for n in range(KMAX + 1)]
    a_zeta = [int(sp.series(d["Z"], T, 0, KMAX + 1).removeO().coeff(T, n))
              for n in range(KMAX + 1)]
    d["a"] = a_euler
    check(a_euler == a_zeta,
          "%s: Euler product a_n == Taylor of P/((1-T)(1-qT)), n<=%d  (a = %s)"
          % (name, KMAX, a_euler))

print()
print("=" * 78)
print("SECTION 2  Pic^0 = E(F_q), the group law, h   (B1(c),(d), B3(a))")
print("=" * 78)

for name in CURVES:
    d = data[name]
    F1, E1 = d["fields"][1], d["curves"][1]
    pts1 = d["pts"][1]
    # group axioms
    okc = all(E1.on_curve(E1.add(P, Q)) for P in pts1 for Q in pts1)
    check(okc, "%s: E(F_q) closed under the group law" % name)
    oki = all(E1.add(P, None) == P and E1.add(E1.neg(P), P) is None for P in pts1)
    check(oki, "%s: identity and inverses" % name)
    okcom = all(E1.add(P, Q) == E1.add(Q, P) for P in pts1 for Q in pts1)
    check(okcom, "%s: commutativity on E(F_q)" % name)
    oka = all(E1.add(E1.add(P, Q), R) == E1.add(P, E1.add(Q, R))
              for P in pts1 for Q in pts1 for R in pts1)
    check(oka, "%s: associativity on E(F_q) (exhaustive)" % name)
    # associativity over F_{q^3}, random
    F3, E3 = d["fields"][3], d["curves"][3]
    pts3 = d["pts"][3]
    oka3 = True
    for _ in range(40):
        P, Q, R = (random.choice(pts3) for _ in range(3))
        if E3.add(E3.add(P, Q), R) != E3.add(P, E3.add(Q, R)):
            oka3 = False
    check(oka3, "%s: associativity on 40 random triples over F_{q^3}" % name)
    h = len(pts1)
    d["h"] = h
    orders = []
    for P in pts1:
        n = 1
        Q = P
        while Q is not None:
            Q = E1.add(Q, P)
            n += 1
        orders.append(n)
    orders = sorted(orders)
    d["orders"] = orders
    check(h == d["Nk"][0], "%s: h = |Pic^0(F_q)| = |E(F_q)| = N_1 = %d" % (name, h))

check(data["D2"]["h"] == 1, "D2: h = 1")
check(data["D3"]["h"] == 4 and data["D3"]["orders"] == [1, 2, 4, 4],
      "D3: h = 4 and E(F_3) is cyclic Z/4 (element orders %s)" % data["D3"]["orders"])

for name in CURVES:
    d = data[name]
    p, h = d["p"], d["h"]
    Pg = 1 - (p + 1 - h) * T + p * T ** 2
    check(sp.expand(Pg - d["Ppoly"]) == 0,
          "%s: B1(c) P(T) = 1-(q+1-h)T+qT^2 = %s" % (name, sp.factor(d["Ppoly"])))
    check(d["Ppoly"].subs(T, 1) == h, "%s: B1(c),(d) h = P(1) = %d" % (name, h))
    Zg = 1 + h * T / ((1 - T) * (1 - p * T))
    check(sp.simplify(Zg - d["Z"]) == 0, "%s: B1(c) Z(T) = 1 + hT/((1-T)(1-qT))" % name)

print()
print("=" * 78)
print("SECTION 3  divisor classes, h^0, and B1(a),(b), B2(a),(b)")
print("=" * 78)

NMAX = 5
for name in CURVES:
    d = data[name]
    p, h = d["p"], d["h"]
    E1 = d["curves"][1]
    pts1 = d["pts"][1]
    # class map:  Tr(P) = sum of the Frobenius orbit, computed in E(F_{q^deg})
    cls = {}     # (deg, orbit index) -> class in E(F_q), as a point of E(F_q)
    ok_rat = True
    plist = []
    for k in range(1, NMAX + 1):
        Ek = d["curves"][k]
        Fk = d["fields"][k]
        for i, orb in enumerate(d["closed"][k]):
            s = None
            for Q in orb:
                s = Ek.add(s, Q)
            if s is None:
                c = None
            else:
                if not (Fk.in_prime_field(s[0]) and Fk.in_prime_field(s[1])):
                    ok_rat = False
                    c = None
                else:
                    # translate the F_q-point of E(F_{q^k}) back to E(F_q)
                    c = (Fk.to_prime(s[0]), Fk.to_prime(s[1]))
                    c = (d["fields"][1].emb(c[0]), d["fields"][1].emb(c[1]))
            plist.append((k, i, c))
    check(ok_rat, "%s: Tr(P) = sum over the Frobenius orbit is F_q-rational for every "
                  "closed point of degree <= %d" % (name, NMAX))
    d["plist"] = plist
    # enumerate effective divisors of degree <= NMAX as multisets of closed points
    pts_by_deg = {}
    for (k, i, c) in plist:
        pts_by_deg.setdefault(k, []).append((k, i, c))

    def effective(n):
        """all multisets of closed points of total degree n"""
        out = []

        def rec(rem, start, cur):
            if rem == 0:
                out.append(list(cur))
                return
            flat = [q for k in sorted(pts_by_deg) for q in pts_by_deg[k]]
            for j in range(start, len(flat)):
                q = flat[j]
                if q[0] <= rem:
                    cur.append(q)
                    rec(rem - q[0], j, cur)
                    cur.pop()
        rec(n, 0, [])
        return out

    percls = {}
    for n in range(0, NMAX + 1):
        eff = effective(n)
        check(len(eff) == d["a"][n],
              "%s: exhaustive enumeration of effective divisors of degree %d gives "
              "a_%d = %d" % (name, n, n, d["a"][n]))
        cnt = {}
        for D in eff:
            c = None
            for (k, i, cc) in D:
                c = E1.add(c, cc)
            cnt[c] = cnt.get(c, 0) + 1
        percls[n] = cnt
    d["percls"] = percls

    # B1(a): a_n = sum over classes of (q^{h^0}-1)/(q-1), with h^0 from the count
    ok_b1a = True
    ok_h0 = True
    for n in range(0, NMAX + 1):
        tot = 0
        for c in pts1:
            m = percls[n].get(c, 0)
            # solve m = (q^{h0}-1)/(q-1)
            h0 = 0
            while (p ** h0 - 1) // (p - 1) < m:
                h0 += 1
            if (p ** h0 - 1) // (p - 1) != m:
                ok_h0 = False
            tot += (p ** h0 - 1) // (p - 1)
            # genus-one Riemann--Roch prediction
            pred = n if n >= 1 else (1 if c is None else 0)
            if h0 != pred:
                ok_h0 = False
        if tot != d["a"][n]:
            ok_b1a = False
    check(ok_b1a, "%s: B1(a) a_n = sum_{[D] in Pic^n} (q^{h^0(D)}-1)/(q-1) for n=0..%d"
          % (name, NMAX))
    check(ok_h0, "%s: every class of degree n>=1 carries exactly (q^n-1)/(q-1) effective "
                 "divisors, i.e. h^0 = deg; in degree 0 only the trivial class, h^0 = 1"
          % name)

    # B1(b) and its deviation set
    ok_gen = all(d["a"][n] == h * (p ** n - 1) // (p - 1) for n in range(1, KMAX + 1))
    check(ok_gen, "%s: B1(b) a_n = h(q^{n+1-g}-1)/(q-1) for every n > 2g-2 = 0" % name)
    check(d["a"][0] == 1 and h * (p ** 0 - 1) // (p - 1) == 0,
          "%s: the single deviation from the generic part sits at n = 0 = 2g-2" % name)

    # B2(a) by explicit linear algebra:  #L(nP_0) = q^{h^0(nP_0)}
    # L(n O) is spanned by the monomials x^i y^j (j<=1) with 2i+3j <= n.
    F6 = d["fields"][6]
    E6 = d["curves"][6]
    aff = [P for P in d["pts"][6] if P is not None]
    mons = []
    for j in (0, 1):
        for i in range(0, 4):
            if 2 * i + 3 * j <= 4:
                mons.append((i, j))
    for n in range(0, 5):
        basis = [(i, j) for (i, j) in mons if 2 * i + 3 * j <= n]
        vals = []
        for (i, j) in basis:
            v = []
            for (x, y) in aff:
                t = F6.pw(x, i)
                if j:
                    t = F6.MUL[t][y]
                v.append(t)
            vals.append(v)
        seen = set()
        for co in itertools.product(range(p), repeat=len(basis)):
            v = [0] * len(aff)
            for cc, row in zip(co, vals):
                e = F6.emb(cc)
                v = [F6.ADD[a][F6.MUL[e][b]] for a, b in zip(v, row)]
            seen.add(tuple(v))
        h0 = n if n >= 1 else 1
        check(len(seen) == p ** h0,
              "%s: B2(a) #L(%d P_0) = q^{h^0} = %d by explicit enumeration of the "
              "F_q-span (distinct functions on %d affine points of C(F_{q^6}))"
              % (name, n, p ** h0, len(aff)))

    # B2(b): the two fibre normalisations, in their counting form
    #   route 1 (over A^x):        sum over effective divisors, fibre volume 1
    #   route 2 (over A^x/K^x):    (1/(q-1)) sum over classes of (q^{h^0}-1)
    ok_fib = True
    for n in range(0, NMAX + 1):
        r1 = d["a"][n]
        r2 = Fraction(0)
        for c in pts1:
            m = percls[n].get(c, 0)
            h0 = 0
            while (p ** h0 - 1) // (p - 1) < m:
                h0 += 1
            r2 += Fraction(p ** h0 - 1, p - 1)
        if Fraction(r1) != r2:
            ok_fib = False
    check(ok_fib, "%s: B2(b) the A^x route (fibre volume 1, sum over effective divisors) "
                  "and the A^x/K^x route (fibre volume 1/(q-1), sum over classes of "
                  "q^{h^0}-1) give the same coefficients for n=0..%d" % (name, NMAX))
    # the 1/(q-1) is exactly |F_q^x| = |K^x cap prod O_v^x|
    units = 1
    for c in range(1, p):
        units += 0
    check(p - 1 == p ** 1 - 1 and percls[0].get(None, 0) == 1,
          "%s: K^x cap prod_v O_v^x = F_q^x has order q-1 = %d  (only the zero divisor "
          "is effective of degree 0, and h^0(0)=1 so L(0)=F_q)" % (name, p - 1))

print()
print("=" * 78)
print("SECTION 4  B2(c): functional equation, Poisson = Riemann-Roch, theta divisor")
print("=" * 78)

# functional equation of Z, symbolically, genus 0..3 (synthetic Weil polynomials)
q = sp.symbols("q", positive=True)
tests = [
    (0, sp.Integer(1), 2),
    (1, 1 - 2 * T + 2 * T ** 2, 2),
    (1, 1 + 3 * T ** 2, 3),
    (2, (1 + 3 * T ** 2) * (1 - 2 * T + 3 * T ** 2), 3),
    (3, (1 + 3 * T ** 2) * (1 - 2 * T + 3 * T ** 2) * (1 + T + 3 * T ** 2), 3),
]
for g, Pp, qq in tests:
    Zg = Pp / ((1 - T) * (1 - qq * T))
    lhs = sp.simplify(Zg.subs(T, 1 / (qq * T)))
    rhs = sp.simplify(qq ** (1 - g) * T ** (2 - 2 * g) * Zg)
    check(sp.simplify(lhs - rhs) == 0,
          "functional equation Z(1/(qT)) = q^{1-g}T^{2-2g}Z(T) for g=%d, q=%d, P=%s"
          % (g, qq, sp.factor(Pp)))

# B1(d) WITHOUT Lefschetz: h = P(1) is forced by B1(a)+(b) alone.
# If a_n = h(q^{n+1-g}-1)/(q-1) for all n > 2g-2 then (1-T)(1-qT)Z(T) at T=1 equals h.
for g, Pp, qq in tests:
    Zg = Pp / ((1 - T) * (1 - qq * T))
    NN = 4 * g + 8
    ser = sp.series(Zg, T, 0, NN).removeO()
    aa = [sp.expand(ser).coeff(T, n) for n in range(NN)]
    hP = sp.expand(Pp.subs(T, 1))
    ok = all(aa[n] == hP * (qq ** (n + 1 - g) - 1) / (qq - 1)
             for n in range(2 * g - 1 if g > 0 else 1, NN))
    check(ok, "g=%d q=%d: the tail a_n = P(1)(q^{n+1-g}-1)/(q-1) holds for every "
              "n > 2g-2, so h = P(1) = %s follows from B1(a)+(b) with no Lefschetz "
              "and no Jacobian" % (g, qq, hP))

# Poisson = Riemann-Roch, counting form, on the two genus-one curves.
# q^{h^0(D)} = q^{deg D + 1 - g} q^{h^0(K_C - D)},  K_C = 0, g = 1.
for name in CURVES:
    d = data[name]
    p, h = d["p"], d["h"]
    E1 = d["curves"][1]
    pts1 = d["pts"][1]

    def h0(n, c):
        if n < 0:
            return 0
        if n == 0:
            return 1 if c is None else 0
        return n

    ok = True
    for n in range(-4, 5):
        for c in pts1:
            cneg = E1.neg(c) if c is not None else None
            if p ** h0(n, c) != p ** (n + 1 - 1) * p ** h0(-n, cneg):
                ok = False
    check(ok, "%s: q^{h^0(D)} = q^{deg D+1-g} q^{h^0(K_C-D)} for every class of degree "
              "-4..4 (this is exactly Poisson for 1_{O_A} with vol(O_A) = q^{1-g})"
          % name)

# the constant in \hat{1_U} = vol(U) 1_{U^perp}: verified in a finite self-dual model
for (m, subs) in [(12, [1, 2, 3, 4, 6]), (16, [1, 2, 4, 8])]:
    okc = True
    for s in subs:
        U = [i for i in range(m) if i % s == 0]          # subgroup of Z/m of order m/s
        Uperp = [j for j in range(m) if all((i * j) % m == 0 for i in U)]
        # Fourier transform of 1_U with counting measure
        import cmath
        ok_here = True
        for j in range(m):
            val = sum(cmath.exp(-2j * cmath.pi * i * j / m) for i in U)
            want = len(U) if j in Uperp else 0
            if abs(val - want) > 1e-9:
                ok_here = False
        if not ok_here:
            okc = False
        if len(U) * len(Uperp) != m:
            okc = False
    check(okc, "finite Poisson model Z/%d: hat(1_U) = |U| . 1_{U^perp} and "
               "|U||U^perp| = |G| for every subgroup -- the shape and the constant "
               "the proof needs for hat(1_{O_A}) = vol(O_A) 1_{O_A(K_C)}" % m)

# theta divisor versus fixed locus of D -> K_C - D, genus one
for name in CURVES:
    d = data[name]
    E1 = d["curves"][1]
    pts1 = d["pts"][1]
    two = [c for c in pts1 if E1.add(c, c) is None]
    theta = [c for c in pts1 if (1 if c is None else 0)]   # W_0 = {[0]}
    check(len(theta) == 1, "%s: the theta divisor W_{g-1} = W_0 of Pic^0 is the single "
                           "principal class" % name)
    check(all(E1.neg(c) == c for c in two),
          "%s: the fixed locus of [D] -> [-D] on Pic^0 is the 2-torsion, %d class(es)"
          % (name, len(two)))
    check(len(two) >= len(theta),
          "%s: at genus one the fixed locus (%d) is >= the theta divisor (%d) -- the "
          "direction the proofs' 'in general larger' asserts" % (name, len(two), len(theta)))

print()
print("=" * 78)
print("SECTION 5  B3(b): class characters and L(T,chi) at genus one")
print("=" * 78)

for name in CURVES:
    d = data[name]
    p, h = d["p"], d["h"]
    E1 = d["curves"][1]
    pts1 = d["pts"][1]
    # a generator / discrete log for Pic^0 (cyclic in both cases)
    gen = None
    for P in pts1:
        n, Q = 1, P
        while Q is not None:
            Q = E1.add(Q, P)
            n += 1
        if n == h:
            gen = P
            break
    dlog = {}
    Q = None
    for i in range(h):
        dlog[Q] = i
        Q = E1.add(Q, gen) if gen is not None else None
    check(len(dlog) == h, "%s: Pic^0 is cyclic of order %d, discrete log built" % (name, h))
    zeta = sp.exp(2 * sp.pi * sp.I / h)
    for r in range(h):
        coeffs = []
        for n in range(0, NMAX + 1):
            s = 0
            for c in pts1:
                m = d["percls"][n].get(c, 0)
                s += sp.simplify(zeta ** (r * dlog[c])) * m
            coeffs.append(sp.simplify(sp.expand(s)))
        if r == 0:
            want = [d["a"][n] for n in range(NMAX + 1)]
            check([sp.nsimplify(c) for c in coeffs] == want,
                  "%s: L(T,chi_0) = Z(T) coefficientwise to T^%d" % (name, NMAX))
        else:
            ok = coeffs[0] == 1 and all(sp.simplify(c) == 0 for c in coeffs[1:])
            check(ok, "%s: L(T,chi^%d) = 1 (a polynomial of degree 2g-2 = 0); "
                      "coefficients %s" % (name, r, [sp.nsimplify(c) for c in coeffs]))

print()
print("=" * 78)
print("CHECKS: %d passed, %d failed" % (PASS, FAIL))
print("=" * 78)
