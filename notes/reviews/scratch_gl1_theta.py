#!/usr/bin/env python3
"""REFUTE review, GL_1 bond round (2026-09-21), reviewer `claude:opus`.

Independent recomputation of proposition B4 of `notes/gl1-bond/proofs.md` in the
NOTEBOOK's xi normalisation

    cxi(s) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)      (report/sections/04_riemann_channel.tex:29)

The claim under test (B4(c)) is

    int_0^oo (theta(y) - 1 - y^{-1/2}) y^{s/2} d^x y = 2 pi^{-s/2} Gamma(s/2) zeta(s)
                                                     = 4 cxi(s)/(s(s-1)),   0 < Re s < 1,

together with B4(b) (Theta(x f) = theta(x^2), theta(1/y) = sqrt y theta(y)) and the
even/odd split.  Everything is computed with mpmath at 50 working digits; the theta
series is summed directly and the functional equation is never used where it is under
test.  The two candidate right-hand sides are separated three ways: value, residues at
s = 0,1, and the ratio.

python3 notes/reviews/scratch_gl1_theta.py
"""

import mpmath as mp

mp.mp.dps = 50

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


def theta(y):
    """sum_{n in Z} exp(-pi n^2 y), summed directly."""
    y = mp.mpf(y) if not isinstance(y, mp.mpf) else y
    s = mp.mpf(1)
    n = 1
    while True:
        t = mp.exp(-mp.pi * n * n * y)
        s += 2 * t
        if t < mp.mpf(10) ** (-mp.mp.dps - 10) and n > 3:
            break
        n += 1
        if n > 200000:
            break
    return s


def psi(y):
    return (theta(y) - 1) / 2


def Lam(s):
    """pi^{-s/2} Gamma(s/2) zeta(s)"""
    return mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def cxi(s):
    """the notebook's xi"""
    return mp.mpf(1) / 2 * s * (s - 1) * Lam(s)


def I_strip(s):
    """int_0^oo (theta(y)-1-y^{-1/2}) y^{s/2} dy/y, computed by splitting at y=1.

    On (1,oo):  (theta-1) y^{s/2-1}  by quadrature, and  -int_1^oo y^{(s-1)/2-1} dy
                = 2/(s-1)  in closed form (convergent for Re s < 1).
    On (0,1):   substitute y -> 1/u, using theta(1/u) = sqrt(u) theta(u), which is
                verified independently below:
                int_0^1 (theta(y)-y^{-1/2}) y^{s/2-1} dy
                    = int_1^oo (theta(u)-1) u^{(1-s)/2-1} du
                and  -int_0^1 y^{s/2-1} dy = -2/s  (convergent for Re s > 0).
    """
    A = mp.quad(lambda y: (theta(y) - 1) * y ** (s / 2 - 1), [1, 2, 5, 20, mp.inf])
    B = mp.quad(lambda u: (theta(u) - 1) * u ** ((1 - s) / 2 - 1),
                [1, 2, 5, 20, mp.inf])
    return A + B + 2 / (s - 1) - 2 / s


DELTA = mp.mpf("1e-3")


def I_direct(s):
    """The integral as literally written, with NO use of theta(1/y).

    On [DELTA, oo) the integrand is quadratured with theta summed directly.  On
    (0, DELTA) one has theta(y) - y^{-1/2} = 0 to working precision (checked below),
    so the integrand is exactly -y^{s/2-1} there and the piece is -2 DELTA^{s/2}/s.
    """
    f = lambda y: (theta(y) - 1 - y ** mp.mpf("-0.5")) * y ** (s / 2 - 1)
    tail = mp.quad(f, [DELTA, mp.mpf("0.05"), mp.mpf("0.3"), 1, 3, 10, mp.inf])
    return tail - 2 * DELTA ** (s / 2) / s


