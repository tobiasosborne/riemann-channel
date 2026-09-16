#!/usr/bin/env python3
"""Independent REFUTE-lane check of D7 (finite graphs and quantum channels)
in notes/selberg-letters/astra-proofs.md.

Written from scratch; does NOT import or re-run
notes/selberg-letters/finite/check_letters.py.  Exact integer / rational
linear algebra (numpy int64 and sympy) wherever a multiplicity matters.
"""
import itertools
import numpy as np
import sympy as sp

def rank_mod(A, pr):
    """Exact rank over GF(pr) of an integer matrix."""
    A = [[int(x) % pr for x in row] for row in A]
    n, mc = len(A), len(A[0])
    r = 0
    for c in range(mc):
        piv = next((i for i in range(r, n) if A[i][c] % pr), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c], pr - 2, pr)
        A[r] = [(x * inv) % pr for x in A[r]]
        for i in range(n):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [(A[i][k] - f * A[r][k]) % pr for k in range(mc)]
        r += 1
        if r == n:
            break
    return r


def nullities(Mint):
    """(nullity(M), nullity(M^2)); two prime fields and the float SVD must agree."""
    n = Mint.shape[0]
    out = []
    for A in (Mint, Mint @ Mint):
        vals = {n - rank_mod(A.tolist(), pr) for pr in (1000003, 2000003)}
        sv = np.linalg.svd(A.astype(float), compute_uv=False)
        nz = int(np.sum(sv < 1e-8 * max(1.0, sv[0])))
        assert len(vals) == 1 and vals == {nz}, (vals, nz)
        out.append(nz)
    return tuple(out)


PASS = FAIL = 0


def chk(name, cond, extra=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  PASS  {name} {extra}", flush=True)
    else:
        FAIL += 1
        print(f"  FAIL  {name} {extra}", flush=True)


def Z(A):
    return bool(np.all(A == 0))


# ---------------------------------------------------------------- graphs
def graph_ops(adj):
    """Report's graph convention:
       (Tu)(v,w) = sum_{x~v, x!=w} u(x,v),  (Ru)(v) = sum_{x~v} u(x,v),
       (Sf)(v,w) = f(v),                    (J0 u)(v,w) = u(w,v)."""
    V = sorted(adj)
    iv = {v: i for i, v in enumerate(V)}
    E = [(v, w) for v in V for w in adj[v]]
    ie = {e: i for i, e in enumerate(E)}
    n, m = len(V), len(E)
    T = np.zeros((m, m), dtype=np.int64)
    R = np.zeros((n, m), dtype=np.int64)
    S = np.zeros((m, n), dtype=np.int64)
    J0 = np.zeros((m, m), dtype=np.int64)
    Sig = np.zeros((n, n), dtype=np.int64)
    for (v, w) in E:
        j = ie[(v, w)]
        for x in adj[v]:
            if x != w:
                T[j, ie[(x, v)]] += 1
        S[j, iv[v]] = 1
        J0[j, ie[(w, v)]] = 1
    for v in V:
        for x in adj[v]:
            R[iv[v], ie[(x, v)]] += 1
            Sig[iv[v], iv[x]] += 1
    return V, E, T, R, S, J0, Sig


def cartesian(a1, a2):
    return {(u, x): sorted([(w, x) for w in a1[u]] + [(u, y) for y in a2[x]])
            for u in a1 for x in a2}


K4 = {i: sorted(j for j in range(4) if j != i) for i in range(4)}
K3 = {i: sorted(j for j in range(3) if j != i) for i in range(3)}
Q3 = {b: sorted(b ^ (1 << k) for k in range(3)) for b in range(8)}
PET = {i: [] for i in range(10)}
for _a, _b in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 5), (1, 6), (2, 7),
               (3, 8), (4, 9), (5, 7), (7, 9), (9, 6), (6, 8), (8, 5)]:
    PET[_a].append(_b)
    PET[_b].append(_a)
PET = {k: sorted(v) for k, v in PET.items()}

# ------------------------------------------------------------- quantum
I2 = sp.eye(2)
Xp = sp.Matrix([[0, 1], [1, 0]])
Yp = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Zp = sp.Matrix([[1, 0], [0, -1]])
BAS = [I2, Xp, Yp, Zp]


def ad(U):
    M = sp.zeros(4, 4)
    for j, b in enumerate(BAS):
        img = sp.expand(U * b * U.conjugate().T)
        for i, a in enumerate(BAS):
            M[i, j] = sp.simplify(sp.trace(a.conjugate().T * img) / 2)
    return np.array(M.tolist(), dtype=object)


