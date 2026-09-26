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

11. **SHARPENED.** MVP-3's “only twice as bad” for conductor 14 was a short-window observation. The first-zero-error ratio 14a1/11a1 is about 2.09 at x=13 but 77.53 at x=50 (final-N proxies). It is not a window-independent conductor prefactor.

## E1. Predictions recorded before new runs

**PREDICTION E1a — OPEN (H-WINDOW-ONLY).** If the very same CCM Fourier-prolate parameter controls the new Weil minimizer, then

`eps_E(x) ~ A_E x^b exp(-4 pi x)`.

CCM §7 prints the zeta leakage `const x^(9/2) exp(-4 pi x)` in `refs/src/2511.22755/mc2arXiv.tex:1324–1329`; transfer to the Weil minimizer is explicitly heuristic there. The asymptotic rate is `4 pi/log(10)=5.4575054` decimal digits per unit x. Importing also zeta's pole-constrained sector `b=9/2` gives 5.3863535 digits/x over 13–50; that power is not justified for a pole-free weight-two form. The unchanged log window `[0,log x]` and Fourier basis do not establish H-WINDOW-ONLY. The archimedean data change from `rho_(2,1/2)(y)` to `rho_(1,1)(y)=exp(-y)/(1-exp(-y))`, and the atoms and pole constraints also change.

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
| rtp2_ellcurve_11a1_axisN_x100.txt | 2565 | 0 |
| rtp2_ellcurve_11a1_axisN_x13.txt | 1255 | 0 |
| rtp2_ellcurve_11a1_axisN_x25.txt | 1623 | 0 |
| rtp2_ellcurve_11a1_axisN_x50.txt | 2581 | 0 |
| rtp2_ellcurve_11a1_axisx_ccm_N120.txt | 213 | 0 |
| rtp2_ellcurve_11a1_axisx_ccm_N200.txt | 612 | 0 |
| rtp2_ellcurve_11a1_axisx_ccm_N60.txt | 363 | 0 |
| rtp2_ellcurve_11a1_spectra_x13.txt | 492 | 0 |
| rtp2_ellcurve_11a1_spectra_x25.txt | 492 | 0 |
| rtp2_ellcurve_11a1_spectra_x50.txt | 492 | 0 |
| rtp2_ellcurve_14a1_axisN_x13.txt | 1255 | 0 |
| rtp2_ellcurve_14a1_axisN_x25.txt | 1623 | 0 |
| rtp2_ellcurve_14a1_axisN_x50.txt | 2581 | 0 |
| rtp2_ellcurve_14a1_axisx_ccm_N120.txt | 213 | 0 |
| rtp2_ellcurve_14a1_axisx_ccm_N60.txt | 363 | 0 |
| rtp2_ellcurve_14a1_spectra_x13.txt | 492 | 0 |
| rtp2_ellcurve_14a1_spectra_x25.txt | 492 | 0 |
| rtp2_ellcurve_14a1_spectra_x50.txt | 492 | 0 |
| rtp2_ellcurve_37a1_axisN_x13.txt | 1248 | 0 |
| rtp2_ellcurve_37a1_axisN_x25.txt | 1615 | 0 |
| rtp2_ellcurve_37a1_axisN_x50.txt | 2573 | 0 |
| rtp2_ellcurve_37a1_axisx_ccm_N120.txt | 198 | 0 |
| rtp2_ellcurve_37a1_axisx_ccm_N60.txt | 338 | 0 |
| rtp2_ellcurve_389a1_record.txt | 16 | 0 |
| rtp2_ellcurve_diagnostic_x2_N200.txt | 1223 | 0 |
| rtp2_ellcurve_pilot_11a1.txt | 399 | 0 |

Completed checks: 25809 

### Resolution and parity

N_sat is certified only on 1..Nmax. A value of 1 is left-censored (N=0 is not scanned).

