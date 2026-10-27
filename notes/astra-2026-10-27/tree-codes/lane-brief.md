# Topic T: the tree as the space of local GKP codes, and the Ihara zeta as the zeta of the squeezes

Read `notes/astra-2026-10-27/brief.md` first (binding). Steer: lattice, symplectic form, map or identity; never an overlap.

## 0. The setting (fix it exactly as written; p an odd prime throughout unless an item says otherwise)

V = Q_p², ω(x, y) = x₁y₂ − x₂y₁, ψ_p(x) = exp(2πi {x}_p) (trivial on Z_p). Weyl operators on L²(Q_p): W(u, v)f(x) = ψ_p(vx) f(x + u), with
W(u,v)W(u',v') = ψ_p(ω((u,v),(u',v'))) W(u',v')W(u,v) (`adelic-gkp.md` §1, local version). A *lattice* L ⊂ V is a free Z_p-module of rank 2
(L = gZ_p², g ∈ GL₂(Q_p)); its dual is L^⊥ = {x ∈ V : ω(x, L) ⊂ Z_p}. The tree T_p: vertices are homothety classes [L] (L ~ cL, c ∈ Q_p^×),
[L] ~ [L'] adjacent iff representatives satisfy pL ⊂ L' ⊂ L with [L : L'] = p; it is (p+1)-regular (standard: Serre, *Trees*, II.1). PGL₂(Q_p)
acts by g·[L] = [gL]. The squeeze D_a f(x) = |a|_p^{1/2} f(ax), a ∈ Q_p^×, satisfies D_a W(u,v) D_a^{-1} = W(a^{-1}u, av) (note §2, Prop. 2):
it is the symplectic map diag(a^{-1}, a) of V. GKP code of a lattice L with L ⊂ L^⊥: the joint eigenspace of {W(λ) : λ ∈ L} (fix a phase
convention making λ ↦ W(λ) a representation on L; for p odd use W̃(u,v) = ψ_p(−uv/2) W(u,v), which is a true representation of V restricted to
any isotropic lattice — prove this or use another convention and state it); its dimension is [L^⊥ : L]^{1/2}. "Qunaught" = code of dimension one =
self-dual lattice L = L^⊥, with state 1_L-type vector (for L = Z_p² the state is 1_{Z_p}).

Record conventions for graphs: `notes/astra-2026-10-23/brief.md` "Conventions" (Ihara zeta ζ_Y(u) = det(1 − uB)^{-1}; the label step M on
(f, g) ∈ Z^{2n} with M^T Ω M = qΩ; the Weil form ½Ω(M − V), V = qM^{-1}). Γ ⊂ PGL₂(Q_p) discrete, cocompact, torsion-free and acting without
inversions, so that Y = Γ\T_p is a finite (p+1)-regular graph (Ihara's setting; Ihara 1966, Serre *Trees* II.1.5, from memory).

## 1. Items, in order of priority (prove or refute; every number printed by a script in `checks/`)

T1 (colours are code dimensions). PROVE: for every lattice L = gZ_p², L^⊥ = (det g)^{-1} L. Hence, up to homothety, every vertex of T_p has a
representative with L ⊂ L^⊥ and [L^⊥ : L] = p^{2k}, k ∈ {0, 1}, k ≡ v_p(det g) mod 2, and the bipartition of T_p by k is: k = 0, the
**qunaught vertices** (self-dual lattices, one-dimensional codes); k = 1, the **qudit vertices** (lattices with [L^⊥ : L] = p², codes of one
p-dimensional qudit). State precisely which representative in the homothety class is meant and why the code is independent of that choice
(up to a canonical isomorphism / scaling by D_c).

T2 (neighbours are MUB axes). Let M be a qudit vertex (M ⊂ M^⊥, [M^⊥ : M] = p²). PROVE: the self-dual lattices L with M ⊂ L ⊂ M^⊥ are exactly
the p + 1 neighbours of [M] in the tree, they are in bijection with the lines of the symplectic F_p-plane M^⊥/M, and for each such L the p states
W(λ)1_L, λ ∈ M^⊥/L ≅ F_p, form an orthonormal basis of the code space C_M ≅ C^p; the p + 1 bases so obtained are mutually unbiased
(|⟨b, b'⟩|² = 1/p across bases). Identify them with the standard MUBs of the Weyl–Heisenberg group over F_p (computational basis and the p
quadratic-phase bases). Dually: the p + 1 neighbours of a qunaught vertex [L] are the index-p sublattices M ⊂ L, i.e. the lines of L/pL, and
1_L lies in each of their codes. CHECK numerically for p = 3, 5, 7: build C_M as functions on Z_p/pZ_p (say which representative M), list the
p + 1 bases, print all cross-basis |⟨b,b'⟩|² and the within-basis Gram matrices.

T3 (geodesics are pairs of transverse Lagrangians; translation is the squeeze). PROVE: the ends of T_p are P¹(Q_p), the set of lines (= Lagrangian
subspaces) of V; a bi-infinite geodesic is a pair of distinct lines ℓ₁ ≠ ℓ₂, and its vertices are exactly the classes of the lattices split by
(ℓ₁, ℓ₂): L = (L ∩ ℓ₁) ⊕ (L ∩ ℓ₂) — in a symplectic basis (e₁ ∈ ℓ₁, e₂ ∈ ℓ₂) these are L_{a,b} = p^a Z_p e₁ ⊕ p^b Z_p e₂, [L_{a,b}] depending on
b − a only. The squeeze diag(a^{-1}, a) with v_p(a) = m translates this geodesic by 2m steps and fixes no vertex; diag(1, p) (in PGL₂, not in
SL₂) translates by one step and exchanges the colours. PROVE: every hyperbolic element γ ∈ PGL₂(Q_p) (one whose two eigenvalues have different
valuations; eigenvalues then lie in Q_p — prove by the Newton polygon) is conjugate in PGL₂(Q_p) to diag(1, λ) with v_p(λ) = ℓ(γ) ≥ 1 its
translation length, i.e. **every hyperbolic element is a squeeze along its axis, composed with a unit**; the elliptic elements (equal valuations)
fix a vertex or an edge. CHECK: p = 3, 5; for ten random integer matrices classify and print the translation length against the valuation of
the eigenvalue ratio, and verify on the tree by explicit lattice reduction (Hermite form) that the axis vertices are the split lattices.

T4 (the Ihara zeta of Γ\T is the zeta of the squeezes in Γ, and its orbit terms are local Lefschetz traces). With Y = Γ\T_p finite as in §0:
(a) PROVE (Ihara's theorem, from memory, in this language): closed non-backtracking walks of length k in Y ↔ Γ-conjugacy classes of hyperbolic
γ ∈ Γ with ℓ(γ) = k, counted with the right multiplicity (state it), so ζ_Y(u) = ∏_{[γ] primitive hyperbolic} (1 − u^{ℓ(γ)})^{-1}, the Euler product
over the primitive squeezes of Γ. (b) PROVE the orbit term identity. The explicit formula of `graph-ihara.md` §5 for a non-bipartite Y has, on
the non-uniform lines, the orbit term +ℓ q^{−mℓ/2} at k = mℓ for each prime cycle of length ℓ. The distributional trace of D_a on L²(Q_p) is
Tr D_a = |a|_p^{1/2} / |1 − a|_p (Lefschetz at the fixed point 0; `adelic-gkp.md` §10 sketches it — PROVE it: compute ∫ |a|^{1/2} δ((a−1)x) dx
rigorously as a distribution pairing, or via the kernel of D_a on a test function). Show: for the hyperbolic γ ~ diag(1, λ) of a prime cycle of
length ℓ, the squeeze part of γ is D_{λ^{±1}} and |λ|_p^{1/2}/|1 − λ|_p = p^{−ℓ/2} (the term's weight), so that **the orbit side of the graph's
explicit formula is Σ over primitive hyperbolic classes of ℓ(γ₀) × (p-adic Lefschetz trace of the squeeze of γ^m)**, with ℓ(γ₀) the length of the
primitive element as the volume of the centraliser Γ_γ\⟨γ⟩. Say exactly which normalisation makes the graph's +ℓq^{−mℓ/2} and Connes's local
term at p (`log p · p^{−k/2}` kicks for ζ) the same formula, and where the sign (+ for the graph, − for ζ: bright versus dark lines,
`graph-ihara.md` §5) enters. (c) CHECK on a graph of the form Γ\T_p: the smallest honest example you can build — e.g. p = 5 with Γ from the
LPS construction (Hamilton quaternions, X^{5,q} for a small q with PGL₂(F_q) vertices; q = 13 gives 2184 vertices; or use any (p+1)-regular
Cayley graph of PGL₂(F_q) with the standard LPS generators), or p = 3 with a known arithmetic Γ — and for it (i) count closed non-backtracking
walks N_k from B for k ≤ 8, (ii) count primitive cycle classes by lengths from Ihara–Bass, (iii) verify the explicit formula with the orbit
weights of (b) against the spectrum of A to machine precision. If building an arithmetic Γ\T is too costly, use any (p+1)-regular graph for
(i)–(iii) (the identity is a theorem for every finite regular graph) and say so; the arithmetic example is the stretch.

T5 (OPEN target; attempt only after T1–T4 are written). The label phase space of `graph-ihara.md` §4 is two numbers per vertex; per adjacency
eigenvalue λ = √p(μ + μ^{-1}) the invariant plane is spanned by the two Satake parameters μ, p/μ. On the tree, the eigenfunctions of the vertex
Laplacian with parameter μ are Poisson transforms from the boundary P¹(Q_p) of the characters |·|^{s} with μ = p^{−s+1/2}... (fix the
normalisation). PROVE or REFUTE: the symplectic form Ω on the label space, restricted to the λ-eigenplane, is (a constant times) the pairing
between the Poisson transforms with parameters μ and p/μ given by the standard intertwining operator / the Casoratian of the radial recurrence
f_{k+2} = λ f_{k+1} − p f_k on the tree (tutorial §6: Ω is the Casoratian). If PROVED, state what the Weil form ½Ω(M − V) is on the boundary P¹(Q_p):
the result should be a positivity of a form on functions on the Lagrangian Grassmannian of V. If you get only a sketch, label it SKETCHED.

## 2. Correction ledger and ambition

If any of T1–T4 is false as stated (e.g. the colour parity, the MUB claim, the normalisation in T4(b)), say so in the first line of the item,
give the smallest counterexample with its script, and state the corrected statement. Ambition: T4(b)–(c) and T5 are the new content; T1–T3 are
the dictionary that makes them exact.

## 3. Output

`<family>-proofs.md`: §1 T1, §2 T2, §3 T3, §4 T4, §5 T5, correction ledger, "Numerical checks for the blind lane", "What this changes in the
notebook" (candidate rows, e.g. `prop:tree-colours-code-dimension`, `prop:tree-neighbours-mub`, `prop:geodesic-squeeze`, `thm:ihara-zeta-squeeze-lefschetz`;
one-line annotations for `graph-ihara.md` §2(b) and §5, `adelic-gkp.md` §10). `progress.txt`: T1, T2, T3, T4a, T4b, T4c, T5, NUM. Scripts
`checks/tree_codes.py` (T1–T3), `checks/mub.py` (T2), `checks/ihara_lefschetz.py` (T4), outputs `checks/output_*.txt`.
