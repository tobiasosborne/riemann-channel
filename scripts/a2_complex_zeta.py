#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
a2_complex_zeta.py  --  the smallest Ramanujan complex of type \tilde A_2,
the Kang-Li determinant identity, RH <=> Ramanujan, and a representation-twisted
("quantum") version.

Construction: Lubotzky-Samuels-Vishne, math/0406217, Algorithm in section
"Explicit constructions" (sec:explicit), with q = 3, d = 3, e = 1, s = 1, so
L = F_3 and Gamma/Gamma(I) is a subgroup of PGL_3(F_3).

Zeta identity: Kang-Li 0804.2305 (Main Theorem, and the combinatorial
definitions of L_E / L_B at main.tex:208-212) and Kang-Li-Wang 0809.1401v1
(Theorem 3 at main.tex:1410-1418, Theorem 2 at :1352-1370).

Geodesic flow: Lubetzky-Lubotzky-Parzanchevski 1702.05452:1009-1027.

Run from the repo root:   python3 scripts/a2_complex_zeta.py
Deterministic; no randomness anywhere.
"""

import sys, time, itertools
from fractions import Fraction
from collections import deque

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

T0 = time.time()
np.set_printoptions(precision=6, suppress=False, linewidth=130)

def hdr(s):
    print()
    print("=" * 78)
    print(s)
    print("=" * 78)
    sys.stdout.flush()

def say(*a):
    print(*a); sys.stdout.flush()

q = 3
d = 3
M_ORDER = 18          # order to which all power-series identities are checked

# ---------------------------------------------------------------- F_{q^d}
# F_27 = F_3[v]/(v^3 + 2v + 2), i.e. v^3 = v + 1
def fmul(a, b):
    r = [0]*5
    for i in range(3):
        ai = a[i]
        if ai:
            for j in range(3):
                r[i+j] = (r[i+j] + ai*b[j]) % 3
    for k in (4, 3):              # v^3 = v+1 ; v^4 = v^2+v
        c = r[k]
        if c:
            r[k] = 0
            r[k-2] = (r[k-2] + c) % 3
            r[k-3] = (r[k-3] + c) % 3
    return tuple(x % 3 for x in r[:3])

FQD  = [(a, b, c) for a in range(3) for b in range(3) for c in range(3)]
ZERO = (0, 0, 0)
ONE  = (1, 0, 0)

def frob(a):                      # phi(x) = x^q  (l = 1, prime to d)
    return fmul(a, fmul(a, a))
def fnorm(a):
    return fmul(a, fmul(frob(a), frob(frob(a))))[0]
def ftrace(a):
    return sum(x[0] for x in (a, frob(a), frob(frob(a)))) % 3

# ----------------------------------------------------------- F_3 linear algebra
def inv3(Min):
    Min = np.asarray(Min, dtype=np.int64) % 3
    n = Min.shape[0]
    A = np.concatenate([Min, np.eye(n, dtype=np.int64)], axis=1)
    for i in range(n):
        p = next(r for r in range(i, n) if A[r, i] % 3)
        if p != i:
            A[[i, p]] = A[[p, i]]
        A[i] = (A[i] * (1 if A[i, i] % 3 == 1 else 2)) % 3
        for r in range(n):
            if r != i and A[r, i] % 3:
                A[r] = (A[r] - A[r, i]*A[i]) % 3
    return A[:, n:] % 3

def det3(Min):
    A = np.asarray(Min, dtype=np.int64).copy() % 3
    n = A.shape[0]; det = 1
    for i in range(n):
        p = None
        for r in range(i, n):
            if A[r, i] % 3:
                p = r; break
        if p is None:
            return 0
        if p != i:
            A[[i, p]] = A[[p, i]]; det = -det
        det = (det * A[i, i]) % 3
        A[i] = (A[i] * (1 if A[i, i] % 3 == 1 else 2)) % 3
        for r in range(i+1, n):
            if A[r, i] % 3:
                A[r] = (A[r] - A[r, i]*A[i]) % 3
    return det % 3

def pgl_norm(Min):
    """canonical representative of a class in PGL_3(F_3): scale so that the
    first non-zero entry (row-major) is 1."""
    A = np.asarray(Min, dtype=np.int64) % 3
    f = A.reshape(-1)
    nz = int(np.flatnonzero(f)[0])
    s = 1 if f[nz] == 1 else 2
    return tuple(int(x) for x in ((A*s) % 3).reshape(-1))

def pgl_mul(a, b):
    A = np.array(a, dtype=np.int64).reshape(3, 3)
    B = np.array(b, dtype=np.int64).reshape(3, 3)
    return pgl_norm(A @ B)

def pgl_inv(a):
    return pgl_norm(inv3(np.array(a, dtype=np.int64).reshape(3, 3)))

# ================================================================ STEP 1
hdr("STEP 1.  The complex: LSV math/0406217 sec:explicit, q=3, d=3, e=1, s=1")

# (1) normal basis zeta_0,zeta_1,zeta_2 of F_27/F_3
theta = None
for a in FQD:
    if a == ZERO:
        continue
    Bm = np.array([a, frob(a), frob(frob(a))], dtype=np.int64).T % 3
    if det3(Bm) != 0:
        theta = a; break
zetas = [theta, frob(theta), frob(frob(theta))]
Bmat = np.array(zetas, dtype=np.int64).T % 3
Binv = inv3(Bmat)
say("F_27 = F_3[v]/(v^3+2v+2);  normal basis zeta_i = phi^i(theta), theta =", theta)

def coords(a):
    return (Binv @ np.array(a, dtype=np.int64)) % 3
def rho(c):
    return np.array([coords(fmul(c, z)) for z in zetas], dtype=np.int64).T % 3
PHI = np.array([coords(frob(z)) for z in zetas], dtype=np.int64).T % 3
say("matrix of phi in the normal basis (a 3-cycle):", PHI.reshape(-1).tolist())

# (2) beta with tr(beta) != 0, and alpha in L = F_3 with gamma = y(alpha) = 1.
#     y(lam) = N(1+beta*lam) - 1 ; p(lam) = lam - gamma must be prime to lam and lam+1,
#     which for q = 3, e = 1 forces gamma = 1 (LSV main.tex:1719-1724 proof).
beta = alpha = None
for bcand in FQD:
    if bcand == ZERO or ftrace(bcand) == 0:
        continue
    for acand in (1, 2):
        w = tuple((ONE[i] + fmul((acand, 0, 0), bcand)[i]) % 3 for i in range(3))
        if (fnorm(w) - 1) % 3 == 1:                    # y(alpha) = gamma = 1
            beta, alpha = bcand, acand; break
    if beta is not None:
        break
say("beta =", beta, " tr(beta) =", ftrace(beta), " alpha =", alpha,
    " gamma = y(alpha) =", (fnorm(tuple((ONE[i]+fmul((alpha,0,0),beta)[i]) % 3 for i in range(3))) - 1) % 3)

# (3) rho(z) = (1 + rho(beta) x) . phi   with x |-> alpha in L = F_3   (LSV Prop. gse)
RZ  = ((np.eye(3, dtype=np.int64) + alpha*rho(beta)) @ PHI) % 3
RZi = inv3(RZ)
bmat = (np.eye(3, dtype=np.int64) - RZi) % 3
say("rho(z) det =", det3(RZ), ";  b = 1 - rho(z)^{-1}, det(b) =", det3(bmat))

# (4) the 13 generators b_u = rho(u) b rho(u)^{-1},  u in F_27^* / F_3^*
reps, seen = [], set()
for u in FQD:
    if u == ZERO:
        continue
    cls = frozenset([u, fmul((2, 0, 0), u)])
    if cls not in seen:
        seen.add(cls); reps.append(u)
S1 = [pgl_norm((rho(u) @ bmat @ inv3(rho(u))) % 3) for u in reps]
assert len(set(S1)) == 13
say("|S_1| =", len(set(S1)), " (= [3,1]_3 = q^2+q+1)")

# (5) closure
idx = {}
elts = []
dq = deque()
Id = pgl_norm(np.eye(3, dtype=np.int64))
idx[Id] = 0; elts.append(Id); dq.append(Id)
while dq:
    g = dq.popleft()
    for s in S1:
        h = pgl_mul(g, s)
        if h not in idx:
            idx[h] = len(elts); elts.append(h); dq.append(h)
NG = len(elts)
say("group order |G| = <S_1> =", NG, "   (|PGL_3(F_3)| = 5616)")
say("  -> G = PGL_3(F_3) = PSL_3(F_3):", NG == 5616)

S1i = [pgl_inv(s) for s in S1]
S1set, S2set = set(S1), set(S1i)
say("S_1 cap S_1^{-1} = empty:", len(S1set & S2set) == 0)

# colour-2 generators: headers b_u b_v of products of d=3 generators equal to 1
i_of = {s: i for i, s in enumerate(S1)}
P_triples = []
for i, s in enumerate(S1):
    for j, t in enumerate(S1):
        w = pgl_inv(pgl_mul(s, t))
        if w in i_of:
            P_triples.append((i, j, i_of[w]))
say("|P| = #{(u,v,w) : b_u b_v b_w = 1 in PGL_3(F_3)} =", len(P_triples),
    "  (expect (q^2+q+1)(q+1) = 52)")
S2 = sorted({pgl_mul(S1[i], S1[j]) for (i, j, k) in P_triples})
say("|S_2| =", len(S2), ";  S_2 == S_1^{-1}:", set(S2) == S2set)
S2 = [pgl_inv(s) for s in S1]          # use this ordering: S2[u] = S1[u]^{-1}

# LSV Prop. whatisr: index r = order of y/(1+y) in L^*/(L^*)^d
#   y -> gamma = 1, 1+y -> 2, so y/(1+y) = 2 and (F_3^*)^3 = F_3^*, hence r = 1.
say("LSV whatisr: r = ord of y/(1+y) in L^*/(L^*)^3 = 1  =>  Gamma_I = PSL_3(L),")
say("  and there is NO well-defined 3-colouring of the quotient (see below).")

# permutations of G by right multiplication
perm_of = {}
perm1 = np.zeros((13, NG), dtype=np.int64)
perm2 = np.zeros((13, NG), dtype=np.int64)
for u in range(13):
    su, si = S1[u], S2[u]
    for gi, g in enumerate(elts):
        perm1[u, gi] = idx[pgl_mul(g, su)]
        perm2[u, gi] = idx[pgl_mul(g, si)]
for u in range(13):
    perm_of[S1[u]] = perm1[u]
    perm_of[S2[u]] = perm2[u]

# --- colouring test -------------------------------------------------------
col = -np.ones(NG, dtype=np.int64); col[0] = 0
dq = deque([0]); ok_col = True
while dq:
    gi = dq.popleft()
    for u in range(13):
        h = perm1[u, gi]
        if col[h] < 0:
            col[h] = (col[gi] + 1) % 3; dq.append(h)
        elif col[h] != (col[gi] + 1) % 3:
            ok_col = False
say("global 3-colouring of the Cayley graph consistent:", ok_col,
    " (False is expected: G is simple, so no epimorphism G -> Z/3)")

# --- link of a vertex -----------------------------------------------------
nbrs = [("1", s) for s in S1] + [("2", s) for s in S2]
link_adj = np.zeros((26, 26), dtype=np.int64)
for a in range(26):
    for b in range(26):
        if a == b:
            continue
        x = pgl_mul(pgl_inv(nbrs[a][1]), nbrs[b][1])
        if x in S1set or x in S2set:
            link_adj[a, b] = 1
deg = link_adj.sum(1)
bip = all(link_adj[a, b] == 0 for a in range(13) for b in range(13)) and \
      all(link_adj[a, b] == 0 for a in range(13, 26) for b in range(13, 26))
# girth
def girth(A):
    n = A.shape[0]
    best = 10**9
    for s in range(n):
        dist = -np.ones(n, dtype=int); par = -np.ones(n, dtype=int)
        dist[s] = 0; Q = deque([s])
        while Q:
            v = Q.popleft()
            for w in np.flatnonzero(A[v]):
                if dist[w] < 0:
                    dist[w] = dist[v]+1; par[w] = v; Q.append(w)
                elif w != par[v]:
                    best = min(best, dist[v]+dist[w]+1)
    return best
gir = girth(link_adj)
co = link_adj[:13, 13:] @ link_adj[:13, 13:].T
off = co[~np.eye(13, dtype=bool)]
say("link of a vertex: %d vertices, degrees %s, bipartite %s, girth %d"
    % (26, sorted(set(deg.tolist())), bip, gir))
say("  any two 'points' lie on exactly one common 'line':", bool(np.all(off == 1)),
    "; each point is on q+1 =", int(co[0, 0]), "lines")
say("  => the point-line incidence graph of PG(2,3) (the unique (4,6)-cage).")

# --- V, E, F, chi ---------------------------------------------------------
V = NG
E = NG * 26 // 2
tri_per_vertex = int(link_adj.sum() // 2)
F = NG * tri_per_vertex // 3
chi = V - E + F
say("V = %d, E = %d, F = %d  (triangles per vertex = %d)" % (V, E, F, tri_per_vertex))
say("chi = V - E + F = %d   (= |G| * 16/3)" % chi)
# check there is no 3-cell (no K_4): link is triangle-free because girth 6
say("clique complex is 2-dimensional (link triangle-free):", gir > 3)
gord = []
for sgen in S1:
    g = sgen; k = 1
    while g != Id:
        g = pgl_mul(g, sgen); k += 1
    gord.append(k)
say("orders of the 13 generators b_u in PGL_3(F_3):", sorted(set(gord)))
ndiag = sum(1 for u in range(13) if pgl_mul(S1[u], S1[u]) == pgl_inv(S1[u]))
say("generators with b_u^3 = 1 (so the triangle {g,gb,gb^2} has a Z/3 stabiliser):", ndiag)
say("=> G acts freely on vertices and on edges, but NOT on the 2-cells:")
say("   %d of the %d triangles are stabilised by an order-3 element." % (NG*ndiag//3, F))
say("   This is exactly the caveat in T5.7 (no free action on unpointed simplices),")
say("   and it is why the per-block Euler factor is not (1-u^3)^{chi*dim/|G|}.")

# ================================================================ STEP 2
hdr("STEP 2.  Vertex level: the spectrum of A_1 and the temperedness test")

rows = np.repeat(np.arange(NG), 13)
A1 = sp.csr_matrix((np.ones(NG*13), (rows, perm1.T.reshape(-1))), shape=(NG, NG))
A2 = sp.csr_matrix((np.ones(NG*13), (rows, perm2.T.reshape(-1))), shape=(NG, NG))
say("A_2 == A_1^T :", (abs(A2 - A1.T)).nnz == 0)
comm = (A1 @ A1.T - A1.T @ A1)
say("A_1 normal (A_1 A_1^T = A_1^T A_1):", abs(comm).nnz == 0)
comm12 = (A1 @ A2 - A2 @ A1)
say("[A_1, A_2] = 0 :", abs(comm12).nnz == 0)

t = time.time()
A1d = np.asarray(A1.todense())
lam = np.linalg.eigvals(A1d)
say("dense eigvals(A_1) of size %d took %.1f s" % (NG, time.time()-t))
order = np.argsort(-np.abs(lam))
lam = lam[order]
say("largest |lambda|:", np.round(np.abs(lam[:6]), 8).tolist())
say("lambda with |lambda| > q^2+q+1-1e-6 :", np.round(lam[np.abs(lam) > 12.999], 6).tolist())

def tempered_defect(l):
    """p(z) = z^3 - (l/q) z^2 + (conj(l)/q) z - 1 is self-inversive.  By Cohn's
    theorem all its zeros lie on |z| = 1 iff all zeros of p'(z) = 3z^2 - 2sz + s~
    lie in |z| <= 1 (s = l/q).  The quadratic is solved in closed form, which is
    numerically stable, unlike np.roots on the nearly-degenerate cubic.
    Returns max|root of p'| - 1 (<= 0 means tempered)."""
    s = l/q
    disc = np.sqrt(s*s - 3.0*np.conj(s) + 0j)
    r1 = (s + disc)/3.0
    r2 = (s - disc)/3.0
    return float(max(abs(r1), abs(r2)) - 1.0)

