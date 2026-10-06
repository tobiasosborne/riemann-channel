# The three ingredients for $\zeta$: what exists on Connes's cokernel

Author: `claude:opus-5.5`, 2026-10-06, lane G of an orchestrated session.

Status: **a record, not a round; nothing registered in db/claims.tsv; no REFUTE review; no shard.** Each statement is labelled *standard*,
*proved here*, *proved in 04t* (or another named page), *checked*, *heuristic*, *open* or *negative finding*. `refs/src/` was absent, so Weil's
criterion, Connes 1998, Tate and Bochner–Schwartz are quoted from memory. Checks: `checks/check_zeta_ingredients.py`, output
`checks/output_zeta_ingredients.txt`, **32 of 32 pass**, about 15 s (numpy, sympy, mpmath; the high-precision window data come from the
reviewer helper `notes/reviews/scratch_rtp2_grid_common.py`).

The question, from `data-ladder.md`: every understood case is a triple $(L,M,\Omega)$ plus a vacuum $J$. Lane E (`cone-bridge.md`) adds that RH
is the non-emptiness of a cone of similitude forms, and that the cone has a witness, the Weil form $\tfrac12\Omega(M-V)$, which is polynomial in the
step. This page takes stock of which of these exist for $\zeta$, and tests on a finite window whether Weil's form for $\zeta$ is "the Weil-form point
of a cone" in lane E's sense.

**Findings.**

- **The step and its adjoint exist exactly, on the whole test algebra** (*standard*). Write $M_a$ for convolution by $\delta_a$. The involution
  $h\mapsto\tilde h$ sends $\delta_a$ to $a\,\delta_{1/a}$, so $V_a:=\tilde\delta_a*{}=a\,M_a^{-1}$, which is $V=qM^{-1}$ with $q=a$. Weil's form $B(h,k)=\omega(h*\tilde k)$
  satisfies $B(M_ah,M_ak)=a\,B(h,k)$ and $B(M_ah,k)=B(h,V_ak)$ for every $a>0$, before RH. What does not exist is integrality: the steps form a
  continuous group, and no finite window carries one of them as an invertible map (*checked*, D4).
- **The $\Omega$ question reduces to the step** (*proved here*, Proposition 1). For a non-degenerate symmetric $G$, a compatible $\Omega$ with
  $\tfrac12\Omega(M-V)=G$ exists iff $M^TGM=qG$, provided $M-V$ is invertible, and then $\Omega=2G(M-V)^{-1}$. So "is Weil's form a Weil-form point?"
  is exactly "is the step a similitude of Weil's form?".
- **On the full algebra, yes, but not for one $\Omega$** (*proved here* in the spectral model, *checked* E1–E4). Each prime step $p$ gives its own
  $\Omega_p=2B(M_p-V_p)^{-1}$. Its weights are $1/(\sqrt p\sin(\gamma\log p))$, with small divisors: 4393 over the first 3000 zeros for $p=2$. No single
  compatible $\Omega$ serves two primes. With respect to the functional-equation pairing $\Omega_{\rm FE}$ of 04t, the Weil form of the step $p$ has weights
  $\sqrt p\sin(\gamma\log p)$, and these have both signs, about half each. So it is indefinite. With respect to $\Omega_{\rm FE}$, Weil's form is the **vacuum** point (unit weights).
  It is a Weil-form point only for the **infinitesimal** step $D$, with $\Omega_D=B(\cdot,D^{-1}\cdot)$. Its Williamson weights there are $|\gamma|$, the analogue of lane E's $\mathrm{Im}\,\alpha_j$.
- **On a finite window, only the infinitesimal step survives** (*checked*, B5, D1–D6). $\Omega_N=G_N(\cdot,D^{-1}\cdot)$ is exactly anti-Hermitian on the mean-zero window space, which is the notebook's Loewner identity.
  The compressed dilation by 2 behaves differently. It is a similitude ($c\to1$, residual $\to0$) only on functions supported in $[0,L-\log2]$. On the whole window, and on the low Fourier modes, the residual of $M^TGM=cG$ stays near
  $0.4$ for $N=5\dots160$ and converges to a non-zero edge limit. It does not shrink with $N$, nor from $x=13$ to $x=100$ (*negative finding*).
