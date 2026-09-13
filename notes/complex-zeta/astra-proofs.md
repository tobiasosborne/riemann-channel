# Geodesic determinants, cochain torsion, and quantum twists of complexes

Author: codex:gpt-6-astra.

This author line applies to every definition, proof, correction, and computation below. Date: 2026-09-13. Only this file is an output of this work. No web access was used. External inputs are the supplied extracts and the locally available TeX at their citation addresses. `proved-here` means proved in this note, not independently refereed. An external theorem used in a proof is explicitly an H-hypothesis; its use is not a claim to have reproved it.

The answer requires distinguishing three objects: the ordered-cell flow of the question, the pointed/opposition flow of a building, and the edge-only Kang–Li zeta. They are not equal. There is a natural graded determinant construction on **specified geodesic data**. There is an unconditional Schur identity for the ordered-cell data. There is a much stronger cohomological/Hecke identity for building data. Neither a single-circle RH nor a universal cubic vertex formula follows merely from having a simplicial complex.

Throughout, $H_k=\mathbb C^{\Omega_k}$, $\dim H_k=(k+1)!f_k$, and $H_k=0$ outside $0\leq k\leq d$. Operators on basis vectors act forwards; a cited operator on functions is transposed when needed. Scalar determinants are unchanged by this transpose. Write $s_k=(-1)^{k+1}$. All determinant identities are in $\mathbb C(u)$, or in its formal expansion at zero. Orders of zeros are positive; orders of poles are negative. In building statements put $n=d+1$; this avoids the question's reuse of $d$ for both dimension and the index of $\mathrm{PGL}_d$.

## T0. The definition and the necessary change of geodesic data

**Definition T0.1 (ordered-cell geodesic data).** For an arbitrary finite abstract simplicial complex define
$$
T_k[ v_0,\ldots,v_k ]=
\sum_{\substack{w\notin\{v_0,\ldots,v_k\}\\
\{v_1,\ldots,v_k,w\}\in X\\
\{v_0,\ldots,v_k,w\}\notin X}}
[ v_1,\ldots,v_k,w ],\qquad 1\leq k\leq d.
$$
Define
$$
Z_k^{\rm ord}(u)=\det_{H_k}(I-uT_k)^{-1},\quad
Z_k^{\epsilon,\rm ord}(u)=\det_{H_k}(I-s_kuT_k)^{-1},\quad
\mathcal Z_{\rm ord}(X,u)=\prod_{k=1}^d\det_{H_k}(I-s_kuT_k)^{(-1)^k}.
$$
For $d=0$ the product is $1$.

Status: **proved-here** (well-defined construction).

<1>1. Every target tuple consists of distinct vertices and is an ordered $k$-cell.

PROOF. These are exactly the first two conditions in the sum.

<1>2. If $d=1$, $T_1$ is Hashimoto's matrix and $\mathcal Z_{\rm ord}=Z_1^{\rm ord}$ is Ihara's zeta, with directed primitive cycles modulo cyclic rotation, not modulo reversal.

PROOF. There are no 2-cells, and the excluded vertex is precisely the immediately previous vertex. The determinant/Euler-product proof is given in T5.1 with one-dimensional identity weights.

<1>3. If $d=2$, $T_1$ excludes turns across a filled triangle. At $k=d$ it shifts to any other top simplex sharing the specified ordered codimension-one face.

PROOF. The last exclusion is automatic in top degree; all the other exclusions remain. In particular “top-cell non-backtracking” retains the ordered overlap, rather than meaning an arbitrary walk on the dual graph.

**Hypothesis H-POINT (building successor conventions).** On an oriented affine diagram of type $\widetilde A_{n-1}$, a pointed $k$-facet has a unique cyclically increasing ordering starting at its distinguished vertex. Its ordered type is a positive composition $(\lambda_0,\ldots,\lambda_k)$ of $n$. Its algebraic step length is $\lambda_0$. Successors shift the ordering and cross to an **opposite vertex in the spherical link** of the common $(k-1)$-facet. Their type is $(\lambda_1,\ldots,\lambda_{k-1},\lambda_0,\lambda_k)$. These are the source's definitions, including incidence multiplicities on a quotient: `2607.21262:main.tex:439-474`, `:479-534`, `:608-615`, `:1811-1846`, `:2235-2260`.

**Definition T0.2 (pointed/opposition building data).** Under H-POINT let $P_k$ be the set of pointed $k$-facets, so $|P_k|=(k+1)f_k$. Let
$$
\mathscr T_k(u)[\sigma]=u^{\lambda_0(\sigma)}
\sum_{\tau\in\operatorname{Succ}(\sigma)}[\tau],\qquad
\mathcal Z_{\rm pt}(X,u)=\prod_{k=1}^{n-1}
\det_{\mathbb C^{P_k}}(I-s_k\mathscr T_k(u))^{(-1)^k}.
$$
The cyclic orientation/type-difference structure and link opposition are part of the data. For quotients that identify vertices of a simplex, use the source's $\Delta$-complex with incidences, not its underlying abstract vertex-set complex. Hereafter building assertions about an abstract complex assume that no such identifications have occurred. A global type function is sufficient; a descended cyclic type-difference structure also specifies the local operators, but does not by itself enlarge the hypotheses of an external theorem.

Status: **conditional-on H-POINT** for identification with the source; the finite determinant definition itself is **proved-here**.

<1>1. This has the precise sign and length conventions of Kang–Yu.

PROOF. The sign on a path of $r$ successor steps is $s_k^r$, whereas its power of $u$ is the sum of the $r$ algebraic lengths. These are respectively $\epsilon(\gamma)$ and $l_A(\gamma)$ in `2607.21262:main.tex:1971-1981`, `:2304-2312` (included in H-KY below).

<1>2. The difference from T0.1 is not a factorial multiplicity correction.

PROOF. There are $k!$ times as many ordered states, but most arbitrary orderings do not respect the cyclic diagram, and nonincidence is weaker than opposition. A dimension ratio alone does not give invariant copies of an operator.

**Hypothesis H-LLP.** LLP's $UT^j$ consists of pointed facets with consecutive colours $c,c+1,\ldots,c+j$, and its successor must also have these consecutive colours and must not extend to a cell. Its Ramanujan result concerns equivariant, collision-free, $b$-regular branching operators: nontrivial eigenvalues satisfy $|\lambda|\leq\sqrt b$, and peripheral ones have $|\lambda|=b$. Interior spectral radii do occur (poles with $0<|\operatorname{Re}s|<1/2$). Addresses: `1702.05452:rw_ramanujan_complex.tex:999-1027`, `:216`, `:229` (branching operators), `:330-336` (definition of a Ramanujan digraph), `:410-416` (the RH corollary), `:487`, `:922-923` (the proved eigenvalue bound), `:1390-1424`. The source's printed $|s|=1$ in its exponential parametrization is not a well-defined invariant of the periodic parameter $s$; T6.4 uses the eigenvalue statement.

**Proposition T0.3 (exact comparison in rank three).** Suppose $X$ is a simplicial, type-preserving, torsion-free finite quotient of the $\mathrm{PGL}_3$ building with residue order $q$. Put $N=q^2+q+1$. Under H-POINT, H-LLP, and H-KL below:

1. The colour-1 restriction of the appropriately restricted edge successor relation is $L_E$; the colour-2 relation is conjugate by edge reversal to $L_E^t$.
2. $\mathscr T_1(u)=uL_E\oplus u^2L_E^t$ on $2f_1$ pointed edges. Thus
   $$D_E(u):=\det(I-\mathscr T_1(u))=
   \det(I-uL_E)\det(I-u^2L_E^t).$$
3. $\mathscr T_2(u)=uL_B$ on $3f_2$ cyclically ordered pointed chambers, and $D_B(u):=\det(I+uL_B)$.
4. The **unrestricted** $T_1$ of T0.1 is not this block sum, even after replacing $u^2$ by $u$. Its outdegree is $2q^2+q$, whereas $L_E$ has outdegree $q^2$.
5. The unrestricted $T_2$ has two invariant cyclic orientations, each of dimension $3f_2$, and the two blocks are reversal-transposes. Consequently
   $$\det_{H_2}(I+uT_2)=D_B(u)^2.$$

Status: **conditional-on H-POINT, H-LLP, H-KL** for source identifications; the combinatorial discrepancies are **proved-here** from the stated building link incidence data.

<1>1. A vertex link is the incidence graph of the projective plane of order $q$. It has $N$ vertices in each part, and each vertex has $q+1$ neighbours.

PROOF. This is the rank-three instance of the subspace/link model in H-POINT. Counting lines in a 3-dimensional vector space gives $(q^3-1)/(q-1)=N$ and $q+1$ lines in a plane.

<1>2. At an edge $(x,y)$, the ordered rule allows $N-1$ endpoints in the same part of $\operatorname{Lk}(y)$ as $x$, and $N-(q+1)=q^2$ in the other part.

PROOF. Same-part vertices never form a triangle with $x,y$; opposite-part vertices do exactly when they are incident to $x$. Exclude $x$ itself in the first count. The total is $2q^2+q$. In particular, there are transitions which change directed edge colour. The colour classes are not invariant blocks of the unrestricted operator.

<1>3. Link opposition keeps just the $q^2$ nonincident opposite-part choices. Reversal exchanges the two directed edge colours and reverses a successor path.

PROOF. Opposition for a point and a line in this link means nonincidence. A forward colour-1 edge has algebraic length 1; its reversal has length 2. This proves statements 1–2, including why the exponent $u^2$ is a **length**, not a second copy or a square of the matrix.

<1>4. In a chamber successor $(v_0,v_1,v_2)\mapsto(v_1,v_2,w)$, $w$ has the colour of $v_0$. The increasing and decreasing cyclic orders are each preserved.

PROOF. Every chamber has all three colours. Reversing a tuple reverses the direction of a gallery, giving transpose-conjugacy between the two orientation blocks. Only the increasing block is used by Kang–Yu/Kang–Li. This accounts for the $6f_2$ versus $3f_2$ dimensions and proves statement 5.

**Hypothesis H-KL (rank-three identity and RH).** For the torsion-free, cocompact, type-preserving quotients in C1, with regularity of the lattice removed by Kang–Li–Wang, let
$$P_3(u)=I-A_1u+qA_2u^2-q^3u^3I.$$
Then
$$
Z_{\rm KL}(u)=D_E(u)^{-1}
=\frac{(1-u^3)^{\chi(X)}}{\det P_3(u)\,D_B(u)},\qquad
\frac{D_B(u)}{D_E(u)}=\frac{(1-u^3)^{\chi(X)}}{\det P_3(u)}.
$$
The four-way equivalence with Ramanujan has nontrivial radii $q^{-1}$ for $P_3$, $q^{-1},q^{-1/2}$ for $L_E$, and $1,q^{-1/2},q^{-1/4}$ for $L_B$. Addresses: `0804.2305:main.tex:215-260`, `0809.1401v1:main.tex:218-221`, `:244-247`, `:342-368`, `:1352-1370`, `:1410-1418`. The $L$-function normalization is `1505.00902:Zeta-and-Lfunction-20170426.tex:1134-1161`. No statement here extends these hypotheses to an arbitrary local imitation of a building.

**Corollary T0.4 (which zeta reduces to which).**
$$
\boxed{\quad\mathcal Z_{\rm pt}=D_B/D_E
=(1-u^3)^\chi L_{\rm vertex},\qquad
Z_{\rm KL}=1/D_E,\qquad L_{\rm vertex}=1/\det P_3.\quad}
$$
Thus even after repairing states and lengths, the proposed **total** zeta is the completed vertex $L$-function, not Kang–Li's edge-only zeta. With the unmodified ordered operators it is neither.

Status: **conditional-on H-KL**; the claim that all three zetas agree is **FALSE-as-drafted**.

<1>1. Substitute $s_1=1$, $s_2=-1$ in T0.2.

PROOF. This gives $D_B/D_E$, and H-KL gives the other expressions. There is no further sign choice that removes $D_B$ while retaining a nonzero odd chamber sector.

**Proposition T0.5 (general-rank comparison).** LLP's $j$-flow is the restriction of the pointed building flow to types $(1,\ldots,1,n-j)$, with $j$ initial ones and unit algebraic length. It is not the unrestricted ordered flow. The latter is not a direct sum of $k!$ Kang–Yu flows.

Status: **conditional-on H-POINT, H-LLP** for the positive identification; the claimed unrestricted identification is **FALSE-as-drafted**.

<1>1. Consecutive colours give exactly the displayed composition, preserved by the successor rule of H-POINT.

PROOF. In the relevant link factor, the two endpoints have complementary line/hyperplane types. Their nonincidence is opposition, matching H-LLP's extra exclusion. This checks the transition relation as well as the states.

<1>2. Nonincidence alone is insufficient outside these types.

PROOF. In the subspace link of a vertex of an $\widetilde A_3$ building, the two planes $\langle e_1,e_2\rangle$ and $\langle e_1,e_3\rangle$ in $\mathbb F_2^4$ are incomparable, hence not joined by a link edge, but are not complementary. The unrestricted edge rule permits this turn; opposition does not. Already rank three fails by T0.3, so no factorial-copy identification holds in general.

## T1. What the torsion identity actually says

**Theorem T1.1 (finite cochain determinant cancellation).** Let $(C^\bullet,d)$ be any bounded finite-dimensional cochain complex over $K=\mathbb C(u)$. Let $h:C^i\to C^{i-1}$ be any degree $-1$ map, let $c\in K^\times$, and assume each
$$F_i=cI+d_{i-1}h_i+h_{i+1}d_i$$
is invertible. Then
$$
\prod_i\det(F_i|C^i)^{(-1)^i}
=\prod_i\det(F_i|H^i(C))^{(-1)^i}
=c^{\sum_i(-1)^i\dim C^i}.
$$
Neither $h^2=0$ nor $h=d^*$ is required.

Status: **proved-here**.

<1>1. $F$ commutes with $d$ and induces $cI$ on cohomology.

PROOF. Expand $d(dh+hd)=(dh+hd)d=dhd$, using $d^2=0$. On a cocycle, $(dh+hd)x=dhx$ is a coboundary.

<1>2. Put $B^i=\operatorname{im}d_{i-1}$, $Z^i=\ker d_i$. Choose bases adapted to $B^i\subset Z^i\subset C^i$.

PROOF. The determinant of $F_i$ factors into those on $B^i$, $H^i=Z^i/B^i$, and $C^i/Z^i$. The last quotient is equivariantly isomorphic via $d_i$ to $B^{i+1}$. The boundary factors cancel between adjacent degrees. This proves the first equality.

<1>3. The remaining determinant on $H^i$ is $c^{\dim H^i}$, and $\sum(-1)^i\dim H^i=\sum(-1)^i\dim C^i$.

PROOF. Apply the same dimension decomposition to $B^i\subset Z^i\subset C^i$. This proves the second equality.

**Proposition T1.2 (ordered, pointed, and ordinary Euler numbers differ).** T1.1 gives the following exponents when $c=1-u^{d+1}$:

| Space in degree $i$ | Dimension | Exponent in T1.1 |
|---|---:|---:|
| ordinary oriented simplicial cochains | $f_i$ | $\chi(X)$ |
| all ordered cells with deletion differential | $(i+1)!f_i$ | $\chi_{\rm ord}=\sum_i(-1)^i(i+1)!f_i$ |
| Kang–Yu pointed cochains | $(i+1)f_i$ | $\chi_{\rm pt}=\sum_i(-1)^i(i+1)f_i$ |

The pointed differential is the source's deformed differential, not ordinary simplicial cohomology. The draft's identification of its alternating determinant with $c^\chi$ is incorrect.

Status: **proved-here**, with the identification of the third complex **conditional-on H-KY**.

<1>1. All three exponents follow directly from the dimensions in T1.1.

PROOF. In the ordered case the alternating deletion differential squares to zero by the usual pairwise cancellation of two deletions. This does not quotient by permutation signs.

<1>2. The smallest nonzero-dimensional counterexample to the ordered exponent is one edge $\Delta^1$.

