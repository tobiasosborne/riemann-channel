# RTP-2 follow-up to lane E: the conductor exponent of the weight-two learning law

Author: `claude:opus`, 2026-09-26. Unreviewed research record; nothing here is registered. No RH assumption anywhere.
**No zero of any L-function is used anywhere**: every run has `--compare 0`, so the driver's COMPARISON STEP is
skipped and no `zero` line is read (the appended reference entries have none). Every number that enters a form
comes from the minimal model (through zst's own point counts), the conductor, and the archimedean factor.

Task, from the lane-E review (`notes/reviews/rtp-round-2-ellcurve-2026-09-26.md`, "most important finding" and
"Recommendation for shard 08j", item 4): pin the exponent alpha in
`log10 eps ~ a_C - k sqrt(x)/C^alpha` by running the lane-E driver on about ten rank-zero curves of small conductor.
Lane E had only two conductors (11, 14): best alpha 0.572, window 0.47–0.67, with 1/2 allowed but not singled out.

## Answer in one paragraph (NUMERICAL)

On a **matched phase-space window** (each curve over the same range of `z = sqrt(x/C)`, 1.087 to 2.132), 16
rank-zero curves with conductors 11 to 36 give **alpha = 0.488**. The intervals are: curve bootstrap 95 %
**[0.473, 0.502]**; between-curve regression 0.4876 ± 0.0065 (95 % t interval [0.474, 0.501], r^2 = 0.998);
leave-one-curve-out [0.483, 0.493]. Adding a `b log10 x` prefactor changes nothing (0.489, [0.474, 0.502]). Adding
three larger conductors (50, 67, 109) gives 0.497 [0.483, 0.519]. So alpha = 1/2 is pinned to about ±0.015 and lies
inside every interval, while 0, 1 and lane E's 0.57 are all excluded. One qualification: on the listed 16 the
estimate sits 0.012 below 1/2, with 1/2 at the upper edge of the bootstrap interval. The Gaussian profile
(n log RSS ratio 9.1) disfavours 1/2, but its iid assumption fails because the residuals are strongly correlated
along x (lane-E review). This is the size of shift that the unresolved N-tail and the slow drift of the local
slope with z can produce (below). On the **unmatched window** x in [13, 50] that lane E used, the same data give
0.552 [0.534, 0.577], which excludes 1/2. That value is an artefact of comparing curves at different z: conductor
36 sits at z = 0.60–1.18 while conductor 11 sits at 1.09–2.13, and the local slope per unit z is lower at small z.
A single `b log10 x` prefactor absorbs this and returns 0.488 [0.456, 0.525] on the same unmatched data. Verdict:
**the conductor enters as sqrt(x/C) to within the resolution of the experiment (about ±0.015 in alpha)**. The
digits per unit `S_max = 2 sqrt(x/C)` on the matched window are 5.04–5.24 (mean 5.12, s.d. 0.05) for all 16 curves.
That is inside the 4.3–5.4 range the review quotes for other objects and about 6 % below `4 pi/ln 10 = 5.4575`.

## What was run

Driver: `zst/tools/rtp2_ellcurve.c` (lane E, `codex:gpt-6-astra`), with one added option (see "Code").
Run script: `zst/tools/rtp2_ellconductors_run.sh` (this lane). Reference data: `ell_ref_ext.txt` (this directory)
via the driver's existing `--ref` option. All forms, eigenpairs and parities are certified (arb balls, Rump plus
deflation intersected with `zst_block_min` brackets, as in lane E). All 1374 `EIG` lines in the 53 files print
12-digit certified minima (no ball-valued entry), even parity, and zero negative eigenvalues in both blocks.

