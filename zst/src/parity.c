/* parity.c: the certified MINIMUM eigenvalue of a symmetric block, and the parity (even/odd) of the
 * global minimum of the truncated Weil form.
 *
 * Why this module exists. zst_eigmin (src/eigmin.c) runs inverse iteration, which converges to the
 * eigenvalue nearest the target 0, i.e. to the eigenvalue of SMALLEST MODULUS. That is the minimum
 * only for a positive semidefinite block. The MVP-3 objects are not positive: for 37a1 and 389a1 the
 * Weil form has eigenvalues of both signs at some windows. So the block is shifted below its minimum
 * before the inverse iteration, and the shift is undone exactly.
 *
 * What is certified, and why not by the Rump eigenpair box alone. The enclosure of zst_eigmin is
 * valid only once its inverse iteration has converged: with a shift far below the spectrum the
 * convergence ratio (lambda_1 - sigma)/(lambda_2 - sigma) is close to 1, the iteration stops far
 * from the eigenvector, and the Krawczyk contraction then returns a tight box around the Newton
 * limit of the bordered system which need not contain any eigenvalue at all (reproduced in
 * tests/test_parity.c: A = H diag(-3,-1,2,5) H shifted by 8I, 10 to 40 iterations, returns
 * 5.0000136... with radius 1e-30 while the spectrum is {5, 7, 10, 13}). This module therefore does
 * not rely on that box. It brackets lambda_min(A) between two independent rigorous bounds:
 *
 *   upper:  lambda_min(A) <= R(v) = (v^T A v)/(v^T v)  for any real v != 0  (Rayleigh-Ritz),
 *           evaluated in ball arithmetic on the ball vector v, so upper(R(v)) bounds the quotient of
 *           every vector in the ball and in particular of its midpoint;
 *   lower:  lambda_min(A) >= sigma whenever A - sigma is certified positive definite.
 *
 * zst_eigmin is used only to produce the vector v, and is given a shift just below lambda_min so
 * that it converges in a couple of steps; the Rayleigh quotient is then accurate to the square of
 * the residual, and the certified bracket [sigma, upper(R(v))] is driven down to the noise floor of
 * the positive-definiteness certificate by a second (refinement) pass.
 *
 * Ground truth for the use of the parity: notes/zeta-spectral-triples/ellcurve/astra-review.md,
 * "Q1: what the structure says" (the minimal eigenvector of the full Weil form is odd for 37a1 at
 * x = 8, 13, 20 and for 389a1 at x = 13, so the paper's even-simple hypothesis, Definition
 * `even-simple` at refs/src/2511.22755/mc2arXiv.tex l.850, fails and the rank-one construction of
 * Lemma `key` l.863-936 is inapplicable there), and "Changes I recommend to the plan", item 5. */
#include "zst.h"

/* Verified positive definiteness (Rump's isspd), the same device as the static verify_pd of
 * src/eigmin.c, reimplemented here because that one is not exported and its only public wrapper
 * (zst_certify_even_simple) also performs the rank-one deflation. The exported zst_inertia_neg is
 * NOT usable for this: its unpivoted ball LDL^T amplifies the input radii by the condition number
 * and goes inconclusive on the larger windows (measured: the zeta even block at x = 30, N = 120,
 * 700 bits, entry radii 2e-201, fails at pivot 88 with a ball of width 14 for every shift tried).
 *
 * With delta = 2^-(prec/2) max_i |F_ii|, an approximate Cholesky factor Lt of mid(F) - delta I is
 * computed in midpoint arithmetic and r = ||F - delta I - Lt Lt^T||_inf is bounded in ball
 * arithmetic. Lt Lt^T is positive semidefinite for any real Lt, so F >= (delta - r) I, and
 * delta > r certifies F positive definite. Returns 1 if certified. */
