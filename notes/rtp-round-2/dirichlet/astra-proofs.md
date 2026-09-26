# RTP-2 lane D: Dirichlet dilation windows

Author: `codex:gpt-6-astra`. Unreviewed research record. No RH assumption. Forms use only the generic Weil builder; reference zeros enter labelled COMPARISON steps only.

## Correction ledger (incremental)

1. **SHARPENED (before runs).** The same logarithmic window does not imply the same effective additive Fourier concentration parameter. Primitive conductor q introduces the Fourier scale q in twisted Poisson summation. A conductor-independent exponent in x is a hypothesis to test, not a consequence of CCM §7.
2. **PROVED (source audit).** CCM §7, `mc2arXiv.tex` lines 1324–1329, prints exactly `(2^14/3) sqrt(2) pi^5 exp(-4 pi lambda^2 + 9 log lambda)`. Thus the quoted exponent and prefactor agree with the source; in x this is `C x^(9/2) exp(-4 pi x)`. This checks the quotation, not Fuchs's theorem independently. CCM explicitly leaves the relation of its prolate ansatz to the Weil minimizer open in §8.
3. **SHARPENED.** The reference file is `zst/tests/data/dirichlet_ref.txt`. Its existing PARI values are floating 40-digit values, not certified balls. Giving them radius 1e-38 is insufficient for the requested high accuracy and is not by itself a certificate. They will supply comparison-only starting guesses, refined with certified Hardy-Z interval Newton.
4. **SHARPENED.** “Trivial set empty” means no pole directions at ±1/2 in the centred variable. Nonprincipal Dirichlet L-functions still have their usual trivial zeros. An odd minimum also makes the existing CCM sum-normalization undefined; an odd comparison must be identified as an extension, not silently sent to the even routine.

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

**PROVED D2 (conditional only on finite block positive definiteness).** Let E_N and O_N be positive definite and fix a_j, j=N+1, for a real reflection-symmetric Loewner form. No assumption about its pole, prime or gamma origin is needed. Write b=b_true+beta. The new columns are `c_e=u_e+b w_e`, `c_o=u_o+b w_o`, with

- `w_e=(sqrt(2)/j, (1/(i+j)-1/(i-j))_(i=1..N))`, `d_e=a_j+b/j`;
- `w_o=(-1/(i-j)-1/(i+j))_(i=1..N)`, `d_o=a_j-b/j`.

For each block `s(beta)=s0+l beta-C beta²`, where `C=w^T G^-1 w>0` and `l=±1/j-2w^T G^-1 c_true`. The admissible interval is `beta*=l/(2C)` plus/minus `r=sqrt((s0+l²/(4C))/C)` when its radicand is nonnegative. The joint interval is the intersection. On its positive interior the joint maximum determinant uniquely maximizes `log s_e+log s_o`; each separate maximum is at its interval centre. The normalized truth position is `tau=-beta*/r`, with `tau²=1-s0/(s0+l²/(4C))`. The joint gain `log(s_e(beta_ME)s_o(beta_ME)/(s_e(0)s_o(0)))` is the gain of MaxEnt **over** the truth, correcting the reversed wording in A1.1'(4). The zero unconstrained column is compatible with both Loewner columns only if all old b_i vanish. For N>=1 the vectors w are nonzero; N=0 requires treating the empty odd block separately.

Proof: congruence of the bordered matrix with `diag(G,d-c^T G^-1 c)` gives positivity and determinant factorization; substitution and completion of the square give the interval formulas. Strict concavity of the logarithm of each positive, strictly concave quadratic gives uniqueness. The even zeroth entry forces b=0 for a zero column, then its remaining entries force b_i=0. These are exactly A1.1' algebra, unchanged when pole terms vanish. The absent pole directions only change the numerical input G and the control, which is now gamma plus conductor, X=1.

## D3. Driver and certification

