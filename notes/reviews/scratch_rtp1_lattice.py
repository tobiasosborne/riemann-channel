#!/usr/bin/env python3
"""REFUTE lane R, RTP-1 (claude:opus, 2026-09-24).  Claims C4-C5 (lane A2) recomputed independently.
Gram entries of QW on the bump lattice from the definitions in real space (no Taylor series, no closed forms
of lane A2): R_1 by mpmath quad; archimedean part of an off-diagonal entry as delta^2 int R_1(u) rho(D + delta u) du
on the reviewer's own tanh-sinh nodes; diagonal from W_R's defining formula with the exact tail
int_{2 delta}^oo dy/sinh y; prime term summed over ALL prime powers with |log k -+ D| < 2 delta (no admissibility
assumed); pole 2 cosh(D/2) c_delta^2.  mpmath 30 digits; eigenpairs by mpmath.eigsy.  Deterministic."""
import sys, os, math, itertools
from functools import lru_cache
import mpmath as mp
mp.mp.dps = 30
NCHK = [0, 0]
def check(c, m):
    NCHK[0] += 1; NCHK[1] += (not c); print(('PASS ' if c else 'FAIL ') + m, flush=True)

def sieve_pp(X):
    s = bytearray([1]) * (X + 1); pp = {}
    for p in range(2, X + 1):
        if s[p]:
            s[p * p::p] = bytearray(len(s[p * p::p]))
            k = p
            while k <= X: pp[k] = p; k *= p
    return pp
