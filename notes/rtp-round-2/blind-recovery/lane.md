# RTP round 2, blind-recovery lane: the most positive grid measure, certified

Author: `claude:opus`. Date: 2026-09-26. Status: unregistered, for REFUTE review. Git not run.

Script: `scripts/rtp2_blind_recovery.py` (deterministic, no timestamps, one `check(cond, msg)` helper as in
`scripts/gl1_bond.py`). Output: `outputs/rtp2_blind_recovery.txt` (102 checks, 0 failed; wall clock 27:37 on
64 cores, peak memory 0.42 GB per worker). The script reuses the reviewer's zst-independent helpers
`notes/reviews/scratch_rtp2_grid_common.py` (`ab0`, `phi`, `blocks`, `prime_powers`, `blocks_np`, `phi_np`).

Game rules (`notes/rtp-round-2/brief.md`). RH is not assumed. No zero of zeta enters anything. The form is
built from the **pole and the archimedean place only**; the primes are **not input**. Prime positions and
weights appear only in steps labelled COMPARISON WITH THE PRIMES, after every solve; those steps use no zeros.
The true form's `lambda_min` (pole + archimedean + primes) is also a comparison value only.

Source of the question: the REFUTE review of lane G, `notes/reviews/rtp-round-2-grid-tomography-2026-09-26.md`,
"Point (d)". That review ran the experiment with float64 Kelley cutting planes, so its refined levels were not
converged (level-2 bracket `[-1.72e-8, -3.6e-9]`). This lane repeats it with an interior point method,
polishes in multiprecision, and certifies every optimum at 80 digits.

---

## 1. The problem

Window `[0, L]`, `L = log x`, `t = y/L`. `H0` is the Loewner form (even block `N+1`, odd block `N`, plan.md 1.3)
of the pole + archimedean data `(a0_n, b0_n)`, `n = 0..N`. A unit atom at `t` contributes `T(t) = K(phi(t))`,
where `phi(t) = (A_0..A_N, B_1..B_N)`, `A_n = -2(1-t) cos 2 pi n t` and `B_n = sin(2 pi n t)/pi`. This is lane
G's convention, and the reviewer checked it against zst. For a finite grid `G = {t_j} ⊂ (0,1)`:

    f(G, N) = max_{w >= 0} lambda_min( H0 + sum_j w_j T(t_j) ),        tau*(G, N) = -f(G, N).

`tau* > 0` means the grid is **empty**: no nonnegative measure on `G` makes the `N`-section PSD. The maximiser
is "the most positive nonnegative grid measure compatible with the pole and the archimedean place".

**Dual.** Minimise `tr(Z H0)` over `Z >= 0` with `tr Z = 1` and `tr(Z T(t_j)) <= 0` for all `j`. Slater holds
for the primal (`w = 0` with `s` very negative), so the two optimal values agree.

### Statements used (PROVED; each is one line)

- **D1 (weak duality).** Take `w >= 0` and PSD `Z` with `q_j := tr(Z T(t_j)) <= 0` for all `j`. Then
  `lambda_min(H(w)) tr Z <= tr(Z H(w)) = tr(Z H0) + sum_j w_j q_j <= tr(Z H0)`. Hence
  `f(G, N) <= tr(Z H0)/tr Z`.
- **D2 (repair).** `tr(e_0 e_0^T T(t)) = A_0(t) = -2(1-t) < 0` on `(0,1)`. Adding `rho e_0 e_0^T` with
  `rho >= max_j q_j^+ / (2(1-t_j))` therefore makes every `q_j <= 0`. The cost rises by `rho a0_0`, and the
  trace by `rho`.
- **D3 (signed control is unbounded).** Suppose the grid moment vectors `phi(t_j)` span `R^{2N+1}`. This holds on
  the uniform even grid when `M - 1 >= 2N + 1`, by lane G's rank formula (G1). Then for every `c` there is a
  signed `w` with `sum_j w_j phi(t_j) = (c - a0_n; -b0_n)`. Since `K(a == c, b == 0) = c I` in both blocks,
  `H0 + T(w) = c I`. So `sup lambda_min = +infinity` once the sign constraint is dropped.
- **D4 (bounded with the sign).** For `w >= 0`, `lambda_min(H(w)) <= H(w)_00 = a0_0 - 2 sum_j (1-t_j) w_j
  <= a0_0`. This holds for every input form, including the controls.

