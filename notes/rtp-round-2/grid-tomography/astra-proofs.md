# Lane G: grid tomography

Author: `codex:gpt-6-astra`.

Incremental record. No RH or zero ordinates enter a computation. The binding
round-2 brief, lane L's L1–L3 and current L4/L5, round-1 B2 §§2,4, the commutant
driver, shard 08i and metric-as-state §§2,3,7 were read. Lane L's progress marks
L1–L3,L5,L6 DONE and L4 PARTIAL. We take its atom convention, recession-cone
identity, distinction between LP outer boxes and axis sections, and conditional
coercivity obstruction; no unfinished L4 numerical claim is assumed.

## Correction ledger

1. The point `y=L` is invisible, not an atom of weight zero. On `[0,L]` its
   arbitrary nonnegative mass defeats boundedness and uniqueness. The requested
   grids are interior, where this defect is absent.
2. Positivity depends **only on** the `2N+1` moments; it does not determine
   their values. In particular this is not an equality-constrained moment problem.
3. The atom quadratic form is a signed autocorrelation, not a nonnegative
   trigonometric polynomial. G3's proposed implication is false.
4. Extremality in a moment fiber is necessary for uniqueness, not sufficient.
   Conversely finitely many exact moments can uniquely determine a sparse
   measure. The actual prime measure has a direct uniqueness certificate at
   the cutoffs in this brief, after deleting the invisible endpoint.
5. `L/(2N)` is a sampling scale, not an exact impossibility threshold for sparse
   recovery. Grid approximation error and matrix positivity tolerance must both
   be specified; a grid missing the atoms need not have any feasible measure.
6. All eleven prescribed uniform grids are in fact infeasible. Their requested
   optimization tables are undefined, not zero-width boxes or diffuse fits.
7. At x=25 the union must deduplicate `log 5=L/2`. Separate variables at an
   identical position would manufacture a spurious weight ambiguity.

## G1. What the window sees — PROVED / SHARPENED

**H-INT:** the finite grid has distinct points `0<y_j<L`.
**H-SIGN:** `w_j>=0`; in the continuum, the unknown measure is nonnegative.
**H-FIN:** the prime-side true finite-section matrix is PSD, whenever its
membership is invoked. This is a finite hypothesis, not RH.

Write `t=y/L`. The atom data, with the brief's sign, are

`A_n(t)=-2(1-t)cos(2πnt) (0<=n<=N)`,
`B_n(t)=sin(2πnt)/π (1<=n<=N)`.

Let `φ=(A_0,...,A_N,B_1,...,B_N)`, `Mμ=∫φ dμ`, and let `K` be the Loewner
assembly map. Its diagonal recovers every `a_n`; row zero recovers
`b_n=n H_{n0}`. Thus `K` is injective and

`H(μ)=H0+K(Mμ)`, and `H(μ)=H(ν) iff Mμ=Mν`.

These are exactly the observable linear data, not moments of every harmonic
through `2N`. Their span has dimension `2N+1`: a relation is
`(1-t)C(t)+S(t)=0`, where `C` is a cosine polynomial and `S` a sine polynomial.
Reflecting `t` to `1-t` gives `t C(t)-S(t)=0`; hence `C=S=0`.

The grid set is a closed convex spectrahedron (include diagonal `diag(w)` in
the LMI). Its cheapest mass bound is already the constant test:

`2 Σ_j (1-t_j)w_j <= H0_00 = C`.

Under H-SIGN and H-INT this proves compactness, even at `N=0`, with
`Σw_j <= C/[2 min_j(1-t_j)]` when nonempty. If `C<0` the set is empty.
For a continuum of points approaching `L`, only the weighted mass is bounded;
compactness of ordinary total mass does not follow. At `L`, `φ(L)=0`.
Indeed, if one strictly positive finite-section measure is feasible, arbitrarily
large extra mass can be put sufficiently close to L: `T(y)->0` in operator norm,
so choose its distance to L small enough that this bounded perturbation lies
below the spectral margin. A continuum formulation needs an edge exclusion
or a weighted-mass topology even after deleting the endpoint itself.

