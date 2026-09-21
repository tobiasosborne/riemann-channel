/* Reference data loader: tests/data/ell_ref.txt (tools/pari_ref.py, PARI 2.17.2).
 * Ground truth: the file itself, and notes/zeta-spectral-triples/ellcurve/plan.md Section 3 (the
 * minimal models, conductors, root numbers and analytic ranks of the four test curves). The analytic
 * normalisation puts the zeros at 1/2 + i gamma, so a curve of analytic rank r has gamma_1 = ... =
 * gamma_r = 0 (PARI's lfunzeros lists the central zero with its multiplicity). */
#include <stdio.h>
#include <string.h>
#include <flint/fmpz_vec.h>
#include "zst.h"

static int fails = 0;
#define CHECK(cond, msg) do { if (!(cond)) { flint_printf("FAIL: %s\n", msg); fails++; } } while (0)

int main(void)
{
    slong prec = 200, K = 6, rank, i;
    fmpz *ainvs = _fmpz_vec_init(5);
    fmpz_t C;
    arb_ptr gamma = _arb_vec_init(K);
    arb_t t, tol;
    int w;

    fmpz_init(C); arb_init(t); arb_init(tol);
    arb_set_str(tol, "1e-37", prec);

    /* 37a1: [0,0,1,-1,0], conductor 37, root number -1, analytic rank 1 */
    CHECK(zst_ell_ref(ainvs, C, &w, &rank, gamma, K, "37a1", NULL, prec) == 1, "37a1: found");
    CHECK(fmpz_equal_si(C, 37), "37a1: conductor 37");
    CHECK(w == -1, "37a1: root number -1");
    CHECK(rank == 1, "37a1: analytic rank 1");
    {
        slong ai[5] = {0, 0, 1, -1, 0};
        int good = 1;
        for (i = 0; i < 5; i++) if (!fmpz_equal_si(ainvs + i, ai[i])) good = 0;
        CHECK(good, "37a1: minimal model [0,0,1,-1,0]");
    }
    CHECK(arb_contains_zero(gamma + 0), "37a1: gamma_1 is the central zero 0");
    arb_set_str(t, "5.0031700140066586953462731557096274931073", prec);
    arb_sub(t, gamma + 1, t, prec); arb_abs(t, t);
    CHECK(arb_lt(t, tol), "37a1: gamma_2 = 5.00317001400665869534...");
    CHECK(mag_cmp_2exp_si(arb_radref(gamma + 1), -100) < 0, "37a1: gamma_2 is a narrow ball");
    CHECK(arb_contains_si(gamma + 1, 5) == 0, "37a1: gamma_2 ball excludes 5");

    /* 389a1: analytic rank 2, so the first two listed ordinates are the central zero */
    CHECK(zst_ell_ref(ainvs, C, &w, &rank, gamma, K, "389a1", NULL, prec) == 1, "389a1: found");
    CHECK(fmpz_equal_si(C, 389), "389a1: conductor 389");
    CHECK(w == 1, "389a1: root number +1");
    CHECK(rank == 2, "389a1: analytic rank 2");
    CHECK(arb_contains_zero(gamma + 0) && arb_contains_zero(gamma + 1), "389a1: two central zeros");
    arb_set_str(t, "2.8760990712604652017634260947208978220800", prec);
    arb_sub(t, gamma + 2, t, prec); arb_abs(t, t);
    CHECK(arb_lt(t, tol), "389a1: gamma_3 = 2.87609907126046520176...");

    /* 11a1: rank 0, first zero 6.3626138947130887013860290088787011871237 */
    CHECK(zst_ell_ref(ainvs, C, &w, &rank, gamma, K, "11a1", NULL, prec) == 1, "11a1: found");
    CHECK(fmpz_equal_si(C, 11) && w == 1 && rank == 0, "11a1: conductor 11, w = +1, rank 0");
    arb_set_str(t, "6.3626138947130887013860290088787011871237", prec);
    arb_sub(t, gamma + 0, t, prec); arb_abs(t, t);
    CHECK(arb_lt(t, tol), "11a1: gamma_1 = 6.36261389471308870138...");

    /* explicit path and the ../ fallback both resolve */
    CHECK(zst_ell_ref(ainvs, C, &w, &rank, gamma, K, "14a1", "tests/data/ell_ref.txt", prec) == 1,
          "14a1: explicit path");
    CHECK(fmpz_equal_si(C, 14) && rank == 0, "14a1: conductor 14, rank 0");

    /* an unknown label fails cleanly; an unusable explicit path falls back to the default locations */
    CHECK(zst_ell_ref(ainvs, C, &w, &rank, gamma, K, "42z9", NULL, prec) == 0, "unknown label: 0");
    CHECK(zst_ell_ref(ainvs, C, &w, &rank, gamma, K, "11a1", "/nonexistent/ell_ref.txt", prec) == 1,
          "unusable path: falls back to tests/data/ell_ref.txt");

    _fmpz_vec_clear(ainvs, 5); _arb_vec_clear(gamma, K);
    fmpz_clear(C); arb_clear(t); arb_clear(tol);
    flint_cleanup();
    flint_printf("test_ell_ref: %s\n", fails ? "FAIL" : "PASS");
    return fails ? 1 : 0;
}
