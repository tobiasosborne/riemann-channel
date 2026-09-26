#!/usr/bin/env python3
"""claude:opus REFUTE review of RTP-2 lane D (2026-09-26). Independent check (e): the Dirichlet Loewner
data (a_n, b_n) rebuilt from the formula sheet (notes/zeta-spectral-triples/ellcurve/astra-review.md F2,
F3, F5, F6, F8, F16) by direct mpmath quadrature -- NOT the closed forms F13-F15 used by libzst -- then the
even/odd blocks (zst/src/blocks.c convention) and their minimal eigenvalues by mpmath eigsy.
Floating (high-precision non-interval) arithmetic; compared with the driver's certified EIG/AB lines."""
import re, sys
from pathlib import Path
import mpmath as mp
ROOT = Path(__file__).resolve().parents[2]
mp.mp.dps = 45

def kron(D, n):
    # Kronecker symbol (D/n) for n >= 1 via sympy-free implementation
    from sympy.ntheory import jacobi_symbol
    from sympy import factorint
    r = 1
    for p, e in factorint(n).items():
        if p == 2:
            if D % 2 == 0: return 0
            v = 1 if D % 8 in (1, 7) else -1
        else:
            v = jacobi_symbol(D % p, p) if D % p else 0
        r *= v ** e
    return r

def prime_powers(X):
    from sympy import factorint
    out = []
    for k in range(2, X + 1):
        f = factorint(k)
        if len(f) == 1:
            (p, m), = f.items(); out.append((k, p, m))
    return out

def ab(D, x, N):
    q = abs(D); kappa = 1 if D < 0 else 0; mu = mp.mpf(kappa) + mp.mpf(1) / 2; d = 2
    L = mp.log(x)
    rho = lambda y: mp.exp(-mu * y) / (-mp.expm1(-d * y))
    T = mp.quad(rho, [L, L + 10, mp.inf])
    s = mp.log(q) - mp.log(mp.pi) + mp.digamma(mu / d) + 2 * T      # F8: log C + 2 log Q + (2/d) psi(mu/d) + 2 T
    atoms = [(mp.mpf(m) * mp.log(p), -kron(D, k) * mp.log(p) / mp.sqrt(k)) for (k, p, m) in prime_powers(int(x))]
    A, B = [], []
    for n in range(N + 1):
        om = 2 * mp.pi * n / L
        pts = mp.linspace(0, L, 2 * n + 3)
        g_sin = lambda y: mp.sin(om * y)
        g_cos = lambda y: (1 - y / L) * mp.cos(om * y)
        Dsin = mp.fsum(w * g_sin(y) for y, w in atoms) - mp.quad(lambda y: g_sin(y) * rho(y), pts)
        Dcos = mp.fsum(w * g_cos(y) for y, w in atoms) - mp.quad(lambda y: (g_cos(y) - 1) * rho(y), pts) + s / 2
        B.append(-Dsin / mp.pi if n else mp.mpf(0)); A.append(2 * Dcos)
    return A, B

def blocks(A, B, N):
    E = mp.matrix(N + 1, N + 1); O = mp.matrix(N, N)
    E[0, 0] = A[0]
    for j in range(1, N + 1):
        E[0, j] = E[j, 0] = mp.sqrt(2) * B[j] / j
        E[j, j] = A[j] + B[j] / j
        O[j - 1, j - 1] = A[j] - B[j] / j
        for i in range(1, j):
            t = (B[i] - B[j]) / (i - j); u = (B[i] + B[j]) / (i + j)
            E[i, j] = E[j, i] = t + u
            O[i - 1, j - 1] = O[j - 1, i - 1] = t - u
    return E, O

def driver_lines(D, x):
    s = (ROOT / f'outputs/rtp2_dirichlet_D{D}_axisN_x{x}.txt').read_text()
    abl = {int(m.group(1)): (m.group(2), m.group(3)) for m in re.finditer(r'^AB n=(\d+) a=(\S+) b=(\S+)', s, re.M)}
    eig = {int(m.group(1)): (m.group(2), m.group(3)) for m in re.finditer(r'^EIG x=\S+ X=\S+ N=(\d+) epsE=(\S+) epsO=(\S+)', s, re.M)}
    return abl, eig

cases = [(-4, 13, 20), (5, 13, 20), (-20, 13, 20)] if len(sys.argv) < 2 else [tuple(map(int, sys.argv[1:4]))]
for D, x, N in cases:
    A, B = ab(D, mp.mpf(x), N)
    abl, eig = driver_lines(D, x)
    for n in range(4):
        da = mp.mpf(abl[n][0]); db = mp.mpf(abl[n][1]) if abl[n][1] != '0' else mp.mpf(0)
        print(f'D={D} x={x} n={n}  |a_mp - a_drv|={mp.nstr(abs(A[n]-da),3)}  |b_mp - b_drv|={mp.nstr(abs(B[n]-db),3)}')
    E, O = blocks(A, B, N)
    eE = min(mp.eigsy(E, eigvals_only=True)); eO = min(mp.eigsy(O, eigvals_only=True))
    dE, dO = eig[N]
    print(f'D={D} x={x} N={N}: mpmath epsE={mp.nstr(eE,12)} driver {dE} rel.diff={mp.nstr(abs(eE/mp.mpf(dE)-1),3)}')
    print(f'D={D} x={x} N={N}: mpmath epsO={mp.nstr(eO,12)} driver {dO} rel.diff={mp.nstr(abs(eO/mp.mpf(dO)-1),3)}')
