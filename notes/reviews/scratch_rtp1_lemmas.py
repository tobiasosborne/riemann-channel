#!/usr/bin/env python3
"""REFUTE lane R, RTP-1 (claude:opus, 2026-09-24).  Claims C1, C4, C8, C9: independent numerical and exact
checks of the lemmas and propositions (the proofs are in the review).  numpy (seeded), sympy, python-flint
fmpq_mat for exact ranks, and the reviewer's zeta (a,b) for the Loewner section.  Deterministic."""
import sys, os, math, itertools
import numpy as np
import sympy as sp
from flint import fmpq_mat, fmpq, arb, ctx
sys.path.insert(0, os.path.dirname(__file__))
import scratch_rtp1_ab as AB
rng = np.random.default_rng(20260924)
NCHK = [0, 0]
def check(c, m):
    NCHK[0] += 1; NCHK[1] += (not c); print(('PASS ' if c else 'FAIL ') + m, flush=True)

# ---------------- C1: ellipsoid lemma ----------------
print('## C1 (lemma A1.1 and its Loewner section A1.1\')')
for trial in range(5):
    n = 6
    X = rng.standard_normal((n, n)); G = X @ X.T + 0.1 * np.eye(n)
    c = rng.standard_normal(n); Gi = np.linalg.inv(G); q = c @ Gi @ c
    d = q * (1 + rng.uniform(0.01, 2))
    B = np.block([[G, c[:, None]], [c[None, :], np.array([[d]])]])
    ok1 = abs(np.linalg.det(B) - np.linalg.det(G) * (d - q)) < 1e-9 * abs(np.linalg.det(B))
    # PSD iff Schur >= 0 on the boundary family d = q (1 + t)
    ok2 = all((np.linalg.eigvalsh(np.block([[G, c[:, None]], [c[None, :], np.array([[q * (1 + t)]])]])).min() >= -1e-12) == (t >= 0) for t in (-0.1, -1e-3, 1e-3, 0.1))
    # max det at c = 0 for fixed d
    base = np.linalg.det(G) * d
    ok3 = all(np.linalg.det(np.block([[G, (s * rng.standard_normal(n))[:, None]], [(s * rng.standard_normal(n))[None, :] * 0 + 0, np.array([[d]])]])) <= base + 1e-12 for s in (0,))
    worse = []
    for _ in range(200):
        cc = rng.standard_normal(n) * 0.3
        Bc = np.block([[G, cc[:, None]], [cc[None, :], np.array([[d]])]])
        if np.linalg.eigvalsh(Bc).min() > 0: worse.append(np.linalg.det(Bc) <= base * (1 + 1e-12))
    # Delta I = log(d/(d-q)) = 2 I_Gauss
    dI = math.log(d / (d - q))
    hG = 0.5 * math.log(np.linalg.det(2 * math.pi * math.e * G)); hd = 0.5 * math.log(2 * math.pi * math.e * d)
    hB = 0.5 * math.log(np.linalg.det(2 * math.pi * math.e * B))
    MI = hG + hd - hB
    check(ok1 and ok2 and all(worse) and abs(dI - 2 * MI) < 1e-9, f'C1 random trial {trial}: det B = det G * Schur; PSD iff Schur >= 0; det max at c = 0 ({len(worse)} admissible c tried); Delta I = 2 I(X;Y) ({dI:.6f} vs {2*MI:.6f})')

# Loewner section on real zeta data (x = 13, N = 10 -> 11), reviewer's (a,b) at 400 bits, mpmath 120 digits
import mpmath as mp
mp.mp.dps = 120
ctx.prec = 450
a_, b_ = AB.ab_total(arb(13).log(), 12, AB.von_mangoldt_table(13), 450)
A = [mp.mpf(t.mid().str(130, radius=False)) for t in a_]; Bv = [mp.mpf(t.mid().str(130, radius=False)) for t in b_]
def blocks(M, bb):
    E = mp.matrix(M + 1, M + 1); O = mp.matrix(M, M)
    E[0, 0] = A[0]
    for j in range(1, M + 1):
        E[0, j] = E[j, 0] = mp.sqrt(2) * bb[j] / j; E[j, j] = A[j] + bb[j] / j; O[j - 1, j - 1] = A[j] - bb[j] / j
    for i in range(1, M + 1):
        for j in range(1, M + 1):
            if i != j:
                E[i, j] = (bb[i] - bb[j]) / (i - j) + (bb[i] + bb[j]) / (i + j)
                O[i - 1, j - 1] = (bb[i] - bb[j]) / (i - j) - (bb[i] + bb[j]) / (i + j)
    return E, O
