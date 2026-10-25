# Lane I: representation-sensitive RH on average

Author: `codex:gpt-6-astra`, 2026-10-25. Research candidates only; nothing registered.

## 0. Setting and scope — PROVED / conventions

Graphs are finite simple loopless graphs. For a regular graph the stated band is used only in degree at least two; in general use the spectral radius of the universal covering tree. The average includes every field, including the identity field, with no polynomial factor removed. Representations are continuous unitary, and nontrivial irreducible unless stated. Independent edge Haar averaging equals independent cotree Haar averaging by the gauge-fixing proof in lane H §0. No RH assumption enters the computations.

The binding briefs and lane H were read. If nontriviality or the band condition is omitted, the trivial representation has real-rooted averages on every graph but is not a matching example; on K4 its eigenvalue 3 lies outside the cubic tree band. The present lane will not turn a sufficient condition into a classification without a converse. “Matching-type” is too ambiguous for an iff: below the precise comparison is the HPS polynomial mu_{d,Y}, indexed by representation dimension.

## 1. I-1 — REFUTED as stated; finite exterior data replace all-order moments

Already S3 standard (dimension two, real type) satisfies the HPS condition, on every graph. Thus the suggested real-type obstruction fails in dimension two, not just for the signing character. Conversely SU(3) defining is complex type and its **every balanced tensor moment** equals that of U(3), yet it fails on C3. Balanced tensor moments cannot detect the determinant character: U(d)=U(1)SU(d) and the scalar factor cancels identically in U^{tensor k} tensor conjugate(U)^{tensor k}. Consequently even agreement of all such moments is insufficient.

### 1.1 Precise sufficient condition, and what it does not say

Set V_a=Lambda^a V, 0<=a<=d, and

    K^{ab}(I,J;K,L)=integral (Lambda^a rho)_{I,J} conjugate((Lambda^b rho)_{K,L}).

Lane H's minor expansion (5)–(6) expresses the average as a contraction of these edge kernels. The following three properties are equivalent:

1. All V_a are irreducible and pairwise nonisomorphic (P1).
2. Every K^{ab} equals delta_ab delta_IK delta_JL / binomial(d,a).
3. The averaging projectors on V_a tensor conjugate(V_b) equal the U(d) projectors.

Schur orthogonality proves 1=>2=>3. Conversely the trace of each diagonal averaging projector is dim End_G(V_a)=1, and each off-diagonal trace is dim Hom_G(V_b,V_a)=0; complete reducibility proves 3=>1. This is an exact **kernel classification**, with no growing moment order and no graph-size dependence.

It implies, by the edge minor contraction,

    Phi_{rho,Y}(x)=mu_{d,Y}(x)
      = sum_{0<=k_e<=d, s_v=sum_{e incident v} k_e<=d}
        (-1)^{sum k_e} x^{d|V|-2 sum k_e}
        product_v (d)_{s_v} / product_e [k_e! (d)_{k_e}].                    (1)