| curve | x | final N | N_sat full/E/O | N_sat/[sqrt(x/C) log x] | epsE at N_sat | epsE final | epsO final | min parity |
|---|---|---|---|---|---|---|---|---|
| 11a1 | 13 | 200 | 3/3/3 | 1.075888 | 2.43947834223e-6 | 7.60586827693e-7 | 0.000145476586851 | E |
| 11a1 | 25 | 260 | 6/6/6 | 1.236441 | 1.23500169465e-10 | 2.42148388413e-11 | 1.16472149147e-8 | E |
| 11a1 | 50 | 420 | 10/10/10 | 1.198974 | 2.96546081715e-16 | 9.12480919174e-18 | 1.40828068046e-14 | E |
| 11a1 | 100 | 420 | 18/18/18 | 1.296353 | 1.58348262006e-25 | 5.86752032195e-27 | 1.17910130007e-23 | E |
| 14a1 | 13 | 200 | 2/2/2 | 0.809177 | 2.34714132383e-5 | 5.47398082239e-6 | 0.000879747523219 | E |
| 14a1 | 25 | 260 | 4/4/4 | 0.929929 | 1.14921916973e-8 | 1.00853123507e-9 | 4.92836083075e-7 | E |
| 14a1 | 50 | 420 | 10/10/10 | 1.352626 | 1.60944223785e-14 | 2.82763646403e-15 | 3.39392540313e-12 | E |
| 37a1 | 13 | 200 | 1/1/1 | 0.6577341 | 0.444699197675 | 0.203253993996 | 0.0121747434397 | O |
| 37a1 | 25 | 260 | 3/2/3 | 1.13383 | 0.0154330254295 | 0.00638896651436 | 8.14692310352e-5 | O |
| 37a1 | 50 | 420 | 4/4/4 | 0.8795782 | 4.58659785715e-5 | 9.64405083618e-6 | 5.24270827475e-8 | O |

### COMPARISON at final N

| curve | x | N | first-zero error (PARI) | error/epsE |
|---|---|---|---|---|
| 11a1 | 13 | 200 | 0.000406325112562 | 534.225807978 |
| 11a1 | 25 | 260 | 3.07075607533e-8 | 1268.12988327 |
| 11a1 | 50 | 420 | 2.23555751598e-14 | 2449.97727515 |
| 11a1 | 100 | 420 | 2.24609323766e-23 | 3828.01100706 |
| 14a1 | 13 | 200 | 0.000850124715393 | 155.302830422 |
| 14a1 | 25 | 260 | 3.46751133644e-7 | 343.817941960 |
| 14a1 | 50 | 420 | 1.73314985464e-12 | 612.932347098 |
| 37a1 | 13 | 200 | inapplicable | — |
| 37a1 | 25 | 260 | inapplicable | — |
| 37a1 | 50 | 420 | inapplicable | — |

### Finite-N tails and Schur envelopes

| curve | x | tail N | epsE(previous)/final | epsO(previous)/final | epsE(60)/final | joint radius | Delta I (nats) | truth tau | sE next | sO next |
|---|---|---|---|---|---|---|---|---|---|---|
| 11a1 | 13 | 120→200 | 1.00162 | 1.014255 | 1.009299 | 8.560739087 | 0.009474191792 | -0.06574159550 | 10.48797386 | 10.48091321 |
| 11a1 | 25 | 200→260 | 1.001408 | 1.008096 | 1.03953 | 9.331564655 | 0.005152022584 | -0.03400086471 | 12.51575012 | 12.50887664 |
| 11a1 | 50 | 200→420 | 1.018217 | 1.028053 | 1.239153 | 8.304630421 | 0.009342921749 | -0.04101800643 | 8.947251868 | 8.942136536 |
| 11a1 | 100 | 200→420 | 1.049451 | 1.01304 | 1.213812 | 7.955294327 | 0.006068803734 | 0.01252111548 | 10.16302903 | 10.15903376 |
| 14a1 | 13 | 120→200 | 1.000946 | 1.010945 | 1.004876 | 9.061980277 | 0.003337548209 | -0.03726779845 | 12.13535849 | 12.13008886 |
| 14a1 | 25 | 200→260 | 1.001068 | 1.007451 | 1.028396 | 9.165456007 | 0.009095556477 | -0.06129854322 | 12.87675022 | 12.87175599 |
| 14a1 | 50 | 200→420 | 1.009904 | 1.031173 | 1.145924 | 8.620815502 | 0.03742308982 | -0.1280645303 | 11.07171177 | 11.06539386 |
| 37a1 | 13 | 120→200 | 1.000303 | 1.007172 | 1.001335 | 10.16449852 | 0.01007585665 | -0.05741680830 | 13.06752973 | 13.06151881 |
| 37a1 | 25 | 200→260 | 1.000285 | 1.006108 | 1.005063 | 10.43396171 | 0.008180241610 | -0.05374122031 | 13.08917020 | 13.08321148 |
| 37a1 | 50 | 200→420 | 1.002189 | 1.02234 | 1.026978 | 10.23933127 | 0.01705629816 | -0.08580483924 | 13.16772720 | 13.16303506 |

