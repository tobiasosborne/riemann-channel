/* Elliptic curves over Q: local point counts and the explicit-formula data of L(E, s).
 *
 * Formula sheet: notes/zeta-spectral-triples/ellcurve/astra-review.md, F1, F4, F5, F17.
 * Analytic normalisation (F1): L_an(E, s) = L_ar(E, s + 1/2),
 *   Lambda_an(E, s) = C_E^{s/2} Gamma_C(s + 1/2) L_an(E, s),  Gamma_C(v) = 2 (2 pi)^{-v} Gamma(v),
 * so the single gamma factor is (Q, d, kappa) = (1/(2 pi), 1, 1/2), i.e. mu = kappa + 1/2 = 1 (F6);
 * the constant 2 in Gamma_C is an s-independent factor and does not enter (F1).  Lambda_an is
 * entire: NO pole term, unlike zeta (F17).  The conductor enters only as + log C_E on every a_n (F8).
 *
 * The input is a GLOBAL MINIMAL integral Weierstrass model and its conductor, both taken from
 * tests/data/ell_ref.txt (PARI); nothing here computes or verifies minimality.
 */
#include <flint/ulong_extras.h>
#include <flint/nmod.h>
#include "zst.h"

/* F4 (H-COUNT, confirmed for minimal models by the review against PARI 2.17.2 for all p <= 2500 on
 * 11a1, 14a1, 37a1, 389a1, plus additive examples of conductor 32 and 36):
 *   A_p = #{(u, v) in F_p^2 : v^2 + a1 u v + a3 v = u^3 + a2 u^2 + a4 u + a6},  a_p = p - A_p,
 * the singular point included.  At a bad prime of a minimal model this gives a_p = 1, -1, 0 for
 * split multiplicative, non-split multiplicative and additive reduction respectively (the
 * nonsingular projective locus has p - 1, p + 1, p points and the rational singular point adds one).
 * The GENERAL Weierstrass equation is essential: it is also correct in characteristics 2 and 3,
 * where completing the square or the cube is not available.
 *
 * Done in O(p): for each u the equation is a quadratic in v,
 *   v^2 + B v - R = 0,  B = a1 u + a3,  R = u^3 + a2 u^2 + a4 u + a6,
 * whose number of roots is, for odd p, 1 + (disc/p) with disc = B^2 + 4R (Legendre symbol, = 0 when
 * p | disc); for p = 2 the two candidates v = 0, 1 are tried directly. */
slong
zst_ell_ap(const fmpz *ainvs, ulong p)
{
    nmod_t mod;
    ulong u, a1, a2, a3, a4, a6, A = 0;

    nmod_init(&mod, p);
    a1 = fmpz_fdiv_ui(ainvs + 0, p);
    a2 = fmpz_fdiv_ui(ainvs + 1, p);
    a3 = fmpz_fdiv_ui(ainvs + 2, p);
    a4 = fmpz_fdiv_ui(ainvs + 3, p);
    a6 = fmpz_fdiv_ui(ainvs + 4, p);

    if (p == 2)
    {
        ulong v;
        for (u = 0; u < 2; u++)
            for (v = 0; v < 2; v++)
            {
                ulong lhs = nmod_add(nmod_mul(v, v, mod),
                                     nmod_add(nmod_mul(nmod_mul(a1, u, mod), v, mod),
                                              nmod_mul(a3, v, mod), mod), mod);
                ulong rhs = nmod_add(nmod_mul(nmod_mul(u, u, mod), u, mod),
                                     nmod_add(nmod_mul(a2, nmod_mul(u, u, mod), mod),
                                              nmod_add(nmod_mul(a4, u, mod), a6, mod), mod), mod);
                A += (lhs == rhs);
            }
    }
    else
    {
        for (u = 0; u < p; u++)
        {
            ulong B = nmod_add(nmod_mul(a1, u, mod), a3, mod);
            ulong R = nmod_add(nmod_mul(nmod_add(nmod_mul(nmod_add(u, a2, mod), u, mod), a4, mod),
                                        u, mod), a6, mod);            /* ((u + a2) u + a4) u + a6 */
            ulong disc = nmod_add(nmod_mul(B, B, mod), nmod_mul(4 % p, R, mod), mod);
            if (disc == 0) A += 1;
            else A += 1 + n_jacobi((slong) disc, p);                  /* 2 if a square, 0 if not */
        }
    }

    return (slong) p - (slong) A;
}

