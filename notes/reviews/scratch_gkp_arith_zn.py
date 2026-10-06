"""REFUTE scratch (zn-flux.md), written from the statements only.
(a) similitude M^dag Omega M = q Omega (and failure of plain transpose); (b) restriction of scalars to Z:
    integrality, alternation, similitude, charpoly = P^2 (N>=3) and NOT a square for N=2; Weil form PD iff Galois-Ramanujan;
(c) spec(rho) = spec(rho-bar); (d) ordinariness <=> Norm(det A_rho) prime to p, against the integral charpoly;
(e) census; (f) Theorem 4.1 for N=2..7 by exact enumeration; (g) closed NB walks with class in N H_1 (K4, N=3)."""
import itertools, math, numpy as np, networkx as nx, sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy import symbols, Poly
x = symbols('x')

def setup(G):
    G = nx.convert_node_labels_to_integers(G)
    T = nx.bfs_tree(G, 0).to_undirected()
    cot = [e for e in G.edges() if not T.has_edge(*e)]
    return G, cot
def Aphi(G, cot, phi, N):
    n = G.number_of_nodes(); A = np.zeros((n, n), complex)
    z = np.exp(2j*np.pi/N)
    val = {e: v for e, v in zip(cot, phi)}
    for (u, v) in G.edges():
        k = val.get((u, v), 0)
        A[u, v] += z**k; A[v, u] += z**(-k)
    return A
def units(N): return [a for a in range(1, N) if math.gcd(a, N) == 1]
graphs = {'K4': nx.complete_graph(4), 'cube': nx.hypercube_graph(3), 'Petersen': nx.petersen_graph()}
q = 2; band = 2*math.sqrt(q)
rng = np.random.default_rng(1)
# (a) similitude
G, cot = setup(graphs['K4'])
A = Aphi(G, cot, [1, 2, 4], 5); n = 4
M = np.block([[np.zeros((n, n)), -np.eye(n)], [q*np.eye(n), A]])
Om = np.block([[np.zeros((n, n)), np.eye(n)], [-np.eye(n), np.zeros((n, n))]])
print('(a) |M^dag Om M - q Om| =', np.abs(M.conj().T@Om@M - q*Om).max(), '  plain transpose:', np.abs(M.T@Om@M - q*Om).max())
# (b) restriction of scalars, exact, for K4 with N=5 and N=2, cube N=3
def restrict(G, cot, phi, N):
    """integer matrices of M and Omega_Z on O^{2n}, O = Z[zeta_N] with power basis 1..zeta^{d-1}."""
    Phi = sp.cyclotomic_poly(N, x); d = sp.degree(Phi, x)
    t = symbols('t')
    n = G.number_of_nodes()
    # multiplication-by-zeta^k matrices in power basis
    def mulmat(k):
        cols = []
        for j in range(d):
            r = Poly(sp.rem(x**(j + k % N), Phi, x), x).all_coeffs()[::-1]
            r = r + [0]*(d - len(r)); cols.append(r)
        return sp.Matrix(cols).T
    Z = {k: mulmat(k) for k in range(N)}
    I = sp.eye(d); O = sp.zeros(d)
    val = {e: v for e, v in zip(cot, phi)}
    Ab = [[O for _ in range(n)] for _ in range(n)]
    for (u, v) in G.edges():
        k = val.get((u, v), 0)
        Ab[u][v] = Ab[u][v] + Z[k % N]; Ab[v][u] = Ab[v][u] + Z[(-k) % N]
    Az = sp.Matrix(sp.BlockMatrix(Ab).as_explicit())
    MZ = sp.Matrix(sp.BlockMatrix([[sp.zeros(n*d), -sp.eye(n*d)], [q*sp.eye(n*d), Az]]).as_explicit())
    # trace form T_ij = Tr(conj(zeta^i) zeta^j) = Tr(zeta^{j-i})
    def tr(k):
        return int(sum(sp.re(sp.exp(2*sp.pi*sp.I*k*a/N)).evalf(30) for a in units(N)).round())
    Tm = sp.Matrix(d, d, lambda i, j: tr(j - i))
    Omz = sp.Matrix(sp.BlockMatrix([[sp.zeros(n*d), sp.kronecker_product(sp.eye(n), Tm)], [-sp.kronecker_product(sp.eye(n), Tm), sp.zeros(n*d)]]).as_explicit())
    return MZ, Omz, Az, d, Tm
for name, N, phi in [('K4', 5, [1, 2, 4]), ('K4', 2, [1, 0, 0]), ('cube', 3, [1, 2, 0, 1, 1]), ('K4', 4, [1, 3, 2])]:
    G, cot = setup(graphs[name])
    MZ, Omz, Az, d, Tm = restrict(G, cot, phi, N)
    cp = MZ.charpoly(x).as_expr()
    sqf = sp.sqf_list(cp)
    issq = all(m % 2 == 0 for f, m in sqf[1])
    gr = all(np.abs(np.linalg.eigvalsh(Aphi(G, cot, [a*p for p in phi], N))).max() < band for a in units(N))
    W = (Omz*(MZ - q*MZ.inv()))/2
    Wn = np.array(W.evalf(), dtype=float)
    pd = np.linalg.eigvalsh((Wn + Wn.T)/2).min() > 1e-9
    print(f'(b) {name} N={N} phi={phi}: Omega_Z antisym {Omz == -Omz.T}, M^T Om M = q Om {(MZ.T*Omz*MZ - q*Omz).is_zero_matrix}, '
          f'V integral {all(v.is_integer for v in q*MZ.inv())}, W symmetric {W == W.T}, charpoly a square: {issq}, '
          f'Galois-Ramanujan {gr}, Weil PD {pd}, det T = {Tm.det()}, SNF T = {smith_normal_form(Tm, domain=sp.ZZ).diagonal()}')
