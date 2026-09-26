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

Extend `f` by zero outside `[0,L]` and put `C_f(y)=int conjugate(f(u)) f(u+y) du`. The quadratic atom evaluation is `q_f(y)=2 Re C_f(y)` and `T_k[f]=-q_f(y_k)`. In the centered Fourier phase convention used for the real Loewner matrix this gives exactly the formula sheet's diagonal `-2(1-t_k)cos(2 pi n t_k)` and off-diagonal `(sin(2 pi n t_k)-sin(2 pi j t_k))/(pi(n-j))`. An uncentered complex Fourier basis differs by a diagonal unitary phase; this does not affect positivity or the cone. In particular `||T_k||<=2` and `T_L=0`.

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