def quantum_ops(letters, rev):
    """Notebook source-letter convention of 08_quantum_ihara_general.tex:
       (Tx)_j = sum_{i != bar j} E_i x_i, Rx = sum_i E_i x_i,
       (Sf)_j = f, (J0 x)_j = E_{bar j} x_{bar j},  E_i = Ad(U_i)."""
    D = len(letters)
    Es = [ad(U) for U in letters]
    N = 4
    T = np.zeros((N * D, N * D), dtype=object)
    R = np.zeros((N, N * D), dtype=object)
    S = np.zeros((N * D, N), dtype=object)
    J0 = np.zeros((N * D, N * D), dtype=object)
    Sig = np.zeros((N, N), dtype=object)
    T[:] = 0; R[:] = 0; S[:] = 0; J0[:] = 0; Sig[:] = 0
    for j in range(D):
        for i in range(D):
            if i != rev[j]:
                T[N * j:N * j + N, N * i:N * i + N] = Es[i]
        S[N * j:N * j + N, :] = np.eye(N, dtype=object)
        J0[N * j:N * j + N, N * rev[j]:N * rev[j] + N] = Es[rev[j]]
    for i in range(D):
        R[:, N * i:N * i + N] = Es[i]
        Sig = Sig + Es[i]
    return T, R, S, J0, Sig


def core(name, T, R, S, J0, Sig, D):
    q = D - 1
    n = Sig.shape[0]
    m = T.shape[0]
    chk(f"{name}: J0^2 = 1", Z(J0 @ J0 - np.eye(m, dtype=J0.dtype)))
    chk(f"{name}: RS = Sigma", Z(R @ S - Sig))
    chk(f"{name}: R J0 S = D", Z(R @ J0 @ S - D * np.eye(n, dtype=R.dtype)))
    chk(f"{name}: T = SR - J0", Z(T - (S @ R - J0)))
    chk(f"{name}: Sigma Hermitian", Z(Sig - np.conjugate(Sig).T))
    chk(f"{name}: RT = Sigma R - R J0", Z(R @ T - (Sig @ R - R @ J0)))
    chk(f"{name}: R J0 T = q R", Z(R @ J0 @ T - q * R))
    chk(f"{name}: (S R J0)^2 = D (S R J0)", Z((S @ R @ J0) @ (S @ R @ J0) - D * (S @ R @ J0)))
    Ts = sp.Matrix(T.tolist())
    Rs = sp.Matrix(R.tolist())
    Ss = sp.Matrix(Sig.tolist())
    Sm = sp.Matrix(S.tolist())
    Jm = sp.Matrix(J0.tolist())
    chk(f"{name}: T invertible", Ts.det() != 0)
    chk(f"{name}: Sigma R = R(T + q T^-1)",
        sp.simplify(Ss * Rs - Rs * (Ts + q * Ts.inv())) == sp.zeros(n, m))
    Lm = sp.Matrix.hstack(Sm, Jm * Sm)
    Cn = sp.Matrix(sp.BlockMatrix([[Ss, q * sp.eye(n)], [-sp.eye(n), sp.zeros(n, n)]]))
    chk(f"{name}: T L = L C", sp.simplify(Ts * Lm - Lm * Cn) == sp.zeros(m, 2 * n))
    chk(f"{name}: L^*L = [[D,Sigma],[Sigma,D]]",
        sp.simplify(Lm.conjugate().T * Lm - sp.Matrix(sp.BlockMatrix(
            [[D * sp.eye(n), Ss], [Ss, D * sp.eye(n)]]))) == sp.zeros(2 * n, 2 * n))
    mu = sp.Symbol('mu')
    nl = bad = 0
    evs = Ss.eigenvects()
    for val, mult, vecs in evs:
        if sp.simplify(val - D) == 0 or sp.simplify(val + D) == 0:
            continue
        for f in vecs:
            for r in sp.solve(mu ** 2 - val * mu + q, mu):
                if sp.simplify(r ** 2 - 1) == 0:
                    continue
                Fm = sp.expand((r * Sm * f - Jm * Sm * f) / (r ** 2 - 1))
                if sp.simplify(Ts * Fm - r * Fm) != sp.zeros(m, 1):
                    bad += 1
                if sp.simplify(Rs * Fm - f) != sp.zeros(n, 1):
                    bad += 1
                nl += 1
    chk(f"{name}: F_mu inverts the pushforward on all {nl} retained lifts "
        f"(including mu = +-sqrt q)", bad == 0)
    ret = [sp.nsimplify(v) for v, _, _ in evs
           if sp.simplify(v - D) != 0 and sp.simplify(v + D) != 0]
    mx = max(abs(complex(v).real) for v in ret)
    strict = mx < 2 * float(sp.sqrt(q)) - 1e-12
    schur = all(float(q - complex(v).real ** 2 / 4) > 1e-12 for v in ret)
    chk(f"{name}: Schur complement q - Sigma^2/4 > 0 <-> strict band", strict == schur,
        f"[max|a_ret| = {mx:.6f}, 2 sqrt q = {2 * float(sp.sqrt(q)):.6f}]")