- **$\Pi_1$** (*checked*, C1–C2, at 40–60 digits). On the window, Weil's $Z_N$ (with the explicit formula's pole terms) is positive definite. Both $Z_N-P_N=-\mathrm{Loc}$
  and $Z_N+P_N$ have inertia $(n-1,1,0)$: exactly one negative direction, which comes from the pole plane. Adding a synthetic off-line quartet (two off-line
  pairs) adds two negative directions. So the negative index is the pole plane plus one per off-line pair, the $\zeta$ analogue of `graph-ihara.md`'s
  "trivial plus off-band".

---------------------------------------------------------------------------------------------------------------------

## 1. The objects and the identities that hold

Conventions are those of `analytic.md`: $u=\log x$, and $F_h(s)=\int h(u)e^{(s-1/2)u}du$ (this is $\hat h(s)$), $\tilde h(x)=x^{-1}\overline{h(1/x)}$,
$g=h*\tilde h$, $\hat g(s)=\hat h(s)\overline{\hat h(1-\bar s)}$, $Z=\sum_\rho\hat g(\rho)=P-\mathrm{Loc}$.

1. **The step.** $\delta_a$ is the unit point mass at $a$ for $d^\times x$. Then $\widehat{\delta_a*h}(s)=a^s\hat h(s)$, and $\widehat{\tilde\delta_a}(s)=\overline{a^{1-\bar s}}=a\cdot a^{-s}$, so
   $\tilde\delta_a=a\,\delta_{1/a}$ (*standard*). In lane E's notation, $M_a=\delta_a*$ and $V_a=\tilde\delta_a*=aM_a^{-1}$. **The involution is the passage $M\mapsto V$.** On a mode
   $x^{\rho}$ the step acts by $a^\rho$, and $|a^\rho|=\sqrt a$ iff $\mathrm{Re}\,\rho=\tfrac12$. "Norm $q$" with $q=a$ is the critical line. After the $|a|^{1/2}$ normalisation, the step is
   unitary and $V=M^{-1}$. The generator is $D=d/du$, which acts by $\rho-\tfrac12$.
2. **Similitude and adjunction for Weil's form** (*standard*, elementary). $(\delta_a*h)*(\delta_a*h)^\sim=a\,(h*\tilde h)$, so $B(M_ah,M_ak)=aB(h,k)$, and
   $B(M_ah,k)=\omega(\delta_a*h*\tilde k)=B(h,V_ak)$. The adjunction holds for the symmetric form itself, as it does for lane E's $W$, since
   $W(Mx,y)=\tfrac12\Omega(x,V(M-V)y)=W(x,Vy)$. Both identities hold for every $a$, with no hypothesis on the zeros.
3. **The functional equation as a pairing** (*proved in 04t*, `thm:fe-pairing-jets`). On a finite full-jet span of zeros, closed under $\rho\mapsto1-\rho$ and
   conjugation, $\Omega_{\rm FE}(e_\rho,e_{1-\rho})=-i\,\mathrm{sgn}\,\gamma$ is a real alternating form with $\Omega(C_tx,C_ty)=e^{-t/2}\Omega(x,y)$ for the whole flow. It is
   compatible with every step. It is indexed by the zeros, so it is not a datum on test functions. 04t's `thm:bond-positive-metric-criterion`(c) gives its
   vacuum: $Je_\rho=-i\,\mathrm{sgn}(\gamma)e_\rho$, $G_J=$ unit weights, under RH and simplicity.
4. **The explicit formula as Lefschetz** (*standard*; dictionary *proved* on the curve side in `analytic.md` §14). $Z=P-\mathrm{Loc}$: the pole form $P$ is
   $H^0\oplus H^2$, and $\mathrm{Loc}=\sum_vW_v$ are the local fixed-point traces (`adelic-gkp.md` §10). Checked here in the form used
   (A2: Gaussian tests, zero side against prime side to $4\cdot10^{-12}$).
5. **Connes's cokernel as $H^1$** (*standard*, Connes 1998, from memory). The orthogonal complement of the overlap profiles in $L^2(C_{\mathbb Q})$ carries the
   squeeze action, with spectrum the critical zeros. It is infinite-dimensional, it sees no off-line zero (analytic L3), and it carries no lattice.

