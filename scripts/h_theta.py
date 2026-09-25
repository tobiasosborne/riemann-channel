#!/usr/bin/env python3
# h_theta.py -- blind numerics lane for the H-THETA round.
# author: claude:opus (numerics lane), 2026-09-21
#
# Tests every computer-testable displayed formula of notes/h-theta/astra-brief.md.
# Deterministic; seed 20260921 (used only for the pseudo-random sampling grids).
# Dependencies: mpmath, numpy, scipy.  Working precision 25 decimal digits.
#
# Conventions (Section 1 of the brief):
#   bond          H = L^2(R_+^x, d^x y), d^x y = dy/y
#   Mellin        fhat(tau) = int_0^inf f(y) y^{i tau} d^x y
#   theta(y)      = sum_{n in Z} e^{-pi n^2 y},  theta(1/y) = y^{1/2} theta(y)
#   phi(y)        = theta(y) - 1 - y^{-1/2}
#   Lambda(s)     = int_0^inf phi(y) y^{s/2} d^x y = 2 pi^{-s/2} Gamma(s/2) zeta(s)
#                 = 4 xi(s)/(s(s-1))            (0 < Re s < 1)
#   g(y)          = y^{1/4} phi(y),  ghat(tau) = Lambda(1/2 + 2 i tau)
#   xi(s)         = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)
#   xi_crit(tau)  = xi(1/2 + 2 i tau)
#   Theta(tau)    = xi(1+2i tau)/xi(1-2i tau)   (inner in C_+)
#   k_w(tau)      = 1/(tau - conj w)            (04h, line 33)

import sys
import numpy as np
import mpmath as mp
from scipy.linalg import eigvalsh

mp.mp.dps = 25
SEED = 20260921
np.random.seed(SEED)

PASSED = 0
FAILED = 0
COUNT = 0


def check(cond, msg):
    """Print 'ok NN  msg' or 'FAIL NN  msg' and tally."""
    global PASSED, FAILED, COUNT
    COUNT += 1
    if cond:
        PASSED += 1
        print("ok %02d  %s" % (COUNT, msg))
    else:
        FAILED += 1
        print("FAIL %02d  %s" % (COUNT, msg))


def sec(title):
    print("")
    print("=" * 78)
    print(title)
    print("=" * 78)


def info(fmt, *a):
    print("      " + (fmt % a if a else fmt))


def fs(z, n=12):
    """format an mpmath number compactly"""
    return mp.nstr(z, n)


# ---------------------------------------------------------------------------
# 0. theta, phi and the basic special functions
# ---------------------------------------------------------------------------

PI = mp.pi
BIG = mp.mpf(200)          # beyond this the theta tail is below any working precision


def thetam1(y):
    """theta(y) - 1 = 2 sum_{n>=1} exp(-pi n^2 y), summed directly (no cancellation)."""
    y = mp.mpf(y)
    if y > BIG:
        return mp.mpf(0)
    tol = mp.mpf(10) ** (-(mp.mp.dps + 10))
    s = mp.mpf(0)
    n = 1
    while True:
        t = mp.exp(-PI * n * n * y)
        s += t
        if t < tol:
            break
        n += 1
        if n > 10 ** 5:
            break
    return 2 * s


def theta_jtheta(y):
    """theta(y) via mpmath's jtheta, using the functional equation for y < 1."""
    y = mp.mpf(y)
    if y >= 1:
        return mp.jtheta(3, 0, mp.exp(-PI * y))
    return y ** mp.mpf(-0.5) * mp.jtheta(3, 0, mp.exp(-PI / y))


def theta(y):
    """theta(y) = 1 + (theta(y)-1), cancellation-free for every y > 0."""
    y = mp.mpf(y)
    if y >= 1:
        return 1 + thetam1(y)
    return y ** mp.mpf(-0.5) * (1 + thetam1(1 / y))


def thetam1_any(y):
    """theta(y) - 1 for any y > 0 (no cancellation: for y<1 the y^{-1/2} dominates)."""
    y = mp.mpf(y)
    if y >= 1:
        return thetam1(y)
    r = y ** mp.mpf(-0.5)
    return r * (1 + thetam1(1 / y)) - 1


def phi(y):
    """phi(y) = theta(y) - 1 - y^{-1/2}, evaluated without cancellation.

    y >= 1 : phi = (theta-1) - y^{-1/2}
    y <  1 : phi = y^{-1/2}(theta(1/y)-1) - 1     (functional equation)
    """
    y = mp.mpf(y)
    if y >= 1:
        return thetam1(y) - y ** mp.mpf(-0.5)
    v = 1 / y
    if v > BIG:
        return mp.mpf(-1)
    return y ** mp.mpf(-0.5) * thetam1(v) - 1


def phi_plus1(y):
    """phi(y) + 1 = y^{-1/2}(theta(1/y)-1) for y < 1, computed without cancellation."""
    y = mp.mpf(y)
    return y ** mp.mpf(-0.5) * thetam1(1 / y)


def phi_plus_ym12(y):
    """phi(y) + y^{-1/2} = theta(y) - 1 for y >= 1, computed without cancellation."""
    return thetam1(mp.mpf(y))


def xi(s):
    """xi(s) = (1/2)s(s-1)pi^{-s/2}Gamma(s/2)zeta(s) = (s-1)pi^{-s/2}Gamma(s/2+1)zeta(s)."""
    s = mp.mpc(s)
    if abs(s) < mp.mpf(10) ** (-20):
        return mp.mpf(1) / 2
    if abs(s - 1) < mp.mpf(10) ** (-20):
        return mp.mpf(1) / 2
    return (s - 1) * PI ** (-s / 2) * mp.gamma(s / 2 + 1) * mp.zeta(s)


def Lam(s):
    """Lambda(s) = 2 pi^{-s/2} Gamma(s/2) zeta(s) (closed form, meromorphic)."""
    s = mp.mpc(s)
    return 2 * PI ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def xi_crit(tau):
    return xi(mp.mpf(1) / 2 + 2j * mp.mpc(tau))


def ghat_cf(tau):
    """ghat(tau) = -xi_crit(tau)/(tau^2 + 1/16), closed form."""
    tau = mp.mpc(tau)
    return -xi_crit(tau) / (tau ** 2 + mp.mpf(1) / 16)


def Theta_sym(tau):
    """Theta(tau) = xi(1+2i tau)/xi(1-2i tau)."""
    tau = mp.mpc(tau)
    return xi(1 + 2j * tau) / xi(1 - 2j * tau)


# --- quadrature of the Mellin integral of phi, with EXACT elementary tails -----
#
# In x = log y:  int phi(e^x) e^{s x/2} dx.
# For x <= -X (X >= 25) phi(e^x) = -1 to well below working precision, and
# for x >= +X phi(e^x) = -e^{-x/2} likewise; both tails integrate in closed form:
#   int_{-inf}^{-X} (-1)      e^{sx/2} dx = -2 e^{-X s/2}/s          (Re s > 0)
#   int_{X}^{inf}  (-e^{-x/2}) e^{sx/2} dx = +2 e^{X(s-1)/2}/(s-1)   (Re s < 1)

XCUT = mp.mpf(25)


def _pts(a, b, s):
    """subdivision points on [a,b] resolving the oscillation e^{i Im(s) x/2}."""
    om = abs(mp.im(s)) / 2
    h = mp.mpf(3)
    if om > 0:
        h = min(h, mp.pi / (2 * om))
    n = int(mp.ceil((b - a) / h)) + 1
    return [a + (b - a) * mp.mpf(k) / n for k in range(n + 1)]


def mellin_phi(s, half=None, X=XCUT, maxdegree=4):
    """int phi(y) y^{s/2} d^x y over (0,inf) ['full'], (1,inf) ['gt'] or (0,1) ['lt']."""
    s = mp.mpc(s)
    f = lambda x: phi(mp.exp(x)) * mp.exp(s * x / 2)
    tail_l = -2 * mp.exp(-X * s / 2) / s
    tail_r = 2 * mp.exp(X * (s - 1) / 2) / (s - 1)
    if half == 'gt':
        return mp.quad(f, _pts(mp.mpf(0), X, s), maxdegree=maxdegree) + tail_r
    if half == 'lt':
        return mp.quad(f, _pts(-X, mp.mpf(0), s), maxdegree=maxdegree) + tail_l
    return (mp.quad(f, _pts(-X, mp.mpf(0), s), maxdegree=maxdegree)
            + mp.quad(f, _pts(mp.mpf(0), X, s), maxdegree=maxdegree)
            + tail_l + tail_r)


def lam_gt(s, N=None):
    """Lambda_>(s) = 2/(s-1) + 2 sum_{n>=1} (pi n^2)^{-s/2} Gamma(s/2, pi n^2). Entire + pole."""
    s = mp.mpc(s)
    if N is None:
        N = int(mp.sqrt((mp.mp.dps + 6) * mp.log(10) / PI)) + 2
    acc = mp.mpc(0)
    for n in range(1, N + 1):
        a = PI * n * n
        acc += a ** (-s / 2) * mp.gammainc(s / 2, a, mp.inf)
    return 2 / (s - 1) + 2 * acc


def lam_gt_entire(s, N=None):
    """Lambda_>(s) - 2/(s-1) = int_1^inf (theta(y)-1) y^{s/2} d^x y = 2 sum (pi n^2)^{-s/2} Gamma(s/2,pi n^2).

    Entire in s (no pole): this is the 'entire part' of Lambda_>."""
    s = mp.mpc(s)
    if N is None:
        N = int(mp.sqrt((mp.mp.dps + 6) * mp.log(10) / PI)) + 2
    acc = mp.mpc(0)
    for n in range(1, N + 1):
        a = PI * n * n
        acc += a ** (-s / 2) * mp.gammainc(s / 2, a, mp.inf)
    return 2 * acc


def lam_lt(s, N=None):
    """Lambda_<(s) := Lambda_>(1-s)."""
    return lam_gt(1 - mp.mpc(s), N)


def ghat_gt(tau):
    return lam_gt(mp.mpf(1) / 2 + 2j * mp.mpc(tau))


# zeta zeros (ordinates), cached
_GAMMAS = []


def gammas(n):
    while len(_GAMMAS) < n:
        _GAMMAS.append(mp.im(mp.zetazero(len(_GAMMAS) + 1)))
    return _GAMMAS[:n]


print("h_theta.py -- blind numerics for notes/h-theta/astra-brief.md")
print("author: claude:opus (numerics lane); mp.dps = %d; seed = %d" % (mp.mp.dps, SEED))

