#define _POSIX_C_SOURCE 200809L
/* rtp1_a1: RTP round 1, lane A1 -- the dilation channel's contraction rate.
 * Author: claude:opus. Brief: notes/rtp-round-1/brief.md (Lane A1); write-up: notes/rtp-round-1/lane-A1.md.
 *
 * Reuses libzst unchanged: zst_riemann_ab (Loewner data (a_n, b_n) as balls, prime powers <= X),
 * zst_even_block / zst_odd_block, zst_eigmin (Rump-certified minimal eigenpair), zst_certify_even_simple
 * (deflated positive-definiteness certificate), zst_secular_roots and zst_zeta_zeros (comparison step only).
 * Ground truth for the form: refs/src/2511.22755/mc2arXiv.tex, Lemma `basicexpli` eq. (form) l.817-819
 * (tau_nm = (b_n - b_m)/(n - m), tau_nn = a_n), formula sheet notes/zeta-spectral-triples/plan.md 1.2-1.3.
 *
 * Modes (all arithmetic in arb balls unless a column is labelled otherwise):
 *   --mode axisN --x X --Nmax M --prec P --cmp N1,N2,.. [--cprec C]
 *       One ball LDL^T of the even block (modes 0..M+1) and of the odd block (modes 1..M+1). Its pivots are
 *       the Schur complements of the successive borderings, so row N gives, for the two new modes +-(N+1)
 *       (one new even and one new odd basis vector), the Schur complements s_e, s_o, the diagonal d_e, d_o,
 *       Delta I_N = log(d_e/s_e) + log(d_o/s_o) (lemma A1.1), log det of the window matrix on |n| <= N, and
 *       the Loewner-structured extension interval for the one new real datum b_{N+1} given a_{N+1}
 *       (lane-A1.md, A1.1'). Rows listed in --cmp also get the certified eps_N (blocks rounded to C bits) and,
 *       in a separately labelled COMPARISON block, |z_1 - gamma_1|; the last listed N gets the Rayleigh
 *       decomposition of eps over pole, archimedean and prime-power terms.
 *   --mode axisx --N N --xmax X --prec P [--fixedL 1]
 *       fixedL 0 (CCM protocol): x runs through the prime powers <= X (and X), window L = log x, primes <= x.
 *       fixedL 1 (partial-information protocol): L = log X fixed, prime cutoff runs through 1 and the prime
 *       powers <= X. Per knot: certified minimal even eigenpair, inertia, log det, Delta I and the structured
 *       interval for mode N+1, overlaps with the final eigenvector; CCM mode also the prime-free control
 *       (pole + archimedean only) and the Rayleigh decomposition of eps at the final x. The COMPARISON block
 *       (zeros used) is printed last and labelled.
 * Output is byte-reproducible (no timings, no addresses); timings go to stderr. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <flint/acb_mat.h>
#include <flint/ulong_extras.h>
#include "zst.h"

static slong n_checks = 0, n_fail = 0;
static void check(int cond, const char *msg)
{
    n_checks++;
    if (!cond) { n_fail++; flint_printf("CHECK FAIL: %s\n", msg); }
}

static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + 1e-9 * t.tv_nsec; }

/* ball -> string: d significant digits of the midpoint when the relative radius is below 10^-d,
 * otherwise the full ball (so every printed digit is certified) */
static char *sb(const arb_t x, slong d)
{
    static char buf[16][256];
    static int k = 0;
    char *s, *out = buf[k = (k + 1) % 16];
    if (arb_is_zero(x)) { strcpy(out, "0"); return out; }
    if (arb_rel_accuracy_bits(x) > (slong) (3.33 * d) + 4) s = arb_get_str(x, d, ARB_STR_NO_RADIUS);
    else s = arb_get_str(x, d, 0);
    strncpy(out, s, 255); out[255] = 0;
    flint_free(s);
    return out;
}

static char *smag(const mag_t m)
{
    static char buf[8][64];
    static int k = 0;
    char *out = buf[k = (k + 1) % 8];
    arf_t f; arf_init(f);
    arf_set_mag(f, m);
    {
        char *s = arf_get_str(f, 3);
        strncpy(out, s, 63); out[63] = 0; flint_free(s);
    }
    arf_clear(f);
    return out;
}

static int is_prime_power(ulong k, ulong *p)
{
    n_factor_t f;
    if (k < 2) return 0;
    n_factor_init(&f);
    n_factor(&f, k, 1);
    if (f.num == 1) { if (p) *p = f.p[0]; return 1; }
    return 0;
}

/* forward substitution y = L^{-1} r with the unit lower triangle of an arb_mat_ldl factor (leading n x n) */
static void fwd_unit(arb_ptr y, const arb_mat_t LD, arb_srcptr r, slong n, slong prec)
{
    slong i;
    for (i = 0; i < n; i++)
        arb_dot(y + i, r + i, 1, arb_mat_entry(LD, i, 0), 1, y, 1, i, prec);
}

/* Structured (Loewner) bordering of one block. G = leading n x n of the factored block (LD = its ball LDL^T),
 * new index n. The new column is c(b) = u + b w, the new diagonal d(b) = a_{j} + sg * b / j (sg = +1 even,
 * -1 odd), with b = b_{j} the one new odd Loewner datum. With beta = b - b_true:
 *   s(beta) = s_true + beta (sg/j - 2P) - beta^2 C,  P = y_c . y_w / D,  C = y_w . y_w / D,
 * y_c = L^{-1} c(b_true) (read off the factor: row n of L times D), y_w = L^{-1} w.
 * Returns the vertex beta*, the half-width r of {s >= 0}, and the three coefficients. */
typedef struct { arb_t s0, lin, C, bstar, r; } sq_t;
static void sq_init(sq_t *q) { arb_init(q->s0); arb_init(q->lin); arb_init(q->C); arb_init(q->bstar); arb_init(q->r); }
static void sq_clear(sq_t *q) { arb_clear(q->s0); arb_clear(q->lin); arb_clear(q->C); arb_clear(q->bstar); arb_clear(q->r); }
static void sq_eval(arb_t s, const sq_t *q, const arb_t beta, slong prec)
{
    arb_t t; arb_init(t);
    arb_mul(t, q->C, beta, prec); arb_sub(t, q->lin, t, prec); arb_mul(t, t, beta, prec);
    arb_add(s, q->s0, t, prec);
    arb_clear(t);
}
static void sq_deriv(arb_t ds, const sq_t *q, const arb_t beta, slong prec)
{
    arb_t t; arb_init(t);
    arb_mul(t, q->C, beta, prec); arb_mul_2exp_si(t, t, 1); arb_sub(ds, q->lin, t, prec);
    arb_clear(t);
}

