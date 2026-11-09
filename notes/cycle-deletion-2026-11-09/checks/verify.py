r"""Checks of the cactus theorem's identities.
(a) P_w(cactus) [cycle-deletion definition, d-matching DP]  ==  polarisation of R(x;tau)^d at the class polynomials F_c(t) = U_d(t/2) + w_c
(b) d = 2:  sum_C mu_{2,Y\\V(C)} = mu_{1,Y}^2 on every atlas graph up to 6 vertices
(c) windmill of triangles: P_w = (x^2-1)^{(k-1)d} [F_{w_1} boxplus_d ... boxplus_d F_{w_k}](x^3-(2k+1)x)
"""
import sympy as sp, networkx as nx, itertools, math, random
from fractions import Fraction
import cdp
from cdp import *
x, t = sp.symbols('x t')

def mu_d_sym(G, d):
    cdp.set_d(d)
    G = nx.convert_node_labels_to_integers(G)
    n = len(G); E = G.number_of_edges()
    c = mu4_scaled(n, list(G.edges()))
    return sp.Poly(sum((-1) ** s * sp.Rational(cs, cdp.SCALE ** E) * x ** (d * n - 2 * s) for s, cs in enumerate(c)), x)

def simple_cycles_sets(G):
    A = adj_from_edges(len(G), list(G.edges()))
    cnt = cycle_counts(A)
    return [m for m, c in enumerate(cnt) for _ in range(c)]

def P_def(G, d, w):
    """cycle-deletion definition with per-cycle weights w (list aligned with simple_cycles_sets)."""
    G = nx.convert_node_labels_to_integers(G)
    cyc = simple_cycles_sets(G); n = len(G)
    tot = sp.Poly(0, x)
    def rec(start, mask, wt):
        nonlocal tot
        H = G.subgraph([v for v in range(n) if not mask >> v & 1])
        tot = tot + mu_d_sym(H, d) * wt if len(H) else tot + sp.Poly(wt, x)
        for j in range(start, len(cyc)):
            if not mask & cyc[j]: rec(j + 1, mask | cyc[j], wt * w[j])
    rec(0, 0, sp.Integer(1))
    return tot

def P_pol(G, d, w):
    """polarisation of R(x;tau)^d, R = sum_S prod(-tau_c) mu_1(Y\\S), at F_c = U_d(t/2) + w_c."""
    G = nx.convert_node_labels_to_integers(G)
    cyc = simple_cycles_sets(G); n = len(G)
    taus = sp.symbols('tau0:%d' % len(cyc))
    R = sp.Integer(0)
    def rec(start, mask, mon):
        nonlocal R
        H = G.subgraph([v for v in range(n) if not mask >> v & 1])
        R += mon * (mu_d_sym(H, 1).as_expr() if len(H) else 1)
        for j in range(start, len(cyc)):
            if not mask & cyc[j]: rec(j + 1, mask | cyc[j], mon * (-taus[j]))
    rec(0, 0, sp.Integer(1))
    Rd = sp.Poly(sp.expand(R ** d), *taus)
    U = sp.Poly(sp.chebyshevu(d, t / 2), t)
    out = sp.Integer(0)
    for mon, coeff in Rd.terms():
        term = coeff
        for j, k in enumerate(mon):
            F = U + w[j]
            ek = (-1) ** k * F.coeff_monomial(t ** (d - k))      # F = sum (-1)^k e_k t^{d-k}
            term *= ek / math.comb(d, k)
        out += term
    return sp.Poly(sp.expand(out), x)

random.seed(1)
def cactus_examples():
    bow = nx.Graph([(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)])
    chain3 = nx.Graph([(0,1),(1,2),(2,0),(2,3),(3,4),(4,2),(4,5),(5,6),(6,4)])          # middle triangle attached at two different vertices
    trisq = nx.Graph([(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,6),(6,3),(5,7)])          # triangle - bridge - square, pendant
    nested = nx.Graph([(0,1),(1,2),(2,3),(3,0),(1,4),(4,5),(5,1),(3,6),(6,7),(7,3)])   # square with triangles at two vertices
    return [('bowtie', bow), ('chain of 3 triangles', chain3), ('triangle-bridge-square+pendant', trisq), ('square with two triangles', nested)]

print('(a) cactus: definition == polarisation')
for name, G in cactus_examples():
    nc = len(simple_cycles_sets(nx.convert_node_labels_to_integers(G)))
    for d in (1, 2, 3, 4):
        if d == 4 and len(G) > 8: continue
        w = [sp.Rational(random.randint(-9, 9), 7) for _ in range(nc)]
        ok = (P_def(G, d, w) - P_pol(G, d, w)).is_zero
        print('   %-34s d=%d cycles=%d weights=%s  equal: %s' % (name, d, nc, w, ok))

print('(b) d=2 identity on the atlas (<= 6 vertices)')
bad = 0; cnt = 0
for G in nx.graph_atlas_g():
    if 1 <= len(G) <= 6 and nx.is_connected(G):
        nc = len(simple_cycles_sets(G)); cnt += 1
        if not (P_def(G, 2, [1] * nc) - mu_d_sym(G, 1) ** 2).is_zero: bad += 1
print('   graphs', cnt, 'failures', bad)

print('(c) windmills: finite free convolution')
def boxplus(p, q, d):
    a = [(-1) ** i * p.coeff_monomial(t ** (d - i)) for i in range(d + 1)]
    b = [(-1) ** i * q.coeff_monomial(t ** (d - i)) for i in range(d + 1)]
    out = 0
    for k in range(d + 1):
        s = sum(sp.Rational(math.factorial(d - i) * math.factorial(d - k + i), math.factorial(d) * math.factorial(d - k)) * a[i] * b[k - i] for i in range(k + 1))
        out += (-1) ** k * s * t ** (d - k)
    return sp.Poly(out, t)
for k in (2, 3):
    for d in (2, 3, 4):
        if k == 3 and d == 4: continue
        G = nx.Graph()
        for i in range(k): G.add_edges_from([(0, 2 * i + 1), (2 * i + 1, 2 * i + 2), (2 * i + 2, 0)])
        nc = k
        # cycle order from simple_cycles_sets is by mask; triangles are symmetric so use symmetric-safe distinct weights and map by mask
        Gi = nx.convert_node_labels_to_integers(G); cyc = simple_cycles_sets(Gi)
        w = [sp.Rational(random.randint(-9, 9), 8) for _ in range(nc)]
        U = sp.Poly(sp.chebyshevu(d, t / 2), t)
        conv = U + w[0]
        for j in range(1, k): conv = boxplus(conv, U + w[j], d)
        rhs = sp.Poly(sp.expand((x ** 2 - 1) ** ((k - 1) * d) * conv.as_expr().subs(t, x ** 3 - (2 * k + 1) * x)), x)
        print('   %d triangles at a hub, d=%d: equal: %s' % (k, d, (P_def(G, d, w) - rhs).is_zero))
