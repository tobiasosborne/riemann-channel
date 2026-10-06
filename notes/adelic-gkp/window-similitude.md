# Is the prime-dilation residual an artefact of the window?

Author: `claude:opus-5.5`, 2026-10-06, lane R of an orchestrated session.

Status: **a record, not a round; nothing registered in db/claims.tsv; no REFUTE review; no shard.** Each statement is labelled *standard*,
*elementary*, *proved here*, *checked*, *heuristic*, *open* or *negative finding*. Carathéodory–Toeplitz and the simple-zero proportion are quoted
from memory. Checks: `checks/check_window_similitude.py`, output `checks/output_window_similitude.txt`, **25 of 25 pass**, about 30 s (numpy, mpmath;
`data/zeros3000.npy`).

The question. Lane G (`zeta-ingredients.md` §3.2, D2–D6) compressed the dilation $x\mapsto2x$ to the window $[0,L]$ (in $u=\log x$), using Fourier modes.
There $M^TGM=cG$ failed, with a best-$c$ residual near 0.4 that did not shrink with $N$ or from $x=13$ to $x=100$. `data-ladder.md` §4 item 2 uses this as a
negative finding: "in truncation only the infinitesimal step survives exactly". This page asks whether the residual comes from the hard cutoff or from the dilation itself.

**Findings.**

- **The dilation is exact; the residual is the cutoff** (*elementary*; *checked*, A2, B1–B10). Weil's form is invariant under every normalised translation
  $u\mapsto u+t$, before RH. On a window the defect sits on a fraction about $\log p/L$ of the space, in every basis.
  For a frame of translates the step is exactly a similitude on everything except the last $m$ elements. Lane G's 0.4 is a Frobenius norm. It
  equals, to within 0.04, the value of the same measure for the frame, where the similitude is exact away from the edge. It decays roughly like $(\log2/L)^{1/2}$.
- **The low-mode residual is the hard edge** (*checked*, B2, B4). On Fourier modes $|n|\le3$, lane G's own-block residual is 0.3–0.9 at every $L$ up to 32. On the first seven
  Hermite functions of a smooth window it is below $10^{-12}$.
- **The surviving finite structure is Toeplitz** (*elementary*; *checked*, C1–C4). The Gram matrix of translates $h(\cdot-j\log p)$ is Toeplitz. Being Toeplitz *is* the statement
  that the prime step is a similitude on the interior. Its entries are the notebook's windowed Weil form (the echo Gram matrix of `weil-positivity-spectroscopy.md`
  §4). From the prime side alone they come out to 13 digits for a Gaussian window, and to the accuracy of the truncated zero sum (1.6 digits raw, 2.8 after the smooth tail, at 1000 zeros) for the dyadic window $x\in[1,2]$.
- **What is missing is finite rank, not similitude** (*proved here* in the critical-zero model, given two cited facts; *checked*, C5). A curve's Toeplitz form
  has rank $2g$. $\zeta$'s has full rank on every window.
- **$\Omega_D$ without $B$** (*proved here*; *checked*, D1–D5). $\Omega_D(h,g)=B(h,H*g)$, where $H*g$ is the antiderivative. Its kernel is the odd function $K=C*\tfrac12\mathrm{sgn}$, with $K'=W$, Weil's distribution. The prime part of $K$ is the weighted
  Chebyshev staircase $-\sum_{n\le e^x}\Lambda(n)n^{-1/2}$. It is natural, and it carries no new datum.

---------------------------------------------------------------------------------------------------------------------

## 1. The translation is unitary for Weil's form

Conventions are lane G's (§1 there). $u=\log x$, $F_h(s)=\int h(u)e^{(s-1/2)u}du$, $B(h,k)=\sum_\rho F_h(\rho)\overline{F_k(1-\bar\rho)}$ (all nontrivial zeros), and
$(U_th)(u)=h(u-t)$. The normalised dilation by $p$ is $U_{\log p}$. The unnormalised one is $\sqrt p\,U_{\log p}$, with multiplier $p$.

