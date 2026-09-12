# Weil positivity for an arbitrary transfer operator

Author: claude:fable-5.1 (orchestrator). Date: 2026-09-12. Proofs of the
theorems: `notes/weil-positivity/astra-proofs.md` (codex:gpt-6-astra, brief in
`notes/weil-positivity/astra-brief.md`). Review:
`notes/reviews/weil-positivity-2026-09-12.md` (claude:opus). Numerics:
`scripts/weil_positivity.py`, `outputs/weil_positivity.txt`. Sources with
byte-cited quotes: `notes/extract/weil-positivity-sources.md`. Lab-book
distillation: `report/sections/08b_weil_positivity.tex`.

## The question

The reflection $\rho \mapsto 1-\bar\rho$ pairs the mode of the Riemann channel
at a zero with the mode at its mirror image; RH says every mode is its own
partner; Weil's criterion says RH holds iff the pairing form
$\sum_\rho \hat g(\rho)\overline{\hat g(1-\bar\rho)}$ is nonnegative, and the
explicit formula writes that form on the primes. What does this mean for a
completely arbitrary Kraus family, discrete or continuous?

## The answer in three layers (statements in the shard, proofs in astra-proofs.md)

1. **No duality.** For any finite-dimensional $X$, trivial set $S$ and
   radius $r$, the rescaled sequence $\nu_\ell = r^{-\ell}(\operatorname{Tr}X^\ell -
   \sum_S \mu^\ell)$ is positive definite iff $|\mu| \le r$ off $S$ (T1.3).
   Positivity is the spectral-gap half of RH, nothing more: modes inside the
   disc pass (Poisson kernel).
2. **A duality.** If the retained multiset is invariant under
   $J(\mu) = r^2/\bar\mu$, the Weil form equals the mode-pairing form,
   $W(c) = M(c) = \sum_\mu f_c(\mu/r)\overline{f_c(J\mu/r)}$ (the finite inflow
   identity), and positivity is equivalent to every mode being $J$-fixed, i.e.
   on the circle (T2.1). An off-circle pair makes the form negative (T2.2).
3. **Kraus families.** Any $\mathrm{Ad}$-family has nonnegative ring traces and
   a conjugation-closed spectrum (T3.1; the adjoint pairing was never needed
   for either). Inverse pairing $B_{\bar i} = B_i^{-1}$ gives the functional
   equation $\mu \mapsto (D-1)/\mu$ (T3.2). Adjoint pairing gives Hilbert-Schmidt
   self-adjointness of $\Sigma$. Both iff unitary (T3.3). Unitary case: Weil
   positivity iff Hastings' bound (T3.4). Continuous case: Bochner in place of
   Herglotz, Dyson-expansion ring norms (T4). Hilbert-Polya inner product iff
   semisimple on the circle; positivity is blind to Jordan blocks (T5).

## Observation X1 (Huang's criterion is the boundedness form)

Setting: $A$ a finite multiset in $\mathbb C$, $z_\mu = \mu/r$, $\nu_\ell =
\sum_{\mu \in A} z_\mu^\ell$ for $\ell \ge 0$, $\nu_{-\ell} = \bar\nu_\ell$.

Claim: the following are equivalent. (i) $\nu$ is positive definite.
(ii) $\nu$ is bounded. (iii) $\operatorname{Re}\nu_\ell \le \nu_0$ for all $\ell \ge 1$, for $A$ closed
under complex conjugation (and (iv) $|\nu_\ell| \le \nu_0$ in general).

Proof. (i) ⇒ (ii): the $2\times 2$ Toeplitz minor $\nu_0^2 - |\nu_\ell|^2 \ge 0$.
(ii) ⇒ all $|z_\mu| \le 1$: this is the growth lemma of T1.2 (the modes of
maximal modulus $R > 1$ contribute $R^\ell$ times a trigonometric polynomial
whose mean square over $\ell < L$ tends to the sum of the squared multiplicities,
so $|\nu_\ell| \ge \frac12 R^\ell (\sum m_j^2)^{1/2}$ for infinitely many $\ell$).
All $|z_\mu| \le 1$ ⇒ (i): T1.3. (i) ⇒ (iii): $\operatorname{Re}\nu_\ell \le |\nu_\ell| \le \nu_0$.
(iii) ⇒ (ii): let $R = \max|z_\mu| > 1$ and $\zeta_j = z_j/R$ the phases of the modes of
maximal modulus, multiplicities $m_j$. The closure of $\{(\zeta_j^\ell)_j\}$ in the torus is a
compact group, so infinitely many $\ell \ge 1$ have $\max_j|\zeta_j^\ell - 1| < \delta$, and for
those $\operatorname{Re}\nu_\ell \ge \tfrac12(\sum_j m_j)R^\ell - o(R^\ell) \to \infty$,
contradicting (iii). (The reviewer supplied this step; the orchestrator's draft had tried
to arrange $\cos(\ell\theta) \le 0$ for most $\ell$, which cannot happen.)
Huang's $h_k = 2(n-1) + q^{k/2} + q^{-k/2}
- q^{-k/2}N_k$ for a $(q+1)$-regular graph is $\nu_0 - \nu_k$ for the
retained multiset (trivial poles $\pm 1$, $\pm q^{-1}$ removed), and that
multiset is both conjugation-closed and reciprocal-invariant, so there
$h_k \ge 0$ for all $k$ is (iii) and is equivalent to Weil positivity.

