# Lane J2: the genus-six census and beyond

Author: `codex:gpt-6-astra`, 2026-10-25.
Status: research record, not registered; no independent REFUTE review claimed.
All new files are confined to this lane. The HKL clone is treated as data.

## 1. J2-1: both K₃,₃ classes contain no Jacobian

**PROVED (using the complete Huang–Kedlaya–Lau census).** Neither strict
Ramanujan switching orbit of K₃,₃ is a Jacobian isogeny class over F₂.
In lane J's BFS mask convention the two L-polynomials, written with constant
coefficient 1, are

\[
P_1(T)=1+3T^2+4T^4+8T^6+16T^8+48T^{10}+64T^{12},
\]
\[
P_6(T)=1+3T^2+12T^4+24T^6+48T^8+48T^{10}+64T^{12}.
\]

Thus each is an isogeny class of six-dimensional abelian varieties over F₂
containing **no Jacobian of a smooth geometrically connected curve over F₂**.
This is an isogeny-class exclusion and is stronger than an exclusion for the
particular graph lattice. It does not assert anything over extensions of F₂.

**Certificate and conventions.** `checks/census_lookup.py` computes
`T^6 det(((1+2T²)/T)I−A)` independently from each supplied 6×6 adjacency
matrix. Its coefficient vectors agree with lane J. It decodes every label
in `sources/hkl-genus-6/lmfdbgenus6_curves_F2.txt`, and obtains

| Mask | Target label | N₁,…,N₆ | Census |
|---|---|---|---|
| 1 | `6.2.a_d_a_e_a_i` | 3,11,9,15,33,95 | ABSENT |
| 6 | `6.2.a_d_a_m_a_y` | 3,11,9,47,33,47 | ABSENT |

The file has exactly 38,327 distinct labels and curve multiplicities summing
to 72,227. Independently, the script reads the six stratum files, reconstructs
their L-polynomials by Newton identities from the six recorded counts, and
recovers exactly the same labels and multiplicities. Stratum sizes are
4,134 hyperelliptic; 7,282 trigonal Maroni 0; 6,181 trigonal Maroni 2;
1,530 bielliptic; 4,204 plane quintic; 48,896 generic. Neither six-count tuple
occurs in any stratum. This also detects a missing-line or label-sign mistake
between the assembled file and the six raw lists.

The base-26 code uses ordinary digits a=0,…,z=25, with a leading a indicating
negation (a alone is zero). For example ac=−2, ag=−6, ba=26, aba=−26.
All integers from −10,000 through 10,000 are round-trip checked. The first
eight assembled rows and the first row of every stratum are printed with
their reconstructed counts and source-line references. In particular, the
first assembled label `6.2.ac_e_ag_i_am_m` has counts (1,9,7,17,21,45),
matching hyperelliptic line 853. No curve equation is evaluated as code.

`Census/Shared/weilpolys.sage` stores the **monic Frobenius polynomial**
χ(X)=X¹²+a₁X¹¹+⋯+a₆X⁶+2a₅X⁵+⋯+64. The label records its descending
coefficients, which are the ascending coefficients of P(T)=T¹²χ(1/T).
`Census/Shared/weil_poly_utils.sage`, functions `trace_from_weil_poly`,
`weil_poly_from_point_count` and `label_from_weil_poly`, confirms the reversal.
The independent Newton implementation checks the convention against all
72,227 count lists, not just an example.

**Provenance (cited complete computation).** Yongyuan Huang, Kiran S. Kedlaya
and Jun Bo Lau, *A census of genus 6 curves over F₂*, arXiv:2402.00716 (2024),
with primary data at <https://github.com/junbolau/genus-6>. The supplied local
README states the complete counts and lists the six strata. The local
assembled-file SHA-256 is
`99d4894e8cdd12db26518b4e7016eb877dff3ad4e61a50d487523f1f92acc7f4`.
Hashes of all six raw count files are in `checks/output_census.json.txt`.
This proof invokes the published census's completeness; it does not claim
to rerun the geometric enumeration or independently prove its completeness.
Since neither target occurs, there is no listed target curve to point-count.
Newton extrapolations N₇,…,N₁₂ are printed as **formal target counts**, not
as counts of nonexistent witness equations.

**Complete near-miss list.** Both targets have (N₁,N₂,N₃)=(3,11,9).
Exactly **272** census isogeny classes, comprising **563** curve classes,
share those three counts. Every label, all six counts, curve multiplicity
and stratum multiplicity is recorded in `checks/output_census.txt` and
`checks/output_census.json.txt` (the same complete list for both targets).
Even the first five counts fail to decide the question:

