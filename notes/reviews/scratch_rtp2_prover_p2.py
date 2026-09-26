#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane P, item P2 (finite-prime language, point masses, prime remainder).
Independent of the lane's checks. mpmath/sympy/numpy. Deterministic. No zeros of zeta are used."""
import mpmath as mp, sympy as sp, numpy as np
mp.mp.dps = 50
ok = 0; bad = 0
def chk(name, cond):
    global ok, bad
    if cond: ok += 1; print("PASS", name)
    else: bad += 1; print("FAIL", name)

# ---- 1. The archimedean set A of finite-prime-language.md contains log q for every prime q, twice over.
# (a) explicitly: 'log of algebraic numbers' (q is algebraic). (b) even without (a): Gauss multiplication
#     psi(q x) = log q + (1/q) sum_{k=0}^{q-1} psi(x + k/q) at x = 1/q gives log q = psi(1) - (1/q) sum_{j=1}^q psi(j/q).
for q in [2, 3, 5, 7, 11, 13, 97]:
    val = mp.digamma(1) - mp.fsum(mp.digamma(mp.mpf(j) / q) for j in range(1, q + 1)) / q
    chk("log %d = psi(1) - (1/%d) sum_j psi(j/%d)  (|diff| = %s)" % (q, q, q, mp.nstr(abs(val - mp.log(q)), 3)), abs(val - mp.log(q)) < mp.mpf(10) ** -45)
chk("psi(1/2) = -gamma - 2 log 2", abs(mp.digamma(0.5) + mp.euler + 2 * mp.log(2)) < mp.mpf(10) ** -45)

# ---- 2. CCM kernels at rational displacement D = log r (no extra factor D), P2.3 step 2 and the 3-atom table
def pole(r): return sp.nsimplify(sp.sqrt(r) + 1 / sp.sqrt(r))
def rho(r): return sp.simplify(sp.sqrt(r) / (r - sp.Rational(1, r) if isinstance(r, int) else r - 1 / r))
tab = {2: (3 * sp.sqrt(2) / 2, 2 * sp.sqrt(2) / 3), 3: (4 * sp.sqrt(3) / 3, 3 * sp.sqrt(3) / 8), 6: (7 * sp.sqrt(6) / 6, 6 * sp.sqrt(6) / 35)}
for r, (pv, rv) in tab.items():
    chk("pole kernel 2cosh(log%d/2) = %s" % (r, pv), sp.simplify(sp.sqrt(r) + 1 / sp.sqrt(r) - pv) == 0)
    chk("rho(log %d) = %s" % (r, rv), sp.simplify(sp.sqrt(r) / (r - sp.Rational(1, r)) - rv) == 0)
    # rho from CCM line 440: x^{1/2}/(x - x^{-1}) at x = r, and e^{y/2}/(e^y - e^{-y}) at y = log r
    chk("rho CCM form agrees numerically at r=%d" % r, abs(mp.e ** (mp.log(r) / 2) / (r - mp.mpf(1) / r) - mp.mpf(sp.N(rv, 60))) < mp.mpf(10) ** -45)

# ---- 3. A_p for M = {1,2,6}, c = (1,2,-1) and R_fin
M = [1, 2, 6]; c = {1: 1, 2: 2, 6: -1}
A = {}
for m in M:
    for n in M:
        rr = sp.Rational(n, m)
        if rr > 1 and rr.q == 1:
            f = sp.factorint(int(rr))
            if len(f) == 1:
                (p, k), = f.items()
                A[p] = A.get(p, 0) + (sp.conjugate(c[m]) * c[n] + c[m] * sp.conjugate(c[n])) / sp.sqrt(p) ** k
chk("A_2 = 2 sqrt2", sp.simplify(A[2] - 2 * sp.sqrt(2)) == 0)
chk("A_3 = -4/sqrt3", sp.simplify(A[3] + 4 / sp.sqrt(3)) == 0)
chk("no prime-power term for the pair ratio 6", set(A) == {2, 3})
Rfin = -sum(A[p] * sp.log(p) for p in A)
Rv = sp.N(Rfin, 40)
print("   R_fin =", Rv)
chk("R_fin = 0.5766201154531615253177476429...", abs(Rv - sp.Float('0.576620115453161525317747642908', 40)) < 1e-29)

