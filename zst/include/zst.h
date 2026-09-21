/* zst: zeta spectral triples (Connes-Consani-Moscovici, arXiv:2511.22755) on FLINT/arb.
 *
 * Tracer-bullet MVP. Pipeline:
 *   zst_riemann_ab      window explicit-formula data of zeta -> Loewner data (a_n, b_n), balls
 *   zst_even_block      (a, b) -> even block E (N+1 x N+1) of the Weil form matrix
 *   zst_odd_block       (a, b) -> odd block  O (N x N)
 *   zst_eigmin          minimal eigenpair of E: approximate inverse iteration, then Rump enclosure
 *   zst_inertia_neg     number of eigenvalues below a shift (unpivoted LDL^T in ball arithmetic)
 *   zst_secular_roots   the real zeros s of g(s) = sum_j xi_j/(j - s): isolation + interval Newton
 *   zst_zeta_zeros      imaginary parts gamma_k of the first K zeros of zeta (acb_dirichlet)
 * Conventions: notes/zeta-spectral-triples/plan.md, Section 1.
 */
#ifndef ZST_H
#define ZST_H

#include <flint/flint.h>
#include <flint/arb.h>
#include <flint/acb.h>
#include <flint/arb_mat.h>
#include <flint/acb_mat.h>
#include <flint/fmpz.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Loewner data of the truncated Weil form of zeta on the window [lambda^-1, lambda], lambda^2 = x.
 * a[n], b[n] for n = 0..N (a[-n] = a[n], b[-n] = -b[n]); tau_{nm} = (b_n - b_m)/(n - m), tau_{nn} = a_n.
 * X is the prime-power cutoff (all prime powers 1 < k <= X enter); normally X = floor(x). */
void zst_riemann_ab(arb_ptr a, arb_ptr b, slong N, const arb_t x, ulong X, slong prec);

/* Window length L = 2 log lambda = log x. */
void zst_window_L(arb_t L, const arb_t x, slong prec);

/* Even block in the basis V_0, (V_j + V_{-j})/sqrt2, j = 1..N; odd block in (V_j - V_{-j})/sqrt2. */
void zst_even_block(arb_mat_t E, arb_srcptr a, arb_srcptr b, slong N, slong prec);
void zst_odd_block(arb_mat_t O, arb_srcptr a, arb_srcptr b, slong N, slong prec);

/* Minimal eigenpair of the real symmetric E. Up to `iters` inverse-iteration steps on midpoints
 * (one LU reused; stops early when stationary), then Rump's verified enclosure, retried up to 3 times. On success returns 1 with eps and v (length dim(E)) as certified balls
 * (v normalised as Rump returns it); returns 0 if the enclosure could not be certified. */
int zst_eigmin(arb_t eps, arb_ptr v, const arb_mat_t E, slong iters, slong prec);

/* Number of eigenvalues of the symmetric A strictly below `shift`, by the inertia of the unpivoted
 * LDL^T factorisation of A - shift. Returns -1 if some pivot ball contains zero (inconclusive). */
slong zst_inertia_neg(const arb_mat_t A, const arb_t shift, slong prec);

/* Certificate of the paper's even-simple hypothesis from a certified even eigenpair (eps, v):
 * with s = 2 * upper(eps), certifies by ball Cholesky that E - s + v v^T/|v|^2 and O - s are positive
 * definite. Then E - s has exactly one negative eigenvalue (interlacing under the rank-one update,
 * and eps - s < 0 along v) and O - s has none: eps is the simple smallest eigenvalue of the whole
 * matrix and its eigenvector is even. Error amplification is linear in the condition number, unlike
 * the unpivoted LDL^T of zst_inertia_neg. Returns 1 if certified, 0 otherwise. */
int zst_certify_even_simple(const arb_mat_t E, const arb_mat_t O, const arb_t eps, arb_srcptr v, slong prec);