| Target | Near-miss label | N₆ | Curves / strata |
|---|---|---:|---|
| mask 1 | `6.2.a_d_a_e_a_h` | 89 (target 95) | 1 generic |
| mask 6 | `6.2.a_d_a_m_a_u` | 23 (target 47) | 1 plane quintic |
| mask 6 | `6.2.a_d_a_m_a_w` | 35 (target 47) | 2 generic |

These are all near misses sharing N₁,…,N₅.

## 2. J2-2: the lattice question after the exclusion

**PROVED NO for a Jacobian match over F₂.** Since neither isogeny class
contains a Jacobian, no curve can have a Jacobian with the graph's integral
module and principal polarization. The antecedent “if found” is false.
There is no curve endomorphism ring or list of Jacobian principal
polarizations in these classes to compare. The number of Jacobian
polarizations is zero; the number of **all** principal polarizations on
abelian varieties in either class is a different problem, not answered
by census absence.

**SHARPENED (ordinarity correction).** Both K₃,₃ masks have 2-rank 2 and
are nonordinary, not just mask 1. Indeed, both P(T) reduce to 1+T² mod 2.
Mask 1 has χ_A=t²(t²−t−4)(t²+t−4); mask 6 has
χ_A=(t−2)²(t+2)²(t−1)(t+1). Mask 6's ±2 blocks are nonordinary even though
A has no zero eigenvalue. The absence of the x²+2 Frobenius factor is not
ordinarity. Lane J's table correctly calls both nonordinary; the “NO” for
mask 6 in its polarization table concerns units of Z[F,V], not absence of
nonordinary factors or absence of every principal polarization.

The graph orders have the explicit presentations
R₀=Z[c,F]/(m_A(c),F²−cF+2), V=c−F, with m_A the squarefree part of χ_A;
they have ranks 10 and 8 respectively. Their rational centralizers have
dimensions 16 and 20 respectively, so R₀ is not the full endomorphism ring.
The additional integral endomorphisms are the integral matrices commuting
with F (opposite ring if using the contravariant equivalence). Principal
polarization enumeration would require a fixed Centeleghe–Stix equivalence,
its transported duality, and its nonordinary positivity comparison, followed
by enumeration of positive unimodular compatible forms modulo module
automorphisms. The ordinary Howe criterion alone does not perform that step.
The symmetric positive Weil form ½Ω(F−V) is not itself an alternating
principal polarization and does not supply the missing comparison.

For any future positive isogeny-class example, equality of every integral
ℓ-adic Tate module for ℓ≠2, and the appropriate 2-divisible/Dieudonné data,
with pairings establishes local equivalence, not automatically a global
integral-module isomorphism. A global F-intertwiner U∈GL₂g(Z), with
UᵀB_JU=B_graph under the fixed functor, would settle the stronger question.

**PROVED (principal polarizability of the isogeny classes).** Both K₃,₃
classes contain principally polarized abelian varieties, despite containing
no Jacobian. For mask 6 every simple factor is elliptic. For mask 1 take
the product E₀²×Jac(D₊)×Jac(D₋), where E₀: y²+y=x³ and

\[
D_+: y^2+xy=1+x^2+x^5,\qquad D_-: y^2+xy=1+x^5.
\]

Their Frobenius polynomials are respectively X²+2,
X⁴−X³−2X+4, and X⁴+X³+2X+4. `checks/lowgenus.py` verifies smoothness and
counts of D₊ and D₋ through degree 4. The product polarization proves
existence in the isogeny class; it does not identify the graph's integral
module with that product or enumerate its principal polarizations.

## 3. J2-3: cube masks 3 and 5

**OPEN (both Jacobian-isogeny verdicts).** Neither a witness nor a global
non-Jacobian obstruction has been established. The following are exact
family exclusions and arithmetic restrictions, not a census of genus 8.
The two target polynomials are

\[
P_3(T)=(1+T^2+4T^4)^2
(1-2T+3T^2-4T^3+4T^4)(1+2T+3T^2+4T^3+4T^4),
\]
\[
P_5(T)=(1+2T^2+5T^4+8T^6+16T^8)^2.
\]

Both have N₁,…,N₇=(3,13,9,41,33,73,129); N₈ is 185 and 313,
respectively. Both have 2-rank 8.

### 3.1 Exhaustive trigonal exclusion

**PROVED (finite enumeration).** Neither cube target has a trigonal
representative over F₂. On the Hirzebruch surface F_e, write S²=−e,
S·F=1. A trigonal curve in class 3S+bF has
g=2b−3e−2. Its coefficient model is
Σ_{j=0}³ f_j(x)y^j=0, deg f_j≤b−ej, with both base and fiber infinities
included. For genus 8 the possibilities are (e,b)=(0,5),(2,8): parity
requires even e, and nonnegative intersection with S gives b≥3e.
The trigonal pencil is unique in genus ≥5 and descends over F₂; its
genus-zero base is P¹. The associated ruled surface is a split Hirzebruch
surface, since vector bundles on P¹ split and Br(P¹/F₂)=0. Thus these two
models cover the trigonal cases, including nonmonic equations.

