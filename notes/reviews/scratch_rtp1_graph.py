#!/usr/bin/env python3
"""REFUTE lane R, RTP-1 (claude:opus, 2026-09-24).  Claim C11 (lane B2.2) recomputed independently.
The random cubic graph is regenerated from the stated protocol (configuration model, random.Random(20260924),
first simple Ramanujan draw).  Traces by the Ihara-Bass route Tr B^k = Tr S_k(A) + (E - V)(1 + (-1)^k),
S_k = A S_(k-1) - q S_(k-2) (exact integers), cross-checked against Hashimoto powers; Ramanujan and simplicity by
the exact characteristic polynomial (squarefree test) plus a double-precision margin; Toeplitz forms at 250 digits
(mpmath).  Also the like-for-like comparison of the 'last datum missing' values with zeta.  Deterministic."""
import random, math
import numpy as np
import mpmath as mp
from flint import fmpz_mat, fmpz_poly
mp.mp.dps = 250
NCHK = [0, 0]
def check(c, m):
    NCHK[0] += 1; NCHK[1] += (not c); print(('PASS ' if c else 'FAIL ') + m, flush=True)
SEED, V, q = 20260924, 40, 2
rng = random.Random(SEED)
def draw():
    while True:
        pts = [v for v in range(V) for _ in range(3)]
        rng.shuffle(pts)
        E = set(); ok = True
        for i in range(0, len(pts), 2):
            a, b = pts[i], pts[i + 1]
            e = (min(a, b), max(a, b))
            if a == b or e in E: ok = False; break
            E.add(e)
        if ok: return sorted(E)
ndraw = 0
while True:
    Eg = draw(); ndraw += 1
    A = np.zeros((V, V), dtype=np.int64)
    for a, b in Eg: A[a, b] = A[b, a] = 1
    ev = np.linalg.eigvalsh(A.astype(float))
    nontriv = ev[:-1]
    if abs(ev[-1] - 3) < 1e-9 and np.abs(nontriv).max() < 2 * math.sqrt(2) - 1e-6: break
E = len(Eg)
Af = fmpz_mat([[int(x) for x in row] for row in A])
cp = Af.charpoly()
x = fmpz_poly([0, 1])
P, r = divmod(cp, x - 3)
g = P.gcd(P.derivative())
margin = 2 * math.sqrt(2) - np.abs(nontriv).max()
check(r == 0 and g.degree() == 0, f'G40 (draw {ndraw}, {E} edges): charpoly divisible by (x-3) once and the rest squarefree -> 39 simple nontrivial eigenvalues; Ramanujan margin to 2 sqrt 2 = {margin:.4f} (double eig), R = 78 atoms')
# traces, exact, two routes
K = 80
S = [2 * fmpz_mat(V, V, [int(i == j) for i in range(V) for j in range(V)]), Af]
for k in range(2, K + 1): S.append(Af * S[-1] - q * S[-2])
tr = [sum(int(S[k][i, i]) for i in range(V)) + (E - V) * (1 + (-1) ** k) for k in range(K + 1)]
tr[0] = 2 * E
D = [(a, b) for a, b in Eg] + [(b, a) for a, b in Eg]
idx = {d: i for i, d in enumerate(D)}
Bm = [[0] * len(D) for _ in D]
for (u, v) in D:
    for w in range(V):
        if (v, w) in idx and w != u: Bm[idx[(u, v)]][idx[(v, w)]] = 1
B = fmpz_mat(Bm); M = fmpz_mat(len(D), len(D), [int(i == j) for i in range(len(D)) for j in range(len(D))])
trB = [len(D)]
for k in range(1, 30): M = M * B; trB.append(sum(int(M[i, i]) for i in range(len(D))))
check(trB == tr[:30], 'Tr B^k by Hashimoto powers = Ihara-Bass route for k < 30')
triv = lambda k: q ** k + 1 + (E - V) * (1 + (-1) ** k)
nu = [mp.mpf(tr[k] - triv(k)) / mp.mpf(q) ** (mp.mpf(k) / 2) for k in range(K + 1)]
nu[0] = mp.mpf(tr[0] - triv(0))   # = 2E - 2 - 2(E - V) = 2V - 2 = 78 atoms of weight 1
check(nu[0] == 78, f'nu_0 = {nu[0]} = number of retained atoms (each of weight 1)')
def T(nus, n): return mp.matrix([[nus[abs(i - j)] for j in range(n)] for i in range(n)])
def lmin(nus, n): return min(mp.eigsy(T(nus, n), eigvals_only=True))
lm = {}
for KK in (6, 30, 54, 72, 76, 77, 78):
    lm[KK] = lmin(nu, KK + 1)