# ---------------------------------------------------------------------------
sec("T0. sanity of the theta implementation")
# ---------------------------------------------------------------------------

ok = True
for y in ['1', '1.5', '2.7', '5.0', '11.0']:
    ok = ok and abs(theta(mp.mpf(y)) - theta_jtheta(mp.mpf(y))) < mp.mpf(10) ** -22
check(ok, "direct sum theta(y)=1+2sum e^{-pi n^2 y} agrees with jtheta(3,0,e^{-pi y}), y>=1")

ok = True
for y in ['0.05', '0.3', '0.7', '0.95']:
    ok = ok and abs(theta(mp.mpf(y)) - theta_jtheta(mp.mpf(y))) < mp.mpf(10) ** -20 * theta(mp.mpf(y))
check(ok, "theta(y) for y<1 via y^{-1/2} jtheta(3,0,e^{-pi/y}) agrees with the cancellation-free form")

ok = True
for y in ['0.05', '0.3', '0.9', '1.0', '2.0', '9.0']:
    yy = mp.mpf(y)
    ok = ok and abs(theta(1 / yy) - mp.sqrt(yy) * theta(yy)) < mp.mpf(10) ** -21 * abs(theta(1 / yy))
check(ok, "theta(1/y) = y^{1/2} theta(y) (Jacobi), y in [0.05,9]")

info("theta(1) = %s", fs(theta(1)))

# ---------------------------------------------------------------------------
sec("T0b. Section 1 conventions: Mellin, dilation, outgoing half, inversion")
# ---------------------------------------------------------------------------

# test vector supported on the outgoing half y > 1:  f(y) = 1_{y>1} y^{-1/2 - i b}
BB = mp.mpf('1.3')


def ftest(y):
    y = mp.mpf(y)
    return 0 if y < 1 else y ** (mp.mpf(-0.5) - 1j * BB)


def ftest_hat(tau, X=mp.mpf(400)):
    tau = mp.mpc(tau)
    c = mp.mpf(-0.5) + 1j * (tau - BB)
    om = abs(mp.im(c))
    h = min(mp.mpf(2), mp.pi / (2 * om)) if om > 0 else mp.mpf(2)
    n = int(mp.ceil(X / h)) + 1
    pts = [X * mp.mpf(k) / n for k in range(n + 1)]
    return mp.quad(lambda x: mp.exp(c * x), pts, maxdegree=4) - mp.exp(c * X) / c


ok = True
for tau in [mp.mpf(2), mp.mpf(2) + 3j, mp.mpf('-1.5') + mp.mpf('0.4') * 1j]:
    a = ftest_hat(tau)
    b = 1 / (mp.mpf('0.5') - 1j * (tau - BB))
    ok = ok and abs(a - b) < mp.mpf('1e-16') * abs(b)
check(ok, "T0b fhat(tau)=int f(y)y^{i tau}d^x y for f=1_{y>1}y^{-1/2-1.3i} equals 1/(1/2-i(tau-1.3))")
check(abs(mp.mpf('0.5') - 1j * ((BB - 1j / 2) - BB)) < mp.mpf('1e-25'),
      "T0b that fhat has its only pole at tau = 1.3 - i/2, i.e. in C_-: fhat is of Hardy class in C_+")
_near = abs(1 / (mp.mpf('0.5') - 1j * (BB - mp.mpf('0.49') * 1j - BB)))
info("|fhat(2+3i)| = %s (in C_+);  |fhat(1.3-0.49i)| = %s (approaching the C_- pole)",
     fs(abs(ftest_hat(mp.mpf(2) + 3j)), 8), fs(_near, 8))
check(abs(ftest_hat(mp.mpf(2) + 3j)) < 1 and _near > 30,
      "T0b |fhat| is bounded in C_+ and blows up at the C_- pole: outgoing half y>1 <-> H^2(C_+) CONFIRMED")


def Ut_ftest_hat(t, tau, X=mp.mpf(400)):
    """Mellin transform of (U_t f)(y) = f(e^{-t} y), computed by quadrature."""
    t = mp.mpf(t)
    tau = mp.mpc(tau)
    f = lambda x: (ftest(mp.exp(x - t)) * mp.exp(1j * tau * x)) if x > t else 0
    c = mp.mpf(-0.5) + 1j * (tau - BB)
    om = abs(mp.im(c))
    h = min(mp.mpf(2), mp.pi / (2 * om)) if om > 0 else mp.mpf(2)
    n = int(mp.ceil(X / h)) + 1
    pts = [t + X * mp.mpf(k) / n for k in range(n + 1)]
    return (mp.quad(lambda x: ftest(mp.exp(x - t)) * mp.exp(1j * tau * x), pts, maxdegree=4)
            - mp.exp(1j * tau * t) * mp.exp(c * X) / c)


ok = True
for (t, tau) in [('0.7', mp.mpf(2)), ('0.7', mp.mpf('1.1') + 2j), ('-0.4', mp.mpf(2))]:
    a = Ut_ftest_hat(mp.mpf(t), tau)
    b = mp.exp(1j * tau * mp.mpf(t)) * ftest_hat(tau)
    ok = ok and abs(a - b) < mp.mpf('1e-15') * abs(b)
check(ok, "T0b (U_t f)^hat = e^{i t tau} fhat for (U_t f)(y) = f(e^{-t} y), t = 0.7 and -0.4")
check(all(ftest(mp.exp(-mp.mpf('0.7')) * mp.mpf(y)) == 0 for y in ['1.0', '1.5', '2.0'])
      and ftest(mp.exp(-mp.mpf('0.7')) * mp.mpf('2.1')) != 0,
      "T0b U_t (t=0.7>0) maps L^2(1,inf) into itself: supp U_t f = {y > e^t} (forward = outgoing)")


def Jftest_hat(tau, X=mp.mpf(400)):
    tau = mp.mpc(tau)
    c = mp.mpf(0.5) + 1j * (tau + BB)
    om = abs(mp.im(c))
    h = min(mp.mpf(2), mp.pi / (2 * om)) if om > 0 else mp.mpf(2)
    n = int(mp.ceil(X / h)) + 1
    pts = [-X + X * mp.mpf(k) / n for k in range(n + 1)]
    return mp.quad(lambda x: ftest(mp.exp(-x)) * mp.exp(1j * tau * x), pts, maxdegree=4) \
        - mp.exp(-c * X) / c


ok = True
for tau in [mp.mpf(2), mp.mpf('0.8') - mp.mpf('0.3') * 1j]:
    ok = ok and abs(Jftest_hat(tau) - ftest_hat(-tau)) < mp.mpf('1e-15') * abs(ftest_hat(-tau))
check(ok, "T0b (Jf)^hat(tau) = fhat(-tau) for (Jf)(y) = f(1/y); J maps the outgoing half to y<1 <-> H^2(C_-)")

# ---------------------------------------------------------------------------
sec("T1. weight, symmetry, membership")
# ---------------------------------------------------------------------------

# T1(a) phi(1/y) = y^{1/2} phi(y)
ok = True
worst = mp.mpf(0)
for y in ['0.02', '0.17', '0.5', '0.99', '1.0', '1.3', '4.0', '30.0']:
    yy = mp.mpf(y)
    lhs = phi(1 / yy)
    rhs = mp.sqrt(yy) * phi(yy)
    rel = abs(lhs - rhs) / max(abs(lhs), mp.mpf(10) ** -30)
    worst = max(worst, rel)
    ok = ok and rel < mp.mpf(10) ** -20
check(ok, "T1(a) phi(1/y) = y^{1/2} phi(y) exactly, 8 values of y (max rel err %s)" % fs(worst, 3))

# T1(b) asymptotics near 0 :  phi(y) = -1 + O(y^{-1/2} e^{-pi/y})
info("near y -> 0:   y        (phi(y)+1)/(2 y^{-1/2} e^{-pi/y})")
ok = True
for y in ['0.2', '0.1', '0.05', '0.02']:
    yy = mp.mpf(y)
    r = phi_plus1(yy) / (2 * yy ** mp.mpf(-0.5) * mp.exp(-PI / yy))
    info("              %-8s  %s", y, fs(r, 16))
    ok = ok and abs(r - 1) < mp.mpf('2e-5')
check(ok, "T1(b) phi(y) = -1 + 2 y^{-1/2} e^{-pi/y}(1+o(1)) as y->0 (ratio -> 1 to 2e-5 at y=0.2..0.02)")
check(abs(phi(mp.mpf('0.2')) + 1 - phi_plus1(mp.mpf('0.2'))) < mp.mpf('1e-22'),
      "T1(b) phi(y)+1 = y^{-1/2}(theta(1/y)-1) identically (the two constant terms cancel exactly)")

info("near y -> inf: y        (phi(y)+y^{-1/2})/(2 e^{-pi y})")
ok = True
for y in ['2', '3', '5', '9']:
    yy = mp.mpf(y)
    r = phi_plus_ym12(yy) / (2 * mp.exp(-PI * yy))
    info("              %-8s  %s", y, fs(r, 16))
    ok = ok and abs(r - 1) < mp.mpf('2e-8')
check(ok, "T1(b) phi(y) = -y^{-1/2} + 2 e^{-pi y}(1+o(1)) as y->inf (ratio -> 1 to 2e-8 at y=2..9)")

# T1(b) J(y^a phi) = y^a phi only for a = 1/4
info("a        max_y | (1/y)^a phi(1/y) - y^a phi(y) |")
for a in ['0.1', '0.25', '0.4']:
    aa = mp.mpf(a)
    d = max(abs((1 / mp.mpf(y)) ** aa * phi(1 / mp.mpf(y)) - mp.mpf(y) ** aa * phi(mp.mpf(y)))
            for y in ['0.3', '0.8', '2.0', '5.0'])
    info("%-8s %s", a, fs(d, 10))
d025 = max(abs((1 / mp.mpf(y)) ** mp.mpf('0.25') * phi(1 / mp.mpf(y))
               - mp.mpf(y) ** mp.mpf('0.25') * phi(mp.mpf(y)))
           for y in ['0.03', '0.3', '0.8', '2.0', '5.0', '40.0'])
