/* test_toeplitz.c: pinned tests of the window data, the Toeplitz form and its blocks, the exact
 * integer stage (rank, critical window, kernel polynomial) and the ported eigmin, on three objects
 * whose divisor is known in closed form.  Hardcoded counts only: ihz_weil_from_counts, never
 * ihz_weil_from_graph (this test deliberately does not link weil_graph.o).
 *
 * Ground truth for the pinned numbers:
 *   K4         plan.md:88-104 (spec(B) from Ihara-Bass), retained charpoly (x^2+x+2)^3, R = 2.
 *   Petersen   lanes/theory.md:113-118 (IH-3: N_k = 30,0,0,0,0,120,120,0 for k = 0..7),
 *              lanes/theory.md:485-499 (IH-18: R = 4, critical at K = 5),
 *              run_ihara_proto.txt:260-263 (eps_M = 18 at K=1, 9.4476568 at K=3, ~0 at K=5;
 *              eps_odd = 25.5 at K=3).
 *   curve      lanes/numerics.md / the Pauli-qubit elliptic curve over F_5 with a = -1 + 2i:
 *              N_1..N_6 = 8, 32, 104, 640, 3208, 15392, retained divisor {a, abar}, sign = -1.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include "ihz.h"

static int failures = 0, checks = 0;

static void
check(int ok, const char *fmt, ...)
{
    va_list ap;
    checks++;
    if (!ok) failures++;
    printf("[%s] ", ok ? "PASS" : "FAIL");
    va_start(ap, fmt);
    vprintf(fmt, ap);
    va_end(ap);
    printf("\n");
}

/* trace sequence p_k = sum of the two roots^k of x^2 + b x + c: p_0 = 2, p_1 = -b, p_k = -b p_{k-1} - c p_{k-2} */
static void
trace_seq(fmpz *p, slong len, slong b, slong c)
{
    slong k;
    if (len > 0) fmpz_set_si(p + 0, 2);
    if (len > 1) fmpz_set_si(p + 1, -b);
    for (k = 2; k < len; k++)
    {
        fmpz_mul_si(p + k, p + k - 1, -b);
        fmpz_submul_si(p + k, p + k - 2, c);
    }
}

/* |a - b| < 2^-100 and the difference ball contains 0 */
static int
close_ball(const arb_t a, const arb_t b)
{
    arb_t d;
    int ok;
    arb_init(d);
    arb_sub(d, a, b, 300);
    ok = arb_contains_zero(d) && mag_cmp_2exp_si(arb_radref(d), -100) < 0;
    arb_clear(d);
    return ok;
}

/* expected t_k = sign * q^{-k/2} c_k as a ball */
static void
expect_t(arb_t out, const fmpz_t c, slong q, slong k, int sign, slong prec)
{
    arb_t r;
    arb_init(r);
    arb_set_fmpz(out, c);
    if (k > 0)
    {
        arb_sqrt_ui(r, (ulong) q, prec);
        arb_pow_ui(r, r, (ulong) k, prec);
        arb_div(out, out, r, prec);
    }
    if (sign < 0) arb_neg(out, out);
    arb_clear(r);
}

static void
print_poly(const char *lab, const fmpz_poly_t P)
{
    char *s = fmpz_poly_get_str_pretty(P, "x");
    printf("      %s = %s\n", lab, s);
    flint_free(s);
}

static int
poly_eq_si(const fmpz_poly_t P, const slong *co, slong n)
{
    fmpz_poly_t Q;
    int ok;
    slong i;
    fmpz_poly_init(Q);
    for (i = 0; i < n; i++) fmpz_poly_set_coeff_si(Q, i, co[i]);
    ok = fmpz_poly_equal(P, Q);
    fmpz_poly_clear(Q);
    return ok;
}

