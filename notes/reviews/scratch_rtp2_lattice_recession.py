#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane L (claude:opus, 2026-09-26): L1 and L5 checked independently.
(1) L1's annihilator: for random interior positions build P(z) = prod (1 - 2 c_k z^{r_k} + z^{2 r_k}), Q = P (1 + ... + z^d),
    check q_n > 0 and sum_n q_n cos(2 pi n t_k) = 0 = sum_n q_n sin(2 pi n t_k) in exact/high precision; check that at the cutoff
    B the recession cone is zero (dual certificate found numerically), and that t -> 0 defeats any fixed N.
(2) L5 at x = 13: atoms log 2 .. log(m+1), window L = log 13.  At each (m, N) decide the recession cone by two small SDPs solved
    with the reviewer's own barrier method (numpy): RAY  max t s.t. T(delta) >= t I, |delta_k| <= 1;
    ZERO max t s.t. Z >= t I, tr Z = 1, tr(Z T_k) = 0 (Z block-diagonal, even/odd).  t_RAY > 0 gives a PD recession ray;
    t_ZERO > 0 with an injective atom map proves the cone is {0} (tr(Z T(delta)) = 0 with Z > 0 forces T(delta) = 0).
    Both witnesses are then re-verified in mpmath at 60 digits (exact projection onto the atom-orthogonal space; Cholesky).
