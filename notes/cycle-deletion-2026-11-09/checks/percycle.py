r"""Per-cycle weights: P = sum_C prod_{c in C} w_c mu_{4, Y\V(C)}; test real-rootedness for w_c in {-1, 5/4} corners and random interior."""
import networkx as nx, sys, random
from fractions import Fraction
from multiprocessing import Pool
from sp4 import *
from flint import fmpz_poly

def cycles_list(adjmask):
    """all simple cycles as vertex masks (with repetition for different cycles on same vertex set)."""
    cnt = cycle_counts(adjmask)
    out = []
    for m, c in enumerate(cnt):
        out += [m] * c
    return out

def P_weighted(adjmask, cyc, wts):
    """wts: list of Fractions per cycle. returns fmpz_poly in y (scaled)."""
    n = len(adjmask); E = sum(bin(a).count('1') for a in adjmask) // 2
    full = (1 << n) - 1
    den = 1
    for w in wts: den = den * w.denominator // __import__('math').gcd(den, w.denominator)
    memo = {}
    def mu(mask):
        if mask not in memo:
            m, edges = induced(adjmask, full ^ mask)
            c = mu4_scaled(m, edges)
            sc = SCALE ** (E - len(edges))
            co = [0] * (2 * m + 1)
            for s, cs in enumerate(c): co[2 * m - s] = (-1) ** s * cs * sc
            memo[mask] = fmpz_poly(co)
        return memo[mask]
    # accumulate weight per removed mask
    acc = {}
    def rec(start, mask, wt):
        acc[mask] = acc.get(mask, 0) + wt
        for j in range(start, len(cyc)):
            if not mask & cyc[j]: rec(j + 1, mask | cyc[j], wt * wts[j])
    rec(0, 0, Fraction(1))
    L = 1
    for v in acc.values(): L = L * v.denominator // __import__('math').gcd(L, v.denominator)
    p = fmpz_poly([0])
    for mask, v in acc.items():
        if v: p = p + mu(mask) * int(v * L)
    return p

def work(args):
    i, n, edges, seed = args
    rnd = random.Random(seed)
    A = adj_from_edges(n, edges)
    cyc = cycles_list(A)
    bad = []
    lo, hi = Fraction(-1), Fraction(5, 4)
    trials = []
    if len(cyc) <= 6:
        for bits in range(1 << len(cyc)):
            trials.append([hi if bits >> j & 1 else lo for j in range(len(cyc))])
    else:
        for _ in range(40):
            trials.append([rnd.choice([lo, hi]) for _ in cyc])
    for _ in range(10):
        trials.append([lo + (hi - lo) * Fraction(rnd.randint(0, 64), 64) for _ in cyc])
    for w in trials:
        if not real_rooted(P_weighted(A, cyc, w)):
            bad.append([str(x) for x in w]); break
    return i, n, edges, len(cyc), bad

if __name__ == '__main__':
    nmax = int(sys.argv[1])
    cases = []
    for i, G in enumerate(nx.graph_atlas_g()):
        if 3 <= len(G) <= nmax and nx.is_connected(G) and G.number_of_edges() > len(G):
            cases.append((i, len(G), list(G.edges()), i))
    with Pool(48) as p:
        res = p.map(work, cases, chunksize=2)
    bad = [r for r in res if r[4]]
    print('graphs', len(res), 'with a failing weight vector:', len(bad))
    for r in bad[:15]: print(r)
