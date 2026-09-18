/* ihz: the Connes-Consani-Moscovici construction for the Ihara zeta of a finite regular graph,
 * on FLINT/arb, with exact integer stages wherever the object is exact.
 *
 * Plan and ground truth: notes/zeta-spectral-triples/ihara/plan.md (sections 1, 4), the theory lane
 * notes/zeta-spectral-triples/ihara/lanes/theory.md (claims IH-n), the prototype
 * notes/zeta-spectral-triples/ihara/ihara_proto.py with run record run_ihara_proto.txt, and
 * refs/src/2511.23257/Araki-final-oct25.tex (CS) / refs/src/2511.22755/mc2arXiv.tex (CCM).
 *
 * CONVENTIONS (fixed; every module uses these, none redefines them)
 *  graph      undirected simple graph, vertices 0..nv-1, edges e = 0..ne-1 as pairs (u[e], v[e]).
 *  directed   directed edge index d in 0..2ne-1: d = e is u[e]->v[e], d = e+ne is v[e]->u[e].
 *  Hashimoto  B[(a->b),(b->c)] = 1 iff c != a  (def:hashimoto-operator; theory IH section 0).
 *  q          degree minus one; regular graphs only in this MVP (irregular: prototype only).
 *  critr      critical radius r = sqrt q; rescaled points w = mu / r.
 *  trivial    integer points with multiplicities: q, 1 (once); -q, -1 (once, if bipartite);
 *             +1 and -1 with multiplicity ne-nv each  (theory IH-1..IH-3).
 *  window     lengths j in {-M..M}, K = 2M+1; the Toeplitz form needs lags 0..2M, hence N_0..N_{2M}.
 *  sequence   t_k = sign * r^{-k} c_k,  c_k = N_k - sum_i tm_i tr_i^k  (exact integer c_k),
 *             sign = +1 for a graph (retained points are poles), -1 for a curve (zeros);
 *             two-sided extension t_{-k} = t_k  (theory IH-1, IH-2, IH-6, IH-33).
 *  Toeplitz   T_{jk} = t_{|j-k|}, j,k in {-M..M} stored as indices 0..K-1 with index j+M.
 *  grading    even block E ((M+1)x(M+1)) in the basis e_0 = delta_0, e_j = (delta_j + delta_{-j})/sqrt2,
 *             j = 1..M: E_00 = t_0, E_0j = sqrt2 t_j, E_ij = t_{|i-j|} + t_{i+j};
 *             odd block O (MxM) in (delta_j - delta_{-j})/sqrt2: O_ij = t_{|i-j|} - t_{i+j}.
 *             An even-block vector c maps back to xi_0 = c_0, xi_{+-j} = c_j / sqrt2  (theory IH-16).
 *  polynomial P(w) = sum_{j=-M}^{M} xi_j w^{j+M} (degree 2M); for even xi it is self-reciprocal and
 *             P(e^{i theta}) = e^{iM theta} R(theta), R(theta) = xi_0 + 2 sum_{j>=1} xi_j cos(j theta).
 *             The retained points are mu = r e^{i theta} at the roots of R  (CS:792, theory IH-11, IH-15).
 *  exact      D = diag(r^j), j = 0..K-1: (D T D)_{jk} = q^{min(j,k)} c_{|j-k|} is an INTEGER matrix
 *             with the same rank and kernel structure as T (ker T = D ker(DTD)); a kernel vector y of
 *             DTD gives the kernel polynomial sum_j y_j z^j in z = mu = r w directly, an integer
 *             polynomial vanishing on the retained divisor  (code-audit section 3; plan 4.3).
 *  eta        the delta at the window edge (position index 0), NOT all-ones (plan 1.3, convention trap).
 */
#ifndef IHZ_H
#define IHZ_H

#include <flint/flint.h>
#include <flint/fmpz.h>
#include <flint/fmpz_mat.h>
#include <flint/fmpz_poly.h>
#include <flint/fmpz_poly_factor.h>
#include <flint/fmpz_vec.h>
#include <flint/arb_fmpz_poly.h>
#include <flint/fmpq_mat.h>
#include <flint/arb.h>
#include <flint/acb.h>
#include <flint/arb_mat.h>
#include <flint/acb_mat.h>
#include <flint/arb_poly.h>
#include <flint/acb_poly.h>

