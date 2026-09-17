/* Even and odd blocks of the Loewner matrix tau_{nm} = (b_n - b_m)/(n - m), tau_{nn} = a_n
 * (a even, b odd in the index).
 * Ground truth: refs/src/2511.22755/mc2arXiv.tex, Lemma `basicexpli` eq. (form) l.817-819 and
 * Lemma `basics` (i) l.837: tau commutes with gamma: V_j -> V_{-j}, so it splits into the
 * gamma = +1 block (basis V_0, (V_j + V_{-j})/sqrt2) and the gamma = -1 block ((V_j - V_{-j})/sqrt2).
 * Block entries derived in notes/zeta-spectral-triples/plan.md Section 1.3. */
#include "zst.h"

static void
loewner_pair(arb_t plus, arb_t minus, arb_srcptr a, arb_srcptr b, slong i, slong j, slong prec)
{
    /* plus  = (b_i - b_j)/(i - j) + (b_i + b_j)/(i + j)   (i != j, i, j >= 1)
     * minus = (b_i - b_j)/(i - j) - (b_i + b_j)/(i + j) */
    arb_t t, u;
    arb_init(t); arb_init(u);
    arb_sub(t, b + i, b + j, prec); arb_div_si(t, t, i - j, prec);
    arb_add(u, b + i, b + j, prec); arb_div_si(u, u, i + j, prec);
    arb_add(plus, t, u, prec);
    arb_sub(minus, t, u, prec);
    arb_clear(t); arb_clear(u);
}

void zst_even_block(arb_mat_t E, arb_srcptr a, arb_srcptr b, slong N, slong prec)
{
    slong i, j;
    arb_t t, u, s2;
    arb_init(t); arb_init(u); arb_init(s2);
    arb_sqrt_ui(s2, 2, prec);
    arb_set(arb_mat_entry(E, 0, 0), a + 0);
    for (j = 1; j <= N; j++)
    {
        arb_div_si(t, b + j, j, prec); arb_mul(t, t, s2, prec);
        arb_set(arb_mat_entry(E, 0, j), t);
        arb_set(arb_mat_entry(E, j, 0), t);
        arb_div_si(t, b + j, j, prec); arb_add(arb_mat_entry(E, j, j), a + j, t, prec);
        for (i = 1; i < j; i++)
        {
            loewner_pair(t, u, a, b, i, j, prec);
            arb_set(arb_mat_entry(E, i, j), t);
            arb_set(arb_mat_entry(E, j, i), t);
        }
    }
    arb_clear(t); arb_clear(u); arb_clear(s2);
}

void zst_odd_block(arb_mat_t O, arb_srcptr a, arb_srcptr b, slong N, slong prec)
{
    slong i, j;
    arb_t t, u;
    arb_init(t); arb_init(u);
    for (j = 1; j <= N; j++)
    {
        arb_div_si(t, b + j, j, prec); arb_sub(arb_mat_entry(O, j - 1, j - 1), a + j, t, prec);
        for (i = 1; i < j; i++)
        {
            loewner_pair(t, u, a, b, i, j, prec);
            arb_set(arb_mat_entry(O, i - 1, j - 1), u);
            arb_set(arb_mat_entry(O, j - 1, i - 1), u);
        }
    }
    arb_clear(t); arb_clear(u);
}
