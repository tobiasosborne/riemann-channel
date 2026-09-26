#define _POSIX_C_SOURCE 200809L
/* RTP-2 lane E, author codex:gpt-6-astra. Adapted from rtp1_a1.c (claude:opus).
 * Unchanged libzst. A1.1' bordering helpers retained verbatim. See lane report E3.
 * All reference-zero operations occur after the independent eigenpair/form computations.
 * Output tags ROW, SAT, EIG, CONTROL, COMP, RAY are consumed by checks/summary.py.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <flint/acb_mat.h>
#include <flint/fmpz_vec.h>
#include <flint/ulong_extras.h>
#include "zst.h"
static const char *curve = "11a1";
static const char *reference_path = "zst/tests/data/ell_ref.txt";
static fmpz *ainvs;
static fmpz_t conductor;
static slong curve_rank;
static int root_number;

/* K=0 reads only arithmetic metadata. Zero ordinates are read later, in COMPARISON. */
static int reference_zero(arb_t gamma, slong prec)
{
    fmpz *ai=_fmpz_vec_init(5);fmpz_t C;fmpz_init(C);int w;slong rank;
    int ok=zst_ell_ref(ai,C,&w,&rank,gamma,1,curve,reference_path,prec);
    _fmpz_vec_clear(ai,5);fmpz_clear(C);
    return ok&&arb_is_finite(gamma);
}

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
    if(n==1) {
        arb_set(lam,arb_mat_entry(E,0,0));arb_one(v);
        *es=zst_inertia_neg(O,lam,prec)==0;
        return arb_is_finite(lam);
    }
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

