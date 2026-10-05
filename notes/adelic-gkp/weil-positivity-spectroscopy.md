# Weil positivity as squeeze spectroscopy of the adelic GKP code

Author: `claude:fable-5.1`, 2026-10-05, at TJO's request ("find a way for me to understand what weil positivity says in the most quantum info friendly way possible"). Status: **a record, not a round.** Nothing is registered in `db/claims.tsv`; no REFUTE review has run; no shard. Statement statuses are in the table near the end. Companion to `adelic-gkp.md`. Checks: `checks/check_weil_qi.py`, output `checks/output_weil_qi.txt`.

**Caveat added the same day.** TJO, after the graph pages: "I am not convincd by the overlap thing in the case of standard zeta." The overlap/filter reading of §1 is therefore not accepted as it stands. The method from here on is to find the QI interpretation on the cases where RH is understood (`graph-ihara.md`, `graph-super.md`, `lattice-tower.md`) and only then match it to the standard zeta. In particular `lattice-tower.md` §7 finds that in the understood case the zeros are oscillator frequencies of a positive Hamiltonian and the squeeze belongs to the poles, which differs from the squeeze-frequency reading below.

**The statement in one paragraph.** Squeeze the code and watch how the overlap of any probe with it changes. The code acts on these signals as a filter, and the frequencies it blocks are the zeros of $\zeta$: call them the dark lines. Weil's form $Z(h)$ is the weight a wavepacket $h$ puts on the dark lines. The explicit formula computes the same number place by place, without knowing where the lines are. **Weil positivity says that this place-by-place number always behaves like a quantum-mechanical weight: it is a squared norm, and the echo built from it is the autocorrelation function of a unitary evolution.** That holds exactly when every dark line is perfectly sharp, which is RH. A violation would be a gain–loss pair of modes under the squeeze. One such pair exists for a trivial reason (the two zero modes of the comb), and Weil positivity says there is no other.

Everything below is in the sector of probes that are invariant under the units $\hat{\mathbb Z}^\times$, which is the sector of $\zeta$. Conventions follow `notes/adelic-gkp/adelic-gkp.md`. The log-squeeze is $t=\log\lambda$, and a zero is written $\rho=\tfrac12+i\gamma$, so RH says every $\gamma$ is real.

## 1. The experiment: squeezing the code is a filter

Project the finite places onto their vacua. The code becomes the real comb $\sum_n\delta_n$ (Theorem 4 of the note at $N=1$). Take an even probe $g$ on $\mathbb R$ with no zero-mode content, $g(0)=0$ and $\int g=0$. Squeeze it by $e^t$ and record its overlap with half the comb:

$$
S_g(t)=e^{t/2}\sum_{n\ge1}g(n\,e^t).
$$

Let $G_g(t)=e^{t/2}g(e^t)$ be what a single tooth at $x=1$ would record. Then

$$
S_g(t)=\sum_{n\ge1}n^{-1/2}\,G_g(t+\log n),\qquad \widehat{S_g}(E)=\zeta(\tfrac12+iE)\,\widehat{G_g}(E),
$$

with $\hat f(E)=\int f(t)e^{iEt}dt$. So **the comb is one tooth passed through a linear time-invariant filter whose frequency response is $\zeta(\tfrac12+iE)$**, where "time" is the log-squeeze. (The series diverges on the line; the identity holds by continuation for probes without zero modes.)

In operator form, write the squeeze as $D_{e^t}=e^{itH}$ with $H=\tfrac12(xp+px)$. Then the filter is

$$
\sum_{n\ge1}n^{-1/2}D_n=\zeta(\tfrac12-iH)=\prod_p\bigl(1-p^{-1/2}D_p\bigr)^{-1}:
$$

each prime contributes a geometric ladder of squeezes by $p$. This is the real-place shadow of the vacuum $1_{\mathbb Z_p}$ at the place $p$.

**Dark lines.** A frequency $E$ at which the response vanishes is missing from the signal of every probe. For the simplest probe, $g_4(x)=e^{-\pi x^2}\bigl(x^2-\tfrac{2\pi}3x^4\bigr)$, the spectrum is exactly

$$
\widehat{S_{g_4}}(E)=-\frac{\Xi(E)}{6\pi},\qquad \Xi(E)=\xi(\tfrac12+iE),
$$

and for a general probe it is $\Xi(E)$ times an entire function. Check V1 confirms this at five frequencies to $10^{-13}$, and finds the signal's component at $\gamma_1=14.1347$ to be $3\times10^{-18}$, against $4\times10^{-5}$ one unit away.

A zero of $\Xi$ at a complex frequency blocks no real frequency. In filter terms RH asks whether all zeros of the response are real.

## 2. Weighing the dark lines

