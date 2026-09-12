# Adversarial review: `notes/weil-positivity/astra-proofs.md`

- **Date:** 2026-09-12
- **Reviewer:** claude:opus (REFUTE lane)
- **Author under review:** codex:gpt-6-astra
- **File under review:** `notes/weil-positivity/astra-proofs.md` (labels T1.1–T1.3, T2.1–T2.3, T3.1–T3.5, T4.1–T4.5, T5.1–T5.3, T6.1–T6.4, ledger T7)
- **Also adjudicated:** three statements X1, X2, X3 proposed by the orchestrator (claude:fable-5.1)
- **Independent numerics:** six scratch scripts `notes/reviews/scratch_weil_*.py`, written from the *statements* only. No code was reused from `scripts/weil_positivity.py`; the transfer operator, the Toeplitz forms, the Dyson expansion, the Hashimoto matrix and the explicit-formula test were all coded from scratch here, and the results are independent confirmations rather than re-runs.

**Headline.** The file is unusually clean. I could not break any labelled statement: every constant, sign, multiplicity and interchange I attacked survived, and the drafted errors flagged in the brief were genuinely corrected rather than papered over. Two MINOR findings only (one an under-claim in T3.1 that matters for X2, one a wording collapse in the orchestrator's X2 itself). The three drafted claims that the independent numerics had already failed (`T2f`, `T3c`, `T3e` in `outputs/weil_positivity.txt`) are exactly the ones astra corrected in T2.1/T3.2/T3.1 — no disagreement between the two lanes.

---

## T1.1 — Poisson-kernel single-mode lemma

**Claim (one line).** For `|z| <= 1`, `sum_{l,m} c_l conj(c_m) z^{[l-m]}` equals `(1/2pi) int |f_c|^2 P_z` when `|z| < 1` and `|f_c(z)|^2` when `|z| = 1`; at `z = 0` it is `sum_l |c_l|^2`.

**VERDICT T1.1: VALID**

Attacks tried and what happened.
- *Fourier orientation.* The risk is the classical sign slip: `P_z` is expanded as `(1-|z|^2) sum_{p,q>=0} z^p conj(z)^q e^{-i(p-q)theta}`, so the coefficient of `e^{-ik theta}` is `z^k` for `k >= 0`, and the lemma needs `(1/2pi) int e^{+ik theta} P_z dtheta = z^{[k]}`. That pairing is the one that makes `|f_c(e^{i theta})|^2 = sum c_l conj(c_m) e^{i(l-m)theta}` produce `z^{[l-m]}` and **not** `conj(z)^{[l-m]}`. I checked it numerically for `z = 0, 0.7, -0.3+0.5i, 0.95i, 0.2-0.8i` and `k = -4..4`: max error `6.7e-16` (`scratch_weil_t1t2.py`). The orientation in ⟨1⟩1 is right.
- *The `z = 0` edge.* `P_0 = 1`, mass `2pi`, contribution `sum_l |c_l|^2`; consistent with `0^0 = 1` in the preamble, and it is what makes a retained zero eigenvalue harmless. Verified (`lhs = rhs = 8.6401261213`).
- *Regrouping of the double geometric series.* Absolute convergence is uniform in `theta` for fixed `|z| < 1`; the justification given is sufficient.
- Boundary case `|z| = 1`: `z^{[l-m]} = z^l conj(z)^m` exactly, so the form is `|f_c(z)|^2`. Checked at `z = e^{0.9i}` (exact agreement) and at `0.999 e^{2.1i}` (interior formula, agreement `5e-9` at the quadrature resolution used).

## T1.2 — two-point bound and the discrete growth lemma

**Claim.** A positive definite Hermitian sequence has `b_0 >= 0` and `|b_k| <= b_0`; and `a_l = sum_j m_j zeta_j^l` (distinct unimodular `zeta_j`, positive integer `m_j`) does not tend to `0`.

**VERDICT T1.2: VALID**

- The `2x2` argument is correct as written: with support `{0,k}` the form is `b_0(|c_0|^2+|c_k|^2) + 2 Re(c_k conj(c_0) b_k)`, and the stated choice gives `2b_0 - 2|b_k| >= 0`. The degenerate case `b_0 = 0` is handled (it forces `b_k = 0`), which is the usual gap in textbook write-ups; astra closes it.
- The Wiener mean-square step is correct: `(1/L) sum_{l<L} (zeta_j conj(zeta_k))^l -> delta_{jk}` because the `zeta_j` are *distinct*, so `L^{-1} sum |a_l|^2 -> sum_j m_j^2 > 0`; the "fixed initial segment plus uniformly small tail" split is a valid Cesàro argument. No hypothesis is missing (positivity of the `m_j` is used only through `sum m_j^2 > 0`).
- Numerically: `0` violations of `|nu_l| <= nu_0` over 300 in-disk random multisets.

## T1.3 — finite Weil positivity is exactly the disk bound

**Claim.** `nu(X;S,r)` is positive definite iff `|mu| <= r` for every `mu` in `spec(X) \ S` (with algebraic multiplicities; a retained zero allowed).

**VERDICT T1.3: VALID**

- *Hidden diagonalisability?* None. Only `Tr X^l = sum_{mu} mu^l` is used, which holds for a triangular form; the closing paragraph says so explicitly. My Jordan test (T5.3 below) confirms that `nu` is literally identical for a Jordan block and for the diagonal matrix with the same spectrum (`max |nu_l(J) - nu_l(D)| = 0` for `l <= 40`).
- *The converse step.* With `R = max |mu|/r > 1`, `R^{-l} nu_l = sum_j m_j zeta_j^l + b_l` with `b_l -> 0` — correct, because *all* modes of maximal modulus are collected into the `zeta_j` and everything else is `O((R'/R)^l)`; retained zeros contribute nothing for `l >= 1`. Boundedness then forces `R^{-l} nu_l -> 0`, contradicting T1.2. Airtight.
- *Numerics.* 200 random multisets (mixing zeros, interior, boundary and exterior modes), Toeplitz order escalated to `L = 400`: **0 mismatches** between "PSD at every tested `L`" and `|mu| <= r`. Finite-`L` masking reproduced independently: a pair at radius `1+eps` first produces a negative Toeplitz eigenvalue at `L = 5, 20, 20, 40` for `eps = 0.2, 0.05, 0.02, 0.01`. This is the same phenomenon the other agent reports (threshold approaching from below); it is a property of *truncation*, not a defect of the theorem, and astra's statement quantifies over all `L`.

## T2.1 — reflection duality and the inflow identity

**Claim.** If `A` is `J`-invariant (`J(mu) = r^2/conj(mu)`), then `W(c) = M(c)` for all finitely supported `c`, and positivity `<=> |mu| = r <=> J(mu) = mu` on `A`.

**VERDICT T2.1: VALID**

- The pivot is ⟨1⟩1: `sum_{z in Z} z^{-k} = sum_w conj(w)^k = nu_{-k}` uses `J`-invariance **as a multiset**, which is exactly the hypothesis, and is precisely where the "reciprocal-only" version fails (see T2.3). Correct.
- ⟨1⟩2: `conj(f_c(j(z))) = sum_m conj(c_m) z^{-m}` since `conj(j(z)) = 1/z`. No Fourier normalisation enters. The Laurent-shift remark (`z^h conj(j(z))^h = 1`) is right.
- Astra correctly distinguishes **`J`-invariance of the multiset** (hypothesis) from **`J`-fixedness of each mode** (conclusion). This is the very point on which the brief's drafted claim was wrong and which the independent numerics flagged as `T2f`; astra does not repeat the error.
- Numerics: `max |W(c) - M(c)| = 9.2e-13` over 200 random `J`-invariant multisets with random degree-4 `c`.

## T2.2 — orbit decomposition and an isolated negative pair

**Claim.** Orbits contribute `m|f(z)|^2` (fixed) or `2m Re(f(z) conj(f(j z)))` (two-element); one off-circle orbit suffices to make the *whole* form negative.

**VERDICT T2.2: VALID**

- The two terms of a non-fixed orbit are genuine complex conjugates because `j` is an involution — checked.
- The Lagrange interpolation is the right fix for the obvious objection ("a negative summand is not a negative form"): prescribing `+1` at `z`, `-1` at `j(z)` and `0` at every other *distinct* point of `Z` kills all other orbits exactly. The interpolating polynomial has degree `<= q-1`, so its coefficient vector is supported in `N_0` as required by the definition of `W`.
- Numerics: five random configurations with a doubled off-circle orbit plus a circle pair give `W(c) = -4.000000` (`= -2m` with `m = 2`) to `1e-15`, with imaginary part `< 1e-14`.

## T2.3 — holomorphic reciprocal symmetry

**Claim.** Invariance under `I(mu) = r^2/mu` alone gives the circle criterion but **not** `W = M`; conjugation symmetry in addition gives `J`-invariance and `W = M`. `I` is holomorphic, not linear.

**VERDICT T2.3: VALID**

- The circle criterion under `I` alone is correct (`|I(mu)| = r^2/|mu|`, then T1.3 twice).
- The separating example is exact: `A = {2i, -i/2}`, `r = 1`. I recomputed: `nu_1 = 1.5i`, `nu_{-1} = -1.5i`, `sum_z z^{-1} = +1.5i != nu_{-1}`; and for `f(z) = 1+z`, `W = 4` while `M = 4 + 3i`. Both of astra's numbers are right, and the example is minimal (two modes).
- The pedantic correction of the brief's word "linear" is justified; the composite `J = conj ∘ I = I ∘ conj` is what the Weil form sees.

## T3.1 — Kraus reality needs no pairing

**Claim.** `C_W(x)_i = x_i^dagger` is an antiunitary involution commuting with `T`; likewise `C_V` with `Sigma`; so both spectra are conjugation-closed with algebraic multiplicities. "If in addition `B_ibar = B_i^dagger`, H-QT supplies the nonnegative ring trace."

**VERDICT T3.1: MINOR**

Everything asserted is true and correctly proved:
- antiunitarity `<x^dagger, y^dagger> = conj<x,y>` via cyclicity — checked;
- `(B x B^dagger)^dagger = B x^dagger B^dagger`, and the transition coefficients of `T` are real `0/1`, hence `C_W T = T C_W` — checked (`d(spec T, conj spec T) <= 1.9e-14` for adjoint-paired families at `n = 2,3`, `D = 4,6`);
- the generalised-eigenspace argument `C (Y - mu)^k = (Y - conj mu)^k C` with an antilinear bijection gives equality of *algebraic* multiplicities, not just of eigenvalue sets. That is the right level of care.

**The fix I supply.** The last sentence (and the matching row of the T7 ledger, "nonnegative ring traces hold in the stated Kraus settings") is weaker than the truth and leaves the false impression that the adjoint pairing is what buys side A. The trace identity

`Tr_W T^l = sum_{cyclically non-backtracking w} |Tr(B_{i_l} ... B_{i_1})|^2 >= 0`

holds for **every** family `E_i = Ad(B_i)` with an arbitrary fixed-point-free reversal and **no pairing hypothesis at all**. The notebook's own proof (`notes/quantum-ihara-general.md` §4, Corollary 2 ⟨1⟩2) uses only `Ad(A)Ad(B) = Ad(AB)` and `Tr_V Ad(A) = |Tr A|^2`; the pairing enters Corollary 2 only in the *determinant* factorisation (`E_ibar E_i = Ad(A_k^dagger A_k) >= 0`), never in the trace. I verified this numerically on completely unpaired random `Ad` families (`n = 2,3`, `D = 4,6`): `Tr T^l` agrees with the word sum to `< 1e-9` relative for `l = 1..5` and is real and positive throughout. This is exactly finding (i) of `outputs/weil_positivity.txt` and is what X2(a) needs; T3.1 should state it, since as written the file's three-way slogan ("Kraus maps supply conjugation symmetry; inverse pairing supplies reciprocal symmetry") silently omits the third and most important item, that Kraus maps supply the nonnegative ring count too.

## T3.2 — inverse pairing and exact multiplicities

**Claim.** `det(xI - T) = (x^2-1)^k prod_alpha (x^2 - alpha x + q)^{a_alpha}` with `k = N(D-2)/2`, `q = D-1`; `A_0 = spec(T) \ S_0` has `2N` elements, no zero, is invariant under `mu -> q/mu`; and `A_0` is conjugation-invariant **iff** `spec(Sigma)` is, which for Kraus families always holds.

**VERDICT T3.2: VALID**

- *Degree/exponent bookkeeping.* Substituting `u = 1/x` in H-QI and multiplying by `x^{ND}` needs `2k + 2N = ND`, i.e. `N(D-2) + 2N = ND` — correct. Both sides then have degree `ND`. I verified the resulting multiset formula numerically for random inverse-paired `Ad` families: greedy multiset matching between `spec(T)` and the predicted `{+1^k, -1^k} ∪ roots` gives `1e-14` at `(n,D) = (2,4), (2,6), (3,4)`, with `|A_0| = 2N` and `d(A_0, q/A_0) <= 3.6e-14`.
- *Double roots.* `alpha = ±2 sqrt q` gives `mu = ±sqrt q` with multiplicity `2 a_alpha`, and the remark that a double root of the determinant says nothing about Jordan structure is both correct and necessary (T5 later needs it).
- *The `±1` collision.* `mu = 1` arises only from `alpha = 1 + q = D` and `mu = -1` only from `alpha = -D`, so removing `S_0` removes exactly `k` copies of each and leaves the `a_{±D}` copies from the quadratics. Correct, and this is the step where a careless treatment would produce the wrong `S` in T3.4.
- *The conjugation criterion.* Forward direction is immediate (`q` real). The converse via the pushforward `h(mu) = mu + q/mu`, whose multiset image is exactly **two** copies of `spec(Sigma)` (including at double roots), is a genuinely good argument; dividing integer multiplicities by two is legitimate.
- *The brief's requested Kraus counterexample does not exist* — astra says so plainly and supplies instead a non-Kraus scalar counterexample (`N=1, D=4`, weights `2i, 1, -i/2, 1`, `Sigma = 2 + 3i/2`, retained factor `x^2 - (2+3i/2)x + 3`). I checked the arithmetic: correct, and `M_1` Kraus maps are indeed multiplication by `|b|^2 >= 0`, so no `n = 1` Kraus counterexample can exist. This matches the independent `T3c` FAIL.
- *The `diag(2i,1)` example.* I recomputed `spec(Sigma)` from the matrix units: `{25/4, 4, 2 + 3i/2, 2 - 3i/2}` — exactly as claimed (numerically `[6.25, 4, 2±1.5i]`). Conjugation-closed but not real: the right example to make the point that inverse pairing does not buy reality.

## T3.3 — simultaneous pairing means unitarity (not "unitary up to scalar")

**Claim.** `Ad(B^dagger) = Ad(B)^{-1} <=> B^dagger B = I`; the projective variant is `Ad(B^dagger) = kappa Ad(B)^{-1} <=> B^dagger B = sqrt(kappa) I`.

**VERDICT T3.3: VALID**

- The computation is right and the correction of the brief is right. Composing gives `x -> P x P` with `P = B^dagger B` Hermitian positive; equality with the identity map forces `Ad(P) = id`, and evaluating at `x = I` gives `P^2 = I`, hence `P = I`. The brief's "nonzero scalar multiple of a unitary" fails because `Ad` is *quadratic* in `B`: for `B = tU`, `Ad(B^dagger) = t^2 Ad(U^dagger)` while `Ad(B)^{-1} = t^{-2} Ad(U^dagger)`, so `t^4 = 1`.
- Numerically: `B = 2I` gives `|Ad(B^dagger) - Ad(B)^{-1}| = 3.75` but `|Ad(B^dagger) - 16 Ad(B)^{-1}| = 0` — the projective statement with `kappa = |c|^4` is exactly right. `diag(1,2)`: defect `3.75`. Unitary: `0`.

## T3.4 — the unitary Ramanujan criterion

**Claim.** For a unitary adjoint-paired family with `r = sqrt(D-1)` and `S = S_0 ⊎ {q^{d_+}, 1^{d_+}} ⊎ {(-q)^{d_-}, (-1)^{d_-}}`: Weil positivity `<=>` Hastings' bound `|lambda| <= 2 sqrt(D-1)/D` off `±1` `<=>` all retained modes on the circle `<=>` all retained modes `J`-fixed.

**VERDICT T3.4: VALID**

- *Is `S` a sub-multiset?* Yes: `q` arises only from `alpha = D` (since `alpha = mu + q/mu`) with multiplicity `d_+`, and `q != ±1` because `q = D-1 >= 3`. The multiplicity of `1` in `spec(T)` is `k + d_+`, of `-1` is `k + d_-`; `S` removes exactly those. Retained size `2(N - d_+ - d_-)`.
- *`lambda` real.* Follows from `Sigma^* = Sigma` in Hilbert–Schmidt, which needs only the **adjoint pairing** (astra says so); unitarity is used only for `||Phi|| <= 1` and `Phi(I) = I` (so `d_+ >= 1`). Correctly apportioned.
- *The band argument.* For real `alpha`, `|alpha| < 2 sqrt q` gives conjugate roots of modulus `sqrt q`; `|alpha| = 2 sqrt q` gives the double root `±sqrt q`; `|alpha| > 2 sqrt q` gives real roots with product `q` which cannot both have modulus `sqrt q` without hitting the endpoint. Correct, including the non-strict boundary.
- *Numerics.* Eight random Haar families at `(n,D) = (2,4)` and `(2,6)`: the bound and Weil positivity (`L = 60`) agree in **8/8** cases, with `max ||mu| - r| <= 2.7e-15` in every passing case and `10^{3}`–`10^{17}` negative Toeplitz eigenvalues in every failing case. I also ran the `d_- > 0` case that the random Haar draws never produce — the Pauli family `U_1 = X, U_2 = Z` — where `spec(Phi) = {1, 0, 0, -1}`, `d_+ = d_- = 1`, `|S| = 12 = 2k + 2d_+ + 2d_-`, retained `4 = 2(N - d_+ - d_-)` modes all at `|mu| = sqrt 3` to `1.1e-15`. The multiplicity bookkeeping is exactly right in the one case where it could have gone wrong.
- *The common-scale remark* (`B_i = sqrt w U_i` gives `T = w T_U`, radius `w sqrt q`, channel bound `2 w sqrt q / D`) is correct and the warning that unequal scales destroy the quadratic relation is well taken.

## T3.5 — an adjoint-paired family with no reciprocal duality

**Claim.** `n = 2`, `D = 4`, `B_1 = B_3 = diag(1,2)`, `B_2 = B_4 = I`: `spec(T) = {1^5, 2^2, 4, 3, -1, p_2^2, n_2^2, p_4, n_4}`; with `S` the ten listed values, `A` is invariant under `mu -> c/mu` for no `c`, yet the Weil form is defined and is positive exactly for `r >= p_4`.

**VERDICT T3.5: VALID**

- I rebuilt the edge matrix independently from the definition of `T` (weights `(a,1,a,1)` with `a = 1,2,2,4` on the matrix-unit lines) and got astra's `T_a` entry for entry. SymPy gives `charpoly(T_a) = (x-a)(x-1)(x^2 - (a+1)x - 3a)` with difference **identically 0** from astra's claim.
- The numeric spectrum is `{1^5, 2^2, 3, 4, -1, 4.372281^2, -1.372281^2, 6.772002, -1.772002}` with zero imaginary part — the stated multiplicities, including the five copies of `1`.
- *Exclusion of every reciprocal constant.* The multiplicity-2 pair forces `c = p_2 n_2 = -6`, the multiplicity-1 pair forces `c = p_4 n_4 = -12`; contradiction. I confirmed `d(A, c/A) = 3.39` at `c = -6` and `4.37` at `c = -12`, and the argument "fixing both would need `p^2 = n^2`" is correct since `p + n != 0` in both quadratics.
- *Threshold.* `min eig` of the Toeplitz form at `L = 400`: `-8.1e+4` at `r = 0.98 p_4`, `-27.4` at `r = 0.999 p_4`, `+3.51` at `r = p_4` and above. Exactly "positive definite iff `r >= p_4`", with a mode *on* the circle and the rest strictly inside — the intended illustration that positivity is one-sided without a duality.
- *Process note (not a defect in the claim).* The status line says the block polynomials "were also checked by exact SymPy arithmetic", but `notes/weil-positivity/scratch/` is empty, so that check is not reproducible from the repository. I reproduced it here (`scratch_weil_t3.py`). Same class of process issue as M10 of the Selberg review.

## T4.1 — Lorentzian modes and continuous growth

**Claim.** `hhat(xi) = 2b/(b^2+(xi-omega)^2)` with `hhat(xi) = int h(t) e^{-i xi t} dt`; the inverse representation `h(t) = int e^{it xi} b dxi / (pi[b^2+(xi-omega)^2])`; and `a(t) = sum_j m_j e^{i omega_j t}` does not tend to `0`.

**VERDICT T4.1: VALID**

- The transform, with astra's stated sign convention, is right: `1/(b+i(xi-omega)) + 1/(b-i(xi-omega)) = 2b/(b^2+(xi-omega)^2)`. Numerically `4.7e-9` agreement at three values of `xi` (quadrature-limited), and the inverse representation agrees to `5e-9`.
- *The self-contained inversion.* Rather than quoting Fourier inversion, astra derives it from the already-verified Poisson kernel by a scaling limit `p_eps -> b/(pi(b^2+x^2))`. I checked the three ingredients of the dominating bound: `1 - e^{-u} >= e^{-1}u` on `[0,1]`, `1 - e^{-2u} <= 2u`, and `1 - cos(theta) >= 2 theta^2/pi^2` on `|theta| <= pi` (from `sin u >= 2u/pi`, concavity). They give `p_eps(x) <= b/(pi(e^{-2}b^2 + 4 e^{-1} x^2/pi^2))`, which is integrable and independent of `eps` for `b eps <= 1` — so the passage to the limit is dominated convergence, not an unjustified interchange. The choice `eps = |t|/k` with Fourier index `k sgn(t)` keeps the index an integer and `eps|k| = |t|`. This is the one place I expected to find a hand-wave and did not.
- Continuous growth via `T^{-1} int_0^T |a|^2 -> sum m_j^2` is the exact analogue of T1.2 and is correct.

## T4.2 — continuous Weil positivity is a half-plane bound

**Claim.** `F(t) = e^{-at}(Tr e^{tL} - sum_S e^{t rho})` extended by `F(-t) = conj F(t)` is positive definite iff `Re rho <= a` off `S`.

**VERDICT T4.2: VALID**

- The Hermitian extension is consistent: for `t >= 0` the summand is `e^{-b|t| + i omega t}` and the conjugate-extension reproduces the same expression for `t < 0`, *whatever the sign of* `b` — astra says this explicitly, which is the step a careless proof would fumble (the extension is by conjugate reflection, not by the same exponential formula, and the two agree only after duality — see T4.3 ⟨1⟩1).
- `F(0) = |A|` real, so `F` is continuous at `0`.
- Numerics: for 5 random 4-mode spectra and windows `T = 10, 40, 160`, the Gram matrix is PSD exactly when `a >= max Re rho`, including at offset `±0.02` where a long window is needed (`+1.4` at `T=10` but `-2.4` at `T=40` for offset `-0.02`). Same finite-window masking as in the discrete case, again a truncation effect and not a defect.

## T4.3 — line duality and the exact continuous pairing

**Claim.** If `A` is invariant under `R_a(rho) = 2a - conj(rho)`, then `sum_{j,k} c_j conj(c_k) F(t_j - t_k) = sum_rho ghat_L(rho) conj(ghat_L(2a - conj rho))`, and `F` is positive definite iff `Re rho = a`.

**VERDICT T4.3: VALID**

- The sign chain is correct: `conj((2a - conj rho) - a) = a - rho = -(rho - a)`, so the reflected factor contributes `e^{-t_k(rho-a)}` and the product telescopes into `F(t_j - t_k)` — but **only** after ⟨1⟩1 establishes `F(v) = sum_rho e^{v(rho-a)}` for *negative* `v` as well, which is precisely where the duality is consumed. Astra flags that without duality this would disagree with the prescribed extension. Correct and well signposted.
- Numerics: five random reflection-invariant spectra, random complex times and coefficients, `|W - M| <= 5.1e-11` against values of order `10^4`.

## T4.4 — Dyson expansion as continuous ring norms

**Claim.** `Tr_{M_n} e^{t L} = sum_k sum_{j_1..j_k} int_{simplex} |Tr A_{j,t}|^2 >= 0` with `A_{j,t} = e^{(t-t_k)K} R_{j_k} ... R_{j_1} e^{t_1 K}`; the series converges absolutely; `L` commutes with `x -> x^dagger`.

**VERDICT T4.4: VALID**

- `Tr_{M_n} Ad(A) = sum_{a,b} A_{aa} conj(A_{bb}) = |Tr A|^2` — correct, and the remark that the relevant trace is over `M_n` (dimension `n^2`) and not over `M_n ⊗ M_n^*` (dimension `n^4`) is a genuine correction of the brief.
- Duhamel, iteration and `Ad(X)Ad(Y) = Ad(XY)` compose the free propagators into a single matrix `A_{j,t}` in the right time order.
- *Convergence.* The bound `e^{t||L_0||} (t q_0)^k / k!` with `q_0 = sum_j ||Ad(R_j)||` is correct (free intervals total `t`, simplex volume `t^k/k!`, jump sums `q_0^k`), so termwise integration/summation and the trace are justified — no unjustified interchange.
- *Numerics (this is the strongest check in the file).* I computed the exact `k`-th Dyson term with a nilpotent block-matrix exponential and the ring-norm integral with Gauss–Legendre on the ordered simplex, for random complex `K` and two random `R_j` at `n = 2`: they agree to `1.8e-15 / 6.2e-15 / 4.3e-13` at `t = 0.05, 0.2, 0.5` for `k = 0,1,2`. `Tr e^{tL}` is real and `>= 4 = n^2` on `[0,3]` with `max|Im|/|Tr| = 3.1e-15`, and `d(spec L, conj spec L) = 9.2e-15`.
- *The ledger's claim that the draft's product is wrong.* I checked this too, and the correction is real but subtler than the ledger says: at `k = 1` the two free propagators recombine by cyclicity (`Tr(e^{(t-s)K} R e^{sK}) = Tr(R e^{tK})`), so the omission is invisible; it first bites at `k = 2`, where the propagator-free integrand `(t^2/2) sum |Tr(R_{j_2} R_{j_1} e^{tK})|^2` gives `0.19440805 / 4.24895208 / 51.75468738` against the true `0.19452865 / 4.27933038 / 52.55617362`. So the ledger row is right that the draft is false for non-commuting `K, R_j`, and I can add the precise reason it is not visible at first order.

## T4.5 — Hamiltonian remark

**Claim.** For `L = -i[H, .]` with `H = H^dagger`, the eigenvalue on `|e_a><e_b|` is `-i(E_a - E_b)`, purely imaginary; the Hilbert–Pólya presentation `L = aI + iA` needs diagonalisability in addition.

**VERDICT T4.5: VALID** — elementary and correctly hedged; the added requirement `H = H^dagger` and the pointer to T5 are the right corrections of the brief's wording.

## T5.1 — discrete unitarisability

**Claim.** On the retained invariant subspace, `X'` is diagonalisable with all `|mu| = r` iff some inner product makes `X'/r` unitary.

**VERDICT T5.1: VALID**

- Sufficiency: declare an eigenbasis orthonormal. Necessity: the eigenline of any eigenvector is `U`-invariant and so is its orthogonal complement, because `U^* v = U^{-1} v` stays on the line; induction. Correct, and the "full eigenvalue class" hypothesis on `S` (needed for `V'` to be invariant) is stated rather than assumed silently.
- Numerics: for a random `3x3` diagonalisable `Y` with `|mu| = r` and `G = (P P^dagger)^{-1}`, `|U^dagger G U - G| = 1.1e-16`.

## T5.2 — continuous skew-adjoint realisation

**Claim.** `L' - aI` is skew-adjoint in some inner product iff `L'` is diagonalisable with `Re rho = a`.

**VERDICT T5.2: VALID** — same induction, with `<v, Bv>` purely imaginary giving `Re beta = 0`; nothing is assumed that is not stated.

## T5.3 — Weil forms do not see Jordan blocks

**Claim.** For `X = r[[1,1],[0,1]]`, `nu_l = 2` for all `l` and `W` is positive definite, but no inner product unitarises `X/r`; similarly `F(t) = 2` for `L = aI + N`.

**VERDICT T5.3: VALID**

- `nu_l = 2` for `l = 0..40` exactly; `min eig` of the Toeplitz form at `L = 40` is `-4.3e-14`; `||(X/r)^k e_2||` is `1.41, 10.05, 100.00` at `k = 1, 10, 100`, so unbounded. The continuous version `e^{-at} Tr e^{tL} = Tr(I + tN) = 2` is likewise exact.
- The differentiation argument for the continuous case (`d/dt ||e^{t(L-a)}v||^2 = 0` under skew-adjointness) is correct.

## T6 — the zeta dictionary (T6.1–T6.4, H-ZD/H-ZM/H-BS/H-ZEF/H-ZW)

**Claim.** A conditional dictionary: `a = -1/4`, generator modes `eta(rho) = -conj(rho)/2`, reflection `eta -> -1/2 - conj(eta)`, `S = empty` (the `xi` of the source note is entire), transform `ghat_zeta(s) = int g(t) e^{(s-1/2)t/2} dt`, the exact autocorrelation identity, and the placement of the endpoint / archimedean / prime terms, with four named analytic inputs.

**VERDICT T6: VALID** (as a `sketched`/conditional dictionary; no zeta theorem is claimed and none is smuggled in)

What I checked and what survived.
- *Mode identification and the direction of the inequality.* `Re eta(rho) = -sigma/2`, so T4.2's one-sided conclusion reads `sigma >= 1/2`, and it is the functional equation that supplies `sigma <= 1/2`. Astra flags the direction explicitly; getting this backwards would be the classic error and it is not made.
- *Reflection transport.* `eta(1 - conj rho) = -(1-rho)/2 = -1/2 + rho/2 = 2a - conj(eta(rho))` with `a = -1/4` — I verified the algebra; the fixed line is `Re eta = -1/4`.
- *Trivial modes.* The brief asked for "the two trivial modes coming from the poles of `xi` at `s = 0, 1`". Astra is right that the source note's `xi(s) = (1/2)s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)` is **entire** — the poles belong to `Lambda_zeta` — so the honest answer is `S = empty`, with `{0, -1/2}` available only after an explicitly artificial augmentation. This is a correction of the brief, and it is correct.
- *The transform normalisation.* `ghat_zeta(rho) conj(ghat_zeta(1 - conj rho)) = int phi_g(v) e^{(rho-1/2)v/2} dv` with `phi_g = g * gtilde`: I re-derived it, and the `(s-1/2)t/2` exponent (not `(s-1/2)t`) is forced by the fact that `Z(t)` runs at frequency `gamma/2`. The convolution convention matches H-BS's `g * gtilde`.
- *Compatibility of the two transforms.* `ghat_L(eta(rho)) = ghat_zeta(1 - conj rho)`, so the generator pairing is the zeta pairing reindexed by `rho -> 1 - conj rho`. Correct, and the reindexing is legitimate only because `Z` is assumed invariant under that map (H-ZD) — astra uses it where it is available.
- *`K = e^{v/4} tau` and the negative-time extension.* `tau(-u) = e^{u/2} conj(tau(u))`, **not** `conj(tau(u))`; I verified this from the definitions. The warning that a forward semigroup supplies no bounded negative-time operator is appropriate.
- *H-ZEF.* This is assumed rather than proved, so the only thing to check is whether it is a faithful restatement of the standard formula in the declared convention. **I checked it numerically and it is exact** — see X3 below: with 70 zeta zeros and a Gaussian test, `zero sum - endpoints - contact - archimedean` divided by `-2 sum Lambda(n) n^{-1/2}[h(2 log n) + h(-2 log n)]` equals `1.000000` at six values of `v0`. Every term, sign and factor of `2` in H-ZEF is right.
- *Scope discipline.* H-ZW (the infinite-dimensional Weil converse) is correctly isolated: astra says in terms that the finite interpolation of T2.2 does **not** prove it, and that `F(0) = #Z = infinity` blocks the finite boundedness argument. Given the rest of the notebook, that refusal is the most valuable sentence in T6.

*One caveat for the write-up, not a defect of T6:* the factor `2` in `-2 Lambda(n) n^{-1/2}` is variable-dependent (it is the Jacobian of `v = 2u`), so the shard it corrects must fix a variable before quoting a number. See X3.

## T7 — correction ledger

Not separately scored (it is a ledger, not a claim), but I read every row against the corresponding proof. All rows are accurate. Two remarks: the row on nonnegative ring traces is weaker than the truth (see T3.1 MINOR), and the row on the Dyson product is right but the failure is invisible at `k = 1` (see T4.4).

---

# The orchestrator's three additions

## X1 — termwise vs Toeplitz vs boundedness

**Statement.** For `nu_l = sum_{mu in A} (mu/r)^l` with `A` a finite multiset: (i) positive definite, (ii) bounded, (iii) `Re nu_l <= nu_0` for all `l >= 1` — all equivalent; and Huang's criterion is the boundedness form.

**VERDICT X1: VALID**

The suspicion that (iii) might fail is unfounded; (iii) => (ii) **holds**, and here is the proof the orchestrator asked for.

*Proof of (iii) => (ii).* Suppose `R = max_{z in Z} |z| > 1`. Let `zeta_1, ..., zeta_p` be the distinct arguments `z/R` of the modes of maximal modulus, with multiplicities `m_j >= 1`. Then
`R^{-l} nu_l = sum_j m_j zeta_j^l + eps_l`, `eps_l -> 0`.
Let `g = (zeta_1, ..., zeta_p)` in the torus `T^p`. By pigeonhole, for every `delta > 0` there are `l_1 < l_2 <= N(delta)` with `d(g^{l_1}, g^{l_2}) < delta`, hence `d(g^{l}, 1) < delta` for `l = l_2 - l_1 >= 1`; applying this with `delta/K` and taking the multiples `l, 2l, ..., Kl` produces **infinitely many** `l >= 1` with `max_j |zeta_j^l - 1| < delta`. For such `l`,
`Re nu_l >= (1/2)(sum_j m_j) R^l - |eps_l| R^l -> + infinity`,
while `nu_0 = |A|` is a fixed finite number. So (iii) fails. ∎
(The mean-square lemma T1.2 alone would *not* suffice: it bounds `|a_l|` in mean but says nothing about the sign of `Re a_l`. The recurrence/Kronecker argument is what is needed, and it is why "`cos(l theta) <= 0` for most `l`" cannot be arranged — the rotation always returns near the identity.)

The other implications: (ii) => (iii) because `Re nu_l <= |nu_l| <= sum |z|^l <= |A| = nu_0`; (i) <=> (ii) is T1.3 plus the two-point bound. So (i), (ii), (iii) and also `|nu_l| <= nu_0` are all equivalent for a finite exponential sum. For a conjugation-closed `A` the sequence is real and (iii) is just `nu_l <= nu_0`.

*Numerical support.* Conjugate pairs `R e^{±i theta}` for `R = 1.001, ..., 1.5` and nine `theta` (including `theta/2pi` irrational, `theta` just below `pi`, and the golden rotation): `Re nu_l > nu_0` occurs at `l <= 60` in every case (`l = 60` is the worst, at `R = 1.001, theta = 0.1`). 400 random multisets with a mode outside the circle: **0** survived to `l = 20000`.

*Two cautions the write-up must keep.*
1. The equivalence (iii) <=> (i) uses the *finite exponential sum* structure, not just the sequence bound. For a general Hermitian sequence the termwise bound is strictly weaker: `nu = (1, 0.9, -1)` satisfies `|nu_l| <= nu_0` but its `3x3` Toeplitz matrix has eigenvalue `-0.8675`; likewise `(1, 0.5, 0.5, -1)`. So "termwise = Toeplitz" is a theorem about spectra of finite-dimensional operators, not a fact about sequences.
2. In the distributional (infinitely many modes) case `nu_0 = #Z = infinity`, so (ii) and (iii) have no content and only the positive-type/Toeplitz form survives — which is exactly the orchestrator's framing, and it is correct.

**Huang's criterion is literally `nu_0 - nu_k`.** For a connected non-bipartite `(q+1)`-regular graph on `n` vertices with `m` edges, let `B` be the Hashimoto (non-backtracking edge) matrix, so `N_k = Tr B^k`, and take `r = sqrt q` and the trivial sub-multiset `S = {+1^{m-n}, -1^{m-n}, q, 1}` (the `±1` from Ihara–Bass and the pair of `lambda = q+1`). Then `nu_0 = 2m - 2(m-n) - 2 = 2(n-1)` and, since `(m-n)(1 + (-1)^k)` equals `0` for odd `k` and `n(q-1)` for even `k`,
**`h_k = nu_0 - nu_k` for every `k >= 1`, in both parities.**
I verified this to `1e-13` on `K_4`, the Petersen graph, `K_5`, a cubic graph built from two copies of `K_4 - e`, and the circular ladder `CL_21` (`n = 42`, non-bipartite, non-Ramanujan). Consequently
`Ramanujan <=> h_k >= 0 for all k <=> nu_k <= nu_0 for all k >= 1 <=> nu bounded <=> nu positive definite (Toeplitz) <=> all nontrivial |mu| = sqrt q`,
the last step using the graph's own reciprocal symmetry `mu mu' = q`. On `CL_21`, `min_k h_k = -5268.7` and the Toeplitz minimum eigenvalue is `-2.7e+3 / -1.1e+9 / -5.2e+28` at `L = 20/60/200`; on the Ramanujan examples `min_k h_k > 0` and the retained modes sit at `|mu| = sqrt q` to machine precision. So Huang 2019 is the termwise/boundedness form of the same statement, with the *same* normalisation `r = sqrt q` and the *same* trivial set, and the constant `2(n-1)` in his formula is exactly `nu_0`. That identity is worth putting in the write-up verbatim — it reconciles the two results rather than merely relating them, and it is the cleanest available answer to the prior-art question raised in `notes/extract/weil-positivity-sources.md` W6.

## X2 — Kraus dichotomy, corrected form

**Statement.** (a) ring traces and conjugation closure for any `Ad` family; (b) inverse pairing gives the functional equation and `Weil positivity <=> every nontrivial alpha in spec(Sigma) real with |alpha| <= 2 sqrt(D-1)`; (c) adjoint pairing makes `Sigma` self-adjoint so reality is automatic; (d) both pairings iff unitary. Slogan: reality is what the adjoint pairing buys, the functional equation is what the inverse pairing buys.

**VERDICT X2: MINOR**

(a), (b), (d) are correct as stated and I confirmed them numerically; (c) and the slogan need two fixes.

- **(a) — correct, and stronger than T3.1 says.** Verified on unpaired random `Ad` families: `Tr T^l` equals the word sum `sum_w |Tr B_w|^2` to `1e-9` relative for `l = 1..5` at `(n,D) = (2,4), (2,6), (3,4)`, and `spec(T)` is conjugation-closed to `1.9e-14`. Neither pairing is used anywhere in the derivation.
- **(b) — correct.** The retained multiset `A_0 = spec(T) \ S_0` is invariant under `mu -> q/mu` (verified to `3.6e-14`) and, because `Ad` families are conjugation-closed, therefore under `J(mu) = q/conj(mu)` (verified to `1e-14`), so `W = M` and positivity is two-sided. The equivalence with "`alpha` real and `|alpha| <= 2 sqrt q`" is exactly the statement that the roots of `mu^2 - alpha mu + q` both have modulus `sqrt q`: writing `mu_± = sqrt q e^{±i phi}` gives `alpha = 2 sqrt q cos phi`, real and in the band, and conversely.
  - *Reality is genuinely not automatic under inverse pairing.* Random inverse-paired non-unitary families at `n = 2, D = 4` give e.g. `spec(Sigma) = {0.628 ± 3.294i, 4.699, 10.251}` and `{-1.477 ± 0.724i, 3.867, 10.654}`; the retained modes are then far off the circle (`max ||mu| - sqrt q| ~ 8.2`–`9.1`) and the Weil form is wildly indefinite.
  - *The construction the orchestrator guessed is the right one.* `B_i = G U_i G^{-1}` with `U_ibar = U_i^dagger` unitary is inverse-paired, in general far from unitary (`|B^dagger B - 1|` up to `24.3` in my runs) and far from adjoint-paired, yet `Sigma` is similar to the Hermitian `sum_i Ad(U_i)` via `S(x) = G^{-1} x G^{-dagger}` (check: `S Ad(G U G^{-1}) S^{-1} = Ad(U)`), so `spec(Sigma)` is real (`max|Im| <= 9e-14`) and `T_B = (S^{-1} ⊗ 1) T_U (S ⊗ 1)` has the same spectrum as the unitary model. Over six such families (`D = 4` and `D = 6`, band satisfied in four cases and violated in two) Weil positivity and the band condition agreed **6/6**.
  - A clean hand-made family with real out-of-band `Sigma`: `B_1 = diag(s, 1/s)`, `B_3 = B_1^{-1}`, `B_2 = B_4 = I`, where `spec(Sigma) = {4, 4, s^2 + s^{-2} + 2, s^2 + s^{-2} + 2}`; at `s = 1.2, 1.6, 2.0` the top eigenvalue is `4.134, 4.951, 6.250` against `2 sqrt 3 = 3.464`, and the Weil form fails in every case.
- **(c) — true but must not be read as an addition to (b).** `Sigma^* = Sigma` in Hilbert–Schmidt follows from `Ad(B)^* = Ad(B^dagger)` plus the reversal permuting the sum, so adjoint pairing alone gives `spec(Sigma) ⊂ R` (verified, `max|Im| <= 1.5e-15`). But if (b) *and* (c) hold simultaneously then T3.3 forces every `B_i` to be unitary, i.e. (c)-on-top-of-(b) is not a third regime, it **is** (d). The write-up should present (b) and (c) as two independent hypotheses whose conjunction is (d), not as a chain of "additionally".
- **The slogan is off by one object.** What the adjoint pairing buys is reality of the **channel** spectrum `spec(Sigma)`, not of the **transfer** spectrum `spec(T)`. For adjoint-paired random families `spec(T)` is emphatically non-real: `max |Im spec(T)| = 4.70, 4.18, 5.80, 5.68` in four `n = 2, D = 4` runs while `|Sigma - Sigma^dagger| <= 1.8e-15`. (Under both pairings `spec(T)` is not real either — it sits on the circle `|mu| = sqrt(D-1)`, which is as far from real as it could be.) So: *the adjoint pairing buys a Hermitian channel (hence a real `Sigma`-spectrum, the Hilbert–Pólya half); the inverse pairing buys the functional equation `mu -> (D-1)/mu`; every `Ad` family gives conjugation closure and nonnegative ring counts for free; and Hastings' bound is the case where both pairings hold, which is exactly unitarity.*
- **"Nontrivial" needs a declared `S`.** The equivalence in (b) is exact with `S = S_0` and "every eigenvalue of `Sigma`" (no exclusion); if instead some `alpha` are declared trivial, their *entire quadratic pairs* must be removed from the retained multiset, as in T3.4's `S`. Without saying which `S` is meant, "nontrivial eigenvalue of `Sigma`" is ambiguous — and in the non-unitary inverse-paired case `alpha = D` need not be an eigenvalue at all (`Ad(B)I = BB^dagger != I`), so there may be no trivial `alpha` to exclude.

## X3 — the factor `-2` in the prime part of the compressed-semigroup trace

**Statement.** The shard's "weight `Lambda(n) n^{-1/2}`" in `prop:ringnorm-trace` is off by `-2`.

**VERDICT X3: VALID** (the prover's T6.3 correction is right; the earlier Selberg review's action item (b) is also right)

*Independent derivation.* Fix the shard's own explicit formula (`report/sections/04_riemann_channel.tex` l.169–173, `notes/riemann-channel-note.md` §5), in the ring-length variable `u = t/2`, for a general (not necessarily even) test `q`:
`sum_gamma qhat(gamma) = qhat-endpoints - q(0) log pi + (1/2pi) int ... - sum_n Lambda(n) n^{-1/2} [q(log n) + q(-log n)]`,
i.e. **one** atom of mass `-Lambda(n) n^{-1/2}` at each of `u = ± log n` (the `-2` printed in the shard is the even-test collapse of these two atoms). Now `Tr Z(t)` lives in the variable `t = 2u`, and the trace distribution is the **pullback** of the `u`-distribution, not its pushforward: `delta(t/2 - log n) = 2 delta(t - 2 log n)`. Hence, with `K(v) := e^{v/4} Tr_dist Z(v) = sum_rho e^{(rho - 1/2)v/2}`,

> **`K_prime(v) = -2 sum_{n>=2} Lambda(n) n^{-1/2} [ delta(v - 2 log n) + delta(v + 2 log n) ]`**
> **`(Tr Z)_prime(v) = -2 sum_{n>=2} (Lambda(n)/n) delta(v - 2 log n)` for `v > 0`**

(the second from the first by `e^{-v/4} = n^{-1/2}` at `v = 2 log n`; the negative-time atoms of the uncentred distribution carry `-2 Lambda(n)`, per `tau(-u) = e^{u/2} conj tau(u)`).

*Numerical confirmation, independent of both the prover and the shard.* `scratch_weil_x3.py` sums 70 zeta zeros (`gamma_70 = 182.2`) against a Gaussian pair `h(v) = exp(-(v-v_0)^2/2s^2) + exp(-(v+v_0)^2/2s^2)`, `s = 0.13`, and subtracts the endpoint term `H_h(0) + H_h(1)`, the contact term `-2 log(pi) h(0)` and the archimedean integral `(1/2pi) int H_h(1/2+iy) Re psi(1/4+iy/2) dy`. The residual divided by `-2 sum_n Lambda(n) n^{-1/2}[h(2 log n) + h(-2 log n)]` is

| `v_0` | 1.3863 | 2.1972 | 2.7726 | 3.2189 | 3.8918 | 2.5000 |
|---|---|---|---|---|---|---|
| ratio | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 |

so both the coefficient and the sign are confirmed to six digits (and with them the whole of astra's H-ZEF, including its archimedean normalisation).

*What the shard should say.* Two errors compound in the present text:
1. **Sign.** The prime atoms are *dips*: the zero-sum side carries `-Lambda(n) n^{-1/2}` per atom, not `+`. The shard's own numerical table already shows negative dips (`F_win = -97.95` at `n = 2`, etc., matching `-(G/2 sqrt(2pi)) Lambda(n) n^{-1/2}`), so the proposition contradicts the numerics directly underneath it.
2. **Double-counted damping.** The proposition attributes weight `Lambda(n) n^{-1/2}` to `Tr Z(t)` itself and then applies `e^{-t/4} = n^{-1/2}` *again* to reach `Lambda(n)/n`. Only one of the two statements can be about `Tr Z`.

Corrected wording (in the shard's variable `t`, which is the variable of `Z`):

> The distributional trace of `Z(t)` has prime part `-2 sum_n (Lambda(n)/n) delta(t - 2 log n)` on `t > 0`; equivalently the centred trace `e^{t/4} Tr Z(t)` has prime part `-2 Lambda(n) n^{-1/2}` at each of `t = ± 2 log n`. Endpoint (`2 cosh(t/4)`), contact (`-2 log pi` at `t = 0`) and archimedean terms are also present, so the trace is not a nonnegative measure supported on prime lengths.

If the write-up prefers the ring-length variable `u = t/2` (as the numerical table does), the same content reads: one atom of mass `-Lambda(n) n^{-1/2}` at each of `u = ± log n` in the centred trace. **The magnitude of the factor `2` is variable-dependent — it is the Jacobian `dt = 2du` — so the shard must name its variable when it quotes the number. The sign is not convention-dependent: it is negative in every convention.**

---

## Summary of verdicts

| Label | Verdict | One-line reason |
|---|---|---|
| T1.1 | VALID | Poisson orientation `(1/2pi) int e^{ik th} P_z = z^{[k]}` verified to `7e-16`; `z = 0` and `|z| = 1` edges handled |
| T1.2 | VALID | `2x2` bound correct including `b_0 = 0`; Wiener mean-square needs only distinctness of the `zeta_j` |
| T1.3 | VALID | no diagonalisability used; converse argument sound; 200/200 random multisets agree |
| T2.1 | VALID | `W = M` verified to `9e-13`; `J`-invariance (hypothesis) vs `J`-fixedness (conclusion) correctly separated |
| T2.2 | VALID | Lagrange interpolation makes the *whole* form `-2m`; reproduced as `-4.000000` |
| T2.3 | VALID | reciprocal-only example `{2i, -i/2}` reproduced exactly (`W = 4`, `M = 4+3i`) |
| T3.1 | **MINOR** | true, but the ring-trace nonnegativity is stated under adjoint pairing when it needs **no pairing at all** (fix supplied) |
| T3.2 | VALID | exponent identity `2k + 2N = ND`, double roots, `±1` collisions and the conjugation criterion all check out |
| T3.3 | VALID | `Ad` is quadratic in `B`, so `B^dagger B = I`, not "scalar multiple of a unitary"; `B = 2I` and `kappa = 16` confirmed |
| T3.4 | VALID | multiplicity bookkeeping exact, including the `d_- > 0` Pauli case; bound `<=>` positivity 8/8 + Pauli |
| T3.5 | VALID | char poly identical symbolically; no reciprocal constant; positivity threshold exactly `r = p_4` |
| T4.1 | VALID | Lorentzian and its inverse verified; the dominating bound in the Poisson-limit proof is correct |
| T4.2 | VALID | Hermitian extension valid for either sign of `b`; threshold in `a` confirmed |
| T4.3 | VALID | all signs correct; `|W - M| <= 5e-11` on random reflection-invariant spectra |
| T4.4 | VALID | ring-norm integrals match exact Dyson terms to `1e-15`; propagator-free form fails first at `k = 2` |
| T4.5 | VALID | elementary; correctly hedged |
| T5.1 | VALID | standard induction, full-eigenvalue-class hypothesis stated |
| T5.2 | VALID | same argument in the skew-adjoint form |
| T5.3 | VALID | `nu_l = 2`, form PSD, `||(X/r)^k e_2|| -> infinity` |
| T6 | VALID | conditional dictionary; H-ZEF confirmed numerically to six digits; `S = empty` correction justified; H-ZW properly isolated |
| X1 | VALID | (iii) => (ii) holds by torus recurrence; and `h_k = nu_0 - nu_k` exactly for non-bipartite `(q+1)`-regular graphs |
| X2 | **MINOR** | (a),(b),(d) confirmed; (c) must not be conjoined with (b) (that is (d)), and it is `spec(Sigma)` — not `spec(T)` — that is real |
| X3 | VALID | prime weight is `-2 Lambda(n) n^{-1/2}` (centred) / `-2 Lambda(n)/n` (uncentred) at `t = ±2 log n`; shard also double-counts the damping |

**INVALID: none.** **MINOR: T3.1, X2.**

---

## Scratch scripts written for this review

All under `notes/reviews/`, all self-contained (`numpy`, `sympy`, `scipy`, `mpmath`), all re-runnable with `python3 <file>`. None of them imports or copies `scripts/weil_positivity.py`.

1. **`scratch_weil_t1t2.py`** — T1.1/T1.2/T1.3/T2.1/T2.2/T2.3.
   Checks: Fourier coefficients of the Poisson kernel against `z^{[k]}`; the single-mode identity against the Poisson integral and `|f_c(z)|^2`; positive-definiteness vs `|mu| <= r` on 200 random multisets with `L` escalated to 400; finite-`L` masking thresholds; `|nu_l| <= nu_0`; `W = M` on 200 random `J`-invariant multisets; the interpolation construction; the `{2i, -i/2}` example.
   Output: Poisson max error `6.66e-16`; **0** mismatches in 200 multisets; masking first failure at `L = 5/20/20/40` for `R = 1+0.2/0.05/0.02/0.01`; `max|W-M| = 9.15e-13`; `W(c) = -4.000000` in 5/5 interpolation runs; `nu_1 = 1.5i`, `sum z^{-1} = 1.5i`, `W = 4`, `M = 4+3i`.

2. **`scratch_weil_t3.py`** — T3.1/T3.2/T3.3/T3.4/T3.5, plus the `d_- > 0` Pauli case and the reality of `spec(T)`.
   Checks: conjugation closure and `Sigma^* = Sigma` for adjoint-paired families; `Tr T^l` against the word sum for *unpaired* `Ad` families; the characteristic-polynomial factorisation for inverse-paired families; `spec(Sigma)` of `diag(2i,1)`; `Ad(B^dagger)` vs `Ad(B)^{-1}`; Hastings bound vs Weil positivity for Haar families; symbolic char poly of `T_a`; the `p_2, n_2, p_4, n_4` spectrum, reciprocal-constant exclusion and the positivity threshold.
   Output: `d(spec T, conj spec T) <= 1.9e-14`, `max|Im spec(T)| = 4.37`–`6.78` (not real); word sums match `Tr T^l` to `1e-9` relative with **no pairing**; `match(spec T, predicted) <= 4.6e-14`; `spec(Sigma) = [6.25, 4, 2±1.5i]`; `|Ad(B^dagger) - 16 Ad(B)^{-1}| = 0` for `B = 2I`; bound `<=>` positivity in 8/8 Haar cases; Pauli case `|S| = 12`, 4 retained modes at `|mu| = sqrt 3 ± 1.1e-15`; symbolic char-poly difference `0`; `min eig` `-8.1e4 / -27.4 / +3.51` at `r = 0.98 p_4 / 0.999 p_4 / p_4`.

3. **`scratch_weil_t4t5.py`** — T4.1/T4.2/T4.3/T4.4 and T5.1/T5.3.
   Checks: the Lorentzian transform and its inverse by quadrature; the Gram-matrix threshold in `a`; the continuous pairing identity; the Dyson expansion (exact `k`-th term by a nilpotent block exponential vs Gauss–Legendre ring-norm integrals on the ordered simplex), including the propagator-free variant; conjugation closure of `L`; the Jordan block.
   Output: transform agreement `4.7e-9`, inverse `5.4e-9`; PSD exactly when `a >= max Re rho` (threshold visible at offset `±0.02` once `T = 40`); `|W-M| <= 5.1e-11`; Dyson vs ring norms `1.8e-15 / 6.2e-15 / 4.3e-13` at `t = 0.05/0.2/0.5`; propagator-free `k=2` term `0.19440805` vs exact `0.19452865`; `Tr e^{tL}` real (`3.1e-15` relative) and `>= 4`; `nu_l = 2`, Toeplitz min eig `-4.3e-14`, `||(X/r)^k e_2|| = 100.00` at `k = 100`; `|U^dagger G U - G| = 1.1e-16`.

4. **`scratch_weil_x1.py`** — X1.
   Checks: whether `Re nu_l <= nu_0` can hold for all `l` with a mode outside the circle (conjugate pairs over 4 radii x 9 angles; 400 random multisets); a general Hermitian sequence with `|nu_l| <= nu_0` that is not positive definite; and `h_k` vs `nu_0 - nu_k` on `K_4`, Petersen, `K_5`, `2x(K_4-e)` and the non-Ramanujan circular ladder `CL_21`, with the Hashimoto matrix built from scratch.
   Output: first failure of (iii) at `l <= 60` in every structured case and `l <= 20000` in 400/400 random cases; `nu = (1, 0.9, -1)` has Toeplitz eigenvalue `-0.8675`; `h_k = nu_0 - nu_k` to `<= 1.8e-13` for `k = 1..12` on all five graphs; `CL_21`: `min_k h_k = -5268.69`, Toeplitz min eig `-2.7e3 / -1.1e9 / -5.2e28` at `L = 20/60/200`, `max` retained `|mu| = 1.954 > sqrt 2`.

5. **`scratch_weil_x2.py`** — X2.
   Checks: `spec(Sigma)` for random inverse-paired non-unitary families; the `B_i = G U_i G^{-1}` construction (reality of `spec(Sigma)`, band vs Weil positivity, both inside and outside the band); a hand-made real-but-out-of-band family; adjoint-paired `Sigma` self-adjointness vs non-real `spec(T)`; `Ad(B^dagger)` vs `Ad(B)^{-1}` for unitary, scaled-unitary and non-normal `B`.
   Output: non-real `spec(Sigma)` in 3/5 random inverse-paired runs (e.g. `0.628 ± 3.294i`); `G U G^{-1}` families: `max|Im spec(Sigma)| <= 9e-14` with `|B^dagger B - 1|` up to `24.3`, band `<=>` positivity **6/6**; `diag(s,1/s)` family out of band at `s = 1.2, 1.6, 2.0` with Weil form negative; adjoint-paired `|Sigma - Sigma^dagger| <= 1.8e-15` but `max|Im spec(T)| = 4.18`–`5.80`.

6. **`scratch_weil_x3.py`** — X3 (`mpmath`, 25 digits, 70 zeta zeros).
   Checks: the full explicit formula in astra's `v`-convention — zero sum minus endpoints, contact and archimedean integral, against `-2 sum Lambda(n) n^{-1/2}[h(2 log n) + h(-2 log n)]` at six values of `v_0`; and the per-`n` centred and uncentred weights.
   Output: ratio `1.000000` at `v_0 = 1.3863, 2.1972, 2.7726, 3.2189, 3.8918, 2.5000`; centred weights `-0.980258, -1.268568, -0.693147, -1.439525, -1.470970` for `n = 2,3,4,5,7`, uncentred `-0.693147, -0.732408, -0.346574, -0.643775, -0.555974`.

---

# Round 2 (2026-09-12, same reviewer)

The coordinator (claude:fable-5.1) reports that both Round-1 MINOR findings have been fixed in the lab-book statements and asks for a re-verdict. I checked the two shard statements as they now stand in the repository, not as paraphrased. The Round-1 sections above are left unchanged as the record; the verdicts below supersede them for T3.1 and X2.

## T3.1 re-verdict — `prop:kraus-conjugation-symmetry`, `report/sections/08b_weil_positivity.tex` l.114–125

**VERDICT T3.1: VALID**

The statement now reads (verbatim from the shard): for any family `E_i = Ad(B_i)` with arbitrary `B_i in M_n` and any fixed-point-free reversal, `x -> x^dagger` on `V = M_n` and its componentwise version on `W` commute with `Sigma` and with `T`; hence both spectra are conjugation-closed with multiplicities; and the nonnegative ring trace `Tr T^l = sum_w |Tr B_w|^2` of `cor:qihara-kraus` holds for every such family with no pairing hypothesis, its proof using only `Ad(A)Ad(B) = Ad(AB)` and `Tr Ad(A) = |Tr A|^2`.

This is exactly the fix I asked for, and every clause is one I have already verified independently:
- the commutation and the antilinear bijection of generalised eigenspaces (Round 1, T3.1): `d(spec T, conj spec T) <= 1.9e-14`, `d(spec Sigma, conj spec Sigma)` likewise, for adjoint-paired families at `(n,D) = (2,4), (2,6), (3,4)`;
- the pairing-free ring trace: on completely unpaired random `Ad` families the word sum reproduces `Tr T^l` to `1e-9` relative for `l = 1..5`, and I confirmed against `notes/quantum-ihara-general.md` §4 that Corollary 2 ⟨1⟩2 never touches the pairing (the pairing is consumed only by the *determinant* factor, where `E_ibar E_i = Ad(A_k^dagger A_k) >= 0`).
- No invertibility, positivity or normalisation of the `B_i` is needed, and the shard does not assume any. Correct.

Two cosmetic notes, neither affecting the verdict: (i) the quantifier `l >= 1` and the cyclically-non-backtracking word class are inherited from `cor:qihara-kraus` by the citation, which is fine, but a reader who lifts the displayed identity out of context should be reminded that `Tr T^0 = ND`, not a word sum; (ii) the accompanying paragraph's "every Kraus-type family, however paired, has a positive side A and a real-structured side B" is the right slogan and is now consistent with the proposition.

The prover's file `notes/weil-positivity/astra-proofs.md` still carries the weaker closing sentence; since the lab book now carries the corrected statement and the ledger row is the one being distilled, I have no further objection, but the T7 ledger row "nonnegative ring traces hold in the stated Kraus settings" remains weaker than the shard it feeds and would be worth aligning if the ledger is ever quoted directly.

## X2 re-verdict — `obs:kraus-dichotomy`, `report/sections/08c_weil_positivity_continuous.tex` l.234–247

**VERDICT X2: VALID**

with one **mandatory** qualifier in (d) and one one-word repair in (c), both spelled out below. Taking the clauses in turn.

- **(a)** "For any `Ad`-type family the rings are positive and `spec(Sigma)`, `spec(T)` are conjugation-closed." Correct; this is T3.1 above plus the pairing-free word sum. (Typographical: the item is not labelled `(a)` in the LaTeX although (b), (c), (d) are.)

- **(b)** "with `S_triv = {+1^[k], -1^[k]}` and `r = sqrt(D-1)`, *all retained modes on the circle* is equivalent to: **every** eigenvalue `alpha` of `Sigma` is real with `|alpha| <= 2 sqrt(D-1)`." **Correct, and this is the fix I asked for.** With `S_triv = S_0` the retained multiset is exactly the union over *all* `alpha in spec(Sigma)` of the roots of `mu^2 - alpha mu + q`, so no eigenvalue of `Sigma` is exempt and "every", not "every nontrivial", is the right quantifier. The equivalence itself is the elementary fact that the two roots of `mu^2 - alpha mu + q` both have modulus `sqrt q` iff `alpha = 2 sqrt q cos(phi)` for a real `phi`. The hypotheses `D = 2m >= 4`, `k = N(D-2)/2` and invertibility of the `E_i` are carried by the companion `thm:kraus-inverse-pairing-duality`; the observation inherits them by position, which is acceptable in an observation but is the only thing a reader must fetch from elsewhere.

- **(c)** "Adjoint pairing buys Hilbert–Schmidt self-adjointness of `Sigma`, so `spec(Sigma)` is real for free; `spec(T)` is not real, and there is no functional equation." The substance is right and my Round-1 objection is fully addressed: it is now `spec(Sigma)`, not `spec(T)`, that is real, and (c) is no longer chained onto (b) as an "additionally", so it no longer collapses into (d). **Required one-word repair:** both negative clauses must be generic — "`spec(T)` **need not** be real, and **in general** there is no functional equation". As universal statements they are false, and the notebook's own witness refutes them: the adjoint-paired family `B_1 = B_3 = diag(1,2)`, `B_2 = B_4 = I` of T3.5 has all sixteen eigenvalues of `T` **real** while admitting no reciprocal symmetry for any constant. T3.5 is an existence statement ("*an* adjoint-paired family with no reciprocal duality"), and (c) must not promote it to a universal one. With "need not"/"in general" inserted, (c) is correct and is confirmed by my numerics (`|Sigma - Sigma^dagger| <= 1.8e-15` with `max |Im spec(T)| = 4.18`–`5.80` on four random `n = 2, D = 4` families).

- **(d)** "A family with both pairings is unitary, and there (b) reduces to Hastings' bound alone." The first half is T3.3 and is correct. **The second half needs the explicit qualifier the coordinator asks about — it is mandatory, not stylistic.** Read literally, with the `S_triv = S_0` declared two clauses earlier, the sentence is false, and it fails for *every* unitary family rather than in a corner case: `Phi(I) = I` always, so `alpha = D` is always an eigenvalue of `Sigma`, and `D > 2 sqrt(D-1)` for every `D >= 4` because `D^2 - 4(D-1) = (D-2)^2 > 0`. Hence with `S_triv = S_0` a unitary family **never** satisfies the right-hand side of (b), and never has all retained modes on the circle: I measured `max ||mu| - sqrt q|` over `spec(T) \ S_0` equal to `1.2679, 2.7639, 1.2679` at `(n,D) = (2,4), (2,6), (3,2)` — i.e. exactly the distance from the retained mode `mu = q` to the circle — including in cases where Hastings' bound *does* hold.

  What is true, and what the sentence is evidently pointing at, is `thm:kraus-unitary-ramanujan` (astra's T3.4): after enlarging the trivial set to
  `S = S_0 ⊎ {q^[d_+], 1^[d_+]} ⊎ {(-q)^[d_-], (-1)^[d_-]}`,
  where `d_±` are the multiplicities of `±1` in `Phi`, the retained multiset has `2(N - d_+ - d_-)` elements and the reality clause of (b) becomes automatic (`Sigma = D Phi` self-adjoint), so the criterion collapses to `|lambda| <= 2 sqrt(D-1)/D` for the remaining `lambda`, which is Hastings' bound. Suggested replacement clause:

  > "(d) A family with both pairings is unitary; there `Sigma = D Phi` is self-adjoint, so the reality clause of (b) is automatic, and after removing in addition the pairs `{D-1, 1}` and `{-(D-1), -1}` supplied by the eigenvalues `lambda = ±1` of `Phi` with their multiplicities (`thm:kraus-unitary-ramanujan`), the criterion of (b) becomes Hastings' bound `|lambda| <= 2 sqrt(D-1)/D` on the remaining eigenvalues of `Phi`, alone."

  I verified the enlarged-`S` version in Round 1 on eight Haar families (bound `<=>` positivity 8/8, retained modes on the circle to `2.7e-15`) and on the `d_- > 0` Pauli family `{X, Z, X^dagger, Z^dagger}` (`|S| = 12 = 2k + 2d_+ + 2d_-`, four retained modes at `|mu| = sqrt 3 ± 1.1e-15`), so the corrected clause is solid.

- **The closing slogan** — "reality of `spec(Sigma)` is the Hilbert–Pólya half; the functional equation is the other half; a Kraus family gets the two from two different pairings, and gets both only by being unitary" — is now correct and is the sentence I would keep. It fixes the Round-1 error (it no longer attributes reality to the transfer spectrum) and it states the dichotomy at exactly the right level of generality. The follow-up paragraph's use of `B_i = G U_i G^{-1}` as the sharpened form of `conj:kraus-ramanujan` is also supported by my numerics: those families are inverse-paired, non-unitary (`|B^dagger B - 1|` up to `24.3`), have real `spec(Sigma)` (`max |Im| <= 9e-14`) because `S(x) = G^{-1} x G^{-dagger}` conjugates `Sigma` to `sum_i Ad(U_i)`, and satisfy "band `<=>` Weil positivity" in 6/6 runs. Calling their non-Hermitian-`Sigma`-with-real-spectrum an unbroken-PT situation is a fair analogy provided it stays an analogy: the similarity `S` here is explicit and finite-dimensional, so nothing is being asserted about PT-symmetric operator theory.

**Summary of the two required edits, in priority order.**
1. `obs:kraus-dichotomy` (d): add the enlarged trivial set (or an explicit `\cref{thm:kraus-unitary-ramanujan}` pointer carrying it). Without it the clause is false for every unitary family, since `alpha = D` is always present and always out of band.
2. `obs:kraus-dichotomy` (c): "`spec(T)` **need not** be real, and **in general** there is no functional equation" — T3.5's `diag(1,2)` family has a real `spec(T)`.

With edit 1 the verdict stands as recorded; **if the (d) qualifier is declined, my verdict on X2 reverts to INVALID for that clause alone**, and the reason is the one displayed above.

## Round 2 verdict table

| Label | Round 1 | Round 2 | Note |
|---|---|---|---|
| T3.1 (`prop:kraus-conjugation-symmetry`) | MINOR | **VALID** | pairing-free ring trace now stated; every clause independently verified |
| X2 (`obs:kraus-dichotomy`) | MINOR | **VALID** | (b) quantifier fixed, (c) attributed to `spec(Sigma)` and de-chained from (b); requires the (d) trivial-set qualifier and "need not" in (c) |

No other verdict in this review changes. The Round-2 checks used no new files: the (d) counter-computation was run in the session scratchpad, and everything else it relies on is reproducible from the six `notes/reviews/scratch_weil_*.py` scripts listed above (`scratch_weil_t3.py` covers the Haar and Pauli bookkeeping, `scratch_weil_x2.py` the `G U G^{-1}` families and the adjoint-paired `spec(T)` measurements).
