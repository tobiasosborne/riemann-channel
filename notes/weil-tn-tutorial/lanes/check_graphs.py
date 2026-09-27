#!/usr/bin/env python3
"""Independent check for demos-graphs.js (worker G, 2026-09-26).

For each graph of the station: Tr B^l (l <= 24) by matrix powers of the Hashimoto matrix B,
the same from Ihara-Bass (sum over adjacency eigenvalues a of the roots of mu^2 - a mu + q, plus
(|E|-|V|) copies of +1 and -1), the rescaled trace sequence
    nu_l = q^{-l/2} (Tr B^l - trivial_l),
    trivial_l = q^l + 1 + (|E|-|V|)(1 + (-1)^l)  [+ (-q)^l + (-1)^l if bipartite],
Huang's h_k = nu_0 - nu_k (and the literal Huang formula with his N_k for non-bipartite graphs),
and the minimal eigenvalue of the (K+1) x (K+1) Toeplitz matrix (nu_{|j-k|})_{j,k=0..K}.
Conventions: B[e][f] = 1 iff head(e) = tail(f) and f != reverse(e) (def:hashimoto-operator).
"""
import numpy as np
from decimal import Decimal, ROUND_HALF_UP

def F(x, d=4):
    """fixed-point like JS toFixed (exact binary ties round away from zero), as WT.fmtF prints"""
    if abs(x) < 0.5 * 10 ** -d: x = 0.0
    return str(Decimal(float(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP))

def cycle_edges(n, off=0):
    return [(off + i, off + (i + 1) % n) for i in range(n)]

def prism(n):
    return 2 * n, cycle_edges(n) + cycle_edges(n, n) + [(i, i + n) for i in range(n)]

def complete(n):
    return n, [(i, j) for i in range(n) for j in range(i + 1, n)]

def circulant(n, S):
    E = set()
    for i in range(n):
        for s in S:
            E.add(tuple(sorted((i, (i + s) % n))))
    return n, sorted(E)

def petersen():
    return 10, cycle_edges(5) + [(5 + i, 5 + (i + 2) % 5) for i in range(5)] + [(i, i + 5) for i in range(5)]

def heawood():                      # LCF [5,-5]^7
    E = set(cycle_edges(14))
    for i in range(14):
        E.add(tuple(sorted((i, (i + (5 if i % 2 == 0 else -5)) % 14))))
    return 14, sorted(E)

def k33():
    return 6, [(i, j) for i in (0, 2, 4) for j in (1, 3, 5)]

def octahedron():
    return 6, [(i, j) for i in range(6) for j in range(i + 1, 6) if j != i + 3]

GRAPHS = [
    ('K4', 'K4', complete(4)), ('Q3', 'cube Q3', prism(4)), ('Petersen', 'Petersen', petersen()),
    ('K33', 'K3,3', k33()), ('Heawood', 'Heawood', heawood()), ('C6xK2', 'prism C6 x K2', prism(6)),
    ('C16xK2', 'prism C16 x K2', prism(16)), ('C21xK2', 'prism C21 x K2', prism(21)),
    ('K5', 'K5', complete(5)), ('Oct', 'octahedron K2,2,2', octahedron()), ('C8_12', 'circulant C8(1,2)', circulant(8, (1, 2))),
]

def analyse(n, edges, Kmax=24):
    A = np.zeros((n, n))
    for u, v in edges:
        A[u, v] = A[v, u] = 1
    deg = A.sum(1)
    assert np.all(deg == deg[0]), 'not regular'
    q = int(deg[0]) - 1
    m = len(edges)
    darts = [(u, v) for u, v in edges] + [(v, u) for u, v in edges]
    D = len(darts)
    B = np.zeros((D, D))
    for i, (u, v) in enumerate(darts):
        for j, (x, y) in enumerate(darts):
            if v == x and y != u:
                B[i, j] = 1
    # bipartite by 2-colouring (structural)
    col = [-1] * n; col[0] = 0; stack = [0]; bip = True
    while stack:
        u = stack.pop()
        for v in range(n):
            if A[u, v]:
                if col[v] < 0: col[v] = 1 - col[u]; stack.append(v)
                elif col[v] == col[u]: bip = False
    trB = [D]; P = np.eye(D)
    for l in range(1, Kmax + 1):
        P = P @ B; trB.append(int(round(np.trace(P))))
    trA = [n]; P = np.eye(n)
    for l in range(1, 13):
        P = P @ A; trA.append(int(round(np.trace(P))))
    lam = np.sort(np.linalg.eigvalsh(A))[::-1]
    # Ihara-Bass modes
    modes = []
    for a in lam:
        disc = complex(a * a - 4 * q) ** 0.5
        modes += [(a + disc) / 2, (a - disc) / 2]
    ib = [sum((mu ** l for mu in modes)).real + (m - n) * (1 + (-1) ** l) for l in range(Kmax + 1)]
    # retained: drop one a = q+1 (and one a = -(q+1) if bipartite)
    nontriv = list(lam)
    nontriv.pop(int(np.argmin(abs(np.array(nontriv) - (q + 1)))))
    if bip:
        nontriv.pop(int(np.argmin(abs(np.array(nontriv) + (q + 1)))))
    ret = []
    for a in nontriv:
        disc = complex(a * a - 4 * q) ** 0.5
        ret += [(a + disc) / 2, (a - disc) / 2]
    triv = [q ** l + 1 + (m - n) * (1 + (-1) ** l) + ((-q) ** l + (-1) ** l if bip else 0) for l in range(Kmax + 1)]
    nu = [(trB[l] - triv[l]) / q ** (l / 2) for l in range(Kmax + 1)]
    retsum_err = max(abs(sum(mu ** l for mu in ret) - nu[l] * q ** (l / 2)) / q ** (l / 2) for l in range(17))   # l <= 16, the demo's window range
    h = [nu[0] - nu[k] for k in range(Kmax + 1)]
    huang = None
    if not bip:   # Huang's literal formula with N_k = Tr B^k - (|E|-|V|)(1+(-1)^k)  (= Tr B^k - n(q-1) for even k)
        huang = [2 * (n - 1) + q ** (k / 2) + q ** (-k / 2) - q ** (-k / 2) * (trB[k] - (m - n) * (1 + (-1) ** k)) for k in range(Kmax + 1)]
    def tmin(K):
        T = np.array([[nu[abs(j - k)] for k in range(K + 1)] for j in range(K + 1)])
        return np.linalg.eigvalsh(T).min()
    a_max = max(abs(a) for a in nontriv)
    return dict(n=n, m=m, q=q, bip=bip, D=D, trB=trB, trA=trA, ib=ib, nu=nu, h=h, huang=huang, retsum_err=retsum_err,
                tmins={K: tmin(K) for K in (4, 8, 12, 16)}, a_max=a_max, ram=a_max <= 2 * np.sqrt(q) + 1e-9,
                maxmu=max(abs(mu) for mu in ret), nret=len(ret))

if __name__ == '__main__':
    for key, name, (n, edges) in GRAPHS:
        r = analyse(n, edges)
        print('=' * 90)
        print(f"{name}: |V|={r['n']} |E|={r['m']} q={r['q']} |E|-|V|={r['m']-r['n']} bipartite={r['bip']} 2|E|={r['D']}  "
              f"retained={r['nret']} nu_0={r['nu'][0]:.0f}")
        print(f"  max nontrivial |a| = {r['a_max']:.6f} vs 2 sqrt q = {2*np.sqrt(r['q']):.6f} -> {'Ramanujan' if r['ram'] else 'NOT Ramanujan'};"
              f" max retained |mu| = {r['maxmu']:.6f} vs sqrt q = {np.sqrt(r['q']):.6f}")
        print('  Tr B^l l=1..12 :', r['trB'][1:13])
        print('  Ihara-Bass     :', [int(round(x)) for x in r['ib'][1:13]],
              ' max |diff| (l<=24) =', f"{max(abs(r['ib'][l]-r['trB'][l]) for l in range(17)):.2e}")
        print('  Tr A^l l=1..12 :', r['trA'][1:13])
        print('  nu_l l=0..16   :', ' '.join(F(x) for x in r['nu'][:17]))
        print('  h_k  k=1..16   :', ' '.join(F(x) for x in r['h'][1:17]))
        kmin = int(np.argmin(r['h'][1:])) + 1
        print(f"  min_k h_k (k<=24) = {F(r['h'][kmin])} at k = {kmin}")
        if r['huang'] is not None:
            print(f"  Huang literal formula vs nu_0 - nu_k, max diff = {max(abs(a-b) for a,b in zip(r['huang'][1:], r['h'][1:])):.2e}")
        print(f"  sum of retained mu^l vs nu_l q^(l/2): max over l<=16 of |.|/q^(l/2) = {r['retsum_err']:.2e}")
        print('  Toeplitz lambda_min (size K+1):', '  '.join(f"K={K}: {F(v)}" for K, v in r['tmins'].items()))
    # the brief's figure for the prism: only {q,1} and +-1 removed (bipartite pair kept)
    n, edges = prism(16); r = analyse(n, edges)
    nu_wrong = [x + ((-r['q']) ** l + (-1) ** l) / r['q'] ** (l / 2) for l, x in enumerate(r['nu'])]
    for K in (11, 12):
        T = np.array([[nu_wrong[abs(j - k)] for k in range(K + 1)] for j in range(K + 1)])
        print(f"prism C16xK2 with {{-q,-1}} NOT removed: lambda_min at size {K+1} = {np.linalg.eigvalsh(T).min():.4f}")
