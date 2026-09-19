/* test_exact.c -- pinned exact checks for graph_io.c, hashimoto.c, cycles.c, truth.c.
 *
 * Ground truth (by file and line):
 *   notes/zeta-spectral-triples/ihara/run_ihara_proto.txt:33   K4       (|V|,|E|, N_k, divisor)
 *   notes/zeta-spectral-triples/ihara/run_ihara_proto.txt:124  cube=Q3  (bipartite, R = 4)
 *   notes/zeta-spectral-triples/ihara/run_ihara_proto.txt:239  petersen (N_k, R = 4, mult 5,5,4,4)
 *   notes/zeta-spectral-triples/ihara/run_ihara_proto.txt:917  necklace6 (nv 24, R = 20, real pair)
 *   notes/zeta-spectral-triples/ihara/run_ihara_proto.txt:1075 twok4    (disconnected, R = 4,
 *                                                                        retained {2, 1})
 *   notes/zeta-spectral-triples/ihara/lanes/theory.md:119      Petersen N_k = 30,0,0,0,0,120,120,0
 *   notes/zeta-spectral-triples/ihara/lanes/numerics.md:121    necklace6 real pair
 *                                                              mu = 1.66498945, 1.201208812
 *   notes/zeta-spectral-triples/ihara/lanes/code-audit.md:212  K4 retained pair mu^2 + mu + 2 = 0
 */
#include <stdio.h>
#include <string.h>
#include "ihz.h"
#include <flint/fmpz_vec.h>

#define PREC 160

static int failures = 0;

static void ck(int ok, const char *what)
{
    printf("%s %s\n", ok ? "PASS" : "FAIL", what);
    if (!ok) failures++;
}

/* a real ball around x of radius 1e-7, for comparing to the run record's printed decimals */
static void near_real(arb_t b, const char *dec)
{
    arb_set_str(b, dec, PREC);
    arb_add_error_2exp_si(b, -23);            /* ~1.2e-7 */
}

/* ------------------------------------------------------------------ helpers */

typedef struct {
    ihz_graph_t G;
    fmpz_mat_t B;
    slong q;
    int regular, bipartite, connected;
    fmpz_poly_t P;                             /* retained charpoly */
    int retained_ok;
    ihz_spectrum_t S;
} obj_t;

static void obj_load(obj_t *O, const char *name)
{
    memset(O, 0, sizeof(*O));
    if (!ihz_graph_named(&O->G, name))
    {
        printf("FAIL cannot build named graph %s\n", name);
        failures++;
        O->G.nv = O->G.ne = 0;
        O->G.u = O->G.v = NULL;
    }
    O->q = -1;
    O->regular = ihz_graph_is_regular(&O->G, &O->q);
    O->bipartite = ihz_graph_is_bipartite(&O->G);
    O->connected = ihz_graph_is_connected(&O->G);
    fmpz_mat_init(O->B, 2 * O->G.ne, 2 * O->G.ne);
    ihz_hashimoto(O->B, &O->G);
    fmpz_poly_init(O->P);
    O->retained_ok = ihz_retained_charpoly(O->P, O->B, O->q, O->bipartite, O->G.nv, O->G.ne);
    ihz_truth_spectrum(&O->S, O->P, PREC);
}

static void obj_clear(obj_t *O)
{
    ihz_spectrum_clear(&O->S);
    fmpz_poly_clear(O->P);
    fmpz_mat_clear(O->B);
    ihz_graph_clear(&O->G);
}

/* N_0..N_kmax against a pinned list */
static void check_counts(const obj_t *O, const slong *want, slong kmax, const char *tag)
{
    fmpz *N = _fmpz_vec_init(kmax + 1);
    slong k;
    int ok = 1;

    ihz_cycle_counts(N, O->B, kmax);
    for (k = 0; k <= kmax; k++)
        if (!fmpz_equal_si(N + k, want[k])) ok = 0;
    printf("%s %s: N_k k=0..%ld =", ok ? "PASS" : "FAIL", tag, (long) kmax);
    for (k = 0; k <= kmax; k++) { printf(" "); fmpz_print(N + k); }
    printf("\n");
    if (!ok) failures++;
    _fmpz_vec_clear(N, kmax + 1);
}

