# Numerics lane: the class-group bond at genus two (notes/genus-two-bond)

Author `claude:fable-5.1` (numerics lane, 2026-09-22), written from `notes/genus-two-bond/astra-proofs.md` without
reading the prover's `checks/` scripts. Script `scripts/genus_two_bond.py` (456 lines, sympy/numpy, exact arithmetic
for every identity: integer point counts, Q(zeta_15) for the L-functions, Q(pi) for the CM field and the
polarisation; floats only for roots, weights and Grams). Output `outputs/genus_two_bond.txt`. Runtime 9 s.

**Ledger: 72 checks, 72 pass, 0 fail.**

## What was recomputed from the curve equation

- `F_{5^k}` arithmetic from the stated moduli (irreducibility verified), brute-force point counts with the single point
  at infinity: `(3, 31, 117, 619)`; Newton gives `P = 1 - 3T + 7T^2 - 15T^3 + 25T^4`, `h = 15`, roots of modulus `sqrt 5`,
  the factorisation over `Q(sqrt 21)`, irreducibility over `Q`.
- Mumford/Cantor arithmetic implemented from scratch: exactly 15 reduced pairs `(u, v)`; `G = [(1,1) - inf]` has order 15,
  its multiples exhaust the classes, all 225 additions agree with `Z/15`, `[(1,4) - inf] = 14G`, and the table rows
  `k = 2, 5, 7` match.
- Effective classes: degree one `{0, 1, 14}`; degree two: all 15 classes, class 0 six times, the others once, from an
  explicit enumeration of the 6 pairs of rational points and the 14 closed points of degree two (Mumford representatives
  built from `F_25` coordinates and from the fibres over `F_5`); `a_0, a_1, a_2 = (1, 3, 20)`, the Perron tail
  `15(5^{n-1} - 1)/4`, and the series of `P/((1-T)(1-5T))`.
- The fourteen `L(T, chi_k)` computed in `Q(zeta_15)` from the class data: `1 + A_k T + 5T^2`, the `A_k` decimals, the
  28 zeros of modulus `5^{-1/2}`, the functional equation `L_k(T) = 5T^2 L_{15-k}(1/(5T))`, the exact integer product
  `P_Y` of degree 32 equal to the displayed factored form, its first coefficients `1 + 9T + 95T^2 + 575T^3 + 3585T^4`,
  `N_1(Y) = 15`, and the three squared factors by character order.
- CM field: `beta^2 - 3beta - 3 = 0`, `delta^2 = 3beta - 17`, the multiplication matrix, the trace matrix with
  determinant `48069 = 21^2 * 109`, `disc Z[pi] = 25 * 48069`, `N(delta^2) = 109`, the reduction mod 2, ordinarity;
  `xi_0 = 1/((2beta - 3)(2pi - beta))` purely imaginary with the displayed alternating unimodular `E_0`; the weights
  `(0.0919994480733, 0.0495772273007)`, the ratio `(25 + 3 sqrt 21)/(2 sqrt 109) = 1.85567957472308`, its square, and
  `|phi_j(xi_0)| = c_j^0` at the four roots; the unit `epsilon` and `(eps_1/eps_2)^2`.
- Theta Fourier weights `(19, 27, 95)/sqrt 15` and `(4, 4A_k, 20)/sqrt 15`, total squared norm 1101; the theta-cyclic
  Gram `[[1101, 282, 195], [282, 126, 47], [195, 47, 39]]` with determinant 254679 and defect of rank 2; the literal cut
  nilpotent.
- E5.3: `rho = alpha/5`, the normalised Cauchy Gram `(4/5)/(1 - conj rho_a rho_b)` with the displayed moduli, positive
  definite, all off-diagonal entries nonzero, Frobenius-normality defect `1.3238593874`.
- E3: on the trivial block invariant Hermitian forms are diagonal (reality leaves two weights); on `H^1(Y)` the 32
  eigenvalues fall into 4 simple and 14 double clusters (real dimension 60 of invariant Hermitian forms; 32 with deck
  invariance; 16 with reality).

## Findings

- F1. No discrepancy with the prover's finite statements. Every displayed number reproduces to the printed precision.
- F2 (implementation note). The `K`-non-normality item is recorded as the prover's argument (`sqrt 109` is not in
  `F = Q(sqrt 21)`), not as an independent factorisation of `f_F` over `Q(pi)`.
