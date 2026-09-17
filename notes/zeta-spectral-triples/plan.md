# Zeta spectral triples (Connes, Consani, Moscovici, arXiv:2511.22755): reading notes and an implementation plan for a rigorous arb/FLINT C library

Status: reading notes plus a validated reference prototype (`ccm_proto.py`, mpmath) and an
implementation plan. Nothing here is a registered lab-book claim. Sidequest of 2026-09-17; intended
to become its own repository.

Source: `refs/src/2511.22755/mc2arXiv.tex` (fetched 2026-09-17, sha256 in `refs/manifest.sha256`;
arXiv id added to `refs/fetch_sources.sh`). Line numbers below refer to that file.

## 0. Summary

The paper constructs, for each window `[lambda^-1, lambda]` and Fourier truncation `N`, a finite
real symmetric matrix `tau` (the Weil quadratic form restricted to `2N+1` Fourier modes of the
window), takes its minimal eigenvector `xi`, and forms a rank-one perturbation `D'` of the scaling
operator `D = -i d/dlog u`. The Connes-van Suijlekom extension of Caratheodory-Fejer makes `D'`
self-adjoint for the inner product `tau - eps_N`, so its spectrum is real; that spectrum is the zero
set of the entire function `xi_hat(z)`, the Fourier transform of `xi`. With only the primes
`p <= lambda^2` the low spectrum agrees with the zeros of `zeta(1/2 + i s)` to dozens of digits. The
proof that the spectrum converges to the zeros as `N, lambda -> infinity` is missing; it would prove RH.

What was done today:

- the full pipeline was re-derived and implemented independently in mpmath (`ccm_proto.py`);
- every closed form was checked against direct quadrature; the paper's column `lambda = sqrt 13,
  N = 120` is reproduced for all 50 listed zeros to every printed digit
  (`run_lambda_sqrt13_N120.txt`), and `lambda = 3, N = 120` matches the paper's Figure 1 regime;
- one typo in the paper was found (the displayed constant `c(L)`, Section 1.6 below); it is a
  multiple of the identity on the diagonal, so it moves `eps_N` but not `xi` or the spectrum;
- FLINT 3.0.1 was installed here and every library call the plan relies on was verified to exist,
  compile and run (`flint_smoke.c`).

The implementation target is a C library (`libzst`, "zeta spectral triples") on FLINT 3 (arb ball
arithmetic) that (a) reproduces the paper with certified enclosures rather than floating point,
(b) runs at parameters far beyond the paper's (`lambda^2 ~ 100`, `N ~ 10^3`, thousands of digits),
and (c) takes the "explicit-formula distribution" as abstract input, so that Dirichlet and Hecke
L-functions, curve and graph zetas, and the Selberg zeta of the modular surface run through the same
code. Section 6 maps those extensions to the cases of this notebook.

## 1. The algorithm, as verified

### 1.1 Window, basis, and the structure theorem

`lambda > 1`, `L = 2 log lambda`. Hilbert space `L^2([lambda^-1, lambda], du/u) ~ L^2([0, L], dx)`
via `x = log(lambda u)`. Basis `U_n(x) = L^{-1/2} exp(2 pi i n x / L)`, `V_n = U_n(log(lambda u))`,
`|n| <= N`. `E_N = span{V_n}` has dimension `2N+1`.

The Weil form is `QW(f, g) = Psi(f^* * g)` with `Psi = W_{0,2} - W_R - sum_p W_p` (eq. `bombtest`,
lines 385-388). By inversion symmetry (Lemma `wsharp`) and translation invariance (Lemma `qtrans`),
`QW(V_n, V_m) = int_0^L q(U_n, U_m)(y) D(y) dy` where `D` is a real distribution on `[0, L]` and

    q(U_n, U_m)(y) = [sin(2 pi m y/L) - sin(2 pi n y/L)] / (pi (n - m))   (n != m),
    q(U_n, U_n)(y) = 2 (1 - y/L) cos(2 pi n y/L).

Hence (Lemma `basicexpli`) the matrix has the Loewner form

    tau_{nm} = (b_n - b_m)/(n - m)  (n != m),   tau_{nn} = a_n,
    b_n = -(1/pi) int_0^L sin(2 pi n y/L) D(y) dy,   a_n = 2 int_0^L (1 - y/L) cos(2 pi n y/L) D(y) dy,

with `b_{-n} = -b_n`, `a_{-n} = a_n`. Equivalently `[D, tau] = |beta><eta| - |eta><beta|`, `beta =
sum b_j V_j`, `eta = sum V_j` (rank-two commutator; Lemma `basics`). Everything downstream uses only
this structure. This is the point of generality: any real distribution `D` on `[0, L]` gives such a
matrix, and the paper's theorems (real spectrum, determinant formula) hold for it verbatim.

### 1.2 The three parts of `D`, in closed form

Write `omega_n = 2 pi n / L`, `z = e^{-2L}`, `rho(x) = e^{x/2}/(e^x - e^{-x}) = sum_{k>=0}
e^{-(2k+1/2) x}`, `A_n = 1/4 - i pi n / L` (so `2k + 1/2 - i omega_n = 2 (k + A_n)`).

Pole term (`W_{0,2}`, rank two; Lemma `w02`). With `K = 32 L sinh^2(L/4)`:

    b_n^{(02)} = K n / (L^2 + 16 pi^2 n^2),
    a_n^{(02)} = K (L^2 - 16 pi^2 n^2) / (L^2 + 16 pi^2 n^2)^2.

(Derivation: `W_{0,2}(V_n, V_m) = conj(c_+(n)) c_-(m) + conj(c_-(n)) c_+(m)` with
`c_+-(n) = int V_n u^{+-1/2} d*u = L^{-1/2} 4 L sinh(L/4)/(L +- 4 pi i n)`; the general pole at
`sigma` gives `c_sigma(n) = L^{-1/2} 2 sinh(sigma L/2)/(sigma + 2 pi i n/L)`.)

Prime term (`W_p`; eq. `bomp`). Over prime powers `1 < k <= lambda^2`, `Lambda` von Mangoldt:

    b_n^{(p)} = (1/pi) sum_k Lambda(k) k^{-1/2} sin(omega_n log k),
    a_n^{(p)} = -2 sum_k Lambda(k) k^{-1/2} (1 - log k / L) cos(omega_n log k).

Archimedean term (`W_R`; Prop. `bigmatrix`, Prop. `computearch`). Three integrals per `n`,

    I_1(n) = int_0^L sin(omega_n x) rho(x) dx,
    I_2(n) = int_0^L x cos(omega_n x) rho(x) dx,
    I_3(n) = int_0^L (cos(omega_n x) - 1) rho(x) dx,

evaluated by expanding `rho` and regularising the divergent `k`-sums with digamma/trigamma. With
`S_1(n) = sum_k z^k/(k + A_n)`, `S_2(n) = sum_k z^k/(k + A_n)^2`, `S_1(0) = sum_k z^k/(k + 1/4)`,
`e = e^{-L/2}`:

    I_1 = -(1/2) Im psi(A_n) - (e/2) Im S_1(n),
    I_2 = -(L e/2) Re S_1(n) + (1/4) Re psi'(A_n) - (e/4) Re S_2(n),
    I_3 = (1/2) [psi(1/4) - Re psi(A_n)] - (e/2) Re S_1(n) + (e/2) S_1(0).

(`S_1 = Phi(z, 1, A)`, `S_2 = Phi(z, 2, A)` Lerch; `S_1(n) = A_n^{-1} 2F1(1, A_n; A_n + 1; z)`;
these are the paper's hypergeometric and Hurwitz-Lerch expressions. Since `z = e^{-2L} < 0.02`
for `lambda >= 3`, direct summation with a geometric tail bound is the right implementation.)
Then

    b_n^{(R)} = I_1(n)/pi,
    a_n^{(R)} = -2 [ w(L) + I_3(n) + C(L) - I_2(n)/L ],
    w(L) = (gamma + log 4 pi)/2 - (1/2) log((e^L + 1)/(e^L - 1)),
    C(L) = int_0^L (1 - e^{-x/2}) rho(x) dx
         = -log(t + 1) + (1/2) log(t^2 + 1) + arctan t + (1/2) log 2 - pi/4,   t = e^{L/2}.

Totals: `b_n = b^{(02)} + b^{(R)} + b^{(p)}`, `a_n = a^{(02)} + a^{(R)} + a^{(p)}`.

### 1.3 Even and odd blocks

`tau` commutes with `gamma: V_j -> V_{-j}`. In the basis `c_0 = V_0`, `c_j = (V_j + V_{-j})/sqrt 2`
(`j >= 1`) the even block `E` (size `N+1`) is

    E_00 = a_0,  E_0j = sqrt2 b_j / j,  E_jj = a_j + b_j/j,
    E_ij = (b_i - b_j)/(i - j) + (b_i + b_j)/(i + j)  (i != j),

and the odd block `O` (size `N`, basis `(V_j - V_{-j})/sqrt 2`) has `O_jj = a_j - b_j/j`,
`O_ij = (b_i - b_j)/(i - j) - (b_i + b_j)/(i + j)`. The paper's hypothesis "even-simple" is:
`eps_N = min spec E` is simple and `eps_N < min spec O`. Working blockwise is four times cheaper
and turns the hypothesis into a certifiable inequality.

### 1.4 Minimal eigenpair and normalisation

`xi` = eigenvector of `E` for `eps_N`, mapped back to `xi_j` (`xi_{-j} = xi_j`, `xi_j = c_j/sqrt 2`
for `j >= 1`), normalised by `<eta | xi> = sum_{j=-N}^{N} xi_j = xi_0 + 2 sum_{j>=1} xi_j = 1`
(equivalently `delta_N(xi) = L^{-1/2}`; the paper's `delta_N(xi) = 1` differs by the factor
`L^{1/2}`, which only rescales `xi_hat`). Nonvanishing of `<eta|xi>` is proved in the paper (after
Def. `even-simple`).

### 1.5 Spectrum, Fourier transform, regularised determinant

The perturbed operator on `E_N` is `D' = D - |D xi><eta|` with `D V_n = n V_n`; its restriction to
`E_N / C xi` is `D''`, self-adjoint for `<f|g>_T = <(tau - eps_N) f | g>` (Lemma `key`), and
(eq. `eq:detDp`)

    Det(D'' - s) = Det(D - s) sum_{j=-N}^{N} xi_j /(j - s).

