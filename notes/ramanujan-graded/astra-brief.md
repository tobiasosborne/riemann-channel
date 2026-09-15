# Brief: the Ramanujan property for graded transfer channels (MPS, cMPS, Lindbladians). Prove or correct D1-D14.

You are the prover lane of a research notebook (repo root = working directory). Read, in this order:
`notes/ramanujan-graded/definition.md` (the orchestrator's draft: the definition and the drafted
statements D1-D14; this is your main input), then `HANDOFF.md` sections "CENTRAL PRIORITY", "Back to
basics", "The zeta conditions factor by factor"; then the lab-book shards
`report/sections/02_definitions.tex` (def:rh-analogue, def:quantum-expander, def:ramanujan-channel,
def:quantum-hashimoto), `02f_definitions_graded_cmps.tex` and `04f_cmps_twisted_supertrace.tex`
(graded cMPS, twisted ring norm = supertrace, ring zeta 1/sdet), `03b_graded_permutation.tex`
(letters, the sign lives in the even-odd coherences, prop:parity-jump-uniform-shift),
`08_quantum_ihara_general.tex` (thm:qihara-general, obs:rh-iff-ramanujan-channel),
`08b_weil_positivity.tex` and `08c_weil_positivity_continuous.tex` (adjoint pairing = reality,
inverse pairing = FE, thm:cmps-ring-norms, prop:hp-inner-product-discrete),
`09b_selberg_dictionary.tex` and `09c_selberg_tower_cusp.tex` (prop:quantum-lindblad-tensor,
conj:quantum-lindblad-gap, the continuous dictionary), `05_weil_lps_channels.tex` (Weil-LPS
channels), `09_prior_art.tex` (cit:harrow-transfer). Sources under `refs/src/`: Hastings 0706.0556
(sd10.tex; the section "Lower Bounds" has the quantum Alon-Boppana argument, lines ~233-310),
Harrow 0709.1142 (main.tex), Dyatlov-Zworski 1306.4203 (zeta.tex, eq:Rue and the Lefschetz identity
near line 526). Numerics you can run and extend: `scripts/graded_ramanujan.py` (79 checks; output
in `outputs/graded_ramanujan.txt`), `scripts/weil_lps.py`, `scripts/zeta_conditions.py`. python3 with
numpy, scipy, sympy, mpmath. Write any scripts to `notes/ramanujan-graded/finite/` (you own it) and
the report to `notes/ramanujan-graded/astra-proofs.md`. Do not modify anything else.

## Task

For each of D1-D14 in `definition.md`: state it precisely (fix conventions, declare every hypothesis
as H-<name> with a one-line justification of whether it is standard), then PROVE it, or CORRECT it
(give the true statement and prove that), or REFUTE it (explicit counterexample, verified by a
script). Keep a correction ledger (one row per change to the orchestrator's draft: what was claimed,
what is true, why). Where a statement is a definition rather than a theorem (the definition of RH /
FE / Ramanujan / manifest, the trivial set, graded quantum expander), say whether it is well posed,
whether the cases in the notebook (graphs and Weil-LPS channels, the 06h elliptic tensor, the
Artin-Schreier super-transfer of 06b, the Riemann graded generator of 04b, the Selberg side of 09c)
satisfy it with the trivial set as stated, and propose the minimal change if not.

Priorities, in order (spend the effort here):
1. D3, D4, D6 (graded quantum Ihara-Bass; band iff circle sector by sector; graded Harrow with the
   character formulas and the Artin factorisation). These carry the paper's main new example: a
   quantum expander whose parity-closed ring zeta has zeros on the critical circle.
2. D8 (graded Chernoff, "odd letters are jumps"): a precise theorem with norm hypotheses.
3. D11 and D12 (continuous Harrow, ungraded and graded): the Fell-absorption/tempered argument for the
   gap 1/2; Clifford theory for PGL_2(R) vs PSL_2(R); the exact decompositions D_k^+ (x) D_k^+ and
   D_k^+ (x) D_k^-, the -T eigenvalues on K-types in the shard-09b normalisation (-T = 2 s(1-s) +
   m^2/2 on a constituent with parameter s and K-type m; check this normalisation against
   prop:quantum-lindblad-tensor and correct it if needed), the matrix-coefficient exponents along
   a_t, and the character statement (iii). Also the Repka threshold: for the complementary series
   pi_s of SL_2(R), when does pi_s (x) pi_s contain a complementary series? State from your knowledge
   with the reference and mark it H-repka; do not invent a citation.
4. D5 (graded Alon-Boppana), D13 (general C^{1|1} formula), D1, D2, D7, D9, D14 (short).
5. D10: give a precise definition of the divisor via correlation functions of regular data for a
   strongly continuous semigroup with a Gamma-grading, and state what has to be assumed for it to
   be well defined; relate to def:distributional-trace of shard 02c. No theorem expected beyond
   "well defined under H-*".

## Conventions (must match the notebook)

- Bond C^{D_+|D_-}, parity P = 1 (+) (-1). Letters A_s homogeneous, P A_s P = eps_s A_s. Doubled
  transfer E = sum_s A_s (x) conj(A_s) acting on vec(X) as X -> sum_s A_s X A_s^+. Gamma = P (x) P
  = Ad(P). Even sector = block-diagonal, odd = block-off-diagonal. Ring norms N_1(n) = Tr E^n,
  N_P(n) = str E^n = Tr(Gamma E^n) = sum_w |Tr(P A_w)|^2. Graded ring zeta Z_P(u) =
  exp(sum N_P(n) u^n/n) = det(1 - u E_1)/det(1 - u E_0). Divisor nu = m_0 - m_1.
- Counting normalisation: q = rho(E). Hastings band in adjacency units: |lambda| <= 2 sqrt(D-1) for
  Sigma = D Phi, D unitary letters; lambda_H = 2 sqrt(D-1)/D in channel units.
- Hashimoto operator (def:quantum-hashimoto): T on B(H) (x) C^D, T(X (x) e_i) = sum_{j != ibar}
  Ad(U_i) X (x) e_j, reversal ibar fixed-point-free with U_ibar = U_i^+. Quantum Ihara-Bass
  (thm:qihara-general, unitary case): det(1 - uT) = (1-u^2)^{n^2(D-2)/2} det(1 - u Sigma + (D-1)u^2)
  on an n-dimensional bond.
- cMPS: T = Q (x) 1 + 1 (x) conj Q + sum_a R_a (x) conj R_a, N_P(L) = str e^{LT}, Z_P(z) = 1/sdet(z - T).
- Selberg / SL_2(R) normalisation: shard 09b (Casimir with principal series parameter s = 1/2 + ir,
  Laplace eigenvalue s(1-s); the two-jump Lindbladian is (1/2)(B_H^2 + B_E^2) = 2 Cas + (1/2) B_W^2).

## Deliverable format

`notes/ramanujan-graded/astra-proofs.md`: for each D-item a block "Statement (as proved) /
Hypotheses H-* / Proof / Status: PROVED | CORRECTED (with the ledger row) | REFUTED (with script) |
OPEN (with what is missing)". Then the correction ledger as a table. Then a section "Definitions:
verdict" (well posed? which notebook cases satisfy them? proposed changes). Then "Numerical
checks" listing every script you wrote with its printed tally. Proofs in Lamport style where they are
more than a few lines (numbered steps, each with its justification). Do not overwrite
`definition.md`. Print the final tally of PROVED/CORRECTED/REFUTED/OPEN at the end of the report.
