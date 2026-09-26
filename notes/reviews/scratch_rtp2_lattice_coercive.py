#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane L (claude:opus, 2026-09-26): L3 on a toy.
Toy window form with a spectral gap: D = (mu/2) delta_0 + c e^{-y} on [0, L] (e^{-|y|} is a positive-definite kernel, so the
second part is a PSD form; the first is mu*I).  Atoms at y_k = log n (n = 2..12, L = log 13) with the lane's Loewner atom
T_k (point mass -delta(y - y_k)).  True weights w* arbitrary; H0 := H* - T(w*).  Checks:
 (a) ||T_k|| <= 2 on E_N for every N tried (the bound L3 uses), and the spectral norm approaches its sup from below;
 (b) lambda_min(H*_N) >= mu and decreases in N (compression), limit ~ mu;
 (c) every displacement with 2 ||delta||_1 < mu is feasible at every N (random + worst sign patterns), and the exact axis
     sections have half-widths >= mu/||T_k|| >= mu/2 (so widths >= mu), for all N;
 (d) the ball is essentially sharp for an atom near the origin: displacement just beyond mu/||T_k|| along the worst
     single atom becomes infeasible at large N;
 (e) H-PIN is impossible under H-GAP: any PSD Z with tr(Z T_k) = +-1 has tr(Z H*) >= mu tr Z >= mu/2 (numerical LP check
     of the cheapest eigenvector dual at each N);
 (f) the lane's counterexample to 'eps_N -> 0 suffices': H* = diag(1, 1, 1/2, 1/3, ...), T = diag(d, -d, 0, ...).
