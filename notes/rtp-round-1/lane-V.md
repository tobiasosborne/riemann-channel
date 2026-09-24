# Lane V: visualisation package for RTP-1

Author: `claude:opus`, 2026-09-24. Brief: `notes/rtp-round-1/viz-brief.md` (author `claude:fable-5.1`), under the
conventions and game rules of `notes/rtp-round-1/brief.md`. Status: figures are secondary sources. Nothing here is a
claim. Every plotted number either comes from a committed output file or is recomputed by the figure script with
the same conventions, and each caption says which.

Deliverables:

- package `viz/rtp1/`: `common.py` (theme, deterministic save, parsers for the lane A1/A2 outputs), `bridges.py`
  (reuse of lane A2's functions, of `scripts/weil_window_extension.py`, and of zst's `(a_n, b_n)`), one script per
  step (`step0_objects.py`, `step1_dilation.py`, `step2_prime_content.py`, `step3_short_range.py`,
  `step4_commutant.py`, `step5_calibration.py`, `step7_maxent.py`) and `make_all.py`;
- figures in `figures/rtp1/`: `<id>.png`, `<id>.svg` (light surface), `<id>.dark.png`, `<id>.dark.svg` (dark
  surface), the plotted numbers as `data/<id>.csv`, the step manifests `manifest/<step>.json`, `index.html` (all
  figures, captions, data sources and scripts; switches to the dark variants under `prefers-color-scheme: dark`),
  `README.md` (the same in Markdown), and the placeholder pages `s4_placeholder.html`, `s5_placeholder.html`.

Reproduction: `python3 viz/rtp1/make_all.py` from anywhere. It takes **47.6 to 47.8 s** wall time (single thread; Step 1
23 s, Step 2 18 s). Two consecutive builds give byte-identical files (110 files compared with `sha256sum`). The
build has no timestamps and no randomness, and it runs 56 internal consistency checks against the lanes' certified
numbers (all pass; a failing check stops the build). Requirements: numpy, mpmath, python-flint 0.9.0, matplotlib
(3.11.2 was installed from PyPI for this lane; it was absent), a C compiler and `zst/build/libzst.a`.

Style: the `dataviz` skill's validated reference palette (categorical slots in fixed order, validated with its
`validate_palette.js` in both modes: adjacent CVD ΔE 9.1 light / 8.4 dark), one-hue blue sequential ramp,
blue/red diverging with a grey midpoint (red negative, blue positive). Identity is never carried by colour alone:
every multi-series panel has a legend and selective direct labels.

