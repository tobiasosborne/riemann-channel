# D4 run status (exact counts)

| file | checks | failed |
|---|---|---|
| rtp2_dirichlet_D-20_axisN_x13.txt | 1255 | 0 |
| rtp2_dirichlet_D-20_axisN_x25.txt | RUNNING | - |
| rtp2_dirichlet_D-3_axisN_x13.txt | 1255 | 0 |
| rtp2_dirichlet_D-3_axisN_x25.txt | RUNNING | - |
| rtp2_dirichlet_D-3_axisx_ccm_N120.txt | RUNNING | - |
| rtp2_dirichlet_D-3_axisx_ccm_N60.txt | RUNNING | - |
| rtp2_dirichlet_D-4_axisN_x13.txt | 1255 | 0 |
| rtp2_dirichlet_D-4_axisN_x25.txt | RUNNING | - |
| rtp2_dirichlet_D-4_axisx_ccm_N120.txt | RUNNING | - |
| rtp2_dirichlet_D-4_axisx_ccm_N60.txt | RUNNING | - |
| rtp2_dirichlet_D-7_axisN_x13.txt | 1255 | 0 |
| rtp2_dirichlet_D-7_axisN_x25.txt | RUNNING | - |
| rtp2_dirichlet_D-7_axisx_ccm_N120.txt | RUNNING | - |
| rtp2_dirichlet_D-7_axisx_ccm_N60.txt | RUNNING | - |
| rtp2_dirichlet_D-8_axisN_x13.txt | 1255 | 0 |
| rtp2_dirichlet_D-8_axisN_x25.txt | RUNNING | - |
| rtp2_dirichlet_D12_axisN_x13.txt | 1255 | 0 |
| rtp2_dirichlet_D12_axisN_x25.txt | RUNNING | - |
| rtp2_dirichlet_D12_axisx_ccm_N120.txt | RUNNING | - |
| rtp2_dirichlet_D12_axisx_ccm_N60.txt | RUNNING | - |
| rtp2_dirichlet_D13_axisN_x13.txt | 1255 | 0 |
| rtp2_dirichlet_D13_axisN_x25.txt | RUNNING | - |
| rtp2_dirichlet_D21_axisN_x13.txt | 1255 | 0 |
| rtp2_dirichlet_D21_axisN_x25.txt | RUNNING | - |
| rtp2_dirichlet_D5_axisN_x13.txt | 1255 | 0 |
| rtp2_dirichlet_D5_axisN_x25.txt | RUNNING | - |
| rtp2_dirichlet_D5_axisx_ccm_N120.txt | RUNNING | - |
| rtp2_dirichlet_D5_axisx_ccm_N60.txt | RUNNING | - |
| rtp2_dirichlet_D8_axisN_x13.txt | 1255 | 0 |
| rtp2_dirichlet_D8_axisN_x25.txt | RUNNING | - |
| rtp2_dirichlet_D8_axisx_ccm_N120.txt | RUNNING | - |
| rtp2_dirichlet_D8_axisx_ccm_N60.txt | RUNNING | - |

# D5. Saturation and final-N results

Eigenvalues are rounded certified-ball results. N_sat is over 1..Nmax, certified unique. Final N is a finite-resolution proxy; it is not an infinite-N certificate.

| D | x | N final | N_sat full/even/odd | epsE at N_sat | epsE final | epsO final | parity |
|---|---|---|---|---|---|---|---|
| -4 | 13 | 200 | 11/11/11 | 3.10228843498e-13 | 3.55108899176e-14 | 7.49736362617e-11 | 1 |
| -3 | 13 | 200 | 17/17/17 | 4.63730601677e-19 | 1.25308864637e-19 | 2.88150878846e-16 | 1 |
| 5 | 13 | 200 | 7/7/7 | 2.10911890230e-11 | 2.10790657667e-12 | 3.00014809680e-9 | 1 |
| 8 | 13 | 200 | 4/4/4 | 1.21057046016e-6 | 2.17699319902e-7 | 0.000143025517367 | 1 |
| -7 | 13 | 200 | 4/4/4 | 2.31119975654e-6 | 2.03745394328e-7 | 0.000177050652770 | 1 |
| 12 | 13 | 200 | 2/2/2 | 0.00173236382165 | 0.000115817314349 | 0.0379151462554 | 1 |
| -20 | 13 | 200 | 1/1/1 | 0.158693673555 | 0.0987740569268 | 1.80464336194 | 1 |
| 21 | 13 | 200 | 2/2/1 | 0.0514183313883 | 0.0232509738349 | 0.809121815454 | 1 |
| 13 | 13 | 200 | 2/2/2 | 0.00122321454012 | 0.000402786486930 | 0.0548613049682 | 1 |
| -8 | 13 | 200 | 2/4/2 | 0.000111143598106 | 4.53702800257e-6 | 0.00271051444180 | 1 |

