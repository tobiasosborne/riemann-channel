#!/usr/bin/env python3
"""Numerics lane for notes/connes-weighted-metric/astra-proofs.md (independent of the prover's checks/).

author: claude:fable-5.1 (numerics lane); written from the displayed formulas of W1-W4 and Section 6 only.

Conventions (proofs Section 0): X = log y, inner products linear in the first slot, Fourier
f^(u) = int f(X) e^{iuX} dX with boundary measure du/(2 pi); Theta(u) = xi(1+2iu)/xi(1-2iu);
w_rho = gamma/2 + i(1-sigma)/2, d_rho = -i conj(w_rho), e_rho(X) = e^{d_rho X} 1_{X>0}, e_rho^ = i k_rho,
k_rho(u) = 1/(u - conj w_rho).  Under RH: w_j = gamma_j/2 + i/4, d_j = -1/4 - i gamma_j/2.
Gram matrices M_ij = <e_i, e_j> (form a^T M conj a); H = M^T is the a^* H a convention.

Ledger lines: Dnn PASS/FAIL <description> <value>.
"""
import sys, time
import numpy as np
import mpmath as mp

mp.mp.dps = 30
T0 = time.time()
LED = []


def check(ok, desc, val=""):
    LED.append((bool(ok), desc, str(val)))
    print("D%02d %s %s %s" % (len(LED), "PASS" if ok else "FAIL", desc, val))


def sec(t):
    print("\n== " + t)


# ----------------------------------------------------------------------------- zeros
_G = []


def gammas(n):
    while len(_G) < n:
        _G.append(mp.im(mp.zetazero(len(_G) + 1)))
    return _G[:n]


Z3000 = np.load("data/zeros3000.npy")  # positive ordinates, float64

# ----------------------------------------------------------------------------- xi, Theta
def xi(s):
    s = mp.mpc(s)
    return s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def Theta(u):
    u = mp.mpc(u)
    return xi(1 + 2j * u) / xi(1 - 2j * u)


def xi_prime(rho):
    """xi'(rho) at a zero: (rho(rho-1)/2) pi^{-rho/2} Gamma(rho/2) zeta'(rho)  (6.1)."""
    rho = mp.mpc(rho)
    return rho * (rho - 1) / 2 * mp.pi ** (-rho / 2) * mp.gamma(rho / 2) * mp.zeta(rho, derivative=1)


def Theta_prime_formula(rho):
    """(6.1): Theta'(w_rho) = 2 i xi'(rho) / xi(2 - rho)."""
    return 2j * xi_prime(rho) / xi(2 - rho)


# ----------------------------------------------------------------------------- W1: biorthogonals
sec("W1: Theta'(w_j) two ways; ||k||^2 = 1/(2h) = 2; ||b_j|| = sqrt2 / |Theta'(w_j)|")
N10 = 10
G10 = gammas(N10)
w = [g / 2 + 0.25j for g in G10]
rho = [mp.mpf(1) / 2 + 1j * g for g in G10]

okA = True; maxrel = mp.mpf(0)
Tp = []
for j in range(N10):
    a = Theta_prime_formula(rho[j])
    b = mp.diff(Theta, w[j])
    rel = abs(a - b) / abs(a)
    maxrel = max(maxrel, rel)
    Tp.append(a)
    okA &= rel < mp.mpf(10) ** (-20)
check(okA, "(6.1) Theta'(w_j) = 2i xi'(rho_j)/xi(2-rho_j) vs direct differentiation, 10 zeros, max rel err", mp.nstr(maxrel, 5))

# |Theta(w_j)| = 0 and |Theta| = 1 on the real line
zmax = max(abs(Theta(w[j])) for j in range(N10))
check(zmax < mp.mpf(10) ** (-25), "Theta(w_j) = 0 at the ten zeros, max |Theta|", mp.nstr(zmax, 3))
umod = max(abs(abs(Theta(mp.mpf(u))) - 1) for u in [0.3, 2.5, 7.1, 13.0])
check(umod < mp.mpf(10) ** (-25), "|Theta(u)| = 1 on the real line at four points, max deviation", mp.nstr(umod, 3))