## 2. Inventory

| ingredient | curve $C/\mathbb F_q$ | CM Hecke $L(\psi,s)$, $K=\mathbb Q(\sqrt{-7})$ (lane C) | $\zeta$ |
|---|---|---|---|
| integral lattice $L$ | $H_1$ of a lift, Deligne or Centeleghe–Stix module; class not fixed by counts (*standard*; *checked*, lanes A, F) | $\mathcal O_K$, one for all split primes (*checked*, lane C) | **none**: $\mathbb Q^2$ is rigid and divisible (G3); the cokernel is a Hilbert space with no integral structure (*negative finding*; *open*) |
| integral step $M$, $V=qM^{-1}$ | Frobenius, Verschiebung, $FV=q$ (*standard*) | $\psi(\mathfrak p)$ per split prime, $V=p/\psi(\mathfrak p)$, all commuting (*standard*) | a continuous group $M_a=\delta_a*$, $V_a=aM_a^{-1}$ exactly by the involution (*standard*); norm $q$ $\Leftrightarrow$ $\mathrm{Re}\,\rho=\tfrac12$; **not integral**, and in truncation a partial isometry losing $n\log p/L$ dimensions (*checked*, D4) |
| $\Omega$ with $\Omega(Mx,y)=\Omega(x,Vy)$ | Weil pairing (*standard*) | any alternating form on rank 2 ($M^T\Omega M=\det M\,\Omega$), one for all primes (*standard*) | $\Omega_{\rm FE}$ on finite jet spans of zeros (*proved in 04t*); per step $\Omega_p=2B(M_p-V_p)^{-1}$, singular and $p$-dependent (*proved here*, E2–E3); on a window, only $\Omega_N=G_N(\cdot,D^{-1}\cdot)$ (*checked*, B5) |
| Weil form $\tfrac12\Omega(M-V)$ | $\tfrac12\mathcal T$ for $\Omega_+$ (lane E, *proved*), polynomial in the step | one per prime: $\mathrm{Im}\,\psi(\mathfrak p)\cdot G_{J_K}$ (*proved here*, rank two) | Weil's $B=\omega(h*\tilde h)$ exists before RH (*standard*); it is $\tfrac12\Omega_p(M_p-V_p)$ only for the $p$-dependent $\Omega_p$; with respect to $\Omega_{\rm FE}$ the prime-step Weil forms are indefinite (*checked*, E1) and $B$ is the vacuum point; $B=\Omega_D(\cdot,D\cdot)$ for the generator (*proved here*) |
| the cone $\mathcal C$ | positive orthant of $g$ mode weights; $\ne\emptyset\Leftrightarrow$ RH (*standard*, lane E Prop. 1) | the ray of $G_{J_K}$, shared by all steps (*standard*) | on zero spans: one weight per ordinate, $\ne\emptyset\Leftrightarrow$ RH and simplicity (*proved in 04t*); on the test algebra: positive measures on the unitary axis (Bochner–Schwartz, from memory), non-empty unconditionally (the $L^2$ form), and RH $\Leftrightarrow B\in\mathcal C$ (Weil) |
| vacuum $J$ | exists; needs $\sqrt{4q-\lambda^2}$ (Hasse–Weil) | $J_K$, one for all primes, local RH free (*checked*, lane C) | $Je_\rho=-i\,\mathrm{sgn}(\gamma)e_\rho$ on zero spans, needs RH and simplicity (*proved in 04t*) = **open** |
| polarisation | $\Theta$; a further point, decides integrality (*standard*; lane E) | the complex structure of $K\otimes\mathbb R$ (lane C) | **none** (`adelic-gkp.md` §12.2; *open*) |
| counts | $N_k=\#C(\mathbb F_{q^k})$ (*standard*) | local: $p+1-\mathrm{Tr}\,\psi(\mathfrak p)$; global zeros not fixed by them (*checked*, lane C) | **none at $\infty$** (§12.1); the prime side has local Lefschetz traces with weight $\log p\cdot p^{-k/2}$, not integers (*standard*) |
| Lefschetz | $\sum(-1)^i\mathrm{Tr}(F^k|H^i)=\#\mathrm{Fix}$ (*standard*) | Weil's explicit formula for $L(\psi,s)$ (*standard*) | explicit formula $Z=P-\mathrm{Loc}$ (*standard*; A2) |

