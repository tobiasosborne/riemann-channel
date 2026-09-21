/* The generic explicit-formula data model against the hand-typed zeta builder.
 *
 * G1 (the point of the whole lane): zst_weil_riemann + zst_weil_ab must reproduce zst_riemann_ab to
 * all digits, INCLUDING the identity shift.  The zeta constants w(L), C(L) of src/riemann_ab.c
 * (lines 103-116, from mc2arXiv.tex l.781 and the corrected C(L)) are TYPED; here they are DERIVED
 * from the generic gamma data (Q, d, mu, mult) + conductor by F8/F10, and F12 asserts that the two
 * agree.  A mismatch means either F8-F12 or riemann_ab.c is wrong.
 * Formula sheet: notes/zeta-spectral-triples/ellcurve/astra-review.md, F8, F10, F12, F16, F18.
 *
 * Q3 (review, "Q2-Q5"): the conductor enters the data only as +log C on every a_n (F8), so two
 * otherwise identical data sets with conductors 1 and 389 must give a_n differing by exactly
 * log 389 and identical b_n.  This is an exact algebraic invariance, not an empirical question.
 */
#include <stdio.h>
#include "zst.h"

static int fails = 0;

static void
check_close(const arb_t got, const arb_t want, const arb_t tol, const char *what, slong n)
{
    arb_t r;
    arb_init(r);
    arb_sub(r, got, want, 600);
    arb_abs(r, r);
    if (!arb_lt(r, tol))
    {
        flint_printf("test_weil: %s_%wd mismatch, generic ", what, n);
        arb_printn(got, 30, 0);
        flint_printf(" typed ");
        arb_printn(want, 30, 0);
        flint_printf("\n");
        fails++;
    }
    arb_clear(r);
}

/* G1 at one window. */
static void
test_g1(ulong xui, slong N, slong prec, const arb_t tol)
{
    zst_weil_t W;
    arb_t x;
    arb_ptr a1 = _arb_vec_init(N + 1), b1 = _arb_vec_init(N + 1);
    arb_ptr a2 = _arb_vec_init(N + 1), b2 = _arb_vec_init(N + 1);
    slong n;

    arb_init(x);
    arb_set_ui(x, xui);
    zst_riemann_ab(a1, b1, N, x, xui, prec);          /* typed */
    zst_weil_riemann(&W, x, xui, prec);               /* derived */
    zst_weil_ab(a2, b2, N, &W, prec);
    for (n = 0; n <= N; n++)
    {
        check_close(a2 + n, a1 + n, tol, "a", n);
        check_close(b2 + n, b1 + n, tol, "b", n);
    }
    if (!arb_is_zero(b2 + 0)) { flint_printf("test_weil: b_0 not exactly zero\n"); fails++; }

    zst_weil_clear(&W);
    _arb_vec_clear(a1, N + 1); _arb_vec_clear(b1, N + 1);
    _arb_vec_clear(a2, N + 1); _arb_vec_clear(b2, N + 1);
    arb_clear(x);
}

/* Q3: conductor 1 vs 389, everything else identical. */
static void
test_conductor_invariance(slong prec, const arb_t tol)
{
    zst_weil_t W1, W2;
    arb_t x, l389, r;
    slong N = 6, n;
    arb_ptr a1 = _arb_vec_init(N + 1), b1 = _arb_vec_init(N + 1);
    arb_ptr a2 = _arb_vec_init(N + 1), b2 = _arb_vec_init(N + 1);

    arb_init(x); arb_init(l389); arb_init(r);
    arb_set_ui(x, 13);
    zst_weil_riemann(&W1, x, 13, prec);
    zst_weil_riemann(&W2, x, 13, prec);
    fmpz_set_ui(W2.cond, 389);
    zst_weil_ab(a1, b1, N, &W1, prec);
    zst_weil_ab(a2, b2, N, &W2, prec);
    arb_log_ui(l389, 389, prec);
    for (n = 0; n <= N; n++)
    {
        arb_sub(r, a2 + n, a1 + n, prec);
        check_close(r, l389, tol, "cond-shift a", n);
        check_close(b2 + n, b1 + n, tol, "cond-invariant b", n);
    }

    zst_weil_clear(&W1); zst_weil_clear(&W2);
    _arb_vec_clear(a1, N + 1); _arb_vec_clear(b1, N + 1);
    _arb_vec_clear(a2, N + 1); _arb_vec_clear(b2, N + 1);
    arb_clear(x); arb_clear(l389); arb_clear(r);
}

/* shift_extra is an unconditional translation of every a_n as well (Q3 in its second form). */
static void
test_shift_extra(slong prec, const arb_t tol)
{
    zst_weil_t W1, W2;
    arb_t x, c, r;
    slong N = 4, n;
    arb_ptr a1 = _arb_vec_init(N + 1), b1 = _arb_vec_init(N + 1);
    arb_ptr a2 = _arb_vec_init(N + 1), b2 = _arb_vec_init(N + 1);

    arb_init(x); arb_init(c); arb_init(r);
    arb_set_ui(x, 9);
    arb_set_str(c, "-2.75", prec);
    zst_weil_riemann(&W1, x, 9, prec);
    zst_weil_riemann(&W2, x, 9, prec);
    arb_set(W2.shift_extra, c);
    zst_weil_ab(a1, b1, N, &W1, prec);
    zst_weil_ab(a2, b2, N, &W2, prec);
    for (n = 0; n <= N; n++)
    {
        arb_sub(r, a2 + n, a1 + n, prec);
        check_close(r, c, tol, "shift_extra a", n);
        check_close(b2 + n, b1 + n, tol, "shift_extra b", n);
    }

    zst_weil_clear(&W1); zst_weil_clear(&W2);
    _arb_vec_clear(a1, N + 1); _arb_vec_clear(b1, N + 1);
    _arb_vec_clear(a2, N + 1); _arb_vec_clear(b2, N + 1);
    arb_clear(x); arb_clear(c); arb_clear(r);
}

int main(void)
{
    slong prec = 400;
    arb_t tol;
    arb_init(tol);
    arb_set_str(tol, "1e-40", prec);

    test_g1(9, 8, prec, tol);
    test_g1(13, 40, prec, tol);
    test_conductor_invariance(prec, tol);
    test_shift_extra(prec, tol);

    arb_clear(tol);
    flint_cleanup();
    flint_printf("test_weil: %s\n", fails ? "FAIL" : "PASS");
    return fails ? 1 : 0;
}