So the `2N` eigenvalues of `D''` are the real zeros of the secular function

    g(s) = sum_j xi_j/(j - s) = -xi_0/s + 2 s sum_{j>=1} xi_j/(j^2 - s^2)

(odd in `s`; `N` positive roots), and the eigenvalues of `D_log^{(lambda,N)}` are `z = 2 pi s/L`.
The Fourier transform of `xi` (extended by zero) is `xi_hat(z) = 2 L^{-1/2} sin(zL/2) sum_j
xi_j/(z - 2 pi j/L)` and `det_reg(D_log^{(lambda,N)} - z) = -i lambda^{-iz} xi_hat(z)`
(Theorem `finmain`). Important for the implementation: `g` is not monotone between consecutive
poles because the `xi_j` change sign, so several roots can share a pole interval (at `lambda =
sqrt 13`, zeros 13 and 14 both lie in `(24, 25)`); root isolation must not assume one root per
interval, and the count `2N` is the completeness check.

### 1.6 Verification record (this session)

- `I_1, I_2, I_3` closed forms vs `mpmath.quad`: agreement to working precision (60 and 130 digits).
- `tau_{nm}` closed vs the defining principal-value integrals for six `(n, m)`: agreement to
  working precision, including the sign conventions of all three parts.
- `lambda = sqrt 13, N = 120, 130 digits`: `eps_N = 3.48e-59`, next even `1.31e-51`, smallest odd
  `3.06e-55`; the 50 differences `|z_k - gamma_k|` equal the paper's table column
  (`2.44e-55, 4.5e-52, 4.16e-50, ..., 2.0e-3, 3.01e-3, 2.04e-3`). mpmath time 108 s.
- `lambda = 3, N = 120`: `eps_N = 2.95e-38`, first zero to `1.6e-34`, twentieth to `2.4e-7`;
  `lambda = 3, N = 40` gives the same `1e-34` on the first zero, so at `lambda = 3` the accuracy is
  set by `lambda`, not by `N`.
- Typo: the paper defines `gamma_L(n)` (eq. after `"funct`) as the integral of
  `(cos - e^{-x/2}) rho` plus `c(L) + w(L)`, with `c(L) = int_0^L (1 - e^{-x/2})/(e^x - e^{-x}) dx`
  (closed form as displayed, `0.352` at `lambda = 3`). The identity `corectc` requires instead the
  correction `C(L) = int_0^L (1 - e^{-x/2}) rho(x) dx = 0.575` (quadrature agrees with the closed
  form in 1.2), added to the `(cos - 1)` integral, not to the `(cos - e^{-x/2})` one. The
  difference is `n`-independent, hence a scalar multiple of the identity: `xi` and the spectrum are
  unchanged, `eps_N` is shifted by `2 (C - c) ~ 0.45`, which would make it negative. Since the
  paper's `eps` values are tiny and their zero table is reproduced exactly by the `C(L)` version,
  their code used the correct constant and only the display is wrong.
- Empirical law (two data points, `lambda = 3` and `sqrt 13`): `|z_1 - gamma_1| ~ 5e4 (1 - chi_4(lambda))`
  and `eps_N ~ 10 (1 - chi_4(lambda))`, with `1 - chi_4 ~ (2^{14}/3) sqrt2 pi^5 lambda^9
  e^{-4 pi lambda^2}` the Fuchs asymptotic quoted by the paper (their Section 7, not independently
  checked). So the accuracy on the first zero is `~ 5.5` digits per unit of `x = lambda^2`, and
  `x = 100` would give of order 500 digits if `N` and the precision are large enough. This is the
  regime the C implementation is for.