/* -------------------------------------------------------------------- case 1: K4 */
static void
case_K4(slong prec)
{
    slong M = 3, len = 7, q = 2, k;
    /* trivial divisor {2:1, 1:1, 1:(ne-nv)=2, -1:2}; ne = 6, nv = 4 */
    slong trm[4] = { 1, 1, 2, 2 };
    slong trv[4] = { 2, 1, 1, -1 };
    /* N_k = Tr B^k = 3 p_k + (2^k + 1 + 2(1 + (-1)^k)), p from x^2 + x + 2 */
    slong Nv[7] = { 12, 0, 0, 24, 24, 0, 96 };
    slong kp[3] = { 2, 1, 1 };            /* x^2 + x + 2 */
    fmpz *N, *tr, *p;
    ihz_weil_t W;
    slong R, Mc, rank0, rank1;
    fmpz_poly_t Q;
    arb_mat_t E, O, T;
    arb_t eps, e, tmp;
    arb_ptr v, xi;
    fmpz_mat_t DTD;
    slong DTDv[9] = { 6, -3, -9, -3, 12, -6, -9, -6, 24 };
    int ok, cert, i, j;

    printf("\n== case 1: K4, q = 2, nv = 4, ne = 6, retained charpoly (x^2+x+2)^3, R = 2 ==\n");
    N = _fmpz_vec_init(len); tr = _fmpz_vec_init(4); p = _fmpz_vec_init(len);
    for (k = 0; k < len; k++) fmpz_set_si(N + k, Nv[k]);
    for (k = 0; k < 4; k++) fmpz_set_si(tr + k, trv[k]);
    trace_seq(p, len, 1, 2);

    ihz_weil_from_counts(&W, N, M, q, tr, trm, 4, 1, prec);

    ok = 1;
    for (k = 0; k < len; k++)
    {
        fmpz_t s; fmpz_init(s);
        fmpz_mul_si(s, p + k, 3);                       /* retained trace s_k = 3 p_k */
        if (!fmpz_equal(W.c + k, s)) ok = 0;
        fmpz_clear(s);
    }
    check(ok, "K4: c_k = 3 (a^k + abar^k), a a root of x^2+x+2, k = 0..6");

    arb_init(e); arb_init(tmp);
    ok = 1;
    for (k = 0; k < len; k++)
    {
        expect_t(e, W.c + k, q, k, 1, prec);
        if (!close_ball(W.t + k, e)) ok = 0;
    }
    check(ok, "K4: t_k = sign * 2^{-k/2} c_k, k = 0..6  (t_0 = 6, t_1 = -3/sqrt2, t_2 = -9/2)");

    /* Toeplitz, even and odd blocks at Mp = 1 */
    arb_mat_init(T, 3, 3); ihz_toeplitz(T, &W, 1, prec);
    ok = 1;
    for (i = 0; i < 3; i++) for (j = 0; j < 3; j++)
        if (!arb_equal(arb_mat_entry(T, i, j), W.t + FLINT_ABS(i - j))) ok = 0;
    check(ok, "K4: T_{jk} = t_{|j-k|} at Mp = 1 (K = 3)");

    arb_mat_init(E, 2, 2); arb_mat_init(O, 1, 1);
    ihz_even_block(E, &W, 1, prec); ihz_odd_block(O, &W, 1, prec);
    arb_set_si(e, 6);
    ok = close_ball(arb_mat_entry(E, 0, 0), e);
    arb_set_si(e, -3);
    ok = ok && close_ball(arb_mat_entry(E, 0, 1), e) && close_ball(arb_mat_entry(E, 1, 0), e);
    arb_set_d(e, 1.5);
    ok = ok && close_ball(arb_mat_entry(E, 1, 1), e);
    check(ok, "K4: even block at Mp = 1 is [[6, -3], [-3, 3/2]] (E_0j = sqrt2 t_j, E_ij = t_|i-j| + t_{i+j})");
    arb_set_d(e, 10.5);
    check(close_ball(arb_mat_entry(O, 0, 0), e), "K4: odd block at Mp = 1 is [t_0 - t_2] = 21/2");

    /* even -> full lift */
    xi = _arb_vec_init(3);
    v = _arb_vec_init(2);
    arb_set_si(v + 0, 6); arb_set_si(v + 1, 4);
    ihz_even_to_full(xi, v, 1, prec);
    arb_set_si(e, 6);
    ok = close_ball(xi + 1, e);
    arb_set_si(e, 4); arb_sqrt_ui(tmp, 2, prec); arb_div(e, e, tmp, prec);
    ok = ok && close_ball(xi + 0, e) && close_ball(xi + 2, e);
    check(ok, "K4: ihz_even_to_full: xi_0 = c_0 at index Mp, xi_{+-j} = c_j/sqrt2");
    _arb_vec_clear(v, 2);

    /* exact integer congruence */
    fmpz_mat_init(DTD, 3, 3);
    ihz_toeplitz_exact(DTD, &W, 1);
    ok = 1;
    for (i = 0; i < 3; i++) for (j = 0; j < 3; j++)
        if (fmpz_cmp_si(fmpz_mat_entry(DTD, i, j), DTDv[3 * i + j]) != 0) ok = 0;
    check(ok, "K4: (DTD)_{jk} = q^{min(j,k)} c_{|j-k|} = [[6,-3,-9],[-3,12,-6],[-9,-6,24]]");

    rank0 = ihz_rank_exact(&W, 0);
    rank1 = ihz_rank_exact(&W, 1);
    check(rank0 == 1, "K4: rank T = 1 = K at Mp = 0 (K = 1), got %ld", rank0);
    check(rank1 == 2, "K4: rank T = 2 < K = 3 at Mp = 1, got %ld", rank1);

    Mc = ihz_critical_window(&R, &W);
    check(Mc == 1 && R == 2, "K4: critical window Mp = 1, R = 2 (got Mp = %ld, R = %ld)", Mc, R);

    fmpz_poly_init(Q);
    ok = ihz_kernel_poly_exact(Q, &W, 1);
    {
        slong co[3] = { 2, 1, 1 };
        (void) kp;
        check(ok && poly_eq_si(Q, co, 3), "K4: kernel polynomial = x^2 + x + 2 (primitive, positive lead)");
        print_poly("Q(z)", Q);
    }

    /* ball stage */
    arb_init(eps);
    v = _arb_vec_init(2);
    ok = ihz_eigmin(eps, v, E, 200, prec);
    check(ok, "K4: ihz_eigmin certifies the minimal eigenpair of the even block at Mp = 1");
    printf("      eps(Mp=1) = "); arb_printn(eps, 20, 0); printf("\n");
    check(ok && arb_contains_zero(eps) && mag_cmp_2exp_si(arb_radref(eps), -66) < 0,
          "K4: eps at the critical window Mp = 1 contains 0 with |eps| < 1e-20");
    cert = ihz_certify_even_simple(E, O, eps, v, prec);
    printf("      ihz_certify_even_simple at eps ~ 0: %d (expected 0: the certificate needs eps > 0 strictly)\n", cert);
    check(cert == 0, "K4: even-simple certificate declines at eps = 0 (expected)");
    _arb_vec_clear(v, 2);

    {
        arb_mat_t E0, O0;
        arb_mat_init(E0, 1, 1); arb_mat_init(O0, 0, 0);
        ihz_even_block(E0, &W, 0, prec); ihz_odd_block(O0, &W, 0, prec);
        v = _arb_vec_init(1);
        ok = ihz_eigmin(eps, v, E0, 200, prec);
        arb_set_si(e, 6);
        check(ok && close_ball(eps, e), "K4: at Mp = 0 (K = 1) eps = t_0 = 6 > 0");
        printf("      eps(Mp=0) = "); arb_printn(eps, 20, 0); printf("\n");
        cert = ihz_certify_even_simple(E0, O0, eps, v, prec);
        printf("      ihz_certify_even_simple at Mp = 0 (eps = 6 > 0): %d\n", cert);
        check(cert == 1, "K4: even-simple certificate holds at Mp = 0 where eps > 0");
        _arb_vec_clear(v, 1);
        arb_mat_clear(E0); arb_mat_clear(O0);
    }

    fmpz_poly_clear(Q); fmpz_mat_clear(DTD);
    arb_mat_clear(E); arb_mat_clear(O); arb_mat_clear(T);
    arb_clear(eps); arb_clear(e); arb_clear(tmp);
    _arb_vec_clear(xi, 3);
    _fmpz_vec_clear(N, len); _fmpz_vec_clear(tr, 4); _fmpz_vec_clear(p, len);
    ihz_weil_clear(&W);
}

