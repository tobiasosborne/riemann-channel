r"""Cycle-deletion polynomial  P_w(Y) = sum_C w^{|C|} mu_{4, Y \\ V(C)}  (w = 1 is the conformal Sp4 average).

Everything is exact (python-flint integers).  Polynomials are kept in y = x^2:
mu_{4,Y}(x) has only the powers x^{4n - 2s}, so P_w(x) = g_w(x^2) with deg g_w = 2n,
and P_w is real-rooted iff every root of g_w is real and >= 0.

Graphs: n vertices 0..n-1, adjacency as a list of bitmasks.
"""
from flint import fmpz_poly, fmpz, fmpq
from functools import lru_cache

D = 4
FALL = [1, 4, 12, 24, 24]           # (4)_s
EDGE = [576, 144, 24, 4, 1]         # 576 / (k! (4)_k)
SCALE = 576


def mu4_scaled(n, edges):
    """Return list c[s] (python ints) with
       576^{|E|} * mu_{4,Y}(x) = sum_s (-1)^s c[s] x^{4n-2s}."""
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
        coeffs = [0] * (2 * m + 1)
        for s, cs in enumerate(c):
            coeffs[2 * m - s] = (-1) ** s * cs * sc
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
    """True iff all roots of g(y) are real and >= 0 (so g(x^2) is real-rooted). Rigorous."""
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
        if r.imag == 0 and r.real > 0:
            good += mult
        elif r.imag == 0 and not (r.real < 0):
            raise RuntimeError('undecided sign')
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
    import networkx as nx
    def A(G):
        G = nx.convert_node_labels_to_integers(G)
        return adj_from_edges(len(G), list(G.edges()))
    # checks against the lane's printed polynomials
    T = T_polys(A(nx.complete_graph(4)))
    E = 6
    g = P_w(T, 1)
    print('K4 Phi * 576^6 in y:', [fmpq(int(c), 576 ** E) for c in g.coeffs()][::-1])
    T = T_polys(A(nx.cycle_graph(3)))
    print('C3:', [fmpq(int(c), 576 ** 3) for c in P_w(T, 1).coeffs()][::-1])
    for name, G in [('C3', nx.cycle_graph(3)), ('C4', nx.cycle_graph(4)), ('C5', nx.cycle_graph(5)), ('K4', nx.complete_graph(4)),
                    ('K5', nx.complete_graph(5)), ('K33', nx.complete_bipartite_graph(3, 3)), ('K6', nx.complete_graph(6))]:
        T = T_polys(A(G))
        print(name, 'real-rooted at w=1:', real_rooted(P_w(T, 1)), ' threshold w* =', threshold(T))
