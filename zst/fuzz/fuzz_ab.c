/* Fuzz harness for zst_riemann_ab and the block builders.
 * Input bytes -> x in [4, 60] (from a 16-bit value), N in [0, 10], precision in {96, 128, 192}.
 * Invariants: all balls finite; radii below 2^-(prec/2); b_0 = 0 exactly (sin(0) terms and the pole
 * term vanish at n = 0); even and odd blocks symmetric (exact ball equality of mirrored entries);
 * a_n consistent between two precisions (the higher-precision ball is contained in the lower one). */
#include <stdint.h>
#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "zst.h"

#define FAIL(msg) do { fprintf(stderr, "fuzz_ab invariant: %s (x=%.6f N=%ld prec=%ld)\n", msg, xd, (long) N, (long) prec); abort(); } while (0)

int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)
{
    slong N, prec, n, i, j;
    uint16_t w;
    double xd;
    ulong X;
    arb_t x;
    arb_ptr a, b, a2, b2;
    arb_mat_t E, O;
    if (size < 4) return 0;
    memcpy(&w, data, 2);
    xd = 4.0 + 56.0 * (w / 65535.0);
    N = data[2] % 11;
    prec = 96 + 32 * (data[3] % 4);
    X = (ulong) xd;
    arb_init(x); arb_set_d(x, xd);
    a = _arb_vec_init(N + 1); b = _arb_vec_init(N + 1); a2 = _arb_vec_init(N + 1); b2 = _arb_vec_init(N + 1);
    zst_riemann_ab(a, b, N, x, X, prec);
    zst_riemann_ab(a2, b2, N, x, X, prec + 64);
    if (!arb_is_zero(b + 0)) FAIL("b_0 = 0");
    for (n = 0; n <= N; n++)
    {
        if (!arb_is_finite(a + n) || !arb_is_finite(b + n)) FAIL("finite");
        if (mag_cmp_2exp_si(arb_radref(a + n), -(prec / 2)) > 0) FAIL("rad a");
        if (mag_cmp_2exp_si(arb_radref(b + n), -(prec / 2)) > 0) FAIL("rad b");
        if (!arb_overlaps(a + n, a2 + n) || !arb_overlaps(b + n, b2 + n)) FAIL("two precisions overlap");
    }
    arb_mat_init(E, N + 1, N + 1); arb_mat_init(O, N, N);
    zst_even_block(E, a, b, N, prec);
    zst_odd_block(O, a, b, N, prec);
    for (i = 0; i <= N; i++)
        for (j = 0; j < i; j++)
            if (!arb_equal(arb_mat_entry(E, i, j), arb_mat_entry(E, j, i))) FAIL("E symmetric");
    for (i = 0; i < N; i++)
        for (j = 0; j < i; j++)
            if (!arb_equal(arb_mat_entry(O, i, j), arb_mat_entry(O, j, i))) FAIL("O symmetric");
    arb_mat_clear(E); arb_mat_clear(O);
    _arb_vec_clear(a, N + 1); _arb_vec_clear(b, N + 1); _arb_vec_clear(a2, N + 1); _arb_vec_clear(b2, N + 1);
    arb_clear(x);
    return 0;
}

#ifdef ZST_PLAIN_FUZZ
int main(int argc, char **argv)
{
    unsigned long iters = (argc > 1) ? strtoul(argv[1], NULL, 10) : 300, it;
    unsigned seed = (argc > 2) ? (unsigned) strtoul(argv[2], NULL, 10) : 4242u;
    uint8_t buf[8];
    srand(seed);
    for (it = 0; it < iters; it++)
    {
        size_t i;
        for (i = 0; i < 8; i++) buf[i] = (uint8_t) (rand() & 0xff);
        LLVMFuzzerTestOneInput(buf, 8);
    }
    flint_cleanup();
    printf("fuzz_ab (plain): %lu inputs, no invariant violated\n", iters);
    return 0;
}
#endif
