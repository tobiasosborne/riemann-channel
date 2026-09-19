# Ihara zeta spectral triples: the CCM construction on a finite graph, what generalises, and the plan for MVP-2

Status: reading notes, a discrete theory lane (36 claims, `lanes/theory.md`), a literature lane
(`lanes/literature.md`), a code audit (`lanes/code-audit.md`), a notebook extraction
(`lanes/notebook-extract.md`) and an mpmath prototype (`ihara_proto.py`, `lanes/numerics.md`).
Nothing here is a registered lab-book claim. Sidequest of 2026-09-18, second vertical MVP after
`zst/` (`../plan.md`, `../report-2026-09-18.md`). Orchestrator: Claude Fable 5.1 (Opus lanes for
theory and numerics, Sonnet lanes for literature, code audit, extraction).

Sources cited by file and line. `CCM:n` is `refs/src/2511.22755/mc2arXiv.tex:n` (Connes, Consani,
Moscovici, "Zeta spectral triples"). `CS:n` is `refs/src/2511.23257/Araki-final-oct25.tex:n`
(Connes, van Suijlekom, "Quadratic forms, real zeros and echoes of the spectral action", the [CS]
of CCM; fetched today with `2106.01715`, `math/0204300`, `math/0606037`, `2310.18423`, sha256 in
`refs/manifest.sha256`). `IH-n`, `NG-n`, `Q-n` are claims, non-generalisation items and open
questions of `lanes/theory.md`. Notebook claim ids carry their `db/claims.tsv` status.

## 0. Summary

The question was: which parts of the Connes-Consani-Moscovici framework generalise easily to the
Ihara zeta of a finite graph, and which do not. The answer, in one paragraph.

The linear algebra generalises verbatim and is classical. Replace the group `R_+^*` by `Z`, the
window `[lambda^-1, lambda]` by `{-M..M}` (`K = 2M+1` points), the Fourier modes `V_n` by the DFT
modes, and the scaling operator `D` by the cyclic shift `Z`. The Weil form becomes a real symmetric
Toeplitz matrix `T` in the rescaled cycle counts with the trivial divisor subtracted (the notebook's
own `Wform` of `def:weil-form`, `thm:weil-positivity-finite`, both `proved`), the rank-two commutator
`[D, tau]` becomes the rank-two displacement `Z T Z^* - T` supported at the cut point of the window
(`IH-10`), the Loewner matrix `(b_n - b_m)/(n - m)` becomes a Loewner matrix on the circle
`z_n (B_n - B_m)/(K (z_n - z_m))` (`IH-9`), and CCM's Lemma `key` becomes a unitary key lemma:
`U = Z^* - |Z^* xi><eta|` satisfies `U^* T U = T` exactly and its quotient `U''` is unitary with
characteristic polynomial `sum_k xi_k w^{K-1-k}` (`IH-11`, new, three-line proof). The conclusion
"spectrum on the critical circle" is then Caratheodory-Fejer 1911, stated as Corollary `corcar` in
`CS:792`, and is Makhoul's 1981 theorem on extreme eigenvectors of Toeplitz matrices; `eps_M` is
Pisarenko's noise floor; `U''` is a CMV-type rank-one perturbation of a unitary with a
paraorthogonal characteristic polynomial (`IH-22` to `IH-25`, `lanes/literature.md` B, C). With a
Cayley transform and a diagonal congruence the graph case is literally an instance of `CS`
Proposition `prop:finmain` (`CS:1356`) (`IH-13`).

What does not generalise is exactly the analytic content of CCM. A finite graph has a finite
divisor, so the window has a critical size `K = R + 1` (`R` = number of distinct retained points)
at which the construction is exact, an under-resolved regime below it, and an over-resolved regime
above it where the kernel is degenerate and even-simplicity fails (`IH-18`, `IH-19`). For zeta every
window is under-resolved and the whole content is the rate at which `eps_N -> 0`; the graph has no
such limit (`NG-3`). There is no second truncation `N` (`NG-1`), no archimedean transcendental
kernel (the graph's gamma factor is the rational term `(|E|-|V|)((q^-1/2)^|k| + (-q^-1/2)^|k|)`,
`IH-5`, `NG-4`), no regularised determinant (`NG-9`), and no Hermite/prolate structure at all: the
completed Ihara zeta is a polynomial (`NG-7`). The one step whose absence blocks CCM's proof, the
convergence `xi_lambda ~ k_lambda`, is the one step a finite graph cannot exercise.

What a graph adds is the ability to watch the chain run on a false RH. The construction never
breaks: for a non-Ramanujan graph it still returns `K-1` points on the circle, while `eps_M` crosses
zero and then diverges like `-m rho^{2M}`, so the growth rate of the noise floor recovers the
offending eigenvalue (`IH-26`, `IH-27`). RH enters the CCM chain in exactly one place, the
identification of the limit measure with the divisor, which is `eps -> 0`, Weil's criterion restored
verbatim (`IH-29`; CCM Cor. `strange`, `CCM:668`). The chain is a spectral realisation of Weil's
criterion, not a route around it.