Take a wavepacket $h(t)$ in the log-squeeze, with $H(E)=\int h(t)e^{iEt}dt$. Weil's form and its echo are

$$
Z(h)=\sum_\rho H(\gamma_\rho)\,\overline{H(\bar\gamma_\rho)},\qquad C_h(t)=\sum_\rho H(\gamma_\rho)\,\overline{H(\bar\gamma_\rho)}\,e^{i\gamma_\rho t},\qquad C_h(0)=Z(h).
$$

$C_h(t)$ is Weil's form between $h$ and $h$ shifted by $t$. If every $\gamma$ is real these are

$$
Z(h)=\sum_\gamma|H(\gamma)|^2,\qquad C_h(t)=\sum_\gamma|H(\gamma)|^2e^{i\gamma t}:
$$

the weight of $h$ on the dark lines, and the beat signal of those lines.

(Relation to the note: its $h$ lives on $\mathbb R_+^\times$ with $\hat h(s)=\int h(x)x^s\,d^\times x$. Here $h(t)=e^{t/2}h_{\mathrm{note}}(e^t)$ and $H(E)=\hat h_{\mathrm{note}}(\tfrac12+iE)$.)

## 3. The same number, place by place

Let $g(u)=\int h(v+u)\overline{h(v)}\,dv$, so its transform is $G(E)=H(E)\overline{H(\bar E)}$. The explicit formula (Guinand–Weil; standard) says

