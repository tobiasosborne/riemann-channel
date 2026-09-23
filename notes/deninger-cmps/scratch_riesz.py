"""Check for reformulation.md, Proposition R7(b): the zero-mode kernels of the model space K_S are not a
Riesz basis (Carleson's condition fails), so no bounded change of inner product on K_S makes the compressed
dilation normal with the modes as eigenvectors.

Modes (prop:functional-model-modes, obs:model-modes-sign): w_n = -gamma_n/2 - i(1-sigma_n)/2 in the lower
half plane; RH is assumed here only to place Im w_n = -1/4 (the first 3000 zeros are on the line to the
precision of data/zeros3000.npy).  Pseudo-hyperbolic distance rho(a,b) = |a-b|/|a-conj b|.  Gram matrix of
the normalised reproducing kernels k_w(tau) = (tau - conj w)^{-1} of H^2 of the lower half plane:
G_nm = 2 sqrt(Im w_n Im w_m) / (i (conj w_n - w_m)) up to the sign convention, |G_nn| = 1.
Author's own check (claude:fable-5.1), not a blind lane.  Run from the repository root.
"""
import numpy as np

z = np.load('data/zeros3000.npy')
lam = -z / 2 - 0.25j
rho = np.abs(lam[1:] - lam[:-1]) / np.abs(lam[1:] - np.conj(lam[:-1]))
print('nearest-neighbour pseudo-hyperbolic distances of the first 3000 modes')
print('  first five  :', np.round(rho[:5], 4))
print('  minimum     :', round(float(rho.min()), 5), 'at n =', int(rho.argmin()) + 1)
print('  last five   :', np.round(rho[-5:], 4))
gap = np.mean(np.diff(z[-200:]))
print('  mean gap of the last 200 zeros:', round(float(gap), 4),
      '  2 pi / log(gamma/2pi) =', round(float(2 * np.pi / np.log(z[-1] / (2 * np.pi))), 4))
print('  under RH rho^2 = (d/2)^2 / ((d/2)^2 + 1/4) for a gap d, so rho -> 0 along any subsequence of gaps -> 0')


def gram(n):
    w = lam[:n]
    a = np.sqrt(np.abs(w.imag))
    return 2 * np.outer(a, a) / (1j * (np.conj(w)[:, None] - w[None, :]))


print('Gram matrix of the normalised kernels: smallest singular value against N')
for n in (10, 25, 50, 100, 200, 400, 800):
    s = np.linalg.svd(gram(n), compute_uv=False)
    print(f'  N = {n:4d}:  sigma_min = {s.min():.3e}   sigma_max = {s.max():.3f}   cond = {s.max() / s.min():.2e}')
print('a Riesz basis would have sigma_min bounded below uniformly in N; the decrease is monotone here')