Two more findings. The sign is flipped relative to CCM because an ungraded graph's nontrivial
divisor consists of poles, not zeros (`IH-6`; `prop:no-ungraded-zeros`, `sketched`); a curve, or a
graded transfer channel with a purely odd retained divisor, has CCM's sign exactly and the same
code (`IH-33`, `IH-34`), and that curve instance is already in the literature (Hallouin-Perret, TAMS
2019, cited at `CS:800`, `IH-35`). And a mixed-parity retained divisor makes the form indefinite by
construction, so the CCM chain requires a single-parity retained divisor (`IH-36`).

MVP-2 is therefore a small library, `ihz/`, whose value is (i) a certified exact anchor for the
whole `zst` pipeline on an object where truth is known, (ii) the under-resolved accuracy law as a
function of window size and angular separation, the one quantitative question where the graph can
inform the zeta case (`Q-2`), (iii) the non-Ramanujan experiment, (iv) the irregular-graph case as
the cheapest example of Weil positivity without duality (`IH-32`, `prop:kraus-no-duality-example`),
and (v) the graded/curve sign as the bridge to `def:graded-transfer-channel`. Estimated at about
1400 lines of C and two weeks at the house standard (TDD, mutation, fuzz, cited ground truth).

## 1. The discrete chain, as verified

### 1.1 Objects

`X` a finite connected `(q+1)`-regular graph, `A` its adjacency matrix, `B` the Hashimoto operator on
the `2|E|` directed edges (`def:hashimoto-operator`), `Z_X(u)^{-1} = det(1 - uB) =
(1-u^2)^{|E|-|V|} det(1 - Au + qu^2)` (`def:ihara-bass`). Spectrum of `B`: `+-1` with multiplicity
`|E|-|V|` each, and for each adjacency eigenvalue `lambda` the two roots of `mu^2 - lambda mu + q`.
Trivial multiset `S_triv = {q, 1}` (from `lambda = q+1`), plus `{-q, -1}` if bipartite, plus the
`2(|E|-|V|)` values `+-1`; retained multiset `A_ret = spec(B) - S_triv` (`def:rescaled-trace-sequence`,
`02b`). Ramanujan iff `|mu| = sqrt q` for all of `A_ret` (`def:ramanujan-graph`). Write
`w = mu / sqrt q`, `R` = number of distinct retained `w`.

Cycle counts `N_k = Tr B^k = sum_{[C] prime, |C| | k} |C|` (graph von Mangoldt), `N_0 = 2|E|`.

### 1.2 The explicit formula in CCM's shape (`IH-1` to `IH-6`, all PROVED)

For `F: Z -> C` finitely supported, `F^(w) = sum_k F(k) w^k`, define
`Psi_X(F) = sum_{mu in A_ret} F^(mu/sqrt q) = sum_k F(k) t_k` with, for `k >= 0`,

    t_k = q^{-k/2} N_k - (1 + eps_bip (-1)^k)(q^{k/2} + q^{-k/2}) - (|E|-|V|)(1 + (-1)^k) q^{-k/2},

and `t_{-k} = t_k` (real). Then `Psi_X = W_C - W_{0,2} - W_R` with

    W_C(F)     = sum_k q^{-|k|/2} N_{|k|} F(k)                      (atoms: cycles, weight |C| q^{-m|C|/2})
    W_{0,2}(F) = sum_k (1 + eps_bip (-1)^k)(q^{|k|/2} + q^{-|k|/2}) F(k)   (pole pair; rank two)
    W_R(F)     = (|E|-|V|) sum_k ((q^{-1/2})^{|k|} + (-q^{-1/2})^{|k|}) F(k)  (gamma factor; one-rung ladder)

This is a finite rearrangement of `Tr B^k`, not an analytic theorem (`NG-5`). Dictionary with
`CCM:445` (`W_p`), `CCM:469` (`W_{0,2}`), `CCM:450` (`W_R`, kernel `rho(x) = sum_n e^{-(2n+1/2)x}`):
the graph's `W_R` is the same ladder truncated to one rung with the same exponent `1/2`, multiplicity
`-chi(X)`, and it is exactly the log-derivative of the factor `(1-u^2)^{|E|-|V|}` that completes
`Z_X` to a function with a clean functional equation (`IH-5`).

Two-sided extension: the Hermitian one `t_{-k} = conj(t_k)` is the definition (it makes the window
form Hermitian); the inverse extension `mu -> q/mu` coincides with it on `A_ret` (a theorem, the
functional equation, `thm:weil-duality-pairing`), but not on `spec(B)` (the image of `+1` is `q`) and
not for irregular graphs (`IH-1`, `IH-2`, `IH-32`).

Sign: CCM's `Psi = W_{0,2} - W_R - sum_p W_p = sum over zeros` (`CCM:465`); the graph's
`Psi_X = W_C - W_{0,2} - W_R = sum over poles`. Feeding a graph into a zeta-signed pipeline gives
`-QW`, so the relevant extremum flips to the largest eigenvalue (`IH-6`). For a curve,
`t_k = q^{-k/2} N_k - (q^{k/2} + q^{-k/2})` has CCM's sign exactly and no `W_R` (`IH-33`).

### 1.3 The window form, the displacement, the key lemma (`IH-7` to `IH-14`)

