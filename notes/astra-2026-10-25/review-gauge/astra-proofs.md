# Lane RG: adversarial review of compact and SU(1,1) graph gauge fields

Author: `codex:gpt-6-astra` (reviewer), 2026-10-25.

This is a same-family REFUTE review of lanes H and K, not the second-family review required by the record's registration gate. No claim is registered and no record page is edited. Exact derivations and independent computations below do not assume RH. The scope is the lanes' stated graph conventions; in particular H normally uses simple graphs and the regular band formula assumes q >= 1.

## H1. Gauge fixing — VALID, PROVED independently

Claim `H-gauge-Haar`: normalized independent-edge Haar integration of a gauge-invariant function equals normalized Haar integration in any spanning-tree gauge.

Choose a rooted spanning tree T. Set t_root=1 and recursively set t_v=t_u s_uv on a tree edge directed from parent u to child v. Then t_u s_uv t_v^{-1}=1. Conditional on the tree labels, each transformed cotree variable is a fixed left and right translate of its original independent Haar variable. Its conditional distribution is normalized Haar and the variables remain independent. Integrating the tree labels contributes exactly 1, not a group volume or a stabilizer factor. The block diagonal gauge conjugates A, hence preserves its determinant. Repeating the argument for any T proves tree independence. G^g/G is the orbit space; integrating on G^g computes its pushforward probability measure and does not require dividing by orbit cardinalities.

The scalar specialization is also VALID: the Leibniz terms containing a simple cycle have an edge used once and vanish for a nontrivial one-dimensional character; dimers give the matching polynomial. This removes no individual trivial-flux eigenvalue. It requires N >= 2 for the faithful Z_N character. The q=0 edge is an exception to the formula 2 sqrt(q), not to Haar gauge fixing.

## H2. Exterior kernels and the space being averaged — VALID, PROVED independently

Claim `H-exterior-kernels`: the mixed exterior matrix-coefficient kernels (5), in compatible bases, determine the entire average.

Let W = direct-sum over vertices v of V_v, with dim W=nd. Globally,

    det(xI-A) = sum_{k=0}^{nd} (-1)^k x^{nd-k} Tr(Lambda^k A).

Here Lambda^k acts on W, not on one fibre V. Decompose Lambda^k W into the summands tensor_v Lambda^{k_v} V_v, sum k_v=k. Expand A as the sum of its directed edge blocks, and allocate the selected input and output indices to those blocks. Alternating the indices allocated to one directed edge turns its matrix entries into a minor. The same result follows by grouping the ordinary Leibniz expansion by the row/column partitions in (6); the grouping is disjoint and exhaustive. The diagonal block contributes x^{|F|}, its row and column sets must both be F, and the determinant sign is precisely the two concatenation signs times (-1)^{sum r_e}. A reverse edge contributes the conjugate minor with its row and column subsets interchanged. This reproduces all indices and signs of (6).

For one unoriented edge with a forward and b reverse occurrences, the averaging operator is the orthogonal projector

    P_ab = integral (Lambda^a rho)(h) tensor conjugate((Lambda^b rho)(h)) dh

on Lambda^a V tensor conjugate(Lambda^b V). Its matrix entry with output (I,K), input (J,L) is exactly K^{ab}(I,J;K,L). Equivalently this space identifies with Hom(Lambda^b V,Lambda^a V), and Haar projects onto the intertwiner space. If constructed from raw tensor powers, one must first use rho^{tensor a} tensor conjugate(rho)^{tensor b} and restrict with the two antisymmetrizers. Averaging rho^{tensor k} on V^{tensor k} alone is not the required kernel. The lane makes the correct mixed-space statement; it does not confuse it with Lambda^k W.

For U(d), Schur orthogonality and distinct central weights give delta_ab delta_IK delta_JL / binomial(d,a). For determinant-one irreducible doublets, Lambda^0=Lambda^2=1 adds exactly the 0-to-2 and 2-to-0 intertwiners. These are the contractions needed later; no general scalar cycle-moment factorization is assumed.

## H3. SU(2) cycle squares and finite subgroup integration — VALID

Claim `H-SU2-cycle-squares`, PROVED: for a simple graph, the defining SU(2) average is the sum of mu_{Y minus V(C)}(x)^2 over vertex-disjoint collections C of unoriented simple cycles, including the empty collection.

Write E=diag([[0,1],[-1,0]]). For H=xI-A, H E=E H^T, so H E is antisymmetric and its monic Pfaffian Q has Q^2=det H. This Q is real: its conjugate is another monic square root of the same real polynomial. Each vertex has two half-indices in a Pfaffian pairing; after projection its nontrivial component is either a doubled edge or a simple cycle. A doubled edge contributes -det U=-1, and a longer cycle contributes minus its holonomy trace (the two orientations are already included). Thus Q is the lane's equation (10). In Q^2, unequal cycle edge sets leave an edge appearing once, whose independent Haar integral vanishes. Equal edge sets determine the same cycle collection, and each of its independent real irreducible characters has mean square 1. All surviving weights are +1. This checks both the sign and the absence of an extra orientation factor in (9).

**Two independent computations completed.** `checks/independent_haar.py` first integrates the raw Leibniz determinant over independent unit quaternions on **every** edge, using exact normalized S^3 monomial integrals. It does not use a Pfaffian or the cycle formula. It then sums the direct complex characteristic polynomials over Q8 cotree labels, choosing a DFS spanning tree instead of the lane's BFS/star tree; it does not use realification or extract square roots of real characteristic polynomials. Both routes give

    C3: x^6 - 6x^4 + 9x^2 + 1 = (x^3-3x)^2 + 1,
    K4: x^8 - 12x^6 + 42x^4 - 32x^2 + 12
        = (x^4-6x^2+3)^2 + 4x^2 + 3.

The constants certify strict positivity on the entire real axis; all six/eight roots are nonreal. Independently enumerating 2-regular **edge subsets** of Petersen and counting perfect matchings of their complements gives constant 36+15+6=57. The three contributions come respectively from the empty collection, eight-cycles, and two disjoint five-cycles.

