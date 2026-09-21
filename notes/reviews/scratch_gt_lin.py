"""REFUTE review, graded toys 2026-09-20: independent lane, script 1.

thm:diagram-linearisation (G1): the linearisation M, its determinants, traces,
kernel/Jordan structure, and the Bass/Hashimoto statement.

Nothing is imported from scripts/graded_toys.py or scripts/elliptic_cavity.py.
python3 notes/reviews/scratch_gt_lin.py
"""
import itertools
import numpy as np
import sympy as sp

PASS = [0]
FAIL = []


def check(name, cond, info=""):
    if cond:
        PASS[0] += 1
    else:
        FAIL.append((name, info))
        print("FAIL  %-58s %s" % (name, info))


def multiset_dist(a, b):
    a = list(np.asarray(a, dtype=complex))
    b = list(np.asarray(b, dtype=complex))
    if len(a) != len(b):
        return float('inf')
    worst = 0.0
    for x in a:
        j = min(range(len(b)), key=lambda k: abs(b[k] - x))
        worst = max(worst, abs(b[j] - x))
        b.pop(j)
    return worst


z = sp.symbols('z')

# ---------------------------------------------------------------- diagrams
# D2: q=2. vertices A B C D E F, S = 6,2,2,1,3,3
D2_V = ['A', 'B', 'C', 'D', 'E', 'F']
D2_S = {'A': 6, 'B': 2, 'C': 2, 'D': 1, 'E': 3, 'F': 3}
D2_E = {('A', 'B'): 2, ('B', 'C'): 2, ('C', 'D'): 1, ('D', 'E'): 1, ('D', 'F'): 1}
D2_CUSPS = [('B', 2)]          # (junction vertex, S(edge to c_1))
D2_q = 2

# D3: q=3
D3_V = ['L1p', 'L1', 'L2', 'X', 'Xp', 'Y', 'Z', 'Zp', 'Q']
D3_S = {'L1p': 48, 'L1': 12, 'L2': 6, 'X': 2, 'Xp': 8, 'Y': 6, 'Z': 12, 'Zp': 48, 'Q': 4}
D3_E = {('L1p', 'L1'): 12, ('L1', 'L2'): 6, ('L2', 'X'): 2, ('X', 'Xp'): 2,
        ('X', 'Y'): 2, ('X', 'Q'): 2, ('Y', 'Z'): 6, ('Z', 'Zp'): 12}
D3_CUSPS = [('L1', 12), ('Z', 12), ('Q', 4), ('Q', 4)]
D3_q = 3


def coord_adjacency(V, S, E):
    n = len(V)
    idx = {v: i for i, v in enumerate(V)}
    A = sp.zeros(n, n)
    for (u, v), se in E.items():
        A[idx[u], idx[v]] = sp.Rational(S[u], se)
        A[idx[v], idx[u]] = sp.Rational(S[v], se)
    return A


def degrees(V, S, E, cusps):
    d = {v: sp.Integer(0) for v in V}
    for (u, v), se in E.items():
        d[u] += sp.Rational(S[u], se)
        d[v] += sp.Rational(S[v], se)
    for (v, se) in cusps:
        d[v] += sp.Rational(S[v], se)
    return d


def cusp_C(V, S, cusps):
    """C = sum_a c_a^2 P_{v_a} with c^2 = S(v)/S(e)  (prop:stabiliser-normalisation)."""
    idx = {v: i for i, v in enumerate(V)}
    C = sp.zeros(len(V), len(V))
    for (v, se) in cusps:
        C[idx[v], idx[v]] += sp.Rational(S[v], se)
    return C


