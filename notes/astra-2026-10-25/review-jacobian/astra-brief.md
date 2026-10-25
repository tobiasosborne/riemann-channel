# Lane RJ: REFUTE review of lane J (2026-10-23, `notes/astra-2026-10-23/jacobian/`) — Ramanujan fluxes as abelian varieties and Jacobians

You are `codex:gpt-6-astra`, acting as the adversarial reviewer. Read `notes/astra-2026-10-25/brief.md` first (binding; its REFUTE
review protocol is your output format), then `notes/astra-2026-10-23/brief.md`, then the lane under review in full:
`notes/astra-2026-10-23/jacobian/astra-brief.md`, `astra-proofs.md`, `progress.txt`, `checks/*.py` and `checks/output_*.txt`
(`output_fluxes.json.txt` has every orbit's A, Weil polynomial, N_k, a_k). Background: `notes/adelic-gkp/no-lift.md`,
`notes/adelic-gkp/howe-positivity.md`, `notes/adelic-gkp/curve-bridge.md` §6, `notes/adelic-gkp/graph-super.md`,
`notes/adelic-gkp/data-ladder.md` §0. Literature from memory: Centeleghe–Stix (Algebra & Number Theory 2015: abelian varieties over
F_p with no real Weil root ±√p ⟷ finitely generated Z[F, V]-modules); Howe (Trans. AMS 1995, principal polarizations and the
positivity criterion); Serre's resultant-1 lemma (Howe–Lauter); Maisner–Nart; Howe–Nart–Ritzenthaler. Write only in
`notes/astra-2026-10-25/review-jacobian/`.

## Items to adjudicate (in this order)

1. The dictionary (§0): a strict Ramanujan Z₂ flux on a (p+1)-regular graph with signed adjacency A gives F with F + V = A,
   FV = p, i.e. F a root of x² − Ax + p. Check that the lane's module is the Centeleghe–Stix one (Z^{2n} with F = M? or Z^n ⊗ Z[F]/(F²−AF+p)?
   — identify it exactly and check it is finitely generated, torsion-free, with the right rank 2n), that "strict Ramanujan" is
   used correctly (no eigenvalue ±2√p, so no real Weil root), and that p = 2, 3 are prime fields (Centeleghe–Stix needs F_p).
2. `K₄ trigonal genus-4 Jacobian class` (§3.1): the curve on the cone XY + Z² = 0 cut by a cubic over F₂, counts 3, 9, 9, 29 and
   the claim that its L-polynomial equals the K₄ Weil polynomial. Recompute: take the lane's explicit equation, count points over
   F_{2^k}, k ≤ 8, by brute force in your own code (and/or with PARI `hyperellcharpoly` where applicable — not here since it is
   nonhyperelliptic; use direct enumeration of the projective model, checking smoothness via the Jacobian criterion at every
   point over F̄₂ up to the needed degree, or via a resultant/discriminant computation), and confirm genus 4 (canonical curve on
   a quadric cone of P³: degree 6 complete intersection of a quadric and a cubic → genus 4 if smooth). Confirm "no hyperelliptic
   representative" by the lane's N₂ bound or independently (264 classes / 217 L-polynomials: recount).
3. `K₅: every Ramanujan orbit a hyperelliptic genus-5 Jacobian over F₃` (§3.3): rerun `jac_hyperelliptic_f3.py` (1,062,882
   equations); independently verify ONE witness per orbit with a different method (PARI `hyperellcharpoly` over F_3 gives the
   L-polynomial directly; compare with the Weil polynomial of the orbit from `output_fluxes.json.txt`). Check the orbit count 5
   and the witness counts (6, 42, 6, 42, 24) at least for one mask by an independent enumeration.
4. J1 refutation (§1): "no unit in Z[F, V] repairs K₄; the repair U = A + (1 − A²)/2 lives in the saturated order". Verify the
   congruence obstructions and that U is integral on the lattice (A² ≡ 1 mod 2 on the relevant lattice?). Check the twelve
   "small-ring NO certificates" are about the right ring, and the scope table's ordinary/nonordinary labels (ordinary iff the
   middle coefficient of the Weil polynomial is odd for p = 2 / prime to p in general — verify per orbit).
5. J2 refutation (§2): the cube flux with a₄ = −1 and the Petersen flux with negative N₅/a₅. Recompute N_k and a_k from the Weil
   polynomial by your own code (a_k = Möbius inversion of N_k over divisors). Confirm negativity. Check the "all-k certificate".
6. `prop:connected-signed-no-resultant-one-partition` (§3.5): the integral orthogonal-projector argument. Is it a proof? Find the
   gap or confirm; test numerically on 20 random connected signed graphs (compute all factorisations of det(tI − A) over Z and
   pairwise resultants).
7. The §3.4 OPEN table (Petersen 6, 10, 22; K₃,₃ 1, 6; cube 3, 5 "pass every a_k test, impossible hyperelliptically") and the
   "PROVED NO" entries (Petersen 1; cube 1, 9, 23): recompute every entry's a_k through k = 12 yourself.
8. Proposed record corrections (`no-lift.md`, `howe-positivity.md`, `curve-bridge.md` §6, `graph-super.md`, `data-ladder.md` §0):
   AGREE / AGREE-WITH-CHANGE / DISAGREE with wording.

(The K₃,₃ census lookup itself is lane J2 of this round, `notes/astra-2026-10-25/census/`; do not duplicate it.)

## Output

`astra-proofs.md` (the review) as in the protocol; `## Verdict lines` with aliases = the lane's candidate ids (use
`jac:k4-trigonal`, `jac:k5-hyperelliptic`, `jac:j1-refuted`, `jac:j2-refuted`, `jac:resultant-one`, `jac:dictionary`,
`jac:open-table` where the lane gave no id); `## Numerical checks for the blind lane` (your independent counts: the K₄ curve's
N₁..N₈; one PARI L-polynomial per K₅ orbit; the cube a₄; the resultant test tally); `## What this changes in the notebook`.
`progress.txt`: RJ1 … RJ8, NUM.
