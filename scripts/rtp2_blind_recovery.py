#!/usr/bin/env python3
"""rtp2_blind_recovery.py -- RTP round 2, blind-recovery lane (author line: claude:opus).

Certified, multiprecision version of the REFUTE reviewer's blind-recovery experiment
(notes/reviews/rtp-round-2-grid-tomography-2026-09-26.md, "Point (d)").

PROBLEM.  Window [0, L], L = log x, t = y/L.  Input: the pole and archimedean Loewner data (a0_n, b0_n),
n = 0..N, i.e. the form H0 (even block N+1, odd block N; plan.md 1.3), and a finite grid of positions
t_j in (0, 1).  NO prime position, NO prime weight, NO zero of zeta enters.  Unknown: w_j >= 0.
    tau*(grid, N) = - max_{w >= 0} lambda_min( H0 + sum_j w_j T(t_j) ),
T(t) = the Loewner blocks of the unit atom moment vector phi(t) = (A_0..A_N, B_1..B_N),
A_n = -2(1-t)cos(2 pi n t), B_n = sin(2 pi n t)/pi (lane G convention; reviewer's helpers).
Weak duality: for every PSD Z with tr(Z T(t_j)) <= 0 on the grid,  lambda_min(H(w)) <= tr(Z H0)/tr Z.

METHOD.
  * float64: primal-dual interior point method (HKM direction, Mehrotra predictor-corrector) written here,
    in the moment coordinates (every T(t_j) = K(phi(t_j)), K the Loewner assembly; every basis matrix of K is
    rank two, u e_i^T + e_i u^T, so the Schur complement costs O(n^2 (2N+1)) plus O(J^2) per step).
  * mpmath certificate at DPS = 80 digits:
      (a) primal: w (binary floats, exact) -> H(w) in mp -> Cholesky of H(w) - s0 I in each block, residual
          E = (H - s0 I) - R R^T in mp; lambda_min(H(w)) >= s0 - ||E||_F - (entry error bound) * dim;
      (b) dual: Z = sum_k mu_k u_k u_k^T (mu_k >= 0 binary floats, u_k binary float vectors: PSD exactly),
          q_j = tr(Z T(t_j)) in mp, repaired by rho e_0 e_0^T with rho = max_j (q_j + err)^+ / (2(1-t_j))
          (tr(e0 e0^T T(t)) = A_0(t) = -2(1-t) < 0 on the interior), upper bound (tr(Z H0) + rho a0_0 + err)/tr.
    The data error of H0 is bounded by comparison with zst's ball data (pole + archimedean, prime cutoff 1)
    plus zst's radii; rounding is bounded by 10^(8-DPS) times absolute sums (at most 10^6 operations per chain).
  * blind coarse-to-fine refinement: level 0 = uniform grid t = j/M; level k = the level-0 uniform grid UNION
    patches of 17 points at spacing h_k = h_0/8^k centred on every level-(k-1) support point (w_j > 1e-4 total).
    The uniform grid stays in every level, so mass can always leave the patches.
  * clusters: maximal runs of support points with consecutive gaps <= 2.01 h_k (level k spacing);
    position = mass-weighted centroid y = L sum w t / sum w, mass = sum w.
  * COMPARISON WITH THE PRIMES (after every solve; uses no zeros): each cluster against the nearest log n,
    mass against Lambda(n)/sqrt n.  The truth's lambda_min (x = 13) is a comparison value only.
  * controls: pole only (arch -> 0), arch negated, pole residue x 0.9 and x 1.1, and signed w (unbounded:
    explicit w with H0 + T(w) = c I, verified in mp).

Deterministic; no timestamps; every claim through check(cond, msg).  Parallel over cases (multiprocessing,
one BLAS thread per worker).  Run:  python3 scripts/rtp2_blind_recovery.py > outputs/rtp2_blind_recovery.txt
"""
import os
for _v in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_v] = '1'
import sys
import inspect
import subprocess
import tempfile
from fractions import Fraction
from math import sumprod
from multiprocessing import Pool

import numpy as np
import mpmath as mp
from mpmath.libmp import from_man_exp, round_nearest
from scipy.linalg import cho_factor, cho_solve, eigh, LinAlgError

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, 'notes', 'reviews'))
from scratch_rtp2_grid_common import ab0, phi, blocks, prime_powers, blocks_np, phi_np  # noqa: E402

DPS = 80
SUPPORT_FRAC = 1e-4

# ---------------------------------------------------------------------------------------------------------
# the single assertion helper (as in scripts/gl1_bond.py)
# ---------------------------------------------------------------------------------------------------------
_PASS = 0
_FAIL = 0
_FAILED = []


def check(cond, msg):
    """The single assertion helper: counts, prints one line, never aborts."""
    global _PASS, _FAIL
    line = inspect.currentframe().f_back.f_lineno
    ok = bool(cond)
    if ok:
        _PASS += 1
    else:
        _FAIL += 1
        _FAILED.append((line, msg))
    print(f"  {'ok  ' if ok else 'FAIL'} [L{line:4d}]  {msg}", flush=True)
    return ok


def note(msg):
    print(f"  --           {msg}", flush=True)


def head(msg):
    print()
    print("=" * 110)
    print(msg)
    print("=" * 110, flush=True)


# ---------------------------------------------------------------------------------------------------------
# data: pole and archimedean parts (mp), variants for the controls
# ---------------------------------------------------------------------------------------------------------
def pole_ab(x, N):
    """pole part of (a_n, b_n) alone (the reviewer's ab0 pole lines, direct exponentials)."""
    L = mp.log(x); pi = mp.pi; half = mp.mpf(1) / 2
    a = []; b = []
    for n in range(N + 1):
        w = 2 * pi * n / L
        ap = mp.mpf(0); bp = mp.mpf(0)
        for s in (half, -half):
            sig = mp.mpc(s, w); eL = mp.exp(sig * L)
            J = -1 / sig + (eL - 1) / (sig * sig * L)
            ap += 2 * J.real
            bp += -((eL - 1) / sig).imag / pi
        a.append(ap); b.append(bp if n else mp.mpf(0))
    return a, b


VARIANTS = {            # (pole coefficient, archimedean coefficient)
    'true': (1, 1), 'pole_only': (1, 0), 'arch_neg': (1, -1), 'pole0.9': (mp.mpf('0.9'), 1), 'pole1.1': (mp.mpf('1.1'), 1),
}


def h0_data(x, N, variant, dps=DPS):
    """(a, b) of the input form for the variant, as mp lists at dps."""
    with mp.workdps(dps + 10):
        a0, b0 = ab0(x, N)
        ap, bp = pole_ab(x, N)
        cp, ca = VARIANTS[variant]
        a = [cp * ap[n] + ca * (a0[n] - ap[n]) for n in range(N + 1)]
        b = [cp * bp[n] + ca * (b0[n] - bp[n]) for n in range(N + 1)]
    return [+v for v in a], [+v for v in b]


# ---------------------------------------------------------------------------------------------------------
# rank-two basis of the Loewner assembly K: moment vector m = (a_0..a_N, b_1..b_N) -> (E, O)
# every basis matrix is  u e_i^T + e_i u^T  in each block
# ---------------------------------------------------------------------------------------------------------
def basis(N):
    K = 2 * N + 1
    UE = np.zeros((N + 1, K)); iE = np.zeros(K, int)
    UO = np.zeros((max(N, 1), K)); iO = np.zeros(K, int)
    for k in range(N + 1):                       # a_k
        UE[k, k] = 0.5; iE[k] = k
        if k >= 1:
            UO[k - 1, k] = 0.5; iO[k] = k - 1
    for k in range(1, N + 1):                    # b_k
        c = N + k
        iE[c] = k; iO[c] = k - 1
        UE[0, c] = np.sqrt(2) / k
        UE[k, c] = 0.5 / k
        UO[k - 1, c] = -0.5 / k
        for j in range(1, N + 1):
            if j != k:
                UE[j, c] = 1.0 / (k - j) + 1.0 / (k + j)
                UO[j - 1, c] = 1.0 / (k - j) - 1.0 / (k + j)
    return (UE, iE), (UO, iO)


class Assembly:
    def __init__(self, N):
        self.N = N
        (self.UE, self.iE), (self.UO, self.iO) = basis(N)
        K = 2 * N + 1
        self.SE = np.zeros((K, N + 1)); self.SE[np.arange(K), self.iE] = 1
        self.SO = np.zeros((K, max(N, 1))); self.SO[np.arange(K), self.iO] = 1

    def K(self, m):
        C = (self.UE * m[None, :]) @ self.SE; E = C + C.T
        C = (self.UO * m[None, :]) @ self.SO; O = C + C.T
        return E, O

    def co(self, YE, YO):
        """adjoint: (tr(B_k Y))_k for symmetric Y = (YE, YO)."""
        return 2 * np.einsum('jk,jk->k', self.UE, YE[:, self.iE]) + 2 * np.einsum('jk,jk->k', self.UO, YO[:, self.iO])

    @staticmethod
    def _G(U, idx, X, W):
        XU = X @ U; WU = W @ U
        UXU = U.T @ XU; UWU = U.T @ WU
        XUi = XU[idx, :]; WUi = WU[idx, :]
        return (XUi * WUi.T + X[np.ix_(idx, idx)] * UWU.T + UXU * W[np.ix_(idx, idx)].T + XUi.T * WUi)

    def G(self, XE, WE, XO, WO):
        """G_kl = sum_blocks tr(B_k X B_l W)."""
        return self._G(self.UE, self.iE, XE, WE) + self._G(self.UO, self.iO, XO, WO)


