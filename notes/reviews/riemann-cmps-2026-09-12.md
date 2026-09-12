# Adversarial review: `notes/riemann-cmps/astra-proofs.md`

- **Date:** 2026-09-12
- **Reviewer:** claude:opus (REFUTE lane)
- **Author under review:** codex:gpt-6-astra
- **File under review:** `notes/riemann-cmps/astra-proofs.md` (1356 lines; labels T1.1–T1.4, T2.1–T2.4, T3.1–T3.3, T4.1–T4.3, T5.1–T5.5, T6.1–T6.5, T7.1–T7.10, T8.1, the H-* inventory and the T8 ledger)
- **Also adjudicated:** three statements X1, X2 (a–d), X3 proposed by the orchestrator (claude:fable-5.1)
- **Independent numerics:** six scratch scripts `notes/reviews/scratch_rcmps_*.py`, written from the **statements** only. No code was reused from `scripts/` — the finite-field arithmetic, the normal basis, the Artin–Schreier transfer matrix, the radical determinant, the centred Weyl operators, the Lindbladian superoperator, the M/M/1 Jacobi matrix, the Mertens sums and the explicit-formula test were all coded from scratch here. Where a result coincides with `outputs/artin_schreier_super.txt`, `outputs/riemann_graded_trace.txt` or `outputs/bc_entropy.txt`, it is an independent confirmation, not a re-run.

**Headline.** I could not break any labelled statement. Every sign, factor of two, multiplicity, Jacobian, interchange of limits and domain caveat I attacked survived, and in the one place where the numerics lane had falsified the brief's drafted law (`q=3, a=(2,1)` and `q=5, a=(0,1,1)`) the prover's corrected law **T7.3/T7.4** and the endpoint criteria **(7.7)/(7.8)** reproduce the failures and the passes exactly — 12/12 coefficient tuples, including the two FAIL cases, in my own independent implementation. The explicit symplectic map **(7.13)** reproduces the numerics lane's extracted `M` entry for entry in all ten cases, and in the *centred* Weyl convention the covariance is exact with **no residual phase** (max residual `7.6e-16` over all `q^{2J}` labels), which is precisely the sharpening astra imposed on H-WEIL-REP. The rederived trace identity `Tr_dist Z(t) = 1 - 2P_+ - e^{-t/2}/(e^t-1)` matches a 260-zero Gaussian-smeared computation to `1.3e-05` relative, and each of the three plausible wrong variants (sign flip, factor 1 instead of 2, `+A` instead of `-A`) is rejected by three to four orders of magnitude.

Five MINOR findings, no INVALID. One of them (T2.3) is a **strengthening**: half of the conclusion does not need the domination premise, and I supply the proof. Two are on the orchestrator's own statements (X1, X3), one on a constant (X2a), and one is a provenance gap in an H-* (H-BC-POS) which the sources file itself already flags.

---

# T1. Distributional rigidity

## T1.1 — existence of the supertrace distribution

**Claim.** Under (G1),(G2) the series `sum eps m e^{lambda t}` converges absolutely against every `phi in C_c^inf(0,inf)` and defines a distribution; the tested sum is order-independent.

**What I attacked.** The integration-by-parts bound. The draft's version (flagged in the ledger) used only `Im lambda`; astra's replacement integrates by parts in the full complex `lambda` and bounds `|e^{lambda t}| <= max(e^{ca}, e^{cb})` on `supp phi subset [a,b] subset (0,inf)` — which is the point, because for *very negative* `Re lambda` the naive derivative bound on `e^{(Re lambda) t}` is not uniform, while `|e^{lambda t}|` on a compact subset of the open half-line is. The estimate `|int e^{lambda t} phi| <= C (1+|lambda|)^{-p} (||phi||_inf + ||phi^{(p)}||_inf)` with `p >= N` then sums by (G2). No boundary terms, because `supp phi` is compact *in the open half-line* — this is why the theorem is stated on `(0,inf)` and not `[0,inf)`.

**Is (G2) enough?** Yes, and it is satisfied by the zeta multiset. Riemann–von Mangoldt gives `N(T) ~ (T/2pi) log(T/2pi e)`, so `sum_rho (1+|rho|)^{-N}` diverges like `log^2 T` at `N = 1` and converges for `N >= 2`; astra takes `N = 3`, which is safe. I integrated the Stieltjes measure `(log(T/2pi)/2pi) dT` against `(1+T)^{-N}` to `T = 1e7` (`scratch_rcmps_t1t2t4.py`, part B) and got `16.16` (still growing) at `N=1`, `0.0195` at `N=2`. So polynomial zero density is exactly what (G2) is for and it suffices.

**VERDICT T1.1: VALID**

## T1.2 — rigidity up to cancelling pairs

**Claim.** Two graded data with the same supertrace distribution on `(0,inf)` have the same net multiplicity at every `lambda`.

**What I attacked.**
1. *Legitimacy of the non-compact test.* The brief asked to pair with `t^k e^{-st}`, which a distribution on the open half-line does not act on. Astra's cutoff `h_{eps,R,s}(t) = chi(t/eps) eta(t/R) t^k e^{-st}` is genuinely in `C_c^inf(0,inf)`, so the pairing is defined, and **the same cutoffs are used for both distributions** — this is the step that makes the comparison legal rather than assumed. I implemented the cutoffs and the limit numerically for an 8-mode datum with `k=4, s=3`: `0.7404186937` against the exact `k! sum nu (s-lambda)^{-(k+1)} = 0.7404186937`, relative error `1.4e-14`.
2. *The `eps` bookkeeping.* The claim that a term carrying `j` derivatives on `chi` and `l` on `t^k` is `O(eps^{k-l-j+1})` with nonnegative exponent because `l+j <= k+1 = p` is correct: `eps^{-j}` from `chi(t/eps)`, `eps^{k-l}` from `t^{k-l}` on `[eps,2eps]`, `eps^1` from the interval length. Uniformity in `eps, R` is what licenses dominated convergence **inside the spectral sum**, not just in each integral. This is the only interchange in the proof and it is justified.
3. *The meromorphic tail.* On a compact set avoiding the spectral values, `|s - lambda| >= |lambda|/2` for large `|lambda|`, so the tail is dominated by `2^{k+1} |nu(lambda)| |lambda|^{-(k+1)}` with `k+1 >= N+2 > N` — summable by (G2). Local finiteness of the spectral set (also from (G2)) leaves only finitely many terms near any `lambda`, so the principal part at `lambda` is exactly `k! nu(lambda) (s-lambda)^{-k-1}` with no lower-order contamination.
4. *Cancelling pairs.* Adding `(lambda,+1)` and `(lambda,-1)` changed the cutoff pairing by `0.00e+00` — the equivalence is exactly the kernel of the theorem, as advertised.
5. *Distributions supported at `t=0`.* Astra flags this explicitly; the common cutoff limit plus the vanishing of `t^k` at the origin is what prevents an atom at `0` from being silently absorbed. Correct.

**VERDICT T1.2: VALID**

## T1.3 — differentiating the explicit formula, and the half-time Jacobian

**Claim.** The trace form of H-ZEF-T has archimedean term `-1/(e^{2u}-1)`, and `comb(t/2) = 2 sum Lambda(n) delta(t - 2 log n)`.

**What I attacked.** I rederived H-ZEF-T from `psi_0` by hand rather than taking it: `d/dx[-(1/2)log(1-x^{-2})] = -1/(x(x^2-1))`, so `x psi_0'(x) = x - x sum Lambda(n) delta(x-n) - 1/(x^2-1)`; the pullback `x = e^u` uses `e^u delta(e^u - n) = delta(u - log n)`, giving `sum_rho e^{rho u} = e^u - comb(u) - 1/(e^{2u}-1)`. Both the **sign** of the archimedean term and the fact that the constant `-log 2 pi` dies under differentiation are as astra states. The `psi_0` identity itself I checked numerically against the direct prime-power count at `x = 10.5, 30.5, 100.5` with 260 zeros (agreement within the expected `x log x / gamma_max` truncation). The Jacobian `delta(t/2 - a) = 2 delta(t - 2a)` is elementary and is applied atom by atom with local finiteness noted.

**VERDICT T1.3: VALID**

## T1.4 — the forced arithmetic net spectra

**Claim.** Supertrace `= comb(u)` forces `nu(1)=1, nu(rho)=-m_rho, nu(-2k)=-1`; supertrace `= 2 P_+(t)` forces `nu(0)=1, nu(-conj(rho)/2)=-m_rho, nu(-(k+1/2))=-1`.

**What I attacked.** The transport. Setting `u = t/2` and multiplying by `e^{-t/2}` gives `sum_rho e^{(rho-1)t/2} = 1 - e^{-t/2} comb(t/2) - e^{-t/2}/(e^t-1)`, and `e^{-t/2} comb(t/2) = 2 sum Lambda(n) n^{-1} delta(t - 2 log n) = 2 P_+` because `e^{-t/2} = 1/n` exactly at `t = 2 log n`. The multiset identity `{rho - 1} = {-conj rho}` uses **both** `rho -> 1-rho` and `rho -> conj rho` (H-ZETA-LOC) and is an identity of multisets, not of individual labels — astra says so, and it matters because `(rho-1)/2 = -conj(rho)/2` only on the critical line. (G1),(G2) for the transported datum: `Re lambda in (-1/2, 0]` so `c = 0`, and `|lambda| = |rho|/2` so `N = 2` still works. The even constant mode `lambda = 0` comes from `e^{t/2} e^{-t/2}` and carries `nu = +1`. All correct.

**VERDICT T1.4: VALID**

---

# T2. What positivity forces

## T2.1 — reality of a parity assignment

**Claim.** The supertrace is real iff `F_Z` is conjugation invariant.

**What I attacked.** Necessity is where a shortcut would be taken. Astra does it through T1.2: the conjugate distribution is the supertrace of the conjugated datum, so reality plus rigidity gives equality of the net multiplicities, which at a zero are `+-m_rho` with `m_rho = m_{conj rho}`, hence equal signs at conjugate values. Real spectral values are unconstrained. That is the right route; the naive "sum the conjugates" argument only gives sufficiency.

**VERDICT T2.1: VALID**

## T2.2 — finite changes to the zero parities

**Claim.** With `F_Z` finite and `F_T` arbitrary, `mu` is positive iff `b = 0` and `F_Z = empty`.

**What I attacked — this is the section the brief singled out.**
1. *The "continuous part" step.* `f` is real-analytic on `u > 0` even when `F_T` is infinite (`sum_{k in F_T} e^{-2ku}` is a Dirichlet series with abscissa `<= 0`, locally uniformly convergent). The argument "if `f(u_0) < 0` then `f < 0` on an interval; the prime-power support is locally finite so shrink to an atom-free subinterval; a nonnegative bump there makes `mu` negative" is correct and is the only way to use H-SCHWARTZ here.
2. *The flipped pole.* `e^{-u} f(u) -> -2` requires `Re rho < 1` for every flipped zero (H-ZETA-LOC), `F_Z` finite, and the trivial sum bounded by `2e^{-2u}/(1-e^{-2u})`. Checked numerically at `u = 200`: `-2.00000000`.
3. *Several real parts in the flipped set.* This is the case the brief asked about. Astra normalises by the **largest** real part `sigma_* > 0` in `F_Z`, so `e^{-sigma_* u} f(u) = A(u) + o(1)` where `A` is the leading trigonometric polynomial from the `Re rho = sigma_*` slice only; everything else (lower real parts, and the trivial ladder times `e^{-sigma_* u}`) is genuinely `o(1)`. I tested mixtures `(sigma,gamma) = (0.5,14.13)+(0.3,3.0)`, `(0.9,5.0)+(0.2,40.0)` and a degenerate slice `(0.5,14.13)+(0.5,21.02)`: the normalised `f` goes negative in every case (minima `-3.45, -2.41, -4.00`).
4. *The oscillation lemma itself.* `A` is real (by T2.1), has no constant term (zeros have nonzero imaginary part), and is nonzero. The mean/mean-square argument is airtight as written: if eventually `A >= -delta` with `|A| <= M`, then `lim (1/T) int A = 0` forces `limsup (1/T) int A_+ <= delta`, while `A^2 = A_+^2 + A_-^2 <= M A_+ + delta^2`, giving `C <= M delta + delta^2` for every `delta > 0` and contradicting `C = sum (2 m_rho)^2 > 0`. Note this needs the frequencies within the slice to be **distinct**, which they are (`rho = sigma_* + i gamma` determines `rho`). Over 400 random real zero-frequency trigonometric polynomials, 400/400 went negative. Crucially, this is the correction the ledger records: a single cosine cannot be isolated from other terms of the same growth, and astra does not try to.
5. *Sufficiency.* `comb + 2 sum_{F_T} e^{-2ku}` is a sum of two positive Radon measures on the open half-line; no constraint on `F_T` at all. This is stronger than the brief asked for.

**VERDICT T2.2: VALID**

## T2.3 — the infinite case under a domination premise

**Claim.** Adding `mu >= comb` as measures (plus H-LANDAU), `b = 0` and `F_Z = empty` for arbitrary `F_Z`.

**What I attacked — "is the domination premise really needed?"**

*The argument as given is correct.* Under domination, `f >= 0` is a positive measure; its weighted Laplace transform `R(s)` is meromorphic with poles only at `1` (if `b=1`), at the flipped zeros (which are **off the real axis**, H-ZETA-LOC), and at `-2j`. If `b = 1`, `R(s) -> -inf` as `s -> 1+`, contradicting positivity. With `b = 0`, `R` is holomorphic at every real point, so Landau forces abscissa `-inf`, so `R` is entire — contradicting a pole at any `rho in F_Z`. Astra's sentence "with `b=0` the meromorphic formula is holomorphic at every positive real point" is about the transform of **`f`**, not of `mu` (whose transform does have the pole at `1` from `nu(1)=+1`); read that way it is right, and the distinction is load-bearing. I verified the pole structure numerically with 120 zero pairs and `k = 4`: `R_4(s)` at `s = 1.5, 1.1, 1.01, 1.001` is `-768, -2.4e6, -2.4e11, -2.4e16` for `b=1` and the positive mirror for `b=0`.

**The finding (MINOR): the `b = 0` half needs no domination at all.** Here is the proof, which I ask to be inserted.

> *Claim.* Let the flipped datum be as in (2.1) with `F_Z` arbitrary, and suppose only that `mu >= 0` on `(0,inf)`. Then `b = 0`.
>
> *Proof.* Choose `chi, eta` in `[0,1]` and monotone, as in T1.2. For fixed real `s > 1`, `h_{eps,R,s} >= 0` increases pointwise to `t^k e^{-st}` as `eps -> 0`, `R -> inf` (because `chi` is nondecreasing and `eta` nonincreasing). Since `mu` is a positive Radon measure (H-SCHWARTZ), monotone convergence gives `int t^k e^{-st} dmu = lim <mu, h_{eps,R,s}> = R_k(s)`, which T1.2 shows is finite for `s > c_0 > 1`. So `R_k(s) >= 0` for every real `s > 1`. But `R_k(s) = k!(1-2b)(s-1)^{-(k+1)} + (holomorphic near 1)`, so `b = 1` gives `R_k(s) -> -inf` as `s -> 1+`. Contradiction. QED

This uses neither H-LANDAU nor the domination premise, and it is the half that matters for the Phantasm (the pole must stay **even**). T2.2's `<1>2` already covers it for finite `F_Z`, by a pointwise argument that does not survive an infinite flip set; the Laplace argument does.

**What I could *not* remove.** The premise is genuinely needed for `F_Z = empty`. The obstruction is the one astra identifies, and it is sharp: for infinite `F_Z` the subseries `2 sum_{F_Z} m_rho e^{rho u}` is only a distribution, and it can carry atoms at prime powers. Concretely, flipping *every* zero gives `mu = 2e^u - comb - 2/(e^{2u}-1)`, whose prime atoms are `-Lambda(n) < 0` — positivity fails, as it must; flipping a cofinite set fails the same way; flipping "half" in any conjugation-asymmetric sense fails by T2.1. So the only surviving question is whether a conjugation-symmetric infinite `F_Z` can have atomic contribution `> -Lambda(n)` at every prime power, i.e. "density at most 1/2" in the atom weighting. That heuristic is the content of astra's own T2.4 and I could not turn it into a proof or a counterexample. Domination is exactly the hypothesis "`mu`'s atom at `log n` is at least `Lambda(n)`" — it is not a weakening in disguise, it is the whole missing input.

