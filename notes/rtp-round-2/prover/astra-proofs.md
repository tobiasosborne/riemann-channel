# RTP-2, lane P: proofs and corrections

Author: `codex:gpt-6-astra`, 2026-09-26.

No RH assumption; no zero ordinates are used as data. This is a research deliverable, not a registration. External inputs remain named hypotheses pending byte-citation. All paths and line numbers refer to the copies read in this session. Only this lane's deliverable, progress file and checks are written.

## Correction ledger

1. **P1 — SHARPENED.** A Gaussian log determinant requires positive definiteness. `log(d/s)` is the loss of determinant relative to the maximum determinant, not a gain of the true determinant. The odd block at `N=0` has an affine Schur complement, not a strictly concave quadratic. Intervals may be empty or singletons; a joint log-det maximiser requires a positive definite extension.
2. **P2 — REFUTED as requested.** The proposed archimedean set contains logarithms of *all* algebraic numbers, including all `log q`. Thus the proposed `L_S` is independent of `S`, and no numerical prime-coordinate projection annihilating the archimedean span exists. Baker independence within the logarithmic subspace does not repair this overlap. A point mass is not a test function for the explicit-formula distribution: its self-convolution contains a mass at zero, and prime evaluation and the archimedean diagonal are undefined. A labelled discrete model must not be called the Weil form.
3. **P3 — SHARPENED.** Semialgebraicity applies to a finite parameter space and every fixed finite marginal image, not literally to an infinite sequence of state coordinates in a Euclidean space. Auxiliary C*-algebra dimension and matrix bond dimension differ. Individual energies need not be algebraic; finite semialgebraic optima over algebraic data are algebraic.
4. **P4 — conditional conclusion.** Numerical bounds require numerical constants in both the elimination and transcendence hypotheses; big-O citations alone are insufficient. A priority claim (“first”) requires a literature audit and is not asserted here. Irrationality alone cannot exclude optima over the real algebraic numbers. The explicit CAD envelope in P4 is derived from determinant-size estimates; its constants are not guessed from a big-O theorem.
5. **Source inventory correction.** A local Tarski–Seidenberg/CAD source does exist: Coste (2002), `refs/src/coste-2002/paper.txt`. The requested H-TS and H-BPR labels are retained. H-LOG2 was located and checked online; it remains to be byte-cited locally.
6. **Source convention correction.** The present CCM copy places `bombtest` at `refs/src/2511.22755/mc2arXiv.tex:465–467`, not lines 385–388 of the briefs. The formula itself is unchanged.

## P1. Bordering and the exact Loewner interval — PROVED / SHARPENED

### Theorem P1.1 (unstructured bordering)

Let `G=G*>0`, `c` a column and `d` real. Set

\[
 B=\begin{pmatrix}G&c\\c^*&d\end{pmatrix},\qquad s=d-c^*G^{-1}c.
\]

Then `B>=0` iff `s>=0`, `B>0` iff `s>0`, and `det B=det G·s`. For prescribed `d>0`, the unique determinant maximiser among PSD completions is `c=0`. On positive definite completions

\[
 \Delta I=\log\frac{d}{s}
 =\log\det\operatorname{diag}(G,d)-\log\det B\ge0.
\]

It equals `2I(X;Y)` for a real Gaussian of covariance `B`, and `I(Z;W)` for a proper (circular) complex Gaussian of covariance `B`. Natural logarithms give nats.

**Proof.**

1. **Congruence.** Multiply on the left by `L=[[I,0],[-c*G^{-1},1]]` and on the right by `L*`. Direct multiplication gives `LBL*=diag(G,s)`. The matrix `L` is invertible with determinant one. Congruence preserves positive (semi)definiteness, and taking determinants proves all three assertions.
2. **Maximum.** `c*G^{-1}c=||G^{-1/2}c||²>=0`, with equality exactly at zero. Thus `s<=d`, with equality exactly at zero; multiplying by `det G>0` proves uniqueness. If `d=0` the only feasible column is zero, the completion is singular, and the logarithmic ratio `0/0` is undefined. If `d<0` there is no PSD completion.
3. **Real information.** A nonsingular real Gaussian in dimension `r` with covariance `A` has entropy `(r/2)log(2πe)+(1/2)log det A`, obtained by integrating its density. Subtracting joint entropy from the sum of marginal entropies cancels the constants and gives `I=(1/2)log(det G·d/det B)=(1/2)log(d/s)`. Equivalently, the conditional variance of `Y` given `X` is `s`.
4. **Complex information.** The proper complex Gaussian density is `(π^r det A)^{-1}exp(-z*A^{-1}z)`, so its entropy is `r log(πe)+log det A`. The same subtraction gives `I=log(d/s)`. Identifying it with a real Gaussian of twice the dimension yields the same result. For `s=0<d` the conditional scalar is deterministic but its marginal is nondegenerate, so mutual information is infinite (joint measure singular relative to the product); the formula holds by the extended value `+∞`. It is not a formula for finite differential entropies at a singular covariance. ∎

For a new block `D>0`, the same congruence gives `S=D-C*G^{-1}C` and `det B=det G det S`. In the PSD region put `P=D^{-1/2}C*G^{-1}CD^{-1/2}`; `0<=P<=I`, so `det S=det D prod(1-p_i)<=det D`, with equality iff `C=0`. Information is additive when the covariance decomposes into independent parity blocks, not for an arbitrary orthogonal splitting that leaves cross terms.

### Theorem P1.2 (fully normalised window bordering)

Use the formula sheet `notes/zeta-spectral-triples/plan.md:44–60,111–120`: `L=2 log λ`, `x=log(λu)`, `V_n(u)=L^{-1/2}exp(2πin x/L)`,

\[
 T_{nm}=\frac{b_n-b_m}{n-m}\ (n\ne m),\quad T_{nn}=a_n,
 \quad a_{-n}=a_n\in\mathbb R,\quad b_{-n}=-b_n\in\mathbb R.
\]

In particular `b_0=0`. Choose `e_0=V_0`, `e_i=(V_i+V_{-i})/√2`, `o_i=(V_i-V_{-i})/√2`. These are orthonormal in the underlying window `L²`, including the unscaled `e_0`. Although `o_i` as functions are imaginary, their Gram entries are real; the real symmetric matrices are the covariances meant in P1.1. One can multiply every odd vector by `-i` to obtain a real sine basis without changing either diagonal parity block.

Fix `N>=1`, let `j=N+1`, and assume both old blocks `G_e` (size `N+1`) and `G_o` (size `N`) are positive definite. Fix `a=a_j`, allow `b=b_j` to vary. Then

\[
 c_e(b)=u_e+bw_e,\quad d_e(b)=a+b/j,
 \qquad c_o(b)=u_o+bw_o,\quad d_o(b)=a-b/j,
\]

where the **exact columns in these orthonormal bases** are

\[
\begin{aligned}
 &(u_e)_0=0,\quad (w_e)_0=\sqrt2/j,\\
 &(u_e)_i=b_i\left(\frac1{i-j}+\frac1{i+j}\right)
            =\frac{2ib_i}{i^2-j^2},\quad
 (w_e)_i=-\frac1{i-j}+\frac1{i+j}=\frac{-2j}{i^2-j^2},\\
 &(u_o)_i=b_i\left(\frac1{i-j}-\frac1{i+j}\right)
            =\frac{2jb_i}{i^2-j^2},\quad
 (w_o)_i=-\frac1{i-j}-\frac1{i+j}=\frac{-2i}{i^2-j^2}
 \quad(1\le i\le N).
\end{aligned}
\]

Choose any reference value `b_ref` (no assumption that it is the arithmetic truth), put `β=b-b_ref`, `c_t=c_t(b_ref)`, `s_{t,0}=a+σ_t b_ref/j-c_tᵀG_t^{-1}c_t`, with `σ_e=+1`, `σ_o=-1`. Define

\[
 C_t=w_t^TG_t^{-1}w_t>0,\quad
 \ell_t=\frac{\sigma_t}{j}-2w_t^TG_t^{-1}c_t,\quad
 \beta_t^*=\frac{\ell_t}{2C_t},\quad
 s_t^*=s_{t,0}+\frac{\ell_t^2}{4C_t}.
\]

