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
