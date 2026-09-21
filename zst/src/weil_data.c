/* The general explicit-formula data model: zst_weil_t -> Loewner data (a_n, b_n).
 *
 * AUTHORITATIVE formula sheet: notes/zeta-spectral-triples/ellcurve/astra-review.md, F2-F18.
 * Paper anchors (refs/src/2511.22755/mc2arXiv.tex, sha256 in refs/manifest.sha256):
 *   Loewner convention (F3)                Lemma `basicexpli`, eq. (form) l.817-833
 *   prime atoms (F5/F16)                   eq. (bomp) l.693-694
 *   archimedean one-sided kernel (F6/F8)   `thetaprime` l.449-459, l.490-495, (weinfty) l.709,
 *                                          Prop. `computearch` l.720-771
 *   pole functional (F18)                  Lemma `w02`, eq. (hh) l.684-686
 *   overall sign W_02 - W_R - sum W_p      `bombtest` l.465-492
 *
 * The window distribution on [0, L], L = log x (F2):
 *   D(q) = sum_k w_k q(y_k)                                        atoms, 0 < y_k <= L
 *        - sum_g mult_g int_0^L (q(y) - q(0)) rho_{d_g,mu_g}(y) dy  gamma factors, SUBTRACTED
 *        + sum_j pmult_j int_0^L q(y) e^{sigma_j y} dy              poles (zeta: sigma = +-1/2)
 *        + (s/2) q(0),   s the identity shift of F8,
 * and (F3/F16) b_n = -(1/pi) D(sin omega_n y), a_n = 2 D((1 - y/L) cos omega_n y), omega_n = 2 pi n/L.
 * Because q(0) = 2 for the diagonal test function (1 - y/L) cos(omega_n y), the delta coefficient s/2
 * lands as the shift s on every a_n; the sine test function vanishes at 0, so b_n never sees it.
 */
#include <flint/ulong_extras.h>
#include <flint/acb.h>
#include "zst.h"

void
zst_weil_init(zst_weil_t *W, slong natoms, slong ngamma, slong npoles, slong prec)
{
    arb_init(W->L);
    arb_init(W->shift_extra);
    fmpz_init(W->cond);
    fmpz_one(W->cond);

    W->natoms = natoms;
    W->y = natoms > 0 ? _arb_vec_init(natoms) : NULL;
    W->w = natoms > 0 ? _arb_vec_init(natoms) : NULL;

    W->ngamma = ngamma;
    W->Q = ngamma > 0 ? _arb_vec_init(ngamma) : NULL;
    W->d = ngamma > 0 ? _arb_vec_init(ngamma) : NULL;
    W->mu = ngamma > 0 ? _arb_vec_init(ngamma) : NULL;
    W->mult = ngamma > 0 ? flint_malloc(ngamma * sizeof(slong)) : NULL;

    W->npoles = npoles;
    W->sigma = npoles > 0 ? _arb_vec_init(npoles) : NULL;
    W->pmult = npoles > 0 ? flint_malloc(npoles * sizeof(slong)) : NULL;
}

void
zst_weil_clear(zst_weil_t *W)
{
    if (W->natoms > 0) { _arb_vec_clear(W->y, W->natoms); _arb_vec_clear(W->w, W->natoms); }
    if (W->ngamma > 0)
    {
        _arb_vec_clear(W->Q, W->ngamma); _arb_vec_clear(W->d, W->ngamma);
        _arb_vec_clear(W->mu, W->ngamma); flint_free(W->mult);
    }
    if (W->npoles > 0) { _arb_vec_clear(W->sigma, W->npoles); flint_free(W->pmult); }
    arb_clear(W->L); arb_clear(W->shift_extra); fmpz_clear(W->cond);
    W->natoms = W->ngamma = W->npoles = 0;
    W->y = W->w = W->Q = W->d = W->mu = W->sigma = NULL;
    W->mult = W->pmult = NULL;
}

