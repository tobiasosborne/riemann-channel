# Lane RG: REFUTE review of lanes H (`notes/astra-2026-10-23/haar/`) and K (`notes/astra-2026-10-23/krein/`) — gauge fields on graphs

You are `codex:gpt-6-astra`, acting as the adversarial reviewer. Read `notes/astra-2026-10-25/brief.md` first (binding; its REFUTE
review protocol is your output format), then `notes/astra-2026-10-23/brief.md`, then both lanes in full (`astra-brief.md`,
`astra-proofs.md`, `progress.txt`, `checks/`). Background: `notes/adelic-gkp/gauge-groups.md` (the SU(1,1) and U(d)/SU(2)
paragraphs both lanes want rewritten), `notes/adelic-gkp/graph-super.md` §6, `notes/adelic-gkp/zn-flux.md` §4,
`notes/adelic-gkp/lattice-tower.md` §5. Literature from memory: Hall–Puder–Sawin, "Ramanujan coverings of graphs" (Adv. Math.
2018: the expected characteristic polynomial of a random d-cover is the d-matching polynomial; real-rooted, roots in the band;
one-sided existence of Ramanujan covers); Heilmann–Lieb (real-rootedness of matching polynomials); Godsil–Gutman; Marcus–Spielman–
Srivastava (interlacing families); Weingarten calculus for U(d) and SU(2) Haar integrals; Gohberg–Lancaster–Rodman "Indefinite
linear algebra" (Krein space, sign characteristic, balanced inertia). Write only in `notes/astra-2026-10-25/review-gauge/`.

## Lane H items (first half of your time)

H1. `H-gauge-Haar` (independent-edge Haar average equals cotree Haar average): a gauge-fixing argument; check it handles the
    normalisation and that nothing depends on the spanning tree.
H2. `H-exterior-kernels` (equations (5)–(6): the averaged det(x − A_ρ) is determined by the exterior-power kernels): rederive. Where
    do the exterior powers Λ^k(C^n ⊗ V_ρ) enter and is the kernel of ρ^{⊗k}-averaging computed on the right space?
H3. `H-SU2-cycle-squares` (equation (9): the SU(2) doublet average is Σ over vertex-disjoint cycle collections of the squared
    matching polynomial of the remainder) and the K₄ value (x⁴ − 6x² + 3)² + 4x² + 3: recompute the K₄ and C₃ averages by TWO
    independent routes — (a) a direct Weingarten / explicit integration over SU(2) in Euler angles with high-precision quadrature
    or exact polynomial integration, (b) averaging over the finite subgroup Q₈ (or 2T) that the lane says reproduces the SU(2)
    doublet average (check that claim: for which polynomial degrees is a finite subgroup a design for the required moments?).
    Confirm C₃: (x³ − 3x)² + 1 and Petersen constant 57.
H4. `H-quaternionic-obstruction` (every quaternionic irrep fails real-rootedness on every graph with a cycle): the Kramers
    argument. Check it does not need the graph to be bipartite or the cycle to be odd; check "fails real-rootedness" means the
    AVERAGED polynomial has a nonreal root, and verify for spin 3/2 on C₃ and K₄ numerically.
H5. `H-doublet-dichotomy`, `H-unitary-average` (= HPS, det ρ nontrivial → HPS d-matching polynomial): check the HPS statement is
    quoted with the right cover degree and the right polynomial (d-matching polynomial of Hall–Puder–Sawin), and recompute U(2)
    on K₄ (constant coefficient 6) and U(3) on Petersen (largest root 2.729781416865).
H6. `H-unitary-root-limit` (empirical root measure of the U(d) average → Kesten–McKay with O(1/d) in each fixed moment): the
    formal-series proof. Check the sixth normalised moment 693/8 for U(16) on K₄ against your own computation.

## Lane K items (second half)

K1. `prop:su11-gauge-compact-unitary` (bounded holonomy iff vertexwise unitarisable): a standard fact (bounded subgroup of
    SU(1,1) is conjugate into U(1) × … ) — check the "matched endpoint conventions" clause.
K2. `cex:su11-krein-ramanujan-rigidity`: the theta-graph example g = [[5/4, 3/4],[3/4, 5/4]], h = diag((−3 ± 4i)/5), A² = (14/5)·1,
    and the K₄ example with largest eigenvalue 2.28979824583255790705…: recompute the twisted adjacency A_s exactly (sympy over
    Q(i)), its characteristic polynomial, its eigenvalues (real? semisimple? strictly inside the band (−2√q, 2√q) with q + 1 the
    degree — the theta graph is not regular: which band does the lane use for it, and is that legitimate?), and confirm the
    holonomy is nonelementary (noncommuting generators, not conjugate into a compact subgroup).
K3. `prop:su11-adjacency-pfaffian` (characteristic polynomial of A_s is a real monic square) and `prop:su11-balanced-krein-count`
    (every real semisimple eigenspace has balanced inertia; κ = half the real in-band multiplicity): the Pfaffian/anti-isometry
    argument. Rederive: SU(1,1) ≅ SL(2,R) ≅ Sp(2,R) — the twisted adjacency commutes with an antilinear (or symplectic) structure J
    with J² = −1; a real eigenvalue's eigenspace is J-stable, so even-dimensional, and the Krein form ⟨·, σ_z ·⟩ is J-anti-invariant,
    forcing balanced inertia. Check each step and the "semisimple" hypothesis (the defective case: `prop:su11-weil-inertia` says Q has
    inertia (2n − d₀/2, 2n − d₀/2, d₀) with d₀ the total geometric band-edge multiplicity — verify on the K₄ collision family).
K4. `prop:su11-k4-interior-collision` (first spectral failure at arcosh(79/54), interior collision at λ = −5/3 with ranks 6 and 4,
    two length-two Jordan chains): recompute the family, the collision parameter t* = 0.9285326263124587…, and the ranks exactly.
K5. `prop:su11-unicyclic-theta-formulas` and `cex:su11-krein-count-semicontinuity`: check the determinant formula on a unicyclic
    graph against brute force for three random unicyclic graphs and random SU(1,1) holonomies (exact rationals on the hyperbola
    a² − |b|² = 1 via Pythagorean-type parametrisations).
K6. The proposed replacement paragraphs for `gauge-groups.md` (both lanes): AGREE / AGREE-WITH-CHANGE / DISAGREE with wording.

## Output

`astra-proofs.md` (the review) as in the protocol; `## Verdict lines` with aliases = the lanes' candidate ids (`H-…` and
`prop:su11-…`, `cex:su11-…`); `## Numerical checks for the blind lane` (your independent K₄ SU(2) polynomial, the C₃ polynomial,
the K₄ SU(1,1) characteristic polynomial, t*, and the ranks); `## What this changes in the notebook`. `progress.txt`: H1 … H6,
K1 … K6, NUM.
