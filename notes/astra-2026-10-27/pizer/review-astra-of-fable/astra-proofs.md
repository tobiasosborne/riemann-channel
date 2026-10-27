# Adversarial REFUTE review of the Fable Pizer lane

Author: `codex:gpt-6-astra` (reviewer of `claude:fable-5.1`).
Date: 2026-10-27. Cross-family review; no record changes are made.

## Scope and procedure

Read the round brief, binding REFUTE protocol, lane brief, complete Fable proof and its scripts. The other astra proof remains unread until the verdict lines are written. All review artifacts are confined to this directory. The author's scripts write output files beside themselves, so reruns use byte-identical source copies in `checks/rerun/`; this avoids modifying the reviewed lane. Independent computations and derivations will be recorded below as completed.

The review distinguishes three assertions: equality of Frobenius polynomials, isomorphism of integral Frobenius modules, and isometry of paired lattices. None implies the next without additional proof. In particular, comparison with an elliptic product is a comparison with the Jacobian only at primes not dividing an established isogeny degree.

## First completed audit: the elliptic quotients and the conjecture

**P3b, isogeny dependency — PROVED by explicit maps, with a correction to the author's explanation.** Write

\[
 C:y^2=-x^6-9x^4-11x^2+37.
\]

The two elliptic involutions are \(s(x,y)=(-x,y)\) and \(hs(x,y)=(-x,-y)\), where \(h\) is the hyperelliptic involution. The quotient by \(h\) itself has genus zero, so the sentence saying that one elliptic quotient is “by the hyperelliptic involution” is false. The actual maps are

\[
 \pi_1(x,y)=(-x^2,y),\qquad
 \pi_2(x,y)=(37/x^2,37y/x^3),
\]

onto

\[
 E_+:Y^2=X^3-9X^2+11X+37,\qquad
 E_-:Y^2=X^3-11X^2-333X-1369.
\]

Both maps extend over the smooth projective curves and have degree two. The substitutions \((X,Y)=(4u+3,8v+4)\) and \((4u+5,8v+4)\), respectively, give *exactly*

\[
 E_1:v^2+v=u^3-u,\qquad E_2:v^2+v=u^3+u^2-23u-50.
\]

These are polynomial identities, checked in `checks/independent_arithmetic.py`; no inference from matching Hecke eigenvalues, Cremona numbering, or an unspecified isogeny class is used to identify the targets. The pullbacks of the invariant differentials are \(-2x\,dx/y\) and \(-2\,dx/y\), hence independent. The induced maps \(\alpha:E_1\times E_2\to J(C)\) (sum of pullbacks) and \(\beta:J(C)\to E_1\times E_2\) (pushforwards) satisfy \(\beta\alpha=[2]\times[2]\): cross terms vanish because the two elliptic factors have opposite eigencharacters under \(s\), while \(h\) acts as \([-1]\) on the Jacobian. These maps are dual under the principal polarizations. Thus \(\deg\alpha=\deg\beta=4\), with 2-primary kernels. This supplies the missing degree certificate, conditional only on the standard identification of this stated model with \(X_0(37)\) (Mazur–Swinnerton-Dyer, *Arithmetic of Weil curves*, 1974, model identification cited from memory; finite point-count matches alone do not prove that identification).

At every odd good reduction prime the degree-four isogeny identifies odd-primary Tate modules and odd-primary point groups. Consequently the author's 3-part argument at \(\ell=7\) survives: the graph gives \((\mathbf Z/9)^2\), whereas the Jacobian gives \(\mathbf Z/9\oplus(\mathbf Z/3)^2\). An unspecified isogeny with a 3-part would **not** justify that conclusion; the explicit degree-four construction is essential.

**`conj:pizer-lattice-away-from-eisenstein` — REFUTED in both directions.** The claim is an isomorphism of unpaired \(\mathbf Z_q[F]\)-modules iff \(q\nmid n=(p-1)/12\), with the implicit necessary restriction \(q\ne\ell\). Discriminant of an alternating form does not decide this unpaired question.

* Already in the printed cells \((p,\ell)=(37,2),(37,5)\), the Frobenius characteristic polynomial is squarefree modulo 3. For \(\ell=2\) it is \((t^2+2t+2)(t^2+2)\), whose two factors and their product are separable modulo 3; \(\ell=5\) gives the same reduction. Thus \(R=\mathbf Z_3[t]/(\chi_F)\) is finite étale, a product of unramified discrete valuation rings. Every full \(F\)-stable lattice in this multiplicity-one rational module is a rank-one projective \(R\)-module and hence free. The graph and Jacobian Tate lattices are therefore isomorphic, although \(3\mid n\). This is a proof of agreement, stronger than equality of the four printed cokernel groups. The new \((37,11,3)\) cell has the same property.
* The independently computed new cell \((p,\ell,q)=(37,139,2)\) refutes sufficiency. Quaternion theta series give, in the author's vertex order,

\[
 B(139)=\begin{pmatrix}48&44&48\\44&48&48\\48&48&44\end{pmatrix},
 \quad B(139)|_X=\begin{pmatrix}0&-4\\-4&0\end{pmatrix}.
\]

Hence \(L_0/(1-M_{139})L_0\simeq\mathbf Z/4\oplus\mathbf Z/4896\), with 2-torsion rank two. On the curve, the sextic has the six distinct roots \(35,37,49,90,102,104\) modulo 139. All six Weierstrass points are rational, so \(J(C)[2](\mathbf F_{139})\simeq(\mathbf Z/2)^4\). Indeed \(J[2]\) is the space of even subsets of the six branch points modulo complementation, of dimension four. Thus the two Frobenius modules cannot be isomorphic, although \(2\nmid3\). This uses the Jacobian itself, not the elliptic product or a disputed 2-primary isogeny comparison.

A correct replacement is conditional: integral cyclicity of Frobenius and the relevant integral Hecke-module structure matter. The condition \(q\nmid n\) says precisely that the *specified graph pairing* is perfect at \(q\); it is neither necessary nor sufficient for the asserted unpaired Frobenius-module isomorphism.

## P1 and the half-loop lemma

**Restatement.** The kernel-count Brandt operator has Eisenstein eigenvalue \(\ell+1\); its remaining eigenvalues are the weight-two cuspidal Hecke eigenvalues. Its quadratic determinant is \((1-u)(1-\ell u)P_{p,\ell}(u)\), and for the unweighted supersingular graph a specified dual-isogeny reversal gives the corrected Ihara determinant.