/* F8: s = log C + sum_g mult_g [2 log Q_g + (2/d_g) psi(mu_g/d_g) + 2 T_{d_g,mu_g}(L)] + shift_extra.
 * Equivalently F10, which displays the paper's regularisation (subtraction exponent 1) explicitly:
 *   s_gamma = -2 [w_{d,Q}(L) + C_{d,mu}(L)],  w_{d,Q} = -log Q - psi(1/d)/d - T_{d,1}(L),
 *   C_{d,mu}(L) = [psi(1/d) - psi(mu/d)]/d - T_{d,mu}(L) + T_{d,1}(L);
 * the T_{d,1} and psi(1/d) terms cancel, which is why the compact F8 is what is implemented.
 * For (d, mu, Q) = (2, 1/2, pi^{-1/2}) this must equal the typed -2(w(L) + C(L)) of riemann_ab.c
 * (F12); tests/test_weil.c checks that through the full (a_n, b_n). */
void
zst_weil_shift(arb_t s, const zst_weil_t *W, slong prec)
{
    arb_t t, u, T;
    slong g;

    arb_init(t); arb_init(u); arb_init(T);

    arb_log_fmpz(s, W->cond, prec);                       /* + log C (F8) */
    for (g = 0; g < W->ngamma; g++)
    {
        arb_log(t, W->Q + g, prec);
        arb_mul_2exp_si(t, t, 1);                         /* 2 log Q */
        arb_div(u, W->mu + g, W->d + g, prec);
        arb_digamma(u, u, prec);
        arb_div(u, u, W->d + g, prec);
        arb_mul_2exp_si(u, u, 1);                         /* (2/d) psi(mu/d) */
        arb_add(t, t, u, prec);
        zst_kernel_tail(T, W->d + g, W->mu + g, W->L, prec);
        arb_mul_2exp_si(u, T, 1);                         /* 2 T_{d,mu}(L) */
        arb_add(t, t, u, prec);
        arb_mul_si(t, t, W->mult[g], prec);
        arb_add(s, s, t, prec);
    }
    arb_add(s, s, W->shift_extra, prec);

    arb_clear(t); arb_clear(u); arb_clear(T);
}

/* One rank-one pole at real sigma contributes + int_0^L q(y) e^{sigma y} dy to D (F18).  With
 * omega = omega_n, D = sigma^2 + omega^2 and E - 1 = expm1(sigma L), and using sin(omega L) = 0,
 * cos(omega L) = 1:
 *   J  = int_0^L e^{sigma y} cos(omega y) dy = sigma (E - 1)/D,
 *   M  = int_0^L y e^{sigma y} cos(omega y) dy = dJ/dsigma
 *      = [(E - 1) + sigma L E]/D - 2 sigma^2 (E - 1)/D^2,
 *   int_0^L e^{sigma y} sin(omega y) dy = omega (1 - E)/D,
 * so the pole adds 2 (J - M/L) to a_n and +(1/pi) omega (E - 1)/D to b_n.  For the zeta pair
 * sigma = +-1/2 this sums to exactly F18,
 *   K = 32 L sinh^2(L/4),  a_n^(02) = K (L^2 - 16 pi^2 n^2)/(L^2 + 16 pi^2 n^2)^2,
 *   b_n^(02) = K n/(L^2 + 16 pi^2 n^2),
 * which tests/test_weil.c verifies against the typed F18 of riemann_ab.c.
 * (sigma, n) = (0, 0) is the removable case J = L, M = L^2/2. */
