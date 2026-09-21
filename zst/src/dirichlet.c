/* Real primitive Dirichlet characters chi_D through the generic explicit-formula data model.
 *
 * D is a fundamental discriminant and chi_D(n) = (D/n) the Kronecker symbol, a real primitive
 * character modulo |D|.  Its completed L-function in the analytic (centred) normalisation is
 *   Lambda(chi, s) = |D|^{s/2} Gamma_R(s + kappa) L(chi, s + 1/2),
 *   Gamma_R(v) = pi^{-v/2} Gamma(v/2),   kappa = 0 for D > 0 (even chi), 1 for D < 0 (odd chi),
 * entire for chi non-principal (no pole term, unlike zeta: F17).  In the data model (F6) the gamma
 * factor Q^s Gamma((s + kappa)/d) is (Q, d, mu) = (pi^{-1/2}, 2, kappa + 1/2), and the conductor |D|
 * enters as + log|D| on every a_n (F8).  The atoms are F5 with the Satake power sums of the
 * degree-one Euler factor: t_m = chi(p)^m, so
 *   w_{p,m} = -chi(p)^m log p * p^{-m/2}   at y = m log p,   for all prime powers p^m <= X,
 * zero exactly at p | D.  (D = 1 gives back zeta's atoms, but not zeta's pole term.)
 *
 * Formula sheet: notes/zeta-spectral-triples/ellcurve/astra-review.md, F2, F5, F6, F8, F16, F17,
 * and its recommendation 1 (the real character is the implementation control for the generic
 * archimedean builder: degree one, no point counting, no pole).
 */
#include <flint/ulong_extras.h>
#include "zst.h"

/* The Kronecker symbol (D/p) for a PRIME p, from the definition.  FLINT 3.0.1 does have
 * fmpz_kronecker (fmpz.h:616); it is written out here so that the convention in use is explicit and
 * auditable, and tests/test_dirichlet.c checks this against both hard-coded truth and
 * fmpz_kronecker.  For odd p it is the Legendre symbol of D mod p, computed by n_jacobi; for p = 2
 * it is 0 if D is even, +1 if D = +-1 (mod 8), -1 if D = +-3 (mod 8). */
static int
kronecker_prime(const fmpz_t D, ulong p)
{
    ulong r;

    if (p == 2)
    {
        r = fmpz_fdiv_ui(D, 8);
        if (r % 2 == 0) return 0;
        return (r == 1 || r == 7) ? 1 : -1;
    }
    r = fmpz_fdiv_ui(D, p);
    if (r == 0) return 0;
    return n_jacobi((slong) r, p);
}

void
zst_weil_dirichlet(zst_weil_t *W, const fmpz_t D, const arb_t x, ulong X, slong prec)
{
    n_primes_t iter;
    ulong p, pm;
    slong j, m, natoms = 0;
    int kappa, c, t;
    arb_t lp, u;
    fmpz_t absD;

    /* count the prime powers 1 < p^m <= X (zero-weight atoms at p | D are kept) */
    n_primes_init(iter);
    while ((p = n_primes_next(iter)) <= X)
        for (pm = p; pm <= X; pm *= p)
        {
            natoms++;
            if (pm > X / p) break;
        }
    n_primes_clear(iter);

    zst_weil_init(W, natoms, 1, 0, prec);
    arb_init(lp); arb_init(u);
    fmpz_init(absD);
    zst_window_L(W->L, x, prec);

    j = 0;
    n_primes_init(iter);
    while ((p = n_primes_next(iter)) <= X)
    {
        c = kronecker_prime(D, p);
        arb_log_ui(lp, p, prec);
        t = c;                                            /* t_m = chi(p)^m, t_1 = chi(p) */
        for (m = 1, pm = p; pm <= X; m++)
        {
            arb_mul_ui(W->y + j, lp, (ulong) m, prec);    /* y = m log p */
            arb_sqrt_ui(u, pm, prec);
            arb_div(W->w + j, lp, u, prec);
            arb_mul_si(W->w + j, W->w + j, -t, prec);     /* w = -chi(p)^m log p p^{-m/2} */
            j++;
            if (pm > X / p) break;
            pm *= p;
            t *= c;
        }
    }
    n_primes_clear(iter);

    /* Gamma_R(s + kappa): Q = pi^{-1/2}, d = 2, mu = kappa + 1/2 (F6). */
    kappa = fmpz_sgn(D) > 0 ? 0 : 1;
    arb_const_pi(W->Q + 0, prec);
    arb_rsqrt(W->Q + 0, W->Q + 0, prec);
    arb_set_ui(W->d + 0, 2);
    arb_set_ui(W->mu + 0, 2 * (ulong) kappa + 1);
    arb_mul_2exp_si(W->mu + 0, W->mu + 0, -1);            /* mu = kappa + 1/2 */
    W->mult[0] = 1;

    fmpz_abs(absD, D);
    fmpz_set(W->cond, absD);                              /* conductor |D| (F8) */

    arb_clear(lp); arb_clear(u);
    fmpz_clear(absD);
}