#ifdef __cplusplus
extern "C" {
#endif

/* ---------------------------------------------------------------- graph_io.c */
typedef struct { slong nv, ne; slong *u, *v; } ihz_graph_t;

void ihz_graph_init(ihz_graph_t *G, slong nv, slong ne);        /* allocates u, v (uninitialised) */
void ihz_graph_clear(ihz_graph_t *G);
int  ihz_graph_read(ihz_graph_t *G, const char *path);          /* "nv ne" then ne lines "u v"; 1 ok, 0 fail */
/* named families; return 0 on unknown name. Names: K4 Kn:<n> Q3 Qd:<d> petersen heawood pappus
 * K33 Kmn:<m>,<n> Cn:<n> prism:<n> (C_n x K_2) necklace:<k> (k copies of K4 minus an edge joined
 * in a cycle by the freed degree-2 vertices) twoK4 (two disjoint K4). Exact constructions as in
 * notes/zeta-spectral-triples/ihara/ihara_proto.py (function build_graph). */
int  ihz_graph_named(ihz_graph_t *G, const char *name);
int  ihz_graph_is_regular(const ihz_graph_t *G, slong *q);      /* 1 and q = degree-1 if regular */
int  ihz_graph_is_bipartite(const ihz_graph_t *G);
int  ihz_graph_is_connected(const ihz_graph_t *G);

/* ---------------------------------------------------------------- hashimoto.c */
void ihz_hashimoto(fmpz_mat_t B, const ihz_graph_t *G);        /* B is 2ne x 2ne, caller inits */
void ihz_adjacency(fmpz_mat_t A, const ihz_graph_t *G);        /* nv x nv */

/* ---------------------------------------------------------------- cycles.c */
/* N[k] = Tr B^k for k = 0..kmax (N[0] = 2ne), exact, by repeated multiplication. */
void ihz_cycle_counts(fmpz *N, const fmpz_mat_t B, slong kmax);
/* Ihara-Bass as an exact polynomial identity: det(1 - uB) == (1-u^2)^{ne-nv} det(1 - Au + q u^2).
 * Returns 1 if the two fmpz_poly are equal. */
int  ihz_ihara_bass_check(const ihz_graph_t *G, const fmpz_mat_t B);

/* ---------------------------------------------------------------- truth.c */
/* Retained characteristic polynomial: charpoly(B) divided exactly by the trivial factors
 * (x-q)(x-1) [(x+q)(x+1) if bipartite] (x-1)^{ne-nv} (x+1)^{ne-nv}. Returns 1 on exact division. */
int  ihz_retained_charpoly(fmpz_poly_t P, const fmpz_mat_t B, slong q, int bipartite, slong nv, slong ne);
/* Certified retained spectrum with multiplicities from the squarefree factorisation of P
 * (arb_fmpz_poly_complex_roots per squarefree factor; never on P itself: it does not terminate on
 * repeated roots). R = number of distinct points. mu[i] balls, mult[i] >= 1, i = 0..R-1. */
typedef struct { acb_ptr mu; slong *mult; slong R; } ihz_spectrum_t;
int  ihz_truth_spectrum(ihz_spectrum_t *S, const fmpz_poly_t P, slong prec);
void ihz_spectrum_clear(ihz_spectrum_t *S);
/* Squarefree part of P (product of distinct irreducible factors, each once): its degree is R. */
void ihz_squarefree_part(fmpz_poly_t Q, const fmpz_poly_t P);

/* ---------------------------------------------------------------- weil_data.c */
typedef struct {
    slong M;          /* window; sequences have length 2M+1 (lags 0..2M) */
    slong q;          /* critr^2 */
    int   sign;       /* +1 graph (poles), -1 curve (zeros) */
    slong ntriv;      /* trivial points */
    fmpz *tr;         /* integer trivial points */
    slong *tm;        /* their multiplicities */
    fmpz *N;          /* N[0..2M] raw counts */
    fmpz *c;          /* c[0..2M] = N_k - sum_i tm_i tr_i^k, exact */
    arb_ptr t;        /* t[0..2M] = sign * q^{-k/2} c_k, balls at prec given at construction */
} ihz_weil_t;

/* From a regular graph: fills q, trivial divisor (per the convention table), N by ihz_cycle_counts,
 * c, t. sign = +1. Returns 0 if G is not regular. */
int  ihz_weil_from_graph(ihz_weil_t *W, const ihz_graph_t *G, slong M, slong prec);
/* From raw counts (curve or any transfer operator): N[0..2M], q, trivial points, sign. */
void ihz_weil_from_counts(ihz_weil_t *W, const fmpz *N, slong M, slong q,
                          const fmpz *tr, const slong *tm, slong ntriv, int sign, slong prec);
void ihz_weil_clear(ihz_weil_t *W);

/* ---------------------------------------------------------------- toeplitz.c */
/* T (K x K, K = 2M'+1 <= 2M+1 for any M' <= W->M): T_{jk} = t_{|j-k|}. */
void ihz_toeplitz(arb_mat_t T, const ihz_weil_t *W, slong Mp, slong prec);
void ihz_even_block(arb_mat_t E, const ihz_weil_t *W, slong Mp, slong prec);   /* (Mp+1)^2 */
void ihz_odd_block(arb_mat_t O, const ihz_weil_t *W, slong Mp, slong prec);    /* Mp^2 */
/* even-block vector c (length Mp+1) -> xi (length 2Mp+1, index j+Mp). */
void ihz_even_to_full(arb_ptr xi, arb_srcptr c, slong Mp, slong prec);
/* Integer matrix (DTD)_{jk} = q^{min(j,k)} c_{|j-k|}, K x K, K = 2Mp+1 (sign included in c's sign). */
void ihz_toeplitz_exact(fmpz_mat_t DTD, const ihz_weil_t *W, slong Mp);

/* ---------------------------------------------------------------- rank.c (exact) */
slong ihz_rank_exact(const ihz_weil_t *W, slong Mp);              /* rank of T_K over Q */
/* Critical window: the smallest K = 2Mp+1 <= 2M+1 with rank T_K < K; returns Mp and sets *R = rank
 * (= K-1 when found). Returns -1 if none within the available lags (window under-resolved). */
slong ihz_critical_window(slong *R, const ihz_weil_t *W);
/* At a window with one-dimensional kernel: the integer kernel polynomial Q(z) = sum_j y_j z^j of
 * DTD (z = mu), primitive with positive leading coefficient. Returns 1 if the kernel is exactly
 * one-dimensional, 0 otherwise. */
int   ihz_kernel_poly_exact(fmpz_poly_t Q, const ihz_weil_t *W, slong Mp);

/* ---------------------------------------------------------------- eigmin.c (port of zst/src/eigmin.c) */
int   ihz_eigmin(arb_t eps, arb_ptr v, const arb_mat_t E, slong iters, slong prec);
slong ihz_inertia_neg(const arb_mat_t A, const arb_t shift, slong prec);
int   ihz_certify_even_simple(const arb_mat_t E, const arb_mat_t O, const arb_t eps, arb_srcptr v, slong prec);

/* ---------------------------------------------------------------- circle_roots.c */
/* Roots theta in [0, pi] of R(theta) = xi_0 + 2 sum_{j=1}^{Mp} xi_j cos(j theta), xi given as the
 * even-block vector mapped to the full vector (xi[j+Mp]); certified balls, increasing, disjoint.
 * Returns the count found (<= maxroots); *unresolved counts candidates not certified. A root at
 * theta in (0, pi) stands for the conjugate pair; theta = 0 or pi is a single real point. */
slong ihz_circle_roots(arb_ptr theta, slong maxroots, slong *unresolved, arb_srcptr xi, slong Mp, slong prec);
/* R(theta) and R'(theta) at a ball theta. */
void  ihz_R_eval(arb_t val, arb_t der, const arb_t theta, arb_srcptr xi, slong Mp, slong prec);

/* ---------------------------------------------------------------- unitary.c */
/* U = Z^* - |Z^* xi><eta| in the position basis (K x K), Z the cyclic shift (Z e_j = e_{j+1 mod K}),
 * eta = delta at position index 0, xi normalised to xi[0] = 1 (theory IH-11). */
void  ihz_unitary_build(arb_mat_t U, arb_srcptr xi, slong K, slong prec);
/* Certificate that U^T (T - eps) U == T - eps: 1 iff every entry ball of the difference contains 0. */
int   ihz_unitary_check(const arb_mat_t U, const arb_mat_t T, const arb_t eps, slong prec);
/* Lemma key (iii): det(U - w) versus -w (-1)^{K+1} Ptilde(w), Ptilde(w) = sum_k xi_k w^{K-1-k}, at a
 * point w; 1 iff the two balls overlap. */
int   ihz_unitary_det_check(const arb_mat_t U, arb_srcptr xi, slong K, const acb_t w, slong prec);

/* ---------------------------------------------------------------- prony.c */
/* Weights alpha_i with t_d = sum_i alpha_i (mu_i/r)^d, d = 0..R-1, from certified points mu_i (balls);
 * alpha[i] balls. Multiplicities are the integers the balls contain. */
void  ihz_prony_weights(acb_ptr alpha, const ihz_weil_t *W, acb_srcptr mu, slong R, slong prec);

/* ---------------------------------------------------------------- compare.c */
/* Match certified root angles theta[0..n-1] (points mu = r e^{i theta}, with conjugates implied for
 * theta in (0,pi)) against the truth spectrum S: for every truth point, the certified distance to
 * the nearest root point; err[i], i = 0..S->R-1. */
void  ihz_compare(arb_ptr err, arb_srcptr theta, slong n, const ihz_spectrum_t *S, slong q, slong prec);

#ifdef __cplusplus
}
#endif
#endif