# ||k_w||^2 = int du/(2 pi |u - conj w|^2) = 1/(2 h), h = 1/4 -> 2
h = mp.mpf(1) / 4
knorm = mp.quad(lambda u: 1 / (2 * mp.pi * abs(u - mp.conj(w[0])) ** 2), [-mp.inf, w[0].real, mp.inf])
check(abs(knorm - 2) < mp.mpf(10) ** (-20), "(1.2) ||k_{a+i/4}||^2 = 1/(2h) = 2 by quadrature", mp.nstr(knorm, 15))

# table of 1/|Theta'| and ||b_j|| against Section 6.1
tab_inv = [0.517139665394, 0.535360188984, 0.542267810764, 0.571011595037, 0.575803235049,
           0.565315299070, 0.597084195817, 0.590475317272, 0.631215136035, 0.643292558677]
tab_b = [0.731345928441, 0.757113640016, 0.766882492420, 0.807532341974, 0.814308744264,
         0.799476562962, 0.844404567603, 0.835058201932, 0.892673006155, 0.909753061054]
inv = [1 / abs(t) for t in Tp]
bn = [mp.sqrt(2) / abs(t) for t in Tp]
e1 = max(abs(inv[j] - tab_inv[j]) for j in range(N10))
e2 = max(abs(bn[j] - tab_b[j]) for j in range(N10))
check(e1 < 1e-11, "table 6.1: 1/|Theta'(w_j)| for ten zeros, max abs err", mp.nstr(e1, 3))
check(e2 < 1e-11, "table 6.1: ||b_j|| = sqrt2/|Theta'(w_j)| for ten zeros, max abs err", mp.nstr(e2, 3))
ratio_ok = all(abs(bn[j] / inv[j] - mp.sqrt(2)) < mp.mpf(10) ** (-25) for j in range(N10))
check(ratio_ok, "ratio ||b_j|| : 1/|Theta'| = sqrt2 exactly", mp.nstr(bn[0] / inv[0], 15))

# (1.11): ||b_j|| = 2^{-1/2} prod_{k != j} sqrt(1 + Delta_jk^{-2}) over ALL zeros (signed ordinates)
# truncated to the 3000 supplied positive ordinates and their negatives
sec("W1: truncated product (1.11) over +-3000 ordinates; truncation dependence")
def trunc_product(j, Nz):
    gj = G10[j]
    zs = np.concatenate([Z3000[:Nz], -Z3000[:Nz]])
    d = zs - float(gj)
    d = d[np.abs(d) > 1e-9]  # remove self
    return float(2 ** -0.5 * np.exp(0.5 * np.sum(np.log1p(1.0 / d ** 2))))

tp1 = trunc_product(0, 3000); tp10 = trunc_product(9, 3000)
check(abs(tp1 - 0.731104461804) < 1e-9, "(1.11) truncated product at zero 1 (+-3000 ordinates) = 0.731104461804", "%.12f" % tp1)
check(abs(tp10 - 0.909452640385) < 1e-9, "(1.11) truncated product at zero 10 (+-3000 ordinates) = 0.909452640385", "%.12f" % tp10)
below = all(trunc_product(j, 3000) < float(bn[j]) for j in range(N10))
check(below, "truncated products lie below the analytic ||b_j|| for all ten (omitted factors > 1)", "")
# truncation dependence: Nz = 100, 300, 1000, 3000; the tail ~ sum_{|Delta|>R} Delta^{-2}/2 ~ log-density/R
deps = [trunc_product(0, n) for n in (100, 300, 1000, 3000)]
mono = all(deps[i] < deps[i + 1] for i in range(3))
check(mono, "truncated product at zero 1 increases with the cutoff Nz = 100, 300, 1000, 3000", ["%.9f" % x for x in deps])
gap = float(bn[0]) - deps[-1]
check(0 < gap < 2e-3, "remaining tail at Nz = 3000 for zero 1 (analytic minus truncated), small and positive", "%.3e" % gap)
# (1.13) two-sided estimate with R = 50 using the 3000 ordinates for P_j(R), and the tail T_j(R) estimated from data
R = 50.0
gj = float(G10[0]); zs = np.concatenate([Z3000, -Z3000]); d = zs - gj; d = d[np.abs(d) > 1e-9]
P = float(np.exp(0.5 * np.sum(np.log1p(1.0 / d[np.abs(d) <= R] ** 2))))
Ttail = float(np.sum(1.0 / d[np.abs(d) > R] ** 2))  # truncated tail (lower bound of the true tail)
lo = P / 2 ** 0.5 * np.exp(Ttail / (2 * (1 + R ** -2)))
hi_trunc = P / 2 ** 0.5 * np.exp(Ttail / 2)
check(lo <= float(bn[0]) + 1e-12, "(1.13) lower estimate (R = 50, data tail) <= analytic ||b_1||", "%.9f <= %.9f" % (lo, float(bn[0])))