static int
verify_pd(const arb_mat_t F, slong prec)
{
    slong n = arb_mat_nrows(F), i, j, k;
    arb_mat_t Lt, Rm;
    arb_t delta, t;
    mag_t r, d;
    int ok = 1;
    if (n == 0) return 1;
    arb_mat_init(Lt, n, n); arb_mat_init(Rm, n, n);
    arb_init(delta); arb_init(t); mag_init(r); mag_init(d);
    for (i = 0; i < n; i++)
    {
        arb_get_mid_arb(t, arb_mat_entry(F, i, i)); arb_abs(t, t);
        if (arb_gt(t, delta)) arb_set(delta, t);
    }
    arb_mul_2exp_si(delta, delta, -(prec / 2));
    arb_get_mid_arb(delta, delta);
    for (j = 0; j < n && ok; j++)                     /* Cholesky-Banachiewicz on midpoints */
    {
        arb_get_mid_arb(t, arb_mat_entry(F, j, j)); arb_sub(t, t, delta, prec);
        for (k = 0; k < j; k++) arb_submul(t, arb_mat_entry(Lt, j, k), arb_mat_entry(Lt, j, k), prec);
        arb_get_mid_arb(t, t);
        if (!arb_is_positive(t)) { ok = 0; break; }
        arb_sqrt(arb_mat_entry(Lt, j, j), t, prec);
        arb_get_mid_arb(arb_mat_entry(Lt, j, j), arb_mat_entry(Lt, j, j));
        for (i = j + 1; i < n; i++)
        {
            arb_get_mid_arb(t, arb_mat_entry(F, i, j));
            for (k = 0; k < j; k++) arb_submul(t, arb_mat_entry(Lt, i, k), arb_mat_entry(Lt, j, k), prec);
            arb_div(t, t, arb_mat_entry(Lt, j, j), prec);
            arb_get_mid_arb(arb_mat_entry(Lt, i, j), t);
        }
    }
    if (ok)
    {
        for (i = 0; i < n; i++)
            for (j = 0; j < n; j++)
            {
                arb_dot(arb_mat_entry(Rm, i, j), arb_mat_entry(F, i, j), 1,
                        arb_mat_entry(Lt, i, 0), 1, arb_mat_entry(Lt, j, 0), 1, FLINT_MIN(i, j) + 1, prec);
                if (i == j) arb_sub(arb_mat_entry(Rm, i, i), arb_mat_entry(Rm, i, i), delta, prec);
            }
        arb_mat_bound_inf_norm(r, Rm);                /* ||.||_2 <= ||.||_inf for symmetric matrices */
        arb_get_mag_lower(d, delta);
        ok = mag_cmp(r, d) < 0;
    }
    arb_mat_clear(Lt); arb_mat_clear(Rm);
    arb_clear(delta); arb_clear(t); mag_clear(r); mag_clear(d);
    return ok;
}

/* An exact point s0 <= lambda_min(A) for every A in the ball matrix: s0 = -(upper(||A||_F) + 1),
 * since |lambda| <= ||A||_2 <= ||A||_F for a real symmetric A. Needs no certificate. */
static void
frobenius_floor(arf_t s0, const arb_mat_t A, slong prec)
{
    slong n = arb_mat_nrows(A), i, j;
    arb_t f;
    arb_init(f);
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            arb_addmul(f, arb_mat_entry(A, i, j), arb_mat_entry(A, i, j), prec);
    arb_sqrt(f, f, prec);
    arb_add_ui(f, f, 1, prec);
    arb_get_ubound_arf(s0, f, prec);
    arf_neg(s0, s0);
    arb_clear(f);
}

/* Largest certified lower bound of the form anchor - g that positive definiteness confirms, starting
 * at g = g0 and multiplying g by 2^step after each refutation (at most `tries`). B is scratch. */
static int
certified_floor(arf_t sigma, const arb_mat_t A, arb_mat_t B, const arf_t anchor, const arf_t g0,
                slong step, slong tries, slong prec)
{
    slong n = arb_mat_nrows(A), i, k;
    arf_t g, s;
    int ok = 0;
    arf_init(g); arf_init(s);
    arf_set(g, g0);
    for (k = 0; k < tries && !ok; k++)
    {
        arf_sub(s, anchor, g, prec, ARF_RND_DOWN);
        arb_mat_set(B, A);
        for (i = 0; i < n; i++)
            arb_sub_arf(arb_mat_entry(B, i, i), arb_mat_entry(B, i, i), s, prec);
        if (verify_pd(B, prec)) { arf_set(sigma, s); ok = 1; }
        else arf_mul_2exp_si(g, g, step);
    }
    arf_clear(g); arf_clear(s);
    return ok;
}

/* Rayleigh quotient (v^T A v)/(v^T v) of a ball vector; upper(rho) bounds lambda_min(A) above. */
static void
rayleigh(arb_t rho, const arb_mat_t A, arb_srcptr v, slong prec)
{
    slong n = arb_mat_nrows(A), i;
    arb_t num, den, t;
    arb_init(num); arb_init(den); arb_init(t);
    for (i = 0; i < n; i++)
    {
        arb_dot(t, NULL, 0, arb_mat_entry(A, i, 0), 1, v, 1, n, prec);
        arb_addmul(num, t, v + i, prec);
        arb_addmul(den, v + i, v + i, prec);
    }
    arb_div(rho, num, den, prec);
    arb_clear(num); arb_clear(den); arb_clear(t);
}