### Final-N endpoint slopes (FLOATING, positive digits gained)

| curve | range x | E digits/x | E digits/sqrt x | E digits/sqrt(x/C) | O digits/x | error digits/x |
|---|---|---|---|---|---|---|
| 11a1 | 13–25 | 0.3747556 | 3.224979 | 10.69604 | 0.3413809 | 0.343469 |
| 11a1 | 25–50 | 0.2569543 | 3.101713 | 10.28722 | 0.2367013 | 0.2455144 |
| 11a1 | 13–50 | 0.2951601 | 3.151312 | 10.45172 | 0.2706515 | 0.2772835 |
| 11a1 | 50–100 | 0.1838354 | 3.138266 | 10.40845 | 0.1815428 | 0.1799592 |
| 11a1 | 13–100 | 0.2311804 | 3.145337 | 10.4319 | 0.2194396 | 0.22135 |
| 14a1 | 13–25 | 0.3112178 | 2.678201 | 10.02091 | 0.2709713 | 0.2824554 |
| 14a1 | 25–50 | 0.2220906 | 2.680871 | 10.0309 | 0.20648 | 0.2120473 |
| 14a1 | 13–50 | 0.2509967 | 2.679797 | 10.02688 | 0.2273961 | 0.2348823 |
| 37a1 | 13–25 | 0.1252174 | 1.077565 | 6.554569 | 0.1812055 | — |
| 37a1 | 25–50 | 0.1128468 | 1.362182 | 8.285829 | 0.1276575 | — |
| 37a1 | 13–50 | 0.1168589 | 1.247658 | 7.589208 | 0.1450244 | — |

### CCM axis-x coverage

| curve | N | knots | last x | last epsE | last epsO | indefinite knots | odd-minimum windows |
|---|---|---|---|---|---|---|---|
| 11a1 | 60 | 24 | 50 | 1.13070309175e-17 | 1.50548637447e-14 | 0 | none |
| 11a1 | 120 | 14 | 25 | 2.44005541640e-11 | 1.19859483614e-8 | 0 | none |
| 11a1 | 200 | 36 | 100 | 6.15767339764e-27 | 1.19447712984e-23 | 0 | none |
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
| 11a1 | 200 | 13–100 | 28 | x | 0.2270742 | 0.7290918 | 1.745904 |
| 11a1 | 200 | 13–100 | 28 | sqrt(x) | 3.148805 | 0.1221076 | 0.2790916 |
| 11a1 | 200 | 13–100 | 28 | sqrt(x/C) | 10.4434 | 0.1221076 | 0.2790916 |
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
| 11a1 | 200 | 0.7031034 | 0.9710677 | 0.1215419 | 2.103295 | 0.1238092 | -22.09439 | 0.4027925 |
| 14a1 | 60 | -2.707515 | 0.8414132 | 0.07079716 | 2.885152 | 0.08507807 | -14.74768 | 0.1238119 |
| 14a1 | 120 | 31.09725 | 2.015498 | 0.02910617 | 1.853983 | 0.07608491 | -12.5445 | 0.1088726 |