/* -------------------------------------------------------------------- case 2: Petersen */
static void
case_petersen(slong prec)
{
    slong M = 3, len = 7, q = 2, k;
    slong trm[4] = { 1, 1, 5, 5 };         /* {2:1, 1:1, 1:(ne-nv)=5, -1:5} */
    slong trv[4] = { 2, 1, 1, -1 };
    slong Nv[7] = { 30, 0, 0, 0, 0, 120, 120 };
    fmpz *N, *tr, *p, *r;
    ihz_weil_t W;
    slong R, Mc, rk[3], i;
    fmpz_poly_t Q;
    arb_mat_t E, O;
    arb_t eps, e, tmp;
    arb_ptr v;
    int ok;

    printf("\n== case 2: Petersen, q = 2, nv = 10, ne = 15, retained (x^2-x+2)^5 (x^2+2x+2)^4, R = 4 ==\n");
    N = _fmpz_vec_init(len); tr = _fmpz_vec_init(4);
    p = _fmpz_vec_init(len); r = _fmpz_vec_init(len);
    for (k = 0; k < len; k++) fmpz_set_si(N + k, Nv[k]);
    for (k = 0; k < 4; k++) fmpz_set_si(tr + k, trv[k]);
    trace_seq(p, len, -1, 2);              /* mu = (1 +- i sqrt7)/2, multiplicity 5 */
    trace_seq(r, len, 2, 2);               /* mu = -1 +- i,          multiplicity 4 */

    ihz_weil_from_counts(&W, N, M, q, tr, trm, 4, 1, prec);

    ok = 1;
    for (k = 0; k < len; k++)
    {
        fmpz_t s; fmpz_init(s);
        fmpz_mul_si(s, p + k, 5);
        fmpz_addmul_si(s, r + k, 4);
        if (!fmpz_equal(W.c + k, s)) ok = 0;
        fmpz_clear(s);
    }
    check(ok, "Petersen: c_k = 5 (mu^k + conj) + 4 (nu^k + conj) over the retained divisor, k = 0..6");

    arb_init(e); arb_init(tmp);
    ok = 1;
    for (k = 0; k < len; k++)
    {
        expect_t(e, W.c + k, q, k, 1, prec);
        if (!close_ball(W.t + k, e)) ok = 0;
    }
    check(ok, "Petersen: t_k = 2^{-k/2} c_k (t_0 = 18, t_1 = -3/sqrt2 = -2.1213..., t_2 = -15/2)");
    printf("      t_0..t_4 ="); for (k = 0; k < 5; k++) { printf(" "); arb_printn(W.t + k, 10, ARB_STR_NO_RADIUS); } printf("\n");

    for (i = 0; i < 3; i++) rk[i] = ihz_rank_exact(&W, i);
    check(rk[0] == 1 && rk[1] == 3 && rk[2] == 4,
          "Petersen: rank T = 1, 3, 4 at K = 1, 3, 5 (rank stops growing at R = 4); got %ld, %ld, %ld",
          rk[0], rk[1], rk[2]);

    Mc = ihz_critical_window(&R, &W);
    check(Mc == 2 && R == 4, "Petersen: critical window Mp = 2 (K = 5), R = 4 (got Mp = %ld, R = %ld)", Mc, R);

    fmpz_poly_init(Q);
    ok = ihz_kernel_poly_exact(Q, &W, 2);
    {
        slong co[5] = { 4, 2, 2, 1, 1 };   /* (x^2 - x + 2)(x^2 + 2x + 2) = x^4 + x^3 + 2x^2 + 2x + 4 */
        check(ok && poly_eq_si(Q, co, 5),
              "Petersen: kernel polynomial = (x^2-x+2)(x^2+2x+2) = x^4+x^3+2x^2+2x+4");
        print_poly("Q(z)", Q);
    }

    /* Mp = 1: under-resolved, eps = 9.4476568 (run_ihara_proto.txt:262) */
    arb_mat_init(E, 2, 2); arb_mat_init(O, 1, 1);
    ihz_even_block(E, &W, 1, prec); ihz_odd_block(O, &W, 1, prec);
    arb_set_d(e, 25.5);
    check(close_ball(arb_mat_entry(O, 0, 0), e), "Petersen: odd block at Mp = 1 is [t_0 - t_2] = 51/2 = 25.5 (run record)");
    arb_init(eps);
    v = _arb_vec_init(2);
    ok = ihz_eigmin(eps, v, E, 200, prec);
    /* E = [[18, -3], [-3, 21/2]]: eps = (57 - sqrt(369))/4 */
    arb_sqrt_ui(e, 369, prec); arb_neg(e, e); arb_add_si(e, e, 57, prec); arb_div_si(e, e, 4, prec);
    check(ok && close_ball(eps, e), "Petersen: eps at Mp = 1 (K = 3) = (57 - sqrt369)/4 = 9.4476568 (run record)");
    printf("      eps(Mp=1) = "); arb_printn(eps, 20, 0); printf("   pinned 9.4476568\n");
    {
        arb_t d; arb_init(d); arb_set_d(d, 9.4476568);
        arb_sub(d, eps, d, prec); arb_abs(d, d);
        arb_set_d(e, 1e-7);
        check(arb_lt(d, e), "Petersen: eps at Mp = 1 agrees with the pinned 9.4476568 to 1e-7");
        arb_clear(d);
    }
    check(ok && ihz_certify_even_simple(E, O, eps, v, prec) == 1,
          "Petersen: even-simple certificate holds at Mp = 1 (eps > 0, under-resolved)");
    _arb_vec_clear(v, 2);
    arb_mat_clear(E); arb_mat_clear(O);

    /* Mp = 2: critical, eps = 0 */
    arb_mat_init(E, 3, 3); arb_mat_init(O, 2, 2);
    ihz_even_block(E, &W, 2, prec); ihz_odd_block(O, &W, 2, prec);
    v = _arb_vec_init(3);
    ok = ihz_eigmin(eps, v, E, 200, prec);
    check(ok, "Petersen: ihz_eigmin certifies the minimal even eigenpair at Mp = 2");
    printf("      eps(Mp=2) = "); arb_printn(eps, 20, 0); printf("\n");
    check(ok && arb_contains_zero(eps) && mag_cmp_2exp_si(arb_radref(eps), -66) < 0,
          "Petersen: eps at the critical window Mp = 2 contains 0 with |eps| < 1e-20");
    printf("      ihz_certify_even_simple at eps ~ 0: %d (expected 0)\n", ihz_certify_even_simple(E, O, eps, v, prec));
    _arb_vec_clear(v, 3);

    fmpz_poly_clear(Q);
    arb_mat_clear(E); arb_mat_clear(O);
    arb_clear(eps); arb_clear(e); arb_clear(tmp);
    _fmpz_vec_clear(N, len); _fmpz_vec_clear(tr, 4);
    _fmpz_vec_clear(p, len); _fmpz_vec_clear(r, len);
    ihz_weil_clear(&W);
}

