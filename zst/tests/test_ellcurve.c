/* Elliptic-curve instance of the generic data model.
 *
 * 1. zst_ell_ap (F4: naive count of the affine F_p-points of the GENERAL Weierstrass equation,
 *    singular point included, a_p = p - A_p) against every 'ap p a_p' line of tests/data/ell_ref.txt
 *    (PARI 2.17.2 via tools/pari_ref.py: all primes <= 2500 on 11a1, 14a1, 37a1, 389a1).  This
 *    covers good primes, both multiplicative types (a_11 = +1 for 11a1 split, a_37 = -1 for 37a1
 *    non-split, a_2 = -1 and a_7 = +1 for 14a1) and p = 2, 3.
 * 2. (a_n, b_n) of zst_weil_ellcurve + zst_weil_ab for 11a1 at x = X = 13, N = 8, against the
 *    50-digit pins of tests/data/ell_pins_11a1_x13_N8.txt, produced by the review lane's
 *    INDEPENDENT mpmath prototype notes/zeta-spectral-triples/ellcurve/checks/ell_check.py through
 *    checks/ell_pins.py (command in the pin file's header).  Tolerance 1e-40 at 400 bits.
 * Formula sheet: notes/zeta-spectral-triples/ellcurve/astra-review.md, F1, F4, F5, F9, F16, F17.
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <flint/fmpz_vec.h>
#include "zst.h"

static int fails = 0;

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
    if (f == NULL) { flint_printf("test_ellcurve: cannot open tests/data/%s\n", name); fails++; }
    return f;
}

/* Parse "a1,a2,a3,a4,a6" into five fmpz. */
static void
parse_ainvs(fmpz *ainvs, const char *s)
{
    char buf[256], *p, *q;
    slong i;
    strncpy(buf, s, sizeof(buf) - 1);
    buf[sizeof(buf) - 1] = '\0';
    p = buf;
    for (i = 0; i < 5; i++)
    {
        q = strchr(p, ',');
        if (q != NULL) *q = '\0';
        fmpz_set_str(ainvs + i, p, 10);
        p = (q != NULL) ? q + 1 : p + strlen(p);
    }
}

static void
test_ap(void)
{
    FILE *f = open_data("ell_ref.txt");
    char line[1024], tag[32], label[64], models[256];
    fmpz *ainvs = _fmpz_vec_init(5);
    slong nap = 0, ncurves = 0;
    long C, w, rank, ap;
    ulong p;
    int have = 0;

    if (f == NULL) { _fmpz_vec_clear(ainvs, 5); return; }
    while (fgets(line, sizeof(line), f))
    {
        if (line[0] == '#' || line[0] == '\n') continue;
        if (sscanf(line, "%31s", tag) != 1) continue;
        if (strcmp(tag, "curve") == 0)
        {
            if (sscanf(line, "%31s %63s %255s %ld %ld %ld", tag, label, models, &C, &w, &rank) != 6)
            { flint_printf("test_ellcurve: bad curve line\n"); fails++; continue; }
            parse_ainvs(ainvs, models);
            have = 1; ncurves++;
        }
        else if (strcmp(tag, "ap") == 0 && have)
        {
            slong got;
            if (sscanf(line, "%31s %lu %ld", tag, &p, &ap) != 3) continue;
            got = zst_ell_ap(ainvs, p);
            if (got != (slong) ap)
            {
                flint_printf("test_ellcurve: %s a_%wu = %wd, PARI says %ld\n", label, p, got, ap);
                fails++;
            }
            nap++;
        }
    }
    fclose(f);
    if (ncurves < 4 || nap < 1400)
    { flint_printf("test_ellcurve: only %wd curves / %wd a_p read\n", ncurves, nap); fails++; }
    else
        flint_printf("test_ellcurve: %wd a_p on %wd curves match PARI\n", nap, ncurves);
    _fmpz_vec_clear(ainvs, 5);
}

static void
test_ab_pins(slong prec)
{
    FILE *f = open_data("ell_pins_11a1_x13_N8.txt");
    char line[1024], tag[32], label[64], models[256], va[256], vb[256];
    fmpz *ainvs = _fmpz_vec_init(5);
    fmpz_t C;
    arb_t x, tol, ref, r;
    arb_ptr a = NULL, b = NULL;
    zst_weil_t W;
    slong N = -1, n, npins = 0;
    long Cl, Xl, xl, Nl;
    int built = 0;

    if (f == NULL) { _fmpz_vec_clear(ainvs, 5); return; }
    fmpz_init(C);
    arb_init(x); arb_init(tol); arb_init(ref); arb_init(r);
    arb_set_str(tol, "1e-40", prec);

    while (fgets(line, sizeof(line), f))
    {
        if (line[0] == '#' || line[0] == '\n') continue;
        if (sscanf(line, "%31s", tag) != 1) continue;
        if (strcmp(tag, "curve") == 0)
        {
            if (sscanf(line, "%31s %63s %255s %ld %ld %ld %ld",
                       tag, label, models, &Cl, &xl, &Xl, &Nl) != 7)
            { flint_printf("test_ellcurve: bad pin header\n"); fails++; break; }
            parse_ainvs(ainvs, models);
            fmpz_set_si(C, Cl);
            N = Nl;
            arb_set_si(x, xl);
            a = _arb_vec_init(N + 1); b = _arb_vec_init(N + 1);
            zst_weil_ellcurve(&W, ainvs, C, x, (ulong) Xl, prec);
            zst_weil_ab(a, b, N, &W, prec);
            built = 1;
        }
        else if (strcmp(tag, "ab") == 0 && built)
        {
            if (sscanf(line, "%31s %ld %255s %255s", tag, &Nl, va, vb) != 4) continue;
            n = Nl;
            if (n < 0 || n > N) continue;
            arb_set_str(ref, va, prec);
            arb_sub(r, a + n, ref, prec); arb_abs(r, r);
            if (!arb_lt(r, tol))
            { flint_printf("test_ellcurve: a_%wd mismatch, got ", n); arb_printn(a + n, 30, 0);
              flint_printf(" pin %s\n", va); fails++; }
            arb_set_str(ref, vb, prec);
            arb_sub(r, b + n, ref, prec); arb_abs(r, r);
            if (!arb_lt(r, tol))
            { flint_printf("test_ellcurve: b_%wd mismatch, got ", n); arb_printn(b + n, 30, 0);
              flint_printf(" pin %s\n", vb); fails++; }
            npins++;
        }
    }
    fclose(f);
    if (npins < 9) { flint_printf("test_ellcurve: only %wd (a,b) pins read\n", npins); fails++; }
    if (built)
    {
        if (W.npoles != 0) { flint_printf("test_ellcurve: E/Q must have no pole term (F17)\n"); fails++; }
        if (!arb_is_zero(b + 0)) { flint_printf("test_ellcurve: b_0 not exactly zero\n"); fails++; }
        zst_weil_clear(&W);
        _arb_vec_clear(a, N + 1); _arb_vec_clear(b, N + 1);
    }
    fmpz_clear(C);
    arb_clear(x); arb_clear(tol); arb_clear(ref); arb_clear(r);
    _fmpz_vec_clear(ainvs, 5);
}

int main(void)
{
    test_ap();
    test_ab_pins(400);
    flint_cleanup();
    flint_printf("test_ellcurve: %s\n", fails ? "FAIL" : "PASS");
    return fails ? 1 : 0;
}
