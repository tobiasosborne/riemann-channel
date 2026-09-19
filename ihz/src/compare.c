/* Certified distance from each truth point of the retained spectrum to the nearest point
 * returned by the construction.
 *
 * Ground truth:
 *   include/ihz.h:14 (critr: w = mu/r, r = sqrt q), 28 (the retained points are mu = r e^{i theta}
 *     at the roots of R), 143-144 (a root theta in (0, pi) stands for the conjugate pair;
 *     theta = 0 or pi is a single real point), 164-168 (this API)
 *   notes/zeta-spectral-triples/ihara/plan.md:323-355 (4.2, src/compare.c: "certified
 *     |theta_root - theta_truth| matched by angle")
 *   zst/src/compare.c (the same nearest-point-in-balls pattern for the zeta lane).
 *
 * err[i] is the ball of the distance |mu_i - r e^{+-i theta_k}| realised at the candidate whose
 * midpoint distance is smallest; every candidate distance is a rigorous enclosure, so err[i]
 * contains the true nearest distance whenever the nearest candidate is the one selected (and in
 * any case it is a rigorous enclosure of SOME candidate distance, hence an upper bound on the
 * true minimum up to its own radius).  With no roots at all err[i] is +inf.
 */
#include "ihz.h"

void
ihz_compare(arb_ptr err, arb_srcptr theta, slong n, const ihz_spectrum_t *S, slong q, slong prec)
{
    arb_t r, c, s, dist, pi;
    acb_t z, diff;
    slong i, k, sgn;

    arb_init(r); arb_init(c); arb_init(s); arb_init(dist); arb_init(pi);
    acb_init(z); acb_init(diff);
    arb_sqrt_ui(r, (ulong) q, prec);
    arb_const_pi(pi, prec);

    for (i = 0; i < S->R; i++)
    {
        int have = 0;
        arb_pos_inf(err + i);
        for (k = 0; k < n; k++)
        {
            /* theta in (0, pi): the conjugate pair r e^{+- i theta}; theta = 0 or pi: one point
             * (the two coincide there, so the branch only saves work) */
            int single = (arb_contains_zero(theta + k) || arb_contains(theta + k, pi));
            arb_sin_cos(s, c, theta + k, prec);
            for (sgn = 0; sgn < (single ? 1 : 2); sgn++)
            {
                arb_mul(acb_realref(z), c, r, prec);
                arb_mul(acb_imagref(z), s, r, prec);
                if (sgn) arb_neg(acb_imagref(z), acb_imagref(z));
                acb_sub(diff, S->mu + i, z, prec);
                acb_abs(dist, diff, prec);
                if (!have || arf_cmp(arb_midref(dist), arb_midref(err + i)) < 0)
                {
                    arb_set(err + i, dist);
                    have = 1;
                }
            }
        }
    }

    arb_clear(r); arb_clear(c); arb_clear(s); arb_clear(dist); arb_clear(pi);
    acb_clear(z); acb_clear(diff);
}
