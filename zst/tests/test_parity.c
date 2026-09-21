/* Unit tests for the certified MINIMUM eigenpair of a block and the parity of the global minimum.
 *
 * Ground truth 1 (closed form): D = diag(-3, -1, 2, 5) conjugated by the Householder reflection
 * H = I - 2 w w^T/(w^T w), w = (1, 2, 3, 4) (fixed, deterministic; H = H^T = H^{-1}), so A = H D H
 * is a full symmetric matrix with spectrum {-3, -1, 2, 5}. Its minimum is -3 and its smallest-modulus
 * eigenvalue is -1: zst_eigmin (inverse iteration targets the smallest modulus) must return -1 and
 * zst_block_min must return -3. This is exactly the failure mode the MVP-3 header warns about
 * (include/zst.h, zst_block_min).
 *
 * Ground truth 2 (zeta regression): x = 13, N = 20, 400 bits. ./build/zst --x 13 --N 20 gives the
 * certified minimal even eigenvalue 1.566107855e-39 with the even-simple hypothesis certified, so the
 * global minimum of the Weil form is even: zst_parity must return +1 with min E = 1.566107855e-39 and
 * a strictly larger min O. Feeding the two blocks in the opposite roles must return -1. */
#include <stdio.h>
#include "zst.h"

static int fails = 0;
#define CHECK(cond, msg) do { if (!(cond)) { flint_printf("FAIL: %s\n", msg); fails++; } } while (0)

/* A = H D H, H = I - 2 w w^T/(w^T w) */
static void
householder_conj(arb_mat_t A, const slong *w, const slong *d, slong n, slong prec)
{
    arb_mat_t H, T;
    arb_t c, t;
    slong i, j, ww = 0;
    arb_mat_init(H, n, n); arb_mat_init(T, n, n);
    arb_init(c); arb_init(t);
    for (i = 0; i < n; i++) ww += w[i] * w[i];
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
        {
            arb_set_si(c, -2 * w[i] * w[j]);
            arb_div_si(c, c, ww, prec);
            if (i == j) arb_add_ui(c, c, 1, prec);
            arb_set(arb_mat_entry(H, i, j), c);
        }
    for (i = 0; i < n; i++)                              /* T = H D */
        for (j = 0; j < n; j++)
            arb_mul_si(arb_mat_entry(T, i, j), arb_mat_entry(H, i, j), d[j], prec);
    arb_mat_mul(A, T, H, prec);
    for (i = 0; i < n; i++)                              /* symmetrise (exact in exact arithmetic) */
        for (j = 0; j < i; j++)
        {
            arb_add(t, arb_mat_entry(A, i, j), arb_mat_entry(A, j, i), prec);
            arb_mul_2exp_si(t, t, -1);
            arb_set(arb_mat_entry(A, i, j), t); arb_set(arb_mat_entry(A, j, i), t);
        }
    arb_mat_clear(H); arb_mat_clear(T); arb_clear(c); arb_clear(t);
}

static void
test_closed_form(void)
{
    slong prec = 200, n = 4, w[4] = {1, 2, 3, 4}, d[4] = {-3, -1, 2, 5};
    arb_mat_t A;
    arb_t lam, lo;
    arb_ptr v = _arb_vec_init(n);
    arb_mat_init(A, n, n); arb_init(lam); arb_init(lo);
    householder_conj(A, w, d, n, prec);

    CHECK(zst_block_min(lam, v, A, 40, prec) == 1, "4x4: block minimum certified");
    CHECK(arb_contains_si(lam, -3), "4x4: block minimum is -3");
    CHECK(mag_cmp_2exp_si(arb_radref(lam), -80) < 0, "4x4: block minimum to 80 bits");

    /* the old path: inverse iteration targets the eigenvalue of smallest modulus, which is -1 here,
     * so it misses the minimum -3 entirely. (Its box is also not a valid enclosure once the iteration
     * has not converged -- the ratio |-1|/|2| = 1/2 here leaves a Rayleigh error near 1e-24 after 40
     * steps while the returned radius is far smaller -- which is why zst_block_min brackets the
     * minimum by Rayleigh above and ball-LDL^T inertia below instead of trusting that box.) */
    CHECK(zst_eigmin(lam, v, A, 40, prec) == 1, "4x4: zst_eigmin certified");
    CHECK(!arb_contains_si(lam, -3), "4x4: zst_eigmin does NOT return the minimum");
    arb_set_si(lo, -2);
    CHECK(arb_gt(lam, lo), "4x4: zst_eigmin lands on the smallest-modulus eigenvalue, not on -3");

    arb_mat_clear(A); arb_clear(lam); arb_clear(lo); _arb_vec_clear(v, n);
}

static void
test_zeta_parity(void)
{
    slong N = 20, prec = 400, dim = N + 1;
    arb_t x, minE, minO, gap, t, tol;
    arb_ptr a, b;
    arb_mat_t E, O;
    int p;
    arb_init(x); arb_init(minE); arb_init(minO); arb_init(gap); arb_init(t); arb_init(tol);
    a = _arb_vec_init(N + 1); b = _arb_vec_init(N + 1);
    arb_mat_init(E, dim, dim); arb_mat_init(O, N, N);
    arb_set_ui(x, 13);
    zst_riemann_ab(a, b, N, x, 13, prec);
    zst_even_block(E, a, b, N, prec);
    zst_odd_block(O, a, b, N, prec);

    p = zst_parity(minE, minO, gap, E, O, 40, prec);
    CHECK(p == 1, "zeta x=13 N=20: parity +1 (even minimum)");
    arb_set_str(t, "1.566107855e-39", prec); arb_set_str(tol, "1e-48", prec);
    arb_sub(t, minE, t, prec); arb_abs(t, t);
    if (!arb_lt(t, tol))
    {
        flint_printf("FAIL: zeta x=13 N=20: min E = "); arb_printn(minE, 12, 0); flint_printf("\n"); fails++;
    }
    CHECK(arb_lt(minE, minO), "zeta x=13 N=20: min E < min O certified");
    CHECK(arb_is_positive(gap), "zeta x=13 N=20: certified positive gap");
    arb_sub(t, minO, minE, prec);
    CHECK(!arb_gt(gap, t), "zeta x=13 N=20: gap is a lower bound on |min E - min O|");

    /* the same two blocks with the roles exchanged: the "even" block now has the larger minimum */
    p = zst_parity(minE, minO, gap, O, E, 40, prec);
    CHECK(p == -1, "zeta x=13 N=20 swapped: parity -1 (odd minimum)");
    CHECK(arb_lt(minO, minE), "zeta x=13 N=20 swapped: min O < min E certified");

    _arb_vec_clear(a, N + 1); _arb_vec_clear(b, N + 1);
    arb_mat_clear(E); arb_mat_clear(O);
    arb_clear(x); arb_clear(minE); arb_clear(minO); arb_clear(gap); arb_clear(t); arb_clear(tol);
}

int main(void)
{
    test_closed_form();
    test_zeta_parity();
    flint_cleanup();
    flint_printf("test_parity: %s\n", fails ? "FAIL" : "PASS");
    return fails ? 1 : 0;
}