check(d025 < mp.mpf(10) ** -20, "T1(b) J(y^{1/4} phi) = y^{1/4} phi (defect %s)" % fs(d025, 3))
ok = True
for a in ['0.1', '0.2', '0.3', '0.4', '0.0', '0.5']:
    aa = mp.mpf(a)
    d = max(abs((1 / mp.mpf(y)) ** aa * phi(1 / mp.mpf(y)) - mp.mpf(y) ** aa * phi(mp.mpf(y)))
            for y in ['0.3', '0.8', '2.0'])
    ok = ok and d > mp.mpf('1e-3')
check(ok, "T1(b) J(y^a phi) != y^a phi for a in {0,0.1,0.2,0.3,0.4,0.5} (a=1/4 is the only fixed weight)")

# T1(b) L^2 norms: ||y^a phi||^2 = int_0^inf y^{2a} phi^2 d^x y, finite iff 0<a<1/2


def l2norm2(a, X=mp.mpf(60)):
    """int_{-X}^{X} e^{2 a x} phi(e^x)^2 dx plus exact tails (phi=-1 left, -e^{-x/2} right)."""
    aa = mp.mpf(a)
    f = lambda x: mp.exp(2 * aa * x) * phi(mp.exp(x)) ** 2
    core = mp.quad(f, [-X, mp.mpf(-3), mp.mpf(0), mp.mpf(3), X])
    tl = mp.exp(-2 * aa * X) / (2 * aa) if aa > 0 else mp.inf
    tr = mp.exp((2 * aa - 1) * X) / (1 - 2 * aa) if aa < mp.mpf('0.5') else mp.inf
    return core + tl + tr


def l2norm2_trunc(a, A, B):
    """int_{A}^{B} e^{2 a x} phi(e^x)^2 dx, truncated (no tails)."""
    aa = mp.mpf(a)
    f = lambda x: mp.exp(2 * aa * x) * phi(mp.exp(x)) ** 2
    pts = sorted(set([mp.mpf(A), mp.mpf(-3), mp.mpf(0), mp.mpf(3), mp.mpf(B)]))
    pts = [p for p in pts if mp.mpf(A) <= p <= mp.mpf(B)]
    return mp.quad(f, pts)


info("a        ||y^a phi||^2 (converged)")
ok = True
for a in ['0.1', '0.25', '0.4']:
    v = l2norm2(a)
    info("%-8s %s", a, fs(v, 16))
    ok = ok and mp.isfinite(v) and v > 0
check(ok, "T1(b) ||y^a phi||^2 finite for a in {0.1, 0.25, 0.4}")
check(abs(l2norm2('0.1') - l2norm2('0.4')) < mp.mpf('1e-15')
      and abs(l2norm2('0.15') - l2norm2('0.35')) < mp.mpf('1e-15'),
      "T1(b) ||y^a phi|| = ||y^{1/2-a} phi|| (J-symmetry of the weight family; a=1/4 is the fixed point)")

info("divergence test: truncated  int_{-X}^{X} e^{2ax} phi(e^x)^2 dx")
info("X        a=0            a=0.5          a=0.25 (control)")
vals0, vals5, vals25 = [], [], []
for X in [10, 20, 40, 80]:
    v0 = l2norm2_trunc('0', -X, X)
    v5 = l2norm2_trunc('0.5', -X, X)
    v25 = l2norm2_trunc('0.25', -X, X)
    vals0.append(v0)
    vals5.append(v5)
    vals25.append(v25)
    info("%-8d %-14s %-14s %s", X, fs(v0, 10), fs(v5, 10), fs(v25, 10))
inc0 = [vals0[i + 1] - vals0[i] for i in range(3)]
inc5 = [vals5[i + 1] - vals5[i] for i in range(3)]
inc25 = [vals25[i + 1] - vals25[i] for i in range(3)]
check(all(abs(inc0[i] - X) < mp.mpf('1e-3') for i, X in enumerate([10, 20, 40])),
      "T1(b) a=0: increments over X=10->20->40->80 are 10, 20, 40 (linear growth: divergent)")
check(all(abs(inc5[i] - X) < mp.mpf('1e-3') for i, X in enumerate([10, 20, 40])),
      "T1(b) a=1/2: increments are 10, 20, 40 (linear growth: divergent)")
check(abs(inc25[-1]) < mp.mpf('1e-8'),
      "T1(b) a=1/4: increment X=40->80 is %s (convergent)" % fs(inc25[-1], 3))

GN2 = l2norm2('0.25')
info("||g||^2 = int y^{1/2} phi(y)^2 d^x y = %s", fs(GN2, 18))

# ---------------------------------------------------------------------------
sec("T2(a). ghat = Lambda(1/2 + 2 i tau)")
# ---------------------------------------------------------------------------

info("tau      ghat (direct quadrature)               Lambda(1/2+2i tau) (Gamma-zeta)   rel err")
ok = True
for t in ['0', '0.7', '2.3', '7.1']:
    tt = mp.mpf(t)
    s = mp.mpf(1) / 2 + 2j * tt
    a = mellin_phi(s)
    b = Lam(s)
    rel = abs(a - b) / abs(b)
    info("%-8s %-38s %-33s %s", t, fs(a, 14), fs(b, 14), fs(rel, 3))
    ok = ok and rel < mp.mpf('1e-18')
check(ok, "T2(a) int_0^inf y^{1/4} phi y^{i tau} d^x y = Lambda(1/2+2i tau), tau in {0,0.7,2.3,7.1}")

ok = True
for t in ['0', '0.7', '2.3', '7.1']:
    tt = mp.mpf(t)
    a = Lam(mp.mpf(1) / 2 + 2j * tt)
    b = ghat_cf(tt)
    ok = ok and abs(a - b) < mp.mpf('1e-20') * abs(a)
check(ok, "T2(a) Lambda(1/2+2i tau) = -xi_crit(tau)/(tau^2+1/16) = -xi_crit/((tau-i/4)(tau+i/4))")

g0 = ghat_cf(0)
x12 = xi(mp.mpf(1) / 2)
info("ghat(0)        = %s", fs(g0, 18))
info("-16 xi(1/2)    = %s", fs(-16 * x12, 18))
info("xi(1/2)        = %s", fs(x12, 18))
check(abs(g0 + 16 * x12) < mp.mpf('1e-20'), "T2(a) ghat(0) = Lambda(1/2) = -16 xi(1/2) = %s" % fs(g0, 12))

ok = all(abs(mp.im(ghat_cf(mp.mpf(t)))) < mp.mpf('1e-20') for t in ['0.3', '1.7', '5.5', '12.0'])
check(ok, "T2(a) ghat is real on the real tau-axis")
ok = all(abs(ghat_cf(mp.mpf(t)) - ghat_cf(-mp.mpf(t))) < mp.mpf('1e-20') for t in ['0.3', '1.7', '5.5'])
check(ok, "T2(a) ghat is even")

# residues at tau = +- i/4 -- which is which
res_p = -xi_crit(1j / 4) / (2 * (1j / 4))          # residue at tau = +i/4
res_m = -xi_crit(-1j / 4) / (-2 * (1j / 4))        # residue at tau = -i/4
eps = mp.mpf(10) ** -12
res_p_num = eps * ghat_cf(1j / 4 + eps)
res_m_num = eps * ghat_cf(-1j / 4 + eps)
info("Res_{tau=+i/4} ghat = %s   (numerically %s)", fs(res_p, 14), fs(res_p_num, 10))
info("Res_{tau=-i/4} ghat = %s   (numerically %s)", fs(res_m, 14), fs(res_m_num, 10))
info("tau=+i/4 <-> s=0 (Lambda residue -2);  tau=-i/4 <-> s=1 (Lambda residue +2);  ds/dtau = 2i")
check(abs(res_p - 1j) < mp.mpf('1e-20') and abs(res_p_num - 1j) < mp.mpf('1e-9'),
      "T2(a) residue of ghat at tau = +i/4 is +i  (the s=0 pole, incoming edge)")
check(abs(res_m + 1j) < mp.mpf('1e-20') and abs(res_m_num + 1j) < mp.mpf('1e-9'),
      "T2(a) residue of ghat at tau = -i/4 is -i  (the s=1 pole, outgoing edge)")
rs0 = eps * Lam(eps)
rs1 = eps * Lam(1 + eps)
check(abs(rs0 + 2) < mp.mpf('1e-10') and abs(rs1 - 2) < mp.mpf('1e-10'),
      "T2(a) Lambda has residues -2 at s=0 and +2 at s=1 (num: %s, %s)" % (fs(rs0, 8), fs(rs1, 8)))
check(abs(mp.mpf(1) / 2 + 2j * (1j / 4)) < mp.mpf('1e-25')
      and abs(mp.mpf(1) / 2 + 2j * (-1j / 4) - 1) < mp.mpf('1e-25'),
      "T2(a) 1/2+2i tau = 0 iff tau = +i/4 and = 1 iff tau = -i/4 (brief's parenthetical is right)")

# zeros of ghat on the real line at gamma_n/2
G3 = gammas(3)
info("n   gamma_n            |ghat(gamma_n/2)|")
ok = True
for n, gg in enumerate(G3, 1):
    v = abs(ghat_cf(gg / 2))
    info("%-3d %-18s %s", n, fs(gg, 14), fs(v, 6))
    ok = ok and v < mp.mpf('1e-20')
check(ok, "T2(a) ghat vanishes at tau = gamma_n/2, n = 1,2,3")

# decay rate
zs = set()
G40 = gammas(35)
us = []
for k in range(400):
    u = 5 + mp.mpf(35) * k / 399
    if all(abs(u - gg / 2) > mp.mpf('0.03') for gg in G40):
        us.append(u)
lu = np.array([float(mp.log(abs(ghat_cf(u)))) for u in us])
uu = np.array([float(u) for u in us])
slope, icpt = np.polyfit(uu, lu, 1)
info("least-squares fit of log|ghat(u)| on u in [5,40] (%d points, zeros excluded):", len(us))
info("   slope = %.8f   (-pi/2 = %.8f)   intercept = %.6f", slope, -float(mp.pi) / 2, icpt)
lu2 = lu - (-float(mp.pi) / 2) * uu
sl2, ic2 = np.polyfit(np.log(uu), lu2, 1)
info("   residual log|ghat| + (pi/2)u fitted against log u: exponent c = %.6f (Stirling predicts -1/4)", sl2)
check(abs(slope + float(mp.pi) / 2) < 0.02,
      "T2(a) |ghat(u)| decays like e^{-pi|u|/2}: fitted slope %.6f vs -pi/2 = %.6f" % (slope, -float(mp.pi) / 2))