/* -------------------------------------------------------------------- case 3: a curve, sign = -1 */
static void
case_curve(slong prec)
{
    slong M = 3, len = 7, q = 5, k;
    slong trm[2] = { 1, 1 };               /* {5:1, 1:1} */
    slong trv[2] = { 5, 1 };
    /* N_k = 1 + 5^k - (a^k + conj(a)^k), a = -1 + 2i (a root of x^2 + 2x + 5).
     * N_0 = 1 + 1 - 2 = 0, which is what the identity t_0 = sign (N_0 - sum tm) = 2 forces. */
    slong Nv[7] = { 0, 8, 32, 104, 640, 3208, 15392 };
    fmpz *N, *tr, *p;
    ihz_weil_t W;
    slong R, Mc, rank0, rank1;
    fmpz_poly_t Q;
    arb_mat_t E, O;
    arb_t eps, e;
    arb_ptr v;
    int ok;

    printf("\n== case 3: elliptic curve over F_5 (Pauli qubit), q = 5, sign = -1, a = -1 + 2i, R = 2 ==\n");
    N = _fmpz_vec_init(len); tr = _fmpz_vec_init(2); p = _fmpz_vec_init(len);
    for (k = 0; k < len; k++) fmpz_set_si(N + k, Nv[k]);
    for (k = 0; k < 2; k++) fmpz_set_si(tr + k, trv[k]);
    trace_seq(p, len, 2, 5);

    ihz_weil_from_counts(&W, N, M, q, tr, trm, 2, -1, prec);

    ok = 1;
    for (k = 0; k < len; k++)
    {
        fmpz_t s; fmpz_init(s);
        fmpz_neg(s, p + k);                /* c_k = N_k - (5^k + 1) = -(a^k + abar^k) */
        if (!fmpz_equal(W.c + k, s)) ok = 0;
        fmpz_clear(s);
    }
    check(ok, "curve: c_k = -(a^k + conj(a)^k), k = 0..6  (c_0 = -2, c_1 = 2, c_2 = 6, c_3 = -22)");

    arb_init(e);
    ok = 1;
    for (k = 0; k < len; k++)
    {
        expect_t(e, W.c + k, q, k, -1, prec);
        if (!close_ball(W.t + k, e)) ok = 0;
    }
    arb_set_si(e, 2);
    check(ok, "curve: t_k = -5^{-k/2} c_k = 5^{-k/2}(a^k + conj(a)^k)");
    check(close_ball(W.t + 0, e), "curve: t_0 = sign (N_0 - sum tm) = 2 = the number of retained points");

    rank0 = ihz_rank_exact(&W, 0);
    rank1 = ihz_rank_exact(&W, 1);
    check(rank0 == 1 && rank1 == 2, "curve: rank T = 1 at K = 1, 2 at K = 3; got %ld, %ld", rank0, rank1);

    Mc = ihz_critical_window(&R, &W);
    check(Mc == 1 && R == 2, "curve: critical window Mp = 1, R = 2 (got Mp = %ld, R = %ld)", Mc, R);

    fmpz_poly_init(Q);
    ok = ihz_kernel_poly_exact(Q, &W, 1);
    {
        slong co[3] = { 5, 2, 1 };
        check(ok && poly_eq_si(Q, co, 3), "curve: kernel polynomial = x^2 + 2x + 5 (the retained divisor)");
        print_poly("Q(z)", Q);
    }

    arb_mat_init(E, 2, 2); arb_mat_init(O, 1, 1);
    ihz_even_block(E, &W, 1, prec); ihz_odd_block(O, &W, 1, prec);
    arb_init(eps);
    v = _arb_vec_init(2);
    ok = ihz_eigmin(eps, v, E, 200, prec);
    printf("      eps(Mp=1) = "); arb_printn(eps, 20, 0); printf("\n");
    check(ok && arb_contains_zero(eps) && mag_cmp_2exp_si(arb_radref(eps), -66) < 0,
          "curve: eps at the critical window Mp = 1 contains 0 with |eps| < 1e-20 (the form is PSD: sign = -1 applied)");
    _arb_vec_clear(v, 2);

    fmpz_poly_clear(Q);
    arb_mat_clear(E); arb_mat_clear(O);
    arb_clear(eps); arb_clear(e);
    _fmpz_vec_clear(N, len); _fmpz_vec_clear(tr, 2); _fmpz_vec_clear(p, len);
    ihz_weil_clear(&W);
}

int
main(void)
{
    slong prec = 256;
    printf("test_toeplitz: weil_data / toeplitz / rank / eigmin at prec = %ld\n", prec);
    case_K4(prec);
    case_petersen(prec);
    case_curve(prec);
    printf("\n%ld checks, %d failures\n", (slong) checks, failures);
    flint_cleanup();
    return failures != 0;
}