## 2. Solver and certificate

1. **float64 primal-dual IPM.** HKM direction with Mehrotra predictor-corrector, written for this problem in
   the moment coordinates. Every basis matrix of the Loewner assembly `K` has the rank-two form
   `u e_i^T + e_i u^T`, so the Schur kernel `G_kl = tr(B_k X B_l W)` costs `O(n^2 (2N+1))`. The self-tests
   compare it with brute force.

   The float IPM alone stalls at about `1e-10` absolute: the Schur complement reaches condition number
   `1e21..1e25` before the gap closes. At `x = 13, N = 20, L/256` its best float bracket was
   `[-8.254034e-6, -8.249530e-6]`, width `4.5e-9`; the reviewer's float Kelley bracket had width `1.3e-9`. The
   certified value is `-8.2537140674e-6`, with the two ends agreeing to 21 digits. Float64 is therefore used
   only to locate the support.
2. **mp IPM (50 digits, `mu` down to `1e-26`).** The same IPM in mpmath, run on the restricted set of
   points carrying at least `1e-4` of the mass, plus their grid neighbours. Inner products are exact integer
   `math.sumprod` over block-floating-point rows, with one rounding per entry. The mp IPM is warm-started from
   a float IPM on the same restricted set.

   **Column generation:** the dual `q_j` is evaluated at 50 digits on the **whole** level grid. Violators are
   added and the problem is re-solved. In 74 of the 75 solves one round sufficed; the exception is pole x 1.1,
   `N = 20`, level 2, which took two. For `N = 134` the mp IPM runs at
   34 digits with `mu` down to `1e-18`, for run time.
3. **Certificate at 80 digits.**
   - (a) **Primal.** `w` is taken exactly as computed. The certificate forms `H(w)` in mp, takes the Cholesky
     factor of `H(w) - s0 I` in each block, and forms the residual `E = (H - s0 I) - R R^T`. Then
     `lambda_min >= s0 - ||E||_F - n (entry error)`, with an explicit bound on the entry error.
   - (b) **Dual.** `Z = R_E R_E^T (+) R_O R_O^T`, where `R` is the mp Cholesky factor of the IPM's `X`, so `Z`
     is PSD for any `R`. The certificate evaluates `q_j` on the full level grid, applies the D2 repair, and
     bounds `(tr Z H0 + rho a0_0 + err)/(tr Z + rho)`.
   - Rounding is bounded by `10^(8-80)` times absolute sums. The error of the data `(a0_n, b0_n)` is bounded by
     comparison with zst's ball data at prime cutoff `X = 1`, compiled against `zst/build/libzst.a`:
     `|diff| + radius <= 2.11e-81` for `x = 13, n <= 60` and `x = 25, n <= 134`. The certificates use
     `delta = 4.21e-81`, and `3 delta + 1e-78` for the controls.

   The printed intervals are therefore certified enclosures of `max lambda_min` on each grid. The one
   caveat is that the zst balls and mpmath's elementary functions are taken as correct.
4. **Coarse to fine.** Level 0 is the uniform grid `t = j/M`. Level `k` is the level-0 grid **union** 17-point
   patches of spacing `h_k = h_0/8^k`, one patch centred on each level-`(k-1)` support point. Keeping the
   uniform grid in every level lets mass leave the patches. The level-`(k-1)` support lies inside level `k`, so
   `tau*` cannot increase from level to level, and it never does.
5. **Clusters.**
   - A core is a maximal run of support points (`w > 1e-4` of the total) with gaps `<= 2.01 h_k`.
   - Every other grid point within `2.01 h_k` of a core joins it (its halo). Everything else is reported as
     stray mass.
   - Position is the mass-weighted centroid `y = L sum w t / sum w`; mass is the summed weight.

   In the first run, cores only (no halo) gave an artificial `-7e-4` mass deficit at `log 5 = L/2` for
   `x = 25`: the missing mass sat on the neighbouring grid point, below the support threshold. With the halo
   the deficit is `-1e-6`.

The mp IPM converges to the analytic centre of the optimal face. When the maximiser is not unique, what is
reported is that canonical maximiser.

## 3. Certified brackets