**Proposition R1** (*elementary*). $B(U_th,U_tk)=B(h,k)$ for every $t\in\mathbb R$ and all test functions, with no hypothesis on the zeros.

*Proof.* $F_{U_th}(s)=e^{(s-1/2)t}F_h(s)$, so the $\rho$ term picks up $e^{(\rho-1/2)t}\,\overline{e^{(1/2-\bar\rho)t}}=1$. On the prime side the same holds, because the pair
function $(U_th)*(U_tk)^*=h*k^*$ does not change. ∎

In the model of this page (lane G §3.1) the sum runs over the first $K=1000$ critical zeros and $\hat h(\gamma)=\int h(u)e^{i\gamma u}du$, so
$Z_K(h)=\sum_{\pm\gamma}|\hat h(\gamma)|^2$ and $Z_K(U_th)=Z_K(h)$ term by term. Check A2 confirms this on a random smooth $h$ for $t=\log2,\log3,2\log5,0.37$, to $5\cdot10^{-16}$.

**Reconciliation with lane G** (*elementary*, with review G4). Lane G's $G_N$ is $B$ on $[0,L]$, and its step is the compression $M_N=P_N\chi_{[0,L]}U_{\log2}$.
- $U_{\log2}$ is $B$-unitary on all test functions. On the subspace of functions supported in $[0,L-\log2]$, which it maps into the window, it is an exact isometry (lane G D5).
- No non-zero finite-dimensional space of compactly supported functions is invariant under a translation, since the supports separate (review G4). So every finite truncation compresses.
  A compression of a unitary is a contraction. The defect of $M^TGM=cG$ therefore measures how much of the truncated space the step pushes out of the window.
- The defect is not a property of the step. Check B1 confirms that the 1000-zero model reproduces lane G's numbers, which were computed with the full explicit formula: 0.464 at $x=13$ and 0.433 at $x=100$ ($N=160$), the same to three digits.

## 2. The same question in three bases

