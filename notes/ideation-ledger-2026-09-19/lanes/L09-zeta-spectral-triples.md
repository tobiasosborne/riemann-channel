# Lane L09: zeta spectral triples sidequest (zst, ihz, CCM)

Scope: the 2026-09-17/18 sidequest reading Connes-Consani-Moscovici, arXiv:2511.22755 ("Zeta
spectral triples"), prototyping it in mpmath, implementing it rigorously in C (`zst/`),
benchmarking it past the paper, then planning and building the Ihara-zeta analogue (`ihz/`) in
five lanes. This ledger records ideas, leads, conjectures, open questions and dead routes only;
the established mathematics is in the source files.

Abbreviations used below exactly as the sources use them: `CCM` = arXiv:2511.22755,
`CS` = Connes-van Suijlekom arXiv:2511.23257, `IH-n` / `NG-n` / `Q-n` = claims, non-generalisation
items and open questions of `ihara/lanes/theory.md`.

## Coverage

| file | lines | read fully? | ideas found |
|---|---:|---|---:|
| notes/zeta-spectral-triples/plan.md | 477 | yes | 24 |
| notes/zeta-spectral-triples/benchmark.md | 88 | yes | 9 |
| notes/zeta-spectral-triples/report-2026-09-18.md | 67 | yes | 6 (all also in plan/benchmark) |
| notes/zeta-spectral-triples/ihara/plan.md | 491 | yes | 28 |
| notes/zeta-spectral-triples/ihara/lanes/theory.md | 1040 | yes | 30 |
| notes/zeta-spectral-triples/ihara/lanes/numerics.md | 393 | yes | 17 |
| notes/zeta-spectral-triples/ihara/lanes/literature.md | 724 | yes | 9 |
| notes/zeta-spectral-triples/ihara/lanes/code-audit.md | 571 | yes | 9 |
| notes/zeta-spectral-triples/ihara/lanes/notebook-extract.md | 649 | yes | 8 |
| zst/README.md | 89 | yes | 4 |
| ihz/README.md | 54 | yes | 4 |

Total ledger entries: 92 (recurring ideas merged into one entry carrying all source lines; the per-file counts below therefore sum to more than 92).

## Ideas and leads

### L09-001 The explicit-formula distribution as an abstract input (`zst_weil_t`)
- Source: notes/zeta-spectral-triples/plan.md:36-38, 213-247; ihara/plan.md:305-321
- Raised by: orchestrator (Claude), reading CCM
- Status at last mention: partially explored (design fixed, M3 not built; `ihz_weil_t` built as a separate discrete type)
- Content: the whole pipeline after the pair `(a_n, b_n)` is independent of which zeta one is doing. The proposal is a single C struct carrying four things: atoms `w_k delta(y - y_k)` inside the window (primes, prime geodesics, ring norms), exponential-series kernels `sum_k P_j(k) e^{-(d_j k + mu_j)x}` (gamma factors, the Selberg identity term), rank-one pole terms (the trivial divisor moved to the right-hand side), and a scalar `shift` multiplying `F(1)`. The claim is that "every explicit formula in sight (Riemann, Dirichlet, Dedekind, Hecke, GL(2), Ihara, Artin-Schreier/Weil, Selberg compact and modular)" fits this shape, with `deg P <= 2` sufficing.
- Lead: implement `zst_weil_ab(a, b, N, W, prec)` once (milestone M3) and then every new L-function or zeta becomes a data builder, not a new pipeline. If it worked, the Selberg, Ihara and graded-divisor cases all run through certified code that already exists.
- Related: L09-010, L09-011, L09-014, L09-016, L09-084.

### L09-002 Any real distribution on the window gives the same structure theorem
- Source: notes/zeta-spectral-triples/plan.md:60-63
- Raised by: orchestrator (Claude), reading CCM
- Status at last mention: raised, not pursued as a statement in its own right
- Content: the matrix of the window Weil form always has the Loewner shape `tau_{nm} = (b_n - b_m)/(n - m)`, `tau_{nn} = a_n`, equivalently `[D, tau] = |beta><eta| - |eta><beta|` (rank-two commutator). "any real distribution `D` on `[0, L]` gives such a matrix, and the paper's theorems (real spectrum, determinant formula) hold for it verbatim." So reality of the spectrum has nothing to do with number theory.
- Lead: state and use this as the generality theorem underlying L09-001; it is also what makes the graph case an instance rather than an analogue (see L09-036). Consequence: any experiment about which distributions give good approximations is legitimate, because reality never fails.
- Related: L09-001, L09-050, L09-051.

### L09-003 A typo in the paper's displayed constant `c(L)`
- Source: notes/zeta-spectral-triples/plan.md:28-29, 163-171; report-2026-09-18.md:19-20
- Raised by: orchestrator (Claude), from independent re-derivation
- Status at last mention: pursued, settled (the paper's numbers come from the correct constant; only the display is wrong)
- Content: CCM display `c(L) = int_0^L (1 - e^{-x/2})/(e^x - e^{-x}) dx` (`0.352` at `lambda = 3`); the identity they use actually needs `C(L) = int_0^L (1 - e^{-x/2}) rho(x) dx = 0.575`, added to the `(cos - 1)` integral rather than the `(cos - e^{-x/2})` one. The difference is `n`-independent, hence a multiple of the identity: it moves `eps_N` by about `0.45` (which would make it negative) but leaves `xi` and the spectrum untouched.
- Lead: none stated beyond recording it; worth telling the authors if the work is ever written up.
- Related: -

### L09-004 The accuracy law: one exponentially small number, the prolate defect
- Source: notes/zeta-spectral-triples/plan.md:172-177; benchmark.md:41-45; report-2026-09-18.md:38-40
- Raised by: TJO (asked the benchmark question) and orchestrator (Claude)
- Status at last mention: pursued, positive; measured on a grid with certified bounds
- Content: two mpmath data points first suggested `|z_1 - gamma_1| ~ 5e4 (1 - chi_4(lambda))` and `eps_N ~ 10 (1 - chi_4(lambda))`, with `1 - chi_4` the Fuchs asymptotic `~ (2^14/3) sqrt2 pi^5 lambda^9 e^{-4 pi lambda^2}`. The certified benchmark then gave, across `x = lambda^2 = 13..50`, `log10 err(z1) ~ -5.4 x + 15`, i.e. 5.4 digits per unit of `x`, matching `4 pi / ln 10 = 5.46`; and `N` does not enter at all. With only the primes up to 50 the first zero is certified to 249 digits.
- Lead: compare the measured law against actual prolate eigenvalues once the prolate module exists (L09-017); this is the quantitative form of the paper's Figure `fpro1` and the exact quantity CCM's missing proof must control.
- Related: L09-007, L09-017, L09-041.

### L09-005 The second law: accuracy degrades linearly in the height of the zero
- Source: notes/zeta-spectral-triples/benchmark.md:46-50; report-2026-09-18.md:41-42
- Raised by: orchestrator (Claude), from the benchmark
- Status at last mention: pursued, positive (empirical, uniform across the grid)
- Content: at every `x`, `log10 err(z_k) ~ log10 err(z1) + 0.37 gamma_k`. Hence the usable range of zeros grows linearly in `x`: zeros certified below `1e-3` reach `gamma_max ~ 14.6 x - 40`, and below `1e-50`, `gamma_max ~ 14.6 x - 170`. The slope `0.37` is independent of `x`, which is the striking part.
- Lead: "The linear degradation in gamma (item 2) is the quantitative shape of what a proof would have to control" (benchmark.md:87-88). Nobody has explained the constant `0.37`; deriving it from the prolate side would be a real result.
- Related: L09-004, L09-017.

### L09-006 The third law: `N` saturates at about `7.5 x`
- Source: notes/zeta-spectral-triples/benchmark.md:51-54; report-2026-09-18.md:43-44
- Raised by: orchestrator (Claude), from the benchmark
- Status at last mention: pursued, positive
- Content: the bandwidth actually needed is `s_max = gamma_max L / 2 pi ~ 2.3 x`, and `N ~ 1.5 s_max` suffices; beyond that `N` only adds spurious roots that the certificate still has to account for. Measured: `x = 20` gives 84 zeros below `1e-3` at `N = 100` and 95 at both `N = 150` and `N = 200`; `x = 30` gives 172 at both `N = 300` and `N = 450`.
- Lead: use `N = 7.5 x` as the default so that the cost `O(N^3)` is not wasted; the remaining question is whether the spurious roots past saturation can be excluded a priori rather than certified away.
- Related: L09-005, L09-027.

### L09-007 `eps_N` as a certified instance of Weil positivity, window by window
- Source: notes/zeta-spectral-triples/plan.md:186, 339-340; benchmark.md:55-57; plan.md:188-189
- Raised by: orchestrator (Claude)
- Status at last mention: pursued, positive (certified for `x = 13..50`)
- Content: `log10 eps_N ~ -5.1 x + 8`, `N`-independent once `N` is saturated. Each run certifies `eps_N > 0` and the even-simple hypothesis, i.e. each run is "a certified instance of Weil positivity on each window". CCM's Corollary `strange` says `mu_lambda` is decreasing and `mu_lambda -> 0` would imply RH, so the certified numbers are a rigorous chain of windowed Weil-criterion instances.
- Lead: certify `eps_N` monotone in both `N` and `lambda` (property test proposed at plan.md:339-340) and push the grid until the law breaks or does not.
- Related: L09-004, L09-050, L09-052.

### L09-008 `x = 100`: does the first zero reach 500 digits?
- Source: notes/zeta-spectral-triples/plan.md:459; benchmark.md:33-34, 61-63; report-2026-09-18.md:33-35, 66-67
- Raised by: orchestrator (Claude)
- Status at last mention: attempted, unfinished (OOM-killed at the 10.7 GB cgroup limit on the first version; not retried after the memory rework)
- Content: extrapolating `N^3 prec^1.6`, `x = 100` (`N = 1000`, 4000 bits) should take about 80 minutes and certify the first zero to about 500 digits with about 700 zeros below `1e-3`. `x = 60` and `x = 80` completed with complete certified spectra (`x = 80` in 55 min, 2.4 GB) but their output files were lost to a cleanup mistake before the tables were extracted.
- Lead: rerun `x = 100` with the reworked memory footprint; the headline would be "the primes up to 100 determine the first zero of zeta to 500 digits, certified". Also regenerate the lost `x = 60` and `x = 80` tables.
- Related: L09-030, L09-009.

### L09-009 The reference zeros are the ceiling, not the construction
- Source: notes/zeta-spectral-triples/benchmark.md:83-85
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued
- Content: comparison uses arb's `acb_dirichlet_zeta_zeros`, computed at full precision only for the first 20 zeros and at 400 bits beyond, "so bounds below 1e-100 are only reported for k <= 20". The construction's own output is certified far tighter than the truth it is compared against.
- Lead: compute high-precision zeta zeros independently (or raise arb's precision for `k > 20`) so that the deep-`x` runs can certify hundreds of digits for zeros beyond the twentieth. Without this, the 200- and 249-digit results only exist for the lowest zeros.
- Related: L09-008.

### L09-010 Derive the archimedean constants instead of typing them in (M3)
- Source: notes/zeta-spectral-triples/plan.md:245-247, 366-371, 472-473
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued (M3 never started)
- Content: "The archimedean constants for a general kernel are derived once from the regularisation, never typed in per case." Each gamma factor `Gamma(s/2 + a)` on the critical line contributes `sum_k e^{-(2k + 2a)x}`-type kernels via Gauss's integral for `psi`; `Gamma_C` has step 1; the Selberg identity term `1/(4 sinh^2(x/2)) = sum_k k e^{-kx}` has a polynomial prefactor. Explicitly flagged as "the one place in the `zst` plan where a derivation, not a transcription, is required".
- Lead: do the derivation, then validate by regenerating zeta's own `w(L)` and `C(L)` to working precision, and by reproducing `L(s, chi_{-4})` zeros. This is the gate on every other extension (Dirichlet, Hecke, Selberg).
- Related: L09-001, L09-011, L09-013, L09-015.

### L09-011 Dirichlet characters, and the conductor is invisible to the spectrum
- Source: notes/zeta-spectral-triples/plan.md:366-371, 408-413
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued
- Content: atoms become `w = -chi(p^m) Lambda(p^m) p^{-m/2}`, the kernel comes from `Gamma_R(s + a)` with `a` the parity, there is no pole term, and the conductor enters only as an identity shift. Stated as "a fact worth stating: the spectrum of the construction does not see the conductor except through the atoms."
- Lead: build `zst_weil_dirichlet` for real primitive characters and test against `acb_dirichlet_hardy_z` root isolation. Relevance named: `conj:galois-graded-bond` (zeros of `L(s, chi)` organised by characters) — the tool would give one self-adjoint operator per character on a common window.
- Related: L09-010, L09-012.

### L09-012 Complex characters need a theorem, not just code
- Source: notes/zeta-spectral-triples/plan.md:415-419, 474
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued; two routes named, route (a) preferred
- Content: for a non-self-dual L-function the distribution satisfies `D(-y) = conj D(y)`, so `tau` is Hermitian with complex `b_n` and the same rank-two commutator. Route (a): take the real form of the pair `{chi, conj chi}` (atoms `2 Re chi(p^m)...`), zeros are the union, matrix real symmetric. Route (b): a Hermitian version of the Connes-van Suijlekom structure theorem, "to be checked in arXiv:CS 2025 before implementing". Listed in the risks as "Hermitian (complex character) case needs the theorem, not just code."
- Lead: read `CS` for a Hermitian statement; if it is not there, either prove it or take route (a). Consequence: without this, half of all L-functions are out of reach.
- Related: L09-011, L09-047.

### L09-013 Dedekind, Hecke and GL(2) L-functions
- Source: notes/zeta-spectral-triples/plan.md:421-424
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued
- Content: atoms at `m log N(P)` with Frobenius/Satake weights (`(alpha_p^m + beta_p^m) log p p^{-m/2}` for a weight-`k` form), kernels `r_1 Gamma_R + r_2 Gamma_C` or `Gamma_C(s + (k-1)/2)`, pole term for Dedekind.
- Lead: the concrete entry point named is `conj:weil-lps-hecke` — the Hecke identification of the Weil-LPS joint spectra "gives concrete weight-2 forms of level `p` to feed in". If the construction reproduces those zeros, the notebook's LPS channels and the CCM machine are talking about the same operator.
- Related: L09-001, L09-010.

### L09-014 Finite transfer operators as the exact sanity anchor (`zst_weil_discrete`)
- Source: notes/zeta-spectral-triples/plan.md:388-395, 426-432
- Raised by: orchestrator (Claude)
- Status at last mention: pursued, positive — became the whole `ihz/` MVP
- Content: for a graph, curve or Weil-LPS channel the group is `Z`, the window is `{-M..M}`, the atoms are the ring norms `Tr E^l` minus the trivial part at `l = 1..M` with weights `q^{-l/2}`, there is no archimedean kernel, and the trivial divisor enters as pole terms. Three uses were listed: (a) an exact sanity anchor, (b) the under-resolved window regime, (c) graded divisors (zeros odd, poles even) where the Weil form is `sum_ret (-nu(lambda)) |f_hat|^2`.
- Lead: implemented as `ihz/`; the three uses became L09-039, L09-041 and L09-058/L09-059.
- Related: L09-018, L09-034, L09-039, L09-041, L09-059.

### L09-015 Selberg zeta, the cusp comb, and a computational form of H-CUSP-BRIDGE
- Source: notes/zeta-spectral-triples/plan.md:396-401, 434-441; ihara/plan.md:403-405
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued (named as the first infinite object beyond `zeta`)
- Content: compact surface: atoms at `k l(gamma)` with weights `l(gamma_0)/(2 sinh(k l/2))`, identity kernel `(Area/4 pi) sum_k k e^{-kx}` (polynomial prefactor, step 1), trivial divisor from the `Gamma_2` factors, divisor to recover `1/2 +- i r_j`. Modular surface: add the parabolic (digamma) kernel and the scattering atoms `Lambda(n)/n` at `2 log n` (the cusp comb of shard 09c, `obs:modular-scattering-sector`). The question, stated plainly: "whether one self-adjoint operator built from prime geodesics plus the cusp comb reproduces both the Maass `r_j` and the `gamma_n/2` is a computational form of the H-CUSP-BRIDGE question."
- Lead: build the Selberg data builder once M3 exists and run it; geodesic data is sparse for small windows (traces `t <= 2 cosh(L/2)`), so the windows must be larger than in the zeta case, which makes the scaling work of M4 a prerequisite. This is the single item with the most direct bearing on the notebook's own Selberg lane (shards 03e/03f, 09c).
- Related: L09-010, L09-019, L09-046, L09-084.

### L09-016 Feed the notebook's own objects in: graded channels and cMPS generators as window data
- Source: notes/zeta-spectral-triples/plan.md:402-404, 443-447
- Raised by: orchestrator (Claude)
- Status at last mention: raised, partially explored (the curve/graded sign was implemented in `ihz`, the general channel input was not)
- Content: once the discrete and Selberg cases exist, the input can be phrased directly in the notebook's terms — "a graded transfer channel or cMPS generator gives ring norms (atoms) and a designated trivial divisor (poles); `libzst` returns a self-adjoint operator and a positive form. This is the bridge from the notebook's definitions to a computable object, and the natural home for experiments on 'Hermitian channel plus lift versus odd block unitary'."
- Lead: implement `ihz_weil_t` as a constructor of the general `zst_weil_t` (ihara/plan.md:403-405, milestone G5) so that a channel defined in the notebook can be run through the certified machinery without new code.
- Related: L09-001, L09-014, L09-019, L09-059, L09-088.

### L09-017 The prolate side: the part that touches the missing proof
- Source: notes/zeta-spectral-triples/plan.md:188-196, 374-377, 449-452, 460-461, 475
- Raised by: a paper (CCM's own Section 7 strategy), taken up by the orchestrator
- Status at last mention: raised, not pursued ("their own project")
- Content: CCM's route to a proof is that `Xi` is the Fourier transform of `E(h)`, `h` the unique combination of Hermite functions `h_0, h_4` with zero integral; `k_lambda` is the same with prolate functions `h_{0,lambda}, h_{4,lambda}`; its Fourier transform converges to `Xi` on substrips of `|Im z| < 1/2`; so if `xi_lambda ~ k_lambda` then `det_reg -> Xi` and Hurwitz gives RH. "Step (ii) is the whole difficulty." The proposal is a separate module computing prolate spheroidal functions at high precision via the `PW_lambda` eigenproblem in a Legendre basis (tridiagonal, arb-certifiable), giving `1 - chi_n(lambda)` and `k_lambda = E(h_lambda)`.
- Lead: build it, then compare `xi_lambda` against `k_lambda` at the `x = 40..100` scales the benchmark already reaches. "This is the part that touches the missing proof." Even a rigorous numerical measurement of `||xi_lambda - k_lambda||` as a function of `lambda` would be new.
- Related: L09-004, L09-005, L09-021, L09-022, L09-041, L09-046, L09-083.

### L09-018 Caratheodory-Fejer as the degenerate case, and the window-accuracy question
- Source: notes/zeta-spectral-triples/plan.md:388-395
- Raised by: orchestrator (Claude)
- Status at last mention: pursued, positive (became `ihz`'s exact anchor)
- Content: on finite objects the discrete analogue of the whole construction is classical Caratheodory-Fejer for Toeplitz matrices: the window Weil form `sum_theta |f_hat(theta)|^2` over the retained divisor has a Toeplitz matrix of rank equal to the number of distinct retained points, so once the window exceeds that number the kernel vector's polynomial vanishes exactly on the divisor. Below that, one gets an approximation regime like the paper's, "on an object where the truth is known: the natural place to study how the accuracy depends on the window."
- Lead: this is the origin of the whole `ihz` MVP; the accuracy-vs-window study is L09-041.
- Related: L09-014, L09-039, L09-041, L09-052.

### L09-019 How the CCM positive form relates to the notebook's letter-derived metrics
- Source: notes/zeta-spectral-triples/plan.md:402-404; ihara/lanes/notebook-extract.md:350-391
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued
- Content: for each window the construction supplies a positive form `tau - eps_N` making a perturbed scaling operator self-adjoint. The question is how that form relates to the letter-derived metric `G_C = ((1, Sigma/2), (Sigma/2, q))` of `thm:hashimoto-lift-metric` (which satisfies `C^dagger G_C C = q G_C` and is positive definite exactly on the strict band `|a| < 2 sqrt q`) and to the `G` of `def:graded-rh-fe-ramanujan`'s (HP) clause. "a question the finite cases can settle."
- Lead: compute both forms on the same small graph at the critical window and compare them directly. If they agree up to a congruence, the CCM construction and the notebook's Hilbert-Polya metric are the same object, which would connect the sidequest to shard 03f.
- Related: L09-016, L09-076.

### L09-020 The odd block: is there a second operator nobody has looked at?
- Source: notes/zeta-spectral-triples/plan.md:462-463
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued; explicitly "Not in the paper"
- Content: the paper takes the minimal eigenvector of the even block and requires `eps_N < min spec O`. The question: "does the minimal eigenvector of the odd block give anything (an 'odd' operator with real spectrum by the same lemma, if `<eta|xi_odd>` can be replaced by a suitable functional)?"
- Lead: try it — compute the odd-block minimal eigenvector at the existing benchmark parameters and see whether its secular roots are near anything. Cheap, since both blocks are already built and certified. Note the graph side gives a reason to care: for a non-Ramanujan object the minimal eigenvector *is* odd and `<eta|xi> = 0` kills the standard normalisation (L09-042, L09-051).
- Related: L09-042, L09-047, L09-051.

### L09-021 The sign pattern and decay of the eigenvector coefficients
- Source: notes/zeta-spectral-triples/plan.md:460
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued
- Content: experiment 4 of the "first experiments once M2 exists" list: the sign pattern and decay of the `xi_j`, and their relation to the prolate Fourier coefficients. The sign changes are already known to matter operationally: they are why the secular function is not monotone between consecutive poles and why several roots can share a pole interval.
- Lead: plot/measure `xi_j` against the prolate coefficients of `k_lambda`; this is the cheapest possible probe of the missing step L09-017, since it needs only the eigenvector already computed.
- Related: L09-017, L09-025.

### L09-022 `det_reg` against `Xi` on a strip
- Source: notes/zeta-spectral-triples/plan.md:302-304, 375-377, 461
- Raised by: a paper (CCM Section 7), taken up by the orchestrator
- Status at last mention: raised, not pursued (M5)
- Content: evaluate `xi_hat(z)` on a grid of the strip, form `det_reg`, fit `e^{a + i b z}` on two points and report the sup-norm deviation from `acb_dirichlet_xi` on compact sets, as `lambda` grows, on `|Im z| <= 0.4`.
- Lead: this is the paper's own Section 7 experiment done with certified enclosures and at `x` far beyond theirs; a rigorous convergence rate for `det_reg -> Xi` would be new data on the missing proof.
- Related: L09-017.

### L09-023 The `(lambda, N, prec) -> accuracy` map as the tool's first job
- Source: notes/zeta-spectral-triples/plan.md:314-316, 456-457
- Raised by: orchestrator (Claude)
- Status at last mention: pursued, positive (the benchmark is this map)
- Content: starting rules of thumb proposed before the runs: `N ~ 10 lambda^2`, `d ~ 6 lambda^2`, meaningful roots are those with `s < N/2`. "the tool's first job is to map `(lambda, N, p) -> accuracy` properly."
- Lead: done for `zeta` (L09-004 to L09-006, which sharpened `N ~ 10x` to `N ~ 7.5x`); the same map for any other L-function is unmeasured.
- Related: L09-004, L09-005, L09-006.

### L09-024 Structured `O(N^2)` solvers, threading, and a Julia wrapper
- Source: notes/zeta-spectral-triples/plan.md:210-212, 265-267, 328-331, 372-374
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued
- Content: `tau` is a Loewner matrix with a rank-two displacement, so a GKO-type displacement-structured `O(N^2)` LU exists; "at high precision this is a real win for `N >= 10^3`". Also proposed: OpenMP over `n` in the build and over columns in the factorisation, `flint_set_num_threads` for `arb_mat_mul_threaded`, and "Optional thin Julia `ccall` wrapper later".
- Lead: this gates L09-008 and the Selberg case L09-015, both of which need `N` in the thousands; currently the `O(N^3)` factorisation plus certificate dominates and runs single-threaded.
- Related: L09-008, L09-015, L09-030.

### L09-025 The symmetric fallback for near-double secular roots
- Source: notes/zeta-spectral-triples/plan.md:292-295, 469-471
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued (the implemented code used a different route)
- Content: when two roots nearly coincide, the proposed fallback is the symmetric form of `D''`, `M = R^{-T} W^T (tau - eps) D' W R^{-1}` with `W` an orthonormal basis of `xi^perp` and `G = W^T (tau - eps) W = R^T R`, whose eigenvalues are the roots, certified by approximate diagonalisation plus Gershgorin. "The prototype missed 2 to 4 of the 120 roots with a naive grid; the C code must not."
- Lead: the shipped code instead used QR candidates, then a sign scan, with completeness by count (L09-027); the symmetric fallback remains unbuilt and would be the honest route if a genuine double root ever appears (which is exactly what a failure of simplicity of the zeta zeros would look like).
- Related: L09-027, L09-065.

### L09-026 Interval `LDL^T` inertia cannot certify at these condition numbers
- Source: notes/zeta-spectral-triples/benchmark.md:66-71; report-2026-09-18.md:46-49
- Raised by: orchestrator (Claude), from the benchmark failure
- Status at last mention: pursued, negative for the original route; replaced
- Content: the interval-`LDL^T` inertia certificate failed from `x = 20` on because input radii are amplified by the squared condition number (`1e192`). Replaced by verified positive definiteness of the deflated matrix `E - 2 eps + c v v^T` and of `O - 2 eps` by approximate Cholesky plus a ball residual (Rump's isspd), whose amplification is only linear. A `2x2` test exposed that the deflation constant must exceed `s - eps`.
- Lead: do not re-attempt ball `LDL^T` inertia at scale. Note the code audit proposes a third route that would sidestep both: exact rational inertia (L09-068).
- Related: L09-068.

### L09-027 The sign scan and the roots that live far beyond the last pole
- Source: notes/zeta-spectral-triples/benchmark.md:28-30, 72-77; zst/README.md:41-43; report-2026-09-18.md:49-52
- Raised by: orchestrator (Claude)
- Status at last mention: pursued, positive
- Content: the QR candidate generator dominated runtime (612 of 673 s at `x = 40`) and its precision cannot be reduced below the dynamic range of the rank-one term (about `5.5 x` digits, because the normalisation `sum xi_j = 1` divides by the eigenfunction's value at the window edge, which is `e^{-pi lambda^2}` small). Replaced by a sign scan with bisection per pole interval plus a geometric grid beyond the last pole: "the tail roots cluster just past N: 400.34, 406.74, 427.4, ... at N = 400, and reach 31 N". Completeness must therefore be by count, never by a search range.
- Lead: the tail roots themselves are an unexplained structure (they come in pairs, reach `31 N`) and nobody asked what they are. If they have a closed form, the completeness argument becomes cheap.
- Related: L09-006, L09-025, L09-028.

### L09-028 Deciding rigorously whether two overlapping balls are one root or two
- Source: notes/zeta-spectral-triples/benchmark.md:78-80
- Raised by: orchestrator (Claude)
- Status at last mention: pursued, positive
- Content: overlapping certified balls (duplicate candidates) used to discard the whole list; now a Newton step on the hull of the pair decides rigorously whether it is one root or two.
- Lead: this is exactly the primitive needed if a double zero of zeta ever appeared in a window; it is the only part of the pipeline that could in principle detect one.
- Related: L09-025.

### L09-029 A mean-value form is mandatory for the far-out roots
- Source: notes/zeta-spectral-triples/report-2026-09-18.md:50-52
- Raised by: orchestrator (Claude)
- Status at last mention: pursued, positive
- Content: "any plain interval evaluation of the secular function's derivative is useless for the far-out roots, where a mean-value form is required."
- Lead: none stated; recorded so the lesson is not relearned.
- Related: L09-027.

### L09-030 Memory as the binding constraint at `N ~ 10^3`
- Source: notes/zeta-spectral-triples/report-2026-09-18.md:52-53; benchmark.md:32-34
- Raised by: orchestrator (Claude)
- Status at last mention: partially resolved (5.1 GB -> 2.4 GB at `N = 800` via an `O(N^2)` Krawczyk step); `x = 100` still unfinished
- Content: peak memory at `N = 800` was cut from 5.1 GB to 2.4 GB by making the Krawczyk step `O(N^2)`; `x = 100` (`N = 1000`, 4000 bits) was OOM-killed at 10.7 GB before the rework.
- Lead: gates L09-008 and L09-015; a further `O(N^2)` pass over the factorisation (L09-024) is the obvious next step.
- Related: L09-008, L09-024.

### L09-031 Known test debt in `secular.c`: two out-of-bounds reads that escape ASan
- Source: zst/README.md:61-64
- Raised by: orchestrator (Claude), from mutation testing
- Status at last mention: recorded as known debt, not fixed
- Content: after two mutation batches (27/30, 35/40, 29/40 killed), the surviving mutants were all inspected; all but two are equivalent mutants or absorbed by Newton polishing. The two real survivors are "out-of-bounds reads in the sort and disjointness loops of `secular.c` that happen inside uninstrumented FLINT calls and so escape ASan."
- Lead: gates trust in the root list, which is what every certified table rests on; worth closing before any result is published.
- Related: L09-027, L09-066.

### L09-032 Replace the hand-rolled positive-definiteness certificate with `arb_mat_spd_solve`
- Source: ihara/lanes/code-audit.md:112-126
- Raised by: orchestrator lane (Sonnet, code audit)
- Status at last mention: raised, not pursued ("worth a follow-up ticket", out of scope for the audit)
- Content: `zst_eigmin`'s `verify_pd` hand-rolls an approximate Cholesky plus ball residual; `arb_mat_cho`, `arb_mat_ldl` and `arb_mat_spd_solve` are all present, certified on the first try at `prec = 200`, and `spd_solve` is "a public, presumably better-tested equivalent of the same Rump-style certificate". Candidate simplification "for **both** verticals".
- Lead: gates nothing mathematical but reduces the surface where a hand-rolled certificate could be wrong; the even-simple certificate is the one step that makes a run a theorem.
- Related: L09-026, L09-068.

### L09-033 A shared core, and spinning the libraries out as standalone repos
- Source: notes/zeta-spectral-triples/plan.md:346-352; ihara/plan.md:296-303; code-audit.md:356-364
- Raised by: orchestrator (Claude)
- Status at last mention: deliberately deferred ("a follow-up once both verticals are stable, not a precondition")
- Content: `eigmin.c` is copied verbatim from `zst/` into `ihz/` (renamed prefix) rather than shared; the plan also proposes `zst/` as a standalone repo (AGPL-3.0 like the notebook) with `docs/formulas.md` kept in lockstep with the code and `proto/ccm_proto.py` kept and never optimised.
- Lead: extract `libzcore` once both verticals are stable; until then the duplicated `eigmin.c` must stay in the mutation-testing set to catch copy errors (ihara/plan.md:385-386).
- Related: L09-031, L09-088.

### L09-034 What MVP-2 is for: five things a graph can do that zeta cannot
- Source: ihara/plan.md:65-71, 268-294
- Raised by: orchestrator (Claude), synthesising the five lanes
- Status at last mention: pursued, partially delivered (G1-G3 done; G4 experiments only partly run)
- Content: the stated value of `ihz/` is (i) a certified exact anchor for the whole `zst` pipeline on an object where truth is known, (ii) the under-resolved accuracy law as a function of window size and angular separation, (iii) the non-Ramanujan experiment, (iv) the irregular-graph case as the cheapest example of Weil positivity without duality, and (v) the graded/curve sign as the bridge to `def:graded-transfer-channel`. Estimated at about 1400 lines and two weeks at the house standard.
- Lead: items (ii), (iii) and (iv) are the unfinished experiments — see L09-041, L09-048, L09-060.
- Related: L09-041, L09-048, L09-058, L09-060.

### L09-035 `IH-11`, the unitary key lemma: a new three-line theorem
- Source: ihara/lanes/theory.md:297-346; ihara/plan.md:29-33, 129-136
- Raised by: Opus theory lane
- Status at last mention: PROVED, "new; not in CS"; implemented and certified in `ihz/src/unitary.c`
- Content: for `T` Hermitian PSD Toeplitz with one-dimensional kernel `C xi`, normalise `xi_0 = 1` and set `U = Z^*(1 - |xi><eta|) = Z^* - |Z^* xi><eta|`. Then `U xi = 0`, `U^* T U = T` **exactly** (proof: `(1-P^*) T (1-P) = T` for `P = |xi><eta|`, and the displacement `|eta><g| + |g><eta|` is killed because `(1-P^*) eta = 0` and `<eta|(1-P) = 0`), so `U''` on `E/C xi` is unitary, with `det(U'' - w) = (-1)^{K+1} sum_k xi_k w^{K-1-k}`. It needs neither evenness of `xi` nor a simple-spectrum `D`.
- Lead: "it, not `corcar`, is what has to be carried to the graded case and to the Selberg case, where the object of interest is an operator and not a polynomial" (theory.md:418-423). Concrete next step: generalise it to a `CS`-type statement with arbitrary `eta` (L09-047), and try it on a Krein form for mixed divisors (L09-045).
- Related: L09-038, L09-045, L09-047, L09-062.

### L09-036 `IH-13`: the graph case is literally an instance of `CS` Proposition `finmain`
- Source: ihara/lanes/theory.md:369-393; ihara/plan.md:137-141, 152-156
- Raised by: Opus theory lane
- Status at last mention: PROVED; implemented as a one-off certificate
- Content: for odd `K`, with `lambda_n = tan(pi n/K)` and the real congruence `C = diag(sqrt(2K) cos(pi n/K))`, the DFT'd Toeplitz form becomes `Q_{nm} = (b_n - b_m)/(lambda_n - lambda_m)`, `Q_{nn} = a_n` — literally `CS`'s equation `form2` at `CS:1128`, with the parity hypotheses of `basics-general` satisfied. So `CS:1356` applies verbatim, not by analogy. Costs: `K` must be odd; the congruence is non-unitary so the `eps`-shift must be done in the Toeplitz picture first; and it trades a natural unitary for an artificial self-adjoint.
- Lead: compute it once as certification that the graph case is an instance, then use the unitary route for everything else. If the Selberg/graded cases have a Cayley analogue, the same congruence trick would carry `CS` there too.
- Related: L09-035, L09-038, L09-047.

### L09-037 Read `eta` off the displacement, never posit it
- Source: ihara/plan.md:143-150; ihara/lanes/numerics.md:18-22, 210-215, 222-231, 281-293, 330-337
- Raised by: Opus numerics lane and Opus theory lane independently ("both lanes hit it independently")
- Status at last mention: pursued, settled; a hard rule for the implementation
- Content: the second displacement vector is not free. In the position basis `eta` is the delta at the window edge; in the DFT basis, all-ones up to `K^{1/2}` and the phase `z_n^{-M}`; in the un-congruenced Cayley picture it is `eta_n = (-1)^n sec(pi n/K)`. The prototype measures the distance of a candidate `eta` to `span(beta, eta)`: all-ones sits at distance `0.82-0.98` while `(-1)^n sec(pi n/K)` sits at `<= 4e-16`. Getting it wrong "costs an `O(1)` error in the recovered angles at a window where the answer is otherwise exact" (angle errors 0.4 to 0.5 where the truth is exact).
- Lead: the rule is stated as "read `eta` off the displacement `Z T Z^* - T`, never posit it"; the generalisation of this observation is `Q-8` (L09-047).
- Related: L09-047, L09-089.

### L09-038 Which backbone: `corcar` in the position basis, with the operator as a cross-check
- Source: ihara/lanes/theory.md:395-425; ihara/plan.md:152-156
- Raised by: Opus theory lane
- Status at last mention: decided and implemented
- Content: four reasons to make `CS` Corollary `corcar` the backbone: a complete published proof needing only "PSD Toeplitz of rank `K-1`"; the perturbed operator adds nothing to the zero set (`spec(U'') = roots(Ptilde)` exactly); Caratheodory-Fejer gives more — the weights, hence multiplicities, and the exact description of the over-resolved failure; and it is `O(K^2)` (Levinson/Prony) rather than `O(K^3)`.
- Lead: keep the unitary operator as a certified cross-check because it is what carries to the graded and Selberg cases; compute the Cayley form once as the `CS:1356` certificate.
- Related: L09-035, L09-036, L09-056.

### L09-039 The three regimes and the critical window `K = R + 1`
- Source: ihara/lanes/theory.md:485-502; ihara/plan.md:168-181; numerics.md:100-117
- Raised by: Opus theory lane and Opus numerics lane (independently)
- Status at last mention: PROVED and verified; the exact anchor of `ihz/`
- Content: with `R` the number of distinct retained points, under-resolved (`K <= R`) gives `eps_M > 0` and `K-1` circle points that are a Pisarenko approximation, not the divisor; critical (`K = R+1`) gives `eps_M = 0`, a one-dimensional kernel and exactly the `R` divisor points; over-resolved (`K > R+1`) gives a kernel of dimension `K-R >= 2`, so even-simplicity fails and only the intersection of the zero sets over `ker T` is the divisor. Verified on Petersen (`R = 4`): `eps_M = 15.88, 9.45, 5.71, 0, 0, 0, 0` for `K = 2..8`, kernel dimensions `1,1,1,1,2,3,4`.
- Lead: this is why a graph cannot exercise CCM's missing step (L09-087, `NG-3`), and it is what makes the graph an exact anchor. The transferable question is the under-resolved law (L09-041).
- Related: L09-018, L09-040, L09-041, L09-052, L09-087.

### L09-040 `Q-1`: is there a canonical `xi` in the over-resolved regime?
- Source: ihara/lanes/theory.md:536-557, 1002-1006; ihara/plan.md:180-181, 459
- Raised by: Opus theory lane
- Status at last mention: OPEN, "Not settled"
- Content: when `d = K-1-R >= 1` the kernel vector's polynomial has the `R` true roots plus `d` arbitrary ones. A family that keeps the circle exists: `Ptilde = q_0(w)(w^d - beta)` with `|beta| = 1` — exactly the paraorthogonal completions, a one-parameter family, none canonical. The minimal-degree choice puts the extra roots at `0` (breaks the circle); the minimum-norm/Levinson choice puts them strictly inside the disc (breaks the circle). Nothing in the CCM/CS chain picks a `beta`.
- Lead: the untested mechanism is named: perturb `T -> T + delta * (|eta><eta|` or the boundary rank-two term`)` and let `delta -> 0+`; does the kernel vector converge to a paraorthogonal one, and with which `beta`? Cheap to test in the existing prototype. If a canonical `beta` emerged, the over-resolved regime would stop being a failure mode.
- Related: L09-039, L09-053.

### L09-041 `Q-2`: the under-resolved law — the one quantitative question a graph can transfer
- Source: ihara/lanes/theory.md:1008-1014; ihara/plan.md:276-279, 459-461; numerics.md:100-105, 380-384
- Raised by: Opus theory lane and Opus numerics lane
- Status at last mention: OPEN; "I have neither derived nor tested this"
- Content: in the under-resolved regime `eps_M > 0` is the Pisarenko noise floor of an exact `R`-atom measure observed with too few lags. The guess, stated but untested: it is governed by the minimal angular separation `delta_min` of the `R` divisor points against the Fejer resolution `2 pi/K`, roughly `eps_M ~ c (K delta_min)^{2(R-K+1)}`. Measured accuracy falls roughly geometrically in `M` (necklace3: angle errors `1.32, 0.57, 0.26` at `K = 3, 5, 7`; Pappus `0.66, 0.52`; Petersen `0.61` at `K = 3`). The numerics lane adds that the minimiser is the degree-`2M` polynomial of unit coefficient norm minimising `sum_mu |xi_hat(mu/critr)|^2 `, i.e. **a discrete prolate/Slepian problem**.
- Lead: fit the law on the graph families (`ihz --scan` already prints the data) and then ask the decisive question: "Is `1 - chi_4(lambda)` (CCM §7) the continuous limit of this rate?" If yes, the graph gives a computable handle on the constant that governs the zeta accuracy (L09-004).
- Related: L09-004, L09-005, L09-018, L09-039, L09-083.

### L09-042 `Q-3`: anti-palindromic minimal eigenvectors, and whether `even-simple` *is* the graph RH
- Source: ihara/lanes/theory.md:1016-1020; ihara/plan.md:290-291, 461-463; numerics.md:26-29, 156-159, 367-370
- Raised by: Opus theory lane and Opus numerics lane (the numerics lane sharpened it)
- Status at last mention: OPEN; a cheap search was proposed and not run
- Content: `CS:865` proves the kernel vector of a one-dimensional kernel is palindromic *or* anti-palindromic; CCM's `even-simple` asserts the `+` sign and lists it among the missing steps. Petersen gives `+` at `K = 4,5`. The numerics lane found the mechanism: an off-circle reciprocal pair `{x, 1/x}` contributes `2 f_hat(x) f_hat(1/x)`, which is `>= 0` on even `f` and `<= 0` on odd `f`, so for a non-Ramanujan regular graph the EVEN block stays PSD at every window while the ODD block carries the negative eigenvalue, `xi_min` becomes odd, `<eta|xi_min> = 0`, and `even-simple` fails. Sharpened question: "is `even-simple` for every window EQUIVALENT to Ramanujan, or only implied by its failure?"
- Lead: "A search over small regular graphs and window sizes for a `-` case would settle whether 'even' is a theorem or a hypothesis over `Z`, and would be cheap." If the equivalence holds, then "CCM's hypothesis is not an auxiliary technical assumption but a restatement of the target" — which would change how the whole CCM programme should be read.
- Related: L09-020, L09-048, L09-050, L09-051.

### L09-043 `IH-28` / `Q-4`: what the returned points do when RH fails
- Source: ihara/lanes/theory.md:743-760, 973-975, 1022-1023; ihara/plan.md:189-190, 463
- Raised by: Opus theory lane
- Status at last mention: CLAIMED at leading order; the exact limit OPEN
- Content: in the non-Ramanujan regime the minimal eigenvector is asymptotically `xi ~ u/||u|| - v/||v||` (two geometric profiles of ratio `1/rho` anchored at the window ends), so `Ptilde(w) ~ 1/(1 - w/rho) - w^{K-1}` on the circle, forcing the roots toward equidistribution with an `O(1/K)` phase modulation and no divisor information. Partially verified: prism at `M = 21`, 41 gaps, mean `0.148627` against `2 pi/(K-1) = 0.149600`, sd `0.012038` (8% of the mean) — approaching but not converged.
- Lead: "Push to `M = 40` in extended precision and report whether the sd decays" (theory.md:973-975). The exact weak-* limit (predicted: normalised Lebesgue with an `O(1/K)` modulation) is unproved.
- Related: L09-048, L09-050, L09-063.

### L09-044 `Q-5`: a principled trivial divisor for an irregular graph
- Source: ihara/lanes/theory.md:800-803, 1025-1028; numerics.md:161-166, 389-393; ihara/plan.md:463-465
- Raised by: Opus theory lane and Opus numerics lane
- Status at last mention: OPEN
- Content: for an irregular graph the Perron pole `mu = 1/R_G` survives but its designated partner `1` does not (`1` is generally not an eigenvalue of `B`), so `W_{0,2}` drops to rank one and the trivial divisor loses its "`H^0` partner of `q`". The prototype's naive Stark-Terras choice (`{rho(B), 1}` plus `+-1` with multiplicity `|E|-|V|`, `critr = sqrt(rho(B))`) leaves a retained divisor that is neither reciprocal- nor circle-closed.
- Lead: two candidate fixes are named and untested — "weighting by a Perron eigenvector, or passing to the universal cover's spectral radius". Related to `obs:divisor-regular-data` cited at `02h:154`. If one restored a functional equation, the irregular case would stop being structurally hopeless (L09-060).
- Related: L09-060, L09-075.

### L09-045 `Q-6`: a Krein-space key lemma for mixed-parity divisors
- Source: ihara/lanes/theory.md:862-871, 1030-1033; ihara/plan.md:219-221, 465-466
- Raised by: Opus theory lane
- Status at last mention: OPEN, "Not settled"
- Content: a graded transfer channel may retain both poles (`nu > 0`) and zeros (`nu < 0`); then `QW_M(f,f) = sum nu_ret(lambda)|f_hat|^2` is indefinite **by construction**, independently of RH, so `eps_M` is not a noise floor and the returned circle spectrum has no interpretation. The signature `(p, n)` is known (retained poles, retained zeros), so a `J`-unitary version of `U''` exists formally.
- Lead: "whether its spectrum localises anywhere useful is open." This is the obstacle to running the construction on `prop:qubit-graded-zeta`'s graded quantum Ihara zeta with both sectors retained; the workaround used instead is to put one sector into the trivial divisor.
- Related: L09-035, L09-058, L09-059.

### L09-046 `Q-7`: is there any `Z`-side analogue of the prolate tower?
- Source: ihara/lanes/theory.md:659-669, 1035-1040; ihara/plan.md:257-259, 403-405, 466-467
- Raised by: Opus theory lane; flagged by the lane as "the real one"
- Status at last mention: OPEN for infinite objects, NO for finite graphs; "I did not investigate it"
- Content: CCM's route to a proof rests on a theta function, a Gaussian self-dual under the Fourier transform, a prolate deformation of the harmonic oscillator, a Meixner-Schafke estimate and Fuchs asymptotics. None of this has a counterpart over `Z`: "There is no theta function on `Z`, no Gaussian fixed by the Fourier transform of `(Z, T)` adapted to a window, no self-dual prolate deformation", and a graph's completed zeta is a polynomial with known roots. "The step whose absence blocks CCM's proof of RH is exactly the step the graph MVP **cannot test at all**."
- Lead: "The only place a discrete model could touch the missing step is an infinite object (a tree quotient, the Selberg zeta)". Concretely: milestone G5 names "the Selberg compact case as the first infinite object where `Q-7` can be asked", and the literature lane points at Slepian's discrete prolate spheroidal sequences as the candidate object (L09-083).
- Related: L09-015, L09-017, L09-083, L09-087.

### L09-047 `Q-8`: a key lemma with a general `eta`, covering zeta and graphs at once
- Source: ihara/plan.md:467-470; ihara/lanes/numerics.md:371-379
- Raised by: Opus numerics lane
- Status at last mention: OPEN; verified numerically in that generality, no clean statement written
- Content: the question is whether `CS`'s Lemma `key-general` holds with `|beta><eta| - |eta><beta|` for an **arbitrary** displacement pair rather than `eta = sum_i e_i`. "The prototype verifies (i), (ii) and (iii) in that generality for every window with `gamma xi = xi`; a clean statement would cover both the zeta and the graph case at once." A second half: the multiplicative (unitary) key lemma needs no parity at all, while the additive one needs `gamma xi = xi` twice over — "Is the parity hypothesis in CCM avoidable by working with a unitary `U'` and a Cayley transform at the end?"
- Lead: write and prove the general-`eta` lemma. If the parity hypothesis is avoidable, one of CCM's two explicitly listed missing steps (`CCM:1385`) disappears. This is the single most promising theorem-shaped item in the lane.
- Related: L09-012, L09-035, L09-037, L09-042.

### L09-048 `IH-27`: the failure of RH is readable off the growth rate of the noise floor
- Source: ihara/lanes/theory.md:720-741, 966-978; ihara/plan.md:185-192, 280-284
- Raised by: Opus theory lane
- Status at last mention: PROVED (the law); the inverse problem raised, not run
- Content: with a retained real pair `{rho, 1/rho}` of multiplicity `m`, `eps_M = -m rho^{K+1}/(rho^2-1)(1+o(1))`, so `d log(-eps_M)/dM -> 2 log rho`. Verified on the prism `C_16 x K_2` (`rho = 1.123952`, predicted `-1299` vs observed `-1351` at `M = 21`, successive ratio `1.2826` vs `rho^2 = 1.263268`) and on two disjoint `K_4` (`rho = sqrt 2`, ratios `2.87, 2.80, 2.46, 2.10, 2.16 -> 2`). The trivial-divisor bookkeeping is load-bearing: forgetting the bipartite pair `{-q,-1}` makes the law report `2 log sqrt q` instead.
- Lead: the untried experiment is stated as check 23: "**Inverse problem:** from the slope of `log(-eps_M)` alone, recover the largest adjacency eigenvalue `lambda = sqrt q (rho + 1/rho)` and compare with the true `2 cos(pi/8) + 1 = 2.847759`. If this works it is a genuinely new diagnostic."
- Related: L09-034, L09-043, L09-061, L09-063.

### L09-049 `IH-26`: the construction never breaks, which means reality carries no information
- Source: ihara/lanes/theory.md:711-718; numerics.md:338-341
- Raised by: Opus theory lane and Opus numerics lane
- Status at last mention: PROVED
- Content: for every `M`, `T - eps_M I >= 0` is Toeplitz (with `eps_M < 0` once indefinite, so the shift adds to the diagonal), so the chain returns `K-1` points on the unit circle regardless. Verified on the prism for `M = 1..21` with `max ||root| - 1| < 4e-15` deep in the indefinite regime. The numerics lane's sharpest version: for the irregular dumbbell the construction returns `2M` circle points at every window "although nothing in the true divisor is within `0.13` of the circle".
- Lead: none stated; it is the reason why "RH is nowhere in the reality half of the CCM chain", which is L09-050.
- Related: L09-050, L09-051, L09-060.

### L09-050 `IH-29`: the chain is a spectral realisation of Weil's criterion, not a route around it
- Source: ihara/lanes/theory.md:762-774; ihara/plan.md:53-56
- Raised by: Opus theory lane
- Status at last mention: CLAIMED; the lane's headline structural reading
- Content: RH enters the CCM chain in exactly one place. Not the reality of the spectrum (unconditional), not the existence of `eps_M` and `xi` (unconditional), but "**In the identification of the limit.**" The returned measure is the Caratheodory measure of `T - eps_M I`; it converges to the true divisor measure iff `eps_M -> 0`, which is Weil's criterion. "**the CCM chain proves reality unconditionally and reduces RH to the vanishing of the noise floor, which is Weil's criterion restored verbatim.** It is not a new route to RH; it is a spectral realisation of the old one."
- Lead: this is the sentence the report to TJO must carry; it also tells you where to spend effort — everything except the limit identification is free.
- Related: L09-007, L09-042, L09-049, L09-052, L09-087.

### L09-051 Reality is free: 200 random Toeplitz matrices with no divisor behind them
- Source: ihara/lanes/numerics.md:23-25, 245-255, 338-341; ihara/plan.md:207-209
- Raised by: Opus numerics lane
- Status at last mention: pursued, positive (verified; a negative result for the importance of the reality theorem)
- Content: the isometry proof needs only `tau_q xi = 0` and shift invariance of the bilinear form — two lines, independent of positivity and of the functional equation. So `T - eps_min` is PSD Toeplitz with a kernel for ANY Hermitian Toeplitz `T`, and all `2M` roots lie on the circle. Verified on 200 random real even Toeplitz matrices (`max ||root| - 1| = 6.1e-13` in double). "The whole content of the chain is positivity, i.e. `thm:weil-positivity-finite`."
- Lead: none stated; the consequence is that effort should go to positivity, not reality.
- Related: L09-049, L09-050, L09-052, L09-090.

### L09-052 `IH-24`: CCM's `eps_N` is Pisarenko's noise floor
- Source: ihara/lanes/theory.md:591-604; ihara/plan.md:33-35
- Raised by: Opus theory lane
- Status at last mention: PROVED (identification)
- Content: Pisarenko's 1973 harmonic decomposition is exactly the construction of `IH-18` under the dictionary `eps_M <-> noise floor sigma^2`, divisor `<->` harmonic frequencies, critical window `K = R+1` `<->` Pisarenko's exact-order case. "**CCM's `eps_N` is a noise floor, and the CCM chain on a finite divisor is Pisarenko.**" The `(lambda, N)`-accuracy study is, in the graph case, the classical under-resolved (order-underestimated) Pisarenko problem.
- Lead: the signal-processing literature on order-underestimated Pisarenko is then directly relevant to `Q-2` (L09-041) and possibly to the zeta accuracy law; nobody looked.
- Related: L09-018, L09-039, L09-041, L09-053.

### L09-053 `IH-25`: `U''` is a CMV/paraorthogonal object
- Source: ihara/lanes/theory.md:606-613; literature.md:317-384
- Raised by: Opus theory lane; literature lane supplied the verified source (Simon, math/0606037)
- Status at last mention: PROVED (identification)
- Content: `U''` is a rank-one perturbation of the shift, unitary for the `T`-inner product, with self-reciprocal characteristic polynomial when `xi` is even — that is the definition of a paraorthogonal polynomial, and the corresponding matrices are the truncated GGT/CMV matrices. `IH-21(a)`'s free unimodular parameter `beta` is exactly the paraorthogonal parameter. Simon's paper proves the statement matrix-first using rank-one perturbations of unitaries.
- Lead: the OPUC toolkit (Verblunsky coefficients, Szego recursion, the CMV five-diagonal form) is then available for the graph case and, via the unitary key lemma, potentially for the Selberg case; nobody has tried to use it. Simon's `math/0606037` and Cantero-Moral-Velazquez `math/0204300` are both already fetched.
- Related: L09-035, L09-040, L09-085.

### L09-054 `IH-5`: is `(1-u^2)^{r-1}` the graph's gamma factor?
- Source: ihara/lanes/theory.md:137-159; ihara/plan.md:103-105; literature.md:136-144, 720-721
- Raised by: Opus theory lane; challenged by the Sonnet literature lane
- Status at last mention: CLAIMED (one identity plus three interpretations); the naming is UNVERIFIED and appears to be the notebook's own
- Content: the identity is proved — `W_R` is exactly the log-derivative contribution of the `(1-u^2)^{|E|-|V|}` factor, and that factor is exactly what produces a clean functional equation, while neither `Z_G` nor `det(1-uB)` satisfies one. Three interpretive reasons follow: the atoms are a geometric series `c s^{|k|}` with `s = q^{-1/2}`, the discrete counterpart of `rho(x) = sum e^{-(2n+1/2)x}` with the same leading exponent `1/2` and the ladder truncated to one rung; the multiplicity `-chi(X)` is topological; and it sits strictly inside the critical circle, contributing an unboundedly positive rank-2 piece. The literature lane searched Horton-Stark-Terras, Stark-Terras III and Terras-Wallace in full and found **no such "gamma factor" framing in any of the three**.
- Lead: "*What is missing:* a statement identifying `(1-u^2)^{r-1}` with an archimedean local factor in a motivic sense." If made precise, this would give the graph an honest archimedean place and would tell the `zst_weil_t` data model what the discrete instance of the kernel family really is.
- Related: L09-001, L09-055, L09-085.

### L09-055 There is no Weil-style explicit formula for graphs in the literature — `IH-3` supplies one
- Source: ihara/lanes/literature.md:145-149, 618-622, 721-724; ihara/lanes/theory.md:90-117, 650-654
- Raised by: Sonnet literature lane (the negative finding) and Opus theory lane (the positive statement)
- Status at last mention: NOT FOUND in the primary sources read; the graph identity is PROVED here
- Content: the graph literature has a prime number theorem (Horton-Stark-Terras Thm 2.10, via Mobius inversion) and a pole-location "RH", but no explicit formula with general test-function pairs `h, g_hat`. Meanwhile `IH-3` writes exactly such a formula, `Psi_X(F) = W_C(F) - W_{0,2}(F) - W_R(F)`, with the three pieces in CCM's own shape — though "This is a finite rearrangement of `Tr B^k`, not an analytic theorem" (`NG-5`).
- Lead: `IH-3` is small and complete; if the "gamma factor" reading (L09-054) can be made structural, the combination is a publishable "explicit formula for the Ihara zeta in Weil's shape", which the lane's own search says does not exist. Also unfound: any paper on "spectral reconstruction from closed walks" (literature.md:635-648) — the fact is definitional, not a theorem to attribute.
- Related: L09-054, L09-085.

### L09-056 `IH-20`: the method is blind to multiplicity; Prony restores it
- Source: ihara/lanes/theory.md:517-534; ihara/plan.md:176-179
- Raised by: Opus theory lane
- Status at last mention: PROVED; Prony implemented and certified (Petersen weights `(5,5,4,4)`)
- Content: `Ptilde` depends on the Caratheodory measure only through its support, so the construction returns the divisor's support and never its multiplicities. At the critical window the weights solve an `(R+1) x R` Vandermonde system with full column rank, so `alpha_j = m(w_j)` uniquely. Petersen has 18 retained points but only 4 distinct ones, multiplicities `5,5,4,4`.
- Lead: "It is a structural limitation of the method, of a piece with `prop:weil-blind-jordan`: Weil positivity sees the divisor as a set of moduli, not as a module." For zeta the zeros are believed simple so CCM never meets this — but if a zeta zero were multiple, the construction would not see it, which is worth stating.
- Related: L09-028, L09-076.

### L09-057 The critical window is detectable blind
- Source: ihara/lanes/theory.md:550-553, 962-963; ihara/plan.md:179-180
- Raised by: Opus theory lane
- Status at last mention: CLAIMED (`IH-21(d)`); implemented in `ihz/src/rank.c` as exact rank over `Q`
- Content: "The right fix is not a choice of `xi` but a choice of window: run at `K = R+1`. `R` is observable without knowing the answer, as the rank of `T` stabilises (`rank T = R` for all `K > R`), so the algorithm can find the critical window by increasing `K` until the rank stops growing, then step back one."
- Lead: the detector must be exact (rank over `Q`), not a ball heuristic — flagged as a risk. This is what makes `ihz --scan` able to find the anchor without being told the answer.
- Related: L09-039, L09-040, L09-068.

### L09-058 `IH-36`: mixed-parity divisors break the chain, and the code must refuse them
- Source: ihara/lanes/theory.md:862-871; ihara/plan.md:219-221, 288-289, 453-454
- Raised by: Opus theory lane
- Status at last mention: CLAIMED; the refusal test was planned (G4) but the `ihz` README does not record it as run
- Content: "**The CCM chain requires the retained divisor to be of a single parity.**" `zeta` (all zeros), an ungraded graph (all poles) and a curve (all zeros) each satisfy this; `prop:qubit-graded-zeta`'s graded quantum Ihara zeta has both a nontrivial numerator and denominator and therefore does not, unless one sector is put into the trivial divisor.
- Lead: implement the refusal as a test (the sign convention "is the single most likely silent error"); then ask `Q-6` (L09-045) whether a Krein-space version says anything.
- Related: L09-045, L09-059, L09-075.

### L09-059 `IH-33`/`IH-34`/`IH-35`: the curve gives CCM's sign back, and it is already in the literature
- Source: ihara/lanes/theory.md:830-860; ihara/plan.md:216-221, 287-289; numerics.md:184-194
- Raised by: Opus theory lane; prior art flagged by the same lane and by the literature lane
- Status at last mention: PROVED; run on the elliptic curve over `F_5` in `ihz` (angles `+-2.034443936` recovered exactly at `M = 1`)
- Content: for a curve, `t_k = q^{-k/2} N_k - (q^{k/2} + q^{-k/2})` has CCM's sign exactly and no `W_R`; nothing in the linear algebra changes, "The only thing that changes is the sign bookkeeping of `def:graded-transfer-channel`" — one global sign chosen once per object. But Hallouin-Perret (TAMS 2019), cited at `CS:800` and `CS:2103`, already derive upper bounds for `#C(F_q)` from precisely this semidefinite symmetric Toeplitz matrix. "**the graded (curve) instance of MVP-2 is not new mathematics**; it is a re-derivation."
- Lead: use it as a certified anchor and as the bridge to `def:graded-transfer-channel`, not as a result; and read Hallouin-Perret in full (L09-082) before claiming anything about curves.
- Related: L09-016, L09-058, L09-079, L09-082.

### L09-060 Irregular graphs: Weil positivity without duality, and a structural impossibility
- Source: ihara/lanes/theory.md:787-824; ihara/plan.md:211-215, 285-286; numerics.md:161-182; ihz/README.md:46-48
- Raised by: Opus theory lane and Opus numerics lane
- Status at last mention: PROVED (what survives, what is modified, what fails); the prototype covers it, `ihz/` does not
- Content: everything using only "Hermitian Toeplitz" survives, but `A_ret` is not invariant under `mu -> R_G^{-1}/mu`, so there is no functional equation; `thm:weil-duality-pairing` does not apply and positivity gives only the **one-sided** Stark-Terras bound, which is Stark-Terras RH in its correct one-sided form. The interpretation then fails even when the output exists: "the construction is structurally incapable of returning an irregular graph's divisor". The dumbbell is the cleanest negative control: `eps_M` changes sign at `M = 4` and `pt.err` saturates at about `0.20`. The triangle-with-a-pendant-path shows the pendant is invisible and the retained divisor contains `mu = 0`, so the reflection is not even defined.
- Lead: "An irregular graph is the cheapest available example inside the notebook of an object with Weil positivity but no duality — the exact situation of `prop:kraus-no-duality-example`." The data model must carry `critr` as a free parameter and a flag for whether the functional equation is asserted. The sharp open question: "is there a sharp statement of the form 'the construction converges iff the retained divisor is reciprocal-closed', i.e. is the functional equation a *necessary* input?"
- Related: L09-044, L09-049, L09-075.

### L09-061 Two disjoint `K_4`: the minimal fully controlled non-Ramanujan test
- Source: ihara/lanes/numerics.md:124-127, 136-139, 355-358; ihara/plan.md:283-284, 377-379
- Raised by: Opus numerics lane, as a "surprise"
- Status at last mention: pursued, positive; recommended as a permanent unit test
- Content: "for a disconnected regular graph the second Perron eigenvalue is retained and produces an off-circle reciprocal pair `{sqrt q, 1/sqrt q}` at angle `0`" — so two disjoint `K_4` give `R = 4`, `rho = sqrt 2`, critical `K = 5`, `eps_M = -2.673, -7.679, -21.48, -52.78, -111.06, -240.05` at `M = 2..7`, `xi_min` odd from `M = 2`, and `pt.err(xi_min) = sqrt 2 - 1` at every `M >= 2` (the off-circle point is never returned) while `pt.err(xi_ker) = 0`.
- Lead: "Worth keeping as a unit test for any C implementation." It is also the cheapest object on which to run the `Q-3` search and the inverse problem.
- Related: L09-042, L09-048, L09-064.

### L09-062 The perturbed operator is literally a companion matrix
- Source: ihara/lanes/numerics.md:232-240, 351-354
- Raised by: Opus numerics lane, as a "surprise"
- Status at last mention: pursued, positive; a structural reading, not registered
- Content: with `<eta|xi> = xi_M = 1` the wrap term of the cyclic shift cancels, `Z' = Z - |Z xi><eta| = S - |S xi><eta| = S'`, and `S'` is precisely the companion matrix of `P(z) = z^M xi_hat(z)`: in the identification `e_j <-> z^{M+j}`, it is multiplication by `z` modulo `P`. "the 'spectral triple' here is nothing but the Frobenius/companion form of the secular polynomial, and the CCM inner product `tau - eps` is precisely the one that makes it unitary. That is the discrete shadow of the notebook's 'side B is a scalar times a unitary on its nontrivial part'."
- Lead: none stated; but it is the clearest statement in the lane of how CCM's construction and the notebook's side-B picture are the same thing, and it is the reading that should carry to the Selberg case.
- Related: L09-035, L09-050.

### L09-063 Only arb can tell "exactly zero" from "small and negative" near the Ramanujan boundary
- Source: ihara/lanes/numerics.md:304-326; ihara/plan.md:440-444
- Raised by: Opus numerics lane
- Status at last mention: pursued, positive (this is the argument for the C/arb implementation)
- Content: double precision suffices for `eps_M` everywhere tried (agreement `<= 2.3e-13`), and for the roots whenever the kernel is simple. "The one thing double genuinely cannot do is certify `eps_M = 0`": at the critical window `cond(T) ~ 1e16 - 1e18` and float64 returns `+-1e-15` with arbitrary sign. "a graph with `lambda_2` just above `2 sqrt q` would need `eps_M` resolved below `(lambda_2/(2 sqrt q))^{2M}`-ish."
- Lead: the experiment implied but not run: take a family with `lambda_2` approaching `2 sqrt q` from above and measure how much precision is needed to detect the failure of Ramanujan at each window. This is the discrete model of "how close to the critical line can the construction see".
- Related: L09-043, L09-048, L09-065.

### L09-064 Real retained points at angle `0` or `pi` are unresolved by the circle-root finder
- Source: ihz/README.md:51-52
- Raised by: orchestrator (Claude), from the implementation
- Status at last mention: recorded as a known limit of the MVP
- Content: "Real retained points at `mu = +-sqrt q` (angle `0` or `pi`) are reported as unresolved by the circle-root finder; the exact kernel polynomial sees them."
- Lead: gates the two-disjoint-`K_4` case (L09-061), whose off-circle pair sits at angle `0`, and any bipartite object with a retained point at `-sqrt q`. The exact stage already carries the anchor there, so the fix is in `circle_roots.c` only.
- Related: L09-061, L09-065.

### L09-065 `ihz_eigmin` declines to certify degenerate block eigenvalues
- Source: ihz/README.md:49-50, 39
- Raised by: orchestrator (Claude), from the implementation
- Status at last mention: recorded as a known limit; the exact stage still carries the anchor
- Content: the ported Krawczyk eigenpair certificate "declines at `eps = 0` and at degenerate eigenvalues" — concretely the prism at `Mp = 6` (even block) and the odd block of `Cn:5` at `Mp = 2`.
- Lead: gates any experiment in the over-resolved regime and any graph with symmetry-forced degeneracy (which is most small test graphs); the symmetric-fallback idea L09-025 or a deflation-based certificate would be the routes.
- Related: L09-025, L09-039, L09-064.

### L09-066 `ihz` was built with testing discipline deliberately relaxed
- Source: ihz/README.md:53-54
- Raised by: TJO (the relaxation was at TJO's request)
- Status at last mention: recorded as debt
- Content: "Testing discipline was relaxed for this build at TJO's request: one pinned test file per worker and the end-to-end anchor; no fuzz, no mutation yet."
- Lead: `zst`'s mutation and fuzz runs each found real bugs (the `b_0` rounding neighbourhood, the `j = N` root branch, the Newton contraction step), so the same passes on `ihz` are likely to find some; this gates trust in every `ihz` number, including the exact anchor.
- Related: L09-031, L09-091.

### L09-067 LPS graphs at scale
- Source: ihara/plan.md:325-327, 369-370, 403-405
- Raised by: orchestrator (Claude)
- Status at last mention: raised, deferred to M4 ("not MVP")
- Content: LPS Cayley graphs (from `scripts/weil_lps.py` generators) with `PGL_2(F_13)`, `|V| = 2184`, `R` up to about 4000, needing `K ~ 4000`.
- Lead: LPS graphs are the notebook's own Ramanujan objects and the ones tied to `conj:weil-lps-hecke`; running the construction on one at its critical window would connect the sidequest to the Weil-LPS lane. It needs the `O(K^2)` structured solvers (L09-024) to be feasible.
- Related: L09-013, L09-024.

### L09-068 The exact-rational inertia fast path: `D T D` is an integer matrix
- Source: ihara/lanes/code-audit.md:300-354; ihara/plan.md:330-331, 365-367
- Raised by: Sonnet code-audit lane
- Status at last mention: "a genuine opportunity for the Ihara port, not required for the MVP"; partially used (`toeplitz.c` carries the exact integer congruence)
- Content: with `d_j = q^{j/2}`, `(DTD)_{jj'} = q^{min(j,j')} c_{|j-j'|}` — an **exact non-negative integer** in every entry, even though `D` itself is irrational. By Sylvester's law of inertia this has the same signature as `T`, which is all the certificates ever ask for. For a rational shift `s`, `D(T - sI)D = DTD - s D^2` is exactly rational, so its inertia can be certified by exact `fmpq_mat` `LDL^T` "with **zero precision loss and zero ball-radius bookkeeping**". The similarity `D T D^{-1}` is explicitly rejected: not symmetric, no exactness gain.
- Lead: this would replace the step that failed at scale in `zst` (L09-026) with an exact computation, for any object whose atoms are integers — i.e. every graph, curve and channel. Worth testing whether it can be pushed back into `zst` for the discrete data model.
- Related: L09-026, L09-032, L09-057.

### L09-069 The Chebyshev reduction for circle roots
- Source: ihara/lanes/code-audit.md:229-261
- Raised by: Sonnet code-audit lane
- Status at last mention: raised, deliberately deferred ("documented but initially-unimplemented speed-up")
- Content: `R(theta) = xi_0 + 2 sum_j xi_j cos(j theta)` becomes, under `x = cos theta` and `cos(j theta) = T_j(x)`, an ordinary real polynomial of degree `M`, so root-finding on `[-1,1]` reduces to real polynomial root isolation and avoids `M` `arb_cos` evaluations per candidate.
- Lead: gates the large-`K` runs (LPS graphs, L09-067) where root finding would otherwise dominate.
- Related: L09-024, L09-067.

### L09-070 `arb_fmpz_poly_complex_roots` hangs forever on repeated roots
- Source: ihara/lanes/code-audit.md:163-227; ihara/plan.md:450
- Raised by: Sonnet code-audit lane (found by running it to a 20 s timeout and by reading FLINT's source)
- Status at last mention: pursued, negative for the naive route; fixed by squarefree factorisation first
- Content: the function's loop only exits when `acb_poly_find_roots` returns pairwise-disjoint balls, which can never happen at a genuinely repeated root, so it runs until precision overflows or the process OOMs. Its "deflation" strips only a `poly(x^d)` structure, not root multiplicity. The fix — `fmpz_mat_charpoly` then `fmpz_poly_factor_squarefree` then `arb_fmpz_poly_complex_roots` per factor — is instantaneous at `n = 12` and `n = 24` and gives multiplicities free from the factorisation exponents.
- Lead: "worth a defensive comment (or an assertion that the input is squarefree) at every call site", because a future edit removing the squarefree step "would silently hang, not fail loudly, on the very test graphs that exercise it".
- Related: L09-071.

### L09-071 `acb_mat_eig_multiple_rump` is not a primary truth route
- Source: ihara/lanes/code-audit.md:128-161, 263-278; ihara/plan.md:448-449
- Raised by: Sonnet code-audit lane
- Status at last mention: pursued, negative as a primary route; demoted to a cross-check
- Content: it needs the approximate eigendata computed at (at least) the certification precision, not a cheap pre-pass (`tol = NULL`, matching `prec`), and even then it failed at `n = 24` in one shot at `prec = 200`. FLINT's own test harness handles this with a doubling-`prec` retry loop. `eig_simple_rump` correctly refuses multiplicity, which most symmetric small graphs have.
- Lead: keep it only as a secondary cross-check with a doubling retry — it is still the only route that returns certified eigen*vectors*, which is what one would need to compare against `xi` itself.
- Related: L09-070.

### L09-072 The `k = 0` boundary term is the most likely silent bug
- Source: ihara/lanes/code-audit.md:302-308, 547-553
- Raised by: Sonnet code-audit lane
- Status at last mention: flagged; a red test was recommended before any other work in `cycles.c`
- Content: the trivial-eigenvalue formula in the notebook is stated for `l >= 1`; `k = 0` (the Toeplitz diagonal `t_0`) needs its own derivation — `Tr B^0 = 2|E|`, minus the `(1-u^2)^{|E|-|V|}` factor's own `k = 0` term `2(|E|-|V|)`, minus the `q^0 + 1 = 2` from the `q+1` pair. Explicitly the same failure mode as `zst`'s fuzz catch, where "`b_0` was a rounding neighbourhood of zero instead of exactly zero".
- Lead: gates every number `ihz` produces, since `t_0` is the whole diagonal.
- Related: L09-066.

### L09-073 Ground truth for the graph side must cite the notebook, not a fetchable paper
- Source: ihara/lanes/code-audit.md:554-564
- Raised by: Sonnet code-audit lane
- Status at last mention: raised, adopted as a documentation convention
- Content: `zst`'s house rule (every formula in `src/` cites `refs/src/2511.22755/mc2arXiv.tex` by file and line) works because CCM is a single fetchable TeX source. The Ihara-Bass ground truth is spread over Bass 1992 (not on arXiv) and Terras 2011 (a book). The recommendation is to cite this repo's own `report/sections/02_definitions.tex` and `08_quantum_ihara_general.tex` by line instead, since those carry their own status and upstream citations.
- Lead: none beyond the convention; but it means the `ihz` code's ground truth is only as good as the notebook's own `stipulated` rows.
- Related: L09-085.

### L09-074 The window-size rule of thumb, superseded
- Source: ihara/lanes/code-audit.md:478-482, 565-571; ihara/plan.md:352-354
- Raised by: Sonnet code-audit lane, then corrected by the theory lane
- Status at last mention: superseded by the exact rule `K = R + 1`
- Content: the audit proposed "`M >= diameter`, or a small multiple, determine empirically" by analogy with `zst`'s `N ~ 10 lambda^2`, and flagged that the right question for Ihara is "how large must `M` be for the window to resolve all nontrivial angles". The plan then replaces it outright: "the window heuristic '`M >= diameter`' in the audit's test plan is replaced by the critical-window rule `K = R+1`."
- Lead: recorded so nobody re-derives the heuristic; the exact answer is `K = R+1` and it is blind-detectable (L09-057).
- Related: L09-039, L09-057.

### L09-075 An ungraded Ramanujan graph has no zeros at all, so a zero-finding MVP on one is vacuous
- Source: ihara/lanes/notebook-extract.md:292-298, 339-342; ihara/lanes/theory.md:163-187; ihara/plan.md:58-63, 112-115
- Raised by: Sonnet notebook-extraction lane (as a warning) and confirmed by the Opus theory lane (`IH-6`)
- Status at last mention: pursued, settled; drove the sign convention of the whole library
- Content: `prop:no-ungraded-zeros` says that for `P = 1` the ring zeta has no zeros — "*every* ordinary (ungraded) Ramanujan graph/expander in this notebook has a zeta with *no zeros at all* — only poles — so a CCM-style zero-finding MVP on a plain Ramanujan graph is vacuous unless a grading is added." Consequently `Psi_X = W_C - W_{0,2} - W_R` sums over poles, and feeding a graph into a zeta-signed pipeline gives `-QW`, so the relevant extremum flips to the **largest** eigenvalue. Makhoul's theorem covers both extremes, so the construction still works, but every inequality reverses.
- Lead: "The sign convention (`sign` field) is the single most likely silent error; the mixed-divisor refusal and the curve test guard it." This is also the argument for the curve/graded instance existing at all.
- Related: L09-058, L09-059.

### L09-076 Concrete test objects with known Jordan structure at the Ramanujan boundary
- Source: ihara/lanes/notebook-extract.md:374-391
- Raised by: Sonnet notebook-extraction lane
- Status at last mention: raised, not pursued (never run through `ihz`)
- Content: `K_3 box Q_3` is 5-regular and Ramanujan with adjacency eigenvalue `-4` of multiplicity two, and its Hashimoto matrix has `dim ker(T+2) = 2`, `dim ker(T+2)^2 = 4`; the ten-letter Pauli channel (`I^4, X^4, Z^2`, `P = Z`, `D = 10`, `q = 9`) is sector-Ramanujan with an odd Hashimoto eigenvalue `3` of nullities `1, 2`. "the endpoint counterexamples (Jordan blocks at `a = +-2 sqrt q`, i.e. at the Ramanujan boundary) are the finite, exactly-computable analogue of what CCM's construction must avoid or handle at a multiple/boundary zero."
- Lead: run both through `ihz` and see what the construction does at a genuine Jordan block on the critical circle — the one situation where `prop:weil-blind-jordan` says Weil positivity holds but no Hilbert-Polya inner product exists. Nobody has tried.
- Related: L09-019, L09-056, L09-065.

### L09-077 The `C4` correction the plan should inherit verbatim
- Source: ihara/lanes/notebook-extract.md:404-410, 436-440
- Raised by: Sonnet notebook-extraction lane
- Status at last mention: raised as a warning, not acted on
- Content: shard 06h's condition C4 carries an explicit "Correction to the reading of 08b: inverse-closed letters do **not** give the FE for the raw doubled transfer" — the reciprocal quadratics arise in the non-backtracking construction only after the Bass factors are removed. "a correction the plan should inherit verbatim, since it is exactly the subtlety a naive graph-window FE implementation would trip over."
- Lead: check that `ihz`'s `fe_asserted` flag and its trivial-divisor bookkeeping respect this; the functional equation is the hypothesis on which the whole two-sided extension rests (`IH-2`).
- Related: L09-044, L09-060.

### L09-078 Caratheodory-Fejer, Pisarenko and the finite window are new to this notebook
- Source: ihara/lanes/notebook-extract.md:444-483
- Raised by: Sonnet notebook-extraction lane (by exhaustive grep)
- Status at last mention: established as a fact about the notebook
- Content: "Caratheodory-Fejer" occurs nowhere in `report/sections/*.tex` or in any established note — only in this sidequest's own files and the 2026-09-17 worklog. "Pisarenko" occurs nowhere in the repository at all. "window" outside the sidequest means only the archimedean test-function window or a Gaussian window on the Selberg side, never a finite-transfer-operator window. So the positivity content (`thm:weil-positivity-finite`) is old but "the finite-window-as-Caratheodory-Fejer framing, and any Pisarenko-style reading, are net new and should be flagged as such rather than cited to a shard."
- Lead: if any of this is registered as a shard, it must be registered as new, not as a corollary of 08b.
- Related: L09-018, L09-052.

### L09-079 The Artin-Schreier curve as the other finite side-A/side-B anchor
- Source: ihara/lanes/notebook-extract.md:516-533; ihara/lanes/theory.md:980-983; ihara/plan.md:287-289
- Raised by: Sonnet notebook-extraction lane
- Status at last mention: raised, not run (the elliptic curve over `F_5` was run instead)
- Content: `thm:as-super-transfer` gives `N_n = str E^n` with the odd block `F` satisfying `F F^dagger = q` and a multiset of `2g = (q-1) q^J` Frobenius eigenvalues with no even-odd cancellation. Proposed check 24: build `t_k` with the fermionic sign from `scripts/artin_schreier_mps.py` data, run the same code, recover `alpha_i/sqrt q` at `K = R+1`, and cross-check against Hallouin-Perret's bound.
- Lead: this would be the first genuinely higher-genus object through the pipeline (the `F_5` elliptic curve has `R = 2`), so it is the first place the critical window is large enough for the under-resolved law to be measured on a curve.
- Related: L09-041, L09-059, L09-082.

### L09-080 TJO's original counterexample probe: a non-Ramanujan cubic graph with off-line zeros
- Source: ihara/lanes/notebook-extract.md:597-633 (summarising transcript/transcript.md:484-492)
- Raised by: TJO
- Status at last mention: honoured — the prism, the necklaces and two disjoint `K_4` are exactly this
- Content: in the founding session TJO offered the Ihara zeta as "the discrete sibling of Selberg's zeta with a genuine, checkable RH" because "the compression from big matrix to small matrix happens in one line", had two small cubic graphs checked for the Ramanujan property and Ihara zero radii, and "asked for a non-Ramanujan cubic graph with explicit off-line Ihara zeros as a counterexample probe". The extraction lane's closing observation: "the graph case functions consistently as TJO's preferred *test bed*: the one setting where RH can fail or hold for computationally cheap, exactly-known reasons... used repeatedly to falsify drafted universal claims before they were allowed into the book as theorems."
- Lead: keep feeding drafted universal claims to small graphs first; the lane's own non-Ramanujan families (prisms `C_n x K_2`, cubic necklaces of `K_4 - e`, two disjoint `K_4`) are the tunable-`rho` stock.
- Related: L09-048, L09-061, L09-076.

### L09-081 Read Connes-Consani, "Weil positivity and trace formula, the archimedean place"
- Source: ihara/lanes/literature.md:547-561, 652-673
- Raised by: Sonnet literature lane
- Status at last mention: raised, not pursued; already in `refs/fetch_sources.sh` but never physically fetched
- Content: arXiv:2006.13771 "expresses the difference between the Weil distribution and the Sonin trace, for the single archimedean place, in terms of prolate spheroidal wave functions and Hermitian Toeplitz matrices — i.e. this is very likely the paper that first connects Weil positivity to the Toeplitz-matrix machinery that CS later makes rigorous, and should be read closely before finalising the finite-graph plan, since its 'single place' framing is the closest existing analogue of a 'one prime `p`' (or one cycle-length) window."
- Lead: fetch and read it; it may already contain the single-place window analysis that `Q-2` is trying to reconstruct.
- Related: L09-041, L09-085.

### L09-082 Read Hallouin-Perret in full before building anything on curves
- Source: ihara/lanes/literature.md:172-196; theory.md:579-582, 855-860
- Raised by: Sonnet literature lane and Opus theory lane
- Status at last mention: raised, not done (no arXiv TeX; TAMS only)
- Content: Hallouin-Perret 2019 recover Weil's and Y. Ihara's classical point-count bounds for curves over finite fields as the first two steps of an SDP hierarchy built from symmetric Toeplitz matrices of moments. It is `[HP]` in `CS`, cited exactly where Corollary `corcar` is stated ("a striking number-theoretic flavor"), and `CS:871` uses its Lemma 33 for `xi_0 != 0`. "the closest existing 'CCM-style Toeplitz-positivity meets a genuine RH bound' precedent."
- Lead: read it before claiming novelty on the curve side; also note the lane's explicit warning: "**Do not conflate** the two 'Ihara's" — Y. Ihara's 1981 curve point-count bound is a different object from the graph Ihara zeta.
- Related: L09-059, L09-079.

### L09-083 Slepian's discrete prolate spheroidal sequences as the `Z`-side prolate object
- Source: ihara/lanes/literature.md:388-441
- Raised by: Sonnet literature lane
- Status at last mention: identified as the right object; not used
- Content: Slepian 1978 (Bell Syst. Tech. J. 57, Part V, the discrete case) introduces DPSS — index-limited and band-limited eigen-sequences of a finite Toeplitz operator built from the sinc kernel — "the exact discrete/finite-index analogue of the continuous Slepian-Pollak prolate functions the CCM papers use", and is "exactly the object this lane's task description calls 'Slepian's discrete prolate spheroidal sequences as the analogue of the paper's prolate functions'". The discrete analogue of Fuchs' eigenvalue-defect asymptotic (which is what `1 - chi_4(lambda)` is) is what DPSS supplies, "the quantity that would govern the finite-graph window's 'plunge region'". Freely downloadable at archive.org/details/bstj57-5-1371; not fetched.
- Lead: this is the concrete candidate answer to `Q-7` on the `Z` side and the natural analytic frame for `Q-2`. Fetch the paper; compute the DPSS plunge for the graph windows and compare with the measured `eps_M`.
- Related: L09-017, L09-041, L09-046.

### L09-084 Terras-Wallace's tree Selberg trace formula as the machinery that already exists
- Source: ihara/lanes/literature.md:591-632
- Raised by: Sonnet literature lane
- Status at last mention: verified verbatim, not used
- Content: Terras-Wallace derive the Ihara-Bass determinant formula from a genuine discrete Selberg trace formula on the `k`-regular tree, built from spherical functions `h_s(d)`, a horocycle transform `Hf` with `f_hat(s) = sum_n Hf(n) q^{|n|/2} z^n`, Selberg's Lemma as a pre-trace identity, and the trace formula `sum_i f_hat(s_i) = f(o)|X| + sum_{rho} nu(rho) sum_{e>=1} Hf(e nu(rho))`. "its trace-formula machinery (spherical/horocycle transform pair on the `k`-regular tree) is the natural 'already exists' analogue of the Fourier-truncation machinery in `zst`/CCM, specialised to `(q+1)`-regular graphs". Also noted: for irregular graphs `A_X` and `Q_X` need not commute, so the single-spherical-transform picture does not apply.
- Lead: if `Q-7` is to be asked on an infinite object, the tree is the object and this is its trace formula; the spherical/horocycle pair is the candidate window machinery.
- Related: L09-015, L09-046, L09-060.

### L09-085 The literature lane's own verification gaps
- Source: ihara/lanes/literature.md:708-724; and per item at 27-38, 237-262, 264-280, 317-330, 375-384, 526-531
- Raised by: Sonnet literature lane
- Status at last mention: recorded as gaps; none closed
- Content: unverified from primary text are Ihara 1966's original statement; **Terras 2011's book content** ("the single biggest gap — the book's actual explicit-formula/RH chapter content was never confirmed"); Pisarenko 1973; **Makhoul 1981's exact hypotheses** ("the abstract wording above is itself already a secondary paraphrase... its 'if distinct' clause needs checking against the actual small-window Weil matrices before use"); Delsarte-Genin-Kamp's eigenpolynomial zero-counting (could not locate a specific paper); Cantoni-Butler 1976; Simon's OPUC theorem number; whether Cantero-Moral-Velazquez 2005 has an arXiv id; and whether Connes-Moscovici's PNAS paper has one.
- Lead: Makhoul is the one that matters mathematically, because the graph's Weil form is real symmetric (not Hermitian PSD), so Makhoul's max-and-min statement, not Caratheodory-Fejer's, is what applies after the sign flip. Also: six arXiv ids were staged for `refs/fetch_sources.sh` (`2106.01715 2511.23257 math/0204300 math/0606037 2006.13771 2310.18423`) and the fetch was outside that lane's write scope.
- Related: L09-053, L09-054, L09-055, L09-081.

### L09-086 `IH-10(b)`: the angle operator fails, and that is a testable negative control
- Source: ihara/lanes/theory.md:253-277, 929-932; numerics.md:202-215
- Raised by: Opus theory lane and Opus numerics lane (independently)
- Status at last mention: PROVED negative; proposed as a deliberate negative control in the test suite
- Content: the literal transcription of `D V_n = n V_n` to the circle — the self-adjoint angle operator `A e_n = (2 pi n/K) e_n` — does not work: `(n-m) That_{nm}` is not of the form `c_n - c_m`, and the numerics lane measured `rank((2 pi n/K - 2 pi m/K) tau_{nm}) = 3` for `M >= 2` rather than 2. The nilpotent truncated shift also fails (no circle, `S^* T S != T`). Only the cyclic shift works.
- Lead: "**Negative control:** `rank([A, T])` for the angle operator is *not* `2`... This is `IH-10`(b) and it is the check that decides the candidate question." Keep it as a test so the wrong `D` cannot creep back in.
- Related: L09-035, L09-037.

### L09-087 The "does not generalise" list, ranked by consequence
- Source: ihara/plan.md:223-266; theory.md:615-700
- Raised by: Opus theory lane; ranked by the orchestrator
- Status at last mention: established; the main deliverable of the theory lane
- Content: twelve items `NG-1` to `NG-12`. Ranked: (1) `NG-3` finite divisor, so no permanent under-resolution, hence "the phenomenon CCM's missing proof must control does not exist on a graph" — the single most important entry; (2) `NG-7` no Hermite/prolate tower; (3) `NG-1`/`NG-2` no second truncation, no Dirichlet-kernel approximation (over `Z` the Dirichlet kernel *is* a delta, so a whole CCM subsection is vacuous); (4) `NG-4` no transcendental archimedean term, so "**MVP-2 therefore does not exercise the hardest existing code path in `zst/`**"; (5) `NG-8` Weil's criterion becomes a finite equivalence, `NG-9` no spectral-triple content, `NG-10` half of even-simple evaporates, `NG-11` multiplicities, `NG-5`/`NG-6` no analytic continuation and no number theory in the atoms; (6) `NG-12`, the one thing the graph adds: the chain can be run on a false RH.
- Lead: "Any claim that MVP-2 'tests the CCM programme' must be qualified by this." And `NG-4` means the M3 archimedean derivation (L09-010) gets no free testing from `ihz`.
- Related: L09-010, L09-039, L09-046, L09-050.

### L09-088 `G5`: make `ihz_weil_t` a constructor of the general `zst_weil_t`
- Source: ihara/plan.md:318-321, 403-405
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued (depends on M3)
- Content: `ihz_weil_t` is "the discrete instance of `zst_weil_t`: atoms at integer lengths with exact integer weights, trivial-divisor points as the pole terms, and `W_R` as a geometric kernel with `d = 1`, `mu = log q / 2`, `P = 1`. When `zst` M3 lands, `ihz_weil_t` should become a constructor for the general data model rather than a separate type."
- Lead: this is the step that makes the two verticals one library, and it is what would let a notebook channel (L09-016) run through the same certified path as zeta.
- Related: L09-001, L09-016, L09-033.

### L09-089 Variant `a3`: an `eta` that transports no information at all
- Source: ihara/lanes/numerics.md:222-231, 281-286
- Raised by: Opus numerics lane (testing a variant the task proposed)
- Status at last mention: pursued, negative; instructive
- Content: with `eta =` all-ones in the **position** basis, `Det(Z'' - s) = +-(s^K - 1)/(s - 1)` *independently of `xi`*: the spectrum is just the nontrivial `K`-th roots of unity, checked to `1e-15` at every window. "That `eta` transports no information at all." Similarly variant `d` (all-ones in the DFT basis) returns the polynomial with `xi`'s coefficients cyclically rotated by one, `ang.err = 0.89`.
- Lead: a permanent warning: a variant can look like it works (real spectrum, points on the circle) while carrying none of the data. The check that catches it is comparing against known truth, which is why the graph anchor matters.
- Related: L09-037, L09-049.

### L09-090 What is the continuous counterpart of using the lag one step outside the window?
- Source: ihara/lanes/numerics.md:245-247, 362-366
- Raised by: Opus numerics lane, as a question for the theory lane
- Status at last mention: OPEN; not answered by the theory lane
- Content: the discrete isometry proof extends the bilinear form to the window `{-M..M+1}` and uses `B~(zP, zg) = B(P, g)`, i.e. it needs the lag `t_{2M+1}`, one beyond the window. "what is the continuous counterpart of `B~(zP, zg) = B(P, g)`, i.e. of using the lag `t_{2M+1}` one step outside the window?" The same one-step-outside structure appears in Lemma `key`(i), which "holds in the critical and over-resolved regimes and fails in the under-resolved one, where the conclusion nevertheless still holds, so (i) is sufficient but not necessary here."
- Lead: answering it would say whether CCM's continuous argument is really the same proof; and it is the precise sense in which the construction sees slightly more data than the window contains.
- Related: L09-047, L09-051.

### L09-091 Mutation testing of the 2026-09-18 changes
- Source: notes/zeta-spectral-triples/report-2026-09-18.md:66-67; zst/README.md:53-64
- Raised by: orchestrator (Claude)
- Status at last mention: listed under "Next, if pursued"; not done
- Content: the benchmark drove several substantial code changes (the positive-definiteness certificate, the sign-scan candidate generator, the mean-value Newton verifier, the `O(N^2)` Krawczyk step); the mutation record in the README covers only the 2026-09-17 MVP.
- Lead: gates trust in every certified number in `benchmark.md`, since all the `x >= 20` rows were produced by the changed code.
- Related: L09-031, L09-066.

### L09-092 The atom side of the graph problem is free
- Source: ihara/lanes/theory.md:216-218
- Raised by: Opus theory lane
- Status at last mention: observed, not exploited
- Content: "Unlike `zeta`, where `lambda^2` primes must be enumerated, `N_k = Tr B^k` is a trace of a matrix power: `O(|E|^3 log k)` by repeated squaring, or `O(|V|^3)` once from `spec(A)`. The atom side of the graph problem is free."
- Lead: means the graph can be pushed to very large windows cheaply on the data side — the cost is entirely in the linear algebra, which is where the `O(K^2)` structured solvers (L09-024, L09-069) would pay.
- Related: L09-024, L09-067, L09-069.

## Small but possibly consequential

1. **L09-020, the odd block.** A second, unexamined operator sitting in already-computed data, explicitly "not in the paper" — and the graph side shows the odd block is exactly where a failure of RH would live.
2. **L09-027, the tail roots.** They cluster just past `N`, come in pairs and reach `31 N`; nobody asked what they are, yet completeness-by-count (hence every certified table) depends on accounting for them.
3. **L09-047, `Q-8`, the general-`eta` key lemma.** One clean statement would cover zeta and graphs at once and might remove CCM's parity hypothesis, which CCM themselves list among the missing steps.
4. **L09-048's inverse problem.** Recovering the offending adjacency eigenvalue from the slope of `log(-eps_M)` alone — the lane says outright "If this works it is a genuinely new diagnostic", and it was never run.
5. **L09-063, the near-Ramanujan precision law.** How much precision is needed to see a `lambda_2` just above `2 sqrt q` is the discrete model of how close to the critical line the construction can see; one line in the numerics lane, no experiment.
6. **L09-068, `D T D` is an exact integer matrix.** It would replace the certificate step that failed at scale in `zst` with exact arithmetic for every integer-atom object, and it was filed as "an opportunity, not a requirement".
7. **L09-076, `K_3 box Q_3` and the ten-letter Pauli channel.** Ready-made objects with a genuine Jordan block at the Ramanujan boundary — the one case where Weil positivity holds but no Hilbert-Polya inner product exists — never run through `ihz`.
8. **L09-054/L09-055, the graph's gamma factor and its missing explicit formula.** The literature lane searched and found neither in the primary sources; `IH-3` plus a motivic reading of `(1-u^2)^{r-1}` would be a small, self-contained result.

## Dead routes recorded

- **Interval `LDL^T` inertia certification at scale.** Fails from `x = 20` on; input radii amplified by the squared condition number (`1e192`). Replaced by verified positive definiteness of the deflated matrix plus a ball residual. — benchmark.md:66-71; report-2026-09-18.md:46-49
- **The QR candidate generator for the secular roots.** Dominated runtime (612 of 673 s at `x = 40`) and its precision cannot be reduced below the dynamic range of the rank-one term (about `5.5 x` digits). Kept only as a fallback. — benchmark.md:72-77
- **Plain interval evaluation of the secular derivative for far-out roots.** Useless; a mean-value form is required. — report-2026-09-18.md:50-52
- **Global root isolation by ball arithmetic in `zst`.** "hopeless while point plus tiny-interval Newton verification is easy", because the normalisation `sum xi_j = 1` amplifies `xi` by 18 to 28 digits. — zst/README.md:39-43
- **arb's `acb_mat_eig_enclosure_rump` used directly for the eigenvector.** It returns its inflated containment box, so the eigenvector had to be re-verified and contracted by hand. — zst/README.md:37-39
- **Completeness of the root list by search range.** Two of the `N` positive roots lie far beyond the last pole (`s ~ 107, 339` at `N = 40`), so completeness must be by count. — zst/README.md:41-43
- **The self-adjoint angle operator `diag(2 pi n/K)` as the discrete `D`.** `(n-m) That_{nm}` is not of the form `c_n - c_m`; measured commutator rank 3, not 2. FAILS. — theory.md:269-272; numerics.md:209
- **The nilpotent truncated shift as the discrete `D`.** Not invertible, `spec(S) = {0}`, so there is no circle for the spectrum and `S^* T S != T`. FAILS. — theory.md:274-277
- **`eta =` all-ones in the position basis (variant a3).** Gives a `xi`-independent determinant `(s^K-1)/(s-1)`; transports no information. — numerics.md:281-286
- **`eta =` all-ones in the DFT basis (variant d).** Returns `xi`'s coefficients cyclically rotated by one; `ang.err = 0.89`. — numerics.md:288-290
- **`CS` Proposition `prop:finmain` taken literally with all-ones `eta` (variant c1).** Roots real but wrong: `ang.err = 0.52` at a window where the truth is exact. The paper's proposition does not apply verbatim to the Toeplitz form, for two independent reasons. — numerics.md:272-279
- **The additive key-lemma family when `xi` is odd.** `eta` is `gamma`-even in every additive variant, so `<eta|xi> = 0` and the normalisation is impossible; this is what happens for every non-Ramanujan object. — numerics.md:292-296
- **`arb_fmpz_poly_complex_roots` on a raw characteristic polynomial.** Never terminates on a repeated root; must square-free-factor first. — code-audit.md:163-201; ihara/plan.md:450
- **`acb_mat_eig_multiple_rump` as a primary truth route.** Failed at `n = 24` even at matching precision; needs a doubling-precision retry and is demoted to a cross-check. — code-audit.md:128-161, 263-278
- **The similarity `D T D^{-1}`.** Not symmetric, still irrational below the diagonal, breaks the `arb_mat_cho`/`ldl` family. "**Do not use this transform.**" — code-audit.md:326-335
- **`nf_elem`/antic exact arithmetic over `Q(sqrt q)` for the Ihara MVP.** Buys nothing: the `t_k` must become balls anyway, and the useful congruence is already exactly integral. — code-audit.md:280-298
- **A canonical `xi` in the over-resolved regime by minimal degree or minimum norm.** Both break the circle conclusion (extra roots at `0`, or strictly inside the disc). — theory.md:543-549
- **Interpreting the construction's output for an irregular graph.** Structurally incapable: the output is always `2M` points on the unit circle and the true divisor is not on any circle; `pt.err` saturates (dumbbell, at about `0.20`). — numerics.md:174-182; theory.md:814-817
- **Running the chain on a mixed-parity retained divisor.** Indefinite by construction, independently of RH; `eps_M` is not a noise floor and the output has no interpretation. — theory.md:862-871
- **Expecting the graph to test CCM's missing step.** `NG-3` and `NG-7`: a finite divisor has a critical window, so permanent under-resolution does not exist, and there is no theta function, no self-dual Gaussian and no prolate tower over `Z`. "the step the graph MVP **cannot test at all**." — theory.md:635-641, 659-669
- **The window heuristic "`M >= diameter`".** Superseded by the exact critical-window rule `K = R+1`. — ihara/plan.md:352-354