print("=== (D7-G)/(D7-FE): symbolic companion identities, generic Hermitian Sigma ===", flush=True)
nn = 2
q = sp.Symbol('q', positive=True)
aa, bb, cc = sp.symbols('aa bb cc', real=True)
Sg = sp.Matrix([[aa, bb], [bb, cc]])
C = sp.Matrix(sp.BlockMatrix([[Sg, q * sp.eye(nn)], [-sp.eye(nn), sp.zeros(nn, nn)]]))
Gc = sp.Matrix(sp.BlockMatrix([[sp.eye(nn), Sg / 2], [Sg / 2, q * sp.eye(nn)]]))
chk("C^* G_C C = q G_C", sp.simplify(C.T * Gc * C - q * Gc) == sp.zeros(2 * nn, 2 * nn))
Fc = sp.Matrix(sp.BlockMatrix([[sp.zeros(nn, nn), sp.sqrt(q) * sp.eye(nn)],
                               [sp.eye(nn) / sp.sqrt(q), sp.zeros(nn, nn)]]))
chk("F_C^2 = 1", sp.simplify(Fc * Fc - sp.eye(2 * nn)) == sp.zeros(2 * nn, 2 * nn))
chk("F_C C F_C = q C^{-1}", sp.simplify(Fc * C * Fc - q * C.inv()) == sp.zeros(2 * nn, 2 * nn))
chk("F_C^* G_C F_C = G_C", sp.simplify(Fc.T * Gc * Fc - Gc) == sp.zeros(2 * nn, 2 * nn))
chk("Schur complement of G_C is q - Sigma^2/4",
    sp.simplify((q * sp.eye(nn) - (Sg / 2) * (Sg / 2)) - (q * sp.eye(nn) - Sg ** 2 / 4))
    == sp.zeros(nn, nn))
Cend = sp.Matrix([[6, 9], [-1, 0]])
chk("at the endpoint a = 2 sqrt q (a=6,q=9) the companion block is a size-2 Jordan block",
    (Cend - 3 * sp.eye(2)).rank() == 1 and ((Cend - 3 * sp.eye(2)) ** 2).rank() == 0)
chk("outside the closed band one root has modulus != sqrt q (a=7,q=9)",
    not all(abs(complex(r)) - 3 < 1e-9
            for r in sp.solve(sp.Symbol('m') ** 2 - 7 * sp.Symbol('m') + 9, sp.Symbol('m'))))

print("=== graphs ===", flush=True)
for nm, adj_, D_ in (("K_4", K4, 3), ("Petersen", PET, 3)):
    V, E, T, R, S, J0, Sig = graph_ops(adj_)
    core(nm, T, R, S, J0, Sig, D_)

print("=== K_3 x Q_3 endpoint counterexample (exact) ===", flush=True)
adj_ = cartesian(K3, Q3)
V, E, T, R, S, J0, Sig = graph_ops(adj_)
chk("5-regular on 24 vertices", set(len(adj_[v]) for v in V) == {5} and len(V) == 24)
ev = sp.Matrix(Sig.tolist()).eigenvals()
evl = sorted(((int(sp.nsimplify(k)), v) for k, v in ev.items()), key=lambda t: t[0])
chk("Sigma spectrum = {2,-1,-1} + {3,1,1,1,-1,-1,-1,-3}",
    evl == [(-4, 2), (-2, 6), (-1, 1), (0, 6), (1, 3), (2, 2), (3, 3), (5, 1)],
    f"[{evl}]")
chk("Ramanujan for q=4: max |a| over nontrivial = 4 = 2 sqrt q (endpoint attained, mult 2)",
    max(abs(k) for k, _ in evl if k != 5) == 4 and dict(evl)[-4] == 2)
Mint = T + 2 * np.eye(T.shape[0], dtype=np.int64)
k1, k2 = nullities(Mint)
chk("dim ker(T+2) = 2, dim ker(T+2)^2 = 4 (GF(1000003), GF(2000003) and SVD agree)",
    (k1, k2) == (2, 4), f"[got ({k1},{k2}), edge space dim {Mint.shape[0]}]")

print("=== quantum: six Pauli letters ===", flush=True)
L6 = [Xp, Xp, Yp, Yp, Zp, Zp]
r6 = [1, 0, 3, 2, 5, 4]
T6, R6, S6, J06, Sig6 = quantum_ops(L6, r6)
G6 = ad(Zp)
even, odd = [0, 3], [1, 2]
chk("Ad(Z) grading is diag(+1,-1,-1,+1) on (I,X,Y,Z): even {I,Z}, odd {X,Y}",
    [G6[i, i] for i in range(4)] == [1, -1, -1, 1])