PROOF. It has $(f_0,f_1)=(2,1)$, hence $\chi=1$ but $\chi_{\rm ord}=2-2=0$. Any cochain automorphism chain-homotopic to $cI$ on this ordered complex has alternating determinant $1$, not $1-u^2$. For $\Delta^2$, $\chi=1$, $\chi_{\rm ord}=3-6+6=3$, and the pointed dimension sum is $3-6+3=0$. Purity does not fix the problem.

<1>3. The draft's unrestricted existential wording, without a chain-homotopy or flow-compatibility requirement, is not an impossibility claim that these examples can refute.

PROOF. On ordinary cochains take $F_i=cI$. Even on $H_i$ let
$$\Pi_i=\frac1{(i+1)!}\sum_{\sigma\in S_{i+1}}\operatorname{sgn}(\sigma)\,\sigma$$
be antisymmetrization. It is a canonical rank-$f_i$ projection. Then $\det(I-u^{d+1}\Pi_i)=c^{f_i}$ and its alternating product is $c^\chi$. If “built from face maps” excludes all permutation operations, a precise allowed algebra would have to be specified before that literal existential assertion has content. This artificial construction does not identify any flow determinant. In particular it cannot rescue T2.

**Hypothesis H-KY (pointed cohomological identity).** For a torsion-free cocompact **type-preserving** quotient of the $\mathrm{PGL}_n$ building, the pointed cochains have a differential $d(u)$, a degree $-1$ map $\delta(u)$, and
$$\Phi_i=(1-u^n)I+d_{i-1}\delta_i+\delta_{i+1}d_i.$$
They satisfy
$$
\det\Phi_0=\det P_n(u),\qquad
P_n(u)=\sum_{j=0}^n(-1)^j q^{j(j-1)/2}u^j A_j,\quad A_0=A_n=I,
$$
$$
\det\Phi_i=(1-u^n)^{if_i}\det(I-s_i\mathscr T_i(u))\quad(i\geq1).
$$
Addresses: `2607.21262:main.tex:2014-2026`, `:2175-2203`, `:2320-2438`, `:2459-2487`. Its determinant/Euler-product assertion is `:1971-1981`, `:2304-2312`. This source contains **no general-rank RH theorem**.

**Theorem T1.3 (the ordinary Euler factor is a difference of two weighted sums).** Under H-KY,
$$
\prod_{i=0}^{n-1}\det\Phi_i^{(-1)^i}=(1-u^n)^{\chi_{\rm pt}},\qquad
\mathcal Z_{\rm pt}(X,u)=\frac{(1-u^n)^{\chi(X)}}{\det P_n(u)}.
$$

Status: **conditional-on H-KY**, with the cancellation **proved-here**.

<1>1. Apply T1.1 to $C^i=\mathbb C(u)^{P_i}$ and $c=1-u^n$.

PROOF. H-KY gives exactly the required chain homotopy and invertibility over $\mathbb C(u)$.

<1>2. Substitute the individual H-KY determinant factors.

PROOF. The left side becomes
$$\det P_n\,c^{\sum_{i\geq1}(-1)^iif_i}\,\mathcal Z_{\rm pt}.$$
Subtract this exponent from $\chi_{\rm pt}$. The result is $\sum_i(-1)^if_i=\chi(X)$, giving the formula. The bare cochain superdeterminant has the weighted exponent; the final flow/vertex comparison has the ordinary exponent.

**Proposition T1.4 (torsion terminology and the special-value limitation).** The cancellation above is a finite determinant-line/torsion calculation. It is not a statement that Knill's analytic torsion is literally $\lim_{u\to1}(1-u^n)^\chi$, or literally $\lim_{u\to1}\mathcal Z$.

Status: **proved-here** for the distinction; the literature identifications are **conditional-on H-TORS**.

<1>1. Ordinary cochains with $h=d^*$ give a concrete version of T1.1, but its alternating determinant still reduces to $c^\chi$.

PROOF. All nonzero Laplacian eigenvalues cancel in unweighted adjacent degrees. To obtain analytic torsion one instead uses degree-weighted pseudodeterminants, removing zero eigenvalues and retaining metric information.

<1>2. A single edge is already a separating example.

PROOF. Its Ihara zeta is $1$, while $d_0^*d_0$ has nonzero eigenvalue $2$, so Knill's squared analytic torsion for this graph is $2$. The limit of the displayed trivial factor $1-u^2$ is $0$. These are three different quantities.

**Hypothesis H-TORS.** Hoffman reformulates Bass through torsion of complexes (`2607.21262:main.tex:351-366`). Knill's $D_i$ in $\mathrm{SDet}(D)=\prod_i\mathrm{Det}(D_i)^{(-1)^i}$ is $d_i^*d_i$, and $\mathrm{Det}$ is a **pseudodeterminant**, with the stated even/odd tree interpretation (`2201.09412:reidemeister.tex:42-52`, `:545-556`). Hashimoto's $h'_X(1)=-2\chi(X)\kappa(X)$ concerns the **vertex determinant** $h_X$, not the Euler factor (`2310.15619:main.tex:950-955`). These facts explain the relationship without identifying different torsions or unrenormalized limits.

## T2. The general Bass identity and the failure of cubic collapse

**Definition T2.1 (three elementary incidence operators).** For $k\geq1$ define
$$
R_k:H_k\to H_{k-1},\quad R_k[v_0,\ldots,v_k]=[v_1,\ldots,v_k],
$$
$$
S_k:H_{k-1}\to H_k,\quad S_k[v_1,\ldots,v_k]
=\sum_{\{v_1,\ldots,v_k,w\}\in X}[v_1,\ldots,v_k,w],
$$
where the appended vertex is distinct, and define cyclic rotation
$$C_k[v_0,\ldots,v_k]=[v_1,\ldots,v_k,v_0].$$
Set $S_{d+1}=R_{d+1}=0$ and
$$F_k=C_k+R_{k+1}S_{k+1},\qquad K_k(z)=I+zF_k.$$
The letter $C_k$ here denotes a rotation operator, not a cochain space.

Status: **proved-here** (definition).

**Theorem T2.2 (universal ordered-cell Bass–Schur identity).** For every finite abstract simplicial complex, every $1\leq k\leq d$, and indeterminate $z$,
$$
\boxed{\quad T_k=S_kR_k-F_k,\qquad
\det_{H_k}(I-zT_k)=
\det_{H_k}K_k(z)\,
\det_{H_{k-1}}\bigl(I-zR_kK_k(z)^{-1}S_k\bigr).\quad}
$$
This is an explicit rational compression by one dimension, not a degree-$(d+1)$ polynomial on vertices. Define $M_k(z)=I-zR_kK_k(z)^{-1}S_k$. In dimension two the total identity is
$$
\boxed{\quad
\mathcal Z_{\rm ord}(X,u)=
\frac{\det_{H_2}K_2(-u)\,\det_{H_1}M_2(-u)}
{\det_{H_1}K_1(u)\,\det_{H_0}M_1(u)}.\quad}
$$
It explicitly retains vertices and ordered edges, and the upper-cell cyclic factor. Calling $M_1$ a “vertex determinant” is valid only if its rational dependence on the full forbidden-transition matrix is stated.

Status: **proved-here**.

<1>1. $S_kR_k$ sums over all successors with the prescribed ordered overlap.

PROOF. Delete the first vertex, then append any vertex giving a $k$-simplex. The disallowed possibility $w=v_0$ is exactly $C_k$.

<1>2. All other disallowed successors are exactly $R_{k+1}S_{k+1}$.

PROOF. Such a successor has distinct new vertex $w$ and the union is a $(k+1)$-simplex. First append $w$ to that larger simplex, then delete $v_0$. This is a bijection of summands, with multiplicity one for an abstract complex. The two forbidden classes are disjoint.

<1>3. Factor $I-zT_k=K_k-zS_kR_k$ and apply Sylvester's identity.

PROOF. Since $K_k(0)=I$, it is invertible over $\mathbb C(z)$. Factoring $K_k$ gives
$$\det K_k\det(I-zK_k^{-1}S_kR_k)=\det K_k\det(I-zR_kK_k^{-1}S_k).$$
Equality as rational functions also prescribes the cancellations at singular values of $K_k$.

<1>4. Substitute $z=u$ in degree 1 and $z=-u$ in degree 2.

PROOF. T0.1 is the ratio of the degree-2 determinant to the degree-1 determinant. This gives the stated placements.

**Corollary T2.3 (Bass for every graph).** If $d=1$ then
$$\det(I-uT_1)=(1-u^2)^{f_1-f_0}
\det_{H_0}\bigl(I-uA+u^2(\operatorname{Deg}-I)\bigr).$$
No regularity assumption is needed.

Status: **proved-here**.

<1>1. $F_1=C_1=J$ is edge reversal, $J^2=I$, and $\det(I+uJ)=(1-u^2)^{f_1}$.

PROOF. Each unoriented edge contributes the $2\times2$ block $\left(\begin{smallmatrix}1&u\\u&1\end{smallmatrix}\right)$.

<1>2. $R_1S_1=A$ and $R_1JS_1=\operatorname{Deg}$.

PROOF. An extension from a vertex followed by suffix deletion ends at its neighbour; with reversal inserted it ends back at that vertex, once per neighbour.

<1>3. $M_1(u)=(I-uA+u^2(\operatorname{Deg}-I))/(1-u^2)$.

PROOF. Use $(I+uJ)^{-1}=(I-uJ)/(1-u^2)$ in T2.2. Its vertex determinant contributes $(1-u^2)^{-f_0}$. Isolated vertices and trees are included by rational cancellation.

**Proposition T2.4 (smallest 2-dimensional obstruction).** On the boundary $X=\partial\Delta^3$ of a tetrahedron,
$$
(f_0,f_1,f_2)=(4,6,4),\quad\chi=2,\quad
T_1=0,\quad\det(I+uT_2)=(1-u^4)^6,\quad
\mathcal Z_{\rm ord}=(1-u^4)^6.
$$
There is **no matrix polynomial of any size or degree** $P(u)$ satisfying
$$\mathcal Z_{\rm ord}(X,u)=(1-u^3)^{\chi(X)}/\det P(u).$$
In particular the proposed cubic matrix with arbitrary $Q_1,Q_2$ fails, even if those coefficients may use global data.

Status: **FALSE-as-drafted; corrected statement proved-here**.

<1>1. Every turn through three distinct vertices closes a 2-simplex, so $T_1=0$.

PROOF. Every 3-element subset of the four vertices is a face.

<1>2. From an ordered triangle there is exactly one allowed new vertex, the missing fourth vertex. The operation rotates the ordered four-vertex sequence.

PROOF. It is a permutation of the 24 ordered triangles in six cycles of length 4. A cycle of length $r$ has $\det(I+uP_r)=1-(-u)^r$, hence the asserted sixth power.

<1>3. The proposed identity would force $\det P(u)=(1-u^3)^2/(1-u^4)^6$.

PROOF. This has a pole at $u=-1$ (also at $u=\pm i$), so is not a polynomial. No freedom in local counts can repair this contradiction.

<1>4. Four is the smallest vertex count for this obstruction among 2-complexes.

PROOF. The only 2-complex on three vertices is the filled triangle. Both its flow operators vanish, and the necessary scalar determinant $1-u^3$ is a polynomial; it does not give this pole obstruction. This is a minimality claim for the exhibited obstruction, not a classification of every possible prescribed-coefficient failure on three vertices.

**Proposition T2.5 (what is, and is not, characterized).** The vertex Hecke polynomial under H-KY is
$$P_n(u)=\sum_{j=0}^n(-1)^j q^{\binom j2}A_j u^j.$$
For $\widetilde A_2$, $Q_1=qA_2$, $Q_2=q^3I$, and the linear coefficient is $-A_1$, **not** minus the undirected adjacency $A=A_1+A_2$. The known sufficient class here is the class in H-KY/H-KL. Equality of numerical link parameters, or the phrase “links are generalized polygons,” is not a proved characterization of that class or of cubic collapse.

Status: **conditional-on H-KY, H-KL** for the building identity; a proposed local-link characterization is **sketched/unestablished**, not used as a theorem.

<1>1. The coefficients follow from the subspace-lattice Möbius function $\mu(j)=(-1)^jq^{j(j-1)/2}$ in H-KY.

PROOF. For $j=1,2,3$ these are $-1,q,-q^3$. Building colours separate $A_1$ from $A_2$. For example at an edge the $q^2$ allowed opposition continuations differ from the unrestricted count in T0.3, so a Schur complement for the latter cannot prove the former identity.

<1>2. A link-parameter condition alone supplies neither a specified cyclic type structure nor an identified Bruhat–Tits universal cover.

PROOF. The supplied theorems assume such a cover and use subspace-lattice incidence/opposition identities, not just vertex valencies and girths. Even a theorem that a universal cover is some affine building would require an additional argument identifying the Hecke/cochain data needed here. No such recognition theorem is assumed or proved in this note. Conversely, accidental determinant identities do not imply that links are buildings.

<1>3. There is an exact **algebraic** criterion, but not a combinatorial classification, for the proposed collapse for a specified complex.

PROOF. Form the explicitly computable rational function
$$B_X(u)=(1-u^{d+1})^{\chi(X)}/\mathcal Z_{\rm ord}(X,u).$$
A proposed polynomial matrix $I-uA+\sum_{j=2}^{d+1}u^jQ_{j-1}$ works exactly when its determinant equals $B_X$. Necessary conditions are that $B_X$ is polynomial of degree at most $(d+1)f_0$ and has the coefficient constraints imposed by $A$ (for example $[u]\det=-\operatorname{Tr}A$). Polynomiality alone is not asserted sufficient with a prescribed $A$ and prescribed local construction. T2.4 violates the first condition. The universal replacement is T2.2, without an unproved “if and only if locally building” assertion.

## T3. Supertrace, zeros, and the limits of the cohomology dictionary

**Theorem T3.1 (the exact graded identity).** On
$$W_+=\bigoplus_{k\text{ odd}}H_k,\qquad
W_-=\bigoplus_{k\text{ even},\ k\geq2}H_k,\qquad
\Tau=\bigoplus_{k=1}^d s_kT_k,$$
we have
$$
\mathcal Z_{\rm ord}(X,u)=\operatorname{sdet}_W(I-u\Tau)^{-1},\qquad
\log\mathcal Z_{\rm ord}=\sum_{m\geq1}\frac{u^m}{m}\operatorname{str}(\Tau^m)
=\sum_{m\geq1}\frac{u^m}{m}\sum_k s_k^{m+1}\operatorname{Tr}(T_k^m).
$$
If $u_0\ne0$, its order is the odd algebraic multiplicity minus the even algebraic multiplicity of $u_0^{-1}$ in $\Tau$. Eigenvalues zero produce no finite zero or pole. Common even/odd factors cancel.

Status: **proved-here**; “zeros are exactly the odd eigenvalues” is **FALSE-as-drafted** without reciprocal, sign, multiplicity, and cancellation qualifications.

<1>1. The parity of degree $k$ is $k+1\pmod2$, so its contribution to the inverse superdeterminant is $\det(I-s_kuT_k)^{-s_k}=\det(I-s_kuT_k)^{(-1)^k}$.

PROOF. This is the definition of $\operatorname{sdet}$ and T0.1.

<1>2. Expand each logarithmic determinant near $u=0$.

PROOF. $\log\det(I-uM)=-\sum_{m\geq1}\operatorname{Tr}(M^m)u^m/m$. Multiplying the parity signs gives $s_k^{m+1}$. For chambers the contribution is $(-1)^{m+1}\operatorname{Tr}(T_2^m)$, not a constant minus sign applied to the unsigned flow at every length.

<1>3. Read the divisor from the characteristic factors.

PROOF. A Jordan block of size $r$ with eigenvalue $\lambda$ contributes $(1-u\lambda)^r$ to the determinant, regardless of its nilpotent part. Taking the ratio subtracts coincident multiplicities.

