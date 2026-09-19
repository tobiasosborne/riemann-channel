/* rank.c: the exact (integer) stage of the window form -- rank, the critical window, and the
 * integer kernel polynomial.
 *
 * Ground truth: lanes/code-audit.md:296-320 (section 3): D = diag(q^{j/2}) gives the INTEGER
 * congruence (D T D)_{jk} = q^{min(j,k)} c_{|j-k|}, which by Sylvester has the same rank and
 * inertia as T; and notes/zeta-spectral-triples/ihara/plan.md:356-368 (section 4.3, "exact stage":
 * exact rank, and ker T computed exactly).  The regimes and the blind detection of the critical
 * window are lanes/theory.md:485-499 (IH-18, PROVED) and plan.md:196-203:
 *
 *     under-resolved  K <= R    rank T = K      eps > 0
 *     critical        K = R+1   rank T = K-1    eps = 0, dim ker = 1, roots(Ptilde) = the divisor
 *     over-resolved   K > R+1   rank T = R      dim ker = K-R >= 2
 *
 * so the critical window is the first odd K = 2Mp+1 at which the rank stops growing (IH-21(d),
 * plan.md:203).  Since ker T = D ker(D T D) and D is diagonal in q^{j/2} = r^j, a kernel vector y
 * of D T D gives the kernel polynomial in the UNRESCALED variable z = mu = r w directly:
 * Q(z) = sum_j y_j z^j, an integer polynomial vanishing on the retained divisor
 * (include/ihz.h `exact` convention row; plan.md:356-368).
 */
#include "ihz.h"

slong
ihz_rank_exact(const ihz_weil_t *W, slong Mp)
{
    slong K = 2 * Mp + 1, r;
    fmpz_mat_t DTD;
    fmpz_mat_init(DTD, K, K);
    ihz_toeplitz_exact(DTD, W, Mp);
    r = fmpz_mat_rank(DTD);
    fmpz_mat_clear(DTD);
    return r;
}

slong
ihz_critical_window(slong *R, const ihz_weil_t *W)
{
    slong Mp, K, r;
    for (Mp = 0; Mp <= W->M; Mp++)
    {
        K = 2 * Mp + 1;
        r = ihz_rank_exact(W, Mp);
        if (r < K)
        {
            *R = r;
            return Mp;
        }
    }
    return -1;
}

int
ihz_kernel_poly_exact(fmpz_poly_t Q, const ihz_weil_t *W, slong Mp)
{
    slong K = 2 * Mp + 1, j, nullity;
    fmpz_mat_t DTD, X;
    fmpz_t g;
    int ok = 0;

    fmpz_mat_init(DTD, K, K);
    fmpz_mat_init(X, K, K);
    ihz_toeplitz_exact(DTD, W, Mp);
    nullity = fmpz_mat_nullspace(X, DTD);
    if (nullity == 1)
    {
        fmpz_poly_zero(Q);
        for (j = 0; j < K; j++)
            fmpz_poly_set_coeff_fmpz(Q, j, fmpz_mat_entry(X, j, 0));
        /* primitive, positive leading coefficient */
        fmpz_init(g);
        fmpz_poly_content(g, Q);
        if (!fmpz_is_zero(g))
        {
            fmpz_poly_scalar_divexact_fmpz(Q, Q, g);
            if (fmpz_sgn(fmpz_poly_lead(Q)) < 0)
                fmpz_poly_neg(Q, Q);
            ok = 1;
        }
        fmpz_clear(g);
    }
    fmpz_mat_clear(DTD);
    fmpz_mat_clear(X);
    return ok;
}
