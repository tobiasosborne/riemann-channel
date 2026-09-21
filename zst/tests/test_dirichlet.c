/* Real primitive Dirichlet characters through the generic data model: the second independent
 * instance of the builder (the review's recommendation 1, "put the real primitive Dirichlet
 * character first as the implementation control").
 *
 * 1. chi(p) = Kronecker (D/p) for D = -4, -3, 5 at every prime p <= 50, against hard-coded truth
 *    (quadratic reciprocity: (-4/p) = (-1/p) = +1 iff p = 1 mod 4; (-3/p) = +1 iff p = 1 mod 3;
 *    (5/p) = (p/5) = +1 iff p = +-1 mod 5; 0 at p | D).  Read back from the atom weights
 *    w_{p,1} = -chi(p) log p / sqrt p (F5 with chi in place of the Satake power sums), which is the
 *    form the character actually enters the distribution in.
 * 2. (a_n, b_n) for chi_D at x = X = 13, N = 8, D = -4, -3, 5, 8, -8, 13, against the 50-digit pins
 *    of tests/data/dirichlet_pins.txt.  Those come from checks/dirichlet_pins.py, an INDEPENDENT
 *    mpmath transcription of the formula sheet (it imports neither the C library nor the review's
 *    elliptic prototype), so this is a genuine cross-check of F2-F16 on a second L-function.
 *    Tolerance 1e-40 at 400 bits.
 * Formula sheet: notes/zeta-spectral-triples/ellcurve/astra-review.md, F2, F5, F6, F8, F14, F16.
 */
#include <stdio.h>
#include <string.h>
#include <flint/fmpz_vec.h>
#include <flint/ulong_extras.h>
#include "zst.h"

static int fails = 0;

static const ulong tp[15] = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47 };
static const int chi_m4[15] = {  0, -1,  1, -1, -1,  1,  1, -1, -1,  1, -1,  1,  1, -1, -1 };
static const int chi_m3[15] = { -1,  0, -1,  1, -1,  1, -1,  1, -1, -1,  1,  1, -1,  1, -1 };
static const int chi_p5[15] = { -1, -1,  0, -1,  1, -1, -1,  1, -1,  1,  1, -1,  1, -1, -1 };

static FILE *
open_data(const char *name)
{
    char path[256];
    FILE *f;
    snprintf(path, sizeof(path), "tests/data/%s", name);
    f = fopen(path, "r");
    if (f == NULL)
    {
        snprintf(path, sizeof(path), "../tests/data/%s", name);
        f = fopen(path, "r");
    }
    if (f == NULL) { flint_printf("test_dirichlet: cannot open tests/data/%s\n", name); fails++; }
    return f;
}

/* chi(p) read back from the m = 1 atom at y = log p. */
static void
test_chi_values(slong Dval, const int *truth, slong prec)
{
    zst_weil_t W;
    fmpz_t D;
    arb_t x, y, wexp, lp, r, tol;
    slong i, j;

    fmpz_init(D); fmpz_set_si(D, Dval);
    arb_init(x); arb_init(y); arb_init(wexp); arb_init(lp); arb_init(r); arb_init(tol);
    arb_set_str(tol, "1e-40", prec);
    arb_set_ui(x, 53);
    zst_weil_dirichlet(&W, D, x, 50, prec);

    for (i = 0; i < 15; i++)
    {
        int found = 0;
        arb_log_ui(lp, tp[i], prec);
        /* expected weight -chi(p) log p / sqrt p */
        arb_sqrt_ui(r, tp[i], prec);
        arb_div(wexp, lp, r, prec);
        arb_mul_si(wexp, wexp, -truth[i], prec);
        for (j = 0; j < W.natoms; j++)
        {
            arb_sub(r, W.y + j, lp, prec);
            arb_abs(r, r);
            if (arb_lt(r, tol))
            {
                found = 1;
                arb_sub(r, W.w + j, wexp, prec);
                arb_abs(r, r);
                if (!arb_lt(r, tol))
                {
                    flint_printf("test_dirichlet: D = %wd, chi(%wu) atom weight ", Dval, tp[i]);
                    arb_printn(W.w + j, 20, 0);
                    flint_printf(", expected ");
                    arb_printn(wexp, 20, 0);
                    flint_printf("\n");
                    fails++;
                }
                break;
            }
        }
        if (!found)
        { flint_printf("test_dirichlet: D = %wd, no atom at log %wu\n", Dval, tp[i]); fails++; }
    }
    if (W.npoles != 0)
    { flint_printf("test_dirichlet: L(chi, s) has no pole term\n"); fails++; }
    if (fmpz_cmp_si(W.cond, Dval < 0 ? -Dval : Dval) != 0)
    { flint_printf("test_dirichlet: conductor should be |D|\n"); fails++; }

    zst_weil_clear(&W);
    fmpz_clear(D);
    arb_clear(x); arb_clear(y); arb_clear(wexp); arb_clear(lp); arb_clear(r); arb_clear(tol);
}

/* The same atom weights against FLINT's own Kronecker symbol (fmpz.h:616), for every prime
 * p <= 200 and eleven fundamental discriminants: an independent check of the convention. */
