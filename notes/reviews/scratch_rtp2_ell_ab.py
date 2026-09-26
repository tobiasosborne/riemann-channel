#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane E (claude:opus, 2026-09-26).  Independent mpmath recomputation of the elliptic
Loewner data (a_n, b_n) and of the block minima eps_N at x = 13, small N, for 11a1, 14a1 and 37a1.
No zst code, no lane script is imported.  Ingredients, all rederived here:
  * a_p by brute-force point counting on the general Weierstrass model (singular point counted, so bad primes
    give a_p = 1, -1, 0 automatically); t_m by the Lucas recurrence at good primes, a_p^m at bad primes;
    prime-power weight w = -t_m log p / p^m (arithmetic normalisation, centre 1);
  * the archimedean + conductor part from the Fourier multiplier h(t) = log(C/4pi^2) + 2 Re psi(1+it), turned into
    the one-sided functional by the digamma series Re psi(1+it) = -gamma + sum_k [1/(k+1) - Re 1/(k+1+it)]:
       D(q) = sum w q(m log p) - int_0^L (q(y)-q(0)) e^{-y}/(1-e^{-y}) dy + (s/2) q(0),
       s = log C - 2 log(2 pi) - 2 gamma - 2 log(1 - e^{-L})    (half of the full-line even pairing);
  * a_n = 2 D((1 - y/L) cos(w_n y)), b_n = -(1/pi) D(sin(w_n y)), w_n = 2 pi n / L, L = log x;
  * Loewner matrix tau_nm = (b_n - b_m)/(n - m), tau_nn = a_n on |n| <= N; even block on (V_n + V_-n)/sqrt2 with V_0,
    odd block on (V_n - V_-n)/sqrt2; minima by mpmath eigsy at 40 digits.
Deterministic.  Compared with the 30-digit AB lines and the EIG lines of outputs/rtp2_ellcurve_<c>_axisN_x13.txt."""
import mpmath as mp, re
mp.mp.dps = 40
MODELS = {'11a1': ((0, -1, 1, -10, -20), 11), '14a1': ((1, 0, 1, 4, -6), 14), '37a1': ((0, 0, 1, -1, 0), 37)}
def ap(ai, p):
    a1, a2, a3, a4, a6 = ai
    A = sum(1 for u in range(p) for v in range(p) if (v*v + a1*u*v + a3*v - (u**3 + a2*u*u + a4*u + a6)) % p == 0)
    return p - A
def primes_upto(n): return [p for p in range(2, n + 1) if all(p % d for d in range(2, int(p**.5) + 1))]
def weights(ai, C, x):
    W = []
    for p in primes_upto(x):
        a = ap(ai, p); good = C % p != 0; t0, t1 = 2, a; m = 1; k = p
        while k <= x:
            t = t1 if m == 1 else None
            if m > 1:
                if good: t0, t1 = t1, a*t1 - p*t0; t = t1
                else: t = a**m
            W.append((k, mp.mpf(-t) * mp.log(p) / k)); m += 1; k *= p
    return W
def D(q, W, C, L, pts):
    s = mp.log(C) - 2*mp.log(2*mp.pi) - 2*mp.euler - 2*mp.log(1 - mp.e**(-L))
    rho = lambda y: mp.e**(-y) / (1 - mp.e**(-y))
    q0 = q(mp.mpf(0))
    I = mp.quad(lambda y: (q(y) - q0) * rho(y) if y > 0 else mp.mpf(0), pts)
    return sum(w * q(mp.log(k)) for k, w in W) - I + s/2 * q0
def ab(c, x, N):
    ai, C = MODELS[c]; L = mp.log(x); W = weights(ai, C, x)
    pts = [L * j / (8 + 4*N) for j in range(9 + 4*N)]
    a, b = [], []
    for n in range(N + 1):
        om = 2 * mp.pi * n / L
        a.append(2 * D(lambda y: (1 - y/L) * mp.cos(om*y), W, C, L, pts))
        b.append(mp.mpf(0) if n == 0 else -D(lambda y: mp.sin(om*y), W, C, L, pts) / mp.pi)
    return a, b
def blocks(a, b, N):
    A = lambda n: a[abs(n)]; B = lambda n: b[n] if n >= 0 else -b[-n]
    tau = lambda n, m: A(n) if n == m else (B(n) - B(m)) / (n - m)
    E = mp.matrix(N + 1, N + 1); O = mp.matrix(N, N)
    for i in range(N + 1):
        for j in range(N + 1):
            if i == 0 and j == 0: E[0, 0] = tau(0, 0)
            elif i == 0: E[0, j] = mp.sqrt(2) * tau(0, j)
            elif j == 0: E[i, 0] = mp.sqrt(2) * tau(i, 0)
            else: E[i, j] = tau(i, j) + tau(i, -j)
    for i in range(1, N + 1):
        for j in range(1, N + 1): O[i-1, j-1] = tau(i, j) - tau(i, -j)
    return E, O
def lane_values(c):
    t = open(f'/home/tobiasosborne/Projects/riemann-channel/outputs/rtp2_ellcurve_{c}_axisN_x13.txt').read()
    AB = {int(m[0]): (mp.mpf(m[1]), mp.mpf(m[2])) for m in re.findall(r'^AB n=(\d+) a=(\S+) b=(\S+)', t, re.M)}
    EIG = {int(m[0]): (mp.mpf(m[1]), mp.mpf(m[2]), int(m[3])) for m in re.findall(r'^EIG x=13 X=13 N=(\d+) epsE=(\S+) epsO=(\S+) parity=(-?\d)', t, re.M)}
    return AB, EIG
checks = fails = 0
def check(ok, msg):
    global checks, fails
    checks += 1
    if not ok: fails += 1
    print(('ok  ' if ok else 'FAIL') + ' ' + msg)
for c in ('11a1', '14a1', '37a1'):
    ai, C = MODELS[c]
    print(f'== {c}: a_p for p <= 13:', {p: ap(ai, p) for p in primes_upto(13)})
    AB, EIG = lane_values(c)
    Ns = sorted(n for n in EIG if n <= 20)
    a, b = ab(c, 13, max(Ns))
    for n in range(4):
        da = abs(a[n] - AB[n][0]); db = abs(b[n] - AB[n][1])
        check(da < 1e-28 and db < 1e-28, f'{c} x=13 n={n}: a={mp.nstr(a[n], 32)} b={mp.nstr(b[n], 32)} |diff| {mp.nstr(max(da, db), 3)}')
    for N in Ns:
        E, O = blocks(a, b, N)
        eE = min(mp.eigsy(E, eigvals_only=True)); eO = min(mp.eigsy(O, eigvals_only=True))
        LE, LO, par = EIG[N]
        rel = max(abs(eE/LE - 1), abs(eO/LO - 1))
        mypar = 1 if eE < eO else -1
        check(rel < 1e-10 and mypar == par, f'{c} x=13 N={N}: epsE {mp.nstr(eE, 13)} epsO {mp.nstr(eO, 13)} parity {mypar:+d} (lane {mp.nstr(LE, 12)}, {mp.nstr(LO, 12)}, {par:+d}); rel diff {mp.nstr(rel, 3)}')
print(f'# checks: {checks} run, {fails} failed')
