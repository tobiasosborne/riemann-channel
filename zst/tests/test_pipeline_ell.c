/* End-to-end acceptance for L(E, s), E/Q (MVP-3 goals G2 and G3, as rewritten by the review:
 * notes/zeta-spectral-triples/ellcurve/plan.md, "Review outcome").
 *
 * Ground truth: notes/zeta-spectral-triples/ellcurve/astra-review.md, "Numerical checks and run
 * records" (the mpmath prototype checks/ell_check.py at 90 dps, records under checks/):
 *
 *   11a1 x = 13, N = 60 : min E 7.67659737e-7, min O 1.52285566e-4, even-simple, first recovered
 *                         ordinate 6.363023471933060838 against PARI 6.36261389471308870138602900888,
 *                         error 4.09577220e-4;
 *   37a1 x = 13, N = 60 : min E 0.2035253240, min O 0.01247513401 -> ODD minimum (H-a): the paper's
 *                         construction is inapplicable;
 *   389a1 x = 13, N = 60: min E 3.1638473921, min O 1.6401401182 -> ODD minimum although w = +1.
 *
 * The first-zero test is two-sided on purpose: an upper bound alone would also pass for a silently
 * different object whose zeros happen to be nearer, so the measured 4.0958e-4 is bracketed. The
 * review's recommendation 4 ("rewrite G2 around measured tolerances") is the reason for the margin,
 * and its correction-ledger row "G2 every true zero lies within recovered root balls" is the reason
 * only the first ordinate is pinned: the recovered ball is an enclosure of a spectral value of the
 * finite model, never a bound on the model's own approximation error. */
#include <stdio.h>
#include <flint/fmpz_vec.h>
#include "zst.h"

static int fails = 0;
#define CHECK(cond, msg) do { if (!(cond)) { flint_printf("FAIL: %s\n", msg); fails++; } } while (0)

/* blocks of the truncated Weil form of the curve at the window x (F4/F5/F6/F9/F16 through Lane B) */
static void
curve_blocks(arb_mat_t E, arb_mat_t O, arb_t L, const char *label, double xd, slong N, slong prec)
{
    zst_weil_t W;
    fmpz *ainvs = _fmpz_vec_init(5);
    fmpz_t C;
    arb_t x;
    arb_ptr a = _arb_vec_init(N + 1), b = _arb_vec_init(N + 1), g = _arb_vec_init(1);
    slong rank; int w;

    fmpz_init(C); arb_init(x); arb_set_d(x, xd);
    if (!zst_ell_ref(ainvs, C, &w, &rank, g, 1, label, NULL, prec))
    { flint_printf("FAIL: reference data for %s\n", label); fails++; }
    zst_weil_ellcurve(&W, ainvs, C, x, (ulong) (xd + 1e-9), prec);
    arb_set(L, W.L);
    zst_weil_ab(a, b, N, &W, prec);
    zst_even_block(E, a, b, N, prec);
    zst_odd_block(O, a, b, N, prec);
    zst_weil_clear(&W);
    _arb_vec_clear(a, N + 1); _arb_vec_clear(b, N + 1); _arb_vec_clear(g, 1);
    _fmpz_vec_clear(ainvs, 5); fmpz_clear(C); arb_clear(x);
}

/* certified: lo < ball < hi */
static int
in_range(const arb_t ball, const char *lo, const char *hi, slong prec)
{
    arb_t a, b;
    int ok;
    arb_init(a); arb_init(b);
    arb_set_str(a, lo, prec); arb_set_str(b, hi, prec);
    ok = arb_gt(ball, a) && arb_lt(ball, b);
    arb_clear(a); arb_clear(b);
    return ok;
}

/* G3: a curve whose Weil-form minimum is certified ODD at this window */
static void
test_odd_minimum(const char *label, double xd, slong N, slong prec,
                 const char *eLo, const char *eHi, const char *oLo, const char *oHi)
{
    arb_mat_t E, O;
    arb_t L, minE, minO, gap;
    char msg[160];
    int par;
    arb_mat_init(E, N + 1, N + 1); arb_mat_init(O, N, N);
    arb_init(L); arb_init(minE); arb_init(minO); arb_init(gap);
    curve_blocks(E, O, L, label, xd, N, prec);
    par = zst_parity(minE, minO, gap, E, O, 40, prec);
    flint_sprintf(msg, "%s x=%g N=%wd: parity -1 (odd minimum) certified", label, xd, N);
    CHECK(par == -1, msg);
    flint_sprintf(msg, "%s: min E in [%s, %s]", label, eLo, eHi);
    if (!in_range(minE, eLo, eHi, prec))
    { flint_printf("FAIL: %s  min E = ", msg); arb_printn(minE, 12, 0); flint_printf("\n"); fails++; }
    flint_sprintf(msg, "%s: min O in [%s, %s]", label, oLo, oHi);
    if (!in_range(minO, oLo, oHi, prec))
    { flint_printf("FAIL: %s  min O = ", msg); arb_printn(minO, 12, 0); flint_printf("\n"); fails++; }
    CHECK(arb_is_positive(gap), "odd minimum: certified positive gap");
    arb_mat_clear(E); arb_mat_clear(O);
    arb_clear(L); arb_clear(minE); arb_clear(minO); arb_clear(gap);
}