static void
test_kronecker_vs_flint(slong prec)
{
    static const slong Ds[11] = { -4, -3, 5, 8, -8, 13, -7, -11, 17, 21, -15 };
    zst_weil_t W;
    fmpz_t D, pz;
    arb_t x, lp, wexp, r, tol;
    n_primes_t iter;
    slong i, j, nchecked = 0;
    ulong p;

    fmpz_init(D); fmpz_init(pz);
    arb_init(x); arb_init(lp); arb_init(wexp); arb_init(r); arb_init(tol);
    arb_set_str(tol, "1e-40", prec);
    arb_set_ui(x, 211);

    for (i = 0; i < 11; i++)
    {
        fmpz_set_si(D, Ds[i]);
        zst_weil_dirichlet(&W, D, x, 200, prec);
        n_primes_init(iter);
        while ((p = n_primes_next(iter)) <= 200)
        {
            int want;
            fmpz_set_ui(pz, p);
            want = fmpz_kronecker(D, pz);
            arb_log_ui(lp, p, prec);
            arb_sqrt_ui(r, p, prec);
            arb_div(wexp, lp, r, prec);
            arb_mul_si(wexp, wexp, -want, prec);
            for (j = 0; j < W.natoms; j++)
            {
                arb_sub(r, W.y + j, lp, prec); arb_abs(r, r);
                if (arb_lt(r, tol))
                {
                    arb_sub(r, W.w + j, wexp, prec); arb_abs(r, r);
                    if (!arb_lt(r, tol))
                    {
                        flint_printf("test_dirichlet: D = %wd, p = %wu disagrees with "
                                     "fmpz_kronecker (= %d)\n", Ds[i], p, want);
                        fails++;
                    }
                    nchecked++;
                    break;
                }
            }
        }
        n_primes_clear(iter);
        zst_weil_clear(&W);
    }
    if (nchecked < 11 * 46)
    { flint_printf("test_dirichlet: only %wd kronecker checks\n", nchecked); fails++; }

    fmpz_clear(D); fmpz_clear(pz);
    arb_clear(x); arb_clear(lp); arb_clear(wexp); arb_clear(r); arb_clear(tol);
}

static void
test_ab_pins(slong prec)
{
    FILE *f = open_data("dirichlet_pins.txt");
    char line[4096], tag[32], va[256], vb[256];
    fmpz_t D;
    arb_t x, tol, ref, r;
    arb_ptr a = NULL, b = NULL;
    zst_weil_t W;
    slong N = -1, n, npins = 0, nblocks = 0;
    long Dl, Xl, xl, Nl;
    int built = 0;

    if (f == NULL) return;
    fmpz_init(D);
    arb_init(x); arb_init(tol); arb_init(ref); arb_init(r);
    arb_set_str(tol, "1e-40", prec);

    while (fgets(line, sizeof(line), f))
    {
        if (line[0] == '#' || line[0] == '\n') continue;
        if (sscanf(line, "%31s", tag) != 1) continue;
        if (strcmp(tag, "chi") == 0)
        {
            if (built) { zst_weil_clear(&W); _arb_vec_clear(a, N + 1); _arb_vec_clear(b, N + 1); built = 0; }
            if (sscanf(line, "%31s %ld %ld %ld %ld", tag, &Dl, &xl, &Xl, &Nl) != 5)
            { flint_printf("test_dirichlet: bad pin header\n"); fails++; break; }
            fmpz_set_si(D, Dl);
            N = Nl;
            arb_set_si(x, xl);
            a = _arb_vec_init(N + 1); b = _arb_vec_init(N + 1);
            zst_weil_dirichlet(&W, D, x, (ulong) Xl, prec);
            zst_weil_ab(a, b, N, &W, prec);
            built = 1; nblocks++;
            if (!arb_is_zero(b + 0)) { flint_printf("test_dirichlet: b_0 not exactly zero\n"); fails++; }
        }
        else if (strcmp(tag, "ab") == 0 && built)
        {
            if (sscanf(line, "%31s %ld %255s %255s", tag, &Nl, va, vb) != 4) continue;
            n = Nl;
            if (n < 0 || n > N) continue;
            arb_set_str(ref, va, prec);
            arb_sub(r, a + n, ref, prec); arb_abs(r, r);
            if (!arb_lt(r, tol))
            { flint_printf("test_dirichlet: D = %ld, a_%wd mismatch, got ", Dl, n);
              arb_printn(a + n, 30, 0); flint_printf(" pin %s\n", va); fails++; }
            arb_set_str(ref, vb, prec);
            arb_sub(r, b + n, ref, prec); arb_abs(r, r);
            if (!arb_lt(r, tol))
            { flint_printf("test_dirichlet: D = %ld, b_%wd mismatch, got ", Dl, n);
              arb_printn(b + n, 30, 0); flint_printf(" pin %s\n", vb); fails++; }
            npins++;
        }
    }
    fclose(f);
    if (built) { zst_weil_clear(&W); _arb_vec_clear(a, N + 1); _arb_vec_clear(b, N + 1); }
    if (nblocks < 6 || npins < 54)
    { flint_printf("test_dirichlet: only %wd blocks / %wd pins read\n", nblocks, npins); fails++; }
    fmpz_clear(D);
    arb_clear(x); arb_clear(tol); arb_clear(ref); arb_clear(r);
}

int main(void)
{
    slong prec = 400;
    test_chi_values(-4, chi_m4, prec);
    test_chi_values(-3, chi_m3, prec);
    test_chi_values(5, chi_p5, prec);
    test_kronecker_vs_flint(prec);
    test_ab_pins(prec);
    flint_cleanup();
    flint_printf("test_dirichlet: %s\n", fails ? "FAIL" : "PASS");
    return fails ? 1 : 0;
}
