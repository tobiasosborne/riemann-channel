"""Random sparse connected graphs (cycle rank 2..6, not cacti preferred): is P_w real-rooted at the endpoints of the cycle window and for random per-cycle weights in the window?"""
import networkx as nx, sys, random
from fractions import Fraction
from multiprocessing import Pool
import cdp
from cdp import *
from flint import fmpz_poly
WIN = {3: (Fraction(-1088, 1000), Fraction(1088, 1000)), 4: (Fraction(-1), Fraction(5, 4)), 5: (Fraction(-1036, 1000), Fraction(1036, 1000))}

def P_weighted(adjmask, cyc, wts):
    n = len(adjmask); E = sum(bin(a).count('1') for a in adjmask) // 2
    full = (1 << n) - 1
    memo = {}
    def mu(mask):
        if mask not in memo:
            m, edges = induced(adjmask, full ^ mask)
            c = mu4_scaled(m, edges)
            sc = cdp.SCALE ** (E - len(edges))
            co = [0] * (cdp.D * m + 1)
            for s, cs in enumerate(c): co[cdp.D * m - 2 * s] = (-1) ** s * cs * sc
            memo[mask] = fmpz_poly(co)
        return memo[mask]
    out = []
    for w in wts:
        acc = {}
        def rec(start, mask, wt):
            acc[mask] = acc.get(mask, 0) + wt
            for j in range(start, len(cyc)):
                if not mask & cyc[j]: rec(j + 1, mask | cyc[j], wt * w[j])
        rec(0, 0, Fraction(1))
        L = 1
        for v in acc.values(): L = L * v.denominator // __import__('math').gcd(L, v.denominator)
        p = fmpz_poly([0])
        for mask, v in acc.items():
            if v: p = p + mu(mask) * int(v * L)
        out.append(p)
    return out

def work(args):
    d, n, extra, seed = args
    cdp.set_d(d)
    rnd = random.Random(seed)
    while True:
        T = nx.random_labeled_tree(n, seed=rnd.randint(0, 10 ** 9))
        G = nx.Graph(T.edges())
        non = [(u, v) for u in range(n) for v in range(u + 1, n) if not G.has_edge(u, v)]
        G.add_edges_from(rnd.sample(non, extra))
        break
    A = adj_from_edges(n, list(G.edges()))
    cnt = cycle_counts(A)
    cyc = [m for m, c in enumerate(cnt) for _ in range(c)]
    if len(cyc) > 400: return None
    lo, hi = WIN[d]
    wts = [[lo] * len(cyc), [hi] * len(cyc), [Fraction(1)] * len(cyc)]
    for _ in range(3): wts.append([rnd.choice([lo, hi]) for _ in cyc])
    for _ in range(2): wts.append([lo + (hi - lo) * Fraction(rnd.randint(0, 32), 32) for _ in cyc])
    polys = P_weighted(A, cyc, wts)
    bad = [i for i, p in enumerate(polys) if not real_rooted(p)]
    return (n, extra, len(cyc), sorted(G.edges()), bad)

if __name__ == '__main__':
    d = int(sys.argv[1]); N = int(sys.argv[2])
    jobs = []
    seed = 0
    for n in (8, 9, 10, 11):
        for extra in (2, 3, 4, 5):
            if d == 5 and n > 9: continue
            for _ in range(N):
                seed += 1; jobs.append((d, n, extra, seed))
    with Pool(60) as p:
        res = [r for r in p.imap_unordered(work, jobs, chunksize=4) if r]
    bad = [r for r in res if r[4]]
    print('d=%d graphs tested %d (8 weight vectors each: all-lo, all-hi, all-1, 3 random corners, 2 random interior); failures: %d' % (d, len(res), len(bad)))
    for r in bad[:10]: print('  FAIL', r)
    from collections import Counter
    print('  by (n, cycle rank):', sorted(Counter((r[0], r[1]) for r in res).items()))
