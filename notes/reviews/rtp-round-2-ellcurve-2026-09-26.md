# REFUTE review: RTP round 2, lane E (weight two: L(E, s) through the dilation window; H-RATE)

Reviewer: `claude:opus` (adversarial REFUTE lane). Date: 2026-09-26.
Subject: `notes/rtp-round-2/ellcurve/astra-proofs.md` (author `codex:gpt-6-astra`, 2026-09-26; lane finished 13:05),
statements E1–E5, the section "Numerical checks for the blind lane", and the five candidate claim rows proposed for
shard 08j. State reviewed: the working tree after the lane finished (git not run; the session's last checkpoint commit
is `8fe4af1`). Driver source hash `380016e6…d75aa9` equals the lane's `checks/source_manifest.sha256`.

Nothing here assumes RH. Zeros enter only in the blocks labelled COMPARISON STEP (the first-zero-error fit in
`scratch_rtp2_ell_fits.py`, which reads the lane's `COMP` lines; PARI ordinates, approximate). No lane file, script,
output, shard or `db/` row was edited; lane D's files were only read. `zst/` was not touched: the byte-identity reruns
compile the committed driver into a temporary directory and link `zst/build/libzst.a` read-only.

## Inputs read

| file | what it is |
|---|---|
| `notes/rtp-round-2/ellcurve/astra-proofs.md` (all), `astra-brief.md`, `progress.txt` | the report under review, its brief |
| `notes/rtp-round-2/brief.md` | round-2 conventions, game rules, output protocol |
| `zst/tools/rtp2_ellcurve.c` (eigenpair certificate, parity, prime terms: lines 270–450), `zst/tools/rtp2_ellcurve_run.sh`, `zst/Makefile` rule `build/rtp2_ellcurve` | the lane's driver and run script |
| `outputs/rtp2_ellcurve_*.txt` (all 26; parsed, not only sampled), `checks/{byte_reproducibility,final_check_count,source_manifest.sha256,recheck_11a1_x100_N200}.txt`, `checks/runlogs/`, `checks/points/point_11a1_N200_x13.txt` | outputs and evidence |
| `notes/rtp-round-2/dirichlet/astra-proofs.md` (structure, D1, D6), `progress.txt`, `outputs/rtp2_dirichlet_{D-4,D-3,D5}_*` | lane D (unfinished; read only) |
| `notes/rtp-round-1/lane-A1.md` §0; `outputs/rtp1_a1_axisN_x13.txt:240`, `outputs/rtp1_a1_axisN_x25.txt:297`, `outputs/rtp1_a1_axisx_ccm_N60.txt:70–71` | round-1 zeta numbers the lane quotes |
| `notes/zeta-spectral-triples/ellcurve/report-ell.md` §3 (items 1–3), `astra-review.md` F1–F11 | H-RATE as posed; formula sheet (F2 functional, F3 Loewner data, F5 weights, F8 shift) |
| `zst/include/zst.h` (weil data model, `zst_ell_ref`) | data model |
| `notes/reviews/rtp-round-1-2026-09-24.md` (format; C2; C12(iii) item 5; line 651), `scratch_rtp1_prolate.py` | previous review, the prolate comparison |
| `refs/src/2511.22755/mc2arXiv.tex` lines 1216–1330 (section 7, "Outlook") | the asymptotic `1 - chi ~ (2^14/3) sqrt2 pi^5 e^{-4 pi lambda^2 + 9 log lambda}` (1325–1326), the "educated guess" (1261–1270) |

## Scripts written by this review (`notes/reviews/`, deterministic)

| script | checks | what it does, independently of the lane |
|---|---|---|
| `scratch_rtp2_ell_rerun.py` | 6 | compiles the committed driver into a temp dir; reruns six cheap cases of the run script with the script's arguments; `cmp` against the committed files |
| `scratch_rtp2_ell_ab.py` | 18 | the elliptic Loewner data from scratch in mpmath (40 digits): `a_p` by brute-force point counting on the general Weierstrass model, Lucas recurrence, weights `-t_m log p/p^m`; archimedean + conductor part rederived from the multiplier `h_C(t) = log(C/4pi^2) + 2 Re psi(1+it)` via the digamma series (identity shift `s = log C - 2 log 2pi - 2 gamma - 2 log(1 - e^{-L})`, half of the full-line even pairing); own quadrature, own blocks, `eigsy` minima and parity. No zst code, no lane script |
| `scratch_rtp2_ell_fits.py` | 101 | parses the `EIG`/`COMP` lines of the seven axis-x files; audits every parity flag against the two block minima; fits of the **global** minimum against `x`, `sqrt x`, `sqrt(x/C)`, `x/log x`, `log x`, `x^p` (free `p`); three-parameter `a + b ln z - k z`; joint fits with a common slope in `sqrt(x)/C^alpha` (alpha profiled), with and without a common prefactor, with and without 37a1's odd (global) minimum as a third conductor; sub-range slopes with standard errors; residual autocorrelation; COMPARISON STEP error fit; shape check on lane D's N = 60 and 120 files (read only) |
| `scratch_rtp2_ell_kernels.py` | 15 | E1 Mellin identity; E1 Hankel identity (direct oscillatory quadrature and DLMF 10.22.43 with both candidate exponents); prediction constants; imported `x^{9/2}` slope; zeta slopes from the certified A1 numbers; E2/E5 algebra (`T*`, `S_max`, zero at `e T*`, action `A`) |
| `scratch_rtp2_ell_controls.py` | 2 | sign-change frequency `t0` of `h_C` (x-independent) against the H-RATE crossing `h_C(T*) = log x`; control inertia from all `CONTROL` lines; the `C > 4 pi^2 e^{2 gamma}` lemma against the 389a1 control |

Total: 142 checks, 0 failures. Runtime: rerun 78 s wall (6 jobs); `scratch_rtp2_ell_ab.py` 123 s; the rest seconds.

## Table of checks

| item | verdict | script | decisive check |
|---|---|---|---|
| E1 (predictions E1a/E1b; Mellin and Hankel constants) | **MINOR** | `scratch_rtp2_ell_kernels.py` | Mellin identity and the Hankel identity `(C/4pi^2)^s Gamma(1+s)/Gamma(1-s)` hold (quadrature agrees to < 1e-4 relative; DLMF exact); **the stated DLMF exponent `mu = 2s` is wrong, it is `mu = 2s+1`** (with `mu = 2s` DLMF gives -10.99 instead of 5.344 at s = -0.6). `8pi/ln10 = 10.9150108`, 3.2909996, 2.9171594, and 5.3863535 for `x^{9/2}e^{-4pi x}` on 13–50 reproduced. "Zeta leakage" is a gloss: CCM quote a prolate eigenvalue defect (Fuchs), not an `eps` law |
| E2 (Weyl surplus; measured determinant minima) | **MINOR** | `scratch_rtp2_ell_kernels.py`, `scratch_rtp2_ell_fits.py` | `T* = 2pi sqrt(x/C)`, `S_max = 2 sqrt(x/C)`, zero at `e T*`, `N* = sqrt(x/C) log x` exact. Measured `N_sat/N*` = 0.66–1.35; drifts 1.08 → 1.30 for 11a1; 11a1 and 14a1 both `N_sat = 10` at x = 50, so the conductor dependence of `N_sat` is not resolved |
| E3 (driver, 26 outputs, 25809 checks, parity, x = 100 / N = 420) | **VALID** | `scratch_rtp2_ell_rerun.py`, `scratch_rtp2_ell_ab.py`, `scratch_rtp2_ell_fits.py` | **6/6 byte-identical** (11a1/14a1 spectra, 389a1 record, 11a1 and 37a1 axis N at x = 13, the N = 200 point at x = 13); 26 files, 25809 checks, 0 failed recounted; independent `(a_n, b_n)` agree to 1e-30 (12 values) and `epsE`, `epsO`, parity at (x, N) = (13, 1/2/3/20) for 11a1, 14a1, 37a1 to 1e-12 relative (6 cases); 101 parity flags consistent with the block minima; x = 100 `N_sat` = 18 (full/E/O) and the 4.945 % N-tail read from the file |
| E4 (tables, fits) | **MINOR** | `scratch_rtp2_ell_fits.py` | every fit row reproduced to the printed digits (5 per-curve rows, the shared-slope table, the three-parameter table, the error fit). Defects: the 37a1 rows of the cross-object and endpoint-slope tables use the **even block, not the global (odd) minimum**; the shared-slope test compares only `alpha = 0` with `alpha = 1/2`; the six-knot N = 120 three-parameter rows are unconstrained (design condition ≈ 440); zeta `N_sat` 134 at x = 25 is the full-window argmin (even block 144, round-1 C2) |
| E5 (verdict) | **MINOR** | `scratch_rtp2_ell_fits.py`, `scratch_rtp2_ell_controls.py` | H-WINDOW-ONLY rejected on the tested range (robust). `sqrt x` shape resolved for 11a1 on 13–100 (free power 0.505, 10 %-RMS window 0.469–0.542). **Conductor exponent only bracketed**: best `alpha` 0.572 (0.47–0.67) with two curves, 0.578 (0.54–0.61) with 37a1's odd minimum added, 0.59–0.60 (0.47–0.73) with a common prefactor. `8 pi` OPEN: k/8pi window 0.905–1.035 (11a1, N = 200), sub-range slopes 10.07–11.15 digits per unit z, residual lag-1 autocorrelation 0.78. Control inertia does not bear on the rate |
| Numerical checks for the blind lane | **VALID** | `scratch_rtp2_ell_ab.py`, `scratch_rtp2_ell_controls.py` | the three `eps` cards, `N_sat = 10`, control inertia (1,0,60)/(1,0,59) and minima −1.78617585006, −0.669967821062, slope 0.2951601 = 10.45172 per `sqrt(x/11)` and the COMPARISON card are the file values; x = 13 values independently recomputed |
| (a) conductor discrimination | see E4/E5 | `scratch_rtp2_ell_fits.py` | shape yes, conductor exponent to ±0.1–0.15 only; not `1/2` specifically |
| (b) certified `eps` of the carrying block; 37a1 parity | see E3/E4 | `scratch_rtp2_ell_fits.py`, `scratch_rtp2_ell_ab.py` | fits and rank-zero tables use the global minimum at every knot; 37a1 parity certified and independently reproduced (odd at x = 13, N = 1 and 20); two tables nevertheless report 37a1's even block as its rate |
| (c) control inertia vs the offered explanation | see E5 | `scratch_rtp2_ell_controls.py` | neutral: identical inertia (1 even, 0 odd negative) at x = 13 for 11a1, 14a1, 37a1 and chi_-4, whose rates span 0.18–1.32 digits per unit x; the symbol's negative part ends at an x-independent `t0` |
| (d) zeta rate quotes | correct | `scratch_rtp2_ell_kernels.py` | 5.33922 (13–25) and 5.378566 (13–50) from the certified A1 values 2.85407e-59 (N = 200), 2.42562e-123 (N = 260) and the review's certified 2.80881e-258 (N = 420); prolate 5.3863535 = round-1 "5.39" (review: 5.386) |

**Tally: E1–E5: 1 VALID (E3), 4 MINOR (E1, E2, E4, E5), 0 INVALID. Candidate rows: 2 VALID, 3 MINOR, 0 INVALID.**

---

## E1. Predictions and constants — MINOR

*Checked.* The Mellin identity `int_0^inf e^{-2 pi u/sqrt C} u^s du/u = (sqrt C/2pi)^s Gamma(s)` (s = 0.7, 2.3, to 1e-20).
The Hankel identity for `K_C(v) = (2pi/sqrt C) sqrt v J_1(4pi sqrt(v/C))`: after `t = 4 pi sqrt(v/C)` the integral is
`(C/16pi^2)^s int_0^inf J_1(t) t^{2s} dt`, and DLMF 10.22.43 (`int t^{mu-1} J_nu dt = 2^{mu-1} Gamma((nu+mu)/2)/Gamma((nu-mu)/2+1)`)
with **`mu = 2s + 1`** gives `(C/4pi^2)^s Gamma(1+s)/Gamma(1-s)` exactly, on the strip `-1 < Re s < 1/4` the lane states
(that strip is `-1 < mu < 3/2`, which confirms `mu = 2s+1`). The report says `mu = 2s`; with that value DLMF returns
−10.99, 3.62, 0.739 at s = −0.6, −0.3, 0.1 against the true 5.344, 2.122, 0.783 (direct oscillatory quadrature agrees
with the identity to 6e-5, 1.5e-7, 4e-11 relative; the integrals are conditionally convergent). The result is right;
the citation step is mis-stated.

The constants are right: `8pi/ln10 = 10.9150108`, per `sqrt x` 3.2909996 (C = 11) and 2.9171594 (C = 14);
`4pi/ln10 = 5.4575054`; the local rate `5.4575054/sqrt(Cx)`; the imported `x^{9/2}` slope 5.3863535 on 13–50. The
internal consistency of E1b is good: the Fourier parameter CCM use is `gamma = 2 pi lambda^2` (mc2arXiv.tex, `wop1`),
and `1 - chi ~ e^{-2 gamma} = e^{-4 pi x}`; the lane's `c_E = 4 pi sqrt(x/C)` is the same construction for the order-one
Hankel kernel, so `e^{-2 c_E} = e^{-8 pi sqrt(x/C)}` is the like-for-like analogue. Ledger items 1–4 (the E2 scale,
the `p^m` versus `p^{m/2}` normalisation, Mellin kernel versus `rho`, the single-conductor degeneracy) are correct; item 2
is a normalisation clarification (arithmetic versus unitary Satake roots; F5 already says so), not an error in the brief.

*Defect 2 (wording).* E1a: "CCM §7 prints the zeta leakage `const x^(9/2) exp(-4 pi x)`". What CCM print
(mc2arXiv.tex:1325–1326) is Fuchs's asymptotic for the eigenvalue defect of the `n = 4` prolate function,
`1 - chi(lambda) ~ (2^14/3) sqrt2 pi^5 e^{-4 pi lambda^2 + 9 log lambda}`; the link to the Weil minimizer is the
"educated guess" of lines 1261–1269, which CCM call "the main remaining obstacle". The lane does say the transfer is
heuristic; the word "leakage" should not stand for a statement about `eps`.

## E2. Resolution prediction and measured determinant minima — MINOR

The algebra is exact (`scratch_rtp2_ell_kernels.py` (4)): with `N = T log x/(2pi)` and the positive-ordinate Weyl count
`(T/pi) log(sqrt C T/(2 pi e))`, the surplus is maximal at `T* = 2 pi sqrt(x/C)` with value `S_max = 2 sqrt(x/C)`,
vanishes at `e T*`, and `N* = sqrt(x/C) log x` (2.788, 4.853, 8.340, 13.885 for 11a1 at 13, 25, 50, 100). The brief's
`2 x log x` is correctly rejected. The `1.7 N*` pilot numbers 5, 8, 14, 24 are correct arithmetic.

The measured part is weaker than the candidate row says. `N_sat` values are small integers (1–18), so the ratio
`N_sat/N*` carries a quantisation error of ±0.5/N* (±18 % at x = 13 for 11a1, ±25 % at N = 2). The ratios are 1.08,
1.24, 1.20, 1.30 (11a1), 0.81, 0.93, 1.35 (14a1), 0.66, 1.13, 0.88 (37a1). The 11a1 sequence drifts upward; the 14a1
and 11a1 values at x = 50 are both 10, so the data do not see the conductor in `N_sat` at all. "Of order `N*`, far below
`2 x log x`" is supported; "tracks `sqrt(x/C) log x`" is not established.

## E3. Driver, outputs, parity, the x = 100 extension — VALID

*Byte identity.* Six cases of `rtp2_ellcurve_run.sh`, with the script's own arguments, rerun from the committed source
compiled into a temporary directory: `11a1_spectra_x13`, `14a1_spectra_x25`, `389a1_record`, `11a1_axisN_x13`,
`37a1_axisN_x13` and `checks/points/point_11a1_N200_x13.txt`: **all identical** (`scratch_rtp2_ell_rerun.py`).

*Counts.* 26 output files, each with exactly one `# checks:` line, summing to 25809, all `0 failed`.

*Independent recomputation* (`scratch_rtp2_ell_ab.py`; no zst code). Point counts give 11a1 `a_p` = −2, −1, 1, −2, 1, 4;
14a1 −1, −2, 0, 1, 0, −4; 37a1 −2, −3, −2, −1, −5, −2 for p ≤ 13. The reviewer's `(a_n, b_n)`, n = 0..3, at x = 13
agree with the 30-digit `AB` lines to 3e-30 or better (all 24 numbers). The block minima:

| curve | N | epsE (review) | epsO (review) | parity | lane |
|---|---|---|---|---|---|
| 11a1 | 3 | 2.439478342233e-6 | 2.990070940342e-4 | even | 2.43947834223e-6, 0.000299007094034 |
| 11a1 | 20 | 8.451334497792e-7 | 1.649704087169e-4 | even | 8.45133449779e-7, 0.000164970408717 |
| 14a1 | 2 | 2.34714132383e-5 | 2.073647052646e-3 | even | 2.34714132383e-5, 0.00207364705265 |
| 14a1 | 20 | 5.727537128503e-6 | 9.84774984053e-4 | even | 5.72753712850e-6, 0.000984774984053 |
| 37a1 | 1 | 0.444699197675 | 0.02232712188442 | **odd** | 0.444699197675, 0.0223271218844 |
| 37a1 | 20 | 0.204824297127 | 0.01328242527418 | **odd** | 0.204824297127, 0.0132824252742 |

All agree to 1e-12 relative (the printed digits). This also confirms that the regularised functional of F2 with the
shift `log C - 2 log 2pi - 2 gamma - 2 log(1 - e^{-L})` is exactly the multiplier form of `h_C`, which the lemma of E5
uses.

*Parity.* The driver intersects two independent certificates per block (`zst_block_min` bracket and the Rump/deflation
eigenpair, `rtp2_ellcurve.c:409–425`) and declares parity only when the intersected balls are ordered. Every one of
the 101 axis-x knots used in fits has its parity flag consistent with the printed block minima; 11a1 and 14a1 are even
at every knot, 37a1 odd at every knot x ≥ 4 (N = 60 and 120) and even at x = 2, 3. `even_simple = 0` for 37a1 at x = 3
(even parity) is a failure of the stronger even-simple certificate, not of parity; the lane does not claim otherwise.

*x = 100.* `SAT` lines give `N = 18` for full, even and odd blocks, unique over 1..420; `epsE(200)/epsE(420)` =
6.15767339764e-27/5.86752032195e-27 = 1.04945; the 2000-bit recheck file reproduces the N = 200 point to every printed
digit. The COMPARISON errors at x = 100 (2.2e-23) sit far above the 1e-38 radius assigned to the PARI ordinate; they are
labelled approximate, as they must be.

## E4. Tables and fits — MINOR

*Reproduced to the printed digits* (`scratch_rtp2_ell_fits.py`): all five per-curve rows (slope, RMS, max), the shared
slope table (2.874362 / 0.2290725; 10.11247 / 0.08568873), the three-parameter table (every `b`, `k/8pi`, RMS, and the
fixed-`k` rows), the COMPARISON error fit (0.6435573 / 0.1471212), the 37a1 odd slopes, the lane-D and zeta slopes.

*Defect 1 (37a1 is reported through the wrong block in two tables).* The cross-object table lists 37a1 under
`epsE at 13/25/50` = 0.2033, 0.00639, 9.64e-6 with 0.1252 and 0.1169 digits per unit x; the final-N slope table gives
37a1 `E digits/sqrt(x/C)` = 6.55, 8.29, 7.59. These are the even block, which does not carry the minimum. The global
(odd) minimum gives 0.1812055 (13–25), 0.1276575 (25–50), 0.1450244 (13–50) digits per unit x, i.e. **9.4853, 9.3733,
9.4184 digits per unit `sqrt(x/37)`** (4.74, 4.69, 4.71 per unit `S_max`). The provenance cell "E block; 37a1 global O"
flags the mismatch but leaves a non-comparable number in a comparison table.

*Defect 2 (the conductor test is a two-point test).* See E5 and (a) below. The shared-slope table must report the
profiled exponent.

*Defect 3 (unconstrained fits shown without warning).* The N = 120 rows of the three-parameter table fit three
parameters to six knots spanning z = 1.09–1.51 (11a1) and 0.96–1.34 (14a1); the design matrix has condition number
≈ 440 and the fitted `k/8pi` are 0.56 and 2.02. These rows carry no information on `k`.

*Defect 4 (zeta row).* "N_sat at 13,25,50 = 56,134,352" are the full-window argmins; the round-1 review (C2) found the
even block's argmin at x = 25 to be 144. The elliptic column is full/E/O; the zeta cell should say which.

The remaining tables (resolution, tails, COMPARISON, Schur envelopes, Rayleigh cancellation, complete control spectra,
individual prime-power terms, phase-space normalisation) are transcriptions of certified file values or arithmetic on
them; spot checks (11a1 k = 49 term 4.08e-18 = 0.36 eps at N = 60; zeta 5.3e-106 = 3.0e10 eps; the conductor shift
−1.14840858453 − (−1.38957064134) = 0.24116 = log(14/11); lane-D values 3.55108899176e-14, 5.39464993971e-30,
1.25308864637e-19, 0.0987740569268 found in `outputs/rtp2_dirichlet_*`) pass.

## E5. Verdict — MINOR

*H-WINDOW-ONLY rejected on the tested range: correct and robust.* Resolved elliptic rates are 0.18–0.37 digits per unit
x against 5.46 (or 5.39 with the zeta prefactor); at x = 50 the window-only law would put `eps` near 1e-250, the
certified N = 420 value is 9.1e-18. The N-tails (1.8 %, 1.0 %, 4.9 %) cannot close a gap of 230 digits.

*The `sqrt x` shape: resolved.* For 11a1 on 13–100 (28 knots, N = 200) a free power `log10 eps = a - s x^p` has its
best fit at **p = 0.505** (RMS within 10 % of the minimum for 0.469 ≤ p ≤ 0.542); RMS 0.122 at p = 1/2 against 0.729 at
p = 1, 0.499 for `x/log x`, 0.801 for a power law in x. On 13–50 at N = 60: p = 0.512 (0.446–0.578) for 11a1, 0.456
(0.397–0.516) for 14a1, 0.462 (0.351–0.575) for 37a1's odd minimum. On 13–25 the shape is not resolved (best p = 0.28
for 11a1 and 1.08 for 14a1 at N = 120), which the lane's ledger item 9 records.