Then

\[
 s_t(\beta)=s_{t,0}+\ell_t\beta-C_t\beta^2
 =s_t^*-C_t(\beta-\beta_t^*)^2.                 \tag{P1.1}
\]

If `s_t*<0` the block is never PSD. If `s_t*=0` its feasible set is the singleton `β_t*`. If `s_t*>0` its feasible interval is

\[
 I_t=[\beta_t^*-r_t,\beta_t^*+r_t],\qquad r_t=\sqrt{s_t^*/C_t}.
\]

Its centre uniquely maximises that block determinant. At either endpoint, the bordered block is singular of nullity one. The full feasible set is `J=I_e∩I_o`.

**Proof.**

1. Reflection commutes with `T`, so the even–odd cross entries vanish. Adding the entries at `(i,j)` and `(i,-j)` yields the even block, subtracting them yields the odd block. For example `T_{i,-j}=(b_i+b)/(i+j)` and `T_{j,-j}=b/j`. The `0,j` entry becomes `√2 b/j`. Collecting the coefficients of `b` gives exactly the displayed `u,w,d`, including every sign.
2. Substitute `c_t+βw_t` and `d_t+σ_tβ/j` into the Schur complement. The mixed quadratic term is `-2βw_tᵀG_t^{-1}c_t`; this fixes the minus sign in `ℓ_t`. `w_e` is nonzero by its zeroth entry; `w_o` is nonzero by any entry with `i>=1`. Positive definiteness of the inverse proves `C_t>0`. Completing the square proves (P1.1).
3. P1.1 converts PSD to the scalar inequality `s_t>=0`, giving the three cases. At a root the congruence has precisely one zero scalar and a positive definite old block. The kernel is generated by `(-G_t^{-1}c_t(b),1)`. The determinant is the positive constant `det G_t` times `s_t`, proving the maximum assertion. Both blocks must be PSD, hence intersection. ∎

**Initial step `N=0`.** `G_e=[a_0]>0`, `c_e=√2 b`, `s_e=a_1+b-2b²/a_0`; the new odd block is the scalar `s_o=a_1-b` because the old odd space is empty. Its feasible set is a half-line and `C_o=0`. Thus the two strictly concave quadratic assertion must explicitly start at `N=1`. No positivity of the old arithmetic window or its enlargement is inferred from RH.

### Theorem P1.3 (necessary and sufficient midpoint condition)

Suppose `s_e*,s_o*>0` and

\[
 A=\max(\beta_e^*-r_e,\beta_o^*-r_o)
 <B=\min(\beta_e^*+r_e,\beta_o^*+r_o),\qquad m=(A+B)/2.
\]

The joint determinant has a unique maximum `β_ME∈(A,B)`. It equals the centre `m` **if and only if** the following explicit condition on the six quadratic parameters holds:

\[
 C_e(m-\beta_e^*)[s_o^*-C_o(m-\beta_o^*)^2]
 +C_o(m-\beta_o^*)[s_e^*-C_e(m-\beta_e^*)^2]=0.       \tag{P1.2}
\]

Here `m` is the explicitly displayed max/min expression in those parameters. Equivalently,
`C_e(m-β_e*)/s_e(m)+C_o(m-β_o*)/s_o(m)=0`.

**Proof.**

1. On `(A,B)` both Schur complements are strictly positive. At each endpoint at least one is zero, so `s_e s_o=0` there and is positive inside. A continuous product attains a positive maximum in the interior.
2. For either block `(log s_t)''=-2C_t/s_t-(s_t'/s_t)²<0`. Thus `log s_e+log s_o` is strictly concave. Its stationary point is unique and is the unique product maximum.
3. Its derivative is `-2[C_e(β-β_e*)/s_e(β)+C_o(β-β_o*)/s_o(β)]`. Substitution of `m` and multiplication by the positive denominators gives exactly (P1.2), in both directions. This is an exact condition, not a claim that distinct centres always force an offset. If `A=B`, the sole feasible point is trivially the determinant maximiser but every determinant is zero and log-det is undefined. If `A>B`, no feasible completion exists. ∎

### Exact rational example (old block sizes `2×2` and `1×1`)

Take `N=1`, `a_0=a_1=a_2=1`, `b_1=0`, and `b_2=b`. Thus `G_e=I_2`, `G_o=[1]` and

\[
 c_e=(b/\sqrt2,4b/3)^T,\quad c_o=2b/3,\quad
 s_e=1+b/2-41b^2/18,\quad s_o=1-b/2-4b^2/9.
\]

All Loewner `a,b` data are rational. If fully rational matrices are desired, use `e_i/√2` for `i>=1` (only for this display):

\[
 \widehat E(b)=\begin{pmatrix}1&0&b/2\\0&1/2&2b/3\\b/2&2b/3&1/2+b/4\end{pmatrix},
 \quad O(b)=\begin{pmatrix}1&2b/3\\2b/3&1-b/2\end{pmatrix}.
\]

The even Schur complement is then `s_e/2`, a constant rescaling that changes neither the feasible interval nor its maximiser. The intervals in the orthonormal convention are

\[
 I_e=\left[\frac{9-3\sqrt{337}}{82},\frac{9+3\sqrt{337}}{82}\right],\quad
 I_o=\left[\frac{-9-3\sqrt{73}}{16},\frac{-9+3\sqrt{73}}{16}\right].
\]

Both roots of `s_e` lie in `(-1,1)` (`s_e(0)>0`, `s_e(±1)<0`). At an even endpoint use `b²=18/41+9b/41` to obtain `s_o=33/41-49b/82>17/82>0`. Concavity then gives `I_e⊂int I_o`. Hence `J=I_e`, its midpoint is `9/82`, and its half-width is `3√337/82`. But `(log s_e+log s_o)'(0)=1/2-1/2=0`. The theorem gives

\[
 b_{ME}=0,\qquad b_{ME}-m=-9/82,\qquad
 \frac{b_{ME}-m}{(B-A)/2}=-3/\sqrt{337}\ne0.
\]

This is a kinematic Loewner counterexample to a universal midpoint claim, not a claim that these rational data equal an arithmetic zeta window. The exact arithmetic is reproduced in `checks/p1_p2.py`.

### Theorem P1.4 (the zero-column obstruction)

In the above Loewner family the two old-to-new parity columns vanish simultaneously **if and only if** `b_1=⋯=b_{N+1}=0`; in fact the even column alone enforces this.

**Proof.** `c_{e,0}=√2 b_j/j=0` forces `b_j=0`. For `1<=i<=N`, the remaining entry is `2i b_i/(i²-j²)`. Its prefactor is nonzero, so every `b_i=0`. Conversely the displayed formulas make both columns zero if all these data vanish. This also covers `N=0`. For the unblocked addition of the pair `V_±j`, changing to parity bases is invertible, so vanishing of the full old-to-new block is equivalent. The statement is not that an isolated odd column can never vanish, nor that fixing `a_j` fixes both new parity diagonals while `b_j` varies. ∎

**Relation to the extension disc.** A Toeplitz column `u(x)=bar(x)e_0+w` is a complex affine section of P1.1's ellipsoid; completing its square gives `c_K=-overline((W_K^{-1}w)_0)/(W_K^{-1})_{00}` in `report/sections/08g_weil_window_extension.tex:86–96,111–120`. The Loewner problem instead has one real parameter shared by two columns *and* two affine diagonals. The P1 proof does not establish all Toeplitz prediction/atom claims of `prop:extension-disc`, so that row is not upgraded here. The structured information deficit is `log[s_e(β_ME)s_o(β_ME)/(s_e(β_true)s_o(β_true))]>=0` when the true completion is positive definite; it need not be a mutual information with fixed marginals because these diagonals vary.

## P2. What Baker does and does not grade

### Hypothesis H-BAKER (named external input)

If `λ_1,…,λ_r` are logarithms of nonzero algebraic numbers, linearly independent over `Q`, then `1,λ_1,…,λ_r` are linearly independent over `Q-bar`. This is the inhomogeneous linear-independence consequence of Baker's theorem (combining independence of algebraic logarithms with transcendence of every nonzero algebraic linear form). Standard reference: A. Baker, *Transcendental Number Theory* (1975), Chapter 2, linear forms in logarithms; theorem number **from memory, to be byte-cited**. We use only this stated consequence, not algebraic independence of logarithms or independence from `γ` and zeta values.

