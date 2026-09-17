/* Real zeros of the secular function g(s) = sum_{j=-N}^{N} xi_j/(j - s), xi_{-j} = xi_j.
 *
 * Ground truth: Connes-Consani-Moscovici, arXiv:2511.22755, local copy
 * refs/src/2511.22755/mc2arXiv.tex (sha256 in refs/manifest.sha256):
 *   Lemma `key` (iii), eq. (eq:detDp), lines 863-870:  Det(D'' - s) = Det(D - s) sum_j (j - s)^{-1} xi_j;
 *   Theorem `finmain` (iii), lines 1085-1118: the spectrum is real and equals the zeros of xi_hat;
 *   eq. (propor1), line 1113: the eigenvalue of D_log^{(lambda,N)} is z = 2 pi s / L.
 *
 * Method. D' = D - |D xi><eta| anticommutes with the parity gamma (D gamma = -gamma D, D xi odd,
 * eta even), so D'^2 is block diagonal; its odd block, in the coordinates o_1..o_N of an odd
 * vector (o_{-j} = -o_j), is
 *     M_{ij} = i^2 delta_{ij} - 2 i xi_i j,
 * whose N eigenvalues are the squares of the N positive roots of g (mu = s^2; the secular
 * determinant of M is 1 - 2 sum_i i^2 xi_i/(i^2 - mu), which is g(s) = 0 with sum_j xi_j = 1).
 * The eigenvalues are approximated by QR on midpoints, and each root s = sqrt(mu) is certified
 * by an interval Newton step on h_j(s) = g(s) (j - s)(j + 1 - s), the pole-free form on
 * [j, j+1] (h_N(s) = g(s)(N - s) beyond the last pole). N pairwise disjoint certified roots is a
 * complete list, since g P(s) is a polynomial of degree 2N, odd in s, with all roots real by the
 * theorem (certified separately through the even-simple inertia check).
 *
 * Why not global isolation: the normalisation sum_j xi_j = 1 makes the xi_j huge (the
 * eigenfunction is tiny at the window edge) while g is small in the upper intervals, so ball
 * evaluation over a sub-interval of width w has radius ~ (sum |xi_j|) w; covering a unit interval
 * with certified sign blocks would take ~1e9 blocks at N = 40. A point plus a tiny Newton interval
 * has no such problem. plan.md Sections 1.5, 3.4. */
#include <stdlib.h>
#include <math.h>
#include <flint/acb_mat.h>
#include "zst.h"

typedef struct { arb_srcptr xi; slong N; slong j; } sec_param;

/* ball evaluation of h_j and its derivative at s (j < N: P = (j-s)(j+1-s); j >= N: P = (N - s)) */
static void
sec_raw(arb_t h0, arb_t h1, const arb_t s, const sec_param *P, slong prec)
{
    slong k, N = P->N, j = P->j;
    arb_t Pv, Pd, t, u, den;
    arb_init(Pv); arb_init(Pd); arb_init(t); arb_init(u); arb_init(den);

    if (j < N)
    {   /* P = (j - s)(j+1 - s), P' = 2s - 2j - 1 */
        arb_sub_si(t, s, j, prec); arb_neg(t, t);
        arb_sub_si(u, s, j + 1, prec); arb_neg(u, u);
        arb_mul(Pv, t, u, prec);
        arb_mul_2exp_si(Pd, s, 1); arb_sub_si(Pd, Pd, 2 * j + 1, prec);
    }
    else
    {   /* P = (N - s), P' = -1 */
        arb_sub_si(Pv, s, N, prec); arb_neg(Pv, Pv);
        arb_set_si(Pd, -1);
    }
    arb_zero(h0); arb_zero(h1);
    for (k = -N; k <= N; k++)
    {
        arb_srcptr xk = P->xi + (k < 0 ? -k : k);
        if (k == j || (j < N && k == j + 1))
        {
            if (j < N)
            {   /* P/(k - s) = (other - s): value (other - s), derivative -1 */
                arb_sub_si(t, s, (k == j) ? j + 1 : j, prec); arb_neg(t, t);
                arb_addmul(h0, xk, t, prec);
                arb_sub(h1, h1, xk, prec);
            }
            else
                arb_add(h0, h0, xk, prec);         /* P/(N - s) = 1 */
            continue;
        }
        /* f = P/u, u = k - s, u' = -1:  f' = (P' u + P)/u^2 */
        arb_sub_si(den, s, k, prec); arb_neg(den, den);
        arb_div(t, Pv, den, prec);
        arb_addmul(h0, xk, t, prec);
        arb_mul(t, Pd, den, prec); arb_add(t, t, Pv, prec);
        arb_sqr(u, den, prec); arb_div(t, t, u, prec);
        arb_addmul(h1, xk, t, prec);
    }
    arb_clear(Pv); arb_clear(Pd); arb_clear(t); arb_clear(u); arb_clear(den);
}

