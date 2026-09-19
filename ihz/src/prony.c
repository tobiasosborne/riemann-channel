/* Prony/Vandermonde weights at the critical window: the multiplicities of the retained divisor.
 *
 * Ground truth:
 *   notes/zeta-spectral-triples/ihara/lanes/theory.md:517-536 (IH-20, PROVED): the construction
 *     returns the support only; at K = R+1 the weights solve the Vandermonde system
 *     t_d = sum_j alpha_j w_j^d and alpha_j = m(w_j) is the unique solution (the w_j are
 *     distinct, so the Vandermonde has full column rank).  Petersen: (5,5,4,4).
 *   notes/zeta-spectral-triples/ihara/plan.md:158-182 (1.4) and 323-355 (4.2, src/prony.c)
 *   include/ihz.h:14 (w = mu / r, r = sqrt q), 104 (t already sign-adjusted), 159-162.
 *
 * Solves the R x R square system sum_i alpha_i (mu_i/r)^d = t_d, d = 0..R-1, with acb_mat_solve.
 * If the solve fails (a ball matrix that cannot be certified invertible) every alpha_i is set
 * indeterminate, so no wrong multiplicity is ever reported.
 */
#include "ihz.h"

void
ihz_prony_weights(acb_ptr alpha, const ihz_weil_t *W, acb_srcptr mu, slong R, slong prec)
{
    acb_mat_t V, b, x;
    acb_t w;
    arb_t r;
    slong i, d;

    if (R <= 0) return;

    acb_mat_init(V, R, R); acb_mat_init(b, R, 1); acb_mat_init(x, R, 1);
    acb_init(w); arb_init(r);

    arb_sqrt_ui(r, (ulong) W->q, prec);                  /* r = sqrt q, the critical radius */

    for (i = 0; i < R; i++)
    {
        acb_div_arb(w, mu + i, r, prec);                 /* w_i = mu_i / r */
        acb_one(acb_mat_entry(V, 0, i));
        for (d = 1; d < R; d++)
            acb_mul(acb_mat_entry(V, d, i), acb_mat_entry(V, d - 1, i), w, prec);
    }
    for (d = 0; d < R; d++)
        acb_set_arb(acb_mat_entry(b, d, 0), W->t + d);

    if (acb_mat_solve(x, V, b, prec))
        for (i = 0; i < R; i++) acb_set(alpha + i, acb_mat_entry(x, i, 0));
    else
        for (i = 0; i < R; i++) acb_indeterminate(alpha + i);

    acb_mat_clear(V); acb_mat_clear(b); acb_mat_clear(x);
    acb_clear(w); arb_clear(r);
}