# ---------------------------------------------------------------------------------------------------------
# float64 primal-dual interior point method for  max s  s.t.  H0 + K(Phi^T w) - s I >= 0,  w >= 0
# dual: min tr(Z H0), Z >= 0, tr Z = 1, tr(Z T_j) <= 0
# ---------------------------------------------------------------------------------------------------------
def _sym(A):
    return 0.5 * (A + A.T)


def _inv_pd(S):
    c = cho_factor(S, lower=True)
    return cho_solve(c, np.eye(S.shape[0]))


def _step_psd(X, dX, gamma):
    try:
        Lc = np.linalg.cholesky(X)
    except np.linalg.LinAlgError:
        return 0.0
    Li = np.linalg.solve(Lc, np.eye(X.shape[0]))
    ev = np.linalg.eigvalsh(_sym(Li @ dX @ Li.T))
    lo = ev[0]
    return 1.0 if lo >= 0 else min(1.0, -gamma / lo)


def _step_lp(x, dx, gamma):
    neg = dx < 0
    if not neg.any():
        return 1.0
    return min(1.0, gamma * np.min(-x[neg] / dx[neg]))


def float_bounds(P, w, XE, XO):
    """float lower bound lambda_min(H(w)) and float upper bound from Z = X (repaired, normalised)."""
    m = P['Phi'].T @ w
    E, O = P['asm'].K(m)
    E = E + P['E0']; O = O + P['O0']
    lb = min(np.linalg.eigvalsh(E)[0], np.linalg.eigvalsh(O)[0])
    co = P['asm'].co(_sym(XE), _sym(XO))
    q = P['Phi'] @ co
    rho = max(0.0, np.max(q / (2 * (1 - P['ts']))))
    cost = co @ P['m0'] + rho * P['m0'][0]
    ub = cost / (np.trace(XE) + np.trace(XO) + rho)
    return lb, ub


def ipm(P, maxit=200, verbose=False, mu_hand=1e-9):
    asm, Phi = P['asm'], P['Phi']
    E0, O0 = P['E0'], P['O0']
    J = Phi.shape[0]; nE = E0.shape[0]; nO = O0.shape[0]
    nu = nE + nO + J
    w = np.full(J, 1.0 / J)
    mw = Phi.T @ w
    Ew, Ow = asm.K(mw)
    s = min(np.linalg.eigvalsh(E0 + Ew)[0], np.linalg.eigvalsh(O0 + Ow)[0]) - 1.0
    XE = np.eye(nE) / (nE + nO); XO = np.eye(nO) / (nE + nO); x = np.full(J, 1.0 / (nE + nO))
    best_lb = (-np.inf, None); best_ub = (np.inf, None)
    stall = 0
    hist = []
    hand = None; last = None
    for it in range(maxit):
        mw = Phi.T @ w
        Ew, Ow = asm.K(mw)
        SE = E0 + Ew - s * np.eye(nE); SO = O0 + Ow - s * np.eye(nO)
        # float bounds on this iterate
        try:
            lb, ub = float_bounds(P, w, XE, XO)
            if lb > best_lb[0]:
                best_lb = (lb, w.copy())
            if ub < best_ub[0]:
                best_ub = (ub, (XE.copy(), XO.copy()))
        except Exception:
            pass
        mu = (np.sum(XE * SE) + np.sum(XO * SO) + x @ w) / nu
        if hand is None and mu < mu_hand:
            hand = (w.copy(), s, XE.copy(), XO.copy(), x.copy(), mu)
        last = (w.copy(), s, XE.copy(), XO.copy(), x.copy(), mu)
        coX = asm.co(XE, XO)
        Ap = np.concatenate([-(Phi @ coX) - x, [np.trace(XE) + np.trace(XO)]])
        b = np.zeros(J + 1); b[-1] = 1.0
        Rp = b - Ap
        gap_rel = (best_ub[0] - best_lb[0]) / max(1e-300, abs(best_ub[0]) + abs(best_lb[0]))
        hist.append((it, mu, np.linalg.norm(Rp), best_lb[0], best_ub[0]))
        if verbose:
            print(f'it {it:3d} mu {mu:.3e} |Rp| {np.linalg.norm(Rp):.2e} lb {best_lb[0]:.12e} ub {best_ub[0]:.12e}')
        if best_ub[0] - best_lb[0] < 1e-15 * max(1.0, abs(best_lb[0])) or mu < 1e-22:
            break
        try:
            WE = _inv_pd(SE); WO = _inv_pd(SO)
        except LinAlgError:
            break
        G = asm.G(XE, WE, XO, WO)
        gs = asm.co(_sym(XE @ WE), _sym(XO @ WO))
        M = np.empty((J + 1, J + 1))
        M[:J, :J] = Phi @ G @ Phi.T + np.diag(x / w)
        M[:J, J] = M[J, :J] = -(Phi @ gs)
        M[J, J] = np.sum(XE * WE.T) + np.sum(XO * WO.T)
        M = _sym(M)
        try:
            cM = cho_factor(M, lower=True)
            solve = lambda r: cho_solve(cM, r)
        except LinAlgError:
            Mp = np.linalg.pinv(M, rcond=1e-15)
            solve = lambda r: Mp @ r

        def Aop(YE, YO, yL):
            return np.concatenate([-(Phi @ asm.co(_sym(YE), _sym(YO))) - yL, [np.trace(YE) + np.trace(YO)]])

        def direction(sigma, corr):
            CE, CO, CL = corr
            # M dy = Rp - A(sigma mu W - X - C)   (then Delta X below satisfies A(Delta X) = Rp); 3 refinement sweeps
            rhs = Rp - Aop(sigma * mu * WE - XE - CE, sigma * mu * WO - XO - CO, sigma * mu / w - x - CL)
            dy = solve(rhs)
            for _ in range(3):
                dw = dy[:J]; ds = dy[J]
                dE, dO = asm.K(Phi.T @ dw)
                dSE = dE - ds * np.eye(nE); dSO = dO - ds * np.eye(nO); dSL = dw
                dXE = sigma * mu * WE - XE - _sym(XE @ dSE @ WE) - _sym(CE)
                dXO = sigma * mu * WO - XO - _sym(XO @ dSO @ WO) - _sym(CO)
                dxL = sigma * mu / w - x - x * dSL / w - CL
                res = Rp - Aop(dXE, dXO, dxL)
                if np.linalg.norm(res) < 1e-15 * (1 + np.linalg.norm(Rp)):
                    break
                dy = dy + solve(res)
            return dw, ds, dSE, dSO, dSL, dXE, dXO, dxL
        zE = np.zeros_like(XE); zO = np.zeros_like(XO); zL = np.zeros(J)
        # predictor
        dw, ds, dSE, dSO, dSL, dXE, dXO, dxL = direction(0.0, (zE, zO, zL))
        ap = min(_step_psd(XE, dXE, 1.0), _step_psd(XO, dXO, 1.0), _step_lp(x, dxL, 1.0))
        ad = min(_step_psd(SE, dSE, 1.0), _step_psd(SO, dSO, 1.0), _step_lp(w, dSL, 1.0))
        mu_a = (np.sum((XE + ap * dXE) * (SE + ad * dSE)) + np.sum((XO + ap * dXO) * (SO + ad * dSO))
                + (x + ap * dxL) @ (w + ad * dSL)) / nu
        sigma = min(1.0, max(0.0, (mu_a / mu) ** 3))
        # corrector (Mehrotra): Delta X = sigma mu W - X - sym(X dS W) - sym(dXa dSa W)
        corr = (dXE @ dSE @ WE, dXO @ dSO @ WO, dxL * dSL / w)
        dw, ds, dSE, dSO, dSL, dXE, dXO, dxL = direction(sigma, corr)
        gamma = 0.98
        ap = min(_step_psd(XE, dXE, gamma), _step_psd(XO, dXO, gamma), _step_lp(x, dxL, gamma))
        ad = min(_step_psd(SE, dSE, gamma), _step_psd(SO, dSO, gamma), _step_lp(w, dSL, gamma))
        if ap < 1e-10 and ad < 1e-10:
            stall += 1
            if stall > 3:
                break
        XE = _sym(XE + ap * dXE); XO = _sym(XO + ap * dXO); x = x + ap * dxL
        w = w + ad * dw; s = s + ad * ds
    return dict(lb=best_lb[0], w=best_lb[1], ub=best_ub[0], X=best_ub[1], iters=it + 1, hist=hist,
                hand=hand if hand is not None else last)


