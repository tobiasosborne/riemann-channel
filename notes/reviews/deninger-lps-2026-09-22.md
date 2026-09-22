# REFUTE review: the (13, 17; 5) LPS square complex as a Deninger finite model (lane `notes/deninger-lps`)

Reviewer: `claude:fable-5.1` (hostile REFUTE protocol). Author under review: `codex:gpt-6-astra`
(`notes/deninger-lps/astra-proofs.md`, 412 lines, B1–B7). Date 2026-09-22. Inputs read: the brief
(`astra-brief.md`), the worked example (`src/lps-deninger-worked-example.md`), the blind numerics ledger
(`numerics.md`, 50 checks, findings F1–F5), the proofs. Independent checks: 40 (four scratch scripts written from
the text before reading the author's `checks/astra_check.py`, reusing only the blind lane's construction of the
complex in `scripts/lps_square_complex.py`; plus one grep for the source-locator correction). The author's script
was not audited line by line; its outputs were compared with mine.

## Independent checks (all pass)

Reversal halves and the bipartite sign (B3). With `S = eps(tail)` on directed horizontal edges: `S T_1 = -T_1 S`,
`S R = -R S`, `S` preserves the directed new space; traces on the reversal sectors of the new space `-18` (`R = +1`)
and `+18` (`R = -1`); `Tr T = 18`. Agrees with the blind lane's F1 and refutes the brief's "same action on both
halves".

Metric cone (B4). Distinct eigenvalues of `T` on `K`: 48; `sum m_a^2 = 16539` exactly (from the clustered
numerical spectrum, which reproduces the Section 13 table). On the `a = 7` eigenspace (multiplicity 4): the eight
vectors `(alpha v, v)`, `(conj(alpha) v, v)` are `F_1`-eigenvectors; a generic Hermitian `4 x 4` block on the
`alpha`-space, with its conjugate on the `conj(alpha)`-space, satisfies `Lambda^* H Lambda = 17 H`, transports to a
real symmetric `F_1^T H F_1 = 17 H` form, and a cross block `alpha/conj(alpha)` is not invariant. So the cone is
block-diagonal Hermitian per repeated eigenvalue, real dimension `m_a^2` per block, total 16539; "one scalar per
copy" is indeed refuted.

Quarter-turn (B4). With the matrix square root `R = (17 - T^2/4)^{1/2}`: `J^2 = -1`, `J F_1 = F_1 J`,
`J^T Omega J = Omega`, `Omega J` symmetric positive definite (least eigenvalue 0.098), `Omega J = G diag(R^{-1}, R^{-1})`
to `1e-8`, `|Omega J - G| = 324.5`: the brief's `G = Omega J` is refuted, the author's `Omega J = G/r(T)` holds, and
it agrees with the worked example's own display. Raw weights `e_alpha^* G e_alpha = 2 r_a^2 = 9.5` and
`e_alpha^* (Omega J) e_alpha = 2 r_a = 4.3589` at `a = 7`.

Traces (B6). `Tr T^2 = 13284`, `Tr F_1^2 = Tr T^2 - 34 * 721 = -11230`, `290 + Tr F_1^2 = -10940 < 0`,
`N_2 = 11520`; `F_1^* F_1 != 17 I` (`|F_1^* F_1 - 17 I| = 7824.5`).

Hecke at `17^2`. 307 primary quaternions of norm 289; `A_17^2 - 17 I = A_289` on vertex functions;
`A_17^2 - 18 I` has entries up to 10 (the 120-vertex quotient has many 4-cycles), and `A_289 - I = A_17^2 - 18 I`
counts length-two walks; the author's `A_distance2` statement is explicitly "on the tree" and is correct there.

`K` as a `PGL_2(F_5)`-module (B3). Character of `K` under the left action on the seven conjugacy classes:
`(1, 1, 1, 1, 1, 1, 721)` = `6 chi_Reg + 1`; isotypic multiplicities `6 d_sigma + delta_{sigma,1}` =
`{7, 6, 24, 24, 30, 30, 36}`; the blind lane's per-eigenvalue tables sum to `dim 1: 13 = 7 + 6`, `dim 4: 48`,
`dim 5: 60`, `dim 6: 36`, weighted sum 721. Consistent.

