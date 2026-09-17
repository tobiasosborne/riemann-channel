/* Unit tests for the secular-root module, written before the QR + Newton implementation (red first).
 * Ground truth is closed-form algebra, not the paper: for N = 1 with xi_0 = a, xi_1 = xi_{-1} = b,
 * a + 2b = 1, g(s) = -a/s + 2bs/(1 - s^2) vanishes iff s^2 = a/(a + 2b) = a, so the unique positive
 * root is sqrt(a). With a = 1/4, b = 3/8 the root is exactly 1/2. */
#include <stdio.h>
#include "zst.h"

static int fails = 0;
#define CHECK(cond, msg) do { if (!(cond)) { flint_printf("FAIL: %s\n", msg); fails++; } } while (0)

static void test_closed_form(void)
{
    slong prec = 200, n, unres;
    arb_ptr xi = _arb_vec_init(2), roots = _arb_vec_init(1);
    arb_t half, val, der, s;
    arb_init(half); arb_init(val); arb_init(der); arb_init(s);
    arb_set_d(xi + 0, 0.25); arb_set_d(xi + 1, 0.375);
    arb_set_d(half, 0.5);
    n = zst_secular_roots(roots, 1, &unres, xi, 1, prec);
    CHECK(n == 1, "N=1: one positive root");
    CHECK(unres == 0, "N=1: nothing unresolved");
    CHECK(n == 1 && arb_contains(roots + 0, half), "N=1: root ball contains 1/2");
    CHECK(n == 1 && mag_cmp_2exp_si(arb_radref(roots + 0), -150) < 0, "N=1: root certified to 150 bits");
    /* h_0(s) = g(s)(0 - s)(1 - s) at s = 1/2 vanishes; derivative g'(1/2) (1/2)(-1/2)... just nonzero */
    zst_secular_eval(val, der, half, xi, 1, 0, prec);
    CHECK(arb_contains_zero(val), "h_0(1/2) contains zero");
    CHECK(!arb_contains_zero(der), "h_0'(1/2) is nonzero");
    /* h_0(s) = -a(1-s) - b s ... at s = 1/4: g = -1 + 2(3/8)(1/4)/(15/16) = -1 + 0.2 = -0.8,
       P = (-1/4)(3/4) = -3/16, h = 0.15 */
    arb_set_d(s, 0.25);
    zst_secular_eval(val, der, s, xi, 1, 0, prec);
    arb_set_str(half, "0.15", prec);
    CHECK(arb_overlaps(val, half), "h_0(1/4) = 0.15");
    _arb_vec_clear(xi, 2); _arb_vec_clear(roots, 1);
    arb_clear(half); arb_clear(val); arb_clear(der); arb_clear(s);
}

static void test_count_and_roots_are_roots(void)
{
    /* N = 5, positive xi: g(s) = sum_k xi_k/(k - s) is then increasing between consecutive poles,
     * so there is exactly one root in each of (0,1), ..., (N-1,N) and none beyond N: the list must be
     * complete (N roots), every root a certified zero of h_j, and the roots disjoint. (For sign-
     * changing xi the roots need not be real; only the paper's even-simple matrices guarantee it.) */
    slong prec = 256, N = 5, n, unres, k;
    arb_ptr xi = _arb_vec_init(N + 1), roots = _arb_vec_init(N);
    arb_t sum, val, der;
    double raw[6] = {2.0, 0.7, 0.31, 0.05, 0.004, 0.0002};
    arb_init(sum); arb_init(val); arb_init(der);
    for (k = 0; k <= N; k++) arb_set_d(xi + k, raw[k]);
    arb_set(sum, xi + 0);
    for (k = 1; k <= N; k++) { arb_add(sum, sum, xi + k, prec); arb_add(sum, sum, xi + k, prec); }
    for (k = 0; k <= N; k++) arb_div(xi + k, xi + k, sum, prec);
    n = zst_secular_roots(roots, N, &unres, xi, N, prec);
    CHECK(n == N, "N=5: complete list of positive roots");
    for (k = 0; k < n; k++)
    {
        slong j = (slong) arf_get_d(arb_midref(roots + k), ARF_RND_DOWN);
        if (j > N) j = N;
        zst_secular_eval(val, der, roots + k, xi, N, j, prec);
        CHECK(arb_contains_zero(val), "N=5: root is a zero of h_j");
        CHECK(j == k, "N=5: exactly one root per pole interval");
        if (k) CHECK(arb_lt(roots + k - 1, roots + k), "N=5: roots increasing and disjoint");
    }
    _arb_vec_clear(xi, N + 1); _arb_vec_clear(roots, N);
    arb_clear(sum); arb_clear(val); arb_clear(der);
}

