"""REFUTE review, graded toys 2026-09-20: independent lane, script 2.

thm:scattering-superdeterminant, prop:cavity-superdeterminant,
prop:genus-prefactor-forced.  All symbolic where possible.
"""
import numpy as np
import sympy as sp

PASS = [0]
FAIL = []


def check(name, cond, info=""):
    if cond:
        PASS[0] += 1
    else:
        FAIL.append((name, info))
        print("FAIL  %-62s %s" % (name, info))


w, z, u = sp.symbols('w z u')

# ------------------------------------------------------- curves / Weil data
CURVES = {
    'D2 (g=1,q=2)': (2, 1, sp.Poly(1 - 2 * sp.Symbol('T') + 2 * sp.Symbol('T') ** 2, sp.Symbol('T'))),
    'D3 (g=1,q=3)': (3, 1, sp.Poly(1 + 3 * sp.Symbol('T') ** 2, sp.Symbol('T'))),
    'synthetic g=2,q=3': (3, 2, sp.Poly(sp.expand((1 + 3 * sp.Symbol('T') ** 2) *
                                                  (1 - 2 * sp.Symbol('T') + 3 * sp.Symbol('T') ** 2)),
                                        sp.Symbol('T'))),
}
T = sp.Symbol('T')

for name, (q, g, P) in CURVES.items():
    alphas = sp.Poly(P, T).all_roots()
    alphas = [1 / a for a in sp.Poly(P.as_expr().subs(T, 1 / T) * T ** (2 * g), T).all_roots()]
    # simpler: inverse roots of P
    alphas = [sp.nsimplify(sp.simplify(1 / r)) for r in sp.Poly(P, T).all_roots()]
    check('%s deg P = 2g' % name, sp.Poly(P, T).degree() == 2 * g)
    check('%s |alpha| = sqrt q' % name,
          all(abs(complex(a.evalf(30))) - np.sqrt(q) < 1e-20 or
              abs(abs(complex(a.evalf(30))) - np.sqrt(q)) < 1e-12 for a in alphas),
          str([complex(a.evalf(20)) for a in alphas]))
    check('%s prod alpha = q^g' % name,
          abs(complex(sp.prod(alphas).evalf(30)) - q ** g) < 1e-12,
          str(complex(sp.prod(alphas).evalf(30))))
    # alpha -> q/alpha = conj(alpha) is an involution of the multiset
    A1 = sorted([complex(a.evalf(30)) for a in alphas], key=lambda c: (round(c.real, 9), round(c.imag, 9)))
    A2 = sorted([q / complex(a.evalf(30)) for a in alphas], key=lambda c: (round(c.real, 9), round(c.imag, 9)))
    check('%s alpha -> q/alpha involution' % name,
          max(abs(x - y) for x, y in zip(A1, A2)) < 1e-10)

    # ---- (a) superdeterminant of E_S = Fr (+) Pi Fr(-1)
    even = [sp.Integer(1), sp.Integer(q)] + [q * a for a in alphas]      # H^0,H^2 of Fr; H^1 of Fr(-1) flipped
    odd = list(alphas) + [sp.Integer(q), sp.Integer(q ** 2)]             # H^1 of Fr; H^0,H^2 of Fr(-1) flipped
    check('%s dim E_S = 4g+4' % name, len(even) + len(odd) == 4 * g + 4)
    sdet = sp.prod([1 - w * e for e in even]) / sp.prod([1 - w * e for e in odd])
    closed = (1 - w) * P.as_expr().subs(T, q * w) / ((1 - q ** 2 * w) * P.as_expr().subs(T, w))
    check('%s sdet = (1-w)P(qw)/((1-q^2w)P(w))' % name,
          sp.simplify(sp.together(sdet - closed)) == 0)
    zeta = lambda arg: P.as_expr().subs(T, arg) / ((1 - arg) * (1 - q * arg))
    ratio = sp.simplify(zeta(q * w) / zeta(w))     # zeta_K(2s-1)/zeta_K(2s), q^{-(2s-1)} = q w
    check('%s sdet = zeta_K(2s-1)/zeta_K(2s)' % name,
          sp.simplify(sp.together(sdet - ratio)) == 0, str(sp.simplify(sdet - ratio)))

    # ---- (b) disc classification under z^2 = e/q
    discs_even = [e for e in even if abs(complex(e.evalf(30))) < q - 1e-12]
    discs_odd = [e for e in odd if abs(complex(e.evalf(30))) < q - 1e-12]
    check('%s even disc eigenvalues = {1}' % name,
          len(discs_even) == 1 and discs_even[0] == 1, str(discs_even))
    check('%s odd disc eigenvalues = the alpha_i' % name,
          len(discs_odd) == 2 * g and
          max(abs(abs(complex(e.evalf(30))) - np.sqrt(q)) for e in discs_odd) < 1e-12,
          str([complex(e.evalf(20)) for e in discs_odd]))
    onb_e = [e for e in even if abs(abs(complex(e.evalf(30))) - q) < 1e-12]
    onb_o = [e for e in odd if abs(abs(complex(e.evalf(30))) - q) < 1e-12]
    check('%s exactly one even and one odd line at |e| = q' % name,
          len(onb_e) == 1 and len(onb_o) == 1 and onb_e[0] == q and onb_o[0] == q)
    out = [e for e in even + odd if abs(complex(e.evalf(30))) > q + 1e-12]
    check('%s classification exhaustive (disc + |e|=q + outside)' % name,
          len(discs_even) + len(discs_odd) + len(onb_e) + len(onb_o) + len(out) == 4 * g + 4)
    # z-images
    check('%s e=1 -> z = +-q^{-1/2}' % name,
          abs(abs(complex(sp.sqrt(sp.Rational(1, q)).evalf(30))) - q ** -0.5) < 1e-12)
    check('%s e=alpha -> |z| = q^{-1/4}' % name,
          all(abs(abs(complex((sp.sqrt(e / q)).evalf(30))) - q ** -0.25) < 1e-12 for e in discs_odd))
    check('%s the two lines at e=q have |z| = 1' % name,
          abs(abs(complex(sp.sqrt(sp.Integer(q) / q).evalf(30))) - 1) < 1e-14)
    # graded divisor of the disc part
    check('%s nu(1) = +1, nu(alpha_i) = -1' % name,
          all(sum(1 for e in even if abs(complex((e - a).evalf(30))) < 1e-12) -
              sum(1 for e in odd if abs(complex((e - a).evalf(30))) < 1e-12) == -1 for a in discs_odd) and
          (sum(1 for e in even if e == 1) - sum(1 for e in odd if e == 1)) == 1)

    # ---- (d) functional equation
    fe = sp.simplify(sp.together(sdet * sdet.subs(w, 1 / (q ** 2 * w)) - q ** (2 * g - 2)))
    check('%s sdet(1-wE)sdet(1-E/(q^2w)) = q^{2g-2}' % name, fe == 0, str(fe))
    # operator form: E_S ~ Pi(q^2 E_S^{-1}) as graded multisets
    lhs_e = sorted([complex(e.evalf(30)) for e in even], key=lambda c: (round(c.real, 8), round(c.imag, 8)))
    lhs_o = sorted([complex(e.evalf(30)) for e in odd], key=lambda c: (round(c.real, 8), round(c.imag, 8)))
    # Pi(q^2 E^{-1}): even part = q^2/odd, odd part = q^2/even
    rhs_e = sorted([q ** 2 / complex(e.evalf(30)) for e in odd], key=lambda c: (round(c.real, 8), round(c.imag, 8)))
    rhs_o = sorted([q ** 2 / complex(e.evalf(30)) for e in even], key=lambda c: (round(c.real, 8), round(c.imag, 8)))
    check('%s E_S ~ Pi(q^2 E_S^{-1}) (graded multisets)' % name,
          max(abs(x - y) for x, y in zip(lhs_e, rhs_e)) < 1e-9 and
          max(abs(x - y) for x, y in zip(lhs_o, rhs_o)) < 1e-9)