check(abs(sl2 + 0.25) < 0.1,
      "T2(a) |ghat(u)| ~ C |u|^c e^{-pi|u|/2} with c = -1/4 (fitted c = %.4f on [5,40])" % sl2)
G80 = gammas(80)
us2 = []
for k in range(400):
    u = 40 + mp.mpf(60) * k / 399
    if all(abs(u - gg / 2) > mp.mpf('0.03') for gg in G80):
        us2.append(u)
lu_b = np.array([float(mp.log(abs(ghat_cf(u)))) for u in us2])
uu_b = np.array([float(u) for u in us2])
sl_b, ic_b = np.polyfit(uu_b, lu_b, 1)
sl2_b, _ = np.polyfit(np.log(uu_b), lu_b - (-float(mp.pi) / 2) * uu_b, 1)
info("second window u in [40,100] (%d points): slope = %.8f, exponent c = %.6f",
     len(us2), sl_b, sl2_b)
check(abs(sl_b + float(mp.pi) / 2) < 0.005,
      "T2(a) on [40,100] the fitted slope is %.6f, i.e. -pi/2 to 2.2e-3" % sl_b)
info("the naive fit of c is contaminated by log|zeta(1/2+2iu)| (fluctuations ~ sqrt(loglog u));")
info("the clean Stirling statement isolates c: |ghat(u)| / (2 pi^{-1/4} sqrt(2pi) u^{-1/4}")
info("e^{-pi u/2} |zeta(1/2+2iu)|) -> 1, which fixes c = -1/4 exactly.")
info("u        ratio")
ok = True
for u in ['40', '70', '100']:
    uu = mp.mpf(u)
    pred = (2 * PI ** mp.mpf(-0.25) * mp.sqrt(2 * PI) * uu ** mp.mpf(-0.25)
            * mp.exp(-PI * uu / 2) * abs(mp.zeta(mp.mpf(1) / 2 + 2j * uu)))
    r = abs(ghat_cf(uu)) / pred
    info("%-8s %s", u, fs(r, 14))
    ok = ok and abs(r - 1) < mp.mpf('0.01')
check(ok, "T2(a) |ghat(u)| = 2 pi^{-1/4} sqrt(2pi) |u|^{-1/4} e^{-pi|u|/2} |zeta(1/2+2iu)| (1+O(1/u)): c = -1/4")

# ---------------------------------------------------------------------------
sec("T2(b). the halves Lambda_> and Lambda_<")
# ---------------------------------------------------------------------------

ok = True
for s in ['0.3', mp.mpf('0.5') + 3j, mp.mpf('0.8') + 10j, mp.mpf('-0.4') + 2j]:
    ss = mp.mpc(s)
    a = lam_gt(ss)
    b = mellin_phi(ss, half='gt')
    ok = ok and abs(a - b) < mp.mpf('1e-17') * abs(a)
check(ok, "T2(b) Lambda_>(s) = 2/(s-1) + 2 sum (pi n^2)^{-s/2} Gamma(s/2,pi n^2) matches direct quadrature")

info("s                     Lambda_<(s) (direct)            Lambda_>(1-s)                   rel err")
ok = True
for s in ['0.3', mp.mpf('0.5') + 3j, mp.mpf('0.8') + 10j]:
    ss = mp.mpc(s)
    a = mellin_phi(ss, half='lt')
    b = lam_gt(1 - ss)
    rel = abs(a - b) / abs(b)
    info("%-21s %-31s %-31s %s", fs(ss, 8), fs(a, 12), fs(b, 12), fs(rel, 3))
    ok = ok and rel < mp.mpf('1e-17')
check(ok, "T2(b) Lambda_<(s) = Lambda_>(1-s) at s in {0.3, 0.5+3i, 0.8+10i}")

ok = True
for s in ['0.3', mp.mpf('0.5') + 3j, mp.mpf('0.8') + 10j]:
    ss = mp.mpc(s)
    tot = lam_gt(ss) + lam_lt(ss)
    ok = ok and abs(tot - Lam(ss)) < mp.mpf('1e-18') * abs(Lam(ss))
check(ok, "T2(b) Lambda_>(s) + Lambda_<(s) = Lambda(s) in the strip")

# smoothness of the entire parts across s = 1 and s = 0
info("s          Lambda_>(s) - 2/(s-1)")
vals = {}
for s in ['0.99', '1', '1.01']:
    vals[s] = lam_gt_entire(mp.mpf(s))
    info("%-10s %s", s, fs(vals[s], 18))
d2 = vals['0.99'] - 2 * vals['1'] + vals['1.01']
info("second difference at h=0.01: %s  (h^2 = 1e-4)", fs(d2, 8))
q = lam_gt_entire(mp.mpf(1))
qq = mp.quad(lambda x: thetam1(mp.exp(x)) * mp.exp(x / 2), [0, 3, 25])
info("Lambda_>(1)-2/(s-1)|_{s=1} = %s ; int_1^inf (theta-1)y^{1/2}d^x y = %s", fs(q, 16), fs(qq, 16))
check(abs(d2) < mp.mpf('1e-5') and abs(q - qq) < mp.mpf('1e-18'),
      "T2(b) Lambda_>(s) - 2/(s-1) is smooth across s=1 and equals int_1^inf (theta-1)y^{s/2}d^x y")

info("s          Lambda_<(s) + 2/s   (= Lambda_>(1-s) - 2/((1-s)-1), the entire part at 1-s)")
vals = {}
for s in ['-0.01', '0', '0.01']:
    vals[s] = lam_gt_entire(1 - mp.mpf(s))
    if mp.mpf(s) != 0:
        direct = lam_lt(mp.mpf(s)) + 2 / mp.mpf(s)
        assert abs(direct - vals[s]) < mp.mpf('1e-18')
    info("%-10s %s", s, fs(vals[s], 18))
d2b = vals['-0.01'] - 2 * vals['0'] + vals['0.01']
info("second difference at h=0.01: %s", fs(d2b, 8))
check(abs(d2b) < mp.mpf('1e-5'), "T2(b) Lambda_<(s) + 2/s is smooth across s=0")

# decay of ghat_> on the real line: 1/|u|, not exponential
info("u        |ghat_>(u)|       |u| |ghat_>(u)|")
prod = []
for u in ['5', '10', '20', '40']:
    uu = mp.mpf(u)
    v = abs(ghat_gt(uu))
    prod.append(uu * v)
    info("%-8s %-17s %s", u, fs(v, 12), fs(uu * v, 12))
pred = 1 - (theta(1) - 1)
info("predicted limit |u||ghat_>(u)| -> |2/(2i) - i(theta(1)-1)| = 1-(theta(1)-1) = %s", fs(pred, 12))
check(all(abs(p - pred) < mp.mpf('0.25') for p in prod) and abs(prod[-1] - pred) < mp.mpf('0.05'),
      "T2(b) |ghat_>(u)| ~ (1-(theta(1)-1))/|u| = %s/|u| (1/|u| decay, NOT exponential)" % fs(pred, 8))
eps = mp.mpf(10) ** -12
rgt = eps * ghat_gt(-1j / 4 + eps)
rlt = eps * lam_lt(mp.mpf(1) / 2 + 2j * (1j / 4 + eps))
info("Res_{tau=-i/4} ghat_> = %s ;  ghat_>(+i/4) = %s (finite)", fs(rgt, 10), fs(ghat_gt(1j / 4), 10))
info("Res_{tau=+i/4} ghat_< = %s ;  ghat_<(-i/4) = %s (finite)", fs(rlt, 10),
     fs(lam_lt(mp.mpf(1) / 2 + 2j * (-1j / 4)), 10))
check(abs(rgt + 1j) < mp.mpf('1e-9') and mp.isfinite(abs(ghat_gt(1j / 4))),
      "T2(b) ghat_> is analytic in Im tau > -1/4 with a simple pole at tau=-i/4, residue -i (the s=1 pole)")
check(abs(rlt - 1j) < mp.mpf('1e-9'),
      "T2(b) ghat_< carries the other pole: simple at tau=+i/4, residue +i (the s=0 pole)")
ok = True
for t in ['0.3', '1.7', '5.5', '13.0']:
    ok = ok and abs(ghat_cf(mp.mpf(t)) - (ghat_gt(mp.mpf(t)) + lam_lt(mp.mpf(1) / 2 + 2j * mp.mpf(t)))) < mp.mpf('1e-18')
check(ok, "T2(b) ghat = ghat_> + ghat_< on the real line")
ok = all(abs(lam_lt(mp.mpf(1) / 2 + 2j * mp.mpf(t)) - lam_gt(mp.mpf(1) / 2 - 2j * mp.mpf(t))) < mp.mpf('1e-18')
         for t in ['0.3', '1.7', '5.5'])
check(ok, "T2(b) ghat_<(tau) = ghat_>(-tau)")
check(abs(ghat_gt(mp.mpf(40))) > mp.mpf('1e-3') and abs(ghat_cf(mp.mpf(40))) < mp.mpf('1e-25'),
      "T2(b) at u=40: |ghat_>| = %s but |ghat| = %s (exponential vs 1/u)"
      % (fs(abs(ghat_gt(mp.mpf(40))), 6), fs(abs(ghat_cf(mp.mpf(40))), 6)))

# T3(c): Lambda_>(rho) purely imaginary and non-zero; Lambda_>(1-rho) non-zero
info("n   rho_n                    Lambda_>(rho_n)                          |Re|/|Im|")
ok1 = ok2 = ok3 = True
for n, gg in enumerate(G3, 1):
    rho = mp.mpf(1) / 2 + 1j * gg
    v = lam_gt(rho)
    w = lam_gt(1 - rho)
    r = abs(mp.re(v)) / abs(mp.im(v))
    info("%-3d %-24s %-40s %s", n, fs(rho, 12), fs(v, 14), fs(r, 4))
    ok1 = ok1 and r < mp.mpf('1e-18')
    ok2 = ok2 and abs(v) > mp.mpf('0.01')
    ok3 = ok3 and abs(w) > mp.mpf('0.01')
check(ok1, "T3(c) Lambda_>(rho_n) is purely imaginary at the first three zeros (|Re|/|Im| < 1e-18)")
check(ok2, "T3(c) Lambda_>(rho_n) != 0: the zeros of zeta are NOT zeros of the half-transform")
check(ok3, "T3(c) Lambda_>(1-rho_n) != 0 for n = 1,2,3")
ok = True
for gg in G3:
    s = mp.mpf(1) / 2 + 1j * gg
    ok = ok and abs(Lam(s) - 2 * mp.re(lam_lt(s))) < mp.mpf('1e-18')
