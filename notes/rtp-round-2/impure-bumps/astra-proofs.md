# RTP-2, lane I: impure lattice bumps

Author: `codex:gpt-6-astra`. Working research record; not registered. Binding brief: `notes/rtp-round-2/brief.md`.

## Correction ledger

1. **REFUTED (I1 sign/double counting).** Prime terms are negative. With A2's `G_nomix`, axis and diagonal terms are already included; only mixed masks may be added.
2. **REFUTED (I1/I2 rank).** A distance-pattern adjacency matrix need not have rank one. The support determines zero positions, not weights.
3. **REFUTED (I1(ii)).** Powers of primes in S, even with exponent at most A, can reach mixed entries. The brief omits this third category of leakage.
4. **SHARPENED (thresholds).** A power absent from the complete ratio set differs from a power unequal to the particular ratio it touches. Admissibility excludes both. At the onset itself the smooth bump remains zero.
5. **REFUTED (I3 unconditional squares).** The unconditional zero identity pairs off-line points. Squares require RH.
6. **SHARPENED (coordinates).** Translates can overlap before `2 delta=log 2`; the first overlap is at half the smallest lattice separation. Euclidean eigenvectors and Schmidt defects then remain coefficient diagnostics, not orthonormal function-space invariants.
7. **SHARPENED (I2 lower bound).** Rotation from a fixed product vector need not cause entanglement. A lower Schmidt bound requires the normal projection to product states, not merely the complement of v0.
8. **REFUTED (I4 terminology).** The Kronecker sum is not the block diagonal covariance of marginal blocks. Its log-det gap is not Gaussian mutual information and may be undefined because the baseline is indefinite.

## Hypotheses

**H-test:** S comprises distinct primes, A is a positive integer, delta>0, and the bump/convolution are exactly A2 §§1.1–1.2. Every matrix is divided by `N_delta=delta R_1(0)`. Coordinates are lexicographic. Orthogonality is not assumed.

**H-gap:** K=G_nomix has a simple ground eigenvalue lambda0 with gap g>0.
**H-small:** epsilon=||M||<g/2.
**H-RH:** all nontrivial zeros lie on the critical line. Used only in conditional theory, never form computation.

## I1. Corrected Kronecker lemma (PROVED under H-test)

Let `B_D[a,b]=1_{|t_a-t_b|=D}`, and let X mask pairs differing in two or more coordinates. Exactly

`P_k = sum_D [R_delta(log k-D)+R_delta(log k+D)] B_D/N_delta`.

Coefficients are nonnegative, positive precisely when `|log k-D|<2 delta`; the plus branch implies the same inequality. Their magnitudes depend on k beyond this support pattern. The span of touched B_D has dimension the number of distances, but this is not a matrix-rank bound. Counterexample: S={2}, A=1, k=3, delta=0.21. Only D=log 2 is touched, and `P_3=c [[0,1],[1,0]]`, c>0, has rank two and eigenvalues ±c. Entrywise positivity does not mean positive semidefiniteness.

For a displacement e define the truncated shift `T_e[a,b]=1_{b-a=e}`. Then `B_D=sum_{e:|sum e_p log p|=D} tensor_p T_(e_p)`. For D>0 unique factorisation leaves one pair e,-e; the individual shift rank is `prod_p(A+1-|e_p|)`, not one.

With `M_pole=X o pole`, `M_arch=-X o arch`, the exact decomposition is

`G = K + M_pole + M_arch - sum_k Lambda(k)/sqrt(k) (X o P_k)`.

Only finitely many prime powers enter: `k<exp(D_max+2 delta)`. Entrywise comparison proves, for every width,

`K=d I + sum_p I tensor ... tensor (G_(p)-d I) tensor ... tensor I`.

Each one-prime form is the full restriction, including foreign-prime contributions on its axis. The ground space is the tensor product of local ground spaces; under H-gap the ground vector is a unique product up to phase.

Separate (E) q^m with q outside S, (H) p^m with p in S and m>A, and (R) p^m with p in S and 1<=m<=A. E/H are exactly the prime powers absent from the complete ratio set. R can still leak: S={2,3}, A=1, k=2 reaches the mixed ratio 3/2 once `delta>log(4/3)/2`. Thus the proposed decomposition both double counts axes and omits mixed R terms.