*(a) The conductor dependence: bracketed, not resolved.* With one conductor per curve, `sqrt x` and `sqrt(x/C)` are the
same fit (ledger item 4); the only conductor information is the ratio of the two curves' `sqrt x`-slopes,
3.07221/2.67651 = 1.1478 at N = 60 (1.1782 at N = 120), against `sqrt(14/11)` = 1.1282 and `ln 14/ln 11` = 1.1006. The
lane's test compares a common slope in `sqrt x` (`alpha = 0`) with a common slope in `sqrt(x/C)` (`alpha = 1/2`). With
the exponent free (common slope in `sqrt(x)/C^alpha`, separate intercepts):

| data | best alpha | RMS at best | alpha with RMS ≤ 1.1 × min | RMS at alpha = 0 / 1/2 / 1 |
|---|---|---|---|---|
| 11a1 + 14a1, N = 60, 13–50 | 0.572 | 0.0814 | 0.472–0.672 | 0.229 / 0.0857 / 0.178 |
| + 37a1 (odd, global), N = 60, 13–50 | 0.578 | 0.0795 | 0.544–0.613 | 0.715 / 0.115 / 0.380 |
| 11a1 + 14a1, common `b ln z - k z` | 0.591 | 0.0808 | 0.472–0.731 | 0.229 / 0.0855 / — |
| + 37a1, common `b ln z - k z` | 0.604 | 0.0789 | 0.511–0.731 | 0.715 / 0.0889 / — |

