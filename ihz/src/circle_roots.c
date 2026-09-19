/* Certified roots on [0, pi] of R(theta) = xi_0 + 2 sum_{j=1}^{Mp} xi_j cos(j theta).
 *
 * Ground truth:
 *   include/ihz.h:26-28, 140-147           (the theta-substitution and this API)
 *   notes/zeta-spectral-triples/ihara/lanes/code-audit.md:229-262
 *       (section 2.5: "the theta-substitution works cleanly"; arb_calc_isolate_roots +
 *        interval Newton, smoke-tested; none of secular.c's cancellation problem)
 *   notes/zeta-spectral-triples/ihara/plan.md:356-371 (4.3: "roots of R(theta) by
 *       arb_calc_isolate_roots plus interval Newton (no cancellation problem ...)")
 *   notes/zeta-spectral-triples/ihara/lanes/theory.md:297-320 (IH-11 (iv): the roots of Ptilde
 *       are K-1 points on |w| = 1; for even xi, P(e^{i theta}) = e^{iM theta} R(theta), so a root
 *       theta in (0, pi) is a conjugate pair and theta in {0, pi} a single real point)
 *   zst/src/secular.c:118-170 (the interval-Newton verify/contract pattern used here; R has no
 *       cancellation problem, so the plain derivative box is enough -- no mean-value form)
 *
 * Index convention: xi is the FULL window vector of length 2*Mp+1 with xi_j at index Mp + j,
 * j = -Mp..Mp, and is assumed even (xi_{-j} = xi_j); only indices Mp..2*Mp are read.
 *
 * Endpoints.  R'(0) = R'(pi) = 0 always (sin(j*0) = sin(j*pi) = 0), so no sign change can ever
 * isolate a root at an endpoint.  They are therefore tested directly: R(0) = sum_j xi_j and
 * R(pi) = sum_j (-1)^j xi_j.  A certified-nonzero value means "not a root"; a ball containing zero
 * is reported through *unresolved, never as a certified root.
 */
#include <stdlib.h>
#include <flint/arb_calc.h>
#include "ihz.h"

#define IHZ_SPLIT_DEPTH  5        /* mid-interval-splitting fallback depth */
#define IHZ_ISO_MAXDEPTH 40
#define IHZ_ISO_MAXEVAL  10000
#define IHZ_WORK_BUDGET  200      /* isolation calls per ihz_circle_roots; degenerate-input guard */

typedef struct { arb_srcptr xi; slong Mp; } ihz_R_param;

void
ihz_R_eval(arb_t val, arb_t der, const arb_t theta, arb_srcptr xi, slong Mp, slong prec)
{
    slong j;
    arb_t v, d, s, c, jt;

    arb_init(v); arb_init(d); arb_init(s); arb_init(c); arb_init(jt);

    arb_set(v, xi + Mp);                       /* xi_0 */
    for (j = 1; j <= Mp; j++)
    {
        arb_mul_si(jt, theta, j, prec);
        arb_sin_cos(s, c, jt, prec);
        arb_mul(c, c, xi + Mp + j, prec);
        arb_mul_2exp_si(c, c, 1);              /* 2 xi_j cos(j theta) */
        arb_add(v, v, c, prec);
        if (der != NULL)
        {
            arb_mul(s, s, xi + Mp + j, prec);
            arb_mul_si(s, s, -2 * j, prec);    /* -2 j xi_j sin(j theta) */
            arb_add(d, d, s, prec);
        }
    }
    if (val != NULL) arb_set(val, v);
    if (der != NULL) arb_set(der, d);

    arb_clear(v); arb_clear(d); arb_clear(s); arb_clear(c); arb_clear(jt);
}

/* R at theta = 0 (sgn = +1: sum over all j of xi_j) and at theta = pi (sgn = -1: sum over all j
 * of (-1)^j xi_j), exactly, with no error contributed by a pi ball. */