$$
C_h(t)=\underbrace{G(\tfrac i2)e^{-t/2}+G(-\tfrac i2)e^{t/2}}_{\text{zero modes}}
-\sum_p\underbrace{\log p\sum_{k\ge1}p^{-k/2}\bigl[g(k\log p-t)+g(-k\log p-t)\bigr]}_{\text{place}\ p}
+\underbrace{\frac1\pi\int G(E)\,e^{iEt}\,\theta'(E)\,dE}_{\text{real place}} .
$$

Here $\theta$ is the Riemann–Siegel theta function, $\theta'(E)=\tfrac12\mathrm{Re}\,\psi(\tfrac14+\tfrac{iE}2)-\tfrac12\log\pi$. Stripping the wavepacket, the bare echo $C(t)=\sum_\rho e^{i\gamma_\rho t}$ is the distribution

$$
C(t)=2\cosh\tfrac t2-\sum_p\log p\sum_{k\ge1}p^{-k/2}\bigl[\delta(t-k\log p)+\delta(t+k\log p)\bigr]+A(t),\qquad \hat A(E)=2\,\theta'(E).
$$

Check V2 confirms the wavepacket form for three packets and up to nine values of $t$, to $10^{-12}$ or better.

| term | in the log-squeeze $t$ | what it is in the code |
|---|---|---|
| zero modes | $2\cosh(t/2)$ | The tooth at $q=0$ and its Fourier partner, the uniform background. A squeeze rescales them by $e^{\pm t/2}$: one gain mode and one loss mode, at the imaginary frequencies $\pm\tfrac i2$. |
| place $p$ | kicks of weight $\log p\,p^{-k/2}$ at $t=\pm k\log p$ | The trace of the squeeze on the $p$-adic mode, a fixed-point count at the origin (note §10). The $p$-adic mode only has squeezes by powers of $p$, so in frequency this term is periodic with period $2\pi/\log p$. |
| real place | a smooth kernel with spectral density $\theta'(E)/\pi\approx\tfrac1{2\pi}\log\tfrac E{2\pi}$ | The same trace on the real mode. $\theta$ is also the phase of the Hadamard gate in the squeeze eigenbasis: $F\,\lvert x\rvert^{-1/2+iE}=e^{2i\theta(E)}\lvert x\rvert^{-1/2-iE}$. So this density is a Wigner time delay. |

The finite analogue of "trace of a squeeze is a fixed-point count": on a qudit $\mathbb Z/N$ the Clifford $M_a\lvert x\rangle=\lvert ax\rangle$ is a permutation matrix, and $\mathrm{Tr}\,M_a=\#\{x:(a-1)x=0\}=\gcd(a-1,N)$.

**Why the primes appear as kicks.** On the code, squeezing the real mode by $p$ cannot be told apart from un-squeezing the $p$-adic mode by $p$, because the rational $p$ fixes the code (the product formula). So real squeezes by exactly $k\log p$ are the ones that the place $p$ can respond to.

![Dark-line density from the place-by-place formula. The real place and the zero modes give a smooth curve that is negative below E of about 6. Subtracting the places 2, 3, 5 and 7 produces oscillations that already peak near the zeros. Subtracting all finite places gives unit spikes at the zeros and zero in between.](fig_density.png)

*Figure 1. The dark-line density at resolution 0.47, computed from the place side only (primes up to $3\times10^6$). It matches the smoothed list of zeros to $4\times10^{-9}$.*

Two things to read off the figure:

- **The real place deposits a smooth background and the primes carve it into spikes.** Each prime redistributes density with zero mean in $E$.
- **The budget is spent exactly.** Between the lines the density is zero, not merely nonnegative. Near $E=0$ the real-place density is negative, and it is the zero-mode term that pays for it: for a packet at $E_0=2$ the zero modes contribute $+0.8817$ and the total is $2\times10^{-23}$ (V2).

## 4. What Weil positivity says

**Weil's criterion (cited):** RH holds if and only if $Z(h)\ge0$ for every wavepacket $h$. Since $Z(h)$ is given by the place-by-place formula, this is an inequality between explicitly known quantities.

The same statement in seven forms:

| form | statement | quantum-information reading |
|---|---|---|
| weight | $Z(h)\ge0$ for all $h$ | The dark-line weight of a wavepacket is a squared norm, an unnormalised probability. |
| echo bound | $\lvert C_h(t)\rvert\le C_h(0)$ for all $h$, $t$ | A return amplitude never exceeds the norm: a Loschmidt echo is at most 1. |
| Gram matrix | $[\,C_h(t_j-t_k)\,]_{jk}\succeq0$ for all $h$ and all times | The matrix of echoes is a Gram matrix of vectors, an unnormalised density matrix. |
| spectrum | the Fourier transform of $C$ is a positive measure | Phase estimation of the squeeze generator returns probabilities; here, unit spikes at the $\gamma$. |
| unitary dynamics | $C_h(t)=\langle\varphi_h\vert e^{itK}\vert\varphi_h\rangle$ with $K$ self-adjoint | The squeeze acts unitarily on the dark space. $K$ is the Hilbert–Pólya operator, and "the metric" is this inner product. |
| channel | the map $D_\lambda\mapsto C(\log\lambda)\,D_\lambda$ is completely positive | It is a mixture of conjugations by the unitaries $\lvert x\rvert^{i\gamma}$: the Kraus operators are the characters of the zeros. |
| response function | $\frac{\xi'}{\xi}(\tfrac12+w)=\int_0^\infty C(t)e^{-wt}dt$ has positive real part for $\mathrm{Re}\,w>0$ | A lossless Green's function or impedance: poles on the imaginary axis with positive residues. |

They are one statement. Positivity of a Hermitian form gives the echo bound by Cauchy–Schwarz, and the echo bound contains $Z(h)=C_h(0)\ge0$. The Gram, spectrum and unitary rows are Bochner's theorem and the GNS construction. The channel row is the standard fact that multiplication by a positive-definite function is completely positive on a group algebra; it is formal here because $C$ is a distribution with infinitely many lines. The response row is the Laplace transform of the spectrum row, and its place-by-place version is the identity

$$
\frac{\xi'}{\xi}(s)=\frac1s+\frac1{s-1}-\frac{\log\pi}2+\frac12\psi\!\left(\frac s2\right)-\sum_n\Lambda(n)\,n^{-s}
$$

(V5).

**What is true without RH.** The squeeze always preserves the Weil form: shifting both arguments by $s$ multiplies the contribution of each zero by $e^{i\gamma s}\overline{e^{i\bar\gamma s}}=1$. This is the functional equation at work, because the Hadamard symmetry pairs $\rho$ with $1-\bar\rho$. So the squeeze is always an isometry of a Hermitian form on the dark space. Weil positivity is the statement that this form is an inner product. That is the precise sense of "the metric".

Check V3 computes the Gram matrix from the place side only, for a wide packet centred at $E=25$: 14 by 14, eigenvalues in $[-10^{-14},\,5.5]$, and the echo stays below its initial value on $0\le t\le6$.

## 5. What a violation would look like

Suppose two neighbouring lines merged and left the axis as a pair $\gamma_0\pm i\eta$.

- **In the echo** the pair contributes one term decaying like $e^{-\eta t}$ and one growing like $e^{+\eta t}$: a gain–loss pair of modes.
- **In the weight** it contributes $2\,\mathrm{Re}\,z\bar w$ with $z=H(\gamma_0+i\eta)$ and $w=H(\gamma_0-i\eta)$ independent. This form has signature $(1,1)$: one direction of negative "probability".

There is a second way to count an off-line zero, and it is always positive: smear $\lvert H(E)\rvert^2$ over a Lorentzian of half-width $\eta$ centred at $\gamma_0$. The echo then decays like $e^{-\eta\lvert t\rvert}$, as for a line with dephasing, and it is a legitimate autocorrelation. This Lorentzian form is what Connes's cutoff construction produces in the limit (his Lemma 3, for function fields; analytic §4). The two forms agree exactly when $\eta=0$.

![Echo magnitude over initial value against log-squeeze. For zeta, computed from the place-by-place formula, the echo beats and stays at or below 1. With a made-up off-line pair counted by the Lorentzian form it decays. Counted by the Weil form it grows past 1.](fig_echo.png)

*Figure 2. A packet centred on $\gamma_4,\gamma_5$. Blue: the true echo from the place side. Orange and aqua: the same line list with $\gamma_4,\gamma_5$ replaced by the made-up pair $31.68\pm0.8i$.*

For the made-up pair the Gram matrix has smallest eigenvalue $-44.8$ in the Weil form and $+7\times10^{-4}$ in the Lorentzian form, and the Weil echo reaches 11.9 times its initial value by $t=4$ (V4).

So, in spectroscopic terms: **RH says every dark line of the code is perfectly sharp.** An off-line zero would be a line with a width, and Weil's form would register that width as a negative weight.

**The one pair that is allowed.** The zero modes are a gain–loss pair, with rates $\pm\tfrac12$ and signature $(1,1)$. Weil positivity says they are the only one. It is enough to test wavepackets with no weight on one of the two zero modes; on those the zero-mode term vanishes and the statement reads $-\sum_vW_v\ge0$, the sum of the local squeeze traces is a negative form (analytic §6, Proposition 7).

## 6. Why it does not come for free

Three arguments a quantum-information reader would try, and where each stops.

1. **"The squeeze is unitary on the mode, so its correlation functions are positive."** True, and it is the wrong correlation function. The squeeze correlations of the code's own signals have spectral density $\lvert\Xi(E)F(E)\rvert^2$, which is positive wherever the zeros are (analytic §3). The dark lines are where this density vanishes. They are not states of the mode; they are what is missing from it. $C(t)$ is the autocorrelation of the complement.
2. **"Then take all signals minus the producible ones; a trace over an orthogonal complement is positive."** Also true, at every finite cutoff (Connes; analytic §5). But the limit of those positive traces is the Lorentzian form of §5, not Weil's form. They agree only if no dark mode leaks through the edge of the cutoff, and that is equivalent to RH (function fields; for $\mathbb Q$ the trace formula itself is open).
3. **"Each place is its own mode with a unitary squeeze; add the places."** Each local term is the trace of a unitary on an infinite-dimensional mode: an infinite multiple of $\delta(t)$ plus a finite part. The explicit formula keeps the finite parts, with a minus sign. No single term has a sign: the prime terms oscillate, and the real-place density is negative below $E\approx6$. Positivity holds only for the sum, and Figure 1 shows it is saturated.

RTP round 2 met the same saturation from the other side: given the zero-mode and real-place terms, maximising positivity over nonnegative weights recovered the prime kicks (HANDOFF 2026-09-26).

For curves over finite fields the same form is positive for a structural reason: every place has a stabiliser vacuum, overlaps are counts, and the metric is the Rosati form (note §11). Over $\mathbb Q$ nothing yet plays that role.

## 7. Status of the statements and what was checked

| statement | status |
|---|---|
| filter identity, $g_4$ spectrum $=-\Xi/6\pi$ | standard (Tate, Riemann); checked V1 |
| explicit formula in echo form | standard (Guinand–Weil); checked V2 |
| Weil's criterion | cited in the notebook (`cit:weil-criterion`) |
| the seven forms are equivalent | standard (Cauchy–Schwarz, Bochner, GNS); the channel row is formal |
| $\mathrm{Re}\,\xi'/\xi>0$ right of the line is RH | analytic §2 (Lagarias 1999, not byte-cited); sampled in V5 |
| Hadamard phase $e^{2i\theta}$ at the real place | standard (Tate's local functional equation); gamma-factor identity checked V5 |
| Lorentzian form as the cutoff limit | cited from Connes for function fields (analytic §4); not established for $\mathbb Q$ |
| readings in the right-hand columns of the tables | reformulation; nothing here is a new theorem |

Checks: `checks/check_weil_qi.py`, 29 of 29 pass (numpy float64 with the notebook's 3000 zeros; mpmath for $\xi$ and $\theta$). Nothing is registered and no REFUTE review has run.

## 8. Three directions from here

- **The echo bound as an inequality on primes.** For a packet whose $g$ has width less than $t$, the echo at $t$ is the smoothed prime kicks plus a small real-place tail. The bound $\lvert C_h(t)\rvert\le C_h(0)$ then says the prime kicks are never louder than the real-place background. This is the form closest to an experiment.
- **Level $N$.** Restate the place-by-place formula on the Bell pair between the real qudit and the finite-adelic qudit, to see whether positivity has a finite-dimensional shadow there (the open question in note §12).
- **The channel form.** The explicit formula writes the dark-line multiplier as zero modes minus local multipliers. Ask which partial sums over places are completely positive on which wavepackets.