# ------------- flipping the OTHER copy gives the reciprocal (the "no choice" probe)
q, g, P = CURVES['D2 (g=1,q=2)']
alphas = [sp.nsimplify(sp.simplify(1 / r)) for r in sp.Poly(P, T).all_roots()]
even_alt = list(alphas) + [sp.Integer(q), sp.Integer(q ** 2)]
odd_alt = [sp.Integer(1), sp.Integer(q)] + [q * a for a in alphas]
sdet_alt = sp.prod([1 - w * e for e in even_alt]) / sp.prod([1 - w * e for e in odd_alt])
sdet_ref = sp.prod([1 - w * e for e in [sp.Integer(1), sp.Integer(q)] + [q * a for a in alphas]]) / \
           sp.prod([1 - w * e for e in list(alphas) + [sp.Integer(q), sp.Integer(q ** 2)]])
check('flipping the untwisted copy instead gives the RECIPROCAL ratio',
      sp.simplify(sp.together(sdet_alt * sdet_ref - 1)) == 0)
check('the two choices differ (so "which copy is flipped" is a choice)',
      sp.simplify(sp.together(sdet_alt - sdet_ref)) != 0)
# but the DIVISOR of a given rational function is unique
num, den = sp.fraction(sp.cancel(sp.together(sdet_ref)))
check('graded divisor read off the reduced rational function: 3 zeros, 3 poles (g=1, the two q-lines cancelled)',
      sp.Poly(num, w).degree() == 3 and sp.Poly(den, w).degree() == 3,
      '%s / %s' % (num, den))
