#!/usr/bin/env python3
"""REFUTE lane R, RTP-1 (claude:opus, 2026-09-24).  Independent (a_n, b_n) of the CCM window form.

Written from the definitions (QW = Psi(f^* * g), Psi = W02 - W_R - sum_p W_p; Loewner data
a_n = Psi(q(U_n,U_n)), b_n = n Psi(q(U_n,U_0))) with this reviewer's own closed forms:
  pole    : a = Re 2*sum_{s=+-1/2} J(s + i w),  J(sig) = -1/sig + (e^{sig L} - 1)/(sig^2 L)
            b = -(1/pi) Im sum_{s} (e^{(s+iw)L} - 1)/(s + i w)                       (direct exponentials)
  arch    : a = -[(log 4pi + gamma) - log((e^L+1)/(e^L-1)) + 2 A_R],
            A_R = (1/2) Re[psi(1/2) - psi(A)] - Re psi'(A)/(4L) + (e/(4L)) Re S2(A) + (e^{-L}/2) sum z^k/(k+1/2)
            b = [-(1/2) Im psi(A) - (e/2) Im S1(A)]/pi,   A = 1/4 - i pi n/L, e = e^{-L/2}, z = e^{-2L}
  primes  : a = -2 sum_k Lambda(k) k^{-1/2} (1 - log k/L) cos(w log k),  b = (1/pi) sum_k Lambda(k) k^{-1/2} sin(w log k)
(the arch arrangement differs from zst's formula sheet: psi(1/2), no I_2/I_3/C(L) split; derived here).
Self-test (run as a script): (i) arch and pole against direct mpmath quadrature of the defining
integrals at 50 digits; (ii) totals against the 30 digits printed by lane A1 / A2 at x = 13.
Deterministic; no timestamps.
"""
import sys
from flint import arb, acb, ctx
import math

def von_mangoldt_table(X):
    """list of (k, p) for prime powers 1 < k <= X"""
    X = int(X)
    sieve = [True] * (X + 1)
    out = []
    for p in range(2, X + 1):
        if sieve[p]:
            for m in range(p * p, X + 1, p):
                sieve[m] = False
            k = p
            while k <= X:
                out.append((k, p)); k *= p
    out.sort()
    return out

def ab_parts(L, Nmax, primes, prec, weights=None):
    """L: arb window length; primes: list of (k,p); returns dict of lists of arb (a,b) per part.
    weights: optional dict k -> arb replacing Lambda(k) k^{-1/2} (for the lattice-weight problem)."""
    old = ctx.prec
    ctx.prec = prec + 40
    L = arb(L)
    pi = arb.pi()
    e = (-L / 2).exp()
    z = (-2 * L).exp()
    # number of Lerch terms: z^K < 2^-(prec+40)
    K = int((prec + 60) / (2 * float(L) / math.log(2))) + 5
    half = arb(1) / 2
    euler = arb.const_euler()
    const = (4 * pi).log() + euler - ((L.exp() + 1) / (L.exp() - 1)).log()
    shalf = arb(0)
    for k in range(K):
        shalf += z ** k / (k + half)
    psi_half = acb(half).digamma()
    out = {'pole': ([], []), 'arch': ([], []), 'prime': ([], [])}
    pw = []
    for (k, p) in primes:
        w = weights[k] if weights is not None else arb(p).log() / arb(k).sqrt()
        pw.append((arb(k).log(), w))
    for n in range(Nmax + 1):
        w = 2 * pi * n / L
        # pole
        ap = arb(0); bp = arb(0)
        for s in (half, -half):
            sig = acb(s, w)
            eL = (sig * L).exp()
            J = -1 / sig + (eL - 1) / (sig * sig * L)
            ap += 2 * J.real
            bp += -((eL - 1) / sig).imag / pi
        # arch
        A = acb(arb(1) / 4, -pi * n / L)
        psiA = A.digamma()
        psi1A = A.polygamma(1) if hasattr(A, 'polygamma') else None
        if psi1A is None:
            raise RuntimeError('no polygamma')
        S1 = acb(0); S2 = acb(0); zk = arb(1)
        for k in range(K):
            S1 += zk / (k + A)
            S2 += zk / ((k + A) ** 2)
            zk *= z
        AR = (psi_half - psiA).real / 2 - psi1A.real / (4 * L) + e / (4 * L) * S2.real + (-L).exp() / 2 * shalf
        ar = -(const + 2 * AR)
        br = (-psiA.imag / 2 - e / 2 * S1.imag) / pi
        # primes
        apr = arb(0); bpr = arb(0)
        for (lk, wk) in pw:
            th = w * lk
            apr += -2 * wk * (1 - lk / L) * th.cos()
            bpr += wk * th.sin() / pi
        out['pole'][0].append(ap); out['pole'][1].append(bp if n else arb(0))
        out['arch'][0].append(ar); out['arch'][1].append(br if n else arb(0))
        out['prime'][0].append(apr); out['prime'][1].append(bpr if n else arb(0))
    ctx.prec = old
    return out