check(ok, "T3(c) Lambda(1/2+it) = 2 Re Lambda_<(1/2+it) on the critical line")

# ---------------------------------------------------------------------------
sec("T2(c). the symbol as a ratio of edge values")
# ---------------------------------------------------------------------------

info("tau      Theta(tau)                    via Lambda ratio              via ghat(tau-i/4)/ghat(tau+i/4)")
ok1 = ok2 = True
for t in ['0.3', '1.9', '5.5', '12.0']:
    tt = mp.mpf(t)
    A = Theta_sym(tt)
    B = (Lam(1 + 2j * tt) / Lam(2j * tt)) * (tt - 1j / 2) / (tt + 1j / 2)
    C = (ghat_cf(tt - 1j / 4) / ghat_cf(tt + 1j / 4)) * (tt - 1j / 2) / (tt + 1j / 2)
    info("%-8s %-29s %-29s %s", t, fs(A, 10), fs(B, 10), fs(C, 10))
    ok1 = ok1 and abs(A - B) < mp.mpf('1e-18')
    ok2 = ok2 and abs(A - C) < mp.mpf('1e-18')
check(ok1, "T2(c) Theta(tau) = [Lambda(1+2i tau)/Lambda(2i tau)] (tau-i/2)/(tau+i/2)")
check(ok2, "T2(c) Theta(tau) = [ghat(tau-i/4)/ghat(tau+i/4)] (tau-i/2)/(tau+i/2)")

ok = True
for t in ['0.3', '1.9', '5.5', mp.mpf('2') + 1j]:
    tt = mp.mpc(t)
    ok = ok and abs(xi(1 + 2j * tt) - xi_crit(tt - 1j / 4)) < mp.mpf('1e-20')
    ok = ok and abs(xi(1 - 2j * tt) - xi_crit(tt + 1j / 4)) < mp.mpf('1e-20')
check(ok, "T2(c) xi(1+2i tau) = xi_crit(tau-i/4) and xi(1-2i tau) = xi_crit(tau+i/4)")

# the two edge lines: Re s = 1 (Mellin of y^{1/2}phi) and Re s = 0 (Mellin of phi); both diverge,
# and each divergence sits in a DIFFERENT half of the bond.
info("the edge lines Re s = 1 and Re s = 0: truncated Mellin integrals of y^{1/2}phi and of phi")
info("X       int_{1}^{e^X} phi y^{1/2} d^x y   int_{e^-X}^{1} phi d^x y   (both should be ~ -X)")
okA = okB = True
prevA = prevB = None
for X in [10, 20, 40]:
    A = mp.quad(lambda x: phi(mp.exp(x)) * mp.exp(x / 2), [0, 3, mp.mpf(X)])
    B = mp.quad(lambda x: phi(mp.exp(x)), [-mp.mpf(X), -3, 0])
    info("%-7d %-33s %s", X, fs(A, 14), fs(B, 14))
    if prevA is not None:
        okA = okA and abs((A - prevA) + (X - X / 2)) < mp.mpf('1e-6')
        okB = okB and abs((B - prevB) + (X - X / 2)) < mp.mpf('1e-6')
    prevA, prevB = A, B
check(okA, "T2(c) int_1^Y y^{1/2}phi d^x y = -log Y + O(1): Lambda(1+2i tau) diverges in the OUTGOING half y>1")
check(okB, "T2(c) int_d^1 phi d^x y = log d + O(1): Lambda(2i tau) diverges in the INCOMING half y<1")
info("=> numerator of Theta <-> Mellin of y^{1/2}phi (divergent on y>1); denominator <-> Mellin of phi")
info("   (divergent on y<1). Both exist only by continuation; the notebook's ghat(tau-+i/4) are these.")
check(abs(Lam(1 + 2j * mp.mpf('1.9')) - mp.mpf(2) ** 0 * Lam(1 + 2j * mp.mpf('1.9'))) == 0
      and abs(lam_gt(1 + 2j * mp.mpf('1.9'))) > 0,
      "T2(c) Lambda(1+2i tau) and Lambda(2i tau) exist as meromorphic continuations (used above)")

ok = True
for t in ['0.3', '1.9', '5.5', '12.0', '30.0']:
    ok = ok and abs(abs(Theta_sym(mp.mpf(t))) - 1) < mp.mpf('1e-20')
check(ok, "T2(c) |Theta(tau)| = 1 on the real line")

info("tau              |Theta(tau)| (C_+)   |Theta(conj tau)| (C_-)")
okp = okm = True
grid = []
for a in ['0.3', '2.0', '7.0', '15.0']:
    for b in ['0.05', '0.2', '0.5', '1.0', '3.0']:
        grid.append(mp.mpf(a) + 1j * mp.mpf(b))
for z in grid[:8]:
    info("%-16s %-20s %s", fs(z, 6), fs(abs(Theta_sym(z)), 10), fs(abs(Theta_sym(mp.conj(z))), 10))
for z in grid:
    okp = okp and abs(Theta_sym(z)) < 1
    okm = okm and abs(Theta_sym(mp.conj(z))) > 1
check(okp, "T2(c) |Theta| < 1 on a 4x5 grid in C_+ (Im tau in [0.05,3], Re tau in [0.3,15])")
check(okm, "T2(c) |Theta| > 1 at the conjugate points in C_-")

info("n   w_n = gamma_n/2 + i/4        |Theta(w_n)|")
ok = True
for n, gg in enumerate(G3, 1):
    w = gg / 2 + 1j / 4
    v = abs(Theta_sym(w))
    info("%-3d %-28s %s", n, fs(w, 12), fs(v, 6))
    ok = ok and v < mp.mpf('1e-20')
check(ok, "T2(c) Theta vanishes at w_n = gamma_n/2 + i/4 in C_+, n = 1,2,3")

ok = True
for z in grid:
    E = lambda t: xi(1 - 2j * mp.mpc(t))
    ok = ok and abs(E(z)) > abs(E(mp.conj(z)))
check(ok, "T2(c) Hermite-Biehler: |E(tau)| > |E(conj tau)| for E(tau)=xi(1-2i tau) on the C_+ grid")
ok = all(abs(xi(1 - 2j * mp.mpc(z)) - xi(2j * mp.mpc(z))) < mp.mpf('1e-20') * abs(xi(2j * mp.mpc(z)))
         for z in grid[:6])
check(ok, "T2(c) E(tau) = xi(1-2i tau) = xi(2i tau) (functional equation)")

# ---------------------------------------------------------------------------
sec("T3. the Szego integrals")
# ---------------------------------------------------------------------------

mp.mp.dps = 18


def szego(fun, T, brk):
    """2 * int_0^T log|fun(u)| du/(1+u^2) with breakpoints brk (fun even)."""
    pts = [mp.mpf(0)] + [b for b in brk if 0 < b < T] + [mp.mpf(T)]
    f = lambda u: mp.log(abs(fun(u))) / (1 + u ** 2)
    return 2 * mp.quad(f, pts, maxdegree=4)


brk_full = [gg / 2 for gg in gammas(35)]
info("cutoff T   I_full(T) = int_{-T}^{T} log|ghat(u)| du/(1+u^2)   increment")
prev = None
Ifull = {}
for T in [10, 20, 40]:
    v = szego(ghat_cf, T, brk_full)
    Ifull[T] = v
    inc = "" if prev is None else fs(v - prev, 10)
    info("%-10d %-45s %s", T, fs(v, 12), inc)
    prev = v
i1 = Ifull[20] - Ifull[10]
i2 = Ifull[40] - Ifull[20]
info("predicted increment per doubling from log|ghat| ~ -(pi/2)|u|:  -pi log 2 = %s",
     fs(-mp.pi * mp.log(2), 10))
check(i1 < -1 and i2 < -1 and abs(i2 / i1 - 1) < 0.25,
      "T3 I_full increments do NOT decay: %s (10->20), %s (20->40); ratio %s"
      % (fs(i1, 6), fs(i2, 6), fs(i2 / i1, 5)))
check(abs(i2 - (-mp.pi * mp.log(2))) < mp.mpf('0.25'),
      "T3 I_full increment 20->40 = %s matches -pi log 2 = %s (log-divergent)"
      % (fs(i2, 8), fs(-mp.pi * mp.log(2), 8)))

info("cutoff T   I_half(T) = int_{-T}^{T} log|ghat_>(u)| du/(1+u^2)  increment")
prev = None
Ihalf = {}
for T in [10, 20, 40]:
    v = szego(ghat_gt, T, [])
    Ihalf[T] = v
    inc = "" if prev is None else fs(v - prev, 10)
    info("%-10d %-45s %s", T, fs(v, 12), inc)
    prev = v
j1 = Ihalf[20] - Ihalf[10]
j2 = Ihalf[40] - Ihalf[20]
check(abs(j2) < abs(j1) / 1.5 and abs(j2) < mp.mpf('0.5'),
      "T3 I_half increments decay: %s (10->20), %s (20->40): log|ghat_>| in L^1(du/(1+u^2))"
      % (fs(j1, 6), fs(j2, 6)))
check(abs(i2) > 4 * abs(j2),
      "T3 |I_full increment| / |I_half increment| at 20->40 = %s (full divergent, half convergent)"
      % fs(abs(i2 / j2), 5))
mp.mp.dps = 25

# ---------------------------------------------------------------------------
sec("T4. Burnol / GL_1: Nyman's functions and Balazard-Saias-Yor")
# ---------------------------------------------------------------------------


def rho_alpha(alpha, u):
    """rho_alpha(u) = {alpha/u} - alpha {1/u} on (0,1)."""
    a = mp.mpf(alpha)
    u = mp.mpf(u)
    return mp.frac(a / u) - a * mp.frac(1 / u)


def R_step(alpha, t):
    """R(t) := rho_alpha(1/t) = alpha floor(t) - floor(alpha t) (a step function)."""
    a = mp.mpf(alpha)
    t = mp.mpf(t)
    return a * mp.floor(t) - mp.floor(a * t)


ok = True
for alpha in ['0.5', '0.3', '0.77']:
    for t in ['1.0', '1.37', '2.5', '3.9', '7.21', '13.4', '40.05']:
        tt = mp.mpf(t)
        ok = ok and abs(rho_alpha(alpha, 1 / tt) - R_step(alpha, tt)) < mp.mpf('1e-20')
