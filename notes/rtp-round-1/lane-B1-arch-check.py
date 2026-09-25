#!/usr/bin/env python3
"""Lane B1 numerical check (claude:opus, 2026-09-24): sign of the archimedean local form.

Yoshida's normalisation (refs/src/yoshida-1992, section 1): for phi supported in [-a, a] and
F = phi * phi~, the Weil form is
  T(F) = pole(F) - (log pi) F(0) - (prime terms) + (1/2pi) int |phi^(t)|^2 Re psi(1/4 + i t/2) dt,
with pole(F) = int F(x)(e^{x/2} + e^{-x/2}) dx = 2 E |int phi(x) e^{x/2} dx|^2, E = +1 (even phi), -1 (odd).
For a <= log2/2 the prime terms vanish. Prints:
  1. t0 with Re psi(1/4 + i t0/2) = 0 (Yoshida quotes t0 = 2.0320...);
  2. the zero of h_+(t) = -log pi + Re psi(1/4 + i t/2) (Connes-Consani's archimedean symbol) and h_+(0);
  3. for the even box phi = (2a)^{-1/2} 1_[-a,a], a = log2/2 (which lies in Yoshida's K(a)):
     the archimedean part -log pi + (1/2pi) int |phi^|^2 Re psi, the pole part, and their sum.
"""
import mpmath as mp

mp.mp.dps = 15
f = lambda t: mp.re(mp.digamma(mp.mpf(1) / 4 + 0.5j * t))
print("t0 (Re psi(1/4+it/2)=0):", mp.findroot(f, 2.0))
h = lambda t: f(t) - mp.log(mp.pi)
print("zero of h_+:", mp.findroot(h, 6.3), " h_+(0) =", h(0))

a = mp.log(2) / 2
ph2 = lambda t: 2 * mp.sin(a * t) ** 2 / (a * t ** 2) if t != 0 else 2 * a   # |phi^(t)|^2, ||phi||=1
T = 2000
body = 2 * mp.quad(lambda t: ph2(t) * f(t), mp.linspace(0, T, T + 1))
tail = 2 * mp.quad(lambda t: mp.log(t / 2) / (a * t ** 2), [T, mp.inf])   # sin^2 -> 1/2, Re psi ~ log(t/2)
arch = -mp.log(mp.pi) + (body + tail) / (2 * mp.pi)
pole = 2 * mp.quad(lambda x: mp.e ** (x / 2) / mp.sqrt(2 * a), [-a, a]) ** 2
print("even box, a=log2/2: archimedean part =", arch, " pole part =", pole, " total =", arch + pole)