**The fix I supply.** Split the claim: "(i) positivity alone forces `b = 0` (proof above, no H-LANDAU, no domination); (ii) under the additional premise `mu >= comb`, also `F_Z = empty`."

**VERDICT T2.3: MINOR**

## T2.4 — the unrestricted infinite question

**Claim (a scope statement).** H-SCHWARTZ makes `f = mu - comb` a signed Radon measure with nonnegative diffuse part but possibly negative atoms at prime powers, down to the comb mass; the transform of `mu + comb` has a real pole at `1` from the comb, so Landau gives no obstruction to further poles at flipped zeros; separating atomic and diffuse parts is not the same as selecting spectral subseries.

**What I attacked.** Every clause. The diffuse part of `f` equals the diffuse part of `mu` (the comb is purely atomic), hence `>= 0` — correct. The statement that Landau on `mu + comb` (or, equally, on `mu` itself) is toothless is correct and I verified the mechanism: with `b = 0` the abscissa of convergence of `int t^k e^{-st} dmu` is exactly `1` (it cannot be less, because `R_k` has the pole `+k!(s-1)^{-(k+1)}` there), and `s = 1` *is* a singularity, so Landau is satisfied without saying anything about the zeros. The refusal to claim full parity rigidity is the correct call, and the located missing step is the correct one.

**VERDICT T2.4: VALID**

---

# T3. Ordinary-trace obstructions

## T3.1 — finite and trace-class no-go

**Claim.** No finite matrix and no trace-class operator has `Tr E^n = N_n = sum b_i^n - sum alpha_j^n` (`Z >= 1`, disjoint after cancellation).

**What I attacked.**
1. *The residue sign.* SymPy: `Res_{u=1/alpha} [alpha u/(1-alpha u)] = -1/alpha` exactly, so the prescribed function has residue `+m_alpha/alpha` and any ordinary trace function has `-m_E(alpha)/alpha` with `m_E >= 0`. The forced identity `m_E(alpha) = -m_alpha` is impossible. The sign is the entire content and it is right.
2. *Meromorphy of `sum lambda_i u/(1-lambda_i u)` for trace class.* This is the step the brief flagged. On `|u| <= R`, only finitely many `lambda_i` exceed `1/(2R)` (because `sum|lambda_i| < inf`), and for the rest `|1 - lambda_i u| >= 1/2`, so the tail is bounded by `2R sum |lambda_i|` and converges normally. Hence the function is meromorphic on `C` with locally finite poles at `1/lambda_i`, and the residue comparison is legitimate. Checked with `lambda_k = 0.9/k^2` (`sum = 1.480`, only 2 above the threshold at `R = 3`).
3. *Jordan blocks and zero eigenvalues.* Neither affects `Tr E^n` for `n >= 1` nor the residues; astra says so.
4. *Coincidence `alpha_j = lambda_i`.* Handled by net multiplicities, since at `u = 1/alpha` only terms with `lambda_i = alpha` are singular.

**VERDICT T3.1: VALID**

## T3.2 — trace and supertrace criteria

**Claim.** (1) trace sequence of a trace-class operator iff `Z(u) = prod (1 - lambda_i u)^{-1}` with `sum|lambda_i| < inf`; (2) supertrace sequence of a finite graded matrix iff `Z` is rational with `Z(0) = 1`, even net spectrum = reciprocal poles, odd net spectrum = reciprocal zeros.

**What I attacked.** The "no nonconstant zero-free exponential factor" clause, which is the sharpening of the brief. If `Z = e^{cu} prod(1-lambda_i u)^{-1}` then `N_1 = c + sum lambda_i` but `N_n = sum lambda_i^n` for `n >= 2`, so the sequence is a trace sequence only if `c = 0`; excluding the factor is necessary and astra does it. `sum |lambda_i| < inf` for a trace-class operator is Weyl's inequality, not an extra assumption. For (2) I checked `Z(u) = det(1-uE_-)/det(1-uE_+)` numerically against the Newton series to 40 terms for `E_+ = diag(3,1)`, `E_- = diag(1.7 +- 0.3i, -2)`: `1.205017394855` both ways. The direction "poles = even, zeros = odd" is the right way round. The caveat that eigenvalue zero, its parity and nilpotent blocks are invisible to positive powers is stated.

**VERDICT T3.2: VALID**

## T3.3 — curves, MPS ring norms, graphs

**Claim.** Positive-genus curve counts have no ordinary finite/trace-class realisation; they have the graded realisation `diag(q,1) (+) Frob|H^1`; the odd **net** spectral multiset is forced; no fixed-finite-bond translation-invariant MPS can have those ring norms; graph non-backtracking counts need no grading.

**What I attacked — "is the MPS ring-norm corollary exactly stated?"** Yes, and the hypotheses that make it exact are all present: *fixed* local tensor (no `n`-dependence), *translation invariant*, *finite* family `A_s` of *finite* matrices, *periodic* amplitudes, and "for all `n`". I re-derived the contraction from scratch — `sum_{s_1..s_n} |Tr(A_{s_n}...A_{s_1})|^2 = Tr (sum_s A_s (x) conj A_s)^n`, verified to `1e-8` relative at `n = 1,2,3` for random `D = 3`, 2-species tensors — so the object excluded is a genuine finite matrix and T3.1 applies. Two loopholes a sloppier statement would leave open are closed: an infinite physical index is covered by the trace-class half of T3.1, and an `n`-dependent gauge is outside the hypothesis.

*Independent confirmation of the negative multiplicities.* I built the `q=3, a=(0,1)` curve counts from the Weil form, ran a from-scratch Prony fit (Hankel solve plus root-finding, order 6) on `N_1..N_12`, and recovered exactly `{3, 1, sqrt3, -sqrt3 (x2), +-i sqrt3}` with coefficients `+1, +1, -2, -2, -1, -1`: **four negative integer multiplicities**. Same conclusion as `outputs/artin_schreier_super.txt` Task 5, obtained independently.

The non-cancellation argument (`|alpha| = sqrt q` differs from both `1` and `q` when `q > 1`) is correct, and the graph remark (`1/det(1-uT)` has no finite zeros, though there is a zero at infinity as a rational function on the sphere) is stated with the right pedantry.

**VERDICT T3.3: VALID**

---

# T4. The Riemann channel as the odd sector

## T4.1 — the exact prime-measure supertrace

**Claim.** `e^{tG} = 1 (+) Z(t) (+) diag(e^{-(k+1/2)t})` is a strongly continuous contraction semigroup with fixed-vector space exactly the even line, and
`str e^{tG} = 1 - Tr_dist Z(t) - sum_{k>=1} e^{-(k+1/2)t} = 2 P_+(t)`, via
**`Tr_dist Z(t) = 1 - 2 P_+(t) - e^{-t/2}/(e^t - 1)`** (4.2).

**What I attacked — every sign and factor, rederived from scratch.**

*Derivation.* From my own H-ZEF-T (see T1.3), put `u = t/2` and multiply by `e^{-t/2}`:
`sum_rho e^{(rho-1)t/2} = 1 - e^{-t/2} comb(t/2) - e^{-t/2}/(e^t-1)`.
The Jacobian gives `comb(t/2) = 2 sum Lambda(n) delta(t - 2 log n)` and the damping gives `e^{-t/2} = 1/n` **at the atom**, so the prime term is exactly `2 sum Lambda(n)/n delta(t-2log n) = 2 P_+`, with **coefficient `-2`, not `-1` and not `+2`**. The archimedean term: `e^{-t/2}/(e^t-1) = e^{-3t/2}/(1-e^{-t}) = sum_{k>=1} e^{-(k+1/2)t}`, checked to `1e-12` at `t = 0.4, 1, 2, 5`. Reindexing `{rho-1} = {-conj rho}` turns the left side into `Tr_dist Z(t)`. So (4.2) holds exactly as printed, and subtracting the ladder gives `str e^{tG} = 2 P_+` with no leftover.

*Numerics (independent of `outputs/riemann_graded_trace.txt`).* 260 `mpmath` zeros, Gaussian window `s = 0.18` in `t`; the smeared zero sum `sum_rho e^{-conj(rho) t_0/2} e^{conj(rho)^2 s^2/8}` against `1 - 2 P_+^{smeared} - A^{smeared}` (the latter by quadrature) at 15 values of `t_0`, nine of them exactly at `t = 2 log n`:

| `t` | 1.3863 | 2.1972 | 2.7726 | 3.2189 | 3.8918 | 4.1589 | 4.3944 | 4.7958 | 5.1299 |
|---|---|---|---|---|---|---|---|---|---|
| `Tr_dist Z` (zeros) | -0.71393 | -0.67158 | 0.13870 | -0.47216 | -0.37537 | -0.02768 | 0.18871 | -0.16910 | -0.06996 |
| `1 - 2P_+ - A` | -0.71393 | -0.67158 | 0.13870 | -0.47216 | -0.37537 | -0.02768 | 0.18871 | -0.16910 | -0.06996 |

max `|diff| = 9.4e-06`, relative `1.3e-05` (the 260-zero truncation). **Wrong variants rejected:** `+2P_+` off by `3.256`; `P_+` with coefficient `1` off by `0.814`; `+A` instead of `-A` off by `0.774`. So all three of the plausible slips are excluded by three to four orders of magnitude. `str e^{tG} = 2 P_+` matches to the same `9.4e-06`. This is an independent confirmation of `outputs/riemann_graded_trace.txt` Task 1 (which reports dip ratios within `5.1e-04`) and of the report's `obs:ringnorm-sign-correction`.

*Operator statements.* Contraction (`||Z(t)|| <= 1` by H-LP; ladder factors `<= 1`); strong continuity of the ladder by dominated convergence; fixed vectors: `Z(t) -> 0` strongly kills `K_S`, no ladder coordinate is fixed, the constant line is fixed pointwise. The generator domain is written out. Nothing hidden.

**VERDICT T4.1: VALID**

## T4.2 — ladder alternatives and rigidity

**Claim.** `C (+) K_S` alone gives `2P_+ + A`; ladder counted even gives `2P_+ + 2A`; both positive, so positivity does not fix the ladder parity. Exact equality to `2P_+` forces the net spectrum; no all-even datum can have supertrace `2P_+` or `comb`.

**What I attacked.** Both variants reproduce to `9.4e-06` in my numerics, and `A(t) > 0`, so the "positivity does not fix the ladder" conclusion is right — this matches Task 2a/2b of the numerics lane. The all-even exclusion is immediate from T1.4 (negative required net multiplicities vs nonnegative available ones) and does **not** smuggle in anything about physical fermions; astra's closing caveat ("It is a Hilbert-space semigroup; it has not been shown to be a trace-preserving generator on an operator algebra") is exactly the right restraint.

**VERDICT T4.2: VALID**

## T4.3 — scope of the Phantasm interpretation

**Claim (remark).** RH = all odd `K_S` modes have real part `-1/4` (not the odd ladder); the even line is added and represents the `zeta` pole, since `xi` as defined is entire; `Z(t)` is not trace class or compact; a finite cMPS transfer cannot give an atomic prime measure; a supertrace is signed and a parity insertion needs a physical construction.

**What I attacked.** `Re(-conj(rho)/2) = -sigma/2 = -1/4` iff `sigma = 1/2` — correct, and correctly restricted to `K_S` (the ladder sits at `-(k+1/2)`). The non-compactness argument is right: for fixed `t>0` every asserted eigenvalue has modulus `e^{-sigma t/2} in (e^{-t/2}, 1)`, bounded away from `0`, so no compact operator has that eigenvalue list. The observation that `xi(s) = (1/2)s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)` is **entire** (so the pole being represented belongs to `zeta`, not `xi`) is the same correction the earlier Weil-positivity review recorded, and it is right. The final paragraph ("an even eigenvalue 1 and an odd eigenvalue 2 give supertrace `-1`") is the honest statement that a supertrace is not a norm.

**VERDICT T4.3: VALID**

---

# T5. Vacuum decay

All of T5.1/T5.2/T5.5 was rebuilt from the statements at `D = 3` and `D = 5` in `scratch_rcmps_t3t5.py`: random Hermitian `H`, random `j`, `B = -iH - (1/2)|j><j|`, superoperator assembled column by column.

## T5.1 — the finite vacuum-decay Lindbladian

**Claim.** `L` is a trace-preserving GKLS generator with unique stationary density `Omega`; `spec(L) = {0} u {b_i} u {conj b_i} u {b_i + conj b_j}` (5.1); coherences odd, populations and vacuum even.

**What I attacked.**
1. *GKLS form.* `J^dag J = |j><j|` on `C (+) H` (zero on the vacuum line), so `bB + bB^dag = -J^dag J` holds as stated; `H_0 = (bB^dag - bB)/2i` reproduces `bB = -iH_0 - (1/2)J^dag J`. Verified: `|L_GKLS(x) - L(x)| < 1e-11`; `|Tr L(x)| < 1e-11`.
2. *Formula (5.2), the load-bearing step.* I checked `e^{tL}(x)` against the block formula at `t = 0.13, 0.9, 3.0`: max deviation `5e-16 / 1.7e-15 / 3.1e-15`. The feed term `a + Tr X - Tr(Z_t X Z_t^dag)` differentiates to `<j, Z_t X Z_t^dag j>` precisely because `B + B^dag = -|j><j|` — the rank-one dissipation is used exactly once and exactly there.
3. *Complete positivity via (5.2).* The decomposition "conjugation by `1 (+) Z_t`" plus "`X -> Tr[(I - Z_t^dag Z_t)X] Omega`" is a correct Kraus decomposition **provided `Z_t` is a contraction**, which follows from `B + B^dag <= 0`. Both checked: `I - Z_t^dag Z_t >= 0` and the Choi matrix of `e^{0.7 L}` has minimum eigenvalue `-1.2e-15`. So no external GKLS existence theorem is needed, as astra claims.
4. *(5.1) with multiplicities, without diagonalisability.* Block triangularity in the ordering `(X, l, r, a)` with diagonal blocks `X -> BX + XB^dag`, `l -> Bl`, `r -> rB^dag`, `a -> 0` is correct (the only off-diagonal coupling is `X -> a`). Greedy multiset matching of the `(d+1)^2` eigenvalues against (5.1): max deviation `6.2e-15` (`D=3`) and `1.3e-14` (`D=5`), with nothing left over. The simplicity of the zero eigenvalue follows from `Re b_i < 0`, which is a hypothesis, and astra says so.
5. *The grading.* `Gamma = 1 (+) (-I_H)`; I verified `[Gamma (x) Gamma, L] = 0` to `1e-11`, and that the odd part's spectrum is exactly `spec(B) u conj spec(B)` (deviation `1.6e-15`). The subtle point — `J` is an odd *operator* but `x -> J x J^dag` preserves the *operator* grading because the two odd factors cancel — is stated and is correct.

**VERDICT T5.1: VALID**

## T5.2 — finite traces

**Claim.** `Tr e^{tL} = |1 + Tr_H Z_t|^2`, `str e^{tL} = |1 - Tr_H Z_t|^2`.

**What I attacked.** The four block traces are `1`, `conj(Tr Z_t)`, `Tr Z_t`, `|Tr Z_t|^2`; the `X -> a` coupling is off-diagonal and does not contribute. Checked at `t = 0.3, 1.1`, `D = 3, 5`: agreement to `1e-9` in all eight comparisons (e.g. `D=5, t=0.3`: `18.908556779` both ways for the trace, `5.714495877` both ways for the supertrace). The `t = 0` values `(d+1)^2` and `(1-d)^2` are right. The sentence "the vacuum-decay transfer is **not** the single-particle generator `0 (+) B`" is the important one and is correct.

**VERDICT T5.2: VALID**

## T5.3 — infinite-dimensional absorbing-vacuum channel

**Claim.** For any strongly continuous, strongly stable contraction semigroup `Z_t`, (5.2) defines a strongly continuous CPTP semigroup on trace class with unique stationary density `Omega` and exact odd coherence evolution; no bounded rank-one exit vector needed.