Window `{-M..M}`, `K = 2M+1`. Position basis: `T_{jk} = t_{j-k}`, real symmetric Toeplitz, lags up
to `2M` (cycle counts `N_1..N_{2M}` needed, the counterpart of primes up to `lambda^2 = e^L`).
DFT basis: `That_{nm} = z_n (B_n - B_m)/(K (z_n - z_m))`, `B_n = sum_{0<|d|<K} sign(d) t_d z_n^{-d}`,
diagonal the Fejer mean `a_n = sum_{|d|<K} (1 - |d|/K) t_d z_n^{-d}` (the counterpart of
`CCM:817`, with the nodes moved from `Z` to the roots of unity, `IH-9`).

Which `D`: the cyclic shift `Z`. `Z T Z^* - T = -(i/K)(|b><E| - |E><b|)` in the DFT basis, verbatim
`CCM:839` with `E = K^{1/2} delta_0` exactly (the discrete Dirichlet kernel is a delta; `CCM:937` ff
is vacuous, `NG-2`). The self-adjoint angle operator `diag(2 pi n/K)` fails: `(n-m) That_{nm}` is not
of the form `c_n - c_m`. The nilpotent shift fails (no circle) (`IH-10`).

Unitary key lemma (`IH-11`, PROVED, not in CS). `T >= 0` Hermitian Toeplitz, `ker T = C xi`,
`<eta|xi> = xi_0 = 1` (automatic that `xi_0 != 0`, `IH-15`, `CS:871`). `U = Z^* - |Z^* xi><eta|`.
Then `U xi = 0`; `U^* T U = T` exactly (proof: `(1-P^*) T (1-P) = T` for `P = |xi><eta|`, and the
displacement `|eta><g| + |g><eta|` is killed by `(1-P^*) eta = 0`, `<eta|(1-P) = 0`); `U''` on
`E/C xi` is unitary; `det(U'' - w) = det(Z^* - w) K^{-1/2} sum_n xihat_n/(z_n - w) =
(-1)^{K+1} Ptilde(w)`, `Ptilde(w) = sum_k xi_k w^{K-1-k}`; `spec(U'') = roots(Ptilde)`, `K-1`
points on `|w| = 1`. It needs neither evenness of `xi` nor a simple-spectrum `D`.

Cayley (`IH-13`): for odd `K`, `lambda_n = tan(pi n/K)` and the real congruence
`C = diag(sqrt(2K) cos(pi n/K))` turn `S^* That S` into `CS`'s form `(b_n - b_m)/(lambda_n - lambda_m)`
(`CS:1128`), so `CS:1356` applies verbatim. Cost: `C` is non-unitary, so the `eps`-shift must be
done in the Toeplitz picture first; and it replaces a natural unitary by an artificial self-adjoint.

Convention trap (both lanes hit it independently). `eta` is the delta at the window edge in the
position basis, i.e. all-ones in the DFT basis up to `K^{1/2}` and the window-shift phase `z_n^{-M}`
(window `{-M..M}` versus `{0..K-1}`). All-ones in the position basis gives a `xi`-independent
determinant `(s^K - 1)/(s - 1)`; and in the un-congruenced Cayley picture the second displacement
vector is `eta_n = (-1)^n sec(pi n/K)`, which `C` turns into all-ones. Taking `CS:1356` with a
literal all-ones `eta` in the wrong coordinates returns real but wrong roots (angle errors `0.4`
to `0.5` where the truth is exact). The rule for the implementation: read `eta` off the displacement
`Z T Z^* - T`, never posit it.

Backbone decision (`IH-14`): the position-basis Toeplitz route (`CS:792`, `corcar`) is the MVP-2
backbone (complete published proof, minimal hypotheses, gives weights and the over-resolved
diagnosis, `O(K^2)`); `U''` is implemented as a certified cross-check because it, not the
polynomial, is what carries to the graded and Selberg cases; the Cayley form is computed once as a
certificate that the graph case is an instance of `CS:1356`.

### 1.4 Grading and the three regimes (`IH-15` to `IH-21`)

Cantoni-Butler: eigenvectors of the persymmetric `T` are symmetric or skew (`J xi = +-xi`), the
even/odd blocks are `ceil(K/2)` and `floor(K/2)`; this is CCM's `gamma` (`CCM:837`) and the
block split of `../plan.md` 1.3 (`IH-16`). Evenness of `xi` means `Ptilde` self-reciprocal, i.e.
the returned divisor obeys `w -> 1/w`: the functional equation (`IH-17`). With a one-dimensional
kernel the parity is automatic (`CS:865`); what `even-simple` (`CCM:850`) adds is the `+` sign
(not needed for the circle conclusion over `Z`) and simplicity (needed, and it fails when
`K > R+1`).

Regimes (`IH-18`, PROVED; Petersen `R = 4`: `eps_M = 15.88, 9.45, 5.71, 0, 0, 0, 0` for `K = 2..8`,
kernel dimensions `1,1,1,1,2,3,4`):

| regime | `K` | `eps_M` | `dim ker(T - eps)` | `roots(Ptilde)` |
|---|---|---|---|---|
| under-resolved | `K <= R` | `> 0` | 1 (if simple) | `K-1` circle points, a Pisarenko approximation, not the divisor |
| critical | `K = R+1` | `= 0` | 1 | exactly the `R` divisor points |
| over-resolved | `K > R+1` | `= 0` | `K-R >= 2` | undetermined; only the intersection over `ker T` is the divisor (`CS:908`) |