**NUMERICAL (implementation).** `zst/tools/rtp2_dirichlet.c` retains A1's Schur quadratic, structured interval, joint MaxEnt and shifted Rump/deflation helpers. Its form builder is exactly `zst_weil_dirichlet; zst_weil_ab`; no library source or include behavior is changed. The independent local prime increment is multiplied by Kronecker(D,k), and its accumulated data are checked against the generic builder (every fixed-L knot and every final Rayleigh decomposition).

Options: `--D`, `--mode axisN|axisx`, `--x`, `--Nmax`, `--cmp N1,N2,...`, `--prec`, `--cprec`, `--N`, `--xmax`, `--fixedL 1`. Axis N automatically certifies eigenpairs at the full determinant minimizer and Nmax in addition to `--cmp`. It certifies the unique determinant argmin over the scanned range for full, even and odd blocks. This is a finite-range certificate, not an assertion about all N.

Both block minima first receive independent Rayleigh/positive-definiteness brackets from `zst_block_min`. Their strict ball ordering implements `zst_parity`'s criterion. Separate Rump eigenpair and deflated positivity certificates produce normalized eigenvectors and sharp eigenvalue balls in both blocks, checked against those independent brackets. The even-simple flag is reported separately. The X=1 control includes `log |D| I`; its positive and negative counts are certified by LDL at zero. Successful nonzero pivots imply zero nullity. The Rayleigh decomposition uses the actual minimizing block.

COMPARISON uses `checks/reference.c`: identify the primitive character by checking its full residue table against Kronecker(D,n), read a starting guess from `zst/tests/data/dirichlet_ref.txt`, and refine a unique real Hardy-Z root by interval Newton using FLINT's `acb_dirichlet_hardy_z` and its derivative. Missing guesses are located by a comparison-only sign scan. The root ball is certified; the assertion that it is the *first* zero inherits PARI's indexing or that scan (not a certified zero-free prefix). All generated reference enclosures are kept in the lane outputs; the original reference file is not overwritten with uncertified high-precision midpoints. Secular roots come from the minimizer without reference-zero input; a complete N-root list is checked for even cases. The existing CCM construction is undefined for odd minima (sum normalization zero), which is reported explicitly. No odd case is silently replaced by the even one.

Arithmetic: FLINT 3 arb balls throughout forms, LDL, eigenvalues, inertia, error differences and Rayleigh parts. Printed scalar values are rounded midpoints only when the relative ball error is smaller than their displayed precision with guard bits; otherwise the complete ball is printed. Joint MaxEnt's location and QR shift candidates are floating; the evaluated Schur values and admissibility checks are balls. Derived slopes, ratios calculated from printed values, and fitted prefactors in `checks/summary.py` will be labelled floating. Output has no time or addresses; elapsed times are stderr only.

**NUMERICAL (pilot).** Before launching the suite, `(D,x,N)=(-4,13,40)` reproduced MVP-3: `eps_E=4.93772909768e-14`, first-zero error `1.89828037683e-12`, all 40 roots certified. The pilot completed 265 checks, zero failed. `make -C zst check` passed all existing tests.

## D4. Runs (incremental)

The run script starts with all x=13 cases, then x=25, then axis-x protocols, then x=50. It runs at most 12 independent processes, with timings retained under `checks/runlogs/`. The requested six characters and optional -20,21,13 are included, plus -8 to compare both character parities at exactly the same conductor 8. The x=50 extension is attempted for all ten characters; eigenvalues at several N will test convergence beyond the determinant minimum. All outputs are `outputs/rtp2_dirichlet_*.txt`.

D3 correction during validation: the inherited shifted helper needs an explicit scalar (1x1) branch; otherwise its QR-based second-eigenvalue gap is infinite. This affected the N=1 odd *control* for D=-20, not the form eigenvalue. Fixed locally in the new driver. Also `zst_block_min` sometimes returns a broad but valid minimum bracket (D=12,x=25,N=40,80). The separate Rump-plus-deflated-PD minimum certificates were already sharp and decisive. The driver now intersects the two valid certificates of each block minimum before the parity comparison; raw bracket overlap is disclosed. This uses a certified *minimum*, not an arbitrary eigenpair. Failed development outputs are retained in checks and the affected cases will be rerun.