N = 10; j = N + 1
def schurs(beta):
    bb = list(Bv); bb[j] = Bv[j] + beta
    E, O = blocks(j, bb)
    return mp.det(E) / mp.det(E[:j, :j]), mp.det(O) / mp.det(O[:N, :N])
h = mp.mpf('1e-8')
S = [schurs(t) for t in (-h, 0, h, 2 * h)]
res = {}
for k in (0, 1):
    sm, s0, sp_, s2 = S[0][k], S[1][k], S[2][k], S[3][k]
    C = -(sp_ + sm - 2 * s0) / (2 * h * h); l = (sp_ - sm) / (2 * h)
    pred2 = s0 + l * 2 * h - C * 4 * h * h
    res[k] = (C, l, s0)
    check(abs(pred2 - s2) < mp.mpf(10) ** -60 * abs(s0) + mp.mpf(10)**-90, f'C1 Loewner: {"even" if k == 0 else "odd"} Schur complement exactly quadratic in b_(N+1) (4th point residual {mp.nstr(abs(pred2 - s2), 3)})')
cen = [res[k][1] / (2 * res[k][0]) for k in (0, 1)]
rad = [mp.sqrt((res[k][2] + res[k][1] ** 2 / (4 * res[k][0])) / res[k][0]) for k in (0, 1)]
for k in (0, 1):
    for sgn in (-1, 1):
        s_end = schurs(cen[k] + sgn * rad[k])[k]
        check(abs(s_end) < mp.mpf(10) ** -80, f'C1 Loewner: block {k} interval endpoint {sgn:+d} gives a singular bordered block (Schur {mp.nstr(s_end, 3)})')
lo = max(cen[0] - rad[0], cen[1] - rad[1]); hi = min(cen[0] + rad[0], cen[1] + rad[1])
f = lambda t: mp.log(res[0][2] + res[0][1] * t - res[0][0] * t * t) + mp.log(res[1][2] + res[1][1] * t - res[1][0] * t * t)
fp = lambda t: sum((res[k][1] - 2 * res[k][0] * t) / (res[k][2] + res[k][1] * t - res[k][0] * t * t) for k in (0, 1))
x0, x1 = lo + (hi - lo) * mp.mpf(10) ** -30, hi - (hi - lo) * mp.mpf(10) ** -30
for _ in range(300):
    xm_ = (x0 + x1) / 2
    if fp(xm_) > 0: x0 = xm_
    else: x1 = xm_
tme = (x0 + x1) / 2   # f concave on (lo, hi): f' decreasing, bisection on its sign
print(f'   x=13, N=10: even interval centre {mp.nstr(cen[0],6)} r {mp.nstr(rad[0],4)}; odd centre {mp.nstr(cen[1],6)} r {mp.nstr(rad[1],4)} (beta = b - b_true)')
print(f'   joint interval [{mp.nstr(lo,6)}, {mp.nstr(hi,6)}], midpoint {mp.nstr((lo+hi)/2,6)}; joint max-det point {mp.nstr(tme,6)} = midpoint {mp.nstr((tme-(lo+hi)/2)/((hi-lo)/2),4)} half-widths')
check(abs(tme - (lo + hi) / 2) > (hi - lo) / 20, 'C1 counter-check: the joint (V_n-basis) max-det b_(N+1) is NOT the centre of the joint admissible interval (differs by > 0.1 half-width)')
# c = 0 is not a Loewner column: symbolic
Ns = 4; jj = Ns + 1
bs = sp.symbols('b1:%d' % (jj + 1))
ce = [sp.sqrt(2) * bs[jj - 1] / jj] + [(bs[i - 1] - bs[jj - 1]) / (i - jj) + (bs[i - 1] + bs[jj - 1]) / (i + jj) for i in range(1, jj)]
co = [(bs[i - 1] - bs[jj - 1]) / (i - jj) - (bs[i - 1] + bs[jj - 1]) / (i + jj) for i in range(1, jj)]
sol = sp.solve(ce + co, bs, dict=True)
check(sol == [{s: 0 for s in bs}], f'C1: c_e = c_o = 0 forces b_1 = ... = b_{jj} = 0 (N = {Ns}, sympy: {sol})')
sol_e = sp.solve(ce, bs, dict=True)
check(sol_e == [{s: 0 for s in bs}], 'C1: already the even column alone vanishes only for b = 0')