/* squarefree part degree must equal R (ihz.h:92) */
static void check_sqfree_degree(const obj_t *O, const char *tag)
{
    fmpz_poly_t Q;
    char buf[128];

    fmpz_poly_init(Q);
    ihz_squarefree_part(Q, O->P);
    snprintf(buf, sizeof(buf), "%s: deg(squarefree part) = R = %ld", tag, (long) O->S.R);
    ck(fmpz_poly_degree(Q) == O->S.R, buf);
    fmpz_poly_clear(Q);
}

/* every retained point has |mu|^2 = q (Ramanujan at the critical radius sqrt q) */
static void check_on_circle(const obj_t *O, const char *tag)
{
    arb_t a;
    slong i;
    int ok = 1;
    char buf[128];

    arb_init(a);
    for (i = 0; i < O->S.R; i++)
    {
        acb_abs(a, O->S.mu + i, PREC);
        arb_mul(a, a, a, PREC);
        if (!arb_contains_si(a, O->q)) ok = 0;
    }
    arb_clear(a);
    snprintf(buf, sizeof(buf), "%s: every retained |mu| = sqrt q = sqrt %ld", tag, (long) O->q);
    ck(ok, buf);
}

/* is the real number dec among the retained points, with multiplicity m? */
static int has_real_point(const obj_t *O, const char *dec, slong m)
{
    arb_t b;
    slong i;
    int found = 0;

    arb_init(b);
    near_real(b, dec);
    for (i = 0; i < O->S.R; i++)
        if (arb_contains_zero(acb_imagref(O->S.mu + i)) &&
            arb_overlaps(acb_realref(O->S.mu + i), b) &&
            O->S.mult[i] == m)
            found = 1;
    arb_clear(b);
    return found;
}

/* ---------------------------------------------------------------- the cases */

static void case_k4(void)
{
    obj_t O;
    static const slong want[7] = { 12, 0, 0, 24, 24, 0, 96 };
    fmpz_poly_t f, g;

    printf("-- K4 (run_ihara_proto.txt:33)\n");
    obj_load(&O, "K4");
    ck(O.G.nv == 4 && O.G.ne == 6, "K4: nv = 4, ne = 6");
    ck(O.regular && O.q == 2, "K4: regular, q = 2");
    ck(!O.bipartite, "K4: not bipartite");
    ck(O.connected, "K4: connected");
    ck(ihz_ihara_bass_check(&O.G, O.B), "K4: Ihara-Bass exact over Z");
    check_counts(&O, want, 6, "K4");

    /* retained charpoly = (x^2 + x + 2)^3, monic, degree 6 = 2|V|-2 (code-audit 2.4) */
    fmpz_poly_init(f);
    fmpz_poly_init(g);
    fmpz_poly_set_coeff_si(f, 2, 1);
    fmpz_poly_set_coeff_si(f, 1, 1);
    fmpz_poly_set_coeff_si(f, 0, 2);
    fmpz_poly_pow(g, f, 3);
    ck(O.retained_ok, "K4: trivial divisor divides charpoly(B) exactly");
    ck(fmpz_poly_equal(O.P, g), "K4: retained charpoly = (x^2 + x + 2)^3 (monic, degree 6)");
    fmpz_poly_clear(g);
    fmpz_poly_clear(f);

    ck(O.S.R == 2 && O.S.mult[0] == 3 && O.S.mult[1] == 3,
       "K4: R = 2 distinct retained points, each of multiplicity 3");
    check_on_circle(&O, "K4");
    check_sqfree_degree(&O, "K4");
    obj_clear(&O);
}

