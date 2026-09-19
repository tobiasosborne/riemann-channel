/* Fuzz harness for zst_secular_roots / zst_secular_eval.
 * Input bytes -> N in [1, 12], N+1 signed 16-bit coefficients (scaled), precision in {128, 192, 256}.
 * Invariants checked (abort on violation, which libFuzzer reports as a crash):
 *   - the returned count is between 0 and N and every returned root is a certified zero of h_j;
 *   - returned roots are increasing and pairwise disjoint;
 *   - no non-finite balls.
 * Build: make fuzz  (clang, -fsanitize=fuzzer,address). Without libFuzzer, `make fuzz-plain` builds a
 * seeded random driver from the same body (ZST_PLAIN_FUZZ). */
#include <stdint.h>
#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "zst.h"

int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)
{
    slong N, prec, k, n, unres;
    arb_ptr xi, roots;
    arb_t sum, val, der;
    if (size < 4) return 0;
    N = 1 + (data[0] % 12);
    prec = 128 + 64 * (data[1] % 3);
    if (size < 2 + 2 * (size_t) (N + 1)) return 0;
    xi = _arb_vec_init(N + 1); roots = _arb_vec_init(N);
    arb_init(sum); arb_init(val); arb_init(der);
    for (k = 0; k <= N; k++)
    {
        int16_t c; memcpy(&c, data + 2 + 2 * k, 2);
        arb_set_si(xi + k, c);
        arb_mul_2exp_si(xi + k, xi + k, -(slong) (k * 2));    /* decaying coefficients, arbitrary signs */
    }
    arb_set(sum, xi + 0);
    for (k = 1; k <= N; k++) { arb_add(sum, sum, xi + k, prec); arb_add(sum, sum, xi + k, prec); }
    if (arb_contains_zero(sum)) goto done;                    /* normalisation impossible */
    for (k = 0; k <= N; k++) arb_div(xi + k, xi + k, sum, prec);

    n = zst_secular_roots(roots, N, &unres, xi, N, prec);
    if (n < 0 || n > N) abort();
    for (k = 0; k < n; k++)
    {
        slong j;
        if (!arb_is_finite(roots + k)) abort();
        if (!arb_is_positive(roots + k)) abort();
        j = (slong) arf_get_d(arb_midref(roots + k), ARF_RND_DOWN);
        if (j > N) j = N;
        zst_secular_eval(val, der, roots + k, xi, N, j, prec);
        if (!arb_contains_zero(val)) abort();
        if (k > 0 && !arb_lt(roots + k - 1, roots + k)) abort();
    }
done:
    _arb_vec_clear(xi, N + 1); _arb_vec_clear(roots, N);
    arb_clear(sum); arb_clear(val); arb_clear(der);
    return 0;
}

#ifdef ZST_PLAIN_FUZZ
int main(int argc, char **argv)
{
    unsigned long iters = (argc > 1) ? strtoul(argv[1], NULL, 10) : 2000, it;
    unsigned seed = (argc > 2) ? (unsigned) strtoul(argv[2], NULL, 10) : 12345u;
    uint8_t buf[64];
    srand(seed);
    for (it = 0; it < iters; it++)
    {
        size_t i, n = 4 + (size_t) (rand() % 60);
        for (i = 0; i < n; i++) buf[i] = (uint8_t) (rand() & 0xff);
        LLVMFuzzerTestOneInput(buf, n);
    }
    flint_cleanup();
    printf("fuzz_secular (plain): %lu inputs, no invariant violated\n", iters);
    return 0;
}
#endif