static void structured(sq_t *q, const arb_mat_t LD, slong n, arb_srcptr w, slong j, int sg, slong prec)
{
    arb_ptr yw = _arb_vec_init(n), yc = _arb_vec_init(n);
    arb_t t, u;
    slong i;
    arb_init(t); arb_init(u);
    fwd_unit(yw, LD, w, n, prec);
    for (i = 0; i < n; i++) arb_mul(yc + i, arb_mat_entry(LD, n, i), arb_mat_entry(LD, i, i), prec);
    arb_zero(q->lin); arb_zero(q->C);
    for (i = 0; i < n; i++)
    {
        arb_mul(t, yc + i, yw + i, prec); arb_div(t, t, arb_mat_entry(LD, i, i), prec); arb_add(q->lin, q->lin, t, prec);
        arb_mul(t, yw + i, yw + i, prec); arb_div(t, t, arb_mat_entry(LD, i, i), prec); arb_add(q->C, q->C, t, prec);
    }
    /* lin = sg/j - 2P */
    arb_mul_2exp_si(q->lin, q->lin, 1); arb_neg(q->lin, q->lin);
    arb_set_si(t, sg); arb_div_si(t, t, j, prec); arb_add(q->lin, q->lin, t, prec);
    arb_set(q->s0, arb_mat_entry(LD, n, n));
    /* vertex and half-width */
    arb_mul_2exp_si(t, q->C, 1); arb_div(q->bstar, q->lin, t, prec);
    arb_sqr(u, q->lin, prec); arb_mul_2exp_si(t, q->C, 2); arb_div(u, u, t, prec); arb_add(u, u, q->s0, prec);
    arb_div(u, u, q->C, prec); arb_sqrt(q->r, u, prec);
    _arb_vec_clear(yw, n); _arb_vec_clear(yc, n);
    arb_clear(t); arb_clear(u);
}

/* joint MaxEnt point: maximiser of log s_e + log s_o on the intersection [lo, hi] of the two admissible
 * intervals (concave; bisection on the sign of the derivative at midpoints, 200 steps). The point itself is
 * a floating prediction; everything evaluated at it afterwards is a ball. */
static void joint_maxent(arb_t bme, const sq_t *qe, const sq_t *qo, const arb_t lo, const arb_t hi, slong prec)
{
    arb_t a, b, m, se, so, de, dO, f;
    slong it;
    arb_init(a); arb_init(b); arb_init(m); arb_init(se); arb_init(so); arb_init(de); arb_init(dO); arb_init(f);
    arb_get_mid_arb(a, lo); arb_get_mid_arb(b, hi);
    for (it = 0; it < 200; it++)
    {
        arb_add(m, a, b, prec); arb_mul_2exp_si(m, m, -1); arb_get_mid_arb(m, m);
        sq_eval(se, qe, m, prec); sq_eval(so, qo, m, prec);
        sq_deriv(de, qe, m, prec); sq_deriv(dO, qo, m, prec);
        /* sign of de/se + do/so = sign of de*so + do*se when both s > 0 */
        arb_mul(f, de, so, prec); arb_addmul(f, dO, se, prec);
        if (arf_sgn(arb_midref(f)) > 0) arb_set(a, m); else arb_set(b, m);
    }
    arb_add(m, a, b, prec); arb_mul_2exp_si(m, m, -1); arb_get_mid_arb(bme, m);
    arb_clear(a); arb_clear(b); arb_clear(m); arb_clear(se); arb_clear(so); arb_clear(de); arb_clear(dO); arb_clear(f);
}

/* new-column derivative vectors w (d c / d b_j) for the even block (indices 0..n-1 = modes 0..j-1) and the
 * odd block (indices 0..j-2 = modes 1..j-1); plan.md 1.3 block formulas differentiated in b_j */
static void w_even(arb_ptr w, slong j, slong prec)
{
    slong i;
    arb_t t;
    arb_init(t);
    arb_sqrt_ui(w + 0, 2, prec); arb_div_si(w + 0, w + 0, j, prec);
    for (i = 1; i < j; i++)
    {
        arb_one(t); arb_div_si(t, t, i + j, prec);
        arb_one(w + i); arb_div_si(w + i, w + i, i - j, prec);
        arb_sub(w + i, t, w + i, prec);                 /* 1/(i+j) - 1/(i-j) */
    }
    arb_clear(t);
}
static void w_odd(arb_ptr w, slong j, slong prec)
{
    slong i;
    arb_t t;
    arb_init(t);
    for (i = 1; i < j; i++)
    {
        arb_one(t); arb_div_si(t, t, i + j, prec);
        arb_one(w + i - 1); arb_div_si(w + i - 1, w + i - 1, i - j, prec);
        arb_add(w + i - 1, w + i - 1, t, prec); arb_neg(w + i - 1, w + i - 1);   /* -1/(i-j) - 1/(i+j) */
    }
    arb_clear(t);
}

/* Everything the bordering N -> N+1 yields, from ball LDL factors LE (even, modes 0..>=N+1) and
 * LO (odd, modes 1..>=N+1) and the blocks E, O. */
typedef struct { arb_t de, se, dI_e, do_, so, dI_o, dI, re, ro, rj, tau_e, tau_o, tau_j, dIs, bme; } border_t;
static void border_init(border_t *r)
{
    arb_init(r->de); arb_init(r->se); arb_init(r->dI_e); arb_init(r->do_); arb_init(r->so); arb_init(r->dI_o);
    arb_init(r->dI); arb_init(r->re); arb_init(r->ro); arb_init(r->rj); arb_init(r->tau_e); arb_init(r->tau_o);
    arb_init(r->tau_j); arb_init(r->dIs); arb_init(r->bme);
}
static void border_clear(border_t *r)
{
    arb_clear(r->de); arb_clear(r->se); arb_clear(r->dI_e); arb_clear(r->do_); arb_clear(r->so); arb_clear(r->dI_o);
    arb_clear(r->dI); arb_clear(r->re); arb_clear(r->ro); arb_clear(r->rj); arb_clear(r->tau_e); arb_clear(r->tau_o);
    arb_clear(r->tau_j); arb_clear(r->dIs); arb_clear(r->bme);
}

static void bordering(border_t *r, const arb_mat_t E, const arb_mat_t O, const arb_mat_t LE, const arb_mat_t LO,
                      slong N, slong prec)
{
    slong j = N + 1;
    sq_t qe, qo;
    arb_ptr w = _arb_vec_init(j);
    arb_t lo, hi, t, u, zero, se, so;
    sq_init(&qe); sq_init(&qo);
    arb_init(lo); arb_init(hi); arb_init(t); arb_init(u); arb_init(zero); arb_init(se); arb_init(so);

    /* A1.1: Schur complements = LDL pivots; Delta I = log(d/s) per block */
    arb_set(r->de, arb_mat_entry(E, j, j)); arb_set(r->se, arb_mat_entry(LE, j, j));
    arb_set(r->do_, arb_mat_entry(O, j - 1, j - 1)); arb_set(r->so, arb_mat_entry(LO, j - 1, j - 1));
    arb_div(t, r->de, r->se, prec); arb_log(r->dI_e, t, prec);
    arb_div(t, r->do_, r->so, prec); arb_log(r->dI_o, t, prec);
    arb_add(r->dI, r->dI_e, r->dI_o, prec);

    /* A1.1': Loewner-structured interval for b_{N+1} */
    w_even(w, j, prec);
    structured(&qe, LE, j, w, j, +1, prec);
    w_odd(w, j, prec);
    structured(&qo, LO, j - 1, w, j, -1, prec);
    arb_set(r->re, qe.r); arb_set(r->ro, qo.r);
    arb_div(r->tau_e, qe.bstar, qe.r, prec); arb_neg(r->tau_e, r->tau_e);
    arb_div(r->tau_o, qo.bstar, qo.r, prec); arb_neg(r->tau_o, r->tau_o);
    /* intersection [lo, hi] */
    arb_sub(lo, qe.bstar, qe.r, prec); arb_sub(t, qo.bstar, qo.r, prec); arb_max(lo, lo, t, prec);
    arb_add(hi, qe.bstar, qe.r, prec); arb_add(t, qo.bstar, qo.r, prec); arb_min(hi, hi, t, prec);
    arb_sub(r->rj, hi, lo, prec); arb_mul_2exp_si(r->rj, r->rj, -1);
    arb_add(t, hi, lo, prec); arb_mul_2exp_si(t, t, -1);             /* centre of the intersection */
    arb_div(r->tau_j, t, r->rj, prec); arb_neg(r->tau_j, r->tau_j);
    /* joint MaxEnt and its log-det deficit relative to the truth (beta = 0) */
    joint_maxent(r->bme, &qe, &qo, lo, hi, prec);
    sq_eval(se, &qe, r->bme, prec); sq_eval(so, &qo, r->bme, prec);
    arb_mul(t, se, so, prec);
    arb_mul(u, qe.s0, qo.s0, prec);
    arb_div(t, t, u, prec); arb_log(r->dIs, t, prec);

    /* checks: s_true >= 0 is the truth lying in the interval; Delta I >= 0; structured gain >= 0 */
    check(arb_is_positive(r->se) && arb_is_positive(r->so), "Schur complements positive");
    check(!arb_is_negative(r->dI_e) && !arb_is_negative(r->dI_o), "Delta I >= 0 per block");
    {
        arb_t one; arb_init(one); arb_one(one);
        arb_abs(t, r->tau_e); check(arb_le(t, one), "truth inside even interval");
        arb_abs(t, r->tau_o); check(arb_le(t, one), "truth inside odd interval");
        arb_clear(one);
    }
    check(arb_is_positive(se) && arb_is_positive(so), "joint MaxEnt point admissible");
    check(!arb_is_negative(r->dIs), "structured gain >= 0");

    _arb_vec_clear(w, j);
    sq_clear(&qe); sq_clear(&qo);
    arb_clear(lo); arb_clear(hi); arb_clear(t); arb_clear(u); arb_clear(zero); arb_clear(se); arb_clear(so);
}

