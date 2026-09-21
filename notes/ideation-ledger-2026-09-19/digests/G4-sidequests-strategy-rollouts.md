# Digest G4: CCM sidequest, RH strategy review, codex transcript residue

Sources merged: lanes L09 (Connes-Consani-Moscovici "zeta spectral triples" sidequest, `zst`/`ihz`),
L10 (the 2026-09-19 RH strategy review plus the Lindblad readings and small reviews),
L14/L15/L16 (codex prover transcript residue, 2026-09-12 to 2026-09-16),
L17 (the 2026-09-19 astra ideation session seen from its transcripts).

## Themes

1. What the CCM chain actually proves: reality is free, positivity is the whole content.
2. The certified zeta benchmark: three accuracy laws, unfinished runs, and scaling.
3. CCM's missing step (the prolate tower) and the hunt for a discrete analogue.
4. Key lemmas, the displacement vector `eta`, and the open generalisations.
5. The finite anchor: windows, regimes, and what a failure of RH looks like on a graph.
6. Signs and divisors: gradings, curves, mixed parity, irregular graphs.
7. Certification engineering, library traps, test debt, and the shared data model.
8. Literature, priority and unverified citations in the CCM sidequest.
9. The cusp bridge: why Riemann differs from Selberg at operator level.
10. Rigidity: what would actually force equal decay widths (the RH-sized step).
11. Weil positivity, the Suzuki screw kernel, and amplification products.
12. Graded channels and cMPS letters: the finite decay-selection mechanism.
13. Stationary states, reinsertion, unbounded generators and the critical BC limit.
14. Lindblad mixing readings: the `||Z_t|| = 1` negative and the right form of a decay statement.
15. Codex prover corrections to the notebook's own drafted statements (09-12 to 09-16).
16. Method, tooling, provenance and repo bookkeeping.
17. Ranked next tasks nobody took, and questions left unsettled.

## Items

### G4-T1-1 Reality of the spectrum is unconditional; positivity is the only place RH enters
- Absorbs: L09-002, L09-049, L09-050, L09-051, L09-062
- Class: EXPLORED-registered
- Raised by: subagent
- What: The CCM window matrix always has the Loewner shape `tau_{nm} = (b_n - b_m)/(n - m)`, `tau_{nn} = a_n`, i.e. `[D, tau]` is a rank-two commutator, for *any* real distribution on the window; so the real spectrum and the circle of returned points cost nothing arithmetic. This was verified brutally: 200 random real even Toeplitz matrices with no divisor behind them all give `T - eps_min` PSD with every root on the circle to `6.1e-13`, and the prism keeps returning circle points deep in the indefinite regime. RH enters the chain in exactly one place — the identification of the limit: the returned measure is the Caratheodory measure of `T - eps_M I` and converges to the true divisor iff `eps_M -> 0`, which is Weil's criterion verbatim. A further reading makes the link to the notebook's own picture: with `<eta|xi> = 1` the perturbed shift `Z'` is literally the companion matrix of `z^M xi_hat(z)`, so the "spectral triple" here is the Frobenius form of the secular polynomial and the CCM inner product is exactly the one making it unitary — the discrete shadow of "side B is a scalar times a unitary on its nontrivial part".
- Lead: spend no further effort on reality or on the existence of `eps` and `xi`; everything except the limit identification is free. The one sentence to carry to TJO is that CCM is a spectral realisation of Weil's criterion, not a route around it.
- Where: `ihara/lanes/theory.md:711-718,762-774`; `ihara/lanes/numerics.md:23-25,232-240`; `notes/zeta-spectral-triples/plan.md:60-63`

### G4-T1-2 `eps_N` is Pisarenko's noise floor, and every certified run is a windowed Weil-positivity instance
- Absorbs: L09-007, L09-018, L09-052, L09-078
- Class: EXPLORED-registered
- Raised by: subagent
- What: On a finite divisor the whole CCM construction is classical Caratheodory-Fejer for Toeplitz matrices, and `eps_M` is exactly Pisarenko's 1973 noise floor under the dictionary `eps_M <-> sigma^2`, divisor `<->` harmonic frequencies, critical window `<->` exact-order case. In the zeta case `log10 eps_N ~ -5.1 x + 8` was certified for `x = 13..50`, and each run therefore certifies `eps_N > 0` plus the even-simple hypothesis, i.e. a rigorous chain of windowed Weil-criterion instances. An exhaustive grep established that "Caratheodory-Fejer" appears nowhere in `report/sections/*.tex` and "Pisarenko" nowhere in the repository, so the finite-window framing is net new to the notebook and must be registered as new, not as a corollary of shard 08b.
- Lead: certify `eps_N` monotone in both `N` and `lambda` and push the grid until the law breaks; and read the signal-processing literature on order-underestimated Pisarenko, which is directly the under-resolved law nobody has derived.
- Where: `ihara/lanes/theory.md:591-604`; `ihara/lanes/notebook-extract.md:444-483`; `benchmark.md:55-57`

### G4-T1-3 The twelve "does not generalise" items, ranked — what a graph cannot test
- Absorbs: L09-087
- Class: EXPLORED-registered
- Raised by: subagent
- What: `NG-1` to `NG-12` list what breaks when CCM is moved to a graph. Ranked by consequence: (1) `NG-3`, a finite divisor has a critical window, so permanent under-resolution — the phenomenon CCM's missing proof must control — does not exist; (2) `NG-7`, no Hermite/prolate tower; (3) `NG-1`/`NG-2`, over `Z` the Dirichlet kernel *is* a delta, so a whole CCM subsection is vacuous; (4) `NG-4`, no transcendental archimedean term, so the graph MVP never exercises the hardest code path in `zst/`; then `NG-8` to `NG-11`; and finally `NG-12`, the one thing the graph adds, which is that the chain can be run on an object whose RH is false.
- Lead: any claim that the graph work "tests the CCM programme" must be qualified by this list; in particular the M3 archimedean derivation gets no free testing from `ihz`.
- Where: `ihara/plan.md:223-266`; `ihara/lanes/theory.md:615-700`

### G4-T2-1 The three measured accuracy laws for zeta
- Absorbs: L09-004, L09-005, L09-006, L09-023
- Class: EXPLORED-registered
- Raised by: subagent
- What: With `x = lambda^2`, certified benchmarking over `x = 13..50` gave: (i) `log10 err(z1) ~ -5.4 x + 15`, i.e. 5.4 digits per unit of `x`, matching the prolate/Fuchs prediction `4 pi / ln 10 = 5.46`, with `N` not entering at all — the primes up to 50 pin the first zero of zeta to 249 certified digits; (ii) accuracy degrades linearly in the height of the zero, `log10 err(z_k) ~ log10 err(z1) + 0.37 gamma_k`, with the slope `0.37` independent of `x` and unexplained; (iii) `N ~ 7.5 x` saturates, beyond which extra `N` only adds spurious roots that still have to be certified away. These three laws are the promised `(lambda, N, prec) -> accuracy` map, done only for zeta.
- Lead: derive the constant `0.37` from the prolate side — that would be a real result, and the linear degradation in `gamma` is the quantitative shape of what a proof would have to control.
- Where: `benchmark.md:41-54`; `notes/zeta-spectral-triples/plan.md:172-177,314-316`

### G4-T2-2 `x = 100`, the lost tables, and the reference-zero ceiling
- Absorbs: L09-008, L09-009, L09-030
- Class: PARTIAL
- Raised by: subagent
- What: Extrapolation says `x = 100` (`N = 1000`, 4000 bits) should take about 80 minutes and certify the first zero to about 500 digits with about 700 zeros below `1e-3`. The first attempt was OOM-killed at the 10.7 GB cgroup limit; an `O(N^2)` Krawczyk step then cut peak memory at `N = 800` from 5.1 GB to 2.4 GB and the run was never retried. Separately the `x = 60` and `x = 80` runs completed with full certified spectra but their output files were lost to a cleanup mistake before the tables were extracted. A quieter ceiling: the comparison truth comes from arb's `acb_dirichlet_zeta_zeros`, computed at full precision only for the first 20 zeros, so bounds below `1e-100` are only reported for `k <= 20` — the construction is certified far tighter than the truth it is compared against.
- Lead: rerun `x = 100` with the reworked memory footprint; the headline would be "the primes up to 100 determine the first zero of zeta to 500 digits, certified". Also regenerate the lost tables and compute independent high-precision zeros for `k > 20`.
- Where: `benchmark.md:32-34,61-63,83-85`; `report-2026-09-18.md:52-53`

### G4-T2-3 Scaling machinery: structured `O(N^2)` solvers, Chebyshev roots, free atoms, LPS graphs
- Absorbs: L09-024, L09-067, L09-069, L09-092
- Class: LEAD-unpursued
- Raised by: subagent
- What: `tau` is a Loewner matrix with a rank-two displacement, so a GKO-type displacement-structured `O(N^2)` LU exists and would be "a real win for `N >= 10^3`"; threading (`flint_set_num_threads`, OpenMP over columns) and a thin Julia wrapper were also proposed. On the graph side the circle root-finding reduces under `x = cos theta` to a real degree-`M` polynomial in Chebyshev form, avoiding `M` `arb_cos` calls per candidate. The atom side of a graph is free — `N_k = Tr B^k` by repeated squaring, or once from `spec(A)` — so all cost is linear algebra. The target that needs all of this is LPS Cayley graphs (`PGL_2(F_13)`, `|V| = 2184`, `R` up to ~4000, hence `K ~ 4000`), which are the notebook's own Ramanujan objects and the ones tied to `conj:weil-lps-hecke`.
- Lead: build the `O(N^2)` factorisation; it simultaneously unblocks `x = 100`, the Selberg case, and the first run of the construction on an LPS channel at its critical window.
- Where: `notes/zeta-spectral-triples/plan.md:210-212,265-267,328-331`; `ihara/plan.md:325-327`; `code-audit.md:229-261`

### G4-T3-1 The prolate module: the part that touches the missing proof
- Absorbs: L09-017, L09-021, L09-022
- Class: LEAD-unpursued
- Raised by: paper
- What: CCM's own route to RH is that `Xi` is the Fourier transform of `E(h)` for the unique Hermite combination `h_0, h_4` with zero integral; `k_lambda` is the same with prolate functions, its Fourier transform converges to `Xi` on substrips of `|Im z| < 1/2`, and if `xi_lambda ~ k_lambda` then `det_reg -> Xi` and Hurwitz gives RH. Step (ii) is the whole difficulty. The proposal is a separate module computing prolate spheroidal functions at high precision through the `PW_lambda` eigenproblem in a Legendre basis (tridiagonal, arb-certifiable), giving `1 - chi_n(lambda)` and `k_lambda`. Two cheap probes sit beside it: the sign pattern and decay of the eigenvector coefficients `xi_j` against the prolate coefficients of `k_lambda` (needs only the eigenvector already computed), and evaluating `det_reg` against `acb_dirichlet_xi` on `|Im z| <= 0.4` at `x` far beyond CCM's own figures.
- Lead: even a rigorous numerical measurement of `||xi_lambda - k_lambda||` as a function of `lambda`, with certified enclosures, would be new data on the missing proof.
- Where: `notes/zeta-spectral-triples/plan.md:188-196,374-377,449-452,460-461`

### G4-T3-2 `Q-7`: is there any `Z`-side analogue of the prolate tower? (open)
- Absorbs: L09-046, L09-083, L09-084
- Class: PARTIAL
- Raised by: subagent
- What: CCM's proof route rests on a theta function, a Gaussian self-dual under the Fourier transform, a prolate deformation of the harmonic oscillator, a Meixner-Schafke estimate and Fuchs asymptotics. None of this has a counterpart over `Z`, and a graph's completed zeta is a polynomial with known roots — so the step whose absence blocks CCM is exactly the step a finite graph cannot test at all. The theory lane flagged this as "the real one" and did not investigate it. Two concrete candidate answers were found by the literature lane and never used: Slepian's 1978 discrete prolate spheroidal sequences (DPSS), the exact index-limited/band-limited analogue of the continuous prolate functions, which supply the discrete analogue of the Fuchs eigenvalue-defect asymptotic that `1 - chi_4(lambda)` is; and Terras-Wallace's genuine discrete Selberg trace formula on the `(q+1)`-regular tree, whose spherical/horocycle transform pair is the natural "already exists" analogue of the Fourier-truncation machinery.
- Lead: the only place a discrete model can touch the missing step is an infinite object — a tree quotient or the Selberg zeta. Fetch Slepian (archive.org/details/bstj57-5-1371, not fetched), compute the DPSS plunge for graph windows, and compare it with the measured `eps_M`.
- Where: `ihara/lanes/theory.md:659-669,1035-1040`; `ihara/lanes/literature.md:388-441,591-632`

### G4-T3-3 `Q-2`: the under-resolved law — the one quantitative question a graph can transfer (open)
- Absorbs: L09-041
- Class: PARTIAL
- Raised by: subagent
- What: Below the critical window, `eps_M > 0` is the Pisarenko noise floor of an exact `R`-atom measure observed with too few lags. The untested guess is that it is governed by the minimal angular separation `delta_min` of the `R` divisor points against the Fejer resolution `2 pi/K`, roughly `eps_M ~ c (K delta_min)^{2(R-K+1)}`. Measured accuracy falls roughly geometrically in `M` (necklace3 angle errors `1.32, 0.57, 0.26` at `K = 3,5,7`). The numerics lane added the sharpest identification: the minimiser is the degree-`2M` polynomial of unit coefficient norm minimising `sum_mu |xi_hat(mu/critr)|^2`, i.e. **a discrete prolate/Slepian problem**. The lane's own words: "I have neither derived nor tested this."
- Lead: fit the law on the existing graph families (`ihz --scan` already prints the data), then ask the decisive question — is `1 - chi_4(lambda)` the continuous limit of this rate? If yes, the graph gives a computable handle on the constant governing the zeta accuracy law.
- Where: `ihara/lanes/theory.md:1008-1014`; `ihara/lanes/numerics.md:100-105,380-384`

### G4-T4-1 `IH-11`, the unitary key lemma: a new three-line theorem, and the backbone decision
- Absorbs: L09-035, L09-038
- Class: EXPLORED-registered
- Raised by: subagent
- What: For `T` Hermitian PSD Toeplitz with one-dimensional kernel `C xi`, normalise `xi_0 = 1` and set `U = Z^*(1 - |xi><eta|)`. Then `U xi = 0` and `U^* T U = T` **exactly**, because `(1-P^*) T (1-P) = T` for `P = |xi><eta|` and the displacement is killed by `(1-P^*) eta = 0`; so `U''` on `E/C xi` is unitary with `det(U'' - w) = (-1)^{K+1} sum_k xi_k w^{K-1-k}`. It needs neither evenness of `xi` nor a simple-spectrum `D`, and it is new — not in Connes-van Suijlekom. The implementation nonetheless makes `CS` Corollary `corcar` the backbone (complete published proof, zero set unchanged by the perturbation, Caratheodory-Fejer additionally gives multiplicities, and `O(K^2)` by Levinson/Prony), with the unitary operator kept as a certified cross-check.
- Lead: it, not `corcar`, is what must be carried to the graded and Selberg cases, where the object of interest is an operator and not a polynomial.
- Where: `ihara/lanes/theory.md:297-346,395-425`; `ihz/src/unitary.c`

### G4-T4-2 `IH-13`: the graph case is literally an instance of Connes-van Suijlekom, not an analogue
- Absorbs: L09-036
- Class: EXPLORED-registered
- Raised by: subagent
- What: For odd `K`, with `lambda_n = tan(pi n/K)` and the real congruence `C = diag(sqrt(2K) cos(pi n/K))`, the DFT'd Toeplitz form becomes `Q_{nm} = (b_n - b_m)/(lambda_n - lambda_m)`, `Q_{nn} = a_n` — literally `CS` equation `form2` at `CS:1128`, with the parity hypotheses satisfied, so `CS:1356` applies verbatim. The costs are that `K` must be odd, the congruence is non-unitary so the `eps`-shift has to be done in the Toeplitz picture first, and it trades a natural unitary for an artificial self-adjoint.
- Lead: compute it once as a certificate that the graph case *is* an instance; if the Selberg or graded cases admit a Cayley analogue, the same congruence trick would carry `CS` there too.
- Where: `ihara/lanes/theory.md:369-393`; `ihara/plan.md:137-141`

### G4-T4-3 Read `eta` off the displacement, never posit it — and three variants that look right and carry nothing
- Absorbs: L09-037, L09-086, L09-089
- Class: EXPLORED-negative
- Raised by: subagent
- What: The second displacement vector is not free: in the position basis it is the delta at the window edge, in the DFT basis all-ones up to `K^{1/2}` and a phase, and in the un-congruenced Cayley picture `eta_n = (-1)^n sec(pi n/K)`. The prototype measures candidates by distance to `span(beta, eta)`: all-ones sits at `0.82-0.98`, the correct vector at `<= 4e-16`, and getting it wrong costs an `O(1)` error (angle errors 0.4-0.5) at a window where the answer is otherwise exact. Two variants are worse than wrong, they are silently empty: all-ones in the position basis gives `Det(Z'' - s) = +-(s^K - 1)/(s - 1)` *independently of `xi`*, and all-ones in the DFT basis returns `xi`'s coefficients cyclically rotated by one. The self-adjoint angle operator `A e_n = (2 pi n/K) e_n` also fails — measured `rank([A,T]) = 3`, not 2 — and so does the nilpotent truncated shift; only the cyclic shift works.
- Lead: keep the angle-operator rank test as a permanent negative control in the suite, and keep the graph anchor, because comparison against known truth is the only check that catches a variant which produces a real spectrum on the circle while transporting no information.
- Where: `ihara/plan.md:143-150`; `ihara/lanes/numerics.md:202-215,281-293`; `ihara/lanes/theory.md:253-277`

### G4-T4-4 `Q-8`: a key lemma with a general `eta`, and the complex-character case (open)
- Absorbs: L09-047, L09-012
- Class: PARTIAL
- Raised by: subagent
- What: The question is whether `CS`'s Lemma `key-general` holds with `|beta><eta| - |eta><beta|` for an **arbitrary** displacement pair rather than `eta = sum_i e_i`. The prototype verifies clauses (i), (ii) and (iii) in that generality for every window with `gamma xi = xi`, but no clean statement was written. The second half is sharper still: the multiplicative (unitary) key lemma needs no parity at all, while the additive one needs `gamma xi = xi` twice over — so is CCM's parity hypothesis avoidable by working with a unitary `U'` and a Cayley transform at the end? The same missing generality blocks non-self-dual L-functions: for a complex character `D(-y) = conj D(y)` makes `tau` Hermitian with complex `b_n` and the same rank-two commutator, and one either takes the real form of the pair `{chi, conj chi}` (route a, preferred) or needs a Hermitian version of the CS structure theorem (route b, unchecked).
- Lead: write and prove the general-`eta` lemma. If the parity hypothesis is avoidable, one of CCM's two explicitly listed missing steps (`CCM:1385`) disappears. This is the single most promising theorem-shaped item in the whole sidequest, and without the Hermitian case half of all L-functions are out of reach.
- Where: `ihara/plan.md:467-470`; `ihara/lanes/numerics.md:371-379`; `notes/zeta-spectral-triples/plan.md:415-419`

### G4-T4-5 `Q-1`: is there a canonical `xi` in the over-resolved regime? (open)
- Absorbs: L09-040
- Class: PARTIAL
- Raised by: subagent
- What: When `d = K-1-R >= 1` the kernel vector's polynomial has the `R` true roots plus `d` arbitrary ones. A family keeping the circle exists, `Ptilde = q_0(w)(w^d - beta)` with `|beta| = 1` — exactly the paraorthogonal completions, a one-parameter family with no canonical member. The minimal-degree choice puts the extra roots at `0` and the minimum-norm/Levinson choice puts them strictly inside the disc, so both break the circle. Nothing in the CCM/CS chain picks a `beta`.
- Lead: the untested mechanism is named and cheap: perturb `T -> T + delta(|eta><eta|` or the boundary rank-two term`)` and let `delta -> 0+`; does the kernel vector converge to a paraorthogonal one, and with which `beta`? If a canonical `beta` emerged the over-resolved regime would stop being a failure mode.
- Where: `ihara/lanes/theory.md:536-557,1002-1006`

### G4-T4-6 What is the continuous counterpart of using the lag one step outside the window? (open)
- Absorbs: L09-090
- Class: PARTIAL
- Raised by: subagent
- What: The discrete isometry proof extends the bilinear form to `{-M..M+1}` and uses `B~(zP, zg) = B(P, g)`, i.e. it needs the lag `t_{2M+1}`, one beyond the window. The numerics lane asked the theory lane what the continuous counterpart of that identity is and got no answer. The same one-step-outside structure appears in Lemma `key`(i), which holds in the critical and over-resolved regimes and fails in the under-resolved one although the conclusion still holds there — so (i) is sufficient but not necessary.
- Lead: answering it would say whether CCM's continuous argument is really the same proof, and it is the precise sense in which the construction sees slightly more data than the window contains.
- Where: `ihara/lanes/numerics.md:245-247,362-366`

### G4-T5-1 Three regimes, the exact anchor `K = R + 1`, and blind detection of it
- Absorbs: L09-034, L09-039, L09-057, L09-074
- Class: EXPLORED-registered
- Raised by: subagent
- What: With `R` the number of distinct retained points: under-resolved (`K <= R`) gives `eps_M > 0` and `K-1` circle points that are a Pisarenko approximation, not the divisor; critical (`K = R+1`) gives `eps_M = 0`, a one-dimensional kernel and exactly the `R` divisor points; over-resolved gives a kernel of dimension `K-R >= 2`, so even-simplicity fails. Verified on Petersen (`R = 4`): `eps_M = 15.88, 9.45, 5.71, 0, 0, 0, 0` for `K = 2..8`. `R` is observable without knowing the answer — `rank T` stabilises at `R` — so the algorithm finds the critical window by increasing `K` until the rank stops growing, but the detector must be exact rank over `Q`, not a ball heuristic. This replaced the audit's earlier heuristic "`M >= diameter`" outright. The whole point of the graph vertical is then five things a graph can do that zeta cannot: an exact anchor, the under-resolved law, the non-Ramanujan experiment, the irregular case, and the graded/curve sign.
- Lead: three of the five (under-resolved law, non-Ramanujan search, irregular case) are the unfinished experiments; the first two are separate items below.
- Where: `ihara/lanes/theory.md:485-502,550-553`; `ihara/plan.md:65-71,168-181`

### G4-T5-2 `Q-3`: anti-palindromic minimal eigenvectors — is "even-simple" *equivalent* to Ramanujan? (open)
- Absorbs: L09-042, L09-020
- Class: PARTIAL
- Raised by: subagent
- What: `CS:865` proves the kernel vector of a one-dimensional kernel is palindromic *or* anti-palindromic, and CCM's `even-simple` asserts the `+` sign, listing it among its own missing steps. The numerics lane found the mechanism: an off-circle reciprocal pair `{x, 1/x}` contributes `2 f_hat(x) f_hat(1/x)`, which is `>= 0` on even `f` and `<= 0` on odd `f`; so for a non-Ramanujan regular graph the even block stays PSD at every window while the **odd** block carries the negative eigenvalue, `xi_min` becomes odd, `<eta|xi_min> = 0`, and `even-simple` fails. A related unexamined object sits in already-computed data: CCM take the minimal eigenvector of the even block only, and nobody has asked whether the odd block's minimal eigenvector gives a second operator with real spectrum by the same lemma.
- Lead: a search over small regular graphs and window sizes for a `-` case would settle whether "even" is a theorem or a hypothesis over `Z`, and it is cheap. If it is an equivalence, then CCM's hypothesis is not an auxiliary technicality but a restatement of the target — which changes how the whole CCM programme should be read.
- Where: `ihara/lanes/theory.md:1016-1020`; `ihara/lanes/numerics.md:26-29,156-159`; `notes/zeta-spectral-triples/plan.md:462-463`

### G4-T5-3 `Q-4` and `IH-27`: the noise-floor growth law, its unrun inverse problem, and the precision needed near the boundary
- Absorbs: L09-043, L09-048, L09-061, L09-063
- Class: PARTIAL
- Raised by: subagent
- What: With a retained real pair `{rho, 1/rho}` of multiplicity `m`, `eps_M = -m rho^{K+1}/(rho^2-1)(1+o(1))`, so `d log(-eps_M)/dM -> 2 log rho` — verified on the prism `C_16 x K_2` and on two disjoint `K_4` (ratios `2.87, 2.80, 2.46, 2.10, 2.16 -> 2`). Two disjoint `K_4` is the minimal fully controlled non-Ramanujan test (the second Perron eigenvalue is retained, giving an off-circle pair at angle 0; recommended as a permanent unit test). When RH fails, `xi ~ u/||u|| - v/||v||` and the returned points approach equidistribution with an `O(1/K)` modulation and no divisor information (prism at `M = 21`: mean gap `0.148627` against `2 pi/(K-1) = 0.149600`, sd 8% of the mean, approaching but not converged). Separately, double precision suffices everywhere except at the critical window, where `cond(T) ~ 1e16-1e18` and only arb can tell "exactly zero" from "small and negative".
- Lead: two experiments, both named and neither run. (a) The inverse problem: from the slope of `log(-eps_M)` alone recover `lambda = sqrt q (rho + 1/rho)` and compare with the true value — "if this works it is a genuinely new diagnostic". (b) Take a family with `lambda_2` approaching `2 sqrt q` from above and measure how much precision is needed to detect the failure of Ramanujan at each window — the discrete model of how close to the critical line the construction can see.
- Where: `ihara/lanes/theory.md:720-741,743-760`; `ihara/lanes/numerics.md:124-127,304-326`

### G4-T5-4 The invariant metric, endpoint Jordan blocks, and multiplicity blindness
- Absorbs: L09-019, L09-056, L09-076, L10-054, L16-023, L16-024
- Class: PARTIAL
- Raised by: subagent
- What: For the Hashimoto companion of `mu^2 - a mu + q`, the explicit metric `G = [[I, Sigma/2],[Sigma/2, qI]]` satisfies `C^dagger G C = q G` and is positive **exactly** on the open Ramanujan band `|Sigma| < 2 sqrt q`; at the endpoint `a = 2 eps sqrt q` the shifted companion is a nonzero square-zero matrix, a size-two Jordan block, and a positive-metric unitary is diagonalisable — so only the *strict* band gives unitarisability, and constructing an invariant Hermitian form is not yet the RH step. Two concrete objects realise the endpoint: `K_3 (box) Q_3`, 5-regular Ramanujan with adjacency eigenvalue `-4` of multiplicity two and `dim ker(T+2) = 2`, `dim ker(T+2)^2 = 4`; and the ten-letter Pauli channel (`I^4, X^4, Z^2`, `P = Z`, `D = 10`, `q = 9`), sector-Ramanujan with an odd Hashimoto eigenvalue 3 of nullities 1, 2. Both are verified, both are products/tensor constructions, and neither has been run through `ihz`. Meanwhile the construction is structurally blind to multiplicity — `Ptilde` depends on the Caratheodory measure only through its support — though Prony restores the weights at the critical window (Petersen: 18 retained points, 4 distinct, multiplicities `5,5,4,4`).
- Lead: compute the CCM positive form `tau - eps_N` and the letter-derived `G_C` on the same small graph at the critical window and compare; if they agree up to a congruence, CCM's construction and the notebook's Hilbert-Polya metric are the same object. Then run both endpoint witnesses through `ihz` — the one situation where Weil positivity holds but no Hilbert-Polya inner product exists.
- Where: `ihara/lanes/notebook-extract.md:374-391`; `ihara/lanes/theory.md:517-534`; `2026-09-16T14-21-08.txt:245-247`; `03f_selberg_letters_finite.tex:54-89`

### G4-T5-5 TJO's own practice: falsify drafted universal claims on small graphs first
- Absorbs: L09-080
- Class: EXPLORED-registered
- Raised by: TJO
- What: In the founding session TJO offered the Ihara zeta as "the discrete sibling of Selberg's zeta with a genuine, checkable RH" because "the compression from big matrix to small matrix happens in one line", had two small cubic graphs checked for the Ramanujan property and Ihara zero radii, and asked for a non-Ramanujan cubic graph with explicit off-line Ihara zeros as a counterexample probe. The extraction lane's observation is that the graph case functions consistently as the test bed where RH can fail or hold for computationally cheap, exactly-known reasons, and is used repeatedly to falsify drafted universal claims before they are allowed into the book as theorems.
- Lead: keep feeding drafted universal claims to small graphs first; the tunable-`rho` stock is prisms `C_n x K_2`, cubic necklaces of `K_4 - e`, and two disjoint `K_4`.
- Where: `ihara/lanes/notebook-extract.md:597-633` (summarising `transcript/transcript.md:484-492`)

