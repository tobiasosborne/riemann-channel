/* Window integrals and tail of one archimedean kernel of the general explicit-formula data model.
 *
 * A gamma factor Q^s Gamma((s + kappa)/d) of a completed L-function contributes, in the centred
 * conventions of the window distribution, the SUBTRACTED functional
 *
 *     D_kernel(q) = - int_0^L (q(y) - q(0)) rho_{d,mu}(y) dy,
 *     rho_{d,mu}(y) = e^{-mu y}/(1 - e^{-d y}) = sum_{k >= 0} e^{-(d k + mu) y},   mu = kappa + 1/2
 *
 * (formula sheet notes/zeta-spectral-triples/ellcurve/astra-review.md, F6; derivation from Gauss's
 * digamma integral in its "Derivation and source audit", which follows the paper's passage from the
 * gamma spectral symbol `thetaprime` to the one-sided distribution:
 * refs/src/2511.22755/mc2arXiv.tex lines 449-459, 490-495, 698-709).  The coefficient is -1, not -2,
 * also for Gamma_C.  This file computes the three window integrals the Loewner data needs (F13/F14,
 * the general-(d, mu) form of Prop. `computearch`, mc2arXiv.tex lines 720-771) and the convergent
 * tail T_{d,mu}(L) of the identity shift (F8).
 *
 * All series remainders are bounded rigorously by F15.
 */
#include <math.h>
#include <flint/acb.h>
#include <flint/mag.h>
#include "zst.h"

/* The regularisation helper: the endpoint series of F13,
 *     S_1 = sum_{k>=0} z^k/(k + A)^1,  S_2 = sum_{k>=0} z^k/(k + A)^2,  S_10 = sum_{k>=0} z^k/(k + a),
 * with z = e^{-dL} in (0, 1), A = (mu - i omega_n)/d and a = mu/d > 0.  These are exactly the pieces
 * left over after the infinite (0, infinity) integrals are evaluated as digamma/trigamma values, i.e.
 * they carry the window regularisation at y = L.  S1 and S2 may be NULL (tail-only use).
 *
 * Truncation after K terms, with the rigorous remainder F15
 *     |sum_{k>=K} z^k/(k + A)^r| <= z^K / [(1 - z) (K + a)^r]      (valid since |k + A| >= k + a),
 * added to every partial sum as a ball error. */
static void
kernel_series(acb_t S1, acb_t S2, arb_t S10, const acb_t A, const arb_t a, const arb_t z, slong prec)
{
    slong K, k;
    acb_t t, kA;
    arb_t zk, q, u;
    mag_t zmag, tail, den;
    double zd;

    acb_init(t); acb_init(kA);
    arb_init(zk); arb_init(q); arb_init(u);
    mag_init(zmag); mag_init(tail); mag_init(den);

    zd = arf_get_d(arb_midref(z), ARF_RND_UP);
    if (!(zd > 0) || zd >= 1) { flint_printf("zst kernel: z = e^{-dL} out of (0,1)\n"); flint_abort(); }
    K = (slong) (prec * 0.6931471805599453 / (-log(zd))) + 8;   /* z^K ~ 2^-prec */

    if (S1 != NULL) acb_zero(S1);
    if (S2 != NULL) acb_zero(S2);
    arb_zero(S10);
    arb_one(zk);
    for (k = 0; k < K; k++)
    {
        if (S1 != NULL)
        {
            acb_add_ui(kA, A, (ulong) k, prec);
            acb_inv(t, kA, prec);
            acb_mul_arb(t, t, zk, prec);
            acb_add(S1, S1, t, prec);
            if (S2 != NULL) { acb_div(t, t, kA, prec); acb_add(S2, S2, t, prec); }
        }
        arb_add_ui(q, a, (ulong) k, prec);
        arb_div(u, zk, q, prec);
        arb_add(S10, S10, u, prec);
        arb_mul(zk, zk, z, prec);
    }

    /* F15: z^K/(1 - z) divided by (K + a)^r, with a lower bound on K + a. */
    arb_get_mag(zmag, z);
    mag_geom_series(tail, zmag, K);                 /* >= sum_{k>=K} z^k = z^K/(1-z) */
    arb_add_ui(q, a, (ulong) K, prec);
    arb_get_mag_lower(den, q);
    mag_div(tail, tail, den);
    arb_add_error_mag(S10, tail);
    if (S1 != NULL) acb_add_error_mag(S1, tail);
    if (S2 != NULL) { mag_div(tail, tail, den); acb_add_error_mag(S2, tail); }

    acb_clear(t); acb_clear(kA);
    arb_clear(zk); arb_clear(q); arb_clear(u);
    mag_clear(zmag); mag_clear(tail); mag_clear(den);
}

