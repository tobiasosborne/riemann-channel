# Pizer graphs, modular curves, and their integral label lattice

> **Status (tidy 2026-10-28): UNREVIEWED.** The planned cross-family (claude:fable) REFUTE review of this proof was not run: the round was held on 2026-10-27. Nothing here is endorsed by a second reader. Not registered.

Author: `codex:gpt-6-astra`

Date: 2026-10-27. Blind prover lane; no other prover's work was read. All literature citations below are **from memory**, as required by the round brief. Nothing is registered or promoted here.

This proof was written incrementally, with exact numerical certificates saved after each completed item. The final sections record reproducible review targets and proposed notebook annotations.

## Conventions and scope

The characteristic prime is $p$; the isogeny prime and good reduction prime for $X_0(p)$ is ℓ; a coefficient/Tate prime will be denoted $r\ne\ell$. Brandt matrices count geometric cyclic kernels and act on column vectors of functions by $(Bf)_i=\sum_j B_{ij}f_j$. The action on the free module on vertices is the transpose. All isomorphisms of elliptic curves in these counts are geometric.

The record's binding label convention is $M=\left(\begin{smallmatrix}B&-\ell I\\ I&0\end{smallmatrix}\right)$, $\Omega=\left(\begin{smallmatrix}0&I\\-I&0\end{smallmatrix}\right)$. This differs from the convention still printed on some older record pages.

## 1. P1 — Brandt determinants and the corrected Ihara zeta

**REFUTED as an ordinary-multigraph assertion; SHARPENED and PROVED with reversal-fixed loops.** The smallest $p\equiv1\pmod {12}$ is already a counterexample: $p=13,\ell=2$ has $B=[3]$, which cannot be the adjacency of a one-vertex graph all of whose loops contribute two. In the required positive-genus sample, with vertices ordered as in `output_pizer_graph.txt`,
$$
 B_{37}(2)=\begin{pmatrix}0&2&1\\2&0&1\\1&1&1\end{pmatrix},\qquad
 P_{37,2}(u)=(1+2u+2u^2)(1+2u^2).
$$
The last vertex has one self-dual isogeny, hence one **half-loop**, meaning a dart fixed by reversal. A half-loop contributes one to the degree. The requested ordinary-loop convention cannot represent this matrix. Both counterexamples, including the actual duality, are printed by the scripts below.

### 1.1 The exact arithmetic identity

**PROVED (using the named classical theorems).** Let $p>3$, $\ell\ne p$, $S_p=\{E_i\}$, and $w_i=|\operatorname{Aut}(E_i)|/2$. Set $W=\operatorname{diag}(w_i)$. Counting actual isogenies and applying duality gives
$$
 w_jB_{ij}=w_iB_{ji},\qquad W^{-1}B=B^tW^{-1}.
$$
Indeed, there are $2w_jB_{ij}$ morphisms of degree ℓ from $E_i$ to $E_j$, and duality bijects them with the opposite morphisms. Consequently
$$
 S=W^{-1/2}BW^{1/2}=S^t,
 \quad B\mathbf1=(\ell+1)\mathbf1,
 \quad B^tW^{-1}\mathbf1=(\ell+1)W^{-1}\mathbf1.
$$
For the divisor action $B^t$, the integral pairing is $\langle e_i,e_j\rangle=w_i\delta_{ij}$; its Eisenstein vector is proportional to $\sum_i e_i/w_i$. For the function action $B$, the Eisenstein vector is $\mathbf1$, and the pairing uses $1/w_i$. This settles the transpose ambiguity in the brief.

The Deuring–Eichler correspondence identifies the complex Hecke module on this class set with the weight-two level-$p$ module, with one Eisenstein line and the entire cusp space $S_2(\Gamma_0(p))$. It does **not** assert an integral isomorphism of these lattices. There are no old cusp forms from level one. Write $a_{\ell,1},\ldots,a_{\ell,g}$ for the eigenvalues with every coefficient-field embedding counted. The dimension statement gives
$$
 |S_p|=g+1,\qquad
 \det(I-uB+\ell u^2I)
 =(1-(\ell+1)u+\ell u^2)\prod_{j=1}^g(1-a_{\ell,j}u+\ell u^2).
$$
Eichler–Shimura at the good prime ℓ identifies the last product with the actual curve numerator:
$$
 \boxed{\det(I-uB+\ell u^2I)=(1-u)(1-\ell u)P_{p,\ell}(u)},\qquad
 Z(X_0(p)/\mathbb F_\ell,u)=\frac{P_{p,\ell}(u)}{(1-u)(1-\ell u)}.
$$
This identity holds for **all** $p>3$, including nontrivial weights. In characteristics $p=2,3$ the usual automorphism weights replace the abbreviated set $\{1,2,3\}$; the class-set/Hecke statement and $g=|S_p|-1=0$ still hold. The quoted supersingular counting formula with residues modulo twelve is a formula for primes $p>3$.

The usual genus formula gives a separate normalization check, for $p>3$:
$$
 g(X_0(p))=\frac{p+1}{12}
 -\frac{1+\left(\frac{-1}{p}\right)}4
 -\frac{1+\left(\frac{-3}{p}\right)}3.
$$
Checking the four residue classes modulo twelve gives precisely the stated supersingular count minus one. The script checks this formula and the mass identity $\sum_i1/w_i=(p-1)/12$ in every cell.

References **from memory**: Deuring, *Die Typen der Multiplikatorenringe elliptischer Funktionenkörper* (1941), the correspondence between supersingular elliptic curves and maximal-order ideal classes; Eichler, *Quaternäre quadratische Formen und die Riemannsche Vermutung für die Kongruenzzetafunktion* (1954), the Brandt/weight-two Hecke correspondence; Pizer, *An algorithm for computing modular forms on $\Gamma_0(N)$* (1980), the computational Brandt-module realization; Gross, *Heights and the special values of L-series* (1987), the weighted supersingular module. The Eichler–Shimura congruence relation at good reduction is used in its usual form $T_\ell=F+V$, $FV=\ell$, on the Jacobian/cohomology, with the two-dimensional factor for each newform embedding.

### 1.2 Loops, half-loops, and a determinant proof

**PROVED.** Suppose all $w_i=1$. Isogenies modulo target isomorphism are darts, and duality is a well-defined involution $J:e\mapsto\bar e$, possibly with fixed points. Let $n=|S_p|$, let $h$ be the number of fixed darts, and let $m$ be the number of two-element reversal orbits. Thus
$$
 2m+h=n(\ell+1).
$$
Define
$$
 H_{ef}=\mathbf1_{t(e)=o(f)}-\mathbf1_{f=\bar e}.