**Proposition T3.2 (algebraic lengths require a polynomial transfer or a delay space).** For pointed building data replace $u\Tau$ by the even polynomial operator $\mathscr A(u)=\bigoplus_k s_k\mathscr T_k(u)$ on parity $k+1$. Then
$$\mathcal Z_{\rm pt}=\operatorname{sdet}(I-\mathscr A(u))^{-1},\qquad
\log\mathcal Z_{\rm pt}=\sum_{r\geq1}\operatorname{str}(\mathscr A(u)^r)/r.$$
A constant transfer matrix linear in $u$ exists after adding delay states, with the **same parity** as their original facet. The sign $s_k$ is inserted once per successor arrow, not at every delay tick.

Status: **proved-here**.

<1>1. Give a state $\sigma$ of algebraic length $\ell(\sigma)$ a chain of $\ell(\sigma)$ states $(\sigma,0),\ldots,(\sigma,\ell-1)$.

PROOF. Move deterministically along this chain with weight 1, then from its last state to $(\tau,0)$ with weight $s_k$ for each original successor $\tau$. Assign all these states parity $k+1$.

<1>2. Eliminate the delay coordinates in $I-u\widetilde\Tau$.

PROOF. Their strictly advancing blocks have determinant 1. The resulting transition from the retained original coordinate to a successor is $s_ku^{\ell(\sigma)}$. Thus the resulting determinant is $\det(I-s_k\mathscr T_k(u))$. Equivalently, each cyclic path has its original sign and total algebraic length. A sign at every delay tick would give the wrong colour-2 edge convention.

**Proposition T3.3 (vertex-relative parity and cancellation).** Under H-KL,
$$L_{\rm vertex}(u)=\frac{D_B(u)}{(1-u^3)^\chi D_E(u)}=\frac1{\det P_3(u)}.$$
In the **factorized expression**, the chamber determinant is a numerator and the edge determinants are denominators. The reduced vertex $L$-function itself has no finite zeros. Thus it is incorrect to call all zeros of $D_B$ uncancelled zeros of $L_{\rm vertex}$.

Status: **conditional-on H-KL**; the uncancelled-zero reading is **FALSE-as-drafted**.

<1>1. The equality is T0.4 divided by $(1-u^3)^\chi$.

PROOF. Its final expression is a reciprocal polynomial. Every finite zero visible in the intermediate numerator cancels against an edge or Euler factor, including multiplicities. The phrase “odd chamber sector” accurately describes the virtual determinant presentation; it does not override this divisor calculation.

**Proposition T3.4 (the cohomology dictionary is parity only).** The assignment $k\leftrightarrow i=k-1$ matches the exponents in the displayed Grothendieck–Lefschetz convention
$$\prod_i\det(I-uF|H^i)^{(-1)^{i+1}},$$
but does not identify the spaces $H_k$ or $\mathbb C^{P_k}$ with cohomology groups of $X$, and does not assign them Weil weight $k-1$.

Status: **proved-here** for the parity comparison; a literal cohomological/weight identification is **FALSE-as-drafted**. The displayed Lefschetz convention is the formal comparison specified in the question, not an additional theorem about $X$.

<1>1. Substitution $i=k-1$ gives exponent $(-1)^k$.

PROOF. This is exactly the determinant exponent in T0.1/T0.2.

<1>2. A graph cycle already disproves a literal space identification.

PROOF. The three-cycle has six ordered-edge states but only one-dimensional ordinary $H^0$. Its Ihara determinant remembers the two directed cycles. The word “$H^0$ only” can describe the absence of an odd **flow** sector, not the ordinary cohomology of a graph; the graph also has nonzero $H^1$.

<1>3. Chamber radii are not those of a single pure weight.

PROOF. The following precise source decomposition supplies three different nontrivial radii. No parity reindexing makes these equal.

**Hypothesis H-KL-TABLE (representation constituents).** The unitary Iwahori-spherical types, their fixed-space dimensions, and their determinant roots are those in `0809.1401v1:main.tex:391-424`, `:1132-1154`, `:1171-1209`. The Steinberg multiplicity statement is `:1183-1186`. The identity's representation-wise contributions and conjugate-pair cancellation are `:1425-1461`. Only the rows explicitly used below are assumed; no numerical value from the non-tempered type-(d) root row is needed.

**Proposition T3.5 (what supplies the three chamber circles).** Write $\alpha_i=\chi_i(\varpi)$ and $\eta=\chi(\varpi)$. On a Ramanujan quotient, the relevant rows of H-KL-TABLE are:

| Constituent | Chamber roots of $D_B$ | Edge roots of $\det(I-uL_E)$ | Vertex roots |
|---|---|---|---|
| tempered unramified principal series (a), $|\alpha_i|=1$, $\prod\alpha_i=1$ | $\pm q^{-1/2}\alpha_i^{-1/2}$, $i=1,2,3$ | $q^{-1}\alpha_i^{-1}$ | the same three |
| one-dimensional (b), $\eta^3=1$ | $-q^{-1}\eta^{-2}$ | $q^{-2}\eta^{-1}$ | $\eta^{-1},q^{-1}\eta^{-1},q^{-2}\eta^{-1}$ |
| Steinberg twist (c), $\eta^3=1$ | $\eta^{-2}$ | none | none |
| tempered nonspherical type (e), $|\eta|=1$ | $q^{-1/2}\eta$, $\pm q^{-1/4}\eta^{-1/2}$ | $q^{-1/2}\eta^{-1}$ | none |

The signs on square roots denote the unordered pair and require no branch choice. Thus the circle $q^{-1/2}$ contains all principal-series chamber roots and one root from each type-(e) constituent. The circle $q^{-1/4}$ comes from the other two roots of type (e). The unit circle comes from Steinberg twists. The one-dimensional representations give **trivial** chamber roots on $q^{-1}$, outside the three listed nontrivial circles.

Status: **conditional-on H-KL-TABLE, H-KL**.

<1>1. Take absolute values in the four rows.

PROOF. The characters in those rows are unitary, so only the stated powers of $q$ survive. The non-tempered spherical constituents are excluded by H-KL's Ramanujan condition.

<1>2. “Weight 1” for the $q^{-1/2}$ chamber roots means only an analogy of inverse spectral radii with a curve's weight-1 Frobenius eigenvalues.

PROOF. A full type-(e) constituent contributes to two circles simultaneously. Extracting its single $q^{-1/2}$ root is a spectral factorization, not a canonical simplicial cohomology group. Steinberg twists have no vertex-fixed vectors and account, together with the one-dimensional rows, for the Euler correction in the source. Their unit radii are not evidence that they are ordinary $H^0(X)$; nor do the $q^{-1/4}$ roots form a curve's $H^2$. There is no honest complete curve-weight dictionary here.

<1>3. The global scalar identity is not an identical scalar equality on every irreducible constituent with the same Euler power.

PROOF. H-KL-TABLE gives the type-(e) contribution to $\det P_3D_B/D_E$ as
$$\frac{1-q^{1/2}\eta^{-1}u}{1-q^{1/2}\eta u}.$$
This need not be 1. It cancels against the conjugate constituent in the untwisted global determinant. Consequently “the proof uses irreducibles” is not permission to restrict an arbitrary scalar determinant identity to a chosen constituent. T5 distinguishes matrix identities from such scalar cancellations.

**Proposition T3.6 (Euler factor versus vanishing order).** Under H-KY, at $u_0^n=1$,
$$\operatorname{ord}_{u_0}\mathcal Z_{\rm pt}=\chi(X)-\operatorname{ord}_{u_0}\det P_n.$$
There is no universal ordinary or degree-weighted Betti-number formula for the order of $\mathcal Z_{\rm ord}$ at these points. On a connected type-preserving rank-three Ramanujan quotient with the three one-dimensional constituents of H-KL-TABLE and $q>1$, this order is $\chi(X)-1$ at each cube root of unity.

Status: **conditional-on H-KY** (and **H-KL-TABLE, H-KL** for the last specialization); the general no-formula implication from T1 alone is **proved-here**.

<1>1. The zeros of $1-u^n$ are simple in characteristic zero.

PROOF. Differentiate: $-nu_0^{n-1}\ne0$. T1.3 gives the order difference.

<1>2. In the rank-three specialization exactly one trivial vertex root equals a specified cube root of unity, and all other vertex roots have modulus below 1.

PROOF. Use the three type-(b) rows and the Ramanujan principal-series row in T3.5. This gives order one for the vertex determinant at each such point.

<1>3. For $\Delta^2$, $\mathcal Z_{\rm ord}=1$ despite $\chi=1$; for $\partial\Delta^3$ its order at $u=1$ is 6 despite $\chi=2$ and $b_1=0$.

PROOF. Use T2.4 and T7's direct filled-triangle calculation. Neither the ordinary Euler number nor the degree-weighted Betti sum agrees with these orders uniformly.

**Hypothesis H-RUELLE.** Deitmar's exterior-power product is `dg-ga/9511006:main.tex:1153-1168`; his order is $-\sum_pp(-1)^p\dim H^p$ with a vanishing ordinary Euler sum, in its stated locally symmetric/coefficient-module setting (`:1194-1212`). For oriented negatively curved surfaces, Dyatlov–Zworski give $\zeta_R=\zeta_1/(\zeta_0\zeta_2)$ and order $-\chi$ (`1606.04560:zazi.tex:68-77`, `:843-855`).

**Proposition T3.7 (the Ruelle comparison has a restricted meaning).** The parallel with H-RUELLE is alternating determinant structure. Deitmar's insertion of degree $p$ and his specific coefficient cohomology are additional structures; they are not T3.1's plain flow supertrace. A formula for one of these orders cannot be imported into the other.

Status: **conditional-on H-RUELLE** for the cited comparisons; **proved-here** for the distinction.

<1>1. The trace insertion in T3.1 is parity, while Deitmar's order inserts degree times parity.

PROOF. Compare $\sum(-1)^i\operatorname{Tr}$ with $\sum i(-1)^i\dim$. T1.3 also shows explicitly where a different weighted dimension sum enters and then cancels. No equality between these different insertions is available.

## T4. Dirac-type constructions: a true block theorem and a false chirality claim

**Theorem T4.1 (one explicit incidence matrix with two Schur evaluations).** On $H_{k-1}\oplus H_k\oplus H_{k+1}$ define
$$
\mathbb D_k(z)=
\begin{pmatrix}
I&-R_k&0\\
-zS_k&I+zC_k&zR_{k+1}\\
0&-S_{k+1}&I
\end{pmatrix}.
$$
Zero-dimensional outer spaces are omitted. Then
$$\det\mathbb D_k(z)=\det_{H_k}(I-zT_k)
=\det K_k(z)\det_{H_{k-1}}M_k(z).$$
All off-diagonal couplings are face/coface maps between adjacent dimensions; $I+zC_k$ is a dimension-preserving mass/rotation term. For $k=1,d=2$ this is a single matrix on vertices, ordered edges, and ordered triangles.

Status: **proved-here**.

<1>1. Eliminate the last identity block.

PROOF. The middle block becomes $I+zC_k+zR_{k+1}S_{k+1}=K_k(z)$. The remaining two-by-two block is
$$\begin{pmatrix}I&-R_k\\-zS_k&K_k(z)\end{pmatrix}.$$

<1>2. Eliminate the first block or the middle block, respectively.

PROOF. The first choice gives $K_k-zS_kR_k=I-zT_k$. The second gives $\det K_k\det(I-zR_kK_k^{-1}S_k)$. These are the two claimed evaluations of the same determinant, including signs.

<1>3. Alternatively, for $k=1,d=2$, eliminate the edge mass $K^0=I+uC_1$ first. One obtains the honest vertex/triangle determinant
$$
\det(I-uT_1)=\det_{H_1}K^0\det_{H_0\oplus H_2}
\begin{pmatrix}
I-uR_1(K^0)^{-1}S_1&uR_1(K^0)^{-1}R_2\\
-uS_2(K^0)^{-1}S_1&I+uS_2(K^0)^{-1}R_2
\end{pmatrix}.
$$
PROOF. This is the block Schur complement with the edge block placed last. In the untwisted case $\det K^0=(1-u^2)^{f_1}$. Triangles survive as a coupled block. When there are no triangles the block disappears and T2.3 is recovered.

**Theorem T4.2 (the total object needs a ratio/Berezinian).** Give the whole auxiliary space of $\mathbb D_k(s_ku)$ parity $k+1$, and put
$$\mathbb D_{\rm flow}(u)=\bigoplus_{k=1}^d\mathbb D_k(s_ku).$$
Then
$$\operatorname{sdet}\mathbb D_{\rm flow}(u)=\mathcal Z_{\rm ord}(X,u)^{-1}.$$
This construction uses separate auxiliary copies of some cell spaces. It does not give each geometric cell a unique parity determined solely by its dimension across every copy.

Status: **proved-here**; the proposed universal **ordinary** fermion determinant with flow parity equal to cell chirality is **FALSE-as-drafted**.

<1>1. Apply T4.1 in every degree.

PROOF. The exponent in the superdeterminant is $s_k$, so its reciprocal is exactly the product with exponents $(-1)^k$ in T0.1.

<1>2. Ordinary Grassmann integration gives $\det D$, not a reciprocal determinant or a superdeterminant merely because $D$ has chiral blocks.

PROOF. Fix the Berezin integration convention for which $\int\exp(-\bar\psi D\psi)\,D\bar\psi D\psi=\det D$. Expansion picks each Grassmann coordinate once; the resulting permutation sum is the ordinary determinant. A ratio requires separate numerator/denominator sectors, or a super-Gaussian with commuting variables as well, interpreted formally when convergence is absent.

<1>3. A polynomial ordinary determinant cannot realize the proposed universal ratio, even allowing an Euler factor $(1-u^3)^a$ with any integer $a$ and a polynomial vertex factor.

PROOF. On $\partial\Delta^3$, $\mathcal Z_{\rm ord}^{-1}=(1-u^4)^{-6}$. The Euler factor cannot remove its poles at $u=\pm i$. If an arbitrarily chosen vertex polynomial is allowed to cancel those poles by fiat, one has abandoned the prescribed building vertex formula and gained a vacuous determinant realization, not the claimed incidence theorem. T2.4 already proves the prescribed collapse impossible. Rational matrices can of course be manufactured; that is not a polynomial fermion construction on one copy of the ordered cells.

<1>4. Chirality and flow superparity are distinct gradings.

PROOF. Within one $\mathbb D_k$, ordinary dimension parity makes its off-diagonal part odd. But the determinant of that matrix uses all its coordinates as fermions; it has no parity exponent. T4.2 assigns the entire auxiliary realization the parity of the retained flow sector. A geometric $(k-1)$-cell used as an auxiliary variable there therefore has a different parity from the same cell used as its own flow state in $\mathbb D_{k-1}$. No identity above equates these gradings.

**Hypothesis H-MO.** The graph construction of Matsuura–Ohta has a block off-diagonal Dirac part, a reversal mass term, and two ordinary determinant evaluations giving Bass and Hashimoto. Its fields on both vertices and edges are Grassmann fields. Addresses: `2501.08803:main.tex:630-648`, `:700-707`, `:750-755`, `:811-826`. The stated gamma-five hermiticity is `:192`. This is not a claim that their ordinary determinant is already a Berezinian with vertex/edge Grassmann parities reversed.

**Proposition T4.3 (relation to the graph fermion proof).** T4.1 in dimension one has the same incidence/reversal Schur mechanism as H-MO. Its exponent $f_1-f_0$ is the reversal-pair contribution minus the vertex denominator contribution. It is not literally $\dim H_1-\dim H_0=2f_1-f_0$.

Status: **proved-here** for the exponent; the literature comparison is **conditional-on H-MO**.

<1>1. Each two-dimensional reversal block has determinant $1-u^2$, not $(1-u^2)^2$.

PROOF. This is T2.3. The vertex compression contributes $(1-u^2)^{-f_0}$. Thus even the graph “index-like” description needs the reversal pairing; raw block dimensions alone give the wrong number.