Missing-reference exception authorized by the brief: `checks/generate_references.py --append` adds D=-7,-20,21 to `zst/tests/data/dirichlet_ref.txt` in its existing format. Only 40-digit comparison seeds are appended; standalone runs at 800 and 1200 bits give overlapping certified Hardy-Z root balls, retained in checks. Existing records are unchanged. This supersedes the earlier plan not to append to that file. No reference datum enters the form or its certificates.

**PROVED D2b (additional control comparison).** At a fixed conductor and window, the odd-character archimedean form exceeds the even-character one as a quadratic form. Indeed, digamma reflection gives
`Re psi(3/4+it/2)-Re psi(1/4+it/2)=pi/cosh(pi t)>0`.
Plancherel expresses the difference of the two controls as the integral of this positive multiplier times the squared Fourier transform of the test function. Thus every nonzero finite-window function has strictly larger odd-character archimedean value, and the negative count for kappa=1 is at most that for kappa=0 in either reflection block. Character parity kappa and window reflection parity E/O are distinct notions.

| protocol | discriminants | resolution/window | bits for LDL / eigenpairs | planned files |
|---|---|---|---|---:|
| axis N | -4,-3,5,8,-7,12,-20,21,13,-8 | x=13, Nmax=200 | 1000 / 700 | 10 |
| axis N | same ten | x=25, Nmax=260 | 1800 / 1200 (D=12: 1400 on rerun) | 10 |
| axis N | same ten | x=50, Nmax=420 | 4200 / 2400 | 10 |
| axis x CCM | same ten | N=60, x through prime powers to 50 | 2700 | 10 |
| axis x CCM | same ten | N=120, x through prime powers to 25 | 1800 | 10 |
| axis x fixed L | -4,5 | N=60, L=log 50, cutoff 1 through 49 | 2700 | 2 |

The original low-cost stages used the development certifier before the two edge-case corrections. Both stages are being rerun with the final driver so all released outputs have the same check logic. D=12 at x=25 also raises eigenpair precision from 1200 to 1400 bits; the form precision stays 1800. The two development failures are preserved as `checks/development_*_failed.txt`, not counted as final successes. No precision increase has been needed for construction of a Weil form.

**PROVED D2c (why a positive control is possible).** The gamma multiplier is minimized at t=0: the digamma series gives
`Re psi(a+ib)-psi(a)=sum_(n>=0) b²/((n+a)((n+a)²+b²)) >= 0` for a>0.
Thus `log(q/pi)+psi((kappa+1/2)/2)>0` is sufficient for positivity on every window and at every N. For kappa=1 this lower bound is `log(q/(8pi))-EulerGamma+pi/2`; it is positive at q=20. Therefore the positive X=1 control for D=-20 is a theorem, not a failure to resolve small negative eigenvalues. For a fixed kappa the entire control spectra at different q differ by exactly log(q2/q1), which the output minima can independently check.

## D5. Extraction conventions (tables appended as runs finish)

**NUMERICAL.** The primary saturated proxy is the largest tested N at each x: 200,260,420. The driver also evaluates eps exactly at the determinant argmin; both will appear in the table. “Saturated” here means well beyond the measured determinant minimum, not a rigorous limit as N tends to infinity. Ratios against the previous sampled N quantify the remaining tail. The N_sat certificate covers integers 1..Nmax only; an argmin at 1 is left-censored and must not be fitted as an interior transition.