For C=E,H the exact onset is `delta_C=min_(r in ratios,k in C)|log(k/r)|/2`. Full loss of admissibility instead minimises over k!=r and includes R leakage. For each rational r only the nearest members of C above/below it matter. Equality at the minimum still gives zero bump weight; entry occurs strictly above. The finite exact binding-pair table follows below. S-smooth numbers with two different prime factors never enter the prime-power sum.

## I3. Positivity and the contradiction pathway (SHARPENED; PROVED)

Write `z_rho=i(rho-1/2)` and `hat f(z)=int f(y)exp(-izy)dy`. Unconditionally,

`G_ab=N_delta^(-1) sum_rho overline(hat phi_a(conj z_rho)) hat phi_b(z_rho)`.

Proof: the transform of `f^* * g` is `overline(hat f(conj z)) hat g(z)`; apply the explicit formula in A2 §1.1. It gives exactly pole minus archimedean minus the full prime sum. Smooth compact support implies rapid horizontal-strip decay, making the paired sum convergent. For f=sum c_a phi_a this gives the same quadratic expression in f. Under H-RH the z_rho are real, hence the value is `sum_rho |hat f(z_rho)|^2/N_delta>=0`. Off-line, rho and 1-conj rho give z and conj z and the indefinite expression `2 Re(overline(hat f(conj z))hat f(z))`.

A certified negative eigenvalue of the true matrix therefore gives a smooth compact test function with negative Weil value and refutes RH. This is precisely `metric-as-state.md` §7.2 on the impure lattice class. Positivity of this restricted family is necessary, not claimed sufficient for RH. The review's mpmath real-space checks are independent numerical evidence at their listed widths, not ball certificates of all impure widths. No unconditional all-width positivity theorem is claimed here.

Even overlapping translates are linearly independent: a relation transforms into the nonzero entire bump transform times an exponential polynomial. The polynomial vanishes on an interval, hence identically, and distinct exponents force every coefficient to vanish. The L2 Gram matrix is `H_ab=R_delta(D_ab)/N_delta`; the generalised problem Gv=lambda Hv would be a different observable from A2's coefficient eigenvector.

## I2. What the channel measures; quantitative bounds (SHARPENED; PROVED)

**Proposition I2a (finite affine prime response, H-test).** Keep all positions log k, the lattice and delta fixed. For each prime q define

`B_q=sum_(m>=1) log(q) q^(-m/2) P_(q^m)`.

Then `G(theta)=pole-arch-sum_q theta_q B_q`, with only finitely many q. Equivalently its entries are affine functions of the independent weights `w_k=Lambda(k)/sqrt(k)` (linear after subtracting pole-arch); when a common local amplitude is varied they are affine in theta_q. Consequently an external prime's first-order contribution is its explicit-formula mass sampled near lattice ratios, not a correlation intrinsic to the places 2 and 3. This dependence is *exactly affine*, not merely first order. Eigenvalues and eigenvectors respond nonlinearly. The pattern matrices are generally high-rank, as I1 proves.

*Proof.* Substitute the full finite prime sum and group powers by their unique base prime. The maximum power is bounded by exp(D_max+2delta), proving finiteness. With a simple normalised eigenpair `(lambda,v)`, differentiation gives

`d lambda/d theta_q = -v* B_q v`,
`d v/d theta_q = sum_(j>0) v_j (v_j* (-B_q)v)/(lambda-lambda_j)`, in the gauge v*v'=0.

Mixed pole and archimedean entries remain genuine couplings of the chosen coordinates. Mixed leakage from the primes 2 and 3 also remains: the brief's exclusion of those first-order terms is false. Second-order spectral terms include products of local and external perturbations divided by gaps; they are spectral interactions of these data, not independent new arithmetic input. Removing one external prime means adding its full B_q, including any axis entries. Such a modified form need not be positive because B_q is not positive semidefinite.

