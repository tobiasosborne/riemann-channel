#!/usr/bin/env python3
"""H-THETA hostile review, check D: the Jordan-chain rule at a multiple zero
(astra-proofs T6(a)), the K_Theta membership of Theta/(tau-w)^l (T6(b)
minimality), the ordinary-kernel overlap formula and the derivative-kernel
overlap sqrt((2j+1)/(2j+2)) (T6(b) Riesz failure).

Synthetic data only: a double zero of an inner function is manufactured so the
rule can be tested; no claim about actual zeta multiplicities is made.

Author: claude:opus (review lane), 2026-09-21.
"""
import mpmath as mp

mp.mp.dps = 30
I = mp.mpc(0, 1)

w = mp.mpc('7.0', '0.25')      # synthetic double zero of B
wb = mp.conj(w)

def B(tau, m=2):
    """inner function with a zero of order m at w (and nothing else)."""
    return ((tau - w) / (tau - wb)) ** m

# ---- D1: transform pair and the derivative kernels ---------------------------
print("D1  M[X^j e^{-i wbar X} 1_{X>0}](tau) = (-i)^{j+1} j! /(tau-wbar)^{j+1} ... check")
print("    equivalently  M^{-1} (tau-wbar)^{-(j+1)} = (-i)^{j+1}/j! X^j e^{-i wbar X}")
for j in range(3):
    lhs = mp.quad(lambda X: X ** j * mp.e ** (-I * wb * X) * mp.e ** (I * mp.mpf('0.7') * X),
                  [0, 5, 20, 80, mp.inf])
    # predicted: M[X^j e^{-i wbar X}] = j! * i^{j+1} / (tau-wbar)^{j+1}
    tau = mp.mpf('0.7')
    pred = mp.factorial(j) * I ** (j + 1) / (tau - wb) ** (j + 1)
    print("   j=%d  quad=%-30s pred=%-30s rel=%s"
          % (j, mp.nstr(lhs, 12), mp.nstr(pred, 12), mp.nstr(abs(lhs - pred) / abs(pred), 3)))
print()

# ---- D2: the derivative kernels lie in K_B ----------------------------------
print("D2  <(tau-wbar)^{-(j+1)}, B h> = 0 for h in H^2_+, j < m = 2  (membership in K_B)")
print("    exact contour value: conj[ B(w) h(w) ] for j=0, and a derivative for j=1")
def pair(j, hk, T=4000):
    """<k^(j), B h> with h = 1/(tau+i)^hk, measure du/2pi, by quadrature."""
    f = lambda u: (1 / (u - wb) ** (j + 1)) * mp.conj(B(u) / (u + I) ** hk)
    return mp.quad(f, [-T, -50, -10, 0, 7, 10, 50, T]) / (2 * mp.pi)
for j in [0, 1]:
    for hk in [1, 2]:
        v = pair(j, hk)
        print("   j=%d  h=1/(tau+i)^%d :  pairing = %-30s |.|=%s"
              % (j, hk, mp.nstr(v, 8), mp.nstr(abs(v), 4)))
print("   (they vanish to quadrature accuracy: B has a double zero at w)")
print("   for contrast, a THIRD kernel (j=2) must NOT be orthogonal:")
for hk in [1, 2]:
    v = pair(2, hk)
    print("   j=2  h=1/(tau+i)^%d :  pairing = %-30s |.|=%s"
          % (hk, mp.nstr(v, 8), mp.nstr(abs(v), 6)))
print()

# ---- D3: the Jordan rule for C_t --------------------------------------------
print("D3  Jordan rule  C_t (X^j e^{-i wbar X}) = e^{-i t wbar} sum_l C(j,l) t^{j-l} X^l e^{...}")
for t in ['0.0', '0.7', '2.5']:
    t = mp.mpf(t)
    maxerr = mp.mpf(0)
    for X in ['0.3', '1.1', '4.0']:
        X = mp.mpf(X)
        for j in [0, 1, 2]:
            lhs = (X + t) ** j * mp.e ** (-I * wb * (X + t))      # (C_t f_j)(X) = f_j(X+t)
            rhs = mp.e ** (-I * t * wb) * sum(mp.binomial(j, l) * t ** (j - l) * X ** l
                                              for l in range(j + 1)) * mp.e ** (-I * wb * X)
            maxerr = max(maxerr, abs(lhs - rhs))
    print("   t=%-6s max |C_t f_j - Jordan formula| over j<=2, 3 points X = %s"
          % (t, mp.nstr(maxerr, 4)))
print("   matrix of C_t on span(f_0,f_1) is e^{-i t wbar} [[1,t],[0,1]]: nilpotent part exact.")
print()