Every bracket below is `[lb, ub]` on `max lambda_min`, with both ends certified at 80 digits. `tau* = -f` is
printed to 10 digits. Across all 48 levels at `x = 13`, `(ub - lb)/|lb| <= 1.6e-14`: the two ends agree to
13–25 digits.

| N | M | level 0 | level 1 | level 2 | level 3 |
|---:|---:|---:|---:|---:|---:|
| 10 | 64 | 1.79538954e-4 | 2.782556624e-6 | **-3.528097345e-7** | **-3.733606042e-7** |
| 10 | 128 | 5.220101253e-5 | 3.189556808e-7 | **-3.656586086e-7** | **-3.737075355e-7** |
| 10 | 256 | 7.888673263e-6 | **-1.640696275e-7** | **-3.708040166e-7** | **-3.738808147e-7** |
| 20 | 64 | 1.796780712e-4 | 3.153111457e-6 | 2.176452432e-8 | 4.515696104e-10 |
| 20 | 128 | 5.253741767e-5 | 6.978682428e-7 | 8.910494501e-9 | 1.819684857e-10 |
| 20 | 256 | 8.253714067e-6 | 2.080175622e-7 | 3.260907690e-9 | 4.742868318e-11 |
| 40 | 64 | 1.796782996e-4 | 3.153393920e-6 | 2.180643103e-8 | 4.529557898e-10 |
| 40 | 128 | 5.253792263e-5 | 6.979302895e-7 | 8.932919481e-9 | 1.824380832e-10 |
| 40 | 256 | 8.254108074e-6 | 2.080561843e-7 | 3.269575183e-9 | 4.758355862e-11 |
| 60 | 64 | 1.796783179e-4 | 3.153438700e-6 | 2.180655831e-8 | 4.529648834e-10 |
| 60 | 128 | 5.253796887e-5 | 6.979312559e-7 | 8.933000905e-9 | 1.824388332e-10 |
| 60 | 256 | 8.254146662e-6 | 2.080562597e-7 | 3.269615661e-9 | 4.758362899e-11 |

Grid spacing `h` in `y`, per level, is `L/M` times `1, 1/8, 1/64, 1/512`. For `M = 256` that is `1.00e-2`,
`1.25e-3`, `1.57e-4`, `1.96e-5`.

What the table shows:

- **Every grid at `N >= 20` is certified empty (`tau* > 0`) at every level.** The level-0 values reproduce the
  reviewer's float brackets (`1.7968e-4`, `5.254e-5`, `8.2537e-6` at `N = 20`) and pin them to 10+ digits.
- **Negative `tau*` (bold) at `N = 10`:** from level 1 or 2 on, the refined grid is **feasible**. The
  most-positive measure then has `lambda_min = +3.74e-7`, against `2.8e-26` for the true measure.
- **`tau*` falls like `h^2`:** the level-to-level exponent `log_8(ratio)` lies in `1.77..2.10` for
  `M = 128, 256` and `1.86..2.39` for `M = 64`.
- **`tau*` is `N`-independent from `N = 40` to `60`**, to at most `2e-5` relative at every level. `N = 20`
  differs from `N = 40` by at most `3.3e-3`.

## 4. Blind recovery at x = 13 (COMPARISON WITH THE PRIMES; uses no zeros)

Visible prime powers: 2, 3, 4, 5, 7, 8, 9, 11. The endpoint 13 is invisible. True mass
`sum Lambda(n)/sqrt n = 4.2604954`. Table entries are `centroid - log n / mass/(Lambda(n)/sqrt n) - 1`.

**Level 0.**
- On `L/128` and `L/256`, at every `N >= 20`: exactly one cluster at each visible prime power and nothing else.
  Every centroid is within `1.04 h` (`L/128`) and `0.41 h` (`L/256`).
- On `L/64` (`h = 0.040`): `log 8` and `log 9` (2.9 h apart) merge into one cluster, giving 7 clusters. They
  separate after refinement.

**Finest level (3), grid family `L/256`, `h = 1.96e-5`:**

