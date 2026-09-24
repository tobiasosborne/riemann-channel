#!/usr/bin/env python3
"""REFUTE lane R, RTP-1 (claude:opus, 2026-09-24).  Claim C10 (lane B2.1(b)-(d)) recomputed independently at
x = 13 (L = log 13, prime powers <= 13), N = 20 (and 60): reviewer's (a,b) (scratch_rtp1_ab.py) split into pole,
arch and prime parts; min-HS-norm admissible prime datum by Dykstra alternating projections (not a barrier method);
PNT mean predictor; lattice-weight box: INNER bound = exact coordinate-axis sections of the spectrahedron
(generalised eigenvalues at 100 digits), OUTER bound = LP over the eigenvector cuts solved by the reviewer's own
exact-arithmetic-style simplex (Bland) at 100 digits.  Deterministic."""
import sys, os, math
import numpy as np
import mpmath as mp
from flint import arb, ctx
sys.path.insert(0, os.path.dirname(__file__))
import scratch_rtp1_ab as AB
NCHK = [0, 0]
def check(c, m):
    NCHK[0] += 1; NCHK[1] += (not c); print(('PASS ' if c else 'FAIL ') + m, flush=True)
ctx.prec = 400
L = arb(13).log(); Lf = math.log(13)
PPL = AB.von_mangoldt_table(13)

def blocks_from(a, b, M, lib=np):
    """even (M+1) and odd (M) blocks of the Loewner form of (a, b); a, b sequences of floats or mpf"""
    if lib is np:
        E = np.zeros((M + 1, M + 1)); O = np.zeros((M, M)); s2 = math.sqrt(2)
    else:
        E = mp.matrix(M + 1, M + 1); O = mp.matrix(M, M); s2 = mp.sqrt(2)
    E[0, 0] = a[0]
    for j in range(1, M + 1):
        E[0, j] = s2 * b[j] / j; E[j, 0] = E[0, j]
        E[j, j] = a[j] + b[j] / j; O[j - 1, j - 1] = a[j] - b[j] / j
    for i in range(1, M + 1):
        for j in range(1, M + 1):
            if i != j:
                t = (b[i] - b[j]) / (i - j); u = (b[i] + b[j]) / (i + j)
                E[i, j] = t + u; O[i - 1, j - 1] = t - u
    return E, O

def setup(N):
    P = AB.ab_parts(L, N, PPL, 400)
    f = lambda xs: [float(t.mid()) for t in xs]
    a0 = [x + y for x, y in zip(f(P['pole'][0]), f(P['arch'][0]))]; b0 = [x + y for x, y in zip(f(P['pole'][1]), f(P['arch'][1]))]
    up, vp = f(P['prime'][0]), f(P['prime'][1])
    return P, a0, b0, up, vp

def basis(N):
    """list of (E, O) for the 2N+1 coordinates z = (u_0..u_N, v_1..v_N)"""
    out = []
    for k in range(N + 1):
        a = [0.0] * (N + 1); a[k] = 1.0; out.append(blocks_from(a, [0.0] * (N + 1), N))
    for k in range(1, N + 1):
        b = [0.0] * (N + 1); b[k] = 1.0; out.append(blocks_from([0.0] * (N + 1), b, N))
    return out