for tag, (V, S, E, cusps, q) in {'D2': (D2_V, D2_S, D2_E, D2_CUSPS, D2_q),
                                 'D3': (D3_V, D3_S, D3_E, D3_CUSPS, D3_q)}.items():
    d = degrees(V, S, E, cusps)
    check('%s core degrees = q+1' % tag, all(d[v] == q + 1 for v in V), str(d))
    # ray vertices: first cusp vertex c_1 has S(c_1) = q*S(e) (degree condition)
    for (v, se) in cusps:
        Sc1 = q * se
        # deg(c_1) = S(c1)/S(e) + S(c1)/S(c1 c2); S(c1 c2) = S(c1)
        check('%s ray c1 degree at %s' % (tag, v),
              sp.Rational(Sc1, se) + sp.Rational(Sc1, Sc1) == q + 1)
    C = cusp_C(V, S, cusps)
    for (v, se) in cusps:
        check('%s junction coupling c^2=1 at %s' % (tag, v), sp.Rational(S[v], se) == 1)

C2 = cusp_C(D2_V, D2_S, D2_CUSPS)
C3 = cusp_C(D3_V, D3_S, D3_CUSPS)
check('C_D2 = diag(0,1,0,0,0,0)', list(C2.diagonal()) == [0, 1, 0, 0, 0, 0], str(C2.diagonal()))
check('C_D3 = diag(0,1,0,0,0,0,1,0,2)',
      list(C3.diagonal()) == [0, 1, 0, 0, 0, 0, 1, 0, 2], str(C3.diagonal()))

A2 = coord_adjacency(D2_V, D2_S, D2_E)
A3 = coord_adjacency(D3_V, D3_S, D3_E)


def resonance_poly(A, C, q):
    """p(z) = det((1+z^2)I - z T_X - C) computed on the coordinate adjacency
    (similar by D^{1/2}), exactly, with u = z/sqrt q substituted as z/sqrt(q)."""
    n = A.shape[0]
    u = z / sp.sqrt(q)
    M = (1 + z ** 2) * sp.eye(n) - u * A - C
    return sp.expand(sp.simplify(sp.expand(M.det())))


p2 = sp.Poly(sp.nsimplify(resonance_poly(A2, C2, 2)), z)
p3 = sp.Poly(sp.nsimplify(resonance_poly(A3, C3, 3)), z)

p2_ref = sp.Poly(sp.expand(z ** 2 / 2 * (z ** 2 - 2) * (z ** 2 + 1) ** 2 * (2 * z ** 4 - 2 * z ** 2 + 1)), z)
p3_ref = sp.Poly(sp.expand(z ** 4 / 3 * (z - 1) ** 2 * (z + 1) ** 2 * (z ** 2 - 3) *
                           (z ** 2 + 1) ** 2 * (3 * z ** 4 + 1)), z)
check('p_2 matches thm:d2-zeta', (p2 - p2_ref).is_zero, str(p2.as_expr() - p2_ref.as_expr()))
check('p_3 matches thm:d3-channels', (p3 - p3_ref).is_zero, str(sp.expand(p3.as_expr() - p3_ref.as_expr())))


def reverse(poly, n):
    return sp.Poly(sp.expand(z ** (2 * n) * poly.as_expr().subs(z, 1 / z)), z)


pt2 = reverse(p2, 6)
pt3 = reverse(p3, 9)
check('ptilde_2(0)=1', pt2.as_expr().subs(z, 0) == 1)
check('ptilde_3(0)=1', pt3.as_expr().subs(z, 0) == 1)

# ------------------------------------------------- (a) det(z-M)=p, det(1-zM)=ptilde
def linearisation(T, C):
    n = T.shape[0]
    return sp.Matrix(sp.BlockMatrix([[T, -(sp.eye(n) - C)], [sp.eye(n), sp.zeros(n, n)]]))


