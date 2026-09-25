#!/usr/bin/env python3
"""H-THETA hostile review, check F: Burnol's cosine transform conventions and
the TWO-CUTOFF covariance of astra-proofs T6(c):

    F_+ f(u) = 2 int_0^inf cos(2 pi u x) f(x) dx      (0203120:305-306)
    D_lambda f(x) = lambda^{-1/2} f(x/lambda)
    F_+ D_lambda = D_{1/lambda} F_+                   (claimed)
    D_lambda L_{a,b} = L_{lambda a, b/lambda}
    U_t R L_{a,b} = R L_{a e^{t/2}, b e^{-t/2}}       (claimed; U_t R = R D_{e^{t/2}})
    M(F_+ f)(s) = M(f)(1-s),  M(f)(s) = pi^{-s/2} Gamma(s/2) int_0^inf f(t) t^{-s} dt
                                                      (0203120:467-468)

The brief's law  U_t L_a = L_{a e^{+-t}}  is tested and fails; the product a*b
is the invariant.

Author: claude:opus (review lane), 2026-09-21.
"""
import mpmath as mp

mp.mp.dps = 25

# test function: f = 1_{[1,2]}  (compactly supported away from 0)
def f(x):
    return mp.mpf(1) if (1 <= x <= 2) else mp.mpf(0)

def Fp_f(u):
    """exact cosine transform of 1_{[1,2]}: 2 int_1^2 cos(2 pi u x) dx."""
    u = mp.mpf(u)
    if u == 0:
        return mp.mpf(2)
    return (mp.sin(4 * mp.pi * u) - mp.sin(2 * mp.pi * u)) / (mp.pi * u)

def Fp_quad(g, u, seg):
    return 2 * mp.quad(lambda x: mp.cos(2 * mp.pi * u * x) * g(x), seg)

print("F0  the exact cosine transform of 1_{[1,2]} agrees with quadrature")
for u in ['0.3', '1.7', '5.0']:
    u = mp.mpf(u)
    print("   u=%-6s exact=%-24s quad=%-24s rel=%s"
          % (u, mp.nstr(Fp_f(u), 12), mp.nstr(Fp_quad(f, u, [1, 1.5, 2]), 12),
             mp.nstr(abs(Fp_f(u) - Fp_quad(f, u, [1, 1.5, 2])) / abs(Fp_f(u)), 3)))
print()

print("F1  covariance   F_+ D_lambda f (u)  ==  D_{1/lambda} F_+ f (u)")
print("    LHS by quadrature of the dilated function; RHS = lambda^{1/2} (F_+f)(lambda u)")
for lam in ['1.7', '0.6', '3.0', '0.25']:
    lam = mp.mpf(lam)
    Df = lambda x: lam ** mp.mpf('-0.5') * f(x / lam)   # supported on [lam, 2lam]
    worst = mp.mpf(0)
    for u in ['0.11', '0.4', '1.3', '2.9', '7.5']:
        u = mp.mpf(u)
        lhs = Fp_quad(Df, u, [lam, 1.5 * lam, 2 * lam])
        rhs = lam ** mp.mpf('0.5') * Fp_f(lam * u)      # = (D_{1/lam} F_+f)(u)
        worst = max(worst, abs(lhs - rhs) / max(abs(rhs), mp.mpf('1e-20')))
    print("   lambda=%-6s  max rel |F_+D_lam f - D_{1/lam}F_+ f| over 5 u = %s"
          % (lam, mp.nstr(worst, 4)))
print()

print("F2  what the covariance does to the two cutoffs")
print("    D_lambda f is constant on (0, lambda a) if f is constant on (0,a):")
print("    and (F_+ D_lambda f)(u) = lambda^{1/2}(F_+f)(lambda u) is constant on")
print("    (0, b/lambda) iff F_+f is constant on (0,b).  So a -> lambda a, b -> b/lambda.")
print("    Demonstration on the SUPPORT version (Sonine K_{a,b}): f = 1_{[1,2]} vanishes on (0,1),")
print("    so a=1 for f;  D_lambda f vanishes on (0,lambda):")
for lam in ['1.7', '0.6']:
    lam = mp.mpf(lam)
    Df = lambda x: lam ** mp.mpf('-0.5') * f(x / lam)
    print("   lambda=%-5s D_lam f(0.5*lam)=%-8s  D_lam f(1.5*lam)=%-8s  (vanishes below lambda)"
          % (lam, mp.nstr(Df(mp.mpf('0.5') * lam), 4), mp.nstr(Df(mp.mpf('1.5') * lam), 4)))
    # second cutoff: track the first interval on which F_+ of the dilate is unchanged
    print("        (F_+D_lam f)(u)/lam^{1/2} at u = 0.4, 0.4/lam :",
          mp.nstr(Fp_quad(Df, mp.mpf('0.4'), [lam, 2 * lam]) / lam ** mp.mpf('0.5'), 8),
          mp.nstr(Fp_f(mp.mpf('0.4')), 8),
          "   [(F_+D_lam f)(b/lam) = lam^{1/2}(F_+f)(b)]")
print("    => one cutoff scales UP by lambda, the other DOWN by lambda; the product ab is invariant.")
print("    Hence the brief's U_t L_a = L_{a e^{+-t}} is false; T6(c)'s law is the right one.")
print()