# COMPARISON: first root, final N

| D | x | N | error (ball) | error/eps (ball) | gamma1 |
|---|---|---|---|---|---|
| -4 | 13 | 200 | 1.36924359116e-12 | 38.5584138931 | 6.02094890469759665490251152161 |
| -3 | 13 | 200 | 4.86212210036e-17 | 388.011024953 | 8.03973715568146668171362321417 |
| 5 | 13 | 200 | 3.32035533794e-10 | 157.519093811 | 6.64845334472771471612327845998 |
| 8 | 13 | 200 | 5.37737315942e-6 | 24.7009185047 | 4.89997399700703650103830489920 |
| -7 | 13 | 200 | 2.91870117758e-6 | 14.3252375702 | 4.47573828372868313197462848719 |
| 12 | 13 | 200 | 0.000723657015974 | 6.24826279249 | 3.80462763305086509714431754004 |
| -20 | 13 | 200 | 0.0907225887304 | 0.918486002833 | 2.35893499408665604861501236977 |
| 21 | 13 | 200 | 0.0138214097826 | 0.594444339439 | 2.31518706430314115204629295971 |
| 13 | 13 | 200 | 0.000743221932889 | 1.84520076270 | 3.11934147900860341390159975672 |
| -8 | 13 | 200 | 1.42968317872e-5 | 3.15114470952 | 3.57615483678758907557757872996 |

# FLOATING slopes (positive digits per x)

| D | E 13–25 | O 13–25 | error 13–25 | E 25–50 | O 25–50 | error 25–50 | E 13–50 | O 13–50 | error 13–50 |
|---|---|---|---|---|---|---|---|---|---|
| -4 | NA | NA | NA | NA | NA | NA | NA | NA | NA |
| -3 | NA | NA | NA | NA | NA | NA | NA | NA | NA |
| 5 | NA | NA | NA | NA | NA | NA | NA | NA | NA |
| 8 | NA | NA | NA | NA | NA | NA | NA | NA | NA |
| -7 | NA | NA | NA | NA | NA | NA | NA | NA | NA |
| 12 | NA | NA | NA | NA | NA | NA | NA | NA | NA |
| -20 | NA | NA | NA | NA | NA | NA | NA | NA | NA |
| 21 | NA | NA | NA | NA | NA | NA | NA | NA | NA |
| 13 | NA | NA | NA | NA | NA | NA | NA | NA | NA |
| -8 | NA | NA | NA | NA | NA | NA | NA | NA | NA |

# FLOATING conductor scaling and polynomial fit

Fit log(eps)=a+b log(x/q)-c x/q at the three final-N samples. This is a three-point interpolation, not a validated asymptotic expansion. b_fixed fixes c=4pi and uses endpoints; A_fixed uses x=50.

| D | q × slope 13–50 | b fitted | c/(4pi) fitted | b_fixed | A_fixed |
|---|---|---|---|---|---|

# Controls, Schur envelopes and Rayleigh totals