defects = np.array([tempered_defect(l) for l in lam])
triv_mask = np.abs(np.abs(lam) - 13.0) < 1e-8
say("number of trivial eigenvalues (|lambda| = q^2+q+1 = 13):", int(triv_mask.sum()))
nt = ~triv_mask
say("nontrivial eigenvalues:", int(nt.sum()))
say("max temperedness defect (Cohn) over nontrivial eigenvalues: %.3e" % defects[nt].max())
say("fraction of nontrivial eigenvalues passing (defect < 1e-10): %.9f"
    % float(np.mean(defects[nt] < 1e-10)))
say("number failing at tolerance 1e-10: %d" % int((defects[nt] >= 1e-10).sum()))
say("max |lambda| over nontrivial eigenvalues: %.9f   (deltoid bound 3q = %d)"
    % (np.abs(lam[nt]).max(), 3*q))
say("joint spectrum: A_1 normal and real => A_2 v = conj(lambda) v on every")
say("  simultaneous eigenvector, so (lambda_1, lambda_2) = (lambda, conj lambda).")
say("Ramanujan (all nontrivial (l_1,l_2) in q*{z1+z2+z3 : |z_i|=1, z1z2z3=1}):",
    bool(defects[nt].max() < 1e-10))
say("distinct |lambda| values (rounded to 1e-6), with multiplicities:")
vals, cnts = np.unique(np.round(np.abs(lam), 6), return_counts=True)
say("   ", list(zip(vals.tolist()[::-1][:12], cnts.tolist()[::-1][:12])))
# a few sample nontrivial eigenvalues
say("sample nontrivial eigenvalues:", np.round(lam[nt][:5], 6).tolist())
del A1d