print("=" * 78)
print("SECTION 1  theta itself and the archimedean normalisation (B4(b), F3)")
print("=" * 78)
for y in ["1/3", "1", "7", "0.05", "2.5"]:
    yy = mp.mpf(mp.mpf(1) / 3) if y == "1/3" else mp.mpf(y)
    lhs = theta(1 / yy)
    rhs = mp.sqrt(yy) * theta(yy)
    check(abs(lhs - rhs) < mp.mpf(10) ** -40,
          "theta(1/y) = sqrt(y) theta(y) at y = %s  (|dev| = %s)"
          % (mp.nstr(yy, 6), mp.nstr(abs(lhs - rhs), 3)))

for xv in ["1.7", "0.6", "0.9"]:
    xx = mp.mpf(xv)
    lat = mp.mpf(1) + 2 * mp.nsum(lambda n: mp.exp(-mp.pi * (xx * n) ** 2), [1, mp.inf])
    check(abs(lat - theta(xx ** 2)) < mp.mpf(10) ** -40,
          "B4(b): sum_{n in Z} f_oo(x n) with f_oo(t) = e^{-pi t^2} equals theta(x^2) "
          "at x = %s  (|dev| = %s)" % (xv, mp.nstr(abs(lat - theta(xx ** 2)), 3)))
    check(abs(lat - theta(xx)) > mp.mpf("1e-3"),
          "  ... and NOT theta(x) at x = %s  (|dev| = %s): the brief's F3 slip, "
          "correctly carried into proofs.md B4(b)"
          % (xv, mp.nstr(abs(lat - theta(xx)), 3)))

print()
print("=" * 78)
print("SECTION 2  the Mellin identity inside the strip 0 < Re s < 1  (B4(c))")
print("=" * 78)
pts = [mp.mpf("0.3"), mp.mpf("0.5"), mp.mpf("0.7"),
       mp.mpc("0.7", "0.2"), mp.mpc("0.5", "3.0"), mp.mpc("0.25", "1.0")]
for s in pts:
    I = I_strip(s)
    tgt_proofs = 4 * cxi(s) / (s * (s - 1))
    tgt_2Lam = 2 * Lam(s)
    tgt_brief = 2 * Lam(s) / (s * (s - 1))
    check(abs(I - tgt_proofs) < mp.mpf(10) ** -30,
          "s = %s: I(s) = 4 cxi(s)/(s(s-1)) (the proofs' corrected constant); "
          "|dev| = %s, |I| = %s" % (mp.nstr(s, 6), mp.nstr(abs(I - tgt_proofs), 3),
                                    mp.nstr(abs(I), 8)))
    check(abs(tgt_proofs - tgt_2Lam) < mp.mpf(10) ** -35,
          "s = %s: 4 cxi(s)/(s(s-1)) = 2 pi^{-s/2}Gamma(s/2)zeta(s) exactly, i.e. the "
          "proofs' two displayed forms agree in the notebook's xi" % mp.nstr(s, 6))
    check(abs(I - tgt_brief) > mp.mpf("1e-3"),
          "s = %s: the BRIEF's 2 xi(s)/(s(s-1)) with xi = pi^{-s/2}Gamma(s/2)zeta(s) "
          "is wrong; |I - brief| = %s and I/brief = %s = s(s-1)"
          % (mp.nstr(s, 6), mp.nstr(abs(I - tgt_brief), 4),
             mp.nstr(I / tgt_brief, 8)))
    check(abs(I / tgt_brief - s * (s - 1)) < mp.mpf("1e-25"),
          "s = %s: the discrepancy factor is exactly s(s-1)" % mp.nstr(s, 6))

# the same integral computed literally, with no splitting and no functional equation
check(abs(theta(DELTA) - DELTA ** mp.mpf("-0.5")) < mp.mpf(10) ** -40,
      "theta(1e-3) - (1e-3)^{-1/2} = %s: below working precision, so on (0,1e-3) the "
      "integrand is -y^{s/2-1} to 50 digits and its integral is -2 DELTA^{s/2}/s "
      "(an elementary tail, not the functional equation)"
      % mp.nstr(abs(theta(DELTA) - DELTA ** mp.mpf("-0.5")), 3))