### Proposition P2.1 — REFUTED (the proposed language and numerical blindness)

Let `A` be the actual numbers named in `notes/metric-tomography/finite-prime-language.md:83–86`, including all logarithms of algebraic numbers. Then

\[
 L_S=\operatorname{span}_{\overline{\mathbb Q}}(1,A)=L_\varnothing
 \quad\text{for every finite }S.
\]

In particular `log q∈L_S` even if `q∉S`. No `Q-bar`-linear map on `L_S` can both give `log p` coordinate one and give every archimedean generator coordinate zero.

**Proof.** For every prime `p`, the number `p` is algebraic, so `log p∈A`. Adding these generators does not enlarge the span. For the second claim the same element `log p` would have to map both to one and zero. ∎

This explicitly refutes the exclusion table at `finite-prime-language.md:116` and the implication at lines 151–152. Restricting the logarithms in `A` would not by itself settle independence from `γ` and all rational polygamma values. For example, `ψ(1)=-γ` and `ψ(1/2)=-γ-2 log 2` already put `log 2` in the span of the digamma values and `γ`. Thus even deleting the explicit “logs of algebraic numbers” does not repair this particular archimedean list. There is also a definitional inconsistency: the list at lines 85–86 does not explicitly contain `log π`, whereas lines 108–119 treat it as included. `π∈A` does not imply `log π∈A` in a vector space. We do not assert that it is outside the span; its claimed inclusion does not follow from the definition.

### Proposition P2.2 — PROVED-conditional (H-BAKER): the genuine logarithmic direct sum

Define the smaller numerical space

\[
 \mathcal B_S=\overline{\mathbb Q}\,1\ \oplus\
 \overline{\mathbb Q}\,i\pi\ \oplus\
 \bigoplus_{p\in S}\overline{\mathbb Q}\log p.
                                                        \tag{P2.1}
\]

The indicated sum is direct. These spaces form an increasing filtration, and `B_S∩B_T=B_{S∩T}`. Each element of their union has a unique finite prime-coordinate vector. An element of `B_S` is **numerically q-blind** for `q∉S`, meaning its `log q` coordinate in `B_{S∪{q}}` is zero. This notion is narrower than any assertion about detecting zeros.

**Proof.**

1. Suppose `q_0 iπ+Σ q_p log p=0` with rational coefficients. Taking imaginary parts gives `q_0=0`. Clearing denominators in the remaining equation and exponentiating gives `prod p^{m_p}=1`, with integers `m_p`. Moving negative exponents to the other side and unique prime factorisation imply all `m_p=0`. Hence `iπ,log p` are `Q`-independent logarithms of the algebraic numbers `-1,p` (branch `log(-1)=iπ`).
2. H-BAKER supplies independence after adjoining `1` and extending scalars to `Q-bar`. Uniqueness of coordinates follows. Apply this to the finite union `S∪T` to prove the intersection identity and the zero-coordinate claim. ∎

A map from a full Weil value to these coordinates is **not** supplied by this theorem. It exists for its prime remainder under the next proposition. A formal external sum `A_formal⊕⊕_p Q-bar·[p]` has labels by construction, but evaluation in `C` is not injective: the archimedean symbol for `log p` and `[p]` have identical numerical value. These are provenance labels, not Baker coordinates of a number.

### Proposition P2.3 — PROVED: why the point-mass theorem is undefined

Use the CCM normalisation: if `g` is the logarithmic representative after the half-density change, set

\[
 F(y)=(g^**g)(y)=\int_{\mathbb R}\overline{g(x)}g(x+y)\,dx,
 \quad g^*(x)=\overline{g(-x)}.
\]

This is the unitary version of the notebook's Mellin involution; the change `F(u)=u^{1/2}f(u)` is recorded in `refs/src/2511.22755/mc2arXiv.tex:430–450`. Then, with `c_R=log(4π)+γ` and `ρ(y)=e^{y/2}/(e^y-e^{-y})`,

\[
\begin{aligned}
 W_{0,2}(F)&=\int_{\mathbb R}2\cosh(y/2)F(y)\,dy,\\
 W_p(F)&=(\log p)\sum_{k\ge1}p^{-k/2}\{F(k\log p)+F(-k\log p)\},\\
 W_{\mathbb R}(F)&=c_R F(0)+\int_0^\infty
 [F(y)+F(-y)-2e^{-y/2}F(0)]\rho(y)\,dy,\\
 Q(g)&=W_{0,2}(F)-W_{\mathbb R}(F)-\sum_pW_p(F).
                                                        \tag{P2.2}
\end{aligned}
\]

These formulas are direct changes of variables in CCM `:445–470`, not a new normalisation or a numerical implementation.

**Proof of the obstruction.**

1. For a nonzero finitely supported measure `μ=Σ c_n δ_{log n}`, combine coincident atoms first. Its convolution `μ* * μ` has at zero the positive mass `Σ|c_n|²`. Neither its value `F(0)` nor point evaluation at a coincident prime atom is defined as a function evaluation. Pairing an explicit-formula distribution with such a distribution has not been defined. The CCM domain is a function class (`:400–428`), not this measure class.
2. At a nonzero rational displacement `D=log r`, `r>1` rational,

\[
 2\cosh(D/2)=\sqrt r+1/\sqrt r\in\overline{\mathbb Q},\qquad
 \rho(D)=\frac{\sqrt r}{r-r^{-1}}\in\overline{\mathbb Q}.
\]

There is **no extra factor of `D`** in either kernel. These algebraic off-diagonal kernel values do not define the diagonal or a product of coincident delta distributions. The pole, being a smooth kernel, can be paired with a measure; the whole Weil distribution cannot thereby be paired with it.
3. The singularity is substantive. Choose a real even `φ∈C_c^∞(-1,1)` with `||φ||₂=1` and put `φ_δ(x)=δ^{-1/2}φ(x/δ)`. Write `R=φ* * φ`, so `R_δ(y)=R(y/δ)` and `R_δ(0)=1`. For one atom regularised by `φ_δ`, the interval `2δ<y<1` contributes
`-2∫e^{-y/2}ρ(y)dy=log δ+O(1)` to `W_R`. On `0<y<2δ`, substitution `y=δt` and the smoothness `R(t)-1=O(t)` bound the regularised contribution uniformly; the tail past 1 is bounded. The pole is `O(δ)` and the prime terms vanish when `2δ<log 2`. Thus `Q(φ_δ)=log(1/δ)+O(1)→+∞`. For finitely many distinct translates, the diagonal coefficient becomes `Σ|c_n|²`; the other archimedean peaks are away from zero and are bounded, as are the finitely many admissible prime terms. There is no finite canonical point-mass value supplied by this limiting procedure. ∎

A chosen subtraction of this divergence, or a chosen finite value for a formal diagonal, would define an additional renormalised model. Its arithmetic would depend on that prescription. We do not silently substitute such a model for `W`.

### Theorem P2.4 — SHARPENED / PROVED-conditional (H-BAKER only for uniqueness): the exact prime remainder on admissible bumps

Let `M` be a finite set of distinct `S`-smooth positive integers, `c_n∈Q-bar`, and `φ` a real even compactly supported smooth function with `||φ||₂=1`. Translate and scale it as above and set

\[
 g_\delta(x)=\sum_{n\in M}c_n\phi_\delta(x-\log n),\qquad
 A_p(c)=\sum_{\substack{m,n\in M\ n/m=p^k,\ k\ge1}}
 \frac{\overline{c_m}c_n+c_m\overline{c_n}}{p^{k/2}}.
                                                        \tag{P2.3}
\]

Choose `δ>0` so that every peak of `F=g_δ* * g_δ`, supported within `2δ` of `log(n/m)`, meets a signed prime-power logarithm only when its centre is that logarithm; also ensure distinct centres are separated by more than `2δ`. Such a `δ` exists because there are finitely many ratio centres, finitely many prime powers in any fixed bounded neighbourhood of them, and positive distances between distinct points.

Then the actual finite prime remainder satisfies

