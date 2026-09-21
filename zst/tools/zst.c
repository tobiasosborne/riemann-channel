#define _POSIX_C_SOURCE 200809L
/* zst: command-line driver of the pipeline.
 *
 *   zst [--x 9] [--N 40] [--prec 400] [--zeros 20] [--iters 40]          Riemann zeta (default)
 *   zst --curve 11a1  [--x 13] [--N 60] ...                              L(E, s), E/Q by label
 *   zst --chi -4      [--x 13] [--N 40] ...                              L(s, chi_D), D fundamental
 *   zst {--curve|--chi} ... --scan-parity 8,13,20                        parity of the minimum per window
 *   [--ref <path>]                                                       reference-data file
 *
 * x = lambda^2 (prime powers <= x enter), N = Fourier truncation, prec in bits.
 *
 * Ground truth, zeta path: refs/src/2511.22755/mc2arXiv.tex, Theorem `finmain` (lines 1085-1118):
 * spectrum of D_log^{(lambda,N)} = zeros of xi_hat = 2 pi s/L over the secular roots s; the delta_N
 * normalisation (Cor. `dirichlet1`, lines 941-990) differs from <eta|xi> = 1 by L^{1/2} and only
 * rescales xi_hat.
 *
 * Ground truth, L-function paths: notes/zeta-spectral-triples/ellcurve/astra-review.md, formula
 * sheet F1-F18 (data model, implemented by src/weil_data.c, src/kernel.c, src/ellcurve.c,
 * src/dirichlet.c) and "Changes I recommend to the plan", item 5: the construction proceeds (sum
 * normalisation, xi_0 > 0, secular roots) ONLY when the minimum of the whole Weil form is even and
 * the even-simple hypothesis certifies; otherwise a certified ODD minimum is itself the result
 * ("the paper's construction is inapplicable at this window"), and only the L2-normalised
 * coefficients of the odd minimiser are reported. Lemma `key` (mc2arXiv.tex l.863-936) and
 * Definition `even-simple` (l.850) are the hypotheses at stake. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <flint/acb_dirichlet.h>
#include <flint/fmpz_vec.h>
#include "zst.h"

static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + 1e-9 * t.tv_nsec; }

/* ------------------------------------------------------------------ Dirichlet reference zeros */

/* tests/data/dirichlet_ref.txt: 'chi <D> <conductor> <kappa>', 'zero <k> <gamma>' ..., 'end'.
 * PARI lfunzeros values, not certified enclosures; returned as balls of radius 1e-38 like the
 * elliptic ones (see src/ell_ref.c). Returns 1 if the discriminant is present. */
static int
chi_ref(arb_ptr gamma, slong K, slong D, const char *path, slong prec)
{
    static const char *fallback[2] = { "tests/data/dirichlet_ref.txt", "../tests/data/dirichlet_ref.txt" };
    FILE *f = NULL;
    char line[512], val[256];
    long d, cond, kappa, k;
    int found = 0, i;
    arb_t rad;

    if (path != NULL) f = fopen(path, "r");
    for (i = 0; f == NULL && i < 2; i++) f = fopen(fallback[i], "r");
    if (f == NULL) return 0;

    arb_init(rad); arb_set_str(rad, "1e-38", prec);
    for (k = 0; k < K; k++) arb_indeterminate(gamma + k);
    while (fgets(line, sizeof(line), f) != NULL)
    {
        if (!found)
        {
            if (line[0] != 'c') continue;
            if (sscanf(line, "chi %ld %ld %ld", &d, &cond, &kappa) != 3) continue;
            if (d != (long) D) continue;
            found = 1;
            continue;
        }
        if (line[0] == 'e' && !strncmp(line, "end", 3)) break;
        if (line[0] != 'z') continue;
        if (sscanf(line, "zero %ld %255s", &k, val) != 2) continue;
        if (k >= 1 && k <= K)
        {
            if (arb_set_str(gamma + k - 1, val, prec) != 0) arb_indeterminate(gamma + k - 1);
            else arb_add_error(gamma + k - 1, rad);
        }
    }
    fclose(f);
    arb_clear(rad);
    return found;
}

/* ------------------------------------------------------------------ the zeta driver (unchanged) */

