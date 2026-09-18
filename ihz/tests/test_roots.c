/* Pinned closed-form tests for circle_roots.c, unitary.c, prony.c, compare.c.
 *
 * Ground truth for the pinned numbers:
 *   notes/zeta-spectral-triples/ihara/plan.md:388-406 (4.4, pinned closed forms: K_4 with
 *     mu^2 + mu + 2 = 0, R = 2, critical K = 3; Petersen R = 4 with multiplicities 5,5,4,4)
 *   notes/zeta-spectral-triples/ihara/lanes/theory.md:503-516 (IH-18 verified values: Petersen
 *     eps_M = 15.8787, 9.4477, 5.7124, 0, ... for K = 2,3,4,5,...; at K = 5 the roots of Ptilde
 *     are exp(+-3 pi i/4) and (1 +- i sqrt 7)/(2 sqrt 2), i.e. exactly the four retained points)
 *   notes/zeta-spectral-triples/ihara/lanes/theory.md:517-536 (IH-20: Prony weights (5,5,4,4))
 *   notes/zeta-spectral-triples/ihara/lanes/theory.md:297-320 (IH-11 (ii),(iii))
 *   include/ihz.h:14, 21-28, 33, 140-168 (conventions and the APIs under test)
 *
 * Every case is built by hand from exact algebraic numbers in arb, and the three closed forms
 * that are not one-liners (the two Petersen angles and the under-resolved eps and xi) are also
 * pinned against 40-digit decimals computed independently with mpmath.
 *
 * Case 1  K_4 at the critical window Mp = 1, K = 3.  q = 2, r = sqrt 2, retained points
 *         mu = (-1 +- i sqrt 7)/2 with multiplicity 3, w = mu/r, cos theta = -1/(2 sqrt 2).
 *         Kernel polynomial w^2 + (1/sqrt 2) w + 1  ->  xi = (1, 1/sqrt 2, 1).
 *         t_k = 6 cos(k theta): t = (6, -3/sqrt 2, -9/2).
 * Case 2  Petersen at Mp = 2, K = 5.  Retained (1 +- i sqrt 7)/2 (mult 5), -1 +- i (mult 4);
 *         theta_1 = arccos(1/(2 sqrt 2)), theta_2 = 3 pi/4; the kernel polynomial
 *         (w^2 - 2cos th1 w + 1)(w^2 - 2cos th2 w + 1) = w^4 + (1/sqrt2) w^3 + w^2 + (1/sqrt2) w + 1
 *         -> xi = (1, 1/sqrt 2, 1, 1/sqrt 2, 1); t_k = 10 cos(k th1) + 8 cos(k th2)
 *         = (18, -3/sqrt 2, -15/2, -9 sqrt 2/4, -27/4).
 * Case 3  Petersen at Mp = 1, K = 3 (under-resolved).  t = (18, -3/sqrt 2, -15/2); the even
 *         block is E = [[18, -3], [-3, 21/2]] exactly, so eps = (57 - sqrt 369)/4 and the
 *         minimal eigenvector maps to xi = (1, 12 sqrt 2/(15 + sqrt 369), 1) after xi[0] = 1.
 */
#include <string.h>
#include <flint/arb.h>
#include <flint/acb.h>
#include <flint/arb_mat.h>
#include <flint/acb_mat.h>
#include "ihz.h"

static int nfail = 0;

static void
check(int ok, const char *name)
{
    flint_printf("%s %s\n", ok ? "PASS" : "FAIL", name);
    if (!ok) nfail++;
}

/* rad(x) < 2^e */
static int
rad_lt_2exp(const arb_t x, slong e)
{
    mag_t m;
    int r;
    mag_init(m);
    mag_set_ui_2exp_si(m, 1, e);
    r = (mag_cmp(arb_radref(x), m) < 0);
    mag_clear(m);
    return r;
}

/* |x - y| < 2^e, for a decimal pin against an exact construction */
static int
close_2exp(const arb_t x, const arb_t y, slong e, slong prec)
{
    arb_t d, b;
    int r;
    arb_init(d); arb_init(b);
    arb_sub(d, x, y, prec);
    arb_abs(d, d);
    arb_one(b);
    arb_mul_2exp_si(b, b, e);
    r = arb_lt(d, b);
    arb_clear(d); arb_clear(b);
    return r;
}

