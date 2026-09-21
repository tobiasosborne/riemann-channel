#!/usr/bin/env python3
"""H-THETA hostile review, check C: the symbol Theta, its vertical decay
Theta(iv) sqrt(v/pi) -> 1 (T2(d), exclusion of a delay factor e^{i a tau}),
the edge-quotient identity (T2(c)/H-THETA-EDGE), the paired Blaschke product,
and the prover's decimal list in "What the numerics lane should check".

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
    if abs(s) < mp.mpf('1e-14'):
        return mp.mpf('0.5')
    if abs(s - 1) < mp.mpf('1e-14'):
        return mp.mpf('0.5')
    return (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2 + 1) * mp.zeta(s)

def Lam(s):
    return 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)

def ghat(tau):
    return Lam(mp.mpf('0.5') + 2j * mp.mpc(tau))

def Theta(tau):
    tau = mp.mpc(tau)
    return xi(1 + 2j * tau) / xi(1 - 2j * tau)

def r(tau):
    tau = mp.mpc(tau)
    return (tau - mp.mpc(0, '0.5')) / (tau + mp.mpc(0, '0.5'))

def Lam_gt(s):
    tot = mp.mpf(0)
    for n in range(1, 16):
        tot += (mp.pi * n * n) ** (-s / 2) * mp.gammainc(s / 2, mp.pi * n * n)
    return 2 / (s - 1) + 2 * tot

def ghat_gt(tau):
    return Lam_gt(mp.mpf('0.5') + 2j * mp.mpc(tau))

print("C1  Theta(iv) sqrt(v/pi) -> 1   (T2(d): no e^{i a tau} delay factor)")
print("    Theta(iv) = xi(2v)/xi(1+2v) = ((2v-1)/(2v+1)) sqrt(pi) G(v)/G(v+1/2) z(2v)/z(2v+1)")
for v in ['1', '2', '10', '100', '1000', '10000', '100000']:
    v = mp.mpf(v)
    t1 = Theta(mp.mpc(0, v))
    t2 = ((2 * v - 1) / (2 * v + 1)) * mp.sqrt(mp.pi) * mp.gamma(v) / mp.gamma(v + mp.mpf('0.5')) \
         * mp.zeta(2 * v) / mp.zeta(2 * v + 1)
    print("   v=%-8s Theta(iv)=%-24s closedform rel=%-10s Theta(iv)sqrt(v/pi)=%s"
          % (v, mp.nstr(t1, 12), mp.nstr(abs(t1 - t2) / abs(t1), 3),
             mp.nstr(t1 * mp.sqrt(v / mp.pi), 12)))
print("   an inner factor e^{i a tau}, a>0, would force |Theta(iv)| <= e^{-av}: excluded.")
print()

print("C2  the edge quotient (H-THETA-EDGE)  Theta = [ghat(tau-i/4)/ghat(tau+i/4)] r(tau)")
for tv in ['0.3', '1.9', '5.5', '12', '7.06736257087', '0.5+0.3j', '2-1j']:
    t = C(tv)
    a = Theta(t)
    b = ghat(t - mp.mpc(0, '0.25')) / ghat(t + mp.mpc(0, '0.25')) * r(t)
    c = Lam(1 + 2j * t) / Lam(2j * t) * r(t)
    print("   tau=%-16s Theta=%-30s rel(edge)=%-9s rel(Lam)=%s"
          % (tv, mp.nstr(a, 12), mp.nstr(abs(a - b) / abs(a), 3),
             mp.nstr(abs(a - c) / abs(a), 3)))
print("   removable value at tau=0:  Theta(0) =", mp.nstr(Theta(mp.mpf('1e-14')), 12),
      "  r(0) =", mp.nstr(r(mp.mpf('1e-14')), 12))
print("   phi_E(1/2) = r/Theta at 0 =",
      mp.nstr(r(mp.mpf('1e-14')) / Theta(mp.mpf('1e-14')), 12))
print("   phi_E(1/2+i) = r(1)/Theta(1) =", mp.nstr(r(1) / Theta(1), 12))
print("   Theta(1) =", mp.nstr(Theta(1), 12))
print("   Theta(i) =", mp.nstr(Theta(mp.mpc(0, 1)), 12),
      "  Theta(2i) =", mp.nstr(Theta(mp.mpc(0, 2)), 12))
print()

print("C3  paired Blaschke product for Theta (T2(c)) with the first M zeros")
M = 300
gam = [mp.im(mp.zetazero(n)) for n in range(1, M + 1)]
def Blaschke(tau, M):
    acc = mp.mpc(1)
    for k in range(M):
        g = gam[k]
        vm = mp.mpc(-g / 2, mp.mpf('0.25'))   # v_{rho,-} = -gamma/2 + i sigma/2, sigma=1/2
        vp = mp.mpc(g / 2, mp.mpf('0.25'))
        acc *= (tau - vm) * (tau - vp) / ((tau - mp.conj(vm)) * (tau - mp.conj(vp)))
    return acc
for tv in ['0.3', '3', '0.5+1j', '2+0.2j']:
    t = C(tv)
    B = Blaschke(t, M)
    print("   tau=%-10s Theta=%-28s B_%d=%-28s |ratio|=%s"
          % (tv, mp.nstr(Theta(t), 10), M, mp.nstr(B, 10),
             mp.nstr(abs(Theta(t) / B), 10)))
print("   (the ratio -> 1 slowly: the truncated tail contributes the residual phase/modulus)")
print("   |Theta| on R (must be 1):", [mp.nstr(abs(Theta(mp.mpf(x))), 8) for x in
                                        ['0.3', '5.5', '30', '200']])
print("   |Theta| in C_+ (must be <1):", [mp.nstr(abs(Theta(C(x))), 8) for x in
                                          ['0.3+0.05j', '2+0.5j', '7+3j']])
print("   Theta at w_n = gamma_n/2 + i/4 (must vanish):",
      [mp.nstr(abs(Theta(mp.mpc(gam[k] / 2, mp.mpf('0.25')))), 4) for k in range(3)])
print()

print("C4  the prover's decimal list")
print("   theta(1)   ->  see scratch_ht_outer.py: 1.08643481")
print("   xi(1/2)    =", mp.nstr(xi(mp.mpf('0.5')), 12))
print("   ghat(0)    =", mp.nstr(ghat(mp.mpf('1e-18')), 18), " -16 xi(1/2) =",
      mp.nstr(-16 * xi(mp.mpf('0.5')), 18))
print("   ghat_>(0)  =", mp.nstr(ghat_gt(0), 12), " (= Lambda_>(1/2))")
print("   Lambda_>(0)  =", mp.nstr(Lam_gt(mp.mpf('1e-30')), 12))
print("   Lambda_>(-1) =", mp.nstr(Lam_gt(mp.mpf(-1)), 12))
print("   ghat_>(1)    =", mp.nstr(ghat_gt(1), 12))
g1 = gam[0]
rho1 = mp.mpc('0.5', g1)
print("   gamma_1      =", mp.nstr(g1, 12))
print("   Lambda_>(1-rho_1) =", mp.nstr(Lam_gt(1 - rho1), 12))
print("   Lambda_>(rho_1)   =", mp.nstr(Lam_gt(rho1), 12))
print("   ghat_>(w_1) = Lambda_>(i gamma_1) =", mp.nstr(Lam_gt(mp.mpc(0, g1)), 12))
print("   ghat(gamma_1/2)   =", mp.nstr(abs(ghat(g1 / 2)), 4), "(a zero)")
print()

print("C5  poles and residues of ghat")
eps = mp.mpf('1e-14')
for sgn in [1, -1]:
    t0 = mp.mpc(0, sgn * mp.mpf('0.25'))
    res = eps * ghat(t0 + eps)
    print("   Res_{tau=%si/4} ghat ~ %s   (s = %d)"
          % ('+' if sgn > 0 else '-', mp.nstr(res, 12), 0 if sgn > 0 else 1))
print("   ghat_>(+i/4) =", mp.nstr(ghat_gt(mp.mpc(0, '0.25')), 12), "(finite)")
print("   eps*ghat_>(-i/4+eps) =", mp.nstr(eps * ghat_gt(mp.mpc(0, '-0.25') + eps), 10))
print()

print("C6  Stirling constant in |ghat(u)| ~ 2 sqrt2 pi^{1/4} |u|^{-1/4} e^{-pi|u|/2}|zeta(1/2+2iu)|")
C = 2 * mp.sqrt(2) * mp.pi ** mp.mpf('0.25')
print("   C = 2 sqrt2 pi^{1/4} =", mp.nstr(C, 12),
      "  (= 2 pi^{-1/4} sqrt(2pi) =", mp.nstr(2 * mp.pi ** mp.mpf('-0.25') * mp.sqrt(2 * mp.pi), 12), ")")
for u in ['20', '40', '70', '100', '300']:
    u = mp.mpf(u)
    pred = C * u ** mp.mpf('-0.25') * mp.exp(-mp.pi * u / 2) * abs(mp.zeta(mp.mpc('0.5', 2 * u)))
    print("   u=%-6s |ghat|/pred = %s" % (u, mp.nstr(abs(ghat(u)) / pred, 14)))
print()

print("C7  u*ghat_>(u) -> -(2-theta(1)) i = -0.91356519 i   (T2(b))")
for u in ['5', '20', '100', '500', '2000']:
    u = mp.mpf(u)
    print("   u=%-6s u*ghat_>(u) = %s" % (u, mp.nstr(u * ghat_gt(u), 12)))
