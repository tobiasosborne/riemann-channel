/* Unit tests for the certified minimal eigenpair and the inertia count. Ground truth is closed-form
 * linear algebra: [[2,-1],[-1,2]] has eigenvalues 1 (vector (1,1)) and 3 (vector (1,-1));
 * diag-like [[1e-30, 1e-31],[1e-31, 1]] is a stand-in for the near-singular even block. */
#include <stdio.h>
#include "zst.h"

static int fails = 0;
#define CHECK(cond, msg) do { if (!(cond)) { flint_printf("FAIL: %s\n", msg); fails++; } } while (0)

int main(void)
{
    slong prec = 200;
    arb_mat_t A;
    arb_t eps, one, shift, t;
    arb_ptr v = _arb_vec_init(2);
    arb_mat_init(A, 2, 2); arb_init(eps); arb_init(one); arb_init(shift); arb_init(t);

    arb_set_si(arb_mat_entry(A, 0, 0), 2); arb_set_si(arb_mat_entry(A, 0, 1), -1);
    arb_set_si(arb_mat_entry(A, 1, 0), -1); arb_set_si(arb_mat_entry(A, 1, 1), 2);
    CHECK(zst_eigmin(eps, v, A, 40, prec) == 1, "2x2: eigenpair certified");
    arb_one(one);
    CHECK(arb_contains(eps, one), "2x2: minimal eigenvalue 1");
    CHECK(mag_cmp_2exp_si(arb_radref(eps), -150) < 0, "2x2: eigenvalue to 150 bits");
    /* normalisation: largest component exactly 1; the other equals 1 */
    CHECK(arb_contains(v + 0, one) && arb_contains(v + 1, one), "2x2: eigenvector (1,1)");

    arb_set_d(shift, 1.5);
    CHECK(zst_inertia_neg(A, shift, prec) == 1, "2x2: one eigenvalue below 1.5");
    arb_set_d(shift, 0.5);
    CHECK(zst_inertia_neg(A, shift, prec) == 0, "2x2: none below 0.5");
    arb_set_d(shift, 3.5);
    CHECK(zst_inertia_neg(A, shift, prec) == 2, "2x2: two below 3.5");
    arb_set_si(shift, 1); /* shift exactly at an eigenvalue: a pivot ball contains zero -> inconclusive */
    CHECK(zst_inertia_neg(A, shift, prec) == -1, "2x2: shift at eigenvalue is inconclusive");

    /* even-simple certificate by deflated Cholesky: for [[2,-1],[-1,2]] with (eps, v) = (1, (1,1)) and
     * the "odd block" [[5]]: shift 2 eps = 2 lies between 1 and 3, so certifiable; with the odd block
     * [[1.5]] it must fail (an odd eigenvalue below the shift); with the shift at 4 (above 3) the even
     * block has two eigenvalues below it and the deflated matrix is indefinite: must fail. */
    {
        arb_mat_t O1; arb_mat_init(O1, 1, 1);
        arb_set_si(arb_mat_entry(O1, 0, 0), 5);
        arb_set_si(arb_mat_entry(A, 0, 0), 2); arb_set_si(arb_mat_entry(A, 0, 1), -1);
        arb_set_si(arb_mat_entry(A, 1, 0), -1); arb_set_si(arb_mat_entry(A, 1, 1), 2);
        arb_one(eps); arb_one(v + 0); arb_one(v + 1);
        CHECK(zst_certify_even_simple(A, O1, eps, v, prec) == 1, "deflated Cholesky: certified");
        arb_set_d(arb_mat_entry(O1, 0, 0), 1.5);
        CHECK(zst_certify_even_simple(A, O1, eps, v, prec) == 0, "deflated Cholesky: odd eigenvalue below shift -> fail");
        arb_set_si(arb_mat_entry(O1, 0, 0), 5);
        arb_set_si(eps, 2);   /* wrong eps (not an eigenvalue): shift 4 > 3, deflation cannot rescue it */
        CHECK(zst_certify_even_simple(A, O1, eps, v, prec) == 0, "deflated Cholesky: shift above second eigenvalue -> fail");
        arb_mat_clear(O1);
    }

    /* near-singular: minimal eigenvalue ~ 1e-30 - 1e-62, certified with a tiny radius */
    arb_set_str(arb_mat_entry(A, 0, 0), "1e-30", prec); arb_set_str(arb_mat_entry(A, 0, 1), "1e-31", prec);
    arb_set_str(arb_mat_entry(A, 1, 0), "1e-31", prec); arb_set_si(arb_mat_entry(A, 1, 1), 1);
    CHECK(zst_eigmin(eps, v, A, 40, prec) == 1, "near-singular: certified");
    arb_set_str(t, "1e-30", prec);
    arb_sub(t, eps, t, prec); arb_abs(t, t);
    arb_set_str(shift, "2e-62", prec);
    CHECK(arb_lt(t, shift), "near-singular: eps = 1e-30 - 1e-62 + O(1e-92)");
    CHECK(mag_cmp_2exp_si(arb_radref(eps), -250) < 0, "near-singular: eigenvalue radius tiny");

    arb_mat_clear(A); arb_clear(eps); arb_clear(one); arb_clear(shift); arb_clear(t); _arb_vec_clear(v, 2);
    flint_cleanup();
    flint_printf("test_eigmin: %s\n", fails ? "FAIL" : "PASS");
    return fails ? 1 : 0;
}
