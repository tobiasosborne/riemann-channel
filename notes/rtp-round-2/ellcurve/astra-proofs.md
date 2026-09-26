# RTP-2 lane E: weight-two dilation windows

Author: `codex:gpt-6-astra`. Unreviewed research record. No RH assumption. Reference zeros are used only in labelled COMPARISON steps. All claims below carry their status; no claim is registered by this lane.

## Correction ledger (incremental)

1. **SHARPENED, before runs.** E2's `2 x log x` does not follow from the supplied Weyl law. The same mode-surplus calculation used in lanes A1/D gives `sqrt(x/C) log x`; see E2. Twice the leading zero density reduces the surplus and changes its turning point exponentially in the window length.
2. **SHARPENED, before runs.** In F4/F5, if alpha,beta are the arithmetic roots with alpha beta=p, the atom weight is `-(alpha^m+beta^m) log(p)/p^m`, not `/p^(m/2)`. The latter denominator requires normalized Satake roots alpha/sqrt(p), beta/sqrt(p). The driver uses the existing library normalization exactly.
3. **SHARPENED, before runs.** The decaying inverse-Mellin gamma kernel and the log-derivative kernel rho in the Weil form are different kernels. Reading off the exponential of the former alone does not prove an eigenvalue decay constant for the latter. H-RATE specifies a scale; a numerical leading constant needs an additional concentration hypothesis.
4. **SHARPENED, before runs.** For any single conductor, sqrt(x) and sqrt(x/C) are constant multiples, so intercept-plus-slope fits have identical residuals. Conductor scaling can only be tested by comparing slopes across curves, or by a constrained joint fit.
5. **NUMERICAL provenance.** Lane D is unfinished on entry (D4/D5 PARTIAL, D6 PENDING). Reuse its independent block-minimum certification, Rump/deflation refinement, Schur bordering, controls, output conventions, and completed outputs. Do not inherit its pending high-window verdict or its Hardy-Z reference evaluator, which applies to Dirichlet characters only. A separate `zst/tools/rtp2_ellcurve.c` avoids modifying a running lane's driver.
6. **SHARPENED.** “Atom density 2 log p versus log p” is not a literal description of F4/F5. The prime-power positions and their count are unchanged. At good elliptic primes there are two normalized Satake contributions, whose signed sum varies with p and m and can vanish; at bad primes there is one or none. Doubling every zeta atom would be a different form. The doubled leading Weyl density is instead visible in the gamma symbol and is consistent with Euler-factor degree two.
7. **NUMERICAL correction to a universal reading of parity.** 37a1 is even at x=2,3 and odd at every tested CCM knot from x=4 through 50 (N=60). The older report's odd observations at x=8,13,20 stand. Rank positivity is not a theorem of odd minimal parity on every short window. In accordance with the brief, no first-zero comparison is made for 37a1 at any window.
8. **NUMERICAL prediction audit, initial completed range.** The stronger E1b constant is not an exact finite-range slope: N=60 gives 10.1894 and 10.0146 digits per sqrt(x/C), below 10.9150, with visible residual structure. The fit supports the scale, not an already established asymptotic constant. The imported 1.7 factor in E2 overestimates the first two curves' low-window determinant transitions; their scale and finite-N tails are tabulated separately.
9. **NUMERICAL qualification.** The small range 13–25 is not independently discriminating in every case: for 14a1 at N=120, the linear-x fit has RMS 0.0340 digits versus 0.0801 for sqrt(x). The longer 13–50 range reverses that ordering. No assertion of exact linearity or a uniform local slope is warranted.
10. **NUMERICAL protocol correction.** The inherited precision and repeated large-control QR spectra made the serial N=200 run too slow (206 seconds for its first knot). It was interrupted along with the unfinished high-N jobs; their partial files are preserved under `checks/interrupted_*`, and completed files were retained. The final script runs the long-axis knots in parallel, with 1000-bit forms/eigenpairs, and caps routine controls at N=120. The x=50 resolution reruns use 1000/700 bits, and x=100 uses 1400/1000. These are still far above the elliptic eigenvalue scale; all requested ball certificates must pass. Complete N=60 control spectra remain available. The aggregate long-axis file contains no cross-window overlap; the original serial N=60/120 files do.

## E1. Predictions recorded before new runs

**PREDICTION E1a — OPEN (H-WINDOW-ONLY).** If the very same CCM Fourier-prolate parameter controls the new Weil minimizer, then

`eps_E(x) ~ A_E x^b exp(-4 pi x)`.

The asymptotic rate is `4 pi/log(10)=5.4575054` decimal digits per unit x. Importing also zeta's pole-constrained sector `b=9/2` gives 5.3863535 digits/x over 13–50; that power is not justified for a pole-free weight-two form. The unchanged log window `[0,log x]` and Fourier basis do not establish H-WINDOW-ONLY. The archimedean data change from `rho_(2,1/2)(y)` to `rho_(1,1)(y)=exp(-y)/(1-exp(-y))`, and the atoms and pole constraints also change.

