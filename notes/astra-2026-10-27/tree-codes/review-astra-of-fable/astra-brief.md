You are `codex:gpt-6-astra`, acting as an adversarial REFUTE reviewer, in the repository riemann-channel (current directory is its root).
Read, in this order: `notes/astra-2026-10-27/brief.md` (round brief; its "Design" section explains this cross-family review), the REFUTE
review protocol section of `notes/astra-2026-10-25/brief.md` (binding), `notes/astra-2026-10-27/tree-codes/lane-brief.md` (the task the
proof answers), then the proof you review in full: `notes/astra-2026-10-27/tree-codes/fable/fable-proofs.md` with its `checks/*.py` and
`checks/output_*.txt` (author `claude:fable-5.1`). You are a reviewer of ANOTHER model family; the record's gate requires exactly this.

Review every PROVED, REFUTED, SKETCHED and NUMERICAL item and every candidate row of its "What this changes in the notebook" section,
and its correction ledger C1–C7 (each ledger entry is itself a claim to adjudicate). For each: restate the claim; check the proof step by
step (the Weyl phase convention and the sign of the symmetric cocycle, C1; the "nested tower of codes per vertex" statement, C2; the
dual-lattice formula and colour parity, T1; the MUB identification, T2; the translation-length formula ℓ(γ) = max(v(det γ) − 2v(tr γ), 0) and
the Newton-polygon argument, T3; the code-tower trace theorem Tr(P_n D_a P_n) = |a|^{1/2} p^{min(v(1−a), 2n)} including the case |a|_p > 1
and a = 1, T4(b); the attribution "D_λ is the Weil image of γ²/det γ", C3, and the odd-length decomposition, C4; the orbit identity and its
normalisation table against the graph explicit formula of `graph-ihara.md` §5 and Connes's local term; the bipartite correction for
X^{5,13}, C6; the T5 statements Ω(v_μ, v_{q/μ}) = μ − q/μ and the flat trace 2p^{−ℓ/2} of the principal series), then RECOMPUTE independently:
rerun the lane's scripts and compare with the saved outputs, and write your own scripts in
`notes/astra-2026-10-27/tree-codes/review-astra-of-fable/checks/` computing the same numbers by a different route (your own MUB
construction and Gram matrices for p = 3, 5, 7; your own lattice reduction for the axis test; the code-tower trace by explicit finite
matrices on Z/p^{2n} for small p, n and several a including |a| > 1 and v(1 − a) > 2n; your own LPS graph (at least X^{5,11}, 660 vertices)
with N_k from a sparse Hashimoto operator, the prime-cycle counts, and the explicit-formula residual with the lane's orbit weights). A verdict
without a recomputation or a derivation is UNVERIFIED, never VALID. Be especially hard on: whether T4(b) is really an identity of traces
or only of numbers; the square in C3 (is the orbit weight attached to γ or to γ²/det γ, and does the Euler product over primitive γ then
need ℓ(γ) or 2ℓ(γ)?); and whether `thm:ihara-zeta-squeeze-lefschetz` as stated holds for bipartite quotients.

Write only inside `notes/astra-2026-10-27/tree-codes/review-astra-of-fable/`: `astra-proofs.md` (this file IS the review; author line
`codex:gpt-6-astra` (reviewer of claude:fable-5.1); written incrementally), `progress.txt`, `checks/`. Do not edit any record page or the
reviewed lane. Do not read `notes/astra-2026-10-27/tree-codes/astra/` until your `## Verdict lines` section is written; after it, if that
directory contains a finished `astra-proofs.md`, you may add a short "## Agreement with the astra proof" section listing where the two proofs
agree and disagree. Do not run git. No network. Interpreters: `python3` (numpy, scipy, mpmath, sympy, networkx) and, for PARI (cypari2,
PARI 2.17.2) and python-flint,
`/tmp/claude-1000/-home-tobias-Projects-riemann-channel/dcae8e10-414e-4cb4-8b95-d35e159cfb50/scratchpad/venv-astra/bin/python`.
Verdict lines: `VERDICT <alias>: <VALID|MINOR|INVALID|UNVERIFIED> — <one clause>` for every candidate row alias, every item id (T1, T2, T3,
T4a, T4b, T4c, T5) and every ledger entry (C1–C7). Also adjudicate each proposed record annotation: AGREE / AGREE-WITH-CHANGE (wording) /
DISAGREE. End with the two mandatory closing sections "Numerical checks for the blind lane" and "What this changes in the notebook" (the
completion signal). Time budget about 45–60 minutes.
