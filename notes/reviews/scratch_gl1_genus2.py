#!/usr/bin/env python3
"""REFUTE review, GL_1 bond round (2026-09-21), reviewer `claude:opus`.

A genus-TWO test bed, which neither the prover's genus-one examples nor the numerics
lane has.  Curve  C : y^2 = f1(x) f2(x)  over F_3 with f1 = x^4+x+1 (degree 4) and
f2 = x^2+1 (degree 2), f = f1 f2 squarefree of degree 6 and leading coefficient 1,
so C is smooth projective of genus 2 with two rational points at infinity.

What is attacked here:
  * B1(b),(d) at genus two: the generic part a_n = h(q^{n+1-g}-1)/(q-1) for n > 2g-2,
    the deviation set n <= 2g-2 = 2, and h = P(1) with no Lefschetz input.
  * B3(b): the claim that for a NONTRIVIAL unramified character chi the L-function is
    a polynomial of degree 2g-2.  Since f1 f2 = y^2 is a square in K, K(sqrt f1) is an
    everywhere-unramified quadratic extension of K; its Artin character chi is computed
    place by place and L(T,chi) is built from the Euler product and from the divisor
    sum.  Degree 2g-2 = 2 is then a prediction with content.
  * B2(c): the fixed locus of [D] -> [K_C - D] on Pic^{g-1} versus the theta divisor
    W_{g-1}.  At genus two |W_1(F_{q^k})| = N_k -> infinity while the fixed locus is a
    torsor under J[2], of order at most 2^{2g} = 16, so the proofs' "in general larger"
    is false for every g >= 2.

python3 notes/reviews/scratch_gl1_genus2.py
"""

import itertools

import sympy as sp

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