**Definition T4.4 (an explicit building cochain linearization).** Under H-KY use its lattice notation: a pointed $r$-facet is $[a_0,\ldots,a_r]$, extended by $a_{j+r+1}=\varpi a_j$, and $[a:b]=\dim_\kappa(a/b)$. Put $\mu(t)=(-1)^tq^{t(t-1)/2}$. The actual degree-changing maps are
$$
(d_if)[a_0,\ldots,a_{i+1}]
=u^{[a_0:a_1]}f[a_1,\ldots,a_{i+1}]
+\sum_{j=1}^{i+1}(-1)^jf[a_0,\ldots,\widehat a_j,\ldots,a_{i+1}],
$$
$$
(\mathcal R_if)[a(0,i-1)]
=(-1)^i\sum_{a_0\supsetneq b\supsetneq a_1}
 u^{[a_0:b]}\mu([a_0:b])f[b,a(1,i)],
$$
$$
(\delta_if)[a(0,i-1)]
=\sum_{j=0}^{i-1}(-1)^{(i+1)j}u^{[a_0:a_j]}
(\mathcal R_if)[a(j,j+i-1)].
$$
The periodic convention in the latter two formulas is for the $(i-1)$-facet, so $a_{j+i}=\varpi a_j$. Maps outside their degrees are zero. These are H-KY's explicit maps, not the unsigned $R_i,S_i$ of T2.

Let $C=\bigoplus_i\mathbb C(u)^{P_i}$ with ordinary cochain parity $i$, let $C[1]$ denote parity reversal, and $c=1-u^n$. On $C\oplus C[1]\oplus C[1]$ define the even block operator
$$
\mathbb B(u)=
\begin{pmatrix}
cI&d&\delta\\
-\delta&I&0\\
-d&0&I
\end{pmatrix}.
$$
“Even” holds because $d,\delta$ change the original cochain parity and the auxiliary spaces have their parity reversed.

Status: **conditional-on H-KY** for these building maps; the block construction is **proved-here**.

**Theorem T4.5 (building torsion as a Berezinian, with its exact limitation).**
$$
\operatorname{sdet}\mathbb B
=\operatorname{sdet}_C(cI+d\delta+\delta d)
=c^{\chi_{\rm pt}}
=\det P_n\,c^{\sum_{i\geq1}(-1)^iif_i}\,\mathcal Z_{\rm pt}.
$$
This gives an explicit cochain construction and the completed vertex identity. The passage from the individual $\Phi_i$ to the successor factors uses H-KY's local Möbius-inversion determinant theorem. It is **not** obtained for arbitrary complexes simply by relabeling T4.1's Schur blocks as Hecke operators.

Status: **conditional-on H-KY**, with the Schur and torsion parts **proved-here**.

<1>1. Eliminate the two auxiliary identity blocks in the category of even graded maps.

PROOF. Their Berezinians equal 1 and the remaining operator is $cI+d\delta+\delta d$, block diagonal in cochain degree with blocks $\Phi_i$.

<1>2. Apply T1.1 and then the individual H-KY determinant identities.

PROOF. The two evaluations are respectively $c^{\chi_{\rm pt}}$ and the last product displayed above. The cancellation in T1.3 produces the ordinary Euler exponent.

<1>3. This is not the square of $d+\delta$ in general, and no self-adjoint/gamma-five property is proved here.

PROOF. H-KY explicitly allows $\delta^2\ne0$ (`2607.21262:main.tex:2377-2378`). Thus $(d+\delta)^2=d\delta+\delta d+\delta^2$, which has an extra degree-$-2$ term. The doubled linearization avoids that error. H-MO's stronger graph structure cannot be imported without a separate construction.

## T5. Kraus weights, local systems, and Artin blocks

**Definition T5.1 (the full-complex twist).** Let $V$ be a finite-dimensional complex space and give each directed edge an arbitrary $E_{(x,y)}\in\operatorname{End}(V)$. On $H_k^V=V\otimes H_k$ use the **last vertex** as fibre anchor and set
$$T_k^E(v\otimes[\sigma])=
\sum_{\sigma\to\tau,\ \sigma=(v_0,\ldots,v_k),\ \tau=(v_1,\ldots,v_k,w)}
E_{(v_k,w)}v\otimes[\tau].$$
For pointed data use its successor relation and its algebraic power $u^{\lambda_0(\sigma)}$. The full twisted graded zeta is the determinant product of T0 with these fibre spaces and operators. A connection in the linear-algebra sense here need not be a flat local system.

Status: **proved-here** (definition).

**Theorem T5.2 (arbitrary weights preserve the universal Schur identity).** Keep $R_k$ as deletion tensored with $I_V$. Replace $S_k$ by
$$S_k^E(v\otimes[v_1,\ldots,v_k])=
\sum_w E_{(v_k,w)}v\otimes[v_1,\ldots,v_k,w],$$
and rotation by
$$C_k^E(v\otimes[v_0,\ldots,v_k])=
E_{(v_k,v_0)}v\otimes[v_1,\ldots,v_k,v_0].$$
Then, without any positivity, pairing, invertibility, or flatness assumption,
$$F_k^E=C_k^E+R_{k+1}S_{k+1}^E,\quad
T_k^E=S_k^ER_k-F_k^E,$$
$$
\det_{H_k^V}(I-zT_k^E)=
\det_{H_k^V}(I+zF_k^E)
\det_{H_{k-1}^V}\bigl(I-zR_k(I+zF_k^E)^{-1}S_k^E\bigr).
$$
The matrix of T4.1 with $S,C$ replaced by $S^E,C^E$ proves the same two evaluations. Any other specified successor rule with this overlap also admits this Schur construction by defining $F$ to be the sum of its forbidden weighted transitions; only the particularly simple $C+RS$ formula uses T0.1's rule.

Status: **proved-here**.

<1>1. Each unrestricted, cyclic, or upper-simplex transition carries exactly the appended-edge weight $E_{(v_k,w)}$.

PROOF. In the upper-simplex term the weight is inserted by $S_{k+1}^E$ and $R_{k+1}$ inserts none. The same term-by-term cancellation as T2.2 therefore holds without commuting any weights.

<1>2. Repeat the factorization and Schur proof of T2.2/T4.1 over the named fibre spaces.

PROOF. $I+zF_k^E$ is invertible at $z=0$, so all operations are valid over $\mathbb C(z)$. No inverse of an $E$ is taken.

<1>3. In graphs, inverse pairing gives $\det(I+uC_1^E)=(1-u^2)^{(\dim V)f_1}$ and the usual polynomial Bass compression with the covariant adjacency and scalar degrees.

PROOF. Each reversal pair has determinant $\det_V(I-u^2E_{(y,x)}E_{(x,y)})$. If the product is $I$, the inverse is the scalar-denominator matrix used in T2.3. For arbitrary weights the pair factor is instead exactly this operator determinant, as in Theorem 1 of `notes/quantum-ihara-general.md`. In dimensions above one, inverse pairing alone does not remove the upper-face term $R_{k+1}S_{k+1}^E$.

**Theorem T5.3 (trace formula, primitive product, and positivity).** For every $m\geq1$,
$$
\operatorname{Tr}(T_k^E)^m=
\sum_{\substack{\sigma_0\to\sigma_1\to\cdots\to\sigma_m=\sigma_0}}
\operatorname{Tr}_V(E_m\cdots E_1).
$$
This sum is over based closed walks in the state digraph, with all step multiplicities; it is not directly a sum over primitive unoriented geodesics. For $V=M_N$ and $E_e=\operatorname{Ad}(B_e)$,
$$\operatorname{Tr}(T_k^E)^m=
\sum_{\text{based closed walks}}|\operatorname{Tr}(B_m\cdots B_1)|^2\geq0.$$
Adjoint pairing is **not needed**. More generally each $E_e$ may be a completely positive sum of Kraus maps, giving a further sum over Kraus labels. For the unsigned factor,
$$Z_k^E(u)=\prod_{[\gamma]\text{ primitive}}
\det_V(I-u^{|\gamma|}E_\gamma)^{-1}.$$
For the signed factor replace $E_\gamma$ by $s_k^{|\gamma|}E_\gamma$; for pointed data replace $|\gamma|$ in the power of $u$ by its algebraic length, while retaining the number of successor steps in the sign.

Status: **proved-here**; the claim that positivity requires adjoint pairing is **FALSE-as-drafted**.

<1>1. Expand the matrix power by its intermediate state indices.

PROOF. Induction gives the chronological composition $E_m\cdots E_1$ for each walk. The trace in the state basis sets the last state equal to the first; the remaining trace is on $V$.

<1>2. For $\operatorname{Ad}(B)$, the matrix trace on $M_N$ is $|\operatorname{Tr}B|^2$, and compositions satisfy $\operatorname{Ad}(B)\operatorname{Ad}(A)=\operatorname{Ad}(BA)$.

PROOF. With column vectorization, the matrix is $\overline B\otimes B$. Tensor-product traces and multiplication prove both statements. For multiple Kraus operators expand by linearity. Reversal is irrelevant to this calculation.

<1>3. Group closed words by repetitions of primitive cyclic words in the logarithmic trace expansion.

PROOF. A primitive word of length $\ell$ repeated $r$ times contributes $\operatorname{Tr}(E_\gamma^r)u^{r\ell}/r$, since its $\ell$ possible based representatives cancel the $\ell$ in $m=r\ell$. Summing over $r$ gives $-\log\det(I-u^\ell E_\gamma)$. Cyclic reanchoring gives the same determinant by repeated Sylvester identities, even when the weights are singular. All statements are formal near zero, hence also determine the rational function.

**Proposition T5.4 (what the positive-ring no-go actually proves).** A single finite transfer matrix contributes a reciprocal polynomial, so it cannot have a nonconstant **reduced** numerator. In this finite-transfer model the numerator of the graded zeta comes from net odd multiplicity between sectors, not from an unsigned individual Kraus flow. Positivity of the numerical ring sequence by itself is a weaker assertion and does not exclude a rational numerator.

Status: **proved-here**; an unrestricted “nonnegative coefficients forbid a numerator” claim is **FALSE-as-drafted**.

<1>1. For a finite matrix $M$, $\exp\sum_m\operatorname{Tr}(M^m)u^m/m=1/\det(I-uM)$.

PROOF. The determinant expansion used above holds without diagonalizability. Its reduced numerator is constant. Equality with a rational function having a genuine zero is impossible.

<1>2. Positivity alone does not prove this conclusion.

PROOF. $(1-u)/(1-2u)$ has nonnegative Taylor coefficients and logarithmic coefficients $(2^m-1)/m>0$, but a reduced numerator. It cannot be the reciprocal determinant of a finite ordinary transfer matrix. This is the finite-dimensional scope in which the notebook's no-go is being used; no claim about every infinite positive system is needed.

**Proposition T5.5 (flatness, anchors, and the full-twist/Artin distinction).** The full-complex twist in T5.1 is not a representation-isotypic block of the untwisted complex.

Status: **FALSE-as-drafted; corrected statements proved-here**.

<1>1. A flat local system requires both invertible reversal $E_{yx}=E_{xy}^{-1}$ and the triangle relation $E_{yz}E_{xy}=E_{xz}$. The latter alone, for arbitrary singular linear maps, is not a rank-constant local system.

PROOF. Reversal must implement an isomorphism between fibres. These relations make transport unchanged by an elementary edge reversal or a triangle homotopy. Conversely the coefficient coboundary squares on a triangle to its curvature $E_{yz}E_{xy}-E_{xz}$, with the appropriate anchoring convention. Thus flatness is exactly what permits the usual cochain complex with these coefficients, but it is not needed in T5.2.

<1>2. With an invertible flat system, first-vertex and last-vertex anchoring are conjugate.

PROOF. Set $G_\sigma=E_{(v_0,v_k)}$ for $\sigma=(v_0,\ldots,v_k)$, and let the first-anchor step carry $E_{(v_0,v_1)}$. In a successor pair $\sigma,\tau$,
$$G_\tau E_{(v_0,v_1)}G_\sigma^{-1}=E_{(v_k,w)}.$$
For $k\geq2$, use flatness inside $\sigma$ and $\tau$ to factor through $v_1,v_k$; for $k=1$ it is immediate. Hence the two flow matrices are block-diagonally conjugate. Without flatness these are different legitimate weighted models, not interchangeable conventions.

<1>3. On a right Cayley graph, the stated forward weights $E_{(g,gs)}=\rho(s)$ are generally **not flat** under the question's chronological column convention.

PROOF. For a triangle $g,gs,gst$, flatness asks $\rho(t)\rho(s)=\rho(st)$; a representation instead gives $\rho(st)=\rho(s)\rho(t)$. Noncommuting images need not satisfy it, including for $\rho=\pi\otimes\overline\pi$. The covariant flat convention is $E_{(g,gs)}=\rho(s^{-1})$, or one may change the entire convention to pullback operators on functions.

<1>4. Those corrected covariant weights on the **full** Cayley complex are pure gauge.

PROOF. Put $F_g=\rho(g^{-1})$. Then $E_{(g,gs)}=F_{gs}F_g^{-1}$. At a last-anchor state use the fibre change $F_{v_k}$. This conjugates the twisted operator to $I_V\otimes T_k$, so
$$\det(I-uT_k^E)=\det(I-uT_k)^{\dim V}.$$
Closed full-complex paths have identity holonomy. The interesting Artin factor lives on a quotient with group voltages, not on this gauge-trivial full cover.

<1>5. A four-cycle is a concrete minimal clique-Cayley counterexample to the draft's block equality.

PROOF. Take $G=\mathbb Z/4$, $S=\{1,-1\}$, its one-dimensional clique complex, and any one-dimensional $\pi$. Then $\pi\otimes\overline\pi=1$, so the full twisted determinant is $(1-u^4)^2$. The trivial representation block of its two directed-flow orbits is $I_2$, with determinant $(1-u)^2$. They are different. The counterexample has no ordering ambiguity or nonflat weights.

**Theorem T5.6 (the correct finite-group Artin decomposition).** Let a finite group $G$ act on $X$ preserving the specified successor/length data and freely on the state sets under consideration. This holds for ordered and pointed states of a Cayley complex, because a fixed pointed/ordered state fixes its anchor vertex. Choose representatives $\sigma_a$ for the state orbits. Encode a transition $\sigma_a\to h\sigma_b$ by a voltage $h\in G$.

For an irreducible unitary $\rho$ of dimension $d_\rho$, define the quotient forward block $T_{k,\rho}$ by replacing this arrow by $\rho(h^{-1})$ on its fibre (and the same length weight). Then
$$
\det(I-s_k\mathscr T_k(u))=
\prod_{\rho\in\widehat G}\det(I-s_k\mathscr T_{k,\rho}(u))^{d_\rho}.
$$
In this forward Fourier convention the block is the multiplicity space of the left $\rho^\vee$-isotypic representation; relabeling duals gives the usual indexing. If $R=\pi\otimes\overline\pi=\bigoplus_\rho a_\rho\rho$, the **Artin determinant** is
$$D_{k,R}(u)=\prod_\rho\det(I-s_k\mathscr T_{k,\rho}(u))^{a_\rho},\qquad
\dim R=(\dim\pi)^2.$$
It need not be a single isotypic determinant. The full $\rho^\vee$-isotypic determinant has exponent $d_\rho$, not $a_\rho$ or 1. The dimension of $R$ may exceed the regular-representation multiplicity bounds.

Status: **proved-here**.

<1>1. Identify the state space with $\mathbb C[G]\otimes\mathbb C^{\{a\}}$ by $g\sigma_a\leftrightarrow(g,a)$.

PROOF. Freeness makes this a bijection, and equivariance makes each arrow act by $g\mapsto gh$ on the group coordinate.

<1>2. For a coefficient vector $x$, use the finite Fourier transform $\widehat x_a(\rho)=\sum_gx_{g,a}\rho(g^{-1})$.

PROOF. A transition $g\mapsto gh$ changes this to $\rho(h^{-1})\widehat x_a(\rho)$. Each of its $d_\rho$ columns carries the same block; left translation acts on the other matrix index by the dual representation. Finite Fourier decomposition is an isomorphism: matrix coefficients of inequivalent irreducibles are orthogonal by averaging intertwiners, each irreducible contributes $d_\rho^2$ dimensions, and their sum is $|G|$ (equivalently decompose the regular representation using its character, which is $|G|$ at the identity and zero otherwise). This proves the determinant multiplicities.