static void case_petersen(void)
{
    obj_t O;
    static const slong want[8] = { 30, 0, 0, 0, 0, 120, 120, 0 };
    fmpz_poly_t f, g, h;
    slong i, n5 = 0, n4 = 0;

    printf("-- Petersen (run_ihara_proto.txt:239, theory.md:119)\n");
    obj_load(&O, "petersen");
    ck(O.G.nv == 10 && O.G.ne == 15, "Petersen: nv = 10, ne = 15");
    ck(O.regular && O.q == 2, "Petersen: regular, q = 2");
    ck(!O.bipartite && O.connected, "Petersen: connected, not bipartite");
    ck(ihz_ihara_bass_check(&O.G, O.B), "Petersen: Ihara-Bass exact over Z");
    check_counts(&O, want, 7, "Petersen");

    /* lambda = 1 (mult 5) gives mu^2 - mu + 2; lambda = -2 (mult 4) gives mu^2 + 2mu + 2 */
    fmpz_poly_init(f); fmpz_poly_init(g); fmpz_poly_init(h);
    fmpz_poly_set_coeff_si(f, 2, 1); fmpz_poly_set_coeff_si(f, 1, -1); fmpz_poly_set_coeff_si(f, 0, 2);
    fmpz_poly_pow(h, f, 5);
    fmpz_poly_zero(f);
    fmpz_poly_set_coeff_si(f, 2, 1); fmpz_poly_set_coeff_si(f, 1, 2); fmpz_poly_set_coeff_si(f, 0, 2);
    fmpz_poly_pow(g, f, 4);
    fmpz_poly_mul(h, h, g);
    ck(O.retained_ok && fmpz_poly_equal(O.P, h),
       "Petersen: retained charpoly = (x^2-x+2)^5 (x^2+2x+2)^4 (degree 18)");
    fmpz_poly_clear(h); fmpz_poly_clear(g); fmpz_poly_clear(f);

    for (i = 0; i < O.S.R; i++)
    {
        if (O.S.mult[i] == 5) n5++;
        if (O.S.mult[i] == 4) n4++;
    }
    ck(O.S.R == 4 && n5 == 2 && n4 == 2,
       "Petersen: R = 4 (two points of multiplicity 5 from lambda = 1, two of 4 from lambda = -2)");
    check_on_circle(&O, "Petersen");
    check_sqfree_degree(&O, "Petersen");
    obj_clear(&O);
}

static void case_q3(void)
{
    obj_t O;
    fmpz_poly_t cp, quo, lin;
    int div_mq, div_m1;

    printf("-- Q3 (run_ihara_proto.txt:124)\n");
    obj_load(&O, "Q3");
    ck(O.G.nv == 8 && O.G.ne == 12, "Q3: nv = 8, ne = 12");
    ck(O.regular && O.q == 2, "Q3: regular, q = 2");
    ck(O.bipartite && O.connected, "Q3: bipartite and connected");
    ck(ihz_ihara_bass_check(&O.G, O.B), "Q3: Ihara-Bass exact over Z");

    /* the bipartite trivial points -q and -1 really are in spec(B) */
    fmpz_poly_init(cp); fmpz_poly_init(quo); fmpz_poly_init(lin);
    fmpz_mat_charpoly(cp, O.B);
    fmpz_poly_set_coeff_si(lin, 1, 1); fmpz_poly_set_coeff_si(lin, 0, O.q);
    div_mq = fmpz_poly_divides(quo, cp, lin);
    fmpz_poly_set_coeff_si(lin, 0, 1);
    div_m1 = fmpz_poly_divides(quo, cp, lin);
    ck(div_mq && div_m1, "Q3: bipartite trivial factors (x+q)(x+1) divide charpoly(B)");
    fmpz_poly_clear(lin); fmpz_poly_clear(quo); fmpz_poly_clear(cp);

    ck(O.retained_ok, "Q3: trivial divisor (with -q, -1) divides charpoly(B) exactly");
    ck(fmpz_poly_degree(O.P) == 2 * O.G.nv - 4, "Q3: retained degree = 2|V| - 4 = 12 (bipartite)");
    ck(O.S.R == 4, "Q3: R = 4");
    check_on_circle(&O, "Q3");
    check_sqfree_degree(&O, "Q3");
    obj_clear(&O);
}

static void case_k33(void)
{
    obj_t O;
    fmpz_poly_t f, g;

    printf("-- K33\n");
    obj_load(&O, "K33");
    ck(O.G.nv == 6 && O.G.ne == 9, "K33: nv = 6, ne = 9");
    ck(O.regular && O.q == 2, "K33: regular, q = 2");
    ck(O.bipartite && O.connected, "K33: bipartite and connected");
    ck(ihz_ihara_bass_check(&O.G, O.B), "K33: Ihara-Bass exact over Z");

    fmpz_poly_init(f); fmpz_poly_init(g);
    fmpz_poly_set_coeff_si(f, 2, 1); fmpz_poly_set_coeff_si(f, 0, 2);   /* lambda = 0 */
    fmpz_poly_pow(g, f, 4);
    ck(O.retained_ok && fmpz_poly_equal(O.P, g),
       "K33: retained charpoly = (x^2 + 2)^4 (degree 2|V|-4 = 8)");
    fmpz_poly_clear(g); fmpz_poly_clear(f);

    ck(O.S.R == 2, "K33: R = 2");
    check_on_circle(&O, "K33");
    check_sqfree_degree(&O, "K33");
    obj_clear(&O);
}

