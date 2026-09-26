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

## I1 numerical threshold table (PROVED finite search; 40-digit logarithms)

In each cell the exact threshold is half the logarithm of the displayed rational separation. The binding pair is `r : k`. The external threshold also equals the full admissibility threshold in all twelve rows; this equality is a result of this enumeration, not a general principle.

| S | A | external E: delta; r:k; separation | excess exponent H: delta; r:k; separation |
|---|---:|---|---|
| [2] | 1 | 0.20273255405; 2:3; 3/2 | 0.34657359028; 2:4; 2 |
| [2] | 2 | 0.11157177566; 4:5; 5/4 | 0.34657359028; 4:8; 2 |
| [2] | 3 | 0.058891517828; 8:9; 9/8 | 0.34657359028; 8:16; 2 |
| [2] | 4 | 0.030312310908; 16:17; 17/16 | 0.34657359028; 16:32; 2 |
| [2, 3] | 1 | 0.077075339914; 6:7; 7/6 | 0.14384103623; 3:4; 4/3 |
| [2, 3] | 2 | 0.013699487094; 36:37; 37/36 | 0.058891517828; 9:8; 9/8 |
| [2, 3] | 3 | 0.0046083275525; 108:109; 109/108 | 0.058891517828; 18:16; 9/8 |
| [2, 3] | 4 | 0.00038565370211; 1296:1297; 1297/1296 | 0.058891517828; 36:32; 9/8 |
| [2, 3, 5] | 1 | 0.016394911411; 30:31; 31/30 | 0.032269260569; 15/2:8; 16/15 |
| [2, 3, 5] | 2 | 0.0011123475111; 450:449; 450/449 | 0.02041099726; 25/3:8; 25/24 |
| [2, 3, 5] | 3 | 3.7038408847e-05; 13500:13499; 13500/13499 | 0.011858263309; 125/8:16; 128/125 |
| [2, 3, 5] | 4 | 1.2345663771e-06; 405000:405001; 405001/405000 | 0.0056470033094; 2025/16:128; 2048/2025 |

The ratios are enumerated as exact fractions, and minimisation compares `max(k/r,r/k)` exactly; only the final logarithm is floating. The sieve covers every prime power up to 1,700,000. Its sufficiency is checked row by row: the largest lattice ratio times the winning multiplicative separation is below the sieve bound, so every omitted k is farther away. Nearest neighbours in each filtered prime-power list suffice by monotonicity of log. This gives an exhaustive proof of the binding pairs without relying on near-tied floating logarithms. Threshold values themselves are mpmath evaluations, not ball enclosures.

## I4. Width sweep (NUMERICAL)

The script copies/adapts A2's bump, autocorrelation scaling, pole/prime formulas, `psi_general`, and Fourier-basis `qU`; it does not import A2, which requires unavailable python-flint and runs its experiment on import. For overlapping entries it uses the full archimedean finite-part integral

`arch=(log(4pi)+gamma)q(0)/2 + int_0^Y [q(y)-exp(-y/2)q(0)]rho(y)dy + q(0)/2 log(tanh(Y/2))`,

where `q(y)=R_delta(y-D)+R_delta(y+D)`, `Y=D+2delta`. This includes off-diagonal F(0), which cannot be dropped once translates overlap. The prime sum contains every supported prime power. Nothing in the forms uses zeros.

Each set has 12 log-spaced widths from its admissible onset to 0.345. We stop before `log(2)/2=0.34657359027997265`, so neither the diagonal prime term nor the `log k+D` branch is active. At the boundary the bump is still zero; strictly beyond it k=2 starts contributing to the diagonal, and at still larger widths also to the plus branch off the diagonal. The same general integral and Kronecker identity remain valid. The first translate overlaps already occur at 0.1438410362 for {2,3}, A=2; 0.05889151783 for {2,3}, A=3; 0.05268025783 for {2,3,5}, A=2.

The following are coefficient-matrix eigenvalues, normalised by N_delta as in A2. `ov0` is absolute overlap with K's product ground vector; it is not the largest Schmidt coefficient. A dash means K is not positive definite, so the real covariance log-det gap is undefined.

**S=[2, 3], A=2.**