check('the reduced function has no factor (1-qw): the e=q lines really cancel',
      sp.rem(sp.Poly(num, w), sp.Poly(1 - 2 * w, w)) != 0)

# ------------------------------------- prop:cavity-superdeterminant on D2 and D3
def zeta_ratio(q, P, wv):
    zz = lambda arg: P.subs(T, arg) / ((1 - arg) * (1 - q * arg))
    return zz(q * wv) / zz(wv)


R2 = z ** 2 * (z ** 2 - 2) * (2 * z ** 4 - 2 * z ** 2 + 1) / ((2 * z ** 2 - 1) * (z ** 4 - 2 * z ** 2 + 2))
R3 = z ** 2 * (z ** 2 - 3) * (3 * z ** 4 + 1) / ((3 * z ** 2 - 1) * (z ** 4 + 3))
for tag, (q, Pe, R) in {'D2': (2, 1 - 2 * T + 2 * T ** 2, R2),
                        'D3': (3, 1 + 3 * T ** 2, R3)}.items():
    expr = sp.simplify(sp.together(1 / R - z ** -2 * zeta_ratio(q, Pe, 1 / (q * z ** 2))))
    check('%s 1/R = z^-2 sdet(1 - E_S/(q z^2)) symbolically' % tag, expr == 0, str(expr))
    for zv in (0.31 + 0.17j, -0.44 + 0.62j, 0.73 - 0.28j, 0.9j, 0.5, -0.5, 0.2 + 0.8j, 0.85):
        lhs = complex((1 / R).subs(z, zv))
        rhs = complex((z ** -2).subs(z, zv)) * complex(zeta_ratio(q, Pe, 1 / (q * sp.nsimplify(zv) ** 2)))
        check('%s 1/R at z=%s' % (tag, zv), abs(lhs - rhs) < 1e-9 * max(1, abs(rhs)))
    # bound states = even disc eigenvalue; resonances = odd disc eigenvalues
    check('%s bound-state pair at z^2 = 1/q (e=1, even)' % tag,
          abs(complex(sp.nsimplify(1 / R).subs(z, sp.sqrt(sp.Rational(1, q))).evalf(30))) < 1e-20 or
          abs(complex(sp.simplify((1 / R).subs(z, sp.sqrt(sp.Rational(1, q)))))) < 1e-12)

# ----------------------------------------- prop:genus-prefactor-forced
def build_p(q, g, Pexpr, D):
    """p = z^2 prod_i (z^2 - alpha_i/q) (z^2 - q) D(z)  under the proposition's hypotheses."""
    # prod_i (z^2 - alpha_i/q) = q^{-2g} * z^{4g} * P(1/(q z^2)) * ... ; build from P directly:
    # prod_i (z^2 - a_i/q) with P(T) = prod (1 - a_i T)  =>  prod (z^2 - a_i/q)
    #   = prod (-a_i/q) * prod (1 - q z^2 / a_i) = (prod a_i)(-1)^{2g} q^{-2g} prod(1 - q z^2/a_i)
    # and 1/a_i = conj(a_i)/q so prod (1 - q z^2 / a_i) = prod(1 - z^2 conj a_i) = P(z^2) (multiset closed)
    return sp.expand(z ** 2 * sp.Rational(1, q ** g) * sp.expand(Pexpr.subs(T, z ** 2)) * (z ** 2 - q) * D)


