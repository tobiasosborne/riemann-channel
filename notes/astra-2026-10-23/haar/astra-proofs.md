# Lane H: exact Haar averages of twisted characteristic polynomials

Author: `codex:gpt-6-astra`, 2026-10-23.

Research record; nothing registered. Statements below distinguish proofs, cited theorems, and numerical checks.

## 0. Setting and gauge fixing — PROVED

Use finite connected **simple** graphs and continuous finite-dimensional unitary representations. Except for an explicitly noted degenerate case, the regular degree is at least two, so q >= 1. Write n=|V|, m=|E|, g=m-n+1, and d=dim rho. The average has degree nd, with no factor removed from individual characteristic polynomials.

**Gauge-fixing lemma.** The average of any gauge-invariant integrable function under independent Haar labels on all m unoriented edges equals its average with every spanning-tree label equal to 1 and g independent Haar cotree labels. Root the tree, set the gauge at its root equal to 1, and recursively choose vertex gauges so that t_u s_uv t_v^{-1}=1 on tree edges. Conditional on all tree labels, the transformed cotree labels are independent Haar, by left/right invariance. The adjacency changes by conjugation with diag(rho(t_v)), proving the assertion for its determinant. The remaining simultaneous conjugation of all g holonomies does not change this function. Thus G^g is a convenient integration space, not literally the nonabelian gauge quotient; that quotient is G^g/G.

For every nontrivial one-dimensional character, the average is exactly the degree-n matching polynomial mu_Y, including when its image is Z_N for N>=2. Independent edge averaging kills each simple-cycle factor in the scalar determinant expansion, leaving dimers. This agrees with `notes/adelic-gkp/zn-flux.md`, Theorem 4.1. The trivial **representation summand** is absent in this setup; the trivial **flux assignment** is included in the average. In particular, no x-(q+1) factor is divided out at that assignment.

## 1. H2 — SHARPENED: an exact exterior-moment polynomial

**REFUTED as phrased:** a scalar weight per base-graph cycle does not describe a general representation, and the polynomial need not contain only powers of parity nd. The exact replacement below is **PROVED**. Its raw permutation version uses full mixed matrix moments; antisymmetrization reduces the necessary data to finitely many exterior-power moments.

### 1.1 Permutations, walks, and the actual independence

Put Omega=V x [d]. For a permutation pi of Omega, retain it only if every moved index (u,i) goes to (v,j) with uv an edge. Let f(pi) be its number of fixed points and c(pi) its number of nontrivial permutation cycles. With independent edge labels,

$$p_{Y,\rho}(x)=\sum_\pi (-1)^{c(\pi)}x^{f(\pi)}
 \prod_{e\in E} M_e(\pi),\tag{1}$$

where, writing e=u->v, the exact factor is

$$M_e(\pi)=\int_G
 \prod_{\pi(u,i)=(v,j)}\rho(h)_{ij}
 \prod_{\pi(v,k)=(u,l)}\overline{\rho(h)_{lk}}\,dh.\tag{2}$$

This is just the Leibniz determinant formula: the sign of a moved cycle of length l, including its l minus signs from xI-A, is -1. It is already an algorithm for any compact group whose representation moments are known. For a finite group, every integral is the exact average of its summand over G.

The permutation cycles are simple on Omega; their projections can revisit base vertices, share base edges, and branch in their union. Their Haar integrals therefore **cannot** be multiplied independently. In particular, a projected trail u->v->w->v->u can use different colors at its repeated vertices. The even-power ansatz holds if Y is bipartite, or if -I belongs to rho(G), since then A and -A have the same law. It is not a general consequence of irreducibility. The SO(3)/A5 K4 polynomial in Section 4 has a nonzero x^3 coefficient.

An equivalent closed-walk form, useful with nonabelian holonomy, is the formal identity

$$p(x)=x^{nd}\left[\mathbb E\exp\left(-\sum_{l\ge1}
 \frac{t^l}{l}\sum_{w\in W_l}\chi_\rho(s(w))\right)\right]_{t=1/x},\tag{3}$$

where W_l consists of rooted oriented closed walks of length l. Expanding the exponential gives the coefficient of t^r as a sum over tuples (a_l) with sum l a_l=r, weighted by product (-1)^{a_l}/(a_l! l^{a_l}), of the **joint** expectations of products of walk characters. Coefficients beyond nd cancel. Equation (3) does not replace joint expectations by products of expectations.

For U(d), the raw balanced moments in (2) are

$$\int\prod_{a=1}^r U_{i_a j_a}\prod_{a=1}^r\overline{U_{k_a l_a}}
 =\sum_{\sigma,\tau\in S_r}\prod_a\delta_{i_a,k_{\sigma(a)}}
 \prod_a\delta_{j_a,l_{\tau(a)}}\operatorname{Wg}_d(\sigma^{-1}\tau).\tag{4}$$