Multiplicities are never seen by `xi` (support only, of a piece with `prop:weil-blind-jordan`);
at the critical window they are recovered by the Prony/Vandermonde step (`IH-20`; Petersen:
`(5,5,4,4)` on four points out of 18). The critical window is detectable blind: `rank T` stops
growing at `R` (`IH-21`(d)). No canonical `xi` in the over-resolved regime is selected by the
construction (`Q-1`).

### 1.5 Non-Ramanujan, irregular, graded (`IH-26` to `IH-36`)

Non-Ramanujan: the construction never breaks (circle spectrum at every `M`); with a real retained
pair `rho, 1/rho`, multiplicity `m`, `eps_M = -m rho^{K+1}/(rho^2 - 1)(1 + o(1))`, so
`d log(-eps_M)/dM -> 2 log rho` (`IH-27`, PROVED; prism `C_16 x K_2`: `rho = 1.123952`, predicted
`-1299` vs observed `-1351` at `M = 21`, ratio `1.2826` vs `rho^2 = 1.2633`; two disjoint `K_4`,
`rho = sqrt 2`: successive ratios `2.87, 2.80, 2.46, 2.10, 2.16 -> 2`). The returned points
go asymptotically equidistributed and carry no divisor information (`IH-28`, CLAIMED). The trivial
divisor bookkeeping is load-bearing: forgetting the bipartite pair `{-q, -1}` makes the law report
`2 log sqrt q`.

The parity mechanism behind this (numerics lane, section 3; proof in two lines): with the even
extension a reciprocal pair `{x, 1/x}` contributes `2 f^(x) f^(1/x)` to the form, which is
`+2 x^{-(K-1)} f^(x)^2 >= 0` on even `f` and `<= 0` on odd `f`. For a regular graph every off-circle
retained point is real, so the EVEN block stays positive semidefinite for every window while the
ODD block carries the negative eigenvalue: `xi_min` is odd, `<eta|xi_min> = 0`, and CCM's
`even-simple` fails. What survives is Caratheodory-Fejer on the kernel: at `K = R+1` the kernel
vector of `T` (equivalently the minimal even-block vector) still vanishes on the whole divisor,
off-circle points included (Vandermonde rank does not need the circle). So what breaks on a false RH
is CCM's prescription "take the minimal eigenvector", not the exact recovery; and in the discrete
setting "`xi_min` even for every window" is implied by Ramanujan's failure being absent, while the
converse (Ramanujan implies `xi_min` even for every `K`) is exactly `Q-3` and open. This is the
finite form of `prop:weil-orbit-negative` (`proved`) read in the `gamma`-grading.

Reality is free (numerics lane, verified on 200 random real even Toeplitz matrices): `T - eps_min`
is PSD Toeplitz with a kernel for ANY Hermitian Toeplitz `T`, so the circle conclusion holds without
positivity or a divisor. The whole content of the chain is positivity, i.e. `thm:weil-positivity-finite`.

Irregular: everything using only "Hermitian Toeplitz" survives (`IH-30`); `sqrt q` becomes
`specrad(B)^{1/2}`, `W_{0,2}` drops to rank one (`IH-31`); the functional equation fails, so
positivity gives only the one-sided Stark-Terras bound (no poles in `R_X < |u| < sqrt R_X`) and the
returned circle points are not the divisor even at `eps = 0` (`IH-32`). The data model must carry
`critr` as a free parameter and a flag for whether the functional equation is asserted.

Graded: a purely odd retained divisor (curve, `N_n = 1 + q^n - sum alpha_i^n`, `thm:as-super-transfer`
`proved`; `def:graded-transfer-channel`) has CCM's sign and the same code (`IH-33`, `IH-34`);
this instance is Hallouin-Perret (`IH-35`). A mixed divisor (e.g. `prop:qubit-graded-zeta`'s
`(1+2u+5u^2)/((1-u)(1-5u))` with both sectors retained) makes the form indefinite by construction
and the output meaningless unless one sector is put into `S_triv` (`IH-36`; `Q-6`).

## 2. What generalises and what does not

Condensed from the 24-row table of `lanes/theory.md` section 8 (`V` verbatim, `M` modified, `F`
fails or vacuous):

