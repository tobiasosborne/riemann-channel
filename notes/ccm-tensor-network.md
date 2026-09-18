# CCM as reconstruction from tensor-network ring data

Current focus requested by TJO on 2026-09-18. The new lab-book sequence is
`02i_definitions_ccm_tensor.tex` followed by `03g` through `03l`.
`db/claims.tsv` is the status/dependency ledger; review records are
`notes/reviews/ccm-tensor-{finite,continuous}-r1.md` and `-r2.md`.
Final adjudication: 15 proved statements, four preserved refutations, and
one open Riemann-bond identification; both second-round reviews PASS.

## Read the shards in this order

1. **03g — Weil Gram and the actual tensor network.** Open powers of a
   retained transfer become Hilbert--Schmidt features in an explicitly
   supplied unitarising metric. A clock register purifies their Gram; a
   unary-clock MPS gives a concrete construction of bond at most 2r.
2. **03h — Kernel and recovered information.** At the critical finite
   window the kernel gives the square-free support polynomial. It is the
   original operator's minimal polynomial only under semisimplicity.
   Weights retain multiplicities; Jordan structure, original physical
   letters and native eigenvectors are not recovered. Grading needs net
   weights of the correct sign.
3. **03i — CCM boundary correction.** Window correlations give a Loewner
   matrix with a rank-two displacement. The minimal vector fixes a rank-one
   boundary correction; the shifted metric makes its quotient self-adjoint.
   A concrete negative input form gives the same real output as a positive
   one, so reality is not a Weil-positivity certificate.
4. **03j — Exact F5 example.** The net divisor of the graded Pauli edge lift
   yields a two-dimensional companion, an explicit positive metric and a
   three-length annihilating relation. The raw doubled adjacency is a
   different operator.
5. **03k — Nullvector and Hamiltonians.** W=F*F is a clock Hamiltonian;
   its kernel projector constrains the transfer history. A separate
   propagation Hamiltonian enforces successive transfer powers, with a
   unique history ground line after boundary pinning. D-double-prime is a
   different Hamiltonian on the quotient, where the nullvector is removed.
6. **03l — Continuous and infinite limits.** Smeared transfer operators
   give a valid HS Gram with explicit summability. An exact intertwiner is
   proved only for an existing finite spectral model with zero unshifted
   minimum and the CCM simple-radical hypotheses. An arithmetic Riemann
   bond and increasing-window identification remain open.

## What changed from the initial handoff

The bond-space proposal survives with explicit choices of space and metric.
Four stronger assertions are retained as refuted rows: unconditional
annihilation of the original transfer by the moment null polynomial;
positive supertrace form from unitary parity sectors; ordinary orthogonal
compression of the scaling operator; and a finite raw HS Gram of an
infinite unitary flow.

The Hamiltonian construction uses additional length/feature degrees of
freedom. It proves no physical-site locality for the original MPS and
identifies no Bost--Connes entanglement spectrum.

## Evidence and review

The proof notes are in `ccm-tensor-network/{finite,continuous,examples,hamiltonian}.md`.
The root checker is `scripts/ccm_tensor_network.py`; deterministic output is
`outputs/ccm_tensor_network.txt`. It checks exact small examples, clock
conjugation, the unary automaton, propagation and pinning, graded signs,
Jordan blindness, and the CCM correction, with copied mutations that must
fail. Independent critic checkers live in the review subdirectories.

The rk-light issue and repair records are `ccm-tensor-network/ISSUES.md` and
`repair-r1-response.md`. Proposer and critic roles are separate, but all
workers in this campaign are OpenAI models; this is not a cross-family review.