Every eigenvalue, reported inertia, determinant comparison, Rayleigh sum, and error difference in the raw files is obtained in ball arithmetic. Displayed values are rounded as described in D3. Slopes use `s(a,b)=(log10 eps(a)-log10 eps(b))/(b-a)` and are explicitly **floating postprocessing**, as are fitted exponents and amplitudes. `checks/summary.py` regenerates all tables from the output files. The reference-root ball certifies a unique zero; the first-index identification remains the labelled comparison convention explained in D3.

The old zeta output has x=50 eigenpairs only through N=360. Its existing value is retained in the extraction. Where the corrected round-1 13–50 slope is compared, I separately cite the review's already certified N=420 value (2.80881e-258; comparison error 3.0346e-254), rather than claim that it came from `rtp1_a1_axisN_x50.txt` or rerun zeta.

<!-- D5_TABLES_BEGIN -->
### Saturation and final-N results

Eigenvalues are rounded certified-ball results. N_sat is over 1..Nmax, certified unique. Final N is a finite-resolution proxy; it is not an infinite-N certificate.

| D | x | N final | N_sat full/even/odd | epsE at N_sat | epsE final | epsO final | parity |
|---|---|---|---|---|---|---|---|
| -4 | 13 | 200 | 11/11/11 | 3.10228843498e-13 | 3.55108899176e-14 | 7.49736362617e-11 | 1 |
| -4 | 25 | 260 | 30/30/30 | 6.34913624745e-29 | 5.39464993971e-30 | 3.88258923824e-26 | 1 |
| -3 | 13 | 200 | 17/17/17 | 4.63730601677e-19 | 1.25308864637e-19 | 2.88150878846e-16 | 1 |
| -3 | 25 | 260 | 41/41/39 | 1.33067281669e-39 | 5.92330252137e-41 | 5.03576541872e-37 | 1 |
| 5 | 13 | 200 | 7/7/7 | 2.10911890230e-11 | 2.10790657667e-12 | 3.00014809680e-9 | 1 |
| 5 | 25 | 260 | 23/23/22 | 6.94290139292e-24 | 3.66818026982e-25 | 1.54653184431e-21 | 1 |
| 8 | 13 | 200 | 4/4/4 | 1.21057046016e-6 | 2.17699319902e-7 | 0.000143025517367 | 1 |
| 8 | 25 | 260 | 13/13/13 | 3.69906341403e-14 | 2.30737261661e-15 | 6.57100869491e-12 | 1 |
| -7 | 13 | 200 | 4/4/4 | 2.31119975654e-6 | 2.03745394328e-7 | 0.000177050652770 | 1 |
| -7 | 25 | 260 | 13/13/13 | 8.53449943462e-15 | 3.27263403207e-16 | 1.65324013253e-12 | 1 |
| 12 | 13 | 200 | 2/2/2 | 0.00173236382165 | 0.000115817314349 | 0.0379151462554 | 1 |
| 12 | 25 | 260 | 7/7/7 | 1.77690413690e-8 | 6.71343285554e-10 | 1.17534100376e-6 | 1 |
| -20 | 13 | 200 | 1/1/1 | 0.158693673555 | 0.0987740569268 | 1.80464336194 | 1 |
| -20 | 25 | 260 | 3/3/3 | 0.00243209532977 | 0.000267954162959 | 0.104112987818 | 1 |
| 21 | 13 | 200 | 2/2/1 | 0.0514183313883 | 0.0232509738349 | 0.809121815454 | 1 |
| 21 | 25 | 260 | 2/2/2 | 0.000433141563711 | 3.58458347666e-5 | 0.0141272342948 | 1 |
| 13 | 13 | 200 | 2/2/2 | 0.00122321454012 | 0.000402786486930 | 0.0548613049682 | 1 |
| 13 | 25 | 260 | 7/7/7 | 6.32827857151e-8 | 4.55002293950e-9 | 6.27965278425e-6 | 1 |
| -8 | 13 | 200 | 2/4/2 | 0.000111143598106 | 4.53702800257e-6 | 0.00271051444180 | 1 |
| -8 | 25 | 260 | 13/13/12 | 1.12249347399e-12 | 1.00380725322e-13 | 3.59244810027e-10 | 1 |
| zeta R1 | 13 | 200 | 56/—/— | — | 2.85407e-59 | — | 1 |
| zeta R1 | 25 | 260 | 134/—/— | — | 2.42562e-123 | — | 1 |
| zeta R1 | 50 | 360 | 352/—/— | — | 2.26934e-257 | — | 1 |
| zeta review | 50 | 420 | 352/—/— | — | 2.80881e-258 | — | 1 |

