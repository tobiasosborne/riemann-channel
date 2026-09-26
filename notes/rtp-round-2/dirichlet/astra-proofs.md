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
