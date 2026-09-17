#!/usr/bin/env python3
"""Reference prototype of Connes-Consani-Moscovici, "Zeta spectral triples" (arXiv:2511.22755).

Pipeline: Weil-form matrix tau on E_N in the basis V_n  ->  even block  ->  minimal eigenpair
(eps_N, xi)  ->  secular zeros of g(s) = sum_j xi_j/(j - s)  ->  z = 2 pi s / L  vs zeta zeros.

Every closed form is cross-checked against direct quadrature at low precision first.
"""
import sys
from mpmath import (mp, mpf, mpc, pi, exp, log, sin, cos, sinh, sqrt, digamma, polygamma, quad,
                    euler, atan, matrix, eigsy, zetazero, findroot, im, re, conj, nstr)

def prime_powers(x):
    """(k, Lambda(k)) for 1 < k <= x."""
    out = []
    k = 2
    while k <= x:
        # trial factorisation
        m, p = k, 2
        while p * p <= m and m % p:
            p += 1
        if m % p == 0 or p * p > m:
            if p * p > m:
                p = m
            q = k
            while q % p == 0:
                q //= p
            if q == 1:
                out.append((k, log(p)))
        k += 1
    return out

def rho(x):
    return exp(x / 2) / (exp(x) - exp(-x))

def arch_integrals_closed(n, L, z, terms=None):
    """I1 = int_0^L sin(w x) rho, I2 = int_0^L x cos(w x) rho, I3 = int_0^L (cos(w x)-1) rho,
    w = 2 pi n / L, via rho = sum_k exp(-(2k+1/2)x) and digamma/trigamma regularisation."""
    A = mpf(1) / 4 - 1j * pi * n / L          # 2k + 1/2 - i w = 2 (k + A)
    if terms is None:
        terms = int(mp.dps * 2.31 / (2 * L)) + 10
    S1 = mpc(0); S2 = mpc(0); S10 = mpf(0)
    zk = mpf(1)
    for k in range(terms):
        S1 += zk / (k + A); S2 += zk / (k + A) ** 2; S10 += zk / (k + mpf(1) / 4)
        zk *= z
    e = exp(-L / 2)
    I1 = -im(digamma(A)) / 2 - e * im(S1) / 2
    I2 = -(L * e / 2) * re(S1) + re(polygamma(1, A)) / 4 - (e / 4) * re(S2)
    I3 = (digamma(mpf(1) / 4) - re(digamma(A))) / 2 - (e / 2) * re(S1) + (e / 2) * S10
    return I1, I2, I3

def C_of_L(L):
    """int_0^L (1 - e^{-x/2}) rho(x) dx  (converts the (cos-1) integral to the (cos-e^{-x/2}) one)."""
    t = exp(L / 2)
    return -log(t + 1) + log(t * t + 1) / 2 + atan(t) + log(2) / 2 - pi / 4

def c_paper(L):
    """The paper's c(L) (their eq. after (corectc)): int_0^L (1-e^{-x/2})/(e^x-e^{-x}) dx."""
    t = exp(L / 2)
    return log(t + 1) + (-2 * log(t * t + 1) - pi - log(4)) / 4 + atan(t)

def w_of_L(L):
    return (euler + log(4 * pi)) / 2 - log((exp(L) + 1) / (exp(L) - 1)) / 2