| delta | lambda(G) | lambda(K) | Schmidt defect | ov0 | log-det gap |
|---:|---:|---:|---:|---:|---:|
| 0.0136994871 | 0.6874305271 | 0.52448928 | 0.001236441 | 0.9986907 | -0.1334903 |
| 0.0183686982 | 0.5045212236 | 0.290999758 | 0.0023368556 | 0.9974121 | -0.32505 |
| 0.0246293217 | 0.3464870081 | 0.0777462637 | 0.0034242952 | 0.99597704 | -1.132964 |
| 0.0330237602 | 0.2295860346 | -0.108515313 | 0.0056509007 | 0.99263726 | — |
| 0.0442792844 | 0.1382920442 | -0.258882513 | 0.0080041801 | 0.98743053 | — |
| 0.0593710412 | 0.06643745839 | -0.36178461 | 0.0051970692 | 0.98468873 | — |
| 0.079606538 | 0.01829973519 | -0.404929326 | 0.00097201792 | 0.99108342 | — |
| 0.106738921 | 0.006830109103 | -0.384898452 | 0.0016705611 | 0.99810024 | — |
| 0.143118864 | 0.003234385513 | -0.285032049 | 0.0041223162 | 0.99697021 | — |
| 0.191898222 | 0.001800262413 | -0.167548725 | 0.003405899 | 0.98960485 | — |
| 0.257303103 | 0.0005090830911 | -0.0607235408 | 0.0029356036 | 0.99528057 | — |
| 0.345 | 8.842738307e-05 | -0.00847737417 | 0.0026738833 | 0.94038234 | — |

**S=[2, 3], A=3.**

| delta | lambda(G) | lambda(K) | Schmidt defect | ov0 | log-det gap |
|---:|---:|---:|---:|---:|---:|
| 0.00460832755 | 1.030630458 | 0.863576836 | 0.0012566744 | 0.99850129 | -0.07289666 |
| 0.00682231936 | 0.7527191157 | 0.518075235 | 0.0025284361 | 0.99689695 | -0.1892261 |
| 0.0100999855 | 0.4955002035 | 0.194871766 | 0.0026794112 | 0.99657438 | -0.6312442 |
| 0.01495235 | 0.2741685566 | -0.0955905562 | 0.0013215956 | 0.99793039 | — |
| 0.0221359498 | 0.1299187792 | -0.338247879 | 0.00052799175 | 0.99823475 | — |
| 0.0327707866 | 0.06594268361 | -0.511878442 | 0.00335686 | 0.9947137 | — |
| 0.048514948 | 0.01883676831 | -0.592137121 | 0.0210979 | 0.98444373 | — |
| 0.0718231214 | 0.006620376728 | -0.587565661 | 0.014563664 | 0.98698989 | — |
| 0.106329306 | 0.001637119907 | -0.483366633 | 0.020145599 | 0.98883013 | — |
| 0.157413395 | 0.0002590331134 | -0.276761307 | 0.0020598887 | 0.99673666 | — |
| 0.233039956 | 7.450302748e-05 | -0.103111498 | 0.011265276 | 0.97456529 | — |
| 0.345 | 1.483654777e-05 | -0.00917192218 | 0.01119416 | 0.99235692 | — |

**S=[2, 3, 5], A=2.**

| delta | lambda(G) | lambda(K) | Schmidt defect | ov0 | log-det gap |
|---:|---:|---:|---:|---:|---:|
| 0.00111234751 | 1.803901214 | 1.69212545 | 0.00045594205 | 0.99947439 | -0.01915962 |
| 0.00187390527 | 1.368850727 | 1.18711286 | 0.0011653749 | 0.99860283 | -0.05263348 |
| 0.00315685606 | 0.9826962321 | 0.693408077 | 0.002827511 | 0.99636953 | -0.1629624 |
| 0.00531816645 | 0.6455818081 | 0.218723098 | 0.0052172976 | 0.99263512 | -0.7148237 |
| 0.00895919671 | 0.358650364 | -0.224008573 | 0.0035381066 | 0.9918239 | — |
| 0.0150930225 | 0.1558575516 | -0.613179374 | 0.0041950765 | 0.99202844 | — |
| 0.0254263116 | 0.05333277369 | -0.912982341 | 0.017018849 | 0.98774765 | — |
| 0.0428341852 | 0.01317663846 | -1.0652619 | 0.0055426838 | 0.98419834 | — |
| 0.0721601881 | 0.002694070451 | -1.04383401 | 0.027288664 | 0.97830339 | — |
| 0.12156395 | 0.0002400983494 | -0.783368912 | 0.0097666353 | 0.98924399 | — |
| 0.20479151 | 3.77753224e-05 | -0.301315159 | 0.0021815292 | 0.95647079 | — |
| 0.345 | 3.111698119e-06 | -0.0168139286 | 0.0014531568 | 0.93690201 | — |