**What I attacked.** The semigroup law: the population loss telescopes, `[a + Tr X - Tr(Z_t X Z_t^*)] + Tr(Z_t X Z_t^*) - Tr(Z_{s}Z_t X Z_t^* Z_s^*) = a + Tr X - Tr(Z_{s+t} X Z_{s+t}^*)`, using only `Z_{t+s} = Z_t Z_s`. Correct. The Kraus rows `|vac><e_j| D_t^{1/2}` need `D_t = I - Z_t^dag Z_t >= 0`, i.e. contractivity — a hypothesis, correctly listed. Trace-norm continuity and the limit `Tr(Z_t X Z_t^*) = sum a_j ||Z_t v_j||^2 -> 0` by dominated convergence under strong stability are both right, and the decomposition of a general trace-class `x` into four positive pieces is the standard move. The disclaimer that the generator need not have the bounded single-jump form of T5.1 is exactly the right hedge — H-LP supplies no exit vector.

**VERDICT T5.3: VALID**

## T5.4 — the formal coherence and population spectra

**Claim (remark, `sketched`).** For `H = K_S` the zero modes sit in the odd coherence blocks, each zero appearing once as `-conj(rho)/2` and once as its conjugate; the even population modes are `-(conj rho_n + rho_m)/2`; the "form factor" `|Tr_dist Z|^2` is formal only, because the pair list violates (G2) and a product of the distributions is undefined.

**What I attacked.** The doubling. Since the zeta multiset is conjugation invariant, `spec(B) u conj spec(B)` gives each value `-conj(rho)/2` total multiplicity `2 m_rho`, **not** `m_rho` as in T4's forced datum. Astra states this in the claim and again in the ledger; I confirmed the combinatorics (`scratch_rcmps_x2x3.py`: multiplicities `[2,2,2,2]` for a critical-line test spectrum). The (G2) violation is real: the diagonal pair values `-Re rho_n` accumulate in a bounded interval, so the pair datum is not a graded spectral datum at all and T1 does not apply to it. Refusing any pair-correlation conclusion is correct.

**VERDICT T5.4: VALID**

## T5.5 — the renewal correction and the trivial Schmidt spectrum

**Claim.** The proposed renewal integral diverges; the canonical cMPS state selected by this bond has one nonzero Schmidt weight, equal to one.

**What I attacked — the two items the brief flagged.**
1. *The renewal integral.* `J Omega = 0` and `e^{t bB} Omega e^{t bB^dag} = Omega`, so `int_0^T ... dt = T Omega`. Verified numerically: the integral's trace is `5.00000000` at `T = 5` for both `D = 3` and `D = 5`. It diverges, exactly as claimed, and the observation that in the *original* `K_S` the equation is not even type-correct (`Omega` lives in the added line) is right. The vacuum is absorbing with infinite holding time, so the no-event semigroup on the enlarged space is not strongly stable — this is the precise reason HANDOFF item 0b's finite-occupation renewal equation is not solved here.
2. *The Schmidt spectrum.* Trace preservation gives left fixed point `I`; T5.1 gives right fixed point `Omega`, rank one; H-CMPS then gives nonzero Schmidt spectrum `{1}`. The **direct** check astra adds is the stronger one and I reproduced it: every ring amplitude containing a jump vanishes identically, because `<j|vac> = 0` and `e^{s bB}` preserves the two blocks. I evaluated the one-jump amplitude `Tr(e^{(1-s)bB} J e^{s bB})` at 19 values of `s`: `0.00e+00` to machine zero in both dimensions. So the only surviving field configuration is the vacuum and the half-chain entanglement is trivial. The caveat about lengths where `Tr e^{t bB}` vanishes (it tends to `1`, so the exception is immaterial at large length) is a real edge case and is handled.

**VERDICT T5.5: VALID**

---

# T6. The prime chain

## T6.1 — normal KMS states and the product purification

**Claim.** A normal KMS`_beta` state for `Ad(N^{it})` on `B(l^2(N))` exists iff `beta > 1`, and equals `N^{-beta}/zeta(beta)`; `spec(-log rho_beta) = {beta log n + log zeta(beta)}`; the thermofield double factorises over primes with bond dimension one.

