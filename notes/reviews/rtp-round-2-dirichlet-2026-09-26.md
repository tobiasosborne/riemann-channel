# REFUTE review: RTP round 2, lane D (a real Dirichlet `L(s, chi)` through the dilation-window pipeline)

Reviewer: `claude:opus` (adversarial REFUTE lane). Date: 2026-09-26. Orchestrator: `claude:fable-5.1`.
Subject: `notes/rtp-round-2/dirichlet/astra-proofs.md` (author `codex:gpt-6-astra`, 2026-09-26), written against
`notes/rtp-round-2/dirichlet/astra-brief.md` and `notes/rtp-round-2/brief.md`; driver `zst/tools/rtp2_dirichlet.c`,
run script `zst/tools/rtp2_dirichlet_run.sh`, outputs `outputs/rtp2_dirichlet_*.txt` (52 files), scratch under
`notes/rtp-round-2/dirichlet/checks/`.

Nothing here assumes RH or GRH. Zeros of `L(s, chi)` enter only section 12 of `scratch_rtp2_dirichlet_refit.py`
(labelled COMPARISON: `gamma_1` tested as an alternative organiser of the slopes). No lane file, output, driver or
fixture was edited; no git command was run. The driver was recompiled from source into the session scratchpad
(not `zst/build/`) for the byte check.

## Status of the subject: PARTIAL, and what is missing

The lane was stopped by the codex usage limit (`lane.log`, 13:40:47). The report ends inside D6. What exists and
what does not:

