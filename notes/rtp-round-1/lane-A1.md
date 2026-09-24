# Lane A1: the dilation channel's contraction rate (RTP-1, Step 1)

Author: `claude:opus`, 2026-09-24. Brief: `notes/rtp-round-1/brief.md` (Lane A1; author `claude:fable-5.1`).
Status: numerics lane, unreviewed (REFUTE lane R pending). Nothing here is registered as a claim.

Code: `zst/tools/rtp1_a1.c` (driver on `libzst`, unchanged: `zst_riemann_ab`, `zst_even_block`,
`zst_odd_block`, `zst_eigmin`, `zst_certify_even_simple`, `zst_inertia_neg`, `zst_secular_roots`,
`zst_zeta_zeros`), `zst/tools/rtp1_a1_run.sh` (regenerates every output), `zst/tools/rtp1_a1_summary.py`
(derived numbers of this note from the outputs). Build rule `build/rtp1_a1` added to `zst/Makefile`
(not part of `all`); `make check` passes unchanged.
Outputs (byte-reproducible, each run twice and compared with `cmp`):
`outputs/rtp1_a1_axisN_x13.txt`, `..._axisN_x25.txt`, `..._axisN_x50.txt` (A1.2 and A1.4),
`outputs/rtp1_a1_axisx_ccm_N60.txt`, `..._axisx_ccm_N120.txt`, `..._axisx_fixedL_N60.txt` (A1.3 and A1.4).

Game rules. RH is not assumed. Every number that enters a form comes from `zst_riemann_ab` (pole, primes,
archimedean place). Zeros of zeta appear only in the blocks headed `COMPARISON STEP` of the outputs and in
Section 5 below. Everything in the tables is a ball-arithmetic result (arb), printed only to digits that the
ball certifies (the printer shows the full ball otherwise), except the columns and numbers explicitly marked
*floating* (derived slopes and fits in `rtp1_a1_summary.py`, and the QR spectrum used only to place a shift).

## 0. Answers in brief

