# RTP-2 lane S: the rate at scale

Author: `codex:gpt-6-astra`, 2026-09-26. Status: work in progress; no registrations.
No RH assumption. Forms use only `zst_riemann_ab` (primes, pole, archimedean factor).
Zeros enter only explicitly labelled COMPARISON STEP calculations.

## Correction ledger

- **SHARPENED:** `N_sat ≈ 1.7 x log x` describes the log-determinant minimum, not 1% convergence of the minimal eigenvalue. The round-1 x=13 and x=25 endpoints also require the new 40-mode test.
- **PROVED:** A less than 1% drop over the next 40 modes does not bound the remaining infinite tail. “Converged” below means exactly the brief's finite-step criterion, never a certified 1% enclosure of `eps_infinity`.
- **SHARPENED:** The prolate expression is an asymptotic equivalent, not a certified finite-x enclosure of `1-chi_4`. We certify arithmetic comparisons with that expression and distinguish the asymptotic interpretation.

## S1. Plan and cost model (recorded before scale runs)

**NUMERICAL (floating cost estimates).** Lane A1 section 2 records 108 s for build, both LDL factors and all borderings at `(50,520,4200)`, and 276 s for five eigenpair/root computations at `N=50,100,200,300,360`, eigenpair precision 2400. The review certifies `(50,420,4200)` but retains no wall time in `scratch_rtp1_tail.py`. Do not invent a review timing. Using `T = 276 N^3 / sum_{n=50,100,200,300,360} n^3 * (p/2400)^1.5` as a conservative one-thread eigenpair-plus-root cost model gives the following estimates; exponent 1.5 is a modelling assumption for high-precision multiplication, not measured scaling.

| x | N | prec | estimated original full eigenpair/root time, seconds (floating) |
|---|---|---|---|
| 50 | 520 | 4200 | 1085.3 |
| 60 | 650 | 5200 | 2920.2 |
| 70 | 800 | 6200 | 7087.9 |
| 100 | 1300 | 9000 | 53193.1 |

Plan: sparse sweeps, spacing 40. x=13 starts at N=200; x=25 at 260; x=50 at 420. x=60 starts at ceil(1.7 x log x)=418; x=70 at 506. Stop a sweep only after a certified upper bound on `eps_N/eps_(N+40)` is below 1.01. Use the larger member for final comparisons. Keep the first qualifying lower N as `N_conv` (grid-dependent; not a claim about every integer N). Extend lower-x grids backwards if necessary to locate the first qualifying tested pair.

Precision: begin at 1000, 1800, 4200, 5200, 6200 bits respectively. These exceed `3.33*5.4*x` by about 766, 1350, 3301, 4121, 4941 bits. The large margins are intentional: A1 observed interval LDL losses up to 4.6 times the eigenvalue bit exponent. Merely adding 200 bits to the exponent is inadequate for these unpreconditioned ball factors. Raise precision on an inconclusive sign; no failed certificate is treated as evidence.

Driver optimisation to test: dot-product LDL with independent columns parallelised by OpenMP, keeping the summation order in each cell fixed. Midpoint inverse iteration supplies an approximate vector; ball residual plus certified inertia at 0 and at twice the Rayleigh value can certify both the minimum and its eigenvector via a spectral-gap bound. This avoids a dense inverse on every sparse-N point. Compare this certificate against unchanged `zst_eigmin` on a reference point; preserve a Rump endpoint cross-check when affordable. All changes stay in the driver and lane checks, never `zst/src/`.

The unoptimised x=85/100 endpoints exceed the one-hour allowance at the proposed thousands-of-bit precision. Attempt them only if the measured optimised driver predicts under one hour per scale. Initial resource target: 8 threads per independent sweep, fewer if OpenMP overhead dominates; no claim of a 64-fold speedup. Timings go to stderr and are copied here as floating seconds. Run `make -C zst check` and byte-reproducibility checks before completion.

## S2. Monotonicity

**PROVED:** Extend a unit vector in the N-th even block by a zero coefficient; its Rayleigh quotient in the (N+1)-st block is unchanged, hence minimisation over the larger unit sphere gives `eps_(N+1) <= eps_N`. This uses fixed x and nested Fourier subspaces, with no RH assumption.

Convergence and numerical tables are pending.

## Certificate used by the scale driver

