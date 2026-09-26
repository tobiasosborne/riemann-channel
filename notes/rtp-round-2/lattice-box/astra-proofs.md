# Lane L: lattice positivity, recession, and widths

Author: `codex:gpt-6-astra`.

Status: incremental research record. Computations use prime, pole and archimedean data only. No files in `zst/` are modified.

## Correction ledger

1. At `y=L` the entire atom matrix is zero, including the sine data. Its von Mangoldt weight need not be zero; its **observable contribution** is zero. Such a coordinate must be removed regardless of whether the endpoint is a prime power.
2. There is no recession threshold depending only on the number of atoms. Already one atom tending to zero defeats every fixed cutoff.
3. With `G delta >= -lambda`, `G^T y=+e_k` bounds **minus** `delta_k`, and `G^T y=-e_k` bounds **plus** `delta_k`. The signs in L2(i), read literally, are reversed.
4. A full-rank sensitivity matrix need not positively span the parameter space. Rank and a small eigenvalue alone do not give a two-sided width bound.
5. Finite-section positivity at `x=13` is not a certificate of positivity on the infinite window. Nor do the cited values establish `eps_N -> 0`: the reported sequence is saturating near a positive, very small floor.

## L1. Recession cone — SHARPENED / PROVED

**H-INT:** distinct positions `0<y_k<L`; put `t_k=y_k/L`, `s_k=min(t_k,1-t_k)` and

`r_k=ceil(1/(4s_k))`, `B=4 sum_k r_k`.

**Theorem L1.** For every `N>=max(m,B)`, `T_N(delta)>=0` implies `delta=0`. Every nonempty affine feasible set `P_N^lat` is then compact, independently of `H0`. If edge atoms are retained, their coordinates are free and the conclusion fails. There is no bound on the required cutoff in terms of `m` alone.

### 1.1 Convention and autocorrelation

Extend `f` by zero outside `[0,L]` and put `C_f(y)=int conjugate(f(u)) f(u+y) du`. The quadratic atom evaluation is `q_f(y)=2 Re C_f(y)` and `T_k[f]=-q_f(y_k)`. Summing the two shifted correlations in the stated Fourier basis gives exactly the formula sheet's diagonal `-2(1-t_k)cos(2 pi n t_k)` and off-diagonal `(sin(2 pi n t_k)-sin(2 pi j t_k))/(pi(n-j))`. In particular `||T_k||<=2` and `T_L=0`.

### 1.2 A finite positive trace annihilator

For each `k`, `r_k s_k` lies in `[1/4,3/4]`, hence `c_k=cos(2 pi r_k t_k)<=0`. The polynomial

`P(z)=prod_k (1-2c_k z^{r_k}+z^{2r_k})`

has nonnegative coefficients, constant and leading coefficients one, degree `d=2 sum r_k`, and vanishes at each `exp(2 pi i t_k)`. Set `Q(z)=P(z)(1+z+...+z^d)`. Every coefficient `q_n`, `0<=n<=2d=B`, is strictly positive: the constant term of `P` covers degrees `0..d` and its leading term covers `d..2d`. Therefore

`sum_{n=0}^B q_n cos(2 pi n t_k)=0` for every `k`.

If `T_N(delta)>=0`, its diagonal entries `a_n` are nonnegative. The displayed identity gives `sum q_n a_n=0`, so `a_n=0` for `0<=n<=B`. In a positive semidefinite matrix a zero diagonal entry forces its entire row to vanish (the two-by-two principal minors). In particular row zero vanishes, so `b_n=0` for every `|n|<=N`. All off-diagonal entries now vanish. For the injectivity argument we may use `a_n=0` for `0<=n<=m` since `B>=m`.

### 1.3 Injectivity, including reflected and rationally related positions

Group the positions by `u=cos(2 pi t)`. The cosine equations for `n=0..m` are a Chebyshev/Vandermonde system and force `sum_{t:cos(2 pi t)=u} delta_t(1-t)=0` in each group. A group has at most two members, `t` and `1-t`. The sine equations for `n=1..m`, using `sin(n theta)=sin(theta) U_{n-1}(cos theta)`, force `delta_t-delta_{1-t}=0` in each two-member group; the cosine equation then forces both to vanish. Single-member groups vanish already by the cosine equations (including `t=1/2`). Thus `delta=0`. Relations such as `y_j=2y_k` cause no exception.