static void
ihz_R_endpoint(arb_t v, arb_srcptr xi, slong Mp, int sgn, slong prec)
{
    slong j;
    arb_t acc, t;
    arb_init(acc); arb_init(t);
    arb_set(acc, xi + Mp);
    for (j = 1; j <= Mp; j++)
    {
        arb_mul_2exp_si(t, xi + Mp + j, 1);
        if (sgn < 0 && (j & 1)) arb_sub(acc, acc, t, prec);
        else                    arb_add(acc, acc, t, prec);
    }
    arb_set(v, acc);
    arb_clear(acc); arb_clear(t);
}

static int
ihz_R_func(arb_ptr out, const arb_t inp, void *param, slong order, slong prec)
{
    const ihz_R_param *P = (const ihz_R_param *) param;
    ihz_R_eval(out, (order >= 2) ? out + 1 : NULL, inp, P->xi, P->Mp, prec);
    return ARB_CALC_SUCCESS;
}

/* Interval Newton on a ball: X = m +- 2^e; if R'(X) excludes 0 and N(X) = m - R(m)/R'(X) lies
 * strictly inside X then X holds exactly one root; then contract.  Returns 1 on success. */
static int
ihz_verify_root(arb_t out, const arb_t start, const ihz_R_param *P, slong prec)
{
    arb_t X, m, v, dm, dX, nx;
    slong e, it, k;
    int ok = 0;

    arb_init(X); arb_init(m); arb_init(v); arb_init(dm); arb_init(dX); arb_init(nx);

    /* polish the midpoint with plain Newton in midpoint arithmetic */
    arb_get_mid_arb(m, start);
    for (k = 0; k < 60; k++)
    {
        ihz_R_eval(v, dm, m, P->xi, P->Mp, prec);
        arb_get_mid_arb(v, v); arb_get_mid_arb(dm, dm);
        if (arb_is_zero(dm)) break;
        arb_div(v, v, dm, prec);
        arb_sub(m, m, v, prec);
        arb_get_mid_arb(m, m);
    }

    for (e = -(prec - 8); e <= -8 && !ok; e += 8)
    {
        arb_set(X, m); arb_add_error_2exp_si(X, e);
        ihz_R_eval(v, NULL, m, P->xi, P->Mp, prec);
        ihz_R_eval(NULL, dX, X, P->xi, P->Mp, prec);
        if (arb_contains_zero(dX)) continue;
        arb_div(nx, v, dX, prec);
        arb_sub(nx, m, nx, prec);
        if (arb_contains(X, nx) && mag_cmp(arb_radref(nx), arb_radref(X)) < 0)
            ok = 1;
    }
    if (ok)
    {
        arb_set(X, nx);
        for (it = 0; it < 100; it++)
        {
            arb_get_mid_arb(m, X);
            ihz_R_eval(v, NULL, m, P->xi, P->Mp, prec);
            ihz_R_eval(NULL, dX, X, P->xi, P->Mp, prec);
            if (arb_contains_zero(dX)) break;
            arb_div(nx, v, dX, prec);
            arb_sub(nx, m, nx, prec);
            if (!arb_overlaps(nx, X)) break;
            arb_intersection(nx, nx, X, prec);
            if (mag_cmp(arb_radref(nx), arb_radref(X)) >= 0) break;
            arb_set(X, nx);
        }
        arb_set(out, X);
    }

    arb_clear(X); arb_clear(m); arb_clear(v); arb_clear(dm); arb_clear(dX); arb_clear(nx);
    return ok;
}

/* a point at one of the given fractions of the block, nudged until R is certified nonzero there */
static void
ihz_cut_point(arf_t out, const arf_interval_t blk, const double *frac, slong nfrac,
              const ihz_R_param *P, slong prec)
{
    arb_t x, w, v, f;
    slong i;
    arb_init(x); arb_init(w); arb_init(v); arb_init(f);
    for (i = 0; i < nfrac; i++)
    {
        arb_set_arf(x, &blk->a);
        arb_set_arf(w, &blk->b);
        arb_sub(w, w, x, prec);
        arb_set_d(f, frac[i]);
        arb_mul(w, w, f, prec);
        arb_add(x, x, w, prec);
        arb_get_mid_arb(x, x);
        ihz_R_eval(v, NULL, x, P->xi, P->Mp, prec);
        if (!arb_contains_zero(v)) break;
    }
    arf_set(out, arb_midref(x));
    arb_clear(x); arb_clear(w); arb_clear(v); arb_clear(f);
}