# generic symbolic cores
for n in (2, 3):
    syms = {}
    T = sp.zeros(n, n)
    for i in range(n):
        for j in range(i, n):
            s = sp.Symbol('t%d%d' % (i, j))
            T[i, j] = s
            T[j, i] = s
    C = sp.diag(*[sp.Symbol('c%d' % i) for i in range(n)])
    M = linearisation(T, C)
    p = sp.expand(((1 + z ** 2) * sp.eye(n) - z * T - C).det())
    lhs = sp.expand((z * sp.eye(2 * n) - M).det())
    check('generic n=%d: det(z-M)=p' % n, sp.simplify(sp.expand(lhs - p)) == 0)
    pt = sp.expand(sp.eye(n).det() * (sp.eye(n) - z * T + z ** 2 * (sp.eye(n) - C)).det())
    lhs2 = sp.expand((sp.eye(2 * n) - z * M).det())
    check('generic n=%d: det(1-zM)=ptilde' % n, sp.simplify(sp.expand(lhs2 - pt)) == 0)
    check('generic n=%d: ptilde = z^2n p(1/z)' % n,
          sp.simplify(sp.expand(pt - z ** (2 * n) * p.subs(z, 1 / z))) == 0)
    check('generic n=%d: M-M0 = [[0,C],[0,0]]' % n,
          sp.simplify(M - linearisation(T, sp.zeros(n, n)) -
                      sp.Matrix(sp.BlockMatrix([[sp.zeros(n, n), C], [sp.zeros(n, n), sp.zeros(n, n)]]))) == sp.zeros(2 * n, 2 * n))

# on D2, D3 (numerically, coefficientwise, exactly)
for tag, (A, C, q, n, p) in {'D2': (A2, C2, 2, 6, p2), 'D3': (A3, C3, 3, 9, p3)}.items():
    T = A / sp.sqrt(q)          # similar to T_X, same determinants
    Tn = np.array(sp.Matrix(T).evalf(30), dtype=float)
    Cn = np.array(sp.Matrix(C).evalf(30), dtype=float)
    M = np.block([[Tn, -(np.eye(n) - Cn)], [np.eye(n), np.zeros((n, n))]])
    cp = np.poly(M)                                     # det(z - M), descending
    pc = [float(p.as_expr().coeff(z, k)) for k in range(2 * n, -1, -1)]
    check('%s det(z-M)=p coefficientwise' % tag, np.max(np.abs(cp - np.array(pc))) < 1e-9,
          str(np.max(np.abs(cp - np.array(pc)))))
    # det(1 - zM) = z^{2n} det(1/z - M) = reversal
    ptc = [float(reverse(sp.Poly(p.as_expr(), z), n).as_expr().coeff(z, k)) for k in range(2 * n, -1, -1)]
    rev = cp[::-1]
    check('%s det(1-zM)=ptilde' % tag, np.max(np.abs(rev - np.array(ptc))) < 1e-9,
          str(np.max(np.abs(rev - np.array(ptc)))))
    # (b) Tr M^m = sum of m-th powers of the roots of p
    roots = np.roots(cp)
    Mp = np.eye(2 * n)
    for m in range(1, 9):
        Mp = Mp @ M
        check('%s Tr M^%d = power sum' % (tag, m),
              abs(np.trace(Mp) - np.sum(roots ** m)) < 1e-7,
              str(abs(np.trace(Mp) - np.sum(roots ** m))))
    # (c) ker M = 0 (+) ker(I-C);  ord_0 p = 2 dim ker(I-C)
    dimk = n - np.linalg.matrix_rank(np.eye(n) - Cn, tol=1e-9)
    nullM = 2 * n - np.linalg.matrix_rank(M, tol=1e-9)
    check('%s dim ker M = dim ker(I-C)' % tag, nullM == dimk, '%d vs %d' % (nullM, dimk))
    ns = sp.Matrix(np.eye(n) - Cn).nullspace()
    for v in ns:
        w = np.concatenate([np.zeros(n), np.array(v, dtype=float).flatten()])
        check('%s (0,y) in ker M' % tag, np.max(np.abs(M @ w)) < 1e-9)
    ord0 = min(k for k in range(2 * n + 1) if p.as_expr().coeff(z, k) != 0)
    check('%s ord_0 p = 2 dim ker(I-C)' % tag, ord0 == 2 * dimk, '%d vs %d' % (ord0, 2 * dimk))
    n2 = 2 * n - np.linalg.matrix_rank(M @ M, tol=1e-9)
    n3 = 2 * n - np.linalg.matrix_rank(M @ M @ M, tol=1e-9)
    check('%s Jordan blocks at 0 all of size two' % tag, (n2 == 2 * dimk) and (n3 == n2),
          'nullities %d %d %d' % (nullM, n2, n3))
    # M - M_0 rank = number of DISTINCT junction vertices
    M0 = np.block([[Tn, -np.eye(n)], [np.eye(n), np.zeros((n, n))]])
    D = M - M0
    want = np.block([[np.zeros((n, n)), Cn], [np.zeros((n, n)), np.zeros((n, n))]])
    check('%s M-M0 = [[0,C],[0,0]]' % tag, np.max(np.abs(D - want)) < 1e-12)
    check('%s rank(M-M0) = #distinct junctions' % tag,
          np.linalg.matrix_rank(D, tol=1e-9) == np.linalg.matrix_rank(Cn, tol=1e-9))