### Archimedean controls and Rayleigh cancellation

| curve | x | N form | N control | control min E | control min O | negative E/O | Rayleigh gamma+log C | Rayleigh primes | sum |
|---|---|---|---|---|---|---|---|---|---|
| 11a1 | 13 | 200 | 200 | -1.38957064134 | 0.0566717962475 | 1/0 | -0.867338025611 | 0.867338786198 | 7.60586827693e-7 |
| 11a1 | 25 | 260 | 260 | -1.61780175257 | -0.346411393408 | 1/1 | -0.939853026777 | 0.939853026801 | 2.42148388413e-11 |
| 11a1 | 50 | 420 | 120 | -1.78621644865 | -0.672179621029 | 1/1 | -0.991414691509 | 0.991414691509 | 9.12480919174e-18 |
| 11a1 | 100 | 420 | 120 | -1.90745980173 | -0.928628119398 | 2/1 | -1.02220094661 | 1.02220094661 | 5.86752032195e-27 |
| 14a1 | 13 | 200 | 200 | -1.14840858453 | 0.297833853064 | 1/0 | -0.722202911951 | 0.722208385932 | 5.47398082239e-6 |
| 14a1 | 25 | 260 | 260 | -1.37663969576 | -0.105249336591 | 1/1 | -0.799400476500 | 0.799400477508 | 1.00853123507e-9 |
| 14a1 | 50 | 420 | 120 | -1.54505439183 | -0.431017564212 | 1/1 | -0.847021092403 | 0.847021092403 | 2.82763646403e-15 |
| 37a1 | 13 | 200 | 200 | -0.176548001496 | 1.26969443609 | 1/0 | 1.40825013735 | -1.39607539391 | 0.0121747434397 |
| 37a1 | 25 | 260 | 260 | -0.404779112728 | 0.866611246438 | 1/0 | 1.23351378318 | -1.23343231395 | 8.14692310352e-5 |
| 37a1 | 50 | 420 | 120 | -0.573193808804 | 0.540843018817 | 1/0 | 1.14319718603 | -1.14319713360 | 5.24270827475e-8 |

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

| object | N_sat at 13,25,50 | epsE at 13 | epsE at 25 | epsE at 50 | digits/x 13–25 | digits/x 13–50 | provenance |
|---|---|---|---|---|---|---|---|
| zeta | 56,134,352 | 2.85407e-59 | 2.42562e-123 | 2.80881e-258 | 5.33922 | 5.378566 | review N=420 at x50 |
| chi_-4 | 11,30,pending | 3.55108899176e-14 | 5.39464993971e-30 | pending | 1.3182 | pending | completed lane D only |
| chi_-3 | 17,41,pending | 1.25308864637e-19 | 5.92330252137e-41 | pending | 1.777118 | pending | completed lane D only |
| chi_5 | 7,23,pending | 2.10790657667e-12 | 3.66818026982e-25 | pending | 1.063283 | pending | completed lane D only |
| chi_8 | 4,13,pending | 2.17699319902e-7 | 2.30737261661e-15 | pending | 0.6645616 | pending | completed lane D only |
| chi_-7 | 4,13,pending | 2.03745394328e-7 | 3.27263403207e-16 | pending | 0.7328492 | pending | completed lane D only |
| chi_12 | 2,7,pending | 0.000115817314349 | 6.71343285554e-10 | pending | 0.4364024 | pending | completed lane D only |
| chi_-20 | 1,3,pending | 0.0987740569268 | 0.000267954162959 | pending | 0.2138819 | pending | completed lane D only |
| chi_21 | 2,2,pending | 0.0232509738349 | 3.58458347666e-5 | pending | 0.2343335 | pending | completed lane D only |
| chi_13 | 2,7,pending | 0.000402786486930 | 4.55002293950e-9 | pending | 0.4122551 | pending | completed lane D only |
| chi_-8 | 2,13,pending | 4.53702800257e-6 | 1.00380725322e-13 | pending | 0.6379268 | pending | completed lane D only |
| 11a1 | 3,6,10 | 7.60586827693e-7 | 2.42148388413e-11 | 9.12480919174e-18 | 0.3747556 | 0.2951601 | E block; 37a1 global O |
| 14a1 | 2,4,10 | 5.47398082239e-6 | 1.00853123507e-9 | 2.82763646403e-15 | 0.3112178 | 0.2509967 | E block; 37a1 global O |
| 37a1 | 1,3,4 | 0.203253993996 | 0.00638896651436 | 9.64405083618e-6 | 0.1252174 | 0.1168589 | E block; 37a1 global O |

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
| 11a1 | 200 | epsE | 13–100 | 0.2270742 | 0.7290918 | 10.4434 | 0.1221076 |
| 11a1 | 200 | epsE | 53–100 | 0.1747772 | 0.1085843 | 10.07894 | 0.07865293 |
| 11a1 | 200 | error | 13–100 | 0.2187673 | 0.6435573 | 10.04783 | 0.1471212 |
| 11a1 | 200 | error | 53–100 | 0.1710572 | 0.1036404 | 9.863292 | 0.08174534 |
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

