# Lane I: which representations have RH on average — classify the irreps whose Haar-averaged twisted characteristic polynomial is real-rooted in the band on every graph

You are `codex:gpt-6-astra`, a prover and constructive verifier. Read `notes/astra-2026-10-25/brief.md` first (binding), then
`notes/astra-2026-10-23/brief.md`, then lane H of the previous round in full (`notes/astra-2026-10-23/haar/astra-brief.md`,
`astra-proofs.md`: §0 gauge fixing, §1 the exterior-kernel formula (5)–(6) and the U(d) = HPS theorem, §2 the quaternionic
obstruction and the doublet dichotomy, §3 the root limit, §4 finite groups; `checks/haar_weingarten.py`, `haar_finite.py`).
Background: `notes/adelic-gkp/gauge-groups.md`, `graph-super.md` §6, `zn-flux.md` §4. Literature from memory: Hall–Puder–Sawin
(Adv. Math. 2018: for a group G and a representation π, the expected characteristic polynomial of the π-twisted adjacency of a
random G-labelling is real-rooted and in the band when π is the standard representation of S_d — the d-matching polynomial —
and they ask/answer for which (G, π) in general: their Theorem about "π-matching polynomials" and the condition that the
expected product be a matching polynomial), Heilmann–Lieb, Godsil (matchings and walks), Marcus–Spielman–Srivastava. Write only
in `notes/astra-2026-10-25/irreps/`.

## 0. The object

Y a finite graph, G compact, ρ: G → U(d) a unitary representation. A G-gauge field assigns g_e ∈ G to each oriented edge with
g_ē = g_e^{−1}; the twisted adjacency A_ρ acts on C^n ⊗ C^d. The AVERAGE polynomial Φ_{ρ,Y}(x) = E_Haar det(x − A_ρ). Lane H: for
ρ = defining rep of U(d), Φ is the d-matching polynomial of HPS (real-rooted, roots in [−2√(deg−1), 2√(deg−1)] for regular Y); for
quaternionic irreps (e.g. SU(2) spin 1/2: Φ_{K₄} = (x⁴ − 6x² + 3)² + 4x² + 3) Φ has nonreal roots on every graph with a cycle; for
dimension-2 irreps: det ρ nontrivial ⟹ HPS 2-matching polynomial, det ρ trivial ⟹ failure.

## 1. The conjecture

I-1 (classification). Φ_{ρ,Y} is real-rooted for every finite graph Y iff Φ_{ρ,Y} equals a matching-type polynomial, iff ρ satisfies
a MOMENT condition: E[ρ(g)^{⊗k} ⊗ ρ̄(g)^{⊗k}] restricted to the relevant invariants coincides, for all k up to the needed degree,
with that of the defining representation of U(d) (or of S_d), i.e. ρ is "unitary-like to all orders": the invariant tensors of
ρ^{⊗k} ⊗ ρ̄^{⊗k} are spanned by the permutation (Brauer-free) tensors. Make this precise: by lane H's exterior-kernel formula the
average depends only on the kernels/invariants of Λ^k(C^n ⊗ C^d) under ρ-averaging along cycles; characterise the ρ for which
the cycle-average of ρ(g_1 ⋯ g_ℓ) ⊗ … contributes only the "HPS terms". Candidates: (a) ρ real or quaternionic ⟹ extra invariants
(the bilinear form) ⟹ failure on some graph (lane H proved quaternionic; prove or refute REAL irreps: SO(3) spin 1 on C₃, K₄,
the cube — compute exactly); (b) ρ complex (not self-dual): is Φ then always the d-matching polynomial? Test: U(1) characters
(known: yes, for every nontrivial character — graph-super §6 / zn-flux §4), SU(3) defining (complex, d = 3): compute Φ on C₃, K₄,
Petersen exactly (Weingarten for SU(3) or a finite unitary 3-design subgroup — justify the design degree needed: degree 2·(#cycles)
in the holonomies); SU(2) spin 1 (real, d = 3); U(2) irreps det^a ⊗ Sym^b; S_n irreps other than the standard one (the sign
representation; the 2-dimensional irrep of S_3; the standard of S_4 vs. its product with sign); the dihedral and quaternion
irreps; a Z_N character (complex for N ≥ 3, real for N = 2 — but Z_2 works: the signing average IS the matching polynomial; so (a)
is false as stated for d = 1 — find the right condition: perhaps "the invariant tensors of ρ^{⊗k} ⊗ ρ̄^{⊗k} are exactly the
permutation tensors for k ≤ |E|" fails for real ρ only when d ≥ 2).
I-2 (the theorem). Prove the sharp classification for compact connected G and irreducible ρ, or for finite G with the design
argument, at least for the class "Φ_{ρ,Y} = d-matching polynomial for all Y". Conjecture: iff ρ is complex-type (Frobenius–Schur
indicator 0) AND its moments up to order |E| match U(d) — which for an irrep of a compact connected group forces ρ(G) ⊇ SU(d)
or d = 1. For FINITE groups: iff ρ(G) is a unitary design of high enough degree — give the degree in terms of Y (the girth / the
number of cycles) and verify with Q₈, 2T, 2O, A₅, S₄ on K₄ and the cube.
I-3 (beyond matching polynomials). Is there any ρ with Φ_{ρ,Y} real-rooted on all graphs but NOT equal to a matching polynomial?
Candidate test cases: real irreps on bipartite graphs only (then the quaternionic argument may fail — check), ρ ⊕ ρ̄.
I-4 (the ladder). One paragraph for `gauge-groups.md` and `data-ladder.md` §2: "RH on average" is a property of (Y, ρ, ensemble);
the classification says which ρ supply it uniformly.

## 2. Numerics (checks/)

`checks/irreps_scan.py`: exact Haar averages (Weingarten or finite designs, exact rationals/cyclotomics) for the representations
listed, graphs C₃, K₄, K₃,₃, cube, Petersen; prints Φ, real-rootedness (Sturm, exact), in-band verdict, and whether Φ equals the
matching-type polynomial. Outputs to `checks/output_*.txt`.

## 3. Output

`astra-proofs.md`: §1 I-1 (the table of ρ × Y with verdicts, exact polynomials), §2 I-2 (theorem or sharpest partial with the
obstruction), §3 I-3, §4 I-4; correction ledger; "Numerical checks for the blind lane"; "What this changes in the notebook"
(candidate rows `thm:rh-on-average-irrep-classification` or `cex:…`; the `gauge-groups.md` paragraph). `progress.txt`: I-0 … I-4, NUM.