**Exact decomposition.** Put M=M_pole+M_arch+M_prime, with the mixed prime part negative and including E,H,R. The true first-order perturbation is `sum v0* M_j v0`. The three expectations along the final vector v are exact Rayleigh contributions, but do not alone add to the eigenvalue shift:

`lambda(G)-lambda(K) = sum_j v* M_j v + [v* K v-lambda(K)]`.

The final bracket is nonnegative relaxation cost. For a second exact accounting, the output also prints the successive minimum-eigenvalue increments along `K -> K+M_pole -> K+M_pole+M_arch -> G`; this telescopes exactly but depends on the stated order. Individual expectations along v are not causal attribution of a nonlinear eigenvector response.

Selected rows below show the cancellation. All 36 rows, full vectors, product vectors, prime lists, first-order triples, final-vector triples, relaxation costs, and exact path increments are retained in `outputs/rtp2_impure_bumps.txt` and `checks/results.json`.

| S; A; delta | first order at v0: pole, arch, prime | at v: pole, arch, prime | relaxation | exact shift |
|---|---|---|---:|---:|
| [2, 3]; 2; 0.01369949 | +0.2339696, -0.06611433, +0 | +0.2252615, -0.06763114, +0 | 0.005310872 | 0.1629412 |
| [2, 3]; 2; 0.07960654 | +1.27813, -0.3781397, -0.4689057 | +1.112293, -0.3521277, -0.3565702 | 0.01963415 | 0.4232291 |
| [2, 3]; 2; 0.345 | +6.150606, -1.699253, -4.442601 | +4.899942, -1.589995, -3.302965 | 0.001584574 | 0.008565802 |
| [2, 3]; 3; 0.004608328 | +0.2191804, -0.04569372, +0 | +0.2068122, -0.04658293, +0 | 0.006824331 | 0.1670536 |
| [2, 3]; 3; 0.04851495 | +2.045479, -0.4610263, -0.959541 | +1.669653, -0.5081223, -0.5959949 | 0.04543832 | 0.6109739 |
| [2, 3]; 3; 0.345 | +12.534, -2.859004, -9.665806 | +11.00156, -3.076692, -7.915901 | 0.0002221988 | 0.009186759 |
| [2, 3, 5]; 2; 0.001112348 | +0.1373033, -0.02310675, +0 | +0.1326591, -0.02339625, +0 | 0.002512912 | 0.1117758 |
| [2, 3, 5]; 2; 0.02542631 | +3.038369, -0.5263767, -1.522073 | +2.624276, -0.5261057, -1.184553 | 0.05269789 | 0.9663151 |
| [2, 3, 5]; 2; 0.345 | +41.41288, -6.450069, -34.94591 | +32.01534, -5.710119, -26.29015 | 0.001742809 | 0.01681704 |

**No requested 0.1 crossing was found.** Non-admissibility permits large prime entries; it does not force a large Schmidt defect. The enlarged scan and its limitations are reported below. The positive forms involve cancellation between pole, archimedean and prime contributions; deleting prime blocks is not a positivity-preserving operation. The negative log-det gaps where both matrices are positive already disprove their identification as mutual information.

## I5. Addition of places and sensitivity (NUMERICAL; requested conditional experiment corrected)

There is no observed width with defect>0.1 on the requested range, so the instruction “at the delta of the O(1) observable” has no available input. We instead declare the fixed diagnostic width **delta=0.2**, and also compute 0.1, 0.05 and two narrow widths. This is not reported as an O(1)-Schmidt crossing. All prime sums are recomputed in the larger lattice; adding a coordinate also enlarges the range of third primes sampled. Thus prime addition does not isolate that new prime's weight.

The restriction sets the new exponent to zero, renormalises the resulting vector, and measures absolute Euclidean overlap, as in A2. At delta=0.2:

| A | added direction | lambda before | lambda after | overlap on old sublattice | old weight |
|---:|---|---:|---:|---:|---:|
| 2 | {2,3} -> {2,3,5} | 0.001353720633 | 0.00003821907721 | 0.9953742509 | 0.1804905499 |
| 1 | {2,3} -> {2,3,5} | 0.009617377905 | 0.002228248928 | 0.9865821133 | 0.5 |
| 1 | {2,3,5} -> {2,3,5,7} | 0.002228248928 | 0.0002422501422 | 0.9814737108 | 0.5 |

