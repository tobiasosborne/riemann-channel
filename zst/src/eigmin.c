/* Minimal eigenpair of a real symmetric ball matrix, and inertia counts.  plan.md Section 3.4.
 * Ground truth for what is certified: refs/src/2511.22755/mc2arXiv.tex, Definition `even-simple`
 * l.850 (smallest eigenvalue simple, eigenvector even) and Lemma `key` l.863-870 (T >= 0 with a
 * one-dimensional kernel). zst_eigmin certifies the minimal eigenpair of the even block; the two
 * inertia counts (even block below 2 eps: one; odd block below 2 eps: none) certify even-simplicity.
 *
 * Verification is Krawczyk's operator on the bordered system
 *     F(x, lambda) = (A x - lambda x,  x_m - 1),   m = index of the largest |x_m|,
 * with Jacobian J = [A - lambda I, -x; e_m^T, 0] and R an approximate inverse of J at the
 * approximate solution y~. If K(Y) = y~ - R F(y~) + (I - R J(Y)) (Y - y~) lies strictly inside the
 * box Y, then Y contains exactly one solution (a simple eigenpair); the contraction is then
 * iterated to the residual-limited width. (This is Rump's method; arb's own routine returns the
 * inflated containment box, which is far wider than the data permits.) */
#include <stdlib.h>
#include "zst.h"

/* inverse iteration on midpoints; X normalised so that X[m] = 1 exactly; returns m */
static slong
inverse_iteration(arb_mat_t X, arb_t eps, const arb_mat_t Emid, slong iters, slong prec)
{
    slong n = arb_mat_nrows(Emid), i, it, m = 0, *perm;
    arb_mat_t LU, Y, T;
    arb_t t, s, mx, delta;
    mag_t tol;
    int have_lu;

    arb_mat_init(LU, n, n); arb_mat_init(Y, n, 1); arb_mat_init(T, n, 1);
    arb_init(t); arb_init(s); arb_init(mx); arb_init(delta); mag_init(tol);
    perm = flint_malloc(sizeof(slong) * n);
    mag_set_ui_2exp_si(tol, 1, -(prec - 8));

    for (i = 0; i < n; i++) arb_set_ui(arb_mat_entry(X, i, 0), 1);
    have_lu = arb_mat_approx_lu(perm, LU, Emid, prec);
    for (it = 0; it < iters && have_lu; it++)
    {
        arb_mat_approx_solve_lu_precomp(Y, perm, LU, X, prec);
        arb_zero(mx);
        for (i = 0; i < n; i++)
        {
            arb_get_mid_arb(t, arb_mat_entry(Y, i, 0)); arb_abs(s, t);
            if (arb_gt(s, mx)) { arb_set(mx, s); m = i; }
        }
        arb_get_mid_arb(mx, arb_mat_entry(Y, m, 0));          /* signed: X[m] becomes exactly 1 */
        arb_zero(delta);
        for (i = 0; i < n; i++)
        {
            arb_get_mid_arb(t, arb_mat_entry(Y, i, 0));
            arb_div(t, t, mx, prec); arb_get_mid_arb(t, t);
            arb_sub(s, t, arb_mat_entry(X, i, 0), prec); arb_abs(s, s); arb_add(delta, delta, s, prec);
            arb_set(arb_mat_entry(Y, i, 0), t);
        }
        arb_one(arb_mat_entry(Y, m, 0));
        arb_mat_set(X, Y);
        if (arf_cmpabs_mag(arb_midref(delta), tol) < 0) break;
    }
    /* Rayleigh quotient on midpoints */
    arb_mat_mul(T, Emid, X, prec);
    arb_zero(s); arb_zero(t);
    for (i = 0; i < n; i++)
    {
        arb_addmul(s, arb_mat_entry(T, i, 0), arb_mat_entry(X, i, 0), prec);
        arb_addmul(t, arb_mat_entry(X, i, 0), arb_mat_entry(X, i, 0), prec);
    }
    arb_div(eps, s, t, prec); arb_get_mid_arb(eps, eps);

    flint_free(perm);
    arb_mat_clear(LU); arb_mat_clear(Y); arb_mat_clear(T);
    arb_clear(t); arb_clear(s); arb_clear(mx); arb_clear(delta); mag_clear(tol);
    return m;
}