/* The N positive zeros of g(s) = sum_{j=-N}^{N} xi_j/(j - s), xi_{-j} = xi_j, xi[0..N] given as
 * balls with sum_j xi_j = 1 (g is odd, so these are half of its 2N real zeros). Candidates are the
 * square roots of the eigenvalues of the odd block of D'^2 (approximate QR); each is certified by
 * interval Newton. Writes up to `maxroots` certified, pairwise disjoint root balls into `roots`,
 * increasing; returns the count. A return value of N is a certified complete list. *unresolved
 * counts candidates that could not be certified (0 on success). */
slong zst_secular_roots(arb_ptr roots, slong maxroots, slong *unresolved,
                        arb_srcptr xi, slong N, slong prec);

/* Interval-Newton certification of one root of g from an approximation s_approx (a point): returns 1
 * and the certified root ball if some interval s_approx +- 2^e (e from -prec/3 up to -16) is mapped
 * strictly into itself by the Newton operator, then contracted; 0 otherwise. */
int zst_secular_verify(arb_t root, arb_srcptr xi, slong N, const arb_t s_approx, slong prec);

/* h_j(s) = g(s) (j - s)(j + 1 - s) for j < N, h_N(s) = g(s)(N - s): value and derivative at the ball s. */
void zst_secular_eval(arb_t val, arb_t der, const arb_t s, arb_srcptr xi, slong N, slong j, slong prec);

/* gamma[k-1] = Im rho_k for k = 1..K. */
void zst_zeta_zeros(arb_ptr gamma, slong K, slong prec);


/* ---- MVP-3 (2026-09-18): the general explicit-formula data model; Dirichlet characters; E/Q ----
 * AUTHORITATIVE formula sheet: notes/zeta-spectral-triples/ellcurve/astra-review.md, "Formula sheet
 * for the workers", F1-F18 (cite F-numbers in code comments next to the TeX lines). Window distribution
 * (F2, F6, F8) on [0, L], L = log x = 2 log lambda:
 *   D(q) = sum_k w_k q(y_k)                                                     atoms, 0 < y_k <= L
 *        - sum_g mult_g int_0^L (q(y) - q(0)) rho_{d_g, mu_g}(y) dy             gamma factors, SUBTRACTED
 *        + (pole terms, F18, rank two at +-1/2 for zeta)
 *        + (s/2) q(0),   s = log C + sum_g mult_g [2 log Q_g + (2/d_g) psi(mu_g/d_g) + 2 T_{d_g,mu_g}(L)]
 * with rho_{d,mu}(y) = sum_{k>=0} e^{-(dk+mu)y} and a gamma factor Q^s Gamma((s + kappa)/d), mu = kappa
 * + 1/2 (F6). (a_n, b_n) per F3/F16: b_n = -(1/pi) D(sin omega_n y), a_n = 2 D((1 - y/L) cos omega_n y),
 * omega_n = 2 pi n / L; the identity shift s is added to every a_n. zst_weil_riemann must reproduce
 * zst_riemann_ab (full a_n including the shift) to all digits: F10/F12. */
typedef struct {
    arb_t    L;                                   /* window length, L = log x */
    slong    natoms; arb_ptr y; arb_ptr w;        /* atoms: positions in (0, L], real weights (F5: -t_m log p / p^m) */
    slong    ngamma; arb_ptr Q; arb_ptr d; arb_ptr mu; slong *mult;  /* gamma factors Q^s Gamma((s+kappa)/d), mu = kappa + 1/2 */
    fmpz_t   cond;                                /* conductor C (>= 1); contributes +log C to the shift (F8) */
    slong    npoles; arb_ptr sigma; slong *pmult; /* rank-one pole terms at real sigma (zeta: +-1/2, F18); usually 0 */
    arb_t    shift_extra;                         /* any further identity shift (default 0; Q3 invariance tests) */
} zst_weil_t;