| N | n=2 | n=3 | n=4 | n=5 | n=7 | n=8 | n=9 | n=11 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | +3.4e-6 / +2.7e-5 | +5.6e-5 / +5.0e-4 | +8.9e-4 / +6.9e-3 | +1.1e-3 / +9.1e-4 | +8.1e-3 / +1.2e-1 | (merged with 9) | -2.6e-2 / +4.6e-1 | +3.4e-2 / +5.8e-1 |
| 20 | +4.5e-10 / +2.2e-9 | +1.6e-9 / +6.6e-9 | +6.3e-9 / +2.4e-8 | +4.4e-9 / -3.1e-9 | +6.7e-8 / +1.6e-6 | +2.6e-6 / +4.2e-5 | +5.5e-6 / +1.5e-5 | +4.3e-5 / +1.0e-3 |
| 40 | +4.5e-10 / +2.2e-9 | +1.5e-9 / +6.3e-9 | +5.8e-9 / +1.9e-8 | +3.4e-9 / -6.9e-9 | +6.2e-9 / +5.4e-8 | +2.2e-8 / +1.0e-8 | +1.7e-8 / -2.8e-8 | +1.1e-7 / +3.6e-6 |
| 60 | +4.5e-10 / +2.2e-9 | +1.5e-9 / +6.3e-9 | +5.8e-9 / +1.9e-8 | +3.4e-9 / -6.9e-9 | +6.2e-9 / +5.4e-8 | +2.2e-8 / +7.4e-9 | +1.6e-8 / -2.9e-8 | +1.0e-7 / +3.1e-6 |

At `N = 20, 40, 60` the stray mass at the finest level is at most `1e-9`. The total mass is `4.2604977` at
`N = 60`, against the true `4.2604954`.

**Refinement history, `N = 60`, `L/256`:**

| level | h | n=2 | n=5 | n=8 | n=9 | n=11 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1.00e-2 | +7.8e-5 / +3.7e-4 | +7.0e-4 / -1.3e-3 | +3.6e-3 / -2.2e-2 | +1.5e-3 / -4.4e-3 | +1.5e-3 / +9.6e-3 |
| 1 | 1.25e-3 | +2.1e-6 / +1.1e-5 | +1.2e-5 / -2.6e-5 | +4.6e-5 / -1.0e-4 | +2.6e-5 / -1.2e-4 | +2.6e-5 / +2.8e-4 |
| 2 | 1.57e-4 | +3.1e-8 / +1.6e-7 | +2.2e-7 / -3.3e-7 | +1.2e-6 / -2.2e-6 | +6.1e-7 / -3.1e-6 | +7.9e-7 / +1.3e-5 |
| 3 | 1.96e-5 | +4.5e-10 / +2.2e-9 | +3.4e-9 / -6.9e-9 | +2.2e-8 / +7.4e-9 | +1.6e-8 / -2.9e-8 | +1.0e-7 / +3.1e-6 |

**Rates.** For `N = 40, 60` on `L/128` and `L/256`, `log_8` of the level-to-level ratio lies in `[1.73, 2.47]`
for all three of `tau*`, the maximum position error and the maximum mass error (`n <= 9`); it is checked to lie
in `[1.6, 2.6]`. So the errors fall like `h^2`, three levels deep. On `L/64` the first refinement is irregular:
a transient extra cluster near `log 8` at level 1. After that the rates are 1.86–4.6 for `N = 40, 60`.

**`N` dependence.**
- `N = 40` and `N = 60` are indistinguishable: per-atom errors agree to two digits, and `tau*` agrees to
  `2e-5` relative.
- `N = 20` recovers the interior atoms equally well: `n = 2..5` within `6.3e-9` in position. The atoms nearest
  the invisible edge lag, and do not follow `h^2` from level 1 to 2: `n = 11` is `+4.3e-5 / +1.0e-3`, against
  `+1.1e-7 / +3.6e-6` at `N = 40`. This is the edge mechanism of lane L's L4.3.
- `N = 10` fails; see section 5.

## 5. Saturation, the interior, and N -> infinity

The task asked whether the errors saturate at a floor consistent with lane L's interior.

