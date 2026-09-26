## E4. Tables (generated; NUMERICAL unless labelled FLOATING)

Eigenvalues and inertia are certified in the raw files. COMPARISON errors use approximate PARI zeros; all slopes, fits and ratios computed here are FLOATING. “Final N” is a finite-resolution proxy, not a bound on the infinite-N tail.

### Run completion

| file | checks | failures |
|---|---|---|
| rtp2_ellcurve_11a1_axisN_x100.txt | RUNNING | — |
| rtp2_ellcurve_11a1_axisN_x13.txt | 1255 | 0 |
| rtp2_ellcurve_11a1_axisN_x25.txt | 1623 | 0 |
| rtp2_ellcurve_11a1_axisN_x50.txt | RUNNING | — |
| rtp2_ellcurve_11a1_axisx_ccm_N120.txt | RUNNING | — |
| rtp2_ellcurve_11a1_axisx_ccm_N200.txt | RUNNING | — |
| rtp2_ellcurve_11a1_axisx_ccm_N60.txt | 363 | 0 |
| rtp2_ellcurve_11a1_spectra_x13.txt | 492 | 0 |
| rtp2_ellcurve_11a1_spectra_x25.txt | 492 | 0 |
| rtp2_ellcurve_11a1_spectra_x50.txt | 492 | 0 |
| rtp2_ellcurve_14a1_axisN_x13.txt | 1255 | 0 |
| rtp2_ellcurve_14a1_axisN_x25.txt | 1623 | 0 |
| rtp2_ellcurve_14a1_axisN_x50.txt | RUNNING | — |
| rtp2_ellcurve_14a1_axisx_ccm_N120.txt | RUNNING | — |
| rtp2_ellcurve_14a1_axisx_ccm_N60.txt | 363 | 0 |
| rtp2_ellcurve_14a1_spectra_x13.txt | 492 | 0 |
| rtp2_ellcurve_14a1_spectra_x25.txt | 492 | 0 |
| rtp2_ellcurve_14a1_spectra_x50.txt | 492 | 0 |
| rtp2_ellcurve_37a1_axisN_x13.txt | 1248 | 0 |
| rtp2_ellcurve_37a1_axisN_x25.txt | 1615 | 0 |
| rtp2_ellcurve_37a1_axisN_x50.txt | RUNNING | — |
| rtp2_ellcurve_37a1_axisx_ccm_N120.txt | RUNNING | — |
| rtp2_ellcurve_37a1_axisx_ccm_N60.txt | 338 | 0 |
| rtp2_ellcurve_diagnostic_x2_N200.txt | RUNNING | — |
| rtp2_ellcurve_pilot_11a1.txt | 399 | 0 |

Completed checks: 13034 

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
| 14a1 | 60 | 24 | 50 | 3.24025668567e-15 | 3.70122291569e-12 | 0 | none |
| 37a1 | 60 | 24 | 50 | 9.90422454756e-6 | 5.74730912207e-8 | 0 | 4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41,43,47,49,50 |

### Linearising variable: equal-weight least squares (FLOATING)

Fit log10(epsE)=intercept−slope×variable over every printed knot with x≥13. RMS and max residuals are in decimal digits. The last two variables necessarily have identical residuals within each curve.

| curve | N | range | knots | variable | slope | RMS residual | max residual |
|---|---|---|---|---|---|---|---|
| 11a1 | 60 | 13–50 | 16 | x | 0.2805567 | 0.2995184 | 0.7558394 |
| 11a1 | 60 | 13–50 | 16 | sqrt(x) | 3.072212 | 0.08788969 | 0.1852243 |
| 11a1 | 60 | 13–50 | 16 | sqrt(x/C) | 10.18937 | 0.08788969 | 0.1852243 |
| 14a1 | 60 | 13–50 | 16 | x | 0.2441695 | 0.2913558 | 0.5033498 |
| 14a1 | 60 | 13–50 | 16 | sqrt(x) | 2.676512 | 0.07435942 | 0.115821 |
| 14a1 | 60 | 13–50 | 16 | sqrt(x/C) | 10.01459 | 0.07435942 | 0.115821 |

### Exponential with an algebraic prefactor (FLOATING)

Fit ln eps=a+b ln z−k z, z=sqrt(x/C), on the same knots (three parameters). Also fit a,b at fixed k=8pi and k=4pi (two parameters). These are finite-range empirical fits, not proofs of a limiting k.

| curve | N | b free | k/(8pi) free | RMS free | b at k=8pi | RMS 8pi | b at k=4pi | RMS 4pi |
|---|---|---|---|---|---|---|---|---|
| 11a1 | 60 | 0.4206909 | 0.9439995 | 0.08781864 | 2.648671 | 0.08980753 | -17.24384 | 0.1729728 |
| 14a1 | 60 | -2.707515 | 0.8414132 | 0.07079716 | 2.885152 | 0.08507807 | -14.74768 | 0.1238119 |

### Archimedean controls and Rayleigh cancellation

| curve | x | N | control min E | control min O | negative E/O | Rayleigh gamma+log C | Rayleigh primes | sum |
|---|---|---|---|---|---|---|---|---|
| 11a1 | 13 | 200 | -1.38957064134 | 0.0566717962475 | 1/0 | -0.867338025611 | 0.867338786198 | 7.60586827693e-7 |
| 11a1 | 25 | 260 | -1.61780175257 | -0.346411393408 | 1/1 | -0.939853026777 | 0.939853026801 | 2.42148388413e-11 |
| 14a1 | 13 | 200 | -1.14840858453 | 0.297833853064 | 1/0 | -0.722202911951 | 0.722208385932 | 5.47398082239e-6 |
| 14a1 | 25 | 260 | -1.37663969576 | -0.105249336591 | 1/1 | -0.799400476500 | 0.799400477508 | 1.00853123507e-9 |
| 37a1 | 13 | 200 | -0.176548001496 | 1.26969443609 | 1/0 | 1.40825013735 | -1.39607539391 | 0.0121747434397 |
| 37a1 | 25 | 260 | -0.404779112728 | 0.866611246438 | 1/0 | 1.23351378318 | -1.23343231395 | 8.14692310352e-5 |

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