Without H-SIGN, for a nonempty set the recession cone is exactly
`{d:K(Md)>=0}` (lane L1), and its lineality space is exactly `ker M`.
Thus every feasible point contains the entire affine fiber `w+ker M`, of
dimension `J-rank M >= J-(2N+1)`. The statement requires nonemptiness.
A particular coordinate is unbounded in both directions along the fiber iff
its coordinate functional does not annihilate `ker M`; a kernel dimension
count alone does not prove this for **every** coordinate. The projected
feasible set is `{z in im M:H0+K(z)>=0}` and can itself be unbounded.
With H-SIGN it is intersected with the finitely generated moment cone
`cone{φ(t_j)}`; fibers are `M^{-1}(z)∩R_+^J`. All assertions follow directly
from the factorization and injectivity of K.

For an unconstrained dense grid, `J>2N+1` forces a kernel. With a prescribed
sparse support there can be exact recovery below the sampling spacing.
The phase perturbation from moving an atom by `δy` is `O(N|δy|/L)`, so
`h << L/N` controls ordinary moment approximation. It is not enough for a
matrix with an extremely small positivity margin: using normalized Fourier
basis entries gives, conservatively, `||T(y+δ)-T(y)|| <=
(2N+1)(2+4πN)|δ|/L`. This bound times the displaced mass must be below the
available spectral gap to guarantee feasibility by rounding.

For the even-M uniform grids in this brief there is an exact resolution
statement: `rank M_N = min(M-1,2N+1)`. Reflect the M/2−1 pairs and keep
the midpoint. In weighted-sum/difference pair coordinates, the cosine
block has rank `min(N+1,M/2)` and the sine block rank
`min(N,M/2−1)`, by the Chebyshev Vandermonde argument used in the signed
control below. The ranks add to the stated formula. Thus unrestricted
weights on this grid are determined by **given moments** iff
`M<=2N+2`, equivalently `h>=L/(2N+2)`. This exact sampling count does
not prevent a sparse positive measure from being determined by moments
on a much finer grid, as G2 shows.

## G2. Moment fibers and the actual prime measure — PROVED / SHARPENED

Let `F_m={μ>=0:Mμ=m}` consist of finite measures. Under H-FIN all of
`F_{Mμ*}` is admissible. The converse is false: admissibility imposes an LMI
on m, not the equality `m=Mμ*`.

**Extremality theorem.** A member μ of F_m is extreme iff it is finitely
atomic and its occupied moment vectors `φ(t_k)` are linearly independent.
In particular it has at most `d=2N+1` atoms and no atom at L.

Proof. A dependence allows a sufficiently small plus/minus perturbation of
the positive occupied weights. If the support has more than d points,
choose d+1 disjoint sets of positive μ mass; the d+1 vectors
`∫_{E_i}φ dμ` are dependent, giving a bounded nonzero signed density with
zero moments and hence the same perturbation. Conversely, a decomposition
of μ as the average of two positive measures forces both to be supported
on its finite support; independence forces identical weights. This also
proves the assertion for non-atomic measures.

Every attainable m has an atomic representation with at most d atoms
(conic Carathéodory). One elementary justification: after normalization by
the finite original total mass, integration puts m in the convex hull of
the compact curve φ([0,1]); an affine Carathéodory representation is finite,
then conic dependence eliminates atoms down to d. Endpoint atoms can be
discarded. This is the bound proved here; an `N+1` Toeplitz quadrature bound
cannot simply be imported for these different moments.

**Exact sparse uniqueness theorem.** Suppose μ* has s distinct interior
atoms, and `N>=2s`. Then F_{Mμ*}, on `[0,L)` (or with mass at L fixed to
zero), is the singleton `{μ*}`.

Proof. Put `c_k=cos(2πt_k)`. The nonnegative function

`p(t)=(1-t) ∏_{k=1}^s (cos(2πt)-c_k)^2`

lies in the span of `A_0,...,A_{2s}`, has zero integral against μ*, and
vanishes in `[0,1)` only at the t_k and their reflections `1-t_k`.
Any positive measure with the same moments must live on that finite set.
Group that set by distinct values c. The cosine moments (Chebyshev
Vandermonde) determine each grouped weighted sum
`(1-t)w_t+t w_{1-t}`; the sine moments (the polynomials U_{n-1}) determine
`w_t-w_{1-t}`. These two equations determine both weights. The single
point t=1/2 uses only the cosine equation. This proves uniqueness, including
coincident reflected pairs. The bound is sufficient, not claimed sharp.