| item | state in the report | missing |
|---|---|---|
| D1, D2 | complete | nothing |
| D3 | complete | nothing (see the D3 defects below) |
| D4 | the run table still reads as a plan ("planned files", "x=50 extension is attempted") | a completion statement. Actual state: 47 of 52 output files are complete, 47,691 driver checks, 0 failed. The five files `outputs/rtp2_dirichlet_D{8,-7,12,21,13}_axisN_x50.txt` stop after `EIG`/`CONTROL` at `N = 420`: no `RAY` table at `N = 420`, and so no generic-builder cross-check or Rayleigh-sum check at `x = 50`; no `REFERENCE` line; no `COMP` lines (5 x 5 = 25 secular-root comparison sets: `N = N_sat, 80, 160, 260, 420`); no `# checks:` line. Their certified eigenvalues are present and no `CHECK FAIL` line was printed before the stop |
| D5 | tables for 5 of 10 characters at `x = 50` | `x = 50` rows (eigenvalues, slopes 25–50 and 13–50, fits) for `D = 8, -7, 12, 21, 13`, although their certified eigenvalues are in the files; COMPARISON and Rayleigh rows for these five at `x = 50`; "digits lost" for the fixed-`N = 60` protocol at `x = 50` (marked "pending") |
| D6 | "Interim verdict from the completed 13–25 sweep (x=50 audit pending)" | the final verdict using 13–50; the comparison with D1b; the parity analysis |
| closing sections | absent | "Numerical checks for the blind lane" and "What this changes in the notebook" (the runner's completion signal). A draft of both exists only as unexecuted text inside `checks/finalize_report.py` and is not part of the record |
| candidate claim rows | none proposed | the report proposes no claim ids. The draft in `finalize_report.py` touches `obs:rtp-round-1-reading`(iii), `lem:bordering-interval` and `num:rtp-dilation-channel` |

## Inputs read

The lane report (all 338 lines), both briefs, `progress.txt`, `lane.log`, the driver (all 593 lines), the run
script, `checks/reference.c`, `checks/first_zero_prefix.py`, `checks/generate_references.py`,
`checks/finalize_report.py`, `checks/bytecheck.sh` with its logs, `checks/final_eigenvalue_fits.txt`,
`checks/preliminary_fits.txt`, all 52 output files (parsed in full by the scripts below), `zst/include/zst.h`
(data model, `zst_weil_dirichlet`), `zst/src/blocks.c`, `zst/src/dirichlet.c` (constructor comments),
`zst/Makefile`, `zst/tests/data/dirichlet_ref.txt`, the formula sheet F1–F18
(`notes/zeta-spectral-triples/ellcurve/astra-review.md`), `notes/rtp-round-1/lane-A1.md` sections 0–1,
`notes/reviews/rtp-round-1-2026-09-24.md` (format; C12(iii); registration verdicts),
`notes/rtp-round-2/ellcurve/astra-proofs.md` sections E1, E2, E4 (scaled-slope tables) and E5,
`refs/src/2511.22755/mc2arXiv.tex` section 7 (lines 1290–1340), and the lane transcript `astra.stdout` (only to
check that D1 was written before the first run: D1a at line 12676, first driver run at line 13549).

## Scripts written for this review (under `notes/reviews/`; deterministic)

| script | what it does, independently of the lane |
|---|---|
| `scratch_rtp2_dirichlet_refit.py` (output saved as `scratch_rtp2_dirichlet_refit.out`) | parses every `axisN` output. (1) completeness of each file; (2) and (13) the finite-`N` tail of `eps_E(N)`: monotonicity, last ratios, local log-log exponent, a three-point power-tail extrapolation; (3) slopes 13–25, 25–50, 13–50 and `q x slope` for all ten characters (including the five incomplete files, from their certified `EIG` lines); (4) the three-point fit `log eps = a + b log(x/q) - c x/q`, with two sensitivity variants (tail-extrapolated values; previous sampled `N`); (5) fixed `c = 4 pi`; (6) power law `slope ~ q^-p` and through-origin fits against `1/q`, `1/sqrt q`, `1/log q`; (7) parity at `q = 8`; (8) `N_sat` against D1b; (9) the `X = 1` control shift `log(q2/q1)`; (10) pooled least squares over all 30 final-`N` points; (11) zeta with `c = 4 pi`; (12) COMPARISON: `gamma_1` as an alternative organiser |
| `scratch_rtp2_dirichlet_mpmath.py` | check (e): `(a_n, b_n)` for `L(s, chi_D)` rebuilt from F2, F3, F5, F6, F8, F16 by direct mpmath quadrature of the defining integrals (not the closed forms F13–F15 that libzst uses), Kronecker symbol from sympy, blocks in the `zst/src/blocks.c` convention, minimal eigenvalues by `mpmath.eigsy` (45 digits). Floating, compared with the driver's printed certified values |
| `scratch_rtp2_dirichlet_prolate.py` | check of D1's source prefactor against Slepian's asymptotic: exact sympy algebra, and a Nyström computation of the sinc-kernel concentration eigenvalues |

## Table of checks

| # | check | result |
|---|---|---|
| 1 | CCM prefactor: `mc2arXiv.tex` lines 1325–1327 print `(2^14/3) sqrt2 pi^5 e^{-4 pi lambda^2 + 9 log lambda}` | confirmed. Independently: Slepian's `1 - lambda_n(c) ~ 4 sqrt(pi) 8^n c^{n+1/2} e^{-2c}/n!`, halved (the compressed Fourier eigenvalue `chi` has `chi^2 = lambda`), at `c = 2 pi lambda^2`, `n = 4`, equals the CCM expression exactly (sympy ratio 1). Nyström check of the Slepian leading term, `n = 0`: ratio 0.865, 0.920, 0.942, 0.954 at `c = 4, 6, 8, 10` (tends to 1) |
| 2 | D1 recorded before the runs | yes (`astra.stdout` lines 12676 and 13549) |
| 3 | D1b algebra (`T* = 2 pi x/q`, zero at `e T*`) | correct |
| 4 | D1c / D2c: `X = 1` control spectra at fixed `kappa` differ by `log(q2/q1)` | exact to 10 digits for all 8 pairs (`x = 13`, `N = 200`), e.g. `D = -20` vs `-4`: 1.6094379124 against `log 5` = 1.6094379124 |
| 5 | D2 (A1.1' without poles): `w_e`, `w_o`, `d_e`, `d_o` against `zst/src/blocks.c` | agree; A1.1'(4) wording correction ("gain of MaxEnt over the truth") is right |
| 6 | D2b: `Re psi(3/4 + it/2) - Re psi(1/4 + it/2) = pi / cosh(pi t)` | correct (reflection `psi(1-z) - psi(z) = pi cot(pi z)` at `z = 1/4 + it/2`) |
| 7 | D2c: digamma series and the `D = -20` positivity bound | correct: bound `log(20/pi) + psi(3/4)` = 0.7651 > 0; measured control minima 1.159, 1.061, 0.993 at `x = 13, 25, 50` decrease towards it. For `q = 7` the bound is -0.285 and the control does turn indefinite at `x = 50` (`minE = -0.0572`, file `D-7_axisN_x50`), as the bound allows |
| 8 | (e) independent `(a_n, b_n)` and `eps` | `x = 13`, `N = 20`, `D = -4, 5, -20`: all printed `a_n, b_n` (`n = 0..3`, 30 digits) agree to 1e-30 or better; `eps_E` and `eps_O` agree to relative 1e-13 (all 12 printed digits): `D = -4`: 6.46618822590e-14; `D = 5`: 2.90753234209e-12; `D = -20`: 0.0996075078912. `x = 50`, `N = 80`, `D = -20`: `a_n, b_n` to 5e-30, `eps_E` 1.32646394485e-10 and `eps_O` 4.67675007096e-7 in all printed digits |
| 9 | (d) byte identity of the two cheapest run-script cases, from a fresh compile of `zst/tools/rtp2_dirichlet.c` | `--D -4 --mode axisx --N 60 --xmax 50 --prec 2700 --fixedL 1` and the same for `--D 5`: both byte-identical to `outputs/rtp2_dirichlet_D{-4,5}_axisx_fixedL_N60.txt` (`cmp`). The lane's own `bytecheck.sh` only compares two runs of the same binary at `Nmax` 40, 40, 3 with each other, not with the released outputs |
| 10 | completeness and check counts | 47/52 files end with `# checks: ... 0 failed` (47,691 checks); the five `x = 50` files named above have no end line, no `CHECK FAIL` line |
| 11 | x = 50 determinant audit table (N_sat full/even/odd, min logdet, pivot bits) | all ten rows reproduce from the `SAT` and `pivot_accuracy_bits` lines |
| 12 | reported slopes and three-point fits | all reproduce to the printed digits |
| 13 | reference zeros: interval Newton in `reference.c` | a valid interval-Newton certificate of a unique zero of Hardy's `Z` in the final box (derivative ball excludes 0; Newton image strictly inside the box); first-positive-index certificates pass for all ten (435–1369 boxes, as reported) |
| 14 | fixed-`L` parity claims (`D = 5`, `X = 47`: even min `-1.18909219699e-12`, odd min `-0.000121535867110`; odd-minimum cutoffs 3, 7, 8, 9, 27, 47) and the `even_simple = 0` knots | reproduced from the outputs |
| 15 | "within 0.7% of 4 pi" (`progress.txt`, D6) | true for `D = -4` (+0.65%) and `-3` (+0.52%), the two characters it was written for; false for the family: 3 of 10 characters (`-4, -3, 21`), range -3.03% (`D = 13`) to +8.32% (`D = -20`) |

## Verdicts

### D1 (predictions; the source prefactor check): VALID

The prefactor audit is right and now independently anchored (check 1): the CCM constant is exactly half of
Slepian's `n = 4` concentration defect at `c = 2 pi lambda^2`, so the `x^{9/2} e^{-4 pi x}` form is the Fuchs/Slepian
asymptotic of the compressed Fourier eigenvalue, not a transcription accident. D1a's preferred prediction
`eps ~ A_D (x/q)^{b_D} e^{-4 pi x/q}` was written before any run (check 2) and is the prediction the data support
(D6). D1b's algebra is right; its qualitative content (N_sat falls with `q`) is borne out, quantitatively only for
small `q` (D6 below). D1c's monotonicities are right and the identity shift is exact in the outputs (check 4).
Nothing to correct. (`scratch_rtp2_dirichlet_prolate.py`, `scratch_rtp2_dirichlet_refit.py` section 9.)

### D2 (pole-free Schur/Loewner lemma; control monotonicities): VALID

D2 is A1.1' with the pole data removed; the algebra does not see where `(a_n, b_n)` come from, and the column
derivatives match `blocks.c` (check 5). The wording correction to A1.1'(4) is right: `log(s_e(beta_ME) s_o(beta_ME)) -
log(s_e(0) s_o(0)) >= 0` is the gain of the MaxEnt point over the truth. D2b and D2c are correct (checks 6, 7). The
subtraction convention matters for D2b/D2c: the window functional equals the `L`-independent distribution
`-integral_0^infinity (g - g(0)) rho + const g(0)` on test functions supported in `[0, L]`, because the tail `T(L)` in
the shift (F8) cancels `integral_L^infinity`; only then is it a Fourier multiplier. The lane asserts Plancherel
without saying this; it is true. D2c is sharp in the right direction: the `q = 7` odd control, whose multiplier
infimum is negative, becomes indefinite at `x = 50`.

### D3 (driver; parity certification; reference zeros): MINOR

What holds. The form builder is exactly `zst_weil_dirichlet; zst_weil_ab`, and an independent quadrature
reproduces it (check 8). Parity is certified properly: each block minimum has two enclosures (`zst_block_min`, and
Rump plus deflated positive-definiteness in `eig_min`); the driver checks that they overlap, intersects them, and
decides parity by strict ball comparison of the intersections. This is sound (both enclose the same minimum; if
`zst_block_min` had enclosed a non-minimal eigenvalue the overlap check would fail). The `N_sat` "certificate"
is a certified unique argmin over `1..Nmax` only, as stated. Output is byte-reproducible (check 9).

Reference zeros. The "certified Hardy-Z refinement" is certified: `reference_zero` runs interval Newton on FLINT's
ball `acb_dirichlet_hardy_z` and its derivative, accepts only a strict inclusion, and `first_zero_prefix.py`
separately excludes zeros of `Z` on `[0, gamma - 2^-10]` and shows `Z' != 0` on the final neighbourhood, so `gamma`
is the first positive zero of `Z` (a critical-line statement; nothing about off-line zeros is assumed or needed). The
comparison step is properly labelled: the zero is read after all eigenpairs, printed under `# COMPARISON STEP`, and
enters only `|z_1 - gamma_1|` and its ratio to `eps`.

Defects.
1. The production driver `#include`s lane scratch: `zst/tools/rtp2_dirichlet.c` line 16 includes
   `../../notes/rtp-round-2/dirichlet/checks/reference.c`, and the `zst/Makefile` rule depends on it. Deleting or
   editing `checks/` changes or breaks the driver. Move `reference.c` next to the driver (e.g.
   `zst/tools/rtp2_reference.c`) or say in D3 that it is part of the driver's source.
2. `zst/tests/data/dirichlet_ref.txt` was extended (D = -7, -20, 21; one 40-digit seed each), as the brief allows.
   Its appended header says "First-index identification from sign scan (not a certified global zero count)". That is
   stale: `first_zero_prefix.py` certifies the first positive index for all ten characters. The driver's
   `REFERENCE ... index=PARI_or_sign_scan` label likewise does not point to that certificate. The three new records
   carry only `zero 1`; any use of `zst --chi D` needing more zeros for these `D` will find none.
3. `bytecheck.sh` tests determinism of one binary at small `Nmax`, not reproduction of the released outputs. The
   stronger check (fresh compile, released files) passes here (check 9); D3/D4 should say which one was done.

The independent quadrature (check 8) also covers a large window: `D = -20`, `x = 50`, `N = 80` (run as
`python3 notes/reviews/scratch_rtp2_dirichlet_mpmath.py -20 50 80`, 3.8 min): `a_n, b_n` agree to 5e-30,
`eps_E = 1.32646394485e-10` and `eps_O = 4.67675007096e-7` agree in all 12 printed digits (relative 3e-12, 5e-13).

### D4 (runs; the x = 50 audit): MINOR

Complete: all `x = 13` and `x = 25` axis-N runs (20), all axis-x runs (20 CCM, 2 fixed-`L`), and axis-N `x = 50` for
`D = -4, -3, 5, -20, -8`, i.e. 47 files, 47,691 checks, 0 failed (check 10). Incomplete: axis-N `x = 50` for `D = 8,
-7, 12, 21, 13` (the lane's "five secular-root comparison sets"); for these the certified eigenvalues at `N = N_sat,
80, 160, 260, 420` and the controls exist, and the Rayleigh decomposition, its generic-builder cross-check, and the
COMPARISON lines do not. The `x = 50` audit table (determinant argmins, logdet, pivot accuracy, Schur half-widths)
is complete for all ten and reproduces (check 11). The run script regenerates exactly the incomplete jobs with
`DS="8 -7 12 21 13" PHASES=x50 zst/tools/rtp2_dirichlet_run.sh` (about 50 minutes wall per job in parallel,
from the run logs: eigenpairs end at 2750–2825 s, the complete jobs needed a few minutes more).

The defect is in the text: D4 still reads as a plan and nowhere states which files are complete; the reader must
infer it from `progress.txt`. Correction 3 below.

### D5 (tables, slopes, conductor-scaled exponents): MINOR

The numbers are right: every reported slope and fit parameter reproduces (check 12), and the per-character 13–25
slopes run from 0.213882 (`D = -20`) to 1.777118 (`D = -3`) digits per unit `x`, 13–50 from 0.2410 to 1.7942
(`D = -4`: 1.336481; `D = -3`: 1.794198). Four defects.

(a) *Certified eps at saturated N?* The `eps` values are certified balls. "Saturated" is not certified and is not
the determinant argmin (the lane says so: `eps(N_sat)/eps(final)` is up to 231). Since the blocks are nested
compressions, `eps_N` is nonincreasing in `N` (Cauchy interlacing; all 30 sequences are monotone), so every
final-`N` value is a certified **upper** bound on the infinite-`N` value, and a slope between two upper bounds bounds
nothing. The tail itself (section 13 of the refit): the last sampled step changes `eps` by at most `log10(1.1517)`
= 0.061 digits (`D = -3`, `x = 50`), and for most `(D, x)` the local exponent `-d ln eps / d ln N` falls step by
step; but it is **not** yet falling for `D = -4` and `5` at `x = 25` and `D = +-8` at `x = 50` (0.067 -> 0.124,
0.131 -> 0.136, 0.085 -> 0.123, 0.106 -> 0.134), so those four points are not demonstrably in a convergent tail.
Consequence, quantified: a further 0.1 digit at `x = 50` moves a 13–50 slope by 0.003 digits per `x` (0.06 in
`q x slope` at `q = 20`). The rate conclusions of D6 survive this; the per-character exponent `c` at the 1% level
does not (item (c)). "Saturated" in the D5 prose should be replaced by "largest tested N" (the tables already say
"final N").

(b) *Missing rows.* The five incomplete characters' `x = 50` eigenvalues are certified and printed, yet their slopes
are "NA". From the `EIG` lines: 13–50 slopes 0.672791 (`D = 8`), 0.750872 (`-7`), 0.444141 (`12`), 0.242710 (`21`),
0.410546 (`13`). `D = 13` is anomalous: its 25–50 slope (0.409726) is below its 13–25 slope (0.412255), the opposite
of every other character; this is what drives its fit to `b = -0.22`, `c/(4 pi) = 0.970`.

(c) *"Conductor-scaled exponents within 0.7% of 4 pi"* (`progress.txt`, D6 line). The three-point fit has three
parameters and three points: it interpolates, has no residual and no error bar, and `b` and `c` are strongly
correlated (tail-extrapolated inputs move `c/(4 pi)` by up to 0.003, `b` by up to 0.28). Per character, `c/(4 pi)`
is 1.0065 (`-4`), 1.0052 (`-3`), 1.0163 (`5`), 1.0105 (`8`), 1.0096 (`-7`), 1.0108 (`12`), 1.0832 (`-20`), 0.9988
(`21`), 0.9698 (`13`), 1.0072 (`-8`). The 0.7% statement is true of the two characters it was written for and of
`D = 21`, and false of the family; the report's own fit table already contradicts it for `D = 5` and `-20`. The
better-posed statement is pooled (section 10): with one common `c`, one power `b` per parity and one amplitude per
character (13 parameters, 30 points), `c/(4 pi) = 1.0039`, rms residual 0.043 digits, max 0.088; restricted to
`x/q >= 1` (28 points), `c/(4 pi) = 1.0019`, rms 0.036. Fixing `c = 4 pi` costs little (rms 0.051). The same pooled
model in raw `x` has rms 6.8 digits.

(d) *Floating labels.* Slopes and fits are labelled FLOATING, correctly. The zeta row "R1, x = 50, N = 360" is an
unconverged value (`N_sat = 352`; `N = 360 -> 420` lowers it by a factor 8.1), which the table half-says; the 13–50
zeta slope should be the review's 5.379 only.

### D6 (interim verdict): MINOR

*Chi-independence in raw x: REFUTED* stands, now on 13–50 and all ten characters: slopes from 0.241 to 1.794 digits
per unit `x`, against 5.379 for zeta; no finite-`N` tail of the size observed (at most 0.06 digits per sampled step)
can bridge a factor 7. VALID in substance.

*The 1/q scaling* is supported by all ten characters, not a subset. `q x slope(13–50)` lies in [4.820, 5.393]
for all ten; a through-origin fit `slope = k/q` has `k = 5.349` and rms 0.012 digits per `x`, against 0.236 for
`k/sqrt q` and 0.208 for `k/log q`; a free power law gives `slope ~ q^{-1.037}` (ten characters) and `q^{-1.024}`
with zeta at `q = 1`. The first-zero height organises the slopes 6.4 times worse (rms of log residuals 0.153 against
0.024; COMPARISON data, section 12). What is only supported by a subset is the *asymptotic* statement that the
per-unit-`x/q` rate is `4 pi/ln 10` = 5.4575: `q x slope` approaches it from below as `x/q` grows (25–50: 5.08 to
5.43), and the three characters with `x/q < 1` at `x = 13` (`q = 13, 20, 21`) are pre-asymptotic (`D = -20`:
`c/(4 pi) = 1.083`; `D = 13`: 0.970).

*Parity* enters the prefactor, not the exponent. At `q = 8` the even character is faster by 0.0266 (13–25), 0.0147
(25–50), 0.0186 (13–50) digits per `x`, and the ratio `eps(D=-8)/eps(D=8)` grows as 20.8, 43.5, 101.2 at `x = 13,
25, 50`, i.e. like `x^{1.17}`. Across the family, with `c = 4 pi` fixed, the fitted powers are `b = 0.59–1.09`
(mean 0.75) for `kappa = 0` and `1.58–2.01` (mean 1.79) for `kappa = 1`; the pooled free-`c` fit gives 0.90 and 2.03.
So `b(kappa = 1) - b(kappa = 0)` is about 1.0–1.1 in the prefactor `(x/q)^b`. This matches the difference of the
lowest even and odd prolate sectors (`c^{1/2}` against `c^{3/2}`), which D1a named without committing to which
parity goes with which; the absolute values sit about 0.25–0.3 above 1/2 and 3/2. For comparison, zeta with
`c = 4 pi` fixed gives `b = 5.0` (13–25 and 25–50), near CCM's `9/2` for the pole-constrained `h_0/h_4` sector.
These are FLOATING post-run observations (the lane's `finalize_report.py` draft proposes `b = 1 + kappa`, also post
hoc).

Defects: the section is headed "Interim" and argues from 13–25 while the tables above it carry 13–50; it does not
compare with D1b (N_sat: `1.7 x log x/q` fits `q = 3, 4` at `x = 50` within 4% — 110 vs 110.8, 80 vs 83.1 — and
overestimates by up to a factor 2.4 for `q = 20` and at small `x/q`); the "0.7%" line in `progress.txt` overstates
(D5(c)); and the closing sections are missing. The draft verdict in `finalize_report.py` is sound in substance but
must not be pasted without the corrections below. One confound the draft correctly states and the final text must
keep: conductor and prime comb change together across this family, so the experiment cannot say whether `q` acts
through the functional equation (the Poisson scale) or through the atoms.

## Verdict lines

VERDICT D1: VALID

VERDICT D2: VALID

VERDICT D3: MINOR — the driver #includes lane scratch (notes/rtp-round-2/dirichlet/checks/reference.c) into a zst tool; the appended header of zst/tests/data/dirichlet_ref.txt ("First-index identification from sign scan (not a certified global zero count)") is stale after checks/first_zero_prefix.py; the lane's byte check compares a binary with itself at small Nmax, not with the released outputs (the latter passes, this review).

VERDICT D4: MINOR — D4 still reads as a plan; state that 47/52 files are complete (47,691 checks, 0 failed) and that axis-N x = 50 for D = 8, -7, 12, 21, 13 lacks the RAY table, the REFERENCE line, all COMP lines and the end-of-run check line, while its certified EIG/CONTROL lines through N = 420 are present.

VERDICT D5: MINOR — final-N eps are certified upper bounds of the infinite-N values, not saturated values (four (D, x) points show no decreasing tail exponent yet; effect on slopes <= 0.003 digits/x); x = 50 rows for five characters are omitted though certified; "conductor-scaled exponents within 0.7% of 4 pi" holds for D = -4, -3, 21 only (per-character c/(4 pi) from 0.970 to 1.083); the pooled fit gives 1.004.

VERDICT D6: MINOR — raw-x chi-independence REFUTED (VALID in substance, on 13–50 and all ten characters); the 1/q law is supported by all ten characters (slope ~ q^-1.04, k/q fit rms 0.012 digits/x), its 4 pi/ln 10 limit only asymptotically; parity shifts the prefactor power by about one; the section is interim, lacks the D1b comparison and the two closing sections.

The report proposes no candidate claim ids; see the recommendation for the rows shard 08j could register once the
corrections are in.

## Corrections to apply

1. `progress.txt`, D6 line. Replace
   "fitted conductor-scaled exponents within 0.7% of 4pi; remaining x50 cases pending."
   by
   "three-point fits log eps = a + b log(x/q) - c x/q give c/(4pi) = 1.0065 (D=-4) and 1.0052 (D=-3); over all ten characters 0.970 (D=13) to 1.083 (D=-20); a pooled fit (common c, one power per parity) gives c/(4pi) = 1.004 (FLOATING); x50 comparison sets for D=8,-7,12,21,13 pending."

2. Report, D4, after the run table. Insert:
   "**NUMERICAL (completion at the stop, 2026-09-26 13:40).** 47 of 52 files are complete (47,691 driver checks, 0 failed). The axis-N x=50 files for D=8,-7,12,21,13 end after the EIG and CONTROL lines at N=420: their eigenvalues at N=N_sat,80,160,260,420 are certified (no CHECK FAIL line), but the Rayleigh table, its generic-builder cross-check, the reference zero and all COMP lines are missing. Regenerate with `DS=\"8 -7 12 21 13\" PHASES=x50 zst/tools/rtp2_dirichlet_run.sh`."
   and change "planned files" to "files (47 complete)".

3. Report, D5 extraction conventions. Replace
   "“Saturated” here means well beyond the measured determinant minimum, not a rigorous limit as N tends to infinity."
   by
   "“Final N” means the largest tested N (200, 260, 420), well beyond the determinant minimum. By interlacing eps_N is nonincreasing in N, so each final-N value is a certified upper bound on the infinite-N value, not an estimate of it. The last sampled step changes eps by at most 0.061 digits (D=-3, x=50); for D=-4 and 5 at x=25 and D=±8 at x=50 the local exponent -d ln eps/d ln N is not yet decreasing. An error of 0.1 digit at x=50 moves a 13–50 slope by 0.003 digits per unit x."

4. Report, D5 tables: add the x=50 rows for D=8,-7,12,21,13 from their EIG lines, marked "eigenvalues certified; file incomplete (no RAY/COMP)": epsE(N_sat) / epsE(420) / epsO(420) = 1.34126866389e-30 / 2.78341006540e-32 / 3.88470771085e-28 (D=8, N_sat 35); 1.27969498626e-33 / 3.36363897513e-35 / 5.95491780729e-31 (D=-7, 41); 1.99821570732e-19 / 4.27129546329e-21 / 3.54390522474e-17 (D=12, 21); 4.53750087410e-10 / 2.43317378269e-11 / 4.42617513034e-8 (D=21, 10); 4.63830885392e-18 / 2.59928813113e-19 / 1.92857049372e-15 (D=13, 21). FLOATING 13–50 slopes: 0.672791, 0.750872, 0.444141, 0.242710, 0.410546. Add the sentence: "D=13 is the only character whose 25–50 slope (0.409726) is below its 13–25 slope (0.412255)."

5. Report, D5 conductor table caption. After "This is a three-point interpolation, not a validated asymptotic expansion." add:
   "It has no residual; b and c are strongly correlated (tail-extrapolated inputs move c/(4pi) by up to 0.003 and b by up to 0.28). Pooled over all 30 final-N points with one c, one b per parity and one amplitude per character: c/(4pi) = 1.0039, rms 0.043 digits; for x/q >= 1 only, 1.0019, rms 0.036; the same model in raw x has rms 6.8 digits (`notes/reviews/scratch_rtp2_dirichlet_refit.py`, section 10)."

6. Report, D6 heading and first paragraph. Replace the heading by "## D6. Verdict" and the first paragraph by:
   "**REFUTED numerically on 13 ≤ x ≤ 50: a character-independent rate in raw x.** At the largest tested N the 13–50 even-minimum slopes run from 0.2410 (D=-20) to 1.7942 (D=-3) decimal digits per unit x (six required characters: 0.4441 to 1.7942), against 5.379 for zeta; the last sampled N step changes eps by at most 0.061 digits. The first-zero error has the same 13–50 slopes to within 0.006 digits per x where compared (13–25: within 0.009). All slopes are FLOATING post-processing of certified eigenvalues."

7. Report, D6 second paragraph. Replace "the leading scale changes approximately as 1/q." and the q=8 sentence by:
   "the leading scale is x/q for all ten characters: q × slope(13–50) lies in [4.820, 5.393]; slope = k/q fits with k = 5.349 and rms 0.012 digits per x (k/sqrt q: 0.236; k/log q: 0.208); a free power law gives q^-1.037, and q^-1.024 with zeta at q=1. The per-unit-(x/q) rate approaches 4pi/ln10 = 5.4575 from below as x/q grows (25–50: 5.08 to 5.43). Parity changes the prefactor, not the exponent: at q=8, eps(D=-8)/eps(D=8) = 20.8, 43.5, 101.2 at x=13, 25, 50 (about x^1.17); with c = 4pi fixed the fitted power of x/q is 0.59–1.09 for kappa=0 and 1.58–2.01 for kappa=1 (difference about one, as for the lowest even and odd prolate sectors). FLOATING."

8. Report, D6: add the D1b comparison: "N_sat(full) against 1.7 x log x/q at x=50: 110 vs 110.8 (q=3), 80 vs 83.1 (q=4), 60 vs 66.5 (q=5), 35/33 vs 41.6 (q=8), 7 vs 16.6 (q=20). The downward shift with q is confirmed; the coefficient 1.7 holds only for small q."

9. `zst/tests/data/dirichlet_ref.txt`, appended header. Replace
   "# First-index identification from sign scan (not a certified global zero count)."
   by
   "# First positive zero of Hardy's Z certified by notes/rtp-round-2/dirichlet/checks/first_zero_prefix.py (interval exclusion; critical-line statement only)."

10. Report, D3: add "The driver includes `notes/rtp-round-2/dirichlet/checks/reference.c` at compile time; it is part of the driver's source." (or move the file into `zst/tools/`), and replace "byte replays pass" (`progress.txt`, D4) by "three small cases rerun byte-identically with the same binary; the two fixed-L N=60 outputs reproduce byte-identically from a fresh compile (REFUTE review)".

11. Complete the two closing sections. The draft in `checks/finalize_report.py` may be used with corrections 6–8 applied; its "Numerical checks for the blind lane" block should add one `x = 13` card from item 8 of this review's check table.

## Recommendation for shard 08j

What the Dirichlet experiment decides about the dilation-channel rate (FLOATING fits of certified eigenvalues,
finite `N`, `13 <= x <= 50`):

1. The rate is not a property of the window. The same window, basis and Loewner structure give 0.24 to 1.79 digits
   per unit `x` for ten real primitive characters and 5.38 for zeta. "The primes only set the floor" is refuted in
   the raw coordinate.
2. The rate is a property of the window **measured in the conductor-normalised variable `x/q`**. One exponent
   `e^{-4 pi x/q}` (pooled `c/(4 pi) = 1.004`) with a parity-dependent power of `x/q` and a character amplitude fits
   all 30 final-`N` points to 0.043 digits rms. Zeta (`q = 1`) sits on the same law with its own power (`b = 5.0`
   near CCM's 9/2). This is what D1a predicted from twisted Poisson summation and what the sister lane E calls
   `S_max = x/q` (E5; the weight-two `2 sqrt(x/C)` is a different transform and is decided there, not here).
3. Arithmetic enters through the conductor in the exponent, through parity and the pole constraints in the power,
   and through the amplitude and the floor. The experiment does not separate the conductor from the prime comb (they
   move together), and it proves nothing about the Weil minimiser: the transfer from prolate concentration to `eps`
   remains OPEN (H-CONCENTRATION-TRANSFER in E5).
4. The Schur envelope does not follow `eps` for any character (joint half-widths 3.5 to 6.0 at the final `N` of every `(D, x)`); the
   round-1 distinction between the envelope and the small-eigenvalue channel carries over unchanged.

Proposed rows (to be written and then reviewed; no VERDICT lines are given for text that does not yet exist):
`num:rtp2-dirichlet-window-rate` (the tables of D5 with corrections 3–5, all ten characters, FLOATING rates),
`lem:weil-control-conductor-shift` (D1c/D2b/D2c: exact `log(q2/q1)` shift at fixed atoms and gamma data; odd-character
control dominates the even one by the multiplier `pi / cosh(pi t)`; positivity when `log(q/pi) + psi((kappa+1/2)/2) > 0`;
PROVED here, and consistent with lane E's elliptic analogue), and a corrected `obs:rtp-round-1-reading`(iii) replacing
"kinematic or arithmetic: undecided" by items 1–3 above.

What remains for the `x = 50` completion:
- rerun axis-N `x = 50` for `D = 8, -7, 12, 21, 13` with the unchanged script
  (`DS="8 -7 12 21 13" PHASES=x50 zst/tools/rtp2_dirichlet_run.sh`), giving the Rayleigh tables with their
  generic-builder cross-check and the 25 COMPARISON sets; no precision change is indicated (pivot accuracy 3806–3908
  of 4200 bits);
- one tail extension where the local exponent is not yet decreasing: `D = +-8` at `x = 50` and `D = -4, 5` at
  `x = 25`, to `N = 600` or more; and `D = -3, -4, 5` at `x = 50`, where the last step is the largest (0.03–0.06
  digits);
- a matched-`x/q` design for the large conductors (`q = 13, 20, 21`), whose `x/q` at `x = 13` is below 1: the
  asymptotic claim needs `x/q >= 2` at three windows, i.e. `x` up to about 100 for `q = 21` (not affordable at
  `N = 420` for small `q`, but cheap for large `q`, where `N_sat <= 10`);
- the two closing sections of the lane report, with corrections 6–8.