### 1.4 Compactness and the absence of an atom-count threshold

For a nonempty spectrahedron its recession cone is exactly `{delta:T_N(delta)>=0}`. To verify the only potentially delicate direction, divide a feasible ray by its parameter and take a limit. A nonempty closed convex subset of finite-dimensional space is bounded iff its recession cone is zero: if unbounded, normalize a sequence relative to one feasible point and take a convergent subsequence of directions; convexity and closedness give a ray.

For fixed `N`, as `t -> 0+`, `T_N(t) -> -2I` entrywise. Hence `-T_N(t)>0` for sufficiently small positive `t`; `delta=-1` is a nonzero recession direction even for `m=1`. This refutes any universal threshold `N(m)`.

Finally, absence of a nonzero supporting functional implies that the conic hull of the atom-evaluation vectors is all of `R^m`: its closure has polar `{0}`, hence is all of `R^m`, and a convex cone dense in a finite-dimensional vector space equals that space (its relative interior agrees with that of its closure). The sign `T=-q` does not change this conclusion.

**Corollary (PROVED).** At a cutoff with zero recession cone, if there is a strictly feasible weight vector, the lattice problem has a unique maximum-determinant solution. The determinant attains its positive maximum on the compact feasible set; the maximizing form is positive definite, and strict concavity of `log det`, together with injectivity of `T`, gives uniqueness. This does not identify that maximizer with truth. The corresponding Loewner-coordinate MaxEnt problem remains unbounded.

## L2. Duality and the controlling spectral quantity — SHARPENED / PROVED

**H-FIN:** `H*=H_N(w*)>=0`. Write `delta=w-w*`, choose orthonormal eigenvectors, and let `G_ik=v_i^*T_k v_i`, `lambda_i=v_i^*H*v_i`.

### 2.1 Weak duality, SDP box, and LP box

Feasibility implies `lambda+G delta>=0`. For `y>=0`, `G^T y=-e_k` gives `delta_k<=lambda^T y`; `G^T y=+e_k` gives `-delta_k<=lambda^T y`. This follows by multiplying and summing the inequalities. It requires neither positive definiteness nor LP optimality.

The exact coordinate endpoints are, by definition, the infimum and supremum of `w_k` over the PSD constraint, i.e. SDPs. Under H-INT and the L1 cutoff they are attained whenever the set is nonempty. Restricting tests to the eigenvectors gives a containing polyhedron, hence an outer box. The full SDP dual allows arbitrary PSD matrices `Z`, with `tr(ZT_j)=+-delta_jk`; the eigenvector LP restricts `Z` to be diagonal in this fixed eigenbasis. If `H*>0`, finite-dimensional Slater duality identifies the SDP endpoints with their dual infima. Axis sections, and sections allowing just two weights to vary, are **inner** bounds on the full coordinate projections.

### 2.2 The sharp bound obtainable from fixed eigenvector cuts

For any set `I` of directions define

`B_k(I)=inf {sum_{i in I} lambda_i(y_i^++y_i^-): y^+,y^->=0, G_I^T y^+=e_k, G_I^T y^-=-e_k}`,

with value infinity when either constraint is infeasible. Then `width_k(P_N^lat)<=B_k(I)`. If the two LP extrema are finite, `B_k(I)` is exactly the width of that relaxed coordinate projection. Thus there is no sharper universal bound from these cuts alone. The two separate optima are preferable to twice their maximum.

### 2.3 A conditioning bound and the missing positivity condition

Suppose the rows of `G_I` positively span `R^m`, equivalently `G_I` has rank `m` and there is `h>0` with `G_I^T h=0`. Let `p_k` solve `G_I^T p_k=e_k`, and set `a_k=max_i |p_ki|/h_i`. Then `y^+=a_k h+p_k` and `y^-=a_k h-p_k` are dual feasible, so

`width_k <= 2 a_k sum_i h_i lambda_i`.

One can optimize `h,p_k`, or use the pseudoinverse right inverse to obtain an explicit bound. Normalize `sum h_i=1`; if these are the `r` smallest eigendirections, then `width_k<=2 a_k lambda_r`. The exact weighted expression retains more information than `lambda_r`. Necessarily `r>=m+1` for positive spanning; merely the `m` smallest eigenvalues and full column rank cannot suffice. Equivalently put `eta=min_{||d||_2=1} max_i(-g_i.d)>0`; feasibility gives `||delta||_2<=lambda_r/eta`, hence `width_k<=2lambda_r/eta`.