`checks/genus8_search.py` searches all 2²⁴=16,777,216 binary coefficient
vectors in **each** family. Counts are accumulated over closed Frobenius
orbits of the projective bundle, using exact binary field arithmetic.
Both cube targets have identical N₁,…,N₇, so the two searches have the
same survivors through these filters:

| Family | After N₁ | N₂ | N₃ | N₄ | N₅ | N₆ |
|---|---:|---:|---:|---:|---:|---:|
| F₀, b=5 | 2,752,512 | 68,880 | 19,074 | 504 | 216 | 0 |
| F₂, b=8 | 2,752,512 | 76,224 | 20,901 | 504 | 192 | 0 |

No smoothness assumption was used to eliminate these equations. In
particular, monic pure cubic covers y³=f(x) are excluded. A separate run
of the same engine in genus 6 reproduces lane J's 72 raw Maroni-0 matches
for K₃,₃ mask 1, all singular, and zero other trigonal matches. The original
lane-J scripts are also rerun in an isolated directory with byte-identical
saved transcripts (`checks/output_prior_rerun.txt`).

### 3.2 Plane curves with two nodes

**PROVED (finite family exclusion).** Neither target is the normalization
of a plane sextic having exactly two ordinary geometric nodes and no other
singularities. This is a tetragonal construction family (projection from
a node). Its arithmetic genus is 10 and its normalization genus is 8.

The nodes are either two F₂-points or one degree-2 closed point. PGL₃(F₂)
is transitive on each configuration type. Fix (1:0:0),(0:1:0), or
(1:α:0),(1:α²:0) with α²+α+1=0. Fix all tangent quadratic coefficients,
requiring a nonzero cross coefficient. Each case leaves 16 free binary
coefficients. There are 16 rational-node cases and 48 conjugate-node
cases, hence **4,194,304** equations tested per target. The normalization
correction is included: a split rational node adds one degree-1 point;
a nonsplit rational node removes one degree-1 point and adds one degree-2
point. A degree-2 node gives the analogous corrections in degrees 2 and 4.

`checks/plane_nodes.py` has total successive survivors
(942080,70930,19440,452,108,24,0,0) through N₁,…,N₈, for either target.
All fail by N₇; no assertion about the singularities of a surviving
equation is needed. Cusps, other singularities, and higher-degree plane
models remain outside this search.

**PROVED (another tetragonal family exclusion).** `checks/ruled_nodes.py`
also searches the one-node genus-9 models in classes 4S+4F on F₀ and
4S+8F on F₂. These correspond to the split smooth-quadric and cone
versions of a (2,4) complete intersection, with one ordinary node, whose
normalization would have genus 8. Fix the rational node at (x,y)=(0,0).
For each of its four tangent quadratics with cross coefficient 1, the
other 19 coefficients vary freely: 2,097,152 equations in each surface
family per target. The normalization correction is applied before the
count filters. Neither target survives N₆. This is not a search on the
nonsplit smooth quadric or over arbitrary singularity types.

### 3.3 Arithmetic obstructions and double covers

**PROVED (necessary tests; all-k positivity).** `checks/obstructions.py`
independently computes every prior orbit's counts through k=31 using
R₀=2I, R₁=A, R_k=AR_{k−1}−2R_{k−2}. These agree with the old 2n×2n
matrix-power output. Positive leading principal minors of 8I−A² certify
the strict real Weil band. Every surviving target passes integrality and
nonnegativity of closed-point counts, N_{dk}≥N_k, and the Weil and
Hasse–Weil–Serre bounds. The tail estimate from lane J gives
k a_k ≥2^k−(20+11k)2^{k/2}>0 for k≥32. Therefore the positivity statement
is for all k, not just the searched range.

The resultant-one obstruction is unavailable by lane J/RJ's integral
projector theorem. All distinct-factor partitions are also tested with
the **reduced** resultant (denominator of the exact rational Bezout
identity, with certificate printed in the JSON). Their minimum values
are 8 for cube mask 3 and 4 for mask 5. There is no resultant-two
double-cover implication. This does not bound the gluing exponent sharply
enough to decide the Schottky question.

Both isogeny classes are principally polarizable. Cube mask 5 is the
square of the K₄ class; for mask 3 every irreducible factor has an explicit
genus-2 Jacobian representative in `output_lowgenus.txt`. Thus no
principal-polarizability-of-the-isogeny-class criterion can exclude them.
Howe's criterion on a specified ordinary integral module remains a
different problem. Lane J's central-order unit NO certificates are not
obstructions to the existence of a Jacobian somewhere in these classes.

