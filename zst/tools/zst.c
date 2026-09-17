#define _POSIX_C_SOURCE 200809L
/* zst: command-line driver of the tracer-bullet pipeline.
 *   zst [--x 9] [--N 40] [--prec 400] [--zeros 20] [--iters 40]
 * x = lambda^2 (primes <= x enter), N = Fourier truncation, prec in bits.
 * Ground truth: refs/src/2511.22755/mc2arXiv.tex, Theorem `finmain` (lines 1085-1118): spectrum of
 * D_log^{(lambda,N)} = zeros of xi_hat = 2 pi s/L over the secular roots s; the delta_N normalisation
 * (Cor. `dirichlet1`, lines 941-990) differs from <eta|xi> = 1 by L^{1/2} and only rescales xi_hat. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <flint/acb_dirichlet.h>
#include "zst.h"

static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + 1e-9 * t.tv_nsec; }

int main(int argc, char **argv)
{
    double xd = 9.0; slong N = 40, prec = 400, K = 20, iters = 40;
    int i;
    for (i = 1; i + 1 < argc; i += 2)
    {
        if (!strcmp(argv[i], "--x")) xd = atof(argv[i + 1]);
        else if (!strcmp(argv[i], "--N")) N = atol(argv[i + 1]);
        else if (!strcmp(argv[i], "--prec")) prec = atol(argv[i + 1]);
        else if (!strcmp(argv[i], "--zeros")) K = atol(argv[i + 1]);
        else if (!strcmp(argv[i], "--iters")) iters = atol(argv[i + 1]);
        else { fprintf(stderr, "unknown option %s\n", argv[i]); return 2; }
    }
    {
        arb_t x, L, eps, shift, twopiL, t, u, sum;
        arb_ptr a, b, v, xi, roots, gamma;
        arb_mat_t E, O;
        ulong X = (ulong) (xd + 1e-9);
        slong nroots, unres, k, dim = N + 1;
        double t0 = now(), t1, t2, t3, t4;
        int ok;

        arb_init(x); arb_init(L); arb_init(eps); arb_init(shift); arb_init(twopiL);
        arb_init(t); arb_init(u); arb_init(sum);
        arb_set_d(x, xd);
        zst_window_L(L, x, prec);
        a = _arb_vec_init(N + 1); b = _arb_vec_init(N + 1);
        v = _arb_vec_init(dim); xi = _arb_vec_init(N + 1);
        roots = _arb_vec_init(N); gamma = _arb_vec_init(K);
        arb_mat_init(E, dim, dim); arb_mat_init(O, N, N);

        flint_printf("zst: x = %g (prime powers <= %wu), N = %wd, prec = %wd bits, L = ", xd, X, N, prec);
        arb_printn(L, 15, 0); flint_printf("\n");

        zst_riemann_ab(a, b, N, x, X, prec);
        zst_even_block(E, a, b, N, prec);
        zst_odd_block(O, a, b, N, prec);
        t1 = now();
        flint_printf("matrix build: %.2fs\n", t1 - t0);

        ok = zst_eigmin(eps, v, E, iters, prec);
        t2 = now();
        flint_printf("minimal even eigenvalue eps_N = "); arb_printn(eps, 10, 0);
        flint_printf("  (%s, %.2fs)\n", ok ? "Rump-certified" : "NOT certified", t2 - t1);
        if (!ok) { flint_printf("eigenpair not certified; raise --prec or --iters\n"); return 1; }

        /* even-simple check: shift = 2 * upper bound of eps (eps > 0 expected) */
        arb_get_ubound_arf(arb_midref(shift), eps, prec); mag_zero(arb_radref(shift));
        arb_mul_2exp_si(shift, shift, 1);
        {
            int es = zst_certify_even_simple(E, O, eps, v, prec);
            t3 = now();
            flint_printf("even-simple hypothesis (deflated Cholesky of E - 2 eps and O - 2 eps): %s  (%.2fs)\n",
                         es ? "CERTIFIED" : "not certified", t3 - t2);
        }

        /* xi_j from the even coordinates, normalised sum_{j=-N}^N xi_j = 1 */
        arb_set(xi + 0, v + 0);
        arb_sqrt_ui(t, 2, prec);
        for (k = 1; k <= N; k++) arb_div(xi + k, v + k, t, prec);
        arb_set(sum, xi + 0);
        for (k = 1; k <= N; k++) { arb_mul_2exp_si(u, xi + k, 1); arb_add(sum, sum, u, prec); }
        for (k = 0; k <= N; k++) arb_div(xi + k, xi + k, sum, prec);
        flint_printf("xi_0 = "); arb_printn(xi + 0, 10, 0);
        flint_printf(", xi_1 = "); arb_printn(xi + 1, 10, 0);
        flint_printf(", xi_N = "); arb_printn(xi + N, 5, 0); flint_printf("\n");

        nroots = zst_secular_roots(roots, N, &unres, xi, N, prec);
        t4 = now();
        flint_printf("positive secular roots: %wd certified of N = %wd, %wd unresolved  ->  spectrum %s  (%.2fs)\n",
                     nroots, N, unres, (nroots == N) ? "COMPLETE" : "incomplete", t4 - t3);

        /* reference zeros: full precision for the first 20 (where the construction is most accurate),
         * 400 bits for the rest (their certified error is far above 1e-100 anyway) */
        {
            slong K1 = FLINT_MIN(K, 20);
            zst_zeta_zeros(gamma, K1, prec);
            if (K > K1)
            {
                acb_ptr rho = _acb_vec_init(K - K1); fmpz_t n1; fmpz_init(n1); fmpz_set_si(n1, K1 + 1);
                acb_dirichlet_zeta_zeros(rho, n1, K - K1, FLINT_MIN(prec, 400));
                for (k = K1; k < K; k++) arb_set(gamma + k, acb_imagref(rho + k - K1));
                _acb_vec_clear(rho, K - K1); fmpz_clear(n1);
            }
        }
        arb_const_pi(twopiL, prec); arb_mul_2exp_si(twopiL, twopiL, 1); arb_div(twopiL, twopiL, L, prec);
        flint_printf("\n  k   z_k = 2 pi s_k / L                                   |z_k - gamma_k| <=\n");
        for (k = 0; k < K && k < nroots; k++)
        {
            mag_t m; mag_init(m);
            arb_mul(t, roots + k, twopiL, prec);
            arb_sub(u, t, gamma + k, prec);
            arb_get_mag(m, u);
            flint_printf("%3wd   ", k + 1); arb_printn(t, 40, ARB_STR_NO_RADIUS);
            flint_printf("   "); mag_printd(m, 3); flint_printf("\n");
            mag_clear(m);
        }
        flint_printf("\ntotal %.2fs\n", now() - t0);

        _arb_vec_clear(a, N + 1); _arb_vec_clear(b, N + 1); _arb_vec_clear(v, dim); _arb_vec_clear(xi, N + 1);
        _arb_vec_clear(roots, N); _arb_vec_clear(gamma, K);
        arb_mat_clear(E); arb_mat_clear(O);
        arb_clear(x); arb_clear(L); arb_clear(eps); arb_clear(shift); arb_clear(twopiL);
        arb_clear(t); arb_clear(u); arb_clear(sum);
    }
    flint_cleanup();
    return 0;
}