\[
 R_{\rm fin}(g_\delta):=Q(g_\delta)-W_{0,2}(F)+W_\mathbb R(F)
       =-\sum_{p\in S}A_p(c)\log p\in\mathcal B_S.       \tag{P2.4}
\]

Its `p`-coordinate is **`-A_p(c)`** in the sign convention `Ψ=W02-WR-ΣWp`, whereas `Wp` has coordinate `+A_p(c)`. The support of this coordinate vector is the active prime content; it is contained in `S` and may be smaller by cancellation. It agrees with the arithmetic prime-content filtration of `metric-as-state.md:73–89` for the finite-place remainder, not with the uncorrected assertion at lines 66–71 that the restriction “contains no zeros”.

**Proof.**

1. Expanding the convolution gives `F(y)=Σ_{m,n}bar(c_m)c_n R_δ(y-log(n/m))`. At `y=k log p`, admissibility kills every summand except those with `n/m=p^k`, and each surviving autocorrelation factor equals one. At `-k log p` the conjugate terms occur. Therefore the coefficient of `log p` in (P2.2) is exactly (P2.3).
2. A prime power ratio of `S`-smooth integers has its prime in `S`, by unique factorisation. Algebraic numbers are closed under conjugation and adjoining square roots, so `A_p(c)` is algebraic. Summing (P2.2) proves (P2.4); P2.2 makes the coefficients unique.
3. If the prime comb weights are replaced by independent real parameters `t_p` with the pole and archimedean terms held fixed, the value on this family is `W02-WR-Σ A_p(c)t_p`, so every derivative with respect to `t_q`, `q∉S`, is zero. This is **operational blindness** to foreign comb weights. In particular the prime remainder is also numerically q-blind in (P2.1). Neither assertion follows merely from full values lying in the original `L_S`. ∎

**Whole-value membership: exact hypotheses, not a blanket assertion.** Let `A_0⊂C` and put `U=span_Qbar(1,iπ,A_0)`. If a class of admissible test functions has algebraic local coefficients, no foreign local terms, and `W02-WR∈U`, then `Q(g)∈U+Σ_{p∈S}Q-bar log p`. Its local terms are numerical prime coordinates **only if** `U∩span_Qbar{log p:p prime}={0}` (or the corresponding finite-union version). This intersection hypothesis is not H-BAKER and is false for the `A` in the question. Without it, membership still holds but the coordinates need not be recoverable.

For the notebook's bumps, membership of the archimedean integrals in its named `A` is **OPEN / unestablished**, as is algebraicity of the bump's exponential moment. For a real even bump the pole between translates at displacement `D` is `2 cosh(D/2)|∫φ_δ(x)e^{x/2}dx|²`; only the `2 cosh` factor is algebraic at a rational ratio. The diagonal contains `(log(4π)+γ)F(0)` **and** the integral in (P2.2); normalising `F(0)` does not evaluate that integral. The given exponential bump has no reduction to rational-argument polygamma values here. The Fourier-window formula itself involves `ψ(1/4-iπn/L)` and a Lerch function, not just rational arguments (`notes/zeta-spectral-triples/plan.md:84–107`). There is therefore no claimed nonzero point-mass class on which the requested whole-value theorem holds. The rigorous replacement on genuine smooth tests is (P2.4).

**Other language corrections.** A finite Euler product at a rational argument is algebraic when defined. A Dirichlet polynomial at an arbitrary algebraic irrational argument need not have algebraic terms; a `Q-bar` vector space is not closed under exponentiation, multiplication, reciprocals, or arbitrary limits. The sweeping inclusion at `finite-prime-language.md:105–110` has not been proved by listing generators. Gauss's digamma formula may introduce logarithms of algebraic units as well as rational primes. None of these defects affects the finite matrix positivity theorem `thm:weil-positivity-finite`, which does not licence evaluating the analytic Weil distribution on delta functions.

## P3. FNW exclusion in semialgebraic form — PROVED-conditional (H-TS)

### Hypothesis H-TS and source status

**H-TS.** Over every real closed field, first-order formulas in the ordered-ring language admit quantifier elimination without adjoining coefficients. In particular a coordinate projection of a semialgebraic set defined over a real closed subfield `F⊂R` is semialgebraic over `F`.

Standard references: A. Tarski, *A Decision Method for Elementary Algebra and Geometry* (1951); A. Seidenberg, “A new decision method for elementary algebra” (1954); Basu–Pollack–Roy, *Algorithms in Real Algebraic Geometry*, second edition (2006), quantifier-elimination theorem (number **from memory, to be byte-cited**). Contrary to the brief's source inventory, there is a relevant local source: M. Coste (2002), `refs/src/coste-2002/paper.txt:173–175` states the projection theorem (Theorem 2.3), and `:248–250` states the first-order version (Theorem 2.6). We retain H-TS for the exact coefficient-preserving real-closed-field formulation requested here; the scanned local text is not a clean byte-citation of every part of that formulation.

### Lemma P3.1 (endpoints over a real closed subfield)

Assume H-TS. If `Y⊂R` is a nonempty semialgebraic set over a real closed subfield `F`, every finite boundary point of `Y`, and hence every finite infimum or supremum, belongs to `F`.

**Proof.**

1. After quantifier elimination, `Y` is a Boolean combination of finitely many sign conditions `P_i(t) ⋈ 0`, with `P_i∈F[t]`. Remove zero polynomials (their sign conditions are constant).
2. Every real root of each `P_i` belongs to `F`: a real closed field has no proper algebraic ordered extension, and adjoining such a root inside `R` would be one. The union `Z` of these root sets is finite.
3. On every component of `R\Z` all the polynomials have constant sign by continuity and the intermediate value theorem. Thus membership in `Y` is constant there, and no point of that open component is a boundary point. Consequently `∂Y⊂Z⊂F`. A finite infimum of a nonempty set is a boundary point (whether or not attained), as is a finite supremum. ∎

### Theorem P3.2 (finite C*-auxiliary algebra, explicit compact parameters)

Fix physical dimension `q`, interaction range `ℓ`, and Hermitian local interaction `h∈M_{q^ℓ}` with real algebraic entries. Write `F=Q-bar∩R`. Define `F_d^alg` to be the translation-invariant C*-finitely correlated states generated by a finite-dimensional complex C*-algebra of **complex vector-space dimension** at most `d`.

There is a finite union of compact semialgebraic parameter spaces over `Q` whose state image is exactly `F_d^alg`; each fixed finite marginal image is compact and semialgebraic over `Q`. Energy is a polynomial over `F` on each parameter space, and

\[
 e_d^{alg}=\min_{\omega\in F_d^{alg}}\omega(h)\in F.       \tag{P3.1}
\]

For the usual **matrix bond dimension** `r`, let `F_r^mat` instead allow auxiliary algebra `M_r(C)` (and smaller matrix algebras). The same statements hold for `e_r^mat`. The dimension of `M_r` as an algebra is `r²`, not `r`.

**Proof.**

1. **Finite list of algebra types.** Every finite-dimensional complex C*-algebra is *-isomorphic to

\[
 \mathcal C=\bigoplus_{a=1}^v M_{n_a}(\mathbb C),\qquad
 m=\dim_\mathbb C\mathcal C=\sum_a n_a^2.
\]

For `m<=d` there are finitely many integer tuples; order the `n_a` to avoid redundant permutations. Fix standard matrix units in each block. This turns the “some algebra of dimension at most d” quantifier into a **finite union**, not a quantifier over unspecified multiplications.

2. **Generating map.** Write the completely positive map `E:M_q⊗C→C` as blocks `E_{ab}:M_{q n_b}→M_{n_a}`. Its Choi matrix

\[
 J_{ab}=\sum_{u,v=1}^{q n_b}|u\rangle\langle v|\otimes
                 E_{ab}(|u\rangle\langle v|)
\]

is Hermitian of size `q n_b n_a`. Use its diagonal real entries and off-diagonal real and imaginary parts as independent real coordinates. Complete positivity is exactly `J_{ab}>=0` for all `a,b`. Indeed a spectral decomposition of `J_{ab}` reshaped into matrices supplies Kraus operators; conversely a Kraus expression gives a sum of vector outer products. A map between direct sums is CP iff each input/output component is CP. A Hermitian matrix is PSD iff **all principal minors** are nonnegative, giving polynomial inequalities over `Q`. To justify the converse of this last criterion, `det(tI+J)` has as coefficients sums of principal minors; if these are nonnegative, it is positive for every `t>0`, so `J` has no negative eigenvalue. Hermiticity is already imposed by coordinates.

