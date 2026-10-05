"""Checks for §14 of notes/adelic-gkp/adelic-gkp.md (K = Q(sqrt 2)).

Q1  Class number formula / residue: res_{s=1} zeta_K = L(1, chi_8) = log(1+sqrt2)/sqrt2  (r1 = 2, h = 1, w = 2, |d| = 8).
Q2  Euler factors by splitting type (2 ramified; p = +-1 mod 8 split; p = +-3 mod 8 inert) reproduce zeta(2) L(2, chi_8).
Q3  Multiplication by eps = 1+sqrt2 on (a, b) (x = a + b sqrt2) is [[1,2],[1,1]], det -1 = N(eps), eigenvalues 1 +- sqrt2:
    a hyperbolic element of GL_2(Z), and in the two real embeddings diag(1+sqrt2, 1-sqrt2), net |N| = 1.
Q4  Trace form in basis {1, sqrt2} is diag(2, 4); sigma1(x)^2 + sigma2(x)^2 = 2a^2 + 4b^2.
Q5  Different: d = (2 sqrt2) = (sqrt2)^3, N(d) = 8 = |d_K|; the dual of Z[sqrt2] under Tr is (1/(2 sqrt2)) Z[sqrt2],
    checked as the inverse transpose of the trace Gram matrix.
Q6  No fractional ideal a = (sqrt2)^k at 2 has a^2 = d^{-1} (odd exponent 3): parity check.
"""
import mpmath as mp

mp.mp.dps = 30
ok = fail = 0


def report(name, good, info=""):
    global ok, fail
    ok += good
    fail += (not good)
    print(f"{'PASS' if good else 'FAIL'}  {name} {info}")


def chi8(n):
    if n % 2 == 0:
        return 0
    return 1 if n % 8 in (1, 7) else -1


def L(s):
    return mp.nsum(lambda k: sum(chi8(int(8 * k + r)) / mp.mpf(8 * k + r) ** s for r in (1, 3, 5, 7)), [0, mp.inf])


# Q1
L1 = L(1)
target = mp.log(1 + mp.sqrt(2)) / mp.sqrt(2)
report("Q1 L(1,chi8) = log(1+sqrt2)/sqrt2", abs(L1 - target) < mp.mpf(10) ** -25, f"({mp.nstr(L1, 20)})")
cnf = 2 ** 2 * 1 * mp.log(1 + mp.sqrt(2)) / (2 * mp.sqrt(8))
report("Q1 class number formula 2^r1 h R/(w sqrt|d|) equals it", abs(cnf - target) < mp.mpf(10) ** -25)

# Q2
N = 200000
sieve = bytearray([1]) * N
sieve[0] = sieve[1] = 0
for i in range(2, int(N ** 0.5) + 1):
    if sieve[i]:
        sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
P = mp.mpf(1)
for p in (i for i in range(N) if sieve[i]):
    if p == 2:
        f = 1 / (1 - mp.mpf(2) ** -2)
    elif p % 8 in (1, 7):
        f = 1 / (1 - mp.mpf(p) ** -2) ** 2
    else:
        f = 1 / (1 - mp.mpf(p) ** -4)
    P *= f
T = mp.zeta(2) * L(2)
report("Q2 Euler product by splitting type vs zeta(2)L(2,chi8)", abs(P - T) / T < mp.mpf(10) ** -5,
       f"(rel err {mp.nstr(abs(P - T) / T, 3)}, primes < {N})")

# Q3
M = mp.matrix([[1, 2], [1, 1]])
ev = sorted([mp.re(e) for e in mp.eig(M)[0]])
report("Q3 det = -1", abs(mp.det(M) + 1) < mp.mpf(10) ** -25)
report("Q3 eigenvalues 1 -+ sqrt2", abs(ev[0] - (1 - mp.sqrt(2))) + abs(ev[1] - (1 + mp.sqrt(2))) < mp.mpf(10) ** -25)
# action on (a,b): (a + b r)(1 + r) = (a + 2b) + (a + b) r with r^2 = 2
for a, b in [(3, -1), (0, 1), (5, 7)]:
    x = a + b * mp.sqrt(2)
    y = x * (1 + mp.sqrt(2))
    report(f"Q3 matrix matches multiplication at ({a},{b})",
           abs(y - ((a + 2 * b) + (a + b) * mp.sqrt(2))) < mp.mpf(10) ** -25)

# Q4
for a, b in [(1, 0), (0, 1), (2, -3)]:
    s1, s2 = a + b * mp.sqrt(2), a - b * mp.sqrt(2)
    report(f"Q4 s1^2+s2^2 = 2a^2+4b^2 at ({a},{b})", abs(s1 ** 2 + s2 ** 2 - (2 * a * a + 4 * b * b)) < mp.mpf(10) ** -25)

# Q5: Gram of trace form G = diag(2,4); dual lattice basis = G^{-1} columns: 1/2 and sqrt2/4 = 1/(2 sqrt2) * (sqrt2, 1)
G = mp.matrix([[2, 0], [0, 4]])
Gi = G ** -1
dual = [Gi[0, 0] * 1, Gi[1, 1] * mp.sqrt(2)]  # 1/2 and sqrt2/4
c = 1 / (2 * mp.sqrt(2))
gens = [c * mp.sqrt(2), c * 1]  # (1/(2 sqrt2)) * {sqrt2, 1} spans (1/(2sqrt2)) Z[sqrt2]
report("Q5 dual basis = (1/(2 sqrt2)) Z[sqrt2] basis", abs(dual[0] - gens[0]) + abs(dual[1] - gens[1]) < mp.mpf(10) ** -25)
report("Q5 N(2 sqrt2) = -8", abs((2 * mp.sqrt(2)) * (-2 * mp.sqrt(2)) + 8) < mp.mpf(10) ** -25)

# Q6
report("Q6 no k with 2k = -3", all(2 * k != -3 for k in range(-20, 21)))

print(f"\n{ok} passed, {fail} failed")