The real-root and universal-cover bound are the cited Hall–Puder–Sawin theorem. P1 is their Definition 1.7; identification is Theorem 1.8, root control Theorem 2.7, compact extension Remark 1.12. Their Corollary 5.6 includes **O(d) as well as U(d)**. Their §5.2 explicitly does not claim a full classification of P1 pairs. Source checked against the [author manuscript](https://www.ias.edu/sites/default/files/math/csdm/15-16/HallPuSa2016.pdf), pp. 5–7, 14, 32 (PDF page numbering); no local TeX source was found. The kernel equivalence and deductions here are supplied directly.

The converse is also true and is proved in §2.1 from the triangle alone; this does not require reconstructing arbitrary tensor contractions.

### 1.2 A cycle test — PROVED

Put D_l(x)=2T_l(x/2), so D_3=x^3-3x and D_4=x^4-4x^2+2. Gauge fixing a cycle C_l to one holonomy U gives

    det(x-A_U)=det(D_l(x) I_d-U-U*)=F_U(D_l(x)).                         (2)

For z+z^{-1}=t,

    F_rho(t)=z^{-d} sum_{a,b=0}^d (-1)^{a+b} z^{2d-a-b} H_ab,
    H_ab=dim Hom_G(Lambda^b V,Lambda^a V).                              (3)

Indeed det(z-U)det(z-U*)/z^d is the first determinant in (2); integrate the character expansions. The Laurent expression is invariant under z<->z^{-1} and hence a polynomial in t. Thus a single finite integer Gram matrix supplies an exact obstruction. For P1 it gives U_d(t/2). Real-rootedness on C_l requires F_rho to have d real roots in [-2,2]: a nonreal root cannot have a real preimage, and a real root outside [-2,2] has fewer than l real preimages under D_l (l>=3). Conversely roots in [-2,2] have all l preimages real in [-2,2], with multiplicities accounted for by Chebyshev extrema.

In particular:

    F_{SU(2),2}(t)=t^2+1;
    F_{SU(3),3}(t)=t^3-2t-2;
    F_{SO(3),3}(t)=t^3-2t-4=(t-2)(t^2+2t+2).                         (4)

The SU3 cubic has discriminant -76, hence one real root and two nonreal roots. Its C3 average is (x^3-3x)^3-2(x^3-3x)-2. This is the smallest simple cyclic graph and a complex-type counterexample to the brief, with no numerical approximation needed. SO3 has three real roots on C3 (with multiplicity), six nonreal. SU3 also has three real roots and six nonreal. Even cycles give the same obstruction, so bipartiteness does not repair these cases.

### 1.3 Exact five-graph verdict table — PROVED by exact computation

Every entry is **real roots / degree**, counted with multiplicity. All counted real roots are certified in the corresponding band. A full count is PASS; a deficient count is FAIL. The exact non-matching SU3 passes on three graphs do not change its failure of the universal property.

| Class | Representations | P1 / equals mu_d on every graph | C3 | K4 | K3,3 | cube | Petersen |
|---|---|---|---|---|---|---|---|
| M1 | nontrivial U1 and Z_N characters (N>=2); S_r sign | YES | 3/3 | 4/4 | 6/6 | 8/8 | 10/10 |
| M2 | U2; S3 standard; dihedral irreducible doublets; two twisted 2T doublets | YES | 6/6 | 8/8 | 12/12 | 16/16 | 20/20 |
| M3 | U3; O3; S4 standard; U2 det^a Sym^2, a!=-1 | YES | 9/9 | 12/12 | 18/18 | 24/24 | 30/30 |
| S2 | SU2 doublet; Q8; untwisted 2T; defining 2O | NO | 0/6 | 0/8 | 0/12 | 0/16 | 0/20 |
| S3 | SU3 defining; Delta(27) defining | NO | 3/9 | 8/12 | 18/18 | 24/24 | 30/30 |
| R3 | SO3; SU2 spin 1; both A5 triples; S4 standard times sign | NO | 3/9 | 4/12 | 10/18 | 16/24 | 20/30 |

Each M_d is precisely (1). S2 is (5) with d=2 (equivalently lane H's cycle-square sum), S3 is (5) with d=3, and R3 is the exact SO3 exterior-kernel contraction. These formulas specify the displayed representation equivalences **on all graphs**, not only the sampled graphs. The dihedral assertion concerns every irreducible two-dimensional representation: reflections have determinant -1. For generalized quaternion groups, determinant-one doublets fail and determinant-nontrivial doublets pass by §2; for Q8 the unique doublet is in the former class.

For complete explicit polynomial data, the next table gives the descending coefficient vector, including every zero coefficient; this avoids any ambiguity about missing powers. The same vectors and verdicts are in `checks/output_scan.json`, and `checks/output_scan.txt` prints every expanded polynomial.

<details>
<summary>Exact rational polynomial coefficient vectors (all thirty cases)</summary>

| Graph | Class | Descending coefficients |
|---|---|---|
| C3 | M1 | `[1, 0, -3, 0]` |
| C3 | M2 | `[1, 0, -6, 0, 9, 0, -1]` |
| C3 | M3 | `[1, 0, -9, 0, 27, 0, -29, 0, 6, 0]` |
| C3 | S2 | `[1, 0, -6, 0, 9, 0, 1]` |
| C3 | S3 | `[1, 0, -9, 0, 27, 0, -29, 0, 6, -2]` |
| C3 | R3 | `[1, 0, -9, 0, 27, 0, -29, 0, 6, -4]` |
| K4 | M1 | `[1, 0, -6, 0, 3]` |
| K4 | M2 | `[1, 0, -12, 0, 42, 0, -40, 0, 6]` |
| K4 | M3 | `[1, 0, -18, 0, 117, 0, -332, 0, 393, 0, -158, 0, 97/9]` |
| K4 | S2 | `[1, 0, -12, 0, 42, 0, -32, 0, 12]` |
| K4 | S3 | `[1, 0, -18, 0, 117, 0, -332, 0, 393, -8, -158, 0, 43/9]` |
| K4 | R3 | `[1, 0, -18, 0, 117, 0, -332, 0, 393, -16, -158, 0, -11/9]` |
| K33 | M1 | `[1, 0, -9, 0, 18, 0, -6]` |
| K33 | M2 | `[1, 0, -18, 0, 117, 0, -336, 0, 423, 0, -198, 0, 21]` |
| K33 | M3 | `[1, 0, -27, 0, 297, 0, -1719, 0, 5652, 0, -10656, 0, 11086, 0, -5778, 0, 1228, 0, -1684/27]` |
| K33 | S2 | `[1, 0, -18, 0, 117, 0, -336, 0, 441, 0, -234, 0, 51]` |
| K33 | S3 | `[1, 0, -27, 0, 297, 0, -1719, 0, 5652, 0, -10656, 0, 11068, 0, -5724, 0, 1174, 0, -1522/27]` |
| K33 | R3 | `[1, 0, -27, 0, 297, 0, -1719, 0, 5652, 0, -10656, 0, 11050, 0, -5670, 0, 1120, 0, -1360/27]` |
| cube | M1 | `[1, 0, -12, 0, 42, 0, -44, 0, 9]` |
| cube | M2 | `[1, 0, -24, 0, 228, 0, -1096, 0, 2832, 0, -3864, 0, 2556, 0, -672, 0, 42]` |
| cube | M3 | `[1, 0, -36, 0, 558, 0, -4884, 0, 26619, 0, -94008, 0, 217180, 0, -324088, 0, 301723, 0, -1479604/9, 0, 46830, 0, -50500/9, 0, 13297/81]` |
| cube | S2 | `[1, 0, -24, 0, 228, 0, -1096, 0, 2844, 0, -3960, 0, 2828, 0, -912, 0, 126]` |
| cube | S3 | `[1, 0, -36, 0, 558, 0, -4884, 0, 26619, 0, -94008, 0, 217168, 0, -323944, 0, 301075, 0, -1467796/9, 0, 45630, 0, -46828/9, 0, 11353/81]` |
| cube | R3 | `[1, 0, -36, 0, 558, 0, -4884, 0, 26619, 0, -94008, 0, 217156, 0, -323800, 0, 300427, 0, -1455988/9, 0, 44430, 0, -43156/9, 0, 11353/81]` |
| Petersen | M1 | `[1, 0, -15, 0, 75, 0, -145, 0, 90, 0, -6]` |
| Petersen | M2 | `[1, 0, -30, 0, 375, 0, -2540, 0, 10155, 0, -24474, 0, 34815, 0, -27360, 0, 10335, 0, -1370, 0, 27]` |
| Petersen | M3 | `[1, 0, -45, 0, 900, 0, -10560, 0, 80820, 0, -424392, 0, 1566070, 0, -4091370, 0, 7525625, 0, -9571425, 0, 24433478/3, 0, -4394410, 0, 37203950/27, 0, -648190/3, 0, 341060/27, 0, -28132/243]` |
| Petersen | S2 | `[1, 0, -30, 0, 375, 0, -2540, 0, 10155, 0, -24450, 0, 34595, 0, -26640, 0, 9345, 0, -790, 0, 57]` |
| Petersen | S3 | `[1, 0, -45, 0, 900, 0, -10560, 0, 80820, 0, -424392, 0, 1566070, 0, -4091370, -24, 7525625, 360, -9571445, -2160, 24434018/3, 6600, -4394950, -10800, 37217720/27, 9048, -647920/3, -3280, 338630/27, 240, -15010/243]` |
| Petersen | R3 | `[1, 0, -45, 0, 900, 0, -10560, 0, 80820, 0, -424392, 0, 1566070, 0, -4091370, -48, 7525625, 720, -9571465, -4320, 24434558/3, 13200, -4395490, -21600, 37231490/27, 18096, -647650/3, -6560, 336200/27, 480, 9776/243]` |

</details>

In particular, putting B=x^12-18x^10+117x^8-332x^6+393x^4-158x^2, the three K4 triples are

    M3=B+97/9,     S3=B-8x^3+43/9,     R3=B-16x^3-11/9.

`checks/finite_certificates.py` independently sums S4 standard and its sign twist on K4, with orbit weights totalling 24^3=13824 in each case. It also sums Delta(27) on C3 and K4, independently reproducing the SU3 polynomials. Delta(27) consists of the monomial matrices e_j -> omega^(a j+b)e_(j+r), a,b,r in Z/3; they have determinant one. Its defining module is irreducible because the diagonal generator has three distinct eigenspaces permuted transitively by the shift. V and V* differ on the scalar omega I. Thus its exterior list is (1,V,V*,1), exactly the SU3 kernels. The finite calculation uses integer restriction of scalars from Q(omega); it verifies the square identity of each resulting characteristic polynomial before averaging. It is not a claimed raw unitary 3-design.

The Q8/2T/2O kernels were rerun exactly, including both quotient-character twists of 2T. All lane H finite coefficients were reproduced by fresh A4 sums and the new matching DP; the K4 Weingarten output was reproduced byte-for-byte. The A4/SO3 reduction is the oriented Hodge-star equivalence of the four exterior modules (1,V,V,1), so it verifies A5 and the S4 sign twist on the cube as well.

## 2. I-2 — PROVED: sharp matching classification in all dimensions; full root classification through dimension three

**PROVED.** For nontrivial irreducible compact-group representations of dimension d<=3, the following are equivalent:

- det rho is a nontrivial character;
- P1 holds;
- Phi_{rho,Y}=mu_{d,Y} on every finite simple graph;
- Phi_{rho,Y} is real-rooted on every finite simple graph;
- Phi_{rho,C3} is real-rooted.

For d=1 this is the scalar signing/phase theorem. For d=2 use Lambda^2 V=det V and lane H's quaternionic dichotomy. For d=3 write delta=det V. Then Lambda^2 V=delta tensor V* is irreducible. The only possible same-dimension collisions among the four exterior powers are 1=delta and V=delta tensor V*. In the latter case taking determinants yields delta=delta^2, hence delta=1. Therefore delta!=1 implies P1. If delta=1 and V is not self-dual, its exterior list is (1,V,V*,1), giving the SU3 cubic in (4). If it is self-dual, odd dimension rules out quaternionic type, and the list is (1,V,V,1), giving the SO3 cubic. Both fail on C3 by (4). This exhausts dimension three, for connected and disconnected compact groups and finite groups alike.

This root-classification theorem is narrower than a classification in all dimensions; universal real-rootedness in higher dimension remains OPEN in this lane. The matching class has a complete answer below.

### 2.1 The sharp matching-polynomial classification in every dimension — PROVED

The converse to the sufficient criterion in §1.1 follows from the cycle formula. For **every** unitary representation of a compact group of positive dimension d, the following are equivalent:

    (i) P1;
    (ii) all exterior kernels equal the U(d) kernels;
    (iii) Phi_{rho,Y}=mu_{d,Y} for every finite simple Y;
    (iv) Phi_{rho,C3}=mu_{d,C3}.

The forward implications were proved above. For (iv)=>(i), composition with the nonconstant polynomial D_3 is injective, so (3) must equal U_d(t/2). Substitute t=z+z^{-1}. The coefficient of z^{d-s} is

    (-1)^s sum_{a+b=s} H_ab.

Every H_ab is a **nonnegative integer**, and every diagonal H_aa is at least one. The target Laurent polynomial is sum_{a=0}^d z^{d-2a}. For odd s its coefficient is zero, forcing every H_ab on that antidiagonal to vanish. For even s its coefficient is one, already supplied by H_{s/2,s/2}>=1; all other entries on the antidiagonal vanish and that diagonal entry equals one. Therefore H=I, which is precisely P1 by complete reducibility. No weighted graphs, loops, reconstruction of arbitrary tensor networks, or high-design assumption is needed. A single triangle detects equality to the matching polynomial.

This gives the exact requested classification **for the class Phi=mu_d on all graphs**, expressed as a finite representation-theoretic test. For a finite group it is computable from its character table alone: if psi_a=chi_{Lambda^a V}, then H_ab=|G|^{-1} sum_C |C| psi_a(C) conjugate(psi_b(C)); the psi_a follow from Newton identities using chi(g^j), 1<=j<=d. The test is exactly H=I. It is not an assertion that real-rootedness alone forces P1 in arbitrary dimension.

### 2.2 Connected counterexample to the proposed image classification — PROVED

Take G=U(1) x SO(3) and rho(z,R)=zR. The representation is irreducible of complex type and has exterior list

    1, zV, z^2 V, z^3.

All four are irreducible and the central weights distinguish them. Hence P1 holds, although the connected image U(1)SO(3) has dimension four and cannot contain SU(3), of dimension eight. Equivalently it is the image of Sym^2 of U(2). Thus even the proposed connected **matching** class is substantially wider than U(d). More generally U(1)SO(2r+1) gives such examples, using the irreducible exterior powers of the odd orthogonal defining representation; the three-dimensional example alone is sufficient for the refutation and does not depend on this generalization.

For all U(2) irreps rho_{a,b}=det^a tensor Sym^b, with a integer and b>=0, the matching classification is explicit:

- b=0: P1 iff a!=0;
- b=1: P1 for every a;
- b=2: P1 iff a!=-1;
- b>=3: never P1, since Lambda^2 Sym^b contains both Sym^{2b-2} and Sym^{2b-6} (and possibly further summands).

The central weight is 2a+b. For b=2 its zero value gives the SO3 representation. These statements classify equality to mu_{b+1}; they do not claim that all remaining cases fail universal real-rootedness.

### 2.3 The design degree — PROVED, and a correction of terminology

A raw determinant term uses at most d matrix entries of an independent edge label U and at most d conjugate entries. Thus equality of **all mixed moments of bidegrees (a,b), 0<=a,b<=d**, with U(d) suffices on every simple graph, with no dependence on girth, edge count, or cycle rank. After gauge fixing there are g independent holonomies; the same per-variable bidegree bound holds, and a sufficient total degree bound is 2dg (per variable, total degree <=2d). The suggested bound 2g omits the representation dimension and is not valid in general.

A conventional unitary d-design matches balanced bidegrees (k,k), k<=d. Alone this does **not** suffice: even Haar SU(d) matches every balanced degree and retains determinant moments. A sufficient stronger construction is a unitary d-design multiplied by an independent scalar uniform on C_M with M>d; scalar averaging kills every nonzero a-b in the needed range. Full mixed (d,d) moment matching is still far stronger than needed; the exact necessary and sufficient condition for the matching class is the antisymmetrized P1 criterion of §2.1. S3 standard is not even a unitary 2-design: E|chi|^4=3, whereas U(2) gives 2, yet it works on **every** graph. Consequently neither increasing |E| nor increasing cycle rank can turn a growing-design requirement into a necessary condition.

For a target such as SU3, a finite subgroup may replace Haar only if its needed exterior kernels agree with that target, including the determinant and any off-diagonal intertwiners. No 3-design replacement is assumed in our SU3 calculation.

### 2.4 SU(d) on every simple graph — PROVED

For the defining representation, the SU(d) exterior kernels differ from U(d) only by K^{0d}=K^{d0}=1. Selecting one such kernel on an edge sends all d colors in one direction and none in the other. At each incident vertex row/column balance forces another such edge, so the selected edges form vertex-disjoint directed simple cycles; all their vertices are saturated and removed from the rest of the contraction. One directed cycle contributes (-1)^d, the sign of the d-color block permutation including its adjacency minus signs. The two orientations therefore give 2(-1)^d. All remaining edges use the U(d) kernels. Hence

    Phi_{SU(d),Y}(x) = sum_{C} [2(-1)^d]^{|C|} mu_{d,Y\V(C)}(x),          (5)

over collections of vertex-disjoint unoriented simple cycles, including the empty collection. On a cycle this reads U_d(D_l/2)+2(-1)^d, in agreement with (3). For d=2 it agrees identically with lane H's sum of squares, giving an independent combinatorial check. For d=3, K4 has four triangles and three four-cycles, so

    Phi_{SU3,K4}=mu_{3,K4}-8x^3-6.                                     (6)

The scan computes (5) exactly on all five requested graphs, including Petersen, without any Weingarten truncation or quadrature.

## 3. I-3 — PARTIAL: distinguish uniform and graph-specific real-rootedness

### 3.1 Bipartite graphs and conjugate sums — PROVED

Bipartiteness does not remove the quaternionic obstruction. If rho is quaternionic, the antiunitary symmetry acts on the color factor and commutes with the adjacency on **every** graph, bipartite or otherwise; lane H's nonconstant-square lemma still applies. For the doublet C4 gives (x^4-4x^2+2)^2+1, with no real roots. SO3 also fails on C4 by (4). SU3 fails on C4 as well, since the same cubic F has nonreal roots. Nevertheless SU3 passes on K3,3 and the cube: this is an exact graph-specific effect, not a universal theorem for bipartite graphs.

For any nontrivial rho, A_{bar rho}=conjugate(A_rho). Both characteristic polynomials are real, hence identical. Therefore

    Phi_{rho direct-sum bar rho,Y}=E det(x-A_rho)^2.

On a graph with a cycle this is not real-rooted, by the nonconstant-square lemma from lane H. Nonconstancy follows by varying a holonomy on a shortest cycle and comparing Tr A^l. This obstruction includes complex-type rho and does not require quaternionic symmetry. Correlated summands must not be averaged independently.

For comparison, **independent** summands can give universally real-rooted products: on G=U(1)xU(1), take rho(z,w)=z direct-sum w. Then Phi=mu_{1,Y}^2, which generally differs from mu_{2,Y}. This reducible example answers the question with “not the dimension-d HPS polynomial” literally, but it is itself a product of matching polynomials, so does not settle the intended irreducible/non-matching-type question. In the nontrivial irreducible class of dimension <=3, §2 rules out such an example. In higher dimension the uniform question remains OPEN here.

### 3.2 A new connected four-dimensional candidate — PROVED formula; uniform roots OPEN

For G=U(1)xUSp(4) in its defining four-dimensional complex representation (USp(4) is the compact symplectic subgroup of U(4), also denoted Sp(2)), or for **any** U(2) irrep det^a tensor Sym^3, one has

    Phi_{rho,Y} = sum_C mu_{4,Y\V(C)},                                 (7)

over the same vertex-disjoint unoriented simple-cycle collections. In particular it is not mu_4 on any cyclic graph. It is real-rooted on every cycle, with F(t)=(t^2-1)(t^2-2), although P1 fails.

Proof of (7). The middle exterior power decomposes as 1+W_5; all other exterior powers are irreducible. The scalar center separates their degrees. Normalize the invariant bivector as j=(e_1 wedge e_2+e_3 wedge e_4)/sqrt(2), let P=jj*, and put Q=P-I_6/6. The degree-two edge kernel is

    P tensor P + (I-P) tensor (I-P)/5
       = I tensor I/6 + (6/5) Q tensor Q.                              (8)

The first term is the U4 kernel. At a vertex, the local alternating contraction with exactly one Q vanishes: all remaining endpoint operators are identities, and the induced functional on End(Lambda^2 C4) is U4-invariant, hence proportional to trace, while Tr Q=0. Two Q incidences use all four colors. Thus the exceptional edges form vertex-disjoint cycles and saturate their vertices. At a vertex with two exceptional edges the wedge contraction is 5/6: in the oriented exterior basis the complementary-pair (Hodge) matrix S satisfies SQS=Q, so the contraction is Tr(Q^2)=5/6. Each exceptional edge contributes 6/5, cancelling vertex factors around each cycle. Its edge multiplicity is two, so the sign is positive. This proves (7). For U2 Sym^3, Lambda^2 Sym^3=Sym^4+1 and both summands stay irreducible with dimensions five and one; the compatible invariant bivector is the same. Its other exterior kernels agree as well, so (7) applies to every determinant twist.

The direct minor contraction in `checks/symplectic4.py` independently sums the two-endpoint kernels (8) with exact rational coefficients. It reproduces the tree determinant, the cycle Gram polynomial and the U4 control, and on K4 gives

    Phi=x^16-24x^14+228x^12-1092x^10+2781x^8-3654x^6
         +2234x^4-495x^2+87/4
       =mu_{4,K4}+4x^4+3.                                            (9)

All sixteen roots are real and in [-2sqrt(2),2sqrt(2)], certified by rational isolation. The cycle formula also passes the real-root test on K5, K3,3, the cube and Petersen, and on all **971 connected simple cyclic graphs with at most seven vertices** in the NetworkX graph atlas (each polynomial and exact root count printed in `checks/output_sp4_atlas7.txt`; the at-most-six-vertex subscan has 129 graphs). These are computations, **not** a proof that (7) is real-rooted for every graph. Every real root of (7) is automatically in the universal-cover band: outside that band each mu_4 of an induced subgraph is positive, since its degree is even and all its roots lie in the smaller subgraph band. Thus the positive sum (7) has no root there. What is open is whether every root is real. This candidate deserves a stability/interlacing argument or an adversarial graph search; the universal classification should not be reported as settled.

### 3.3 The correct real-type obstruction — PROVED

Every nontrivial real-type representation with determinant one, of dimension d>=2, fails on **every cycle** C_l. To see this, choose a real orthonormal form, so U lies in SO(d). Its nonreal eigenvalues occur in conjugate pairs, its -1 eigenspace has even dimension, and its +1 eigenspace has parity d. Consequently

    det(tI-U-U*)=(t-2)^epsilon Q_U(t)^2,  epsilon=d mod 2,

with Q_U monic real-rooted. Its coefficient of t^{floor(d/2)-1} is -(Tr U-epsilon), which varies on any nontrivial compact image. Hence E Q_U^2 is not real-rooted by the same nonconstant-square argument, and multiplying by t-2 cannot repair it. Substitution t=D_l(x) preserves the existence of nonreal roots. This proves the claim. In particular **every nontrivial real-type irrep of a compact connected group** fails uniform real-rootedness, since its determinant is a continuous map to {+1,-1}, hence trivial. Together with the quaternionic obstruction, this proves that **complex type is necessary for a nontrivial irrep of a compact connected group to have the uniform property**. It is not sufficient. The disconnected real P1 examples O(d), S_r standard and dihedral doublets explain exactly why the original real-type conjecture was too broad.

The standard/sign-twisted comparison extends beyond S4. Let d=r-1 and H_a=Lambda^a std of S_r. These are the hook irreps, with H_a tensor sgn=H_{d-a}. Thus Lambda^a(std tensor sgn) is H_a for a even and H_{d-a} for a odd. If d is even, these are all distinct, so P1 holds. If d is odd, exterior powers pair up, determinant is one, and for d>=3 the real obstruction applies. The Gram formula gives F(t)=U_d(t/2)-(d+1) in the latter case. Its only root in [-2,2] is t=2, so it cannot pass the cycle test. The d=1 twist is the trivial representation, outside our nontrivial hypothesis. Sign characters themselves, and the S4 two-dimensional irrep factoring through S3, lie in the scalar and doublet positive classes respectively.

### 3.4 Nontrivial determinant ceases to suffice in higher dimension — REFUTED

The connected complex-type irrep Sym^5 of U(2), of dimension six and determinant det^{15}, fails already on C3. Its exterior Gram diagonal is (1,1,3,3,3,1,1), and distinct central weights kill off-diagonal entries. Formula (3) gives

    F(t)=t^6-5t^4+8t^2-3.

The cubic in y=t^2 has discriminant -31 and exactly one real root, in (0,1). Thus F has only two real roots, and Phi_C3 has exactly six real roots out of eighteen. This exact certificate prevents extrapolation of the d<=3 determinant criterion. `checks/cycle_scan.py` prints decompositions and exact cycle tests for Sym^b, 1<=b<=10, with and without a nonzero central weight when the latter choice exists. Sym^3 and Sym^4 with nonzero central weight pass all cycles while failing P1; these cases cannot be dismissed using the triangle's root verdict alone.

## 4. I-4 — PROVED interpretation and proposed record paragraph

For `gauge-groups.md` and `data-ladder.md` §2, proposed wording (not applied):

> “RH on average” belongs to the graph, representation and probability ensemble. For independent Haar edge labels, the average equals the HPS d-matching polynomial on every simple graph exactly when the exterior powers Lambda^0 rho,...,Lambda^d rho are irreducible and pairwise inequivalent; equality on one triangle already detects this condition. It holds for U(d), O(d), the standard S_{d+1} representation and further complex examples such as U(1)SO(3), so neither complex type nor full unitary moment matching is the criterion. Real determinant-one representations fail on cycles, quaternionic irreps fail on every cyclic graph, and even complex SU(3) fails on the triangle. Universal real-rootedness beyond the matching class remains a separate question: the four-dimensional U(2) Sym^3 family has a different exact cycle-deletion polynomial and passes the finite tests here, but is not proved to pass every graph.

The ladder consequence is a restriction on **ensembles**, not a new integral lattice or polarisation for an individual field. A real-rooted average does not say that each flux is in the band. The existing scalar Z_N/U(1) statements remain valid for every nontrivial character; no averaging statement for number-field L-functions follows from this classification.

## Correction ledger

| Claim in the brief / potential inference | Correction |
|---|---|
| All balanced tensor moments like U(d) characterize the desired class | **REFUTED:** SU3 agrees at every balanced order but fails on C3; determinant moments are unbalanced. |
| Real irreps fail once d>=2 | **REFUTED:** S3 standard already works, as do O(d) and S_r standard. The proved obstruction is real type **and determinant one**; hence all nontrivial connected real irreps fail. |
| Complex type suffices | **REFUTED:** SU3 on C3; even nontrivial determinant does not rescue U2 Sym^5. |
| Connected matching examples must contain SU(d) | **REFUTED:** U(1)SO3, equivalently U2 Sym^2, satisfies P1 and is a proper connected subgroup of U3. |
| Finite matching examples require increasingly high unitary designs | **REFUTED:** S3 is not a unitary 2-design and works for every graph. Fixed exterior kernels suffice. |
| Degree 2 times cycle rank is enough | **CORRECTED:** raw sufficient degree is <=2d in each holonomy (<=2dg total), with unbalanced moments included; exterior kernels are sharper. |
| HPS standard S_d gives mu_d | **CORRECTED:** its dimension is d-1, hence mu_{d-1}. |
| HPS already supplies a full classification | **NOT USED:** the source supplies sufficiency; the triangle antidiagonal argument here supplies necessity for equality to mu_d. No higher-dimensional universal real-root classification is claimed. |
| Quaternionic failure may disappear on bipartite graphs | **REFUTED:** Kramers squares are independent of bipartiteness; C4 is an explicit obstruction. |
| rho direct-sum bar rho may fix failure | **REFUTED:** its average is the mean square of a varying real polynomial on any cyclic graph. Independent summands behave differently. |
| Real-rooted on a graph implies matching on that graph | **REFUTED:** SU3 on K3,3, cube, Petersen; U2 Sym^3 on every cycle and K4. The proposed universal implication remains open above d=3. |

## Numerical checks for the blind lane

Run from `notes/astra-2026-10-25/irreps`. All scripts use installed Python 3, SymPy, NetworkX, NumPy and python-flint; no install and no external writes. The main scan reads lane H modules and saved coefficient vectors without modifying them. Computations are rational/integer; Sturm isolation counts multiplicity. No numerical zeta or L-function zeros and no RH assumption are inputs.

1. **SU3 cycle cubic discriminant -76**, and U2 Sym^5 reduced discriminant **-31**: `python3 checks/cycle_scan.py`.
2. **S3 standard E|chi|^4=3**, versus U2's 2: the same command. This is a concrete design obstruction with a positive matching outcome.
3. **SU3 K4 constant 43/9 and x^3 coefficient -8**: `python3 checks/finite_certificates.py`; 2835 simultaneous-conjugacy representatives have total weight **19683** in Delta(27). Every restriction-of-scalars polynomial is certified to be a square before averaging.
4. **S4 standard K4 constant 97/9**, versus its sign twist **-11/9**: the same command, two sums of total weight **13824**.
5. **SU3 Petersen: 30/30 real and in-band; constant -15010/243**: `python3 checks/irreps_scan.py --graphs Petersen`. This also reproduces the three lane H finite coefficient vectors exactly; about six minutes in this environment.
6. **U2 Sym^3 K4 constant 87/4 and 16/16 real in-band**: `python3 checks/symplectic4.py`. The cycle expansion is separately run by `python3 checks/sp4_scan.py`; `--atlas 6` checks all 129 connected cyclic simple graphs through six vertices, and `--atlas 7` all 971 through seven vertices.

Saved outputs: `checks/output_scan.txt` and `.json` (all thirty main cases); `output_cycles.txt`; `output_certificates.txt`; `output_symplectic4.txt`; `output_sp4_scan.txt`; `output_sp4_atlas.txt`; `output_sp4_atlas7.txt`; `output_sp4_summary.txt`; `output_rerun_weingarten.txt`; `output_rerun_kernels.txt`. The two rerun scripts are the read-only lane H originals invoked with `PYTHONDONTWRITEBYTECODE=1` and stdout redirected here. No Monte Carlo is used. The U2 higher-spin scan is a **cycle** scan; no all-five-graph result is claimed for every b>=4.

## What this changes in the notebook

Candidate rows only. **Nothing registered; no record page edited; no independent REFUTE review performed in this lane.** The prior same-family review of lane H does not adjudicate these new converse and cycle-deletion arguments.

| Candidate id | Status | Precisely scoped claim / evidence |
|---|---|---|
| `thm:rh-on-average-irrep-classification` | PROVED for the matching subclass | For every compact-group unitary representation, Phi=mu_d on all finite simple graphs iff P1; equivalently equality on C3 alone. §2.1 antidiagonal nonnegativity proof. This row is **not** an all-dimensional classification of real-rootedness alone. |
| `thm:rh-on-average-irrep-dim-three` | PROVED | For nontrivial irreps of dimension <=3, uniform real-rootedness, uniform matching equality and nontrivial determinant are equivalent. §2. |
| `cex:balanced-unitary-moments-average-rh` | REFUTED conjecture | SU3 has all balanced U3 moments yet fails on C3; Delta(27) supplies an exact finite analogue of its exterior kernels. §§1–2 and finite certificates. |
| `cex:connected-matching-image-su` | REFUTED conjecture | U(1)SO3 satisfies P1 without containing SU3; U2 Sym^2 is an equivalent image example. §2.2. |
| `thm:su-average-cycle-deletion` | PROVED | Defining SU(d) average is sum_C [2(-1)^d]^|C| mu_{d,Y\V(C)}. §2.4 and independent Delta(27) K4 check. |
| `thm:real-det-one-cycle-obstruction` | PROVED | Nontrivial real determinant-one representations fail on every cycle; hence connected real irreps fail the uniform property. §3.3. |
| `thm:conjugate-sum-average-obstruction` | PROVED | rho direct-sum bar rho fails on every cyclic graph because its average is a nonconstant mean square. §3.1. |
| `thm:conformal-sp4-average-cycle-deletion` | PROVED | U(1)USp(4) defining and U2 det^a Sym^3 have Phi=sum_C mu_{4,Y\V(C)}; every real root lies in the universal-cover band. §3.2 and direct exterior contraction. |
| `conj:conformal-sp4-average-real-rooted` | OPEN; exact finite evidence | Formula (7) is real-rooted for every finite simple graph. Passes all 971 connected cyclic graphs through seven vertices, plus cube and Petersen; passes every cycle by proof. |

Record annotations proposed: replace the averaging paragraph of `gauge-groups.md` by §4; append its ensemble qualification to `data-ladder.md` §2; annotate `graph-super.md` §6 and `zn-flux.md` §4 that their scalar statements survive, while higher-dimensional analogues are representation-sensitive. The dimension convention for S_r must be r-1. None of these edits is made here.

**Next decisive work:** independently REFUTE-review the triangle converse (especially the character indices and nonnegative antidiagonal argument), the saturated-cycle SU(d) contraction, and the Q-projector contraction for (7). Then prove stability/interlacing for (7), or find a counterexample beyond the tested graphs. That question is a concrete candidate for a genuinely non-HPS irreducible universal RH-on-average family. A Lie-theoretic list of every connected P1 image and a full all-dimensional real-root classification are not claimed here; the finite exact P1 iff theorem is the completed matching-class result.
