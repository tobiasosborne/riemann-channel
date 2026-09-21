/* Window integrals I1, I2, I3 and the tail T of the exponential-series kernel rho_{d,mu}.
 *
 * Ground truth:
 *   - the formula sheet notes/zeta-spectral-triples/ellcurve/astra-review.md, F6, F8, F9, F13-F15
 *     (F7: rho_{1,1} = rho_{2,1} + rho_{2,2}, since Gamma_C(s+1/2) = Gamma_R(s+1/2) Gamma_R(s+3/2));
 *   - 50-digit mpmath quadrature of the DEFINING integrals in tests/data/kernel_pins.txt, produced by
 *     notes/zeta-spectral-triples/ellcurve/checks/kernel_pins.py (command in that file's header).
 * Tests:
 *   1. the duplication identity (1,1) = (2,1) + (2,2) for I1, I2, I3 and for T, at n = 0, 1, 5 and
 *      L = log 9, log 13 (balls agree within 1e-40 at 400 bits);
 *   2. every pin of tests/data/kernel_pins.txt, within 1e-40;
 *   3. the closed form F9, T_{1,1}(L) = -log(1 - e^{-L}).
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "zst.h"

static int fails = 0;

static void
check_close(const arb_t got, const arb_t want, const arb_t tol, const char *what)
{
    arb_t r;
    arb_init(r);
    arb_sub(r, got, want, 600);
    arb_abs(r, r);
    if (!arb_lt(r, tol))
    {
        flint_printf("test_kernel: %s mismatch, got ", what);
        arb_printn(got, 30, 0);
        flint_printf(" want ");
        arb_printn(want, 30, 0);
        flint_printf("\n");
        fails++;
    }
    arb_clear(r);
}

/* F7 (duplication): rho_{1,1} = rho_{2,1} + rho_{2,2}, hence the same for I1, I2, I3 and T. */
static void
test_duplication(slong prec, const arb_t tol)
{
    static const slong ns[3] = { 0, 1, 5 };
    static const ulong xs[2] = { 9, 13 };
    arb_t L, d1, m1, d2, ma, mb, x;
    arb_t Ia[3], Ib[3], Ic[3], Ta, Tb, Tc, s;
    slong i, j, k;

    arb_init(L); arb_init(d1); arb_init(m1); arb_init(d2); arb_init(ma); arb_init(mb); arb_init(x);
    arb_init(Ta); arb_init(Tb); arb_init(Tc); arb_init(s);
    for (k = 0; k < 3; k++) { arb_init(Ia[k]); arb_init(Ib[k]); arb_init(Ic[k]); }

    arb_one(d1); arb_one(m1);                 /* (d, mu) = (1, 1): Gamma_C(s + 1/2) */
    arb_set_ui(d2, 2); arb_one(ma); arb_set_ui(mb, 2);  /* (2, 1) and (2, 2) */

    for (i = 0; i < 2; i++)
    {
        arb_set_ui(x, xs[i]);
        zst_window_L(L, x, prec);
        for (j = 0; j < 3; j++)
        {
            zst_kernel_I123(Ia[0], Ia[1], Ia[2], ns[j], d1, m1, L, prec);
            zst_kernel_I123(Ib[0], Ib[1], Ib[2], ns[j], d2, ma, L, prec);
            zst_kernel_I123(Ic[0], Ic[1], Ic[2], ns[j], d2, mb, L, prec);
            for (k = 0; k < 3; k++)
            {
                arb_add(s, Ib[k], Ic[k], prec);
                check_close(Ia[k], s, tol, "duplication I");
            }
        }
        zst_kernel_tail(Ta, d1, m1, L, prec);
        zst_kernel_tail(Tb, d2, ma, L, prec);
        zst_kernel_tail(Tc, d2, mb, L, prec);
        arb_add(s, Tb, Tc, prec);
        check_close(Ta, s, tol, "duplication T");
        /* F9: T_{1,1}(L) = -log(1 - e^{-L}) */
        arb_neg(s, L); arb_exp(s, s, prec); arb_neg(s, s);
        arb_log1p(s, s, prec); arb_neg(s, s);
        check_close(Ta, s, tol, "F9 closed-form tail");
    }

    for (k = 0; k < 3; k++) { arb_clear(Ia[k]); arb_clear(Ib[k]); arb_clear(Ic[k]); }
    arb_clear(L); arb_clear(d1); arb_clear(m1); arb_clear(d2); arb_clear(ma); arb_clear(mb); arb_clear(x);
    arb_clear(Ta); arb_clear(Tb); arb_clear(Tc); arb_clear(s);
}

/* Every line of tests/data/kernel_pins.txt. */
static void
test_pins(slong prec, const arb_t tol)
{
    FILE *f;
    char line[1024], tag[16], ds[64], mus[64], v[3][256];
    slong n, npins = 0;
    ulong X;
    arb_t d, mu, L, x, I[3], T, ref;

    f = fopen("tests/data/kernel_pins.txt", "r");
    if (f == NULL) f = fopen("../tests/data/kernel_pins.txt", "r");
    if (f == NULL)
    {
        flint_printf("test_kernel: cannot open tests/data/kernel_pins.txt\n");
        fails++;
        return;
    }
    arb_init(d); arb_init(mu); arb_init(L); arb_init(x); arb_init(T); arb_init(ref);
    for (n = 0; n < 3; n++) arb_init(I[n]);

    while (fgets(line, sizeof(line), f))
    {
        if (line[0] == '#' || line[0] == '\n') continue;
        if (sscanf(line, "%15s", tag) != 1) continue;
        if (strcmp(tag, "i123") == 0)
        {
            if (sscanf(line, "%15s %63s %63s %ld %lu %255s %255s %255s",
                       tag, ds, mus, (long *) &n, &X, v[0], v[1], v[2]) != 8) continue;
            arb_set_str(d, ds, prec); arb_set_str(mu, mus, prec);
            arb_set_ui(x, X); zst_window_L(L, x, prec);
            zst_kernel_I123(I[0], I[1], I[2], n, d, mu, L, prec);
            for (X = 0; X < 3; X++)
            {
                arb_set_str(ref, v[X], prec);
                check_close(I[X], ref, tol, "I123 pin");
            }
            npins += 3;
        }
        else if (strcmp(tag, "tail") == 0)
        {
            if (sscanf(line, "%15s %63s %63s %lu %255s", tag, ds, mus, &X, v[0]) != 5) continue;
            arb_set_str(d, ds, prec); arb_set_str(mu, mus, prec);
            arb_set_ui(x, X); zst_window_L(L, x, prec);
            zst_kernel_tail(T, d, mu, L, prec);
            arb_set_str(ref, v[0], prec);
            check_close(T, ref, tol, "tail pin");
            npins++;
        }
    }
    fclose(f);
    if (npins < 40) { flint_printf("test_kernel: only %wd pins read\n", npins); fails++; }
    for (n = 0; n < 3; n++) arb_clear(I[n]);
    arb_clear(d); arb_clear(mu); arb_clear(L); arb_clear(x); arb_clear(T); arb_clear(ref);
}

int main(void)
{
    slong prec = 400;
    arb_t tol;
    arb_init(tol);
    arb_set_str(tol, "1e-40", prec);

    test_duplication(prec, tol);
    test_pins(prec, tol);

    arb_clear(tol);
    flint_cleanup();
    flint_printf("test_kernel: %s\n", fails ? "FAIL" : "PASS");
    return fails ? 1 : 0;
}