| phase | curves | protocol | outputs (`outputs/`) | wall |
|---|---|---|---|---|
| `n60` | 11a1 14a1 15a1 17a1 19a1 20a1 21a1 24a1 26a1 27a1 30a1 32a1 33a1 34a1 35a1 36a1, and extras 50a1 67a1 109a1 | lane-E axis-x CCM: N = 60, knots = prime powers ≤ 50 and x = 50, 2700 bits | `rtp2_ellconductors_<c>_axisx_ccm_N60.txt` (19) | 265–290 s each |
| `n120` | 11a1 17a1 26a1 36a1 | same, N = 120, to x = 50, 3200 bits | `…_axisx_ccm_N120.txt` (4) | 1600–1700 s each |
| `matchz` | the 18 curves other than 11a1 | same as `n60` but xmax = round(50 C/11), capped at 250 (the driver's limit) | `…_axisx_ccm_N60_matchz.txt` (18) | 316–716 s each |
| `satpts` | 11a1 20a1 27a1 36a1 50a1 67a1 | single knot at the top of the matched window, N = 120 and N = 200, 2000 bits | `…_point_x<X>_N{120,200}.txt` (12) | 44 s / 150 s |

Total 53 output files, 19336 driver checks, 0 failed, 6.1 core-hours. Outputs have no timestamps: 15a1, 36a1 and
109a1 (N = 60) were rerun into a scratch directory and are byte-identical. The new 11a1 and 14a1 N = 60 files are
byte-identical to lane E's `rtp2_ellcurve_{11a1,14a1}_axisx_ccm_N60.txt` apart from the header line, the skipped
comparison block, and the check count: 363 − 25 = 338, the 25 being the comparison checks. (The reproducibility
rerun rewrote `checks/runlogs/{15a1,36a1,109a1}_axisx_ccm_N60.log`; those three wall times are the rerun's.)
`checks/check_models.py --pari` needs `cypari2`, which was installed in a scratch venv; its output is committed as
`checks/check_models.out`.

Fits: `fit.py` (this directory; numpy, scipy), output `checks/fit.out`, 1811 checks, 0 failed, deterministic (fixed
bootstrap seed; rerun `cmp`-identical). It reads only `EIG` lines. The global minimum at each knot is
min(epsE, epsO), and every parity flag is audited against the two printed block minima.

## Provenance (details in `sources.md`)

The models, conductors and ranks come from Cremona's `ecdata` table `allcurves.00000-09999` (raw GitHub file,
sha256 `259f3846…efa968`; the rows are copied verbatim to `cremona_rows.txt`). Each was checked three ways:

- **LMFDB.** A record for each of the 19 curves (API or curve page, via WebFetch; `curl` got a reCAPTCHA). All agree
  on a-invariants, conductor, rank and analytic rank 0.
- **PARI 2.17.2.** `ellglobalred` conductor, `ellminimalmodel` (minimal), `ellrootno` = +1 and `ellanalyticrank`
  = 0 for all 19.
- **Pure Python.** The prime support of the discriminant equals the conductor's, and the multiplicative primes are
  exactly those with exponent 1 in C.

In addition, `zst_ell_ap`, the driver's own point count read through `zst_ell_ref` from `ell_ref_ext.txt`, equals
PARI `ellap` for all primes below 200 on all 19 curves. Root numbers +1 are PARI's (forced by analytic rank 0);
none was taken from LMFDB.

## Code

- `zst/tools/rtp2_ellcurve.c`: added `--compare 0|1` (default 1). With 0, the COMPARISON STEP of both the axisN and
  axisx modes is replaced by one comment line, `# COMPARISON STEP skipped (--compare 0): no reference zero read or
  used`, and no zero is read. Nothing else changed. The `--ref <path>` option already existed.
- **Regression checks with the default:** `make -C zst check` passes. Lane-E outputs `11a1_axisN_x13`,
  `389a1_record` and `14a1_spectra_x25` rerun byte-identically.
- `zst/src/`, `zst/include/` and `zst/tests/data/ell_ref.txt` are untouched. `ell_ref_ext.txt` is the original
  file verbatim (its first 1607 lines `cmp`-identical) plus 17 appended curve/end blocks without `ap` or `zero`
  lines. The loader does not need `ap` lines, and it reads `zero` lines only in the comparison step.
- Checks: `checks/check_models.py` (+ `.out`), `checks/ap_check.c`, `checks/ap_compare.py` (+ `.out`), run logs in
  `checks/runlogs/`.

## Tables

Certified digits only. "digits/unit S_max" is the least-squares slope of −log10 eps against `S_max = 2 sqrt(x/C)`,
equal to `(sqrt C/2)` times the slope against sqrt x. Fits and slopes are floating-point arithmetic on certified
values.

### Table 1. Unmatched window, N = 60: certified global minimum eps (all even parity) and per-curve slopes on 13 ≤ x ≤ 50 (16 knots)

| curve | C | eps(13) | eps(25) | eps(50) | digits / sqrt x | digits / unit S_max | RMS sqrt x | RMS x | best power p |
|---|---|---|---|---|---|---|---|---|---|
| 11a1 | 11 | 7.676597373e-07 | 2.517205451e-11 | 1.130703092e-17 | 3.07221 | 5.09469 | 0.0879 | 0.2995 | 0.512 |
| 14a1 | 14 | 5.500672778e-06 | 1.037169120e-09 | 3.240256686e-15 | 2.67651 | 5.00730 | 0.0744 | 0.2914 | 0.456 |
| 15a1 | 15 | 1.210228066e-05 | 3.295600352e-09 | 1.570612803e-14 | 2.59759 | 5.03021 | 0.0843 | 0.3029 | 0.424 |
| 17a1 | 17 | 3.404172096e-05 | 1.842379624e-08 | 1.475436009e-13 | 2.43890 | 5.02793 | 0.0524 | 0.2340 | 0.520 |
| 19a1 | 19 | 7.828732295e-05 | 7.666611344e-08 | 7.569750003e-13 | 2.33860 | 5.09686 | 0.0815 | 0.2202 | 0.548 |
| 20a1 | 20 | 1.041873318e-04 | 1.373790414e-07 | 3.235087260e-12 | 2.15931 | 4.82836 | 0.0755 | 0.1848 | 0.585 |
| 21a1 | 21 | 1.450259725e-04 | 3.095753125e-07 | 3.663934274e-12 | 2.23139 | 5.11277 | 0.1291 | 0.0961 | 0.785 |
| 24a1 | 24 | 6.081098412e-04 | 8.261018294e-07 | 5.254025369e-11 | 2.00881 | 4.92057 | 0.0434 | 0.1895 | 0.519 |
| 26a1 | 26 | 6.651117697e-04 | 2.976108683e-06 | 2.460395430e-10 | 1.87209 | 4.77291 | 0.0786 | 0.1112 | 0.699 |
| 27a1 | 27 | 9.834930957e-04 | 3.070236618e-06 | 3.241816012e-10 | 1.88084 | 4.88657 | 0.0434 | 0.1630 | 0.562 |
| 30a1 | 30 | 2.307315957e-03 | 1.143543286e-05 | 2.016991645e-09 | 1.74163 | 4.76966 | 0.0860 | 0.1054 | 0.713 |
| 32a1 | 32 | 2.998246319e-03 | 1.382071800e-05 | 4.501296854e-09 | 1.69866 | 4.80454 | 0.0308 | 0.1563 | 0.533 |
| 33a1 | 33 | 2.919165830e-03 | 1.157064214e-05 | 3.584189988e-09 | 1.73869 | 4.99401 | 0.0565 | 0.1881 | 0.471 |
| 34a1 | 34 | 1.745540720e-03 | 1.889364045e-05 | 6.382099626e-09 | 1.62728 | 4.74431 | 0.0821 | 0.1472 | 0.603 |
| 35a1 | 35 | 3.864489299e-03 | 3.227134004e-05 | 1.137600539e-08 | 1.59447 | 4.71651 | 0.1000 | 0.1085 | 0.727 |
| 36a1 | 36 | 6.873034603e-03 | 4.738025331e-05 | 1.496440154e-08 | 1.62560 | 4.87681 | 0.0517 | 0.1184 | 0.631 |
| 50a1 | 50 | 4.992416648e-02 | 6.224664455e-04 | 1.583244410e-06 | 1.27091 | 4.49335 | 0.0442 | 0.1606 | 0.354 |
| 67a1 | 67 | 1.902469004e-02 | 1.126463216e-04 | 5.602589160e-06 | 0.91803 | 3.75719 | 0.2783 | 0.3617 | 0.050 |
| 109a1 | 109 | 2.258793149e-01 | 1.645385864e-02 | 3.431034052e-04 | 0.78242 | 4.08433 | 0.0586 | 0.0756 | 0.639 |

- **Rank zero, even parity.** All 19 curves have an even global minimum at every knot x = 2…50 and a positive
  definite form at every knot (no curve dropped). The 11a1 and 14a1 slopes reproduce lane E (3.072212, 2.676512;
  checked in `fit.py`).
- **The 16 listed curves.** 4.72–5.11 digits per unit S_max (mean 4.92, s.d. 0.14). The per-S_max slope falls as
  C rises, because larger C means smaller z on this window.
- **The extras sit mostly below the conductor scale** (sqrt(x/C) < 1). 67a1 has a shoulder: eps falls from 1.9e-2
  to 1.1e-4 between x = 13 and 25, then only to 5.6e-6 by x = 50. That shoulder is why its sqrt-x fit is poor
  (RMS 0.28, best power 0.05).

### Table 2. Matched window z = sqrt(x/C) in [sqrt(13/11), sqrt(50/11)] = [1.087, 2.132], N = 60

| curve | C | last knot x | knots | z range | digits / unit S_max | digits / sqrt x | eps at last knot |
|---|---|---|---|---|---|---|---|
| 11a1 | 11 | 50 | 16 | 1.087–2.132 | 5.09469 | 3.07221 | 1.130703e-17 |
| 14a1 | 14 | 61 | 16 | 1.102–2.087 | 5.04312 | 2.69566 | 2.603130e-17 |
| 15a1 | 15 | 68 | 18 | 1.125–2.129 | 5.06547 | 2.61580 | 8.598679e-18 |
| 17a1 | 17 | 77 | 19 | 1.163–2.128 | 5.14820 | 2.49724 | 4.582072e-18 |
| 19a1 | 19 | 86 | 22 | 1.100–2.128 | 5.09664 | 2.33850 | 5.133664e-18 |
| 20a1 | 20 | 89 | 21 | 1.118–2.110 | 5.10643 | 2.28366 | 9.558281e-18 |
| 21a1 | 21 | 95 | 22 | 1.091–2.127 | 5.19333 | 2.26655 | 4.738716e-18 |
| 24a1 | 24 | 109 | 24 | 1.099–2.131 | 5.09939 | 2.08182 | 4.523905e-18 |
| 26a1 | 26 | 118 | 25 | 1.092–2.130 | 5.12297 | 2.00939 | 5.280722e-18 |
| 27a1 | 27 | 121 | 24 | 1.089–2.117 | 5.12388 | 1.97218 | 5.636140e-18 |
| 30a1 | 30 | 136 | 28 | 1.111–2.129 | 5.12700 | 1.87212 | 4.717982e-18 |
| 32a1 | 32 | 145 | 29 | 1.132–2.129 | 5.15157 | 1.82136 | 3.609605e-18 |
| 33a1 | 33 | 150 | 30 | 1.115–2.132 | 5.18359 | 1.80469 | 2.201883e-18 |
| 34a1 | 34 | 151 | 30 | 1.098–2.107 | 5.24138 | 1.79778 | 3.903506e-18 |
| 35a1 | 35 | 159 | 31 | 1.108–2.131 | 5.11539 | 1.72932 | 3.199374e-18 |
| 36a1 | 36 | 163 | 31 | 1.093–2.128 | 5.06795 | 1.68932 | 3.765423e-18 |
| 50a1 | 50 | 227 | 38 | 1.105–2.131 | 5.17150 | 1.46272 | 2.547931e-18 |
| 67a1 | 67 | 250 | 38 | 1.100–1.932 | 5.19038 | 1.26821 | 7.472338e-17 |
| 109a1 | 109 | 250 | 25 | 1.096–1.514 | 4.57577 | 0.87656 | 2.778177e-12 |

- **The 16 listed curves.** 5.043–5.241 digits per unit S_max (mean 5.124, s.d. 0.051). eps at the top of the
  window is 2e-18 to 3e-17 for every conductor from 11 to 50: equal z gives equal eps to within about one digit.
- **67a1 and 109a1** are cut short by the driver's x ≤ 250 limit. 109a1 covers only z ≤ 1.51, where the slope is
  lower (4.58).
- **Parity.** Every knot of every matched-window run is even (checked).

### Table 3. The exponent alpha (common k and alpha; digits = log10)

M1: `log10 eps = a_c − k sqrt(x)/C^alpha` (per-curve intercepts). M2: common intercept. M3: M1 + common `b log10 x`.
M4: M2 + common `b log10 x`. Intervals: bootstrap = curves resampled with replacement, 2000 draws, percentile 95 %
(the honest one: curve-to-curve arithmetic is the noise); LOO = leave one curve out; "10 % window" = RMS ≤ 1.1 ×
minimum (the review's descriptive window); Gaussian = n log(RSS/RSS_min) ≤ 3.84 (iid; too narrow, the residuals are
correlated along x). "Between" = OLS of log s_c on log C for the per-curve sqrt-x slopes s_c.

| data | model | best alpha | bootstrap 95 % | LOO | 10 % window | Gaussian | RMS best | RMS at 0 / 1/2 / 1 | 1/2 inside bootstrap |
|---|---|---|---|---|---|---|---|---|---|
| matched, 16 | M1 | **0.4884** | **[0.473, 0.502]** | [0.483, 0.493] | [0.454, 0.522] | [0.481, 0.495] | 0.0801 | 0.487 / 0.0810 / 0.575 | yes |
| matched, 16 | M3 | 0.4886 (b = 0.49) | [0.474, 0.502] | [0.484, 0.493] | [0.455, 0.522] | [0.482, 0.495] | 0.0798 | 0.255 / 0.0807 / 0.271 | yes |
| matched, 16 | M2 | 0.4683 | [0.462, 0.475] | [0.466, 0.470] | [0.460, 0.477] | [0.467, 0.470] | 0.1129 | 1.900 / 0.213 / 2.337 | no (misspecified: intercepts differ by ~1 digit) |
| matched, 16 | between | 0.4876 ± 0.0065 | t: [0.474, 0.501] | | | | r^2 = 0.998 | | yes |
| matched, 19 | M1 | 0.4965 | [0.483, 0.519] | [0.488, 0.499] | [0.465, 0.528] | [0.491, 0.502] | 0.0932 | 0.681 / 0.0933 / 0.666 | yes |
| matched, 19 | between | 0.5205 ± 0.0112 | t: [0.497, 0.544] | | | | r^2 = 0.992 | | yes (109a1's partial window pulls it up) |
| unmatched 13–50, 16 | M1 | 0.5517 | [0.534, 0.577] | [0.548, 0.557] | [0.506, 0.597] | [0.540, 0.563] | 0.0860 | 0.470 / 0.0969 / 0.391 | **no** |
| unmatched 13–50, 16 | M3 | 0.4877 (b = 1.76) | [0.456, 0.525] | [0.480, 0.502] | [0.417, 0.578] | [0.468, 0.509] | 0.0807 | 0.470 / 0.0808 / 0.155 | yes |
| unmatched 13–50, 16 | M2 | 0.4673 | [0.455, 0.477] | [0.464, 0.469] | [0.449, 0.487] | [0.463, 0.472] | 0.1423 | 2.005 / 0.177 / 1.133 | no |
| unmatched 13–50, 16 | M4 | 0.4656 (b = 0.05) | [0.396, 0.508] | [0.430, 0.477] | [0.364, 0.608] | [0.435, 0.499] | 0.1423 | 2.004 / 0.143 / 0.248 | yes |
| unmatched 13–50, 16 | between | 0.5544 ± 0.0140 | t: [0.524, 0.584] | | | | r^2 = 0.991 | | no |
| unmatched 13–50, 19 | M1 | 0.5827 | [0.551, 0.633] | [0.566, 0.595] | [0.529, 0.637] | [0.570, 0.596] | 0.1151 | 0.620 / 0.141 / 0.397 | no |
| unmatched 13–50, 19 | M3 | 0.5243 (b = 1.31) | [0.473, 0.615] | [0.496, 0.537] | [0.425, 0.657] | [0.497, 0.553] | 0.1120 | 0.620 / 0.113 / 0.182 | yes |

- **Per-curve residuals** of the matched-window between-curve regression, as the percentage by which each curve's
  slope departs from the fitted law: +0.4, −1.0, −0.6, +0.9, −0.3, −0.1, +1.5, −0.5, −0.2, −0.2, −0.3, +0.1, +0.7,
  +1.8, −0.7, −1.6 for 11a1…36a1. That is 1.8 % at most, against 13 % for the lane-E conductor pair.
- **Reduction type** (semistable mean +0.21 %, additive mean −0.47 %). Additive reduction somewhere: 20a1, 24a1,
  27a1, 32a1, 36a1. No visible dependence on reduction type or on the number of bad primes.

### Table 4. Saturation in N

The four N = 120 axis runs are compared with N = 60 at the same knots. The largest relative change of eps is always
at the top knot (x = 49 or 50). The slopes are over 13 ≤ x ≤ 50.

| curve | max rel. change of eps, N 60 → 120 | digits / unit S_max, N = 60 | N = 120 |
|---|---|---|---|
| 11a1 | 0.164 (x = 50) | 5.09469 | 5.12346 |
| 17a1 | 0.094 (x = 49) | 5.02793 | 5.04915 |
| 26a1 | 0.055 (x = 50) | 4.77291 | 4.78701 |
| 36a1 | 0.025 (x = 49) | 4.87681 | 4.88623 |

The single-knot runs sit at the top of the matched window (z ≈ 2.13; 67a1 at 1.93):

| curve | x | eps N = 60 | N = 120 | N = 200 | log10(eps60/eps200) | log10(eps120/eps200) |
|---|---|---|---|---|---|---|
| 11a1 | 50 | 1.130703092e-17 | 9.715393488e-18 | 9.291035576e-18 | 0.0853 | 0.0194 |
| 20a1 | 91 | 5.578023652e-18 | 4.879516545e-18 | 4.654305656e-18 | 0.0786 | 0.0205 |
| 27a1 | 123 | 3.971795314e-18 | 3.619496072e-18 | 3.459619981e-18 | 0.0600 | 0.0196 |
| 36a1 | 164 | 3.227377197e-18 | 2.823604758e-18 | 2.661840389e-18 | 0.0837 | 0.0256 |
| 50a1 | 227 | 2.547931371e-18 | 2.254830504e-18 | 2.069611243e-18 | 0.0903 | 0.0372 |
| 67a1 | 250 | 7.472337515e-17 | 6.672141535e-17 | 6.393699781e-17 | 0.0677 | 0.0185 |

N = 60 is not fully converged at the top of the window: it overstates eps there by 0.06–0.09 digits, and N = 120
still by 0.02–0.04. The tail is **the same size at every conductor** from 11 to 67 (no trend in C). At equal z the
unresolved tail is therefore conductor-independent, so it biases every matched-window slope by the same amount:
about +0.04 digits per unit S_max (≈ 0.8 %). It cannot move alpha by more than about 0.01. It does lower the absolute
slope: corrected to N = 200, the matched-window mean would be about 5.16 digits per unit S_max rather than 5.12.

## Verdict on alpha (NUMERICAL)

The conductor exponent is **alpha = 0.49 ± 0.015**. Best estimates are 0.488 on 16 curves and 0.497 with three larger
conductors; all bootstrap, leave-one-out and between-curve intervals contain 1/2; alpha = 0, 1, 0.57 and 0.6 are
excluded.

1/2 is therefore singled out in the practical sense: a band of width ~0.03 containing it. It is not singled out in
the strict sense that the data could tell 0.49 from 0.50. The best values lie 0.003–0.012 below 1/2, with 1/2 at the
upper edge of the 16-curve bootstrap interval; the iid Gaussian profile would exclude it, but that profile is not
trustworthy here (correlated residuals). Two known effects are of the size of that offset: the conductor-independent
N-tail, and the slow growth of the local slope with z (4.7–4.9 digits per S_max at z ≈ 0.6–1.2, 5.0–5.2 at
1.1–2.1). The matched-window test cannot manufacture 1/2. If the true exponent were a' ≠ 1/2, windows matched in
sqrt(x/C) would sit at different values of the true variable. With a local slope growing in z (log-derivative
g ≈ 0.1), the apparent exponent would be 1/2 + (a' − 1/2)(1 + g): deviations from 1/2 are amplified, not hidden.

Lane E's 0.57 (two curves) and this lane's unmatched 0.55 (16 curves) are a design artefact of the fixed x-window,
for three reasons:

- The same data give 0.488 once a `b log10 x` prefactor is allowed, or once the window is matched in z.
- The extras (50, 67, 109), which sit at z < 1, push the unmatched value further, to 0.58.
- Their matched-window slopes (5.17, 5.19) fall in line with the rest.

## Digits per unit S_max against the other objects

| object / window | digits per unit S_max |
|---|---|
| 16 listed curves, matched window z 1.09–2.13, N = 60 | 5.04–5.24 (mean 5.12, s.d. 0.05); N-tail corrected ≈ 5.16 |
| same curves, unmatched x 13–50 (z from 0.60–1.18 up to 1.09–2.13), N = 60 | 4.72–5.11 (mean 4.92) |
| 50a1, 67a1 matched (to z 2.13, 1.93) | 5.17, 5.19 |
| 109a1 matched (z ≤ 1.51 only), 50a1/67a1/109a1 unmatched (z < 1 over much of the window) | 4.58; 4.49, 3.76, 4.08 |
| review's quoted range for zeta (per x), primitive characters (per x/q), 11a1/14a1/37a1 | 4.3–5.4 |
| `4 pi/ln 10` (bare, H-CONCENTRATION-TRANSFER leading term) | 5.4575 |

- **Where the elliptic values fall.** On the resolved window they lie at the top of the review's range and 5–6 %
  below the bare constant, a larger shortfall than zeta's (5.38 against 5.46, 1.4 %).
- **Growth with z.** The per-S_max rate grows slowly with z. This is consistent with a `−2A + O(log A)` law, whose
  logarithmic correction lowers the finite-range slope, though it does not establish it.
- **The constant.** With alpha fixed at 1/2, the common slope is k = 10.26 digits per unit sqrt(x/C) (M1), or 10.52
  with a log prefactor (M3), against `8 pi/ln 10 = 10.915`, a ratio of 0.94–0.96. The review's point stands:
  `8 pi` is not determined by a finite-range slope with structured residuals. What is now established is that the
  constant is the same for all 16 curves to ±1 % (s.d. of the per-S_max slopes 0.051 on 5.12).

## Findings against the brief

1. **The fixed x-window conductor test is biased.** Lane E's shared-slope test and the review's profiled exponent
   (0.572, window 0.47–0.67) both compare curves over the same x-range, hence over different z-ranges. With 16
   curves the bias is resolved and significant: 0.552 [0.534, 0.577] excludes 1/2. The right test compares curves
   over the same z-range, or allows a prefactor. The review's recommendation ("N = 60 axis x, x ≤ 50"), run as written
   and fitted with per-curve intercepts, would have **excluded** alpha = 1/2 on these data. The matched-window runs (≈ 6–12 min per curve) are what
   decide it.
2. **A common intercept is misspecified.** Intercepts differ by about one digit between curves at equal z (for
   example eps(z = 2.13) = 2.2e-18 for 33a1 against 2.6e-17 for 14a1). Common-intercept fits (M2, M4) give 0.466–0.468
   with RMS 40–75 % worse and should not be quoted as the exponent.
3. **N = 60 overstates eps at z ≈ 2.1 by 15–23 % relative to N = 200** (0.06–0.09 digits), although the
   log-determinant argmin there is N_sat ≈ 10 (lane E). eps keeps falling slowly with N well past N_sat. The tail
   is conductor-independent, so it does not affect alpha, but it lowers every absolute rate by about 1 %.
4. **Below the conductor scale (sqrt(x/C) < 1) the sqrt-x law does not describe eps.** 67a1 shows a shoulder
   (Table 1), and the unmatched fits of the three extras are poor. The review's warning about parity statements at
   `sqrt(x/C) < 1` extends to rate statements. The window x ≤ 50 is too short for conductors much above 50.
5. **Rank zero means even parity throughout.** All 19 rank-zero curves have an even global minimum and a positive
   definite form at every computed knot (x = 2 up to 250; N = 60, 120, 200). No curve had to be dropped for odd parity.
6. **Provenance.** LMFDB sits behind a reCAPTCHA for scripted access, and WebFetch returns a model's paraphrase.
   One page request by LMFDB label returned a different curve (21.a1 = Cremona 21a5), and one summary reported a
   local root number as the global one. The byte-exact Cremona table plus PARI is the reliable route. LMFDB
   agreement is recorded as a cross-source only.
7. **Driver limit.** `rtp2_ellcurve` rejects x > 250 (`main`: `xmax>250`). That caps the matched window for C > 55
   (67a1 to z = 1.93, 109a1 to z = 1.51). Lifting it would need a larger `ks[256]` knot array; not done here.

## What this changes in the notebook

- **Proposed wording for `num:rtp2-ellcurve-window-rate` (shard 08j), replacing the review's "conductor exponent
  bracketed 0.47–0.67 by two conductors":** "On matched windows `sqrt(x/C)` in [1.09, 2.13], sixteen rank-zero
  curves of conductor 11–36 give `log10 eps = a_C − k sqrt(x)/C^alpha` with alpha = 0.488 (curve bootstrap
  [0.473, 0.502]; with three curves of conductor 50–109, 0.497 [0.483, 0.519]); the digits per unit
  `S_max = 2 sqrt(x/C)` are 5.04–5.24, the same for all curves to ±1 %. On the unmatched window x in [13, 50] the
  estimate is biased to 0.55." Status NUMERICAL. The recommended replacement for `obs:rtp-round-1-reading`(iii)
  can then say "weight-two results are linear in sqrt(x/C), the conductor exponent pinned to 1/2 within ±0.015".
- **H-CONCENTRATION-TRANSFER** (`log eps = −2A + O(log A)`, `A = 2 pi S_max`) gains a one-parameter consistency
  check: the scale variable is `S_max` with the predicted conductor power. The constant remains OPEN, with the
  measured finite-range rate 0.94–0.96 of the bare `4 pi/ln 10`.
- **Not claimed:** anything about zeros (none used); the value `8 pi`; any statement for curves of positive rank;
  any statement at `sqrt(x/C) < 1`.