def make_problem(x, N, ts, variant='true'):
    a, b = h0_data(x, N, variant, dps=40)
    af = np.array([float(v) for v in a]); bf = np.array([float(v) for v in b])
    E0, O0 = blocks_np(af, bf, N)
    asm = Assembly(N)
    ts = np.asarray(ts, float)
    Phi = phi_np(N, ts)
    m0 = np.concatenate([af, bf[1:]])
    return dict(x=x, N=N, ts=ts, E0=E0, O0=O0, asm=asm, Phi=Phi, m0=m0, variant=variant)




# ---------------------------------------------------------------------------------------------------------
# multiprecision linear algebra on numpy object arrays of mpf (mp.fdot inner products)
# ---------------------------------------------------------------------------------------------------------
def mzeros(n, m):
    Z = np.empty((n, m), dtype=object)
    Z[:, :] = mp.mpf(0)
    return Z


def meye(n):
    Z = mzeros(n, n)
    for i in range(n):
        Z[i, i] = mp.mpf(1)
    return Z


def _fixed_rows(rows):
    """exact block-floating-point form of a list of mpf rows: (list of ints, common exponent) per row."""
    out = []
    for row in rows:
        tups = [v._mpf_ for v in row]
        es = [t[2] for t in tups if t[1]]
        if not es:
            out.append(([0] * len(row), 0))
            continue
        E = min(es)
        out.append(([(-(t[1] << (t[2] - E)) if t[0] else (t[1] << (t[2] - E))) if t[1] else 0 for t in tups], E))
    return out


def _mk(total, e):
    return mp.mp.make_mpf(from_man_exp(total, e, mp.mp.prec, round_nearest))


def mmul(A, B):
    """matrix product with exact integer inner products (math.sumprod) and one rounding per entry."""
    Ar = _fixed_rows(A.tolist()); Bc = _fixed_rows(B.T.tolist())
    return np.array([[_mk(sumprod(ai, bj), Ea + Eb) for bj, Eb in Bc] for ai, Ea in Ar],
                    dtype=object).reshape(A.shape[0], B.shape[1])


def mmv(A, v):
    vl = list(v)
    return np.array([mp.fdot(a, vl) for a in A.tolist()], dtype=object)


def msym(A):
    return (A + A.T) * mp.mpf('0.5')


def mtr(A):
    return mp.fsum(A[i, i] for i in range(A.shape[0]))


def minner(A, B):
    return mp.fdot(A.ravel().tolist(), B.ravel().tolist())


def mchol(A):
    """lower Cholesky factor as list of lists, or None if a pivot is not positive."""
    n = A.shape[0]; Al = A.tolist(); L = [[mp.mpf(0)] * n for _ in range(n)]
    for j in range(n):
        Lj = L[j]; pre = Lj[:j]
        d2 = Al[j][j] - mp.fdot(pre, pre)
        if not d2 > 0:
            return None
        d = mp.sqrt(d2); Lj[j] = d
        for i in range(j + 1, n):
            Li = L[i]
            Li[j] = (Al[i][j] - mp.fdot(Li[:j], pre)) / d
    return L


def tri_inv(L):
    n = len(L); Inv = [[mp.mpf(0)] * n for _ in range(n)]
    for j in range(n):
        col = [mp.mpf(0)] * n
        col[j] = 1 / L[j][j]
        for i in range(j + 1, n):
            col[i] = -mp.fdot(L[i][j:i], col[j:i]) / L[i][i]
        for i in range(j, n):
            Inv[i][j] = col[i]
    return np.array(Inv, dtype=object)


def chol_solve(L, r):
    n = len(L); y = [mp.mpf(0)] * n
    for i in range(n):
        y[i] = (r[i] - mp.fdot(L[i][:i], y[:i])) / L[i][i]
    z = [mp.mpf(0)] * n
    for i in range(n - 1, -1, -1):
        z[i] = (y[i] - mp.fsum(L[k][i] * z[k] for k in range(i + 1, n))) / L[i][i]
    return np.array(z, dtype=object)


def to_float(A):
    return np.array([[float(v) for v in row] for row in A.tolist()])


def basis_mp(N):
    K = 2 * N + 1
    UE = mzeros(N + 1, K); UO = mzeros(N, K)
    (_, iE), (_, iO) = basis(N)
    half = mp.mpf(1) / 2
    for k in range(N + 1):
        UE[k, k] = half
        if k >= 1:
            UO[k - 1, k] = half
    for k in range(1, N + 1):
        c = N + k
        UE[0, c] = mp.sqrt(2) / k; UE[k, c] = half / k; UO[k - 1, c] = -half / k
        for j in range(1, N + 1):
            if j != k:
                UE[j, c] = mp.mpf(1) / (k - j) + mp.mpf(1) / (k + j)
                UO[j - 1, c] = mp.mpf(1) / (k - j) - mp.mpf(1) / (k + j)
    return UE, iE, list(range(N + 1)), UO, iO, list(range(1, N + 1)), list(range(N + 1, K))


class AssemblyMP:
    def __init__(self, N):
        self.N = N
        self.UE, self.iE, self.aE, self.UO, self.iO, self.aO, self.bc = basis_mp(N)
        self.half = mp.mpf(1) / 2

    def K(self, m):
        N = self.N
        E, O = blocks(list(m[:N + 1]), [mp.mpf(0)] + list(m[N + 1:]), N)
        return np.array(E.tolist(), dtype=object), np.array(O.tolist(), dtype=object)

    def co(self, YE, YO):
        """(tr(B_k Y))_k for symmetric Y."""
        N = self.N; out = [None] * (2 * N + 1)
        for k in range(N + 1):
            out[k] = YE[k, k] + (YO[k - 1, k - 1] if k >= 1 else mp.mpf(0))
        for k in range(1, N + 1):
            c = N + k
            out[c] = 2 * mp.fdot(self.UE[:, c].tolist(), YE[:, k].tolist()) + 2 * mp.fdot(self.UO[:, c].tolist(), YO[:, k - 1].tolist())
        return np.array(out, dtype=object)

    def _G(self, U, idx, acols, X, W):
        n, K = U.shape; bc = self.bc; Ub = U[:, bc]; half = self.half

        def XU_of(Y):
            R = mzeros(n, K)
            for k in acols:
                R[:, k] = Y[:, idx[k]] * half
            R[:, bc] = mmul(Y, Ub)
            return R

        def UtY(Y):
            # U^T X U is symmetric: a-rows from Y directly, (b, a) block by symmetry, (b, b) block upper half only
            R = mzeros(K, K)
            for k in acols:
                R[k, :] = Y[idx[k], :] * half
            R[np.ix_(bc, acols)] = R[np.ix_(acols, bc)].T
            Ur = _fixed_rows(Ub.T.tolist()); Yc = _fixed_rows(Y[:, bc].T.tolist())
            for i in range(len(bc)):
                ui, Eu = Ur[i]
                for j in range(i, len(bc)):
                    v = _mk(sumprod(ui, Yc[j][0]), Eu + Yc[j][1])
                    R[bc[i], bc[j]] = v; R[bc[j], bc[i]] = v
            return R
        XU = XU_of(X); WU = XU_of(W)
        UXU = UtY(XU); UWU = UtY(WU)
        XUi = XU[idx, :]; WUi = WU[idx, :]
        Xii = X[np.ix_(idx, idx)]; Wii = W[np.ix_(idx, idx)]
        return XUi * WUi.T + Xii * UWU.T + UXU * Wii.T + XUi.T * WUi

    def G(self, XE, WE, XO, WO):
        return self._G(self.UE, self.iE, self.aE, XE, WE) + self._G(self.UO, self.iO, self.aO, XO, WO)


def phi_mp_rows(N, ts):
    return np.array([phi(N, mp.mpf(float(t))) for t in ts], dtype=object)


def _congruence_lower(Li, dX):
    """P = Li dX Li^T for lower-triangular Li, symmetric dX; float result (exact integer inner products)."""
    n = dX.shape[0]
    Lr = _fixed_rows(Li.tolist() if isinstance(Li, np.ndarray) else Li)
    Dc = _fixed_rows(dX.T.tolist())
    A = [[_mk(sumprod(Lr[i][0][:i + 1], Dc[j][0][:i + 1]), Lr[i][1] + Dc[j][1]) for j in range(n)] for i in range(n)]
    Ar = _fixed_rows(A)
    P = np.zeros((n, n))
    for i in range(n):
        ai, Ea = Ar[i]
        for j in range(i, n):
            v = float(_mk(sumprod(ai[:j + 1], Lr[j][0][:j + 1]), Ea + Lr[j][1]))
            P[i, j] = v; P[j, i] = v
    return P


def _alpha_mp(Li, dX, gamma):
    """largest step (<= 1, times gamma) keeping X + a dX PD (X = L L^T, Li = L^-1), from the float spectrum
    of the well-scaled matrix L^-1 dX L^-T; the step is re-verified by mp Cholesky before acceptance."""
    lo = np.linalg.eigvalsh(_congruence_lower(Li, dX))[0]
    return 1.0 if lo >= 0 else min(1.0, gamma / (-lo))