def build_ab(lam, N, check=False):
    """Return arrays a[0..N], b[0..N] with tau_{nm} = (b_n - b_m)/(n-m), tau_{nn} = a_n,
    b_{-n} = -b_n, a_{-n} = a_n."""
    L = 2 * log(lam); z = exp(-2 * L)
    pp = prime_powers(int(lam * lam + mpf('1e-30')))
    K = 32 * L * sinh(L / 4) ** 2
    CL, wL = C_of_L(L), w_of_L(L)
    a = [None] * (N + 1); b = [None] * (N + 1)
    for n in range(N + 1):
        w = 2 * pi * n / L
        I1, I2, I3 = arch_integrals_closed(n, L, z)
        if check and n <= 3:
            # quadrature check of the three integrals
            J1 = quad(lambda x: sin(w * x) * rho(x), [0, L])
            J2 = quad(lambda x: x * cos(w * x) * rho(x), [0, L])
            J3 = quad(lambda x: (cos(w * x) - 1) * rho(x), [0, L])
            print(f"  n={n}: |I1-quad|={nstr(abs(I1-J1),3)} |I2-quad|={nstr(abs(I2-J2),3)} |I3-quad|={nstr(abs(I3-J3),3)}")
        # pole term (rank two): b^(02)_n = K n/(L^2+16 pi^2 n^2), a^(02)_n = K (L^2-16 pi^2 n^2)/(L^2+16 pi^2 n^2)^2
        den = L * L + 16 * pi * pi * n * n
        b02 = K * n / den
        a02 = K * (L * L - 16 * pi * pi * n * n) / den ** 2
        # archimedean: b^(R)_n = I1/pi ; a^(R)_n = -2 [ w(L) + I3 + C(L) - I2/L ]
        bR = I1 / pi
        aR = -2 * (wL + I3 + CL - I2 / L)
        # primes: b^(p)_n = (1/pi) sum Lambda(k) k^{-1/2} sin(w log k); a^(p)_n = -2 sum Lambda k^{-1/2} (1 - log k/L) cos(w log k)
        bp = mpf(0); ap = mpf(0)
        for k, Lk in pp:
            y = log(k)
            bp += Lk / sqrt(k) * sin(w * y)
            ap += Lk / sqrt(k) * (1 - y / L) * cos(w * y)
        b[n] = b02 + bR + bp / pi
        a[n] = a02 + aR - 2 * ap
    return L, a, b

def tau_entry(a, b, n, m):
    sn = 1 if n >= 0 else -1; sm = 1 if m >= 0 else -1
    if n == m:
        return a[abs(n)]
    return (sn * b[abs(n)] - sm * b[abs(m)]) / (n - m)

def even_block(a, b, N):
    """Basis c_0 = V_0, c_j = (V_j + V_{-j})/sqrt2, j = 1..N."""
    E = matrix(N + 1, N + 1)
    E[0, 0] = a[0]
    for j in range(1, N + 1):
        E[0, j] = E[j, 0] = sqrt(2) * b[j] / j
        for i in range(1, N + 1):
            if i == j:
                E[i, i] = a[i] + b[i] / i
            else:
                E[i, j] = (b[i] - b[j]) / (i - j) + (b[i] + b[j]) / (i + j)
    return E

def odd_block(a, b, N):
    O = matrix(N, N)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                O[i - 1, i - 1] = a[i] - b[i] / i
            else:
                O[i - 1, j - 1] = (b[i] - b[j]) / (i - j) - (b[i] + b[j]) / (i + j)
    return O

def quad_check_tau(lam, a, b, L):
    """Check a few tau entries against the defining integrals by quadrature."""
    pp = prime_powers(int(lam * lam + mpf('1e-30')))
    K = 32 * L * sinh(L / 4) ** 2
    def q(n, m, y):
        if n == m:
            return 2 * (1 - y / L) * cos(2 * pi * n * y / L)
        return (sin(2 * pi * m * y / L) - sin(2 * pi * n * y / L)) / (pi * (n - m))
    for (n, m) in [(0, 0), (1, 1), (2, 2), (0, 1), (1, 3), (-2, 3)]:
        # W02 by direct formula
        W02 = K * (L * L - 16 * pi * pi * m * n) / ((L * L + 16 * pi * pi * m * m) * (L * L + 16 * pi * pi * n * n))
        # W_R by quadrature of the principal-value form
        om0 = q(n, m, mpf(0))
        WR = om0 / 2 * (euler + log(4 * pi * (exp(L) - 1) / (exp(L) + 1))) \
             + quad(lambda x: (exp(x / 2) * q(n, m, x) - om0) / (exp(x) - exp(-x)), [0, L])
        Wp = sum(Lk / sqrt(k) * q(n, m, log(k)) for k, Lk in pp)
        direct = W02 - WR - Wp
        closed = tau_entry(a, b, n, m)
        print(f"  tau[{n:2d},{m:2d}]: closed={nstr(closed, 12)} direct={nstr(direct, 12)} diff={nstr(abs(closed-direct), 3)}")

