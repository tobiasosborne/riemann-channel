# Lane B2: the kinematic commutant and the calibration case (RTP-1, Steps 4 and 5)

Author: `claude:opus`, 2026-09-24. Brief: `notes/rtp-round-1/brief.md` (Lane B2; author `claude:fable-5.1`), with the
orchestrator's corrections after lanes A1, A2 and B1 (B2.1 reformulated with the prime data as the unknown; lane A1's
structured interval (A1.1') in place of "disc" or "ellipsoid"; the archimedean form is not called positive).
Status: numerics lane, unreviewed (REFUTE lane R pending). Nothing here is registered as a claim.

Code: `scripts/rtp1_commutant.py` (B2.1), `scripts/rtp1_calibration.py` (B2.2). Both are deterministic (seed
20260924), use a single `check(cond, msg)` helper in the style of `scripts/gl1_bond.py`, print no timestamps, and run in
about 2.5 minutes each on one thread. `rtp1_commutant.py` reads `(a_n, b_n)` from zst through a 25-line C printer that it
compiles at run time against `zst/build/libzst.a`, as `scripts/rtp1_prime_content.py` does. zst is not modified.
Outputs: `outputs/rtp1_commutant.txt` (37 checks, 0 failed) and `outputs/rtp1_calibration.txt` (33 checks, 0 failed).
Each was produced from the repository root with `python3 scripts/<name>.py > outputs/<name>.txt 2>&1`, run twice, and
confirmed byte-identical with `cmp`.

Game rules. RH is not assumed. Every number that enters a zeta form comes from `zst_riemann_ab` (pole, primes,
archimedean place) or from closed forms of the pole term. Zeros of zeta are not used anywhere in this lane. In the
calibration script the graph's spectrum is used in two places only. The first is the section headed `COMPARISON STEP`.
The second is the exact certificate that the random graph is Ramanujan, which decides which graph is used and never
builds a form.

Precision.
- zeta data: zst balls at 400 bits (radii at most `1e-115`). Linear algebra on the true form (spectra, the ray through
  the truth, near-kernels): mpmath at 100 digits.
- Convex optimisation (minimal-norm and maximum-determinant problems): IEEE double, using a log-det barrier with damped
  Newton steps. Each solution carries a duality gap or KKT residual, and its feasibility is re-checked at 100 digits.
- The lattice box (Section 4): outer bounds from LP dual vectors re-verified at 100 digits. These are valid bounds in
  100-digit arithmetic but are not ball-certified.
- Graphs: traces are exact integers. `nu_k` are arb balls at 600 bits. Eigenvalues are certified enclosures
  (`acb_mat.eig`), so every sign and every negative count is certified. The exception is the permutation's degenerate
  spectra, where the script falls back to mpmath and says so.
- Levinson recursion, overlaps and kernel roots: mpmath at 180 digits.

## 0. Answers in brief

- **Dimension counts (B2.1(a)).** On `E_N = span{V_n : |n| <= N}` the exact dimensions over `Q` (checked for `N = 1..6`)
  are:
  - Hermitian forms: `(2N+1)^2`;
  - commuting with `gamma`: `(N+1)^2 + N^2`;
  - real: `(N+1)(2N+1)`;
  - both: `(N+1)^2`;
  - Loewner (`[D, H] = |beta><eta| - |eta><beta|`, `eta = sum V_n`): `4N+1`, and a Loewner form is automatically real;
  - Loewner and `gamma` together: **`2N+1`**, which is exactly the data `(a_0..a_N, b_1..b_N)`.

  The positive cone of this kinematic space contains the identity in its interior, so its linear span is the whole
  `2N+1`-dimensional space. Positivity removes no dimension, and no linear kinematic condition on `(a, b)` is left.
- **The positive set of prime data (B2.1(b)).** Fix the true pole and archimedean data and leave the prime data `(u, v)`
  free. The admissible set `P_N = {(u, v) : H0 + T(u, v) >= 0}` is a closed convex spectrahedron in `R^{2N+1}`:
  - It is **full-dimensional** (dimension `2N+1`) and **unbounded**.
  - Its recession cone is the full positive cone of the kinematic space, so any positive Loewner form can be added to an
    admissible prime datum.
  - `0` is not in `P_N`: `H0` has 2 + 2 negative eigenvalues (even + odd) at `x = 13`, with `lambda_min = -1.96`.
  - The maximum-determinant element does not exist, because `sup log det = +infinity`.
  - The minimal-norm element exists. At `N = 20` its Hilbert-Schmidt norm is 2.36, against 8.21 for the truth, and it
    lies on the boundary with rank deficiency 1 + 2.
- **Distance from the true prime data (B2.1(c)).** At `x = 13`, `N = 20`:
  - The minimal-norm prediction has relative distance **0.957** and captures **8.3%** of the true prime contribution
    (the Hilbert-Schmidt projection).
  - The maximum-determinant element on the ball of the true norm is at relative distance **1.34**, which is worse than
    predicting no prime data at all.
  - The PNT mean (the prime distribution replaced by the pole's density `e^{y/2}`) is **not admissible**
    (`lambda_min = -1.23`). It captures 22%, at relative distance 0.91.
  - As `N` grows, all predictions get worse: the minimal-norm prediction captures 16% at `N = 10` and 2.8% at `N = 60`.
  - What positivity does fix is the compression of the prime form to the four negative directions of `H0`: the
    minimal-norm prediction matches it to **7%** (3.9% in the coefficient norm), and matches `(u_1, u_2, v_1, v_2)`
    to 6%.
  - The truth sits on the boundary of `P_N`, to within `lambda_min(H_true) = 1.6e-39`. It is isolated on its own ray:
    the admissible multiples `s T_true` fill `[1 - 5.7e-36, 1 + 2.0e-38]`.
- **With the lattice known (B2.1(d), beyond the brief).** Keep the possible positions `log n`, `n = 2..12`, and leave the
  11 weights free. The same positivity then **pins every weight**. The certified outer box widths at `N = 20` are
  `<= 1.1e-7` for `n <= 9`, `2.2e-6` for `n = 10`, `1.1e-5` for `n = 11` and `1.3e-3` for `n = 12`. This includes the
  zero weights at 6, 10 and 12. The Loewner coordinates hide this.
- **Calibration learning curve (B2.2).** The random Ramanujan cubic graph G40 has `R = 78` distinct atoms.
  - Along the window `K`, which is also the data cutoff: `lambda_min(T_K)` falls smoothly, at 0.13 to 0.79 decimal digits
    per unit of `K`, which is a **power law** `x_eq^{-0.44 .. -2.6}` in `x_eq = q^K`. It reaches **exactly 0** at
    `K = R = 78`.
  - The next trace is interior to its disc until `K = R - 1`, where it is on the boundary.
  - At fixed window the partial forms are indefinite until the last cycle length enters, at scale `q^{K/2}`: with only the
    last length missing, `lambda_min = -3.9e11`.
  - `lambda_min` is a cancellation residual, as for zeta.
  - The Petersen graph (girth 5, critical window 4) has **no prime datum in its window**: kinematics alone give its exact
    singular form.
- **Contrast with zeta (lane A1).**

  | aspect | zeta (lane A1) | graph (calibration) |
  |---|---|---|
  | collapse | never | finite (`K = R`) |
  | rate | `e^{-4 pi x}` | power law in `x_eq` |
  | resolution axis / saturation | saturation at `N_sat ~ 1.7 x log x` | no resolution axis; the analogue of `N_sat` is `K = R` |
  | last datum missing at fixed window | `-5.7e-7` | `-3.9e11` |
  | kinematic form | indefinite by O(1) in 1 to 3 directions | one negative direction of size `q^{K/2}` |

  The fixed-window difference is a continuous-versus-discrete edge effect, not arithmetic. Both forms are cancellation
  residuals.

## 1. B2.1(a): the kinematic constraints as linear conditions

Ambient space: Hermitian `(2N+1) x (2N+1)` matrices `H = (H_nm)`, `n, m = -N..N`, in the orthonormal basis `V_n`. As a
real vector space its coordinates are `h_nn`, `Re h_nm` and `Im h_nm` (`n < m`). The conditions are:

- `[gamma]`: `gamma H gamma = H`, i.e. `H_{-n,-m} = H_nm`. This is the Weyl element of the window.
- `[real]`: `Im H_nm = 0`.
- `[Loewner]`: there is a `beta in C^{2N+1}` with `(n - m) H_nm = beta_n - conj(beta_m)` for all `n, m`. This is
  `[D, H] = |beta><eta| - |eta><beta|` with `D V_n = n V_n` and `eta = sum_n V_n` (plan.md 1.1). The diagonal equations
  force `Im beta_n = 0`, and `beta` is determined up to a real constant.

Each condition is real-linear in `H`, or in `(H, beta)`. The dimension of the space cut out with the auxiliary `beta` is
the dimension of the solution space minus that of its `beta`-only part (1). Exact ranks over `Q` (`fmpq_mat`) for
`N = 1..6` agree with these closed forms:

| space | dimension | N = 1..6 |
|---|---|---|
| Hermitian | `(2N+1)^2` | 9, 25, 49, 81, 121, 169 |
| + gamma | `(N+1)^2 + N^2` | 5, 13, 25, 41, 61, 85 |
| + real | `(N+1)(2N+1)` | 6, 15, 28, 45, 66, 91 |
| + gamma + real | `(N+1)^2` | 4, 9, 16, 25, 36, 49 |
| Loewner | `4N+1` | 5, 9, 13, 17, 21, 25 |
| Loewner + real | `4N+1` | (same: reality is automatic) |
| Loewner + gamma (= + real) | `2N+1` | 3, 5, 7, 9, 11, 13 |

The kinematic space `K_N` = Loewner + gamma is the set of Loewner forms of real sequences with `a` even and `b` odd,
which is zst's data format. Its `2N+1` basis forms are independent (Gram matrix in the Hilbert-Schmidt inner product:
minimal eigenvalue 0.56 at `N = 20`, 0.29 at `N = 40`). Every such `(a, b)` is the Loewner data of some smooth real
distribution `D` on `[0, L]`, because the `2N+1` functions `(1 - y/L) cos(2 pi n y/L)` and `sin(2 pi n y/L)` are
independent. So no linear kinematic condition on `(a, b)` remains. The identity (`a = 1`, `b = 0`) is an interior point
of the positive cone `C_N`. Hence `span C_N = K_N`, of dimension `2N+1`, and `C_N` is a pointed full-dimensional
cone. **Before any arithmetic datum, the kinematics leave `2N+1` free parameters, and positivity is an inequality that
removes none.**

## 2. B2.1(b): the positive set of the prime data

Set-up (`x = 13`, i.e. `L = log 13`, prime powers 2, 3, 4, 5, 7, 8, 9, 11, and 13 with weight exactly 0). zst's totals are
split using its prime-cutoff argument:

- prime part = `(X = 13) - (X = 1)`, which equals the closed form of plan.md 1.2 to `2.4e-99`;
- pole part = closed form;
- archimedean part = `(X = 1) - pole`, which reproduces `b^R_n = I_1(n)/pi` by quadrature to `1.9e-42`.

zst's `a_1` and `b_1` agree with lane A1's 30 printed digits. `H0` is the Loewner form of pole plus archimedean. `T(u, v)`
is the Loewner form of the prime data, `z = (u_0..u_N, v_1..v_N)`, and `P_N = {z : H0 + T(z) >= 0}`. Two norms are used:

- `||z||_HS`, the Hilbert-Schmidt norm of `T(z)` on `E_N` (basis-free);
- `||z||_c = (sum_{|n| <= N} u_n^2 + v_n^2)^{1/2}`.

Characterisation (all at `N = 20` unless stated otherwise; the `N`-table is below):

1. **`0` is not in `P_N`.** `H0` has 2 negative even eigenvalues (`-0.848`, `-0.170`) and 2 negative odd ones (`-1.961`,
   `-0.418`), consistent with lane A1's control (2 even for `x = 9..23`). This is indefinite, as lane B1 says of pole
   plus archimedean outside short support.
2. **`P_N` is full-dimensional**, of dimension `2N+1`: `z_true + delta (1, .., 1, 0, .., 0)` has `lambda_min >= delta`.
3. **`P_N` is unbounded.** `T = cI` is admissible for `c >= 1.96`, and `log det(H0 + cI) = 98.9, 189.3, 283.3` at
   `c = 10, 100, 1000`. The recession cone is `{z : T(z) >= 0} = C_N`, which is full-dimensional, and `P_N + C_N = P_N`.
   Kinematics plus positivity therefore give only lower bounds, in the Loewner order, on the prime data. **The
   maximum-determinant element does not exist.**
4. **Where the truth sits.** `lambda_min(H_true) = 1.566e-39` at 100 digits (lane A1 certifies 1.57e-39), so the truth
   is in `P_N`, but on its boundary to working precision. The ray `s -> H0 + s T_true` meets `P_N` in
   `[1 - 5.7e-36, 1 + 2.0e-38]`, so the true prime data are both the smallest and the largest admissible multiple of
   themselves (at every `N` tested, both ends are within `1e-20` of 1). `H_true` has 9 + 9 eigenvalues below `1e-3`,
   8 + 8 below `1e-6`, 4 + 4 below `1e-20` and 2 + 2 below `1e-30`. The near-kernel conditions `W^T T(z) W = 0`
   have rank exactly `k(delta)`, the number of near-zero eigenvalues, not `k(k+1)/2` (the singular-value gap exceeds
   `1e3`). So each near-zero eigenvalue of the true form costs one condition on the prime data, and the face of `P_N`
   through the truth has dimension `2N+1 - k(delta)`: 23, 25 and 28 at `delta = 1e-3, 1e-6, 1e-10`.
5. **Minimal-norm elements.** These were computed with a barrier method, `t` up to `1e10`, and a dual certificate from
   the central path. `min ||z||_HS = 2.3601` (duality gap `4.1e-9`) against `||z_true||_HS = 8.2133`, and
   `min ||z||_c = 1.9566` against 6.0969. Both minimisers are on the boundary (`lambda_min = 3.8e-11` and `4.6e-11`
   at 100 digits), with rank deficiency 1 + 2. The minimal norm is essentially independent of `N` (2.336 to 2.378 for
   `N = 10..60`).
6. **Maximum determinant, relaxed** to the ball `||z||_HS <= ||z_true||_HS`. The maximiser lies on the sphere, with
   multiplier `mu = 0.363`, KKT residual `1.2e-7`, `lambda_min = 0.891` and `log det = 35.0` (truth: `-780.4`). It
   raises every `u_n` by about 1: it is essentially "add the identity".

## 3. B2.1(c): the kinematic predictions against the true prime data (`x = 13`, `N = 20`)

In the table below:
- `rel. dist` = `||z_p - z_true||_HS / ||z_true||_HS`;
- `captured` = `<z_p, z_true>_HS / ||z_true||_HS^2`, the fraction of the true prime contribution along the prediction;
- `on neg(H0)` = the relative distance of the compressions `W^T T W` to the four negative directions `W` of `H0`, the
  only directions where positivity forces anything.

| prediction | `||z_p||_HS` | rel. dist | captured | cos | on neg(H0) |
|---|---|---|---|---|---|
| zero (no prime data) | 0 | 1.000 | 0 | 0 | 1.000 |
| isotropic `cI`, `c = -lambda_min(H0)` | 12.56 | 1.807 | 0.036 | 0.023 | 1.160 |
| min `||.||_HS` | 2.360 | **0.957** | **0.083** | 0.289 | **0.073** |
| min `||.||_c` | 2.436 | 0.957 | 0.086 | 0.291 | 0.039 |
| max det on the ball `||.||_HS <= ||z_true||_HS` | 8.213 | **1.337** | 0.107 | 0.107 | 1.205 |
| PNT mean (pole density `e^{y/2}`), no positivity | 4.336 | 0.911 | 0.224 | 0.425 | 0.544 |
| nearest point of `P_N` to the PNT mean | 3.816 | 0.887 | 0.214 | 0.461 | 0.018 |

Mode by mode (coefficient table in the output):

- the minimal-norm prediction reproduces `(u_1, u_2, v_1, v_2)` to 5.7% (true `1.2197, 0.3601, -0.4387, -0.2756`;
  predicted `1.2467, 0.3998, -0.4128, -0.2186`);
- it misses `u_0` entirely (predicted 0, true `-2.94`);
- it predicts a smooth decaying tail for `n >= 3`, where the true data are O(1) at every `n`. The true prime
  distribution is eight point masses at `log k`, and these are full-band.

On the negative subspace of `H0` the compression `W^T T W` has eigenvalues:

| | even | odd |
|---|---|---|
| truth | 0.20, 0.87 | 0.43, 1.99 |
| minimal-norm prediction | 0.27, 0.98 | 0.42, 1.96 |

**Positivity fixes what the primes must do on the negative directions of the pole-plus-archimedean form, to about 7%,
and nothing else.**

The PNT predictor is the prime distribution `-sum Lambda(k) k^{-1/2} delta(y - log k)` replaced by its mean density
`-e^{y/2} dy`. By the explicit formula, that mean is the pole's density. The predictor uses no prime and is the natural
"kinematic mean". It is not admissible: `lambda_min(H0 + T_PNT) = -1.226`. Its accuracy depends on `x` and `N`
(section 5b of the output):

| x | N = 40: rho | captured | N = ceil(1.7 x log x): N | rho | captured |
|---|---|---|---|---|---|
| 13 | 0.957 | 0.110 | 57 | 0.970 | 0.079 |
| 25 | 0.925 | 0.166 | 137 | 0.979 | 0.048 |
| 50 | 0.875 | 0.252 | 333 | 0.986 | 0.030 |
| 100 | 0.802 | 0.372 | 783 | 0.991 | 0.019 |
| 200 | 0.692 | 0.533 | | | |

At fixed resolution the pole mean slowly learns the low modes as `x` grows. At the saturation resolution of lane A1 it
gets worse with `x`, because the point masses at `log k` are full-band and the mean density is not.

Dependence on `N` (`x = 13`; `N_sat(13) ≈ 56`):

| N | neg H0 | lmin H0 | lmin H_true | 1 - s_lo | s_hi - 1 | `||z_t||_HS` | min HS | dist | capt | max-det dist | capt | PNT dist | capt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10 | 2+2 | -1.936 | 2.83e-26 | 3.5e-23 | 2.3e-25 | 5.855 | 2.336 | 0.916 | 0.160 | 1.248 | 0.221 | 0.817 | 0.439 |
| 20 | 2+2 | -1.961 | 1.57e-39 | 5.7e-36 | 2.0e-38 | 8.213 | 2.360 | 0.957 | 0.083 | 1.336 | 0.107 | 0.911 | 0.224 |
| 30 | 2+2 | -1.971 | 4.92e-48 | 3.4e-44 | 7.4e-47 | 9.998 | 2.369 | 0.971 | 0.056 | 1.384 | 0.042 | 0.941 | 0.152 |
| 40 | 2+2 | -1.975 | 9.46e-54 | 1.0e-49 | 1.5e-52 | 11.739 | 2.373 | 0.979 | 0.041 | 1.378 | 0.051 | 0.957 | 0.110 |
| 60 | 2+2 | -1.980 | 1.01e-58 | 2.6e-54 | 1.7e-57 | 14.167 | 2.378 | 0.986 | 0.028 | 1.389 | 0.035 | 0.971 | 0.076 |

The `lambda_min(H_true)` column reproduces lane A1's certified `eps_N` at `x = 13`. The captured fraction falls roughly
like `||z_true||^{-2}`: the correction that positivity demands is fixed (norm about 2.37), while the truth's norm grows
like `sqrt N` because the prime data are full-band.

## 4. B2.1(d): the lattice-restricted problem (not in the brief)

The calibration graph's prime data live on the integer lattice of lags, which its Toeplitz structure builds in. The
zeta analogue keeps the possible positions `log n`, `n = 2..12`, and leaves the weights `w_n` free:
`D_p = -sum w_n delta(y - log n)`, with truth `w_n = Lambda(n)/sqrt n`. The weight is 0 at 6, 10 and 12. `n = 13` has
weight exactly 0 at `x = 13` and is dropped. This is arithmetic input (the multiplicative lattice), but nothing says
which `n` are prime powers. The set is `P_N^lat = {w in R^11 : H0 + T(w) >= 0}`.

The method is an outer bound. For fixed vectors `v_i`, `P_N^lat` lies in `Pi = {w : v_i^T H(w) v_i >= 0}`, and every
such condition is linear in `w`. Take `v_i` to be the `2N+1` eigenvectors of `H_true` (100 digits); then
`Pi = {w : lambda_i + g_i . (w - w_true) >= 0}`. Each face of the box of `Pi` is an LP, solved in double. Its dual vector
`y >= 0`, with `G^T y = +-e_n`, is then re-verified at 100 digits (residual `< 1e-60`), and weak duality gives
`+-(w_n - w_true,n) <= y^T lambda`. The double-precision LP values are not trusted: its feasibility tolerance is
`1e-7`. As a consistency check, moving any single weight out by twice its bound makes the form indefinite in all 22
cases (100-digit spectra).

Certified outer box at `N = 20` (41 conditions, 16 with `lambda_i < 1e-6`):

| n | `Lambda(n)/sqrt n` | `w - w_true >=` | `w - w_true <=` | width |
|---|---|---|---|---|
| 2 | 0.490129 | -1.07e-07 | 2.28e-15 | 1.07e-07 |
| 3 | 0.634284 | -7.75e-14 | 7.71e-08 | 7.71e-08 |
| 4 | 0.346574 | -5.21e-13 | 1.60e-12 | 2.13e-12 |
| 5 | 0.719763 | -4.02e-11 | 1.02e-14 | 4.02e-11 |
| 6 | 0 | -9.35e-14 | 1.92e-10 | 1.93e-10 |
| 7 | 0.735485 | -6.84e-10 | 3.03e-12 | 6.87e-10 |
| 8 | 0.245065 | -1.13e-10 | 3.92e-10 | 5.05e-10 |
| 9 | 0.366204 | -4.85e-09 | 4.76e-08 | 5.24e-08 |
| 10 | 0 | -2.06e-06 | 1.69e-07 | 2.23e-06 |
| 11 | 0.722993 | -8.32e-06 | 2.17e-06 | 1.05e-05 |
| 12 | 0 | -3.78e-04 | 8.90e-04 | 1.27e-03 |

The largest widths as `N` varies (over `n <= 7` / `n <= 10` / `n <= 12`) are:

| N | `n <= 7` | `n <= 10` | `n <= 12` |
|---|---|---|---|
| 10 | 4.2e-5 | 2.9e-2 | 0.70 |
| 20 | 1.1e-7 | 2.2e-6 | 1.3e-3 |
| 30 | 1.9e-7 | 1.9e-7 | 2.2e-5 |
| 40 | 2.8e-6 | 2.8e-6 | 2.8e-6 |
| 60 | 2.0e-7 | 2.0e-7 | 7.0e-7 |

The widths at `N >= 30` are limited by the certificate construction (blends of the LP dual with a strictly positive
NNLS solution), not by `Pi`. The same polytope for the free Loewner data `(u, v)` is unbounded (LP status "unbounded"
along `u_0`).

Reading. **Given the pole, the archimedean place and the lattice `{log n}`, Weil positivity of the `x = 13` window
determines the eleven weights, and so the von Mangoldt pattern up to 12, to `1e-3` or better once `N >= 20`.** The
mechanism is the near-singularity of the true form: 16 eigenvalues below `1e-6` against 11 unknowns, so each near-zero
eigenvalue costs one linear condition (Section 2, item 4). In the free Loewner coordinates the same positivity leaves an
unbounded set, because a generic `2N+1`-dimensional perturbation can always add a positive form. This is a statement
about the converse direction (positivity and the lattice give the primes), not about RH. It uses that the window form is
positive, which lane A1 certifies at `x = 13`.

## 5. B2.2: the calibration cases and the protocol mapping

Window form (shard 08g, `def:window-extension-set`): the Toeplitz matrix `T_K = (nu_{|j-k|})`, `j, k = 0..K`, of the
rescaled traces `nu_k = q^{-k/2} (Tr B^k - trivial_k)`, where `B` is the Hashimoto matrix; for a permutation,
`nu_k = Tr P^k`. For a `(q+1)`-regular graph (Ihara–Bass), `trivial_k = q^k + 1 + (E - V)(1 + (-1)^k)`. The `q^k` term is
the analogue of the pole (the Ihara zeta has its pole at `u = 1/q`); the rest is the analogue of the archimedean or
trivial terms; and `N_0 = 2E` is the dimension. All of these are fixed by `(q, V)`: they are the kinematic data. The
prime data are the prime-cycle counts `pi(l)`, through `Tr B^k = sum_{l | k} l pi(l)`.

Cases:

1. **The permutation `(1 2)(3 4 5)`** (shard 08g): 4 distinct atoms, no pole, kinematic form `5 I`.
2. **The Petersen graph** (shard 08g; Ramanujan, `q = 2`): 4 distinct atoms, girth 5, critical window 4. Every entry of
   `T_K`, `K <= 4`, is kinematic: **its window form contains no prime datum at all** (`pi(l) = 0` for `l <= 4`;
   `pi(5) = 24` and `pi(6) = 20` count 12 pentagons and 10 hexagons in two orientations).
3. **G40**: a random cubic graph on 40 vertices (configuration model, seed 20260924, first simple draw). It is
   certified Ramanujan by exact arithmetic: the integer characteristic polynomial, divided by `(x - 3)`, has all 39
   roots isolated in `(-2 sqrt 2, 2 sqrt 2)`, and they are simple. So `R = 78` distinct atoms lie on the circle, and
   the critical window is `K = 78`. Girth 4; `pi(l) = 6, 6, 6, 16, 32, 68, ...` for `l = 4, 5, 6, ...`, and
   `pi(l) q^{-l} = 0.109, 0.050, 0.025, 0.0128` at `l = 10, 20, 40, 78` (prime cycle theorem `pi(l) ~ q^l / l`).
   `ihz/` was not needed: its named graphs have few distinct eigenvalues, and G40 gives a long curve.

The shard's numbers are reproduced first: permutation radii 5, 4.2, 2.0571 and Petersen count-unit radii 35.5, 40.6, 49.4.

Protocol mapping (a finding against the brief, Section 10):

- The graph's `K` is the window and the data cutoff at the same time, since the window of order `K` sees exactly the
  cycles of length `<= K`. So the **axis-K protocol is the analogue of lane A1's CCM axis-x protocol**, not of its
  axis N.
- There is no graph analogue of the resolution `N`: the graph's window form is exact and finite-dimensional.
- The **data axis** (fixed `K`, cycle lengths `<= P` added) is the analogue of lane A1's fixed-L protocol.
- For Toeplitz data the disc of `prop:extension-disc` already is the structured section (lane A1's Lemma A1.1'), so
  "disc" needs no modification here.
- `Delta I_K = log nu_0 - log e_{K+1}` (lane A1's unstructured information) and
  `Delta I^s_K = log e_K - log e_{K+1} = -log(1 - tau_K^2)` (the gain of the truth over the disc centre, a Verblunsky
  coefficient).

## 6. B2.2, axis K (`rtp1_calibration.txt` section 3)

G40, `K = 0..77`. All `T_K` are certified positive definite, and `lambda_min(T_78)` is a certified ball containing 0.

| K | lambda_min(T_K) | log det | e_K (radius) | tau_K | Delta I_K | Delta I^s_K | 1 - overlap |
|---|---|---|---|---|---|---|---|
| 0 | 78 | 4.36 | 78 | -0.027 | 0.001 | 0.001 | 0.75 |
| 12 | 6.85 | 54.2 | 54.5 | -0.119 | 0.37 | 0.014 | 0.19 |
| 24 | 0.163 | 99.6 | 33.8 | -0.051 | 0.84 | 0.003 | 0.050 |
| 36 | 9.77e-4 | 136.0 | 11.1 | -0.133 | 1.97 | 0.018 | 0.016 |
| 48 | 6.63e-7 | 155.9 | 1.74 | -0.074 | 3.81 | 0.006 | 5.9e-3 |
| 54 | 1.81e-8 | 156.5 | 0.78 | -0.008 | 4.61 | 0.000 | 3.7e-3 |
| 60 | 3.04e-10 | 151.2 | 0.23 | 0.004 | 5.84 | 0.000 | 1.9e-3 |
| 66 | 6.91e-13 | 134.1 | 9.6e-3 | -0.110 | 9.02 | 0.012 | 1.1e-3 |
| 72 | 6.55e-17 | 93.2 | 5.9e-5 | -0.083 | 14.1 | 0.007 | 8.1e-4 |
| 73 | 3.14e-17 | 83.5 | 5.8e-5 | -0.932 | 16.1 | 2.02 | 3.8e-5 |
| 75 | 1.06e-18 | 59.9 | 7.7e-6 | -0.988 | 19.9 | 3.75 | 1.0e-5 |
| 76 | 1.32e-20 | 44.4 | 1.8e-7 | 0.049 | 19.9 | 0.002 | 7.5e-4 |
| 77 | 7.00e-21 | 28.9 | 1.8e-7 | **-1** | inf | inf | 0 |
| 78 | **0** (certified ball) | | | | | | |

Learning rates of `lambda_min`, in decimal digits per unit of `K`: 0.13 (`K = 6..30`), 0.25 (30..54), 0.47 (54..72),
0.79 (72..77). In `x_eq = q^K` this is a power law, `lambda_min ~ x_eq^{-p}` with `p = 0.44, 0.83, 1.56, 2.64`.

Other features of the axis-K run:
- The truth is interior to its disc for every `K < 77`. The mean `|tau|` is 0.19 for `K < 39` and 0.37 for
  `39 <= K < 77`, and the maximum is 0.988 (at `K = 75`). At `K = 77` the truth is on the boundary (`|tau| = 1` to
  `1e-60`; `prop:extension-disc`(iv)).
- The radius shrinks from 78 to `1.8e-7`, and then to 0.
- `Delta I_K` grows slowly (0.0 to 0.3 nats for `K < 10`, 14 to 20 nats near the end).
- `Delta I^s_K` is small except at alternate steps near the end (2.0 and 3.7 nats at `K = 73, 75`), where even and odd
  eigenvectors take turns.
- The minimal eigenvector converges in shape: `1 - overlap` is 0.19 at `K = 12` and `7.5e-4` at `K = 76` (the
  overlap is maximised over shifts).

Permutation (`K = 0..3`) and Petersen (`K = 0..3`): definite, singular at `K = 4`, truth on the boundary at `K = 3`. The
permutation's radii are 5, 5, 4.2, 2.057. The Petersen graph collapses to a point using kinematic data only.

## 7. B2.2, data axis and Rayleigh decomposition (sections 4 and 5)

The G40 data axis at fixed window, `K = 77` and `K = 38` (`P` = longest cycle length included; `P < 4` is the kinematic
form alone):

| P (K = 77) | lambda_min | #neg | log\|det\| | overlap with final |
|---|---|---|---|---|
| 0 (kinematic) | -7.78e11 | 1 | 372.7 | 6.0e-4 |
| 10 | -7.78e11 | 7 | 378.8 | 6.0e-4 |
| 20 | -7.78e11 | 37 | 573.4 | 6.0e-4 |
| 40 | -7.78e11 | 37 | 1068.8 | 5.9e-4 |
| 60 | -7.77e11 | 17 | 869.3 | 2.7e-4 |
| 70 | -7.59e11 | 7 | 489.5 | 1.6e-5 |
| 76 | -3.89e11 | 1 | 113.3 | 1.9e-7 |
| 77 (all) | +7.00e-21 | 0 | 28.9 | 1 |

These rows show:
- Every partial form with `P < K` is indefinite, and the negative counts are certified.
- The kinematic form has exactly one negative eigenvalue, of size about `q^{K/2}`: this is the pole direction.
- The negative count rises to 39 and then falls by exactly one per added cycle length over the last 39 lengths.
- The same holds at `K = 38`: `lambda_min = -5.2e5` with only length 38 missing.
- The permutation behaves differently. It has no pole, and every partial form is positive definite (`5 I`, then
  `lambda_min = 3`, then 1), because each partial datum is the moment sequence of a positive measure.

Rayleigh decomposition of `lambda_min` at the final window (`K = 77`):

| term | contribution |
|---|---|
| dimension `N_0 = 2E` | +120.0 |
| pole `q^k` | -2.777e5 |
| trivial terms | -120.5 |
| each cycle length | positive, from `1.4e-2` to `1.2e4` (largest at length 45) |
| sum = `lambda_min` | `7.0e-21` (the parts sum to it to `1e-60` relative) |

**`lambda_min` is a cancellation residual**, as in zeta. Every cycle term exceeds it by at least `2e18`; at `K = 38` the
factor is `2.5e4`. The signs are opposite to zeta's, because zeta's primes enter `Psi` with a minus sign and the graph's
cycle counts with a plus sign.

## 8. B2.2 comparison step (graph spectrum used here only; section 6)

The kernel root of the minimal eigenvector nearest the lowest atom `theta_1 = 0.37315` is the analogue of `z_1`. The
roots lie on the unit circle to `1e-100` (Carathéodory–Fejér).

| K | 12 | 24 | 36 | 48 | 60 | 72 | 77 |
|---|---|---|---|---|---|---|---|
| lambda_min | 6.85 | 0.163 | 9.8e-4 | 6.6e-7 | 3.0e-10 | 6.6e-17 | 7.0e-21 |
| \|theta - theta_1\| | 0.21 | 0.026 | 1.3e-3 | 4.7e-6 | 9.9e-9 | 6.1e-15 | 9.1e-19 |
| err / lambda_min | 0.031 | 0.16 | 1.3 | 7.1 | 32.5 | 93.6 | 129 |

At `K = R = 78` the kernel polynomial of the singular `T_78` has the true atoms as roots, to `2.4e-162`. The error
tracks `lambda_min` with a slowly growing ratio: roughly `err ∝ lambda_min^{0.88}` over `K = 36..77`. In zeta the ratio
is constant at about `1e4` (lane A1).

## 9. B2.1 on the calibration case, and the like-for-like scale (section 6b)

For G40, fix the kinematic data (`nu_0 = 78` and the pole and trivial parts of `nu_k`) and let the prime data be
`x_k = q^{-k/2} N_k`. Then `P^graph_K = M_K - nu^kin`, where `M_K` is the moment space of positive measures of mass
`nu_0` on the circle (Carathéodory–Toeplitz). It has dimension `K` and is **bounded**: every `2 x 2` minor gives
`|nu_k| <= nu_0`. Its **maximum-determinant element exists**. By Hadamard it is `nu = (nu_0, 0, .., 0)`, i.e.
`N_k = trivial_k`: **the graph prime number theorem**. At `K = 77` this prediction has relative distance `4.7e-10` from
the truth (Hilbert-Schmidt norm of the Toeplitz prime part), and the relative diameter of the whole set is at most
`1.1e-8`. At `K = 38` the figures are `1.7e-4` and `4.1e-3`.

This is a structural difference from zeta. The graph's lag 0 carries no prime datum; zeta's Loewner diagonal `a_n` does.
That is why zeta's `P_N` is unbounded and has no maximum-determinant element. The graph's tight relative posterior,
however, is the square-root law at `x_eq = 2^77 ≈ 1.5e23`. At comparable windows the graph's PNT prediction is no better
than zeta's:

| K | 4 | 5 | 6 | 7 | 8 | 10 | 12 | 16 | 20 | 30 | 38 | 60 | 77 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| x_eq = 2^K | 16 | 32 | 64 | 128 | 256 | 1024 | 4096 | 6.6e4 | 1.0e6 | 1.1e9 | 2.7e11 | 1.2e18 | 1.5e23 |
| rho(K) | 6.72 | 4.70 | 3.95 | 3.11 | 2.22 | 1.10 | 0.63 | 0.19 | 0.055 | 2.3e-3 | 1.7e-4 | 1.3e-7 | 4.7e-10 |

Compare zeta's `rho = 0.96 .. 0.80` at `x = 13..100` (`N = 40`). In absolute terms the graph's positive set is never
small: it is the moment space, of diameter `O(nu_0)`. Zeta's lattice-restricted weights, by contrast, are pinned in
absolute terms (Section 4).

## 10. The control signature, and how it differs from zeta

The calibration signature (G40, Petersen, permutation; RH is a theorem for each):

1. The window and the data are one axis. `lambda_min(T_K)` falls smoothly, as a power law in `x_eq = q^K` that steepens
   (exponent 0.44 to 2.6), and reaches **exactly 0 at the finite critical window `K = R`**, a count of atoms fixed by `V`.
   The posterior collapses to a point.
2. The next trace is interior to its disc until `K = R - 1`, and on the boundary there. The disc radius falls from
   `nu_0` to `1.8e-7`, and then to 0.
3. At fixed window every partial form is indefinite until the last cycle length enters, at scale `q^{K/2}`: the pole is
   cancelled only by the full cycle count. A permutation, which has no pole, has positive partial forms throughout.
4. `lambda_min` is a cancellation residual (pole `-2.8e5` against cycle terms, each more than `1e18 lambda_min`).
5. A graph whose girth exceeds its critical window (Petersen) needs no prime datum: kinematics give its exact form.

Against zeta (lane A1):

- **Collapse versus floor.** Zeta's `eps_N(x) > 0` at every `x` and falls like `e^{-4 pi x}`: exponentially in `x`, and
  doubly exponentially in the window length `L`. The graph's falls like a power of `x_eq` and then hits 0. **The
  calibration case does not show an `e^{-c x}` law.** A finite spectrum with RH true gives a power law and a finite
  collapse.
- **Saturation.** Zeta has a resolution axis with saturation at `N_sat ≈ 1.7 x log x`. The graph has none; its
  Weyl-count scale is the collapse point `K = R`.
- **Next datum.** Zeta's admissible interval stays O(1) above `N_sat` with the truth interior, and has the truth on the
  boundary below `N_sat`. The graph's disc shrinks steadily with the truth interior until `K = R - 1`.
- **Indefinite until the last datum** is shared, but the size differs by 18 orders of magnitude: `-5.7e-7` for zeta
  against `-3.9e11` for the graph. In zeta the prime power at the window edge enters with weight `1 - log k / L -> 0`,
  because the continuous autocorrelation of a window function vanishes at the edge. The Toeplitz corner carries full
  weight. So zeta's "barely indefinite" is a continuous-window edge effect, not arithmetic.
- **Kinematic form.** Zeta's is indefinite by O(1) in 1 to 3 directions; the graph's has one negative direction of size
  `q^{K/2}`.
- **Cancellation residual.** Shared, so it does not by itself distinguish zeta's floor.

## 11. Findings against the brief

1. **"The maximum-determinant element of the window cone consistent with the pole and archimedean data" (B2.1) does not
   exist, even in the corrected formulation.** With the prime data free in the Loewner coordinates, `P_N` is unbounded,
   its recession cone is the whole positive cone of `K_N`, and `sup log det = +infinity`. The ball-relaxed
   maximum-determinant element (radius = the truth's norm) is farther from the truth than zero (relative distance 1.34).
   The minimal-norm element exists. It captures 8% of the true prime data at `N = 20` and 3% at `N = 60`, but it
   reproduces the compression to the negative directions of `H0` to 7%. MaxEnt in the Loewner coordinates carries no
   information about the primes beyond the negative directions of `H0`.
2. **"The dimension of the admissible cone before any prime is seen" is trivial.** The kinematic space is `2N+1`
   dimensional and is exactly zst's `(a even, b odd)` data. The positive cone has non-empty interior (the identity), so
   its span is everything. The Loewner condition implies reality, so the brief's three conditions are not independent.
   The condition is linear only because `eta = sum V_n` is fixed; "rank-two commutator" with a free `eta` is not a linear
   condition.
3. **The Loewner coordinates hide the lattice.** Restricted to weights on the known positions `log n`, the same
   positivity pins the von Mangoldt weights up to 12 to `1e-3` or better at `x = 13`, including the zeros at 6, 10 and
   12 (Section 4). The brief's question "how far is the kinematic prediction from the true form" has opposite answers in
   the two coordinate systems. The lattice is arithmetic input, but it is the zeta analogue of the integer lags that the
   graph's Toeplitz structure builds in.
4. **"Ramanujan graph or genus-one curve ... with `scripts/weil_window_extension.py` and `ihz/`" (B2.2).** Both examples
   in `weil_window_extension.py` have 4 distinct atoms, so their learning curves are four steps long. The Petersen graph
   has **no prime datum in its window at all** (girth 5 > critical window 4). It is a pure-kinematics case, not a
   calibration of learning from primes. I added a certified-Ramanujan random cubic graph with 78 atoms. The genus-one
   curve (2 atoms) would be shorter still and was not run.
5. **"Along K (resolution)" (orchestrator's B2.2 protocol) is a misnomer for graphs.** `K` is the window and the data
   cutoff at once, so the graph's K axis is the analogue of lane A1's CCM axis-x protocol. There is no analogue of A1's
   axis N, and no analogue of the saturation `N_sat`, other than the collapse point `K = R`.
6. **"The `e^{-4 pi x}` floor as a cancellation residual" does not single out zeta.** The graph's `lambda_min` is also a
   cancellation residual (pole against cycles, each term more than `1e18 lambda_min`). What distinguishes zeta is the
   rate (exponential in `x` against a power law in `x_eq`) and the absence of a collapse.
7. **"Indefinite until the last prime power at fixed window" (lane A1) is shared, and its smallness is not arithmetic.**
   Zeta's last-missing `lambda_min = -5.7e-7` is small because the window weight vanishes at the edge. The graph's
   analogue is `-3.9e11`.
8. **Question 3 of the round.** The calibration case does not reproduce an exponential learning law, so "any discrete
   spectrum on the critical line plus kinematics" does not by itself produce `e^{-4 pi x}`. This supports lane A1's
   verdict (specific to the arithmetic). Caveat: the graph's Weyl law is finite (`R` atoms), unlike zeta's, so the
   calibration cannot separate "a spectrum with zeta's Weyl law" from "these zeros". A family with growing `V` would be
   needed for that.
9. **Shard 08g `obs:rescaling-and-zeta`(iii) ("the mean of the higher traces is the pole").** Used as a predictor of
   the prime data inside the window, the pole mean is not admissible and captures 22% at `x = 13`, `N = 20`. Its
   relative error falls only slowly with `x` at fixed `N` (0.96 to 0.69 for `x = 13..200`) and grows at the saturation
   resolution. The graph's PNT is worse at comparable `x_eq` (`rho > 1` for `K <= 10`). The shard's argument concerns
   traces beyond the window and is not contradicted, but "the pole predicts the primes" holds only in the square-root
   sense and only at large `x`.
10. **Precision.** The convex problems ran in double (duality gaps about `4e-9`). The truth sits `1e-39` from the
    boundary, so every statement about the truth's position was made at 100 digits. The lattice box needed a 100-digit
    dual certificate, because the double-precision LP is unreliable below its `1e-7` tolerance.

## 12. Reproduction

    python3 scripts/rtp1_commutant.py > outputs/rtp1_commutant.txt 2>&1      # about 2.5 min
    python3 scripts/rtp1_calibration.py > outputs/rtp1_calibration.txt 2>&1  # about 2.7 min
    # each run twice; cmp confirmed byte identity for both outputs

`rtp1_commutant.py` needs `zst/build/libzst.a` (built by `make -C zst` if missing), `cc` and FLINT. Both scripts need
python-flint 0.9, mpmath, numpy and scipy.
