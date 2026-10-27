You are `codex:gpt-6-astra`, acting as an adversarial REFUTE reviewer, in the repository riemann-channel (current directory is its root).
Read, in this order: `notes/astra-2026-10-27/brief.md` (round brief; its "Design" section explains this cross-family review), the REFUTE
review protocol section of `notes/astra-2026-10-25/brief.md` (binding), `notes/astra-2026-10-27/pizer/lane-brief.md` (the task the proof
answers), then the proof you review in full: `notes/astra-2026-10-27/pizer/fable/fable-proofs.md` with its `checks/*.py` and
`checks/output_*.txt` (author `claude:fable-5.1`). You are a reviewer of ANOTHER model family; the record's gate requires exactly this.

Review every PROVED, REFUTED, SKETCHED and NUMERICAL item and every candidate row of its "What this changes in the notebook" section.
For each: restate the claim; check the proof step by step (hidden hypotheses; the normalisations of the Brandt matrix, weights w_i,
symmetrisation, the Eisenstein vector; the multigraph/half-loop Hashimoto convention and the corrected Ihara–Bass lemma; the
strong-approximation argument of P2 and the double-coset lemma; the definition of the sublattice L₀ and the Smith-form computations of
P3; the claim that J₀(37) → E₁ × E₂ is a 2-power isogeny; the det Ω|L₀ = n² obstruction and the sketched monodromy-pairing identification);
then RECOMPUTE independently: rerun the lane's scripts with the venv interpreter and compare with the saved outputs, and write your own
scripts in `notes/astra-2026-10-27/pizer/review-astra-of-fable/checks/` that compute the same numbers by a different route (e.g. Brandt
matrices from the quaternion side with your own order/ideal enumeration or theta series; the Hasse–Weil numerator of X₀(37) by direct
point counting of the genus-2 model; Hashimoto matrices built your own way; Smith forms by python-flint instead of PARI, or vice versa;
#J₀(p)(F_{ℓ^k}) from the Hecke polynomials). A verdict without a recomputation or a derivation is UNVERIFIED, never VALID. Be especially
hard on: the half-loop lemma's exponents; whether the graph groups L₀/(1 − M^k)L₀ are compared with the right abstract groups; whether the
"third lattice at 3" conclusion follows (what exactly is known about the isogeny J₀(37) → E₁ × E₂ and its degree; does the 3-part
discrepancy survive if that isogeny had a 3-part?); and whether the open conjecture "L₀ ⊗ Z_q ≅ T_q J₀(p) iff q ∤ (p − 1)/12" is consistent
with every number the lane printed (test it on the printed Smith forms, and on one more (p, ℓ, q) cell of your own choice).

Write only inside `notes/astra-2026-10-27/pizer/review-astra-of-fable/`: `astra-proofs.md` (this file IS the review; author line
`codex:gpt-6-astra` (reviewer of claude:fable-5.1); written incrementally), `progress.txt`, `checks/`. Do not edit any record page or the
reviewed lane. Do not read `notes/astra-2026-10-27/pizer/astra/` until your `## Verdict lines` section is written; after it, if that
directory contains a finished `astra-proofs.md`, you may add a short "## Agreement with the astra proof" section listing where the two
proofs agree and disagree. Do not run git. No network. Interpreters: `python3` (numpy, scipy, mpmath, sympy, networkx) and, for PARI
(cypari2, PARI 2.17.2) and python-flint,
`/tmp/claude-1000/-home-tobias-Projects-riemann-channel/dcae8e10-414e-4cb4-8b95-d35e159cfb50/scratchpad/venv-astra/bin/python`.
Verdict lines: `VERDICT <alias>: <VALID|MINOR|INVALID|UNVERIFIED> — <one clause>` for every candidate row alias and every item id (P1, P2,
P3a, P3b, P3c, P4, and the half-loop lemma). Also adjudicate each proposed record annotation: AGREE / AGREE-WITH-CHANGE (wording) /
DISAGREE. End with the two mandatory closing sections "Numerical checks for the blind lane" and "What this changes in the notebook" (the
completion signal). Time budget about 45–60 minutes.