# the D3 correction has rank 3 while h = 4 (F2)
check('D3 rank C = 3 but h = 4',
      np.linalg.matrix_rank(np.array(sp.Matrix(C3).evalf(30), dtype=float), tol=1e-9) == 3 and len(D3_CUSPS) == 4)

# D2, D3 cores are NOT (q+1)-regular by themselves (F4)
def core_degrees(V, S, E):
    d = {v: sp.Integer(0) for v in V}
    for (u, v), se in E.items():
        d[u] += sp.Rational(S[u], se)
        d[v] += sp.Rational(S[v], se)
    return d
cd2 = core_degrees(D2_V, D2_S, D2_E)
check('D2 core not 3-regular (B has degree 2)', cd2['B'] == 2 and all(cd2[v] == 3 for v in D2_V if v != 'B'),
      str(cd2))

# --------------------------------------------- (c) loop at a c=1 junction
Tl = sp.Matrix([[sp.Rational(1, 2), 1], [1, sp.Rational(-1, 3)]])
Cl = sp.diag(1, 0)
pl = sp.Poly(sp.expand(((1 + z ** 2) * sp.eye(2) - z * Tl - Cl).det()), z)
check('loop core: p = z(6z^3-z^2-z-3)/6',
      sp.simplify(pl.as_expr() - z * (6 * z ** 3 - z ** 2 - z - 3) / 6) == 0, str(pl.as_expr()))
ord0l = min(k for k in range(5) if pl.as_expr().coeff(z, k) != 0)
check('loop core: ord_0 p = 1 though dim ker(I-C)=1', ord0l == 1)
Ml = np.array(linearisation(Tl, Cl).evalf(30), dtype=float)
check('loop core: Jordan block at 0 has size one',
      (4 - np.linalg.matrix_rank(Ml, tol=1e-9)) == 1 and (4 - np.linalg.matrix_rank(Ml @ Ml, tol=1e-9)) == 1)

# ------------------------------------------- five random rational cores, 1..3 cusps
rng = np.random.default_rng(20260920)
for trial in range(5):
    n = int(rng.integers(2, 5))
    T = sp.zeros(n, n)
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < 0.7:
                val = sp.Rational(int(rng.integers(-4, 5)), int(rng.integers(1, 4)))
                T[i, j] = val
                T[j, i] = val
    h = int(rng.integers(1, 4))
    C = sp.zeros(n, n)
    for a in range(h):
        v = int(rng.integers(0, n))
        C[v, v] += 1
        T[v, v] = 0                              # no loop at a junction
    M = linearisation(T, C)
    p = sp.Poly(sp.expand(((1 + z ** 2) * sp.eye(n) - z * T - C).det()), z)
    check('random %d: det(z-M)=p (exact)' % trial,
          sp.expand((z * sp.eye(2 * n) - M).det() - p.as_expr()) == 0)
    Mn = np.array(sp.Matrix(M).evalf(30), dtype=float)
    Mp = np.eye(2 * n)
    rts = np.roots([float(p.as_expr().coeff(z, k)) for k in range(2 * n, -1, -1)])
    ok = True
    for m in range(1, 7):
        Mp = Mp @ Mn
        ok = ok and abs(np.trace(Mp) - np.sum(rts ** m)) < 1e-7
    check('random %d: Tr M^m = power sums m=1..6' % trial, ok)
    dimk = len([1 for i in range(n) if C[i, i] == 1])
    Cn = np.array(sp.Matrix(C).evalf(30), dtype=float)
    dk = n - np.linalg.matrix_rank(np.eye(n) - Cn, tol=1e-9)
    ord0 = min(k for k in range(2 * n + 1) if p.as_expr().coeff(z, k) != 0)
    check('random %d: ord_0 p = 2 dim ker(I-C)' % trial, ord0 == 2 * dk, '%d %d' % (ord0, dk))