| A; step | movement at 0.2 | at 0.1 | at 0.05 | at 0.001 | at 0.0005 |
|---|---:|---:|---:|---:|---:|
| 2; +5 | 0.00462574908 | 0.02000019069 | 0.01076029444 | 0.000411940039 | 0.0000973352011 |
| 1; +5 | 0.01341788669 | 0.00626558350 | 0.00710900945 | 0.00000266495499 | 0.000000660229703 |
| 1; +7 | 0.01852628918 | 0.01168672230 | 0.00604242012 | 0.0000360857361 | 0.00000881737952 |

Here movement is `1-overlap`. The narrow-width ratios are about four when delta doubles, consistent with the proved perturbative quadratic law under a fixed limiting gap. The wide-width sequence is nonmonotone; neither an asymptotic prime-learning exponent nor posterior-contraction law follows from these three direction additions. In particular this is not a MaxEnt completion experiment.

To isolate an external prime q, hold the lattice and width fixed and remove *all* powers of q from *all* entries. The next table uses {2,3}, A=2, delta=0.2; the true lambda is 0.00135372063318. `lambda_off` concerns an altered functional and is not an RH counterexample. The derivative column varies the common amplitude theta_q of the true negative q term about theta_q=1; it is not a finite-difference approximation to full removal.

| q | lambda_off | shift | 1-overlap | defect_off | d lambda/d theta_q | norm(dv/d theta_q) |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | -0.522422554 | -0.523776275 | 1 | 0.335202333 | -0.441838446 | 16.7302619 |
| 7 | -0.445422019 | -0.44677574 | 0.804990346 | 0.478853164 | -0.3338406 | 13.5277492 |
| 11 | -0.55884856 | -0.56020228 | 1 | 0.400488044 | -0.260513416 | 12.3335937 |
| 13 | -0.55469109 | -0.556044811 | 1 | 0.22938423 | -0.19185092 | 10.4226859 |
| 17 | -0.579160987 | -0.580514708 | 1 | 0.204830785 | -0.153998091 | 19.5387336 |
| 19 | -0.575973463 | -0.577327184 | 1 | 0.204637834 | -0.15315584 | 19.4361112 |
| 23 | -0.0549332966 | -0.0562870173 | 1 | 0.148747704 | -0.0175047952 | 2.2214311 |
| 29 | -0.098109883 | -0.0994636037 | 1 | 0.44632291 | -0.0103389763 | 1.14275498 |
| 31 | -0.265501847 | -0.266855568 | 1 | 0.456731052 | -0.0249790697 | 2.76090741 |
| 37 | -0.546651947 | -0.548005667 | 1 | 0.470862131 | -0.0490887763 | 5.42572514 |
| 41 | -0.301553517 | -0.302907237 | 1 | 0.45911847 | -0.0280860276 | 3.10431584 |
| 43 | -0.172842231 | -0.174195951 | 1 | 0.450023686 | -0.0169420437 | 1.87258431 |
| 47 | -0.0187553541 | -0.0201090747 | 1 | 0.455975396 | -0.00279193437 | 0.308589246 |
| 53 | 0.00135372063 | 1.54173549e-16 | 0 | 0.00319814799 | -1.6044619e-16 | 1.77339301e-14 |

All external primes through 47 make this altered form indefinite when individually removed. The support of 53 has just entered and its effect is below useful float64 resolution (its first-order contribution is about 1.6e-16); the tiny reported full-removal difference for 53 is numerical noise. Many removals give orthogonal ground vectors, a reflection-parity change rather than a small rotation. The exact derivatives and the finite-removal results quantify quite different regimes because the spectral gap is small.

At the same width the sector removals are:

| form | lambda_min | Schmidt defect |
|---|---:|---:|
| full | 0.0013537206331 | 0.003198147992 |
| no_external | -2.9496987345 | 0.3810989831 |
| no_mixed_arch | -0.92987066659 | 0.3323333617 |
| no_mixed_pole | -3.8055745265 | 0.09151970754 |
| no_mixed_prime | -3.0178280392 | 0.3678526529 |

The genuine full form has small Schmidt defect while several altered forms have order-one defect. Thus the external prime data strongly constrain and, in this example, reduce the coefficient correlation left by the other terms. It would be misleading to assign a large correlation of a prime-deleted form to the true Weil form.

## I2/I4 support lists and the failed crossing search (NUMERICAL)

External primes active somewhere in the two-prime form (including axes) are as follows. “Active” means strictly positive mathematical bump support; an entry can be exponentially tiny near onset. Complete lists at every sweep width, including the much longer three-prime lists, are in the output's `SWEEP` records.