<1>3. Apply the same quotient construction to a direct sum of representations.

PROOF. Every voltage matrix is block diagonal under that decomposition. Determinants multiply with exponent $a_\rho$. In particular an arbitrary $R$ is not literally a subrepresentation of the regular representation: for $\pi=1\oplus1$, $R=1^{\oplus4}$ while the regular representation has only one trivial copy. What always transfers is spectral support.

<1>4. An equivariant **matrix** Schur identity restricts to all these blocks.

PROOF. Its factors and incidence maps preserve isotypic subspaces, and the same finite linear algebra applies to their multiplicity spaces. A scalar determinant equality alone does not imply such a restriction; T3.5 gives the warning in the building representation calculation.

**Hypothesis H-KY-LOCAL (the local algebra behind equivariant/twisted use).** The explicit maps of T4.4 and the source's operators
$$
(W_if)[a(0,i)]=f[a(0,i)]+s_i u^{[a_0:a_1]}f[a(1,i+1)],
\qquad
(Q_if)[a(0,i)]=\sum_{a_0\supseteq b\supsetneq a_1}u^{[a_0:b]}f[b,a(1,i)]
$$
have the factorization
$$\Phi_i=cW_i^{-1}J_i(I-s_i\Sigma_i)J_i^{-1}Q_i^{-1}.$$
Here $Q_i$ is unipotent in the ordered-type filtration, $J_i$ is cyclic rotation, and $\Sigma_i$ has the same weighted closed paths as $\mathscr T_i$; the additional intersection condition for successors is forced on a closed path by monotonicity of a link subspace dimension. Also $\Phi_0=P_n$ as an **operator**. Addresses: `2607.21262:main.tex:2516-2576`, `:2586-2640`, `:2930-2968`, `:2973-3091`. These precise local identities, not merely the final scalar equality, are the external input for the next extension.

**Theorem T5.7 (exact Euler-factor bookkeeping on finite-group blocks).** Assume H-KY and H-KY-LOCAL, and a finite group of lifted building automorphisms preserving the cyclic type/length and incidence data. Suppose it acts freely on vertices, hence on pointed states. Let $C_{i,\rho}$ be the multiplicity block in pointed degree $i$, $m_{i,\rho}=\dim C_{i,\rho}$, and $w_{i,\rho}(u)=\det(W_i|C_{i,\rho})$. Use the same dual indexing as in T5.6. Then
$$
\mathcal Z_\rho(u):=\prod_{i\geq1}\det(I-s_i\mathscr T_{i,\rho}(u))^{(-1)^i}
=\frac{F_\rho(u)}{\det(P_n|C_{0,\rho})},
$$
$$
\boxed{\quad F_\rho(u)=c^{m_{0,\rho}}\prod_{i\geq1}w_{i,\rho}(u)^{(-1)^i},
\qquad\prod_\rho F_\rho(u)^{d_\rho}=c^{\chi(X)}.\quad}
$$
If the action is free on **unpointed simplices as well**, this simplifies to
$$F_\rho=c^{d_\rho\chi(X)/|G|},\qquad
F_R=\prod_\rho F_\rho^{a_\rho}=c^{(\dim\pi)^2\chi(X)/|G|}.$$
Without that extra freeness the boxed local-rotation formula is the answer; a fractional power $c^{\chi(\dim\pi)^2/|G|}$ is not a rational determinant and must not be asserted. The factor does not live only in the trivial block.

Status: **conditional-on H-KY, H-KY-LOCAL**; the block bookkeeping and extension argument are **proved-here**.

<1>1. The differential, homotopy, $W,Q,J,\Sigma$, and type filtration are equivariant.

PROOF. Their definitions use incidence, cyclic type differences and subspace indices, all preserved by the assumed lifted action. Thus $Q_i$ remains unipotent on each multiplicity block.

<1>2. The equality of determinants of $I-s_i\Sigma_i$ and $I-s_i\mathscr T_i$ also holds on each block.

PROOF. Insert any group element $g$ into the traces. A contributing path now closes up to $g$ on $X$, and after lifting closes up to a building automorphism. The subspace index in H-KY-LOCAL has the same initial and final value, since that automorphism preserves indices. The monotone inequalities along the path must all be equalities, forcing exactly the additional successor intersection conditions. The paths and their weights are therefore identical for the two traces with insertion $g$. A central character projector is a linear combination of such insertions; hence their power traces on every isotypic block agree. Divide by $d_\rho$ to obtain equality on multiplicity spaces and use the logarithmic determinant expansion.

<1>3. The local factorization gives
$$\det\Phi_{i,\rho}=c^{m_{i,\rho}}\det(I-s_i\mathscr T_{i,\rho})/w_{i,\rho}.$$
Apply T1.1 on the multiplicity cochain complex.

PROOF. Its exponent is $\sum_i(-1)^im_{i,\rho}$. Substitute the last formula for $i\geq1$, leave $\Phi_{0,\rho}=P_{n,\rho}$, and cancel all $i\geq1$ dimension exponents. The remaining identity is exactly $\det P_{n,\rho}\,\mathcal Z_\rho=c^{m_{0,\rho}}\prod_iw_{i,\rho}^{(-1)^i}$.

<1>4. If the action is free on unpointed $i$-simplices, each simplex orbit gives a regular $G$-module tensored with its $(i+1)$ pointings.

PROOF. Its weighted cyclic rotation has determinant $c$ per simplex: the product of its edge-length weights is $u^n$, and the sign in $W_i$ makes the determinant $1-u^n$. In a multiplicity block there are $d_\rho$ copies per orbit, giving $w_{i,\rho}=c^{d_\rho f_i/|G|}$ and $m_{0,\rho}=d_\rho f_0/|G|$. Substitution gives the simplified exponents. With simplex stabilizers, those rotations act nontrivially on the fibre block and cannot be replaced by these fractional counts.

<1>5. Multiply over $\rho$ with the regular multiplicities.

PROOF. T5.6 gives $\prod_\rho w_{i,\rho}^{d_\rho}=\det W_i=c^{f_i}$ and $\sum_\rho d_\rho m_{0,\rho}=f_0$. This proves the global factor identity, including when unpointed stabilizers occur.

**Theorem T5.8 (honest flat coefficients versus arbitrary Kraus coefficients).** For an invertible flat local system of rank $r$ on an $X$ satisfying H-KY, the coefficient version of the pointed identity is
$$\mathcal Z_{\rm pt,E}(u)=\frac{(1-u^n)^{r\chi(X)}}{\det P_{n,E}(u)},$$
with consistent fibre transport in the covariant Hecke operators. This uses H-KY-LOCAL. It is a full local-system determinant, not the finite-group quotient Artin block of T5.7. There is no corresponding assertion for arbitrary nonflat Kraus weights. Independently, ordinary simplicial cochains with any rank-$r$ flat local system satisfy T1.1 with exponent $r\chi(X)$; their deformed pointed counterparts have exponent $r\chi_{\rm pt}$ before the local cancellation.

Status: **conditional-on H-KY, H-KY-LOCAL** for the building extension; ordinary cochain cancellation is **proved-here**.

<1>1. Use parallel transport to trivialize the local system over every simplex and every contractible building incidence configuration in the local identities.

PROOF. Invertibility and triangle flatness make transport independent of simplicial path homotopies. The building universal cover trivializes the lifted system. In these coordinates all local H-KY-LOCAL matrix identities are the scalar identities tensored with $I_r$; they descend equivariantly with the local-system monodromy.

<1>2. The $W_i$ circuit around a single simplex has identity holonomy, hence determinant $c^r$.

PROOF. For $i\geq2$ the boundary loop is contractible through that simplex, and for $i=1$ it is an edge and its inverse. Thus the cyclic weight product is $u^n I_r$. Unipotence of $Q_i$ persists. The closed-path comparison of $\Sigma_i$ with $\mathscr T_i$ keeps the same path and holonomy, so its trace argument is unchanged by a coefficient trace.

<1>3. Repeat T1.3 with all dimensions multiplied by $r$.

PROOF. The cochain determinant gives $c^{r\chi_{\rm pt}}$, while the local factors give $c^{r\sum(-1)^iif_i}$; their quotient is $c^{r\chi}$. First- and last-anchor versions agree by T5.5. For function rather than forward operators use the dual local system when transposing fibre blocks, so the same assertion holds with a consistently defined $P_{n,E}$.

<1>4. Adjoint pairing alone supplies neither this cancellation nor flatness.

PROOF. On a filled triangle choose $B_{01}=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$, $B_{12}=\operatorname{diag}(1,-1)$, $B_{02}=I$, and define reverse weights by adjoints. All are unitary and inverse-paired as channels, but $\operatorname{Ad}(B_{12}B_{01})\ne I=\operatorname{Ad}(B_{02})$. The coefficient differential has nonzero curvature. T5.2 and T5.3 still apply; T5.8's cochain proof does not.

## T6. Ramanujan quantum expanders and the precise twisted RH

Author: codex:gpt-6-astra. This section continues the preceding conventions: $X$ has dimension $n-1$, the finite Cayley group is $G$, and the locally compact building group, when needed, is denoted $\mathcal G=\mathrm{PGL}_n(F)$.

**Hypothesis H-LSV (the vertex spectrum and Cayley construction).** The colour-shift operators are commuting normal operators with $A_k^*=A_{n-k}$. Their tempered joint spectrum is
$$
\operatorname{Aspec}_n=
\left\{\bigl(q^{k(n-k)/2}e_k(z_1,\ldots,z_n)\bigr)_{k=1}^{n-1}:
|z_i|=1,\ \prod_i z_i=1\right\},
$$
where $e_k$ is the elementary symmetric polynomial. Ramanujan means that all simultaneous eigenvectors other than the specified **type-trivial** ones have their joint eigenvalues in this set. The type-trivial ones may include nonconstant characters, with eigenvalues $|S_k|\omega^k$, $\omega^n=1$. The stated LSV construction gives Ramanujan Cayley clique complexes on $\mathrm{PGL}_n(\mathbb F_{q^e})$ with colour classes of sizes $|S_k|={n\brack k}_q$ and $S_k^{-1}=S_{n-k}$.

Addresses: `math/0406208:main.tex:541-572` (Hecke operators and the Ramanujan definition), `:1437-1441` and `:1470` (the tempered set $\mathrm{Aspec}$ itself), `:1326-1358`, `:1408-1418`, `:1436-1478`; `math/0406217:main.tex:497-515`, `:676-682`, `:2617-2626` (the per-colour sets $S_k$ with $|S_k|=\binom nk_q$ and $S_{n-k}=S_k^{-1}$), `:1673-1686`. The last two intervals specify the coloured generating sets; the generator formula $b_u=1-rz^{-1}$ is `math/0406217:main.tex:1407-1415`. This hypothesis is a statement about the joint Hecke spectrum, not a claim that every nontrivial finite-group irreducible representation is itself a tempered representation of $\mathcal G$.

**Hypothesis H-STRONG (the scope of flow-Ramanujan results).** LLP's definition requires every infinite-dimensional **Iwahori-spherical** constituent of $L^2(\Gamma\backslash\mathcal G)$ to be tempered. This can be stronger than the vertex, or maximal-compact-spherical, definition. The cited LSV explicit examples satisfy the stronger property; equivalence of the two notions in ranks one and two is also stated there. Addresses: `1702.05452:rw_ramanujan_complex.tex:196-214`, `:674-701`. This is the extra spectral hypothesis when applying H-LLP in general rank. It is not silently included in an arbitrary tuple of channels satisfying only a vertex spectral bound.

**Definition T6.1 (the quantum vertex property, with its exceptional space).** Let $X=\operatorname{Cay}(G,S)$ have the H-LSV colour classes, with $S=\bigcup_kS_k$ generating $G$. For a unitary representation $\pi:G\to U(N)$ set $R=\operatorname{Ad}\pi$ on $M_N$, and define
$$
\Phi_k(a)=\frac1{|S_k|}\sum_{s\in S_k}\pi(s)a\pi(s)^*,\qquad
\widehat A_k=|S_k|\Phi_k=\sum_{s\in S_k}R(s).
$$
Let $\mathcal F_R=\{a:R(g)a=a\text{ for every }g\in G\}$. Let $\mathcal E_R$ be the sum, inside $R$, of the type-character subrepresentations excluded by the H-LSV convention for this complex. It includes $\mathcal F_R$; it can be larger. Call the tuple **Ramanujan of type $\widetilde A_{n-1}$ relative to $\mathcal E_R$** when its joint spectrum on $\mathcal E_R^\perp$ lies in $\operatorname{Aspec}_n$. If $\mathcal E_R=\mathcal F_R$, this is precisely the fixed-point-complement definition in the question.

Status: **proved-here** (definition). Replacing $\mathcal E_R$ by $\mathcal F_R$ for all partite complexes is **FALSE-as-drafted**.

**Theorem T6.2 (Harrow-type transfer, with correct multiplicities and scope).** Under H-LSV, for every finite-dimensional unitary $\pi$:

1. The $\Phi_k$ are commuting normal, unital, trace-preserving completely positive maps, with $\Phi_k^*=\Phi_{n-k}$. Their common fixed space is $\pi(G)'$, the commutant. It is one-dimensional exactly when $\pi$ is irreducible.
2. They satisfy Definition T6.1 relative to $\mathcal E_R$. In particular the draft's fixed-point-complement theorem holds when there are no additional type-character summands in $R$.
3. The nonexceptional quantum vertex polynomial
   $$P_{n,R}(u)=\sum_{k=0}^n(-1)^kq^{k(k-1)/2}\widehat A_k u^k,\qquad \widehat A_0=\widehat A_n=I,$$
   restricted to $\mathcal E_R^\perp$, has all its zeros on $|u|=q^{-(n-1)/2}$, counted with multiplicity.
4. In rank three, under H-KL and a lifted finite-group action as in T5.6–T5.7, the **quotient Artin flow factors** for $R$ inherit H-KL's nontrivial root radii, after deleting the corresponding type-trivial spectral summands. The unit-length edge factor has radii $q^{-1},q^{-1/2}$; the algebraic-length-two reversed-edge factor has radii $q^{-1/2},q^{-1/4}$; the chamber factor has radii $1,q^{-1/2},q^{-1/4}$. Their graded product uses the factors and Euler correction of T5.7, including cancellation. This is not an assertion about the arbitrary full-complex connection $E_{(g,gs)}=R(s)$ in the forward convention.
5. In general rank, H-KY gives the determinant identity, **not** a list of prescribed RH circles for all its factors. With H-STRONG and the branching hypotheses of H-LLP, each applicable LLP quotient Artin flow satisfies the one-sided bound in T6.4. No unsourced “Kang–Yu RH theorem” is asserted.

Status: parts 1–3 **conditional-on H-LSV**, with the finite-group transfer and fixed-space proofs **proved-here**; part 4 **conditional-on H-KL** and the stated lifted action; part 5 **conditional-on H-KY, H-STRONG, H-LLP**. The unrestricted theorem in the draft is **FALSE-as-drafted**.

<1>1. The colour sums commute as elements of $\mathbb C[G]$.

PROOF. They commute in the regular representation by H-LSV. The regular representation of the group algebra is faithful: an element annihilating the vector at the identity has every coefficient zero. Hence their commutators vanish in the algebra and in every representation. Inversion gives $\widehat A_k^*=\widehat A_{n-k}$, so commutativity also implies normality. Each $\Phi_k$ is an average of unitary conjugations, proving its channel properties.

<1>2. The common fixed space is the commutant.

PROOF. If $\Phi_k(a)=a$, the Hilbert–Schmidt identity
$$\frac1{|S_k|}\sum_{s\in S_k}\|R(s)a-a\|_2^2
=2\|a\|_2^2-2\operatorname{Re}\langle a,\Phi_k(a)\rangle=0$$
forces $R(s)a=a$ for every $s\in S_k$. Apply this for all $k$, and use generation of $G$. The converse follows by substitution. If $\pi=\bigoplus_\rho m_\rho\rho$, its commutant is $\bigoplus_\rho M_{m_\rho}$, of dimension $\sum_\rho m_\rho^2$. This is one exactly for an irreducible $\pi$.