Se = sp.Matrix([[Sig6[i, j] for j in even] for i in even])
So = sp.Matrix([[Sig6[i, j] for j in odd] for i in odd])
chk("even adjacency spectrum {6,-2}",
    sorted(float(k) for k, v in Se.eigenvals().items() for _ in range(v)) == [-2.0, 6.0])
chk("odd adjacency spectrum {-2,-2}",
    sorted(float(k) for k, v in So.eigenvals().items() for _ in range(v)) == [-2.0, -2.0])
u = sp.Symbol('u')
Z0 = sp.factor(sp.expand((sp.eye(2) - u * Se + 5 * u ** 2 * sp.eye(2)).det()))
Z1 = sp.factor(sp.expand((sp.eye(2) - u * So + 5 * u ** 2 * sp.eye(2)).det()))
chk("reduced graded zeta = (1+2u+5u^2)/((1-u)(1-5u))",
    sp.simplify(Z1 / Z0 - (1 + 2 * u + 5 * u ** 2) / ((1 - u) * (1 - 5 * u))) == 0,
    f"[{Z1} / {Z0}]")


def NP(letters, rev, P, nmax):
    D = len(letters)
    out = []
    for n_ in range(1, nmax + 1):
        tot = 0
        for w in itertools.product(range(D), repeat=n_):
            if any(w[(k + 1) % n_] == rev[w[k]] for k in range(n_)):
                continue
            M = np.eye(2, dtype=complex)
            for i in reversed(w):
                M = M @ letters[i]
            tot += abs(np.trace(P @ M)) ** 2
        out.append(int(round(tot)))
    return out


L6n = [np.array(sp.Matrix(U).evalf().tolist(), dtype=complex) for U in L6]
Zn = np.array(sp.Matrix(Zp).evalf().tolist(), dtype=complex)
vals = NP(L6n, r6, Zn, 6)
chk("N_P(1..6) = 8,32,104,640,3208,15392 (brute force over cyclically "
    "non-backtracking words, |Tr(P U_w)|^2)",
    vals == [8, 32, 104, 640, 3208, 15392], f"[{vals}]")
ser = sp.expand(sp.series(sp.log((1 + 2 * u + 5 * u ** 2) / ((1 - u) * (1 - 5 * u))),
                          u, 0, 7).removeO())
chk("... and they equal n [u^n] log Z(u) of the reduced zeta",
    [int(ser.coeff(u, k) * k) for k in range(1, 7)] == [8, 32, 104, 640, 3208, 15392])
core("Pauli6", T6, R6, S6, J06, Sig6, 6)

print("=== quantum: ten-letter endpoint counterexample (I x4, X x4, Z x2, P=Z) ===", flush=True)
L10 = [I2, I2, I2, I2, Xp, Xp, Xp, Xp, Zp, Zp]
r10 = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]
T10, R10, S10, J010, Sig10 = quantum_ops(L10, r10)
Se10 = sp.Matrix([[Sig10[i, j] for j in even] for i in even])
So10 = sp.Matrix([[Sig10[i, j] for j in odd] for i in odd])
chk("even adjacency {10,2}",
    sorted(float(k) for k, v in Se10.eigenvals().items() for _ in range(v)) == [2.0, 10.0])
chk("odd adjacency {6,-2}",
    sorted(float(k) for k, v in So10.eigenvals().items() for _ in range(v)) == [-2.0, 6.0])
chk("sector Ramanujan (closed band): D=10, q=9, 2 sqrt q = 6; the ODD endpoint 6 is attained",
    max(2.0, 2.0, 6.0) == 6.0)
oddidx = [4 * j + i for j in range(10) for i in odd]
T10o = np.array([[int(T10[i, j]) for j in oddidx] for i in oddidx], dtype=np.int64)
n1, n2 = nullities(T10o - 3 * np.eye(T10o.shape[0], dtype=np.int64))
chk("odd Hashimoto at mu=3: nullities 1 and 2 (one size-2 Jordan block)",
    (n1, n2) == (1, 2), f"[got ({n1},{n2}), odd edge space dim {T10o.shape[0]}]")
chk("the endpoint odd quadratic 1-6u+9u^2 has no even partner, so it survives in the net zeta",
    sp.simplify(sp.expand((sp.eye(2) - u * So10 + 9 * u ** 2 * sp.eye(2)).det())
                - (1 - 6 * u + 9 * u ** 2) * (1 + 2 * u + 9 * u ** 2)) == 0
    and sp.simplify(sp.expand((sp.eye(2) - u * Se10 + 9 * u ** 2 * sp.eye(2)).det())
                    - (1 - 10 * u + 9 * u ** 2) * (1 - 2 * u + 9 * u ** 2)) == 0)

print(f"\nTALLY scratch_sl_finite.py: {PASS} PASS / {FAIL} FAIL", flush=True)
