# REFUTE review RJ: Ramanujan fluxes, polarizations, and Jacobians

Author: `codex:gpt-6-astra` (reviewer), 2026-10-25.

This is a same-family adversarial review of lane J of 2026-10-23. It does not satisfy the record's additional second-family review gate. No claims are registered and no record page is edited. All fresh computations and rerun copies are confined to this review directory. Verdicts below apply to the stated scope, especially **isogeny class** versus **integral polarized lattice**.

## RJ1. The dictionary — VALID

**PROVED.** The object is exactly the abelian group `T = Z^n ⊕ Z^n` with

\[
F=\begin{pmatrix}A&-pI\\I&0\end{pmatrix},\qquad
V=\begin{pmatrix}0&pI\\-I&A\end{pmatrix}.
\]

It is free of rank `2n` over Z, hence finitely generated and Z-torsion-free. Multiplication gives `FV=VF=pI` and `F+V=diag(A,A)`: the latter is **not** literally the n-by-n matrix A. The commuting operators make T a module over `Z[f,v]/(fv-p)` and its finite image order `Z[F,V]`; there is no requirement that it be free of rank one over that order. In particular, “torsion-free” must specify the underlying Z-module, not mean a faithful module over the unreduced universal ring.

An equivalent presentation is `Z^n[t]/(t²I-tA+pI)Z^n[t]`, with t acting by multiplication. Division by the monic matrix polynomial leaves a unique vector polynomial of degree at most one, so its Z-rank is 2n. The integral isomorphism sends `u+t v` to `(u+Av,v)`; under it multiplication by t is the displayed F. A bare tensor product `Z^n ⊗ Z[F]/(F²-AF+p)` is ambiguous unless the matrix-valued relation is specified.

Since A is real symmetric, its eigenspaces give two-dimensional blocks with characteristic polynomial `x²-λx+p`. Strictness means **every** signed-adjacency eigenvalue satisfies `|λ|<2√p`; it is not the usual unsigned convention that exempts trivial eigenvalues. Both roots are distinct, nonreal, of modulus √p, and F is semisimple even when A has repeated eigenvalues. Integrality of F proves its roots algebraic integers; all their conjugates occur in its characteristic polynomial and have that modulus. At an endpoint the block has a repeated real root and is not semisimple. Thus strictness does exactly the work claimed.

