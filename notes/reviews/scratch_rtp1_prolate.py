#!/usr/bin/env python3
"""REFUTE lane R, RTP-1 (claude:opus, 2026-09-24).  Claim C12(iii): compare the certified eps_N (reviewer's
recomputation, scratch_rtp1_axisN.py) with the prolate-concentration asymptotic that CCM Section 7 attaches to the
e^{-4 pi x} law (plan.md 1.6: 1 - chi_4(lambda) ~ (2^14/3) sqrt2 pi^5 lambda^9 e^{-4 pi lambda^2}, the paper's
quoted Fuchs asymptotic, NOT independently checked here).  Pure arithmetic on printed numbers; deterministic."""
import mpmath as mp
mp.mp.dps = 30
eps = {13: mp.mpf('3.48399e-59'), 25: mp.mpf('2.42562e-123'), 50: mp.mpf('2.26934e-257')}   # N = 120, 260, 360
err = {13: mp.mpf('2.43629e-55'), 25: mp.mpf('2.25195e-119'), 50: mp.mpf('2.45308e-253')}
chi = lambda x: mp.mpf(2) ** 14 / 3 * mp.sqrt(2) * mp.pi ** 5 * mp.sqrt(x) ** 9 * mp.e ** (-4 * mp.pi * x)
for x in (13, 25, 50):
    print(f'x={x}: eps = {mp.nstr(eps[x],4)}, 1 - chi_4 (asymptotic) = {mp.nstr(chi(x),4)}, eps/(1-chi_4) = {mp.nstr(eps[x]/chi(x),4)}, err/(1-chi_4) = {mp.nstr(err[x]/chi(x),4)}')
sl = lambda f, a, b: -(mp.log10(f(b)) - mp.log10(f(a))) / (b - a)
for a, b in ((13, 25), (25, 50)):
    print(f'slope {a}->{b} (digits per unit x): eps {mp.nstr(sl(lambda t: eps[t], a, b), 4)}, first-zero error {mp.nstr(sl(lambda t: err[t], a, b), 4)}, '
          f'bare e^(-4 pi x) {mp.nstr(4 * mp.pi / mp.log(10), 4)}, prolate asymptotic {mp.nstr(sl(chi, a, b), 4)}')
# N-convergence (scratch_rtp1_axisN.py X tail; inverse iteration, uncertified tail values): x = 13 at N = 200, x = 50 at N = 400, 420
eps2 = {13: mp.mpf('2.85407e-59'), 25: eps[25], 50: mp.mpf('2.80881e-258')}
print('with the larger-N values (x=13: N=200; x=50: N=420; x=25: N=260 as before):')
for x in (13, 25, 50):
    print(f'   x={x}: eps/(1-chi_4) = {mp.nstr(eps2[x]/chi(x),4)}')
for a, b in ((13, 25), (25, 50), (13, 50)):
    print(f'   slope {a}->{b}: eps {mp.nstr(sl(lambda t: eps2[t], a, b), 4)}, prolate asymptotic {mp.nstr(sl(chi, a, b), 4)}, bare {mp.nstr(4 * mp.pi / mp.log(10), 4)}')