**PROVED (finite symmetric-matrix certificate).** Let `A` be the exact real symmetric even block enclosed by the input balls. Choose an exact dyadic nonzero vector `u` by approximate inverse iteration, set `q=u/||u||`, and enclose `rho=q^T A q` and `r=||Aq-rho q||_2` in balls. Fix an exact dyadic `s` (the midpoint of twice the Rayleigh ball). Certify by ball LDL that `A` has zero negative eigenvalues and `A-sI` exactly one, with every pivot excluding zero. Require `rho-r>0` and `rho+r<s` as interval inequalities. The spectral theorem gives an eigenvalue in `[rho-r,rho+r]`; exactly one eigenvalue lies below `s`, so this is the simple minimum. Moreover, writing `q=alpha v+w`, `w perpendicular v`, gives `||w|| <= r/(s-rho)`, since every other eigenvalue is at least `s`. Choose the sign with `alpha>=0`; then `||q-v|| <= sqrt(2)||w|| <= 2r/(s-rho)`. Adding this last bound to every component of the normalised-vector ball encloses the true unit eigenvector. An odd-block LDL at a shift above the upper endpoint of the certified even eigenvalue establishes even-simplicity.

**PROVED (LDL count).** The recurrence in the driver is `d_i=A_ii-s-sum_(k<i) L_ik^2 d_k`, `L_ji=(A_ji-sum_(k<i) L_jk L_ik d_k)/d_i`. Each nonzero pivot ball contains the exact pivot, so congruence to `diag(d_i)` and Sylvester inertia give the count. OpenMP assigns independent `j` cells only; each dot product retains its original order. Midpoint arithmetic is restricted to choosing `u`, which has no authority over the certificate.

**NUMERICAL (validation in progress).** An exact 3-by-3 matrix with spectrum `{1,6,7}`, nontrivial eigenvector, shifted inertia checks, and deliberate zero-pivot rejection passes `checks/test_driver.py`. The original Rump solver and the new residual certificate agree at `(x,N,p)=(13,120,1000)` and `(25,260,1800)`: `3.483988199331277e-59` and `2.425617541041462e-123` respectively (rounded; full enclosures in reference outputs). A first implementation reused midpoints of the interval factor: valid eigenvalue bounds, but insufficient vector accuracy for the zero comparison at x=25, and no eigenpair certificate at x=50. Recomputing a midpoint factor separately removes the inherited interval-width loss. Failed/incomplete pilot files remain in `checks/`, explicitly not final results.

**SHARPENED (measured bottleneck and second certified route).** The 6200-bit ball LDL at `(70,506)` was inconclusive: a pivot contained zero (`checks/failed_x70_6200*`). Instead of simply inflating precision, the driver now also offers `--fast 1`, using the residual positive-definiteness certificate already used in `zst/src/eigmin.c`, implemented with parallel dot products in this driver. This is not displacement-structured arithmetic: it remains cubic, with lower precision and constants. Cache `(a_n,b_n)` once at the maximum N of a sweep; these data are independent of N.

**PROVED (deflated alternative).** With the same exact unit `q`, Rayleigh `rho`, and dyadic `s`, set `F=A-sI+(s+1)qq^T`. If `F` is positive definite, rank-one interlacing gives at most one eigenvalue of `A` below `s`. Since `rho<s`, there is at least one; the previous residual and vector proof applies unchanged. To certify `F>0`, choose exact `delta>0`, compute any approximate Cholesky factor `T` as an exact dyadic matrix, and bound `R=F-delta I-TT^T` in ball arithmetic. Because `R` is symmetric, `||R||_2 <= ||R||_inf`; if the computed upper bound is below `delta`, then `F >= (delta-||R||_inf)I > 0`. The driver chooses `delta=2^(-floor(p/2))*max_i |mid(F_ii)|`. The odd block uses the same PD proof above an upper bound on the even eigenvalue. This route needs no signed interval factor of the ill-conditioned form. Self-tests check this PD route and the inertia route on the same nontrivial exact matrix.

Revised precision plan for this route: `p=60x+400` bits (3400 at x=50, 4600 at x=70), leaving over three eigenvalue bit exponents plus a safety margin for the vector/zero calculation, and placing the PD residual shift well below the second eigenvalue. The certificate, not this heuristic, decides success. Keep the original x=50/60 sweeps running as an independent inertia-route check. Benchmark the PD route at `(50,420,3400)` before deciding whether x=85 and 100 fit the time budget.

**NUMERICAL (first timings; seconds are floating wall times under concurrent load).** The PD pilot `(50,420,3400)`, four threads, takes 10.494096 s to build the data and 35.043675 s for the row (45.572695 s total); its certified `eps=2.808808827666894e-258` agrees with the independent reviewed value and the 4200-bit inertia sweep. A 16-thread repeat is being timed to decide the optional scales. Initial mandatory sweeps use four threads each. The x=13 sweep to its comparison endpoint took 100.845818 s. `make -C zst check` passes unchanged.