### COMPARISON: first root, final N

| D | x | N | error (ball) | error/eps (ball) | gamma1 |
|---|---|---|---|---|---|
| -4 | 13 | 200 | 1.36924359116e-12 | 38.5584138931 | 6.02094890469759665490251152161 |
| -4 | 25 | 260 | 2.54172642712e-28 | 47.1156878672 | 6.02094890469759665490251152161 |
| -3 | 13 | 200 | 4.86212210036e-17 | 388.011024953 | 8.03973715568146668171362321417 |
| -3 | 25 | 260 | 3.01497655714e-38 | 509.002629236 | 8.03973715568146668171362321417 |
| 5 | 13 | 200 | 3.32035533794e-10 | 157.519093811 | 6.64845334472771471612327845998 |
| 5 | 25 | 260 | 7.87056999737e-23 | 214.563337089 | 6.64845334472771471612327845998 |
| 8 | 13 | 200 | 5.37737315942e-6 | 24.7009185047 | 4.89997399700703650103830489920 |
| 8 | 25 | 260 | 7.45333904342e-14 | 32.3022774465 | 4.89997399700703650103830489920 |
| -7 | 13 | 200 | 2.91870117758e-6 | 14.3252375702 | 4.47573828372868313197462848719 |
| -7 | 25 | 260 | 5.74301376538e-15 | 17.5485975795 | 4.47573828372868313197462848719 |
| 12 | 13 | 200 | 0.000723657015974 | 6.24826279249 | 3.80462763305086509714431754004 |
| 12 | 25 | 260 | 5.38313221787e-9 | 8.01844947838 | 3.80462763305086509714431754004 |
| -20 | 13 | 200 | 0.0907225887304 | 0.918486002833 | 2.35893499408665604861501236977 |
| -20 | 25 | 260 | 0.000279539568020 | 1.04323651827 | 2.35893499408665604861501236977 |
| 21 | 13 | 200 | 0.0138214097826 | 0.594444339439 | 2.31518706430314115204629295971 |
| 21 | 25 | 260 | 2.60986873282e-5 | 0.728081449299 | 2.31518706430314115204629295971 |
| 13 | 13 | 200 | 0.000743221932889 | 1.84520076270 | 3.11934147900860341390159975672 |
| 13 | 25 | 260 | 1.01725521657e-8 | 2.23571447901 | 3.11934147900860341390159975672 |
| -8 | 13 | 200 | 1.42968317872e-5 | 3.15114470952 | 3.57615483678758907557757872996 |
| -8 | 25 | 260 | 3.67712339543e-13 | 3.66317675394 | 3.57615483678758907557757872996 |

### FLOATING slopes (positive digits per x)