static int
run_zeta(double xd, slong N, slong prec, slong K, slong iters)
{
    arb_t x, L, eps, shift, twopiL, t, u, sum;
    arb_ptr a, b, v, xi, roots, gamma;
    arb_mat_t E, O;
    ulong X = (ulong) (xd + 1e-9);
    slong nroots, unres, k, dim = N + 1;
    double t0 = now(), t1, t2, t3, t4;
    int ok;

    arb_init(x); arb_init(L); arb_init(eps); arb_init(shift); arb_init(twopiL);
    arb_init(t); arb_init(u); arb_init(sum);
    arb_set_d(x, xd);
    zst_window_L(L, x, prec);
    a = _arb_vec_init(N + 1); b = _arb_vec_init(N + 1);
    v = _arb_vec_init(dim); xi = _arb_vec_init(N + 1);
    roots = _arb_vec_init(N); gamma = _arb_vec_init(K);
    arb_mat_init(E, dim, dim); arb_mat_init(O, N, N);

    flint_printf("zst: x = %g (prime powers <= %wu), N = %wd, prec = %wd bits, L = ", xd, X, N, prec);
    arb_printn(L, 15, 0); flint_printf("\n");

    zst_riemann_ab(a, b, N, x, X, prec);
    zst_even_block(E, a, b, N, prec);
    zst_odd_block(O, a, b, N, prec);
    t1 = now();
    flint_printf("matrix build: %.2fs\n", t1 - t0);

    ok = zst_eigmin(eps, v, E, iters, prec);
    t2 = now();
    flint_printf("minimal even eigenvalue eps_N = "); arb_printn(eps, 10, 0);
    flint_printf("  (%s, %.2fs)\n", ok ? "Rump-certified" : "NOT certified", t2 - t1);
    if (!ok) { flint_printf("eigenpair not certified; raise --prec or --iters\n"); return 1; }

    /* even-simple check: shift = 2 * upper bound of eps (eps > 0 expected) */
    arb_get_ubound_arf(arb_midref(shift), eps, prec); mag_zero(arb_radref(shift));
    arb_mul_2exp_si(shift, shift, 1);
    {
        int es = zst_certify_even_simple(E, O, eps, v, prec);
        t3 = now();
        flint_printf("even-simple hypothesis (deflated Cholesky of E - 2 eps and O - 2 eps): %s  (%.2fs)\n",
                     es ? "CERTIFIED" : "not certified", t3 - t2);
    }

    /* xi_j from the even coordinates, normalised sum_{j=-N}^N xi_j = 1 */
    arb_set(xi + 0, v + 0);
    arb_sqrt_ui(t, 2, prec);
    for (k = 1; k <= N; k++) arb_div(xi + k, v + k, t, prec);
    arb_set(sum, xi + 0);
    for (k = 1; k <= N; k++) { arb_mul_2exp_si(u, xi + k, 1); arb_add(sum, sum, u, prec); }
    for (k = 0; k <= N; k++) arb_div(xi + k, xi + k, sum, prec);
    flint_printf("xi_0 = "); arb_printn(xi + 0, 10, 0);
    flint_printf(", xi_1 = "); arb_printn(xi + 1, 10, 0);
    flint_printf(", xi_N = "); arb_printn(xi + N, 5, 0); flint_printf("\n");

    nroots = zst_secular_roots(roots, N, &unres, xi, N, prec);
    t4 = now();
    flint_printf("positive secular roots: %wd certified of N = %wd, %wd unresolved  ->  spectrum %s  (%.2fs)\n",
                 nroots, N, unres, (nroots == N) ? "COMPLETE" : "incomplete", t4 - t3);

    /* reference zeros in three precision tiers: full precision for the first 20, then 1200 bits up to
     * the 400th (bounds down to ~1e-350 stay measurable), then 400 bits (bounds down to ~1e-118) */
    {
        slong tiers[3][2] = {{20, prec}, {400, FLINT_MIN(prec, 1200)}, {K, FLINT_MIN(prec, 400)}}, ti, k0 = 0;
        for (ti = 0; ti < 3 && k0 < K; ti++)
        {
            slong k1 = FLINT_MIN(K, tiers[ti][0]);
            if (k1 > k0)
            {
                acb_ptr rho = _acb_vec_init(k1 - k0); fmpz_t n1; fmpz_init(n1); fmpz_set_si(n1, k0 + 1);
                acb_dirichlet_zeta_zeros(rho, n1, k1 - k0, tiers[ti][1]);
                for (k = k0; k < k1; k++) arb_set(gamma + k, acb_imagref(rho + k - k0));
                _acb_vec_clear(rho, k1 - k0); fmpz_clear(n1);
            }
            k0 = k1;
        }
    }
    arb_const_pi(twopiL, prec); arb_mul_2exp_si(twopiL, twopiL, 1); arb_div(twopiL, twopiL, L, prec);
    flint_printf("\n  k   z_k = 2 pi s_k / L                                   |z_k - gamma_k| <=\n");
    for (k = 0; k < K && k < nroots; k++)
    {
        mag_t m; mag_init(m);
        arb_mul(t, roots + k, twopiL, prec);
        arb_sub(u, t, gamma + k, prec);
        arb_get_mag(m, u);
        flint_printf("%3wd   ", k + 1); arb_printn(t, 40, ARB_STR_NO_RADIUS);
        flint_printf("   "); mag_printd(m, 3); flint_printf("\n");
        mag_clear(m);
    }
    flint_printf("\ntotal %.2fs\n", now() - t0);

    _arb_vec_clear(a, N + 1); _arb_vec_clear(b, N + 1); _arb_vec_clear(v, dim); _arb_vec_clear(xi, N + 1);
    _arb_vec_clear(roots, N); _arb_vec_clear(gamma, K);
    arb_mat_clear(E); arb_mat_clear(O);
    arb_clear(x); arb_clear(L); arb_clear(eps); arb_clear(shift); arb_clear(twopiL);
    arb_clear(t); arb_clear(u); arb_clear(sum);
    return 0;
}