## S2–S4. Incremental results

**NUMERICAL.** First qualifying tested 40-mode pairs (not necessarily the first pair over all integer N):

| x | N_conv | final N | eps at final N, rounded | eps_Nconv / eps_final, rounded |
|---|---|---|---|---|
| 13 | 400 | 440 | 2.546250839967488e-59 | 1.003746547943147 |
| 25 | 500 | 540 | 1.940610904604938e-123 | 1.004556921045291 |

The complete balls and all preceding failed ratio tests are in `outputs/rtp2_scale_x13.txt` and `..._x25.txt`; final tables will include precision, controls, and timing. The x=13 COMPARISON STEP gives `|z1-gamma1|=1.781925403772520e-55`, ratio `6998.231972287823`; all 440 positive secular roots are certified and distinct. The prime-free control at N=440 has two negative even and two negative odd eigenvalues (512-bit certified inertia).

## S5. Source and comparison convention

**PROVED (algebraic substitution), source asymptotic quoted.** `refs/src/2511.22755/mc2arXiv.tex`, Section 7, line 1325 specifies `n=4` and attributes the result to Fuchs, Theorem 1. Line 1326 reads exactly:

```tex
$$1-\chi(\lambda)\sim\frac{2^{14}}{3} \sqrt{2} \pi ^5 e^{-4 \pi  \lambda^2+9 \log(\lambda)} $$
```

Thus, with `x=lambda^2`, compare with `P(x)=C x^(9/2) exp(-4 pi x)`, `C=(2^14/3)sqrt(2)pi^5`, and `log10 P=-a0 x+4.5 log10 x+log10 C`, `a0=4pi/log(10)`. A finite-x ratio to P is not a ratio to a rigorously computed prolate eigenvalue; no finite-x error term for this asymptotic is supplied here.

**PROVED (overlap convention).** Section 1.1 of the formula sheet defines `U_n^L(t)=L^(-1/2) exp(2pi i n t/L)`. Under the unitary rescaling to `[0,1]`, all these bases become the same Fourier basis. Therefore the absolute coefficient dot product of the unit even eigenvectors, padding the shorter list by zeros, is the requested common-window overlap. `checks/overlap.c` evaluates this in balls from exact Arb dumps. It is not the intrinsic overlap of functions on different physical windows. The first overlap, x=13 to 25, is `[0.9879466966245984 +/- 1.62e-17]`.

**NUMERICAL (optional-scale decision, recorded before running x=85).** The 16-thread repeat of the PD pilot takes 28.048920 s total (11.263545 s data, 16.740201 s row), versus 45.572695 s with four threads; stdout is byte-identical (`cmp`). Its iteration/factor part is 10.482341 s and the remaining PD verification about 6.010884 s. Extrapolate these as `N^2 p^1.5` times the observed iteration-count ratio and `N^3 p^1.5`, respectively; doubling to 32 threads is assumed to halve only the parallel PD part, not the sequential triangular solves. Allow several hundred seconds for the final full secular-root calculation. This predicts roughly 40–55 minutes for an x=85 sweep from N=642 (ceil(1.7 x log x)) through a final N around 1000–1100 at 5500 bits, and over one hour (roughly 75–100 minutes) for x=100 from 783 through about 1300 at 6400 bits. Attempt x=85 with 32 threads, cap N=1122 on its 40-grid (and an hour of wall time); defer x=100 under the brief's per-scale allowance. These are scheduling estimates, not mathematical conclusions.

**SHARPENED (first-zero computation).** The full-root routine certifies all 540 positive roots at x=25, but, with the conservative residual-certified eigenvector, its edge normalisation widens the first-zero-error ball to `[+/- 1.11e-102]`, too wide to resolve the actual error. The secular function is homogeneous in its coefficients, so the new first-root completion deliberately keeps the unit-eigenvector coefficients unnormalised. It uses `zst_secular_eval` and `zst_secular_verify` from the same library pipeline. A prime-side sign scan locates a candidate; interval Newton encloses it; a fixed-sign derivative proves uniqueness on a surrounding basin. Interval subdivision proves `h_j(s)=g(s)(j-s)(j+1-s)` nonzero on the entire positive range below that basin. Nonzero coefficients at the preceding integer poles rule out polynomial roots there. Thus this is certified to be the first positive root, without computing every remote root and without using any zero as a starting guess. Only then is `gamma_1` queried.