| CCM step | discrete analogue | |
|---|---|---|
| group `R_+^*`, `x = log u` | `Z`, length `k`; compact dual `T` | M |
| window `[lambda^-1, lambda]` | `{-M..M}`, `K = 2M+1` | V |
| `Psi = W_{0,2} - W_R - sum W_p` | `Psi_X = W_C - W_{0,2} - W_R` (poles, not zeros) | M |
| inversion symmetry (Lemma `wsharp`) | `t_{-k} = t_k` | V |
| `W_p`: `Lambda(n) n^{-1/2}` at `log n` | `|C| q^{-m|C|/2}` at `m|C|`; a matrix trace, not a prime enumeration | V |
| `W_{0,2}`, rank two | `q^{|k|/2} + q^{-|k|/2}` (doubled if bipartite) | V |
| `W_R`, digamma/Lerch kernel | `(|E|-|V|)((q^{-1/2})^{|k|} + (-q^{-1/2})^{|k|})`, rational | M |
| second truncation `N`, `E_N^perp` | none | F |
| Dirichlet kernel `~ delta` | `E = K^{1/2} delta_0` exactly | F |
| Loewner `(b_n-b_m)/(n-m)` | Loewner on the circle; verbatim after Cayley | M |
| `[D, tau]` rank two | `Z T Z^* - T` rank two; angle operator fails | M |
| `gamma`, even/odd blocks | persymmetry, Cantoni-Butler | V |
| `even-simple` | simplicity only, and it fails for `K > R+1` | M |
| `<eta|xi> != 0` | automatic (Caratheodory-Fejer) | M |
| `D' = D - |D xi><eta|` self-adjoint for `T` | `U = Z^* - |Z^* xi><eta|` unitary for `T` | M |
| `Det(D''-s) = Det(D-s) sum xi_j/(j-s)` | `det(U''-w) = det(Z^*-w) K^{-1/2} sum xihat_n/(z_n-w)` | V |
| `det_reg`, `xi^` entire with real zeros | ordinary `det`, `Ptilde` with circle zeros | V |
| `mu_lambda` decreasing, `-> 0 => RH` | `eps_M >= 0` for all `M` iff Ramanujan; finite equivalence | M |
| convergence of the spectrum to the divisor | exact at `K = R+1`; no limit to study | F |
| Hermite/prolate strategy, the missing step | none: `Xi` is a polynomial | F |
| spectral triple, infrared limit | finite unitary; linear algebra | M |
| multiplicities | support only; Prony recovers weights | M |

The does-not-generalise list (`NG-1` to `NG-12`), ranked by consequence for the programme:

1. `NG-3` finite divisor: no permanent under-resolution, hence no rate, hence the phenomenon CCM's
   missing proof must control does not exist on a graph.
2. `NG-7` no Hermite/prolate tower: no theta function on `Z`, no self-dual Gaussian, `Xi` a
   polynomial with known roots. The only place a discrete model could touch the missing step is an
   infinite object (a tree quotient, the Selberg zeta of `../plan.md` 6.5), `Q-7`.
3. `NG-1`, `NG-2` no second truncation, no Dirichlet-kernel approximation.
4. `NG-4` no transcendental archimedean term: MVP-2 does not exercise the hardest `zst` code path
   (`riemann_ab.c`, the future `kernel.c` of M3).
5. `NG-8` Weil's criterion becomes a finite equivalence; `NG-9` no spectral-triple content;
   `NG-10` half of even-simple evaporates, the other half can fail; `NG-11` multiplicities;
   `NG-5`, `NG-6` no analytic continuation, no number theory in the atoms.
6. `NG-12`, the one thing the graph adds: the chain can be run on a false RH.

## 3. What MVP-2 can and cannot test

Can, and should:

1. Exact anchor. At `K = R+1` the certified roots equal the certified Hashimoto angles; the
   certified `U''` is `T`-unitary with `spec(U'') = roots(Ptilde)`; the Cayley form matches
   `CS:1128` to ball width. This certifies the whole `zst` linear-algebra path (eigmin, the
   positive-definiteness certificate, the even/odd split) on an object with known truth.
2. The under-resolved law (`Q-2`). `eps_M` as a function of `K < R+1` and of the minimal angular
   separation of the divisor; the accuracy of the `K-1` returned points against the nearest divisor
   points. This is the discrete counterpart of CCM's `eps_N ~ 10 (1 - chi_4(lambda))`
   (`../plan.md` 1.6) and the one place where the graph can inform the zeta case.
3. The non-Ramanujan experiment: the sign change of `eps_M`, the slope `2 log rho`, the
   equidistribution of the returned points, the odd `xi_min` versus the even-block kernel vector
   that still recovers the divisor; families with `rho` tunable (prisms `C_n x K_2`, cubic
   necklaces of `K_4 - e`), and the minimal fully controlled case, two disjoint `K_4` (the second
   Perron eigenvalue is retained, `rho = sqrt 2`, critical `K = 5`).
4. Irregular graphs: the one-sided regime; what `eps_M` and the returned points do without a
   functional equation.
5. Graded sign: a curve (Artin-Schreier data from `scripts/artin_schreier_mps.py`, or the elliptic
   curve `y^2 = x^3 + 4x + b` over `F_5` of `prop:qubit-graded-zeta`) through the same code with
   the sign flipped; the mixed-divisor negative (`IH-36`) as a test that the code refuses it.
6. Anti-palindromic minimal eigenvectors (`Q-3`): a cheap search over small regular graphs and
   windows; settles whether "even" is a theorem or a hypothesis over `Z`.

Cannot: anything about `N, lambda -> infinity`, the prolate comparison (`../plan.md` M5), the
archimedean regularisation (M3). These remain `zst` work.

## 4. Library design (`ihz/`)

