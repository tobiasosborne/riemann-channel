# Cerednik–Drinfeld audit of the (13,17;5) complex

Author: `codex:gpt-6-astra`

| Claim | Verdict | Statement to audit |
|---|---|---|
| CD1 | SHARPENED / PROVED | The connected genus-721 object over Q is the w₁₃ quotient; the usual level curve has two geometric components. |
| CD2 | PROVED / SHARPENED | X₁₃=H₁(Y,Z), monodromy M=ZᵗZ, det M=2²¹⁷3⁹²5³³·7; this component group is not killed by T₁₇−18. |
| CD3 | REFUTED / SHARPENED | Whole-curve Frobenius polynomial and a noncanonical companion realization hold; the proposed global toric splitting and canonical paired identification do not. |
| CD4 | REFUTED / SHARPENED / OPEN | Degrees enter normalized period formulas; no canonical Petersson pullback or universal equality of raw norm ratios with degrees is supplied. |
| CD5 | SHARPENED / OPEN | A whole curve and a geometric coefficient metric are obtained; canonical paired comparison, CP realization and the GL₁ analogue remain open. |

This audit is written incrementally; the progress file is the explicit exception requested in the durability instructions.


## Source audit and conventions

Author: `codex:gpt-6-astra`

The predecessor's B1–B7 and correction ledger, the 50-check blind report, the reconstruction script, the worked example, and the manuscript's Theorem 5.2, Definition 6.1, Theorem 6.2 and Proposition 9.3 are inputs, not substitutes for the arithmetic comparison below. Denote the **square complex** by S, its horizontal **graph** by Y, and the **curve constructed below** by C. In particular H¹(S)=0, H¹(Y,R) has dimension 721, and H¹(C) has dimension 1442. These are three different cohomologies.

The requested case-insensitive searches of `refs/src` returned **no occurrence of `cerednik`, `čerednik`, `monodromy pairing`, or `ribet`**. The `drinfeld` hits largely concern function-field Langlands or quantum groups, not this uniformization. Representative byte quotations:

* `refs/src/1012.3223/main.tex:971`: “This conjecture was proven by Drinfel\cprime d in the function field case”. This is the Ramanujan statement, not Cerednik–Drinfeld.
* `refs/src/2603.26443/final_draft.tex:2091`: “as a consequence of Drinfeld's proof of the Langlands correspondence”. Again a different theorem.
* `refs/src/1412.3327/main.tex:126`: “the Ihara zeta function for a finite arithmetic quotient of a Bruhat-Tits tree equals the Hasse-Weil zeta function of the corresponding Shimura curve.”
* `refs/src/1303.6848/main.tex:154`: “the Ihara zeta function for a finite graph equals the Hasse-Weil zeta function of the corresponding Shimura curve.”
* `refs/src/2411.15489/main.tex:325`: “equals to the Hasse-Weil zeta function of the corresponding Shimura curve”; line 329 repeats this in a comment.
* `refs/src/2302.08850/sn-article.tex:169` and `refs/src/1402.4759/main.tex:184` say “equals the non-trivial part of the Hasse-Weil zeta function”.
* `refs/src/math/0407509/main.tex:170`: “this formula allowed Ihara to relate $Z(u)$ to the Hasse-Weil zeta function”.
* `refs/src/1307.3851/main.tex:1978` has only a commented bibliography item, “Shimura curves over finite fields and their rational”.

The unqualified equalities in these introductions are **not** an exact level, dual-graph, or pairing theorem; in particular they cannot erase the distinction between the bad prime 13 and the good prime 17, or between reciprocal graph determinants and curve numerators. All external arithmetic inputs below are **not byte-cited** to the repository. Online primary-source links are locators, not claims that their contents occur in `refs/src`.

## CD1 — SHARPENED: specify the curve, including its ramified-prime quotient

### 1. Levels and the cited uniformization theorem