# ---------------------------------------------------- (d) Bass / Hashimoto
def hashimoto(edges, nv):
    dirs = []
    for (u, v) in edges:
        dirs.append((u, v))
        dirs.append((v, u))
    m = len(dirs)
    B = np.zeros((m, m))
    for i, (u, v) in enumerate(dirs):
        for j, (a, b) in enumerate(dirs):
            if v == a and b != u:
                B[i, j] = 1.0
    return B


GRAPHS = {
    'K4': (4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)], 2),
    'cube': (8, [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4),
                 (0, 4), (1, 5), (2, 6), (3, 7)], 2),
    'K33': (6, [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)], 2),
    'Petersen': (10, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (5, 7), (7, 9), (9, 6), (6, 8), (8, 5),
                      (0, 5), (1, 6), (2, 7), (3, 8), (4, 9)], 2),
    'C5': (5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)], 1),
}
for name, (nv, edges, q) in GRAPHS.items():
    A = np.zeros((nv, nv))
    for (u, v) in edges:
        A[u, v] = 1
        A[v, u] = 1
    check('%s is (q+1)-regular' % name, np.all(A.sum(axis=1) == q + 1), str(A.sum(axis=1)))
    B = hashimoto(edges, nv)
    ne = len(edges)
    for uu in (0.13, 0.37, -0.21, 0.51):
        lhs = np.linalg.det(np.eye(2 * ne) - uu * B)
        rhs = (1 - uu ** 2) ** (ne - nv) * np.linalg.det(np.eye(nv) - uu * A + q * uu ** 2 * np.eye(nv))
        check('%s Bass at u=%.2f' % (name, uu), abs(lhs - rhs) < 1e-7 * max(1, abs(rhs)),
              '%g %g' % (lhs, rhs))
    # shard's spectral form: spec(sqrt q M0) u {+-1}^{|E|-|V|} = spec(B)
    T = A / np.sqrt(q)
    M0 = np.block([[T, -np.eye(nv)], [np.eye(nv), np.zeros((nv, nv))]])
    left = np.concatenate([np.sqrt(q) * np.linalg.eigvals(M0),
                           np.ones(ne - nv), -np.ones(ne - nv)])
    right = np.linalg.eigvals(B)
    check('%s spec(sqrt q M0) u {+-1} = spec(B)' % name,
          multiset_dist(left, right) < 1e-6, str(multiset_dist(left, right)))
    # and the brief's (wrong) form, for the record
    bad = np.concatenate([np.linalg.eigvals(M0), np.ones(ne - nv), -np.ones(ne - nv)])
    rightn = np.linalg.eigvals(B) / np.sqrt(q)
    if ne > nv:
        check('%s brief form spec(M0)u{+-1}=spec(B)/sqrt q FAILS (expected)' % name,
              multiset_dist(bad, rightn) > 1e-3, str(multiset_dist(bad, rightn)))

