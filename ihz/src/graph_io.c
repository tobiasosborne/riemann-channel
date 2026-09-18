/* graph_io.c -- undirected simple graphs and the named families.
 *
 * Ground truth (by file and line):
 *   notes/zeta-spectral-triples/ihara/ihara_proto.py:60   lcf()       (LCF notation)
 *   notes/zeta-spectral-triples/ihara/ihara_proto.py:70   necklace()  (cubic necklace)
 *   notes/zeta-spectral-triples/ihara/ihara_proto.py:81   GRAPHS      (k4, cube, petersen, k33,
 *                                                          heawood, pappus, necklace*, twok4)
 *   notes/zeta-spectral-triples/ihara/plan.md:75          section 1.1 (objects; q = deg - 1)
 *   notes/zeta-spectral-triples/ihara/plan.md:323         section 4.2 (module list: K_n, Q_d,
 *                                                          Petersen, Heawood, K_{m,n}, C_n x K_2)
 *   notes/zeta-spectral-triples/ihara/lanes/theory.md:23  section 0 (standing notation)
 * Vertex/edge counts and spectra reproduce notes/zeta-spectral-triples/ihara/run_ihara_proto.txt.
 *
 * Conventions are those of include/ihz.h: vertices 0..nv-1, edges e = 0..ne-1 as pairs (u[e],v[e]).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ihz.h"

/* ------------------------------------------------------------------ core */

void ihz_graph_init(ihz_graph_t *G, slong nv, slong ne)
{
    G->nv = nv;
    G->ne = ne;
    G->u = ne > 0 ? flint_malloc(sizeof(slong) * (size_t) ne) : NULL;
    G->v = ne > 0 ? flint_malloc(sizeof(slong) * (size_t) ne) : NULL;
}

void ihz_graph_clear(ihz_graph_t *G)
{
    if (G->u) flint_free(G->u);
    if (G->v) flint_free(G->v);
    G->u = G->v = NULL;
    G->nv = G->ne = 0;
}

int ihz_graph_read(ihz_graph_t *G, const char *path)
{
    FILE *f;
    slong nv, ne, i;
    long a, b, xnv, xne;

    f = fopen(path, "r");
    if (!f) return 0;
    if (fscanf(f, "%ld %ld", &xnv, &xne) != 2 || xnv < 0 || xne < 0)
    {
        fclose(f);
        return 0;
    }
    nv = (slong) xnv;
    ne = (slong) xne;
    ihz_graph_init(G, nv, ne);
    for (i = 0; i < ne; i++)
    {
        if (fscanf(f, "%ld %ld", &a, &b) != 2 ||
            a < 0 || b < 0 || a >= xnv || b >= xnv)
        {
            ihz_graph_clear(G);
            fclose(f);
            return 0;
        }
        G->u[i] = (slong) a;
        G->v[i] = (slong) b;
    }
    fclose(f);
    return 1;
}

/* ------------------------------------------------------- edge-set builder */

typedef struct { slong *u, *v; slong n, alloc; } edgebuf_t;

static void eb_init(edgebuf_t *E)
{
    E->n = 0;
    E->alloc = 16;
    E->u = flint_malloc(sizeof(slong) * (size_t) E->alloc);
    E->v = flint_malloc(sizeof(slong) * (size_t) E->alloc);
}

static void eb_clear(edgebuf_t *E)
{
    flint_free(E->u);
    flint_free(E->v);
}

/* add the undirected edge {a,b} unless already present or a == b (simple graph) */
static void eb_add(edgebuf_t *E, slong a, slong b)
{
    slong i, lo, hi;

    if (a == b) return;
    lo = a < b ? a : b;
    hi = a < b ? b : a;
    for (i = 0; i < E->n; i++)
        if (E->u[i] == lo && E->v[i] == hi) return;
    if (E->n == E->alloc)
    {
        E->alloc *= 2;
        E->u = flint_realloc(E->u, sizeof(slong) * (size_t) E->alloc);
        E->v = flint_realloc(E->v, sizeof(slong) * (size_t) E->alloc);
    }
    E->u[E->n] = lo;
    E->v[E->n] = hi;
    E->n++;
}