Game rule 2: zeros of zeta appear only in panels labelled "comparison (zeros used)". These are Step 1 `s1_envelope`
panel (b) (lane A1's certified `|z_1 - gamma_1|` from its COMPARISON STEP blocks) and both panels of Step 2
`s2_explicit`. The Step 7 cartoon uses invented toy ordinates (6, 11, 15), not zeros of zeta, and says so.

## Figure list

"Certified" means the plotted numbers are midpoints of balls certified by a lane (parsed from its output, or
produced by calling that lane's own certified routines). "Recomputed" means computed here for display, with the
check against a certified number named.

| file | one-line caption | kind | data source | script |
|---|---|---|---|---|
| `s0_line` | Weil distribution on the dilation line: CCM windows (x = 13, 50), pole, archimedean and their sum, prime comb | closed form | brief Conventions; plan.md 1 | `step0_objects.py` |
| `s0_testfns` | Fourier test functions V_n in the x = 13 window; the bump at log 6 with delta_max({2,3}, 1) = 0.0771 reaching log 7 | closed form; delta_max certified (A2) | `outputs/rtp1_prime_content.txt` | `step0_objects.py` |
| `s0_lattice` | {2,3} (A <= 3) and {2,3,5} (A <= 2) lattice points on the line by degree, foreign prime powers, binding pairs | exact; delta_max certified (A2) | `outputs/rtp1_prime_content.txt` | `step0_objects.py` |
| `s0_convolution` | phi^* * phi for bumps at log 4 and log 6: support around log(3/2), touching log 2 only at a non-admissible delta | closed form (floating) | A2 delta grid | `step0_objects.py` |
| `s1_window` | heat maps of tau (full, even, odd) at x = 13, N = 30 | **recomputed** (floating, from zst's `(a_n, b_n)`); block decomposition checked | zst via `bridges.zst_ab` | `step1_dilation.py` |
| `s1_ground` | minimal even eigenvector as a function in the window, x = 13, 25, 50 (N = 60, 150, 360), and its coefficients | **recomputed** (multiprecision midpoint inverse iteration); Rayleigh quotients equal A1's certified eps | zst; A1 axisN outputs | `step1_dilation.py` |
| `s1_axisN` | Delta I_N vs N (N_sat and 7.5x marked), collapse vs N/(x log x), envelope r_j vs N, truth position abs(tau_j) | certified (A1) | `outputs/rtp1_a1_axisN_x{13,25,50}.txt` | `step1_dilation.py` |
| `s1_learning_ccm` | CCM protocol at N = 60, 120: eps_N(x), 1 - overlap (coefficient and intrinsic), log det, prime powers ticked | certified (A1) | `outputs/rtp1_a1_axisx_ccm_N{60,120}.txt` | `step1_dilation.py` |
| `s1_learning_fixedL` | fixed-window protocol: number of negative eigenvalues vs prime powers included (0 only at 49), lambda_min, overlap, log abs(det) | certified (A1) | `outputs/rtp1_a1_axisx_fixedL_N60.txt` | `step1_dilation.py` |
| `s1_envelope` | Schur envelope r_j vs eps_N and an e^(-4 pi x) reference; (b) comparison (zeros used): abs(z_1 - gamma_1) follows eps_N | certified (A1); (b) comparison (zeros used) | A1 CCM outputs | `step1_dilation.py` |
| `s1_posterior` | admissible interval of the next datum b_(N+1) (centre = structured MaxEnt, truth, edge = singular) for 12 N at x = 13; unstructured ellipsoid as an exact 2-D section, labelled as such | (a) certified (A1); (b) **recomputed**, matches certified s_e, r_e | A1 axisN x13; zst | `step1_dilation.py` |
| `s2_gram` | Gram matrix {2,3}, A = 2, delta = 0.01232: G, prime-free part, mixed entries, their pole and archimedean parts | certified (A2 routines, arb midpoints); lambda_min checked | `scripts/rtp1_prime_content.py` | `step2_prime_content.py` |
| `s2_eigvec_23` | minimal eigenvector on the {2,3} grid (A = 2, 3) vs the product state (Kronecker sum), and the difference | certified (A2 routines); lambda and Schmidt defect checked | A2 script and output | `step2_prime_content.py` |
| `s2_eigvec_235` | the same for {2,3,5}, A = 2, in three slices | certified (A2 routines) | A2 script and output | `step2_prime_content.py` |
| `s2_scaling` | mixed-entry gap (slope 1), Schmidt defect (slope 2), eigenvector movement on adding a prime (slope 2), against delta | certified (A2) | `outputs/rtp1_prime_content.txt` sections 5b, 6 | `step2_prime_content.py` |
| `s2_deltamax` | delta_max vs A for {2}, {2,3}, {2,3,5}, annotated with binding pairs | certified (A2) | same, section 2 | `step2_prime_content.py` |
| `s2_explicit` | comparison (zeros used): zero-side partial sums vs prime-side values; certified truncation errors | comparison (zeros used): Psi and errors certified (A2), curves **recomputed** (floating) | same, section 7; flint zeros | `step2_prime_content.py` |
| `s3_short_range` | Weil distribution near 0; a bump inside and widened past log 2; the form value of one bump split by term; total on log scale | closed form + floating; five certified check points (A2 `entry`) | lane B1 statements; A2 script | `step3_short_range.py` |
| `s4_placeholder` | kinematic commutant: **not drawn**, lane B2 had not reported | placeholder | none | `step4_commutant.py` |
| `s5_placeholder` | calibration case: **not drawn**, lane B2 had not reported | placeholder | none | `step5_calibration.py` |
| `s7_disc` | extension disc of the next trace for K = 1, 2, 3 (in place and recentred on the MaxEnt centre), radius r_K; K = 4 pinned | exact examples (floating) | `scripts/weil_window_extension.py` (its `disc`, `levinson_centre`) | `step7_maxent.py` |
| `s7_saddle` | toy off-line pair: bowl (all on the line) vs saddle (pair at 1/2 +- 0.4), and the exposing test function | toy closed form | metric-as-state.md section 7 | `step7_maxent.py` |

Checks run by the build (a selection): `U^T tau U` equals zst's even and odd blocks; zst's `(a_1, b_1)` equal the
values printed in A1's output; the recomputed ground states have Rayleigh quotients `1.0136e-58`, `6.7808e-123`,
`2.2693e-257`, matching A1's certified eps (to 2%); `argmin log det = 56, 134, 352`; the recomputed Schur complement
and interval half-width at x = 13, N = 60 (`1.1497`, `1.1687`) equal the certified `s_e`, `r_e`; the plotted Gram
matrix has lambda_min `0.76014856` and every mixed entry equals its pole plus its archimedean part; lambdas and
Schmidt defects of the three eigenvector cases match A2's table; the eigenvector with mixed entries zeroed is a
product state (Schmidt defect < 1e-12); the floating partial sums reproduce all of A2's certified truncation errors
above 1e-14 to their three printed digits; the floating bump form value matches A2's certified diagonal at delta =
0.02 to 0.2 to six digits; the permutation and Petersen discs have centre = Levinson predictor and radius =
det T_K / det T_(K-1).

## Findings against the brief

1. **Steps 4 and 5 could not be drawn: lane B2 had not reported.** At the final build `notes/rtp-round-1/lane-B2.md`
   did not exist. Lane B2's in-progress files were present (`outputs/rtp1_commutant.txt`, reporting 27 checks passed
   and 1 failed; `scripts/rtp1_commutant.py`; `scripts/rtp1_calibration.py` still being written). They were not
   used, because an unreported, unreviewed lane with a failing check is not a data source. Per the brief, there are
   placeholder pages (`s4_placeholder.html`, `s5_placeholder.html`, and cards in the index). The step scripts check
   for B2's files at build time and list what they found. Nothing of B2 is anticipated. Re-run
   `make_all.py` after adding drawing code once lane B2 reports.
2. **Step 1 posterior: not the free ellipsoid with `c = 0`.** Following lane A1's correction (A1.1'), the main panel
   is the admissible **interval** of the next datum `b_(N+1)` (certified `r_j`, `tau_j`), drawn per row in its own
   units: the centre is the structured MaxEnt prediction, the true value is marked, and the edge is the singular
   enlargement. The unstructured ellipsoid appears only as a second panel labelled as such. It is an **exact 2-D
   section**, not a projection onto the two dominant directions. The section is the plane through the MaxEnt point
   `(c = 0, d = d_true)` that contains the Loewner line of admissible columns. A projection would misstate the
   chord: a line can leave the ellipsoid before its projection leaves the ellipsoid's shadow. The section shows
   both facts at once: the Loewner line crosses the set in exactly the admissible interval, and `c = 0` is off the
   line. The section is for the even block. The joint interval of A1 is the intersection of the even and odd
   intervals.
3. **Saturation marker.** The brief asks for `N = 7.5 x`. Both are marked: the benchmark's `7.5 x` (diamonds,
   labelled "not the saturation") and lane A1's `N_sat = argmin log det ≈ 1.7 x log x` (circles). Plotted against
   `N/(x log x)`, the three `Delta I_N` curves fall onto one another near 1.7. `7.5 x` agrees only near x = 50.