def ipm_mp(x, N, variant, tsS, st0, dps=50, maxit=90, mu_stop=1e-26):
    """IPM of the same problem restricted to grid points tsS, in mpmath at dps, warm-started from the float state
    st0 = (w, s, XE, XO, xL) restricted to tsS."""
    with mp.workdps(dps):
        a0, b0 = h0_data(x, N, variant, dps)
        E0, O0 = blocks(a0, b0, N)
        E0 = np.array(E0.tolist(), dtype=object); O0 = np.array(O0.tolist(), dtype=object)
        asm = AssemblyMP(N)
        Phi = phi_mp_rows(N, tsS); PhiT = Phi.T
        J = len(tsS); nE = N + 1; nO = N; nu = nE + nO + J
        IE = meye(nE); IO = meye(nO)
        w0, s0, XE0, XO0, x0 = st0
        w = np.array([mp.mpf(float(max(v, 1e-12))) for v in w0], dtype=object)
        xL = np.array([mp.mpf(float(max(v, 1e-12))) for v in x0], dtype=object)
        XE = np.array([[mp.mpf(float(v)) for v in r] for r in XE0], dtype=object)
        XO = np.array([[mp.mpf(float(v)) for v in r] for r in XO0], dtype=object)
        for X in (XE, XO):
            while mchol(X) is None:
                X += meye(X.shape[0]) * mp.mpf('1e-14')
        KE, KO = asm.K(mmv(PhiT, w))
        Hf = [to_float(E0 + KE), to_float(O0 + KO)]
        s = mp.mpf(min(np.linalg.eigvalsh(H)[0] for H in Hf)) - mp.mpf('1e-11')
        while mchol(E0 + KE - s * IE) is None or mchol(O0 + KO - s * IO) is None:
            s -= mp.mpf('1e-9')
        b = np.array([mp.mpf(0)] * J + [mp.mpf(1)], dtype=object)

        def Aop(YE, YO, yL):
            co = asm.co(msym(YE), msym(YO))
            return np.concatenate([-mmv(Phi, co) - yL, np.array([mtr(YE) + mtr(YO)], dtype=object)])
        hist = []
        for it in range(maxit):
            KE, KO = asm.K(mmv(PhiT, w))
            SE = E0 + KE - s * IE; SO = O0 + KO - s * IO
            mu = (minner(XE, SE) + minner(XO, SO) + mp.fdot(list(xL), list(w))) / nu
            Rp = b - Aop(XE, XO, xL)
            rp = mp.sqrt(mp.fdot(list(Rp), list(Rp)))
            hist.append((it, mu, rp, s))
            if mu < mu_stop and rp < mu_stop:
                break
            LSE = mchol(SE); LSO = mchol(SO)
            if LSE is None or LSO is None:
                break
            LiE = tri_inv(LSE); LiO = tri_inv(LSO)
            WE = mmul(LiE.T, LiE); WO = mmul(LiO.T, LiO)
            LXE = mchol(XE); LXO = mchol(XO)
            if LXE is None or LXO is None:
                break
            LiXE = tri_inv(LXE); LiXO = tri_inv(LXO)
            G = asm.G(XE, WE, XO, WO)
            XWE = mmul(XE, WE); XWO = mmul(XO, WO)
            gs = asm.co(msym(XWE), msym(XWO))
            PG = mmul(Phi, G)
            M = mzeros(J + 1, J + 1)
            M[:J, :J] = mmul(PG, PhiT)
            for j in range(J):
                M[j, j] += xL[j] / w[j]
            v = -mmv(Phi, gs)
            M[:J, J] = v; M[J, :J] = v
            M[J, J] = mtr(XWE) + mtr(XWO)
            M = msym(M)
            LM = mchol(M)
            if LM is None:
                break

            def direction(sigma, corr):
                CE, CO, CL = corr
                smu = sigma * mu
                rhs = Rp - Aop(smu * WE - XE - CE, smu * WO - XO - CO, np.array([smu / wj for wj in w], dtype=object) - xL - CL)
                dy = chol_solve(LM, list(rhs))
                dw = dy[:J]; ds = dy[J]
                dKE, dKO = asm.K(mmv(PhiT, dw))
                dSE = dKE - ds * IE; dSO = dKO - ds * IO
                dXE = smu * WE - XE - msym(mmul(mmul(XE, dSE), WE)) - msym(CE)
                dXO = smu * WO - XO - msym(mmul(mmul(XO, dSO), WO)) - msym(CO)
                dxL = np.array([smu / w[j] - xL[j] - xL[j] * dw[j] / w[j] - CL[j] for j in range(J)], dtype=object)
                return dw, ds, dSE, dSO, dXE, dXO, dxL

            def lp_alpha(v, dv, gamma):
                a = 1.0
                for vi, dvi in zip(v, dv):
                    if dvi < 0:
                        a = min(a, gamma * float(-vi / dvi))
                return a
            zE = mzeros(nE, nE); zO = mzeros(nO, nO); zL = np.array([mp.mpf(0)] * J, dtype=object)
            dw, ds, dSE, dSO, dXE, dXO, dxL = direction(mp.mpf(0), (zE, zO, zL))
            ap = min(_alpha_mp(LiXE, dXE, 1.0), _alpha_mp(LiXO, dXO, 1.0), lp_alpha(xL, dxL, 1.0))
            ad = min(_alpha_mp(LiE, dSE, 1.0), _alpha_mp(LiO, dSO, 1.0), lp_alpha(w, dw, 1.0))
            ap_ = mp.mpf(ap); ad_ = mp.mpf(ad)
            mu_a = (minner(XE + ap_ * dXE, SE + ad_ * dSE) + minner(XO + ap_ * dXO, SO + ad_ * dSO)
                    + mp.fdot(list(xL + ap_ * dxL), list(w + ad_ * dw))) / nu
            sigma = min(mp.mpf(1), max(mp.mpf(0), (mu_a / mu) ** 3))
            corr = (mmul(mmul(dXE, dSE), WE), mmul(mmul(dXO, dSO), WO), np.array([dxL[j] * dw[j] / w[j] for j in range(J)], dtype=object))
            dw, ds, dSE, dSO, dXE, dXO, dxL = direction(sigma, corr)
            gamma = 0.95
            ap = min(_alpha_mp(LiXE, dXE, gamma), _alpha_mp(LiXO, dXO, gamma), lp_alpha(xL, dxL, gamma))
            ad = min(_alpha_mp(LiE, dSE, gamma), _alpha_mp(LiO, dSO, gamma), lp_alpha(w, dw, gamma))
            for _ in range(30):              # backtrack until all new blocks are PD (verified in mp)
                ap_ = mp.mpf(ap); ad_ = mp.mpf(ad)
                nXE = msym(XE + ap_ * dXE); nXO = msym(XO + ap_ * dXO); nxL = xL + ap_ * dxL
                nw = w + ad_ * dw; ns = s + ad_ * ds
                nKE, nKO = asm.K(mmv(PhiT, nw))
                ok = (mchol(nXE) is not None and mchol(nXO) is not None and all(v > 0 for v in nxL) and all(v > 0 for v in nw)
                      and mchol(E0 + nKE - ns * IE) is not None and mchol(O0 + nKO - ns * IO) is not None)
                if ok:
                    break
                ap *= 0.7; ad *= 0.7
            if not ok:
                break
            XE, XO, xL, w, s = nXE, nXO, nxL, nw, ns
        return dict(w=w, s=s, XE=XE, XO=XO, xL=xL, mu=mu, rp=rp, iters=it + 1, hist=hist)


# ---------------------------------------------------------------------------------------------------------
# data error: reviewer's mp (a0_n, b0_n) against zst's balls (pole + archimedean = prime cutoff 1)
# ---------------------------------------------------------------------------------------------------------
ZST_C = r"""
#include <stdio.h>
#include <stdlib.h>
#include "zst.h"
int main(int argc, char **argv)
{
    ulong X = strtoul(argv[1], 0, 10); slong N = atol(argv[2]); slong prec = atol(argv[3]);
    ulong XP = strtoul(argv[4], 0, 10);
    arb_t x; arb_ptr a = _arb_vec_init(N + 1), b = _arb_vec_init(N + 1); slong n;
    arb_init(x); arb_set_ui(x, X);
    zst_riemann_ab(a, b, N, x, XP, prec);
    for (n = 0; n <= N; n++) {
        flint_printf("%wd ", n);
        arb_printn(a + n, 110, ARB_STR_NO_RADIUS); flint_printf(" "); mag_printd(arb_radref(a + n), 3); flint_printf(" ");
        arb_printn(b + n, 110, ARB_STR_NO_RADIUS); flint_printf(" "); mag_printd(arb_radref(b + n), 3); flint_printf("\n");
    }
    _arb_vec_clear(a, N + 1); _arb_vec_clear(b, N + 1); arb_clear(x);
    return 0;
}
"""