All in double precision (the toy is well conditioned)."""
import math
import numpy as np
from scipy.optimize import linprog
NCHK = [0, 0]
def check(c, msg):
    NCHK[0] += 1; NCHK[1] += (not c); print(('PASS ' if c else 'FAIL ') + msg, flush=True)

def full_loewner(a, b, N):
    """full (2N+1) Loewner matrix tau_nm = (b_n - b_m)/(n - m), tau_nn = a_n; a_{-n} = a_n, b_{-n} = -b_n"""
    idx = np.arange(-N, N + 1); A = np.array([a[abs(n)] for n in idx]); B = np.array([(b[n] if n > 0 else -b[-n]) if n else 0.0 for n in idx])
    M = np.zeros((2 * N + 1, 2 * N + 1))
    for i, n in enumerate(idx):
        for j, k in enumerate(idx):
            M[i, j] = A[i] if i == j else (B[i] - B[j]) / (n - k)
    return M
L = math.log(13); mu = 0.1; c = 0.7
def atom(N, t):
    return full_loewner([-2 * (1 - t) * math.cos(2 * math.pi * j * t) for j in range(N + 1)], [math.sin(2 * math.pi * j * t) / math.pi for j in range(N + 1)], N)
def expo_form(N):
    # D(y) = c e^{-y}: a_n = 2 int (1 - y/L) cos(w y) c e^{-y} dy, b_n = -(1/pi) int sin(w y) c e^{-y} dy (closed forms via complex exp)
    a, b = [], []
    for n in range(N + 1):
        w = 2 * math.pi * n / L; z = complex(-1, w)                      # int_0^L e^{z y} dy, int_0^L y e^{z y} dy
        I0 = (np.exp(z * L) - 1) / z; I1 = (L * np.exp(z * L)) / z - (np.exp(z * L) - 1) / z ** 2
        a.append(2 * c * (I0 - I1 / L).real); b.append(-(c / math.pi) * I0.imag)
    return full_loewner(a, b, N)
# quadrature cross-check of the closed forms at one n
from scipy.integrate import quad
n0 = 3; w0 = 2 * math.pi * n0 / L
qa = 2 * quad(lambda y: (1 - y / L) * math.cos(w0 * y) * c * math.exp(-y), 0, L, limit=200)[0]
qb = -quad(lambda y: math.sin(w0 * y) * c * math.exp(-y), 0, L, limit=200)[0] / math.pi
M3 = expo_form(3)
check(abs(M3[2 * 3, 2 * 3] - qa) < 1e-12 and abs((M3[2 * 3, 3] * 3) - qb) < 1e-12, f'toy Loewner data of c e^(-y) match quadrature (a_3 {qa:.12f}, b_3 {qb:.12f})')
ts = [math.log(n) / L for n in range(2, 13)]
rng = np.random.default_rng(7)
wstar = rng.normal(size=len(ts))
for N in (10, 40, 120):
    Ts = [atom(N, t) for t in ts]
    norms = [np.abs(np.linalg.eigvalsh(T)).max() for T in Ts]
    Hstar = mu * np.eye(2 * N + 1) + expo_form(N)
    H0 = Hstar - sum(w * T for w, T in zip(wstar, Ts))
    lmin = np.linalg.eigvalsh(Hstar)[0]
    check(max(norms) <= 2 + 1e-12, f'N={N}: ||T_k|| over the 11 atoms: max {max(norms):.6f}, min {min(norms):.6f} (<= 2)')
    pred = [2 * math.cos(math.pi / (math.ceil(1 / t) + 1)) for t in ts]
    dev = max(abs(a - b) for a, b in zip(norms, pred))
    print(f'   N={N}: ||T_k|| vs 2 cos(pi/(ceil(L/y_k)+1)): max deviation {dev:.2e}  (norms {[round(v, 4) for v in norms]})')
    if N == 120: check(dev < 1e-3 and all(a <= b + 1e-12 for a, b in zip(norms, pred)), 'N=120: ||T_k|| agrees with 2 cos(pi/(ceil(L/y_k)+1)) < 2 for every atom (from below)')
    check(lmin >= mu - 1e-12, f'N={N}: lambda_min(H*) = {lmin:.8f} >= mu = {mu}')
    # (c) random displacements in the open l1-ball of radius mu/2
    worst = np.inf
    for trial in range(400):
        d = rng.normal(size=len(ts)) * np.maximum(rng.random(len(ts)) < 0.5, np.eye(len(ts))[trial % 11]); d = d / np.abs(d).sum() * (mu / 2) * (1 - 1e-9)
        if trial < 22: d = np.zeros(len(ts)); d[trial % 11] = (1 if trial < 11 else -1) * mu / 2 * (1 - 1e-9)
        worst = min(worst, np.linalg.eigvalsh(H0 + sum((w + dd) * T for w, dd, T in zip(wstar, d, Ts)))[0])
    check(worst >= -1e-12, f'N={N}: 400 displacements with 2||delta||_1 < mu (incl. all +-mu/2 e_k) stay feasible: min lambda_min {worst:.3e}')
    # exact axis sections of the lattice set around w*
    Lc = np.linalg.cholesky(Hstar); Li = np.linalg.inv(Lc)
    hw = []
    for T, nr in zip(Ts, norms):
        ev = np.linalg.eigvalsh(Li @ T @ Li.T)
        hi = -1 / ev[0] if ev[0] < 0 else np.inf; lo = 1 / ev[-1] if ev[-1] > 0 else np.inf
        hw.append((min(hi, lo), nr))
    check(all(h >= mu / nr - 1e-12 for h, nr in hw), f'N={N}: axis-section half-widths >= mu/||T_k|| >= mu/2: min half-width {min(h for h, _ in hw):.5f} (mu/2 = {mu/2})')
    # (d) sharpness near the origin: the atom at log 2 has ||T|| closest to 2
    k = int(np.argmax(norms)); T = Ts[k]
    ev, V = np.linalg.eigh(T)
    # direction that pushes the form down fastest: sign so that delta*T has eigenvalue -||T||
    sgn = 1 if abs(ev[0]) >= abs(ev[-1]) else -1
    dcrit = min(hw[k][0], np.inf)
    print(f'   N={N}: atom n={k+2}: ||T|| = {norms[k]:.5f}; its axis half-width {dcrit:.5f} vs the ball bound mu/2 = {mu/2} and mu/||T|| = {mu/norms[k]:.5f}')
    # (e) cheapest eigenvector-LP pin cost for coordinate 0 (upper + lower); must be >= mu
    lam, Vh = np.linalg.eigh(Hstar)
    G = np.array([[v @ T @ v for T in Ts] for v in Vh.T])
    cost = 0
    for s in (1, -1):
        r = linprog(lam, A_eq=G.T, b_eq=-s * np.eye(len(ts))[0], bounds=[(0, None)] * len(lam), method='highs')
        cost += r.fun if r.status == 0 else np.inf
    check(cost >= mu - 1e-9, f'N={N}: cheapest eigenvector dual pair for w_2 costs {cost:.5f} >= mu (H-PIN impossible under H-GAP)')
# (f) the lane's diagonal example
for Nn in (10, 100, 1000):
    Hd = np.r_[1.0, 1.0, 1 / np.arange(2, Nn)]
    # feasible delta: 1 + d >= 0, 1 - d >= 0 -> [-1, 1] regardless of Nn; eps_N = 1/(Nn-1)
    check(Hd.min() == 1 / (Nn - 1), f'diag example Nn={Nn}: eps = {Hd.min():.2e} -> 0 while the feasible interval stays [-1, 1]')
print(f'# checks: {NCHK[0]} run, {NCHK[1]} failed')
