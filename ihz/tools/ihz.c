#define _POSIX_C_SOURCE 200809L
/* ihz command-line driver: the CCM construction on a regular graph (or on raw counts), with the
 * exact stage (critical window, kernel polynomial against the retained charpoly) and the ball stage
 * (certified minimal eigenpair, roots on the circle, unitary key lemma, Prony weights, comparison
 * with the certified truth). Conventions: include/ihz.h; plan: notes/zeta-spectral-triples/ihara/plan.md.
 *
 *   ihz --graph <name|file> [--M m] [--prec bits] [--scan] [--no-unitary]
 *   ihz --counts N0,N1,...,N2M --q q --triv p:m,p:m,... --sign +-1 [--prec bits] [--scan]
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <flint/arb_calc.h>
#include <flint/fmpz_vec.h>
#include "ihz.h"

static void print_ball(const char *lab, const arb_t x) {
    printf("%s = ", lab); arb_printn(x, 20, 0); printf("   rad "); mag_printd(arb_radref(x), 3); printf("\n");
}

/* one window: returns 0 on success; fills summary fields */
static int run_window(const ihz_weil_t *W, slong Mp, const ihz_spectrum_t *S, slong prec, int do_unitary,
                      int verbose, arb_t eps_out, slong *nroots_out, slong *unres_out, arb_t maxerr_out, int *unit_ok)
{
    slong K = 2 * Mp + 1, i;
    arb_mat_t E, O, T; arb_t eps; arb_ptr v, xi, theta, err; slong nroots, unres;
    arb_mat_init(E, Mp + 1, Mp + 1); arb_mat_init(O, Mp, Mp); arb_mat_init(T, K, K);
    ihz_even_block(E, W, Mp, prec); ihz_odd_block(O, W, Mp, prec); ihz_toeplitz(T, W, Mp, prec);
    arb_init(eps); v = _arb_vec_init(Mp + 1); xi = _arb_vec_init(K);
    int ok = ihz_eigmin(eps, v, E, 200, prec);
    if (!ok) { printf("  Mp=%ld: eigmin FAILED to certify\n", Mp); arb_indeterminate(eps); }
    arb_set(eps_out, eps);
    int cert = ok ? ihz_certify_even_simple(E, O, eps, v, prec) : 0;
    ihz_even_to_full(xi, v, Mp, prec);
    slong rank = ihz_rank_exact(W, Mp);
    theta = _arb_vec_init(2 * Mp + 2);
    nroots = ok ? ihz_circle_roots(theta, 2 * Mp + 2, &unres, xi, Mp, prec) : 0;
    if (!ok) unres = -1;
    *nroots_out = nroots; *unres_out = unres;
    err = _arb_vec_init(S ? S->R : 1); arb_zero(maxerr_out);
    if (S && ok) {
        ihz_compare(err, theta, nroots, S, W->q, prec);
        for (i = 0; i < S->R; i++) if (arb_gt(err + i, maxerr_out) || i == 0) arb_set(maxerr_out, err + i);
    }
    *unit_ok = -1;
    if (do_unitary && ok && Mp >= 1) {
        arb_mat_t U; arb_ptr xin = _arb_vec_init(K); acb_t w;
        arb_mat_init(U, K, K);
        if (!arb_contains_zero(xi + 0)) {
            for (i = 0; i < K; i++) arb_div(xin + i, xi + i, xi + 0, prec);
            ihz_unitary_build(U, xin, K, prec);
            int u1 = ihz_unitary_check(U, T, eps, prec);
            acb_init(w); acb_set_d_d(w, 0.3, 0.4);
            int u2 = ihz_unitary_det_check(U, xin, K, w, prec);
            acb_clear(w);
            *unit_ok = (u1 && u2) ? 1 : 0;
            if (verbose) printf("  unitary key lemma: U^T(T-eps)U = T-eps %s, det identity %s\n", u1 ? "CERTIFIED" : "not certified", u2 ? "CERTIFIED" : "not certified");
        } else if (verbose) printf("  unitary key lemma: xi_0 ball contains 0, skipped\n");
        arb_mat_clear(U); _arb_vec_clear(xin, K);
    }
    if (verbose) {
        printf("  Mp=%ld K=%ld: exact rank %ld (kernel dim %ld)\n", Mp, K, rank, K - rank);
        print_ball("  eps", eps);
        printf("  even-simple certificate: %s\n", cert ? "CERTIFIED" : "not certified (expected at eps = 0)");
        printf("  roots of R(theta) on [0,pi]: %ld certified, %ld unresolved\n", nroots, unres);
        for (i = 0; i < nroots; i++) { printf("    theta_%ld", i); print_ball("", theta + i); }
        if (S && ok) for (i = 0; i < S->R; i++) { printf("    truth point %ld (mult %ld): |mu - root| <= ", i, S->mult[i]); mag_printd(arb_radref(err + i), 3); printf(" + |mid| "); arb_printn(err + i, 5, 0); printf("\n"); }
        if (S && ok && nroots == S->R / 2 + (S->R % 2)) {
            /* Prony weights from the certified root points, matched to truth order by ihz_compare's convention is not needed: use truth points directly */
            acb_ptr alpha = _acb_vec_init(S->R);
            ihz_prony_weights(alpha, W, S->mu, S->R, prec);
            printf("  Prony weights at the truth points:");
            for (i = 0; i < S->R; i++) { printf(" "); acb_printn(alpha + i, 8, 0); }
            printf("\n");
            _acb_vec_clear(alpha, S->R);
        }
    }
    arb_mat_clear(E); arb_mat_clear(O); arb_mat_clear(T); arb_clear(eps);
    _arb_vec_clear(v, Mp + 1); _arb_vec_clear(xi, K); _arb_vec_clear(theta, 2 * Mp + 2); _arb_vec_clear(err, S ? S->R : 1);
    return ok ? 0 : 1;
}