| A | delta | external primes |
|---:|---:|---|
| 2 | 0.02 | 37 |
| 2 | 0.05 | 11, 13, 17, 19, 37 |
| 2 | 0.1 | 5, 7, 11, 13, 17, 19, 31, 37, 41, 43 |
| 2 | 0.2 | 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53 |
| 3 | 0.02 | 7, 13, 37, 53, 71, 73, 107, 109, 211, 223 |
| 3 | 0.05 | 5, 7, 11, 13, 17, 19, 23, 29, 37, 53, 59, 67, 71, 73, 79, 101, 103, 107, 109, 113, 197, 199, 211, 223, 227, 229, 233 |
| 3 | 0.1 | 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263 |
| 3 | 0.2 | 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317 |

An additional 401-point log grid for each lattice gives:

| S | A | largest sampled defect | width at that sample | smallest sampled ground gap |
|---|---:|---:|---:|---:|
| [2, 3] | 2 | 0.0083513432148 | 0.27748777009 | 0.00027259572 |
| [2, 3] | 3 | 0.038148883729 | 0.24427388224 | 2.963482e-05 |
| [2, 3, 5] | 2 | 0.031980131971 | 0.068225721702 | 3.5744162e-06 |

There is **no first observed delta with Schmidt defect>0.1**. These are maxima on the stated finite grids, not certified suprema on the intervals; excluding every narrower unsampled peak is **OPEN**. The expectation of an observed 0.1 crossing in the requested sweep is not borne out. In particular there are no identified primes “driving” that nonexistent crossing. The single-prime sensitivity table is the available arithmetic response instead.

At {2,3}, A=2, delta=0.2 the finite Schur-complement theorem I2c gives

`0.002147677857 <= defect(v) <= 0.003201624504`,

while direct SVD gives 0.003198147992. This is a nonzero quantitative lower bound, well below 0.1. The small-perturbation norm hypothesis is not assumed merely because the measured defect is small. All the sweep records print ||M||, g, eta and whether ||M||<g/2 actually holds.

At the diagnostic width delta=0.2 the mixed prime split is itself quantitative:

| class | expectation along v0 | expectation along v | operator norm |
|---|---:|---:|---:|
| E: external primes | -1.390753653 | -1.517296509 | 3.001283247 |
| H: powers of 2 or 3 beyond A=2 | -0.04066886719 | -0.04205917985 | 0.1584962663 |
| R: represented powers leaking to mixed ratios | -0.09275883215 | -0.1310258173 | 0.4348349223 |

Thus the new prime part is mostly external in this example, but the omitted represented-power leakage is larger than the excess-exponent contribution. It cannot be removed from the general lemma. The q=5,7,37 spectral derivative formulas were also checked by centred finite differences of amplitude ±1e-6; eigenvalue derivative errors are below 2e-10 and vector derivative norm errors below 5e-8.

## I6. COMPARISON STEP — zeros used only here (NUMERICAL)

`data/zeros3000.npy` supplies the first 2000 positive ordinates as float64 numbers; these are not new ball-certified zeros. They are loaded only inside the explicitly labelled comparison function, after every form and sensitivity computation. Conjugate zeros supply the factor two:

`Z_M(D)=2 sum_(j<=M) cos(gamma_j D) [delta int_-1^1 phi_1(t)cos(delta gamma_j t)dt]^2`.

The two raw, unnormalised prime-side entries at delta=0.1 are 0.00471668172766817 (r=6; prime powers 5,7) and 0.00109526807815369 (r=8; prime powers 7,8,9). The first and 2000th positive ordinates are approximately 14.1347251417 and 2515.2865 respectively; the output prints the cached values at their available precision.

| ratio | M=10 error | 30 | 100 | 300 | 1000 | 2000 |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | 2.6584e-7 | 3.1473e-6 | 5.6532e-8 | 2.4842e-11 | 5.2276e-15 | 1.0807e-15 |
| 8 | 6.4975e-6 | 2.7906e-6 | 3.0848e-8 | 1.2282e-10 | 5.9690e-15 | 3.3220e-16 |

Fourier integrals are evaluated by Gaussian rules of orders 1024 and 1536, whose maximum difference is printed. The last errors reach the float64 ordinate/quadrature floor and must not be read as measured infinite-tail errors at 1e-18. The output additionally gives the sum of absolute terms from M+1 through 2000 (a finite remainder, **not** a bound on the omitted infinite tail). Signed errors need not decrease monotonically: the r=6 error increases from M=10 to 30. Repeated integration by parts gives faster-than-any-power decay of the smooth bump transform; the rapid drop before the numerical floor agrees with A2's Gevrey-bump truncation behaviour. No new fitted asymptotic constant is asserted. This is an implementation comparison of I3, not an RH assumption or certificate.