- **`N = 10`: yes, visibly.**
  - The refined grids become feasible. `max lambda_min` converges to `+3.734e-7 .. +3.739e-7` across
    `M = 64, 128, 256`. The true measure's value is `+2.83e-26`.
  - The maximiser converges to a **different, strictly feasible measure**: 7 clusters at `0.6932, 1.0987,
    1.3872, 1.6105, 1.954, 2.1716, 2.4323` with total mass 4.6901 (truth 4.2605).
  - `log 8` and `log 9` are fused at 2.17. The edge cluster at 2.43 carries 58% excess mass.
  - Its errors are frozen from level 2 on: level 2 and level 3 agree to two digits for every atom. That is a
    floor, and it is set by the problem, not the grid.
  - This is lane L3's statement made concrete: a strictly positive truth sits in the interior of the feasible
    set, and the maximiser of `lambda_min` need not be the truth. `N = 10` lies below `2s = 16`, the sufficient
    exact-moment threshold of G2 (`s = 8` atoms), and just below the empirical pinning threshold `N ~ 11` found in
    the review of G2.
- **`N = 20, 40, 60`: no floor down to the resolution reached.**
  - Every grid optimum is negative: at level 3, `lambda_min <= -4.5e-10`. The true measure's value is
    positive: `1.566e-39` at `N = 20`, `9.46e-54` at `N = 40`, `1.01e-58` at `N = 60`. So the grid maximiser
    has not yet entered the feasible set.
  - Since `tau* ~ h^2`, reaching the truth's scale would need `h ~ 1e-20 .. 1e-30`.
  - Lane L's weight-box widths at fixed positions (outer LP bounds) are `3e-25 .. 2.7e-7` for `n = 2..11` at
    `N = 20`, and `2.3e-36 .. 1.6e-13` at `N = 40`. Both are far below our errors, so the interior is not
    reached. The data can neither confirm nor exclude a floor below `1e-8`.
  - The coercivity floor (lane L3.2/3.4) is 50 orders further down: `eps_N = 2.85e-59` at `x = 13, N = 200`
    (lane L, not recomputed), and under RH it decreases to a positive `mu_L`.
- **`N -> infinity` in the data.**
  - At fixed `x = 13` on grids resolving the cutoff, results are `N`-independent from `N = 40` on.
  - On a **fixed** grid, raising `N` beyond the grid's resolution destroys recovery. At `x = 25, N = 134` on
    `L/128`, `h = 0.025` exceeds `L/(2N+1) = 0.012` and the moment map has rank `127 < 269`. There
    `tau* = 0.24437910478` (certified), and the maximiser has 3 clusters at level 0 and 21 clusters, most of
    them spurious, after one refinement.
  - So the order of limits matters: the grid must resolve `L/(2N)` before `N` grows.

## 6. x = 25

Visible prime powers: 2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23; true mass 7.1616227. `log 16` and `log 17`
are `0.0606` apart.

| case | level | h | tau* (certified; rel. width) | clusters | 16 / 17 |
|---|---:|---:|---|---:|---|
| N = 60, L/128 | 0 | 2.51e-2 | 8.56613283304e-5 (2e-21) | 12 | **not separated** (one cluster, 0.021 below log 17) |
| | 1 | 3.14e-3 | 1.3497787984e-6 (2e-20) | 14 | separated: `+5.1e-4 / -3.7e-3` and `+5.6e-5 / -1.5e-3`; a 0.0014 satellite 0.032 below log 16 |
| | 2 | 3.93e-4 | 4.09318639739e-9 (7e-17) | 14 | separated: `+1.2e-5 / +2.9e-4` and `+2.1e-6 / -8.5e-5` |
| N = 134, L/128 | 0 | 2.51e-2 | 0.244379104775 (4e-16) | 3 | under-resolved (see section 5) |
| | 1 | 3.14e-3 | 8.52755934232e-5 (2e-14) | 21 | multiple spurious clusters |
| N = 134, L/512 | 0 | 6.29e-3 | 4.05799221404e-6 (3e-13) | 14 | separated at level 0: `+4.3e-3 / +0.16` and `+2.1e-3 / -0.039` |
| | 1 | 7.86e-4 | 8.404935229e-9 .. 8.404935239e-9 (1.2e-9) | 13 | separated: `+3.5e-5 / +7.8e-4` and `+5.2e-6 / -2.3e-4` |

**`N = 60`, level 2.** All 13 prime powers are recovered. Positions are within `1.5e-6` for `n <= 13` and
`n = 19`, `2.1e-6` at 17 and `1.2e-5` at 16. Masses are within `4e-5` for `n <= 13` and `n = 19`, `2.9e-4` at 16
and `8.5e-5` at 17.