**What I attacked.**
1. *The normal-KMS argument.* Invariance plus distinct eigenvalues `log n` forces diagonality; `alpha_{i beta}(e_{nm}) = (n/m)^{-beta} e_{nm}` (verified by explicit matrices at `(n,m) = (2,5),(7,3)`, agreement to `1e-12`); the KMS identity with `A = e_{mn}`, `B = e_{nm}` then gives `p_n = (n/m)^{-beta} p_m` (verified over all `1 <= n,m <= 12`), hence `p_n propto n^{-beta}`, normalisable exactly for `beta > 1`. I also checked the convention itself: with `varrho = e^{-beta H}/Z` and `alpha_t = Ad(e^{itH})`, `omega(A alpha_{i beta}(B)) = Tr(A e^{-beta H} B)/Z = omega(BA)` by cyclicity — the direction is right, which is where a factor `e^{+beta H}` would otherwise slip in.
2. *The type III comparison — is it stated honestly?* Yes. Astra separates the two questions cleanly: the nonexistence is about normal states **in this fixed representation on all bounded operators**, whereas H-BC-POS is about a state on the **Bost–Connes `C^*`-algebra** with its own GNS completion, supplying no trace-class density on `l^2(N)`. He also corrects the supplied wording twice (the algebra is not `B(l^2)`; the high-temperature range is `0 < beta <= 1`, not all `beta <= 1`). Both corrections are right. See the H-* section for the one provenance gap.
3. *The factorisation.* The Euler product for `zeta(beta)` (checked truncated at `p <= 37`, `1.430325` vs `1.432418`) and the TFD product form are standard, and the statement "entanglement between left and right at each site, but none between different prime sites" is the correct reading of bond dimension one **along the chain**. The unit conversion note (`beta log n` vs T4's ring lengths `2 log n`) is already in the ledger and is needed — see X3.

**VERDICT T6.1: VALID**

## T6.2 — proof of H-MM1

**Claim.** The birth–death generator with `lambda < mu` has spectrum `{0} u [-(sqrt lambda + sqrt mu)^2, -(sqrt mu - sqrt lambda)^2]`.

**What I attacked — including the rank-one resolvent step the brief flagged.**
1. *The conjugation.* `pi_k lambda = pi_{k+1} mu` makes both hopping entries `sqrt(lambda mu)` after conjugating by `sqrt(pi_k)`; the diagonal is `-(lambda+mu)` for `k >= 1` and `-lambda` at `k = 0`. Correct, and it is the boundary diagonal that carries all the information.
2. *The band.* The constant-diagonal half-line Jacobi matrix has spectrum `[-(lambda+mu)-2a, -(lambda+mu)+2a] = [-(sqrt lambda + sqrt mu)^2, -(sqrt mu - sqrt lambda)^2]` by the sine transform, and truncated plane waves far from the boundary are Weyl sequences for the modified matrix too. Verified on `3001 x 3001` truncations at `(lambda,mu) = (0.35,1), (0.19,1), (0.04,1), (0.7,0.9)`: top eigenvalue `< 3.3e-16`, and `3000/3000` of the remaining eigenvalues inside the predicted band in every case.
3. *The outside-band solution.* Interior `x = -(lambda+mu) + a(z + 1/z)` and boundary `x = -lambda + az` force `a/z = mu`, so `z = sqrt(lambda/mu) < 1` and `x = 0`. Verified symbolically to `1e-12` in all four cases.
4. *The rank-one resolvent step.* This is Sherman–Morrison applied to `(x - K) - mu|e_0><e_0|`, and the pole condition `1 - mu m(x) = 0` with `m(x) = <e_0, (x-K)^{-1} e_0> = z/a`. I computed `m(0)` by solving the `2001`-dimensional linear system directly: `1.0000000000` against `z/a = 1.0000000000` (and `1.1111111111` both ways for `(0.7,0.9)`), with `1 - mu m(0) = 1.1e-16`. So `m(x) = z/a` is right, the pole is exactly at the eigenvalue already found, and no other point outside the band is in the spectrum.

**VERDICT T6.2: VALID**

## T6.3 — the classical prime-by-prime dynamics

**Claim.** Rates `n -> pn` at `r_p`, `n -> n/p` at `r_p p^beta`; independent product of birth–death chains; nonexplosive; unique stationary law `n^{-beta}/zeta(beta)`; spectrum (6.2) = closure of `{0}` union the finite Minkowski sums of `I_p = [-r_p(p^{beta/2}+1)^2, -r_p(p^{beta/2}-1)^2]`.

**What I attacked — the three items the brief flagged.**
1. *The rates.* I rederived the diagonal action of (6.1) from the isometries: `mu_p^dag mu_p = I` gives the uniform loss `-r_p x_n`, `mu_p mu_p^dag = P_{p | .}` gives `-r_p p^beta 1_{p|n} x_n`, and the gain terms are `r_p 1_{p|n} x_{n/p}` and `r_p p^beta x_{pn}`. This matches astra's display exactly. Detailed balance `pi(n) r_p = pi(pn) r_p p^beta` is `n^{-beta} = (pn)^{-beta} p^beta`. Correct.
2. *The band per prime.* `lambda_p = r_p`, `mu_p = r_p p^beta` gives `I_p` exactly as printed. Verified on truncated single-prime generators for `p = 2,3,5,7` at `beta = 1.5, r_p = p^{-(beta+2)}`: the non-zero spectrum lands in `I_p` to `1e-6` in all four cases (e.g. `p=2`: `[-0.635690, -0.041087]` observed vs `[-0.635690, -0.041087]` predicted).
3. *Is the closure essential?* **Yes, and this is the right place to insist on it.** The right endpoints `-r_p(p^{beta/2}-1)^2 -> 0^-` accumulate at `0`, and — more seriously — when `sum_p r_p p^beta < inf` the sum of the *left* endpoints over **all** primes converges (I get `-1.002516` summing over `p < 2 x 10^4` for the `r_p = p^{-(beta+2)}` example), so there are limit points of infinite sums that lie in no finite Minkowski sum. The spectrum of a direct sum is the closure of the union of the summand spectra, so those points are in the spectrum. Dropping the closure would be a genuine error and astra does not drop it.
4. *The choice of Hilbert space.* `L^2(pi)` with `pi` the product Gibbs measure on finite-support configurations, decomposed as the orthogonal sum over finite prime sets `A` of `(x)_{p in A} H_p^0`. Each component is invariant, the restricted generator is a finite sum of commuting bounded single-prime generators on separate factors, and the tensor spectral theorem gives the Minkowski sum. The unbounded direct sum has the stated domain. All correct, and the remark that this "also defines the generator rigorously even when the down-rate coefficients are not summable" is the honest way to handle the `r_p = p^{-beta}` example.
5. *Uniqueness of the stationary law.* The `L^2` gap argument on finite coordinate sets, upgraded to total variation by Cauchy–Schwarz, then Kolmogorov consistency — correct, and it avoids needing a recurrence theorem.

**VERDICT T6.3: VALID**

## T6.4 — the off-diagonal sectors

**Claim.** Under `sum_p r_p p^beta < inf`, (6.1) is a bounded CPTP semigroup with `rho_beta` stationary, and on the KMS-weighted Hilbert space `||x||_beta = ||rho_beta^{-1/4} x rho_beta^{-1/4}||_HS` the generator is bounded self-adjoint and nonpositive **including** the off-diagonal sectors.

**What I attacked.** I recomputed the single-prime matrix-unit action: `|k><l|` hops to `|k+1><l+1|` at `lambda` and to `|k-1><l-1|` at `mu` when both indices are positive, with loss `-lambda - (mu/2)(1_{k>0} + 1_{l>0})` — exactly astra's coefficients. Conjugating by `(pi_k pi_l)^{-1/4}` turns **both** hoppings into `sqrt(lambda mu)`, so the fixed-difference sectors are real symmetric half-line Jacobi matrices with interior diagonal `-(lambda+mu)` and boundary `-lambda` (difference zero) or `-lambda - mu/2` (difference nonzero). I verified the exact operator identity `sector(delta != 0) = sector(0) - (mu/2)|e_0><e_0|` to `1e-14` and diagonalised `2001 x 2001` truncations: top eigenvalue `-2.4e-17` for `delta = 0` (the stationary state) and `-0.1668` for `delta = 1,2,5`. So the quadratic-form comparison is valid and the off-diagonal sectors are *strictly* negative. The paragraph disclaiming the `r_p = p^{-beta}` example (every down coefficient is `1`, so `sum r_p p^beta = inf` and the stronger condition fails) is correct and necessary.

**VERDICT T6.4: VALID**

## T6.5 — delocalisation

**Claim.** As `beta -> 1^+`, `rho_beta` has no normal trace-norm limit and its mass on every finite-rank projection vanishes; below the threshold the classical process has no stationary probability on finite-support configurations; none of this proves "ergodicity breaking" of a Riemann Lindbladian.

**What I attacked.** `||rho_beta|| = 1/zeta(beta)` (the top eigenvalue is at `n = 1`), so `Tr(P rho_beta) <= rank(P)/zeta(beta) -> 0`; checked numerically (`1/zeta = 0.383, 0.179, 0.049, 0.0099` at `beta = 1.5, 1.2, 1.05, 1.01`). The elementary proof that `sum_p 1/p` diverges — "if it converged, `prod_{p <= P} (1-1/p)^{-1}` would be bounded, while it dominates every harmonic partial sum" — is correct as written and does not quote Mertens. `prod_p (1 - p^{-beta}) = 0` when `sum p^{-beta} = inf`, then a countable union over finite exceptional sets: correct. The `beta <= 0` case (no summable geometric law in even one factor) is handled separately. And the closing `<1>3` — that loss of normalisability is *not* a spectral-gap statement, *not* multiple steady states, and that the arithmetic high-temperature state lives in a different representation and cannot be identified with T5's pure absorbing vacuum — is the most valuable paragraph in T6 and is exactly right.

**VERDICT T6.5: VALID**

---

# T7. Artin–Schreier

Everything below was rebuilt from scratch in `scratch_rcmps_t7.py` and `scratch_rcmps_t7b.py`: `F_{q^n}` by an irreducible polynomial (sympy irreducibility test), normal-basis generator by rank test, `S_n(g)` by brute force over the field, the transfer matrix from (7.1), the radical `ker P(S)` by Gaussian elimination over `F_q`, the shift determinant on the radical, the embedding matrix `A`, the `L`-polynomial by Newton's identities, the projective curve by direct point count, and the **centred** Weyl operators. 235 checks, **0 failures**, across 12 coefficient tuples over `q = 3, 5, 7` — including the two the numerics lane had FAIL and the two extra tuples `(3,(0,0,1))`, `(3,(1,0,1))`.

## T7.1 — Gauss evaluation

**Claim.** H-GAUSS, plus `|sum psi(Q)|^2 = q^{n+d}` and `conj(sum psi(Q)) = eta(-1)^r sum psi(Q)`.

**What I attacked.** The diagonalisation-by-congruence step in odd characteristic (using `2 != 0` to produce a nonzero diagonal value from a nonzero off-diagonal entry) is correct; `sum_x psi(ax^2) = eta(a) g(psi)` via `sum_y (1+eta(y)) psi(ay)` with `eta(0)=0`; `|g|^2 = q` by `(x,y) -> (x-y,x+y)`; `g^2 = eta(-1) q`. The determinant convention warning ("we use `det` of `A` in `Q(x) = x^t A x`, not of `2A`") is necessary — the two differ by `eta(2)^n`, which is not always a square — and since astra **proves** H-GAUSS in his own convention and only ever uses the **ratio** of two sums in the same convention, nothing depends on which convention the literature uses. Good hygiene.

**VERDICT T7.1: VALID**

## T7.2 — ring and trace quadratic forms for every `n`

**Claim.** `Tr E_g^n = sum_x psi(x^t M x)` with `M = P(S)`, and `S_n(g) = sum_x psi(x^t C M x)`; both radicals equal `ker M`, so `d_n = dim ker M` and `|S_n| = |t_n|`.

**What I attacked.**
1. *Short rings (`n <= J`).* This is where the closed-path bijection could fail. I verified `Tr E_g^n = sum_x psi(Q^circ(x))` by brute force for `n = 1..7` (`q=3`), `1..5` (`q=5`), `1..4` (`q=7`) in all 12 tuples, including `n < J` and `n = J`: all PASS. The wraparound repetitions are handled correctly by cyclic indices.
2. *The factor of two.* `sum_i x_i x_{i+j}` has matrix `S^j`; symmetrising gives `(S^j + S^{-j})/2`, and the `j=0` term gives `a_0 I` (not `2a_0 I`). The `j` term of the trace form has unsymmetrised matrix `C S^{-j}` (I re-derived: `(C S^{-j})_{ik} = c_{k+j-i}`), and since `C^t = C`, `S^t = S^{-1}`, its symmetric part is `C(S^j + S^{-j})/2`, summing to `CM`. All factors of two are right, and the shift convention is stated.
3. *`ker(CM) = ker M`.* `C` is the Gram matrix of the trace pairing in a basis, hence invertible; it is a circulant in the normal basis hence commutes with `S` and with `M`. Verified for `n` up to `9`.
4. *`d_n` as an integer.* `d_n = log_q(|S_n|^2/q^n) = dim ker P(S)` verified in every case — this is the identity that makes the numerics lane's empirical `d_n` column an honest invariant rather than a fitted number.

**VERDICT T7.2: VALID**

## T7.3 — the corrected sign law, including `q | n`

**Claim.** `S_n(g) = (-1)^{n-1} delta_n Tr E_g^n` with `delta_n = det(S | ker P(S))` (7.4); equivalently (7.5); the draft's law holds at `n` iff `delta_n = eta(-1)^{d_n}`.

**What I attacked — the A-matrix argument, symbolically, including `q | n`.**
1. *`A^t = A`, `A^2 = C`, `A^{[q]} = S A`, `A S = S^{-1} A`.* I built `A_{ri} = theta^{q^{r+i}}` in `F_{q^n}` and verified all four identities **as exact identities in `F_{q^n}`** for `(q,n) = (3,1),(3,2),(3,3),(3,4),(3,6),(5,2),(5,3),(5,4),(5,5),(7,3)` — six of which have `q | n` or are otherwise degenerate. All PASS. The point astra makes — that these identities use cyclic indices, not diagonalisation of `S`, hence survive `q | n` where `S` is not semisimple — is exactly right and is what makes the whole theorem uniform in `n`.
2. *Invertibility of `A`.* The argument by shortening a linear relation among distinct field embeddings is the standard Artin argument and is correct; I checked `det A != 0` numerically via `det C != 0`.
3. *The determinant square class on the radical.* `D = det(A|R_n)` in an `F_q`-basis of `R_n`; then `D^2 = det(C|R_n)` (because `A^2 = C` and `A` preserves `R_n`, which needs `P(z) = P(1/z)`) and `D^q = det(S|R_n) D` (because the matrix of `A^{[q]}|R_n` in an `F_q`-basis is the entrywise Frobenius of the matrix of `A|R_n`). Hence `eta(det(C|R_n)) = D^{q-1} = det(S|R_n)`. **I verified both identities exactly in `F_{q^n}`** — including the invariance assertion `A R_n subset R_n`, which the code asserts rather than assumes — for eleven `(q,a,n)` triples covering `dim R_n = 0,1,2,3` and `q | n` (`3,(1,1),6`; `3,(2,1),3`; `3,(0,1,1),6`; `5,(1,1),5`): all PASS (`scratch_rcmps_t7b.py`).
4. *Stickelberger as a corollary.* The same computation on all of `V` gives `eta(det C) = det S = (-1)^{n-1}`. Verified for `n = 1..6, 9` over `q = 3, 5, 7`. This is the right response to the fact — which `notes/extract/riemann-cmps-sources.md` section F records explicitly — that the statement the notebook wants was **not found verbatim in any arXiv TeX source**: astra proves it instead of citing it.
5. *The descent to `V/R_n`.* Both forms descend (a quadratic form vanishes on the radical in odd characteristic), `(CM)bar = Cbar Mbar` because `C` preserves `R_n`, and the determinant ratio in a *common* quotient basis is `det Cbar = det C / det(C|R_n)` — basis-change squares cancel, which is why `eta` of the ratio is well defined. Then `eta(det Cbar) = (-1)^{n-1} delta_n`, and the two Gauss sums share the radical factor `q^{d_n}` and the power `g(psi)^{r_n}`, giving (7.4).
6. *The whole law, end to end.* `S_n = (-1)^{n-1} delta_n t_n` verified against brute-force `S_n` and `Tr E_g^n` for all `n` in range, in **all 12 tuples**: all PASS.

**VERDICT T7.3: VALID**

## T7.4 — the periodic sign and the endpoint criteria

**Claim.** `delta_n = 1` for `n` odd and `(-1)^{min(v_-, q^{v_q(n)})}` for `n` even; boxed `S_n = (1 - 2 [2h | n]) t_n` with `h` the least power of `q` exceeding `v_-`; `v_+-` even; the notebook's `alpha_i = -lambda_i(E_g)` holds for all `n` iff `P(-1) != 0` (7.7); the draft's law holds for all `n` iff `P(-eta(-1)) != 0` (7.8).

**What I attacked.**
1. *The parity of `v_+-`.* Under `z -> 1/z` the local parameter `w = (z-1)/(z+1)` goes to `-w` (and `w = (z+1)/(z-1)` near `-1`), with denominators units because `q` is odd; `P(z) = P(1/z)` then makes the local series even in `w`, so both orders are even. Multiplying by the unit `z^J` does not change the order. Confirmed in every case: `v_- in {0,2,4}`, `v_+ in {0,2}`, never odd.
2. *The multiplicity of `-1` in `z^n - 1`.* For `n` even and `q` odd, `e = q^{v_q(n)}` is odd and `n/e` is even, so `-1` really is a root of multiplicity exactly `e`. For `n` odd, `-1` is not a root at all. Both used, both correct.
3. *The chain to the boxed formula.* `det(S|R_n) = prod` of roots of `gcd(f, z^n-1)`; roots off `+-1` pair up to `1` (both `f` and `z^n-1` are self-reciprocal — I checked `z^{2J} f(1/z) = f(z)`); the root `1` contributes `1`; the root `-1` contributes `(-1)^{min(v_-,e)}`. `min(v_-,e)` is odd iff `e < v_-` (since `e` is odd and `v_-` even) iff `h` does **not** divide `n`. Combining with `(-1)^{n-1}` gives `S_n/t_n = -1` exactly when `n` is even and `h | n`, i.e. `2h | n` since `h` is odd. Every link checked; the boxed law verified numerically in all 12 tuples for all `n` in range.
4. *The two endpoint criteria against the numerics-lane FAIL cases.* This is the decisive test. My independent computation of `v_+-` and of both laws:

| `q` | `a` | `eta(-1)` | `v_-` | `v_+` | `h` | `P(-1)` | `P(-eta(-1))` | (7.7) predicts | observed | (7.8) predicts | observed | numerics lane |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | (0,1) | -1 | 0 | 0 | 1 | `!=0` | `!=0` | holds | holds | holds | holds | both PASS |
| 3 | (1,1) | -1 | 2 | 0 | 3 | `0` | `!=0` | fails | fails | holds | holds | `alpha_i` FAILS, law PASS |
| 3 | **(2,1)** | -1 | 0 | 2 | 1 | `!=0` | `0` | holds | holds | **fails** | **fails** | **law FAIL (n=1,2,4,5,7,8)** |
| 3 | (0,1,1) | -1 | 4 | 0 | 9 | `0` | `!=0` | fails | fails | holds | holds | `alpha_i` FAILS, law PASS |
| 3 | (0,0,1) | -1 | 0 | 0 | 1 | `!=0` | `!=0` | holds | holds | holds | holds | both PASS |
| 3 | (1,0,1) | -1 | 0 | 0 | 1 | `!=0` | `!=0` | holds | holds | holds | holds | both PASS |
| 5 | (0,1) | +1 | 0 | 0 | 1 | `!=0` | `!=0` | holds | holds | holds | holds | both PASS |
| 5 | (1,2) | +1 | 0 | 0 | 1 | `!=0` | `!=0` | holds | holds | holds | holds | both PASS |
| 5 | (1,1) | +1 | 2 | 0 | 5 | `0` | `0` | fails | fails | fails | fails | (T7.5 example) |
| 5 | **(0,1,1)** | +1 | 2 | 0 | 5 | `0` | `0` | fails | fails | **fails** | **fails** | **law FAIL (n=2,4,6)** |
| 7 | (0,1) | -1 | 0 | 0 | 1 | `!=0` | `!=0` | holds | holds | holds | holds | both PASS |
| 7 | (1,1) | -1 | 2 | 0 | 7 | `0` | `!=0` | fails | fails | holds | holds | `alpha_i` FAILS, law PASS |

**12/12 agreement, in both columns, including both of the numerics lane's FAIL cases and all three of its `alpha_i` FAILS.** So the corrected law and the endpoint criteria are not merely consistent with the falsification — they *predict* it from the coefficients alone, and they also predict which of the passing cases pass. In particular for `q=3, a=(2,1)`: `h = 1` so `S_n = (-1)^{n-1} t_n`, and the observed ratios `S_n/t_n = +1,-1,+1,-1,+1` at `n = 1..5` are exactly that, while the draft's `-(-eta(-1))^n conj(t_n)` has the opposite sign at every `n` — matching `outputs/artin_schreier_super.txt` line 112 onward. For `q=5, a=(0,1,1)`: `h = 5`, so the sign flips only at `10 | n`, i.e. never in the tested range `n <= 6` — matching the observed `S_n = t_n` at `n = 2,4,6` where the draft wanted `-t_n`.
5. *The `(7.8)` derivation.* `-(-eta(-1))^n conj(t_n) = (-1)^{n-1} eta(-1)^{d_n} t_n` uses `conj(t_n) = eta(-1)^{r_n} t_n` from T7.1; the criterion `delta_n = eta(-1)^{d_n}` for all `n` reduces to `v_- = 0` when `eta(-1) = 1` and to `v_+ = 0` when `eta(-1) = -1`, i.e. to `P(-eta(-1)) != 0` in both cases. I rechecked the `eta(-1) = -1` half: the congruence `d_n = min(v_+, q^{v_q(n)}) + [2|n] min(v_-, q^{v_q(n)}) (mod 2)` makes `v_+ = 0` sufficient, and `n = 1` (where `e = 1`, `delta_1 = 1`, `d_1` odd) makes it necessary. Correct.

**One cosmetic defect to fix before distillation.** In `<1>3` the displayed congruence is written `... +mathbf1_{2\mid n} ...` — a missing backslash, which will not compile. It should read `\mathbf 1_{2\mid n}`. The mathematics is unaffected.

**VERDICT T7.4: VALID**

## T7.5 — decisive counterexamples

**Claim.** Both proposed universal sign laws are false; the failure occurs already for `n` prime to `q`; explicit cases `(3,(2,1),1)` and `(5,(1,1),2)`, plus a table.

**What I attacked.** I recomputed every row of the table from scratch (`scratch_rcmps_t7b.py`), with `3 sqrt 3 = 5.1962`, `81 sqrt 3 = 140.2961`, `5 sqrt 5 = 11.1803`:

| `q` | `a` | `n` | `S_n` | `t_n` | `d_n` | `delta_n` | astra's table |
|---|---|---|---|---|---|---|---|
| 3 | (2,1) | 1 | `+3.0000` | `+3.0000` | 1 | `+1` | `3, 3, 1` — matches |
| 3 | (2,1) | 2 | `+5.1962i` | `-5.1962i` | 1 | `+1` | `3i sqrt3, -3i sqrt3, 1` — matches |
| 3 | (1,1) | 2 | `+5.1962i` | `+5.1962i` | 1 | `-1` | `3i sqrt3, 3i sqrt3, 1` — matches |
| 3 | (1,1) | 6 | `+81.0000` | `-81.0000` | 2 | `+1` | `81, -81, 2` — matches |
| 3 | (0,1,1) | 6 | `-140.2961i` | `-140.2961i` | 3 | `-1` | `-81 i sqrt3` both, `3` — matches |
| 5 | (1,1) | 2 | `+11.1803` | `+11.1803` | 1 | `-1` | `5 sqrt5` both, `1` — matches |

Every row obeys (7.4). The two worked derivations are also correct in detail: for `q=3, a=(2,1)` the polynomial `g(x) = 2x^2 + x^4` is identically zero on `F_3` (since `x^4 = x^2` there), giving `S_1 = 3`, and the one-site cyclic energy `(2+1)x^2 = 0` gives `t_1 = 3`, `d_1 = 1`, against the draft's `-conj(t_1) = -3`; for `q=5, a=(1,1)`, `Q^circ = (x_0+x_1)^2` gives `t_2 = 5 g(psi) = 5 sqrt 5`, and writing `z = a + b sqrt 2` in `F_25` gives `tr(z^2 + z^6) = 4a^2` — I reproduced that computation (`tr(z^2) = 2a^2 + 4b^2`, `tr(z^6) = 2a^2 - 4b^2`) — so `S_2 = 5 eta(4) g(psi) = 5 sqrt 5` too, against the draft's `-5 sqrt 5`. The claim that the failure is not confined to `q | n` is correct: `n = 1` and `n = 2` are both prime to `3` and `5` respectively. The 628-comparison sweep astra reports is consistent with my 12-tuple sweep.

**VERDICT T7.5: VALID**

## T7.6 — scaled unitarity

**Claim.** `E_g E_g^dag = q I_{q^J}`; `E_g/sqrt q` unitary with semisimple eigenvalues of modulus `sqrt q`; `E_{-g} = conj(E_g)` entrywise.

**What I attacked.** The index bookkeeping: the input column of an output row `y = (u_1..u_{J-1}, x)` is forced to be `s = (z, u_1..u_{J-1})`, so two rows share columns only if `u = u'`, and the sum over the **oldest** spin `z` gives `q 1_{x=x'}` because `a_J != 0` — I re-derived `s_{J+1-j} = u_{J-j}` for `j < J` and `s_1 = z` for `j = J`, confirming astra's phase. Verified `|E E^dag - qI| < 1e-10` in all 12 tuples. The separate `J = 0` treatment (minimal scalar transfer, not the module's redundant `q`-state register) is a real correction and is needed for the "`q^J`-dimensional scaled unitary" claims to be true.

**VERDICT T7.6: VALID**

## T7.7 — the corrected polynomial and the explicit Frobenius spectrum

**Claim.** `L(g,T)^h = prod_{omega^{2h}=1} D_g(omega T) / D_g(T)^h` (7.9); `m_{F_g}(z) = (1/h) sum_omega m_E(omega^{-1} z) - m_E(z)` (7.10); `F_g` diagonal with those multiplicities satisfies `F F^dag = qI`, `L = det(I - T F_g)`, `S_n = -Tr F_g^n`; the simpler blocks hold under (7.7)/(7.8).

**What I attacked — the multiplicity formula, the filter, and where H-AS enters.**
1. *The filter.* `sum_{omega^{2h}=1} omega^n = 2h [2h | n]`, so with `log D_g(T) = -sum t_n T^n/n` and the boxed sign, `log L = -log D_g(T) + (1/h) sum_omega log D_g(omega T)`. I verified the equivalent determinant form `[L(g,T) D_g(T)]^h = det(I - T^{2h} E_g^{2h})` numerically (max coefficient deviation `7.0e-15 / 3.5e-11 / 4.7e-14 / 5.6e-12 / 6.5e-12` for `(3,(0,1)), (3,(1,1)), (3,(2,1)), (5,(0,1)), (5,(1,2))`), which covers `h = 1` and `h = 3`. Astra's own SymPy check at `q=3, a=(1,1), h=3` quotes `L = 1 - i sqrt3 T + ((-3+3i sqrt3)/2) T^2 + ((9+3i sqrt3)/2) T^3`; I recomputed those coefficients from `S_1 = -i sqrt3`, `S_2 = S_3 = 3i sqrt3` by Newton's identities and got exactly the same three numbers.
2. *(7.10).* Taking orders at `T = 1/z` in (7.9) gives the formula; I implemented it directly from the eigenvalues of `E_g` (rotate the spectrum by the `2h` roots of unity, cluster, subtract) and compared `det(I - T F_g)` with the `L` computed independently from brute-force `S_n`: agreement to `2.8e-15 ... 7.9e-14` in 5/5 cases, always with **exactly** `D = q^J` roots, all of modulus `sqrt q` to `1e-6`. The count `sum_z m_F = (2h/h) D - D = D` is right.
3. *Where H-AS is used, and only there.* Astra is explicit: polynomiality is what makes the rational numbers `(1/h) sum_omega m_E(omega^{-1} z) - m_E(z)` nonnegative **integers**; without it (7.9) alone would allow rational or negative multiplicities. He says so in `<1>2` ("that arithmetic step has not been concealed") and repeats it in the status line and the ledger. No Weil root-size input is used anywhere — the `|alpha| = sqrt q` conclusion comes from T7.6 (scaled unitarity of the transfer), not from H-WEIL. That independence is worth preserving in the distillation.
4. *The delimitation.* The closing paragraph shows both directions of the draft's spectral test can fail: for `q=5, a=(1,1)` every `t_n` is real so `spec E_g` is conjugation-invariant yet `P(-1) = 0` and the notebook claim fails; for `q=3, a=(2,1)`, `P(-1) != 0` so the notebook claim holds while `Tr E_g = 3 != -3 = Tr(-conj E_g)` so the spectral symmetry fails. I confirmed both.