3. **Unitality and boundary state.** Require

\[
 \sum_b E_{ab}(I_q\otimes I_{n_b})=I_{n_a}\quad(\forall a).
                                                        \tag{P3.2}
\]

These are `m` real linear equations in the Choi coordinates (each equality is Hermitian). Choose Hermitian densities `ρ_a>=0`, impose `Σ_a tr ρ_a=1`, and require

\[
 \sum_a E_{ab,1}^{\dagger}(\rho_a)=\rho_b,\qquad
 E_{ab,1}(X)=E_{ab}(I_q\otimes X).                       \tag{P3.3}
\]

Adjoints use the ordinary matrix trace. These are `m` real polynomial equations of total degree at most two, bilinear in `ρ,J` minus a linear term. Density positivity is again all principal minors. No faithful-density, injectivity, primitivity, purity, or exact-rank restriction is imposed. Including degenerate boundaries is necessary for a compact class.

4. **The generated state and its energy.** Put `E_A(X)=E(A⊗X)` and `ρ(X)=Σ_a tr(ρ_a X_a)`. Define

\[
 \omega(A_1\otimes\cdots\otimes A_t)
      =\rho\big(E_{A_1}\circ\cdots\circ E_{A_t}(1_\mathcal C)\big).
                                                        \tag{P3.4}
\]

Iterating `id⊗E` gives a CP map on the full local matrix algebra, so composing with `ρ` proves positivity for **all** positive local observables. Unitality gives normalisation and consistency on the right; (P3.3) gives consistency on the left and translation invariance. The compatible local states define a state on the infinite chain. Conversely this is precisely a C*-FCS presentation, so no further hidden constraints are needed. Expanding a range-`ℓ` observable in matrix units makes (P3.4) a polynomial, linear in `ρ` and degree `ℓ` in `J`; the total degree is at most `ℓ+1`. With algebraic `h`, its energy polynomial has coefficients in `F`. Its fixed `t`-site marginal is a polynomial map to a finite-dimensional real matrix space. H-TS therefore makes each marginal image semialgebraic over the same field.

5. **Compactness and gauge.** Take the trace of (P3.2). With the Choi convention above, `Σ_b tr J_{ab}=n_a`. Each positive Choi block therefore has bounded trace and bounded entries (`|J_uv|²<=J_uu J_vv`). The densities have total trace one and are bounded as well. All the constraints are closed, so the finite-dimensional parameter space is compact. It is nonempty: product-state channels give examples. We have chosen the **unital CP presentation in standard C*-matrix units with a trace-one positive boundary functional**. This removes the noncompact similarity freedom of arbitrary raw tensor presentations. Residual blockwise unitary changes and Kraus decompositions need not be fixed uniquely or divided out; the Choi representation avoids Kraus redundancy, and residual unitary freedom is compact. No gauge requiring a strictly positive `ρ` is used.

6. **State-space compactness and attainment.** Each local expectation is polynomial and continuous in the parameters. The state image is consequently compact for the topology of all local expectations (the weak-* topology on states). A finite union over algebra types stays compact. The energy is a continuous local expectation, so it attains its minimum. Strictly speaking, this infinite-dimensional image is not itself a semialgebraic subset of an unspecified `R^n`; the finite parameter space and finite marginal images are the correct objects.

7. **Algebraicity.** The energy image is a nonempty compact semialgebraic subset of `R` over `F`, by H-TS. Lemma P3.1 puts its minimum in `F`. For matrix bond `r`, repeat with `C=M_r` and, if desired, take the finite union for `1<=n<=r`. This proves (P3.1) and the matrix version. ∎

The algebra structure fact in step 1 is the finite-dimensional C*-algebra classification: decompose the centre by minimal central projections; each summand has scalar centre and is a full matrix algebra by the finite-dimensional *-representation decomposition. Its use imposes no arithmetic restriction on the state parameters.

### Parameter count (used in P4)

For a fixed tuple with `m=Σ n_a²`, the independent Choi coordinates number

\[
 \sum_{a,b}(q n_a n_b)^2=q^2m^2,
\]

and density coordinates number `m`. Thus `k_0=q²m²+m` real parameters suffice. There are `m` unital equations, `m` stationary equations, one trace equation, and

\[
 \sum_{a,b}(2^{q n_a n_b}-1)+\sum_a(2^{n_a}-1)
\]

PSD inequalities, using every nonempty principal minor. For `C=M_r`, `q=2`, this becomes `k_0=4r⁴+r²`, Choi size `2r²`, density size `r`, and maximum degree of the constraints plus the range-two energy graph is `max(2r²,3)`. These are upper counts without removing dependent equations, which is preferable for a transparent effective bound.

### Corollary P3.3 (FNW exclusion and strict gap)

If the true ground energy density `e_0=inf_{all TI states}ω(h)` is transcendental, then every finite `d` and `r` satisfies `e_d^alg>e_0`, `e_r^mat>e_0`, and no translation-invariant C*-FCS ground state exists.

**Proof.** Every class is contained in all TI states, so its infimum is at least `e_0`. Equality is impossible because P3.2 makes the former algebraic and the latter transcendental. A ground state in the class would give equality by evaluating its energy. Notice that attainment was not needed for the strict inequality: a finite algebraic infimum already suffices. P3.2 proves attainment in addition. ∎

This does not say that every energy in the class is algebraic. Already for the algebraic one-site interaction `h=|1><1|`, a TI product state with density `diag(1-t,t)`, `0<=t<=1`, has energy `t`; it may be transcendental. The optimum is nevertheless zero. “Algebraic ansatz” refers to its defining constraints, not a restriction that its free parameters are algebraic.

**H-HULTHEN.** For `h=S_x⊗S_x+S_y⊗S_y+S_z⊗S_z`, `S_a=σ_a/2`, the spin-1/2 antiferromagnetic chain with one interaction per site has `e_0=1/4-log 2`. Reference: L. Hulthén (1938), *Über das Austauschproblem eines Kristalles*, Ark. Mat. Astr. Fys. 26A no. 11; normalisation/theorem number **from memory, to be byte-cited**. H-BAKER with the single logarithm, or H-LOG2 below, implies that this value is transcendental. Hence P3.3 applies under H-TS, H-HULTHEN and that transcendence input.

### Corollary P3.4 (exact scope of the notebook transposition)

Let `X⊂R^k` be nonempty semialgebraic over `F=Q-bar∩R`, and let `v:X→R` have a single-valued semialgebraic graph over `F`. If `inf_X v` is finite, it belongs to `F`; compactness and continuity additionally imply attainment. The same holds for the supremum. Polynomial functionals qualify; rational functions qualify where their denominators are nonzero, and a specified algebraic-function branch qualifies when its graph is semialgebraically defined. Finite unions and algebraic constraints on transfer data qualify. Proof: apply H-TS to the graph and Lemma P3.1 to its image.

This is the precise version of `finite-prime-language.md:133–141`. Fixed transcendental coefficients, entropy/log-det objectives, infinitely many constraints or variables, and an unselected multivalued algebraic relation do not automatically qualify. A fit using *true transcendental target data* as coefficients is not an optimisation over algebraic data. Individual determinants and traces need not be algebraic when parameters are unrestricted; only their finite semialgebraic optima have the asserted property. This distinction also corrects lines 157–163 of that note.

## P4. An explicit Diophantine lower bound — PROVED-conditional

### H-BPR: a deliberately coarse, fully specified endpoint bound

Use integer coefficient height `H(P)=max |coefficient(P)|` and primitive minimal-polynomial height for algebraic numbers. For `s>=1`, total degree `δ>=2`, `k>=1` **total real variables including the projected coordinate**, and integer input coefficients of absolute value at most `2^τ`, `τ>=1`, take

\[
 D(s,\delta,k)=(2s\delta)^{\,2^{k+1}},\qquad
 H(s,\delta,k,\tau)=2^{(\tau+1)D(s,\delta,k)^2}.          \tag{P4.1}
\]