- F3 (implementation note). The exact product `P prod L_k` must be formed in `Q(zeta_15)` (reduction modulo `Phi_15`
  after each multiplication); a floating product of the fourteen quadratics accumulates a rounding error of `5e-4` on
  coefficients of size `5^16`, which is harmless for the comparison but not a certificate.

## Ledger

| id | status | check |
|---|---|---|
| D01 | PASS | modulus for F_5^1 irreducible [0, 1] |
| D02 | PASS | modulus for F_5^2 irreducible [1, 1, 1] |
| D03 | PASS | modulus for F_5^3 irreducible [1, 0, 1, 1] |
| D04 | PASS | modulus for F_5^4 irreducible [1, 0, 1, 1, 1] |
| D05 | PASS | point counts N_1..N_4 = (3,31,117,619) [3, 31, 117, 619] |
| D06 | PASS | power sums s_k = (3,-5,9,7) [3, -5, 9, 7] |
| D07 | PASS | P(T) = 1 - 3T + 7T^2 - 15T^3 + 25T^4 25*T**4 - 15*T**3 + 7*T**2 - 3*T + 1 |
| D08 | PASS | chi_F = z^4 f_F reciprocal of P |
| D09 | PASS | h = P(1) = 15 15 |
| D10 | PASS | all four Frobenius roots have modulus sqrt 5 0.0 |
| D11 | PASS | f_F = (z^2 - b1 z + 5)(z^2 - b2 z + 5) over Q(sqrt21) |
| D12 | PASS | f_F irreducible over Q |
| D13 | PASS | number of reduced divisors (Mumford pairs) = 15 15 |
| D14 | PASS | 15 G = 0 and no smaller positive multiple vanishes |
| D15 | PASS | multiples of G exhaust the 15 reduced divisors |
| D16 | PASS | all 225 additions agree with Z/15 |
| D17 | PASS | [(1,4) - inf] = 14 G (inverse of G) |
| D18 | PASS | E1 table rows for k = 2, 5, 7 (u, v) [([1, 3, 1], [1]), ([2, 0, 1], [2, 3]), ([4, 3, 1], [3, 3])] |
| D19 | PASS | rational affine points are (1,1),(1,4) [(1, 1), (1, 4)] |
| D20 | PASS | degree-one effective classes = {0, 1, 14} [0, 1, 14] |
| D21 | PASS | effective degree-two divisors: 6 pairs + 14 closed points = 20 (6, 14) |
| D22 | PASS | every degree-two class effective; class 0 six times, others once {0: 6, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: |
| D23 | PASS | a_0, a_1, a_2 = (1, 3, 20) [1, 3, 20] |
| D24 | PASS | Z(T) = P/((1-T)(1-5T)) gives (1,3,20,90,465,2340,11715,58590) [1, 3, 20, 90, 465, 2340, 11715, 58590] |
| D25 | PASS | a_n = 15(5^{n-1}-1)/4 for n = 3..7 |
| D26 | PASS | special counts (1,3,20) = sum over classes of (5^h0 - 1)/4 at n = 0,1,2 |
| D27 | PASS | L(T, chi_k) = 1 + A_k T + 5 T^2 with A_k = 1 + zeta^k + zeta^-k, all k |
| D28 | PASS | A_k decimals (k = 1..7) and symmetry A_k = A_{15-k} [2.827090915285, 2.338261212718, 1.61803398875, 0.790943073465, 0.0, -0.61803398875, -0.9562952014 |
| D29 | PASS | A_3 = (1+sqrt5)/2, A_6 = (1-sqrt5)/2, A_5 = 0 |
| D30 | PASS | all 28 zeros of the L_k have modulus 5^{-1/2} 5.551115123125783e-17 |
| D31 | PASS | functional equation L_k(T) = 5 T^2 L_{15-k}(1/(5T)) |
| D32 | PASS | P_Y = P prod L_k has integer coefficients (exact in Q(zeta_15)) |
| D33 | PASS | P_Y equals the displayed factored form (degree 32, leading 5^16) |
| D34 | PASS | first coefficients 1 + 9T + 95T^2 + 575T^3 + 3585T^4 |
| D35 | PASS | N_1(Y) = 5 + 1 + 9 = 15 (infinity splits completely) |
| D36 | PASS | order-3 characters give (1+5T^2)^2 |
| D37 | PASS | order-5 characters give (1+T+9T^2+5T^3+25T^4)^2 |
| D38 | PASS | order-15 characters give the octic squared |
| D39 | PASS | L_k(1) = 6 + A_k and L_k(5^{-1/2}) = 2 + A_k/sqrt5 |
| D40 | PASS | pi * pi^{-1} = 1 in K |
| D41 | PASS | beta^2 - 3 beta - 3 = 0 |
| D42 | PASS | delta^2 = 3 beta - 17 |
| D43 | PASS | pi = (beta + delta)/2 |
| D44 | PASS | multiplication-by-pi matrix in power basis has last column (-25,15,-7,3) |
| D45 | PASS | trace matrix on (1,beta,pi,beta pi) as displayed, det 48069 = 21^2 * 109 48069 |
| D46 | PASS | disc Z[pi] = disc f_F = 1201725 = 25 * 48069 1201725 |
| D47 | PASS | N_{F/Q}(delta^2) = 109, not a rational square (no imaginary quadratic subfield) |
| D48 | PASS | K is not normal: 109 is not a square in F = Q(sqrt21) argument: sqrt109 not in F |
| D49 | PASS | f_F mod 2 = z^4+z^3+z^2+z+1 irreducible |
| D50 | PASS | middle coefficient 7 prime to 5 (ordinary) |
| D51 | PASS | xi_0 * (2beta-3)(2pi-beta) = 1 |
| D52 | PASS | xi_0 is purely imaginary: conj(xi_0) = -xi_0 |
| D53 | PASS | E_0 alternating integer unimodular, as displayed [[0, 0, 0, -1], [0, 0, -1, -3], [0, 1, 0, 0], [1, 3, 0, 0]] |
| D54 | PASS | reference weights c_1^0, c_2^0 = (0.0919994480733, 0.0495772273007) (0.09199944807333865, 0.04957722730071405) |
| D55 | PASS | ratio d_2/d_1 = (25+3sqrt21)/(2sqrt109) = 1.85567957472308 1.8556795747230825 |
| D56 | PASS | R_0^2 = (407 + 75 sqrt21)/218 |
| D57 | PASS | |phi_j(xi_0)| = c_j^0: xi_0 at the four roots is purely imaginary with |.| = c_1^0 (twice), c_2^0 (twice) [0.049577227301, 0.049577227301, 0.091999448 |
| D58 | PASS | epsilon = (5+sqrt21)/2 is a unit of norm 1 and (eps_1/eps_2)^2 = (527+115 sqrt21)/2 |
| D59 | PASS | k = 0 theta Fourier coefficients (19, 27, 95)/sqrt15 [np.float64(4.905778905196061), np.float64(6.97137002317335), np.float64(24.528894525980306)] |
| D60 | PASS | k != 0 coefficients (4, 4A_k, 20)/sqrt15 |
| D61 | PASS | total squared norm of theta over degrees 0..2 = 1101 1101.0 |
| D62 | PASS | G_theta as displayed, det 254679 [[1101, 282, 195], [282, 126, 47], [195, 47, 39]] |
| D63 | PASS | defect G - N^t G N as displayed, rank 2 2 |
| D64 | PASS | literal cut on degrees 0..2 is nilpotent: (I (x) N_3)^3 = 0, spectrum {0} |
| D65 | PASS | rho = alpha/5 = (0.379128785 +- 0.237194782 i, -0.079128785 +- 0.440157512 i) |
| D66 | PASS | normalised Cauchy Gram diagonal 1, |G_12| = 0.860 0.8601427276903612 |
| D67 | PASS | Gram entries as displayed (moduli of row 1) |
| D68 | PASS | Cauchy Gram positive definite with all off-diagonal entries nonzero |
| D69 | PASS | Frobenius-normality defect of the Cauchy Gram = 1.3238593874 1.3238593874015678 |
| D70 | PASS | trivial block: invariant Hermitian forms are diagonal (4 real parameters), reality leaves 2 |
| D71 | PASS | F-invariant Hermitian forms on H^1(Y): 32 eigenvalues in 4 + 14 clusters (mult 1 and 2), real dimension 4 + 14*4 = 60 (18, 60) |
| D72 | PASS | with deck-group invariance: diagonal, 32 weights; with reality: 2 + 7*2 = 16 |
