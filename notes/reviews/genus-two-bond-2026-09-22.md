# REFUTE review: the class-group bond at genus two (`notes/genus-two-bond/astra-proofs.md`)

- Reviewer: `claude:fable-5.1` (hostile REFUTE protocol). Author: `codex:gpt-6-astra`. Date: 2026-09-22.
- Files read: `notes/genus-two-bond/astra-brief.md`, `notes/genus-two-bond/astra-proofs.md` (545 lines, all sections),
  `report/sections/04p_gl1_bond.tex` (36-47, 64-81, 88-90, 103-109), `06f_ring_norm_genus_two.tex` (122-130, 227-239),
  `04l_elliptic_cavity_channel.tex` (48-53, 160-175, 233-238), `04o_graded_toys_exits.tex` (127-134),
  `04k_elliptic_cavity_scattering.tex` (290-304), `04r_h_theta_channels.tex` (19-31), `notes/gl1-bond/proofs.md` (18-30, 99-101),
  `notes/ring-norm-tensor/astra-proofs.md` (1011-1039).
- Independent checks: 49 (two scratch scripts written from the text before opening the author's `checks/`; 12 byte-cited
  line ranges read in `refs/src` and the shards). The author's `checks/` were opened only afterwards, to compare outputs.

## Independent checks performed

**Finite data (script 1, exact).** Brute-force point counts of `y^2 = x^5 + x^3 + x^2 - 2` over `F_5, F_25, F_125, F_625`
(field arithmetic by the irreducible moduli listed by the author, irreducibility re-verified), one point at infinity each:
`N = (3, 31, 117, 619)`. Newton: power sums `(3, -5, 9, 7)`, `P(T) = 1 - 3T + 7T^2 - 15T^3 + 25T^4`, `h = P(1) = 15`; the four
roots of `f_F` all have modulus `2.2360679775 = sqrt 5`. Reduced Mumford pairs `(u, v)` with `u | f - v^2`, `deg v < deg u <= 2`:
exactly 15. Cantor addition implemented from scratch: `[(1,1) - inf]` has order exactly 15, its multiples exhaust the 15
reduced divisors, all 225 sums agree with addition mod 15, and `(1,4)` is class 14. Effective counts `a_0, a_1, a_2 = 1, 3, 20`
and `a_n = 15(5^{n-1} - 1)/4` for `n >= 3` give `Z(T)(1-T)(1-5T) = P(T)` exactly (checked to order 8). The fourteen
`L(T, chi_k)` computed from the class data: degree-one coefficients `A_k = 1 + zeta^k + zeta^{-k}` to 12 digits, all
degree-two coefficients exactly `5`. Product `P prod_k L_k`: degree 32, coefficients `1, 9, 95, 575, 3585, 16588, ...`,
leading `5^16`; `N_1(Y) = 6 + 9 = 15`; the author's four-factor integer display matches the product to `1e-8`.