Weil odd block (B5). Rebuilt `Sigma_- = 18 Phi_-` for `(13; 17)` from `scripts/weil_lps.py` (intertwiner error
`7e-15`): spectrum `18 (1), 3 (8), -3 (3), -5 (6), +-5.55485 (3 each), +-1.77302 (3 each), 3.56155 (3), -0.56155 (3)`,
exactly the root multiset of `(x-18)(x-3)^8(x+3)^3(x+5)^6(x^2-3x-2)^3(x^4-34x^2+97)^3`. Its common roots with
`spec T` are `3, -3, -5` with multiplicities `min(8,44) = 8`, `min(3,6) = 3`, `min(6,12) = 6`, and the quadratic
and quartic roots are at distance `>= 0.019` from every eigenvalue of `T`: the gcd `(x-3)^8(x+3)^3(x+5)^6` and
the nondivisibility are confirmed. Character of `End(W_-)` over `SL_2(F_13)` by class: `36` (centre), `0` (split
regular), `1` (nonsplit regular), `{1.69722, 5.30278} = (7 -+ sqrt 13)/2` (unipotent), as stated; multiplicity of
the finite Steinberg (dimension 13) in `End(W_-)`: `0.000000`; of the trivial representation: `1`;
`<End W_-, End W_-> = 4`, so `End(W_-)` is multiplicity-free with four constituents, and with the trivial one
present and Steinberg absent the only dimension split of `35` from `{7, 7, 12, 12, 12, 14, 14}` is `7 + 14 + 14`,
confirming (B5.2).

Source locator. The labels `thm:graded-harrow`, `thm:graded-qihara-bass`, `cor:graded-band-circle` are in
`report/sections/03c_graded_ramanujan.tex` (lines 150, 92, 111), not in `05*`: the author's correction is right and
the brief was wrong.

## Verdicts by item

**B1 — VALID.** The Hamilton quaternions are a division algebra over `Q` (norm form anisotropic), so the brief's
`Gamma < PGL_2(Q)` was wrong and the author's `PB^x(Q)` with the two local splittings is right; the primary
(congruence) subgroup is the Mozes–Rattaggi lattice; `F_r x F_s` on `T_2r x T_2s` is a correct counterexample to a
general vanishing statement; the Betti certificate (rank mod 101 of `B_2 B_2^t` plus `B_1 B_2 = 0`) is the same
one the blind lane used and is sound. Statements of Mozes (1995) and Rattaggi (2004) are given with the right
hypotheses (`p, l = 1 mod 4`).

**B2 — VALID.** `K = H_1` of the horizontal colour graph, with the corrected quotient (the stabiliser
`Lambda_13(5)` of a vertex of the 17-tree, not `Gamma(5)`); the correspondence `p_* r^*` through the graph of
directed vertical edges is exactly the worked example's `T_1`; the telescoping identity `T_1 D = D A_17` and the
characteristic-polynomial quotient are correct and were verified numerically by the blind lane (D19, D38).

**B3 — VALID.** The adelic description with `U_2 = image(1 + 2 O_2)` is required: with maximal level at 2 the
12 projective Hurwitz units would identify points; the count `12 x 120 / 12 = 120` is right and the
norm-Euclidean class-number-one argument is standard. The old/new dimensions 238/1442 and the two-dimensional
kernel `(1, -1), (eps, eps)` are verified; the sign twist `S` exchanging the halves and reversing `a_17` is
verified (it is the quadratic character `(./5)` composed with the reduced norm, unramified at 13 and 17 with
`(13/5) = (17/5) = -1`, which is why it twists `St` at 13 and negates `a_17`). Casselman's description of the
Iwahori-fixed line of `St (x) chi` with reversal eigenvalue `-chi(13)` is stated correctly (I can verify the
consequence, `w_p = -a_p` for `p || N`, against the standard elliptic-curve dictionary, and the antisymmetric
sector `R = -1` then selects untwisted `St`; I cannot byte-verify the sources). The multiplicity formula
`m(pi) = dim pi_2^{U_2} dim pi_5^{U_5}` is the correct double-coset count given multiplicity one; the module
identity `K_C = 6 Reg + 1` and its isotypic multiplicities are verified. The refutations of the brief (eight
irreducible degrees; "integer `a_17` means rational newform"; eigenvalue `+5`) are all correct.

**B4a — VALID.** The spectral identification `(K (+) K, F_1) = (+) (V_pi, Frob_17)^{m(pi)}` over an algebraically
closed field follows from B3 plus the Eichler–Shimura congruence relation, stated with its correct authors and
scope (weight two, no Deligne); the distinction "one-operator semisimple system, not a Hodge structure or a
lattice" is exactly right.

