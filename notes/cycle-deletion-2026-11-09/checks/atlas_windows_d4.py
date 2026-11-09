import networkx as nx, sys
from multiprocessing import Pool
from fractions import Fraction
from sp4 import *
def lower_threshold(T, iters=30):
    a, b = Fraction(0), Fraction(-4)
    if real_rooted(P_w(T, (-4, 1))): return float('-inf')
    for _ in range(iters):
        m = (a + b) / 2
        if real_rooted(P_w(T, (m.numerator, m.denominator))): a = m
        else: b = m
    return float(a)
def work(args):
    i, n, edges = args
    A = adj_from_edges(n, edges)
    T = T_polys(A)
    th = threshold(T, hi=(8,1), iters=34)
    lo = lower_threshold(T)
    return i, n, edges, th, lo
if __name__ == '__main__':
    nmax = int(sys.argv[1])
    cases = []
    for i, G in enumerate(nx.graph_atlas_g()):
        if 3 <= len(G) <= nmax and nx.is_connected(G) and G.number_of_edges() >= len(G):
            cases.append((i, len(G), list(G.edges())))
    with Pool(48) as p:
        res = p.map(work, cases, chunksize=4)
    from collections import defaultdict
    by = defaultdict(list)
    for r in res: by[len(r[2]) - r[1] + 1].append(r)
    for rank in sorted(by):
        rs = by[rank]
        ups = sorted(r[3] for r in rs); los = sorted(r[4] for r in rs)
        print('cycle rank', rank, 'graphs', len(rs), 'min w* %.6f' % ups[0], 'median %.4f' % ups[len(ups)//2], '#inf(>8)', sum(u == float('inf') for u in ups),
              '| lower: max %.6f' % los[-1], 'min %.4f' % los[0])
    print('--- smallest upper thresholds with rank >= 2')
    rs = sorted((r for r in res if len(r[2]) - r[1] + 1 >= 2), key=lambda r: r[3])
    for r in rs[:25]: print(r[0], 'n=%d E=%d' % (r[1], len(r[2])), 'w*=%.6f lo=%.6f' % (r[3], r[4]), r[2])
    print('--- largest (closest to 0) lower thresholds')
    rs = sorted(res, key=lambda r: -r[4])
    for r in rs[:15]: print(r[0], 'n=%d E=%d' % (r[1], len(r[2])), 'w*=%.6f lo=%.6f' % (r[3], r[4]), r[2])