# ---------------- C4: Kronecker-sum lemma ----------------
print('## C4 (lemma 4.1 of lane A2)')
def lattice(S, Amax):
    return list(itertools.product(range(Amax + 1), repeat=len(S)))
for S, Amax in (((2, 3), 2), ((2, 3, 5), 1), ((2, 3, 5), 2), ((2, 3), 3)):
    pts = lattice(S, Amax); logp = np.log(S)
    t = np.array([np.dot(p, logp) for p in pts])
    coef = rng.standard_normal(6)
    g = lambda D: 3.0 + sum(coef[k] * np.cos((k + 1) * 0.7 * D) * np.exp(-0.1 * D) for k in range(6))   # arbitrary even function, g(0) = diag
    G = np.array([[g(abs(t[i] - t[k])) for k in range(len(pts))] for i in range(len(pts))])
    ndiff = np.array([[sum(pi != pk for pi, pk in zip(pts[i], pts[k])) for k in range(len(pts))] for i in range(len(pts))])
    Gn = np.where(ndiff >= 2, 0.0, G)
    d = g(0.0)
    Kr = d * np.eye(len(pts))
    Gp = []
    for q, p in enumerate(S):
        Gq = np.array([[g(abs(a - b) * math.log(p)) for b in range(Amax + 1)] for a in range(Amax + 1)])
        Gp.append(Gq)
        term = np.array([[1.0]])
        for r in range(len(S)):
            term = np.kron(term, (Gq - d * np.eye(Amax + 1)) if r == q else np.eye(Amax + 1))
        Kr += term
    w, V = np.linalg.eigh(Gn)
    lam_pred = d + sum(np.linalg.eigvalsh(Gq)[0] - d for Gq in Gp)
    vprod = np.array([[1.0]])
    for Gq in Gp: vprod = np.kron(vprod, np.linalg.eigh(Gq)[1][:, [0]])
    ov = abs(float(vprod[:, 0] @ V[:, 0]))
    check(np.abs(Gn - Kr).max() < 1e-13 and abs(w[0] - lam_pred) < 1e-12 and abs(ov - 1) < 1e-10,
          f'C4 S={S} A={Amax}: G with mixed entries zeroed = Kronecker sum (max diff {np.abs(Gn-Kr).max():.1e}); lambda_min = sum rule; eigvec = product (1-overlap {1-ov:.1e}); arbitrary even kernel, no admissibility used')

# ---------------- C8: max-det completion of Toeplitz data ----------------
print('## C8 (max-det next lag = disc centre = Burg)')
def toeplitz_prop(nu, n):
    """prop:extension-disc's convention: T_jk = nu_(j-k), nu_(-k) = conj(nu_k); then the last column above the
    diagonal is u(x) = (conj x, conj nu_K, ..., conj nu_1)^T as the proposition writes."""
    T = np.empty((n, n), complex)
    for j in range(n):
        for k in range(n):
            T[j, k] = nu[j - k] if j >= k else np.conj(nu[k - j])
    return T