def run(N, verbose=True):
    P, a0, b0, up, vp = setup(N)
    H0E, H0O = blocks_from(a0, b0, N)
    eE, eO = np.linalg.eigvalsh(H0E), np.linalg.eigvalsh(H0O)
    Bs = basis(N)
    vecs = np.array([np.concatenate([E.ravel(), O.ravel()]) for E, O in Bs]).T   # HS coordinates
    Q = vecs.T @ vecs
    ztrue = np.array(up + vp[1:])
    Tz = lambda z: (sum(z[i] * Bs[i][0] for i in range(len(z))), sum(z[i] * Bs[i][1] for i in range(len(z))))
    hs = lambda z: math.sqrt(z @ Q @ z)
    # Dykstra: project 0 onto {X in range(T)} cap {X + H0 >= 0}
    nE = (N + 1) ** 2
    def projC2(X):
        XE = X[:nE].reshape(N + 1, N + 1) + H0E; XO = X[nE:].reshape(N, N) + H0O
        w, V = np.linalg.eigh((XE + XE.T) / 2); XE = (V * np.maximum(w, 0)) @ V.T - H0E
        w, V = np.linalg.eigh((XO + XO.T) / 2); XO = (V * np.maximum(w, 0)) @ V.T - H0O
        return np.concatenate([XE.ravel(), XO.ravel()])
    Qi = np.linalg.inv(Q)
    projC1 = lambda X: vecs @ (Qi @ (vecs.T @ X))
    x = np.zeros(vecs.shape[0]); p = np.zeros_like(x); q = np.zeros_like(x)
    for it in range(60000):
        y = projC1(x + p); p = x + p - y
        xn = projC2(y + q); q = y + q - xn
        if it % 1000 == 999 and np.linalg.norm(xn - x) < 1e-13: x = xn; break
        x = xn
    zmin = Qi @ (vecs.T @ projC1(x))
    TE, TO = Tz(zmin)
    lmin_min = min(np.linalg.eigvalsh(H0E + TE)[0], np.linalg.eigvalsh(H0O + TO)[0])
    capt = (zmin @ Q @ ztrue) / (ztrue @ Q @ ztrue); dist = hs(zmin - ztrue) / hs(ztrue)
    # PNT mean: -e^{y/2} dy on [0, L]
    # PNT mean -e^{y/2} dy on [0, L], closed form: int_0^L (1 - y/L) e^{sig y} dy = -1/sig + (e^{sig L} - 1)/(sig^2 L)
    def Jc(sig): return -1 / sig + (np.exp(sig * Lf) - 1) / (sig * sig * Lf)
    uP = [float(-2 * Jc(0.5 + 2j * math.pi * n / Lf).real) for n in range(N + 1)]
    vP = [float(((np.exp((0.5 + 2j * math.pi * n / Lf) * Lf) - 1) / (0.5 + 2j * math.pi * n / Lf)).imag / math.pi) for n in range(1, N + 1)]
    if N == 20:
        mp.mp.dps = 30
        for n in (0, 1, 3):
            qa = -2 * mp.quad(lambda y: (1 - y / Lf) * mp.cos(2 * mp.pi * n * y / Lf) * mp.e ** (y / 2), [0, Lf])
            qb = mp.quad(lambda y: mp.sin(2 * mp.pi * n * y / Lf) * mp.e ** (y / 2), [0, Lf]) / mp.pi
            assert abs(qa - uP[n]) < 1e-12 and (n == 0 or abs(qb - vP[n - 1]) < 1e-12)
    zP = np.array(uP + vP)
    PE, PO = Tz(zP)
    lP = min(np.linalg.eigvalsh(H0E + PE)[0], np.linalg.eigvalsh(H0O + PO)[0])
    captP = (zP @ Q @ ztrue) / (ztrue @ Q @ ztrue)
    return dict(eE=eE, eO=eO, hs_true=hs(ztrue), hs_min=hs(zmin), capt=capt, dist=dist, lmin_min=lmin_min, it=it, lP=lP, captP=captP, distP=hs(zP - ztrue) / hs(ztrue))

R = run(20)
print(f"N=20: H0 even eigenvalues < 0: {[round(x,4) for x in R['eE'] if x < 0]}; odd: {[round(x,4) for x in R['eO'] if x < 0]}")
check(abs(min(R['eO'].min(), R['eE'].min()) + 1.961) < 2e-3, f"zero prime data inadmissible: lambda_min(H0) = {min(R['eO'].min(), R['eE'].min()):.4f} (odd block; lane -1.96); even block min {R['eE'].min():.4f}")
check(abs(R['hs_true'] - 8.2133) < 1e-3, f"||z_true||_HS = {R['hs_true']:.4f} (lane 8.2133)")
check(abs(R['hs_min'] - 2.3601) < 2e-3 and abs(R['capt'] - 0.083) < 2e-3 and abs(R['dist'] - 0.957) < 2e-3 and R['lmin_min'] > -1e-7,
      f"min-HS-norm admissible prime datum (Dykstra, {R['it']+1} sweeps): norm {R['hs_min']:.4f} (lane 2.3601), captures {100*R['capt']:.2f}% (lane 8.3%), rel. dist {R['dist']:.3f} (lane 0.957), lambda_min {R['lmin_min']:.1e}")