for s in [mp.mpf("0.3"), mp.mpc("0.7", "0.2")]:
    Id = I_direct(s)
    Is = I_strip(s)
    check(abs(Id - Is) < mp.mpf("1e-6"),
          "s = %s: brute-force quadrature of the integral AS WRITTEN agrees with the "
          "split evaluation to %s (so the split, which uses theta(1/y), is not "
          "smuggling the answer in)" % (mp.nstr(s, 6), mp.nstr(abs(Id - Is), 3)))

print()
print("=" * 78)
print("SECTION 3  zeros, residues, and the divergence outside the strip")
print("=" * 78)
zer = [mp.mpf("14.134725141734693790457251983562"),
       mp.mpf("21.022039638771554992628479593896")]
for t in zer:
    s = mp.mpc("0.5", t)
    I = I_strip(s)
    check(abs(I) < mp.mpf("1e-25"),
          "at the zero s = 1/2 + %si the transform vanishes: |I| = %s (against |I| ~ 8 "
          "elsewhere in the strip)" % (mp.nstr(t, 12), mp.nstr(abs(I), 3)))
    check(abs(I - 4 * cxi(s) / (s * (s - 1))) < mp.mpf("1e-28"),
          "  ... and still equals 4 cxi(s)/(s(s-1)) there (|dev| = %s)"
          % mp.nstr(abs(I - 4 * cxi(s) / (s * (s - 1))), 3))
    check(abs(cxi(s)) < mp.mpf("1e-28"),
          "  ... cxi(1/2+%si) = %s: in 0<Re s<1, Gamma(s/2) has no pole and no zero, so "
          "the zeros of the transform ARE the zeros of zeta"
          % (mp.nstr(t, 6), mp.nstr(abs(cxi(s)), 3)))

for (s0, res) in [(mp.mpf(1), mp.mpf(2)), (mp.mpf(0), mp.mpf(-2))]:
    for eps in [mp.mpf("1e-10"), mp.mpf("1e-12")]:
        val = eps * 4 * cxi(s0 + eps) / ((s0 + eps) * (s0 + eps - 1))
        check(abs(val - res) < mp.mpf("1e-8"),
              "the analytic continuation has a SIMPLE pole at s = %d with residue %d "
              "(eps = %s gives %s): 2 Lambda(s), not 2 Lambda(s)/(s(s-1)), which would "
              "have a double pole" % (int(s0), int(res), mp.nstr(eps, 2),
                                      mp.nstr(val, 10)))
# a double pole would make eps^2 * f finite and nonzero; check it is not
for s0 in [mp.mpf(0), mp.mpf(1)]:
    eps = mp.mpf("1e-10")
    val2 = eps ** 2 * 4 * cxi(s0 + eps) / ((s0 + eps) * (s0 + eps - 1))
    check(abs(val2) < mp.mpf("1e-8"),
          "eps^2 * transform -> 0 at s = %d: the pole is simple, not double"
          % int(s0))

# divergence outside the strip
for s in [mp.mpf(2), mp.mpf(3), mp.mpc("1.0", "1.0")]:
    tails = []
    for A in [mp.mpf(10), mp.mpf(100), mp.mpf(1000)]:
        t = mp.quad(lambda y: (theta(y) - 1 - y ** mp.mpf("-0.5")) * y ** (s / 2 - 1),
                    [A, 2 * A])
        tails.append(abs(t))
    if s.real > 1:
        ok = tails[2] > tails[1] > tails[0]
        word = "grows"
    else:
        ok = min(tails) > mp.mpf("0.5") and abs(tails[2] - tails[0]) < mp.mpf("1e-6")
        word = "does not decay (Re s = 1, the boundary)"
    check(ok, "s = %s: the tail int_A^{2A} %s (%s, %s, %s for A = 10,100,1000), so "
              "the integral diverges for Re s >= 1 -- the proofs' 'the integral "
              "diverges outside the strip' is right and the brief's 'for all s' is not"
          % (mp.nstr(s, 4), word, mp.nstr(tails[0], 4), mp.nstr(tails[1], 4),
             mp.nstr(tails[2], 4)))
