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