<1>3. Every joint spectral value in $R$ occurs in the regular vertex representation, except possibly with a larger multiplicity in $R$.

PROOF. Decompose $R=\bigoplus_\rho a_\rho\rho$ and $\mathbb C[G]=\bigoplus_\rho d_\rho\rho$. The algebra elements giving the $A_k$ act by the same matrices in each copy of $\rho$. Thus support inclusion, not an embedding of $R$ in a single regular representation, proves the assertion. Removing the type-character summands leaves H-LSV's tempered joint spectrum.

<1>4. On a simultaneous nonexceptional eigenvector, $P_{n,R}(u)$ has the scalar eigenvalue
$$\sum_{k=0}^n(-1)^k q^{k(k-1)/2}q^{k(n-k)/2}e_k(z)u^k
=\prod_{j=1}^n(1-q^{(n-1)/2}z_ju).$$
PROOF. The exponent in the coefficient is $k(n-1)/2$, and $e_n(z)=1$. Since $|z_j|=1$, all roots have the stated modulus. Simultaneous normality gives an orthonormal eigenbasis, so taking the product proves the determinant assertion.

<1>5. For flows use T5.6, rather than treating $R$ as a subspace of vertex functions with the wrong dimension.

PROOF. Each quotient flow block has its spectrum among the full scalar flow spectrum, because its determinant occurs with positive regular multiplicity $d_\rho$. Replacing that multiplicity by $a_\rho$ creates no new spectral values. H-KL therefore transfers the nontrivial radii. For the reversed-edge determinant, $1-u^2\lambda=0$ gives $|u|=|\lambda|^{-1/2}$, explaining the two additional radii. The forward Fourier convention in T5.6 uses $R(s^{-1})$ on vertex fibres, which exchanges $k$ with $n-k$ relative to $\widehat A_k$. Changing to the pullback convention, or consistently exchanging those colours, resolves this; H-LSV's tempered set is invariant under the corresponding duality $z_j\mapsto z_j^{-1}$. A transpose without also tracking the fibre convention is not justified.

<1>6. Deleting a fixed-point block and deleting all spectrally trivial building modes are different operations.

PROOF. Suppose $X$ has a nonconstant type character $\chi$ with $\chi(s)=\omega^k$ on $S_k$, and take $\pi=1\oplus\chi$. Its adjoint representation contains $\chi$ and $\chi^{-1}$ on the two off-diagonal matrix units. Their channel eigenvalues are $\omega^k$ and $\omega^{-k}$, so they are not common fixed points when $\omega\ne1$. In rank three, their unnormalized first eigenvalue has modulus $q^2+q+1>3q$ for $q>1$, whereas H-LSV bounds every tempered first eigenvalue by $3q$. Thus the proposed fixed-point-only assertion fails on such a partite Ramanujan complex. No positivity or faithfulness argument removes these modes.

<1>7. The all-rank distinction in part 5 is essential.

PROOF. A nonspherical Iwahori constituent can have no vertex-fixed vectors. A theorem about the vertex tuple alone then imposes no direct condition on it. H-STRONG supplies the missing hypothesis for H-LLP. H-KY supplies a different ingredient, the cohomological determinant identity, and states no RH. These inputs cannot be interchanged.

**Proposition T6.3 (one faithful representation and the exact converse criterion).** For a fixed coloured Cayley complex let $\mathcal B_X\subset\widehat G$ be the irreducibles whose vertex colour-sum matrices have at least one nonexceptional joint eigenvalue outside $\operatorname{Aspec}_n$. Let $\operatorname{supp}(R)=\{\rho:a_\rho>0\}$. Then
$$
R\text{ satisfies Definition T6.1}\iff\mathcal B_X\cap\operatorname{supp}(R)=\varnothing,
\qquad
X\text{ is vertex-Ramanujan}\iff\mathcal B_X=\varnothing.
$$
Consequently coverage of every nonexceptional irreducible by $\pi\otimes\overline\pi$ is sufficient for the converse. More precisely the converse also follows if all missing irreducibles are independently known to be good. Faithfulness of $\pi$ alone does not imply coverage. For a particular generating set, coverage is not a necessary condition for both objects accidentally to be Ramanujan; the proposed unconditional “if and only if coverage” needs this qualification.

Status: **proved-here** as a finite-group spectral criterion; the faithful-only converse is **FALSE-as-drafted**.

<1>1. The two equivalences follow by the decompositions in T6.2, step <1>3.

PROOF. The regular representation contains every irreducible; $R$ tests exactly its support. The displayed set intersections are therefore necessary and sufficient, including all multiplicities and exceptional modes.

<1>2. A concrete faithful counterexample already exists in graph rank.

PROOF. Let $G=\mathbb Z/28$, $S=\{1,-1,3,-3\}$, and let $X$ be its Cayley clique complex. It is a connected 4-regular bipartite graph: all generators are odd, so there are no triangles and the clique complex has dimension one. The nontrivial character $g\mapsto e^{2\pi ig/28}$ has adjacency eigenvalue
$$2\cos(\pi/14)+2\cos(3\pi/14)>3.5135>2\sqrt3.$$
It is neither the constant nor the bipartite eigenvalue. Hence this graph is not Ramanujan. Take the faithful one-dimensional $\pi(g)=e^{2\pi ig/28}$. Then $\pi\otimes\overline\pi=1$, $M_1=\mathbb C$, and the fixed-point complement is zero; the quantum condition is vacuous. This counterexample is small and explicit; no minimal-vertex claim for this converse is made.

<1>3. In contrast, full coverage really proves the converse.

PROOF. If every potentially bad irreducible is in $\operatorname{supp}(R)$ and the tested blocks are good, $\mathcal B_X$ must be empty. This is a statement about all spectral blocks, not about recovering the group from a faithful matrix representation. For an irreducible $\pi$, central elements act by scalars, so its adjoint representation can in particular miss all irreducibles with nontrivial central character.

**Hypothesis H-KAMBER (normalized one-sided spectral criterion).** On the stated finite-dimensional extended affine-Hecke modules, $p$-temperedness is equivalent to
$$|\theta|\leq q^{l(\beta_i)(p-1)/p}$$
for every eigenvalue $\theta$ of $h_{\beta_i}$. The associated zeta is the reciprocal product of $\det(I-h_{\beta_i}u^{l(\beta_i)})$. Addresses: `1701.00154:L_p_Expander_Complexes.tex:334-358`, especially `:345-350`; the building-quotient and stronger Ramanujan scope is `:130-165`. The corollary at `:359-363` calls its bounded variable a “pole,” but the adjacent determinant formula and eigenvalue theorem require distinguishing an actual $u$-pole from its inverse normalized spectral parameter. We use the unambiguous eigenvalue theorem.