/* xi from even eigenvector (plan.md 1.4), secular roots, z_1 = 2 pi s_1 / L. COMPARISON STEP helper:
 * returns the number of certified positive roots (N = complete). */
static slong first_root(arb_t z1, arb_srcptr v, slong N, const arb_t L, slong prec)
{
    arb_ptr xi = _arb_vec_init(N + 1), roots = _arb_vec_init(N);
    arb_t t, u, sum;
    slong k, nroots, unres;
    arb_init(t); arb_init(u); arb_init(sum);
    arb_set(xi + 0, v + 0);
    arb_sqrt_ui(t, 2, prec);
    for (k = 1; k <= N; k++) arb_div(xi + k, v + k, t, prec);
    arb_set(sum, xi + 0);
    for (k = 1; k <= N; k++) { arb_mul_2exp_si(u, xi + k, 1); arb_add(sum, sum, u, prec); }
    for (k = 0; k <= N; k++) arb_div(xi + k, xi + k, sum, prec);
    nroots = zst_secular_roots(roots, N, &unres, xi, N, prec);
    if (nroots > 0)
    {
        arb_const_pi(t, prec); arb_mul_2exp_si(t, t, 1); arb_div(t, t, L, prec);
        arb_mul(z1, roots + 0, t, prec);
    }
    else arb_indeterminate(z1);
    _arb_vec_clear(xi, N + 1); _arb_vec_clear(roots, N);
    arb_clear(t); arb_clear(u); arb_clear(sum);
    return nroots;
}

/* Certified minimal eigenpair of the symmetric block E (any inertia), with optional odd block O for the
 * even-simple status. Route: shift sigma just below the smallest eigenvalue (from an approximate QR spectrum,
 * or 0 when E is certified positive definite), zst_eigmin on E - sigma (Rump/Krawczyk), then
 * zst_certify_even_simple on the shifted blocks: E - sigma has exactly one eigenvalue below 2(lam - sigma),
 * so lam is the simple minimum of E. Returns 1 if lam is certified as the simple minimum; *es = 1 if in
 * addition every odd eigenvalue exceeds the certified threshold (even-simple). v is normalised to unit length. */
static int eig_min(arb_t lam, arb_ptr v, int *es, const arb_mat_t E, const arb_mat_t O, int pd, slong prec)
{
    slong n = arb_mat_nrows(E), m = arb_mat_nrows(O), i, attempt;
    arb_mat_t Es, Os, O0;
    arb_t sigma, eps, t, l1, l2;
    int ok = 0;
    const double frac[3] = {1e-3, 1e-1, 0.5};
    arb_mat_init(Es, n, n); arb_mat_init(Os, m, m); arb_mat_init(O0, 0, 0);
    arb_init(sigma); arb_init(eps); arb_init(t); arb_init(l1); arb_init(l2);
    *es = 0;
    arb_indeterminate(lam);
    /* an indefinite block has O(1)-separated low eigenvalues here; 448 bits are ample (the balls say so) */
    if (!pd) prec = FLINT_MIN(prec, 448);
    if (!pd)
    {
        /* approximate spectrum of the midpoint matrix (floating QR at qprec bits; it only places the shift) */
        slong qprec = FLINT_MIN(prec, 512);
        acb_mat_t A; acb_ptr ev; mag_t tol;
        acb_mat_init(A, n, n); ev = _acb_vec_init(n); mag_init(tol);
        for (i = 0; i < n; i++)
        {
            slong jj;
            for (jj = 0; jj < n; jj++)
            {
                arb_get_mid_arb(acb_realref(acb_mat_entry(A, i, jj)), arb_mat_entry(E, i, jj));
                arb_zero(acb_imagref(acb_mat_entry(A, i, jj)));
            }
        }
        mag_set_ui_2exp_si(tol, 1, -(qprec - 30));
        if (!acb_mat_approx_eig_qr(ev, NULL, NULL, A, tol, 0, qprec))
            flint_printf("# note: QR for the shift did not converge (the certificate below decides)\n");
        arb_pos_inf(l1); arb_pos_inf(l2);
        for (i = 0; i < n; i++)
        {
            arb_get_mid_arb(t, acb_realref(ev + i));
            if (arf_cmp(arb_midref(t), arb_midref(l1)) < 0) { arb_set(l2, l1); arb_set(l1, t); }
            else if (arf_cmp(arb_midref(t), arb_midref(l2)) < 0) arb_set(l2, t);
        }
        acb_mat_clear(A); _acb_vec_clear(ev, n); mag_clear(tol);
    }
    for (attempt = 0; attempt < (pd ? 1 : 3) && !ok; attempt++)
    {
        if (pd) arb_zero(sigma);
        else
        {
            /* sigma = l1 - frac (l2 - l1): the nearest eigenvalue to sigma is the smallest one */
            arb_sub(t, l2, l1, prec); arb_set_d(sigma, frac[attempt]); arb_mul(t, t, sigma, prec);
            arb_sub(sigma, l1, t, prec); arb_get_mid_arb(sigma, sigma);
        }
        arb_mat_set(Es, E); arb_mat_set(Os, O);
        for (i = 0; i < n; i++) arb_sub(arb_mat_entry(Es, i, i), arb_mat_entry(Es, i, i), sigma, prec);
        for (i = 0; i < m; i++) arb_sub(arb_mat_entry(Os, i, i), arb_mat_entry(Os, i, i), sigma, prec);
        if (zst_eigmin(eps, v, Es, pd ? 60 : 1000, prec))
        {
            if (zst_certify_even_simple(Es, Os, eps, v, prec)) { ok = 1; *es = 1; }
            else if (zst_certify_even_simple(Es, O0, eps, v, prec)) ok = 1;
            arb_add(lam, eps, sigma, prec);
            /* unit normalisation */
            arb_zero(t);
            for (i = 0; i < n; i++) arb_addmul(t, v + i, v + i, prec);
            arb_sqrt(t, t, prec);
            for (i = 0; i < n; i++) arb_div(v + i, v + i, t, prec);
        }
    }
    if (!ok) arb_indeterminate(lam);
    arb_mat_clear(Es); arb_mat_clear(Os); arb_mat_clear(O0);
    arb_clear(sigma); arb_clear(eps); arb_clear(t); arb_clear(l1); arb_clear(l2);
    return ok;
}

