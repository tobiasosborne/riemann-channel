/* cycles.c -- exact cycle counts N_k = Tr B^k and the Ihara-Bass identity as an exact
 * polynomial identity over Z.
 *
 * Ground truth (by file and line):
 *   notes/zeta-spectral-triples/ihara/lanes/theory.md:30-33   Ihara-Bass; N_k = Tr B^k, N_0 = 2|E|
 *   notes/zeta-spectral-triples/ihara/plan.md:75-88           section 1.1 (objects, cycle counts)
 *   notes/zeta-spectral-triples/ihara/lanes/code-audit.md:63  section 2.1 (use repeated
 *       fmpz_mat_mul from a running product, not kmax separate fmpz_mat_pow calls)
 *   notes/zeta-spectral-triples/ihara/ihara_proto.py:126      check_ihara_bass()
 *       (Q = diag(deg - 1), so the identity is checked in the irregular form too)
 *   notes/zeta-spectral-triples/ihara/run_ihara_proto.txt:36  K4: N_1..N_7 = 0,0,24,24,0,96,168
 *
 * det(1 - uB): fmpz_mat_charpoly gives det(x - B) of degree n = 2|E|; reversing it gives
 * u^n det(1/u - B) = det(1 - uB).  The same reversal turns det(x^2 - xA + Q), obtained as the
 * charpoly of the 2|V| x 2|V| companion block [[A, -Q],[I, 0]], into det(1 - Au + Q u^2).
 */
#include "ihz.h"

void ihz_cycle_counts(fmpz *N, const fmpz_mat_t B, slong kmax)
{
    slong n = fmpz_mat_nrows(B), k;
    fmpz_mat_t P, T;

    if (kmax < 0) return;
    fmpz_set_si(N + 0, n);                       /* N_0 = Tr B^0 = 2|E| */
    if (kmax == 0 || n == 0)
    {
        for (k = 1; k <= kmax; k++) fmpz_zero(N + k);
        return;
    }

    fmpz_mat_init(P, n, n);
    fmpz_mat_init(T, n, n);
    fmpz_mat_set(P, B);                          /* running product B^k */
    for (k = 1; k <= kmax; k++)
    {
        if (k > 1)
        {
            fmpz_mat_mul(T, P, B);
            fmpz_mat_swap(P, T);
        }
        fmpz_mat_trace(N + k, P);
    }
    fmpz_mat_clear(T);
    fmpz_mat_clear(P);
}

/* (1 - u^2)^g into R */
static void one_minus_u2_pow(fmpz_poly_t R, slong g)
{
    fmpz_poly_t base;

    fmpz_poly_init(base);
    fmpz_poly_set_coeff_si(base, 0, 1);
    fmpz_poly_set_coeff_si(base, 2, -1);
    fmpz_poly_pow(R, base, (ulong) g);
    fmpz_poly_clear(base);
}

int ihz_ihara_bass_check(const ihz_graph_t *G, const fmpz_mat_t B)
{
    slong nv = G->nv, ne = G->ne, n = 2 * ne, i, g;
    slong *deg;
    fmpz_mat_t A, C;
    fmpz_poly_t lhs, rhs, cp, fac;
    int eq;

    /* LHS: det(1 - uB) = reverse of charpoly(B) */
    fmpz_poly_init(lhs);
    fmpz_poly_init(cp);
    fmpz_mat_charpoly(cp, B);
    fmpz_poly_reverse(lhs, cp, n + 1);
    fmpz_poly_clear(cp);

    /* companion block C = [[A, -Q],[I, 0]], Q = diag(deg - 1); charpoly(C) = det(x^2 - xA + Q) */
    deg = flint_calloc((size_t) (nv > 0 ? nv : 1), sizeof(slong));
    for (i = 0; i < ne; i++) { deg[G->u[i]]++; deg[G->v[i]]++; }

    fmpz_mat_init(A, nv, nv);
    ihz_adjacency(A, G);
    fmpz_mat_init(C, 2 * nv, 2 * nv);
    fmpz_mat_zero(C);
    for (i = 0; i < nv; i++)
    {
        slong j;
        for (j = 0; j < nv; j++)
            fmpz_set(fmpz_mat_entry(C, i, j), fmpz_mat_entry(A, i, j));
        fmpz_set_si(fmpz_mat_entry(C, i, nv + i), -(deg[i] - 1));
        fmpz_one(fmpz_mat_entry(C, nv + i, i));
    }
    fmpz_mat_clear(A);
    flint_free(deg);

    fmpz_poly_init(rhs);
    fmpz_poly_init(cp);
    fmpz_mat_charpoly(cp, C);
    fmpz_poly_reverse(rhs, cp, 2 * nv + 1);        /* det(1 - Au + Q u^2) */
    fmpz_poly_clear(cp);
    fmpz_mat_clear(C);

    /* multiply by (1 - u^2)^{|E|-|V|}; if the exponent is negative (a tree), move it left */
    g = ne - nv;
    fmpz_poly_init(fac);
    if (g >= 0)
    {
        one_minus_u2_pow(fac, g);
        fmpz_poly_mul(rhs, rhs, fac);
    }
    else
    {
        one_minus_u2_pow(fac, -g);
        fmpz_poly_mul(lhs, lhs, fac);
    }
    fmpz_poly_clear(fac);

    eq = fmpz_poly_equal(lhs, rhs);
    fmpz_poly_clear(rhs);
    fmpz_poly_clear(lhs);
    return eq;
}