/* F13/F14.  With omega_n = 2 pi n/L, A_n = (mu - i omega_n)/d, a = mu/d, z = e^{-dL}, e = e^{-mu L}:
 *   I1(n) = int_0^L sin(omega_n y) rho(y) dy      = -Im psi(A_n)/d - (e/d) Im S_1(n)
 *   I2(n) = int_0^L y cos(omega_n y) rho(y) dy    = Re psi'(A_n)/d^2 - (e/d^2) Re S_2(n)
 *                                                   - (e L/d) Re S_1(n)
 *   I3(n) = int_0^L (cos(omega_n y) - 1) rho(y) dy = [psi(a) - Re psi(A_n)]/d
 *                                                   - (e/d) Re S_1(n) + (e/d) S_1(0)
 * (these use e^{i omega_n L} = 1: integer frequencies only).  For (d, mu) = (2, 1/2) they are the
 * formulas of src/riemann_ab.c verbatim, i.e. mc2arXiv.tex lines 720-771.
 * The outputs must be distinct arb_t from the inputs. */
void
zst_kernel_I123(arb_t I1, arb_t I2, arb_t I3, slong n, const arb_t d, const arb_t mu,
                const arb_t L, slong prec)
{
    arb_t pi, omega, a, z, e, t, u, S10;
    acb_t A, psi, psi1, S1, S2, one;

    arb_init(pi); arb_init(omega); arb_init(a); arb_init(z); arb_init(e);
    arb_init(t); arb_init(u); arb_init(S10);
    acb_init(A); acb_init(psi); acb_init(psi1); acb_init(S1); acb_init(S2); acb_init(one);

    arb_const_pi(pi, prec);
    arb_mul_ui(omega, pi, 2 * (ulong) n, prec);
    arb_div(omega, omega, L, prec);                              /* omega_n = 2 pi n / L */
    arb_div(a, mu, d, prec);                                     /* a = mu/d */
    arb_set(acb_realref(A), a);
    arb_div(t, omega, d, prec); arb_neg(acb_imagref(A), t);      /* A_n = (mu - i omega_n)/d */
    arb_mul(t, d, L, prec); arb_neg(t, t); arb_exp(z, t, prec);  /* z = e^{-dL} */
    arb_mul(t, mu, L, prec); arb_neg(t, t); arb_exp(e, t, prec); /* e = e^{-mu L} */

    acb_digamma(psi, A, prec);
    acb_one(one);
    acb_polygamma(psi1, one, A, prec);
    kernel_series(S1, S2, S10, A, a, z, prec);

    /* I1 = -[Im psi(A) + e Im S1]/d */
    arb_mul(t, e, acb_imagref(S1), prec);
    arb_add(t, acb_imagref(psi), t, prec);
    arb_div(t, t, d, prec);
    arb_neg(I1, t);

    /* I2 = [Re psi'(A) - e Re S2]/d^2 - (e L/d) Re S1 */
    arb_mul(t, e, acb_realref(S2), prec);
    arb_sub(t, acb_realref(psi1), t, prec);
    arb_sqr(u, d, prec);
    arb_div(t, t, u, prec);
    arb_mul(u, e, L, prec); arb_mul(u, u, acb_realref(S1), prec); arb_div(u, u, d, prec);
    arb_sub(I2, t, u, prec);

    /* I3 = [psi(a) - Re psi(A) + e (S1(0) - Re S1)]/d */
    arb_digamma(t, a, prec);
    arb_sub(t, t, acb_realref(psi), prec);
    arb_sub(u, S10, acb_realref(S1), prec);
    arb_mul(u, u, e, prec);
    arb_add(t, t, u, prec);
    arb_div(I3, t, d, prec);

    arb_clear(pi); arb_clear(omega); arb_clear(a); arb_clear(z); arb_clear(e);
    arb_clear(t); arb_clear(u); arb_clear(S10);
    acb_clear(A); acb_clear(psi); acb_clear(psi1); acb_clear(S1); acb_clear(S2); acb_clear(one);
}

/* F8: T_{d,mu}(L) = int_L^infinity rho_{d,mu}(y) dy = (e^{-mu L}/d) sum_{k>=0} e^{-dLk}/(k + mu/d).
 * (For (d, mu) = (1, 1) this is the closed form -log(1 - e^{-L}) of F9.) */
void
zst_kernel_tail(arb_t T, const arb_t d, const arb_t mu, const arb_t L, slong prec)
{
    arb_t a, z, e, t, S10;

    arb_init(a); arb_init(z); arb_init(e); arb_init(t); arb_init(S10);

    arb_div(a, mu, d, prec);
    arb_mul(t, d, L, prec); arb_neg(t, t); arb_exp(z, t, prec);
    arb_mul(t, mu, L, prec); arb_neg(t, t); arb_exp(e, t, prec);
    kernel_series(NULL, NULL, S10, NULL, a, z, prec);
    arb_mul(t, S10, e, prec);
    arb_div(T, t, d, prec);

    arb_clear(a); arb_clear(z); arb_clear(e); arb_clear(t); arb_clear(S10);
}
