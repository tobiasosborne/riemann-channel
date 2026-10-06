#!/usr/bin/env python3
"""Checks for 'The local Fourier-gate phases and the root number' (notes/adelic-gkp/gate-phases.md), lane I, 2026-10-06.

K = Q(sqrt(-7)), pi = sqrt(-7) (embedded as i*sqrt7), w = (1 + pi)/2. Elements of K are stored as pairs (X, Y) of Fractions
meaning (X + Y*pi)/2; Tr = X, N = (X^2 + 7 Y^2)/4.
Additive characters (as in adelic-gkp.md): psi_inf(x) = exp(-2 pi i x), psi_p(x) = exp(2 pi i {x}_p); on K: psi o Tr.
Self-dual measures: at the complex place 2 dx dy (for exp(-4 pi i Re(z w))); at a finite place vol(O_v) = N(different)^(-1/2).
Unitary Hecke character of 49a1: psi_u((alpha)) = eps(alpha) alpha / |alpha|, eps the Legendre symbol mod pi.
Its local components (derived on the page, checked in B1): psi_inf(z) = |z|/z; psi_7 = eps on units, psi_7(pi) = i;
psi_v(uniformiser) = psi_u(p_v) at the other places. 441d1: psi' = psi * (chi_{-3} o N).
Local epsilon factor at s: Z(Phi^, chi^-1, 1-s) = eps(s) * Z(Phi, chi, s) when both local L-factors are 1;
at infinity the Gamma-factor ratio is divided out. Needs PARI/GP (/usr/bin/gp) with elldata; runs in about 20 s.
"""
import cmath
import math
import subprocess
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
import sympy

mp.mp.dps = 50
npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


def gp(script):
    r = subprocess.run(["gp", "-q", "-f"], input="\\p 38\ndefault(colors,\"no\");\n" + script + "\nquit\n",
                       capture_output=True, text=True, timeout=600)
    out = {}
    for line in r.stdout.splitlines():
        if line.startswith("@"):
            k, v = line[1:].split(" ", 1)
            out[k] = v.strip()
    return out


def pnum(s):
    s = s.replace(" ", "").replace("E", "e").replace("*I", "j")
    if "j" in s:
        return complex(s.replace("+-", "-"))
    return float(s)


def digits(err, scale=1.0):
    return -math.log10(max(err, 1e-300) / scale)