/* ------------------------------------------------------------------ L-function windows */

typedef struct {
    int          is_curve;       /* 1 = elliptic curve, 0 = real Dirichlet character */
    const char  *label;
    fmpz        *ainvs;          /* curve only */
    fmpz_t       C;              /* conductor */
    slong        D;              /* character only */
    int          w;              /* root number (curve) */
    slong        rank;           /* analytic rank (curve) = number of central zeros */
    arb_ptr      gamma;          /* reference ordinates, gamma[0..K-1] */
    slong        K;
    slong        ncentral;       /* leading reference ordinates equal to 0 */
} lfun_t;

/* blocks of the truncated Weil form of the object at the window x, truncation N */
static void
build_blocks(arb_mat_t E, arb_mat_t O, arb_t L, const lfun_t *F, double xd, slong N, slong prec)
{
    zst_weil_t W;
    arb_t x;
    arb_ptr a = _arb_vec_init(N + 1), b = _arb_vec_init(N + 1);
    ulong X = (ulong) (xd + 1e-9);                     /* X = floor(x): all prime powers 1 < p^m <= X */

    arb_init(x); arb_set_d(x, xd);
    if (F->is_curve) zst_weil_ellcurve(&W, F->ainvs, F->C, x, X, prec);
    else { fmpz_t D; fmpz_init(D); fmpz_set_si(D, F->D); zst_weil_dirichlet(&W, D, x, X, prec); fmpz_clear(D); }
    arb_set(L, W.L);
    zst_weil_ab(a, b, N, &W, prec);
    zst_even_block(E, a, b, N, prec);
    zst_odd_block(O, a, b, N, prec);
    zst_weil_clear(&W);
    _arb_vec_clear(a, N + 1); _arb_vec_clear(b, N + 1);
    arb_clear(x);
}

/* sum-normalised xi from the even eigenvector v (v_0, (v_j + v_{-j})/sqrt2): xi_0 = v_0,
 * xi_j = v_j/sqrt2, then divided by sum_{j=-N}^{N} xi_j.  mc2arXiv.tex l.852-862. */
static void
sum_normalise(arb_ptr xi, arb_srcptr v, slong N, slong prec)
{
    arb_t t, u, sum;
    slong k;
    arb_init(t); arb_init(u); arb_init(sum);
    arb_set(xi + 0, v + 0);
    arb_sqrt_ui(t, 2, prec);
    for (k = 1; k <= N; k++) arb_div(xi + k, v + k, t, prec);
    arb_set(sum, xi + 0);
    for (k = 1; k <= N; k++) { arb_mul_2exp_si(u, xi + k, 1); arb_add(sum, sum, u, prec); }
    for (k = 0; k <= N; k++) arb_div(xi + k, xi + k, sum, prec);
    arb_clear(t); arb_clear(u); arb_clear(sum);
}