**CM field and metrics (script 2).** `disc Z[pi] = 1201725 = 3^2 5^2 7^2 109`; `beta^2 - 3beta - 3 = 0` and
`delta^2 = 3beta - 17` exactly modulo `f_F`; the Galois group of `f_F` is `D_4` (sympy), so `K` is non-normal with the unique
quadratic subfield `Q(sqrt 21)`, no imaginary quadratic subfield; `N_{F/Q}(delta^2) = 109`. Trace matrix of
`(1, beta, pi, beta pi)` reproduced entry for entry, determinant `48069 = 21^2 * 109`; the maximal-order basis returned by
sympy's `round_two` is `Z[pi] + Z (pi^3 + 2pi^2 + 2pi)/5`, and `(pi^3 + 2pi^2 + 2pi)/5 - 5/pi = pi^2 - pi + 3`, so it is
`Z[pi, 5/pi]` with index 5, as claimed (sympy's printed discriminant `1922` is a sympy defect, contradicted by its own
basis; not the author's error). `d_1 = 2.371947819`, `d_2 = 4.401575121`, `20 - b_1^2 = (25 - 3 sqrt 21)/2`,
`R_0 = d_2/d_1 = 1.85567957472308 = (25 + 3 sqrt 21)/(2 sqrt 109)`, `R_0^2 = (407 + 75 sqrt 21)/218`;
`c^0 = (0.0919994480733, 0.0495772273007)`. `E_0 = Tr(xi_0 x conj y)` on the basis, with `sqrt 21` embedded as `2beta - 3`:
exactly the author's integer antisymmetric matrix, determinant 1; `Im phi(xi_0) > 0` precisely at `alpha_{1,-}` and
`alpha_{2,+}` (the author's `Phi_0`), and `|phi_j(xi_0)| = c_j^0`. The unit `eps = (5 + sqrt 21)/2` has norm 1 and
`eps_1^4 = 526.99810246 = (527 + 115 sqrt 21)/2`. The E4.3 obstruction algebra: `|phi_1 xi|^2 = -phi_1(xi^2)`, so equal
weights force `xi^2 in Q_{<0}`, hence `Q(xi) = Q(sqrt(-d)) subset K`, excluded; correct.

**Cuts and Grams (script 2).** `theta_n(j) = 5^{h^0(jG + nP_0)}` from the E1 table: `G_theta = [[1101, 282, 195], [282, 126, 47],
[195, 47, 39]]`, determinant `254679`, defect `G - N^t G N` of rank 2 with the displayed entries; the total squared norm
1101 equals the Parseval sum of the Fourier weights `(19, 27, 95)/sqrt 15` and `(4, 4A_k, 20)/sqrt 15` (recomputed by hand:
`4 = 5 - 1`, `4A_k = 5A_k - A_k`, `20 = 25 - 5`). The scalar Blaschke model: normalised Gram `(4/5)/(1 - conj(rho_a) rho_b)`
at the four zeros `conj(alpha)/5` of `P` has unit diagonal, is positive definite, has all off-diagonal moduli nonzero
(`0.6725, 0.8474, 0.6993, ...`), and `max |(F/sqrt5)^* G (F/sqrt5) - G| = 1.3238593874015678`.

**Sources.** `refs/src/1012.3223/main.tex:318-332` (reciprocity, product of L-series) and `:1235-1244` (unramified
extension of order `h`, `zeta_{F'}` factorisation, `g_{F'} = (g-1)h + 1`): verbatim. `refs/src/1112.5826/main.tex:534`
(Galois group of the Hilbert class field is `Pic(O)`): verbatim. `refs/src/1701.07742/main.tex:551-555` (ordinary
criterion: middle coefficient prime to `p`) and `:560-618` (Deligne modules): present as stated. `refs/src/1012.3513/hecke.tex:992`
(cusp count `h_X d_x`) and `refs/src/2603.26443/final_draft.tex:884-892` (cusps and `Pic(R)`): present. All shard line ranges
cited (04p, 04l, 04o, 04k, 04r, 06f, gl1-bond, ring-norm-tensor) contain what is attributed to them.

## Verdicts

**E1 — VALID.** Every number reproduced independently (counts, `P`, `h`, the 15 reduced divisors, the generator of order 15,
closure of all 225 additions, the theta set `{0, 1, 14}`, `h^0` in degrees 0-2, `a_n`, the identity `Z (1-T)(1-5T) = P`).
The algebraic modulus argument (`b_j^2 < 20`) is correct and does not use `asm:weil-curves`.

**E2 — VALID.** The fourteen polynomials `1 + A_k T + 5T^2`, the degree-two coefficient `5`, the vanishing beyond degree
`2g - 2`, the functional-equation constant `chi(kappa)` with `kappa = [K_C - 2P_0] = 0` (checked: `5T^2 L_{15-k}(1/(5T)) = L_k(T)`),
the genus `16` of the pointed class-field cover, the degree-32 product with its integer factorisation and `N_1(Y) = 15`
all check. The correction to `notes/gl1-bond/proofs.md:99-101` (a single nontrivial `L`-factor is the numerator quotient
only for a degree-two cover; in general the quotient is the product over the nontrivial characters) is right. The
cohomological identification is stated with the standard inputs (rank-one lisse sheaves, trace formula) correctly marked
not byte-cited; E2.3's refusal to call it a Hilbert-space isomorphism (dimensions 15 versus 32) is correct.

**E3 — VALID.** The direct model `Z' = rU` on 32 modes is a literal application of `thm:frobenius-channel-expander`
(04o:127-134), and the distinction from that theorem's D2 convention `U^2 ~ (Frob/sqrt q) (x) 1_2` (64 modes) is read
correctly from line 133 and 04l:233-238. The invariant-metric equation `(conj(mu_a) mu_b - 1) H_ab = 0`, the diagonal
cone on the trivial block, the reality condition `H(cx, cy) = conj H(x, y)` giving `diag(h_1, h_1, h_2, h_2)` (two
parameters, one ratio), and the point that 04l's single ray came from symmetries acting transitively on the D2 modes
(04l:160-164) which have no genus-two counterpart, are all correct. The `Q_l` remark (no distinguished conjugation) is
right and sharpens the brief.

**E4 — VALID.** The field identities, the discriminant `48069`, maximality of `Z[pi, 5/pi]` (relative discriminant of norm
109 squarefree; independently confirmed by the index-5 maximal-order basis), the absence of an imaginary quadratic
subfield (D_4 Galois group; `N(delta^2) = 109` not a square), the Riemann-form description with weights `|phi_j(xi)|`, the
reference lattice `(O_K, xi_0 = 1/(sqrt 21 delta))` with `D_K = (sqrt 21 delta)` (norm `441 * 109 = 48069`), the unimodular
integer `E_0`, the CM type `{alpha_{1,-}, alpha_{2,+}}`, the ratio `R_0` and its square in `F`, the obstruction that no
rational `K`-module marking gives equal weights, and the unit-rescaling argument (`eps_1^4`) all reproduce. The OPEN verdict
on the bond-to-`H^1` comparison is the honest one: the brief supplied no map, and E4.4 shows the theta Fourier data
give one three-vector per character, not four eigenline weights. The Hodge reading is correctly made conditional on
`asm:cm-hodge-type` and `asm:cm-polarised-lift`.

**E5 — VALID.** The literal cut `n <= 2` is a multiplicity-15 backward shift (infinite-dimensional coisometry); the
truncation `0 <= n <= 2` is `I_15 (x) N_3`, nilpotent, characteristic function `z^3 I_15`, determinant `z^45`; the theta-cyclic
Gram, its determinant and its rank-two defect are exactly as displayed; the replacement `B = P/f_F` has the Cauchy Gram
`(4/5)/(1 - conj(rho_a) rho_b)` with nonzero off-diagonals and normality defect `1.3238593874`; the rank obstruction (defect
`(1 - r^2) I_d` versus a scalar exit) is 04l:171-175 verbatim. The brief's E5 is refuted as stated.

**E6 — VALID.** The proved content is `prop:siegel-constant-term` (04r:19-31), quoted correctly with the weighted
involution at fixed `y`; the Riemann-Roch involution `(j, n) -> (-j, 2 - n)` sends `k` to `15 - k`; the cusp count 15 is
Lorscheid's `h_X d_x` with `d_x = 1`; the H-CLASS block form and its eigenvalues `+- sqrt(m_k m_{15-k})` follow from
04k:290-304 as a conditional statement. The fold is correctly left open.

## Verdict lines

VERDICT E1: VALID
VERDICT E2a: VALID
VERDICT E2b: VALID
VERDICT E3a: VALID
VERDICT E3b: VALID
VERDICT E4a: VALID
VERDICT E4b: VALID
VERDICT E4c: VALID
VERDICT E5: VALID
VERDICT E6: VALID

## MINOR fixes (wording only; no verdict affected)

1. E4.1: add that `Z[pi]` has index exactly 5 in `O_K` with the explicit extra generator `(pi^3 + 2pi^2 + 2pi)/5 = 5/pi + pi^2 - pi + 3`,
   which makes the maximality statement checkable by a reader without the relative-discriminant argument.
2. E3.3: state that "deck-group invariant" is an added hypothesis for the block-diagonal description (the text says so,
   but the ledger row for E3 should carry it).
3. E5.3: fix one ordering convention for `<k_a, k_b>` (the Hermitian conjugate of the displayed matrix is equally valid; say
   which slot is linear, as 04s does).
4. "Progress" section duplicates the ledger; harmless.

## Assessment

The lane's corrected statements are sound, and the finite data are now certified twice. What the round settles: the
genus-two class-group bond has exact finite data (E1), its Fourier decomposition labels `H^1` of the genus-16 pointed
Hilbert class cover with fourteen quadratic `L`-factors (E2), the trivial Frobenius block has a genuinely non-vacuous
metric cone with one free ratio (E3), and the CM reference lattice has a computable, non-unit ratio `(25 + 3 sqrt 21)/(2 sqrt 109)`
with the theorem that no rational `K`-module marking can make the two Hodge weights equal (E4). What it refutes from the
brief: the degree cut as an exit model for `H^1` (E5), the "two candidate answers" framing (E4.5), and "normalised by
the lattice" as a normalisation (E4.5). What remains open, and is correctly labelled so: a bond-intrinsic comparison map
to geometric `H^1` (without which "the symmetric ray is the Hodge metric" has no meaning at genus two), and the genus-two
H-CLASS fold. No claim is INVALID.