/* lexicographic sort, so the edge order is the prototype's sorted(set(...)) order */
static void eb_sort(edgebuf_t *E)
{
    slong i, j, tu, tv;

    for (i = 1; i < E->n; i++)
    {
        tu = E->u[i];
        tv = E->v[i];
        for (j = i; j > 0 && (E->u[j - 1] > tu ||
                              (E->u[j - 1] == tu && E->v[j - 1] > tv)); j--)
        {
            E->u[j] = E->u[j - 1];
            E->v[j] = E->v[j - 1];
        }
        E->u[j] = tu;
        E->v[j] = tv;
    }
}

static void eb_finish(ihz_graph_t *G, edgebuf_t *E, slong nv)
{
    slong i;

    eb_sort(E);
    ihz_graph_init(G, nv, E->n);
    for (i = 0; i < E->n; i++)
    {
        G->u[i] = E->u[i];
        G->v[i] = E->v[i];
    }
    eb_clear(E);
}

/* ---------------------------------------------------------- the families */

/* ihara_proto.py:60  the n-cycle plus chords i -- i + shifts[i mod len] */
static void build_lcf(edgebuf_t *E, slong n, const slong *shifts, slong ns)
{
    slong i, j;

    for (i = 0; i < n; i++)
        eb_add(E, i, (i + 1) % n);
    for (i = 0; i < n; i++)
    {
        j = ((i + shifts[i % ns]) % n + n) % n;
        eb_add(E, i, j);
    }
}

/* ihara_proto.py:70  k copies of K4 minus an edge, joined in a cycle by the freed
 * degree-2 vertices: block i has p=4i, q=4i+1 (degree 2 inside), r=4i+2, s=4i+3. */
static void build_necklace(edgebuf_t *E, slong k)
{
    slong i, p, q, r, s;

    for (i = 0; i < k; i++)
    {
        p = 4 * i; q = 4 * i + 1; r = 4 * i + 2; s = 4 * i + 3;
        eb_add(E, p, r);
        eb_add(E, p, s);
        eb_add(E, q, r);
        eb_add(E, q, s);
        eb_add(E, r, s);
    }
    for (i = 0; i < k; i++)
        eb_add(E, 4 * i + 1, 4 * ((i + 1) % k));
}

/* "name:<a>" / "name:<a>,<b>": parse the integer arguments after the colon. */
static int parse_args(const char *s, slong *a, slong *b, int want)
{
    char *end;
    long x, y;

    x = strtol(s, &end, 10);
    if (end == s) return 0;
    *a = (slong) x;
    if (want == 1) return *end == '\0';
    if (*end != ',') return 0;
    s = end + 1;
    y = strtol(s, &end, 10);
    if (end == s || *end != '\0') return 0;
    *b = (slong) y;
    return 1;
}

