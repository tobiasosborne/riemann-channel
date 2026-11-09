r"""Cycle-deletion polynomial  P_w(Y) = sum_C w^{|C|} mu_{4, Y \\ V(C)}  (w = 1 is the conformal Sp4 average).

Everything is exact (python-flint integers).  Polynomials are kept in y = x^2:
mu_{4,Y}(x) has only the powers x^{4n - 2s}, so P_w(x) = g_w(x^2) with deg g_w = 2n,
and P_w is real-rooted iff every root of g_w is real and >= 0.

Graphs: n vertices 0..n-1, adjacency as a list of bitmasks.
"""
from flint import fmpz_poly, fmpz, fmpq
from functools import lru_cache

import math
def set_d(d):
    global D, FALL, EDGE, SCALE
    D = d
    FALL = [math.perm(d, s) for s in range(d + 1)]            # (d)_s
    SCALE = math.factorial(d) ** 2
    EDGE = [SCALE // (math.factorial(k) * math.perm(d, k)) for k in range(d + 1)]
set_d(4)


def mu4_scaled(n, edges):
    """Return list c[s] (python ints) with
       SCALE^{|E|} * mu_{d,Y}(x) = sum_s (-1)^s c[s] x^{dn-2s}."""
    if n == 0:
        return [1]
    # order edges so that vertices close early: process vertices in a greedy min-degree order
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v); adj[v].add(u)
    remaining = {v: set(adj[v]) for v in range(n)}
    order = []
    left = set(range(n))
    while left:
        v = min(left, key=lambda a: (len(remaining[a]), a))
        order.append(v); left.discard(v)
        for u in remaining[v]:
            remaining[u].discard(v)
    done = set()
    seq = []                       # ('e',u,v) or ('close',v)
    for v in order:
        for u in adj[v]:
            if u not in done:
                seq.append(('e', v, u))
        done.add(v)
        seq.append(('c', v))
    states = {(0,) * n: fmpz_poly([1])}
    tpow = [fmpz_poly([0] * k + [EDGE[k]]) for k in range(D + 1)]
    for op in seq:
        new = {}
        if op[0] == 'e':
            _, u, v = op
            for st, p in states.items():
                su, sv = st[u], st[v]
                kmax = D - max(su, sv)
                for k in range(kmax + 1):
                    if k == 0:
                        ns = st; q = p * SCALE
                    else:
                        l = list(st); l[u] = su + k; l[v] = sv + k; ns = tuple(l)
                        q = p * tpow[k]
                    if ns in new:
                        new[ns] = new[ns] + q
                    else:
                        new[ns] = q
        else:
            v = op[1]
            for st, p in states.items():
                f = FALL[st[v]]
                l = list(st); l[v] = 0; ns = tuple(l)
                q = p * f
                if ns in new:
                    new[ns] = new[ns] + q
                else:
                    new[ns] = q
        states = new
    (st, p), = states.items()
    return [int(c) for c in p.coeffs()]


def induced(adjmask, mask):
    """relabelled (n, edges) of the induced subgraph on vertex bitmask."""
    vs = [v for v in range(len(adjmask)) if mask >> v & 1]
    idx = {v: i for i, v in enumerate(vs)}
    edges = [(idx[u], idx[v]) for u in vs for v in vs if u < v and adjmask[u] >> v & 1]
    return len(vs), edges


