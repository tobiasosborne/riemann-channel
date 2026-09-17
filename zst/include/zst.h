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

#ifdef __cplusplus
}
#endif
#endif