int ihz_graph_named(ihz_graph_t *G, const char *name)
{
    edgebuf_t E;
    slong i, j, b, n, m, d, nv;
    const char *arg;
    static const slong heawood_shifts[2] = { 5, -5 };
    static const slong pappus_shifts[6]  = { 5, 7, -7, 7, -7, -5 };

    if (!name) return 0;
    arg = strchr(name, ':');
    arg = arg ? arg + 1 : NULL;

    eb_init(&E);

    /* K4 == Kn:4 (ihara_proto.py:82 "k4") */
    if (!strcmp(name, "K4"))
    {
        n = 4;
        for (i = 0; i < n; i++) for (j = i + 1; j < n; j++) eb_add(&E, i, j);
        eb_finish(G, &E, n);
        return 1;
    }
    if (!strncmp(name, "Kn:", 3))
    {
        if (!arg || !parse_args(arg, &n, &m, 1) || n < 1) { eb_clear(&E); return 0; }
        for (i = 0; i < n; i++) for (j = i + 1; j < n; j++) eb_add(&E, i, j);
        eb_finish(G, &E, n);
        return 1;
    }
    /* Q3 == Qd:3 (ihara_proto.py:83 "cube": a -- a xor 2^b) */
    if (!strcmp(name, "Q3") || !strncmp(name, "Qd:", 3))
    {
        d = 3;
        if (arg && (!parse_args(arg, &d, &m, 1) || d < 1)) { eb_clear(&E); return 0; }
        if (d >= (slong) (8 * sizeof(slong) - 2)) { eb_clear(&E); return 0; }
        nv = (slong) 1 << d;
        for (i = 0; i < nv; i++)
            for (b = 0; b < d; b++)
            {
                j = i ^ ((slong) 1 << b);
                if (i < j) eb_add(&E, i, j);
            }
        eb_finish(G, &E, nv);
        return 1;
    }
    /* ihara_proto.py:84: outer 5-cycle, inner pentagram, spokes */
    if (!strcmp(name, "petersen"))
    {
        for (i = 0; i < 5; i++) eb_add(&E, i, (i + 1) % 5);
        for (i = 0; i < 5; i++) eb_add(&E, 5 + i, 5 + (i + 2) % 5);
        for (i = 0; i < 5; i++) eb_add(&E, i, i + 5);
        eb_finish(G, &E, 10);
        return 1;
    }
    if (!strcmp(name, "heawood"))          /* ihara_proto.py:88 lcf(14, [5,-5]) */
    {
        build_lcf(&E, 14, heawood_shifts, 2);
        eb_finish(G, &E, 14);
        return 1;
    }
    if (!strcmp(name, "pappus"))           /* ihara_proto.py:89 lcf(18,[5,7,-7,7,-7,-5]) */
    {
        build_lcf(&E, 18, pappus_shifts, 6);
        eb_finish(G, &E, 18);
        return 1;
    }
    /* K33 == Kmn:3,3 (ihara_proto.py:87 "k33") */
    if (!strcmp(name, "K33"))
    {
        for (i = 0; i < 3; i++) for (j = 3; j < 6; j++) eb_add(&E, i, j);
        eb_finish(G, &E, 6);
        return 1;
    }
    if (!strncmp(name, "Kmn:", 4))
    {
        if (!arg || !parse_args(arg, &m, &n, 2) || m < 1 || n < 1) { eb_clear(&E); return 0; }
        for (i = 0; i < m; i++) for (j = m; j < m + n; j++) eb_add(&E, i, j);
        eb_finish(G, &E, m + n);
        return 1;
    }
    if (!strncmp(name, "Cn:", 3))          /* the n-cycle; q = 1 (degenerate, plan.md:4.4) */
    {
        if (!arg || !parse_args(arg, &n, &m, 1) || n < 3) { eb_clear(&E); return 0; }
        for (i = 0; i < n; i++) eb_add(&E, i, (i + 1) % n);
        eb_finish(G, &E, n);
        return 1;
    }
    if (!strncmp(name, "prism:", 6))       /* C_n x K_2 (plan.md:323) */
    {
        if (!arg || !parse_args(arg, &n, &m, 1) || n < 3) { eb_clear(&E); return 0; }
        for (i = 0; i < n; i++)
        {
            eb_add(&E, i, (i + 1) % n);
            eb_add(&E, n + i, n + (i + 1) % n);
            eb_add(&E, i, n + i);
        }
        eb_finish(G, &E, 2 * n);
        return 1;
    }
    if (!strncmp(name, "necklace:", 9))
    {
        if (!arg || !parse_args(arg, &n, &m, 1) || n < 2) { eb_clear(&E); return 0; }
        build_necklace(&E, n);
        eb_finish(G, &E, 4 * n);
        return 1;
    }
    if (!strcmp(name, "twoK4"))            /* ihara_proto.py:93 "twok4" */
    {
        for (b = 0; b < 2; b++)
            for (i = 0; i < 4; i++)
                for (j = i + 1; j < 4; j++)
                    eb_add(&E, 4 * b + i, 4 * b + j);
        eb_finish(G, &E, 8);
        return 1;
    }

    eb_clear(&E);
    return 0;
}