### G4-T6-1 No ungraded zeros; the sign field is the most likely silent error; mixed parity must be refused
- Absorbs: L09-058, L09-075
- Class: EXPLORED-registered
- Raised by: subagent
- What: `prop:no-ungraded-zeros` says that for `P = 1` the ring zeta has no zeros at all — only poles — so a CCM-style zero-finding MVP on a plain Ramanujan graph is vacuous unless a grading is added. Consequently `Psi_X = W_C - W_{0,2} - W_R` sums over poles, feeding a graph into a zeta-signed pipeline gives `-QW`, and the relevant extremum flips to the **largest** eigenvalue; Makhoul's theorem covers both extremes so the construction still works, but every inequality reverses. Separately the chain requires the retained divisor to be of a single parity: zeta (all zeros), an ungraded graph (all poles) and a curve (all zeros) each qualify, but the graded quantum Ihara zeta of `prop:qubit-graded-zeta` has both a nontrivial numerator and denominator and does not, unless one sector is pushed into the trivial divisor.
- Lead: the `sign` field is named as the single most likely silent error in the whole library; implement the mixed-parity refusal as a test (planned as G4 but not recorded as run in the `ihz` README) and let the curve test guard the other side.
- Where: `ihara/lanes/theory.md:163-187,862-871`; `ihara/plan.md:58-63,219-221`

### G4-T6-2 The curve instance gives CCM's sign back — but Hallouin-Perret got there first
- Absorbs: L09-059, L09-079, L09-082
- Class: EXPLORED-registered
- Raised by: subagent
- What: For a curve, `t_k = q^{-k/2} N_k - (q^{k/2} + q^{-k/2})` has CCM's sign exactly and there is no `W_R`; nothing in the linear algebra changes, only the one global sign of `def:graded-transfer-channel`. This was run on the elliptic curve over `F_5` in `ihz`, recovering angles `+-2.034443936` exactly at `M = 1`. But Hallouin-Perret (TAMS 2019), cited at `CS:800` and `CS:2103`, already derive upper bounds for `#C(F_q)` from precisely this semidefinite symmetric Toeplitz matrix as the first two steps of an SDP hierarchy — so the graded/curve instance is a re-derivation, not new mathematics, and `CS:871` even uses their Lemma 33. The next genuinely higher-genus object is the Artin-Schreier curve: `thm:as-super-transfer` gives `N_n = str E^n` with `2g = (q-1) q^J` Frobenius eigenvalues and no even-odd cancellation, and the check was specified (build `t_k` with the fermionic sign from `scripts/artin_schreier_mps.py`, recover `alpha_i/sqrt q` at `K = R+1`) but not run.
- Lead: read Hallouin-Perret in full before claiming anything on the curve side (no arXiv TeX, TAMS only), and do not conflate Y. Ihara's curve point-count bound with the graph Ihara zeta. Then run the Artin-Schreier curve — its critical window is the first one large enough to measure the under-resolved law on a curve.
- Where: `ihara/lanes/theory.md:830-860`; `ihara/lanes/literature.md:172-196`; `ihara/lanes/notebook-extract.md:516-533`

### G4-T6-3 `Q-6`: a Krein-space key lemma for mixed-parity divisors (open)
- Absorbs: L09-045
- Class: PARTIAL
- Raised by: subagent
- What: A graded transfer channel may retain both poles (`nu > 0`) and zeros (`nu < 0`); then `QW_M(f,f) = sum nu_ret(lambda)|f_hat|^2` is indefinite **by construction**, independently of RH, so `eps_M` is not a noise floor and the returned circle spectrum has no interpretation. The signature `(p, n)` is known, so a `J`-unitary version of `U''` exists formally, but "whether its spectrum localises anywhere useful is open".
- Lead: this is the obstacle to running the construction on the graded quantum Ihara zeta with both sectors retained; the only workaround in use is to put one sector into the trivial divisor, which is a choice, not a theorem.
- Where: `ihara/lanes/theory.md:862-871,1030-1033`

### G4-T6-4 `Q-5` and irregular graphs: Weil positivity without duality
- Absorbs: L09-044, L09-060, L09-077
- Class: EXPLORED-negative
- Raised by: subagent
- What: For an irregular graph everything using only "Hermitian Toeplitz" survives, but `A_ret` is not invariant under `mu -> R_G^{-1}/mu`, so there is no functional equation, `thm:weil-duality-pairing` does not apply, and positivity gives only the one-sided Stark-Terras bound. Interpretation then fails even when output exists: the construction returns `2M` circle points while the true divisor is on no circle (dumbbell: `eps_M` changes sign at `M = 4`, `pt.err` saturates near `0.20`; triangle-with-pendant: the pendant is invisible and `mu = 0` is retained, so the reflection is not even defined). The Perron pole `mu = 1/R_G` survives but its partner `1` generally does not, so `W_{0,2}` drops to rank one and the trivial divisor loses its `H^0` partner. A correction the plan must inherit verbatim: shard 06h's C4 says inverse-closed letters do **not** give the FE for the raw doubled transfer — the reciprocal quadratics appear only after the Bass factors are removed.
- Lead: two candidate fixes for the trivial divisor are named and untested — weighting by a Perron eigenvector, or passing to the universal cover's spectral radius. And the sharp open question: is there a statement "the construction converges iff the retained divisor is reciprocal-closed", i.e. is the functional equation a *necessary* input? An irregular graph is the cheapest example inside the notebook of Weil positivity without duality, the exact situation of `prop:kraus-no-duality-example`.
- Where: `ihara/lanes/theory.md:787-824,1025-1028`; `ihara/lanes/numerics.md:161-182`; `ihara/lanes/notebook-extract.md:404-410`

### G4-T7-1 Certificates that failed at scale, and the exact-integer route that would replace them
- Absorbs: L09-025, L09-026, L09-027, L09-028, L09-029, L09-032, L09-068
- Class: EXPLORED-registered
- Raised by: subagent
- What: Interval `LDL^T` inertia certification died from `x = 20` on, because input radii are amplified by the squared condition number (`1e192`); it was replaced by verified positive definiteness of the deflated matrix `E - 2 eps + c v v^T` by approximate Cholesky plus a ball residual, whose amplification is only linear. The QR candidate generator for the secular roots dominated runtime (612 of 673 s at `x = 40`) and was replaced by a sign scan with bisection per pole interval plus a geometric grid beyond the last pole; completeness must be by count, never by a search range, because tail roots cluster just past `N` and reach `31 N`. Overlapping certified balls are now resolved by a Newton step on the hull, which decides rigorously whether it is one root or two, and any interval evaluation of the secular derivative for far-out roots needs a mean-value form. The audit found a third route that would sidestep all of this: with `d_j = q^{j/2}`, `(DTD)_{jj'} = q^{min(j,j')} c_{|j-j'|}` is an **exact non-negative integer** in every entry, so by Sylvester's law of inertia the signature can be certified by exact `fmpq_mat` `LDL^T` with zero precision loss. The audit also proposed replacing the hand-rolled `verify_pd` with arb's public `arb_mat_spd_solve`.
- Lead: push the exact-rational inertia route back into `zst` for every object with integer atoms — graph, curve, channel. And build the unbuilt symmetric fallback `M = R^{-T} W^T (tau - eps) D' W R^{-1}` for near-double roots, since a genuine double root is exactly what a failure of simplicity of the zeta zeros would look like — the Newton-hull primitive is the only part of the pipeline that could in principle detect one.
- Where: `benchmark.md:66-80`; `code-audit.md:112-126,300-354`; `notes/zeta-spectral-triples/plan.md:292-295`

### G4-T7-2 FLINT/arb traps found by running them
- Absorbs: L09-070, L09-071
- Class: EXPLORED-negative
- Raised by: subagent
- What: `arb_fmpz_poly_complex_roots` never terminates on a repeated root — its loop exits only when `acb_poly_find_roots` returns pairwise-disjoint balls, which cannot happen at a genuine multiplicity, and its "deflation" strips only a `poly(x^d)` structure. The fix (`fmpz_mat_charpoly`, then `fmpz_poly_factor_squarefree`, then roots per factor) is instantaneous at `n = 12` and `n = 24` and gives multiplicities free from the factorisation exponents. `acb_mat_eig_multiple_rump` is not usable as a primary truth route: it needs approximate eigendata at the certification precision and still failed at `n = 24` at `prec = 200`; FLINT's own harness uses a doubling-precision retry loop.
- Lead: put a defensive assertion at every call site that the input is squarefree, because a future edit removing that step "would silently hang, not fail loudly, on the very test graphs that exercise it". Keep `eig_multiple_rump` only as a cross-check with a doubling retry — it is still the only route returning certified eigen*vectors*, which is what comparing against `xi` itself would need.
- Where: `code-audit.md:163-227,128-161`

### G4-T7-3 Known bugs, test debt, and library plumbing
- Absorbs: L09-031, L09-033, L09-064, L09-065, L09-066, L09-072, L09-091
- Class: PARTIAL
- Raised by: subagent
- What: Two real mutation survivors remain in `zst`: out-of-bounds reads in the sort and disjointness loops of `secular.c` that happen inside uninstrumented FLINT calls and escape ASan. The mutation record covers only the 2026-09-17 MVP, although the benchmark drove four substantial code changes afterwards (PD certificate, sign scan, mean-value Newton, `O(N^2)` Krawczyk), so every `x >= 20` row in `benchmark.md` was produced by unmutated code. `ihz` was built with testing discipline deliberately relaxed at TJO's request — one pinned test file per worker plus the end-to-end anchor, no fuzz, no mutation — although `zst`'s fuzz and mutation passes each found real bugs. Two known limits: real retained points at angle 0 or `pi` are reported unresolved by the circle root-finder, and `ihz_eigmin` declines to certify at `eps = 0` and at degenerate block eigenvalues (prism even block at `Mp = 6`, odd block of `Cn:5` at `Mp = 2`). The audit flagged the `k = 0` boundary term `t_0` as the most likely silent bug — it is the whole Toeplitz diagonal and needs its own derivation (`Tr B^0 = 2|E|`, minus `2(|E|-|V|)`, minus 2), exactly the failure mode `zst`'s fuzz caught when `b_0` was a rounding neighbourhood of zero. `eigmin.c` is copied verbatim between the two verticals rather than shared.
- Lead: run fuzz and mutation on `ihz` and on the changed `zst` code before any number is published; write the `k = 0` red test before touching `cycles.c`; keep the duplicated `eigmin.c` in the mutation set until `libzcore` is extracted.
- Where: `zst/README.md:53-64`; `ihz/README.md:49-54`; `code-audit.md:302-308,547-553`

### G4-T7-4 One data model for every explicit formula, and the builders never written
- Absorbs: L09-001, L09-010, L09-011, L09-013, L09-014, L09-016, L09-088
- Class: LEAD-unpursued
- Raised by: subagent
- What: After the pair `(a_n, b_n)` the whole pipeline is independent of which zeta one is doing. The proposal (milestone M3) is a single C struct carrying atoms `w_k delta(y - y_k)`, exponential-series kernels `sum_k P_j(k) e^{-(d_j k + mu_j)x}`, rank-one pole terms, and a scalar shift, with `deg P <= 2` sufficing for Riemann, Dirichlet, Dedekind, Hecke, GL(2), Ihara, Artin-Schreier/Weil and Selberg alike. The archimedean constants must be *derived* once from the regularisation, never typed in per case — explicitly flagged as the one place in the plan where a derivation rather than a transcription is required, and the gate on every extension. The discrete instance was built separately as `ihz_weil_t` (integer-length atoms, trivial-divisor poles, `W_R` as a geometric kernel with `d = 1`, `mu = log q/2`, `P = 1`) and should become a constructor of the general type. Dirichlet characters are a small step with one striking consequence: the conductor is invisible to the spectrum, entering only through the atoms and an identity shift.
- Lead: implement `zst_weil_ab` once and every new L-function becomes a data builder, not a new pipeline; then a graded transfer channel or cMPS generator defined in the notebook could be run through certified code without new code being written. The named entry point for Hecke is `conj:weil-lps-hecke`, which supplies concrete weight-2 forms of level `p` to feed in.
- Where: `notes/zeta-spectral-triples/plan.md:36-38,213-247,366-371,402-404`; `ihara/plan.md:305-321,403-405`

### G4-T8-1 The graph has no Weil-style explicit formula in the literature, and the "gamma factor" reading is ours
- Absorbs: L09-054, L09-055
- Class: PARTIAL
- Raised by: subagent
- What: The literature lane read Horton-Stark-Terras, Stark-Terras III and Terras-Wallace in full and found no explicit formula with general test-function pairs for graphs — only a prime number theorem and a pole-location "RH" — and also no paper on "spectral reconstruction from closed walks". Meanwhile `IH-3` writes exactly such a formula, `Psi_X(F) = W_C(F) - W_{0,2}(F) - W_R(F)`, in CCM's own shape (though it is a finite rearrangement of `Tr B^k`, not an analytic theorem). Alongside it, `IH-5` proves that `W_R` is exactly the log-derivative contribution of `(1-u^2)^{|E|-|V|}`, the factor that produces a clean functional equation, and reads that factor as a graph "gamma factor" on three grounds — geometric-series atoms `c s^{|k|}` with `s = q^{-1/2}` mirroring `rho(x) = sum e^{-(2n+1/2)x}` with the same leading exponent `1/2`, the topological multiplicity `-chi(X)`, and its position strictly inside the critical circle. The naming is unverified and appears to be the notebook's own.
- Lead: what is missing is a statement identifying `(1-u^2)^{r-1}` with an archimedean local factor in a motivic sense. Made precise, `IH-3` plus that reading is a small, self-contained, publishable "explicit formula for the Ihara zeta in Weil's shape", which the lane's own search says does not exist.
- Where: `ihara/lanes/literature.md:136-149,618-622`; `ihara/lanes/theory.md:90-117,137-159`

### G4-T8-2 `U''` is a CMV/paraorthogonal object and the OPUC toolkit is sitting unused
- Absorbs: L09-053
- Class: LEAD-unpursued
- Raised by: subagent
- What: `U''` is a rank-one perturbation of the shift, unitary for the `T`-inner product, with self-reciprocal characteristic polynomial when `xi` is even — that is the definition of a paraorthogonal polynomial, and the corresponding matrices are the truncated GGT/CMV matrices. The free unimodular parameter `beta` of the over-resolved regime is exactly the paraorthogonal parameter. Simon's `math/0606037` proves the statement matrix-first via rank-one perturbations of unitaries, and both it and Cantero-Moral-Velazquez `math/0204300` are already fetched.
- Lead: the OPUC machinery (Verblunsky coefficients, Szego recursion, the CMV five-diagonal form) is then available for the graph case and, through the unitary key lemma, potentially for the Selberg case. Nobody has tried to use any of it.
- Where: `ihara/lanes/theory.md:606-613`; `ihara/lanes/literature.md:317-384`

### G4-T8-3 Verification gaps, unfetched sources, and one typo in CCM
- Absorbs: L09-003, L09-073, L09-081, L09-085
- Class: PARTIAL
- Raised by: subagent
- What: Unverified from primary text are Ihara 1966's original statement, **Terras 2011's book content** (called "the single biggest gap" — the explicit-formula/RH chapter was never confirmed), Pisarenko 1973, **Makhoul 1981's exact hypotheses** (the wording in use is already a secondary paraphrase, and its "if distinct" clause needs checking against the actual small-window Weil matrices), Delsarte-Genin-Kamp, Cantoni-Butler 1976, Simon's OPUC theorem number, and two arXiv-id questions. Six arXiv ids were staged for `refs/fetch_sources.sh` and the fetch was outside the lane's write scope. One named unfetched paper matters most: Connes-Consani arXiv:2006.13771, "Weil positivity and trace formula, the archimedean place", which expresses the difference between the Weil distribution and the Sonin trace for the single archimedean place in terms of prolate functions and Hermitian Toeplitz matrices — very likely the paper that first connects Weil positivity to this machinery, and whose "single place" framing is the closest existing analogue of a one-prime window. Also recorded: CCM's displayed constant `c(L)` is a typo — the identity they use needs `C(L) = int_0^L (1 - e^{-x/2}) rho(x) dx = 0.575`, not `0.352`; the difference is `n`-independent so it moves `eps_N` by about `0.45` but leaves `xi` and the spectrum untouched, and their numbers come from the correct constant. A documentation convention was adopted for `ihz` because the Ihara-Bass ground truth is spread over Bass 1992 (not on arXiv) and a Terras book: cite this repo's own `report/sections/02_definitions.tex` and `08_quantum_ihara_general.tex` by line.
- Lead: fetch 2006.13771 before finalising anything about single-place windows; and check Makhoul's hypotheses, since the graph's Weil form is real symmetric, so after the sign flip it is Makhoul's max-and-min statement, not Caratheodory-Fejer's, that applies. Note the side effect of the citation convention: `ihz`'s ground truth is only as good as the notebook's own `stipulated` rows.
- Where: `ihara/lanes/literature.md:547-561,708-724`; `code-audit.md:554-564`; `notes/zeta-spectral-triples/plan.md:163-171`

### G4-T9-1 H-CUSP-BRIDGE: the single named gap between the Selberg machinery and a Riemann statement
- Absorbs: L09-015, L10-019, L16-026, L17-002
- Class: PARTIAL
- Raised by: TJO
- What: The modular scattering zeros sit at `s = rho/2`; if they were geodesic first-band resonances the flow exponent would be `lambda = rho/2 - 1`. The compact Haar-pairing proof is unavailable because the Eisenstein Laurent coefficients are outside `L^2`: at a scattering pole the first-band state is the leading Laurent coefficient of the Eisenstein series, which has a nonzero `y^{1-s_0}` constant term. Truncated Maass-Selberg norms are positive throughout `0 < Re s_0 < 1/2`, not only on the critical line, and their growth in the truncation height `Y` is exactly the missing Haar integrability — so truncation positivity is not the RH coercivity. TJO's own steering ("I want to understand precisely why Riemann is different to Selberg here") launched two lanes on exactly this. The missing object is stated concretely: a noncompact flow-resolvent realisation with finite-rank resonant data at `s_0 - 1`, a multiplicity-preserving first-band pushforward to Eisenstein Laurent data, and a compatible positive pairing; nothing in the compact DFG material supplies it.
- Lead: there is also a purely computational form. If the CCM data model reached the Selberg case (atoms at `k l(gamma)` with weights `l(gamma_0)/(2 sinh(k l/2))`, identity kernel `(Area/4 pi) sum_k k e^{-kx}`, plus the parabolic digamma kernel and the cusp comb atoms `Lambda(n)/n` at `2 log n`), then whether one self-adjoint operator built from prime geodesics plus the cusp comb reproduces both the Maass `r_j` and the `gamma_n/2` is a computational form of H-CUSP-BRIDGE. Geodesic data is sparse for small windows, so this needs the scaling work first.
- Where: `notes/rh-strategy-2026-09-19/cusp-bridge.md:7`; `notes/selberg-letters/astra-proofs.md:358`; `notes/zeta-spectral-triples/plan.md:396-401,434-441`

### G4-T9-2 Even under RH the Riemann scattering Laplace parameter is nonreal — the sharpest Riemann/Selberg difference
- Absorbs: L10-004, L10-073, L10-075, L10-098
- Class: EXPLORED-negative
- Raised by: subagent
- What: At `s = 1/4 + i gamma/2` the Laplace parameter is `mu = s(1-s) = 3/16 + gamma^2/4 + i gamma/4`, nonreal for every nonzero `gamma`. So proving the Selberg `mu >= 1/4` gap cannot turn Riemann scattering modes into self-adjoint Laplace eigenfunctions: the Eisenstein Laurent eigenfunctions grow like `y^{1-s}` and are outside `L^2`, and on the truncated fundamental domain the surviving cusp boundary term `|c|^2 (1-s) Y^{1-2 sigma}` exactly balances the imaginary part (`Im(mu)||f||^2 = eta |c|^2 Y^{1-2sigma} + o(1)`) — dropping it would manufacture a false reality proof. By contrast compact first-band modes satisfy `lambda = -1/2 +- sqrt(1/4 - mu)` and self-adjointness gives either the vertical `-1/2` line or the real interval `[-1,0]`, with a possible Jordan block exactly at `mu = 1/4`. A related conceptual correction: hyperbolicity is not itself a Lindblad emission process — the Liouville measure is preserved, and the dissipation in the physical picture comes from the *cusp boundary*, not from the flow.
- Lead: stop looking for a self-adjointness argument in this sector; look instead for an arithmetic rigidity of resonance widths. This rules out a whole family of "make it self-adjoint" strategies.
- Where: `notes/rh-strategy-2026-09-19/SYNTHESIS.md:24-28`; `riemann-vs-selberg-operators.md:17-18,34-42`; `riemann-vs-selberg-cmps.md:128`

### G4-T9-3 The Cauchy Gram of Eisenstein Laurent states, its one-exit identity, and why it does not select RH
- Absorbs: L10-005, L10-023, L10-024, L10-026, L10-048, L10-076
- Class: EXPLORED-registered
- Raised by: subagent
- What: Normalized by `c_i Y^{1/2 - s_i}`, the leading truncated Eisenstein Laurent states have exactly the Cauchy Gram `K_ij = 1/(1 - conj(s_i) - s_j)`, and with `C = diag(s_i - 1/2)` one gets the finite one-exit dissipativity identity `C*K + KC = -11*`. Equivalently `K` is the Gram of the explicit output functions `g_i(t) = exp(C_i t)`, the map into `L^2(0, inf)` is an isometry, the modal semigroup becomes left translation, and `d/dt ||exp(tC)v||_K^2 = -|sum_i exp(tC_i)v_i|^2`: stored energy equals future emitted energy, decay is energy leaving through one channel — and none of this depends on RH. The same normalized states map isometrically to Hardy kernels `k_i(x) = 1/(x - conj(tau_i))`, an explicit isometry of finite modal spans that holds even for hypothetical off-line zeros. Three negatives follow. The Gram is positive definite for arbitrary distinct parameters in the whole strip, so it does not select RH. The naive Hadamard finite-part pairing leaves the **zero matrix**, because every denominator `1 - s_i - conj(s_j)` has positive real part. And even under RH the centered flow cannot be unitary in this norm for `N >= 2`, since `(A + 3/4)*K + K(A + 3/4) = (1/2)K - 11*` pits a rank-`N` term against a rank-one one; generic exit positivity instead gives modal width `1/2 + |1|^2/(2 G_ii)`, a mode-dependent extra escape term present throughout the strip.
- Lead: use the identity as the normalization target and debugging oracle for any proposed arithmetic exit map, and stop re-proving positivity of this Gram — the task is to isolate a prime-defined mechanism fixing the exit-to-storage ratio, or compensating the extra escape via correlated return amplitudes. Different pairings, subleading Laurent data and nonlocal boundary terms remain open.
- Where: `notes/rh-strategy-2026-09-19/cusp-bridge.md:26-30,34-54,68-74`; `riemann-vs-selberg-operators.md:46-58`; `positivity-products.md:120-124`

### G4-T9-4 The flow-to-wave intertwiner `WT = TC`, with Bonthonneau-Weich and Uetake as the two endpoints
- Absorbs: L10-013, L10-014, L10-015, L10-025, L10-072, L10-074, L10-078, L10-080, L10-087, L17-022
- Class: PARTIAL
- Raised by: subagent
- What: The "half shift" is a change of generator, not of clock: for Laplace parameter `s(1-s)` the wave exponents are `q = +-(s - 1/2)`, so the decaying outgoing branch is `q = s - 1/2` while geodesic first-band bookkeeping is `lambda = s - 1`, hence `q = lambda + 1/2`; in the cusp, with `r = log y` and `u_0 = y^{1/2} v(r,t)`, the wave equation becomes `v_tt = v_rr`, free escape down the cusp. That gives a concrete map instead of a spectral coincidence: if a first-band Poisson pushforward `P` satisfies `Delta P = -P(A^2 + A)` with `A = -X`, set `C = A + 1/2` and `T u = (Pu, PCu)`; block multiplication against `W = [[0, I],[1/4 - Delta, 0]]` gives `WT = TC` directly. The two endpoints exist and are verified. Bonthonneau-Weich (arXiv:1712.07832, cached) give a globally meromorphic flow resolvent with finite-rank residues covering cofinite Fuchsian orbifolds including `PSL(2,Z)`, but their own text says the identification with discretized transfer spectra and the first band is future work. Uetake 2007 (Ann. Polon. Math. 92, DOI 10.4064/ap92-2-1, cached PDF) supplies a factored modular Lax-Phillips generator with causal scalar factor `F(p) = xi(2p)/xi(-2p)`, whose Theorem 4.4 says the eigenvalues of `-2A_c` are the nontrivial zeros with algebraic multiplicity and that the imaginary spectrum of `2A_c + 1/2` is exactly RH, plus Section 5 explicit automorphic boundary profiles. Three cautions attach: read Uetake's "basis" conservatively as the completeness actually proved in 4.2 (no Riesz bounds), do **not** import `dom(A_c) = dom(L) ∩ K` (a compressed half-line translation generator allows nonzero boundary traces), and declare BW's time-reversal convention before mapping their `s` to the repo's `lambda`. A live search for a cusp first-band/Eisenstein theorem found only compact and convex-cocompact results — a search limitation, not a no-go.
- Lead: prove the four analytic conditions — (a) the BW pole exists with the claimed finite multiplicity; (b) `P` matches the Eisenstein Laurent chain injectively; (c) `T` satisfies the outgoing cusp asymptotics; (d) the LP regular-data projection preserves chain length. That would derive the shift at operator level and join two established resonance pictures **without using RH**. Also read Uetake's Theorem 6.3 (an RH-equivalent cyclicity condition) and ask whether its augmentation is arithmetically natural; his Poincaré-series profiles are the only non-zero-defined test data available.
- Where: `riemann-vs-selberg-operators.md:26,72,84-96,150-156,178`; `refs/src/1712.07832/preprint.tex:143-172`; `refs/src/uetake-2007/paper.pdf`

