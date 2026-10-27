# Topic P: the Pizer graph as Γ\T_ℓ, its Ihara zeta as the L-polynomial of X₀(p) over F_ℓ, and its label phase space as H¹

Read `notes/astra-2026-10-27/brief.md` first (binding). Steer: lattice, symplectic form, map or identity; never an overlap. The record's deep
version of this topic is the LPS/Shimura-curve route (`report/sections/04u_deninger_lps.tex`, `04z_cerednik_drinfeld.tex`, genus 721 at
(13, 17; 5)); this topic is its elementary cousin, with elliptic curves and X₀(p), and must be exact and fully checked at small p.

## 0. The setting

p, ℓ distinct primes. S_p = the set of supersingular j-invariants in F_{p²} (every supersingular curve is defined over F_{p²}; #S_p = ⌊p/12⌋ + {0, 1, 1, 2}
for p ≡ 1, 5, 7, 11 mod 12; from memory, Silverman AEC V.4). For E_i, E_j ∈ S_p the **Brandt matrix** B(ℓ)_{ij} = #{subgroups C ⊂ E_i of order ℓ
with E_i/C ≅ E_j} (row sums ℓ + 1). Weights w_i = |Aut(E_i)|/2 ∈ {1, 2, 3}; w_i = 1 for all i iff p ≡ 1 mod 12. When all w_i = 1, B(ℓ) is symmetric
and is the adjacency matrix of the (ℓ+1)-regular **Pizer graph** G(p, ℓ) (loops and multiple edges allowed; a loop counts as in B(ℓ)). The record's
graph conventions (`notes/astra-2026-10-23/brief.md`): ζ_Y(u) = det(1 − uB_{Hashimoto})^{-1} = (1 − u²)^{−(|E|−|V|)} det(1 − Au + ℓu²)^{-1}; label
step M = ((A, −ℓ), (1, 0)) on Z^{2n}, M^T Ω M = ℓΩ, Weil form ½Ω(M − V). For a multigraph with loops state the Hashimoto operator you use and
check Ihara–Bass numerically for it (a loop is an oriented edge pair e, ē with the same endpoints — say whether the convention makes
det(1 − uB) = (1 − u²)^{|E|−|V|} det(1 − Au + ℓu²) still hold; it does for multigraphs without loops; for loops the "+ ℓu²" needs
(D − 1) = ℓ on every vertex which still holds if a loop contributes 2 to the degree — settle this and PRINT the check).

Quaternion side: B_{p,∞} the definite quaternion algebra over Q ramified at p and ∞; O a maximal order; End(E_i) ≅ O_i are the maximal orders in
the class set of O (Deuring; from memory); the class number h(O) = #S_p. Modular side: X₀(p), genus g = #S_p − 1 (true for all p: g(X₀(p)) =
⌊(p+1)/12⌋ − {0 or 1 corrections}; verify), J₀(p) its Jacobian, S₂(Γ₀(p)) of dimension g, every form new, with Hecke eigenvalues a_ℓ(f).
The **Eichler/Deuring theorem** (basis problem; Eichler 1955, Pizer 1980 "An algorithm for computing modular forms on Γ₀(N)", Gross 1987
"Heights and the special values of L-series" §§1–5; from memory): the Brandt matrices B(n) acting on the Brandt module Z[S_p] are the Hecke
operators T_n on M₂(Γ₀(p)) = C·Eis ⊕ S₂(Γ₀(p)) as Hecke modules; the Eisenstein line is the vector (1, …, 1) (or (1/w_i) depending on which side
B acts on — settle), eigenvalue ℓ + 1. **Eichler–Shimura** (from memory): for ℓ ≠ p, the L-polynomial of X₀(p) over F_ℓ is P_{p,ℓ}(u) =
∏_{f ∈ newforms of S₂(Γ₀(p)), over all Galois conjugates} (1 − a_ℓ(f) u + ℓ u²), i.e. Frob_ℓ on H¹(X₀(p)) has characteristic polynomial given by
the T_ℓ eigenvalues (Eichler–Shimura relation T_ℓ = Frob + Ver on J₀(p) mod ℓ).

## 1. Items, in order of priority (prove or refute; every number printed by a script in `checks/`)

P1 (the Ihara zeta of the Pizer graph is the reciprocal L-polynomial of X₀(p) mod ℓ). PROVE, from the cited theorems and with every
normalisation explicit (weights w_i, the symmetrisation of B(ℓ), the trivial eigenvalue): for p ≡ 1 mod 12,
    det(1 − B(ℓ) u + ℓ u²) = (1 − u)(1 − ℓu) · P_{p,ℓ}(u),