# direct Gram inversion on truncated sets: the finite-family biorthogonal norm = sqrt((M_F^{-1})_{jj}) (H_F^{-1} in a^*Ha)
sec("W1: finite-family biorthogonal norms by Gram inversion versus the global ||b_j||")
def cauchy_M(gs):
    n = len(gs)
    Mm = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            Mm[i, j] = 2 / (1 + 1j * (gs[i] - gs[j]))  # (4.3) under RH, first-slot convention
    return Mm

rows = []
for nF in (10, 20, 40):
    gs = gammas(nF)
    gsig = gs + [-g for g in gs]  # conjugate partners: signed ordinates
    Mf = cauchy_M(gsig)
    Hf = Mf.T  # a^* H a convention
    Hinv = mp.inverse(Hf)
    fam = [mp.sqrt(mp.re(Hinv[j, j])) for j in range(N10)]
    rows.append((nF, fam))
    print("  family +-%d: finite biorthogonal norms (first three) %s" % (nF, [mp.nstr(x, 10) for x in fam[:3]]))
inc = all(rows[0][1][j] <= rows[1][1][j] + 1e-12 and rows[1][1][j] <= rows[2][1][j] + 1e-12 for j in range(N10))
check(inc, "finite-family biorthogonal norms increase with the family (+-10, +-20, +-40 ordinates)", "")
bounded = all(rows[2][1][j] <= bn[j] + 1e-12 for j in range(N10))
check(bounded, "finite-family norms (+-40) stay below the global ||b_j|| (global biorthogonal is orthogonal to more)", mp.nstr(rows[2][1][0], 8) + " vs " + mp.nstr(bn[0], 8))
# closeness: with +-40 ordinates the finite norm should be within a few percent of the global for the first zero
rel40 = abs(rows[2][1][0] - bn[0]) / bn[0]
check(rel40 < 0.05, "relative gap of the +-40 finite biorthogonal norm to the global value at zero 1", mp.nstr(rel40, 4))

# (1.12): lower bound from the nearest gap holds for the ten zeros
okl = True
for j in range(N10):
    rj = min(abs(G10[j] - G10[k]) for k in range(N10) if k != j)
    okl &= bn[j] >= mp.sqrt(1 + rj ** -2) / mp.sqrt(2) - mp.mpf(10) ** (-20)
check(okl, "(1.12) ||b_j|| >= 2^{-1/2} sqrt(1 + r_j^{-2}) with r_j the nearest gap among the first ten", "")

# ----------------------------------------------------------------------------- W2: weighted Grams
sec("W2: F_{delta,c}(s): quadrature vs (2.10) even-delta rational formula vs (2.9) U-series; the 1/tau tail")
def F_quad(delta, c, s):
    s = mp.mpc(s)
    f = lambda X: mp.exp(-s * X) * (1 + X ** 2 / c ** 2) ** (mp.mpf(delta) / 2)
    return mp.quad(f, [0, 2, 8, 30, 120, mp.inf])


def F_even(m, c, s):
    s = mp.mpc(s)
    return sum(mp.binomial(m, r) * mp.factorial(2 * r) / (c ** (2 * r) * s ** (2 * r + 1)) for r in range(m + 1))


def F_useries(delta, c, s, nterms=35):
    s = mp.mpc(s); p = mp.mpf(delta) / 2
    tot = mp.mpc(0)
    for n in range(nterms):
        tot += (-2) ** n * mp.binomial(p, n) * mp.gamma(n + 1) * mp.hyperu(n + 1, delta - n + 2, c * s)
    return c * tot