### G4-T9-5 Which observable, which width: four numbers for the same zeros
- Absorbs: L10-003, L10-022, L10-077, L10-083, L10-084
- Class: EXPLORED-registered
- Raised by: subagent
- What: Four distinct experiments give four distinct widths for the same zeros. (1) Geodesic correlation: poles of the Laplace transform of `<f ∘ flow_t, g>`, with the Riemann subset at `lambda = rho/2 - 1`, width 3/4 under RH — and only after the missing identification. (2) Automorphic wave escape: `q = s - 1/2`, width 1/4, realized by Uetake's factored LP semigroup. (3) Bond/cMPS coherence: amplitude rate `b = -conj(rho)/2`, width 1/4, but *population* survival of a single eigenmode has rate `2 Re b`, width 1/2 — coherence and population must not be conflated. (4) The stationary emitted field: the vacuum-exit realization has a pure absorbing vacuum with no ongoing output at all. The relabelling that connects them is `b = lambda' + 1/2` via the FE partner `rho' = 1 - conj(rho)`; the alternative same-label formula uses an adjoint/conjugate and reverses the sign, and conflating the two maps is dangerous. Two different `1/4`s also have to be kept apart: the one in `Delta - 1/4` is a geometric threshold / half-density correction, while "every arithmetic scattering pole has `Re q = -1/4`" is extra arithmetic information. And the Riemann FE gives the symmetry `s' = 1/2 - conj(s)` about `Re C = -1/4`, but `phi(s)phi(1-s) = 1` exchanges poles and zeros and does not impose it on one pole set — reflection alone permits eigenvalues off the axis, exactly as a functional equation permits off-line zeros.
- Lead: state which observable is meant before quoting any width, and fix one relabelling convention repo-wide. The "same 1/4" language in older shards is ambiguous without this, and the three candidate centres (-1/2 Selberg, -3/4 flow, -1/4 model) belong to three different operators.
- Where: `riemann-vs-selberg-operators.md:64,120-125,144-146`; `notes/rh-strategy-2026-09-19/cusp-bridge.md:24`; `SYNTHESIS.md:13-22`

### G4-T9-6 Two repository corrections recorded and deliberately not yet applied
- Absorbs: L10-016, L10-027, L10-079, L17-011
- Class: EXPLORED-registered
- Raised by: subagent
- What: (1) `report/sections/04_riemann_channel.tex:71-75` and `notes/riemann-channel-note.md:59-64` write `Z(t)* k_lambda = exp(-it conj(lambda)) k_lambda` and call it decaying; substituting `lambda = gamma/2 - i beta/2` gives the real exponent `+beta t/2`, i.e. growth. The correct formula for the defined lower-half-plane compression is `Z(t) k_lambda = exp(it conj(lambda)) k_lambda`, generator eigenvalue `-conj(rho)/2`, consistent with shard 04b:249-252; numerically at `beta = 1/2, t = 1` the old modulus is `exp(1/4)` and the corrected one `exp(-1/4)`. The proof is elementary: in `H^2(C_-)` multiplication by `exp(-itz)` is contractive for `t >= 0` and reproducing kernels are eigenvectors of its adjoint. Two lanes found this independently. (2) The entire-xi scattering symbol differs from the raw Eisenstein coefficient by a rational factor: `S(tau) = [(2i tau - 1)/(2i tau + 1)] phi(1/2 + i tau)`. Uetake's original LP scattering matrix (p.110) is `-[(p - 1/2)/(p + 1/2)] F(p)` with an extra generator pole at `p = -1/2`, and his alternative convention (p.116) is `F(p)(1/2 + p)/(1/2 - p)`; they agree on the nontrivial arithmetic modal set after the stated transformations but are not interchangeable as whole symbols.
- Lead: apply both under the repo's review discipline — the evidence is already there twice over. Both matter as soon as one constructs an operator rather than matching a scalar pole set.
- Where: `notes/rh-strategy-2026-09-19/cusp-bridge.md:64,76`; `riemann-vs-selberg-operators.md:20,74-78`; `2026-09-19T11-22-06.txt:80`

### G4-T9-7 The cusp prime comb: negative atoms, a `+1/2` boundary constant, and an identity of measures only
- Absorbs: L10-021, L14-004, L14-005
- Class: EXPLORED-registered
- Raised by: prover
- What: The orchestrator drafted the modular cusp term as `C(t) = sum_{n>=2}(Lambda(n)/n)[delta(t - 2 log n) + delta(t + 2 log n)] + A(t)` with positive weights and asked only for the sign convention. The prover found the stated scattering multiplier gives **negative** prime peaks (the primes are dips), and then a further term the brief did not anticipate: the `r = 0` calculation adds a `+1/2` constant to the archimedean distribution, coming from `q(1 + 2ir) + q(1 - 2ir)` differing from its right-Abel boundary distribution by `+pi delta_0(r)`. More important is the qualification the prover attached: the notebook's claim that the full compressed-semigroup trace is a pure prime comb "needs qualification — I can prove the requested damping identity for the stated prime measures, but that alone does not establish an identity of full operator traces". The cusp-bridge lane says the same from the other side: the damping identity implies no operator identification and any proposed affine bridge must supply an intertwiner on regular/resonant data, not infer it from the prime weights.
- Lead: closing the gap needs either a genuine trace-class statement for `Z(t)` — which the later riemann-cmps session shows is impossible, since an infinite eigenvalue list precludes compactness — or a regularised trace with a stated regularisation. If closed, the cusp term of the modular trace formula would literally *be* the damped Riemann channel rather than merely share its prime weights.
- Where: `2026-09-12T12-54-39.txt:83,111,115`; `report/sections/09c_selberg_tower_cusp.tex:122-138`; `notes/rh-strategy-2026-09-19/cusp-bridge.md:11`

### G4-T9-8 What the Selberg-letters prover lane corrected
- Absorbs: L16-019, L16-021, L16-022, L16-025
- Class: EXPLORED-negative
- Raised by: prover
- What: Four corrections to the drafted Selberg material. (i) The obvious construction — the full transverse exterior algebra and its flat supertrace — gives the Ruelle zeta `zeta_R(s) = Z_S(s)/Z_S(s+1)`, whose retained zeros and poles occupy **two bands shifted by one unit**, so reflection about the midpoint sends one band where no band exists and the single-line Ramanujan condition is unsatisfiable for any surface; the fix is the two-term transverse complex (even generator `A = -X`, odd generator `A + 1`) which gives `Z_S` directly. (ii) The drafted positive form (pull back the surface `L^2` product through the pushforward) is degenerate: the two resonances `lambda_+ = s_+ - 1` and `lambda_- = s_- - 1` attached to one Laplace eigenvalue push forward to the *same* eigenfunction, so their difference is in the kernel; a positive form needs separate orthogonal copies per branch. The same degeneracy appears in the finite Hashimoto case, where the untagged metric `<Ru, Rv>` has exactly the differences of partner lifts as kernel. (iii) `lambda_1 >= 1/4` is a **theorem** for the full modular group `PSL_2(Z)`; what is open is the Selberg eigenvalue conjecture for congruence subgroups. (iv) The reflection heat supertrace is not an ordinary trace and needs its own definition (regularisation, weight, or flat trace); and taking the weight down to 1 in `D_k^+ ⊗ D_k^{+/-}` requires a covering group of `PSL_2(R)` or a projective representation — the naive limit does not exist inside `PSL_2(R)`.
- Lead: count the bands before asking for RH — a graded zeta with two shifted bands can never have a single critical line, and this is a one-line structural test applicable to every candidate in the notebook. Write any "positive form from a pushforward" branchwise from the start. When citing "Selberg 1/4" as hypothesis H-COERC, say for which group.
- Where: `2026-09-16T14-21-08.txt:199-201,266-268`; `notes/selberg-letters/astra-proofs.md:367,385`

### G4-T10-1 The target, and the gap in one sentence
- Absorbs: L10-001, L10-017, L17-001, L17-004
- Class: PARTIAL
- Raised by: TJO
- What: The stated research target is to construct prime-defined, graded cMPS letters and a physical field correlation whose observable decay modes are exactly the Riemann zero divisor, deriving their common width from those letters, with a stationary arithmetic bond and a controlled infinite limit. TJO's own steering during the session was normative, not descriptive: "decay modes is the crucial unlock in my opinion; the cMPS interpretation *ought* to be the physically natural setting to represent decay modes correctly", plus a demand that all agent work be written continuously and two extra lanes on why Riemann differs from Selberg. The orchestrator's compact statement of where the programme stands, which appears in no final file: "the repository can represent zeros as decay modes, but it has not found an arithmetic reason forcing equal decay rates". Representation is solved; rigidity is not.
- Lead: build the letters from primes, compute the physical two-point function, read off the divisor. The letters must come first and the zeros must come out, never be inserted.
- Where: `notes/rh-strategy-2026-09-19/SYNTHESIS.md:7`; `SESSION.md:7`; `2026-09-19T11-20-25.txt:99,143`

### G4-T10-2 Uniform width = uniform exit energy per stored modal energy — and keep it modal
- Absorbs: L10-006, L10-047
- Class: EXPLORED-registered
- Raised by: subagent
- What: For a passive realization `A*G + GA = -C*C` with `Av = lambda v`, one has exactly `-Re(lambda) = ||Cv||^2 / (2 <v, Gv>)`. So proving `||Cv||^2 = 2 kappa <v, Gv>` for every retained resonant mode would force width `kappa`; this needs neither normality of `A` nor simplicity of the zeros. The stronger identity `C*C = 2 kappa G` on the whole retained state space yields `A*G + GA = -2 kappa G`, metric skew-adjointness after centering, which in finite dimension excludes Jordan blocks — and because Weil positivity is blind to Jordan blocks, that full identity is strictly **stronger** than divisor RH.
- Lead: construct `C` and `G` arithmetically and prove the *modal* equality only. Recorded warning: defining them from already-centered real zero frequencies is circular.
- Where: `notes/rh-strategy-2026-09-19/positivity-products.md:98-118`

### G4-T10-3 Nonnormality is necessary, not a defect
- Absorbs: L10-007, L10-033
- Class: EXPLORED-registered
- Raised by: subagent
- What: With one exit of rank one and `N >= 2` modes all of width 1/4, the generator `B` cannot be normal — its Hermitian part would have to be `-(1/2)I`, of rank `N`, contradicting the rank-one exit. Individual eigenmodes each have one lifetime; coherent superpositions need not, and demanding centered unitarity in the *physical* norm would wrongly exclude this physically natural possibility. This is a genuine correction to earlier repo instinct, found by the cusp lane and cross-checked by the graded-channels lane.
- Lead: seek a *second*, arithmetic positive form that orthogonalizes the modes, rather than demanding that the physical transfer become unitary after rescaling. Proving that form from non-spectral data is the RH-sized step, and it separates "divisor on the line" (RH) from "unitarizable semigroup" (strictly stronger).
- Where: `notes/rh-strategy-2026-09-19/cusp-bridge.md:92,124`; `riemann-vs-selberg-operators.md:66,146`

### G4-T10-4 Any positivity claim must be sensitive to the line
- Absorbs: L10-020, L10-036
- Class: EXPLORED-registered
- Raised by: subagent
- What: An existence claim for "some positive metric" is not evidence of a mechanism. The compact branchwise positive form yields unitary centered flow only if the extra Selberg 1/4 coercivity holds, and its full algebraic block fails at a Jordan threshold; and the Cauchy Gram is positive definite for arbitrary distinct parameters in the whole strip, so it does not select RH. Of the eleven rows of the cusp lane's claim-status ledger, ten are reviewed repo results, checked deductions or numerical checks; the single "Open / RH-equivalent" row is "positive centered metric from arithmetic input — the unresolved arithmetic mechanism".
- Lead: demand that any positivity claim be *sensitive* to the line — construct a positive form that fails for off-line parameters, or admit it is only normalization.
- Where: `notes/rh-strategy-2026-09-19/cusp-bridge.md:9,42,112-127`; `03e_selberg_letters.tex:144-178`

### G4-T10-5 The letter-generated Krylov basis carries an explicit rational positive invariant metric
- Absorbs: L10-065
- Class: EXPLORED-registered
- Raised by: subagent
- What: In the `2|2` toy, the source Krylov space `span{L_eta^k(R sigma)}` and the sink-observable space each have dimension four. With `A = L_eta|_odd`, `K = A + I/4` and `v = R sigma`, the companion form `K_comp = [[0,0,0,-9/256],[1,0,0,0],[0,1,0,-11/8],[0,0,1,0]]` admits the positive definite `G = [[10496/27,0,-32/3,0],[0,32/3,0,-1],[-32/3,0,1,0],[0,-1,0,1]]` with `K_comp*G + G K_comp = 0`, checked by principal minors. The point is that this metric is constructed on a space generated by physical letters and a field insertion — no eigenvectors and no zeta frequencies are assigned — and it is *not* the physical Hilbert-Schmidt norm, exactly as the cusp lane's nonnormality warning requires.
- Lead: this is the concrete instance of the "second arithmetic positive form" the programme needs. The recipe is reusable: build the Krylov space from the physical insertion, reduce to companion form, solve the linear Lyapunov system for an invariant form, test positivity by minors — the positivity, not the existence, is the content.
- Where: `notes/rh-strategy-2026-09-19/graded-channels.md:110-118`

### G4-T10-6 The minimal missing identity, stated cleanly
- Absorbs: L10-068
- Class: LEAD-unpursued
- Raised by: subagent
- What: For independently specified local/arithmetic letters there must be a positive form `G` on the *observable* odd realization with `A_obs*G + G A_obs = -(1/2)G`, together with an input/output divisor identity tying precisely these poles — including their algebraic multiplicities — to the Riemann zeros under `b = -conj(rho)/2`. The finite toy supplies the first half in finite dimension and supplies no arithmetic divisor identity at all. Prime-dependent coefficients may not be fitted to known zero positions.
- Lead: this is the cleanest single statement of what would have to be proved, and it is the sentence any future construction should be measured against.
- Where: `notes/rh-strategy-2026-09-19/graded-channels.md:126`

### G4-T10-7 The two-state passive toy: CP, passivity, one channel and the FE together do not force a common width
- Absorbs: L10-081, L10-082, L10-092
- Class: EXPLORED-negative
- Raised by: subagent
- What: Take `j = (sqrt(2g), 0)`, `H = [[0,w],[w,0]] - Omega I`, `B = -iH - (1/2)j*j`, giving `b_+- = -g/2 + i Omega +- sqrt(g^2/4 - w^2)`. At `g = 1/2` the centre is exactly `-1/4` with FE symmetry `b -> -1/2 - conj(b)`, and there is a CPTP vacuum cMPS completion for every real `w`. But `w > 1/4` gives both widths 1/4 (underdamped); `0 < w < 1/4` gives two distinct widths summing to 1/2, both inside the strip (at `w = 1/8` exactly `1/4 +- sqrt3/8`); and `w = 1/4` gives equal widths with a nonzero nilpotent, a Jordan threshold with `t exp((-1/4 + i Omega)t)` matrix elements. The cMPS lane produced the same negative from the letters side: at `a = c = 1/20, b = 0, d = 1/2` the reflection survives but the discriminant is exactly `-2399/10000` and the widths are about 0.0060754 and 0.4939246. The toy can also be written as an effective PT-symmetric Hamiltonian after centering, and PT alone permits both regimes.
- Lead: the constructive hint is that a letter-defined coercive coupling theorem could force the underdamped regime, just as a spectral-gap inequality selects the Selberg branch — the scalar inequality `w > g/2` is exactly what is missing for the modular boundary operator. And RH would read as "PT unbroken" for the arithmetic operator; the PT literature has actual techniques for proving unbroken regimes, and this connection was raised in one sentence and dropped.
- Where: `riemann-vs-selberg-operators.md:102-116`; `riemann-vs-selberg-cmps.md:92,114`

### G4-T10-8 Multiple zeros are allowed, and Jordan blocks are invisible to the usual bounds
- Absorbs: L10-085, L10-108, L10-118
- Class: EXPLORED-registered
- Raised by: subagent
- What: Model-space positivity accommodates multiplicity: RH alone allows polynomial-times-exponential decay, while centered skew-adjointness would additionally impose semisimplicity and is strictly stronger; three lanes recorded this independently. Shang's reset Lindbladian gives an explicit instance — with `A = diag(1, 1/3)`, `b = (cos th, sin th)` at `th* = 0.49088...`, the eigenvalue `-1/9` has algebraic multiplicity 3 and geometric multiplicity 2, and the uniform trace-distance mixing bound simply does not see it, absorbing `t e^{-t/9}` into constants — the same moral as "Weil positivity is blind to Jordan blocks". Becker-Zworski's bound cuts the other way at one point only: a Jordan block at the slowest rate whose generalized eigenvector lies in the admissible class would force a `t e^{-gamma t}` term and is therefore ruled out — for the extreme rate alone.
- Lead: never let a construction quietly assume simple zeros. A mixing-time formulation of RH would be blind to multiple zeros, which is either a feature or a sign that it is the wrong formulation; an RH decay bound on a regularity class rules out Jordan blocks only at the extreme rate, and that should be stated precisely.
- Where: `riemann-vs-selberg-operators.md:142`; `notes/extract/2609.12284-reading.md:125-131`; `notes/extract/2609.13121-reading.md:109-111`

### G4-T10-9 Lemma target: the modewise cusp leakage estimate `||jv||^2 >= (1/2)||v||^2`
- Absorbs: L10-086, L17-024
- Class: LEAD-unpursued
- Raised by: subagent
- What: On a common dense core with a genuine trace map `j` and a physical energy norm satisfying `2 Re<v, Bv> = -||jv||^2`, an eigenmode gives `-2 Re(b) = ||jv||^2/||v||^2`. The needed arithmetic input is the *modewise* estimate `||jv||^2 >= (1/2)||v||^2`, derived from automorphic cusp matching **before knowing zero locations**; combined with the FE pairing `b -> -1/2 - conj(b)` it forces equality and width 1/4. The quantifier is the whole point: demanding the bound for *every* vector of a finite modal span is impossible for a one-row `j` above dimension one, so "find a scalar dissipator" is the wrong target. Neither bare cyclicity of the minimal model nor generic positivity can prove it, since both hold for the unequal-width toys.
- Lead: Uetake's Section 5 Poincaré-series profiles supply non-zero-defined test data with which to attempt it. This is the sharpest quantifier-correct statement of the RH-sized inequality in the whole group.
- Where: `riemann-vs-selberg-operators.md:158-170`; `2026-09-19T11-22-16.txt:91`

### G4-T11-1 Individual prime-power blocks are indefinite
- Absorbs: L10-008
- Class: EXPLORED-negative
- Raised by: subagent
- What: One prime power `n = p^k` contributes `Delta K_a(t,u) = w[h_a(t-u) - h_a(t) - h_a(u)]` with `w = Lambda(n)/sqrt n`, `a = log n`. On the two nodes `A, -A` with `a/2 < A < a` this is `w(2A - a)[[0,1],[1,0]]`, eigenvalues `+-w(2A - a)` — indefinite at its first visibility.
- Lead: any positivity proof must use correlated cross-prime/archimedean compensation or a nonlinear update; there is no sum-of-independent-positive-prime-blocks ansatz. This does not refute positivity of the total kernel.
- Where: `notes/rh-strategy-2026-09-19/positivity-products.md:24-32`

### G4-T11-2 The increment Toeplitz reformulation and the sought sign-controlled Schur recurrence
- Absorbs: L10-040, L10-042, L10-043, L10-046
- Class: PARTIAL
- Raised by: subagent
- What: The differences `d_j = v_{j+1} - v_j` have Toeplitz Gram `c_h(m) = Psi((m+1)h) + Psi((m-1)h) - 2 Psi(mh)`, congruent to the screw Gram by an invertible matrix, so the PSD conditions are exactly equivalent — and each prime power with `a/h = L + theta` contributes only at `m = +-L` (weight `-w h (1 - theta)`) and `m = +-(L+1)` (weight `-w h theta`), i.e. at most four diagonals, with trigonometric polynomial `-2wh[(1-theta)cos(Lx) + theta cos((L+1)x)]`. It also reduces repeated `Psi` evaluations from quadratic to linear in grid size. Numerically at mesh `h = 1/4`, `A = 2` gives min eigenvalue 0.0210158467482652494 for `K` and 0.000747659951048785 for the increment Toeplitz; `A = 4` gives 0.0146176837661784046 and 0.000375484666271565, agreeing to 32 digits at 40 and 70 decimal digits — and the small positive increment eigenvalue warns against seeking a mesh-independent lower bound. Suzuki's screw kernel is the underlying object; finite-interval positivity is insufficient and unconditional on small intervals, and the existing numerical Cholesky factors are a discovery aid only.
- Lead: derive a sign-controlled innovation/Schur recurrence for the **sum** of archimedean and sparse prime Toeplitz pieces — that is the new structure. Stop sign attached: Suzuki already proves `Psi(t) >= 0` for all real `t` is equivalent to RH and `Psi = O(1)` iff RH, so replacing matrix positivity with scalar positivity is not progress.
- Where: `notes/rh-strategy-2026-09-19/positivity-products.md:18,38,58-92,140`; `refs/src/2206.03682/screwz_15.tex:400-425`

### G4-T11-3 A two-line diagnostic for any claimed sum-of-squares factorization
- Absorbs: L10-041
- Class: LEAD-unpursued
- Raised by: subagent
- What: For the full even `Psi` with `Psi(0) = 0`, the two-node matrix at `A, -A` has eigenvalues `Psi(2A)` and `4Psi(A) - Psi(2A)`. That makes the cancellation mechanism visible before any large Gram matrix is built.
- Lead: apply it to any candidate factorization before scaling up. Mentioned once, never used.
- Where: `notes/rh-strategy-2026-09-19/positivity-products.md:36`

### G4-T11-4 Amplification: the fixed-loss lemma, why ordinary tensoring fails, and the missing projector
- Absorbs: L10-037, L10-038, L10-039, L10-044, L10-045, L10-053
- Class: EXPLORED-negative
- Raised by: subagent
- What: A conditional reduction exists: if for each `k` an arithmetic product gives a scalar meromorphic response `R_k` with (1) survival of `k lambda` as a genuine pole for every centered retained `lambda`, (2) `R_k` the Laplace transform of `r_k` with `|r_k(t)| <= M_k(1+t)^{d_k} exp(epsilon_k t)` and `epsilon_k/k -> 0`, and (3) the same meromorphic continuation — then `k Re lambda <= epsilon_k`, so `Re lambda <= 0` and reflection gives `Re lambda = 0`. Crucially `M_k` may be exponential or worse; only the coefficient of `t` must be sublinear. No such product exists. Ordinary tensor powers give `epsilon_k = kc` and recover nothing; the Deligne tensor engine needs an independently controlled pole set and for ordinary graph transfer powers the interesting spectrum stays poles; Rosati positivity is not an independent proof because the constructed odd transfer already inputs the Frobenius moduli it would prove. What actually kills the Deligne loss in the finite-field case is not tensoring at all but **slicing over a one-dimensional base, which costs only one factor `sqrt q` independent of the tensor exponent**. And a tensor product can silently count a different object, or a supertrace can erase the pole one wants (the genus-two Jacobian/curve projector warning).
- Lead: find the analytic analogue of slicing — a product operation whose exponential growth loss is sublinear in tensor degree — and exhibit its projector. Testing the exponential loss, not the state-space dimension or prefactor, is the right early feasibility test.
- Where: `notes/rh-strategy-2026-09-19/positivity-products.md:15-17,42-52,160`; `07_deligne_via_graphs.tex:224-236`; `06f_ring_norm_genus_two.tex:213-221`

### G4-T11-5 The exact bridge specification, and its physical reading
- Absorbs: L10-049, L10-050
- Class: LEAD-unpursued
- Raised by: subagent
- What: With the Riemann no-event normalization `A` (modes `-conj(rho)/2`) and `B = 2A + 1/2` (centered modes `1/2 - conj(rho)`), define `V(t) = int_0^t exp(rB) b dr` for an arithmetic boundary distribution `b`. Establishing `<V(t), V(u)>_G = Psi(t) + Psi(u) - Psi(t-u)` from physical letters and prime/archimedean data — including the mixed `t,u` correlations — would make the right side a Gram kernel, so Suzuki would give RH; agreement only at `t = u` or at finitely many times is insufficient. `b` may be a distribution; it is `V(t)` that must have finite norm. The physical reading is that the Toeplitz entries are the Gram entries of finite time-bin amplitudes `V((j+1)h) - V(jh)`, and their Schur complements are the energy of the next output amplitude after projecting onto previously observed amplitudes — so prime-power contributions are not independent PSD channels and interference among physical histories and the archimedean sector is essential.
- Lead: its advantage is that it says which cMPS observable to calculate. Under RH the mode components are `(exp(i gamma t) - 1)/(i gamma)`, matching Suzuki's Eq_109 — but those components must not be used as the construction.
- Where: `notes/rh-strategy-2026-09-19/positivity-products.md:128-140`

### G4-T11-6 The prime kink no-go, packaged as a cheap stopping test
- Absorbs: L10-051
- Class: EXPLORED-negative
- Raised by: subagent
- What: `Psi'(a+) - Psi'(a-) = -log(p)/sqrt(p^k)` at each prime-power time `a = log(p^k)`, so `K(t,t) = 2 Psi(t)` has genuine first-derivative kinks. But for bounded `B` and a Hilbert vector `b`, `V(t) = int_0^t exp(rB) b dr` is entire, hence real-analytic on the diagonal. Every fixed finite-dimensional, time-homogeneous, bounded-generator cMPS amplitude model of this form is therefore excluded.
- Lead: calculate the jump at `log 2`; if a proposed exact prime-history model is analytic there, its bridge identity is impossible. An exact candidate needs an unbounded generator with a distributional boundary, explicit delay propagation at prime lengths, or another singularity mechanism.
- Where: `notes/rh-strategy-2026-09-19/positivity-products.md:144-152`

### G4-T11-7 The prime-side screw-kernel positivity test, whose script exists only in a transcript
- Absorbs: L14-029
- Class: PARTIAL
- Raised by: prover
- What: A check was written that builds Suzuki's screw function from the primes alone — `Psi(t) = 8(cosh(t/2) - 1) - sum_n (log p/sqrt n)(t - log n)_+ + t(psi(1/4) - log pi)/2 + (C - e^{-t/2} Phi(e^{-2t}, 2, 1/4))/4` with `C = pi^2 + 8G` — forms `K_ij = Psi(t_i) + Psi(t_j) - Psi(|t_i - t_j|)` on the grid `t_k = k/8`, and compares its eigenvalues with the Gram matrix built from 3000 cached zero ordinates; it also checks the delay identity `4 Re(xi'/xi)(1 + 2ix)` against a sum of Poisson kernels at width 1/4. The script exists only in the transcript; only its description survives as check 16.3.
- Lead: this is the notebook's one *prime-side* positivity test whose failure would be evidence against RH rather than an artefact. Turn it into a committed script with controlled truncation and cancellation error — the final note itself cautions that a failed Cholesky at floating point is not a negative Weil vector until those errors are controlled.
- Where: `2026-09-12T19-12-16.txt:138`; `notes/resonances/astra-freeassoc.md` (check 16.3)

### G4-T12-1 The relevant object is the observable odd *subquotient*, not the full odd transfer spectrum
- Absorbs: L10-002, L17-006
- Class: EXPLORED-registered
- Raised by: subagent
- What: The decay modes that matter may be only those visible to actual field insertions, not every eigenvalue of the odd transfer. A regular fermionic cMPS with a faithful mixed stationary bond naturally selects one decay band in a two-point function: the full odd transfer of the `2|2` toy has eight modes, the emitted-fermion two-point function has four. The orchestrator's reframing is the important part — instead of asking which operator has the zeros as eigenvalues, ask which *observable* has them as poles.
- Lead: for any candidate arithmetic channel, specify the field insertion first and compute the insertion-generated Krylov space and its observable quotient *before* any spectral numerics. If it works, the "extra" fast modes never need explaining away, and it explains how a channel can have extra fast modes without spoiling RH.
- Where: `notes/rh-strategy-2026-09-19/SYNTHESIS.md:9`; `graded-channels.md:108,118`; `2026-09-19T11-20-25.txt:286`

### G4-T12-2 The regular `C^(2|2)` fermionic cMPS and its exact observable closure
- Absorbs: L10-009, L10-010, L10-064
- Class: EXPLORED-registered
- Raised by: subagent
- What: Bond `C^(2|2)`, `P = Z ⊗ I`, one fermion letter `R = X ⊗ |0><1|`, `H = diag(aX + bZ, cX + dZ)`, `Q = -iH - R*R/2`. At `a = c = d = 1/2, b = 0` the fermionic two-point resolvent is exactly `8z(z^2 + z + 1)/[5(8z^4 + 8z^3 + 14z^2 + 6z + 1)]`, all four poles with real part `-1/4` and imaginary parts `+-(sqrt7 +- 2)/4`; the full odd transfer also has a band at width 3/4 that the field insertions simply do not see. The mechanism is structural, not a projector: with `w1 = X⊗X`, `w2 = X⊗Y`, `w3 = Y⊗I`, `w4 = X⊗Z` anticommuting Majoranas and `R = (w1 + i w2)/2`, the signed Heisenberg transfer `L_eta*(O) = Q*O + OQ - R*OR` preserves `span(w1..w4)` with an explicit 4x4 drift matrix — because the Hamiltonians in this family are quadratic in the Majoranas. The jump returns to active internal states rather than an absorbing vacuum: the emitted fermion resets the internal two-level system while flipping bond parity, giving a unique faithful stationary density (Schmidt weights ~0.0146, 0.0382, 0.2618, 0.6854, entropy 0.796154 nats), parity covariance, trace preservation, mixing and nonnegative ring supertraces at six lengths.
- Lead: treat this as the first controlled test case for a prime-defined analogue, and for arithmetic letters check closure of a finite generating family of odd observables under the correctly signed transfer before any spectral numerics. The slow band is a tangible candidate for the proper physical decay subspace; the fast band must be classified or cancelled by an actual trace identity, never discarded to fit RH. No zeta zeros and no projector were supplied anywhere in the construction.
- Where: `notes/rh-strategy-2026-09-19/graded-channels.md:73-82,86-108`; `riemann-vs-selberg-cmps.md:24-41`

### G4-T12-3 Three independent requirements: observable closure, reflection symmetry, independent coercivity
- Absorbs: L10-011, L10-088, L10-093, L10-094, L10-095
- Class: EXPLORED-registered
- Raised by: subagent
- What: On the observable space with `N = M + I/4`, a letter-derived involution `J = [0 0 -1 0; 0 0 0 1; -1 0 0 0; 0 1 0 0]` gives `JNJ = -N` with no diagonalization. Diagonalizing `J` (not `M`) puts `N` off-diagonal, and for `a > q = 1/4` the block product is self-adjoint in the positive metric `G = diag(a + q, a - q)`; minus it is similar to the real symmetric `S = [[(a-c)^2 + d^2 - 1/16, -2d sqrt(a^2 - 1/16)],[-2d sqrt(a^2 - 1/16), (a+c)^2 + d^2 - 1/16]]`, and the independent inequality `S >= 0` forces the common width. The elementary form of the criterion: with `b = 0`, all four modes have width 1/4 exactly when `alpha >= 0`, `beta >= 0` and `alpha^2 - 4 beta >= 0`, where `alpha = 2(a^2 + c^2 + d^2) - 1/8` and `beta = (a^2 - c^2 - d^2)^2 + (-a^2 - c^2 + d^2)/8 + 1/256`. This is a literal finite physical analogue of Selberg's quadratic relation followed by its Laplace spectral bound, and the output response `F(z) = tr[R*(z - L_eta)^{-1}(R sigma)]` has poles inside the explicit 4x4 `M` for *any* stationary `sigma`. None of the three requirements may be inferred from the other two.
- Lead: for arithmetic letters, supply `J` from arithmetic symmetries (not eigenvalue matching), then look for a sum-of-squares or boundary-flux proof of the analogue of `S >= 0`. The toy's 2x2 `S` is the complete model calculation for that step. The arithmetic analogue is a three-inequality condition, not a single one, and endpoint Jordan behaviour needs separate checking if a unitarizing metric is claimed.
- Where: `riemann-vs-selberg-cmps.md:62-92,106-116`; `SYNTHESIS.md:51-63`

### G4-T12-4 What breaks the toy: `bd != 0` splits the widths, a quartic term destroys the selection
- Absorbs: L10-012, L10-089, L10-090
- Class: EXPLORED-negative
- Raised by: subagent
- What: With `y = z + 1/4`, `det(zI - M) = y^4 + alpha y^2 - 2bd y + beta`. If all four poles have real part `-1/4`, reality of `M` forces the polynomial to be even in `y`, so **`bd = 0` is necessary** — and it is not implied by parity, CAR regularity, complete positivity or a faithful mixed stationary state. Concretely `b = 0.01` keeps everything and splits the widths to ~0.24622128 / ~0.25377872, exactly, via the centered linear coefficient `-2bd y`. Adding `0.01 P` to `H` is different in kind: it keeps grading and the stationary state but is a *quartic* fermion interaction, so it destroys linear observable closure and makes all eight odd poles visible, with output denominator of degree exactly eight and coprime numerator. Summary: mode selection is robust within the quadratic class, uniform widths require a symmetry plus a band inequality, and generic parity-even interactions destroy the selection itself.
- Lead: the smallest immediate arithmetic experiment named anywhere in the group is to look for the analogue of the `P/100` term in any candidate prime letters — an uncontrolled component outside the generating family kills observable selection before any spectral computation. The additional four modes cannot be dismissed as unphysical from grading alone.
- Where: `riemann-vs-selberg-cmps.md:43-56,96-102,114`

### G4-T12-5 The parity-jump budget, the Hilbert-Schmidt no-go, and the tight-frame identity that replaces it
- Absorbs: L10-056, L10-058, L10-059, L10-060
- Class: EXPLORED-negative
- Raised by: subagent
- What: The parity jump `gamma(Ad P - I)` shifts all odd rates by `-2 gamma` and leaves the even block alone; in tight-frame language `R = sqrt(gamma)P` supplies `4 gamma I_O`, so a desired `c = 1/4` exhausts the whole budget at `gamma = 1/8`. That is a trap: for `L(X) = -i[H_0, X] + gamma(PXP - X) + D(X)` bistochastic and preserving the whole odd space, if `L|_O + 2 gamma I` is HS-skew-adjoint then all `R_a` are scalar and `D = 0` — proved from `-Re Tr(X* D(X)) = (1/2) sum_a ||[R_a*, X]||_HS^2` together with the fact that the commutant of all off-diagonal block matrices is `C I`. No zeta data enter. The positive replacement: define `C_O X = ([R_1*, X], ..., [R_m*, X])` on the odd subspace; the Hermitian part of the restricted generator is `-(1/2)C_O*C_O`, so `L|_O + cI` is HS-skew-adjoint iff `C_O*C_O = 2c I_O`. The useful letter problem is therefore a **tight-frame identity for commutators**, not merely parity covariance — a quadratic identity among arithmetic letters checkable without knowing any eigenvalue. The original proposal it grew out of was to formulate a letter-level Dirichlet-form defect for uniform odd dissipation and test whether arithmetic symmetry kills it, rather than assuming a positive metric built from preassigned zeta zeros.
- Lead: four escape hatches from the no-go are named and none has been tried — a nontracial invariant state with a different metric; a proper odd *resonance subspace* instead of the whole coherence space; an invariant positive form not equal to the HS form; or sharing the target rate between parity dephasing and other noises. Recorded: equal real parts of eigenvalues alone do not imply HS skew-adjointness.
- Where: `notes/rh-strategy-2026-09-19/graded-channels.md:22,25,29-41,51-59`

### G4-T12-6 No universal odd-sector Alon-Boppana floor, and why Hastings' argument cannot be split
- Absorbs: L10-055, L16-015
- Class: EXPLORED-negative
- Raised by: prover
- What: `E = (Ad I + Ad P)/2` kills the odd block, and primitive bounded-degree examples also exist, so no universal odd-sector Alon-Boppana floor exists and "RH because odd relaxation is an extremal expander rate" is unsupported without a separate arithmetic normalization or duality condition. The mechanism of the failure is one sentence: Hastings' quantum Alon-Boppana proof counts closed words and relies on those word traces being **nonnegative**, whereas odd-sector traces `Tr(Gamma E^n)` restricted to the off-diagonal blocks can be negative, so the counting argument has no analogue sector by sector.
- Lead: if a graded Alon-Boppana bound is wanted, it must be proved for the *sum* `Tr E^n`, which is nonnegative, and only then split — or a genuinely different argument is needed. Recording the obstruction saves re-attempting the direct translation.
- Where: `notes/rh-strategy-2026-09-19/graded-channels.md:21`; `03c_graded_ramanujan.tex:132-144`; `2026-09-15T08-37-49.txt:123-125`

### G4-T12-7 Which transfer, which trace: do not conflate the physical norm with the signed correlation
- Absorbs: L10-057, L10-096
- Class: EXPLORED-registered
- Raised by: subagent
- What: The physical norm uses the plus-sign transfer, whereas a fermionic field two-point function uses the *signed* transfer between insertions; the signed transfer is not being asserted to be a physical CPTP evolution, it is the required fermionic correlation propagation inside a physical cMPS. Verified against the cached Haegeman-Cirac-Osborne-Verstraete source, with the orientation (creation at the left endpoint) giving the displayed trace expression in the canonical `l = I, r = sigma` gauge. Separately, the doubled-bond cMPS supertrace is the parity-twisted closure norm and hence nonnegative — but that shard is marked sketched/unreviewed, and a formal graded spectral transfer and its trace distribution need not have a Kraus realization. The Selberg flat supertrace is a signed orbit distribution of a single-copy geometric complex and is a *different object* from the full doubled-bond Lindbladian supertrace.
- Lead: label every transfer — `L_eta` for correlations, `L` for dynamics — and never conflate the flat supertrace with the ring norm. Neither the toy's physical correlation nor its ring norm has been identified with the explicit formula.
- Where: `riemann-vs-selberg-cmps.md:102,132`; `graded-channels.md:23,106`; `refs/src/1211.3935/calculus.tex:378-403`

### G4-T12-8 The `C^(1|1)` witness, and why its arbitrary frequency matters
- Absorbs: L10-061, L10-063
- Class: EXPLORED-registered
- Raised by: subagent
- What: With `P = Z`, `H_0 = (omega/2)Z` and jumps `sqrt(1/8)X`, `sqrt(1/8)Y`, the even spectrum is `{0, -1/2}`, the odd block is `-1/4 I` plus rotation `+-i omega`, the stationary density is uniquely `I/2`, and the supertrace is `1 + e^{-t/2} - 2 e^{-t/4} cos(omega t) = |1 - e^{(-1/4 + i omega)t}|^2` — the correct two reference rates, a mixed stationary state and an additive functional equation at the finite rational-zeta level, from balanced population-exchange letters. It demonstrates an escape from the all-parity-damping ansatz. Two limitations: `R_X^2 != 0`, so it violates cMPS kinetic regularity (and unitary remixing to raising/lowering makes squares vanish but the mutual anticommutator nonzero), so it is graded GKLS data and not a finite-kinetic-energy fermionic cMPS; and the oscillation frequency is *free* — the check script uses `omega = sqrt 2`, never a zeta ordinate.
- Lead: a mechanism producing one vertical line is cheap; producing the *right* ordinates is the hard part, which is why the trace-identification problem remains indispensable. No RH inference follows from this toy.
- Where: `notes/rh-strategy-2026-09-19/graded-channels.md:61-67`

### G4-T12-9 Pre-registered failure criteria for the observable-subspace route
- Absorbs: L10-067
- Class: EXPLORED-registered
- Raised by: subagent
- What: The graded-channels lane wrote its stop conditions before doing the work. Failure if: the four-mode cancellation is destroyed by every meaningful arithmetic extension, positivity uses fitted eigenvalues, or a trace/divisor assertion silently suppresses poles visible to required insertions; if physical source/sink poles move, the proposed cMPS violates kinetic regularity, or the bond stays absorbing; if the existing covariant perturbations retain free nonuniform decay parameters; if metrics degenerate, modes escape, reference/trivial factors are inconsistent, or divergent prime rates are assumed to produce a normal semigroup.
- Lead: use these verbatim as pre-registered stop conditions for the arithmetic attempt.
- Where: `notes/rh-strategy-2026-09-19/graded-channels.md:128,134,140,146`

### G4-T12-10 Finite positivity need not survive regulator removal
- Absorbs: L10-071
- Class: EXPLORED-negative
- Raised by: subagent
- What: `C_n = [[2 - 1/n, 1],[-1, 0]]` has a positive invariant `G_n = [[1, 1 - 1/(2n)],[1 - 1/(2n), 1]]`, but `lambda_min(G_n) = 1/(2n) -> 0`; the limiting companion has a nonzero Jordan nilpotent and admits no positive invariant metric at all. This sits alongside the repo's own `1/p` prime-jump cutoff mass-loss warning.
- Lead: any limit argument must control the *conditioning* of the metric, not merely its existence at each `n`.
- Where: `notes/rh-strategy-2026-09-19/graded-channels.md:146`; `04g_phase_side_lindbladian.tex:121-135`

### G4-T12-11 The five-step arithmetic programme that replaces "find a Lindbladian with the zeros as eigenvalues"
- Absorbs: L10-099, L17-007, L17-021, L17-023
- Class: LEAD-unpursued
- Raised by: subagent
- What: (1) A finite generating family of odd observables closing under the correctly signed Heisenberg transfer, with explicit intertwiner and boundary source/sink — in the toy, the four Majoranas. (2) A letter symmetry giving `J(A + kappa)J = -(A + kappa)` with `kappa = 1/4`, `J` from arithmetic symmetries. (3) The square of the centered observable generator reducing, in an independently defined positive form, to minus an arithmetic self-adjoint `S`, with the analogue of `S >= 0` proved by sum-of-squares or boundary flux. (4) The selected output's meromorphic response having the desired zeta/scattering divisor including archimedean factors and correct affine normalization, distinguishing genuine cancellation from an omitted mode. (5) Passing all identities to regular-data correlations on fixed domains with controlled meromorphic convergence and algebraic multiplicities. The orchestrator's closing diagnosis separates the same three ingredients: observable closure and reflection symmetry are cheap (they come from CAR and quadratic Hamiltonians), and only coercivity is RH-sized.
- Lead: the smallest immediate arithmetic experiment is to derive the signed Heisenberg image of the first proposed prime/cusp output letter and its first two commutators, and calculate the component lying outside the proposed generating family. Look for the arithmetic source of step (3) only.
- Where: `riemann-vs-selberg-cmps.md:140-150`; `2026-09-19T11-20-25.txt:387-389,445`; `2026-09-19T11-30-31.txt:72`

### G4-T12-12 The boxed Ramanujan criterion for a boson-fermion cMPS: `A†G + GA = -2 Delta G`, `G > 0`
- Absorbs: L15-011
- Class: PARTIAL
- Raised by: prover
- What: Answering TJO's question "what is the general shape of the Ramanujan property for fermion+boson cMPS? I am hoping it is a condition on `Q, R`": fermionic correlations propagate with the parity-twisted transfer `K_f(X) = Q†X + XQ + sum_b R_b†XR_b - sum_f R_f†XR_f` (minus signs on fermionic species only; the ordinary norm transfer has all plus signs and is CP, and `X -> PX` intertwines them). Restricting to an invariant sector `E` meant to carry the zeros and setting `A = K_f|_E`, the one-sided condition is `Re lambda <= -Delta`, which with an arithmetic reflection `lambda -> -2 Delta - conj(lambda)` becomes `Re lambda = -Delta` (with `Delta = 1/4` in the Riemann normalisation). The matrix form is `A†G + GA = -2 Delta G` with `G > 0`, equivalently `e^{tA} = e^{-Delta t}U_t` with `U_t` unitary in `G` — in finite dimension exactly "critical-line spectrum **and** diagonalizability". It is exported and unreviewed, and not registered as a claim.
- Lead: the open half is `G`. Choosing it from the BC and symplectic structure would give it arithmetic content; the stationary density does not supply it. Ask whether the Weil/metaplectic representation on the bond supplies a canonical invariant positive form, and whether that is the form making the shifted transfer skew-adjoint — if so, RH becomes a covariance statement about a representation rather than a spectral statement about an operator.
- Where: `2026-09-13T12-11-30.txt:593-595`; `outputs/ramanujan-boson-fermion-cmps.md:88`

### G4-T12-13 Kinetic regularity is an independent condition that narrows the generator cone
- Absorbs: L10-062, L15-012
- Class: EXPLORED-registered
- Raised by: prover
- What: A regular mixed cMPS requires the jump operators to obey the species' commutation and anticommutation relations — `PQP = Q`, `PR_a P = (-1)^{p_a}R_a` **and** `R_a R_b = (-1)^{p_a p_b} R_b R_a`, hence `R_f^2 = 0` — with `Q = -iH - (1/2) sum R_a†R_a` in left canonical form. Parity covariance alone does not impose that. This is a real narrowing of the earlier Bost-Connes cone calculation: the `(p-1)(p+1)^2`- and `(2p-2)`-dimensional cones were computed without the regularity constraint, so they overcount the physically realisable graded cMPS generators. The repo's own shard already warns that finite kinetic energy is independent of the other zeta conditions.
- Lead: screen every candidate letter set against `R^2 = 0` before spectral work, and re-run the cone dimension count with the regularity relations imposed — they are quadratic in the jump operators, so the regular locus is a variety inside the cone, not a linear section. If it is much smaller, the "covariance leaves too much freedom" conclusion may need revising in the direction the programme wants.
- Where: `2026-09-13T12-11-30.txt:525-533,552`; `06h_zeta_conditions.tex:57-62,157-172`

### G4-T12-14 The `sigma`-metric dissipation identity: the GNS metric of the stationary state is the wrong metric
- Absorbs: L15-013
- Class: PARTIAL
- Raised by: prover
- What: With `||X||_sigma^2 = Tr(sigma X†X)` and `sigma` the stationary bond density, stationarity gives the exact identity `-2 Re<X, K_f X>_sigma = sum_b ||[R_b, X]||_sigma^2 + sum_f ||{R_f, X}||_sigma^2`. Regularity (`R_f^2 = 0`, so `{R_f, R_f} = 0`) makes the right-hand side vanish at `X = R_f`. Hence **no strictly positive instantaneous dissipation bound in the BC-state metric can hold on a sector containing a nonzero `R_f`**, even though the spectral decay rates on that sector can all be strictly positive. This is exactly why the Ramanujan condition must be spectral, or in a *different* metric, rather than a Dirichlet-form coercivity bound.
- Lead: promote it to a proposition with an evidence script, and test whether `G` can instead be `sigma^{-1}`-weighted or a Weil-invariant form. It contradicts the most obvious guess in the Phantasm programme — that the zeros are the decay rates in the stationary state's own metric.
- Where: `2026-09-13T12-11-30.txt:530,536,541-634`

### G4-T12-15 Elementary odd modes and the full odd sector have different decay rates
- Absorbs: L15-014
- Class: EXPLORED-negative
- Raised by: prover
- What: Take two fermionic bond modes, `R_1 = sqrt(kappa) c_1`, `R_2 = sqrt(kappa) c_2`, `H = g(c_1†c_2† + c_2c_1)`, `Q = -iH - (kappa/2)(n_1 + n_2)`. On the elementary odd sector `span{c_1, c_2, c_1†, c_2†}` the parity-twisted transfer eigenvalues are `-kappa/2 +- ig`, but the **full** odd operator space also contains `-3kappa/2 +- ig`; the exact characteristic polynomial of the full odd block is `[((z + kappa/2)^2 + g^2)((z + 3kappa/2)^2 + g^2)]^2`. So a Ramanujan property demanding one uniform rate on the whole odd sector is false even for a perfectly regular fermionic cMPS.
- Lead: identify the sector `E` arithmetically. The higher operator sectors are integer multiples (`1x`, `3x`) of the elementary rate, which looks like a multi-particle tower; if the zeros are the elementary modes one needs a physical reason — a Krylov space generated by single insertions, say — to project onto them. It is three lines of sympy and constrains every later Ramanujan formulation; it should be a registered evidence script.
- Where: `2026-09-13T12-11-30.txt:536,610,620`

### G4-T12-16 How the involution `J` and the metric `G` were actually found
- Absorbs: L17-012, L17-013
- Class: EXPLORED-registered
- Raised by: subagent
- What: The reflection symmetry is presented in the notes as "derived directly from the letters, with no diagonalization". It was in fact found by an exhaustive SymPy search over all `4! x 2^4 = 384` signed permutation matrices, testing `JN + NJ = 0` symbolically in `a, c, d` and taking the first hit, followed by a rotation to the `J`-eigenbasis. The rational metric `G` was obtained by writing a general symmetric matrix with ten unknowns, solving `K^T G + G K = 0` on the companion basis by `linsolve`, and checking the leading principal minors.
- Lead: both are cheap reusable recipes for any candidate arithmetic letter family — search a small finite group of signed permutations (or the relevant Clifford/Majorana monomials) for an involution anticommuting with the centered drift, and solve the linear Lyapunov system for an invariant form. That turns "is there a functional equation here?" into a finite check.
- Where: `2026-09-19T11-30-31.txt:64,68`; `2026-09-19T11-22-27.txt:132,136`

### G4-T13-1 An exact finite cMPS/Lindblad realization of the cusp Gram
- Absorbs: L10-028
- Class: EXPLORED-registered
- Raised by: subagent
- What: Set `R = K^{1/2}`, `B = RCR^{-1}`, `j = 1* R^{-1}`; then `B* + B = -j*j`, so `B = -iH - (1/2)j*j`. On the bond `C|vac> ⊕ C^N` with jump `L = |vac> j` and `Q = 0 ⊕ B`, the canonical relation `Q + Q* + L*L = 0` holds and the vacuum-to-mode coherences carry exactly the decay eigenvalues `s_i - 1/2`. It is an admissible finite physical model, not yet a proof mechanism.
- Lead: its limitations *are* the programme — it takes a finite pole list as input, has an absorbing pure vacuum, has no prime-defined letters, and has no mixed BC critical stationary state. It is nevertheless the debugging oracle against which any letters-first construction should be compared.
- Where: `notes/rh-strategy-2026-09-19/cusp-bridge.md:84-90,123`

### G4-T13-2 Three distinct spectra must be kept apart
- Absorbs: L10-100, L17-014
- Class: EXPLORED-registered
- Raised by: orchestrator
- What: The no-jump generator `Q`, the physical transfer `L`, and the poles visible to specified correlation insertions are three different spectra, and a physical construction must say which of them carries the zeta divisor and prove that the modes are observable. The absorbing-vacuum construction does this for odd coherences but has trivial stationary entanglement, and arbitrary mixed reinsertion need not preserve those modes. The orchestrator also attached the caveat that identifying an actual fermionic output correlation requires the correct parity insertion, and that not every odd bond observable is already a physical local field insertion. Three days of prior repo work had not made this distinction.
- Lead: every future claim of the form "the zeros are the eigenvalues of `X`" should be forced to name which of the three objects `X` is.
- Where: `notes/rh-strategy-2026-09-19/cmps-renewal-bridge.md:11-13`; `2026-09-19T11-20-25.txt:165`

### G4-T13-3 The finite inverse renewal criterion `M = -(B sigma + sigma B*) >= 0`, and its exact failures
- Absorbs: L10-101, L10-102, L10-103, L17-015
- Class: EXPLORED-registered
- Raised by: orchestrator
- What: For stable `B` with `E = -(B + B*) >= 0`, the generator `L_Omega(X) = BX + XB* + Omega tr(EX)` is CP and trace preserving with explicit letters `R_ab = sqrt(w_a e_b)|v_a><u_b|`, `Q = B`. For a target `sigma` with `r = tr(E sigma) > 0`, a reset density making `sigma` stationary exists **iff** `M >= 0`, and then `Omega = M/r` uniquely; conversely every reset has a unique normalized stationary density, though faithfulness needs further controllability hypotheses. Two exact consequences were computed. Reinsertion changes the physical spectrum even when the no-jump generator is preserved: for `B = -iX - diag(1,0)/2` with no-jump modes `-1/4 +- i sqrt15/4`, resetting to `I/2` gives transfer modes `{0, -1/2, -1/2 +- 2i}` while resetting to `diag(1,0)` gives `{0, -1/2, -1/4 +- i sqrt63/4}`. And for `sigma = diag(p, 1-p)` the required reset numerator has determinant `-(1-2p)^2`, so **only the uniform target works** — an exact algebraic statement, not a numerical conjecture.
- Lead: once an arithmetic no-jump generator and a proposed BC cutoff state are specified independently, positivity of `M` is a falsifiable compatibility condition, and the reset cannot then be chosen freely. A Gibbs-weighted BC cutoff state is a *biased* target, so this is a direct warning about that route; and any proposal that builds the divisor into `Q` and then "adds a stationary state" must recompute the observable spectrum afterwards.
- Where: `notes/rh-strategy-2026-09-19/cmps-renewal-bridge.md:15-41,55-57`

### G4-T13-4 The critical BC state is not a normal density — a type-III/GNS formulation is required
- Absorbs: L10-097
- Class: LEAD-unpursued
- Raised by: subagent
- What: Treating the critical Bost-Connes state as a finite trace-one matrix would suppress a real limit problem. A proposed type-III/GNS formulation must replace the finite Schmidt-density argument with a specified state, a positive covariance/GNS form, domains for its evolution, and convergence of local physical correlations. The wording matters: "nonnormal" here concerns normality of a *state as a functional*, which is distinct from nonnormality of the finite decay matrix.
- Lead: the route is named and never attempted. Note also that neither property by itself derives reflection symmetry, observable closure or the coercivity estimate.
- Where: `riemann-vs-selberg-cmps.md:134-138`; `04c_phantasm_channels.tex:123-132`

### G4-T13-5 The grading obstruction: a stable graded bond with a rank-one homogeneous exit is impossible
- Absorbs: L10-104
- Class: EXPLORED-negative
- Raised by: orchestrator
- What: If both parity sectors are nonzero, `B` commutes with `P`, and `E = -(B + B*)` has rank one, then `E`'s range lies wholly in one parity sector and the other sector evolves unitarily, so `B` cannot be stable on the whole graded bond. Independently confirmed by the graded-channels lane.
- Lead: the escapes are named — more exits, a reference sector with different dynamics, an operator/coherence grading, or a restricted resonance realization. It does not rule out the reference-vacuum embedding or a proper observable coherence space.
- Where: `notes/rh-strategy-2026-09-19/cmps-renewal-bridge.md:43-47`

### G4-T13-6 Siemon-Holevo-Werner's exit-space / reinsertion formalism, with its cautions and one source sign error
- Absorbs: L10-128, L10-129, L10-130, L10-132
- Class: PARTIAL
- Raised by: TJO
- What: A **no-event semigroup** maps every pure state to a multiple of a pure state and is necessarily `C_t rho C_t*` with `C_t = exp(tK)` a contraction semigroup; the exit space is defined by `<j psi, j phi> = -(<K psi, phi> + <psi, K phi>)`, with `||J phi||^2 = ||phi||^2 - lim_t ||e^{tK}phi||^2`; a **standard** semigroup is the minimal solution from a CP perturbation of a no-event generator; reinsertion maps satisfy `tr reins(sigma) <= tr sigma`, and jump operators correspond precisely to Kraus operators of the reinsertion via `L_alpha = M_alpha j`. The worked example — the half-sided shift on `L^2(R^+)` with exit space `C`, `j psi = psi(0)` and a rebound state — is the natural model for the Hardy/half-line compression. Two cautions from the same source: there exist semigroups that appear probability-preserving to first order (on the finite-rank part of the generator's domain) but not for finite times; and *nonstandard* dynamical semigroups `gen_hat rho = gen rho - tr(gen rho)rho_hat` are a genuine extra class. One correction: the displayed gauge lemma (Kgauge) has the wrong sign relative to the dissipativity computation in its own proof; only the proof's sign leaves the generator invariant under `L -> L + lambda`.
- Lead: this is exactly the machinery that the Uetake domain caution and the prime-kink no-go call for — an unbounded no-event generator with a genuine boundary exit. Any arithmetic generator checked only at the level of the formal GKLS relation `Q + Q* + sum R*R = 0` still needs a separate conservativity theorem at finite times; and if it turns out non-conservative, the nonstandard class is how to repair it without changing the no-event part. Use the proof's sign in any gauge-fixing of arithmetic letters.
- Where: `notes/extract/shw-unbounded-generators-sources.md:11-79,95-129`; `TORUN.tex:147,378,402,646`

### G4-T13-7 Arveson's "units" of a dynamical semigroup
- Absorbs: L10-131
- Class: LEAD-unpursued
- Raised by: paper
- What: Arveson calls no-event semigroups with this property the *units* of the semigroup. A whole structural theory (product systems, units) sits behind a single quoted line.
- Lead: nobody in the repo has looked at it; it is an unexplored structural frame for the no-event letters.
- Where: `notes/extract/shw-unbounded-generators-sources.md:109-114`

### G4-T13-8 The BC finite-level obstruction is structural, and our prime-level extension is a stipulation
- Absorbs: L10-133, L10-134
- Class: EXPLORED-registered
- Raised by: subagent
- What: From Connes-Marcolli, `varphi_beta(e(a/b)) = b^{-beta} prod_{p|b}(1 - p^{beta-1})/(1 - p^{-1})` for `0 < beta <= 1`, together with `mu_n* mu_n = 1` and `mu_n e(r) mu_n* = (1/n) sum_{ns=r} e(s)`. These relations, not any approximation of the zeta zeros, give the finite-representation obstruction B0.2: a finite matrix representation of the BC algebra is blocked by the isometry relations themselves. The prime-level matrix extension B1.1 is our own stipulation and is not claimed in that source; our finite cone uses equality for trace preservation and derives its conditional Choi description explicitly, while the source's unbounded-domain and conservativity caveats remain applicable to any future adelic limit.
- Lead: a finite feasibility result in the BC cone is not a step toward the adelic limit until a limit theorem exists — finite-dimensional feasibility alone is not such a limit theorem.
- Where: `notes/extract/bc-symmetry-sources.md:14-49`

### G4-T13-9 vom Ende on unique decompositions of generators — consulted, never used
- Absorbs: L10-135
- Class: LEAD-unpursued
- Raised by: subagent
- What: Frederik vom Ende, *Understanding and Generalizing Unique Decompositions of Generators of Dynamical Semigroups*, arXiv:2310.04037; abstract consulted, not used as a premise or registered claim.
- Lead: canonical uniqueness of the `(K, L_alpha)` decomposition matters if one wants to claim that an arithmetic generator's letters are *the* letters rather than one gauge among many. Never followed up.
- Where: `notes/extract/bc-symmetry-sources.md:52-55`

### G4-T13-10 The vacuum is absorbing: the renewal fixed point fails and the vacuum-decay model doubles the zero list
- Absorbs: L14-032, L14-040
- Class: EXPLORED-negative
- Raised by: prover
- What: The brief drafted "this is reinsertion at the rebound state `Omega = |vac><vac|`, and the fixed-point equation `rho_inf ∝ int_0^inf Z(t) Omega Z(t)* dt` is solved by `Omega` itself". The prover: the state is a pure fixed point, but inserting it into the renewal integral makes the integral diverge — `Omega` lies outside `K_S`, and in the enlarged space the integral equals `T Omega` up to cutoff `T`. The vacuum is absorbing, not a finite-holding-time renewal state. Separately, the brief drafted that each zero appears once as an odd mode `-conj(rho)/2` and once as its conjugate; since the zero multiset is already conjugation-invariant, the combined odd list has multiplicity `2 m_rho` — so the one object that exists (the absorbing-vacuum CPTP semigroup) realises the **double** of the graded datum that positivity forces.
- Lead: the reinsertion state must have finite mean holding time and *which* state it is remains undetermined — finding an arithmetically natural one is the concrete next step. And the doubling mismatch between the existing object and the forced one (a square root, a real structure, a further grading?) is a well-posed question.
- Where: `2026-09-12T21-42-08.txt:87,131`

### G4-T13-11 The `Gamma_0(N)` scattering-sector / Dirichlet-character mismatch
- Absorbs: L15-008
- Class: PARTIAL
- Raised by: prover
- What: The planned next move was a finite-level `Gamma_0(N)` scattering-matrix computation matched against Bost-Connes characters. The prover checked and warned that the literature gives no automatic one-to-one match between untwisted `Gamma_0(N)` scattering sectors and all Dirichlet characters mod `N`: counting sectors by characters is wrong without twisting. Two starting points were named and are not in `refs/`: arXiv 1803.06016 (*Twist-minimal trace formulas*, §2.7, for the explicit Eisenstein formulas) and arXiv 1106.5741 (*Newforms and spectral multiplicities*).
- Lead: fetch both, extract the explicit Eisenstein/scattering formulas for `Gamma_0(N)` with nebentypus, and write down the actual sector/character correspondence — a statement about *twisted* `Gamma_0(N)`, newform level and oldform multiplicity. If it is many-to-one, the "one BC character per scattering channel" picture is wrong as stated and the bond needs the multiplicity space. Cheap to settle, expensive to discover late.
- Where: `2026-09-13T12-11-30.txt:101,141`

### G4-T13-12 The missing invariant-sector argument for reinsertion
- Absorbs: L15-009
- Class: LEAD-unpursued
- Raised by: prover
- What: The prover organised "the next most consequential step" as three questions, of which only the second reached the repo. (1) What is the common arithmetic structure — compute a small-level scattering matrix and its symmetry action, then look for an explicit map from the BC residue/character construction. (2) Does the induced state pass the positivity test — in the SHW exit-and-reinsertion form, stationarity of a proposed `sigma` with `Tr(C sigma) > 0` *solves for* the reset state, `Omega = -(B sigma + sigma B†)/Tr(C sigma)`, so existence is exactly `-(B sigma + sigma B†) >= 0`. (3) Does reinsertion preserve the odd zero modes — "preserving `B` as the no-event generator does not itself preserve its eigenvalues in the full Lindbladian; this needs an explicit invariant-sector argument."
- Lead: item (3) is the one nobody wrote down, and it is a checkable linear condition: for the vacuum-decay model whose odd sector already carries the zeros, add the rank-one reset `Tr(CX)Omega` and ask whether the zero-mode subspace is still invariant — it is iff `Tr(CX) = 0` on that subspace. That decides in an afternoon whether any reset completion can keep the zeros.
- Where: `2026-09-13T12-11-30.txt:113-147`

### G4-T13-13 Stage the BC limit: work at `beta > 1` first, and formulate `beta = 1` as a state functional
- Absorbs: L15-010, L16-001
- Class: LEAD-unpursued
- Raised by: prover
- What: The critical BC state is not a normal density in the standard representation, so reaching `beta = 1` requires an algebraic formulation of the limit: find a CP unital Heisenberg semigroup with `varphi_BC ∘ T_t = varphi_BC` and `T_t ∘ alpha_g = alpha_g ∘ T_t`, i.e. impose stationarity on the *state functional*, not on a density matrix. Two side cautions: carrying a symplectic action does not mean the generator commutes with every symplectic transformation, and the BC fixed state alone does not force Galois covariance — covariance is an additional requirement of the programme. The same staging fixes a separate problem: with the drafted rates `lambda_p = 1/p` the no-jump quadratic form diverges and there is no semigroup at all, but with *summable* rates `lambda_p = p^{-beta}`, `beta > 1`, the absence of a normal stationary density is an honest theorem proved by a valuation argument on the shell index.
- Lead: redo the cone calculation at `beta > 1`, where the state is an honest density `diag(p^{-beta}, (1 - p^{-beta})/(p-1), ...)`, and watch how the cone dimensions vary; the `beta -> 1+` behaviour (does the cone grow or collapse?) is the finite-level shadow of the critical limit and is cheap to compute.
- Where: `2026-09-13T12-11-30.txt:145,183-188`; `2026-09-14T14-56-39.txt:221`

### G4-T13-14 Individual edge jumps restore Gibbs stationarity — at what arithmetic cost?
- Absorbs: L16-006
- Class: PARTIAL
- Raised by: prover
- What: The brief's detailed-balance proposal (reverse jumps `V_p†` at rate `lambda_p p^{-beta}`) fails twice: the rate orientation is backwards (the required ratio is `d_p/u_p = p^beta`), and even after reversing it the *phase* jumps keep creating off-diagonal shell coherences, so the diagonal Gibbs state is not stationary. The prover's repair replaces the global prime isometries by **resolved individual edge jumps** `b -> pb`, one Lindblad operator per edge of the shell graph rather than one per prime, which does preserve the diagonal Gibbs state.
- Lead: write the edge-jump generator out explicitly and ask whether any arithmetic content survives — it is a classical birth-death chain on the divisor lattice, so the question is whether anything of the Bost-Connes structure remains. If nothing does, that is a clean statement of the cost of imposing detailed balance.
- Where: `2026-09-14T14-56-42.txt:241-243`; `astra-finite-model.md:391`

### G4-T14-1 The Poisson-equation / mean-absorption-time certificate as the transferable item
- Absorbs: L10-105
- Class: LEAD-unpursued
- Raised by: subagent
- What: In the Heisenberg picture `L†(G^+ - beta P) = -Q`, so `Y = G^+ - beta P` solves `L†Y = -(1-P)` and is bounded; a bounded solution of the Poisson/Lyapunov equation certifies uniform worst-case exponential mixing — the quantum analogue of "mixing time ≲ max expected hitting time × log(1/eps)". Shang's Theorem 1 gives `t_mix(eps) <= 3 kappa^2 ceil(2 log_2(1/eps))`, dimension-independent, with **no spectral information used at any point**.
- Lead: for the notebook's absorbing-vacuum channel the analogues are `q(t) = Tr(Z_t X Z_t†)` and the Gramian `W = int_0^inf Z_t† Z_t dt` (finite `N`: `B†W + WB = -1`), with `sup_rho D(rho_t, Omega)` lying between `||Z_t||^2` and `||Z_t||`. Note that the `||Z_t|| = 1` result below limits what this can deliver unconditionally.
- Where: `notes/extract/2609.12284-reading.md:91-100,143-150`

### G4-T14-2 What Shang's reset Lindbladian actually shows — four facts, all checked
- Absorbs: L10-106, L10-107, L10-109, L10-110
- Class: EXPLORED-registered
- Raised by: subagent
- What: (i) The exact spectrum is `{0} ∪ {-sigma_j(A)^2} ∪ {-(lambda_i + lambda_k)/2, i != k}`, proved by the matrix determinant lemma and checked numerically to `1e-14` — all real; this is not in the paper. (ii) The gap lies in `[sigma_min(A)^2/2, sigma_min(A)^2]` and equals the mixing rate: a benign, not a non-normal, example, with no cutoff, no dimension-dependent burn-in and no transient amplification — so the paper gives *no* general relation between spectrum and mixing time and cannot be cited as evidence that the gap controls mixing in the Riemann setting. (iii) Rank-one reset bonds make the ring zeta factorise: `det(z - T) = det(z - K)(1 - <<G|(z-K)^{-1}|R>>)`, with the secular factor's zeros at `-spec(AA†)`. (iv) Structurally it is a cousin of the repo's vacuum-decay model, differing in that the dark state is annihilated by the no-event generator while the reset target overlaps it, which is what makes the population block a nontrivial rank-one feedback.
- Lead: a nonzero overlap between dark state and reset target is the mechanism that turns a pure fixed point into a nontrivial feedback — potentially useful for the mixed-reset question. The ring-zeta factorisation is explicitly low priority ("unlikely to reach arithmetic content") but is a toy for sdet factorisations.
- Where: `notes/extract/2609.12284-reading.md:107-139,176-181`

### G4-T14-3 Restricted mixing: find the initial-state class on which the argument does go through
- Absorbs: L10-111, L10-114
- Class: LEAD-unpursued
- Raised by: subagent
- What: Shang's own scope caveat is the model: "the lower bound is not an oracle lower bound... its input has an easily prepared solution, and initialization at `|r>` does not populate the slow mode used in the proof". The repair for the Riemann case is the same move: candidates named are `X` with `Tr(XW)` finite, or smooth vectors / the domain of a power of `B`, and the question is whether "all modes at rate 1/4" is then equivalent to a uniform exponential bound on that class — a Gearhart-Pruss-type statement in a weighted norm. The Becker-Zworski note gives the right shape: `||Z(t)f|| <= C(f)e^{-t/4}` on a regularity class.
- Lead: this is the repair for the `||Z_t|| = 1` negative — the correct statement of RH as decay is one-sided and class-restricted.
- Where: `notes/extract/2609.12284-reading.md:62-69,199-202`; `2609.13121-reading.md:106,155`

### G4-T14-4 `||Z_t|| = 1` for every `t`, independently of RH — the biggest recorded negative
- Absorbs: L10-113, L10-121
- Class: PARTIAL
- Raised by: subagent
- What: For inner `S` on the lower half-plane and `phi_t(z) = e^{-itz}`, the model-space kernel estimate gives `||Z_t|| >= |phi_t(w)| - |S(w)| = e^{-t eps} - |S(x - i eps)|` at `w = x - i eps`. For `S(tau) = xi(1 - 2i tau)/xi(1 + 2i tau)`, Stirling gives a Gamma ratio `~ x^{-2 eps}` and the convexity bound gives `|zeta(1 - 2eps + 2ix)| << x^{eps + delta}` with `|zeta(1 + 2eps + 2ix)|` bounded below, so `|S(x - i eps)| -> 0` as `x -> inf` for each fixed `0 < eps < 1/4` (mpmath at `eps = 0.2`: `|S| = 0.72, 0.60, 0.095, 0.027` at `x = 10, 100, 1000, 5000`). Hence the Riemann semigroup is not uniformly exponentially stable, the Riesz-basis/Lyapunov certificate `A†G + GA = -2 Delta G` with `G` bounded invertible **cannot hold on all of `K_S`**, and the absorbing-vacuum channel has **infinite worst-case trace-distance mixing time**. The item is marked `[inferred]` and **unreviewed**, with a second reader explicitly requested. An independent route to the same conclusion exists: Sarason's formula `||Z(t)|| = dist_{L^inf}(e^{i tau t}, S·H^inf)`, with the observation that zeros at constant height with spacing tending to zero are not interpolating, so the reproducing kernels are not a Riesz basis.
- Lead: get the second reader, and compute the Sarason distance numerically with a Blaschke truncation. If confirmed, record as a proved negative — "no worst-case mixing-time form of RH for the Riemann/absorbing-vacuum channel" — which directly limits the Lyapunov targets above.
- Where: `notes/extract/2609.12284-reading.md:153-167,196-198`; `2609.13121-reading.md:152-157`

### G4-T14-5 The Gram / eigenvector condition number: a test statistic, not evidence
- Absorbs: L10-115, L14-026, L16-002
- Class: PARTIAL
- Raised by: subagent
- What: Assigning width 1/4 to the cached zeta ordinates and forming the Cauchy/exit Gram `G_mn = 2w/(2w - i(a_n - a_m))` with `w = 1/4`, the condition number is about 9.88 for the first 24 ordinates and about 701 for the last 24 of a 3000-ordinate cache, with the largest neighbouring overlap growing from 0.570 to 0.939. A later prover pass corrected the reading twice and settled it: under a labelled hypothesis the number is a legitimate *test statistic*, since a Riesz basis requires `kappa(N)` bounded as `N -> inf`, so only **unbounded** growth would disprove the candidate; growth from 10 to 700 over a finite window decides nothing. A concrete analogue is already measured on the other side: Becker-Zworski's Fock-truncated generator at `V = x^2/2, h = 1` has eigenvector condition number 17.5, 145, 1.2e3, 1.1e4, 9.3e4 at `d = 4,6,8,10,12`, with no Jordan blocks.
- Lead: ranked follow-up 1 in two separate lanes and never run. For the Blaschke product with the first `N` zero pairs (`w = -gamma_n/2 - i/4`), compute `cond(Gamma_N)`, `M_N = sup_t e^{t/4}||Z_t^{(N)}||` and `||W_N||` (compare with 2, the value for a normal operator), and fit the growth law against the zero density `log(gamma/2pi)`. Cheap and decisive for TJO's non-normal/Jordan hypothesis, and it is the same computation that would confirm or refute `||Z_t|| = 1`.
- Where: `notes/extract/2609.12284-reading.md:189-195`; `2026-09-12T19-12-16.txt:134,146`; `2026-09-14T14-56-39.txt:221,236`

### G4-T14-6 Becker-Zworski: the correct form of a decay statement is one-sided and class-restricted
- Absorbs: L10-116, L10-117, L10-126
- Class: EXPLORED-registered
- Raised by: paper
- What: Their Theorem 1 gives `||e^{tL}T - Pi||_1 <= C_{h,V} e^{-gamma_h t}(||T||_1 + ...)` with `gamma_h = lambda_1(h)/(2h)`, and that exponent is optimal — but there is **no gap on all of trace class**; the operator-norm version can fail even when the spectral bound is right. Since the repo's own RH statement is one-sided after the FE reflection ("no mode slower than 1/4"), the correct analogue is `||Z(t)f|| <= C(f)e^{-t/4}` on a regularity class. Two caveats about the source itself: lines 977-1132 come *after* `\end{document}` and are not typeset, yet they contain the proof that there is no spectral gap on trace class (`||LX_N||_1/||X_N||_1 = 2/H_N -> 0`, and in fact `||e^{tL}|_{tr X=0}||_{1->1} = 1`) on which a typeset Remark relies, plus a slow-decay example `E(t) ~ c/(2t)`; and the log-Sobolev inequality is used only to relax `d ∈ L^inf` to `d ∈ L^q`, giving no rate and saying nothing about cutoff.
- Lead: adopt this *form* for the RH decay statement. If the no-gap fact is used downstream it must be reproved or the untypeset tail cited as such — and note that `||e^{tL}|_{tr X=0}||_{1->1} = 1` is the exact analogue of the `||Z_t|| = 1` claim. Do not expect log-Sobolev machinery to supply a uniform arithmetic rate.
- Where: `notes/extract/2609.13121-reading.md:22-27,46-51,95-108`

### G4-T14-7 Vectorised generators are generic; the SUSY splitting is too clean to be a ring-norm mechanism
- Absorbs: L10-119, L10-120
- Class: EXPLORED-negative
- Raised by: subagent
- What: `M = Q_x + Q_y + h ∂_x ∂_y` is exactly `Q⊗1 + 1⊗conj Q + R⊗conj R` with `R ~ sqrt(h)∂` — a form generic to any vectorised Lindbladian, so structural resemblance is not evidence. The SUSY pair `Q ≃ -a*a/2h`, `S ≃ -aa*/2h` with `∂_x Q = S ∂_x` does move the off-diagonal information into a fermionic sector with no zero mode, a clean graded splitting separating fixed point from relaxation — but the supertrace `tr e^{-tH/2h} - tr e^{-t aa*/2h} = 1` (the Witten index) cancels the entire nonzero spectrum. A trace formula needs the opposite, zeros surviving with a sign.
- Lead: any grading used for the Phantasm must have a supertrace that does *not* collapse; a graded splitting that is too clean destroys the trace formula. And do not cite structural resemblance of vectorised generators as support for anything.
- Where: `notes/extract/2609.13121-reading.md:120-129`

### G4-T14-8 The pure-fixed-point trace-norm reduction, directly applicable and elementary
- Absorbs: L10-122
- Class: LEAD-unpursued
- Raised by: paper
- What: For `A >= 0` with trace 1 and `Pi` pure, `A - Pi` has at most one negative eigenvalue, so `||A - Pi||_1 = 2||A - Pi|| <= 2||A - Pi||_2`. It turns trace-norm mixing into operator/HS estimates whenever the fixed point is pure.
- Lead: apply it to the notebook's vacuum-decay Lindbladian and compute the exact trace-norm decay alongside the eigenvector condition number.
- Where: `notes/extract/2609.13121-reading.md:92-95,158-161` (BZ:676-679)

### G4-T14-9 Purified-Gibbs / Witten Lindbladians cannot carry the zeros
- Absorbs: L10-123, L10-124
- Class: EXPLORED-negative
- Raised by: subagent
- What: For a purified-Gibbs Lindbladian the diagonal is a reversible classical diffusion with real spectrum and Gibbs invariant measure, and the vacuum coherences `|nu><phi_k|` are exact eigenmodes with rates `lambda_k/2h`. Those rates are the spectrum of a self-adjoint `H >= 0`, so they are real, with no oscillation: complex modes `beta/2 + i gamma/2` cannot appear this way without a non-self-adjoint "Witten Laplacian". It is also not KMS-detailed-balance in the quantum sense, since the fixed point is not faithful. A discrete version was proposed to close the family off for good: on `l^2(N)` choose a jump `a` with `a nu = 0` and `nu_n ∝ n^{-beta/2}` (normalisable iff `beta > 1`, with a pole at `beta = 1`), compute the `a*a` spectrum and the coherence rates; predicted outcome negative.
- Lead: the discrete run is cheap, has a zeta-flavoured pole at `beta = 1`, and would definitively close off the single-jump purified-Gibbs family. The item also names exactly what would have to be broken — self-adjointness of the effective Laplacian.
- Where: `notes/extract/2609.13121-reading.md:136-143,162-165`

### G4-T14-10 Neither Lindblad paper supplies expanders, Ramanujan graphs, a Hastings bound or cutoff
- Absorbs: L10-127
- Class: EXPLORED-negative
- Raised by: subagent
- What: Neither paper has families, degree, an Alon-Boppana/Hastings-type bound, or cutoff. Shang's bound has no cutoff (prefactor `<= 1` from `t = 0`) and its rates range over `[kappa^{-2}/2, 2]`, so there is no "one rate" structure. Neither has KMS/GNS detailed balance for a faithful state, cMPS, grading/supertrace, or number theory.
- Lead: stop mining the Lindblad-mixing literature for the Ramanujan side. The whole transferable content was two method items (the Poisson certificate, the pure-fixed-point reduction) and two negatives (`||Z_t|| = 1`, the SUSY collapse).
- Where: `notes/extract/2609.12284-reading.md:183-185`; `2609.13121-reading.md:147-148`

### G4-T15-1 The Selberg tower dictionary was drafted upside down
- Absorbs: L14-001, L14-002, L14-010
- Class: DEAD
- Raised by: orchestrator
- What: The brief drafted `Lambda(sigma) = -(d/d sigma) log D(sigma)` with `D(sigma) = prod_{j>=1} Z(sigma + j)`; the prover's first reply was that the flat-trace transform is `D'/D`, i.e. `+partial_sigma log D`, so the minus sign proposed for that `D` is false. The companion error: the brief drafted "the graph analogue of `D` is `1/det(1 - uT)`", whereas the graph log-derivative has *exactly the same* sign as `partial_sigma log D`, so the correct analogue is `det(1 - uT)` itself. Also listed among the corrected items is the drafted convention for the Selberg trivial-zero multiplicities `(2g-2)(2k+1)`.
- Lead: rewrite the dictionary so that "Selberg tower `D`" ↔ "`det(1 - uT)`" and "Ihara zeta" ↔ "`D^{-1}`", and note that the tower `prod_{j>=1} Z(sigma + j)` is present on the hyperbolic side and absent on the graph side because the tree is one-dimensional (no transverse Jacobian). Re-check every place in the report that pairs a tower with a determinant, and check the multiplicity convention before importing the trivial zeros, since the tower multiplies them.
- Where: `2026-09-12T12-54-39.txt:71,81,111`; `notes/selberg/astra-proofs.md:332,510`

### G4-T15-2 The constant mode must be deleted on both sides of the dictionary
- Absorbs: L14-003
- Class: DEAD
- Raised by: orchestrator
- What: The brief drafted "all first-band resonances lie on `Re sigma = -1/2` iff every `r_j` is real" with `j >= 0`, i.e. including `lambda_0 = 0`. With `j = 0` the alleged band contains `0` and `-1` and so cannot lie on that line — the statement is false on *every* compact connected surface. The corrected property is the absence of **nonconstant** complementary-series parameters.
- Lead: this is exactly the continuous analogue of removing the constant adjacency mode (and the bipartite extremal mode when present) in the graph Ramanujan condition, so any "Ramanujan = RH" statement in the notebook must carry the same trivial-mode deletion on both sides. Worth checking wherever the notebook writes "all modes decay at rate 1/4".
- Where: `2026-09-12T12-54-39.txt:81,111`; `notes/selberg/astra-proofs.md:461`

### G4-T15-3 `Omega = -Delta` exactly, and the tensor Lindbladian is not the Casimir
- Absorbs: L14-006, L14-007
- Class: EXPLORED-registered
- Raised by: prover
- What: The brief asked for the constant `c` in `Omega f = c y^2(F_xx + F_yy)` without guessing. The answer: on right-`K`-invariant functions `Omega = -Delta` with the notebook's positive Laplacian, so `c = +1`, and the Lindbladian built from the two non-compact jumps `L_1 = -iH`, `L_2 = -iE` is `(1/2)(H^2 + E^2) = 2 Omega = -2 Delta` on that sector. For the tensor version the prover declined to make the requested gap remark and proved an exact operator identity instead: the Lindbladian equals `2 Omega_{pi ⊗ conj pi} + B_W^2/2`, with `B_W rho = 0` only on the diagonal-`K`-invariant sector, where `<rho, L rho>_HS = -(1/2) sum_j ||[A_j, rho]||^2_HS <= 0`.
- Lead: a Lindblad time `t` corresponds to hyperbolic Laplacian time `2t`, so any later attempt to match a Lindblad relaxation rate to the spectral gap 1/4 must carry the factor 2. And a spectral gap for the tensor Lindbladian is **not** obtained from the Casimir alone — the `B_W^2/2` term must be controlled and the invariant-domain question (is it a core?) is left open. Closing it would give a genuine "quantum Selberg gap".
- Where: `2026-09-12T12-54-39.txt:77,126`; `notes/selberg/astra-proofs.md:786`

### G4-T15-4 A flow generator is not a Lindbladian, and the prime circles are blind to the zeros
- Absorbs: L14-008, L14-009
- Class: EXPLORED-registered
- Raised by: prover
- What: "A first-order translation generator is anti-self-adjoint and is not a dissipative sum-of-squares generator merely because it generates a flow"; calling it a Lindbladian without an additional construction confuses it with a sum of squares. Alongside it the prover strengthened its own earlier draft: not merely "the finite Euler product has no zeros anywhere in `C`", but that `spec(A_S) = ∪_{p ∈ S}(2 pi i/log p)Z`, sitting on the imaginary axis, is **disjoint from the zero set of the continued Riemann zeta** — proved from `zeta(iv) = chi(iv) zeta(1 - iv) != 0` for real `v != 0` (the zero-free line plus the gamma quotient) together with `zeta(0) = -1/2`.
- Lead: a standing caution for the whole programme — if the Phantasm is to be a Lindbladian, the dissipation must be *constructed*, as the cusp/exit term is in the Riemann channel, not inherited from a flow. And the sharpest form of "the prime circles are blind to the zeros" is that the blindness *is* the zero-free line in disguise, so any construction hoping to produce zeros from prime circles must break either the finiteness or the unitarity.
- Where: `2026-09-12T12-54-39.txt` draft `_L0147`; `notes/selberg/astra-proofs.md:87,99,784`

### G4-T15-5 Cut: the contour proof that each off-line mode contributes a Lorentzian of unit mass
- Absorbs: L14-011
- Class: DEAD
- Raised by: prover
- What: Two early drafts of the Weil-positivity file carried a full contour computation of `int_R e^{ixt}/(x^2 + b^2) dx` — closing in the upper half-plane for `t > 0` with the arc bounded by `pi R/(R^2 - b^2)`, picking up the pole at `ib` with residue `e^{-bt}/(2ib)`, giving `pi e^{-bt}/b`; clockwise for `t < 0`; `pi/b` at `t = 0`; then shifting `x = xi - omega`. Its point was that the inverse transform of the Lorentzian `2b/(b^2 + (xi - omega)^2)` has **mass 1**. It was deleted and is absent from the final file.
- Lead: restore it if the continuous Weil form is ever to be normalised as a spectral *measure* rather than a distribution — the unit mass is what makes "each mode of width `b` contributes one Lorentzian of weight one" literally true.
- Where: `2026-09-12T17-21-49.txt:124,130,143`

### G4-T15-6 Cut: the continuous ring word `A_{j_1...j_k}`, and the drafted Dyson product that was false
- Absorbs: L14-012, L14-018
- Class: DEAD
- Raised by: prover
- What: The brief drafted the continuous ring norm as `sum_k sum_{j_1..j_k} int |Tr(e^{(t-t_k)K}R_{j_k}...R_{j_1}e^{t_1 K})|^2`, which read literally has the `R`'s adjacent with no free propagators between them — false for noncommuting `K` and `R_j`. The correction needs the full time-ordered product, the `k = 0` term, a finite jump-list hypothesis and absolute convergence. An early draft introduced exactly the right notation, `A_{j_1...j_k} = e^{(t-t_k)K}R_{j_k}e^{(t_k - t_{k-1})K}...e^{t_1 K}` with the degenerate cases spelled out and `A_∅ = e^{tK}`, and stated "no trace preservation is assumed" — and that notation was cut from the final file.
- Lead: `A_{j_1...j_k}` is the continuous analogue of the non-backtracking word `A_w` whose `|Tr A_w|^2` is the discrete ring norm; having a name for it (and for the empty word) is what would let one write a *continuous Ihara-Bass* by words rather than by determinants. Without it the repo has the theorem but not the combinatorial object. The moral is also substantive: the continuous ring norm is genuinely a *time-ordered* word, which is what makes it harder than the discrete count.
- Where: `2026-09-12T17-21-49.txt:83,124,130,143`

### G4-T15-7 The Kraus dichotomy corrected: unitarity on the nose, and reality is free
- Absorbs: L14-013, L14-014, L14-017, L14-021
- Class: DEAD
- Raised by: orchestrator
- What: Three drafted statements failed. (a) "Both pairings hold iff every `B_i` is a nonzero scalar multiple of a unitary" is false: simultaneous adjoint and inverse pairing requires *actual* unitarity `B†B = I`, disproved by `B = 2I`; scalar `B†B` characterises only a projective equality. (b) The requested inverse-paired Kraus counterexample **cannot exist**: the antiunitary involution `C(v ⊗ |i>) = v† ⊗ |i>` commutes with `T` for *every* Kraus family, adjoint-paired or not, so conjugation symmetry is automatic and counterexamples live only in the strictly larger non-Kraus superoperator class. (c) The requested `n = 1` example of an adjoint-paired non-scalar-unitary family is logically impossible, since every nonzero `1x1` matrix is a scalar multiple of a unitary. Separately, `mu -> r^2/mu` is a holomorphic reciprocal map, not a linear one, and the identity `W(c) = M(c)` needs conjugation symmetry of the retained multiset on top of reciprocal symmetry.
- Lead: "adjoint pairing buys reality" is too weak a slogan — reality is free for any Kraus presentation, and the real content of adjoint pairing is the nonnegative ring count `Tr T^l = sum_w |Tr B_w|^2`. That changes which hypothesis is load-bearing in the RH analogy. Also: a scale as innocent as `B = 2I` changes the transfer operator, its critical radius, its trivial roots and the channel normalisation, so a family of unequal scales need not preserve the quadratic duality at all. And the two halves of "RH = Weil positivity" split cleanly — the *bound* needs only the functional equation, the *inflow identity* needs reality too.
- Where: `2026-09-12T17-21-49.txt:79,81,114`

### G4-T15-8 The abandoned scalar-weight non-backtracking laboratory
- Absorbs: L14-015
- Class: LEAD-unpursued
- Raised by: prover
- What: The prover's first attempt at the counterexample built a `4x4` non-backtracking matrix directly from *scalar weights* — `rev = [2,3,0,1]`, weights `(a,1,a,1)` for `a ∈ {1,2,4}`, `T_ji = 0` if `j = bar i` and `= w_i` otherwise — and factored its characteristic polynomial. That is a superoperator family **not** of Kraus form, i.e. precisely the class where the counterexample does live. It was dropped for a genuine `n = 2, D = 4` Kraus family, and nothing in the repo records it.
- Lead: the scalar-weight non-backtracking matrix is the cheapest laboratory for "inverse pairing without Kraus" — the two-line model to use if one wants to see the functional equation *without* positivity of ring counts.
- Where: `2026-09-12T17-21-49.txt:117,148`

### G4-T15-9 The trivial set `S` has no arithmetic occupants
- Absorbs: L14-016
- Class: DEAD
- Raised by: orchestrator
- What: The brief drafted `S` as "the two trivial modes coming from the poles of `xi` at `s = 0` and `s = 1`". The notebook's completed `xi` is entire; those poles belong to the explicit-formula side `Lambda_zeta`, not to the mode list. For the zero-mode semigroup one must take `S = ∅`, and `{0, -1/2}` can be removed only after an explicitly artificial spectral augmentation.
- Lead: any attempt to make the Riemann channel's Weil form two-sided by deleting a trivial set has to *invent* that set, which is a strike against the construction.
- Where: `2026-09-12T17-21-49.txt:87,121`

### G4-T15-10 "Every zeta has side A, a nonnegative count of rings" is not a universal premise
- Absorbs: L14-020
- Class: DEAD
- Raised by: orchestrator
- What: The brief opened with that framing. The prover's ledger records that nonnegative ring traces hold in the stated Kraus settings only, are not a property of arbitrary superoperators, and are distinct from Weil positive-definiteness even when available — and crucially that the one-sided theorems need no positive ring-count premise at all.
- Lead: positivity of ring counts (side A) and Weil positive-definiteness of the rescaled trace sequence are logically independent, and the RH-relevant one is the latter. Worth checking whether the "ring gas" picture is doing any work in the main line of argument, or is only motivation.
- Where: `2026-09-12T17-21-49.txt:71`; `notes/weil-positivity/astra-proofs.md` (final ledger)

### G4-T15-11 Three resonance seeds refuted: the special information sits in the couplings
- Absorbs: L14-022, L14-023, L14-024, L14-027
- Class: DEAD
- Raised by: orchestrator
- What: Four drafted seeds failed. (S2) "GUE positions with equal widths is the fingerprint of a chaotic Hermitian `H` with scalar loss, not of cavity plus one lead" — false: the prover built the inverse design explicitly (prescribe poles `a = (-2, -0.7, 0.4, 1.8)` at common width `1/4`, form `P = prod(z - (a_k - iw))`, take `U = Re P`, `V = Im P`, read the closed energies as the roots of `U` and the coupling squares as `2V(h)/U'(h)`, set `H_eff = diag(h) - (i/2)jj^T`) and recovered the prescribed poles exactly, so equal widths at *arbitrary irregular* positions are realisable with one passive channel and tuned couplings. (S4) "Positivity of the Hamiltonian makes a J-unitary monodromy similar to a unitary" — false: two positive slabs `diag(4,1/4)` and `diag(1/4,4)` with `det H = 1` give monodromy eigenvalues `diag(-16, -1/16)`, manifestly off the circle; positive periodic media have forbidden bands. (S5) "Each local Euler factor `S_p` is an inner function whose zeros lie on `Im tau = -1/2`" — the factors are unimodular on the real line but not individually inner in the channel half-plane, checked at `p = 2`, `y = 0.25, 0.49, 0.51` against the true Blaschke factor. (S6) "What forbids superradiance here?" — nothing does; neither one exit nor GUE-like spacing prohibits superradiant width segregation, Hecke commutativity alone does not prove Poisson statistics, and GUE-like spacing does not place a physical cusp cavity in a time-reversal-broken ensemble.
- Lead: read this way, the special information in RH sits in the **couplings**, not in the loss operator, so any argument "equal widths ⟹ scalar loss ⟹ normal-plus-constant generator" is invalid and the programme cannot get Hermiticity for free from RH. The relevant positivity must belong to the spectral operator or its boundary response (a Weyl/Herglotz function), not to a spatial monodromy. And if a superradiance prohibition is wanted it must come from an arithmetic identity about the coupling vector `j`; the concrete test is to sweep the opening strength in a closed Hermitian model and watch for width splitting.
- Where: `2026-09-12T19-12-16.txt:77-81,131,134,152`; `notes/resonances/astra-freeassoc.md:101,226-234,321`

### G4-T15-12 Wigner time delay is convention-sensitive at the level of a rational function
- Absorbs: L14-025
- Class: EXPLORED-registered
- Raised by: prover
- What: The completed channel delay differs from the physical cusp delay by a rational term, so positivity of the completed model delay is not an unconditional positivity assertion for every convention of physical cusp delay. In the Selberg-file convention `q_phi = 2m`, whose Fourier transform carries the prime dips, the archimedean part and the pole boundary constant — none of which may be discarded when comparing signs.
- Lead: any "physical observable sensitive to equal widths" built from the delay must first fix which delay.
- Where: `2026-09-12T19-12-16.txt` (prover message); cross-references the cusp prime comb item

### G4-T15-13 Is there a Ramanujan property for a lead, or for continuous spectrum? (unanswered)
- Absorbs: L14-028
- Class: LEAD-unpursued
- Raised by: orchestrator
- What: Seed S8 asked: the Weil-LPS channels are exactly Ramanujan because of Deligne, and the analogue of the cusp there is absent (they are compact). What is the compact-vs-cusp dichotomy in expander language — is there a notion of "Ramanujan for the continuous spectrum / for a lead"? The final note defines no such notion; it observes only that Hecke/Ramanujan rigidity is the strongest arithmetic input available but acts on the discrete Laplace sector, whereas the zeros are scattering poles (the mechanism is ranked fifth, "currently acting on the wrong spectral sector").
- Lead: define "Ramanujan for a lead" — e.g. a uniform bound on the resonance widths of an open graph or quotient in terms of the degree — and test it on the Weil-LPS channels with one vertex opened. That would be a finite, checkable toy version of exactly the statement RH is asking for.
- Where: `2026-09-12T19-12-16.txt:83`; `notes/resonances/astra-freeassoc.md`

### G4-T15-14 The Artin-Schreier sign law and the super-transfer block were both false as drafted
- Absorbs: L14-030, L14-031, L14-035, L14-036, L14-037
- Class: DEAD
- Raised by: orchestrator
- What: The brief drafted, from 40 brute-force cases, `S_n(g) = -(-eta(-1))^n conj(Tr E_g^n)`, equivalently `(-1)^{n+1} eta(-1)^{d_n} Tr E_g^n`. The prover found a counterexample before writing anything: for `q = 3`, `g = 2x^2 + x^4`, `n = 1`, the exponential sum is `S_1 = 3` where the formula gives `-3`; a second is `(q,a,n) = (5,(1,1),2)`. The corrected law is `S_n = (-1)^{n-1} det(S | ker P(S)) Tr E_g^n` — the determinant of the cyclic shift on the **radical** of the quadratic form, equivalently the periodic sign `1 - 2·1_{2h | n}` — verified by 628 exact finite-field checks. The drafted failure class "`q | n`" is also wrong: the exact criterion for the whole sequence is `P(-eta(-1)) != 0`, and for `L(g,T) = det(1 + T E_g)` it is `P(-1) != 0`, i.e. `sum_j (-1)^j a_j != 0`. The drafted graded super-transfer matrix `E = [E_0 ⊕ (1)]_even ⊕ [-eta(-1) ⊕_a E_{ag}]_odd` with `str E^n = N_n` is false too: at `q = 3`, `g = 2x^2 + x^4` its supertrace is `-2` while the projective count is 10. When the endpoint condition fails, the replacement is a roots-of-unity rotation construction, verified symbolically at `q = 3`, `a = (1,1)`, `h = 3`: `[L(g,T) D_g(T)]^3 = det(I - T^6 E_g^6)` identically. A separate correction: `E_g/sqrt q` is a Clifford operation implementing an explicit symplectic `M_g ∈ Sp(2J, F_q)`, verified over 105 Weyl-label covariance comparisons with maximum residual `7.56e-16`, and the brief's "up to a phase" covariance is too weak — arbitrary label-dependent phases admit Weyl displacements, so the covariance must be *centred* and exact.
- Lead: anywhere the notebook says "the sign is the Frobenius permutation sign", the radical term has to be carried; the coefficient criterion `P(-eta(-1)) != 0` tells you in advance which curves the MPS picture describes exactly, and is cheap on any family. The `h`-th root construction is the only worked example of the corrected recipe and exists only in a transcript — worth committing. Finally, `d_n = dim ker(M_g^n - I)` and the Weil bound is saturated exactly when `M_g^n = I`, which makes saturation a finite group-order question in `Sp(2J, F_q)` — fully computable.
- Where: `2026-09-12T21-42-08.txt:91,117,129,159,171,173,204`

### G4-T15-15 Positivity does not fix the ladder's parity, and infinite-parity rigidity is open
- Absorbs: L14-033, L14-039
- Class: PARTIAL
- Raised by: orchestrator
- What: The brief proposed closing the infinite case by applying Landau's theorem to the diffuse part of the signed measure `f = supertrace - comb`. The prover could not: flipping infinitely many parities can produce **negative prime atoms** in `mu - comb`, and the argument needs those atoms separated from the diffuse part. What is proved is the finite-flip theorem (extended to arbitrary flips of trivial-zero parities provided only finitely many nontrivial zeros are flipped) and a theorem under the stronger domination hypothesis `mu >= comb`. Relatedly, the parity of the archimedean ladder is genuinely undetermined: over `C ⊕ K_S` alone the supertrace is `2P_+ + e^{-t/2}/(e^t - 1)`, and with the ladder counted even it is `2P_+ + 2e^{-t/2}/(e^t - 1)` — both positive.
- Lead: the missing step is a separation of the atomic and diffuse parts of a signed measure whose Laplace transform is `2 sum_{rho ∈ F} m_rho/(s - rho) + ...`. If closed, positivity of the supertrace would force **all** the parities, i.e. the Phantasm's grading would be determined by positivity rather than assumed. Meanwhile something other than positivity must decide whether the ladder `-(k + 1/2)`, `k >= 1`, is bosonic or fermionic — a sharply posed question whose answer would be a real structural datum about the archimedean place.
- Where: `2026-09-12T21-42-08.txt:81,85,150`

### G4-T15-16 Positive-power traces are blind to zero eigenvalues and nilpotents
- Absorbs: L14-034
- Class: EXPLORED-registered
- Raised by: prover
- What: For `J = 0` the minimal Artin-Schreier transfer matrix is the scalar quadratic Gauss sum `E_g = sum_x psi(a_0 x^2)`, with `E_0 = q`. `scripts/artin_schreier_mps.py` instead retains a redundant `q`-state register whose positive-power traces agree but which carries extra **zero eigenvalues**, so it is not the claimed one-dimensional scaled unitary; similarly `Tr E_0^n = q^n` for all `n` while the nonzero spectrum is just `{q}` with `q^J - 1` invisible zero eigenvalues for `J >= 1`.
- Lead: a concrete code fix, and a general caution: every "the transfer matrix *is* the Frobenius" claim proved by traces is a claim about net multisets, never about operator similarity, unless semisimplicity is added (H-FROB-SS).
- Where: `2026-09-12T21-42-08.txt:191`, draft `_L0147`

### G4-T15-17 H-MM1 was handed over as an assumption and had to be proved, on a specified weighted space
- Absorbs: L14-038
- Class: EXPLORED-registered
- Raised by: orchestrator
- What: The brief listed as a given that the birth-death generator on `N` with constant rates `lambda < mu` has spectrum `{0} ∪ [-(sqrt lambda + sqrt mu)^2, -(sqrt lambda - sqrt mu)^2]`. The prover proved it — detailed balance makes the backward generator self-adjoint in `L^2(pi)`, conjugating by `f_k -> sqrt(pi_k) f_k` gives off-diagonal `a = sqrt(lambda mu)` and diagonal `-(lambda + mu)`, the sine transform gives the band, and the boundary equation forces `z = sqrt(lambda/mu)`, `x = 0` — and added the qualification that matters: the infinite prime-chain spectrum is the **closure of the union of finite Minkowski sums** of those bands on a *specified stationary weighted space*.
- Lead: "the prime chain's spectrum is a union of real intervals and contains no trace of the zeros" is only true on that weighted space; on unweighted or unbounded closures nothing is asserted. Anyone arguing that the zeros are not in the Bost-Connes chain must pin the space.
- Where: `2026-09-12T21-42-08.txt:75,152`

### G4-T15-18 The population block's `|Tr Z|^2` is not a form factor
- Absorbs: L14-041
- Class: DEAD
- Raised by: orchestrator
- What: The brief drafted that the even population block carries the pair sums `-(conj(rho_n) + rho_m)/2` "whose formal trace is `|Tr Z(t)|^2`, i.e. the form factor of the zeros". The prover declined: only a formal expression or a finite-cutoff equality is available, because the pair spectral list violates the finite-order condition (G2) and a product of two distributional traces is undefined. No form-factor or pair-correlation limit is claimed.
- Lead: if Montgomery pair correlation is ever to appear inside this framework it must be as a regularised population trace with a stated regularisation — worth knowing before anyone builds a pair-correlation argument on this block.
- Where: `2026-09-12T21-42-08.txt:87`

### G4-T15-19 Simplicial complexes: the drafted vertex-level Bass collapse, and the complexes never tested
- Absorbs: L15-001, L15-002, L15-003
- Class: PARTIAL
- Raised by: orchestrator
- What: The brief guessed a vertex-level identity `det(1 - uT_1)det(1 + uT_2)^{-1} = (1 - u^3)^chi det P(u)^{-1}` holding exactly for complexes "whose vertex links are all generalised polygons of the same parameters". The prover proved the universal Schur identity and the building case but refused the characterisation: "equality of numerical link parameters, or the phrase 'links are generalized polygons', is not a proved characterization of that class or of cubic collapse". Two requested test complexes were never built: the 7-vertex triangulated torus and the cone, asked for twice as the smallest places the vertex-level identity should fail; the prover used the tetrahedron boundary instead. And the octahedral 2-sphere was computed twice in the prover's own sanity script and never reported — the tool outputs are not in the transcript, so its numbers are lost.
- Lead: characterise exactly which finite 2-complexes admit a vertex-level Bass polynomial with locally-determined `Q_1, Q_2`; a clean "iff" would say whether the numerator/denominator split is a building phenomenon or a local-geometry one, which bears on whether the Phantasm needs a building at all. Run the ordered-cell flow on the 7-vertex torus — the smallest complex with `chi = 0`, `b_1 = 2` and no free faces, hence the one case separating "trivial factor is `(1-u^{d+1})^chi`" from "the vanishing order is a Betti number". Recompute the octahedron: same `chi = 2` as `∂Δ^3` but different links, so it is the cheapest check of whether the exponent depends on `chi` alone or on the `f`-vector. Seconds of compute.
- Where: `2026-09-13T10-23-10.txt:85,95,147,164`; `notes/complex-zeta/astra-proofs.md:330,346`

### G4-T15-20 Four literature routes for a complex zeta, handed to the prover and never used
- Absorbs: L15-004, L15-005, L15-006, L15-007
- Class: LEAD-unpursued
- Raised by: orchestrator
- What: The brief supplied ten literature facts; four were never cited or tested. (C6) Storm: for a hypergraph the "right" zeta is not a new object — it is the ordinary Ihara-Hashimoto zeta of the vertex/edge incidence bipartite graph evaluated at `sqrt u`. (C8) Benard-Chaubet-Dang-Schick: for a triangulated closed `n`-manifold the **signed** zeta `prod_gamma(1 - eps_gamma z^{|gamma|})`, with a sign on each primitive geodesic orbit in the `(n-1)`-skeleton, is a polynomial vanishing to order `b_1` at `z = (n+2)^{-1}` — a genuinely different construction, since the signs live on orbits rather than on cell dimension, and the prover's own `∂Δ^3` number (order 6 at `u = 1` with `b_1 = 0`) shows the ordered default is not that object. (D2) The graph trivial factor `(1 - u^2)^{c_1 - c_0}` is `det(1 - uJ)` for the edge-reversal involution — a determinant of an involution, not a combinatorial count. (D4) Aizenman-Warzel: "the loop ensemble has a fermionic nature". Separately (F2) the brief asserts, as a literature-sweep result, that no quantum/Kraus-weighted zeta of a complex exists — the sentence any novelty claim would rest on, and it was never restated as a claim.
- Lead: compute the Ihara zeta of the incidence bipartite/tripartite graph at `u^{1/2}` or `u^{1/3}` for the test complexes and compare with the ordered graded determinant — if they agree, the whole campaign reduces to the already-proved quantum Ihara-Bass theorem. Implement the `eps_gamma`-signed geodesic zeta on `∂Δ^3` and a torus and check the order-`b_1` statement, then ask whether `eps_gamma` is the `Z_2` holonomy of a flat line bundle (a supertrace of transport around `gamma`). Ask what plays the role of `J` for complexes — the candidate is the cyclic rotation `C_k` already isolated in `F_k = C_k + R_{k+1}S_{k+1}`, which would make the trivial factor a statement about a `Z_{d+1}` action rather than about torsion, a much more elementary route. And give the priority claim a byte-cited "Not found" entry in `notes/extract/`.
- Where: `2026-09-13T10-23-10.txt:72-73`; `notes/complex-zeta/astra-proofs.md:462`

### G4-T15-21 The genus-2 "polarisation trace line" ansatz is false
- Absorbs: L15-015
- Class: DEAD
- Raised by: orchestrator
- What: The brief proposed that the even block of the doubled transfer have the eigenvalue `q` sitting in the trace line of `End(H^{1,0})` (the polarisation class) with the three nilpotent modes in the traceless part. Two `least_squares` fits built on that labelling — first with real `B`, then with `B = [[a, ib],[ic, d]]` — were abandoned, and the final file proves the structural reason: the `q`-eigenvector cannot be the pure trace-line operator `0 ⊕ I_2`, and the vacuum line is not an invariant line carrying eigenvalue 1; the true eigenvectors are `(sqrt2, I_2)` and `(-sqrt2, I_2)` for `q` and `1`.
- Lead: the useful residue is that the cohomological labelling of eigenvectors (vacuum ↔ 1, polarisation class ↔ `q`) is *not* preserved by any tensor with active fermionic couplings — the true eigenvectors mix the vacuum with the trace line in the ratio `+-sqrt2`. Any future "the bond is `H^*(J)`" story has to accommodate that mixing.
- Where: `2026-09-14T11-00-06.txt:125,129,132`; `notes/ring-norm-tensor/astra-proofs.md:692,759`

### G4-T15-22 The `F_5` three-species case was closed by a rational contraction certificate, and the method was not reused
- Absorbs: L15-016, L15-017
- Class: PARTIAL
- Raised by: prover
- What: For most of the session the deliverable was an explicit nine-species construction on `C^{1|2}` for every `q >= 16`, plus an exact 28-real-unknown polynomial feasibility system for the two-even/one-odd tensor over `F_5`, declared **open**. In the audit pass the prover found a certificate and reversed it: exact existence over `F_5` is proved, and the conjecture was simultaneously widened to the universal claim for every ordinary simple genus-two curve, status open. The method: `least_squares` on all 28 unknowns, QR-with-column-pivoting on the `9x28` Jacobian to select 9 active coordinates, Newton iteration in `mpmath` at 110 digits, then exact rational re-evaluation of `F` and `J` and verification of Kantorovich/Krawczyk bounds (`eta < 1e-70`, `epsilon < 1e-50`, `kappa < 1/4`, `eta + kappa r < r` at `r = 1e-30`) — a strict contraction of a rational box into itself. The pass also recorded that the genus-1 total-degree argument does not generalise (`|pi_1|^2|pi_2|^2 = q^2` gives one equation, not two), so Rosati positivity is genuinely needed.
- Lead: the same machinery answers the other open feasibility questions of the same file at almost no cost — three-species existence over `F_7, F_9, F_11, F_13` (the gap between `q = 5` and the `q >= 16` closed form); the purely bosonic `C^{2|2}` genus-2 realisation with cancellation allowed; and whether a two-species (one even, one odd) solution is genuinely infeasible rather than merely not found. Each is the same shape of problem: a square polynomial system in a box. What remains after the reversal is the *selection* problem — the certified `F_5` tensor is a numerically located algebraic point with 90-digit coordinates and no geometric meaning; finding a closed form (or proving none exists over `Q(pi_1, pi_2)` in a normal form) is the next concrete step.
- Where: `2026-09-14T11-00-06.txt:150,176-282,283,371,462`

### G4-T15-23 The archimedean side of the yolo Lindbladian was never built
- Absorbs: L16-003, L16-004
- Class: PARTIAL
- Raised by: orchestrator
- What: Both 09-14 afternoon briefs asked for an archimedean factor — the Gamma-factor (harmonic-oscillator) ladder on `L^2(R_+^*)` plus a Hamiltonian `D = x d/dx + 1/2`, or optionally a truncated oscillator with `T_{log p} = exp(log p (a - a†))` — and neither lane built one; the final report says flatly "no harmonic oscillator or archimedean Hamiltonian is added". So *every* negative result of 09-14 (no poles in the strip, no critical-line relaxation modes, no pole at `s = 1`) is a statement about the phase (profinite) factor only. The brief's optional figures of the singularity hunt were also never produced, so the clean negative exists only as tables.
- Lead: build the truncated oscillator `k = 0..K` with `T_{log p} = exp(log p(a - a†))` or a log-grid shift, tensor it onto the shell ladder, and rerun the singularity hunt. The archimedean factor is exactly the completion that §5.7 showed is missing to remove the spurious pole at `s = -2`, so this would be the first honest test of whether the *completed* object has strip structure. A contour plot of `|F(s)|` over `Re s ∈ [0.3,1.2]`, `Im s ∈ [0,40]` is a few lines on top of the existing mesh.
- Where: `2026-09-14T14-56-39.txt:92-99`; `2026-09-14T14-56-42.txt:93-101,128-131`; `astra-finite-model.md:62`

### G4-T15-24 The finite model's vacuum return function is independent of the shell cutoff
- Absorbs: L16-005
- Class: EXPLORED-registered
- Raised by: prover
- What: Mid-run the prover announced the closed form `F(s) = 1/(1 - sum_{p <= P} p^{-(s + beta + 1)})` and the point that matters: it does not depend on the shell cutoff `B` at all. The Euler-product (multiset) companion is `zeta_P(s + beta + 1)`, so the ordered-word resolvent has a *prime-sum* denominator while the multiset object has an Euler product, and the difference between them is exactly the word-multiplicity factor. Enlarging the shell space changes nothing.
- Lead: the negative result therefore cannot be blamed on truncation, which makes it much stronger than a numerical scan. Since `F` does not depend on `B`, the only free knobs are the rates and the length weight: ask which rate family `lambda_p` makes `1 - sum_p lambda_p p^{-s-1}` have zeros anywhere near the critical line. That is a constraint one can write down directly, and if no admissible (positive, summable) family works, the ordered-word route is closed for good.
- Where: `2026-09-14T14-56-42.txt:197-201`

### G4-T15-25 "Half entropy is RH" is C5 without C4
- Absorbs: L16-007, L16-008
- Class: EXPLORED-negative
- Raised by: prover
- What: The notebook's slogan "the odd sector is a sub-system with half the entropy, therefore RH" was first judged outright false for the continuum half-entropy cMPS, on the grounds that RH is an *additive central line fixed by a functional equation*, not a ratio of growth exponents. The final judgement is sharper and more useful: `lambda_- = lambda_+/2` does pass the central-line test, but only relative to an *explicitly prescribed* reflection `lambda -> 2 - lambda`, and the divisor does not obey that reflection — the example has **C5 without C4**, RH-shaped spectrum with no functional equation selecting the centre; shifting the spectrum by `-2` transports the target to `lambda -> -2 - lambda`, showing "half of a growth exponent" is not invariant under growth shifts. A companion correction was made at the last edit: the TP alternative uses `R_f = [[0,1],[0,0]]` and `R_b = Pi/2`, which do not anticommute, so the standard kinetic-regularity relation fails — but that is a failure of the *ansatz*, not a proof that the state has infinite kinetic energy.
- Lead: whenever a candidate is described as "half entropy = RH", first ask which FE fixes the centre; if none is exhibited the claim is empty. Conversely, look for a graded cMPS where the FE and the half-entropy relation pick out the *same* centre — that is the missing C4+C5 example. And look for a larger-bond or non-minimal presentation of the same ring state whose `(Q, R)` do satisfy the graded commutation relation; if one exists, the "K fails" column of the condition table changes.
- Where: `2026-09-14T16-38-51.txt:291,329`; `astra-constructions.md:156-160,335`

### G4-T15-26 C6curve versus C6projective, and the freedom of even zero modes
- Absorbs: L16-009, L16-010
- Class: EXPLORED-registered
- Raised by: prover
- What: Two inequivalent strengthenings of the ergodicity condition were in play. The draft's C6curve says that apart from the Perron root `q` the only other nonzero even eigenvalue is `1` (the `H^0` pole) — a *prohibition* on extra even modes. The final's C6projective requires the full pair `{1, q}` to be present — a *requirement*. They cut different examples. Separately, the first FE-failing / RH-satisfying witness used a second even eigenvalue `r = 2`, which bought an extra pole at `u = 1/2` and pushed the example out of curve normal form; the consistency pass found `r = 0` works, because an even zero mode contributes nothing to any positive-power trace and is invisible in the counts. All eight `(C4, C5, C6)` combinations then fit.
- Lead: keep both condition names in the ledger, and exhibit one tensor satisfying C6curve but not C6projective (no `H^0`, e.g. the affine rungs) and one the other way round (extra subleading even modes) to separate them cleanly. The general principle worth recording is that **even zero modes are free** — they change the bond and the fixed-point structure without moving any divisor point in the `u`-plane, the cheapest way to decouple C6 from C4 and C5, and the same trick as the "idle qubit" that destroys uniqueness without moving the divisor.
- Where: `2026-09-14T16-38-51.txt:258,291,320,324`; `astra-constructions.md:98,1742`

### G4-T15-27 Weighted MPS versus literal point count, and amplitude sum versus squared norm
- Absorbs: L16-011, L16-012
- Class: EXPLORED-registered
- Raised by: prover
- What: Two constraints flagged before any tensor was chosen. First, a *weighted* MPS can reproduce a curve's point counts as its Ramond norm while its words are not in bijection with the points — the counts come out right but the state is not a literal enumeration; and a simple Perron eigenvalue does not by itself give a trace-preserving normalisation on the whole bond, since TP is an extra equation on the letters. Second, for the tiny Dirichlet L-functions over `F_2[x]/(x^3+x+1)` and `F_3[x]/(x^2+1)`, the Horner transfer `f -> xf + c mod M` on the bond `F_q[x]/M` naturally produces an **open-chain, character-weighted MPS**, not a closed ring: summing its amplitudes gives the L-polynomial, taking the squared norm of the same state gives a different quantity, so the character amplitudes are not positive ring norms.
- Lead: for any "the MPS counts the points of `X`" claim, state explicitly which of the two it is (literal count or weighted norm) — the physical reading (correlation lengths, entanglement spectrum, what the odd sector *is*) only makes sense for the literal-count version. And whenever a tiny L-function is realised by Horner letters, say which of "sum of amplitudes" (side A, open chain, monic polynomials) and "squared Ramond norm" (side B, Frobenius orbits) is being asserted; the relation between the two presentations is the thing to write down.
- Where: `2026-09-14T16-38-51.txt:225-227,250-252`

### G4-T15-28 The graded divisor cancels, so it can hide modes that violate the band
- Absorbs: L16-014, L16-018
- Class: EXPLORED-negative
- Raised by: prover
- What: The notebook's divisor `nu = m_0 - m_1` is a *difference*, so an even mode and an odd mode at the same point cancel; a pair of such modes sitting outside the Ramanujan band therefore leaves the zeta and the divisor untouched. That is exactly why the drafted "band iff circle, sector by sector" is false — even a *mixing* qubit channel can have matching even and odd modes outside the band that cancel from its zeta. A related conflation was diagnosed nearby: the displayed Lie-group (continuum Harrow) walk has a tempered threshold `1/(2d)` while shard 09b quotes `1/2`, and neither is an error — `1/2` belongs to the faster two-jump normalisation.
- Lead: every Ramanujan claim in the notebook must say whether it is about the (cancelled) divisor or the (uncancelled) retained spectrum, and the two should get different names — this is the root of the D4 failure and of the Selberg endpoint subtlety. Fix one time normalisation per shard and state it at the top, or the temperedness argument appears to give contradictory gaps.
- Where: `2026-09-15T08-37-49.txt:98-100,164-166`

### G4-T15-29 The LPS examples are not curves, and integrality plus the circle condition is not enough
- Absorbs: L16-016, L16-017
- Class: EXPLORED-negative
- Raised by: prover
- What: `scripts/graded_ramanujan.py` passes all 79 of its checks, but none of them tests the *printed genus claims*: reducing the first LPS example gives a zeta numerator of **degree 4, not 36**, and the second has **uncancelled poles on the critical circle**, so its reduced zeta has no curve-shaped denominator either. Two independent reasons why "Weil-LPS channel = curve" should not be asserted. A third, sharper witness was verified separately: a primitive unitary channel whose numerator is an integer polynomial with all roots on the circle, but for which the hypothetical curve would have `-2` rational points.
- Lead: add the genus/degree assertions to the script's check list so they cannot drift again, and state the LPS examples as "period-two graded expanders with net multiplicities subtracted", not as curves. And add "the implied point counts `N_n` are nonnegative integers" (essentially the C2 "genuine gas" condition) as an explicit requirement whenever a channel is proposed as a curve — cheap to check, and it kills candidates fast.
- Where: `2026-09-15T08-37-49.txt:164-166,188-190,212-214`

### G4-T15-30 The cut `P = X` grading example
- Absorbs: L16-020
- Class: DEAD
- Raised by: prover
- What: Two inequivalent qubit witnesses for the period-two phenomenon were written. The cut one grades the bond by `P = X`, so the Pauli `Z` is the odd peripheral eigenoperator of the channel built from letters `X, Y`; the kept one grades by `P = Z` with `X` odd. They are unitarily equivalent as abstract examples but not as *notebook* examples, because the notebook's grading is always `P = diag(+1,-1) = Z`. The cut draft also contained the cleaner statement of the bipartite case: a bipartite Ramanujan Cayley graph gives a period-two graded channel in which the even eigenvalue `-1` is *allowed* rather than excluded.
- Lead: keep the `P = X` version as a reminder that the grading is a choice — the same channel is a mixing graded expander or a period-two one depending on which Pauli is called the parity. Any theorem that quantifies over gradings should say so.
- Where: `2026-09-15T08-37-49.txt:192,230`; `notes/ramanujan-graded/finite/finite_checks.py:161`

### G4-T16-1 Diagnostic scripts as regression oracles, explicitly not as evidence
- Absorbs: L10-034
- Class: EXPLORED-registered
- Raised by: subagent
- What: Eight diagnostics were written and saved with JSON/TXT output — `cusp_bridge_diagnostic.py`, `positivity-products-check.py`, `graded_channels_checks.py`, `regular_cmps_decay_check.py`, `regular_cmps_decay_exact.py`, `riemann_selberg_toy_modes.py`, `riemann_vs_selberg_cmps_check.py`, `cmps_renewal_check.py` — all reproducible offline. Every lane insists the algebra, not the floating point, carries the claims. One number is load-bearing: the three-mode on-line centered defect norm is about 2.2544, i.e. it is not zero under RH.
- Lead: reuse them as regression oracles for any arithmetic candidate.
- Where: `notes/rh-strategy-2026-09-19/cusp-bridge.md:78,109,126`; `graded-channels.md:163-165`

### G4-T16-2 Small normalisation and convention errors caught in flight
- Absorbs: L10-035, L10-091, L14-019
- Class: EXPLORED-registered
- Raised by: subagent
- What: Three worth remembering. (a) A NumPy integer failed JSON serialization at export while all mathematical assertions passed. (b) SymPy's integer-polynomial `gcd` retains the common constant factor 5 in the denominator and its derivative, so a simple-pole assertion must check `degree(gcd) == 0`, not `gcd == 1` — a check-normalization issue, not a repeated pole. (c) The brief wrote `Tr_{M_n ⊗ M_n^*} e^{tL}`, but that space has dimension `n^4` and is the space of superoperators; `e^{tL}` acts on the `n^2`-dimensional state space, so the intended trace is `Tr_{M_n}`. The same confusion would quadruple every dimension count in a cMPS bond-space estimate.
- Lead: adopt the gcd-degree convention in any future coprimality assertion, and assert visibility of a pole via exact coprimality and denominator degree, never via a residue magnitude threshold (the `H + P/100` residues, ~4.6e-5 and 1.6e-4, are only indicative; the degree-eight coprime denominator is the proof).
- Where: `notes/rh-strategy-2026-09-19/graded-channels.md:49,170-172`; `riemann-vs-selberg-cmps.md:100`; `2026-09-12T17-21-49.txt:83`

### G4-T16-3 Recovery snapshots, and the off-site copy that was never made
- Absorbs: L10-018, L17-003, L17-018
- Class: PARTIAL
- Raised by: TJO
- What: TJO's directive "I want the agent work to be continuously written so it is not lost", issued after only two agents had been spawned, changed the working method for the whole session: every agent wrote its report to disk before reporting in chat, and the orchestrator built `scripts/research_checkpoint.py`. Snapshots are written to a `.partial` file, every archived byte is read back against an embedded per-file SHA-256 manifest, and only then is the file renamed and given an external `.sha256` receipt plus a `LATEST-{full,session}.json` pointer; archives exclude `.git`, `.recovery`, caches and symlinks, reject absolute or `..` member paths, record the base commit, and crucially include the git-ignored `refs/src/` cache. A deliberately corrupted archive was verified to be rejected. They restore the working tree, not git history.
- Lead: the one residual risk the orchestrator flagged himself was never mitigated — the archives sit on the same disk as the repository. One `cp` of the latest full archive and its receipt to another disk closes it.
- Where: `notes/rh-strategy-2026-09-19/RECOVERY.md:44-48`; `2026-09-19T11-20-25.txt:37,80,426`

### G4-T16-4 The AI-authorship statements in both read papers
- Absorbs: L10-112
- Class: EXPLORED-registered
- Raised by: paper
- What: Shang (arXiv:2609.12284): "The Lindbladian construction and the complexity analysis were developed through multiple rounds of discussion between the author and the GPT6 Astra, where AI makes the main technical contributions." Becker-Zworski (arXiv:2609.13121): the appendix is credited to "Chat GPT 6" and "the key Volterra factorisation argument was suggestedby ChatGPT" (typo verbatim).
- Lead: relevant precedent for the repo's own prover-lane methodology (Codex/Astra as prover, Opus as refuter).
- Where: `notes/extract/2609.12284-reading.md:26-27`; `2609.13121-reading.md:17-18`

### G4-T16-5 A bouquet is not a Watanabe-Fukumizu graph: Theorem 1 is a loop-admitting extension
- Absorbs: L10-136, L10-137, L10-138
- Class: EXPLORED-registered
- Raised by: reviewer
- What: WF edges are two-element subsets of `V`, so loops and multiple edges are excluded; their `d_i` counts hyperedges (`D/2` on a bouquet, not `D`); and their own scalar Ihara-Bass specialisation evaluates on a bouquet to `(1-u^2)^{D/2-1}(1 - u + (D/2-1)u^2)`, which is **wrong** — the truth is `(1-u^2)^{D/2-1}(1 - Du + (D-1)u^2)`. The algebra of the identification is nonetheless exactly right (push-through for `A`, `i ↔ bar i` relabelling for `D`, the pair prefactor, no dropped weight hypothesis), verified numerically on a bouquet; and the order-of-composition and source-versus-target-weight differences wash out of `det(1 - u·)` because reversal is a bijection of cyclically non-backtracking sequences and, with `d = diag(uE_e)`, `M = dB` while `T = Bd`, so Sylvester gives equality (verified to 4e-16). One document could decide the priority question and has not been fetched: the NIPS 2009 supplementary material, which `1103.0605` says contains a direct proof of the corollary without hypergraphs.
- Lead: adopt the reviewer's draft wording and add the reversal-bijection/Sylvester sentence; fetch the NIPS supplement. Do **not** let this stand as a priority concession — for arbitrary non-invertible weights on a bouquet, no local source covers the case. (Noted in passing: WF are internally inconsistent here, their hypergraph definition giving the reverse of their graph definition.)
- Where: `notes/reviews/provenance-2026-09-12.md:91-115,140-173,328-345`

### G4-T16-6 Fifteen citation addresses that do not resolve, and two prior-art glosses
- Absorbs: L10-139, L10-140, L10-141, L10-142
- Class: EXPLORED-registered
- Raised by: reviewer
- What: An adversarial provenance review of 39 citations found that **no quoted string is misquoted or fabricated**, but 11 citations name a nonexistent file (`1801.00876` → `tenseur9.tex`, `2304.05714` → `PT-RC_reloaded.tex`, `0706.0556` → `sd10.tex`, `0709.1142` → `main.tex` not `expand.tex`, `2309.15873` → `AiM_Final.tex`, `2405.04361` → `v3.tex`), 2 point past EOF (`2204.06424:main.tex:3068` and `:3095-3096` in a 2342-line file; the real loci are `main.bbl:30` and `:94,100`), and 2 ranges exclude the quote they label. Two glosses also need rewording: Matsuura-Ohta explicitly extend from finite groups to `U(N_c)`, which refutes "for a representation of *any* group" but is *better* for the repo's claim 3 since `rho_adj` of `U(N_c)` is precisely the notebook's object; and "finite Galois group" is an inference, since "finite" appears nowhere in the local sources (though the downstream conclusion stands — `Ad(U_i)` for generic unitaries generates an infinite group, so the notebook's object is not literally a Stark-Terras L-function). Finally, three vectorisation conventions are in conflict: `A_X = sum_i U_i ⊗ conj U_i` in the prior-art note, `Ad(A) = conj A ⊗ A` in the theorem note, and `rho_adj(U_e) = U_e ⊗ U_e†` in MO.
- Lead: rewrite the filenames and ranges — `refs/README.md` promises re-checkability against these paths and 11 of them do not resolve. Reword the gloss and claim the upside. Fix one vectorisation convention everywhere; conventions of this kind have already caused two sign errors elsewhere in the repo.
- Where: `notes/reviews/provenance-2026-09-12.md:9-13,77-79,248-251,260-290,329-336`

### G4-T16-7 The Theorem 1 algebra review: six small repairs, all with wording supplied
- Absorbs: L10-143, L10-144, L10-145, L10-146, L10-147, L10-148
- Class: EXPLORED-registered
- Raised by: reviewer
- What: A REFUTE-stance verification returned VALID for thm1/cor2/cor3/cor4 with six minor repairs. (a) Theorem 1's "identity of rational functions" clause is redundant and mildly misleading: the steps are valid *pointwise* at any single `u` satisfying ASSUME; nothing needs small `|u|`, a Neumann series or continuation, and the ASSUME set is the cofinite complement of the zero locus of `prod_p det(1 - u^2 E_bar i E_i)` — verified numerically at `|u|/r` up to 32, outside the Neumann disc, to `1e-14`. (b) The norm bound `min_i ||E_bar i E_i||^{-1/2}` is undefined when some `E_bar i E_i = 0`, is better written `(max_i ||E_bar i E_i||)^{-1/2}`, and needs a submultiplicative norm that the note never specifies. (c) Corollary 3 divides by `1 - u^2` without stating the exclusion, although the conclusion is an identity of polynomials. (d) Corollary 4's "as they partly do in Corollary 3" is false at `D = 2`, where the exponent `N(D-2)/2 = 0` makes the cancellation total; the same step also skips the case where the second factor has a pole. (e) The invertibility hypothesis "for all `i`" could be relaxed to one representative per pair, since `det(1 - BC) = det(1 - CB)` transfers it — a free strengthening, never applied. (f) `scripts/qihara_general.py` tests the equivalent `1 - uM(u)` form, so the *displayed* identity `det(1 + D(u) - A(u))` is never evaluated; two lines would close the gap. The script also has docstring/label drift, `w5` assigned twice, a `pref` product over a `set` with nondeterministic iteration order, and an `exact_check` drawing random rationals from an RNG shared with the float checks, so the "exact" instances are not reproducible independently of execution order.
- Lead: apply the six repairs (exact replacement wording was supplied for each) and give the exact checks a separate RNG.
- Where: `notes/reviews/theorem1-algebra-2026-09-12.md:19-107,161-179`; `notes/reviews/provenance-2026-09-12.md:303-320`

### G4-T16-8 Discrimination controls: write a knowingly-wrong variant and confirm the test catches it
- Absorbs: L10-149
- Class: EXPLORED-registered
- Raised by: reviewer
- What: The reviewer wrote its tests from the *statement*, not the code, and added two deliberately-wrong variants — substituting `(1 - u^2 E_i E_bar i)^{-1}` inside `A` and `D`, and multiplying the resolvent on the left — both of which come out unequal, proving the tests are ordering- and side-sensitive. It also closed coverage gaps in the author's script (`D = 2` was never tested, nor singular/nilpotent/zero `E`, nor `u` outside the Neumann disc); all pass.
- Lead: adopt the pattern for future numerical verification. Several of the 2026-09-19 lanes' scripts assert only that the right thing passes.
- Where: `notes/reviews/theorem1-algebra-2026-09-12.md:69-98,162-163`

### G4-T16-9 Recovering a lost codex output by replaying `apply_patch` calls from the rollout log
- Absorbs: L14-042
- Class: EXPLORED-registered
- Raised by: prover
- What: After the first 09-12 session the harness overwrote `notes/selberg/astra-proofs.md` with the prover's final chat message, leaving a 2-line file. Rather than rewriting from memory the prover located its own rollout JSONL under `~/.codex/sessions/2026/09/12/`, extracted the five `custom_tool_call` entries whose input starts `text(await tools.apply_patch(`, JSON-decoded each patch, deleted the corrupted file and replayed the patches through the `apply_patch` binary in order — restoring the file byte for byte.
- Lead: a reusable recovery procedure for any lost codex output, and the reason the transcripts contain complete patch bodies at all. It also explains the truncation pattern (the extractor caps lines at 20 000 characters). Worth writing into the env-quirks notes.
- Where: `2026-09-12T12-54-39.txt:161-232`

### G4-T16-10 CAS strategy for cMPS checks: verify the Kraus identities, evaluate the norm numerically
- Absorbs: L16-013
- Class: EXPLORED-registered
- Raised by: prover
- What: The first full run of 13 example scripts had exactly one failing check: SymPy would not simplify a square root arising in a sampled-channel expression under the assumption `t > 0`. Rather than fight the CAS the prover replaced that check by direct Kraus completeness checks — `sum_a R_a†R_a + Q + Q† = 0` plus nilpotency of the fermionic jump.
- Lead: for cMPS checks, verify the defining Kraus/Lindblad identities symbolically and evaluate the norm numerically, rather than asking a CAS to simplify a symbolic time-dependent norm. The same trap will recur in every continuous-length example.
- Where: `2026-09-14T16-38-51.txt:278-280`

### G4-T16-11 The four-lane design, including a parent audit lane that was erased
- Absorbs: L17-005
- Class: EXPLORED-registered
- Raised by: orchestrator
- What: The first `SESSION.md` listed four planned lanes: (1) cusp/scattering bridge and spectral positivity; (2) Weil positivity, tensor amplification, arithmetic product substitutes; (3) graded channels, Lindbladians, finite models and no-go constraints; and (4) **parent: repository/status audit, source preservation, cross-review, ranked synthesis**. The fourth disappeared when `SESSION.md` was rewritten, although it was executed — it is why `cmps-renewal-bridge.md` exists and why the lane reports carry cross-review sections.
- Lead: the design principle worth keeping is that a fan-out of this kind needs an explicit fourth "parent" lane for audit, provenance and synthesis, not just a dispatcher.
- Where: `2026-09-19T11-20-25.txt:27,298`

### G4-T16-12 The session's own lead lives outside the ledgered directory
- Absorbs: L17-008, L17-009
- Class: EXPLORED-registered
- Raised by: orchestrator
- What: The `HANDOFF.md` insert states the main lead in three sentences — a regular fermionic cMPS with a faithful mixed stationary bond has a physical two-point function selecting a closed four-mode sector; its quadratic fermion structure supplies observable closure; separate reflection and coercivity conditions enforce a common width; perturbations distinguish these requirements — plus what the operator lane delivered. The worklog records the shutdown validation: reference manifest passed, `make check` passed with 357 claims and zero errors or warnings, six saved diagnostics reran, session recovery extraction/hash verification passed and a corrupted archive was rejected. The claim-status snapshot taken at the session start is a useful baseline: 357 rows — 124 proved, 96 sketched, 59 cited, 34 numerical, 34 assumed, 7 open, 3 conjectured; no status was promoted by any of the five lanes, by design.
- Lead: `HANDOFF.md` is the paragraph a future session will actually read first, so it is worth checking that it still matches whatever this ledger concludes.
- Where: `HANDOFF.md:5`; `docs/worklog/2026-09-19.md`; `2026-09-19T11-20-25.txt:471,618`

### G4-T16-13 Subagent shells had no network egress; route downloads through the parent
- Absorbs: L17-010
- Class: EXPLORED-registered
- Raised by: subagent
- What: The cusp lane tried to fetch `https://arxiv.org/src/1712.07832` from inside its own sandbox and got `urlopen error [Errno -3] Temporary failure in name resolution`; the parent then fetched the same e-print with an escalated `curl` and unpacked it to `refs/src/1712.07832/`. The same pattern repeated for Uetake: the subagent could open pages with the web tool but not download, so the parent downloaded the publisher PDF under escalation and ran `pdfinfo`/`pdftotext`.
- Lead: in future fan-outs route all downloads through the parent from the start; subagents should use the web tool for discovery only and hand URLs up. Doing otherwise costs a round trip per source.
- Where: `2026-09-19T11-22-06.txt:60,126,325`; `cusp-bridge-sources/1712.07832/retrieval.json`

### G4-T16-14 The BLAS-thread CI fixture, the gate's thread pinning, and the exemption rule
- Absorbs: L17-016, L17-017, L17-019
- Class: PARTIAL
- Raised by: orchestrator
- What: The pre-commit hook re-runs seeded scripts and diffs them against `outputs/`, and two fixtures turned out not to be thread-count-invariant. `scripts/qihara_general.py` prints "trace formula m=1..4: max error 5.5e-12" at 2, 4 and 8 BLAS threads but **3.7e-12 at one thread**, so a single-threaded CI run fails; only the second fixture was fixed, by adding `+ 0.0` after rounding in `scripts/graded_ramanujan.py` (a display-only change, since the assertions use the unrounded array). During shutdown the hook stalled with a single Python check oversubscribing about 64 cores through BLAS; it was killed and rerun with `OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2`, which reproduced the recorded outputs. Separately `labbook_check.py`'s exemption list became a named set `maintenance_scripts = {labbook_check.py, transcript_to_md.py, research_checkpoint.py}` with the documented criterion "maintenance tools do not assert mathematical claims or produce evidence".
- Lead: `qihara_general.py` still embeds a thread-dependent printed rounding error in a committed fixture — a live reproducibility bug in the repo's own gate. Either print fewer digits, assert a bound instead of a value, or pin the thread count (to 2) inside `scripts/ci_local.sh` rather than relying on the caller's environment.
- Where: `2026-09-19T11-20-25.txt:410,526-618`; `docs/worklog/2026-09-19.md`

### G4-T17-1 Cusp next test 1: extend the Gram/exit identity to generalized Laurent (Jordan) data
- Absorbs: L10-029
- Class: LEAD-unpursued
- Raised by: subagent
- What: Start with a synthetic double scattering pole, take all bivariate Laurent coefficients of Maass-Selberg including logarithmic cusp terms, compute the resulting confluent Cauchy matrix and its dissipative generator, and compare with repeated-zero Hardy kernel derivatives. Success is an explicit positive Gram identity plus a matching Jordan chain preserving algebraic multiplicity; failure is an unavoidable extra boundary term or chain-length mismatch, which would isolate a real obstruction.
- Lead: ranked first by its lane and called "the quickest useful theorem", and it avoids silently assuming zero simplicity. Note: a positive centered unitary form on the full Jordan chain would require semisimplicity and is *stronger* than RH.
- Where: `notes/rh-strategy-2026-09-19/cusp-bridge.md:96`

### G4-T17-2 Cusp next test 2: construct the actual noncompact first-band pushforward on regular data
- Absorbs: L10-030
- Class: LEAD-unpursued
- Raised by: subagent
- What: Use Bonthonneau-Weich's resolvent, start from one scattering pole, and match its distributional state to the Eisenstein Laurent coefficient through the Poisson transform. Success is a finite-rank Riesz range, wavefront/cusp-growth conditions, and a nonzero multiplicity-preserving pushforward at `lambda = s - 1` with the sign of `X` explicitly fixed. Failure would be a proof that the pole occurs only in a related determinant or a different flow sector — in which case it would be inappropriate to import compact DFG positivity at all.
- Lead: this is the concrete version of closing H-CUSP-BRIDGE.
- Where: `notes/rh-strategy-2026-09-19/cusp-bridge.md:98`; `refs/src/1712.07832/preprint.tex:143-164`

### G4-T17-3 Cusp next test 3: derive the cMPS exit map `j` and `H` from a cusp boundary / Schur-complement / Mayer-tail construction
- Absorbs: L10-031
- Class: LEAD-unpursued
- Raised by: subagent
- What: Seek analytic formulas for `j` and `H` from modular branches or prime input, then compare finite approximants against the Cauchy Gram realization. The explicit failure condition is stated in advance: `j` or `H` is fitted from a supplied list of zero locations, or cutoffs change the divisor uncontrollably.
- Lead: the matrix construction of the cusp Gram realization is the debugging oracle, and the Mayer-tail route is the only *letters-first* suggestion in that lane.
- Where: `notes/rh-strategy-2026-09-19/cusp-bridge.md:100`

### G4-T17-4 Cusp next test 4: SHW-style mixed rebound on the modal bond
- Absorbs: L10-032
- Class: LEAD-unpursued
- Raised by: subagent
- What: In the finite Gram realization, try a Siemon-Holevo-Werner rebound density on the modal bond and compute which coherence sectors survive. Success is a symmetry or invariant subspace preserving the original decay generator while yielding a nontrivial stationary density; failure is that rebounding alters every zero mode, or the stationary state stays absorbing and pure. Recorded caution: no finite approximation can by itself furnish the infinite critical KMS state. Echoed as priority 2 by the graded-channels lane; the finite criterion it needs (`M >= 0`) *was* proved.
- Lead: mixing the rebound in is the only route from the pure absorbing vacuum to the BC-style mixed stationary bond.
- Where: `notes/rh-strategy-2026-09-19/cusp-bridge.md:102`; `graded-channels.md:130-134`

### G4-T17-5 The positivity lane's three ranked next tests, each with a stop condition
- Absorbs: L10-052
- Class: LEAD-unpursued
- Raised by: subagent
- What: (1) Compute the arithmetic cMPS time-bin covariance and exit ratio around the `log 2` and `log 3` ridges with the correct normalization `B = 2A + 1/2`; stop if it is analytic at `log 2`, if it assigns an independent positive block per prime, or if it produces the density-operator pair-difference spectrum instead of the amplitude modes. (2) Find nonlinear innovations for the prime-defined Toeplitz matrices — an arithmetic formula for each Schur pivot `d - k*K^{-1}k`; a putative negative vector must be interval-certified and converted to a smooth test before being interpreted as mathematical failure. (3) Audit product loss and spectral survival for `k = 1,2,3`, reporting surviving scaled poles, even/odd cancellation and growth exponents; stop if all bounds are `epsilon_k = k epsilon_1`, or if the pole is erased by a supertrace.
- Lead: the lane's own instruction is "only pursue uniform width after the actual arithmetic bridge is verified".
- Where: `notes/rh-strategy-2026-09-19/positivity-products.md:156-160`

### G4-T17-6 Graded-channels priority 1: deform the *letters*, not the eigenvalues
- Absorbs: L10-066
- Class: LEAD-unpursued
- Raised by: subagent
- What: From the `2|2` toy take `R = X ⊗ lowering`, `H = diag(H_+, H_-)`, then permit arithmetic finite-level character actions on the internal index. Impose parity, `R^2 = 0`, the canonical gauge and a faithful stationary bond *before* seeking uniform widths; form the insertion-generated Krylov space and its observable quotient with the parity-twisted transfer, and derive its polynomial/intertwining relations directly from the letters.
- Lead: the lane's own framing — "the immediate experiment is parameter classification of this `2|2` family and exact residues, not an expensive search over guessed zeta ordinates". This was the lane's highest priority and was never started.
- Where: `notes/rh-strategy-2026-09-19/graded-channels.md:122-128`

### G4-T17-7 Graded-channels priority 3: an SDP feasibility test of the commutator-frame defect inside the BC cone
- Absorbs: L10-069
- Class: LEAD-unpursued
- Raised by: subagent
- What: For primes `p = 3,5,7`, impose the linear stationary/covariance constraints and examine the Hermitian part on a candidate observable coherence space. For a tracial model with a fixed metric, `C_O*C_O = 2cI` is *linear* in the Kossakowski matrix, so Choi positivity makes this a concrete semidefinite feasibility problem. Screening input: the BC cone already contains generators with full Weil/Galois/parity covariance, a unique tracial stationary density and *unequal* odd rates, while imposing all Weyl covariance collapses to pure depolarization and kills the oscillations.
- Lead: full covariance plus stationarity alone has already failed, so rerunning that ansatz is not useful — the new content would have to be the *observable subspace* restriction. For nontracial or nonnormal models use the appropriate weighted form and do not import the HS no-go.
- Where: `notes/rh-strategy-2026-09-19/graded-channels.md:136-140`; `04d_bc_symmetry_generators.tex:143-182`

### G4-T17-8 Graded-channels priority 4: a regulator theorem separating the four limits
- Absorbs: L10-070
- Class: LEAD-unpursued
- Raised by: subagent
- What: Each approximant must specify its regular source/sink spaces and physical observable transfer; then one checks local uniform convergence of the correlation resolvent on contours isolating poles, convergence of residues and their ranks, controlled noncancellation, and separately persistence of the positive metric — with bond dimension, prime cutoff, continuum spacing and temperature limits kept apart. A finite correlation's scalar pole order alone does not certify geometric or algebraic modal multiplicities.
- Lead: this is the step between any finite success and an actual theorem, and it is where the `C_n` conditioning counterexample bites.
- Where: `notes/rh-strategy-2026-09-19/graded-channels.md:142-146`; `03d_graded_ramanujan_continuum.tex:78-97`

### G4-T17-9 A 3x3 non-normal toy: is a weighted-norm decay bound the same as a sectoral Lyapunov criterion?
- Absorbs: L10-125
- Class: LEAD-unpursued
- Raised by: subagent
- What: Check on a `3x3` non-normal toy whether a Becker-Zworski-type weighted-norm bound with a `t`-independent constant is equivalent to the Lyapunov criterion `A†G + GA <= -2 gamma G` restricted to the slowest sector.
- Lead: small and cheap, and it would settle in an afternoon whether the weighted-norm decay statement and the Lyapunov certificate are the same thing sector by sector — directly the question behind the exit-energy identity and the minimal missing identity.
- Where: `notes/extract/2609.13121-reading.md:166-167`

### G4-T17-10 The four ranked tasks with nobody on them at shutdown
- Absorbs: L17-020
- Class: LEAD-unpursued
- Raised by: orchestrator
- What: When TJO said "shut it all down", four written-down tasks had no agent working on them: (i) extend the cusp Gram/exit identity to generalized Laurent/Jordan data at a synthetic double scattering pole; (ii) test SHW-style mixed rebound on the finite Gram realization; (iii) the arithmetic product / Deligne tensor amplification lane, explicitly deferred until a product with sublinear growth loss is identified; (iv) the positivity lane's nonlinear Schur/innovation recurrence for the sparse prime Toeplitz updates. Both second-round agents had in fact finished writing their reports before the interrupt reached them — neither was cut off mid-derivation, both mid-housekeeping.
- Lead: (i) is the cheapest and most informative, and it is the one that avoids silently assuming zero simplicity. The one loose thread from the interrupted agents: `riemann_selberg_modes` was interrupted at the exact moment it went to verify that `refs/src/1403.0256/RuelleResonForHn.tex` exists, so that citation is unverified.
- Where: `2026-09-19T11-20-25.txt:344,455-471`; `2026-09-19T11-22-06.txt:105`; `2026-09-19T11-22-16.txt:113`

## Top leads in this group

1. **G4-T4-4** (`Q-8`, the general-`eta` key lemma) — one clean statement would cover zeta and graphs at once and might remove CCM's parity hypothesis, which CCM themselves list among their missing steps; verified numerically in that generality, never written down.
2. **G4-T5-2** (`Q-3`, is even-simple *equivalent* to Ramanujan?) — a cheap search over small regular graphs would decide whether CCM's auxiliary hypothesis is actually a restatement of the target. Proposed, never run.
3. **G4-T3-3** with **G4-T3-2** (`Q-2` and `Q-7`) — the under-resolved law is a discrete prolate/Slepian problem and DPSS is the named candidate answer; if `1 - chi_4(lambda)` is the continuous limit of the graph rate, the graph gives a computable handle on the constant governing the zeta accuracy law.
4. **G4-T10-9** (the modewise cusp leakage estimate) — the quantifier-correct form of the RH-sized inequality, `||jv||^2 >= (1/2)||v||^2` for retained resonant modes only, with Uetake's Poincaré profiles as non-zero-defined test data.
5. **G4-T9-4** (the intertwiner `WT = TC`) — an exact algebraic identity connecting two established resonance pictures, with four named analytic conditions, and it would derive the half-shift at operator level **without using RH**.
6. **G4-T12-11** (the five-step arithmetic programme) with its smallest experiment: compute the signed Heisenberg image of the first proposed prime/cusp letter and measure the component outside the generating family — the arithmetic analogue of the `P/100` term that kills the mechanism before any spectral numerics.
7. **G4-T17-1** (cusp Jordan data) — called "the quickest useful theorem" by its own lane, avoids assuming zero simplicity, and a failure isolates a genuine obstruction.
8. **G4-T14-4** with **G4-T14-5** (`||Z_t|| = 1` and the condition-number test) — the biggest recorded negative is marked unreviewed and a second reader was requested; one Blaschke-truncation computation would settle it and simultaneously test TJO's non-normality hypothesis. Ranked follow-up 1 in two lanes, never run.
9. **G4-T7-1** (exact-rational inertia) — `D T D` is an exact integer matrix, so the certificate step that failed at scale in `zst` can be replaced by exact arithmetic for every integer-atom object. Filed as "an opportunity, not a requirement".
10. **G4-T5-3**, the inverse problem — recover the offending adjacency eigenvalue from the slope of `log(-eps_M)` alone; the lane says outright "if this works it is a genuinely new diagnostic", and it was never run. *(small but consequential)*
11. **G4-T5-4** — `K_3 □ Q_3` and the ten-letter Pauli channel are ready-made objects with verified Jordan blocks at the Ramanujan boundary, the one case where Weil positivity holds but no Hilbert-Polya inner product exists, and neither has been run through `ihz`. *(small but consequential)*
12. **G4-T7-1**, the tail roots — they cluster just past `N`, come in pairs and reach `31 N`; nobody asked what they are, yet completeness-by-count, hence every certified table, depends on accounting for them. *(small but consequential)*
13. **G4-T12-14** — the `sigma`-metric dissipation identity says the GNS metric of the stationary state *cannot* certify uniform decay on a sector containing a fermionic jump, contradicting the most obvious guess in the Phantasm programme. Stated in one message, no evidence script. *(small but consequential)*
14. **G4-T13-12** — the missing invariant-sector argument is a checkable linear condition (`Tr(CX) = 0` on the zero-mode subspace) that would decide in an afternoon whether any reset completion can keep the zeros. *(small but consequential)*
15. **G4-T10-7**, the PT reading — RH becomes "the unbroken PT regime" for the arithmetic operator, and the PT literature has techniques for proving unbrokenness; raised in one sentence and dropped. Alongside it: **G4-T13-7**, Arveson's units, a whole structural theory of no-event semigroups behind a single quoted line, and **G4-T11-3**, the two-line `Psi(2A)` / `4Psi(A) - Psi(2A)` diagnostic any claimed sum-of-squares factorization must pass. *(all small but consequential)*

## Dead routes (consolidated)

**CCM sidequest — method and certification**
- Interval `LDL^T` inertia certification at scale: fails from `x = 20`, input radii amplified by the squared condition number (`1e192`). — G4-T7-1, `benchmark.md:66-71`
- The QR candidate generator for secular roots: dominates runtime and its precision cannot go below the rank-one term's dynamic range (~`5.5x` digits). Kept only as a fallback. — G4-T7-1, `benchmark.md:72-77`
- Plain interval evaluation of the secular derivative for far-out roots: useless; a mean-value form is mandatory. — G4-T7-1, `report-2026-09-18.md:50-52`
- Global root isolation by ball arithmetic in `zst`: hopeless, because `sum xi_j = 1` amplifies `xi` by 18-28 digits. — `zst/README.md:39-43`
- Completeness of the root list by search range: two positive roots lie far beyond the last pole (`s ~ 107, 339` at `N = 40`). Completeness must be by count. — `zst/README.md:41-43`
- `arb_mat_eig_enclosure_rump` used directly for the eigenvector: returns its inflated containment box. — `zst/README.md:37-39`
- `arb_fmpz_poly_complex_roots` on a raw characteristic polynomial: never terminates on a repeated root; square-free-factor first. — G4-T7-2, `code-audit.md:163-201`
- `acb_mat_eig_multiple_rump` as a primary truth route: failed at `n = 24` even at matching precision; demoted to a cross-check. — G4-T7-2, `code-audit.md:128-161`
- The similarity `D T D^{-1}`: not symmetric, still irrational below the diagonal, breaks the `arb_mat_cho`/`ldl` family. "Do not use this transform." — `code-audit.md:326-335`
- `nf_elem`/antic exact arithmetic over `Q(sqrt q)`: buys nothing, since the `t_k` become balls anyway and the useful congruence is already integral. — `code-audit.md:280-298`
- The window heuristic "`M >= diameter`": superseded by `K = R+1`. — G4-T5-1, `ihara/plan.md:352-354`

**CCM sidequest — mathematics**
- The self-adjoint angle operator `diag(2 pi n/K)` as the discrete `D`: `(n-m)That_{nm}` is not of the form `c_n - c_m`; measured commutator rank 3. — G4-T4-3, `theory.md:269-272`
- The nilpotent truncated shift as the discrete `D`: not invertible, `spec(S) = {0}`, `S^*TS != T`. — G4-T4-3, `theory.md:274-277`
- `eta =` all-ones in the position basis: `xi`-independent determinant `(s^K-1)/(s-1)`; transports no information. — G4-T4-3, `numerics.md:281-286`
- `eta =` all-ones in the DFT basis: returns `xi`'s coefficients rotated by one; `ang.err = 0.89`. — G4-T4-3, `numerics.md:288-290`
- `CS` Proposition `finmain` taken literally with all-ones `eta`: roots real but wrong, `ang.err = 0.52` at an exact window. — `numerics.md:272-279`
- The additive key-lemma family when `xi` is odd: `eta` is `gamma`-even in every additive variant, so `<eta|xi> = 0` — which is what happens for every non-Ramanujan object. — `numerics.md:292-296`
- A canonical `xi` in the over-resolved regime by minimal degree or minimum norm: both break the circle. — G4-T4-5, `theory.md:543-549`
- Interpreting the output for an irregular graph: structurally impossible; output is always `2M` circle points, `pt.err` saturates near 0.20. — G4-T6-4, `numerics.md:174-182`
- Running the chain on a mixed-parity retained divisor: indefinite by construction, independently of RH. — G4-T6-3, `theory.md:862-871`
- Expecting a graph to test CCM's missing step: a finite divisor has a critical window, and there is no theta function, self-dual Gaussian or prolate tower over `Z`. — G4-T1-3, `theory.md:635-641,659-669`

**RH strategy — positivity and amplification**
- Sum of independent positive prime-power blocks for the Suzuki kernel: each block is indefinite at first visibility. — G4-T11-1, `positivity-products.md:24-32`
- Re-proving `Psi(t) >= 0` as new: Suzuki already has `Psi >= 0 ⇔ RH` and `Psi = O(1) ⇔ RH`. — G4-T11-2, `positivity-products.md:38`
- Ordinary tensor powers as Deligne-style amplification: `epsilon_k = kc`, no improvement; ordinary graph transfer powers leave the interesting spectrum as poles. — G4-T11-4, `positivity-products.md:15,52`
- Rosati/Frobenius-moduli positivity as an independent RH proof: the moduli are already an input. — G4-T11-4, `positivity-products.md:17`
- Any fixed finite-dimensional, time-homogeneous, bounded-generator cMPS amplitude model claiming the exact Suzuki covariance: real-analytic on the diagonal, but the true kernel has prime kinks `-log p/sqrt(p^k)`. — G4-T11-6, `positivity-products.md:144-152`

**RH strategy — cusp and operators**
- The naive Hadamard finite-part cusp pairing: leaves the **zero matrix**. — G4-T9-3, `cusp-bridge.md:26-30`
- Making the centered cusp flow unitary in the normalized cusp Gram: impossible for `N >= 2` even under RH (rank `N` against rank one). — G4-T9-3, `cusp-bridge.md:44-52`
- Demanding centered unitarity for every superposition in the physical norm: uniform widths with one rank-one exit *force* nonnormality. — G4-T10-3, `cusp-bridge.md:92,124`
- Hoping the Selberg `mu >= 1/4` gap settles the Riemann sector: `mu = 3/16 + gamma^2/4 + i gamma/4` is nonreal even under RH. — G4-T9-2, `SYNTHESIS.md:24-28`
- Deriving RH from CP + passivity + one channel + FE: the two-state toy at `g = 1/2` satisfies all of them with two distinct widths for `0 < w < 1/4`. — G4-T10-7, `riemann-vs-selberg-operators.md:102-114`
- Inferring uniform decay from reflection symmetry alone: weak drive keeps the reflection with widths ~0.0061 / ~0.4939, discriminant `-2399/10000`. — G4-T10-7, `riemann-vs-selberg-cmps.md:92`
- Importing `dom(A_c) = dom(L) ∩ K` from Uetake p.110: a compressed half-line translation generator allows nonzero boundary traces. — G4-T9-4, `riemann-vs-selberg-operators.md:80`
- Treating `S(tau)` and the raw Eisenstein `phi` as the same symbol: they differ by `(2i tau - 1)/(2i tau + 1)`, and Uetake's original LP matrix has yet another factor plus a pole at `p = -1/2`. — G4-T9-6, `riemann-vs-selberg-operators.md:74-78`
- The old Hardy kernel formula in shard 04 and `notes/riemann-channel-note.md`: `Z(t)* k_lambda = exp(-it conj(lambda))k_lambda` gives *growth* `exp(+beta t/2)`. **Not yet repaired.** — G4-T9-6, `04_riemann_channel.tex:71-75`

**RH strategy — channels and states**
- Assuming parity, CAR, CP and faithful stationarity give a common width: `bd = 0` is necessary and is implied by none of them. — G4-T12-4, `riemann-vs-selberg-cmps.md:43-56`
- Assuming grading alone protects observable mode selection: `0.01 P` is a quartic interaction that makes the denominator degree eight. — G4-T12-4, `riemann-vs-selberg-cmps.md:54,114`
- Adding dissipative bistochastic prime noise to a parity jump on the *full* odd block in the HS metric: forces all jumps scalar and `D = 0`. — G4-T12-5, `graded-channels.md:29-41`
- "RH because odd relaxation is an extremal expander rate": `E = (Ad I + Ad P)/2` kills the odd block; no universal floor. — G4-T12-6, `graded-channels.md:21`
- Imposing full Weyl covariance on the BC generator cone: collapses to pure depolarization and kills the oscillations; full Weil/Galois/parity covariance plus a unique tracial state still permits unequal odd rates. — G4-T17-7, `04d:143-182`
- Assuming a finite positive invariant metric survives a regulator limit: `C_n` has `lambda_min(G_n) = 1/(2n) -> 0` and the limit admits none. — G4-T12-10, `graded-channels.md:146`
- A biased diagonal BC cutoff state with a scalar measure-and-prepare reset: the reset numerator has determinant `-(1-2p)^2`, so only the uniform target works. — G4-T13-3, `cmps-renewal-bridge.md:57`
- A stable graded bond with a single homogeneous rank-one exit: one parity sector is forced to evolve unitarily. — G4-T13-5, `cmps-renewal-bridge.md:43-47`
- The `2|2` Pauli two-jump toy as a regular fermionic cMPS: `R_X^2 != 0` violates kinetic regularity, and remixing makes the anticommutator nonzero. — G4-T12-8, `2026-09-19T11-22-27.txt:69`
- The renewal fixed point at the vacuum: `Omega` is outside `K_S` and absorbing; the integral diverges. — G4-T13-10, `2026-09-12T21-42-08.txt:131`
- A worst-case trace-distance mixing-time form of RH for the absorbing-vacuum channel: `||Z_t|| = 1` for every `t` independently of RH (marked **unreviewed**). — G4-T14-4, `2609.12284-reading.md:153-167`
- A SUSY/Witten-index graded splitting as a ring-norm mechanism: the supertrace cancels the whole nonzero spectrum. — G4-T14-7, `2609.13121-reading.md:124-129`
- A single-jump "purified Gibbs"/Witten Lindbladian carrying the zeros: coherence rates are the spectrum of a self-adjoint `H >= 0`, hence real. — G4-T14-9, `2609.13121-reading.md:136-143`
- Mining the Lindblad-mixing literature for expanders/Ramanujan/cutoff: neither paper contains any. — G4-T14-10, `2609.12284-reading.md:183-185`

**Codex prover corrections — drafted statements shown false**
- `Lambda(sigma) = -partial_sigma log D(sigma)`: wrong sign; the flat-trace transform is `+partial_sigma log D`. — G4-T15-1
- "The graph analogue of `D` is `1/det(1-uT)`": false; it is `det(1-uT)` itself. — G4-T15-1
- "All first-band resonances on `Re sigma = -1/2` iff every `r_j` is real, `j >= 0`": false on every compact connected surface; the constant mode must be excluded. — G4-T15-2
- The cusp prime comb with *positive* weights and no boundary constant: the atoms are dips, and a `+1/2` archimedean constant is missing. — G4-T9-7
- "Both Kraus pairings iff every `B_i` is a scalar multiple of a unitary": false; `B†B = I` on the nose, disproved by `B = 2I`. — G4-T15-7
- "Give a Kraus counterexample where `spec(T)\S_0` is not conjugation-closed": no such example exists — every Kraus family is conjugation-symmetric. — G4-T15-7
- An `n = 1` adjoint-paired non-scalar-unitary example: logically impossible. — G4-T15-7
- "`mu -> r^2/mu`, the linear map": not linear; and `W = M` needs conjugation symmetry on top of reciprocal symmetry. — G4-T15-7
- The Dyson product without free propagators between jumps: false for noncommuting `K, R_j`. — G4-T15-6
- `Tr_{M_n ⊗ M_n^*} e^{tL}`: wrong space (`n^4`, superoperators); the intended trace is `Tr_{M_n}`. — G4-T16-2
- "`S` = the two trivial modes from the poles of `xi` at `s = 0, 1`": the notebook's `xi` is entire; take `S = ∅`. — G4-T15-9
- "Every zeta function has side A, a nonnegative count of rings": true in the stated Kraus settings only. — G4-T15-10
- Seed S2, "GUE positions with equal widths is the fingerprint of scalar loss": false; a tuned one-port realises equal widths at arbitrary positions. — G4-T15-11
- Seed S4, "positivity of the Hamiltonian makes a J-unitary monodromy similar to a unitary": two positive slabs give eigenvalues `diag(-16, -1/16)`. — G4-T15-11
- Seed S5, "each local Euler factor is inner in the channel half-plane": unimodular on the real line only. — G4-T15-11
- Seed S6, "what forbids superradiance here?": nothing does. — G4-T15-11
- The Artin-Schreier sign law `S_n = -(-eta(-1))^n conj(Tr E_g^n)`: false at `(q,a,n) = (3,(2,1),1)` and `(5,(1,1),2)`; the correction is a determinant on the **radical**. — G4-T15-14
- "Failure is confined to `q | n`": false; the exact criterion is `P(-eta(-1)) != 0`. — G4-T15-14
- The drafted graded super-transfer block: supertrace `-2` where the projective count is 10. — G4-T15-14
- "Each zero appears once as an odd mode plus once as its conjugate": the vacuum-decay model realises the **double** of the forced datum. — G4-T13-10
- "The formal population trace is the form factor `|Tr Z(t)|^2`": undefined; (G2) fails and a product of distributional traces does not exist. — G4-T15-18
- Closing the infinite-parity case by Landau on the diffuse part: blocked by negative prime atoms; proved only under `mu >= comb`. — G4-T15-15
- "H-MM1, take as given": not merely given — proved, and only on a specified stationary weighted space, as a *closure* of Minkowski sums. — G4-T15-17
- H-WEIL-REP's "up to a phase" Weyl covariance: too weak; centred exact covariance is required. — G4-T15-14
- The vertex-level Bass identity for every finite 2-complex: false on `∂Δ^3`; the universal replacement is the forbidden-transition Schur complement. — G4-T15-19
- "Links are generalised polygons ⇔ cubic collapse": not proved, explicitly declined. — G4-T15-19
- "The Cayley/Kraus twist is the `pi ⊗ conj pi`-isotypic block of the untwisted determinant": false; a covariant full-cover connection is pure gauge and Artin factors use quotient voltages. — `2026-09-13T10-23-10.txt:142` (theme 15)
- "The zeros of the total zeta are exactly the eigenvalues of the odd sector": false; chamber factors can cancel against edge factors. — `2026-09-13T10-23-10.txt:178` (theme 15)
- "`Tr E_{++} = sum_s ||a_s||_HS^2`", hence the HS proof of the genus bound: false; the correct trace is `sum_s |Tr a_s|^2`. — `2026-09-14T11-00-06.txt:114` (theme 15)
- "Place the eigenvalue `q` in the polarisation trace line": false whenever the fermionic couplings are active. — G4-T15-21
- "The cut rank of `psi(tr(x^3))` over `F_2` probes a non-quadratic obstruction": false — `x^3 = x^{1+2}` is quadratic in characteristic 2. — `2026-09-14T11-00-06.txt:114` (theme 15)
- "Exact three-species existence over `F_5` is open": superseded within the same session by a rational contraction certificate. — G4-T15-22
- "Full linear Weil covariance does not force equal odd decay rates", tested at `p = 5`: the assertion failed at `p = 5` and was re-established only at `p = 7` via a scalar-orbit perturbation of size `1/(4p^2)`; the smallest odd prime where the freedom is visible is 7. — `2026-09-13T12-11-30.txt:217,230` (theme 15)
- S3: the prime Lindbladian acts as a scalar on vacuum/Gauss coherences: no invariant scalar; explicit mod-3, `p = 2` counterexample. — `2026-09-14T14-56-39.txt:182` (theme 15)
- S4: the critical BC state is the pure vector state of `e_0` on `C(Zhat)`: Haar is represented by `e_0` but is not pure (`omega(1_{2Zhat}) = 1/2 != 1/4`). — `:197` (theme 15)
- S5: the vacuum-to-shell overlaps have `1/zeta(s)` as a factor: overlaps are nonnegative with zeta in the **numerator**; reciprocal zeta comes only from a separate multiset product. — `:197` (theme 15)
- S5: commuting jumps / the shell stay term / parity closure restore Euler weights: `pq` occurs twice as an ordered word; word multiplicity is `Omega(n)!/prod_p k_p!`. — `:197` (theme 15)
- S6: parity insertion performs the quotient by `Q^x`: two-dimensional counterexample; parity closure changes a boundary functional and imposes no quotient. — `:218` (theme 15)
- S6: Connes 1999 identifies this ring norm with an unconditional periodic-orbit trace: it proves a local cutoff formula and a finite-set-of-places formula only. — `:187,218` (theme 15)
- S7: a spectral line conversely supplies anti-Hermiticity: needs diagonalisability; explicit Jordan counterexample. — `:218` (theme 15)
- S8: reverse jumps at rate `lambda_p p^{-beta}` restore detailed balance: rate orientation backwards, and phase jumps still create coherences. — G4-T13-14
- The whole yolo guess `sum_p (1/p) D_{V_p ⊗ T_{log p}}` as an already-defined normal Lindbladian with an ordinary ring supertrace: the no-jump form diverges at rates `1/p`, and `e^{tL_F}` is bounded with bounded inverse, hence non-compact and not trace class. — `2026-09-14T14-56-39.txt:182,207` (theme 15)
- D1: the sub-system rule makes the odd sector a sub-MPS automatically: a weighted MPS can have the right counts without enumerating points, and TP is an extra equation. — G4-T15-27
- D4 (zeta conditions): inverse-closed letters give the FE for the ring zeta: true for the Hashimoto transfer after removing Bass factors, false for a raw doubled transfer (`B = diag(1,2)`). — `2026-09-14T16-38-51.txt:233` (theme 15)
- D5 (zeta conditions): `L(u, sgn) = ((1-mu)/(1-m^2u))^{1/2}` for the `Z/2` swap: the pair shift is not a `Z/2` cover; the genuine tiny example is the two-loop rose with voltages `0,0,1,1`. — `:250` (theme 15)
- D4 (graded Ramanujan): band iff circle, sector by sector: false — matching even and odd modes outside the band cancel from the zeta. — G4-T15-28
- D5 (graded Ramanujan): an odd-sector Alon-Boppana lower bound: refuted; Hastings' argument needs nonnegative word traces. — G4-T12-6
- The Weil-LPS examples are curves (printed genus 36): first reduces to numerator degree **4**; second has uncancelled poles on the critical circle. — G4-T15-29
- D2/D3/D7 (Selberg): the Ruelle supertrace satisfies the single-line condition, and the pullback form is positive: two shifted bands; degenerate pullback. — G4-T9-8
- D6 (Selberg): `lambda_1 >= 1/4` for the modular surface is open, and truncated Eisenstein positivity gives RH: known for the full modular group; truncation positivity holds throughout `0 < Re s_0 < 1/2`. — G4-T9-8
- D8 (Selberg): K-type parity is the Hodge form degree and grades the flow: `X` is odd under it, so it does not commute with the flow. — `2026-09-16T14-21-08.txt:288` (theme 9)
- "Theorem 1 is the one-vertex case of Watanabe-Fukumizu's corollary": a bouquet is not a WF graph, and their own scalar specialisation is *false* on a bouquet. — G4-T16-5
- "Artin-Ihara L-function for a representation of *any* group" (prior-art gloss): the source says finite groups, extended to `U(N_c)`. — G4-T16-6

## Bookkeeping issues

- `scripts/qihara_general.py` still prints a BLAS-thread-dependent rounding error (`5.5e-12` at 2/4/8 threads, `3.7e-12` at one) into a committed fixture, so the repo's own reproducibility gate can fail on a machine with a different thread count; `scripts/ci_local.sh` does not pin the thread count. — G4-T16-14, `docs/worklog/2026-09-19.md`
- `outputs/graded_ramanujan.txt` was edited to turn `-0.0` into `0.0` and the script now adds `+0.0` after rounding: display-only, but a fixture was changed during a shutdown rather than during review. — G4-T16-14
- The Hardy sign error in `report/sections/04_riemann_channel.tex:71-75` and `notes/riemann-channel-note.md:59-64` was diagnosed independently by two lanes and **deliberately left unrepaired**; so was the scattering-symbol normalisation `S(tau) = [(2i tau - 1)/(2i tau + 1)] phi(1/2 + i tau)`. — G4-T9-6
- Eleven citations in the 2026-09-12 provenance set name a nonexistent file, two point past EOF, and two ranges exclude the quote they label — although no quoted string is misquoted. `refs/README.md` promises re-checkability against those paths. — G4-T16-6
- `refs/src/1403.0256/RuelleResonForHn.tex` is cited in `riemann-vs-selberg-operators.md` as the compact first-band primary source, and the agent was interrupted at the exact moment it went to verify that the path exists. **Unverified.** — G4-T17-10
- Eight literature items in the CCM sidequest are unverified from primary text (Terras 2011's book content is "the single biggest gap"; Makhoul 1981's exact hypotheses matter mathematically), and six staged arXiv ids were never fetched — including Connes-Consani 2006.13771, the closest existing single-place analogue. — G4-T8-3
- Every inter-agent payload in the 2026-09-19 session is a Fernet token or an empty block, so the orchestrator's briefs and the subagents' reports back are **unrecoverable**; any ideation in a brief that no subagent acted on is gone. Future fan-outs should have the parent write each brief to disk as it sends it. — L17 coverage caveat
- `ihz` was built with testing discipline relaxed at TJO's request (no fuzz, no mutation), and `zst`'s mutation record covers only the pre-benchmark MVP although all `x >= 20` rows came from changed code; two real out-of-bounds reads in `secular.c` remain unfixed. — G4-T7-3
- The recovery archives live on the same disk as the repository and the off-site copy the orchestrator flagged was never made. — G4-T16-3
- The cusp diagnostic's three-mode centered defect norm was first written as "about 2.59" and silently corrected to "about 2.2544"; the number is load-bearing for the claim that the defect is nonzero under RH. — G4-T16-1
- The `ihz` code cites the notebook's own `report/sections/*.tex` for ground truth rather than a fetchable paper, so its correctness is only as good as the notebook's `stipulated` rows. — G4-T8-3
- Two condition names, C6curve and C6projective, cut different examples and both should stay in the condition ledger. — G4-T15-26
- The `x = 60` and `x = 80` certified spectra were lost to a cleanup mistake before their tables were extracted. — G4-T2-2
- Three conflicting vectorisation conventions are in use across the prior-art note, the theorem note and Matsuura-Ohta; conventions of this kind have already caused two sign errors in the repo. — G4-T16-6
- `scripts/graded_ramanujan.py` passes 79 checks but none of them tests its own printed genus claims, which are wrong by a wide margin. — G4-T15-29

## Audit

Total lane entries in the six files: **350**
(L09 = 92, L10 = 149, L14 = 42, L15 = 17, L16 = 26, L17 = 24; counted with `grep -c '^### L'`, no duplicate IDs.)

Absorbed: **350**. Every lane entry appears in the "Absorbs" list of exactly one digest item
(149 items across 17 themes). None was deliberately left out.

Per-lane absorption check: L09-001..092 all assigned; L10-001..149 all assigned; L14-001..042 all
assigned; L15-001..017 all assigned; L16-001..026 all assigned; L17-001..024 all assigned.

The lanes' own "Small but possibly consequential" and "Dead routes recorded" sections introduce no
new IDs — every bullet there points back to a numbered entry or to a source pointer, and each has
been folded into the corresponding digest item, the Top-leads list, or the consolidated dead-route
list above.