def ab_total(L, Nmax, primes, prec, parts=('pole', 'arch', 'prime'), weights=None):
    P = ab_parts(L, Nmax, primes, prec, weights)
    a = [sum((P[q][0][n] for q in parts), arb(0)) for n in range(Nmax + 1)]
    b = [sum((P[q][1][n] for q in parts), arb(0)) for n in range(Nmax + 1)]
    return a, b

if __name__ == '__main__':
    import mpmath as mp
    NCHK = [0]
    FAIL = [0]
    def check(cond, msg):
        NCHK[0] += 1
        if not cond:
            FAIL[0] += 1
        print(('PASS ' if cond else 'FAIL ') + msg)
    mp.mp.dps = 50
    x = 13
    Lf = mp.log(x)
    ctx.prec = 400
    L = arb(13).log()
    P = ab_parts(L, 12, von_mangoldt_table(13), 400)
    rho = lambda y: mp.e ** (y / 2) / (mp.e ** y - mp.e ** (-y))
    for n in (0, 1, 2, 5, 12):
        w = 2 * mp.pi * n / Lf
        # arch by quadrature of the definition
        f = lambda y: ((1 - y / Lf) * mp.cos(w * y) - mp.e ** (-y / 2)) * rho(y)
        AR = mp.quad(f, mp.linspace(0, Lf, 8))
        ar = -((mp.log(4 * mp.pi) + mp.euler) - mp.log((mp.e ** Lf + 1) / (mp.e ** Lf - 1)) + 2 * AR)
        br = mp.quad(lambda y: mp.sin(w * y) * rho(y), mp.linspace(0, Lf, 8)) / mp.pi
        ap = mp.quad(lambda y: 2 * (1 - y / Lf) * mp.cos(w * y) * 2 * mp.cosh(y / 2), mp.linspace(0, Lf, 8))
        bp = -mp.quad(lambda y: mp.sin(w * y) * 2 * mp.cosh(y / 2), mp.linspace(0, Lf, 8)) / mp.pi
        for name, qv, fv in (('arch a', ar, P['arch'][0][n]), ('arch b', br, P['arch'][1][n]),
                             ('pole a', ap, P['pole'][0][n]), ('pole b', bp, P['pole'][1][n])):
            d = abs(qv - mp.mpf(fv.mid().str(60, radius=False)))
            check(d < mp.mpf(10) ** -40, f'x=13 n={n} {name}: closed form vs quadrature, diff {mp.nstr(d, 3)}')
    # totals against lane A1 printed values (30 digits)
    a, b = ab_total(L, 3, von_mangoldt_table(13), 400)
    ref = {0: ('0.0453328442159587070934518363426', '0'),
           1: ('0.0465118895436779793116060710601', '0.0457203442394000540357853654912'),
           2: ('0.0506210483629745920069696920272', '0.0939818448885741857990582354453'),
           3: ('0.0603025794859511884689695760125', '0.148752677000255263998143181043')}
    for n in range(4):
        da = abs(mp.mpf(a[n].mid().str(40, radius=False)) - mp.mpf(ref[n][0]))
        db = abs(mp.mpf(b[n].mid().str(40, radius=False)) - mp.mpf(ref[n][1]))
        check(da < 1e-29 and db < 1e-29, f'x=13 n={n}: total (a,b) vs lane A1 printed 30 digits: {mp.nstr(da,2)}, {mp.nstr(db,2)}')
    print(f'# checks: {NCHK[0]} run, {FAIL[0]} failed')