from scipy.optimize import minimize
def verblunsky(nuseq):
    """Levinson-Durbin reflection coefficients (for T_jk = nu_(j-k)); returns list, final error"""
    n = len(nuseq)
    refl = []
    for m in range(1, n):
        Tm = toeplitz_prop(nuseq[:m + 1], m + 1)
        # reflection coefficient = -(normalised) partial correlation: 1 - |k|^2 = e_m/e_(m-1)
        e_m = np.linalg.det(Tm).real / np.linalg.det(Tm[:m, :m]).real
        e_p = np.linalg.det(Tm[:m, :m]).real / (np.linalg.det(Tm[:m - 1, :m - 1]).real if m > 1 else 1.0)
        refl.append(np.sqrt(max(0.0, 1 - e_m / e_p)))
    return refl
for trial in range(4):
    K = 5
    th = rng.uniform(0, 2 * np.pi, 9); wt = rng.uniform(0.2, 1.0, 9)
    nu = [complex(np.sum(wt * np.exp(1j * k * th))) + (0.3 if k == 0 else 0) for k in range(K + 1)]
    TK = toeplitz_prop(nu, K + 1); TKi = np.linalg.inv(TK)
    w = np.array([0] + [np.conj(nu[K + 1 - i]) for i in range(1, K + 1)])
    col = toeplitz_prop(nu + [0.37 + 0.11j], K + 2)[:K + 1, K + 1]
    conv_ok = np.allclose(col, np.array([np.conj(0.37 + 0.11j)] + list(w[1:])))
    c_printed = -(TKi @ w)[0] / TKi[0, 0]                 # as printed in prop:extension-disc(i)
    c_conj = -np.conj((TKi @ w)[0]) / TKi[0, 0]           # with the conjugate
    rK = np.linalg.det(TK).real / np.linalg.det(TK[:K, :K]).real
    detf = lambda x: np.linalg.det(toeplitz_prop(nu + [x], K + 2)).real
    best = minimize(lambda z: -detf(z[0] + 1j * z[1]), [c_conj.real + 0.3 * rK, c_conj.imag - 0.2 * rK], method='Nelder-Mead', options=dict(xatol=1e-13, fatol=1e-18, maxiter=6000))
    xm = best.x[0] + 1j * best.x[1]
    refl = verblunsky(nu + [c_conj])
    ang = np.linspace(0, 2 * np.pi, 13)
    inside = all(np.linalg.eigvalsh(toeplitz_prop(nu + [c_conj + 0.999 * rK * np.exp(1j * a)], K + 2)).min() > -1e-10 for a in ang)
    outside = all(np.linalg.eigvalsh(toeplitz_prop(nu + [c_conj + 1.001 * rK * np.exp(1j * a)], K + 2)).min() < 0 for a in ang)
    # (ii) Yule-Walker as printed: T_(K-1) a = -(nu_1..nu_K)^T, c = -sum a_j nu_(K+1-j)
    aYW = np.linalg.solve(toeplitz_prop(nu, K), -np.array(nu[1:K + 1]))
    cYW = -sum(aYW[jj - 1] * nu[K + 1 - jj] for jj in range(1, K + 1))
    check(conv_ok and abs(xm - c_conj) < 1e-6 * rK and refl[-1] < 1e-6 and inside and outside,
          f'C8 trial {trial} (complex data): argmax_x det T_(K+1)(x) = centre (|diff|/r_K = {abs(xm-c_conj)/rK:.1e}); next reflection coefficient there {refl[-1]:.1e}; admissible set = disc of radius det T_K/det T_(K-1)')
    print(f'   prop (i) as printed: |c_printed - argmax|/r_K = {abs(c_printed - xm)/rK:.3f};  (ii) Yule-Walker as printed: |c_YW - argmax|/r_K = {abs(cYW - xm)/rK:.3f}')
    if trial == 0:
        check(abs(c_printed - xm) > 1e-3 * rK, 'C8 side finding: prop:extension-disc(i) as printed, c_K = -(W^-1 w)_0/(W^-1)_00, is off for complex data; the centre is -conj((W^-1 w)_0)/(W^-1)_00 (identical for real data)')
    # multi-step: n x n band completion by always taking the centre (zero reflection coefficients)
    n = K + 5
    nuext = list(nu)
    for m in range(K + 1, n):
        Tm = toeplitz_prop(nuext, m); Tmi = np.linalg.inv(Tm)
        wm = np.array([0] + [np.conj(nuext[m - i]) for i in range(1, m)])
        nuext.append(-np.conj((Tmi @ wm)[0]) / Tmi[0, 0])
    W = toeplitz_prop(nuext, n); Wi = np.linalg.inv(W)
    off = max(abs(Wi[i, k]) for i in range(n) for k in range(n) if abs(i - k) > K)
    check(off < 1e-10 * np.abs(Wi).max(), f'C8 trial {trial}: centre-by-centre extension to {n}x{n} has inverse vanishing outside the band (max {off:.1e}): stationary point of the strictly concave log det on the free entries, hence the unique max-det completion, and it is Toeplitz')