For x=13 the eight visible atoms are 2,3,4,5,7,8,9,11, with weights
`log p/sqrt(p^m)`. Thus `N>=16` suffices for exact-moment uniqueness. For
x=25 the thirteen visible atoms are 2,3,4,5,7,8,9,11,13,16,17,19,23;
`N>=26` suffices. Both are below the full-window determinant saturation
cutoffs 56 and 134 from the reviewed round-1 computation. At the endpoints
13 and 25 the true weights are nonzero but invisible; allowing that mass to
vary destroys uniqueness. No zero information enters this argument.

Extremality alone does not imply uniqueness: at N=0 each single interior
atom with adjusted weight gives the same prescribed A_0 and is extreme.
At the present larger cutoffs uniqueness follows from the explicit p,
not just from the atom count. Sparse exact-moment recovery is therefore
possible; recovering those moments from the positivity inequality remains
the separate question. If H*>0 at a finite cutoff, small new positive
atoms remain feasible by `||T(y)||<=2`; exact support recovery from this
inequality alone fails at every such cutoff.

## G3. The proposed near-kernel support theorem — REFUTED; replacement PROVED

Extend f by zero beyond its window and normalize the Fourier modes in
L². The actual sensitivity is

`q_v(y)=-v* T(y)v = 2 Re ∫ conjugate(f(u)) f(u+y) du`.

It is a positive-definite autocorrelation function, which does **not** mean
pointwise nonnegative. For a single Fourier mode,
`q(y)=2(1-t)cos(2πnt)`, negative for example at n=1,t=1/2.
It is an affine-envelope trigonometric function, not a trigonometric
polynomial. Its Fourier transform, rather than its pointwise value, is
nonnegative. Even an exact null vector says only

`∫q_v dμ* = v*H0 v`,

not that this integral is zero or that individual atoms occur at zeros.
The right side can have either sign. For arbitrary admissible μ it gives
the one-sided inequality `∫q_v dμ <= v*H0 v`. Near-singularity does not
repair these two missing steps. This refutes the requested theorem.

**Replacement (dual localization).** If `Z>=0` and
`p_Z(y)=tr(Z T(y))>=0` on the allowed set, then every admissible μ obeys
`∫p_Z dμ >= -tr(ZH0)`; this sign gives no small upper bound. To obtain
the useful upper bound instead require `q_Z(y)=-tr(Z T(y))>=0`. Then

`∫q_Z dμ <= tr(ZH0)`.

Consequently `μ({q_Z>=η}) <= tr(ZH0)/η`. This becomes informative only
when the cost is small and q_Z is nonnegative. More generally with known
moment equalities one may add their dual functions and subtract their
known costs. Near-kernel eigenvectors supply candidate cuts but establish
neither nonnegativity nor a small pole/archimedean cost automatically.
An exact-moment support certificate such as p in G2 is of this latter
kind. Proof of all bounds: take the trace of the PSD inequality against Z,
then use nonnegativity of the measure. These conditions, not the zeros of
individual autocorrelations, are the appropriate position certificates.

## G4. Uniform grids: an empty feasible set — NUMERICAL, ball-certified

The experiment's first outcome is **infeasibility**, not a diffuse admissible
measure. In every requested uniform-grid case, even the eigenvector LP
relaxation is empty under H-SIGN. Consequently coordinate boxes, total-mass
extrema, minimum-norm and maximum-entropy admissible measures, and distances
of those nonexistent optimizers to a histogram are **undefined**. A negative
LP upper bound must not be plotted as a recovered zero weight. No feasible
SDP axis section exists on these uniform grids either.

For cuts `G w+b>=0`, the displayed certificate is a nonnegative vector y
with `G^T y<0` and `b^T y<0`. If `w>=0`, the inequalities would imply
`0<=y^T(Gw+b)<0`. HiGHS proposes y using `sum y=1`; mpmath at 160 digits
repairs its residual with the constant-test cut. A separate C verifier
reconstructs the test vectors, their PSD positive combination, the
pole/archimedean data, and every grid sensitivity in **1024-bit Arb balls**.
All eleven strict contradictions certify. These certificates use no zero
ordinates or RH. The normalization after the tiny repair differs slightly
from one; these are certificate costs, not claimed optimal separating margins.

