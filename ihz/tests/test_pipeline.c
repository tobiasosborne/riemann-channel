/* End-to-end anchor: on K4 and Petersen the exact stage finds the critical window and the kernel
 * polynomial equals the squarefree retained characteristic polynomial; the ball stage at that window
 * returns certified roots matching the certified truth, the unitary key lemma certifies, Prony weights
 * contain the multiplicities. Ground truth: notes/zeta-spectral-triples/ihara/plan.md sections 1.4, 6;
 * lanes/theory.md IH-11, IH-18, IH-20; run_ihara_proto.txt. */
#include <stdio.h>
#include <flint/fmpz_vec.h>
#include "ihz.h"

static int fails = 0;
#define CHECK(cond, msg) do { printf("%s: %s\n", (cond) ? "PASS" : "FAIL", msg); if (!(cond)) fails++; } while (0)

static void anchor(const char *name, slong R_expected, slong Mc_expected, double eps_under_expected)
{
    slong prec = 256, i;
    ihz_graph_t G; fmpz_mat_t B; ihz_weil_t W; ihz_spectrum_t S; fmpz_poly_t P, Psf, Q;
    CHECK(ihz_graph_named(&G, name), "named graph built");
    slong q; CHECK(ihz_graph_is_regular(&G, &q), "regular");
    int bip = ihz_graph_is_bipartite(&G);
    fmpz_mat_init(B, 2 * G.ne, 2 * G.ne); ihz_hashimoto(B, &G);
    CHECK(ihz_ihara_bass_check(&G, B), "Ihara-Bass exact identity");
    CHECK(ihz_weil_from_graph(&W, &G, G.nv, prec), "Weil data from graph");
    fmpz_poly_init(P); fmpz_poly_init(Psf); fmpz_poly_init(Q);
    CHECK(ihz_retained_charpoly(P, B, q, bip, G.nv, G.ne), "retained charpoly exact division");
    ihz_squarefree_part(Psf, P);
    CHECK(fmpz_poly_degree(Psf) == R_expected, "R = degree of squarefree part");
    CHECK(ihz_truth_spectrum(&S, P, prec), "truth spectrum certified");
    CHECK(S.R == R_expected, "truth spectrum has R distinct points");
    slong R; slong Mc = ihz_critical_window(&R, &W);
    CHECK(Mc == Mc_expected && R == R_expected, "critical window Mp = R/2, rank R");
    CHECK(ihz_kernel_poly_exact(Q, &W, Mc), "kernel one-dimensional at the critical window");
    if (fmpz_sgn(fmpz_poly_lead(Psf)) < 0) fmpz_poly_neg(Psf, Psf);
    fmpz_poly_primitive_part(Psf, Psf);
    CHECK(fmpz_poly_equal(Q, Psf), "EXACT ANCHOR: kernel polynomial == squarefree retained charpoly");
    /* under-resolved window eps */
    if (Mc >= 1) {
        arb_mat_t E1; arb_t e1; arb_ptr v1; arb_mat_init(E1, Mc, Mc); arb_init(e1); v1 = _arb_vec_init(Mc);
        ihz_even_block(E1, &W, Mc - 1, prec);
        CHECK(ihz_eigmin(e1, v1, E1, 200, prec), "eigmin certified at Mp = Mc - 1");
        arb_t ref; arb_init(ref); arb_set_d(ref, eps_under_expected); arb_add_error_2exp_si(ref, -20);
        CHECK(arb_overlaps(e1, ref), "eps at Mp = Mc - 1 matches the prototype");
        arb_clear(ref); arb_mat_clear(E1); arb_clear(e1); _arb_vec_clear(v1, Mc);
    }
    /* ball stage at the critical window */
    slong K = 2 * Mc + 1;
    arb_mat_t E, T; arb_t eps; arb_ptr v, xi, theta, err;
    arb_mat_init(E, Mc + 1, Mc + 1); arb_mat_init(T, K, K); arb_init(eps);
    ihz_even_block(E, &W, Mc, prec); ihz_toeplitz(T, &W, Mc, prec);
    v = _arb_vec_init(Mc + 1); xi = _arb_vec_init(K);
    CHECK(ihz_eigmin(eps, v, E, 200, prec), "eigmin certified at the critical window");
    CHECK(arb_contains_zero(eps), "eps ball contains 0 at the critical window");
    ihz_even_to_full(xi, v, Mc, prec);
    theta = _arb_vec_init(K); slong unres;
    slong nroots = ihz_circle_roots(theta, K, &unres, xi, Mc, prec);
    CHECK(unres == 0, "no unresolved root candidates");
    CHECK(2 * nroots == R_expected || (2 * nroots - 1 == R_expected), "root count accounts for R points");
    err = _arb_vec_init(S.R);
    ihz_compare(err, theta, nroots, &S, q, prec);
    int allsmall = 1;
    for (i = 0; i < S.R; i++) { arb_t b; arb_init(b); arb_abs(b, err + i); if (!(arb_contains_zero(err + i) || mag_cmp_2exp_si(arb_radref(err + i), -100) < 0)) allsmall = 0; if (arf_cmpabs_2exp_si(arb_midref(err + i), -100) > 0) allsmall = 0; arb_clear(b); }
    CHECK(allsmall, "every truth point within 2^-100 of a certified root point");
    /* Prony weights at the truth points */
    acb_ptr alpha = _acb_vec_init(S.R); ihz_prony_weights(alpha, &W, S.mu, S.R, prec);
    int wok = 1; for (i = 0; i < S.R; i++) { acb_t m; acb_init(m); acb_set_si(m, S.mult[i]); if (!acb_contains(alpha + i, m)) wok = 0; acb_clear(m); }
    CHECK(wok, "Prony weight balls contain the multiplicities");
    /* unitary key lemma */
    arb_mat_t U; arb_ptr xin = _arb_vec_init(K); acb_t w; arb_mat_init(U, K, K);
    CHECK(!arb_contains_zero(xi + 0), "xi_0 nonzero");
    for (i = 0; i < K; i++) arb_div(xin + i, xi + i, xi + 0, prec);
    ihz_unitary_build(U, xin, K, prec);
    CHECK(ihz_unitary_check(U, T, eps, prec), "U^T (T - eps) U = T - eps certified");
    acb_init(w); acb_set_d_d(w, 0.3, 0.4);
    CHECK(ihz_unitary_det_check(U, xin, K, w, prec), "det(U - w) identity certified");
    acb_clear(w); arb_mat_clear(U); _arb_vec_clear(xin, K);
    _acb_vec_clear(alpha, S.R); _arb_vec_clear(err, S.R); _arb_vec_clear(theta, K);
    _arb_vec_clear(v, Mc + 1); _arb_vec_clear(xi, K); arb_mat_clear(E); arb_mat_clear(T); arb_clear(eps);
    ihz_spectrum_clear(&S); ihz_weil_clear(&W); fmpz_poly_clear(P); fmpz_poly_clear(Psf); fmpz_poly_clear(Q);
    fmpz_mat_clear(B); ihz_graph_clear(&G);
}

int main(void)
{
    /* K4: R = 2, critical Mp = 1, multiplicity 3 each; eps at Mp = 0 is t_0 = 6 */
    printf("== K4\n"); anchor("K4", 2, 1, 6.0);
    /* Petersen: R = 4, critical Mp = 2; Prony weights checked against the truth's own multiplicities */
    printf("== petersen\n"); anchor("petersen", 4, 2, 9.4476568);
    printf(fails ? "test_pipeline: %d FAILURES\n" : "test_pipeline: PASS\n", fails);
    flint_cleanup();
    return fails ? 1 : 0;
}