**Proposition T6.4 (one-sided RH in the correct variable).** Under H-LLP, for a $b$-regular applicable flow with $b>1$ and zeta $\det(I-uT)^{-1}$, a pole at $u=b^{-s}$ satisfies
$$\operatorname{Re}s=1\quad\text{for peripheral }|\lambda|=b,
\qquad\operatorname{Re}s\leq\tfrac12\quad\text{for }|\lambda|\leq\sqrt b.$$
The imaginary part is defined modulo $2\pi/\log b$. The condition $|s|=1$ printed in the quoted source cannot literally replace $\operatorname{Re}s=1$. Interior cases $0<|\operatorname{Re}s|<1/2$ occur by H-LLP (the source's existence clause carries an absolute value); the positive-side interior cases in rank three are supplied by the type-(e) chamber roots of T3.5 at $\operatorname{Re}s=1/2,1/4$ with $b=q$. [Wording corrected after review, 2026-09-13.] Under H-KAMBER, actual nontrivial $u$-poles satisfy $|u|\geq q^{-(p-1)/p}$, with trivial radius $q^{-1}$ in the quoted normalization. These are lower bounds on pole radii, or upper bounds on eigenvalue radii, not forced equalities.

Status: **conditional-on H-LLP, H-KAMBER** for the spectral assertions and existence of interior examples; conversion of variables is **proved-here**. Literal $|s|=1$ and the unreversed pole inequality are **FALSE-as-drafted**.

<1>1. A finite pole corresponds to $\lambda=u^{-1}\ne0$.

PROOF. Taking absolute values in $u=b^{-s}$ gives $|\lambda|=b^{\operatorname{Re}s}$. This proves both alternatives and shows why the modulus of $s$ is not the right invariant. A zero eigenvalue gives no finite pole and no finite $s$.

<1>2. For a Kamber factor let $\ell=l(\beta_i)>0$.

PROOF. The equation $1-\theta u^\ell=0$ gives $|u|=|\theta|^{-1/\ell}$. H-KAMBER then gives $|u|\geq q^{-(p-1)/p}$. The variable with the source's upper bound is $|\theta|^{1/\ell}=|u|^{-1}$, not $|u|$.

<1>3. Neither inequality entails a reciprocal spectral symmetry.

PROOF. A disc includes its interior. T3.5's type-(e) chamber roots have $\operatorname{Re}s=1/2$ and $1/4$ with $b=q$, providing the listed rank-three mechanism for interior poles of the unsigned chamber flow; the sign in $I+uL_B$ changes arguments but not moduli. Their occurrence, rather than merely their admissibility in a table, is part of H-LLP's existence assertion.

**Proposition T6.5 (which rank-three factors have a duality).** Assume $q>1$ and the commuting adjoint relation $A_2=A_1^*$. On a simultaneous vertex eigenvector, write $a$ for the eigenvalue of $A_1$, so
$$p_a(u)=1-au+q\overline a\,u^2-q^3u^3.$$
Its zero multiset is invariant under $u\mapsto q^{-2}/\overline u$, even before imposing Ramanujan. The full untwisted real vertex determinant is also invariant, as a zero multiset, under the holomorphic inversion $u\mapsto q^{-2}/u$. The principal-series parts of the edge and chamber determinants inherit dualities at constants $q^{-2}$ and $q^{-1}$ respectively. The **full** nontrivial edge and chamber factors have no such universal single-radius duality. In particular the type-(e) chamber block alone cannot have a zero-set symmetry $u\mapsto c/\overline u$, or $u\mapsto c/u$, for any constant $c>0$.

Status: the algebraic identities and the type-(e) obstruction are **proved-here**; attribution of principal-series factors is **conditional-on H-KL-TABLE**, and applicability of the adjoint relation is **conditional-on H-LSV**.

<1>1. Direct calculation gives the anti-reciprocal identity
$$p_a(u)=-q^3u^3\,\overline{p_a\!\left(\frac1{q^2\overline u}\right)}.$$
PROOF. The conjugated expression is $1-\overline a/(q^2u)+a/(q^3u^2)-1/(q^3u^3)$. Multiplication by $-q^3u^3$ gives exactly $p_a(u)$. Its constant and leading coefficients are nonzero, so the displayed involution preserves all its roots with multiplicity. For the full real determinant, complex conjugation also preserves the multiset; composing the two symmetries gives the stated holomorphic inversion. For an arbitrary coefficient block only the anti-holomorphic symmetry has been established without a reality or dual-block condition.

<1>2. For a principal-series constituent the edge polynomial is $p_a(u)$, and the chamber polynomial is $p_a(u^2)$ in the source's root conventions.

PROOF. H-KL-TABLE gives their roots $q^{-1}\alpha_i^{-1}$ and $\pm q^{-1/2}\alpha_i^{-1/2}$. The normalized constant terms are 1, hence their polynomials are respectively $\prod_i(1-q\alpha_i u)$ and $\prod_i(1-q\alpha_i u^2)$. The first involution lifts under the square map to $u\mapsto q^{-1}/\overline u$ for the second. These statements concern the principal-series factors; a unit-length chamber clock and the algebraic-length edge clock have different scales.

<1>3. On the Ramanujan vertex spectrum the anti-reciprocal involution fixes each root, since all have modulus $q^{-1}$.

PROOF. Its fixed set is the circle $|u|=q^{-1}$. Equivalently the normalized Satake parameters have modulus one. This is the precise single-circle, Hilbert–Polya-style spectral reading. A canonical self-adjoint logarithm or a canonical unitary realization of a particular companion matrix has not been constructed: repeated roots can make a companion matrix nonsemisimple, and logarithms require branch choices. The spectral reading does not remove those extra requirements.

<1>4. A type-(e) chamber block has one root at radius $q^{-1/2}$ and two at radius $q^{-1/4}$.

PROOF. Under either proposed inversion the radius $r$ goes to $c/r$. If each of the two radii were fixed, one would need both $c=q^{-1}$ and $c=q^{-1/2}$, impossible for $q>1$. If the radii were exchanged, their multiplicities would have to agree, but they are 1 and 2. Thus even this allowed irreducible block has no single such duality. Steinberg roots at radius 1 introduce another scale. The edge principal-series and type-(e) parts likewise carry different scales with independently varying multiplicities; H-KL supplies no symmetry pairing them. Separate restricted circles can be given separate normalizations, but this is not a functional equation for the entire factor.

**Proposition T6.6 (Weil positivity here is a bound until a duality is supplied).** Let $M$ be any retained finite transfer block, with eigenvalue multiset $\{\mu_j\}_{j=1}^N$, counted algebraically, and let $r>0$. Put $\nu_m=\sum_j(\mu_j/r)^m$ for $m\geq0$, with $\nu_0=N$ and $\nu_{-m}=\overline{\nu_m}$. Then $\nu$ is a positive-definite sequence on $\mathbb Z$ exactly when all $|\mu_j|\leq r$. If the retained multiset is additionally invariant under $\mu\mapsto r^2/\overline\mu$, the bound forces every retained eigenvalue onto $|\mu|=r$. This is the finite form of the distinction in `notes/weil-positivity.md`; it applies to each retained ordinary block, not automatically to an alternating sum with negative spectral multiplicities.

Status: **proved-here**.

<1>1. A single $z$ in the open unit disc has moments $z^m$, $m\geq0$, of the positive Poisson measure on the circle with centre $z$; a $z$ on the circle gives a point mass.

PROOF. Expanding the positive density $(1-|z|^2)/|e^{it}-z|^2$ as a Fourier series gives its $m$-th moment $z^m$. Therefore any finite sum of these moment sequences is positive definite. This proves sufficiency, including $z=0$.

<1>2. Positive definiteness implies $|\nu_m|\leq\nu_0=N$ by its two-by-two minors.

PROOF. If the largest modulus of the normalized eigenvalues were $R>1$, write their contribution as $R^m\sum_jb_je^{im\theta_j}$, with distinct phases and positive integer multiplicities $b_j$. The Cesaro mean square of the sum tends to $\sum_jb_j^2>0$, because distinct phase cross terms have mean zero. Hence its modulus is bounded below by a positive constant on an infinite subsequence. The smaller-modulus contribution is $o(R^m)$, contradicting boundedness of $\nu_m$. This proves necessity.

<1>3. With the additional involution, an eigenvalue strictly inside the circle would have a partner strictly outside it.

PROOF. The partner's modulus is $r^2/|\mu|>r$. Thus no interior eigenvalue is possible. T6.5 supplies this mechanism for the vertex/principal-series duality. T6.4 alone does not. All these arguments are blind to Jordan blocks, so positivity alone does not construct a Hilbert–Polya inner product for a nonsemisimple transfer matrix.

**Hypothesis H-COVER (the type cover and contractibility).** The building is contractible, its vertex type changes under $g\in\mathcal G$ by the character $\tau(g)=\operatorname{ord}_{\varpi}\det g\pmod n$, and torsion-free lattices act freely on it. The local pointed ordering, lengths and indices are preserved by cyclic shifts of the type diagram. Addresses: `1702.05452:rw_ramanujan_complex.tex:196-214`; `2607.21262:main.tex:439-474`, `:1724-1738`; `math/0406208:main.tex:1334-1358`; the equivalence of type preservation with membership in the kernel is `2607.21262:main.tex:2014-2019`. Contractibility is also the geometric input to the lifted-local-system argument in T5.8.

**Proposition T6.7 (using a type cover without assuming one was present).** Let $\Gamma\subset\mathcal G$ be torsion-free and cocompact, with a simplicial quotient and descended cyclic type-difference data, but not necessarily type-preserving. Under H-COVER, H-KY and H-KY-LOCAL, the pointed determinant identity descends from the type-preserving cover:
$$\mathcal Z_{\rm pt}(\Gamma\backslash\mathscr B,u)=(1-u^n)^{\chi(\Gamma\backslash\mathscr B)}/\det P_n(u).$$
In rank three H-KL's nontrivial radius conclusions also apply if this quotient is vertex-Ramanujan. This is a deduction using a finite cover and local equivariance; it is not a claim that the quoted theorem omitted its type-preservation hypothesis.

Status: **conditional-on H-COVER, H-KY, H-KY-LOCAL** for the identity; **conditional-on H-COVER, H-LSV, H-KL** for rank-three RH.

<1>1. Set $\Gamma_0=\Gamma\cap\ker\tau$. The cover $X_0=\Gamma_0\backslash\mathscr B\to X=\Gamma\backslash\mathscr B$ has finite cyclic deck group $H=\Gamma/\Gamma_0$.

PROOF. $H$ embeds in $\mathbb Z/n$. It acts freely even on unpointed simplices of $X_0$: a setwise stabilizer would lift to an element of the torsion-free $\Gamma$ stabilizing a finite simplex in the building, hence a finite-order element, hence the identity. Thus $\chi(X_0)=|H|\chi(X)$.

<1>2. Apply T5.7 on $X_0$ to the trivial representation of this deck group.

PROOF. All local maps commute with $H$, because they use type differences rather than an absolute type label. Its invariant pointed and vertex spaces are exactly the corresponding spaces on $X$, with descended incidences. Freeness on simplices makes its factor $c^{\chi(X_0)/|H|}=c^{\chi(X)}$. This gives the displayed identity.

<1>3. Passing to this specific cover preserves vertex-Ramanujan, and also preserves strong Ramanujan when that property is assumed.

PROOF. Decompose $L^2(\Gamma_0\backslash\mathcal G)$ under the deck characters. Every character of $H\subset\mathbb Z/n$ extends to a character of $\mathbb Z/n$, hence to a unitary character of $\mathcal G$ through $\tau$. Multiplication by that character identifies its deck-isotypic space with a unitary-character twist of $L^2(\Gamma\backslash\mathcal G)$. These characters are trivial on the vertex and Iwahori stabilizers and preserve temperedness: multiplying matrix coefficients by a modulus-one character preserves their absolute values. They only permute the type-trivial exceptions. Thus the cover satisfies the relevant Ramanujan condition exactly when the base does. Apply H-KL on $X_0$ in rank three, then restrict its flow operators to $H$-invariants as in T6.2. No new eigenvalues arise on the quotient.

## T7. The zeta that wants to exist: verdict and numerical targets

**Definition T7.1 (recommended object).** The object recommended here is the **graded geodesic determinant of a complex with specified geodesic data**, not an unqualified new invariant called “the Ihara zeta of every complex.” Specify, in each degree $k\geq1$, a finite state set $\mathcal S_k$, a successor relation with incidence multiplicities, a positive integer algebraic length $\ell_k(\sigma)$, and a step transport $U_{\sigma\tau}$ on a finite-dimensional fibre $V$. Give the entire degree-$k$ fibre/state space parity $k+1$. Its full definition, including the sign, is
$$
\boxed{\begin{gathered}
\mathscr T_k^U(u)(v\otimes[\sigma])
=\sum_{\sigma\rightsquigarrow\tau}u^{\ell_k(\sigma)}U_{\sigma\tau}v\otimes[\tau],
\qquad W=\bigoplus_{k=1}^d V\otimes\mathbb C^{\mathcal S_k},\quad
|V\otimes\mathbb C^{\mathcal S_k}|=k+1\pmod2,\\
\mathcal Z(X,\mathfrak g,U;u)
=\operatorname{sdet}_{W}\!\left(I-\bigoplus_{k=1}^d(-1)^{k+1}\mathscr T_k^U(u)\right)^{-1}
=\prod_{k=1}^d\det_{V\otimes\mathbb C^{\mathcal S_k}}
\!\left(I-(-1)^{k+1}\mathscr T_k^U(u)\right)^{(-1)^k}.
\end{gathered}}
$$
For an arbitrary abstract complex, the intrinsic default is $\mathcal S_k=\Omega_k$, unit length, the ordered overlap/noncell rule T0.1, and last-anchor transport $U_{\sigma\tau}=E_{(v_k,w)}$ for a 1-skeleton connection. For a building quotient, use the cyclically ordered pointed states, **opposition** successors and first-gap algebraic length of T0.2. For a quotient Artin factor use the quotient states and voltage transports of T5.6; do not mistake that for the full-cover connection. The scalar case is $V=\mathbb C$ with all transports 1. The word “natural” here means functorial under isomorphisms preserving these specified data. This note does not prove uniqueness among all possible choices of higher-dimensional geodesics.

Status: **proved-here** as a finite graded construction; its building identification is **conditional-on H-POINT, H-KY**.

<1>1. Isomorphisms preserving states, lengths, successor incidences and transports conjugate the displayed matrices degree by degree.

PROOF. They biject all matrix summands, preserve the grading, and therefore preserve the superdeterminant. For a graph the prescribed default is exactly Hashimoto and has only an even flow sector. For a building it is precisely the completed vertex product of T1.3; in rank three Kang–Li's edge-only zeta is obtained by retaining only the edge factor, not by identifying it with the total product.

<1>2. The theorem list has the following precise status.

PROOF. T2.2/T5.2 prove the general rational Bass–Schur identity for arbitrary transports. T3.1–T3.2 prove the supertrace and delay realization. T5.3 proves the primitive product and Kraus ring positivity. T4.1–T4.2 prove an incidence-matrix realization with auxiliary copies and an actual Berezinian. T1.3/T4.5 and T5.7–T5.8 give the stronger cohomological, vertex and flat-coefficient identities **conditional on the building hypotheses**. T6.2 proves finite-group quantum spectral transfer conditional on H-LSV, and inherits the rank-three factor RH conditional on H-KL; T6.4 gives the conditional one-sided branching RH. A characterization of all complexes admitting a prescribed low-degree vertex formula remains **sketched/unestablished**. None of these results constructs ordinary cohomology whose Frobenius is the cell flow, or identifies cell chirality with flow superparity.

For a general complex the universal result is the explicit forbidden-transition Schur complement, with lower-cell and upper-cell information retained. A cubic Hecke identity is a theorem for the building data; it is false for the ordered default even on a four-vertex sphere. This does **not** prove that only buildings can ever have an accidental vertex identity. The surface-like feature that survives scrutiny is the possibility of an odd chamber contribution to a graded divisor. It is not an identification with surface cohomology or a universal Betti-number formula. On the building vertex side those chamber factors can cancel completely as finite zeros, because the reduced vertex $L$-function is a reciprocal polynomial. “Fermionic zeros” therefore describes net odd multiplicity in a specified graded presentation and must be checked after cancellation.

**Proposition T7.2 (three smallest useful exact tests).** The following tests use the **ordered default** of T0.1. The input must specify the faces; do not silently replace a specified complex by its clique completion.

| Complex and vertices | $f$-vector and $\chi$ | $\det(I-uT_1)$ | $\det(I+uT_2)$ | Predicted total and Euler-factor interpretation |
|---|---|---|---|---|
| graph cycle $C_3$, 3 vertices, no filled triangle | $(3,3)$, $0$ | $(1-u^3)^2$, degree 6 | absent | $(1-u^3)^{-2}$; graph Bass factor $(1-u^2)^{-\chi}=1$ |
| filled triangle $\Delta^2$, 3 vertices | $(3,3,1)$, $1$ | $1$, degree 0 | $1$, degree 0 | $1$; there is no forced $(1-u^3)$ factor in this flow zeta |
| tetrahedron boundary $\partial\Delta^3$, 4 vertices | $(4,6,4)$, $2$ | $1$, degree 0 | $(1-u^4)^6$, degree 24 | $(1-u^4)^6$; the proposed cubic Euler factor $(1-u^3)^2$ cannot supply a polynomial vertex compression |

Each row must satisfy the full rational equality in T2.2 and the block-matrix equality in T4.1. The second and third rows are non-building 2-complexes. The graph row is the smallest simple graph with a primitive nonbacktracking cycle, the second row is the smallest 2-complex, and the third is the smallest example giving T2.4's pole obstruction.

Status: **proved-here**; all displayed polynomials were also independently checked exactly with `sympy` in an inline `timeout 60 python3` calculation, with no scratch files written.

<1>1. The graph has two oriented cycles, each of length three; the filled triangle has no allowed successor in either degree.

PROOF. These observations give the first two determinant rows directly. For the filled triangle the Schur factors themselves need not equal 1: $\det K_1(u)=(1+2u)(1-u)^2$, and $\det M_1(u)$ is its reciprocal. In degree two, $\det K_2(-u)=(1-u^3)^2$ and $\det M_2(-u)$ is its reciprocal. This explicitly tests cancellation of the rational Schur factors at their singular points.

<1>2. The boundary row is T2.4's six chamber cycles of length four.

PROOF. Its 1-skeleton is $K_4$, but its 3-simplex is deliberately absent. Replacing it by the clique complex of $K_4$ gives the filled tetrahedron, a different, three-dimensional complex with all its ordered flows zero. This distinction is essential for interpreting a “surface-like” effect of the odd sector.

<1>3. If the numerical pipeline accepts only clique complexes, an additional small non-building surface test is the octahedral sphere with six vertices, the clique complex of $K_{2,2,2}$.

PROOF. Its $f$-vector is $(6,12,8)$ and $\chi=2$. Label its vertices in three antipodal pairs. From an edge, the only allowed endpoint is the antipode of its first vertex, giving six cycles of length four on the 24 ordered edges. From a triangle, the same antipodal rule gives eight cycles of length six on its 48 orderings. Hence the signed determinants are $(1-u^4)^6$ and $(1-u^6)^8$, and the total is $(1-u^6)^8/(1-u^4)^6$. After cancellation its numerator and denominator degrees are 36 and 12. The proposed vertex expression would require $(1-u^3)^2(1-u^4)^6/(1-u^6)^8$, which has a pole at $u=-1$ and is not polynomial. This is an optional fourth test accommodating the clique-only convention; it does not replace the three minimal diagnostics above.

**Proposition T7.3 (predictions and limits for the PGL$_3(\mathbb F_3)$ numerical lane).** If the reported Cayley construction has the $q=3$ building links and the stated building-quotient interpretation, the expected counts are
$$
|G|=5616,\quad f_1=73008,\quad f_2=97344,\quad\chi=29952.
$$
The pointed edge space has dimension $146016$; each directed-colour edge block has dimension $73008$ and outdegree 9. The pointed chamber space has dimension $292032$ and outdegree 3. The all-ordered chamber space instead has dimension $584064$, with two orientation blocks. The all-ordered edge outdegree is 21, not 9. The cubic vertex determinant has degree $16848$; the edge algebraic determinant has degree $219024$ and the chamber determinant degree $292032$ under the nonzero-spectrum building hypotheses. The cleared identity has degree $308880$ on each side:
$$\det P_3\,D_B=(1-u^3)^{29952}\det(I-uL_E)\det(I-u^2L_E^t).$$

Status: the counts and degree arithmetic are **proved-here conditional-on H-POINT, H-KL** for this construction; applying the formula to a non-type-preserving quotient uses T6.7. The observations about the existing output below are read-only numerical observations, not proof of its construction or of an entire determinant identity.

<1>1. Count incident cells at a vertex.

PROOF. The vertex has $2(q^2+q+1)=26$ neighbours, so $f_1=13f_0$. Its link has $26\cdot4/2=52$ edges, giving $f_2=52f_0/3$. The group order is $((27-1)(27-3)(27-9))/(3-1)=5616$. These give the displayed counts and $\chi$. The state dimensions and outdegrees follow from T0.3. Under the nonzero eigenvalues in the building tables the polynomial degrees equal the state dimensions, multiplied by the algebraic-length power when appropriate; the vertex leading term is $-27u^3I$.

<1>2. The observed output supports limited checks and must not replace the hypotheses.

PROOF. The read-only file `outputs/a2_complex_zeta.txt`, as inspected while appending this section, reports these cell counts, a failed global 3-colouring, and agreement of the cleared logarithmic determinant series through $u^{18}$ both on the 5616-vertex base and its 16848-vertex type-preserving cover (lines 17–22, 94–121). This is consistent with T6.7, but agreement to order 18 is not an exact determinant proof of degree 308880. The link diagnostic reports 26 vertices, 4-regular, bipartite, girth 6 and a unique line through any two points; the first four already force the unique $(4,6)$-cage, the incidence graph of $\mathrm{PG}(2,3)$, so the identification is certified. [Sentence corrected after review, 2026-09-13: the version read during the append reported the diagnostic wrongly.]

<1>3. Two distinctions in that output matter for the quantum checks.

PROOF. First, the correct nontrivial **chamber eigenvalue** radii are $1,3^{1/2},3^{1/4}$, the reciprocals of the roots in H-KL; $3^{3/4}$ printed as a prediction there is not the reciprocal of $3^{-1/4}$. The reported modulus $1.316074$ is approximately $3^{1/4}$ and fits the correct radius. Second, its failure of pure-power Euler corrections on representation blocks (lines 200–235) is not a counterexample to T5.7's local-rotation formula: $\chi/|G|=16/3$ is already nonintegral, so freeness on all unpointed simplices cannot hold. The required check is the actual product of the $w_{i,\rho}$ determinants with the appropriate Fourier convention, not a fitted fractional power. The numerical output has not been independently audited block by block in this note.

## T8. Correction ledger, hypothesis register, and result

**Proposition T8.1 (append-only qualification of an overbroad sentence in T4).** The literal wording of T4.2, step <1>3, “even allowing ... a polynomial vertex factor,” is too strong if that factor is completely arbitrary. The correct obstruction is to realizing $\mathcal Z_{\rm ord}^{-1}$ by a polynomial ordinary determinant with **only** an Euler-factor adjustment, and to the prescribed universal building-shaped vertex identity of T2.4. It is not an obstruction after multiplication by an arbitrary polynomial chosen to cancel the denominator.

Status: that literal unrestricted sentence is **FALSE-as-drafted; corrected statement proved-here**. The matrix and Berezinian identities in T4.1–T4.2 are unaffected. T0–T5 have been left intact as requested; this qualification is authoritative for interpreting the earlier sentence.

<1>1. On $\partial\Delta^3$, any power of $1-u^3$ is nonzero at $u=i$, while $\mathcal Z_{\rm ord}^{-1}$ has a pole there.

PROOF. A polynomial determinant cannot have that pole. This proves the obstruction with Euler factors only. T2.4 separately proves the prescribed vertex-collapse obstruction.

<1>2. An unrestricted extra polynomial can cancel it.

PROOF. Choose $p(u)=(1-u^4)^6$. Then $p(u)\mathcal Z_{\rm ord}^{-1}=1$, the determinant of an identity matrix. Thus no theorem excluding *every* polynomial multiplier was proved, and none is intended. Allowing arbitrary rational matrices or arbitrary cancelling multipliers gives no prescribed incidence/Hecke construction.

**Proposition T8.2 (correction ledger).** The following table records the corrected claims and their surviving replacements. A missing external result is labeled unestablished rather than disproved.

Status: **proved-here** as an accounting of the preceding statements, with the conditional statuses retained.

| Drafted or tempting claim | Correction and location |
|---|---|
| Unrestricted ordered flow equals LLP flow | LLP also restricts colours/states. Its consecutive-type component is the corresponding pointed opposition flow, T0.3–T0.5. |
| Ordered flow is $k!$ copies of Kang–Yu flow | State counts do not imply conjugacy; opposition is stricter than nonincidence. Already the rank-three edge outdegrees differ, T0.3/T0.5. |
| The two raw edge colour classes are invariant $L_E,L_E^t$ blocks | They are not invariant for the unrestricted rule. They become blocks only after imposing the building successor relation, T0.3. |
| The reversed-edge $u^2$ is a multiplicity or matrix square | It is algebraic length two; the operator is still the reversed-edge adjacency, T0.3/T3.2. |
| All $3!$ chamber orders represent $L_B$ once | Pointed cyclic chambers have $3f_2$ states; all orders give two transpose-related orientation blocks and a squared determinant, T0.3. |
| Total graded zeta equals Kang–Li's edge-only zeta | The repaired total is $D_B/D_E=(1-u^3)^\chi/\det P_3$; Kang–Li's zeta is $1/D_E$, T0.4. |
| Kang–Yu's cochain product itself has exponent $\chi$ | Its exponent is $\sum(-1)^i(i+1)f_i$. Subtracting the local $if_i$ contributions gives $\chi$, T1.2–T1.3. |
| Ordered-cochain torsion universally gives ordinary $\chi$ | The chain-homotopy determinant exponent is $\sum(-1)^i(i+1)!f_i$, already wrong for one edge. The literal unconstrained existence statement admits artificial projection constructions, T1.2. |
| Knill's super pseudodeterminant is literally the $u\to1$ zeta/Euler-factor limit | It is a different metric and degree-weighted object; even one edge distinguishes them. Spanning trees occur in the vertex determinant's special value, T1.4. |
| Universal cubic vertex Bass identity for every 2-complex | False on the four-vertex tetrahedron boundary. The universal replacement is the rational forbidden-transition Schur complement, T2.2–T2.4. |
| Building cubic has linear term minus undirected adjacency | It has $-A_1u$, with $qA_2u^2$ and $-q^3Iu^3$, T2.5. |
| Matching generalized-polygon link parameters characterizes cubic collapse | No such recognition/classification theorem is proved or assumed. Known building sufficiency and an algebraic obstruction are given; a full characterization remains unestablished, T2.5. |
| Odd eigenvalues themselves are exactly zeta zeros | Zeros are at reciprocals of signed eigenvalues, with net algebraic multiplicity after cancellation; zero eigenvalues give no finite divisor, T3.1. |
| Chamber roots are uncancelled zeros of the vertex $L$-function | Its reduced expression is $1/\det P_3$, so all those apparent numerator zeros cancel, T3.3. |
| $k$-cells literally realize $H^{k-1}$ with Weil weight $k-1$ | Only the parity exponents match. Flow-state dimensions and chamber radii disprove the literal interpretation, T3.4–T3.5. |
| The chamber weight-1 circle contains the whole odd sector | Principal series and part of type (e) give $q^{-1/2}$; type (e) also gives $q^{-1/4}$, and Steinberg gives radius 1. One-dimensional constituents give separate trivial roots, T3.5. |
| Vanishing order at $u^n=1$ is always ordinary or weighted Euler characteristic | For the building total it is $\chi-\operatorname{ord}\det P_n$; there is no such uniform Betti formula for the ordered default. Deitmar's degree insertion is a different theorem, T3.6–T3.7. |
| One pure fermion determinant and cell chirality automatically give the total supertrace | An ordinary Grassmann integral gives an ordinary determinant. The universal total realization is a ratio/Berezinian with auxiliary copies; chirality and flow superparity differ, T4.1–T4.3. |
| No polynomial multiplier could clear the rational total | Too broad as literally worded in T4.2, step <1>3; an arbitrary multiplier can clear it. The precise surviving obstruction is T8.1. |
| The building Laplacian is $(d+\delta)^2$ | $\delta^2$ need not vanish; the explicit doubled linearization uses $d\delta+\delta d$, T4.4–T4.5. |
| Adjoint pairing is needed for Kraus ring positivity | Complete positivity of the step maps suffices; arbitrary Kraus maps have the sum-of-squares trace formula, T5.3. |
| Positivity of a sequence alone excludes a rational numerator | False: $(1-u)/(1-2u)$. The no-go used here concerns an ordinary finite transfer trace, T5.4. |
| Arbitrary Kraus weights preserve the building scalar Euler/Hecke formula | Arbitrary weights preserve the Schur identity. An invertible flat local system is needed for the cochain/local cancellation proved here, T5.2/T5.8. |
| $E_{(g,gs)}=R(s)$ is flat in the forward chronological convention | It is generally not; the covariant convention is $R(s^{-1})$, or one must switch to pullbacks consistently, T5.5. |
| Full-cover connection equals a quotient representation block | False already on $C_4$ with a one-dimensional $\pi$. A covariant full-cover representation connection is pure gauge; Artin factors use quotient voltages, T5.5–T5.6. |
| $R=\pi\otimes\overline\pi$ embeds in a single regular representation | Only spectral support inclusion is automatic. Regular exponents are $d_\rho$; Artin exponents are $a_\rho$, T5.6/T6.2. |
| Euler factor is only trivial, or always $c^{\chi N^2/|G|}$ on the quantum block | The exact answer is the local-rotation product $F_R=\prod F_\rho^{a_\rho}$. The simple power requires freeness on unpointed simplices; stabilizers prevent fractional-power prescriptions, T5.7. |
| Scalar global determinant equality restricts automatically to every irreducible | It does not. Matrix identities and equivariant closed-path arguments restrict; scalar conjugate cancellations need bookkeeping, T3.5/T5.7. |
| Removing channel fixed points removes every building-trivial mode | Additional type characters may remain and violate the tempered bound. Remove the specified exceptional space, or assume it equals the fixed space, T6.1–T6.2. |
| Every nontrivial finite-group irrep “is tempered” | Temperedness belongs to the locally compact representation/the Hecke joint spectrum. The finite-group decomposition transfers that spectrum; it does not identify the two categories, H-LSV/T6.2. |
| One faithful $\pi$ detects Ramanujan | False even for a faithful character of a non-Ramanujan Cayley graph on 28 vertices. The exact criterion is support versus the set of bad blocks, T6.3. |
| General-rank Kang–Yu supplies factor-by-factor RH | The cited paper supplies the determinant identity. LLP/Kamber require their own stronger building spectral hypotheses and give one-sided information, T6.2/T6.4. |
| The quoted LLP condition literally says an invariant $|s|=1$ | The invariant peripheral condition is $\operatorname{Re}s=1$, with periodic imaginary part. The eigenvalue form removes the printed ambiguity, T6.4. |
| Kamber's upper eigenvalue bound is an upper bound on actual $u$-poles | It inverts: $|u|\geq q^{-(p-1)/p}$. The unambiguous source theorem is on $h_{\beta_i}$ eigenvalues, T6.4. |
| Higher-dimensional RH automatically has a duality | Vertex/principal-series factors have the stated anti-reciprocal symmetries. Type-(e) chamber multiplicities obstruct a single symmetry for that block; one-sided positivity allows interior modes, T6.5–T6.6. |
| A non-type-preserving Cayley quotient automatically satisfies the quoted type-preserving theorem | A separate cover/descent argument is required; T6.7 provides it under the explicit local and covering hypotheses. |
| Numerical chamber eigenvalue radius is $q^{3/4}$ when roots have radius $q^{-1/4}$ | The reciprocal eigenvalue radius is $q^{1/4}$. The observed $1.316074$ at $q=3$ agrees with this, T7.3. |
| A literature search finding no general/quantum zeta proves nonexistence | It does not. No such impossibility hypothesis is used. The exact finite obstructions proved here concern specific identities and conventions. |

<1>1. Each false algebraic assertion in the table has an explicit calculation, matrix proof, or counterexample at its listed location.

PROOF. The smallest recurring complexes are the single edge, the filled triangle and the tetrahedron boundary. The representation-block/full-cover distinction uses $C_4$; the faithful-only converse uses the stated $C_{28}$ Cayley graph. For a rigorous inequality in that last example, $\cos x\geq1-x^2/2$ and $\pi^2<10$ give its offending eigenvalue greater than $171/49>2\sqrt3$; the decimal values in T6.3/T7's sanity checks are not needed to establish failure.

<1>2. The statements called unestablished are not being counted as counterexample theorems.

PROOF. A full combinatorial characterization of low-degree vertex collapse, a canonical cohomological realization of flow weights, and a canonical self-adjoint Hilbert–Polya operator were not constructed. The given finite identities establish neither their existence nor their impossibility in all forms.

**Definition T8.3 (complete H-hypothesis register).** The following is the complete list of H-inputs used in this note, including the additional local-source inputs read in the repository. A citation to an H-input asserts only the statement and scope explicitly recorded with that input. No proof relies on an uncited “no such object exists” search conclusion.

Status: **conditional-on the listed source statements** wherever invoked; this register is provenance, not a new proof of those statements.

| Hypothesis | Content used | Citation addresses |
|---|---|---|
| H-POINT | Cyclic pointed facets, algebraic lengths, link opposition, successor types and quotient incidences | `2607.21262:main.tex:439-474`; `2607.21262:main.tex:479-534`; `2607.21262:main.tex:608-615`; `2607.21262:main.tex:1811-1846`; `2607.21262:main.tex:2235-2260` |
| H-LLP | Consecutively coloured unit bundles and geodesic flow; collision-free regular branching spectral bound; existence of interior poles | `1702.05452:rw_ramanujan_complex.tex:999-1027`; `1702.05452:rw_ramanujan_complex.tex:216`; `1702.05452:rw_ramanujan_complex.tex:229`; `1702.05452:rw_ramanujan_complex.tex:330-336` (definition); `1702.05452:rw_ramanujan_complex.tex:410-416` (RH corollary); `1702.05452:rw_ramanujan_complex.tex:487`; `1702.05452:rw_ramanujan_complex.tex:922-923`; `1702.05452:rw_ramanujan_complex.tex:1390-1424` |
| H-KL | Rank-three edge/chamber/vertex determinant identity, removal of lattice regularity assumption, four-way RH equivalence and $L$ normalization | `0804.2305:main.tex:215-260`; `0809.1401v1:main.tex:218-221`; `0809.1401v1:main.tex:244-247`; `0809.1401v1:main.tex:342-368`; `0809.1401v1:main.tex:1352-1370`; `0809.1401v1:main.tex:1410-1418`; `1505.00902:Zeta-and-Lfunction-20170426.tex:1134-1161` |
| H-KY | Type-preserving all-rank determinant theorem; deformed pointed cochains and null-homotopic Laplacians; individual $\Phi_i$ factors; signed primitive product | `2607.21262:main.tex:1971-1981`; `2607.21262:main.tex:2014-2026`; `2607.21262:main.tex:2175-2203`; `2607.21262:main.tex:2304-2312`; `2607.21262:main.tex:2320-2438`; `2607.21262:main.tex:2459-2487` |
| H-TORS | Hoffman's torsion interpretation; Knill's specified pseudodeterminants and tree interpretation; Hashimoto's vertex special-value formula | `2607.21262:main.tex:351-366`; `2201.09412:reidemeister.tex:42-52`; `2201.09412:reidemeister.tex:545-556`; `2310.15619:main.tex:950-955` |
| H-KL-TABLE | Used unitary representation rows, fixed-space dimensions, Steinberg multiplicities and representation-wise scalar cancellations | `0809.1401v1:main.tex:391-424`; `0809.1401v1:main.tex:1132-1154`; `0809.1401v1:main.tex:1171-1209`; `0809.1401v1:main.tex:1183-1186`; `0809.1401v1:main.tex:1425-1461` |
| H-RUELLE | Deitmar's exterior-power product and degree-weighted order in its specified coefficient cohomology; surface Ruelle parity and order | `dg-ga/9511006:main.tex:1153-1168`; `dg-ga/9511006:main.tex:1194-1212`; `1606.04560:zazi.tex:68-77`; `1606.04560:zazi.tex:843-855` |
| H-MO | Graph Dirac incidence/reversal matrix, Grassmann fields, two ordinary determinant evaluations, stated gamma-five hermiticity | `2501.08803:main.tex:630-648`; `2501.08803:main.tex:700-707`; `2501.08803:main.tex:750-755`; `2501.08803:main.tex:811-826`; `2501.08803:main.tex:192` |
| H-KY-LOCAL | Operator identity $\Phi_0=P_n$; $W,Q,J,\Sigma$ factorization, type filtration and closed-path intersection argument used for equivariance/flat coefficients | `2607.21262:main.tex:2516-2576`; `2607.21262:main.tex:2586-2640`; `2607.21262:main.tex:2930-2968`; `2607.21262:main.tex:2973-3091` |
| H-LSV | Colour-shift Hecke convention, commuting normality, precise tempered joint spectrum and type-trivial exceptions; explicit Ramanujan Cayley clique constructions and generators | `math/0406208:main.tex:541-572`; `math/0406208:main.tex:1437-1441`; `math/0406208:main.tex:1470`; `math/0406208:main.tex:1326-1358`; `math/0406208:main.tex:1408-1418`; `math/0406208:main.tex:1436-1478`; `math/0406217:main.tex:497-515`; `math/0406217:main.tex:676-682`; `math/0406217:main.tex:2617-2626`; `math/0406217:main.tex:1407-1415`; `math/0406217:main.tex:1673-1686` |
| H-STRONG | LLP's Iwahori-spherical Ramanujan hypothesis; stronger scope and applicability to the stated LSV explicit examples | `1702.05452:rw_ramanujan_complex.tex:196-214`; `1702.05452:rw_ramanujan_complex.tex:674-701` |
| H-KAMBER | Normalized Bernstein–Lusztig eigenvalue criterion, its determinant zeta, and building/strong-Ramanujan scope | `1701.00154:L_p_Expander_Complexes.tex:130-165`; `1701.00154:L_p_Expander_Complexes.tex:334-358`, especially `1701.00154:L_p_Expander_Complexes.tex:345-350`; ambiguous pole wording separately recorded at `1701.00154:L_p_Expander_Complexes.tex:359-363` |
| H-COVER | Contractibility, torsion-free free action, type character and preservation of cyclic local data | `1702.05452:rw_ramanujan_complex.tex:196-214`; `2607.21262:main.tex:439-474`; `2607.21262:main.tex:1724-1738`; `2607.21262:main.tex:2014-2019`; `math/0406208:main.tex:1334-1358` |

<1>1. The finite linear-algebra inputs used without an H-label are proved in the note or explicitly allowed in the question.

PROOF. Schur complements and Sylvester are allowed; cochain cancellation is T1.1; the finite-group decomposition and multiplicities are justified in T5.6; the ring trace identity is T5.3; the finite Weil-positivity distinction is reproved in T6.6. The earlier notebook's arbitrary-weight graph theorem and positivity note were read as requested, but the corresponding statements used here have their own proofs. The formal Grothendieck–Lefschetz sign convention is the comparison supplied in the question, not a theorem asserting that the cell spaces are arithmetic cohomology.

<1>2. Computational evidence is kept separate from these H-inputs.

PROOF. Exact small-state polynomial checks, exact arbitrary rational-matrix Schur checks on a triangle with a pendant edge, and the elementary $C_{28}$ eigenvalue check were run with inline `timeout 60 python3` commands; no scratch script or other file was created by this author. The existing numerical lane's output was only read. Its finite-series checks and reported spectra do not strengthen any theorem's status beyond the proofs and explicitly assumed source results above.

RESULT: **proved-here** — the ordered graded geodesic determinant, universal arbitrary-weight Bass–Schur and auxiliary Berezinian identities, cochain determinant cancellation, Kraus trace/primitive-product positivity, exact finite-group multiplicity and converse criteria, finite duality/positivity algebra, and the small-complex counterexamples; **conditional-on H-*** — pointed building identification, Kang–Li/Kang–Yu Hecke and torsion formulas, their equivariant/flat-coefficient and type-cover consequences, LSV quantum spectral transfer, rank-three factor RH and LLP/Kamber one-sided RH; **sketched/unestablished** — a combinatorial characterization of low-degree vertex collapse beyond the stated building class and a canonical cohomological/Hilbert–Polya realization; **FALSE-as-drafted** — the ordered/building identifications, universal cubic collapse, uncancelled chamber-zero and literal cohomology/chirality claims, unrestricted full-cover/isotypic and scalar Euler-factor twist claims, fixed-point-only and faithful-only Ramanujan transfer claims, unsourced all-rank factor RH and universal duality claims, and the overbroad polynomial-multiplier obstruction qualified in T8.1.