void zst_secular_eval(arb_t val, arb_t der, const arb_t s, arb_srcptr xi, slong N, slong j, slong prec)
{
    sec_param P;
    P.xi = xi; P.N = N; P.j = j;
    sec_raw(val, der, s, &P, prec);
}

/* Interval Newton: X = s0 +- r. If h'(X) excludes 0 and N(X) = m - h(m)/h'(X) lies strictly inside
 * X, then X contains exactly one root; iterate the contraction. Returns 1 on success. */
static int
verify_root(arb_t r_out, const sec_param *P, const arb_t s0, slong prec)
{
    arb_t X, m, hm, dm, hX, dX, nx;
    slong e, it;
    int ok = 0;
    arb_init(X); arb_init(m); arb_init(hm); arb_init(dm); arb_init(hX); arb_init(dX); arb_init(nx);
    for (e = -(prec / 3); e <= -16 && !ok; e += 8)
    {
        arb_set(X, s0); arb_add_error_2exp_si(X, e);
        arb_get_mid_arb(m, X);
        sec_raw(hm, dm, m, P, prec);
        sec_raw(hX, dX, X, P, prec);
        if (arb_contains_zero(dX)) continue;
        arb_div(nx, hm, dX, prec); arb_sub(nx, m, nx, prec);
        if (arb_contains(X, nx) && mag_cmp(arb_radref(nx), arb_radref(X)) < 0)
            ok = 1;
    }
    if (ok)
    {
        arb_set(X, nx);
        for (it = 0; it < 100; it++)
        {
            arb_get_mid_arb(m, X);
            sec_raw(hm, dm, m, P, prec);
            sec_raw(hX, dX, X, P, prec);
            if (arb_contains_zero(dX)) break;
            arb_div(nx, hm, dX, prec); arb_sub(nx, m, nx, prec);
            if (!arb_overlaps(nx, X)) break;
            arb_intersection(nx, nx, X, prec);
            if (mag_cmp(arb_radref(nx), arb_radref(X)) >= 0) break;
            arb_set(X, nx);
        }
        arb_set(r_out, X);
    }
    arb_clear(X); arb_clear(m); arb_clear(hm); arb_clear(dm); arb_clear(hX); arb_clear(dX); arb_clear(nx);
    return ok;
}

int zst_secular_verify(arb_t root, arb_srcptr xi, slong N, const arb_t s_approx, slong prec)
{
    sec_param P;
    double sr = arf_get_d(arb_midref(s_approx), ARF_RND_NEAR);
    slong j = (slong) sr;
    if (j > N) j = N;
    if (j < 0) j = 0;
    P.xi = xi; P.N = N; P.j = j;
    return verify_root(root, &P, s_approx, prec);
}

static int
cmp_arf_d(const void *a, const void *b)
{
    double x = *(const double *) a, y = *(const double *) b;
    return (x > y) - (x < y);
}

/* Candidate generator 1: sign scan in midpoint arithmetic. On each unit interval [j, j+1] evaluate
 * h_j at G+1 equispaced points and bisect every sign change; beyond the last pole scan h_N on a
 * geometric grid up to 2^12 N. Returns the number of candidates written to sd (doubles suffice: the
 * candidates are polished by Newton at full precision before certification). */
static slong
candidates_scan(double *sd, arb_srcptr xi, slong N, slong prec, slong G)
{
    slong j, k, n = 0, it;
    sec_param P;
    arb_t s, lo, hi, h, d, hl, hh;
    P.xi = xi; P.N = N;
    arb_init(s); arb_init(lo); arb_init(hi); arb_init(h); arb_init(d); arb_init(hl); arb_init(hh);
    for (j = 0; j <= N && n < N; j++)
    {
        slong npts = (j < N) ? G : 64 * 26;    /* tail: distance from N = 2^(k/64)/16, k = 0..1664: 1.1% steps up to 2^22 (the
                                                 * tail roots come in pairs separated by ~10% of their distance from N) */
        int sgn_prev = 0;
        P.j = j;
        for (k = 0; k <= npts && n < N; k++)
        {
            int sgn;
            if (j < N) { arb_set_si(s, j); arb_set_si(d, k); arb_div_si(d, d, G, prec); arb_add(s, s, d, prec); }
            else       { arb_set_si(s, N); arb_set_d(d, pow(2.0, (double) k / 64.0) / 16.0); arb_add(s, s, d, prec); }
            sec_raw(h, d, s, &P, prec);
            sgn = arb_is_positive(h) ? 1 : (arb_is_negative(h) ? -1 : 0);
            if (sgn == 0) { sd[n++] = arf_get_d(arb_midref(s), ARF_RND_NEAR); sgn_prev = 0; continue; }
            if (sgn_prev != 0 && sgn != sgn_prev)
            {   /* bisect [lo, s] */
                arb_set(hi, s);
                for (it = 0; it < 40; it++)
                {
                    arb_add(d, lo, hi, prec); arb_mul_2exp_si(d, d, -1);
                    sec_raw(h, hl, d, &P, prec);
                    if (arb_is_positive(h) == (sgn > 0)) arb_set(hi, d); else arb_set(lo, d);
                }
                arb_add(d, lo, hi, prec); arb_mul_2exp_si(d, d, -1);
                sd[n++] = arf_get_d(arb_midref(d), ARF_RND_NEAR);
            }
            arb_set(lo, s); sgn_prev = sgn;
        }
    }
    arb_clear(s); arb_clear(lo); arb_clear(hi); arb_clear(h); arb_clear(d); arb_clear(hl); arb_clear(hh);
    return n;
}