int zst_block_min(arb_t lam, arb_ptr v, const arb_mat_t A, slong iters, slong prec)
{
    slong n = arb_mat_nrows(A), i, j, qr_prec;
    arb_mat_t B;
    acb_mat_t Ac;
    acb_ptr mu;
    arb_t rho;
    arf_t sigma, sig2, floorF, anchor, g, ub;
    mag_t scale;
    int ok = 0;

    if (n == 0) { arb_indeterminate(lam); return 0; }

    arb_mat_init(B, n, n); arb_init(rho);
    arf_init(sigma); arf_init(sig2); arf_init(floorF); arf_init(anchor); arf_init(g); arf_init(ub);
    mag_init(scale);
    arb_mat_bound_inf_norm(scale, A);
    mag_add_ui(scale, scale, 1);
    frobenius_floor(floorF, A, prec);

    /* Pass 1: a shift just below the spectrum, so that the inverse iteration of zst_eigmin converges
     * in a couple of steps. The approximate minimum of the midpoint matrix comes from an approximate
     * QR (the device secular.c uses for its root candidates); it needs no accuracy guarantee,
     * because every candidate shift is verified by verify_pd and lowered until it is certified, with
     * the Frobenius floor -- valid unconditionally -- as the fallback. */
    qr_prec = FLINT_MIN(prec, 256);
    acb_mat_init(Ac, n, n);
    mu = _acb_vec_init(n);
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            arb_get_mid_arb(acb_realref(acb_mat_entry(Ac, i, j)), arb_mat_entry(A, i, j));
    acb_mat_approx_eig_qr(mu, NULL, NULL, Ac, NULL, 0, qr_prec);
    arf_set(anchor, arb_midref(acb_realref(mu + 0)));
    for (i = 1; i < n; i++)
        if (arf_cmp(arb_midref(acb_realref(mu + i)), anchor) < 0)
            arf_set(anchor, arb_midref(acb_realref(mu + i)));
    acb_mat_clear(Ac); _acb_vec_clear(mu, n);

    arf_set_mag(g, scale);
    arf_mul_2exp_si(g, g, -(prec / 2));
    if (!certified_floor(sigma, A, B, anchor, g, 32, 10, prec) || arf_cmp(sigma, floorF) < 0)
        arf_set(sigma, floorF);

    /* Pass 2: eigenvector of A - sigma (positive definite, minimum nearly zero, so the inverse
     * iteration targets it directly), then the Rayleigh quotient of A along it. The Rayleigh bound
     * is valid for ANY nonzero vector, so when the shifted inverse iteration does not certify (it
     * can fail when the shift dwarfs the eigenvalue, e.g. the zeta even block at x = 30, N = 120,
     * whose minimum 2.2e-135 is far below the shift the certificate can reach at 700 bits) the
     * unshifted block and the Frobenius-shifted block are tried in turn for a vector. */
    {
        slong att;
        for (att = 0; att < 3 && !ok; att++)
        {
            arb_mat_set(B, A);
            if (att != 1)
            {
                const arf_struct *sh = (att == 0) ? sigma : floorF;
                for (i = 0; i < n; i++)
                    arb_sub_arf(arb_mat_entry(B, i, i), arb_mat_entry(B, i, i), sh, prec);
            }
            ok = zst_eigmin(rho, v, B, iters, prec);
        }
    }
    if (!ok) goto done;
    rayleigh(rho, A, v, prec);
    arb_get_ubound_arf(ub, rho, prec);

    /* Pass 3: tighten the certified lower bound, now anchored at the accurate Rayleigh quotient. */
    arb_get_lbound_arf(anchor, rho, prec);
    arf_set_mag(g, scale);
    arf_mul_2exp_si(g, g, -(prec / 2));      /* below this, verify_pd's own delta cannot separate */
    if (certified_floor(sig2, A, B, anchor, g, 64, 12, prec) && arf_cmp(sig2, sigma) > 0)
        arf_set(sigma, sig2);

    if (arf_cmp(sigma, ub) > 0) { ok = 0; goto done; }       /* inconsistent: refuse to certify */
    arb_set_interval_arf(lam, sigma, ub, prec);

done:
    if (!ok) arb_indeterminate(lam);
    arb_mat_clear(B); arb_clear(rho);
    arf_clear(sigma); arf_clear(sig2); arf_clear(floorF); arf_clear(anchor); arf_clear(g); arf_clear(ub);
    mag_clear(scale);
    return ok;
}

int zst_parity(arb_t minE, arb_t minO, arb_t gap, const arb_mat_t E, const arb_mat_t O,
               slong iters, slong prec)
{
    slong nE = arb_mat_nrows(E), nO = arb_mat_nrows(O);
    arb_ptr vE, vO;
    int res = 0;

    arb_indeterminate(minE); arb_indeterminate(minO); arb_indeterminate(gap);
    if (nE == 0 || nO == 0) return 0;

    vE = _arb_vec_init(nE); vO = _arb_vec_init(nO);
    if (zst_block_min(minE, vE, E, iters, prec) && zst_block_min(minO, vO, O, iters, prec))
    {
        /* both balls enclose the true block minima, so arb_lt is a proof of the strict inequality */
        if (arb_lt(minE, minO)) res = 1;
        else if (arb_lt(minO, minE)) res = -1;
        if (res != 0)
        {
            arf_t u, l;
            arf_init(u); arf_init(l);
            arb_get_ubound_arf(u, res == 1 ? minE : minO, prec);
            arb_get_lbound_arf(l, res == 1 ? minO : minE, prec);
            arf_sub(arb_midref(gap), l, u, prec, ARF_RND_DOWN);
            mag_zero(arb_radref(gap));
            if (!arb_is_positive(gap)) arb_zero(gap);
            arf_clear(u); arf_clear(l);
        }
    }
    _arb_vec_clear(vE, nE); _arb_vec_clear(vO, nO);
    return res;
}
