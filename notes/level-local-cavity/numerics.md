# Numerics lane, level-local-cavity (2026-09-22)

Author: `claude:fable-5.1` (numerics fork; the prover's `checks/` scripts were not read). Script
`scripts/level_local_cavity.py` (mpmath at 40 digits, numpy for the random cores; 6.6 s), output
`outputs/level_local_cavity.txt`. Every displayed formula of `astra-proofs.md` L1–L4 that admits a finite
check was tested: **68 checks, 68 pass, 0 fail.**

## Ledger

| # | Status | Check |
|---|---|---|
| D01 | PASS | q=5: M_q(s) = B(1-s)B(s)^{-1} equals the closed form (1.1) 1.28e-41 |
| D02 | PASS | q=5: diagonal and off-diagonal entries match the prover's table (0.218634648327813 - 0.387681428625362j) (0.282655097128056 - 0.00629331146495754j) |
| D03 | PASS | q=5: det M = (1 - q^{2-2s})/(1 - q^{2s}) = table value (-0.182350078814851 - 0.165963512494691j) |
| D04 | PASS | q=5: functional equation M_q(s) M_q(1-s) = I 4.76e-42 |
| D05 | PASS | q=5: H^T M H = diag(m+, m-) with m+ = 1/(z b_{-a}), m- = 1/(z b_a)  |
| D06 | PASS | q=5: det M^{-1} = z^2 (z^2 - a^2)/(1 - a^2 z^2) (-2.99940394615 + 2.72986783186j) |
| D07 | PASS | q=7: M_q(s) = B(1-s)B(s)^{-1} equals the closed form (1.1) 6.42e-42 |
| D08 | PASS | q=7: diagonal and off-diagonal entries match the prover's table (0.134991110996399 - 0.379918588305854j) (0.238480995379373 - 0.0409197366700405j) |
| D09 | PASS | q=7: det M = (1 - q^{2-2s})/(1 - q^{2s}) = table value (-0.181314294000262 - 0.0830541055837149j) |
| D10 | PASS | q=7: functional equation M_q(s) M_q(1-s) = I 5.3e-42 |
| D11 | PASS | q=7: H^T M H = diag(m+, m-) with m+ = 1/(z b_{-a}), m- = 1/(z b_a)  |
| D12 | PASS | q=7: det M^{-1} = z^2 (z^2 - a^2)/(1 - a^2 z^2) (-4.55874444668 + 2.08821066586j) |
| D13 | PASS | q=5: z M_12(z) -> sqrt q as z -> 0 (simple pole of the off-diagonal) 2.2360679775 |
| D14 | PASS | q=5: z^2 det M(z) -> -q (double pole of det M; (1.3) gives (z^2-q)/(z^2(1-qz^2))) -5.0 |
| D15 | PASS | three random symmetric cores (n=3, two rays): S(z) -> W^*W - I as z -> 0 (regular; no pole) 2.46e-6 |
| D16 | PASS | q=5, t=a: S_t = -Q(z)^{-1}Q(1/z) equals -z(I - tzF)^{-1}(zI - tF) 5.13e-41 |
| D17 | PASS | q=5, t=a: det S_t = p_t/ptilde_t with p_t = z^2(z^2-t^2), ptilde_t = 1 - t^2 z^2  |
| D18 | PASS | q=5, t=sqrt q: S_t = -Q(z)^{-1}Q(1/z) equals -z(I - tzF)^{-1}(zI - tF) 2.07e-41 |
| D19 | PASS | q=5, t=sqrt q: det S_t = p_t/ptilde_t with p_t = z^2(z^2-t^2), ptilde_t = 1 - t^2 z^2  |
| D20 | PASS | q=5: (1.8) M^{-1} = -D S_a D and M = -D S_a^{-1} D  |
| D21 | PASS | q=5: the raw equality M = S_a FAILS, max entry error as in the table 1.50604826933 |
| D22 | PASS | q=5: S_a eigenvalues -z b_a on (1,1) and -z b_{-a} on (1,-1)  |
| D23 | PASS | q=5: (1.10) S_{sqrt q} = -z^2 D M D  |
| D24 | PASS | q=5: bound states of S_{sqrt q} at z = +-a (ptilde = 0), eigenvalue +-(sqrt q + 1/sqrt q), core vector (1,+-1)  |
| D25 | PASS | q=5: S_a has no bound states (ptilde_a zeros at \|z\| = sqrt q > 1); resonances at +-a and two delays  |
| D26 | PASS | q=7, t=a: S_t = -Q(z)^{-1}Q(1/z) equals -z(I - tzF)^{-1}(zI - tF) 4.59e-41 |
| D27 | PASS | q=7, t=a: det S_t = p_t/ptilde_t with p_t = z^2(z^2-t^2), ptilde_t = 1 - t^2 z^2  |
| D28 | PASS | q=7, t=sqrt q: S_t = -Q(z)^{-1}Q(1/z) equals -z(I - tzF)^{-1}(zI - tF) 8.12e-42 |
| D29 | PASS | q=7, t=sqrt q: det S_t = p_t/ptilde_t with p_t = z^2(z^2-t^2), ptilde_t = 1 - t^2 z^2  |
| D30 | PASS | q=7: (1.8) M^{-1} = -D S_a D and M = -D S_a^{-1} D  |
| D31 | PASS | q=7: the raw equality M = S_a FAILS, max entry error as in the table 1.66362344181 |
| D32 | PASS | q=7: S_a eigenvalues -z b_a on (1,1) and -z b_{-a} on (1,-1)  |
| D33 | PASS | q=7: (1.10) S_{sqrt q} = -z^2 D M D  |
| D34 | PASS | q=7: bound states of S_{sqrt q} at z = +-a (ptilde = 0), eigenvalue +-(sqrt q + 1/sqrt q), core vector (1,+-1)  |
| D35 | PASS | q=7: S_a has no bound states (ptilde_a zeros at \|z\| = sqrt q > 1); resonances at +-a and two delays  |
| D36 | PASS | q=5: L_- vanishes at 2 pi k/ell + i/2 and L_+ at (2k+1) pi/ell + i/2, k = -4..4 (height 1/2) 1.04e-40 |
| D37 | PASS | q=5: comb spacing 2 pi/log q 3.90396253166234 |
| D38 | PASS | q=5: (N.1) (L_-/r)(i/2) = -log q/(q-1), L_-'(i/2) = i log q/(q-1) (-0.402359478108525 - 2.92525588005019e-38j) |
| D39 | PASS | q=5: M_q(1) = (q+1)^{-1} all-ones (no pole of M at s = 1)  |
| D40 | PASS | q=7: L_- vanishes at 2 pi k/ell + i/2 and L_+ at (2k+1) pi/ell + i/2, k = -4..4 (height 1/2) 1.51e-41 |
| D41 | PASS | q=7: comb spacing 2 pi/log q 3.22891851416156 |
| D42 | PASS | q=7: (N.1) (L_-/r)(i/2) = -log q/(q-1), L_-'(i/2) = i log q/(q-1) (-0.324318358175886 + 4.82574694524305e-38j) |
| D43 | PASS | q=7: M_q(1) = (q+1)^{-1} all-ones (no pole of M at s = 1)  |
| D44 | PASS | c=0.447214: I - Z_c^* Z_c = J_c^* J_c  |
| D45 | PASS | c=0.447214: spec Z_c = {0, c} (delay mode and resonance)  |
| D46 | PASS | c=0.447214: (1 - c^2) sum c^{2n} = 1  |
| D47 | PASS | c=-0.377964: I - Z_c^* Z_c = J_c^* J_c  |
| D48 | PASS | c=-0.377964: spec Z_c = {0, c} (delay mode and resonance)  |
| D49 | PASS | c=-0.377964: (1 - c^2) sum c^{2n} = 1  |
| D50 | PASS | delay space L^2(0, log 5): eight functions ell^{-1/2} e^{2 pi i j X/ell} have identity Gram 8.13e-45 |
| D51 | PASS | K_A perp A K_B for A = b_{c1}, B = b_{c2} (reproducing-kernel evaluation)  |
| D52 | PASS | A k_{c2} = x k_{c1} + y k_{c2} (partial fractions) checked at a third point  |
| D53 | PASS | (2.13)/(2.15): U_A^* Z_{AB} U_A is lower triangular with diagonal Z_A = c1, Z_B = c2 (0.802371485037 + 3.55188428516e-42j) |
| D54 | PASS | coupling entry equals k_0^B J_A = sqrt(1-\|c1\|^2) sqrt(1-\|c2\|^2) 0.802371485037 |
| D55 | PASS | (2.16): I - Z_{AB}^* Z_{AB} has rank one with norm 1 - \|I(0)\|^2 = 1 - \|c1 c2\|^2 0.9662 |
| D56 | PASS | J_{AB} = conj(B(0)) J_A (+) J_B reproduces the defect operator  |
| D57 | PASS | (3.1) B_35(1-s) B_35(s)^{-1} = M_5(s) (x) M_7(s) 0.0 |
| D58 | PASS | Walsh transform H(x)H diagonalises M_35 with eigenvalues m_{5,e5} m_{7,e7} 0.0 |
| D59 | PASS | det M_35 = (det M_5)^2 (det M_7)^2  |
| D60 | PASS | M_35(s) M_35(1-s) = I  |
| D61 | PASS | residual orders at i/2 of the reduced channels ++, +-, -+, --: 0, 0, 0, 1 ++:0.0001632 +-:0.0001486 -+:0.0001521 --:1.0 |
| D62 | PASS | no integer relation m log 5 = n log 7 with n < 200 (incommensurate periods) 1.98e-5 |
| D63 | PASS | q=5, c=0.44721: (1/i) d/dtau log(u b_c(u)) = ell[2 + 2 sum c^n cos(n ell tau)] at tau = 0.23 5.12583330796659 |
| D64 | PASS | q=5, c=-0.44721: (1/i) d/dtau log(u b_c(u)) = ell[2 + 2 sum c^n cos(n ell tau)] at tau = 0.23 2.24250048770089 |
| D65 | PASS | q=5: phase derivative of L_+ L_- = 4 ell [1 + sum q^{-m} cos(2 m ell tau)] (odd harmonics cancel) 7.36833379566748 |
| D66 | PASS | q=7, c=0.37796: (1/i) d/dtau log(u b_c(u)) = ell[2 + 2 sum c^n cos(n ell tau)] at tau = 0.23 5.56096374464004 |
| D67 | PASS | q=7, c=-0.37796: (1/i) d/dtau log(u b_c(u)) = ell[2 + 2 sum c^n cos(n ell tau)] at tau = 0.23 2.86017537718383 |
| D68 | PASS | q=7: phase derivative of L_+ L_- = 4 ell [1 + sum q^{-m} cos(2 m ell tau)] (odd harmonics cancel) 8.42113912182386 |

## Findings

- **F1 (all prover numbers reproduce).** `M_q(0.7+0.3i)` for `q = 5, 7` from the oldform definition
  `B(1-s)B(s)^{-1}` equals the closed form (1.1) to `1e-35` and the table to `1e-14`; `det M`, the `H`-diagonalisation
  (1.2), `det M^{-1}` (1.3), the functional equation `M(s)M(1-s) = I`, the false-equality errors `1.50604826933` and
  `1.66362344181`, the comb spacings `3.90396253166234` and `3.22891851416156`, the cancelled-point values
  `-0.402359478108525` and `-0.324318358175886`, the residual orders `0, 0, 0, 1` at `N = 35`, and the phase-derivative
  identities at `tau = 0.23` all reproduce.
- **F2 (the fixed-cut obstruction, L1.2, seen numerically).** `z M_12(z) -> sqrt q` and `z^2 det M(z) -> -q` as
  `z -> 0` (poles), while three random symmetric cores with two rays give `S(z) -> W^*W - I` at `z = 1e-6` (regular).
  The brief's `M = -Q^{-1}Q(1/z)` for a symmetric core is impossible, as the prover says.
- **F3 (the two corrected realisations, L1.3–L1.4).** `S_t` from the 04k definition equals `-z(I - tzF)^{-1}(zI - tF)`
  with `det S_t = z^2(z^2 - t^2)/(1 - t^2 z^2)`; `M^{-1} = -D S_a D`, `M = -D S_a^{-1} D`, and `S_{sqrt q} = -z^2 D M D`
  hold to `1e-35`; `S_a` has eigenvalues `-z b_{+-a}` on `(1, +-1)`, no bound states; `S_{sqrt q}` has bound states at
  `z = +-a` with eigenvalue `+-(sqrt q + 1/sqrt q)` and core vector `(1, +-1)` (core equation `(lambda - theta)x = Tx`
  with ray amplitudes `theta^k`).
- **F4 (cascade formulas (2.13)–(2.16) on a two-factor Blaschke model).** With `A = b_{c1}`, `B = b_{c2}`
  (`c1 = 0.3+0.2i`, `c2 = -0.5+0.1i`), `K_A perp A K_B`; the compressed shift on `K_{AB}` in the orthonormal basis
  `(e_A, A e_B)` is lower triangular with diagonal `c1, c2` and coupling `sqrt(1-|c1|^2) sqrt(1-|c2|^2) = k_0^B J_A`;
  `I - Z^*Z` has rank one with norm `1 - |c1 c2|^2` and equals the row `(conj(B(0)) J_A, J_B)`. (My first run
  used a Blaschke factor without the conjugate, `1 - c z`, which is not inner for complex `c`; corrected.)
- **F5 (delay space).** Eight functions `ell^{-1/2} e^{2 pi i j X/ell}` on `(0, log 5)` have identity Gram to `8e-45`:
  the delay model space is infinite-dimensional, as the prover states, one fiber dimension per cell.
- **F6 (a slip in my own expectation, not the prover's).** I first expected `z^2 det M -> 1/q`; the prover's (1.3)
  gives `-q`, which is what the computation shows.

No discrepancy with the proofs was found.