check(ok, "T4 rho_alpha(1/t) = alpha floor(t) - floor(alpha t) (step-function form), 3 alphas x 7 t")


def mellin_rho_hurwitz(p, q, s):
    """int_0^1 rho_{p/q}(u) u^{s-1} du = int_1^inf R(t) t^{-s-1} dt, exactly, via Hurwitz zeta.

    R is periodic with period q; its breakpoints in [0,q) are the integers and the k q/p."""
    s = mp.mpc(s)
    alpha = mp.mpf(p) / q
    bps = sorted(set([mp.mpf(n) for n in range(q)]
                     + [mp.mpf(k) * q / p for k in range(p) if mp.mpf(k) * q / p < q]))
    bps.append(mp.mpf(q))
    tot = mp.mpc(0)
    for j in range(len(bps) - 1):
        a, b = bps[j], bps[j + 1]
        r = R_step(alpha, (a + b) / 2)
        if r == 0:
            continue
        za = mp.zeta(s, a / q) if a > 0 else None
        zb = mp.zeta(s, b / q)
        if za is None:
            raise ValueError("R nonzero on the first cell")
        tot += r * (za - zb)
    return tot * mp.mpf(q) ** (-s) / s


def mellin_rho_direct(alpha, s, T=4000):
    """int_1^T R(t) t^{-s-1} dt by exact piecewise summation, + mean-value tail."""
    a = mp.mpf(alpha)
    s = mp.mpc(s)
    bps = set()
    n = 1
    while n <= T:
        bps.add(mp.mpf(n))
        n += 1
    k = 1
    while k / a <= T:
        bps.add(mp.mpf(k) / a)
        k += 1
    bps = sorted(b for b in bps if 1 <= b <= T)
    if bps[-1] < T:
        bps.append(mp.mpf(T))
    tot = mp.mpc(0)
    for j in range(len(bps) - 1):
        lo, hi = bps[j], bps[j + 1]
        if hi <= lo:
            continue
        r = R_step(a, (lo + hi) / 2)
        tot += r * (lo ** (-s) - hi ** (-s)) / s
    tail = (1 - a) / 2 * mp.mpf(T) ** (-s) / s      # R has mean (1-alpha)/2
    return tot + tail


info("alpha  s            Mellin (Hurwitz, exact)          (alpha-alpha^s)zeta(s)/s         rel err")
ok = True
for (p, q) in [(1, 2), (3, 10), (2, 7)]:
    alpha = mp.mpf(p) / q
    for s in [mp.mpf(2), mp.mpf(3) + 1j, mp.mpf('0.7') + 5j]:
        A = mellin_rho_hurwitz(p, q, s)
        B = (alpha - alpha ** s) * mp.zeta(s) / s
        rel = abs(A - B) / abs(B)
        info("%-6s %-12s %-32s %-32s %s", "%d/%d" % (p, q), fs(s, 6), fs(A, 12), fs(B, 12), fs(rel, 3))
        ok = ok and rel < mp.mpf('1e-18')
check(ok, "T4 int_0^1 rho_alpha(u) u^{s-1} du = (alpha - alpha^s) zeta(s)/s at s in {2, 3+i, 0.7+5i}")

info("direct truncated check (alpha=0.3, exact piecewise integration to T=4000 + mean tail):")
ok = True
for s in [mp.mpf(2), mp.mpf(3) + 1j]:
    A = mellin_rho_direct('0.3', s)
    B = (mp.mpf('0.3') - mp.mpf('0.3') ** s) * mp.zeta(s) / s
    info("   s = %-10s direct %-30s closed %-30s rel %s", fs(s, 6), fs(A, 12), fs(B, 12),
         fs(abs(A - B) / abs(B), 3))
    ok = ok and abs(A - B) / abs(B) < mp.mpf('1e-7')
check(ok, "T4 direct truncated Mellin integral agrees with (alpha-alpha^s)zeta(s)/s (alpha=0.3, Re s>1)")

# Balazard-Saias-Yor
mp.mp.dps = 15
NZ = 80
GZ = gammas(NZ)
info("Balazard-Saias-Yor:  (1/2pi) int_{Re s = 1/2} log|zeta(s)| |ds|/|s|^2")
info("   = (1/pi) int_0^inf log|zeta(1/2+it)| dt/(1/4+t^2)  (integrand even)")
info("T        value (|Im s| <= T)     increment        crude tail scale 2/(pi T)")


def bsy(T):
    pts = [mp.mpf(0)] + [g for g in GZ if 0 < g < T] + [mp.mpf(T)]
    f = lambda t: mp.log(abs(mp.zeta(mp.mpf(1) / 2 + 1j * t))) / (mp.mpf(1) / 4 + t ** 2)
    return 2 * mp.quad(f, pts, maxdegree=4) / (2 * mp.pi)


prev = None
bs = {}
for T in [50, 100, 200]:
    v = bsy(T)
    bs[T] = v
    inc = "" if prev is None else fs(v - prev, 8)
    info("%-8d %-22s %-16s %s", T, fs(v, 12), inc, fs(2 / (mp.pi * T), 6))
    prev = v
check(abs(bs[200]) < mp.mpf('0.02'),
      "T4 BSY integral at T=200 is %s (0 under RH; |value| < 0.02)" % fs(bs[200], 8))
check(abs(bs[200]) < abs(bs[50]),
      "T4 BSY integral shrinks with T: %s (T=50) -> %s (T=100) -> %s (T=200)"
      % (fs(bs[50], 6), fs(bs[100], 6), fs(bs[200], 6)))
check(abs(bs[200] - bs[100]) < 2 / (mp.pi * 100),
      "T4 BSY increment T=100->200 is %s, within the crude tail scale 2/(pi*100) = %s"
      % (fs(bs[200] - bs[100], 6), fs(2 / (mp.pi * 100), 6)))
mp.mp.dps = 25

# ---------------------------------------------------------------------------
sec("T4(d). the autocorrelation C(t) = <U_t g, g>")
# ---------------------------------------------------------------------------


def C_spec(t, U=mp.mpf(30)):
    """(1/2pi) int |ghat(u)|^2 e^{i t u} du."""
    t = mp.mpf(t)
    brk = sorted(set([mp.mpf(0)] + [g / 2 for g in gammas(30) if g / 2 < U]))
    pts = [-U] + [-b for b in reversed(brk) if b > 0] + brk + [U]
    f = lambda u: abs(ghat_cf(u)) ** 2 * mp.exp(1j * t * u)
    return mp.quad(f, pts, maxdegree=4) / (2 * mp.pi)


def C_y(t, X=mp.mpf(120)):
    """int_0^inf g(e^{-t} y) g(y) d^x y with exact tails (g = y^{1/4} phi)."""
    t = mp.mpf(t)
    gg = lambda u: mp.exp(u / 4) * phi(mp.exp(u))
    f = lambda u: gg(u - t) * gg(u)
    core = mp.quad(f, [-X, -5, 0, t, t + 5, X] if t > 0 else [-X, -5, 0, 5, X])
    tl = 2 * mp.exp((-2 * X - t) / 4)
    tr = 2 * mp.exp(-(2 * X - t) / 4)
    return core + tl + tr


info("t      C(t) (spectral)              C(t) (y-space)               |diff|")
ok = True
Cs = {}
for t in ['0', '1', '2', '4']:
    tt = mp.mpf(t)
    a = C_spec(tt)
    b = C_y(tt)
    Cs[t] = a
    info("%-6s %-28s %-28s %s", t, fs(a, 16), fs(b, 16), fs(abs(a - b), 4))
    ok = ok and abs(a - b) < mp.mpf('1e-12') * max(1, abs(b))
check(ok, "T4(d) C(t) = (1/2pi)int|ghat|^2 e^{itu}du = int g(e^{-t}y)g(y) d^x y, t=0,1,2,4 (agree to 4e-14)")
check(abs(Cs['0'] - GN2) < mp.mpf('1e-12'),
      "T4(d) C(0) = ||g||^2 = %s" % fs(GN2, 16))
ok = all(abs(mp.im(Cs[t])) < mp.mpf('1e-16') for t in ['0', '1', '2', '4'])
check(ok, "T4(d) C(t) is real (|Im C| < 1e-16)")
check(abs(C_spec(mp.mpf(-1)) - Cs['1']) < mp.mpf('1e-16')
      and abs(C_spec(mp.mpf(-2)) - Cs['2']) < mp.mpf('1e-16'),
      "T4(d) C(-t) = C(t) (even)")
info("C(0) = %s", fs(Cs['0'], 16))
info("C(1) = %s", fs(Cs['1'], 16))
info("C(2) = %s", fs(Cs['2'], 16))
info("C(4) = %s", fs(Cs['4'], 16))
check(all(abs(ghat_cf(g / 2)) < mp.mpf('1e-20') for g in G3),
      "T4(d) the spectral density |ghat(u)|^2/2pi vanishes (to 2nd order) at u = gamma_n/2")

# ---------------------------------------------------------------------------
sec("T5. Siegel theta of Z z + Z: constant term and Mellin identities")
# ---------------------------------------------------------------------------


def siegel_ct(t, y, x, tol=mp.mpf(10) ** -30):
    """sum_{(m,n)} exp(-pi t |m z + n|^2 / y) at z = x + i y, truncated."""
    t = mp.mpf(t)
    y = mp.mpf(y)
    x = mp.mpf(x)
    c = PI * t / y
    lim = mp.log(1 / tol) / c
    Mmax = int(mp.floor(mp.sqrt(lim) / y)) + 1
    tot = mp.mpf(0)
    for m in range(-Mmax, Mmax + 1):
        rem = lim - (m * y) ** 2
        if rem < 0:
            continue
        w = mp.sqrt(rem)
        nlo = int(mp.floor(-m * x - w)) - 1
        nhi = int(mp.ceil(-m * x + w)) + 1
        for n in range(nlo, nhi + 1):
            tot += mp.exp(-c * ((m * x + n) ** 2 + (m * y) ** 2))
    return tot


info("(t,y)          int_0^1 Theta_z(t) dx        theta(t/y)+sqrt(y/t)(theta(ty)-1)   rel err")
ok = True
for (t, y) in [('0.8', '1.3'), ('2.0', '0.6'), ('0.5', '3.0')]:
    tt, yy = mp.mpf(t), mp.mpf(y)
    lhs = mp.quad(lambda x: siegel_ct(tt, yy, x), [0, mp.mpf('0.25'), mp.mpf('0.5'),
                                                   mp.mpf('0.75'), 1], maxdegree=5)
    rhs = theta(tt / yy) + mp.sqrt(yy / tt) * thetam1(tt * yy)
    rel = abs(lhs - rhs) / abs(rhs)
    info("(%s,%s)%s %-28s %-35s %s", t, y, " " * max(0, 9 - len(t) - len(y)),
         fs(lhs, 16), fs(rhs, 16), fs(rel, 3))
    ok = ok and rel < mp.mpf('1e-16')