static void
ihz_isolate_rec(arb_ptr theta, slong maxroots, slong *found, slong *unres, slong *budget,
                const arf_interval_t block, const ihz_R_param *P, slong depth, slong prec)
{
    static const double half[4] = { 0.5, 0.375, 0.625, 0.4375 };
    arf_interval_ptr blocks;
    int *flags;
    slong i, n, nmax;
    int degen;
    arb_t ball, root;

    if (*found >= maxroots) return;
    if (arf_cmp(&block->a, &block->b) >= 0) return;
    if (*budget <= 0) { (*unres)++; return; }
    (*budget)--;

    nmax = P->Mp + 1;      /* R has at most Mp roots in [0, pi]; +1 so the sweep always finishes */
    n = arb_calc_isolate_roots(&blocks, &flags, ihz_R_func, (void *) P, block,
                               IHZ_ISO_MAXDEPTH, IHZ_ISO_MAXEVAL >> FLINT_MIN(depth, 4),
                               nmax, prec);
    /* A degenerate R (a double root: R and R' vanish together, which no sign change can see)
     * makes the bisection return thousands of unknown blocks.  Keep the certified ones, call the
     * rest a single unresolved candidate, and do not recurse: the split fallback would cost
     * 2^IHZ_SPLIT_DEPTH isolations per block. */
    degen = (n > 4 * P->Mp + 8);

    arb_init(ball); arb_init(root);
    for (i = 0; i < n; i++)
    {
        if (degen && flags[i] != 1) continue;
        if (*found >= maxroots) { (*unres)++; continue; }
        arf_interval_get_arb(ball, blocks + i, prec);

        if (flags[i] == 1)
        {   /* arb_calc_isolate_roots certified exactly one root in this block */
            if (ihz_verify_root(root, ball, P, prec) && arb_overlaps(root, ball))
            { arb_set(theta + *found, root); (*found)++; }
            else (*unres)++;
        }
        else if (depth < IHZ_SPLIT_DEPTH)
        {   /* mid-interval-splitting fallback */
            arf_interval_t L, Rr;
            arf_t mid;
            arf_interval_init(L); arf_interval_init(Rr); arf_init(mid);
            ihz_cut_point(mid, blocks + i, half, 4, P, prec);
            if (arf_cmp(mid, &blocks[i].a) > 0 && arf_cmp(mid, &blocks[i].b) < 0)
            {
                arf_set(&L->a, &blocks[i].a); arf_set(&L->b, mid);
                arf_set(&Rr->a, mid);         arf_set(&Rr->b, &blocks[i].b);
                ihz_isolate_rec(theta, maxroots, found, unres, budget, L,  P, depth + 1, prec);
                ihz_isolate_rec(theta, maxroots, found, unres, budget, Rr, P, depth + 1, prec);
            }
            else (*unres)++;
            arf_interval_clear(L); arf_interval_clear(Rr); arf_clear(mid);
        }
        else
        {   /* last resort at the splitting depth limit: interval Newton on the block itself.  It
             * certifies a root sitting exactly ON a block endpoint, which no sign change can see;
             * a duplicate coming from the two blocks either side is merged afterwards. */
            if (ihz_verify_root(root, ball, P, prec) && arb_overlaps(root, ball))
            { arb_set(theta + *found, root); (*found)++; }
            else (*unres)++;
        }
    }
    if (degen) (*unres)++;

    arb_clear(ball); arb_clear(root);
    _arf_interval_vec_clear(blocks, n);
    flint_free(flags);
}