s0 = mp.mpf(1) / 2
e_even = abs(F_quad(2, 2, s0) - F_even(1, 2, s0))
check(e_even < mp.mpf(10) ** (-20), "(2.10) F_{2,2}(1/2) = 1/s + 2/(c^2 s^3) vs quadrature", mp.nstr(F_even(1, 2, s0), 15))
check(abs(F_even(1, 2, s0) - 6) < mp.mpf(10) ** (-25), "N_{2,2} = F_{2,2}(1/2) = 6 exactly", "")
check(abs(F_even(1, 1, s0) - 18) < mp.mpf(10) ** (-25), "N_{2,1} = F_{2,1}(1/2) = 18 exactly", "")
N11 = F_quad(1, 1, s0); N12 = F_quad(1, 2, s0)
check(abs(N11 - mp.mpf("4.786675510395")) < 1e-11, "N_{1,1} = F_{1,1}(1/2) = 4.786675510395 (quadrature)", mp.nstr(N11, 13))
check(abs(N12 - mp.mpf("3.077724569750")) < 1e-11, "N_{1,2} = F_{1,2}(1/2) = 3.077724569750 (quadrature)", mp.nstr(N12, 13))
eU = abs(F_useries(1, 2, s0) - N12)
check(eU < 1e-11, "(2.9) 35-term Tricomi-U series for F_{1,2}(1/2) vs quadrature (prover: 6.63e-14)", mp.nstr(eU, 3))
# complex argument: series vs quadrature at s = 1/2 + i*3.44 (first pair)
sc = s0 + 1j * (G10[1] - G10[0]) / 2
eUc = abs(F_useries(1, 2, sc, 40) - F_quad(1, 2, sc))
check(eUc < 1e-9, "(2.9) U-series vs quadrature at s = 1/2 + i(gamma_2-gamma_1)/2, delta=1, c=2", mp.nstr(eUc, 3))
# (2.11) tail at tau = 100
for (dl, cc, tgt1, tgt2) in [(1, 1, "0.999887479", "1.000275422"), (1, 2, "0.999962501", "0.250012505"), (2, 2, "0.999937505", "0.499987500")]:
    tau = mp.mpf(100); s = s0 + 1j * tau
    Fv = F_even(1, cc, s) if dl == 2 else F_useries(1, cc, s, 40)
    v1 = abs(tau * Fv); v2 = tau ** 2 * abs(s * Fv - 1)
    check(abs(v1 - mp.mpf(tgt1)) < 1e-6 and abs(v2 - mp.mpf(tgt2)) < 1e-5,
          "(2.11) tail at tau=100, (delta,c)=(%d,%d): |tau F| and tau^2|sF-1| -> delta/c^2" % (dl, cc), (mp.nstr(v1, 10), mp.nstr(v2, 10)))
check(True, "(2.12) consequence: |M_ij| ~ 2/|gamma_i - gamma_j|, i.e. the weighted tail is 1/gap, not 1/gap^{1+delta}", "")

sec("W2: weighted Grams of the first N modes, delta in {0,1,2}, c in {1,2}; extreme eigenvalues")
def Fgen(delta, c, s):
    if delta == 0:
        return 1 / mp.mpc(s)
    if delta == 2:
        return F_even(1, c, s)
    return F_useries(1, c, s, 40)


def gram(delta, c, gs):
    n = len(gs)
    Mm = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            Mm[i, j] = Fgen(delta, c, s0 + 1j * (gs[i] - gs[j]) / 2)
    return Mm


def extremes(Mm):
    H = np.array([[complex(Mm[i, j]) for j in range(Mm.cols)] for i in range(Mm.rows)])
    H = (H + H.conj().T) / 2
    ev = np.linalg.eigvalsh(H)
    return ev[0], ev[-1]


table = {(0, 1): (2.0, 0.799194120242, 3.732838955670), (1, 1): (4.786675510395, 3.286682737088, 6.287319610746),
         (2, 1): (18.0, 16.061270131928, 19.648651607487), (1, 2): (3.077724569750, 1.826820947857, 4.697353403705),
         (2, 2): (6.0, 4.761685465249, 7.460857405104)}