## 2. What is proved and what is not

Proved in the paper (finite-dimensional linear algebra plus standard spectral theory):
`QW_lambda` is lower bounded, closed, with discrete spectrum (Theorem `thmsmallest`); for each
`(lambda, N)` with the even-simple hypothesis, `D_log^{(lambda,N)}` is self-adjoint on `E'_N + E_N^perp`,
its spectrum is real and equals the zero set of `xi_hat`, and `det_reg = -i lambda^{-iz} xi_hat(z)`.
Also `mu_lambda` (the infimum of `QW_lambda`) is decreasing in `lambda`, and `mu_lambda -> 0` would
imply RH (Cor. `strange`; this is Weil's criterion restricted to windows).

Not proved: (i) even-simplicity for `QW_lambda` and its truncations (assumed; certifiable per
`(lambda, N)` by the tool); (ii) that `xi_lambda` is close to the prolate guess `k_lambda =
E(h_lambda)`; (iii) convergence of the spectrum to the zeros. The paper's strategy: `Xi` is the
Fourier transform of `E(h)`, `h` the unique combination of Hermite functions `h_0, h_4` with zero
integral (Lemma `hermfact`); `k_lambda` is the same with prolate functions `h_{0,lambda}, h_{4,lambda}`;
`k_lambda`'s Fourier transform converges to `Xi` on substrips of `|Im z| < 1/2` (Lemma `hermfact1`,
proved from a Meixner-Schafke estimate); so if `xi_lambda ~ k_lambda` then `det_reg -> Xi` and
Hurwitz gives RH. Step (ii) is the whole difficulty; the numbers above show the accuracy is governed
by `1 - chi_4(lambda)`, which is the paper's Figure `fpro1` in a quantitative form.

## 3. Library design (`libzst`)

### 3.1 Principles

- Rigor: every quantity is an arb ball; the outputs are certified enclosures of `eps_N`, of the
  even-simple gap, of `xi`, of each spectral value `z_k`, and of `|z_k - gamma_k|` against
  `acb_dirichlet_zeta_zero`. A run is a computer-verified statement.
- Generality: the pipeline after `(a_n, b_n)` is independent of `zeta`. The input is an abstract
  explicit-formula distribution (3.2). New L-functions and zetas are new distribution builders,
  not new pipelines.
- Speed: `O(N)` special-function evaluations, `O(N^2)` for the secular roots, one `O(N^3)` dense
  factorisation at working precision for the eigenpair; structured `O(N^2)` solvers later.
- Plain C11, FLINT >= 3.0 (`-lflint -lmpfr -lgmp`), Makefile, no other dependencies. Optional
  thin Julia `ccall` wrapper later.

### 3.2 Data model: the explicit-formula distribution

    typedef struct {
        arb_t  L;                 /* window length in the log variable (2 log lambda for zeta) */
        /* atoms:   D_atoms = sum_k w_k delta(y - y_k),  0 < y_k <= L, real w_k          */
        slong  natoms; arb_ptr y; arb_ptr w;            /* zeta: y = log p^m, w = -Lambda p^{-m/2} */
        /* kernels: D_kern  = sum_j c_j rho_j(x),  rho_j(x) = sum_{k>=0} P_j(k) e^{-(d_j k + mu_j) x} */
        slong  nkern; arb_ptr kc; arb_ptr d; acb_ptr mu; slong *pdeg; arb_ptr pcoef;
        /* poles:   sum_s m_s Fhat(-i sigma_s), rank-one each (zeta: sigma = +-1/2, m = 1)     */
        slong  npoles; acb_ptr sigma; slong *pmult;
        /* identity shift: c * F(1) terms (conductor, Euler-constant, window-edge constants)   */
        arb_t  shift;
    } zst_weil_t;

Rationale. Every explicit formula in sight (Riemann, Dirichlet, Dedekind, Hecke, GL(2), Ihara,
Artin-Schreier/Weil, Selberg compact and modular) is: a finite set of atoms inside the window
(primes, prime geodesics, ring norms), a finite set of archimedean/identity kernels that are
exponential series in `x` (each gamma factor `Gamma(s/2 + a)` on the critical line contributes
`sum_k e^{-(2k + 2a) x}`-type kernels by Gauss's integral for `psi`; `Gamma_C` has step 1; the
Selberg identity term `1/(4 sinh^2(x/2)) = sum_k k e^{-kx}` has a polynomial prefactor), a finite
set of rank-one pole terms (the trivial divisor moved to the right-hand side), and constants
multiplying `F(1)` (which are multiples of the identity on the diagonal and affect only `eps`).
The kernel family `P(k) e^{-(dk + mu)x}` with `deg P <= 2` and complex `mu` covers all of these,
and its window integrals are polygamma of order `<= deg P + 1` plus `z`-series with `z = e^{-dL}`.

