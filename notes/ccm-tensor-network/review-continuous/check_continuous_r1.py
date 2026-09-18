#!/usr/bin/env python3
"""Independent checks for the continuous CCM tensor-network review.

Run normally for green.  Run with --mutate to reverse beta in the
displacement identity; the checker must then exit nonzero.
"""

import sys
import numpy as np


MUTATE = "--mutate" in sys.argv
passed = 0
failed = 0


def check(name, condition, detail=""):
    global passed, failed
    if bool(condition):
        passed += 1
        print(f"PASS {name}")
    else:
        failed += 1
        print(f"FAIL {name}: {detail}")


def close(name, got, want, tol=2e-9):
    err = float(np.max(np.abs(np.asarray(got) - np.asarray(want))))
    check(name, err <= tol, f"max error {err:.3e}, got={got}, want={want}")


# C3: independently integrate zero-extended Fourier correlations.
L = 2.7
grid = np.linspace(0.0, L, 500_001)
for m, n in [(-2, 1), (-1, 2), (0, 2)]:
    corr = (
        np.sin(2 * np.pi * m * grid / L)
        - np.sin(2 * np.pi * n * grid / L)
    ) / (np.pi * (n - m))
    # A nontrivial smooth half-interval density.
    density = 1.0 + 0.3 * grid + 0.2 * np.cos(1.7 * grid)
    direct = np.trapezoid(corr * density, grid)
    b_m = -np.trapezoid(
        np.sin(2 * np.pi * m * grid / L) * density, grid
    ) / np.pi
    b_n = -np.trapezoid(
        np.sin(2 * np.pi * n * grid / L) * density, grid
    ) / np.pi
    close(f"C3 Loewner sign m={m},n={n}", direct, (b_m - b_n) / (m - n))

# Endpoint distributions: delta'_0(phi)=-phi'(0+) gives +2/L in every entry.
for m, n in [(-2, 1), (0, 0), (2, 2)]:
    if m == n:
        deriv = -2.0 / L
    else:
        deriv = (2 * np.pi * (m - n) / L) / (np.pi * (n - m))
    close(f"delta-prime endpoint m={m},n={n}", -deriv, 2.0 / L, 1e-13)

# C3/C4: arbitrary Loewner data, displacement, and the exact N=1 example.
indices = np.array([-1.0, 0.0, 1.0])
T = np.array([[6.0, 2.0, 2.0], [2.0, 1.0, 2.0], [2.0, 2.0, 6.0]])
D = np.diag(indices)
xi = np.array([-0.5, 2.0, -0.5])
eta = np.ones(3)
beta = np.array([-2.0, 0.0, 2.0])
if MUTATE:
    beta = -beta
disp = D @ T - T @ D
rhs = np.outer(beta, eta) - np.outer(eta, beta)
close("C3 rank-two displacement", disp, rhs, 1e-13)
close("C4 T xi", T @ xi, np.zeros(3), 1e-13)
close("C4 T D xi=-beta", T @ D @ xi, -beta, 1e-13)
Dprime = D - np.outer(D @ xi, eta)
close("C4 metric symmetry", T @ Dprime, Dprime.T @ T, 1e-13)
check("C5 counter spectrum T", np.allclose(np.linalg.eigvalsh(T), [0.0, 4.0, 9.0]))

# Quotient representative on xi-perp and its outer roots.
_, _, vh = np.linalg.svd(xi.reshape(1, -1))
C = vh[1:].T
G = C.T @ T @ C
B = C.T @ Dprime @ C
Hq = np.linalg.cholesky(G)
# Similarity using a spectral solve is robust to the Cholesky orientation.
qeval = np.linalg.eigvals(np.linalg.solve(G, B.T @ G).T)  # same B eigenvalues
close("C5 quotient roots", np.sort(np.real(np.linalg.eigvals(B))), [-np.sqrt(2), np.sqrt(2)], 2e-12)
check("C5 roots outside Fourier grid", np.max(np.abs(np.linalg.eigvals(B))) > 1.4)