# real symmetric: unconstrained (non-Toeplitz) max-det completion by damped Newton-free BFGS from a PD start
K = 2; n = 6
nu = [2.0, 0.9, -0.3]
free = [(i, k) for i in range(n) for k in range(i + 1, n) if k - i > K]
nuext = list(nu)
for m in range(K + 1, n):
    Tm = np.array([[nuext[abs(i - k)] for k in range(m)] for i in range(m)]); Tmi = np.linalg.inv(Tm)
    wm = np.array([0] + [nuext[m - i] for i in range(1, m)])
    nuext.append(-(Tmi @ wm)[0] / Tmi[0, 0])
def build(z):
    T = np.array([[nu[abs(i - k)] if abs(i - k) <= K else 0.0 for k in range(n)] for i in range(n)])
    for (i, k), v in zip(free, z): T[i, k] = T[k, i] = v
    return T
def negld(z):
    ev = np.linalg.eigvalsh(build(z))
    return 1e10 if ev.min() <= 0 else -np.sum(np.log(ev))
def grad(z):
    Wi_ = np.linalg.inv(build(z)); return np.array([-2 * Wi_[i, k] for (i, k) in free])
z0 = np.array([nuext[k - i] for (i, k) in free]) + rng.uniform(-0.05, 0.05, len(free))
check(np.linalg.eigvalsh(build(z0)).min() > 0, 'C8: perturbed start is a PD completion')
opt = minimize(negld, z0, jac=grad, method='BFGS', options=dict(gtol=1e-13))
Wopt = build(opt.x)
toe_dev = max(abs(Wopt[i, k] - Wopt[0, k - i]) for i in range(n) for k in range(i, n))
check(toe_dev < 1e-7 and abs(Wopt[0, n - 1] - nuext[n - 1]) < 1e-7 and np.abs(z0 - opt.x).max() > 1e-3,
      f'C8: unconstrained max-det completion of a real band-{K} Toeplitz pattern ({n}x{n}, BFGS from a perturbed PD start) is Toeplitz (dev {toe_dev:.1e}) and equals the centre-by-centre (Burg/AR) extension (corner diff {abs(Wopt[0,n-1]-nuext[n-1]):.1e})')

# re-verdict pass: prop:extension-disc(i) as corrected (conjugate) -- centre and the printed radius formula on complex data
for trial in range(3):
    K = 4
    th = rng.uniform(0, 2 * np.pi, 7); wt = rng.uniform(0.2, 1.0, 7)
    nu = [complex(np.sum(wt * np.exp(1j * k * th))) + (0.2 if k == 0 else 0) for k in range(K + 1)]
    TK = toeplitz_prop(nu, K + 1); TKi = np.linalg.inv(TK)
    w = np.array([0] + [np.conj(nu[K + 1 - i]) for i in range(1, K + 1)])
    c = -np.conj((TKi @ w)[0]) / TKi[0, 0]
    r2 = (nu[0].real - (np.conj(w) @ TKi @ w).real) / TKi[0, 0].real + abs(c) ** 2
    rdet = np.linalg.det(TK).real / np.linalg.det(TK[:K, :K]).real
    g = lambda x: nu[0].real - (np.conj(np.array([np.conj(x)] + list(w[1:]))) @ TKi @ np.array([np.conj(x)] + list(w[1:]))).real
    check(abs(r2 - rdet ** 2) < 1e-9 * rdet ** 2 and abs(g(c + np.sqrt(r2) * np.exp(0.7j))) < 1e-9 and g(c) > 0,
          f'prop:extension-disc(i) corrected, complex trial {trial}: centre -conj((W^-1 w)_0)/(W^-1)_00 and r_K^2 formula = (det W_K/det W_(K-1))^2 (rel diff {abs(r2 - rdet**2)/rdet**2:.1e}); g = 0 on the circle')