### Leading phase-space normalization (FLOATING)

S_max=x for zeta, x/q for primitive degree one, 2 sqrt(x/C) for weight two. The conditional universal prediction is 4pi/log(10)=5.457505 digits per unit S_max.

| object | range | digits per S_max |
|---|---|---|
| zeta | 13–25 | 5.33922 |
| zeta | 13–50 | 5.378566 |
| chi_-4 | 13–25 | 5.272799 |
| chi_-3 | 13–25 | 5.331354 |
| chi_5 | 13–25 | 5.316417 |
| chi_8 | 13–25 | 5.316493 |
| chi_-7 | 13–25 | 5.129944 |
| chi_12 | 13–25 | 5.236829 |
| chi_-20 | 13–25 | 4.277637 |
| chi_21 | 13–25 | 4.921004 |
| chi_13 | 13–25 | 5.359316 |
| chi_-8 | 13–25 | 5.103414 |
| 11a1 | 13–25 | 5.348022 |
| 11a1 | 13–50 | 5.22586 |
| 11a1 | 50–100 | 5.204226 |
| 14a1 | 13–25 | 5.010455 |
| 14a1 | 13–50 | 5.013441 |

### Fixed-N Schur envelope at matched windows

| curve | x | N | epsE | joint radius | Delta I | truth tau | first-zero error (PARI) | error/eps |
|---|---|---|---|---|---|---|---|---|
| 11a1 | 13 | 60 | 7.67659737296e-7 | 6.207542468 | 0.009347975332 | -0.03236896692 | 0.000409577219972 | 533.540056972 |
| 11a1 | 25 | 60 | 2.51720545071e-11 | 6.700113821 | 0.01102715488 | 0.03785857335 | 3.18346151920e-8 | 1264.68084609 |
| 11a1 | 50 | 60 | 1.13070309175e-17 | 5.971490306 | 0.02766198528 | -0.06956115282 | 2.75848146010e-14 | 2439.61609394 |
| 14a1 | 13 | 60 | 5.50067277783e-6 | 6.852889139 | 0.005081645411 | -0.03407901961 | 0.000853571315821 | 155.175803088 |
| 14a1 | 25 | 60 | 1.03716912030e-9 | 6.442750617 | 0.006318856650 | -0.008505970666 | 3.56036486397e-7 | 343.277175756 |
| 14a1 | 50 | 60 | 3.24025668567e-15 | 6.358497438 | 0.01413511748 | -0.04653131703 | 1.97887413662e-12 | 610.715239126 |


<!-- E4_TABLES_END -->

