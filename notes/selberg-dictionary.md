# The continuous (Selberg) dictionary: summary and pointers

Written 2026-09-12 (evening). This top-level note is the entry point for the continuous
analogue of the quantum Ihara zeta; the mathematics lives in `notes/selberg/`.

- `notes/selberg/astra-brief.md`: the brief given to the prover (codex, model
  `gpt-6-astra`, reasoning effort xhigh, single session
  `01a09541-4a59-7360-9f22-2926ca60c872`; `notes/selberg/astra-session.log`).
- `notes/selberg/astra-proofs.md`: the proof submission, 13 propositions T1.1–T6.1
  with Lamport-structured proofs, explicit hypotheses H-BASE/H-GEO/H-GUI/H-LAP/H-SZ/
  H-PHI/H-ZETA/H-GAMMA/H-AN, and a correction ledger. Restored verbatim after the
  harness overwrote it (629/629 nonblank lines byte-matched against the session log).
- `notes/reviews/selberg-2026-09-12.md`: the Opus REFUTE review (second family
  relative to the codex author), verdict per proposition.
- `notes/extract/selberg-sources.md`: the nine arXiv TeX sources fetched for the
  standard inputs, with byte-cited quotes (rows appended to `db/provenance.tsv`).
- `scripts/selberg_lindblad.py`, `outputs/selberg_lindblad.txt`: exact sympy checks
  (Lindblad = ½ΣX², Casimir on K-invariants = y²(F_xx+F_yy) with c = 1, two-jump
  Lindbladian = 2Ω, Poincaré determinant 4 sinh²) and the numerical cusp transform
  (dips at 2 log n with amplitude ∝ Λ(n)/n to eight digits, plus the exact boundary
  constant from the pole of ζ at 1).

What survived of the question "Lindblad from the vector fields on PSL, small operator =
Laplacian, Poisson comb analogy": all of it, with corrections. The Lindbladian with the
two non-compact jumps is 2Ω = −2Δ on the K-invariant sector (the Casimir carries the
compact direction with a minus sign, so it is not a Lindbladian off that sector); the
comb is the Guillemin flat trace of the geodesic flow, whose Laplace transform is
+D'/D for the tower D(ς) = ∏_{j≥1} Z_Sel(ς+j); the tower's zeros are the bands
−½−k±ir_j, and the nonconstant first band sits on Re ς = −½ iff Δ has no eigenvalue in
(0,¼); the primes of ζ enter only through the cusp of the modular surface, as dips of
weight Λ(n)/n at 2 log n in the transform of −½ φ'/φ(½+ir), plus ½ from the pole of ζ.
The direct sum over primes of circles has only a local orbital trace and no zeros.
The lab-book sections are `report/sections/09b_selberg_dictionary.tex` and
`09c_selberg_tower_cusp.tex`.
