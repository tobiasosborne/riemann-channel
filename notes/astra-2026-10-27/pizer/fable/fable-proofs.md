# Topic P (Fable lane): the Pizer graph as Γ\T_ℓ, its Ihara zeta as the L-polynomial of X₀(p) over F_ℓ, its label phase space as H¹

Author: `claude:fable-5.1`, 2026-10-27. Blind of `pizer/astra/`. Brief: `../lane-brief.md`; round brief `../../brief.md` (binding; the
steer "lattice, symplectic form, map or identity; never an overlap" is followed: nothing below uses an overlap).
Scripts: `checks/pizer_graph.py` (P1), `checks/pizer_quotient.py` (P2), `checks/label_lattice.py` (P3); outputs `checks/output_*.txt`.
Interpreter: the PARI venv of the brief (cypari2 / PARI 2.17.2, python-flint). Everything printed is exact (integer characteristic
polynomials, Smith forms, Hermite forms, `qfminim` short vectors); the only floats are the eigenvalue listings printed for the eye.
Literature is cited from memory and marked so; `refs/src/` is not available.

Conventions (record, `notes/astra-2026-10-23/brief.md`): Y a finite (q+1)-regular graph, A adjacency, B_H the Hashimoto operator on oriented
edges, ζ_Y(u) = det(1 − uB_H)^{-1}; label step M = ((A, −q), (1, 0)) on Z^{2n} ∋ (f, g), M^TΩM = qΩ, Ω = ((0, 1), (−1, 0)) ⊗ 1_n, V = qM^{-1},
Weil form ½Ω(M − V). Here q = ℓ. Variable names: PARI/flint print polynomials in `x`; in the identities below `x` is `u` (for det(1 − ·u) type
polynomials) or the characteristic-polynomial variable, as labelled.

**Headline.** P1 PROVED (and the brief's Ihara–Bass question SETTLED with a correction: the Pizer graph has **half-loops**, and
det(1 − uB_H) = (1 + u)^f (1 − u²)^{(N−f)/2 − n} det(1 − B(ℓ)u + ℓu²), f = #self-dual loops, N = (ℓ+1)n); P2 PROVED for **all** p (not only
h = 1), with an exact quaternion-side recomputation at p = 37 matching the Φ_ℓ graphs for ℓ = 2, 3, 5, 7 under one relabelling, including the
half-loop counts; P3(a) computed exactly (p ∈ {37, 73, 109}, ℓ ∈ {2, 3, 5, 7}, k ≤ 4); P3(b): the graph's lattice **is not** H₁(E₁) ⊕ H₁(E₂)
and (at ℓ = 7, in the 3-part) **is not** H₁(J₀(37)) either — the graph picks a third lattice in the isogeny class, and the obstruction sits at
the primes dividing the component-group order n = (p−1)/12; P3(c) SKETCHED: Ω on the nontrivial label lattice is the doubled
Grothendieck monodromy pairing of the toric reduction of J₀(p) at p (discriminant n² = |Φ_p|²), not the unimodular Weil pairing on
H₁(X₀(p), Z). P4 written as HEURISTIC with one PROVED negative (the Tate module is not the completion of the label lattice).

---------------------------------------------------------------------------------------------------------------------

## §1. P1 — the Ihara zeta of the Pizer graph is the reciprocal L-polynomial of X₀(p) over F_ℓ

### 1.1 Objects and normalisations

S_p = supersingular j-invariants in F_{p²}; n = #S_p; E_i a curve with j(E_i) = j_i; w_i = |Aut(E_i)|/2 ∈ {1, 2, 3} (p > 3).
**Brandt matrix** B(ℓ)_{ij} = #{C ⊂ E_i[ℓ], |C| = ℓ, E_i/C ≅ E_j}. Row sums ℓ + 1. Two facts used throughout:

(B1) *B(ℓ)_{ij} is the multiplicity of j_j as a root of Φ_ℓ(j_i, Y).* Reason: Φ_ℓ(j(E), Y) = ∏_{C ⊂ E[ℓ], |C| = ℓ} (Y − j(E/C)) for every
elliptic curve E over any field of characteristic ≠ ℓ (the definition of the modular polynomial via Γ₀(ℓ)\SL₂(Z) in characteristic 0 and
reduction; standard — Lang, *Elliptic functions*, Ch. 5; Silverman AEC II / Advanced Topics; from memory). This holds also at j = 0, 1728 (e.g.
Φ₂(0, Y) = (Y − 54000)³ in characteristic 0, as PARI's `polmodular(2)` shows). So B(ℓ) is computable from Φ_ℓ alone, and that is what
`pizer_graph.py` does (the supersingular j are the images of the roots of Deuring's polynomial H_p(λ) = Σ_i C(m, i)² λ^i, m = (p−1)/2, under
λ ↦ 256(λ² − λ + 1)³/(λ²(λ−1)²); each j is re-checked with `ellissupersingular`).

(B2) *Weighted symmetry* w_j B(ℓ)_{ij} = w_i B(ℓ)_{ji}. Reason: #{subgroups C with E_i/C ≅ E_j} = #Hom_ℓ(E_i, E_j)/|Aut E_j| (isogenies with
the same kernel differ by an automorphism of the target), and #Hom_ℓ(E_i, E_j) = #Hom_ℓ(E_j, E_i) by duality. Hence B(ℓ)W is symmetric for
W = diag(w_i), and the **symmetrisation** is S(ℓ) = W^{−1/2} B(ℓ) W^{1/2} = W^{−1/2}(B(ℓ)W)W^{−1/2}, symmetric with the same characteristic
polynomial as B(ℓ). (The brief wrote W^{1/2}BW^{−1/2}; with B(ℓ) acting on *column* vectors as above, i.e. on functions, (Bf)(i) = Σ_C f(E_i/C), the
correct conjugation is W^{−1/2}BW^{1/2}; the transposed convention gives the other. Both are the same matrix up to transposition.) Checked
exactly for every (p, ℓ) of the table (an assertion in the script).

**The trivial eigenvalue.** B(ℓ)·(1, …, 1)^T = (ℓ+1)(1, …, 1)^T (row sums): the constant *function* is the Eisenstein eigenvector on the function
side; on the divisor side (row vectors, formal sums Σ a_i e_i ↦ Σ a_i B_{ij} e_j) the Eisenstein vector is (1/w_i)_i, since Σ_i B_{ij}/w_i =
Σ_i B_{ji}/w_j = (ℓ+1)/w_j by (B2). This settles the brief's "(1, …, 1) or (1/w_i)": both, on the two sides.

**Eichler's theorem (basis problem; from memory: Eichler 1955/1973 "The basis problem for modular forms and the traces of the Hecke
operators"; Pizer 1980 "An algorithm for computing modular forms on Γ₀(N)"; Gross 1987 "Heights and the special values of L-series" §§1–5,
Prop. 5.6).** For prime level p the Brandt module Z[S_p] ⊗ C with the operators B(n), n ≥ 1, is isomorphic as a Hecke module to
M₂(Γ₀(p)) = C·E₂^{(p)} ⊕ S₂(Γ₀(p)); the Eisenstein line has eigenvalue σ(n) coprime-to-p (ℓ + 1 at n = ℓ), and the degree-zero part Z[S_p]^0 ⊗ C ≅
S₂(Γ₀(p)). Consequently, as polynomials in Z[x],

    charpoly(B(ℓ)) = (x − ℓ − 1) · charpoly(T_ℓ | S₂(Γ₀(p)))                                            (E)

for every ℓ ≠ p and every p (the right factor is computed by PARI's `mfheckemat(mfinit([p,2],1), ℓ)` on the cuspidal space; every form is new
at prime level). (E) is the statement checked exactly in the table for p ∈ {11, 37, 73, 101, 109}, ℓ ∈ {2, 3, 5, 7}: 20 equalities of integer
polynomials, all true.