**Design qualification.** Q8, as eight unit quaternions, integrates every real-coordinate polynomial of total degree <=3, but not degree 4: E_Q8 q0^4=1/4 whereas E_SU2 q0^4=1/8. The binary tetrahedral group 2T integrates through degree 5, but not degree 6: E_2T q0^6=3/32 whereas E_SU2 q0^6=5/64. Antipodal symmetry kills odd moments; direct axis/half-coordinate sums check all the even moments through the stated degrees. In balanced unitary-design terminology, Q8 is a 1-design but not a 2-design, and 2T is a 2-design but not a 3-design; the failures can also be expressed as moments of |tr(U)|. The determinant can have raw degree four in an individual edge, so a blanket fourth-moment design claim for Q8 would be false. The lane does **not** need that claim: its exterior kernels are exactly the SU(2) kernels. In the Pfaffian-square proof each edge has degree at most two after using determinant-one identities. This explains equality for every graph size. It does not justify replacing SU(2) by Q8 for higher spins.

`H-compact-RH` is VALID as a refutation. Its minimality qualifications also check: under the simple-graph, q>=1 convention C3 is the smallest regular graph; no scalar irreducible provides a counterexample. Below group order eight the only nonabelian case is S3, whose doublet satisfies P1. The loop, parallel-edge and q=0 examples in the body have their explicitly different conventions and are correct: x^2+1, (x^2-3)^2+3, and (x^2-1)^d respectively.

## H4. Quaternionic obstruction — VALID, PROVED; spin 3/2 checked

Claim `H-quaternionic-obstruction`: the **averaged** characteristic polynomial has a nonreal root for every nontrivial quaternionic irreducible representation and every simple graph containing a cycle. This does not assert that the individual Hermitian adjacencies have nonreal eigenvalues.

For the compact unitary representation, the commuting antiunitary J has J^2=-1. Each real adjacency eigenspace is J-stable and has even dimension; consequently det(xI-A_s)=Q_s(x)^2 for a monic real-rooted Q_s of degree nd/2. If E Q_s^2 were real-rooted, its real zeros would be even. At any such zero a, E Q_s(a)^2=0 forces Q_s(a)=0 almost surely. Dividing out that common factor and repeating forces a deterministic monic Q_s when its entire degree has been exhausted. This argument also handles repeated zeros and does not merely say that an expected square is nonnegative.

To exclude deterministic Q_s, choose an edge on a shortest simple cycle of length l and vary only its label h. In Tr A_s^l, closed walks with trivial reduction contribute a constant, while shortest cycles through the chosen edge contribute a positive multiple of Re chi(h). No shorter nontrivial closed walk can cancel this term. At identity Re chi=d, and for some h it is smaller: equality for every h would force every unitary rho(h) to be the identity. The characteristic polynomial therefore varies. Its coefficients are continuous, and every nonempty open subset of a compact group has positive Haar measure, so this is variation of the distribution, not merely a measure-zero exception. The argument works for even cycles and bipartite graphs as well as odd cycles. On a forest all fields gauge away; the doublet gives mu_Y^2.

Independent spin-3/2 checks are in `checks/independent_unitary_spin.py`. For C3 let D=x^3-3x and t=2 cos(theta). The four holonomy eigenvalues are exp(+-i theta), exp(+-3i theta), so the determinant is (D-t)^2(D-(t^3-3t))^2. Exact Weyl integration, E t^{2k}=Catalan(k), gives

    E det = D^4-D^2+2
          = x^12-12x^10+54x^8-109x^6+87x^4-9x^2+2.

It is >=7/4 on the real axis; exact isolation returns zero real roots. On K4, 100000 independently sampled SU(2) fields in Sym^3(C^2), seed 20261025, give a nonreal root estimate -0.432185414723+0.214225253417i. The two independent half-samples give imaginary parts 0.214609652578 and 0.213840032251. Representation-unitarity and Kramers-pair residuals are below 8e-15. The script prints every coefficient and its pointwise standard error. This is NUMERICAL corroboration, not a certified root enclosure; the exact obstruction above supplies the theorem.

## H5. HPS, the doublet dichotomy, and finite equivalences — VALID

Claims `H-doublet-dichotomy` and `H-unitary-average` are PROVED under their stated hypotheses. For an irreducible doublet, nontrivial determinant makes Lambda^0, Lambda^1, Lambda^2 pairwise nonisomorphic irreducibles, so P1 applies. Trivial determinant puts the unitary image in SU(2), where H3/H4 apply. **Nontrivial determinant alone is not asserted to imply P1 in arbitrary dimension.** For example an irreducible quaternionic four-dimensional representation tensored with a nontrivial character need not have irreducible second exterior power.