**NUMERICAL visualization.** [Rate fits and residuals](checks/rate_fits.png), also [PDF](checks/rate_fits.pdf), generated by `checks/plot.py`. The figure uses 11a1 at N=200 through 100 and 14a1 at N=60 through 50; fits and residuals are floating. It does not extrapolate outside those ranges.

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

**NUMERICAL verdict from the two-curve x≤50 comparison.** H-WINDOW-ONLY is refuted as a description of the tested range: roughly 0.28/0.24 digits per x in the fixed-N elliptic fits versus 5.38 for resolved zeta, and sqrt(x) gives much smaller residuals over 13–50. H-RATE receives quantitative support: a common slope in sqrt(x/C), with separate curve intercepts, has RMS 0.08569 digits, versus 0.22907 for a common slope in sqrt(x). Both have three fitted parameters. This does not logically rule out a completely different eventual asymptotic after the sampled range. The long run supplies the additional test below.

**PROVED / NUMERICAL extra control.** The digamma series gives `Re psi(1+it)>=psi(1)=-EulerGamma`. Hence the elliptic control is positive on every window and every finite Fourier space whenever `C>4 pi^2 exp(2 EulerGamma)`. This is a sufficient, not necessary, condition. As a further check using the fourth existing PARI model, `outputs/rtp2_ellcurve_389a1_record.txt` records x=13,N=60 at 700 bits: the full form has an odd minimum (rank 2, root number +1), while its prime-free control is positive in both blocks. No zero comparison is made. Thus even within weight two, “the archimedean control must be indefinite” would be false. Positivity of a control does not establish a concentration rate for the full form.


**NUMERICAL long-window verdict.** All 36 independently certified N=200 CCM knots through x=100 are complete. On the 28 knots from 13 through 100, fitting log10 eps against x gives 0.227074 digits/x with RMS residual 0.729092 digits; against sqrt(x/C) it gives 10.4434 digits per unit with RMS 0.122108 digits. Thus the square-root variable reduces RMS by a factor 5.97. The comparison error similarly gives RMS 0.643557 (x) versus 0.147121 (sqrt(x/C)). The last point is epsE `6.15767339764e-27`, epsO `1.19447712984e-23`, error `2.35516405250e-23`, error/eps `3824.76286158`; its 2000-bit recheck agrees with the 1000-bit point to every displayed digit.

**SHARPENED H-RATE status.** Supported numerically as the correct tested window variable; OPEN as an asymptotic theorem. E1b's stronger leading constant is compatible with the long data, but is not determined by them: fitting `ln eps=a+b ln z-k z` at z=sqrt(x/11) gives k/(8pi)=0.971068 and b=0.703103, RMS 0.121542 digits. Fixing k=8pi and refitting only a,b gives b=2.10330 and RMS 0.123809, nearly as good; fixing k=4pi gives b=-22.0944 and RMS 0.402793. This favors the optimized-Hankel prediction over the bare squared-Mellin-tail constant within the tested model class. It does not prove the coefficient 8pi, the power b, or convergence of the prefactor. The shorter 53–100 segment has slope 10.0789 in z with RMS 0.07865, so a single fitted slope must not be advertised as an asymptotic limit. The error/eps ratio changes from about 534 to 3825 across the long interval; equality of their leading exponential is compatible with a drifting algebraic factor, not a constant ratio.

**NUMERICAL Schur conclusion.** The Loewner posterior interval is a different observable from eps. At fixed N=60, the joint half-width for 11a1 is 6.20754, 6.70011, 5.97149 at x=13,25,50, while eps loses nearly eleven decimal digits. For 14a1 those widths are 6.85289, 6.44275, 6.35850. The truth positions stay interior, and Delta I remains below 0.028 nats at these six points. H-RATE describes the near-null eigenvalue and associated spectral error, not exponential contraction of this one-coordinate Schur envelope.