static void print_ab_reference(slong prec)
{
    arb_t x; arb_ptr a, b; slong n;
    arb_init(x); a = _arb_vec_init(4); b = _arb_vec_init(4);
    arb_set_ui(x, 13);
    zst_riemann_ab(a, b, 3, x, 13, prec);
    flint_printf("# cross-lane reference (Conventions): zst (a_n, b_n) at x = 13, prime powers <= 13\n");
    for (n = 0; n <= 3; n++)
        flint_printf("#   n = %wd  a_n = %s  b_n = %s\n", n, sb(a + n, 30), sb(b + n, 30));
    _arb_vec_clear(a, 4); _arb_vec_clear(b, 4); arb_clear(x);
}

static void rayleigh_table(double xd, ulong X, const arb_t L, slong N, arb_srcptr v, const arb_t eps, slong prec);

static void mode_axisN(double xd, slong Nmax, slong prec, const char *cmp, slong cprec)
{
    slong M = Nmax + 1, N;
    ulong X = (ulong) (xd + 1e-9);
    arb_t x, L, t, logdetE, logdetO, logdet, sumdI;
    arb_ptr a, b, cum = NULL, ldv = NULL;
    arb_mat_t E, O, LE, LO;
    border_t r;
    int okE, okO;
    double t0 = now();

    arb_init(x); arb_init(L); arb_init(t); arb_init(logdetE); arb_init(logdetO); arb_init(logdet); arb_init(sumdI);
    a = _arb_vec_init(M + 1); b = _arb_vec_init(M + 1);
    arb_mat_init(E, M + 1, M + 1); arb_mat_init(O, M, M);
    arb_mat_init(LE, M + 1, M + 1); arb_mat_init(LO, M, M);
    border_init(&r);

    arb_set_d(x, xd);
    zst_window_L(L, x, prec);
    flint_printf("# rtp1_a1 axisN (lane A1.2): the resolution axis at fixed window\n");
    flint_printf("# author claude:opus; driver zst/tools/rtp1_a1.c on libzst (FLINT %s)\n", FLINT_VERSION);
    flint_printf("# fixed: x = lambda^2 = %g, window L = log x = %s, prime powers k <= %wu enter, prec = %wd bits\n",
                 xd, sb(L, 15), X, prec);
    flint_printf("# varied: N = 1..%wd (window matrix on |n| <= N is the leading block of the one on |n| <= N+1)\n", Nmax);
    flint_printf("# reference: benchmark saturation N ~ 7.5 x = %.1f\n", 7.5 * xd);
    print_ab_reference(prec);

    zst_riemann_ab(a, b, M, x, X, prec);
    zst_even_block(E, a, b, M, prec);
    zst_odd_block(O, a, b, M, prec);
    okE = arb_mat_ldl(LE, E, prec);
    okO = arb_mat_ldl(LO, O, prec);
    flint_printf("# ball LDL^T of even block (size %wd): %s; odd block (size %wd): %s\n", M + 1,
                 okE ? "all pivots certified positive" : "FAILED", M, okO ? "all pivots certified positive" : "FAILED");
    flint_printf("#   (so the window form is certified positive definite on |n| <= N for every N <= %wd)\n", M);
    check(okE && okO, "ball LDL^T succeeds");
    if (!okE || !okO) { flint_printf("abort: raise --prec\n"); return; }
    {
        slong acc = WORD_MAX, kk;
        for (kk = 0; kk <= M; kk++) acc = FLINT_MIN(acc, arb_rel_accuracy_bits(arb_mat_entry(LE, kk, kk)));
        for (kk = 0; kk < M; kk++) acc = FLINT_MIN(acc, arb_rel_accuracy_bits(arb_mat_entry(LO, kk, kk)));
        flint_printf("#   worst relative accuracy of the pivots: %wd bits (of %wd; error control of every column below)\n", acc, prec);
    }
    fprintf(stderr, "axisN x=%g: build+ldl %.1fs\n", xd, now() - t0);

    flint_printf("#\n# Columns (row N = the bordering |n| <= N -> |n| <= N+1, new modes +-(N+1)):\n");
    flint_printf("#   s_e, s_o   Schur complements of the new even / odd basis vector (LDL pivots)\n");
    flint_printf("#   dI         Delta I_N = log(d_e/s_e) + log(d_o/s_o), d = new diagonal entries (nats)\n");
    flint_printf("#   dI_e       even part of dI\n");
    flint_printf("#   logdet     log det of the window matrix on |n| <= N (size 2N+1)\n");
    flint_printf("#   r_e, r_o   half-widths of the admissible interval of b_{N+1} given a_{N+1} and |n| <= N (Loewner-structured)\n");
    flint_printf("#   r_j        half-width of the intersection of the two intervals; tau_j = truth position in it (-1..1)\n");
    flint_printf("#   dIs        log-det gain of the truth over the structured MaxEnt point (joint maximiser)\n");
    flint_printf("#   b          b_{N+1} (for scale)\n");
    flint_printf("%5s %12s %12s %12s %12s %14s %11s %11s %11s %9s %11s %12s\n",
                 "N", "s_e", "s_o", "dI", "dI_e", "logdet", "r_e", "r_o", "r_j", "tau_j", "dIs", "b");

    arb_zero(logdetE); arb_zero(logdetO); arb_zero(sumdI);
    arb_log(logdetE, arb_mat_entry(LE, 0, 0), prec);
    cum = _arb_vec_init(Nmax + 2);          /* cum[N] = sum of Delta I over the borderings 1..N-1 */
    ldv = _arb_vec_init(Nmax + 2);          /* ldv[N] = log det of the window matrix on |n| <= N */
    for (N = 1; N <= Nmax; N++)
    {
        double tn = now();
        arb_log(t, arb_mat_entry(LE, N, N), prec); arb_add(logdetE, logdetE, t, prec);
        arb_log(t, arb_mat_entry(LO, N - 1, N - 1), prec); arb_add(logdetO, logdetO, t, prec);
        arb_add(logdet, logdetE, logdetO, prec);
        bordering(&r, E, O, LE, LO, N, prec);
        arb_set(cum + N, sumdI); arb_add(sumdI, sumdI, r.dI, prec);
        arb_set(ldv + N, logdet);
        flint_printf("%5wd %12s %12s %12s %12s %14s %11s %11s %11s %9s %11s %12s\n", N,
                     sb(r.se, 5), sb(r.so, 5), sb(r.dI, 6), sb(r.dI_e, 6), sb(logdet, 8),
                     sb(r.re, 4), sb(r.ro, 4), sb(r.rj, 4), sb(r.tau_j, 3), sb(r.dIs, 4), sb(b + N + 1, 6));
        if (N % 50 == 0) fprintf(stderr, "  N=%ld %.2fs\n", (long) N, now() - tn);
    }

    /* certified eps_N at the listed N, and the labelled comparison */
    if (cmp && *cmp)
    {
        char *list = strdup(cmp), *tok;
        arb_t eps, z1, gamma1, err, lasteps;
        arb_ptr v, lastv = NULL;
        slong lastN = 0;
        arb_init(eps); arb_init(z1); arb_init(gamma1); arb_init(err); arb_init(lasteps);
        flint_printf("#\n# certified minimal eigenvalue of the even block at selected N (zst_eigmin + deflated PD certificate)\n");
        flint_printf("# COMPARISON STEP (zeros of zeta used HERE ONLY, labelled; nothing above depends on them):\n");
        flint_printf("#   z_1 = 2 pi s_1 / L from the secular roots of the minimal even eigenvector (zst pipeline),\n");
        flint_printf("#   gamma_1 from acb_dirichlet_zeta_zeros; roots = certified positive secular roots (N = complete list)\n");
        flint_printf("#   eigenpair and roots at %wd bits (blocks rounded from %wd)\n", cprec, prec);
        zst_zeta_zeros(gamma1, 1, cprec);
        flint_printf("%5s %14s %12s %8s %12s %14s\n", "N", "eps_N", "even-simple", "roots", "|z1-g1|<=", "sum dI(<N)");
        for (tok = strtok(list, ","); tok; tok = strtok(NULL, ","))
        {
            slong Nc = atol(tok), nr, k, kk;
            arb_mat_t Ew, Ow;
            int es = 0, ok;
            mag_t m;
            double tc = now();
            if (Nc < 1 || Nc > M) continue;
            v = _arb_vec_init(Nc + 1);
            mag_init(m);
            /* the blocks rounded to cprec bits (balls stay valid: rounding only widens them) */
            arb_mat_init(Ew, Nc + 1, Nc + 1); arb_mat_init(Ow, Nc, Nc);
            for (k = 0; k <= Nc; k++) for (kk = 0; kk <= Nc; kk++) arb_set_round(arb_mat_entry(Ew, k, kk), arb_mat_entry(E, k, kk), cprec);
            for (k = 0; k < Nc; k++) for (kk = 0; kk < Nc; kk++) arb_set_round(arb_mat_entry(Ow, k, kk), arb_mat_entry(O, k, kk), cprec);
            ok = eig_min(eps, v, &es, Ew, Ow, 1, cprec);
            check(ok, "minimal even eigenpair certified");
            if (Nc <= 200 && Nc <= Nmax)
            {
                /* independent check of the pivot bookkeeping: preconditioned ball determinants */
                arb_t d1, d2;
                arb_init(d1); arb_init(d2);
                arb_mat_det(d1, Ew, cprec); arb_mat_det(d2, Ow, cprec);
                arb_mul(d1, d1, d2, cprec); arb_log(d1, d1, cprec);
                check(arb_overlaps(d1, ldv + Nc), "log det from LDL pivots = log det from arb_mat_det");
                arb_clear(d1); arb_clear(d2);
            }
            nr = first_root(z1, v, Nc, L, cprec);
            arb_sub(err, z1, gamma1, prec); arb_get_mag(m, err);
            /* sum of Delta I over the borderings 1..Nc-1 = total correlation log(prod d / det) beyond N=1 */
            flint_printf("%5wd %14s %12s %8wd %12s %14s\n", Nc, sb(eps, 6), es ? "CERTIFIED" : (ok ? "no" : "?"),
                         nr, smag(m), Nc <= Nmax ? sb(cum + Nc, 8) : "-");
            arb_mat_clear(Ew); arb_mat_clear(Ow);
            if (lastv) _arb_vec_clear(lastv, lastN + 1);
            lastv = v; lastN = Nc; arb_set(lasteps, eps);
            mag_clear(m);
            fprintf(stderr, "  cmp N=%ld %.1fs\n", (long) Nc, now() - tc);
        }
        free(list);
        if (lastv)
        {
            rayleigh_table(xd, X, L, lastN, lastv, lasteps, cprec);
            _arb_vec_clear(lastv, lastN + 1);
        }
        arb_clear(eps); arb_clear(z1); arb_clear(gamma1); arb_clear(err); arb_clear(lasteps);
    }

    border_clear(&r);
    if (cum) _arb_vec_clear(cum, Nmax + 2);
    if (ldv) _arb_vec_clear(ldv, Nmax + 2);
    _arb_vec_clear(a, M + 1); _arb_vec_clear(b, M + 1);
    arb_mat_clear(E); arb_mat_clear(O); arb_mat_clear(LE); arb_mat_clear(LO);
    arb_clear(x); arb_clear(L); arb_clear(t); arb_clear(logdetE); arb_clear(logdetO); arb_clear(logdet); arb_clear(sumdI);
}