static void case_necklace6(void)
{
    obj_t O;

    printf("-- necklace:6 (run_ihara_proto.txt:917, numerics.md:121)\n");
    obj_load(&O, "necklace:6");
    ck(O.G.nv == 24 && O.G.ne == 36, "necklace:6: nv = 24, ne = 36");
    ck(O.regular && O.q == 2, "necklace:6: cubic (q = 2)");
    ck(O.connected, "necklace:6: connected");
    ck(!O.bipartite, "necklace:6: not bipartite");
    ck(ihz_ihara_bass_check(&O.G, O.B), "necklace:6: Ihara-Bass exact over Z");
    ck(O.retained_ok && fmpz_poly_degree(O.P) == 2 * O.G.nv - 2,
       "necklace:6: retained degree = 2|V| - 2 = 46");
    ck(O.S.R == 20, "necklace:6: R = 20 distinct retained points");
    ck(has_real_point(&O, "1.66498945", 2),
       "necklace:6: off-circle real point mu = 1.66498945 (multiplicity 2)");
    ck(has_real_point(&O, "1.201208812", 2),
       "necklace:6: reciprocal real point mu = 1.201208812 (multiplicity 2)");
    check_sqfree_degree(&O, "necklace:6");
    obj_clear(&O);
}

static void case_twok4(void)
{
    obj_t O;

    printf("-- twoK4 (run_ihara_proto.txt:1075)\n");
    obj_load(&O, "twoK4");
    ck(O.G.nv == 8 && O.G.ne == 12, "twoK4: nv = 8, ne = 12");
    ck(O.regular && O.q == 2, "twoK4: regular, q = 2");
    ck(!ihz_graph_is_connected(&O.G), "twoK4: is_connected = 0 (disconnected)");
    ck(ihz_ihara_bass_check(&O.G, O.B), "twoK4: Ihara-Bass exact over Z");
    ck(O.retained_ok && fmpz_poly_degree(O.P) == 2 * O.G.nv - 2,
       "twoK4: retained degree = 2|V| - 2 = 14");
    ck(O.S.R == 4, "twoK4: R = 4");
    ck(has_real_point(&O, "2", 1) && has_real_point(&O, "1", 1),
       "twoK4: retained contains the second Perron pair {q, 1} = {2, 1}");
    check_sqfree_degree(&O, "twoK4");
    obj_clear(&O);
}

/* graph_io round trip through the "nv ne" + edge-list reader */
static void case_io(void)
{
    ihz_graph_t G, H;
    FILE *f;
    const char *path = "build/test_exact_k4.edges";
    slong i;
    int ok = 1;

    printf("-- graph_io read/write round trip\n");
    ihz_graph_named(&G, "K4");
    f = fopen(path, "w");
    if (!f) { printf("FAIL graph_io: cannot open %s\n", path); failures++; ihz_graph_clear(&G); return; }
    fprintf(f, "%ld %ld\n", (long) G.nv, (long) G.ne);
    for (i = 0; i < G.ne; i++) fprintf(f, "%ld %ld\n", (long) G.u[i], (long) G.v[i]);
    fclose(f);
    ck(ihz_graph_read(&H, path), "graph_io: ihz_graph_read parses an edge list");
    if (H.nv != G.nv || H.ne != G.ne) ok = 0;
    for (i = 0; ok && i < G.ne; i++)
        if (H.u[i] != G.u[i] || H.v[i] != G.v[i]) ok = 0;
    ck(ok, "graph_io: round trip reproduces K4 exactly");
    ihz_graph_clear(&H);
    ihz_graph_clear(&G);

    ck(!ihz_graph_named(&H, "no_such_family"), "graph_io: unknown family name returns 0");
}

int main(void)
{
    printf("test_exact: graph_io, hashimoto, cycles, truth (prec = %d bits)\n", (int) PREC);
    case_io();
    case_k4();
    case_petersen();
    case_q3();
    case_k33();
    case_necklace6();
    case_twok4();
    printf("%s test_exact: %d failure(s)\n", failures ? "FAIL" : "PASS", failures);
    flint_cleanup();
    return failures != 0;
}