/* G2: 11a1 at x = 13, N = 60 -- even-simple certified, 2N roots complete, first ordinate pinned */
static void
test_11a1(void)
{
    slong N = 60, prec = 700, dim = N + 1, nroots, unres, k;
    double xd = 13.0;
    arb_mat_t E, O;
    arb_t L, minE, minO, gap, lam, twopiL, t, u, sum, lo, hi;
    arb_ptr v, xi, roots;
    int par, es;

    arb_mat_init(E, dim, dim); arb_mat_init(O, N, N);
    arb_init(L); arb_init(minE); arb_init(minO); arb_init(gap); arb_init(lam);
    arb_init(twopiL); arb_init(t); arb_init(u); arb_init(sum); arb_init(lo); arb_init(hi);
    v = _arb_vec_init(dim); xi = _arb_vec_init(N + 1); roots = _arb_vec_init(N);

    curve_blocks(E, O, L, "11a1", xd, N, prec);
    par = zst_parity(minE, minO, gap, E, O, 40, prec);
    CHECK(par == 1, "11a1 x=13 N=60: parity +1 (even minimum) certified");
    CHECK(in_range(minE, "7.6765e-7", "7.6767e-7", prec), "11a1: min E = 7.67659737e-7");
    CHECK(in_range(minO, "1.52285e-4", "1.52286e-4", prec), "11a1: min O = 1.52285566e-4");

    CHECK(zst_block_min(lam, v, E, 40, prec) == 1, "11a1: even minimiser certified");
    es = zst_certify_even_simple(E, O, lam, v, prec);
    CHECK(es == 1, "11a1: even-simple hypothesis CERTIFIED");

    /* sum-normalised xi; xi_0 > 0 is forced by even-simple (astra-review.md, Q1) */
    arb_set(xi + 0, v + 0);
    arb_sqrt_ui(t, 2, prec);
    for (k = 1; k <= N; k++) arb_div(xi + k, v + k, t, prec);
    arb_set(sum, xi + 0);
    for (k = 1; k <= N; k++) { arb_mul_2exp_si(u, xi + k, 1); arb_add(sum, sum, u, prec); }
    for (k = 0; k <= N; k++) arb_div(xi + k, xi + k, sum, prec);
    CHECK(arb_is_positive(xi + 0), "11a1: xi_0 > 0 certified (D'' invertible)");
    CHECK(in_range(xi + 0, "425.59", "425.60", prec), "11a1: xi_0 = 425.5965725 (prototype pin)");

    nroots = zst_secular_roots(roots, N, &unres, xi, N, prec);
    CHECK(nroots == N && unres == 0, "11a1: all N positive secular roots certified (2N complete)");

    /* first recovered ordinate against PARI 6.36261389471308870138602900887870118712378883... */
    arb_const_pi(twopiL, prec); arb_mul_2exp_si(twopiL, twopiL, 1); arb_div(twopiL, twopiL, L, prec);
    arb_mul(t, roots + 0, twopiL, prec);
    arb_set_str(u, "6.3626138947130887013860290088787011871237", prec);
    arb_sub(t, t, u, prec); arb_abs(t, t);
    arb_set_str(lo, "1e-5", prec); arb_set_str(hi, "5e-4", prec);
    if (!arb_lt(t, hi))
    { flint_printf("FAIL: 11a1 |z_1 - gamma_1| < 5e-4; got "); arb_printn(t, 8, 0); flint_printf("\n"); fails++; }
    if (!arb_gt(t, lo))
    { flint_printf("FAIL: 11a1 |z_1 - gamma_1| > 1e-5 (a different object would be suspiciously close); got ");
      arb_printn(t, 8, 0); flint_printf("\n"); fails++; }

    arb_mat_clear(E); arb_mat_clear(O);
    arb_clear(L); arb_clear(minE); arb_clear(minO); arb_clear(gap); arb_clear(lam);
    arb_clear(twopiL); arb_clear(t); arb_clear(u); arb_clear(sum); arb_clear(lo); arb_clear(hi);
    _arb_vec_clear(v, dim); _arb_vec_clear(xi, N + 1); _arb_vec_clear(roots, N);
}

int main(void)
{
    test_11a1();
    test_odd_minimum("37a1", 13.0, 60, 700, "0.20", "0.21", "0.012", "0.013");
    test_odd_minimum("389a1", 13.0, 60, 700, "3.16", "3.17", "1.64", "1.65");
    flint_cleanup();
    flint_printf("test_pipeline_ell: %s\n", fails ? "FAIL" : "PASS");
    return fails ? 1 : 0;
}