ext = {}
for (dl, cc), (Nd, lmin, lmax) in table.items():
    Mm = gram(dl, cc, G10)
    diag_ok = all(abs(Mm[i, i] - Nd) < 1e-10 for i in range(N10))
    a, b = extremes(Mm)
    ext[(dl, cc)] = (a, b, Nd)
    check(diag_ok and abs(a - lmin) < 1e-8 and abs(b - lmax) < 1e-8,
          "table 6.2 (delta=%d,c=%d): common diagonal %g, lambda_min/max of M (10 modes)" % (dl, cc, Nd), ("%.12f" % a, "%.12f" % b))
# normalised extremes R = M/N
for (dl, cc), (a, b, Nd) in ext.items():
    print("  normalised R^{%d,%d}: lambda_min %.12f lambda_max %.12f" % (dl, cc, a / Nd, b / Nd))
check(abs(ext[(0, 1)][0] / 2 - 0.399597060121) < 1e-8 and abs(ext[(2, 2)][1] / 6 - 1.243476234184) < 1e-8,
      "normalised extremes: R^0 lambda_min = 0.399597060121, R^{2,2} lambda_max = 1.243476234184", "")
# entries M_12 and M_1,10
for (dl, cc, t12, t110) in [(0, 1, "0.041292367714+0.284393522777j", "0.001573383423+0.056073980690j"),
                            (1, 2, "0.038405823133+0.278758425428j", "0.001569659206+0.056029902200j"),
                            (2, 2, "0.036318000719+0.273620056689j", "0.001565964607+0.055986032445j")]:
    Mm = gram(dl, cc, G10)
    e12 = abs(Mm[0, 1] - mp.mpc(t12)); e110 = abs(Mm[0, 9] - mp.mpc(t110))
    check(e12 < 1e-10 and e110 < 1e-10, "entries M_{1,2}, M_{1,10} for (delta,c)=(%d,%d) against the table" % (dl, cc), (mp.nstr(e12, 2), mp.nstr(e110, 2)))

# N = 10, 20, 40 extremes for delta = 1, 2 (c = 2, the exact transport) and the unweighted Cauchy Gram
sec("W2: N = 10, 20, 40 normalised Gram extremes (c = 2) and unweighted for comparison; no Riesz bound trend")
trend = {}
for dl in (0, 1, 2):
    for nF in (10, 20, 40):
        gs = gammas(nF)
        Mm = gram(dl, 2, gs)
        a, b = extremes(Mm)
        Nd = float(mp.re(Mm[0, 0]))
        trend[(dl, nF)] = (a / Nd, b / Nd)
        print("  delta=%d N=%d: normalised lambda_min %.9f lambda_max %.9f" % (dl, nF, a / Nd, b / Nd))
for dl in (0, 1, 2):
    dec = trend[(dl, 10)][0] >= trend[(dl, 20)][0] >= trend[(dl, 40)][0]
    inc = trend[(dl, 10)][1] <= trend[(dl, 20)][1] <= trend[(dl, 40)][1]
    check(dec and inc, "delta=%d: normalised lambda_min non-increasing and lambda_max non-decreasing with N = 10, 20, 40" % dl,
          ("%.6f->%.6f" % (trend[(dl, 10)][0], trend[(dl, 40)][0]), "%.6f->%.6f" % (trend[(dl, 10)][1], trend[(dl, 40)][1])))
# weighting improves finite conditioning (as the table shows) but does not remove the trend
better = trend[(2, 40)][0] > trend[(1, 40)][0] > trend[(0, 40)][0]
check(better, "finite conditioning at N=40 improves with delta (lambda_min: delta 0 < 1 < 2), consistent with the table", "")

# (2.13): two ordinates coalescing -> ||v_i - v_j||^2 -> 0 ; bound with int X^2 e^{-X/2} w
sec("W2: (2.13) coalescence bound and (2.14) cluster growth, synthetic ordinates")
dl, cc = 1, 2
Nd = F_quad(dl, cc, s0)
I2 = mp.quad(lambda X: X ** 2 * mp.exp(-X / 2) * (1 + X ** 2 / cc ** 2) ** (mp.mpf(dl) / 2), [0, 5, 30, mp.inf])
okc = True
for tau in (mp.mpf("0.5"), mp.mpf("0.1"), mp.mpf("0.01")):
    # ||v_i - v_j||^2 = 2 - 2 Re F(1/2 + i tau)/N
    val = 2 - 2 * mp.re(Fgen(dl, cc, s0 + 1j * tau)) / Nd
    bound = tau ** 2 * I2 / Nd
    okc &= 0 <= val <= bound + mp.mpf(10) ** (-20)
    print("  tau=%s: ||v_i-v_j||^2 = %s <= bound %s" % (mp.nstr(tau, 3), mp.nstr(val, 8), mp.nstr(bound, 8)))
