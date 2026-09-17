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

/* K = y~ - Z + (I - R J(Y)) D  with D = Y - y~ */
static void
krawczyk(arb_mat_t K, arb_mat_t C, arb_mat_t JY, const arb_mat_t E, const arb_mat_t Y, const arb_mat_t D,
         const arb_mat_t R, const arb_mat_t Z, const arb_mat_t Ytil, slong m, slong prec)
{
    slong n = arb_mat_nrows(E), i;
    bordered_jacobian(JY, E, Y, m, prec);
    arb_mat_mul(C, R, JY, prec);
    for (i = 0; i <= n; i++) arb_sub_ui(arb_mat_entry(C, i, i), arb_mat_entry(C, i, i), 1, prec);
    arb_mat_neg(C, C);
    arb_mat_mul(K, C, D, prec);
    arb_mat_sub(K, K, Z, prec);
    arb_mat_add(K, K, Ytil, prec);
}

int zst_eigmin(arb_t eps, arb_ptr v, const arb_mat_t E, slong iters, slong prec)
{
    slong n = arb_mat_nrows(E), i, j, m, inflate, it;
    arb_mat_t Emid, X, Ytil, Y, Jm, R, F, Z, JY, C, D, K;
    arb_t t, lam;
    int ok = 0;

    arb_mat_init(Emid, n, n); arb_mat_init(X, n, 1);
    arb_mat_init(Ytil, n + 1, 1); arb_mat_init(Y, n + 1, 1); arb_mat_init(K, n + 1, 1);
    arb_mat_init(Jm, n + 1, n + 1); arb_mat_init(R, n + 1, n + 1); arb_mat_init(JY, n + 1, n + 1);
    arb_mat_init(C, n + 1, n + 1); arb_mat_init(F, n + 1, 1); arb_mat_init(Z, n + 1, 1); arb_mat_init(D, n + 1, 1);
    arb_init(t); arb_init(lam);

    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            arb_get_mid_arb(arb_mat_entry(Emid, i, j), arb_mat_entry(E, i, j));

    m = inverse_iteration(X, lam, Emid, iters, prec);

    /* y~ = (X, lam), exact midpoints */
    for (i = 0; i < n; i++) arb_set(arb_mat_entry(Ytil, i, 0), arb_mat_entry(X, i, 0));
    arb_set(arb_mat_entry(Ytil, n, 0), lam);

    /* R ~ J(y~)^{-1} */
    bordered_jacobian(Jm, Emid, Ytil, m, prec);
    if (!arb_mat_approx_inv(R, Jm, prec)) goto done;

    /* F(y~) in ball arithmetic from the ball matrix E; Z = R F(y~) */
    {
        arb_mat_t EX; arb_mat_init(EX, n, 1);
        arb_mat_mul(EX, E, X, prec);
        for (i = 0; i < n; i++)
        {
            arb_mul(t, lam, arb_mat_entry(X, i, 0), prec);
            arb_sub(arb_mat_entry(F, i, 0), arb_mat_entry(EX, i, 0), t, prec);
        }
        arb_zero(arb_mat_entry(F, n, 0));           /* X[m] - 1 = 0 exactly */
        arb_mat_clear(EX);
    }
    arb_mat_mul(Z, R, F, prec);
    if (getenv("ZST_DEBUG"))
    {
        mag_t mR, mF, mZ; mag_init(mR); mag_init(mF); mag_init(mZ);
        arb_mat_bound_inf_norm(mR, R); arb_mat_bound_inf_norm(mF, F); arb_mat_bound_inf_norm(mZ, Z);
        flint_printf("eigmin: m=%wd |R|<=", m); mag_printd(mR, 3); flint_printf(" |F|<="); mag_printd(mF, 3);
        flint_printf(" |Z|<="); mag_printd(mZ, 3); flint_printf(" F[0]="); arb_printn(arb_mat_entry(F,0,0), 5, 0);
        flint_printf(" E[0,0] rad="); mag_printd(arb_radref(arb_mat_entry(E,0,0)), 3); flint_printf("\n");
        mag_clear(mR); mag_clear(mF); mag_clear(mZ);
    }

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
        krawczyk(K, C, JY, E, Y, D, R, Z, Ytil, m, prec);
        ok = 1;
        for (i = 0; i <= n; i++)
            if (!arb_contains(arb_mat_entry(Y, i, 0), arb_mat_entry(K, i, 0)) ||
                mag_cmp(arb_radref(arb_mat_entry(K, i, 0)), arb_radref(arb_mat_entry(Y, i, 0))) >= 0)
            { ok = 0; break; }
        if (!ok)
            for (i = 0; i <= n; i++)
                mag_mul_2exp_si(arb_radref(arb_mat_entry(D, i, 0)), arb_radref(arb_mat_entry(D, i, 0)), 2);
    }
    if (getenv("ZST_DEBUG"))
    {
        mag_t mC; mag_init(mC); arb_mat_bound_inf_norm(mC, C);
        flint_printf("eigmin: ok=%d after %wd inflations, |C|<=", ok, inflate); mag_printd(mC, 3);
        flint_printf(" rad K[0]="); mag_printd(arb_radref(arb_mat_entry(K,0,0)), 3);
        flint_printf(" rad D[0]="); mag_printd(arb_radref(arb_mat_entry(D,0,0)), 3); flint_printf("\n");
        mag_clear(mC);
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
        krawczyk(K, C, JY, E, Y, D, R, Z, Ytil, m, prec);
        for (i = 0; i <= n; i++)
            if (mag_cmp(arb_radref(arb_mat_entry(K, i, 0)), arb_radref(arb_mat_entry(Y, i, 0))) < 0) improved = 1;
        if (!improved) break;
    }
    for (i = 0; i <= n; i++) arb_intersection(arb_mat_entry(Y, i, 0), arb_mat_entry(Y, i, 0), arb_mat_entry(K, i, 0), prec);
    for (i = 0; i < n; i++) arb_set(v + i, arb_mat_entry(Y, i, 0));
    arb_set(eps, arb_mat_entry(Y, n, 0));

done:
    arb_mat_clear(Emid); arb_mat_clear(X); arb_mat_clear(Ytil); arb_mat_clear(Y); arb_mat_clear(K);
    arb_mat_clear(Jm); arb_mat_clear(R); arb_mat_clear(JY); arb_mat_clear(C); arb_mat_clear(F);
    arb_mat_clear(Z); arb_mat_clear(D);
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