static void
pole_ab(arb_t pa, arb_t pb, const arb_t sigma, const arb_t omega, const arb_t L, slong prec)
{
    arb_t D, E1, J, M, t, u;

    arb_init(D); arb_init(E1); arb_init(J); arb_init(M); arb_init(t); arb_init(u);

    arb_sqr(D, sigma, prec);
    arb_sqr(t, omega, prec);
    arb_add(D, D, t, prec);

    if (arb_is_zero(D))                     /* sigma = 0 and n = 0 */
    {
        arb_set(J, L);
        arb_sqr(M, L, prec); arb_mul_2exp_si(M, M, -1);
        arb_zero(pb);
    }
    else
    {
        arb_mul(t, sigma, L, prec);
        arb_expm1(E1, t, prec);                              /* E - 1 */
        arb_mul(J, sigma, E1, prec); arb_div(J, J, D, prec); /* J */
        /* M = [(E-1) + sigma L E]/D - 2 sigma^2 (E-1)/D^2 */
        arb_add_ui(u, E1, 1, prec);                          /* E */
        arb_mul(u, u, sigma, prec); arb_mul(u, u, L, prec);
        arb_add(u, u, E1, prec);
        arb_div(M, u, D, prec);
        arb_sqr(u, sigma, prec); arb_mul(u, u, E1, prec); arb_mul_2exp_si(u, u, 1);
        arb_sqr(t, D, prec); arb_div(u, u, t, prec);
        arb_sub(M, M, u, prec);
        /* b gets -(1/pi) * omega (1 - E)/D = +(1/pi) omega (E - 1)/D */
        arb_mul(pb, omega, E1, prec); arb_div(pb, pb, D, prec);
    }
    arb_div(t, M, L, prec);
    arb_sub(t, J, t, prec);
    arb_mul_2exp_si(pa, t, 1);

    arb_clear(D); arb_clear(E1); arb_clear(J); arb_clear(M); arb_clear(t); arb_clear(u);
}

/* F16: (a_n, b_n) for n = 0..N.
 *   a_n = 2 sum_k w_k (1 - y_k/L) cos(omega_n y_k)              atoms
 *         + sum_g mult_g * (-2) [I3(n) - I2(n)/L]               gamma factors (bare, F14)
 *         + sum_j pmult_j * 2 [J - M/L]                         poles (F18)
 *         + s                                                   identity shift (F8)
 *   b_n = -(1/pi) sum_k w_k sin(omega_n y_k) + sum_g mult_g I1(n)/pi + sum_j pmult_j (...)/pi
 * b_0 = 0 exactly (F3; b_n is odd in n). */
void
zst_weil_ab(arb_ptr a, arb_ptr b, slong N, const zst_weil_t *W, slong prec)
{
    arb_t pi, omega, s, I1, I2, I3, t, u, v, sn, cs, pa, pb;
    slong n, i, g;

    arb_init(pi); arb_init(omega); arb_init(s);
    arb_init(I1); arb_init(I2); arb_init(I3);
    arb_init(t); arb_init(u); arb_init(v); arb_init(sn); arb_init(cs);
    arb_init(pa); arb_init(pb);

    arb_const_pi(pi, prec);
    zst_weil_shift(s, W, prec);

    for (n = 0; n <= N; n++)
    {
        arb_mul_ui(omega, pi, 2 * (ulong) n, prec);
        arb_div(omega, omega, W->L, prec);

        arb_set(a + n, s);
        arb_zero(b + n);

        /* gamma factors: a += -2 mult [I3 - I2/L],  b += mult I1/pi   (F16) */
        for (g = 0; g < W->ngamma; g++)
        {
            zst_kernel_I123(I1, I2, I3, n, W->d + g, W->mu + g, W->L, prec);
            arb_div(t, I2, W->L, prec);
            arb_sub(t, I3, t, prec);
            arb_mul_2exp_si(t, t, 1);
            arb_mul_si(t, t, W->mult[g], prec);
            arb_sub(a + n, a + n, t, prec);
            arb_div(t, I1, pi, prec);
            arb_mul_si(t, t, W->mult[g], prec);
            arb_add(b + n, b + n, t, prec);
        }

        /* poles (F18) */
        for (i = 0; i < W->npoles; i++)
        {
            pole_ab(pa, pb, W->sigma + i, omega, W->L, prec);
            arb_mul_si(pa, pa, W->pmult[i], prec);
            arb_add(a + n, a + n, pa, prec);
            arb_div(pb, pb, pi, prec);
            arb_mul_si(pb, pb, W->pmult[i], prec);
            arb_add(b + n, b + n, pb, prec);
        }

        /* atoms (F5/F16) */
        arb_zero(u); arb_zero(v);
        for (i = 0; i < W->natoms; i++)
        {
            arb_mul(t, omega, W->y + i, prec);
            arb_sin_cos(sn, cs, t, prec);
            arb_mul(sn, sn, W->w + i, prec);
            arb_add(u, u, sn, prec);                          /* sum w_k sin(omega y_k) */
            arb_div(t, W->y + i, W->L, prec);
            arb_sub_ui(t, t, 1, prec); arb_neg(t, t);         /* 1 - y_k/L */
            arb_mul(t, t, cs, prec); arb_mul(t, t, W->w + i, prec);
            arb_add(v, v, t, prec);
        }
        arb_div(u, u, pi, prec);
        arb_sub(b + n, b + n, u, prec);                       /* b += -(1/pi) sum ... */
        arb_mul_2exp_si(v, v, 1);
        arb_add(a + n, a + n, v, prec);                       /* a += 2 sum ... */
    }

    arb_zero(b + 0);                                          /* F3: b_0 = 0 exactly */

    arb_clear(pi); arb_clear(omega); arb_clear(s);
    arb_clear(I1); arb_clear(I2); arb_clear(I3);
    arb_clear(t); arb_clear(u); arb_clear(v); arb_clear(sn); arb_clear(cs);
    arb_clear(pa); arb_clear(pb);
}