The manuscript check confirms the indexing and the exact polynomial: HPS Theorem 1.8 identifies the characteristic-polynomial average for a P1 representation of dimension d with the average **matching** polynomial of d-sheeted covers. For S_r standard, d=r-1; its expected new characteristic polynomial is mu_{r-1,Y}, while its full characteristic polynomial includes the fixed base factor det(xI-A_Y). Theorem 2.7 gives real roots in the universal-cover interval for loopless graphs; Remark 1.12 and Corollary 5.6 include compact U(d). Existence is one-sided on a general graph; bipartiteness gives both sides. The lane cites the right results. [HPS author manuscript, pp. 5–7, 14–15, 32](https://www.ias.edu/sites/default/files/math/csdm/15-16/HallPuSa2016.pdf).

For an independent U2/K4 calculation, `independent_haar.py` constructs every DFS-gauged **2-cover**, computes its ordinary matching polynomial by vertex deletion, and averages. This gives

    x^8-12x^6+42x^4-40x^2+6.

This differs from averaging the new part of a 2-cover, which has degree four. The lane's separate S3 standard calculation correctly uses 3-covers for the new-part comparison.

For U3/Petersen, `independent_unitary_spin.py` applies the differential operator

    product_{uv in E} sum_{k=0}^d (-partial_u partial_v)^k/[k! (d)_k]

to product_v z_v^d, then sets each z_v=x as it leaves the active graph. This is a vertex-elimination calculation in exact FLINT rationals, independently implemented rather than the lane's enumeration of edge multiplicity assignments. It reproduces all 31 coefficients, isolates all 30 roots in the band, and gives largest root

    2.7297814168653852866211304750417748.

For `H-finite-equivalences`, the reductions follow from the verified mixed exterior kernels, not raw design moments. An irreducible determinant-one doublet has the SU(2) kernels; the two nontrivial 2T character twists have nontrivial determinant and U2 kernels. Both A5 triples are oriented real irreducible representations: Lambda^1 and Lambda^2 are identified by Hodge star, and Lambda^0=Lambda^3=1. This fixes also the off-diagonal kernels and gives precisely the SO3/A4 calculation in compatible oriented bases. This checks the possible hidden basis dependence. The twists are faithful: a kernel element has scalar untwisted image, hence is +-1, and its C3 character is 1 there. The lane's finite tables and kernel scripts are rerun and compared in the audit below.

## H6. Fixed root moments and the limit — VALID, PROVED independently

Claim `H-unitary-root-limit`: for a fixed finite regular graph with q>=1, the normalized kth root moment differs from that of its universal covering tree by O_{Y,k}(1/d).

The lane correctly uses S_{d+1} standard, not the permutation representation on d sheets. On a trivial free word its trace is d; on a nontrivial word it is Fix(word)-1. For products of finitely many such fixed-point counts, expand by trajectories and identify equal sheet indices. Consistency requires injective partial permutations in each color. A pattern with v distinct labels and e distinct permutation constraints contributes (r)_v/product_i(r)_{e_i}, where r=d+1. Every component contains one of the nontrivial freely reduced closed words. A graph without a cycle has no nontrivial reduced closed walk, hence each component has e>=v. This includes words which are proper powers, repeated constraints and coincident starting labels. Thus each pattern is O(1), and there are only finitely many at fixed total length. This establishes the joint-moment bound without an independence assumption between the words.

Write Tr A^k=d a_k+R_k. Coefficientwise in a formal variable t,

    log E det(I-tA) = -d sum_k a_k t^k/k
                     + log E exp(-sum_k R_k t^k/k).

Every fixed coefficient in the second term is a polynomial in finitely many bounded joint moments. Newton's logarithm identity now gives sum_j lambda_j^k=d a_k+O(1). Since a_k=n times the tree return count, normalization yields the stated rate. HPS supplies a common compact real support, which converts moment convergence to weak convergence. The tree resolvent equations in the lane give the Kesten–McKay density; q=1 is the arcsine case. No convergence of expectations of logarithms is substituted for this calculation.

An independent sixth-moment derivation uses independent triples in the line graph of a 3-regular d-cover of K4. Put N=4d, M=6d. Then

    m1=M,
    m2=binom(M,2)-3N,
    E m3=binom(M,3)-3N(M-2)+6M-N-4.

The last 4 is the expected number of triangles: each base triangle has expected one closed lift. Newton identities applied to these three coefficients give normalized sixth moment 87-6/d, hence **693/8 at d=16**. The script prints this symbolic derivation. It does not compute or import the full d=16 polynomial.

The body's strong-convergence warning is also PROVED: for even N, (1-exp(-N))x^N+exp(-N)(x-a)^N is positive on R, despite almost-sure strong convergence of the underlying matrices to zero. Its roots lie on an Apollonius circle with radius ratio tending to exp(-1), bounded away from zero. The Bordenave–Collins attribution was checked against `refs/src/1801.00876/tenseur9.tex:343` and `:354`; the Haar-unitary attribution is distinguished there at `:312`. The [Collins–Male publication abstract](https://www.numdam.org/articles/10.24033/asens.2211/) also explicitly verifies convergence of normalized traces and norms after adjoining independent Haar unitaries. These random-spectrum results are not a substitute for the formal-series argument.

## K1. Bounded holonomy and matched endpoints — VALID, PROVED

Claim `prop:su11-gauge-compact-unitary`: compact holonomy closure is equivalent to a positive vertexwise parallel metric, hence to vertexwise unitarizability. Average a positive Hermitian form over the compact closure at a base vertex, and transport it along a tree. Holonomy invariance makes that transport independent of the path. Factor the resulting positive forms as L_v^dagger L_v; the transformed edge maps are Euclidean unitary. Conversely such a metric bounds every base-point holonomy operator, and its closure is compact. The vertex block similarity preserves the entire characteristic polynomial and Jordan structure.

The stronger SU(1,1) statement also follows directly. If h>0 is invariant, h^{-1} eta is h-self-adjoint, has one positive and one negative eigenvalue, and commutes with holonomy. Its two eigenlines are respectively positive and negative for eta. Choosing an eta-orthonormal basis and adjusting its determinant conjugates the group, within SU(1,1), into diag(e^{i theta},e^{-i theta}). There is a single compact torus here, not independent arbitrary U(1) factors.

“Matched endpoints” is necessary and correctly included. For a unitary field on a regular graph of degree D=q+1, the two energy identities in the lane identify the +D eigenspace with parallel sections and the -D eigenspace with anti-parallel sections. The latter requires rho(c)v=(-1)^{length(c)}v for **all** closed walks; it need not accompany +D on a nonbipartite graph. A similarity transports these spaces. One may compare full spectra, or remove the same geometrically identified sectors on both sides. Removing every occurrence of the numerical value D is unjustified for an unbounded field. Boundedness alone gives reality and semisimplicity, not the band inequality.

The lane's endpoint counterexamples and sign convention are valid. In the record labels M=[[A,-qI],[I,0]], J_H=[[0,H],[-H,0]],

    Q = J_H(M-q M^{-1})/2 = [[H,-HA/2],[-HA/2,qH]],
    M^dagger J_H M=q J_H,     M^dagger Q M=q Q.

For R=[[0,I],[-I,0]], R M R^{-1}=[[0,-I],[qI,A]] and R^dagger J_H R=J_H. Thus the page's Q has diagonal blocks qH,H and positive cross term HA/2, without an overall sign flip. `independent_krein.py` verifies these block identities on the exact K4 matrix. Q is an ordinary Hermitian form; A is self-adjoint for H.

## K2. Exact rigidity counterexamples — VALID

Claim `cex:su11-krein-ramanujan-rigidity` is VALID as a refutation. In the theta example the actual graph is two vertices joined by three parallel edges, each of length one. Its degree sequence is (3,3), so q=2 and the band [-2 sqrt(2),2 sqrt(2)] is legitimate. A subdivided theta graph would generally be irregular, but that is not the lane's example. **The assertion “the theta graph is not regular” in the review brief is incorrect for this explicitly specified graph.**

With g=[[5/4,3/4],[3/4,5/4]], h=diag((-3+4i)/5,(-3-4i)/5), and S=I+g+h, direct arithmetic gives

    S = [[33/20+4i/5,3/4],[3/4,33/20-4i/5]],
    A_theta = [[0,S],[adj(S),0]],
    A_theta^2=(14/5)I,       det(xI-A_theta)=(x^2-14/5)^2.

The annihilator x^2-14/5 is squarefree; the eigenvalues are +-1.673320053068151095956344051570..., each twice and strictly in band. For K4 the direct 8-by-8 rational-complex determinant is

    det(xI-A) = [(x-1)(x^3+x^2-5x-29/5)]^2
              = x^8-12x^6-(8/5)x^5+(238/5)x^4+(48/5)x^3
                -(1724/25)x^2-(232/25)x+841/25.

The reduced polynomial p annihilates A exactly and gcd(p,p')=1. Its four roots, each with full multiplicity two, are approximately

    -2.06049372360344689926602155,
    -1.22930452222911100778706671,
     1,
     2.28979824583255790705308826.

The independent script prints the full A matrix and rational isolating intervals proving strict-band reality; the decimal roots are 60-digit evaluations, not the certification. The annihilator proves semisimplicity.

Holonomy is not merely noncommuting: g has eigenvalues 2 and 1/2 and boundary fixed points {+1,-1}, while h sends z to (-7-24i)z/25 and does not preserve that pair. Any finite boundary orbit invariant under a hyperbolic element must lie in its two fixed points. Thus the group is nonelementary and unbounded. The exact commutator difference is gh-hg=[[0,-6i/5],[6i/5,0]]. Noncommutation alone would not prove nonelementarity; the endpoint argument supplies the missing strength.

The body’s supplementary examples also survive review. A parabolic two-edge cycle has A^2=4I and semisimple adjacency at the closed band edges; its transfer is defective. An ordinary simple C_m, m>=3, has eigenvalues r+r^{-1} with r^m an eigenvalue of holonomy. Hyperbolic holonomy fails reality or the band bound. For noncentral parabolic holonomy, applying r+r^{-1} to a size-two forward-shift Jordan block preserves that block unless r=+-1; for m>=3 some root avoids those values. Thus ordinary simple cycles cannot furnish a smaller counterexample, and K4 is minimal among simple regular graphs in the lane's setting. The unbounded K4 isospectral family with h=I has reduced polynomial (x^2-1)(x^2-5); the independent script verifies its direct determinant and annihilator symbolically for all rational Cayley parameters, hence for the full real hyperbolic family. Finally, simple real reduced roots persist under sufficiently small perturbations of a real polynomial. Hyperbolicity and failure to preserve the endpoint pair persist too, proving the stated open nonelementary Ramanujan locus.

## K3. Pfaffian doubling, balanced inertia, and defective fields — VALID

Claims `prop:su11-adjacency-pfaffian`, `prop:su11-balanced-krein-count`, and `prop:su11-weil-inertia` are PROVED with the hypotheses stated in the lane. The review brief's proposed square-minus-one explanation must be corrected.

For U=[[a,b],[conjugate(b),conjugate(a)]], set C=(I tensor sigma_x) followed by conjugation. Then

    C^2=+1,     CA=AC,     [Cu,Cv]_H=-conjugate([u,v]_H).

This is a **real structure and an anti-isometry**, not the compact SU(2) quaternionic structure. A commuting C with square +1 does not by itself imply even eigenspace dimension. Indeed an antilinear operator squaring to -1 cannot commute with the full defining SU(1,1) representation: the hyperbolic element g would force each of its one-dimensional real-eigenvalue spaces to support such an operator, which is impossible.

The independent source of doubling is the nondegenerate alternating form E=I tensor [[0,1],[-1,0]]. The identity U^T E_2 U=E_2 on each edge, together with the reverse-edge inverse, gives A^T E=EA. Hence E(xI-A) is skew-symmetric and its Pfaffian divided by Pf(E) is a monic degree-n square root of det(xI-A). Reality follows from CA=AC and uniqueness of a monic square root. Generalized eigenspaces for different eigenvalues are orthogonal for E, so each generalized eigenspace is nondegenerate for E. If the reduced root is simple, that space has dimension two; an E-self-adjoint endomorphism of a two-dimensional symplectic space is scalar. This proves semisimplicity in the simple-reduced-spectrum case without assuming it from even algebraic multiplicity.

For a **real semisimple** eigenvalue, its eigenspace is nondegenerate for H: H-self-adjointness pairs only conjugate generalized spectral subspaces, and the real spectral summand pairs with itself. C preserves that space and reverses H-signs, forcing inertia (m,m,0). Consequently kappa_B is half the full real in-band multiplicity, equivalently the reduced root count with multiplicity. At a defective eigenvalue its ordinary eigenspace can have a radical; the lane correctly excludes this from the original count. Balanced positive and negative indices alone do not imply zero radical. The collision computation below explicitly gives a two-dimensional totally null eigenspace.

For Q on the doubled label space, C direct-sum C is again an antilinear anti-isometry, so n_+(Q)=n_-(Q), even when A is defective. Completing the square yields the congruence

    Q congruent to H direct-sum H(qI-A^2/4).

Since H is invertible and q>0,

    dim ker Q = dim ker(A-2 sqrt(q)I) + dim ker(A+2 sqrt(q)I) = d0.

The equality follows by the coprime factorization of A^2-4qI and uses **geometric**, not algebraic, multiplicities. The label dimension is 4n, hence

    In(Q)=(2n-d0/2, 2n-d0/2, d0).

The independent exact rank calculations give Q rank 16 at the defective K4 collision with its true q=2, so In(Q)=(8,8,0). At the later actual band crossing, cosh(t)=(31+30 sqrt(2))/16, rank Q=14 and In(Q)=(7,7,2). A sharper defective-edge test uses the *same collision matrix* with an explicitly external positive parameter q=25/36: the -5/3 eigenvalue has algebraic multiplicity four but geometric multiplicity two, rank Q=14, and inertia (7,7,2). Using algebraic d0=4 would give the wrong nullity. This auxiliary cutoff is not claimed to be K4's regular-graph q.

The body's general semisimple inertia formula is also VALID. A strictly in-band real spectral subspace of H-signature (a,b) contributes (2a,2b); an edge contributes (a,b,a+b); a real out-of-band subspace of dimension m contributes (m,m); a conjugate nonreal pair of total dimension 2m contributes (2m,2m) on labels. This follows from the same Schur congruence and the neutral pairing on the nonreal pair. Thus the formula using r_+,r_-,e_+,e_-,o,z has the correct factors of two.

Finally the distinction concerning an invariant positive metric is VALID. If A is real semisimple and strictly in band, the two transfer roots above each adjacency eigenvalue are distinct and on the critical circle; M/sqrt(q) is diagonalizable with unimodular spectrum, hence preserves a positive Hermitian metric obtained by pulling back the Euclidean metric in an eigenbasis. At an adjacency band edge the companion produces a nontrivial Jordan block. A nontrivial adjacency Jordan block cannot coexist with a diagonalizable M because A direct-sum A=M+qM^{-1}. The fixed indefinite Q and existence of some positive invariant metric are different claims.

## K4. First interior collision — VALID, PROVED and recomputed

Claim `prop:su11-k4-interior-collision`: keeping cotree labels -I,g_t,h, with g_t=exp(t sigma_x), the first failure is a defective interior collision at t*=arcosh(79/54).

`independent_krein.py` uses r=tanh(t/2), c=(1+r^2)/(1-r^2), b=2r/(1-r^2), makes a constant exact similarity to real coordinates, and computes the full characteristic determinant over the rational-function field. This is independent of the lane's half-trace Newton derivation. It gives the square of

    p_t(x)=(x-1)[x^3+x^2-5x-(9+16c)/5],
    disc(cubic)=-(64/25)(2c+3)(54c-79).

For 1<=c<79/54 the cubic has three distinct real roots and never takes x=1 as a root. Its two negative roots move from -sqrt(5),-1 towards -5/3; its positive root moves from sqrt(5) to 7/3. Thus no root reaches the q=2 band edge first. At

    t*=log((79+5 sqrt(133))/54)
      =0.928532626312458727195051893511588718301778443710...

the reduced polynomial is (x-1)(x-7/3)(x+5/3)^2. Exact field row reduction gives

    rank(A+5I/3)=6,     rank((A+5I/3)^2)=4.

The generalized -5/3 space has dimension four and kernel dimension two; the second kernel already has dimension four. Therefore its Jordan blocks are exactly two blocks of size two. The independent kernel basis has zero H-Gram matrix. The claim is about the **first failure of semisimplicity** at t*, followed immediately by nonreal roots, not nonreal roots already at t*. Substituting x=-5/3+y and c=79/54+delta reduces the cubic to y^3-4y^2-(16/5)delta, yielding y=-delta/10 +- i(2/sqrt(5))sqrt(delta)+O(delta^{3/2}) as stated. The in-band negative count drops from 4 to 2 across the collision while full Q inertia stays (8,8,0).

## K5. Unicyclic graphs, theta formulas, and semicontinuity — VALID

Claim `prop:su11-unicyclic-theta-formulas` is PROVED, including its parabolic qualification. Gauge a unicyclic graph to identity except for one cycle edge with holonomy g. If g is diagonalizable with eigenvalues w,w^{-1}, the two scalar-flux determinants coincide: both depend on w+w^{-1}=tr(g). Relative to the untwisted scalar determinant, the only affected Leibniz components are the two orientations of the unique full cycle; their common complement contributes chi_F. Thus

    p_g(x)=chi_Y(x)+(2-tr(g))chi_F(x),
    det(xI-A_g)=p_g(x)^2.

Polynomial continuation in the matrix entries extends this identity to noncentral parabolic g. Attaching a path and applying vertex deletion proves the stated Chebyshev lollipop formula, with U_{-1}=0. Graphs with genuine attached trees are irregular; the lane explicitly treats b as an external adjacency cutoff and does not call qI their Bass degree term.

For **three independently generated random graphs**, seed 20261025, with cycle lengths 3,4,5 and three attached vertices apiece, `independent_krein.py` directly computes the 12-,14-,16-dimensional characteristic matrices over Q(i). The holonomies are rational KAK products with Cayley parameters

    (r,u,v)=(2/7,5/7,4/11), (3/7,-3/7,-3/11), (4/7,5/7,-4/11).

They have exact traces -38584/45621, 427/650, and 564200/167277 respectively. Each satisfies det(g)=1 and g^dagger eta g=eta exactly, and every determinant equals the proposed square. The script prints the edge lists, all holonomy entries, chi_Y, chi_F, and p_g, so these are reproducible tests rather than rounded hyperbola samples.

For the stronger parabolic Jordan formula, in a Jordan fibre basis the matrix is [[B_epsilon,epsilon K],[0,B_epsilon]], with B_epsilon real symmetric and K=E_uv-E_vu real skew-symmetric. Diagonalize B_epsilon orthogonally. A block upper-triangular similarity removes each off-resonant block by division by lambda-mu; it introduces no further terms because the upper-block ideal has square zero. The remaining block at lambda is [[lambda I,epsilon P_lambda K P_lambda],[0,lambda I]]. If m=dim E_lambda and r=rank(P_lambda K P_lambda), it has r size-two blocks and 2m-2r size-one blocks. Its eigenspace inertia is (m-r,m-r,r): the surviving y-components lie in ker(PKP), pair nondegenerately with an equally sized set of x-components, and the r remaining x-components are radical. This proves the lane's formula, including the difference from the generalized space's inertia (m,m). The independent script tests defective parabolic C3 and C4 and semisimple parabolic triangle-plus-leaf.

For the two-vertex theta, linearity of the 2-by-2 adjugate gives A^2=delta I with delta=3+tr(g)+tr(h)+tr(gh^{-1}). If delta is positive the roots are real semisimple, if negative they are nonreal, and at zero either S=0 gives A=0 or S and adj(S) both have rank one and A has two nilpotent size-two blocks. In the latter case ker A=im A and H-self-adjointness implies [Av,Aw]=[v,A^2w]=0; the eigenspace really is totally null. This verifies the complete theta classification.

Claim `cex:su11-krein-count-semicontinuity` is VALID. The fixed-h theta family has delta=(9+4 cosh(t))/5. At cosh(t)=31/4 it reaches 8 and the closed-band count is 2; immediately beyond it the count is 0. These fields remain nonelementary. At the separate interior example with R=diag(exp(2pi i/3),exp(-2pi i/3)), S_t=(exp(t sigma_x)-I)R, so delta=2-2 cosh(t). At zero A=0 is semisimple and kappa=2; at every nonzero t the spectrum is imaginary and kappa=0. Exact substitution t=log(2) gives A^2=-I/2 in our script. The first example refutes lower semicontinuity within the unbounded locus; the second refutes it on the full field space even away from band edges. Local constancy remains valid on strata with simple reduced real roots separated from each other and the band boundary.

The omitted bounded-count refutation is also VALID: theta labels I,I,diag((4+3i)/5,(4-3i)/5) have compact nontrivial holonomy and A^2=(41/5)I, hence kappa=0 rather than n=2. Compactness does not imply an in-band spectrum.

## K6. Proposed record corrections

**Lane H replacement: AGREE-WITH-CHANGE.** Its mathematics is correct. State the graph scope and preserve the one-sided existence qualification in the replacement itself. Suggested complete wording:

> For a finite loopless (q+1)-regular graph with q>=1, the defining U(d) Haar average is the degree-nd d-matching polynomial of Hall–Puder–Sawin and has all roots in [-2 sqrt(q),2 sqrt(q)]. The standard representation of S_r gives the (r-1)-matching polynomial. The cover-existence theorem is one-sided in general and two-sided for bipartite graphs. For the defining SU(2) doublet on a simple graph, the average is the sum, over vertex-disjoint cycle collections, of the squared matching polynomial of the remaining graph. On K4 it is (x^4-6x^2+3)^2+4x^2+3, with no real roots. Every nontrivial quaternionic irreducible representation fails averaged real-rootedness on every simple graph containing a cycle.

**Lane K replacement: AGREE-WITH-CHANGE.** The proposed paragraph is correct, but should also correct the page's description of Q and retain the distinction between the fixed form and an arbitrary invariant positive metric. Suggested complete wording:

> Unbounded, even nonelementary, SU(1,1) holonomy can have real semisimple adjacency spectrum strictly inside the Ramanujan band. In the defining representation the characteristic polynomial is a real monic square, and every real semisimple eigenspace has equally many positive and negative directions for the inherited form H=I tensor diag(1,-1). The canonical Weil form Q is an ordinary Hermitian form; away from adjacency band edges it has inertia (2n,2n), even through an interior defective collision. It is therefore indefinite when the transfer spectrum lies strictly on the critical circle. Existence of some invariant positive metric for the normalized transfer is a separate question; real semisimple adjacency spectrum strictly inside the band does give such a metric. At the band edges the companion transfer is defective and Q is singular.

The lane H annotations to `graph-super.md` §6 and `zn-flux.md` §4 are **AGREE**: the scalar result survives, includes the trivial flux assignment, and requires a nontrivial character/N>=2. The corrected HPS cover index and one-sided existence statement should accompany any citation. The lane K companion-label correction and strict-band qualification are **AGREE**. The proposed `data-ladder.md` observation that compactness or finite image alone does not imply averaged RH is **AGREE**. The fixed-form/invariant-metric distinction does not refute the registered abstract invariant-polarisation theorem.

## Additional body claims and coverage of the protocol

The candidate tables contain eighteen rows, all adjudicated below. To avoid silently omitting proved/refuted claims without candidate IDs, the following supplemental aliases are assigned by this reviewer; their derivations are included above or here.

| Supplemental alias | Restated claim and independent adjudication |
|---|---|
| H-scalar-average | VALID: every nontrivial scalar character gives the matching polynomial, with normalized Haar and no deleted flux factor; H1. |
| H-trail-parity-refutation | VALID: the general parity/simple-cycle-weight ansatz is false. The independent full enumeration of all 1728 A4/K4 fields gives x^12-18x^10+117x^8-332x^6+393x^4-16x^3-158x^2-11/9. In particular the nonzero x^3 coefficient refutes even parity. The determinant's projected color cycles can revisit a base vertex, so a scalar weight per disjoint base cycle is not the general expansion; H2 supplies the actual contractions. |
| H-counterexample-minimality | VALID: C3, Q8 and the separate loop/multigraph/q=0 qualifications have the precise minimality scope checked in H3 and K2. For the parallel-edge polynomial, write the sum of three unit quaternions S: E det(S)=3 and Var(det(S))=3, giving (x^2-3)^2+3. |
| H-strong-convergence-inputs | VALID: the local Bordenave–Collins source distinguishes permutation strong convergence from the earlier Haar-unitary result; neither identifies expected-polynomial roots. H6 checks the cited scope and supplies the required extra proof. |
| H-strong-convergence-warning | VALID: the exponentially rare scalar matrix example disproves the purported inference from strong convergence to real-rooted expected determinants or their root-measure convergence; H6. |
| prop:su11-companion-conventions | VALID: the two companion matrices are symplectically conjugate; the Q cross term changes sign without an overall sign reversal; K1 and exact matrix identities. |
| prop:su11-endpoint-sectors | VALID: geometrically parallel/anti-parallel sectors, not numerical degree-valued eigenvalues, control removal of trivial modes; K1. The lane's accidental theta eigenvalue example has delta=9 and det(g-I)=-16, checked in the rerun. |
| prop:su11-simple-cycle | VALID: the holonomy eigenvalues require m-th roots, hyperbolic simple cycles fail the band/reality test, and noncentral parabolic simple cycles are defective; K2/K5 and exact C3–C5 reruns. |
| prop:su11-k4-isospectral | VALID: the entire hyperbolic family with h=I has squarefree annihilator (x^2-1)(x^2-5), independently computed symbolically; K2. |
| prop:su11-open-ramanujan-locus | VALID: simple real reduced roots in the strict band and the stated nonelementary condition persist in an open neighbourhood of the exact K4 example; K2. |
| cex:su11-bounded-count | VALID: compact theta flux with delta=41/5 has kappa=0, refuting the unconditional bounded count n; K5. |
| prop:su11-general-weil-inertia | VALID: the semisimple formula for an arbitrary H-self-adjoint adjacency has the stated in-band, edge, outside-band and nonreal-pair contributions; K3. |
| prop:su11-positive-invariant-metric | VALID: strict-band real semisimple adjacency gives a positive invariant transfer metric, while adjacency edges/Jordan blocks preclude one; this does not make the fixed Q positive; K3. |

The finite-sum formula |G|^{-g} sum det(x-A) is already covered by H1 and `H-finite-equivalences`; the Pfaffian simple-root semisimplicity assertion is covered by `prop:su11-adjacency-pfaffian`; the parabolic compression, lollipop, and delta=0 cases are explicitly included under `prop:su11-unicyclic-theta-formulas`. No additional independent PROVED/REFUTED item is left unadjudicated.

## Reproduction audit and numerical scope

All seven input Python files were read. To respect the read-only source lanes, byte-identical copies were placed under `checks/rerun_haar/` and `checks/rerun_krein/`: several scripts write files beside `__file__`. The SHA-256 identity checks and full comparisons are in `checks/output_audit_reruns.txt`.

All six saved text outputs match their reruns **exactly after removing elapsed-time fields only**. Both exact polynomial JSON files match structurally and coefficient-for-coefficient. This includes the complete 100000-sample run in each of eight lane H ensembles, every reported standard error and bootstrap coordinate interval, all 640 lane K samples, and all 149 MP80 follow-ups. No numerical discrepancy was hidden by a tolerance or selective comparison.

`check:su11-five-graph-scan` is VALID **as a NUMERICAL computation**, not a probability theorem or exact classification. The accepted unbounded counts are (43,6,28,22,50) in order K4, Petersen, K5, cube, theta, each out of 64. The sampling distribution and the finite-precision limitations are accurately stated. The 80-digit brackets use floating arithmetic, not interval certification; the exact named examples carry the rigorous refutation. Likewise lane H's Gaussian root-coordinate intervals are pointwise statistical approximations with coefficient covariance, not simultaneous rigorous root regions.

The audit also recomputes finite-table real-root counts by exact Sturm counts on squarefree factors, including multiplicity. All real roots lie even in the rational inner interval [-14/5,14/5]. The independent A4/K4 enumeration does not use the lane's conjugacy-orbit reduction; the independent SU(2), U(2), U(3), spin-3/2 and SU(1,1) calculations are described with their different routes above. Exact rational/algebraic arithmetic is used wherever claimed. Decimal roots and Monte Carlo estimates have the precision/limitations stated at their point of use.

Reproduce the independent checks from this review directory:

```sh
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 checks/independent_haar.py
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 checks/independent_unitary_spin.py
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 checks/independent_krein.py
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 checks/audit_reruns.py
```

The copied original programs can be rerun with their original arguments from this directory, replacing `checks/` by `checks/rerun_haar/` or `checks/rerun_krein/`; redirect stdout for the Haar programs to their corresponding `output_*.txt` paths before running the audit. The Krein program writes its own log. No copied source was modified.

## Correction ledger for the review brief

| Potential trap | Finding |
|---|---|
| “The theta graph is not regular” | Incorrect for the stated two-vertex, three-parallel-edge graph: it is 3-regular and q=2 is legitimate. Subdivision would change the question. |
| SU(1,1) has the same commuting J^2=-1 structure as SU(2) | Incorrect. The lane correctly uses C^2=+1 for reality and sign reversal, and a separate alternating-form/Pfaffian argument for doubling. |
| “Nontrivial determinant implies the HPS polynomial” without a dimension hypothesis | Insufficient in general dimension. It is equivalent to P1 for an irreducible doublet; U(d) defining satisfies all of P1 independently. The lane has the needed qualification. |
| A finite subgroup must be a raw fourth-moment design to reproduce the doublet determinant | Incorrect. Q8 fails degree four but has exactly the required exterior kernels; 2T passes degree five and fails degree six. |
| Expected full characteristic polynomial of a d-cover equals the d-matching polynomial | Incorrect indexing/object. Full r-cover average has the base characteristic factor; the expected new polynomial is mu_{r-1,Y}. The lane's correction is right. |
| Real-rooted average can be inferred from individual Hermitian matrices or strong convergence | Incorrect; the quaternionic expected-square obstruction and rare-event example directly show why. |

## Verdict lines

VERDICT H-gauge-Haar: VALID — normalized conditional Haar invariance proves tree independence.
VERDICT H-exterior-kernels: VALID — the mixed exterior projectors reproduce the determinant block expansion.
VERDICT H-SU2-cycle-squares: VALID — raw S^3 integration and direct Q8 sums reproduce both requested polynomials.
VERDICT H-compact-RH: VALID — the compact-group conjecture is refuted by the strictly positive C3 and K4 averages.
VERDICT H-quaternionic-obstruction: VALID — a nonconstant monic Kramers square cannot have a real-rooted mean square.
VERDICT H-doublet-dichotomy: VALID — nontrivial determinant is exactly the additional P1 condition in dimension two.
VERDICT H-unitary-average: VALID — the polynomial and cover-degree index agree with HPS and independent computations.
VERDICT H-unitary-root-limit: VALID — bounded word-count moments justify the formal logarithm and the O(1/d) rate.
VERDICT H-finite-equivalences: VALID — compatible exterior kernels give the reductions and all saved tables reproduce.
VERDICT prop:su11-gauge-compact-unitary: VALID — positive parallel metrics give exactly vertexwise unitarizability with matched endpoints.
VERDICT cex:su11-krein-ramanujan-rigidity: VALID — exact nonelementary theta and K4 matrices are semisimple and strictly in band.
VERDICT prop:su11-adjacency-pfaffian: VALID — symplectic self-adjointness gives a real monic square and simple reduced roots force semisimplicity.
VERDICT prop:su11-balanced-krein-count: VALID — the C^2=+1 anti-isometry balances every nondegenerate real eigenspace.
VERDICT prop:su11-unicyclic-theta-formulas: VALID — exact rational tests and the resonant skew compression verify the full formulas.
VERDICT cex:su11-krein-count-semicontinuity: VALID — both the closed-band crossing and the interior collision refute lower semicontinuity.
VERDICT prop:su11-weil-inertia: VALID — anti-isometry and Schur congruence give the formula with geometric edge multiplicity.
VERDICT prop:su11-k4-interior-collision: VALID — the direct determinant and exact ranks certify the first defective collision at the stated parameter.
VERDICT check:su11-five-graph-scan: VALID — all numerical outputs and ensemble summaries reproduce with their stated limitations.
VERDICT H-scalar-average: VALID — independent edge integration kills scalar cycles and retains precisely dimers.
VERDICT H-trail-parity-refutation: VALID — the independently enumerated SO3 K4 polynomial has the forbidden x^3 term.
VERDICT H-counterexample-minimality: VALID — the stated simple-graph and finite-group minima respect every exceptional convention.
VERDICT H-strong-convergence-inputs: VALID — the cited random-spectrum theorems have the scope distinguished by the lane.
VERDICT H-strong-convergence-warning: VALID — exponentially rare scalar matrices disprove the expected-polynomial inference.
VERDICT prop:su11-companion-conventions: VALID — exact block multiplication confirms the symplectic coordinate change and Weil signs.
VERDICT prop:su11-endpoint-sectors: VALID — unitary energy identities identify the sectors that may be removed.
VERDICT prop:su11-simple-cycle: VALID — the corrected holonomy-root formula proves the hyperbolic and parabolic exclusions.
VERDICT prop:su11-k4-isospectral: VALID — direct symbolic determinants and annihilators verify the entire hyperbolic family.
VERDICT prop:su11-open-ramanujan-locus: VALID — simple real strict-band reduced roots and the exhibited nonelementarity persist locally.
VERDICT cex:su11-bounded-count: VALID — compact theta flux has delta=41/5 and zero in-band negative count.
VERDICT prop:su11-general-weil-inertia: VALID — spectral Schur congruence gives all four semisimple contributions with correct multiplicities.
VERDICT prop:su11-positive-invariant-metric: VALID — unimodular diagonalizability controls metric existence independently of the fixed Weil form.

## Numerical checks for the blind lane

Run the commands above; the corresponding saved outputs are `checks/output_independent_haar.txt`, `checks/output_independent_unitary_spin.txt`, and `checks/output_independent_krein.txt`.

1. **K4 SU(2):** x^8-12x^6+42x^4-32x^2+12 = (x^4-6x^2+3)^2+4x^2+3, by both raw continuous Haar integration and direct Q8 enumeration.
2. **C3 SU(2):** x^6-6x^4+9x^2+1 = (x^3-3x)^2+1, by the same two independent routes.
3. **K4 SU(1,1):** det(xI-A)=[(x-1)(x^3+x^2-5x-29/5)]^2; largest eigenvalue 2.28979824583255790705308826249058774889855..., semisimple and strictly in band.
4. **Collision parameter:** t*=arcosh(79/54)=0.928532626312458727195051893511588718301778443710...; reduced polynomial (x-1)(x-7/3)(x+5/3)^2.
5. **Collision ranks:** rank(A+5I/3)=6 and rank((A+5I/3)^2)=4; In(Q)=(8,8,0) at the true q=2, including the defective point.
6. **Other independent anchors:** Petersen SU(2) constant 57; K4 U(2) constant 6; Petersen U(3) largest root 2.7297814168653852866211304750417748; K4 U(16) normalized sixth moment 693/8.

## What this changes in the notebook

All **18 candidate rows** survive as written within their stated hypotheses: 18 VALID, 0 MINOR, 0 INVALID, 0 UNVERIFIED. The thirteen supplemental body adjudications are also VALID. A VALID verdict on `H-compact-RH` validates its **REFUTED** status; it does not assert compact-group averaged RH. The two `cex:` candidates likewise remain proved counterexamples. `check:su11-five-graph-scan` remains NUMERICAL, never promoted to an exact sampling-law theorem.

| Record destination | Reviewed change |
|---|---|
| `gauge-groups.md`, U(d)/SU(2)/S_r paragraph | Replace the open averaging claim with the HPS identification, corrected cover index, one-sided existence qualification, and SU(2)/quaternionic obstruction; use K6's wording. |
| `gauge-groups.md`, SU(1,1) paragraph | Record the exact nonelementary counterexamples, Pfaffian square, balanced real eigenspaces, and fixed-Q/invariant-metric distinction; use K6's wording. |
| `graph-super.md` §6 and `zn-flux.md` §4 | Retain scalar averaging; annotate that it does not extend to arbitrary compact representations and includes the trivial flux assignment. |
| `lattice-tower.md` §5 and companion restatements | Retain the polarisation-orientation qualification; keep strict-band transfer semisimplicity separate from closed-band adjacency, and align the label convention. |
| `data-ladder.md` | Add that averaged RH depends on graph, representation and ensemble, while finite image or compactness alone is insufficient. |

No record file, registry, or source lane has been changed. The next gate is the required second-family review, especially of the mixed exterior contraction and the separation of SU(1,1)'s real anti-isometry from its symplectic doubling. The original compact-group averaged-RH conjecture and Krein–Ramanujan rigidity conjecture remain decisively refuted; there is no new unresolved numerical obstruction in this review.