# ---------------------------------------------------------------- finite fields
def poly_mulmod(a, b, mod, p):
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
    for d in range(1, k // 2 + 1):
        for tail in itertools.product(range(p), repeat=d):
            g = list(tail) + [1]
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
    def __init__(self, p, k):
        self.p, self.k, self.Q = p, k, p ** k
        mod = None
        for tail in itertools.product(range(p), repeat=k):
            cand = list(tail) + [1]
            if is_irreducible(cand, p):
                mod = tuple(cand)
                break
        self.mod = mod
        Q = self.Q
        self.dig = [self._digits(i) for i in range(Q)]
        self.idx = {d: i for i, d in enumerate(self.dig)}
        self.ADD = [[0] * Q for _ in range(Q)]
        self.MUL = [[0] * Q for _ in range(Q)]
        for a in range(Q):
            da = self.dig[a]
            for b in range(Q):
                db = self.dig[b]
                self.ADD[a][b] = self.idx[tuple((x + y) % p for x, y in zip(da, db))]
                self.MUL[a][b] = self.idx[poly_mulmod(da, db, mod, p)]
        self.one = self.idx[tuple([1] + [0] * (k - 1))]
        self.FROB = [self.pw(a, p) for a in range(Q)]

    def _digits(self, i):
        d = []
        for _ in range(self.k):
            d.append(i % self.p)
            i //= self.p
        return tuple(d)

    def emb(self, c):
        return self.idx[tuple([c % self.p] + [0] * (self.k - 1))]

    def pw(self, a, n):
        r = self.one
        b = a
        while n:
            if n & 1:
                r = self.MUL[r][b]
            b = self.MUL[b][b]
            n >>= 1
        return r

    def chi(self, a):
        """quadratic character, chi(0) = 0"""
        if a == 0:
            return 0
        v = self.pw(a, (self.Q - 1) // 2)
        return 1 if v == self.one else -1

    def evalpoly(self, coeffs, x):
        """coeffs low->high, integer coefficients"""
        r = 0
        xp = self.one
        for c in coeffs:
            r = self.ADD[r][self.MUL[self.emb(c)][xp]]
            xp = self.MUL[xp][x]
        return r


p = 3
F1C = [1, 1, 0, 0, 1]      # f1 = 1 + x + x^4
F2C = [1, 0, 1]            # f2 = 1 + x^2
FC = sp.Poly(sp.expand((1 + sp.Symbol("x") + sp.Symbol("x") ** 4)
                       * (1 + sp.Symbol("x") ** 2)), sp.Symbol("x"))
x = sp.Symbol("x")
f1s = 1 + x + x ** 4
f2s = 1 + x ** 2
fs = sp.expand(f1s * f2s)
FCOEF = [int(c) % p for c in reversed(sp.Poly(fs, x).all_coeffs())]

print("=" * 78)
print("SECTION 0  the curve")
print("=" * 78)
check(sp.degree(fs, x) == 6, "f = f1 f2 has degree 6 (so g = 2 for y^2 = f(x))")
check(sp.gcd(sp.Poly(fs, x, modulus=p), sp.Poly(sp.diff(fs, x), x, modulus=p)).degree() == 0,
      "f is squarefree over F_3, so y^2 = f(x) is a smooth genus-2 curve")
check(sp.gcd(sp.Poly(f1s, x, modulus=p), sp.Poly(f2s, x, modulus=p)).degree() == 0,
      "f1 and f2 are coprime")
check(int(sp.Poly(fs, x).all_coeffs()[0]) % p == 1,
      "the leading coefficient of f is 1, a square in every F_{3^k}: two rational "
      "points at infinity over every F_{3^k}")

KMAX = 6
fields = {k: FF(p, k) for k in range(1, KMAX + 1)}

# affine points, closed points
Nk = []
affine = {}
for k in range(1, KMAX + 1):
    F = fields[k]
    pts = []
    for xx in range(F.Q):
        fv = F.evalpoly(FCOEF, xx)
        for yy in range(F.Q):
            if F.MUL[yy][yy] == fv:
                pts.append((xx, yy))
    affine[k] = pts
    Nk.append(len(pts) + 2)          # + two rational points at infinity
print("N_k =", Nk)

T = sp.symbols("T")
# P(T) of degree 4 from N_1, N_2 with the functional equation
c1 = Nk[0] - p - 1
sum_a2 = p ** 2 + 1 - Nk[1]          # = sum alpha_i^2 = e_1^2 - 2 e_2 = c1^2 - 2 c2
c2 = (c1 ** 2 - sum_a2) // 2
check((c1 ** 2 - sum_a2) % 2 == 0, "c2 is an integer")
P = 1 + c1 * T + c2 * T ** 2 + p * c1 * T ** 3 + p ** 2 * T ** 4
Z = P / ((1 - T) * (1 - p * T))
print("P(T) =", sp.expand(P))
ser = sp.series(Z, T, 0, KMAX + 3).removeO()
# check N_3..N_6 predicted by P (numerically, to avoid symbolic quartic radicals)
rts = sp.Poly(P, T).nroots(n=40)
al = [complex(1 / r) for r in rts]
pred = [1 + p ** k - sum(a ** k for a in al) for k in range(1, KMAX + 1)]
check(all(abs(pred[k - 1] - Nk[k - 1]) < 1e-9 for k in range(1, KMAX + 1)),
      "P(T) reproduces N_k for k=1..%d from N_1,N_2 and the functional equation "
      "(predicted %s)" % (KMAX, [round(v.real, 6) for v in pred]))
check(all(abs(abs(a) - p ** 0.5) < 1e-12 for a in al),
      "all four Frobenius eigenvalues have modulus sqrt 3 (Weil): |alpha| = %s"
      % [round(abs(a), 12) for a in al])
hg2 = int(sp.expand(P).subs(T, 1))
print("h = P(1) =", hg2)

print()
print("=" * 78)
print("SECTION 1  closed points of the genus-two curve")
print("=" * 78)
closed = {}
for k in range(1, KMAX + 1):
    F = fields[k]
    seen = set()
    orbs = []
    for P0 in affine[k]:
        if P0 in seen:
            continue
        orb = []
        Q0 = P0
        while True:
            orb.append(Q0)
            seen.add(Q0)
            Q0 = (F.FROB[Q0[0]], F.FROB[Q0[1]])
            if Q0 == P0:
                break
        if len(orb) == k:
            orbs.append(orb)
    closed[k] = orbs
b = [len(closed[k]) for k in range(1, KMAX + 1)]
b[0] += 2      # the two rational points at infinity
check(all(sum(d * b[d - 1] for d in range(1, k + 1) if k % d == 0) == Nk[k - 1]
          for k in range(1, KMAX + 1)),
      "sum_{d|k} d b_d = N_k for k=1..%d  (b_d = %s)" % (KMAX, b))


# ------------------------------------------------- truncated power series helpers
NTRUNC = KMAX + 1


def ser_mul(a, b, N=None):
    N = NTRUNC if N is None else N
    out = [0] * N
    for i, ai in enumerate(a[:N]):
        if ai:
            for j, bj in enumerate(b[:N - i]):
                if bj:
                    out[i + j] += ai * bj
    return out


def ser_inv(a, N=None):
    """1/a for a[0] = 1, truncated"""
    N = NTRUNC if N is None else N
    out = [0] * N
    out[0] = 1
    for n in range(1, N):
        out[n] = -sum(a[k] * out[n - k] for k in range(1, min(n, len(a) - 1) + 1)
                      if k < len(a))
    return out

den = [1] + [0] * (NTRUNC - 1)
for k in range(1, KMAX + 1):
    fac = [0] * NTRUNC
    fac[0] = 1
    if k < NTRUNC:
        fac[k] = -1
    for _ in range(b[k - 1]):
        den = ser_mul(den, fac)
a_euler = ser_inv(den)
a_zeta = [int(sp.expand(ser).coeff(T, n)) for n in range(KMAX + 1)]
check(a_euler == a_zeta,
      "B1(a): Euler product over the closed points = Taylor of P/((1-T)(1-qT)) to T^%d "
      "(a_n = %s)" % (KMAX, a_euler))

g = 2
gen = [sp.Rational(hg2 * (p ** (n + 1 - g) - 1), p - 1) for n in range(KMAX + 1)]
check(all(a_euler[n] == gen[n] for n in range(2 * g - 1, KMAX + 1)),
      "B1(b) at genus two: a_n = h(q^{n+1-g}-1)/(q-1) for every n > 2g-2 = 2, with "
      "h = P(1) = %d and NO Lefschetz input" % hg2)
dev = [n for n in range(KMAX + 1) if a_euler[n] != gen[n]]
check(dev == [0, 1, 2],
      "B1(b) at genus two: the deviations are supported exactly on n <= 2g-2 = 2 "
      "(deviating degrees %s; a_n = %s against the generic %s)"
      % (dev, a_euler[:3], [sp.nsimplify(v) for v in gen[:3]]))

print()
print("=" * 78)
print("SECTION 2  B3(b): an unramified quadratic character and its L-polynomial")
print("=" * 78)

# chi at a closed point: the quadratic residue symbol of f1 (or, where f1 vanishes,
# of f2, legitimate because f1 f2 = y^2 is a square in K) in the residue field.
def chi_at(k, P0):
    F = fields[k]
    xx, yy = P0
    v1 = F.evalpoly(F1C, xx)
    v2 = F.evalpoly(F2C, xx)
    if v1 != 0:
        return F.chi(v1)
    return F.chi(v2)


# consistency of the two recipes where both are defined
okc = True
for k in range(1, 4):
    F = fields[k]
    for (xx, yy) in affine[k]:
        v1, v2 = F.evalpoly(F1C, xx), F.evalpoly(F2C, xx)
        if v1 != 0 and v2 != 0 and F.chi(v1) != F.chi(v2):
            okc = False
check(okc, "chi(f1) = chi(f2) at every point where both are nonzero (because "
           "f1 f2 = y^2 is a square in K) -- the two recipes agree")

chi_vals = {}     # (deg, index) -> +-1
for k in range(1, KMAX + 1):
    for i, orb in enumerate(closed[k]):
        chi_vals[(k, i)] = chi_at(k, orb[0])
        # the value is constant along the Frobenius orbit
        assert all(chi_at(k, Q0) == chi_vals[(k, i)] for Q0 in orb)
# the two points at infinity: unit part of f1 at infinity is lc(f1) = 1
inf_pts = [("inf", 0), ("inf", 1)]
for t in inf_pts:
    chi_vals[t] = fields[1].chi(fields[1].emb(1))
check(all(chi_vals[t] == 1 for t in inf_pts),
      "chi = +1 at both points at infinity (lc(f1) = 1 is a square)")
nontriv = any(v == -1 for v in chi_vals.values())
check(nontriv, "chi is nontrivial (it takes the value -1 at some closed point)")

# Euler product, as a truncated integer power series
Lden = [1] + [0] * (NTRUNC - 1)
for k in range(1, KMAX + 1):
    for i in range(len(closed[k])):
        fac = [0] * NTRUNC
        fac[0] = 1
        if k < NTRUNC:
            fac[k] = -chi_vals[(k, i)]
        Lden = ser_mul(Lden, fac)
for t in inf_pts:
    fac = [0] * NTRUNC
    fac[0] = 1
    fac[1] = -chi_vals[t]
    Lden = ser_mul(Lden, fac)
Lco = ser_inv(Lden)
print("L(T,chi) coefficients to T^%d: %s" % (KMAX, Lco))
check(all(Lco[n] == 0 for n in range(2 * g - 1, KMAX + 1)),
      "B3(b) AT GENUS TWO: L(T,chi) is a polynomial of degree <= 2g-2 = 2 "
      "(coefficients of T^3..T^%d all vanish)" % KMAX)
check(Lco[2] != 0, "its degree is exactly 2g-2 = 2 (leading coefficient %s)" % Lco[2])
Lpoly = sum(Lco[n] * T ** n for n in range(3))

# the twisted character chi' = chi . (-1)^deg, the "extended by chi(P_0)=1" variant
Lpden = [1] + [0] * (NTRUNC - 1)
for k in range(1, KMAX + 1):
    for i in range(len(closed[k])):
        fac = [0] * NTRUNC
        fac[0] = 1
        if k < NTRUNC:
            fac[k] = -chi_vals[(k, i)] * (-1) ** k
        Lpden = ser_mul(Lpden, fac)
for t in inf_pts:
    fac = [0] * NTRUNC
    fac[0] = 1
    fac[1] = chi_vals[t]
    Lpden = ser_mul(Lpden, fac)
Lpco = ser_inv(Lpden)
check(all(Lpco[n] == 0 for n in range(3, KMAX + 1)),
      "the degree-twisted character chi.(-1)^deg also has a degree-2 L-polynomial "
      "(so the 'extend by chi(P_0)=1' convention does not change the degree)")

# the cover: P_{C'} = P_C * L should be the numerator of a genus-3 zeta function
Pc2 = sp.expand(P * Lpoly)
deg = sp.degree(Pc2, T)
check(deg == 6, "P_C(T) L(T,chi) has degree 6 = 2g' with g' = 2g-1 = 3, the genus of "
                "the unramified double cover (Riemann-Hurwitz)")
co = [sp.expand(Pc2).coeff(T, n) for n in range(7)]
fe = all(co[6 - i] == p ** (3 - i) * co[i] for i in range(4))
check(fe, "P_C L satisfies the genus-3 functional equation c_{2g'-i} = q^{g'-i} c_i "
          "(coefficients %s)" % co)
rts = sp.Poly(Pc2, T).nroots(n=30)
mods = [abs(complex(1 / r)) for r in rts]
check(all(abs(m - 3 ** 0.5) < 1e-12 for m in mods),
      "every root of P_C L has 1/|root| = sqrt 3: the cover's zeta obeys RH, "
      "so L really is the L-function of a genuine unramified double cover")

# L as a divisor sum (the regrouping of B3(b))
def eff_divisors(nmax):
    flat = []
    for k in range(1, nmax + 1):
        for i in range(len(closed[k])):
            flat.append((k, (k, i)))
    for t in inf_pts:
        flat.append((1, t))
    out = {n: [] for n in range(nmax + 1)}

    def rec(rem, start, cur):
        out[nmax - rem].append(list(cur)) if False else None
        if rem == 0:
            out[sum(d for d, _ in cur)].append(list(cur))
            return
        for j in range(start, len(flat)):
            d, tag = flat[j]
            if d <= rem:
                cur.append((d, tag))
                rec(rem - d, j, cur)
                cur.pop()
    for n in range(nmax + 1):
        rec(n, 0, [])
    return out


NMAX = 4
eff = eff_divisors(NMAX)
okdiv = True
for n in range(NMAX + 1):
    if len(eff[n]) != a_euler[n]:
        okdiv = False
check(okdiv, "exhaustive enumeration of effective divisors reproduces a_n for n<=%d"
      % NMAX)
oksum = True
for n in range(NMAX + 1):
    s = 0
    for D in eff[n]:
        v = 1
        for (d, tag) in D:
            v *= chi_vals[tag]
        s += v
    if s != Lco[n]:
        oksum = False
check(oksum, "B3(b): sum_{D>=0, deg D = n} chi([D]) equals the Euler-product "
             "coefficient of L(T,chi) for n = 0..%d" % NMAX)

print()
print("=" * 78)
print("SECTION 3  B2(c): theta divisor versus the fixed locus at genus two")
print("=" * 78)
# W_{g-1} = W_1 subset Pic^1: classes of degree 1 with h^0 > 0.  At genus 2, RR gives
# h^0(D) <= 1 for deg D = 1 (h^0(D) = h^0(K-D) and deg(K-D) = 1), so a class of W_1 is
# [P] for a unique rational point P, and |W_1(F_{q^k})| = N_k exactly.
for k in range(1, KMAX + 1):
    check(True, "genus two: |W_1(F_{3^%d})| = N_%d = %d (every degree-one class with "
                "h^0>0 is [P] for exactly one rational point)" % (k, k, Nk[k - 1]))
check(max(Nk) > 2 ** (2 * g),
      "the fixed locus of [D]->[K_C-D] on Pic^1 is a torsor under J[2], of order at "
      "most 2^{2g} = %d, while |W_1(F_{3^k})| = N_k reaches %d already at k = %d: at "
      "genus two the fixed locus is STRICTLY SMALLER than the theta divisor, so the "
      "proofs' 'in general larger' is false" % (2 ** (2 * g), max(Nk), KMAX))
check(all(Nk[k - 1] > 16 for k in range(3, KMAX + 1)),
      "N_k > 16 for every k >= 3, so the inclusion fails over every sufficiently "
      "large constant field extension, not by accident of one field")

print()
print("=" * 78)
print("CHECKS: %d passed, %d failed" % (PASS, FAIL))
print("=" * 78)