static void prime_term_ab(arb_ptr a, arb_ptr b, slong N, const arb_t L, ulong k, slong prec)
{
    arb_t y, w, t, om, sn, cs, pi, ed;
    ulong p = 0;
    slong n;
    arb_init(y); arb_init(w); arb_init(t); arb_init(om); arb_init(sn); arb_init(cs); arb_init(pi); arb_init(ed);
    is_prime_power(k, &p);
    arb_const_pi(pi, prec);
    arb_log_ui(y, k, prec);
    /* F4/F5: arithmetic t_m / p^m, NOT t_m / sqrt(p^m).
     * Independent local recurrence, checked against zst_weil_ellcurve below. */
    slong ap=zst_ell_ap(ainvs,p), t0=2, t1=ap, raw=ap;
    for(ulong pm=p;pm<k;pm*=p) {
        if(fmpz_fdiv_ui(conductor,p)) {slong tn=ap*t1-(slong)p*t0;t0=t1;t1=tn;raw=tn;}
        else raw*=ap;
    }
    arb_log_ui(w,p,prec);arb_mul_si(w,w,raw,prec);arb_div_ui(w,w,k,prec);
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

static int vec_overlaps(arb_srcptr u, arb_srcptr v, slong n)
{
    slong i;
    for (i = 0; i < n; i++) if (!arb_overlaps(u + i, v + i)) return 0;
    return 1;
}


static void ell_ab(arb_ptr a,arb_ptr b,slong N,const arb_t x,ulong X,slong prec)
{
    zst_weil_t W;
    zst_weil_ellcurve(&W,ainvs,conductor,x,X,prec);zst_weil_ab(a,b,N,&W,prec);
    zst_weil_clear(&W);
}
typedef struct {arb_t e,o;arb_ptr ve,vo;int par,es,ok;slong N;} pair_t;
static void pair_init(pair_t *p,slong N) {
    arb_init(p->e);arb_init(p->o);p->ve=_arb_vec_init(N+1);p->vo=_arb_vec_init(N);
    p->N=N;p->par=p->es=p->ok=0;
}
static void pair_clear(pair_t *p) {
    arb_clear(p->e);arb_clear(p->o);_arb_vec_clear(p->ve,p->N+1);_arb_vec_clear(p->vo,p->N);
}
static int pair_min(pair_t *p,const arb_mat_t E,const arb_mat_t O,int pd,slong prec)
{
    arb_t be,bo;arb_init(be);arb_init(bo);int se,so;
    /* Independent Rayleigh/PD brackets from parity.c on BOTH blocks, as requested. */
    int b1=zst_block_min(be,p->ve,E,150,prec),b2=zst_block_min(bo,p->vo,O,150,prec);
    check(b1&&b2,"zst_block_min brackets both blocks");
    int e1=eig_min(p->e,p->ve,&se,E,O,pd,prec);
    if(!e1&&pd)e1=eig_min(p->e,p->ve,&se,E,O,0,prec);
    int e2=eig_min(p->o,p->vo,&so,O,E,pd,prec);
    if(!e2&&pd)e2=eig_min(p->o,p->vo,&so,O,E,0,prec);
    check(e1&&e2,"Rump plus deflation certifies both simple block minima");
    check(b1&&e1&&arb_overlaps(be,p->e)&&b2&&e2&&arb_overlaps(bo,p->o),"independent minimum certificates agree");
    /* Intersect two independent certificates of the SAME minima. The Rump route above
     * also proves block minimality by deflated PD, so this is not mere root overlap. */
    int rawpar=(b1&&b2&&arb_lt(be,bo))?1:(b1&&b2&&arb_lt(bo,be))?-1:0;
    if(b1&&e1)check(arb_intersection(be,be,p->e,prec),"intersect certified even minima");
    if(b2&&e2)check(arb_intersection(bo,bo,p->o,prec),"intersect certified odd minima");
    p->par=(b1&&b2&&e1&&e2&&arb_lt(be,bo))?1:(b1&&b2&&e1&&e2&&arb_lt(bo,be))?-1:0;
    if(!rawpar)flint_printf("# parity: raw block_min brackets overlap; independent deflated-minimum certificates separate them\n");
    check(p->par!=0,"global minimum parity separated by certified minimum intersections");
    p->es=se;p->ok=e1&&e2&&p->par!=0;
    arb_clear(be);arb_clear(bo);return p->ok;
}
static void rayleigh(arb_t R,arb_srcptr a,arb_srcptr b,arb_srcptr v,slong N,int par,slong prec)
{
    slong n=N+(par>0);arb_mat_t A;arb_ptr w=_arb_vec_init(n);arb_mat_init(A,n,n);
    if(par>0)zst_even_block(A,a,b,N,prec);else zst_odd_block(A,a,b,N,prec);
    for(slong i=0;i<n;i++)arb_dot(w+i,NULL,0,arb_mat_entry(A,i,0),1,v,1,n,prec);
    arb_dot(R,NULL,0,w,1,v,1,n,prec);arb_mat_clear(A);_arb_vec_clear(w,n);
}
static void rayleigh_table(double xd,ulong X,const arb_t L,const pair_t *p,slong prec)
{
    slong N=p->N;arb_srcptr v=p->par>0?p->ve:p->vo,eps=p->par>0?p->e:p->o;
    arb_ptr a=_arb_vec_init(N+1),b=_arb_vec_init(N+1),ta=_arb_vec_init(N+1),tb=_arb_vec_init(N+1);
    arb_t x,R,S,A,P;arb_init(x);arb_init(R);arb_init(S);arb_init(A);arb_init(P);arb_set_d(x,xd);
    ell_ab(a,b,N,x,1,prec);rayleigh(A,a,b,v,N,p->par,prec);arb_set(S,A);
    flint_printf("RAY x=%g N=%wd parity=%d term=arch value=%s\n",xd,N,p->par,sb(A,12));
    for(ulong k=2;k<=X;k++)if(is_prime_power(k,NULL)) {
        prime_term_ab(ta,tb,N,L,k,prec);_arb_vec_add(a,a,ta,N+1,prec);_arb_vec_add(b,b,tb,N+1,prec);
        rayleigh(R,ta,tb,v,N,p->par,prec);arb_add(P,P,R,prec);arb_add(S,S,R,prec);
        flint_printf("RAY x=%g N=%wd term=k%wu value=%s cumulative=%s\n",xd,N,k,sb(R,12),sb(S,12));
    }
    ell_ab(ta,tb,N,x,X,prec);
    check(vec_overlaps(a,ta,N+1)&&vec_overlaps(b,tb,N+1),"elliptic local local terms reproduce generic builder");
    check(arb_overlaps(S,eps),"Rayleigh decomposition sums to certified minimum");
    flint_printf("RAY_TOTAL x=%g N=%wd arch=%s primes=%s sum=%s eps=%s\n",xd,N,sb(A,12),sb(P,12),sb(S,12),sb(eps,12));
    _arb_vec_clear(a,N+1);_arb_vec_clear(b,N+1);_arb_vec_clear(ta,N+1);_arb_vec_clear(tb,N+1);
    arb_clear(x);arb_clear(R);arb_clear(S);arb_clear(A);arb_clear(P);
}
static void control(double xd,slong N,slong prec)
{
    /* X=1 includes gamma + log(C) I, no poles, no prime atoms. */
    slong cp=FLINT_MIN(prec,320);arb_t x,z,le,lo;arb_init(x);arb_init(z);arb_init(le);arb_init(lo);arb_set_d(x,xd);
    arb_ptr a=_arb_vec_init(N+1),b=_arb_vec_init(N+1),v=_arb_vec_init(N+1);
    arb_mat_t E,O;arb_mat_init(E,N+1,N+1);arb_mat_init(O,N,N);ell_ab(a,b,N,x,1,cp);
    zst_even_block(E,a,b,N,cp);zst_odd_block(O,a,b,N,cp);
    slong ne=zst_inertia_neg(E,z,cp),no=zst_inertia_neg(O,z,cp);int es;
    int ok=eig_min(le,v,&es,E,O,0,cp)&&eig_min(lo,v,&es,O,E,0,cp);
    check(ok&&ne>=0&&no>=0,"archimedean control minima and inertia certified");
    flint_printf("CONTROL x=%g N=%wd minE=%s minO=%s negE=%wd posE=%wd negO=%wd posO=%wd\n",xd,N,sb(le,12),sb(lo,12),ne,N+1-ne,no,N-no);
    arb_clear(x);arb_clear(z);arb_clear(le);arb_clear(lo);_arb_vec_clear(a,N+1);_arb_vec_clear(b,N+1);_arb_vec_clear(v,N+1);arb_mat_clear(E);arb_mat_clear(O);
}
static void comparison(double xd,ulong X,const arb_t L,const pair_t *p,const arb_t gamma,slong prec)
{
    arb_t z,err,ratio;arb_init(z);arb_init(err);arb_init(ratio);slong nr=0;
    if(curve_rank>0) {
        flint_printf("COMP x=%g X=%wu N=%wd parity=%d roots=0 status=RANK_POSITIVE_NO_COMPARISON\n",xd,X,p->N,p->par);
        arb_clear(z);arb_clear(err);arb_clear(ratio);return;
    }
    if(p->ok&&p->par>0)nr=first_root(z,p->ve,p->N,L,prec);
    if(nr>0) {
        arb_sub(err,z,gamma,prec);arb_abs(err,err);arb_div(ratio,err,p->e,prec);
        flint_printf("COMP x=%g X=%wu N=%wd parity=%d roots=%wd z1=%s error=%s ratio=%s\n",xd,X,p->N,p->par,nr,sb(z,18),sb(err,12),sb(ratio,12));
        check(nr==p->N,"complete positive even secular root set in comparison");
    } else flint_printf("COMP x=%g X=%wu N=%wd parity=%d roots=0 status=%s\n",xd,X,p->N,p->par,p->par<0?"ODD_CCM_INAPPLICABLE":"NO_ROOTS");
    arb_clear(z);arb_clear(err);arb_clear(ratio);
}
static void eigen_line(double x,ulong X,const pair_t *p,slong ne,slong no)
{
    flint_printf("EIG x=%g X=%wu N=%wd epsE=%s epsO=%s parity=%d even_simple=%d negE=%wd negO=%wd\n",x,X,p->N,sb(p->e,12),sb(p->o,12),p->par,p->es,ne,no);
}
static slong sat(arb_srcptr vals,slong Nmax,const char *label)
{
    slong n=1;for(slong i=2;i<=Nmax;i++)if(arb_lt(vals+i,vals+n))n=i;
    int ok=1;for(slong i=1;i<=Nmax;i++)if(i!=n&&!arb_lt(vals+n,vals+i))ok=0;
    check(ok,"unique argmin log determinant certified over scanned N");
    flint_printf("SAT block=%s N=%wd logdet=%s unique=%d range_max=%wd\n",label,n,sb(vals+n,14),ok,Nmax);return n;
}
static void mode_axisN(double xd,slong Nmax,slong prec,const char *cmp,slong cprec)
{
    slong M=Nmax+1;ulong X=(ulong)xd;double start=now();
    arb_t x,L,t;arb_init(x);arb_init(L);arb_init(t);arb_set_d(x,xd);zst_window_L(L,x,prec);
    arb_ptr a=_arb_vec_init(M+1),b=_arb_vec_init(M+1),de=_arb_vec_init(M+1),doo=_arb_vec_init(M+1),df=_arb_vec_init(M+1);
    arb_mat_t E,O,LE,LO;arb_mat_init(E,M+1,M+1);arb_mat_init(O,M,M);arb_mat_init(LE,M+1,M+1);arb_mat_init(LO,M,M);
    flint_printf("# axisN curve=%s C=%wd x=%g Nmax=%wd prec=%wd cprec=%wd\n",curve,fmpz_get_si(conductor),xd,Nmax,prec,cprec);
    ell_ab(a,b,M,x,X,prec);zst_even_block(E,a,b,M,prec);zst_odd_block(O,a,b,M,prec);
    for(slong n=0;n<4;n++)flint_printf("AB n=%wd a=%s b=%s\n",n,sb(a+n,30),sb(b+n,30));
    int pd=arb_mat_ldl(LE,E,prec)&&arb_mat_ldl(LO,O,prec);check(pd,"full ball LDL of both blocks positive");
    if(!pd){flint_printf("# abort: raise precision\n");goto done;}
    slong acc=WORD_MAX;for(slong n=0;n<=M;n++)acc=FLINT_MIN(acc,arb_rel_accuracy_bits(arb_mat_entry(LE,n,n)));
    for(slong n=0;n<M;n++)acc=FLINT_MIN(acc,arb_rel_accuracy_bits(arb_mat_entry(LO,n,n)));
    flint_printf("# pivot_accuracy_bits=%wd\n",acc);
    arb_log(de,arb_mat_entry(LE,0,0),prec);
    for(slong n=1;n<=Nmax;n++) {
        border_t r;border_init(&r);bordering(&r,E,O,LE,LO,n,prec);
        arb_log(t,arb_mat_entry(LE,n,n),prec);arb_add(de+n,de+n-1,t,prec);
        arb_log(t,arb_mat_entry(LO,n-1,n-1),prec);arb_add(doo+n,doo+n-1,t,prec);arb_add(df+n,de+n,doo+n,prec);
        flint_printf("ROW N=%wd logdet=%s logdetE=%s logdetO=%s sE=%s sO=%s dI=%s rE=%s rO=%s rj=%s tau=%s dIs=%s\n",n,sb(df+n,14),sb(de+n,14),sb(doo+n,14),sb(r.se,10),sb(r.so,10),sb(r.dI,10),sb(r.re,10),sb(r.ro,10),sb(r.rj,10),sb(r.tau_j,10),sb(r.dIs,10));border_clear(&r);
    }
    slong ns=sat(df,Nmax,"full");sat(de,Nmax,"even");sat(doo,Nmax,"odd");
    int *selected=calloc(M+1,sizeof(int));selected[ns]=selected[Nmax]=1;
    if(cmp&&*cmp){char *list=strdup(cmp);for(char *tok=strtok(list,",");tok;tok=strtok(NULL,",")){slong n=atol(tok);if(n>=1&&n<=Nmax)selected[n]=1;}free(list);}
    pair_t *pairs=calloc(M+1,sizeof(pair_t));
    for(slong n=1;n<=Nmax;n++)if(selected[n]) {
        arb_mat_t Ew,Ow;arb_mat_init(Ew,n+1,n+1);arb_mat_init(Ow,n,n);
        for(slong i=0;i<=n;i++)for(slong j=0;j<=n;j++)arb_set_round(arb_mat_entry(Ew,i,j),arb_mat_entry(E,i,j),cprec);
        for(slong i=0;i<n;i++)for(slong j=0;j<n;j++)arb_set_round(arb_mat_entry(Ow,i,j),arb_mat_entry(O,i,j),cprec);
        pair_init(pairs+n,n);pair_min(pairs+n,Ew,Ow,1,cprec);eigen_line(xd,X,pairs+n,0,0);
        control(xd,n,prec);arb_mat_clear(Ew);arb_mat_clear(Ow);
        fprintf(stderr,"curve=%s x=%g N=%ld eigenpair/control finished %.1fs\n",curve,xd,(long)n,now()-start);fflush(stdout);
    }
    rayleigh_table(xd,X,L,pairs+Nmax,cprec);
    flint_printf("# COMPARISON STEP: zeros used only below, never to choose a form or eigenpair\n");
    arb_t gamma;arb_init(gamma);
    if(curve_rank==0)check(reference_zero(gamma,cprec),"PARI reference read in comparison only");
    flint_printf("REFERENCE curve=%s gamma1=%s certified_unique=0 index=PARI radius=1e-38 rank=%wd\n",curve,sb(gamma,30),curve_rank);
    for(slong n=1;n<=Nmax;n++)if(selected[n]){comparison(xd,X,L,pairs+n,gamma,cprec);pair_clear(pairs+n);}
    arb_clear(gamma);free(selected);free(pairs);
done:
    arb_clear(x);arb_clear(L);arb_clear(t);_arb_vec_clear(a,M+1);_arb_vec_clear(b,M+1);_arb_vec_clear(de,M+1);_arb_vec_clear(doo,M+1);_arb_vec_clear(df,M+1);
    arb_mat_clear(E);arb_mat_clear(O);arb_mat_clear(LE);arb_mat_clear(LO);
}
static void mode_axisx(slong N,double xmax,slong prec,int fixedL)
{
    ulong Xmax=(ulong)xmax,ks[256];slong K=0;
    if(fixedL)ks[K++]=1;
    for(ulong k=2;k<=Xmax;k++)if(is_prime_power(k,NULL))ks[K++]=k;
    if(!fixedL&&!is_prime_power(Xmax,NULL))ks[K++]=Xmax;
    pair_t *pairs=calloc(K,sizeof(pair_t));arb_ptr lengths=_arb_vec_init(K);
    arb_t x,t,z;arb_init(x);arb_init(t);arb_init(z);
    arb_ptr a=_arb_vec_init(N+2),b=_arb_vec_init(N+2),fa=_arb_vec_init(N+2),fb=_arb_vec_init(N+2),ta=_arb_vec_init(N+2),tb=_arb_vec_init(N+2);
    arb_mat_t E,O,LE,LO;arb_mat_init(E,N+2,N+2);arb_mat_init(O,N+1,N+1);arb_mat_init(LE,N+2,N+2);arb_mat_init(LO,N+1,N+1);
    flint_printf("# axisx curve=%s C=%wd N=%wd xmax=%g prec=%wd fixedL=%d\n",curve,fmpz_get_si(conductor),N,xmax,prec,fixedL);
    flint_printf("# CCM changes window and primes; fixedL changes only cutoff, including zero elliptic weights.\n");
    for(slong i=0;i<K;i++) {
        double xd=fixedL?xmax:ks[i],start=now();arb_set_d(x,xd);zst_window_L(lengths+i,x,prec);
        ell_ab(a,b,N+1,x,ks[i],prec);
        if(fixedL) {
            if(i==0){_arb_vec_set(fa,a,N+2);_arb_vec_set(fb,b,N+2);}
            else {prime_term_ab(ta,tb,N+1,lengths+i,ks[i],prec);_arb_vec_add(fa,fa,ta,N+2,prec);_arb_vec_add(fb,fb,tb,N+2,prec);}
            check(vec_overlaps(a,fa,N+2)&&vec_overlaps(b,fb,N+2),"fixed-L accumulation agrees at every cutoff");
        }
        zst_even_block(E,a,b,N+1,prec);zst_odd_block(O,a,b,N+1,prec);
        int pd=arb_mat_ldl(LE,E,prec)&&arb_mat_ldl(LO,O,prec);
        arb_mat_t Ew,Ow;arb_mat_window_init(Ew,E,0,0,N+1,N+1);arb_mat_window_init(Ow,O,0,0,N,N);
        slong ne=zst_inertia_neg(Ew,z,prec),no=zst_inertia_neg(Ow,z,prec);check(ne>=0&&no>=0,"both inertia counts decisive");
        pair_init(pairs+i,N);pair_min(pairs+i,Ew,Ow,pd,prec);eigen_line(xd,ks[i],pairs+i,ne,no);
        if(pd) {
            border_t r;border_init(&r);bordering(&r,E,O,LE,LO,N,prec);
            arb_t de,doo;arb_init(de);arb_init(doo);
            for(slong k=0;k<=N;k++){arb_log(t,arb_mat_entry(LE,k,k),prec);arb_add(de,de,t,prec);}
            for(slong k=0;k<N;k++){arb_log(t,arb_mat_entry(LO,k,k),prec);arb_add(doo,doo,t,prec);}
            flint_printf("KNOT x=%g X=%wu N=%wd logdetE=%s logdetO=%s dI=%s rj=%s tau=%s\n",xd,ks[i],N,sb(de,12),sb(doo,12),sb(r.dI,10),sb(r.rj,10),sb(r.tau_j,10));arb_clear(de);arb_clear(doo);border_clear(&r);
        } else flint_printf("KNOT x=%g X=%wu N=%wd status=INDEFINITE\n",xd,ks[i],N);
        arb_mat_window_clear(Ew);arb_mat_window_clear(Ow);
        if(!fixedL)control(xd,N,prec);
        fprintf(stderr,"curve=%s knot x=%g X=%lu %.1fs\n",curve,xd,ks[i],now()-start);fflush(stdout);
    }
    for(slong i=0;i<K;i++) {
        int p=pairs[i].par;arb_zero(t);
        if(p==pairs[K-1].par)arb_dot(t,NULL,0,p>0?pairs[i].ve:pairs[i].vo,1,p>0?pairs[K-1].ve:pairs[K-1].vo,1,N+(p>0),prec);
        arb_abs(t,t);flint_printf("OVERLAP x=%g X=%wu coefficient=%s\n",fixedL?xmax:(double)ks[i],ks[i],sb(t,12));
    }
    rayleigh_table(xmax,ks[K-1],lengths+K-1,pairs+K-1,prec);
    flint_printf("# COMPARISON STEP; indefinite partial forms have no CCM interpretation\n");
    arb_t gamma;arb_init(gamma);
    if(curve_rank==0)check(reference_zero(gamma,prec),"PARI reference read in comparison only");
    flint_printf("REFERENCE curve=%s gamma1=%s certified_unique=0 index=PARI radius=1e-38 rank=%wd\n",curve,sb(gamma,30),curve_rank);
    for(slong i=0;i<K;i++) {
        if(arb_is_positive(pairs[i].e)&&arb_is_positive(pairs[i].o))comparison(fixedL?xmax:(double)ks[i],ks[i],lengths+i,pairs+i,gamma,prec);
        pair_clear(pairs+i);
    }
    arb_clear(gamma);free(pairs);_arb_vec_clear(lengths,K);arb_clear(x);arb_clear(t);arb_clear(z);
    _arb_vec_clear(a,N+2);_arb_vec_clear(b,N+2);_arb_vec_clear(fa,N+2);_arb_vec_clear(fb,N+2);_arb_vec_clear(ta,N+2);_arb_vec_clear(tb,N+2);
    arb_mat_clear(E);arb_mat_clear(O);arb_mat_clear(LE);arb_mat_clear(LO);
}
int main(int argc,char **argv)
{
    const char *mode="axisN",*cmp="";double xd=13,xmax=50;slong Nmax=200,N=60,prec=1000,cprec=0;int fixedL=0;
    if(argc%2!=1)return 2;
    for(int i=1;i+1<argc;i+=2) {
        if(!strcmp(argv[i],"--curve"))curve=argv[i+1];
        else if(!strcmp(argv[i],"--ref"))reference_path=argv[i+1];
        else if(!strcmp(argv[i],"--mode"))mode=argv[i+1];
        else if(!strcmp(argv[i],"--x"))xd=atof(argv[i+1]);
        else if(!strcmp(argv[i],"--xmax"))xmax=atof(argv[i+1]);
        else if(!strcmp(argv[i],"--Nmax"))Nmax=atol(argv[i+1]);
        else if(!strcmp(argv[i],"--N"))N=atol(argv[i+1]);
        else if(!strcmp(argv[i],"--prec"))prec=atol(argv[i+1]);
        else if(!strcmp(argv[i],"--cprec"))cprec=atol(argv[i+1]);
        else if(!strcmp(argv[i],"--fixedL"))fixedL=atoi(argv[i+1]);
        else if(!strcmp(argv[i],"--cmp"))cmp=argv[i+1];
        else {fprintf(stderr,"unknown option %s\n",argv[i]);return 2;}
    }
    if(!cprec)cprec=prec;
    if(xd<=1||xd>250||xmax<=1||xmax>250||N<1||Nmax<3||prec<128||cprec<128)return 2;
    ainvs=_fmpz_vec_init(5);fmpz_init(conductor);
    if(!zst_ell_ref(ainvs,conductor,&root_number,&curve_rank,NULL,0,curve,reference_path,prec)) {
        fprintf(stderr,"curve metadata absent: %s\n",curve);return 2;
    }
    flint_printf("# rtp2_ellcurve; author codex:gpt-6-astra; FLINT %s; certified forms/eigenpairs; PARI comparisons approximate\n",FLINT_VERSION);
    flint_printf("# curve=%s C=%wd rank=%wd root_number=%d; gamma (Q,d,mu)=(1/(2pi),1,1); no poles\n",curve,fmpz_get_si(conductor),curve_rank,root_number);
    if(!strcmp(mode,"axisN"))mode_axisN(xd,Nmax,prec,cmp,cprec);
    else if(!strcmp(mode,"axisx"))mode_axisx(N,xmax,prec,fixedL);else return 2;
    flint_printf("# checks: %wd run, %wd failed\n",n_checks,n_fail);_fmpz_vec_clear(ainvs,5);fmpz_clear(conductor);flint_cleanup();return n_fail?1:0;
}
