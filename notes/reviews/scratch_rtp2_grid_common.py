#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane G (claude:opus, 2026-09-26). Common helpers, independent of zst and of the lane script.

(a_n, b_n) of the CCM window form, split pole / archimedean / primes, in mpmath, with the closed forms of the
round-1 reviewer (notes/reviews/scratch_rtp1_ab.py, ported from python-flint to mpmath): pole by direct
exponentials, archimedean by the psi(1/2) - psi(A), psi'(A), Lerch arrangement (not zst's I_2/I_3/C(L) split).
Window [0, L], L = log x; t = y/L. Atom moment functions (lane G's convention, checked below against zst):
A_n(t) = -2 (1-t) cos(2 pi n t), B_n(t) = sin(2 pi n t)/pi; the prime part of (a_n, b_n) is
sum_k w_k (A_n(t_k), B_n(t_k)), w_k = Lambda(k)/sqrt(k), t_k = log k / L (k <= x; k = x is invisible).
Blocks: plan.md section 1.3. Run as a script: self-test against the lane's zst data files (x=13,25).
"""
import mpmath as mp
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LANE = ROOT / 'notes/rtp-round-2/grid-tomography/checks'

def prime_powers(x, include_endpoint=False):
    out = []
    for n in range(2, x + 1):
        if n == x and not include_endpoint:
            continue
        p = next(q for q in range(2, n + 1) if n % q == 0)
        r = n
        while r % p == 0:
            r //= p
        if r == 1:
            out.append((n, p))
    return out

def ab0(x, N):
    """pole + archimedean (a_n, b_n), n = 0..N, at the current mp.dps (no primes)."""
    L = mp.log(x); pi = mp.pi; e = mp.exp(-L / 2); z = mp.exp(-2 * L)
    K = int((mp.mp.prec + 60) / (2 * float(L) / float(mp.log(2)))) + 5
    half = mp.mpf(1) / 2
    const = mp.log(4 * pi) + mp.euler - mp.log((mp.exp(L) + 1) / (mp.exp(L) - 1))
    shalf = mp.fsum(z ** k / (k + half) for k in range(K))
    psi_half = mp.digamma(half)
    a = []; b = []
    for n in range(N + 1):
        w = 2 * pi * n / L
        ap = mp.mpf(0); bp = mp.mpf(0)
        for s in (half, -half):
            sig = mp.mpc(s, w); eL = mp.exp(sig * L)
            J = -1 / sig + (eL - 1) / (sig * sig * L)
            ap += 2 * J.real
            bp += -((eL - 1) / sig).imag / pi
        A = mp.mpc(mp.mpf(1) / 4, -pi * n / L)
        psiA = mp.digamma(A); psi1A = mp.psi(1, A)
        S1 = mp.mpc(0); S2 = mp.mpc(0); zk = mp.mpf(1)
        for k in range(K):
            S1 += zk / (k + A); S2 += zk / (k + A) ** 2; zk *= z
        AR = (psi_half - psiA).real / 2 - psi1A.real / (4 * L) + e / (4 * L) * S2.real + mp.exp(-L) / 2 * shalf
        ar = -(const + 2 * AR)
        br = (-psiA.imag / 2 - e / 2 * S1.imag) / pi
        a.append(ap + ar); b.append((bp + br) if n else mp.mpf(0))
    return a, b

def phi(N, t):
    """moment vector (A_0..A_N, B_1..B_N) of a unit atom at t = y/L."""
    t = mp.mpf(t)
    return [-2 * (1 - t) * mp.cos(2 * mp.pi * n * t) for n in range(N + 1)] + \
           [mp.sin(2 * mp.pi * n * t) / mp.pi for n in range(1, N + 1)]

def atoms(x):
    """interior visible atoms: list of (n, t, weight)."""
    L = mp.log(x)
    return [(n, mp.log(n) / L, mp.log(p) / mp.sqrt(n)) for n, p in prime_powers(x)]

def ab_true(x, N):
    a, b = ab0(x, N)
    a = list(a); b = list(b)
    for n, t, w in atoms(x):
        f = phi(N, t)
        for k in range(N + 1):
            a[k] += w * f[k]
        for k in range(1, N + 1):
            b[k] += w * f[N + k]
    return a, b

def blocks(a, b, N, ctor=None):
    """even block (N+1) and odd block (N), plan.md 1.3; ctor = mp.matrix or numpy."""
    E = [[mp.mpf(0)] * (N + 1) for _ in range(N + 1)]; O = [[mp.mpf(0)] * N for _ in range(N)]
    E[0][0] = a[0]
    for i in range(1, N + 1):
        E[0][i] = E[i][0] = mp.sqrt(2) * b[i] / i
        E[i][i] = a[i] + b[i] / i
        O[i - 1][i - 1] = a[i] - b[i] / i
        for j in range(1, i):
            t = (b[i] - b[j]) / (i - j); u = (b[i] + b[j]) / (i + j)
            E[i][j] = E[j][i] = t + u
            O[i - 1][j - 1] = O[j - 1][i - 1] = t - u
    return mp.matrix(E), mp.matrix(O)

def atom_blocks(N, t):
    f = phi(N, t)
    return blocks(f[:N + 1], [mp.mpf(0)] + f[N + 1:], N)

# ---------- float64 helpers (moment functions vectorised) ----------
def phi_np(N, ts):
    ts = np.asarray(ts, float)
    n = np.arange(N + 1)
    A = -2 * (1 - ts[:, None]) * np.cos(2 * np.pi * n[None, :] * ts[:, None])
    B = np.sin(2 * np.pi * n[None, 1:] * ts[:, None]) / np.pi
    return np.hstack([A, B])            # shape (J, 2N+1)

def blocks_np(a, b, N):
    a = np.asarray(a, float); b = np.asarray(b, float)
    E = np.zeros((N + 1, N + 1)); O = np.zeros((N, N))
    E[0, 0] = a[0]
    i = np.arange(1, N + 1)
    E[0, 1:] = E[1:, 0] = np.sqrt(2) * b[1:] / i
    I, Jm = np.meshgrid(i, i, indexing='ij')
    with np.errstate(divide='ignore', invalid='ignore'):
        T = (b[I] - b[Jm]) / (I - Jm); U = (b[I] + b[Jm]) / (I + Jm)
    E[1:, 1:] = np.where(I == Jm, 0, T + U); O[:, :] = np.where(I == Jm, 0, T - U)
    E[1:, 1:] += np.diag(a[1:] + b[1:] / i); O += np.diag(a[1:] - b[1:] / i)
    return E, O

def atom_blocks_np(N, ts):
    """stack of atom blocks for all t in ts: (J,N+1,N+1), (J,N,N)."""
    F = phi_np(N, ts)
    Es = []; Os = []
    for f in F:
        E, O = blocks_np(f[:N + 1], np.concatenate([[0.0], f[N + 1:]]), N)
        Es.append(E); Os.append(O)
    return np.array(Es), np.array(Os)

def read_lane_ab(x, N):
    """AB lines of the lane's zst data file: (a_x, b_x, a_1, b_1) per n, as mpf."""
    out = []
    for line in (LANE / f'x{x}_N{N}.data').read_text().splitlines():
        if line.startswith('AB '):
            s = line.split(); out.append([mp.mpf(v) for v in s[2:6]])
    return out

if __name__ == '__main__':
    fails = 0; count = 0
    def check(c, m):
        global fails, count
        count += 1; fails += (not c); print(('PASS ' if c else 'FAIL ') + m)
    mp.mp.dps = 60
    for x, N in [(13, 20), (25, 60)]:
        ref = read_lane_ab(x, N)
        a0, b0 = ab0(x, N)
        at, bt = ab_true(x, N)
        d0 = max(max(abs(a0[n] - ref[n][2]), abs(b0[n] - ref[n][3])) for n in range(N + 1))
        dt = max(max(abs(at[n] - ref[n][0]), abs(bt[n] - ref[n][1])) for n in range(N + 1))
        check(d0 < mp.mpf(10) ** -50, f'x={x} N={N}: reviewer pole+arch (a,b) = zst cutoff-1 data, max diff {mp.nstr(d0, 3)}')
        check(dt < mp.mpf(10) ** -50, f'x={x} N={N}: reviewer total (a,b) with atoms A_n,B_n = zst total, max diff {mp.nstr(dt, 3)}')
    # quadrature spot check of the archimedean + pole a_n at x=13 (definitions, cf. scratch_rtp1_ab.py)
    mp.mp.dps = 40
    Lf = mp.log(13); rho = lambda y: mp.e ** (y / 2) / (mp.e ** y - mp.e ** (-y))
    a0, b0 = ab0(13, 5)
    for n in (0, 3):
        w = 2 * mp.pi * n / Lf
        AR = mp.quad(lambda y: ((1 - y / Lf) * mp.cos(w * y) - mp.e ** (-y / 2)) * rho(y), mp.linspace(0, Lf, 8))
        ar = -((mp.log(4 * mp.pi) + mp.euler) - mp.log((mp.e ** Lf + 1) / (mp.e ** Lf - 1)) + 2 * AR)
        ap = mp.quad(lambda y: 2 * (1 - y / Lf) * mp.cos(w * y) * 2 * mp.cosh(y / 2), mp.linspace(0, Lf, 8))
        check(abs(ar + ap - a0[n]) < mp.mpf(10) ** -30, f'x=13 n={n}: pole+arch a_n = quadrature of the definitions, diff {mp.nstr(abs(ar + ap - a0[n]), 3)}')
    print(f'# checks: {count} run, {fails} failed')
