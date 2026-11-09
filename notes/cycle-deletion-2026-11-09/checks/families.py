r"""Thresholds of P_w = sum_C w^{|C|} mu_{d,Y\\V(C)} on sparse non-cactus families (d from argv)."""
import networkx as nx, sys, itertools
from fractions import Fraction
from multiprocessing import Pool
import cdp
from cdp import *
from flint import fmpz_poly

def T_sparse(adjmask):
    """T[j] via explicit cycle enumeration (good for sparse graphs with few cycles)."""
    n = len(adjmask); E = sum(bin(a).count('1') for a in adjmask) // 2
    full = (1 << n) - 1
    cnt = cycle_counts(adjmask)
    cyc = [m for m, c in enumerate(cnt) for _ in range(c)]
    acc = {}
    def rec(start, mask, j):
        acc[(mask, j)] = acc.get((mask, j), 0) + 1
        for i in range(start, len(cyc)):
            if not mask & cyc[i]: rec(i + 1, mask | cyc[i], j + 1)
    rec(0, 0, 0)
    memo = {}
    T = {}
    for (mask, j), a in acc.items():
        if mask not in memo:
            m, edges = induced(adjmask, full ^ mask)
            c = mu4_scaled(m, edges)
            sc = cdp.SCALE ** (E - len(edges))
            co = [0] * (cdp.D * m + 1)
            for s, cs in enumerate(c): co[cdp.D * m - 2 * s] = (-1) ** s * cs * sc
            memo[mask] = fmpz_poly(co)
        T[j] = T.get(j, fmpz_poly([0])) + memo[mask] * a
    return [T.get(j, fmpz_poly([0])) for j in range(max(T) + 1)], len(cyc)

def thr(T, sign, big=16, iters=36):
    a, b = Fraction(0), Fraction(sign * big)
    if real_rooted(P_w(T, (b.numerator, b.denominator))): return float('inf') * sign
    for _ in range(iters):
        m = (a + b) / 2
        if real_rooted(P_w(T, (m.numerator, m.denominator))): a = m
        else: b = m
    return float(a)

def work(args):
    d, name, n, edges = args
    cdp.set_d(d)
    T, nc = T_sparse(adj_from_edges(n, edges))
    return name, n, len(edges), nc, thr(T, -1), thr(T, 1)

def theta(a, b, c):
    G = nx.Graph(); nxt = 2
    for L in (a, b, c):
        prev = 0
        for _ in range(L - 1):
            G.add_edge(prev, nxt); prev = nxt; nxt += 1
        G.add_edge(prev, 1)
    return G

if __name__ == '__main__':
    d = int(sys.argv[1]); nmax = int(sys.argv[2])
    cases = []
    for a in range(1, 6):
        for b in range(max(a, 2), 8):
            for c in range(b, 10):
                if a + b + c - 1 <= nmax: cases.append(('theta(%d,%d,%d)' % (a, b, c), theta(a, b, c)))
    for k in range(3, 7):
        if 2 * k <= nmax:
            cases.append(('ladder%d' % k, nx.ladder_graph(k)))
            cases.append(('prism%d' % k, nx.circular_ladder_graph(k)))
    for k in range(4, 9):
        if k + 1 <= nmax: cases.append(('wheel%d' % k, nx.wheel_graph(k + 1)))
    for m in range(3, 8):
        if m + 2 <= nmax: cases.append(('K2,%d' % m, nx.complete_bipartite_graph(2, m)))
    for k in range(2, 6):
        if 2 * k + 1 <= nmax: cases.append(('fan/book: %d triangles on an edge' % k, nx.complete_multipartite_graph(1, 1, k)))
    # subdivided K4: every edge subdivided s times
    for s in (1, 2):
        G = nx.complete_graph(4); H = nx.Graph(); nxt = 4
        for u, v in G.edges():
            prev = u
            for _ in range(s):
                H.add_edge(prev, nxt); prev = nxt; nxt += 1
            H.add_edge(prev, v)
        if len(H) <= nmax + 2: cases.append(('K4 subdivided x%d' % s, H))
    cases.append(('Petersen', nx.petersen_graph())); cases.append(('cube', nx.hypercube_graph(3))); cases.append(('K33', nx.complete_bipartite_graph(3, 3)))
    jobs = []
    for name, G in cases:
        G = nx.convert_node_labels_to_integers(G)
        jobs.append((d, name, len(G), list(G.edges())))
    with Pool(56) as p:
        res = p.map(work, jobs, chunksize=1)
    print('d =', d)
    res.sort(key=lambda r: r[5])
    print('--- smallest upper thresholds'); [print('  %-34s n=%2d E=%2d cycles=%4d  window [%.6f, %.6f]' % r) for r in res[:14]]
    res.sort(key=lambda r: -r[4])
    print('--- largest lower thresholds'); [print('  %-34s n=%2d E=%2d cycles=%4d  window [%.6f, %.6f]' % r) for r in res[:14]]
