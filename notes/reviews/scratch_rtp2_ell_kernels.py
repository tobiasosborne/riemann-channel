#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane E (claude:opus, 2026-09-26).  E1/E2 algebra, checked numerically:
 (1) Mellin identity int_0^inf exp(-2 pi u/sqrt C) u^s du/u = (sqrt C/2pi)^s Gamma(s);
 (2) Hankel-kernel identity int_0^inf K_C(v) v^s dv/v = (C/4pi^2)^s Gamma(1+s)/Gamma(1-s),
     K_C(v) = (2pi/sqrt C) sqrt v J_1(4 pi sqrt(v/C)); and which DLMF 10.22.43 exponent mu it needs
     (DLMF: int_0^inf t^{mu-1} J_nu(t) dt = 2^{mu-1} Gamma((nu+mu)/2)/Gamma((nu-mu)/2+1));
 (3) the prediction constants 4pi/ln10, 8pi/ln10, per sqrt(x) for C = 11, 14, the imported x^{9/2} slope 13-50,
     round-1 zeta slopes 5.339 / 5.379 from the certified A1 numbers;
 (4) E2 / E5 algebra: T*, S_max, the zero e T*, the action A = int_0^T* [log x - h_asym] dt = 2 pi S_max.
Deterministic."""
import mpmath as mp
mp.mp.dps = 30
checks = fails = 0
def check(ok, msg):
    global checks, fails
    checks += 1; fails += (not ok); print(('ok  ' if ok else 'FAIL') + ' ' + msg)
C = mp.mpf(11)
for s in (mp.mpf('0.7'), mp.mpf('2.3')):
    I = mp.quad(lambda u: mp.e**(-2 * mp.pi * u / mp.sqrt(C)) * u**(s - 1), [0, 1, mp.inf])
    check(abs(I / ((mp.sqrt(C) / (2 * mp.pi))**s * mp.gamma(s)) - 1) < 1e-20, f'(1) Mellin identity at s={s}')
K = lambda v: (2 * mp.pi / mp.sqrt(C)) * mp.sqrt(v) * mp.besselj(1, 4 * mp.pi * mp.sqrt(v / C))
for s in (mp.mpf('-0.6'), mp.mpf('-0.3'), mp.mpf('0.1')):
    # substitute t = 4 pi sqrt(v/C): integrand (C/16pi^2)^s J_1(t) t^{2s}; oscillatory tail by quadosc
    I = (C / (16 * mp.pi**2))**s * mp.quadosc(lambda t: mp.besselj(1, t) * t**(2 * s), [0, mp.inf], zeros=lambda n: mp.besseljzero(1, n))
    rhs = (C / (4 * mp.pi**2))**s * mp.gamma(1 + s) / mp.gamma(1 - s)
    dl = lambda mu: 2**(mu - 1) * mp.gamma((1 + mu) / 2) / mp.gamma((1 - mu) / 2 + 1)
    check(abs(I / rhs - 1) < 1e-4, f'(2) Hankel identity (direct oscillatory quadrature, conditionally convergent; rel. tol 1e-4) at s={s}: lhs {mp.nstr(I, 15)} rhs {mp.nstr(rhs, 15)}')
    check(abs((C / (16 * mp.pi**2))**s * dl(2 * s + 1) / rhs - 1) < 1e-25, f'(2) DLMF 10.22.43 reproduces it with mu = 2s+1')
    print(f'     with mu = 2s (as printed in the report) DLMF gives {mp.nstr((C / (16 * mp.pi**2))**s * dl(2 * s), 12)} (not the identity)')
d4, d8 = 4 * mp.pi / mp.log(10), 8 * mp.pi / mp.log(10)
print('(3) 4pi/ln10 =', mp.nstr(d4, 9), ' 8pi/ln10 =', mp.nstr(d8, 9), ' per sqrt x: C=11', mp.nstr(d8 / mp.sqrt(11), 8), ' C=14', mp.nstr(d8 / mp.sqrt(14), 8))
check(abs(d8 - mp.mpf('10.9150108')) < 5e-8 and abs(d8 / mp.sqrt(11) - mp.mpf('3.2909996')) < 5e-8 and abs(d8 / mp.sqrt(14) - mp.mpf('2.9171594')) < 5e-8, '(3) E1b constants as printed')
sl = d4 - mp.mpf(9) / 2 * (mp.log10(50) - mp.log10(13)) / 37
check(abs(sl - mp.mpf('5.3863535')) < 5e-8, f'(3) x^(9/2) e^(-4 pi x) slope 13-50 = {mp.nstr(sl, 9)} (round-1 review: 5.386)')
e13, e25, e50 = mp.mpf('2.85407e-59'), mp.mpf('2.42562e-123'), mp.mpf('2.80881e-258')   # A1 certified (N=200, 260) and review tail (N=420)
s1325 = (mp.log10(e13) - mp.log10(e25)) / 12; s1350 = (mp.log10(e13) - mp.log10(e50)) / 37
check(abs(s1325 - mp.mpf('5.33922')) < 5e-6 and abs(s1350 - mp.mpf('5.378566')) < 5e-6, f'(3) zeta slopes {mp.nstr(s1325, 7)}, {mp.nstr(s1350, 7)} as tabulated')
for x in (13, 25, 50, 100):
    x = mp.mpf(x); L = mp.log(x)
    S = lambda T: T * L / (2 * mp.pi) - T / mp.pi * mp.log(mp.sqrt(C) * T / (2 * mp.pi * mp.e))
    Ts = mp.findroot(lambda T: mp.diff(S, T), 2 * mp.pi * mp.sqrt(x / C))
    Tz = mp.findroot(S, mp.e * Ts)
    A = mp.quad(lambda t: L - mp.log(C * t**2 / (4 * mp.pi**2)), [0, Ts])
    check(abs(Ts / (2 * mp.pi * mp.sqrt(x / C)) - 1) < 1e-20 and abs(Tz / (mp.e * Ts) - 1) < 1e-20 and abs(S(Ts) - 2 * mp.sqrt(x / C)) < 1e-20
          and abs(A - 4 * mp.pi * mp.sqrt(x / C)) < 1e-15, f'(4) x={int(x)}: T*={mp.nstr(Ts, 8)}, S_max=2 sqrt(x/C)={mp.nstr(S(Ts), 8)}, zero at e T*, A={mp.nstr(A, 8)}=4 pi sqrt(x/C); N*=sqrt(x/C) log x={mp.nstr(mp.sqrt(x / C) * L, 6)}')
print(f'# checks: {checks} run, {fails} failed')