So the data exclude "no conductor" (`alpha = 0`) and `alpha = 1`, and admit `alpha = 1/2`, but they prefer 0.57–0.60 and
do not single out 1/2. Two conductors (11 and 14, whose square roots differ by 13 %) cannot separate a conductor law
from any other curve-to-curve difference (the two curves also differ in every `a_p` and in the number of bad primes).
The lane had a third conductor in hand and did not use it: 37a1's certified odd minimum, which gives 9.27–9.49 digits
per unit `sqrt(x/37)` and, pairwise, `alpha` = 0.578 (against 11a1) and 0.580 (against 14a1). It is a different sector
(the minimiser is odd; a central zero), so it is corroboration, not a test. The rank-zero curves 15a1, 17a1, 19a1, 20a1,
21a1 were skipped for want of reference zeros; `eps` does not need zeros (only the model and the conductor), so the
decisive conductor test was available within the lane's budget.

*The constant `8 pi`: OPEN, and the data constrain it weakly.* 11a1 at N = 200: `k/8pi` free = 0.971, but any value in
0.905–1.035 is within 10 % of the best RMS; at N = 60, 0.825–1.060 (11a1) and 0.735–0.950 (14a1). Sub-range slopes per
unit z are 10.70 ± 0.12 (13–25), 10.32 ± 0.15 (25–50), 10.08 ± 0.10 (50–100), but 10.07 ± 0.17 (13–32), 11.15 ± 0.12
(32–64), 10.23 ± 0.10 (64–100): the local rate does not converge monotonically, it oscillates beyond its standard
errors. The residuals of the `k = 8 pi` fit have lag-1 autocorrelation 0.78 and five sign runs over 28 knots (a dip of
−0.30 digits at x = 59–61): the RMS values are descriptive, not noise estimates, and no confidence statement on `k` can
be read off them. The lane's "compatible, not determined" is the right status; "favors the optimized-Hankel prediction
over the bare squared-Mellin-tail constant" is supported only for 11a1 at N = 200 (RMS 0.124 against 0.403) and at
N = 60 (0.090 against 0.173).

