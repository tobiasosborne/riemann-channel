/* weil_data.c: the window data (N_k, c_k, t_k) of the Weil/Toeplitz form from raw counts.
 *
 * Ground truth: notes/zeta-spectral-triples/ihara/plan.md:107-137 (section 1.2, the explicit formula
 * in CCM's shape) and lanes/theory.md:90-118 (IH-3, PROVED: lag-by-lag
 * t_k = q^{-k/2} N_k - trivial part); the exact integer c_k and its sign convention are
 * lanes/code-audit.md:302-312 (section 3) and the convention table of include/ihz.h.
 *
 *   c_k = N_k - sum_i tm_i tr_i^k        exact integer ("retained" trace, sum over the retained divisor)
 *   t_k = sign * q^{-k/2} c_k            sign = +1 for a graph (poles), -1 for a curve (zeros)
 *
 * Self-contained: this file calls no other ihz module.
 */
#include <stdlib.h>
#include "ihz.h"

void
ihz_weil_from_counts(ihz_weil_t *W, const fmpz *N, slong M, slong q,
                     const fmpz *tr, const slong *tm, slong ntriv, int sign, slong prec)
{
    slong len = 2 * M + 1, i, k;
    fmpz_t pw, acc;
    arb_t r, den;

    W->M = M;
    W->q = q;
    W->sign = sign;
    W->ntriv = ntriv;
    W->tr = ntriv > 0 ? _fmpz_vec_init(ntriv) : NULL;
    W->tm = ntriv > 0 ? flint_malloc(sizeof(slong) * ntriv) : NULL;
    W->N = _fmpz_vec_init(len);
    W->c = _fmpz_vec_init(len);
    W->t = _arb_vec_init(len);

    for (i = 0; i < ntriv; i++)
    {
        fmpz_set(W->tr + i, tr + i);
        W->tm[i] = tm[i];
    }
    for (k = 0; k < len; k++)
        fmpz_set(W->N + k, N + k);

    /* c_k = N_k - sum_i tm_i tr_i^k, exact */
    fmpz_init(pw);
    fmpz_init(acc);
    for (k = 0; k < len; k++)
    {
        fmpz_zero(acc);
        for (i = 0; i < ntriv; i++)
        {
            fmpz_pow_ui(pw, W->tr + i, (ulong) k);
            fmpz_addmul_si(acc, pw, W->tm[i]);
        }
        fmpz_sub(W->c + k, W->N + k, acc);
    }
    fmpz_clear(pw);
    fmpz_clear(acc);

    /* t_k = sign * q^{-k/2} c_k as balls: only sqrt(q) is inexact (plan.md:358) */
    arb_init(r);
    arb_init(den);
    arb_sqrt_ui(r, (ulong) q, prec);
    for (k = 0; k < len; k++)
    {
        arb_set_fmpz(W->t + k, W->c + k);
        if (k > 0)
        {
            arb_pow_ui(den, r, (ulong) k, prec);
            arb_div(W->t + k, W->t + k, den, prec);
        }
        if (sign < 0)
            arb_neg(W->t + k, W->t + k);
    }
    arb_clear(r);
    arb_clear(den);
}

void
ihz_weil_clear(ihz_weil_t *W)
{
    slong len = 2 * W->M + 1;
    if (W->ntriv > 0)
    {
        _fmpz_vec_clear(W->tr, W->ntriv);
        flint_free(W->tm);
    }
    W->tr = NULL;
    W->tm = NULL;
    _fmpz_vec_clear(W->N, len);
    _fmpz_vec_clear(W->c, len);
    _arb_vec_clear(W->t, len);
    W->N = NULL;
    W->c = NULL;
    W->t = NULL;
    W->ntriv = 0;
}