### 2.4 Why the minimum eigenvalue is insufficient

For example `H(delta)=diag(eps,1+delta,1-delta)` has minimum eigenvalue `eps` at truth but feasible width two for all `eps>0`. Even with `H=diag(eps+delta,1-delta)` the width tends to one. Any bound with constant permitted to grow like `1/eps` is tautological. A useful `C eps` statement needs a quantitative positive-spanning certificate supported on eigenvalues of order `eps`, including control of its dual mass. The width is controlled jointly by the low spectrum and the **positive-spanning conditioning** of its sensitivities.

### 2.5 Residuals are not exact certificates

If the computed equality has residual `r`, weak duality contains the additional term `r.delta`. Small absolute residual alone is insufficient when weights have no independently bounded scale. A rigorous implementation must solve the supported dual system in balls with nonnegative components, or bound this term using an independently certified box. The computations below distinguish their precision and certificate regime explicitly.

## L3. Fixed-window limit — SHARPENED; generic assertion REFUTED

### 3.1 A sufficient uniqueness theorem (PROVED-conditional)

**H-POS:** the true form is nonnegative on every Fourier polynomial in this fixed window. **H-PIN:** for each coordinate `k` there are cutoffs `N_j -> infinity` and PSD matrices `Z_j^+,Z_j^-` on `E_{N_j}` with

`tr(Z_j^+ T_l)=delta_kl`, `tr(Z_j^- T_l)=-delta_kl`, and `tr((Z_j^++Z_j^-)H*) -> 0`.

Then `P_infinity^lat={w*}`. Indeed every feasible displacement satisfies the two dual inequalities for every `j`; both costs are nonnegative under H-POS, and their sum tends to zero, so its `k`th coordinate is zero. It suffices to take diagonal `Z` as in L2 and require `B_k(I_j)->0`. In particular `lambda_{r_j}/eta_j -> 0` for positively spanning sensitivities suffices. Rank, or merely `eps_N -> 0`, is not this hypothesis.

Conversely, when the nested finite spectrahedra are eventually compact and contain truth, singleton intersection implies that every exact coordinate width tends to zero. Otherwise maximizers a fixed distance from truth have a convergent subsequence in the first compact set, whose limit belongs to every later set. With strict finite feasibility, SDP duality then supplies certificates H-PIN (arbitrarily close to each optimum). Thus the **full SDP** vanishing-cost condition is also necessary under these hypotheses; the diagonal LP version need not be necessary.

### 3.2 Coercivity forbids uniqueness (PROVED)

**H-GAP:** for some `mu_L>0`, `H*[f]>=mu_L ||f||_2^2` on the window form domain. Since `||T_k||<=2`, every displacement with `2 sum_k |delta_k|<mu_L` remains feasible on the whole window. Therefore `P_infinity^lat` contains an open neighborhood of truth. In particular exact finite-section coordinate widths are at least `mu_L` (take `delta=+-mu_L e_k/2`). This is a property of any coercive window form with these atom operators, independently of arithmetic.

H-POS alone does not imply uniqueness even within the distribution/Loewner framework: take the true form `I`, represented by `D=(1/2)delta_0`, and let `H0=I-T(w*)`. All the same interior atom matrices are present and H-GAP holds. No additional numerical smallness changes this logical counterexample.

Adding a constraint `w>=0` does not restore uniqueness under H-GAP. A sufficiently small positive displacement on the zero composite coordinates, leaving all prime-power coordinates unchanged, is feasible. Thus even strictly positive weights at **every** interior lattice position occur nearby; positivity cannot force the exact zero pattern at a fixed coercive window.

Even `eps_N -> 0` does not suffice in general nested PSD affine families: take `H*=diag(1,1,1/2,1/3,...)`, and `T(delta)=diag(delta,-delta,0,...)`. The finite minima tend to zero while the feasible interval remains `[-1,1]`. This last example illustrates the missing sensitivity hypothesis; it is not claimed to have the zeta kernel.

### 3.3 What is known for the zeta operator without RH (PROVED with cited input)

