/* Loewner data (a_n, b_n) of the truncated Weil quadratic form of zeta.
 *
 * Ground truth: Connes-Consani-Moscovici, arXiv:2511.22755, local copy
 * refs/src/2511.22755/mc2arXiv.tex (sha256 in refs/manifest.sha256), cited by line:
 *   basis U_n, V_n and the window: eqs. (expbasis) l.353, (toa) l.498, (vN) l.560;
 *   q(U_n,U_m): eqs. (symrealmn1) l.375, (symrealn1) l.387;
 *   Loewner form tau_{nm} = (b_n - b_m)/(n - m), tau_{nn} = a_n: Lemma `basicexpli`, eq. (form) l.817-819,
 *     b_n = -(1/pi) int sin(2 pi n y/L) D(y), a_n = 2 int (1 - y/L) cos(2 pi n y/L) D(y);
 *   distribution D = log_*(Psi^#), Psi^# = W_{0,2}^# - W_R^# - sum W_p^#: eq. (psipsisharp) l.484-492;
 *   pole term: Lemma `w02`, eq. (hh) l.685 (its Loewner data b^(02), a^(02) is derived in plan.md 1.2);
 *   prime term: eq. (bomp) l.693;
 *   archimedean term: eq. (weinfty) l.709, Prop. `computearch` l.720-771 (digamma/trigamma and
 *     e^{-2L}-series forms of the three integrals), alpha_L, beta_L, gamma_L l.788-791, Prop.
 *     `bigmatrix` l.794-798, w(L) l.781.
 *   Correction: the displayed c(L) (l.777) is not the correction the identity (corectc) l.773 needs;
 *     the correct one is C(L) = int_0^L (1 - e^{-x/2}) rho(x) dx (closed form below, checked by
 *     quadrature in ccm_proto.py). The difference is n-independent (a multiple of the identity).
 * Formula sheet: notes/zeta-spectral-triples/plan.md Section 1.2. */
#include <math.h>
#include <flint/ulong_extras.h>
#include <flint/acb.h>
#include <flint/mag.h>
#include "zst.h"

void zst_window_L(arb_t L, const arb_t x, slong prec)
{
    arb_log(L, x, prec);
}

/* S1 = sum_{k>=0} z^k/(k + A), S2 = sum z^k/(k + A)^2 (A complex, Re A = 1/4), S10 = sum z^k/(k + 1/4),
 * with rigorous geometric tail bounds. */
static void
lerch_sums(acb_t S1, acb_t S2, arb_t S10, const acb_t A, const arb_t z, slong prec)
{
    slong K, k;
    acb_t zk, t, kA;
    arb_t q, u;
    mag_t zmag, tail, den;
    double zd;

    acb_init(zk); acb_init(t); acb_init(kA);
    arb_init(q); arb_init(u);
    mag_init(zmag); mag_init(tail); mag_init(den);

    zd = arf_get_d(arb_midref(z), ARF_RND_UP);
    if (zd <= 0 || zd >= 1) { flint_printf("lerch_sums: z out of range\n"); flint_abort(); }
    /* z^K ~ 2^-prec */
    K = (slong) (prec * 0.6931471805599453 / (-log(zd))) + 4;

    acb_zero(S1); acb_zero(S2); arb_zero(S10);
    acb_one(zk);
    for (k = 0; k < K; k++)
    {
        acb_add_ui(kA, A, k, prec);
        acb_div(t, zk, kA, prec);
        acb_add(S1, S1, t, prec);
        acb_div(t, t, kA, prec);
        acb_add(S2, S2, t, prec);
        arb_set_d(q, 0.25); arb_add_ui(q, q, k, prec);
        arb_div(u, acb_realref(zk), q, prec);
        arb_add(S10, S10, u, prec);
        acb_mul_arb(zk, zk, z, prec);
    }
    /* tails: |sum_{k>=K} z^k/(k+A)^r| <= (sum_{k>=K} z^k) / K^r  since |k + A| >= k >= K */
    arb_get_mag(zmag, z);
    mag_geom_series(tail, zmag, K);
    mag_set_ui_lower(den, K);
    mag_div(tail, tail, den);
    acb_add_error_mag(S1, tail);
    arb_add_error_mag(S10, tail);
    mag_div(tail, tail, den);
    acb_add_error_mag(S2, tail);

    acb_clear(zk); acb_clear(t); acb_clear(kA);
    arb_clear(q); arb_clear(u);
    mag_clear(zmag); mag_clear(tail); mag_clear(den);
}