# ---- 4. P2.4 on an actual smooth bump: prime remainder equals -sum A_p log p exactly (only R_delta(0)=1 matters)
def phi0(u):
    out = np.zeros_like(u); m = np.abs(u) < 1
    out[m] = np.exp(-1.0 / (1 - u[m] ** 2)); return out
h = 2e-5
u = np.arange(-50000, 50001) * h
ph = phi0(u); ph = ph / np.sqrt(np.sum(ph ** 2) * h)
from scipy.signal import fftconvolve
acf = fftconvolve(ph, ph[::-1], mode='full') * h          # values at t = k h, k = -(n-1)..(n-1)
tgrid = np.arange(-(len(u) - 1), len(u)) * h
def R(t):   # autocorrelation of the L2-normalised even bump, support [-2,2], R(0) = 1
    t = np.atleast_1d(np.asarray(t, dtype=float))
    return np.where(np.abs(t) < 2, np.interp(t, tgrid, acf), 0.0)
chk("R(0) = 1 for the L2-normalised bump", abs(R(0.0)[0] - 1) < 1e-9)
delta = 0.05   # admissible: nearest foreign prime powers to ratio centres log 2, log 3, log 6 are log 7, log 5 (gap 0.154 > 2 delta)
def F(y):
    return sum(c[m] * c[n] * R((y - np.log(n / m)) / delta)[0] for m in M for n in M)
primes = [2, 3, 5, 7, 11, 13]
Wp_total = 0.0
for p in primes:
    k = 1
    while k * np.log(p) < np.log(6) + 2 * delta + 1e-12:
        Wp_total += np.log(p) * p ** (-k / 2) * (F(k * np.log(p)) + F(-k * np.log(p))); k += 1
chk("sum_p W_p(F) = sum_p A_p log p on the admissible bump (|diff| < 1e-8)", abs(Wp_total - float(sum(A[p] * sp.log(p) for p in A))) < 1e-8)

# ---- 5. P2.3 step 3: the regularised point mass has Q -> +infinity like log(1/delta)
# single atom, L2-normalised: W_R(R_delta) = c_R + int_0^{2 delta} (2 R(y/delta) - 2 e^{-y/2}) rho(y) dy + log tanh(delta)
cR = float(mp.log(4 * mp.pi) + mp.euler)
tt = np.linspace(1e-9, 2, 20001); Rt = R(tt)
vals = []
for d in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]:
    y = d * tt
    rho_y = np.exp(y / 2) / (np.exp(y) - np.exp(-y))
    near = np.trapz((2 * Rt - 2 * np.exp(-y / 2)) * rho_y, y)
    WR = cR + near + np.log(np.tanh(d))
    W02 = 2 * np.cosh(0) * 0  # placeholder, bounded by 2cosh(2d) * int F = O(d); computed below
    intF = np.trapz(Rt, tt) * 2 * d
    W02 = 2 * np.cosh(d) * intF
    Q = W02 - WR   # no prime terms for 2 delta < log 2
    vals.append((d, Q, Q - np.log(1 / d)))
    print("   delta = %.0e   Q = %.6f   Q - log(1/delta) = %.6f" % (d, Q, Q - np.log(1 / d)))
dif = [abs(vals[i + 1][2] - vals[i][2]) for i in range(len(vals) - 1)]
chk("Q(phi_delta) - log(1/delta) converges at rate O(delta) (successive differences shrink ~10x; last < 1e-3)", all(dif[i + 1] < 0.2 * dif[i] for i in range(len(dif) - 1)) and dif[-1] < 1e-3)
chk("Q(phi_delta) -> +infinity (grows by log 10 per decade)", all(abs((vals[i + 1][1] - vals[i][1]) - np.log(10)) < 0.25 for i in range(len(vals) - 1)))
# L1 normalisation (the literal point-mass limit): F scales by 1/delta, so Q ~ delta^{-1} log(1/delta), prime evaluations ~ 1/delta
print("checks passed %d failed %d" % (ok, bad))
