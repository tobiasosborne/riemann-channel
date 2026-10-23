# Lane T: the torsion tower with its pairings sees the endomorphism order and never the ideal class — theorem and audit

You are `codex:gpt-6-astra`, a prover and constructive verifier in a mathematical research notebook (git repo, current
directory). Read `notes/astra-2026-10-23/brief.md` first (binding). Then read, in this order: `notes/adelic-gkp/data-ladder.md` §0–§2
and the "answer in one paragraph" (the claims "the counts decide RH but fix only the isogeny class", "the lattice's class is seen by
the pairing, not by any overlap", "the tower is blind to RH but sees the lattice class"); `notes/adelic-gkp/overlap-data.md` (lane F:
"overlaps see the order, never the class; the Weil pairing sees the class" — find the exact statement and the computation behind
it); `notes/adelic-gkp/tower-pairing.md` (lane U: "the tower's logical commutator with the step is the Weil/Tate pairing exactly
and separates the q = 7 lattices at N = 8"; open item "whether the tower sees the class only up to genus in general";
`checks/check_tower_pairing.py`, `check_cm_tower.py`), `notes/adelic-gkp/curve-bridge.md` §6 (Latimer–MacDuffee: the lattices in an
isogeny class of ordinary elliptic curves with a given endomorphism ring form a torsor under the class group; "counts do not fix
the lattice"), `notes/adelic-gkp/lattice-tower.md` (the level tower of GKP codes: the lattices (1 − M^k)Z^{2n}, the level-N Bell
pairs, the syndrome torus), the partial review `notes/reviews/adelic-gkp-rsu-fable-2026-10-06.md` (what was and was not
adjudicated for lane U: "the 42 comparisons and the N = 8 separation of lane U are unadjudicated"), and `db/claims.tsv` rows
`cit:latimer-macduffee`, `cit:lenstra-structure`. Literature to cite from memory: Waterhouse, "Abelian varieties over finite
fields" (1969, the class-group torsor for ordinary curves; End rings in an isogeny class); Lenstra, "Complex multiplication
structure of elliptic curves" (J. Number Theory 1996: E(F_{q^k}) ≅ O/(π^k − 1) as O-modules for ordinary E with End = O);
Deligne, "Variétés abéliennes ordinaires sur un corps fini" (1969); Silverman AEC III.8 (Weil pairing, e_N(φx, φy) = e_N(x, y)^{deg φ}
on the target); Frey–Rück / Lichtenbaum on the Tate pairing; Kohel's thesis (isogeny volcanoes). PARI through cypari2 (see the
shared brief) gives `ellcard`, `ellgroup`, `ellweilpairing`, `elltatepairing`, `ellisomat`/`ellisogeny` over finite fields;
use it for the audit. Write only `notes/astra-2026-10-23/tower/{astra-proofs.md,progress.txt,checks/}`.

## 0. Definitions