The edge atom `23` (`t = 0.974`) is split. The main cluster is at `+3.6e-4` with `-5.5%` mass, and a
satellite of mass `0.037` sits `4.6e-3` below. Their combined mass is within 0.3% of the truth. Stray mass is
`8.9e-5`.

**`N = 134`, `L/512`, level 1.**
- Exactly 13 clusters, one per prime power.
- Positions are within `2.7e-6` for `n <= 13` and `n = 19`; `5.2e-6` at 17, `1.9e-5` at 23, `3.5e-5` at 16.
- Masses are within `9.5e-5` except at 16 (`7.8e-4`) and 17 (`2.3e-4`). `log 5 = L/2` lies on the grid:
  `+5.5e-7 / -2.1e-6`.
- Stray mass is `2.5e-4`.

**Answer to "do 16 and 17 separate".** They separate at higher `N` **only together with** a finer grid, and at
`N = 60` after one refinement. At `N = 134` the `L/128` grid is under-resolved and nothing is recovered.

## 7. Controls (x = 13, grid L/256, same pipeline, certified brackets)

| input form | N | final level | max lambda_min | clusters | where the mass goes |
|---|---:|---:|---:|---:|---|
| pole only (arch -> 0) | 20 | 2 | **+0.2468** (feasible) | 20 | an equally spaced comb at spacing `0.123 ~ L/(N+1)` (0.123, 0.247, 0.370, ...); total mass 6.34; max offset from nearest log n 0.57 |
| pole only | 40 | 1 | +0.1258 (feasible) | 40 | comb at spacing `0.063 ~ L/(N+1)`; mass 6.50 |
| arch negated | 20 | 2 | -0.7525 | 20 | comb at spacing ~0.122 starting at 0.090; mass 8.77 |
| arch negated | 40 | 1 | -1.676 | 40 | comb at spacing ~0.063; mass 9.37 |
| pole x 0.9 | 20 / 40 | 2 / 1 | -0.1186 / -0.1186 | 8 / 8 | clusters at 0.778, 1.228, 1.535, 1.784, 1.871, 2.175, 2.36, 2.50: offsets up to 0.16, mass errors up to 120% |
| pole x 1.1 | 20 / 40 | 2 / 1 | +0.1063 / +0.1063 (feasible) | 11 / 13 | clusters at 0.625, 0.993, 1.259, 1.36, 1.455, 1.76, 1.87, ...: offsets up to 0.16, mass errors up to 99% (N = 20) and 236% (N = 40) |
| true (reference) | 20 | 3 | -4.74e-11 | 8 | the prime powers (section 4) |

**Signed weights (D3, verified in mp).** On `L/256` the certificate constructs `w` with `H0 + T(w) = c I`
exactly, up to a moment residual `<= 3e-79`, for `c = 1, 10, 100`.

| N | c | lambda_min | sum abs(w) | sum w | negative weights |
|---:|---:|---:|---:|---:|---:|
| 20 | 1 | 1 | 5.9 | 4.39 | 28 |
| 20 | 10 | 10 | 17.8 | -2.33 | 96 |
| 20 | 100 | 100 | 211 | -69.5 | 128 |
| 60 | 1 | 1 | 9.3 | 4.80 | 43 |
| 60 | 10 | 10 | 27.6 | -2.73 | 107 |
| 60 | 100 | 100 | 368 | -78.1 | 128 |

The signed problem is unbounded, and the construction spreads signed mass over the whole window.

**What the controls say.** The positional information sits in the **exact balance between the pole and the
archimedean term**, together with the sign of `w`.

- Remove or flip the archimedean term and the maximiser becomes a translation-invariant comb at the Fourier
  scale `L/(N+1)`, one cluster per unit of cutoff. Nothing in it refers to arithmetic.
- Mis-scale the pole by 10% and the grid is either feasible with margin 0.1, so the maximiser drifts to an
  interior point unrelated to the primes, or infeasible by 0.12, so it compromises. Either way the positions are
  off by up to 0.16.
- Only the true balance makes the problem **critical**, with `tau* -> 0` under refinement. In that regime, and
  only there, the maximiser is pinned to the prime powers.

## 8. What went wrong, and limitations

