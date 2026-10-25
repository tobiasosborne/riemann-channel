# Lane RA: REFUTE review of lanes A (`notes/astra-2026-10-23/average/`) and C (`notes/astra-2026-10-23/canonical/`)

You are `codex:gpt-6-astra`, acting as the adversarial reviewer. Read `notes/astra-2026-10-25/brief.md` first (binding; its REFUTE
review protocol is your output format), then `notes/astra-2026-10-23/brief.md`, then both lanes in full (`astra-brief.md`,
`astra-proofs.md`, `progress.txt`, `checks/` with saved outputs). Background: `notes/adelic-gkp/ff-dirichlet.md`,
`notes/adelic-gkp/graph-super.md` §9, `notes/adelic-gkp/graph-ihara.md` §8–§9, `notes/adelic-gkp/data-ladder.md`, tutorial Section 6
(`notes/adelic-gkp/tutorial/page.html`: Ω as the Casoratian). Write only in `notes/astra-2026-10-25/review-average-canonical/`.
(Lane A2 of this round, `notes/astra-2026-10-25/hhalf/`, attacks H-half for all (q, g); do not duplicate; you review what lane A
claimed PROVED.)

## Lane A items (first half)

A1. `prop:sf-quadratic-average-exact` (the Euler-product formula (1)–(5) for the hyperelliptic average): rederive (1) from quadratic
    reciprocity in F_q[t] — check the sign ε^{d·deg h} and the case h = 1; check (2) and (5); recompute L̄_{3,2} = 1 + (62/27)u² + 9u⁴
    and L̄_{7,3} by brute-force enumeration in your own code (all squarefree D of degree 5 resp. 7, L(u, χ_D) by direct character
    sums, not by the functional equation).
A2. `lem:reciprocal-half-stability` (H-half + reciprocity ⟹ all roots on |w| = 1): is this a correct lemma? (Eneström–Kakeya-type
    statements need care: the lane says the EK premise fails for g ≥ 2 and uses a different argument — which? Check it on a
    self-inversive polynomial with nonnegative decreasing first half that has a root OFF the circle, if one exists — search
    degree 4–8 with small integer coefficients.)
A3. `thm:hyperelliptic-average-low-genus` (A1 for g ≤ 3, all odd q): the g = 3 factorisation B = (1 + w)(1 + (b₁ − 1)w + w²) and
    0 < b₁ < 1 — verify the inequality proof (the bracket bound and the induction).
A4. `obs:geometric-level-average-dichotomy` REFUTED (cubic isotypic average 1 + u at (q, d) = (7, 3)): recompute by enumeration
    (cubic characters mod f of degree 3 over F_7, all f; which "isotypic" average exactly — one character per f? both? completed or raw?).
A5. `prop:ff-irreducible-level-average` ((10)–(12), the Ramanujan-sum formula): check (12) on (q, d) = (3, 2) and (5, 2).

## Lane C items (second half)

C1. `prop:graph-trace-schur-support` (retained Ihara trace positivity ⟺ Ramanujan; Schur length = distinct spectral support):
    the Toeplitz matrix of which moments exactly (the normalised traces tr(A/√q)^k? the Hashimoto traces?), with the trivial
    eigenvalue removed how? Recompute for K₄ (α₀ = −√2/4, α₁ = −1) and for one prism (m = 16, first failure at index 13, value
    43707967/3998190) by your own Schur algorithm in exact arithmetic.
C2. `prop:casoratian-szego-conformal` (the graph Abel identity and the Szegő determinant identity share a two-dimensional
    conformal alternating form; the raw Szegő multiplier includes z): is this a theorem or a reformulation? Give the sharpest
    true statement; check against tutorial Section 6's Casoratian.
C3. `prop:ff-schur-logtrace` (completed character log-traces give a Toeplitz/Schur RH criterion; termination at distinct roots):
    recompute the q = 5 quartic example (Λ = 1 + (−2 + i)u + (3 − 4i)u², α₀ = (2 + i)/(2√5), |α₀|² = 1/4).
C4. `prop:ff-prime-aggregate-insufficient` (exact quadratic counterexamples): verify them.
C5. `prop:zeta-schur-purepoint-product` (PROVED-conditional H-RH: infinite support, Szegő product zero) and
    `num:zeta-prime-schur-probes` (c₀ = .0343767341909677, α₀ = −.821215963567708 at p = 2, L = .4, τ = .1): the zeta-rung
    computations use primes, pole and archimedean factor only (game rule 3) — audit the scripts for any zero input; recompute c₀, c₁.
C6. The lane's headline "Schur coordinates are not the ladder's finite-rank-per-mode datum" and its proposed annotations
    (`graph-ihara.md` §8/§9 "Ω is the Casoratian, Q = ½Ω(M − qM⁻¹)", `data-ladder.md`): AGREE / AGREE-WITH-CHANGE / DISAGREE.

## Output

`astra-proofs.md` (the review) as in the protocol; `## Verdict lines` with the lanes' candidate ids; `## Numerical checks for the
blind lane`; `## What this changes in the notebook`. `progress.txt`: A1 … A5, C1 … C6, NUM.