*(c) The controls do not support the mechanism; they are neutral.* The negative part of the elliptic symbol
`h_C(t) = log(C/4pi^2) + 2 Re psi(1+it)` ends at the **x-independent** frequency `t0` = 1.847 (C = 11), 1.625 (14),
0.923 (37); the H-RATE scale is the x-dependent crossing `h_C(T*) = log x`, at T* = 6.818, 9.463, 13.390, 18.940 for
C = 11 and x = 13, 25, 50, 100 (within 0.2 % of `2 pi sqrt(x/C)`). The control inertia is governed by `t0` (one or two
negative modes, growing like log x), not by `T*`. At x = 13 the controls of 11a1, 14a1, 37a1 and chi_-4 all have inertia
(1 negative even, 0 negative odd), while the resolved rates over 13–25 are 0.375, 0.311, 0.181 and 1.318 digits per unit
x; the 389a1 control is positive definite (minima 2.176, 3.626 ≥ `h_389(0)` = 1.133) and its full form has an O(1)
minimum 1.640. The lane itself says the controls do not display the residual and that positivity of a control does not
establish a rate; the causal paragraph's "the experiments support concentration kinematics after incorporating the gamma
factor, conductor…" rests on the fits and the Weyl algebra only, and should say so.

*Lane-D dependence.* "Lane D's pole-free degree-one examples already have conductor-scaled linear-x behavior" was
written while lane D's x = 50 runs were pending. It holds on lane D's resolved N = 120 data on 13–25: best power
p = 1.05, 1.00, 1.02 for q = −4, −3, 5 (RMS of the x-fit 0.034, 0.024, 0.041 against 0.29, 0.35, 0.22 for `sqrt x`;
`scratch_rtp2_ell_fits.py`, last block, on `outputs/rtp2_dirichlet_{D-4,D-3,D5}_axisx_ccm_N{60,120}.txt`). Lane D's N = 60 files to x = 50 are
not resolved at the top of the range for q = 3, 4 (`N_sat` is already 30 and 41 at x = 25; the N = 60 fits on 13–50
give best powers 0.68 and 0.28 with RMS 0.69 and 1.04 digits even for `sqrt x`) and must not be used for shape. The sentence needs the provenance.