hence ζ_{G(p,ℓ)}(u) = (1 − u²)^{−(|E|−|V|)} / [(1 − u)(1 − ℓu) P_{p,ℓ}(u)], and P_{p,ℓ} is the numerator of the Hasse–Weil zeta of X₀(p) over F_ℓ. For
general p state the weighted version (the symmetrised matrix W^{1/2} B W^{−1/2} or the Hecke action on Z[S_p] with the pairing ⟨e_i, e_j⟩ = w_i δ_ij)
and what graph, if any, it is the Ihara zeta of. COROLLARY: G(p, ℓ) is Ramanujan because |a_ℓ(f)| ≤ 2√ℓ, which for weight 2 is **Weil's RH for the
abelian variety J₀(p) over F_ℓ** (no Deligne needed); say this precisely. CHECK (the central numerical content): build G(p, ℓ) directly over F_{p²}
from the modular polynomial Φ_ℓ (PARI `polmodular(ℓ)`, roots of Φ_ℓ(X, j_i) over F_{p²}, with the supersingular j found by the Hasse invariant or by
`ellissupersingular`), for p ∈ {37, 73, 109} (all ≡ 1 mod 12; #S_p = 3, 6, 9) and ℓ ∈ {2, 3, 5, 7}; print B(ℓ), its eigenvalues, and compare with
the eigenvalues a_ℓ(f) from `mfinit([p, 2], 1)` / `mfeigenbasis` / `mfcoefs` (the eigenvalues over the number fields K_f: compare characteristic
polynomials over Z exactly, not floats); verify Ihara–Bass for the multigraph, and verify |a_ℓ| ≤ 2√ℓ. Then the weighted case p = 101 (#S_p = 9, one
j with w = 3) and p = 37 is fine; also p = 11 (#S_p = 2, w = (2, 3)... check) as the smallest. PRINT also the count #X₀(p)(F_ℓ) = ℓ + 1 − Σ_f a_ℓ(f) and
sanity-check it against a direct point count of a model of X₀(p) if PARI gives one easily (e.g. for p = 37, X₀(37) is the genus-2 curve
y² = −x⁶ − 9x⁴ − 11x² + 37 — from memory, verify or find the correct model; `hyperellcharpoly` over F_ℓ gives P_{37,ℓ} directly: match it).

P2 (the Pizer graph is a quotient of the tree by a global lattice). PROVE: for a vertex E ∈ S_p, the Tate module T_ℓ(E) is a self-dual lattice in
V_ℓ(E) = T_ℓ(E) ⊗ Q_ℓ ≅ Q_ℓ² for the Weil pairing e_{ℓ^∞} (a qunaught at ℓ in the sense of topic T), and an ℓ-isogeny φ: E → E' identifies V_ℓ(E) ≅ V_ℓ(E')
and sends T_ℓ(E) onto an index-ℓ sublattice of T_ℓ(E'); the ℓ + 1 neighbours of E in G(p, ℓ) are the ℓ + 1 index-ℓ superlattices of T_ℓ(E), the
neighbours of [T_ℓ(E)] in the tree T_ℓ. Then PROVE the global statement (from memory; Serre, Pizer, or the "supersingular isogeny graphs are Ramanujan"
literature): G(p, ℓ) ≅ Γ\T_ℓ with Γ = O[1/ℓ]^× / Z[1/ℓ]^× acting on T_ℓ through O ⊗ Q_ℓ ≅ M₂(Q_ℓ), when h(O) = 1 (p ∈ {2, 3, 5, 7, 13}); for general p
derive the correct statement from strong approximation for B¹ (which holds since B is split at ℓ): is G(p, ℓ) = Γ\T_ℓ for the Γ attached to one order
O, a disjoint union over the class set, or a quotient by the parity of the reduced norm (two colours ↔ norm ∈ ℓ^{2Z} versus ℓ^{2Z+1})? Give the exact
statement with proof, and CHECK it on p = 37 (h = 3): compute the orders/ideal classes with PARI (`alginit` for the quaternion algebra of discriminant
37, `algmaximal`? — or avoid PARI's algebra package and use the Brandt-matrix identity B(ℓ) = ⟨ideal classes, ℓ-neighbours⟩ computed from a
reduced norm form: the theta-series route of Pizer; choose the route you can make exact) and compare the resulting graph with the Φ_ℓ graph of P1.
If strong approximation gives only the weaker "connected and covered by the tree", say so.

P3 (the label phase space is H¹ of X₀(p): how exactly). The label space Z^{2n}, n = #S_p = g + 1, with Ω and M = ((B(ℓ), −ℓ), (1, 0)) (for p ≡ 1 mod 12),
has 2g nontrivial modes (eigenvalue pairs μ, ℓ/μ per newform conjugate) and the trivial pair ℓ, 1 (λ = ℓ + 1). PROVE: the characteristic polynomial of M on
the nontrivial part is u^{2g} P_{p,ℓ}(1/u), so (nontrivial label space ⊗ Q, M) ≅ (H¹(X₀(p) ⊗ F̄_ℓ, Q_λ)-type, Frob_ℓ) as modules over Q[M] — i.e. the
graph's phase space **is** H¹ of the modular curve rationally, with M = Frobenius at ℓ and the Weil form ½Ω(M − V) positive iff Weil's theorem. Then the
integral question (OPEN in the record; `data-ladder.md` §1 items 2–3: counts fix the isogeny class, not the lattice): (a) compute the Smith normal
form of (1 − M^k) on the nontrivial label sublattice for k = 1, 2, 3 (define that sublattice integrally: the Ω-orthogonal / the saturation of the
kernel of the trivial-mode projection — state which, and whether the trivial mode splits off integrally; tutorial §6 says the labelling (f,g) ↦ σf + τg
has kernel (1, −1) on the trivial line) and compare with #J₀(p)(F_{ℓ^k}) = P-based count ∏(1 − α^k) — equality of orders is forced by P1; the content is
the **group structure**. (b) For p = 37, J₀(37) is isogenous to E₁ × E₂ with E₁ = 37a1 (rank 1, a₂ = −2), E₂ = 37b1 (a₂ = 0) (from memory; verify with
`ellinit("37a1")` if elldata is present, else from the Cremona equations y² + y = x³ − x (37a) and y² + y = x³ + x² − 23x − 50 (37b)); compute
E₁(F_{ℓ^k}) × E₂(F_{ℓ^k}) as abstract groups (`ellgroup`) and compare with the Smith forms of (a). State what agreement or disagreement means (the
label lattice is / is not the product lattice; J₀(37) itself is not E₁ × E₂ but isogenous to it; which lattice in the isogeny class the graph picks is
the question of `data-ladder.md` §1.2 — the record's lane F found that overlaps see only the order; here the graph is a different source of a lattice).
(c) Is Ω on the label lattice the Weil (intersection) pairing on H₁(X₀(p), Z) up to the trivial mode? State the obstruction or the identification
(Gross's pairing ⟨e_i, e_j⟩ = w_i δ_ij on Z[S_p] against the intersection pairing — from memory, Gross 1987 §3 and Ribet's work relate Z[S_p] to the
component group of J₀(p) at p and to H₁; cite what you use and label it from memory). Label (c) SKETCHED if that is what it is.

P4 (what this says for ζ; short, one paragraph each, labelled HEURISTIC unless proved). (i) In the language of the adelic lattice: vertices of G(p, ℓ)
are B^×(Q)\B^×(A_f)/Ô^×, "rational points modulo an adelic compact", the symplectic geometry sits in B_ℓ^× = GL₂(Q_ℓ) acting on lattices of Q_ℓ²;
for G_m over Q the same double coset Q^×\A_f^×/Ẑ^× is a point and the tree at ℓ is a line. Make this comparison exact (one displayed line each) and
state what it says about the absence of a finite-rank H¹ for ζ. (ii) The "two meanings of qunaught" (the local T_ℓ(E) ⊂ V_ℓ(E) at a vertex, and the
global label lattice Z^{2n} ⊃ nontrivial part ≅ H₁(J₀(p), Z) up to isogeny) are one object on this topic: say in which sense (the Tate module of the
Jacobian is the ℓ-adic completion of the global lattice), and whether that identification is compatible with the two symplectic forms.

## 2. Correction ledger and ambition

If any statement of §0 is wrong (the count #S_p, the weights, the genus formula, Eichler–Shimura's exact form, the model of X₀(37), the Cremona
labels), say so in the ledger and use the correct one. Ambition: P1 exact with the numerical table, P2 exact for all p, P3(a)–(b) computed and
interpreted; P3(c), P4 are stretch.

## 3. Output

`<family>-proofs.md`: §1 P1, §2 P2, §3 P3, §4 P4, correction ledger, "Numerical checks for the blind lane", "What this changes in the notebook"
(candidate rows, e.g. `thm:pizer-ihara-zeta-x0p`, `prop:pizer-tree-quotient`, `prop:pizer-label-space-h1`, `num:pizer-label-lattice-smith`; one-line
annotations for `graph-ihara.md` §2–§3 (the K₄/E coincidence versus this exact identity), `data-ladder.md` §0 (a new rung: the Pizer graph), §1.2).
`progress.txt`: P1, P2, P3a, P3b, P3c, P4, NUM. Scripts `checks/pizer_graph.py` (P1 table), `checks/pizer_quotient.py` (P2), `checks/label_lattice.py`
(P3), outputs `checks/output_*.txt`.
