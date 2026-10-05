"""Checks for notes/adelic-gkp/adelic-gkp.md.

Conventions (Tate): psi_inf(x) = exp(-2 pi i x), psi_p(x) = exp(2 pi i {x}_p), so
psi_fin(r) = exp(2 pi i r) for r in Q; self-dual measures, vol(Zhat) = 1.

C1  Level-N Bell structure + self-duality: for f = g (x) phi, phi = sum_a phi_a 1_{a+N Zhat},
    Theta(f) = sum_a phi_a sum_n g(a+Nn)  equals  Theta(fhat) =
    sum_{y in N^-1 Z} ghat(y) N^-1 sum_a phi_a exp(2 pi i a y).
C2  Joint logical Paulis X_b (x) X_b and Z_b (x) Z_b^-1 (b in N^-1 Z) fix Theta at level N.
C3  Modular laws of theta(tau) = <Theta, exp(i pi tau x^2) (x) 1_Zhat>:
    S: theta(-1/tau) = sqrt(tau/i) theta(tau); T^2: theta(tau+2) = theta(tau);
    T fails: theta(tau+1) = sum (-1)^n e^{i pi tau n^2} (the 2-adic vacuum).
C4  2-adic origin of the sign: psi_2(x^2/2) = (-1)^x on Z (x mod 2 is x^2 mod 2).
C5  Tate/Riemann: int_0^oo (theta(i a^2) - 1) a^s da/a = pi^{-s/2} Gamma(s/2) zeta(s), Re s > 1.
C6  Rank-one GNS check of the sign of an off-line pair: the form
    z conj(w) + w conj(z) on C^2 has signature (1,1).
"""
import mpmath as mp
import random

mp.mp.dps = 40
random.seed(20261002)
ok = 0
fail = 0


def report(name, err, tol):
    global ok, fail
    good = err < tol
    ok += good
    fail += (not good)
    print(f"{'PASS' if good else 'FAIL'}  {name}: err = {mp.nstr(err, 5)}")


def gauss(x0, s):
    # g(x) = exp(-pi (x-x0)^2 / s^2) * exp(2 pi i k x) with a random chirp-free phase k
    return lambda x: mp.exp(-mp.pi * (x - x0) ** 2 / s ** 2)


def gauss_hat(x0, s):
    # ghat(y) = int g(x) exp(-2 pi i x y) dx = s exp(-pi s^2 y^2) exp(-2 pi i x0 y)
    return lambda y: s * mp.exp(-mp.pi * s ** 2 * y ** 2) * mp.exp(-2j * mp.pi * x0 * y)


# C1, C2
for N in [1, 2, 3, 6, 12]:
    labels = [mp.mpf(k) / N for k in range(N * N)]  # a in N^-1 Z / N Z
    for trial in range(3):
        x0 = mp.mpf(random.uniform(-0.7, 0.7))
        s = mp.mpf(random.uniform(0.6, 2.5)) * N
        g, gh = gauss(x0, s), gauss_hat(x0, s)
        phi = [mp.mpc(random.gauss(0, 1), random.gauss(0, 1)) for _ in labels]
        R = 40
        lhs = mp.fsum(phi[i] * mp.fsum(g(a + N * n) for n in range(-R, R + 1)) for i, a in enumerate(labels))
        Y = 40 * N
        rhs = mp.fsum(gh(mp.mpf(k) / N) / N * mp.fsum(phi[i] * mp.exp(2j * mp.pi * a * k / N) for i, a in enumerate(labels))
                      for k in range(-Y, Y + 1))
        report(f"C1 Poisson at level N={N}, trial {trial}", abs(lhs - rhs) / (abs(lhs) + 1e-30), mp.mpf(10) ** -25)
        # C2: X_b (x) X_b: shift both factors by b in N^-1 Z; label a -> a+b mod N
        b = mp.mpf(random.randrange(-3 * N, 3 * N)) / N
        # phi(. + b) = sum_a phi_a 1_{a - b + N Zhat}; g(. + b); Theta = sum_a phi_a sum_n g((a - b + N n) + b)
        lhs_X2 = mp.fsum(phi[i] * mp.fsum(g(((a - b) % N) + N * n + b) for n in range(-R - 4, R + 5))
                         for i, a in enumerate(labels))
        lhs_X = lhs
        report(f"C2 X_b(x)X_b invariance N={N}, trial {trial}", abs(lhs_X - lhs_X2) / abs(lhs_X), mp.mpf(10) ** -25)
        # Z_b (x) Z_b^-1: multiply by psi(b x) = psi_inf(b x_inf) psi_fin(b x_fin); on a+N Zhat psi_fin(b x) = e^{2 pi i b a}
        lhs_Z = mp.fsum(phi[i] * mp.exp(2j * mp.pi * b * a) *
                        mp.fsum(g(a + N * n) * mp.exp(-2j * mp.pi * b * (a + N * n)) for n in range(-R, R + 1))
                        for i, a in enumerate(labels))
        report(f"C2 Z_b(x)Z_b^-1 invariance N={N}, trial {trial}", abs(lhs_Z - lhs) / abs(lhs), mp.mpf(10) ** -25)