Unbalanced moments vanish by the central U(1). At r=1 this is Schur orthogonality, delta_ik delta_jl/d. At d=r=2, Wg(id)=1/3 and Wg((12))=-1/6. For r>d the generalized inverse formulation of Weingarten calculus is understood. Here a single edge contributes at most d entries in each direction.

### 1.2 The smaller data set: exterior-power kernels

For subsets I,J of [d] of size a and K,L of size b, set

$$K_\rho^{ab}(I,J;K,L)=\int_G
 (\Lambda^a\rho(h))_{I,J}\overline{(\Lambda^b\rho(h))_{K,L}}\,dh,
 \qquad 0\le a,b\le d.\tag{5}$$

**PROVED:** these kernels alone determine p on every simple graph. A fully specified minor expansion is as follows. Order the symbols 0 and all oriented edges. Partition Omega into row sets R_0,R_e and into column sets C_0,C_e; require R_0=C_0=F, R_e contained in the colors at the tail of e, C_e in the colors at its head, and |R_e|=|C_e|=r_e. Each set is internally increasingly ordered. Let epsilon be the product of the signs of the row and column concatenation permutations. Then

$$p(x)=\sum_{(R,C)}\epsilon(R,C)(-1)^{\sum_e r_e}x^{|F|}
 \prod_{e=u\to v\in E^+}
 K_\rho^{r_e,r_{\bar e}}(R_e,C_e;C_{\bar e},R_{\bar e}),\tag{6}$$

with local color indices understood in the kernels. To prove (6), group the Leibniz terms by their row/column allocation to the directed blocks and diagonal. The alternating sums within each block are minors. The reverse block is U*, so its minor is the conjugate minor with exchanged index sets. Independence then gives (5). This also proves the representation-equivalence reductions used in Section 4.

Thus full moment data are sufficient, but substantially more than necessary. The scalar numbers m_k=integral chi(h^k) do not supply the joint matrix-coefficient contractions needed in (6); no sufficiency assertion about that scalar sequence is being used. The relevant finite data are the projectors/intertwiners in Lambda^a rho tensor conjugate(Lambda^b rho), in compatible exterior bases.

### 1.3 U(d), and the correct Hall–Puder–Sawin index

Suppose Lambda^0 rho,...,Lambda^d rho are irreducible and pairwise nonisomorphic (property P1). Schur orthogonality gives

$$K_\rho^{ab}(I,J;K,L)=\frac{\delta_{ab}\delta_{IK}\delta_{JL}}{\binom da}.\tag{7}$$

In (6) this forces equal edge multiplicities in both directions, and identical row/column subsets at each endpoint. For k_e in {0,...,d}, put s_v=sum_{e incident v} k_e and |k|=sum_e k_e. Only s_v<=d are allowed. The result is

$$p_{Y,\rho}(x)=\sum_k(-1)^{|k|}x^{nd-2|k|}
 \frac{\prod_v(d)_{s_v}}{\prod_e k_e!\,(d)_{k_e}}
 =:\mu_{d,Y}(x),\qquad(d)_r=\frac{d!}{(d-r)!}.\tag{8}$$

For clarity, the weight can also be derived without sign bookkeeping. In a random d-cover choose s_v distinct sheet vertices at v, allocating k_e of them to edge e. There are (d)_{s_v}/product_{e incident v} k_e! allocations. Across an edge, the probability of matching the prescribed two k_e-subsets is k_e!/(d)_{k_e}. Multiplication gives exactly (8). Thus mu_{d,Y} is the average **matching** polynomial of d-covers.

The defining U(d) representation satisfies P1: its exterior powers are irreducible and the center acts on the a-th power by z^a, making them distinct. Hence its Haar average is (8). For S_r standard the dimension is r-1, so its averaged new characteristic polynomial is mu_{r-1,Y}, not mu_{r,Y}. In particular the comparison for U(2) is **S3 standard / new part of a 3-cover**; the new part of a 2-cover gives mu_{1,Y}.