# (c) rho vs rho-bar spectra
mx = 0
for name in graphs:
    G, cot = setup(graphs[name])
    for N in [3, 5, 7, 8]:
        phi = rng.integers(0, N, len(cot))
        e1 = np.linalg.eigvalsh(Aphi(G, cot, phi, N)); e2 = np.linalg.eigvalsh(Aphi(G, cot, -phi, N))
        mx = max(mx, np.abs(e1 - e2).max())
print('(c) max |spec(rho) - spec(rho-bar)| over random fluxes:', mx)
# (d)+(e) census and ordinariness
def census(name, N, check_ord_exact=0):
    G, cot = setup(graphs[name]); g = len(cot)
    ram = gr = ordn = 0; onband = 0; mism = 0; checked = 0
    spec_ok = {}
    for phi in itertools.product(range(N), repeat=g):
        phi = np.array(phi)
        ev = {a: np.linalg.eigvalsh(Aphi(G, cot, (a*phi) % N, N)) for a in units(N)}
        r1 = np.abs(ev[1]).max() < band
        ram += r1
        onband += any(np.min(np.abs(np.abs(e) - band)) < 1e-9 for e in ev.values())
        if all(np.abs(e).max() < band for e in ev.values()):
            gr += 1
            nrm = round(np.prod([np.prod(e) for e in ev.values()]))
            o = (nrm % q != 0); ordn += o
            if checked < check_ord_exact:
                MZ, Omz, Az, d, Tm = restrict(G, cot, list(phi), N)
                cp = Poly(MZ.charpoly(x).as_expr(), x).all_coeffs()
                mid = cp[len(cp)//2]
                mism += ((mid % q != 0) != o); checked += 1
    return N**g, ram, gr, ordn, onband, mism, checked
for name, N in [('K4', 3), ('K4', 4), ('K4', 5), ('K4', 6), ('cube', 3), ('cube', 4), ('Petersen', 3), ('Petersen', 4)]:
    c = census(name, N, check_ord_exact=6 if name == 'K4' else 0)
    print(f'(e) {name} N={N}: classes {c[0]}, Ramanujan {c[1]}, Galois-Ramanujan {c[2]}, ordinary {c[3]}, near band edge {c[4]}; '
          f'ordinariness rule vs exact middle coefficient: {c[5]} mismatches in {c[6]}')
# K4 N=3 spectra
G, cot = setup(graphs['K4']); from collections import Counter
cnt = Counter()
for phi in itertools.product(range(3), repeat=3):
    cp = np.poly(Aphi(G, cot, phi, 3)); cnt[tuple(np.round(cp.real, 6))] += 1
print('(e) K4 N=3 spectra (charpoly coeffs: count):', dict(cnt))
# (f) Theorem 4.1, exact averages
y = symbols('y')
def matching_poly(G):
    n = G.number_of_nodes(); E = list(G.edges()); tot = 0
    for k in range(n//2 + 1):
        c = sum(1 for S in itertools.combinations(E, k) if len({v for e in S for v in e}) == 2*k)
        tot += (-1)**k*c*x**(n - 2*k)
    return sp.expand(tot)
for name, Ns in [('K4', range(2, 8)), ('cube', range(2, 5)), ('Petersen', [2, 3])]:
    G, cot = setup(graphs[name]); g = len(cot); mu = matching_poly(G)
    mcoef = np.array(Poly(mu, x).all_coeffs(), float)
    res = []
    for N in Ns:
        acc = np.zeros(G.number_of_nodes() + 1, complex)
        for phi in itertools.product(range(N), repeat=g):
            acc += np.poly(Aphi(G, cot, phi, N))
        acc /= N**g
        res.append((N, float(np.abs(acc - mcoef).max())))
    print(f'(f) {name}: matching poly {mu}; max coeff error of N-torsion average:', res)
# (g) walks: closed non-backtracking walks of length 9 in K4 with class in 3 H_1
G, cot = setup(graphs['K4'])
dirE = [(u, v) for (u, v) in G.edges()] + [(v, u) for (u, v) in G.edges()]
idx = {e: i for i, e in enumerate(dirE)}
def cls(e):
    c = np.zeros(len(cot), int)
    for i, (a, b) in enumerate(cot):
        if e == (a, b): c[i] = 1
        if e == (b, a): c[i] = -1
    return c
tot = {}; sel = {}
for k in range(3, 10):
    t = s = 0
    for start in dirE:
        stack = [(start, [start])]
        while stack:
            e, path = stack.pop()
            if len(path) == k:
                if path[-1][1] == path[0][0] and path[0] != (path[-1][1], path[-1][0]):
                    t += 1
                    c = sum(cls(f) for f in path)
                    if all(v % 3 == 0 for v in c): s += 1
                continue
            for f in dirE:
                if f[0] == e[1] and f != (e[1], e[0]): stack.append((f, path + [f]))
    tot[k] = t; sel[k] = s
print('(g) K4 closed NB walks (Tr B^k) and those with class in 3H_1:', {k: (tot[k], sel[k]) for k in tot})