**Eichler–Shimura (from memory: Shimura, *Introduction to the arithmetic theory of automorphic functions*, 1971, Thm 7.11 and Cor. 7.10 /
"Eichler–Shimura relation" T_ℓ = Frob_ℓ + Ver_ℓ on J₀(p)_{F_ℓ}; Igusa for good reduction of X₀(p) at ℓ ∤ p).** For ℓ ≠ p, X₀(p) has good
reduction at ℓ, and the characteristic polynomial of Frob_ℓ on H¹_ét(X₀(p)_{F̄_ℓ}, Q_q) (q ≠ ℓ) is ∏_f (x² − a_ℓ(f)x + ℓ), the product over an
eigenbasis of S₂(Γ₀(p)) (equivalently over newforms and their Galois conjugates). So the L-polynomial of X₀(p)/F_ℓ is

    P_{p,ℓ}(u) = ∏_f (1 − a_ℓ(f)u + ℓu²) = u^{2g} χ_Frob(1/u),      #X₀(p)(F_ℓ) = ℓ + 1 − Tr(T_ℓ | S₂(Γ₀(p))),

and Z(X₀(p)/F_ℓ, u) = P_{p,ℓ}(u)/((1−u)(1−ℓu)).

### 1.2 Theorem (P1). PROVED (from (B1), (B2), (E), Eichler–Shimura, Ihara–Bass as re-derived in 1.3).

For every p and every ℓ ≠ p:

    det(1 − B(ℓ)u + ℓu²) = (1 − u)(1 − ℓu) · P_{p,ℓ}(u).                                                (P1)

*Proof.* det(1 − B(ℓ)u + ℓu²) = ∏_{λ ∈ spec B(ℓ)} (1 − λu + ℓu²) (over the algebraic closure; B(ℓ) is diagonalisable since it is conjugate to the
symmetric S(ℓ) by (B2)). By (E) the spectrum is {ℓ+1} ∪ {a_ℓ(f)}_f with multiplicity; the factor of λ = ℓ+1 is 1 − (ℓ+1)u + ℓu² = (1−u)(1−ℓu), and
the rest is ∏_f (1 − a_ℓ(f)u + ℓu²) = P_{p,ℓ}(u) by Eichler–Shimura. ∎

Equivalently, with the 2n × 2n label step M_ℓ = ((B(ℓ), −ℓ), (1, 0)): det(x − M_ℓ) = det(x² − B(ℓ)x + ℓ) = (x−1)(x−ℓ) · x^{2g}P_{p,ℓ}(1/x) (block
determinant with commuting blocks; this is how the script computes the left side of (P1), as the reversed characteristic polynomial of M_ℓ).

**Corollary (Ramanujan = Weil for J₀(p)). PROVED.** Every nontrivial eigenvalue a_ℓ(f) of B(ℓ) satisfies |a_ℓ(f)| ≤ 2√ℓ. Precisely: by
Eichler–Shimura the a_ℓ(f) are the traces of Frob_ℓ on the 2-dimensional pieces of H¹ of the abelian variety J₀(p)/F_ℓ, i.e. a_ℓ(f) = α + ᾱ with
α ᾱ = ℓ; Weil's theorem for abelian varieties over finite fields (Weil 1948, *Variétés abéliennes et courbes algébriques*; from memory) says
|α| = √ℓ for every eigenvalue of Frobenius on H¹ (equivalently on the Tate module) of an abelian variety, hence |a_ℓ(f)| ≤ 2√ℓ. No Deligne
(weight > 2, or Ramanujan–Petersson for Maass forms) is needed; for weight 2 it is the Riemann hypothesis for the curve X₀(p)/F_ℓ, i.e. for its
Jacobian. So G(p, ℓ) is Ramanujan for every p and ℓ ≠ p. In the record's language: the Weil form ½Ω(M_ℓ − V_ℓ) = ((ℓ, B(ℓ)/2), (B(ℓ)/2, 1)) is
positive semidefinite on the nontrivial label modes iff B(ℓ)² ≤ 4ℓ there (`graph-ihara.md` §6), and that is exactly Weil's theorem for J₀(p)/F_ℓ.
Table: max |a_ℓ(f)| at (p, ℓ) = (73, 2): 2.618 < 2.828; (101, 2): 2.763 < 2.828; (101, 7): 4.701 < 5.292 (all 20 cells printed; all pass).

**Zeta.** Hence, for p ≡ 1 mod 12 (all w_i = 1) and with the Hashimoto operator of 1.3,

    ζ_{G(p,ℓ)}(u) = det(1 − uB_H)^{-1} = (1 + u)^{−f} (1 − u²)^{−((N−f)/2 − n)} / [(1 − u)(1 − ℓu) P_{p,ℓ}(u)],   N = (ℓ+1)n,

and the "H¹ part" of the graph's zeta, det(1 − B(ℓ)u + ℓu²)/((1−u)(1−ℓu)), **is** the numerator P_{p,ℓ}(u) of the Hasse–Weil zeta of X₀(p) over F_ℓ.