For a separable degree-2 map C→D over F₂, P_D divides P_C,
N_k(C)≤2N_k(D), and, writing f for 2-rank,

\[
r=f_C-2f_D+1,\qquad
\delta=g_C-2g_D+1=\sum_{P\ {ramified}}(m_P+1)/2,
\]

where the sum is over geometric ramification points and the reduced
Artin–Schreier pole orders m_P are odd and positive. Thus 0≤r≤δ, and
r=0 forces δ=0. The script enumerates every polynomial divisor of base
genus 1, 2 or 3, applies these restrictions and the degree-2 point bound
through k=31, and excludes non-Jacobian genus-2 polynomials using a complete
enumeration of all 768 smooth hyperelliptic equations (20 polynomials).
The point bound is automatic beyond this range by Weil's bound.

* Cube mask 5 has **no degree-2 quotient of genus 1, 2 or 3**.
* Cube mask 3 has none of genus 1 or 3; the only possible genus-2 quotient
  polynomial is 1+T²+4T⁴, represented by
  D: y²+(x²+x+1)y=x⁵+1. Its counts begin (3,7,9,31,33,43).
  Such a double cover must have five simple geometric branch points.
  Since N₂(C)=13 and N₂(D)=7, exactly one branch point lies over F₄;
  hence the branch divisor is one rational point plus one degree-4 point.

**PROVED (finite double-cover exclusion).** On the displayed genus-2
base, `checks/double_covers.py` enumerates all 512 functions in L(2D₀)
for each of the 18 divisors D₀=P+Q just described. It tests the pole
residues to require exactly those five simple branch points, then counts
the normalized covers z²+z=f. None of the **9,216** raw functions matches
the cube mask-3 target. Counts from the linear trace filters are checked
against direct enumeration of z for every tested function at each stage.
The file records the denominator, basis construction, local regularization
rules and every staged survivor count. `lowgenus.py` additionally verifies
that all 48 genus-2 equations with polynomial 1+T²+4T⁴ lie in the single
PGL₂(F₂)/y-shift orbit of the displayed base.

Here the function family is complete for the specified covers. Locally,
a degree-2 cover with conductor ≤2D₀ has an Artin–Schreier representative
with pole order ≤2 at D₀ and no other poles. The changes between such
local representatives are h²+h with h a local section of O(D₀).
Since deg D₀=5>2g(D)−2=2, H¹(D,O(D₀))=0. The changes can therefore be
absorbed globally, leaving f∈H⁰(D,O(2D₀)). This is the elementary
Čech/Artin–Schreier version of the Riemann–Roch completeness argument.
The script constructs this 9-dimensional space explicitly: for P=∞,
f=(a+by)/q² with deg a≤9, deg b≤6; for finite P, denominator
q²(x+1)² and deg a≤10, deg b≤7. Vanishing to order two at the unwanted
conjugate points imposes eight, respectively ten, independent binary
conditions. The resulting bases each have dimension nine. The local
ramification test at a finite denominator root is c₋₁+√c₋₂≠0; at ∞
it is the coefficient b₆≠0 (use the uniformizer x²/y).

Consequently **neither cube target admits a degree-2 quotient of genus
0, 1, 2 or 3**. This is still a family exclusion, not a non-Jacobian
theorem: degree-2 quotients of genus 4 and curves with no involution are
not excluded. It also excludes degree-4 V₄-Galois covers of P¹: their
three quadratic quotients have genera summing to 8, so at least one has
genus ≤2, contradicting the degree-2 quotient exclusion.

**PROVED (other named families).** Hyperelliptic representatives are
excluded by N₂=13>2·5. An F₂-rational automorphism of tame prime order ℓ
fixing an F₂-point acts on its tangent line by an element of F₂×; that
element would have order ℓ, a contradiction. Hence an F₂-Galois cyclic
cover of degree 5 or 7 is impossible since N₁=3 is not divisible by 5 or 7.
For a pure Kummer equation y^ℓ=f(x), ℓ=5 or 7, even without a rational
Galois action, gcd(ℓ,4−1)=1 gives exactly one F₄-point over each point of
P¹(F₄), including ramified and unramified zero/pole fibers on the
normalization. Thus N₂=5, again impossible. Degree 3 has already been
excluded by the exhaustive trigonal search. Smooth complete intersections
(2,4) in P³ and (2,2,2) in P⁴ have genera 9 and 5, respectively, and do
not supply genus-8 witnesses; singular models require normalization.