print("F3  U_t R = R D_{e^{t/2}}   (notebook time vs Sonine dilation)")
print("    (Rf)(y) = 2^{-1/2} y^{1/4} f(sqrt y),   (U_t h)(y) = h(e^{-t} y)")
for t in ['0.8', '-1.3']:
    t = mp.mpf(t)
    lam = mp.e ** (t / 2)
    worst = mp.mpf(0)
    for y in ['0.7', '2.0', '5.5', '9.0']:
        y = mp.mpf(y)
        R = lambda g, yy: 2 ** mp.mpf('-0.5') * yy ** mp.mpf('0.25') * g(mp.sqrt(yy))
        lhs = R(f, mp.e ** (-t) * y)                              # (U_t R f)(y)
        Df = lambda x: lam ** mp.mpf('-0.5') * f(x / lam)
        rhs = R(Df, y)                                            # (R D_lam f)(y)
        worst = max(worst, abs(lhs - rhs))
    print("   t=%-6s lambda=e^{t/2}=%-16s  max |U_t R f - R D_lam f| = %s"
          % (t, mp.nstr(lam, 10), mp.nstr(worst, 4)))
print()

print("F4  Burnol's functional equation   M(F_+ f)(s) = M(f)(1-s)   (0203120:467-468)")
print("    M(f)(s) = pi^{-s/2} Gamma(s/2) int_0^inf f(t) t^{-s} dt   (right Mellin transform)")
FR_f = lambda s: (2 ** (1 - s) - 1) / (1 - s)          # int_1^2 t^{-s} dt
def FR_Fp(s):
    """int_0^inf F_+f(u) u^{-s} du, 0 < Re s < 1, oscillatory tail summed."""
    head = mp.quad(lambda u: Fp_f(u) * u ** (-s), [0, mp.mpf('0.25'), mp.mpf('0.5'), 1])
    tail = mp.mpf(0)
    K = 4000
    for k in range(1, K + 1):
        tail += mp.quad(lambda u: Fp_f(u) * u ** (-s), [k, k + mp.mpf('0.5'), k + 1])
    return head + tail
M = lambda s, FR: mp.pi ** (-s / 2) * mp.gamma(s / 2) * FR
for sv in [mp.mpf('0.4'), mp.mpf('0.6'), mp.mpc('0.5', '1.0')]:
    a = M(sv, FR_Fp(sv))
    b = M(1 - sv, FR_f(1 - sv))
    print("   s=%-14s M(F_+f)(s)=%-30s M(f)(1-s)=%-30s rel=%s"
          % (mp.nstr(sv, 6), mp.nstr(a, 10), mp.nstr(b, 10),
             mp.nstr(abs(a - b) / abs(b), 3)))
print()

print("F5  (Rf)^hat(tau) = sqrt2 F_R(1/2 - 2 i tau)   (astra-proofs T6(c) convention)")
for tv in [mp.mpf('0.6'), mp.mpc('1.0', '0.3')]:
    R = lambda yy: 2 ** mp.mpf('-0.5') * yy ** mp.mpf('0.25') * f(mp.sqrt(yy))
    q = mp.quad(lambda y: R(y) * y ** (1j * tv) / y, [1, mp.mpf('2.25'), 4])
    pred = mp.sqrt(2) * FR_f(mp.mpf('0.5') - 2j * tv)
    print("   tau=%-14s quad=%-30s pred=%-30s rel=%s"
          % (mp.nstr(tv, 6), mp.nstr(q, 10), mp.nstr(pred, 10),
             mp.nstr(abs(q - pred) / abs(pred), 3)))
print()

print("F6  the algebraic semigroup T_t^0 of H-THETA-1: is it a semigroup?")
print("    T_t^0 e_k = e^{lam t} sum_j C(k,j)(t/2)^{k-j} e_j  ==  e^{lam t} exp((t/2) d/dX) on X^k")
lam = mp.mpc('-0.25', '-7.0')
def Tmat(t, K):
    Mx = mp.zeros(K, K)
    for k in range(K):
        for j in range(k + 1):
            Mx[j, k] = mp.e ** (lam * t) * mp.binomial(k, j) * (t / 2) ** (k - j)
    return Mx
K = 5
for (t, u) in [('0.7', '1.3'), ('2.0', '-0.5')]:
    t, u = mp.mpf(t), mp.mpf(u)
    d = mp.norm(Tmat(t, K) * Tmat(u, K) - Tmat(t + u, K))
    print("   ||T_t T_u - T_{t+u}||  at (t,u)=(%s,%s), K=%d : %s" % (t, u, K, mp.nstr(d, 4)))
gen = mp.zeros(K, K)
for k in range(K):
    gen[k, k] = lam
    if k >= 1:
        gen[k - 1, k] = mp.mpf(k) / 2
d = mp.norm(mp.expm(gen * mp.mpf('0.7')) - Tmat(mp.mpf('0.7'), K))
print("   ||exp(0.7 A_0) - T_0.7|| with A_0 e_k = lam e_k + (k/2) e_{k-1} :", mp.nstr(d, 4))
print("   lambda_rho = (conj rho - 1)/2 at rho = 1/2 + i gamma gives Re = -1/4 and freq -gamma/2:")
for g in ['14.1347251417', '21.0220396388']:
    g = mp.mpf(g)
    lr = (mp.conj(mp.mpc('0.5', g)) - 1) / 2
    w = mp.mpc(g / 2, mp.mpf('0.25'))
    print("     gamma=%-16s lambda_rho=%-24s  -i conj(w_rho)=%s"
          % (g, mp.nstr(lr, 10), mp.nstr(-1j * mp.conj(w), 10)))
print("   (these agree: T_t^0 targets exactly the K_Theta mode eigenvalues, NOT U_t|,")
print("    whose rate on the evaluators would be (conj rho - 1/2)/2.)")
