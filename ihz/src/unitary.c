/* The unitary key lemma IH-11: U = Z^* - |Z^* xi><eta|, its T-isometry certificate and the
 * determinant identity.
 *
 * Ground truth:
 *   notes/zeta-spectral-triples/ihara/lanes/theory.md:297-320 (IH-11, statement and proof):
 *     U := Z^*(1 - |xi><eta|) = Z^* - |Z^* xi><eta|,  <eta|xi> = xi_0 = 1;
 *     (i) U xi = 0;  (ii) U^* T U = T exactly;  (iii) det(U'' - w) = (-1)^{K+1} Ptilde(w),
 *     Ptilde(w) = sum_{k=0}^{K-1} xi_k w^{K-1-k}, together with det(U - w) = -w det(U'' - w).
 *   notes/zeta-spectral-triples/ihara/lanes/theory.md:433-448 (IH-15: xi_0 != 0 is automatic)
 *   notes/zeta-spectral-triples/ihara/plan.md:117-157 (1.3, the convention trap: eta is the
 *     delta at the window edge in the POSITION basis, never all-ones)
 *   include/ihz.h:33 (eta), 149-157 (this API)
 *
 * CONVENTIONS FIXED HERE (the caller must match them):
 *   position basis e_0..e_{K-1}; Z e_j = e_{j+1 mod K}, hence Z^* e_j = e_{j-1 mod K}, i.e.
 *     (Z^*)_{ij} = 1 iff i = (j - 1) mod K   and   (Z^* xi)_i = xi_{(i+1) mod K};
 *   eta = e_0 (position index 0), so |Z^* xi><eta| has column 0 equal to Z^* xi and the rest 0:
 *     U_{ij} = (Z^*)_{ij} - (Z^* xi)_i [j == 0];
 *   xi is the full window vector of length K = 2Mp+1 RE-INDEXED to 0..K-1 (entry k is xi_{k-Mp});
 *   NORMALISATION: the caller must pass xi already divided by xi[0], so that xi[0] = 1
 *     (= <eta|xi>).  ihz_unitary_build does not renormalise; if xi[0]'s ball contains zero the
 *     matrix is built anyway and the checks below are simply expected to fail.
 *   Ptilde in ihz_unitary_det_check uses the same position-basis entries xi[0..K-1].
 */
#include "ihz.h"

void
ihz_unitary_build(arb_mat_t U, arb_srcptr xi, slong K, slong prec)
{
    slong i, j;

    arb_mat_zero(U);
    for (j = 0; j < K; j++)
        arb_one(arb_mat_entry(U, (j + K - 1) % K, j));      /* Z^* */

    for (i = 0; i < K; i++)                                  /* minus |Z^* xi><eta| */
        arb_sub(arb_mat_entry(U, i, 0), arb_mat_entry(U, i, 0), xi + ((i + 1) % K), prec);

}

int
ihz_unitary_check(const arb_mat_t U, const arb_mat_t T, const arb_t eps, slong prec)
{
    slong K = arb_mat_nrows(T), i, j;
    arb_mat_t S, Ut, X, Y;
    int ok = 1;

    arb_mat_init(S, K, K); arb_mat_init(Ut, K, K);
    arb_mat_init(X, K, K); arb_mat_init(Y, K, K);

    arb_mat_set(S, T);                                       /* S = T - eps I */
    for (i = 0; i < K; i++)
        arb_sub(arb_mat_entry(S, i, i), arb_mat_entry(S, i, i), eps, prec);

    arb_mat_transpose(Ut, U);
    arb_mat_mul(X, S, U, prec);
    arb_mat_mul(Y, Ut, X, prec);
    arb_mat_sub(Y, Y, S, prec);

    for (i = 0; i < K && ok; i++)
        for (j = 0; j < K && ok; j++)
            if (!arb_contains_zero(arb_mat_entry(Y, i, j))) ok = 0;

    arb_mat_clear(S); arb_mat_clear(Ut); arb_mat_clear(X); arb_mat_clear(Y);
    return ok;
}

int
ihz_unitary_det_check(const arb_mat_t U, arb_srcptr xi, slong K, const acb_t w, slong prec)
{
    acb_mat_t A;
    acb_t d, p, t;
    slong i, k;
    int ok;

    acb_mat_init(A, K, K);
    acb_init(d); acb_init(p); acb_init(t);

    for (i = 0; i < K; i++)
    {
        slong j;
        for (j = 0; j < K; j++)
            acb_set_arb(acb_mat_entry(A, i, j), arb_mat_entry(U, i, j));
        acb_sub(acb_mat_entry(A, i, i), acb_mat_entry(A, i, i), w, prec);
    }
    acb_mat_det(d, A, prec);

    /* Ptilde(w) = sum_{k=0}^{K-1} xi_k w^{K-1-k}, by Horner in the position index */
    acb_zero(p);
    for (k = 0; k < K; k++)
    {
        acb_mul(p, p, w, prec);
        acb_add_arb(p, p, xi + k, prec);
    }
    /* IH-11 (iii): det(U - w) = -w det(U'' - w) = -w (-1)^{K+1} Ptilde(w) */
    acb_mul(t, p, w, prec);
    acb_neg(t, t);
    if (((K + 1) & 1) != 0) acb_neg(t, t);

    ok = acb_overlaps(d, t);

    acb_mat_clear(A); acb_clear(d); acb_clear(p); acb_clear(t);
    return ok;
}