**Scope of polynomial inequalities.** The elementary deficit/excess
constraints derived from N_{dk}≥N_k and nonnegative closed-point counts,
and positivity of the real Weil polynomial/moment form, all pass. This
is not a claim to have implemented every obstruction in the entire
Howe–Lauter literature. The local HKL implementation of their
resultant-one/two test (`weil_poly_utils.sage:106–183`) is covered exactly
by the Bezout computation; the remaining higher gluing and indecomposable
polarization questions are open. No unspecified “positivity test” is
declared sufficient.

## 4. J2-4: Petersen mask 22 is a Jacobian class

**PROVED YES (constructive), mask 22.** Let C be the smooth projective
model of

\[
\boxed{y^3=x^{12}+x^9+x^6+x^3+1.}
\]

The polynomial f on the right is squarefree: f′=x⁸+x² and
gcd(f,f′)=1. Thus y³=f(x) is smooth at all finite points, and f is not
a cube over the algebraic closure, so the curve is geometrically
integral. At infinity set t=1/x and w=y/x⁴; then
w³=1+t³+t⁶+t⁹+t¹². At t=0, w³=1 has nonzero derivative w², giving
three geometric points and no ramification. The tame degree-3 map to P¹
has twelve simple branch points, each with ramification index 3.
Riemann–Hurwitz gives 2g−2=−6+12·2=18, hence **g=10**.

`checks/verify_petersen.py` counts every finite x and every possible cube
y³ in its own finite-field implementation, using a histogram, and adds
the roots of w³=1 at infinity. This is independent of the search's binary
linear constraints and closed-point-orbit counting. The counts are

| k | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| N_k | 3 | 15 | 9 | 27 | 33 | 195 | 129 | 27 | 513 | 915 | 2049 | 3627 |

The first ten counts and the functional equation give

\[
P_C(T)=(1+2T^2)^4(1-T^2+4T^4)^3,
\]

exactly the Petersen mask-22 polynomial. Counts 11 and 12 are independent
checks against that reconstructed polynomial. The 2-rank is **6**,
since P_C(T) mod 2 = (1+T²)³ has degree 6. This is a nonordinary cubic
graph flux with a Jacobian in its isogeny class. The graph's particular
nonordinary integral module/polarization is not identified with Jac(C).

**PROVED (exhaustive trigonal comparison).** In genus 10 the Hirzebruch
possibilities are (e,b)=(0,6),(2,9),(4,12), with 28 binary coefficients
each. `genus8_search.py --graph Petersen` searches all 2²⁸ equations in
each family for each target. Masks 6 and 10 have no trigonal matches.
Mask 22 has 32 smooth equation matches on F₄, b=12, and none on F₀,F₂.
These 32 are equation vectors, **not** a count of curve isomorphism classes;
many are related by y-translations. The displayed witness is the first.

**OPEN, masks 6 and 10.** Both pass the all-k closed-point test and all
elementary polynomial inequalities in §3.3. Their minimum reduced
resultants are 16, so neither the resultant-one nor resultant-two test
decides them. Both isogeny classes contain products of explicitly
principally polarized lower-genus factors. In particular mask 10's
degree-6 factor is the genus-3 Jacobian of
y²+(x²+x)y=1+x⁷, with counts (3,3,15,7,43,87), verified independently.
The double-cover restrictions leave these possible base polynomials:

| Target | Base genus | Monic Frobenius polynomial |
|---|---:|---|
| Petersen 6 | 1 | X²−X+2 |
| Petersen 6 | 3 | X⁶+X⁵+2X⁴+4X³+4X²+4X+8 |
| Petersen 10 | 2 | X⁴−X³+2X²−2X+4 |

All other genus-1/2/3 polynomial divisors are excluded by the tests stated
in §3.3. A surviving base polynomial does not assert a degree-2 map or
even, in genus 3, a base curve. Petersen 22 has no degree-2 quotient of
genus 1–3 by the same tests; its degree-3 witness shows that this is a
family restriction, not a Jacobian obstruction.

**PROVED (smooth plane-sextic exclusion for masks 6 and 10).**
`checks/plane_smooth.py` tests all 2²⁸ homogeneous sextic equations in P²
over F₂. For mask 6 the staged survivors through N₁,…,N₈ are
(73400320,62720,14840,4704,1428,336,168,0); for mask 10 they are
(73400320,62720,14840,4704,0). Thus neither open class has a smooth
plane-sextic representative (genus 10). No raw full-count match reaches
the smoothness test. Higher-gonality models and the surviving double-cover
directions remain possible.

## 5. J2-5: the conjecture after these examples

**REFUTED, J2′ and the all-cycle-positivity version of J2″.** A precise
candidate condition on A is

\[
\mathcal C(A):\quad
\frac1k\sum_{d\mid k}\mu(k/d)
\left(2^d+1-\operatorname{tr}R_d(A)\right)\ge0
\quad\text{for every }k\ge1,
\]

