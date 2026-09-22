#!/usr/bin/env python3
"""Author: codex:gpt-6-astra. Finite checks, not certification of infinite claims."""
from pathlib import Path
import argparse
import math
import numpy as np
import mpmath as mp
from scipy.integrate import quad

mp.mp.dps = 65
ROOT = Path(__file__).resolve().parents[3]


def xi(z):
    return z * (z - 1) * mp.power(mp.pi, -z / 2) * mp.gamma(z / 2) * mp.zeta(z) / 2


def gram_quad(gamma, delta, c):
    out = np.empty((len(gamma), len(gamma)), dtype=complex)
    def weight(x):
        return math.exp(-x / 2) * (1 + (x / c) ** 2) ** (delta / 2)
    for i, gi in enumerate(gamma):
        for j in range(i + 1):
            tau = (gi - gamma[j]) / 2
            if i == j:
                val = quad(weight, 0, np.inf, epsabs=2e-11, epsrel=2e-12)[0]
            else:
                re = quad(weight, 0, np.inf, weight='cos', wvar=tau, epsabs=2e-11)[0]
                im = -quad(weight, 0, np.inf, weight='sin', wvar=tau, epsabs=2e-11)[0]
                val = re + 1j * im
            out[i, j] = val
            out[j, i] = np.conj(val)
    return out


def struve_laplace(s, delta, c):
    p = mp.mpf(delta) / 2
    nu = p + mp.mpf('0.5')
    return (mp.power(c, -2*p) * mp.sqrt(mp.pi) * mp.gamma(p+1) / 2
            * mp.power(2*c/s, nu) * (mp.struveh(nu, c*s) - mp.bessely(nu, c*s)))


def u_series(s, delta, c, count=35):
    p = mp.mpf(delta)/2
    return c * mp.fsum([(-2)**n * mp.binomial(p, n) * mp.factorial(n)
                       * mp.hyperu(n+1, delta-n+2, c*s) for n in range(count)])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--matrices', action='store_true', help='Print all first-ten Gram entries.')
    opts = parser.parse_args()
    zeros = [mp.zetazero(j) for j in range(1, 11)]
    gamma = np.array([float(z.imag) for z in zeros])
    all_positive = np.load(ROOT / 'data/zeros3000.npy')
    all_signed = np.concatenate((-all_positive, all_positive))
    print('Author: codex:gpt-6-astra')
    print('n gamma |Theta_prime| reciprocal norm_b norm_b/reciprocal product6000_norm')
    for j, rho in enumerate(zeros):
        # At a zero of zeta, only its differentiated factor survives in xi'.
        xi_prime = (rho*(rho-1)/2 * mp.power(mp.pi, -rho/2)
                    * mp.gamma(rho/2) * mp.diff(mp.zeta, rho))
        theta_prime = 2j * xi_prime / xi(2-rho)
        w = rho.imag/2 + mp.j/4
        independently_differentiated = mp.diff(lambda z: xi(1+2j*z)/xi(1-2j*z), w)
        assert abs(theta_prime / independently_differentiated - 1) < mp.mpf('1e-50')
        reciprocal = 1 / abs(theta_prime)
        pole_integral = quad(lambda x: 1/(2*math.pi*(x*x+0.25**2)),
                             -np.inf, np.inf, epsabs=1e-12)[0]
        norm_b = math.sqrt(pole_integral) * float(reciprocal)
        diffs = float(rho.imag)-all_signed
        diffs = diffs[np.abs(diffs)>1e-9]
        partial_product = math.exp(-math.log(2)/2 + np.log1p(diffs**-2).sum()/2)
        assert partial_product < norm_b
        print(j+1, mp.nstr(rho.imag, 18), mp.nstr(abs(theta_prime), 14),
              mp.nstr(reciprocal, 14), f'{norm_b:.12f}',
              f'{norm_b/float(reciprocal):.12f}', f'{partial_product:.12f}')
    s = 0.5 + 0.5j * (gamma[:, None]-gamma[None, :])
    m0 = 1/s
    print('\nGram spectra: delta c diagonal raw_min raw_max normalized_min normalized_max')
    matrices = [(0, 2, m0)]
    for c in [1, 2]:
        for delta in [1, 2]:
            gram = gram_quad(gamma, delta, c)
            if delta == 2:
                assert np.max(np.abs(gram - (1/s + 2/(c*c*s**3)))) < 1e-9
            for i, j in [(0, 0), (0, 1), (0, 9), (8, 9)]:
                sv = mp.mpc(float(s[i, j].real), float(s[i, j].imag))
                special = complex(struve_laplace(sv, delta, c))
                assert abs(special-gram[i, j]) < 1e-9
            matrices.append((delta, c, gram))
    for delta, c, gram in matrices:
        ev = np.linalg.eigvalsh(gram)
        diag = gram[0, 0].real
        print(delta, c, *(f'{x:.12f}' for x in [diag, ev[0], ev[-1], ev[0]/diag, ev[-1]/diag]))
        print(' M12 =', format(gram[0, 1], '.12f'), 'M1,10 =', format(gram[0, 9], '.12f'))
        if opts.matrices:
            print(np.array2string(gram, precision=10, max_line_width=220))
    # Independent U expansion test with a controlled geometric expansion variable <= 1/2.
    us = u_series(mp.mpf('0.5'), 1, 2)
    direct = mp.quad(lambda x: mp.exp(-x/2)*mp.sqrt(1+x*x/4), [0, mp.inf])
    print('\n35-term U-series diagonal error:', mp.nstr(abs(us-direct), 8))
    assert abs(us-direct) < mp.mpf('1e-10')
    d = -0.25-0.5j*gamma
    loss = -(d[:, None]+d[None, :].conj())*m0
    arithmetic_loss = -(d[:, None]+d[None, :].conj())*np.eye(10)
    print('energy loss residual:', np.max(np.abs(loss-np.ones((10, 10)))))
    print('arithmetic loss residual:', np.max(np.abs(arithmetic_loss-0.5*np.eye(10))))
    print('energy loss eigenvalues:', np.linalg.eigvalsh(loss))
    print('arithmetic loss eigenvalues:', np.linalg.eigvalsh(arithmetic_loss))
    finite_loss = (1-np.exp(-s))/s
    print('energy finite-time t=1 min/max:', np.linalg.eigvalsh(finite_loss)[[0, -1]])
    print('arithmetic finite-time t=1 eigenvalue:', -math.expm1(-0.5))
    assert np.max(np.abs(loss-1)) < 1e-13
    assert np.max(np.abs(arithmetic_loss-0.5*np.eye(10))) < 1e-13
    assert np.linalg.eigvalsh(finite_loss)[0] > 0
    print('\nAsymptotic check: delta c tau |tau F|, tau^2 |s F - 1|')
    for delta, c in [(1, 1), (1, 2), (2, 2)]:
        for tau in [30., 100.]:
            sv = mp.mpc(.5, tau)
            # Oscillatory integral avoids huge cancelling Struve/Bessel values at high imaginary argument.
            def weight(x):
                return math.exp(-x/2)*(1+(x/c)**2)**(delta/2)
            fv = (quad(weight, 0, np.inf, weight='cos', wvar=tau, epsabs=1e-12)[0]
                  - 1j*quad(weight, 0, np.inf, weight='sin', wvar=tau, epsabs=1e-12)[0])
            print(delta, c, tau, f'{abs(tau*fv):.9f}', f'{tau*tau*abs(complex(sv)*fv-1):.9f}')
    print('All finite checks passed. Stored product is truncated, not a certified infinite tail.')


if __name__ == '__main__':
    main()
