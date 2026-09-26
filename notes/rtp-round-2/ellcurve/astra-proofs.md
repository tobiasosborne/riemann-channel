# RTP-2 lane E: weight-two dilation windows

Author: `codex:gpt-6-astra`. Unreviewed research record. No RH assumption. Reference zeros are used only in labelled COMPARISON steps. All claims below carry their status; no claim is registered by this lane.

## Correction ledger (incremental)

1. **SHARPENED, before runs.** E2's `2 x log x` does not follow from the supplied Weyl law. The same mode-surplus calculation used in lanes A1/D gives `sqrt(x/C) log x`; see E2. Twice the leading zero density reduces the surplus and changes its turning point exponentially in the window length.
2. **SHARPENED, before runs.** In F4/F5, if alpha,beta are the arithmetic roots with alpha beta=p, the atom weight is `-(alpha^m+beta^m) log(p)/p^m`, not `/p^(m/2)`. The latter denominator requires normalized Satake roots alpha/sqrt(p), beta/sqrt(p). The driver uses the existing library normalization exactly.
3. **SHARPENED, before runs.** The decaying inverse-Mellin gamma kernel and the log-derivative kernel rho in the Weil form are different kernels. Reading off the exponential of the former alone does not prove an eigenvalue decay constant for the latter. H-RATE specifies a scale; a numerical leading constant needs an additional concentration hypothesis.
4. **SHARPENED, before runs.** For any single conductor, sqrt(x) and sqrt(x/C) are constant multiples, so intercept-plus-slope fits have identical residuals. Conductor scaling can only be tested by comparing slopes across curves, or by a constrained joint fit.
5. **NUMERICAL provenance.** Lane D is unfinished on entry (D4/D5 PARTIAL, D6 PENDING). Reuse its independent block-minimum certification, Rump/deflation refinement, Schur bordering, controls, output conventions, and completed outputs. Do not inherit its pending high-window verdict or its Hardy-Z reference evaluator, which applies to Dirichlet characters only. A separate `zst/tools/rtp2_ellcurve.c` avoids modifying a running lane's driver.

## E1. Predictions recorded before new runs

**PREDICTION E1a — OPEN (H-WINDOW-ONLY).** If the very same CCM Fourier-prolate parameter controls the new Weil minimizer, then

`eps_E(x) ~ A_E x^b exp(-4 pi x)`.

The asymptotic rate is `4 pi/log(10)=5.4575054` decimal digits per unit x. Importing also zeta's pole-constrained sector `b=9/2` gives 5.38674 digits/x over 13–50 (the actual arithmetic is regenerated below); that power is not justified for a pole-free weight-two form. The unchanged log window `[0,log x]` and Fourier basis do not establish H-WINDOW-ONLY. The archimedean data change from `rho_(2,1/2)(y)` to `rho_(1,1)(y)=exp(-y)/(1-exp(-y))`, and the atoms and pole constraints also change.

**PROVED (kernel identities; no minimizer conclusion).** Write lambda=sqrt(x), and u for the positive multiplicative variable before taking logs. The elementary Mellin identity is

`int_0^infinity exp(-2 pi u/sqrt(C)) u^s du/u = (sqrt(C)/(2 pi))^s Gamma(s)` for Re(s)>0.

Thus the weight-two completed L-function is obtained, up to a constant and the centred shift, from the Mellin transform of the modular Fourier sum `sum_(n>=1) a_n exp(-2 pi n u/sqrt(C))`. Its first exponential decays on the scale lambda/sqrt(C) at u=lambda. Zeta instead uses `sum exp(-pi n^2 u^2)` and has scale lambda^2=x. This makes sqrt(x/C), not sqrt(log x) or x/C, the candidate weight-two window scale. It does not specify whether amplitude, squared mass, or optimized concentration controls eps.

The centred gamma-ratio kernel supplies a sharper conditional prediction. For

`K_C(v)=(2 pi/sqrt(C)) sqrt(v) J_1(4 pi sqrt(v/C))`,

the Bessel Mellin integral gives `int K_C(v) v^s dv/v = (C/(4 pi^2))^s Gamma(1+s)/Gamma(1-s)` in its convergence strip (then meromorphically). This is the weight-two gamma/conductor scattering ratio. Its product argument at the two support boundaries is v=lambda^2=x; after square-root coordinates the finite Hankel parameter is `c_E=4 pi sqrt(x/C)`. The corresponding zeta Fourier parameter is `c_zeta=2 pi x`. The standard finite Hankel kernel is `sqrt(c r t) J_alpha(c r t)`; see the primary paper [Boulsane–Karoui, arXiv:1701.04622](https://arxiv.org/abs/1701.04622). Identifying these transforms with the actual arithmetic Weil minimizer remains an additional hypothesis.

**PREDICTION E1b — OPEN (H-RATE plus H-HANKEL-TRANSFER).** If optimized low-sector concentration has leakage `exp(-2 c_E)` up to powers and transfers to eps, then

`eps_E(x) ~ A_E (sqrt(x/C))^b_E exp(-8 pi sqrt(x/C))`.

This predicts `8 pi/log(10)=10.9150108` digits per unit sqrt(x/C), or `10.9150108/sqrt(C)` digits per unit sqrt(x): 3.29096 for C=11 and 2.91720 for C=14. Its local rate per x is `5.4575054/sqrt(C x)`, before algebraic corrections. The error of a stably recovered simple first zero is predicted to share the leading exponential, with a separate prefactor. No exact power or amplitude is predicted. A bare squared Mellin tail instead suggests `exp(-4 pi sqrt(x/C))`, half this slope; record it as a weaker competing constant, not as a consequence of H-RATE. These predictions use only the already published MVP-3 observations, not a new elliptic run.

## E2. Resolution prediction

**PROVED algebra; OPEN as a saturation law.** In either reflection sector the Fourier-mode count up to T is approximately `T log(x)/(2 pi)`. Subtract the supplied positive-ordinate Weyl count:

`S_E(T)=T log(x)/(2 pi) - T/pi log(sqrt(C) T/(2 pi e))`.

Its derivative vanishes at `T*=2 pi sqrt(x/C)`, and S_E vanishes at `e T*`. Under `N=T log(x)/(2 pi)`, these become `N*=sqrt(x/C) log(x)` and `e N*`. I expect determinant minima on this scale, with order-one constants depending on parity, low zeros, and the omitted poles. The round-1 empirical constant 1.7 is a useful pilot guess, not a theorem: for 11a1 this suggests N near 5, 8, 14 at x=13,25,50, and near 24 at x=100. These N are determinant transitions, not quantitative certificates of convergence as N tends to infinity; eps must be checked at much larger N. The prescribed N=60,120,200 protocols should resolve the leading rate well, unlike zeta at those same windows.