def cycle_counts(adjmask):
    """cnt[mask] = number of (unoriented) simple cycles with vertex set exactly mask."""
    n = len(adjmask)
    cnt = [0] * (1 << n)
    # DP over paths starting at the lowest vertex of the mask
    for s in range(n):
        # paths starting at s using only vertices > s
        allowed = ((1 << n) - 1) & ~((1 << (s + 1)) - 1)
        dp = {(1 << s, s): 1}
        frontier = [(1 << s, s)]
        # BFS by popcount
        layer = {(1 << s, s): 1}
        while layer:
            nxt = {}
            for (m, v), c in layer.items():
                if bin(m).count('1') >= 3 and adjmask[v] >> s & 1:
                    cnt[m] += c
                nb = adjmask[v] & allowed & ~m
                while nb:
                    b = nb & -nb; nb ^= b
                    key = (m | b, b.bit_length() - 1)
                    nxt[key] = nxt.get(key, 0) + c
            layer = nxt
    return [c // 2 for c in cnt]


def collections(adjmask):
    """N[mask] = list a[j] = number of collections of j vertex-disjoint cycles with union of vertex sets = mask."""
    n = len(adjmask)
    cnt = cycle_counts(adjmask)
    N = [None] * (1 << n)
    N[0] = [1]
    for mask in range(1, 1 << n):
        low = mask & -mask
        acc = {}
        sub = mask
        while sub:
            if sub & low and cnt[sub]:
                rest = N[mask ^ sub]
                if rest:
                    for j, a in enumerate(rest):
                        if a:
                            acc[j + 1] = acc.get(j + 1, 0) + cnt[sub] * a
            sub = (sub - 1) & mask
        if acc:
            m = max(acc)
            N[mask] = [acc.get(j, 0) for j in range(m + 1)]
        else:
            N[mask] = []
    return N


def T_polys(adjmask):
    """Return list T[j] = fmpz_poly in y with  576^{|E|} P_w = sum_j w^j T[j](y),  deg T[0] = 2n."""
    n = len(adjmask)
    E = sum(bin(a).count('1') for a in adjmask) // 2
    N = collections(adjmask)
    full = (1 << n) - 1
    T = {}
    for mask in range(1 << n):
        if not N[mask]:
            continue
        m, edges = induced(adjmask, full ^ mask)
        c = mu4_scaled(m, edges)
        sc = SCALE ** (E - len(edges))
        # mu in y: sum_s (-1)^s c[s] y^{2m-s}
        coeffs = [0] * (D * m + 1)
        for s, cs in enumerate(c):
            coeffs[D * m - 2 * s] = (-1) ** s * cs * sc
        p = fmpz_poly(coeffs)
        for j, a in enumerate(N[mask]):
            if a:
                T[j] = T.get(j, fmpz_poly([0])) + p * a
    return [T.get(j, fmpz_poly([0])) for j in range(max(T) + 1)]


def P_w(T, w):
    """g_w(y) as fmpz_poly up to positive scaling; w a Fraction-like (num, den) or int."""
    if isinstance(w, int):
        num, den = w, 1
    else:
        num, den = w
    J = len(T) - 1
    p = fmpz_poly([0])
    for j, t in enumerate(T):
        p = p + t * (num ** j * den ** (J - j))
    return p


def real_rooted(g):
    """True iff all roots of g(x) are real. Rigorous."""
    deg = g.degree()
    # strip y^k
    co = [int(c) for c in g.coeffs()]
    k = 0
    while co[k] == 0:
        k += 1
    h = fmpz_poly(co[k:])
    if h.degree() == 0:
        return True
    good = 0
    for r, mult in h.complex_roots():
        if r.imag == 0:
            good += mult
    return good == h.degree()


def adj_from_edges(n, edges):
    a = [0] * n
    for u, v in edges:
        a[u] |= 1 << v; a[v] |= 1 << u
    return a


def threshold(T, lo=(0, 1), hi=(4, 1), iters=40):
    """sup of w >= 0 such that P_w is real-rooted on [0,w] (bisection, assumes an interval)."""
    from fractions import Fraction
    a, b = Fraction(*lo), Fraction(*hi)
    if real_rooted(P_w(T, (b.numerator, b.denominator))):
        return float('inf')
    for _ in range(iters):
        m = (a + b) / 2
        if real_rooted(P_w(T, (m.numerator, m.denominator))):
            a = m
        else:
            b = m
    return float(a)


if __name__ == '__main__':
    import networkx as nx, sys
    from fractions import Fraction
    from multiprocessing import Pool
    def lower_threshold(T, iters=30):
        a, b = Fraction(0), Fraction(-8)
        if real_rooted(P_w(T, (-8, 1))): return float('-inf')
        for _ in range(iters):
            m = (a + b) / 2
            if real_rooted(P_w(T, (m.numerator, m.denominator))): a = m
            else: b = m
        return float(a)
    def work(args):
        d, i, n, edges = args
        set_d(d)
        T = T_polys(adj_from_edges(n, edges))
        return i, n, edges, threshold(T, hi=(8, 1), iters=30), lower_threshold(T)
    nmax = int(sys.argv[2])
    cases = []
    for i, G in enumerate(nx.graph_atlas_g()):
        if 3 <= len(G) <= nmax and nx.is_connected(G) and G.number_of_edges() >= len(G):
            cases.append((int(sys.argv[1]), i, len(G), list(G.edges())))
    with Pool(48) as p:
        res = p.map(work, cases, chunksize=2)
    uni = [r for r in res if len(r[2]) == r[1]]
    print('d =', sys.argv[1], ' unicyclic window: [%.6f, %.6f] .. [%.6f, %.6f]' % (min(r[4] for r in uni), min(r[3] for r in uni), max(r[4] for r in uni), max(r[3] for r in uni)))
    print('all graphs: min upper %.6f   max lower %.6f' % (min(r[3] for r in res), max(r[4] for r in res)))
    rs = sorted(res, key=lambda r: r[3])
    for r in rs[:6]: print('  up', r[0], 'n=%d E=%d' % (r[1], len(r[2])), 'w*=%.6f lo=%.6f' % (r[3], r[4]), r[2])
    rs = sorted(res, key=lambda r: -r[4])
    for r in rs[:6]: print('  lo', r[0], 'n=%d E=%d' % (r[1], len(r[2])), 'w*=%.6f lo=%.6f' % (r[3], r[4]), r[2])