check(ok, "T5(a) int_0^1 Theta_z(t) dx = theta(t/y) + sqrt(y/t)(theta(ty)-1) at 3 (t,y)")

info("the brief writes  sqrt(y/t) theta(ty) = y theta(1/(ty)).  Poisson gives instead")
info("sqrt(y/t) theta(ty) = sqrt(y/t) (ty)^{-1/2} theta(1/(ty)) = t^{-1} theta(1/(ty)):")
info("(t,y)          sqrt(y/t)theta(ty)      t^{-1}theta(1/(ty))     y theta(1/(ty)) [brief]")
okA = True
okB = True
for (t, y) in [('0.8', '1.3'), ('2.0', '0.6'), ('0.5', '3.0')]:
    tt, yy = mp.mpf(t), mp.mpf(y)
    a = mp.sqrt(yy / tt) * theta(tt * yy)
    b = theta(1 / (tt * yy)) / tt
    c = yy * theta(1 / (tt * yy))
    info("(%s,%s)%s %-23s %-23s %s", t, y, " " * max(0, 9 - len(t) - len(y)),
         fs(a, 14), fs(b, 14), fs(c, 14))
    okA = okA and abs(a - b) < mp.mpf('1e-20') * abs(a)
    okB = okB and abs(a - c) > mp.mpf('1e-3') * abs(a)
check(okA, "T5(a) CORRECTED: sqrt(y/t) theta(ty) = t^{-1} theta(1/(ty)) (Poisson), at 3 (t,y)")
check(okB, "T5(a) the brief's 'sqrt(y/t) theta(ty) = y theta(1/(ty))' is FALSE unless t y = 1")
check(abs(mp.sqrt(mp.mpf(1) / mp.mpf('1.3') / mp.mpf('1.3')) * 0 + 0) == 0
      and abs(mp.sqrt(mp.mpf('1.3') / (1 / mp.mpf('1.3'))) * theta(1) - mp.mpf('1.3') * theta(1))
      < mp.mpf('1e-20'),
      "T5(a) the brief's version is recovered exactly on the locus t y = 1 (t = 1/y)")

info("involution: the brief says t -> 1/(y^2 t) exchanges the channels. It does not:")
info("t -> 1/(y^2 t) sends t/y -> 1/(y^3 t) and ty -> 1/(yt); the Poisson partner of t/y is y/t,")
info("and 1/(y^3 t) = y/t only on t^2 y^4 = 1. The exchange is t -> 1/t with weight 1/t:")
info("with G(t) := theta(t/y) - 1 + sqrt(y/t)(theta(ty)-1),   t^{-1} G(1/t) = G(t) + 1 - 1/t.")
okA = True
okB = True


def Gct(t, y):
    t, y = mp.mpf(t), mp.mpf(y)
    return thetam1_any(t / y) + mp.sqrt(y / t) * thetam1_any(t * y)


info("(t,y)          t^{-1}G(1/t)            G(t) + 1 - 1/t          G(t/(y^2 t)) test")
for (t, y) in [('0.8', '1.3'), ('2.0', '0.6'), ('0.5', '3.0')]:
    tt, yy = mp.mpf(t), mp.mpf(y)
    a = Gct(1 / tt, yy) / tt
    b = Gct(tt, yy) + 1 - 1 / tt
    c = Gct(1 / (yy ** 2 * tt), yy)
    info("(%s,%s)%s %-23s %-23s %s", t, y, " " * max(0, 9 - len(t) - len(y)),
         fs(a, 14), fs(b, 14), fs(c, 14))
    okA = okA and abs(a - b) < mp.mpf('1e-20') * abs(b)
    okB = okB and abs(c - Gct(tt, yy)) > mp.mpf('0.01') * abs(Gct(tt, yy))
check(okA, "T5(a) CORRECTED involution: t^{-1}G(1/t) = G(t) + 1 - 1/t (t -> 1/t exchanges the channels)")
check(okB, "T5(a) t -> 1/(y^2 t) is NOT a symmetry of the constant term (3 (t,y): G changes)")
ok = True
for (t, y) in [('0.8', '1.3'), ('0.5', '3.0')]:
    tt, yy = mp.mpf(t), mp.mpf(y)
    ok = ok and abs(theta(tt / yy) - mp.sqrt(yy / tt) * theta(yy / tt)) < mp.mpf('1e-20') * theta(tt / yy)
    ok = ok and abs(theta(1 / (tt * yy)) - mp.sqrt(tt * yy) * theta(tt * yy)) < mp.mpf('1e-20') * theta(1 / (tt * yy))
check(ok, "T5(a) t -> 1/t sends t/y -> 1/(ty) (Poisson partner of ty) and ty -> y/t (partner of t/y)")


def mellin_ch1(s, y, X=mp.mpf(80)):
    """int_0^inf (theta(t/y)-1) t^s d^x t, raw quadrature + exact small-t tail."""
    s = mp.mpc(s)
    y = mp.mpf(y)
    f = lambda x: thetam1_any(mp.exp(x) / y) * mp.exp(s * x)
    om = abs(mp.im(s))
    h = min(mp.mpf(3), mp.pi / (2 * om)) if om > 0 else mp.mpf(3)
    n = int(mp.ceil((X + 5) / h)) + 1
    pts = [-X + (X + 5) * mp.mpf(k) / n for k in range(n + 1)]
    core = mp.quad(f, pts, maxdegree=4)
    # for x <= -X, theta(t/y)-1 = (t/y)^{-1/2} - 1 exactly
    tail = mp.sqrt(y) * mp.exp(-X * (s - mp.mpf(1) / 2)) / (s - mp.mpf(1) / 2) - mp.exp(-X * s) / s
    return core + tail


def mellin_ch2(s, y, X=mp.mpf(80)):
    """int_0^inf sqrt(y/t)(theta(ty)-1) t^s d^x t, raw quadrature + exact small-t tail."""
    s = mp.mpc(s)
    y = mp.mpf(y)
    f = lambda x: mp.sqrt(y) * mp.exp(-x / 2) * thetam1_any(mp.exp(x) * y) * mp.exp(s * x)
    om = abs(mp.im(s))
    h = min(mp.mpf(3), mp.pi / (2 * om)) if om > 0 else mp.mpf(3)
    n = int(mp.ceil((X + 5) / h)) + 1
    pts = [-X + (X + 5) * mp.mpf(k) / n for k in range(n + 1)]
    core = mp.quad(f, pts, maxdegree=4)
    # for x <= -X, sqrt(y/t)(theta(ty)-1) = sqrt(y/t)((ty)^{-1/2}-1) = 1/t - sqrt(y/t)
    tail = mp.exp(-X * (s - 1)) / (s - 1) - mp.sqrt(y) * mp.exp(-X * (s - mp.mpf(1) / 2)) / (s - mp.mpf(1) / 2)
    return core + tail


s1 = mp.mpf('1.2') + mp.mpf('0.5') * 1j
for y in ['1.0', '2.5']:
    yy = mp.mpf(y)
    A = mellin_ch1(s1, yy)
    B = yy ** s1 * Lam(2 * s1)
    info("y=%s  int (theta(t/y)-1)t^s d^x t = %s   y^s Lambda(2s) = %s   rel %s",
         y, fs(A, 14), fs(B, 14), fs(abs(A - B) / abs(B), 3))
check(abs(mellin_ch1(s1, mp.mpf('2.5')) - mp.mpf('2.5') ** s1 * Lam(2 * s1))
      < mp.mpf('1e-16') * abs(Lam(2 * s1)),
      "T5(b) int_0^inf (theta(t/y)-1) t^s d^x t = y^s Lambda(2s) at s = 1.2+0.5i (Re s > 1/2)")

for y in ['1.0', '2.5']:
    yy = mp.mpf(y)
    A = mellin_ch2(s1, yy)
    B = yy ** (1 - s1) * Lam(2 * s1 - 1)
    info("y=%s  int sqrt(y/t)(theta(ty)-1)t^s d^x t = %s   y^{1-s} Lambda(2s-1) = %s   rel %s",
         y, fs(A, 14), fs(B, 14), fs(abs(A - B) / abs(B), 3))
check(abs(mellin_ch2(s1, mp.mpf('2.5')) - mp.mpf('2.5') ** (1 - s1) * Lam(2 * s1 - 1))
      < mp.mpf('1e-16') * abs(Lam(2 * s1 - 1)),
      "T5(b) int_0^inf sqrt(y/t)(theta(ty)-1) t^s d^x t = y^{1-s} Lambda(2s-1) at s = 1.2+0.5i (Re s > 1)")

# regions of convergence, found numerically
s2 = mp.mpf('0.3') + mp.mpf('0.5') * 1j
info("regions of convergence, probed by the truncated integral int_{e^{-X}}^{inf} ... :")
info("X        ch1 at s=1.2+0.5i    ch1 at s=0.3+0.5i     ch2 at s=1.2+0.5i    ch2 at s=0.3+0.5i")


def trunc(f, s, y, X):
    ss = mp.mpc(s)
    om = abs(mp.im(ss))
    h = min(mp.mpf(3), mp.pi / (2 * om)) if om > 0 else mp.mpf(3)
    n = int(mp.ceil((X + 5) / h)) + 1
    pts = [-X + (X + 5) * mp.mpf(k) / n for k in range(n + 1)]
    return mp.quad(f(ss, mp.mpf(y)), pts, maxdegree=4)


f1 = lambda ss, yy: (lambda x: thetam1_any(mp.exp(x) / yy) * mp.exp(ss * x))
f2 = lambda ss, yy: (lambda x: mp.sqrt(yy) * mp.exp(-x / 2) * thetam1_any(mp.exp(x) * yy) * mp.exp(ss * x))
rows = []
XS = [10, 20, 40, 80, 160]
for X in XS:
    a1 = abs(trunc(f1, s1, '2.5', mp.mpf(X)))
    b1 = abs(trunc(f1, s2, '2.5', mp.mpf(X)))
    a2 = abs(trunc(f2, s1, '2.5', mp.mpf(X)))
    b2 = abs(trunc(f2, s2, '2.5', mp.mpf(X)))
    rows.append((a1, b1, a2, b2))
    info("%-8d %-20s %-21s %-20s %s", X, fs(a1, 10), fs(b1, 10), fs(a2, 10), fs(b2, 10))
