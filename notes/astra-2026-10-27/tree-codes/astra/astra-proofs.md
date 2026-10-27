# Local lattice codes, tree translations, and Ihara orbit traces

Author: `codex:gpt-6-astra`

Date: 2026-10-27. Blind prover, topic T. No other prover's work was consulted. This is a proposed proof record, not registration; cross-family review remains required.

Conventions: the round and lane briefs apply, subject to explicitly proved corrections below. The additive character has conductor Z_p and Haar measure gives Z_p volume one. All codes use the trivial stabiliser character. Other characters give displaced codes and are extra data. In graph formulas p=q, and the binding label convention is M=((A,-pI),(I,0)), Ω=((0,I),(-I,0)), even where older record pages use different coordinates.

The constructions here use lattice inclusions, Weyl commutators, tree actions and determinant/trace identities. No zeta function is defined or inferred from a vacuum overlap. Inner products occur only in verifying the requested finite-dimensional MUB statement.

## 1. T1 — colours and canonical code dimensions

**SHARPENED / PROVED:** the duality and colour claim is true with the unique determinant-normalised representative. **REFUTED:** arbitrary homothetic representatives give canonically isomorphic codes, or are related by D_c. The phase convention proposed in §0 also has the wrong sign.

### 1.1 Correct Weyl section (PROVED)

With the stipulated W(u,v)f(x)=ψ(vx)f(x+u), direct multiplication gives