The CM column's Weil-form entry comes from Proposition 2 of lane E in rank two. Every alternating form is compatible with every $M$ of determinant $q$,
and $\tfrac12\Omega(M-V)$ has weight $\varepsilon\,\mathrm{Im}\,\psi(\mathfrak p)$ relative to $G_{J_K}$.

## 3. The $\Omega$ question

**Proposition 1** (*proved here*; checked on a random example, E5). Let $G$ be symmetric and non-degenerate, let $M^TGM=qG$, put $V=qM^{-1}$, and let $M-V$
be invertible. Then $\Omega:=2G(M-V)^{-1}$ is alternating, $M^T\Omega M=q\Omega$, and $\tfrac12\Omega(M-V)=G$. Conversely, if $\Omega$ is compatible and
$\tfrac12\Omega(M-V)=G$, then $M^TGM=qG$ (lane E, Prop. 3).

*Proof.* $V=G^{-1}M^TG$ gives $V^TG=GM$ and $M^TG=GV$, so $A=G(M-V)$ satisfies $A^T=GV-GM=-A$. Then $\Omega=2GA^{-1}G$ is alternating.
$M^T\Omega M=2GV(M-V)^{-1}M=2qG(M-V)^{-1}$, since $M$ commutes with $V$. ∎

So for a positive $G$ the content is entirely in $M$: whether the given step is a similitude. The real-symplectic triviality the brief mentions
(any positive form is the vacuum form of some $J$) does not touch this, because there $M$ is constructed from $G$ rather than given.

### 3.1 On the full algebra: the spectral model