**NUMERICAL resolution audit at x=50.** At N=420 the rank-zero minima are `9.12480919174e-18` (11a1) and `2.82763646403e-15` (14a1). Their 13–50 endpoint rates are respectively 0.2951601 and 0.2509967 digits/x, or 10.45172 and 10.02688 digits per sqrt(x/C); the first-zero-error rates are 0.2772835 and 0.2348823 digits/x. At the same x,N the 37a1 even/odd minima are `9.64405083618e-6` and `5.24270827475e-8`, decisively odd. At N=200 the two rank-zero even minima exceed their N=420 values by 1.82% and 0.99%, respectively. Thus the large object-dependent rate difference survives a direct finite-N tail check. This is empirical saturation, not a rigorous bound on all further N.


**NUMERICAL final long-window tail.** At `(11a1,x=100,N=420)`, epsE is `5.86752032195e-27`, epsO is `1.17910130007e-23`, and the minimum remains even. The full/even/odd determinant minima are all N=18 over 1..420. The N=200 even value exceeds the N=420 value by 4.9451%, so the measured long-range law survives the resolution check. Using the final-N endpoints gives 0.1838354 digits/x over 50–100 and 0.2311804 over 13–100; the corresponding sqrt(x/11) rates are 10.40845 and 10.43190. The first-zero error at N=420 is `2.24609323766e-23`, ratio `3828.01100706`. The 1000/1400-bit long runs needed no precision rescue; the extra 2000-bit check was an independent validation.

**NUMERICAL completion and provenance.** All 26 final output files are complete: 25,809 driver checks, zero failures. The separate output audit passes 3,783 checks; independent quadrature passes 36; four precision reruns agree in both eigenvalues and parity; the pilot reruns byte-identically. `make -C zst check` passes. `checks/audit.txt`, `checks/source_manifest.sha256`, `checks/final_check_count.txt`, `checks/byte_reproducibility.txt` and `checks/make-check.txt` retain the evidence. Numerical job timings are in `checks/runlogs`; the experiment finished comfortably inside the 90-minute allowance (about 38 minutes from the recorded pre-run predictions to the last numerical job). A shell coordinator reread its file during editing after all its numerical jobs had succeeded; the final settled `RESUME=1` run rebuilt the aggregate and exited zero. This affected no certificate. Interrupted development outputs are separate from the final outputs.

**NUMERICAL lane-D boundary at completion.** All ten characters' x=13 and x=25 completed outputs and the completed N=60 CCM Rayleigh tables were reused. Lane D's x=50 resolution files still lack completion markers at this snapshot and were excluded, as were any final-asymptotic claims depending on those pending jobs. The comparative table marks them pending; this is not missing elliptic work. The old zeta supplement at x=50,N=420 is explicitly attributed to the round-1 review, not to an invented rerun.

## Numerical checks for the blind lane

**NUMERICAL; certified eigenvalues, rounded to the displayed digits.** The first three cards are the global eps_N, together with the other block so parity can be checked independently:

| curve | x | N | epsE | epsO | global minimum |
|---|---:|---:|---|---|---|
| 11a1 | 13 | 200 | 7.60586827693e-7 | 0.000145476586851 | even |
| 14a1 | 25 | 260 | 1.00853123507e-9 | 4.92836083075e-7 | even |
| 37a1 | 50 | 420 | 9.64405083618e-6 | 5.24270827475e-8 | odd |

**NUMERICAL certificate cards.** For 11a1 at x=50, the unique full/even/odd determinant minimizers over 1..420 are all N=10. At x=50,N=60 its gamma-plus-conductor control has inertia (negative,zero,positive) `(1,0,60)` in E and `(1,0,59)` in O. Its least control eigenvalues are `-1.78617585006` and `-0.66996782106` (complete isolating intervals in the spectrum file).

**FLOATING slope card.** From `(11a1,13,200)` to `(11a1,50,420)`, the positive epsE slope is `0.2951601` decimal digits per x, or `10.45172` per sqrt(x/11). This endpoint slope differs from a least-squares slope across knots; the fit definition matters. **NUMERICAL COMPARISON card:** at `(11a1,50,420)`, the PARI-based first-zero error is `2.23555751598e-14`, ratio to eps `2449.97727515`; the construction's 420 roots are certified, the external PARI zero is approximate.