def zst_crosscheck(x, N):
    """max over n <= N of |certificate data (a0_n, b0_n) at DPS digits - zst midpoint| + zst radius
    (pole + archimedean data, prime cutoff 1), or None."""
    zdir = os.path.join(REPO, 'zst'); lib = os.path.join(zdir, 'build', 'libzst.a')
    if not os.path.exists(lib):
        return None
    with tempfile.TemporaryDirectory() as td:
        src = os.path.join(td, 'p.c'); exe = os.path.join(td, 'p')
        with open(src, 'w') as fh:
            fh.write(ZST_C)
        cp = subprocess.run(['cc', '-O2', '-I' + os.path.join(zdir, 'include'), src, lib, '-lflint', '-lmpfr', '-lgmp', '-lm',
                             '-o', exe], capture_output=True, text=True)
        if cp.returncode != 0:
            return None
        out = subprocess.run([exe, str(x), str(N), '400', '1'], capture_output=True, text=True).stdout
    with mp.workdps(DPS):
        a0, b0 = h0_data(x, N, 'true', DPS)       # exactly the data the certificates use (rounded to DPS digits)
    with mp.workdps(130):
        worst = mp.mpf(0)
        for line in out.strip().splitlines():
            t = line.split(); n = int(t[0])
            worst = max(worst, abs(a0[n] - mp.mpf(t[1])) + mp.mpf(t[2]), abs(b0[n] - mp.mpf(t[3])) + mp.mpf(t[4]))
    return worst


# ---------------------------------------------------------------------------------------------------------
# the certificate (mpmath, DPS digits, explicit rounding and data error bounds)
# ---------------------------------------------------------------------------------------------------------
def certify(x, N, variant, ts, w, s_hint, RE, RO, delta, margin0=1e-45):
    """Bracket [lb, ub] on max_{w>=0 on ts} lambda_min(H0 + T(w)).
    w: primal weights (any numbers, clipped at 0); s_hint: an estimate of lambda_min(H(w));
    Z = RE RE^T (+) RO RO^T + rho e0 e0^T: PSD by construction for any matrices RE, RO.
    delta: bound on the error of the (a0, b0) data."""
    with mp.workdps(DPS):
        eps = mp.mpf(10) ** (8 - DPS)
        a0, b0 = h0_data(x, N, variant, DPS)
        m0 = a0 + b0[1:]
        K = 2 * N + 1; J = len(ts)
        Phi = phi_mp_rows(N, ts)
        wl = [max(mp.mpf(v), mp.mpf(0)) for v in w]
        sw = mp.fsum(wl)
        # ---- primal ----
        cols = Phi.T.tolist()
        m = [mp.fdot(wl, cols[k]) for k in range(K)]
        a = [a0[n] + m[n] for n in range(N + 1)]; bb = [mp.mpf(0)] + [b0[n] + m[N + n] for n in range(1, N + 1)]
        E, O = blocks(a, bb, N)
        lbs = []
        for H in (np.array(E.tolist(), dtype=object), np.array(O.tolist(), dtype=object)):
            n = H.shape[0]
            Hmax = max(abs(v) for v in H.ravel())
            e_H = 4 * (delta + eps * (J + 2) * 2 * (sw + 1)) + eps * (Hmax + abs(mp.mpf(s_hint)) + 1)
            margin = mp.mpf(margin0) * max(1, abs(mp.mpf(s_hint)))
            s0 = None
            for _ in range(40):
                cand = mp.mpf(s_hint) - margin
                A = H - cand * meye(n)
                Lc = mchol(A)
                if Lc is not None:
                    s0 = cand
                    break
                margin *= 10
            if s0 is None:
                lbs.append(-mp.inf)
                continue
            Ln = np.array(Lc, dtype=object)
            Res = A - mmul(Ln, Ln.T)
            fro = mp.sqrt(mp.fsum(v * v for v in Res.ravel()))
            Lrow = max(mp.fdot(r, r) for r in Lc)
            fro_err = n * (n * eps * (Lrow + max(abs(v) for v in A.ravel())))
            lbs.append(s0 - fro - fro_err - n * e_H)
        lb = min(lbs)
        # ---- dual ----
        asm = AssemblyMP(N)
        Zs = []; e_Z = mp.mpf(0); trZ = mp.mpf(0)
        for R, n in ((RE, N + 1), (RO, N)):
            Rm = np.array([[mp.mpf(v) for v in row] for row in (R.tolist() if isinstance(R, np.ndarray) else R)], dtype=object)
            Z = mmul(Rm, Rm.T)
            rn = max(mp.fdot(r, r) for r in Rm.tolist())
            e_Z = max(e_Z, n * eps * rn)
            trZ += mtr(Z)
            Zs.append(Z)
        co = asm.co(msym(Zs[0]), msym(Zs[1]))
        colsum = max(mp.fsum(abs(v) for v in asm.UE[:, k]) + mp.fsum(abs(v) for v in asm.UO[:, k]) for k in range(K))
        dco = 2 * e_Z * colsum * 2 + eps * max(abs(v) for v in co)
        cl = list(co)
        phisum = 2 * (N + 1) + N
        rho = mp.mpf(0); qmax = -mp.inf
        for j in range(J):
            row = list(Phi[j])
            q = mp.fdot(row, cl)
            err = dco * phisum + eps * mp.fsum(abs(u * v) for u, v in zip(row, cl))
            qmax = max(qmax, q)
            tj = mp.mpf(float(ts[j]))
            rho = max(rho, (q + err) / (2 * (1 - tj)))
        cost = mp.fdot(cl, m0)
        cost_err = dco * mp.fsum(abs(v) for v in m0) + delta * mp.fsum(abs(v) for v in cl) + eps * mp.fsum(abs(u * v) for u, v in zip(cl, m0))
        num = cost + rho * a0[0] + cost_err + rho * delta
        tr_err = 2 * (N + 1) * e_Z
        den = (trZ + rho - tr_err) if num >= 0 else (trZ + rho + tr_err)
        ub = num / den
        return dict(lb=lb, ub=ub, rho=rho, qmax=qmax / trZ, cost=cost / trZ, trZ=trZ, dco=dco)


# ---------------------------------------------------------------------------------------------------------
# grids, clusters, comparison
# ---------------------------------------------------------------------------------------------------------
def visible_prime_powers(x):
    return [(n, np.log(n), np.log(p) / np.sqrt(n)) for n, p in prime_powers(x)]


def clusters(ts, w, hk, L, frac=SUPPORT_FRAC):
    """cores = maximal runs of support points (w > frac * total) with gaps <= 2.01 hk; every other grid point within
    2.01 hk of a core joins it (halo), the rest is stray mass.  Returns [(centroid y, mass, #core pts, core span y)],
    total mass, stray mass."""
    ts = np.asarray(ts, float); w = np.asarray(w, float)
    idx = np.argsort(ts); ts = ts[idx]; w = w[idx]
    tot = w.sum(); keep = w > frac * tot
    cores = []; cur = []
    for j in range(len(ts)):
        if not keep[j]:
            continue
        if cur and ts[j] - ts[cur[-1]] > 2.01 * hk:
            cores.append(cur); cur = []
        cur.append(j)
    if cur:
        cores.append(cur)
    members = [list(c) for c in cores]; stray = 0.0
    incore = set(j for c in cores for j in c)
    for j in range(len(ts)):
        if j in incore or w[j] <= 0:
            continue
        d = [max(ts[c[0]] - ts[j], ts[j] - ts[c[-1]], 0.0) for c in cores]
        k = int(np.argmin(d)) if d else -1
        if k >= 0 and d[k] <= 2.01 * hk:
            members[k].append(j)
        else:
            stray += w[j]
    res = []
    for c, mem in zip(cores, members):
        m = w[mem].sum()
        res.append((L * (ts[mem] * w[mem]).sum() / m, m, len(c), L * (ts[c[-1]] - ts[c[0]])))
    return res, tot, stray


def compare(x, cl):
    """COMPARISON WITH THE PRIMES: nearest visible prime power to each cluster."""
    pp = visible_prime_powers(x)
    rows = []
    for y, m, k, span in cl:
        n, ly, wt = min(pp, key=lambda r: abs(r[1] - y))
        rows.append((n, y - ly, m / wt - 1, m, k, span))
    return rows


def next_grid(base, ts, w, hk_new):
    tot = sum(w)
    sup = [t for t, wj in zip(ts, w) if wj > SUPPORT_FRAC * tot]
    new = set(base)
    for s0 in sup:
        for i in range(-8, 9):
            t = s0 + i * hk_new
            if 0 < t < 1:
                new.add(t)
    return sorted(new)