def theta(tau, sign=False):
    return mp.fsum(((-1) ** n if sign else 1) * mp.exp(1j * mp.pi * tau * n * n) for n in range(-60, 61))


for tau in [mp.mpc(0.3, 0.8), mp.mpc(-1.1, 0.5), mp.mpc(0.05, 1.7)]:
    report(f"C3 S law at tau={tau}", abs(theta(-1 / tau) - mp.sqrt(tau / 1j) * theta(tau)), mp.mpf(10) ** -25)
    report(f"C3 T^2 law at tau={tau}", abs(theta(tau + 2) - theta(tau)), mp.mpf(10) ** -25)
    report(f"C3 T maps to (-1)^n twist at tau={tau}", abs(theta(tau + 1) - theta(tau, sign=True)), mp.mpf(10) ** -25)
    print(f"      |theta(tau+1) - theta(tau)| = {mp.nstr(abs(theta(tau + 1) - theta(tau)), 5)} (nonzero: T is not a symmetry)")

# C4: psi_2(x^2/2) for x in Z: fractional 2-adic part of x^2/2 is 1/2 iff x odd
for x in range(-7, 8):
    frac = mp.mpf(x * x % 2) / 2
    report(f"C4 psi_2(x^2/2) = (-1)^x at x={x}", abs(mp.exp(2j * mp.pi * frac) - (-1) ** x), mp.mpf(10) ** -30)

# C5: Tate/Riemann Mellin
for s in [mp.mpf(3), mp.mpf(2.5), mp.mpc(2, 3)]:
    # theta(i a^2) - 1; for a < 1 use theta(i a^2) = a^-1 theta(i / a^2) (C3's S law) to evaluate
    th = lambda a: mp.jtheta(3, 0, mp.exp(-mp.pi * a * a)) if a >= 1 else mp.jtheta(3, 0, mp.exp(-mp.pi / (a * a))) / a
    integrand = lambda a: (th(a) - 1) * a ** s / a
    val = mp.quad(integrand, [0, 0.25, 1, 4, mp.inf])
    target = mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
    report(f"C5 Tate integral at s={s}", abs(val - target) / abs(target), mp.mpf(10) ** -20)

# C6: signature of the hyperbolic form 2 Re(z conj w)
M = mp.matrix([[0, 1], [1, 0]])
ev = mp.eig(M)[0]
report("C6 off-line pair form has signature (1,1)", abs(sorted([mp.re(e) for e in ev])[0] + 1) + abs(sorted([mp.re(e) for e in ev])[1] - 1),
       mp.mpf(10) ** -30)

print(f"\n{ok} passed, {fail} failed")
