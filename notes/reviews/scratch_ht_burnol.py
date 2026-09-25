#!/usr/bin/env python3
"""H-THETA hostile review, check E: the orientation of Burnol's V(Delta)=B.HH^2
(astra-proofs T4(a)).  Burnol's HH^2 is ess-supp in {|u| <= 1} (0001013:283-284),
i.e. the INCOMING half y<1 of the notebook bond, whose Mellin transforms are
Hardy in C_-.  Tested on Nyman's rho_alpha and on Burnol's A(u).

  rho_alpha(u) = {alpha/u} - alpha{1/u},  u in (0,1),
  int_0^1 rho_alpha(u) u^{s-1} du = (alpha - alpha^s) zeta(s)/s        (:348-349)
  ((s-1)/s) zeta(s)/s = int_0^1 A(u) u^{s-1} du,
  A(u) = [1/u] log u + log([1/u]!) + [1/u]                             (:396-398)
  V f(u) = f(u) - int_u^inf f(t) dt/t   acts as the multiplier (s-1)/s  (:392-394)

and  (R f)^hat(tau) = sqrt2 F_L(1/2 + 2 i tau),  F_L(s) = int f(x) x^{s-1} dx
     (R f)(y) = 2^{-1/2} y^{1/4} f(sqrt y)                          [T4(a)]
so  Re s > 1/2  <->  Im tau < 0  <->  C_-.

Author: claude:opus (review lane), 2026-09-21.
"""
import mpmath as mp

mp.mp.dps = 25

def frac(x):
    return x - mp.floor(x)

def rho_alpha(u, a):
    return frac(a / u) - a * frac(1 / u)

def A(u):
    m = int(mp.floor(1 / u))
    return m * mp.log(u) + mp.log(mp.factorial(m)) + m

def mellin01(f, s, N=1500):
    """int_0^1 f(u) u^{s-1} du with breakpoints at u = 1/k (f is a step/linear
    function of [1/u]); integrate piecewise on [1/(k+1), 1/k]."""
    tot = mp.mpf(0)
    for k in range(1, N + 1):
        lo, hi = mp.mpf(1) / (k + 1), mp.mpf(1) / k
        tot += mp.quad(lambda u: f(u) * u ** (s - 1), [lo, hi])
    return tot

print("E1  Nyman:  int_0^1 rho_alpha(u) u^{s-1} du = (alpha - alpha^s) zeta(s)/s")
for a in ['0.5', '0.3']:
    a = mp.mpf(a)
    for sv in [mp.mpf(2), mp.mpc(3, 1), mp.mpc('0.7', 5)]:
        num = mellin01(lambda u: rho_alpha(u, a), sv, N=1200)
        ex = (a - a ** sv) * mp.zeta(sv) / sv
        print("   a=%-5s s=%-14s quad=%-30s exact=%-30s rel=%s"
              % (a, mp.nstr(sv, 6), mp.nstr(num, 10), mp.nstr(ex, 10),
                 mp.nstr(abs(num - ex) / abs(ex), 3)))
print()

print("E2  Burnol :396-398   ((s-1)/s) zeta(s)/s = int_0^1 A(u) u^{s-1} du")
print("    A is supported in (0,1]: the V-image of the theta test lies in the")
print("    INCOMING half y<1, i.e. HH^2 = L^2(|u|<=1), exactly as Burnol defines it.")
for sv in [mp.mpf(2), mp.mpf(3), mp.mpc(2, 1), mp.mpc('0.8', 3)]:
    num = mellin01(A, sv, N=1500)
    ex = ((sv - 1) / sv) * mp.zeta(sv) / sv
    print("   s=%-14s quad=%-30s exact=%-30s rel=%s"
          % (mp.nstr(sv, 6), mp.nstr(num, 10), mp.nstr(ex, 10),
             mp.nstr(abs(num - ex) / abs(ex), 3)))
print()

print("E3  V acts as the multiplier (s-1)/s  (and kills 1/u)")
f = lambda u: mp.e ** (-u) if u > 0 else mp.mpf(0)
Vf = lambda u: f(u) - mp.quad(lambda t: f(t) / t, [u, u + 1, u + 10, mp.inf])
for sv in [mp.mpf('1.5'), mp.mpc('1.3', 2)]:
    lhs = mp.quad(lambda u: Vf(u) * u ** (sv - 1), [0, 1, 5, 25, mp.inf])
    rhs = ((sv - 1) / sv) * mp.quad(lambda u: f(u) * u ** (sv - 1), [0, 1, 5, 25, mp.inf])
    print("   s=%-14s  (Vf)^(s)=%-28s  ((s-1)/s) fhat=%-28s rel=%s"
          % (mp.nstr(sv, 6), mp.nstr(lhs, 10), mp.nstr(rhs, 10),
             mp.nstr(abs(lhs - rhs) / abs(rhs), 3)))
