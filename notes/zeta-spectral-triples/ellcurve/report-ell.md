# MVP-3 report: the CCM construction on L(E, s) for E/Q, and on real Dirichlet characters (2026-09-18)

Plan `plan.md` (draft + "Review outcome"), review `astra-review.md` (formula sheet F1-F18, authoritative),
prototype `checks/ell_check.py` (astra), C implementation in `zst/` (Lane B: `kernel.c`, `weil_data.c`,
`ellcurve.c`, `dirichlet.c`; Lane C: `parity.c`, `ell_ref.c`, CLI `tools/zst.c`), 12 tests green in 3 s,
captured runs under `bench/`. Ground truth PARI 2.17.2 via cypari2 (`zst/tools/pari_ref.py`,
`tests/data/ell_ref.txt`, `tests/data/dirichlet_ref.txt`).

## 1. What was built

The generic explicit-formula data model of the parent plan (M3): a window distribution on `[0, L]` made
of atoms, subtracted gamma-factor kernels `(Q, d, mu, mult)`, optional rank-one pole terms, a conductor and
an identity shift, with the archimedean constants DERIVED (F8) rather than typed. Regression G1: zeta
through the generic builder reproduces `zst_riemann_ab` (every `a_n`, `b_n`, including the shift) to
`1e-40` at `x = 9, 13`. Two independent instances: real primitive Dirichlet characters (`Gamma_R(s + kappa)`,
no pole) and elliptic curves over Q (`Gamma_C(s + 1/2)`, conductor, bad primes, no pole), each pinned to an
independent mpmath computation (Lane B's `checks/dirichlet_pins.py` written from the sheet alone;
`checks/ell_pins.py` from astra's prototype). Point counting on the general Weierstrass equation matches
PARI's `ellap` at all 1468 primes `<= 2500` of the four curves (including p = 2, 3 and the bad primes).
Certified parity of the global minimum (`zst_parity`: certified minima of the even and odd blocks) gates
the construction: only an even minimum admits the paper's rank-one perturbation.

## 2. Results (certified balls; review numbers reproduced to all printed digits)

| object | x | N | min E | min O | parity | first zero error | wall |
|---|---:|---:|---|---|:--:|---:|---:|
| 11a1 (C = 11, w = +1, r = 0) | 13 | 60 | 7.68e-7 | 1.52e-4 | even | 4.10e-4 | 0.7 s |
| 11a1 | 30 | 120 | 1.36e-12 | 5.67e-10 | even | 2.13e-9 | 4.5 s |
| 14a1 (C = 14, two bad primes) | 13 | 60 | 5.50e-6 | 9.12e-4 | even | 8.54e-4 | 0.8 s |
| 37a1 (C = 37, w = -1, r = 1) | 8 / 13 / 20 | 60 | 0.933 / 0.204 / 0.0254 | 0.159 / 0.0125 / 7.8e-4 | ODD | (inapplicable) | 1.6 s |
| 389a1 (C = 389, w = +1, r = 2) | 8 / 13 / 20 | 60 | 3.51 / 3.16 / 2.76 | 2.58 / 1.64 / 0.815 | ODD | (inapplicable) | 1.6 s |
| chi_{-4} | 13 | 40 | 4.94e-14 | 8.12e-11 | even | 1.90e-12 | 0.2 s |
| chi_5 | 13 | 40 | 2.48e-12 | 3.30e-9 | even | 3.90e-10 | 0.2 s |

Zeta for comparison (same machine, earlier): x = 13, N = 20: first zero error 2.3e-35.

## 3. What was learned about the construction

1. **The construction cannot see a central zero.** Under the paper's hypotheses `D''` is invertible
   (`xi_0 = prod s_k^2 / (N!)^2 > 0`, review Q1), so an odd-order zero at the centre is not representable
   at any finite N. Numerically the hypothesis itself fails for both rank-positive curves: the global
   minimum of the Weil form is ODD at every tested window for 37a1 (w = -1) AND for 389a1 (w = +1). So
   the parity of the minimiser is the observable, and it is not a root-number theorem. The central
   multiplicity-r term is `r L |V_0><V_0|` and penalises only the even block, which explains the
   observation without proving it. An odd-radical variant (`beta/B` in place of `eta`) exists but has
   two central zero modes; an antiperiodic (half-integer) Fourier grid is the natural follow-up
   (H-HALF-GRID, open).
2. **Accuracy is object-dependent.** From x = 13 to 30, 11a1 gains 5 digits where zeta gained ~92; the
   truncation N is not the limit (N = 60 -> 120 moves the 11a1 value by 3e-6 at an error of 4e-4). The
   natural window scale for weight 2 is `sqrt(x / C_E)` (Mellin kernel `e^{-2 pi u / sqrt C_E}`) rather
   than `x` (theta kernel): H-RATE, open; the "5.5 digits per unit x" law is zeta's, not universal.
   Conductor 14 (two bad primes) is only twice as bad as conductor 11 at the same window.
3. **The conductor enters only through the atoms and an identity shift** (`+log C` on the diagonal,
   F8), an exact invariance now a unit test (Q3): the spectrum of the construction does not see `C`
   except through `a_p`.
4. **Dirichlet characters behave like zeta.** chi_{-4} at x = 13, N = 40 reaches 1.9e-12 on the first
   zero (6.0209...); the odd character's `Gamma_R(s + 1)` kernel `(2, 3/2)` and the even character's
   `(2, 1/2)` both come out of the same builder.
5. **A soundness bug in the zeta MVP's certifier, found and fixed.** `zst_eigmin`'s Krawczyk
   contraction used the mean-value remainder `2 R_x (D_lam D_x)`, valid only for a box centred on the
   approximation; the contraction moves the box off-centre and the factor 2 then EXCLUDED the true
   solution whenever inverse iteration had not converged (reproducer: dyadic 4x4 with spectrum
   {5, 7, 10, 13}, 10 iterations returned `[5.0000792 +/- 5e-21]`). Fixed to the exact quadratic
   remainder (F is quadratic, so `F(y~ + d) = F(y~) + J d - d_lam d_x` exactly); regression test in
   `test_eigmin.c` (red on the old code, green now). All earlier zeta certificates were unaffected
   (their inverse iteration converges in one step; Lane C cross-checked x = 9..30 independently).
   Lane C's `zst_block_min` brackets the minimum between a Rayleigh quotient and a certified
   positive-definiteness shift and does not rely on the Krawczyk box at all.

## 4. Open

- H-HALF-GRID: an odd-dimensional (antiperiodic) truncation that can carry a single central mode;
  derive basis, edge functional, kernel integrals (F14 assumes integer frequencies).
- H-RATE: fit the 11a1/14a1 first-zero error against `sqrt(x/C)` and `x` at two N each, x = 13..60.
- De-duplicate Rump's `isspd` (`verify_pd` static in `eigmin.c`, copied into `parity.c`); replace
  `zst_inertia_neg` (unpivoted LDL, unusable at N >~ 120) by the isspd route.
- Precision floor: isspd certifies `lambda_min > ~2^{-prec/2} ||A||`; zeta at x = 30, N = 120 needs
  ~1400 bits for its `2.2e-135` minimum (graceful: wide but valid enclosure otherwise).
- Mutation and fuzz for the new modules (relaxed for the tracer bullet).
