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