static void
mk_toeplitz(arb_mat_t T, arb_srcptr t, slong K)
{
    slong i, j;
    for (i = 0; i < K; i++)
        for (j = 0; j < K; j++)
            arb_set(arb_mat_entry(T, i, j), t + FLINT_ABS(i - j));
}

/* alpha contains the integer m (real part) and 0 (imaginary part) */
static int
alpha_is(const acb_t a, slong m)
{
    return arb_contains_si(acb_realref(a), m) && arb_contains_zero(acb_imagref(a));
}

/* ------------------------------------------------------------------ case 1: K_4, Mp = 1 */
static void
case_K4(slong prec)
{
    slong Mp = 1, K = 3, n, unres = 0, i;
    arb_ptr xi = _arb_vec_init(K), t = _arb_vec_init(K), theta = _arb_vec_init(8), err;
    arb_t sq2, th_exact, eps, tmp;
    arb_mat_t T, U;
    acb_ptr mu = _acb_vec_init(2), alpha = _acb_vec_init(2);
    acb_t w;
    ihz_weil_t W;
    ihz_spectrum_t S;
    slong mult[2] = { 3, 3 };

    arb_init(sq2); arb_init(th_exact); arb_init(eps); arb_init(tmp);
    arb_sqrt_ui(sq2, 2, prec);

    /* xi = (1, 1/sqrt2, 1) in the full/position indexing (Mp = 1 so they agree) */
    arb_one(xi + 0);
    arb_inv(xi + 1, sq2, prec);
    arb_one(xi + 2);

    /* theta = arccos(-1/(2 sqrt 2)) */
    arb_mul_2exp_si(tmp, sq2, 1);
    arb_inv(tmp, tmp, prec);
    arb_neg(tmp, tmp);
    arb_acos(th_exact, tmp, prec);

    n = ihz_circle_roots(theta, 8, &unres, xi, Mp, prec);
    check(n == 1, "K4 Mp=1: one root on [0,pi]");
    check(unres == 0, "K4 Mp=1: unresolved == 0");
    if (n == 1)
    {
        check(arb_overlaps(theta + 0, th_exact), "K4 Mp=1: root == arccos(-1/(2 sqrt2))");
        check(rad_lt_2exp(theta + 0, -100), "K4 Mp=1: root radius < 1e-30");
        flint_printf("     theta = "); arb_printn(theta + 0, 30, 0); flint_printf("\n");
    }
    else { check(0, "K4 Mp=1: root == arccos(-1/(2 sqrt2))"); check(0, "K4 Mp=1: root radius < 1e-30"); }

    /* t = (6, -3/sqrt2, -9/2), T the 3x3 Toeplitz, eps = 0 */
    arb_set_si(t + 0, 6);
    arb_set_si(t + 1, -3); arb_div(t + 1, t + 1, sq2, prec);
    arb_set_si(t + 2, -9); arb_div_si(t + 2, t + 2, 2, prec);
    arb_mat_init(T, K, K); mk_toeplitz(T, t, K);
    arb_mat_init(U, K, K);
    ihz_unitary_build(U, xi, K, prec);
    arb_zero(eps);
    check(ihz_unitary_check(U, T, eps, prec) == 1, "K4 Mp=1: U^T (T-eps) U == T-eps at eps=0");

    acb_init(w);
    acb_set_d_d(w, 0.3, 0.4);
    check(ihz_unitary_det_check(U, xi, K, w, prec) == 1, "K4 Mp=1: det(U-w) == -w(-1)^{K+1} Ptilde(w)");

    /* mu = (-1 +- i sqrt7)/2 */
    arb_sqrt_ui(tmp, 7, prec);
    acb_set_si(mu + 0, -1); acb_div_si(mu + 0, mu + 0, 2, prec);
    arb_mul_2exp_si(acb_imagref(mu + 0), tmp, -1);
    acb_conj(mu + 1, mu + 0);

    memset(&W, 0, sizeof(W));
    W.M = Mp; W.q = 2; W.sign = 1; W.t = t;
    ihz_prony_weights(alpha, &W, mu, 2, prec);
    check(alpha_is(alpha + 0, 3) && alpha_is(alpha + 1, 3), "K4 Mp=1: Prony weights contain (3,3)");
    flint_printf("     alpha = "); acb_printn(alpha + 0, 20, 0);
    flint_printf("  "); acb_printn(alpha + 1, 20, 0); flint_printf("\n");

    memset(&S, 0, sizeof(S));
    S.R = 2; S.mu = mu; S.mult = mult;
    err = _arb_vec_init(2);
    ihz_compare(err, theta, n, &S, 2, prec);
    for (i = 0; i < 2; i++)
        check(arb_contains_zero(err + i) && rad_lt_2exp(err + i, -84),
              i == 0 ? "K4 Mp=1: compare err[0] contains 0, radius < 1e-25"
                     : "K4 Mp=1: compare err[1] contains 0, radius < 1e-25");

    _arb_vec_clear(err, 2);
    _arb_vec_clear(xi, K); _arb_vec_clear(t, K); _arb_vec_clear(theta, 8);
    _acb_vec_clear(mu, 2); _acb_vec_clear(alpha, 2);
    arb_mat_clear(T); arb_mat_clear(U);
    arb_clear(sq2); arb_clear(th_exact); arb_clear(eps); arb_clear(tmp); acb_clear(w);
}