/* F5 (H-LUCAS, confirmed): with alpha_p beta_p = p, alpha_p + beta_p = a_p at a good prime,
 *   good p (p does not divide C_E): t_0 = 2, t_1 = a_p, t_m = a_p t_{m-1} - p t_{m-2} = alpha^m + beta^m,
 *   bad p (degree-one or trivial Euler factor):  t_m = a_p^m,
 *   w_{p,m} = -t_m log p / p^m          (this is -c_m log p p^{-m/2} with c_m = t_m p^{-m/2}:
 *                                        the p^{-m/2} of the centred normalisation is essential,
 *                                        review "Correction ledger", first row),
 * placed at y = m log p, for all prime powers p^m <= X.  Atoms of weight zero (t_m = 0, e.g. m = 2
 * at a supersingular-like p, or every m at an additive prime) are kept: they cost nothing and keep
 * the atom count equal to the number of prime powers. */
void
zst_weil_ellcurve(zst_weil_t *W, const fmpz *ainvs, const fmpz_t C, const arb_t x, ulong X, slong prec)
{
    n_primes_t iter;
    ulong p, pm;
    slong j, natoms = 0, m, ap, tprev, tcur, raw;
    arb_t lp, t;

    /* count the prime powers 1 < p^m <= X */
    n_primes_init(iter);
    while ((p = n_primes_next(iter)) <= X)
        for (pm = p; pm <= X; pm *= p)
        {
            natoms++;
            if (pm > X / p) break;                 /* next multiplication would overflow past X */
        }
    n_primes_clear(iter);

    zst_weil_init(W, natoms, 1, 0, prec);
    arb_init(lp); arb_init(t);
    zst_window_L(W->L, x, prec);

    j = 0;
    n_primes_init(iter);
    while ((p = n_primes_next(iter)) <= X)
    {
        int good = (fmpz_fdiv_ui(C, p) != 0);
        ap = zst_ell_ap(ainvs, p);
        arb_log_ui(lp, p, prec);
        tprev = 2; tcur = ap;                      /* t_0, t_1 */
        raw = ap;
        for (m = 1, pm = p; pm <= X; m++)
        {
            arb_mul_ui(W->y + j, lp, (ulong) m, prec);            /* y = m log p */
            arb_mul_si(t, lp, raw, prec);
            arb_div_ui(t, t, pm, prec);
            arb_neg(W->w + j, t);                                 /* w = -t_m log p / p^m */
            j++;
            if (pm > X / p) break;
            pm *= p;
            if (good) { slong tn = ap * tcur - (slong) p * tprev; tprev = tcur; tcur = tn; raw = tcur; }
            else raw *= ap;                                       /* t_m = a_p^m */
        }
    }
    n_primes_clear(iter);

    /* Gamma_C(s + 1/2) as (Q, d, mu) = (1/(2 pi), 1, 1), multiplicity 1 (F6; equivalently
     * (2, 1) + (2, 2) by Legendre duplication, F7).  Coefficient -1, not -2. */
    arb_const_pi(W->Q + 0, prec);
    arb_mul_2exp_si(W->Q + 0, W->Q + 0, 1);
    arb_inv(W->Q + 0, W->Q + 0, prec);
    arb_one(W->d + 0);
    arb_one(W->mu + 0);
    W->mult[0] = 1;

    fmpz_set(W->cond, C);                                         /* + log C_E on every a_n (F8) */

    arb_clear(lp); arb_clear(t);
}