**PROVED, external input (not byte-cited).** Cerednik (1976), Drinfeld (1976), in the prime-to-p level form explained by Boutot–Carayol (1991): interchange the invariants at p and infinity of an indefinite rational quaternion algebra ramified at p. The formal completion at p of its Shimura curve, with maximal-order-unit level at p, is uniformized by the Drinfeld formal half-plane for the resulting definite algebra, with its height parity and prime-to-p adelic level. Geometric dual graphs are the corresponding tree quotients with height parity. Weil descent is the unramified Frobenius twist by w_p; quotienting by w_p removes this twist. For a torsion-free action without inversions, components are projective lines and node equations are xy=p. Kurihara (1979) and Jordan–Livné (1985; 1987; 1999) describe this graph/descent formulation and its quotients. [Boutot–Carayol (1991)](https://smf.emath.fr/publications/uniformisation-p-adique-des-courbes-de-shimura-les-theoremes-de-cerednik-et-drinfeld), [Jordan–Livné, §1](https://arxiv.org/pdf/math/9802136).

Use B=(-1,-1)_Q, ramified at {2,∞}, with Hurwitz maximal order O. Set G=PB×. For the level away from 13 use exactly

\[
U_2=\operatorname{im}(1+2O_2),\quad
U_5=\ker(\operatorname{PGL}_2(\mathbf Z_5)\to\operatorname{PGL}_2(\mathbf F_5)),\quad
U_r=\operatorname{PGL}_2(\mathbf Z_r)\quad(r\ne2,5,13).
\]

At 5 this is **projective principal** level: in B× it is represented by Z₅×(1+5M₂(Z₅)), not an unspecified full symplectic Γ(5) marking. At 2 retain the stated subgroup, not all maximal-order units.

Let B′ be ramified at {2,13}, and identify its finite local algebras with B away from 13. Let **C₀** be the canonical (possibly geometrically disconnected) Shimura curve with those projective levels and

\[
V_{13}^0=\operatorname{im}(O_{B',13}^{\times}).
\]

It has a rational involution w₁₃ given adelically by a uniformizer of B′₁₃. Define

\[
\boxed{C=C_0/\langle w_{13}\rangle.}
\]

Equivalently use the compact open subgroup V₁₃=PB′×(Q₁₃), containing V₁₃⁰ with index two. In B′× this notation means quotient by the center and the extra normalizer action; it is not the usual maximal-order-unit level. This explicit quotient is essential to the answer over Q.

### 2. The actual uniformizing group

The arithmetic group for one half-plane quotient is

\[
\Lambda=\{[b]\in PB^\times(\mathbf Q):[b]_r\in U_r\text{ for every }r\ne13\}.
\tag{1}
\]

It is the predecessor's Λ₁₃(5), **not** the product-lattice group Γ(5). Before imposing U₅ write Λ₁₃=⟨[S₁₃]⟩. The primary-lattice theorem used in B1, and the class-set computation in B3, identify (1) with ker(Λ₁₃→PGL₂(F₅)). In B× one can use the projective images of primary elements of O[1/13]× with scalar reduction at 5. “Norm a power of 13” alone omits the primary condition at 2.

For clarity, the projective adelic version of the cited formal uniformization in this case is

\[
\widehat{C_0}_{\breve{\mathbf Z}_{13}}
\simeq G(\mathbf Q)\backslash\left(
\widehat\Omega_{13,\breve{\mathbf Z}_{13}}\times\mathbf Z/2\mathbf Z
\times G(\mathbf A_f^{(13)})/U^{(13)}\right).
\]

Here the breve denotes completion of the maximal unramified extension. An element b acts on the first factor through b₁₃, adds v₁₃(Nrd b) to the height modulo two, and acts on the last factor by left multiplication. Descent Frobenius applies coefficient Frobenius and adds one to height; w₁₃ adds one to height without coefficient Frobenius. There is one orbit of the last factor: its orbit set is the connected-component set of the horizontal adelic graph, and that graph is connected by (2). Choosing its representative 1 leaves precisely the stabilizer Λ in (1). This is the explicit level-sensitive version of the theorem being used, including the otherwise easily lost height factor.

Here is the parity check, which also handles descent. A representative of any [b] in (1) may be centrally scaled so its norm is 13ⁿ and it is a unit away from 13. Scalar reduction at 5 forces 13ⁿ to be a square mod 5. Since (13/5)=−1, n is even. Thus **Λ already preserves the two tree types**; its even-norm subgroup is Λ itself. Meanwhile Λ₁₃ is transitive on tree vertices and maps onto the 120-element PGL₂(F₅). Consequently

\[
Y=\Lambda\backslash\mathcal T_{14},\qquad
|V(Y)|=120,  |E(Y)|=840,  b_1(Y)=721.
\tag{2}
\]

The bipartition is ε(g)=(det g/5); each side has 60 vertices. This proves the identification with the specific Cayley graph, not merely an isospectral graph.

### 3. Why the usual curve has two copies, and the quotient has one

For C₀ the global geometric graph is the **bipartite double cover** Y†: vertices (g,s), s∈{+,-}, and an edge from (g,+) to (gφ(a),−) for every directed horizontal edge (g,a) of Y. Thus

\[
|V(Y^\dagger)|=240,\quad |E(Y^\dagger)|=1680.
\]

Because Y is already bipartite, this cover is **disconnected**:

\[
Y^\dagger=Y_+\sqcup Y_-,\qquad
Y_\delta=\{(g,s):s\,\varepsilon(g)=\delta\},\quad Y_\delta\simeq Y.
\tag{3}
\]

This is also obtained directly from the half-plane times height-parity uniformization: Λ acts trivially on height parity, leaving two connected half-plane quotients. In the vertex-class coordinates of (3), w₁₃ sends (g,s) to (g,−s). It exchanges the connected components, so acts freely on the entire geometric curve. Its quotient has graph exactly Y, with no further quotient of its 120 vertices and no new thicknesses.

For completeness the component field is Q(√5). Shimura's connected-component reciprocity theorem (canonical models, 1971; **not byte-cited**) identifies components with the positive reduced-norm idele class quotient; Galois acts by Artin reciprocity. In this level that quotient has order two: the only unit norm restriction is the square class at 5. At 2 the norm of 1+2O₂ is all Z₂×: it contains square units and the square classes represented by N(1+2i)=5 and N(2+i+j+k)=7. At 13 the usual O× level contributes units. The nontrivial component character is therefore η₅. Both 13 and 17 have η₅=−1. The local uniformizer w₁₃ exchanges the components, exactly as (3) says.

Hence C₀ splits into its two genus-721 components over the unramified quadratic extension of Q₁₃, with Frobenius exchanging them. Its individual component is not the asserted Q-curve with an internal T₁₇ correspondence: T₁₇ also exchanges the two components. By contrast **C is geometrically connected over Q and is split Mumford-uniformized over Q₁₃ itself**:

\[
C_{\mathbf Q_{13}}^{\rm an}\simeq\Lambda\backslash\Omega_{13}.
\tag{4}
\]

The Frobenius twist disappears on the w₁₃ quotient. “Two sides of a bipartite graph” are sets of irreducible components inside one connected special fibre; they are not its two connected components. The two copies in (3) are an additional, different doubling.

### 4. Stabilizers, genus, and the reversal sign

The primary lattice acts freely on vertices and is a free group; Λ is its subgroup. There are no effective projective vertex stabilizers, torsion, or edge inversions. The central automorphisms ±1 have already been removed; they do not introduce a factor of two in node thickness. Thus the quotient of the Drinfeld model has **120 smooth rational components and 840 ordinary double points, all of thickness one**. Each component meets 14 others; the model is stable as well as regular semistable. Its arithmetic genus is Σg(component)+b₁(Y)=721. The *generic fibre* is a Mumford curve; the singular special fibre is a union of rational curves, not itself a smooth Mumford curve.

Write X₁₃=H₁(Y,Z) and K=X₁₃⊗R. Identifying chains and cochains by the unit edge metric identifies K with the harmonic representatives of H¹(Y,R). Integrally H¹(Y,Z)=Hom(H₁(Y,Z),Z), not canonically the same lattice via a unimodular form; CD2 computes the obstruction.

Orient every edge of Y† from its + side to its − side. Its harmonic cochains form the predecessor's directed newspace N, with dim N=1442. On these oriented chains w₁₃ acts as **−R**, where R reverses the underlying edge of Y. Therefore

\[
H_1(Y^\dagger,\mathbf Q)^{w_{13}=+1}=N_{R=-1}=K_{\mathbf Q}.
\tag{5}
\]

This is the precise geometry of the predecessor's Steinberg sign: local Jacquet–Langlands sends St⊗χ at 13 to χ∘Nrd on B′₁₃×; V₁₃-invariance forces χ(13)=+1. Reversal is −χ(13), while the involution on curve cohomology is +χ(13). Multiplication by ε(tail) exchanges N₋ and N₊ and anticommutes with T₁₇. Thus the discarded w₁₃=−1 piece has the reflected T₁₇ spectrum; it is not the second copy in Bass doubling.

**CD1 verdict.** The brief's bare “X_{B′}(5)” is insufficient and, interpreted as the full usual adelic level curve, has twice the geometric graph and cohomology. The explicit w₁₃ quotient C supplies the requested whole genus-721 Q-curve, with precisely Y as its dual graph. Alternatively one may work with a connected component of C₀ over Q(√5), but then must descend and specify the component-switching Hecke action; simply calling it the same Q-curve is incorrect.


## CD2 — PROVED for C: the cycle metric is the monodromy pairing

### 1. Character lattice, with its integral meaning

**PROVED, external input (not byte-cited).** Raynaud (1970), *Spécialisation du foncteur de Picard*, and Grothendieck, SGA 7 I, Exposé IX (1972): for a proper regular semistable curve over a strictly henselian DVR, normalization of its geometric special fibre gives

\[
1\longrightarrow T\longrightarrow\operatorname{Pic}^0(C_s)
\longrightarrow\prod_v\operatorname{Jac}(\widetilde C_v)\longrightarrow0,
\qquad X^*(T)=H_1(\mathcal G,\mathbf Z).
\tag{6}
\]

Here the character lattice is geometric; descent records the residue-field Galois action. For a principally polarized Jacobian the monodromy homomorphism is the positive integral form

\[
b(c,d)=\sum_{e\in E(\mathcal G)}t_e c_e d_e,
\tag{7}
\]

where xy=π^{t_e}u is the local node equation, v(π)=1; one may use a semistable model with thicknesses instead of resolving each edge into t_e unit edges. Its cokernel is the geometric Néron component group. [Precise graph formulas, Papikian (2005), §4](https://www.numdam.org/item/10.5802/aif.2078.pdf).

One can see the character assertion without a dimension guess: a degree-zero line bundle on a union of rational components is determined by gluing scalars at nodes, modulo changing trivialization on components. Thus T is the quotient of (G_m)^E by the vertex-rescaling torus (G_m)^V/G_m. Taking characters gives ker(∂:Z^E→Z^V). All normalization Jacobians in (6) vanish here, so dim T=721 and J has totally toric reduction. Its **identity component in the special fibre** is a torus; J itself is a proper abelian variety, not that torus.

All t_e=1 by CD1, so in the integral fundamental-cycle basis of the worked example

\[
\boxed{X_{13}=H_1(Y,\mathbf Z),\qquad b(x,y)=x^tMy,\qquad M=Z^tZ.}
\tag{8}
\]

The root-at-identity breadth-first tree and chord order are those of worked-example §6. The old `scripts/lps_square_complex.py` only constructs an orthonormal nullspace (its variable `M` is actually the restricted transport); it does not supply this integral Z. The new permitted scratch script `checks/cycle_checks.py` reconstructs the prescribed Z, with its chord rows equal to I₇₂₁. Hence its columns are an **integral** basis: any integral cycle is uniquely reconstructed from its chord coefficients. This proves M≥I in these coordinates, in particular positivity, without a floating-point eigenvalue test.

### 2. Hecke compatibility and symmetry

Prime-to-13 Hecke correspondences extend through the uniformization theorem, act on the dual graph, and induce the same pull–push on (6). At 17 the two projections are exactly the 18-sheeted correspondence of the square complex: reordering ab=±b′a′ transports the horizontal edge (g,a) to (gφ(b′),a′). It descends to C because w₁₃ commutes with Hecke at 17. Thus the unnormalized T₁₇ action on X₁₃ is the predecessor's T, and in cycle coordinates is **L**, with T₁Z=ZL. Consequently χ_L=χ_T.

Monodromy is functorial for homomorphisms and their polarized duals (Grothendieck, SGA 7 IX, 1972; **not byte-cited**): b_A(f^*x,y)=b_B(x,(f^∨)^*y), with character maps contravariant. For the present trivial-central-character, inverse-stable double coset, the Rosati adjoint of T₁₇ is T₁₇. Therefore b(Tx,y)=b(x,Ty). Finite verification gives the same result independently:

\[
L^tM= (ZL)^tZ=(T_1Z)^tZ=Z^tT_1Z=ML.
\tag{9}
\]

This is an exact geometric interpretation of the **coefficient** inner product and the symmetry of the transverse operator. It does not yet identify an alternating form on a doubled space with the curve's cup product.

### 3. Component group and its computed order

With the principal polarization identifying the character groups of J and J∨, Grothendieck's exact sequence is

\[
0\longrightarrow X_{13}\xrightarrow{\ b\ }
X_{13}^{\vee}:=\operatorname{Hom}(X_{13},\mathbf Z)
\longrightarrow\Phi_{13}(\overline{\mathbf F}_{13})\longrightarrow0.
\tag{10}
\]

Here C has split reduction, so the residue Galois action on graph, lattices and Φ is trivial. Thus the Tamagawa number |Φ₁₃(F₁₃)| equals det M. For C₀ one would instead have two geometric groups exchanged by Frobenius; its total geometric order is (det M)². The notation X∨/X is legitimate only after specifying the injection b; it is not a unimodular identification.

**PROVED (determinant, two exact certificates).** Cauchy–Binet gives

\[
\det(Z^tZ)=\sum_{|S|=721}\det(Z_S)^2=\tau(Y).
\tag{11}
\]

A cycle minor is ±1 precisely when the complementary 119 edges form a spanning tree, and otherwise zero. Equivalently, Kirchhoff's matrix-tree theorem computes τ(Y) as any reduced Laplacian determinant. The graph adjacency spectrum is

\[
\{14,-14,4^{[34]},(-4)^{[34]},2^{[25]},(-2)^{[25]}\}.
\]

The scratch script verifies (A²−196I)(A²−16I)(A²−4I)=0 in integers, connectedness, bipartiteness, tr A²=1680 and tr A⁴=95040; these certify those multiplicities exactly. Thus

\[
\begin{aligned}
\det M
 &=\frac{28\,10^{34}18^{34}12^{25}16^{25}}{120}\\
 &=\boxed{2^{217}\,3^{92}\,5^{33}\,7}.
\end{aligned}
\tag{12}
\]

A separate fraction-free integer Bareiss elimination of the 119×119 reduced Laplacian returns exactly the same integer. This computes the order, not a Smith-normal-form decomposition of Φ.

### 4. What the Eisenstein comparison does, and does not, say

Ribet (1990), *On modular representations of Gal(Qbar/Q) arising from modular forms*, character-group formalism, **not byte-cited**: for distinct p,q, (M,pq)=1, put J′=Jac(X₀^{pq}(M)), J=J₀(Mpq), J″=J₀(Mq)². The two degeneracy maps give the Hecke-equivariant character sequence

\[
0\longrightarrow X_p(J')\longrightarrow X_q(J)
\longrightarrow X_q(J'')\longrightarrow0,
\tag{13}
\]

for the usual Γ₀ levels; away-from-pq Hecke actions agree. The graph description realizes the kernel as cycles of the two-sided quaternionic graph. This is a character-lattice sequence across **different bad primes**, not a decomposition of a single global Tate module. [Ribet's theorem and notation as restated by Ribet–Stein, §3.10](https://wstein.org/papers/serre/ribet-stein.pdf).

Its level-raising use also needs Ihara's lemma: for prime r∤N and residual characteristic ℓ∤Nr, ℓ≥5, the two degeneracy maps on H¹ of modular curves, localized at a non-Eisenstein maximal ideal with irreducible residual representation, inject the two old copies with torsion-free cokernel; the adjoint composite has matrix [[r+1,T_r],[T_r,r+1]] at trivial character. This is the form used in Ribet's level-raising argument (Ihara 1973; Ribet 1990; **not byte-cited**). No such localized theorem is needed to deduce (8)–(12), and its hypotheses must not be silently transferred to our U₂U₅ normalizer quotient.

In particular **REFUTED for this Φ:** the naive prediction that all T_r−(r+1) kill it. There is a finite counterexample already at r=17. Identify the graph critical group with

\[
\Phi\simeq\operatorname{Div}^0(V(Y))/ (14I-A_{13})\mathbf Z^{V(Y)}.
\]

The induced correspondence is A₁₇ on vertex divisors. In the script's lexicographic labels the identity vertex has index 20. Put d=e₀−e₂₀, Q=14I−A₁₃, and solve

\[
Qx=(A_{17}-18I)d,\qquad x_{20}=0.
\]

The exact solution has **x₀=−364/135**, so it is not integral: (T₁₇−18)[d]≠0 in Φ. The script solves this by the exact inverse polynomial on the five nonzero Laplacian eigenspaces, not numerical division. The ordinary Γ₀ modular-component Eisenstein result and the present Shimura quotient are different assertions. Prime factors of (12) alone would not have proved or disproved an Eisenstein-module assertion; the induced action is the test.


## CD3 — distinguish local degeneration from Frobenius at a good prime

### 1. The correct local exact sequence

**PROVED, external input (not byte-cited).** Raynaud (1971), rigid uniformization of abelian varieties, and Grothendieck, SGA 7 IX (1972): a split totally degenerate abelian variety over a complete discretely valued field has analytic uniformization T^an/Π, where Π is a rank-g period lattice. Its polarization identifies Π with the character group of the dual torus. For our principally polarized J and ℓ≠13 this yields, as **G_{Q₁₃}-modules**,

\[
0\longrightarrow X_{13}^{\vee}\otimes\mathbf Z_\ell(1)
\longrightarrow T_\ell J
\longrightarrow X_{13}\otimes\mathbf Z_\ell\longrightarrow0.
\tag{14}
\]

The principal polarization, not an assumption det M=1, identifies the period lattice with X₁₃. The monodromy map b:X₁₃→X₁₃∨ instead describes inertia on this extension. In a chosen abstract splitting, inertia has off-diagonal block t_ℓ(σ)M, up to the fixed sign convention for tame character and Weil pairing. Since M is nonsingular and positive, the rational extension is not split as a G_{Q₁₃}-representation. Analytic ℓ-power torsion gives the analogous exact sequence also for ℓ=13; there the usual ℓ≠13 tame-inertia description is replaced by p-adic semistable comparison.

Bertolini–Darmon (1998), §3, Lemma 3.3 and Proposition 3.4, **not byte-cited**, make the missing data concrete for a Schottky uniformization: a symmetric multiplicative period pairing on Λ^ab defines the discrete lattice in Hom(Λ^ab,G_m), and its valuation is positive definite; quotient by that period lattice is the Jacobian. Their Corollary 4.14 makes the Shimura-curve Hecke action compatible with this toric uniformization. **Valuations alone forget the units of the period matrix.** [Bertolini–Darmon, §§3–4](https://www.math.mcgill.ca/darmon/pub/Articles/Research/17.Heegner-Cerednik/paper.pdf).

**REFUTED.** The toric part of the Néron special fibre is not “Jac(X) itself”. Their dimensions agree, but T has Tate-module rank g, whereas J has rank 2g. Nor is (14) an exact sequence of G_Q-modules: its filtration is attached to the decomposition group at 13. A Frobenius element at 17 need not preserve its toric subspace. There is no global `Frob₁₇ on the 13-special-fibre torus` supplied by this construction. Even at 13, the split local semisimplification has arithmetic-Frobenius eigenvalues 13 on X∨(1) and 1 on X; this is a different bad-reduction statement, not the weight-one good-prime polynomial.

### 2. A whole-curve Frobenius realization does hold, by a different theorem

**PROVED, external inputs (not byte-cited).** Jacquet–Langlands (1970): weight-two cuspidal representations transfer between GL₂ and B′× when the local GL₂ representations at 2 and 13 are discrete series; away from these places the local representations and Hecke eigenvalues agree. The weight-two Eichler–Shimura congruence relation (Eichler 1954; Shimura 1958; Igusa 1959), for modular and quaternionic Shimura Jacobians, gives a two-dimensional Galois constituent with polynomial X²−a_p(f)X+p at each good prime p and trivial central character. It respects level-fixed multiplicities. Weil (1948) gives |α|=√p under every complex embedding for these roots. These are statements about the entire smooth proper curve's étale cohomology, not its bad-fibre graph alone.

For the explicit C, good reduction holds away from {2,5,13}; in particular at 17. Its forms are exactly the predecessor's Π₋: the chosen U₂ and U₅ invariants, St at 13, spherical elsewhere. The quotient V₁₃=PB′×(Q₁₃) removes the nontrivial unramified Steinberg twist. If m_f is the dimension of the chosen level-fixed multiplicity space (all coefficient embeddings included), then Σ_f m_f=721 and, for ℓ≠17,

\[
\boxed{\det(1-u\operatorname{Frob}_{17}\mid V_\ell J)
=\prod_f(1-a_{17}(f)u+17u^2)^{m_f}
=\det(I-uL+17u^2I).}
\tag{15}
\]

Convention: arithmetic Frobenius on the covariant Tate module; equivalently geometric Frobenius on étale H¹. These give the same polynomial, not the same representation without dualization. The Hecke relation on V_ℓJ is F²−T₁₇F+17I=0; “T₁₇ is trace of Frobenius” means a₁₇=α+β on each two-dimensional constituent, not that T₁₇ is itself a Galois element acting on X₁₃.

**New consequence, PROVED:** the worked example's completed rational function is the actual good-reduction zeta function of this explicitly specified quotient curve:

\[
\mathcal Z(u)=Z(C_{\mathbf F_{17}},u)
=\frac{\det(I-uL+17u^2I)}{(1-u)(1-17u)}.
\tag{16}
\]

Thus all its N_n are genuine point counts and its Möbius-inverted primitive exponents count closed points. In particular the printed values predict #C(F₁₇)=0 and #C(F₂₈₉)=11520. This conclusion uses the corrected global curve and the congruence relation; it does not identify individual closed points with the signed square-walk orbits. The signed Ihara quotient remains a different presentation of the same rational function, with its 5760 correction.

### 3. What “the companion realizes Frobenius” can legitimately mean

Put F_B=[[L,−17I],[I,0]]. It satisfies F_B+17F_B⁻¹=diag(L,L) and has the polynomial (15). The finite check gives rank_(F₁₀₃)(T₁²−68I)=840, so ±2√17 are absent even on all edge cochains. Together with Weil's weak bound this proves all quadratic factors have distinct roots. Frobenius is semisimple on each two-dimensional constituent; therefore F_B and Frob₁₇ are isomorphic as **semisimple one-operator Q_ℓ-spaces**. One may prove this by their rational canonical decompositions; over an algebraic closure it is just matching eigenspaces. Choosing such an isomorphism is choosing companion vectors. It is not canonical, does not identify integral lattices, and does not specify the action of G_Q or a Hodge structure.

**REFUTED as the asserted construction.** There is no natural way to take the associated graded of (14), place Frob₁₇ on it, and read off this companion matrix: Frob₁₇ has no induced action on that associated graded unless an extra, generally false, filtration-preservation assertion is supplied. Total degeneracy does not repair this. The corrected conclusion is stronger than the predecessor's unidentified summand at the level of (15)–(16), but no stronger at the level of a canonical companion basis.

### 4. Weil pairing versus Ω_M: the precise comparison and the obstruction

The Weil pairing of the principal polarization is a perfect alternating Z_ℓ(1)-valued form on T_ℓJ. The local toric submodule in (14) is Lagrangian; the induced pairing with the quotient is **evaluation** between X₁₃∨(1) and X₁₃. After choosing a symplectic splitting of the underlying Q_ℓ-vector spaces and a trivialization of the Tate twist, write the split space as X⊕X∨ and its form as

\[
\omega_{\rm ev}((a,\lambda),(a',\lambda'))=\lambda'(a)-\lambda(a').
\]

Pull this form back along (a,b)↦(a,Mb). It is exactly

\[
\Omega_M=\begin{pmatrix}0&M\\-M&0\end{pmatrix}.
\tag{17}
\]

This is the valid **rational, choice-dependent local** meaning of “Weil pairing composed with monodromy”. The pairing on the local graded pieces is canonical; a splitting and the identification of the second copy via M are extra operations. The splitting need not, and generally does not, put the remote-prime Frobenius in companion form.

There is a sharp integral obstruction to the brief's unrestricted equality:

\[
\det\Omega_M=(\det M)^2.
\]

For ℓ∈{2,3,5,7}, Ω_M on X⊗Z_ℓ⊕X⊗Z_ℓ is not perfect, whereas the principal Weil pairing is perfect. No integral change of companion basis can fix that. For other ℓ this discriminant obstruction vanishes, but no canonical simultaneous Frobenius/pairing comparison follows. Over algebraically closed characteristic-zero coefficients one can *choose* a symplectic intertwiner by pairing the α and 17/α eigenspaces; descent of that choice and integral compatibility are separate questions. Thus existence after choices is proved; the claimed canonical construction is **OPEN / unsupported**, and its universal integral form is **REFUTED**.

### 5. What is proved about G_M

**PROVED, algebraically from the geometric coefficient metric.** With b represented by M and T by L,

\[
G_M=\begin{pmatrix}M&-ML/2\\-ML/2&17M\end{pmatrix},
\quad F_B^t\Omega_MF_B=17\Omega_M,
\quad F_B^tG_MF_B=17G_M.
\tag{18}
\]

The Schur complement is M(17I−L²/4), positive exactly when |a|<2√17 for every eigenvalue. This example has that strictness by the preceding modular-rank exclusion plus Weil, or by the predecessor's stronger exact spectral certificate |a|<8. Thus **the worked metric is precisely the Bass metric constructed from monodromy**, with no arbitrary scale on edges. It is not the direct-sum metric diag(M,M), and it is not a metric supplied on T_ℓJ by ℓ-adic polarization (there is no ordering defining positivity over Q_ℓ).

Crucially, positive monodromy and Hecke self-adjointness alone do **not** prove its positivity: on a one-dimensional positive lattice, L=[9] gives 17−81/4<0. The good-prime Weil bound remains an independent input. Monodromy is available at the bad prime; purity is about a good prime.

Finally, in orthonormal coordinates let R=(17I−T²/4)^{1/2}. The worked example's compatible complex structure has

\[
\Omega_B\mathsf J=G\,\operatorname{diag}(R^{-1},R^{-1}),
\]

not G itself. Calling G “the Hodge metric” still requires both a comparison and this spectral normalization. This preserves the predecessor's correction rather than concealing it under the word monodromy.


## CD4 — degrees enter the comparison, but are not the raw ratio of the two norms

### 1. Which eigenline and which level?

**SHARPENED.** A₁₇-eigenspaces are not individual eigenform lines (one has dimension 77). Even after specifying a simultaneous global eigensystem, the level-fixed space can have dimension m_f>1. Fixing a newvector or one elliptic quotient is additional data. At 2 the condition is invariance under U₂ after local Jacquet–Langlands; it is not a declaration that the GL₂ conductor exponent is one. At 5 projective principal level allows several local types. Thus “Γ₀(2·13·25)-type” is not an exact conductor or an exact space of differentials. The individual forms and 2-adic conductors were not identified in the predecessor and are not identified by a₁₇ alone here.

Complex Eichler–Shimura (Eichler 1957; Shimura 1959; **not byte-cited**) identifies holomorphic plus antiholomorphic weight-two differentials with H¹(C(C),C), and pairs differentials by (i/2)∫ω∧barω. It does **not** give a canonical map from the rank-g integral character lattice of a 13-adic torus to the g-dimensional complex space of holomorphic differentials. The canonical principal polarization does not identify its limiting real torus skeleton with complex holomorphic forms. Jacquet–Langlands identifies eigensystems, not the scalar of an arbitrary eigenform comparison; on a compact Shimura curve there is no cusp q-expansion to fix that scalar.

If a Hecke-equivariant comparison j:K_R→a specified real form of the weight-two space is chosen, P=j*⟨,⟩_Pet is a positive Hecke-symmetric form and

\[
G_P=\begin{pmatrix}P&-PL/2\\-PL/2&17P\end{pmatrix}
\]

is another companion certificate. Rescaling j by c_f on a simple eigenspace rescales its ratio to M by |c_f|²; on a multiplicity space the comparison is a matrix. One can choose j to be an isometry, so it is false that two intrinsically specified *different* points of the cone follow just from the existence of the two normed spaces. A normalization can turn their comparison into meaningful arithmetic, but must be part of the statement.

### 2. Exact identities for a specified elliptic quotient

**PROVED.** Let φ:C→E be a nonconstant map, π:J→E its induced quotient, and d=deg φ, so ππ∨=[d]. (If only an optimal quotient is given, define d by this last identity; a map over Q may require a degree-one divisor class.) Suppose E has multiplicative reduction at 13. Let e generate its geometric character group X_E=Z, let n₁₃(E)=v₁₃(Δ_min)=|Φ_E(Fbar₁₃)|, and write

\[
\pi^*e=k v,
\]

where v is primitive on the selected integral character line in X₁₃ and k≥1 is its index. Monodromy functoriality proves

\[
\boxed{k^2 b_J(v,v)=d\,n_{13}(E).}
\tag{19}
\]

Indeed b_J(π*e,π*e)=b_E(e,(π∨)*π*e)=d b_E(e,e), and the elliptic monodromy norm is n₁₃(E). This is an integral statement, including the saturation factor k². For quotients of our split J the multiplicative reduction of E is split, so n₁₃(E) is also its usual Tamagawa number. In general the geometric component number and the number of residue-rational components differ for nonsplit reduction.

For a Néron differential ω_E write A_E=(i/2)∫_{E(C)}ω_E∧barω_E. If φ*ω_E=cη for a chosen differential η on C, ordinary integration over a degree-d map gives the second exact identity

\[
|c|^2\,\|\eta\|_{\rm Hodge}^2=d A_E.
\tag{20}
\]

Thus under the comparison v↦η,

\[
\boxed{\frac{\|\eta\|_{\rm Hodge}^2}{b_J(v,v)}
=\frac{k^2 A_E}{|c|^2 n_{13}(E)}.}
\tag{21}
\]

The degree **cancels** in this normalization. The period area, differential scaling, and lattice index remain. This directly disproves “raw Petersson/monodromy ratio is the degree” as a general identity.

Alternatively take a classical normalized rational newform f, η_f=2πi f(z)dz, and a map φ_mod:X₀(N_f)→the **same E** with φ_mod*ω_E=c_mod η_f. Our convention is ||f||²_Pet=∫|f(z)|²dxdy. Then ||η_f||²=4π²||f||²_Pet, so comparison of (19) with (20) for φ_mod gives

\[
\frac{4\pi^2\|f\|_{\rm Pet}^2}{b_J(v,v)}
=\frac{d_{\rm mod}}{d_C}
 \frac{k^2 A_E}{|c_{\rm mod}|^2 n_{13}(E)}.
\tag{22}
\]

This is the correct elementary place for a ratio of parametrization degrees. If the two optimal targets are merely isogenous, the chosen isogeny and the pullback of differentials must also be recorded. Equations (19)–(22) are proved here, not an appeal to an unspecified period theorem.

### 3. The actual Ribet–Takahashi statement, and its scope

**PROVED, cited theorem (not byte-cited).** Ribet–Takahashi (1997), Theorems 1–2: take a rational weight-two newform of squarefree conductor N=DpqM, with D a product of an even number of primes, and p,q,D,M pairwise coprime. Let A,A′ be its optimal elliptic quotients of J₀^D(pqM), J₀^{Dpq}(M), and δ,δ′ the polarization degrees. Put c_q=v_qΔ(A), c′_p=v_pΔ(A′). Then

\[
\delta'=\frac{\delta}{c'_pc_q}\,\mathcal E^2,
\qquad
\mathcal E=|\operatorname{im}(\Phi_q(J)\to\Phi_q(A))|
 |\operatorname{coker}(\Phi_p(J')\to\Phi_p(A'))|.
\tag{23}
\]

The integer ℰ divides c′_p c_q. If M is squarefree and not prime (including M=1), each prime ℓ dividing ℰ has reducible A[ℓ]. In particular the simple product formula is valid away from those exceptional primes, with the stated optimal targets. This is a theorem about **degrees and component maps**, not equality of unnormalized complex and integral norms. [Original paper, pp. 11111–11113](https://www.pnas.org/cgi/reprint/94/21/11110.pdf).

Takahashi (2001), *Degrees of Parametrizations of Elliptic Curves by Shimura Curves*, **not byte-cited**, proves in the squarefree-conductor setting N=DM that for an optimal quotient J₀^D(M)→E the induced map of geometric component groups at r|D is surjective; his degree comparisons and computational formulas refine this same framework. The hypotheses include the standard Eichler Γ₀ level and the specified optimal quotient. [Takahashi (2001)](https://www.sciencedirect.com/science/article/pii/S0022314X00926143).

The graph-monodromy identities and the multiplicative period uniformization used here are unconditional. The quoted degree theorem is unconditional under its hypotheses. Applying its squarefree Γ₀ formula directly to our primary U₂, projective-principal U₅, w₁₃ quotient is **not justified**. Its factors may also differ between members of the isogeny class. No “Ribet–Takahashi invariant for each a₁₇” is computed here. Bertolini–Darmon (1998) is used precisely for the p-adic uniformization/Hecke compatibility stated in CD3, not as a source for a canonical complex Petersson identification. No result from an unspecified Bertolini–Darmon 2005 paper is invoked.

For forms with nonrational coefficient field the quotient is generally higher-dimensional; one needs coefficient-field lattices, polarization/congruence ideals, and period comparisons. Equations for one optimal elliptic quotient are not a theorem identifying one real number for every Hecke multiplicity space. Integer a₁₇ by itself does not even establish the rational-form hypothesis.

**CD4 verdict.** The monodromy point G_M is now geometrically specified as a Bass construction. Parametrization degrees and component numbers carry real arithmetic information in normalized comparisons. The claimed two canonical, necessarily different points and the universal raw ratio formula are **REFUTED as stated**. A comparison for fully specified forms, lattices, differential normalizations and periods is **OPEN in this example**, not asserted to be conjectural in every standard multiplicity-one setting.


## CD5 — SHARPENED: what geometry supplies, and what it still does not

**(a) Arithmetic model, not a cup product of the squares.** The model of C over Z₁₃ supplies the unit edge lengths and hence the integral positive monodromy pairing on K. The 17-direction squares specify the Hecke correspondence on its dual graph. This answers the predecessor's missing **geometric origin of the coefficient metric**. The same explicit global curve also supplies a genuine polarization, H⁰/H¹/H², and the zeta function at 17. It does not make the square complex S a surface: H¹(S)=0 still rules out the proposed ordinary face cup product. Nor does monodromy by itself prove the companion positivity; the strict good-prime bound is still needed. “Deninger's positivity here is Grothendieck's positivity” must be restricted to the coefficient pairing, not treated as an independent proof of the critical circle or as an identification of Hodge stars.

**(b) Correct dictionary.** Horizontal harmonic cohomology is X₁₃⊗R; transverse transport is T₁₇ on X₁₃; the edge metric is Grothendieck's monodromy pairing; Bass doubling has the same one-prime Frobenius system as the entire H¹(C), after a noncanonical choice. Replace the brief's last equals sign by “noncanonical one-operator realization”. The Weil pairing belongs to the global Jacobian, and the monodromy pairing to its degeneration; their filtered relationship is (14), not a global two-copy decomposition.

For the GL₁ bond of `04p_gl1_bond.tex`, a meaningful analogue would have to supply a degeneration or an appropriate replacement, its character/period lattice and a positive pairing, a comparison to the actual theta/model space, and prime correspondences compatible with that comparison and the required trace formula. A Jacobi theta vector in L²(R₊×) is not a Néron model or a special fibre. Its “reduction” is **OPEN / speculation**, not an object defined by this audit. Moreover `04q_h_theta.tex:110–128` proves the naive theta forward-cyclic-and-cut proposal false: the forward cyclic space is the whole bond and the outgoing half is outer. That obstruction survives this analogy.

**(c) Exactly which old items change.** B4's “only a selected summand, no entire curve” can now be upgraded to the explicitly defined C₀/w₁₃ and the equality (16). B4b's coefficient-metric provenance closes; its canonical cup/Petersson/companion comparison does not. The 16539-dimensional invariant-metric cone remains: geometry selects G_M within it but does not shrink the cone or import 04l's transitive four-mode symmetry. B6's inverse graded-CP realization remains **OPEN**. The existing direct-sector dimension and negative ordinary-trace obstructions survive, as does the failure of signs inserted in individual Kraus operators. Actual point counts give a genuine curve trace formula but no homogeneous Kraus family with the required net divisor. The distinction in `07_deligne_via_graphs.tex` and `notes/deligne-via-graphs.md` between a geometric realization, purity, and an explicit compatible metric remains necessary.

## Numerical checks for the blind lane

Author: `codex:gpt-6-astra`

Run `OPENBLAS_NUM_THREADS=1 python3 -B notes/cerednik-drinfeld/checks/cycle_checks.py`. It writes no files. It reconstructs the primary generators, reductions, graph, square reordering transport, and **the worked example's specified integral cycle basis**, rather than mistaking the old script's orthonormal-nullspace variable `M` for a cycle Gram.

| Status | Finite test | Result / certificate |
|---|---|---|
| PROVED | Primary sets, quotient, graph | 14 norm-13 and 18 norm-17 generators; 120 vertices; 840 horizontal edges; 1080 vertical edges; 252 distinct reordering rules. |
| PROVED | Connectedness and bipartition | BFS visits all 120 vertices; ε(g)=(det g/5) changes on both colours. |
| PROVED | Prescribed cycle basis | Identity root, BFS neighbours in vertex order, chords in edge order; Z has shape 840×721, ∂Z=0 and chord block I. |
| PROVED | Integral positive Gram | M=ZᵗZ=I+Z_treeᵗZ_tree, hence M≥I. |
| PROVED | Chain transport and Hecke symmetry | T₁ᵗ=T₁, T₁D=DA₁₇, T₁Z=ZL, LᵗM=ML, all in exact integers. |
| PROVED | Adjacency spectrum used for det M | Exact annihilating polynomial, connected bipartition, tr A²=1680, tr A⁴=95040 certify ±14 (1), ±4 (34), ±2 (25). |
| PROVED | det M = τ(Y) | Matrix-tree spectrum formula and independent 119×119 Bareiss cofactor both give 2²¹⁷3⁹²5³³·7. |
| PROVED | Component-group Hecke action is not naively Eisenstein | The normalized rational solution to Qx=(A₁₇−18I)(e₀−e₂₀) has x₀=−364/135. |
| PROVED | Geometric two-copy cover | Vertices (g,±) split by ±ε(g) into two connected 120-vertex copies; w exchanges them. |
| PROVED | Reversal sign | w=−R on oriented chains of the cover; SR=−RS and ST₁₇=−T₁₇S for S=ε(tail); the w=+1 piece is N₋=K, the w=−1 piece has reflected spectrum. |
| PROVED | Companion forms | Exact block multiplication verifies FᵗΩ_MF=17Ω_M and Fᵗ(2G_M)F=17(2G_M). |
| PROVED | Exact strictness at Weil endpoints | rank_(F₁₀₃)(T₁²−68I)=840. The attempted prime 101 has rank 832 and is not used as a certificate of invertibility. Combined with the independently cited curve Weil bound, this proves G_M>0. |
| Numerical cross-check | Generalized symmetric eigenproblem ZᵗT₁Zv=aMv | max |a|≈7.46410161513778; min(17−a²/4)≈3.07179676972441. These decimals are not the proof of strictness. |
| OPEN as a finite check | Canonical Weil/Petersson comparison | Requires a specified map, period data and compatible integral lattices; checking block similitudes cannot test an unspecified comparison. |

In orthonormal edge coordinates, the change of basis Q=ZM^(−1/2) sends the coefficient metric to I and sends L to the symmetric matrix M^(1/2)LM^(−1/2). Applying it to both copies takes (17)–(18) exactly to the worked example's Ω_B and G. Thus equality of the finite formulas has no extra factor 2 or edge-stabilizer weight. On the **two-component** cover the unnormalized pullback v↦(v,v) instead has monodromy norm 2b(v,v), as a degree-two covering should; one must not use that invariant sublattice with its inherited norm as though it were already the quotient curve's polarized character lattice.

Scope of the checks: arithmetic uniformization/descent and the Galois realization are applications of the stated theorems, not finite computations. The scratch script does not recompute the full degree-721 characteristic polynomial or enumerate points on an equation for C. The predecessor's supplied factorization is consistent with these checks; (15) identifies the actual polynomial abstractly without needing that printed factor table. The component-group **order** is computed; its full invariant-factor decomposition is not claimed.

## Corrections to the brief

| Brief assertion | Verdict | Correction |
|---|---|---|
| “X_{B′}(5)” specifies the curve | SHARPENED | Specify U₂, projective principal U₅, and whether level at 13 is O′₁₃× or its projective normalizer. |
| Usual level curve has just 120 geometric components | REFUTED | C₀ has two geometric connected components, each with graph Y; globally the graph is Y† with 240 vertices and 1680 edges. |
| The graph might need a quotient by its bipartition | REFUTED | Each copy has both bipartite sides; quotient by w₁₃ identifies the two copies, leaving Y itself. |
| K belongs to a genus-721 curve over Q | PROVED after correction | Use C=C₀/w₁₃, geometrically connected over Q and split Mumford over Q₁₃. |
| Γ(5)\T₁₄ | SHARPENED | Use the horizontal stabilizer Λ₁₃(5), not the two-prime product lattice. |
| Principal congruence at 5 equals an unspecified Γ(5) marking | SHARPENED | The relevant adelic subgroup is scalar mod 5; symplectic markings and component fields must be distinguished. |
| The special fibre “is a Mumford curve” | SHARPENED | The smooth generic fibre is Mumford; its stable special fibre is the nodal rational-component curve. |
| All effective stabilizers and thickness corrections vanish | PROVED | The primary lattice is free, the level subgroup has no inversions, and w₁₃ exchanges whole components; t_e=1. |
| H¹ graph and character lattice are integrally identical via the edge metric | REFUTED | X₁₃=H₁; H¹ is its integral dual, and the monodromy map has index det M. |
| M is a geometric pairing; T₁₇ is symmetric | PROVED | M is the Grothendieck pairing of C; square transport is its Hecke correspondence. |
| Φ=X∨/X and |Φ|=det M | PROVED with conventions | Use the monodromy injection and geometric components; here split reduction makes the rational-component order the same. |
| Import an Eisenstein component-group conclusion | REFUTED in its naive form | T₁₇−18 does not annihilate this Φ; a rational-solution counterexample is given. |
| Toric reduction means J equals its special-fibre torus | REFUTED | The torus has Tate rank g; J has Tate rank 2g and a period-lattice extension. |
| The toric filtration carries Frob₁₇ on its graded pieces | REFUTED as an asserted canonical construction | It is local at 13, not a global G_Q filtration. |
| Bass doubling is the whole good-prime Frobenius system | SHARPENED / PROVED | For C it is a noncanonical semisimple one-operator realization, and the whole zeta function equals the worked completed function. |
| Ω_M is integrally the principal Weil pairing | REFUTED | det Ω_M=(det M)² obstructs this at ℓ=2,3,5,7. |
| Monodromy composition canonically gives Ω_M and companion Frobenius together | OPEN / unsupported | Evaluation on local graded pieces gives Ω_M only after choices; those choices are not a companion basis for Frob₁₇. |
| G is simply the doubled monodromy metric, hence automatically positive | SHARPENED / REFUTED | It is the specific Bass construction from M and T, positive only under the strict good-prime bound. |
| G=Ω_B𝒥 | REFUTED | Ω_B𝒥=G diag(R⁻¹,R⁻¹), R²=17I−T²/4. |
| Every f-isotypic component is a line and has conductor 650 | REFUTED | Multiplicity spaces and U₂ local types matter; neither follows from the one-prime spectrum. |
| Petersson/monodromy ratio is a parametrization degree | REFUTED | Equations (19)–(22) include period area, differential scaling and saturation index; degrees can cancel. |
| Ribet–Takahashi applies unchanged at this level | REFUTED | Its exact standard-level hypotheses, optimal targets and component corrections must be checked. |
| Two canonical, necessarily different metric-cone points follow | OPEN / unsupported | Only G_M is selected on the given space; a Petersson pullback still needs a normalized comparison, and it can be made equal by choice. |
| The original faces now supply the cup pairing | REFUTED literally | H¹(S)=0; the arithmetic curve is additional geometry. |
| B6 or the theta bond's missing geometry follows | OPEN | Neither a homogeneous Kraus realization nor a toric “reduction” of the GL₁ theta model is constructed. |

## What this changes in the notebook

Author: `codex:gpt-6-astra`

| Claim | Status to register | One-sentence statement |
|---|---|---|
| CD1 | SHARPENED / PROVED | The explicit primary-level Shimura curve quotient C₀/w₁₃ has genus 721 and split 13-adic dual graph X^{13,5}; the unquotiented level curve has two geometric copies. |
| CD2 | PROVED | Horizontal cycles are the toric character lattice with unit-thickness Grothendieck pairing M=ZᵗZ, Hecke action T₁₇, and component order 2²¹⁷3⁹²5³³·7. |
| CD3 | SHARPENED / OPEN | The completed Bass zeta is Z(C/F₁₇,u), but its companion coordinates and Ω_M are not canonically the integral polarized Tate module. |
| CD4 | REFUTED as raw ratio / OPEN as comparison | Parametrization degrees enter explicit normalized period formulas; they do not define an unqualified canonical Petersson/monodromy ratio here. |
| CD5 | SHARPENED / OPEN | Arithmetic degeneration supplies the coefficient metric and the whole curve, while canonical paired comparison, B6's CP realization and the GL₁ reduction analogy remain unconstructed. |

Register this as a genuine closure of the geometric **coefficient-pairing** gap and of the **whole-curve zeta** gap, with the level/descent correction above; retain the canonical comparison and inverse-CP questions rather than replacing them by a stronger unsupported identification.