PP = sieve_pp(1_700_000)
PPs = sorted(PP)
import bisect
# ---------- delta_max table (exact up to 30 digits) ----------
def ratios(S, A):
    pts = list(itertools.product(range(A + 1), repeat=len(S)))
    ns = [math.prod(p ** a for p, a in zip(S, pt)) for pt in pts]
    rs = set()
    for x in ns:
        for y in ns:
            if y >= x: rs.add(mp.mpf(y) / x if y % x else y // x)
    return pts, ns, rs
def delta_max(S, A):
    _, ns, _ = ratios(S, A)
    best = (mp.log(2) / 2, '1 vs 2')
    fr = set()
    for x in ns:
        for y in ns:
            if y > x: fr.add((y // math.gcd(x, y), x // math.gcd(x, y)))
    for (num, den) in fr:
        r = mp.mpf(num) / den
        i = bisect.bisect_left(PPs, int(r))
        for k in PPs[max(0, i - 3): i + 4]:
            if den == 1 and k == num: continue
            d = abs(mp.log(k) - mp.log(r)) / 2
            if d < best[0]: best = (d, f'{num}/{den} vs {k}')
    return best
lane = {((2,), 1): '0.2027325541', ((2,), 2): '0.1115717757', ((2,), 3): '0.05889151783', ((2,), 4): '0.03031231091',
        ((2,), 5): '0.01587434916', ((2,), 6): '0.01587434916', ((2, 3), 1): '0.07707533991', ((2, 3), 2): '0.01369948709',
        ((2, 3), 3): '0.004608327552', ((2, 3), 4): '0.0003856537021', ((2, 3, 5), 1): '0.01639491141',
        ((2, 3, 5), 2): '0.001112347511', ((2, 3, 5), 3): '3.703840885e-5', ((2, 3, 5), 4): '1.234566377e-6'}
DM = {}
for (S, A), v in lane.items():
    d, pair = delta_max(S, A)
    DM[(S, A)] = d
    check(abs(d - mp.mpf(v)) < mp.mpf(v) * 1e-9, f'delta_max{S} A={A} = {mp.nstr(d, 10)} ({pair}); lane A2 {v}')

# ---------- entries ----------
phi1 = lambda t: mp.exp(-1 / (1 - t * t)) if abs(t) < 1 else mp.mpf(0)
@lru_cache(maxsize=None)
def R1(u):
    u = mp.mpf(u); lo, hi = max(-1, u - 1), min(1, u + 1)
    if lo >= hi: return mp.mpf(0)
    return mp.quad(lambda s: phi1(s) * phi1(s - u), [lo, (lo + hi) / 2, hi])
R10 = R1(0)
# tanh-sinh nodes on [-2, 2] for the archimedean convolution
h = mp.mpf(1) / 128   # R_1 is Gevrey (not analytic): tanh-sinh converges sub-exponentially; 1/128 gives ~1e-15
NODES = []
k = 0
while True:
    t = k * h
    x = 2 * mp.tanh(mp.pi / 2 * mp.sinh(t)); wgt = 2 * h * (mp.pi / 2) * mp.cosh(t) / mp.cosh(mp.pi / 2 * mp.sinh(t)) ** 2
    if 2 - x < mp.mpf(10) ** -28: break
    NODES.append((x, wgt)); 
    if k: NODES.append((-x, wgt))
    k += 1
RN = [(x, w * R1(x)) for x, w in NODES]
mu0 = mp.quad(phi1, [-1, 0, 1])
_d = abs(mp.fsum(w for _, w in RN) - mu0 ** 2)
check(_d < 1e-12, f'tanh-sinh rule on [-2,2] ({len(NODES)} nodes): int R_1 = mu_0^2 (independent moment) to {mp.nstr(_d, 2)}')
rho = lambda y: mp.e ** (y / 2) / (mp.e ** y - mp.e ** (-y))
def arch_off(D, dl):
    return dl ** 2 * mp.fsum(w * rho(D + dl * x) for x, w in RN)
def arch_diag(dl):
    R0 = dl * R10
    f = lambda s: (2 * dl * R1(s) - 2 * mp.e ** (-dl * s / 2) * R0) * rho(dl * s) * dl
    return (mp.log(4 * mp.pi) + mp.euler) * R0 + mp.quad(f, [0, 1, 2]) + R0 * mp.log(mp.tanh(dl))
def c_delta(dl): return dl * mp.quad(lambda t: phi1(t) * mp.e ** (dl * t / 2), [-1, 0, 1])
def prime_term(D, dl):
    tot = mp.mpf(0)
    lo, hi = mp.e ** (D - 2 * dl), mp.e ** (D + 2 * dl)
    for kk in PPs[bisect.bisect_left(PPs, int(lo)): bisect.bisect_right(PPs, int(hi) + 1)]:
        u = (mp.log(kk) - D) / dl
        if abs(u) < 2: tot += mp.log(PP[kk]) / mp.sqrt(kk) * dl * R1(u)
    return tot    # the (log k + D) branch never contributes: log k + D >= log 2 > 2 delta for every delta used
def gram(S, A, dl, drop_mixed=None):
    pts = list(itertools.product(range(A + 1), repeat=len(S)))
    t = [sum(a * mp.log(p) for a, p in zip(pt, S)) for pt in pts]
    nrm = dl * R10; cd2 = c_delta(dl) ** 2
    diag = (2 * cd2 - arch_diag(dl)) / nrm
    n = len(pts); G = mp.matrix(n, n); parts = {}
    cache = {}
    for i in range(n):
        for j in range(n):
            if i == j: G[i, j] = diag; continue
            D = abs(t[i] - t[j]); key = mp.nstr(D, 25)
            if key not in cache:
                cache[key] = (2 * mp.cosh(D / 2) * cd2 / nrm, arch_off(D, dl) / nrm, prime_term(D, dl) / nrm)
            po, ar, pr = cache[key]
            mixed = sum(a != b for a, b in zip(pts[i], pts[j])) >= 2
            parts[(i, j)] = (po, ar, pr, mixed)
            G[i, j] = po - ar - pr
    return pts, G, parts, diag
def eig(G):
    E, Q = mp.eigsy(G)
    idx = sorted(range(len(E)), key=lambda i: E[i])
    return [E[i] for i in idx], [[Q[r, i] for r in range(G.rows)] for i in idx]
def trunc4(x):  # round down to 4 significant digits, as lane A2
    e = math.floor(math.log10(x)); return math.floor(x / 10 ** (e - 3)) * 10 ** (e - 3)
# ---------- measurements ----------
A2rows = {  # lane A2 table: (S, A, delta) -> (d, lam(G), lam(nomix), lam(noP))
    ((2,), 1, 0.1824): (0.220168, 0.044731016, 0.044731016, -0.0945246), ((2,), 3, 0.05300): (1.11944, 0.29004107, 0.29004107, 0.872899),
    ((2, 3), 1, 0.06936): (0.892886, 0.20834288, 0.059879534, 0.630368), ((2, 3), 1, 0.02312): (1.87154, 0.89532959, 0.84431801, 1.78405),
    ((2, 3), 1, 0.007707): (2.93014, 1.8552569, 1.8381324, 2.90098), ((2, 3), 2, 0.01232): (2.47301, 0.76014856, 0.61293939, 2.30378),
    ((2, 3), 2, 0.004109): (3.54977, 1.6558568, 1.6055744, 3.49332), ((2, 3), 2, 0.001369): (4.64176, 2.6863122, 2.6694452, 4.62296),
    ((2, 3, 5), 1, 0.01475): (2.29929, 0.74604970, 0.56557107, 2.12670), ((2, 3, 5), 1, 0.004918): (3.37214, 1.6258251, 1.5647946, 3.31460),
    ((2, 3, 5), 1, 0.001639): (4.46246, 2.6509770, 2.6305545, 4.44328)}
def schmidt(v, pts, S, A):
    worst = 0
    for q in range(len(S)):
        M = mp.matrix(A + 1, (A + 1) ** (len(S) - 1))
        others = [pt[:q] + pt[q + 1:] for pt in pts]
        olist = sorted(set(others)); oi = {o: i for i, o in enumerate(olist)}
        for vi, pt in zip(v, pts): M[pt[q], oi[pt[:q] + pt[q + 1:]]] = vi
        sv = mp.svd_r(M, compute_uv=False)
        worst = max(worst, 1 - max(sv) ** 2)
    return worst
results = {}
for (S, A, dl), ref in A2rows.items():
    pts, G, parts, d = gram(S, A, mp.mpf(dl))
    E, V = eig(G)
    Gn = G.copy(); GnoP = G.copy()
    for (i, j), (po, ar, pr, mixed) in parts.items():
        if mixed: Gn[i, j] = 0
        GnoP[i, j] = po - ar
    lam_n = eig(Gn)[0][0]; lam_noP = eig(GnoP)[0][0]
    mixed_prime = max([abs(pr) for (po, ar, pr, mixed) in parts.values() if mixed] + [0])
    ok = all(abs(x - y) < 1e-5 * max(1, abs(y)) for x, y in zip((d, E[0], lam_n, lam_noP), ref))   # lane prints 6-8 significant digits
    check(ok and mixed_prime == 0 and E[0] > 0 and E[1] - E[0] > 1e-3,
          f'S={S} A={A} delta={dl}: d={mp.nstr(d,7)} lam(G)={mp.nstr(E[0],9)} lam(nomix)={mp.nstr(lam_n,9)} lam(noP)={mp.nstr(lam_noP,7)} (lane A2 {ref}); PD, simple; mixed prime terms {mixed_prime}')
    results[(S, A, dl)] = (pts, G, parts, E, V, lam_n)
# gap_mix linear in delta, Schmidt defect ~ delta^2
for S, A in (((2, 3), 1), ((2, 3), 2), ((2, 3, 5), 1)):
    ds = sorted([k[2] for k in results if k[0] == S and k[1] == A], reverse=True)
    gaps = [(results[(S, A, x)][5] - results[(S, A, x)][3][0]) for x in ds]
    sch = [schmidt(results[(S, A, x)][4][0], results[(S, A, x)][0], S, A) for x in ds]
    ratio = [g / x for g, x in zip(gaps, ds)]
    sl = [mp.log(sch[i] / sch[i + 1]) / mp.log(ds[i] / ds[i + 1]) for i in range(2)]
    check(all(g < 0 for g in gaps) and abs(ratio[-1] - ratio[-2]) < 0.05 * abs(ratio[-1]) and all(1.9 < s < 2.45 for s in sl),
          f'S={S} A={A}: mixed entries raise lambda_min: gap_mix/delta = {[mp.nstr(r,4) for r in ratio]} (converging: linear in delta); Schmidt defect {[mp.nstr(s,3) for s in sch]}, log-log slopes {[mp.nstr(s,3) for s in sl]}')
# pole vs arch split of the mixed entries at 0.9 delta_max, first order along v_min
for S, A, dl in (((2, 3), 1, 0.06936), ((2, 3), 2, 0.01232), ((2, 3, 5), 1, 0.01475)):
    pts, G, parts, E, V, _ = results[(S, A, dl)]
    v = V[0]
    fp = sum(v[i] * v[j] * po for (i, j), (po, ar, pr, mx) in parts.items() if mx)
    fa = sum(v[i] * v[j] * (-ar) for (i, j), (po, ar, pr, mx) in parts.items() if mx)
    line = f'S={S} A={A} delta={dl}: first-order mixed pole part {mp.nstr(fp,4)}, arch part {mp.nstr(fa,4)}, ratio {mp.nstr(-fp/fa,3)}'
    if (S, A) == ((2, 3), 1):
        Gp = G.copy(); Ga = G.copy()
        for (i, j), (po, ar, pr, mx) in parts.items():
            if mx: Gp[i, j] = -ar; Ga[i, j] = po
        lp, la = eig(Gp)[0][0], eig(Ga)[0][0]
        line += f'; lam with mixed pole removed {mp.nstr(lp,4)}, with mixed arch removed {mp.nstr(la,4)}'
        check(abs(lp + 0.0396) < 5e-4 and abs(la - 0.3105) < 5e-4, 'lane A2: removing the mixed pole part makes {2,3} A=1 indefinite (-0.0396); removing the mixed arch part gives 0.3105')
    check(fp > 0 and fa < 0, line)
# eigenvector movement {2} -> {2,3} at common delta, A = 1: slope ~ 2
dc = trunc4(0.9 * float(DM[((2, 3, 5), 1)]))
ov = []
for dl in (dc, dc / 10, dc / 100):
    _, G2, _, _ = gram((2,), 1, mp.mpf(dl)); v2 = eig(G2)[1][0]
    pts, G23, _, _ = gram((2, 3), 1, mp.mpf(dl)); v23 = eig(G23)[1][0]
    sub = [v23[i] for i, pt in enumerate(pts) if pt[1] == 0]
    nrm = mp.sqrt(sum(x * x for x in sub))
    ov.append(1 - abs(sum(a * b for a, b in zip(sub, v2))) / nrm)
sl = mp.log(ov[0] / ov[2]) / mp.log(100)
check(1.9 < sl < 2.15 and abs(ov[0] - 4.6e-5) < 0.2e-5, f'{{2}} -> {{2,3}}, A = 1, delta = {dc}, /10, /100: 1 - overlap = {[mp.nstr(x,3) for x in ov]} (lane A2: 4.6e-5, 4.2e-7, 4.1e-9); slope {mp.nstr(sl,3)}')
print(f'# checks: {NCHK[0]} run, {NCHK[1]} failed')
