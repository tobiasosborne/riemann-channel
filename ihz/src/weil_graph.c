/* weil_graph.c: window data of the Weil form straight from a finite (q+1)-regular graph.
 *
 * Ground truth: notes/zeta-spectral-triples/ihara/plan.md:88-104 (section 1.1: spec(B) = trivial
 * multiset u retained multiset, S_triv = {q, 1} plus {-q, -1} if bipartite plus +-1 with
 * multiplicity |E|-|V| each) and plan.md:107-137 / lanes/theory.md:90-118 (IH-3, the lag-by-lag
 * identity t_k = q^{-k/2} N_k - trivial_k, with N_k = Tr B^k).  The trivial divisor is exactly the
 * `trivial` row of the convention table of include/ihz.h; getting it wrong is load-bearing
 * (plan.md:216-218).  sign = +1: for an ungraded graph the retained divisor consists of POLES
 * (IH-6, plan.md:139-142).
 *
 * The Toeplitz form of the window {-M..M} needs lags 0..2M, hence N_0..N_{2M} (plan.md:150-152).
 */
#include <stdlib.h>
#include "ihz.h"

int
ihz_weil_from_graph(ihz_weil_t *W, const ihz_graph_t *G, slong M, slong prec)
{
    slong q, g, kmax = 2 * M, ntriv, i;
    int bip;
    fmpz_mat_t B;
    fmpz *N, *tr;
    slong *tm;

    if (!ihz_graph_is_regular(G, &q))
        return 0;

    bip = ihz_graph_is_bipartite(G);
    g = G->ne - G->nv;                      /* = -chi(X), the multiplicity of +-1 */

    /* trivial divisor, per the convention table of include/ihz.h */
    ntriv = bip ? 6 : 4;
    tr = _fmpz_vec_init(ntriv);
    tm = flint_malloc(sizeof(slong) * ntriv);
    i = 0;
    fmpz_set_si(tr + i, q);       tm[i++] = 1;
    fmpz_set_si(tr + i, 1);       tm[i++] = 1;
    if (bip)
    {
        fmpz_set_si(tr + i, -q);  tm[i++] = 1;
        fmpz_set_si(tr + i, -1);  tm[i++] = 1;
    }
    fmpz_set_si(tr + i, 1);       tm[i++] = g;
    fmpz_set_si(tr + i, -1);      tm[i++] = g;

    /* N_k = Tr B^k, k = 0..2M (N_0 = 2|E|) */
    fmpz_mat_init(B, 2 * G->ne, 2 * G->ne);
    ihz_hashimoto(B, G);
    N = _fmpz_vec_init(kmax + 1);
    ihz_cycle_counts(N, B, kmax);
    fmpz_mat_clear(B);

    ihz_weil_from_counts(W, N, M, q, tr, tm, ntriv, 1, prec);

    _fmpz_vec_clear(N, kmax + 1);
    _fmpz_vec_clear(tr, ntriv);
    flint_free(tm);
    return 1;
}