**PROVED (kernel identities; no minimizer conclusion).** Write lambda=sqrt(x), and u for the positive multiplicative variable before taking logs. The elementary Mellin identity is

`int_0^infinity exp(-2 pi u/sqrt(C)) u^s du/u = (sqrt(C)/(2 pi))^s Gamma(s)` for Re(s)>0.

Thus the weight-two completed L-function is obtained, up to a constant and the centred shift, from the Mellin transform of the modular Fourier sum `sum_(n>=1) a_n exp(-2 pi n u/sqrt(C))`. Its first exponential decays on the scale lambda/sqrt(C) at u=lambda. Zeta instead uses `sum exp(-pi n^2 u^2)` and has scale lambda^2=x. This makes sqrt(x/C), not sqrt(log x) or x/C, the candidate weight-two window scale. It does not specify whether amplitude, squared mass, or optimized concentration controls eps.

The centred gamma-ratio kernel supplies a sharper conditional prediction. For

`K_C(v)=(2 pi/sqrt(C)) sqrt(v) J_1(4 pi sqrt(v/C))`,

the Bessel Mellin integral gives `int K_C(v) v^s dv/v = (C/(4 pi^2))^s Gamma(1+s)/Gamma(1-s)` for -1 < Re(s) < 1/4 (then meromorphically), by [DLMF 10.22.43](https://dlmf.nist.gov/10.22.E43) with mu=2s and nu=1, after substituting t=4 pi sqrt(v/C). This is the weight-two gamma/conductor scattering ratio. Its product argument at the two support boundaries is v=lambda^2=x; after square-root coordinates the finite Hankel parameter is `c_E=4 pi sqrt(x/C)`. The corresponding zeta Fourier parameter is `c_zeta=2 pi x`. The standard finite Hankel kernel is `sqrt(c r t) J_alpha(c r t)`; see the primary paper [Boulsane–Karoui, arXiv:1701.04622](https://arxiv.org/abs/1701.04622). Identifying these transforms with the actual arithmetic Weil minimizer remains an additional hypothesis.

**PREDICTION E1b — OPEN (H-RATE plus H-HANKEL-TRANSFER).** If optimized low-sector concentration has leakage `exp(-2 c_E)` up to powers and transfers to eps, then

`eps_E(x) ~ A_E (sqrt(x/C))^b_E exp(-8 pi sqrt(x/C))`.

This predicts `8 pi/log(10)=10.9150108` digits per unit sqrt(x/C), or `10.9150108/sqrt(C)` digits per unit sqrt(x): 3.2909996 for C=11 and 2.9171594 for C=14. Its local rate per x is `5.4575054/sqrt(C x)`, before algebraic corrections. The error of a stably recovered simple first zero is predicted to share the leading exponential, with a separate prefactor. No exact power or amplitude is predicted. A bare squared Mellin tail instead suggests `exp(-4 pi sqrt(x/C))`, half this slope; record it as a weaker competing constant, not as a consequence of H-RATE. These predictions use only the already published MVP-3 observations, not a new elliptic run.

## E2. Resolution prediction

**PROVED algebra; OPEN as a saturation law.** In either reflection sector the Fourier-mode count up to T is approximately `T log(x)/(2 pi)`. Subtract the supplied positive-ordinate Weyl count:

`S_E(T)=T log(x)/(2 pi) - T/pi log(sqrt(C) T/(2 pi e))`.

Its derivative vanishes at `T*=2 pi sqrt(x/C)`, and S_E vanishes at `e T*`. Under `N=T log(x)/(2 pi)`, these become `N*=sqrt(x/C) log(x)` and `e N*`. I expect determinant minima on this scale, with order-one constants depending on parity, low zeros, and the omitted poles. The round-1 empirical constant 1.7 is a useful pilot guess, not a theorem: for 11a1 this suggests N near 5, 8, 14 at x=13,25,50, and near 24 at x=100. These N are determinant transitions, not quantitative certificates of convergence as N tends to infinity; eps must be checked at much larger N. The prescribed N=60,120,200 protocols should resolve the leading rate well, unlike zeta at those same windows.

## E3. Driver, provenance and run protocol

**NUMERICAL.** The separate driver `zst/tools/rtp2_ellcurve.c` ports lane D's working certifier without changing lane D, libzst sources or headers. The imported source SHA256 is in `checks/driver-source.sha256`; `checks/adapt_driver.py` records the initial port only, and is not a regeneration command for later hand-edited additions. Every form is built by `zst_weil_ellcurve; zst_weil_ab`. The independent per-prime-power recurrence in the driver reproduces the full generic-builder a,b data in each final Rayleigh decomposition. It retains the even/odd Schur quadratics of A1.1', their intersection, truth position and joint maximum-determinant gain. The latter is the gain of MaxEnt over truth, correcting A1.1'(4)'s reversed prose.

Both block minima receive independent `zst_block_min` brackets and Rump/deflation minimum-eigenpair certificates. Their intersections certify the global parity, and even simplicity is separately reported. All form, eigenpair, inertia, Schur and Rayleigh calculations use FLINT 3 ball arithmetic. A successful LDL certifies every scanned leading principal block positive definite. N_sat denotes the uniquely certified determinant minimizer on the finite scanned interval 1..Nmax; it is not an infinite-N convergence threshold. The final-N tail is measured separately. Printed midpoint digits have relative ball precision guards. QR shift candidates and the joint MaxEnt location are floating, with subsequent ball checks.

`--mode spectra` additionally computes the **complete ordered spectra** of the elliptic gamma-plus-conductor control, chi_-4 control, zeta gamma-only control and zeta gamma-plus-poles control. QR only proposes each interval. The two certified inertia counts i and i+1 at its endpoints isolate the ith eigenvalue. The intervals and both counts are printed, so the comparison includes more than just the lowest eigenvalue. This mode uses 384-bit forms and inertia, and 192-bit QR seeds; see `checks/spectra.c`.

**NUMERICAL, COMPARISON provenance.** `zst_ell_ref(...,K=0)` initially loads only the model, conductor, rank and root number. With the form/eigenpairs complete, a labelled COMPARISON step loads K=1. The file's 40-digit PARI ordinates and assigned radius 1e-38 are **approximations, not certified L-zero enclosures**; therefore first-zero errors are numerical comparisons, conditional on that reference accuracy. The construction's own secular roots are certified, and completeness of its N positive roots is checked for every even case. Rank-positive 37a1 is reported without a zero comparison, even at any small window where its minimum were to be even. No reference zero chooses a form, eigenvector or certificate.

**NUMERICAL pilot.** `(11a1,x=13,N=60)` gives epsE `7.67659737296e-7`, comparison error `0.000409577219972`, ratio `533.540056972`, reproducing MVP-3. The pilot completed 399 checks, zero failed. `make -C zst check` passed, captured in `checks/make-check.txt`. The first development build lacked the fmpz-vector header and crashed before producing data; the include was corrected, compilation is clean, and only the successful pilot is used.

| protocol | curves | range | form / eigenpair bits |
|---|---|---|---|
| axis N | 11a1, 14a1, 37a1 | x=13; Nmax=200 | 1000 / 700 |
| axis N | same | x=25; Nmax=260 | 1800 / 1200 |
| axis N | same | x=50; Nmax=420 | 1000 / 700 |
| CCM axis x | same | prime-power knots plus endpoint 50; N=60 | 2700 |
| CCM axis x | same | prime-power knots to 25; N=120 | 1800 |
| long CCM axis x | 11a1 | independent knots through 100; N=200 | 1000 |
| long resolution check | 11a1 | x=100; Nmax=420 | 1400 / 1000 |
| complete control spectra | 11a1, 14a1 and common controls | x=13,25,50; N=60 | 384 |

The script `zst/tools/rtp2_ellcurve_run.sh` runs at most 12 independent processes; times go to `checks/runlogs`, numerical files to `outputs/rtp2_ellcurve_*.txt`. Additional curves 15a1,17a1,19a1,20a1,21a1 are omitted: cypari2 is absent from the available Python and no independently verified reference/model set was available at entry. The four existing curve records were read; the experiment uses the requested rank-zero pair and 37a1. The allowed optional reference-file exception is not exercised.

**NUMERICAL independent audit.** `checks/independent_ab.py` computes point counts by literal enumeration of all affine pairs, reconstructs the arithmetic prime-power traces, and integrates the defining distribution against the four Fourier test functions using mpmath quadrature at 70 and 100 decimal digits. All 24 printed a,b values at x=13 for 11a1,14a1,37a1 agree with the independent computation to their 30 printed digits; precision doubling agrees within 1e-65 (36 checks). This quadrature check is floating, with precision-stability evidence, not an additional ball certificate.

**PROVED control identity.** The elliptic gamma-plus-conductor Fourier multiplier is
`h_C(t)=log(C/(4 pi^2))+2 Re psi(1+it)`. Thus changing C with atoms fixed shifts the entire form by log(C'/C) I; it leaves eigenvectors and the CCM secular roots unchanged, but changes the minimum eigenvalue. For the prime-free controls this means every ordered 14a1 eigenvalue is its 11a1 counterpart plus log(14/11). `checks/audit.py` verifies the identity within the certified intervals for both blocks, all 121 eigenvalues, all three windows. This is not an invariance under changing the actual elliptic curve, because its atoms change too.

<!-- E4_TABLES_BEGIN -->
## E4. Tables (generated; NUMERICAL unless labelled FLOATING)

Eigenvalues and inertia are certified in the raw files. COMPARISON errors use approximate PARI zeros; all slopes, fits and ratios computed here are FLOATING. “Final N” is a finite-resolution proxy, not a bound on the infinite-N tail.

### Run completion

| file | checks | failures |
|---|---|---|
| rtp2_ellcurve_11a1_axisN_x100.txt | RUNNING | — |
| rtp2_ellcurve_11a1_axisN_x13.txt | 1255 | 0 |
| rtp2_ellcurve_11a1_axisN_x25.txt | 1623 | 0 |
| rtp2_ellcurve_11a1_axisN_x50.txt | RUNNING | — |
| rtp2_ellcurve_11a1_axisx_ccm_N120.txt | 213 | 0 |
| rtp2_ellcurve_11a1_axisx_ccm_N200.txt | RUNNING | — |
| rtp2_ellcurve_11a1_axisx_ccm_N60.txt | 363 | 0 |
| rtp2_ellcurve_11a1_spectra_x13.txt | 492 | 0 |
| rtp2_ellcurve_11a1_spectra_x25.txt | 492 | 0 |
| rtp2_ellcurve_11a1_spectra_x50.txt | 492 | 0 |
| rtp2_ellcurve_14a1_axisN_x13.txt | 1255 | 0 |
| rtp2_ellcurve_14a1_axisN_x25.txt | 1623 | 0 |
| rtp2_ellcurve_14a1_axisN_x50.txt | RUNNING | — |
| rtp2_ellcurve_14a1_axisx_ccm_N120.txt | 213 | 0 |
| rtp2_ellcurve_14a1_axisx_ccm_N60.txt | 363 | 0 |
| rtp2_ellcurve_14a1_spectra_x13.txt | 492 | 0 |
| rtp2_ellcurve_14a1_spectra_x25.txt | 492 | 0 |
| rtp2_ellcurve_14a1_spectra_x50.txt | 492 | 0 |
| rtp2_ellcurve_37a1_axisN_x13.txt | 1248 | 0 |
| rtp2_ellcurve_37a1_axisN_x25.txt | 1615 | 0 |
| rtp2_ellcurve_37a1_axisN_x50.txt | RUNNING | — |
| rtp2_ellcurve_37a1_axisx_ccm_N120.txt | 198 | 0 |
| rtp2_ellcurve_37a1_axisx_ccm_N60.txt | 338 | 0 |
| rtp2_ellcurve_diagnostic_x2_N200.txt | 1223 | 0 |
| rtp2_ellcurve_pilot_11a1.txt | 399 | 0 |

Completed checks: 14881 

### Resolution and parity

| curve | x | final N | N_sat full/E/O | N_sat/[sqrt(x/C) log x] | epsE at N_sat | epsE final | epsO final | min parity |
|---|---|---|---|---|---|---|---|---|
| 11a1 | 13 | 200 | 3/3/3 | 1.075888 | 2.43947834223e-6 | 7.60586827693e-7 | 0.000145476586851 | E |
| 11a1 | 25 | 260 | 6/6/6 | 1.236441 | 1.23500169465e-10 | 2.42148388413e-11 | 1.16472149147e-8 | E |
| 14a1 | 13 | 200 | 2/2/2 | 0.809177 | 2.34714132383e-5 | 5.47398082239e-6 | 0.000879747523219 | E |
| 14a1 | 25 | 260 | 4/4/4 | 0.929929 | 1.14921916973e-8 | 1.00853123507e-9 | 4.92836083075e-7 | E |
| 37a1 | 13 | 200 | 1/1/1 | 0.6577341 | 0.444699197675 | 0.203253993996 | 0.0121747434397 | O |
| 37a1 | 25 | 260 | 3/2/3 | 1.13383 | 0.0154330254295 | 0.00638896651436 | 8.14692310352e-5 | O |

### COMPARISON at final N

| curve | x | N | first-zero error (PARI) | error/epsE |
|---|---|---|---|---|
| 11a1 | 13 | 200 | 0.000406325112562 | 534.225807978 |
| 11a1 | 25 | 260 | 3.07075607533e-8 | 1268.12988327 |
| 14a1 | 13 | 200 | 0.000850124715393 | 155.302830422 |
| 14a1 | 25 | 260 | 3.46751133644e-7 | 343.817941960 |
| 37a1 | 13 | 200 | inapplicable | — |
| 37a1 | 25 | 260 | inapplicable | — |

### Finite-N tails and Schur envelopes

| curve | x | tail N | epsE(previous)/final | epsO(previous)/final | epsE(60)/final | joint radius | Delta I (nats) | truth tau | sE next | sO next |
|---|---|---|---|---|---|---|---|---|---|---|
| 11a1 | 13 | 120→200 | 1.00162 | 1.014255 | 1.009299 | 8.560739087 | 0.009474191792 | -0.06574159550 | 10.48797386 | 10.48091321 |
| 11a1 | 25 | 200→260 | 1.001408 | 1.008096 | 1.03953 | 9.331564655 | 0.005152022584 | -0.03400086471 | 12.51575012 | 12.50887664 |
| 14a1 | 13 | 120→200 | 1.000946 | 1.010945 | 1.004876 | 9.061980277 | 0.003337548209 | -0.03726779845 | 12.13535849 | 12.13008886 |
| 14a1 | 25 | 200→260 | 1.001068 | 1.007451 | 1.028396 | 9.165456007 | 0.009095556477 | -0.06129854322 | 12.87675022 | 12.87175599 |
| 37a1 | 13 | 120→200 | 1.000303 | 1.007172 | 1.001335 | 10.16449852 | 0.01007585665 | -0.05741680830 | 13.06752973 | 13.06151881 |
| 37a1 | 25 | 200→260 | 1.000285 | 1.006108 | 1.005063 | 10.43396171 | 0.008180241610 | -0.05374122031 | 13.08917020 | 13.08321148 |

### Final-N endpoint slopes (FLOATING, positive digits gained)

| curve | range x | E digits/x | E digits/sqrt x | E digits/sqrt(x/C) | O digits/x | error digits/x |
|---|---|---|---|---|---|---|
| 11a1 | 13–25 | 0.3747556 | 3.224979 | 10.69604 | 0.3413809 | 0.343469 |
| 14a1 | 13–25 | 0.3112178 | 2.678201 | 10.02091 | 0.2709713 | 0.2824554 |
| 37a1 | 13–25 | 0.1252174 | 1.077565 | 6.554569 | 0.1812055 | — |

### CCM axis-x coverage

| curve | N | knots | last x | last epsE | last epsO | indefinite knots | odd-minimum windows |
|---|---|---|---|---|---|---|---|
| 11a1 | 60 | 24 | 50 | 1.13070309175e-17 | 1.50548637447e-14 | 0 | none |
| 11a1 | 120 | 14 | 25 | 2.44005541640e-11 | 1.19859483614e-8 | 0 | none |
| 14a1 | 60 | 24 | 50 | 3.24025668567e-15 | 3.70122291569e-12 | 0 | none |
| 14a1 | 120 | 14 | 25 | 1.01431791973e-9 | 5.06225076986e-7 | 0 | none |
| 37a1 | 60 | 24 | 50 | 9.90422454756e-6 | 5.74730912207e-8 | 0 | 4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41,43,47,49,50 |
| 37a1 | 120 | 14 | 25 | 0.00639699049973 | 8.33896278277e-5 | 0 | 4,5,7,8,9,11,13,16,17,19,23,25 |

### Linearising variable: equal-weight least squares (FLOATING)

Fit log10(epsE)=intercept−slope×variable over every printed knot with x≥13. RMS and max residuals are in decimal digits. The last two variables necessarily have identical residuals within each curve.

| curve | N | range | knots | variable | slope | RMS residual | max residual |
|---|---|---|---|---|---|---|---|
| 11a1 | 60 | 13–50 | 16 | x | 0.2805567 | 0.2995184 | 0.7558394 |
| 11a1 | 60 | 13–50 | 16 | sqrt(x) | 3.072212 | 0.08788969 | 0.1852243 |
| 11a1 | 60 | 13–50 | 16 | sqrt(x/C) | 10.18937 | 0.08788969 | 0.1852243 |
| 11a1 | 120 | 13–25 | 6 | x | 0.3711897 | 0.1078897 | 0.1624078 |
| 11a1 | 120 | 13–25 | 6 | sqrt(x) | 3.225089 | 0.03522068 | 0.0542738 |
| 11a1 | 120 | 13–25 | 6 | sqrt(x/C) | 10.69641 | 0.03522068 | 0.0542738 |
| 14a1 | 60 | 13–50 | 16 | x | 0.2441695 | 0.2913558 | 0.5033498 |
| 14a1 | 60 | 13–50 | 16 | sqrt(x) | 2.676512 | 0.07435942 | 0.115821 |
| 14a1 | 60 | 13–50 | 16 | sqrt(x/C) | 10.01459 | 0.07435942 | 0.115821 |
| 14a1 | 120 | 13–25 | 6 | x | 0.3162483 | 0.0339899 | 0.05790865 |
| 14a1 | 120 | 13–25 | 6 | sqrt(x) | 2.737282 | 0.08013304 | 0.1274878 |
| 14a1 | 120 | 13–25 | 6 | sqrt(x/C) | 10.24197 | 0.08013304 | 0.1274878 |

### Exponential with an algebraic prefactor (FLOATING)

Fit ln eps=a+b ln z−k z, z=sqrt(x/C), on the same knots (three parameters). Also fit a,b at fixed k=8pi and k=4pi (two parameters). These are finite-range empirical fits, not proofs of a limiting k.

| curve | N | b free | k/(8pi) free | RMS free | b at k=8pi | RMS 8pi | b at k=4pi | RMS 4pi |
|---|---|---|---|---|---|---|---|---|
| 11a1 | 60 | 0.4206909 | 0.9439995 | 0.08781864 | 2.648671 | 0.08980753 | -17.24384 | 0.1729728 |
| 11a1 | 120 | -13.69513 | 0.5594814 | 0.01262519 | 0.6161512 | 0.03664619 | -15.62753 | 0.01345265 |
| 14a1 | 60 | -2.707515 | 0.8414132 | 0.07079716 | 2.885152 | 0.08507807 | -14.74768 | 0.1238119 |
| 14a1 | 120 | 31.09725 | 2.015498 | 0.02910617 | 1.853983 | 0.07608491 | -12.5445 | 0.1088726 |

### Archimedean controls and Rayleigh cancellation

| curve | x | N form | N control | control min E | control min O | negative E/O | Rayleigh gamma+log C | Rayleigh primes | sum |
|---|---|---|---|---|---|---|---|---|---|
| 11a1 | 13 | 200 | 200 | -1.38957064134 | 0.0566717962475 | 1/0 | -0.867338025611 | 0.867338786198 | 7.60586827693e-7 |
| 11a1 | 25 | 260 | 260 | -1.61780175257 | -0.346411393408 | 1/1 | -0.939853026777 | 0.939853026801 | 2.42148388413e-11 |
| 14a1 | 13 | 200 | 200 | -1.14840858453 | 0.297833853064 | 1/0 | -0.722202911951 | 0.722208385932 | 5.47398082239e-6 |
| 14a1 | 25 | 260 | 260 | -1.37663969576 | -0.105249336591 | 1/1 | -0.799400476500 | 0.799400477508 | 1.00853123507e-9 |
| 37a1 | 13 | 200 | 200 | -0.176548001496 | 1.26969443609 | 1/0 | 1.40825013735 | -1.39607539391 | 0.0121747434397 |
| 37a1 | 25 | 260 | 260 | -0.404779112728 | 0.866611246438 | 1/0 | 1.23351378318 | -1.23343231395 | 8.14692310352e-5 |

### Complete control spectra, N=60

| control | x | block | dimension | negative | first three eigenvalues | maximum |
|---|---|---|---|---|---|---|
| 11a1 | 13 | E | 61 | 1 | -1.389506, 0.9979105, 2.146532 | 8.800277 |
| 11a1 | 13 | O | 60 | 0 | 0.06018465, 1.657207, 2.54948 | 8.699065 |
| chi_-4 | 13 | E | 61 | 1 | -0.4505942, 0.6745242, 1.256459 | 4.58748 |
| chi_-4 | 13 | O | 60 | 0 | 0.2009301, 1.008971, 1.459152 | 4.536873 |
| zeta_gamma | 13 | E | 61 | 3 | -2.955156, -0.7362003, -0.1354367 | 3.201035 |
| zeta_gamma | 13 | O | 60 | 2 | -1.29678, -0.3852603, 0.07042063 | 3.150578 |
| zeta_gamma_poles | 13 | E | 61 | 2 | -0.8483357, -0.1706915, 0.216161 | 3.285072 |
| zeta_gamma_poles | 13 | O | 60 | 2 | -1.979926, -0.4232322, 0.05750095 | 3.150573 |
| 11a1 | 25 | E | 61 | 1 | -1.617739, 0.5617744, 1.697466 | 8.346135 |
| 11a1 | 25 | O | 60 | 1 | -0.3427328, 1.211321, 2.09843 | 8.244883 |
| chi_-4 | 25 | E | 61 | 1 | -0.5480178, 0.4518949, 1.029594 | 4.360403 |
| chi_-4 | 25 | O | 60 | 0 | 0.002663599, 0.7826782, 1.232087 | 4.309779 |
| zeta_gamma | 25 | E | 61 | 3 | -3.272663, -0.9720214, -0.3639465 | 2.973933 |
| zeta_gamma | 25 | O | 60 | 3 | -1.576794, -0.6162495, -0.1579689 | 2.923483 |
| zeta_gamma_poles | 25 | E | 61 | 3 | -1.114162, -0.4018705, -0.01160679 | 5.01489 |
| zeta_gamma_poles | 25 | O | 60 | 3 | -3.031011, -0.6720325, -0.1775591 | 2.923474 |
| 11a1 | 50 | E | 61 | 1 | -1.786176, 0.1940078, 1.31374 | 7.956139 |
| 11a1 | 50 | O | 60 | 1 | -0.6699678, 0.831828, 1.712384 | 7.854844 |
| chi_-4 | 50 | E | 61 | 1 | -0.6168383, 0.2646664, 0.8348531 | 4.165398 |
| chi_-4 | 50 | O | 60 | 1 | -0.1537881, 0.5890805, 1.037082 | 4.114755 |
| zeta_gamma | 50 | E | 61 | 4 | -3.544436, -1.182036, -0.5610275 | 2.7789 |
| zeta_gamma | 50 | O | 60 | 4 | -1.838629, -0.8163922, -0.3545257 | 2.728459 |
| zeta_gamma_poles | 50 | E | 61 | 3 | -1.373111, -0.6048645, -0.2094325 | 7.618749 |
| zeta_gamma_poles | 50 | O | 60 | 4 | -4.67373, -0.8901807, -0.3806719 | 2.728445 |
| 14a1 | 13 | E | 61 | 1 | -1.148344, 1.239073, 2.387694 | 9.041439 |
| 14a1 | 13 | O | 60 | 0 | 0.3013467, 1.89837, 2.790642 | 8.940227 |
| 14a1 | 25 | E | 61 | 1 | -1.376577, 0.8029365, 1.938628 | 8.587297 |
| 14a1 | 25 | O | 60 | 1 | -0.1015707, 1.452483, 2.339592 | 8.486045 |
| 14a1 | 50 | E | 61 | 1 | -1.545014, 0.4351699, 1.554902 | 8.197301 |
| 14a1 | 50 | O | 60 | 1 | -0.4288058, 1.07299, 1.953546 | 8.096006 |

### Cross-object comparison on round-1 axes (FLOATING slopes)

| object | N_sat at 13,25,50 | epsE at 13 | epsE at 25 | epsE at 50 | digits/x 13–50 | provenance |
|---|---|---|---|---|---|---|
| zeta | 56,134,352 | 2.85407e-59 | 2.42562e-123 | 2.80881e-258 | 5.378566 | review N=420 at x50 |
| chi_-4 | 11,30,pending | 3.55108899176e-14 | 5.39464993971e-30 | pending | pending | completed lane D only |
| chi_-3 | 17,41,pending | 1.25308864637e-19 | 5.92330252137e-41 | pending | pending | completed lane D only |
| chi_5 | 7,23,pending | 2.10790657667e-12 | 3.66818026982e-25 | pending | pending | completed lane D only |
| chi_8 | 4,13,pending | 2.17699319902e-7 | 2.30737261661e-15 | pending | pending | completed lane D only |
| chi_12 | 2,7,pending | 0.000115817314349 | 6.71343285554e-10 | pending | pending | completed lane D only |
| chi_-8 | 2,13,pending | 4.53702800257e-6 | 1.00380725322e-13 | pending | pending | completed lane D only |

Zeta uses existing A1 outputs and the certified N=420 supplement in notes/reviews/rtp-round-1-2026-09-24.md:651. Other lanes are read only; pending results are not extrapolated.

### Rayleigh parts at matched x=50, N=60

| object | pole | gamma plus conductor | primes | epsilon (actual minimizing block) |
|---|---|---|---|---|
| zeta | 1.622046 | -1.530054 | -0.09199213 | 1.7501e-116 |
| chi_-4 | 0 | -0.180074838169 | 0.180074838169 | 5.96617753626e-58 |
| chi_5 | 0 | -0.635062456015 | 0.635062456015 | 1.43283593401e-50 |
| 11a1 | 0 | -0.991071123002 | 0.991071123002 | 1.13070309175e-17 |
| 14a1 | 0 | -0.846788401728 | 0.846788401728 | 3.24025668567e-15 |
| 37a1 | 0 | 1.14380303702 | -1.14380297955 | 5.74730912207e-8 |

The displayed O(1) parts must not be subtracted at their printed precision to recover epsilon; the raw ball computations verify the cancellation before rounding.

### Shared conductor-scaled slope test (FLOATING)

Both rank-zero curves at N=60, x≥13: separate intercepts, one common slope. Each model has three parameters and uses exactly the same knots.

| common variable | points | common slope | RMS residual | max residual |
|---|---|---|---|---|
| sqrt(x) | 32 | 2.874362 | 0.2290725 | 0.4743257 |
| sqrt(x/C) | 32 | 10.11247 | 0.08568873 | 0.1810935 |

### Error fits and late-window robustness (FLOATING)

| curve | N | quantity | range | digits/x | RMS x | digits/sqrt(x/C) | RMS sqrt |
|---|---|---|---|---|---|---|---|
| 11a1 | 60 | epsE | 13–50 | 0.2805567 | 0.2995184 | 10.18937 | 0.08788969 |
| 11a1 | 60 | error | 13–50 | 0.2645802 | 0.2466754 | 9.598545 | 0.09792132 |
| 11a1 | 120 | epsE | 13–25 | 0.3711897 | 0.1078897 | 10.69641 | 0.03522068 |
| 11a1 | 120 | error | 13–25 | 0.3411622 | 0.08827327 | 9.827228 | 0.02373476 |
| 14a1 | 60 | epsE | 13–50 | 0.2441695 | 0.2913558 | 10.01459 | 0.07435942 |
| 14a1 | 60 | error | 13–50 | 0.2300957 | 0.2453149 | 9.427203 | 0.07564523 |
| 14a1 | 120 | epsE | 13–25 | 0.3162483 | 0.0339899 | 10.24197 | 0.08013304 |
| 14a1 | 120 | error | 13–25 | 0.2886464 | 0.04732317 | 9.338886 | 0.09677314 |

### Individual prime-power Rayleigh terms at x=50,N=60

| prime power | zeta | chi_-4 | 11a1 | 14a1 | 37a1 |
|---|---|---|---|---|---|
| 2 | -0.08983809962 | 0 | 0.821134188485 | 0.442518830164 | 0.304000513398 |
| 3 | -0.002139120699 | 0.193965236725 | 0.191264351986 | 0.463344985304 | -0.730379119736 |
| 4 | -1.457698748e-5 | 0 | 0 | -0.0532766445839 | 0 |
| 5 | -3.345071777e-7 | -0.0146576233203 | -0.0319530755788 | 0 | -0.581156686974 |
| 7 | -4.030585190e-11 | 0.000783411111207 | 0.0116071670276 | -0.0110131768598 | -0.162982418906 |
| 11 | -8.351439361e-19 | 1.37446566465e-6 | -0.000259415805614 | 0 | -0.198363144227 |
| 23 | -1.052993032e-40 | 4.96886063076e-16 | 6.72232584814e-8 | 0 | 0.00113912304248 |
| 49 | -5.304360530e-106 | -9.53373420948e-53 | 4.08111561210e-18 | -6.70642211702e-17 | -1.37156749856e-9 |


<!-- E4_TABLES_END -->

## E5. Interpretation (incremental)

**PROVED algebra, conditional interpretation.** The difference in the explicit formula can be located precisely. Near y=0, `rho_(1,1)(y)~1/y`, whereas `rho_(2,1/2)(y)~1/(2y)`. Their Fourier multipliers have high-frequency terms

`h_E(t)~log(C t^2/(4 pi^2))`,
`h_chi(t)~log(q |t|/(2 pi))`,
`h_zeta(t)~log(|t|/(2 pi))`.

This gives the respective turning frequencies `T*=2 pi sqrt(x/C)`, `2 pi x/q`, `2 pi x` when the leading symbol is equated to `log x`. For the leading Weyl models, define `S_max=max_T [T log(x)/(2 pi)-N_Weyl(T)]`. Then `S_max=2 sqrt(x/C)` for elliptic curves, `x/q` for primitive Dirichlet characters, and `x` for zeta. The associated integrated leading-symbol action is

`A=int_0^T* [log x-h_asymp(t)] dt=2 pi S_max`,

namely `4 pi sqrt(x/C)`, `2 pi x/q`, `2 pi x`. This identity is just integration of `d log t` with d=2 or 1; it is not an estimate for the Weil minimizer. E1b and the CCM heuristic can therefore be stated uniformly as **H-CONCENTRATION-TRANSFER: `log eps=-2 A+O(log A)`**, or `eps` exponential in `-4 pi S_max`, after sufficiently resolving N. The integral uses the leading symbol down to zero only as an algebraic model; the exact digamma symbol has low-frequency corrections. The identification with the arithmetic minimizer, its sector and prefactor remains OPEN.

**NUMERICAL reading of the controls.** The same window does not give the same gamma operator. Its spectrum changes by degree and gamma shift, and by the exact conductor identity shift. The complete controls in E4 have order-one low eigenvalues; none by itself displays the small positive residual of the full form. At matched x=50,N=60, zeta's pole `+1.62205`, gamma `-1.53005` and prime sum `-0.0919921` cancel, while 11a1's pole-free gamma-plus-conductor value `-0.991071` cancels against a positive total prime quotient `+0.991071`. Individual elliptic prime terms have both signs and some vanish. Even the near-edge k=49 contribution is `4.08112e-18` for 11a1, only about 0.36 eps at N=60; the zeta contribution is negative and about `3.0e10 eps`. The zeta claim that every interior atom dominates eps by enormous factors does not transfer to elliptic curves.

**SHARPENED causal conclusion.** The absence of a pole alone cannot explain the square-root rate: lane D's pole-free degree-one examples already have conductor-scaled linear-x behavior. Nor is a uniform doubling of prime atoms the mechanism—there is no such doubling in the implemented distribution. The archimedean degree and conductor specify a different functional-equation transform (Hankel rather than additive Fourier) and a different phase-space scale. Arithmetic still supplies the cancellation, the actual minimizing vector and finite-range fluctuations. The experiments support concentration kinematics **after incorporating the gamma factor, conductor and arithmetic functional equation**. They do not prove that rho alone, a Weyl law alone, arbitrary signed atoms of degree two, or the empty-prime control forces the rate. These distinctions resolve the ambiguity of “kinematic”: the bare window/Loewner structure is insufficient; the proposed invariant is the transform concentration action A, conditional on H-CONCENTRATION-TRANSFER.

**NUMERICAL provisional verdict from completed x≤50 runs.** H-WINDOW-ONLY is refuted as a description of the tested range: roughly 0.28/0.24 digits per x in the fixed-N elliptic fits versus 5.38 for resolved zeta, and sqrt(x) gives much smaller residuals over 13–50. H-RATE receives quantitative support: a common slope in sqrt(x/C), with separate curve intercepts, has RMS 0.08569 digits, versus 0.22907 for a common slope in sqrt(x). Both have three fitted parameters. This does not logically rule out a completely different eventual asymptotic after the sampled range. A final verdict on the preferred leading constant awaits the long run below.