The `(a_n, b_n)` builder is then generic:

    void zst_weil_ab(arb_ptr a, arb_ptr b, slong N, const zst_weil_t *W, slong prec);

For zeta a convenience constructor `zst_weil_riemann(W, lambda, prec)` fills atoms (prime powers
up to `lambda^2` via `n_primes` / `n_factor`), one kernel `(d, mu, P) = (2, 1/2, 1)` with
coefficient `-1`, two poles `sigma = +-1/2`, and the shift `-2 w(L) - 2 C(L)` folded in as in 1.2.
The archimedean constants for a general kernel are derived once from the regularisation, never
typed in per case (Milestone M3 does this derivation and validates it on zeta and on a real
Dirichlet character).

### 3.3 Modules

    src/weil_data.c     constructors for zeta (M1), Dirichlet (M3), user-supplied distributions
    src/kernel.c        window integrals of P(k) e^{-(dk+mu)x} against sin, cos, x cos:
                        polygamma regularisation + z-series with rigorous geometric tail (mag_geom_series)
    src/loewner.c       (a,b) -> even/odd blocks; matrix-vector products in O(N) special structure
    src/eigmin.c        minimal eigenpair of the even block; certification; even-simple check
    src/secular.c       real roots of g(s); Fourier transform xi_hat; det_reg on a grid
    src/compare.c       certified comparison with acb_dirichlet_zeta_zero(s) / hardy_z zeros
    src/zst.h           public API; tools/zst.c CLI; tests/

### 3.4 Numerical core

Special functions (`kernel.c`). Per `n`: `acb_digamma(A_n)`, `acb_polygamma(1, A_n)` (verified
present), and the sums `S_1, S_2` by direct summation of `z^k/(k + A)^r` with the tail bounded by
`|z|^K/(1 - |z|) / |Re A|^r` via `mag_geom_series` and `arb_add_error`. Terms needed:
`prec * log 2 / (d L)`; at 700 bits and `L = 2.5` about 100 terms. Cost per `n` is microseconds
to milliseconds; the whole `(a, b)` build is negligible at `N = 10^3`. Parallel over `n` with
OpenMP (each thread owns its arb variables; FLINT is thread-safe for independent objects).

Minimal eigenpair (`eigmin.c`). arb has no symmetric eigensolver; `acb_mat_approx_eig_qr` is
general complex `O(N^3)` and would work but wastes the symmetry. Plan:
1. Approximate: inverse iteration on the even block with shift 0 using `arb_mat_approx_solve`
   (Cholesky or LU on midpoints), two or three iterations from a vector even in `j` and
   positive; the convergence factor is `eps_1/eps_2` (`1e-8` at `lambda = sqrt 13`). Rayleigh
   quotient gives `eps_N`.
2. Certify the pair with `acb_mat_eig_enclosure_rump` (verified present; Rump's verification for a
   simple eigenpair), which returns balls for `eps_N` and `xi` given the approximation.
3. Certify minimality and simplicity by inertia: compute a certified `arb_mat_ldl` of `E - s` for
   `s` slightly above the certified `eps_N` and check exactly one negative pivot (all pivot balls
   must exclude zero); do the same on the odd block `O - s` and require zero negative pivots. This
   is the even-simple hypothesis of Theorem `finmain`, certified.
   Precision: the condition number of `E` is `||E||/eps_N ~ 1e60`; ball radii grow by that factor,
   so the working precision must exceed `log2(||E||/eps_N) + target bits` (`~ 200 + 3.32 d` bits for
   `d` digits); the driver doubles `prec` until the certified radii meet the tolerance.

Secular roots (`secular.c`). `g(s)` and `g'(s) = sum xi_j/(j - s)^2` are `O(N)` per evaluation
with ball coefficients. Isolate the `N` positive roots by adaptive bisection on each pole
interval `(j, j+1)`: subdivide until each piece either has a certified sign change with `g'` of
one sign (unique root) or is certified root-free; then interval Newton (`arb_calc_refine_root_newton`
or hand-rolled with the explicit derivative) to full precision. Completeness check: exactly `N`
positive roots (the theorem guarantees `2N` real roots in total); failure means a near-double root
or `xi_j` balls containing zero, which the driver reports (and can resolve by raising `prec`).
Fallback for close pairs: the symmetric form of `D''`, `M = R^{-T} W^T (tau - eps) D' W R^{-1}`
with `W` an orthonormal basis of `xi^perp` and `G = W^T (tau - eps) W = R^T R`, whose eigenvalues
are the roots; certified by approximate diagonalisation plus Gershgorin (`acb_mat_eig_simple_rump`).
The prototype missed 2 to 4 of the 120 roots with a naive grid; the C code must not.

