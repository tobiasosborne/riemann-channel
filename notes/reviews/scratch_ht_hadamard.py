#!/usr/bin/env python3
"""H-THETA hostile review, check B: the paired Hadamard normalisation b = 0
used in astra-proofs T2(c)/T2(d) (and independently in Uetake 2007, p.111).

Claim:  xi(s) = e^{a+bs} P(s),  P(s) = prod_{Im rho > 0} (1-s/rho)(1-s/conj rho),
        P'(1/2)/P(1/2) = -sum 2(Re rho - 1/2)/|rho-1/2|^2 = 0,
        xi'(1/2) = 0  =>  b = 0;  xi(0) = 1/2 => e^a = 1/2.
So  xi(s) = (1/2) prod (1-s/rho)(1-s/conj rho).

Author: claude:opus (review lane), 2026-09-21.
"""
import mpmath as mp

mp.mp.dps = 30

def C(x):
    """parse a complex literal string into mpc at working precision."""
    if isinstance(x, str) and ('j' in x):
        z = complex(x)
        return mp.mpc(mp.mpf(repr(z.real)), mp.mpf(repr(z.imag)))
    return mp.mpc(x)

def xi(s):
    s = mp.mpc(s)
    if abs(s) < mp.mpf('1e-12'):
        return mp.mpf('0.5')
    if abs(s - 1) < mp.mpf('1e-12'):
        return mp.mpf('0.5')
    if mp.re(s) < mp.mpf('0.5'):        # use xi(s) = xi(1-s): avoids Gamma poles
        s = 1 - s
    return (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2 + 1) * mp.zeta(s)

def xi_raw(s):
    """the same formula WITHOUT the reflection branch, so that xi'(1/2) is a
    genuine numerical test and not symmetric by construction."""
    s = mp.mpc(s)
    return (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2 + 1) * mp.zeta(s)

print("B1  elementary normalisations")
print("   xi(0)   =", mp.nstr(xi(mp.mpf('1e-30')), 20))
print("   xi(1)   =", mp.nstr(xi(1 - mp.mpf('1e-30')), 20))
print("   xi(1/2) =", mp.nstr(xi(mp.mpf('0.5')), 20))
d1 = mp.diff(xi_raw, mp.mpf('0.5'))
d2 = mp.diff(xi_raw, mp.mpf('0.5'), 2)
print("   xi'(1/2)  =", mp.nstr(d1, 10), "   (must be 0: xi(s)=xi(1-s))")
print("   xi''(1/2) =", mp.nstr(d2, 12), "  (nonzero, so 1/2 is not a zero/critical degeneracy)")
print("   symmetry check |xi(s)-xi(1-s)| at s=0.3+2i:",
      mp.nstr(abs(xi_raw(mp.mpc('0.3', '2')) - xi_raw(1 - mp.mpc('0.3', '2'))), 5))
print()

N = 1500
print("B2  loading %d zeta zeros ..." % N)
import os, json
_cache = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.ht_zeros_cache.json')
if os.path.exists(_cache):
    gam = [mp.mpf(x) for x in json.load(open(_cache))[:N]]
else:
    gam = [mp.im(mp.zetazero(n)) for n in range(1, N + 1)]
    json.dump([mp.nstr(g, 30) for g in gam], open(_cache, 'w'))
print("   gamma_1 =", mp.nstr(gam[0], 12), " gamma_%d =" % N, mp.nstr(gam[-1], 12))

def P_partial(s, M):
    """prod_{n<=M} (1-s/rho_n)(1-s/conj rho_n) with rho_n = 1/2 + i gamma_n."""
    acc = mp.mpc(1)
    for k in range(M):
        r = mp.mpc('0.5', gam[k])
        acc *= (1 - s / r) * (1 - s / mp.conj(r))
    return acc

# tail of sum 1/|rho|^2 beyond gamma_N, via the Riemann-von Mangoldt density
T = gam[-1]
S_tail = mp.quad(lambda t: (mp.log(t / (2 * mp.pi)) / (2 * mp.pi)) / (mp.mpf('0.25') + t ** 2),
                 [T, 10 * T, 1000 * T, mp.inf])
