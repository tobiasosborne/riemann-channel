/* End-to-end: x = 9, N = 40, 400 bits. Ground truth: the mpmath prototype
 * notes/zeta-spectral-triples/ccm_proto.py (run: lambda=3, N=40, 60 digits, 2026-09-17) gives
 * |z_1 - gamma_1| = 2.89e-34, |z_5 - gamma_5| = 2.33e-25, eps_N = 5.3927444e-38, next even 4.43e-31,
 * smallest odd 2.08e-34, and N = 40 positive secular roots (paper: Theorem `finmain`,
 * refs/src/2511.22755/mc2arXiv.tex lines 1085-1118). */
#include <stdio.h>
#include "zst.h"

int main(void)
{
    slong N = 40, prec = 400, dim = N + 1, k, nroots, unres, fails = 0;
    arb_t x, L, eps, shift, twopiL, t, u, sum, tol;
    arb_ptr a, b, v, xi, roots, gamma;
    arb_mat_t E, O;
    arb_init(x); arb_init(L); arb_init(eps); arb_init(shift); arb_init(twopiL);
    arb_init(t); arb_init(u); arb_init(sum); arb_init(tol);
    a = _arb_vec_init(N + 1); b = _arb_vec_init(N + 1); v = _arb_vec_init(dim); xi = _arb_vec_init(N + 1);
    roots = _arb_vec_init(N); gamma = _arb_vec_init(5);
    arb_mat_init(E, dim, dim); arb_mat_init(O, N, N);
    arb_set_ui(x, 9);
    zst_window_L(L, x, prec);
    zst_riemann_ab(a, b, N, x, 9, prec);
    zst_even_block(E, a, b, N, prec);
    zst_odd_block(O, a, b, N, prec);
    if (!zst_eigmin(eps, v, E, 40, prec)) { flint_printf("eigmin not certified\n"); fails++; }
    arb_set_str(t, "5.3927444e-38", prec); arb_set_str(tol, "1e-44", prec);
    arb_sub(u, eps, t, prec); arb_abs(u, u);
    if (!arb_lt(u, tol)) { flint_printf("eps mismatch: "); arb_printn(eps, 12, 0); flint_printf("\n"); fails++; }
    arb_get_ubound_arf(arb_midref(shift), eps, prec); mag_zero(arb_radref(shift)); arb_mul_2exp_si(shift, shift, 1);
    if (zst_inertia_neg(E, shift, prec) != 1) { flint_printf("even inertia != 1\n"); fails++; }
    if (zst_inertia_neg(O, shift, prec) != 0) { flint_printf("odd inertia != 0\n"); fails++; }
    arb_set(xi + 0, v + 0); arb_sqrt_ui(t, 2, prec);
    for (k = 1; k <= N; k++) arb_div(xi + k, v + k, t, prec);
    arb_set(sum, xi + 0);
    for (k = 1; k <= N; k++) { arb_mul_2exp_si(u, xi + k, 1); arb_add(sum, sum, u, prec); }
    for (k = 0; k <= N; k++) arb_div(xi + k, xi + k, sum, prec);
    nroots = zst_secular_roots(roots, N, &unres, xi, N, prec);
    if (nroots != N) { flint_printf("only %wd roots (%wd unresolved)\n", nroots, unres); fails++; }
    zst_zeta_zeros(gamma, 5, prec);
    arb_const_pi(twopiL, prec); arb_mul_2exp_si(twopiL, twopiL, 1); arb_div(twopiL, twopiL, L, prec);
    arb_mul(t, roots + 0, twopiL, prec); arb_sub(t, t, gamma + 0, prec); arb_abs(t, t);
    arb_set_str(tol, "1e-33", prec);
    if (!arb_lt(t, tol)) { flint_printf("|z_1 - gamma_1| not < 1e-33: "); arb_printn(t, 5, 0); flint_printf("\n"); fails++; }
    arb_mul(t, roots + 4, twopiL, prec); arb_sub(t, t, gamma + 4, prec); arb_abs(t, t);
    arb_set_str(tol, "1e-24", prec);
    if (!arb_lt(t, tol)) { flint_printf("|z_5 - gamma_5| not < 1e-24: "); arb_printn(t, 5, 0); flint_printf("\n"); fails++; }
    _arb_vec_clear(a, N + 1); _arb_vec_clear(b, N + 1); _arb_vec_clear(v, dim); _arb_vec_clear(xi, N + 1);
    _arb_vec_clear(roots, N); _arb_vec_clear(gamma, 5);
    arb_mat_clear(E); arb_mat_clear(O);
    arb_clear(x); arb_clear(L); arb_clear(eps); arb_clear(shift); arb_clear(twopiL);
    arb_clear(t); arb_clear(u); arb_clear(sum); arb_clear(tol);
    flint_cleanup();
    flint_printf("test_pipeline: %s\n", fails ? "FAIL" : "PASS");
    return fails ? 1 : 0;
}