**VERDICT T7.7: VALID**

## T7.8 — the corrected projective super-transfer

**Claim.** `C: y^q - y = g(x)` is geometrically connected with one rational point at infinity; `N_n = 1 + q^n + sum_{a != 0} S_n(ag) = str E^n` for the corrected (7.11); `F F^dag = q I_{(q-1)q^J}`; `2g(C) = (q-1)q^J`; the draft's odd block is valid only under (7.8) and is false in general, with `N_1 = 10` for `q=3, g = 2x^2+x^4`.

**What I attacked.**
1. *The projective count and the point at infinity.* The Hilbert-90 step (`y -> y^q - y` is `F_q`-linear with kernel `F_q`, image = trace-zero hyperplane because both have dimension `n-1` and the image has trace zero; the trace map is nonzero because `tr theta != 0` for a normal generator) is correct and is proved rather than quoted. The irreducibility argument (`g != h^q - h` by the pole-order obstruction `q | d` vs `q nmid d = q^J+1`; Galois group of prime order `q`) is correct, and `e = q` at the place above `x = inf` with residue degree `1` gives exactly **one** rational point at infinity over every extension. I checked the count independently by brute force: for `(3,(0,1)), (3,(2,1)), (3,(1,1)), (5,(1,2))` and `n` up to `5` (resp. `4`), the direct projective count, the character sum `1 + q^n + sum_a S_n(ag)`, and `str` of the corrected (7.11) agree **in all 22 comparisons**.
2. *`Tr E_0^n = q^n`.* Verified for `n = 1..5`, `J = 1, 2`, `q = 3, 5`. The structural claims (`E_0^J` is the all-ones matrix, `E_0^{J+1} = q E_0^J`, so the only nonzero eigenvalue is `q` with multiplicity one and the other `q^J - 1` are zero, possibly with nilpotent blocks) are correct — I checked `Tr E_0 = q` (the self-loops) and `Tr E_0^2 = q^2`.
3. *The `N_1 = 10` counterexample.* Reproduced exactly. For `q=3, g = 2x^2+x^4`: all three `x in F_3` have `g(x) = 0` and all three `y` satisfy `y^3 = y`, so the affine count is `9` and `N_1 = 10`; the **draft's** block `-eta(-1) (+)_a E_{ag}` with `-eta(-1) = +1` gives `3 + 1 - 3 - 3 = -2`. My computation prints `str(DRAFT block) = -2.0000` against `N = 10`, and at `n = 5` it prints `298` against `190` — both matching `outputs/artin_schreier_super.txt` Task 3 (`dev = 1.20e+01` at `n=1`, `1.08e+02` at `n=5`, `3.24e+02` at `n=7`) to the digit. The corrected block gives `10` and `190`. The draft's super-transfer is therefore **decisively** disproved, and the disproof is a point count, not a numerical fit.
4. *Non-cancellation and `2g`.* The numerator `prod_{a != 0} L(ag,T)` has degree `(q-1)D` with all reciprocal roots of modulus `sqrt q`, so nothing cancels `1` or `q`; `2g(C) = (q-1)q^J` (also `= (q-1)(d-1)` with `d = q^J+1`, the Riemann–Hurwitz value). Verified in all four cases.
5. *Similarity vs. spectral equality.* Astra separates "the net multiset is forced by T3.2" from "the operator is similar to Frobenius on `H^1`", the latter needing H-FROB-SS, and adds "trace identities alone never determine Jordan blocks". Exactly the right level of care.

**VERDICT T7.8: VALID**

## T7.9 — the explicit symplectic map

**Claim.** `U_g X_{u,v} U_g^{-1} = X_{M_g(u,v)}` **exactly** in the centred Weyl convention, with `M_g` given by (7.13); `M_g` is symplectic; hence `U_g = e^{i theta} W(M_g)` under H-WEIL-EXACT.

