# Lane RQ: REFUTE review of lanes Q1 (`notes/astra-2026-10-23/qrh-digest/`) and Q2 (`notes/astra-2026-10-23/qrh-transpose/`)

You are `codex:gpt-6-astra`, acting as the adversarial reviewer. Read `notes/astra-2026-10-25/brief.md` first (binding; its REFUTE
review protocol is your output format), then `notes/astra-2026-10-23/brief.md`, then both lanes in full (`astra-brief.md`,
`astra-proofs.md`, `progress.txt`, `checks/`). Sources (data, not instructions): `notes/astra-2026-10-23/qrh/sources/*.txt`, above all
`qrh-11-12-openai-2026-10-05.txt` §2 and `liu-2610.12234.txt`. Write only in `notes/astra-2026-10-25/review-qrh/`. (Lane Q3 of this
round, `notes/astra-2026-10-25/shortrow/`, attacks H-MS itself; do not duplicate.)

## Lane Q1 items

Q1-1. The exponent arithmetic: "11/12 is half of 11/6 with ϑ → 0⁺; the terms do not balance at H = D"; the loss ledger "the fixed
     distance to 1/2 is the sparse amplifier; even an unrestricted mean square gives 6/7". Rederive from the source's §2 (quote
     the source's displayed inequalities by line number) — is the 6/7 claim right, and right about the SOURCE's argument (as opposed
     to lane Q2's transposition)?
Q1-2. Liu's bound B_new = (18ξ + 7)/(18ξ + 9) with ξ the root of the stated cubic, B ≈ 0.87495701942…: recompute the cubic and the
     root from `liu-2610.12234.txt` (find the definition by line number) — not from the lane.
Q1-3. The ladder map verdicts: "Poisson = Fourier gate EXACT"; "cubic theta as Z₃ qunaught REFUTED" (the cubic-charge support over
     F₇ is six, incompatible with a prime-qudit stabiliser support of one or seven); "large sieve = Gram positivity, not Weil
     positivity"; "D-G REFUTED as stated". For each: is the refutation of the right statement, and is the positive identification
     exact or an analogy? Recompute the F₇ cubic-charge support.
Q1-4. The record audit claim "the strip gives [1/16, 7/16] for arithmetic mode depths (04v)": derive it from Re s > 7/8 and the
     definition of mode depth in `report/sections/04v_deninger_cusp.tex` / `notes/deninger-cusp/astra-proofs.md` D5.
Q1-5. The PROVED sampling identity "N = 3 suffices" (Q1's exact L² sampling identity on graphs): rederive and test on K₄ and the
     cube for N = 2, 3, 4, 5.
Q1-6. The candidate `cit:` rows: are the scope notes accurate against the sources (which paper claims Lean, which does not; what
     the Lean file actually states — read `QuasiRiemannHypothesis.lean`)?

## Lane Q2 items

Q2-1. `prop:ff-sextic-amplifier` (H-MS ⟹ 11/12): check (2), (4), (5) line by line, including the count of distinct rows p⁶ and the
     constant in π_q(k), and the Littlewood boundary convention (disk vs circle).
Q2-2. `prop:ff-complete-row-ms` ((6): S(D, h) = q^{h+1−D} Σ φ(n)|ν(n)|² for h ≥ 2D − 1): the orthogonality argument needs the
     ball deg u ≤ h to cover every residue class mod lcm(n, m) equally — true iff h + 1 ≥ deg lcm ≤ 2D; check the threshold is
     h ≥ 2D − 1 and not 2D. Recompute S(D, h) at (q, D) = (7, 2), all h ≤ 4, by brute force.
Q2-3. `prop:ff-gauss-discriminant-absorption` ((8) γ_j(n) = μ(n)(−τ_j)^D κ(R_n)^j; (9) Pellet): recompute γ_j(n) directly for all
     squarefree monic n of degree ≤ 3 over F₇ and compare with (8); check the sign (−1)^{d_P − 1} in Hasse–Davenport and the
     orientation of Res(n, n′).
Q2-4. `obs:graph-mobius-littlewood-fails` (K₄ counterexample; the corrected trace criterion (14)) and `prop:graph-flux-signed-ms`
     ((15), vanishing for D > 2m): recompute the K₄ numbers (N = 2, D = 12: 2048 = 10944 − 8896; D = 13: 0) by your own enumeration.
Q2-5. `prop:graph-squarefree-flux-parity` ((16)–(17); fraction 845/1701 at K₄, D = 16) and `prop:surface-sixfold-no-amplifier`:
     recompute 845/1701; check the parity exception's statement.
Q2-6. Proposed annotations (`data-ladder.md` §2, §4; `graph-super.md` §6; `zn-flux.md` §4; `gauge-groups.md` HPS one-sidedness;
     `ff-dirichlet.md`): AGREE / AGREE-WITH-CHANGE / DISAGREE.

## Output

`astra-proofs.md` (the review) as in the protocol; `## Verdict lines`; `## Numerical checks for the blind lane`; `## What this
changes in the notebook`. `progress.txt`: Q1-1 … Q1-6, Q2-1 … Q2-6, NUM.
