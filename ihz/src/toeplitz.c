/* toeplitz.c: the window form T_{jk} = t_{|j-k|}, its even/odd blocks under the grading gamma, the
 * lift of an even-block vector to the full window, and the exact integer congruence D T D.
 *
 * Ground truth: notes/zeta-spectral-triples/ihara/plan.md:150-152 (position basis, K = 2M+1, lags
 * up to 2M), lanes/theory.md:456-466 (IH-16, PROVED: T is real symmetric Toeplitz hence
 * persymmetric, Cantoni-Butler splits it into blocks of sizes ceil(K/2) and floor(K/2); this is
 * CCM's gamma) and lanes/code-audit.md:60-66 (the entry formula is a direct t[|i-j|] +- t[i+j]
 * lookup, not a Loewner divided difference).  The exact integer congruence is
 * lanes/code-audit.md:296-320 (section 3):  (D T D)_{jk} = q^{min(j,k)} c_{|j-k|}, D = diag(q^{j/2}),
 * an integer matrix with the same inertia, rank and (after applying D) kernel as T.
 *
 * Basis conventions are the `grading` row of include/ihz.h's convention table:
 *   E_00 = t_0,  E_0j = sqrt2 t_j,  E_ij = t_{|i-j|} + t_{i+j}      (i, j >= 1)
 *   O_ij = t_{|i-j|} - t_{i+j}                                      (i, j >= 1)
 *   even-block vector c  ->  xi_0 = c_0, xi_{+-j} = c_j / sqrt2, stored at index j + Mp.
 */
#include "ihz.h"

void
ihz_toeplitz(arb_mat_t T, const ihz_weil_t *W, slong Mp, slong prec)
{
    slong K = 2 * Mp + 1, j, k;
    for (j = 0; j < K; j++)
        for (k = 0; k < K; k++)
            arb_set(arb_mat_entry(T, j, k), W->t + FLINT_ABS(j - k));
}

void
ihz_even_block(arb_mat_t E, const ihz_weil_t *W, slong Mp, slong prec)
{
    slong n = Mp + 1, i, j;
    arb_t s2;
    arb_init(s2);
    arb_sqrt_ui(s2, 2, prec);

    arb_set(arb_mat_entry(E, 0, 0), W->t + 0);
    for (j = 1; j < n; j++)
    {
        arb_mul(arb_mat_entry(E, 0, j), W->t + j, s2, prec);
        arb_set(arb_mat_entry(E, j, 0), arb_mat_entry(E, 0, j));
    }
    for (i = 1; i < n; i++)
        for (j = 1; j < n; j++)
            arb_add(arb_mat_entry(E, i, j), W->t + FLINT_ABS(i - j), W->t + (i + j), prec);

    arb_clear(s2);
}

void
ihz_odd_block(arb_mat_t O, const ihz_weil_t *W, slong Mp, slong prec)
{
    slong i, j;
    /* rows/columns are the modes j = 1..Mp, stored at index j-1 */
    for (i = 1; i <= Mp; i++)
        for (j = 1; j <= Mp; j++)
            arb_sub(arb_mat_entry(O, i - 1, j - 1), W->t + FLINT_ABS(i - j), W->t + (i + j), prec);
}

void
ihz_even_to_full(arb_ptr xi, arb_srcptr c, slong Mp, slong prec)
{
    slong j;
    arb_t s2;
    arb_init(s2);
    arb_sqrt_ui(s2, 2, prec);
    arb_set(xi + Mp, c + 0);
    for (j = 1; j <= Mp; j++)
    {
        arb_div(xi + Mp + j, c + j, s2, prec);
        arb_set(xi + Mp - j, xi + Mp + j);
    }
    arb_clear(s2);
}

void
ihz_toeplitz_exact(fmpz_mat_t DTD, const ihz_weil_t *W, slong Mp)
{
    slong K = 2 * Mp + 1, j, k;
    fmpz_t pw;
    fmpz_init(pw);
    for (j = 0; j < K; j++)
        for (k = 0; k < K; k++)
        {
            fmpz_set_si(pw, W->q);
            fmpz_pow_ui(pw, pw, (ulong) FLINT_MIN(j, k));
            fmpz_mul(fmpz_mat_entry(DTD, j, k), pw, W->c + FLINT_ABS(j - k));
            if (W->sign < 0)
                fmpz_neg(fmpz_mat_entry(DTD, j, k), fmpz_mat_entry(DTD, j, k));
        }
    fmpz_clear(pw);
}
