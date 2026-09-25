#!/usr/bin/env python3
"""H-THETA hostile review, re-verdict pass (2026-09-21): the four MINOR fixes as
printed in report/sections/04q_h_theta.tex and 04r_h_theta_channels.tex.

G1  thm:symbol-edge-quotient (b): xi has no real zeros -- zeta(sigma)<0 and
    sigma(sigma-1)<0 on (0,1), so xi(sigma)>0 there; xi(0)=xi(1)=1/2.
G2  thm:theta-vector-cyclic (d): phi.1_{(1,inf)} is in L^2(1,inf;d^x y) although
    phi is not in H, and its Mellin transform is Lambda_>(2 i tau), argument in
    Re s < 0 < 1.
G3  thm:gl1-bad-zero-defect: the printed v_pm(tau) = (tau -+ i/4)/(tau +- i/4)
    against Burnol's (s-1)/s read at s = 1/2 +- 2 i tau -- WHICH sign goes with
    which (the parenthetical's pairing is reversed; the operative definitions
    V_y = mult by v_-, B_-(tau)=B(1/2+2i tau) are the correct ones).
G4  prop:kernels-not-riesz (b): the printed overlap (1/2)/sqrt((a-a')^2+1/4) is
    the general 2b/sqrt((a-a')^2+4b^2) at b = 1/4.

Author: claude:opus (review lane), 2026-09-21.
"""
import mpmath as mp

mp.mp.dps = 25
I = mp.mpc(0, 1)

def xi(s):
    s = mp.mpc(s)
    return (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2 + 1) * mp.zeta(s)

print("G1  xi has no real zeros: xi(sigma) > 0 on (0,1)")
print("    sigma   zeta(sigma)       sigma(sigma-1)    xi(sigma)")
for v in ['0.001', '0.05', '0.2', '0.4', '0.5', '0.6', '0.8', '0.95', '0.999']:
    s = mp.mpf(v)
    print("    %-7s %-17s %-17s %s" % (v, mp.nstr(mp.zeta(s), 8),
                                       mp.nstr(s * (s - 1), 8), mp.nstr(xi(s), 12)))
vals = [mp.re(xi(mp.mpf(k) / 1000)) for k in range(1, 1000)]
imax = max(abs(mp.im(xi(mp.mpf(k) / 200))) for k in range(1, 200))
print("    min over 999 points of (0,1): %s  at sigma = 1/2 (max |Im xi| = %s)"
      % (mp.nstr(min(vals), 12), mp.nstr(imax, 3)))
print("    xi(0) = xi(1) = 1/2; all nontrivial zeros lie in 0<=Re s<=1, so xi has")
print("    no real zero anywhere and every zero is paired by rho <-> conj rho.  FIX ADEQUATE.")
print()

print("G2  the unweighted outgoing half phi.1_{(1,inf)}")
def thetam1(y):
    s, n = mp.mpf(0), 1
    while True:
        t = mp.exp(-mp.pi * n * n * y)
        s += t
        if t < mp.mpf(10) ** (-mp.mp.dps - 8):
            break
        n += 1
    return 2 * s
phi = lambda y: thetam1(y) - 1 / mp.sqrt(y)        # y >= 1, cancellation-free
XC = mp.mpf(30)
# beyond X = 30 the theta tail is 0 at this precision and phi = -e^{-X/2} exactly,
# so int_XC^inf phi^2 dX = e^{-XC}
nrm = mp.quad(lambda X: phi(mp.e ** X) ** 2, [0, 1, 3, 10, XC]) + mp.e ** (-XC)
print("    ||phi.1_{y>1}||^2_{L^2(1,inf;d^x y)} = %s  (finite: it IS a Hilbert vector)"
      % mp.nstr(nrm, 12))
Xd = mp.mpf(40)
print("    for contrast, int_{e^-X}^1 |phi|^2 d^x y at X = 10, 20, 40 :",
      [mp.nstr(mp.quad(lambda X: (mp.sqrt(mp.e ** X) * thetam1(1 / mp.e ** X) - 1) ** 2,
                       [-L, -1, 0]), 8) for L in [10, 20, 40]],
      " -> linear in X: phi is NOT in H")