rates = [(-mp.log10(lm[b]) + mp.log10(lm[a])) / (b - a) for a, b in ((6, 30), (30, 54), (54, 72), (72, 77))]
print('   lambda_min(T_K): ' + ', '.join(f'K={k}: {mp.nstr(v, 4)}' for k, v in lm.items()))
print('   digits per unit K: ' + ', '.join(mp.nstr(r, 3) for r in rates) + ' ; as exponents of x_eq = 2^K: ' + ', '.join(mp.nstr(r / mp.log10(2), 3) for r in rates))
check(lm[77] > 0 and abs(lm[78]) < mp.mpf(10) ** -150 and abs(lm[77] - mp.mpf('7.00e-21')) < mp.mpf('0.01e-21'),
      f'T_77 PD (lambda_min {mp.nstr(lm[77], 4)}; lane 7.00e-21), T_78 singular (|lambda_min| = {mp.nstr(abs(lm[78]), 3)} at 250 digits): collapse at K = R = 78')
check(all(abs(r - t) < 0.02 for r, t in zip(rates, (0.13, 0.25, 0.47, 0.79))), 'rates 0.13, 0.25, 0.47, 0.79 digits per unit K reproduced (the rate itself grows 6-fold: no single power law)')
# next trace position in its disc: Verblunsky coefficients via Levinson (real data)
def levinson(nus, Kmax):
    a = [mp.mpf(1)]; e = nus[0]; refl = []
    for m in range(1, Kmax + 1):
        acc = mp.fsum(a[i] * nus[m - i] for i in range(m))
        k_ = -acc / e; refl.append(k_)
        a = [ (a[i] if i < m else 0) + k_ * (a[m - i] if m - i < m else 0) for i in range(m + 1)]
        a[0] = mp.mpf(1)
        e = e * (1 - k_ ** 2)
    return refl
refl = levinson(nu, 78)
# refl[m-1] is the reflection coefficient of lag m: position of nu_m in the disc of order K = m - 1
tau = {m - 1: refl[m - 1] for m in range(1, 79)}
inner = max(abs(tau[K_]) for K_ in range(0, 77))
check(inner < 1 and abs(abs(tau[77]) - 1) < mp.mpf(10) ** -100, f'next trace interior for every K < 77 (max |tau| = {mp.nstr(inner, 4)}), on the boundary at K = 77 (|tau| - 1 = {mp.nstr(abs(tau[77]) - 1, 3)})')
# fixed window K = 77, last cycle length missing
mob = lambda n: 0 if any(n % (p * p) == 0 for p in range(2, int(n ** 0.5) + 1)) else (-1) ** sum(1 for p in range(2, n + 1) if n % p == 0 and all(p % d for d in range(2, int(p ** 0.5) + 1)))
lpi = [0] + [sum(mob(l // d) * tr[d] for d in range(1, l + 1) if l % d == 0) for l in range(1, 79)]
nuP = list(nu); nuP[77] = nu[77] - mp.mpf(lpi[77]) / mp.mpf(q) ** (mp.mpf(77) / 2)
removed = mp.mpf(lpi[77]) / mp.mpf(q) ** (mp.mpf(77) / 2)
lP = lmin(nuP, 78)
check(abs(lP / mp.mpf('-3.89e11') - 1) < 0.01, f'K = 77, cycle length 77 removed: lambda_min = {mp.nstr(lP, 4)} (lane -3.89e11); removed datum = {mp.nstr(removed, 4)} -> |lambda_min|/|removed datum| = {mp.nstr(abs(lP)/removed, 4)}')
# graph PNT as max-det element: Hadamard, nu = (nu_0, 0, ...)
x_true = [mp.mpf(tr[k]) / mp.mpf(q) ** (mp.mpf(k) / 2) for k in range(78)]
x_pnt = [mp.mpf(triv(k)) / mp.mpf(q) ** (mp.mpf(k) / 2) for k in range(78)]
hs = lambda xs: mp.sqrt(mp.fsum((78 - k) * (2 if k else 1) * xs[k] ** 2 for k in range(1, 78)))
rel = hs([a - b for a, b in zip(x_true, x_pnt)]) / hs(x_true)
check(abs(rel / mp.mpf('4.7e-10') - 1) < 0.05, f'graph PNT (nu_k = 0, k >= 1; Hadamard max-det) relative HS distance from the truth at K = 77: {mp.nstr(rel, 3)} (lane 4.7e-10); by Hadamard this is the max-det element at EVERY K, not only the largest')
# like-for-like with zeta's fixed-window value (scratch_rtp1_fixedL.py): -5.66e-7 at N = 60 against the removed term's norm 0.23
print(f'   ratio |lambda_min| / ||removed datum||: graph {mp.nstr(abs(lP)/removed, 3)}; zeta (k = 49, L = log 50): 5.66e-7/0.231 = {5.66e-7/0.231:.2e} at N = 60, 0.0200/0.277 = {0.0200/0.277:.2e} at N = 240')
print(f'# checks: {NCHK[0]} run, {NCHK[1]} failed')
