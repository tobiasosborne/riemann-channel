#!/usr/bin/env python3
"""claude:opus REFUTE review of RTP-2 lane D, check of D1 (source prefactor). FLOATING.
(1) exact algebra: Slepian/Fuchs 1 - lambda_n(c) ~ 4 sqrt(pi) 8^n c^(n+1/2) e^(-2c) / n! for the time-band
    concentration eigenvalue; the compressed Fourier eigenvalue chi has |chi|^2 = lambda, so
    1 - |chi| ~ (1 - lambda)/2. With c = 2 pi lambda^2 (CCM eq. wop1) and n = 4 this must equal
    (2^14/3) sqrt2 pi^5 lambda^9 e^(-4 pi lambda^2) (mc2arXiv.tex 1324-1329).
(2) numerical: Nystrom eigenvalues of the sinc kernel on [-1,1] versus the Slepian leading term, n = 0, 4."""
import sympy as sp
import mpmath as mp
lam = sp.symbols('lambda', positive=True)
c = 2 * sp.pi * lam**2; n = 4
slep_half = 4 * sp.sqrt(sp.pi) * 8**n * c**sp.Rational(2*n+1, 2) / sp.factorial(n) / 2
ccm = sp.Rational(2**14, 3) * sp.sqrt(2) * sp.pi**5 * lam**9
print('(1) [Slepian/2 at c=2 pi lambda^2] / [CCM prefactor] =', sp.simplify(slep_half / ccm), '; exponent e^{-2c} = e^{-4 pi lambda^2}:', sp.simplify(2*c - 4*sp.pi*lam**2) == 0)
mp.mp.dps = 40
M = 70
xs, ws = zip(*[(x, w) for x, w in zip(*mp.gauss_legendre_nodes(M))]) if hasattr(mp, 'gauss_legendre_nodes') else (None, None)
if xs is None:
    import numpy as np
    xg, wg = np.polynomial.legendre.leggauss(M)
    # refine nodes to 40 digits by Newton on P_M
    xs = []
    for x0 in xg:
        x = mp.mpf(x0)
        for _ in range(8):
            p, dp = mp.legendre(M, x), mp.diff(lambda t: mp.legendre(M, t), x)
            x -= p / dp
        xs.append(x)
    ws = [2 / ((1 - x**2) * mp.diff(lambda t: mp.legendre(M, t), x)**2) for x in xs]
def kern(cc, x, y):
    return cc / mp.pi if x == y else mp.sin(cc * (x - y)) / (mp.pi * (x - y))
for cc in [4, 6, 8, 10]:
    A = mp.matrix(M, M)
    for i in range(M):
        for j in range(M):
            A[i, j] = mp.sqrt(ws[i]) * kern(cc, xs[i], xs[j]) * mp.sqrt(ws[j])
    ev = sorted(mp.eigsy(A, eigvals_only=True), reverse=True)
    out = []
    for nn in (0, 4):
        lead = 4 * mp.sqrt(mp.pi) * 8**nn * mp.mpf(cc)**(nn + mp.mpf(1)/2) * mp.e**(-2*cc) / mp.factorial(nn)
        out.append(f'n={nn}: 1-lambda={mp.nstr(1-ev[nn],6)} Slepian={mp.nstr(lead,6)} ratio={mp.nstr((1-ev[nn])/lead,5)}')
    print(f'(2) c={cc}: ' + ' | '.join(out))