def Lam_gt(s):
    tot = mp.mpf(0)
    for n in range(1, 16):
        tot += (mp.pi * n * n) ** (-s / 2) * mp.gammainc(s / 2, mp.pi * n * n)
    return 2 / (s - 1) + 2 * tot
for tv in [mp.mpf('0.7'), mp.mpc('1.3', '0.4'), mp.mpc('0', '0.9')]:
    # exact tail: int_XC^inf (-e^{-X/2}) e^{i tau X} dX = -e^{XC(i tau - 1/2)}/(i tau - 1/2)
    q = (mp.quad(lambda X: phi(mp.e ** X) * mp.e ** (I * tv * X), [0, 1, 2, 4, 8, 16, XC])
         - mp.e ** (XC * (I * tv - mp.mpf('0.5'))) / (I * tv - mp.mpf('0.5')))
    pred = Lam_gt(2 * I * tv)
    print("    tau=%-14s  int_1^inf phi y^{i tau} d^x y = %-28s  Lambda_>(2 i tau) rel = %s"
          % (mp.nstr(tv, 6), mp.nstr(q, 10), mp.nstr(abs(q - pred) / abs(pred), 3)))
print("    argument s = 2 i tau has Re s = -2 Im tau < 0 < 1 on C_+, so (c)'s zero-free")
print("    half-plane Re s < 1 applies verbatim.  FIX ADEQUATE.")
for tv in [mp.mpc('3', '0.5'), mp.mpc('0', '2.0'), mp.mpc('10', '0.05')]:
    print("      |Lambda_>(2 i tau)| at tau = %-12s : %s (nonzero)"
          % (mp.nstr(tv, 6), mp.nstr(abs(Lam_gt(2 * I * tv)), 8)))
print()

print("G3  the v_pm parenthetical of thm:gl1-bad-zero-defect")
print("    printed: v_pm(tau) = (tau -+ i/4)/(tau +- i/4), 'read at s = 1/2 +- 2 i tau'")
for tv in ['0.3', '2', '-1.4']:
    t = mp.mpf(tv)
    sp, sm = mp.mpf('0.5') + 2 * I * t, mp.mpf('0.5') - 2 * I * t
    vp = (t - I / 4) / (t + I / 4)
    vm = (t + I / 4) / (t - I / 4)
    print("    tau=%-6s (s-1)/s at s_+=1/2+2i tau = %-26s  v_-(tau) = %-26s  |diff|=%s"
          % (tv, mp.nstr((sp - 1) / sp, 10), mp.nstr(vm, 10),
             mp.nstr(abs((sp - 1) / sp - vm), 3)))
    print("             (s-1)/s at s_-=1/2-2i tau = %-26s  v_+(tau) = %-26s  |diff|=%s"
          % (mp.nstr((sm - 1) / sm, 10), mp.nstr(vp, 10),
             mp.nstr(abs((sm - 1) / sm - vp), 3)))
print("    => (s-1)/s at s = 1/2 + 2 i tau is v_MINUS, not v_+: the '+-' pairing in the")
print("    parenthetical is reversed.  The operative definitions (V_y = multiplication by")
print("    v_-, V_y N = B_- H^2(C_-), B_-(tau) = B(1/2+2i tau)) are consistent and correct,")
print("    so no conclusion changes; the hint should read 'at s = 1/2 -+ 2 i tau'.")
print()

print("G4  prop:kernels-not-riesz (b): overlap (1/2)/sqrt((a-a')^2+1/4) at height b=1/4")
b = mp.mpf('0.25')
for d in ['4', '1', '0.25', '0.02']:
    d = mp.mpf(d)
    gen = 2 * b / mp.sqrt(d ** 2 + 4 * b ** 2)
    shard = mp.mpf('0.5') / mp.sqrt(d ** 2 + mp.mpf('0.25'))
    kw, kv = mp.mpc(0, b), mp.mpc(d, b)
    direct = abs(I / (kv - mp.conj(kw))) * (2 * b)
    print("    gap=%-7s general 2b/sqrt(.)=%-16s shard form=%-16s direct=%s"
          % (d, mp.nstr(gen, 10), mp.nstr(shard, 10), mp.nstr(direct, 10)))
print("    identical.  FIX/STATEMENT CORRECT.")