Sibling of `zst/`, same layout (`include/ src/ tests/ fuzz/ tools/ Makefile README.md`), same rules
of the house (red-green TDD, `make mutate`, `make fuzz`, every formula cites its ground truth by
file and line: `CS`, `CCM`, the shards `02_definitions.tex:73-102` and
`08_quantum_ihara_general.tex:27-31`, `lanes/theory.md` claims, and `ihara_proto.py`'s run record).
`eigmin.c` is copied verbatim from `zst/` (renamed prefix); a shared core is a follow-up once both
verticals are stable, not a precondition (`lanes/code-audit.md` section 4).

### 4.1 Data model

    typedef struct {
        slong  K;                 /* window size 2M+1 */
        arb_t  critr;             /* critical radius: sqrt q for regular, specrad(B)^{1/2} otherwise */
        int    fe_asserted;       /* functional equation of the retained divisor asserted (regular) */
        int    sign;              /* +1: retained points are poles (graph); -1: zeros (curve, CCM) */
        fmpz  *N;                 /* N[0..2M], exact cycle counts (or point counts) */
        /* trivial divisor: real points r_i with multiplicities m_i, subtracted exactly */
        slong  ntriv; arb_ptr r; slong *m;
        arb_ptr t;                /* t[0..2M], the rescaled retained sequence, balls */
    } ihz_weil_t;

This is the discrete instance of `zst_weil_t` (`../plan.md` 3.2): atoms at integer lengths with
exact integer weights, trivial-divisor points as the pole terms, and `W_R` as a geometric kernel
with `d = 1`, `mu = log q / 2`, `P = 1`. When `zst` M3 lands, `ihz_weil_t` should become a
constructor for the general data model rather than a separate type.

### 4.2 Modules and API

    src/graph_io.c      edge-list parser; builders K_n, Q_d, Petersen, Heawood, K_{m,n}, C_n x K_2 prisms,
                        cubic necklaces, LPS Cayley graphs (later, from scripts/weil_lps.py generators)
    src/hashimoto.c     graph -> fmpz_mat_t B (2|E| x 2|E|); regularity, bipartiteness, connectivity
    src/cycles.c        N_k = Tr B^k, k = 0..2M, exact (repeated fmpz_mat_mul); prime-cycle check for small k
    src/weil_data.c     ihz_weil_t from a graph (q, trivial divisor, sign) or from a curve's point counts
    src/toeplitz.c      t -> T (K x K) and its even/odd blocks; DFT-basis form; the exact integer
                        congruence diag(q^{j/2}) T diag(q^{j/2}) for exact rank / inertia (fmpq)
    src/eigmin.c        = zst/src/eigmin.c: ihz_eigmin, ihz_inertia_neg, ihz_certify_even_simple
    src/rank.c          exact rank of T over Q(sqrt q) via the integer congruence; critical-window
                        detection (rank stabilises at R); kernel dimension
    src/circle_roots.c  roots of Ptilde on |w| = 1: theta-substitution R(theta) = xi_0 + 2 sum xi_j cos(j theta)
                        for even xi (sin-form for odd), arb_calc_isolate_roots + interval Newton;
                        completeness by count K-1; the general (non-palindromic) case via acb_poly
    src/unitary.c       U = Z^* - |Z^* xi><eta|; certified ||U^* T U - T||; eigenvalues of U'' by
                        acb_mat_eig_multiple_rump with precision doubling; the Cayley form Q and its
                        match to CS form2
    src/prony.c         weights (multiplicities) at the critical window: Vandermonde solve in balls
    src/truth.c         certified spectrum of B with multiplicities: fmpz_mat_charpoly ->
                        fmpz_poly_factor_squarefree -> arb_fmpz_poly_complex_roots per factor
                        (the unfactored call does not terminate on repeated roots, code-audit 2.4);
                        acb_mat_eig_multiple_rump as a secondary cross-check only
    src/compare.c       certified |theta_root - theta_truth| matched by angle; eps_M sign and slope
    tools/ihz.c         CLI: --graph <file|name> --M <n> [--scan Mmin..Mmax] [--curve counts] [--sign]
    tools/mutate.py     = zst/tools/mutate.py pointed at ihz/src

Public prototypes as in `lanes/code-audit.md` section 4, amended: `ihz_weil_t` replaces
`ihz_weil_discrete_t` and carries `critr`, `fe_asserted`, `sign`; `ihz_rank_exact` and
`ihz_critical_window` are added; `ihz_unitary_check` and `ihz_cayley_form` are added;
`ihz_prony_weights` is added; the window heuristic "`M >= diameter`" in the audit's test plan is
replaced by the critical-window rule `K = R+1`.

### 4.3 Numerical core

Exact stage (fmpz/fmpq): `B`, `N_k`, the Ihara-Bass identity as an exact polynomial identity
(unit test), the integer congruence of `T`, its exact rank and inertia at rational shifts. Ball
stage (arb): `t_k` (only `q^{-k/2}` is inexact), `T` and its blocks, `eps_M` and `xi` by the ported
`ihz_eigmin` (Krawczyk on the bordered system), the even-simple certificate by the ported
positive-definiteness route (`E - 2 eps + c v v^T`, `O - 2 eps`), roots of `R(theta)` by
`arb_calc_isolate_roots` plus interval Newton (no cancellation problem: `xi` is `O(1)` here, unlike
`zst`'s `1e28` amplification), completeness by count `K-1`. At the critical window `eps = 0` exactly
and `ker T` is computed exactly over `Q(sqrt q)` when `q` is a square and in balls otherwise; the
`eps`-shift certificate is then `T >= 0` with a one-dimensional kernel, certified by exact rank plus
ball positive semidefiniteness of the deflated matrix.

Precision: `K <= 200` and `prec = 256` bits cover every graph in section 3; LPS graphs
(`PGL_2(F_13)`, `|V| = 2184`, `R` up to `~ 4000`) need `K ~ 4000` and are M4-scale work, not MVP.

### 4.4 Tests, fuzz, mutation

Pinned closed forms: `K_4` (`q = 2`, retained `mu^2 + mu + 2 = 0`, `R = 2`, critical `K = 3`),
`K_{3,3}` (bipartite, `{-q,-1}` trivial), `Q_3` (bipartite, spectrum `3, 1^3, -1^3, -3`), Petersen
(`R = 4`, multiplicities `5, 5, 4, 4`; `eps_M` values above), Heawood and Pappus (bipartite
Ramanujan, `R = 4` and `6`), `C_n` (`q = 1`, degenerate, must not mis-certify), two disjoint `K_4`
(non-Ramanujan, `eps_M = -2.673, -7.679, -21.48, -52.78, -111.06, -240.05` at `M = 2..7`), the
necklace of six `K_4 - e` (`lambda_2 = 2.86619826`, `eps_M` positive to `M = 5`, `-8.257` at `M = 6`,
`-624.42` at `M = 14`; even-block kernel exact from `M = 10`), the prism `C_16 x K_2` (`IH-27`
trajectory), the dumbbell and the triangle with a pendant path (irregular; `pt.err` saturating at
`0.20`; the pendant invisible). Integration: exact recovery at `K = R+1` certified; under-resolved
values pinned from `ihara_proto.py` (section 6). Fuzz: random regular graphs by a pairing model
(invariants: Ihara-Bass identity, `t_k` real, even/odd eigenvectors, roots on the circle, count
`K-1`, `U^* T U = T`), arbitrary normalised `xi` for `circle_roots`. Mutation on every new `src`
file; `eigmin.c` included for copy errors.

## 5. Milestones

- G0 (done): `ihara_proto.py` and its run record; `lanes/numerics.md` (section 6 below).
- G1, exact stage (2 days): `graph_io`, `hashimoto`, `cycles`, Ihara-Bass exact identity test,
  `truth.c` with the squarefree route; acceptance: certified spectra with multiplicities for the
  pinned graphs, Petersen's `(5,5,4,4)` included.
- G2, the anchor (4 days): `weil_data`, `toeplitz`, `rank`, `eigmin` port, `circle_roots`,
  `compare`, CLI; acceptance: at `K = R+1` every pinned Ramanujan graph returns its retained divisor
  as certified balls matching `truth.c`, with `eps = 0` certified and the kernel certified
  one-dimensional; under-resolved `eps_M` and roots reproduce the prototype to ball width.
- G3, the operator (2 days): `unitary.c` (certified `U^* T U = T`, `spec(U'') = roots`), the Cayley
  form against `CS:1128`, `prony.c`; acceptance: Petersen weights `(5,5,4,4)` certified.
- G4, the experiments (3 days): section 3 items 2 to 6 as scripted runs with captured outputs under
  `bench/`; the `Q-2` law fitted; the non-Ramanujan slope certified against `2 log rho`; the
  curve instance through the same code; the mixed-divisor refusal.
- G5, convergence with `zst` (later): `ihz_weil_t` as a constructor of the general `zst_weil_t`
  once M3 exists; LPS graphs at scale (M4); the Selberg compact case as the first infinite object
  where `Q-7` can be asked.

## 6. Prototype record

`ihara_proto.py` (numpy, sympy, mpmath at 40 digits; seeded; 21 s from the repo root; options
`--graph`, `--M`, `--Mmax`, `--dps`), captured run `run_ihara_proto.txt` (1470 lines, 446 tagged
checks, all PASS; re-run by the orchestrator, identical modulo blank lines). Write-up
`lanes/numerics.md`. Independent of the theory lane (neither read the other); the orchestrator's
own numpy check of `IH-3`, `IH-11`, `IH-18` on `K_4` and Petersen agreed to `1e-14`.

Identity checks: Ihara-Bass at random `u` (`<= 1.5e-15`), `N_k = Tr B^k` against direct prime-cycle
enumeration and `N_k = sum_{d | k} d P_d`, `spec(B)` against the `mu^2 - lambda mu + q` prediction
(`<= 5.8e-15`), trace-route `t_k` against the direct divisor sum (`<= 2.2e-36`), Cantoni-Butler,
functional-equation closure of `A_ret` (`<= 7.7e-38`; the trivial `+-1` copies are NOT reciprocal
closed, so the trivial part must be subtracted in its even extension).

Regimes (Ramanujan objects; `eps` at the critical window `|eps| < 1e-39`, angle error `0`, kernel
dimension `3` one window later):

| object | `R` | critical `M` | `eps` at `M_crit - 1` | angle error there |
|---|---|---|---|---|
| `K_4`, `K_{3,3}`, Pauli curve | 2 | 1 | (`K = 1`) | |
| `Q_3` | 4 | 2 | `3.0` | `3.6e-1` |
| Petersen | 4 | 2 | `9.4476568` | `6.1e-1` |
| Heawood | 4 | 2 | `12.0` | `5.2e-1` |
| Pappus | 6 | 3 | `4.661334` | `5.2e-1` |
| necklace of two `K_4 - e` | 8 | 4 | `1.965774` | `3.5e-1` |
| necklace of three | 8 | 4 | `2.9357842` | `2.6e-1` (`1.32, 0.57, 0.26` at `K = 3, 5, 7`) |

Perturbed operator: the multiplicative variant (shift, `eta` = delta at the window edge, `xi_M = 1`)
is the companion matrix of `z^M xi^(z)`, satisfies `D'^T (tau - eps) D' = tau - eps` exactly and
`Det(D'' - s) = +-s^M xi^(s)` (this is `IH-11`); the additive Cayley variant with
`eta_n = (-1)^n sec(pi n/K)` satisfies Lemma `key` (i)-(iii) to `1e-40` and returns the angles by
`theta = 2 arctan s` to `1.3e-15` (this is `IH-13`); the angle operator has a rank-3 commutator.

Non-Ramanujan, irregular and graded: as recorded in sections 1.5 and 4.4. Precision: `Tr B^k`
exact, the only cancellation is about `q^{k/2}/R`; double suffices for `eps_M` everywhere (agrees
to `2.3e-13`) and for the roots when the kernel is simple; double cannot certify `eps_M = 0` at
the critical window (condition number `1e16` to `1e18`, float64 returns `+-1e-15` with arbitrary
sign), which is the argument for arb and for the exact rank stage of section 4.3.

## 7. Risks

- `acb_mat_eig_multiple_rump` fails at moderate size without precision doubling (code-audit 2.3);
  it is secondary only, the primary truth route is exact.
- `arb_fmpz_poly_complex_roots` hangs on repeated roots; always square-free-factor first.
- Over-resolved windows: the code must detect `dim ker > 1` and refuse to interpret `xi`; the
  critical-window detector must be exact (rank over `Q`), not a ball heuristic.
- The sign convention (`sign` field) is the single most likely silent error; the mixed-divisor
  refusal and the curve test guard it.
- Nothing here touches CCM's missing step; the report to TJO must say so plainly.

## 8. Open questions carried

`Q-1` canonical `xi` when over-resolved; `Q-2` the under-resolved law (MVP-2 measures it; the
numerics lane notes the minimiser is a discrete prolate/Slepian problem, the natural place to ask
whether `1 - chi_4(lambda)` is its continuous limit); `Q-3` anti-palindromic minimal eigenvectors,
now sharpened to "is `even-simple` for every window EQUIVALENT to Ramanujan, or only implied by its
failure" (MVP-2 searches); `Q-4` the exact weak-* limit in the non-Ramanujan case; `Q-5` a principled
trivial divisor for irregular graphs, and whether the functional equation is a necessary input for
convergence (dumbbell: `eps_M` changes sign at `M = 4`, error saturates); `Q-6` a Krein-space key
lemma for mixed divisors; `Q-7` any `Z`-side analogue of the prolate tower (no for finite graphs;
open for infinite objects); `Q-8` (numerics lane) a `CS`-type key lemma with a general `eta` read
off the displacement `|beta><eta| - |eta><beta|`, which would cover zeta and graphs in one
statement, and whether CCM's parity hypothesis is avoidable by the unitary route plus a Cayley
transform at the end (the multiplicative variant needs no parity).

## 9. References

- CCM: `refs/src/2511.22755/mc2arXiv.tex` (Lemma `basics` 837, Def. `even-simple` 850, Lemma `key`
  863, Thm `finmain` 1085, Cor. `strange` 668, outlook 1216-1400).
- CS: `refs/src/2511.23257/Araki-final-oct25.tex` (Cor. `corcar` 792, Toeplitz case 831-913,
  finite even case 1148-1362, Prop. `prop:finmain` 1356, Hallouin-Perret at 800 and 2103).
- Connes-Consani, Spectral triples and zeta-cycles, `refs/src/2106.01715/Spectraltriples.tex` (the
  [VJ] of CCM). Simon, Rank one perturbations and the zeros of paraorthogonal polynomials,
  `refs/src/math/0606037/main.tex`. Cantero-Moral-Velazquez, CMV matrices, `refs/src/math/0204300/main.tex`.
- No TeX source: Caratheodory-Fejer 1911; Pisarenko 1973; Makhoul 1981 (IEEE TASSP 29, 868-872);
  Cantoni-Butler 1976 (LAA 13, 275-288); Slepian 1978; Stark-Terras I-III; Horton-Stark-Terras
  2006; Terras 2011; Hallouin-Perret 2019 (TAMS 372, 5409-5451). Verification status per item in
  `lanes/literature.md`; Makhoul's exact hypotheses, Terras's chapter contents and Ihara 1966
  remain UNVERIFIED there.
- Notebook: `def:ihara-zeta`, `def:hashimoto-operator`, `def:ihara-bass`, `def:ramanujan-graph`
  (stipulated); `def:rescaled-trace-sequence`, `def:weil-form` (02b); `thm:weil-positivity-finite`,
  `thm:weil-duality-pairing`, `prop:weil-orbit-negative`, `prop:kraus-no-duality-example`,
  `prop:weil-blind-jordan` (proved); `def:graded-transfer-channel`, `def:graded-rh-fe-ramanujan`,
  `prop:no-ungraded-zeros`, `prop:qubit-graded-zeta` (sketched); `thm:as-super-transfer` (proved).
  Full extraction with lines in `lanes/notebook-extract.md`.