static void test_root_beyond_last_pole(void)
{
    /* N = 1, xi_0 = 4, xi_1 = -3/2 (sum = 1): the positive root is sqrt(4) = 2, beyond the last pole
     * at s = N = 1, so it exercises the h_N(s) = g(s)(N - s) branch. Added to kill the mutant that
     * treated j = N like j < N (survived tools/mutate.py, seed 1). */
    slong prec = 200, n, unres;
    arb_ptr xi = _arb_vec_init(2), roots = _arb_vec_init(1);
    arb_t two, val, der;
    arb_init(two); arb_init(val); arb_init(der);
    arb_set_si(xi + 0, 4); arb_set_d(xi + 1, -1.5);
    arb_set_si(two, 2);
    n = zst_secular_roots(roots, 1, &unres, xi, 1, prec);
    CHECK(n == 1, "beyond pole: one positive root");
    CHECK(n == 1 && arb_contains(roots + 0, two), "beyond pole: root ball contains 2");
    zst_secular_eval(val, der, two, xi, 1, 1, prec);
    CHECK(arb_contains_zero(val), "beyond pole: h_1(2) contains zero");
    /* g(3) = xi_1/(-1-3) + xi_0/(-3) + xi_1/(1-3) = 3/8 - 4/3 + 3/4 = -5/24, h_1(3) = (1-3) g(3) = 5/12 */
    arb_set_si(two, 3);
    zst_secular_eval(val, der, two, xi, 1, 1, prec);
    arb_set_si(der, 5); arb_div_si(der, der, 12, prec);
    CHECK(arb_overlaps(val, der), "beyond pole: h_1(3) = 5/12");
    _arb_vec_clear(xi, 2); _arb_vec_clear(roots, 1);
    arb_clear(two); arb_clear(val); arb_clear(der);
}

static void test_verify_from_perturbed_start(void)
{
    /* The certified root must not depend on the accuracy of the start: from 1/2 + 1e-9 (N = 1,
     * xi = (1/4, 3/8)) the Newton verifier must still return a ball containing exactly 1/2, with
     * radius far below the perturbation, and from a start on the wrong side of the pole (1 + 1e-9,
     * j = 1) it must fail rather than certify a wrong ball. Added to kill the survivors that changed
     * the contraction step of the Newton operator (tools/mutate.py, seed 2, secular.c:116). */
    slong prec = 200;
    arb_ptr xi = _arb_vec_init(2);
    arb_t s, root, half;
    arb_init(s); arb_init(root); arb_init(half);
    arb_set_d(xi + 0, 0.25); arb_set_d(xi + 1, 0.375);
    arb_set_d(half, 0.5);
    arb_set_str(s, "0.500000001", prec);
    CHECK(zst_secular_verify(root, xi, 1, s, prec) == 1, "perturbed start: verified");
    CHECK(arb_contains(root, half), "perturbed start: contains 1/2");
    CHECK(mag_cmp_2exp_si(arb_radref(root), -120) < 0, "perturbed start: contracted below 2^-120");
    arb_set_str(s, "0.500001", prec);    /* 1e-6, inside the verifier's window (radii up to 2^-16) */
    CHECK(zst_secular_verify(root, xi, 1, s, prec) == 1, "perturbed start 1e-6: verified");
    CHECK(arb_contains(root, half), "perturbed start 1e-6: contains 1/2");
    CHECK(mag_cmp_2exp_si(arb_radref(root), -120) < 0, "perturbed start 1e-6: contracted below 2^-120");
    arb_set_str(s, "0.4999", prec);       /* 1e-4 is outside the window: must fail, not certify */
    CHECK(zst_secular_verify(root, xi, 1, s, prec) == 0, "start 1e-4 away: outside window, not certified");
    arb_set_str(s, "0.9", prec);          /* no root near 0.9 (the only positive root is 1/2) */
    CHECK(zst_secular_verify(root, xi, 1, s, prec) == 0, "no root near 0.9: not certified");
    _arb_vec_clear(xi, 2); arb_clear(s); arb_clear(root); arb_clear(half);
}

int main(void)
{
    test_verify_from_perturbed_start();
    test_closed_form();
    test_count_and_roots_are_roots();
    test_root_beyond_last_pole();
    flint_cleanup();
    flint_printf("test_secular: %s\n", fails ? "FAIL" : "PASS");
    return fails ? 1 : 0;
}