Model (*proved in 04t*, its "diagonal semisimplification"). Take coordinates $x_\rho=\hat h(\rho)$ over the first $K$ critical zeros (3000 in the checks; on
these RH is a numerical fact). Here $B=\sum|x_\rho|^2$, $M_p=\mathrm{diag}(p^\rho)$, $V_p=\mathrm{diag}(p^{1-\rho})$, and $\Omega_{\rm FE}$ has weights $-i\,\mathrm{sgn}\,\gamma$ (04t's normalisation). 04t
`prop:weil-form-not-metric`(b) warns that unit weights are tied to the evaluation normalisation. The statements below compare weights within one
normalisation and are unaffected by it.

- **Compatible forms are diagonal** (*proved here*). A sesquilinear $\Omega$ with $\Omega(M_ax,M_ay)=a\,\Omega(x,y)$ for two multiplicatively independent $a$ pairs $\rho$
  only with $1-\bar\rho$, which is $\rho$ itself on the line. So every compatible form is one weight $w_\gamma$ per mode.
- **Prime steps** (*proved here*; checked E1–E3). The Weil form of $M_p$ for $\Omega$ has weights $w_\gamma\cdot\sqrt p\sin(\gamma\log p)$, up to a constant. For
  $\Omega_{\rm FE}$ these weights are $\sqrt p\sin(\gamma\log p)$, of both signs (fractions negative 0.502, 0.497, 0.498 for $p=2,3,5$). For $B$ to be the Weil form of $M_p$, one needs
  $w_\gamma\propto1/(\sqrt p\sin(\gamma\log p))$. This is $\Omega_p=2B(M_p-V_p)^{-1}$, the exact analogue of lane E's $\Omega_+=\mathrm{Tr}(x\bar y/(V-F))$. It exists as a
  formal form, but $M_p-V_p$ has multiplier $p^s-p^{1-s}$, which vanishes at $s=\tfrac12+i\pi k/\log p$ on the critical line. Its weights are therefore
  unbounded: $\min|\sin(\gamma\log2)|=1.6\cdot10^{-4}$ over 3000 zeros, which gives weight 4393. For two primes at once, one would need $\sqrt2\sin(\gamma\log2)/(\sqrt3\sin(\gamma\log3))$
  to be constant. It is not: the ratios at the first five zeros are $-1.67,-0.83,-1.14,0.71,0.61$.
- **The vacuum reading** (*proved here*, given 04t). Relative to $\Omega_{\rm FE}$, $B$ has unit weights for every step at once. That is the property of a vacuum form
  $\Omega(\cdot,J\cdot)$, and $B=G_J$ for 04t's $J$. In the CM case (lane C) the shared objects are $\Omega$ and the vacuum $J_K$, and the Weil forms
  $\tfrac12\Omega(M_\mathfrak p-V_\mathfrak p)$ differ from prime to prime. **So $B$ sits where $G_{J_K}$ sits, not where a per-prime Weil form sits.**
- **The generator** (*proved here*; checked E4). The group $\mathbb R_+^\times$ has no generating step. Its infinitesimal generator $D$ gives
  $\tfrac1{2t}\Omega_{\rm FE}(e^{tD}-e^{-tD})\to\Omega_{\rm FE}(\cdot,D\cdot)$, with weights $|\gamma|>0$. The form $\Omega_D:=B(\cdot,D^{-1}\cdot)$ has weights $\propto1/\gamma$. Pairing $\rho$ with $1-\bar\rho$, it is
  anti-Hermitian whether or not RH holds, and $B=\Omega_D(\cdot,D\cdot)$. The Williamson weights of $B$ relative to $\Omega_D$ are $|\gamma|$, the infinitesimal analogue
  of lane E's $\varepsilon_j\,\mathrm{Im}\,\alpha_j$. This is the Hilbert–Pólya statement in symplectic form. It is tautological, since $\Omega_D$ is built from $B$, just as $\Omega_+$ is built from the algebra in lane E.
- **The curve has the same feature** (*proved here*, one line). $\mathcal T$ is the Weil form of $\Omega_+$ for $F$. For $F^2$ it is not: $\tfrac12\Omega_+(F^2-V^2)=\tfrac12\Omega_+((F-V)(F+V))=\tfrac12\mathcal T(\cdot,(F+V)\cdot)$, with weights
  $\lambda_j$. For the genus-two curve these are 3.79 and $-0.79$, which is indefinite. The "Weil-form point" is attached to a generator of the step group. For $\zeta$ that generator is $D$, not a prime.

### 3.2 On a finite window (item 2)

**The window model** (checked B1–B4). The test functions live on $[0,L]$, $L=\log x$, with basis $e_n=e^{2\pi inu/L}/\sqrt L$, $|n|\le N$. $G_N$ is computed from the explicit formula
(pole, archimedean and prime parts; A2 validates the archimedean term). It equals the notebook's CCM window form, as computed by the reviewer helper, to $1.1\cdot10^{-12}$ (B1). On
the diagonal it exceeds the 3000-zero sum by less than the Riemann–von Mangoldt tail estimate (B3). The step is the normalised translation
$(U_ah)(u)=h(u-a)$, compressed: $M_N=P_N\chi_{[0,L]}U_a$. The multiplier is $1$; it is $2$ for the unnormalised dilation by 2.

| test | $x=13$ ($\log2/L=0.27$) | $x=100$ ($0.15$) | status |
|---|---|---|---|
| $\Omega_N=G_N(\cdot,D^{-1}\cdot)$ anti-Hermitian on mean-zero functions | to $2\cdot10^{-17}$ ($N=20$) | (same identity) | *checked* (B5) |
| best-$c$ residual of $M^TGM=cG$, whole window, $N=5,10,20,40,80,160$ | 0.40, 0.45, 0.47, 0.48, 0.47, 0.46 | 0.37, 0.40, 0.45, 0.44, 0.44, 0.43 | *negative finding* (D2) |
| low modes $\lvert n\rvert\le3$: distance of $M^TGM$ to the cut limit $W(\chi U_ae_m,\chi U_ae_n)$ | $2.6\cdot10^{-2}\to1.8\cdot10^{-3}$ | $1.7\cdot10^{-2}\to1.6\cdot10^{-3}$ | *checked* (D3) |
| best-$c$ residual of the cut limit (low modes) | 0.379 ($c=0.372$) | 0.395 ($c=0.393$) | *negative finding* (D3, D6) |
| #singular values of $M_N$ below $\tfrac12$ against $n\log2/L$ | 87 vs 86.7 ($N=160$) | 48 vs 48.3 | *checked* (D4) |
| residual at $c=1$ on four smooth functions supported in $[0,L-\log2]$, $N=20\dots160$ | $1.3\cdot10^{-6}\to5.5\cdot10^{-11}$ | $2.2\cdot10^{-3}\to7.9\cdot10^{-8}$ | *checked* (D5) |

Reading:

1. **The infinitesimal step is exact in truncation** (*checked*; the identity is the notebook's Loewner displacement, `notes/ccm-tensor-network/continuous.md` C3.2).
   On the kernel of the boundary covector, the displacement vanishes: $D^{-1}$ maps mean-zero window functions into the window. B4 shows that the
   identity holds term by term for each critical zero's rank-one form. It encodes squeeze invariance only, not positivity.
2. **A prime step is a similitude only away from the edge** (*checked*). On functions supported in $[0,L-\log p]$ the compressed dilation is an exact isometry in the
   limit $N\to\infty$, which is translation invariance surviving the compression. On the whole window the residual stays near 0.4 for every $N$ (*negative finding*).
   The low-mode block converges to a definite non-zero limit, the Weil form of the cut translates. That limit is an edge effect of size $O(1)$, not $O(\log p/L)$, because every Fourier mode
   carries the window's endpoint jumps. It does not decrease from $x=13$ to $x=100$ (D6).
3. **No finite window carries an integral step** (*checked*, D4; *proved here* for the lattice-of-bumps model). Each application of $M_N$ loses $n\log p/L$
   dimensions to within one. In a Toeplitz model on translates of a fixed bump, the compressed shift is nilpotent. Then $M^TGM=cG$ with $\det M=0$ forces
   $c=0$ or $\det G=0$, so no non-degenerate similitude form exists on any window. A finite-dimensional space invariant under translations consists of exponential polynomials,
   which are not test functions (*standard*, from memory). So the finite invariant subspaces live on the dual side, as the zero modes.

## 4. $\Pi_1$: the pole plane as the inverted-oscillator mode (item 3)

(*checked*, C1, at 40, 50 and 60 digits through the reviewer helper; the pole part comes from the closed form $F(0)F(1)^\dagger+F(1)F(0)^\dagger$, B2.)

| $x=13$ | $n$ | $\lambda_{\min}(Z_N)$ | inertia $Z_N$ | inertia $P_N$ | inertia $Z_N-P_N$ ($=-\mathrm{Loc}$) | inertia $Z_N+P_N$ |
|---|---|---|---|---|---|---|
| $N=5$ | 11 | $7.1\cdot10^{-17}$ | $(11,0,0)$ | $(1,1,9)$ | $(10,1,0)$, $\lambda_-=-5.842$ | $(10,1,0)$, $\lambda_-=-0.648$ |
| $N=10$ | 21 | $2.8\cdot10^{-26}$ | $(21,0,0)$ | $(1,1,19)$ | $(20,1,0)$, $-5.846$ | $(20,1,0)$, $-0.694$ |
| $N=15$ | 31 | $1.2\cdot10^{-33}$ | $(31,0,0)$ | $(1,1,29)$ | $(30,1,0)$, $-5.849$ | $(30,1,0)$, $-0.704$ |

- **Which form has the negative direction.** Weil's $Z_N$ is $P-\mathrm{Loc}$, so it includes the explicit formula's pole terms. It is positive definite, as RH requires.
  The single negative direction appears when the pole plane is counted against the zeros. With the Lefschetz sign it is $Z-P=-\mathrm{Loc}$ (analytic Prop. 7).
  With the same sign it is $Z+P$, which is lane E's $\tfrac12\Omega(M-V)$ on $H^0\oplus H^1\oplus H^2$ and `graph-ihara.md`'s $\mathcal Q$ including the uniform mode. Both
  have inertia $(n-1,1,0)$, since $P$ and $-P$ both have signature $(1,1)$. The brief's "with the pole terms kept" is ambiguous on this point. Read as $Z$, the count is zero.
- **Lane E's language** (*standard* reading). The unnormalised step has eigenvalues $a^0=1$ and $a^1=a$ on the two zero modes: the trivial pair, $\lambda=q+1>2\sqrt q$, hyperbolic.
  The Weil form of a hyperbolic pair has signature $(1,1)$ (lane E, X2). This gives one negative direction, with no Krein sign to choose.
- **Off-line pairs** (*checked*, C2). Adding a synthetic quartet $\{\rho,\bar\rho,1-\rho,1-\bar\rho\}$ to the zero form gives negative index 2 for $Z+Q$ and 3 for $Z+Q-P$.
  The quartets tested are $\rho=0.75+5i$ and $\rho=0.6+14.13i$, at $N=10$. The added $Q$ is an addition to the zero form; it is not consistent with the prime side. Each off-line pair $\{\rho,1-\bar\rho\}$ is a hyperbolic plane (`adelic-gkp.md` C6).
  So **the negative index is (pole plane) + (number of off-line pairs)**, the analogue of "(trivial eigenvalues) + (eigenvalues outside the band)".
- **Precision note** (*checked* in exploration, not a registered check). The window form has most of its spectrum near zero: 14 of 41 eigenvalues lie below $10^{-9}$ at $x=13$,
  $N=20$. Its positivity can be certified only at high precision; float64 data with quadrature error $10^{-12}$ cannot certify it.

## 5. Conclusion

1. (*standard*) $\zeta$ has the step and its adjoint exactly ($M_a=\delta_a*$, $V_a=aM_a^{-1}$ by the involution), and Weil's form $B$ is a similitude form with adjunction for every $a$ before RH.
2. (*proved in 04t*) $\zeta$ has a functional-equation pairing $\Omega_{\rm FE}$ compatible with the whole flow, but only on finite spans of zeros.
3. (*standard*) $\zeta$ has the explicit formula as its Lefschetz formula and a continuous step group with generator $D$.
4. (*proved here*) By Proposition 1, Weil's form is a lane-E Weil-form point exactly when the step is its similitude; for each prime this holds on the full algebra, but only with a prime-dependent, singular $\Omega_p$, and no single compatible $\Omega$ serves two primes.
5. (*checked*) With respect to $\Omega_{\rm FE}$ every prime step's Weil form is indefinite (weights $\sqrt p\sin(\gamma\log p)$), and Weil's form is the vacuum point, the analogue of lane C's shared $G_{J_K}$.
6. (*proved here*) Weil's form is the Weil-form point of the infinitesimal generator $D$ for $\Omega_D=B(\cdot,D^{-1}\cdot)$, with Williamson weights $|\gamma|$; this is the analogue of lane E's $\mathcal T=2W_{\Omega_+}$ for the generator $F$, and it is tautological.
7. (*checked*) In truncation only the infinitesimal step survives exactly (the Loewner identity), and a prime dilation is a similitude only on functions supported away from the window edge.
8. (*negative finding*) On the whole window the prime-2 residual stays near 0.4 for $N\le160$ and does not fall from $x=13$ to $x=100$, and each step loses $n\log p/L$ dimensions, so the finite probe undercuts "the prime dilations act as similitudes of the Weil form" as a statement about truncations.
9. (*negative finding*; *open*) $\zeta$ has no integral lattice, no integral step, no polarisation and no counts at $\infty$, and its vacuum $J$ exists only on zero spans under RH, which is the open statement.
10. (*checked*) On the window $Z_N>0$, $Z_N\mp P_N$ have exactly one negative direction (the pole plane), and each synthetic off-line pair adds one.

**Where this page qualifies earlier pages** (no edits made). `cone-bridge.md` §5 (ii) and `data-ladder.md` §4.2 read Weil's form for $\zeta$ as the
analogue of the Weil-form witness (*heuristic* there). §3.1 refines this. Relative to the pairing the notebook already has ($\Omega_{\rm FE}$), Weil's form is the vacuum point.
It is a Weil-form point only for the generator $D$, or for one prime at a time with a singular $\Omega_p$. The match $B\leftrightarrow\mathcal T$ of `analytic.md` §14
is consistent with this, because $\mathcal T$ is the Weil form for the generator $F$ only. Also, `notes/weil-bond-analytic/checks/metric_blocker_checks.py` imports
`scripts/rtp2_blind_recovery.py`, which uses `math.sumprod` (Python $\ge3.12$). It does not run on this container's Python 3.11.15. This page computes the pole part itself.

## 6. Status and checks

*Review 2026-10-06 (`notes/reviews/adelic-gkp-zeta-2026-10-06.md`, 6 VALID / 5 MINOR / 2 INVALID, both INVALIDs in the synthesis, none on this page):* G0, $F_h$ "(this is $\hat h(s)$)" is off by $s\mapsto s-\tfrac12$ from `analytic.md`'s $\hat h$ (§1.1 uses $\hat h$, §3.2 the normalised $h^\natural$). G3, "unaffected by normalisation" is false for "$B=G_J$": every positive form invariant under all steps is the vacuum form of some compatible $\Omega$ (04t `thm:bond-positive-metric-criterion`(d)), so "vacuum point" says that $B$ is invariant under the whole family and nothing more; indefiniteness, the singular weights and the absence of a common $\Omega_p$ are normalisation-independent.


*Citation correction 2026-10-06 (`notes/adelic-gkp/citations-2026-10-06.md`):* Connes's Theorem 1 (`math/9811068`) realises the critical zeros in the cokernel of a weighted space $L^2_\delta(C_k)$ with $\delta>1$, where the action is not unitary and multiplicities are capped at $n<(1+\delta)/2$; in plain $L^2(C_{\mathbb Q})$ there is no such statement (off-line zeros would appear as resonances). §§1–2 of this page say "$L^2$"; read $L^2_\delta$.


| statement | status | checks |
|---|---|---|
| zeros file; explicit formula with Weil's archimedean term, Gaussian tests to $4\cdot10^{-12}$ | checked | A1–A2 |
| $\tilde\delta_a=a\delta_{1/a}$, $V_a=aM_a^{-1}$; $B$ a similitude with adjunction for all $a$ | standard | none (one line) |
| window $G_N$ = notebook CCM form; pole part rank 2, signature $(1,1)$; zero side within the tail | checked | B1–B3 |
| Loewner identity per zero; $G_N(\cdot,D^{-1}\cdot)$ anti-Hermitian on mean-zero window functions | checked (identity: notebook C3.2) | B4–B5 |
| $Z_N>0$; $Z_N\mp P_N$ inertia $(n-1,1,0)$ at $N=5,10,15$ | checked (40–60 digits) | C1 |
| synthetic off-line quartet adds two negative directions | checked | C2 |
| prime-2 dilation: residual $\approx0.4$, not shrinking in $N$ or from $x=13$ to $100$; non-zero cut limit | negative finding; checked | D1–D3, D6 |
| singular-value defect $n\log2/L$; exact similitude away from the edge | checked | D4–D5 |
| no non-degenerate similitude for a nilpotent compressed shift (Toeplitz model) | proved here (one line) | none |
| Proposition 1 ($\Omega=2G(M-V)^{-1}$) | proved here; checked | E5 |
| compatible forms diagonal; prime-step Weil forms $\sqrt p\sin(\gamma\log p)$ indefinite for $\Omega_{\rm FE}$; $\Omega_p$ singular, $p$-dependent; no common $\Omega$ | proved here (spectral model); checked | E1–E3 |
| $B$ = vacuum point of $\Omega_{\rm FE}$; $B=\Omega_D(\cdot,D\cdot)$, Williamson weights $\lvert\gamma\rvert$ | proved here (given 04t); checked | E4 |
| curve: $\mathcal T$ is not the Weil form of $\Omega_+$ for $F^2$ (weights $\lambda_j$) | proved here (one line) | none |
| inventory cells quoted from lanes A, C, E, F, 04t, `adelic-gkp.md` | as on those pages | there |

`checks/check_zeta_ingredients.py`: **32 of 32 pass**, about 15 s.

## 7. Next

- Whether $\Omega_D=B(\cdot,D^{-1}\cdot)$, which is defined on the test algebra before RH (it needs only $\hat k(\tfrac12)=0$), has a description that does not
  pass through $B$. For example, a two-point pairing of the theta orbit, in the sense of `analytic.md` §14 (b).
- A smooth window basis (B-splines or prolates), in which the low modes do not carry the endpoint jumps. The question is whether the prime-step residual on the leading eigenvectors of $G_N$
  then decays like $\log p/L$. Here it was measured only on Fourier modes and on four hand-chosen functions.
- The CM analogue of §3.1: for $L(\psi,s)$, whether the global Weil form is the vacuum point of the global $\Omega_{\rm FE}$ while the local $J_K$ is shared. This would bring lane C's
  local/global split into the same table.