/* the recovered ordinates z_k = 2 pi s_k / L against the reference list, skipping the ncentral
 * central zeros (which the finite construction cannot produce: under even-simple D'' is invertible
 * and xi_0 = prod s_k^2/(N!)^2 > 0, astra-review.md "Q1"). Prints at most `show` rows. */
static void
compare_zeros(arb_srcptr roots, slong nroots, const arb_t L, const lfun_t *F, slong show, slong prec)
{
    arb_t twopiL, z, d;
    slong k;
    arb_init(twopiL); arb_init(z); arb_init(d);
    arb_const_pi(twopiL, prec); arb_mul_2exp_si(twopiL, twopiL, 1); arb_div(twopiL, twopiL, L, prec);
    if (F->ncentral > 0)
        flint_printf("reference zeros: %wd central zero(s) gamma = 0 skipped (analytic rank %wd);"
                     " z_k is compared with gamma_{k+%wd}\n", F->ncentral, F->rank, F->ncentral);
    flint_printf("\n  k   z_k = 2 pi s_k / L                        gamma_k (PARI)                          |z_k - gamma_k|\n");
    for (k = 0; k < show && k < nroots && k + F->ncentral < F->K; k++)
    {
        mag_t m; mag_init(m);
        arb_mul(z, roots + k, twopiL, prec);
        arb_sub(d, z, F->gamma + k + F->ncentral, prec);
        arb_get_mag(m, d);
        flint_printf("%3wd   ", k + 1); arb_printn(z, 30, ARB_STR_NO_RADIUS);
        flint_printf("   "); arb_printn(F->gamma + k + F->ncentral, 30, ARB_STR_NO_RADIUS);
        flint_printf("   "); mag_printd(m, 4); flint_printf("\n");
        mag_clear(m);
    }
    arb_clear(twopiL); arb_clear(z); arb_clear(d);
}

/* one window: parity decision, then either the CCM construction or the "odd minimum" report.
 * Returns the parity (+1 / -1 / 0). `show` = how many recovered ordinates to tabulate. */