Reproduce the main experiment with `make -C zst build/rtp2_ellcurve` then `zst/tools/rtp2_ellcurve_run.sh` (12 jobs by default, optional RESUME=1). `checks/summary.py` prints the tables; `checks/audit.py` checks the output protocol, parity, roots, determinant extraction and all control spectral shifts; `checks/reproduce_extras.sh` reproduces the pilot byte check, extra precision checks and independent quadrature; `checks/plot.py` regenerates the figure. All scripts run from the repository root or find it from their own location. The run script builds the driver outside `all`.

## What this changes in the notebook

**SHARPENED H-RATE.** Replace “open, untested window-scale suggestion” by **numerically supported on 11a1/14a1 through x=50 and 11a1 through x=100; asymptotic theorem OPEN**. Specify the scale z=sqrt(x/C), distinguish the elementary Mellin kernel from the gamma-ratio Hankel kernel, and keep `exp(-8pi z)` under H-HANKEL-TRANSFER / H-CONCENTRATION-TRANSFER. The evidence does not establish an exact prefactor, a limiting coefficient, or positivity at all windows.

**Proposed replacement for `obs:rtp-round-1-reading`(iii) — NUMERICAL with an OPEN mechanism.** At resolved finite N, a common dilation window and Loewner/Fourier structure permit very different rates: zeta gives about 5.38 digits/x, whereas 11a1 and 14a1 give 0.295 and 0.251 over the same 13–50 interval. Degree-one character results available from lane D are consistent with scaling x by conductor; weight-two results favor sqrt(x/C). The Schur envelope is not the decaying observable. The proposed common concentration action is `A=2pi S_max`, with `S_max=x`, `x/q`, or `2sqrt(x/C)`; the transfer `log eps=-2A+O(log A)` from Fourier/Hankel concentration to the true Weil minimizer remains OPEN. Arithmetic is necessary for the measured cancellation, while the data support gamma degree and conductor as organizers of its scale. Neither “window kinematics alone determines the rate” nor “the cancellation proves the rate is specific to zeta's individual primes” survives this experiment as an adequate interpretation.

**Candidate claim rows (proposals only; no registration).**

| candidate | status | content / scope |
|---|---|---|
| `num:rtp2-ellcurve-window-rate` | NUMERICAL | E4 finite-N eps, comparison errors, parity and residual tables; H-RATE scale supported on the stated curves and ranges |
| `obs:rtp2-gamma-concentration-action` | OPEN / PROVED-conditional on H-CONCENTRATION-TRANSFER | leading Weyl algebra gives A=d T*; conditional leakage gives degree/conductor rate normalization; no proved link to the Weil minimum |
| `num:rtp2-ellcurve-resolution` | NUMERICAL | determinant minima track sqrt(x/C) log x with order-one factors, not 2x log x; finite-N tails separately quantified |
| `lem:gamma-control-shift-and-lower-bound` | PROVED | at fixed atoms/gamma, conductor changes by an identity shift; elliptic control is uniformly positive for C>4pi² exp(2 EulerGamma), via the digamma series |
| `num:rtp2-ellcurve-parity-window` | NUMERICAL | rank-zero tested minima even; 37a1 switches from even at x=2,3 to odd at tested knots x≥4; 389a1 odd at x=13 despite root number +1 |

**Next experiment — OPEN.** Compute finite Hankel concentration eigenvalues for the gamma-ratio kernel, identify the correct sector and normalization, and compare their defects directly with eps at matched z and several N. In parallel, compare distinct rank-zero isogeny classes at the same conductor and multiple widely separated conductors at matched z. That separates the proposed transform scale from arithmetic-dependent prefactors more sharply than the present pair C=11,14. Extend x only while checking the N tail and the reference-zero precision; none of this licenses an RH assumption or an all-window positivity conclusion.
