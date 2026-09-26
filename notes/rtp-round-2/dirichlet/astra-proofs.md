# RTP-2 lane D: Dirichlet dilation windows

Author: `codex:gpt-6-astra`. Unreviewed research record. No RH assumption. Forms use only the generic Weil builder; reference zeros enter labelled COMPARISON steps only.

> **Completion note (`claude:opus`, 2026-09-26).** The codex lane was stopped by the codex usage limit at 13:40 on 2026-09-26, with D4–D6 PARTIAL and without the two closing sections. The five missing axis-N `x = 50` runs (`D = 8, -7, 12, 21, 13`) were then regenerated, unchanged, with `DS="8 -7 12 21 13" PHASES=x50 zst/tools/rtp2_dirichlet_run.sh`. **Sections D4, D5 (tables), D6 and the two closing sections were completed by `claude:opus` on 2026-09-26 from the lane's finished outputs after the codex lane was stopped, and the eleven corrections of the REFUTE review `notes/reviews/rtp-round-2-dirichlet-2026-09-26.md` were applied.** D1–D3 and ledger items 1–4 are astra-authored and unchanged except where a review correction applies; every such edit is marked *[claude:opus: …]*. The completion ledger below lists what changed; the verification files are in `x50-completion/`. The draft `checks/finalize_report.py` was not run and is superseded (running it would overwrite this report with uncorrected text).

## Completion ledger (`claude:opus`, 2026-09-26)

| review correction | where | what was done |
|---|---|---|
| 1 | `progress.txt`, D6 | replaced by the review's text; its closing clause "x50 comparison sets … pending" changed to "… completed after the stop" |
| 2 | D4 | the completion-at-stop paragraph inserted verbatim; "planned files" changed to "files (47 complete at the stop; 52 after the rerun)" (the review's "files (47 complete)", extended by the rerun); a completion paragraph added |
| 3 | D5 conventions | sentence replaced verbatim |
| 4 | D5 tables | superseded by the rerun: the five `x = 50` rows now come from the complete files, not from the `EIG` lines of incomplete files; all fifteen values given in the correction are identical in the complete files, and the five FLOATING 13–50 slopes are reproduced. The D=13 sentence is inserted verbatim |
| 5 | D5 fit caption | inserted verbatim (inside the generator `x50-completion/complete_d5.py`, so that it survives regeneration); the pooled numbers are reproduced on the complete outputs |
| 6, 7, 8 | D6 | heading and first paragraph replaced verbatim (6); the "1/q" and `q = 8` sentences replaced verbatim (7); the D1b comparison added verbatim (8); the rest of D6 rewritten as the final verdict |
| 9 | `zst/tests/data/dirichlet_ref.txt` | the stale header line replaced verbatim; `make -C zst check` passes afterwards (`x50-completion/make-check.txt`) |
| 10 | D3; `progress.txt`, D4 | the D3 sentence added verbatim; the `progress.txt` wording replaced verbatim |
| 11 | closing sections | written from the draft in `checks/finalize_report.py` with corrections 6–8 applied and the `x = 13` card of the review's check 8 added |

Also applied, from the review's verdict text (no replacement text given there): D5(a) "saturated" removed from the D5 prose; D5(d) the zeta `x = 50`, `N = 360` row labelled unconverged; D3 defect 3 (what the byte check tested) stated in D3. Open defects left as they are (outside this completion's remit, which excludes the driver): the driver still `#include`s `checks/reference.c` (now stated in D3); its `REFERENCE … index=PARI_or_sign_scan` label does not point to the first-index certificate; the three appended fixture records carry only `zero 1`.

## Correction ledger

1. **SHARPENED (before runs).** The same logarithmic window does not imply the same effective additive Fourier concentration parameter. Primitive conductor q introduces the Fourier scale q in twisted Poisson summation. A conductor-independent exponent in x is a hypothesis to test, not a consequence of CCM §7.
2. **PROVED (source audit).** CCM §7, `mc2arXiv.tex` lines 1324–1329, prints exactly `(2^14/3) sqrt(2) pi^5 exp(-4 pi lambda^2 + 9 log lambda)`. Thus the quoted exponent and prefactor agree with the source; in x this is `C x^(9/2) exp(-4 pi x)`. This checks the quotation, not Fuchs's theorem independently. CCM explicitly leaves the relation of its prolate ansatz to the Weil minimizer open in §8.
3. **SHARPENED.** The reference file is `zst/tests/data/dirichlet_ref.txt`. Its existing PARI values are floating 40-digit values, not certified balls. Giving them radius 1e-38 is insufficient for the requested high accuracy and is not by itself a certificate. They will supply comparison-only starting guesses, refined with certified Hardy-Z interval Newton.
4. **SHARPENED.** “Trivial set empty” means no pole directions at ±1/2 in the centred variable. Nonprincipal Dirichlet L-functions still have their usual trivial zeros. An odd minimum also makes the existing CCM sum-normalization undefined; an odd comparison must be identified as an extension, not silently sent to the even routine.