*The lemma (control shift and lower bound): correct.* The conductor enters F2 only through `(s/2) q(0)`; `a_n` gains
`log C` for every n, `b_n` (q = sin, q(0) = 0) nothing, so each block shifts by `log C · I`. The control is the
multiplier form of `h_C` (confirmed above by the independent recomputation), `Re psi(1+it) ≥ psi(1) = -gamma` by the
digamma series, so the control is positive definite on every window and every Fourier truncation once
`C > 4 pi^2 e^{2 gamma}` = 125.234.

*(d) Zeta quotes.* Correct. 5.33922 (13–25) and 5.378566 (13–50) follow from the certified A1 values 2.85407e-59
(x = 13, N = 200, `outputs/rtp1_a1_axisN_x13.txt:240`), 2.42562e-123 (x = 25, N = 260, `…x25.txt:297`) and the review's
certified 2.80881e-258 (x = 50, N = 420, review line 651); the imported prolate slope 5.3863535 is the round-1
review's 5.386 ("5.39" in `obs:rtp-round-1-reading`(iii)); the bare exponent 5.4575. The zeta Rayleigh parts
(1.622046, −1.530054, −0.0919921; `rtp1_a1_axisx_ccm_N60.txt:70–71`) and `eps = 1.75e-116` are the x = 50, N = 60 CCM
values; at N = 60 zeta is far from resolved (`N_sat` = 352), so the "matched x = 50, N = 60" table compares a resolved
elliptic form with an unresolved zeta form. It is labelled "matched N", which is accurate, but the 3.0e10-eps
statement about zeta's k = 49 term is an N = 60 statement only (round-1 C3).

