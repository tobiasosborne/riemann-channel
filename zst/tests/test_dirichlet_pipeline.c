/* End-to-end acceptance for a real primitive Dirichlet character (MVP-3 goal G2', the review's
 * recommendation 1: "put the real primitive Dirichlet character first as the implementation
 * control" -- degree one, no point counting, no pole term, an independent gamma factor
 * Gamma_R(s + kappa), and PARI ground truth).
 *
 * Object: chi_{-4}, the odd real primitive character of conductor 4 (kappa = 1, kernel (d, mu) =
 * (2, 3/2), Q = pi^{-1/2}: F6 of notes/zeta-spectral-triples/ellcurve/astra-review.md).
 * Reference zeros: tests/data/dirichlet_ref.txt (PARI 2.17.2 lfunzeros with an explicit `precision`
 * argument, the review's "reference precision accidentally stuck at 64 bits" correction);
 * gamma_1 = 6.0209489046975966549025115216120858688640.
 *
 * Tolerance: MEASURED first, then pinned with a margin. ./build/zst --chi -4 --x 13 --N 40 gives
 * |z_1 - gamma_1| = 1.898e-12, identical at 400, 500 and 700 bits (it is the model's approximation
 * error, not an interval width), so the bracket is [1e-13, 5e-12]; the lower bound makes the test
 * fail if the pipeline is silently computing a different -- more accurate -- object. */
#include <stdio.h>
#include "zst.h"

static int fails = 0;
#define CHECK(cond, msg) do { if (!(cond)) { flint_printf("FAIL: %s\n", msg); fails++; } } while (0)

int main(void)
{
    slong N = 40, prec = 500, dim = N + 1, nroots, unres, k;
    double xd = 13.0;
    zst_weil_t W;
    arb_mat_t E, O;
    arb_t x, L, minE, minO, gap, lam, twopiL, t, u, sum, lo, hi;
    arb_ptr a, b, v, xi, roots;
    fmpz_t D;
    int par, es;

    arb_mat_init(E, dim, dim); arb_mat_init(O, N, N);
    arb_init(x); arb_init(L); arb_init(minE); arb_init(minO); arb_init(gap); arb_init(lam);
    arb_init(twopiL); arb_init(t); arb_init(u); arb_init(sum); arb_init(lo); arb_init(hi);
    a = _arb_vec_init(N + 1); b = _arb_vec_init(N + 1);
    v = _arb_vec_init(dim); xi = _arb_vec_init(N + 1); roots = _arb_vec_init(N);
    fmpz_init(D); fmpz_set_si(D, -4);

    arb_set_d(x, xd);
    zst_weil_dirichlet(&W, D, x, (ulong) (xd + 1e-9), prec);
    arb_set(L, W.L);
    zst_weil_ab(a, b, N, &W, prec);
    zst_even_block(E, a, b, N, prec);
    zst_odd_block(O, a, b, N, prec);
    zst_weil_clear(&W);

    par = zst_parity(minE, minO, gap, E, O, 40, prec);
    CHECK(par == 1, "chi_-4 x=13 N=40: parity +1 (even minimum) certified");
    CHECK(arb_is_positive(minE), "chi_-4: min E > 0 certified (Weil positivity, Q4)");
    CHECK(arb_lt(minE, minO), "chi_-4: min E < min O certified");

    CHECK(zst_block_min(lam, v, E, 40, prec) == 1, "chi_-4: even minimiser certified");
    es = zst_certify_even_simple(E, O, lam, v, prec);
    CHECK(es == 1, "chi_-4: even-simple hypothesis CERTIFIED");

    arb_set(xi + 0, v + 0);
    arb_sqrt_ui(t, 2, prec);
    for (k = 1; k <= N; k++) arb_div(xi + k, v + k, t, prec);
    arb_set(sum, xi + 0);
    for (k = 1; k <= N; k++) { arb_mul_2exp_si(u, xi + k, 1); arb_add(sum, sum, u, prec); }
    for (k = 0; k <= N; k++) arb_div(xi + k, xi + k, sum, prec);
    CHECK(arb_is_positive(xi + 0), "chi_-4: xi_0 > 0 certified (D'' invertible)");

    nroots = zst_secular_roots(roots, N, &unres, xi, N, prec);
    CHECK(nroots == N && unres == 0, "chi_-4: all N positive secular roots certified (2N complete)");

    arb_const_pi(twopiL, prec); arb_mul_2exp_si(twopiL, twopiL, 1); arb_div(twopiL, twopiL, L, prec);
    arb_mul(t, roots + 0, twopiL, prec);
    arb_set_str(u, "6.0209489046975966549025115216120858688640", prec);
    arb_sub(t, t, u, prec); arb_abs(t, t);
    arb_set_str(lo, "1e-13", prec); arb_set_str(hi, "5e-12", prec);
    if (!arb_lt(t, hi))
    { flint_printf("FAIL: chi_-4 |z_1 - gamma_1| < 5e-12; got "); arb_printn(t, 8, 0); flint_printf("\n"); fails++; }
    if (!arb_gt(t, lo))
    { flint_printf("FAIL: chi_-4 |z_1 - gamma_1| > 1e-13 (measured 1.898e-12); got ");
      arb_printn(t, 8, 0); flint_printf("\n"); fails++; }

    arb_mat_clear(E); arb_mat_clear(O);
    arb_clear(x); arb_clear(L); arb_clear(minE); arb_clear(minO); arb_clear(gap); arb_clear(lam);
    arb_clear(twopiL); arb_clear(t); arb_clear(u); arb_clear(sum); arb_clear(lo); arb_clear(hi);
    _arb_vec_clear(a, N + 1); _arb_vec_clear(b, N + 1);
    _arb_vec_clear(v, dim); _arb_vec_clear(xi, N + 1); _arb_vec_clear(roots, N);
    fmpz_clear(D);
    flint_cleanup();
    flint_printf("test_dirichlet_pipeline: %s\n", fails ? "FAIL" : "PASS");
    return fails ? 1 : 0;
}