This checks all hypotheses of Centeleghe–Stix, *Categories of abelian varieties over finite fields I: Abelian varieties over F_p*, Algebra & Number Theory 9 (2015), Theorem 1, [author text, p. 2](https://www.math.uni-frankfurt.de/~stix/research/preprints/CENTELEGHE-STIX-AVFp-part1-20150110.pdf). The theorem is an anti-equivalence with choices; its output has dimension n. Here p=2 for the four cubic graphs and p=3 for K5, both prime fields. Supersingular roots of `x²+p` are allowed; real roots of `x²-p` are excluded. The lane's precise theorem statement corrects its original brief appropriately.

**PROVED (remaining §0 claims).** Equality in the regular adjacency norm bound forces a constant-modulus extremal eigenvector, hence +d exactly for balanced signings and −d exactly for antibalanced signings. Nontrivial flux alone does not remove −d. Block multiplication verifies the symplectic conjugacy with the old step and `Ω(F−V)=[[2I,−A],[-A,2pI]]`; its Schur complement is `(4pI−A²)/2`. Finally, `P(u)=det(I-uF)` is an H¹ polynomial; `P/((1-u)(1-pu))` is a curve-zeta candidate, `P_s/P_0` is the full graph super ratio, and `det(I-F^k)` counts points of the abelian variety. These are distinct constructions in higher dimension.

## RJ2. K4 trigonal Jacobian class — VALID

**PROVED, independently reproduced.** The actual equations reviewed are

\[
XY+Z^2=0,\qquad T^3+T^2X+T^2Z+TX^2+TYZ+Y^3=0.
\]

`python3 checks/review_k4.py` enumerates normalized projective points, first filtering by the quadric and then evaluating the cubic. It uses fresh binary-field moduli, not the lane's field class. For k=1,…,8 its counts are **3, 9, 9, 29, 33, 69, 129, 285**. Every enumerated curve point has Jacobian rank two. Finite-degree checking alone would not establish geometric smoothness; the following elimination does.

On X=1, put Y=Z² and write

\[
G=T^3+(1+Z)T^2+(1+Z^3)T+Z^6.
\]

Then `G_T=T²+1+Z³` and `G_Z=T(T+Z²)`. At a singular point either T=0, which forces Z³=1 and G=1, a contradiction; or T=Z², in which case the equations include

\[
a=Z^2(Z^4+Z^2+1)=0,\quad b=Z^4+Z^3+1=0.
\]

The explicit identity `(Z³+Z²)a+(Z⁵+Z³+1)b=1` in F2[Z] excludes this case. At X=0 the quadric forces Z=0. The cone vertex is excluded because C(0,0,0,1)=1; the remaining chart Y=1 has T³=1 and `C_T=T²≠0`. This proves smoothness over the entire algebraic closure, independently of the lane's Gröbner calculation.

The quadric is integral and C is not its multiple, so this is a degree-six complete intersection. Its Koszul resolution gives `H⁰(O_C)=F2`, also after base change; smoothness then implies geometric connectedness and irreducibility. Adjunction gives `ω_C=O_C(1)` of degree 6, hence genus 4, and the displayed embedding is canonical. The ruling of the cone restricts to a degree-three map (a general ruling meets the cubic in three points; the vertex is absent), so the curve is trigonal.

Recovering `P(u)` from the counts by the exponential of `Σ(N_k−2^k−1)u^k/k` gives

\[
P(u)=1+2u^2+5u^4+8u^6+16u^8.
\]

This equals the graph determinant. Equivalently the **Weil characteristic polynomial** is `W(x)=x⁸+2x⁶+5x⁴+8x²+16`; P and W must not be identified as polynomials in the same variable. The first four counts plus the genus-four functional equation already suffice; degrees five through eight are independent consistency checks. Equality of Frobenius polynomials proves F2-isogeny of the abelian varieties, not equality of their integral modules or principal polarizations.

**PROVED (no hyperelliptic representative).** `review_hyperelliptic_f2.py` independently enumerates smooth raw equations using FLINT polynomial gcds, then explores orbits using generators `y↦y+x^j` (0≤j≤5), `x↦x+1`, and `x↦1/x`. It does not import the lane's minimum-shift or PGL2 routines. Point counting enumerates y directly rather than using an Artin–Schreier trace test. Results:

| Quantity | Independent value |
|---|---:|
| Smooth equations | 49,152 |
| Classes under y shifts | 1,536 |
| F2-isomorphism classes | 264 |
| Distinct L-polynomials | 217 |
| K4 matches | 0 |
| Isomorphism classes having N2=9 | 48 |

All 264 representatives, counts and polynomials agree with the original JSON. The smoothness criterion follows by eliminating y from `h=0`, `f'+h'y=0`, `y²=f`; the second weighted chart supplies the infinity test. Every genus-four hyperelliptic curve over F2 admits this model: its unique degree-two map descends to a genus-zero curve, which splits over the finite field. The listed generators give every base automorphism and every y shift; the only nonzero F2 scaling is 1. Each shift orbit has 32 elements because the shift kernel is `{0,h}`. Thus this really is exhaustive.

The review brief's suggestion of using the lane's N2 bound for K4 needs correction: `N2=9≤10`, so that bound does **not** exclude K4. The independent census supplies the exclusion. The lane itself uses the census correctly. Its additional canonical-model search reruns with 0, 0, 24 smooth matching cubic classes on the three quadrics; these are equation classes, not isomorphism classes. Independently, `review_canonical.py` uses a different row-reduced cubic quotient basis and direct Boolean evaluation of the surviving coefficient vectors, without a Walsh transform. It obtains the same counts and verifies equality of the full 24-element set after changing quotient basis. The affine Jacobian ideals are tested on every chart. The three quadrics cover the canonical genus-four cases: a smooth geometrically integral canonical curve has a unique geometrically integral quadric, which is split smooth, nonsplit smooth, or a cone over F2. The explicit witness above suffices for the positive Jacobian assertion without this auxiliary exhaustive search.

## RJ3. All five K5 classes — VALID

**PROVED, independently reproduced with PARI.** The full unchanged F3 script reruns on all **1,062,882** degree-12 equations and reproduces the saved output. Independently, `review_arithmetic.py` classifies K5 switching classes by all triangle signs under all 120 vertex permutations; this gives five strict orbits `(mask,size)=(1,10),(3,15),(11,10),(12,15),(13,12)`, totaling 62 classes. The two other classes are balanced/antibalanced. Exact leading principal minors certify strictness.

`python3 checks/review_k5.py` sends each displayed f to PARI `hyperellcharpoly(Mod(1,3)*f)`, verifies squarefreeness, and compares the entire degree-ten characteristic polynomial with the graph's W. All five agree. The five results are printed in the blind-check section. Since f is squarefree of degree 12 in odd characteristic, its smooth projective model has genus 5; its two infinity points are handled by the leading coefficient, not by counting the affine plane alone.

**PROVED (different exhaustive enumeration, all five totals).** The independent search uses division by `x⁹−x`:

\[
f=r+(x^9-x)g,\qquad \deg r<9,\quad\deg g=3.
\]

The required `N2=20` is the maximum for a degree-two cover of P1(F9). Therefore every fiber, including infinity, consists of two F9-points: each of the nine values of r must be a nonzero square. Enumerating residues gives **512** possible r. Every quotient g has four F3 coefficients with nonzero cubic coefficient; applying N1=4 leaves **10,368** equations. Of these, **192** are singular. PARI computes the Frobenius polynomial of each of the **10,176** smooth survivors. Matching totals for masks 1,3,11,12,13 are **6,42,6,42,24**, and the complete coefficient-vector sets agree with the lane's JSON, not merely their cardinalities.

Unique polynomial division proves coverage of all degree-12 equations. A squarefree degree-11 model has only one infinity point and at most 18 affine F9-points, so cannot have N2=20. Every genus-five hyperelliptic curve over F3 admits a degree-11 or degree-12 model. Thus the targeted search is exhaustive, while the five explicit witnesses already establish the assertion. These are equation counts, not counts of curve isomorphism classes. In particular, the nonordinary pentagon class is a Jacobian class: a supersingular factor does not itself prohibit Jacobian realization.

## RJ4. J1, its ring, and polarization scope — VALID

**REFUTED (J1 as originally conjectured); the lane's refutation is correct.** Set `C=F+V=diag(A,A)` and let m be the minimal polynomial of A. Reduction by the two monic relations gives

\[
R_0=\mathbb Z[F,V]\cong
\mathbb Z[c,f]/(m(c),f^2-cf+p).
\]

To check that there are no additional additive relations, evaluate `a(C)+F b(C)` at both distinct roots above every eigenvalue λ. Their difference forces b(λ)=0 and then a(λ)=0. Thus degree<m representatives are unique. The Ω-adjoint fixes C and interchanges F,V. For a fixed element one has `(F−V)b(C)=0`; strictness makes F−V invertible, so b=0. Therefore an alternating twist by a central element of R0 must lie in **Z[C]**, not just in `Q[C]`. A principal twist has f(A) integral and unimodular. Every algebraic integer component of a unit is itself a unit, even with repeated factors. This validates the ring and norm assumptions used in all twelve NO certificates.

For an ordinary pair ±λ, negating a Frobenius root preserves its p-adic valuation and reverses its imaginary sign. Hence every arithmetic CM type requires opposite twist signs on ±λ. This is necessary on ordinary subvarieties of the mixed examples, under the lane's explicitly ordinary-normalized comparison. No supersingular sign rule is used.

### The five obstruction arguments

**PROVED.** Each of the following is a finite congruence obstruction, not a failed bounded search. `review_polarizations.py` independently checks the residues and that the requisite factors divide every orbit to which the lane applies the certificate.

| Required real factors | Necessary condition and contradiction | Orbits |
|---|---|---|
| `(t²−1)(t²−5)` | Opposite unit values at ±1 give zero even-part sum. If f(√5)=a+b√5, then a≡0 mod4. Opposite signs require norm −1, impossible in `a²−5b²≡−1 mod16`. | K4:1; Petersen:6; cube:5 |
| `(t²−1)(t²−4)` | Congruences force f(2)=f(−1), f(−2)=f(1), but f(2)≡f(−2) mod4 forces equality of these ±1 values. | Petersen:1,10; K33:6 |
| `t(t²−5)` | f(0)=±1 and a≡f(0) mod5 make the quadratic norm 1 mod5, whereas the required norm is −1. | Petersen:22; K5:13 |
| `t²−3` | The maximal real order is Z[√3]; a negative-norm unit would give a²−3b²=−1, impossible mod3. | cube:3,23 |
| `(t²−1)(t²−t−8)` or its mirror | The unit congruences below are incompatible. | K5:1,11 |

For the last row θ=(1+√33)/2. Norm −1 is impossible mod3; an odd half-integral unit would satisfy `a²−33b²=±4`, impossible mod8. The continued fraction `√33=[5; overline(1,2,1,10)]` gives the fundamental unit ε=23+4√33=19+8θ. All units are ±ε^k. Normalize f(1)=1 and f(−1)=−1. Evaluation of the quadratic relation forces residues 1 mod8 at θ=1 and −1 mod6 at θ=−1. The pairs for `±ε^k`, depending only on sign and parity of k, are `(7,5),(5,1),(1,1),(3,5)`; none is `(1,5)`. Negative powers obey the same parity table. The mirror follows by t↦−t. For K4 the independent script also enumerates **all 16⁴ residue polynomials** of degree below four, obtaining zero admissible unit/sign candidates.

### K4's repair and the positive cube certificates

**PROVED.** On the actual graph lattice, `A≡J−I mod2`, so `A²≡I mod2` because J²=4J. Thus `U=A+(I−A²)/2` is integral on Z4, and `diag(U,U)` is integral on T. The independent calculation prints

\[
U=\begin{pmatrix}-1&-2&1&1\\-2&-1&1&1\\1&1&-1&0\\1&1&0&-1\end{pmatrix},\quad
U^{-1}=\begin{pmatrix}1&0&1&1\\0&1&1&1\\1&1&1&2\\1&1&2&1\end{pmatrix}.
\]

Both are integral and det U=1. The minimal polynomial of A has degree four, so the unique reduced polynomial `(1+2t−t²)/2` proves U is not in Z[A]. It lies in the lattice-dependent saturated order `Q[A]∩M4(Z)`; “saturated” here must not be replaced silently by “maximal.” The form `B=Ω diag(U,U)` is alternating, compatible and unimodular. For `ι=(F−V)diag(U,U)`, the leading principal minors of Bι are **14,52,56,16,184,1092,1974,441**, proving positivity. The associated sign pattern is positive at 1,√5 and negative at −1,−√5. The independent square classes −7,−3 over Q(√5) allow the required ordinary embedding. Thus the repair exists for a compatible ε, while the small-ring nonexistence holds for every ordinary ε.

**PROVED (cube YES claims).** For masks 1 and 9, det A=1, so C itself is a unit. To establish *arithmetic* positivity, existence of a suitable CM type must still be checked; positivity for an arbitrary archimedean sign choice is insufficient. The lane supplies that check correctly. For mask 9 the two independent modes 1±√2 have discriminants −5±2√2: each is totally negative and their product 17 is nonsquare in Q(√2), so their square classes are independent. For mask 1, the cubic has discriminant 592=16·37, resultant with t²−8 equal to −23, and reduction `(t−10)(t²+9t−7)` mod23. The unique simple common root 10 gives a separate odd valuation for each conjugate discriminant in the real splitting field. The rational discriminant −7 has independent odd valuation at 7; neither prime ramifies in the real field. Consequently the four quadratic sign choices are independent. Ordinariness makes each quadratic extension split locally at the chosen prime above 2, so the Galois sign action supplies primes realizing all these choices. Choose the signs of λ. Howe then gives a principal polarization of `Ω diag(A,A)` for a compatible ε.

Together with the negative a4 below, this proves the separate candidate that **principally polarized graph modules need not even be isogenous to curve Jacobians**. It does not assert that those forms are positive for every ε.

### Hypothesis and ordinariness audit

**PROVED (scope).** The bilinear Howe criterion agrees with the locally available primary exposition `refs/src/1701.07742/main.tex:3474–3497,3556–3590`: compatibility, nondegeneracy, and Φε-positivity are required; unimodularity makes the polarization principal. Multiplicities do not invalidate the ordinary criterion. The squarefree and canonical-lifting/comparison hypotheses in the lane's BKM statement, including the index formula for the isogeny degree, agree with [Bergström–Karemaker–Marseglia, Theorem 4.10](https://arxiv.org/html/2101.05531v3#S4.Thmtheorem10). Its real comparison unit does not prove that Ω has a repair in R0. Every nonordinary example here has repeated Weil factors, so the quoted squarefree theorem does not apply directly. In the mixed cases the NO conclusions are restricted to the central ring and the ordinary-normalized comparison; full nonordinary polarizability remains open in this lane.

The coefficient of x^n in W is prime to p exactly in the ordinary cases. Independent values are:

| Graph | Masks, in order | Middle coefficients | Ordinary masks |
|---|---|---|---|
| K4 | 1 | 5 | 1 |
| Petersen | 1,6,10,22 | 88,200,88,264 | none |
| K33 | 1,6 | 8,24 | none |
| cube | 1,3,5,9,23 | 1,73,89,65,145 | all five |
| K5 | 1,3,11,12,13 | −40,−12,40,12,0 | 1,11 |

These reproduce the entire scope table: **12 NO**, **2 compatible-ε YES**, **3 nonordinary OPEN**. Each of the five graphs has a NO orbit, so the lane's additional per-graph universal refutation is valid. In particular cube:23 is ordinary despite its repeated quartic factor; a “supersingular-looking” spectral symmetry is not an ordinariness test.

## RJ5. J2 and its all-k certificate — VALID

**REFUTED (the original J2); independently reproduced.** `review_arithmetic.py` constructs W from `x^n det((x+p/x)I−A)`, rather than taking powers of the 2n-by-2n step. It computes traces by formal-series division in `−uP'(u)/P(u)`, and closed-point counts recursively from `N_k=Σ_{d|k}d a_d`, with a second Möbius-inversion check. All 17 orbits agree with every saved N_k and a_k through k=31; the independent calculation continues through k=40.

| Counterexample | Independent N values | Closed-point obstruction |
|---|---|---|
| cube:1 or cube:9 | N2=13, N4=9 | a4=(9−13)/4=−1 |
| cube:23 | N1=3, N2=13, N3=9, N6=−23 | a6=(−23−9−13+3)/6=−7 |
| Petersen:1 | N1=3, N5=−7 | a5=(−7−3)/5=−2 |

All these matrices are strictly Ramanujan by exact positive principal minors of `4pI−A²`. Thus these are counterexamples to curve-count positivity, not failures of the Weil property. The cube:1 and cube:9 formal N_k are nonnegative at **every** k, which illustrates why checking N_k alone misses an obstruction.

**PROVED (tail).** For n≤10,p≥2, the verified Weil property gives `|Tr F^d|≤20p^(d/2)`. With h=⌊k/2⌋, bounding the absolute value of every proper-divisor contribution gives

\[
k a_k\ge p^k+1-20p^{k/2}
-\sum_{d=1}^{h}(p^d+1+20p^{d/2})
\ge p^k-(20+11k)p^{k/2}.
\]

At k=32, `2^16=65536>372=20+11·32`; `2^(k/2)/(20+11k)` is increasing thereafter. This proves a_k>0 for k≥32, as well as N_k>0, so the finite absence statements are genuinely all-k certificates. The absolute-value bound remains valid even when some earlier N_d are negative. No unproved RH is assumed: the strict band was checked exactly. Since Tr A=0, N1=p+1, and the Hasse–Weil–Serre bound is automatic for these simple graphs.

**PROVED (the separate cycle-count candidate).** Counting length-four walks gives `Tr A⁴=n(p+1)(2p+1)+8S4`. The root recurrence gives `Tr F⁴=Tr A⁴−4p Tr A²+2np²`. Since `N2=p²+1+n(p−1)`, subtraction yields `a4=(p⁴−p²)/4−2S4`. Petersen has no triangles, so `Tr F⁵=Tr A⁵=10S5` and a5=6−2S5. A fresh enumeration by vertex subsets and permutations verifies every orbit's cycle signs; cube masks 1,9 have S4=2, and Petersen:1 has S5=4. The matching average depends only on the underlying graph, so cannot distinguish these flux obstructions. The invariant is the cycle-sign cohomology class, not a representative's number of negative edges.

## RJ6. No resultant-one partition — VALID

**PROVED.** The proposition `prop:connected-signed-no-resultant-one-partition` has no gap under its stated symmetric, connected signed-adjacency hypotheses. If `h=h1 h2` and `Res(h1,h2)=±1`, integral Bézout coefficients give `e≡1 mod h1`, `e≡0 mod h2`. Consequently h divides e²−e, and Cayley–Hamilton gives an integral symmetric idempotent E=e(A). It is nontrivial because h1 and h2 have disjoint, nonempty spectral supports. Repeated factors cause no problem: resultant one prevents sharing a factor across the partition.

For a real symmetric idempotent, `0≤E_ii≤1`. Since E is integral, E_ii is 0 or 1, and

\[
E_{ii}=(E^2)_{ii}=\sum_j E_{ij}^2
\]

forces every off-diagonal entry to vanish. Thus E selects a nonempty proper coordinate subset. Commutation with A then forces every crossing adjacency entry to vanish, contradicting connectedness of the support graph. The proof applies to any symmetric integer matrix with connected off-diagonal support; regularity, the prime field and the Ramanujan bound are unnecessary.

**NUMERICAL (stress test, not the proof).** With seed 20261025, the independent script generates 20 connected signed graphs on 4–12 vertices, factors each characteristic polynomial over Z, and tests every nontrivial unordered monic factorization, including splits of repeated factors. It finds **15 reducible characteristic polynomials, 88 factorizations, 44 pairs of distinct irreducible factors, 10 pairwise resultants of absolute value one, and 0 resultant-one complete partitions**. The JSON saves every matrix and every resultant. Thus replacing “complete partition” with “pair of irreducible factors” would be false. K4's pairwise absolute resultants remain 2,4,4, and its genuine Jacobian witness agrees with the absence of this obstruction. The arithmetic Serre/Howe–Lauter split-polarization criterion is relevant only when its complete-partition hypothesis holds; here the graph structure rules that out.

For the arithmetic implication, [Howe–Lauter, *New methods for bounding the number of points on curves over finite fields*, Theorem 2.2, Lemma 2.3 and Proposition 2.8](https://arxiv.org/html/1202.6308) give the precise chain: the gluing exponent divides the reduced resultant, resultant one forces exponent one, and a principally polarized product with trivial gluing cannot be a smooth connected Jacobian.

## RJ7. The OPEN / PROVED NO table — VALID in its stated scope

**PROVED (necessary tests); OPEN (the remaining Jacobian realizations).** These are the independent closed-point counts through degree 12, computed from W rather than copied from the lane's count arrays:

| Graph:mask | a1,…,a12 | Consequence |
|---|---|---|
| Petersen:1 | 3,6,2,3,−2,5,18,32,64,83,170,377 | NO |
| Petersen:6 | 3,6,2,3,6,13,18,32,56,103,186,293 | passes; OPEN |
| Petersen:10 | 3,6,2,3,14,5,18,32,48,75,202,377 | passes; OPEN |
| Petersen:22 | 3,6,2,3,6,29,18,0,56,87,186,285 | passes; OPEN |
| K33:1 | 3,4,2,1,6,13,18,30,56,127,186,285 | passes; OPEN |
| K33:6 | 3,4,2,9,6,5,18,18,56,87,186,385 | passes; OPEN |
| cube:1 | 3,5,2,−1,6,9,18,30,56,115,186,367 | NO |
| cube:3 | 3,5,2,7,6,9,18,18,56,115,186,319 | passes; OPEN |
| cube:5 | 3,5,2,7,6,9,18,34,56,51,186,351 | passes; OPEN |
| cube:9 | 3,5,2,−1,6,25,18,30,56,83,186,295 | NO |
| cube:23 | 3,5,2,15,6,−7,18,6,56,147,186,343 | NO |

The passing assertions extend to every k by RJ5, not merely k≤12. Across all five graphs the rerun has 17 strict orbits / 176 switching classes; 13 orbits / 145 switching classes pass every a_k test. Seven undecided *cubic* orbits remain after removing K4's positive class and the four count-obstructed classes. “OPEN” here adjudicates what lane J has established; it is not a claim that no other lane or literature computation can settle them. The current round's K33 full-census lookup is deliberately left to lane J2.

**PROVED (separate hyperelliptic-bound claim).** `Tr A²=n(p+1)` gives `N2=p²+1+n(p−1)`. The unique hyperelliptic map descends to a genus-zero curve over the finite field; that curve has a rational point, hence is P1. Therefore a hyperelliptic curve has `N2≤2(p²+1)`. For K33, cube and Petersen, respectively, N2=11,13,15>10. All their listed classes are impossible hyperelliptically. This argument neither excludes nonhyperelliptic curves nor uses ordinariness. K5 is at equality 20, and K4 is below its bound.

**PROVED (the omitted restricted-search claim).** `review_genus6.py` redoes just the lane's plane-quintic and two trigonal-family searches, not the external genus-six census. It directly evaluates candidate coefficient vectors over fresh finite fields, filtering after each degree; it uses no Walsh transform. It reproduces every prefix count and these final raw matches for K33 masks (1,6):

| Family | Coefficient vectors | Raw matches | Smooth matches |
|---|---:|---|---|
| Plane quintic | 2²¹ | (0,0) | (0,0) |
| Bidegree (3,4) on P1×P1 | 2²⁰ | (72,0) | (0,0) |
| Maroni 2 on F2 | 2²⁰ | (0,0) | (0,0) |

The independent check finds and saves an **F2-rational singular point for every one of the 72** candidates, a stronger explicit certificate than merely a nonunit singularity ideal. The scroll coverage is correct: a genus-six trigonal curve has a unique degree-three pencil (two distinct pencils would force genus≤4), so its pencil descends; its base is P1 over a finite field. On F_e it has class `3S+bF`, genus `2b−3e−2=6`, and nonnegative intersection with S requires `b≥3e`. Thus e is even and e≤2, giving e=0,b=4 or e=2,b=7. Over P1 the vector bundle splits; these are precisely the two searched families. This is still only a restricted negative search, leaving the bielliptic and generic strata untouched. The genus-two / genus-three classifications cited by the lane cannot decide these higher-genus glued products.

### Additional body claim: the gluing indices — VALID

**PROVED, independently reproduced.** `review_gluing.py` uses PARI `matkerint`, rather than the lane's SymPy Smith transformations, to obtain saturated kernels of the rational-isogeny-factor annihilators. It finds:

| Example | Kernel ranks | Index of their sum | Restricted Ω determinants |
|---|---|---:|---|
| K4:1 | 2,2,4 | 16 | 4,4,16 |
| Petersen:22 | 8,12 | 15,625 | 15,625;15,625 |
| K5:13 | 2,8 | 25 | 25;25 |

These validate the lane's specific gluing claim. They are not a comparison with the integral module of any constructed curve. The separate candidate that equality of the graph's **particular polarized lattice** with a constructed Jacobian remains unproved is correctly marked OPEN: neither equal point counts nor these graph-side indices supply a polarization-preserving integral isomorphism. J2′ sufficiency likewise remains OPEN on the evidence of this lane.

## RJ8. Proposed record corrections

No record page has been edited. The following decisions concern the lane's proposed wording, not a retroactive registration of its results.

| Page | Decision | Wording to use |
|---|---|---|
| `no-lift.md` | **AGREE-WITH-CHANGE** | “Lane J constructs a genus-four trigonal Jacobian in the K4 F2-isogeny class and genus-five hyperelliptic Jacobians in all five strict Ramanujan K5 F3-isogeny classes. A supersingular factor does not by itself preclude Jacobian realization. The Centeleghe–Stix anti-equivalence requires choices; its bare module dictionary does not identify the graph form with an arithmetic principal polarization. The full Petersen principal-polarization question remains open in this lane.” Preserve the 5-gluing and the distinction between an ordinary canonical lift and other CM lifts. |
| `howe-positivity.md` | **AGREE-WITH-CHANGE** | “The K4 repair is `U=A+(I−A²)/2∈Q[A]∩M4(Z)`, outside Z[A]; `diag(U,U)` lies outside Z[F,V]. It gives a principal polarization for a compatible ordinary embedding, while no unit in Z[F,V] repairs Ω for any ordinary embedding. The isogeny class contains Lane J's trigonal curve; equality of the particular polarized lattices remains open.” This names the actual lattice order and retains the embedding scope. |
| `curve-bridge.md` §6 | **AGREE** | “The new K4 and K5 curve witnesses identify isogeny classes only; counts still do not determine the integral module or its polarization.” |
| `graph-super.md` | **AGREE** | “Distinguish the signed H¹ polynomial P_s, the full graph ratio P_s/P_0, the formal curve counts `p^k+1−Tr F^k`, the odd-flux walk counts, and the abelian-variety counts `det(I−F^k)` in the strict prime-field case. Positivity of the last two does not imply positivity of formal curve or closed-point counts. Balanced signings retain +d and antibalanced signings retain −d.” |
| `data-ladder.md` §0 | **AGREE-WITH-CHANGE** | “A strict Ramanujan signed flux on a (p+1)-regular graph, with p prime, supplies an abelian-variety module; its isogeny class may or may not contain a curve Jacobian. The chosen categorical equivalence, integral module, principal polarization and Jacobian realization are additional questions.” The prime-field and strictness hypotheses must remain visible. No unconditional principal-polarization implication follows from the module dictionary. |

## Correction ledger and review coverage

**SHARPENED.** No mathematical counterexample to the lane's stated core conclusions was found. The review brief's K4 N2 shortcut is invalid; the lane's actual exhaustive proof survives. The larger-order repair is not a repair in Z[F,V]. The positive curve conclusions are about isogeny classes. Nonordinary central-ring NO statements retain their ordinary-normalized scope, and the cube YES statements retain “for a compatible ε.” A pairwise resultant-one test is insufficient; a complete partition is required. These are the qualifications to carry into any record annotation.

The eleven candidate rows of the original closing table are adjudicated individually below. Additional omitted body claims are also included: the canonical equation census, polarization-criterion scope, higher-genus hyperelliptic bound, restricted genus-six searches, and gluing indices. Dictionary subclaims (trivial modes, zeta conventions, variance and conjugacy) are covered in RJ1; the exhaustive flux counts and all-k tail in RJ5; the five certificate proofs and positive repairs in RJ4. “VALID” on an OPEN-status row means the claimed limitation is justified, not that the missing theorem has been proved.

## Verdict lines

VERDICT jac:dictionary: VALID — the explicit free rank-2n module satisfies the prime-field Centeleghe–Stix hypotheses.
VERDICT jac:j1-refuted: VALID — K4 has no repairing unit in Z[F,V] although its integral saturated-order repair exists.
VERDICT jac:j1-five-graphs: VALID — every listed graph has a certified small-ring NO orbit in the stated normalization.
VERDICT jac:j2-refuted: VALID — the cube and Petersen counterexamples and the all-k certificate reproduce exactly.
VERDICT jac:k4-trigonal: VALID — the smooth genus-four trigonal witness matches and the exhaustive hyperelliptic census has no match.
VERDICT jac:k5-hyperelliptic: VALID — all five orbit witnesses and all five exhaustive equation totals are independently confirmed by PARI.
VERDICT jac:resultant-one: VALID — the integral orthogonal-projector proof rules out every nontrivial complete resultant-one partition.
VERDICT jac:cycle-counts: VALID — the a4 and Petersen a5 identities follow from walk counts and reproduce orbit by orbit.
VERDICT jac:ppav-not-jacobian: VALID — cube masks 1 and 9 have compatible-embedding principal repairs but negative a4.
VERDICT jac:open-table: VALID — every numerical entry is confirmed while the seven remaining cubic realizations are unresolved by lane J.
VERDICT jac:polarized-lattice-open: VALID — the witnesses establish isogeny and do not identify the particular polarized integral lattices.
VERDICT jac:canonical-census: VALID — direct enumeration in a different quotient basis reproduces the complete 24-element smooth matching set.
VERDICT jac:polarization-scope: VALID — the ordinary Howe and squarefree BKM hypotheses are correctly separated.
VERDICT jac:hyperelliptic-bound: VALID — N2 excludes K33, cube and Petersen but does not exclude K4.
VERDICT jac:genus6-restricted: VALID — the three restricted searches reproduce and every final candidate has an explicit rational singular point.
VERDICT jac:gluing: VALID — independent PARI integral kernels reproduce all three indices and restricted determinants.

## Numerical checks for the blind lane

Commands below run from `notes/astra-2026-10-25/review-jacobian/`. PARI scripts automatically invoke the supplied preinstalled interpreter. No installation or network access is needed for the computations.

1. `python3 checks/review_k4.py`: the displayed projective K4 curve has **N1,…,N8 = 3,9,9,29,33,69,129,285**, with no singular point; the printed Bézout identity proves geometric smoothness.
2. `python3 checks/review_k5.py`: PARI returns W(x); reversing gives the following five **L-polynomials P(u)=u¹⁰W(1/u)**, one per explicit witness:

   | K5 mask | P(u) |
   |---|---|
   | 1 | `1+5u²−8u³+9u⁴−40u⁵+27u⁶−72u⁷+135u⁸+243u¹⁰` |
   | 3 | `1+5u²−4u³+17u⁴−12u⁵+51u⁶−36u⁷+135u⁸+243u¹⁰` |
   | 11 | `1+5u²+8u³+9u⁴+40u⁵+27u⁶+72u⁷+135u⁸+243u¹⁰` |
   | 12 | `1+5u²+4u³+17u⁴+12u⁵+51u⁶+36u⁷+135u⁸+243u¹⁰` |
   | 13 | `1+5u²+25u⁴+75u⁶+135u⁸+243u¹⁰` |

3. The same PARI command independently finds **6,42,6,42,24** matching equations from **512** F9 residue polynomials and **10,368** N1/N2 survivors; **10,176** of the latter are smooth.
4. `python3 checks/review_arithmetic.py`: cube masks 1 and 9 have **a4=−1**; cube:23 has **N6=−23,a6=−7**; Petersen:1 has **N5=−7,a5=−2**.
5. The same command gives the resultant tally **20 graphs / 88 complete factorizations / 10 pairwise absolute-resultant-one cases / 0 complete resultant-one partitions** (seed 20261025).
6. `python3 checks/review_hyperelliptic_f2.py`: **49,152 equations / 264 classes / 217 L-polynomials / 0 K4 matches**. `python3 checks/review_canonical.py` gives **24** smooth matching canonical cubic classes.

`python3 checks/review_all.py --rerun` regenerates the seven original checks from exact relocated copies and all eight independent checks, then compares every original saved output byte for byte. The current audit is `checks/output_review_audit.txt`: **13 original output files identical; all 8 independent checks pass**. All 17 orbit records, every saved curve representative and every witness coefficient vector were parsed and compared. Fresh outputs are `checks/output_independent_*.txt`; fuller data are the corresponding `.json.txt` files. Arithmetic uses exact integers, finite fields and rational polynomials; NumPy is used only for bounded integer/Boolean arrays. The review never applies PARI's hyperelliptic routine to the nonhyperelliptic K4 curve.

## What this changes in the notebook

**PROVED / REFUTED results supported for subsequent registration, subject to the remaining second-family review gate:** the prime-field module dictionary; the small-ring J1 refutation with its larger-order K4 repair; the J2 counterexamples; K4's trigonal Jacobian isogeny class and hyperelliptic exclusion; all five K5 hyperelliptic Jacobian classes; the no-resultant-one-partition proposition; the cycle formulas; and the compatible-embedding principally polarized cube counterexamples. The auxiliary censuses and gluing indices also reproduce. This review proposes no new registration and changes no record page.

**OPEN remains OPEN on this evidence:** the seven surviving cubic orbit realizations; the full nonordinary polarization questions; and equality of any particular graph polarized lattice with a constructed curve Jacobian. The K33 census adjudication belongs to lane J2 and was not duplicated here.

Apply the five annotations in RJ8 with their explicit prime-field, strictness, order, embedding and isogeny qualifications. The accurate ladder sentence is that a strict prime-field Ramanujan flux supplies an abelian-variety module whose isogeny class may or may not contain a curve Jacobian. Neither a universal curve interpretation nor a universal non-Jacobian interpretation survives these examples.

The next steps are the independent second-family REFUTE review, reconciliation with lane J2's K33 lookup, and an actual integral-module/polarization comparison for a curve witness. More matching point counts alone will not settle the last problem.