static int
run_window(const lfun_t *F, double xd, slong N, slong prec, slong iters, slong show, int verbose)
{
    arb_mat_t E, O;
    arb_t L, minE, minO, gap, lam, t;
    arb_ptr v, xi, roots;
    slong dim = N + 1, nroots = 0, unres = 0, k;
    int par, es = 0;
    double t0 = now(), t1, t2;

    arb_mat_init(E, dim, dim); arb_mat_init(O, N, N);
    arb_init(L); arb_init(minE); arb_init(minO); arb_init(gap); arb_init(lam); arb_init(t);
    v = _arb_vec_init(dim); xi = _arb_vec_init(N + 1); roots = _arb_vec_init(N);

    build_blocks(E, O, L, F, xd, N, prec);
    t1 = now();
    if (verbose)
    {
        flint_printf("x = %g (prime powers <= %wu), N = %wd, prec = %wd bits, L = ", xd,
                     (ulong) (xd + 1e-9), N, prec);
        arb_printn(L, 15, 0);
        flint_printf("   (matrix build %.2fs)\n", t1 - t0);
    }

    par = zst_parity(minE, minO, gap, E, O, iters, prec);
    t2 = now();

    if (verbose)
    {
        flint_printf("certified block minima (Rayleigh above, ball LDL^T inertia below):\n");
        flint_printf("   min E = "); arb_printn(minE, 12, 0); flint_printf("\n");
        flint_printf("   min O = "); arb_printn(minO, 12, 0); flint_printf("\n");
        flint_printf("parity: %s   certified gap >= ", par > 0 ? "+1 (EVEN minimum)" :
                     par < 0 ? "-1 (ODD minimum)" : "0 (UNDECIDED)");
        if (par != 0) arb_printn(gap, 8, ARB_STR_NO_RADIUS); else flint_printf("-");
        flint_printf("   (%.2fs)\n", t2 - t1);
    }

    if (par == 0)
    {
        flint_printf("parity undecided: the two certified minima overlap. Raise --prec (or --iters).\n");
        goto done;
    }
    if (par < 0)
    {
        /* astra-review.md, recommendation 5: a certified odd minimum is the research result. */
        flint_printf("odd minimum: the paper's construction is inapplicable at this window\n");
        flint_printf("   (the even-simple hypothesis of mc2arXiv.tex l.850 fails: the global minimum of the\n"
                     "    Weil form lies in the odd block, so Lemma `key' l.863 gives no rank-one deflation,\n"
                     "    the sum normalisation of xi is undefined, and no CCM spectrum is defined here.)\n");
        flint_printf("   min E = "); arb_printn(minE, 12, 0); flint_printf("\n");
        flint_printf("   min O = "); arb_printn(minO, 12, 0); flint_printf("\n");
        flint_printf("   gap  >= "); arb_printn(gap, 8, ARB_STR_NO_RADIUS); flint_printf("\n");
        {
            arb_ptr vo = _arb_vec_init(N);
            if (zst_block_min(lam, vo, O, iters, prec))
            {
                arb_zero(t);
                for (k = 0; k < N; k++) arb_addmul(t, vo + k, vo + k, prec);
                arb_sqrt(t, t, prec);
                flint_printf("   L2-normalised odd minimiser, first coefficients (basis (V_j - V_{-j})/sqrt2;\n"
                             "   the eigenvalue above is certified, the eigenvector is the inverse-iteration\n"
                             "   minimiser and is printed without radii):\n     ");
                for (k = 0; k < N && k < 6; k++)
                {
                    arb_div(lam, vo + k, t, prec);
                    flint_printf("c_%wd = ", k + 1); arb_printn(lam, 12, ARB_STR_NO_RADIUS);
                    flint_printf(k + 1 < N && k < 5 ? ",  " : "\n");
                }
            }
            _arb_vec_clear(vo, N);
        }
        goto done;
    }

    /* parity +1: the even minimum is a candidate for the paper's even-simple hypothesis */
    if (!zst_block_min(lam, v, E, iters, prec))
    {
        flint_printf("even minimiser not certified; raise --prec or --iters\n");
        goto done;
    }
    es = zst_certify_even_simple(E, O, lam, v, prec);
    flint_printf("even-simple hypothesis (deflated Cholesky of E - 2 eps and O - 2 eps): %s\n",
                 es ? "CERTIFIED" : "NOT certified");
    if (!es)
    {
        if (!arb_is_positive(lam))
            flint_printf("   (the minimum is not positive, so the 2 eps threshold of zst_certify_even_simple\n"
                         "    does not separate it; the construction is not attempted.)\n");
        goto done;
    }

    sum_normalise(xi, v, N, prec);
    flint_printf("xi_0 = "); arb_printn(xi + 0, 12, 0);
    flint_printf("   (consistency check, astra-review.md Q1: under even-simple D'' is invertible and\n"
                 "    xi_0 = prod_{k=1}^{N} s_k^2 / (N!)^2 > 0; a non-positive xi_0 refutes the hypothesis)\n");
    if (!arb_is_positive(xi + 0))
        flint_printf("   WARNING: xi_0 is not certified positive.\n");
    flint_printf("xi_1 = "); arb_printn(xi + 1, 10, 0);
    flint_printf(", xi_N = "); arb_printn(xi + N, 5, 0); flint_printf("\n");

    nroots = zst_secular_roots(roots, N, &unres, xi, N, prec);
    flint_printf("positive secular roots: %wd certified of N = %wd, %wd unresolved  ->  spectrum %s\n",
                 nroots, N, unres, (nroots == N) ? "COMPLETE" : "incomplete");
    compare_zeros(roots, nroots, L, F, show, prec);

done:
    flint_printf("window total %.2fs\n", now() - t0);
    arb_mat_clear(E); arb_mat_clear(O);
    arb_clear(L); arb_clear(minE); arb_clear(minO); arb_clear(gap); arb_clear(lam); arb_clear(t);
    _arb_vec_clear(v, dim); _arb_vec_clear(xi, N + 1); _arb_vec_clear(roots, N);
    return par;
}