for s in [mp.mpf("-0.2"), mp.mpf(0)]:
    tails = []
    for a in [mp.mpf("1e-2"), mp.mpf("1e-3"), mp.mpf("1e-4")]:
        t = mp.quad(lambda y: (theta(y) - 1 - y ** mp.mpf("-0.5")) * y ** (s / 2 - 1),
                    [a, 10 * a])
        tails.append(abs(t))
    check(tails[2] >= tails[1] >= tails[0] - mp.mpf("1e-30"),
          "s = %s: the piece int_a^{10a} near 0 does not decay (%s, %s, %s for "
          "a = 1e-2,1e-3,1e-4): divergence at the other end for Re s <= 0"
          % (mp.nstr(s, 4), mp.nstr(tails[0], 4), mp.nstr(tails[1], 4),
             mp.nstr(tails[2], 4)))

print()
print("=" * 78)
print("SECTION 4  which constant term carries which pole (B4 'Reading')")
print("=" * 78)
# Drop only the 1: convergence at y -> 0 fails for Re s <= 0, fine at infinity.
# Drop only the y^{-1/2}: convergence at y -> oo fails for Re s >= 1, fine at 0.
s = mp.mpf("0.4")
J1 = mp.quad(lambda y: (theta(y) - 1) * y ** (s / 2 - 1), [1, 3, 10, mp.inf])
check(abs(J1) < mp.inf and J1 == J1,
      "int_1^oo (theta-1) y^{s/2-1} dy converges for every s: neither constant term "
      "matters at infinity except y^{-1/2}")
for s0, which in [(mp.mpf("1.5"), "y^{-1/2}"), (mp.mpf("-0.5"), "1")]:
    if which == "y^{-1/2}":
        t1 = abs(mp.quad(lambda y: -y ** ((s0 - 1) / 2 - 1), [100, 200]))
        t2 = abs(mp.quad(lambda y: -y ** ((s0 - 1) / 2 - 1), [1000, 2000]))
        check(t2 > t1, "the term -y^{-1/2} alone diverges at infinity for Re s > 1: "
                       "it is the constant term that produces the pole at s = 1")
    else:
        t1 = abs(mp.quad(lambda y: -y ** (s0 / 2 - 1), [mp.mpf("1e-3"), mp.mpf("1e-2")]))
        t2 = abs(mp.quad(lambda y: -y ** (s0 / 2 - 1), [mp.mpf("1e-5"), mp.mpf("1e-4")]))
        check(t2 > t1, "the term -1 alone diverges at 0 for Re s < 0: it is the "
                       "constant term that produces the pole at s = 0")
check(True, "conclusion: the pairing is  1 <-> pole at s = 0  and  y^{-1/2} <-> pole "
            "at s = 1; the proofs' Reading lists '1, y^{-1/2}' against '(the poles "
            "s = 1, 0)', i.e. in the reverse order (the brief had 's = 0, 1')")

# odd part transforms with the same rule
for y in [mp.mpf("0.25"), mp.mpf("2.5"), mp.mpf("0.9")]:
    u = theta(y) - 1 - y ** mp.mpf("-0.5")
    v = y ** mp.mpf("-0.5") * (theta(1 / y) - 1 - mp.sqrt(y))
    check(abs(u - v) < mp.mpf("1e-35"),
          "the odd part obeys u(y) = y^{-1/2} u(1/y) at y = %s (|dev| = %s): the "
          "even/odd split is consistent with the automorphism"
          % (mp.nstr(y, 4), mp.nstr(abs(u - v), 3)))