**PROVED, using a cited theorem:** Hall, Puder and Sawin, *Ramanujan coverings of graphs* (Advances in Mathematics 323, 2018), Theorems 1.8 and 2.7, Remark 1.12 and Corollary 5.6, identify this average and show that mu_{d,Y} has only real roots in the universal-cover band for loopless Y. Thus the entire U(d) subcase of H1 is a known theorem. [Author manuscript, 2016](https://www.ias.edu/sites/default/files/math/csdm/15-16/HallPuSa2016.pdf). The source was not found in `refs/src/`; no local line citation is invented.

### 1.4 SU(2): a sum of squares on every simple graph

**PROVED.** For the defining representation of SU(2), or any subgroup whose defining two-dimensional representation remains irreducible,

$$\boxed{\displaystyle p_Y^{\rm sp}(x)=
 \sum_{\mathcal C}\mu_{Y\setminus V(\mathcal C)}(x)^2,}\tag{9}$$

where C ranges over all collections of vertex-disjoint unoriented simple cycles of length at least three, including the empty collection. This is an exact character integration, and also explains all the Q8/2T/2O computations.

Here is a proof including the square-root determinant step. Let J be block diagonal with blocks [[0,1],[-1,0]]. For H=xI-A, quaternionic self-duality gives HJ=JH^T, so HJ is antisymmetric. The monic polynomial Q_s(x)=Pf(HJ) satisfies Q_s(x)^2=det(H), since det J=1. It is real: conjugation preserves its square and its leading coefficient, so it preserves Q_s. In the Pfaffian expansion each base vertex has two half-indices. A diagonal pairing gives x; non-diagonal pairings project to a doubled edge or to a simple cycle, with different components vertex-disjoint. A doubled edge has weight -det U=-1. The two orientations of a longer cycle sum to -tr rho(s(C)). The sign can be checked on one cycle after gauging all but one of its edges to the identity. Consequently

$$Q_s(x)=\sum_{\mathcal C}(-1)^{|\mathcal C|}
 \mu_{Y\setminus V(\mathcal C)}(x)
 \prod_{C\in\mathcal C}\operatorname{tr}\rho(s(C)).\tag{10}$$

This is the quaternionic Moore-determinant expansion, derived here from its Pfaffian realization. Average its square using independent labels on **all** edges. If two cycle collections have different edge unions, an edge occurs in exactly one product and has a factor linear in rho(h) or its conjugate; its integral is zero. Equal edge unions determine the same collection. For that collection the cycles are edge-disjoint, their holonomies are independent Haar, and each real irreducible character has integral chi^2=1. Every surviving sign is positive, yielding (9). This proof uses only irreducibility and determinant-one two-dimensional unitarity, not all raw SU(2) moments.

On K4 let mu=x^4-6x^2+3. There are four triangles (each leaves one vertex), three four-cycles (each leaves the empty graph), and no disjoint pair of cycles. Therefore

$$\boxed{p_{K4,\mathrm{SU}(2)}=\mu^2+4x^2+3
 =x^8-12x^6+42x^4-32x^2+12.}\tag{11}$$

In the three star-tree cotree variables a,b,c, (10) is mu-xT-F. Here T is the sum of the four triangular traces tr a, tr b, tr c, tr(acb^{-1}); F is the sum of tr(ac), tr(bc^{-1}), tr(a^{-1}b). Exact character integration gives E T=E F=E TF=0, E T^2=4, E F^2=3. This provides the requested direct three-variable calculation.

Equation (8), with d=2, gives

$$\boxed{p_{K4,\mathrm U(2)}=\mu_{2,K4}
 =x^8-12x^6+42x^4-40x^2+6.}\tag{12}$$

Neither polynomial equals mu or mu^2. Script `checks/haar_weingarten.py` computes both, independently verifies (12) by summing all 216 S3 holonomy tuples in an integral standard-representation basis, and verifies (11) by summing all 512 Q8 tuples. For Q8 it uses an integer realification, takes the exact monic square root of each realified characteristic polynomial, and squares it back as a certificate. The output is `checks/output_weingarten.txt`.

## 2. H1 — REFUTED

Already the triangle C_3 (q=1), SU(2), and its defining irreducible representation give

    p(x) = (x^3-3x)^2+1.

Gauge fixing leaves one Haar holonomy h. With D=x^3-3x, the characteristic polynomial is (D-tr h)^2. The character has mean zero and squared mean one by irreducibility and its real character. Hence p is strictly positive on the entire real axis, and all six roots are nonreal. Exactly the same calculation holds for the faithful two-dimensional representation of Q_8. This is minimal in vertex count among connected simple regular graphs of degree >=2, and in representation dimension under that degree restriction. An exact script and root certificates follow below.

If q=0 is admitted literally, K_2 is an even smaller but degenerate counterexample: p=(x^2-1)^d, whereas the stated band is {0}. The standard 2 sqrt(q) tree-band formula must exclude this case (the universal cover is the finite edge, of spectral radius 1).

For cubic graphs, K4 is the smallest simple example. Equation (11) is at least 3 on the real line, so **all eight roots are nonreal**. One is approximately 2.368004478439+0.207526808432 i; the check also prints rational complex isolating rectangles. The triangle has a certified imaginary root i y, where y is the unique root of y^3+3y-1 in (8/25,33/100): the endpoint values are -113/15625 and 25937/1000000, and the derivative is positive. No numerical root solver is needed to refute H1.

Q8 is also minimal in **finite-group order** for this nondegenerate simple-graph counterexample. All groups of order below eight are abelian except S3. Their nontrivial irreducibles are one-dimensional, or S3 standard, and these satisfy the matching-polynomial theorem. Q8 has its faithful irreducible doublet of determinant one, and (11) applies. This minimality statement excludes the q=0 defect already noted.

If loops are allowed, an even smaller counterexample is one vertex with one loop, degree two: A=h+h*=tr(h) I_2, giving p=x^2+1 for SU(2) and Q8. If parallel edges are allowed, the cubic graph with two vertices and three parallel edges gives p=(x^2-3)^2+3. The primary minimality claims above use the simple-graph convention of the requested examples; they are not claims about all graph conventions.

### A stronger obstruction — PROVED

For any ensemble of monic real polynomials Q of fixed degree whose roots are real, **E Q^2 is real-rooted if and only if Q is almost surely constant as a polynomial**. Indeed, E Q^2 is nonnegative on the real axis, so all its real roots have even multiplicity. A zero of multiplicity 2r forces Q,Q',...,Q^(r-1) to vanish there almost surely: divide out successive common linear factors and evaluate the remaining expected square. If all roots are real, these common factors account for the whole degree of Q, making its monic polynomial deterministic. The converse is immediate.

An irreducible quaternionic representation admits an antiunitary J_rho with square -1 commuting with its image. Thus I_n tensor J_rho commutes with A_s, Kramers pairing makes det(x-A_s)=Q_s(x)^2, and Q_s is monic real-rooted. On any graph with a cycle this characteristic polynomial varies with the field. To see this, choose an edge on a shortest cycle of length l, put all other labels equal to 1, and vary this edge label h. Backtracking length-l walks have constant trace; simple length-l cycles through this edge change Tr A^l by a positive integer multiple of Re chi(h)-d. This is nonzero for some h in a nontrivial representation. Continuity and full support of Haar ensure nonconstancy on sets of positive measure. The preceding lemma applies.

Consequently **every nontrivial quaternionic irreducible representation fails real-rootedness on every finite simple graph containing a cycle**. This includes every half-integer spin representation of SU(2). For the doublet, (9) gives the sharper explicit statement: its average is real-rooted exactly when Y is a forest. On a forest there are no holonomies and p=mu_Y^2; when a cycle exists the nonzero lower-degree square in (9) prevents real-rootedness by the same lemma. For the regular graphs of degree at least two in this lane, failure is therefore universal in the quaternionic class.

A surviving positive statement is the P1 criterion of Section 1.3. In dimension two it gives a complete dichotomy for nontrivial irreducible unitary rho on a cyclic simple graph: if det rho is nontrivial, p=mu_{2,Y} and is in-band; if det rho is trivial, the image lies in SU(2) and p is not real-rooted.

## 3. H3 — PROVED for the loopless regular setting, q >= 1

The finite-d band assertion follows from Section 1.3. The root empirical measures also converge to Kesten–McKay. The following argument supplies the additional step concerning **expected polynomials**, rather than inferring it from convergence of random spectra.

Write the roots of mu_{d,Y} as lambda_{d,1},...,lambda_{d,nd}. Let a_k count rooted length-k closed walks in Y whose lift to the universal cover is closed. If t_k is the number of closed walks of length k from a vertex of the (q+1)-regular tree, then a_k=n t_k. We will prove

$$\sum_{j=1}^{nd}\lambda_{d,j}^k=d a_k+O_{Y,k}(1).\tag{13}$$

Use the exact equality of polynomials with the S_{d+1} standard representation, and put r=d+1. Gauge-fix g independent uniform permutations sigma_i in S_r. For a closed base walk w, let w(sigma) be its free-group holonomy word. Tr std(w(sigma)) is d when w is trivial, and Fix(w(sigma))-1 otherwise. Consequently

$$\operatorname{Tr}(A_{\rm new}^k)=d a_k+R_{k,d},\qquad
R_{k,d}=\sum_{w\in W_k,\ w\ne1}\big(\operatorname{Fix}(w(\sigma))-1\big).\tag{14}$$

**Bounded-moment lemma — PROVED.** For any fixed finite list of nontrivial free words, all fixed-order joint moments of their fixed-point counts are bounded uniformly as r tends to infinity. Expand a product of fixed-point counts by trajectories of their starting sheet indices. There are finitely many index-identification patterns at a fixed total word length. A consistent pattern with v distinct sheet indices and e distinct directed permutation constraints has at most (r)_v embeddings and probability product_i 1/(r)_{e_i}, where e=sum_i e_i; inconsistent partial bijections have probability zero. In the colored constraint multigraph every connected component contains a nontrivial reduced closed walk, hence a cycle, so e>=v. Each contribution is O(r^{v-e})=O(1). The finitely many small r are harmless. This also proves uniformly bounded joint moments of any fixed collection of R_{k,d}.

Now work with formal power series only; no exchange of analytic limits is required. With

$$\widetilde p_d(t)=t^{nd}p_{Y,U(d)}(1/t)
=\mathbb E\det(I-t A_{\rm new}),$$

the determinant/traces identity and (14) give

$$\log\widetilde p_d(t)
=-d\sum_{k\ge1}\frac{a_k}{k}t^k
 +\log\mathbb E\exp\left(-\sum_{k\ge1}\frac{R_{k,d}}k t^k\right).\tag{15}$$

For every fixed K, each coefficient through degree K of the last logarithm is bounded uniformly in d: it is a fixed polynomial in joint moments of finitely many R's, and the series inside that logarithm has constant coefficient 1. On the other hand log p-tilde=-sum_k (sum_j lambda_{d,j}^k)t^k/k. Comparing coefficients proves (13).

All roots lie in the same compact real interval by HPS. Thus convergence of every moment implies weak convergence of their empirical measures, and the limiting moments t_k determine the tree spectral measure. Its density is

$$\boxed{\displaystyle \frac{q+1}{2\pi}
 \frac{\sqrt{4q-z^2}}{(q+1)^2-z^2}\,mathbf1_{|z|<2\sqrt q}\,dz.}\tag{16}$$

At q=1 this is the arcsine density 1/(pi sqrt(4-z^2)). This proves all of H3 under the graph convention stated in Section 0; it uses the established HPS theorem and the bounded-moment argument, and does not assume RH.

For a direct identification of the density, the forward-subtree Green function satisfies h(z)=1/(z-q h(z)), with h(z)~1/z at infinity. The rooted tree Green function is M(z)=1/(z-(q+1)h(z)). Solving the quadratic and taking -Im M(z+i0)/pi gives (16), with its Laurent coefficients equal to the closed-walk counts t_k.

`checks/haar_limit.py` checks exact root moments on K4 at d=1,2,4,8,16. For example, the sixth normalized moment is 87-6/d, tending to the tree value 87. The script also computes the exact U(3) Petersen polynomial and isolates all its 30 roots in the band; its largest root is approximately 2.729781416865.

### What strong convergence does, and does not, give

**PROVED, cited results.** Bordenave and Collins, *Eigenvalues of random lifts and polynomials of random permutation matrices* (Annals of Mathematics 190, 2019), prove strong convergence in probability for independent permutations on the complement of constants. The local source is `refs/src/1801.00876/tenseur9.tex`, lines 343–358; its application to random lifts is at lines 534–536. For independent Haar unitaries the appropriate earlier citation is Collins and Male, *The strong asymptotic freeness of Haar and deterministic matrices* (Ann. Sci. ENS 47, 2014); Bordenave–Collins explicitly distinguish it at lines 312–318. [Collins–Male publication](https://www.numdam.org/articles/10.24033/asens.2211/).

Applied to the fixed matrix-valued adjacency polynomial, these results give convergence of the random spectral measure to (16), and asymptotic confinement of the random spectra to arbitrarily small enlargements of the tree band. They do not give exact finite-d confinement, or real-rootedness of an expectation of characteristic polynomials. In particular E log det is not log E det.

**PROVED elementary warning example.** Let B_N be the zero matrix with probability 1-exp(-N), and a I_N with probability exp(-N), where a>0 is fixed. These matrices converge strongly to zero almost surely (the exceptional probabilities are summable), whereas

$$\mathbb E\det(xI-B_N)=(1-e^{-N})x^N+e^{-N}(x-a)^N.$$

For even N this is strictly positive for every real x, hence not real-rooted. Its roots satisfy |x/(x-a)|=(e^{-N}/(1-e^{-N}))^{1/N}, which tends to e^{-1}, so their measures do not tend to delta_0 either. Strong convergence alone is insufficient even for the limiting expected-polynomial root measure. Equations (13)–(15) are the missing control in this lane.

## 4. H4 — finite-group RH REFUTED; all requested cases computed exactly

**PROVED:** the finite average is |G|^{-g} sum_{h in G^g} det(x-A_h). Equations (5)–(6) allow its replacement by a smaller group with the same exterior kernels. This removes the proposed exponential bottleneck in all requested cases, including A5 and Petersen.

| Representation(s) | Exact replacement, for every simple Y | Reason |
|---|---|---|
| Q8 faithful 2; 2T defining 2; 2O defining 2 (also its sign twist) | SU(2) defining; equation (9) | Lambda^0=Lambda^2=1, Lambda^1 irreducible; the same determinant-one and Schur kernels |
| S3 standard 2; the other two faithful 2T doublets | U(2); equation (8) with d=2 | Lambda^0, Lambda^1, Lambda^2 are irreducible and pairwise distinct |
| Both A5 three-dimensional irreps | SO(3) defining = SU(2) spin 1 = tetrahedral A4 rotations | Lambda^0=Lambda^3=1; Hodge star identifies Lambda^1 and Lambda^2; Schur kernels have weight 1/3 |

The statement about 2T requires a correction to the brief. Its three faithful doublets are rho_0 tensor eta^j, j=0,1,2, where eta is a character of its quotient C3. Only j=0 has determinant one. For j=1,2, det(rho_0 tensor eta^j)=eta^{2j} is nontrivial, so the two twisted images lie in U(2) and satisfy P1. Their faithfulness follows because a kernel element would have scalar rho_0-image, hence be +/-1, while eta(-1)=1. Therefore **the same finite group on the same graph has both outcomes, depending on the irrep**.

For the A5 reduction, choose real orthonormal bases of either three-dimensional irrep and an orientation. Their images lie in SO(3). The oriented Hodge-star map identifies the two middle exterior powers with the same three-dimensional irreducible action; the remaining exterior powers are trivial. These facts fix every kernel (5), including the off-diagonal 1<->2 and 0<->3 kernels. The tetrahedral rotation group A4 has exactly the same kernels in its defining representation. The script enumerates this A4 as the twelve integral matrices obtained from cyclic coordinate permutations and even diagonal sign changes. It sums characteristic polynomials with FLINT integer arithmetic, grouping holonomy tuples by simultaneous conjugation. It therefore computes the **exact A5 average**, not a sample or a spherical-design approximation.

All four graphs have q=2. In the next table, the count is the number of real roots including multiplicity; **every real root counted is certified inside the band**. A missing real root means failure of H1.

| Graph | n, g | Q8 / untwisted 2T / faithful 2O | S3 / twisted 2T | A5, either 3 |
|---|---|---|---|---|
| K4 | 4, 3 | 0/8, FAIL | 8/8, PASS | 4/12, FAIL |
| K3,3 | 6, 4 | 0/12, FAIL | 12/12, PASS | 10/18, FAIL |
| cube | 8, 5 | 0/16, FAIL | 16/16, PASS | 16/24, FAIL |
| Petersen | 10, 6 | 0/20, FAIL | 20/20, PASS | 20/30, FAIL |

**Exact polynomial table for the doublets.** Each row lists coefficients of P(y) in descending powers, where p(x)=P(x^2). These are integers, not rounded coefficients.

| Y | Q8 / untwisted 2T / faithful 2O | S3 / twisted 2T |
|---|---|---|
| K4 | [1,-12,42,-32,12] | [1,-12,42,-40,6] |
| K3,3 | [1,-18,117,-336,441,-234,51] | [1,-18,117,-336,423,-198,21] |
| cube | [1,-24,228,-1096,2844,-3960,2828,-912,126] | [1,-24,228,-1096,2832,-3864,2556,-672,42] |
| Petersen | [1,-30,375,-2540,10155,-24450,34595,-26640,9345,-790,57] | [1,-30,375,-2540,10155,-24474,34815,-27360,10335,-1370,27] |

For example, the A5/SO(3) K4 polynomial is

$$x^{12}-18x^{10}+117x^8-332x^6+393x^4-16x^3-158x^2-\frac{11}{9}.\tag{17}$$

This explicitly refutes H2's parity ansatz. One of its nonreal roots is approximately 1.009829519919+0.210409009232 i. The exact polynomials for **every** row, and **all** roots to twelve decimal places, are printed in [`checks/output_finite.txt`](checks/output_finite.txt); the rational coefficient vectors are also in `checks/output_finite.json`. Root decimals are approximations, but real-root counts and band containment use exact rational isolating intervals (width at most 10^-20). The SU(2) no-real-root verdicts have the additional sum-of-squares certificates: their numbers of spanning cycle collections are respectively 3,6,9,6, giving positive lower bounds for p on the entire real axis.

The A4 calculation reduces 12^g tuples to 178, 1846, 21154, and 250342 representatives respectively, with exact orbit weights summing to 1728, 20736, 248832, and 2985984. This evaluates the A5 Petersen case without attempting 60^6 determinants. No finite-group result in the table relies on floating-point arithmetic.

`checks/haar_kernels.py` independently builds Q8, 2T, and 2O as explicit quaternion matrices. It checks their full six-by-six kernels (5) in exact arithmetic, including both 2T twists, and checks the quotient character on all products in 2T. Its output is `checks/output_kernels.txt`.

## 5. Numerical experiment — NUMERICAL, not a proof

`checks/haar_mc.py` ran **100000 independent samples for each of the eight requested cases**, with fixed recorded seeds. SU(2) uses normalized four-dimensional Gaussians (uniform unit quaternions); spin 1 uses the induced SO(3) rotation; U(2) and U(3) use complex Gaussian QR with diagonal phase correction. Cotree holonomies are independent. The code computes Hermitian eigenvalues in double precision and polynomial coefficients in long double, accumulating the mean and full covariance by a centered, stable batch update.

The trace and quadratic coefficients are deterministic and set exactly. For the defining U(d) and SU(2) doublet ensembles, A -> -A invariance allows exact symmetrization of each sample polynomial, removing its odd coefficients. This is an unbiased variance reduction. It is **not** applied to spin 1. Standard errors refer to these symmetrized estimators where applicable.

| Y | Representation | Largest absolute imaginary part of estimated roots | Largest absolute real part | Largest coefficient deviation / its SE |
|---|---|---|---|---|
| K4 | U(2) | 0 | 2.522916689259 | 1.6013 |
| K4 | SU(2), spin 1/2 | 0.298436007284 | 2.368330496746 | 0.9649 |
| K4 | SU(2), spin 1 | 0.209231574057 | 2.643441185775 | 1.0296 |
| K4 | U(3) | 0 | 2.600768944820 | 1.6554 |
| Petersen | U(2) | 0 | 2.700491573814 | 0.5698 |
| Petersen | SU(2), spin 1/2 | 0.154117208536 | 2.645504831205 | 1.7510 |
| Petersen | SU(2), spin 1 | 0.056087942979 | 2.738327666719 | 2.0404 |
| Petersen | U(3) | 0 | 2.729822705316 | 0.9604 |

Every row now has an exact comparison polynomial, including U(3) Petersen from `haar_limit.py`. The final column ranges over coefficients with non-negligible estimated SE. It is a diagnostic, not a familywise hypothesis test.

All coefficients, their pointwise standard errors, and every estimated root with **95% coordinate intervals** are in [`checks/output_mc.txt`](checks/output_mc.txt). These intervals use 500 Gaussian resamples of the coefficient mean with its **full covariance**, followed by minimum-distance assignment of resampled roots to the estimated roots. They are statistical approximations, not certified disks or simultaneous confidence regions. They can lose their interpretation at root collisions and exclude floating-point error. For example, the largest positive K4 U(2) root has estimated interval [2.522093910636,2.523666866423], containing its exact value 2.523255734295. The exact refutations and band verdicts do not rely on any of these Monte Carlo intervals.

To reproduce all outputs, run from `notes/astra-2026-10-23/haar` (the JSON outputs let the last command compare against the exact polynomials):

```sh
OPENBLAS_NUM_THREADS=1 python3 checks/haar_weingarten.py > checks/output_weingarten.txt
OPENBLAS_NUM_THREADS=1 python3 checks/haar_finite.py > checks/output_finite.txt
python3 checks/haar_kernels.py > checks/output_kernels.txt
OPENBLAS_NUM_THREADS=1 python3 checks/haar_limit.py > checks/output_limit.txt
OPENBLAS_NUM_THREADS=1 python3 checks/haar_mc.py --samples 100000 > checks/output_mc.txt
```

Dependencies: Python 3, NumPy, SciPy, SymPy, NetworkX, python-flint. Exact computations use rational/integer arithmetic; real-root isolation is exact, with 30-digit complex approximations printed to 12 decimal places. The additional complex rectangles in the K4 certificate have rational endpoints. No assumption about RH or any numerical zeta/L-function zero enters a computation.

## Correction ledger

| Brief or notebook assertion | Correction and status |
|---|---|
| RH on average for every compact group / every finite group | **REFUTED:** SU(2) and Q8 already fail on C3; K4 is a cubic counterexample. Every quaternionic irrep fails on every cyclic simple graph. |
| U(d) has no known Heilmann–Lieb analogue here | **SHARPENED:** the average is exactly the HPS d-matching polynomial; the finite-d in-band theorem is already known. |
| S_d standard gives the d-matching polynomial | **CORRECTED:** it gives the (d-1)-matching polynomial. The index of the matching polynomial is representation dimension, not cover degree. |
| Cycle weights can be integrated independently | **REFUTED:** shared edges couple projected walks. The exact replacement is the edge tensor contraction (6). |
| Only powers x^(nd-2k), with positive combinatorial coefficients | **REFUTED in general:** SO(3)/A5 on K4 has an x^3 term; even the C3 SU(2) constant violates the naive alternating-positive ansatz. |
| All faithful 2T doublets are SU(2) subgroups | **CORRECTED:** the two nontrivial character twists have nontrivial determinant and the U(2) average. |
| Full raw moments are required | **SHARPENED:** the finite exterior-power kernels (5) suffice. This permits exact reduction from A5 to A4 and from binary polyhedral groups to SU(2)/U(2) formulas. |
| Bordenave–Collins (2019) alone gives H3 | **CORRECTED:** it concerns permutation strong convergence; Haar unitaries use Collins–Male (2014). Neither alone controls roots of expected polynomials. Section 3 supplies that step. |
| “Trivial mode gone” in the Z_N average | **CLARIFIED:** there is no trivial representation summand, but the zero flux is included and nothing is removed from its determinant. N>=2 is essential. |
| The band formula covers every regular degree | **CORRECTED:** q=0 is exceptional; K2's universal cover is itself and has spectral radius 1, not 0. Minimality also depends on whether loops/parallel edges are allowed. |
| HPS implies two-sided Ramanujan covers of every graph | **CORRECTED:** its general existence statement is one-sided; bipartiteness upgrades it to two-sided. The average polynomial itself has all roots in the two-sided band. |

The classical citations requested in the brief are Godsil and Gutman, *On the matching polynomial of a graph* (1981), for the signing average, and Heilmann and Lieb, *Theory of monomer-dimer systems* (1972), for matching-polynomial real-rootedness and the regular-tree root bound. These attributions were recalled from memory and the bibliographic data checked; the scalar determinant argument is supplied in Section 0. The separate Godsil–Gutman paper *On the theory of the matching polynomial* is also from 1981. [Godsil–Gutman journal paper](https://onlinelibrary.wiley.com/doi/10.1002/jgt.3190050203), [Heilmann–Lieb publication record](https://collaborate.princeton.edu/en/publications/theory-of-monomer-dimer-systems-2/). No source text for those papers was located in `refs/src/`. The interlacing background is Marcus, Spielman and Srivastava, *Interlacing families I: Bipartite Ramanujan graphs of all degrees* (2015); this lane uses the resulting HPS theorem, not an unproved extension of interlacing to arbitrary groups. HPS and the strong-convergence references are identified at their points of use above.

## Numerical checks for the blind lane

Six checkpoints, independently recomputable from this directory:

1. K4 SU(2) constant coefficient **12**: `python3 checks/haar_weingarten.py` (also directly summed over Q8).
2. K4 U(2) constant coefficient **6**: the same command (also directly summed over S3).
3. K4 A5 coefficient of x^3 **-16**: `python3 checks/haar_finite.py --graphs K4`.
4. Petersen SU(2) constant coefficient **57**: `python3 checks/haar_finite.py --graphs Petersen`.
5. Petersen U(3) largest root **2.729781416865**: `python3 checks/haar_limit.py`.
6. K4 U(16) sixth normalized root moment **693/8**: the same command.

## What this changes in the notebook

Proposed claim rows only; **nothing registered, no source page edited, no independent REFUTE review yet**:

| Candidate | Status | Statement / proof |
|---|---|---|
| H-gauge-Haar | PROVED | Independent edge Haar averaging equals cotree Haar averaging; Section 0. |
| H-exterior-kernels | PROVED | The averaged determinant is determined by the finite exterior-power kernels; equations (5)–(6). |
| H-SU2-cycle-squares | PROVED | The doublet average is the sum of squared matching polynomials over disjoint cycle deletions; equation (9). |
| H-compact-RH | REFUTED | C3/Q8 gives (x^3-3x)^2+1; K4/Q8 gives (11). |
| H-quaternionic-obstruction | PROVED | Every nontrivial quaternionic irrep fails averaged real-rootedness on every cyclic simple graph; Section 2. |
| H-doublet-dichotomy | PROVED | For irreducible doublets on cyclic simple graphs, nontrivial determinant gives the HPS polynomial; determinant one gives failure. |
| H-unitary-average | PROVED, known theorem | Defining U(d) average equals mu_{d,Y}, real-rooted in-band; HPS and Section 1.3. |
| H-unitary-root-limit | PROVED | The empirical root measure tends to Kesten–McKay, with O(1/d) error in each fixed moment; Section 3. |
| H-finite-equivalences | PROVED, exact checks | Q8/2T/2O and A5 reductions and all four graph tables; Section 4 and scripts. |

Suggested replacement for the U(d)/SU(2)/S_d averaging paragraph of `notes/adelic-gkp/gauge-groups.md`:

> The defining U(d) Haar average is the degree-nd d-matching polynomial of Hall–Puder–Sawin, so all its roots lie in the tree band. The standard representation of S_r gives the (r-1)-matching polynomial. SU(2) behaves differently: for its doublet the average is the sum, over vertex-disjoint cycle collections, of the squared matching polynomial of the remaining graph; on K4 it is (x^4-6x^2+3)^2+4x^2+3 and has no real roots. More generally quaternionic irreducible representations fail averaged real-rootedness on every cyclic simple graph.

One-line annotations are candidates for `graph-super.md` Section 6 and `zn-flux.md` Section 4: their scalar averaging theorem remains valid for every nontrivial character and N>=2, and does not extend to arbitrary higher-dimensional representations. Correct the cover-degree index and the distinction between one-sided existence and the two-sided root bound where HPS is quoted. `data-ladder.md` can retain its scalar-family statement while adding that compactness and finite image alone do not imply RH on average.

“RH on average” is a property of the **graph, representation, and chosen probability ensemble**. P1 guarantees it uniformly over loopless graphs; quaternionic symmetry obstructs it uniformly over cyclic simple graphs. The same 2T group and the same K4 graph exhibit both answers in different faithful irreps. Thus neither the bare group nor the bare graph determines the answer.

Next: independent REFUTE review of the exterior-kernel formula, the Pfaffian sum-of-squares identity, and the formal-series proof of the root limit before any registration. A remaining mathematical classification problem is which irreps beyond P1 have real-rooted averages on all loopless graphs; this lane makes no universal claim for the remaining real or complex representations.