void zst_weil_init(zst_weil_t *W, slong natoms, slong ngamma, slong npoles, slong prec);
void zst_weil_clear(zst_weil_t *W);

/* Window integrals I1, I2, I3 of one kernel rho_{d,mu} for mode n >= 0 (F13-F15: polygamma plus the
 * z = e^{-dL} series with the rigorous tail F15). */
void zst_kernel_I123(arb_t I1, arb_t I2, arb_t I3, slong n, const arb_t d, const arb_t mu, const arb_t L, slong prec);

/* Convergent tail T_{d,mu}(L) = int_L^inf rho_{d,mu} (F8) and the total identity shift s of W (F8). */
void zst_kernel_tail(arb_t T, const arb_t d, const arb_t mu, const arb_t L, slong prec);
void zst_weil_shift(arb_t s, const zst_weil_t *W, slong prec);

/* Loewner data (a_n, b_n), n = 0..N (F16; b_0 = 0 exactly). */
void zst_weil_ab(arb_ptr a, arb_ptr b, slong N, const zst_weil_t *W, slong prec);

/* Constructors. x = lambda^2 (window), X = prime-power cutoff (all p^m with 1 < p^m <= X enter). */
void zst_weil_riemann(zst_weil_t *W, const arb_t x, ulong X, slong prec);
/* Real primitive Dirichlet character of fundamental discriminant D (chi(n) = Kronecker (D/n)),
 * gamma factor Gamma_R(s + kappa), kappa = 0 for D > 0, 1 for D < 0; conductor |D|; no pole. */
void zst_weil_dirichlet(zst_weil_t *W, const fmpz_t D, const arb_t x, ulong X, slong prec);
/* Elliptic curve E/Q from a GLOBAL MINIMAL Weierstrass model [a1,a2,a3,a4,a6] and its conductor C
 * (both inputs; taken from tests/data/ell_ref.txt, never computed here): atoms per F4/F5, gamma
 * factor Gamma_C(s + 1/2) as (Q = 1/(2 pi), d = 1, mu = 1, mult 1), no pole (F17). */
void zst_weil_ellcurve(zst_weil_t *W, const fmpz *ainvs, const fmpz_t C, const arb_t x, ulong X, slong prec);

/* a_p = p - A_p, A_p = number of affine F_p-solutions of the general Weierstrass equation, singular
 * point included (F4); valid at good and bad primes of a minimal model, also p = 2, 3. */
slong zst_ell_ap(const fmpz *ainvs, ulong p);

/* Reference data from tests/data/ell_ref.txt (tools/pari_ref.py; PARI 2.17.2). Fills the minimal
 * model, conductor, root number w, analytic rank, and the first K zero ordinates gamma_k (analytic
 * normalisation; central zeros as 0 with multiplicity) as balls of radius 1e-38. Returns 1, or 0 if the
 * label is absent. `path` NULL = default location relative to the zst directory. */
int zst_ell_ref(fmpz *ainvs, fmpz_t C, int *w, slong *rank, arb_ptr gamma, slong K,
                const char *label, const char *path, slong prec);

/* Certified MINIMUM eigenpair of a real symmetric block (not the smallest modulus: the block is shifted
 * below its Frobenius bound before inverse iteration, then Rump-enclosed). Returns 1 on success. */
int zst_block_min(arb_t lam, arb_ptr v, const arb_mat_t A, slong iters, slong prec);

/* Parity of the global minimum of the Weil form (review, Q1): certified minima of E and O. Returns
 * +1 if min E < min O is certified (even-simple candidate; then zst_certify_even_simple applies),
 * -1 if min O < min E is certified (odd minimum: the paper's construction is inapplicable), 0 if
 * undecided. gap = certified lower bound on |min E - min O|. */
int zst_parity(arb_t minE, arb_t minO, arb_t gap, const arb_mat_t E, const arb_mat_t O, slong iters, slong prec);

#ifdef __cplusplus
}
#endif
#endif
