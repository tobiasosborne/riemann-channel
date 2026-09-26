#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane P, item P4: the CAD envelope, H-LOG2 as quoted, the decimal bounds B(d).
H-LOG2 checked against the TeX e-print of Nesterenko-Waldschmidt, arXiv:math/0002047, main.tex lines 164-168
(fetched by the reviewer into the session scratchpad; not in refs/). mpmath, exact integers. Deterministic."""
import mpmath as mp, math, sympy as sp
mp.mp.dps = 100
ok = 0; bad = 0
def chk(name, cond):
    global ok, bad
    if cond: ok += 1; print("PASS", name)
    else: bad += 1; print("FAIL", name)

# ---- 1. CAD recurrences: delta_{i+1} = 2 delta_i^2 has closed form (2 delta)^{2^i}/2; h_i/delta_i <= h_0/delta + 3i
for dl in [2, 3, 8, 18]:
    di = dl; closed = True
    for i in range(6):
        closed &= (2 * di == (2 * dl) ** (2 ** i)); di = 2 * di * di
    chk("delta_i = (2 delta)^{2^i}/2 for delta = %d, i < 6" % dl, closed)
# the per-step inequality 2 d h + 2 d log2 d + log2((2d)!) <= 2 d h + 6 d^2 (d >= 1)
chk("log2((2x)!) + 2x log2 x <= 6 x^2 for x = 1..2000", all(math.lgamma(2 * x + 1) / math.log(2) + 2 * x * math.log2(x) <= 6 * x * x for x in range(1, 2001)))
# the "parenthesis" bound 1 + h0/delta + 3(k-1) <= tau + 4k + 1 with h0 = tau + k log2(delta+1), delta >= 2
chk("1 + h0/delta + 3(k-1) <= tau + 4k + 1 (grid)", all(1 + (t + k * math.log2(dl + 1)) / dl + 3 * (k - 1) <= t + 4 * k + 1
                                                       for t in range(1, 60) for k in range(1, 60) for dl in range(2, 40)))
# Mahler/length chain for integer factors: H(Q) <= 2^{deg P} L(P) on random factorable examples
import random
random.seed(5); x = sp.symbols('x'); good = True
for t in range(40):
    Q = sp.Poly([random.randint(-9, 9) or 1 for _ in range(random.randint(2, 5))], x)
    R = sp.Poly([random.randint(-9, 9) or 1 for _ in range(random.randint(2, 5))], x)
    P = Q * R
    good &= max(abs(c) for c in Q.all_coeffs()) <= 2 ** P.degree() * sum(abs(c) for c in P.all_coeffs())
chk("H(Q) <= 2^{deg P} L(P) for integer factors Q | P (40 random)", good)

# ---- 2. H-LOG2 exactly as in N-W Theorem 3(1); sanity on real approximants (degree 1 and 2)
def nw_bound(dg, L):
    return mp.e ** (-151000 * dg**2 * (mp.log(L) + dg * mp.log(dg)) / (1 + mp.log(dg)))
l2 = mp.log(2)
cf = mp.identify  # unused; use continued fraction convergents
a = []; y = l2
for i in range(25):
    ai = int(mp.floor(y)); a.append(ai); y = 1 / (y - ai)
p0, q0, p1, q1 = 1, 0, a[0], 1
okcf = True
for ai in a[1:]:
    p0, q0, p1, q1 = p1, q1, ai * p1 + p0, ai * q1 + q0
    L = max(3, abs(p1) + abs(q1))
    okcf &= abs(l2 - mp.mpf(p1) / q1) >= nw_bound(1, L)
chk("N-W bound holds (trivially) on 24 continued-fraction convergents of log 2", okcf)
# monotonicity of the exponent in the degree n (so replacing n by D is legitimate)
chk("exponent n^2 (log L + n log n)/(1 + log n) increasing in n (n = 1..2000, L = 3, 1e6)",
    all((lambda f: all(f(n + 1) > f(n) for n in range(1, 2000)))(lambda n, L=L: n * n * (math.log(L) + n * math.log(n)) / (1 + math.log(n))) for L in [3, 1e6]))

# ---- 3. the simplifications of step 5: for D >= 4, log(D+1) + D log D <= D^2; 151000((tau+1) log 2 + 1) <= 200000 (tau + 2)
chk("log(D+1) + D log D <= D^2 for D = 4..10^6 (sampled) and asymptotically", all(math.log(D + 1) + D * math.log(D) <= D * D for D in list(range(4, 5000)) + [10**k for k in range(4, 300)]))
chk("151000((tau+1) log 2 + 1) <= 200000 (tau + 2) for tau >= 0", all(151000 * ((t + 1) * math.log(2) + 1) <= 200000 * (t + 2) for t in range(0, 10**5, 7)))

# ---- 4. E(d) = log10(-log10 B(d)) = log10(200000 (tau+2)) + 2^{k+3} log10(2 s delta), interval arithmetic
rep = {2: '1.71528382146590596e22', 3: '1.95274538929341369e102', 4: '2.15629830912744022e315', 8: '1.43759761809591357e4954'}
iv = mp.iv; iv.dps = 80
for d in [2, 3, 4, 8]:
    k = 4 * d**4 + d**2 + 1; dl = 2 * d * d; s = 2 ** (2 * d * d) + 2 ** d + 2 * d * d; tau = 32 * d**4
    E = mp.log10(200000 * (tau + 2)) + mp.mpf(2) ** (k + 3) * mp.log10(2 * s * dl)
    Ei = iv.log(iv.mpf(200000 * (tau + 2)), 10) + iv.mpf(2) ** (k + 3) * iv.log(iv.mpf(2 * s * dl), 10)
    relerr = abs(E / mp.mpf(rep[d]) - 1)
    chk("d=%d E(d) = %s agrees with the report to 17 digits (rel. diff %s); relative interval width %s" % (d, mp.nstr(E, 18), mp.nstr(relerr, 3), mp.nstr(mp.mpf(Ei.delta.b) / E, 3)),
        relerr < mp.mpf(10) ** -16 and Ei.a <= E <= Ei.b)
    # sharper exponent actually delivered by the lane's own derivation: D' = delta_{k-1} = (2 delta)^{2^{k-2}}... (see note)
    Dp_log10 = mp.mpf(2) ** (k - 1) * mp.log10(2 * dl) - mp.log10(2)            # log10 delta_{k-1}
    # log2 H' <= D' (tau + 4k + 1); exponent C' <= 151000 D'^2 (log((D'+1) H') + D' log D') <= 151000 D'^3 ((tau+4k+1) log 2 + 2) (crude)
    Cp_log10 = mp.log10(151000) + 3 * Dp_log10 + mp.log10((tau + 4 * k + 1) * mp.log(2) + 2)
    print("   d=%d  report E(d) = %s   sharper (D = delta_{k-1}) log10 C' <= %s   ratio %s" % (d, mp.nstr(E, 8), mp.nstr(Cp_log10, 8), mp.nstr(Cp_log10 / E, 4)))
print("checks passed %d failed %d" % (ok, bad))