*Parity-window row.* At x = 2, 3 the 37a1 minima are 1.69/1.30 (even) against 3.80/2.23, and the 389a1 minimum at
x = 13 is 1.640; `sqrt(x/C)` = 0.23, 0.28, 0.18. These are O(1) minima at windows far below the conductor scale: their
parity is not the parity of a near-null vector and says nothing about the central zero. Ledger item 7's "rank
positivity is not a theorem of odd minimal parity on every short window" is true but only in this vacuous regime.

## Numerical checks for the blind lane — VALID

The three `eps` cards are the file values (`EIG` lines), the parity column matches, and the 11a1 x = 13 values are
recomputed independently above (N = 3 and 20; the card's N = 200 value lies in the certified file, which reruns
byte-identically). `N_sat = 10` at x = 50 (unique over 1..420), control inertia (1,0,60)/(1,0,59) and minima
−1.78617585006, −0.669967821062 (`rtp2_ellcurve_11a1_axisx_ccm_N60.txt`), slope 0.2951601 digits per unit x = 10.45172
per `sqrt(x/11)`, and the COMPARISON card (2.23555751598e-14, ratio 2449.97727515) are the file values.

## Verdict lines

VERDICT E1: MINOR — the Hankel identity is right but the DLMF 10.22.43 step is mis-stated (mu = 2s+1, not mu = 2s; with mu = 2s DLMF gives −10.99 instead of 5.344 at s = −0.6), and "CCM §7 prints the zeta leakage" must say that CCM quote Fuchs's eigenvalue defect of the n = 4 prolate function, linked to the minimizer only through the "educated guess" (mc2arXiv.tex:1261–1269, 1325–1326).

VERDICT E2: MINOR — the Weyl-surplus algebra is exact, but the measured N_sat/[sqrt(x/C) log x] ratios (0.66–1.35, quantised at ±0.5/N*, drifting 1.08→1.30 for 11a1; 11a1 and 14a1 both 10 at x = 50) show only that N_sat is of order sqrt(x/C) log x, not that it tracks it or sees the conductor.

VERDICT E3: VALID

VERDICT E4: MINOR — every fit row reproduces, but the 37a1 rows of the cross-object and endpoint-slope tables report the even block instead of the global (odd) minimum (correct: 0.1812/0.1450 digits per x, 9.485/9.418 per sqrt(x/37)), the shared-slope test omits the profiled conductor exponent (best 0.572, 10 %-RMS window 0.47–0.67), the six-knot N = 120 three-parameter rows are unconstrained, and zeta's 134 is the full-window argmin (even block 144).