- **Float64 is not enough.** The float IPM's Schur complement reaches condition `1e21..1e25` near the optimum,
  and float brackets stall at `~1e-10` absolute. The reviewer's float Kelley brackets at refined levels were not
  converged: its level-2 bracket `[-1.72e-8, -3.6e-9]` spans a factor of 5. Its refined grids omit the
  uniform grid, so it is not directly comparable with the certified `-3.2609e-9` here. Two consequences:
  - Its level-2 positions agree with ours in magnitude for `log 2..log 5`: reviewer `2.7e-8 .. 1.8e-7`, here
    `3.1e-8 .. 4.0e-7` at level 2, `N = 20`. At `log 7` we find `+2.3e-6`, against the reviewer's `-3.0e-7`.
  - Its edge values (`log 11` within `8e-4`) were solver-limited. At `N = 20` we find `1.9e-4` at level 2.
- **Cluster bookkeeping.** The first run used cores only. It reported a spurious `-7e-4` mass deficit at
  `log 5 = L/2` for `x = 25`, which came from sub-threshold mass on the neighbouring point. Halo assignment
  fixed it. The support threshold `1e-4` of the total still defines "cluster"; stray mass is printed per level.
- **Refined optima are grid optima.** Level `k` contains the uniform level-0 grid plus patches, so a better
  configuration off the patches is only visible at spacing `h_0`. The certificates certify the optimum **on each
  level grid**, not over all positions.
- **`N = 134` precision and run time.** At `x = 25, N = 134` the mp IPM ran at 34 digits (`mu` down to
  `1e-18`); the level-1 bracket there has relative width `1.2e-9`. Its run time (about 10 min per level) set
  the wall clock.
- **Rigour caveat.** The certificates are mpmath at 80 digits with explicit rounding bounds, not interval
  arithmetic. The data error rests on zst's balls, compared entrywise.
- **Non-uniqueness.** Wherever the optimal face is not a point, the reported maximiser is its analytic centre.

## 9. Verdict

The statement "the most positive nonnegative measure compatible with the pole and the archimedean place on a
window sits on the primes with von Mangoldt weights" is **supported, as a finite-window variational statement,
for `N` above the atom count and to the precision reached**.

At `x = 13`:
- With the pole and archimedean data exact and `w >= 0`, the certified maximiser of
  `lambda_min(H0 + T(w))` over three-times-refined uniform grids has exactly one cluster per visible prime
  power and no stray mass.
- At `N = 40, 60` the positions are within `2e-8` of `log n` (`1e-7` at the edge atom 11). The masses are within
  `5e-8` of `Lambda(n)/sqrt n` (`3.6e-6` at 11).
- Both errors fall like `h^2`, from `h = 1e-2` to `h = 2e-5`, with no sign of a floor.

At `x = 25`:
- 13 clusters, with `log 16` and `log 17` separated once the grid is fine enough.

It is not an exact-recovery statement. The only floor the data show is the one the theory predicts:
- At `N = 10` the maximiser converges to a strictly feasible measure with `lambda_min = 3.7e-7`, far above the
  truth's `2.8e-26`, which is not the prime measure. This is lane L3's interior, made visible.
- At `N >= 20` every grid optimum is still negative: `-4.5e-10 .. -4.7e-11` at level 3. The truth's
  `lambda_min` is `+1.6e-39` (`N = 20`) down to `+1.0e-58` (`N = 60`). Lane L's interior and the coercivity
  floor are far below the resolution reached, so the data neither confirm nor exclude a floor there.
- As `N -> infinity` at fixed `x`, the results stabilise from `N = 40` on, provided the grid resolves
  `L/(2N)`. On a fixed grid, larger `N` destroys recovery.

The controls show that the positional signal is carried by the exact pole–archimedean balance, which makes the
problem critical. Pole-only, sign-flipped or 10%-mis-scaled data give Fourier-scale combs or off-prime clusters,
and dropping the sign makes the problem unbounded.

Proposed row, unregistered: `num:rtp-grid-blind-recovery-certified`.

## 10. Reproduction

    python3 scripts/rtp2_blind_recovery.py > outputs/rtp2_blind_recovery.txt      # ~28 min on 64 cores

`RTP2_BR_CACHE=<file>` optionally pickles the raw results, so the report can be re-run without recomputing. It
is a development aid, off by default, and writes only where pointed.