/* intrinsic L^2(R_+^x, d*u) overlap of two even window functions (centred windows, log u = t in [-L/2, L/2]):
 * f = sum_j v_j phi_j^{L}, phi_0 = L^{-1/2}, phi_j = (-1)^j sqrt2 L^{-1/2} cos(2 pi j t / L)  (plan.md 1.1:
 * V_n(u) = L^{-1/2} exp(2 pi i n (t + L/2)/L)); int_{-h}^{h} cos(al t) cos(be t) dt = h [sinc((al-be)h) + sinc((al+be)h)]. */
static void l2_overlap(arb_t res, arb_srcptr v1, const arb_t L1, arb_srcptr v2, const arb_t L2, slong N, slong prec)
{
    slong j, m;
    arb_t h, al, be, s, t, u, pi, c;
    arb_init(h); arb_init(al); arb_init(be); arb_init(s); arb_init(t); arb_init(u); arb_init(pi); arb_init(c);
    arb_const_pi(pi, prec);
    arb_min(h, L1, L2, prec); arb_mul_2exp_si(h, h, -1);
    arb_zero(res);
    for (j = 0; j <= N; j++)
        for (m = 0; m <= N; m++)
        {
            arb_mul_ui(al, pi, 2 * j, prec); arb_div(al, al, L1, prec);
            arb_mul_ui(be, pi, 2 * m, prec); arb_div(be, be, L2, prec);
            arb_sub(t, al, be, prec); arb_mul(t, t, h, prec); arb_sinc(t, t, prec);
            arb_add(u, al, be, prec); arb_mul(u, u, h, prec); arb_sinc(u, u, prec);
            arb_add(s, t, u, prec); arb_mul(s, s, h, prec);
            /* times c_j c_m, c_0 = 1, c_j = sqrt2 (j >= 1) */
            if (j > 0 && m > 0) arb_mul_2exp_si(s, s, 1);
            else if (j > 0 || m > 0) { arb_sqrt_ui(c, 2, prec); arb_mul(s, s, c, prec); }
            if ((j + m) & 1) arb_neg(s, s);
            arb_mul(s, s, v1 + j, prec); arb_mul(s, s, v2 + m, prec);
            arb_add(res, res, s, prec);
        }
    /* normalisation (L1 L2)^{-1/2} */
    arb_mul(t, L1, L2, prec); arb_rsqrt(t, t, prec); arb_mul(res, res, t, prec);
    arb_clear(h); arb_clear(al); arb_clear(be); arb_clear(s); arb_clear(t); arb_clear(u); arb_clear(pi); arb_clear(c);
}

