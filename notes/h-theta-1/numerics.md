# H-THETA-1 numerics lane (numerics.md)

Author: `claude:fable-5.1` (numerics lane, independent of `notes/h-theta-1/checks/`, which was not read).
Script: `scripts/h_theta_1.py` (333 lines, mpmath at 30 digits for scalars, numpy double for the one linear
solve; deterministic). Output: `outputs/h_theta_1.txt`. Runtime 27 s. **48 checks, 48 pass, 0 fail.**

Targets: the eight numbered items of "Numerical checks for the blind lane" in `notes/h-theta-1/astra-proofs.md`
and the displayed formulas of T1 (3)–(4), T2 (5)–(6), T4 (15)–(23), T6 (30)–(35), T7 (37)–(41).

## Ledger

| id | verdict | check and value |
|---|---|---|
| D01 | PASS | item 1: 24-digit ordinates agree with data/zeros3000.npy (max dev) 0.00e+00 |
| D02 | PASS | item 1: xi(1/2 + i gamma_n) = 0 relative to a neighbour (max) 5.3e-24 |
| D03 | PASS | item 2: Cauchy Gram i/(w_j - conj w_i) matches the displayed 3x3 (max dev) 6.9e-09 |
| D04 | PASS | item 2: loss matrix -(d_i + conj d_j) G_ij is identically 1 (max dev) 1.8e-32 |
| D05 | PASS | item 2: notebook kernels (thm:model-space-jets) integrated in X=log y give the same Gram 2.5e-32 |
| D06 | PASS | item 2: loss spectrum (3,0,0) ['0.0', '1.97215e-31', '3.0'] |
| D07 | PASS | item 3: cyclic product of -(d_i + conj d_j) (11.477251648 - 37.3489700175j) |
| D08 | PASS | item 3: (16) Im[prod (2a + i q)] = -q12 q23 q31 != 0 -37.34897002 |
| D09 | PASS | item 4: F(2) real positive (structure-function normalisation (19)) 0.0411594371818 |
| D10 | PASS | item 4: E_*(2) = b 0.3513948086 |
| D11 | PASS | item 4: E_*(-1 -+ 1e-4) ~ -+1e-4 F(-1): no pole at s = -1, E_*(-1) = 0 (-1.15975e-5 + 0.0j) (1.15971e-5 + 0.0j) |
| D12 | PASS | item 4: E_*(rho_n) converged between 40 and 64 nodes (max rel dev) 3.0e-14 |
| D13 | PASS | item 4: structure-phase ratios (22) at the three zeros (max dev) ['(-0.9988074119 - 0.04882370219j)', '(-0.9998336882 + 0.01823721236j)', '(-0.9979057142 - 0.06468528111j)'] |
| D14 | PASS | item 4: /E_*^#/E_*/ = 1 on the critical line 0.0e+00 |
| D15 | PASS | item 4: the three phases are distinct (min pairwise distance) 0.0159 |
| D16 | PASS | item 4: Sonine Gram is real on the critical line (max /Im///./) 0.0e+00 |
| D17 | PASS | item 4: raw Sonine Gram G^Son entries (max rel dev from the displayed table) 1.6e-11 |
| D18 | PASS | item 4: normalised Sonine Gram O (23) (max dev) 4.5e-09 |
| D19 | PASS | item 4: loss matrix -(d_i + conj d_j) O_ij is Hermitian 0.0e+00 |
| D20 | PASS | item 4: loss spectrum (23) incl. the negative eigenvalue -0.09239752 ['-0.0923975213', '0.469315406', '1.12308212'] |
| D21 | PASS | item 4: the loss matrix is NOT positive (negative eigenvalue): no contraction realisation on these evaluators -0.0923975213 |
| D22 | PASS | item 4: cyclic product N12 N23 N31 of the actual loss matrix is not real (T4 (15)) (0.0056630306 - 0.018428485j) |
| D23 | PASS | item 4: extreme eigenvalues of T = Q C Q (diagnostic -0.4710777795, 0.5623175942) and //T// < 1 -0.4710777795 0.5623175942 |
| D24 | PASS | item 5: delta = 0.2 for both modes (0.2 + 0.0j) |
| D25 | PASS | item 5: reset trace one |
| D26 | PASS | item 5: modal-mixture holding law S(t) = e^{-0.2 t} for every mixture (max dev) 2.0e-31 |
| D27 | PASS | item 5: mean holding time 5 (continuous) (5.0 + 0.0j) |
| D28 | PASS | item 5: sampled (Delta = 1) mean (1 - e^{-0.2})^{-1} (33) (5.516655566 + 0.0j) |
| D29 | PASS | item 5: Cayley cogenerator I - V^*V has rank one (34) ['-7.39557e-32', '0.400413'] |
| D30 | PASS | item 5: Cayley-step mean 4.43125 (35) 4.43125 |
| D31 | PASS | item 5: generator loss -(A + A^*) has rank one (scalar exit) ['0.0', '0.4'] |
| D32 | PASS | item 6: coherent two-zero reset mean (30) (4.61864473922355 + 0.0j) |
| D33 | PASS | item 6: direct integration of S(t) agrees (4.61864473922355 + 0.0j) |
| D34 | PASS | item 6: S(t) from explicit exponential modes matches (30) (max dev) 9.9e-32 |
| D35 | PASS | item 7: b0, b1 orthonormal |
| D36 | PASS | item 7: C_1 matrix (37) |
| D37 | PASS | item 7: -(A_C + A_C^*) = j^* j (38) |
| D38 | PASS | item 7: I - C_1^* C_1 (39) at t = 1 |
| D39 | PASS | item 7: its spectrum (0.00505426, 0.63025175), both positive: finite-time rank one refuted ['0.00505426093', '0.630251755'] |
| D40 | PASS | item 7: det(I - C_t^* C_t) > 0 for t > 0 (sample) |
| D41 | PASS | item 7: S_j(1), m_j(1) (41) 0.379081662320396 0.341173496088356 |
| D42 | PASS | item 7: int m_j = 1, mean 2 |
| D43 | PASS | item 7: stationary density I/2 for the exit reset |
| D44 | PASS | item 7: basis reset b0 for C_t has mean 2 (40) 2.0 |
| D45 | PASS | item 7: basis reset b1 for C_t has mean 6 (40) 6.0 |
| D46 | PASS | item 7: (40) S_Omega and mean for a general density 4.0 |
| D47 | PASS | item 8: jet Gram identity (3) with lowering coefficients 1/2 (max dev) 2.0e-31 |
| D48 | PASS | item 8: closed form (4) for the jet Gram (max dev) 3.9e-31 |

## Findings

- **F1 (T2 confirmed with the notebook's own kernels).** The first-slot Gram `i/(w_j - conj w_i)` of the Riemann
  model at the first three zeros was recomputed directly from the notebook's `y`-picture kernel
  `-i y^{-(1-sigma)/2 - i gamma/2} 1_{y>1}` (thm:model-space-jets) in the variable `X = log y`, agreeing to 2.5e-32
  with the displayed matrix; the loss matrix `-(d_i + conj d_j) G_ij` is identically 1, spectrum (3, 0, 0) (D03–D06).
- **F2 (the Sonine scheme (17)–(21) reproduces independently).** A Nyström discretisation of `T = Q C Q` on 40 and
  64 Gauss–Legendre nodes of (0,1), the anchor solve `(I - T^2) v = r_2`, and the exact moments (21) for the
  `x^{s-1}` term of (18) give `E_*` with `F(2) = 0.0411594371818`, `b = 0.3513948086`, converged to 3e-14 between
  the two discretisations. The structure-phase ratios (22) agree to 8 decimals (D13), have modulus one to 1e-30
  (D14) and are pairwise distinct (min distance 0.016, D15). The raw Gram `G^Son` agrees with the displayed table to
  1.6e-11 relative (D17), is real (D16), the normalised `O` agrees to 4.5e-9 (D18), and the loss spectrum is
  `(-0.0923975213, 0.469315406, 1.12308212)` (D20), reproducing the negative eigenvalue. The extreme eigenvalues of
  `T` are `-0.4710777795, 0.5623175942` (D23), `||T|| < 1`.
- **F3 (`E_*(-1) = 0` is a cancellation, not a value).** At `s = -1` the term `1/(s + t - 1)` of (17) with `t = 2` has a
  pole, which must cancel against the poles of the moments (21) at `s = -1`; a literal evaluation at `s = -1` divides
  by zero. Evaluating at `s = -1 -+ 1e-4` gives `-+1.1597e-5` (D11), i.e. `F` is regular there and `E_*(-1) = 0` holds
  as a limit. The proofs should say "removable" at this point (the same applies to `H` at `s = 0` and the other
  moment poles); this is a presentation point, not an error.
- **F4 (the actual three-zero obstruction is visible numerically).** The cyclic product `N12 N23 N31` of the actual
  Sonine loss matrix is `0.00566 - 0.01843 i`, not real (D22): the analytic argument (15)–(16) is confirmed on the
  computed Gram, independently of the negative loss eigenvalue.
- **F5 (T6, T7 laws all reproduce).** The synthetic pair `0.7 +- 1.5i`: holding law `e^{-0.2 t}` for every modal
  mixture, mean 5, sampled mean `(1 - e^{-0.2})^{-1}`, Cayley-step mean 4.43125 with `I - V^*V` of rank one (D24–D31);
  the coherent two-zero reset mean 4.61864473922355 by (30), by direct integration and from explicit exponential
  modes (D32–D34); the length-two chain: (37)–(41) all reproduce, `I - C_1^* C_1` has two positive eigenvalues
  `(0.00505426, 0.63025175)` (finite-time rank one refuted), basis-reset means 2 and 6, the general law (40)
  (D35–D46); the jet identity (3) and the closed form (4) hold to 1e-31 (D47–D48).
- No formula of the proofs failed to reproduce. Tolerances were set at the displayed precision (8 decimals for
  (22)–(23), 10 significant digits for the raw Gram).