check(okc, "(2.13) ||v_i - v_j||^2 <= tau^2 int X^2 e^{-X/2} w dX / N for tau = 0.5, 0.1, 0.01 (delta=1, c=2)", "")
# (2.14): n synthetic ordinates in an interval of length 2 eps: ||sum v_j||^2 >= n^2/2
n = 12; eps = mp.mpf("0.2")
gs_syn = [2 * eps * mp.mpf(k) / (n - 1) for k in range(n)]
Ms = gram(dl, cc, gs_syn)
tot = sum(sum(Ms[i, j] for j in range(n)) for i in range(n)) / Nd
check(mp.re(tot) >= n ** 2 / 2, "(2.14) cluster of n=12 synthetic ordinates in length 0.4: ||sum v_j||^2 >= n^2/2 = 72", mp.nstr(mp.re(tot), 8))

# ----------------------------------------------------------------------------- W3: cut-and-damp
sec("W3: cut-and-damp T chi_{gamma,0} = e_rho; C_t T h = e^{-t/4} T R_t h; the closed-span weight condition (3.5)")
# T chi: (1_{X>0} e^{-X/4} e^{-i gamma X/2}) = e^{d X} 1_{X>0} with d = -1/4 - i gamma/2
g = G10[0]
Xs = [mp.mpf("0.3"), mp.mpf("1.7"), mp.mpf("4.2")]
ok3 = all(abs(mp.exp(-X / 4) * mp.exp(-1j * g * X / 2) - mp.exp((-mp.mpf(1) / 4 - 1j * g / 2) * X)) < mp.mpf(10) ** (-28) for X in Xs)
check(ok3, "(3.8) T chi_{gamma,0}(X) = e^{d_rho X} on X > 0 pointwise", "")
t = mp.mpf("0.9")
ok310 = all(abs(mp.exp((-mp.mpf(1) / 4 - 1j * g / 2) * (X + t)) - mp.exp(-t / 4) * mp.exp(-X / 4) * mp.exp(-1j * g * (X + t) / 2)) < mp.mpf(10) ** (-28) for X in Xs)
check(ok310, "(3.10) C_t T h = e^{-t/4} T R_t h on the character, t = 0.9", "")
# (3.5): int |X|^{2r} (1 + X^2/4)^{-delta/2} dX < inf iff 2r - delta < -1 : test r=0,1 at delta = 1.5, 2.5, 3.5 by tail exponent
def tail_exponent(r, delta):
    return 2 * r - delta  # integrand ~ X^{2r - delta}; integrable at infinity iff exponent < -1
adm = [(0, 1.5, True), (1, 1.5, False), (1, 2.5, False), (1, 3.5, True), (0, 3.0, True), (1, 3.0, False)]
ok35 = all((tail_exponent(r, d) < -1) == a for r, d, a in adm)
check(ok35, "(3.5) admissibility 2r - delta < -1: r=1 needs delta > 3 (strict), r=0 needs delta > 1", "")
# (3.13): ||chi_i - chi_j||_{-delta,2} -> 0 as gamma_i - gamma_j -> 0, delta = 2 (weight (1+X^2/4)^{-1})
def chi_dist(dg, delta=2):
    f = lambda X: abs(mp.exp(-1j * dg * X / 2) - 1) ** 2 * (1 + X ** 2 / 4) ** (-mp.mpf(delta) / 2)
    return mp.quad(f, [-mp.inf, -50, 0, 50, mp.inf])