**What I attacked — the formula, the convention, and the comparison with the numerics lane.**
1. *The factorisation.* I re-derived the three-step decomposition and checked that it reproduces (7.1)`/sqrt q` including the index relabelling `s_{J+1-j} -> a_{J+1-k} s_k` with the `k=1` term being `a_J s_1 x = c s_1 x`, i.e. exactly the Fourier phase.
2. *The three covariances.* The scaled Fourier kernel `q^{-1/2} psi(c s x)` sends `(u_1,v_1) -> (-v_1/c, c u_1)` **with no residual phase** — I verified both generators by hand (`F X_{1,0} F^dag = X_{0,c}` and `F X_{0,1} F^dag = X_{-1/c,0}`). The quadratic multiplier sends `(u,v) -> (u, v+Ku)` with `K` symmetric, `K_{11} = 2a_0`, `K_{1k} = a_{J+1-k}`, because `(1/2)[(s+u)^t K (s+u) - s^t K s] = (Ku) . (s + u/2)` — the *centred* exponent, which is exactly why the centred convention is the one that kills the phase. The permutation acts identically on `u` and `v`.
3. *Composing to (7.13).* Tracing the three steps gives `u'_k = u_{k+1}` (`k<J`), `u'_J = -v_1/c`, `v'_k = v_{k+1} + a_{J-k} u'_J` (`k<J`), `v'_J = c u_1 + sum_{k=2}^J a_{J+1-k} u_k + 2 a_0 u'_J`. **Identical to (7.13), index for index.** (My first implementation had an off-by-one in the `v'_J` sum and failed; astra's formula is the correct one, and it is what fixed my code.)
4. *Numerics, and the comparison with the numerics lane's `M`.* I built the centred Weyl operators `X_{u,v}|s> = psi(v.(s + u/2))|s+u>` (with `u/2 = u . 2^{-1}` in `F_q`) and checked `U_g X_{u,v} U_g^{-1} = X_{M_g(u,v)}` over **every** phase-space label when `q^{2J} <= 200` and over the generators otherwise:

| `(q,a)` | labels tested | max entrywise residual |
|---|---|---|
| `(3,(0,1))`, `(3,(1,1))`, `(3,(2,1))` | 9 each | `5.6e-16` |
| `(3,(0,1,1))`, `(3,(0,0,1))`, `(3,(1,0,1))` | 81 each | `7.6e-16` |
| `(5,(0,1))`, `(5,(1,2))`, `(5,(1,1))` | 25 each | `3.1e-16` |
| `(5,(0,1,1))` | generators | `2.8e-16` |
| `(7,(0,1))`, `(7,(1,1))` | 49 each | `4.6e-16` |

`M_g` is symplectic mod `q` in all 12 cases. **And the matrices agree exactly with the numerics lane's extracted `M`** — e.g. `q=3, a=(0,1,1)`: mine is `[[0,1,0,0],[0,0,2,0],[0,0,2,1],[1,1,0,0]]`, identical to `outputs/artin_schreier_super.txt`; `q=5, a=(0,1,1)`: `[[0,1,0,0],[0,0,4,0],[0,0,4,1],[1,1,0,0]]`, identical; `q=3, a=(2,1)`: `[[0,2],[1,2]]`, identical; `q=7, a=(1,1)`: `[[0,6],[1,5]]`, identical. **The difference between the conventions is exactly the phase and nothing else:** the numerics lane, using the uncentred `W(u,v) = X^u Z^v`, records nontrivial phases (`-0.5 + 0.866i` for `q=3, a=(1,1)`; `0.309 - 0.951i` for `q=5, a=(1,2)`; `0.623 + 0.782i` for `q=7, a=(1,1)`), while in astra's centred convention every one of those phases is `1` to `8e-16`. That is precisely the point of H-WEIL-EXACT and the reason astra rejected H-WEIL-REP's word "phase": with arbitrary label-dependent phases one can multiply by a Weyl displacement and change the trace, so the implementer would not be determined up to a scalar.
5. *The scalar ambiguity.* "Commutes with every `X_{0,v}` ⟹ diagonal; commutes with every `X_{u,0}` ⟹ constant diagonal" is correct and needs the *exact* covariance, as astra notes.

**VERDICT T7.9: VALID**

## T7.10 — fixed spaces, the Weil bound, the permutation sign

**Claim.** `|Tr E_g^n|^2 = q^{n + dim ker(M_g^n - I)}` (7.14) with `d_n = dim ker(M_g^n - I) <= 2J`; saturation iff `M_g^n = I`; `S_n = (-1)^{n-1} Tr E_g^n` when `d_n = 0`.

**What I attacked — the character-modulus identity via `Tr Ad(U) = #fixed Weyl labels`.** The `q^{2J}` centred Weyl matrices are a Hilbert–Schmidt-orthogonal basis of `End(C^{q^J})` (a nontrivial shift has zero diagonal, a nontrivial phase has zero character sum), exact covariance makes `Ad(U_g^n)` a **permutation** of that basis with coefficient `1` on every fixed label, so `Tr Ad(U_g^n) = #ker(M_g^n - I) = q^{dim ker}`, and `Tr Ad(V) = |Tr V|^2` for unitary `V`. Since `E_g^n = q^{n/2} U_g^n`, (7.14) follows. **This proves H-WEIL-REP's character-modulus clause rather than assuming it**, which is the right structure. I verified `|Tr E_g^n|^2 = q^{n + dim ker(M^n - I)}` for `n = 1..6` in all 12 tuples (72 comparisons, all exact), independently of `outputs/artin_schreier_super.txt` Task 4 which reports the same for `n = 1..12` in 11 cases.

The bound `d_n <= 2J` has two independent proofs (the `gcd` description with `deg(z^J P(z)) = 2J`, and the kernel of a map on a `2J`-dimensional space), and saturation `d_n = 2J` iff `M_g^n - I = 0` is immediate. The worked example `q=3, a=(0,1)`: `M_g = [[0,-1],[1,0]]`, order `4`, `d_2 = 0`, `d_4 = 2 = 2J` — confirmed by my `M` and by the numerics lane's `d'_n = [0,0,0,2,...]`. The final caution — "equality of the dimensions in (7.14) by itself does not identify determinant actions on the two different fixed spaces", i.e. `dim ker(M_g^n - I)` on `F_q^{2J}` and `dim ker P(S)` on `F_q^n` agree as *numbers* but the determinant correction `delta_n` is computed on the second, not the first — is exactly the distinction that makes the draft's `eta(-1)^{d_n}` correction wrong. Correct and well flagged.

**VERDICT T7.10: VALID**

---

# T8. Ledger and scope

## T8.1 — the established scope of the Phantasm

**Claim.** The data force and realise a graded single-particle **spectral** Phantasm and a genuine absorbing-vacuum channel with the zero channel in its odd coherences; they do **not** establish a nontrivial cMPS whose norm is the prime measure with a normal critical Bost–Connes stationary bond.

**What I attacked.** I read every row of the T8 ledger against the proof it refers to. All rows are accurate. In particular the rows that are corrections rather than confirmations — T1(a) (full complex `lambda`), T1(b) (cutoffs), T2(b) (leading trigonometric polynomial, not one cosine), T2(c) (domination premise, missing step located), T4 (`Tr_dist Z = 1 - 2P_+ - e^{-t/2}/(e^t-1)`), T5(a) (unique stationary **density**, fixed-operator space `C Omega`), T5(d) (doubled coherence list), T5(e) (the rebound integral is **not** solved by `Omega`), T6(a) (representation and temperature), T6(b) (closure and choice of Hilbert space), T7(a) (the trace form is `CM`, not `M`; self-duality unavailable for even `n`), T7(b) (the determinant of the shift on the radical, not `eta(-1)^{d_n}`), T7(d) (the `N_1 = 10` disproof), T7(e) (arbitrary phases do not characterise a Weil implementer) — are each ones I independently confirmed above. The open list (unrestricted T2(c); validation of H-LP; the critical cMPS/renewal/prime-jump realisation) is accurate, and the sentence "neither RH nor the existence of the full physical Phantasm is proved" is the correct summary.

Two additions I would make to the ledger, neither a correction of a false row: (i) the T2(c) row should record that `b = 0` needs **no** domination (T2.3 above); (ii) the T7(e) row should record that in the *centred* convention the covariance has no phase at all, and that this is what distinguishes it from the uncentred convention used by the numerics lane — the symplectic matrix is the same in both.

**VERDICT T8.1: VALID**

---

# The H-* inventory

I checked each H-* against (a) what the file actually uses it for and (b) the byte-verified quotes in `notes/extract/riemann-cmps-sources.md`, re-grepping with `grep -n -a -F` where I relied on a quote.

- **H-ZEF-T.** Rederived from `psi_0` independently (T1.3 above); the archimedean sign, the `x`-multiplication and the pullback are all right, and astra's caveat that "differentiation alone recovers the antiderivative only up to a constant" is the correct hedge. **VERDICT H-ZEF-T: VALID**
- **H-ZERO-COUNT.** Standard; astra's added precision about the counting convention (`0 < Im rho <= T`, with multiplicity, asymptotic) is what makes it usable for (G2). **VERDICT H-ZERO-COUNT: VALID**
- **H-ZETA-LOC.** Added by astra, not in the brief; and it is genuinely needed three times (strip for (G1); **nonzero imaginary part** for "A has no constant term" in T2.2 and for "no real poles" in T2.3; the two symmetries for T1.4/T4.1). No RH content. **VERDICT H-ZETA-LOC: VALID**
- **H-SCHWARTZ.** Standard; the added sentence "this is positivity, not positive definiteness on convolutions" is the right warning given the earlier Weil-positivity file. **VERDICT H-SCHWARTZ: VALID**
- **H-LANDAU.** Faithful to the byte-verified statement at `1009.0228:main.tex:173-179` in its Dirichlet form, correctly transposed to the Laplace form (Widder Ch. II Thm 5b, cited as a textbook). The added clause "a measure with abscissa `-inf` is outside this assertion" is not decoration: it is exactly the case T2.3 has to exclude. **VERDICT H-LANDAU: VALID**
- **H-LIDSKII.** Faithful to `1105.2914:main.tex:225-240` including "eigenvalues written according to their algebraic multiplicities". The additions (`sum|lambda_i| < inf`, zero eigenvalues need not be listed, each `E^n` trace class) are all true and all used. **VERDICT H-LIDSKII: VALID**
- **H-WEIL.** The added "geometrically connected" is necessary (otherwise the even list `{1,q}` changes) and astra says why. **VERDICT H-WEIL: VALID**
- **H-LP.** Honestly labelled as assumed operator data, with an explicit list of what is *not* established from the symbol (innerness, completeness, the geometric identification). **VERDICT H-LP: VALID**
- **H-TRACE.** Explicitly a definition by fiat, with the correct note that H-ZETA-LOC and T1.1 are also needed for convergence and that this is not Lidskii applied to `Z(t)`. **VERDICT H-TRACE: VALID**
- **H-CMPS.** Faithful to `1002.1824:mpsQFT4.tex:81` ("the eigenvalues of the matrix `rho(x)` would exactly correspond to the squares of the Schmidt coefficients"), and astra's sharpening — equality of **nonzero** spectra / identification of supports by an isometry, not literal operator equality, with the general form `sqrt l r sqrt l` — is the correct canonical-form statement and is what T5.5 needs in the rank-deficient case. **VERDICT H-CMPS: VALID**
- **H-BC.** Recorded verbatim as supplied and then explicitly corrected in two places (the algebra is the BC `C^*`-algebra, not `B(l^2)`; the range is `0 < beta <= 1`). Recording-then-correcting rather than silently using the overbroad form is the right discipline. **VERDICT H-BC: VALID**
- **H-BC-POS.** The uniqueness-for-`0 < beta <= 1` clause and the `beta > 1` Gibbs classification are faithful to `math/0404128:houcheschapter1final7.tex:1815-1849`. **The type III`_1` clause is not.** The only byte-verified support in the repository is the dictionary table at `math/0404128:...:688-695`, which labels the **"System at critical temperature"** as type III`_1` — i.e. `beta = 1` — and the sources file itself records the caveat that this passage "does **not** in these passages prove or restate the type-`III_1` factor claim". Astra's attribution line ("as supplied; no external source was consulted") is honest, and T6 uses the clause only for a comparison that no proof depends on, so nothing downstream breaks. But the hypothesis as written asserts more than the local evidence carries. **Fix:** split it — "(i) for `0 < beta <= 1` there is a unique KMS`_beta` state [Connes–Marcolli `math/0404128` Thm, byte-verified]; (ii) its GNS von Neumann algebra is a factor of type III`_1` [Bost–Connes 1995, *not* byte-verified in this repository; `math/0404128` only labels the critical temperature III`_1` in its dictionary table]". **VERDICT H-BC-POS: MINOR**
- **H-MM1.** Supplied, then **proved** in T6.2 on a precisely specified weighted space, with the boundary convention (`omit the down jump at k=0`, backward generator on functions, `L^2(pi)`) spelled out. Verified numerically. **VERDICT H-MM1: VALID**
- **H-GAUSS.** Supplied, then **proved** in T7.1, with the determinant convention declared. Since only ratios in a fixed convention are used, the (real) discrepancy between the Lidl–Niederreiter and Weil-index normalisations is harmless, and astra flags it. **VERDICT H-GAUSS: VALID**
- **H-STICK.** The sources file records that the wanted statement was **not found verbatim in any arXiv TeX source** (only the unrelated `disc Z_K = 0,1 mod 4` theorem of the same name, at `2208.06138:main.tex:219-225`). Astra's response — prove it from H-NORMAL and the embedding matrix in T7.3 `<1>2` — is the correct one, and I verified the resulting `eta(det C) = det S = (-1)^{n-1}` for `n = 1..6, 9` over `q = 3,5,7`. The independent parity confirmation from `1007.4899` (self-dual normal basis exists iff `n` odd, for odd `q`) is consistent. **VERDICT H-STICK: VALID**
- **H-NORMAL.** The self-dual clause is faithful to the Lempel–Weinberger quote at `1007.4899:selfdualnb_elsart6.tex:258-271` (`n` odd, or `n = 2 mod 4` with `q` even), and astra restricts to odd `q` correctly. The general sign proof uses only the existence of a normal basis, as stated — this matters, because a self-dual normal basis does **not** exist for even `n` and the whole point of T7.3 is to handle even `n`. **VERDICT H-NORMAL: VALID**
- **H-WEIL-REP.** The character-modulus clause `|Tr W(M)|^2 = q^{dim ker(M-1)}` is faithful to Thomas's Theorem 1A at `math/0610644:ArxivThomasWeil3.tex:187-198` (`|gamma| = 1`, so the modulus is `|F|^{(1/2) dim ker(g-1)}`) and to the Howe remark at lines 202-203. Astra's objection to the word "phase" is correct and important, and he proves the character-modulus clause rather than using it. **VERDICT H-WEIL-REP: VALID**
- **H-WEIL-EXACT.** Faithful to `quant-ph/0602001:poswig.tex:504-545` (Gross: `mu(S) w(v) mu(S)^dag = w(Sv)`, no phase) and to the Egorov characterisation at `math/0610818:main.tex:414-429` ("determined up to scalar by `rho(g) pi(h) rho(g)^{-1} = pi(g.h)`"). My numerics confirm that the exact, phase-free form holds in the centred convention for all twelve transfer matrices. **VERDICT H-WEIL-EXACT: VALID**
- **H-AS.** Standard Artin–Schreier `L`-polynomial theorem; astra is explicit that polynomiality is arithmetic input, that it is **not** to be inferred from a sign law, that the degree is exactly `q^J`, and that **no** root sizes are assumed. Its single use — nonnegativity and integrality in (7.10) — is declared in three places. **VERDICT H-AS: VALID**
- **H-FROB-SS.** Added, and correctly scoped to operator similarity only; the forced net multiset and the constructed transfer do not use it, and the sentence "no positive Hermitian metric on the original cohomological realization is part of this hypothesis" forecloses the obvious over-reading. **VERDICT H-FROB-SS: VALID**

---

# The orchestrator's three statements

## X1 — character-sector grading, and the Bost–Connes analogy

**Statement.** "The `Z_2` grading of the Artin–Schreier super-transfer matrix is the decomposition into the trivial versus nontrivial additive-character sectors of the Hilbert-90 fibre sum; the trivial sector carries exactly the two poles of `Z_C` and the nontrivial sectors exactly the zeros."

**Is this a correct reading of T7.8 as proved?** Substantially yes, with two wording fixes that matter.

*What is proved.* The Hilbert-90 decomposition is `#{(x,y) affine} = sum_{a in F_q} S_n(ag)` with `S_n(0.g) = q^n` (T7.8 `<1>1`, which I confirmed by direct point count in 22 cases). (7.11) puts `E_0` (with `Tr E_0^n = q^n`, i.e. the `a = 0` term) **and** an extra `1` in the even block, and `(+)_{a != 0} F_{ag}` in the odd block. Exponentiating gives `Z_C(T) = prod_{a != 0} L(ag,T) / [(1-T)(1-qT)]`, and T7.8 `<1>4` proves there is **no** cancellation between numerator and denominator (`|alpha| = sqrt q != 1, q`). So: even block ⟷ poles, odd block ⟷ zeros, and the odd block is indexed by the nontrivial additive characters. That much is exactly right and is the honest arithmetic content of the grading.

**Fix 1 (the point at infinity is not a character sector).** The even block is `E_0 (+) 1`, and the extra `1` is the rational point at infinity, which is **not** part of the Hilbert-90 fibre sum (that sum is the *affine* count). The two poles are therefore split: the pole at `T = 1/q` comes from `E_0`, i.e. from the trivial character sector; the pole at `T = 1` comes from the point at infinity. So "the trivial sector carries exactly the two poles" should read "the even sector carries exactly the two poles: `T = 1/q` from the trivial-character sector `E_0`, and `T = 1` from the point at infinity". The grading is the trivial/nontrivial character decomposition of the **affine** count, **plus one extra even line**.

**Fix 2 (the odd blocks are `F_{ag}`, not `E_{ag}`).** "The direct sum over the nontrivial characters `a`" is right as an indexing statement, but each summand is the **corrected** block `F_{ag}` of (7.10), not `-eta(-1) E_{ag}`. Substituting `E_{ag}` is precisely the draft error that T7.8 `<1>5` disproves with `N_1 = 10` vs `-2`. Any distillation of X1 must carry the corrected block or the endpoint condition (7.8).

**Fix 3 (a precision, not an error).** "Carries exactly" is true of the **nonzero net** spectrum. The even block also carries `q^J - 1` zero eigenvalues (invisible to all positive-power traces, possibly with nilpotent blocks), which carry no pole. Astra states this; the X1 wording should not lose it.

**The Bost–Connes analogy.** Status: **observation, not a theorem** — and it should be labelled so. Its ingredients are individually sound: `Gal(Q^ab/Q) = Zhat^x` has the Dirichlet characters as its (continuous) character group; `prop:bc-mpo` (`report/sections/04_riemann_channel.tex`, `\label{prop:bc-mpo}` — l.252–259 as of this review; the shard was edited by another lane at 22:35, so cite the label, not the line) gives transfer eigenvalues `L(beta, bar chi)/zeta(beta)` in the character basis; only the principal character's `L`-function has a pole at `s = 1`. So a Galois-symmetric graded bond would have even sector ⟷ the pole of `zeta`, odd sector ⟷ the zeros of the `L(s,chi)`.

**Consistency with what is proved, and one thing the proofs *do* say.** Nothing in the file contradicts the analogy. But T7.8 makes it more precise in a way the orchestrator should keep: in the Artin–Schreier case the graded object computes the zeta function **of the cover**, `Z_C`, whose numerator is `prod_{a != 0} L(ag,T)` — *all* the nontrivial characters together — and **not** the zeta function of the base `P^1`. The faithful analogue is therefore that a Galois-graded prime-chain bond would compute the Dedekind zeta of `Q(zeta_N)` (all Dirichlet characters mod `N` at once), not `zeta` alone. That is a testable consequence: by T1.2, a graded datum whose supertrace is `2 P_+` has the net spectrum of T4's `G` and **only** the zeta zeros; a datum carrying the zeros of all `L(s,chi)` would have a different supertrace (the corresponding ray-class prime comb). The two cannot both hold for the same bond.

Two further honest caveats. (i) `prop:bc-mpo` is `sketched`, and its eigenvalues `L(beta, bar chi)/zeta(beta)` are *values* of `L` at a fixed `beta`, not *zeros* of `L`; nothing in the notebook puts any `L`-zero into the prime chain. (ii) T6.3/T6.4 prove the prime-chain generator's spectrum is real (classically in general, and for the full generator on the weighted space under `sum r_p p^beta < inf`), so the existing prime-chain construction demonstrably is **not** the Galois-symmetric graded bond the analogy imagines. The analogy is a research direction, not a corollary.

**VERDICT X1: MINOR**

## X2 — entropy of the Gibbs state and cutoffs

All four checked in `scratch_rcmps_x2x3.py`; `scripts/bc_entropy.py` was **not** imported (the geometric entropy, the sieve to `2 x 10^7`, the Mertens sums and the Stieltjes constants were recoded).

### X2(a)

**Statement.** `S(rho_beta) = log zeta(beta) - beta zeta'(beta)/zeta(beta)` for `beta > 1`, and `S ~ 1/(beta-1) + log(1/(beta-1))` as `beta -> 1^+`.

**What I checked.** The closed form is immediate from `p_n = n^{-beta}/zeta(beta)` and `zeta'(beta) = -sum n^{-beta} log n`; I confirmed it against the direct von Neumann entropy with a tail estimate at `beta = 3, 2, 1.5, 1.2`. The asymptotic is where the statement needs a fix. With `zeta = 1/eps + gamma + O(eps)` and `zeta' = -1/eps^2 - gamma_1 + O(eps)` (`eps = beta-1`),

`-beta zeta'/zeta = 1/eps + 1 - gamma + O(eps)`, `log zeta = log(1/eps) + O(eps)`,

so **`S = 1/(beta-1) + log(1/(beta-1)) + (1 - gamma) + o(1)`** with `1 - gamma = 0.42278434`. Numerically, `S - [1/eps + log(1/eps)]` at `eps = 10^{-3}, 10^{-5}, 10^{-7}, 10^{-9}` is `0.42297192, 0.42278621, 0.42278435, 0.42278434` — converging to `1 - gamma` to eight digits. This is exactly the `+0.4230` that `outputs/bc_entropy.txt` already reports at `beta = 1.001` and `+0.4247` at `beta = 1.01`, so the notebook's own numerics already contain the constant.

**The fix.** As a two-term asymptotic with an unwritten `O(1)` remainder the statement is true, but written as "`S ~ A + B`" it invites the reading `S - A - B -> 0`, which is false. Write `S(rho_beta) = 1/(beta-1) + log(1/(beta-1)) + (1 - gamma) + o(1)`.

**VERDICT X2a: MINOR**

### X2(b)

**Statement.** Prime cutoff `p <= P` at `beta = 1`: `S_P = log P + log log P + C + o(1)`; determine `C`.

**What I checked.** The per-prime entropy is exactly `S_p = -log(1-1/p) + log p/(p-1)` (verified to `1e-14`), so `S_P` splits into the two Mertens sums the orchestrator names. Summing primes to `2 x 10^7` with my own sieve:

| `P` | `sum_{p<=P} log p/(p-1) - log P` | `sum_{p<=P} -log(1-1/p) - log log P` | `S_P - log P - log log P` |
|---|---|---|---|
| `10^3` | `-0.543870` | `+0.581090` | `+0.037221` |
| `10^4` | `-0.564210` | `+0.578447` | `+0.014237` |
| `10^5` | `-0.573274` | `+0.577520` | `+0.004246` |
| `10^6` | `-0.576560` | `+0.577255` | `+0.000695` |
| `10^7` | `-0.577029` | `+0.577225` | `+0.000197` |
| `2 x 10^7` | `-0.576954` | `+0.577230` | `+0.000276` |

The first column converges to `-gamma = -0.577216` and the second to `+gamma`. The first is Mertens in the form `sum_{n <= x} Lambda(n)/n = log x - gamma + o(1)`: indeed `sum_{p<=P} log p/(p-1) = sum_{p<=P} log p/p + sum_p log p/(p(p-1)) + o(1)`, and the second sum is exactly the prime-power tail of `sum Lambda(n)/n`. The second is Mertens' third theorem, `prod_{p<=P}(1-1/p)^{-1} ~ e^gamma log P`.

**Therefore `C = (-gamma) + (+gamma) = 0` exactly.** It is not merely small: the two Euler–Mascheroni constants cancel identically, and the residual `+0.0007` at `P = 10^6` (which is what `outputs/bc_entropy.txt` reports as "about 0.001") is the `o(1)`, decaying like the Mertens error terms. This is a pretty fact and worth stating with the cancellation visible rather than as a numerical near-zero.

**VERDICT X2b: VALID**

### X2(c)

**Statement.** Bond cutoff `n <= N` at `beta = 1`: `S_N = (1/2) log N + log log N + C' + o(1)`; determine `C'`.

**What I checked.** With `p_n = (1/n)/H_N`, `S_N = (sum_{n<=N} log n / n)/H_N + log H_N`. Using `H_N = log N + gamma + O(1/N)` and `sum_{n<=N} log n/n = (log^2 N)/2 + gamma_1 + o(1)` (`gamma_1 = -0.0728158455`, the first Stieltjes constant):

`S_N = (1/2) log N + log log N - gamma/2 + (gamma^2/2 + gamma_1 + gamma)/log N + O(1/log^2 N)`.

So **`C' = -gamma/2 = -0.288608`**, and the `1/log N` coefficient is `gamma^2/2 + gamma_1 + gamma = 0.67099`. Direct summation:

| `N` | `S_N - (1/2)log N - log log N` | two-term prediction |
|---|---|---|
| `10^4` | `-0.218212` | `-0.215756` |
| `10^5` | `-0.231929` | `-0.230326` |
| `10^6` | `-0.241161` | `-0.240040` |
| `10^7` | `-0.247806` | `-0.246978` |
| `10^8` | `-0.252818` | `-0.252182` |

and continuing with the asymptotic forms to `N = 10^{10}, 10^{14}, 10^{20}, 10^{40}` the residual after subtracting the two-term prediction is `-4.1e-04, -2.1e-04, -1.0e-04, -2.6e-05`, i.e. `O(1/log^2 N)` as it should be.

**Caution for the write-up.** `outputs/bc_entropy.txt`'s "approaching about `-0.25`" is a finite-`N` artefact: at `N = 10^7` the `1/log N` term still contributes `+0.042`. The limit is `-gamma/2 = -0.2886`, and the approach is logarithmically slow, so no amount of direct summation will display it. The statement as posed ("`+ C' + o(1)`; determine `C'`") is correct; the value is `-gamma/2`.

**VERDICT X2c: VALID**

### X2(d)

**Statement.** The number of entanglement levels below `E` is `floor(e^E)`: exponential (Hagedorn) growth, not Cardy growth, so the finite-entanglement-scaling law for CFTs does not apply.

**What I checked.** `#{n : log n <= E} = floor(e^E)` is exact. Hagedorn temperature `beta_H = 1`, because `sum_n e^{-beta log n} = zeta(beta)` converges iff `beta > 1` — which is the *same* threshold as the Bost–Connes transition, and that is the substantive point. Against Cardy's `exp(2 pi sqrt(cE/6))` (which is sub-exponential): at `E = 10` the counts are `22026` vs `3333`, at `E = 20` they are `4.85 x 10^8` vs `9.6 x 10^4`. So the entanglement-level density is exponential, not Cardy, and the input to the CFT finite-entanglement-scaling derivation (a Cardy-type entanglement spectrum, giving `S = (c kappa/6) log chi`) is absent. The independent signature is in X2(c): the truncated entropy is `(1/2) log N + log log N - gamma/2`, which is **not** of the form `alpha log chi` — the `log log N` term is the departure.

*One precision to carry.* The entanglement spectrum of `rho_beta` is `{beta log n + log zeta(beta)}`, so the level count below `E` is `floor(e^{(E - log zeta(beta))/beta})`; `floor(e^E)` is the count for the bare entanglement-Hamiltonian spectrum `{log n}` (i.e. `beta = 1` with the additive constant dropped). At `beta = 1` there is no normal Gibbs state at all (T6.1), so the clean statement is about the spectrum of `log N`, not about a state. The rescaling by `beta` is an affine reparametrisation and changes nothing about exponential-vs-Cardy.

**VERDICT X2d: VALID**

## X3 — complementary halves

**Statement.** "The vacuum-decay channel of T5 has the zeros as its odd relaxation modes but a pure fixed point (trivial entanglement); the prime-chain Gibbs Lindbladian of T6 has the Bost–Connes Gibbs state as fixed point (entanglement spectrum = ring lengths) but a real spectrum containing no zeros; the Phantasm, if it exists, must have both, and no construction in the notebook has both."

**Is this a faithful corollary of T5 and T6 as proved?** The *shape* is faithful and it is the correct summary of T8.1 `<1>1`. Three qualifications are needed before it can stand as a corollary rather than a slogan; each is something astra states and the compression drops.

1. **"has the zeros as its odd relaxation modes" understates the odd sector.** T5.1 `<1>5` gives odd spectrum `spec(B) u conj spec(B)`. Since the zeta multiset is conjugation invariant, **each** value `-conj(rho)/2` occurs with total multiplicity `2 m_rho`, not `m_rho` — once on `|v_n><vac|` and once on `|vac><v_n|`. T4's forced datum (T1.4) has `nu = -m_rho`. So T5's channel does **not** realise T4's graded datum; it realises its double. Moreover the T5 even sector carries `{0} u {b_i + conj b_j}` — `d^2 + 1` modes, the pair sums — which T4's datum does not have at all, and whose infinite-dimensional version violates (G2) (T5.4). The corollary should read "has each zero twice as an odd relaxation mode, plus an even population sector of pair sums that T4's datum does not contain".
2. **"entanglement spectrum = ring lengths" is off by a factor and a constant.** T6.1 gives `spec(-log rho_beta) = {beta log n + log zeta(beta)}`. T4's ring lengths are `2 log n`. These coincide only at `beta = 2` and only up to the additive `log zeta(beta)`; astra's ledger already records this ("the two conventions differ by that factor"). Say "entanglement spectrum `beta log n + log zeta(beta)`, proportional to the ring lengths `2 log n`".
3. **"a real spectrum containing no zeros" is proved at two different strengths.** T6.3 proves it for the **classical/diagonal** part, on `L^2(pi)`, for `beta > 1` and any positive summable up-rates — that is unconditional. T6.4 extends it to the **full quantum generator** only (i) under the stronger rate condition `sum_p r_p p^beta < inf` (which the draft's `r_p = p^{-beta}` fails) and (ii) on the explicitly specified KMS-weighted Hilbert space, with astra disclaiming any transfer to unweighted operator spaces or unbounded closures. And the fixed point exists only for `beta > 1`: at the Bost–Connes point `beta = 1` there is **no** normal Gibbs state (T6.1), so "has the Bost–Connes Gibbs state as fixed point" must be read at `beta > 1`, above the transition — which is itself part of why the two halves do not meet.

With those three repairs the sentence is a faithful corollary: T8.1 `<1>1` says precisely that T5.3 supplies a true CPTP semigroup with exact zero coherences but a rank-one stationary density (T5.5), that T6.1 excludes a normal critical KMS density, and that "none of these deductions identifies that absorbing state with the critical arithmetic state or its cMPS entanglement spectrum". The last clause of X3 ("no construction in the notebook has both") is exactly T8.1's scope audit and is accurate. The middle clause ("the Phantasm, if it exists, must have both") is definitional, not a theorem, and should be labelled as the definition it is.

**VERDICT X3: MINOR**

---

# Summary of verdicts

| Label | Verdict | One-line reason |
|---|---|---|
| T1.1 | VALID | full-complex-`lambda` integration by parts is the right fix; (G2) with `N >= 2` holds for the zeta multiset and suffices |
| T1.2 | VALID | cutoffs are genuinely in `C_c^inf(0,inf)`, the `eps^{k-l-j+1}` bookkeeping is right, tail summable by (G2); pairing reproduced to `1.4e-14` |
| T1.3 | VALID | rederived from `psi_0`: archimedean sign `-1/(e^{2u}-1)` and Jacobian `2` both confirmed |
| T1.4 | VALID | `{rho-1} = {-conj rho}` as multisets; `e^{-t/2} = 1/n` at the atom; (G1),(G2) survive the transport |
| T2.1 | VALID | necessity via T1.2, not via a naive reindex |
| T2.2 | VALID | leading-slice mean/mean-square lemma is airtight and handles several real parts; 400/400 numerical confirmations |
| T2.3 | **MINOR** | true, but **`b = 0` needs no domination premise and no Landau** — proof supplied; the premise is genuinely needed only for `F_Z = empty` |
| T2.4 | VALID | the missing step (possible negative prime atoms in `mu - comb`) is located exactly; I confirmed Landau is toothless because `sigma_c = 1` from `nu(1) = +1` |
| T3.1 | VALID | residue `-1/alpha` verified symbolically; trace-class meromorphy argument is correct |
| T3.2 | VALID | `Z = det(1-uE_-)/det(1-uE_+)` verified to `1e-12`; the "no zero-free exponential factor" clause is necessary |
| T3.3 | VALID | MPS corollary exactly stated (fixed, finite, translation-invariant, all `n`); ring-norm identity reproduced; Prony recovers 4 negative multiplicities |
| T4.1 | VALID | every sign rederived; `Tr_dist Z = 1 - 2P_+ - e^{-t/2}/(e^t-1)` confirmed to `1.3e-05` relative with 260 zeros; three wrong variants rejected by `10^3`–`10^4` |
| T4.2 | VALID | both ladder variants positive to `9.4e-06`; all-even exclusion immediate from T1.4 |
| T4.3 | VALID | `Z(t)` non-compact (eigenvalue moduli `> e^{-t/2}`); `xi` entire; RH restricted to the odd `K_S` modes |
| T5.1 | VALID | (5.2), CP via the Kraus rows, and (5.1) with multiplicities all verified to `1e-14` at `D = 3, 5`; grading commutes to `1e-11` |
| T5.2 | VALID | `|1 +- Tr Z_t|^2` verified in 8/8 comparisons |
| T5.3 | VALID | semigroup law telescopes; contraction needed and stated; no bounded exit vector assumed |
| T5.4 | VALID | doubling and the (G2) violation of the pair list both stated; no pair-correlation claim |
| T5.5 | VALID | renewal integral `= T Omega` (trace `5.00000000` at `T=5`); every one-jump ring amplitude is `0.00e+00` |
| T6.1 | VALID | `p_n = (n/m)^{-beta} p_m` verified over `144` pairs; the normal-vs-arithmetic distinction is drawn honestly |
| T6.2 | VALID | band containment `3000/3000` in 4/4 cases; `m(0) = z/a` confirmed by a direct `2001`-dim resolvent solve |
| T6.3 | VALID | `I_p` reproduced for `p = 2,3,5,7`; the closure **is** essential (infinite sum of left endpoints converges to `-1.0025`) |
| T6.4 | VALID | `sector(delta!=0) = sector(0) - (mu/2)|e_0><e_0|` verified exactly; all sectors nonpositive |
| T6.5 | VALID | `Tr(P rho_beta) <= rank(P)/zeta(beta)`; elementary divergence of `sum 1/p`; correctly refuses to call it ergodicity breaking |
| T7.1 | VALID | Gauss evaluation proved, not quoted; determinant convention declared and only ratios used |
| T7.2 | VALID | ring form verified by brute force for all `n` including `n <= J`; trace-form matrix is `CM` with the right factors of two |
| T7.3 | VALID | `A^t=A`, `A^2=C`, `A^{[q]}=SA`, `AS=S^{-1}A` verified exactly in `F_{q^n}` for 10 cases incl. `q|n`; `D^2 = det(C|R_n)`, `D^q = det(S|R_n)D` verified for 11 triples; (7.4) holds in 12/12 tuples |
| T7.4 | VALID | `v_+-` even; `delta_n` and the boxed `1-2[2h|n]` verified; **(7.7) and (7.8) reproduce the numerics lane 12/12, including both FAIL cases** (one `\mathbf 1` typo to fix) |
| T7.5 | VALID | all six table rows recomputed exactly; both worked counterexamples reproduced by hand and by machine |
| T7.6 | VALID | `E E^dag = qI` in 12/12; the `J = 0` minimal convention is a real and necessary correction |
| T7.7 | VALID | (7.9) verified for `h = 1, 3`; (7.10) gives exactly `q^J` roots on `|z| = sqrt q` and `det(I-TF) = L` to `1e-13`; H-AS used only where declared |
| T7.8 | VALID | 22/22 point-count comparisons; the `N_1 = 10` vs `-2` disproof of the draft block reproduced exactly |
| T7.9 | VALID | (7.13) rederived index for index; **exact phase-free centred covariance, residual `<= 7.6e-16` over all labels**; `M_g` identical to the numerics lane's in all 10 cases |
| T7.10 | VALID | `Tr Ad(U^n) = #` fixed Weyl labels proved, not assumed; `|Tr E^n|^2 = q^{n+d_n}` in 72/72 comparisons |
| T8.1 | VALID | every ledger row checked against its proof; the open list is accurate |
| H-ZEF-T / H-ZERO-COUNT / H-ZETA-LOC / H-SCHWARTZ / H-LANDAU / H-LIDSKII / H-WEIL / H-LP / H-TRACE / H-CMPS / H-BC / H-MM1 / H-GAUSS / H-STICK / H-NORMAL / H-WEIL-REP / H-WEIL-EXACT / H-AS / H-FROB-SS | VALID (each) | faithful to the byte-verified quotes where quotes exist; proved in-file where they do not (H-MM1, H-GAUSS, H-STICK, the character modulus) |
| H-BC-POS | **MINOR** | the type III`_1` clause for all `0 < beta <= 1` exceeds the byte-verified quote, which labels only the **critical temperature** III`_1`; split the citation |
| X1 | **MINOR** | correct reading, but the even block is the trivial sector **plus the point at infinity** (which supplies the pole at `T=1`), and the odd summands are `F_{ag}`, not `E_{ag}`; the BC analogy is an observation and its faithful form computes the **cover's** zeta (all characters) |
| X2a | **MINOR** | true as a two-term asymptotic, but the `O(1)` term is exactly `1 - gamma = 0.42278434` and must be written |
| X2b | VALID | `C = 0` **exactly**, by the cancellation `(-gamma) + (+gamma)` of the two Mertens constants |
| X2c | VALID | `C' = -gamma/2 = -0.288608`; the observed `-0.25` is the `0.671/log N` correction, not the limit |
| X2d | VALID | `floor(e^E)`, Hagedorn `beta_H = 1`, not Cardy; the `log log N` term in X2(c) is the independent signature |
| X3 | **MINOR** | faithful in shape, but the T5 odd list is **doubled** (plus an even pair-sum sector), the T6 entanglement spectrum is `beta log n + log zeta(beta)` not the ring lengths, and T6's reality is unconditional only for the classical part and only for `beta > 1` |

**INVALID: none. MINOR: 5 (T2.3, H-BC-POS, X1, X2a, X3).**

---

# Scratch scripts written for this review

All under `notes/reviews/`, all self-contained (`numpy`, `sympy`, `scipy`, `mpmath`), all re-runnable with `python3 <file>`. **None of them imports or copies anything from `scripts/`.**

1. **`scratch_rcmps_t1t2t4.py`** — T1.1, T1.2, T1.3, T1.4, T2.1, T2.2, T2.3, T4.1, T4.2.
   *Checks:* `psi_0` explicit formula against a direct prime-power count (260 `mpmath` zeros); the T1.2 cutoff pairing `<mu, chi(t/eps) eta(t/R) t^k e^{-st}>` against `k! sum nu (s-lambda)^{-(k+1)}`, and the invisibility of cancelling pairs; convergence exponents for (G2) on the zeta multiset; **(4.2) `Tr_dist Z(t) = 1 - 2P_+ - e^{-t/2}/(e^t-1)` by Gaussian smearing at 15 values of `t`, with three wrong variants as controls**; `str e^{tG} = 2P_+` and both ladder variants; `e^{-t/2}/(e^t-1) = sum_k e^{-(k+1/2)t}`; the T2.2 oscillation lemma on 400 random trigonometric polynomials and on mixed-real-part flip sets; the flipped-pole limit; and the T2.3 strengthening (`R_k(s) -> -inf` as `s -> 1+` when `b = 1`).
   *Output:* pairing rel. error `1.4e-14`; cancelling pair `0.00e+00`; **(4.2) max `|diff| = 9.4e-06`, rel `1.3e-05`**; wrong variants off by `3.256 / 0.814 / 0.774`; oscillation `400/400`; `e^{-u}f(200) = -2.00000000`; `R_4(1.001) = -2.4e+16` for `b=1`, `+2.4e+16` for `b=0`.

2. **`scratch_rcmps_t3t5.py`** — T3.1, T3.2, T3.3, T5.1, T5.2, T5.5.
   *Checks:* the residue `-1/alpha` in SymPy and the sign flip in the prescribed function; the trace-class meromorphy threshold; `Z(u) = det(1-uE_-)/det(1-uE_+)` against a 40-term Newton series; curve counts and a from-scratch Prony fit (Hankel solve + `np.roots` + Vandermonde least squares); the MPS ring-norm identity at `n = 1,2,3`; and the full `D = 3, 5` vacuum-decay model (GKLS form, trace preservation, formula (5.2) at three times, Choi positivity, contraction, spectrum (5.1) by greedy matching, grading commutation, odd-spectrum extraction, both trace formulas, the renewal integral, and the one-jump ring amplitude).
   *Output:* residue `-1/alpha` exact; `1.205017394855` both ways; Prony roots `{3, 1, +-sqrt3, +-i sqrt3}` with coefficients `+1,+1,-2,-2,-1,-1`; ring norms agree to `1e-13`; (5.2) to `3.1e-15`; spectrum (5.1) to `1.3e-14` on all `(d+1)^2` eigenvalues; `[Gamma(x)Gamma, L] < 1e-11`; `Tr e^{tL} = |1+Tr Z_t|^2` in 8/8; renewal integral trace `5.00000000`; one-jump amplitude `0.00e+00`.

3. **`scratch_rcmps_t6.py`** — T6.1, T6.2, T6.3, T6.4, T6.5.
   *Checks:* the KMS identity `p_n = (n/m)^{-beta} p_m` over all `1 <= n,m <= 12` and `alpha_{i beta}(e_{nm})` by explicit matrices; the Euler product; the entanglement spectrum and its relation to the ring lengths; the M/M/1 spectrum on `3001`-dimensional truncations at four rate pairs, plus the boundary/interior equations and a direct `2001`-dimensional resolvent solve for `m(0)`; the single-prime bands `I_p` for `p = 2,3,5,7`; the convergence of the infinite sum of left endpoints (the closure); the off-diagonal sectors and the exact rank-one comparison; and the delocalisation bounds.
   *Output:* KMS forcing PASS; band containment `3000/3000` in 4/4; `m(0) = 1.0000000000 = z/a` with `1 - mu m(0) = 1.1e-16`; `I_p` matched to `1e-6`; `sum_p` left endpoints `= -1.002516`; sector tops `-2.4e-17 (delta=0)` and `-0.1668 (delta != 0)`; `sum_{p<2e5} 1/p = 2.76361`.

4. **`scratch_rcmps_t7.py`** — T7.2, T7.3, T7.4, T7.6, T7.7, T7.8, T7.9, T7.10 (235 checks, **0 failures**).
   *Checks:* from-scratch `F_{q^n}` (irreducible polynomial by sympy, normal-basis generator by rank test), brute-force `S_n(g)`, the transfer matrix from (7.1), the ring quadratic form, `d_n = dim ker P(S) = log_q(|S_n|^2/q^n)`, `delta_n = det(S|ker P(S))` by Gaussian elimination over `F_q`, the sign law (7.4), the boxed periodic law (7.6), **both endpoint criteria (7.7) and (7.8) against the observed laws**, `v_+-` from `z^J P(z)`, the `A`-matrix identities and `eta(det C) = det S = (-1)^{n-1}`, `E E^dag = qI`, the `L`-polynomial by Newton's identities, (7.9), the multiplicity formula (7.10) and `det(I - T F_g) = L(g,T)`, the direct projective point count vs the character sum vs `str` of the corrected and the draft super-transfer, the explicit `M_g` from (7.13), symplecticity mod `q`, exact **centred** Weyl covariance, and `|Tr E^n|^2 = q^{n + dim ker(M^n - I)}`.
   *Output:* 12/12 tuples pass (7.4) and (7.6); **(7.7) and (7.8) agree with the observed laws 12/12, including `q=3 a=(2,1)` and `q=5 a=(0,1,1)`**; `A`-identities exact for 10 `(q,n)` pairs incl. `q|n`; `E E^dag = qI` in 12/12; (7.10) gives exactly `q^J` roots on `|z| = sqrt q` with `det(I-TF) - L` at most `7.9e-14`; 22/22 point counts, with `str(DRAFT block) = -2.0000` vs `N = 10` and `298` vs `190`; `M_g` symplectic in 12/12 and **identical to the numerics lane's**; centred covariance residual `<= 7.6e-16`; character modulus exact in 72/72.

5. **`scratch_rcmps_t7b.py`** — the T7.3 `<1>2` determinant square class, and the T7.5 table.
   *Checks:* `D = det(A|R_n)` computed in `F_{q^n}` in an `F_q`-basis of the radical (with the invariance `A R_n subset R_n` asserted, not assumed), then `D^2 = det(C|R_n)` and `D^q = det(S|R_n) D` for 11 `(q,a,n)` triples covering `dim R_n = 0,1,2,3` and four cases with `q | n`; and an independent recomputation of every row of T7.5's table.
   *Output:* all 11 determinant checks PASS (e.g. `q=3, a=(0,1,1), n=6`, `dim R_n = 3`, `delta_n = -1`); all six table rows reproduce astra's values exactly (`3 sqrt3 = 5.1962`, `81 sqrt3 = 140.2961`, `5 sqrt5 = 11.1803`) and obey (7.4).

6. **`scratch_rcmps_x2x3.py`** — X2(a)–(d) and the multiplicity half of X3.
   *Checks:* the closed-form entropy against the direct sum with a tail estimate; the limit of `S - [1/eps + log(1/eps)]` at `eps = 10^{-3} ... 10^{-9}`; the exact identity `S_geom(1/p) = -log(1-1/p) + log p/(p-1)`; both Mertens sums with a from-scratch sieve to `2 x 10^7`; the bond-cutoff entropy by direct summation to `10^7` and by the `H_N`/Stieltjes asymptotics to `10^{40}`, with the two-term residual; the level counting against Cardy; and the doubling of the T5 odd list.
   *Output:* `S - [1/eps+log(1/eps)] -> 0.42278434 = 1 - gamma`; `sum log p/(p-1) - log P -> -0.577216`, `sum -log(1-1/p) - log log P -> +0.577230`, so **`C = 0`**; `C' = -gamma/2` with the two-term prediction fitting to `4.1e-04`; `floor(e^{20}) = 4.85e8` vs Cardy `9.6e4`; T5 odd multiplicities `[2,2,2,2]`.

---

# What the write-up should carry forward

1. **T2.3, mandatory split.** "(i) positivity alone forces `b = 0`" (proof in the T2.3 section above, no Landau, no domination) and "(ii) `mu >= comb` additionally forces `F_Z = empty`". Without (i) the lab book leaves the impression that the *pole's* parity is only conditionally even, when it is unconditionally so.
2. **H-BC-POS, citation split.** Uniqueness for `0 < beta <= 1` is byte-verified (`math/0404128:...:1815-1849`); the type III`_1` factor property is **not** byte-verified in this repository (the only local evidence labels the critical temperature only) and should be attributed to Bost–Connes 1995 as an unverified citation, exactly as `notes/extract/riemann-cmps-sources.md` section I already recommends.
3. **X1, two wording fixes.** The even block is the trivial-character sector **plus** the point at infinity, and the two poles are split between them (`T = 1/q` from `E_0`, `T = 1` from infinity); the odd summands are the corrected `F_{ag}`, not `E_{ag}`. And the faithful form of the Bost–Connes analogy is that a Galois-graded bond computes the **cover's** zeta — all characters together — not `zeta` alone.
4. **X2 constants.** `S = 1/(beta-1) + log(1/(beta-1)) + (1 - gamma) + o(1)`; prime cutoff `C = 0` exactly, by the cancellation of the two Mertens `gamma`'s; bond cutoff `C' = -gamma/2`, with the finite-`N` value `-0.25` explained as the `0.671/log N` correction.
5. **X3, three qualifications** (doubled odd list plus an even pair-sum sector; entanglement spectrum `beta log n + log zeta(beta)`; T6's reality unconditional only for the classical part and only above the transition).
6. **T7.4 typo.** `mathbf1_{2\mid n}` -> `\mathbf 1_{2\mid n}` in `<1>3`.
7. **Worth keeping verbatim.** The centred-vs-uncentred Weyl point (T7.9): the symplectic matrix `M_g` is convention-independent and matches the numerics lane exactly, but only the *centred* convention makes the covariance phase-free, which is what licenses "`U_g = e^{i theta} W(M_g)` for a phase independent of `n`" and hence the character-modulus identity of T7.10. This is the cleanest reconciliation available between the prover's and the numerics lane's conventions.

---

# Round 2 (2026-09-12, same reviewer)

The coordinator (claude:fable-5.1) reports that the Round-1 MINOR findings have been applied to the lab book and asks for a re-verdict on two of them. I checked the two statements **as they now stand in the repository**, not as paraphrased, and I also checked their `db/claims.tsv` rows and their declared dependencies, because in this book the printed status is *derived* from the deps and a wrong dep list silently promotes a claim. The Round-1 sections above are left unchanged as the record; the verdicts below supersede them for T2.3 and X3.

## T2.3 re-verdict — `prop:parity-infinite-dominated`, `report/sections/04b_phantasm_forced.tex`

The statement now reads (verbatim from the shard, l.157–164):

> With `F_Z` possibly infinite: (i) positivity of the supertrace alone forces `b=0`, the pole even, by monotone convergence of the cutoff pairings, with no domination premise and no Landau input; (ii) if moreover the supertrace dominates the comb as measures then `F_Z=∅`. In both parts `F_T` remains arbitrary.

followed by "Part (i) is the reviewer's strengthening of the prover's statement; part (ii) cannot be freed of its premise by the same route, because for infinite `F_Z` the flipped subseries is only a distribution and can carry negative mass at the prime-power atoms."

**This is exactly the split I asked for, and each clause is one I verified.**

- *The symbols are defined where they must be.* `b`, `F_Z`, `F_T` and the reference parity (pole even, everything else odd) are fixed in `thm:parity-forced-finite` immediately above, and `prop:parity-infinite-dominated` inherits them by position. They agree with the meanings I used.
- *Part (i) is the theorem I proved in Round 1*, and the named mechanism ("monotone convergence of the cutoff pairings") is the correct one: `h_{ε,R,s} ≥ 0` increases pointwise to `t^k e^{-st}`, `μ` is a positive Radon measure by `asm:positive-distributions`, so `∫ t^k e^{-st} dμ = R_k(s) ≥ 0` for real `s > 1`, while `b = 1` makes `R_k(s) ~ -k!(s-1)^{-(k+1)} → -∞`.
- *The dependency list is complete for part (i)* and correctly retains `asm:landau-laplace` for part (ii): `asm:explicit-formula-trace`, `asm:zero-count-location` (which is what puts the flipped-zero poles off the real axis, so nothing but `s = 1` is singular there), `asm:positive-distributions`, `thm:supertrace-rigidity`, and `asm:landau-laplace`. Part (i) uses the first four and not the fifth, as the statement says.
- *The claim that `F_T` stays arbitrary in part (i) is correct and I re-checked it:* the trivial-ladder terms `k!/(s+2j)^{k+1}` are `O(j^{-(k+1)})`, hence locally uniformly summable, with poles only at `s = -2j < 0`, so they neither obstruct the finiteness of `R_k(s)` for `s > 1` nor contribute anything near `s = 1`, however large `F_T` is.
- *Round-2 numerics, for the case T2.2's pointwise argument cannot reach.* I re-ran the weighted transform with 400 zero pairs and 4000 ladder terms for three **maximal** flip sets — `F_Z` = every zero with `F_T` = every trivial zero; `F_Z` = every other zero with `F_T` = every trivial zero; `F_Z` = every zero with `F_T = ∅`. In all three, `R_4(s)` at `s = 1.5, 1.1, 1.01, 1.001` is `≈ -768, -2.4e+06, -2.4e+11, -2.4e+16` for `b = 1` and the positive mirror for `b = 0`. The blow-up is insensitive to the size of either flip set, exactly as part (i) claims. (Run in the session scratchpad; it needs no new script, being the `b`-sweep of `scratch_rcmps_t1t2t4.py` part F with larger sets.)

**One sentence should be added elsewhere, and it is not optional for a reader reconstructing part (i).** The paragraph under `thm:supertrace-rigidity` says only that the proof "pairs the supertrace with cut-off versions of `t^k e^{-st}`". Part (i) needs those cut-offs to be **nonnegative and monotone** in the two parameters — otherwise there is nothing for monotone convergence to act on. The prover's own construction does record it ("They may be chosen between zero and one and monotone in their transition regions", `notes/riemann-cmps/astra-proofs.md` T1.2 ⟨1⟩1); the lab book drops it. Suggested insertion in that paragraph: "…with the cut-offs chosen nonnegative and monotone in both parameters, so that they increase pointwise to `t^k e^{-st}`." This is a completeness repair in a *different* statement, not a defect in `prop:parity-infinite-dominated`, so it does not affect the verdict.

**VERDICT T2.3: VALID**

## X3 re-verdict — `obs:complementary-halves`, `report/sections/04c_phantasm_channels.tex`

The statement now reads (verbatim from the shard, l.209–221):

> The vacuum-decay channel has the zeros as odd relaxation modes (each zero twice, as a coherence and its conjugate, plus an even pair-sum sector) but a pure stationary state, hence trivial entanglement. The prime-chain Gibbs Lindbladian, for `β>1`, has `ρ_β` as stationary state, with entanglement spectrum `β log n + log ζ(β)`, proportional to the ring lengths `2 log n`, but a real spectrum with no zeros: unconditionally for its classical part, and on the weighted space of `prop:prime-chain-offdiagonal` for the full generator when `Σ r_p p^β < ∞`. No construction in this book has both, and the Phantasm would need both.

**All three Round-1 repairs are in, correctly:** the doubling and the even pair-sum sector; the entanglement spectrum written as `β log n + log ζ(β)` and only *proportional* to the ring lengths; and the reality of the prime-chain spectrum split into the unconditional classical part and the weighted-space statement under the stronger rate condition, with `β > 1` stated so the Bost–Connes point is not silently claimed. The closing clause is the scope audit of T8.1 and is accurate. As a **statement** this is now faithful to T5 and T6 as proved.

**But the row is recorded as `proved`, and its declared dependencies do not carry its first clause.** `db/claims.tsv` gives

`deps = thm:vacuum-decay-finite; prop:vacuum-renewal-trivial-entanglement; prop:prime-chain-lindbladian; prop:normal-kms-gibbs`, `status = proved`.

Three things are missing, and the book's own machinery shows why they matter:

1. **The first clause is about `K_S`, not about the finite model.** The word "zeros" only has content for `H = K_S`; `thm:vacuum-decay-finite` is the finite-dimensional model with an abstract `B` and says nothing about zeros. The statement that carries the clause is `obs:zero-coherences-populations` — "For `H=K_S` each zero appears once as an odd coherence mode `-conj(ρ)/2` and once as its conjugate (odd multiplicity `2 m_ρ`), the even populations carry the pair sums…" — whose status is **`sketched`**. It is not in the deps.
2. **`asm:lax-phillips-modes` is nowhere in the chain.** The book *does* have it (it is the dep of `prop:ringnorm-trace`, `prop:riemann-graded-generator`, `prop:ladder-parity-free`), but the channel side does not declare it: `prop:absorbing-vacuum-channel` is `proved` with `deps = -`, and its last sentence is "For `H = K_S` it realises the Riemann channel as its odd coherence sector" — which is true only given that `Z(t)` on `K_S` *is* a strongly continuous, strongly stable contraction semigroup with those modes, i.e. given `asm:lax-phillips-modes`. The prover's own status line says so ("`proved-here` for the stated semigroup premises; Riemann specialization `conditional-on H-LP`"). As the deps stand, the Lax–Phillips input has disappeared from this branch of the book.
3. **`prop:prime-chain-offdiagonal` is cited in the text but absent from the deps.**

Because `scripts/labbook_check.py` *derives* the printed status from the deps ("assumed dep → `-conditional`; sketched dep caps at sketched"), the repair is mechanical and self-correcting:

- add `asm:lax-phillips-modes` to `prop:absorbing-vacuum-channel` (it will print as `proved-conditional`, which is what it is);
- add `obs:zero-coherences-populations` and `prop:prime-chain-offdiagonal` to `obs:complementary-halves`.

The gate will then demote `obs:complementary-halves` to the honest status by itself, with no editorial judgement required. Nothing in the text has to change.

**Scope of this verdict.** It is on the statement text, which is correct, and it is **conditional on that dependency repair**. The statement says "unconditionally for its classical part" about T6 but says nothing qualifying the vacuum-decay clause, and a bare `proved` label on a clause whose only support in the book is a `sketched` observation is precisely the rounding-up this lane exists to catch. **If the deps row is left as it is and the claim keeps `proved`, my verdict on that row reverts to MINOR**, for the reason displayed above.

**VERDICT X3: VALID**

## Two bookkeeping notes, neither affecting a verdict

- **`num:bc-entropy` text drift.** The shard (l.181–191) now carries the three constants correctly — "Constants fixed by the review: `S = 1/(β-1) + log(1/(β-1)) + (1-γ_E) + o(1)`; the prime-cutoff constant is exactly `0`, the two Mertens constants cancelling; the bond-cutoff constant is `-γ_E/2`" — but the `statement` column of the corresponding `db/claims.tsv` row still ends at "the count of entanglement levels below `E` is `floor(e^E)`" with no constants. The gate compares statuses and labels, not statement text, so it will not catch the drift. Worth syncing, since the db row is what gets quoted downstream. The shard wording itself I checked and it is right, including the fact that `-γ_E/2 = -0.2886` is the limit while the file's own `0.657 at N = 10^7` and "falls towards 1/2" are finite-`N` values.
- **X1 and H-BC-POS, applied without a verdict, checked anyway.** `obs:character-sector-grading` (status `sketched`) now splits the point at infinity from the trivial-character sector, names the two poles separately (`T = 1/q` from the de Bruijn count, `T = 1` from the point at infinity, "not a character sector"), uses the corrected blocks `F_{ag}`, says "as its net spectrum", and carries the cover-zeta reading ("the graded object would compute the zeta of the cover, the Dedekind zeta of the cyclotomic field at level `N`, not `ζ` alone") together with the caveat that the prime-chain MPO is nevertheless not that object. All four Round-1 fixes are in, correctly. `cit:bc-kms-unique` now claims only uniqueness for `0 < β ≤ 1` and the `β > 1` Gibbs classification, with the note column recording "the type III`_1` assertion is in the Bost–Connes original (Selecta 1995), no local source" — which is exactly the split I asked for and matches the caveat already in `notes/extract/riemann-cmps-sources.md` §I.

## Round-2 verdict table

| Label (lab-book id) | Round 1 | Round 2 | Note |
|---|---|---|---|
| T2.3 (`prop:parity-infinite-dominated`) | MINOR | **VALID** | the (i)/(ii) split is in, the dep list is right, `F_T` arbitrary confirmed; add "nonnegative and monotone" to the `thm:supertrace-rigidity` paragraph |
| X3 (`obs:complementary-halves`) | MINOR | **VALID** | all three repairs in; **requires** adding `obs:zero-coherences-populations` + `prop:prime-chain-offdiagonal` to its deps and `asm:lax-phillips-modes` to `prop:absorbing-vacuum-channel`, else the verdict on the row reverts to MINOR |
| X1 (`obs:character-sector-grading`) | MINOR | **VALID** | all four repairs in; status `sketched` is right for an analogy |
| X2a (`num:bc-entropy`) | MINOR | **VALID** | `(1-γ_E)` recorded in the shard; sync the `db/claims.tsv` statement column |
| H-BC-POS (`cit:bc-kms-unique`) | MINOR | **VALID** | cited fact now claims only uniqueness for `0 < β ≤ 1`; type III`_1` attributed without a local quote |

No other verdict in this review changes. **Round 2 — INVALID: none. MINOR: none**, conditional on the one dependency repair recorded under X3.