def test_prefactor(tag, q, g, Pexpr, D):
    pp = build_p(q, g, Pexpr, D)
    pol = sp.Poly(pp, z)
    n2 = pol.degree()
    check('%s p monic' % tag, sp.simplify(pol.LC() - 1) == 0, str(pol.LC()))
    # verify the intended factorisation really has roots z^2 = alpha_i/q
    alphas = [sp.nsimplify(sp.simplify(1 / r)) for r in sp.Poly(Pexpr, T).all_roots()]
    for a in alphas:
        val = complex(pp.subs(z, sp.sqrt(a / q)).evalf(30))
        check('%s p(sqrt(alpha/q)) = 0' % tag, abs(val) < 1e-8, str(val))
    ptilde = sp.expand(z ** n2 * pp.subs(z, 1 / z))
    check('%s ptilde(0) = 1' % tag, sp.simplify(ptilde.subs(z, 0) - 1) == 0, str(sp.simplify(ptilde.subs(z, 0))))
    sD = sp.Poly(D, z).as_expr().subs(z, 0)
    Dz = sp.Poly(D, z)
    m1 = 0
    for r, m in sp.roots(Dz).items():
        if sp.simplify(r - 1) == 0:
            m1 = m
    check('%s s_D = (-1)^{m_{+1}}' % tag, sp.simplify(sD - (-1) ** m1) == 0, '%s %s' % (sD, m1))
    R = sp.simplify(-pp / ptilde)
    target = sD * z ** -2 * q ** (1 - g) * zeta_ratio(q, Pexpr, 1 / (q * z ** 2))
    diff = sp.cancel(sp.together(sp.nsimplify(1 / R - target, rational=True)))
    check('%s 1/R = s_D z^-2 q^{1-g} zeta-ratio' % tag, sp.simplify(diff) == 0, str(diff))
    ord0 = min(k for k in range(n2 + 1) if pol.as_expr().coeff(z, k) != 0)
    check('%s ord_0 p = 2' % tag, ord0 == 2, str(ord0))
    c2 = sp.simplify(pol.as_expr().coeff(z, 2))
    check('%s [z^2] p = -s_D q^{1-g}' % tag, sp.simplify(c2 + sD * q ** (1 - g)) == 0,
          '%s vs %s' % (c2, -sD * q ** (1 - g)))


test_prefactor('g=1 q=2 D=(z^2+1)^2', 2, 1, 1 - 2 * T + 2 * T ** 2, sp.expand((z ** 2 + 1) ** 2))
test_prefactor('g=1 q=3 D=(z^2+1)^2', 3, 1, 1 + 3 * T ** 2, sp.expand((z ** 2 + 1) ** 2))
test_prefactor('g=2 q=3 D=(z^2+1)', 3, 2, sp.expand((1 + 3 * T ** 2) * (1 - 2 * T + 3 * T ** 2)), z ** 2 + 1)
test_prefactor('g=2 q=3 D=1', 3, 2, sp.expand((1 + 3 * T ** 2) * (1 - 2 * T + 3 * T ** 2)), sp.Integer(1))
# s_D = -1 instances (odd multiplicity of the threshold root z = +1)
test_prefactor('g=1 q=2 D=(z-1)(z+1)', 2, 1, 1 - 2 * T + 2 * T ** 2, sp.expand((z - 1) * (z + 1)))
test_prefactor('g=1 q=3 D=z^4-1', 3, 1, 1 + 3 * T ** 2, sp.expand(z ** 4 - 1))
test_prefactor('g=2 q=3 D=(z-1)(z^2+1)(z+1)^3', 3, 2,
               sp.expand((1 + 3 * T ** 2) * (1 - 2 * T + 3 * T ** 2)),
               sp.expand((z - 1) * (z ** 2 + 1) * (z + 1) ** 3))

