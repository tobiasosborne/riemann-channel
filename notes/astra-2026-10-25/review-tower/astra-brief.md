# Lane RT: REFUTE review of lane T (2026-10-23, `notes/astra-2026-10-23/tower/`) — the torsion tower sees order and genus

You are `codex:gpt-6-astra`, acting as the adversarial reviewer. Read `notes/astra-2026-10-25/brief.md` first (binding; its REFUTE
review protocol is your output format), then `notes/astra-2026-10-23/brief.md` (game rules, conventions), then the lane under
review in full: `notes/astra-2026-10-23/tower/astra-brief.md` (what was asked), `astra-proofs.md` (what was claimed), `progress.txt`,
and the scripts in `checks/` with their saved `output_*.txt`. Background the lane relied on: `notes/adelic-gkp/overlap-data.md`,
`notes/adelic-gkp/tower-pairing.md` (lane U, with `checks/check_tower_pairing.py`, `check_cm_tower.py`), `notes/adelic-gkp/curve-bridge.md`
§6, `notes/adelic-gkp/cm-lift.md`, `HANDOFF.md` session 2026-10-06 Findings (F). Write only in `notes/astra-2026-10-25/review-tower/`.

## Items to adjudicate (in this order)

1. `thm:ordinary-torsion-similitude-order` (T1). Claim: for ordinary E, E' over F_q, isogenous with End = O, the compatible
   Frobenius/Weil/reduced-Tate tower modulo one compatible cyclotomic automorphism determines exactly (isogeny class, O). Check:
   (a) the ideal chosen prime to N' works for all N | N' and the compatibility along the tower is a genuine isomorphism of
   pro-systems, not level-by-level; (b) the Tate pairing functoriality statement used (which pairing: Frey–Rück reduced Tate on
   E(F_{q^k})[N] × E(F_{q^k})/N, or Lichtenbaum's; the correct exponent for an isogeny of degree d; which side the isogeny acts on);
   (c) the converse direction — that the tower determines O and not only Z[π]: where exactly does the tower see the conductor of
   O inside O_K? (Lenstra: E(F_{q^k}) ≅ O/(π^k − 1) as O-modules; two curves with different End in the same isogeny class can have
   isomorphic groups for small k — exhibit the smallest k that separates, for the lane's F_41 example and for a conductor-2 or
   conductor-3 example you construct). (d) Nonmaximal orders: does the proof use "every ideal class contains an ideal prime to N"
   for invertible ideals of a nonmaximal order (true, but cite or prove it) and does it silently assume Pic(O) acts transitively
   on the curves with End = O (Waterhouse: true for ordinary E; state it).
2. `thm:ordinary-strict-tower-genus` (T2). Claim: within one ordinary isogeny class and order O, strict tower isomorphism (μ_N
   identified once and for all) holds iff the relative ideal class lies in Pic(O)²; S_N(c) = Norm(A)·Norm((O/NO)^×). Check the
   reduction to norms, the "isolated-level caveat" the lane mentions (what is it exactly, and does it break the iff at some N?),
   and the identification of "genus" (classes mod squares of Pic(O) — for nonmaximal O is the genus field / norm-residue description
   still the right one?). Recompute S_N(c) for the lane's D = −24 (q = 7) and D = −20 (q = 41) examples by brute force over ideals
   of small norm, and for a class-number-4 or non-cyclic Pic example of your own (e.g. D = −84, Pic ≅ (Z/2)², where every class
   is its own genus — a sharp test: there the strict tower must separate ALL classes; find a prime p split in Q(√−21) with
   ordinary curves of End = O_K and check). PARI (`ellcard`, `ellgroup`, `ellweilpairing`, `elltatepairing`, `ellisomat`) is
   available at the interpreter named in the round brief.
3. `num:q7-strict-tower-audit` and `num:q41-same-order-tower`: rerun `tower_audit.py`, `tower_strict.py`, `replay_tower_flint.py`,
   `replay_cm_flint.py`, `audit_overlap_refinement.py`; compare with saved outputs; then **do the PARI rerun the lane left pending**
   (`checks/rerun_legacy.py` and the GP payloads of the original lane-F/U/CM scripts) and report agreement or discrepancy
   number by number. Decide the lane's claim "the common maximal order of lane U's q = 7 pair is D = −24 (Q(√−6)), not Q(√−7)" by
   computing disc Z[π] and the conductor from the curves in `tower-pairing.md`.
4. `prop:torsion-topology-retains-integral-class`: the homology argument (a topological torus isomorphism intertwining M recovers
   the class through H₁). Is it a proposition or a tautology? Give the precise statement you would register, or INVALID.
5. The lane's T4 verdict ("T4 as worded REFUTED: strict pairings do see genus") and its proposed record corrections (HANDOFF (F),
   `overlap-data.md`, `tower-pairing.md`, `data-ladder.md`, `lattice-tower.md` §8, `shard-draft/claims-rows.tsv` row
   `prop:gkp-overlaps-see-order`): AGREE / AGREE-WITH-CHANGE / DISAGREE each, with wording.

## Output

`astra-proofs.md` (the review): one section per item with the adjudication and the independent recomputation; `## Correction
ledger` (what lane T got wrong, what the brief of lane T got wrong); `## Verdict lines`; `## Numerical checks for the blind lane`
(your own numbers: the separating k of 1(c), the S_N sets of item 2 for three discriminants, the PARI-vs-FLINT agreement count of
item 3); `## What this changes in the notebook` (which candidate rows may go to the gate as `codex:gpt-6-astra`-reviewed, which
need a second-family review, the corrections you endorse). `progress.txt`: RT1 … RT5, NUM.