def leg(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


# ---- arithmetic in K = Q(sqrt(-7)), elements (X, Y) = (X + Y pi)/2 --------------------------------
def kmul(a, b):
    return ((a[0] * b[0] - 7 * a[1] * b[1]) / 2, (a[0] * b[1] + a[1] * b[0]) / 2)


def kconj(a):
    return (a[0], -a[1])


def knorm(a):
    return (a[0] ** 2 + 7 * a[1] ** 2) / 4


def kc(a):                       # complex embedding, pi -> i sqrt 7
    return complex(float(a[0]) / 2, float(a[1]) * math.sqrt(7) / 2)


def kint(a):                     # a in O_K ?
    return a[0].denominator == 1 and a[1].denominator == 1 and (a[0] - a[1]) % 2 == 0


def kdiv_int(a, n):
    return (a[0] / n, a[1] / n)


PI = (Fr(0), Fr(2))
assert kmul(PI, kconj(PI)) == (Fr(14), Fr(0))         # pi * pibar = 7, stored as (14, 0)
PIINV = kdiv_int(kconj(PI), 7)                          # 1/pi = pibar/7 = -pi/7


def pik(k):
    """pi^k as (X, Y)"""
    r = (Fr(2), Fr(0))
    for _ in range(abs(k)):
        r = kmul(r, PI if k > 0 else PIINV)
    return r


def eps7(a):                     # Legendre symbol of (a mod pi), a in O_K; a = (X + Y pi)/2 = X/2 mod pi
    return leg(int(a[0]), 7)     # (2/7) = 1


def psi_tr(a):                   # finite-place additive character psi_p(Tr a) for a with p-power denominators
    return cmath.exp(2j * math.pi * float(a[0] % 1))


print("== A  root numbers from PARI: global, local over Q, and the L-functions")
A = gp(r"""
E=ellinit("49a1"); F=ellinit("441d1");
print("@g1 ",ellrootno(E)); print("@g2 ",ellrootno(F));
print("@l1 ",[ellrootno(E,0),ellrootno(E,3),ellrootno(E,7)]); print("@l2 ",[ellrootno(F,0),ellrootno(F,3),ellrootno(F,7)]);
print("@r1 ",lfunrootres(lfuncreate(E))[3]); print("@r2 ",lfunrootres(lfuncreate(F))[3]);
print("@a1 ",[ellak(E,3),ellak(E,9),ellak(E,27),ellak(E,81)]); print("@a2 ",[ellak(F,3),ellak(F,9),ellak(F,27),ellak(F,81),ellak(F,729)]);
print("@N ",[ellglobalred(E)[1],ellglobalred(F)[1]]);
""")
g1, g2 = int(A["g1"]), int(A["g2"])
l1 = [int(x) for x in A["l1"].strip("[]").split(",")]
l2 = [int(x) for x in A["l2"].strip("[]").split(",")]
check("A1 ellrootno: 49a1 has W = +1, 441d1 has W = -1; lfunrootres agrees",
      g1 == 1 and g2 == -1 and A["r1"] == "1" and A["r2"] == "-1", f"ellrootno {g1}, {g2}; lfunrootres {A['r1']}, {A['r2']}")
check("A2 local root numbers over Q [w_inf, w_3, w_7]: 49a1 [-1, +1, -1], 441d1 [-1, -1, -1]",
      l1 == [-1, 1, -1] and l2 == [-1, -1, -1], f"49a1 {l1}, 441d1 {l2}")
check("A3 Euler factor at 3: 49a1 a_9 = -3 (the inert step, factor (1 + 3^(1-2s))^-1); 441d1 a_(3^k) = 0 (factor 1)",
      A["a1"] == "[0, -3, 0, 9]" and A["a2"] == "[0, 0, 0, 0, 0]", f"49a1 {A['a1']}, 441d1 {A['a2']}; conductors {A['N']}")

# -----------------------------------------------------------------------------------------------
print("== B  the local components of psi and the gate phases of 49a1 (places of K)")


def split_prime_element(p):
    """generator pi_p = (x + y sqrt-7)/2 of a prime above split p, with eps(pi_p) = +1 (the value psi(p))"""
    for y in range(1, int(math.isqrt(4 * p // 7)) + 2):
        r = 4 * p - 7 * y * y
        if r > 0 and math.isqrt(r) ** 2 == r:
            x = math.isqrt(r)
            el = (Fr(x), Fr(y))
            if eps7(el) == -1:
                el = (-el[0], -el[1])
            return el
    raise ValueError(p)


def psi_components(alpha, chi7_pi):
    """returns (unramified part, psi_7(alpha), psi_inf(alpha)) for alpha in O_K - {0}, using the
    ideal factorisation of alpha; chi7_pi is the value assigned to psi_7(pi)"""
    n = int(knorm(alpha))
    unram = 1 + 0j
    rest = alpha
    for p, e in sympy.factorint(n).items():
        if p == 7:
            continue
        if leg(-7, p) == 1 or p == 2:                     # split (2 splits: -7 = 1 mod 8)
            for el in (split_prime_element(p), None):
                if el is None:
                    el = kconj(split_prime_element(p))
                    el = el if eps7(el) == 1 else (-el[0], -el[1])
                while True:
                    q = kdiv_int(kmul(rest, kconj(el)), p)
                    if not kint(q):
                        break
                    rest = q
                    unram *= kc(el) / math.sqrt(p)
        else:                                             # inert: psi((p)) = eps(p) p = -p
            for _ in range(e // 2):
                rest = kdiv_int(rest, p)
                unram *= -1
    k = 0
    while True:
        q = kdiv_int(kmul(rest, kconj(PI)), 7)
        if not kint(q):
            break
        rest, k = q, k + 1
    assert knorm(rest) in (1,), (alpha, rest)            # rest is a unit +-1
    beta = kmul(pik(-k), alpha)                           # alpha / pi^k, a unit at 7
    psi7 = chi7_pi ** k * eps7(beta)
    a = kc(alpha)
    return unram, psi7, abs(a) / a


rng = np.random.default_rng(7)
alphas = [(Fr(0), Fr(2)), (Fr(14), Fr(0)), (Fr(-14), Fr(0)), (Fr(1), Fr(1))]
while len(alphas) < 300:
    X, Y = (int(v) for v in rng.integers(-60, 61, 2))
    if (X - Y) % 2 == 0 and (X, Y) != (0, 0):
        alphas.append((Fr(X), Fr(Y)))
alphas.append(kmul(kmul(PI, PI), kmul(PI, (Fr(3), Fr(1)))))
err_i = max(abs(np.prod(psi_components(a, 1j)) - 1) for a in alphas)
bad_mi = sum(abs(np.prod(psi_components(a, -1j)) - 1) > 1e-9 for a in alphas)
check("B1 the idele class character is trivial on K^x with psi_inf(z) = |z|/z, psi_7 = eps on units, psi_7(sqrt-7) = i "
      "(301 elements, unramified part from the prime factorisation)", err_i < 1e-12,
      f"max |prod_v psi_v(alpha) - 1| = {err_i:.1e}; with psi_7(sqrt-7) = -i instead, {bad_mi} of {len(alphas)} fail")

g7 = mp.fsum(leg(u, 7) * mp.expj(2 * mp.pi * u / 7) for u in range(1, 7))
check("B2 Gauss sum at 7: sum_u (u/7) e^(2 pi i u/7) = i sqrt 7", abs(g7 - 1j * mp.sqrt(7)) < mp.mpf(10) ** -45,
      f"|difference| = {mp.nstr(abs(g7 - 1j * mp.sqrt(7)), 3)}")


def fourier_finite(Phi, reps, volM, y):
    """Phi^(y) = vol(p^M O) * sum_{x in O/p^M O} Phi(x) psi(Tr(x y)); valid when p^M O * y lies in the dual of O"""
    return volM * sum(Phi(x) * psi_tr(kmul(x, y)) for x in reps)


def Phi7(x):                     # charged state at 7: eps(x) 1_{O^x}(x); x in O_K given as (X, Y)
    return eps7(x) if kint(x) and int(x[0]) % 7 else 0


reps7 = [(Fr(2 * a + b), Fr(b)) for a in range(7) for b in range(7)]          # O / 7O = O / p^2
vol7 = 7 ** -0.5 * 7 ** -2                                                     # vol(p^2 O_7), vol(O_7) = 7^(-1/2)
maxerr, nonzero = 0.0, 0
for t in reps7:                  # y = t pi / 49 = t / pi^3 runs over p^-3 / p^-1 (Phi^ is p^-1-periodic)
    y = kdiv_int(kmul(t, PI), 49)
    lhs = fourier_finite(Phi7, reps7, vol7, y)
    sev = kmul(t, PI)                                                          # 7y = t pi / 7 = -t/pi
    sev = kdiv_int(sev, 7)
    rhs = 1j / 7 * (Phi7(sev) if kint(sev) else 0)                             # i * D_7 Phi (y) = i 7^(-1) Phi(7y)
    maxerr = max(maxerr, abs(lhs - rhs))
    nonzero += abs(rhs) > 0
check("B3 Fourier gate at 7: F[eps 1_{O^x}] = i * D_7[eps 1_{O^x}], D_7 f(y) = |7|^(1/2) f(7y), on all of p^-3/p^-1 "
      "(support on the shell v = -2 only)", maxerr < 1e-12 and nonzero == 6, f"max |diff| = {maxerr:.1e}, {nonzero} nonzero classes of 49")


def zeta_K7(f, chi_pi, s, shells=range(-3, 3)):
    units = [(Fr(2 * u), Fr(0)) for u in range(1, 7)]
    tot = 0
    for k in shells:
        for u in units:
            x = kmul(pik(k), u)
            tot += f(x) * chi_pi ** k * eps7(u) * 7.0 ** (-k * s) / 6
    return tot


def Phi7hat(y):
    return fourier_finite(Phi7, reps7, vol7, y)


for s in (0.5, 0.3 + 0.7j, 1.7 - 0.4j):
    Z1 = zeta_K7(Phi7, 1j, s)
    Z2 = zeta_K7(Phi7hat, -1j, 1 - s)
    pred = 1j * 49 ** (0.5 - s)
    check(f"B4 local functional equation at 7, s = {s}: Z(Phi^, chi^-1, 1-s) / Z(Phi, chi, s) = i * 49^(1/2 - s)",
          abs(Z2 / Z1 - pred) < 1e-12 * abs(pred), f"ratio {complex(Z2 / Z1):.12f}, |diff| = {abs(Z2 / Z1 - pred):.1e}")
eps_7 = 1j

# complex place
h = 0.0125
xs = np.arange(-4.5, 4.5 + h / 2, h)
Xg, Yg = np.meshgrid(xs, xs, indexing="ij")
Zg = Xg + 1j * Yg
G = np.exp(-2 * np.pi * np.abs(Zg) ** 2)
errF = 0.0
for wpt in (0.3 + 0.2j, -0.5 + 0.1j, 0.1 - 0.7j, 0.6 + 0.45j):
    val = np.sum(Zg * G * np.exp(-4j * np.pi * np.real(Zg * wpt))) * 2 * h * h
    pred = -1j * np.conj(wpt) * np.exp(-2 * np.pi * abs(wpt) ** 2)
    errF = max(errF, abs(val - pred))
check("B5 Fourier gate at the complex place (kernel exp(-4 pi i Re zw), measure 2dxdy): F[z e^(-2pi|z|^2)] = -i * zbar e^(-2pi|z|^2)",
      errF < 1e-12, f"max |diff| at 4 points = {errF:.1e}")
Ge = np.exp(-np.pi * np.abs(Zg) ** 2)
errE = 0.0
for wpt in (0.3 + 0.2j, -0.5 + 0.1j):
    val = np.sum(Zg * Ge * np.exp(-2j * np.pi * (Xg * wpt.real + Yg * wpt.imag))) * h * h
    errE = max(errE, abs(val - (-1j) * wpt * np.exp(-np.pi * abs(wpt) ** 2)))
check("B5 same state in the Euclidean picture of two real modes (kernel exp(-2 pi i (xu + yv))): F[z e^(-pi|z|^2)] = -i z e^(-pi|z|^2), "
      "the Hermite phase (-i)^1", errE < 1e-12, f"max |diff| = {errE:.1e}")

mp.mp.dps = 25


def Zinf(f, chi, s):
    """int_C f(z) chi(z) |z|_C^s d^x z, d^x z = 2 dx dy / |z|^2, |z|_C = |z|^2"""
    def integrand(r, th):
        z = r * mp.expj(th)
        return f(z) * chi(z) * r ** (2 * s) * 2 / r
    return mp.quad(integrand, [0, 1, mp.inf], [0, mp.pi, 2 * mp.pi])


fz = lambda z: z * mp.exp(-2 * mp.pi * abs(z) ** 2)
fzhat = lambda z: -1j * mp.conj(z) * mp.exp(-2 * mp.pi * abs(z) ** 2)
chi_inf = lambda z: abs(z) / z
chi_inf_inv = lambda z: z / abs(z)
Linf = lambda s: 2 * (2 * mp.pi) ** (-(s + mp.mpf(1) / 2)) * mp.gamma(s + mp.mpf(1) / 2)   # Gamma_C(s + 1/2)
for s in (mp.mpf(1) / 2, mp.mpc(0.3, 0.7)):
    Z1 = Zinf(fz, chi_inf, s)
    Z2 = Zinf(fzhat, chi_inf_inv, 1 - s)
    epsv = Z2 / Z1 * Linf(s) / Linf(1 - s)
    check(f"B6 local functional equation at infinity, s = {mp.nstr(s, 3)}: eps_inf = Z(Phi^, chi^-1, 1-s) L(s) / (Z(Phi, chi, s) L(1-s)) = -i",
          abs(epsv + 1j) < mp.mpf(10) ** -18, f"eps = {mp.nstr(epsv, 15)}, |diff| = {mp.nstr(abs(epsv + 1j), 2)}")
wrong = Zinf(fz, chi_inf_inv, mp.mpf(1) / 2)
check("B6 sector selection: z e^(-2pi|z|^2) has zero overlap with the opposite character z/|z|", abs(wrong) < mp.mpf(10) ** -18,
      f"|Z| = {mp.nstr(abs(wrong), 2)}")
eps_inf = -1j

W1 = eps_inf * eps_7
check("B7 49a1: product of the local gate phases over the places of K = (-i)(i) = +1 = ellrootno(49a1)", abs(W1 - g1) < 1e-15,
      f"product = {W1}")

# -----------------------------------------------------------------------------------------------
print("== C  the twist by -3: the local state at 3 (K_3 = Q_9, 3 inert in K)")
reps3 = [(Fr(2 * a + b), Fr(b)) for a in range(3) for b in range(3)]           # O/3O = F_9
units3 = [u for u in reps3 if int(knorm(u)) % 3]
eta = lambda x: leg(int(knorm(x)), 3)                                          # (N x / 3) on O_3^x


def red3(x):
    a, b = int((x[0] - x[1]) / 2) % 3, int(x[1]) % 3
    return (Fr(2 * a + b), Fr(b))


mult_ok = all(eta(kmul(a, b)) == eta(a) * eta(b) for a in units3 for b in units3)
kernel = sum(eta(u) == 1 for u in units3)
squares = {red3(kmul(u, u)) for u in units3}
check("C1 eta(x) = (N x / 3) is the quadratic character of F_9^x = (O_K/3)^x (multiplicative, kernel = the 4 squares)",
      mult_ok and kernel == 4 and all(eta(s_) == 1 for s_ in squares) and len(squares) == 4, f"kernel size {kernel}")
g9 = mp.fsum(eta(u) * mp.expj(2 * mp.pi * mp.mpf(int(u[0])) / 3) for u in units3)
g3 = mp.fsum(leg(u, 3) * mp.expj(2 * mp.pi * u / 3) for u in (1, 2))
check("C2 Gauss sums: g(F_3) = sum (u/3) e^(2pi i u/3) = i sqrt3; g(F_9, eta) = 3; Hasse-Davenport g(F_9) = -g(F_3)^2",
      abs(g3 - 1j * mp.sqrt(3)) < 1e-20 and abs(g9 - 3) < 1e-20 and abs(g9 + g3 ** 2) < 1e-20,
      f"g3 = {mp.nstr(g3, 12)}, g9 = {mp.nstr(g9, 12)}")


def Phi3(x):                     # charged state at 3: eta(x) 1_{O^x}
    return eta(x) if kint(x) and int(knorm(x)) % 3 else 0


def one3(x):                     # vacuum 1_{O_3}
    return 1 if kint(x) else 0


reps9 = [(Fr(2 * a + b), Fr(b)) for a in range(9) for b in range(9)]          # O/9O
maxerr = 0.0
maxerr_vac = 0.0
nz = 0
for t in reps9:                  # y = t/27 runs over 3^-3 O / 3^-1 O ... use O/9O reps: y = t/9 in 3^-2 O mod O
    y = kdiv_int(t, 9)
    lhs = fourier_finite(Phi3, reps9, 1 / 81, y)                               # vol(9 O_3) = 1/81, vol(O_3) = 1
    ty = kdiv_int(t, 3)
    rhs = (1 / 3) * (Phi3(ty) if kint(ty) else 0)                              # D_3 Phi(y) = |3|^(1/2) Phi(3y), |3| = 1/9
    maxerr = max(maxerr, abs(lhs - rhs))
    nz += abs(rhs) > 0
    lv = fourier_finite(one3, reps9, 1 / 81, y)
    maxerr_vac = max(maxerr_vac, abs(lv - (1 if kint(y) else 0)))
check("C3 Fourier gate at 3: F[eta 1_{O^x}] = + D_3[eta 1_{O^x}] on 3^-2 O / O (bare phase +1, the normalised F_9 Gauss sum)",
      maxerr < 1e-12 and nz == 8, f"max |diff| = {maxerr:.1e}, {nz} nonzero classes of 81")
check("C3 for 49a1 the state at 3 is the qunaught 1_{O_3}: F[1_{O_3}] = 1_{O_3} (phase 1)", maxerr_vac < 1e-12, f"max |diff| = {maxerr_vac:.1e}")


def zeta_K3(f, chi3, s, shells=range(-2, 3)):
    tot = 0
    for k in shells:
        for u in units3:
            x = (u[0] * Fr(3) ** k, u[1] * Fr(3) ** k)
            tot += f(x) * chi3 ** k * eta(u) * 9.0 ** (-k * s) / 8
    return tot


def Phi3hat(y):
    return fourier_finite(Phi3, reps9, 1 / 81, y)


psi3_of_3 = -1                   # psi_u((3)) = eps(3)*3/3 = (3/7) = -1, the inert half turn
chi_m3_at_9 = 1                  # chi_{-3,3}(N 3) = chi_{-3,3}(3)^2 = 1
chi3_unif = psi3_of_3 * chi_m3_at_9
for s in (0.5, 0.3 + 0.7j):
    Z1 = zeta_K3(Phi3, chi3_unif, s)
    Z2 = zeta_K3(Phi3hat, 1 / chi3_unif, 1 - s)
    pred = -(9 ** (0.5 - s))
    check(f"C4 local functional equation at 3 for psi' (psi'_3(3) = -1), s = {s}: ratio = -9^(1/2 - s)",
          abs(Z2 / Z1 - pred) < 1e-12 * abs(pred), f"ratio {complex(Z2 / Z1):.12f}")
Zw = zeta_K3(Phi3hat, 1, 0.5) / zeta_K3(Phi3, 1, 0.5)
check("C4 control: with psi'_3(3) = +1 (no half turn) the same state would give phase +1", abs(Zw - 1) < 1e-12, f"ratio {complex(Zw):.12f}")
eps_3 = -1
W2 = eps_inf * eps_7 * eps_3
check("C5 441d1: product of the local gate phases (-i)(i)(-1) = -1 = ellrootno(441d1)", abs(W2 - g2) < 1e-15, f"product = {W2}")

lam7 = mp.fsum(leg(u, 7) * mp.expj(2 * mp.pi * u / 7) for u in range(1, 7)) / mp.sqrt(7)
lam_inf = -1j                    # eps(sign, psi_inf) for psi_inf(x) = exp(-2 pi i x): F[x e^(-pi x^2)] = -i y e^(-pi y^2)
xs1 = np.arange(-7, 7 + 1e-9, 0.005)
eF = max(abs(np.sum(xs1 * np.exp(-np.pi * xs1 ** 2) * np.exp(-2j * np.pi * xs1 * y)) * 0.005 - (-1j) * y * np.exp(-np.pi * y ** 2))
         for y in (0.2, -0.9, 1.3))
eps_chi3 = mp.fsum(leg(u, 3) * mp.expj(2 * mp.pi * u / 3) for u in (1, 2)) / mp.sqrt(3)
w_over_Q = {"inf": complex(lam_inf * eps_inf), "7": complex(lam7 * eps_7), "3_49a1": 1, "3_441d1": complex(eps_chi3 ** 2 * 1)}
check("C6 over Q: w_inf = lambda_inf eps_inf = (-i)(-i) = -1; w_7 = lambda_7 eps_7 = (i)(i) = -1 (lambda_7 the normalised Gauss sum of chi_-7); "
      "w_3(441d1) = eps(chi_-3,3)^2 det(quarter turn) = (i)^2 (1) = -1; all equal PARI's ellrootno(E, p)",
      eF < 1e-12 and abs(w_over_Q["inf"] - l1[0]) < 1e-15 and abs(w_over_Q["7"] - l1[2]) < 1e-15 and abs(w_over_Q["7"] - l2[2]) < 1e-15
      and abs(w_over_Q["3_441d1"] - l2[1]) < 1e-15 and l1[1] == 1,
      f"w_inf {w_over_Q['inf']:.3f}, w_7 {w_over_Q['7']:.3f}, w_3 {w_over_Q['3_441d1']:.3f}; Hermite check {eF:.1e}")

B = gp(f"""
E=ellinit("49a1"); F=ellinit("441d1");
L1=lfuncreate([n->ellan(E,n), 0, [0,1], 2, {7 * 7}, {int(round(W1.real))}]);
L1w=lfuncreate([n->ellan(E,n), 0, [0,1], 2, {7 * 7}, {-int(round(W1.real))}]);
L2=lfuncreate([n->ellan(F,n), 0, [0,1], 2, {7 * 7 * 9}, {int(round(W2.real))}]);
L2w=lfuncreate([n->ellan(F,n), 0, [0,1], 2, {7 * 7 * 9}, {-int(round(W2.real))}]);
print("@f1 ",lfuncheckfeq(L1)); print("@f1w ",lfuncheckfeq(L1w)); print("@f2 ",lfuncheckfeq(L2)); print("@f2w ",lfuncheckfeq(L2w));
print("@an1 ",ellan(E,3000)); print("@an2 ",ellan(F,3000));
""")
f1, f1w, f2, f2w = (int(B[k]) for k in ("f1", "f1w", "f2", "f2w"))
check("C7 the L-function built from the a_n with conductor prod_v N_v (49; 49 * 9 = 441) and W = prod of gate phases satisfies the "
      "functional equation; with -W it fails", f1 < -100 and f2 < -100 and f1w > -5 and f2w > -5,
      f"lfuncheckfeq: 49a1 2^{f1} (wrong sign 2^{f1w}); 441d1 2^{f2} (wrong sign 2^{f2w})")
mp.mp.dps = 30


def theta_feq(an, N, W):
    """lane C's overlap form: f(i/(N y)) = W N y^2 f(iy), f(iy) = sum a_n exp(-2 pi n y); computed from the a_n alone"""
    f = lambda y: mp.fsum(a * mp.exp(-2 * mp.pi * (k + 1) * y) for k, a in enumerate(an) if a)
    worst = mp.mpf(0)
    for c in (mp.mpf("0.8"), mp.mpf("1.25")):
        y = c / mp.sqrt(N)
        worst = max(worst, abs(f(1 / (N * y)) - W * N * y ** 2 * f(y)) / abs(f(y)))
    return worst


an1 = [int(v) for v in B["an1"].strip("[]").split(",")]
an2 = [int(v) for v in B["an2"].strip("[]").split(",")]
t1, t1w = theta_feq(an1, 49, int(round(W1.real))), theta_feq(an1, 49, -int(round(W1.real)))
t2, t2w = theta_feq(an2, 441, int(round(W2.real))), theta_feq(an2, 441, -int(round(W2.real)))
check("C7 independent of PARI's functional equation: the overlap f(iy) = sum a_n e^(-2 pi n y) (3000 terms) satisfies "
      "f(i/(Ny)) = W N y^2 f(iy) with W = the product of gate phases, at y = 0.8/sqrt N and 1.25/sqrt N",
      t1 < mp.mpf(10) ** -25 and t2 < mp.mpf(10) ** -25 and t1w > 0.1 and t2w > 0.1,
      f"relative error 49a1 {mp.nstr(t1, 2)} ({float(-mp.log10(t1)):.1f} digits), 441d1 {mp.nstr(t2, 2)} ({float(-mp.log10(t2)):.1f} digits); "
      f"with -W: {mp.nstr(t1w, 3)}, {mp.nstr(t2w, 3)}")

# -----------------------------------------------------------------------------------------------
print("== D  the ladder: zeta, Dirichlet, curves over F_q, graphs")
eG = max(abs(np.sum(np.exp(-np.pi * xs1 ** 2) * np.exp(-2j * np.pi * xs1 * y)) * 0.005 - np.exp(-np.pi * y ** 2)) for y in (0.2, -0.9, 1.3))
Dz = gp(r"""print("@z ",lfunrootres(lfuncreate(1))[3]); print("@m3 ",lfunrootres(lfuncreate(-3))[3]);
G=znstar(5,1); print("@g5 ",G.gen); print("@m5 ",lfunrootres(lfuncreate([G,[1]]))[3]);""")
check("D1 zeta: the Gaussian is Fourier-invariant (phase 1), every finite state is the qunaught (phase 1); PARI root number 1",
      eG < 1e-12 and Dz["z"] == "1", f"|F[e^(-pi x^2)] - e^(-pi y^2)| = {eG:.1e}")
W3 = complex(eps_chi3) * lam_inf
check("D2 L(s, chi_-3): eps_3 = i (normalised F_3 Gauss sum), eps_inf = -i (odd Hermite phase); product 1 = PARI",
      abs(W3 - 1) < 1e-15 and Dz["m3"] == "1", f"product {W3:.3f}")
chi5 = {1: 1, 2: 1j, 4: -1, 3: -1j}                                                 # chi(2) = i, PARI's [znstar(5,1), [1]]
tau5 = sum(chi5[u] * cmath.exp(2j * math.pi * u / 5) for u in range(1, 5))
W5 = tau5 / math.sqrt(5) * lam_inf
P5 = pnum(Dz["m5"])
check("D3 L(s, chi mod 5 of order 4, chi(2) = i): eps_5 = tau(chi)/sqrt5, eps_inf = -i; product = PARI's root number (a phase, not +-1)",
      Dz["g5"] == "[2]" and abs(W5 - P5) < 1e-14, f"product {W5:.12f}, PARI {P5:.12f}")


def Zcurve(P, q, u):
    return np.polyval(P[::-1], u) / ((1 - u) * (1 - q * u))


Pemode = [1, 1, 2]                                    # E mode over F_2: x^2 + x + 2, a = -1, P(u) = 1 + u + 2u^2
cp = gp(r"""print("@cp ",Vec(hyperellcharpoly(Mod(1,5)*(x^5+x^3+x^2-2))));""")["cp"]
cpv = [int(v) for v in cp.strip("[]").split(",")]
Pg2 = cpv                                             # Vec(charpoly) from the top = increasing coefficients of u^4 charpoly(1/u)
ok, worst = True, 0.0
for P, q, g in ((Pemode, 2, 1), (Pg2, 5, 2)):
    for u in (0.13 + 0.21j, -0.3 + 0.05j, 0.07 - 0.4j):
        lhs = Zcurve(P, q, 1 / (q * u))
        rhs = q ** (1 - g) * u ** (2 - 2 * g) * Zcurve(P, q, u)
        worst = max(worst, abs(lhs - rhs) / abs(rhs))
    for s in (0.5 + 3.1j, 0.2 + 0.7j):
        xi = lambda s_: q ** ((g - 1) * s_) * Zcurve(P, q, q ** (-s_))
        worst = max(worst, abs(xi(s) - xi(1 - s)) / abs(xi(s)))
check("D4 curves over F_q (E mode over F_2, genus-2 curve y^2 = x^5+x^3+x^2-2 over F_5): Z(1/(qu)) = q^(1-g) u^(2-2g) Z(u); "
      "xi(s) = q^((g-1)s) Z(q^-s) = xi(1-s), root number +1", worst < 1e-12, f"max relative error {worst:.1e}; P(u) = {Pg2}")

import networkx as nx


def ihara_check(Gr):
    n, m = Gr.number_of_nodes(), Gr.number_of_edges()
    q = Gr.degree[0] - 1
    A = nx.to_numpy_array(Gr, nodelist=sorted(Gr.nodes()))
    darts = [(a, b) for a, b in Gr.edges()] + [(b, a) for a, b in Gr.edges()]
    idx = {d: i for i, d in enumerate(darts)}
    Bm = np.zeros((2 * m, 2 * m))
    for (a, b) in darts:
        for c in Gr.neighbors(b):
            if c != a:
                Bm[idx[(a, b)], idx[(b, c)]] = 1
    zeta = lambda u: 1 / np.linalg.det(np.eye(2 * m) - u * Bm)
    xi = lambda u: np.linalg.det(np.eye(n) - u * A + q * u * u * np.eye(n))
    err_bass = max(abs(1 / zeta(u) - (1 - u * u) ** (m - n) * xi(u)) / abs(xi(u)) for u in (0.11 + 0.05j, -0.2 + 0.1j))
    Lam = lambda u: (complex(1 - u * u) ** (m - n + n / 2)) * (complex(1 - q * q * u * u) ** (n / 2)) * zeta(u)
    signs = [Lam(1 / (q * u)) / Lam(u) for u in (0.1, 0.17, 0.23 / q)]
    Xi = lambda s: q ** (-n / 2) * q ** (n * s) * xi(q ** (-s))
    err_xi = max(abs(Xi(s) - Xi(1 - s)) / abs(Xi(s)) for s in (0.3 + 1.1j, 0.5 + 2.0j, 0.9 - 0.3j))
    return n, m, q, err_bass, signs, err_xi


n4, m4, q4, eb4, sg4, ex4 = ihara_check(nx.complete_graph(4))
n5, m5, q5, eb5, sg5, ex5 = ihara_check(nx.complete_graph(5))
check("D5 K_4 (q = 2, n = 4, m = 6): Ihara-Bass det(1 - uB) = (1-u^2)^(m-n) det(1 - uA + qu^2); "
      "Lambda(u) = (1-u^2)^(m-n+n/2) (1-q^2u^2)^(n/2) zeta(u) has Lambda(1/(qu)) = +Lambda(u); Xi(s) = q^(n(s-1/2)) det(1 - Aq^-s + q^(1-2s)) is even about 1/2",
      eb4 < 1e-10 and all(abs(s_ - 1) < 1e-10 for s_ in sg4) and ex4 < 1e-12,
      f"Bass {eb4:.1e}; sign {np.round(sg4[0], 12)}; Xi symmetric to {ex4:.1e}")
check("D5 K_5 (q = 3, n = 5): the same Lambda with principal branches has sign (-1)^n = -1, while Xi(s) stays even (+1): "
      "the graph sign is a convention of the trivial factor, not a local phase",
      eb5 < 1e-10 and all(abs(s_ + 1) < 1e-10 for s_ in sg5) and ex5 < 1e-12, f"sign {np.round(sg5[0], 12)}; Xi symmetric to {ex5:.1e}")

print(f"\n{npass} of {npass + nfail} pass")