check(abs(R['lP'] + 1.226) < 2e-3 and abs(R['captP'] - 0.224) < 2e-3, f"PNT mean: lambda_min(H0 + T_PNT) = {R['lP']:.4f} (lane -1.226), captures {100*R['captP']:.1f}% (lane 22%), rel. dist {R['distP']:.3f}")
# unboundedness / no max-det: H0 + c I is admissible for c >= 1.961 and log det -> infinity
P, a0, b0, up, vp = setup(20)
H0E, H0O = blocks_from(a0, b0, 20)
ld = [np.linalg.slogdet(H0E + c * np.eye(21))[1] + np.linalg.slogdet(H0O + c * np.eye(20))[1] for c in (10, 100, 1000)]
check(all(ld[i] < ld[i + 1] for i in range(2)) and abs(ld[0] - 98.9) < 0.1, f'c I (a_n = c, b_n = 0) is a Loewner-gamma form: log det(H0 + cI) = {[round(x,1) for x in ld]} -> unbounded, sup log det = +inf, no max-det element')
R60 = run(60)
check(abs(R60['capt'] - 0.028) < 2e-3, f"N=60: min-norm element captures {100*R60['capt']:.2f}% (lane 2.8%), norm {R60['hs_min']:.4f}")
# ---------------- lattice weights: inner and outer boxes ----------------
mp.mp.dps = 100
N = 20
Pm = AB.ab_parts(L, N, PPL, 400)
g = lambda xs: [mp.mpf(t.mid().str(110, radius=False)) for t in xs]
a0m = [x + y for x, y in zip(g(Pm['pole'][0]), g(Pm['arch'][0]))]; b0m = [x + y for x, y in zip(g(Pm['pole'][1]), g(Pm['arch'][1]))]
ns = list(range(2, 13))
Lm = mp.log(13)
def Tn(n):
    a = [-2 * (1 - mp.log(n) / Lm) * mp.cos(2 * mp.pi * k * mp.log(n) / Lm) for k in range(N + 1)]
    b = [mp.sin(2 * mp.pi * k * mp.log(n) / Lm) / mp.pi for k in range(N + 1)]
    return blocks_from(a, b, N, lib=mp)
vm = {k: mp.log(p) / mp.sqrt(k) for k, p in PPL}
wtrue = [vm.get(n, mp.mpf(0)) for n in ns]
TT = [Tn(n) for n in ns]
H0E, H0O = blocks_from(a0m, b0m, N, lib=mp)
HE = H0E + sum((w * t[0] for w, t in zip(wtrue, TT)), mp.matrix(N + 1, N + 1))
HO = H0O + sum((w * t[1] for w, t in zip(wtrue, TT)), mp.matrix(N, N))
aT, bT = AB.ab_total(L, N, PPL, 400)
HEt, HOt = blocks_from(g(aT), g(bT), N, lib=mp)
check(mp.mnorm(HE - HEt, 1) < mp.mpf(10) ** -90 and mp.mnorm(HO - HOt, 1) < mp.mpf(10) ** -90, 'H(w_true) with 11 lattice weights = the true window form (13 has weight exactly 0)')
lamE, VE = mp.eigsy(HE); lamO, VO = mp.eigsy(HO)
lams = [lamE[i] for i in range(N + 1)] + [lamO[i] for i in range(N)]
check(min(lams) > 0 and abs(min(lams) - mp.mpf('1.566e-39')) < mp.mpf('0.01e-39'), f'lambda_min(H_true) = {mp.nstr(min(lams), 4)} (> 0; lane A1 1.57e-39); {sum(1 for l in lams if l < 1e-6)} eigenvalues below 1e-6')
# inner: exact axis sections {t : H_true + t T_n >= 0}
def section(Tb):
    out = []
    for H, T_ in ((HE, Tb[0]), (HO, Tb[1])):
        Lc = mp.cholesky(H); Li = mp.inverse(Lc)
        Mx = Li * T_ * Li.T
        mu = mp.eigsy((Mx + Mx.T) / 2, eigvals_only=True)
        out.append((max(mu), min(mu)))
    mx = max(o[0] for o in out); mn = min(o[1] for o in out)
    lo = -1 / mx if mx > 0 else -mp.inf; hi = -1 / mn if mn < 0 else mp.inf
    return lo, hi
lane_w = {2: 1.07e-7, 3: 7.71e-8, 4: 2.13e-12, 5: 4.02e-11, 6: 1.93e-10, 7: 6.87e-10, 8: 5.05e-10, 9: 5.24e-8, 10: 2.23e-6, 11: 1.05e-5, 12: 1.27e-3}
inner = {}
for n, T_ in zip(ns, TT):
    lo, hi = section(T_); inner[n] = (lo, hi)