4. **"Kinematic envelope" is read as lane A1's Schur envelope `r_j`** (A1 Finding 8). The other reading, lane B2's
   max-det element of the window cone, cannot be drawn yet. The `e^(-4 pi x)` line is a reference slope anchored at
   `eps_120(13)`, not a fit.
5. **Step 2 gap against delta "(linear)" is drawn log-log with a slope-1 guide.** delta spans six decades
   (1e-7 to 0.07). On linear axes every case except the largest delta would sit at the origin. The linearity shows
   as slope 1 (and A2's `gap/delta` values converge).
6. **"Same colour scale".** The mixed entries, their pole part and their archimedean part share one scale, as asked.
   G and its prime-free part share a second scale. The diagonal (about 2.5) is 20 times the largest mixed entry,
   so a single scale would show the mixed block as blank.
7. **Lane A2's output prints D to 6 digits** (`D = 0.693147`). That is fine for reading, but not for re-summing the
   zero side: `cos(gamma D)` at `gamma ~ 500` turns the rounding into errors of 1e-10. The first version of the
   comparison panel disagreed with the certified errors at M >= 300 for this reason. The script now uses the exact
   `D = log r`, and the floating curves reproduce every certified error above 1e-14. This is not an error in lane
   A2 (its certified numbers use exact D), but anyone re-summing from the printout will hit it.
8. **Lane A2's script cannot be imported.** It runs its whole measurement (~100 s) at module level.
   `bridges.a2()` parses its source and executes only the definitions and the cheap setup (Sections 0, 2 and 3
   setup, plus function definitions). It skips the check loops, the measurement loop and the zeros section. This
   takes 4.5 s and reproduces A2's numbers exactly (checked). It depends on the script's section markers
   (`head("1. CONSISTENCY`, `head("2. TEST`, `head("4. STRUCTURE`, `print_gram((2,), 2`) and raises if they change.
   A `main()` guard in that script would make this unnecessary.
9. **Step 3 uses lane B1**, which landed while this lane ran (`notes/rtp-round-1/lane-B1.md` sections 1 and 2). The
   caption states Yoshida 1992 Theorem 1 (positivity for `phi` supported in `[-log 2/2, log 2/2]`, about the pole
   plus archimedean form) and Bombieri 2000 Theorem 12 (lower bound `(log(1/|I|) - log^+ log(1/|I|) - O(1)) ||F||^2`,
   O(1) unspecified; log 2 is not his range). It also records B1's note that the archimedean part alone is not
   positive there. Two observations from the figure (floating, one test function; not claims):
   - the archimedean contribution to the bump's form value carries the logarithmic self-energy: it is positive for
     small delta and negative past delta ≈ 0.135;
   - the total falls to 9.7e-3 at `delta = log 2/2` and to 3.4e-4 near `delta = 0.625`, and stays positive for this
     one bump through a near-cancellation of pole and archimedean parts.
   A single positive diagonal entry proves nothing about positivity on the space.
10. **Step 7 discs are nested only after recentring.** The discs at K = 1, 2, 3 concern different unknowns (`t_2`,
    `t_3`, `t_4`). In place they are not nested: the Petersen K = 3 disc is not inside the K = 2 disc. Recentred on
    their MaxEnt (Burg) centres they are nested, because the radius is non-increasing. Both views are drawn. In both
    examples the truth lies on the edge at K = 3 and the disc is a point at K = 4 (four atoms, singular window).
11. **Step 7 cartoon: what exposes the pair.** In the toy (Gaussian wave packets, one dominant toy zero) the
    off-line pair adds an off-diagonal term proportional to `cosh(beta Δy) cos(Δphi)` to a unit diagonal. Two
    packets at the same centre in log u cannot expose it (cosh = 1, so the block is positive semidefinite). They must
    be separated in log u by enough that `cosh(beta Δy) |cos Δphi| > 1`. This is a property of the cartoon, consistent
    with metric-as-state.md 7.2 ("invisible to every family of test functions whose transforms vanish at that
    pair"), not a statement about zeta.
12. **Ground-state observation (Step 1, recomputed, not a claim).** The minimal even eigenfunctions at x = 13, 25,
    50 nearly coincide as functions of log u: a bump of full width at half maximum 0.51 (floating), well inside every window. This agrees with
    A1's certified intrinsic overlap 0.9989 between x = 13 and x = 50 at N = 60. Their coefficients decay by 12
    orders within the first 20 to 30 modes.
13. **Window convention.** As A2 notes, the test-function window is `log u in [-L/2, L/2]`, and `[0, L]` is the
    support of `q` in the dilation variable. `s0_line` draws the windows as the support of `q`, and the captions say
    which variable is meant.
14. **Environment.** matplotlib was not installed; I installed matplotlib 3.11.2 from PyPI. Three SVGs have their
    dense fills rasterised inside the SVG (lines and text stay vector) to keep the package at 14 MB.