| x | N | M (`h=L/M`, J=M−1) | certificate `b^T y` |
|---:|---:|---:|---:|
|13|20|64|−1.77218006360e−4|
|13|20|128|−5.22841053980e−5|
|13|20|256|−8.15313837417e−6|
|13|40|64|−1.76874875812e−4|
|13|40|128|−5.19936149409e−5|
|13|40|256|−7.99157226501e−6|
|13|60|64|−1.77041384553e−4|
|13|60|128|−5.15631496452e−5|
|13|60|256|−8.00093935025e−6|
|25|60|128|−8.49321221948e−5|
|25|134|128|−8.47189232157e−5|

This is already a positional observation: the prescribed small displacement
of all atoms onto any of these grids destroys feasibility. It is not a
proof of global uniqueness of an unknown continuum support. A strictly
positive finite true matrix permits sufficiently tiny changes in positions
as well as weights, by the continuity bound in G1.

### Feasible union grids and precision protocol

The optional control uses the union of the grid with every `log n`,
`2<=n<x`, not just the prime powers. It has M+10 positions at x=13.
At x=25, `log 5=L/2` is already on the grid and is deduplicated, giving
M+21 positions. The true visible measure is explicitly feasible; both true
blocks are certified positive by 1280-bit Arb Cholesky. Its masses are
4.260495442124349047 at x=13 and the value tabulated below at x=25.

The box control deliberately distinguishes three convex sets: the full
SDP, the LP with selected true eigenvector cuts, and the latter with sign
constraints on the occupied true coordinates relaxed. We compute the
third as an **outer bound for the first**: 20 smallest-eigenvector cuts
at x=13, 30 at x=25; the other grid/composite weights remain nonnegative.
This centered LP has the true displacement zero as a feasible initial
basis. A deterministic 160-digit simplex avoids HiGHS tolerance artifacts
when eigenvalues are below 1e−100. Every returned primal/dual basis is
solved afresh and audited; the later 180-digit residual repair uses the
independent constant-test bounds `0<=w_j<=H0_00/[2(1-t_j)]`.
Thus the displayed bounds remain valid for the actual sign-constrained
SDP even when the selected-cut relaxation is larger. These box numbers
are high-precision numerics, not exact full-SDP projections or ball
certificates. The uniform-grid **emptiness** results above are ball-certified.

The eigenvectors are selected using true prime data. They are legal
prime-side verification witnesses under the brief, but this selection is
not a blind algorithm for discovering primes without using their locations.
Likewise the numerical dual functions are checked on their finite allowed
grids. Their sign between grid points is not certified, so these boxes
cannot be transferred unchanged to a free continuum of positions.

### Signed grid control — PROVED / NUMERICAL

At x=13,N=20,M=64 the map has rank 41 and nullity 22. This rank also has
an exact proof: group the 31 reflected pairs and midpoint by
`c=cos(2πj/64)`. The invertible pair coordinates are the weighted sum
`(1-t)w_t+t w_{1-t}` and difference `w_t-w_{1-t}`. The cosine block is a
21-row Chebyshev Vandermonde on 32 distinct c's; the sine block is a
20-row Chebyshev-U Vandermonde on 31 distinct c's with nonzero sine
factors. Their ranks add. Symmetric pair perturbations have zero sine
moments and give 32 cosine unknowns against 21 independent equations;
every coordinate participates in a null vector, by Vandermonde independence.

The script constructs signed weights with `M w=-M(H0)+M(I)`, giving
`H(w)=I` with residual 8.90e−162 at 160 digits (seven negative weights).
Every weight box is `(-∞,+∞)`. Surjectivity makes the projected set the
entire translated positive kinematic cone: each diagonal prime moment
has interval `[-a_n^0,+∞)` and each sine moment `(-∞,+∞)`. To attain the
diagonal lower endpoint cancel all H0 entries and choose a diagonal PSD
remainder with that diagonal zero; any sine datum can be made feasible
by adding a sufficiently large identity. Thus projecting to moments
removes the kernel ambiguity but does **not** restore bounded boxes.

### Union-grid mass localization — NUMERICAL