/* ------------------------------------------------------------ predicates */

static slong *degrees(const ihz_graph_t *G)
{
    slong *deg, i;

    deg = flint_calloc((size_t) (G->nv > 0 ? G->nv : 1), sizeof(slong));
    for (i = 0; i < G->ne; i++)
    {
        deg[G->u[i]]++;
        deg[G->v[i]]++;
    }
    return deg;
}

int ihz_graph_is_regular(const ihz_graph_t *G, slong *q)
{
    slong *deg, i, d;
    int ok = 1;

    if (G->nv <= 0) return 0;
    deg = degrees(G);
    d = deg[0];
    for (i = 1; i < G->nv; i++)
        if (deg[i] != d) { ok = 0; break; }
    flint_free(deg);
    if (ok && q) *q = d - 1;                        /* q = degree - 1 (ihz.h convention table) */
    return ok;
}

/* adjacency lists, as a CSR-style pair (start[], adj[]) over the 2ne directed ends */
static void adjacency_lists(const ihz_graph_t *G, slong **start_out, slong **adj_out)
{
    slong *start, *adj, *pos, i;

    start = flint_calloc((size_t) (G->nv + 1), sizeof(slong));
    adj = flint_malloc(sizeof(slong) * (size_t) (2 * G->ne > 0 ? 2 * G->ne : 1));
    pos = flint_calloc((size_t) (G->nv > 0 ? G->nv : 1), sizeof(slong));
    for (i = 0; i < G->ne; i++)
    {
        start[G->u[i] + 1]++;
        start[G->v[i] + 1]++;
    }
    for (i = 0; i < G->nv; i++)
        start[i + 1] += start[i];
    for (i = 0; i < G->ne; i++)
    {
        adj[start[G->u[i]] + pos[G->u[i]]++] = G->v[i];
        adj[start[G->v[i]] + pos[G->v[i]]++] = G->u[i];
    }
    flint_free(pos);
    *start_out = start;
    *adj_out = adj;
}

int ihz_graph_is_bipartite(const ihz_graph_t *G)
{
    slong *start, *adj, *colour, *stack, top, i, s, x, y, k;
    int ok = 1;

    if (G->nv <= 0) return 1;
    adjacency_lists(G, &start, &adj);
    colour = flint_malloc(sizeof(slong) * (size_t) G->nv);
    stack = flint_malloc(sizeof(slong) * (size_t) G->nv);
    for (i = 0; i < G->nv; i++) colour[i] = -1;

    for (s = 0; s < G->nv && ok; s++)
    {
        if (colour[s] >= 0) continue;
        colour[s] = 0;
        top = 0;
        stack[top++] = s;
        while (top > 0 && ok)
        {
            x = stack[--top];
            for (k = start[x]; k < start[x + 1]; k++)
            {
                y = adj[k];
                if (colour[y] < 0)
                {
                    colour[y] = 1 - colour[x];
                    stack[top++] = y;
                }
                else if (colour[y] == colour[x]) { ok = 0; break; }
            }
        }
    }
    flint_free(stack);
    flint_free(colour);
    flint_free(adj);
    flint_free(start);
    return ok;
}

int ihz_graph_is_connected(const ihz_graph_t *G)
{
    slong *start, *adj, *seen, *stack, top, i, x, y, k, n = 0;

    if (G->nv <= 0) return 1;
    adjacency_lists(G, &start, &adj);
    seen = flint_calloc((size_t) G->nv, sizeof(slong));
    stack = flint_malloc(sizeof(slong) * (size_t) G->nv);
    top = 0;
    stack[top++] = 0;
    seen[0] = 1;
    n = 1;
    while (top > 0)
    {
        x = stack[--top];
        for (k = start[x]; k < start[x + 1]; k++)
        {
            y = adj[k];
            if (!seen[y]) { seen[y] = 1; n++; stack[top++] = y; }
        }
    }
    i = (n == G->nv);
    flint_free(stack);
    flint_free(seen);
    flint_free(adj);
    flint_free(start);
    return (int) i;
}