/* ------------------------------------------------------- case 2: Petersen, Mp = 2 (critical) */
static void
case_petersen5(slong prec)
{
    slong Mp = 2, K = 5, n, unres = 0, i;
    arb_ptr xi = _arb_vec_init(K), t = _arb_vec_init(K), theta = _arb_vec_init(8), err;
    arb_t sq2, th1, th2, eps, tmp, pin;
    arb_mat_t T, U;
    acb_ptr mu = _acb_vec_init(4), alpha = _acb_vec_init(4);
    acb_t w;
    ihz_weil_t W;
    ihz_spectrum_t S;
    slong mult[4] = { 5, 5, 4, 4 };
    static const slong want[4] = { 5, 5, 4, 4 };

    arb_init(sq2); arb_init(th1); arb_init(th2); arb_init(eps); arb_init(tmp); arb_init(pin);
    arb_sqrt_ui(sq2, 2, prec);

    /* xi = (1, 1/sqrt2, 1, 1/sqrt2, 1) */
    arb_one(xi + 0); arb_one(xi + 2); arb_one(xi + 4);
    arb_inv(xi + 1, sq2, prec); arb_set(xi + 3, xi + 1);

    arb_mul_2exp_si(tmp, sq2, 1); arb_inv(tmp, tmp, prec);
    arb_acos(th1, tmp, prec);                        /* arccos(1/(2 sqrt2)) */
    arb_const_pi(th2, prec);
    arb_mul_si(th2, th2, 3, prec); arb_div_si(th2, th2, 4, prec);   /* 3 pi/4 */

    arb_set_str(pin, "1.209429202888188813642133015319084761086", prec);
    check(close_2exp(th1, pin, -110, prec), "Petersen K=5: theta_1 pin (40 digits)");
    arb_set_str(pin, "2.356194490192344928846982537459627163148", prec);
    check(close_2exp(th2, pin, -110, prec), "Petersen K=5: theta_2 pin (40 digits)");

    n = ihz_circle_roots(theta, 8, &unres, xi, Mp, prec);
    check(n == 2, "Petersen K=5: two roots on [0,pi]");
    check(unres == 0, "Petersen K=5: unresolved == 0");
    if (n == 2)
    {
        check(arb_overlaps(theta + 0, th1) && rad_lt_2exp(theta + 0, -100), "Petersen K=5: root 1 == theta_1, radius < 1e-30");
        check(arb_overlaps(theta + 1, th2) && rad_lt_2exp(theta + 1, -100), "Petersen K=5: root 2 == theta_2, radius < 1e-30");
        flint_printf("     theta_1 = "); arb_printn(theta + 0, 30, 0); flint_printf("\n");
        flint_printf("     theta_2 = "); arb_printn(theta + 1, 30, 0); flint_printf("\n");
    }
    else { check(0, "Petersen K=5: root 1 == theta_1, radius < 1e-30"); check(0, "Petersen K=5: root 2 == theta_2, radius < 1e-30"); }

    /* t = (18, -3/sqrt2, -15/2, -9 sqrt2/4, -27/4) */
    arb_set_si(t + 0, 18);
    arb_set_si(t + 1, -3); arb_div(t + 1, t + 1, sq2, prec);
    arb_set_si(t + 2, -15); arb_div_si(t + 2, t + 2, 2, prec);
    arb_mul_si(t + 3, sq2, -9, prec); arb_div_si(t + 3, t + 3, 4, prec);
    arb_set_si(t + 4, -27); arb_div_si(t + 4, t + 4, 4, prec);

    arb_mat_init(T, K, K); mk_toeplitz(T, t, K);
    arb_mat_init(U, K, K); ihz_unitary_build(U, xi, K, prec);
    arb_zero(eps);
    check(ihz_unitary_check(U, T, eps, prec) == 1, "Petersen K=5: U^T (T-eps) U == T-eps at eps=0");

    acb_init(w); acb_set_d_d(w, 0.3, 0.4);
    check(ihz_unitary_det_check(U, xi, K, w, prec) == 1, "Petersen K=5: det(U-w) == -w(-1)^{K+1} Ptilde(w)");

    /* mu = (1 +- i sqrt7)/2 (mult 5), -1 +- i (mult 4) */
    arb_sqrt_ui(tmp, 7, prec);
    acb_one(mu + 0); acb_div_si(mu + 0, mu + 0, 2, prec);
    arb_mul_2exp_si(acb_imagref(mu + 0), tmp, -1);
    acb_conj(mu + 1, mu + 0);
    acb_set_si_si(mu + 2, -1, 1);
    acb_conj(mu + 3, mu + 2);

    memset(&W, 0, sizeof(W));
    W.M = Mp; W.q = 2; W.sign = 1; W.t = t;
    ihz_prony_weights(alpha, &W, mu, 4, prec);
    {
        int ok = 1;
        for (i = 0; i < 4; i++) if (!alpha_is(alpha + i, want[i])) ok = 0;
        check(ok, "Petersen K=5: Prony weights contain (5,5,4,4)");
        flint_printf("     alpha =");
        for (i = 0; i < 4; i++) { flint_printf(" "); acb_printn(alpha + i, 15, 0); }
        flint_printf("\n");
    }

    memset(&S, 0, sizeof(S));
    S.R = 4; S.mu = mu; S.mult = mult;
    err = _arb_vec_init(4);
    ihz_compare(err, theta, n, &S, 2, prec);
    {
        int ok = 1;
        for (i = 0; i < 4; i++) if (!(arb_contains_zero(err + i) && rad_lt_2exp(err + i, -84))) ok = 0;
        check(ok, "Petersen K=5: all four compare errors contain 0, radius < 1e-25");
    }

    _arb_vec_clear(err, 4);
    _arb_vec_clear(xi, K); _arb_vec_clear(t, K); _arb_vec_clear(theta, 8);
    _acb_vec_clear(mu, 4); _acb_vec_clear(alpha, 4);
    arb_mat_clear(T); arb_mat_clear(U);
    arb_clear(sq2); arb_clear(th1); arb_clear(th2); arb_clear(eps); arb_clear(tmp); arb_clear(pin);
    acb_clear(w);
}