The form is closed, semibounded, has the Fourier polynomials as a form core, and its associated operator has compact resolvent. These are Proposition `Hilbert1` and Theorem `thmsmallest` of the supplied source, [Connes–Consani–Moscovici, Sections 3.1–3.2](https://arxiv.org/html/2511.22755v1#S3). In consequence `eps_N` decreases to the **attained** lowest eigenvalue `mu_L`. Under H-POS either `mu_L>0`, which invokes 3.2, or there is a nonzero actual kernel vector. A finite list of positive finite-section eigenvalues proves neither alternative, and does not prove H-POS. At `x=13` the cited `N=120,200` values are `3.48e-59,2.85e-59`, consistent with a positive floor, not evidence for a limit of zero.

The compactness argument can also be seen directly: the archimedean Fourier multiplier grows like `log(2+|t|)`, whereas the pole and the finitely many shifts are bounded. A bounded form-norm set has uniformly small Fourier tails. The map cutting off both position and frequency is compact, so the form-domain embedding into the window `L^2` space is compact.

### 3.4 COMPARISON STEP — theoretical RH implication, no numerical zeros

**H-RH:** the Riemann hypothesis. Under this hypothesis the fixed-window zeta form is strictly positive and, by compact resolvent, satisfies H-GAP. Thus **under RH, the actual fixed-window lattice set is not a singleton**.

Proof. The explicit formula under RH writes the form as a nonnegative sum of `|fhat(gamma)|^2`, with positive multiplicities. For an element of the closed form domain, approximate in form norm by core functions. Positivity of each summand and continuity of each evaluation on window `L^2` show that a null vector would have `fhat(gamma)=0` for every distinct zero ordinate. Its Fourier transform is entire of finite exponential type and bounded on the real line, so a nonzero such transform has `O(T)` zeros in `|z|<=T`, by Jensen's formula and the exponential-type bound (center Jensen at a point where the transform is nonzero).

There are more than linearly many **distinct** zeta ordinates under RH; multiplicities must not be overlooked here. Indeed `N(T)~T log T/(2 pi)` and Littlewood's RH bound `S(T)=O(log T/log log T)` bound every jump, hence every multiplicity near height `T`, by `O(log T/log log T)`. Consequently the number of distinct ordinates up to `T` is at least a constant times `T log log T`. The two counting inputs and the RH bound are recorded in [Carneiro–Chirre, Section 1.1, equations (1.2)–(1.3)](https://arxiv.org/html/1702.04099#S1.SS1). This contradicts the exponential-type zero count unless `f=0`. Thus the lowest attained eigenvalue is strictly positive. No zero location or RH assumption enters any numerical matrix or certificate in this lane.

**Reading.** Positivity at a fixed window can pin weights to an exceptionally small neighborhood, but exact recovery is not a consequence of RH; RH implies a nonzero neighborhood instead. The general H-PIN theorem is valid for any family of window forms, and is incompatible with H-GAP at a fixed window. For the specific fixed windows here, unconditional infinite-dimensional positivity and a prime-side quantitative lower bound remain unproved in this lane.

## L4. Multi-window boxes — NUMERICAL, with ball certificates

The script is `scripts/rtp2_lattice_box.py`; the reproducible output is `outputs/rtp2_lattice_box.txt`. It builds a C bridge under this lane's `checks/`, linking the existing `zst/build/libzst.a`. Totals and the prime-free data use the same window with prime cutoffs `X=x` and `X=1`. Independently summed atom formulas reproduce their difference to at least 190 decimal places. The interior positions are always `log 2,...,log(x-1)`; all five chosen endpoints are prime powers, but the endpoint exclusion is valid for any endpoint.

Precision: data and certificate solves are Arb balls at 1280 bits. Approximate eigenvectors come from FLINT/Arb's QR routine at 1152 bits (requested tolerance `2^-1100`). Each chosen vector is then frozen as exact dyadic coordinates; its Rayleigh cost and atom sensitivities are evaluated as balls. Python runs a two-phase Bland simplex at 200 decimal digits, with HiGHS double values recorded as search diagnostics and supported-system audits at 260 digits. The guard digits address dual multipliers as large as `1e67` at the edge; the initial 200-digit residual check was insufficient for a `1e-150` absolute threshold in five x=25 cases, although all their ball certificates already passed. Supported dual systems are then solved **again in balls**. Positivity of all dual coefficients and feasibility of the exact basic primal solution certify both outer bounds and optimality for this fixed-vector LP. These are exact certificates for the chosen dyadic cuts; agreement with ideal eigenvector cuts is a high-precision numerical statement. Printed short decimals round the ball centers; the detailed `CERT` lines retain enclosures, and `CERTIFIED_WIDTH` prints an upper bound rounded outward to twelve significant digits using exact decimal arithmetic.

The minimum eigenvalue in each parity block is independently enclosed with `zst_eigmin`. A rank-one positive-definiteness check on `H-2lambda I+4lambda vv^T/(v^Tv)` verifies minimality: its positivity bounds the negative index of `H-2lambda I` by one, while the enclosed eigenvalue gives one negative direction. This avoids the unstable unpivoted LDL test at x=25. All these checks use only prime-side matrices. The higher spectral quantiles below are QR/Rayleigh numerical estimates, not interval eigenvalue enclosures.

The saturation cutoff minimizes the total log determinant on the scanned integer range `0<=N<=200`, using the two blocks' Cholesky pivots at 1280 bits. It is a sampled argmin, not a proof of a global-in-N minimum. The cutoffs found are:

| x | interior atoms m | N_sat in scan | log det at N_sat (rounded) |
|---|---:|---:|---:|
| 13 | 11 | 56 | -1291.664798 |
| 17 | 15 | 83 | -2327.523807 |
| 19 | 17 | 94 | -2962.401357 |
| 23 | 21 | 123 | -4460.944825 |
| 25 | 23 | 134 | -5328.600491 |

### 4.1 Spectrum at both resolutions

`eps` is the minimum of the two certified block eigenvalues, rounded below; `lambda_m` and `lambda_(m+1)` are numerical estimates from the 1152-bit eigensolve, rounded to six digits. `r_used` is the largest spectral rank appearing in any of the verified optimal LP bases; it describes these certificates and is not asserted minimal.

| x | N | eps | lambda_m | lambda_(m+1) | r_used |
|---:|---:|---:|---:|---:|---:|
| 13 | 56 | 1.95538e-58 | 8.51088e-27 | 2.05492e-24 | 12 |
| 17 | 83 | 1.33448e-79 | 1.59319e-34 | 5.23208e-32 | 16 |
| 19 | 94 | 5.86601e-90 | 2.06928e-38 | 6.92568e-36 | 18 |
| 23 | 123 | 2.73312e-111 | 4.25007e-46 | 1.33887e-43 | 24 |
| 25 | 134 | 1.25554e-121 | 8.15342e-50 | 3.23283e-47 | 26 |
| 13 | 60 | 1.01356e-58 | 7.22103e-27 | 1.67788e-24 | 12 |
| 17 | 60 | 5.61383e-74 | 2.12382e-32 | 4.08226e-30 | 18 |
| 19 | 60 | 1.83173e-79 | 1.22968e-33 | 1.77066e-31 | 20 |
| 23 | 60 | 4.28649e-88 | 2.59386e-34 | 2.06171e-32 | 26 |
| 25 | 60 | 1.07936e-91 | 7.03993e-34 | 8.39927e-32 | 28 |

The `m` smallest eigenvalues by themselves do not describe these certificates: more directions are needed, and their sensitivities are very uneven across positions. At fixed N, `lambda_m` even increases from x=23 to 25 while `eps` continues to decrease.

### 4.2 LP boxes, and the certified bounds

The entries are rounded **LP widths**. Every endpoint has a ball-certified dual bound and a matching ball-certified primal optimum for the fixed-vector relaxation. The twelve-digit outward upper bounds and all coordinates `n=2..x-1`, not only the selected columns here, are printed in the output. `n=6` and `n=12` have true weight zero throughout. The last column changes its coordinate with x.

| x | N | width at n=2 | width at n=6 | width at n=12 | worst width, n=x-1 |
|---:|---:|---:|---:|---:|---:|
| 13 | 56 | 1.192655524e-38 | 4.251260e-30 | 2.328012649e-10 | 2.328012649e-10 |
| 17 | 83 | 1.646086672e-52 | 3.759632e-44 | 2.171886e-28 | 8.288468325e-12 |
| 19 | 94 | 2.080215547e-59 | 4.228656e-51 | 5.769689e-36 | 2.027492338e-12 |
| 23 | 123 | 2.075584280e-73 | 3.656089084e-65 | 1.091347336e-50 | 1.000839753e-13 |
| 25 | 134 | 2.000607387e-80 | 3.364439e-72 | 6.450034e-58 | 2.225924060e-14 |
| 13 | 60 | 1.000472324e-38 | 3.579417e-30 | 2.121317700e-10 | 2.121317700e-10 |
| 17 | 60 | 6.079486546e-50 | 1.293759e-41 | 3.545446e-26 | 1.459510808e-10 |
| 19 | 60 | 1.069682249e-53 | 1.878670e-45 | 6.699063e-31 | 4.152016052e-10 |
| 23 | 60 | 4.470869087e-59 | 5.916416e-51 | 1.894371e-37 | 9.172920091e-9 |
| 25 | 60 | 8.231774550e-61 | 9.668708e-53 | 1.313248e-39 | 4.364656164e-8 |

At x=13, N=20 the new computation reproduces the review's endpoints and widths (`2.984430119e-25` at n=2, `1.252865705e-4` at n=12). At N=40 these become `2.332954265e-36` and `4.249427115e-9`. Thus the old tolerance-limited, nonmonotone table was not a property of positivity.

### 4.3 Rates: the widths do not track eps

Define an endpoint rate by `[log10(value at x=13)-log10(value at x=25)]/12`; the fit column is ordinary least squares on all five x values. These slopes are floating derived statistics, not certified asymptotic laws.

| quantity | saturation: endpoint / five-point fit | fixed N=60: endpoint / five-point fit |
|---|---:|---:|
| eps | 5.26603 / 5.27134 | 2.74772 / 2.69166 |
| lambda_m | 1.91822 / 1.92103 | 0.58425 / 0.54912 |
| width at n=2 | 3.48128 / 3.48145 | 1.84039 / 1.79853 |
| width at n=6 | 3.50847 / 3.50741 | 1.88070 / 1.83799 |
| width at n=12 | 3.96312 / 3.92534 | 2.43402 / 2.35612 |
| worst width at n=x-1 | 0.33496 / 0.33255 | **-0.19278 / -0.20962** |

At saturation the selected fixed coordinates shrink substantially more slowly than eps, and the moving edge is much slower still. At fixed N=60, the edge width grows by a factor about 206 between x=13 and 25. The previously quoted 5.38 uses a wider x range and more fully converged N; it must not be substituted for the 5.26603 measured at these actual log-det minima. Neither the minimal eigenvalue alone nor `lambda_m` alone predicts these widths. L2's weighted, conditioned dual formula is the correct statement.

The widths increase strictly with n in every requested box. This points to location, not to zero/nonzero von Mangoldt weight: the worst position at x=17 is n=16, a prime power with positive true weight. As an atom approaches the edge, the overlap interval in its autocorrelation shortens; at any fixed N its entire matrix tends to zero. The sensitivities of the low eigendirections are correspondingly poorly conditioned near the edge. A vanishing true weight at a composite does not by itself create that mechanism.

### 4.4 Two-coordinate SDP sections (the permitted fallback)

The **full SDP coordinate boxes with all other weights free were not computed**. Instead, for N=20 and 40 the script computes all four support endpoints of each section with only `(2,3)`, `(4,5)`, `(6,7)`, `(8,9)`, `(10,12)` or `(11,12)` allowed to vary. This is the explicitly permitted two-coordinate fallback; other weights are fixed at truth.

Method, independent of the eigenvector LP: Cholesky-whiten `H*` at 200 digits. For the upper endpoint in a chosen coordinate, minimize the convex function `r -> lambda_max(-A-rB)` in double. The reciprocal is the boundary radius of `I+t(A+rB)>=0`. Two test vectors on opposite sides of the scalar minimizer give a rank-two PSD dual: their nonnegative weights are solved at 200 digits so the other coordinate's sensitivity cancels. An interior primal point is chosen at `(1-1e-12)` of the high-precision ray endpoint. Both the primal matrices and the two-vector dual systems are then reconstructed in **1280-bit balls in the original, unwhitened coordinates** and certified. The relative endpoint gaps are below `3.2e-11` (typically about `1e-12`); the selected section widths below have matching inner/outer ten-digit displays.

| N | free pair | projected coordinate | section width (inner/outer agree to shown digits) | full eigenvector-LP width |
|---:|---|---:|---:|---:|
| 20 | 2,3 | 2 | 3.556569160e-34 | 2.984430119e-25 |
| 20 | 2,3 | 3 | 7.418235870e-33 | 1.762261183e-23 |
| 20 | 6,7 | 6 | 3.223418895e-27 | 1.362526363e-17 |
| 20 | 11,12 | 11 | 2.890880148e-13 | 2.665999400e-7 |
| 20 | 11,12 | 12 | 1.407613711e-8 | 1.252865705e-4 |
| 40 | 2,3 | 2 | 1.544802860e-47 | 2.332954265e-36 |
| 40 | 2,3 | 3 | 4.836374734e-46 | 1.66756677e-34 |
| 40 | 6,7 | 6 | 2.315849543e-39 | 7.11364748e-28 |
| 40 | 11,12 | 11 | 2.641558656e-20 | 1.61023177e-13 |
| 40 | 11,12 | 12 | 1.440107066e-13 | 4.249427115e-9 |

These section projections give **lower bounds** on the full SDP widths. The LP gives upper bounds. Their large separation leaves the tightness of the full LP relaxation OPEN; a ratio between a section and an LP is not a proved relaxation gap for the full SDP. Every other two-coordinate endpoint is recorded in the output and `checks/sections_N*.certificates`.

## L5. First recession cutoff at x=13 — PROVED by numerical ball certificates

Atoms are the first `m` positions, `log 2,...,log(m+1)`, in the common window `L=log 13`.

| m | first N with zero recession cone | certificate at previous cutoff |
|---:|---:|---|
| 2 | 2 | positive definite recession matrix at N=1 |
| 3 | 2 | positive definite recession matrix at N=1 |
| 4 | 2 | nontrivial kernel: m>2N+1 at N=1 |
| 5 | 3 | positive definite recession matrix at N=2 |
| 6 | 3 | nontrivial kernel at N=2 |
| 7 | 4 | positive definite recession matrix at N=3 |
| 8 | 4 | nontrivial kernel at N=3 |
| 9 | 5 | positive definite recession matrix at N=4 |
| 10 | 5 | nontrivial kernel at N=4 |
| 11 | 6 | positive definite recession matrix at N=5 |

### 5.1 Construction and exact meaning of the certificates

At each candidate cutoff the double search solves `max t` subject to `T(delta)>=tI`, `tr T(delta)=1`, using an orthonormal basis of the atom span and eigenvector separation cuts. Positive primal values give candidate recession rays. Negative dual values give candidate positive definite matrices orthogonal to the atom span. This normalization detects every **nonzero PSD matrix**. The kernel of `T` is handled separately; imposing only `sum delta=+-1`, as suggested in the brief, would miss every zero-sum recession direction.

The C verifier reconstructs all atom matrices in 1280-bit balls. For a ray it certifies `T(delta)>0` by Cholesky. For a candidate dual `Z0`, it forms the atom Gram matrix `M_ij=tr(T_i T_j)`, solves `M h=(tr(T_i Z0))_i` in balls and certifies

`Z=Z0-sum h_i T_i > 0`.

This defines an exactly orthogonal matrix, not a matrix whose residual is merely small. The successful interval solve proves injectivity of the atom map. Hence a PSD `T(delta)` has `tr(Z T(delta))=0`, forcing `T(delta)=0` and then `delta=0`. Six primal and ten dual certificates pass. Dimension `2N+1` of the Loewner data proves the remaining lower-cutoff kernels exactly. At N=0 the recession cone is plainly nonzero.

### 5.2 All requested cutoffs

Compression makes the recession cones decrease with `N`. The certified lower-cutoff witnesses therefore establish every earlier case; the first zero-cone certificate establishes every later cutoff through `N=40` and beyond. Thus the table settles the entire requested range without treating noisy minimum eigenvalues as exact zero tests. For m=10 and 11 the double dual margins are only about `1.85e-8` and `1.21e-9`; they pass the exact ball projection/Cholesky verification. The results do not assert a universal atom-count threshold, which L1 refutes.