void zst_riemann_ab(arb_ptr a, arb_ptr b, slong N, const arb_t x, ulong X, slong prec)
{
    arb_t L, z, e, K2, wL, CL, pi, t, u, v, omega, den, I1, I2, I3, S10, sn, cs, lk, lp;
    acb_t A, psi, psi1, S1, S2, one;
    slong n;
    ulong k;
    /* prime powers 1 < k <= X: positions log k and weights Lambda(k) k^{-1/2} */
    slong npp = 0;
    arb_ptr ppy, ppw;

    arb_init(L); arb_init(z); arb_init(e); arb_init(K2); arb_init(wL); arb_init(CL); arb_init(pi);
    arb_init(t); arb_init(u); arb_init(v); arb_init(omega); arb_init(den);
    arb_init(I1); arb_init(I2); arb_init(I3); arb_init(S10); arb_init(sn); arb_init(cs);
    arb_init(lk); arb_init(lp);
    acb_init(A); acb_init(psi); acb_init(psi1); acb_init(S1); acb_init(S2); acb_init(one);
    acb_one(one);

    arb_const_pi(pi, prec);
    zst_window_L(L, x, prec);
    arb_mul_si(z, L, -2, prec); arb_exp(z, z, prec);          /* z = e^{-2L} */
    arb_mul_2exp_si(e, L, -1); arb_neg(e, e); arb_exp(e, e, prec); /* e = e^{-L/2} */
    /* K2 = 32 L sinh^2(L/4) */
    arb_mul_2exp_si(t, L, -2); arb_sinh(t, t, prec); arb_sqr(t, t, prec);
    arb_mul(K2, t, L, prec); arb_mul_ui(K2, K2, 32, prec);
    /* w(L) = (gamma + log 4 pi)/2 - (1/2) log((e^L + 1)/(e^L - 1)) */
    arb_const_euler(wL, prec);
    arb_mul_ui(t, pi, 4, prec); arb_log(t, t, prec); arb_add(wL, wL, t, prec);
    arb_exp(t, L, prec); arb_add_ui(u, t, 1, prec); arb_sub_ui(v, t, 1, prec);
    arb_div(u, u, v, prec); arb_log(u, u, prec); arb_sub(wL, wL, u, prec);
    arb_mul_2exp_si(wL, wL, -1);
    /* C(L) = -log(t+1) + (1/2) log(t^2+1) + atan t + (1/2) log 2 - pi/4,  t = e^{L/2} */
    arb_mul_2exp_si(t, L, -1); arb_exp(t, t, prec);
    arb_add_ui(u, t, 1, prec); arb_log(u, u, prec); arb_neg(CL, u);
    arb_sqr(u, t, prec); arb_add_ui(u, u, 1, prec); arb_log(u, u, prec); arb_mul_2exp_si(u, u, -1);
    arb_add(CL, CL, u, prec);
    arb_atan(u, t, prec); arb_add(CL, CL, u, prec);
    arb_const_log2(u, prec); arb_mul_2exp_si(u, u, -1); arb_add(CL, CL, u, prec);
    arb_mul_2exp_si(u, pi, -2); arb_sub(CL, CL, u, prec);

    /* prime powers 1 < k <= X: count, then fill exactly npp slots (no slack: an over-read is a bug) */
    for (k = 2; k <= X; k++)
    {
        n_factor_t f;
        n_factor_init(&f);
        n_factor(&f, k, 1);
        npp += (f.num == 1);
    }
    ppy = _arb_vec_init(npp); ppw = _arb_vec_init(npp);
    npp = 0;
    for (k = 2; k <= X; k++)
    {
        n_factor_t f;
        n_factor_init(&f);
        n_factor(&f, k, 1);
        if (f.num == 1)
        {
            arb_log_ui(ppy + npp, k, prec);                    /* log k */
            arb_log_ui(lp, f.p[0], prec);                      /* Lambda(k) = log p */
            arb_sqrt_ui(t, k, prec);
            arb_div(ppw + npp, lp, t, prec);                   /* log p / sqrt k */
            npp++;
        }
    }

    for (n = 0; n <= N; n++)
    {
        slong i;
        /* omega = 2 pi n / L;  A = 1/4 - i pi n / L */
        arb_mul_ui(omega, pi, 2 * (ulong) n, prec); arb_div(omega, omega, L, prec);
        arb_set_d(t, 0.25); arb_set(acb_realref(A), t);
        arb_mul_ui(t, pi, (ulong) n, prec); arb_div(t, t, L, prec); arb_neg(acb_imagref(A), t);

        acb_digamma(psi, A, prec);
        acb_polygamma(psi1, one, A, prec);
        lerch_sums(S1, S2, S10, A, z, prec);

        /* I1 = -(1/2) Im psi - (e/2) Im S1 */
        arb_mul(t, e, acb_imagref(S1), prec);
        arb_add(I1, acb_imagref(psi), t, prec);
        arb_mul_2exp_si(I1, I1, -1); arb_neg(I1, I1);
        /* I2 = -(L e/2) Re S1 + (1/4) Re psi1 - (e/4) Re S2 */
        arb_mul(t, L, e, prec); arb_mul(t, t, acb_realref(S1), prec); arb_mul_2exp_si(t, t, -1);
        arb_neg(I2, t);
        arb_mul_2exp_si(t, acb_realref(psi1), -2); arb_add(I2, I2, t, prec);
        arb_mul(t, e, acb_realref(S2), prec); arb_mul_2exp_si(t, t, -2); arb_sub(I2, I2, t, prec);
        /* I3 = (1/2)[psi(1/4) - Re psi] - (e/2) Re S1 + (e/2) S10 */
        arb_set_d(t, 0.25); arb_digamma(t, t, prec);
        arb_sub(I3, t, acb_realref(psi), prec); arb_mul_2exp_si(I3, I3, -1);
        arb_sub(t, S10, acb_realref(S1), prec); arb_mul(t, t, e, prec); arb_mul_2exp_si(t, t, -1);
        arb_add(I3, I3, t, prec);

        /* pole term: den = L^2 + 16 pi^2 n^2 */
        arb_mul_ui(t, pi, 4 * (ulong) n, prec); arb_sqr(t, t, prec);
        arb_sqr(den, L, prec); arb_add(den, den, t, prec);
        /* b = K2 n / den */
        arb_mul_ui(b + n, K2, (ulong) n, prec); arb_div(b + n, b + n, den, prec);
        /* a = K2 (L^2 - 16 pi^2 n^2)/den^2 */
        arb_sqr(u, L, prec); arb_sub(u, u, t, prec); arb_mul(u, u, K2, prec);
        arb_sqr(v, den, prec); arb_div(a + n, u, v, prec);

        /* archimedean: b += I1/pi ; a += -2 [w + I3 + C - I2/L] */
        arb_div(t, I1, pi, prec); arb_add(b + n, b + n, t, prec);
        arb_add(t, wL, I3, prec); arb_add(t, t, CL, prec);
        arb_div(u, I2, L, prec); arb_sub(t, t, u, prec);
        arb_mul_2exp_si(t, t, 1); arb_sub(a + n, a + n, t, prec);

        /* primes: b += (1/pi) sum w_k sin(omega y_k); a += -2 sum w_k (1 - y_k/L) cos(omega y_k) */
        arb_zero(u); arb_zero(v);
        for (i = 0; i < npp; i++)
        {
            arb_mul(t, omega, ppy + i, prec);
            arb_sin_cos(sn, cs, t, prec);
            arb_mul(sn, sn, ppw + i, prec); arb_add(u, u, sn, prec);
            arb_div(t, ppy + i, L, prec); arb_sub_ui(t, t, 1, prec); arb_neg(t, t);
            arb_mul(t, t, cs, prec); arb_mul(t, t, ppw + i, prec); arb_add(v, v, t, prec);
        }
        arb_div(u, u, pi, prec); arb_add(b + n, b + n, u, prec);
        arb_mul_2exp_si(v, v, 1); arb_sub(a + n, a + n, v, prec);
    }

    /* b_n is odd in n (Lemma `basicexpli` l.817-819: b_{-j} = -b_j), so b_0 = 0 exactly; the ball
     * computed above is only a rounding neighbourhood of 0 (found by fuzz/fuzz_ab.c). */
    arb_zero(b + 0);

    _arb_vec_clear(ppy, npp); _arb_vec_clear(ppw, npp);
    arb_clear(L); arb_clear(z); arb_clear(e); arb_clear(K2); arb_clear(wL); arb_clear(CL); arb_clear(pi);
    arb_clear(t); arb_clear(u); arb_clear(v); arb_clear(omega); arb_clear(den);
    arb_clear(I1); arb_clear(I2); arb_clear(I3); arb_clear(S10); arb_clear(sn); arb_clear(cs);
    arb_clear(lk); arb_clear(lp);
    acb_clear(A); acb_clear(psi); acb_clear(psi1); acb_clear(S1); acb_clear(S2); acb_clear(one);
}