*[Items 5–9 added by claude:opus on 2026-09-26 after the runs; 5–8 follow the lane's unexecuted draft in `checks/finalize_report.py`, rechecked on the complete outputs; 9 follows the REFUTE review, D5(c).]*

5. **REFUTED numerically.** The raw-x rate is not character-independent: the 13–50 spread of the even-minimum slopes is 1.3501 digits per unit x for the six required characters (0.4441 for D=12 to 1.7942 for D=-3) and 1.5532 for all ten (from 0.2410 for D=-20). Conductor changes the leading scale; it cannot be relegated to a multiplicative amplitude in an unscaled exp(-4pi x) law.
6. **SHARPENED.** The determinant argmin is not a precision criterion for eps (eps(N_sat)/eps(final) reaches 231, D=-20, x=50). At x=50 the coefficient q N_sat/(x log x) ranges from 0.716 (D=-20) to 1.687 (D=-3); the factor 1.7 of round 1 holds only for small q.
7. **PROVED correction to A1.1'(4)** (in D2). The nonnegative structured log-determinant difference is the gain of MaxEnt over the truth, not of the truth over MaxEnt.
8. **SHARPENED.** The prime-free Dirichlet control contains log q I and need not be indefinite: for D=-20 and D=-8 it is positive definite at every tested x (for D=-20 on every window, by D2c); for D=-7, whose D2c bound is negative, it turns indefinite at x=50. Odd global minima do occur in the fixed-L partial forms, so even-only diagnostics can mislead.
9. **WITHDRAWN.** The interim `progress.txt` line "fitted conductor-scaled exponents within 0.7% of 4pi" holds for D=-4, -3 (for which it was written) and 21 only; the three-point c/(4pi) runs from 0.970 (D=13) to 1.083 (D=-20). Only the pooled statement of D6 (c/(4pi) = 1.0039) is supported.

## D1. Prediction recorded before numerical experiments

**PREDICTION D1a (OPEN: deliberately competing hypotheses).** The naive window-only hypothesis is
`eps(x) ~ A_D x^b exp(-4 pi x)`, with 5.458 digits per x asymptotically and about 5.386 over 13–50 if b=9/2. Neither the unchanged Fourier basis nor changing only mu in rho proves this hypothesis: the form also contains `log q I`, the pole constraints disappear, and the prime comb changes.

My preferred conductor-aware prediction is `eps(x) ~ A_D (x/q)^b_D exp(-4 pi x/q)` at sufficient N. The same leading exponential should occur in first-zero errors when the corresponding simple root is recovered. Reason: for a primitive character, split the twisted sum into residue classes modulo q and apply Poisson summation. The finite Fourier transform of chi is its Gauss sum times the conjugate character, so the dual dilation is `1/(q u)`. Rescaling additive coordinates by sqrt(q) restores the self-dual Fourier transform and replaces lambda by lambda/sqrt(q), hence lambda² by x/q in the concentration parameter. This is a heuristic transfer to the Weil minimizer, not an eigenvalue theorem.

Parity affects which Hermite/prolate sector is available, and removing the zeta pole constraints removes its particular h0/h4 vanishing-integral combination. Consequently b_D need not be 9/2; the unconstrained lowest even/odd prolate sectors suggest powers 1/2 and 3/2 before the Mellin map and normalization. I do not predict an exact b_D or amplitude A_D. The conductor shift alone is exactly an identity shift at fixed atoms and gamma data (and does not move eigenvectors), but changing a primitive character changes those atoms as well. Therefore it cannot be dismissed as merely a prefactor in the complete family. The already published MVP-3 values at x=13 (chi_-4: eps about 5e-14 versus zeta about 1e-59) motivate testing conductor scaling, without using any new run.

**PREDICTION D1b (OPEN, with PROVED algebra).** Use the supplied one-sided Weyl count `Z_q(T) ~ T/(2pi) log(qT/(2pi e))`. The mode surplus is
`S(T)=T/(2pi)[log x-log(qT/(2pi e))]`.
Differentiation gives its maximum at `T=2pi x/q` and its zero at `T=2pi e x/q`. Since `N=T log x/(2pi)`, the corresponding scales are `x log x/q` and `e x log x/q`. Thus, translating round 1's surplus heuristic predicts a *decrease* of N_sat with conductor, roughly `1.7 x log x/q`, not an increase. Constants and small-x shifts can depend on parity, the missing pole constraints, and the arbitrary determinant threshold. Argmin log det is not an exact convergence test for eps; final-N tails will be reported separately.

**PREDICTION D1c (OPEN).** The X=1 control includes the conductor identity shift. Its Fourier multiplier is `h_(q,kappa)(t)=log(q/pi)+Re psi((kappa+1/2+it)/2)`. Increasing q at fixed kappa shifts every eigenvalue upwards by log(q2/q1); thus negative inertia cannot increase with q on the same window and N. At fixed q,kappa,x it cannot decrease as N grows (interlacing). These monotonicities are PROVED. Exact counts are deferred to certified measurements. In particular zeta's archimedean indefiniteness does not imply indefiniteness for every Dirichlet control.

## D2. Pole-free Loewner bordering

**PROVED D2 (conditional only on finite block positive definiteness).** Let E_N and O_N be positive definite and fix a_j, j=N+1, for a real reflection-symmetric Loewner form. No assumption about its pole, prime or gamma origin is needed. For the normalized-position and logarithmic-gain assertions, assume also H-PD: the true bordered blocks are positive definite. This ensures s0>0, r>0 and a nonempty positive joint interior; it is certified at every reported positive bordering. Write b=b_true+beta. The new columns are `c_e=u_e+b w_e`, `c_o=u_o+b w_o`, with

- `w_e=(sqrt(2)/j, (1/(i+j)-1/(i-j))_(i=1..N))`, `d_e=a_j+b/j`;
- `w_o=(-1/(i-j)-1/(i+j))_(i=1..N)`, `d_o=a_j-b/j`.

For each block `s(beta)=s0+l beta-C beta²`, where `C=w^T G^-1 w>0` and `l=±1/j-2w^T G^-1 c_true`. The admissible interval is `beta*=l/(2C)` plus/minus `r=sqrt((s0+l²/(4C))/C)` when its radicand is nonnegative. The joint interval is the intersection. On its positive interior the joint maximum determinant uniquely maximizes `log s_e+log s_o`; each separate maximum is at its interval centre. The normalized truth position is `tau=-beta*/r`, with `tau²=1-s0/(s0+l²/(4C))`. The joint gain `log(s_e(beta_ME)s_o(beta_ME)/(s_e(0)s_o(0)))` is the gain of MaxEnt **over** the truth, correcting the reversed wording in A1.1'(4). The zero unconstrained column is compatible with both Loewner columns only if all old b_i vanish. For N>=1 the vectors w are nonzero; N=0 requires treating the empty odd block separately.

Proof: congruence of the bordered matrix with `diag(G,d-c^T G^-1 c)` gives positivity and determinant factorization; substitution and completion of the square give the interval formulas. Strict concavity of the logarithm of each positive, strictly concave quadratic gives uniqueness. The even zeroth entry forces b=0 for a zero column, then its remaining entries force b_i=0. These are exactly A1.1' algebra, unchanged when pole terms vanish. The absent pole directions only change the numerical input G and the control, which is now gamma plus conductor, X=1.

**PROVED D2b (additional control comparison).** At a fixed conductor and window, the odd-character archimedean form exceeds the even-character one as a quadratic form. Indeed, digamma reflection gives
`Re psi(3/4+it/2)-Re psi(1/4+it/2)=pi/cosh(pi t)>0`.
Plancherel expresses the difference of the two controls as the integral of this positive multiplier times the squared Fourier transform of the test function. Thus every nonzero finite-window function has strictly larger odd-character archimedean value, and the negative count for kappa=1 is at most that for kappa=0 in either reflection block. Character parity kappa and window reflection parity E/O are distinct notions.

**PROVED D2c (why a positive control is possible).** The gamma multiplier is minimized at t=0: the digamma series gives
`Re psi(a+ib)-psi(a)=sum_(n>=0) b²/((n+a)((n+a)²+b²)) >= 0` for a>0.
Thus `log(q/pi)+psi((kappa+1/2)/2)>0` is sufficient for positivity on every window and at every N. For kappa=1 this lower bound is `log(q/(8pi))-EulerGamma+pi/2`; it is positive at q=20 (for example, EulerGamma<1, pi>3, and log(20/(8pi))>-1/4 give a lower bound >1/4). Therefore the positive X=1 control for D=-20 is a theorem, not a failure to resolve small negative eigenvalues. For a fixed kappa the entire control spectra at different q differ by exactly log(q2/q1), which the output minima can independently check.

## D3. Driver and certification

**NUMERICAL (implementation).** `zst/tools/rtp2_dirichlet.c` retains A1's Schur quadratic, structured interval, joint MaxEnt and shifted Rump/deflation helpers. Its form builder is exactly `zst_weil_dirichlet; zst_weil_ab`; no library source or include behavior is changed. The independent local prime increment is multiplied by Kronecker(D,k), and its accumulated data are checked against the generic builder (every fixed-L knot and every final Rayleigh decomposition).

Options: `--D`, `--mode axisN|axisx`, `--x`, `--Nmax`, `--cmp N1,N2,...`, `--prec`, `--cprec`, `--N`, `--xmax`, `--fixedL 1`. Axis N automatically certifies eigenpairs at the full determinant minimizer and Nmax in addition to `--cmp`. It certifies the unique determinant argmin over the scanned range for full, even and odd blocks. This is a finite-range certificate, not an assertion about all N.

Both block minima first receive independent Rayleigh/positive-definiteness brackets from `zst_block_min`. Separate Rump eigenpair and deflated positivity certificates produce normalized eigenvectors and sharp minimum-eigenvalue balls in both blocks. Intersecting the two certificates before strict ball comparison implements `zst_parity`'s ordering criterion even when its raw brackets are broad. The `even_simple` flag records the legacy sufficient 2-epsilon gap test. At (D,x)=(21,2),(21,3),(13,3),(-8,2), for both N=60 and 120, it is zero because the odd minimum is below 2 eps_E; the two separately certified simple block minima nevertheless prove min_E<min_O, hence the actual simple-even hypothesis. This is not an odd minimum or an uncertified CCM comparison. The X=1 control includes `log |D| I`; its positive and negative counts are certified by LDL at zero. Successful nonzero pivots imply zero nullity. The Rayleigh decomposition uses the actual minimizing block.

COMPARISON uses `checks/reference.c`: identify the primitive character by checking its full residue table against Kronecker(D,n), read a starting guess from `zst/tests/data/dirichlet_ref.txt`, and refine a unique real Hardy-Z root by interval Newton using FLINT's `acb_dirichlet_hardy_z` and its derivative. Missing guesses are located by a comparison-only sign scan. The root ball is certified. A separate comparison-only audit, `checks/first_zero_prefix.py`, now certifies that it is the first positive Hardy-Z zero: interval exclusion on the preceding segment and a nonvanishing derivative throughout the final root neighborhood. All ten certificates pass at 160 bits for exclusion and 800 bits for root refinement (435–1369 interval boxes). This proves the critical-line index without assuming anything about off-line zeros; the raw output label records the original guess source. All generated reference enclosures are kept in the lane outputs; the original reference file is not overwritten with uncertified high-precision midpoints. Secular roots come from the minimizer without reference-zero input; a complete N-root list is checked for even cases. The existing CCM construction is undefined for odd minima (sum normalization zero), which is reported explicitly. No odd case is silently replaced by the even one.

Arithmetic: FLINT 3 arb balls throughout forms, LDL, eigenvalues, inertia, error differences and Rayleigh parts. Printed scalar values are rounded midpoints only when the relative ball error is smaller than their displayed precision with guard bits; otherwise the complete ball is printed. Joint MaxEnt's location and QR shift candidates are floating; the evaluated Schur values and admissibility checks are balls. Printed dIs is the certified gain at the 200-bisection point, hence a lower bound on the exact structured-MaxEnt gain. Derived slopes, ratios calculated from printed values, and fitted prefactors in `checks/summary.py` will be labelled floating. Output has no time or addresses; elapsed times are stderr only.

**NUMERICAL (pilot).** Before launching the suite, `(D,x,N)=(-4,13,40)` reproduced MVP-3: `eps_E=4.93772909768e-14`, first-zero error `1.89828037683e-12`, all 40 roots certified. The pilot completed 265 checks, zero failed. `make -C zst check` passed all existing tests.

D3 correction during validation: the inherited shifted helper needs an explicit scalar (1x1) branch; otherwise its QR-based second-eigenvalue gap is infinite. This affected the N=1 odd *control* for D=-20, not the form eigenvalue. Fixed locally in the new driver. Also `zst_block_min` sometimes returns a broad but valid minimum bracket (D=12,x=25,N=40,80). The separate Rump-plus-deflated-PD minimum certificates were already sharp and decisive. The driver now intersects the two valid certificates of each block minimum before the parity comparison; raw bracket overlap is disclosed. This uses a certified *minimum*, not an arbitrary eigenpair. Failed development outputs are retained in checks and the affected cases were rerun successfully.

Missing-reference exception authorized by the brief: `checks/generate_references.py --append` adds D=-7,-20,21 to `zst/tests/data/dirichlet_ref.txt` in its existing format. Only 40-digit comparison seeds are appended; standalone runs at 800 and 1200 bits give overlapping certified Hardy-Z root balls, retained in checks. Existing records are unchanged. This supersedes the earlier plan not to append to that file. No reference datum enters the form or its certificates.

The driver includes `notes/rtp-round-2/dirichlet/checks/reference.c` at compile time; it is part of the driver's source. *[claude:opus: REFUTE review correction 10, verbatim.]* `checks/bytecheck.sh` reruns three small cases (`Nmax` 40, 40, 3) twice with the same binary and compares the two runs; it does not compare with the released outputs. The stronger check, a fresh compile reproducing the two fixed-L `N = 60` outputs byte for byte, was done by the REFUTE review (its check 9). *[claude:opus: review D3 defect 3.]*



## D4. Runs (completed)

The run script ran all x=13 cases, then x=25, then the axis-x protocols, then x=50, with at most 12 independent processes and timings retained under `checks/runlogs/`. The requested six characters and the optional -20, 21, 13 were included, plus -8 to compare both character parities at exactly the same conductor 8. The x=50 extension ran for all ten characters, with eigenvalues at N = N_sat, 80, 160, 260, 420 to show the tail beyond the determinant minimum. All outputs are `outputs/rtp2_dirichlet_*.txt`. *[claude:opus: paragraph rewritten from the lane's plan wording into a record of what ran; content unchanged.]*



| protocol | discriminants | resolution/window | bits for LDL / eigenpairs | files (47 complete at the stop; 52 after the rerun) |
|---|---|---|---|---:|
| axis N | -4,-3,5,8,-7,12,-20,21,13,-8 | x=13, Nmax=200 | 1000 / 700 | 10 |
| axis N | same ten | x=25, Nmax=260 | 1800 / 1200 (D=12: 1400 on rerun) | 10 |
| axis N | same ten | x=50, Nmax=420 | 4200 / 2400 | 10 |
| axis x CCM | same ten | N=60, x through prime powers to 50 | 2700 | 10 |
| axis x CCM | same ten | N=120, x through prime powers to 25 | 1800 | 10 |
| axis x fixed L | -4,5 | N=60, L=log 50, cutoff 1 through 49 | 2700 | 2 |

The original low-cost stages used the development certifier before the two edge-case corrections. Both stages were rerun successfully with the final driver so all released outputs have the same check logic. D=12 at x=25 also raises eigenpair precision from 1200 to 1400 bits; the form precision stays 1800. The two development failures are preserved as `checks/development_*_failed.txt`, not counted as final successes. No precision increase has been needed for construction of a Weil form.

**NUMERICAL (completion at the stop, 2026-09-26 13:40).** 47 of 52 files are complete (47,691 driver checks, 0 failed). The axis-N x=50 files for D=8,-7,12,21,13 end after the EIG and CONTROL lines at N=420: their eigenvalues at N=N_sat,80,160,260,420 are certified (no CHECK FAIL line), but the Rayleigh table, its generic-builder cross-check, the reference zero and all COMP lines are missing. Regenerate with `DS="8 -7 12 21 13" PHASES=x50 zst/tools/rtp2_dirichlet_run.sh`. *[claude:opus: REFUTE review correction 2, verbatim.]*

**NUMERICAL (completion after the stop; `claude:opus`, 2026-09-26).** The five files were regenerated with the unchanged script, driver and precisions (`x50-completion/run.log`: exit 0 for all five). All 52 files now end with `# checks: … 0 failed`: **60,526 driver checks, 0 failed** (47,691 + 5 × 2,567). Each regenerated file has 420 `ROW` lines, the three `SAT` lines, `EIG`/`CONTROL` at N = N_sat, 80, 160, 260, 420, the 24-line `RAY` table with `RAY_TOTAL` at N=420 (the generic-builder cross-check and the Rayleigh-sum check are inside the check count), the labelled `# COMPARISON STEP` block with a certified `REFERENCE` line and five `COMP` lines (all N roots found at each N), and the end-of-run line. Consistency with the partial versions (`x50-completion/prefix_check.py`, output `prefix_check.txt`): the partial files were overwritten by the rerun, so a byte comparison of the whole shared prefix was not possible here (the earlier versions survive only in git history, which this completion did not read). Every line of them that survives in the lane transcript `astra.stdout` (39 lines: `SAT block=full`, pivot accuracy, and `EIG` at N = N_sat, 80, 160, 420 for each of the five) occurs verbatim in the regenerated files; every value the REFUTE review recorded from them (its correction 4; the x=50 audit table: N_sat full/even/odd, minimum logdet, pivot bits, joint half-width at N=420) is identical; and the review's `scratch_rtp2_dirichlet_refit.py`, rerun on the complete files (`x50-completion/review_refit_on_complete_outputs.out`), reproduces its saved output except for the five completeness lines, so every eigenvalue-derived number, including those from the N=260 values, is unchanged to the printed digits. No discrepancy was found. `checks/audit_outputs.py` passes on the complete set (793 floating/structural checks, 0 failed; `x50-completion/audit_outputs.txt`).



## D5. Results and extraction conventions

**NUMERICAL.** The primary proxy is the largest tested N at each x: 200,260,420. *[claude:opus: "saturated" removed, review D5(a).]* The driver also evaluates eps exactly at the determinant argmin; both appear in the table. “Final N” means the largest tested N (200, 260, 420), well beyond the determinant minimum. By interlacing eps_N is nonincreasing in N, so each final-N value is a certified upper bound on the infinite-N value, not an estimate of it. The last sampled step changes eps by at most 0.061 digits (D=-3, x=50); for D=-4 and 5 at x=25 and D=±8 at x=50 the local exponent -d ln eps/d ln N is not yet decreasing. An error of 0.1 digit at x=50 moves a 13–50 slope by 0.003 digits per unit x. *[claude:opus: REFUTE review correction 3, verbatim.]* Ratios against the previous sampled N quantify the remaining tail. The N_sat certificate covers integers 1..Nmax only; an argmin at 1 is left-censored and must not be fitted as an interior transition.

Every eigenvalue, reported inertia, determinant comparison, Rayleigh sum, and error difference in the raw files is obtained in ball arithmetic. Displayed values are rounded as described in D3. Slopes use `s(a,b)=(log10 eps(a)-log10 eps(b))/(b-a)` and are explicitly **floating postprocessing**, as are fitted exponents and amplitudes. `checks/summary.py` regenerates all tables from the output files. *[claude:opus: the block below is now produced by `x50-completion/complete_d5.py`, which runs `checks/summary.py` and adds the review's caption corrections and the pooled and per-character analyses.]* The reference-root ball certifies a unique zero, and the independent zero-free-prefix certificate in D3 verifies its first positive Hardy-Z index.

The old zeta output has x=50 eigenpairs only through N=360. Its existing value is retained in the extraction. Where the corrected round-1 13–50 slope is compared, I separately cite the review's already certified N=420 value (2.80881e-258; comparison error 3.0346e-254), rather than claim that it came from `rtp1_a1_axisN_x50.txt` or rerun zeta.

<!-- D5_TABLES_BEGIN -->
*[D5 tables regenerated by claude:opus on 2026-09-26 from the 52 complete outputs with `x50-completion/complete_d5.py`, which runs the lane's `checks/summary.py` and appends the analyses after "x50 determinant and precision audit".]*

### Saturation and final-N results

Eigenvalues are rounded certified-ball results. N_sat is over 1..Nmax, certified unique. Final N is a finite-resolution proxy; it is not an infinite-N certificate.

| D | x | N final | N_sat full/even/odd | epsE at N_sat | epsE final | epsO final | parity |
|---|---|---|---|---|---|---|---|
| -4 | 13 | 200 | 11/11/11 | 3.10228843498e-13 | 3.55108899176e-14 | 7.49736362617e-11 | 1 |
| -4 | 25 | 260 | 30/30/30 | 6.34913624745e-29 | 5.39464993971e-30 | 3.88258923824e-26 | 1 |
| -4 | 50 | 420 | 80/80/80 | 2.71447632755e-62 | 1.26056711373e-63 | 4.15988533034e-59 | 1 |
| -3 | 13 | 200 | 17/17/17 | 4.63730601677e-19 | 1.25308864637e-19 | 2.88150878846e-16 | 1 |
| -3 | 25 | 260 | 41/41/39 | 1.33067281669e-39 | 5.92330252137e-41 | 5.03576541872e-37 | 1 |
| -3 | 50 | 420 | 110/110/110 | 9.75722882765e-85 | 5.16001185419e-86 | 2.41802649492e-81 | 1 |
| 5 | 13 | 200 | 7/7/7 | 2.10911890230e-11 | 2.10790657667e-12 | 3.00014809680e-9 | 1 |
| 5 | 25 | 260 | 23/23/22 | 6.94290139292e-24 | 3.66818026982e-25 | 1.54653184431e-21 | 1 |
| 5 | 50 | 420 | 60/60/60 | 1.43283593401e-50 | 2.61101968035e-52 | 5.71930699218e-48 | 1 |
| 8 | 13 | 200 | 4/4/4 | 1.21057046016e-6 | 2.17699319902e-7 | 0.000143025517367 | 1 |
| 8 | 25 | 260 | 13/13/13 | 3.69906341403e-14 | 2.30737261661e-15 | 6.57100869491e-12 | 1 |
| 8 | 50 | 420 | 35/35/30 | 1.34126866389e-30 | 2.78341006540e-32 | 3.88470771085e-28 | 1 |
| -7 | 13 | 200 | 4/4/4 | 2.31119975654e-6 | 2.03745394328e-7 | 0.000177050652770 | 1 |
| -7 | 25 | 260 | 13/13/13 | 8.53449943462e-15 | 3.27263403207e-16 | 1.65324013253e-12 | 1 |
| -7 | 50 | 420 | 41/41/39 | 1.27969498626e-33 | 3.36363897513e-35 | 5.95491780729e-31 | 1 |
| 12 | 13 | 200 | 2/2/2 | 0.00173236382165 | 0.000115817314349 | 0.0379151462554 | 1 |
| 12 | 25 | 260 | 7/7/7 | 1.77690413690e-8 | 6.71343285554e-10 | 1.17534100376e-6 | 1 |
| 12 | 50 | 420 | 21/21/21 | 1.99821570732e-19 | 4.27129546329e-21 | 3.54390522474e-17 | 1 |
| -20 | 13 | 200 | 1/1/1 | 0.158693673555 | 0.0987740569268 | 1.80464336194 | 1 |
| -20 | 25 | 260 | 3/3/3 | 0.00243209532977 | 0.000267954162959 | 0.104112987818 | 1 |
| -20 | 50 | 420 | 7/10/7 | 2.76343802769e-8 | 1.19593688708e-10 | 4.12406333640e-7 | 1 |
| 21 | 13 | 200 | 2/2/1 | 0.0514183313883 | 0.0232509738349 | 0.809121815454 | 1 |
| 21 | 25 | 260 | 2/2/2 | 0.000433141563711 | 3.58458347666e-5 | 0.0141272342948 | 1 |
| 21 | 50 | 420 | 10/10/10 | 4.53750087410e-10 | 2.43317378269e-11 | 4.42617513034e-8 | 1 |
| 13 | 13 | 200 | 2/2/2 | 0.00122321454012 | 0.000402786486930 | 0.0548613049682 | 1 |
| 13 | 25 | 260 | 7/7/7 | 6.32827857151e-8 | 4.55002293950e-9 | 6.27965278425e-6 | 1 |
| 13 | 50 | 420 | 21/21/15 | 4.63830885392e-18 | 2.59928813113e-19 | 1.92857049372e-15 | 1 |
| -8 | 13 | 200 | 2/4/2 | 0.000111143598106 | 4.53702800257e-6 | 0.00271051444180 | 1 |
| -8 | 25 | 260 | 13/13/12 | 1.12249347399e-12 | 1.00380725322e-13 | 3.59244810027e-10 | 1 |
| -8 | 50 | 420 | 33/33/33 | 1.35761691174e-28 | 2.81634289669e-30 | 4.03066792841e-26 | 1 |
| zeta R1 | 13 | 200 | 56/—/— | — | 2.85407e-59 | — | 1 |
| zeta R1 | 25 | 260 | 134/—/— | — | 2.42562e-123 | — | 1 |
| zeta R1 (unconverged, N=360) | 50 | 360 | 352/—/— | — | 2.26934e-257 | — | 1 |
| zeta review | 50 | 420 | 352/—/— | — | 2.80881e-258 | — | 1 |

### COMPARISON: first root, final N

| D | x | N | error (ball) | error/eps (ball) | gamma1 |
|---|---|---|---|---|---|
| -4 | 13 | 200 | 1.36924359116e-12 | 38.5584138931 | 6.02094890469759665490251152161 |
| -4 | 25 | 260 | 2.54172642712e-28 | 47.1156878672 | 6.02094890469759665490251152161 |
| -4 | 50 | 420 | 6.60763626321e-62 | 52.4179648290 | 6.02094890469759665490251152161 |
| -3 | 13 | 200 | 4.86212210036e-17 | 388.011024953 | 8.03973715568146668171362321417 |
| -3 | 25 | 260 | 3.01497655714e-38 | 509.002629236 | 8.03973715568146668171362321417 |
| -3 | 50 | 420 | 3.03641185717e-83 | 588.450558442 | 8.03973715568146668171362321417 |
| 5 | 13 | 200 | 3.32035533794e-10 | 157.519093811 | 6.64845334472771471612327845998 |
| 5 | 25 | 260 | 7.87056999737e-23 | 214.563337089 | 6.64845334472771471612327845998 |
| 5 | 50 | 420 | 6.60361361002e-50 | 252.913207040 | 6.64845334472771471612327845998 |
| 8 | 13 | 200 | 5.37737315942e-6 | 24.7009185047 | 4.89997399700703650103830489920 |
| 8 | 25 | 260 | 7.45333904342e-14 | 32.3022774465 | 4.89997399700703650103830489920 |
| 8 | 50 | 420 | 1.03517371091e-30 | 37.1908445606 | 4.89997399700703650103830489920 |
| -7 | 13 | 200 | 2.91870117758e-6 | 14.3252375702 | 4.47573828372868313197462848719 |
| -7 | 25 | 260 | 5.74301376538e-15 | 17.5485975795 | 4.47573828372868313197462848719 |
| -7 | 50 | 420 | 6.54981873016e-34 | 19.4724189445 | 4.47573828372868313197462848719 |
| 12 | 13 | 200 | 0.000723657015974 | 6.24826279249 | 3.80462763305086509714431754004 |
| 12 | 25 | 260 | 5.38313221787e-9 | 8.01844947838 | 3.80462763305086509714431754004 |
| 12 | 50 | 420 | 3.88810152315e-20 | 9.10286248415 | 3.80462763305086509714431754004 |
| -20 | 13 | 200 | 0.0907225887304 | 0.918486002833 | 2.35893499408665604861501236977 |
| -20 | 25 | 260 | 0.000279539568020 | 1.04323651827 | 2.35893499408665604861501236977 |
| -20 | 50 | 420 | 1.36945505490e-10 | 1.14508973650 | 2.35893499408665604861501236977 |
| 21 | 13 | 200 | 0.0138214097826 | 0.594444339439 | 2.31518706430314115204629295971 |
| 21 | 25 | 260 | 2.60986873282e-5 | 0.728081449299 | 2.31518706430314115204629295971 |
| 21 | 50 | 420 | 1.95332120333e-11 | 0.802787378868 | 2.31518706430314115204629295971 |
| 13 | 13 | 200 | 0.000743221932889 | 1.84520076270 | 3.11934147900860341390159975672 |
| 13 | 25 | 260 | 1.01725521657e-8 | 2.23571447901 | 3.11934147900860341390159975672 |
| 13 | 50 | 420 | 6.39865921133e-19 | 2.46169677563 | 3.11934147900860341390159975672 |
| -8 | 13 | 200 | 1.42968317872e-5 | 3.15114470952 | 3.57615483678758907557757872996 |
| -8 | 25 | 260 | 3.67712339543e-13 | 3.66317675394 | 3.57615483678758907557757872996 |
| -8 | 50 | 420 | 1.11326486478e-29 | 3.95287401294 | 3.57615483678758907557757872996 |

### FLOATING slopes (positive digits per x)

| D | E 13–25 | O 13–25 | error 13–25 | E 25–50 | O 25–50 | error 25–50 | E 13–50 | O 13–50 | error 13–50 |
|---|---|---|---|---|---|---|---|---|---|
| -4 | 1.3182 | 1.27382 | 1.31095 | 1.34526 | 1.3188 | 1.3434 | 1.33648 | 1.30421 | 1.33288 |
| -3 | 1.77712 | 1.7298 | 1.7673 | 1.8024 | 1.77274 | 1.79988 | 1.7942 | 1.75882 | 1.78931 |
| 5 | 1.06328 | 1.02398 | 1.0521 | 1.08591 | 1.05728 | 1.08305 | 1.07857 | 1.04648 | 1.07301 |
| 8 | 0.664562 | 0.611482 | 0.654852 | 0.676742 | 0.649131 | 0.674294 | 0.672791 | 0.63692 | 0.667988 |
| -7 | 0.732849 | 0.669147 | 0.725504 | 0.759524 | 0.737738 | 0.757716 | 0.750872 | 0.715492 | 0.747269 |
| 12 | 0.436402 | 0.375721 | 0.427375 | 0.447855 | 0.420827 | 0.445652 | 0.444141 | 0.406198 | 0.439724 |
| -20 | 0.213882 | 0.103241 | 0.209273 | 0.254014 | 0.216087 | 0.252396 | 0.240998 | 0.179488 | 0.23841 |
| 21 | 0.234334 | 0.146496 | 0.226994 | 0.246731 | 0.220161 | 0.245034 | 0.24271 | 0.19627 | 0.239183 |
| 13 | 0.412255 | 0.328444 | 0.405307 | 0.409726 | 0.380508 | 0.408054 | 0.410546 | 0.363622 | 0.407163 |
| -8 | 0.637927 | 0.573138 | 0.632478 | 0.662079 | 0.638001 | 0.660756 | 0.654246 | 0.616964 | 0.651585 |
| zeta R1 (x=50 at N=360: not used) | 5.33922 | — | 5.32907 | 5.36116 | — | 5.35852 | 5.35404 | — | 5.34897 |
| zeta review | 5.33922 | — | 5.32907 | 5.39745 | — | 5.3948 | 5.37857 | — | 5.37348 |

D=13 is the only character whose 25–50 slope (0.409726) is below its 13–25 slope (0.412255). *[Correction 4 of the REFUTE review, sentence inserted by claude:opus.]* The zeta row at x=50, N=360 is not converged (N_sat=352; N=360 to 420 lowers eps by a factor 8.1), so the zeta 13–50 slope to use is the review row, 5.37857 *[review D5(d), claude:opus]*.

### FLOATING conductor scaling and polynomial fit

Fit log(eps)=a+b log(x/q)-c x/q at the three final-N samples. This is a three-point interpolation, not a validated asymptotic expansion. It has no residual; b and c are strongly correlated (tail-extrapolated inputs move c/(4pi) by up to 0.003 and b by up to 0.28). Pooled over all 30 final-N points with one c, one b per parity and one amplitude per character: c/(4pi) = 1.0039, rms 0.043 digits; for x/q >= 1 only, 1.0019, rms 0.036; the same model in raw x has rms 6.8 digits (`notes/reviews/scratch_rtp2_dirichlet_refit.py`, section 10). *[Correction 5 of the REFUTE review, inserted by claude:opus; the pooled numbers are reproduced on the complete outputs below.]* b_fixed fixes c=4pi and uses endpoints; A_fixed uses x=50.

| D | q × slope 13–50 | b fitted | c/(4pi) fitted | b_fixed | A_fixed |
|---|---|---|---|---|---|
| -4 | 5.34592 | 2.32736 | 1.00653 | 1.76424 | 2421.96 |
| -3 | 5.38259 | 2.17445 | 1.00517 | 1.57925 | 5514.06 |
| 5 | 5.39284 | 1.94597 | 1.01634 | 0.81791 | 149.264 |
| 8 | 5.38233 | 1.04773 | 1.01051 | 0.594302 | 120.502 |
| -7 | 5.25611 | 2.29453 | 1.00963 | 1.81964 | 902.099 |
| 12 | 5.32969 | 0.985188 | 1.01083 | 0.673635 | 89.6714 |
| -20 | 4.81996 | 3.45218 | 1.08321 | 2.01606 | 830.233 |
| 21 | 5.09691 | 1.0664 | 0.998808 | 1.086 | 93.5586 |
| 13 | 5.3371 | -0.217523 | 0.969746 | 0.58575 | 115.5 |
| -8 | 5.23396 | 2.07754 | 1.00719 | 1.76723 | 1420.99 |

### Controls, Schur envelopes and Rayleigh totals

| D | x | N | joint half-width | negative E/O | control min E | control min O | Rayleigh arch | Rayleigh primes |
|---|---|---|---|---|---|---|---|---|
| -4 | 13 | 200 | 4.709660901 | 1/0 | -0.450623277091 | 0.199181115282 | -0.161507309151 | 0.161507309151 |
| -4 | 25 | 260 | 4.668022858 | 1/0 | -0.548045087096 | 0.000877929597053 | -0.173328153399 | 0.173328153399 |
| -4 | 50 | 420 | 4.470290981 | 1/1 | -0.616863861734 | -0.155604589595 | -0.179292625174 | 0.179292625174 |
| -3 | 13 | 200 | 4.362475483 | 1/1 | -0.738305349543 | -0.0885009571702 | -0.328682220866 | 0.328682220866 |
| -3 | 25 | 260 | 3.963179122 | 1/1 | -0.835727159548 | -0.286804142855 | -0.342085057189 | 0.342085057189 |
| -3 | 50 | 420 | 3.549872308 | 2/1 | -0.904545934186 | -0.443286662046 | -0.348940379900 | 0.348940379900 |
| 5 | 13 | 200 | 4.844692855 | 1/0 | -1.34577327083 | 0.310347442721 | -0.588566768749 | 0.588566768751 |
| 5 | 25 | 260 | 4.907052580 | 1/0 | -1.66328301184 | 0.0298643468239 | -0.619111615117 | 0.619111615117 |
| 5 | 50 | 420 | 4.258373727 | 1/1 | -1.93505893085 | -0.232587881551 | -0.634634841046 | 0.634634841046 |
| 8 | 13 | 200 | 5.362163595 | 1/0 | -0.875769641583 | 0.780351071967 | -0.397790546911 | 0.397790764610 |
| 8 | 25 | 260 | 5.204137962 | 1/0 | -1.19327938260 | 0.499867976070 | -0.431919772016 | 0.431919772016 |
| 8 | 50 | 420 | 5.794128371 | 1/0 | -1.46505530160 | 0.237415747695 | -0.448688585032 | 0.448688585032 |
| -7 | 13 | 200 | 4.950286148 | 0/0 | 0.108992510844 | 0.758796903217 | 0.241374854281 | -0.241374650536 |
| -7 | 25 | 260 | 5.185359513 | 0/0 | 0.0115707008397 | 0.560493717532 | 0.228579662294 | -0.228579662294 |
| -7 | 50 | 420 | 5.729216772 | 1/0 | -0.0572480737989 | 0.404011198341 | 0.222903053538 | -0.222903053538 |
| 12 | 13 | 200 | 5.178332194 | 1/0 | -0.470304533475 | 1.18581618008 | -0.223714359618 | 0.223830176933 |
| 12 | 25 | 260 | 5.398650636 | 1/0 | -0.787814274488 | 0.905333084178 | -0.267152501751 | 0.267152502422 |
| 12 | 50 | 420 | 5.500469183 | 1/0 | -1.05959019349 | 0.642880855803 | -0.286421515018 | 0.286421515018 |
| -20 | 13 | 200 | 5.602314131 | 0/0 | 1.15881463534 | 1.80861902772 | 1.25644196864 | -1.15766791171 |
| -20 | 25 | 260 | 5.596662019 | 0/0 | 1.06139282534 | 1.61031584203 | 1.09930759841 | -1.09903964425 |
| -20 | 50 | 420 | 5.663447680 | 0/0 | 0.992574050700 | 1.45383332284 | 1.07637916795 | -1.07637916783 |
| 21 | 13 | 200 | 5.831991998 | 0/0 | 0.0893112544608 | 1.74543196801 | 0.347211604198 | -0.323960630363 |
| 21 | 25 | 260 | 5.989479112 | 1/0 | -0.228198486552 | 1.46494887211 | 0.0684254668885 | -0.0683896210538 |
| 21 | 50 | 420 | 4.905560988 | 1/0 | -0.499974405556 | 1.20249664374 | -0.00910034003179 | 0.00910034005612 |
| 13 | 13 | 200 | 5.332518718 | 1/0 | -0.390261825801 | 1.26585888775 | -0.201224841042 | 0.201627627529 |
| 13 | 25 | 260 | 5.054037523 | 1/0 | -0.707771566814 | 0.985375791851 | -0.286085346338 | 0.286085350888 |
| 13 | 50 | 420 | 5.022479853 | 1/0 | -0.979547485818 | 0.722923563476 | -0.316020521600 | 0.316020521600 |
| -8 | 13 | 200 | 4.672063784 | 0/0 | 0.242523903469 | 0.892328295841 | 0.328008645739 | -0.328004108711 |
| -8 | 25 | 260 | 3.999096709 | 0/0 | 0.145102093464 | 0.694025110157 | 0.309305145779 | -0.309305145779 |
| -8 | 50 | 420 | 4.589664255 | 0/0 | 0.0762833188256 | 0.537542590965 | 0.301663184281 | -0.301663184281 |

### FLOATING finite-N tail check

| D | x | previous N | final N | eps(previous)/eps(final) | eps(N_sat)/eps(final) |
|---|---|---|---|---|---|
| -4 | 13 | 120 | 200 | 1.03515 | 8.73616 |
| -4 | 25 | 180 | 260 | 1.04664 | 11.7693 |
| -4 | 50 | 260 | 420 | 1.08017 | 21.5338 |
| -3 | 13 | 120 | 200 | 1.07788 | 3.7007 |
| -3 | 25 | 180 | 260 | 1.03894 | 22.465 |
| -3 | 50 | 260 | 420 | 1.15174 | 18.9093 |
| 5 | 13 | 120 | 200 | 1.01473 | 10.0058 |
| 5 | 25 | 180 | 260 | 1.05135 | 18.9274 |
| 5 | 50 | 260 | 420 | 1.0911 | 54.8765 |
| 8 | 13 | 120 | 200 | 1.00407 | 5.56075 |
| 8 | 25 | 180 | 260 | 1.01724 | 16.0315 |
| 8 | 50 | 260 | 420 | 1.0665 | 48.188 |
| -7 | 13 | 120 | 200 | 1.00474 | 11.3436 |
| -7 | 25 | 180 | 260 | 1.03096 | 26.0784 |
| -7 | 50 | 260 | 420 | 1.04512 | 38.045 |
| 12 | 13 | 120 | 200 | 1.00108 | 14.9577 |
| 12 | 25 | 180 | 260 | 1.00421 | 26.4679 |
| 12 | 50 | 260 | 420 | 1.03553 | 46.7824 |
| -20 | 13 | 120 | 200 | 1.00041 | 1.60663 |
| -20 | 25 | 180 | 260 | 1.00118 | 9.07653 |
| -20 | 50 | 260 | 420 | 1.00633 | 231.069 |
| 21 | 13 | 120 | 200 | 1.00063 | 2.21145 |
| 21 | 25 | 180 | 260 | 1.00115 | 12.0835 |
| 21 | 50 | 260 | 420 | 1.00688 | 18.6485 |
| 13 | 13 | 120 | 200 | 1.00135 | 3.03688 |
| 13 | 25 | 180 | 260 | 1.00411 | 13.9082 |
| 13 | 50 | 260 | 420 | 1.03329 | 17.8445 |
| -8 | 13 | 120 | 200 | 1.00365 | 24.497 |
| -8 | 25 | 180 | 260 | 1.01712 | 11.1824 |
| -8 | 50 | 260 | 420 | 1.0608 | 48.205 |

### Zeta round 1 (existing output only; no rerun)

| x | N | N_sat | epsE | error upper (COMPARISON) | joint half-width |
|---|---|---|---|---|---|
| 13 | 200 | 56 | 2.85407e-59 | 2.00e-55 | 2.836 |
| 25 | 260 | 134 | 2.42562e-123 | 2.25e-119 | 2.146 |
| 50 | 360 | 352 | 2.26934e-257 | 2.45e-253 | 1.442 |

Review supplement (not recomputed): zeta x=50,N=420 eps=2.80881e-258; error=3.0346e-254; 13–50 slopes 5.379 and 5.373, source notes/reviews/rtp-round-1-2026-09-24.md, lines 649–651. The existing x50 driver output stops eigenpair comparisons at N=360.

### Axis x and fixed-L outcomes

| D | protocol | N | knots | indefinite knots | odd-minimum cutoffs | final epsE | final epsO |
|---|---|---|---|---|---|---|---|
| -4 | ccm | 60 | 24 | 0 | none | 5.96617753626e-58 | 8.16868262361e-54 |
| -4 | ccm | 120 | 14 | 0 | none | 5.80279382985e-30 | 4.36970457418e-26 |
| -4 | fixedL | 60 | 24 | 23 | 7,8,9,13,16,23,31,32,47 | 5.96617753626e-58 | 8.16868262361e-54 |
| -3 | ccm | 60 | 24 | 0 | none | 1.96419958945e-70 | 1.87624023106e-66 |
| -3 | ccm | 120 | 14 | 0 | none | 6.80621440932e-41 | 5.75089082085e-37 |
| 5 | ccm | 60 | 24 | 0 | none | 1.43283593401e-50 | 1.82177146066e-46 |
| 5 | ccm | 120 | 14 | 0 | none | 4.06665709788e-25 | 1.59687591870e-21 |
| 5 | fixedL | 60 | 24 | 23 | 3,7,8,9,27,47 | 1.43283593401e-50 | 1.82177146066e-46 |
| 8 | ccm | 60 | 24 | 0 | none | 4.97249268353e-32 | 6.03517666880e-28 |
| 8 | ccm | 120 | 14 | 0 | none | 2.44934862761e-15 | 6.88284258813e-12 |
| -7 | ccm | 60 | 24 | 0 | none | 7.41744506610e-35 | 1.16223342280e-30 |
| -7 | ccm | 120 | 14 | 0 | none | 3.63042721239e-16 | 1.72512766520e-12 |
| 12 | ccm | 60 | 24 | 0 | none | 5.75113733890e-21 | 4.51318365274e-17 |
| 12 | ccm | 120 | 14 | 0 | none | 6.80989556112e-10 | 1.24123071322e-6 |
| -20 | ccm | 60 | 24 | 0 | none | 1.43407523933e-10 | 4.86253222952e-7 |
| -20 | ccm | 120 | 14 | 0 | none | 0.000268874531039 | 0.106335257818 |
| 21 | ccm | 60 | 24 | 0 | none | 2.95394939571e-11 | 5.02080091588e-8 |
| 21 | ccm | 120 | 14 | 0 | none | 3.59846816725e-5 | 0.0146210626418 |
| 13 | ccm | 60 | 24 | 0 | none | 3.56044415876e-19 | 2.35329747011e-15 |
| 13 | ccm | 120 | 14 | 0 | none | 4.61245847185e-9 | 6.61815739516e-6 |
| -8 | ccm | 60 | 24 | 0 | none | 4.82698622448e-30 | 6.49698307009e-26 |
| -8 | ccm | 120 | 14 | 0 | none | 1.06671299424e-13 | 3.77026181317e-10 |

### FLOATING fixed-resolution slopes and loss relative to final-N proxy

| D | N fixed | slope 13–25 | slope 25–50 | terminal x | decimal digits lost vs final-N proxy |
|---|---|---|---|---|---|
| -4 | 60 | 1.31466 | 1.12318 | 50 | 5.67513 |
| -4 | 120 | 1.31681 | — | 25 | 0.0316739 |
| -3 | 60 | 1.76958 | 1.18641 | 50 | 15.5805 |
| -3 | 120 | 1.7748 | — | 25 | 0.0603417 |
| 5 | 60 | 1.05783 | 1.02036 | 50 | 1.73939 |
| 5 | 120 | 1.06008 | — | 25 | 0.0447869 |
| 8 | 60 | 0.657367 | 0.670482 | 50 | 0.251997 |
| 8 | 120 | 0.662547 | — | 25 | 0.0259329 |
| -7 | 60 | 0.722952 | 0.750958 | 50 | 0.343445 |
| -7 | 120 | 0.729265 | — | 25 | 0.0450603 |
| 12 | 60 | 0.433752 | 0.444052 | 50 | 0.129194 |
| 12 | 120 | 0.435925 | — | 25 | 0.0061958 |
| -20 | 60 | 0.213377 | 0.251133 | 50 | 0.0788637 |
| -20 | 120 | 0.213773 | — | 25 | 0.00148916 |
| 21 | 60 | 0.233867 | 0.243633 | 50 | 0.0842299 |
| 21 | 120 | 0.234216 | — | 25 | 0.00167897 |
| 13 | 60 | 0.40981 | 0.405541 | 50 | 0.13665 |
| 13 | 120 | 0.411811 | — | 25 | 0.00591888 |
| -8 | 60 | 0.628993 | 0.657306 | 50 | 0.233991 |
| -8 | 120 | 0.635859 | — | 25 | 0.0263973 |

### x50 determinant and precision audit

These LDL/bordering certificates complete before the expensive eigenpair comparisons. All values below are ball-certified; N_sat is the unique argmin over 1..420.

| D | N_sat full/even/odd | minimum full logdet | worst pivot accuracy (bits of 4200) | joint half-width at N420 |
|---|---|---|---|---|
| -4 | 80/80/80 | -1287.1115063921 | 3553 | 4.470290981 |
| -3 | 110/110/110 | -2401.2069788692 | 3238 | 3.549872308 |
| 5 | 60/60/60 | -856.07791085415 | 3708 | 4.258373727 |
| 8 | 35/35/30 | -302.47559909992 | 3824 | 5.794128371 |
| -7 | 41/41/39 | -373.15804027167 | 3807 | 5.729216772 |
| 12 | 21/21/21 | -117.12155458100 | 3873 | 5.500469183 |
| -20 | 7/10/7 | -24.953377726696 | 3908 | 5.663447680 |
| 21 | 10/10/10 | -31.159762225705 | 3906 | 4.905560988 |
| 13 | 21/21/15 | -99.791521188752 | 3877 | 5.022479853 |
| -8 | 33/33/33 | -268.76034318545 | 3829 | 4.589664255 |

### FLOATING q × slope per character (claude:opus, complete outputs)

q × slope in decimal digits per unit x/q; 4π/ln10 = 5.4575. Final-N values (certified upper bounds on the infinite-N eps).

| D | q | kappa | slope 13–50 | q×slope 13–25 | q×slope 25–50 | q×slope 13–50 | x/q at x=13 |
|---|---|---|---|---|---|---|---|
| -4 | 4 | 1 | 1.336481 | 5.2728 | 5.3810 | 5.3459 | 3.250 |
| -3 | 3 | 1 | 1.794198 | 5.3314 | 5.4072 | 5.3826 | 4.333 |
| 5 | 5 | 0 | 1.078569 | 5.3164 | 5.4295 | 5.3928 | 2.600 |
| 8 | 8 | 0 | 0.672791 | 5.3165 | 5.4139 | 5.3823 | 1.625 |
| -7 | 7 | 1 | 0.750872 | 5.1299 | 5.3167 | 5.2561 | 1.857 |
| 12 | 12 | 0 | 0.444141 | 5.2368 | 5.3743 | 5.3297 | 1.083 |
| -20 | 20 | 1 | 0.240998 | 4.2776 | 5.0803 | 4.8200 | 0.650 |
| 21 | 21 | 0 | 0.242710 | 4.9210 | 5.1813 | 5.0969 | 0.619 |
| 13 | 13 | 0 | 0.410546 | 5.3593 | 5.3264 | 5.3371 | 1.000 |
| -8 | 8 | 1 | 0.654246 | 5.1034 | 5.2966 | 5.2340 | 1.625 |

Through-origin fits of the ten 13–50 slopes (digits per unit x): k/q: k = 5.3491, rms 0.0120; k/sqrt q: k = 2.2930, rms 0.2357; k/log q: k = 1.5996, rms 0.2082. Free power law: slope ∝ q^-1.037 (ten characters), q^-1.024 with zeta (q=1, review value 5.37857). q × slope(13–50) range [4.820, 5.393]. FLOATING.

### FLOATING pooled fit over the 30 final-N points (claude:opus, complete outputs)

Model log eps = a_D + b_kappa log(x/q) − c x/q (one amplitude per character). Residuals in decimal digits.

| model | points | parameters | c/(4π) | b(kappa=0) | b(kappa=1) | rms | max |
|---|---|---|---|---|---|---|---|
| common c, b per parity [all 30] | 30 | 13 | 1.00391 | 0.895 | 2.031 | 0.0426 | 0.0881 |
| common c, b per parity [x/q ≥ 1] | 28 | 13 | 1.00193 | 0.772 | 1.857 | 0.0355 | 0.0831 |
| c = 4pi fixed, b per parity [all 30] | 30 | 12 | 1 (fixed) | 0.751 | 1.787 | 0.0508 | 0.1114 |
| c = 4pi fixed, b per parity [x/q ≥ 1] | 28 | 12 | 1 (fixed) | 0.693 | 1.721 | 0.0375 | 0.0715 |
| common c, b per character [all 30] | 30 | 21 | 1.00782 | per D | per D | 0.0252 | 0.0817 |
| common c, b per character [x/q ≥ 1] | 28 | 21 | 1.00721 | per D | per D | 0.0178 | 0.0625 |
| raw x: common c, b per parity [all 30] | 30 | 13 | 0.14470 | 13.950 | -10.519 | 6.7589 | 17.7216 |
| raw x: common c, b per parity [x/q ≥ 1] | 28 | 13 | 0.09415 | -6.818 | -35.567 | 6.1315 | 16.0243 |

Per-character power of x/q with c = 4π fixed (least squares over the three windows): D=-4: 1.762, D=-3: 1.577, D=5: 0.814, D=8: 0.593, D=-7: 1.818, D=12: 0.673, D=-20: 2.012, D=21: 1.086, D=13: 0.588, D=-8: 1.766. Range 0.59–1.09 (mean 0.75) for kappa=0, 1.58–2.01 (mean 1.79) for kappa=1. Parity at q=8: eps(D=-8)/eps(D=8) = 20.8, 43.5, 101.2 at x = 13, 25, 50. FLOATING.

### N_sat (full window) against the D1b heuristic 1.7 x log x / q

| D | x=13 | x=25 | x=50 |
|---|---|---|---|
| -4 | 11 vs 14.2 | 30 vs 34.2 | 80 vs 83.1 |
| -3 | 17 vs 18.9 | 41 vs 45.6 | 110 vs 110.8 |
| 5 | 7 vs 11.3 | 23 vs 27.4 | 60 vs 66.5 |
| 8 | 4 vs 7.1 | 13 vs 17.1 | 35 vs 41.6 |
| -7 | 4 vs 8.1 | 13 vs 19.5 | 41 vs 47.5 |
| 12 | 2 vs 4.7 | 7 vs 11.4 | 21 vs 27.7 |
| -20 | 1 vs 2.8 | 3 vs 6.8 | 7 vs 16.6 |
| 21 | 2 vs 2.7 | 2 vs 6.5 | 10 vs 15.8 |
| 13 | 2 vs 4.4 | 7 vs 10.5 | 21 vs 25.6 |
| -8 | 2 vs 7.1 | 13 vs 17.1 | 33 vs 41.6 |

### FLOATING tail diagnosis: local exponent −d ln eps/d ln N on the sampled steps from N=80

eps_N is nonincreasing in N (interlacing), so every final-N value is a certified upper bound on the infinite-N value. "not decreasing" marks points not shown to be in a convergent tail.

| D | x | N | exponents | last-step digits | flag |
|---|---|---|---|---|---|
| -4 | 13 | 80,120,200 | 0.179, 0.068 | 0.015 |  |
| -4 | 25 | 80,120,180,260 | 0.320, 0.067, 0.124 | 0.020 | not decreasing |
| -4 | 50 | 80,160,260,420 | 4.045, 0.389, 0.161 | 0.033 |  |
| -3 | 13 | 80,120,200 | 0.231, 0.147 | 0.033 |  |
| -3 | 25 | 80,120,180,260 | 0.329, 0.248, 0.104 | 0.017 |  |
| -3 | 50 | 80,110,160,260,420 | 46.073, 6.498, 0.749, 0.295 | 0.061 |  |
| 5 | 13 | 80,120,200 | 0.068, 0.029 | 0.006 |  |
| 5 | 25 | 80,120,180,260 | 0.083, 0.131, 0.136 | 0.022 | not decreasing |
| 5 | 50 | 80,160,260,420 | 0.771, 0.329, 0.182 | 0.038 |  |
| 8 | 13 | 80,120,200 | 0.019, 0.008 | 0.002 |  |
| 8 | 25 | 80,120,180,260 | 0.216, 0.105, 0.046 | 0.007 |  |
| 8 | 50 | 80,160,260,420 | 0.351, 0.106, 0.134 | 0.028 | not decreasing |
| -7 | 13 | 80,120,200 | 0.020, 0.009 | 0.002 |  |
| -7 | 25 | 80,120,180,260 | 0.302, 0.181, 0.083 | 0.013 |  |
| -7 | 50 | 80,160,260,420 | 0.455, 0.128, 0.092 | 0.019 |  |
| 12 | 13 | 80,120,200 | 0.005, 0.002 | 0.000 |  |
| 12 | 25 | 80,120,180,260 | 0.060, 0.025, 0.011 | 0.002 |  |
| 12 | 50 | 80,160,260,420 | 0.164, 0.167, 0.073 | 0.015 |  |
| -20 | 13 | 80,120,200 | 0.002, 0.001 | 0.000 |  |
| -20 | 25 | 80,120,180,260 | 0.011, 0.006, 0.003 | 0.001 |  |
| -20 | 50 | 80,160,260,420 | 0.114, 0.038, 0.013 | 0.003 |  |
| 21 | 13 | 80,120,200 | 0.002, 0.001 | 0.000 |  |
| 21 | 25 | 80,120,180,260 | 0.014, 0.007, 0.003 | 0.000 |  |
| 21 | 50 | 80,160,260,420 | 0.116, 0.039, 0.014 | 0.003 |  |
| 13 | 13 | 80,120,200 | 0.005, 0.003 | 0.001 |  |
| 13 | 25 | 80,120,180,260 | 0.057, 0.024, 0.011 | 0.002 |  |
| 13 | 50 | 80,160,260,420 | 0.231, 0.165, 0.068 | 0.014 |  |
| -8 | 13 | 80,120,200 | 0.015, 0.007 | 0.002 |  |
| -8 | 25 | 80,120,180,260 | 0.229, 0.108, 0.046 | 0.007 |  |
| -8 | 50 | 80,160,260,420 | 0.335, 0.085, 0.123 | 0.026 | not decreasing |

Not shown in a decreasing tail: D=-4 x=25, D=5 x=25, D=8 x=50, D=-8 x=50. Largest |eps slope − first-zero-error slope| over 13–50, all ten characters (COMPARISON): 0.0056 digits per unit x.


<!-- D5_TABLES_END -->

**NUMERICAL D4/D5 (fixed-window parity).** Odd minima really occur in partial-information forms, even though the complete CCM forms examined so far have even minima. For D=5 at x=50,N=60,X=47, the even minimum is `-1.18909219699e-12` and the odd minimum is `-0.000121535867110` (one negative even eigenvalue, two negative odd eigenvalues). Thus reporting only the even block would conceal the much larger obstruction to positivity. The driver reports these odd minima and both inertias. No CCM zero comparison is defined for an indefinite partial form or an odd minimizer; those are not silently assigned the even block's roots. Rates in D5 refer to the complete positive forms, whose minimizing parity is certified case by case.

## D6. Verdict

*[Rewritten by claude:opus on 2026-09-26 from the 52 complete outputs; the first paragraph is the REFUTE review's correction 6 verbatim, the first part of the second its correction 7 verbatim, the D1b paragraph its correction 8 verbatim. All rates and fits below are FLOATING post-processing of certified eigenvalues at finite N.]*

**REFUTED numerically on 13 ≤ x ≤ 50: a character-independent rate in raw x.** At the largest tested N the 13–50 even-minimum slopes run from 0.2410 (D=-20) to 1.7942 (D=-3) decimal digits per unit x (six required characters: 0.4441 to 1.7942), against 5.379 for zeta; the last sampled N step changes eps by at most 0.061 digits. The first-zero error has the same 13–50 slopes to within 0.006 digits per x where compared (13–25: within 0.009). All slopes are FLOATING post-processing of certified eigenvalues. *[claude:opus: with the five completed x=50 files the first-zero comparison now covers all ten characters; the largest 13–50 difference is 0.0056 digits per x, D=5.]*

The ten 13–50 slopes (digits per unit x): D=-4 1.336481, D=-3 1.794198, D=5 1.078569, D=8 0.672791, D=-7 0.750872, D=12 0.444141, D=-20 0.240998, D=21 0.242710, D=13 0.410546, D=-8 0.654246.

**NUMERICAL support for D1a:** the leading scale is x/q for all ten characters: q × slope(13–50) lies in [4.820, 5.393]; slope = k/q fits with k = 5.349 and rms 0.012 digits per x (k/sqrt q: 0.236; k/log q: 0.208); a free power law gives q^-1.037, and q^-1.024 with zeta at q=1. The per-unit-(x/q) rate approaches 4pi/ln10 = 5.4575 from below as x/q grows (25–50: 5.08 to 5.43). Parity changes the prefactor, not the exponent: at q=8, eps(D=-8)/eps(D=8) = 20.8, 43.5, 101.2 at x=13, 25, 50 (about x^1.17); with c = 4pi fixed the fitted power of x/q is 0.59–1.09 for kappa=0 and 1.58–2.01 for kappa=1 (difference about one, as for the lowest even and odd prolate sectors). FLOATING. This does not establish an exact prefactor law. In particular this experiment does not justify saying that arithmetic determines only the floor while a universal exp(-4pi x) rate comes from the unscaled window.

**NUMERICAL (FLOATING): the exponent 4π x/q, pooled over all ten characters.** Over the 30 final-N points (ten characters at x = 13, 25, 50), the model log eps = a_D + b_kappa log(x/q) − c x/q, with one common c, one power of x/q per parity and one amplitude per character (13 parameters), gives **c/(4π) = 1.0039, rms residual 0.043 digits** (max 0.088), b(kappa=0) = 0.90, b(kappa=1) = 2.03. Restricted to x/q ≥ 1 (28 points): c/(4π) = 1.0019, rms 0.036. With c = 4π fixed: rms 0.051, b = 0.75 and 1.79. With one power per character: c/(4π) = 1.0078, rms 0.025. The same parity model in raw x has rms 6.8 digits. These numbers were recomputed on the complete outputs by `x50-completion/complete_d5.py`, independently of the review's script, and agree with its section 10 (the regenerated files carry the same eigenvalues as their partial predecessors). Parity enters the prefactor power only: b(kappa=1) − b(kappa=0) = 1.14 (free c) or 1.04 (c = 4π), with the absolute values about 0.25–0.3 above the lowest-sector 1/2 and 3/2 that D1a named without assigning parity; the draft's b = 1 + kappa is post hoc and not adopted. For comparison, zeta with c = 4π fixed gives b = 5.0 on 13–25 and 25–50, near CCM's 9/2 for the pole-constrained h0/h4 sector (review, refit section 11).

**Withdrawn: "fitted conductor-scaled exponents within 0.7% of 4pi"** (interim `progress.txt`). The per-character three-point fits give c/(4π) = 1.0065 (D=-4), 1.0052 (-3), 1.0163 (5), 1.0105 (8), 1.0096 (-7), 1.0108 (12), 1.0832 (-20), 0.9988 (21), 0.9698 (13), 1.0072 (-8): within 0.7% only for D = -4, -3, 21. Three points fix three parameters, so these fits have no residual, and b and c are strongly correlated. Only the pooled statement above is supported. The per-unit-(x/q) rate reaches 4π/ln 10 only asymptotically: q = 13, 20, 21 have x/q < 1 at x = 13 and are pre-asymptotic (D=-20: 1.083; D=13: 0.970, the only character whose 25–50 slope is below its 13–25 slope).

**Comparison with D1b.** N_sat(full) against 1.7 x log x/q at x=50: 110 vs 110.8 (q=3), 80 vs 83.1 (q=4), 60 vs 66.5 (q=5), 35/33 vs 41.6 (q=8), 7 vs 16.6 (q=20). The downward shift with q is confirmed; the coefficient 1.7 holds only for small q. *[claude:opus: over all ten characters at x = 50, q N_sat/(x log x) runs from 0.716 (D=-20) to 1.687 (D=-3); full table in D5.]*

**Saturation caveats.** Every rate above uses the largest tested N (200, 260, 420). By interlacing these are certified upper bounds on the infinite-N eps, not converged values. The last sampled step changes eps by at most 0.061 digits (D=-3, x=50); it is 0.03–0.04 digits for D=-3 at x=13 and for D=-4 and 5 at x=50, and at most 0.028 digits elsewhere. Four points are not shown to be in a decreasing tail: D=-4 and D=5 at x=25 (local exponents −d ln eps/d ln N 0.067 → 0.124 and 0.131 → 0.136) and D=8 and D=-8 at x=50 (0.106 → 0.134 and 0.085 → 0.123). A further 0.1 digit at x=50 would move a 13–50 slope by 0.003 digits per x (0.06 in q × slope at q=20): far too small to bridge the factor of about 7 between the characters and zeta, but enough to limit per-character c at the 1% level. The determinant argmin is not a convergence criterion (eps(N_sat)/eps(final) reaches 231 at D=-20, x=50).

**NUMERICAL (COMPARISON and controls).** The first-zero error tracks eps: at x=50, N=420 the ratio error/eps runs from 0.80 (D=21) to 588 (D=-3), character-dependent and slowly growing with x (D=-4: 38.6, 47.1, 52.4). The first-zero height organises the slopes worse than q (rms of log residuals 0.153 against 0.024; review, refit section 12, COMPARISON data). The joint Schur half-widths at the final N of every (D, x) lie between 3.55 and 5.99 and do not contract with eps, so the round-1 distinction between the Schur envelope and the small-eigenvalue channel carries over unchanged. The Rayleigh decomposition at x=50, now certified for all ten characters, is a near-cancellation of an archimedean and a prime part of size 0.009 (D=21) to 1.08 (D=-20); the archimedean part is positive for D=-7, -20, -8 and negative for the other seven. The archimedean-only control at x=50, N=420 has negative inertia (E/O) 1/1 (D=-4, 5), 2/1 (D=-3), 1/0 (D=8, -7, 12, 21, 13) and 0/0 (D=-20, -8).

**What the experiment does not decide.** Conductor and prime comb change together across this family, so it cannot say whether q acts through the functional equation (the Poisson scale of D1a) or through the atoms. It proves nothing about the Weil minimiser: the transfer from prolate concentration to eps remains OPEN (H-CONCENTRATION-TRANSFER, lane E). Everything here is a finite computation on 13 ≤ x ≤ 50; no RH or GRH is assumed, and zeros enter only the labelled COMPARISON steps.

**Answer to the lane's question.** The rate is not the same for every L-function in the raw window variable x, so "the arithmetic content of the dilation channel is the floor, not the rate" is refuted as stated. The data fit the window's prolate rate e^{−4πy} in the conductor-normalised variable y = x/q, which is what D1a predicted before the runs. Arithmetic then enters through q in the exponent, through parity (and, for zeta, the pole constraints) in the power of y, and through the amplitude and the floor.

## Numerical checks for the blind lane

**NUMERICAL: certified eigenvalues (rounded ball midpoints; every printed digit certified); the slope and the pooled fit are FLOATING.** Reproduce these from the prime-side driver alone (pole-free Weil data of L(s, χ_D): primes, conductor, archimedean factor), without supplying reference zeros to the form:

| D | x | N | eps_E | eps_O | global minimum | note |
|---|---|---|---|---|---|---|
| -4 | 13 | 20 | 6.46618822590e-14 | 1.29408802638e-10 | even | also reproduced by independent mpmath quadrature (REFUTE review, check 8) |
| 5 | 13 | 20 | 2.90753234209e-12 | 3.65105020928e-9 | even | as above |
| -20 | 13 | 20 | 0.0996075078912 | 1.84985574399 | even | as above |
| -4 | 13 | 200 | 3.55108899176e-14 | 7.49736362617e-11 | even | |
| 5 | 25 | 260 | 3.66818026982e-25 | 1.54653184431e-21 | even | |
| -4 | 50 | 420 | 1.26056711373e-63 | 4.15988533034e-59 | even | |
| 8 | 50 | 420 | 2.78341006540e-32 | 3.88470771085e-28 | even | from the rerun after the stop |

One saturation check: D=-4, x=50, N_sat(full/even/odd) = 80/80/80, unique over 1..420; minimum full logdet = -1287.1115063921. One slope: D=-4, 13–50: 1.336481 digits per unit x from the N=200 and N=420 values. One pooled number: c/(4π) = 1.0039, rms 0.043 digits, over the 30 final-N points (model of D6). One control inertia: D=-3, x=13, N=200, X=1 has (negative, zero, positive) = (1, 0, 200) in E and (1, 0, 199) in O, with minima -0.738305349543 and -0.0885009571702. One control shift: minE(D=-20) − minE(D=-4) at x=13, N=200 equals log 5 = 1.6094379124 to ten digits.

Reproduction:

```sh
make -C zst build/rtp2_dirichlet
zst/tools/rtp2_dirichlet_run.sh              # DS, PHASES=x13,x25,axisx,x50, JOBS, X50_ALL restrict or parallelise
python3 notes/rtp-round-2/dirichlet/checks/first_zero_prefix.py
python3 notes/rtp-round-2/dirichlet/checks/audit_outputs.py
python3 notes/rtp-round-2/dirichlet/x50-completion/complete_d5.py   # runs checks/summary.py; rewrites the D5 block
python3 notes/rtp-round-2/dirichlet/x50-completion/prefix_check.py
```

`--prec` is 4200 at x=50 with eigenpair precision 2400; D=12 at x=25 uses eigenpair precision 1400. The reference-generation program and its two-precision enclosures are in `checks/`; the three missing character records were appended to the reference fixture under the brief's exception. No library source or include behaviour was changed.

## What this changes in the notebook

*[Written by claude:opus, 2026-09-26, consistent with the REFUTE review's "Recommendation for shard 08j". Nothing is registered by this report; each row is to be written and then reviewed.]*

**Candidate claim rows for shard 08j.**

| id | kind | status | content |
|---|---|---|---|
| `num:rtp2-dirichlet-window-rate` | numerical | NUMERICAL (certified eigenvalues; FLOATING rates and fits) | the D5 tables with the review's corrections 3–5, all ten characters at x = 13, 25, 50: raw-x character-independence refuted (13–50 slopes 0.241–1.794 digits per x against zeta's 5.379); slope = k/q with k = 5.349, rms 0.012; pooled c/(4π) = 1.0039, rms 0.043 digits; parity in the power of x/q only; final-N values are certified upper bounds, four points not shown in a decreasing tail |
| `lem:weil-control-conductor-shift` | lemma | PROVED (D1c, D2b, D2c; review VALID) | at fixed atoms and gamma data the X=1 control spectra differ by exactly log(q2/q1); the odd-character control dominates the even one by the multiplier π/cosh(πt); the control is positive on every window when log(q/π) + ψ((κ+1/2)/2) > 0 |
| `obs:rtp-round-1-reading`(iii), corrected | observation | SHARPENED | replace "kinematic or arithmetic: undecided" by: (1) the rate is not a property of the window in raw x; (2) it is the window's rate in the conductor-normalised variable x/q (one exponent e^{−4πx/q}, pooled c/(4π) = 1.004; zeta on the same law with its own power b = 5.0); (3) arithmetic enters through q in the exponent, parity and pole constraints in the power, and amplitude and floor; conductor and prime comb are not separated; the transfer to eps is OPEN (H-CONCENTRATION-TRANSFER) |

**Existing rows.** `lem:bordering-interval`: no new row; D2 shows it holds without pole terms, and the A1.1'(4) wording is corrected to "the gain of MaxEnt over the truth". `num:rtp-dilation-channel`: the Schur envelope does not follow eps for any character (joint half-widths 3.5 to 6.0), the first-zero error tracks eps, and the N_sat coefficient 1.7 holds only for small q. Round 1's zeta statements stay as they are; no zeta run or shard was changed here.

**One next experiment (OPEN).** A matched-x/q design: run the characters at the same y = x/q ≥ 2 on three windows (x up to about 100 for q = 21, cheap there because N_sat ≤ 10), extend the tails to N ≥ 600 where they are not yet decreasing (D = ±8 at x = 50, D = -4 and 5 at x = 25), and test whether eps/[y^{b_κ} e^{−4πy}] stabilises, including the matched-conductor pair D = ±8. Zeros enter only the labelled comparison.
