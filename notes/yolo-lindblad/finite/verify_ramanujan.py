#!/usr/bin/env python3
"""N3: exact cyclotomic and rational checks; smooth-prime restriction explicit."""
import itertools
import math
import sympy as sp
from finite_common import Checks, divisors, primes


def c(b, n):
    return sum(sp.Integer(d)*sp.mobius(b//d) for d in divisors(math.gcd(b, n)))


def valuation(n, p):
    k = 0
    while n % p == 0:
        n //= p; k += 1
    return k


def main():
    check = Checks("verify_ramanujan")
    x = sp.symbols("x")
    # Fourier definition certified in Q[x]/Phi_b(x), not rounded roots of unity.
    for b in divisors(840):
        cyclo = sp.Poly(sp.cyclotomic_poly(b, x), x)
        for n in (1, 2, 3, 5, 6, 12, 30):
            poly = sp.Poly(sum(x**((a*n) % b) for a in range(b) if math.gcd(a, b) == 1), x)
            check((poly - sp.Poly(c(b, n), x)).rem(cyclo).is_zero,
                  f"b={b}, n={n}: Fourier Ramanujan sum = divisor formula, exact")
        check(c(b, 1) == sp.mobius(b), f"b={b}: c_b(1)=mu(b), exact")
        for beta in (2, 3):
            # Sum over independent p-adic valuations with exact geometric tails.
            expectation = sp.Integer(1)
            for p0, k in sp.factorint(b).items():
                p, k = int(p0), int(k)
                r = sp.Rational(1, p**beta)
                local = sum((1-r)*r**v*c(p**k, p**v) for v in range(k)) + r**k*c(p**k, p**k)
                expectation *= local
            divisor_formula = sum(sp.mobius(b//d)*sp.Rational(1, d**(beta - 1)) for d in divisors(b))
            product_formula = sp.Rational(1, b**(beta - 1))*sp.prod(1-p**(beta - 1) for p in sp.factorint(b))
            check(expectation == divisor_formula == product_formula,
                  f"b={b}, beta={beta}: Haar-Gibbs phase expectation, exact rational")
    rows = []
    for P in (5, 7, 13, 31):
        pp = primes(P)
        for n in range(1, 31):
            nu = [valuation(n, p) for p in pp]
            nP = math.prod(p**v for p, v in zip(pp, nu))
            terms = []
            for exponents in itertools.product(*(range(v + 2) for v in nu)):
                b = math.prod(p**k for p, k in zip(pp, exponents))
                # Independent multiplicative form; certified against c on smaller cutoffs.
                cb = sp.prod(c(p**k, n) for p, k in zip(pp, exponents))
                terms.append((b, cb))
            for s in (2, 3):
                lhs = sum(cb*sp.Rational(1, b**s) for b, cb in terms)
                inv_zetaP = sp.prod(1-sp.Rational(1, p**s) for p in pp)
                sigma = sum(sp.Rational(1, d**(s - 1)) for d in divisors(nP))
                rhs = inv_zetaP*sigma
                check(lhs == rhs, f"P={P}, n={n}, s={s}: complete smooth b-series, {len(terms)} exact terms")
                if n in (1, 6, 29, 30):
                    rows.append(dict(P=P, n=n, nP=nP, s=s, terms=len(terms), value=str(lhs)))
    # The critical limit is elementary, including b=1.
    t = sp.symbols("t", positive=True)
    for b in divisors(120):
        # t_p -> 1 independently: local t_p^k - t_p^(k-1) vanishes.
        polynomial = sp.sympify(sp.prod(t**int(k)-t**(int(k)-1) for k in sp.factorint(b).values()))
        check(polynomial.subs(t, 1) == (1 if b == 1 else 0), f"b={b}: critical expectation limit")
    print("selected exact rows:", rows)
    check.finish(dict(rows=rows, note="Smooth identity uses n_P; exponents beyond v_p(n)+1 vanish exactly."))


if __name__ == "__main__":
    main()