E/F_q ordinary elliptic curve, π Frobenius, O = End(E) ⊇ Z[π]. The TOWER DATA of E: for every k the group E(F_{q^k}) with the
action of π, and for every N the Galois module E[N] = E(F̄_q)[N] with the action of π, the Weil pairing e_N: E[N] × E[N] → μ_N, and
the Tate pairing(s) on E[N] over F_{q^k} for every k with N | q^k − 1. Two curves have ISOMORPHIC tower data if for every N there is
a π-equivariant group isomorphism E[N] → E'[N] carrying e_N to e_N' up to an automorphism of μ_N (and the same for the Tate
pairings), compatibly along the tower (N | N'); say exactly what compatibility means and whether lane U's definition is this one.
Define also the STRICT tower data where the identification of μ_N is fixed once and for all (the "ε-uniform identification" of
HANDOFF 2026-10-06 (iii)), which forbids the Aut(μ_N) freedom.

## 1. The conjectures

T1 (blindness theorem). Let E, E' be ordinary over F_q, isogenous, with End(E) = End(E') = O. Then E and E' have isomorphic tower
data. Proof sketch to complete: E' ≅ I ∗ E for an invertible O-ideal I (Waterhouse/Deligne); for each N choose I in its class
prime to N (possible: every ideal class contains ideals prime to any given integer); the isogeny φ_I: E → I ∗ E has degree N(I)
prime to N, so φ_I: E[N] → E'[N] is a π-equivariant isomorphism and e_N'(φx, φy) = e_N(x, y)^{N(I)}, i.e. the Weil pairing is
carried to itself up to the automorphism ζ ↦ ζ^{N(I)} of μ_N; the same for the Tate pairing (prove it, with the correct
statement of the Tate pairing's functoriality). Compatibility along the tower: the choice of I depends on N; show that one can
choose compatible identifications (I prime to N' works for all N | N') and that the resulting system is an isomorphism of tower
data as defined. Also the group structures: E(F_{q^k}) ≅ O/(π^k − 1) ≅ E'(F_{q^k}) (Lenstra). Conclude: the tower data determine
at most the pair (isogeny class, O), i.e. the order, never the ideal class.

T2 (what the strict tower sees). With the identification of μ_N fixed (strict data), the isomorphism above is twisted by
ζ ↦ ζ^{N(I)}. Conjecture: the strict tower data see the class of I only through the norms N(I) mod N for ideals I in the class,
i.e. through the image of the class in (Z/N)^×/(norms of principal ideals…) — determine exactly: the set {N(I) mod N : I in the
class, I prime to N} and whether it separates classes. For K = Q(√−7)-type CM orders used in lane U (q = 7, N = 8; find the
actual curves and orders in `tower-pairing.md`) compute this set. If the strict data separate some classes and not others, say
which (conjecture: they separate exactly the classes whose norm-residue invariants differ, a genus-theory invariant: the tower
sees the class "up to genus", which is the open item's phrase — prove it or correct it).

T3 (audit). Lane F's "the Weil pairing sees the class" and lane U's "separates the q = 7 lattices at N = 8": re-run
`check_overlap_data.py` and `check_tower_pairing.py` (read them first; they may use their own conventions), and decide for each
whether the separation observed is (a) a separation of different endomorphism orders (then T1 is consistent and the pages'
wording must change to "sees the order"), (b) a separation of classes in the strict sense of T2 (genus-theory), or (c) an
artefact of a non-equivariant identification (a bug). Print the endomorphism rings of the curves involved (PARI: compute
the discriminant of Z[π] and the conductor of End(E) from the isogeny volcano, `ellisomat` or the Kohel-type criterion) and the
norm-residue sets of T2.

T4 (the ladder). State the consequence for `data-ladder.md`: every datum that is "local or torsion" (counts, groups, pairings,
level-N Bell pairs, syndrome tori of the level tower) determines at most the order; the ideal class is a global datum of H_1 of
the canonical lift. Formulate the sharpest true sentence for the ladder's "lattice" column and for zeta (where the ladder says the
missing item is "a finite-rank integral structure on a global H^1": T1 says that no tower of local/torsion data can supply its
class, only its order; say whether that is a new constraint or a restatement).

## 2. Numerics (checks/)

`checks/tower_audit.py` (PARI via cypari2: for q = 7 and the lane-U curves, and for a second example with class number 2 or 3 and
the same order, e.g. find ordinary curves over F_p with End = O_K for K of class number 2 (disc −15, −20, −24) and p split: list
all curves in the isogeny class with End = O_K (there are h(O_K) of them up to isomorphism), compute E(F_{p^k}) for k ≤ 6, E[N]
with Weil pairing values on a basis for N = 2, 3, 4, 8 (in F_{p^k} with N | p^k − 1), the Tate pairings, and exhibit the
equivariant isomorphisms of T1 explicitly as the isogenies φ_I), `checks/tower_strict.py` (the norm-residue sets of T2). Outputs to
`checks/output_*.txt`.

## 3. Output

`astra-proofs.md`: §1 T1 PROVED (full proof, with the Tate-pairing functoriality statement and its source); §2 T2 decided; §3 T3
the audit verdict per page with the printed orders; §4 T4; correction ledger; "Numerical checks for the blind lane" (the h(O)
curves of one class-number-2 example with their E(F_p) and one Weil-pairing value each, and the isogeny that identifies them);
"What this changes in the notebook" (which sentences of `overlap-data.md`, `tower-pairing.md`, `data-ladder.md` and HANDOFF must
change; candidate rows; whether `shard-draft/` rows are affected).
`progress.txt`: T0, T1, T2, T3, T4, NUM.