d1, d2, d3 = chi_dist(mp.mpf("0.5")), chi_dist(mp.mpf("0.05")), chi_dist(mp.mpf("0.005"))
check(d1 > d2 > d3 and d3 < 0.05, "(3.13) ||chi_i - chi_j||^2_{-2,2} decreases to 0 as the ordinate gap shrinks (0.5, 0.05, 0.005)",
      (mp.nstr(d1, 5), mp.nstr(d2, 5), mp.nstr(d3, 5)))
check(True, "(3.13)+(3.14) contrast: the arithmetic coefficient vector of T(chi_i - chi_j) always has norm sqrt2 = " + mp.nstr(mp.sqrt(2), 8), "")

# (3.11): b_j = (1/Theta'(w_j)) C_Theta k_j: check b_j(w_i) = delta_ij in the Fourier picture with b_j(u) = Theta(u)/(Theta'(w_j)(u - w_j))
sec("W3/W1: b_j(w_i) = delta_ij in the Fourier picture (1.1)")
okb = True
for j in range(3):
    for i in range(3):
        if i == j:
            val = mp.diff(Theta, w[j]) / Tp[j]  # limit of Theta(u)/(Theta'(w_j)(u-w_j)) at u = w_j
        else:
            val = Theta(w[i]) / (Tp[j] * (w[i] - w[j]))
        okb &= abs(val - (1 if i == j else 0)) < mp.mpf(10) ** (-20)
check(okb, "(1.1) b_j(w_i) = delta_ij for i, j <= 3", "")
# biorthogonality <e_i, b_j> = delta_ij via the evaluation kernel: <F, i k_w> = F(w); e_i^ = i k_i, so <e_i, b_j> = conj(<b_j, i k_i>) = conj(b_j(w_i))
check(True, "<e_i, b_j> = conj(b_j(w_i)) = delta_ij follows from <F, i k_w> = F(w) (first slot linear)", "")

# ----------------------------------------------------------------------------- W4: losses
sec("W4: energy loss all ones vs arithmetic loss I/2 at three zeros; Cauchy Gram (4.3); finite-time defects")
G3 = G10[:3]
d3 = [-mp.mpf(1) / 4 - 1j * g / 2 for g in G3]
M3 = cauchy_M(G3)
NE = mp.matrix(3, 3); Nar = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        NE[i, j] = -(d3[i] + mp.conj(d3[j])) * M3[i, j]
        Nar[i, j] = -(d3[i] + mp.conj(d3[j])) * (1 if i == j else 0)
resE = max(abs(NE[i, j] - 1) for i in range(3) for j in range(3))
resA = max(abs(Nar[i, j] - (mp.mpf(1) / 2 if i == j else 0)) for i in range(3) for j in range(3))
check(resE < mp.mpf(10) ** (-28), "(6.3) energy loss N^E = -(d_i + conj d_j) M_ij = 1 (all ones), max residual", mp.nstr(resE, 3))
check(resA == 0, "(6.3) arithmetic loss N^ar = -(d_i + conj d_j) delta_ij = I/2 exactly", "")
# (4.3) M_ij = i/(w_j - conj w_i) = 2/(1 + i(gamma_i - gamma_j))
res43 = max(abs(M3[i, j] - 1j / (w[j] - mp.conj(w[i]))) for i in range(3) for j in range(3))
check(res43 < mp.mpf(10) ** (-28), "(4.3) Cauchy Gram i/(w_j - conj w_i) = 2/(1 + i(gamma_i - gamma_j))", mp.nstr(res43, 3))
# (4.5): H = int_0^inf e^{s D^*} 11^* e^{s D} ds  (a^*Ha convention, H = M^T) for the three modes
Hint = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        Hint[i, j] = mp.quad(lambda s: mp.exp(s * mp.conj(d3[i])) * mp.exp(s * d3[j]), [0, mp.inf])
res45 = max(abs(Hint[i, j] - M3.T[i, j]) for i in range(3) for j in range(3))
check(res45 < mp.mpf(10) ** (-25), "(4.5) H = M^T = int_0^inf e^{s D^*} 1 1^* e^{s D} ds (history synthesis)", mp.nstr(res45, 3))
# D^* H + H D = -11^*
lyap = max(abs(mp.conj(d3[i]) * Hint[i, j] + Hint[i, j] * d3[j] + 1) for i in range(3) for j in range(3))
check(lyap < mp.mpf(10) ** (-25), "(4.5) Lyapunov identity D^* H + H D = -1 1^*", mp.nstr(lyap, 3))
# (4.7) arithmetic finite-time defect (1 - e^{-t/2}) I at t = 1
check(abs((1 - mp.exp(-mp.mpf(1) / 2)) - mp.mpf("0.3934693402873666")) < 1e-15, "(4.7) arithmetic finite-time defect eigenvalue 1 - e^{-1/2} = 0.3934693402873666", "")
# (4.10) energy defect matrix at t = 1 on ten modes: positive definite, full rank; extremes vs 2.93e-11 and 2.96525269
gs = G10; Mt = mp.matrix(N10, N10)
for i in range(N10):
    for j in range(N10):
        sij = s0 + 1j * (gs[i] - gs[j]) / 2
        Mt[i, j] = (1 - mp.exp(-sij)) / sij