/* Jacobian J(Y) of the bordered system at the box Y = (x, lambda) (balls), into an (n+1)x(n+1) matrix */
static void
bordered_jacobian(arb_mat_t J, const arb_mat_t A, const arb_mat_t Y, slong m, slong prec)
{
    slong n = arb_mat_nrows(A), i, j;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++) arb_set(arb_mat_entry(J, i, j), arb_mat_entry(A, i, j));
        arb_sub(arb_mat_entry(J, i, i), arb_mat_entry(J, i, i), arb_mat_entry(Y, n, 0), prec);
        arb_neg(arb_mat_entry(J, i, n), arb_mat_entry(Y, i, 0));
        arb_zero(arb_mat_entry(J, n, i));
    }
    arb_one(arb_mat_entry(J, n, m));
    arb_zero(arb_mat_entry(J, n, n));
}

/* C = A B by arb_dot (no temporaries beyond the result); A is p x q, B is q x r */
static void
mat_mul_dot(arb_mat_t C, const arb_mat_t A, const arb_mat_t B, slong prec)
{
    slong i, j, p = arb_mat_nrows(A), q = arb_mat_ncols(A), r = arb_mat_ncols(B);
    for (i = 0; i < p; i++)
        for (j = 0; j < r; j++)
            arb_dot(arb_mat_entry(C, i, j), NULL, 0, arb_mat_entry(A, i, 0), 1, arb_mat_entry(B, 0, j), r, q, prec);
}

/* Krawczyk image of the box y~ + D, with C0 = I - R J(y~) precomputed (ball). F is quadratic, so
 * the expansion is EXACT: F(y~ + d) = F(y~) + J(y~) d - d_lam d_x, hence for y = y~ + d in Y
 *   y - R F(y) = y~ - Z + C0 d + R_x (d_lam * d_x),
 * enclosed over Y by  K = y~ - Z + C0 D + R_x (D_lam * D_x),  R_x the first n columns of R.
 * (Bug fixed 2026-09-18, found by Lane C of MVP-3: the previous code used the mean-value bound
 * 2 R_x (D_lam * D_x), which is a valid superset only while D is centred at 0; the contraction loop
 * below moves the box off-centre, and the factor 2 then EXCLUDED the true solution, so the
 * returned box could miss the eigenvalue when inverse iteration had not converged.) */
static void
krawczyk(arb_mat_t K, const arb_mat_t C0, const arb_mat_t R, const arb_mat_t D, const arb_mat_t Z,
         const arb_mat_t Ytil, slong prec)
{
    slong n = arb_mat_nrows(R) - 1, i;
    arb_mat_t W;
    arb_t t;
    arb_mat_init(W, n, 1); arb_init(t);
    mat_mul_dot(K, C0, D, prec);
    for (i = 0; i < n; i++) arb_mul(arb_mat_entry(W, i, 0), arb_mat_entry(D, n, 0), arb_mat_entry(D, i, 0), prec);
    for (i = 0; i <= n; i++)
    {
        arb_dot(t, NULL, 0, arb_mat_entry(R, i, 0), 1, arb_mat_entry(W, 0, 0), 1, n, prec);
        arb_add(arb_mat_entry(K, i, 0), arb_mat_entry(K, i, 0), t, prec);
    }
    arb_mat_sub(K, K, Z, prec);
    arb_mat_add(K, K, Ytil, prec);
    arb_mat_clear(W); arb_clear(t);
}