**General p (weights).** (P1) holds verbatim for all p: it is a statement about the matrix B(ℓ), and (E) holds for all p. What changes is the
graph. For p ≢ 1 mod 12, B(ℓ) is not symmetric; S(ℓ) = W^{−1/2}B(ℓ)W^{1/2} is symmetric but has irrational entries (√2, √3), so it is not the
adjacency matrix of any multigraph. The object whose zeta is (1 − u²)^{−(…)}/det(1 − B(ℓ)u + ℓu²) is the **quotient graph of groups** Γ\\T_ℓ of §2
with vertex groups of orders w_i (Bass 1992, "The Ihara–Selberg zeta function of a tree lattice", from memory, defines ζ for a finite graph of
groups / tree lattice and proves the Ihara-type determinant formula with the stabiliser orders as weights; Serre, *Trees*, for the quotient
structure). On the Brandt module with Gross's pairing ⟨e_i, e_j⟩ = w_i δ_{ij} the operator B(ℓ) is self-adjoint (that is (B2)), which is the
invariant way to say "symmetric after weighting". I do not claim more than this for the weighted zeta (SKETCHED: the identification with
Bass's zeta of the graph of groups is cited, not re-derived here).

### 1.3 Ihara–Bass for the Pizer multigraph: loops, and half-loops. PROVED, and the brief's question settled.

**The oriented-edge set.** For p ≡ 1 mod 12 (Aut(E_i) = ±1 for all i) define the oriented edges as the pairs e = (E_i, C), C ⊂ E_i[ℓ] of order ℓ;
N = (ℓ+1)n of them; start(e) = i, end(e) = j with E_i/C ≅ E_j. The **reversal** ē is (E_j, C′) where C′ = image of E_i[ℓ] under the isogeny
φ_C: E_i → E_i/C ≅ E_j; C′ is well defined because the isomorphism E_i/C ≅ E_j is unique up to ±1, which fixes subgroups. ē is the kernel of the
dual isogeny, so ē̄ = e, and A_{ij} := #{e : start i, end j} = B(ℓ)_{ij}. **A fixed point e = ē is a loop (E_i, C) whose isogeny φ: E_i → E_i has
ker φ̂ = ker φ, i.e. φ̂ = εφ with ε ∈ Aut = ±1; the trace of φ is (1+ε)φ ∈ Z forces ε = −1, so φ² = −ℓ: a half-loop is an element φ ∈ O_i = End(E_i)
with trd φ = 0, nrd φ = ℓ, counted up to sign.** Such loops exist exactly when Z[√−ℓ] embeds in some O_i, e.g. for p = 37, ℓ = 2 ((−2/37) = −1 so
Q(√−2) ⊂ B_{37,∞}).

**Hashimoto operator.** B_H(e, e′) = 1 iff end(e) = start(e′) and e′ ≠ ē. (With a half-loop e, the step e → e is backtracking and is excluded.) Let S
(N × n) be the start matrix, T the end matrix, J the reversal permutation. Then J² = 1, T = JS, SᵀT = A = B(ℓ), SᵀS = (ℓ+1)·1_n (a half-loop
contributes 1 to the degree, a loop pair 2, exactly as in B(ℓ)), and B_H = TSᵀ − J.

**Lemma (Ihara–Bass with half-loops). PROVED.** Let f = #{e : ē = e}. Then

    det(1 − uB_H) = (1 + u)^f (1 − u²)^{(N − f)/2 − n} · det(1 − B(ℓ)u + ℓu²).

*Proof.* 1 − uB_H = K − uTSᵀ with K = 1 + uJ, K^{-1} = (1 − uJ)/(1 − u²). By Sylvester, det(K − uTSᵀ) = det K · det(1_n − uSᵀK^{-1}T), and
SᵀK^{-1}T = (SᵀT − uSᵀJT)/(1−u²) = (A − u(ℓ+1))/(1−u²) because JT = S. So det(1_n − uSᵀK^{-1}T) = det((1−u²) − uA + (ℓ+1)u²)/(1−u²)^n =
det(1 − Au + ℓu²)/(1−u²)^n. Finally J has f eigenvalues +1 from its fixed points and (N−f)/2 two-cycles each contributing (1+u)(1−u), so
det K = (1+u)^f (1−u²)^{(N−f)/2}. ∎

So: for a multigraph whose loops are oriented pairs (f = 0) the record's formula (1 − u²)^{|E|−|V|} det(1 − Au + ℓu²) holds with |E| = N/2 and the
loop counted twice in the degree and twice in A_ii; for the Pizer graph with the dual-isogeny reversal the loop count in B(ℓ)_{ii} is *once per
subgroup*, a self-dual loop is a half-edge, and the correction is the factor ((1+u)/(1−u))^{f/2} relative to (1 − u²)^{N/2 − n}. In Bass–Serre
terms a half-loop is an edge of T_ℓ inverted by an element of Γ (§2): the inversion γ with γ² = −ℓ.

**Numerical settlement (all exact, `output_pizer_graph.txt`).** The script constructs every isogeny explicitly over the splitting field
F_{p^{2k}} of E[ℓ] (k = order of −p mod ℓ; the F_{p²}-models are chosen with Frobenius −p by `ellcard` and a quadratic twist if needed, then
embedded with `ffembed`; subgroups are found by grouping ℓ-torsion points, since the ℓ-division polynomial can split further — at p = 109, ℓ = 5
all of E[5] is F_{p²}-rational), computes the dual kernel as the characteristic polynomial of x ↦ x(φ(P)) on F[x]/(h_{C″}), transports it along
the explicit isomorphism E_i/C ≅ E_j (x ↦ sx, s = (B_j/B′)(A′/A_j)), checks that the reversal is an involution with target(ē) = start(e), that
A = B(ℓ), and then compares the degree-N integer polynomial det(1 − uB_H) with the lemma, and with the naive formula:

| p | ℓ | N | f | Tr B(ℓ) | lemma | naive (1−u²)^{N/2−n} |
|---|---|---|---|---|---|---|
| 37 | 2 | 9 | 1 | 1 | true | **false** |
| 37 | 3 | 12 | 0 | 2 | true | true |
| 37 | 5 | 18 | 2 | 4 | true | **false** |
| 37 | 7 | 24 | 0 | 6 | true | true |
| 73 | 2, 3 | 18, 24 | 0, 0 | 2, 2 | true | true |
| 73 | 5, 7 | 36, 48 | 2, 2 | 4, 2 | true | **false** |
| 109 | 2 | 27 | 1 | 1 | true | **false** |
| 109 | 3, 5, 7 | 36, 54, 72 | 0 | 4, 4, 6 | true | true |

(N odd, e.g. 9 and 27, is itself proof that a fixed-point-free reversal is impossible there.) The half-loop counts are reproduced independently
on the quaternion side in §2 (p = 37: f = 1, 0, 2, 0 for ℓ = 2, 3, 5, 7, as Σ_i #{γ ∈ O_i : trd γ = 0, nrd γ = ℓ}/2).

### 1.4 The table (P1). All numbers in `checks/output_pizer_graph.txt`; a few displayed.

Counts and weights: #S_p = 2, 3, 6, 9, 9 for p = 11, 37, 73, 101, 109 (formula ⌊p/12⌋ + {0,1,1,2} confirmed); g(X₀(p)) = dim S₂(Γ₀(p)) = n − 1
in every case (PARI `mfdim`); weights (2, 3) at p = 11 (j = 1728 ≡ 1 and j = 0), (3, 1, …, 1) at p = 101 (j = 0 only), all 1 at p ≡ 1 mod 12; Eichler's
mass Σ 1/|O_i^×| = Σ 1/(2w_i) = (p−1)/24 in every case (so Σ 1/w_i = (p−1)/12 — the brief's §0 did not state the mass formula, I add it as the check
that the weights are right).

p = 37 (vertices j = 30t+18, 7t+25, 8 in F_{37²} = F_37(t)):
B(2) = [[0,2,1],[2,0,1],[1,1,1]], charpoly x³ − x² − 6x = x(x+2)(x−3): a₂ ∈ {0, −2} (37b, 37a), P_{37,2}(u) = (1 + 2u²)(1 + 2u + 2u²) = 4u⁴+4u³+4u²+2u+1, #X₀(37)(F₂) = 5.
B(3) = [[0,3,1],[3,0,1],[1,1,2]], charpoly (x−4)(x+3)(x−1): a₃ ∈ {−3, 1}; P_{37,3} = 9u⁴+6u³+3u²+2u+1; #X₀(37)(F₃) = 6.
B(5) = [[1,3,2],[3,1,2],[2,2,2]], a₅ ∈ {−2, 0}; P_{37,5} = 25u⁴+10u³+10u²+2u+1; #X₀(37)(F₅) = 8.
B(7) = [[2,3,3],[3,2,3],[3,3,2]], a₇ = −1 twice; P_{37,7} = 49u⁴+14u³+15u²+2u+1 = (1 + u + 7u²)²; #X₀(37)(F₇) = 10.
p = 73: B(2) = [[2,0,0,1,0,0],[0,0,1,1,1,0],[0,1,0,1,0,1],[1,1,1,0,0,0],[0,1,0,0,0,2],[0,0,1,0,2,0]], charpoly x⁶−2x⁵−10x⁴+16x³+22x²−18x−9 = (x−3)(x−1)(x²+3x+1)(x²−x−3)
(the rational newform of level 73 has a₂ = 1, the two quadratic ones a₂ = (−3±√5)/2 and (1±√13)/2, matching the printed eigenvalues −2.618, −0.382, −1.303, 2.303), P_{73,2} = 32u¹⁰+16u⁹+24u⁸+12u⁷+10u⁶+7u⁵+5u⁴+3u³+3u²+u+1, #X₀(73)(F₂) = 4.
p = 109, ℓ = 7: B(7) 9 × 9 printed, P_{109,7} of degree 16 printed, #X₀(109)(F₇) = 8... see the output (the counts are 5, 4, 8, 14 for ℓ = 2, 3, 5, 7
at p = 109; 3, 2, 10, 8 at p = 101; 4, 6, 8, 14 at p = 73; 5, 5, 5, 10 at p = 11).

**The model of X₀(37).** The brief's model y² = −x⁶ − 9x⁴ − 11x² + 37 (from memory, Mazur–Swinnerton-Dyer 1974) is **confirmed**:
`hyperellcharpoly` over F_ℓ equals ∏_f (x² − a_ℓ(f)x + ℓ) from `mfheckemat` for ℓ = 3, 5, 7, 11, 13, 17, 19, 23 (eight exact equalities of quartics,
e.g. ℓ = 5: x⁴ + 2x³ + 10x² + 10x + 25 = (x² + 2x + 5)(x² + 5)), and a direct point count of the model (affine points plus the two points at
infinity, y² = −1) gives 6, 8, 10, 14, 20, 12, 18, 16 = ℓ + 1 − Tr T_ℓ. At ℓ = 2 this model is singular (y² = (x³+x²+x+1)² mod 2); X₀(37) has good
reduction at 2 and #X₀(37)(F₂) = 5 comes from the Hecke trace a₂(37a) + a₂(37b) = −2 + 0.

---------------------------------------------------------------------------------------------------------------------

## §2. P2 — the Pizer graph is the quotient of the tree by a global lattice

### 2.1 Local statement (vertices and neighbours in the tree). PROVED.

Let E be supersingular over F̄_p, ℓ ≠ p, T = T_ℓ(E) ≅ Z_ℓ², V = T ⊗ Q_ℓ, e: V × V → Q_ℓ(1) the ℓ-adic Weil pairing (alternating, nondegenerate).
(i) *T is self-dual*: e restricts to a perfect pairing T × T → Z_ℓ(1) (perfectness of e_{ℓ^n} on E[ℓ^n] for every n; Silverman AEC III.8, from
memory). So [T^⊥ : T] = 1: T is a qunaught lattice at ℓ in the sense of topic T / `graph-ihara.md` §2(b), and its class [T] is a vertex of T_ℓ =
GL₂(Q_ℓ)/Q_ℓ^×GL₂(Z_ℓ) of the self-dual colour.
(ii) *Subgroups are superlattices.* For C ⊂ E[ℓ] of order ℓ put L_C = ℓ^{-1}{t ∈ T : (t mod ℓT) ∈ C} ⊂ V, using T/ℓT = E[ℓ]. Then T ⊂ L_C ⊂ ℓ^{-1}T
with L_C/T ≅ C, and C ↦ L_C is a bijection between the ℓ + 1 subgroups and the ℓ + 1 index-ℓ superlattices of T, i.e. the neighbours of [T] in
the tree. (iii) *The isogeny identifies them.* φ = φ_C: E → E′ = E/C induces φ_*: V(E) ≅ V(E′) and φ_*^{-1}(T(E′)) = L_C: for t ∈ T, φ_*(ℓ^{-1}t) ∈
T(E′) iff φ_*(t) ∈ ℓT(E′) iff φ(t mod ℓ) = 0 in E′[ℓ] (naturality of T → T/ℓ) iff (t mod ℓ) ∈ C. And φ_* is a *symplectic similitude* of factor ℓ:
e′(φx, φy) = e(x, φ̂φy) = ℓ e(x, y). So the ℓ + 1 neighbours of E in G(p, ℓ) are the ℓ + 1 neighbours of [T_ℓ(E)] in T_ℓ, each carried by a
similitude of factor ℓ of the Weil form — the local version of M^TΩM = ℓΩ. ∎ (The brief's phrasing "sends T(E) onto an index-ℓ sublattice of
T(E′)" is the same statement read from E′: φ_*T(E) ⊂ T(E′) has index ℓ.)

### 2.2 Global statement. PROVED for all p (strong approximation), with the class-set and the colour questions answered.

Notation: B = B_{p,∞}, O a maximal order, Ô = O ⊗ Ẑ, O_ℓ = O ⊗ Z_ℓ ≅ M₂(Z_ℓ) (B splits at ℓ), Ô^{(ℓ)} the part away from ℓ. Deuring's
correspondence (from memory: Deuring 1941; Gross 1987 §2; Voight, *Quaternion algebras*, Ch. 42): E ↦ Hom(E₀, E) is a bijection S_p ≅ Cl(O) =
left ideal classes of O = End(E₀), and Cl(O) = B^×(Q)\B^×(A_f)/Ô^× (the adelic description of the class set; Voight Ch. 27, from memory). Under it
the ℓ-isogenies E_I → E_I/C correspond to the ℓ + 1 left ideals J ⊂ I of index ℓ², and E_J = E_I/C; so B(ℓ)_{[I][J]} = #{J ⊂ I index ℓ² : [J] = [J′]}.

**Theorem (P2). PROVED.** For every p and every ℓ ≠ p, with Γ := O[1/ℓ]^×/Z[1/ℓ]^× acting on T_ℓ through O ⊗ Q_ℓ ≅ M₂(Q_ℓ):

    G(p, ℓ) ≅ Γ\T_ℓ   as quotient multigraphs (vertices = Γ-orbits of vertices, edges = Γ-orbits of edges, half-loops = edges inverted by Γ),

with vertex stabilisers Γ_{[I]} ≅ O_R(I)^×/±1 of order w_{[I]}. It is **one** connected quotient for one order O (not a disjoint union over the
class set, and not a two-colour cover): Γ always contains elements of odd norm valuation, so Γ\T_ℓ is not bipartite.

*Proof.* (a) *Reduction to one place.* Claim: B^×(A_f) = B^×(Q) · B^×(Q_ℓ) · Ô^×. Given x ∈ B^×(A_f), write nrd(x) = r·t·v with r ∈ Q^×_{>0},
t ∈ Q_ℓ^×, v ∈ Ẑ^× (possible: A_f^× = Q^×_{>0}·Q_ℓ^×·Ẑ^×, indeed A_f^× = Q^×_{>0}Ẑ^×). Choose γ ∈ B^×(Q) with nrd γ = r (Hasse–Schilling–Maass:
nrd(B^×(Q)) = Q^×_{>0} for B definite; from memory), g ∈ B^×(Q_ℓ) with nrd g = t, u ∈ Ô^× with nrd u = v (nrd(O_q^×) = Z_q^× at every q, also at
the ramified q = p, for a maximal order; from memory). Then y := γ^{-1}xu^{-1}g^{-1} has nrd y = 1, so y ∈ B¹(A_f). **Strong approximation**
(Kneser 1966 / Eichler; from memory) for the simply connected group B¹ with B¹(Q_ℓ) = SL₂(Q_ℓ) non-compact says B¹(Q)·B¹(Q_ℓ) is dense in B¹(A_f);
since Ô¹ is open, B¹(A_f) = B¹(Q)B¹(Q_ℓ)Ô¹. Write y = γ₁g₁u₁ accordingly. Then x = γγ₁ · g₁u₁ g u — and since B^×(A_f) = B^×(A_f^{(ℓ)}) × B^×(Q_ℓ),
the ℓ-components g₁, g commute with the away-from-ℓ part u₁^{(ℓ)} of u₁, so x = (γγ₁)(g₁u_{1,ℓ}g)(u₁^{(ℓ)}u) ∈ B^×(Q)B^×(Q_ℓ)Ô^×. (b) *Double
coset bookkeeping.* K′ := Ô^{(ℓ)×} × B^×(Q_ℓ) is a subgroup containing Ô^×, and (a) says B^×(A_f) = B^×(Q)K′. For H ⊂ G ⊃ K′ ⊃ U with G = HK′
one has H\G/U ≅ (H ∩ K′)\K′/U (the map is onto by G = HK′; if Hk₁U = Hk₂U then k₂ = hk₁u with h = k₂u^{-1}k₁^{-1} ∈ H ∩ K′). Here H ∩ K′ =
B^×(Q) ∩ (Ô^{(ℓ)×} × B^×(Q_ℓ)) = {γ ∈ B^× : γ ∈ O_q^× ∀q ≠ ℓ} = O[1/ℓ]^×. Hence

    Cl(O) = B^×(Q)\B^×(A_f)/Ô^× ≅ O[1/ℓ]^× \ B^×(Q_ℓ)/O_ℓ^× = O[1/ℓ]^× \ GL₂(Q_ℓ)/GL₂(Z_ℓ) = O[1/ℓ]^×\{lattices in Q_ℓ²}.

The centre Z[1/ℓ]^× = ±ℓ^Z ⊂ O[1/ℓ]^× acts on lattices by scaling, so Cl(O) ≅ Γ\V(T_ℓ) with Γ = O[1/ℓ]^×/Z[1/ℓ]^×. (c) *Edges.* The Hecke
operator T_ℓ on Z[Cl(O)] = functions on B^×(Q)\B^×(A_f)/Ô^× is the double coset Ô^×·diag(ℓ,1)_ℓ·Ô^×, i.e. the sum over the ℓ + 1 tree-neighbours
at the ℓ-component; under (b) the ℓ + 1 neighbours of the vertex Γ·[L] are Γ·[L′] for the ℓ + 1 neighbours L′ of L in T_ℓ, and the ideal J ⊂ I of
index ℓ² corresponding to the neighbour L′ ⊂ L is exactly the one with E_J = E_I/C (2.1 (ii)–(iii) read through Deuring: the ideal of the lattice L′
is {x ∈ O : x_ℓ L ⊂ L′} away from ℓ trivial). So the multigraph with A_{[L][L′]} = #{neighbours L″ of L with ΓL″ = ΓL′} has adjacency B(ℓ) —
this is the quotient multigraph Γ\T_ℓ. (d) *Stabilisers and inversions.* Γ_{[L]} = (O_L[1/ℓ]^× ∩ GL₂(Z_ℓ)Q_ℓ^×)/Z[1/ℓ]^× = O_L^×/±1 where O_L is
the order of the lattice (the right order of the ideal), of order w. An edge {L, L′} inverted by γ ∈ Γ means γL = L′, γL′ = ℓ^mL, so γ² ∈ ℓ^m O_L^×;
with nrd γ = ℓ^{odd} this is γ² = −ℓ up to units when O_L^× = ±1: the half-loops of §1.3. (e) *Colours.* Γ preserves the bipartition of T_ℓ iff
every γ ∈ O[1/ℓ]^× has even ℓ-adic norm valuation. But Γ\T_ℓ = G(p, ℓ) is never bipartite: a bipartite (ℓ+1)-regular graph has adjacency
eigenvalue −(ℓ+1), and by (E) + Weil all nontrivial eigenvalues are ≤ 2√ℓ < ℓ + 1 in absolute value. So Γ contains elements of odd norm
valuation (equivalently: some O_i contains an element of norm ℓ^{odd}; at p = 37 already of norm ℓ for ℓ = 2, 3, 5, 7 — printed), the two
colours of T_ℓ are identified in the quotient, and every vertex of G(p, ℓ) has lifts of both colours: self-dual lattices (Tate modules) and
their odd-colour neighbours (GKP codes of one ℓ-dimensional qudit in the reading of `graph-ihara.md` §2(b)) — Γ scales the Weil form by
nrd γ ∈ ℓ^Z, so "self-dual" is only a Γ-orbit-wise notion up to the similitude factor. ∎

Remarks. (1) Nothing in the proof needs h(O) = 1; the brief's "when h(O) = 1" is a sufficient but unnecessary restriction. What strong
approximation gives is the full identification, not merely "connected and covered by the tree". (2) Changing O to another maximal order O′
conjugates Γ inside B^× (O′ = αOα^{-1} need not hold — maximal orders fall into h types — but Cl(O′) ≅ Cl(O) and the two quotient graphs are
isomorphic since both are G(p, ℓ)); the vertex Γ·[Z_ℓ²] is the class of O itself. (3) For p ≢ 1 mod 12 the quotient has vertex groups of order
w_i and the "graph" is a graph of groups; its Ihara zeta in Bass's sense is the weighted object of §1.2.

### 2.3 Exact check at p = 37 (h = 3) on the quaternion side. `checks/pizer_quotient.py`, output `checks/output_pizer_quotient.txt`. NUMERICAL, all exact.

B = (−2, −37)_Q, verified ramified exactly at {37, ∞} (`algramifiedplaces`). Maximal order O from `alginit`, Z-basis (rows in 1, i, j, k):
(1/2, 0, 1/2, 1/2), (0, 1/4, 1/2, 3/4), (0, 0, 1, 0), (0, 0, 0, 1); det(trd(e_a e_b)) = 1369 = 37², so the reduced discriminant is 37 and O is
maximal; O·O = O. Left ideals are Z-lattices in Hermite normal form (flint); ideal equivalence J = Iβ is tested exactly by whether Ī·J contains
an element of norm nrd(I)nrd(J) (PARI `qfminim` on the integer Gram matrix of the reduced norm); neighbours of I are the ℓ + 1 lattices
Ox + ℓI, x ∈ I/ℓI, of index ℓ² in I. Results: class number h = 3 (BFS at ℓ = 2; representatives of norms 1, 2, 2); unit groups of the three right
orders all of order 2 (so w = (1, 1, 1)); Eichler mass Σ 1/|O_i^×| = 3/2 = (37−1)/24. Ideal-class Brandt matrices:
B(2) = [[1,1,1],[1,0,2],[1,2,0]], B(3) = [[2,1,1],[1,0,3],[1,3,0]], B(5) = [[2,2,2],[2,1,3],[2,3,1]], B(7) = [[2,3,3],[3,2,3],[3,3,2]].
The single relabelling (j₀, j₁, j₂) ↦ (class 1, class 2, class 0) carries these onto the four Φ_ℓ matrices of §1.4 simultaneously (asserted).
Half-loops from the orders, f_ℓ = Σ_i #{γ ∈ O_i : trd γ = 0, nrd γ = ℓ}/2 = 1, 0, 2, 0 for ℓ = 2, 3, 5, 7, equal to the isogeny-side counts of §1.3.
Elements of norm ℓ in the three orders: (2, 0, 0), (4, 0, 0), (4, 2, 2), (4, 4, 4) — consistent with the diagonal of B(ℓ) through
#{γ ∈ O_i : nrd γ = ℓ} = |O_i^×|·B(ℓ)_{ii} = 2B(ℓ)_{ii} (e.g. ℓ = 7: 4 = 2·2 at every vertex). So the quotient-graph description and the Φ_ℓ graph
agree exactly, including the inversion structure.

---------------------------------------------------------------------------------------------------------------------

## §3. P3 — the label phase space and H¹ of X₀(p): rationally yes, integrally no

### 3.1 The nontrivial sublattice, defined integrally. PROVED (elementary).

L = Z^{2n} ∋ (f, g), M = M_ℓ = ((B(ℓ), −ℓ), (1, 0)), Ω = ((0, 1), (−1, 0)); M^TΩM = ℓΩ (asserted exactly for all 12 (p, ℓ) with p ≡ 1 mod 12).
v = (1, …, 1). The trivial plane L_triv = Zv ⊕ Zv is M-invariant (M(av, bv) = (((ℓ+1)a − ℓb)v, av)), with M|L_triv having eigenvalues ℓ, 1. Its
Ω-orthogonal is L₀ = {(f, g) : Σf = Σg = 0} = (v^⊥)², M-invariant because B(ℓ) is symmetric (p ≡ 1 mod 12), saturated, of rank 2(n−1) = 2g;
it is also the saturation of the kernel of the projection onto the trivial modes, so the two definitions offered by the brief coincide. The trivial
mode does **not** split off integrally: [Z^{2n} : L₀ ⊕ L_triv] = n² (printed: 9, 36, 81 for n = 3, 6, 9), because Z^n ⊋ v^⊥ ⊕ Zv has index n.
(On the trivial plane the labelling (f, g) ↦ σf + τg of `graph-ihara.md` §4 has kernel Z(v, −v), as tutorial §6 says; it is injective on L₀ for a
connected non-bipartite graph.) The dual choice Z^{2n}/L_triv = (Z^n/Zv)² is the Z-dual of L₀ with the transposed action, and all Smith forms
below are the same for it (SNF of a matrix equals that of its transpose).

**Proposition (rational identification). PROVED.** charpoly(M | L₀) = ∏_f (x² − a_ℓ(f)x + ℓ) = x^{2g} P_{p,ℓ}(1/x) = charpoly(Frob_ℓ | H¹(X₀(p)_{F̄_ℓ}, Q_q)),
and M|L₀ is semisimple (B(ℓ) symmetric). Hence, whenever P_{p,ℓ} has no repeated root, (L₀ ⊗ Q, M) ≅ (H¹(X₀(p)_{F̄_ℓ}, Q_q) ⊗ Q̄, Frob_ℓ) as modules
over the polynomial ring (both are the direct sum of the 1-dimensional eigenspaces of the same 2g distinct eigenvalues); when P_{p,ℓ} has a
repeated root (p = 37, ℓ = 7: P = (1 + u + 7u²)²), both are still semisimple with the same multiplicities (Frobenius on H¹ of an abelian variety is
semisimple, Weil / Tate; from memory), so the isomorphism holds in all cases over Q̄, and over Q as Q[x]-modules by comparing invariant factors
(both are ⊕ over the distinct irreducible factors with equal multiplicities; checked at the level of characteristic polynomials in all 12 cells:
`output_label_lattice.txt`, "equal True"). The Weil form ½Ω(M − V) restricted to L₀ is positive semidefinite iff B(ℓ)² ≤ 4ℓ on L₀ iff Weil's theorem
for J₀(p)/F_ℓ (§1.2). So **the graph's phase space is H¹ of the modular curve rationally, with M_ℓ = Frobenius at ℓ.** ∎

### 3.2 (a) Smith normal forms of 1 − M^k on L₀. NUMERICAL (exact), `checks/label_lattice.py`.

For p ∈ {37, 73, 109}, ℓ ∈ {2, 3, 5, 7}, k ∈ {1, 2, 3, 4}: |L₀/(1 − M^k)L₀| = det(1 − M^k|L₀) = Res_x(∏_f(x² − a_ℓx + ℓ), 1 − x^k) = #J₀(p)(F_{ℓ^k}) in all
48 cells (forced by 3.1, as the brief says; the content is the group structure). Examples (invariant factors ≠ 1):

| p | ℓ | k = 1 | k = 2 | k = 3 | k = 4 |
|---|---|---|---|---|---|
| 37 | 2 | 15 | 3, 15 | 45 | 15, 15 |
| 37 | 3 | 21 | 105 | 2, 2, 2, 126 | 5, 1365 |
| 37 | 5 | 48 | 12, 96 | 13104 | 2, 8, 24, 960 |
| 37 | 7 | 9, 9 | 63, 63 | 6, 6, 54, 54 | 2331, 2331 |
| 73 | 2 | 114 | 3, 1368 | 2, 2, 2, 2, 2394 | 3, 3, 3, 46512 |
| 73 | 7 | 99, 594 | 5, 6930, 20790 | 6, 12, 252, 8316, 24948 | 15, 15, 15, 15, 512820, 3076920 |
| 109 | 2 | 4428 | 6, 495936 | 22968036 | 12, 683399808 |
| 109 | 7 | 6, 2215566 | 2, 2, 6, 3574339394310 | 3, 3, 126, 217022416825406598 | 4, 4, 120, 586581764025442920668280 |

(p = 109, ℓ = 7, k = 4: order 1126236986928850407683097600 = #J₀(109)(F_{7⁴}).)

### 3.3 (b) p = 37 against E₁ × E₂. REFUTED for the product lattice; and the graph lattice is not H₁(J₀(37)) either (3-part at ℓ = 7).

Cremona labels confirmed by PARI without `elldata`: 37a1: y² + y = x³ − x, conductor 37, a₂ = −2, a₃ = −3, a₅ = −2, analytic rank 1; 37b1: y² + y =
x³ + x² − 23x − 50, conductor 37, a₂ = 0, a₃ = 1, a₅ = 0, rank 0 — these are the two eigenvalue systems of B(ℓ) in §1.4, so J₀(37) ~ E₁ × E₂ (isogenous).
Groups E_i(F_{ℓ^k}) by `ellgroup` over `ffgen([ℓ,k])`, product put in Smith form, against L₀/(1 − M^k)L₀:

| ℓ | k | L₀/(1−M^k)L₀ | E₁(F) × E₂(F) | equal |
|---|---|---|---|---|
| 2 | 1..4 | 15; 3,15; 45; 15,15 | 15; 3,15; 45; 15,15 | yes, yes, yes, yes |
| 3 | 1..4 | 21; 105; 2,2,2,126; 5,1365 | 21; 105; 2,2,2,126; 5,1365 | yes ×4 |
| 5 | 1 | 48 | 2, 24 | **no** (2-part Z/16 vs Z/2 × Z/8) |
| 5 | 2 | 12, 96 | 2, 2, 6, 48 | **no** (2-part) |
| 5 | 3 | 13104 | 2, 6552 | **no** (2-part) |
| 5 | 4 | 2, 8, 24, 960 | 4, 8, 24, 480 | **no** (2-part) |
| 7 | 1 | 9, 9 | 3, 3, 9 | **no** (**3-part**: Z/9² vs Z/3² × Z/9) |
| 7 | 2 | 63, 63 | 3, 21, 63 | **no** (3-part Z/9² vs Z/3² × Z/9; 7-parts equal) |
| 7 | 3 | 6, 6, 54, 54 | 6, 18, 18, 54 | **no** (3-part) |
| 7 | 4 | 2331, 2331 | 3, 777, 2331 | **no** (3-part Z/9² vs Z/3² × Z/9) |

In every cell the two groups have the same order; at ℓ = 5 they differ only in their 2-parts, at ℓ = 7 only in their 3-parts; at ℓ = 2, 3 they agree
for k ≤ 4.

**What agreement and disagreement mean.** (i) The groups of the product lattice differ from the graph's, so (L₀, M_ℓ) is **not** H₁(E₁) ⊕ H₁(E₂)
with Frobenius, as a Z[x]-module, for ℓ = 5, 7 (PROVED by the table: isomorphic modules have isomorphic cokernels of 1 − x^k; the cokernel
L/(1 − F^k)L of a Deligne / Centeleghe–Stix module is the group of F_{q^k}-points, and for E_i this is E_i(F_{ℓ^k}); from memory, Deligne 1969
"Variétés abéliennes ordinaires sur un corps fini", Howe 1995 for the points statement; ordinary at ℓ = 5, 7 since a_ℓ ≢ 0 mod ℓ). (ii) J₀(37)
is not E₁ × E₂ but isogenous to it by an isogeny of 2-power degree (from memory: both modular degrees are 2, X₀(37) → E_i are the quotients by
w₃₇ and by the hyperelliptic involution, and J₀(37) = (E₁ × E₂)/(graph of E₁[2] ≅ E₂[2]); Mazur–Swinnerton-Dyer 1974). A 2-power isogeny induces
isomorphisms on the odd parts of the groups of points. **Therefore the 3-parts of J₀(37)(F_{7^k}) are those of E₁ × E₂, namely Z/3 × Z/3 × Z/9
at k = 1, and the graph lattice gives Z/9 × Z/9: (L₀, M₇) is not H₁(J₀(37)_{F₇}) with Frob₇ either (nor T₃(J₀(37)) ⊗ Frob₇ after ⊗Z₃; PROVED
modulo the from-memory facts just listed).** The 2-part discrepancies at ℓ = 5 are undecidable here (the gluing changes 2-parts). (iii) So the
Pizer graph is a *third* source of a lattice in the isogeny class of J₀(p)_{F_ℓ}, different from both the product and the Jacobian, and it depends
on ℓ only through B(ℓ) acting on the one lattice Z[S_p]^0 ⊕ Z[S_p]^0. The place where it differs from the Jacobian in this example is the prime
3 = n = (p−1)/12, the order of the component group of J₀(37) at p = 37 (Mazur 1977, *Modular curves and the Eisenstein ideal*, II.11: Φ_p is cyclic of
order num((p−1)/12); from memory) and the discriminant of Ω|L₀ is n² = 9 (3.4). At ℓ = 5 the 3-parts agree (Z/3 at k = 1, (Z/3)² at k = 2, 4, Z/9 at
k = 3 on both sides), so the data are consistent with the conjecture that L₀ ⊗ Z_q ≅ T_q(J₀(p)) as Z_q[Frob_ℓ]-modules for q ∤ n and fail for q | n;
this is OPEN (NUMERICAL at one prime p; see 3.4 for the mechanism and `data-ladder.md` §1.2 for why it matters: the counts fix the isogeny class,
the graph fixes a lattice, and it is a different lattice from the one the Weil pairing on the curve fixes).

### 3.4 (c) Ω on the label lattice versus the Weil pairing on H₁(X₀(p), Z). SKETCHED, with one PROVED obstruction.

**Obstruction (PROVED).** In the basis (e_i − e_n, 0), (0, e_i − e_n), i < n, of L₀, Ω|L₀ = ((0, C), (−C, 0)) with C_{ij} = 1 + δ_{ij} the Gram matrix of
the root lattice A_{n−1} = v^⊥; det C = n, det(Ω|L₀) = n² (printed: 9, 36, 81). The Weil (intersection) pairing on H₁(X₀(p), Z) is unimodular. So
there is **no** isomorphism (L₀, Ω) ≅ (H₁(X₀(p), Z), ⟨,⟩) of symplectic lattices for n ≥ 2 — the index is n = |Φ_p|; rationally the two symplectic
spaces are isomorphic (same dimension), and with the step they are isomorphic as Q[x]-modules by 3.1.

**Identification (SKETCHED, from memory).** X₀(p) has semistable reduction at p whose special fibre is two copies of P¹ crossing at the n
supersingular points (Deligne–Rapoport 1973), so J₀(p) has purely toric reduction at p, and the character group of the torus is X = H₁(dual graph,
Z) = the cycle space of the graph with 2 vertices and the n edges e_i, i.e. X = Z[S_p]^0 (degree-zero divisors); Grothendieck's monodromy pairing
on X (SGA 7 IX) is Σ_i w_i a_i b_i, the thickness of the edge e_i being w_i — this is **Gross's pairing ⟨e_i, e_j⟩ = w_i δ_{ij} restricted to degree
zero** (Gross 1987 §3; Ribet 1990, "On modular representations of Gal(Q̄/Q) arising from modular forms", §3, uses exactly this X and this pairing as
the "supersingular module"), and its discriminant is |Φ_p| (Grothendieck), = n for p ≡ 1 mod 12 (Mazur). Hence:

    (L₀, Ω) = (X ⊕ X, ((0, C), (−C, 0))) with C the monodromy pairing of J₀(p) at p,  det = |Φ_p|² —

the same structure that `04z_cerednik_drinfeld.tex` found for the LPS square complex ("Ω_M is the evaluation pairing pulled back along (a, b) ↦
(a, Mb) after a splitting, and det Ω_M = (det M)² obstructs an integral identification"), now in the elementary case: the Hecke algebra T acts on X,
Frob_ℓ on T_q(J₀(p)) ⊗ Q is a 2 × 2 matrix over T ⊗ Q with trace T_ℓ and determinant ℓ, and (X ⊕ X, M_ℓ) is its companion form. The Raynaud
sequence 0 → X^∨ ⊗ Z_q(1) → T_q J₀(p) → X ⊗ Z_q → 0 is local at p and is *not* a Frob_ℓ-filtration (ℓ ≠ p), so the companion is a noncanonical
one-operator realisation, exactly as in 04z. When X ⊗ Z_q is free of rank one over T ⊗ Z_q (Mazur 1977, II.16–17: X is locally free of rank 1 over T at
Gorenstein maximal ideals; from memory) and T_q J₀(p) is free of rank 2 over T ⊗ Z_q with Frob_ℓ having a cyclic vector (e.g. ρ_m(Frob_ℓ) not scalar
mod m), one gets L₀ ⊗ Z_q ≅ T_q J₀(p) as Z_q[Frob_ℓ]-modules; the Eisenstein primes q | n = |Φ_p| are where these hypotheses are delicate, and q = 3 at
p = 37 is where 3.3 found the failure. I have not proved the conditional statement; it is the natural explanation of the table and is left OPEN.
The Weil pairing on T_q J₀(p) is perfect, Ω|L₀ ⊗ Z_q is perfect iff q ∤ n: so even where the modules might agree, the symplectic forms agree at most
up to the index n, never integrally when q | n.

---------------------------------------------------------------------------------------------------------------------

## §4. P4 — what this says for ζ (HEURISTIC except where marked)

**(i) Adelic lattice, one line each.** Vertices of G(p, ℓ) (PROVED, §2): S_p = B^×(Q)\B^×(A_f)/Ô^× = Γ\(GL₂(Q_ℓ)/Q_ℓ^×GL₂(Z_ℓ)), rational points of a
definite form modulo an adelic compact, the symplectic geometry living in GL₂(Q_ℓ) acting on lattices of Q_ℓ² by similitudes of the Weil form.
For G_m: Q^×\A_f^×/Ẑ^× = {1} (A_f^× = Q^×_{>0}Ẑ^×), the "tree" at ℓ is the line Q_ℓ^×/Z_ℓ^× = ℓ^Z (a 2-regular tree, q = 1), the global lattice
Z[1/ℓ]^×/{±1} = ℓ^Z acts by the unit shift, and the quotient is **one vertex with one loop**: Ihara–Bass with q = 1 gives det(1 − Au + u²) = (1 − u)²
— the trivial pair (1, q) degenerates to (1, 1) and the nontrivial part is empty. So the Pizer construction, applied to G_m, has genus 0: no
finite-rank H¹, no Weil form to be positive, and all of ζ's zeros are "global" (`data-ladder.md` §3). What the modular case has and G_m lacks is a
non-abelian B^×(Q) whose double coset is a set of size g + 1 > 1, i.e. a non-trivial class set; the zeros of P_{p,ℓ} live in the degree-zero part of
Z[class set]. There is no ℓ-local reason for them to exist — they are the h − 1 nontrivial Hecke eigenlines of a *global* class set, which is why the
same lattice Z[S_p]^0 serves every ℓ at once (3.3 (iii)). HEURISTIC conclusion: a finite-rank H¹ for ζ would need a global, non-abelian class set
with a Hecke action; the abelian double coset of G_m is a point.

**(ii) The two qunaughts.** Local: T_ℓ(E) ⊂ V_ℓ(E), self-dual for the Weil pairing e_{ℓ^∞}, a vertex of T_ℓ; global: L₀ = Z[S_p]^0 ⊕ Z[S_p]^0 with Ω and
M_ℓ, rationally H¹(X₀(p)) with Frob_ℓ. The brief's proposed identification "T_q(J₀(p)) is the q-adic completion of the global lattice" is: **true
rationally** for every q ≠ ℓ, p (3.1: T_q J ⊗ Q ≅ L₀ ⊗ Q_q as Q_q[Frob_ℓ]-modules, semisimple with equal characteristic polynomials), **false
integrally** (PROVED at p = 37, ℓ = 7, q = 3 modulo the from-memory facts of 3.3: coker(1 − Frob₇ | T₃J₀(37)) = J₀(37)(F₇)[3^∞] = Z/3 × Z/3 × Z/9 while
coker(1 − M₇ | L₀ ⊗ Z₃) = Z/9 × Z/9), and **not compatible with the two symplectic forms** at q | n (Weil pairing perfect, Ω|L₀ of discriminant n²).
The local qunaught at a vertex and the global one are therefore not "one object": T_ℓ(E) is the Tate module of one vertex curve, L₀ is (two copies
of) the character group of the toric reduction of the *Jacobian of the modular curve* at p, and the symplectic structure of L₀ is the monodromy
pairing at p, not the Weil pairing at ℓ. They meet only through the double coset: the vertex set of the graph on which L₀ lives is the Γ-orbit
space of the local qunaughts. In the record's terms (`data-ladder.md` §1.2): overlaps see the order, the Weil pairing sees the class, and the graph
sees a third thing — the Hecke module X with its monodromy form — which fixes a lattice in the isogeny class that is in general neither the
product nor the Jacobian.

---------------------------------------------------------------------------------------------------------------------

## Correction ledger (what the brief got wrong or left open, and what was settled)

1. **Ihara–Bass for the Pizer graph.** The record's formula ζ = (1 − u²)^{−(|E|−|V|)} det(1 − Au + ℓu²)^{-1} is false for the Pizer graph with the
   dual-isogeny reversal whenever some O_i contains √−ℓ: the loops with φ² = −ℓ are half-edges. Correct: det(1 − uB_H) = (1 + u)^f (1 − u²)^{(N−f)/2−n}
   det(1 − B(ℓ)u + ℓu²), N = (ℓ+1)n, f = #half-loops (§1.3; refuted numerically at (37, 2), (37, 5), (73, 5), (73, 7), (109, 2); N = 9 and 27 are odd).
   The "+ℓu²" is right: a half-loop contributes 1 to the degree and 1 to A_ii, a loop pair 2 and 2, so SᵀS = ℓ + 1 always.
2. **Symmetrisation.** W^{−1/2}B(ℓ)W^{1/2} (not W^{1/2}BW^{−1/2}) for B acting on functions; the Eisenstein vector is (1,…,1) on functions and (1/w_i)
   on divisors (§1.1).
3. **Mass.** Σ 1/|O_i^×| = (p−1)/24, i.e. Σ 1/w_i = (p−1)/12 (checked at all five p); the brief did not state it. The counts #S_p = ⌊p/12⌋ + {0,1,1,2}, the
   weights, the genus g = #S_p − 1 (all p tested, via mfdim), Eichler–Shimura's form, the model of X₀(37) and the Cremona labels 37a1 (a₂ = −2,
   rank 1), 37b1 (a₂ = 0, rank 0) are all **correct as stated**. Note 1728 ≡ 1 mod 11 (the j = 1 vertex of p = 11 is j = 1728, w = 2).
4. **P2's "when h(O) = 1".** Unnecessary: Γ\T_ℓ = G(p, ℓ) for every p with Γ from any one maximal order (§2.2); the two colours are always identified;
   the quotient is a graph of groups with vertex groups of orders w_i when p ≢ 1 mod 12.
5. **P3's premise "nontrivial label space ≅ H¹ of the modular curve"**: true over Q, false over Z (§3.3–3.4); the trivial mode does not split off
   integrally (index n²).
6. **P4(ii)'s "the Tate module of the Jacobian is the ℓ-adic completion of the global lattice"**: false integrally (§4(ii)).
7. Environment: `elldata` is absent (the Cremona equations were used and their conductors/a_ℓ verified); `polmodular(ℓ, 0, j)` rejects j ∉ F_p, so Φ_ℓ
   is computed over Z and substituted; the ℓ-division polynomial over F_{p²} is *not* a product of kernel polynomials when p ≡ ±1 mod ℓ (p = 109,
   ℓ = 5), so subgroups must be built from points.

## Numerical checks for the blind lane

Commands (venv python = the interpreter named in the brief):
`cd notes/astra-2026-10-27/pizer/fable && <venv>/bin/python checks/pizer_graph.py` (≈ 1–2 min; `checks/pizer_graph.py 37` for p = 37 only),
`<venv>/bin/python checks/pizer_quotient.py`, `<venv>/bin/python checks/label_lattice.py`.

1. p = 37, ℓ = 2: B(2) = [[0,2,1],[2,0,1],[1,1,1]] (vertices j = 30t+18, 7t+25, 8 ∈ F_{37²}), charpoly x³ − x² − 6x = (x−3)·x·(x+2), P_{37,2}(u) =
   4u⁴ + 4u³ + 4u² + 2u + 1, #X₀(37)(F₂) = 5; Hashimoto N = 9, f = 1, det(1 − uB_H) = −8u⁹ − 4u⁸ + 12u⁷ + 8u⁶ − 3u⁴ − 4u³ − 2u² + 1 =
   (1+u)(1−u²)·(1−u)(1−2u)·P_{37,2}(u).
2. p = 109, ℓ = 7: #X₀(109)(F₇) = 8, N = 72, f = 0, the degree-72 polynomial det(1 − uB_H) equals (1 − u²)^{27} det(1 − B(7)u + 7u²) exactly;
   p = 73, ℓ = 7: f = 2, N = 48, (1+u)²(1−u²)^{17} det(1 − B(7)u + 7u²).
3. X₀(37): y² = −x⁶ − 9x⁴ − 11x² + 37 has Frobenius characteristic polynomial x⁴ + 2x³ + 10x² + 10x + 25 over F₅ and x⁴ − 8x³ + 58x² − 184x + 529
   over F₂₃, both equal to ∏_f (x² − a_ℓ(f)x + ℓ); point counts 8 and 16.
4. Quaternion side p = 37: h = 3, |O_i^×| = (2, 2, 2), mass 3/2, ideal-class B(5) = [[2,2,2],[2,1,3],[2,3,1]] ↔ Φ₅ matrix [[1,3,2],[3,1,2],[2,2,2]] under
   (j₀, j₁, j₂) ↦ (1, 2, 0); half-loops (1, 0, 2, 0) for ℓ = 2, 3, 5, 7 on both sides.
5. p = 37, ℓ = 7, k = 1: L₀/(1 − M₇)L₀ = Z/9 × Z/9, E₁(F₇) × E₂(F₇) = Z/9 × (Z/3)², both of order 81 = #J₀(37)(F₇); ℓ = 2, k = 4: both Z/15 × Z/15.
6. det(Ω|L₀) = n² = 9, 36, 81 for p = 37, 73, 109; #J₀(109)(F_{7⁴}) = 1126236986928850407683097600 with invariant factors 4, 4, 120, 586581764025442920668280.

## What this changes in the notebook

Candidate rows (none registered; cross-family review wanted):

| id | kind | status | statement |
|---|---|---|---|
| `thm:pizer-ihara-zeta-x0p` | thm | PROVED (from Eichler, Eichler–Shimura, Weil; cited from memory) | det(1 − B(ℓ)u + ℓu²) = (1−u)(1−ℓu)P_{p,ℓ}(u) for all p, ℓ ≠ p; G(p,ℓ) Ramanujan = Weil's RH for J₀(p)/F_ℓ; 20 exact cells |
| `lem:ihara-bass-half-loops` | lem | PROVED | det(1 − uB_H) = (1+u)^f(1−u²)^{(N−f)/2−n} det(1 − Au + qu²) for a quotient of a tree with f inverted edges; the Pizer graph has f = Σ_i #{φ ∈ O_i: φ² = −ℓ}/2 |
| `prop:pizer-tree-quotient` | prop | PROVED (strong approximation) | G(p,ℓ) = Γ\T_ℓ, Γ = O[1/ℓ]^×/Z[1/ℓ]^×, for every p; one component, colours identified, vertex groups of order w_i; exact at p = 37 on the quaternion side |
| `prop:pizer-label-space-h1` | prop | PROVED (rational) | (L₀ ⊗ Q, M_ℓ) ≅ (H¹(X₀(p)), Frob_ℓ); L₀ = Ω^⊥ of the trivial plane, index n² |
| `num:pizer-label-lattice-smith` | num | NUMERICAL / REFUTED | the graph lattice is not H₁(E₁)⊕H₁(E₂) (p = 37, ℓ = 5, 7) and not H₁(J₀(37)) (ℓ = 7, 3-part); 48 Smith forms printed |
| `prop:pizer-omega-monodromy` | prop | PROVED (obstruction) / SKETCHED (identification) | det Ω|L₀ = n² = |Φ_p|²; Ω|L₀ is the doubled monodromy pairing on X = Z[S_p]^0, not the Weil pairing on H₁(X₀(p),Z) |
| `conj:pizer-lattice-away-from-eisenstein` | conj | OPEN | L₀ ⊗ Z_q ≅ T_q J₀(p) as Z_q[Frob_ℓ]-modules iff q ∤ (p−1)/12 (p ≡ 1 mod 12) |

One-line annotations: `graph-ihara.md` §2–§3: "the K₄/E coincidence of spectra is replaced, on the Pizer graph G(p, ℓ), by the exact identity
det(1 − B(ℓ)u + ℓu²) = (1−u)(1−ℓu)P_{p,ℓ}(u) (Eichler + Eichler–Shimura), with the graph's phase space rationally H¹(X₀(p)) and Frobenius the step;
the record's Ihara–Bass formula needs the half-loop factor (1+u)^f(1−u²)^{−f/2} on this graph" (2026-10-27 Fable lane P). `graph-ihara.md` §9 row
"Ihara–Bass": add "for graphs with inverted edges see `lem:ihara-bass-half-loops`". `data-ladder.md` §0: new rung "Pizer graph G(p, ℓ): L = Z[S_p]^0
⊕ Z[S_p]^0 (the character group of the toric reduction of J₀(p) at p, doubled), step M_ℓ, Ω = monodromy pairing doubled (disc |Φ_p|²), vacuum
exists (Weil for J₀(p)/F_ℓ), arithmetic J: the lattice is a third one in the isogeny class — neither the Jacobian's nor the product's". `data-ladder.md`
§1.2: "a graph is a third source of a lattice: it sees the Hecke module X with its monodromy form (not the order, not the class); at p = 37, ℓ = 7 it
differs from H₁(J₀(37)) at the Eisenstein prime 3". `04z` header: the elementary cousin (X₀(p) at p, 2-vertex dual graph; Hecke graph at ℓ) confirms
the "det Ω_M = (det M)²" obstruction in genus 2, 5, 8.

Next step: (1) cross-family REFUTE review of §1.3 (the half-loop lemma and its reversal construction) and §3.3 (the Deligne/points identification
and the 2-power-gluing claim for J₀(37), both from memory); (2) decide `conj:pizer-lattice-away-from-eisenstein`: compute J₀(p)(F_{ℓ^k}) group
structures directly (genus-2 Jacobian arithmetic over F_{ℓ^k} for p = 37 — not in PARI; Magma/Sage) and compare at q = 2 and at q | n for p = 73 (n = 6),
109 (n = 9); or prove the conditional statement of 3.4 from Mazur's freeness results; (3) the weighted zeta (p ≢ 1 mod 12) as Bass's zeta of the
graph of groups, with the (1 + u)^f-type factors for the torsion stabilisers written out and checked at p = 11, 101.