`near` means within h of any **visible** prime-power position; `far` is
its complement, including the upper-edge strip. These are optimized
linear mass objectives, not sums of separately optimized coordinate
upper bounds. `R` is the guaranteed lower bound `near_lower/far_upper`
for any feasible measure (infinite if its far mass is zero). Digits below
are rounded for readability; full precision and every coordinate are in
the output and `checks/boxes_x*_N*_M*.json`.

| x | N | M | total mass outer interval | near mass lower | far mass upper | R lower |
|---:|---:|---:|---|---:|---:|---:|
|13|20|64|[4.26043620,4.41494498]|4.25868188|0.154824327|27.5065|
|13|20|128|[4.26041014,5.09625498]|4.25407363|0.836012572|5.08852|
|13|20|256|[4.26039105,6.93188397]|4.24004959|2.67154402|1.58711|
|13|40|64|[4.2604954419,4.2606545881]|4.2604954378|1.59147017e−4|26770.8|
|13|40|128|[4.2604954417,4.2709350731]|4.2604954264|1.04396324e−2|408.107|
|13|40|256|[4.2604954416,4.4931470518]|4.2604953943|0.232651612|18.3127|
|13|60|64|[4.26049544209,4.26054006172]|4.26049544153|4.461972894e−5|95484.5|
|13|60|128|[4.26049544208,4.26429958825]|4.26049543997|3.804146290e−3|1119.96|
|13|60|256|[4.26049544206,4.36896311458]|4.26049543555|0.108467673|39.2789|
|25|60|128|[7.161622730925,7.161631690344]|7.161622730900|8.959428386e−6|799339|
|25|134|128|[7.161622730928504098,7.161622731198028830]|7.161622730928504098|2.695247304e−10|2.657130097e10|

The upper edge is the main weakness of these outer bounds: for the
x=13 cases the far-mass optimum equals the last grid coordinate's
individual upper bound to the printed precision. At N=60 this is
4.46197e−5 at `63L/64`, but 0.108468 at `255L/256`. Increasing M adds
points closer to the invisible endpoint; worse total-mass localization
on a finer grid is therefore not evidence of worse interior resolution.
Nor does a large outer bound establish that the full SDP permits that
much edge mass.

At x=13,N=60,M=256 the logarithmic coordinates have these outer boxes;
the eight nonzero weights form the prominent interior peaks. Zero
lower endpoints on all other coordinates follow from feasible truth.

| n | lower | upper |
|---:|---:|---:|
|2|0.490129071734273595832270|0.490129071734273595856951|
|3|0.634284100597563976781468|0.634284100597563977186388|
|4|0.346573590279972649056929|0.346573590279972654708616|
|5|0.719762515553600451927669|0.719762515553600491218663|
|6|0|7.36813464191e−19|
|7|0.735484904010973427280049|0.735484904010998296299369|
|8|0.245064535866101579606591|0.245064535867136798165156|
|9|0.366204096199711445995026|0.366204096222703247855314|
|10|0|2.60106226514e−12|
|11|0.722992574831081834842185|0.722992627858829142097575|
|12|0|2.69709148669e−7|

The tabulated last digits are numerical values, not directed-rounding
ball endpoints. The independent residual corrections are at most
3.48e−140 in the x=13 boxes, 3.45e−122 at x=25,N=60, and 3.52e−113 at
x=25,N=134. They use a genuine a priori mass scale; we do not infer
validity from a small dual residual without bounding its effect.

### Exact SDP axis sections — NUMERICAL, 100-digit inertia

For the feasible x=13,N=20 union with M=64, hold every other weight at
truth and change the displayed coordinate by δ. Bisection of the full
even and odd matrices with unpivoted LDL positivity tests brackets each
endpoint to relative width below 1e−23. These are the full PSD constraint
**on an axis**, hence inner sections of coordinate projections, not
optimal boxes with other coordinates free.

| coordinate | sign of δ | magnitude at boundary |
|---|---:|---:|
|L/64|+|7.89437249044180517518584e−40|
|17L/64|+|9.20188701152767829123385e−39|
|63L/64|+|1.41188496521917254173731e−6|
|log 2|−|2.94704199030315828891318e−36|
|log 2|+|1.00762957312922033924240e−38|

Both inside-positive and outside-indefinite endpoints are retained in
`checks/axis_sections.json`. The large edge/interior disparity is already
present in actual feasible sections, though the outer LP bounds are much
larger than these section widths.