def solve_level(x, N, variant, ts, use_mp):
    """float IPM on the whole level grid; optionally mp IPM on a restricted set with column generation
    (50 digits and mu down to 1e-26 for N <= 60; 34 digits and mu down to 1e-18 for larger N, for run time)."""
    dps_ipm, mu_stop = (50, 1e-26) if N <= 60 else (34, 1e-18)
    tf = np.array([float(t) for t in ts])
    P = make_problem(x, N, tf, variant)
    r = ipm(P, mu_hand=1e-10)
    info = dict(float_lb=r['lb'], float_ub=r['ub'], float_iters=r['iters'])
    if not use_mp:
        XE, XO = r['X']
        R = []
        for X in (XE, XO):
            try:
                R.append(np.linalg.cholesky(_sym(X)))
            except np.linalg.LinAlgError:
                ev, V = np.linalg.eigh(_sym(X)); R.append(V * np.sqrt(np.clip(ev, 0, None))[None, :])
        return dict(w=list(r['w']), s=r['lb'], RE=R[0], RO=R[1], **info, mp_iters=0, cg_rounds=0, J_S=0, margin0=1e-15)
    w, s, XE, XO, xL, mu = r['hand']
    tot = w.sum(); J = len(tf)
    keep = set(np.where(w > SUPPORT_FRAC * tot)[0])
    S = set()
    for j in keep:
        S |= {max(j - 1, 0), j, min(j + 1, J - 1)}
    PhiF = None
    for rnd in range(4):
        Sl = sorted(S)
        P2 = make_problem(x, N, tf[Sl], variant)
        r2 = ipm(P2, mu_hand=1e-10)
        R = ipm_mp(x, N, variant, tf[Sl], r2['hand'][:5], dps=dps_ipm, mu_stop=mu_stop)
        with mp.workdps(dps_ipm):
            if PhiF is None:
                PhiF = phi_mp_rows(N, tf)
            asm = AssemblyMP(N)
            co = list(asm.co(R['XE'], R['XO'])); trX = mtr(R['XE']) + mtr(R['XO'])
            q = [mp.fdot(list(PhiF[j]), co) / trX for j in range(J)]
        viol = [j for j in range(J) if j not in S and q[j] > mp.mpf(mu_stop) * 1e8]
        if not viol:
            break
        for j in viol:
            S |= {max(j - 1, 0), j, min(j + 1, J - 1)}
    wf = [mp.mpf(0)] * J
    for k, j in enumerate(Sl):
        wf[j] = R['w'][k]
    with mp.workdps(dps_ipm):
        RE = np.array(mchol(R['XE']), dtype=object); RO = np.array(mchol(R['XO']), dtype=object)
    info.update(mp_iters=R['iters'], cg_rounds=rnd + 1, J_S=len(Sl), mp_mu=float(R['mu']), mp_rp=float(R['rp']),
                qmax_outside=float(max([q[j] for j in range(J) if j not in S] or [mp.mpf(-1)])))
    return dict(w=wf, s=R['s'], RE=RE, RO=RO, **info, margin0=10.0 ** (4 - dps_ipm))


def run_chain(spec):
    """one coarse-to-fine chain: spec = (tag, x, N, M, levels, variant, use_mp, delta)."""
    tag, x, N, M, levels, variant, use_mp, delta = spec
    L = float(np.log(x))
    base = [Fraction(j, M) for j in range(1, M)]
    ts = list(base); hk = Fraction(1, M)
    out = []
    for lev in range(levels + 1):
        sol = solve_level(x, N, variant, ts, use_mp)
        cert = certify(x, N, variant, ts, sol['w'], sol['s'], sol['RE'], sol['RO'], delta,
                       margin0=sol['margin0'])
        wflt = [float(v) for v in sol['w']]
        cl, tot, stray = clusters([float(t) for t in ts], wflt, float(hk), L)
        out.append(dict(level=lev, h=float(hk) * L, J=len(ts), lb=cert['lb'], ub=cert['ub'], rho=cert['rho'],
                        qmax=cert['qmax'], clusters=cl, total=tot, stray=stray, cmp=compare(x, cl),
                        t_grid=[float(t) for t in ts], w_opt=wflt,
                        **{k: v for k, v in sol.items() if k not in ('w', 's', 'RE', 'RO', 'margin0')}))
        if lev == levels:
            break
        hk = hk / 8
        ts = next_grid(base, ts, wflt, hk)
    return tag, out


# ---------------------------------------------------------------------------------------------------------
# controls and comparison values
# ---------------------------------------------------------------------------------------------------------
def signed_control(spec):
    """(ii) signed w: explicit w_c with H0 + T(w_c) = c I on the uniform grid (min-norm solution in mp)."""
    tag, x, N, M, cs, delta = spec
    ts = [Fraction(j, M) for j in range(1, M)]
    rows = []
    with mp.workdps(DPS):
        a0, b0 = h0_data(x, N, 'true', DPS)
        Phi = phi_mp_rows(N, ts)
        Gm = mp.matrix(mmul(Phi.T, Phi).tolist())
        K = 2 * N + 1
        for c in cs:
            c = mp.mpf(c)
            target = [c - a0[n] for n in range(N + 1)] + [-b0[n] for n in range(1, N + 1)]
            z = mp.lu_solve(Gm, mp.matrix(target))
            w = mmv(Phi, [z[k] for k in range(K)])
            m = mmv(Phi.T, w)
            res = max(abs(m[k] - target[k]) for k in range(K))
            a = [a0[n] + m[n] for n in range(N + 1)]; bb = [mp.mpf(0)] + [b0[n] + m[N + n] for n in range(1, N + 1)]
            E, O = blocks(a, bb, N)
            dev = max(max(abs(E[i, j] - (c if i == j else 0)) for i in range(N + 1) for j in range(N + 1)),
                      max(abs(O[i, j] - (c if i == j else 0)) for i in range(N) for j in range(N)))
            lam_lb = c - (N + 1) * (dev + 8 * delta)
            wf = np.array([float(v) for v in w])
            rows.append((float(c), lam_lb, float(np.abs(wf).sum()), float(wf.sum()), float(wf.min()), float(wf.max()),
                         int((wf < 0).sum()), float(res)))
    return tag, rows


def truth_lambda(spec):
    """COMPARISON WITH THE PRIMES: lambda_min of the true form (pole + arch + primes) at x, N (no zeros)."""
    tag, x, N, dps = spec
    with mp.workdps(dps):
        a0, b0 = ab0(x, N)
        a = list(a0); b = list(b0)
        L = mp.log(x)
        for n, p in prime_powers(x):
            f = phi(N, mp.log(n) / L); wt = mp.log(p) / mp.sqrt(n)
            for k in range(N + 1):
                a[k] += wt * f[k]
            for k in range(1, N + 1):
                b[k] += wt * f[N + k]
        E, O = blocks(a, b, N)
        le = min(mp.eigsy(E, eigvals_only=True)); lo = min(mp.eigsy(O, eigvals_only=True))
        return tag, (le, lo)


def dispatch(task):
    kind = task[0]
    if kind == 'chain':
        return run_chain(task[1])
    if kind == 'signed':
        return signed_control(task[1])
    if kind == 'truth':
        return truth_lambda(task[1])
    raise ValueError(kind)


# ---------------------------------------------------------------------------------------------------------
# reporting
# ---------------------------------------------------------------------------------------------------------
def e(v, d=3):
    return mp.nstr(mp.mpf(v), d, min_fixed=1, max_fixed=0) if v is not None else 'None'


def print_chain(tag, x, out):
    for o in out:
        tau_lo, tau_hi = -o['ub'], -o['lb']
        rel = (o['ub'] - o['lb']) / abs(o['lb']) if o['lb'] != 0 else mp.inf
        print(f"  [{tag}] level {o['level']}: h = {o['h']:.4e}, grid {o['J']} pts; max lambda_min in "
              f"[{e(o['lb'], 12)}, {e(o['ub'], 12)}] (rel. width {e(rel, 2)}); tau* in [{e(tau_lo, 10)}, {e(tau_hi, 10)}]; "
              f"repair rho = {e(o['rho'], 2)}; mp IPM iters {o['mp_iters']}, col.gen rounds {o['cg_rounds']}, |S| {o['J_S']}; "
              f"{len(o['clusters'])} clusters, total mass {o['total']:.10f}, stray mass {o['stray']:.2e}")
        for n, dy, dm, m, k, span in o['cmp']:
            print(f"      COMPARISON n = {n:2d}: centroid - log n = {dy:+.3e}, mass/(Lambda(n)/sqrt n) - 1 = {dm:+.3e}, "
                  f"mass {m:.8f}, {k} pts, span {span:.2e}")


def errs(o, exclude=()):
    rows = [r for r in o['cmp'] if r[0] not in exclude]
    return (max(abs(r[1]) for r in rows) if rows else float('nan'), max(abs(r[2]) for r in rows) if rows else float('nan'))


def per_atom(o, n):
    r = [row for row in o['cmp'] if row[0] == n]
    return r[0] if len(r) == 1 else None