/* Candidate generator 2: eigenvalues of M_ij = i^2 delta_ij - 2 i xi_i j by approximate QR at qr_prec. */
static slong
candidates_qr(double *sd, arb_srcptr xi, slong N, slong prec, slong qr_prec)
{
    slong i, j, n = 0;
    acb_mat_t M;
    acb_ptr mu;
    mag_t tol;
    arb_t t;
    acb_mat_init(M, N, N);
    mu = _acb_vec_init(N);
    mag_init(tol); arb_init(t);

    /* M_{ij} = i^2 delta_ij - 2 i xi_i j on midpoints (indices 1..N) */
    for (i = 1; i <= N; i++)
        for (j = 1; j <= N; j++)
        {
            arb_get_mid_arb(t, xi + i);
            arb_mul_si(t, t, -2 * i * j, prec);
            if (i == j) arb_add_ui(t, t, (ulong) (i * i), prec);
            acb_set_arb(acb_mat_entry(M, i - 1, j - 1), t);
        }
    /* candidates only need to land in the Newton basin, so the QR runs at reduced precision first;
     * zst_secular_roots retries at full precision if the certified list comes out incomplete */
    mag_set_ui_2exp_si(tol, 1, -qr_prec + 20);
    acb_mat_approx_eig_qr(mu, NULL, NULL, M, tol, 0, qr_prec);

    /* candidate positive roots s = sqrt(Re mu) */
    for (i = 0; i < N; i++)
    {
        double re = arf_get_d(arb_midref(acb_realref(mu + i)), ARF_RND_NEAR);
        if (re > 0) sd[n++] = sqrt(re);
    }
    acb_mat_clear(M); _acb_vec_clear(mu, N); mag_clear(tol); arb_clear(t);
    return n;
}

