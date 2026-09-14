"""Exact finite checks for astra-structure.md; no zero data or dependencies.

The Fourier checks use unnormalized Ramanujan sums and sqrt(p) V_p.
The matrix checks use a cyclic Fourier compression large enough to contain
every mode contributing to the explicitly checked low matrix entries.
These are checks of the written proofs, not substitutes for those proofs.
"""

from collections import Counter
from fractions import Fraction as Q
from math import gcd


def shell(b):
    return {Q(a, b): Q(1) for a in range(b) if gcd(a, b) == 1}


def phi(b):
    return len(shell(b))


def add(*vectors):
    out = Counter()
    for vector in vectors:
        for r, value in vector.items():
            out[r] += value
    return {r: value for r, value in out.items() if value}


def scale(a, vector):
    return {r: a * value for r, value in vector.items() if a * value}


def forward(p, vector):
    """sqrt(p) V_p on finite Fourier polynomials, exactly."""
    return add(*({(r + k) / p: value for k in range(p)}
                 for r, value in vector.items()))


def backward(p, vector):
    """sqrt(p) V_p^* on finite Fourier polynomials, exactly."""
    return add(*({(p * r) % 1: value}
                 for r, value in vector.items()))


checks = 0
for p in (2, 3, 5, 7):
    for b in range(1, 41):
        expected = shell(p * b) if b % p == 0 else add(shell(b), shell(p * b))
        assert forward(p, shell(b)) == expected
        expected = (scale(Q(phi(b), phi(b // p)), shell(b // p))
                    if b % p == 0 else shell(b))
        assert backward(p, shell(b)) == expected
        checks += 2

for n in range(1, 81):
    divisors = [d for d in range(1, n + 1) if n % d == 0]
    assert add(*(shell(d) for d in divisors)) == {Q(a, n): Q(1) for a in range(n)}
    assert sum(phi(d) for d in divisors) == n
    checks += 2

# Nontrivial modulo-3 character and an imprimitive modulo-6 character.
g3 = {Q(1, 3): Q(1), Q(2, 3): Q(-1)}
assert backward(2, g3) == scale(-1, g3)
assert backward(3, g3) == {}
g6 = {Q(1, 6): Q(1), Q(5, 6): Q(-1)}
assert backward(2, g6) == g3
checks += 3


def zero(n):
    return [[Q(0) for _ in range(n)] for _ in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    n = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(n)), Q(0))
             for j in range(n)] for i in range(n)]


def lin(*terms):
    n = len(terms[0][1])
    return [[sum((c * a[i][j] for c, a in terms), Q(0))
             for j in range(n)] for i in range(n)]


def dissipator_scaled(a, rho, divisor):
    """D_{a/sqrt(divisor)}(rho), with real exact entries."""
    at = transpose(a)
    ata = mul(at, a)
    return lin((Q(1, divisor), mul(mul(a, rho), at)),
               (-Q(1, 2 * divisor), mul(ata, rho)),
               (-Q(1, 2 * divisor), mul(rho, ata)))


n = 8
# A = sqrt(2) P_N V_2 P_N, rows and columns indexed by r = j/N.
a = [[Q(int((2 * i - j) % n == 0)) for j in range(n)] for i in range(n)]
vac = zero(n)
vac[0][0] = Q(1)
lvac = dissipator_scaled(a, vac, 2)
assert lvac[0][n // 2] == Q(1, 2)  # even input creates odd coherences
assert lvac[n // 2][n // 2] == Q(1, 2)
assert lvac[0][0] == -Q(1, 2)
checks += 3

# The (vacuum, shell-2) derivative only depends on weights w_0 and w_1.
# Later shell weights of the geometric density cannot affect this entry.
rho = zero(n)
rho[0][0], rho[n // 2][n // 2] = Q(1), Q(1, 2)
lrho = lin((Q(1), dissipator_scaled(a, rho, 2)),
           (Q(2), dissipator_scaled(transpose(a), rho, 2)))
assert lrho[0][n // 2] == -Q(1, 4)  # u=1, d=2, beta=1
checks += 1

# Check the conserved V_2 matrix element on the low vacuum/shell coherence.
coherence = zero(n)
coherence[0][n // 2] = Q(1)
lcoherence = dissipator_scaled(a, coherence, 2)
assert sum(mul(a, lcoherence)[i][i] for i in range(n)) == 0
assert sum(mul(a, coherence)[i][i] for i in range(n)) == 1
checks += 2

ordered_products = Counter(p * q for p in (2, 3) for q in (2, 3))
assert ordered_products[6] == 2
assert ordered_products[4] == 1
checks += 2

# Euler--Maclaurin's exact value at -2, where all higher terms vanish.
assert -Q(1, 3) + Q(1, 2) - Q(1, 6) == 0
checks += 1

print(f"{checks} exact finite checks passed.")