No zeros are used."""
import sys, os, math, itertools
import numpy as np
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
NCHK = [0, 0]
def check(c, msg):
    NCHK[0] += 1; NCHK[1] += (not c); print(('PASS ' if c else 'FAIL ') + msg, flush=True)

def blocks_np(a, b, N):
    E = np.zeros((N + 1, N + 1)); O = np.zeros((N, N)); s2 = math.sqrt(2)
    E[0, 0] = a[0]
    for j in range(1, N + 1):
        E[0, j] = E[j, 0] = s2 * b[j] / j; E[j, j] = a[j] + b[j] / j; O[j - 1, j - 1] = a[j] - b[j] / j
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                t = (b[i] - b[j]) / (i - j); u = (b[i] + b[j]) / (i + j); E[i, j] = t + u; O[i - 1, j - 1] = t - u
    return E, O
def atom_np(N, t):
    return blocks_np([-2 * (1 - t) * math.cos(2 * math.pi * j * t) for j in range(N + 1)],
                     [math.sin(2 * math.pi * j * t) / math.pi for j in range(N + 1)], N)
def atom_mp(N, t):
    a = [-2 * (1 - t) * mp.cos(2 * mp.pi * j * t) for j in range(N + 1)]; b = [mp.sin(2 * mp.pi * j * t) / mp.pi for j in range(N + 1)]
    E = mp.matrix(N + 1, N + 1); O = mp.matrix(N, N); s2 = mp.sqrt(2); E[0, 0] = a[0]
    for j in range(1, N + 1):
        E[0, j] = E[j, 0] = s2 * b[j] / j; E[j, j] = a[j] + b[j] / j; O[j - 1, j - 1] = a[j] - b[j] / j
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                u = (b[i] - b[j]) / (i - j); v = (b[i] + b[j]) / (i + j); E[i, j] = u + v; O[i - 1, j - 1] = u - v
    return E, O

# ---------------- generic barrier: maximise t s.t. F0 + sum x_j F_j - t I >= 0 (block list), plus optional box |x|<=1 -------------
def max_lmin(F0, Fs, box):
    nb = len(F0); n = len(Fs)
    x = np.zeros(n)
    lm = min(np.linalg.eigvalsh(F0[b])[0] for b in range(nb) if F0[b].size)
    t = lm - 1.0
    def mats(x, t): return [F0[b] + sum(x[j] * Fs[j][b] for j in range(n)) - t * np.eye(F0[b].shape[0]) for b in range(nb)]
    def phi(x, t, mu):
        s = t
        for M in mats(x, t):
            if M.size == 0: continue
            w = np.linalg.eigvalsh(M)
            if w[0] <= 0: return -np.inf
            s += mu * np.sum(np.log(w))
        if box:
            if np.any(np.abs(x) >= 1): return -np.inf
            s += mu * np.sum(np.log(1 - x * x))
        return s
    mu = 1.0
    for stage in range(40):
        for it in range(100):
            Ms = mats(x, t); g = np.zeros(n + 1); H = np.zeros((n + 1, n + 1)); g[n] = 1.0
            for b, M in enumerate(Ms):
                if M.size == 0: continue
                Mi = np.linalg.inv(M)
                P = [Mi @ Fs[j][b] for j in range(n)] + [-Mi]
                for a in range(n + 1):
                    g[a] += mu * np.trace(P[a])
                    for c in range(a, n + 1):
                        H[a, c] -= mu * np.sum(P[a] * P[c].T); H[c, a] = H[a, c]
            if box:
                g[:n] += mu * (-2 * x / (1 - x * x)); H[np.arange(n), np.arange(n)] += mu * (-2 * (1 + x * x) / (1 - x * x) ** 2)
            try: st = np.linalg.solve(-H, g)
            except np.linalg.LinAlgError: st = np.linalg.lstsq(-H, g, rcond=None)[0]
            dec = g @ st
            f0 = phi(x, t, mu); s = 1.0
            while s > 1e-14:
                xn, tn = x + s * st[:n], t + s * st[n]
                if phi(xn, tn, mu) >= f0 + 0.25 * s * dec: break
                s /= 2
            x, t = xn, tn
            if dec < 1e-12: break
        mu /= 4
        if mu < 1e-13: break
    return t, x

def affine_basis(Tlist, N):
    """orthonormal basis (Frobenius, block-diagonal Z = (ZE, ZO)) of {Z : tr(Z T_k) = 0 for all k}; returns Z0 with tr Z0 = 1"""
    dE, dO = N + 1, N
    def vecz(E, O): return np.r_[E[np.triu_indices(dE)] * np.where(np.eye(dE)[np.triu_indices(dE)] > 0, 1, 2), O[np.triu_indices(dO)] * np.where(np.eye(dO)[np.triu_indices(dO)] > 0, 1, 2)] if dO else E[np.triu_indices(dE)] * np.where(np.eye(dE)[np.triu_indices(dE)] > 0, 1, 2)
    # coordinates: upper-triangular entries of ZE, ZO; tr(Z T) = sum_i<=j c_ij * T_ij * (2 if i<j)
    A = np.array([vecz(*Tk) for Tk in Tlist])            # m x D
    tr = vecz(np.eye(dE), np.eye(dO) if dO else np.zeros((0, 0)))
    Aall = np.vstack([A, tr])
    D = Aall.shape[1]
    # particular solution of A c = 0, tr c = 1, and nullspace
    rhs = np.r_[np.zeros(len(Tlist)), 1.0]
    c0 = np.linalg.lstsq(Aall, rhs, rcond=None)[0]
    U, s, Vt = np.linalg.svd(Aall); rank = int(np.sum(s > 1e-10 * s[0])); Nsp = Vt[rank:].T
    def mat(c):
        iu = np.triu_indices(dE); E = np.zeros((dE, dE)); E[iu] = c[:len(iu[0])]; E = E + E.T - np.diag(np.diag(E))
        if dO:
            io = np.triu_indices(dO); O = np.zeros((dO, dO)); O[io] = c[len(iu[0]):]; O = O + O.T - np.diag(np.diag(O))
        else: O = np.zeros((0, 0))
        return E, O
    return c0, Nsp, mat, rank

def decide(m, N, L=math.log(13)):
    ts = [math.log(n) / L for n in range(2, m + 2)]
    Tl = [atom_np(N, t) for t in ts]
    # injectivity of the atom map on R^m (Loewner data a_0..a_N, b_1..b_N)
    Amap = np.array([[-2 * (1 - t) * math.cos(2 * math.pi * j * t) for j in range(N + 1)] + [math.sin(2 * math.pi * j * t) / math.pi for j in range(1, N + 1)] for t in ts]).T
    rk = np.linalg.matrix_rank(Amap, tol=1e-12)
    if rk < m: return 'KERNEL', None, rk
    tray, xr = max_lmin([np.zeros_like(B) for B in Tl[0]], Tl, box=True)
    c0, Nsp, mat, rank = affine_basis(Tl, N)
    F0 = list(mat(c0)); Fs = [list(mat(Nsp[:, j])) for j in range(Nsp.shape[1])]
    tz, cz = max_lmin(F0, Fs, box=False) if Nsp.shape[1] else (-1, None)
    return ('RAY' if tray > 1e-9 else ('ZERO' if tz > 1e-12 else 'UNDECIDED')), (tray, xr, tz, (c0 + Nsp @ cz) if cz is not None else None, mat), rk

def certify(m, N, kind, data, L13=None):
    mp.mp.dps = 60
    L = mp.log(13); ts = [mp.log(n) / L for n in range(2, m + 2)]
    Tm = [atom_mp(N, t) for t in ts]
    if kind == 'RAY':
        x = [mp.mpf(float(v)) for v in data[1]]
        E = sum((x[k] * Tm[k][0] for k in range(m)), mp.zeros(N + 1)); O = sum((x[k] * Tm[k][1] for k in range(m)), mp.zeros(N))
        lm = min(mp.eigsy(E, eigvals_only=True)[0], mp.eigsy(O, eigvals_only=True)[0] if N else mp.inf)
        return lm > 0, lm
    # ZERO: Z0 from double, then project exactly onto {tr(Z T_k) = 0}: Z = Z0 - sum h_i T_i, Gram system M h = r
    E0, O0 = data[4](data[3]); Z0 = (mp.matrix(E0.tolist()), mp.matrix(O0.tolist()) if N else mp.matrix(0, 0))
    ip = lambda A, B: mp.fsum(A[0][i, j] * B[0][i, j] for i in range(N + 1) for j in range(N + 1)) + (mp.fsum(A[1][i, j] * B[1][i, j] for i in range(N) for j in range(N)) if N else 0)
    M = mp.matrix(m, m); r = mp.matrix(m, 1)
    for i in range(m):
        r[i] = ip(Z0, Tm[i])
        for j in range(m): M[i, j] = ip(Tm[i], Tm[j])
    h = mp.lu_solve(M, r)
    ZE = Z0[0] - sum((h[i] * Tm[i][0] for i in range(m)), mp.zeros(N + 1)); ZO = Z0[1] - sum((h[i] * Tm[i][1] for i in range(m)), mp.zeros(N))
    Zc = (ZE, ZO); res = max(abs(ip(Zc, Tm[i])) for i in range(m))
    lm = min(mp.eigsy(ZE, eigvals_only=True)[0], mp.eigsy(ZO, eigvals_only=True)[0])
    return lm > 0 and res < mp.mpf(10) ** -50, lm

# ---------------- (1) L1 annihilator on random positions ----------------
rng = np.random.default_rng(20260926)
from fractions import Fraction
for trial in range(4):
    mm = int(rng.integers(2, 5)); tpos = sorted(rng.uniform(0.05, 0.95, mm))
    r = [math.ceil(1 / (4 * min(t, 1 - t))) for t in tpos]; cks = [math.cos(2 * math.pi * rk * t) for rk, t in zip(r, tpos)]
    P = np.array([1.0])
    for rk, c in zip(r, cks):
        f = np.zeros(2 * rk + 1); f[0] = 1; f[rk] = -2 * c; f[2 * rk] = 1; P = np.convolve(P, f)
    d = len(P) - 1; Q = np.convolve(P, np.ones(d + 1)); B = 2 * d
    res = max(max(abs(np.sum(Q * np.cos(2 * math.pi * np.arange(B + 1) * t))), abs(np.sum(Q * np.sin(2 * math.pi * np.arange(B + 1) * t)))) / np.sum(Q) for t in tpos)
    check(np.all(Q > 0) and all(c <= 1e-15 for c in cks) and B == 4 * sum(r) and res < 1e-12,
          f'L1 annihilator, positions {np.round(tpos, 3).tolist()}: r = {r}, c_k <= 0, all {B + 1} coefficients q_n > 0 (min {Q.min():.3g}), sum q_n e(n t_k) = 0 (rel {res:.1e}); B = 4 sum r_k = {B}')
    # the proof's identity is itself a PD dual certificate: Z = diag(z_n), z_0 = q_0, z_{+-n} = q_n / 2 (|n| <= B) has
    # tr(Z T_k) = -2 (1 - t_k) sum_n q_n cos(2 pi n t_k) = 0 for every k, so T(delta) >= 0 forces tr(Z T(delta)) = 0, T(delta) = 0
    z = np.r_[Q[:0:-1] / 2, Q[0], Q[1:] / 2]
    trs = [abs(sum(z[i] * (-2 * (1 - t) * math.cos(2 * math.pi * (i - B) * t)) for i in range(2 * B + 1))) / z.sum() for t in tpos]
    check(min(z) > 0 and max(trs) < 1e-12, f'   at N = B = {B}: Z = diag(q) is positive definite (min {min(z):.3g}) and orthogonal to every atom (rel {max(trs):.1e}): zero recession cone')
# t -> 0 defeats every fixed N
for N_ in (5, 20, 60):
    t = 1e-3 / N_; E, O = atom_np(N_, t)
    check(np.linalg.eigvalsh(-E)[0] > 0 and np.linalg.eigvalsh(-O)[0] > 0, f'L1(no m-only threshold): one atom at t = {t:.1e}, N = {N_}: -T is positive definite (lambda_min {min(np.linalg.eigvalsh(-E)[0], np.linalg.eigvalsh(-O)[0]):.4f}), so delta = -1 is a recession direction')
# edge atom: T_L = 0
E, O = atom_np(12, 1.0); check(np.abs(E).max() < 1e-12 and np.abs(O).max() < 1e-12, 'edge atom t = 1: all Loewner entries vanish (|T| < 1e-12), so its weight is free')
# operator norm of T_k on E_N stays below 2 (used in L3)
for N_ in (20, 80, 200):
    nrm = max(max(np.abs(np.linalg.eigvalsh(B)).max() for B in atom_np(N_, math.log(n) / math.log(13))) for n in range(2, 13))
    check(nrm <= 2, f'||T_k|| on E_{N_} over n = 2..12 at x = 13: max {nrm:.6f} <= 2')

# ---------------- (2) L5 table ----------------
LANE = {2: 2, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 5, 10: 5, 11: 6}
for m in range(2, 12):
    first = None; log = []
    for N in range(0, 9):
        if 2 * N + 1 < m: log.append(f'N={N}:KERNEL(2N+1<m)'); continue
        kind, data, rk = decide(m, N)
        if kind in ('RAY', 'ZERO'):
            ok, lm = certify(m, N, kind, data)
            log.append(f'N={N}:{kind}{"*" if ok else "?"}({mp.nstr(lm, 3)})')
        else:
            ok = False; log.append(f'N={N}:{kind}(tray={data[0] if data else None})')
        if kind == 'ZERO' and ok: first = N; break
    check(first == LANE[m], f'L5 m={m}: first zero-cone cutoff {first} (lane {LANE[m]}); ' + ' '.join(log))
print(f'# checks: {NCHK[0]} run, {NCHK[1]} failed')
