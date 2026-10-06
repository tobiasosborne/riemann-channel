"""REFUTE scratch (cm-lift.md), written from the statements only.
Inputs: PARI zeros (lfunzeros up to T=90) and PARI ellap for p<=4e5 (files zeros_*.txt, ap.txt from gp).
(1) a_p = (x|7) x for 4p = x^2+7y^2, and a_p(441d1) = (p|3) a_p(49a1), against ellap;
(2) theta series (1/2) sum eps(alpha) alpha q^{N alpha} against ellan;
(3) theta functional equation f(i/(Ny)) = eps N y^2 f(iy);
(4) Weil explicit formula with MY OWN Gaussian packets (no zero-mode term), prime side from PARI's a_p."""
import math, numpy as np, mpmath as mp, subprocess
from sympy import legendre_symbol as leg

def gp(cmd):
    return subprocess.run(['gp', '-q', '-f'], input=cmd + '\n\\q\n', capture_output=True, text=True).stdout.strip()

import os
if not os.path.exists('ap.txt'):
    gp('E1=ellinit("49a1"); E2=ellinit("441d1"); f=fileopen("ap.txt","w"); forprime(p=2,400000, filewrite(f, Str(p," ",ellap(E1,p)," ",ellap(E2,p)))); fileclose(f);')
for j, lab in [(1, '49a1'), (2, '441d1')]:
    if not os.path.exists(f'zeros_{j}.txt'):
        gp(f'default(realprecision,38); write("zeros_{j}.txt", lfunzeros(lfuncreate(ellinit("{lab}")),90));')
ap = {}
for line in open('ap.txt'):
    p, a1, a2 = map(int, line.split()); ap[p] = (a1, a2)
