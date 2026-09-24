#!/usr/bin/env python3
"""REFUTE lane R, RTP-1 (claude:opus, 2026-09-24), re-verdict pass.  eps_N and the COMPARISON STEP
|z_1 - gamma_1| (zeros used here only) at x = 50, N = 420, to test the corrected shard's "the minimal eigenvalue
and the first-zero error fall together at about 5.38 digits per unit of x between 13 and 50".  Reviewer's (a, b)
and ball LDL^T; inverse iteration plus a certified inertia bracket.  Deterministic."""
import sys, os
from flint import arb, acb, ctx
import mpmath as mp
sys.path.insert(0, os.path.dirname(__file__))
import scratch_rtp1_ab as AB, scratch_rtp1_linalg as LA
X, N, prec = 50, 420, 4200
ctx.prec = prec
a, b = AB.ab_total(arb(X).log(), N, AB.von_mangoldt_table(X), prec)
lam, resid, v = LA.eig_even(prec, a, b, '0', 6, int(prec * 0.3) - 20)
mp.mp.dps = 40
mid = mp.mpf(lam.strip('[').split()[0])
br = LA.inertia(prec, a, b, [mp.nstr(mid * (1 - mp.mpf('1e-6')), 30), mp.nstr(mid * (1 + mp.mpf('1e-6')), 30)])
ok = br[0]['negE'] == 0 and br[0]['undE'] == 0 and br[1]['negE'] == 1 and br[1]['undE'] == 0 and br[1]['negO'] == 0 and br[1]['undO'] == 0
print(f'x={X} N={N}: eps_N = {mp.nstr(mid, 6)}; certified bracket (rel 1e-6, even-simple, below odd): {ok}')
mp.mp.dps = int(prec * 0.3) - 40
xi = [mp.mpf(v[0])] + [mp.mpf(t) / mp.sqrt(2) for t in v[1:]]
Lm = mp.log(X)
g = lambda s_: -xi[0] / s_ + 2 * s_ * mp.fsum(xi[j] / (j * j - s_ * s_) for j in range(1, len(xi)))
gam1 = mp.mpf(acb.zeta_zero(1).imag.mid().str(int(prec * 0.3) - 30, radius=False))
sr = mp.findroot(g, gam1 * Lm / (2 * mp.pi), tol=mp.mpf(10) ** (-(mp.mp.dps - 20)))
err = abs(2 * mp.pi * sr / Lm - gam1)
mp.mp.dps = 30
e13, r13 = mp.mpf('2.85407e-59'), mp.mpf('2.00e-55')     # x = 13, N = 200 (lane A1 certified; reviewer's eps)
print(f'# COMPARISON STEP x={X} N={N}: |z_1 - gamma_1| = {mp.nstr(err, 6)}; ratio to eps = {mp.nstr(err / mid, 5)}')
print(f'slope 13 -> 50 (x=13 at N=200): eps {mp.nstr((mp.log10(e13) - mp.log10(mid)) / 37, 4)}, first-zero error {mp.nstr((mp.log10(r13) - mp.log10(err)) / 37, 4)} digits per unit x')