where R₀=2, R₁=t, R_d=tR_{d−1}−2R_{d−2}. This expresses nonnegative
formal closed-point counts directly in terms of signed closed walks.
It is necessary, but the proposed equivalence
“P_A is a Jacobian polynomial iff C(A)” is **false** for either K₃,₃
mask. They satisfy C(A) for all k and are excluded by the complete census.
No additional finite cutoff in the same positivity test fixes this.

### 5.1 An additional genus-six control: the triangular prism

**PROVED (constructive and census-checked).** To test whether the failure
could be explained just by genus or 2-rank, `checks/prism.py` enumerates
the strict Ramanujan fluxes of the triangular prism (C₃×K₂). Its printed
BFS convention has four orbits, masks 1,2,5,6, of sizes 6,3,3,2. All have
2-rank 2. The census verdicts are NO,NO,NO,YES, respectively. Mask 2
already has a₃=−2; masks 1 and 5 pass all closed-point tests and give two
more count-positive non-Jacobian classes.

For mask 6 the real Weil polynomial is (t²−5)(t²−2)² and

\[
P(T)=1+3T^2+12T^4+20T^6+48T^8+48T^{10}+64T^{12}.
\]

Its label is `6.2.a_d_a_m_a_u`, the plane-quintic near miss of K₃,₃ mask 6.
An affine equation is

\[
x^5+x^4y+y^5+y^4+x^2y+xy^2+x^2+y^2+y=0.
\]

Homogenize to degree 5. Unit Groebner ideals on all three projective
charts prove geometric smoothness; adjunction gives genus 6. The script
independently enumerates projective points over F₂ through F₄₀₉₆ and gets

(3,11,9,47,33,23,129,287,513,1031,2049,3599).

The first six counts determine P; the next six verify it. Finite-field
log/exp tables are exact integer lookup tables, not numerical logarithms.
The contrast with K₃,₃ mask 6 is especially sharp: the same genus, the
same 2-rank, and the same first **five** counts, but opposite Jacobian
verdicts. The counts differ first at N₆=23 versus 47.

### 5.2 Which proposed conditions survive?

