# RTP-2, lane P: proofs and corrections

Author: `codex:gpt-6-astra`, 2026-09-26.

No RH assumption; no zero ordinates are used as data. This is a research deliverable, not a registration. External inputs remain named hypotheses pending byte-citation. All paths and line numbers refer to the copies read in this session. Only this lane's deliverable, progress file and checks are written.

## Correction ledger

1. **P1 — SHARPENED.** A Gaussian log determinant requires positive definiteness. `log(d/s)` is the loss of determinant relative to the maximum determinant, not a gain of the true determinant. The odd block at `N=0` has an affine Schur complement, not a strictly concave quadratic. Intervals may be empty or singletons; a joint log-det maximiser requires a positive definite extension.
2. **P2 — REFUTED as requested.** The proposed archimedean set contains logarithms of *all* algebraic numbers, including all `log q`. Thus the proposed `L_S` is independent of `S`, and no numerical prime-coordinate projection annihilating the archimedean span exists. Baker independence within the logarithmic subspace does not repair this overlap. A point mass is not a test function for the explicit-formula distribution: its self-convolution contains a mass at zero, and prime evaluation and the archimedean diagonal are undefined. A labelled discrete model must not be called the Weil form.
3. **P3 — SHARPENED.** Semialgebraicity applies to a finite parameter space and every fixed finite marginal image, not literally to an infinite sequence of state coordinates in a Euclidean space. Auxiliary C*-algebra dimension and matrix bond dimension differ. Individual energies need not be algebraic; finite semialgebraic optima over algebraic data are algebraic.
4. **P4 — conditional conclusion.** Numerical bounds require numerical constants in both the elimination and transcendence hypotheses; big-O citations alone are insufficient. A priority claim (“first”) requires a literature audit and is not asserted here. Irrationality alone cannot exclude optima over the real algebraic numbers.
5. **Source convention correction.** The present CCM copy places `bombtest` at `refs/src/2511.22755/mc2arXiv.tex:465–467`, not lines 385–388 of the briefs. The formula itself is unchanged.

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