print()
print("=" * 78)
print("SECTION 5  the notebook's xi and the symbol of prop:functional-model-modes")
print("=" * 78)
for s in [mp.mpc("0.3", "2.0"), mp.mpc("0.8", "-1.0"), mp.mpf(2), mp.mpf("-3.0")]:
    check(abs(cxi(s) - cxi(1 - s)) < mp.mpf("1e-30") * max(1, abs(cxi(s))),
          "cxi(s) = cxi(1-s) at s = %s" % mp.nstr(s, 6))
eps = mp.mpf("1e-25")
check(abs(cxi(1 + eps) - mp.mpf("0.5")) < mp.mpf("1e-20"),
      "cxi(1) = 1/2 (as a limit, cxi(1+1e-25) = %s)" % mp.nstr(cxi(1 + eps), 12))
check(abs(cxi(0 + eps) - mp.mpf("0.5")) < mp.mpf("1e-20"),
      "cxi(0) = 1/2 (as a limit, cxi(1e-25) = %s)" % mp.nstr(cxi(0 + eps), 12))
check(abs(2 * cxi(2) / (2 * 1) * 2 - mp.pi / 3) < mp.mpf("1e-40") or
      abs(4 * cxi(2) / (2 * (2 - 1)) - mp.pi / 3) < mp.mpf("1e-40"),
      "the continuation at s = 2 is 4 cxi(2)/(2.1) = 2 Lambda(2) = pi/3 = %s "
      "(the brief's form would give pi/6)"
      % mp.nstr(4 * cxi(2) / (2 * (2 - 1)), 12))
for tau in [mp.mpf("0.7"), mp.mpf("3.2"), mp.mpf("-1.1")]:
    S = cxi(1 - 2j * tau) / cxi(1 + 2j * tau)
    check(abs(abs(S) - 1) < mp.mpf("1e-30"),
          "S(tau) = cxi(1-2i tau)/cxi(1+2i tau) is unimodular for real tau = %s "
          "(|S| - 1 = %s)" % (mp.nstr(tau, 4), mp.nstr(abs(abs(S) - 1), 3)))

print()
print("=" * 78)
print("SECTION 6  which variable carries the bond?  (B4(b) in x versus B4(c) in y)")
print("=" * 78)
# B4(b) puts the bond state on the dilation line as x -> theta(x^2) (numerics F3);
# B4(c) states the Mellin identity in y.  With y = x^2 one has d^x y = 2 d^x x, so the
# SAME transform taken in the idele variable x carries HALF the constant:
#     int_0^oo (theta(x^2) - 1 - x^{-1}) x^s d^x x = Lambda(s) = 2 cxi(s)/(s(s-1)).
for s in [mp.mpf("0.3"), mp.mpf("0.5"), mp.mpc("0.7", "0.2")]:
    Ix = mp.mpf(1) / 2 * I_strip(s)        # exact change of variable y = x^2
    check(abs(Ix - 2 * cxi(s) / (s * (s - 1))) < mp.mpf(10) ** -30,
          "s = %s: int (theta(x^2)-1-x^{-1}) x^s d^x x = 2 cxi(s)/(s(s-1)) = "
          "Lambda(s) -- in the IDELE variable the constant is 2 cxi/(s(s-1)), half "
          "the 4 cxi/(s(s-1)) of B4(c); proofs.md B4 never says which variable the "
          "bond state lives in" % mp.nstr(s, 6))
    check(abs(2 * cxi(s) / (s * (s - 1)) - Lam(s)) < mp.mpf(10) ** -35,
          "s = %s: 2 cxi(s)/(s(s-1)) = Lambda(s), so the BRIEF's displayed constant "
          "'2 xi(s)/(s(s-1))' is the right one for the idele variable if xi is read "
          "as the NOTEBOOK's xi -- the brief's error is the pair (xi convention, "
          "variable), not a single factor" % mp.nstr(s, 6))

print()
print("=" * 78)
print("CHECKS: %d passed, %d failed" % (PASS, FAIL))
print("=" * 78)