| Condition proposed as the dividing line | Verdict and certificate |
|---|---|
| Ordinarity is necessary | **REFUTED:** Petersen 22 (rank 6, genus 10) and prism 6 (rank 2, genus 6) are explicit Jacobian classes. |
| Ordinarity is sufficient | **REFUTED:** ordinary cube masks 1,9,23 fail closed-point positivity. |
| A predicate depending only on genus and 2-rank | **REFUTED:** prism 6 and both K₃,₃ masks have (g,f)=(6,2), with opposite verdicts; even the prism alone has both outcomes. |
| Nonnegative signed-cycle/closed-point counts | **REFUTED:** both K₃,₃ masks and prism masks 1,5. |
| A condition using only N₁,…,N₅, or equivalently the first five signed-walk traces | **REFUTED:** prism 6 versus K₃,₃ mask 6. |
| Principal polarizability somewhere in the isogeny class | **REFUTED as sufficient:** the products in §2 give both K₃,₃ classes principal polarizations. |
| Existence of a rational theta divisor in that weak PPAV sense | **REFUTED as sufficient:** the product theta divisors on those products are defined over F₂ but reducible. |
| An unspecified rational “theta vector” on the graph lattice | **OPEN / not yet a mathematical condition:** its transformation law, positivity, and realization as a theta divisor must be specified. A formal vector or positive Weil form is insufficient. |
| A supersingular factor prevents a Jacobian | **REFUTED:** the explicit Petersen and prism witnesses (also lane J's K₅ examples). |

For a fixed underlying graph, signing does not even change P(T) mod 2,
since A_s mod 2 is the unsigned adjacency. Thus ordinarity and 2-rank
cannot distinguish signings of that graph. The prism examples prove this
failure within a single cubic graph, with all-k-positive orbits on both
sides.

**OPEN (a narrower surviving conjecture, J2″-ordinary).** For an
**ordinary** strict Ramanujan Z₂ flux on a connected simple cubic graph,
P_A is a Jacobian polynomial iff C(A). Necessity is proved; sufficiency
is not. All decided ordinary cases in this dataset agree: K₄ is YES and
cube masks 1,9,23 are NO. The first unresolved tests are precisely cube
masks 3 and 5. This is a restricted conjecture, not a repaired theorem
for all cubic graphs. A full iff criterion must retain more information
than 2-rank, elementary count positivity, or the existence of some
principal polarization; indecomposability and the Schottky condition
remain distinct requirements.
Moreover, the isogeny-class property depends only on χ_A, so any proposed
graph criterion must be invariant under integral signed matrices having
the same characteristic polynomial. A condition on the particular graph
lattice's unit group or pairing does not automatically have this property.

**Updated requested table.**

| Graph | Masks | Jacobian-isogeny verdict over the stated prime field |
|---|---|---|
| K₄ / F₂ | 1 | YES, lane J's trigonal witness |
| K₃,₃ / F₂ | 1,6 | NO, complete genus-6 census (§1) |
| cube / F₂ | 1,9,23 | NO, negative closed-point counts |
| cube / F₂ | 3,5 | OPEN; the construction families above excluded |
| Petersen / F₂ | 1 | NO, negative a₅ |
| Petersen / F₂ | 22 | YES, y³=x¹²+x⁹+x⁶+x³+1 (§4) |
| Petersen / F₂ | 6,10 | OPEN; no trigonal or smooth plane-sextic representative |
| K₅ / F₃ | 1,3,11,12,13 | YES, lane J's five hyperelliptic witnesses |

Four of lane J's seven formerly open count-positive cubic classes remain
open. The extra prism test is fully decided by the genus-6 census, with
an independent equation verification for its positive orbit.

## Correction ledger

| Prior item | Correction / resolution |
|---|---|
| Lane J §3.4: K₃,₃ masks 1,6 OPEN | **Resolved NO** by the complete census. The earlier scoped statement was correct; it is now superseded. |
| Lane J §3.4: Petersen 22 OPEN | **Resolved YES** by the explicit genus-10 trigonal witness. The graph lattice's polarization question remains separate and open. |
| Lane J J2′: all a_k≥0 might characterize cubic Jacobian classes | **REFUTED:** both K₃,₃ masks; additionally prism masks 1,5. |
| Brief's “nonordinary-free” wording for K₃,₃ mask 6 | **Corrected:** both masks have 2-rank 2 and are nonordinary. No zero adjacency eigenvalue is not an ordinarity test. The small-ring repair obstruction for mask 6 is a different fact. |
| Label polynomial versus L-polynomial | HKL stores χ(X) monic; its descending coefficients are the ascending coefficients of P(T). All 72,227 raw count lists validate the convention. |
| Matching first three, or even five, counts settles a genus-6 class | **REFUTED:** 272 near-miss labels at three counts; prism 6 and K₃,₃ mask 6 agree through five counts but have opposite verdicts. Six counts are required in general. |
| Nonordinary blocks or low 2-rank exclude Jacobians | **REFUTED:** Petersen 22 and prism 6. The original lane J already had nonordinary K₅ witnesses; now this is established for cubic graphs over F₂ as well. |
| Small-order unit NO implies no principal polarization or no Jacobian in the class | **REFUTED:** all seven target isogeny classes have explicit principally polarized products; Petersen 22 is a Jacobian class despite its small-order obstruction. |
| A (2,4) complete intersection cannot help at genus 8 | True for a **smooth** intersection (genus 9); one-node normalizations have genus 8 and were separately searched in two quadric families. |
| Positivity means monotonic N_k in k | Only divisibility gives N_k≤N_{dk}. The verified Petersen witness has N₆=195>N₈=27, which is entirely compatible with a curve. |
| The graph's positive Weil form is a curve's principal polarization | These are different forms and different questions; census absence already excludes a Jacobian for either K₃,₃ lattice, while positive examples identify only isogeny classes. |

No prior lane directory, record page, claim registry, or source-data file
was edited. No network access or Git command was used. The new theorem
using the census explicitly depends on its published completeness; the
constructive Petersen and prism theorems have independent point counts
and smoothness/genus certificates.

## Numerical checks for the blind lane

Run from `notes/astra-2026-10-25/census/`. Requirements are Python 3,
SymPy, NumPy, NetworkX, python-flint (for the copied prior checks), and
g++ for the finite binary equation searches. No Sage/Magma, PARI or network
is needed. The `.cpp` files are source companions, compiled inside
`checks/` by their Python entry points. Every mathematical operation is
integer, rational, polynomial, or finite-field arithmetic; there are no
floating spectral tests or probabilistic curve smoothness tests.

1. `python3 checks/census_lookup.py`: **38,327** labels and **72,227** raw
   curve records agree exactly; both target labels are ABSENT; the common
   near-miss list has **272** labels and **563** curves.
2. `python3 checks/verify_petersen.py`: the witness has **N₆=195,
   N₈=27, N₁₂=3627**, genus **10**, and 2-rank **6**.
3. `python3 checks/genus8_search.py`: the two genus-8 families have
   **216** and **192** survivors after N₅, and **0** after N₆, for both
   masks. `--graph Petersen` finds **32** smooth equation vectors for
   mask 22 and none for masks 6,10.
4. `python3 checks/plane_nodes.py`: **4,194,304** two-node sextics per
   target, **24** survivors after N₆ and **0** after N₇.
5. `python3 checks/lowgenus.py` and `python3 checks/double_covers.py`:
   **48** equations in the one genus-2 base isomorphism class; **18×512
   =9,216** Artin–Schreier functions, **0** matches.
6. `python3 checks/prism.py`: prism mask 6 has **N₆=23** and **2-rank 2**;
   K₃,₃ mask 6 has **N₆=47** and the same rank, despite their identical
   first five counts. The plane-quintic witness is checked through k=12.

`python3 checks/run_all.py` reruns all thirteen jobs and checks the
expected verdicts. It completed successfully. `checks/output_audit.txt`
records PASS for every job; `checks/output_manifest.json.txt` gives
SHA-256 hashes of **40** source/output files. `rerun_prior.py` reruns
`jac_fluxes.py`, `jac_trigonal.py`, `jac_genus6.py`, and `jac_verify.py`
from copies under this lane: all four saved transcripts match byte for
byte. The old source directory is read-only throughout.

## What this changes in the notebook

Proposed rows only; nothing is registered, and the results still need the
record's independent REFUTE review (including the computational family
completeness arguments). The census citation is an explicit dependency
of the negative genus-6 classifications.