/* pole-term Loewner data alone (plan.md 1.2, as in riemann_ab.c): b = K n/den, a = K (L^2 - 16 pi^2 n^2)/den^2 */
static void pole_ab(arb_ptr a, arb_ptr b, slong N, const arb_t L, slong prec)
{
    arb_t K2, pi, t, den, u;
    slong n;
    arb_init(K2); arb_init(pi); arb_init(t); arb_init(den); arb_init(u);
    arb_const_pi(pi, prec);
    arb_mul_2exp_si(t, L, -2); arb_sinh(t, t, prec); arb_sqr(t, t, prec);
    arb_mul(K2, t, L, prec); arb_mul_ui(K2, K2, 32, prec);
    for (n = 0; n <= N; n++)
    {
        arb_mul_ui(t, pi, 4 * (ulong) n, prec); arb_sqr(t, t, prec);
        arb_sqr(den, L, prec); arb_add(den, den, t, prec);
        arb_mul_ui(b + n, K2, (ulong) n, prec); arb_div(b + n, b + n, den, prec);
        arb_sqr(u, L, prec); arb_sub(u, u, t, prec); arb_mul(u, u, K2, prec);
        arb_sqr(t, den, prec); arb_div(a + n, u, t, prec);
    }
    arb_zero(b + 0);
    arb_clear(K2); arb_clear(pi); arb_clear(t); arb_clear(den); arb_clear(u);
}

/* one prime-power term of the Loewner data at window L (plan.md 1.2, eq. `bomp` l.693 of mc2arXiv.tex, as
 * implemented in riemann_ab.c): b_n += (1/pi) w sin(omega_n log k), a_n += -2 w (1 - log k/L) cos(omega_n log k),
 * w = Lambda(k) k^{-1/2}, omega_n = 2 pi n/L. Writes the increment (not the total). The driver checks that
 * base (X = 1) + sum of increments reproduces zst_riemann_ab at the full cutoff, entry by entry. */
static void prime_term_ab(arb_ptr a, arb_ptr b, slong N, const arb_t L, ulong k, slong prec)
{
    arb_t y, w, t, om, sn, cs, pi, ed;
    ulong p = 0;
    slong n;
    arb_init(y); arb_init(w); arb_init(t); arb_init(om); arb_init(sn); arb_init(cs); arb_init(pi); arb_init(ed);
    is_prime_power(k, &p);
    arb_const_pi(pi, prec);
    arb_log_ui(y, k, prec);
    arb_log_ui(w, p, prec); arb_sqrt_ui(t, k, prec); arb_div(w, w, t, prec);
    arb_div(ed, y, L, prec); arb_sub_ui(ed, ed, 1, prec); arb_neg(ed, ed);      /* 1 - log k / L */
    for (n = 0; n <= N; n++)
    {
        arb_mul_ui(om, pi, 2 * (ulong) n, prec); arb_div(om, om, L, prec);
        arb_mul(t, om, y, prec);
        arb_sin_cos(sn, cs, t, prec);
        arb_mul(b + n, sn, w, prec); arb_div(b + n, b + n, pi, prec);
        arb_mul(a + n, cs, w, prec); arb_mul(a + n, a + n, ed, prec); arb_mul_si(a + n, a + n, -2, prec);
    }
    arb_zero(b + 0);
    arb_clear(y); arb_clear(w); arb_clear(t); arb_clear(om); arb_clear(sn); arb_clear(cs); arb_clear(pi); arb_clear(ed);
}

static char *negstr(slong k)
{
    static char buf[8][24];
    static int j = 0;
    char *out = buf[j = (j + 1) % 8];
    if (k < 0) strcpy(out, "?"); else snprintf(out, 24, "%ld", (long) k);
    return out;
}

static int vec_overlaps(arb_srcptr u, arb_srcptr v, slong n)
{
    slong i;
    for (i = 0; i < n; i++) if (!arb_overlaps(u + i, v + i)) return 0;
    return 1;
}

static void rayleigh(arb_t R, arb_srcptr a, arb_srcptr b, arb_srcptr v, slong N, slong prec)
{
    arb_mat_t E; arb_ptr w; slong i;
    arb_mat_init(E, N + 1, N + 1); w = _arb_vec_init(N + 1);
    zst_even_block(E, a, b, N, prec);
    for (i = 0; i <= N; i++) arb_dot(w + i, NULL, 0, arb_mat_entry(E, i, 0), 1, v, 1, N + 1, prec);
    arb_dot(R, NULL, 0, w, 1, v, 1, N + 1, prec);        /* v is unit */
    arb_mat_clear(E); _arb_vec_clear(w, N + 1);
}

/* Rayleigh decomposition of eps = v^T E v (v unit, the certified minimal even eigenvector) over the terms of
 * Psi = W02 - W_R - sum_k W_k at window L = log x, prime powers k <= X. The column `cumulative` is the Rayleigh
 * quotient of the same v under the partial-information form Psi_k (primes <= k only, same window). */
static void rayleigh_table(double xd, ulong X, const arb_t L, slong N, arb_srcptr v, const arb_t eps, slong prec)
{
    arb_ptr ap = _arb_vec_init(N + 1), bp = _arb_vec_init(N + 1), a1 = _arb_vec_init(N + 1), b1 = _arb_vec_init(N + 1);
    arb_ptr a2 = _arb_vec_init(N + 1), b2 = _arb_vec_init(N + 1);
    arb_t R, S, x;
    ulong p, k;
    arb_init(R); arb_init(S); arb_init(x);
    arb_set_d(x, xd);
    flint_printf("#\n# Rayleigh decomposition of eps at x = %g, N = %wd: eps = v^T E v (v unit) split over the terms of\n", xd, N);
    flint_printf("# Psi = W02 - W_R - sum_k W_k (each term's own Loewner block, same v); cumulative = v^T E(Psi_k) v,\n");
    flint_printf("# the Rayleigh quotient of v under the partial form with prime powers <= k only (same window)\n");
    pole_ab(ap, bp, N, L, prec);
    rayleigh(R, ap, bp, v, N, prec); arb_set(S, R);
    flint_printf("%10s %22s %22s\n", "term", "v^T E_term v", "cumulative");
    flint_printf("%10s %22s %22s\n", "pole", sb(R, 10), sb(S, 10));
    zst_riemann_ab(a1, b1, N, x, 1, prec);
    _arb_vec_sub(a2, a1, ap, N + 1, prec); _arb_vec_sub(b2, b1, bp, N + 1, prec);
    rayleigh(R, a2, b2, v, N, prec); arb_add(S, S, R, prec);
    flint_printf("%10s %22s %22s\n", "arch", sb(R, 10), sb(S, 10));
    /* a1, b1 accumulate base + prime terms; must reproduce zst_riemann_ab at the full cutoff */
    for (k = 2; k <= X; k++)
    {
        if (!is_prime_power(k, &p)) continue;
        prime_term_ab(a2, b2, N, L, k, prec);
        _arb_vec_add(a1, a1, a2, N + 1, prec); _arb_vec_add(b1, b1, b2, N + 1, prec);
        rayleigh(R, a2, b2, v, N, prec); arb_add(S, S, R, prec);
        flint_printf("%7s%3wu %22s %22s\n", "k = ", k, sb(R, 10), sb(S, 10));
    }
    zst_riemann_ab(a2, b2, N, x, X, prec);
    check(vec_overlaps(a1, a2, N + 1) && vec_overlaps(b1, b2, N + 1), "local prime terms reproduce zst_riemann_ab");
    flint_printf("%10s %22s\n", "eps", sb(eps, 10));
    check(arb_overlaps(S, eps), "Rayleigh parts sum to eps");
    _arb_vec_clear(ap, N + 1); _arb_vec_clear(bp, N + 1); _arb_vec_clear(a1, N + 1); _arb_vec_clear(b1, N + 1);
    _arb_vec_clear(a2, N + 1); _arb_vec_clear(b2, N + 1);
    arb_clear(R); arb_clear(S); arb_clear(x);
}