Status: proved (author claude:fable-5.1, reviewer claude:opus, VERDICT X1: VALID); the
reviewer also verified $h_k = \nu_0 - \nu_k$ to $10^{-13}$ on $K_4$, Petersen, $K_5$ and a
non-Ramanujan ladder.

## Observation X2 (the Kraus dichotomy)

For any family $\mathcal E_i = \mathrm{Ad}(B_i)$: rings positive and spectrum
conjugation-closed (T3.1 and Corollary 2 of the general Ihara-Bass note).
Inverse pairing: the retained multiset is invariant under $\mu \mapsto q/\mu$
and under conjugation, hence under $J$ with $r = \sqrt q$ (T3.2), so by T2.1
Weil positivity is equivalent to every retained $\mu$ on the circle
$|\mu| = \sqrt q$. Since the retained $\mu$ are the roots of
$\mu^2 - \alpha\mu + q$ over the eigenvalues $\alpha$ of $\Sigma$, and the two
roots of that quadratic lie on $|\mu| = \sqrt q$ iff $\alpha = 2\sqrt q\cos\theta$
is real with $|\alpha| \le 2\sqrt q$, the criterion reads: every nontrivial
eigenvalue of $\Sigma$ is real with $|\alpha| \le 2\sqrt{D-1}$. Adjoint
pairing makes $\Sigma$ Hilbert-Schmidt self-adjoint, so the reality is free
and only the bound remains (T3.4). Both pairings iff unitary (T3.3), so (c) is
not an extra hypothesis on top of (b): (b)+(c) is (d). In the unitary case the
eigenvalue $\alpha = D$ of $\Sigma$ (from $\Phi(1) = 1$) always violates the band
$|\alpha| \le 2\sqrt{D-1}$, so (b) must be applied with the enlarged trivial set of T3.4
(the pairs $\{q,1\}$ and $\{-q,-1\}$ removed once per eigenvalue $\pm1$ of $\Phi$); the
reviewer flagged this qualifier as mandatory. Likewise $\operatorname{spec}(T)$ need
not be real for adjoint-paired families, but can be (T3.5's family has sixteen real
modes and no duality). So: reality of
$\operatorname{spec}(\Sigma)$ (not of $\operatorname{spec}(T)$, which stays
non-real; the Hilbert-Polya half) comes from the adjoint pairing, the functional equation from the inverse pairing, and a
channel that is unitary gets both, which is why Hastings' bound alone is RH
there. A concrete inverse-paired non-unitary family with real $\Sigma$-spectrum:
$B_i = G U_i G^{-1}$ with unitary $U_i$ and a common invertible $G$; then
$\Sigma = \mathrm{Ad}(G)\,\Sigma_U\,\mathrm{Ad}(G)^{-1}$ is similar to the
self-adjoint $\Sigma_U$, its spectrum is real, and the bound holds iff it holds
for the unitary family. The reviewer checks this construction and a family
with non-real $\Sigma$-spectrum (X2 in the review file).

Status: proved after the MINOR wording fix (VERDICT X2); the reviewer confirmed the
$G U_i G^{-1}$ construction (band iff Weil positivity, 6/6) and that random inverse-paired
families have non-real $\Sigma$-spectrum.

## What is and is not established

Established (proved, two families): T1.3, T2.1-T2.3, T3.1-T3.5, T4.2-T4.4,
T5.1-T5.3, subject to the review verdicts. Sketched: the zeta dictionary entry
(T6). X1 and X2 proved after review. Not established: anything about zeta; the infinite-dimensional
converse (Weil's) is cited, not reproved.
