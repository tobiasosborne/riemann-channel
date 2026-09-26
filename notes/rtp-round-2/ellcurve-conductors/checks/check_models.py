#!/usr/bin/env python3
"""Independent checks of the curve data in cremona_rows.txt (author claude:opus, 2026-09-26).

(1) pure python: b2,b4,b6,b8,c4,Delta from the a-invariants; the prime support of Delta equals the
    prime support of the conductor; multiplicative primes (p | Delta, p not | c4; valid for a minimal
    model at every p) are exactly the primes with exponent 1 in the conductor; minimality test
    v_p(Delta) < 12 or v_p(c4) < 4 (sufficient for minimality at p).
(2) PARI (cypari2, optional; pass --pari): ellglobalred conductor, ellminimalmodel == model, ellrootno,
    ellanalyticrank (an L-value computation at s = 1, no zeros), ellap for p < 200 printed for the zst cross-check.
No zeros of any L-function are computed or read.
"""
import sys
from pathlib import Path
here = Path(__file__).resolve().parent.parent

def factor(n):
    n = abs(n); f = {}; d = 2
    while d * d <= n:
        while n % d == 0: f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def vp(n, p):
    if n == 0: return 99
    k = 0
    while n % p == 0: n //= p; k += 1
    return k

rows = []
for line in (here / 'cremona_rows.txt').read_text().splitlines():
    if line.startswith('#') or not line.strip(): continue
    c, cl, num, ai, rk, tor = line.split()
    rows.append((f'{c}{cl}{num}', int(c), [int(t) for t in ai.strip('[]').split(',')], int(rk)))

fails = 0; checks = 0
def check(cond, msg):
    global fails, checks
    checks += 1
    if not cond: fails += 1; print('FAIL', msg)

print('label C Delta c4 support(Delta) factor(C) multiplicative')
for lab, C, (a1, a2, a3, a4, a6), rk in rows:
    b2 = a1*a1 + 4*a2; b4 = 2*a4 + a1*a3; b6 = a3*a3 + 4*a6
    b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
    c4 = b2*b2 - 24*b4
    D = -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6
    fC = factor(C); fD = factor(D)
    mult = sorted(p for p in fD if c4 % p != 0)
    check(D != 0, f'{lab} nonsingular')
    check(sorted(fD) == sorted(fC), f'{lab} bad primes {sorted(fD)} vs conductor primes {sorted(fC)}')
    check(mult == sorted(p for p, e in fC.items() if e == 1), f'{lab} multiplicative primes {mult} vs exponent-1 primes of C')
    inc = [p for p in fD if not (vp(D, p) < 12 or vp(c4, p) < 4)]
    if inc: print(f'# {lab}: sufficient minimality test inconclusive at {inc} (v_p(Delta) >= 12 and v_p(c4) >= 4); decided by PARI ellminimalmodel below')
    check(rk == 0, f'{lab} rank 0 in the table')
    print(lab, C, D, c4, sorted(fD), dict(fC), mult)

if '--pari' in sys.argv:
    import cypari2
    pari = cypari2.Pari(); pari.default('realprecision', 50)
    print('PARI', pari.version())
    print('label ellglobalred_N minimal rootno analyticrank ap(p<200)')
    for lab, C, ai, rk in rows:
        E = pari.ellinit(ai)
        N = int(pari.ellglobalred(E)[0])
        mm = [int(t) for t in pari.ellminimalmodel(E)[:5]] == ai
        w = int(pari.ellrootno(E)); ar = int(pari.ellanalyticrank(E)[0])
        check(N == C, f'{lab} PARI conductor {N}'); check(mm, f'{lab} PARI minimal model')
        check(w == 1, f'{lab} root number {w}'); check(ar == 0, f'{lab} analytic rank {ar}')
        aps = [int(pari.ellap(E, p)) for p in pari.primes(46)]  # primes < 200
        print(lab, N, int(mm), w, ar, ','.join(map(str, aps)))
print(f'# checks: {checks} run, {fails} failed')
sys.exit(bool(fails))