# (1)
bad = 0; nsplit = 0
for p, (a1, a2) in ap.items():
    if p > 10**4: break
    if p == 7 or leg(p % 7, 7) != 1:
        if not (a1 == 0 and (a2 == 0)): bad += 1
        continue
    nsplit += 1
    sols = [(xx, yy) for yy in range(1, int(math.isqrt(4*p//7)) + 1) for xx in [math.isqrt(4*p - 7*yy*yy)] if xx*xx + 7*yy*yy == 4*p and xx > 0]
    assert len(sols) == 1, (p, sols)
    xx = sols[0][0]
    pred = leg(xx % 7, 7) * xx
    pred2 = (leg(p % 3, 3) if p != 3 else 0) * pred
    if pred != a1 or pred2 != a2: bad += 1
print(f'(1) a_p formula, p<1e4: {nsplit} split primes, mismatches (incl. inert/bad zero test): {bad}')
# (2) theta series
NMAX = 600
an = list(map(int, gp(f'print(ellan(ellinit("49a1"),{NMAX}))').strip('[]').split(',')))
coef = [0j]*(NMAX + 1)
B = int(math.isqrt(4*NMAX)) + 2
for a in range(-B, B + 1):
    for b in range(-B, B + 1):
        # alpha = a + b w, w = (1+sqrt(-7))/2 ; N = a^2 + ab + 2b^2
        Nn = a*a + a*b + 2*b*b
        if Nn == 0 or Nn > NMAX: continue
        # alpha mod sqrt(-7): w = (1+s)/2 == 1/2 == 4 mod 7, so alpha == a + 4b mod 7
        r = (a + 4*b) % 7
        e = 0 if r == 0 else leg(r, 7)
        alpha = complex(a + b/2, b*math.sqrt(7)/2)
        coef[Nn] += 0.5*e*alpha
err = max(abs(coef[n] - an[n-1]) for n in range(1, NMAX + 1))
print(f'(2) theta series vs ellan up to n={NMAX}: max |diff| = {err:.1e}')
# (3) theta functional equation
mp.mp.dps = 30
an3 = list(map(int, gp('print(ellan(ellinit("49a1"),3000))').strip('[]').split(',')))
an4 = list(map(int, gp('print(ellan(ellinit("441d1"),3000))').strip('[]').split(',')))
for name, A, N, eps in [('49a1', an3, 49, 1), ('441d1', an4, 441, -1)]:
    f = lambda yy: mp.fsum(A[n-1]*mp.e**(-2*mp.pi*n*yy) for n in range(1, 3001))
    for yy in [mp.mpf('0.9')/mp.sqrt(N), mp.mpf('1.3')/mp.sqrt(N)]:
        lhs = f(1/(N*yy)); rhs = eps*N*yy**2*f(yy)
        print(f'(3) {name} y={float(yy):.4f}: f(i/Ny)={mp.nstr(lhs,12)}  eps N y^2 f(iy)={mp.nstr(rhs,12)}  rel.diff={mp.nstr(abs(lhs-rhs)/abs(lhs),3)}  (with -eps: {mp.nstr(abs(lhs+rhs)/abs(lhs),3)})')
# (4) explicit formula
def readz(fn):
    s = open(fn).read().strip().strip('[]')
    return np.array([float(t) for t in s.split(',')])
X = max(ap)
logp = {p: math.log(p) for p in ap}
def prime_side(which, N, E0, tau, t):
    # h(r) = exp(-tau^2 (r-E0)^2) e^{irt};  ghat(u) = (1/2pi) int h(r) e^{-iru} dr = (sqrt(pi)/(2 pi tau)) e^{-(u-t)^2/(4tau^2)} e^{-i E0 (u-t)}
    def gh(u):
        return math.sqrt(math.pi)/(2*math.pi*tau)*np.exp(-(u - t)**2/(4*tau*tau))*np.exp(-1j*E0*(u - t))
    S = 0j
    for p, a in ap.items():
        a = a[which]
        if N % p == 0: continue  # additive reduction: a_{p^k} = 0, local factor 1
        # normalised Frobenius roots alpha, beta with alpha+beta = a/sqrt p, alpha beta = 1
        c1 = a/math.sqrt(p)
        ck = [2.0, c1]  # power sums s_k = alpha^k+beta^k, s_k = c1 s_{k-1} - s_{k-2}
        k = 1; L = logp[p]
        while k*L < 40 * tau + t + 5 and p**k <= X**3:
            if k >= 2: ck.append(c1*ck[-1] - ck[-2])
            S += ck[k]*L/p**(k/2)*(gh(k*L) + gh(-k*L))
            k += 1
    return -S
def arch_side(N, E0, tau, t):
    mp.mp.dps = 20
    f = lambda r: mp.e**(-tau**2*(r - E0)**2)*mp.e**(1j*r*t)*(mp.log(N) - 2*mp.log(2*mp.pi) + 2*mp.re(mp.digamma(1 + 1j*r)))
    a, b = E0 - 9/tau, E0 + 9/tau
    pts = list(np.linspace(a, b, 13))
    return complex(mp.quad(f, pts))/(2*math.pi)
def zero_side(z, E0, tau, t):
    g = np.concatenate([z, -z[z > 0]])
    return complex(np.sum(np.exp(-tau**2*(g - E0)**2)*np.exp(1j*g*t)))
for which, name, N, fn in [(0, '49a1', 49, 'zeros_1.txt'), (1, '441d1', 441, 'zeros_2.txt')]:
    z = readz(fn)
    # sanity: largest p needed: exp(u) with u up to t + ~2*tau*sqrt(40 ln10)
    for (E0, tau) in [(15.0, 0.3), (40.0, 0.5), (2.0, 0.8), (0.0, 1.0)]:
        for t in [0.0, 0.7, 2.3]:
            Z = zero_side(z, E0, tau, t)
            P = prime_side(which, N, E0, tau, t)
            A = arch_side(N, E0, tau, t)
            print(f'(4) {name} E0={E0:5.1f} tau={tau} t={t}: zeros={Z.real:+.12f}{Z.imag:+.12f}i  primes+arch={(P+A).real:+.12f}{(P+A).imag:+.12f}i  |diff|={abs(Z-P-A):.1e}')