Comparison (`compare.c`). `acb_dirichlet_zeta_zero(s)` gives certified `gamma_k` (verified: 40
digits at 400 bits in the smoke test); output `z_k`, `gamma_k`, and a certified bound on
`|z_k - gamma_k|`. For other L-functions, real zeros of `acb_dirichlet_hardy_z` with a character
via `arb_calc_isolate_roots`.

Determinant (`secular.c`). `xi_hat(z)` on a grid of the strip, `det_reg`, and the normalised
comparison with `acb_dirichlet_xi` (verified present): fit `e^{a + ibz}` on two points and report
the sup-norm deviation on compact sets, the paper's Section 7 experiment.

### 3.5 Precision and parameter management

- Inputs: `lambda` (or `x = lambda^2`), `N`, target digits `d`, max precision.
- Working precision `p`: start at `max(256, 3.32 d + 200)`; after the eigenpair certification,
  if the relative radius of `xi` exceeds `10^{-d}`, double `p` and repeat (the `(a,b)` build is
  cheap, the factorisation is the cost).
- Outputs carry their radii; the CLI prints `z_k` with the number of certified digits and
  `|z_k - gamma_k|` as an upper bound.
- Rule of thumb from the runs: meaningful roots are those with `s < N/2`; the paper's `N = 120`
  tables stop at zero 50 (`s ~ 58`). A starting rule `N ~ 10 lambda^2` and `d ~ 6 lambda^2` reproduces
  the paper's regime; the tool's first job is to map `(lambda, N, p) -> accuracy` properly.

### 3.6 Performance

| step | cost | `N = 120, 700 bits` | `N = 1000, 3500 bits` |
|---|---|---|---|
| `(a, b)` build | `O(N)` polygamma + `O(N * prec/L)` series | milliseconds | seconds |
| even-block factorisation | `O(N^3)` at `prec` | well under a second | minutes (single thread) |
| Rump certification | one solve + a few matvecs | seconds | minutes |
| inertia checks (two LDL) | `2 O(N^3)` | seconds | minutes |
| secular roots | `O(N^2)` per Newton sweep | negligible | seconds |

Later structured speedups: `tau` is a Loewner matrix (`[D, tau]` of rank two), so GKO-type
`O(N^2)` displacement-structured LU exists; at high precision this is a real win for `N >= 10^3`.
Threading: OpenMP over `n` in the build and over columns in the factorisation;
`flint_set_num_threads` for `arb_mat_mul_threaded`.

### 3.7 Tests and CI

- Unit: `I_1, I_2, I_3` against `arb_calc` quadrature at 3 values of `n`; `W_{0,2}` rank-two identity;
  `(a, b)` against hard-coded 40-digit values from `ccm_proto.py` (committed as `tests/reference/`).
- Integration: `lambda = 3, N = 40` must give `|z_1 - gamma_1| <= 3e-34` (the prototype value);
  `lambda = sqrt 13, N = 120` must reproduce the paper's 50-row column to the printed digits.
- Property: the count of real secular roots equals `2N`; `eps_N` decreases in `N` and in `lambda`
  (Prop. `Hilbert1`, eq. `monotone`); `eps_N > 0` certified (a windowed Weil-criterion instance).
- CI: GitHub Actions on Ubuntu 24.04 (`apt install libflint-dev`, FLINT 3.0.1, the version verified
  here) and a job building FLINT 3.2 from source.

### 3.8 Repository layout

    zst/                     standalone repo (proposed name; AGPL-3.0 like this notebook)
      README.md  LICENSE  Makefile
      src/  include/zst.h  tools/zst.c  tests/  tests/reference/  bench/
      docs/formulas.md      Section 1 of this note, kept in lockstep with the code
      docs/extensions.md    Section 6 of this note
      proto/ccm_proto.py    the mpmath reference (kept, never optimised)

## 4. Milestones and acceptance criteria

- M0 (done today): reading, formula sheet, mpmath prototype, paper's table reproduced, FLINT
  function inventory verified (`flint_smoke.c`).
- M1 zeta pipeline, approximate: `zst --lambda 3 --N 40 --digits 60` prints 20 zeros; matches the
  prototype to `1e-30`. Deliverables: `weil_data.c` (zeta), `kernel.c`, `loewner.c`, approximate
  `eigmin.c`, `secular.c` with the `2N` count, `compare.c`. One day of work.