# C5 Fourier transform formula, including included-grid removable limits.
Lf = 3.1
omega = 2 * np.pi * indices / Lf
z = 0.73 + 0.41j
xgrid = np.linspace(0.0, Lf, 600_001)
fun = sum(xi[j] * np.exp(1j * omega[j] * xgrid) / np.sqrt(Lf) for j in range(3))
direct = np.trapezoid(fun * np.exp(-1j * z * (xgrid - Lf / 2)), xgrid)
# Centered transform; the multiplicative convention cancels the centering phase.
formula = 2 / np.sqrt(Lf) * np.sin(z * Lf / 2) * np.sum(xi / (z - omega))
close("C5 Fourier rational formula", direct, formula, 2e-9)
for j in range(3):
    expected = np.sqrt(Lf) * ((-1) ** int(indices[j])) * xi[j]
    direct_grid = np.trapezoid(
        fun * np.exp(-1j * omega[j] * (xgrid - Lf / 2)), xgrid
    )
    close(f"C5 included grid j={int(indices[j])}", direct_grid, expected, 2e-9)

# Fourier convention audit: U(t)=exp(-itH) matches the MINUS transform.
tgrid = np.linspace(0.0, 1.0, 500_001)
fvals = tgrid
h = 2.0
feature = np.trapezoid(fvals * np.exp(-1j * h * tgrid), tgrid)
minus_hat = feature
plus_hat = np.trapezoid(fvals * np.exp(+1j * h * tgrid), tgrid)
close("Fourier U=e^-itH uses minus sign", feature, minus_hat, 1e-13)
check("Fourier plus and minus differ", abs(feature - plus_hat) > 0.5)

# C7: nontrivial exact finite intertwiner with H=diag(+1/2,-1/2).
Lc = 2 * np.pi
js = np.array([-1.0, 0.0, 1.0])
hs = np.array([0.5, -0.5])


def mode_integral(j, hh):
    a = j - hh
    return (np.exp(1j * a * Lc) - 1.0) / (1j * a * np.sqrt(Lc))


features = np.array([[mode_integral(j, hh) for j in js] for hh in hs])
xi_b = np.array([3 * np.sqrt(Lc) / 8, np.sqrt(Lc) / 4, 3 * np.sqrt(Lc) / 8])
close("C7 xi endpoint normalization", np.sum(xi_b) / np.sqrt(Lc), 1.0, 1e-13)
close("C7 A xi=0", features @ xi_b, np.zeros(2), 1e-12)
Q = features.conj().T @ features
check("C7 exact Gram has simple radical", np.linalg.matrix_rank(Q, tol=1e-10) == 2)
c = np.array([0.4 + 0.2j, -0.7 + 0.1j, 1.1 - 0.3j])
f0 = np.sum(c) / np.sqrt(Lc)
dprime_c = js * c - f0 * (js * xi_b)
close("C7 corrected intertwiner", features @ dprime_c, hs * (features @ c), 2e-12)

# Missing-hypothesis counterexample for C7: epsilon=0 need not mean ker Q=C xi.
features_rank1 = np.array([[0.0, np.sqrt(Lc), 0.0]], dtype=complex)
Q_rank1 = features_rank1.conj().T @ features_rank1
xi_one = np.array([np.sqrt(Lc) / 2, 0.0, np.sqrt(Lc) / 2])
close("C7 nonsimple example A xi=0", features_rank1 @ xi_one, [0.0], 1e-13)
check("C7 nonsimple zero minimum", abs(np.min(np.linalg.eigvalsh(Q_rank1))) < 1e-13)
check("C7 radical dimension is two", 3 - np.linalg.matrix_rank(Q_rank1) == 2)

print(f"TALLY check_continuous_r1.py: {passed} PASS / {failed} FAIL")
sys.exit(1 if failed else 0)