# ---- D4: Theta/(tau-w) in K_B and orthogonal to every ordinary kernel -------
print("D4  T6(b): at a double zero, B(tau)/(tau-w) lies in K_B and is _|_ k_w")
f = lambda u: (B(u) / (u - w)) * mp.conj(1 / (u - wb))
v = mp.quad(f, [-4000, -50, -10, 0, 7, 10, 50, 4000]) / (2 * mp.pi)
print("   <B/(tau-w), k_w> =", mp.nstr(v, 8), " |.|=", mp.nstr(abs(v), 4))
f2 = lambda u: (B(u) / (u - w)) * mp.conj(B(u) / (u + I) ** 2)
v2 = mp.quad(f2, [-4000, -50, -10, 0, 7, 10, 50, 4000]) / (2 * mp.pi)
print("   <B/(tau-w), B h>  =", mp.nstr(v2, 8), " |.|=", mp.nstr(abs(v2), 4), " (so it is in K_B)")
nrm = mp.quad(lambda u: abs(B(u) / (u - w)) ** 2, [-4000, -50, 0, 7, 50, 4000]) / (2 * mp.pi)
print("   ||B/(tau-w)||^2   =", mp.nstr(nrm, 10), " (nonzero: the ordinary kernels are NOT complete)")
print()

# ---- D5: normalised kernel overlaps -----------------------------------------
print("D5  |<k~_{a+ib}, k~_{a'+ib}>| = 2b/sqrt((a-a')^2+4b^2)   at b = 1/4")
b = mp.mpf('0.25')
for d in ['10', '2.5', '1', '0.25', '0.05', '0.005']:
    d = mp.mpf(d)
    a, ap = mp.mpf(0), d
    kw, kv = mp.mpc(a, b), mp.mpc(ap, b)
    ip = I / (kv - mp.conj(kw))             # <k_w,k_v> = i/(v - conj w), measure du/2pi
    nw = mp.sqrt(1 / (2 * b)); nv = nw
    num = abs(ip) / (nw * nv)
    pred = 2 * b / mp.sqrt((a - ap) ** 2 + 4 * b ** 2)
    # independent quadrature of the same inner product
    q = mp.quad(lambda u: (1 / (u - mp.conj(kw))) * mp.conj(1 / (u - mp.conj(kv))),
                [-8000, -100, 0, 100, 8000]) / (2 * mp.pi)
    print("   gap=%-8s overlap=%-16s formula=%-16s quad(ip) rel=%s"
          % (d, mp.nstr(num, 10), mp.nstr(pred, 10), mp.nstr(abs(q - ip) / abs(ip), 3)))
print("   -> 1 as the gap -> 0: no uniform Riesz lower bound if gaps get arbitrarily small.")
print()

print("D6  normalised consecutive derivative-kernel overlap = sqrt((2j+1)/(2j+2))")
for j in range(6):
    num = mp.gamma(2 * j + 2) / mp.sqrt(mp.gamma(2 * j + 1) * mp.gamma(2 * j + 3))
    pred = mp.sqrt(mp.mpf(2 * j + 1) / (2 * j + 2))
    # direct physical-space integrals with b = 1/4
    bb = mp.mpf('0.25')
    n0 = mp.quad(lambda X: X ** (2 * j) * mp.e ** (-2 * bb * X), [0, 10, 100, mp.inf])
    n1 = mp.quad(lambda X: X ** (2 * j + 2) * mp.e ** (-2 * bb * X), [0, 10, 100, mp.inf])
    cr = mp.quad(lambda X: X ** (2 * j + 1) * mp.e ** (-2 * bb * X), [0, 10, 100, mp.inf])
    direct = cr / mp.sqrt(n0 * n1)
    print("   j=%d  Gamma formula=%-16s sqrt((2j+1)/(2j+2))=%-16s direct quad=%s"
          % (j, mp.nstr(num, 10), mp.nstr(pred, 10), mp.nstr(direct, 10)))
print()

print("D7  the counting-function contradiction of T6(b): log|xi_crit(iv)| vs O(v)")
def xi(s):
    s = mp.mpc(s)
    return (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2 + 1) * mp.zeta(s)
for v in ['10', '100', '1000', '10000']:
    v = mp.mpf(v)
    val = mp.log(abs(xi(mp.mpf('0.5') - 2 * v)))
    print("   v=%-8s log|xi_crit(iv)| = log|xi(1/2-2v)| = %-20s   v log v = %s"
          % (v, mp.nstr(val, 12), mp.nstr(v * mp.log(v), 12)))
print("   ratio log|xi_crit(iv)|/(v log v) ->",
      mp.nstr(mp.log(abs(xi(mp.mpf('0.5') - 2 * mp.mpf('1e5')))) /
              (mp.mpf('1e5') * mp.log(mp.mpf('1e5'))), 8))
print("   a counting function N(T)=O(T) would force log|xi_crit(iv)| = O(v): contradiction.")