# outer: LP  max/min dw_n  s.t.  lambda_i + g_i . dw >= 0  (g_in = v_i^T T_n v_i), via the dual  min lambda^T y, G^T y = -+ e_n, y >= 0
vecsE = [[VE[r, i] for r in range(N + 1)] for i in range(N + 1)]; vecsO = [[VO[r, i] for r in range(N)] for i in range(N)]
def quad(Mt, v): return mp.fsum(v[r] * mp.fsum(Mt[r, c] * v[c] for c in range(len(v))) for r in range(len(v)))
G = [[quad(T_[0], v) for T_ in TT] for v in vecsE] + [[quad(T_[1], v) for T_ in TT] for v in vecsO]
m_, k_ = len(G), len(ns)
def simplex_min(c, A, b):
    """min c^T y, A y = b (b >= 0), y >= 0; Bland's rule, two phases, mpmath.  returns (value, y)"""
    mrow, ncol = len(A), len(A[0])
    # phase 1 tableau with artificials
    T = [list(A[i]) + [mp.mpf(1) if j == i else mp.mpf(0) for j in range(mrow)] + [b[i]] for i in range(mrow)]
    basis = [ncol + i for i in range(mrow)]
    def pivot(r, s):
        pv = T[r][s]; T[r] = [x / pv for x in T[r]]
        for i in range(mrow):
            if i != r and T[i][s] != 0:
                f_ = T[i][s]; T[i] = [x - f_ * y for x, y in zip(T[i], T[r])]
        basis[r] = s
    def solve(cost, allowed):
        for _ in range(5000):
            cb = [cost[j] for j in basis]
            red = [cost[s] - mp.fsum(cb[i] * T[i][s] for i in range(mrow)) for s in range(len(cost))]
            ent = next((s for s in range(len(cost)) if s in allowed and s not in basis and red[s] < -mp.mpf(10) ** -80), None)
            if ent is None: return True
            rows = [(T[i][-1] / T[i][ent], basis[i], i) for i in range(mrow) if T[i][ent] > mp.mpf(10) ** -80]
            if not rows: return False
            r = min(rows)[2]
            pivot(r, ent)
        raise RuntimeError('simplex iteration limit')
    c1 = [mp.mpf(0)] * ncol + [mp.mpf(1)] * mrow
    solve(c1, set(range(ncol + mrow)))
    if mp.fsum(T[i][-1] for i in range(mrow) if basis[i] >= ncol) > mp.mpf(10) ** -60: return None, None
    for i in range(mrow):
        if basis[i] >= ncol:
            s = next((s for s in range(ncol) if abs(T[i][s]) > mp.mpf(10) ** -60 and s not in basis), None)
            if s is not None: pivot(i, s)
    c2 = list(c) + [mp.mpf(0)] * mrow
    ok = solve(c2, set(range(ncol)))
    y = [mp.mpf(0)] * ncol
    for i in range(mrow):
        if basis[i] < ncol: y[basis[i]] = T[i][-1]
    return mp.fsum(c[j] * y[j] for j in range(ncol)), y
At = [[G[i][n] for i in range(m_)] for n in range(k_)]   # G^T: k x m
outer = {}
for jn, n in enumerate(ns):
    res = []
    for sgn in (-1, 1):   # sgn = -1: upper bound on dw_n (G^T y = -e_n); +1: bound on -dw_n
        rhs = [mp.mpf(0)] * k_; rhs[jn] = mp.mpf(-sgn)
        A_ = [list(row) for row in At]; b_ = list(rhs)
        for i in range(k_):
            if b_[i] < 0: A_[i] = [-x for x in A_[i]]; b_[i] = -b_[i]
        val, y = simplex_min(lams, A_, b_)
        if y is not None:
            resid = max(abs(mp.fsum(At[i][j] * y[j] for j in range(m_)) - rhs[i]) for i in range(k_))
            assert min(y) >= 0 and resid < mp.mpf(10) ** -60
        res.append(val)
    outer[n] = (-res[1] if res[1] is not None else -mp.inf, res[0] if res[0] is not None else mp.inf)
print('   n : inner axis section [lo, hi] (exact)          | outer LP box [lo, hi] (dual-certified) | lane box width')
allok = True
for n in ns:
    lo_i, hi_i = inner[n]; lo_o, hi_o = outer[n]
    w_in, w_out = hi_i - lo_i, hi_o - lo_o
    ok = lo_o <= lo_i + mp.mpf(10) ** -50 and hi_i <= hi_o + mp.mpf(10) ** -50 and w_in <= lane_w[n] * 1.02
    allok &= ok
    print(f'   {n:2d}: [{mp.nstr(lo_i,3)}, {mp.nstr(hi_i,3)}] width {mp.nstr(w_in,3)} | [{mp.nstr(lo_o,3)}, {mp.nstr(hi_o,3)}] width {mp.nstr(w_out,3)} | {lane_w[n]:.3g}')
check(allok, 'lattice weights: inner (axis sections) within outer (LP box) for every n, and inner widths never exceed the lane widths')
check(all(outer[n][1] - outer[n][0] <= 1.02 * lane_w[n] for n in ns), 'outer LP box widths (reviewer simplex) <= lane widths for every n (the lane box is confirmed as an outer bound)')
print(f'# checks: {NCHK[0]} run, {NCHK[1]} failed')