# ---------------- C9: dimension counts by exact rank ----------------
print('## C9 (kinematic dimensions, exact rank over Q)')
def dims(N):
    idx = list(range(-N, N + 1)); m = len(idx); pos = {v: i for i, v in enumerate(idx)}
    # real coordinates of Hermitian H: h_nn (m), Re h_nm, Im h_nm for n<m ; plus beta_n = x_n + i y_n
    var = {}
    for i in range(m): var[('d', i)] = len(var)
    for i in range(m):
        for k in range(i + 1, m): var[('r', i, k)] = len(var); var[('i', i, k)] = len(var)
    nH = len(var)
    for i in range(m): var[('bx', i)] = len(var); var[('by', i)] = len(var)
    nv = len(var)
    def ent(i, k):
        """(real part coeffs, imag part coeffs) of H_ik as dicts"""
        if i == k: return {var[('d', i)]: 1}, {}
        if i < k: return {var[('r', i, k)]: 1}, {var[('i', i, k)]: 1}
        return {var[('r', k, i)]: 1}, {var[('i', k, i)]: -1}
    rows = {'gamma': [], 'real': [], 'loew': []}
    for i in range(m):
        for k in range(i, m):
            gi, gk = pos[-idx[i]], pos[-idx[k]]
            R1, I1 = ent(i, k); R2, I2 = ent(gi, gk)
            for A1, A2 in ((R1, R2), (I1, I2)):
                r = [0] * nv
                for v, c in A1.items(): r[v] += c
                for v, c in A2.items(): r[v] -= c
                if any(r): rows['gamma'].append(r)
            if i != k:
                r = [0] * nv; r[var[('i', i, k)]] = 1; rows['real'].append(r)
            # Loewner: (n - m) H_ik = beta_i - conj(beta_k)
            dn = idx[i] - idx[k]
            rr = [0] * nv; ri = [0] * nv
            for v, c in R1.items(): rr[v] += dn * c
            for v, c in I1.items(): ri[v] += dn * c
            rr[var[('bx', i)]] -= 1; rr[var[('bx', k)]] += 1
            ri[var[('by', i)]] -= 1; ri[var[('by', k)]] -= 1
            rows['loew'].append(rr); rows['loew'].append(ri)
    def nullity(rs, with_beta):
        cols = nv if with_beta else nH
        if not rs: return cols
        M = fmpq_mat(len(rs), cols, [fmpq(x) for r in rs for x in r[:cols]])
        return cols - M.rref()[1]
    beta_only = 1   # beta_n real and constant (checked below)
    # constraints on beta when H = 0: rank of loew rows restricted to beta columns
    Mb = fmpq_mat(len(rows['loew']), 2 * m, [fmpq(x) for r in rows['loew'] for x in r[nH:]])
    kb = 2 * m - Mb.rref()[1]
    out = dict(herm=nullity([], False), gamma=nullity(rows['gamma'], False), real=nullity(rows['real'], False),
               gamma_real=nullity(rows['gamma'] + rows['real'], False),
               loew=nullity(rows['loew'], True) - kb, loew_real=nullity(rows['loew'] + rows['real'], True) - kb,
               loew_gamma=nullity(rows['loew'] + rows['gamma'], True) - kb)
    return out, kb
for N in range(1, 8):
    o, kb = dims(N)
    exp = dict(herm=(2 * N + 1) ** 2, gamma=(N + 1) ** 2 + N ** 2, real=(N + 1) * (2 * N + 1), gamma_real=(N + 1) ** 2,
               loew=4 * N + 1, loew_real=4 * N + 1, loew_gamma=2 * N + 1)
    check(o == exp and kb == 1, f'C9 N={N}: {o} (beta-only kernel {kb})')
print(f'# checks: {NCHK[0]} run, {NCHK[1]} failed')
