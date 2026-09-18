# CCM in tensor-network language — rk-light campaign

User directive (2026-09-18): make a complete understanding of CCM in this
project's tensor-network terms the current focus; investigate the Weil form,
bond and transfer spaces, kernel, and reconstruction; write lab-book shards.

Read `/home/tobias/.claude/skills/rk-light/SKILL.md`. The existing
`db/{claims,definitions,notation,provenance}.tsv` remain the single sources of
truth; this directory contains research arguments, review records, and briefs.
No author promotes their own claims. All new arguments begin as SKETCH.
Use addressable ASSUME/PROVE steps and explicit hypotheses, and preserve
refuted stronger formulations. Numerical checks are evidence, never proofs.

## Questions and integration contract

1. Distinguish the physical MPS auxiliary space, its doubled transfer space,
   the Hilbert space of operators on that transfer space, and the cyclic
   moment/GNS space. Which of these does CCM reconstruct?
2. Give the actual contractions for counts, the Weil moment matrix, and its
   Gram realisation. Track conjugation, metric, grading, and normalisation.
3. Characterise the kernel and the minimal-eigenvector prescription; separate
   exact finite reconstruction from finite-window fitting and continuous CCM.
4. Derive the rank-one boundary correction and explain the quotient metric,
   secular equation, and what remains missing for the Riemann bond.
5. Attack the tempting identifications: positivity implies native unitarity;
   trace counts detect Jordan blocks; kernel always annihilates the original
   transfer; full physical bond recovered; real finite spectrum proves RH;
   unregularised trace/HS norm of an infinite unitary flow is finite.

Root alone edits report/sections, report.tex, db/, HANDOFF.md, shared summaries,
and CI. Workers have disjoint lane files. Propose merge text in your own lane.
Use existing macros where sensible; no new local LaTeX macros. Shards <=320
lines. Definitions will be centralised in `02i_definitions_ccm_tensor.tex`.
Proposed theorem ids should start `thm:ccm-tn-`, `prop:ccm-tn-`, etc.

## Lanes

- finite (Sol 5.6 xhigh): `notes/ccm-tensor-network/finite.md` and optional
  `finite-shards.tex`; finite Gram, kernels, GNS/reconstruction, tensor network,
  grading, counterexamples. No shared edits.
- continuous (Astra xhigh): `notes/ccm-tensor-network/continuous.md` and optional
  `continuous-shard.tex`; source-checked continuous/Loewner CCM, exact rank-one
  correction, natural transfer/insertion networks and limits. No shared edits.
- checks (Sol 5.6 xhigh): `scripts/ccm_tensor_network.py`,
  `outputs/ccm_tensor_network.txt`, `notes/ccm-tensor-network/checks.md` and
  `notes/ccm-tensor-network/checks/`; independent reproducible checks, red
  mutations on copies, no bare assert. No shared edits.

## Sources

- `HANDOFF.md:171-202` is the proposal to scrutinise, not an established theorem.
- `report/sections/03c_graded_ramanujan.tex`, `03f_selberg_letters_finite.tex`,
  `04e_cmps_parity_overlap.tex`, `04f_cmps_twisted_supertrace.tex`,
  `08b_weil_positivity.tex`, `08c_weil_positivity_continuous.tex`.
- `notes/zeta-spectral-triples/plan.md`, `ihara/lanes/theory.md`,
  `ellcurve/astra-review.md`, `ellcurve/report-ell.md`.
- Primary sources `refs/src/2511.22755/mc2arXiv.tex` and the TeX source under
  `refs/src/2511.23257/`. Cite file, line, label. Any cited-fact row needs a
  short exact contiguous quotation for the provenance database.

Work autonomously; report genuine blockers, not permission questions. Do not
edit or commit the pre-existing uncommitted zst/ellcurve/tutorial work.