def secular_roots(xi_even, N, sub=32):
    """xi_even[j] = xi_j for j=0..N (xi_{-j}=xi_j), normalised sum_{all j} xi_j = 1.
    g(s) = -xi_0/s + 2 s sum_{j>=1} xi_j/(j^2 - s^2) has exactly 2N real zeros (N positive ones);
    between consecutive poles there may be several (xi_j changes sign), so sample each pole
    interval on a grid of `sub` points and bisect every sign change.  Returns positive roots."""
    def g(s):
        return -xi_even[0] / s + 2 * s * sum(xi_even[j] / (j * j - s * s) for j in range(1, N + 1))
    roots = []
    eps = mpf(10) ** (-mp.dps // 2)
    for j in range(N):
        lo, hi = mpf(j) + eps, mpf(j + 1) - eps
        grid = [lo + (hi - lo) * k / sub for k in range(sub + 1)]
        vals = [g(s) for s in grid]
        for k in range(sub):
            if vals[k] * vals[k + 1] < 0:
                r = findroot(g, (grid[k], grid[k + 1]), solver='bisect',
                             tol=mpf(10) ** (-mp.dps + 5), maxsteps=mp.dps * 4)
                roots.append(findroot(g, r))
    return roots

def main():
    lam = mpf(sys.argv[1]) if len(sys.argv) > 1 else mpf(3)
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    mp.dps = int(sys.argv[3]) if len(sys.argv) > 3 else 60
    L = 2 * log(lam)
    print(f"lambda={lam}, N={N}, dps={mp.dps}, L={nstr(L,10)}, primes powers <= {int(lam*lam)}")

    print("C(L) check: closed vs quadrature of (1-e^{-x/2}) rho, and the paper's c(L):")
    CLq = quad(lambda x: (1 - exp(-x / 2)) * rho(x), [0, L])
    print("  C(L) closed =", nstr(C_of_L(L), 20), " quad =", nstr(CLq, 20), " paper c(L) =", nstr(c_paper(L), 20))

    print("archimedean closed forms vs quadrature:")
    L, a, b = build_ab(lam, N, check=True)
    print("tau entries closed vs direct:")
    quad_check_tau(lam, a, b, L)

    E = even_block(a, b, N); O = odd_block(a, b, N)
    ev, U = eigsy(E)
    evo = eigsy(O, eigvals_only=True)
    idx = min(range(N + 1), key=lambda i: ev[i])
    eps0 = ev[idx]
    others = sorted(ev[i] for i in range(N + 1) if i != idx)
    print(f"even block: eps_N = {nstr(eps0, 8)}, next even = {nstr(others[0], 8)}, {nstr(others[1], 8)}; smallest odd = {nstr(min(evo), 8)}")
    c = [U[i, idx] for i in range(N + 1)]
    xi = [c[0]] + [c[j] / sqrt(2) for j in range(1, N + 1)]   # xi_j, j >= 0
    norm = xi[0] + 2 * sum(xi[1:])
    xi = [x / norm for x in xi]
    roots = secular_roots(xi, N)
    print(f"{len(roots)} positive secular roots found (expected N = {N}); z = 2 pi s / L vs zeta zeros:")
    for k, s in enumerate(roots[:min(50, len(roots))]):
        zk = 2 * pi * s / L
        gam = im(zetazero(k + 1))
        print(f"  {k+1:2d}: z = {nstr(zk, 25)}  gamma = {nstr(gam, 25)}  |diff| = {nstr(abs(zk - gam), 3)}")

if __name__ == "__main__":
    main()