**Proposition I2b (rotation bounds, H-gap and H-small).** Set `Q=I-v0 v0*`, `B=Q(K-lambda0)Q` on ran Q, `b=QMv0`, `eta=||b||`, and `W=lambda_max(K)-lambda0`. Choose the ground vector v of K+M with `a=<v0,v>>0`; write v=a v0+u. Weyl bounds give `|Delta lambda|<=epsilon`, and

`u=-a [B+QMQ-Delta lambda]^-1 b`.

Thus, with t=||u||/a,

`eta/(W+2epsilon) <= t <= eta/(g-2epsilon)`.

Since `||u||^2=t^2/(1+t^2)`, this yields two-sided bounds for departure from the fixed v0. For any bipartition across which v0 is a product, its Schmidt defect obeys

`defect(v) <= ||u||^2 <= eta^2/((g-2epsilon)^2+eta^2)`.

*Proof.* Project the eigenvalue equation by Q and use that the inverse bracket is positive definite with spectrum between g-2epsilon and W+2epsilon. Compare its action on b using its extreme singular values. The best product overlap is at least the overlap with v0. Simplicity of the perturbed ground follows from g-2epsilon>0.

There is no positive lower Schmidt bound in terms of eta and g alone: a perturbation `M_L tensor I` rotates a local ground vector while leaving the full ground vector a product. This refutes that reading of the brief's requested bound.

**Proposition I2c (a finite lower bound that detects entanglement).** At a chosen cut, express the normalised coefficient vector as a matrix in local orthonormal bases beginning with the factors of v0:

`C = [[a, y*], [x, Z]]`, `a>0`; let `T=Z-x y*/a`.

If `a>=||T||_2`, then

`||T||_F / [(1+||x||/a)(1+||y||/a)] <= sqrt(defect(v)) <= ||T||_F`.

The upper bound remains valid without the displayed hypothesis. These are finite, non-asymptotic bounds; a lower bound exceeding sqrt(0.1) proves the requested O(1) coefficient observable. The condition holds, for example, under `epsilon<g/4`: I2b gives ||u||<1/sqrt(5), a>2/sqrt(5), and `||T||<=||u||+||u||^2/a<a`.

*Proof.* The Schmidt defect is the squared Frobenius distance from C to the matrices of rank at most one. The rank-one matrix `[[a,y*],[x,xy*/a]]` proves the upper bound. Multiplication by `L=[[1,0],[-x/a,I]]` on the left and `R=[[1,-y*/a],[0,I]]` on the right takes C to diag(a,T). If a>=||T||_2, the squared distance of this diagonal matrix from rank one is ||T||_F^2, by the singular-value decomposition. For every rank-one C1, `||L(C-C1)R||_F<=||L||_2||R||_2||C-C1||_F`. Finally ||L||<=1+||x||/a and ||R||<=1+||y||/a. Infimise.

For an explicitly small parameter s, `G(s)=K+sM`, write `z=B^-1 QMv0` and let `N=(I-|v_L><v_L|) tensor (I-|v_R><v_R|)` project normal to the product tangent space. Analytic simple-eigenpair perturbation and I2c give

`defect(v(s)) = s^2 ||Nz||^2 + O(s^3)`.

Indeed x,y,Z are O(s), a=1+O(s^2), and `Z=-s Nz+O(s^2)`; therefore T=-s Nz+O(s^2), while the two norm bounds differ by a factor 1+O(s). This is the precise quadratic law, with the normal excitation rather than eta as its coefficient. It does not force an O(1) defect at finite width. At the measured crossings we additionally evaluate the finite I2c bounds, without pretending H-small holds if its norm test fails.

**Log-det statement (PROVED).** Where K and G are positive definite, `log det K-log det G` is a log-det gap. K is a Kronecker sum, not the direct sum of covariance principal blocks corresponding to a partition of variables. The Gaussian identity of A1.1(4), `2I=log det G_L+log det G_R-log det G`, therefore does not identify this gap as mutual information. It has no general nonnegativity guarantee. If K is indefinite, neither an absolute determinant nor an even number of negative eigenvalues repairs the covariance interpretation; we report the gap as undefined.