static void mode_axisx(slong N, double xmax, slong prec, int fixedL)
{
    ulong Xmax = (ulong) (xmax + 1e-9), k;
    slong nk = 0, i, K;
    double *knx; ulong *knX;
    arb_ptr *vs, Ls, lams, logdets, eps0;
    int *oks, *ess, *pds;
    slong *negs, *neg0, *npp;
    border_t *brd;
    arb_t x, L, t, u;
    arb_mat_t E, O, LE, LO;
    arb_ptr a, b, fa, fb, ta, tb;

    arb_init(x); arb_init(L); arb_init(t); arb_init(u);
    /* knots */
    knx = flint_malloc(sizeof(double) * (Xmax + 2)); knX = flint_malloc(sizeof(ulong) * (Xmax + 2));
    if (fixedL) { knx[nk] = xmax; knX[nk] = 1; nk++; }
    for (k = 2; k <= Xmax; k++)
        if (is_prime_power(k, NULL)) { knx[nk] = fixedL ? xmax : (double) k; knX[nk] = k; nk++; }
    if (!fixedL && !is_prime_power(Xmax, NULL)) { knx[nk] = xmax; knX[nk] = Xmax; nk++; }
    K = nk;

    vs = flint_malloc(sizeof(arb_ptr) * K);
    Ls = _arb_vec_init(K); lams = _arb_vec_init(K); logdets = _arb_vec_init(K); eps0 = _arb_vec_init(K);
    oks = flint_malloc(sizeof(int) * K); ess = flint_malloc(sizeof(int) * K); pds = flint_malloc(sizeof(int) * K);
    negs = flint_malloc(sizeof(slong) * K); neg0 = flint_malloc(sizeof(slong) * K); npp = flint_malloc(sizeof(slong) * K);
    brd = flint_malloc(sizeof(border_t) * K);
    a = _arb_vec_init(N + 2); b = _arb_vec_init(N + 2);
    fa = _arb_vec_init(N + 2); fb = _arb_vec_init(N + 2); ta = _arb_vec_init(N + 2); tb = _arb_vec_init(N + 2);
    arb_mat_init(E, N + 2, N + 2); arb_mat_init(O, N + 1, N + 1);
    arb_mat_init(LE, N + 2, N + 2); arb_mat_init(LO, N + 1, N + 1);

    flint_printf("# rtp1_a1 axisx (lane A1.3): the prime axis at fixed resolution N = %wd\n", N);
    flint_printf("# author claude:opus; driver zst/tools/rtp1_a1.c on libzst (FLINT %s); prec = %wd bits\n", FLINT_VERSION, prec);
    if (fixedL)
    {
        arb_set_d(x, xmax); zst_window_L(L, x, prec);
        flint_printf("# PROTOCOL fixed-L (partial-information form, NOT the CCM form except in the last row):\n");
        flint_printf("#   held fixed: window L = log %g = %s, Fourier modes |n| <= N, pole and archimedean terms;\n", xmax, sb(L, 15));
        flint_printf("#   varied: prime-power cutoff X (X = 1: no primes); the form is Psi_X = W02 - W_R - sum_{k<=X} W_k\n");
        flint_printf("#   restricted to the fixed window; each step adds exactly one closed-form prime-power term.\n");
    }
    else
    {
        flint_printf("# PROTOCOL CCM (the zst form at x = lambda^2):\n");
        flint_printf("#   held fixed: number of Fourier modes |n| <= N (so the matrix size), the rule 'prime powers <= x enter';\n");
        flint_printf("#   varied: x through the prime powers <= %g, and with it the window L = log x (all of a_n, b_n change,\n", xmax);
        flint_printf("#   the basis V_n is rescaled to the new window, and the prime power k = x enters with weight 0: its\n");
        flint_printf("#   a-weight (1 - log k/L) and b-phase sin(2 pi n log k/L) vanish at x = k, so the form is continuous in x).\n");
    }
    flint_printf("# overlap_c: |<v(x), v_final>| of unit coefficient vectors in the even basis (window rescaled to unit length)\n");
    if (!fixedL) flint_printf("# overlap_f: |<f_x, f_final>| in L^2(R_+^x, d*u) of the unit eigenfunctions on centred windows (intrinsic)\n");
    flint_printf("# eps: certified minimal eigenvalue of the even block; neg: certified number of negative even eigenvalues\n");
    flint_printf("# dI, r_j, tau_j: the bordering N -> N+1 at this knot, as in axisN (only when the block is PD)\n");

    for (i = 0; i < K; i++)
    {
        double tk = now();
        ulong p;
        slong nppk = 0;
        arb_t zero;
        arb_mat_t Ew, Ow;
        arb_init(zero);
        for (k = 2; k <= knX[i]; k++) nppk += is_prime_power(k, &p);
        npp[i] = nppk;
        arb_set_d(x, knx[i]);
        zst_window_L(Ls + i, x, prec);
        if (!fixedL) zst_riemann_ab(a, b, N + 1, x, knX[i], prec);
        else
        {
            /* fixed window: base (X = 1) once, then add the one new prime-power term per knot */
            if (i == 0) { zst_riemann_ab(fa, fb, N + 1, x, 1, prec); }
            else
            {
                prime_term_ab(ta, tb, N + 1, Ls + i, knX[i], prec);
                _arb_vec_add(fa, fa, ta, N + 2, prec); _arb_vec_add(fb, fb, tb, N + 2, prec);
            }
            _arb_vec_set(a, fa, N + 2); _arb_vec_set(b, fb, N + 2);
            if (i == K - 1)
            {
                zst_riemann_ab(ta, tb, N + 1, x, knX[i], prec);
                check(vec_overlaps(a, ta, N + 2) && vec_overlaps(b, tb, N + 2),
                      "fixed-L accumulation reproduces zst_riemann_ab at the full cutoff");
            }
        }
        zst_even_block(E, a, b, N + 1, prec);
        zst_odd_block(O, a, b, N + 1, prec);
        arb_mat_window_init(Ew, E, 0, 0, N + 1, N + 1);
        arb_mat_window_init(Ow, O, 0, 0, N, N);
        negs[i] = zst_inertia_neg(Ew, zero, prec);
        pds[i] = arb_mat_ldl(LE, E, prec) && arb_mat_ldl(LO, O, prec);
        vs[i] = _arb_vec_init(N + 1);
        oks[i] = eig_min(lams + i, vs[i], ess + i, Ew, Ow, pds[i], prec);
        {
            char msg[128];
            snprintf(msg, sizeof msg, "minimal even eigenpair certified (axisx, x = %g, X = %lu)", knx[i], (unsigned long) knX[i]);
            check(oks[i], msg);
        }
        border_init(brd + i);
        if (pds[i])
        {
            arb_zero(logdets + i);
            for (k = 0; k <= (ulong) N; k++) { arb_log(t, arb_mat_entry(LE, k, k), prec); arb_add(logdets + i, logdets + i, t, prec); }
            bordering(brd + i, E, O, LE, LO, N, prec);
        }
        else
        {
            arb_mat_det(t, Ew, prec); arb_abs(t, t); arb_log(logdets + i, t, prec);
        }
        /* prime-free control at the same window (CCM protocol only) */
        if (!fixedL)
        {
            /* its eigenvalues are O(1): 320 bits are ample (the balls say so) */
            arb_ptr v0 = _arb_vec_init(N + 1);
            int es0;
            slong cprec = FLINT_MIN(prec, 320);
            zst_riemann_ab(a, b, N, x, 1, cprec);
            zst_even_block(Ew, a, b, N, cprec);
            zst_odd_block(Ow, a, b, N, cprec);
            neg0[i] = zst_inertia_neg(Ew, zero, cprec);
            if (!eig_min(eps0 + i, v0, &es0, Ew, Ow, 0, cprec)) arb_indeterminate(eps0 + i);
            check(arb_is_finite(eps0 + i), "control minimal eigenvalue certified");
            _arb_vec_clear(v0, N + 1);
        }
        arb_mat_window_clear(Ew); arb_mat_window_clear(Ow);
        arb_clear(zero);
        fprintf(stderr, "  knot x=%g X=%lu %.1fs\n", knx[i], (unsigned long) knX[i], now() - tk);
    }

    flint_printf("%6s %4s %4s %14s %4s %5s %16s %12s %12s %10s %10s %7s\n", "x", "X", "#pp", "eps", "neg", "e-s",
                 "logdet_even", "overlap_c", fixedL ? "-" : "overlap_f", "dI", "r_j", "tau_j");
    for (i = 0; i < K; i++)
    {
        arb_t oc, of;
        arb_init(oc); arb_init(of);
        arb_dot(oc, NULL, 0, vs[i], 1, vs[K - 1], 1, N + 1, prec); arb_abs(oc, oc);
        if (!fixedL) { l2_overlap(of, vs[i], Ls + i, vs[K - 1], Ls + K - 1, N, FLINT_MIN(prec, 256)); arb_abs(of, of); }
        flint_printf("%6g %4wu %4wd %14s %4s %5s %16s %12s %12s %10s %10s %7s\n", knx[i], knX[i], npp[i], sb(lams + i, 6),
                     negstr(negs[i]),
                     ess[i] ? "yes" : "no", sb(logdets + i, 8), sb(oc, 8), fixedL ? "-" : sb(of, 8),
                     pds[i] ? sb(brd[i].dI, 5) : "-", pds[i] ? sb(brd[i].rj, 4) : "-", pds[i] ? sb(brd[i].tau_j, 3) : "-");
        arb_clear(oc); arb_clear(of);
    }

    if (!fixedL)
    {
        flint_printf("#\n# CONTROL (no arithmetic): pole + archimedean only (prime cutoff X = 1) at the same windows and N\n");
        flint_printf("%6s %16s %6s\n", "x", "lambda_min", "neg");
        for (i = 0; i < K; i++)
            flint_printf("%6g %16s %6wd\n", knx[i], sb(eps0 + i, 6), neg0[i]);

        rayleigh_table(knx[K - 1], knX[K - 1], Ls + K - 1, N, vs[K - 1], lams + K - 1, prec);
    }

    /* COMPARISON STEP */
    {
        arb_t gamma1, z1, err;
        mag_t m;
        arb_init(gamma1); arb_init(z1); arb_init(err); mag_init(m);
        zst_zeta_zeros(gamma1, 1, prec);
        flint_printf("#\n# COMPARISON STEP (zeros of zeta used HERE ONLY, labelled; nothing above depends on them):\n");
        flint_printf("#   z_1 = 2 pi s_1 / L from the secular roots of the minimal even eigenvector; gamma_1 = %s\n", sb(gamma1, 20));
        flint_printf("%6s %4s %8s %12s\n", "x", "X", "roots", "|z1-g1|<=");
        for (i = 0; i < K; i++)
        {
            slong nr = 0;
            double tc = now();
            if (oks[i]) { nr = first_root(z1, vs[i], N, Ls + i, pds[i] ? prec : FLINT_MIN(prec, 448)); arb_sub(err, z1, gamma1, prec); arb_get_mag(m, err); }
            flint_printf("%6g %4wu %8wd %12s\n", knx[i], knX[i], nr, (oks[i] && nr > 0) ? smag(m) : "-");
            fprintf(stderr, "  cmp x=%g %.1fs\n", knx[i], now() - tc);
        }
        arb_clear(gamma1); arb_clear(z1); arb_clear(err); mag_clear(m);
    }

    for (i = 0; i < K; i++) { _arb_vec_clear(vs[i], N + 1); border_clear(brd + i); }
    flint_free(vs); flint_free(brd);
    _arb_vec_clear(Ls, K); _arb_vec_clear(lams, K); _arb_vec_clear(logdets, K); _arb_vec_clear(eps0, K);
    flint_free(oks); flint_free(ess); flint_free(pds); flint_free(negs); flint_free(neg0); flint_free(npp);
    flint_free(knx); flint_free(knX);
    _arb_vec_clear(a, N + 2); _arb_vec_clear(b, N + 2);
    _arb_vec_clear(fa, N + 2); _arb_vec_clear(fb, N + 2); _arb_vec_clear(ta, N + 2); _arb_vec_clear(tb, N + 2);
    arb_mat_clear(E); arb_mat_clear(O); arb_mat_clear(LE); arb_mat_clear(LO);
    arb_clear(x); arb_clear(L); arb_clear(t); arb_clear(u);
}