$$
A half-loop cannot immediately follow itself; a pair of ordinary loop orientations behaves exactly as in ordinary Ihara theory. With tail and head incidence matrices $O,T$ of size $n\times(2m+h)$, one has $H=T^tO-J$, $OT^t=B$, $OJ T^t=D=(\ell+1)I$. The matrix determinant lemma and $J^2=I$ give
$$
\begin{aligned}
\det(I-uH)
 &=\det(I+uJ)\det\left(I-uO(I+uJ)^{-1}T^t\right)\\
 &=(1-u^2)^{m-n}(1+u)^h\det(I-uB+\ell u^2I).
\end{aligned}
$$
This is a rational identity and hence a polynomial identity after cancellation, including cases $m<n$. Therefore the zeta defined by this non-backtracking operator is
$$
 \boxed{\zeta_{\rm dart}(u)=
 \frac{(1-u^2)^{n-m}(1+u)^{-h}}
 {(1-u)(1-\ell u)P_{p,\ell}(u)}}.
$$
When $h=0$, this is precisely ordinary Ihara–Bass with $m=|E|$, and an ordinary loop contributes two. If instead one counts every half-loop as one unoriented edge, so $|E|=m+h$, the correction relative to the brief's formula is a factor $(1-u)^h$ in the zeta. A half-loop by itself is excluded as a cyclically non-backtracking length-one walk, since it is its own reverse; this convention is defined by ζ = $\det(I-uH)^{-1}$, avoiding an ambiguous prime-cycle convention.

For $(37,2)$, $m=4,h=1,n=3$, so
$$
 \det(I-uH)=(1-u^2)(1+u)(1-u)(1-2u)P_{37,2}(u).
$$
Even diagonal entries do not determine the actual reversal: at $(13,5)$, $B=[6]$ but there are two half-loops and two paired loops. The adjacency alone does not fix the non-backtracking determinant unless the reversal convention is supplied.

For general weights the appropriate global object is an **edge-indexed quotient / graph of groups**: $B_{ij}$ counts lifted neighbours, not just orbits of edges. The matrix $S$ has the same determinant and spectrum as $B$, but need not be an integral adjacency. No ordinary unweighted Ihara interpretation is claimed for it. The determinant identity above remains exact; a graph-of-groups zeta requires its stabilizer and edge conventions to be specified separately.

### 1.3 Ramanujan and the numerical certificate

**PROVED.** Weil's theorem for the abelian variety $J_0(p)/\mathbb F_\ell$ puts every Frobenius eigenvalue α at complex absolute value $\sqrt\ell$. Since $a_{\ell,j}=\alpha+\ell/\alpha$, each $a_{\ell,j}$ is real and lies in $[-2\sqrt\ell,2\sqrt\ell]$. Thus the Brandt graph/operator is Ramanujan after removing its Eisenstein line. This uses the weight-two geometric theorem, not Deligne's general-weight theorem. Strict positivity, as opposed to nonnegativity, additionally excludes endpoints; every tested example has an exact certificate of strictness.

**NUMERICAL, exact arithmetic.** `checks/pizer_graph.py` constructs supersingular $j$'s from the Legendre Hasse polynomial, checks them with `ellissupersingular`, factors $\Phi_\ell(X,j_i)$ over $\mathbb F_{p^2}$, and retains all multiplicities. For $p=37,73,109$, ℓ $=2,3,5,7$, plus $p=101,11,13$, it prints every matrix, every exact cusp characteristic polynomial and newform coefficient, the curve numerator, and the predicted first point count. Independent `mfheckemat` and `mfeigenbasis`/`mfcoefs` calculations agree over $\mathbb Z$; coefficients in a proper subfield are counted with their full coefficient-field multiplicity. The decimal eigenvalues are only a display: exact positive leading minors of the weighted restriction of $4\ell I-B^2$ certify all bounds.

`checks/pizer_quotient.py` independently enumerates all cyclic ℓ-kernels using torsion points and Vélu isogenies, computes the dual kernel as $\phi(E[\ell])$, transports it by an actual isomorphism back to the standard source model for each loop, and thereby determines the reversal-fixed darts. For all the unweighted cases it recomputes the Brandt matrix and verifies the corrected Bass identity by exact characteristic polynomials of the dart operator. The main P1 script calls this independent duality routine as well, so **all printed Bass checks use the actual isogeny reversal**, not a pairing guessed from diagonal parity.

The brief's model
$$
 y^2=-x^6-9x^4-11x^2+37
$$
is consistent with $X_0(37)$: at ℓ $=3,5,7$, `hyperellcharpoly` agrees exactly with the modular/Brandt numerator, and separate direct counts over $\mathbb F_\ell$ and $\mathbb F_{\ell^2}$ agree. Its written characteristic-two reduction is singular, so that equation is not a valid characteristic-two check. These matching local polynomials verify the requested sanity check; they alone are not a proof that an arbitrary rational curve model is modular.

## 2. P2 — the global tree quotient

### 2.1 The local lattice and its symplectic form

**PROVED.** Over an algebraic closure of characteristic $p\ne\ell$, choose a compatible system of roots of unity to identify $\mathbb Z_\ell(1)$ with $\mathbb Z_\ell$. The inverse limit of the Weil pairings gives a perfect alternating pairing
$$
 T_\ell(E)\times T_\ell(E)\longrightarrow\mathbb Z_\ell(1).
