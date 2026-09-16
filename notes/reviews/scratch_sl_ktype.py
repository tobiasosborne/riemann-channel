#!/usr/bin/env python3
"""Independent REFUTE-lane check of D8 (K-type parity) and the D5 sign obstruction."""
import mpmath as mp, sympy as sp
PASS = FAIL = 0
def chk(name, cond, extra=""):
    global PASS, FAIL
    if cond: PASS += 1; print(f"  PASS  {name} {extra}")
    else:    FAIL += 1; print(f"  FAIL  {name} {extra}")
mp.mp.dps = 30

print("== D8: the K-type theta counterexample ==")
def theta(t, K=60): return mp.nsum(lambda n: (-1)**int(n)*mp.e**(-2*t*n**2), [-K, K]) \
    if False else sum((-1)**n*mp.e**(-2*t*n**2) for n in range(-K,K+1))
def poisson(t, K=60): return mp.sqrt(mp.pi/(2*t))*sum(mp.e**(-mp.pi**2*(k+mp.mpf(1)/2)**2/(2*t)) for k in range(-K,K+1))
for tv in (0.2, 0.5, 1.0, 2.0):
    chk(f"direct sum = Poisson-transformed sum at t={tv}", abs(theta(mp.mpf(tv))-poisson(mp.mpf(tv))) < mp.mpf('1e-25'),
        f"[{mp.nstr(theta(mp.mpf(tv)),12)}]")
chk("theta factor at t=1 is 0.730000328323 (report's printed number)",
    mp.nstr(theta(mp.mpf(1)), 12) == '0.730000328323', f"[{mp.nstr(theta(mp.mpf(1)),12)}]")
chk("the Poisson side is a sum of positive terms, so str != 0 for every t>0",
    all(poisson(mp.mpf(tv)) > 0 for tv in (0.01,0.1,1,10,100)))

print("== D8: weight shift sign ==")
m = sp.Symbol('m'); Om = sp.Symbol('Omega'); sig = sp.Symbol('sigma')
# W f = i m f  =>  W^2 f = -m^2 f;  L_adj = 2 Omega + W^2/2
chk("L_adj = 2 Omega - m^2/2 on weight m (report's D8 step 3 sign is right)",
    sp.simplify((2*Om + sp.Rational(1,2)*(-m**2)) - (2*Om - m**2/2)) == 0)
chk("with Omega = -sigma this is -2 sigma - m^2/2; for m=2n: -2 sigma - 2 n^2",
    sp.simplify((2*(-sig) - (2*sp.Symbol('n'))**2/2) - (-2*sig - 2*sp.Symbol('n')**2)) == 0)
chk("matches 03d obs:continuous-harrow-tempered rate -T_* = 2 s(1-s) + m^2/2",
    sp.simplify(-(2*(-sig) - m**2/2) - (2*sig + m**2/2)) == 0)

print("== D8 step 3: the Hodge-bundle diffusion supertrace formula ==")
t, T0, chi = sp.symbols('t T0 chi')
# McKean-Singer with Delta_2 = Delta_0: Tr e^{-2t D1} = 2 T0 - chi
lhs = 2*T0 - sp.exp(-2*t)*(2*T0 - chi)
rhs = 2*(1-sp.exp(-2*t))*T0 + sp.exp(-2*t)*chi
chk("2Tr e^{-2t D0} - e^{-2t}Tr e^{-2t D1} = 2(1-e^{-2t})Tr e^{-2t D0} + e^{-2t} chi",
    sp.simplify(lhs-rhs) == 0)

print("== D5: the flat supertraces are negative ==")
tt = sp.Symbol('tt', positive=True)
chk("str e^{t B_perp} = 2 - e^t - e^{-t} < 0 for t>0",
    all(float((2-sp.exp(tt)-sp.exp(-tt)).subs(tt, v)) < 0 for v in (0.1,1,5)))
chk("-C/(1-e^{-t}) has negative atoms for t>0",
    all(float((-1/(1-sp.exp(-tt))).subs(tt,v)) < 0 for v in (0.1,1,5)))
print(f"\nTALLY scratch_sl_ktype.py: {PASS} PASS / {FAIL} FAIL")