int main(int argc, char **argv)
{
    double xd = 9.0; slong N = 40, prec = 400, K = 20, iters = 40;
    const char *curve = NULL, *scan = NULL, *ref = NULL;
    slong D = 0; int have_chi = 0, i, rc = 0;

    for (i = 1; i + 1 < argc; i += 2)
    {
        if (!strcmp(argv[i], "--x")) xd = atof(argv[i + 1]);
        else if (!strcmp(argv[i], "--N")) N = atol(argv[i + 1]);
        else if (!strcmp(argv[i], "--prec")) prec = atol(argv[i + 1]);
        else if (!strcmp(argv[i], "--zeros")) K = atol(argv[i + 1]);
        else if (!strcmp(argv[i], "--iters")) iters = atol(argv[i + 1]);
        else if (!strcmp(argv[i], "--curve")) curve = argv[i + 1];
        else if (!strcmp(argv[i], "--chi")) { D = atol(argv[i + 1]); have_chi = 1; }
        else if (!strcmp(argv[i], "--scan-parity")) scan = argv[i + 1];
        else if (!strcmp(argv[i], "--ref")) ref = argv[i + 1];
        else { fprintf(stderr, "unknown option %s\n", argv[i]); return 2; }
    }
    if (curve == NULL && !have_chi)
    {
        rc = run_zeta(xd, N, prec, K, iters);
        flint_cleanup();
        return rc;
    }
    if (curve != NULL && have_chi) { fprintf(stderr, "--curve and --chi are exclusive\n"); return 2; }

    {
        lfun_t F;
        slong k;
        slong Kref = FLINT_MAX(K, 8);
        double t0 = now();

        memset(&F, 0, sizeof(F));
        F.K = Kref;
        F.gamma = _arb_vec_init(Kref);
        fmpz_init(F.C);
        F.ainvs = _fmpz_vec_init(5);

        if (curve != NULL)
        {
            F.is_curve = 1; F.label = curve;
            if (!zst_ell_ref(F.ainvs, F.C, &F.w, &F.rank, F.gamma, Kref, curve, ref, prec))
            {
                fprintf(stderr, "curve %s not in the reference file (tests/data/ell_ref.txt)\n", curve);
                return 2;
            }
            flint_printf("zst: curve %s  [", curve);
            for (k = 0; k < 5; k++) { fmpz_print(F.ainvs + k); if (k < 4) flint_printf(","); }
            flint_printf("]  conductor "); fmpz_print(F.C);
            flint_printf("  root number %+d  analytic rank %wd\n", F.w, F.rank);
            flint_printf("     gamma factor Gamma_C(s + 1/2) = (Q, d, mu) = (1/2pi, 1, 1), no pole (F17)\n");
        }
        else
        {
            F.is_curve = 0; F.label = "chi";
            F.D = D;
            fmpz_set_si(F.C, D < 0 ? -D : D);
            if (!chi_ref(F.gamma, Kref, D, ref, prec))
            {
                fprintf(stderr, "chi_%ld not in the reference file (tests/data/dirichlet_ref.txt)\n", (long) D);
                return 2;
            }
            flint_printf("zst: real primitive character chi_D, D = %wd (Kronecker symbol), conductor ", D);
            fmpz_print(F.C);
            flint_printf("\n     gamma factor Gamma_R(s + %d) = (Q, d, mu) = (pi^-1/2, 2, %s), no pole (F6, F17)\n",
                         D < 0 ? 1 : 0, D < 0 ? "3/2" : "1/2");
        }
        /* the leading reference ordinates equal to zero are the central zero with its multiplicity */
        F.ncentral = 0;
        while (F.ncentral < Kref && arb_contains_zero(F.gamma + F.ncentral)) F.ncentral++;

        if (scan != NULL)
        {
            char buf[256], *p, *q;
            strncpy(buf, scan, sizeof(buf) - 1); buf[sizeof(buf) - 1] = 0;
            flint_printf("\nparity scan (certified minima of the even and odd blocks per window):\n");
            for (p = buf; p != NULL && *p; p = q)
            {
                q = strchr(p, ','); if (q != NULL) *q++ = 0;
                flint_printf("\n--- x = %s ---\n", p);
                run_window(&F, atof(p), N, prec, iters, 5, 1);
            }
        }
        else
        {
            run_window(&F, xd, N, prec, iters, K, 1);
        }
        flint_printf("\ntotal %.2fs\n", now() - t0);

        _arb_vec_clear(F.gamma, Kref);
        _fmpz_vec_clear(F.ainvs, 5);
        fmpz_clear(F.C);
    }
    flint_cleanup();
    return rc;
}
