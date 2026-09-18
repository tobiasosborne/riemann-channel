/* truth.c -- the certified truth oracle: retained characteristic polynomial of B, its squarefree
 * part, and the certified retained spectrum with multiplicities.
 *
 * Ground truth (by file and line):
 *   notes/zeta-spectral-triples/ihara/lanes/theory.md:36-41  trivial divisor {q,1}, plus {-q,-1}
 *       if bipartite, plus +-1 with multiplicity |E|-|V| each; retained = the rest, of size
 *       2|V|-2 (2|V|-4 if bipartite)
 *   include/ihz.h:15-16                                      the same convention table
 *   notes/zeta-spectral-triples/ihara/lanes/code-audit.md:163 section 2.4, THE TRAP:
 *       arb_fmpz_poly_complex_roots does not terminate on a repeated root (its isolation loop
 *       `for (prec = initial_prec; ; prec *= 2)` never exits), so factor squarefree FIRST and
 *       call it once per squarefree factor, taking the multiplicity from the exponent.
 *   notes/zeta-spectral-triples/ihara/lanes/code-audit.md:212 K4 worked example: squarefree
 *       factors (x-2), (x+1)^2, (x^3 + ...)^3 with the retained pair mu^2 + mu + 2 = 0.
 *   notes/zeta-spectral-triples/ihara/plan.md:296-345         section 4.2 (src/truth.c route)
 *
 * NORMALISATION: fmpz_mat_charpoly returns the monic det(x - B); all trivial factors are monic,
 * so ihz_retained_charpoly returns a MONIC polynomial (leading coefficient +1) of degree
 * 2|V|-2, or 2|V|-4 when bipartite.
 */
#include <stdlib.h>
#include "ihz.h"
#include <flint/arb_fmpz_poly.h>

/* P <- P / (x - a)^m, exactly; 0 if any division is inexact */
static int divide_off(fmpz_poly_t P, slong a, slong m)
{
    fmpz_poly_t lin, quo;
    slong i;
    int ok = 1;

    if (m <= 0) return 1;
    fmpz_poly_init(lin);
    fmpz_poly_init(quo);
    fmpz_poly_set_coeff_si(lin, 1, 1);
    fmpz_poly_set_coeff_si(lin, 0, -a);
    for (i = 0; i < m && ok; i++)
    {
        if (!fmpz_poly_divides(quo, P, lin)) { ok = 0; break; }
        fmpz_poly_set(P, quo);
    }
    fmpz_poly_clear(quo);
    fmpz_poly_clear(lin);
    return ok;
}

int ihz_retained_charpoly(fmpz_poly_t P, const fmpz_mat_t B, slong q, int bipartite,
                          slong nv, slong ne)
{
    slong g = ne - nv;
    int ok;

    fmpz_mat_charpoly(P, B);

    /* trivial divisor, ihz.h:15-16 / theory.md:36-38 */
    ok = divide_off(P, q, 1) && divide_off(P, 1, 1);
    if (ok && bipartite)
        ok = divide_off(P, -q, 1) && divide_off(P, -1, 1);
    if (ok && g > 0)
        ok = divide_off(P, 1, g) && divide_off(P, -1, g);
    return ok;
}

void ihz_squarefree_part(fmpz_poly_t Q, const fmpz_poly_t P)
{
    fmpz_poly_factor_t fac;
    slong i;

    fmpz_poly_factor_init(fac);
    fmpz_poly_factor_squarefree(fac, P);
    fmpz_poly_one(Q);
    for (i = 0; i < fac->num; i++)
        if (fmpz_poly_degree(fac->p + i) > 0)
            fmpz_poly_mul(Q, Q, fac->p + i);
    fmpz_poly_factor_clear(fac);
}

/* canonical order: by real part, then imaginary part (midpoints) */
static int root_cmp(const acb_t x, const acb_t y)
{
    int c = arf_cmp(arb_midref(acb_realref(x)), arb_midref(acb_realref(y)));
    if (c != 0) return c;
    return arf_cmp(arb_midref(acb_imagref(x)), arb_midref(acb_imagref(y)));
}

int ihz_truth_spectrum(ihz_spectrum_t *S, const fmpz_poly_t P, slong prec)
{
    fmpz_poly_factor_t fac;
    acb_ptr mu;
    slong *mult;
    slong i, j, k, R = 0, d;

    S->mu = NULL;
    S->mult = NULL;
    S->R = 0;
    if (fmpz_poly_degree(P) < 1) return 1;          /* nothing retained: R = 0 */

    fmpz_poly_factor_init(fac);
    fmpz_poly_factor_squarefree(fac, P);            /* code-audit 2.4: never call the root finder
                                                       on P itself, only on squarefree factors */
    for (i = 0; i < fac->num; i++)
    {
        d = fmpz_poly_degree(fac->p + i);
        if (d > 0) R += d;
    }
    if (R == 0) { fmpz_poly_factor_clear(fac); return 1; }

    mu = _acb_vec_init(R);
    mult = flint_malloc(sizeof(slong) * (size_t) R);

    k = 0;
    for (i = 0; i < fac->num; i++)
    {
        d = fmpz_poly_degree(fac->p + i);
        if (d <= 0) continue;
        arb_fmpz_poly_complex_roots(mu + k, fac->p + i, 0, prec);
        for (j = 0; j < d; j++) mult[k + j] = fac->exp[i];
        k += d;
    }
    fmpz_poly_factor_clear(fac);

    /* sort (insertion; R is small here) into the canonical order */
    for (i = 1; i < R; i++)
    {
        acb_t tv;
        slong tm = mult[i];
        acb_init(tv);
        acb_set(tv, mu + i);
        for (j = i; j > 0 && root_cmp(mu + (j - 1), tv) > 0; j--)
        {
            acb_set(mu + j, mu + (j - 1));
            mult[j] = mult[j - 1];
        }
        acb_set(mu + j, tv);
        mult[j] = tm;
        acb_clear(tv);
    }

    S->mu = mu;
    S->mult = mult;
    S->R = R;
    return 1;
}

void ihz_spectrum_clear(ihz_spectrum_t *S)
{
    if (S->mu) _acb_vec_clear(S->mu, S->R);
    if (S->mult) flint_free(S->mult);
    S->mu = NULL;
    S->mult = NULL;
    S->R = 0;
}