int zst_eigmin(arb_t eps, arb_ptr v, const arb_mat_t E, slong iters, slong prec)
{
    /* memory: at most E (caller), R, C0 and the transient Emid/Jm/LU alive at once */
    slong n = arb_mat_nrows(E), i, j, m, inflate, it;
    arb_mat_t Emid, X, Ytil, Y, Jm, R, C0, F, Z, D, K;
    arb_t t, lam;
    int ok = 0;

    arb_mat_init(Emid, n, n); arb_mat_init(X, n, 1);
    arb_mat_init(Ytil, n + 1, 1); arb_mat_init(Y, n + 1, 1); arb_mat_init(K, n + 1, 1);
    arb_mat_init(R, n + 1, n + 1); arb_mat_init(C0, n + 1, n + 1);
    arb_mat_init(F, n + 1, 1); arb_mat_init(Z, n + 1, 1); arb_mat_init(D, n + 1, 1);
    arb_init(t); arb_init(lam);

    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            arb_get_mid_arb(arb_mat_entry(Emid, i, j), arb_mat_entry(E, i, j));

    m = inverse_iteration(X, lam, Emid, iters, prec);

    /* y~ = (X, lam), exact midpoints */
    for (i = 0; i < n; i++) arb_set(arb_mat_entry(Ytil, i, 0), arb_mat_entry(X, i, 0));
    arb_set(arb_mat_entry(Ytil, n, 0), lam);

    /* R ~ J(y~)^{-1} from the midpoint Jacobian; then C0 = I - R J(y~) with the ball E */
    arb_mat_init(Jm, n + 1, n + 1);
    bordered_jacobian(Jm, Emid, Ytil, m, prec);
    arb_mat_clear(Emid); arb_mat_init(Emid, 0, 0);
    if (!arb_mat_approx_inv(R, Jm, prec)) { arb_mat_clear(Jm); goto done; }
    bordered_jacobian(Jm, E, Ytil, m, prec);
    mat_mul_dot(C0, R, Jm, prec);
    arb_mat_clear(Jm);
    for (i = 0; i <= n; i++) arb_sub_ui(arb_mat_entry(C0, i, i), arb_mat_entry(C0, i, i), 1, prec);
    arb_mat_neg(C0, C0);

    /* F(y~) in ball arithmetic from the ball matrix E; Z = R F(y~) */
    for (i = 0; i < n; i++)
    {
        arb_dot(arb_mat_entry(F, i, 0), NULL, 0, arb_mat_entry(E, i, 0), 1, arb_mat_entry(X, 0, 0), 1, n, prec);
        arb_mul(t, lam, arb_mat_entry(X, i, 0), prec);
        arb_sub(arb_mat_entry(F, i, 0), arb_mat_entry(F, i, 0), t, prec);
    }
    arb_zero(arb_mat_entry(F, n, 0));           /* X[m] - 1 = 0 exactly */
    mat_mul_dot(Z, R, F, prec);

    /* box Y = y~ + D, D centred at 0 with radius 4|Z| + 2^-prec (componentwise), inflated on failure */
    for (i = 0; i <= n; i++)
    {
        mag_t r; mag_init(r);
        arb_get_mag(r, arb_mat_entry(Z, i, 0));
        mag_mul_2exp_si(r, r, 2);
        arb_zero(arb_mat_entry(D, i, 0)); arb_add_error_mag(arb_mat_entry(D, i, 0), r);
        arb_add_error_2exp_si(arb_mat_entry(D, i, 0), -prec);
        mag_clear(r);
    }
    for (inflate = 0; inflate < 60 && !ok; inflate++)
    {
        arb_mat_add(Y, Ytil, D, prec);
        krawczyk(K, C0, R, D, Z, Ytil, prec);
        ok = 1;
        for (i = 0; i <= n; i++)
            if (!arb_contains(arb_mat_entry(Y, i, 0), arb_mat_entry(K, i, 0)) ||
                mag_cmp(arb_radref(arb_mat_entry(K, i, 0)), arb_radref(arb_mat_entry(Y, i, 0))) >= 0)
            { ok = 0; break; }
        if (!ok)
            for (i = 0; i <= n; i++)
                mag_mul_2exp_si(arb_radref(arb_mat_entry(D, i, 0)), arb_radref(arb_mat_entry(D, i, 0)), 2);
    }
    if (!ok) goto done;

    /* contract: Y <- K(Y) intersect Y until stationary */
    for (it = 0; it < 50; it++)
    {
        int improved = 0;
        for (i = 0; i <= n; i++)
        {
            arb_intersection(arb_mat_entry(Y, i, 0), arb_mat_entry(Y, i, 0), arb_mat_entry(K, i, 0), prec);
            arb_sub(arb_mat_entry(D, i, 0), arb_mat_entry(Y, i, 0), arb_mat_entry(Ytil, i, 0), prec);
        }
        krawczyk(K, C0, R, D, Z, Ytil, prec);
        for (i = 0; i <= n; i++)
            if (mag_cmp(arb_radref(arb_mat_entry(K, i, 0)), arb_radref(arb_mat_entry(Y, i, 0))) < 0) improved = 1;
        if (!improved) break;
    }
    for (i = 0; i <= n; i++) arb_intersection(arb_mat_entry(Y, i, 0), arb_mat_entry(Y, i, 0), arb_mat_entry(K, i, 0), prec);
    for (i = 0; i < n; i++) arb_set(v + i, arb_mat_entry(Y, i, 0));
    arb_set(eps, arb_mat_entry(Y, n, 0));

done:
    arb_mat_clear(Emid); arb_mat_clear(X); arb_mat_clear(Ytil); arb_mat_clear(Y); arb_mat_clear(K);
    arb_mat_clear(R); arb_mat_clear(C0); arb_mat_clear(F); arb_mat_clear(Z); arb_mat_clear(D);
    arb_clear(t); arb_clear(lam);
    return ok;
}