# ------------------------------------------------ det S = (-1)^h p/ptilde on D2, D3
def scattering(Ahat, C, q, junctions, zval):
    """S(z) = -Q(z)^{-1} Q(1/z), Q = I - z Gamma, Gamma = W^*(lam - T)^{-1}W."""
    n = Ahat.shape[0]
    T = Ahat / np.sqrt(q)
    h = len(junctions)
    W = np.zeros((n, h))
    for a, (vi, c) in enumerate(junctions):
        W[vi, a] = c
    lam = zval + 1.0 / zval
    G = np.linalg.inv(lam * np.eye(n) - T)
    Gam = W.T @ G @ W
    Q = np.eye(h) - zval * Gam
    Qi = np.eye(h) - (1.0 / zval) * Gam
    return -np.linalg.solve(Q, Qi)


def sym_adj(V, S, E):
    n = len(V)
    idx = {v: i for i, v in enumerate(V)}
    A = np.zeros((n, n))
    for (u, v), se in E.items():
        w = np.sqrt(S[u] * S[v]) / se
        A[idx[u], idx[v]] = w
        A[idx[v], idx[u]] = w
    return A


for tag, (V, S, E, cusps, q, p, n) in {'D2': (D2_V, D2_S, D2_E, D2_CUSPS, 2, p2, 6),
                                       'D3': (D3_V, D3_S, D3_E, D3_CUSPS, 3, p3, 9)}.items():
    Ahat = sym_adj(V, S, E)
    idx = {v: i for i, v in enumerate(V)}
    junc = [(idx[v], np.sqrt(S[v] / se)) for (v, se) in cusps]
    h = len(junc)
    pt = reverse(sp.Poly(p.as_expr(), z), n)
    for zv in (0.31 + 0.17j, -0.44 + 0.62j, 0.73 - 0.28j):
        Sm = scattering(Ahat, None, q, junc, zv)
        lhs = np.linalg.det(Sm)
        rhs = (-1) ** h * complex(p.as_expr().subs(z, zv)) / complex(pt.as_expr().subs(z, zv))
        check('%s det S = (-1)^h p/ptilde at %s' % (tag, zv), abs(lhs - rhs) < 1e-8,
              '%s %s' % (lhs, rhs))

# ---- the Bass step in (d) NEEDS regularity: a counterexample on a non-regular graph
for name, (nv, edges) in {'path P4': (4, [(0, 1), (1, 2), (2, 3)]),
                          'triangle+pendant': (4, [(0, 1), (1, 2), (2, 0), (2, 3)]),
                          'K4 minus an edge': (4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)])}.items():
    A = np.zeros((nv, nv))
    for (uu, vv) in edges:
        A[uu, vv] = 1
        A[vv, uu] = 1
    degs = A.sum(axis=1)
    check('%s is NOT regular' % name, len(set(degs.tolist())) > 1, str(degs))
    B = hashimoto(edges, nv)
    ne = len(edges)
    Dm = np.diag(degs)
    ok_gen = True
    ok_q = True
    for uu in (0.13, 0.31, -0.19):
        gen = (1 - uu ** 2) ** (ne - nv) * np.linalg.det(np.eye(nv) - uu * A + uu ** 2 * (Dm - np.eye(nv)))
        lhs = np.linalg.det(np.eye(2 * ne) - uu * B)
        if abs(lhs - gen) > 1e-7 * max(1, abs(gen)):
            ok_gen = False
        for qtry in (1, 2, 3):
            spec_form = (1 - uu ** 2) ** (ne - nv) * np.linalg.det(
                np.eye(nv) - uu * A + qtry * uu ** 2 * np.eye(nv))
            if abs(lhs - spec_form) < 1e-7 * max(1, abs(spec_form)):
                ok_q = False
    check('%s: general Bass (D-I) holds' % name, ok_gen)
    check('%s: the shard form det(I-uA+q u^2) FAILS for every q (regularity is needed)' % name, ok_q)

print("\nscratch_gt_lin: %d passed, %d failed" % (PASS[0], len(FAIL)))