- M2 certification: Rump enclosure of the eigenpair, inertia-certified even-simplicity, interval
  Newton roots with certified radii, certified `|z_k - gamma_k|`; adaptive precision driver.
  Acceptance: the paper's `sqrt 13` column reproduced with certified bounds; a certified statement
  "for `lambda = sqrt 13, N = 120` the even-simple hypothesis holds and `|z_1 - gamma_1| < 3e-55`".
- M3 generality: the archimedean constants derived from the gamma-factor data rather than typed
  in (Gauss's integral for `psi`, window-edge terms); `zst_weil_dirichlet` for real primitive
  characters (`Gamma_R(s + a)`, `a` the parity, no pole term, conductor as identity shift).
  Acceptance: zeta constants `w(L), C(L)` regenerated by the general routine to working precision;
  `L(s, chi_{-4})` low zeros reproduced against `acb_dirichlet_hardy_z` root isolation.
- M4 scale: `lambda^2 = 50..100`, `N = 500..1500`, thousands of digits; OpenMP; timing table;
  the `(lambda, N) -> accuracy` map and the `eps_N` versus `1 - chi_4(lambda)` law over a range of
  `lambda` (needs prolate eigenvalues; see 6.7).
- M5 `det_reg -> Xi` study and the prolate comparison `xi_lambda` vs `k_lambda` (Section 7 of the
  paper): requires prolate spheroidal wave functions at high precision (Legendre-basis eigenproblem
  of `PW_lambda`; arb has no built-in), a separate module.

## 5. Why this is worth doing beyond reproduction

The construction is a machine that takes the finite data of an explicit formula on a window
(atoms, kernels, trivial divisor) and returns a self-adjoint operator whose spectrum approximates
the nontrivial divisor, with the spectrum provably real for every `(lambda, N)`. That is exactly
the shape of question this notebook keeps asking (shards 08b/08c: Weil positivity for an arbitrary
transfer operator; 02h: graded RH/FE/Ramanujan on a divisor with a designated trivial part). The
Weil form here is the finite Weil form of `thm:weil-positivity-finite` in the continuous setting,
and the Connes-van Suijlekom structure theorem is the mechanism that turns positivity into reality.
Three consequences the tool can test:

1. On finite objects (graphs, curves) the discrete analogue is the classical Caratheodory-Fejer
   theorem for Toeplitz matrices: the window Weil form `sum_theta |f_hat(theta)|^2` over the retained
   divisor has a Toeplitz matrix of rank equal to the number of distinct retained points, so once the
   window exceeds that number the kernel vector's polynomial vanishes exactly on the divisor. Below
   that window size one gets an approximation regime like the paper's, on an object where the truth
   is known: the natural place to study how the accuracy depends on the window.
2. For infinite objects with a known "RH" (Selberg zeta of a compact surface, where reality comes
   from self-adjointness of the Laplacian; shards 03e/03f) the construction can be run against the
   Laplace spectrum, and the modular surface adds the Riemann zeros at `rho/2` through the scattering
   term (the cusp comb of shard 09c, `obs:modular-scattering-sector`): whether one self-adjoint
   operator built from prime geodesics plus the cusp comb reproduces both the Maass `r_j` and the
   `gamma_n/2` is a computational form of the H-CUSP-BRIDGE question.
3. The construction supplies, for each window, a positive form making a perturbed scaling operator
   self-adjoint; how that form relates to the letter-derived metrics of `thm:hashimoto-lift-metric`
   and to the `G` of `def:graded-rh-fe-ramanujan` (HP) is a question the finite cases can settle.

## 6. Extension roadmap, mapped to this notebook's cases

6.1 Real Dirichlet characters (M3). Atoms `w = -chi(p^m) Lambda p^{-m/2}`; kernel from
`Gamma_R(s + a)`, `a in {0, 1}`; no pole; conductor `log q` as identity shift (moves `eps` only,
a fact worth stating: the spectrum of the construction does not see the conductor except through
the atoms). Test against `acb_dirichlet_hardy_z` zeros. Relevance: `conj:galois-graded-bond`
(zeros of `L(s, chi)` organised by characters); the tool gives, per character, a self-adjoint
operator on the same window.

6.2 Complex characters and non-self-dual L-functions. The Weil form is Hermitian and the
distribution is not even under `y -> -y` (`D(-y) = conj D(y)`); `tau` is Hermitian with complex
`b_n` and the same rank-two commutator. Two routes: (a) the real form of the pair `{chi, conj chi}`
(atoms `2 Re chi(p^m) ...`), zeros the union, real symmetric; (b) the Hermitian version of the
Connes-van Suijlekom theorem (to be checked in arXiv:CS 2025 before implementing). Route (a) first.

6.3 Dedekind zeta, Hecke and GL(2) L-functions. Atoms at `m log N(P)` with Frobenius/Satake weights
(`(alpha_p^m + beta_p^m) log p p^{-m/2}` for a weight-`k` form), kernels `r_1 Gamma_R + r_2 Gamma_C`
or `Gamma_C(s + (k-1)/2)`, pole term for Dedekind. Relevance: the Hecke identification of the
Weil-LPS joint spectra (`conj:weil-lps-hecke`) gives concrete weight-2 forms of level `p` to feed in.

6.4 Finite transfer operators: Ihara zeta of a graph, Artin-Schreier and elliptic curves, Weil-LPS
channels (shards 05, 06, 06b-06h, 08). The group is `Z` (lengths integers), the window is `{-M..M}`,
the atoms are the ring norms `Tr E^l - trivial` at `l = 1..M` with weights `q^{-l/2}`, no archimedean
kernel, the trivial divisor as pole terms. This is the Toeplitz/Caratheodory-Fejer case of item 5.1;
implement as `zst_weil_discrete` and use it (a) as an exact sanity anchor, (b) to study the
under-resolved window regime, (c) for graded divisors (zeros odd, poles even) where the Weil form is
`sum_ret (-nu(lambda)) |f_hat|^2` and the sign bookkeeping of `def:graded-transfer-channel` applies.

6.5 Selberg zeta. Compact surface: atoms at `k l(gamma)` with weights `l(gamma_0) / (2 sinh(k l/2))`
(prime geodesics from a Fuchsian group, e.g. arithmetic groups where lengths come from traces),
identity kernel `(Area/4 pi) * sum_k k e^{-kx}`-type (polynomial prefactor, step 1), trivial
divisor from the `Gamma_2` factors. Divisor to recover: `1/2 +- i r_j`. Modular surface: add the
parabolic kernel (digamma symbol) and the scattering atoms (`Lambda(n)/n` at `2 log n`, shard 09c),
recover Maass `r_j` and `gamma_n/2` together. Geodesic data for small windows is sparse (traces
`t <= 2 cosh(L/2)`), so windows must be larger than in the zeta case; the tool's scaling (M4)
matters here.

6.6 The divisor formulation. Once 6.4 and 6.5 exist, the input can be phrased directly in the
notebook's terms: a graded transfer channel or cMPS generator gives ring norms (atoms) and a
designated trivial divisor (poles); `libzst` returns a self-adjoint operator and a positive form.
This is the bridge from the notebook's definitions to a computable object, and the natural home for
experiments on "Hermitian channel plus lift versus odd block unitary".

6.7 Prolate side (M5). High-precision prolate spheroidal functions (`PW_lambda` eigenproblem in a
Legendre basis, tridiagonal, arb-certifiable), `1 - chi_n(lambda)`, and `k_lambda = E(h_lambda)`; the
paper's Figures `fpro3`, `fpro4`, `fpro1` and the `xi_lambda` vs `k_lambda` comparison at high
precision. This is the part that touches the missing proof.

## 7. First experiments once M2 exists

1. `(lambda, N)` accuracy map for zeros 1..50, `lambda^2 = 9..40`, `N = 40..400`: locate the `N`-limited
   and `lambda`-limited regimes; check the `5.5` digits per unit `lambda^2` law and the `s < N/2` rule.
2. `eps_N(lambda)` certified positive and monotone; compare with `1 - chi_4(lambda)` once 6.7 exists.
3. `x = lambda^2 = 100`, `N ~ 1000`, `~ 1500` digits: does the first zero reach 500 digits?
4. Sign pattern and decay of `xi_j`; relation to the prolate Fourier coefficients.
5. `det_reg` vs `Xi` on `|Im z| <= 0.4` as `lambda` grows (paper Section 7).
6. The odd block: does its minimal eigenvector give anything (an "odd" operator with real spectrum
   by the same lemma, if `<eta|xi_odd>` can be replaced by a suitable functional)? Not in the paper.

## 8. Risks and open points

- arb has no symmetric eigensolver; the inverse-iteration plus Rump plus inertia route is standard
  but must be written and tested carefully at condition numbers `1e60` and beyond.
- Root isolation with sign-changing `xi_j` (several roots per pole interval, roots near poles where
  `xi_j` is at noise level): the `2N` count is the safeguard; near-double roots need the symmetric
  fallback.
- The general archimedean regularisation (M3) is the one place where a derivation, not a
  transcription, is required; validate it by regenerating the zeta constants.
- Hermitian (complex character) case needs the theorem, not just code.
- Prolate functions at high precision are their own project.
- Everything about convergence (`N, lambda -> infinity`) remains numerical; the tool makes the
  numerics rigorous, not the limit.