**B4b — VALID.** The refutation of the brief's "Omega_B = cup, G = Petersson" is correct as a matter of logic:
Jacquet–Langlands and Eichler–Shimura supply no comparison map from graph cycles to Betti cycles and no Hodge
action of Frobenius; the author's OPEN with the conditional certificate `G_P` is the honest status. The two
finite facts that make the brief's "symmetric ray" claim fail were verified: the cone dimension 16539 (not
`1 + number of eigenvalues`) and `Omega J = G/r(T) != G`.

**B5 — VALID.** Refutation of the identification: the notebook's `(13; 17)` channel lives at level 13 on
`PSL_2(F_13)` with Fourier selection by `End(W_-) = 1 + 7 + 14 + 14` (split principal-series types, no
Steinberg), the worked model at level 5 with `St` at 13; the exact degree-36 polynomial, its gcd with `chi_T`,
and the nondivisibility are reproduced; the Harrow-versus-old/new and the zeta-sign distinctions are correct
(the ungraded script's Bass roots are poles). The sharpened statement (same quaternionic Hecke family at 17, two
different local selection rules, formula (B5.1)) is sound.

**B6 — VALID.** The CP obstructions are elementary and verified: `Tr E^2 = 290 - 11230 < 0` rules out the exact
sector prescription, and `Ad(-U) = Ad(U)` kills scalar signs, so the brief's signed-walk Kraus candidate fails.
The letter-register construction `A_{j,i} = U_i (x) |j><i|` is a genuine CP realization of the block Hashimoto
map of `weil_lps_hashimoto.py` (its restriction to the diagonal-register algebra is exactly that block map); the
"OPEN" for a realization of the exact net divisor with cancelling modes is correctly left open (the necessary
inequality `N_n >= 0` holds for all `n`, so no negativity refutation is available). The Hilbert–Schmidt remark
(`F_1^* F_1 != 17 I`) is verified.

**B7 — VALID.** `Z log p + Z log q` is dense in `R` (`log p / log q` irrational), so the quotient is
non-Hausdorff; the brief's "solenoid" was wrong. The rest is a fair statement of what does and does not follow.

## Verdict lines

VERDICT B1: VALID
VERDICT B2: VALID
VERDICT B3: VALID
VERDICT B4a: VALID
VERDICT B4b: VALID
VERDICT B5: VALID
VERDICT B6: VALID
VERDICT B7: VALID

## MINOR fixes (wording only; no verdict depends on them)

1. B3, "elementary class-set justification": say explicitly that the diagonal action of the 12 projective
   Hurwitz units on `(O/2O)^x x PGL_2(F_5)` is free and transitive on the first factor, so the quotient is in
   bijection with `PGL_2(F_5)`, and that the Cayley identification then uses the primary representatives (the
   reader otherwise has to reconstruct the count `12 * 120 / 12`).
2. B3, the reversal sign: add the one-line dictionary "`R` on Iwahori-fixed vectors is the Atkin–Lehner element
   at 13; for an elliptic curve with `13 || N` its eigenvalue is `-a_13`, so `R = -1` is split multiplicative
   reduction (`a_13 = +1`, untwisted `St`)", which makes the selection rule checkable against tables.
3. Numerical checklist, `T_{17^2}`: keep "on the tree" attached to `A_distance2`; on the 120-vertex quotient
   `A_17^2 - 18 I` has entries up to 10 and is the length-two walk count, not a 0/1 adjacency.
4. B5, (B5.2): note that the multiplicity-free decomposition with the trivial constituent present and the
   Steinberg absent forces `7 + 14 + 14` from the dimension list of `PSL_2(F_13)`, which gives the reader a
   dimension-only check of the displayed character values.

## Assessment

The corrected statements are sound. Of the brief's original claims the following are now settled negatively, by
finite computation or by exact algebra: the two reversal halves are not isomorphic Hecke modules (sign twist,
`-spec T`); the invariant-metric cone is block-Hermitian of real dimension 16539, not one scalar per copy;
`Omega J` is `G/r(T)`, not `G`; the notebook's Weil–LPS `(13; 17)` channel is not the same object as the square
complex's transverse operator (different level, different local selection, non-dividing Bass factors, Steinberg
absent from `End(W_-)`); and no direct or signed-Kraus CP realization of the exact `N_n` exists. What survives, and
is proved: `K` is graph `H^1` with `T = T_17` (B2), the spectrum is a weight-two Hecke spectrum with the explicit
local conditions (B3), the Bass doubling is spectrally Frobenius at 17 (B4a). The brief's central geometric hope,
that the doubled pairing and metric are the cup product and Petersson metric of a modular curve transported by
Jacquet–Langlands, is correctly downgraded to OPEN: it needs a comparison map that neither theorem supplies. The
author's 33-row correction ledger is justified in every row I could test.