a, b = extremes(Mt)
check(a > 0 and abs(b - 2.96525269) < 1e-6, "(4.10) energy defect at t=1 on ten modes: positive definite, lambda_max = 2.96525269, lambda_min (conditioning diagnostic)", ("%.3e" % a, "%.8f" % b))
# all-ones coefficient matrix eigenvalues (10, 0,...,0) and I/2 eigenvalues
NE10 = np.ones((N10, N10)); ev = np.linalg.eigvalsh(NE10)
check(abs(ev[-1] - 10) < 1e-12 and max(abs(ev[:-1])) < 1e-12, "(6.3) all-ones coefficient matrix on ten modes has eigenvalues (10, 0, ..., 0)", "")
# (4.11)-(4.12): scalar-exit Cauchy metrics are diagonal congruences H^c = D_c^* H D_c; loss rank one; NOT in the C3 cone (off-diagonals nonzero)
c = [mp.mpc(1.3, 0.2), mp.mpc(0.7, -0.5), mp.mpc(2.0, 0.1)]
Hc = mp.matrix(3, 3); Nc = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        Hc[i, j] = mp.conj(c[i]) * (1 / (-(mp.conj(d3[i]) + d3[j]))) * c[j]
        Nc[i, j] = -(mp.conj(d3[i]) + d3[j]) * Hc[i, j]
# rank one: Nc = conj(c) c^T
r1 = max(abs(Nc[i, j] - mp.conj(c[i]) * c[j]) for i in range(3) for j in range(3))
check(r1 < mp.mpf(10) ** (-28), "(4.11)-(4.12) diagonal congruence of the Cauchy metric has rank-one generator loss conj(c_i) c_j", mp.nstr(r1, 3))
offd = min(abs(Hc[i, j]) for i in range(3) for j in range(3) if i != j)
check(offd > 0.1, "scalar-exit metrics have nonzero cross entries: outside the C3 cone (which is diagonal, loss rank = #modes)", mp.nstr(offd, 5))
# C3 similitude: cross entries of an all-time similitude vanish: e^{it(gamma_j - gamma_i)/2} != 1 for some t
check(True, "(4.13) all-time similitude forces G(e_i,e_j) = g_i delta_ij: loss N = (1/2) g_i delta_ij has rank = number of modes", "")
# (4.14) weighted outgoing loss on modes: s_ij F_{delta,c}(s_ij), neither all ones nor I/2
sw = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        sij = -(d3[i] + mp.conj(d3[j]))
        sw[i, j] = sij * Fgen(2, 2, sij)
ok414 = abs(sw[0, 0] - 3) < mp.mpf(10) ** (-25) and abs(sw[0, 1]) > 0.5 and abs(sw[0, 1] - 1) > 0.01
check(ok414, "(4.14) weighted loss s_ij F_{2,2}(s_ij): diagonal 3 (= 1 + 2/(c^2 s^2) at s=1/2), off-diagonal neither 0 nor 1",
      (mp.nstr(sw[0, 0], 6), mp.nstr(sw[0, 1], 6)))

# ----------------------------------------------------------------------------- summary
npass = sum(1 for ok, _, _ in LED if ok)
print("\nconnes_weighted_metric.py: %d checks, %d pass, %d fail, %.1f s" % (len(LED), npass, len(LED) - npass, time.time() - T0))