For completeness, on each feasible finite union grid the minimum squared
norm and the minimum of `Σw log w` exist uniquely by compactness and strict
convexity (`0 log 0=0`). Since H* is positive definite, adding a sufficiently
small positive amount at **every** grid position gives a strictly positive
weight vector with PSD form. Convex mixing with that vector shows that the
`Σw log w` minimizer has every weight positive: the `t log t` improvement
at a zero coordinate dominates the O(t) change elsewhere. Thus even an
entropy optimizer cannot literally recover the sparse support. This is
an existence/support statement, not a computed union-grid optimizer;
the requested uniform-grid optimizers are absent as proved above.

## G5. Near-kernel profiles — NUMERICAL; G3's location rule fails

We take the eight smallest eigenvectors of the x=13,N=60 true matrix.
Their sensitivities are evaluated on all 255 interior points of the
L/256 grid, and independently at the eight exact prime-power positions.
`checks/near_kernel_profiles.tsv` is the plot-data table. Every sign
crossing detected on that grid is refined by 180 bisections in 160-digit
arithmetic. This counts **detected crossings**, not a certified global
zero count; tangencies and crossings within one cell could be missed.

The correlation below is Spearman between `−|q_v|` and minus distance
to the nearest prime-power position. It can be moderately positive
because both quantities depend strongly on y; it is not a zero-set
identification statistic.

| vector (0-based) | eigenvalue | fraction q<0 | detected crossings | crossings within h of a prime power | correlation |
|---:|---:|---:|---:|---:|---:|
|0|1.01356e−58|0|0|0|0.619207|
|1|8.54688e−55|0.882353|1|0|0.567447|
|2|3.70021e−51|0.133333|2|0|0.564368|
|3|1.07551e−47|0.8|3|0|0.478450|
|4|2.53815e−44|0.211765|4|0|0.496023|
|5|4.59682e−41|0.701961|5|0|0.333664|
|6|5.10118e−38|0.278431|8|0|0.454953|
|7|3.39568e−35|0.690196|9|0|0.437590|

The smallest-vector q is positive on this whole interior grid and has
`q(log 2)=0.124124192448681281`,
`q(log 3)=0.000882317836679668784`,
`q(log 11)=1.0919383252618063e−34`.
Smallness at large y is an envelope effect, not evidence for isolated
prime support: values between the later primes are small as well.
The next vector has its first detected root at
`y=0.307108616089253715988577`, distance
`0.38603856447069159` from the first prime position log 2. All 32 detected
crossings across these eight vectors miss every prime-power position by
more than h. The exact prime evaluations, complete root lists and
nearest-root distances are retained in `checks/near_kernel.json`.

## G6. Larger window — NUMERICAL, with certified uniform-grid infeasibility

Both x=25 uniform grids remain empty under H-SIGN, with strict Arb
Farkas margins around −8.5e−5. The union, containing thirteen visible
prime powers among all integer positions, has true total mass
`7.1616227309285040987`. On that feasible control the far-mass bound
improves from `8.95942838552e−6` at N=60 to
`2.69524730385e−10` at N=134, a factor of approximately 33,241.6.
The near/far ratio lower bound rises from 7.99339e5 to 2.65713e10.
This is improvement at a fixed grid spacing within the larger window,
not an assertion that the pure grid becomes feasible.

At N=134 the composite coordinate log 6 has upper bound
`2.46551636223e−57` and log 12 has upper bound
`1.13084665287e−48`; the log 23 lower bound is
`0.653795739213813699696398` against true weight
`0.65379573921381370155`. All coordinates, including the deduplicated
log 5 point, are tabulated in the output.

## Numerical checks for the blind lane

Reproduce with `python3 scripts/rtp2_grid_tomography.py >
outputs/rtp2_grid_tomography.txt`. The script compiles only under this lane's
`checks/`, linking the existing `zst/build/libzst.a`; it never builds or
modifies zst. `--prepare`, `--boxes`, `--verify`, `--supplemental` and
`--report` expose the individual stages. The default runs them all.
All number-producing inputs are primes, pole and archimedean data.