def main():
    head('rtp2_blind_recovery.py -- claude:opus; RTP round 2, blind-recovery lane; no zeros of zeta anywhere '
         '(the only comparison is with log n and Lambda(n)/sqrt n, labelled); deterministic')
    print(f"  float IPM (HKM, Mehrotra) + mp IPM at 50 digits on a restricted set with column generation; certificate at {DPS} digits")
    print(f"  support threshold {SUPPORT_FRAC} of the total mass; refinement: level-0 uniform grid UNION 17-point patches at h/8^k")

    head('1. Data and assembly self-tests (no primes enter H0)')
    d13 = zst_crosscheck(13, 60); d25 = zst_crosscheck(25, 134)
    ok = d13 is not None and d25 is not None
    check(ok, 'zst printer compiled against zst/build/libzst.a and run (pole + archimedean, prime cutoff X = 1)')
    if ok:
        check(d13 < mp.mpf(10) ** (4 - DPS) and d25 < mp.mpf(10) ** (4 - DPS),
              f'certificate data (reviewer mp (a0_n, b0_n) at {DPS} digits) = zst ball data: max |diff| + radius = {e(d13)} (x=13, n<=60), '
              f'{e(d25)} (x=25, n<=134)')
    delta = {13: 2 * (d13 if ok else mp.mpf(10) ** -60), 25: 2 * (d25 if ok else mp.mpf(10) ** -60)}
    note(f'data error bound used in the certificates: delta = {e(delta[13])} (x=13), {e(delta[25])} (x=25); controls: 3 delta + 1e-78')
    N = 20; asm = Assembly(N); rng = np.random.default_rng(20260926)
    m = rng.standard_normal(2 * N + 1)
    E, O = asm.K(m); E2, O2 = blocks_np(m[:N + 1], np.concatenate([[0], m[N + 1:]]), N)
    check(max(abs(E - E2).max(), abs(O - O2).max()) < 1e-13, 'rank-two basis assembly K(m) = reviewer blocks_np (float), N = 20')
    XE = rng.standard_normal((N + 1, N + 1)); XE = XE @ XE.T; WE = rng.standard_normal((N + 1, N + 1)); WE = WE @ WE.T
    XO = rng.standard_normal((N, N)); XO = XO @ XO.T; WO = rng.standard_normal((N, N)); WO = WO @ WO.T
    Bs = [asm.K(np.eye(2 * N + 1)[k]) for k in range(2 * N + 1)]
    Gb = np.array([[np.trace(Bk[0] @ XE @ Bl[0] @ WE) + np.trace(Bk[1] @ XO @ Bl[1] @ WO) for Bl in Bs] for Bk in Bs])
    cob = np.array([np.trace(Bk[0] @ XE) + np.trace(Bk[1] @ XO) for Bk in Bs])
    check(abs(asm.G(XE, WE, XO, WO) - Gb).max() < 1e-12 * abs(Gb).max() and abs(asm.co(XE, XO) - cob).max() < 1e-12 * abs(cob).max(),
          'Schur kernel G_kl = tr(B_k X B_l W) and adjoint co(X) = (tr B_k X)_k agree with brute force (float)')
    with mp.workdps(30):
        am = AssemblyMP(N)
        Gm = am.G(*(np.array([[mp.mpf(float(v)) for v in r] for r in A], dtype=object) for A in (XE, WE, XO, WO)))
        com = am.co(*(np.array([[mp.mpf(float(v)) for v in r] for r in A], dtype=object) for A in (XE, XO)))
    check(abs(to_float(Gm) - Gb).max() < 1e-12 * abs(Gb).max() and max(abs(float(com[k]) - cob[k]) for k in range(2 * N + 1)) < 1e-10,
          'mp Schur kernel and mp adjoint agree with the float versions')

    # ------------------------------------------------------------------ tasks
    tasks = []
    for Nc in (60, 40, 20, 10):
        for M in (256, 128, 64):
            tasks.append(('chain', (f'x13_N{Nc}_M{M}', 13, Nc, M, 3, 'true', True, delta[13])))
    tasks.insert(3, ('chain', ('x25_N134_M128', 25, 134, 128, 1, 'true', True, delta[25])))
    tasks.insert(3, ('chain', ('x25_N134_M512', 25, 134, 512, 1, 'true', True, delta[25])))
    tasks.insert(4, ('chain', ('x25_N60_M128', 25, 60, 128, 2, 'true', True, delta[25])))
    tasks.insert(5, ('truth', ('truth_N60', 13, 60, 160)))
    dc = 3 * delta[13] + mp.mpf(10) ** -78
    for var in ('pole_only', 'arch_neg', 'pole0.9', 'pole1.1'):
        tasks.append(('chain', (f'ctl_{var}_N40', 13, 40, 256, 1, var, True, dc)))
    for var in ('pole_only', 'arch_neg', 'pole0.9', 'pole1.1'):
        tasks.append(('chain', (f'ctl_{var}_N20', 13, 20, 256, 2, var, True, dc)))
    tasks.append(('truth', ('truth_N40', 13, 40, 130)))
    tasks.append(('truth', ('truth_N20', 13, 20, 100)))
    tasks.append(('truth', ('truth_N10', 13, 10, 80)))
    tasks.append(('signed', ('signed_N60', 13, 60, 256, (1, 10, 100), delta[13])))
    tasks.append(('signed', ('signed_N20', 13, 20, 256, (1, 10, 100), delta[13])))
    cache = os.environ.get('RTP2_BR_CACHE')      # development only: pickle of the raw results (not written by default)
    if cache and os.path.exists(cache):
        import pickle
        with open(cache, 'rb') as fh:
            res = pickle.load(fh)
    else:
        with Pool(min(len(tasks), 60)) as pool:
            res = dict(pool.map(dispatch, tasks, chunksize=1))
        if cache:
            import pickle
            with open(cache, 'wb') as fh:
                pickle.dump(res, fh)
    report(res)