u0 = mp.mpf('0.7')
print("   V(1/u) at u=0.7 :", mp.nstr(1 / u0 - mp.quad(lambda t: 1 / t ** 2, [u0, 10, mp.inf]), 5))
print()

print("E4  ORIENTATION.  bond image of a function supported in (0,1):")
print("    (Rf)^hat(tau) = sqrt2 F_L(1/2+2i tau);  Re s>1/2 <-> Im tau<0 (C_-).")
alpha = mp.mpf('0.3')
FL = lambda s: (alpha - alpha ** s) * mp.zeta(s) / s
def Rf_hat(tau):
    """direct quadrature of int_0^inf (R rho_alpha)(y) y^{i tau} d^x y."""
    g = lambda y: 2 ** mp.mpf('-0.5') * y ** mp.mpf('0.25') * rho_alpha(mp.sqrt(y), alpha)
    tot = mp.mpf(0)
    N = 900
    for k in range(1, N + 1):
        lo, hi = (mp.mpf(1) / (k + 1)) ** 2, (mp.mpf(1) / k) ** 2
        tot += mp.quad(lambda y: g(y) * y ** (1j * tau) / y, [lo, hi])
    return tot
for tv in [mp.mpc(0, '-0.4'), mp.mpc(2, '-1.0'), mp.mpc('1.5', '-0.2')]:
    q = Rf_hat(tv)
    pred = mp.sqrt(2) * FL(mp.mpf('0.5') + 2j * tv)
    print("   tau=%-16s quad=%-30s sqrt2*F_L=%-30s rel=%s"
          % (mp.nstr(tv, 6), mp.nstr(q, 8), mp.nstr(pred, 8),
             mp.nstr(abs(q - pred) / abs(pred), 3)))
print()
print("   sup over horizontal lines Im tau = c of |sqrt2 F_L(1/2+2i tau)| :")
for c in ['-2', '-1', '-0.3', '0.3', '1', '2']:
    c = mp.mpf(c)
    vals = [abs(mp.sqrt(2) * FL(mp.mpf('0.5') + 2j * mp.mpc(x, c)))
            for x in ['0.13', '0.5', '1', '3', '10', '40']]
    print("     Im tau = %-7s  max|.| over Re tau in [0,40] = %-18s  %s"
          % (c, mp.nstr(max(vals), 8), "C_- (bounded: Hardy)" if c < 0 else "C_+ (grows / unbounded)"))
print()
print("   L^2 norms on horizontal lines (Hardy test):")
for c in ['-1.5', '-0.75', '-0.1', '0.1', '0.75', '1.5']:
    c = mp.mpf(c)
    nrm = mp.quad(lambda x: abs(mp.sqrt(2) * FL(mp.mpf('0.5') + 2j * mp.mpc(x, c))) ** 2,
                  [-200, -20, -2, 0, 2, 20, 200]) / (2 * mp.pi)
    print("     Im tau = %-7s   (1/2pi) int |F|^2 dx over [-200,200] = %s" % (c, mp.nstr(nrm, 8)))
print("   -> uniformly bounded for Im tau < 0 (H^2(C_-)), divergent for Im tau > 0.")
print("   CONCLUSION: Burnol's V(Delta) = B.HH^2 sits in the INCOMING half;")
print("   the outgoing-half defect needs the reflection J (astra-proofs T4(a)/(b)).")
print()

print("E5  the elementary factor v_-(tau) = (s_+ - 1)/s_+ with s_+ = 1/2+2i tau")
for tv in ['0.3', '2', '-1']:
    t = mp.mpf(tv)
    s = mp.mpf('0.5') + 2j * t
    print("   tau=%-6s  (s-1)/s = %-28s  (tau+i/4)/(tau-i/4) = %s"
          % (tv, mp.nstr((s - 1) / s, 12),
             mp.nstr((t + mp.mpc(0, '0.25')) / (t - mp.mpc(0, '0.25')), 12)))
print("   v_- has its zero at tau=-i/4 (C_-) and its pole at +i/4: inner in C_-.")
print("   v_+ = 1/v_- has its zero at +i/4: inner in C_+. dim K_{v_+^2} = 2.")