/* ------------------------------------------- case 3: Petersen, Mp = 1 (under-resolved, eps > 0) */
static void
case_petersen3(slong prec)
{
    slong Mp = 1, K = 3, n, unres = 0;
    arb_ptr xi = _arb_vec_init(K), t = _arb_vec_init(K), theta = _arb_vec_init(8);
    arb_t sq2, s369, eps, x0, th_exact, tmp, pin;
    arb_mat_t T, U;

    arb_init(sq2); arb_init(s369); arb_init(eps); arb_init(x0);
    arb_init(th_exact); arb_init(tmp); arb_init(pin);
    arb_sqrt_ui(sq2, 2, prec);
    arb_sqrt_ui(s369, 369, prec);

    /* t = (18, -3/sqrt2, -15/2); even block E = [[t0, sqrt2 t1],[sqrt2 t1, t0+t2]] = [[18,-3],[-3,21/2]] */
    arb_set_si(t + 0, 18);
    arb_set_si(t + 1, -3); arb_div(t + 1, t + 1, sq2, prec);
    arb_set_si(t + 2, -15); arb_div_si(t + 2, t + 2, 2, prec);

    /* eps = (57 - sqrt 369)/4 */
    arb_set_si(eps, 57); arb_sub(eps, eps, s369, prec); arb_div_si(eps, eps, 4, prec);
    arb_set_str(pin, "9.447656821925363485133836744033640051610", prec);
    check(close_2exp(eps, pin, -110, prec), "Petersen K=3: eps = (57-sqrt369)/4 pin (40 digits)");
    flint_printf("     eps = "); arb_printn(eps, 30, 0); flint_printf("\n");

    /* minimal eigenvector c = (1, (15+sqrt369)/12); xi_0 = c_0, xi_{+-1} = c_1/sqrt2;
     * normalised to xi[0] = 1 the position vector is (1, 12 sqrt2/(15+sqrt369), 1) */
    arb_set_si(x0, 15); arb_add(x0, x0, s369, prec);
    arb_mul_si(tmp, sq2, 12, prec);
    arb_div(x0, tmp, x0, prec);
    arb_set_str(pin, "0.4960793315679853456413411364838940050509", prec);
    check(close_2exp(x0, pin, -110, prec), "Petersen K=3: normalised xi_0 pin (40 digits)");
    arb_one(xi + 0); arb_set(xi + 1, x0); arb_one(xi + 2);

    arb_mat_init(T, K, K); mk_toeplitz(T, t, K);
    arb_mat_init(U, K, K); ihz_unitary_build(U, xi, K, prec);
    check(ihz_unitary_check(U, T, eps, prec) == 1, "Petersen K=3: U^T (T-eps) U == T-eps at eps>0");

    /* R(theta) = xi_0 + 2 cos theta, root arccos(-xi_0/2) */
    arb_mul_2exp_si(tmp, x0, -1); arb_neg(tmp, tmp);
    arb_acos(th_exact, tmp, prec);
    arb_set_str(pin, "1.821452484998607076976109431370418156936", prec);
    check(close_2exp(th_exact, pin, -110, prec), "Petersen K=3: root angle pin (40 digits)");

    n = ihz_circle_roots(theta, 8, &unres, xi, Mp, prec);
    check(n == 1, "Petersen K=3: one root on [0,pi]");
    check(unres == 0, "Petersen K=3: unresolved == 0");
    if (n == 1)
    {
        check(arb_overlaps(theta + 0, th_exact) && rad_lt_2exp(theta + 0, -100),
              "Petersen K=3: root == arccos(-xi_0/2), radius < 1e-30");
        flint_printf("     theta = "); arb_printn(theta + 0, 30, 0); flint_printf("\n");
    }
    else check(0, "Petersen K=3: root == arccos(-xi_0/2), radius < 1e-30");

    _arb_vec_clear(xi, K); _arb_vec_clear(t, K); _arb_vec_clear(theta, 8);
    arb_mat_clear(T); arb_mat_clear(U);
    arb_clear(sq2); arb_clear(s369); arb_clear(eps); arb_clear(x0);
    arb_clear(th_exact); arb_clear(tmp); arb_clear(pin);
}

int
main(void)
{
    slong prec = 256;
    flint_printf("ihz test_roots (prec = %wd)\n", prec);
    flint_printf("-- case 1: K_4, Mp = 1 (critical window, K = 3)\n");
    case_K4(prec);
    flint_printf("-- case 2: Petersen, Mp = 2 (critical window, K = 5)\n");
    case_petersen5(prec);
    flint_printf("-- case 3: Petersen, Mp = 1 (under-resolved, K = 3)\n");
    case_petersen3(prec);
    flint_printf("%s: %wd failure(s)\n", nfail ? "FAILURES" : "ALL PASS", (slong) nfail);
    flint_cleanup();
    return nfail != 0;
}