**Normalization audit — PROVED.** If \(B_{ij}\) counts kernels on \(E_i\) with quotient isomorphic to \(E_j\), then \(2w_jB_{ij}=\#\operatorname{Hom}_\ell(E_i,E_j)=2w_iB_{ji}\). Thus \(BW=WB^t\), \(B\mathbf1=(\ell+1)\mathbf1\), and \(\mathbf1^tW^{-1}B=(\ell+1)\mathbf1^tW^{-1}\). On column *functions* the inner product is \(W^{-1}\), and the symmetric conjugate is \(W^{-1/2}BW^{1/2}\). On column *divisors* the matrix is \(B^t\), the pairing is \(W\), and the Eisenstein vector is \(W^{-1}\mathbf1\). The author's definitions are consistent, except that the later shorthand “B is self-adjoint for Gross's pairing” must explicitly retain the divisor/row convention. Degree zero on the function side is \(\sum f_i/w_i=0\), not \(\sum f_i=0\) when weights differ. For \(p=2,3\), the definition \(w_i=|\operatorname{Aut}E_i|/2\) remains appropriate but the list \(\{1,2,3\}\) does not; the numerical table only treats \(p>3\).

The modular-polynomial product counts kernels with multiplicity, including at the exceptional j-invariants. Eichler's prime-level Brandt-module theorem and Eichler–Shimura then give the determinant identity exactly as written. This uses the away-from-p Hecke algebra; an unqualified assertion about all operators at the ramified prime requires its own normalization. The product over newforms must include all coefficient-field embeddings, as the author does. Weil's theorem gives the Ramanujan bound. This is a statement about the Brandt spectrum; in the weighted cases it is not the spectrum of an ordinary undirected adjacency matrix obtained by forgetting stabilizers.

**Weil-form correction.** For the convention actually fixed in the brief and proof,

\[
 M=\begin{pmatrix}B&-\ell I\\I&0\end{pmatrix},\quad
 V=\ell M^{-1}=\begin{pmatrix}0&\ell I\\-I&B\end{pmatrix},\quad
 \tfrac12\Omega(M-V)=\begin{pmatrix}I&-B/2\\-B/2&\ell I\end{pmatrix}.
\]

The displayed \(\bigl(\begin{smallmatrix}\ell I&B/2\\B/2&I\end{smallmatrix}\bigr)\) in §1.2 belongs to the other convention in `graph-ihara.md`, not this \(M\). The positivity criterion is unchanged. With unequal weights the function-side form must use \(\Omega_{W^{-1}}\), or one must move to symmetric coordinates; the ordinary \(\Omega\) does not give a symplectic similitude for nonsymmetric \(B\).

**Half-loop lemma — PROVED by independent derivation.** Let \(\mathcal E\) be a finite set of arcs, with origin and terminus, and an involution \(J\) interchanging them; allow fixed arcs, necessarily loops. Assume every vertex has \(d=\ell+1\) outgoing arcs. This is the precise hypothesis, stronger than an unspecified “quotient of a tree” with stabilizers. Let \(U\) be origin incidence and \(V_0=JU\) terminus incidence. Then

\[
 H=V_0U^t-J,\quad
 \det(I-uH)=\det(I+uJ)\det\left(I-uU^t(I+uJ)^{-1}V_0\right).
\]

As \(U^tV_0=A\), \(U^tJV_0=dI\), and \((I+uJ)^{-1}=(I-uJ)/(1-u^2)\), the second determinant is \(\det(I-uA+(d-1)u^2)/(1-u^2)^n\). If \(f\) arcs are fixed by reversal and \(m=(N-f)/2\) are reversal pairs, then \(\det(I+uJ)=(1+u)^f(1-u^2)^m\). Therefore

\[
 \boxed{\det(I-uH)=(1+u)^f(1-u^2)^{m-n}\det(I-uA+\ell u^2).}
\]

This identity in rational functions is a polynomial identity after cancellation; \(m-n\) may be negative. No exponent involving a rounded value of \(N/2\) is legitimate. In particular, one vertex with one fixed arc has \(H=0\), \(d=1\), and the formula gives \((1+u)(1-u^2)^{-1}(1-u)=1\). One vertex with one ordinary loop pair gives \((1-u)^2\). These independent degenerate tests are in `independent_matrices.py`.

For \(p\equiv1\pmod {12}\), automorphisms modulo sign are trivial. Kernel duality is then an actual involution on the author's arc set. If a kernel is fixed, \(\widehat\phi=\epsilon\phi\), \(\epsilon=\pm1\). The positive sign would make \(2\phi\) a scalar, impossible for norm the prime \(\ell\); the negative sign gives trace zero and \(\phi^2=-\ell\). Division by two counts \(\pm\phi\) exactly. This trace-zero count is not asserted without modification at vertices with larger automorphism groups.

**Numerical audit — reproduced, with a transcription correction.** The full graph script's saved output is reproduced byte for byte. Independent quaternion theta series reproduce all four \(p=37\) matrices and \(f=(1,0,2,0)\). Independent arc pairing and closed-walk trace recurrences reproduce all twelve printed Hashimoto determinant polynomials; CM embedding counts supply a separate check of \(f\) (the small quadratic class numbers are computed by enumerating reduced binary quadratic forms). The 20 Brandt/Hecke polynomial identities and strict spectral bounds are checked again in exact arithmetic. Direct point enumeration over \(\mathbf F_\ell\) and \(\mathbf F_{\ell^2}\), using an independent finite-field implementation, recovers all eight genus-two numerators without `hyperellcharpoly`.

There is a genuine textual error: \(\#X_0(109)(\mathbf F_7)=10\), **not 8** as stated in §1.4 and closing numerical check 2, and not 14 as in the parenthetical list in §1.4. The saved script output is correct: \(\operatorname{Tr}B(7)=6\), \(\operatorname{Tr}T_7=-2\), so the answer is \(8-(-2)=10\). The four correct counts for \(p=109\) are \(5,4,8,10\).

**Weighted zeta — UNVERIFIED as stated.** The determinant identity for weighted Brandt matrices is proved. The paragraph identifying a formula with an unspecified exponent “(…)” with Bass's zeta of a graph of groups does not define the edge operator, its weights, or its Euler factors. A bibliography is not a verification of that missing formula. Do not register this additional zeta identification until those data and a weighted test, e.g. \((11,2)\), are supplied.

## P2: the arithmetic quotient and the quaternion check

**Restatement.** A single localized maximal-order unit group has the entire supersingular class set as its vertex quotient, for any class number; adjacency is the Hecke neighbor correspondence. The quotient identifies both tree colors.

**Local lattice argument — PROVED.** The perfect Tate-module Weil pairing establishes self-duality after a trivialization of the Tate twist. The preimage \(L_C=\ell^{-1}\{t\in T:t\bmod\ell\in C\}\) has \(L_C/T=C\). Naturality modulo \(\ell\) shows \(\phi^{-1}T(E/C)=L_C\), and duality gives \(e(\phi x,\phi y)=\ell e(x,y)\). Thus the lattice index and similitude factor are correct. Being self-dual is a statement about a representative and a fixed form, not about every representative of a homothety class.

**Strong approximation and double cosets — PROVED, with convention fixes.** Put \(G=B^\times(\mathbb A_f)\), \(H=B^\times(\mathbb Q)\), \(U=\widehat O^\times\), and \(K'=B^\times(\mathbb Q_\ell)\widehat O^{(\ell)\times}\). Normalize the reduced norm of an arbitrary adele by a positive rational norm, an \(\ell\)-component, and a compact unit norm. Surjectivity of reduced norm on rational positive elements and local maximal-order units gives those choices. Strong approximation for the simply connected \(B^1\), noncompact at \(\ell\), then gives \(G=HK'\). This use of strong approximation is valid despite definiteness at infinity: the noncompact place omitted from the adelic approximation is \(\ell\). In the author's multiplication rearrangement only the away-from-\(\ell\) unit component is commuted past the \(\ell\)-components; no illegal commutation in the quaternion algebra is needed.

For \(U\subset K'\subset G\) and \(G=HK'\), the elementary map \((H\cap K')\backslash K'/U\to H\backslash G/U\) is bijective. If \(k_2=hk_1u\), then \(h=k_2u^{-1}k_1^{-1}\in K'\), proving injectivity. Here \(H\cap K'=O[1/\ell]^\times\). Scalars \(\ell^\mathbf Z\) remove homothety, while local scalar units already lie in \(O_\ell^\times\). This yields exactly

\[
 \mathrm{Cl}(O)\cong\Gamma\backslash\mathrm{PGL}_2(\mathbb Q_\ell)/\mathrm{PGL}_2(\mathbb Z_\ell),
 \qquad \Gamma=O[1/\ell]^\times/\mathbf Z[1/\ell]^\times.
\]

The diagonal \(\mathrm{diag}(\ell,1)\) double coset supplies \(\ell+1\) neighbors counted with their local multiplicities. Vertex stabilizers are \(O_i^\times/\{\pm1\}\): scale any representative fixing a vertex to determinant valuation zero, then it is a unit at every finite place. Absence of eigenvalue \(-\ell-1\), from Eichler–Shimura and Weil, excludes a bipartition of the neighbor relation. Thus there are odd-norm elements and both tree colors lie over every quotient vertex. Connectedness is also immediate from the connected tree. There is no need for class number one.

Three repairs are required for a literal record statement:

1. The Hom module \(\operatorname{Hom}(E_0,E)\) is naturally a **right** \(\operatorname{End}(E_0)\)-module. To use the author's left ideals and right orders, take \(\operatorname{Hom}(E,E_0)\), or reverse every ideal convention consistently.
2. At unequal weights the ordinary orbit graph is **not** the kernel-count multigraph. The stabilizer can identify different outgoing tree edges; the Brandt entry is the sum of indices \([\Gamma_v:\Gamma_e]\) of the corresponding edge orbits. For example the printed \(B_{11}(2)=\bigl(\begin{smallmatrix}1&2\\3&0\end{smallmatrix}\bigr)\) is asymmetric and cannot be an ordinary undirected adjacency matrix. The correct all-p assertion is an identification with an **edge-indexed quotient graph / graph of groups**. The unweighted multigraph statement, with inversions, holds when all \(w_i=1\).
3. The number of conjugacy types of maximal orders need not equal the ideal class number. In particular, the phrase “maximal orders fall into h types” is not justified. Localizations for different maximal orders can be related through an \(\ell\)-supported ideal representative; the resulting quotient has the same class-set description. This does not imply that the original maximal orders are rationally conjugate.

**Independent quaternion certificate — NUMERICAL / exact.** `independent_theta.py` verifies the supplied order's identity element, multiplication closure and reduced discriminant 37. It enumerates all 35 two-dimensional subspaces of \(O/2O\), retains the three stable under left multiplication, and obtains the two nonprincipal norm-two ideal classes. Norm-one Hom theta coefficients separate the three classes. Instead of the author's repeated neighbor enumeration and PARI `qfminim`, the review uses SymPy HNF, its own exact Gram reduction and an exhaustive bounded-vector enumeration of the six Hom lattices \(\overline I_i I_j\). The coordinate bounds follow from \(|z_i|^2\le R(Q^{-1})_{ii}\), so the enumeration is complete. The coefficient at norm \(\ell\,\mathrm{nrd}(I_i)\mathrm{nrd}(I_j)\), divided by the target unit count two, gives \(B_{ij}(\ell)\). The coefficients at norm one give three unit counts two and mass \(3/2\); the known mass formula exhausts the class set. This proves that the computation did not silently miss an ideal class.

The resulting four matrices agree with the modular-polynomial matrices under the single permutation \((1,2,0)\); trace-zero norm counts give \(1,0,2,0\). The same enumeration supplies \(B(11)\) and \(B(139)\) for the new cells. This independently verifies the author's P2 matrices and inversion counts, rather than reusing its ideal equivalence tests. A post-verdict convention check records one scalar-label correction: the signed reduced-trace Gram determinant is **−1369**; the script computes its absolute value 1369 and labels it as the determinant. The reduced discriminant 37 and maximality conclusion are unchanged; see `independent_conventions.py`.

## P3a and the rational identification: which lattice and which Frobenius?

**Restatement.** Remove the trivial rank-two plane by taking its integral symplectic orthogonal. The remaining lattice has the curve's Frobenius polynomial; its cokernel groups have Jacobian point-count orders, but their abstract structures need not be Jacobian point groups.

**The integral lattice — PROVED.** For \(p\equiv1\pmod {12}\), put \(X=\ker(\mathbf Z^n\xrightarrow{\sum}\mathbf Z)\). Symmetry and constant row sums make \(X\) stable under \(B\), and

\[
 L_0=X\oplus X=(\mathbf Z\mathbf1\oplus\mathbf Z\mathbf1)^{\perp_\Omega}.
\]

It is saturated, of rank \(2(n-1)\). Its definition as the kernel of the rational trivial-mode projection gives exactly the same integral lattice. Since \(\mathbf Z^n/(X+\mathbf Z\mathbf1)\cong\mathbf Z/n\), the specified trivial and nontrivial lattices together have index \(n^2\) in \(\mathbf Z^{2n}\). This does not mean \(L_0\) itself has finite index in that higher-rank lattice. In the author's basis \(e_i-e_n\), the restricted Brandt matrix is \(B_{ij}-B_{in}\); the code implements that correctly.

The alternative quotient \((\mathbf Z^n/\mathbf Z\mathbf1)^2\) is dual to \(X^2\) on the vertex factors. One detail suppressed by the author is harmless: the companion of \(R^t\) is not literally the transpose of the companion of \(R\). Nevertheless, with \(C(R)=\bigl(\begin{smallmatrix}R&-\ell I\\I&0\end{smallmatrix}\bigr)\) and the unimodular matrix \(S=\bigl(\begin{smallmatrix}0&I\\I&-R^t\end{smallmatrix}\bigr)\),

\[
 S C(R^t)=C(R)^t S.
\]

Thus all Smith forms of \(1-C(R)^k\) agree with those for the dual quotient. The claimed invariance of the numerical table under this alternative convention is correct.

**Rational comparison — correct after repairing the proof and coefficient fields.** The characteristic-polynomial identity is immediate from P1. But “B is symmetric, hence M is semisimple” is false in general: a scalar adjacency eigenvalue \(a=2\sqrt\ell\) gives a nontrivial Jordan block in \(\bigl(\begin{smallmatrix}a&-\ell\\1&0\end{smallmatrix}\bigr)\). Repeated quadratic factors arising from *different* Hecke eigenlines, such as \(\ell=7,p=37\), are harmless; a repeated root *inside* one quadratic factor is the issue.

For every printed cell the review checks \(\gcd(\chi_{T_\ell}(t),t^2-4\ell)=1\) and isolates the Hecke roots with rational intervals proving strict inequalities. This alone repairs all numerical instances. For completeness, a general weight-two good-reduction repair can be derived using the following additional standard theorem: the filtered crystalline module of an abelian variety with good reduction over \(\mathbf Q_\ell\) is weakly admissible (Fontaine's good-reduction comparison/weak-admissibility theorem, cited from memory).

Indeed, let \(A_f\) be a newform factor, \(K\) its Hecke field, and \(d=\dim A_f=[K:\mathbf Q]\). If an embedding gives \(a_\ell^2=4\ell\), this is an identity in \(K\). On the crystalline \(H^1\), Frobenius satisfies \((F-a_\ell/2)^2=0\). Frobenius is semisimple for abelian varieties over finite fields; it commutes with the semisimple \(K\)-action, so \(F=a_\ell/2\). The Hodge subspace \(\mathrm{Fil}^1\), of dimension \(d>0\), is \(K\)-stable and therefore \(F\)-stable. All its Newton slopes are \(1/2\), giving \(t_N=d/2\), while the induced Hodge filtration gives \(t_H=d\). This contradicts weak admissibility. Hence each quadratic has distinct roots. Diagonalizing the self-adjoint Hecke operator now really does prove semisimplicity of the companion. This extra argument is absent from the submitted proof; Weil's non-strict bound alone would not suffice.

The correctly typed conclusion, for every coefficient prime \(q\ne\ell\), is

\[
 (L_0\otimes\mathbf Q_q,M_\ell)\ \cong\
 (V_qJ_0(p)_{\mathbf F_\ell},F_\ell)
\]

as semisimple one-operator modules. Equivalently one can use geometric Frobenius on étale \(H^1\); arithmetic Frobenius acts on the covariant Tate module. Semisimple modules over \(\mathbf Q_q[t]\) with the same characteristic polynomial have the same irreducible constituents and multiplicities. There is no tensor product “over Q” that turns an unspecified Betti \(H^1(X_0(p),\mathbf Q)\) into a canonically defined Frobenius module. The graph supplies a rational form of the one-operator system, not a canonical Betti or Galois identification. The coefficient prime \(q=p\) is allowed here as long as \(q\ne\ell\).

**All 48 Smith forms — NUMERICAL / exact, independently reproduced.** `independent_matrices.py` changes to the simple-root basis \(e_i-e_{i+1}\) of \(X\), with Cartan Gram matrix rather than the author's all-ones-plus-identity Gram. PARI `matsnf` reproduces the author's FLINT invariant factors in every cell. Independently of the author's resultant formula, put \(S_0=2I\), \(S_1=T_\ell\), \(S_k=T_\ell S_{k-1}-\ell S_{k-2}\). Then

\[
 \#J_0(p)(\mathbf F_{\ell^k})
 =\det\big((1+\ell^k)I-S_k\big).
\]

This identity follows pair by pair from \(S_k(a)=\alpha^k+\beta^k\), \(\alpha\beta=\ell\); it gives all 48 orders exactly. In particular the large \((109,7,4)\) order is \(1126236986928850407683097600\), and its invariant factors are \(4,4,120,586581764025442920668280\). Equality of these orders carries no group-structure information beyond the Frobenius polynomial.

## P3b: the abstract groups and the surviving “third lattice” conclusion

The explicit degree-four isogeny was proved above. `independent_arithmetic.py` also recomputes all sixteen pairs \(E_i(\mathbf F_{\ell^k})\), \(\ell=2,3,5,7\), \(1\le k\le4\), without `ellgroup`, `ellcard`, or the author's finite-field routines: it constructs polynomial-basis finite fields, enumerates every point, implements the generalized Weierstrass group law, and finds element orders and the group exponent. Every product invariant-factor list agrees with the saved output. In particular the products are \(\mathbf Z/2\oplus\mathbf Z/24\) at \((5,1)\) and \((\mathbf Z/3)^2\oplus\mathbf Z/9\) at \((7,1)\), versus graph groups \(\mathbf Z/48\) and \((\mathbf Z/9)^2\).

The rigorous local comparison is

\[
 T_qA/(1-F_\ell^k)T_qA\ \cong\ A(\mathbf F_{\ell^k})[q^\infty],\qquad q\ne\ell.
\]

It follows by applying \(1-F^k\) to \(0\to T_qA\to V_qA\to A[q^\infty]\to0\): the middle map is invertible because none of the Weil eigenvalues has a power equal to one. Therefore the displayed discrepancy at \(q=2,\ell=5\) refutes equality with the elliptic-product Tate lattice, and the discrepancy at \(q=3,\ell=7\) refutes equality with both the product and Jacobian Tate lattices. No ordinary canonical lift is needed.

The author's justification “ordinary at \(\ell=5,7\) since \(a_\ell\not\equiv0\)” is **wrong at 5**: its own table says \(a_5(E_2)=0\). Thus one cannot invoke the ordinary Deligne-module theorem for the whole product there. The prime-to-characteristic Tate-module argument above repairs both refutations. At the characteristic prime itself the full-rank lattice should not be equated with the geometric Tate module, whose rank is only the p-rank.

The review can also resolve the submitted proof's uncertainty about the Jacobian's 2-part at \(\ell=5\). The branch factorization has degrees \(1,1,4\), and the even-subset computation gives \(\#J[2](\mathbf F_5)=2\). The Frobenius polynomial modulo 2 is \((t+1)^4\), so Frobenius on \(J[2]\) has one Jordan block and is cyclic. The graph's Smith form \([48]\) gives the same one-dimensional fixed space and hence the same cyclicity. Lifting a cyclic vector by Nakayama gives a companion basis on both free \(\mathbf Z_2\)-modules; consequently

\[
 L_0\otimes\mathbf Z_2\cong T_2J_0(37)_{\mathbf F_5}
\]

as Frobenius modules. The discrepancy with the product at 2 is precisely a place where replacing the Jacobian by its isogenous product would give the wrong answer. At every other coefficient prime \(q\ne5\), the discriminant \(128000=2^{10}5^3\) is a unit, so the squarefree-polynomial argument gives the same conclusion. This strengthens, rather than merely repeats, the warning that matching point-group orders does not fix the lattice.

The “third lattice” assertion is thus established at \((p,\ell,q)=(37,7,3)\), but must not be universalized to every \(\ell\), nor localized only at component-group primes. The new \((37,139,2)\) cell already proves failure at a prime away from that component group.

## P3c: the pairing obstruction and the monodromy sketch

**Restatement and obstruction — PROVED.** The specified graph alternating form is a doubled positive vertex pairing, not an integral principal intersection pairing. In the \(e_i-e_n\) basis,

\[
 C=I_{n-1}+\mathbf1\mathbf1^t,\quad
 \Omega_0=\begin{pmatrix}0&C\\-C&0\end{pmatrix},\quad
 \det C=n,\quad\det\Omega_0=n^2.
\]

The determinant lemma gives \(\det C=1+(n-1)=n\); the Smith form of \(C\) is \(1,\ldots,1,n\). Thus the alternating lattice has polarization type \((1,\ldots,1,n)\) and is not isometric to a unimodular intersection lattice when \(n>1\). In the simple-root basis the same calculation is the determinant of the \(A_{n-1}\) Cartan matrix; the independent computation gives \(9,36,81\) for \(\det\Omega_0\). Over \(\mathbf Z_q\) this obstruction holds exactly when \(q\mid n\). It is an obstruction for the **specified form**, not for all possible forms on the same unpaired Frobenius module.

**Monodromy identification — correct with its stated geometric input.** For \(p\equiv1\pmod {12}\), the standard Deligne–Rapoport model has two geometric rational components meeting at the \(n\) supersingular points, each of thickness one. Its dual graph has two vertices and \(n\) edges, all oriented the same way. The boundary map is \((a_i)\mapsto(-\sum a_i,\sum a_i)\), so its cycle group is exactly \(X\). The normalization sequence for line bundles identifies the torus character group with this cycle group. The semistable monodromy formula is the edge-length pairing \(b(a,c)=\sum_i a_ic_i\) (Deligne–Rapoport, 1973; Grothendieck, SGA 7 IX; standard statements cited from memory). Restricting it to \(X\) gives \(C\). Hence the form on \(X\oplus X\) is

\[
 \Omega_0((a,b),(c,d))=b(a,d)-b(b,c),
\]

which makes “doubled monodromy” precise. It is not a claim that the skew form itself is Grothendieck's symmetric monodromy pairing. The monodromy exact sequence \(0\to X\to X^\vee\to\Phi_p\to0\) gives \(\Phi_p\cong\mathbf Z/n\) in this case, so the discriminant identity \(\det\Omega_0=|\Phi_p|^2\) follows without guessing from the component-group order.

The weighted generalization uses edge thicknesses \(w_i\): the Gram determinant is \((\prod_iw_i)(\sum_i1/w_i)\), not generally \(n\). In particular it is 5 at \(p=11\) and 25 at \(p=101\). The unweighted hypothesis must remain on the candidate \(n^2\) statement.

There is an abstract index-\(n\) pairing-preserving embedding \(X\oplus X\to X\oplus X^\vee\), \((a,b)\mapsto(a,b(b,-))\), where the target carries the evaluation alternating form. This explains the index, but does **not** produce an integral Frobenius-compatible embedding into \(T_qJ\). A rational identification of the alternating spaces and a separate rational identification of one-operator modules do not automatically yield a simultaneous polarized identification.

The author's warning about the Raynaud sequence is correct: it is local at the bad prime \(p\), and does not supply a filtration preserved by a chosen Frobenius at a distinct prime \(\ell\). The proposed conditional cyclic-basis criterion is elementary once its hypotheses are supplied: if \(X\otimes\mathbf Z_q\) is free rank one over the relevant Hecke algebra \(R\), \(T_qJ\) is free rank two over \(R\), and Frobenius has an \(R\)-cyclic vector and characteristic polynomial \(t^2-T_\ell t+\ell\), then a cyclic basis gives the companion action and the desired module isomorphism. Here \(q\ne\ell\). The from-memory Mazur citation does not prove those freeness/cyclicity hypotheses at every prime away from \(n\); the new cell explicitly shows why such an inference is false. No unconditional freeness claim is promoted by this review.

## P4: the adelic comparison and its limits

The quaternion double-coset identity is valid in the corrected P2 sense. The identity \(\mathbf Q^\times\backslash\mathbb A_f^\times/\widehat{\mathbf Z}^\times=\{1\}\) is also exact: cancel the finitely many valuations of an idele with a positive rational number. The valuation lattice \(\mathbf Q_\ell^\times/\mathbf Z_\ell^\times\cong\mathbf Z\), with edges between consecutive integers, is a line. Calling it “the tree of \(\mathbf G_m\)” requires specifying this valuation/extended-building convention; the reduced building of a torus is a point.

The unit shift quotient has one vertex and one ordinary loop pair. Its Hashimoto operator is the \(2\times2\) identity, so \(\det(1-uH)=(1-u)^2\), independently checked above. Removing the vertex Eisenstein plane leaves no nontrivial label modes. However the loop graph itself has \(H_1\cong\mathbf Z\): “genus zero, no finite-rank H¹” must not be read as a statement about its ordinary graph cohomology. Nor does a trivial class set prove a general nonexistence theorem for cohomological realizations of the Riemann zeta function. The conclusion about what an analogue for zeta might require remains HEURISTIC, as requested by the task.

The local \(T_\ell(E)\) at one supersingular vertex and the global \(X\oplus X\) have different roles and generally different ranks. The quotient construction relates them through the vertex set; it supplies no canonical equality of the two lattices or their pairings. The rational one-operator comparison and the integral counterexample at \((37,7,3)\) are sound after the P3 repairs. At \(q\mid n\), non-isometry of the specified graph form and the principal Weil pairing is proved even in cells where the unpaired Frobenius modules agree.

## Candidate-row adjudications

Each proposed row is adjudicated separately; the sections above provide its derivation and independent numerical evidence.

| Candidate alias | Restated claim | Decision and required change |
|---|---|---|
| `thm:pizer-ihara-zeta-x0p` | The Brandt quadratic determinant is the Eisenstein factor times the curve numerator, and its cuspidal spectrum is Ramanujan by Weil. | VALID. The identity and all 20 polynomial cells stand; “graph” means the weighted Brandt operator when stabilizers are nontrivial. The erroneous displayed Weil form and point-count transcription are subsidiary corrections to P1. |
| `lem:ihara-bass-half-loops` | Inverted edges alter the ordinary Bass factor by the specified powers, and trace-zero norm-ℓ elements count Pizer half-loops. | MINOR. State the regular arc-involution hypotheses and restrict the formula `#elements/2` to `w_i=1`; the determinant derivation and exponents themselves are correct. |
| `prop:pizer-tree-quotient` | One maximal order's localized units give the whole tree quotient for all p, with identified colors. | MINOR. For general p use the edge-indexed quotient/graph of groups, and fix the left/right Hom convention. |
| `prop:pizer-label-space-h1` | The nontrivial label companion is the curve's rational Frobenius system. | MINOR. Compare over `Q_q`, explicitly as a noncanonical one-operator system, and supply the missing strict-endpoint/semisimplicity argument. |
| `num:pizer-label-lattice-smith` | Forty-eight exact cokernel computations distinguish the graph from the elliptic product at ℓ=5,7 and from the Jacobian at (ℓ,q)=(7,3). | MINOR. Every invariant factor is correct; replace the false ordinarity assertion and certify the degree-four isogeny as above. Use Tate-module language for the rigorous prime-to-ℓ conclusions. |
| `prop:pizer-omega-monodromy` | The specified graph form is the skew doubling of monodromy and has determinant `n²=|Φ_p|²`, obstructing a principal pairing. | VALID with the existing `p≡1 mod12` context retained. The proof above derives the pairing from the two-component dual graph; it gives no automatic Frobenius-compatible integral identification. |
| `conj:pizer-lattice-away-from-eisenstein` | The unpaired Frobenius lattices agree exactly away from the primes dividing `(p−1)/12`. | INVALID. Necessity already fails at `(37,2,3)` and `(37,5,3)`; sufficiency fails at the independent cell `(37,139,2)`. Replace OPEN with REFUTED. |

## Proposed record annotations and correction ledger

No record page is edited. The following are decisions on the submitted proposals, with concrete replacement wording where required.

| Destination/proposal | Adjudication | Wording to use |
|---|---|---|
| `graph-ihara.md` §§2–3 | AGREE-WITH-CHANGE | “For the Pizer family the Brandt identity is `det(1−Bu+ℓu²)=(1−u)(1−ℓu)P_{p,ℓ}(u)` (Eichler–Shimura). Its nontrivial companion is a rational Frobenius realization after extending coefficients to `Q_q`. When all vertex weights are one, dual-isogeny half-loops give `det(1−uH)=(1+u)^f(1−u²)^((N−f)/2−n)det(1−Bu+ℓu²)`.” Use the corrected Weil form for the chosen companion convention. |
| `graph-ihara.md` §9, Ihara–Bass row | AGREE | Add the reference to `lem:ihara-bass-half-loops` for inverted edges, with that lemma's explicit hypotheses. |
| `data-ladder.md` §0, new Pizer rung | AGREE-WITH-CHANGE | “For `p≡1 mod12`, the Pizer lattice is `X⊕X`, where `X` is the character lattice of the toric reduction at p. Its companion step has the good-prime Frobenius polynomial; its alternating form is the skew doubling of monodromy, with discriminant `n²`. It can differ integrally from the Jacobian and the elliptic product, e.g. `(37,7,3)`; such differences are not confined to primes dividing n.” The arithmetic-polarization column should not identify this nonprincipal form with the Jacobian's principal Weil pairing. |
| `data-ladder.md` §1.2 | AGREE-WITH-CHANGE | “The Pizer graph supplies a particular integral Hecke module and companion Frobenius lattice. At `(p,ℓ,q)=(37,7,3)` its rational-point cokernel differs from the Jacobian's; at `(37,139,2)` it also differs away from the component-group primes. Pairing discriminants and unpaired Frobenius-module classes are distinct data.” |
| `04z_cerednik_drinfeld.tex` header | AGREE | The two-vertex dual graph for `X_0(p)` gives an elementary counterpart of the doubled-monodromy determinant obstruction in genera 2,5,8; retain the distinction between the local toric filtration and good-prime Frobenius. |

The seven numbered correction-ledger entries in the submitted proof are also adjudicated:

1. **Half-loops: AGREE-WITH-CHANGE.** Apply the correction to the stated dual-isogeny arc convention with trivial projective vertex stabilizers. The ordinary Bass formula remains valid for ordinary loop pairs; weighted graphs of groups need a separate formula.
2. **Symmetrization: AGREE.** Use `W^(−1/2)BW^(1/2)` on functions and transpose consistently on divisors.
3. **Mass, model and labels: AGREE-WITH-CHANGE.** The mass and all tabulated weights/genus counts are correct for the tested primes. The explicit quotient transformations verify the named elliptic targets. A finite list of matching numerators is a consistency check, not a proof that an arbitrary genus-two model is `X_0(37)`; retain the stated literature input. Correct the `(109,7)` curve count to 10.
4. **No class-number-one restriction: AGREE-WITH-CHANGE.** The vertex quotient works for every class number; distinguish ordinary graphs from edge-indexed graphs at unequal weights and fix the left-ideal convention.
5. **Rational versus integral label comparison: AGREE-WITH-CHANGE.** Say “a noncanonical rational one-Frobenius realization; not an integral identification in general.” Do not assert failure at every good prime. The specified direct sum with the trivial plane has index `n²`.
6. **Tate-module completion: AGREE-WITH-CHANGE.** The universal integral identification is refuted at `(37,7,3)`, and again at `(37,139,2)`; use a coefficient prime distinct from the residue characteristic. The comparison is true at other cells, including `(37,2,3)` and `(37,5,3)`.
7. **Environment and division polynomials: AGREE-WITH-CHANGE.** The reruns work without `elldata`, and computing `Φ_ℓ` over `Z` avoids the specialization limitation. Replace “the division polynomial is not a product of kernel polynomials” by “its irreducible factors need not themselves be whole kernel polynomials.” The division polynomial always factors into the cyclic-subgroup kernel polynomials over a suitable field; those kernel polynomials can themselves split. Grouping torsion points is a valid implementation, not a theorem that no alternative exists.

## Verdict lines

VERDICT P1: MINOR — the determinant theorem holds after correcting the displayed Weil form and the misprinted (109,7) point count.
VERDICT P2: MINOR — retain edge indices at nontrivial stabilizers and use a consistent left-ideal convention.
VERDICT P3a: VALID — all 48 Smith forms and Hecke-derived orders are independently reproduced on the correctly defined saturated lattice.
VERDICT P3b: MINOR — both lattice refutations survive the explicit degree-four isogeny and prime-to-characteristic Tate-module repair.
VERDICT P3c: MINOR — the monodromy obstruction holds but it does not imply the proposed criterion for unpaired Frobenius lattices.
VERDICT P4: MINOR — the G_m conclusion concerns absent nontrivial label modes rather than vanishing graph H¹ or a nonexistence theorem for zeta.
VERDICT half-loop-lemma: VALID — the stated arc involution gives exactly the exponents f and (N−f)/2−n.
VERDICT thm:pizer-ihara-zeta-x0p: VALID — the Brandt determinant and weighted Ramanujan spectrum follow from the stated theorems and match all 20 cells.
VERDICT lem:ihara-bass-half-loops: MINOR — add regular arc-involution hypotheses and restrict the trace-zero count divided by two to unit weights.
VERDICT prop:pizer-tree-quotient: MINOR — the all-p quotient is edge-indexed when projective vertex stabilizers are nontrivial.
VERDICT prop:pizer-label-space-h1: MINOR — formulate a Q_q one-operator isomorphism and supply the missing endpoint exclusion.
VERDICT num:pizer-label-lattice-smith: MINOR — the numerical groups are correct but the Jacobian comparison requires the repaired isogeny and Tate arguments.
VERDICT prop:pizer-omega-monodromy: VALID — the unweighted two-component dual graph gives the stated doubled pairing and discriminant n².
VERDICT conj:pizer-lattice-away-from-eisenstein: INVALID — printed cells refute necessity and the independent (37,139,2) cell refutes sufficiency.
VERDICT P1-ramanujan: VALID — Weil bounds the nontrivial Brandt spectrum and all printed cells satisfy independently certified strict bounds.
VERDICT P1-weighted-zeta: UNVERIFIED — no weighted edge operator or complete determinant formula is specified.
VERDICT P1-numerics: MINOR — all saved numbers reproduce but the prose misstates the correct value #X₀(109)(F₇)=10.
VERDICT P2-local: VALID — kernel superlattices have the asserted index and the induced Weil-pairing similitude factor is ℓ.
VERDICT P2-quaternion: MINOR — every matrix and half-loop count reproduces but 1369 is the absolute trace determinant and the signed determinant is −1369.
VERDICT P3-rational: MINOR — symmetry alone does not imply companion semisimplicity and the repaired comparison is over Q_q.
VERDICT P3c-obstruction: VALID — det Ω₀=n² obstructs isometry with a principal intersection lattice for n>1.
VERDICT P3c-monodromy: VALID — the cycle group and edge-thickness pairing give the stated identification from the standard semistable model.
VERDICT P3c-cyclic-criterion: VALID — the conditional isomorphism follows from a cyclic basis under the explicitly stated freeness hypotheses.
VERDICT P3c-freeness: UNVERIFIED — the from-memory citation does not establish the claimed freeness and cyclicity hypotheses at the relevant maximal ideals.
VERDICT P4-integral-negative: MINOR — the counterexample is correct after replacing the remembered gluing assertion by the explicit degree-four isogeny.

## Agreement with the astra proof

This directory was first read **after the 25 verdict lines had been written**, as required. Its `astra-proofs.md` contains both completion sections. The comparison is not a substitute for a cross-family review of that proof.

* The two proofs and this review agree on the weighted Brandt normalization, half-loop exponents, one-order tree quotient, all shared Smith forms, doubled monodromy obstruction, explicit degree-four elliptic splitting, and the actual Jacobian discrepancy at `(37,7,3)`.
* The astra proof explicitly handles the companion endpoint issue using a recalled Coleman–Edixhoven regularity theorem; this review supplied a filtered-crystalline derivation and independently certified strictness in every printed cell. Its direct Jacobian calculation gives the cyclic group of order 48 over `F_5`, agreeing with this review's independent 2-torsion/cyclic-module argument.
* It additionally constructs the unimodular reduction `L_red=e^⊥/Ze`, `e=(1,1)`, an index-n overlattice of `L_0`. Its success at `(37,7,3)` does not answer the general integral question. The new `(37,139,2)` obstruction in this review also applies to that reduction, since its index 3 is a unit at 2. The astra proof leaves the general polarized identification open; it does not assert Fable's false “iff” conjecture.
* The comparison prompted two further convention checks, recorded explicitly rather than folded into the blind provenance. First, the signed quaternion trace determinant is −1369, independently checked in `independent_conventions.py`; the subsidiary `P2-quaternion` verdict is MINOR for this label. Second, the companion-compatible edge labeling is `τf−σg`, whose kernel on the trivial plane is `(1,1)`: indeed `Hσ=ℓτ` and `Hτ=τB−σ`, so `H(τf−σg)=τ(Bf−ℓg)−σf`. Fable's stated kernel `(1,−1)` is correct for its written `σf+τg` map, but that map belongs to the older companion convention. This does not alter `L_0` or its Smith forms.

## Numerical checks for the blind lane

Run from the repository root. The original scripts have been rerun, using the specified venv, from byte-identical copies under `checks/rerun/` because two of them overwrite adjacent output files. `output_audit_artifacts.txt` certifies exact source and saved-output matches for all three. Independent scripts use different bases, libraries, arithmetic implementations, or counting formulas as explained above.

```bash
PY=/tmp/claude-1000/-home-tobias-Projects-riemann-channel/dcae8e10-414e-4cb4-8b95-d35e159cfb50/scratchpad/venv-astra/bin/python
D=notes/astra-2026-10-27/pizer/review-astra-of-fable/checks
PYTHONDONTWRITEBYTECODE=1 "$PY" "$D/rerun/pizer_graph.py" > "$D/rerun/stdout_pizer_graph.txt"
PYTHONDONTWRITEBYTECODE=1 "$PY" "$D/rerun/pizer_quotient.py" > "$D/rerun/stdout_pizer_quotient.txt"
PYTHONDONTWRITEBYTECODE=1 "$PY" "$D/rerun/label_lattice.py" > "$D/rerun/stdout_label_lattice.txt"
python3 "$D/independent_theta.py" > "$D/output_independent_theta.txt"
PYTHONDONTWRITEBYTECODE=1 "$PY" "$D/independent_arithmetic.py" > "$D/output_independent_arithmetic.txt"
PYTHONDONTWRITEBYTECODE=1 "$PY" "$D/independent_matrices.py" > "$D/output_independent_matrices.txt"
python3 "$D/independent_conventions.py" > "$D/output_independent_conventions.txt"
python3 "$D/audit_artifacts.py" > "$D/output_audit_artifacts.txt"
```

Six compact certificates:

1. **Quaternion matrices and half-loops:** the theta computation gives `B_37(2)=[[1,1,1],[1,0,2],[1,2,0]]` before relabeling, and `f_2,f_3,f_5,f_7=1,0,2,0`. One permutation `(1,2,0)` matches all four supplied modular-polynomial matrices. The trace Gram determinant is −1369, with reduced discriminant 37.
2. **Bass exponents:** `(p,ℓ)=(37,2)` has `(N,f,m−n)=(9,1,1)`; `(73,7)` has `(48,2,17)`; `(109,7)` has `(72,0,27)`. All twelve determinant polynomials agree by independent walk traces. A single half-loop gives determinant 1 and tests the negative exponent −1.
3. **Direct genus-two counts:** over `F_5,F_25` the counts are 8 and 42, giving `P=1+2u+10u²+10u³+25u⁴`; over `F_139,F_(139²)` they are 140 and 19846, giving `P=1+262u²+19321u⁴` and Jacobian order 19584.
4. **The actual-Jacobian obstruction at 7:** graph `[9,9]`, elliptic product `[3,3,9]`, and degree-four quotient maps prove that the latter is the actual Jacobian group. All sixteen elliptic-product groups were independently enumerated, and all 48 graph Smith forms were recomputed using PARI in a different lattice basis.
5. **The conjecture fails at a divisor of n:** at `(37,2,3)` the Frobenius discriminant is 2048, a 3-adic unit; at `(37,5,3)` it is 128000, also a 3-adic unit. Finite étaleness proves module agreement, despite `3|n`. The extra `(37,11,3)` check gives discriminant 329584640 and graph group `[153]`.
6. **The conjecture fails away from n:** at `(37,139,2)` theta series give `B=[[48,44,48],[44,48,48],[48,48,44]]` and graph group `[4,4896]`. The six rational branch roots `35,37,49,90,102,104` give `J[2]=(Z/2)^4`, whereas the graph has 2-torsion rank two. This comparison uses the actual Jacobian, not the isogenous elliptic product.

The auxiliary `search_endpoints.py` was an exploratory search, stopped after the completed prime 643 once a general derivation was available. Its partial output is preserved for provenance, and no verdict relies on completing that search. The main matrix script's exact endpoint certificates cover every requested cell. All final independent certificate scripts completed successfully; no network, git operation, or record-page edit was used.

## What this changes in the notebook

The cross-family review supports the Brandt/curve determinant theorem, the explicitly defined half-loop determinant, the corrected arithmetic tree quotient, the rational one-Frobenius comparison, all printed Smith forms, and the doubled-monodromy obstruction. It supplies the explicit degree-four isogeny needed to validate the claimed Jacobian discrepancy at `(37,7,3)`. The weighted Bass-zeta formula and the blanket applicability of the recalled freeness statement remain UNVERIFIED, with the missing hypotheses identified above.

The material change is that `conj:pizer-lattice-away-from-eisenstein` must be recorded as **REFUTED**, not OPEN: both implications fail. Retain the distinction between a pairing's discriminant and the isomorphism class of an unpaired Frobenius lattice. The next useful integral statement should impose actual cyclicity/local-order hypotheses or compute the specific arithmetic lattice, rather than classify discrepancies solely by the component-group order. The proposed annotation decisions and exact replacement wording are recorded above; nothing has been registered or edited outside this review directory.
