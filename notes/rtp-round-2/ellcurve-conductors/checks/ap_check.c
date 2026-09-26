/* claude:opus 2026-09-26: print zst_ell_ap (zst's own point count on the minimal model, which the
 * driver uses) for primes p < 200, for each curve of ell_ref_ext.txt; compared with PARI ellap by
 * checks/ap_compare.py. Build: cc -O2 -I../../../../zst/include ap_check.c ../../../../zst/build/libzst.a -lflint -lmpfr -lgmp -lm */
#include <stdio.h>
#include <flint/fmpz_vec.h>
#include "zst.h"
int main(int argc, char **argv)
{
    const char *path = argv[1];
    for (int c = 2; c < argc; c++)
    {
        fmpz *ai = _fmpz_vec_init(5); fmpz_t C; fmpz_init(C); int w; slong rank;
        if (!zst_ell_ref(ai, C, &w, &rank, NULL, 0, argv[c], path, 128)) { printf("%s MISSING\n", argv[c]); return 1; }
        printf("%s", argv[c]);
        for (ulong p = 2; p < 200; p++) { int pr = 1; for (ulong d = 2; d * d <= p; d++) if (p % d == 0) pr = 0; if (pr) printf("%s%ld", p == 2 ? " " : ",", (long) zst_ell_ap(ai, p)); }
        printf("\n"); _fmpz_vec_clear(ai, 5); fmpz_clear(C);
    }
    return 0;
}
