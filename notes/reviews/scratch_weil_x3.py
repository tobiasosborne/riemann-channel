#!/usr/bin/env python3
"""X3: independent normalisation check of the Weil explicit formula in the notebook's
time variable v = t (the variable of Z(t)), to settle the weight and sign of the prime
atoms in the centred trace.  Reviewer claude:opus, 2026-09-12.

Convention under test (astra's H-ZEF):
    H_h(s) = int h(v) e^{(s-1/2) v/2} dv,   K(v) = sum_rho e^{(rho-1/2) v/2},
    <K,h> = sum_rho H_h(rho)
          = H_h(0)+H_h(1) - 2 log(pi) h(0) + (1/2pi) int H_h(1/2+iy) Re psi(1/4+iy/2) dy
            - 2 sum_n Lambda(n) n^{-1/2} [ h(2 log n) + h(-2 log n) ].
Test function: h(v) = exp(-(v-v0)^2/2s^2) + exp(-(v+v0)^2/2s^2)  (real, even).
Then H_h(1/2+iy) = 2 s sqrt(2pi) e^{-y^2 s^2/8} cos(y v0 / 2).
"""
import mpmath as mp
mp.mp.dps = 25
s = mp.mpf('0.13')
NZ = 70
print(f"  test width s = {s}, number of zeta zeros used: {NZ}")
zeros = [mp.im(mp.zetazero(k)) for k in range(1, NZ + 1)]
print(f"  gamma_1 = {zeros[0]}, gamma_{NZ} = {zeros[-1]}, damping e^{{-gamma^2 s^2/8}} at the last zero = "
      f"{mp.e**(-zeros[-1]**2*s**2/8)}")

def H(y, v0):                       # H_h(1/2 + i y)
    return 2 * s * mp.sqrt(2 * mp.pi) * mp.e ** (-y ** 2 * s ** 2 / 8) * mp.cos(y * v0 / 2)
def h(v, v0):
    return mp.e ** (-(v - v0) ** 2 / (2 * s ** 2)) + mp.e ** (-(v + v0) ** 2 / (2 * s ** 2))
def Hreal(sigma, v0):               # H_h(s) for real s: int h(v) e^{(s-1/2)v/2} dv
    a = (sigma - mp.mpf(1) / 2) / 2
    return mp.sqrt(2 * mp.pi) * s * (mp.e ** (a * v0 + a ** 2 * s ** 2 / 2) + mp.e ** (-a * v0 + a ** 2 * s ** 2 / 2))

def vonmangoldt(n):
    f = mp.mpf(0)
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97):
        m, k = n, 0
        while m % p == 0: m //= p; k += 1
        if k and m == 1: return mp.log(p)
    return mp.mpf(0)

print()
print(f"{'v0':>7} {'zero sum (LHS)':>20} {'endpoints':>14} {'contact':>12} {'archimedean':>14} "
      f"{'residual':>14} {'-2 Lam n^-1/2 h':>16} {'ratio':>9}")
for v0 in [mp.mpf('1.3863'), mp.mpf('2.1972'), mp.mpf('2.7726'), mp.mpf('3.2189'), mp.mpf('3.8918'), mp.mpf('2.5')]:
    lhs = 2 * mp.fsum([H(g, v0) for g in zeros])          # both signs of gamma
    endp = Hreal(mp.mpf(0), v0) + Hreal(mp.mpf(1), v0)
    contact = -2 * mp.log(mp.pi) * h(0, v0)
    arch = mp.quad(lambda y: H(y, v0) * mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * y / 2)) / (2 * mp.pi),
                   [-200, -20, -1, 0, 1, 20, 200])
    resid = lhs - endp - contact - arch
    prime = -2 * mp.fsum([vonmangoldt(n) / mp.sqrt(n) * (h(2 * mp.log(n), v0) + h(-2 * mp.log(n), v0))
                          for n in range(2, 400)])
    print(f"{float(v0):7.4f} {float(lhs):20.10f} {float(endp):14.6f} {float(contact):12.6f} {float(arch):14.6f} "
          f"{float(resid):14.8f} {float(prime):16.8f} {float(resid/prime):9.6f}")
print()
print("  ratio residual / (-2 Lambda(n) n^{-1/2} atoms) = 1 confirms coefficient AND sign.")
print("  With the shard's weight +Lambda(n) n^{-1/2} at v = 2 log n the ratio would be -2.")
print()
print("  atom-by-atom, at v0 = 2 log n the dominant atom is n:")
for n in (2, 3, 4, 5, 7):
    v0 = 2 * mp.log(n)
    print(f"    n={n}: 2 log n = {float(v0):.6f},  Lambda(n)/sqrt(n) = {float(vonmangoldt(n)/mp.sqrt(n)):.6f},"
          f"  centred weight -2 Lambda(n)/sqrt n = {float(-2*vonmangoldt(n)/mp.sqrt(n)):+.6f},"
          f"  uncentred (x e^{{-v/4}}) = {float(-2*vonmangoldt(n)/n):+.6f}")