\[
W(u,v)W(u',v')=\psi(uv')W(u+u',v+v').
\]

Consequently the symmetric section is

\[
\mathsf W(u,v)=\psi(uv/2)W(u,v),\qquad
\mathsf W(z)\mathsf W(z')=\psi(\omega(z,z')/2)\mathsf W(z+z').
\]

The **plus** sign is forced by the given order of translation and modulation. For odd p and ω(L,L)⊂Z_p the cocycle restricts to one, so this is a representation of the additive group L. Set

\[
\mathcal C_L=\{f:\mathsf W(\lambda)f=f\ (\lambda\in L)\}.
\]

Smallest allowed prime counterexample to the proposed minus section: at p=3 let L have columns (1/3,1/3),(0,3). Its determinant is one, so it is self-dual. For z=(1/3,1/3), the ratio W_-(z)^2/W_-(2z) is ψ(2/9)≠1. Printed in `checks/output_tree_codes.txt`. The commutator convention of the brief itself is correct.

### 1.2 Dual lattice and normalisation (PROVED)

Let L=gZ_p² and d=v_p(det g). For x=gy and z∈Z_p²,

\[
\omega(x,gz)=\det(g)\omega(y,z).
\]

Since Z_p² is self-dual, this is integral for all z precisely when y∈(det g)^{-1}Z_p². Thus, as equality of subsets of V,

\[
L^\perp=(\det g)^{-1}L=p^{-d}L.
\]

The last equality uses multiplication of a Z_p-module by a unit. In particular L⊂L^⊥ iff d≥0, and then [L^⊥:L]=p^{2d}.

Let k∈{0,1} be d modulo two and define

\[
L^{\mathrm{can}}=p^{(k-d)/2}L.
\]

This has determinant valuation k. Replacing L by cL changes d to d+2v_p(c), and produces the same subset L^can: the remaining scalar is a unit. Changing the basis of L also does nothing. Moreover any representative of [L] with determinant valuation k is exactly L^can. **There is a unique lattice here, not a choice of isomorphism.** Its stabiliser code, with the fixed section and trivial character, is literally the same subspace of L²(Q_p).

For completeness, dim C_L=p^d for any integral symplectic lattice of determinant valuation d≥0. Choose a basis with determinant exactly p^d by rescaling one column by a unit. It is h diag(p^d,1) with h∈SL₂(Q_p). Weyl covariance under h transports the standard code to C_L. This covariance can be constructed from Fourier transformation, multiplication by quadratic characters, and D_a, which generate the rank-one Weil representation; the implementer is unique up to phase. This standard fact is used only for code transport, not for any trace identity. Bibliographic source from memory: A. Weil, *Sur certains groupes d'opérateurs unitaires*, Acta Mathematica 111 (1964), the Heisenberg representation and symplectic intertwiners.

For L_d=p^dZ_p⊕Z_p, invariance under (0,Z_p) forces support in Z_p, and invariance under (p^dZ_p,0) forces constancy on p^d-cosets. Hence C_(L_d) is the space of functions on Z_p/p^dZ_p and has dimension p^d, proving the formula without any formal infinite-dimensional index count. Thus k=0 gives a qunaught and k=1 gives one p-dimensional qudit.

An index-p inclusion changes determinant valuation by one, hence changes k. This proves that code dimension gives the tree's bipartition. It does **not** give a colouring invariant under all PGL₂(Q_p): an element of odd determinant valuation exchanges colours. SL₂(Q_p) preserves them.

### 1.3 What homothety does not mean (REFUTED)

The smallest prime example is [Z_3²]=[3Z_3²], but their unnormalised codes have dimensions one and nine. D_3 sends Z_3² to 3^{-1}Z_3⊕3Z_3, whose determinant valuation is zero, whereas 3Z_3² has determinant valuation two. Scalar homothety cI multiplies ω by c²; a Clifford squeeze diag(c^{-1},c) preserves ω. They are different operations. Code independence in T1 is therefore exactly the uniqueness of L^can, and not an invariance under scalar homothety on unnormalised codes.

**NUMERICAL / exact checks.** `python3 notes/astra-2026-10-27/tree-codes/astra/checks/tree_codes.py`: for each p=3,5,7, thirty rational lattice bases verify the dual equality, normalisation, index and unit independence using mutual integral transition matrices. The two counterexamples above are printed as well.

## 2. T2 — neighbouring lattices and mutually unbiased stabiliser bases

**PROVED after the phase correction and a notation clarification:** “1_L” must mean a normalised vector φ_L in the qunaught ray C_L, not literally the indicator of a subset L⊂Q_p² viewed as a function on Q_p. For non-split L the vector can be a quadratic character times an indicator. Its phase is immaterial. Orthonormality requires normalisation.

### 2.1 The lattice incidence (PROVED)

Let M=M^can have determinant valuation one. Then M^⊥=p^{-1}M and

\[
E=M^\perp/M\cong\mathbb F_p^2,\qquad
\langle\bar x,\bar y\rangle=p\omega(x,y)\pmod p
\]

is a well-defined nondegenerate alternating form. Indeed changing x by M changes pω(x,y) by pZ_p, and the radical is M by double duality.

The inverse image L of a line in E has [L:M]=p and determinant valuation zero. An alternating form vanishes on a line, so ω(L,L)⊂Z_p, and L=L^⊥. Conversely any self-dual L between M and M^⊥ has this index and maps to a line. These are exactly p+1 lattices.

They are precisely the normalised representatives of the neighbours of [M]. In one direction, M has index p in L, giving adjacency. In the other, write a neighbour as [K] with pM⊂K⊂M and [M:K]=p; K has determinant valuation two, so its normalised representative is L=p^{-1}K, which lies between M and p^{-1}M. This proves both surjectivity and that no vertex is duplicated.

Dually, for a self-dual L its neighbours have unique representatives M⊂L of index p. They correspond to the lines M/pL of L/pL, and C_L⊂C_M since the former has more stabilisers. Thus its qunaught vector lies in every neighbouring code.

### 2.2 The basis and MUB claim (PROVED)

The operators \(\mathsf W(x)\), x∈M^⊥, preserve C_M. Modulo M and scalar phases they give the irreducible p-dimensional Weyl–Heisenberg representation of E, with commutator ψ(ω(x,y)). For a line l=L/M, its p commuting operators decompose C_M into one-dimensional character spaces. The trivial character space is C_L. The map

\[
M^\perp/L\longrightarrow\widehat{L/M},\qquad
x\longmapsto\bigl(\lambda\mapsto\psi(\omega(\lambda,x))\bigr)
\]

is an isomorphism by nondegeneracy. Consequently the p vectors \(\mathsf W(x)\phi_L\), x∈M^⊥/L, are unit vectors in distinct character spaces and form an orthonormal basis. Representatives of a coset change only a scalar phase; W instead of \(\mathsf W\) gives the same rays.

Here is a short proof of mutual unbiasedness that is independent of the chirp formulas. In the p-dimensional representation, every noncentral Weyl operator has trace zero: conjugate it by a Weyl operator with nontrivial commutator to multiply its trace by a nontrivial p-th root of unity. A character projector of a line has the form

\[
P_{l,\chi}=p^{-1}\sum_{z\in l}\chi(z)^{-1}\mathsf W_l(z),
\]

where the section on l is chosen to be a representation. It has trace one and is a rank-one orthogonal projector. If l≠l', the only pair z∈l,z'∈l' with z+z'=0 is z=z'=0. It follows that

\[
\operatorname{Tr}(P_{l,\chi}P_{l',\chi'})=p^{-2}\operatorname{Tr}(I)=1/p.
\]

This is exactly the squared inner product of the corresponding unit vectors. No overlap formula for a zeta is involved.

### 2.3 Explicit standard MUBs (PROVED and NUMERICAL)

Choose M=pZ_p⊕Z_p, so M^⊥=Z_p⊕p^{-1}Z_p. C_M consists of functions supported in Z_p and constant on pZ_p-cosets. Identify C^p with C_M by the orthonormal basis

\[
e_x=\sqrt p\,1_{x+p\mathbb Z_p},\qquad x\in\mathbb F_p.
\]

The lines and associated self-dual lattices are

\[
L_\infty=p\mathbb Z_p\oplus p^{-1}\mathbb Z_p,\qquad
L_t=M+\mathbb Z_p(1,t/p)\quad(t\in\mathbb F_p).
\]

For L_∞ the displaced qunaught basis is the computational basis. For L_t it is, in these coordinates,

\[
b_{t,b}(x)=p^{-1/2}\zeta_p^{-tx^2/2+bx},\qquad b\in\mathbb F_p,
\]

with arithmetic in F_p. In particular b_(t,0) is fixed by \(\mathsf W(1,t/p)\), since its action is ζ_p^(tx+t/2)f(x+1). All other columns are obtained by modulation. These are the standard p quadratic-phase Weyl–Heisenberg MUBs, together with the computational basis. The symplectic transport used in T1 supplies this description for every M.

`checks/mub.py` prints every basis (as an exact exponent table), every within-basis complex Gram matrix and every cross-basis probability matrix for p=3,5,7. Computation is complex128, with an asserted error tolerance of 10^{-12}; the largest observed within-basis error is 3.33066907387546962×10^{-16} and largest cross-basis error is 2.22044604925031308×10^{-16}. There are respectively 4,6,8 bases and 6,15,28 unordered pairs. Full output is `checks/output_mub.txt`.

## 3. T3 — Lagrangian ends, apartments, and the two dilation parameters

**SHARPENED / PROVED, with two literal refutations:** a squeeze of valuation zero fixes its apartment pointwise, and a general hyperbolic PGL₂ element need not be a symplectic Clifford. Its projective dilation parameter is the **square** of a Clifford squeeze parameter when a lift exists.

### 3.1 Boundary and split lattices (PROVED)

Every line in the two-dimensional alternating space V is Lagrangian. Fix L₀=Z_p². A line l has a primitive vector v∈L₀, unique up to a unit after its scale is fixed, and determines the ray

\[
[\mathbb Z_pv+p^nL_0],\quad n\ge0.
\]

Conversely a ray from [L₀] can be represented by such decreasing lattices: at level n it specifies a primitive rank-one direct summand modulo p^n, and these summands are compatible. Their inverse limit is a primitive line in L₀; its Q_p-span recovers l. Different rays from the same origin cannot merge again in a tree. This identifies ∂T_p with P¹(Q_p), equivariantly for PGL₂(Q_p). The same lattice description proves the usual locally compact topology agrees with the end topology.

For two distinct lines choose e₁,e₂ on them with ω(e₁,e₂)=1. The lattices split by these lines are exactly

\[
L_{r,s}=p^r\mathbb Z_pe_1\oplus p^s\mathbb Z_pe_2.
\]

Their homothety classes depend only on n=s−r. Consecutive n give neighbours, so they form a bi-infinite geodesic with these endpoints. The uniqueness of a path between two vertices in a tree implies uniqueness of the geodesic between distinct ends. Thus an **unordered** pair of distinct lines is an unoriented geodesic; ordering the pair orients it. This is the apartment associated to the split torus preserving the pair.

### 3.2 Symplectic versus projective dilation (PROVED / REFUTED)

Writing a=p^m u with u∈Z_p^×, diag(a^{-1},a) sends (r,s) to (r−m,s+m), hence sends n to n+2m. Its signed displacement on the oriented apartment is 2m and its translation length is 2|m|. For m≠0 it fixes no vertex; for m=0 it fixes every apartment vertex. The identity a=1 is the smallest counterexample to the unqualified “fixes no vertex”.

The element diag(1,p) sends n to n+1 and exchanges the two code colours. More generally diag(1,λ), λ=p^ℓu with ℓ>0, is a translation by ℓ composed with diag(1,u), which fixes the apartment pointwise (but can act on its attached branches).

This is a **projective dilation/similitude**, not in general a Clifford of the fixed symplectic phase space. A PGL₂ element represented by diag(1,λ) has an SL₂(Q_p) lift iff λ is a square in Q_p^×. When λ=a², one lift is diag(a^{-1},a), implemented by D_a. Having even valuation is necessary but not sufficient: at p=3, λ=18 has valuation two and nonsquare unit part. The smallest odd-length obstruction is λ=3. These are printed by `tree_codes.py`.

Therefore “every hyperbolic element is a squeeze composed with a unit” is true if *squeeze* means a projective split-torus translation diag(1,p^ℓ). It is false if it means the symplectic squeeze D_(p^ℓ) specified in the setting. This distinction is decisive in T4(b).

### 3.3 Hyperbolicity from the Newton polygon (PROVED)

Take a representative g∈GL₂(Q_p) and put t=v_p(tr g), d=v_p(det g), with t=+∞ when the trace is zero. Its characteristic polynomial is X²−TX+Δ. Its roots have different valuations precisely when 2t<d; the Newton polygon then has two segments of horizontal length one, giving valuations t and d−t. In particular both are integers. To see explicitly that the roots lie in Q_p, substitute X=p^tY. The polynomial becomes

\[
Y^2-(T/p^t)Y+\Delta/p^{2t},
\]

whose reduction has the distinct roots 0 and T/p^t in F_p. Hensel's lemma gives both roots in Z_p. Alternatively, a nonsplit quadratic has Galois-conjugate roots of equal valuation, since the valuation on a finite p-adic extension is unique. This also excludes a nonsplit unequal-slope case.

Let α,β be ordered with v_p(α)<v_p(β). Diagonalising over Q_p and dividing by α gives diag(1,λ), λ=β/α, and

\[
\ell(g)=v_p(\lambda)=d-2t>0.
\]

It translates its split apartment by this many edges. For any vertex x outside the apartment A, the unique paths to A and their translates give

\[
d(x,gx)=\ell(g)+2d(x,A).
\]

Indeed their projections to A are distinct and separated by ℓ(g), so the concatenation has no backtracking. This proves both that ℓ is the translation length and that the vertices realising it are exactly the split lattices.

### 3.4 Equal slopes: a fixed vertex or an inverted edge (PROVED)

If 2t≥d the slopes are both d/2. When d is even, rescale g to h with determinant a unit and integral trace. Unless h is scalar, choose v with v,hv independent. The lattice L=Z_pv+Z_phv satisfies hL=L by the characteristic equation and unit determinant. A scalar fixes every vertex after homothety. Thus g fixes a vertex.

When d is odd, rescale so v_p(det h)=1 and v_p(tr h)≥1. In a cyclic basis as above, hL⊂L has index p. The characteristic equation gives h²L⊂pL; their indices agree, so h²L=pL. Hence h exchanges [L] and [hL], fixing the midpoint of their edge. In this case it fixes **no vertex**, by colour parity. “Fixes an edge” must mean setwise, allowing inversion; the example ((0,1),(p,0)) exhibits this. On the geometric tree its translation length is zero, while its minimum displacement over vertices is one. The assumptions on Γ in T4 exclude such elements.

### 3.5 Constructive tree check (exact arithmetic; finite p-adic approximation)

`tree_codes.py` generates ten seeded random integer matrices for each of p=3,5. It prints all entries, trace/determinant valuations, eigenvalue slopes, ratio valuation, and a fixed-vertex or inverted-edge witness in elliptic cases. There are two hyperbolic matrices in the p=3 sample and five in the p=5 sample. Five additional diagnostic matrices per prime include diag(1,p), diag(1,p²), a case with nonrational p-adic eigenlines, an edge inversion, and the identity.

For every hyperbolic case, simple Hensel lifting to forty p-adic digits constructs rational eigenline approximants. At each of seven consecutive split lattices, the script checks **exactly** that gL_n and L_(n+ℓ) have the same local Hermite form, that consecutive vertices are adjacent, and that their displacement is ℓ. A neighbour leaving the apartment has displacement ℓ+2. The HNF procedure removes the minimum entry valuation and performs upper triangular reduction over Z_p, using unit inverses; it is not ordinary integer HNF incorrectly applied over Z_p. It verifies its own output by mutual integral transition matrices. Thus all stated vertex equalities are exact rational lattice tests, rather than floating-point comparisons of p-adic approximants. The Newton-polygon theorem supplies the infinite-axis assertion.

Bibliographic reference from memory for the standard tree dictionary: J.-P. Serre, *Trees*, English translation (1980), Chapter II, §1. The proofs above state the needed local arguments explicitly.

## 4. T4 — Ihara conjugacy classes and the corrected Lefschetz identity

### 4.1 T4(a): Euler product over oriented primitive translations

**PROVED:** Ihara's Euler product is the product over primitive hyperbolic Γ-conjugacy classes, with inverse classes counted separately. Calling these projective squeezes is consistent with T3; calling all of them symplectic Clifford squeezes is not.

Let Γ⊂PGL₂(Q_p) be discrete, torsion-free, cocompact, and without inversions as in the brief. A vertex stabiliser in PGL₂ is compact. Its intersection with Γ is finite (a discrete subgroup of a compact group) and therefore trivial. The action is free on vertices and edges and T_p→Y is the universal covering. The quotient may have loops or parallel edges; the oriented-edge formulation accommodates both. Every nonidentity element of Γ is hyperbolic by T3: a vertex-fixing element would be trivial, and an edge-inverting element is excluded.

A cyclically non-backtracking closed walk lifts to the segment from x to γx on the axis of a nonidentity γ. Repeating it in both directions gives that axis. Moving the lift conjugates γ, and changing the distinguished point along the closed walk leaves its conjugacy class unchanged. Conversely the quotient of the axis segment from x to γx is cyclically reduced. These operations are mutually inverse between **oriented closed walks modulo cyclic rotation** and conjugacy classes [γ]≠[1]. Reversing the walk replaces γ by γ^{-1}. These classes are not identified: a conjugacy taking a translation to its inverse would reverse its axis and fix a point, impossible for this free action.

The centraliser C_Γ(γ) preserves the oriented axis and injects into its translation group Z: the kernel fixes vertices. Hence

\[
C_\Gamma(\gamma)=\langle\gamma_0\rangle,
\qquad \gamma=\gamma_0^m,\quad m\ge1,
\]

where γ₀ is the uniquely oriented primitive generator and ℓ(γ)=mℓ(γ₀). A repeated prime walk of total length k=mℓ₀ has **ℓ₀**, not k, distinct edge-rooted sequences. Its repeats agree after ℓ₀ cyclic shifts. Therefore

\[
N_k=\operatorname{Tr}B^k
 =\sum_{\substack{[\gamma_0]\text{ primitive}\ m\ell(\gamma_0)=k}}\ell(\gamma_0)
 =\sum_{d\mid k}dP_d,
\quad
P_k=\frac1k\sum_{d\mid k}\mu(d)N_{k/d}.
\]

Here P_d counts oriented primitive cycles modulo cyclic rotation. Formal logarithms now give

\[
\det(1-uB)^{-1}
 =\exp\left(\sum_{k\ge1}\frac{N_k}{k}u^k\right)
 =\prod_{[\gamma_0]\text{ primitive}}(1-u^{\ell(\gamma_0)})^{-1}.
\]

This holds as a formal identity and analytically for |u|<1/p. It is the required map from a quotient of the symplectic lattice tree to a zeta function, without a vacuum overlap.

**Centraliser-volume correction (PROVED).** With unit edge length the relevant volume is

\[
\operatorname{vol}\bigl(C_\Gamma(\gamma)\backslash\operatorname{Axis}(\gamma)\bigr)=\ell(\gamma_0).
\]

Equivalently, identify the ambient centraliser with Q_p^× and give its unit subgroup Haar volume one; then C_Γ(γ) has covolume ℓ(γ₀). The expression “Γ_γ\backslash⟨γ⟩” in the brief is not this quotient. In the other direction C_Γ(γ)/⟨γ⟩ has order m, not ℓ(γ₀).

Bibliographic references from memory: Y. Ihara, *On discrete subgroups of the two by two projective linear group over p-adic fields*, J. Math. Soc. Japan 18 (1966), the zeta function of a uniform tree lattice; Serre, *Trees* (1980), free tree actions and graph fundamental groups. The covering/counting argument above proves the version used here.

### 4.2 T4(b): flat trace, boundary germ, and a factor-of-two refutation

**REFUTED as a statement about the original symplectic squeeze of γ. PROVED with a precise replacement:** the graph weight is the local half-density Lefschetz trace of γ on the **affine boundary coordinate at an attracting end**. That coordinate has multiplier λ, whereas the original Clifford parameter is a square root of λ when one exists.

#### The local trace formula (PROVED)

For a∈Q_p^×, a≠1, the kernel of D_a on Schwartz–Bruhat functions is

\[
K_a(x,y)=|a|_p^{1/2}\delta(y-ax).
\]

Its restriction to the diagonal is well defined as a distribution because the linear map x↦(1−a)x is invertible. Explicitly, for χ∈S(Q_p), let δ_N(z)=p^N1_(p^N Z_p)(z). Change variables y=(1−a)x to get

\[
\begin{aligned}
\lim_{N\to\infty}|a|_p^{1/2}
 \int\chi(x)\delta_N((1-a)x)\,dx
 &=\frac{|a|_p^{1/2}}{|1-a|_p}
   \lim_{N\to\infty}\int\chi(y/(1-a))\delta_N(y)\,dy\\
 &=\frac{|a|_p^{1/2}}{|1-a|_p}\chi(0).
\end{aligned}
\]

The last expression is eventually constant, not just convergent, since χ is locally constant near zero. Choose any χ identically one near zero. The **flat/local trace** is therefore

\[
\tau(a):=\operatorname{Tr}^{\flat}D_a
 =\frac{|a|_p^{1/2}}{|1-a|_p},\qquad a\ne1.
\]

This is not a Hilbert-space operator trace: a unitary on infinite-dimensional L²(Q_p) is not trace class. At a=1 the diagonal pullback is singular; the formula makes no claim there. It is a fixed-point contribution with the stated local regularisation. The script also verifies it by traces of finite-rank compressions onto locally constant compactly supported functions, using exact intersection volumes of p-adic balls.

One has τ(a^{-1})=τ(a). If v_p(a)≠0, the ultrametric inequality gives

\[
\tau(a)=p^{-|v_p(a)|/2}.
\]

#### A counterexample satisfying all group hypotheses (REFUTED)

At the smallest allowed prime p=3 put

\[
g_1=\operatorname{diag}(1,3),\qquad
g_2=\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]

The images of g₁, g₁^{-1}, g₂, g₂^{-1} on [Z_3²] are its four distinct neighbours: their rank-one image lines modulo 3 are (1,0),(0,1),(1,2),(1,1), printed by the script. A reduced word in these generators traces a non-backtracking path: the only possible reversal is multiplication by the inverse of the preceding generator, since the four neighbours are distinct. Thus no reduced nonempty word fixes the base vertex, and every vertex is reached. This proves that Γ=⟨g₁,g₂⟩ is free, discrete, torsion-free, simply transitive on vertices, and cocompact. It has no edge inversions (an inversion would have square fixing a vertex and hence have order two).

Let Γ⁺ be its index-two even-word subgroup. It is again discrete, torsion-free, cocompact, and without inversions. The element γ=g₁²=diag(1,9) is primitive in Γ⁺: its centraliser in the free group Γ is ⟨g₁⟩, whose intersection with Γ⁺ is ⟨g₁²⟩. Its length is two, and its symplectic lift is diag(1/3,3), implemented by D₃. Hence

\[
\underbrace{\tau(3)}_{\text{actual Clifford trace}}=3^{-1/2}
\ne 3^{-1}
=\underbrace{3^{-\ell(\gamma)/2}}_{\text{graph weight}}.
\]

The numerical values are 0.57735026918962573 and 1/3. D₉ has trace 1/3, but its action on the original lattice tree has length four, not two. Moreover this actual symplectic lift lies in SL₂(Q), so it also preserves the global lattice Q²⊂A²: the mismatch persists under the round's adelic steer.

Generally, if γ has a symplectic lift with λ=a², then

\[
\ell(\gamma)=2|v_p(a)|,
\quad\tau(a^m)=p^{-m\ell(\gamma)/4},
\quad p^{-m\ell(\gamma)/2}=\tau(a^m)^2.
\]

Thus a corrected identity using the actual Clifford is the **square** of its positive flat trace in axis coordinates, not its trace. When λ is nonsquare there is no such lift at all. Relabelling D_λ as “the squeeze part of γ” silently changes the symplectic action and cannot repair the asserted identification.

#### The exact boundary replacement (PROVED)

Let γ~diag(1,λ) with v_p(λ)=ℓ>0. In the chart on P¹(Q_p) whose line is Q_p(e₁+xe₂), its action is x↦λx. The origin is its attracting fixed line, a Lagrangian of the original V. Pullback of **half densities** in this coordinate is exactly

\[
\mathcal U_\gamma f(x)=|\lambda|_p^{1/2}f(\lambda x)=D_\lambda f(x).
\]

Consequently the local contribution at this attracting boundary end is

\[
\operatorname{Lef}_{\partial,+}(\gamma^m)=\tau(\lambda^m)=p^{-m\ell/2}.
\]

This number is independent of axis-coordinate rescaling and of conjugation of γ; reversing the chosen end replaces λ by λ^{-1} and leaves τ unchanged. It is explicitly **one fixed-point contribution**. A trace formula on the whole projective boundary must account separately for both fixed ends; it must not silently double this contribution. Nor is this an assertion about a global trace-class representation on the boundary.

The boundary half-density operator has the same functional formula as a one-mode Schrödinger dilation, but it is induced by the projective action on the Lagrangian Grassmannian, not by γ's linear symplectic action on V. Combining with T4(a) gives the exact identity, for k≥1,

\[
\boxed{\quad p^{-k/2}N_k
 =\sum_{\substack{[\gamma_0]\ \mathrm{primitive}\m\ell(\gamma_0)=k}}
  \ell(\gamma_0)\operatorname{Lef}_{\partial,+}(\gamma_0^m).\quad}
\]

This provides the requested lattice → symplectic boundary → zeta/trace connection, with the representation and multiplicities stated. It does not assert that Γ acts as Cliffords on the code spaces of all its vertices; a colour-exchanging element even changes their dimensions.

#### Time, measure, orientation and sign (PROVED for the nonzero-valuation terms)

The graph uses integer edge time k and unit edge volume. Set t=k log p and give an edge physical length log p. A prime cycle then has period T₀=ℓ₀ log p, and its positive-time orbit measure becomes

\[
\sum_{[\gamma_0]\text{ oriented primitive}}\sum_{m\ge1}
 T_0e^{-mT_0/2}\,\delta_{mT_0}.
\]

Equivalently multiply the graph's discrete orbit coefficients by log p and push the atom at k to k log p. This is the convention obtained by differentiating the Euler product in s after u=p^{-s}, rather than in log u.

On Q_p^× choose multiplicative Haar measure giving Z_p^× volume log p, and take test functions constant on unit cosets. On the shells with v_p(a)=k≠0 the integral of τ(a) contributes exactly

\[
\log p\,p^{-|k|/2}\,F(k\log p).
\]

Thus one oriented graph cycle has the same positive-time atom formula as a formal prime of norm p^{ℓ₀}. This is an equality of the **local weight formula**, not an equality between the two global zeta functions. Reverse graph cycles remain separate, as required by T4(a); a two-sided Connes/Weil test adds both k and −k explicitly. The unit shell, including a=1, requires the usual regularisation and is not supplied by the nonsingular calculation above. Neither is the archimedean term.

Finally τ is positive on both sides. The sign flip is external to the fixed-point computation: the graph has the positive ordinary trace term +p^{-k/2}N_k, whereas isolating the zero/H¹ contribution in the arithmetic explicit formula gives pole terms **minus** local prime terms. This is the determinant/supertrace convention (“bright” versus “dark”), not a sign of D_a or of its local Jacobian. No positivity theorem for global zeta follows.

Bibliographic reference from memory: A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Mathematica 5 (1999), the semi-local distributional trace formula and local fixed-point kernels. Only the explicitly derived nonunit-shell kernel and its Haar normalisation are asserted here; no unverified theorem numbering or complete regularisation is used.

### 4.3 T4(c): an explicit arithmetic quotient and independent exact counts

**PROVED construction; exact count certificates and NUMERICAL spectral comparison.** The arithmetic stretch is achieved with a small quaternionic congruence quotient: p=5, reduction modulo 3, and vertex group PGL₂(F₃). This avoids assuming the parameter restrictions of the most commonly presented X^{p,q} notation. The construction below proves the needed tree action directly.

#### Quaternionic lattice and congruence quotient (PROVED)

Let H=Q⟨i,j⟩/(i²=j²=−1,ij=−ji), k=ij, with the Lipschitz order O=Z[1,i,j,k]. At 5 choose ι∈Z_5 with ι²=−1, ι≡2 mod 5, and split H by

\[
i\mapsto\begin{pmatrix}\iota&0\\0&-\iota\end{pmatrix},\quad
j\mapsto\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
k\mapsto\begin{pmatrix}0&\iota\\\iota&0\end{pmatrix}.
\]

The six elements 1±2i,1±2j,1±2k have norm five, inverse pairs projectively, and integral matrices of determinant valuation one. Their image lattices are the six neighbours of Z_5²: the image lines modulo 5 are

\[
(0,1),(1,0),(1,3),(1,2),(1,4),(1,1).
\]

The same reduced-word argument used for the p=3 counterexample proves that Λ=⟨[1+2i],[1+2j],[1+2k]⟩ is a free group on three generators acting simply transitively on the vertices of T₅. It is discrete, cocompact and without inversions.

It is also an arithmetic tree lattice, not just a named Cayley graph: Λ is contained in O[1/5]^× modulo central scalars and has finite index there. To prove the latter, move the base vertex of any element of this order-unit group back by the unique element of Λ. The remainder lies in its base-vertex stabiliser. A stabilising element has even norm valuation; scale it to norm one. The displayed splitting identifies O⊗Z_5 with M₂(Z_5), so such a stabiliser has integral 5-adic coordinates. Its coordinates also lie in Z[1/5], hence are integers. The positive definite real norm is now a sum of four integer squares equal to one, leaving only finitely many elements. Thus the stabiliser is finite, proving finite index and arithmeticity. This argument uses the definite quaternion algebra and does not need an unproved invocation of LPS freeness.

Reduction modulo 3 is given explicitly by

\[
i\mapsto\begin{pmatrix}0&1\\2&0\end{pmatrix},\qquad
j\mapsto\begin{pmatrix}1&1\\1&2\end{pmatrix}.
\]

Their squares are −I and they anticommute, so this is a homomorphism of the quaternion order, and it is defined on 5-localised units. The six projective reductions of 1±2i,1±2j,1±2k are distinct, have determinant nonsquare modulo 3, and generate all 24 elements of PGL₂(F₃); the script prints the matrices and exhausts the group by multiplication.

Let Γ be the reduction kernel in Λ. Since Λ acts simply transitively on vertices, Γ\T₅ is exactly the Cayley graph of PGL₂(F₃) with these six generators. It is a connected simple 6-regular graph with 24 vertices and 72 edges. The determinant square class gives its bipartition. Γ has all the hypotheses of T4(a). This is the norm-five Hamilton quaternion construction underlying LPS, in a small congruence quotient whose properties were checked directly. Bibliographic background from memory: A. Lubotzky, R. Phillips and P. Sarnak, *Ramanujan graphs*, Combinatorica 8 (1988), quaternionic tree lattices and their congruence graphs; no quoted theorem is needed to certify this small example.

#### Determinant and spectrum (exact certificate)

The adjacency characteristic polynomial, computed over Z, is

\[
\det(tI-A)=t^4(t-6)(t+6)(t-2)^9(t+2)^9.
\]

The nontrivial spectrum is 0,±2, so this graph is Ramanujan by the direct inequality 2<2√5; no RH or Deligne theorem was assumed in computing it. Ihara–Bass gives

\[
\zeta_Y(u)^{-1}
=(1-u^2)^{49}(1-25u^2)(1+5u^2)^4
 (1-2u+5u^2)^9(1+2u+5u^2)^9.
\]

`ihara_lefschetz.py` builds the 144×144 Hashimoto matrix B and takes its integer powers. Independently it computes the adjacency characteristic polynomial, substitutes to form det(1−Au+5u²), and obtains N_k from coefficients of −u(d/du)log ζ_Y(u)^{-1}. Möbius inversion of this second route gives the prime-cycle counts. Both routes agree exactly:

| k | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| N_k | 0 | 0 | 0 | 1296 | 0 | 34560 | 0 | 767376 |
| P_k, oriented | 0 | 0 | 0 | 324 | 0 | 5760 | 0 | 95760 |

In particular the distinction between primitive multiplicity and total length is visible at length eight, which includes repetitions of the prime cycles of length four.

The T4(b) obstruction also occurs inside this very arithmetic example. Each generator has order four modulo 3. Thus γ=[(1+2i)^4] is primitive in the congruence kernel: the centraliser in the free group Λ is generated by [1+2i], and its intersection with the kernel is generated by its fourth power. Direct quaternion multiplication gives (1+2i)^4=−7−24i, of norm 625. Its SL₂ lift is (−7−24i)/25; its two 5-adic eigenvalues have valuations −2 and 2. The tree length is four, its actual Clifford flat trace in axis coordinates is 1/5, and its graph orbit weight is 1/25. The script prints all these quantities. This makes the distinction between the two trace representations visible on a primitive cycle of the graph used in the numerical check.

#### Explicit formula and the local weights (PROVED; NUMERICAL check)

For every finite connected (p+1)-regular graph, write E for its number of undirected edges and n for its number of vertices. Ihara–Bass yields, for k≥1,

\[
N_k=\operatorname{Tr}M^k+(E-n)(1+(-1)^k),
\qquad M=\begin{pmatrix}A&-pI\\I&0\end{pmatrix}.
\]

Here is the needed determinant identity directly. Let S,T be the origin and terminus incidence matrices from vertices to oriented edges, and R edge reversal. Then B=TSᵀ−R, R²=I, SᵀT=A, and SᵀRT=(p+1)I. The determinant lemma and (I+uR)^{-1}=(I−uR)/(1−u²) give

\[
\det(I-uB)
=\det(I+uR)\det\bigl(I-uS^T(I+uR)^{-1}T\bigr)
=(1-u^2)^{E-n}\det(I-uA+pu^2).
\]

This is a formal identity; logarithmic differentiation proves the displayed trace formula. Bibliographic attribution from memory: H. Bass, *The Ihara–Selberg zeta function of a tree lattice*, International Journal of Mathematics 3 (1992), the determinant formula. The short calculation fixes all signs and conventions used here.

Let b=1 for a bipartite graph and b=0 otherwise. Removing the uniform eigenvalue p+1 and, when b=1, the alternating eigenvalue −(p+1), and normalising M by √p gives

\[
C_Y(k)=p^{-k/2}N_k
 -(1+b(-1)^k)(p^{k/2}+p^{-k/2})
 -n(p-1)p^{-k/2}\mathbf1_{2\mid k}.
\]

The cycle term is, by T4(b), Σ_(d|k) dP_d τ(p^k). Replacing p^k by the actual eigenvalue ratio of each γ₀^(k/d) makes no difference to this trace, since its nonzero valuation is k. This verifies the local trace weights without requiring explicit p-adic roots for every cycle.

The script independently diagonalises A in complex128, solves w²−(λ/√p)w+1=0 on every nontrivial mode, and compares Σw^k with the formula above. The maximum absolute error through k=8 is 9.9475983006414026×10^{-14}. The largest cancellation is between orbit and trivial terms, so this is consistent with ordinary double precision, not a rigorous floating-point enclosure. Exact count identities provide the rigorous part of the check.

As a separate non-bipartite check of precisely the formula printed in `graph-ihara.md` §5, the script also runs K₅ with p=3. Its N₁,…,N₈ are (0,0,60,120,120,780,2520,6120), its prime counts are (0,0,20,30,24,120,360,750), and its maximum spectral-formula error is 4.44089209850062616×10^{-15}. No embedding of this K₅ deck group in PGL₂(Q₃) is asserted or needed. The arithmetic example above supplies that part of the task.

## 5. T5 — Casoratian, a constructive Poisson intertwiner, and the boundary Weil form

**SHARPENED / PROVED:** Ω is exactly the rescaled Casoratian. It has an explicit realisation on two copies of **automorphic boundary distributions**, with a finite-quotient pairing and a Poisson-normalised intertwiner. The resulting Weil form is written below. **REFUTED:** the two spherical Poisson functions supply the whole symplectic plane, or the graph modes are ordinary L² functions on the boundary. An identification with a single universal local intertwining-integral form, without the quotient pairing, is not proved and is not used.

### 5.1 Parameters and the exact Casoratian (PROVED)

Fix a real adjacency eigenvalue λ and let E_λ be its eigenspace on Y, using counting measure on vertices. Write

\[
\alpha+\beta=\lambda,\qquad \alpha\beta=p,
\qquad z=\alpha/\sqrt p,\quad z^{-1}=\beta/\sqrt p.
\]

Thus λ=√p(z+z^{-1}). The brief mixed z with α: the two unnormalised Satake parameters are α,p/α; the two normalised ones are z,z^{-1}, **not** z,p/z. For multiplicity r, the invariant label space is E_λ⊕E_λ of dimension 2r; a single normalised eigenvector selects a two-dimensional plane.

In the binding coordinates, a recurrence solution f_(n+2)=λf_(n+1)−pf_n has state v_n=(f_(n+1),f_n). For another solution g,

\[
W_n(f,g)=f_{n+1}g_n-f_ng_{n+1},\qquad W_{n+1}=pW_n.
\]

This follows by substituting the recurrence and cancelling the λ terms. Therefore p^{-n}W_n is independent of n and is precisely Ω(v₀,w₀). For E_λ-valued solutions sum the expression over vertices. For the characteristic solutions f_n=α^n, g_n=β^n,

\[
p^{-n}W_n=\alpha-\beta,
\quad
\Omega((\alpha,1),(\beta,1))=\alpha-\beta.
\]

This proves the Casoratian statement without an analogy or a boundary theorem.

The radial **vertex adjacency** equation on the tree is instead

\[
\lambda r_n=r_{n-1}+pr_{n+1}\quad(n\ge1).
\]

Putting f_n=p^n r_n gives the label recurrence above. At the root, regular radial functions must also obey λr₀=(p+1)r₁; this boundary condition removes one of the two initial degrees of freedom. Omitting either the rescaling or this condition gives an incorrect radial identification.

### 5.2 Poisson transform and its explicit inverse (PROVED)

Fix an origin o in T_p and write h_ξ(v) for the Busemann height towards ξ∈∂T_p=P¹(Q_p), normalised by h_ξ(o)=0. It increases by one on the unique neighbour towards ξ and decreases by one on the other p neighbours. For α∈C^× put

\[
K_\alpha(v,\xi)=\alpha^{h_\xi(v)},\qquad
\lambda=\alpha+p/\alpha.
\]

Then A K_α=λK_α by the neighbour count. If α=p^s, this is λ=p^s+p^{1−s}, and z=p^{s−1/2}; the brief's p^{1/2−s} is the inverse normalised parameter. No branch choice for s is needed if α is used directly.

Let D(∂T) be the space of complex finitely additive measures on clopen boundary sets, equivalently linear functionals on locally constant boundary functions. For each v, K_α(v,·) is locally constant, so

\[
(\mathcal P_\alpha\nu)(v)=\nu(K_\alpha(v,\cdot))
\]

is well defined by a finite sum. It is a λ-eigenfunction on T. There is no convergence assumption on ν.

**Inverse formula.** Suppose α≠±1 and F is any λ-eigenfunction on T. For an edge v→w directed away from o, with d(o,v)=n, let C_w be the boundary cylinder beyond w. Define

\[
\boxed{\quad
\nu_F^\alpha(\partial T)=F(o),\qquad
\nu_F^\alpha(C_w)=
 \alpha^{-n}\frac{F(w)-\alpha^{-1}F(v)}{\alpha-\alpha^{-1}}.
\quad}
\]

These cylinder values are compatible. At a nonroot vertex v, summing over its p children gives

\[
\sum_w\nu_F^\alpha(C_w)
=\frac{\alpha^{-n}}{\alpha-\alpha^{-1}}
 ((\lambda-p\alpha^{-1})F(v)-F(v^-))
=\nu_F^\alpha(C_v).
\]

At the root the sum over p+1 children is F(o), using λ−(p+1)/α=α−α^{-1}. Hence the formula defines a finitely additive measure.

To prove it inverts the Poisson transform, note that

\[
K_\alpha(w,\xi)-\alpha^{-1}K_\alpha(v,\xi)
=(\alpha-\alpha^{-1})\alpha^n1_{C_w}(\xi).
\]

The Poisson transform of the constructed measure has the correct value at o and the same difference across every oriented edge as F, so induction gives P_αν_F^α=F everywhere. The same edge identity recovers every cylinder mass from P_αν, proving injectivity. Thus **P_α is a bijection between boundary distributions and all λ-eigenfunctions on the tree** for α≠±1. This proves the version needed here directly, rather than citing a boundary representation theorem.

For nontrivial graph eigenvalues λ≠±(p+1), both roots α,β avoid ±1. Consequently

\[
\mathcal I_{\alpha\to\beta}
 =(\mathcal P_\beta)^{-1}\mathcal P_\alpha
\]

is an explicit invertible intertwiner, computed by the cylinder formula. The boundary action is the one transported through P_α from the tree action; equivalently it is the usual Busemann-weighted action, not bare pushforward of measures. With this convention I is equivariant. It is Poisson-normalised by P_β I=P_α and fixes the visual spherical measure, as proved in §5.5. This specifies precisely the intertwiner used here. Identifying a separately defined “standard intertwiner” with it requires that same normalisation and domain; no integral of products of singular distributions is being asserted.

Let D_(α,Γ) consist of distributions whose Poisson transforms are Γ-invariant. The explicit inverse identifies it with E_λ(Y). These are the automorphic boundary data. This construction also works for a free cocompact subgroup of Aut(T); in the PGL₂ setting its boundary is canonically the Lagrangian Grassmannian of V.

### 5.3 The quotient pairing and the pullback of Ω (PROVED)

For ν∈D_(α,Γ) and η∈D_(β,Γ), define the bilinear pairing

\[
B_\Gamma(\nu,\eta)=\sum_{v\in V(Y)}
 (\mathcal P_\alpha\nu)(\widetilde v)
 (\mathcal P_\beta\eta)(\widetilde v),
\]

where any lifts of vertices may be used. Γ-invariance makes this independent of the lifts. It is the finite quotient's counting/Petersson pairing, transported to the boundary. Equivalently it pairs ν with I_(β→α)η in the same-parameter Poisson realisation. It is **additional global quotient data**, not the local intertwiner alone.

For explicit evaluation let F be a set of vertex lifts and form the locally constant finite-rank kernel

\[
\mathcal K_\Gamma(\xi,\eta)=
 \sum_{v\in F}\alpha^{h_\xi(v)}\beta^{h_\eta(v)}.
\]

Then B_Γ(ν,η)=(ν⊗η)(K_Γ). A finite cylinder partition suffices, so this tensor-distribution pairing is well defined; it is not an undefined pointwise product of distributions. Changing the basepoint changes the coordinate descriptions of ν and the kernel compatibly.

Assume α≠β. Take (ν₊,ν₋)∈D_(α,Γ)⊕D_(β,Γ) and put F₊=P_αν₊, F₋=P_βν₋. The map to labels is

\[
(f,g)=(\alpha F_++\beta F_-,\ F_++F_-).
\]

It is invertible, and M acts on the two summands by α,β. Direct expansion gives the required symplectic identity:

\[
\boxed{\quad
\Omega_\partial((\nu_+,\nu_-),(\eta_+,\eta_-))
=(\alpha-\beta)
 \bigl(B_\Gamma(\nu_+,\eta_-)-B_\Gamma(\eta_+,\nu_-)\bigr).
\quad}
\]

On a single normalised adjacency eigenvector this is precisely the characteristic-solution Casoratian of §5.1, with constant α−β. On a repeated eigenspace the pairing sums over its multiplicity. This is a complete, explicit boundary version of the claim, with the quotient pairing specified.

### 5.4 The boundary Weil form and what its positivity says (PROVED)

In these binding coordinates the Weil form is

\[
\mathcal Q_\lambda=\tfrac12\Omega(M-pM^{-1})
 =\begin{pmatrix}1&-\lambda/2\\-\lambda/2&p\end{pmatrix},
\qquad
Q(f,g)=\|f\|^2-\lambda\langle f,g\rangle+p\|g\|^2
\]

for real labels. The older record's matrix ((p,λ/2),(λ/2,1)) belongs to its alternative coordinates. The symplectic change (f,g)↦(g,−f) carries that convention to this one; silently mixing the two changes the cross-term sign.

Since Q vanishes on either characteristic line, its boundary expression is

\[
\boxed{\quad Q_\partial(\nu_+,\nu_-)
 =-(\alpha-\beta)^2B_\Gamma(\nu_+,\nu_-).\quad}
\]

If |λ|<2√p, choose Im α>0 and β=conj(α). Real label vectors correspond exactly to ν₋=conj(ν₊). Hence

\[
\boxed{\quad Q_\partial(\nu,\bar\nu)
 =(4p-\lambda^2)\sum_{v\in Y}|\mathcal P_\alpha\nu(\widetilde v)|^2>0
 \quad(\nu\ne0).\quad}
\]

This is a positive Hermitian form on the automorphic distributions on P¹(Q_p), the Lagrangian Grassmannian, with an explicit finite boundary kernel. It is the graph's Weil positivity transported by an isomorphism. It supplies **no independent reason** for an arbitrary graph's eigenvalues to lie in the band.

For α=β=±√p the characteristic-coordinate map collapses. Keep two independent initial-data distributions under P_α instead. The boundary form is the pullback of

\[
Q(f,g)=\|f-\lambda g/2\|^2+(p-\lambda^2/4)\|g\|^2.
\]

At the endpoint this is nonnegative with a kernel, while Ω remains nondegenerate. The second recurrence solution is nα^n, and its rescaled Casoratian with α^n is −α. This is the Jordan/endpoint qualification, not positive definiteness.

For the uniform and, if present, alternating modes λ=±(p+1), one Poisson root is the exceptional value ±1. The two-parameter inverse/intertwiner statement in §5.2 deliberately excludes these modes. Their label planes still have a boundary realisation by using the admissible root α=±p for **both initial-data copies**. The displayed initial-data formula for Q remains valid, with determinant −(p−1)²/4, hence one negative direction. These are precisely the trivial planes removed from the non-uniform graph formula; no invertibility of P_(±1) is claimed.

Outside the band the same boundary realisation exists but Q is indefinite. An exact nontrivial example at odd p is Y=C₁₂□C₃, a 4-regular graph (p=3) with adjacency eigenvalue λ=2+√3 and a nonconstant cosine eigenvector e of norm one. Taking F₊=F₋=e gives

\[
Q=-(\lambda^2-12)=5-4\sqrt3<0.
\]

The script verifies the eigenvector, cylinder reconstruction, and the value −1.9282032302755088. Thus “a form on the boundary is positive for every graph because the boundary principal series has an inner product” cannot be a valid inference.

### 5.5 Two obstructions to the naive boundary reading (PROVED / REFUTED)

**Spherical collapse.** Let ν_o be the visual probability measure, giving each depth-n cylinder mass 1/((p+1)p^(n−1)). Then P_αν_o is radial, has value one at o, and satisfies the root condition and the radial adjacency recurrence. Those determine it uniquely from λ. Therefore

\[
\mathcal P_\alpha\nu_o=\mathcal P_\beta\nu_o.
\]

In particular I_(α→β)ν_o=ν_o, which proves the stated spherical normalisation. The two radial functions, even after multiplying their n-th values by p^n, have **zero** mutual Casoratian. They cannot produce the nondegenerate Ω of the two-dimensional label plane. By contrast the two horocyclic plane waves α^(h_ξ), β^(h_ξ), evaluated along a ray towards ξ, give the characteristic solutions α^n,β^n and Casoratian α−β. The latter calculation is valid; conflating it with two regular spherical radial solutions is not.

**Ordinary L² boundary data do not contain these graph modes.** Suppose |α|=√p and ν=fν_o with f∈L²(∂T,ν_o). At distance n from o,

\[
\|K_\alpha(v,\cdot)\|_2^2=\int p^{h_\xi(v)}d\nu_o(\xi)=1,
\]

and

\[
\|K_\alpha(v,\cdot)\|_1
=\left(1+\frac{p-1}{p+1}n\right)p^{-n/2}\longrightarrow0.
\]

The first identity is the constant spherical function for parameter p; the second is the repeated-root spherical recurrence at λ=2√p, with its root normalisation. Both can also be checked by summing cylinder masses. For bounded f, the second identity implies P_α(fν_o)(v)→0 uniformly as d(o,v)→∞. Approximate any L² f by bounded functions and use the first identity with Cauchy–Schwarz; the same conclusion holds for every L² f.

A nonzero Γ-periodic eigenfunction cannot tend to zero at infinity: any nonzero value repeats on an unbounded Γ-orbit. Thus D_(α,Γ) has **no nonzero L² density** when |α|=√p. The distributions above are essential. This explains why the positive Hilbert structure of a local boundary representation does not automatically prove Ramanujan for a finite quotient. It also identifies the missing domain issue in a proposed direct pairing by the usual boundary intertwining integral.

### 5.6 Checks and the precise remaining limitation

`checks/boundary_casoratian.py` verifies the matrices and characteristic-coordinate pairings symbolically. It constructs the universal covering tree through depth four for K₅ and C₁₂□C₃ (108 terminal cylinders, 161 tested vertices each), reconstructs the lifted eigenfunctions from both Poisson parameters, and checks cylinder additivity. The largest reconstruction error in these examples is 3.85802501057241898×10^{-15}. It separately checks the vanishing spherical Casoratian and the nonzero plane-wave Casoratian, the kernel L¹/L² formulas, and the endpoint rank-one form.

For the K₅ λ=−1 mode, choosing F₊ to have squared norm two gives Q=22 by both the direct label formula and the boundary kernel. For C₁₂□C₃ the negative value above is exact symbolically and agrees numerically. Errors are complex128 numerical checks, not a substitute for the constructive inversion proof.

**OPEN, and not claimed:** replacing the explicitly quotient-dependent B_Γ by a single intrinsic local intertwining-integral pairing on singular Γ-automorphic boundary distributions, together with a new geometric positivity mechanism. The Poisson-normalised intertwiner and the finite boundary kernel above are proved. Equating their quotient pairing with an unspecified “standard” local pairing would require defining that pairing's extension to these distributions and proving the equality. The current result is a constructive boundary realisation of the existing Weil form, not a proof of Ramanujan from local symplectic geometry.

Bibliographic background from memory: A. Figà-Talamanca and C. Nebbia, *Harmonic Analysis and Representation Theory for Groups Acting on Homogeneous Trees* (1991), boundary Poisson transforms and principal series. All identities actually used here were derived above.

## Correction ledger

| item | statement needing correction | proved replacement / witness |
|---|---|---|
| §0 Weyl section | ψ(−uv/2)W is a representation on every integral symplectic lattice | Use ψ(+uv/2)W for the stipulated translation/modulation order. The minus section has multiplier ψ(2/9) on the printed self-dual p=3 example. |
| T1 homothety | scalar homothety preserves the code up to D_c | A homothety class has a unique representative of determinant valuation zero or one. Other representatives have different code dimensions; scalar cI and symplectic diag(c^{-1},c) differ. |
| T2 vector notation | “1_L” is an indicator and the displayed vectors are automatically orthonormal | Use a normalised qunaught vector φ_L in the fixed-character stabiliser ray. It may be a quadratic phase times an indicator. |
| T3 length | valuation-m squeeze fixes no vertex, and translates by “2m steps” as an unsigned length | Signed translation is 2m; length is 2|m|. For m=0 the apartment is fixed pointwise. |
| T3 group | every projective hyperbolic translation is a Clifford squeeze | A lift to SL₂ exists precisely when its eigenvalue ratio is a square; even valuation alone is insufficient. The Clifford parameter is a square root of that ratio. |
| T3 ellipticity | “fixes an edge” need not specify inversion | Odd determinant valuation and equal slopes give a setwise fixed edge with its endpoints exchanged, not a fixed vertex. |
| T4(a) multiplicity | each length-k class contributes k rooted walks | A power γ₀^m contributes ℓ(γ₀), with oriented inverse classes kept separate. |
| T4(b) representation | γ~diag(1,λ) has original symplectic squeeze D_λ | D_λ is its boundary-coordinate half-density dilation. When γ lifts, the original Clifford is D_a with a²=λ, and its flat trace has half the decay exponent. |
| T4(b) volume | Γ_γ\backslash⟨γ⟩ has volume ℓ(γ₀) | The relevant quotient is C_Γ(γ)\backslash Axis(γ), or C_Γ(γ)\backslash G_γ with unit-torus volume one. |
| T4(b) trace | a unitary dilation has the displayed ordinary trace | It has the displayed local flat trace for a≠1. The identity/unit-shell regularisation is additional data; one boundary fixed point must not be counted twice. |
| T4(b) arithmetic normalisation | graph and prime coefficients agree without changing time or measure | Set t=k log p, multiply graph coefficients by log p, and give Z_p^× multiplicative volume log p. This matches nonzero-valuation atom kernels, with the global explicit-formula sign handled separately. |
| T5 parameters | λ=√p(μ+μ^{-1}) has step eigenvalues μ,p/μ | Use normalised z,z^{-1}, or unnormalised α,β with αβ=p. |
| T5 radial equation | the vertex radial recurrence is already f_(n+2)=λf_(n+1)−pf_n | Rescale radial values by p^n, and retain the root condition; the regular spherical subspace is only one-dimensional. |
| T5 boundary domain | two spherical functions / ordinary L² boundary functions yield the full label plane | Use two independent Poisson data sets. Graph modes in the band are automorphic distributions with no nonzero L² densities. The finite quotient pairing is explicitly required. |
| Record coordinate convention | the two printed Q matrices can be interchanged without a change of coordinates | The binding M=((A,−pI),(I,0)) has Q=((I,−A/2),(−A/2,pI)); the old convention is symplectically conjugate by (f,g)↦(g,−f). |

The first six priority items T1–T4(c) have proofs or explicit corrected refutations. T5 has proved Casoratian and constructive boundary theorems; the stronger intrinsic-local-pairing question remains OPEN, so its progress entry is PARTIAL. No unproved positivity transfer to ζ or to arbitrary regular graphs is proposed.

## Numerical checks for the blind lane

All scripts use `python3`, numpy and/or sympy; no network, PARI, or downloaded data is needed. The following are six concrete quantities to recompute. Counts and quaternion/lattice calculations are exact; floating-point comparisons are labelled and do not certify an error bound beyond the reported residuals.

| quantity | expected value | script |
|---|---:|---|
| Largest within-basis Gram error for p=7 MUBs | 3.33066907387546962×10^{-16} | `checks/mub.py` |
| Arithmetic quotient N₈ | 767376 | `checks/ihara_lefschetz.py` |
| Arithmetic quotient oriented P₈ | 95760 | `checks/ihara_lefschetz.py` |
| Actual Clifford flat trace for the arithmetic primitive cycle [(1+2i)^4] | 1/5 | `checks/ihara_lefschetz.py` |
| Boundary flat trace / graph weight for that same cycle | 1/25 | `checks/ihara_lefschetz.py` |
| Nontrivial Weil value for C₁₂□C₃ in §5.4 | 5−4√3 ≈ −1.9282032302755088 | `checks/boundary_casoratian.py` |

Commands from the repository root:

```sh
python3 notes/astra-2026-10-27/tree-codes/astra/checks/tree_codes.py
python3 notes/astra-2026-10-27/tree-codes/astra/checks/mub.py
python3 notes/astra-2026-10-27/tree-codes/astra/checks/ihara_lefschetz.py
python3 notes/astra-2026-10-27/tree-codes/astra/checks/boundary_casoratian.py
```

Their saved outputs are respectively `checks/output_tree_codes.txt`, `checks/output_mub.txt`, `checks/output_ihara_lefschetz.txt`, and `checks/output_boundary_casoratian.txt`. Every script completed successfully with its assertions enabled. Review priority: check the Weyl phase from operator multiplication; distinguish a tree translation's eigenvalue ratio from its Clifford parameter; verify the arithmetic generator's order and primitivity; then inspect the domain of the boundary pairing.

## What this changes in the notebook

These are **candidate rows only**, authored by `codex:gpt-6-astra`, with no registration or cross-family review yet. “PROVED” describes this lane's claimed proof status, not promotion through the record gate.

| proposed id | status | statement and proof location |
|---|---|---|
| `prop:local-weyl-symmetric-section` | PROVED | The stipulated W has symmetric section ψ(+uv/2)W and cocycle ψ(ω/2); §1.1. |
| `prop:tree-colours-code-dimension` | PROVED / SHARPENED | Unique determinant-normalised lattice representatives give qunaught/qudit colours; arbitrary homothety is not a code isomorphism; §1. |
| `prop:tree-neighbours-mub` | PROVED | Normalised neighbouring qunaught rays give the full finite Weyl–Heisenberg MUB set of each qudit code; §2. |
| `prop:geodesic-squeeze` | PROVED / SHARPENED | Boundary lines, split apartments, Newton slopes, translation length, and the square-class obstruction to a Clifford lift; §3. |
| `thm:ihara-zeta-projective-translations` | PROVED | Oriented primitive conjugacy classes give the Euler product, with primitive-length multiplicity and centraliser covolume; §4.1. |
| `prop:local-dilation-flat-trace` | PROVED | For a≠1 the local diagonal trace of D_a is |a|^{1/2}/|1−a|; §4.2. |
| `thm:ihara-zeta-squeeze-lefschetz` (literal brief target) | REFUTED | The original Clifford trace has the wrong decay exponent, including on a primitive arithmetic cycle; §§4.2–4.3. |
| `thm:ihara-zeta-boundary-lefschetz` | PROVED | Ihara orbit coefficients equal primitive centraliser volume times the attracting boundary half-density fixed-point contribution; §4.2. |
| `prop:quaternionic-pgl2f3-tree-quotient` | PROVED; exact computed spectrum | Explicit arithmetic quotient of T₅ with PGL₂(F₃) vertices, exact determinant/count certificates; §4.3. |
| `prop:poisson-cylinder-inverse` | PROVED | Explicit inverse from any tree eigenfunction to its boundary cylinder distribution, for α≠±1; §5.2. |
| `prop:label-casoratian-boundary-pairing` | PROVED / SHARPENED | The label Ω is the rescaled Casoratian and the stated two-parameter Poisson pullback of the finite quotient pairing; §§5.1–5.3. |
| `prop:boundary-poisson-weil-form` | PROVED | Explicit boundary kernel for Q, nonnegative iff in the band and definite iff strictly inside it, with endpoint and trivial-mode qualifications; §5.4. |
| `prop:graph-boundary-no-l2-density` | PROVED | Nonzero periodic tree eigenfunctions in the band cannot have ordinary L² visual-boundary densities; §5.5. |
| `conj:intrinsic-automorphic-boundary-pairing` | OPEN | Define and identify a local intertwining-integral pairing on the singular automorphic data that yields the graph form without inserting the quotient pairing; §5.6. |

Suggested one-line annotations, **not applied**:

- `graph-ihara.md` §2(b): “For odd p use the unique representatives of determinant valuation zero/one and the symmetric section ψ(+uv/2)W; neighbouring qunaught rays give MUBs, while a general projective tree translation is a similitude and need not lift to a local Clifford.”
- `graph-ihara.md` §5: “The orbit weight is the local half-density Lefschetz contribution on the boundary at one attracting Lagrangian; when a Clifford lift exists its parameter is the square root of the projective eigenvalue ratio, so its original one-mode flat trace must be squared to obtain this weight.”
- `adelic-gkp.md` §10: “For a≠1 the dilation formula is a local flat kernel trace, not a trace-class Hilbert trace; the unit shell needs regularisation, and graph boundary multipliers must be distinguished from symplectic squeeze parameters.”
- `graph-ihara.md` §§4, 6, 8: “Ω is the rescaled Casoratian; Q=½Ω(M−pM^{-1}); compare the old and binding matrices only after the symplectic coordinate change (f,g)↦(g,−f).”
- `data-ladder.md` §3: “The local lattice tree and its Lagrangian boundary give an exact route to Ihara through a discrete quotient and orbit traces, but the quotient pairing and automorphic distributions remain global data; local boundary Hilbert positivity does not supply Ramanujan.”

The next step is the promised cross-family REFUTE review, especially of the representation distinction in T4(b) and the quotient/domain qualifications in T5. The unresolved intrinsic boundary-pairing problem is separated from the proved construction. All changes and outputs are confined to this lane; no record page or claim database was edited.
