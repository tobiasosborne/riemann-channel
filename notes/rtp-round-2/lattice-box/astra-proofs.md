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

Even `eps_N -> 0` does not suffice in general nested PSD affine families: take `H*=diag(1,1,1/2,1/3,...)`, and `T(delta)=diag(delta,-delta,0,...)`. The finite minima tend to zero while the feasible interval remains `[-1,1]`. This last example illustrates the missing sensitivity hypothesis; it is not claimed to have the zeta kernel.

### 3.3 What is known for the zeta operator without RH (PROVED with cited input)

The form is closed, semibounded, has the Fourier polynomials as a form core, and its associated operator has compact resolvent. These are Proposition `Hilbert1` and Theorem `thmsmallest` of the supplied source, [Connes–Consani–Moscovici, Sections 3.1–3.2](https://arxiv.org/html/2511.22755v1#S3). In consequence `eps_N` decreases to the **attained** lowest eigenvalue `mu_L`. Under H-POS either `mu_L>0`, which invokes 3.2, or there is a nonzero actual kernel vector. A finite list of positive finite-section eigenvalues proves neither alternative, and does not prove H-POS. At `x=13` the cited `N=120,200` values are `3.48e-59,2.85e-59`, consistent with a positive floor, not evidence for a limit of zero.

The compactness argument can also be seen directly: the archimedean Fourier multiplier grows like `log(2+|t|)`, whereas the pole and the finitely many shifts are bounded. A bounded form-norm set has uniformly small Fourier tails. The map cutting off both position and frequency is compact, so the form-domain embedding into the window `L^2` space is compact.

### 3.4 COMPARISON STEP — theoretical RH implication, no numerical zeros

**H-RH:** the Riemann hypothesis. Under this hypothesis the fixed-window zeta form is strictly positive and, by compact resolvent, satisfies H-GAP. Thus **under RH, the actual fixed-window lattice set is not a singleton**.

Proof. The explicit formula under RH writes the form as a nonnegative sum of `|fhat(gamma)|^2`, with positive multiplicities. For an element of the closed form domain, approximate in form norm by core functions. Positivity of each summand and continuity of each evaluation on window `L^2` show that a null vector would have `fhat(gamma)=0` for every distinct zero ordinate. Its Fourier transform is entire of finite exponential type and bounded on the real line, so a nonzero such transform has `O(T)` zeros in `|z|<=T`, by Jensen's formula and the exponential-type bound (center Jensen at a point where the transform is nonzero).

There are more than linearly many **distinct** zeta ordinates under RH; multiplicities must not be overlooked here. Indeed `N(T)~T log T/(2 pi)` and Littlewood's RH bound `S(T)=O(log T/log log T)` bound every jump, hence every multiplicity near height `T`, by `O(log T/log log T)`. Consequently the number of distinct ordinates up to `T` is at least a constant times `T log log T`. The two counting inputs and the RH bound are recorded in [Carneiro–Chirre, Section 1.1, equations (1.2)–(1.3)](https://arxiv.org/html/1702.04099#S1.SS1). This contradicts the exponential-type zero count unless `f=0`. Thus the lowest attained eigenvalue is strictly positive. No zero location or RH assumption enters any numerical matrix or certificate in this lane.

**Reading.** Positivity at a fixed window can pin weights to an exceptionally small neighborhood, but exact recovery is not a consequence of RH; RH implies a nonzero neighborhood instead. The general H-PIN theorem is valid for any family of window forms, and is incompatible with H-GAP at a fixed window. For the specific fixed windows here, unconditional infinite-dimensional positivity and a prime-side quantitative lower bound remain unproved in this lane.