**H-BPR.** Every finite endpoint of the projection onto one coordinate of a Boolean combination of sign conditions on those polynomials has algebraic degree at most `D` and minimal-polynomial height at most `H`.

Reference: S. Basu, R. Pollack, M.-F. Roy, *Algorithms in Real Algebraic Geometry*, second edition (2006), Chapter 11 (full cylindrical algebraic decomposition) and Chapter 14, Theorem 14.16 for the sharper quantifier-elimination algorithm; identification of the latter number is **from memory, to be byte-cited**. Formula (P4.1) is **not quoted as a formula printed in that theorem**. It is a much weaker envelope, with constants derived in the next paragraph from the full projection theorem. The sharper singly exponential one-block bounds usually written with unspecified absolute constants are not used. The theorem input retained under this name is the correctness of full CAD projection, including truncations on degree-drop loci, not an invented numerical value for a big-O constant. A local independent formulation unexpectedly exists in Coste `refs/src/coste-2002/paper.txt:749–774,782–800`, giving precisely the full projection mechanism needed below. This source discovery improves on the brief's “no local source” inventory.

**Derivation of the numerical envelope from full CAD (PROVED conditional on its projection theorem).**

1. Start with degree `δ_0=δ` and log-base-two coefficient **length** bound `h_0=τ+k log₂(δ+1)`; there are at most `(δ+1)^k` monomials. At each projection form all leading truncations of the input polynomials, then output their coefficients, principal subresultants of each truncation and its derivative, and pairwise principal subresultants of truncations. The output polynomials involve only the remaining variables. The full projection theorem supplies a sign-invariant cylindrical decomposition, even where leading coefficients vanish. After `k-1` projections its nonzero univariate polynomials cut the line into cells on each of which the existential formula is constant. Every finite boundary point is therefore a root of one of them.
2. A principal subresultant is a determinant of size at most `2δ_i`, with entries coefficients of the relevant polynomials or their derivatives. Truncation and coefficient extraction do not increase length; differentiation increases it by at most `δ_i`. Consequently valid simultaneous degree and log-length recurrences are

\[
 \delta_{i+1}=2\delta_i^2,\qquad
 h_{i+1}\le2\delta_i h_i+2\delta_i\log_2\delta_i
                  +\log_2((2\delta_i)!)
 \le2\delta_i h_i+6\delta_i^2.
\]

The determinant estimate is the sum over permutations; the last inequality uses `log₂((2δ_i)!)<=2δ_i log₂(2δ_i)` and `1+2 log₂δ_i<=3δ_i`. Coefficients retained without a determinant satisfy the same bound. Dividing by `δ_{i+1}` proves inductively

\[
 \delta_i=(2\delta)^{2^i}/2,\qquad
 h_i\le\delta_i\big(h_0/\delta+3i\big).
\]

The number of projected polynomials can be enormous, but these **per-polynomial** bounds do not multiply them together; pairwise projection suffices.
3. Let a final polynomial `P` vanish at the endpoint `α`. Its primitive minimal polynomial divides the primitive part of `P` over `Z`. For any integer factor `Q`, `H(Q)<=2^{deg P}L(P)`: indeed coefficient elementary-symmetric bounds give `H(Q)<=2^{deg Q}M(Q)`, multiplicativity of Mahler measure and `M(integer polynomial)>=1` give `M(Q)<=M(P)`, and Jensen's inequality gives `M(P)<=L(P)`. Therefore

\[
 \deg\alpha\le\delta_{k-1},\qquad
 \log_2 H(\alpha)\le\delta_{k-1}(1+h_0/\delta+3(k-1)).
\]

For `δ>=2`, `log₂(δ+1)<=δ`, so the last parenthesis is at most `τ+4k+1`. Since `δ_{k-1}<=D` and `D>4k+1`, the height is at most `(τ+1)D²` in base-two logarithms. This proves the envelope (P4.1). **No hidden asymptotic constant enters it.** Coefficient heights for arbitrary algebraic input data would also require defining polynomials and isolating intervals for those coefficients; our Heisenberg input is rational, so this complication does not arise. ∎

### H-LOG2: an explicit approximation measure

For any real algebraic `α` of degree `n>=1`, whose primitive minimal polynomial has length `L(α)`, and any `L>=max(3,L(α))`, assume

\[
 |\log2-\alpha|\ \ge\
 \exp\!\left[-151000\,n^2\,
       \frac{\log L+n\log n}{1+\log n}\right].           \tag{P4.2}
\]