int main(int argc, char **argv)
{
    const char *mode = "axisN", *cmp = "";
    double xd = 13, xmax = 50;
    slong Nmax = 120, N = 100, prec = 1000, cprec = 0;
    int fixedL = 0, i;
    for (i = 1; i + 1 < argc; i += 2)
    {
        if (!strcmp(argv[i], "--mode")) mode = argv[i + 1];
        else if (!strcmp(argv[i], "--x")) xd = atof(argv[i + 1]);
        else if (!strcmp(argv[i], "--xmax")) xmax = atof(argv[i + 1]);
        else if (!strcmp(argv[i], "--Nmax")) Nmax = atol(argv[i + 1]);
        else if (!strcmp(argv[i], "--N")) N = atol(argv[i + 1]);
        else if (!strcmp(argv[i], "--prec")) prec = atol(argv[i + 1]);
        else if (!strcmp(argv[i], "--cmp")) cmp = argv[i + 1];
        else if (!strcmp(argv[i], "--fixedL")) fixedL = atoi(argv[i + 1]);
        else if (!strcmp(argv[i], "--cprec")) cprec = atol(argv[i + 1]);
        else { fprintf(stderr, "unknown option %s\n", argv[i]); return 2; }
    }
    if (cprec <= 0) cprec = prec;
    if (!strcmp(mode, "axisN")) mode_axisN(xd, Nmax, prec, cmp, cprec);
    else if (!strcmp(mode, "axisx")) mode_axisx(N, xmax, prec, fixedL);
    else { fprintf(stderr, "unknown mode %s\n", mode); return 2; }
    flint_printf("#\n# checks: %wd run, %wd failed\n", n_checks, n_fail);
    flint_cleanup();
    return n_fail ? 1 : 0;
}