| D | E 13–25 | O 13–25 | error 13–25 | E 25–50 | O 25–50 | error 25–50 | E 13–50 | O 13–50 | error 13–50 |
|---|---|---|---|---|---|---|---|---|---|
| -4 | 1.3182 | 1.27382 | 1.31095 | NA | NA | NA | NA | NA | NA |
| -3 | 1.77712 | 1.7298 | 1.7673 | NA | NA | NA | NA | NA | NA |
| 5 | 1.06328 | 1.02398 | 1.0521 | NA | NA | NA | NA | NA | NA |
| 8 | 0.664562 | 0.611482 | 0.654852 | NA | NA | NA | NA | NA | NA |
| -7 | 0.732849 | 0.669147 | 0.725504 | NA | NA | NA | NA | NA | NA |
| 12 | 0.436402 | 0.375721 | 0.427375 | NA | NA | NA | NA | NA | NA |
| -20 | 0.213882 | 0.103241 | 0.209273 | NA | NA | NA | NA | NA | NA |
| 21 | 0.234334 | 0.146496 | 0.226994 | NA | NA | NA | NA | NA | NA |
| 13 | 0.412255 | 0.328444 | 0.405307 | NA | NA | NA | NA | NA | NA |
| -8 | 0.637927 | 0.573138 | 0.632478 | NA | NA | NA | NA | NA | NA |
| zeta R1 | 5.33922 | — | 5.32907 | 5.36116 | — | 5.35852 | 5.35404 | — | 5.34897 |
| zeta review | 5.33922 | — | 5.32907 | 5.39745 | — | 5.3948 | 5.37857 | — | 5.37348 |

### FLOATING conductor scaling and polynomial fit

Fit log(eps)=a+b log(x/q)-c x/q at the three final-N samples. This is a three-point interpolation, not a validated asymptotic expansion. b_fixed fixes c=4pi and uses endpoints; A_fixed uses x=50.

| D | q × slope 13–50 | b fitted | c/(4pi) fitted | b_fixed | A_fixed |
|---|---|---|---|---|---|

### Controls, Schur envelopes and Rayleigh totals

| D | x | N | joint half-width | negative E/O | control min E | control min O | Rayleigh arch | Rayleigh primes |
|---|---|---|---|---|---|---|---|---|
| -4 | 13 | 200 | 4.709660901 | 1/0 | -0.450623277091 | 0.199181115282 | -0.161507309151 | 0.161507309151 |
| -4 | 25 | 260 | 4.668022858 | 1/0 | -0.548045087096 | 0.000877929597053 | -0.173328153399 | 0.173328153399 |
| -3 | 13 | 200 | 4.362475483 | 1/1 | -0.738305349543 | -0.0885009571702 | -0.328682220866 | 0.328682220866 |
| -3 | 25 | 260 | 3.963179122 | 1/1 | -0.835727159548 | -0.286804142855 | -0.342085057189 | 0.342085057189 |
| 5 | 13 | 200 | 4.844692855 | 1/0 | -1.34577327083 | 0.310347442721 | -0.588566768749 | 0.588566768751 |
| 5 | 25 | 260 | 4.907052580 | 1/0 | -1.66328301184 | 0.0298643468239 | -0.619111615117 | 0.619111615117 |
| 8 | 13 | 200 | 5.362163595 | 1/0 | -0.875769641583 | 0.780351071967 | -0.397790546911 | 0.397790764610 |
| 8 | 25 | 260 | 5.204137962 | 1/0 | -1.19327938260 | 0.499867976070 | -0.431919772016 | 0.431919772016 |
| -7 | 13 | 200 | 4.950286148 | 0/0 | 0.108992510844 | 0.758796903217 | 0.241374854281 | -0.241374650536 |
| -7 | 25 | 260 | 5.185359513 | 0/0 | 0.0115707008397 | 0.560493717532 | 0.228579662294 | -0.228579662294 |
| 12 | 13 | 200 | 5.178332194 | 1/0 | -0.470304533475 | 1.18581618008 | -0.223714359618 | 0.223830176933 |
| 12 | 25 | 260 | 5.398650636 | 1/0 | -0.787814274488 | 0.905333084178 | -0.267152501751 | 0.267152502422 |
| -20 | 13 | 200 | 5.602314131 | 0/0 | 1.15881463534 | 1.80861902772 | 1.25644196864 | -1.15766791171 |
| -20 | 25 | 260 | 5.596662019 | 0/0 | 1.06139282534 | 1.61031584203 | 1.09930759841 | -1.09903964425 |
| 21 | 13 | 200 | 5.831991998 | 0/0 | 0.0893112544608 | 1.74543196801 | 0.347211604198 | -0.323960630363 |
| 21 | 25 | 260 | 5.989479112 | 1/0 | -0.228198486552 | 1.46494887211 | 0.0684254668885 | -0.0683896210538 |
| 13 | 13 | 200 | 5.332518718 | 1/0 | -0.390261825801 | 1.26585888775 | -0.201224841042 | 0.201627627529 |
| 13 | 25 | 260 | 5.054037523 | 1/0 | -0.707771566814 | 0.985375791851 | -0.286085346338 | 0.286085350888 |
| -8 | 13 | 200 | 4.672063784 | 0/0 | 0.242523903469 | 0.892328295841 | 0.328008645739 | -0.328004108711 |
| -8 | 25 | 260 | 3.999096709 | 0/0 | 0.145102093464 | 0.694025110157 | 0.309305145779 | -0.309305145779 |