Reference: Yu. V. Nesterenko and M. Waldschmidt, *On the approximation of the values of exponential function and logarithm by algebraic numbers*, arXiv:math/0002047 (2000), **Theorem 3(1), page 3**. Bibliographic starting point was from memory; the theorem and the constant `151000` were checked in the [authors' paper](https://arxiv.org/pdf/math/0002047), page 3, during this lane. It remains **to be byte-cited into the notebook provenance** and is retained as named H-LOG2 per the brief. This is a uniform bound in both degree and length, not just an irrationality measure for rational approximants. With coefficient height at most `H` and degree at most `D`, take `L=(D+1)H`; the exponent is increasing with `n>=1`, so replacing the actual degree by `D` is legitimate. For instance `n²/(1+log n)` is increasing and so is `n log n`.

### Theorem P4.1 (explicit spin-chain bound)

Assume H-TS, H-BPR, H-LOG2 and H-HULTHEN in the forms above. Let `d>=2` denote **ordinary matrix bond dimension**, and let `e_d=e_d^mat` be the minimum over all TI C*-FCS with auxiliary `M_d` (allowing smaller presentations). Set

\[
\begin{aligned}
 k_d&=4d^4+d^2+1,\quad \delta_d=2d^2,\\
 s_d&=2^{2d^2}+2^d+2d^2,\quad \tau_d=32d^4,\\
 D_d&=(2s_d\delta_d)^{2^{k_d+1}},\quad H_d=2^{(\tau_d+1)D_d^2}.
\end{aligned}                                                \tag{P4.3}
\]

Then

\[
 e_d-e_0\ge
 \exp\!\left[-151000D_d^2
 \frac{\log((D_d+1)H_d)+D_d\log D_d}{1+\log D_d}\right]
 \ge B(d)>0,                                                  \tag{P4.4}
\]

where the especially simple explicit decimal bound used in the check is

\[
 \boxed{ B(d)=10^{-200000(\tau_d+2)D_d^4}
 =10^{-200000(32d^4+2)(2s_d\delta_d)^{2^{k_d+3}}}. }             \tag{P4.5}
\]

This bound also applies to any subclass, in particular TI matrix-product states of bond at most `d`, and to the brief's class with **auxiliary algebra dimension** at most `d`. These are different classes; using the larger matrix class gives a common conservative bound, not an identification of their minima.

**Proof.**

1. **Hamiltonian and energy polynomial.** In the physical basis `00,01,10,11`,

\[
 h=\begin{pmatrix}1/4&0&0&0\\0&-1/4&1/2&0\\
                   0&1/2&-1/4&0\\0&0&0&1/4\end{pmatrix}.
\]

For Choi indices `(i,a,b)` with physical `i∈{0,1}`, incoming auxiliary `a∈{1,…,d}` and outgoing `b∈{1,…,d}`, the convention is

\[
 J_{(i,a,b),(j,c,z)}=E(|i\rangle\langle j|\otimes
                         |a\rangle\langle c|)_{bz}.
\]

Thus

\[
 e(J,\rho)=\sum_{i,j,k,l=0}^1 h_{(i,k),(j,l)}
 \sum_{a,b,c,z,t=1}^d
 \rho_{zb}J_{(i,a,b),(j,c,z)}J_{(k,t,a),(l,t,c)}.          \tag{P4.6}
\]

The scalar is real on Hermitian data; in real coordinates take its real part, a polynomial with rational coefficients and degree three. Multiplying by four clears all denominators. Introduce a single output coordinate `x` with equation `4x+4e(J,ρ)-1=0`, so `x=1/4-e`. Optimising directly in this shifted variable avoids any unaccounted height growth under a subsequent affine substitution.

2. **Counts.** The Choi matrix has size `M=2d²` and has `M²=4d⁴` real Hermitian coordinates. The density has `d²`. With `x`, the total is `k_d`. There are `2^M-1` Choi minor inequalities and `2^d-1` density minor inequalities; `d²` real unital equations, `d²` real stationary equations, one trace equation and one graph equation. Their sum is exactly `s_d`. The maximal degree is `max(M,d,2,3)=2d²`. No factorisation, division by a density eigenvalue, or rank assumption is used.
3. **Input heights.** Each complex coordinate is at most two real monomials in absolute coefficient length. A determinant of size at most `M` has length at most `2^M M!`. Unital equations have length at most `2d+1`. Real stationary equations have length at most `8d²+2`. Since the absolute coefficient sum of `4h` is eight, expanding (P4.6) yields length at most `64d⁵` for `4e`, and at most `64d⁵+5` for the graph polynomial. These are all strictly less than `2^{32d⁴}`. For example `log₂(2^M M!)<=M+M log₂M<=M+M²<8M²=32d⁴`; the other polynomial bounds are smaller for `d>=2` (also checked as integer inequalities in the script). Coefficient height is at most length. Thus `τ_d` is a valid, deliberately loose bit bound.
4. **Endpoint.** P3 gives a compact nonempty feasible set. Its `x` image has maximum `α_d=1/4-e_d`. H-BPR and steps 2–3 imply `deg α_d<=D_d`, `H(α_d)<=H_d`. H-HULTHEN gives

\[
 e_d-e_0=\log2-\alpha_d\ge0.
\]

Apply H-LOG2 with `L=(D_d+1)H_d` to obtain the first inequality in (P4.4). In particular it also proves strictness.
5. **Decimal simplification.** For `D>=4`, `log(D+1)+D log D<=D²`. Drop the denominator `1+log D>=1` in (P4.4). Its exponent in absolute value is at most
`151000[(τ+1)log 2+1]D⁴<=200000(τ+2)D⁴`. Finally `exp(-C)>=10^{-C}` for `C>=0`. This proves (P4.5) with no unprinted constants.
6. **Coverage of smaller and direct-sum auxiliaries.** An auxiliary `⊕_a M_{n_a}` with `Σ n_a²<=d` has faithful block representation on dimension `R=Σ n_a<=d`. If `R<d`, add a decoupled filler block of size `d-R`, a product channel on it, and boundary density zero there. Compose the block generating map with the CP conditional expectation deleting off-diagonal blocks of `M_d`; include the output block algebra into `M_d`. The resulting map is CP and unital, and its stationary boundary functional reproduces all original local expectations. This also embeds smaller `M_r` presentations into `M_d`. Hence `F_d^alg⊂F_d^mat`; its minimum is no smaller and inherits the same lower bound. A TI MPS with auxiliary `M_d` is a subclass of these CP presentations and inherits it as well. ∎

If one only wants the auxiliary-algebra-dimension convention, the direct-sum count `4m²+m` in P3 can substantially reduce `k`; the finite union of tuple images can be bounded type by type and the least resulting bound taken. Formula (P4.5) intentionally uses a single transparent bound valid for both conventions. It says nothing about finite-chain energies or arbitrarily growing translation periods at fixed nominal tensor size.

### Priority and the metric analogue

**Priority — OPEN, not a theorem.** The qualitative argument is FNW's precedent. A directly relevant subsequent paper is V. Blakaj and M. M. Wolf, *On the set of reduced states of translation invariant, infinite quantum systems*, Lett. Math. Phys. **114**, 28 (2024), [DOI/source](https://doi.org/10.1007/s11005-024-01776-1), Introduction and Theorem 1: it discusses the FNW transcendental-energy obstruction and proves non-semialgebraicity of the full marginal set. It does not supply the explicit degree/height-to-error calculation (P4.3–P4.5) in the material inspected. Targeted searches for a Heisenberg/MPS Diophantine rate found no such rate, but this is not an exhaustive priority search. Therefore the note's “first” and “nobody appears to have written it down” (`finite-prime-language.md:72–74`) must be labelled unverified, not promoted to a rigorous historical claim. This lane proves a conditional quantitative obstruction; it does not prove novelty or a sharp convergence rate.

**Metric analogue and open inputs — SHARPENED / OPEN.** One needs a specific finite semialgebraic candidate class defined over a fixed real closed coefficient field, an algebraically definable *optimal* invariant on that class, an independent identification of the true metric's value with a number outside that field, and an effective separation measure plus coefficient bounds for a rate. Knowing a listed constant to be transcendental would not automatically identify it as the required invariant; the arithmetic/archimedean data already in the candidate class may themselves include it. The irrationality of any specified nonzero zeta-zero ordinate, the irrationality/transcendence of Euler's `γ`, and of the usual first Stieltjes constant `γ_1` remain open inputs here. For `γ` and Stieltjes constants, a standard primary survey is J. C. Lagarias, *Euler's constant: Euler's work and modern developments*, Bull. AMS **50** (2013), 527–628, [source](https://doi.org/10.1090/S0273-0979-2013-01423-X). The zero-ordinate statement is retained as the notebook's open problem, not a theorem about absence of future progress; no verified resolution was found. Most importantly, **irrationality of an ordinate is insufficient for P3's exclusion** because algebraic irrational minima are permitted. Transcendence (or nonmembership in the actual coefficient field) and an invariant-realisation argument are needed. Nor would transcendence of `γ` or `γ_1` alone settle the original Baker grading: independence from an entire archimedean span is stronger. The assertion that *any one* of the three listed inputs automatically unlocks metric exclusion (`finite-prime-language.md:230–232`) is therefore refuted in that unqualified form.

## Numerical checks for the blind lane

All checks use arithmetic data or symbolic kinematic examples and contain no zero calls. They are independent checks of the formulas, not implementations of a new full Weil form. Accordingly no uncalibrated alternative `W` is reported; the mandatory `zst` calibration for such an implementation is not being bypassed. Source-only substitutions in (P2.2) use exactly CCM's `Ψ`, and all P1 block formulas are verified against the full Loewner matrix symbolically.

Run from the repository root:

```
python3 notes/rtp-round-2/prover/checks/p1_p2.py
python3 notes/rtp-round-2/prover/checks/p3_choi.py
python3 notes/rtp-round-2/prover/checks/p4_bound.py
```

Outputs are retained alongside the scripts as `p1_p2.txt`, `p3_choi.txt`, `p4_bound.txt`.

### P1: exact offset, with decimals for orientation

`checks/p1_p2.py` uses SymPy exact rational/radical arithmetic. It constructs the full `5×5` Loewner matrix and checks the parity transformation, both enlarged determinants, both even endpoints, strict positivity of the odd complement there, and the product's derivative at zero. The proof of unique global optimality is P1.3, not numerical root selection.

| quantity | exact value | decimal (display only) |
|---|---|---|
| left endpoint of the joint interval | `(9-3√337)/82` | `-0.561861942098261681652136079953` |
| right endpoint | `(9+3√337)/82` | `0.781374137220212901164331201904` |
| midpoint | `9/82` | `0.109756097560975609756097560976` |
| joint maximum | `0` | `0` |
| maximum minus midpoint | `-9/82` | `-0.109756097560975609756097560976` |
| offset / half-width | `-3/√337` | `-0.163420413210852990787760114410` |

### P2: three atom centres, and the legitimate direct sum

Take centres `M={1,2,6}`, coefficients `(1,2,-1)`, `S={2,3}`, and any admissible normalised bump from P2.4. Equivalently use the formal atoms only to enumerate the pairs. The script factors each integer ratio exactly:

| pair ratio | finite-place local coefficient | pole kernel | archimedean off-origin kernel |
|---|---|---|---|
| `2/1=2` | `A_2=2√2` | `3√2/2` | `2√2/3` |
| `6/2=3` | `A_3=-4/√3` | `4√3/3` | `3√3/8` |
| `6/1=6` | no prime-power term | `7√6/6` | `6√6/35` |

Consequently

\[
 R_{\rm fin}=-2\sqrt2\log2+\frac4{\sqrt3}\log3
       =0.576620115453161525317747642908\ldots,
\]

with Baker coordinates `(constant,iπ,log2,log3)=(0,0,-2√2,4/√3)`. Each other prime coordinate is zero. The symbolic coefficients are exact; the decimal is not evidence for independence (H-BAKER is). This is a three-centre instance of the **corrected** theorem. The original `L_S` has no claimed coordinates, and a full atomic Weil value is undefined; there is no fabricated three-atom check of that false statement.

### P3: energy and Choi conventions

`checks/p3_choi.py` checks the cubic contraction (P4.6) on an exact complex product channel with pure physical density `[[1/2,i/2],[-i/2,1/2]]` and auxiliary density `I_2/2`. Its Choi matrix is PSD of trace 2, its generating map is unital, and the boundary is stationary. The contraction equals the direct product-state expectation `1/4`. It also checks the local Hamiltonian spectrum `{-3/4,1/4,1/4,1/4}`. Complex off-diagonal entries make this a check of the index/conjugation convention as well as the energy scale.

### P4: explicit conditional decimal lower bounds

Let `E(d)=log₁₀(-log₁₀ B(d))`. The exact quantity computed, without ever materialising the astronomical integer `D_d`, is

\[
 E(d)=\log_{10}(200000(\tau_d+2))
                  +2^{k_d+3}\log_{10}(2s_d\delta_d).
\]

| `d` | `k_d` | `δ_d` | `s_d` | `τ_d` |
|---:|---:|---:|---:|---:|
| 2 | 69 | 8 | 268 | 512 |
| 3 | 334 | 18 | 262170 | 2592 |
| 4 | 1041 | 32 | 4294967344 | 8192 |
| 8 | 16449 | 128 | `340282366920938463463374607431768211840` | 131072 |

| `d` | `E(d)` (approximation, 17 significant digits) | conservative rounded **lower bound** on the gap |
|---:|---|---|
| 2 | `1.71528382146590596 × 10^22` | `10^{-10^{1.7152839 × 10^22}}` |
| 3 | `1.95274538929341369 × 10^102` | `10^{-10^{1.9527454 × 10^102}}` |
| 4 | `2.15629830912744022 × 10^315` | `10^{-10^{2.1562984 × 10^315}}` |
| 8 | `1.43759761809591357 × 10^4954` | `10^{-10^{1.4375977 × 10^4954}}` |

These are positive decimal powers, not numerical underflow to zero. For scale, even the `d=2` bound has about `10^{1.7153×10^22}` zeros before its first nonzero decimal digit. The displayed conservative exponents are rounded **up**, so the resulting powers are smaller than the exact bound (P4.5). Computation uses `mpmath` at 100 decimal digits for display and `mpmath.iv` at 80 decimal digits to enclose the logarithms and verify the direction of each rounding; input-height inequalities use exact Python integers. This certifies the arithmetic of the **conditional** bound, not H-LOG2 or CAD itself. No variational optimisation or numerical estimate of the actual `e_d` is claimed. The huge weakness comes mainly from deliberately extravagant CAD degree and height bounds; these numbers are not estimates of physical convergence.

## What this changes in the notebook

No claim database or report shard was edited; these are proposed changes for REFUTE review.

| existing claim row | proposed treatment |
|---|---|
| `lem:bordering-interval` (lemma, sketched) | **PROVED after wording corrections** in P1: `d>0`, positive definite completion for finite information; `N>=1` for two strictly concave quadratics; allow empty/singleton feasible sets; determinant deficit rather than gain; two columns together in (iii). Add P1.2's explicit `u,w,ℓ` and P1.3's midpoint iff criterion. |
| `prop:extension-disc` (proposition, sketched) | **Unchanged**; P1 only supplies the general Schur-complement step. The database summary still omits the conjugate in its complex disc-centre formula, unlike corrected shard `report/sections/08g_weil_window_extension.tex:91`; synchronise that wording when editing. |
| `obs:prime-by-prime-blind` (observation, sketched) | **Do not upgrade from P2**. The proposed numerical proof is refuted for `L_S`. Separate the existing ansatz claim from P2.4's precise foreign-comb blindness; a restriction of the full Weil form can carry information about zeros, as the correction in `metric-as-state.md:73–89` already says. |
| `thm:weil-positivity-finite` (theorem, proved) | **Unchanged**; a finite spectral/trace criterion is not a definition of the analytic form on point masses. |
| `prop:trace-supertrace-criterion` (proposition, proved) | **Unchanged**; finite graded trace rationality is independent of the new optimal-value obstruction. |
| `obs:factor-by-factor-limits` (observation, sketched) | **Unchanged**; append the precisely scoped P3.4 transposition as a separate result, not a proof of all limits/continuation assertions. |

Suggested new rows (labels provisional; the status column expresses proof status, with dependencies to be recorded explicitly):

| suggested id | kind | status and scope |
|---|---|---|
| `prop:loewner-midpoint-condition` | proposition | **PROVED**; P1.3, nonempty interior and positive old blocks |
| `obs:finite-prime-language-collapse` | observation | **PROVED / REFUTATION**; P2.1, original `L_S` independent of `S` |
| `prop:atomic-weil-domain-obstruction` | proposition | **PROVED**; P2.3, no unprescribed atomic extension |
| `thm:baker-prime-remainder` | theorem | **PROVED-conditional on H-BAKER**; P2.4, genuine normalised admissible bumps and subtracted finite-place remainder |
| `prop:finite-bond-semialgebraic-optimum` | proposition | **PROVED-conditional on H-TS**; P3.2–P3.4, compact parametrisation, attained algebraic energy, finite semialgebraic optima |
| `thm:fnw-transcendental-exclusion` | theorem | **PROVED-conditional on H-TS and a transcendental target**; P3.3; Heisenberg also H-HULTHEN and H-LOG2 or H-BAKER |
| `thm:diophantine-heisenberg-floor` | theorem | **PROVED-conditional on H-TS, H-BPR, H-LOG2, H-HULTHEN**; P4.1 with the explicit envelope derived above |
| `num:diophantine-heisenberg-floor` | numerical | **NUMERICAL, conditional formula evaluation**; exact parameter counts and interval-enclosed logarithmic displays, not an optimisation run |

The future-directions note needs more than a status upgrade. Replace its proposed whole-value Baker grading and foreign-prime exclusion; remove the point-mass inclusion until a new regularisation is specified and justified; distinguish logarithmic coordinates from archimedean provenance; retain the compact semialgebraic optimum theorem; replace the quantitative sketch by P4 with its explicit hypotheses; remove the automatic inference from mere irrationality to metric exclusion; mark novelty as **OPEN**. Membership of the bump archimedean integrals in the named `A`, a useful transcendental metric invariant and a much sharper effective degree bound remain **OPEN**.

**Sources still to byte-cite.** H-BAKER (Baker 1975, Chapter 2; additionally the theorem is stated in Baker's own 1970 ICM lecture, p. 20, [primary proceedings](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1970.1/ICM1970.1.ocr.pdf)); H-TS in its coefficient-field form; the full CAD theorem under H-BPR (BPR Chapter 11, with the local Coste projection source and our explicit elementary coefficient proof); Nesterenko–Waldschmidt Theorem 3(1), including the definition of length; and H-HULTHEN in precisely the `S=σ/2`, per-site normalisation. FNW's exact original wording and historical attribution remain to be checked against its 1992 paper rather than inferred from the notebook; Blakaj–Wolf supplies a useful later primary attribution. The numerical bound's constants do **not** require guessing a constant in BPR Theorem 14.16.

**Local source audit.** `refs/src` and `refs/ocr` were listed. The latter contains the Burg and Landau OCR texts. Burg's autocorrelation setting is visible at `refs/ocr/burg-1975/ch2.ocr.txt:5–24`; none of P1's algebra depends on a new Burg quotation. A Lagarias source is present at `refs/src/math/0404394/main.tex` (*Li Coefficients for Automorphic L-Functions*, title/author `:143–146`); it reports the Bombieri–Lagarias arithmetic decomposition at `:322–330`. `refs/src/math/0008177/main.tex` is the elementary RH criterion source. No original Bombieri–Lagarias 1999 source was identified in this scan; no claim here is inferred from an absent copy. All actual Weil signs, domain restrictions and kernels used in P2 were read from the CCM file at the exact lines cited above.