int main(int argc, char **argv)
{
    const char *gname = NULL, *counts = NULL, *triv = NULL; slong M = -1, prec = 256, q = 0; int sign = 1, scan = 0, do_unitary = 1;
    for (int i = 1; i < argc; i++) {
        if (!strcmp(argv[i], "--graph") && i + 1 < argc) gname = argv[++i];
        else if (!strcmp(argv[i], "--M") && i + 1 < argc) M = atol(argv[++i]);
        else if (!strcmp(argv[i], "--prec") && i + 1 < argc) prec = atol(argv[++i]);
        else if (!strcmp(argv[i], "--counts") && i + 1 < argc) counts = argv[++i];
        else if (!strcmp(argv[i], "--q") && i + 1 < argc) q = atol(argv[++i]);
        else if (!strcmp(argv[i], "--triv") && i + 1 < argc) triv = argv[++i];
        else if (!strcmp(argv[i], "--sign") && i + 1 < argc) sign = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--scan")) scan = 1;
        else if (!strcmp(argv[i], "--no-unitary")) do_unitary = 0;
        else { fprintf(stderr, "unknown option %s\n", argv[i]); return 2; }
    }
    ihz_weil_t W; ihz_spectrum_t S; int have_S = 0; fmpz_poly_t P, Psf, Q;
    fmpz_poly_init(P); fmpz_poly_init(Psf); fmpz_poly_init(Q);
    if (gname) {
        ihz_graph_t G;
        if (!ihz_graph_named(&G, gname) && !ihz_graph_read(&G, gname)) { fprintf(stderr, "unknown graph %s\n", gname); return 2; }
        slong qq; int reg = ihz_graph_is_regular(&G, &qq), bip = ihz_graph_is_bipartite(&G), con = ihz_graph_is_connected(&G);
        printf("graph %s: nv=%ld ne=%ld regular=%d q=%ld bipartite=%d connected=%d\n", gname, G.nv, G.ne, reg, reg ? qq : -1, bip, con);
        if (!reg) { fprintf(stderr, "irregular graphs are prototype-only in this MVP\n"); return 2; }
        fmpz_mat_t B; fmpz_mat_init(B, 2 * G.ne, 2 * G.ne); ihz_hashimoto(B, &G);
        printf("Ihara-Bass exact identity: %s\n", ihz_ihara_bass_check(&G, B) ? "PASS" : "FAIL");
        if (M < 0) M = G.nv;   /* critical K = R+1 <= 2 nv - 1, so Mp <= nv - 1 */
        if (!ihz_weil_from_graph(&W, &G, M, prec)) return 2;
        if (!ihz_retained_charpoly(P, B, qq, bip, G.nv, G.ne)) { printf("retained charpoly: inexact division (trivial divisor wrong?)\n"); return 3; }
        ihz_squarefree_part(Psf, P);
        printf("retained charpoly degree %ld, squarefree part degree R=%ld\n", fmpz_poly_degree(P), fmpz_poly_degree(Psf));
        if (!ihz_truth_spectrum(&S, P, prec)) { printf("truth spectrum FAILED\n"); return 3; }
        have_S = 1;
        printf("truth: %ld distinct retained points:\n", S.R);
        for (slong i = 0; i < S.R; i++) { printf("  mu_%ld (mult %ld) = ", i, S.mult[i]); acb_printn(S.mu + i, 15, 0); printf("\n"); }
        fmpz_mat_clear(B); ihz_graph_clear(&G);
    } else if (counts && q > 0 && triv) {
        /* parse counts and trivial points */
        slong n = 1; for (const char *p = counts; *p; p++) if (*p == ',') n++;
        if (n % 2 == 0) { fprintf(stderr, "--counts needs an odd number 2M+1 of entries\n"); return 2; }
        M = (n - 1) / 2; fmpz *N = _fmpz_vec_init(n); char *buf = strdup(counts); char *tok = strtok(buf, ","); slong i = 0;
        while (tok) { fmpz_set_str(N + i++, tok, 10); tok = strtok(NULL, ","); }
        slong nt = 1; for (const char *p = triv; *p; p++) if (*p == ',') nt++;
        fmpz *tr = _fmpz_vec_init(nt); slong *tm = malloc(nt * sizeof(slong)); char *b2 = strdup(triv); tok = strtok(b2, ","); i = 0;
        while (tok) { long pp, mm; sscanf(tok, "%ld:%ld", &pp, &mm); fmpz_set_si(tr + i, pp); tm[i++] = mm; tok = strtok(NULL, ","); }
        ihz_weil_from_counts(&W, N, M, q, tr, tm, nt, sign, prec);
        printf("counts: M=%ld q=%ld sign=%d ntriv=%ld\n", M, q, sign, nt);
        _fmpz_vec_clear(N, n); _fmpz_vec_clear(tr, nt); free(tm); free(buf); free(b2);
    } else { fprintf(stderr, "usage: see header of tools/ihz.c\n"); return 2; }

    printf("t_k (k = 0..%ld):", 2 * W.M); for (slong k = 0; k <= 2 * W.M; k++) { printf(" "); arb_printn(W.t + k, 8, 0); } printf("\n");
    slong R; slong Mc = ihz_critical_window(&R, &W);
    if (Mc < 0) printf("critical window: not reached within M=%ld (under-resolved everywhere)\n", W.M);
    else {
        printf("critical window: Mp=%ld (K=%ld), exact rank R=%ld\n", Mc, 2 * Mc + 1, R);
        if (ihz_kernel_poly_exact(Q, &W, Mc)) {
            printf("exact kernel polynomial Q(z) = "); fmpz_poly_print_pretty(Q, "z"); printf("\n");
            if (have_S) {
                fmpz_poly_t Qs; fmpz_poly_init(Qs); fmpz_poly_set(Qs, Psf);
                if (fmpz_sgn(fmpz_poly_lead(Qs)) < 0) fmpz_poly_neg(Qs, Qs);
                fmpz_poly_t Qp; fmpz_poly_init(Qp); fmpz_poly_primitive_part(Qp, Qs);
                printf("EXACT ANCHOR: kernel polynomial == squarefree retained charpoly: %s\n", fmpz_poly_equal(Q, Qp) ? "PASS" : "FAIL");
                fmpz_poly_clear(Qs); fmpz_poly_clear(Qp);
            }
        } else printf("kernel at the critical window is not one-dimensional\n");
    }
    arb_t eps, maxerr; arb_init(eps); arb_init(maxerr); slong nroots, unres; int uok;
    if (scan) {
        slong Mmax = (Mc >= 0 ? Mc + 1 : W.M); if (Mmax > W.M) Mmax = W.M;
        printf("\nscan  Mp   K  rank  kerdim  eps                          roots unres  maxerr(mid)   unitary\n");
        for (slong Mp = 0; Mp <= Mmax; Mp++) {
            slong rk = ihz_rank_exact(&W, Mp);
            run_window(&W, Mp, have_S ? &S : NULL, prec, do_unitary, 0, eps, &nroots, &unres, maxerr, &uok);
            printf("      %2ld  %2ld  %3ld  %3ld     ", Mp, 2 * Mp + 1, rk, 2 * Mp + 1 - rk); arb_printn(eps, 12, 0);
            printf("  %3ld  %3ld   ", nroots, unres); arb_printn(maxerr, 6, 0); printf("   %s\n", uok < 0 ? "-" : (uok ? "ok" : "FAIL"));
        }
    }
    slong Mrun = (Mc >= 0) ? Mc : W.M;
    printf("\nball stage at Mp=%ld (prec %ld):\n", Mrun, prec);
    run_window(&W, Mrun, have_S ? &S : NULL, prec, do_unitary, 1, eps, &nroots, &unres, maxerr, &uok);
    arb_clear(eps); arb_clear(maxerr);
    if (have_S) ihz_spectrum_clear(&S);
    ihz_weil_clear(&W); fmpz_poly_clear(P); fmpz_poly_clear(Psf); fmpz_poly_clear(Q);
    flint_cleanup();
    return 0;
}
