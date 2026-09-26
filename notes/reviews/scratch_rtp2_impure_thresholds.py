#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane I (claude:opus, 2026-09-26): I1 threshold table and E/H/R classification.
Independent of scripts/rtp2_impure_bumps.py: brute force over ALL prime powers in a log-window around every
lattice ratio (no nearest-neighbour shortcut), separations as exact Fractions, logs by mpmath at 40 digits.
Also: the external-prime support lists of the report (I2/I4) and the first-overlap widths."""
import math, itertools, bisect
from fractions import Fraction
import mpmath as mp
mp.mp.dps = 40
NC = [0, 0]
def check(c, m):
    NC[0] += 1; NC[1] += (not c); print(('PASS ' if c else 'FAIL ') + m, flush=True)
X = 2_000_000
sv = bytearray([1]) * (X + 1); sv[0] = sv[1] = 0
for p in range(2, int(X ** .5) + 1):
    if sv[p]: sv[p*p::p] = bytearray(len(sv[p*p::p]))
PP = {}
for p in range(2, X + 1):
    if sv[p]:
        k = p
        while k <= X: PP[k] = p; k *= p
KS = sorted(PP)
def vp(k, p):
    m = 0
    while k % p == 0: k //= p; m += 1
    return m
def ratios(S, A):
    rs = set()
    for e in itertools.product(range(-A, A + 1), repeat=len(S)):
        r = Fraction(1)
        for p, a in zip(S, e): r *= Fraction(p) ** a
        if r >= 1: rs.add(r)
    return rs
def kind(k, S, A):
    p = PP[k]
    if p not in S: return 'E'
    return 'H' if vp(k, p) > A else 'R'
def onset(S, A, window=Fraction(2)):
    """min over lattice ratios r and prime powers k of the class, k != r, of max(k/r, r/k); brute force in [r/2, 2r]."""
    best = {}
    rs = ratios(S, A)
    for r in rs:
        lo, hi = r / window, r * window
        for k in KS[bisect.bisect_left(KS, math.floor(lo)): bisect.bisect_right(KS, math.ceil(hi))]:
            if Fraction(k) == r: continue
            sep = max(Fraction(k) / r, r / Fraction(k))
            c = kind(k, S, A)
            for cl in (c, 'all'):
                if cl not in best or sep < best[cl][0]: best[cl] = (sep, r, k)
    return best, max(rs)
# report table (E, H columns): (S, A) -> ((deltaE, r, k), (deltaH, r, k))
REP = {((2,), 1): (('0.20273255405', '2', 3), ('0.34657359028', '2', 4)),
       ((2,), 2): (('0.11157177566', '4', 5), ('0.34657359028', '4', 8)),
       ((2,), 3): (('0.058891517828', '8', 9), ('0.34657359028', '8', 16)),
       ((2,), 4): (('0.030312310908', '16', 17), ('0.34657359028', '16', 32)),
       ((2, 3), 1): (('0.077075339914', '6', 7), ('0.14384103623', '3', 4)),
       ((2, 3), 2): (('0.013699487094', '36', 37), ('0.058891517828', '9', 8)),
       ((2, 3), 3): (('0.0046083275525', '108', 109), ('0.058891517828', '18', 16)),
       ((2, 3), 4): (('0.00038565370211', '1296', 1297), ('0.058891517828', '36', 32)),
       ((2, 3, 5), 1): (('0.016394911411', '30', 31), ('0.032269260569', '15/2', 8)),
       ((2, 3, 5), 2): (('0.0011123475111', '450', 449), ('0.02041099726', '25/3', 8)),
       ((2, 3, 5), 3): (('3.7038408847e-05', '13500', 13499), ('0.011858263309', '125/8', 16)),
       ((2, 3, 5), 4): (('1.2345663771e-06', '405000', 405001), ('0.0056470033094', '2025/16', 128))}
A2 = {((2,), 1): '0.2027325541', ((2,), 2): '0.1115717757', ((2,), 3): '0.05889151783', ((2,), 4): '0.03031231091',
      ((2, 3), 1): '0.07707533991', ((2, 3), 2): '0.01369948709', ((2, 3), 3): '0.004608327552', ((2, 3), 4): '0.0003856537021',
      ((2, 3, 5), 1): '0.01639491141', ((2, 3, 5), 2): '0.001112347511', ((2, 3, 5), 3): '3.703840885e-5', ((2, 3, 5), 4): '1.234566377e-6'}
for (S, A), (e, h) in REP.items():
    best, rmax = onset(S, A)
    dl = {c: mp.log(mp.mpf(b[0].numerator) / b[0].denominator) / 2 for c, b in best.items()}
    okE = abs(dl['E'] - mp.mpf(e[0])) < mp.mpf(e[0]) * 1e-9
    okH = abs(dl['H'] - mp.mpf(h[0])) < mp.mpf(h[0]) * 1e-9
    # binding pair: exact separation of the report's pair must equal the minimum (ties allowed)
    sepE = max(Fraction(e[2]) / Fraction(e[1]), Fraction(e[1]) / Fraction(e[2]))
    sepH = max(Fraction(h[2]) / Fraction(h[1]), Fraction(h[1]) / Fraction(h[2]))
    okpair = sepE == best['E'][0] and sepH == best['H'][0] and Fraction(e[1]) in ratios(S, A) and Fraction(h[1]) in ratios(S, A)
    okall = best['all'][0] == best['E'][0] and abs(dl['all'] - mp.mpf(A2[(S, A)])) < mp.mpf(A2[(S, A)]) * 1e-9
    # sieve sufficiency: window [r/2, 2r] with 2r <= X
    check(okE and okH and okpair and okall and 2 * rmax < X,
          f'S={S} A={A}: E {mp.nstr(dl["E"],12)} ({best["E"][1]}:{best["E"][2]}), H {mp.nstr(dl["H"],12)} ({best["H"][1]}:{best["H"][2]}), '
          f'R-leak onset {mp.nstr(dl.get("R", mp.inf),6) if "R" in best else "none"}; all = E = lane A2 delta_max {A2[(S,A)]}')
    print(f'    R leakage: {best.get("R")}')
# the report's explicit R example and threshold of the "numerical check"
check(abs(mp.log(mp.mpf(4) / 3) / 2 - mp.mpf('0.1438410362')) < 1e-9 and Fraction(3, 2) in ratios((2, 3), 1), '{2,3} A=1: k=2 reaches mixed ratio 3/2 at delta = log(4/3)/2 = 0.1438410362')
dH = mp.log(mp.mpf(25) / 24) / 2
check(mp.nstr(dH, 30) == mp.nstr(mp.mpf('0.02041099726012756477728853257766'), 30), f'delta_H({{2,3,5}},2) = log(25/24)/2 = {mp.nstr(dH, 32)}')
# first-overlap widths: half the smallest log gap between lattice points
for S, A, rep in (((2, 3), 2, 0.1438410362), ((2, 3), 3, 0.05889151783), ((2, 3, 5), 2, 0.05268025783)):
    ns = sorted(math.prod(p ** a for p, a in zip(S, e)) for e in itertools.product(range(A + 1), repeat=len(S)))
    g = min(Fraction(b, a) for a, b in zip(ns, ns[1:]))
    d = mp.log(mp.mpf(g.numerator) / g.denominator) / 2
    check(abs(d - rep) < 1e-10, f'first overlap S={S} A={A}: ratio {g}, delta {mp.nstr(d, 12)} (report {rep})')
# external prime lists (report I2/I4 table), from the support condition |log k -+ D| < 2 delta over ALL pairs incl. axes/diagonal
REPL = {(2, 0.02): [37], (2, 0.05): [11, 13, 17, 19, 37], (2, 0.1): [5, 7, 11, 13, 17, 19, 31, 37, 41, 43],
        (2, 0.2): [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53],
        (3, 0.02): [7, 13, 37, 53, 71, 73, 107, 109, 211, 223]}
for (A, d), lst in REPL.items():
    ext = set()
    for r in ratios((2, 3), A):
        D = mp.log(mp.mpf(r.numerator) / r.denominator)
        for k in KS[: bisect.bisect_right(KS, int(mp.exp(D + 2 * d)) + 1)]:
            if PP[k] in (2, 3): continue
            lk = mp.log(k)
            if abs(lk - D) < 2 * d or abs(lk + D) < 2 * d: ext.add(PP[k])
    check(sorted(ext) == lst, f'external primes {{2,3}} A={A} delta={d}: {sorted(ext)}')
print(f'# checks: {NC[0]} run, {NC[1]} failed')
# ---- ties: all minimising (r, k) pairs per class (the report calls its pair "the" binding pair) ----
for (S, A) in REP:
    best, _ = onset(S, A)
    for cl in ('E', 'H'):
        sep = best[cl][0]; ties = []
        for r in ratios(S, A):
            for k in KS[bisect.bisect_left(KS, math.floor(r / 2)): bisect.bisect_right(KS, math.ceil(r * 2))]:
                if Fraction(k) != r and kind(k, S, A) == cl and max(Fraction(k) / r, r / Fraction(k)) == sep: ties.append(f'{r}:{k}')
        if len(ties) > 1: print(f'    tie S={S} A={A} class {cl}: {sorted(ties)}')