def report(res):
    pp13 = [n for n, _, _ in visible_prime_powers(13)]
    pp25 = [n for n, _, _ in visible_prime_powers(25)]
    L13 = float(np.log(13))

    head('2. COMPARISON value (primes enter; no zeros): lambda_min of the true form at x = 13')
    truth = {}
    for Nc in (10, 20, 40, 60):
        le, lo = res[f'truth_N{Nc}']
        truth[Nc] = min(le, lo)
        print(f'  N = {Nc:2d}: lambda_min(even) = {e(le, 12)}, lambda_min(odd) = {e(lo, 12)}')
    with mp.workdps(60):
        ok20 = abs(truth[20] / mp.mpf('1.56610785511170290964964297444284186782486892548257683604779575e-39') - 1) < mp.mpf(10) ** -30
    check(ok20, f'truth lambda_min at N = 20 = {e(truth[20], 12)} agrees with lane L ball value 1.56610785511e-39 to 1e-30 relative')
    note('coercivity floor (lane L, not recomputed): eps_N at x = 13 is 3.48e-59 (N = 120), 2.85e-59 (N = 200); under RH it '
         'decreases to a positive attained mu_L')

    head('3. Blind recovery at x = 13 (pole + archimedean data only), uniform grids L/M and three refinement levels')
    for Nc in (10, 20, 40, 60):
        for M in (64, 128, 256):
            tag = f'x13_N{Nc}_M{M}'
            print(f'\n  --- {tag} ---')
            print_chain(tag, 13, res[tag])
    for Nc in (10, 20, 40, 60):
        for M in (64, 128, 256):
            tag = f'x13_N{Nc}_M{M}'; out = res[tag]
            check(all(o['lb'] <= o['ub'] for o in out), f'{tag}: certified brackets consistent (lb <= ub) at every level')
            check(all((o['ub'] - o['lb']) < mp.mpf(10) ** -12 * abs(o['lb']) for o in out),
                  f'{tag}: certified relative bracket width < 1e-12 at every level (max {e(max((o["ub"] - o["lb"]) / abs(o["lb"]) for o in out), 2)})')
            if Nc == 10:
                ol = out[-1]
                check(ol['lb'] > 0 and len(ol['clusters']) != len(pp13) and abs(ol['total'] / 4.260502 - 1) > 0.05,
                      f'{tag}: N = 10 FAILS to recover: refinement makes the grid feasible (finest max lambda_min >= {e(ol["lb"], 4)} > 0, '
                      f'truth 2.8e-26), the maximiser has {len(ol["clusters"])} clusters (not 8) and mass {ol["total"]:.4f} (truth 4.2605)')
                continue
            check(all(o['ub'] < 0 for o in out),
                  f'{tag}: every level grid certified EMPTY (ub < 0: no nonnegative measure on the grid makes the section PSD)')
            o0 = out[0]; ns = sorted(r[0] for r in o0['cmp']); dmax = max(abs(r[1]) for r in o0['cmp'])
            if M == 64:
                check(len(o0['cmp']) == 7 and 8 not in ns and dmax < 2 * o0['h'],
                      f'{tag} level 0 (h = {o0["h"]:.3e}): 7 clusters, log 8 and log 9 (2.9 h apart) merged into one; every centroid '
                      f'within {dmax / o0["h"]:.2f} h of its nearest log n')
            else:
                check(ns == pp13 and dmax < 2 * o0['h'],
                      f'{tag} level 0: one cluster at each visible prime power {ns}, nothing else; max |centroid - log n| = '
                      f'{dmax / o0["h"]:.2f} h')
            ol = out[-1]; ns = sorted(r[0] for r in ol['cmp'])
            check(ns == pp13 and ol['stray'] < 1e-6 * ol['total'],
                  f'{tag} level {ol["level"]} (h = {ol["h"]:.2e}): exactly one cluster per visible prime power, stray mass {ol["stray"]:.1e}')
    for Nc in (40, 60):
        for M in (128, 256):
            o = res[f'x13_N{Nc}_M{M}'][-1]; p, mm = errs(o, exclude=(11,)); r11 = per_atom(o, 11)
            check(p < 1e-7 and abs(r11[1]) < 5e-7 and mm < 3e-7 and abs(r11[2]) < 1e-5,
                  f'x13_N{Nc}_M{M} finest level: |centroid - log n| <= {p:.1e} (n <= 9), {abs(r11[1]):.1e} (n = 11); '
                  f'|mass/(Lambda(n)/sqrt n) - 1| <= {mm:.1e} (n <= 9), {abs(r11[2]):.1e} (n = 11)')
            out = res[f'x13_N{Nc}_M{M}']; rates = []
            for a, b in zip(out[:-1], out[1:]):
                pa, ma = errs(a, exclude=(11,)); pb, mb = errs(b, exclude=(11,))
                rates.append((np.log(float(a['lb'] / b['lb'])) / np.log(8), np.log(pa / pb) / np.log(8), np.log(ma / mb) / np.log(8)))
            check(all(1.6 < r < 2.6 for rr in rates for r in rr),
                  f'x13_N{Nc}_M{M}: tau*, position error and mass error all fall like h^p with p in [1.6, 2.6] at every refinement '
                  f'(p = ' + ', '.join(f'{a:.2f}/{b:.2f}/{c:.2f}' for a, b, c in rates) + ')')
    for M in (64, 128, 256):
        o = res[f'x13_N20_M{M}'][-1]; r11 = per_atom(o, 11)
        o40 = res[f'x13_N40_M{M}'][-1]; r11b = per_atom(o40, 11)
        check(abs(r11[2]) > 5e-4 and abs(r11[2]) > 50 * abs(r11b[2]),
              f'x13_N20_M{M} finest level: the edge atom n = 11 lags (mass error {abs(r11[2]):.1e} at N = 20 against '
              f'{abs(r11b[2]):.1e} at N = 40 on the same grid family)')
        a, b = res[f'x13_N40_M{M}'], res[f'x13_N60_M{M}']
        dev = max(abs(float(x['lb'] / y['lb']) - 1) for x, y in zip(a, b))
        check(dev < 1e-4, f'x13 M={M}: tau* at N = 40 and N = 60 agree to {dev:.1e} relative at every level (N-independent)')
    note('COMPARISON: at N = 20, 40, 60 every grid maximiser has lambda_min < 0 < lambda_min(truth) (section 2); the grid optimum '
         'approaches 0 from below like h^2 and would reach the truth scale 1e-39 .. 1e-58 only at h ~ 1e-20 .. 1e-30')

    head('4. Error tables (COMPARISON WITH THE PRIMES; uses no zeros)')
    print('  max |centroid - log n| over n in {2,...,9} / at n = 11 ; max |mass ratio - 1| over n in {2,...,9} / at n = 11')
    for Nc in (10, 20, 40, 60):
        for M in (64, 128, 256):
            tag = f'x13_N{Nc}_M{M}'; out = res[tag]
            cells = []
            for o in out:
                p, mm = errs(o, exclude=(11,)); r11 = per_atom(o, 11)
                cells.append(f"L{o['level']}: {p:.1e}/{abs(r11[1]) if r11 else float('nan'):.1e}; {mm:.1e}/{abs(r11[2]) if r11 else float('nan'):.1e}; tau {float(-o['lb']):.2e}")
            print(f'  {tag:15s} ' + ' | '.join(cells))
    print('\n  refinement rates: log_8 of the level-to-level ratio (h shrinks by 8 per level) of tau*, of max position error'
          ' (n <= 9) and of max relative mass error (n <= 9)')
    for Nc in (10, 20, 40, 60):
        for M in (64, 128, 256):
            tag = f'x13_N{Nc}_M{M}'; out = res[tag]; cells = []
            for a, b in zip(out[:-1], out[1:]):
                pa, ma = errs(a, exclude=(11,)); pb, mb = errs(b, exclude=(11,))
                ta, tb = float(-a['lb']), float(-b['lb'])
                cells.append(f"L{a['level']}->L{b['level']}: tau {np.log(ta / tb) / np.log(8):.2f}, pos {np.log(pa / pb) / np.log(8):.2f}, "
                             f"mass {np.log(ma / mb) / np.log(8):.2f}")
            print(f'  {tag:15s} ' + ' | '.join(cells))
    print('\n  per-atom errors at the finest level, grid L/256:')
    for Nc in (10, 20, 40, 60):
        o = res[f'x13_N{Nc}_M256'][-1]
        print(f'  N = {Nc:2d}, h = {o["h"]:.2e}: ' + '; '.join(f'n={r[0]}: dy {r[1]:+.2e}, dm {r[2]:+.2e}' for r in o['cmp']))

    head('5. x = 25: N = 60 (mp IPM, two refinements, grid L/128) and N = 134 (mp IPM at 34 digits, one refinement, '
         'grids L/128 and L/512)')
    for tag in ('x25_N60_M128', 'x25_N134_M128', 'x25_N134_M512'):
        print(f'\n  --- {tag} ---')
        print_chain(tag, 25, res[tag])
        out = res[tag]
        check(all(o['lb'] <= o['ub'] for o in out), f'{tag}: certified brackets consistent (lb <= ub) at every level')
        for o in out:
            n16 = [r for r in o['cmp'] if r[0] == 16]; n17 = [r for r in o['cmp'] if r[0] == 17]
            note(f'{tag} level {o["level"]}: clusters nearest to 16: {len(n16)}, to 17: {len(n17)}; '
                 f'clusters matched: {sorted(r[0] for r in o["cmp"])}; stray mass {o["stray"]:.1e}')

    def sep(o):
        c16 = [r for r in o['cmp'] if r[0] == 16 and abs(r[1]) < o['h'] and abs(r[2]) < 0.2]
        c17 = [r for r in o['cmp'] if r[0] == 17 and abs(r[1]) < o['h'] and abs(r[2]) < 0.2]
        return len(c16) == 1 and len(c17) == 1
    a = res['x25_N60_M128']
    check(not sep(a[0]) and all(sep(o) for o in a[1:]),
          'x25_N60: log 16 and log 17 (0.0606 apart) are NOT separated on L/128 (h = 0.025) but ARE separated after one and two '
          'refinements (a cluster within h of each, masses within 20%)')
    b = res['x25_N134_M512']
    check(all(sep(o) for o in b), 'x25_N134 on L/512 (h = 0.0063): log 16 and log 17 separated at level 0 and level 1')
    c = res['x25_N134_M128']
    check(-c[0]['ub'] > 0.2, f'x25_N134 on L/128: under-resolved (h = 0.025 > L/(2N+1) = 0.012): tau* >= {e(-c[0]["ub"], 4)}, '
          f'{len(c[0]["clusters"])} clusters at level 0')
    ob = b[-1]; others = [r for r in ob['cmp'] if r[0] not in (5, 16)]
    note(f'x25_N134_M512 level 1: max |centroid - log n| = {max(abs(r[1]) for r in others):.1e}, max |mass ratio - 1| = '
         f'{max(abs(r[2]) for r in others):.1e} over n not in (5, 16); n = 16: {per_atom(ob, 16)[1]:+.1e} / {per_atom(ob, 16)[2]:+.1e}; '
         f'n = 5 (log 5 = L/2 on the grid): {per_atom(ob, 5)[1]:+.1e} / {per_atom(ob, 5)[2]:+.1e}')

    head('6. Controls at x = 13, grid L/256')
    for var in ('pole_only', 'arch_neg', 'pole0.9', 'pole1.1'):
        for Nc in (20, 40):
            tag = f'ctl_{var}_N{Nc}'
            print(f'\n  --- {tag} ---')
            print_chain(tag, 13, res[tag])
            out = res[tag]; ol = out[-1]; dmax = max(abs(r[1]) for r in ol['cmp']); mmax = max(abs(r[2]) for r in ol['cmp'])
            check(all(o['lb'] <= o['ub'] for o in out), f'{tag}: certified brackets consistent at every level')
            if var in ('pole_only', 'pole1.1'):
                check(ol['lb'] > 0.1 and dmax > 0.01,
                      f'{tag}: the grid is FEASIBLE with a large margin (max lambda_min >= {e(ol["lb"], 4)}); the maximiser has '
                      f'{len(ol["clusters"])} clusters, max |centroid - nearest log n| = {dmax:.3f}, max mass error {mmax:.2f}: no recovery')
            else:
                check(ol['ub'] < -0.1 and dmax > 0.01,
                      f'{tag}: the grid is far from feasible (max lambda_min <= {e(ol["ub"], 4)}); the maximiser has '
                      f'{len(ol["clusters"])} clusters, max |centroid - nearest log n| = {dmax:.3f}, max mass error {mmax:.2f}: no recovery')
    print()
    for tag in ('signed_N20', 'signed_N60'):
        for c, lam_lb, l1, tot, wmin, wmax, nneg, r in res[tag]:
            check(mp.mpf(c) - lam_lb < mp.mpf(10) ** -30,
                  f'{tag}: signed w with H0 + T(w) = c I, c = {c:g}: lambda_min >= {e(lam_lb, 20)}; sum|w| = {l1:.4e}, '
                  f'sum w = {tot:.4e}, min w = {wmin:.3e}, max w = {wmax:.3e}, {nneg} negative weights, moment residual {r:.1e}')
    print(f'\n# checks: {_PASS} passed, {_FAIL} failed')
    for line, msg in _FAILED:
        print(f'  FAILED [L{line}] {msg}')


if __name__ == '__main__':
    main()
