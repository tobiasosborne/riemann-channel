#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane L (claude:opus, 2026-09-26): L4 recomputed independently.
Data: zst (a_n, b_n) via scratch_rtp2_lattice_common (C printer on libzst.a); own atoms, own blocks, mpmath eigsy
(not FLINT QR), own LP solve.  For each case: (1) H0 + T(w*) equals zst's true form; (2) eps; (3) the eigenvector-LP box
(dual form min lambda^T y, G^T y = -+e_k, y >= 0; Bland simplex at high precision) and an independent optimality check
(the primal vertex obtained from the dual support is feasible for every eigenvector cut and has zero duality gap);
(4) at x = 13, N = 20: the FULL SDP box (all other weights free) by a primal barrier method in whitened coordinates:
the central point is an inner (feasible) point, and Z = mu M^{-1} is a PSD dual certificate giving an outer bound;
(5) whether the LP endpoint is SDP-feasible; (6) the L2 positive-spanning bound 2 lambda_r / eta.  No zeros used.
Usage: python3 scratch_rtp2_lattice_box.py [x N [sdp]]  (default: 13 20 sdp)."""
import sys, os, time, multiprocessing as mpc
import numpy as np
from scipy.optimize import linprog
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scratch_rtp2_lattice_common as C

NCHK = [0, 0]
def check(c, msg):
    NCHK[0] += 1; NCHK[1] += (not c); print(('PASS ' if c else 'FAIL ') + msg, flush=True)

X = int(sys.argv[1]) if len(sys.argv) > 1 else 13
N = int(sys.argv[2]) if len(sys.argv) > 2 else 20
DO_SDP = (len(sys.argv) <= 1) or (len(sys.argv) > 3 and sys.argv[3] == 'sdp')
SDP_NS = [int(v) for v in sys.argv[4].split(',')] if len(sys.argv) > 4 else None   # restrict the SDP box to these n
DPS = 160 if N <= 40 else 250
mp.mp.dps = DPS
H0, T, W, HT, NS, RAD = C.setup(X, N)
m = len(NS)
Hs = C.combine(H0, T, W)
diff = max(mp.mnorm(Hs[0] - HT[0], 1), mp.mnorm(Hs[1] - HT[1], 1))
check(diff < mp.mpf(10) ** -(min(DPS, 218) - 12), f'x={X} N={N}: H0 + sum_k w*_k T_k equals zst true form, diff {mp.nstr(diff, 3)}; zst radius {RAD:.1e}')

# eigen-decomposition of the true form (both blocks)
lam, vec = [], []   # vec entries: (parity, column vector)
for p in (0, 1):
    ev, V = mp.eigsy(Hs[p])
    for i in range(Hs[p].rows):
        lam.append(ev[i]); vec.append((p, V[:, i]))
order = sorted(range(len(lam)), key=lambda i: lam[i])
lam = [lam[i] for i in order]; vec = [vec[i] for i in order]
eps = lam[0]
print(f'SPECTRUM eps={mp.nstr(eps, 10)} lambda_m={mp.nstr(lam[m-1], 10)} lambda_m+1={mp.nstr(lam[m], 10)} (#<1e-6: {sum(1 for l in lam if l < 1e-6)})')
check(eps > 0, 'true finite form positive definite (mpmath eigsy)')

def quad(M, v):
    return (v.T * M * v)[0]
G = [[quad(T[k][p], v) for k in range(m)] for (p, v) in vec]
R = len(G)

# ---------- LP: Bland two-phase simplex on the dual (review's rtp1 routine, re-typed) ----------
def simplex_min(c, A, b, tol):
    mrow, ncol = len(A), len(A[0])
    Tb = [list(A[i]) + [mp.mpf(1) if j == i else mp.mpf(0) for j in range(mrow)] + [b[i]] for i in range(mrow)]
    basis = [ncol + i for i in range(mrow)]
    def pivot(r, s):
        pv = Tb[r][s]; Tb[r] = [x / pv for x in Tb[r]]
        for i in range(mrow):
            if i != r and Tb[i][s] != 0:
                f = Tb[i][s]; Tb[i] = [x - f * y for x, y in zip(Tb[i], Tb[r])]
        basis[r] = s
    def solve(cost, allowed):
        for _ in range(20000):
            cb = [cost[j] for j in basis]
            red = [cost[s] - mp.fsum(cb[i] * Tb[i][s] for i in range(mrow)) for s in range(len(cost))]
            ent = next((s for s in range(len(cost)) if s in allowed and s not in basis and red[s] < -tol), None)
            if ent is None: return True
            rows = [(Tb[i][-1] / Tb[i][ent], basis[i], i) for i in range(mrow) if Tb[i][ent] > tol]
            if not rows: return False
            pivot(min(rows)[2], ent)
        raise RuntimeError('iteration limit')
    solve([mp.mpf(0)] * ncol + [mp.mpf(1)] * mrow, set(range(ncol + mrow)))
    for i in range(mrow):
        if basis[i] >= ncol:
            s = next((s for s in range(ncol) if abs(Tb[i][s]) > tol and s not in basis), None)
            if s is not None: pivot(i, s)
    solve(list(c) + [mp.mpf(0)] * mrow, set(range(ncol)))
    y = [mp.mpf(0)] * ncol
    for i in range(mrow):
        if basis[i] < ncol: y[basis[i]] = Tb[i][-1]
    return y, [bb for bb in basis if bb < ncol]

tol = mp.mpf(10) ** (-(DPS - 40))
GT = [[G[i][k] for i in range(R)] for k in range(m)]
def lp_endpoint(k, sgn):
    """sgn=+1: max delta_k (dual G^T y = -e_k); sgn=-1: max -delta_k (G^T y = +e_k). Returns bound, y, vertex delta, checks"""
    rhs = [mp.mpf(0)] * m; rhs[k] = mp.mpf(-sgn)
    A = [list(r) for r in GT]; b = list(rhs)
    for i in range(m):
        if b[i] < 0: A[i] = [-x for x in A[i]]; b[i] = -b[i]
    y, supp = simplex_min(lam, A, b, tol)
    val = mp.fsum(l * yy for l, yy in zip(lam, y))
    res = max(abs(mp.fsum(GT[i][j] * y[j] for j in range(R)) - rhs[i]) for i in range(m))
    # primal vertex: g_i . d = -lambda_i on the support (complementary slackness), m x m solve
    sup = [i for i in range(R) if y[i] > 0]
    if len(sup) < m:   # degenerate: complete with other basic columns
        sup = sorted(set(sup) | set(supp))[:m]
    Mx = mp.matrix([G[i] for i in sup]); rv = mp.matrix([-lam[i] for i in sup])
    d = mp.lu_solve(Mx, rv); d = [d[j] for j in range(m)]
    slack = min(lam[i] + mp.fsum(G[i][j] * d[j] for j in range(m)) for i in range(R))
    gap = abs(sgn * d[k] - val)
    return val, y, d, min(y), res, slack, gap

def _lp_job(a):
    mp.mp.dps = DPS
    return a, lp_endpoint(*a)
def run_lp():
    out = {}
    with mpc.get_context('fork').Pool(min(2 * m, 48)) as pool:
        rr = dict(pool.map(_lp_job, [(k, s) for k in range(m) for s in (+1, -1)]))
    for k in range(m):
        up = rr[(k, +1)]; lo = rr[(k, -1)]
        out[k] = (lo, up)
        ok = all(e[3] >= 0 and e[4] < mp.mpf(10) ** (-DPS + 40) * (1 + max(e[1])) and e[5] > -abs(e[0]) * mp.mpf(10) ** -40 and e[6] < abs(e[0]) * mp.mpf(10) ** -40 for e in (lo, up))
        check(ok, f'LP n={NS[k]}: max dual multiplier {mp.nstr(max(max(lo[1]), max(up[1])), 2)}; width {mp.nstr(lo[0] + up[0], 10)} = [{mp.nstr(-lo[0], 6)}, {mp.nstr(up[0], 6)}]; dual y>=0, residual {mp.nstr(max(lo[4], up[4]), 2)}, primal vertex min slack {mp.nstr(min(lo[5], up[5]), 2)}, gap {mp.nstr(max(lo[6], up[6]), 2)}')
    return out
t0 = time.time(); LP = run_lp(); print(f'# LP time {time.time()-t0:.1f}s', flush=True)
LANE = {(13, 20): {2: '2.9844301186e-25', 3: '1.76226118295e-23', 6: '1.36252636287e-17', 11: '2.6659994004e-7', 12: '0.000125286570504'},
        (13, 56): {2: '1.192655524e-38', 6: '4.251260e-30', 12: '2.328012649e-10'},
        (13, 60): {2: '1.000472324e-38', 6: '3.579417e-30', 12: '2.121317700e-10'},
        (25, 60): {2: '8.231774550e-61', 6: '9.668708e-53', 12: '1.313248e-39', 24: '4.364656164e-8'},
        (25, 134): {2: '2.000607387e-80', 6: '3.364439e-72', 12: '6.450034e-58', 24: '2.225924060e-14'},
        (17, 60): {2: '6.079486546e-50', 6: '1.293759e-41', 12: '3.545446e-26', 16: '1.459510808e-10'},
        (17, 83): {2: '1.646086672e-52', 6: '3.759632e-44', 12: '2.171886e-28', 16: '8.288468325e-12'}}.get((X, N), {})
for n, s in LANE.items():
    k = NS.index(n); wd = LP[k][0][0] + LP[k][1][0]; digs = len(s.replace('.', '').split('e')[0].lstrip('0')) - 1
    check(abs(wd / mp.mpf(s) - 1) < 10 ** -(digs - 1), f'lane LP width at n={n}: lane {s}, reviewer {mp.nstr(wd, 12)}')
ws = [LP[k][0][0] + LP[k][1][0] for k in range(m)]
check(all(ws[i] < ws[i + 1] for i in range(m - 1)), f'LP widths strictly increasing in n (lane claim): {[mp.nstr(v, 3) for v in ws]}')

# needle structure: how many distinct LP vertices attain the 2m box endpoints?
verts = []
for k in range(m):
    for s_ in (0, 1):
        d = LP[k][s_][2]
        if not any(max(abs(d[l] - v[l]) / (abs(v[l]) + mp.mpf(10) ** -300) for l in range(m)) < mp.mpf(10) ** -20 for v in verts):
            verts.append(d)
alt = all(mp.sign(verts[0][l]) == -mp.sign(verts[0][l + 1]) for l in range(m - 1))
print(f'NEEDLE2 the {2 * m} LP box endpoints are attained at {len(verts)} distinct vertices; vertex signs alternate in n: {alt}; '
      f'successive component ratios |d_(n+1)/d_n| of the first: {[mp.nstr(abs(verts[0][l + 1] / verts[0][l]), 3) for l in range(m - 1)]}')
check(len(verts) == 2, f'LP box of all {m} coordinates is the bounding box of exactly two vertices (a needle)')
# is the LP endpoint SDP-feasible?
def lmin_at(d):
    Hd = C.combine(Hs, T, d)
    return min(mp.eigsy(Hd[0], eigvals_only=True)[0], mp.eigsy(Hd[1], eigvals_only=True)[0])
for n in [n for n in (2, 6, 12, X - 1) if n in NS]:
    k = NS.index(n); d = LP[k][1][2]
    print(f'LPVERTEX n={n} delta = {[mp.nstr(v, 3) for v in d]}')
    print(f'LPVERTEX n={n}: lambda_min(H(w* + delta_LP,upper)) = {mp.nstr(lmin_at(list(d)), 4)}  (negative => LP endpoint is not in the spectrahedron)')

# L2 conditioning bound with the r = m+1 smallest directions (exact null vector h of G_r^T, mpmath)
r = m + 1
Gr = mp.matrix([G[i] for i in range(r)])            # r x m
# null vector of Gr^T (m x r): solve with h_r = 1
Asub = mp.matrix(m, m); rhs = mp.matrix(m, 1)
for k in range(m):
    for i in range(m): Asub[k, i] = Gr[i, k]
    rhs[k] = -Gr[r - 1, k]
hh = mp.lu_solve(Asub, rhs); h = [hh[i] for i in range(m)] + [mp.mpf(1)]
sgnh = set(mp.sign(v) for v in h)
print(f'POSSPAN r=m+1={r}: null vector of G_r^T has entry signs {sorted(int(v) for v in sgnh)} -> the {r} smallest eigendirections '
      f'{"DO" if len(sgnh) == 1 else "do NOT"} positively span R^m')
if len(sgnh) == 1:
    h = [abs(v) for v in h]; hs = mp.fsum(h); h = [v / hs for v in h]
    for n in [n for n in (2, 6, 12) if n in NS]:
        k = NS.index(n)
        # min-norm p with G_r^T p = e_k
        GT_r = mp.matrix(m, r)
        for kk in range(m):
            for i in range(r): GT_r[kk, i] = Gr[i, kk]
        ek = mp.matrix(m, 1); ek[k] = 1
        pk = GT_r.T * mp.lu_solve(GT_r * GT_r.T, ek)
        ak = max(abs(pk[i]) / h[i] for i in range(r))
        bnd = 2 * ak * mp.fsum(h[i] * lam[i] for i in range(r))
        wd = LP[k][0][0] + LP[k][1][0]
        print(f'L2BOUND n={n}: 2 a_k sum h_i lambda_i = {mp.nstr(bnd, 4)}  vs LP width (all cuts) {mp.nstr(wd, 4)}  ratio {mp.nstr(bnd / wd, 3)};  2 a_k lambda_r = {mp.nstr(2 * ak * lam[r - 1], 3)}')
# support ranks of the optimal duals
rused = max(max(i for i in range(R) if LP[k][s_][1][i] > 0) + 1 for k in range(m) for s_ in (0, 1))
print(f'RUSED largest spectral rank in any optimal LP dual support: {rused}')
# needle structure: LP corner vertices and ray sections from truth along them (inner bounds for every coordinate)
def ray_tmax(d):
    """largest t >= 0 with H* + t T(d) >= 0"""
    tm = mp.inf
    for p in (0, 1):
        Lc = mp.cholesky(Hs[p]); Li = mp.inverse(Lc)
        Td = sum((d[l] * T[l][p] for l in range(m)), mp.zeros(Hs[p].rows))
        K = Li * Td * Li.T; mu_ = mp.eigsy((K + K.T) / 2, eigvals_only=True)[0]
        if mu_ < 0: tm = min(tm, -1 / mu_)
    return tm
k2 = NS.index(2)
dplus = [LP[k2][1][2][l] for l in range(m)]; dminus = [LP[k2][0][2][l] for l in range(m)]
same = max(abs(LP[k][1 if (NS[k] % 2 == 0) == True else 0][2][l] - dplus[l]) / (abs(dplus[l]) + 1e-300) for k in range(m) for l in range(m)) if X == 13 else None
tp, tn = ray_tmax(dplus), ray_tmax(dminus)
print(f'NEEDLE corner vertices: t_max along delta_LP^+ = {mp.nstr(tp, 6)}, along delta_LP^- = {mp.nstr(tn, 6)}')
INNER = {}
for k in range(m):
    pts = [mp.mpf(0), tp * dplus[k], tn * dminus[k]]
    INNER[k] = max(pts) - min(pts)
    wd = LP[k][0][0] + LP[k][1][0]
    print(f'RAYBOX n={NS[k]:2d}: inner (two ray sections) {mp.nstr(INNER[k], 6)}  LP outer {mp.nstr(wd, 6)}  LP/inner {mp.nstr(wd / INNER[k], 4)}')
# ---------- full SDP box at this (x, N) by a barrier method ----------
def whiten():
    """A_k = Lambda^{-1/2} V^T T_k V Lambda^{-1/2}, block-diagonal over parity"""
    out = []
    for p in (0, 1):
        idx = [i for i in range(R) if vec[i][0] == p]
        V = mp.matrix(Hs[p].rows, len(idx))
        for c, i in enumerate(idx):
            for r_ in range(Hs[p].rows): V[r_, c] = vec[i][1][r_] / mp.sqrt(lam[i])
        out.append([V.T * T[k][p] * V for k in range(m)])
    return out
def sdp_endpoint(args):
    k, sgn, scale = args
    mp.mp.dps = DPS
    A = WH
    D = [mp.mpf(s) for s in scale]          # u-coordinates: delta_l = D_l u_l
    B = [[D[l] * A[p][l] for l in range(m)] for p in (0, 1)]
    ntot = sum(A[p][0].rows for p in (0, 1))
    def Mof(u):
        return [mp.eye(A[p][0].rows) + sum((u[l] * B[p][l] for l in range(m)), mp.zeros(A[p][0].rows)) for p in (0, 1)]
    def logdet(Ms):
        s = mp.mpf(0)
        for M in Ms:
            try: Lc = mp.cholesky(M)
            except Exception: return None
            for i in range(M.rows):
                if not (Lc[i, i] > 0): return None
                s += 2 * mp.log(Lc[i, i])
        return s
    u = [mp.mpf(0)] * m; mu = mp.mpf(1)
    hist = []
    while True:
        for it in range(200):
            Ms = Mof(u)
            Pl = [[mp.inverse(Ms[p]) * B[p][l] for l in range(m)] for p in (0, 1)]
            g = [sgn * (1 if l == k else 0) + mu * sum(sum(Pl[p][l][i, i] for i in range(Ms[p].rows)) for p in (0, 1)) for l in range(m)]
            Hm = mp.matrix(m, m)
            for a in range(m):
                for b_ in range(a, m):
                    v = sum(mp.fsum(Pl[p][a][i, j] * Pl[p][b_][j, i] for i in range(Ms[p].rows) for j in range(Ms[p].rows)) for p in (0, 1))
                    Hm[a, b_] = Hm[b_, a] = -mu * v
            step = mp.lu_solve(-Hm, mp.matrix(g))       # ascent direction
            dec = mp.fsum(g[l] * step[l] for l in range(m))
            f0 = sgn * u[k] + mu * logdet(Ms)
            t = mp.mpf(1)
            while True:
                un = [u[l] + t * step[l] for l in range(m)]
                ld = logdet(Mof(un))
                if ld is not None and sgn * un[k] + mu * ld >= f0 + t * dec / 4: break
                t /= 2
                if t < mp.mpf(10) ** -60: break
            u = un
            if dec < mp.mpf(10) ** (-DPS + 60) * (1 + abs(f0)): break
        Ms = Mof(u)
        Z = [mu * mp.inverse(M) for M in Ms]
        trZ = sum(sum(Zp[i, i] for i in range(Zp.rows)) for Zp in Z)
        resid = [sum(mp.fsum(Z[p][i, j] * B[p][l][j, i] for i in range(Z[p].rows) for j in range(Z[p].rows)) for p in (0, 1)) + sgn * (1 if l == k else 0) for l in range(m)]
        inner = sgn * u[k]
        outer = trZ + mp.fsum(abs(r_) for r_ in resid)   # |u'_l| <= 1 on the LP box (scale = LP half-extent max)
        hist.append((mu, inner, outer))
        if outer - inner < mp.mpf(10) ** -8 * abs(inner) or mu < mp.mpf(10) ** -70: break
        mu /= 10
    lmin = min(mp.eigsy(M, eigvals_only=True)[0] for M in Ms)
    # direct check in the original (unwhitened) coordinates: H(w* + delta_inner) positive definite
    dlt = [D[l] * u[l] for l in range(m)]
    Hd = C.combine(Hs, T, dlt)
    lmin = min(lmin, min(mp.eigsy(Hd[p], eigvals_only=True)[0] for p in (0, 1)) / eps)
    return k, sgn, inner * D[k], outer * D[k], lmin, len(hist)

if DO_SDP:
    WH = whiten()
    # scale: u = delta / D, D_l = max(|LP lower_l|, |LP upper_l|), so the LP box lies in |u_l| <= 1
    scale = [mp.nstr(max(LP[l][0][0], LP[l][1][0]), 30) for l in range(m)]
    jobs = [(k, s, scale) for k in range(m) for s in (+1, -1) if SDP_NS is None or NS[k] in SDP_NS]
    t0 = time.time()
    with mpc.get_context('fork').Pool(min(len(jobs), 44)) as pool:
        res = pool.map(sdp_endpoint, jobs)
    print(f'# SDP time {time.time()-t0:.1f}s', flush=True)
    E = {}
    for k, s, inn, out, lmin, nst in res:
        E[(k, s)] = (inn, out)
        check(lmin > 0 and inn <= out, f'SDP endpoint n={NS[k]} sign={s:+d}: inner {mp.nstr(inn, 8)} <= exact <= outer {mp.nstr(out, 8)} (central point lambda_min(M) {mp.nstr(lmin, 3)} > 0; {nst} barrier stages)')
    SEC = {2: '3.55656916034e-34', 3: '7.41823587029e-33', 6: '3.22341889452e-27', 11: '2.89088014777e-13', 12: '1.40761371112e-8'} if (X, N) == (13, 20) else {}
    print('SDPBOX  n | full SDP width (inner..outer) | eigenvector LP width | LP/SDP | lane 2-coord section (inner bound)')
    for k in [k for k in range(m) if (k, 1) in E]:
        wi = E[(k, 1)][0] + E[(k, -1)][0]; wo = E[(k, 1)][1] + E[(k, -1)][1]; wl = LP[k][0][0] + LP[k][1][0]
        sec = SEC.get(NS[k])
        print(f'SDPBOX {NS[k]:2d} | {mp.nstr(wi, 8)} .. {mp.nstr(wo, 8)} | {mp.nstr(wl, 8)} | {mp.nstr(wl / wo, 4)} | {sec} | ray-section inner {mp.nstr(INNER[k], 6)}')
        check(wo <= wl * (1 + mp.mpf(10) ** -20) and (sec is None or mp.mpf(sec) <= wo * (1 + mp.mpf(10) ** -6)),
              f'n={NS[k]}: section (lane) <= SDP width <= LP width')
print(f'# checks: {NCHK[0]} run, {NCHK[1]} failed')