| Candidate row | Status | Evidence / dependencies |
|---|---|---|
| `cit:huang-kedlaya-lau-genus6` | CITATION | Huang–Kedlaya–Lau, arXiv:2402.00716; supplied primary clone, six strata and checksum manifest (§1). |
| `thm:k33-flux-not-jacobian` | PROVED using cited complete census | Both exact degree-12 polynomials in §1; two independent label/count lookups. |
| `thm:closed-point-positive-flux-not-jacobian` | PROVED / J2′ REFUTED | K₃,₃ masks 1,6 have all a_k≥0 but no genus-6 Jacobian. |
| `thm:petersen22-flux-jacobian` | PROVED, constructive | y³=x¹²+x⁹+x⁶+x³+1; smoothness, genus 10, point counts through k=12 (§4). |
| `thm:prism6-flux-jacobian` | PROVED, constructive | Smooth plane quintic in §5.1, exact counts through k=12. |
| `thm:flux-jacobian-not-determined-by-rank` | PROVED | Same genus, 2-rank and first five counts, opposite verdicts: prism 6 versus K₃,₃ 6. |
| `thm:cube-flux-no-trigonal` | PROVED, finite exhaustive computation | Both Maroni families; every binary equation, no raw count match (§3.1). |
| `thm:cube-flux-no-low-genus-double-cover` | PROVED, finite computation plus RR/AS completeness | Both masks have no degree-2 quotient of genus ≤3 (§3.3). |
| `prop:flux-family-search-exclusions` | PROVED with stated family scope | Two-node plane sextics, one-node ruled curves, and Petersen smooth plane sextics; these do not classify all curves. |
| `conj:ordinary-positive-cubic-flux-jacobian` | OPEN | J2″-ordinary in §5.2; cube masks 3,5 are the first unresolved tests here. |
| `open:cubic-flux-four-classes` | OPEN | cube 3,5 and Petersen 6,10. |

**Candidate annotations, not applied.**

* `no-lift.md`: “The dodecahedral Petersen class (lane J's BFS mask 22)
  is isogenous over F₂ to the genus-10 Jacobian
  y³=x¹²+x⁹+x⁶+x³+1. Its supersingular factor does not prevent a
  Jacobian. The specific glued graph module and principal polarization
  have not been identified with this Jacobian.”
* `data-ladder.md` §0: “A strict prime-field Ramanujan graph flux supplies
  an abelian-variety module. Even nonnegative formal closed-point counts
  do not ensure a Jacobian class: both K₃,₃ classes are excluded by the
  complete genus-6 census. Conversely the nonordinary Petersen mask 22
  and triangular-prism mask 6 have explicit Jacobian representatives.
  Isogeny class, integral module, polarization and Jacobian realization
  remain separate levels.”
* Lane J §3.4: replace K₃,₃'s OPEN row by NO with the census citation,
  split Petersen's row into mask 22 YES and masks 6,10 OPEN, and replace
  the J2′ OPEN sentence by REFUTED. Preserve its distinction between
  class-level and lattice-level claims.

**Next steps.** For the cube, test degree-2 covers of genus-4 curves,
tetragonal models beyond the enumerated singular quadric/plane families,
and indecomposable principal polarizations in the ordinary isogeny
classes. For Petersen 6 and 10, the three residual base-polynomial rows
in §4 give precise double-cover directions; no trigonal or smooth
plane-sextic search remains to be repeated. For the lattice problem,
compute the explicit Petersen/prism Jacobian modules under a fixed
nonordinary duality comparison before claiming equality with graph Ω.