/* Number of prime powers k = p^m with 1 < k <= X. */
static slong
count_prime_powers(ulong X)
{
    slong npp = 0;
    ulong k;
    for (k = 2; k <= X; k++)
    {
        n_factor_t f;
        n_factor_init(&f);
        n_factor(&f, k, 1);
        npp += (f.num == 1);
    }
    return npp;
}

/* Riemann zeta through the generic model (F12, F17, F18):
 *   atoms  -Lambda(k) k^{-1/2} = -log p * p^{-m/2} at y = log k = m log p, for 1 < k = p^m <= X
 *          (the general F5 with t_m = 1 for every m and p: c_m(p) = 1);
 *   gamma  one factor Gamma_R(s) = pi^{-s/2} Gamma(s/2): Q = pi^{-1/2}, d = 2, kappa = 0 so
 *          mu = 1/2, multiplicity 1;
 *   conductor 1;
 *   poles  the rank-two functional W_02 of Lemma `w02` (mc2arXiv.tex l.684-686) as two rank-one
 *          poles at sigma = +-1/2 (the poles of the completed zeta at s = 0, 1 in centred
 *          coordinates).  This is the ONLY object here that has them (F17). */
void
zst_weil_riemann(zst_weil_t *W, const arb_t x, ulong X, slong prec)
{
    slong j = 0;
    ulong k;
    arb_t t;

    zst_weil_init(W, count_prime_powers(X), 1, 2, prec);
    arb_init(t);
    zst_window_L(W->L, x, prec);

    for (k = 2; k <= X; k++)
    {
        n_factor_t f;
        n_factor_init(&f);
        n_factor(&f, k, 1);
        if (f.num == 1)
        {
            arb_log_ui(W->y + j, k, prec);                    /* y = log p^m */
            arb_log_ui(t, f.p[0], prec);                      /* Lambda(p^m) = log p */
            arb_sqrt_ui(W->w + j, k, prec);
            arb_div(W->w + j, t, W->w + j, prec);
            arb_neg(W->w + j, W->w + j);                      /* w = -log p * p^{-m/2} */
            j++;
        }
    }

    arb_const_pi(W->Q + 0, prec);
    arb_rsqrt(W->Q + 0, W->Q + 0, prec);                      /* Q = pi^{-1/2} */
    arb_set_ui(W->d + 0, 2);
    arb_one(W->mu + 0); arb_mul_2exp_si(W->mu + 0, W->mu + 0, -1);   /* mu = 1/2 */
    W->mult[0] = 1;

    fmpz_one(W->cond);

    arb_one(W->sigma + 0); arb_mul_2exp_si(W->sigma + 0, W->sigma + 0, -1);   /* +1/2 */
    arb_neg(W->sigma + 1, W->sigma + 0);                                      /* -1/2 */
    W->pmult[0] = 1;
    W->pmult[1] = 1;

    arb_clear(t);
}