### FLOATING finite-N tail check

| D | x | previous N | final N | eps(previous)/eps(final) | eps(N_sat)/eps(final) |
|---|---|---|---|---|---|
| -4 | 13 | 120 | 200 | 1.03515 | 8.73616 |
| -4 | 25 | 180 | 260 | 1.04664 | 11.7693 |
| -3 | 13 | 120 | 200 | 1.07788 | 3.7007 |
| -3 | 25 | 180 | 260 | 1.03894 | 22.465 |
| 5 | 13 | 120 | 200 | 1.01473 | 10.0058 |
| 5 | 25 | 180 | 260 | 1.05135 | 18.9274 |
| 8 | 13 | 120 | 200 | 1.00407 | 5.56075 |
| 8 | 25 | 180 | 260 | 1.01724 | 16.0315 |
| -7 | 13 | 120 | 200 | 1.00474 | 11.3436 |
| -7 | 25 | 180 | 260 | 1.03096 | 26.0784 |
| 12 | 13 | 120 | 200 | 1.00108 | 14.9577 |
| 12 | 25 | 180 | 260 | 1.00421 | 26.4679 |
| -20 | 13 | 120 | 200 | 1.00041 | 1.60663 |
| -20 | 25 | 180 | 260 | 1.00118 | 9.07653 |
| 21 | 13 | 120 | 200 | 1.00063 | 2.21145 |
| 21 | 25 | 180 | 260 | 1.00115 | 12.0835 |
| 13 | 13 | 120 | 200 | 1.00135 | 3.03688 |
| 13 | 25 | 180 | 260 | 1.00411 | 13.9082 |
| -8 | 13 | 120 | 200 | 1.00365 | 24.497 |
| -8 | 25 | 180 | 260 | 1.01712 | 11.1824 |

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
| 21 | ccm | 60 | 24 | 0 | none | 2.95394939571e-11 | 5.02080091588e-8 |
| 13 | ccm | 60 | 24 | 0 | none | 3.56044415876e-19 | 2.35329747011e-15 |
| -8 | ccm | 60 | 24 | 0 | none | 4.82698622448e-30 | 6.49698307009e-26 |


<!-- D5_TABLES_END -->

**NUMERICAL D4/D5 (fixed-window parity).** Odd minima really occur in partial-information forms, even though the complete CCM forms examined so far have even minima. For D=5 at x=50,N=60,X=47, the even minimum is `-1.18909219699e-12` and the odd minimum is `-0.000121535867110` (one negative even eigenvalue, two negative odd eigenvalues). Thus reporting only the even block would conceal the much larger obstruction to positivity. The driver reports these odd minima and both inertias. No CCM zero comparison is defined for an indefinite partial form or an odd minimizer; those are not silently assigned the even block's roots. Rates in D5 refer to the complete positive forms, whose minimizing parity is certified case by case.