# ================================================================ STEP 3
hdr("STEP 3.  Edge / chamber operators and exact integer closed-walk counts")

# allowed straight (geodesic) successors of a colour-1 directed edge
allowed = [[t for t in range(13) if pgl_mul(S1[u], S1[t]) not in S2set] for u in range(13)]
nsucc = sorted({len(a) for a in allowed})
say("straight-flow successors of a directed colour-1 edge:", nsucc, " (expect q^2 = 9)")
say("  rule (LLP 1702.05452:1009-1027 / Kang-Li 0804.2305:210):")
say("  (x,y)->(y,z) allowed iff {x,y,z} is NOT a 2-cell; equivalently s_u s_t not in S_2.")

# ---- L_E on G x S_1 ------------------------------------------------------
NE = NG*13
ri, ci = [], []
for u in range(13):
    for t in allowed[u]:
        ri.append(np.arange(NG)*13 + u)
        ci.append(perm1[u]*13 + t)
LE = sp.csr_matrix((np.ones(NG*13*9, dtype=np.int64),
                    (np.concatenate(ri), np.concatenate(ci))), shape=(NE, NE))
say("L_E: %d x %d, %d nonzeros, out-degree %d" % (NE, NE, LE.nnz, LE.nnz//NE))

# ---- L_B on G x (chambers at a vertex) ----------------------------------
CH = [(i, j) for (i, j, k) in P_triples]
ch_of = {c: n for n, c in enumerate(CH)}
kmap = {(i, j): k for (i, j, k) in P_triples}
succ_by_j = {}
for (i, j) in CH:
    succ_by_j.setdefault(j, []).append(i)     # t' with (j,t') in CH ... fixed below
succ_pairs = {}
for j in range(13):
    succ_pairs[j] = [tp for tp in range(13) if (j, tp) in ch_of]
LB_rows, LB_cols = [], []
for n, (i, j) in enumerate(CH):
    k = kmap[(i, j)]
    for tp in succ_pairs[j]:
        if tp == k:
            continue
        m = i_of[pgl_inv(pgl_mul(S1[j], S1[tp]))]
        n2 = ch_of[(tp, m)]
        shift = perm2[i_of[pgl_inv(pgl_mul(S1[i], S1[j]))]]   # g -> g s_i s_j
        LB_rows.append(np.arange(NG)*52 + n)
        LB_cols.append(shift*52 + n2)
NB = NG*52
LB = sp.csr_matrix((np.ones(len(LB_rows)*NG, dtype=np.int64),
                    (np.concatenate(LB_rows), np.concatenate(LB_cols))), shape=(NB, NB))
say("L_B: %d x %d (directed chambers = 3F), %d nonzeros, out-degree %d"
    % (NB, NB, LB.nnz, LB.nnz//NB))

def traces_by_symmetry(Mat, block, starts, M):
    """exact Tr(Mat^m), m=1..M, using the free G-action: Tr = |G| * sum over the
    `starts` classes of the diagonal return count from the identity vertex."""
    out = [0]*(M+1)
    for s in starts:
        v = np.zeros(Mat.shape[0], dtype=np.int64)
        v[s] = 1
        for m in range(1, M+1):
            v = Mat.T @ v            # row-vector times Mat
            out[m] += int(v[s])
    return [NG*x for x in out]

t = time.time()
trLE = traces_by_symmetry(LE, 13, [u for u in range(13)], M_ORDER)
trLB = traces_by_symmetry(LB, 52, [n for n in range(52)], M_ORDER)
say("exact traces computed in %.1f s" % (time.time()-t))
trLEt = traces_by_symmetry(LE.T.tocsr(), 13, [u for u in range(13)], M_ORDER)
say("Tr((L_E^t)^m) == Tr(L_E^m) for all m:", trLEt == trLE)
say()
say(" m :          Tr(L_E^m)                 Tr(L_B^m)")
for m in range(1, M_ORDER+1):
    say("%2d : %24d %24d" % (m, trLE[m], trLB[m]))

# ---- exact Tr(A_1^a A_2^b) = |G| * n(a,b) -------------------------------
t = time.time()
nab = {}
w0 = np.zeros(NG, dtype=object); w0[:] = 0; w0[0] = 1
wa = w0
for a in range(0, M_ORDER+1):
    wb = wa
    for b in range(0, M_ORDER+1-a):
        nab[(a, b)] = int(wb[0])
        if a+b < M_ORDER:
            nb = np.zeros(NG, dtype=object); nb[:] = 0
            for u in range(13):
                nb = nb + wb[perm1[u]]          # right-multiplication by A_2
            wb = nb
    if a < M_ORDER:
        na = np.zeros(NG, dtype=object); na[:] = 0
        for u in range(13):
            na = na + wa[perm2[u]]              # right-multiplication by A_1
        wa = na
say("exact n(a,b) = (A_1^a A_2^b)[e,e] computed in %.1f s" % (time.time()-t))
say("n(1,1) = %d  (expect 13), n(3,0) = %d, n(0,3) = %d, n(2,2) = %d"
    % (nab[(1, 1)], nab[(3, 0)], nab[(0, 3)], nab[(2, 2)]))

# ---------------------------------------------------------------- series
def series_zero(M=M_ORDER):
    return [Fraction(0) for _ in range(M+1)]

def logdet_I_minus_uM(traces, M=M_ORDER, upow=1, sign=+1):
    """log det(I - sign * (u^upow) M) = -sum_m sign^m Tr(M^m) u^{m*upow}/m"""
    s = series_zero(M)
    for m in range(1, M+1):
        e = m*upow
        if e > M:
            break
        s[e] += Fraction(-(sign**m) * traces[m], m)
    return s

def add(a, b):
    return [x+y for x, y in zip(a, b)]
def sub(a, b):
    return [x-y for x, y in zip(a, b)]
def scal(a, c):
    return [x*c for x in a]

def log_1_minus_u3(M=M_ORDER):
    s = series_zero(M)
    for k in range(1, M//3+1):
        s[3*k] = Fraction(-1, k)
    return s

from math import comb
def logdet_cubic(nfun, NGr, M=M_ORDER):
    """log det(I - A_1 u + q A_2 u^2 - q^3 u^3 I) as a power series,
    using Tr(A_1^a A_2^b) = NGr * nfun(a,b) and [A_1,A_2] = 0."""
    s = series_zero(M)
    for k in range(1, M+1):
        # X = A_1 u + (-q) A_2 u^2 + q^3 u^3 I ; Tr(X^k)
        acc = [Fraction(0)]*(M+1)
        for a in range(k+1):
            for b in range(k+1-a):
                c = k-a-b
                e = a+2*b+3*c
                if e > M:
                    continue
                mult = comb(k, a)*comb(k-a, b)
                coef = mult * ((-q)**b) * ((q**3)**c)
                acc[e] += Fraction(coef * NGr * nfun(a, b))
        for e in range(1, M+1):
            s[e] -= acc[e]/k
    return s


def fit_euler(dif, M=M_ORDER):
    """write a log-series as a*log(1-u) + c*log(1-u^3) if possible; return (a,c,ok)."""
    ks = [i for i in range(1, M+1) if i % 3]
    a_vals = {-dif[i]*i for i in ks}
    if len(a_vals) != 1:
        return (None, None, False)
    a = a_vals.pop()
    c_vals = {-(dif[3*k] + Fraction(a, 3*k))*k for k in range(1, M//3+1)}
    if len(c_vals) != 1:
        return (a, None, False)
    return (a, c_vals.pop(), True)

def report_identity(name, lhs, rhs, M=M_ORDER):
    dd = sub(lhs, rhs)
    bad = [(i, dd[i]) for i in range(1, M+1) if dd[i] != 0]
    if not bad:
        say("  %-58s HOLDS to order u^%d" % (name, M))
    else:
        say("  %-58s FAILS; first bad coefficients:" % name)
        for i, v in bad[:6]:
            say("      u^%-3d residual = %s" % (i, v))
    return not bad

hdr("STEP 3b.  The cleared Kang-Li / Kang-Li-Wang identity")

say("Source form (0809.1401v1:main.tex:1410-1418, Theorem 3):")
say("   (1-u^3)^chi = det(I - A_1 u + q A_2 u^2 - q^3 u^3 I) det(I + L_B u)")
say("                 / [ det(I - L_E u) det(I - (L_E)^t u^2) ]")
say("i.e.  det(cubic) * det(I + L_B u)")
say("         =  (1-u^3)^chi * det(I - L_E u) * det(I - (L_E)^t u^2).")
say("Degree check for X_Gamma: LHS 3|G| + 3F = %d ; RHS 3chi + |E_1| + 2|E_1| = %d"
    % (3*NG + NB, 3*chi + NE + 2*NE))

def build_sides(nfun, NGr, trE, trEt, trB, chival, M=M_ORDER):
    L = add(logdet_cubic(nfun, NGr, M), logdet_I_minus_uM(trB, M, 1, -1))
    R = add(scal(log_1_minus_u3(M), chival),
            add(logdet_I_minus_uM(trE, M, 1, +1), logdet_I_minus_uM(trEt, M, 2, +1)))
    return L, R

hdr("STEP 3c.  Test on X_Gamma = Cayley complex of PGL_3(F_3)  (5616 vertices)")
say("NOTE: Kang-Li hypothesis (I), ord_pi det Gamma subset 3Z (= type preservation),")
say("      FAILS here, because r = 1 above: Gamma(I) is not contained in Gamma_1.")
nf = lambda a, b: nab[(a, b)]
L, R = build_sides(nf, NG, trLE, trLEt, trLB, chi)
ok_base = report_identity("det(cubic)*det(I+L_B u) = (1-u^3)^chi det det", L, R)
# alternatives
Lm, _ = build_sides(nf, NG, trLE, trLEt, trLB, chi)
Lalt = add(logdet_cubic(nf, NG), logdet_I_minus_uM(trLB, M_ORDER, 1, +1))
report_identity("variant: det(I - L_B u) instead of det(I + L_B u)", Lalt, R)
Rmis = add(logdet_I_minus_uM(trLE, M_ORDER, 1, +1), logdet_I_minus_uM(trLEt, M_ORDER, 2, +1))
Lmis = add(add(scal(log_1_minus_u3(), chi), logdet_cubic(nf, NG)),
           logdet_I_minus_uM(trLB, M_ORDER, 1, -1))
report_identity("variant: (1-u^3)^chi on the A/L_B side (prompt's form)", Lmis, Rmis)
# solve for the best exponent c in (1-u^3)^c
diff = sub(L, add(logdet_I_minus_uM(trLE, M_ORDER, 1, +1),
                  logdet_I_minus_uM(trLEt, M_ORDER, 2, +1)))
say("  residual det(cubic)det(I+L_Bu)/[det(I-L_Eu)det(I-L_E^t u^2)] as a log-series:")
say("   coefficients of u^1..u^6:", [str(x) for x in diff[1:7]])
a_, c_, ok_ = fit_euler(diff)
say("   fit residual = a*log(1-u) + c*log(1-u^3):  a = %s, c = %s, consistent to u^%d: %s"
    % (a_, c_, M_ORDER, ok_))
say("   (chi = %d; a = 0 and c = chi is the Kang-Li-Wang statement)" % chi)

hdr("STEP 3d.  Test on the type-preserving 3-fold cover  (16848 vertices)")
say("Gamma~ = Gamma(I) cap Gamma_1 is type preserving and torsion free, and")
say("Gamma/Gamma~ = PGL_3(F_3) x Z/3 (Goursat, since delta(Gamma(I)) = Z/3).")
say("Closed-walk counts on the cover = 3 * (base counts with total colour shift = 0).")
NGc = 3*NG
chic = 3*chi
trLEc  = [3*trLE[m] if m % 3 == 0 else 0 for m in range(M_ORDER+1)]
trLBc  = [3*trLB[m] if m % 3 == 0 else 0 for m in range(M_ORDER+1)]
nfc = lambda a, b: (nab[(a, b)] if (a-b) % 3 == 0 else 0)
say("cover: V = %d, E = %d, F = %d, chi = %d" % (NGc, 3*E, 3*F, chic))
Lc, Rc = build_sides(nfc, NGc, trLEc, trLEc, trLBc, chic)
ok_cov = report_identity("cover: det(cubic)*det(I+L_B u) = (1-u^3)^chi det det", Lc, Rc)
Lcalt = add(logdet_cubic(nfc, NGc), logdet_I_minus_uM(trLBc, M_ORDER, 1, +1))
report_identity("cover variant: det(I - L_B u)", Lcalt, Rc)
diffc = sub(Lc, add(logdet_I_minus_uM(trLEc, M_ORDER, 1, +1),
                    logdet_I_minus_uM(trLEc, M_ORDER, 2, +1)))
ac, cc, okc = fit_euler(diffc)
say("  cover fit: a = %s, c = %s, consistent: %s   (chi_cover = %d)" % (ac, cc, okc, chic))


# ================================================================ STEP 3e
hdr("STEP 3e.  Cross-checks requested by the prover (T0.3/T0.4, T2.4)")

say("(i) the UNRESTRICTED ordered edge rule is not Kang-Li's L_E.")
unres = [sum(1 for z in (S1+S2)
             if z != pgl_inv(S1[u])                     # z != x (no backtracking)
             and pgl_mul(S1[u], z) not in S1set | S2set # {x,y,z} not a 2-cell
             ) for u in range(13)]
say("    out-degree of the unrestricted rule (z any neighbour of y, {x,y,z} not a cell):",
    sorted(set(unres)), " (2q^2+q = %d)" % (2*q*q+q))
say("    Kang-Li's rule keeps only colour-1 continuations: out-degree q^2 = 9 (above).")
say("    Colour-2 edges are the reversals of colour-1 edges and have algebraic length 2,")
say("    which is the det(I - (L_E)^t u^2) factor.")

say()
say("(ii) all 6 orderings of a chamber: T_2 = L_B (+) L_B-reversed, so")
say("     det(I + u T_2) = det(I + u L_B)^2.")
SS = S1set | S2set
ordstates = []
for a_ in S1+S2:
    for b_ in S1+S2:
        ab = pgl_mul(a_, b_)
        if ab in SS:
            ordstates.append((a_, b_))
say("     ordered pointed 2-cells per vertex:", len(ordstates), " (= 6F/|G| = %d)" % (6*F//NG))
os_idx = {c: n for n, c in enumerate(ordstates)}
NO = len(ordstates)
rowsT, colsT = [], []
for n, (a_, b_) in enumerate(ordstates):
    forb = pgl_inv(pgl_mul(a_, b_))
    for c_ in S1+S2:
        if pgl_mul(b_, c_) not in SS or c_ == forb:
            continue
        rowsT.append(np.arange(NG)*NO + n)
        colsT.append(perm_of[a_]*NO + os_idx[(b_, c_)])
T2 = sp.csr_matrix((np.ones(len(rowsT)*NG, dtype=np.int64),
                    (np.concatenate(rowsT), np.concatenate(colsT))),
                   shape=(NG*NO, NG*NO))
say("     T_2: %d states, out-degree %d" % (NG*NO, T2.nnz//(NG*NO)))
trT2 = traces_by_symmetry(T2, NO, list(range(NO)), M_ORDER)
say("     Tr(T_2^m) == 2 Tr(L_B^m) for m = 1..%d:" % M_ORDER,
    all(trT2[m] == 2*trLB[m] for m in range(1, M_ORDER+1)))
say("     => det(I + u T_2) = det(I + u L_B)^2  (verified through u^%d)" % M_ORDER)

say()
say("(iii) T2.4: the boundary of a tetrahedron (not a building quotient).")
tetV = [0, 1, 2, 3]
tetE = [(i, j) for i in tetV for j in tetV if i != j]
tet2cells = set(frozenset(c) for c in itertools.combinations(tetV, 3))
t1nnz = 0
for (x, y) in tetE:
    for (y2, z) in tetE:
        if y2 != y or z == x:
            continue
        if frozenset({x, y, z}) not in tet2cells:      # geodicity
            t1nnz += 1
say("     T_1 has %d transitions (every triple of distinct vertices is a 2-cell):"
    % t1nnz, t1nnz == 0)
tord = [(a_, b_, c_) for a_ in tetV for b_ in tetV for c_ in tetV
        if len({a_, b_, c_}) == 3]
ti = {t: n for n, t in enumerate(tord)}
Ttet = np.zeros((len(tord), len(tord)), dtype=np.int64)
for (a_, b_, c_) in tord:
    for w_ in tetV:
        if w_ in (b_, c_) or w_ == a_:
            continue
        Ttet[ti[(a_, b_, c_)], ti[(b_, c_, w_)]] = 1
say("     ordered 2-cells: %d, out-degree %s" % (len(tord), sorted(set(Ttet.sum(1)))))
cyc, seen_ = [], set()
for n in range(len(tord)):
    if n in seen_:
        continue
    L_ = 0; m_ = n
    while m_ not in seen_:
        seen_.add(m_); L_ += 1; m_ = int(np.flatnonzero(Ttet[m_])[0])
    cyc.append(L_)
say("     T_2 is a permutation with cycle type", sorted(cyc),
    "=> det(I + u T_2) = (1 - u^4)^%d" % sum(1 for L_ in cyc if L_ == 4))
say("     matches the prover's (1-u^4)^6:", sorted(cyc) == [4]*6)

# ================================================================ STEP 4
hdr("STEP 4.  RH by factor")

say("Kang-Li-Wang Thm 2 (0809.1401v1:1352-1370): X Ramanujan <=>")
say("  nontrivial zeros of det(I-A_1u+qA_2u^2-q^3u^3) on |u| = q^{-1}")
say("  <=> nontrivial zeros of det(I-L_E u) on |u| in {q^{-1}, q^{-1/2}}")
say("  <=> nontrivial zeros of det(I+L_B u) on |u| in {1, q^{-1/2}, q^{-1/4}}.")
say("In eigenvalue terms: |lambda(L_E)| in {q, q^{1/2}} = {3, 1.7320508} (nontrivial),")
say("and |lambda(L_B)| in {1, q^{1/4}, q^{1/2}} = {1, 1.3160740, 1.7320508}  [u = -1/lambda].")

say()
say("(a) growth of the exact traces (verified numbers, indicated conclusion):")
for m in range(6, M_ORDER+1):
    say("   m=%2d  |Tr L_E^m|^(1/m) = %.6f    |Tr L_B^m|^(1/m) = %s"
        % (m, abs(trLE[m])**(1.0/m),
           ("%.6f" % (abs(trLB[m])**(1.0/m))) if trLB[m] else "  0"))

say()
say("(b) sub-leading exponent for L_E.  X_Gamma has exactly one trivial eigenvalue")
say("    of A_1, so L_E has exactly one eigenvalue of modulus q^2 = 9.  Subtract it")
say("    and divide by q^m = 3^m: a bounded, oscillating sequence <=> |lambda| = q")
say("    is the sub-leading modulus, i.e. the RH exponent 1/2 in |u| = q^{-1}.")
for m in range(6, M_ORDER+1):
    r = (trLE[m] - q**(2*m)) / float(q**m)
    say("    m=%2d  (Tr L_E^m - q^{2m}) / q^m = %18.6f   |.|^(1/m) = %.6f"
        % (m, r, abs(r)**(1.0/m) if r else 0.0))

say()
say("(c) largest-modulus eigenvalues of L_E and L_B (ARPACK, verified numerically):")
t = time.time()
try:
    evE = spla.eigs(LE.astype(float), k=40, which='LM', maxiter=20000,
                    tol=1e-10, return_eigenvectors=False)
    evE = evE[np.argsort(-np.abs(evE))]
    say("   |lambda(L_E)| top 40:", np.round(np.abs(evE), 6).tolist())
except Exception as ex:
    say("   ARPACK on L_E failed:", ex)
say("   (%.1f s)" % (time.time()-t))
say("   (ARPACK is not used for L_B: its spectrum sits on circles of radius 1,")
say("    q^{1/2} and q^{1/4} with enormous degeneracies and it does not converge.")
say("    L_B is handled exactly, block by block, in step 5b below.)")
say("   reference moduli: q^2 = %d, q = %d, q^{1/2} = %.6f, q^{1/4} = %.6f, 1"
    % (q*q, q, q**0.5, q**0.25))

# ================================================================ STEP 5
hdr("STEP 5.  The twisted (quantum) version: pi = 12-dim irrep of PGL_3(F_3)")

# P^2(F_3): 13 points
pts = []
for v in itertools.product(range(3), repeat=3):
    if v == (0, 0, 0):
        continue
    f = np.array(v) % 3
    nz = int(np.flatnonzero(f)[0])
    s = 1 if f[nz] == 1 else 2
    c = tuple(int(x) for x in (f*s) % 3)
    if c not in pts:
        pts.append(c)
pt_idx = {p: i for i, p in enumerate(pts)}
say("|P^2(F_3)| =", len(pts))

def permrep(g):
    Am = np.array(g, dtype=np.int64).reshape(3, 3)
    Pm = np.zeros((13, 13))
    for i, p in enumerate(pts):
        w = (Am @ np.array(p, dtype=np.int64)) % 3
        nz = int(np.flatnonzero(w)[0]); s = 1 if w[nz] == 1 else 2
        Pm[pt_idx[tuple(int(x) for x in (w*s) % 3)], i] = 1.0
    return Pm

# orthonormal basis of 1^perp
Wfull = np.linalg.qr(np.concatenate([np.ones((13, 1))/np.sqrt(13),
                                     np.eye(13)[:, :12]], axis=1))[0]
Wc = Wfull[:, 1:13]
assert abs(Wc.T @ np.ones(13)).max() < 1e-12

PI1 = [Wc.T @ permrep(s) @ Wc for s in S1]
PI2 = [Wc.T @ permrep(s) @ Wc for s in S2]
say("pi(s) orthogonal to 1e-12:",
    max(np.abs(p @ p.T - np.eye(12)).max() for p in PI1) < 1e-12)

def chan(PIs):
    Mm = np.zeros((144, 144))
    for p in PIs:
        Mm += np.kron(p, p)          # pi real => conj(pi) = pi
    return Mm/13.0

Ph1, Ph2 = chan(PI1), chan(PI2)
say("[Phi_1, Phi_2] = 0 :", np.abs(Ph1 @ Ph2 - Ph2 @ Ph1).max() < 1e-10)
vecI = np.eye(12).reshape(-1)/np.sqrt(12)
say("unital  (Phi_k(I) = I):", np.abs(Ph1 @ vecI - vecI).max() < 1e-12,
    np.abs(Ph2 @ vecI - vecI).max() < 1e-12)
say("trace preserving (Phi_k^dagger(I) = I):",
    np.abs(Ph1.T @ vecI - vecI).max() < 1e-12,
    np.abs(Ph2.T @ vecI - vecI).max() < 1e-12)
mu = np.linalg.eigvals(Ph1)
mu = mu[np.argsort(-np.abs(mu))]
say("Phi_1 spectrum: largest |mu| =", np.round(np.abs(mu[:6]), 8).tolist())
nontriv = np.abs(mu - 1.0) > 1e-9
say("number of eigenvalues equal to 1:", int((~nontriv).sum()))
mun = mu[nontriv]
say("largest nontrivial |mu| = %.9f   ->  |13 mu| = %.9f"
    % (np.abs(mun).max(), 13*np.abs(mun).max()))
say("classical Ramanujan bound for A_1 on \\tilde A_2 (deltoid radius) 3q = %d" % (3*q))
say("Hastings / quantum-Ramanujan bound 2 sqrt(D-1)/D with D = 13: %.9f  (|13 mu| <= %.6f)"
    % (2*np.sqrt(12)/13, 2*np.sqrt(12)))
dq_ = np.array([tempered_defect(13*m) for m in mun])
say("max temperedness defect of (13 mu, 13 conj mu) over the %d nontrivial modes: %.3e"
    % (len(mun), dq_.max()))
say("=> Ramanujan quantum expander of type \\tilde A_2 (all joint eigenvalues in the deltoid):",
    bool(dq_.max() < 1e-8))
say("NOTE: Phi_1 = (1/13) sum_s pi(s) (x) conj(pi(s)) is exactly A_1^{(pi (x) pi-bar)}/13,")
say("  so 13*spec(Phi_1) is a sub-multiset of spec(A_1) on C[G]: Ramanujan complex")
say("  => Ramanujan quantum expander, automatically.")
say("  check: every 13*mu is an eigenvalue of A_1 on C[G]:",
    bool(max(min(abs(13*m - lam)) for m in mu) < 1e-6))

# --- blockwise zeta identity for the representation nu = 1 + pi -----------
hdr("STEP 5b.  Blockwise (representation-twisted) Kang-Li identity")

NU = [permrep(s) for s in S1]                 # 13-dim integer permutation rep
NUi = [permrep(s) for s in S2]

def block_traces(n_out, build, M=M_ORDER):
    Mm = build()
    P_ = np.eye(Mm.shape[0], dtype=np.int64)
    out = [0]*(M+1)
    for m in range(1, M+1):
        P_ = P_ @ Mm
        out[m] = int(np.trace(P_))
    return out

def LE_block(reps, dt=np.int64):
    D = reps[0].shape[0]
    Mm = np.zeros((13*D, 13*D), dtype=dt)
    for u in range(13):
        R = np.array(np.round(reps[u]), dtype=dt) if dt is np.int64 else np.asarray(reps[u])
        for t in allowed[u]:
            Mm[u*D:(u+1)*D, t*D:(t+1)*D] += R
    return Mm

def LB_block(reps, dt=np.int64):
    D = reps[0].shape[0]
    Mm = np.zeros((52*D, 52*D), dtype=dt)
    for n, (i, j) in enumerate(CH):
        k = kmap[(i, j)]
        sh = reps[i] @ reps[j]
        sh = np.array(np.round(sh), dtype=dt) if dt is np.int64 else np.asarray(sh)
        for tp in succ_pairs[j]:
            if tp == k:
                continue
            m = i_of[pgl_inv(pgl_mul(S1[j], S1[tp]))]
            n2 = ch_of[(tp, m)]
            Mm[n*D:(n+1)*D, n2*D:(n2+1)*D] += sh
    return Mm

def A_block_traces(reps1, reps2, M=M_ORDER):
    D = reps1[0].shape[0]
    A1b = sum(np.round(r).astype(np.int64).astype(object) for r in reps1)
    A2b = sum(np.round(r).astype(np.int64).astype(object) for r in reps2)
    out = {}
    Xa = np.eye(D, dtype=object)
    for a in range(M+1):
        Xb = Xa
        for b in range(M+1-a):
            out[(a, b)] = int(np.trace(Xb))
            Xb = Xb @ A2b
        Xa = Xa @ A1b
    return out

# the 13 lines of P^2(F_3) give a second 13-point permutation representation
lines = []
for a in pts:                       # a line is the kernel of a functional
    v = np.array(a, dtype=np.int64)
    ker = tuple(sorted(i for i, p in enumerate(pts)
                       if int(v @ np.array(p, dtype=np.int64)) % 3 == 0))
    lines.append(ker)
ln_idx = {L: i for i, L in enumerate(lines)}
say("|lines of P^2(F_3)| = %d, each with %d points" % (len(lines), len(lines[0])))

def linerep(g):
    Am = np.array(g, dtype=np.int64).reshape(3, 3)
    Pm = np.zeros((13, 13))
    for i, L in enumerate(lines):
        img = set()
        for pi in L:
            w = (Am @ np.array(pts[pi], dtype=np.int64)) % 3
            nz = int(np.flatnonzero(w)[0]); sc = 1 if w[nz] == 1 else 2
            img.add(pt_idx[tuple(int(x) for x in (w*sc) % 3)])
        Pm[ln_idx[tuple(sorted(img))], i] = 1.0
    return Pm

NUL  = [linerep(s) for s in S1]
NULi = [linerep(s) for s in S2]
say("point-rep and line-rep characters equal (so pi ~ pi'):",
    all(abs(np.trace(permrep(s)) - np.trace(linerep(s))) < 1e-9 for s in S1+S2))

say()
say("Bookkeeping (prover T5.5/T5.6, folded in):")
say("  * The full-complex twist E_{(g,gs)} = rho(s) is NOT flat: flatness on the")
say("    triangle g,gs,gst asks rho(t)rho(s) = rho(st).  Checked on a sample:")
PIof = {S1[i]: PI1[i] for i in range(13)}
bad_flat = sum(1 for (i, j, k) in P_triples
               if np.abs(PI1[j] @ PI1[i] - PIof.get(pgl_mul(S1[i], S1[j]),
                                                    PI1[i] @ PI1[j])).max() > 1e-9)
say("    chambers (g,gs,gst) where rho(t)rho(s) != rho(st), out of %d:" % len(P_triples),
    bad_flat)
say("  * The covariant weights E_{(g,gs)} = rho(s^{-1}) ARE pure gauge (F_g = rho(g^{-1})),")
say("    so det(I - u T_E^rho) = det(I - u L_E)^{dim rho} on the FULL complex.  Reason,")
say("    verified structurally: every closed straight walk of the full complex returns")
say("    to its own directed edge, hence s_1...s_m = e and the holonomy is trivial;")
say("    this is exactly the condition our trace computation enumerates.")
say("  * The genuine Artin object is the VOLTAGE QUOTIENT (T5.6): states = the 13")
say("    colour-1 edges at the identity vertex, arrow (e,u) -> (e,t) with voltage")
say("    h = b_u and a fibre weight rho(h^{+-1}) (sign fixed by the composition order,")
say("    see the convention note below).  That is what the blocks below are.")
say("  * These blocks ARE the isotypic blocks: for rho = the regular representation")
say("    the construction returns L_E itself (index identity (u,g),(t,h) <-> (g,u),(h,t)),")
say("    so Tr(L_E^m) = sum_rho dim(rho) Tr(L_E^{(rho)m}).")

say("  * Convention: in our matrix layout the weights are multiplied in PATH order,")
say("    so the fibre weight of the arrow with voltage h must be rho(h); the trace of")
say("    a closed quotient walk is then chi_rho(holonomy), a class function, which is")
say("    the Artin/Ihara L-function.  T5.6's rho(h^{-1}) is the same block written for")
say("    the opposite composition order (equivalently for rho^vee); nu has a real")
say("    character, so the two give the same determinant.  We verify the block")
say("    construction directly against the holonomy sum below.")

# --- direct verification: Tr(T_nu^m) = sum over closed quotient walks of chi_nu(holonomy)
chi_nu = np.array([float(np.trace(permrep(g))) for g in elts])
def holonomy_trace(Mat, nstates, starts, M, chivec, blocksz):
    out = [0.0]*(M+1)
    for st in starts:
        v = np.zeros(Mat.shape[0], dtype=np.int64); v[st] = 1
        for m in range(1, M+1):
            v = Mat.T @ v
            vv = v.reshape(NG, blocksz)[:, st]
            out[m] += float(vv @ chivec)
    return out
hol_E = holonomy_trace(LE, NE, list(range(13)), 8, chi_nu, 13)
say("  * check Tr(T_nu^m) = sum_{closed quotient walks} chi_nu(holonomy), m = 1..8:")
_chk = block_traces(13*13, lambda: LE_block(NU))
say("      holonomy sum :", [int(round(x)) for x in hol_E[1:9]])
say("      block trace  :", _chk[1:9])
say("      agree:", all(abs(hol_E[m]-_chk[m]) < 1e-6 for m in range(1, 9)))
hol_B = holonomy_trace(LB, NB, list(range(52)), 9, chi_nu, 52)
_chkB = block_traces(52*13, lambda: LB_block(NU))
say("  * same for the chamber operator, m = 1..9:")
say("      holonomy sum :", [int(round(x)) for x in hol_B[1:10]])
say("      block trace  :", _chkB[1:10])
say("      agree:", all(abs(hol_B[m]-_chkB[m]) < 1e-6 for m in range(1, 10)))
say("  * contrast with the gauge-trivial FULL twist, whose trace is dim(rho)*Tr(L_E^m):")
say("      dim(nu)*Tr(L_E^m)/|G| , m=1..8 :",
    [13*trLE[m]//NG for m in range(1, 9)])
say("      nu-block (voltage quotient), m=1..8 :", _chk[1:9])
say("    they differ, as they must: the quotient carries nontrivial holonomy.")

blocks = [("trivial rep, dim 1", [np.ones((1, 1))]*13, [np.ones((1, 1))]*13, 1),
          ("nu = 1 + pi (points), dim 13", NU, NUi, 13),
          ("nu' = 1 + pi' (lines), dim 13", NUL, NULi, 13)]
ck_store = {}
for label, reps1, reps2, dimr in blocks:
    say()
    say("--- block: %s" % label)
    t = time.time()
    trEb = block_traces(13*dimr, lambda: LE_block(reps1))
    trBb = block_traces(52*dimr, lambda: LB_block(reps1))
    nb = A_block_traces(reps1, reps2)
    say("    Tr(L_E^m), m=1..8:", trEb[1:9])
    say("    Tr(L_B^m), m=1..8:", trBb[1:9])
    Lb = add(logdet_cubic(lambda a, b: nb[(a, b)], 1),
             logdet_I_minus_uM(trBb, M_ORDER, 1, -1))
    Rb0 = add(logdet_I_minus_uM(trEb, M_ORDER, 1, +1),
              logdet_I_minus_uM(trEb, M_ORDER, 2, +1))
    dif = sub(Lb, Rb0)
    a_b, c_b, ok_b = fit_euler(dif)
    say("    Euler factor F_rho(u) = (1-u)^a (1-u^3)^c :  a = %s, c = %s, consistent: %s"
        % (a_b, c_b, ok_b))
    say("    naive fractional guess (chi/|G|)*dim = %s (T5.7 says it must NOT be asserted"
        % str(Fraction(chi, NG)*dimr))
    say("     when the deck group has 2-cell stabilisers, which it does here)")
    say("    residual series (u^1..u^9):", [str(x) for x in dif[1:10]])
    ck_store[label] = (a_b, c_b)
    say("    (%.1f s)" % (time.time()-t))

say()
say("pi-block (dim 12) = nu-block minus trivial block (T5.6 convention):")
a_t, c_t = ck_store["trivial rep, dim 1"]
a_n, c_n = ck_store["nu = 1 + pi (points), dim 13"]
say("   trivial:  a = %s, c = %s" % (a_t, c_t))
say("   nu:       a = %s, c = %s" % (a_n, c_n))
say("   pi:       a = %s, c = %s" % (a_n-a_t, c_n-c_t))
say("   naive (chi/|G|)*12 = %s" % str(Fraction(chi, NG)*12))
say("   Consistency with the full complex requires sum_rho d_rho a_rho = 0 and")
say("   sum_rho d_rho c_rho = chi = %d; the two blocks we can build give partial sums" % chi)
say("   d_1 a_1 + d_pi a_pi = %s, d_1 c_1 + d_pi c_pi = %s"
    % (str(a_t + 12*(a_n-a_t)), str(c_t + 12*(c_n-c_t))))
say("   point-rep and line-rep blocks agree:",
    ck_store["nu = 1 + pi (points), dim 13"] == ck_store["nu' = 1 + pi' (lines), dim 13"])

# --- exact polynomial identity on the trivial block --------------------------
say()
say("Exact polynomial check on the trivial block (no truncation):")
import sympy as spy
uu = spy.symbols('u')
LEt_ = LE_block([np.ones((1, 1))]*13)
LBt_ = LB_block([np.ones((1, 1))]*13)
def dImuM(Mint):
    Mx = spy.Matrix(np.asarray(Mint, dtype=np.int64).tolist())
    n = Mx.shape[0]
    co = Mx.charpoly(spy.Symbol('x')).all_coeffs()      # c_n x^n + ... + c_0
    # det(I - uM) = sum_k c_k u^{n-k} with charpoly det(xI-M) = sum c_k x^k
    return spy.Poly(sum(co[::-1][k]*uu**(n-k) for k in range(n+1)), uu)
P3t = spy.Poly(1 - 13*uu + 39*uu**2 - 27*uu**3, uu)
lhs = P3t * dImuM(-LBt_)
rhs = spy.Poly((1-uu)**int(a_t)*(1-uu**3)**int(c_t), uu) * dImuM(LEt_) \
      * spy.Poly(dImuM(LEt_.T).as_expr().subs(uu, uu**2), uu)
say("   deg LHS = %d, deg RHS = %d" % (lhs.degree(), rhs.degree()))
say("   det(P_3) det(I+uL_B) = (1-u)^%s (1-u^3)^%s det(I-uL_E) det(I-u^2 L_E^t)  EXACTLY: %s"
    % (a_t, c_t, spy.simplify((lhs - rhs).as_expr()) == 0))

# ---------------------------------------------------------------- RH by block
hdr("STEP 5c.  RH by factor, verified exactly on the blocks we can build")

def block_report(name, reps1, reps2):
    D = reps1[0].shape[0]
    A1b = sum(np.asarray(r) for r in reps1)
    evA = np.linalg.eigvals(A1b)
    dfe = np.array([tempered_defect(l) for l in evA])
    triv = np.abs(np.abs(evA) - 13.0) < 1e-8
    say("  %s: A_1 block %dx%d" % (name, D, D))
    say("     |lambda(A_1)| =", np.round(np.sort(np.abs(evA))[::-1], 6).tolist())
    if (~triv).sum():
        say("     max temperedness defect (nontrivial): %.3e" % dfe[~triv].max())
    E_ = LE_block(reps1, dt=float); B_ = LB_block(reps1, dt=float)
    eE = np.linalg.eigvals(E_); eB = np.linalg.eigvals(B_)
    aE = np.abs(eE); aB = np.abs(eB)
    aE = aE[aE > 1e-9]; aB = aB[aB > 1e-9]
    vE, cE = np.unique(np.round(aE, 6), return_counts=True)
    vB, cB = np.unique(np.round(aB, 6), return_counts=True)
    say("     |lambda(L_E)| (nonzero) values/multiplicities:",
        list(zip(vE.tolist(), cE.tolist())))
    say("        predicted: q^2 = 9 (trivial), then q = 3 and q^{1/2} = %.6f" % q**0.5)
    say("     |lambda(L_B)| (nonzero) values/multiplicities:",
        list(zip(vB.tolist(), cB.tolist())))
    say("        predicted (KLW Thm 2(4), |u| in {1, q^{-1/2}, q^{-1/4}}):")
    say("        1, q^{1/4} = %.6f, q^{1/2} = %.6f  (+ the trivial q = 3)"
        % (q**0.25, q**0.5))

block_report("trivial", [np.ones((1, 1))]*13, [np.ones((1, 1))]*13)
block_report("pi (12-dim)", PI1, PI2)
say()
say("These are exact spectra of genuine isotypic blocks, so the radii above are")
say("VERIFIED for the trivial and the 12-dimensional isotypic components of")
say("L^2(edges) and L^2(directed chambers); for the remaining components they are")
say("INDICATED by the full-space ARPACK run on L_E and by KLW Theorem 2 applied to")
say("the fully verified statement (2) about the A_1 spectrum.")

say()
say("Total elapsed: %.1f s" % (time.time()-T0))
