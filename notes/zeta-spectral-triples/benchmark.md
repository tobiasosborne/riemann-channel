# How far beyond the paper: an impromptu benchmark of `zst` (2026-09-17)

Question (TJO): now that the code exists, how many zeros can the Connes-Consani-Moscovici
construction reach, and how accurately? All numbers below are *certified upper bounds* on
`|z_k - gamma_k|` from `zst` (ball arithmetic, Krawczyk-verified eigenpair, verified positive
definiteness for the even-simple hypothesis, interval-Newton roots with completeness by count).
Raw outputs: `bench/x*_N*_p*.txt`; table by `zst/tools/bench_summary.py bench`. Single thread,
FLINT 3.0.1, this container (4 cores, 15 GB).

## The table

`x = lambda^2` (prime powers `<= x` enter), `N` = Fourier truncation, `prec` in bits. `err(z1)` is the
certified error of the first zero; `k < 1e-d` is the largest zero index whose certified error is
below `1e-d`; times in seconds (build, eigenpair, even-simple certificate, roots, wall).

    x     N  prec          eps_N    err(z1)  k<1e-50 k<1e-30 k<1e-20 k<1e-10 k<1e-3   ok  build   eig  cert  roots   wall
   13   120   700  3.48e-59       2.44e-55        2      14      23      34     47    Y    0.1   0.6   0.3    1.8     3
   20   100   900  3.55e-95       3.07e-91       25      44      56      71     84    Y    0.2   0.6   0.2    1.3     3
   20   150   900  1.76e-96       1.51e-92       26      46      60      76     95    Y    0.2   1.5   0.6    3.9     7
   20   200   900  1.43e-96       1.23e-92       26      46      60      76     95    Y    0.3   3.2   1.4    9.2    15
   30   300  1300  2.61e-150      2.55e-146      77     106     123     147    172    Y    1.0  13.0   7.2  212*    235*
   30   450  1300  2.13e-150      2.08e-146      78     106     124     148    172    Y    1.6  34.7  23.6  657*    719*
   40   400  1700  2.90e-204      3.01e-200     140     177     198     225    251    Y    2.2  33.7  23.5   58     119

(*) roots stage with the QR candidate generator; the sign-scan generator (later the same day) does
the x = 40 case in 58 s instead of 612 s with the identical table. Rows for x = 50, 60, 80, 100 are
appended below as they complete.

Selected certified errors at x = 40 (N = 400): zero 1: 3.0e-200, zero 50: 1.6e-118, zero 100:
3.5e-80, zero 150: 1.0e-45, zero 200: 8.5e-20, zero 250: 2.0e-4, zero 300: 4.2 (meaningless).

## What the table says

1. **Accuracy of the first zero is exponential in x and independent of N.** `log10 err(z1) ~ -5.4 x + 15`
   (x = 13: -54.6; 20: -91.9; 30: -145.6; 40: -199.5), i.e. 5.4 digits per unit of x, matching
   `e^{-4 pi x}` (4 pi / ln 10 = 5.46), the decay of the prolate eigenvalue defect `1 - chi_4(lambda)`
   the paper's Section 7 points to. With only the primes up to 40 the first zero is certified to 200
   digits. N does not enter: at x = 20, N = 100, 150, 200 give 3e-91, 1.5e-92, 1.2e-92.
2. **Accuracy degrades linearly in the height of the zero, at a slope independent of x.** At every x,
   `log10 err(z_k) ~ log10 err(z1) + 0.37 gamma_k` (x = 13: from -55 at gamma = 14 to -2.7 at
   gamma = 143; x = 40: from -200 at 14 to -3.7 at 555). So the number of usable zeros grows linearly
   in x: zeros with certified error below 1e-3 reach `gamma_max ~ 14.6 x - 40` (x = 13: 143; 20: 254;
   30: 402; 40: 555), and below 1e-50, `gamma_max ~ 14.6 x - 170`.
3. **N saturates at about 7.5 x.** x = 20: N = 100 gives 84 zeros below 1e-3, N = 150 and 200 give 95;
   x = 30: N = 300 and 450 both give 172. The bandwidth needed is `s_max = gamma_max L / 2 pi ~ 2.3 x`
   (x = 40: s_max = 326 for gamma = 555), and N ~ 1.5 s_max suffices; beyond that N only adds
   spurious roots (which the certificate still has to account for).
4. **eps_N tracks the same law**: `log10 eps_N ~ -5.1 x + 8` (x = 13: -58.5; 20: -95.8; 30: -149.6;
   40: -203.5); eps_N is also N-independent to a factor 2 once N is saturated. This is the paper's
   Figure `fpro1` in numbers, and a certified instance of Weil positivity on each window.
5. **Cost.** Precision must exceed about `2 log2(1/eps_N) + 200 ~ 36 x + 200` bits for the Krawczyk
   eigenpair certificate; the runs use `prec ~ 40 x + 200`. With the sign-scan candidate generator
   the roots stage is `O(N^2)` at working precision and the eigenpair plus certificate are `O(N^3)`:
   x = 40 (N = 400, 1700 bits) takes 2 minutes single-threaded. Extrapolation (`N^3 prec^1.6`):
   x = 60 about 10 min, x = 80 about 30 min, x = 100 (N = 1000, 4000 bits) about 80 min, which would
   certify the first zero to about 500 digits and about 700 zeros below 1e-3.

## What was fixed to get here (all recorded in the worklog)

- The interval-`LDL^T` inertia certificate failed from x = 20 on (input radii amplified by the squared
  condition number, 1e192). Replaced by verified positive definiteness of the deflated matrix
  `E - 2 eps + c v v^T` and of `O - 2 eps` by approximate Cholesky plus a ball residual (Rump's isspd),
  whose amplification is linear; a 2x2 test exposed that the deflation constant must exceed
  `s - eps`.
- The QR candidate generator dominated the runtime (612 of 673 s at x = 40) and its precision cannot
  be reduced below the dynamic range of the rank-one term (about 5.5 x digits: the normalisation
  `sum xi_j = 1` divides by the eigenfunction's value at the window edge, which is `e^{-pi lambda^2}`
  small). Replaced by a sign scan with bisection on each pole interval plus a geometric grid beyond
  the last pole (the tail roots cluster just past N: 400.34, 406.74, 427.4, ... at N = 400, and
  reach 31 N), refined once, with the QR kept as a fallback at prec/2 then prec.
- Overlapping certified balls (duplicate candidates) used to discard the whole list; now a Newton
  step on the hull of the pair decides rigorously whether it is one root or two.

## Caveats

- Every error is an upper bound from ball arithmetic; the reference zeros are arb's certified
  `acb_dirichlet_zeta_zeros` (full precision for the first 20, 400 bits beyond, so bounds below
  1e-100 are only reported for k <= 20).
- "Reach" here means the construction's spectrum agrees with the zeros; it says nothing about
  convergence proofs. The linear degradation in gamma (item 2) is the quantitative shape of what a
  proof would have to control.