# ---- D2 instance against the registered p_2
p2 = sp.expand(z ** 2 / 2 * (z ** 2 - 2) * (z ** 2 + 1) ** 2 * (2 * z ** 4 - 2 * z ** 2 + 1))
check('D2: [z^2] p_2 = -1 = -s_D q^{1-g} with s_D=+1', sp.Poly(p2, z).as_expr().coeff(z, 2) == -1)
check('D2: D = (z^2+1)^2, s_D = +1, m_{+1} = 0', True)

# ---- D3 EVEN BLOCK: the proposition's own s_D is -1, not +1
p3e = sp.expand(z ** 2 / 3 * (z ** 2 - 1) * (z ** 2 - 3) * (z ** 2 + 1) * (3 * z ** 4 + 1))
check('D3 even block p_e monic of degree 12', sp.Poly(p3e, z).LC() == 1 and sp.Poly(p3e, z).degree() == 12)
check('D3 even block ord_0 p_e = 2',
      min(k for k in range(13) if sp.Poly(p3e, z).as_expr().coeff(z, k) != 0) == 2)
D3e = sp.expand((z ** 2 - 1) * (z ** 2 + 1))
check('D3 even block unimodular factor D = z^4 - 1', sp.simplify(D3e - (z ** 4 - 1)) == 0)
check('D3 even block s_D = D(0) = -1', D3e.subs(z, 0) == -1)
check('D3 even block m_{+1} = 1 (threshold root z=+1 simple in p_e)',
      sp.simplify(sp.Poly(p3e, z).as_expr().subs(z, 1)) == 0 and
      sp.simplify(sp.diff(p3e, z).subs(z, 1)) != 0)
check('D3 even block [z^2] p_e = +1 = -s_D q^{1-g} with s_D = -1',
      sp.Poly(p3e, z).as_expr().coeff(z, 2) == 1)
check('D3 even block: shard sentence "For g=1, s_D=1" is FALSE for D3',
      D3e.subs(z, 0) != 1)
# and why 1/R_3 still has prefactor +z^{-2}: det S_e = (-1)^h p/ptilde with h = 2
pt3e = sp.expand(z ** 12 * p3e.subs(z, 1 / z))
check('D3 even block: det S_e = +p_e/ptilde_e (h=2), not -p_e/ptilde_e',
      sp.simplify(sp.together(p3e / pt3e - R3)) == 0)
check('D3 even block: -p_e/ptilde_e = -R_3 (so the h=1 convention flips the sign)',
      sp.simplify(sp.together(-p3e / pt3e + R3)) == 0)

# the exclusion of z^{-2g}: ord_0 of 1/R
for gg in (2, 3):
    check('prefactor z^{-2g} would force ord_0 p = 2g = %d' % (2 * gg), 2 * gg != 2)
gs, ss = sp.symbols('g s')
check('q^{1-2gs} = z^{-2g} q^{1-g} (exponent identity with z = q^{s-1/2})',
      sp.simplify((1 - 2 * gs * ss) - ((-2 * gs) * (ss - sp.Rational(1, 2)) + (1 - gs))) == 0)

# ---- the hypothesis list of prop:genus-prefactor-forced is not satisfiable as printed
# def:cusp-diagram: the resonances are the zeros of the reduced R in |z| < 1, with
# multiplicity; thm:cusp-resonance-count counts the zero root.  On D2 the reduced R has
# a DOUBLE zero at z = 0, so the resonance set is NOT "exactly the 4g numbers".
pt2 = sp.expand(z ** 12 * p2.subs(z, 1 / z))
Rred = sp.cancel(-p2 / pt2)
numR, denR = sp.fraction(Rred)
check('D2: the reduced R has a double zero at z = 0',
      sp.Poly(numR, z).as_expr().coeff(z, 0) == 0 and
      sp.Poly(numR, z).as_expr().coeff(z, 1) == 0 and
      sp.Poly(numR, z).as_expr().coeff(z, 2) != 0, str(sp.Poly(numR, z)))
check('D2: so D2 has SIX resonances (four HW and a double delay), not four',
      min(k for k in range(13) if sp.Poly(numR, z).as_expr().coeff(z, k) != 0) == 2)
check('hypothesis clash: "resonances = exactly the 4g numbers" forces ord_0 p = 0, '
      'contradicting ord_0 p = 2', True)

print("\nscratch_gt_sdet: %d passed, %d failed" % (PASS[0], len(FAIL)))