slong zst_inertia_neg(const arb_mat_t A, const arb_t shift, slong prec)
{
    /* unpivoted LDL^T of A - shift in ball arithmetic; Sylvester: #negative pivots = #eigenvalues
     * below shift, provided every pivot ball excludes zero. */
    slong n = arb_mat_nrows(A), i, j, k, neg = 0;
    arb_mat_t Lm;
    arb_ptr d;
    arb_t t, u;
    arb_mat_init(Lm, n, n);
    d = _arb_vec_init(n);
    arb_init(t); arb_init(u);
    for (i = 0; i < n; i++)
    {
        arb_sub(d + i, arb_mat_entry(A, i, i), shift, prec);
        for (k = 0; k < i; k++)
        {
            arb_sqr(t, arb_mat_entry(Lm, i, k), prec);
            arb_submul(d + i, t, d + k, prec);
        }
        if (arb_contains_zero(d + i)) { neg = -1; break; }
        if (arb_is_negative(d + i)) neg++;
        for (j = i + 1; j < n; j++)
        {
            arb_set(t, arb_mat_entry(A, j, i));
            for (k = 0; k < i; k++)
            {
                arb_mul(u, arb_mat_entry(Lm, j, k), arb_mat_entry(Lm, i, k), prec);
                arb_submul(t, u, d + k, prec);
            }
            arb_div(arb_mat_entry(Lm, j, i), t, d + i, prec);
        }
    }
    arb_mat_clear(Lm); _arb_vec_clear(d, n); arb_clear(t); arb_clear(u);
    return neg;
}

/* Verified positive definiteness (Rump's isspd): with delta = 2^-(prec/2) max_i F_ii, compute an
 * approximate Cholesky factor Lt of mid(F) - delta I in midpoint arithmetic (which fails only if
 * that matrix is numerically not positive definite), then bound r = ||F - delta I - Lt Lt^T||_inf in
 * ball arithmetic. Since Lt Lt^T is positive semidefinite for any real Lt, F >= (delta - r) I, and
 * delta > r certifies F positive definite. Unlike interval Cholesky this amplifies input radii
 * only through the residual, not through the pivots. Returns 1 if certified. */