- **A1.1.** The ellipsoid lemma holds as stated (proof in Section 1). But the unconstrained MaxEnt
  prediction `c = 0` is **not a Loewner column**: the window form's new column is fixed by the one new datum
  `b_{N+1}` (given `a_{N+1}`). The exact analogue of `prop:extension-disc` is therefore the section of the
  ellipsoid by that affine line: an **interval** of admissible `b_{N+1}` (Lemma A1.1'), whose centre is the
  structured MaxEnt prediction. Both are computed.
- **A1.2 (axis N).** Below a saturation point `Delta I_N` is tens of nats per step (peaks of 44, 76 and 133
  nats at `x = 13, 25, 50`). Above it, `Delta I_N` is 0.05 to 0.4 nats per step. The saturation point grows like `x log x`, not like `x`: `N_sat ≈ 1.7 x log x` (argmin of
  `log det`: `N = 56, 134, 352` at `x = 13, 25, 50`, i.e. `4.3x, 5.4x, 7.0x`; the benchmark's `7.5x` is
  matched only near `x = 50`). Below saturation the true `b_{N+1}` sits **on the boundary** of its admissible
  interval (`|tau| ≈ 1`), the analogue of `prop:extension-disc`(iv). Above it the truth is interior and the
  interval half-width is 0.5 to 3.7 at every `x`.
- **A1.3 (axis x).** With `N` held fixed, `eps_N(x)` and `|z_1 - gamma_1|` fall at 5.0 to 5.3 decimal digits per
  unit of `x` (the `e^{-4 pi x}` law is 5.46) **only while `N >= N_sat(x)`**. After that they slow down
  (`N = 60`: 4.1 digits per unit of `x` at `x = 16`, 0.5 to 0.8 near `x = 50`). The eigenvector converges
  in shape (`1 - overlap = 0.012` at `x = 13`, `1.6e-4` at `x = 23`, `N = 120`). In the clean fixed-window
  protocol, the partial-information form is **indefinite until the very last prime power enters** (3 to 16
  negative even eigenvalues; at `L = log 50` with every prime power except 49: `lambda_min = -5.66e-7` and
  eigenvector overlap `2.7e-48`). It becomes positive definite (`eps = 1.75e-116`) only when `k = 49`
  enters.
- **A1.4.** `|z_1 - gamma_1| / eps_N` is 7.0e3 (`x = 13`), 9.3e3 (`x = 25`), 1.08e4 (`x = 50`) at saturated `N`,
  and the two quantities have the same slope in `x` at every fixed `N` (to 0.2 digits per unit of `x`, and to
  0.02 for `x >= 13`). The first-zero error is
  proportional to `eps_N`.
- **Question 3 of the round.** In the sense of this lane, the `e^{-4 pi x}` convergence is **not** explained
  by the kinematic envelope. It is specific to the arithmetic (Section 6). The Schur envelope of the next
  datum does not shrink at that rate: at saturated `N` it does not shrink at all, and at fixed `N` it shrinks
  at about 0.7 digits per unit of `x`. The kinematic data alone (pole plus archimedean, same window, same
  Loewner structure) give an indefinite form with `lambda_min` from `-0.07` to `-1.37`. `eps` is the residual
  of an O(1) cancellation to which every prime power `< x` contributes at least `10^{34} eps` (at `x = 50`). The kinematics
  set where `N` saturates (a Weyl-count scale, `~ x log x`); the arithmetic sets the floor.

## 1. A1.1: the ellipsoid extension lemma, and its Loewner section

**Lemma A1.1 (ellipsoid extension).** Let `G` be a positive-definite Hermitian `n x n` matrix, `C` an
`n x m` matrix, `D` Hermitian `m x m`, and `B = [[G, C], [C^*, D]]`; write `S = D - C^* G^{-1} C`.

1. `B >= 0` iff `S >= 0` (and `B > 0` iff `S > 0`). For `m = 1` (`C = c`, `D = d`) the admissible set is
   `{(c, d) : d - c^* G^{-1} c >= 0}`. For fixed `d > 0` it is the ellipsoid `c^* G^{-1} c <= d`, centred at 0
   with semi-axes `sqrt(d mu_i(G))`.
2. `det B = det G det S`.
3. For fixed `D > 0`, `det B <= det G det D`, with equality iff `C = 0`: the maximum-determinant completion
   with known diagonal block is `C = 0`.
4. `Delta I := log det D - log det S = log det G + log det D - log det B >= 0`, with equality iff `C = 0`. It equals
   `2 I(X; Y)` for a real centred Gaussian `(X, Y)` with covariance `B` (the mutual information between the old
   and the new coordinates). It is additive over an orthogonal splitting of the new block (here: even and odd).
5. In the unpivoted `LDL^*` factorisation of a positive-definite matrix, the `k`-th pivot is the Schur
   complement of the `k`-th bordering, `D_k = det B_k / det B_{k-1}`. One factorisation of the largest window
   therefore gives every `Delta I_N`.

*Proof.* The congruence `[[I, 0], [-C^* G^{-1}, I]] B [[I, -G^{-1} C], [0, I]] = diag(G, S)` gives (1) and
(2) (Sylvester's law of inertia; determinant of a product). For (3): if `S >= 0` write
`S = D^{1/2} (I - P) D^{1/2}` with `P = D^{-1/2} C^* G^{-1} C D^{-1/2}`. Then `0 <= P <= I`,
`det S = det D prod_i (1 - p_i) <= det D`, and equality holds iff every eigenvalue `p_i` of `P` is 0, iff
`P = 0`, iff `G^{-1/2} C = 0`, iff `C = 0`. (4) is (2) combined with (3). The Gaussian identity is
`I(X; Y) = (1/2) log(det G det D / det B)` for real Gaussians. Additivity holds because `S` is block diagonal
when `C` and `D` split. (5) is (2) applied to each leading block. QED.

*Relation to `prop:extension-disc`.* In the Toeplitz case the new column `u(x) = x-bar e_0 + w` has a single
free complex entry, and the remaining entries `w` are old data (shift invariance). The admissible set is the
section of the ellipsoid of (1) by that complex affine line, which is the disc. Its centre, the Levinson
predictor, is the maximum-determinant point on the line, not `c = 0`. Items (1) to (3) are the unconstrained
version of (i) and (ii); the disc is the constrained one.

**Lemma A1.1' (Loewner section: the admissible interval of the next datum).** In the window form, the
bordering `|n| <= N -> |n| <= N+1` adds one even basis vector `(V_j + V_{-j})/sqrt2` and one odd basis vector
`(V_j - V_{-j})/sqrt2`, with `j = N+1` (`zst/src/blocks.c`, `plan.md` 1.3). Their columns and diagonals are
affine in the one new odd datum `b = b_j`:

    even:  c_e(b) = u_e + b w_e,  d_e(b) = a_j + b/j,  w_e = (sqrt2/j, (1/(i+j) - 1/(i-j))_{i=1..N}),
    odd:   c_o(b) = u_o + b w_o,  d_o(b) = a_j - b/j,  w_o = ((-1/(i-j) - 1/(i+j))_{i=1..N}),

where `u_e` and `u_o` depend only on `b_1..b_N`. Given `a_j`, and writing `beta = b - b_true`, each Schur
complement is a concave quadratic,
`s(beta) = s_true + l beta - C beta^2` with `C = w^* G^{-1} w > 0` and `l = +-1/j - 2 w^* G^{-1} c(b_true)`.
Hence:

1. The admissible `b` of each block form the interval `beta* +- r`, where `beta* = l/(2C)`,
   `r = sqrt(s*/C)` and `s* = s_true + l^2/(4C)`. The joint admissible set is the intersection of the two
   intervals.
2. The maximum-determinant `b` of each block is the centre of its interval. The joint maximum-determinant
   point maximises `s_e s_o` on the intersection; `log s_e + log s_o` is concave there, so it is unique.
3. The truth sits at `tau = -beta*/r`, and `|tau| = sqrt(1 - s_true/s*)`. So the truth is on the boundary iff the
   bordered block is singular, the analogue of `prop:extension-disc`(iii) and (iv).
4. `Delta I^s := log(s_e(beta_ME) s_o(beta_ME)) - log(s_e(0) s_o(0)) >= 0` is the log-determinant gain of the
   truth over the structured MaxEnt prediction.
5. The unconstrained MaxEnt column `c = 0` is not a Loewner column unless `b_1 = ... = b_N = 0`. The 0-th
   entry `sqrt2 b/j` of `c_e` forces `b = 0`, and then `c_e = u_e = 0` forces `b_i (1/(i-j) + 1/(i+j)) = 0`
   for every `i`.

*Proof.* Substitute `c(b)` and `d(b)` into `s = d - c^* G^{-1} c` (Lemma A1.1(1)) and expand in `beta`. The
leading coefficient is `-w^* G^{-1} w < 0` because `w != 0` (`w_{e,0} = sqrt2/j`, and `w_{o,i} != 0`). Items
(1) to (4) are then elementary facts about a concave quadratic, and (3) uses `s(beta) = s* - C (beta - beta*)^2`
at `beta = 0`. QED.

The driver computes `C` and `l` from one forward substitution with the ball `L` factor per step. It reads
`y_c = L^{-1} c(b_true)` off row `j` of the factor, and it checks in balls that `|tau| <= 1` for both blocks,
that the joint MaxEnt point is admissible, and that `Delta I >= 0` and `Delta I^s >= 0` (the check counts are
in the outputs; 0 failed). The joint MaxEnt point is found by bisection on midpoints (200 steps), so it is a
floating prediction; `Delta I^s` is a ball evaluated at that point, and it is a certified lower bound for the
exact structured gain.

## 2. Certification, precision, cost

| item | method | certified |
|---|---|---|
| `(a_n, b_n)` | `zst_riemann_ab` | balls |
| `Delta I_N`, `log det`, `s_e`, `s_o` | ball `arb_mat_ldl` of the even block (modes `0..Nmax+1`) and the odd block | yes: success certifies that every leading block is positive definite (Weil positivity of every window `|n| <= N <= Nmax+1`) |
| structured interval, `tau`, `Delta I^s` | ball forward substitution | yes (MaxEnt point: floating, see above) |
| `eps_N` and eigenvector | `zst_eigmin` (Krawczyk/Rump), then `zst_certify_even_simple` | yes, including simplicity and minimality. For indefinite forms: shifted by `sigma` below `lambda_min` (placed by a floating QR), then the same certificate on `E - sigma` |
| negative-eigenvalue counts | `zst_inertia_neg` (ball `LDL^T`) | yes (`?` would mean inconclusive; none occurred) |
| `log det` check | `arb_mat_det` (preconditioned) against the sum of pivots, at every compared `N <= 200` | agrees (balls overlap) |
| prime terms used in the Rayleigh decomposition and the fixed-window protocol | local closed form (plan.md 1.2) | checked entrywise against `zst_riemann_ab` at the full cutoff (balls overlap) |

Precision. Ball `LDL^T` of these forms loses 2.6, 3.5 and 4.6 times `log2(1/eps)` bits at `x = 13, 25, 50`
(the factor grows with `x` and `N`). The worst relative accuracy of a pivot is 493 of 1000 bits (`x = 13`),
392 of 1800 (`x = 25`) and 247 of 4200 (`x = 50`), as printed in each output. This is far more than the
`~ 2 log2(1/eps) + 200` bits the eigenpair certificate needs (benchmark item 5). So the axis-N runs use 1000,
1800 and 4200 bits for the factorisation, and round the blocks to `cprec` = 700, 1200 and 2400 bits (about
`40x + 200`) for the eigenpair and the comparison. Cost (single thread, FLINT 3.0.1): `x = 50`,
`Nmax = 520`, 4200 bits takes 1.8 min for the factorisation and all borderings, plus 4.6 min for five certified
eigenpairs and root sets. The whole suite takes 12 min of CPU (6.5 min wall with 3 parallel jobs).

Cross-lane consistency (Conventions section of the brief): this lane uses `zst`'s `(a_n, b_n)` directly. Each
axis-N output prints them at `x = 13` for `n = 0..3` to 30 digits, for comparison by lane A2, e.g.
`a_1 = 0.0465118895436779793116060710601`, `b_1 = 0.0457203442394000540357853654912`.

## 3. A1.2: axis N (resolution at fixed window)

**Protocol.** Held fixed: `x = lambda^2`, hence the window `L = log x`, the prime powers `k <= x` and all of
`(a_n, b_n)`, which do not depend on `N`. Varied: the Fourier cutoff `N`. The window matrix on `|n| <= N` is
exactly the leading principal block of the one on `|n| <= N+1`, in both the even and the odd blocks. Row `N`
is the bordering `N -> N+1` (new modes `+-(N+1)`). `Delta I` is in nats. `r_j` is the half-width of the joint
admissible interval of `b_{N+1}` and `tau_j` the truth's position in it (`+-1` = boundary). `Delta I^s` is the
structured gain of Lemma A1.1'(4).

`x = 13` (`rtp1_a1_axisN_x13.txt`, 1000 bits):

| N | Delta I_N | s_e | s_o | log det (\|n\|<=N) | r_j | tau_j | Delta I^s |
|---|---|---|---|---|---|---|---|
| 1 | 20.26 | 1.30e-7 | 4.32e-6 | -21.76 | 2.1e-4 | 1.00 | 13.4 |
| 5 | 39.77 | 1.43e-9 | 1.87e-8 | -166.04 | 7.8e-7 | -0.999 | 10.4 |
| 10 | 44.20 | 3.75e-11 | 2.95e-10 | -376.62 | 9.2e-8 | 1.00 | 16.5 |
| 20 | 35.82 | 1.23e-8 | 3.22e-8 | -780.43 | 5.1e-6 | 1.00 | 14.1 |
| 30 | 18.56 | 2.46e-4 | 5.46e-4 | -1058.84 | 0.097 | -1.00 | 14.9 |
| 40 | 14.96 | 9.56e-4 | 1.93e-3 | -1213.33 | 0.10 | 0.999 | 11.6 |
| 50 | 7.88 | 0.041 | 0.056 | -1282.89 | 0.47 | -0.986 | 6.9 |
| 55 | 4.86 | 0.143 | 0.207 | -1288.14 | 0.50 | 0.946 | 4.2 |
| 60 | 1.92 | 1.15 | 1.32 | -1287.47 | 1.17 | 0.710 | 1.27 |
| 70 | 0.162 | 3.91 | 3.95 | -1274.65 | 1.20 | -0.036 | 0.0018 |
| 100 | 0.229 | 4.40 | 4.41 | -1210.30 | 1.86 | 0.266 | 0.15 |
| 160 | 0.064 | 3.07 | 3.08 | -1057.51 | 2.65 | -0.005 | 2.3e-5 |
| 200 | 0.048 | 3.92 | 3.92 | -947.59 | 2.84 | 0.104 | 0.021 |

`x = 25` (`..._x25.txt`, 1800 bits): `Delta I = 23.5, 53.7, 68.1, 67.1, 69.5, 49.1, 30.6, 16.5, 9.2, 3.3,
1.09, 0.25, 0.29, 0.08` at `N = 1, 5, 10, 20, 40, 60, 80, 100, 120, 130, 150, 160, 200, 260`. `r_j` goes from
`6e-14` (`N = 10`) through `0.12` (`N = 100`) to 0.76 to 3.4 for `N >= 150`. `log det` is minimal at `N = 134`
(`-5328.60`).

`x = 50` (`..._x50.txt`, 4200 bits): `Delta I = 25.7, 89.3, 115.1, 132.9, 116.0, 84.4, 55.2, 26.1, 13.0,
7.0, 2.85, 1.32, 0.73, 0.42, 0.12, 0.37` at `N = 1, 10, 20, 50, 100, 150, 200, 250, 300, 320, 340, 360, 380,
400, 450, 520`. `r_j` goes from `3.4e-25` (`N = 50`) through `0.37` (`N = 300`) to 0.54 to 3.7 for `N >= 367`.
`log det` is minimal at `N = 352` (`-22727.96`).

**Saturation** (`rtp1_a1_summary.py`; floating post-processing of certified midpoints):

| x | N_ld = argmin log det | N_1 (10-row mean of Delta I < 1 from here on) | 7.5x | N_ld/x | N_ld/(x log x) | mean Delta I, last 100 rows | mean \|tau\| below N_ld | mean \|tau\| above N_1 |
|---|---|---|---|---|---|---|---|---|
| 13 | 56 | 58 | 97.5 | 4.31 | 1.68 | 0.12 | 0.929 | 0.149 |
| 25 | 134 | 150 | 187.5 | 5.36 | 1.67 | 0.28 | 0.962 | 0.184 |
| 50 | 352 | 367 | 375 | 7.04 | 1.80 | 0.35 | 0.969 | 0.226 |

Reading. `Delta I_N` saturates at `N_sat ≈ 1.7 x log x` (both criteria give the same scale). Heuristic reading
(not a claim): mode `N` resolves frequencies up to `T = 2 pi N / L`. The window has `T L / 2pi` modes per sign up to
`T`, and the Weyl law gives `(T/2 pi) log(T/2 pi e)` zeros. The surplus of modes over zeros peaks at
`T = 2 pi x` (`N = x log x`) and vanishes at `T = 2 pi e x` (`N = e x log x`). The observed `N_sat` lies
between the two (constant 1.7, against 1 and `e`). Below it each new mode is almost determined by the earlier
ones (tens of nats, truth on the boundary); above it each new mode carries O(0.1) nats and the truth is
interior. The benchmark's `7.5 x` comes from two points (`x = 20, 30`) and a different criterion (zeros usable
to `1e-3`). It agrees with `N_sat` only near `x = 50`.

**Certified `eps_N` and the labelled comparison** (A1.4; `COMPARISON STEP` blocks):

| x | N | eps_N (certified, even-simple CERTIFIED) | \|z_1 - gamma_1\| <= | ratio |
|---|---|---|---|---|
| 13 | 10 / 20 / 40 / 60 | 2.83e-26 / 1.57e-39 / 9.46e-54 / 1.01e-58 | 3.67e-21 / 2.27e-35 / 7.19e-50 / 7.11e-55 | 1.3e5 / 1.5e4 / 7.6e3 / 7.0e3 |
| 13 | 80 / 120 / 200 | 4.48e-59 / 3.48e-59 / 2.85e-59 | 3.13e-55 / 2.44e-55 / 2.00e-55 | 7.0e3 |
| 25 | 25 / 50 / 100 | 6.65e-56 / 1.26e-83 / 3.25e-113 | 2.90e-51 / 1.73e-79 / 3.15e-109 | 4.4e4 / 1.4e4 / 9.7e3 |
| 25 | 150 / 190 / 260 | 6.78e-123 / 3.04e-123 / 2.43e-123 | 6.30e-119 / 2.82e-119 / 2.25e-119 | 9.3e3 |
| 50 | 50 / 100 / 200 | 9.58e-104 / 1.23e-157 / 5.70e-221 | 3.27e-99 / 1.83e-153 / 6.47e-217 | 3.4e4 / 1.5e4 / 1.1e4 |
| 50 | 300 / 360 | 8.45e-251 / 2.27e-257 | 9.18e-247 / 2.45e-253 | 1.1e4 |

`eps_N` saturates at the same `N_sat` as `Delta I_N`. At `N ≈ N_sat` it is within a factor 3.5 (`x = 13`,
`N = 60`) and 2.8 (`x = 25`, `N = 150`) of its value at the largest `N`, and it keeps decreasing beyond: by a
further factor of about 3 up to `2 N_sat`, then by about 20% up to `3.5 N_sat` (`x = 13`, `N = 200`). The saturated values fall at 5.34 decimal digits per unit
of `x` from 13 to 25 and 5.36 from 25 to 50; the first-zero errors fall at 5.33 and 5.36
(`e^{-4 pi x}`: 5.46).

## 4. A1.3: axis x (primes at fixed resolution)

**Protocol CCM** (`rtp1_a1_axisx_ccm_N60.txt`, `..._N120.txt`). Held fixed: the number of modes (`|n| <= N`,
so the matrix size) and the rule "prime powers `<= x` enter". Varied: `x` through the prime powers
`2, 3, 4, 5, 7, ...`, and with it the window `L = log x`. Every `(a_n, b_n)` changes between knots, and the
basis `V_n` is rescaled to the new window. **Not** held fixed: `L`, the pole and archimedean terms, and
the weights `(1 - log k/L)` and phases `2 pi n log k / L` of the prime powers already present. At `x = k` the new
prime power `k` enters with weight exactly 0 (its `a`-weight `1 - log k/L` and its `b`-phase `sin 2 pi n`
vanish; the balls show `[+/- 1e-209]` and smaller), so the form is continuous in `x`. Two overlaps are
printed: `overlap_c` of the unit coefficient vectors (the window rescaled to unit length) and `overlap_f`, the
intrinsic `L^2(R_+^x, d*u)` overlap of the unit eigenfunctions on centred windows.

`N = 120`, 1800 bits (all `eps` certified, all even-simple; `neg` = 0 throughout):

| x | #pp | eps_N(x) | log det (even) | 1 - overlap_c | 1 - overlap_f | Delta I_N | r_j | \|z_1 - gamma_1\| <= (COMPARISON) |
|---|---|---|---|---|---|---|---|---|
| 2 | 1 | 1.330e-3 | 161.12 | 0.307 | 0.024 | 2.8e-4 | 3.98 | 0.213 |
| 3 | 2 | 5.55e-8 | 129.28 | 0.189 | 6.0e-3 | 8.6e-3 | 3.62 | 4.64e-5 |
| 5 | 4 | 9.75e-18 | 51.44 | 0.094 | 1.4e-3 | 0.016 | 3.11 | 2.56e-14 |
| 7 | 5 | 7.67e-28 | -58.97 | 0.054 | 5.4e-4 | 0.078 | 2.81 | 3.20e-24 |
| 9 | 7 | 2.95e-38 | -207.04 | 0.032 | 2.5e-4 | 0.046 | 2.68 | 1.58e-34 |
| 11 | 8 | 1.12e-48 | -391.63 | 0.020 | 1.3e-4 | 0.066 | 2.50 | 7.03e-45 |
| 13 | 9 | 3.48e-59 | -615.02 | 0.012 | 6.7e-5 | 0.35 | 2.68 | 2.44e-55 |
| 16 | 10 | 3.74e-75 | -1022.91 | 5.3e-3 | 2.6e-5 | 0.18 | 1.77 | 2.93e-71 |
| 17 | 11 | 2.10e-80 | -1176.96 | 3.9e-3 | 1.9e-5 | 0.19 | 2.00 | 1.68e-76 |
| 19 | 12 | 5.77e-91 | -1515.07 | 1.9e-3 | 8.9e-6 | 0.34 | 1.63 | 4.87e-87 |
| 23 | 13 | 7.84e-111 | -2291.97 | 1.6e-4 | 8.8e-7 | 2.93 | 0.65 | 7.12e-107 |
| 25 | 14 | 5.26e-119 | -2703.96 | 0 | 0 | 9.20 | 0.26 | 4.95e-115 |

`N = 60`, 2700 bits, to `x = 50`: `eps_N(x)` = `1.01e-58` (13), `6.99e-71` (16), `1.08e-91` (25),
`4.82e-100` (31), `2.47e-106` (37), `2.14e-114` (47), `1.75e-116` (50). `Delta I_N` = 1.9 (13), 4.8 (16),
49 (25), 93 (37), 131 (50). `r_j` = 1.17 (13), 0.18 (16), `4.6e-8` (25), `8.3e-17` (37), `5.3e-25` (50), with
`tau_j = +-1.00` from `x = 17` on. `1 - overlap_c` = 0.033 (13), 0.0067 (25), `4.0e-6` (49). `|z_1 - gamma_1|` =
`7.11e-55` (13), `1.28e-87` (25), `4.40e-112` (50).

Slopes `d log10(.)/dx` between knots (floating, `rtp1_a1_summary.py`), for `eps` and `|z_1 - gamma_1|`:

| N | x = 5..13 | x = 16 | x = 19 | x = 25 | x = 37 | x = 50 |
|---|---|---|---|---|---|---|
| 60 | -4.9 to -5.2 / -4.7 to -5.2 | -4.05 / -4.03 | -2.74 / -2.72 | -1.80 / -1.78 | -1.03 / -1.02 | -0.51 / -0.50 |
| 120 | -4.9 to -5.3 / -4.7 to -5.2 | -5.32 / -5.31 | -5.28 / -5.27 | -4.09 / -4.08 | | |

So along the prime axis the learning rate is the `e^{-4 pi x}` law (5.0 to 5.3 digits per unit of `x`) as long as
`N >= N_sat(x) ≈ 1.7 x log x` (`N = 60`: to `x ≈ 13`; `N = 120`: to `x ≈ 22`). After that it is resolution
limited. The first-zero error follows `eps` step for step.

**Control (no arithmetic)**, CCM mode, same windows and `N`: pole plus archimedean only (prime cutoff 1),
certified. The number of negative even eigenvalues is 0 at `x = 2` (no prime power inside the window: the
form *is* the CCM form there), 1 for `x = 3..8`, 2 for `x = 9..23` and 3 for `x >= 25`. `lambda_min` is
`-0.074` (3), `-0.848` (13), `-1.114` (25) and `-1.373` (50), and agrees between `N = 60` and `N = 120` to 3 digits.

**Protocol fixed-L** (`rtp1_a1_axisx_fixedL_N60.txt`; a partial-information form, *not* the CCM form except in
its last row). Held fixed: `L = log 50`, `|n| <= 60`, and the pole and archimedean terms. Varied: the
prime-power cutoff `X = 1, 2, 3, 4, 5, 7, ..., 49`. Each step adds exactly one closed-form prime-power term
`-W_k`, with its full weight `(1 - log k / L) > 0`.

| X | #pp | lambda_min (certified) | neg (even) | log\|det\| (even) | overlap_c with X = 49 | \|z_1 - gamma_1\| (COMPARISON) |
|---|---|---|---|---|---|---|
| 1 | 0 | -1.373 | 3 | 30.68 | 0.704 | 10.8 |
| 2 | 1 | -1.693 | 4 | 28.13 | 0.715 | 10.8 |
| 5 | 4 | -1.149 | 10 | 21.73 | 0.448 | 11.4 |
| 9 | 7 | -1.122 | 14 | 0.38 | 0.019 | 12.0 |
| 13 | 9 | -1.074 | 16 | -121.52 | 1.2e-5 | 12.4 |
| 19 | 12 | -0.923 | 16 | -553.66 | 7.2e-11 | 12.7 |
| 29 | 16 | -0.628 | 14 | -1343.84 | 4.4e-19 | 13.0 |
| 37 | 19 | -0.432 | 10 | -2423.56 | 3.4e-32 | 13.2 |
| 43 | 21 | -0.0699 | 6 | -3079.66 | 1.2e-43 | 13.3 |
| 47 | 22 | -5.66e-7 | 3 | -3298.43 | 2.7e-48 | 13.3 |
| 49 | 23 | +1.75e-116 | 0 | -3389.26 | 1 | 4.40e-112 |

At fixed window, positivity (the admissible posterior being non-empty) appears only with the **last** prime
power. Before it, the minimal eigenvector of the partial form is unrelated to the final one (overlap
`2.7e-48` at `X = 47`), and the `z_1` read off it is O(1) wrong. In this protocol the learning curve is a
step: all the information about `xi` arrives at once. The CCM protocol avoids the step because it widens the
window only as fast as the primes arrive: the prime power `k` enters at the window edge, with weight 0 at
`x = k`.

**Rayleigh decomposition of `eps`** (printed in every axis-N output for the largest compared `N`, and in the CCM
axis-x outputs for the final `x`). This is `eps = v^T E v` for the certified unit eigenvector `v`, split over
the terms of `Psi = W02 - W_R - sum_k W_k`. At `x = 50`, `N = 360`: pole `+1.5506`, archimedean `-1.4790`,
`k = 2`: `-7.06e-2`, 3: `-9.61e-4`, 4: `-2.85e-6`, 5: `-2.21e-8`, 7: `-1.55e-13`, 11: `-1.07e-24`, 23:
`-1.41e-63`, 31: `-4.34e-95`, 37: `-1.43e-123`, 43: `-6.02e-160`, 47: `-1.22e-194`, 49: `-8.38e-223`; the sum
is `eps = 2.2693e-257` (the balls overlap). Every prime-power contribution is negative and exceeds `eps` by at
least `10^{34}`. The cumulative column (the Rayleigh quotient of the same `v` under the partial form with
prime powers `<= k`) telescopes: after `k` it equals the next contribution to 2 to 10 digits, because the
contributions decay fast. Observation, not a claim: for `k` from 11 to 29, `log10 |R_k|` is roughly
`-2.7 k`, i.e. about `e^{-2 pi k}` (`k = 23`: `-62.85` against `-62.8`), with deviations of several digits;
it steepens near the window edge. The same pattern holds at
`x = 13` (`N = 200`) and `x = 25` (`N = 260`).

## 5. A1.4: side by side (the comparison step; zeros used here only)

At saturated `N` (the columns come from the same outputs; `Delta I` is the mean over the last 100 rows, `r_j` the
range over `N >= N_1`):

| x | N | eps_N | \|z_1 - gamma_1\| <= | err/eps | Delta I (saturated) | r_j (saturated) | Delta I_N at N = 60 |
|---|---|---|---|---|---|---|---|
| 13 | 120 | 3.48e-59 | 2.44e-55 | 7.0e3 | 0.12 | 0.60 to 3.6 | 1.92 |
| 25 | 260 | 2.43e-123 | 2.25e-119 | 9.3e3 | 0.28 | 0.76 to 3.4 | 49.1 |
| 50 | 360 | 2.27e-257 | 2.45e-253 | 1.08e4 | 0.35 | 0.54 to 3.7 | 131.4 |

The first-zero error is proportional to `eps_N`, with a ratio of `~1e4` that drifts slowly upwards with `x`.
It follows `eps_N` at every fixed `N` as well, including unsaturated `N` (Section 4 slopes). It is not
proportional to `Delta I_N` or to the envelope `r_j`: at saturated `N` both are O(0.1) and O(1) at every `x`,
while the error falls by 200 orders of magnitude between `x = 13` and `x = 50`. At `x = 50` the certified bound `2.45e-253`
(`N = 360`, 2400 bits) is 4 orders tighter than the benchmark's `1.54e-249` (`N = 400`, 2100 bits), whose ratio
to its own `eps` (`3.31e-258`) is `4.7e8`. The benchmark's bound was evidently limited by the radius at 2100 bits.

## 6. Question 3: kinematic envelope or arithmetic?

"Kinematic envelope" is read here as in shard 08g ("Not established, and one computation proposed"): the
Schur-complement bound on what the unseen data can do to the window form, given positivity and the structure
of the form. In the dilation channel the structure is the Loewner form with the pole and archimedean terms
known exactly. The data answer the question as follows.

1. **The envelope does not decay at `e^{-4 pi x}`.** The admissible interval of the next datum (Lemma A1.1') has
   half-width 0.5 to 3.7 at saturated `N` for `x = 13, 25, 50`, and `Delta I_N` there is 0.1 to 0.35 nats, not
   decreasing in `x`. At fixed `N = 60` the envelope does shrink with `x` (from 1.17 at `x = 13` to `5.3e-25` at
   `x = 50`, about 0.7 decimal digits per unit of `x`). It shrinks because `N` falls below `N_sat(x)` and the
   next mode becomes redundant, not at the 5.46 digits per unit of `x` of the first zero. The quantity that does
   track the first-zero error is `eps_N` itself (ratio `~1e4` at every `x` and `N`), and `eps_N` is not the envelope.
2. **The kinematic data alone give no small eigenvalue.** With pole plus archimedean terms only, same window,
   same Loewner structure, the form is indefinite (1 to 3 negative even eigenvalues, `lambda_min = -0.07` to
   `-1.37`). At fixed window, every partial-information form is indefinite until the last prime power `<= x`
   enters.
3. **`eps` is an arithmetic cancellation.** `eps` is the residual of `+1.55` (pole) and `-1.48` (archimedean)
   against prime-power contributions, each of which exceeds `eps` by at least `10^{34}` at `x = 50`. Removing
   any single prime power moves the Rayleigh quotient of the eigenvector by far more than `eps`.
4. **What the kinematics do set** is the resolution scale: the saturation `N_sat ≈ 1.7 x log x` of `Delta I_N`,
   of `eps_N` and of the envelope. It is a Weyl-count scale (heuristic in Section 3), and the Weyl law is
   kinematic data (the archimedean factor plus the pole). Below `N_sat` the envelope is tiny and the truth
   sits on its boundary. That is the Loewner redundancy of a window with more modes than zeros, and it is
   kinematic, but its size (for example `r ~ 1e-7` at `x = 13`, `N = 10`) has nothing to do with `e^{-4 pi x}`.

Verdict for the round: within the dilation channel, the `e^{-4 pi x}` convergence is **specific to the
arithmetic**. It is the size of the residual after an exact cancellation that uses every prime power up to
`x`, and the first-zero error is slaved to that residual. The kinematic envelope explains where the channel
saturates in `N`, not how fast it converges in `x`. Caveat (not tested here): the paper's prolate heuristic
(`1 - chi_4(lambda) ~ e^{-4 pi lambda^2}`, CCM Section 7; `plan.md` 1.6) reads the rate `4 pi` as the
concentration defect of the square `[-lambda, lambda]^2` in the *additive* variable. That is kinematic only
after Poisson summation, which uses all the primes at once (the integers). Lane B2's calibration case, where
the arithmetic is known, is the place to separate "any discrete spectrum with this Weyl law" from "these zeros".

## 7. Findings against the brief

1. **The MaxEnt prediction `c = 0` (A1.1) is not admissible for the window form** (Lemma A1.1'(5)): the
   Loewner structure fixes the new column up to `b_{N+1}`, and `c = 0` is not of that form. The brief's
   `Delta I_K` is still well defined. It is the Gaussian mutual information between the new and the old modes
   (Lemma A1.1(4)), and it is reported. In addition I computed the exact analogue of `prop:extension-disc`:
   the admissible interval of `b_{N+1}` given `a_{N+1}`, its structured MaxEnt point and `Delta I^s`. The
   brief's statement that A1.1 is "the non-Toeplitz analogue of `prop:extension-disc`(i)-(ii)" is only half
   right. The disc is a section of the ellipsoid by the structural constraint, and its centre is the
   constrained MaxEnt point, not `c = 0`.
2. **"Known diagonal" is ambiguous for the two new modes `+-(N+1)`.** In the `V_n` basis the new 2x2 block is
   `[[a, b/(N+1)], [b/(N+1), a]]`: its diagonal is `a_{N+1}`, and its off-diagonal entry contains the new
   datum. I used the even/odd diagonal `d_{e,o} = a +- b/(N+1)`, as the brief says to work in the blocks. The
   `V`-basis version differs by `-log(1 - (b_{N+1}/((N+1) a_{N+1}))^2)`.
3. **"Each new prime power changes `(a_n, b_n)` by the closed-form prime term" (A1.3) is false in the CCM
   protocol.** At `x = k` the prime power `k` enters with weight 0, and between knots every entry changes
   because `L = log x` changes. The statement is true only in the fixed-window protocol, which I ran as the
   second protocol. It is not the CCM form, and it is indefinite until the last prime power.
4. **Saturation is not at `7.5 x`.** `Delta I_N` and `eps_N` saturate at `N_sat ≈ 1.7 x log x` (`4.3x`, `5.4x`,
   `7.0x` at `x = 13, 25, 50`). The benchmark's `7.5x` (two points, a criterion based on zeros usable to
   `1e-3`) agrees only near `x = 50`. Benchmark item 1's "N does not enter" holds only for `N >= N_sat(x)`. At
   fixed `N` the `e^{-4 pi x}` law fails beyond `x ≈ N / (1.7 log x)`, so "the learning curve at fixed `N`"
   (A1.3) measures the resolution limit as much as the primes unless `N` is chosen above `N_sat(x_max)`.
5. **Benchmark data point.** The benchmark's `x = 50` value `err(z_1) = 1.54e-249` is precision-limited. At
   2400 bits `zst` certifies `2.45e-253` (`N = 360`), which restores `err/eps ≈ 1e4` and gives 5.36 digits per
   unit of `x` between `x = 25` and 50. The law `log10 err ~ -5.4 x + 15` is unaffected; its `x = 50` point
   (`-248.5`) should read `-252.6`.
6. **"Eigenvector overlap with the eigenvector at the final `x`" needs an identification of windows.** The
   eigenvectors at different `x` live on different windows. I report the coefficient overlap (window rescaled
   to unit length) and the intrinsic `L^2(R_+^x, d*u)` overlap on centred windows. They differ by one to two
   orders of magnitude in `1 - overlap`.
7. **Precision.** Ball `LDL^T` needs 2.6 to 4.6 times `log2(1/eps)` bits of headroom (Section 2), much more
   than the benchmark's `40x + 200`. `x = 50` with `Nmax = 520` needed 4200 bits and 6.4 min in total. That is
   affordable, so the brief's "as far as the stack allows" is met at `x = 13, 25, 50`, all certified.
   Nothing exploratory in mpmath was needed.
8. **"Kinematic envelope" (question 3) is ambiguous** between shard 08g's Schur radius and lane B2's
   "maximum-determinant element of the window cone consistent with the pole and archimedean data". I answered
   for the first. For the second, the relevant datum from this lane is the prime-free control: it is
   indefinite, so no positive element of that cone agrees with the pole and archimedean data on the full
   Loewner window, and the B2 computation needs a relaxation. This is my reading of the control, not a
   computation of the cone.
9. **Partial-information forms are not posteriors.** The brief's picture of a posterior contracting as data
   are added presupposes positive forms at every stage. At fixed window the partial forms are indefinite, so the
   posterior of the partial data (the positive extensions) is not represented by them. In the CCM protocol
   every stage is positive, which is why it gives a smooth learning curve.

## 8. Reproduction

    make -C zst && make -C zst check          # pipeline and tests unchanged
    zst/tools/rtp1_a1_run.sh                  # writes outputs/rtp1_a1_*.txt (12 min CPU, 6.5 min wall)
    zst/tools/rtp1_a1_run.sh /tmp/rerun && for f in outputs/rtp1_a1_*.txt; do cmp $f /tmp/rerun/$(basename $f); done
    python3 zst/tools/rtp1_a1_summary.py      # saturation table, ratios, slopes (Sections 3-5)

Each output starts with its fixed parameters and ends with its check count (all 0 failed). Byte identity of
two independent runs was confirmed with `cmp` for all six files.