/* polish each candidate by Newton on midpoints, certify by interval Newton, sort, require disjointness */
static slong
roots_from_candidates(arb_ptr roots, slong maxroots, slong *unresolved,
                      arb_srcptr xi, slong N, slong prec, double *sd, slong ncand)
{
    slong i, j, found = 0, unres = 0;
    sec_param P;
    arb_t s0;
    P.xi = xi; P.N = N;
    arb_init(s0);
    qsort(sd, ncand, sizeof(double), cmp_arf_d);
    for (i = 0; i < ncand && found < maxroots; i++)
    {
        slong k;
        if (sd[i] <= 0) { unres++; continue; }
        if (i > 0 && sd[i] == sd[i - 1]) continue;       /* duplicate candidate */
        /* refine the candidate on midpoints with a few Newton steps before the interval step */
        arb_set_d(s0, sd[i]);
        P.j = (slong) sd[i]; if (P.j > N) P.j = N;
        for (k = 0; k < 8; k++)
        {
            arb_t h, d; arb_init(h); arb_init(d);
            sec_raw(h, d, s0, &P, prec);
            arb_get_mid_arb(h, h); arb_get_mid_arb(d, d);
            if (arb_is_zero(d)) { arb_clear(h); arb_clear(d); break; }
            arb_div(h, h, d, prec); arb_sub(s0, s0, h, prec); arb_get_mid_arb(s0, s0);
            arb_clear(h); arb_clear(d);
        }
        {
            double sr = arf_get_d(arb_midref(s0), ARF_RND_NEAR);
            slong jj = (slong) sr; if (jj > N) jj = N; if (jj < 0) jj = 0;
            P.j = jj;
        }
        if (verify_root(roots + found, &P, s0, prec)) found++;
        else
        {
            unres++;
            if (getenv("ZST_DEBUG"))
            {
                arb_t h, d; arb_init(h); arb_init(d);
                sec_raw(h, d, s0, &P, prec);
                flint_printf("secular: unverified candidate sd=%.17g s0=", sd[i]); arb_printn(s0, 25, 0);
                flint_printf(" j=%wd h(s0)=", P.j); arb_printn(h, 5, 0); flint_printf(" rad="); mag_printd(arb_radref(h), 3);
                flint_printf(" h'(s0)="); arb_printn(d, 5, 0); flint_printf(" rad="); mag_printd(arb_radref(d), 3);
                flint_printf(" rad(xi_0)="); mag_printd(arb_radref(xi + 0), 3); flint_printf("\n");
                arb_clear(h); arb_clear(d);
            }
        }
    }
    /* sort, and demand pairwise disjoint enclosures (distinct roots) */
    for (j = 1; j < found; j++)
    {
        i = j;
        while (i > 0 && arb_lt(roots + i, roots + i - 1)) { arb_swap(roots + i, roots + i - 1); i--; }
    }
    /* overlapping certified balls: either the same root twice or two roots too close to separate.
     * Decide rigorously: if the Newton operator maps the hull of the pair into itself, the hull has
     * exactly one root and one copy is kept; otherwise both are dropped as unresolved. */
    for (j = 1; j < found; j++)
    {
        if (!arb_overlaps(roots + j, roots + j - 1)) continue;
        {
            arb_t H, m, hm, dm, hH, dH, nx; int one = 0;
            arb_init(H); arb_init(m); arb_init(hm); arb_init(dm); arb_init(hH); arb_init(dH); arb_init(nx);
            arb_union(H, roots + j, roots + j - 1, prec);
            P.j = (slong) arf_get_d(arb_midref(H), ARF_RND_DOWN); if (P.j > N) P.j = N; if (P.j < 0) P.j = 0;
            arb_get_mid_arb(m, H);
            sec_raw(hm, dm, m, &P, prec); sec_raw(hH, dH, H, &P, prec);
            if (!arb_contains_zero(dH))
            {
                arb_div(nx, hm, dH, prec); arb_sub(nx, m, nx, prec);
                if (arb_contains(H, nx) && mag_cmp(arb_radref(nx), arb_radref(H)) < 0) one = 1;
            }
            if (one)
            {   /* keep one copy: the intersection, which still contains the root */
                arb_intersection(roots + j - 1, roots + j - 1, roots + j, prec);
                for (i = j; i + 1 < found; i++) arb_swap(roots + i, roots + i + 1);
                found--; j--;
            }
            else
            {
                for (i = j - 1; i + 2 < found; i++) arb_swap(roots + i, roots + i + 2);
                found -= 2; unres += 2; j -= 2; if (j < 0) j = 0;
            }
            arb_clear(H); arb_clear(m); arb_clear(hm); arb_clear(dm); arb_clear(hH); arb_clear(dH); arb_clear(nx);
        }
    }

    if (unresolved) *unresolved = unres;
    arb_clear(s0);
    return found;
}

slong zst_secular_roots(arb_ptr roots, slong maxroots, slong *unresolved,
                        arb_srcptr xi, slong N, slong prec)
{
    slong want = FLINT_MIN(N, maxroots), found = 0, G, ncand, nscan = 0;
    double *sd = flint_malloc(sizeof(double) * (N + 64 * 26 + 2));
    arb_ptr scan_roots = getenv("ZST_DEBUG") ? _arb_vec_init(maxroots) : NULL;
    /* sign scan with increasing grid density, then QR at prec/3, then QR at prec */
    for (G = 16; G <= 64 && found < want; G *= 4)
    {
        ncand = candidates_scan(sd, xi, N, prec, G);
        found = roots_from_candidates(roots, maxroots, unresolved, xi, N, prec, sd, ncand);
        if (getenv("ZST_DEBUG"))
        {
            flint_printf("secular: scan G=%wd: %wd candidates, %wd certified\n", G, ncand, found);
            _arb_vec_set(scan_roots, roots, found); nscan = found;
        }
    }
    if (found < want)
    {
        ncand = candidates_qr(sd, xi, N, prec, FLINT_MAX(256, prec / 2));
        found = roots_from_candidates(roots, maxroots, unresolved, xi, N, prec, sd, ncand);
        if (getenv("ZST_DEBUG")) flint_printf("secular: QR at prec/2: %wd candidates, %wd certified\n", ncand, found);
    }
    if (found < want)
    {
        ncand = candidates_qr(sd, xi, N, prec, prec);
        found = roots_from_candidates(roots, maxroots, unresolved, xi, N, prec, sd, ncand);
    }
    if (scan_roots)
    {
        slong i, k;
        for (i = 0; i < found; i++)
        {
            int seen = 0;
            for (k = 0; k < nscan; k++) if (arb_overlaps(roots + i, scan_roots + k)) { seen = 1; break; }
            if (!seen) { flint_printf("secular: root missed by the scan: "); arb_printn(roots + i, 12, ARB_STR_NO_RADIUS); flint_printf("\n"); }
        }
        _arb_vec_clear(scan_roots, maxroots);
    }
    flint_free(sd);
    return found;
}