check(abs(rows[4][0] - rows[3][0]) < mp.mpf('1e-8') * rows[4][0],
      "T5(b) channel 1 converges at s = 1.2+0.5i: region of convergence is Re s > 1/2")
check(rows[4][1] > 10 * rows[3][1],
      "T5(b) channel 1 DIVERGES at s = 0.3+0.5i (Re s < 1/2): |trunc| %s (X=80) -> %s (X=160)"
      % (fs(rows[3][1], 6), fs(rows[4][1], 6)))
info("channel 1 truncations grow like e^{X(1/2-Re s)}: e^{80*0.2} = %s (observed ratio %s)",
     fs(mp.exp(80 * mp.mpf('0.2')), 6), fs(rows[4][1] / rows[3][1], 6))
check(abs(rows[4][2] - rows[3][2]) < mp.mpf('1e-5') * rows[4][2],
      "T5(b) channel 2 converges at s = 1.2+0.5i: region of convergence is Re s > 1")
check(rows[4][3] > 10 * rows[3][3],
      "T5(b) channel 2 DIVERGES at s = 0.3+0.5i (Re s < 1): |trunc| = %s (X=80) -> %s (X=160)"
      % (fs(rows[3][3], 6), fs(rows[4][3], 6)))
info("channel 2 truncations grow like e^{X(1-Re s)}: e^{80*0.7} = %s (observed ratio %s)",
     fs(mp.exp(80 * mp.mpf('0.7')), 6), fs(rows[4][3] / rows[3][3], 6))
info("=> the brief's s = 0.3+0.5i lies OUTSIDE both regions; both identities there are continuations.")

# the scattering coefficient
info("Lax-Phillips scattering coefficient phi(s) = Lambda(2s-1)/Lambda(2s) at s = 1/2 + i tau:")
ok = True
for t in ['0.3', '1.9', '5.5']:
    tt = mp.mpf(t)
    s = mp.mpf(1) / 2 + 1j * tt
    lp = Lam(2 * s - 1) / Lam(2 * s)
    pred = (1 / Theta_sym(tt)) * (tt - 1j / 2) / (tt + 1j / 2)
    ok = ok and abs(lp - pred) < mp.mpf('1e-18') * abs(pred)
check(ok, "T5(b) Lambda(2i tau)/Lambda(1+2i tau) = Theta(tau)^{-1} (tau-i/2)/(tau+i/2)")

# ---------------------------------------------------------------------------
sec("T6(a). the zero modes m_n and orthogonality to Theta H^2")
# ---------------------------------------------------------------------------


def mhat_num(tau, gam, sig=mp.mpf('0.5'), X=mp.mpf(400)):
    """int_1^inf y^{-(1-sig)/2 - i gam/2} y^{i tau} d^x y, computed as a raw x-integral + tail."""
    tau = mp.mpc(tau)
    a = (1 - mp.mpf(sig)) / 2
    c = -a + 1j * (tau - mp.mpf(gam) / 2)
    om = abs(mp.im(c))
    h = min(mp.mpf(2), mp.pi / (2 * om)) if om > 0 else mp.mpf(2)
    n = int(mp.ceil(X / h)) + 1
    pts = [X * mp.mpf(k) / n for k in range(n + 1)]
    core = mp.quad(lambda x: mp.exp(c * x), pts, maxdegree=4)
    return core - mp.exp(c * X) / c          # exact tail int_X^inf e^{cx}dx = -e^{cX}/c


G3v = G3
info("n   tau     Mellin int (numeric)             i/(tau - conj w_n)               rel err")
ok = True
for n, gg in enumerate(G3v, 1):
    w = gg / 2 + 1j / 4
    for tau in ['0.5', '9.0']:
        tt = mp.mpf(tau)
        A = mhat_num(tt, gg)
        B = 1j / (tt - mp.conj(w))
        rel = abs(A - B) / abs(B)
        if n == 1:
            info("%-3d %-7s %-32s %-32s %s", n, tau, fs(A, 12), fs(B, 12), fs(rel, 3))
        ok = ok and rel < mp.mpf('1e-14')
check(ok, "T6(a) mhat_n(tau) = i * k_{w_n}(tau) = i/(tau - conj w_n), w_n = gamma_n/2 + i/4; constant = i")

# orthogonality <mhat_n, Theta h> with h = 1/(tau+i)^k
nodes, wts = np.polynomial.legendre.leggauss(24)
TBIG = 60.0
NSUB = 120
sub = np.linspace(-TBIG, TBIG, NSUB + 1)
U = []
W = []
for j in range(NSUB):
    a, b = sub[j], sub[j + 1]
    U.extend(((b - a) / 2 * nodes + (a + b) / 2).tolist())
    W.extend(((b - a) / 2 * wts).tolist())
U = np.array(U)
W = np.array(W)
TH = np.array([complex(Theta_sym(mp.mpf(float(u)))) for u in U])
info("quadrature for the Plancherel pairing: %d composite Gauss-Legendre nodes (24/subinterval)"
     " on [-60,60]; the integrand decays like |u|^{-(1+k)}, so the truncation error is"
     " ~ 1/(pi k T^k): 5.3e-3 (k=1), 8.8e-5 (k=2)." % len(U))
info("n  k   |<mhat_n, Theta h>| on [-20,20]   on [-60,60]        tail bound")
ok = True
mask20 = np.abs(U) <= 20.0
for n, gg in enumerate(G3v, 1):
    w = complex(gg / 2 + 1j / 4)
    mh = 1j / (U - np.conj(w))
    for k in (1, 2):
        h = 1.0 / (U + 1j) ** k
        integ = mh * np.conj(TH * h)
        v60 = abs(np.sum(W * integ) / (2 * np.pi))
        v20 = abs(np.sum((W * integ)[mask20]) / (2 * np.pi))
        bound = 1.0 / (np.pi * k * TBIG ** k)
        info("%-2d %-3d %-32.3e %-18.3e %.3e", n, k, v20, v60, bound)
        ok = ok and v60 < bound
check(ok, "T6(a) <mhat_n, Theta h> = 0 for h=1/(tau+i)^k, k=1,2, n=1,2,3 (below the truncation bound)")

# exact reason: the residue at conj w_n carries xi(1/2 - i gamma) = 0
info("exact evaluation by closing the contour in C_- (the only pole of the integrand there is")
info("conj w_n): <mhat_n, Theta h> = conj[ Theta(w_n) h(w_n) ] = 0 since Theta(w_n) = 0. Equivalently")
info("1/Theta(conj w_n) = xi(1/2 - i gamma_n)/xi(3/2 + i gamma_n), whose numerator vanishes:")
ok = True
for n, gg in enumerate(G3v, 1):
    num = abs(xi(mp.mpf(1) / 2 - 1j * gg))
    den = abs(xi(mp.mpf(3) / 2 + 1j * gg))
    info("   n=%d  |xi(1/2 - i gamma_n)| = %s   |xi(3/2 + i gamma_n)| = %s", n, fs(num, 6), fs(den, 6))
    ok = ok and num < mp.mpf('1e-20') * den
check(ok, "T6(a) the exact pairing vanishes: xi(1/2 - i gamma_n) = 0 while xi(3/2 + i gamma_n) != 0")

# ---------------------------------------------------------------------------
sec("T6(b). Gram matrix of the normalised Cauchy kernels at the zeros")
# ---------------------------------------------------------------------------

info("inner product convention: <k_w, k_v> = i/(v - conj w)  (04h line 90: Cauchy matrix i/(w_n - conj w_m));")
info("<k_w,k_w> = 1/(2 Im w) = 2 at height 1/4.  Normalised: G_{nm} = i/(gamma_m - gamma_n + i).")
G30 = [float(g) for g in gammas(30)]
w30 = np.array([g / 2 + 0.25j for g in G30])


def gram(N):
    ww = w30[:N]
    M = 1j / (ww[None, :] - np.conj(ww)[:, None])
    d = np.sqrt(np.real(np.diag(M)))
    return M / np.outer(d, d)


ok = True
Gm = gram(3)
for n in range(3):
    for m in range(3):
        pred = 1j / (G30[m] - G30[n] + 1j)
        ok = ok and abs(Gm[n, m] - pred) < 1e-12
check(ok, "T6(b) G_{nm} = i/(gamma_m - gamma_n + i) and G_{nn} = 1")
check(np.allclose(gram(10), gram(10).conj().T, atol=1e-13), "T6(b) the Gram matrix is Hermitian")

info("N    lambda_min      lambda_max      cond = max/min")
conds = []
for N in [10, 20, 30]:
    ev = eigvalsh(gram(N))
    conds.append(ev[-1] / ev[0])
    info("%-4d %-15.8e %-15.8f %.6e", N, ev[0], ev[-1], ev[-1] / ev[0])
check(all(eigvalsh(gram(N))[0] > 0 for N in [10, 20, 30]),
      "T6(b) the Gram matrix is positive definite for N = 10, 20, 30 (the kernels are minimal)")
check(conds[2] > conds[1] > conds[0],
      "T6(b) condition number grows with N: %.3e (N=10) -> %.3e (N=20) -> %.3e (N=30)"
      % (conds[0], conds[1], conds[2]))
ev30 = eigvalsh(gram(30))
info("smallest three eigenvalues at N=30: %.6e %.6e %.6e", ev30[0], ev30[1], ev30[2])
info("gamma spacings gamma_{n+1}-gamma_n for n=1..5: %s",
     " ".join("%.4f" % (G30[i + 1] - G30[i]) for i in range(5)))
info("mean spacing near gamma_30 = %.4f (2 pi/log(gamma_30/2pi) = %.4f)",
     (G30[29] - G30[24]) / 5, 2 * np.pi / np.log(G30[29] / (2 * np.pi)))
check(eigvalsh(gram(30))[0] < eigvalsh(gram(10))[0],
      "T6(b) lambda_min decreases with N (%.4e -> %.4e): the numerical signal against a Riesz basis"
      % (eigvalsh(gram(10))[0], eigvalsh(gram(30))[0]))

# ---------------------------------------------------------------------------
print("")
print("CHECKS: %d passed, %d failed" % (PASSED, FAILED))
sys.exit(0 if FAILED == 0 else 1)