slong
ihz_circle_roots(arb_ptr theta, slong maxroots, slong *unresolved,
                 arb_srcptr xi, slong Mp, slong prec)
{
    /* Generic first cut.  Dyadic bisection of [0, L], L ~ pi, puts its split points at the
     * multiples of pi/2^n -- exactly the angles a graph divisor sits on (3 pi/4 for Petersen at
     * K = 5) -- and a root landing on a split point has no sign change at any scale.  Cutting
     * first at ~0.618 L makes the grid generic. */
    static const double gcut[4] = { 0.6180339887498949, 0.5713567, 0.6539123, 0.4271907 };
    ihz_R_param P;
    arb_t v, vg, gap;
    arf_interval_t block, Lh, Rh;
    arf_t cut;
    slong found = 0, unres = 0, budget = IHZ_WORK_BUDGET, i, j;

    P.xi = xi; P.Mp = Mp;
    if (unresolved != NULL) *unresolved = 0;
    if (maxroots <= 0 || Mp < 0) return 0;

    arb_init(v); arb_init(vg); arb_init(gap);
    arf_interval_init(block); arf_interval_init(Lh); arf_interval_init(Rh); arf_init(cut);

    /* theta = 0: R(0) = sum_j xi_j */
    ihz_R_endpoint(v, xi, Mp, +1, prec);
    if (arb_contains_zero(v)) unres++;

    /* theta = pi: R(pi) = sum_j (-1)^j xi_j.  The isolation stops at a rigorous lower bound
     * L <= pi, so the sliver [L, pi] is covered here by evaluating R on the ball [L, U] that
     * contains it (U >= pi). */
    arb_const_pi(gap, prec);
    arb_get_lbound_arf(&block->a, gap, prec);
    arb_get_ubound_arf(&block->b, gap, prec);
    arb_set_interval_arf(gap, &block->a, &block->b, prec);
    ihz_R_endpoint(v, xi, Mp, -1, prec);
    ihz_R_eval(vg, NULL, gap, xi, Mp, prec);
    if (arb_contains_zero(v) || arb_contains_zero(vg)) unres++;

    /* isolate on [0, L] */
    arf_set(&block->b, &block->a);
    arf_zero(&block->a);
    ihz_cut_point(cut, block, gcut, 4, &P, prec);
    if (arf_cmp(cut, &block->a) > 0 && arf_cmp(cut, &block->b) < 0)
    {
        arf_set(&Lh->a, &block->a); arf_set(&Lh->b, cut);
        arf_set(&Rh->a, cut);       arf_set(&Rh->b, &block->b);
        ihz_isolate_rec(theta, maxroots, &found, &unres, &budget, Lh, &P, 0, prec);
        ihz_isolate_rec(theta, maxroots, &found, &unres, &budget, Rh, &P, 0, prec);
    }
    else
        ihz_isolate_rec(theta, maxroots, &found, &unres, &budget, block, &P, 0, prec);

    /* sort increasing */
    for (j = 1; j < found; j++)
    {
        i = j;
        while (i > 0 && arb_lt(theta + i, theta + i - 1)) { arb_swap(theta + i, theta + i - 1); i--; }
    }
    /* merge overlapping enclosures: they come from disjoint isolating blocks, so an overlap is
     * one root seen twice (a root on a shared block endpoint); the intersection still holds it */
    for (j = 1; j < found; j++)
    {
        if (!arb_overlaps(theta + j, theta + j - 1)) continue;
        arb_intersection(theta + j - 1, theta + j - 1, theta + j, prec);
        for (i = j; i + 1 < found; i++) arb_swap(theta + i, theta + i + 1);
        found--; j--;
    }

    if (unresolved != NULL) *unresolved = unres;
    arb_clear(v); arb_clear(vg); arb_clear(gap);
    arf_interval_clear(block); arf_interval_clear(Lh); arf_interval_clear(Rh); arf_clear(cut);
    return found;
}