VERDICT E5: MINOR — H-WINDOW-ONLY rejected and the sqrt x shape resolved (free power 0.505, window 0.469–0.542, 11a1 on 13–100), but "H-RATE: a common slope in sqrt(x/C)" overstates the conductor evidence (two conductors fix the exponent only to 0.47–0.67, best 0.57; with 37a1's odd minimum 0.54–0.61, best 0.58), the control inertia is neutral rather than supporting, and the lane-D sentence needs its provenance (resolved N = 120 data on 13–25 only).

VERDICT num:rtp2-ellcurve-window-rate: MINOR — the numbers are right; the row must state the scale as sqrt(x)/C^alpha with alpha bracketed to 0.47–0.67 by two conductors (11, 14), 1/2 admissible but not singled out, and must not list 37a1's even-block rate as its rate.

VERDICT obs:rtp2-gamma-concentration-action: VALID

VERDICT num:rtp2-ellcurve-resolution: MINOR — replace "track sqrt(x/C) log x with order-one factors" by "are of order sqrt(x/C) log x (ratios 0.66–1.35), far below 2 x log x; the conductor dependence of N_sat is not resolved (11a1 and 14a1 both 10 at x = 50)".

VERDICT lem:gamma-control-shift-and-lower-bound: VALID

VERDICT num:rtp2-ellcurve-parity-window: MINOR — the parities are right (reproduced independently for 37a1 at x = 13), but the even 37a1 minima at x = 2, 3 and the odd 389a1 minimum at x = 13 are O(1) (1.3–1.7) at sqrt(x/C) ≤ 0.28; the row must say that these parities are not those of near-null vectors.

## Corrections to apply

1. **E1, Hankel step.** Replace "by [DLMF 10.22.43](https://dlmf.nist.gov/10.22.E43) with mu=2s and nu=1, after
   substituting t=4 pi sqrt(v/C)" by: "by DLMF 10.22.43 (`int_0^inf t^(mu-1) J_nu(t) dt = 2^(mu-1)
   Gamma((nu+mu)/2)/Gamma((nu-mu)/2+1)`, valid for `-nu < Re mu < 3/2`) with mu=2s+1 and nu=1, after substituting
   t=4 pi sqrt(v/C)".
2. **E1a, first paragraph.** Replace "CCM §7 prints the zeta leakage `const x^(9/2) exp(-4 pi x)` in
   `refs/src/2511.22755/mc2arXiv.tex:1324–1329`; transfer to the Weil minimizer is explicitly heuristic there." by:
   "CCM §7 quote from Fuchs the eigenvalue defect of the n = 4 prolate function, `1 - chi(lambda) ~ (2^14/3) sqrt2 pi^5
   lambda^9 exp(-4 pi lambda^2) = const x^(9/2) exp(-4 pi x)` (`mc2arXiv.tex:1325–1326`); its relevance to the Weil
   minimizer rests on the 'educated guess' of lines 1261–1269, which CCM call the main remaining obstacle."
3. **Resolution table and candidate row `num:rtp2-ellcurve-resolution`.** Replace "determinant minima track
   sqrt(x/C) log x with order-one factors, not 2x log x" by: "determinant minima are of order sqrt(x/C) log x (ratios
   0.66–1.35 over three curves and x = 13–100; 1.08, 1.24, 1.20, 1.30 for 11a1), far below 2 x log x; with integer
   N_sat ≤ 18 the conductor dependence is not resolved (11a1 and 14a1 both have N_sat = 10 at x = 50)".
4. **Cross-object table, 37a1 row.** Replace the row by
   `| 37a1 | 1,3,4 | 0.0121747434397 | 8.14692310352e-5 | 5.24270827475e-8 | 0.1812055 | 0.1450244 | global minimum = odd block; the even block (0.2033, 0.00639, 9.64e-6) does not carry it |`.
   **Final-N endpoint slope table, 37a1 rows:** add the global-minimum rates per unit `sqrt(x/C)`: 9.48530 (13–25),
   9.37331 (25–50), 9.41837 (13–50), and label the existing `E` columns "even block (not the minimum)".
5. **Shared conductor-scaled slope table.** Add the rows: "free exponent, common slope in sqrt(x)/C^alpha: best alpha
   0.572, RMS 0.0814, alpha with RMS ≤ 1.1 × min 0.472–0.672 (32 points); with 37a1's odd global minimum added:
   0.578, RMS 0.0795, 0.544–0.613 (48 points); with a common b ln z − k z prefactor: 0.591 (0.472–0.731) and 0.604
   (0.511–0.731)". Change the caption to "a two-conductor test: it excludes alpha = 0 and alpha = 1, it does not single
   out alpha = 1/2".
6. **Three-parameter table.** Add under it: "The N = 120 rows (six knots, design condition number ≈ 440) do not constrain
   k. For N = 60 and N = 200 the values of k/8pi with RMS within 10 % of the optimum are 0.825–1.060 (11a1, N = 60),
   0.735–0.950 (14a1, N = 60), 0.905–1.035 (11a1, N = 200). Residuals are strongly correlated (lag-1 autocorrelation
   0.78 for 11a1, N = 200, k = 8pi); RMS values are descriptive."
7. **Zeta row of the cross-object table.** Replace "56,134,352" by "56,134,352 (full-window argmin; even block 144 at
   x = 25, round-1 review C2)".
8. **E5, "NUMERICAL verdict from the two-curve x≤50 comparison".** Replace "H-RATE receives quantitative support: a
   common slope in sqrt(x/C), with separate curve intercepts, has RMS 0.08569 digits, versus 0.22907 for a common slope
   in sqrt(x). Both have three fitted parameters." by: "The sqrt x shape is resolved (free power 0.505, window
   0.469–0.542, for 11a1 on 13–100). The conductor dependence is bracketed, not resolved: a common slope in
   sqrt(x)/C^alpha has its best fit at alpha = 0.572 (RMS 0.0814; alpha = 1/2 gives 0.0857, alpha = 0 gives 0.2291),
   with alpha between 0.47 and 0.67 inside 10 % of the best RMS. Two conductors (11, 14) cannot distinguish a conductor
   law from other curve-to-curve differences; 37a1's odd global minimum, a third conductor in a different sector, gives
   alpha = 0.58 pairwise."
9. **E5, "NUMERICAL reading of the controls".** Append: "Control inertia does not track the rate: at x = 13 the controls
   of 11a1, 14a1, 37a1 and chi_-4 all have one negative even and no negative odd eigenvalue, while their resolved rates
   over 13–25 are 0.375, 0.311, 0.181 and 1.318 digits per unit x. The negative part of the elliptic symbol ends at the
   x-independent frequency t0 = 1.847, 1.625, 0.923 (C = 11, 14, 37); the H-RATE scale is the x-dependent crossing
   h_C(T*) = log x. The controls are neutral evidence for the mechanism."
10. **E5, "SHARPENED causal conclusion".** Replace "lane D's pole-free degree-one examples already have conductor-scaled
    linear-x behavior" by "lane D's pole-free degree-one examples, at resolved N = 120 on 13–25, are linear in x (best
    power 1.05, 1.00, 1.02 for q = −4, −3, 5; lane D unfinished at the time of writing)".
11. **Candidate row `num:rtp2-ellcurve-parity-window`.** Append: "At x = 2, 3 (37a1) and x = 13 (389a1) the minima are
    O(1) (1.30–1.69) at sqrt(x/C) ≤ 0.28; these parities are not those of near-null vectors."
12. **Candidate row `num:rtp2-ellcurve-window-rate`.** Replace "H-RATE scale supported on the stated curves and ranges"
    by "sqrt x shape supported (11a1 13–100, 14a1 13–50); conductor exponent bracketed 0.47–0.67 by two conductors;
    8pi not determined (k/8pi 0.905–1.035 at N = 200)".

## Recommendation for shard 08j

1. **What the weight-two experiment settles.** With the same window `[0, log x]`, the same Fourier basis and the same
   Loewner structure, the resolved rate of `eps_N` is 5.38 digits per unit x for zeta and 0.25–0.30 (13–50) for 11a1
   and 14a1, with a different functional shape (`x` against `sqrt x`, the latter resolved over 13–100). The rate is
   therefore **not kinematic in the window**: `obs:rtp-round-1-reading`(iii)'s question is answered negatively for the
   window/Loewner structure alone. This is the one conclusion of the lane that is both robust and new.
2. **What it points to, without settling.** The rate is organised by the functional-equation data (gamma degree and
   conductor): per unit of the phase-space variable `S_max` (`x` for zeta, `x/q` for primitive characters,
   `2 sqrt(x/C)` for weight two) every object measured so far gives 4.3–5.4 digits against the bare 5.46. This is the
   right thing to register as an OPEN hypothesis (H-CONCENTRATION-TRANSFER, `log eps = -2A + O(log A)` with
   `A = 2 pi S_max`; the algebra is exact and reviewed), not as a finding. In this sense the rate is "kinematic" in the
   L-function's gamma factor and conductor, while arithmetic supplies the cancellation (every elliptic Rayleigh
   decomposition cancels an O(1) gamma-plus-conductor part against an O(1) signed prime sum).
3. **What must not go into the shard.** "The window scale is `sqrt(x/C_E)`" as a numerical finding: the data give
   `sqrt x` for the shape and `C^{-alpha}`, alpha ≈ 0.47–0.67, for the conductor. The coefficient `8 pi` (the fits
   admit 0.9–1.04 × 8pi and the residuals are structured). The archimedean-only controls as evidence for the mechanism
   (neutral). Parity statements at windows with `sqrt(x/C) < 1`.
4. **Next experiment, cheap and decisive for the conductor.** `eps` needs no reference zeros. Run the N = 60 CCM
   axis x (x ≤ 50, about 4 min per curve) for rank-zero curves spanning a decade of conductor (e.g. 11, 14, 15, 17, 19,
   20, 21, 24, 26, 27 and one or two near 100), with Weierstrass models checked by point counting against the conductor
   (bad primes and reduction types from the singular fibres). Fit the common exponent alpha with separate intercepts;
   report the profile. Only after alpha is fixed does comparing the slope with `8 pi` mean anything. The first-zero
   comparison can be added later where PARI data exist.
5. **Registration.** Register `lem:gamma-control-shift-and-lower-bound` (VALID) and
   `obs:rtp2-gamma-concentration-action` (VALID as OPEN / conditional); register `num:rtp2-ellcurve-window-rate`,
   `num:rtp2-ellcurve-resolution` and `num:rtp2-ellcurve-parity-window` only with corrections 3, 11 and 12. The
   proposed replacement for `obs:rtp-round-1-reading`(iii) is acceptable after replacing "weight-two results favor
   sqrt(x/C)" by "weight-two results are linear in sqrt x, with a conductor exponent between about 0.47 and 0.67".