Each basis spans a space $V$ of dimension $n$, with Gram matrix $A_{ij}=Z_K(b_j,b_i)$ and a compression $M$ of $U_{\log2}$. The diagnostics are:
- the best-$c$ residual $\|M^\dagger AM-cA\|_F/\|A\|_F$ (lane G's measure);
- the same residual on a low block;
- the **interior fraction**. Order the right singular vectors of $M$ (in an $L^2$-orthonormal basis) by how much mass leaks out of $V$, and take the largest $k$ for which the defect
  $R=M^\dagger AM-A$ on the first $k$ of them satisfies $\|R_k\|_2\le10^{-6}\|A\|_2$. The interior fraction is $k/n$.

The three bases:
- **(a)** Lane G's hard window: $e_m=e^{2\pi imu/L}/\sqrt L$ on $[0,L]$, $|m|\le N$, $n=2N+1$, with the exact $M=P\chi U$.
- **(b)** A smooth window: the Hermite functions $\psi_k(u/s)/\sqrt s$, $k<n$, which are a Gaussian times a polynomial. Their effective support is $|u|\le s\sqrt{2n}=:L/2$, and $M$ is the $L^2$-orthogonal compression.
- **(c)** A coherent-state frame: $g_j(u)=e^{-(u-j\delta)^2/2\sigma^2}$, with $\delta=\sigma=\log2/m$, $m=16$, $j<J=L/\delta$. Here $U_{\log2}g_j=g_{j+m}$, so the compressed step is
  the index shift $S$, which kills the last $m$ elements.

| $L$ | (a) $c$ / residual | (a) low $\lvert n\rvert\le3$ | (a) interior | (b) $c$ / residual | (b) low $k<7$ | (b) interior | (c) residual | (c) interior | $1-\log2/L$ |
|---|---|---|---|---|---|---|---|---|---|
| $\log13=2.56$ | 0.677 / 0.464 | 0.38 | 0.701 | 0.595 / 0.489 | $2\cdot10^{-15}$ | 0.636 | 0.499 | 0.729 | 0.730 |
| $\log100=4.61$ | 0.747 / 0.433 | 0.40 | 0.822 | 0.715 / 0.450 | $8\cdot10^{-16}$ | 0.785 | 0.444 | 0.849 | 0.849 |
| 8 | 0.835 / 0.369 | 0.93 | 0.891 | 0.805 / 0.396 | $1\cdot10^{-15}$ | 0.866 | 0.371 | 0.914 | 0.913 |
| 16 | 0.915 / 0.274 | 0.38 | 0.938 | 0.890 / 0.311 | $1\cdot10^{-14}$ | 0.925 | 0.279 | 0.957 | 0.957 |
| 32 | 0.957 / 0.190 | 0.30 | 0.963 | 0.943 / 0.234 | ($A_{\rm low}\approx0$) | 0.956 | 0.202 | 0.978 | 0.978 |

The columns (a) and (b) use $n=321$. Column (c) uses $n=J=59\dots739$. The low columns give lane G's best-$c$ residual on the block. For (b) at $L=32$, the first seven Hermite functions have bandwidth below $\gamma_1$, so their block of $A$ is about $10^{-29}$ and the ratio is noise. Measured against the whole form, that block's defect is below $10^{-12}$ at every $L$ for $n\ge321$ (B4). At $n=81$ the block's defect is $1.1\cdot10^{-6}$ at $L=\log13$, and $n=81$ at $L=32$ is excluded because its bandwidth, 7.9, is below $\gamma_1$. Going from $n=321$ to $n=641$ at $L=16$ changes the residuals by less than 0.01 (B9).

Reading:

1. **On the interior the step is exact, in every basis** (*checked*, B3, B5, B6).
   - In the frame (c), $S^TAS=A$ holds on the $(J-m)\times(J-m)$ interior block to $10^{-13}$, which is the Toeplitz property of $A$. The interior fraction is exactly $1-m/J=1-\log2/L$, and the $L^2$-orthogonal compression gives the same.
   - In (a) the interior fraction approaches $1-\log2/L$ from below, within 0.03 at $n=321$. The deficit is the transition region of a time–frequency concentration problem. It is the complement of lane G's D4 count of $n\log2/L$ lost singular values.
   - In (b) it follows the phase-space estimate $1-(4/\pi)\log2/L$ to within 0.03. A disc of radius $\sqrt{2n}$ shifted by $\log2/s$ loses that fraction (*heuristic*).
   - In all three the fraction tends to 1 like $1-O(\log p/L)$.
2. **The whole-space residual is the edge share, and it is the same in all bases** (*checked*, B7–B8; the explanation is *heuristic*).
   - The frame shift is an exact similitude on everything except the last $m$ elements. Its whole-space residual is still 0.499, 0.444, 0.371, 0.279, 0.202, which matches (a) to within 0.04 at every $L$.
   - So a residual near 0.4 at $L\approx3$–5 is what an *exact* similitude-away-from-the-edge produces under this norm.
   - It decays with $L$: residual$\cdot\sqrt{L/\log2}$ lies between 0.89 and 1.59 for $L$ from 2.6 to 32 in all three bases. Lane G's "does not shrink from $x=13$ to $x=100$" (0.464 to 0.433) is correct on that range, which is too short to show the decay. A plausible reason for the square root: $A$ has no off-diagonal decay, because the echo oscillates. So the $2m$ edge rows and columns hold a fraction about $2\log2/L$ of $\|A\|_F^2$.
3. **The low-mode residual is the hard edge** (*checked*, B2, B4).
   - Every Fourier mode of the hard window carries its endpoint jumps. On slowly varying modes those jumps are all of $Z$ (review G4). So the low block of (a) has no interior at all, and lane G's residual on it, the cut limit 0.38 of D3, stays at 0.3–0.9 for every $L$.
   - The low Hermite functions are interior, with residual $\le2\cdot10^{-15}$ relative to their block.
   - Lane G's §7 question has this answer: in a smooth basis the low modes are exact, while the whole-space residual is unchanged.
4. **The leading eigenvectors of the windowed form are not interior in either basis** (*checked*, B10). Their residual falls from 0.58 to 0.15 in (a) and from 0.55 to 0.10 in (b) over
   $L=2.6\dots32$. They fill the window, so they carry the edge share. This is the honest answer to lane G §7's "residual on the leading eigenvectors of $G_N$". It decreases with $L$, but not as a clean power.

## 3. The Gram matrix of translates is the windowed Weil form

Fix a window function $h$ and put $h_j=U_{j\log p}h$, $j=0..J$, with $\Gamma_{jk}=B(h_j,h_k)$.

**Proposition R2** (*elementary*). (i) $\Gamma_{jk}=\nu_{j-k}(h)$ with
$$\nu_d(h)=B(U_{d\log p}h,h)=\sum_\rho|\hat h(\gamma)|^2p^{i\gamma d}\quad(\text{critical zeros}),$$
so $\Gamma$ is Toeplitz. (ii) Let $S$ be the index shift ($Se_j=e_{j+1}$, $Se_J=0$). Then $S^T\Gamma S$ equals $\Gamma$ on the leading $J\times J$ block and differs only in the last row and column. (iii) (i) and (ii) are each equivalent to
$B(U_{\log p}h_j,U_{\log p}h_k)=B(h_j,h_k)$ for $j,k<J$. **The Toeplitz structure is the similitude property of the prime step on the span of the translates.** Lane G's remark (§3.2 item 3), that a nilpotent compressed shift admits no non-degenerate similitude form, concerns the full block including the last row and column. There is no conflict.

*Proof.* R1 with $t=\log p$. ∎

**Which notebook object this is** (*standard* readings).
- $\nu_d(h)$ is the echo $C_h(t)$ of `weil-positivity-spectroscopy.md` §2 at $t=d\log p$. The Gram matrix $[C_h(t_j-t_k)]$ of check V3 there (and of `cm-lift.md`) is $\Gamma$ on the grid $t_j=0.35j$.
- For a curve, 08b's Weil form $\sum c_l\bar c_k\nu_{l-k}$ (`registered-record.md` §2.3) has the same shape, with $\nu_\ell$ the rescaled Frobenius traces. Here $\nu_d(h)$ is the $|\hat h|^2$-weighted trace of $S_p^d$, with $S_p=p^{-1/2}M_p$, on the zero modes.
- On the prime side, $\nu_d=$ pole $+$ arch $-\sum_n\Lambda(n)n^{-1/2}[g(\log n-d\log p)+g(-\log n-d\log p)]$ with $g=h*h^*$. For $g$ concentrated near 0, the prime term at $d\ge1$ is dominated by
  $n=p^d$, giving $-\log p\,p^{-d/2}g(0)$: the local Lefschetz trace of the $d$-th power.
- The dyadic window $h=1_{[0,\log2]}$ (that is, $x\in[1,2]$) has translates $1_{[2^j,2^{j+1}]}$. So $\Gamma$ is the CCM window form of $x=2^{J+1}$, restricted to dyadic step functions.

**Numerical match** (*checked*, C1–C4; $p=2$, $J=8$).

| window | entries | zero sum ($K$ zeros) against the explicit formula (pole $-$ primes $-$ archimedean, no zeros) | digits |
|---|---|---|---|
| Gaussian, $\tau=0.1$ | $\nu_0,\nu_1,\nu_2=1.881161\cdot10^{-2},\,-1.650444\cdot10^{-2},\,1.130336\cdot10^{-2}$ | max relative difference $1.1\cdot10^{-14}$ at $K=1000$ | 13 |
| dyadic $1_{[0,\log2]}$, $\nu_0=0.12711$ | $d=0$: raw $5.0,\,3.1,\,1.4\cdot10^{-3}$; minus the smooth Riemann–von Mangoldt tail $3.8,\,2.2,\,0.88\cdot10^{-4}$ ($K=500,1000,3000$) | $d\ge2$: raw $3.5,\,1.5,\,0.34\cdot10^{-5}$ | 1.6 raw, 2.8 after the tail ($K=1000$) |

The zero-sum $\Gamma$ is Toeplitz to $8\cdot10^{-15}$ (C1). The $9\times9$ Toeplitz matrices built from the prime side alone are positive definite, with eigenvalues in $[3.3\cdot10^{-8},\,0.082]$
for the Gaussian and $[1.4\cdot10^{-3},\,0.303]$ for the dyadic window (C4). For the dyadic window the error that remains after the tail is the fluctuating part of the zero count, and it shrinks with $K$.

**Proposition R3** (rank; *proved here* in the critical-zero model, given two facts quoted from memory). Let $h$ be such that $\hat h(\gamma)\ne0$ at every zero (a Gaussian, say). Then $\Gamma$ has full rank $J+1$ for every $J$. For a curve of genus $g$, the corresponding Toeplitz form has rank $2g$ on every window of length $\ge2g$.

*Proof.* The symbol of $\Gamma$ is the positive measure $\mu=\sum_\gamma|\hat h(\gamma)|^2\delta_{\gamma\log p\bmod2\pi}$. A positive Toeplitz form has rank $r<J+1$ only if $\mu$ has
$r$ atoms (Carathéodory–Toeplitz, *standard*). Then all ordinates would lie in $r$ residue classes mod $2\pi/\log p$, which contain $O(rT)$ points up to $T$. But a positive proportion of zeros are simple
(Levinson, Conrey; from memory), so there are $\gg T\log T$ distinct ordinates up to $T$. For the curve, $\nu_\ell=\sum_{j=1}^{2g}e^{i\ell\theta_j}$ has $2g$ atoms. ∎ Check C5 finds rank 4 for a synthetic genus-two sequence and 9 of 9 for both $\zeta$ windows.

So the prime step survives truncation as the Toeplitz shift. What it has no counterpart of is the curve's finite quotient: the kernel quotient of the curve's form is $H^1$, of rank $2g$, on which $F$ acts by an integer matrix. For $\zeta$ the
Toeplitz form has an atom for every zero, so there is no finite lattice for the shift to act on.

## 4. $\Omega_D$ as a pairing on test functions

Lane G defines $\Omega_D=B(\cdot,D^{-1}\cdot)$ with $D=d/du$, on $g$ with $\int g=0$ (lane G's $\hat k(\tfrac12)=0$). In the model, $(Dh)^\wedge(\gamma)=-i\gamma\hat h(\gamma)$.

**Proposition R4** (*proved here*, elementary; *checked*, D1–D4).
- (a) For $\int g=0$, the antiderivative $D^{-1}g=H*g=\tfrac12\mathrm{sgn}*g$ ($H$ the Heaviside function) is the unique compactly supported one, and $\Omega_D(h,g)=B(h,H*g)$.
- (b) In the zero-sum model, $\Omega_D(h,g)=\sum_{\pm\gamma}\hat h(\gamma)\overline{\hat g(\gamma)}/(i\gamma)=\iint h(u)\overline{g(v)}K(u-v)\,du\,dv$ for every $g$, where
  $$K(x)=\sum_{\gamma>0}\frac{2\sin\gamma x}{\gamma}=\bigl(C*\tfrac12\mathrm{sgn}\bigr)(x),\qquad C(x)=\sum_{\pm\gamma}e^{i\gamma x}.$$
  This kernel is the antisymmetric part of convolution with $H$ (the symmetric part $\tfrac12$ is annihilated by $\int g=0$), projected on the zero spectrum by $C$. $K$ is odd and real, so $\Omega_D$ is anti-Hermitian.
- (c) For Weil's full form, (b) holds in the form (a). The pole part $2\cosh(x/2)$ of Weil's distribution $W$ cannot be convolved with $\mathrm{sgn}$ on its own. It is paired with the compactly supported $H*g$.

*Proof.* $\widehat{H*g}=i\hat g/\gamma$ for $\gamma\ne0$, and $\overline{i/\gamma}=1/(i\gamma)$. Also $\int\tfrac12\mathrm{sgn}(w)e^{-i\gamma w}dw=1/(i\gamma)$. ∎

The checks use $h=e^{-u^2/2\tau^2}\sin15u$ and $g=e^{-(u-0.3)^2/2\tau^2}\sin(22(u-0.3))$ with $\tau=0.2$.
- The zero sum gives $\Omega_D=1.664480653814\cdot10^{-3}$.
- The kernel integral and $Z_K(h,H*g)$ (antiderivative by the complex error function) agree with it to $10^{-15}$ (D1, D2).
- The explicit formula applied to the pair function of $h$ and $H*g$, from primes, poles and the archimedean term only, agrees to $1.2\cdot10^{-17}$ (D3).
- $\Omega_D(h,g)+\Omega_D(g,h)=2\cdot10^{-18}$, computed from the prime side alone (D4). This is lane G's Loewner identity (B5), on the line instead of the window.

**Proposition R5** (*standard*: the explicit formula for $\psi$, integrated; *checked*, D5). $K'=W$. So for $0<x_1<x_2$,
$$K(x_2)-K(x_1)=\Bigl[4\sinh\tfrac x2\Bigr]_{x_1}^{x_2}-\sum_{x_1<\log n<x_2}\frac{\Lambda(n)}{\sqrt n}-\int_{x_1}^{x_2}\frac{dx}{e^{x/2}-e^{-3x/2}} .$$
The prime part of $K$ is minus the weighted Chebyshev function $\psi_{1/2}(e^x)=\sum_{n\le e^x}\Lambda(n)n^{-1/2}$. D5 tests this between $\log2.5$ and $\log34.5$. The staircase increment there is 8.5694. The zero side, Gaussian-smoothed at $\sigma=0.005$, and the prime side differ by $2.2\cdot10^{-5}$.

**Reading.** $\Omega_D$ is natural:
- $B$ pairs through the von Mangoldt kicks, and $\Omega_D$ through their counting function. This is the position–momentum pair $B=\Omega_D(\cdot,D\cdot)$.
- It is compatible with every step at once, because $H*$ commutes with translations.

For the data ladder:
- It gives review S2b's "$\Omega_D$ on the test algebra" an explicit prime-side kernel, so $\Omega_D$ can be described through $\psi$ rather than through $B$.
- It adds no datum. It is $B$ composed with the canonical antiderivative, and its antisymmetry is the Loewner identity, which holds before RH.
- It carries no lattice and no reason for positivity.

## 5. Conclusion

1. (*elementary*) Weil's form is invariant under every normalised translation $u\mapsto u+\log p$, before RH, on both sides of the explicit formula. The prime dilations are exact similitudes, with multiplier $p$ unnormalised.
2. (*checked*) Lane G's residual near 0.4 is a cutoff effect. In the frame of translates, the same norm gives the same number to within 0.04 although the step is exact on all but $\log2/L$ of the space. The residual decays roughly like $(\log2/L)^{1/2}$.
3. (*checked*) In all three bases the interior, where the defect is below $10^{-6}$, has fraction $1-O(\log2/L)$: exactly $1-\log2/L$ for the frame, $1-\log2/L-0.03$ for the hard window, and about $1-(4/\pi)\log2/L$ for Hermite functions.
4. (*checked*) The O(1) residual on low Fourier modes is the hard edge. On low Hermite modes it is below $10^{-12}$.
5. (*elementary*) What survives truncation is the Toeplitz structure of the Gram matrix of translates, which is exactly the similitude of the step on its interior. That matrix is the notebook's windowed Weil (echo) form.
6. (*checked*) Its entries computed from the zeros match the prime side to 13 digits (Gaussian window) and to 1.6 digits raw, 2.8 after the smooth tail (dyadic window, 1000 zeros).
7. (*proved here*, given Carathéodory–Toeplitz and a positive proportion of simple zeros) The difference from the curve is rank. The curve's Toeplitz form has rank $2g$ and its quotient is the integral $H^1$. $\zeta$'s has full rank on every window, so there is no lattice for the shift to act on.
8. (*proved here*; *checked*) $\Omega_D(h,g)=B(h,H*g)$ has the odd kernel $C*\tfrac12\mathrm{sgn}$, whose prime part is the weighted Chebyshev staircase. It is natural and adds no datum.

**Replacement sentence for `data-ladder.md` §4 item 2.** This replaces "In the window the compressed dilation by 2 is a similitude of the Gram form only on functions supported away from the edge; on the whole window the residual stays near $0.4$ for $N\le160$ and $x\le100$ (*negative finding*)", and lane G's summary "in truncation only the infinitesimal step survives exactly". The file is not edited here.

> In a window the prime steps survive exactly as the Toeplitz shift. Weil's form is invariant under every translation $u\mapsto u+\log p$ before RH, so the Gram matrix of the translates $h(\cdot-j\log p)$ is Toeplitz, and the compressed step is an exact similitude on all but a fraction $O(\log p/L)$ of any window basis (exactly so for a frame of translates). Lane G's residual near $0.4$ is that edge share in the Frobenius norm, and it decays roughly like $(\log p/L)^{1/2}$ (`window-similitude.md`). What the prime steps lack is not similitude but a finite-rank integral structure: $\zeta$'s Toeplitz form has full rank on every window, one atom $\gamma\log p$ mod $2\pi$ per zero, where a curve's has rank $2g$, so there is no lattice for the shift to act on.

## 6. Status and checks

| statement | status | checks |
|---|---|---|
| $B(U_th,U_tk)=B(h,k)$ for all $t$, before RH; $Z_K$ invariant | elementary; checked | A2 |
| closed forms (hard-window transforms and $M$; Hermite transforms) | checked | A3–A4 |
| 1000-zero model reproduces lane G's 0.464 / 0.433 | checked | B1 |
| low Fourier modes: residual O(1) at every $L$ (hard edge); low Hermite modes $<10^{-12}$ | checked | B2, B4 |
| interior fraction $\to1$ as $1-O(\log2/L)$ in (a), (b), (c); exact in (c) | checked (phase-space constant $4/\pi$ heuristic) | B3, B5, B6 |
| whole-space residual = edge share, same in all bases, $\approx(\log2/L)^{1/2}$ | checked; the square-root explanation heuristic | B7–B9 |
| leading eigenvectors of the windowed form not interior | checked | B10 |
| Gram matrix of translates Toeplitz $\Leftrightarrow$ step a similitude on the interior (R2) | elementary; checked | C1 |
| Toeplitz entries from zeros = prime side (13 digits Gaussian; dyadic within the zero-sum tail) | checked | C2–C3 |
| prime-side Toeplitz matrices positive definite | checked | C4 |
| full rank for $\zeta$, rank $2g$ for a curve (R3) | proved here (model; two facts from memory); checked | C5 |
| $\Omega_D=B(\cdot,H*\cdot)$, kernel $C*\tfrac12\mathrm{sgn}$ (R4) | proved here; checked | D1–D2 |
| $\Omega_D$ from the prime side; antisymmetry from the prime side | checked | D3–D4 |
| $K'=W$; prime part of $K$ the weighted Chebyshev staircase (R5) | standard; checked | D5 |

`checks/check_window_similitude.py`: **25 of 25 pass**, about 30 s.

## 7. Next

- Repeat section 2 with the full Weil form (lane G's explicit-formula $G_N$) in the Hermite basis. R1 predicts the same interior fractions. This was not run here, because the brief asked for the zero sum.
- For two primes at once, the translates by $j\log2+k\log3$ give a two-level Toeplitz matrix whose symbol lives on the line $\gamma\mapsto(\gamma\log2,\gamma\log3)$ in the torus. Whether anything finite-rank survives for the family is *open*.
- Annotate lane G §3.2 reading 2 and §5 item 8 (the "negative finding") with a pointer to this page. That is a decision for the orchestrator; no existing note was edited.