The first-only certificate reproduces the full x=13 result (1092 exclusion cells; 3.056622 s) and resolves x=25 as `|z1-gamma1|=[1.801891090212607e-119 +/- 3.67e-135]`, ratio `[9285.174508382088 +/- 4.62e-13]` (1536 exclusion cells; 6.685266 s). The separate `outputs/rtp2_scale_comparison_x*.txt` files are the authoritative COMPARISON STEP outputs. They also include the prime-free control; x=25 has three negative eigenvalues in each parity block. Full-root pilot outputs are retained as checks, not used for the final error-rate fit.

**NUMERICAL (reproducibility).** After separating the first-root completion, the complete x=13 axis-N certificate output regenerates byte-for-byte with the current driver (`checks/reproduce_x13.txt`, `cmp` success). The standalone first-root certificate is checked against the original full-root result at x=13. The x=25 full-root pilot's wide error interval is retained in `checks/fullroots_x25.txt`. Canonical scale files contain the eigenpair/convergence certificate; comparison files contain the tight zero error and controls. Formatting-only addition of `fast=0` to the initial inertia-route headers records the method selected by the final runner. No certified values were changed by that normalisation.

**PROVED (driver's optional displacement recurrence).** Both parity blocks have displacement rank two with distinct nodes `d_n=n^2`: the even generators are `g_n=2n b_n`, `h_n=1` for n>0 and `g_0=0,h_0=1/sqrt(2)`; the odd generators are `g_n=2b_n,h_n=n` for n>=1. Off the diagonal, `A_ij=(g_i h_j-h_i g_j)/(d_i-d_j)`. A diagonal shift leaves this identity unchanged. With pivot p and column multiplier `ell_i=A_ik/p`, the Schur complement has generators `g'_i=g_i-ell_i g_k`, `h'_i=h_i-ell_i h_k`, and diagonal `A'_ii=A_ii-p ell_i^2`. Expansion proves the identity, so a signed ball LDL needs only quadratic arithmetic. The optional `--structured 1` implements this recurrence and agrees with dense inertia in both parity blocks at four shifts of the x=13,N=20 form. Its unpreconditioned ball version is **inconclusive** already at `(50,420,4200)` (generator interval growth); it is not used to support the main scale tables. It can also supply an approximate factor to the independent PD/residual certificate. A transposed copy of the midpoint factor makes backward solves contiguous, without changing their arithmetic order. These driver-only experiments identify both the available structure and its precision limitation.

**NUMERICAL (tail and implementation follow-up).** The x=50 sequence still has `eps_900=[1.517481900488044e-258 +/- 4.52e-274]` and `eps_860/eps_900=[1.016974659573797 +/- 1.89e-16]`. Thus the reviewed N=420 value is still almost twice a later certified value; no convergence is claimed at 900. The structured midpoint-factor plus independent PD certificate succeeds at `(50,420,3400)` and returns exactly the same printed eigenvalue as the dense route; 38.899799 s total, with 8.603448 s for factor/iteration (four threads, concurrent load). The production tables keep their stated methods.

For long sweeps, the driver supports a continuation from the preceding certified epsilon ball. That input is used **only** in the 40-mode ratio, never to build a form or an eigenvector. The row's eigenpair is independently recomputed. A continuation at x=13 from N=400 to 440 reproduces the stopping decision. The x=60 run is split after its last completed old-driver row to use cached data and contiguous backward solves; its earlier certified rows are retained and its continuation header makes the split explicit. The runner regenerates these segments. Reported timing remains that of the actual runs, including the slower initial segment.

**NUMERICAL (S2–S3, x=50 complete).** The first qualifying pair on the required grid is **N=900 to 940**, at 4200 bits:

- `eps_900=[1.517481900488044e-258 +/- 4.52e-274]`;
- `eps_940=[1.505987039594760e-258 +/- 7.68e-275]`;
- `eps_900/eps_940=[1.007632775442993 +/- 1.58e-16] < 1.01`.

Both minima are residual/inertia certified. The odd block at N=940 has zero eigenvalues below twice the upper bound on eps, certifying even-simplicity. All preceding 40-step ratios from N=420 fail the 1% test. The matrix portion took **1755.415890 s (floating)** from output creation to the final even-simple certificate write; this filesystem wall measurement is recorded in `checks/wall_x50.json` and appended to the timing log, since the initial driver entered its unnecessary full-root stage before printing its final row timer. That full-root stage was stopped; the independently certified first-root completion supplies the requested comparison. This time includes data rebuilding in the initial driver; the final runner caches data.