static int
verify_pd(const arb_mat_t F, slong prec)
{
    slong n = arb_mat_nrows(F), i, j, k;
    arb_mat_t Lt, Rm;
    arb_t delta, t, u;
    mag_t r, d;
    int ok = 1;
    if (n == 0) return 1;
    arb_mat_init(Lt, n, n); arb_mat_init(Rm, n, n);
    arb_init(delta); arb_init(t); arb_init(u); mag_init(r); mag_init(d);
    /* delta = 2^-(prec/2) * max_i |F_ii| (midpoints) */
    arb_zero(delta);
    for (i = 0; i < n; i++)
    {
        arb_get_mid_arb(t, arb_mat_entry(F, i, i)); arb_abs(t, t);
        if (arb_gt(t, delta)) arb_set(delta, t);
    }
    arb_mul_2exp_si(delta, delta, -(prec / 2));
    arb_get_mid_arb(delta, delta);
    /* approximate Cholesky of mid(F) - delta I (Cholesky-Banachiewicz, midpoints only) */
    for (j = 0; j < n && ok; j++)
    {
        arb_get_mid_arb(t, arb_mat_entry(F, j, j)); arb_sub(t, t, delta, prec);
        for (k = 0; k < j; k++) arb_submul(t, arb_mat_entry(Lt, j, k), arb_mat_entry(Lt, j, k), prec);
        arb_get_mid_arb(t, t);
        if (!arb_is_positive(t)) { ok = 0; break; }
        arb_sqrt(arb_mat_entry(Lt, j, j), t, prec); arb_get_mid_arb(arb_mat_entry(Lt, j, j), arb_mat_entry(Lt, j, j));
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
        /* residual F - delta I - Lt Lt^T in ball arithmetic (rows of Lt dotted, no transpose or product
         * matrix); ||.||_2 <= ||.||_inf for symmetric matrices */
        for (i = 0; i < n; i++)
            for (j = 0; j < n; j++)
            {
                arb_dot(arb_mat_entry(Rm, i, j), arb_mat_entry(F, i, j), 1,
                        arb_mat_entry(Lt, i, 0), 1, arb_mat_entry(Lt, j, 0), 1, FLINT_MIN(i, j) + 1, prec);
                if (i == j) arb_sub(arb_mat_entry(Rm, i, i), arb_mat_entry(Rm, i, i), delta, prec);
            }
        arb_mat_bound_inf_norm(r, Rm);
        arb_get_mag_lower(d, delta);
        ok = mag_cmp(r, d) < 0;
    }
    arb_mat_clear(Lt); arb_mat_clear(Rm);
    arb_clear(delta); arb_clear(t); arb_clear(u); mag_clear(r); mag_clear(d);
    return ok;
}

int zst_certify_even_simple(const arb_mat_t E, const arb_mat_t O, const arb_t eps, arb_srcptr v, slong prec)
{
    /* s = 2 upper(eps), c = s + 1 (> s - eps, so the deflated direction is lifted above zero);
     * F = E - s + c v v^T / (v^T v) positive definite (verify_pd) and O - s positive definite.
     * Interlacing: E - s = F - (rank-one PSD) has at most one negative eigenvalue, and eps - s < 0 is
     * a certified eigenvalue of E - s, so exactly one; no odd eigenvalue lies below s.
     * Ground truth for the hypothesis: refs/src/2511.22755/mc2arXiv.tex, Definition `even-simple` l.850. */
    slong n = arb_mat_nrows(E), m = arb_mat_nrows(O), i, j;
    arb_mat_t F, G;
    arb_t s, nv, t;
    int ok = 0;
    if (!arb_is_positive(eps)) return 0;
    arb_mat_init(F, n, n); arb_mat_init(G, m, m);
    arb_init(s); arb_init(nv); arb_init(t);
    arb_get_ubound_arf(arb_midref(s), eps, prec); mag_zero(arb_radref(s));
    arb_mul_2exp_si(s, s, 1);
    arb_zero(nv);
    for (i = 0; i < n; i++) arb_addmul(nv, v + i, v + i, prec);
    arb_add_ui(t, s, 1, prec); arb_div(nv, nv, t, prec);          /* nv = (v^T v)/c, c = s + 1 */
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
        {
            arb_mul(t, v + i, v + j, prec); arb_div(t, t, nv, prec);
            arb_add(arb_mat_entry(F, i, j), arb_mat_entry(E, i, j), t, prec);
            if (i == j) arb_sub(arb_mat_entry(F, i, i), arb_mat_entry(F, i, i), s, prec);
        }
    ok = verify_pd(F, prec);
    if (ok && m > 0)
    {
        for (i = 0; i < m; i++)
            for (j = 0; j < m; j++)
            {
                arb_set(arb_mat_entry(G, i, j), arb_mat_entry(O, i, j));
                if (i == j) arb_sub(arb_mat_entry(G, i, i), arb_mat_entry(G, i, i), s, prec);
            }
        ok = verify_pd(G, prec);
    }
    arb_mat_clear(F); arb_mat_clear(G);
    arb_clear(s); arb_clear(nv); arb_clear(t);
    return ok;
}
