#!/usr/bin/env python3
"""H-THETA hostile review, check A: the outer-ness bound of astra-proofs T3(c).

Claim (T3(c)):  for  z = (1-s)/2,  Re s < 1,
    -z Lambda_>(s) = p(0) + int_0^infty p'(X) e^{-zX} dX,
    p(X) = 1 - e^{X/2}(theta(e^X)-1),  p' >= 0,  int_0^infty p' = theta(1)-1,
hence   Re[ -(1-s) Lambda_>(s)/2 ] >= p(0) - (theta(1)-1) = 3 - 2 theta(1) > 0,
so Lambda_> is zero-free on Re s < 1 and ghat_> is outer.

Author: claude:opus (review lane), 2026-09-21.
"""
import mpmath as mp

mp.mp.dps = 30

def thetam1(y):
    """theta(y)-1 = 2 sum_{n>=1} exp(-pi n^2 y), for y >= ~0.3 (no cancellation)."""
    s = mp.mpf(0)
    n = 1
    while True:
        t = mp.exp(-mp.pi * n * n * y)
        s += t
        if t < mp.mpf(10) ** (-mp.mp.dps - 8):
            break
        n += 1
    return 2 * s

def theta(y):
    y = mp.mpf(y)
    if y >= 1:
        return 1 + thetam1(y)
    return (1 + thetam1(1 / y)) / mp.sqrt(y)

TH1 = theta(1)
BOUND = 3 - 2 * TH1

def r0(X):
    return mp.e ** (X / 2) * thetam1(mp.e ** X)

def p(X):
    return 1 - r0(X)

def Lam_gt_quad(s):
    """Lambda_>(s) = -int_0^infty p(X) e^{-zX} dX, z=(1-s)/2, by quadrature."""
    z = (1 - s) / 2
    f = lambda X: p(X) * mp.e ** (-z * X)
    # p(X) -> 1 exponentially; split [0,3] and the analytic tail int_3^inf 1*e^{-zX}
    head = mp.quad(f, [0, 0.5, 1, 2, 3])
    corr = mp.quad(lambda X: (p(X) - 1) * mp.e ** (-z * X), [3, 6, 12])
    tail = mp.e ** (-3 * z) / z
    return -(head + corr + tail)

def Lam_gt_gamma(s):
    """Lambda_>(s) = 2/(s-1) + 2 sum_{n>=1} (pi n^2)^{-s/2} Gamma(s/2, pi n^2)."""
    tot = mp.mpf(0)
    for n in range(1, 13):
        tot += (mp.pi * n * n) ** (-s / 2) * mp.gammainc(s / 2, mp.pi * n * n)
    return 2 / (s - 1) + 2 * tot

def lhs(s):
    return mp.re(-(1 - s) * Lam_gt_gamma(s) / 2)

print("theta(1)      =", mp.nstr(TH1, 20))
print("p(0)=2-th(1)  =", mp.nstr(p(0), 20))
print("int p' = th-1 =", mp.nstr(TH1 - 1, 20))
print("bound 3-2th(1)=", mp.nstr(BOUND, 20))
print()

# --- consistency of the two evaluations of Lambda_> --------------------------
print("A1  Lambda_> : incomplete-gamma form vs the T3(c) quadrature form")
for s in [mp.mpf('0.3'), mp.mpc('0.5', '3'), mp.mpc('-0.4', '2'),
          mp.mpc('0.99', '0'), mp.mpc('-5', '1')]:
    a, b = Lam_gt_gamma(s), Lam_gt_quad(s)
    print("   s=%-18s gamma=%-34s rel.diff=%s"
          % (mp.nstr(s, 8), mp.nstr(a, 12), mp.nstr(abs(a - b) / abs(a), 3)))
print()

# --- the IBP identity --------------------------------------------------------
print("A2  -z Lambda_>(s) = p(0) + int_0^inf p'(X) e^{-zX} dX")
dp = lambda X: mp.diff(p, X)
for s in [mp.mpf('0.3'), mp.mpc('0.5', '3'), mp.mpc('-2', '7')]:
    z = (1 - s) / 2
    L = -z * Lam_gt_gamma(s)
    R = p(0) + mp.quad(lambda X: dp(X) * mp.e ** (-z * X), [0, 0.5, 1, 2, 4, 8])
    print("   s=%-16s LHS=%-32s rel.diff=%s"
          % (mp.nstr(s, 6), mp.nstr(L, 12), mp.nstr(abs(L - R) / abs(L), 3)))
print("   int_0^inf p' dX =", mp.nstr(mp.quad(dp, [0, .5, 1, 2, 4, 8, 16]), 12),
      " (predicted theta(1)-1 =", mp.nstr(TH1 - 1, 12), ")")
print()

# --- the grid ----------------------------------------------------------------
print("A3  grid: Re[-(1-s)Lambda_>(s)/2] >= %s ?" % mp.nstr(BOUND, 10))
res = [mp.mpf(x) for x in
       ['-200', '-50', '-20', '-5', '-1', '0', '0.25', '0.5', '0.75', '0.9',
        '0.99', '0.999', '0.99999', '0.9999999']]
ims = [mp.mpf(x) for x in ['0', '0.5', '1', '5', '20', '100', '1000', '10000']]
worst = mp.mpf('1e9'); worst_at = None; npts = 0; fails = 0
vmin_row = {}
for re_s in res:
    row = []
    for im_s in ims:
        s = mp.mpc(re_s, im_s)
        v = lhs(s)
        npts += 1
        row.append(v)
        if v < BOUND:
            fails += 1
            print("   *** VIOLATION at s =", mp.nstr(s, 10), " value =", mp.nstr(v, 12))
        if v < worst:
            worst, worst_at = v, s
    vmin_row[str(re_s)] = min(row)
for k in vmin_row:
    print("   Re s = %-12s  min over Im s grid = %s" % (k, mp.nstr(vmin_row[k], 12)))
print("   points tested: %d,  violations: %d" % (npts, fails))
print("   infimum on the grid = %s at s = %s" % (mp.nstr(worst, 14), mp.nstr(worst_at, 10)))
print()

# --- boundary behaviour Re s -> 1 and the two extremes ------------------------
print("A4  limits")
for eps in ['1e-2', '1e-4', '1e-6', '1e-9']:
    s = 1 - mp.mpf(eps)
    print("   s = 1-%-8s  -zL = %s   (predicted limit p(0)+int p' = 1)"
          % (eps, mp.nstr(lhs(s), 14)))
for re_s in ['-10', '-100', '-1000']:
    s = mp.mpf(re_s)
    print("   s = %-8s      -zL = %s   (predicted limit p(0) = %s)"
          % (re_s, mp.nstr(lhs(s), 14), mp.nstr(p(0), 14)))
print()

# --- zero-freeness spot check: |Lambda_>| bounded away from 0 ----------------
print("A5  |Lambda_>(s)| on the grid (should never be 0)")
mn = mp.mpf('1e9')
for re_s in res:
    for im_s in ims:
        s = mp.mpc(re_s, im_s)
        v = abs(Lam_gt_gamma(s))
        if v < mn:
            mn, mn_at = v, s
print("   min |Lambda_>| = %s at s = %s" % (mp.nstr(mn, 10), mp.nstr(mn_at, 10)))
print("   (|Lambda_>(s)| >= 2*bound/|1-s| is implied; no zero possible)")