$$
Thus $T_\ell(E)$ is a self-dual rank-two lattice in $V_\ell(E)$. For an ℓ-isogeny $\phi:E\to E'$, the map on Tate modules is injective with cokernel of order ℓ and
$$
 \langle\phi x,\phi y\rangle_{E'}=\ell\langle x,y\rangle_E.
$$
Under the rational identification induced by $\phi$,
$$
 T_\ell(E)\subset \phi^{-1}T_\ell(E'),\qquad
 [\phi^{-1}T_\ell(E'):T_\ell(E)]=\ell.
$$
The superlattices between $T$ and $\ell^{-1}T$ with this index are the lines in $\ell^{-1}T/T\simeq E[\ell]$; hence they are exactly the ℓ + 1 cyclic kernels. Their homothety classes are the neighbours of $[T]$ in the Bruhat–Tits tree.

**Necessary precision.** The superlattice is not self-dual for the *fixed* source pairing. Its self-duality uses the target pairing, which pulls back to ℓ times the source pairing. Consequently a one-edge move belongs to the symplectic **similitude** geometry. With a single fixed pairing on $\mathbb Q_\ell^2$, the self-dual representatives occupy one colour, not every vertex. This is exactly the parity distinction already present in `graph-ihara.md` §2$b$.

### 2.2 One maximal order suffices, at every class number

**PROVED (strong approximation and Deuring).** Put $D=B_{p,\infty}$, choose a maximal order $O$, and fix $D\otimes\mathbb Q_\ell\simeq M_2(\mathbb Q_\ell)$. Let
$$
 \Gamma=O[1/\ell]^\times/\mathbb Z[1/\ell]^\times,
 \qquad K^\ell=\prod_{v\ne\ell,\infty}O_v^\times.
$$
There is a Hecke-compatible bijection
$$
 \boxed{\Gamma\backslash\operatorname{Vert}(\mathcal T_\ell)
 \simeq D^\times(\mathbb Q)\backslash D^\times(\mathbb A_f)/\widehat O^\times
 \simeq S_p.}
$$
The edges are the corresponding local index-ℓ neighbours. With stabilizers retained, this is an isomorphism of edge-indexed quotient graphs, with possible inversions. It is **one quotient for arbitrary class number**, not a disjoint union over ideal classes. Different choices of the base order give the same class-set description with a different base vertex.

Here is the strong-approximation argument, including its norm obstruction. For a finite adele $b$, choose a positive rational number $a$ whose valuations outside ℓ equal those of $\operatorname{nrd}(b)$. The reduced norm of $D^\times(\mathbb Q)$ is $\mathbb Q_{>0}^\times$, so choose $c$ with norm $a$. Local norms of maximal-order units are all local units, also at the ramified prime $p$. Right multiplication by an element of $K^\ell$ therefore makes $c^{-1}b$ have norm one outside ℓ. The norm-one group $D^1$ is simply connected and split/noncompact at ℓ. Strong approximation away from $\{\ell,\infty\}$ supplies a rational norm-one element in the required open coset outside ℓ. Thus
$$
 D^\times(\mathbb A_f)=D^\times(\mathbb Q)D_\ell^\times K^\ell.
$$
At ℓ, vertices are $D_\ell^\times/(\mathbb Q_\ell^\times O_\ell^\times)$. A local central homothety is a power of ℓ times an integral unit; the power is rational and the unit is absorbed in $O_\ell^\times$. Two such local vertices represent the same adelic class precisely when the rational identification is a unit at all finite places outside ℓ, namely an element of $O[1/\ell]^\times$. This proves injectivity as well as surjectivity and proves the neighbour compatibility.

The action is discrete and cocompact: discreteness is the usual definite quaternion $S$-arithmetic embedding in $\operatorname{PGL}_2(\mathbb Q_\ell)$, and the preceding finite class-set quotient gives cocompactness. Vertex stabilizers are conjugates of $O_i^\times/\{\pm1\}$, of size $w_i$. When all $w_i=1$, there are no vertex stabilizers, but an element of projective order two can still invert an edge. Its quotient is a half-loop. Barycentric subdivision removes inversions at the price of midpoint stabilizers. Thus the tree-to-graph map need not be an ordinary graph covering under the brief's two-dart-loop convention.

References **from memory**: Serre, *Trees* (1980 English edition), the Bruhat–Tits lattice model and quaternion arithmetic quotients; Vignéras, *Arithmétique des algèbres de quaternions* (1980), strong approximation for the norm-one group and the reduced-norm theorem; Deuring/Pizer as in §1. These standard arithmetic inputs are used as theorems, not asserted to have been re-proved computationally.

### 2.3 Norm parity and the two-colour quotient

**PROVED.** Type changes by $v_\ell(\operatorname{nrd}\gamma)\bmod2$. The norm map on $O[1/\ell]^\times$ attains odd valuation. To see this without assuming connectedness of the isogeny graph, start with a rational quaternion of norm ℓ and apply the same strong-approximation correction outside ℓ; its corrected norm remains ℓ and it is a unit outside ℓ. Consequently
$$
 \Gamma^+=\ker\bigl(\Gamma\longrightarrow\mathbb Z/2\bigr)
 =O[1/\ell]^1/\{\pm1\},\qquad [\Gamma:\Gamma^+]=2.
$$
An element of even norm valuation can be rescaled by a rational power of ℓ to have norm one, which proves the displayed equality. The quotient by $\Gamma^+$ has two copies of the class set, one per colour, with vertex operator
$$
 \begin{pmatrix}0&B(\ell)\\B(\ell)&0\end{pmatrix}
$$
(in the same row convention, with indices for general weights). It is the bipartite double cover of the dart quotient. Passing from $\Gamma^+$ to $\Gamma$ identifies the two colours. Neither the class-number-one hypothesis nor a disjoint union of orders is needed.

**PROVED corollary: an ordinary-graph repair.** When all $w_i=1$, the norm-one quotient has neither vertex stabilizers nor edge inversions, so its bipartite double is an ordinary multigraph (all its edges join opposite colours). Its ordinary Ihara identity is
$$
 \zeta_{\Gamma^+\backslash\mathcal T_\ell}(u)
 =
 \frac{(1-u^2)^{-n(\ell-1)}}
 {(1-u^2)(1-\ell^2u^2)P_{p,\ell}(u)P_{p,\ell}(-u)}.
$$
Here $P_{p,\ell}(u)P_{p,\ell}(-u)=P_{p,\ell^2}(u^2)$, since $(1-\alpha u)(1+\alpha u)=1-\alpha^2u^2$. This supplies a literal ordinary-graph/curve-numerator identity over the quadratic field extension, with length variable $u^2$. It is proved by diagonalizing the two-colour swap and applying ordinary Bass. The script also prints exact dart-matrix Bass checks for this double at $p=37$ and all four isogeny primes.

### 2.4 Exact quaternion certificate at $p=37$

**NUMERICAL, exact and independent of modular polynomials.** In $D=(-2,-37)$, write $i^2=-2$, $j^2=-37$, $ij=-ji$. PARI constructs the maximal order with basis
$$
 1,\quad i,\quad(1+i+j)/2,\quad(2+i-ij)/4.
$$
The rational norm Gram matrix and reduced-trace discriminant are printed in `checks/output_quaternion.txt`; the latter is $-37^2=-1369$. The finite Hasse invariants are zero at 2 and one-half at 37; infinity also has invariant one-half. The order has only the units $\pm1$.

The script enumerates all two-dimensional right-stable subspaces of $O/2O$, takes their preimages, and tests ideal equivalence by left transporters and **exact norm-one-ratio elements**, not by isometry of norm forms. This matters: conjugacy classes of maximal orders (the type set) are not the same as ideal classes (the supersingular set). It finds three inequivalent right ideals, of norms $1,2,2$, and the direct 2-neighbour matrix
$$
 \begin{pmatrix}1&1&1\\1&0&2\\1&2&0\end{pmatrix}.
$$
There are exactly three classes by the class-number theorem, so the representatives are complete. For representatives $I_i$ with reduced ideal norms $n_i$, the formula used for all four primes is
$$
 B(\ell)_{ij}=
 \frac{\#\{\alpha:\alpha I_j\subset I_i,\ \operatorname{nrd}(\alpha)=\ell n_i/n_j\}}
 {|O_L(I_j)^\times|}.
$$
Indeed, $\alpha I_j\subset I_i$ then has index $\ell^2$, and two such multipliers give the same subideal exactly when they differ by a left-order unit of $I_j$. The denominator here is two. Norm enumeration uses a verified unimodular basis change followed by an integer box search with the exact bounds $|v_i|^2\le R(G^{-1})_{ii}$; no floating norm-search completeness is assumed. The resulting matrices at ℓ $=2,3,5,7$ agree with the modular-polynomial matrices under the one permutation $(2,0,1)$. Independently, trace-zero norm-ℓ elements modulo sign give the half-loop vectors $(1,0,0),(0,0,0),(0,1,1),(0,0,0)$, matching the Vélu duality calculation.

## 3. P3 — one-operator cohomology and the integral obstruction

### 3.1 Rational comparison: the precise statement

**SHARPENED; PROVED using the stated geometric theorems and the additional weight-two regularity input below.** The expression $(H^1,\mathbb Q[M])$ in the brief needs a coefficient-field qualification. If $r\ne\ell$, there is a noncanonical isomorphism
$$
 \boxed{(L_0\otimes\mathbb Q_r,M)\simeq
 (H^1_{\mathrm{et}}(X_0(p)_{\overline{\mathbb F}_\ell},\mathbb Q_r),F)}
$$
as **one-operator** $\mathbb Q_r[T]$-modules, where $F$ denotes geometric Frobenius on cohomology (equivalently the pullback of the Frobenius endomorphism). The graph provides a rational model of this system. It does not identify a $\mathbb Q$-vector space literally with a $\mathbb Q_r$-vector space, give a canonical map, identify polarizations, or give the entire Galois representation. On a Tate module one uses the Frobenius endomorphism/arithmetical Galois action instead; the standard dual conventions give the same Weil characteristic polynomial after the appropriate twist.

For $p\equiv1\pmod {12}$, set $n=|S_p|=g+1$, $U=\mathbb Q\mathbf1$, and $C=\mathbf1^\perp\subset\mathbb Q^n$. On $C\oplus C$, the characteristic polynomial is
$$
 \det(tI-M)=\prod_{j=1}^g(t^2-a_{\ell,j}t+\ell)
 =t^{2g}P_{p,\ell}(1/t).
$$
This follows directly by taking the Schur complement of $tI-M$ and applying §1. Since $B$ is symmetric, it is semisimple. Its companion doubling is semisimple exactly when no cusp eigenvalue satisfies $a_{\ell,j}^2=4\ell$: on an endpoint it has a nonzero two-by-two Jordan block. Frobenius on the cohomology of an abelian variety is semisimple (Weil/Rosati). Thus equality of characteristic polynomials alone is insufficient; the endpoint condition must be addressed.

**Additional standard input, from memory:** Coleman–Edixhoven, *On the semi-simplicity of the $U_p$-operator on modular forms*, Math. Ann. **310** (1998), weight-two regularity at primes not dividing the level: the two roots of $t^2-a_\ell(f)t+\ell\varepsilon(\ell)$ are distinct for a weight-two cuspidal newform. Here the nebentypus is trivial. This excludes the endpoints in the present modular family. With that input, both operators above are semisimple and have the same characteristic polynomial, which proves similarity over $\mathbb Q_r$: decompose into irreducible factors, whose multiplicities determine a semisimple module over a characteristic-zero polynomial ring. Repeated *distinct-root* factors from different forms cause no problem; at $p=37,\ell=7$ the repeated quadratic is explicitly checked.

If this additional recalled theorem is not imported, the same conclusion is **PROVED-conditional on H-strict:** no cusp eigenvalue is $\pm2\sqrt\ell$. The unconditional conclusions from Deuring–Eichler, Eichler–Shimura, and Weil alone are the characteristic-polynomial identity and nonnegative Weil form. The scripts certify H-strict exactly in every requested cell; the general weight-two regularity reference should be checked bibliographically during review.

For the binding convention, if $B$ is symmetric then
$$
 V=\ell M^{-1}=\begin{pmatrix}0&\ell I\\-I&B\end{pmatrix},\qquad
 Q=\tfrac12\Omega(M-V)=\begin{pmatrix}I&-B/2\\-B/2&\ell I\end{pmatrix}.
$$
The Schur complement is $\ell I-B^2/4$. Thus $Q\ge0$ on the cusp labels iff the Weil bounds hold, and $Q>0$ iff they are strict. In this family Weil supplies the bounds and the regularity input supplies strictness. The sign and order of the blocks differ from the older $\left(\begin{smallmatrix}0&-I\\\ell I&B\end{smallmatrix}\right)$ convention; no form is silently transported between them.

### 3.2 P3$a$: the saturated nontrivial lattice and its Smith forms

**PROVED and NUMERICAL.** Use the precise integral lattice requested in the brief:
$$
 A_{n-1}=\{x\in\mathbb Z^n:\textstyle\sum x_i=0\},\qquad
 L_0=A_{n-1}\oplus A_{n-1}.
$$
It is both the saturated intersection of the rational cusp space with the full label lattice and the $\Omega$-orthogonal complement of $\mathbb Z\mathbf1\oplus\mathbb Z\mathbf1$. It is stable under $M,V$. In the basis $k_i=e_i-e_n$, let $K=(k_1,\ldots,k_g)$, $C_0=K^tK=I_g+\mathbf1_g\mathbf1_g^t$, and $BK=KA$. Then
$$
 M_0=\begin{pmatrix}A&-\ell I_g\\I_g&0\end{pmatrix},\quad
 \Omega_0=\begin{pmatrix}0&C_0\\-C_0&0\end{pmatrix},\quad
 \det C_0=n,\quad\det\Omega_0=n^2.
$$
The Gram Smith factors are $1,\ldots,1,n$; thus the alternating elementary divisors are $1,\ldots,1,n$. The integral trivial-plus-cusp sum has index $n^2$ in $\mathbb Z^{2n}$. Rational projection onto the trivial line divides the coordinate sum by $n$, so the indicated rational decomposition does not give an integral orthogonal splitting when $n>1$. There is no alternative $M$-equivariant integral complement to this trivial lattice either: the cusp eigenvalues have absolute value $\sqrt\ell$, so none is $1$ or $\ell$; the rational invariant complement is therefore unique, and its integral vectors all lie in $L_0$.

For every $k\ge1$,
$$
 |L_0/(1-M_0^k)L_0|=\det(1-M_0^k)
 =\prod_i(1-\alpha_i^k)=\#J_0(p)(\mathbb F_{\ell^k}).
$$
The eigenvalues have absolute value $\sqrt\ell>1$, so the cokernels are finite; conjugate factors make the determinant positive. This is an equality of orders, not an isomorphism of groups. `checks/label_lattice.py` prints Smith factors for all $p=37,73,109$, ℓ $=2,3,5,7$, $k=1,2,3$, and separately verifies the order by the resultant $\operatorname{Res}_t(\det(t-M_0),1-t^k)$.

### 3.3 An integral symplectic reduction, distinct from the saturated complement

**PROVED (additional constructive result).** There is also a natural unimodular way to remove the trivial pair. In the binding convention the primitive eigenvalue-one vector is
$$
 e=(\mathbf1,\mathbf1),\quad Me=e,\qquad
 L_{\rm red}=e^\perp/\mathbb Ze.
$$
The edge-label map compatible with this $M$ is $(f,g)\mapsto\tau f-\sigma g$, whose kernel contains $(\mathbf1,\mathbf1)$. The tutorial's $(1,-1)$ refers to a different sign/order convention and cannot be inserted into this $M$ unchanged.

Because $e$ is primitive isotropic in a unimodular symplectic lattice, $L_{\rm red}$ is free, symplectic, and unimodular of rank $2g$. Both $M$ and $V$ preserve $e^\perp$ and its line. A concrete standard symplectic basis is
$$
 v_i=(e_i,e_n),\qquad w_i=(0,e_i-e_n),\qquad 1\le i<n,
$$
viewed modulo $\mathbb Ze$. Their pairings are $\Omega(v_i,w_j)=\delta_{ij}$, and the other pairs vanish. The inclusion of $L_0$ induces an injective equivariant map
$$
 L_0\hookrightarrow L_{\rm red},\qquad [L_{\rm red}:L_0]=n.
$$
Indeed, for $\sum f_i=\sum g_i=s$, rational projection subtracts $(s/n)e$; its possible cosets over $L_0$ form $\mathbb Z/n$. Thus this is a specific $M,V$-stable self-dual overlattice of the saturated complement, with the same rational Frobenius system. The script constructs its integral matrix and embedding and verifies their intertwining and pairing identities.

The two integral choices can give different finite groups despite identical counts. At $p=37,\ell=7,k=1$,
$$
 L_0/(1-M_0)L_0\simeq(\mathbb Z/9)^2,
 \qquad L_{\rm red}/(1-M_{\rm red})L_{\rm red}
 \simeq(\mathbb Z/3)^2\oplus\mathbb Z/9.
$$
This is a concrete demonstration that “remove the trivial mode” must specify an integral operation. Unimodularity alone is not an arithmetic polarization theorem or an identification with the Jacobian.

### 3.4 P3$b$: comparison with the elliptic product, and with the actual Jacobian

**REFUTED:** the saturated label lattice is not uniformly the product lattice; moreover it is not uniformly the actual Jacobian lattice, even as an unpolarized Frobenius module. **NUMERICAL and PROVED** certificates follow. Write $[d_1,\ldots,d_s]$ for $\bigoplus_i\mathbb Z/d_i$, omitting unit factors. The two brief equations are correct:
$$
 E_a:y^2+y=x^3-x,\qquad E_b:y^2+y=x^3+x^2-23x-50.
$$
PARI verifies conductor 37 for both, discriminants $37$ and $50653=37^3$, and their coefficients at $2,3,5,7$ are respectively $(-2,-3,-2,-1)$ and $(0,1,0,-1)$. The installed `elldata` is absent, so the literal Cremona database labels cannot be queried here; the stated equations, conductors, and modular coefficients are verified directly.

| ℓ | $k$ | saturated labels $L_0$ | symplectic reduction $L_{\rm red}$ | $E_a(\mathbb F_{\ell^k})\times E_b(\mathbb F_{\ell^k})$ |
|---:|---:|---|---|---|
| 2 | 1 | [15] | [15] | [15] |
| 2 | 2 | [3,15] | [3,15] | [3,15] |
| 2 | 3 | [45] | [45] | [45] |
| 3 | 1 | [21] | [21] | [21] |
| 3 | 2 | [105] | [105] | [105] |
| 3 | 3 | [2,2,2,126] | [2,2,2,126] | [2,2,2,126] |
| 5 | 1 | [48] | [48] | [2,24] |
| 5 | 2 | [12,96] | [12,96] | [2,2,6,48] |
| 5 | 3 | [13104] | [13104] | [2,6552] |
| 7 | 1 | [9,9] | [3,3,9] | [3,3,9] |
| 7 | 2 | [63,63] | [3,21,63] | [3,21,63] |
| 7 | 3 | [6,6,54,54] | [6,18,18,54] | [6,18,18,54] |

All entries and orders are printed in `checks/output_label_lattice.txt`. The first product disagreement in the tested increasing-prime order is ℓ $=5,k=1$: order 48 on both sides, but cyclic labels versus noncyclic product. Disagreement proves that the relevant integral Frobenius modules cannot be isomorphic; a finite list of agreements does not prove an integral module isomorphism. The product is only an isogeny representative of the modular Jacobian, so disagreement with it alone does not refute identification with the Jacobian.

**A proof separating the saturated labels from $J_0(37)$ itself.** For the displayed even sextic model of $X_0(37)$, the two elliptic quotient maps have coordinates
$$
 (x,y)\mapsto(-x^2,y),\qquad
 (x,y)\mapsto(37/x^2,37y/x^3).
$$
Their target equations are respectively
$$
 Y^2=X^3-9X^2+11X+37,\qquad
 Y^2=X^3-11X^2-333X-1369.
$$
`checks/curve37.py` reduces these equations to the two minimal models $E_a,E_b$ above. The involutions are $(x,y)\mapsto(-x,y)$ and its composition with the hyperelliptic involution. The induced maps on Jacobians yield a $(2,2)$-isogeny
$$
 J_0(37)\longrightarrow E_a\times E_b
$$
of degree 4: the two pullback/pushforward composites are multiplication by 2, and the cross terms vanish, since the involution acts with opposite signs on the two summands. Equivalently, the map and its dual compose to $[2]$ on the abelian surface. At the good prime 7, all rational groups in question have order 81, which is odd. A degree-four isogeny therefore induces an isomorphism on these finite groups. Hence
$$
 \boxed{J_0(37)(\mathbb F_7)\simeq[3,3,9]\ne[9,9]
 \simeq L_0/(1-M_0)L_0.}
$$
This is an integral obstruction already on the 3-adic Tate module, not just a polarization obstruction. It uses the classical identification of the sextic as $X_0(37)$, from memory (Ogg, *Hyperelliptic modular curves*, 1974, the level-37 genus-two model). Its arithmetic compatibility is checked at every requested good prime; no numerical agreement alone is being substituted for that model identification.

**Independent actual-Jacobian check at 5.** Moving the rational branch point $x=2$ to infinity gives over $\mathbb F_5$ the odd-degree model
$$
 y^2=x^5-2x^4-2x^3+x^2-2x-1.
$$
The script enumerates every reduced Mumford divisor and uses exact Cantor composition. There are 48 classes; the divisor with $(u,v)=(x^2-2x-1,2-2x)$ has order 48. Thus
$$
 J_0(37)(\mathbb F_5)\simeq[48],
$$
so both label constructions agree here with the Jacobian, although neither agrees with the product. This is a useful distinction between isogeny-class data and the actual lattice.

**Characteristic-two check completed.** The rational substitution $x=2X+1$, $y=8Y+4$ gives the integral equation
$$
 Y^2+Y=-X^6-3X^5-6X^4-7X^3-5X^2-2X.
$$
Its characteristic-two model is smooth: the affine derivative in $Y$ is one, and the unique point at infinity is smooth because the next coefficient after the leading term is odd. PARI's characteristic polynomial and a separate direct point count over $\mathbb F_2$ and $\mathbb F_4$ verify the missing ℓ = 2 comparison. The same transformed model agrees at 3, 5, and 7. Thus the original sextic was a correct rational model, with an unsuitable written reduction at 2.

### 3.5 P3$c$: the pairing is not the Jacobian's integral intersection form

**REFUTED for the saturated label lattice, with a PROVED obstruction.** For $g>0$, the intersection pairing on $H_1(X_0(p)(\mathbb C),\mathbb Z)$ is unimodular, as is the Weil pairing on the Tate module of its principally polarized Jacobian. In contrast,
$$
 \det\Omega_0=(g+1)^2.
$$
An integral symplectic isomorphism therefore cannot exist. At a coefficient prime $r\mid(g+1)$, it cannot exist over $\mathbb Z_r$ either. For $p=37$, this is determinant 9, and §3.4 strengthens the obstruction at $r=3$ to a disagreement of the underlying Frobenius modules at good reduction ℓ = 7. Removing a rational trivial summand does not remove this defect integrally.

**SKETCHED geometric explanation, using standard results from memory.** The semistable reduction of $X_0(p)$ at $p$ has two genus-zero components joined at the supersingular points (with the usual automorphism/thickness qualifications). For $p\equiv1\pmod {12}$, its toric character lattice is
$$
 X_p=\operatorname{Div}^0(S_p)=A_{n-1},
$$
and the monodromy pairing is the restriction of the Brandt pairing, here the dot product. Its matrix is $C_0$. The resulting component group is cyclic of order $n=(p-1)/12$, in agreement with the Smith form of $C_0$. This is the elementary modular-curve counterpart of the mechanism already recorded in `report/sections/04z_cerednik_drinfeld.tex`.

For a coefficient prime $r\ne p$, the semistable Tate-module sequence at $p$ has the form
$$
 0\longrightarrow X_p^\vee\otimes\mathbb Z_r(1)
 \longrightarrow T_rJ_0(p)
 \longrightarrow X_p\otimes\mathbb Z_r\longrightarrow0.
$$
The natural perfect alternating pairing pairs a lattice with its **dual**. Replacing the dual summand by $X_p$ through the monodromy map $C_0:X_p\to X_p^\vee$ pulls that pairing back to $\Omega_0$ and introduces precisely the index $n$ and determinant $n^2$. This explains the graph pairing's arithmetic origin without claiming it is already the principal pairing.

References **from memory**: Deligne–Rapoport, *Les schémas de modules de courbes elliptiques* (1973), the special fibre of $X_0(p)$; Grothendieck, SGA 7 I, Exposé IX (1972), the monodromy pairing and component group; Gross (1987), the supersingular pairing; Ribet, *On modular representations of $\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)$ arising from modular forms* (1990), the character-group/Hecke comparison. Precise integral identifications and conventions in these references are left for the cross-family review; the elementary discriminant obstruction above needs none of them.

The sequence is local at the **bad prime $p$**. A Frobenius at the unrelated good prime ℓ does not act on its graded pieces as though it were a global Galois filtration. A chosen splitting of this sequence is not a construction of the graph companion as a global Frobenius action. This is the same caution emphasized in the headers of `04u_deninger_lps.tex` and `04z_cerednik_drinfeld.tex`; the present proof does not redo their LPS/Shimura-curve construction.

**OPEN:** identify $L_{\rm red}$, with its step and a genuine arithmetic polarization, with a specific member of the modular Jacobian isogeny class in general. It removes the discriminant obstruction, and the small-group checks are encouraging, but those facts do not produce a canonical polarized comparison. Even a rational isomorphism of one-operator systems does not automatically preserve a specified alternating form: that is an additional compatibility problem.

## 4. P4 — what survives on the adelic and zeta side

**P4$i$, PROVED identities; HEURISTIC interpretation.** The exact quaternion construction is
$$
 S_p\simeq D^\times(\mathbb Q)\backslash D^\times(\mathbb A_f)/\widehat O^\times
 \simeq\Gamma\backslash\bigl\{\text{homothety classes of lattices in }\mathbb Q_\ell^2\bigr\},
 \qquad D_\ell^\times\simeq\operatorname{GSp}_2(\mathbb Q_\ell)=\operatorname{GL}_2(\mathbb Q_\ell).
$$
The similitude multiplier is the reduced norm, and its valuation records the tree displacement parity. The exact multiplicative comparison is
$$
 \mathbb Q^\times\backslash\mathbb A_f^\times/\widehat{\mathbb Z}^{\times}=\{*\},
 \qquad \mathbb Q_\ell^\times/\mathbb Z_\ell^\times\xrightarrow{\ v_\ell\ }\mathbb Z.
$$
The first equality is the trivial ideal class group of $\mathbb Q$: cancel every finite valuation by a rational number. The second is a valuation line, the discrete extended building of $\mathbb G_m$. The reduced building of $\operatorname{PGL}_1$ is a **point**, so “the tree for $\mathbb G_m$ is a line” requires this extended-building qualification. Embedded in the diagonal torus of $\operatorname{PGL}_2$, it is an apartment, with no branching; the symplectic diagonal embedding $a\mapsto\operatorname{diag}(a,a^{-1})$ moves by twice the valuation. These finite double cosets supply no analogue of the nontrivial finite cusp module in §1. This is a limitation of this construction, not a nonexistence theorem for a cohomology of $\zeta$. In particular, neither the point quotient nor the valuation line gives the global Riemann zeta function by the Pizer determinant identity. The exact ladder step here is the Hecke/curve numerator, obtained from the lattice quotient and its symplectic similitudes; extrapolating it to a global finite-rank $H^1$ for $\zeta$ is HEURISTIC and unsupported.

**P4(ii), REFUTED literally; PROVED corrected comparison.** The two “qunaughts” are not one object: $T_\ell(E_i)$ has rank two and belongs to a supersingular elliptic curve in characteristic $p$, whereas the nontrivial labels have rank $2g$ and model the cohomology of a different curve reduced in characteristic ℓ. For $p=37$, the ranks are already two and four, and the saturated global pairing is non-unimodular. What is exact for the *actual* Jacobian, after comparison choices, is
$$
 H_1(J_0(p)(\mathbb C),\mathbb Z)\otimes\mathbb Z_r
 \simeq T_rJ_0(p)\simeq T_r(J_0(p)_{\overline{\mathbb F}_\ell})
 \quad(r\ne\ell),
$$
with Betti/étale comparison and smooth proper specialization carrying the principal intersection form to the Weil pairing (up to the conventional Tate twist/sign). This comparison uses the Jacobian's own lattice; it does not replace that lattice with $L_0$ or with the local rank-two $T_\ell(E_i)$. At $r=\ell$ in characteristic ℓ, the étale Tate module has rank equal to the $\ell$-rank, not $2g$; the full height-$2g$ object is the divisible group/crystalline realization. Thus the brief's same-prime completion claim cannot be used at the good reduction prime. The unimodular reduction $L_{\rm red}$ is a constructive candidate for a global label lattice, but compatibility with an arithmetic principal polarization remains OPEN. The map actually proved is local lattices $\to$ class-set Hecke operator $\to$ a rational Frobenius system and its zeta determinant, not an identification of the vertex Tate module with the Jacobian Tate module.

**PROVED scope qualification for the round's adelic steer.** The quaternion construction is an inner-form version of the lattice/symplectic framework, locally identified with the original two-dimensional framework at ℓ. It is not a global identification with the fixed rational lattice $\mathbb Q^2\subset\mathbb A^2$ and its $\operatorname{SL}_2(\mathbb Q)$ action: no $\mathbb Q$-algebra isomorphism $D\simeq M_2(\mathbb Q)$ exists, since their ramification differs. The new global integral symplectic object in this lane is the Brandt label construction, followed by the cohomological comparison and the integral qualifications above.

## Correction ledger

| Brief statement or ambiguity | Verdict and corrected statement |
|---|---|
| Every unweighted Brandt matrix is an ordinary multigraph adjacency with two-dart loops. | **REFUTED.** Self-dual isogenies give reversal-fixed darts. The smallest counterexample is $B_{13}(2)=[3]$; the required genus-two counterexample is $B_{37}(2)$. |
| Ordinary Bass applies without another factor to those graphs. | **REFUTED.** Use $(1-u^2)^{m-n}(1+u)^h$ in the determinant, where $m$ counts paired edges and $h$ counts fixed darts. Alternatively use the norm-one bipartite double and the quadratic-extension numerator. |
| Symmetrize the row-counting $B$ by $W^{1/2}BW^{-1/2}$ when $W=\operatorname{diag}(w_i)$. | **SHARPENED.** The row convention needs $W^{-1/2}BW^{1/2}$; the displayed alternative applies to the transpose convention. |
| The Eisenstein vector is unspecified up to a weight convention. | **PROVED.** It is $\mathbf1$ for functions and $W^{-1}\mathbf1$ for the divisor transpose action. |
| Supersingular count and weights stated for all primes with the residue-modulo-twelve formula. | **SHARPENED.** That formula and $w_i\in\{1,2,3\}$ are for $p>3$. The identity $g=|S_p|-1$ is correct. The weights at $p=11$, in $j=(0,1)$ order, are $(3,2)$; at $p=101$, only $j=0$ has weight 3. |
| Maximal orders are indexed bijectively by the class set. | **SHARPENED.** Right ideal classes index the supersingular curves; their left orders may be conjugate. Do not replace the ideal class set by the type set. |
| The single-order group gives the full quotient only at class number one. | **SHARPENED.** Strong approximation gives one quotient for every class number. Stabilizers and inversions must be retained. |
| All neighbouring vertex lattices are self-dual in one fixed local symplectic space. | **SHARPENED.** The isogeny is a similitude of multiplier $\ell$; the target pairing rescales. With one fixed pairing, the self-dual representatives have one colour. |
| A Frobenius polynomial alone proves the companion/H¹ isomorphism. | **SHARPENED.** It also needs semisimplicity; companion endpoints fail. Weight-two regularity supplies the missing general input, and all numerical cells certify strictness directly. The comparison is after scalar extension to $\mathbb Q_r$, for one operator. |
| Positive Weil form iff the weak Weil bound, without an endpoint qualification. | **SHARPENED.** Nonnegative corresponds to the weak bound; positive corresponds to the strict bound. |
| The trivial mode splits off integrally, with its tutorial kernel unchanged. | **REFUTED/CONVENTION FIX.** The orthogonal direct sum has index $n^2$; the binding companion's eigenvalue-one kernel is $(\mathbf1,\mathbf1)$. Symplectic reduction gives a different index-$n$ overlattice. |
| The saturated nontrivial labels and their $\Omega$ are integral H¹ with its principal pairing. | **REFUTED.** Pairing determinant $n^2$; moreover at $(p,\ell)=(37,7)$ the rational-point groups differ, so even the unpolarized integral modules differ. |
| The two meanings of qunaught are one Tate module. | **REFUTED.** The ranks and underlying varieties differ; the valid Betti/Tate comparison uses the actual Jacobian and a coefficient prime distinct from the reduction prime. |
| The $\mathbb G_m$ tree is a line. | **SHARPENED.** The extended valuation building is a line; the reduced $\operatorname{PGL}_1$ building is a point. |
| The proposed $X_0(37)$ sextic might be wrong. | **NUMERICAL, with a model correction at 2.** It matches all requested local numerators after the explicit integral substitution at 2. |
| The two Cremona equations or their stated $a_2$ values might be wrong. | **NUMERICAL.** Both equations, conductors, and coefficients are verified; the installed Cremona database itself is unavailable. |

The monodromy explanation is SKETCHED; a general arithmetic identification of the unimodular reduced lattice remains OPEN. All other stated limitations above are part of the proved formulation, not unfinished numerical work.

## Numerical checks for the blind lane

All commands run from the repository root. The scripts automatically use the preinstalled PARI interpreter when necessary; they make no network requests. Arithmetic checks are exact. Printed floating eigenvalues are displays only; the bounds are certified by rational positive-definiteness tests. The saved-output audit reports 24 Brandt/Hecke cells, 16 actual-reversal Bass cells, eight weighted cells, four independent quaternion norm comparisons, four ordinary bipartite-double Bass checks, 36 Smith levels, 12 elliptic-product comparisons, four good curve-model polynomials, and eight direct curve point counts.

Six compact review targets:

| Certificate | Expected result | Script |
|---|---|---|
| Actual reversal at the smallest unweighted counterexample, $(p,\ell)=(13,2)$ | $B=[3]$, one fixed dart and one paired loop | pizer_graph.py or pizer_quotient.py |
| Cusp characteristic polynomial at $(37,2)$ | $x(x+2)$, hence $P=(1+2u+2u^2)(1+2u^2)$ | pizer_graph.py |
| Quaternion maximal-order reduced-trace discriminant at 37 | $-1369$; the three ideal classes recover the same four Brandt matrices | pizer_quotient.py --quaternion-only |
| Integral separation at $(37,7),k=1$ | saturated labels $[9,9]$; reduced labels and actual Jacobian $[3,3,9]$; common order 81 | label_lattice.py, with the degree-four quotient proof in §3.4 |
| Direct actual-Jacobian group over $\mathbb F_5$ | cyclic order 48; the elliptic product is $[2,24]$ | curve37.py and label_lattice.py |
| Good characteristic-two curve model | $\#X_0(37)(\mathbb F_2)=5$, $\#X_0(37)(\mathbb F_4)=9$ | curve37.py |

Commands:

    python3 notes/astra-2026-10-27/pizer/astra/checks/pizer_graph.py
    python3 notes/astra-2026-10-27/pizer/astra/checks/pizer_quotient.py
    python3 notes/astra-2026-10-27/pizer/astra/checks/label_lattice.py
    python3 notes/astra-2026-10-27/pizer/astra/checks/curve37.py
    python3 notes/astra-2026-10-27/pizer/astra/checks/check_summary.py

Saved outputs are the correspondingly named output_pizer_graph.txt, output_pizer_quotient.txt, output_label_lattice.txt, output_curve37.txt, and output_check_summary.txt in checks/. The independent quaternion-only output is output_quaternion.txt. The summary script audits completeness and records SHA-256 hashes of the numerical outputs. The two probe scripts preserve local PARI API documentation and exploratory arithmetic; they are not needed for the final certificates.

## What this changes in the notebook

These are **candidate rows only, pending cross-family REFUTE review**. Nothing has been registered, and no record page has been edited.

| Candidate id | Status | Statement and location |
|---|---|---|
| thm:pizer-brandt-x0p | PROVED, classical inputs named | Weighted Brandt determinant equals $(1-u)(1-\ell u)P_{p,\ell}(u)$; row/transpose normalization settled (§1.1). |
| prop:pizer-ihara-halfloops | PROVED; original ordinary-loop assertion REFUTED | Actual reversal can have fixed darts; corrected Bass factor $(1-u^2)^{m-n}(1+u)^h$ (§1.2). |
| cor:pizer-ramanujan-weil | PROVED | Weil for $J_0(p)$ gives the Ramanujan bound in weight two (§1.3). |
| prop:pizer-tree-quotient | PROVED, strong approximation input named | One $O[1/\ell]^\times$ quotient works at every class number, with edge indices/inversions retained (§2.2). |
| prop:pizer-norm-parity-double | PROVED | The norm-one subgroup has index two, gives the bipartite double, and in the unweighted case an ordinary Ihara identity with $P_{p,\ell^2}(u^2)$ (§2.3). |
| prop:pizer-label-space-h1 | PROVED with the recalled weight-two regularity theorem; otherwise PROVED-conditional on H-strict | Noncanonical one-Frobenius comparison after extension to $\mathbb Q_r$; no automatic integral or polarized comparison (§3.1). |
| prop:pizer-label-integral-obstruction | PROVED | The trivial pair does not split integrally; $\det\Omega_0=n^2$; saturated labels differ even from actual Jacobian Tate data at $(37,7)$ (§§3.2, 3.4–3.5). |
| prop:pizer-label-symplectic-reduction | PROVED | $e^\perp/\mathbb Ze$ is a unimodular, $M,V$-stable index-$n$ overlattice of the saturated cusp labels (§3.3). |
| num:pizer-label-lattice-smith | NUMERICAL, exact certificates | All requested Smith forms and elliptic-product comparisons, with equal orders but differing structures (§§3.2–3.4). |
| num:pizer-j37-finite-groups | NUMERICAL with exact group-law certificate; degree-four comparison PROVED | $J_0(37)(\mathbb F_5)=[48]$ and $J_0(37)(\mathbb F_7)=[3,3,9]$ (§3.4). |
| sketch:pizer-monodromy-pairing | SKETCHED, references from memory | The Brandt pairing restricts to the bad-prime monodromy form; replacing the dual character lattice creates the discriminant defect (§3.5). |
| prop:pizer-adelic-scope | PROVED identities and obstructions; zeta extrapolation HEURISTIC | Exact quaternion and multiplicative double cosets; local/global Tate objects are different; the inner form is only locally split (§4). |
| question:pizer-reduced-jacobian-lattice | OPEN | Identify the unimodular reduced labels and an arithmetic polarization within the modular Jacobian isogeny class (§3.5). |

Proposed one-line annotations:

- **graph-ihara.md §2(a)–(b):** Pizer graphs are arithmetic quotients of the local symplectic-similitude lattice tree; fixed-pairing qunaughts occupy one colour, and quotient edge inversions produce half-loops.
- **graph-ihara.md §3:** The $K_4/E$ spectral coincidence has an arithmetic counterpart: Brandt plus Eichler–Shimura identifies the Pizer determinant with the $X_0(p)$ numerator, with explicit loop corrections and no automatic integral Jacobian identification.
- **graph-ihara.md §8(4):** In this weight-two modular family, the Ramanujan bound comes from Weil's theorem for the Jacobian; general-weight Deligne is unnecessary.
- **data-ladder.md §0:** Add the Pizer rung: a quaternion class-set operator supplies a rational modular-curve Frobenius system and explicit integral label lattices, whose choice is finer than the zeta numerator.
- **data-ladder.md §1.2–§1.3:** Removing the trivial mode integrally is a substantive choice: at $(37,7)$ saturated and symplectically reduced labels have equal counts and different groups, while the saturated pairing has discriminant 9.
- **lattice-tower.md §§1–2:** For arithmetic graph companions, specify the integral removal of trivial modes before interpreting the cokernel tower as the Jacobian's point groups.

The next mathematical step is a comparison of the **full polarized modules**, not more equality-of-order tests: start with the unimodular reduction for $J_0(37)$, its explicit degree-four elliptic splitting, and the coefficient primes 2 and 3. The review should first check the recalled Coleman–Edixhoven regularity statement and the classical level-37 model identification, then test the half-loop determinant and the integral counterexample independently. The LPS/Shimura-curve route in 04u/04z already records the analogous distinction between a local monodromy lattice and a global one-Frobenius model; the present result supplies a small, fully computable modular-curve version.