S_head = sum(1 / (mp.mpf('0.25') + g ** 2) for g in gam)
print("   sum_{n<=N} 1/|rho|^2 =", mp.nstr(S_head, 12), "  tail estimate =", mp.nstr(S_tail, 6))
print()

print("B3  L(s) := log xi(s) - log(1/2) - sum_{n<=N} log[(1-s/rho)(1-s/conj rho)]")
print("    if xi = e^{a+bs} P then L(s) = (a-log(1/2)) + b s + tail(s),")
print("    tail(s) ~ (s^2-s) * S_tail.  Test: L(s)/(s^2-s) ~ S_tail, s-independent.")
for sv in ['2', '3', '-1', '5', '0.5', '0.25']:
    s = mp.mpf(sv)
    L = mp.log(xi(s) / (mp.mpf('0.5') * P_partial(s, N)))
    q = L / (s ** 2 - s) if abs(s ** 2 - s) > 1e-9 else mp.nan
    print("   s=%-6s  L(s)=%-22s  L/(s^2-s)=%-22s" % (sv, mp.nstr(L, 10), mp.nstr(q, 10)))
print("   S_tail (predicted common value) =", mp.nstr(S_tail, 10))
print()

print("B4  the decisive test: b = xi'(1/2)/xi(1/2) - sum_rho [1/(1/2-rho)+1/(1/2-conj rho)]")
lg = d1 / xi_raw(mp.mpf('0.5'))
ssum = sum(1 / (mp.mpf('0.5') - mp.mpc('0.5', g)) + 1 / (mp.mpf('0.5') - mp.mpc('0.5', -g))
           for g in gam)
print("   xi'(1/2)/xi(1/2)          =", mp.nstr(lg, 10))
print("   sum over %d computed zeros =" % N, mp.nstr(ssum, 10))
print("   b = difference             =", mp.nstr(lg - ssum, 10))
print()

print("B5  the off-line cancellation (synthetic quadruple rho, 1-conj rho)")
for (sig, g) in [(mp.mpf('0.8'), mp.mpf('30')), (mp.mpf('0.6'), mp.mpf('5')),
                 (mp.mpf('0.95'), mp.mpf('1000'))]:
    r1 = mp.mpc(sig, g)          # Im > 0
    r2 = mp.mpc(1 - sig, g)      # = 1 - conj(rho), also Im > 0
    t1 = 2 * (mp.re(r1) - mp.mpf('0.5')) / abs(r1 - mp.mpf('0.5')) ** 2
    t2 = 2 * (mp.re(r2) - mp.mpf('0.5')) / abs(r2 - mp.mpf('0.5')) ** 2
    print("   sigma=%-6s gamma=%-6s  term(rho)=%-16s term(1-conj rho)=%-16s sum=%s"
          % (sig, g, mp.nstr(t1, 8), mp.nstr(t2, 8), mp.nstr(t1 + t2, 3)))
print()

print("B6  value test of xi(s) = (1/2) prod_{n<=N} (...) * exp(tail)")
for sv in ['2', '3+1j', '-2', '0.5+14j']:
    s = C(sv)
    prod = mp.mpf('0.5') * P_partial(s, N) * mp.e ** ((s ** 2 - s) * S_tail)
    tru = xi(s)
    print("   s=%-10s xi=%-26s prod*e^tail=%-26s rel=%s"
          % (sv, mp.nstr(tru, 10), mp.nstr(prod, 10),
             mp.nstr(abs(prod - tru) / abs(tru), 3)))
print()

print("B7  Blaschke convergence of Theta's zero divisor: sum Im w / (1+|w|^2)")
tot = sum((mp.mpf('0.25')) / (1 + (g / 2) ** 2 + mp.mpf('0.0625')) for g in gam)
print("   partial sum over %d zeros (both signs) = %s" % (N, mp.nstr(2 * tot, 10)))
print("   tail ~ sum 1/gamma^2 -> finite; Blaschke condition holds.")