| D | x | N | joint half-width | negative E/O | control min E | control min O | Rayleigh arch | Rayleigh primes |
|---|---|---|---|---|---|---|---|---|
| -4 | 13 | 200 | 4.709660901 | 1/0 | -0.450623277091 | 0.199181115282 | -0.161507309151 | 0.161507309151 |
| -3 | 13 | 200 | 4.362475483 | 1/1 | -0.738305349543 | -0.0885009571702 | -0.328682220866 | 0.328682220866 |
| 5 | 13 | 200 | 4.844692855 | 1/0 | -1.34577327083 | 0.310347442721 | -0.588566768749 | 0.588566768751 |
| 8 | 13 | 200 | 5.362163595 | 1/0 | -0.875769641583 | 0.780351071967 | -0.397790546911 | 0.397790764610 |
| -7 | 13 | 200 | 4.950286148 | 0/0 | 0.108992510844 | 0.758796903217 | 0.241374854281 | -0.241374650536 |
| 12 | 13 | 200 | 5.178332194 | 1/0 | -0.470304533475 | 1.18581618008 | -0.223714359618 | 0.223830176933 |
| -20 | 13 | 200 | 5.602314131 | 0/0 | 1.15881463534 | 1.80861902772 | 1.25644196864 | -1.15766791171 |
| 21 | 13 | 200 | 5.831991998 | 0/0 | 0.0893112544608 | 1.74543196801 | 0.347211604198 | -0.323960630363 |
| 13 | 13 | 200 | 5.332518718 | 1/0 | -0.390261825801 | 1.26585888775 | -0.201224841042 | 0.201627627529 |
| -8 | 13 | 200 | 4.672063784 | 0/0 | 0.242523903469 | 0.892328295841 | 0.328008645739 | -0.328004108711 |

# FLOATING finite-N tail check

| D | x | previous N | final N | eps(previous)/eps(final) | eps(N_sat)/eps(final) |
|---|---|---|---|---|---|
| -4 | 13 | 120 | 200 | 1.03515 | 8.73616 |
| -3 | 13 | 120 | 200 | 1.07788 | 3.7007 |
| 5 | 13 | 120 | 200 | 1.01473 | 10.0058 |
| 8 | 13 | 120 | 200 | 1.00407 | 5.56075 |
| -7 | 13 | 120 | 200 | 1.00474 | 11.3436 |
| 12 | 13 | 120 | 200 | 1.00108 | 14.9577 |
| -20 | 13 | 120 | 200 | 1.00041 | 1.60663 |
| 21 | 13 | 120 | 200 | 1.00063 | 2.21145 |
| 13 | 13 | 120 | 200 | 1.00135 | 3.03688 |
| -8 | 13 | 120 | 200 | 1.00365 | 24.497 |

# Zeta round 1 (existing output only; no rerun)

| x | N | N_sat | epsE | error upper (COMPARISON) | joint half-width |
|---|---|---|---|---|---|
| 13 | 200 | 56 | 2.85407e-59 | 2.00e-55 | 2.836 |
| 25 | 260 | 134 | 2.42562e-123 | 2.25e-119 | 2.146 |
| 50 | 360 | 352 | 2.26934e-257 | 2.45e-253 | 1.442 |

Review supplement (not recomputed): zeta x=50,N=420 eps=2.80881e-258; error=3.0346e-254; 13–50 slopes 5.379 and 5.373, source notes/reviews/rtp-round-1-2026-09-24.md, lines 649–651. The existing x50 driver output stops eigenpair comparisons at N=360.

# Axis x and fixed-L outcomes

| D | protocol | N | knots | indefinite knots | odd-minimum cutoffs | final epsE | final epsO |
|---|---|---|---|---|---|---|---|
| -4 | ccm | 60 | 23 | 0 | none | 2.73558909982e-57 | 3.86976014688e-53 |
| -4 | ccm | 120 | 6 | 0 | none | 9.92055466960e-8 | 6.51755246951e-5 |
| -3 | ccm | 60 | 24 | 0 | none | 1.96419958945e-70 | 1.87624023106e-66 |
| -3 | ccm | 120 | 6 | 0 | none | 5.53923289164e-11 | 5.03960377996e-8 |
| 5 | ccm | 60 | 23 | 0 | none | 1.08443227021e-49 | 1.39109884928e-45 |
| 5 | ccm | 120 | 6 | 0 | none | 6.10073301756e-7 | 0.000176165261473 |
| 8 | ccm | 60 | 23 | 0 | none | 2.56730841266e-31 | 2.88484929920e-27 |
| 8 | ccm | 120 | 6 | 0 | none | 0.000376344486114 | 0.0618844212385 |
| -7 | ccm | 60 | 23 | 0 | none | 3.87625353437e-34 | 6.11305043902e-30 |
| -7 | ccm | 120 | 6 | 0 | none | 0.000678374414719 | 0.110491862791 |
| 12 | ccm | 60 | 23 | 0 | none | 1.68739588796e-20 | 1.19254706017e-16 |
| 12 | ccm | 120 | 6 | 0 | none | 0.0137360330746 | 0.743156189506 |