For the following three boxes, use x=13,N=60,M=64 and the union with
log 2,...,log 12. The 20 smallest eigenvector cuts, zero-coordinate sign
constraints, and free occupied-coordinate displacements define the stated
outer LP; do not compare these values to full-SDP projections.

| check | target |
|---|---|
|upper weight at L/64|1.19432844295284757877e−25|
|upper weight at 17L/64|4.53241895982741147708e−22|
|upper weight at log 6|6.62432918801208870802e−19|
|x=25,N=134,M=128 union: near/far mass ratio lower|2.6571300973791111104e10|
|x=13,N=60, second-smallest vector: first detected q root|0.307108616089253715988577|

Additional discriminating check: on the **pure** x=13,N=20,M=256 grid,
`b^T y = -8.15313837417e−6`, `y>=0`, `G^T y<0`, all independently
verified in Arb. The 200-digit matrix data, test vectors, 170-digit
Farkas inputs, dual box vectors, repaired residual summaries, axis
brackets and profile tables are saved under `checks/`. The 100-digit
axis upper threshold at `17L/64` is 9.20188701152767829123e−39, much
smaller than a coordinate projection outer bound.


## What this changes in the notebook

The reproducible run ends with **117 checks passed, zero failed**. Eleven
uniform-grid infeasibility certificates pass a separate Arb verifier;
eleven feasible-union box tables have independently bounded residual
corrections; five axis endpoints have 100-digit inside/outside inertia
brackets. Source/output hashes are in `checks/manifest.json`. No claim
has been registered in a shard or database by this lane.

The measure formulation is the correct tomography problem, with an
explicit distinction between **observing moments** and **imposing positivity
on their assembled matrix**. At the present cutoffs the exact moments
uniquely determine the sparse visible prime measure. Positivity alone
allows a neighborhood of weights and positions whenever the finite true
matrix is positive definite. Lane L's conditional fixed-window coercivity
obstruction therefore persists when positions are freed. Nothing here
establishes infinite-window positivity or assumes RH.

H-SIGN changes the geometry decisively: it makes each finite interior
grid set compact when nonempty and turns near-kernel cuts into useful
support constraints after suitable nonnegative dual combinations. It
also exposes the failure of the chosen discretization: every prescribed
pure grid is empty. The union controls show strong interior concentration
and a weaker edge region; they do not discover positions independently,
since the true logarithmic positions and eigenvectors enter their
construction. A single small eigenvalue or the zeros of its individual
signed autocorrelation are insufficient support certificates. Full SDP
coordinate projections and continuum stability bounds are not supplied
by these LP outer boxes.

Candidate claim rows for shard 08j (for REFUTE review, not registration):

| candidate label | status | precise content |
|---|---|---|
| `prop:window-measure-moment-factorization` | PROVED | The window sees exactly the 2N+1 Loewner moments; it need not determine their values. |
| `prop:window-sign-grid-compactness` | PROVED | On a finite interior grid, the constant test bounds weighted mass; H-SIGN gives compactness even at N=0. |
| `prop:loewner-sparse-measure-uniqueness` | PROVED | Given exact moments, N>=2s recovers an s-atom interior measure; the invisible endpoint must be fixed or quotiented out. |
| `obs:near-kernel-support-correction` | PROVED / REFUTED | Individual q_v are signed autocorrelations; localization requires a nonnegative dual function with small known cost. |
| `num:rtp-grid-infeasibility` | NUMERICAL, ball-certified | All eleven specified uniform grids are infeasible with H-SIGN. |
| `num:rtp-grid-union-localization` | NUMERICAL | Selected-cut outer boxes on grids containing the true positions; x=25 far-mass bound improves by about 3.324e4. |

**Next experiment.** First exclude a specified edge strip, or constrain
weighted mass instead of ordinary mass. Then solve the unknown-position
problem with movable atoms and adaptive separating eigenvectors computed
from the current candidate, without seeding log n. Compare this with
shifted uniform grids under the explicit relaxation `H(mu)>=-tau I`.
Track the minimum required tau versus h, and the recovered support versus
tau; the Farkas witnesses here already give lower bounds on the required
relaxation. This separates discretization error, conditioning of the
moments, and the information supplied by positivity. In particular,
compare **dual nonnegative support certificates** with the exact-moment
annihilator of G2, rather than searching for prime locations among zeros
of individual near-kernel autocorrelations.
