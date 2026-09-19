/* hashimoto.c -- the Hashimoto (non-backtracking edge) operator B and the adjacency matrix A.
 *
 * Ground truth (by file and line):
 *   notes/zeta-spectral-triples/ihara/lanes/theory.md:23-33  section 0 (B on C^{2|E|}, N_0 = 2|E|)
 *   notes/zeta-spectral-triples/ihara/ihara_proto.py:110     hashimoto()  B[e,f]=1 iff e=(a,b),
 *                                                            f=(b,c), c != a
 *   notes/zeta-spectral-triples/ihara/ihara_proto.py:103     adjacency()
 *   notes/zeta-spectral-triples/ihara/lanes/code-audit.md:63 section 2.1 (fmpz_mat idioms;
 *                                                            K4 gives Tr B^3 = 24)
 *
 * Directed-edge index convention is the one fixed in include/ihz.h: d in 0..2ne-1 with
 * d = e the arc u[e] -> v[e] and d = e + ne the arc v[e] -> u[e].  The prototype interleaves
 * its arcs instead; the two differ by a permutation, so B's spectrum, traces and charpoly agree.
 */
#include "ihz.h"

/* tail and head of directed edge index d, in the header's convention */
static void arc(const ihz_graph_t *G, slong d, slong *from, slong *to)
{
    if (d < G->ne) { *from = G->u[d]; *to = G->v[d]; }
    else           { *from = G->v[d - G->ne]; *to = G->u[d - G->ne]; }
}

void ihz_hashimoto(fmpz_mat_t B, const ihz_graph_t *G)
{
    slong n = 2 * G->ne, i, j;
    slong *from, *to;

    fmpz_mat_zero(B);
    if (n == 0) return;

    from = flint_malloc(sizeof(slong) * (size_t) n);
    to = flint_malloc(sizeof(slong) * (size_t) n);
    for (i = 0; i < n; i++)
        arc(G, i, from + i, to + i);

    /* B[(a->b),(b->c)] = 1 iff c != a  (ihz.h convention table) */
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            if (from[j] == to[i] && to[j] != from[i])
                fmpz_one(fmpz_mat_entry(B, i, j));

    flint_free(to);
    flint_free(from);
}

void ihz_adjacency(fmpz_mat_t A, const ihz_graph_t *G)
{
    slong e;

    fmpz_mat_zero(A);
    for (e = 0; e < G->ne; e++)
    {
        fmpz_add_ui(fmpz_mat_entry(A, G->u[e], G->v[e]),
                    fmpz_mat_entry(A, G->u[e], G->v[e]), 1);
        fmpz_add_ui(fmpz_mat_entry(A, G->v[e], G->u[e]),
                    fmpz_mat_entry(A, G->v[e], G->u[e]), 1);
    }
}
