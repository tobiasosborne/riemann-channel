#!/usr/bin/env python3
"""cerednik_drinfeld.py -- numerics lane for `notes/cerednik-drinfeld/astra-proofs.md` (CD2, CD3).

Author line: claude:fable-5.1 (numerics fork).  Independent of the prover's `checks/` (not read).
The (13,17;5) LPS square complex is rebuilt from the quaternion sets exactly as in
`scripts/lps_square_complex.py` (construction copied, not imported, so that this script is
self-contained and deterministic).  Every claim is a `check(cond, msg)`; a failing check is
recorded and the run continues.  Exact arithmetic (python ints / sympy over ZZ) wherever the
claim is exact; floating point only for eigenvalue diagnostics, which are labelled as such.

What is tested (CD2/CD3 of the prover's note):
  * the worked example's integral cycle basis Z (identity root, BFS tree with neighbours in
    vertex order, chords in edge order): 840 x 721, boundary zero, chord rows = I_721;
  * M = Z^t Z = I + Z_tree^t Z_tree  (so M >= I exactly), positivity;
  * det M exactly, by Sylvester det(I_721 + Z_t^t Z_t) = det(I_119 + Z_t Z_t^t) (Bareiss, ints),
    against the number of spanning trees tau(Y) from the reduced Laplacian (Bareiss) and from
    the closed spectral formula 28*10^34*18^34*12^25*16^25/120; factorisation 2^217 3^92 5^33 7;
  * Smith normal form: coker(I + AB) = coker(I + BA) (unimodular block equivalence), so the
    invariant factors of M are those of the 119 x 119 matrix I + Z_t Z_t^t padded with ones;
    compared with the Smith form of the reduced Laplacian (critical group);
  * L = chord rows of T_1 Z, T_1 Z = Z L and L^t M = M L exactly; chi_L = chi_T (spectrum);
  * the T_17 action on the component group: (A_17 - 18) on the critical group, the rational
    solution of Q x = (A_17 - 18)(e_0 - e_id) with x_id = 0 (x_0 = -364/135 claimed), and the
    order of the image of A_17 - 18 on the critical group;
  * the bipartite sign S = eps(tail) on directed edges: S R = -R S, S T_D = -T_D S, S preserves
    the new space; the two-copy cover splits into two connected 120-vertex copies;
  * companion forms: F^t Omega_M F = 17 Omega_M, F^t (2 G_M) F = 17 (2 G_M) exactly; G_M > 0
    (Schur complement M(17 - L^2/4), generalised eigenvalues of L; rank_103(T_1^2 - 68) = 840);
    reversal sector spectra;
  * the completed Bass zeta: N_n = 1 + 17^n - Tr F^n for n = 1..6 against the worked example,
    and the point-count predictions #C(F_17) = 0, #C(F_289) = 11520.
"""
import sys, time
from itertools import product
from fractions import Fraction
import numpy as np
import sympy
from sympy import Matrix, ZZ, factorint
from sympy.matrices.normalforms import smith_normal_form

T0 = time.time()
LEDGER = []
def check(cond, msg):
    tag = "D%02d" % (len(LEDGER) + 1)
    LEDGER.append((tag, bool(cond), msg))
    print("%s %s %s" % (tag, "PASS" if cond else "FAIL", msg)); sys.stdout.flush()
    return bool(cond)

# ---------------------------------------------------------------- quaternions, PGL_2(F_5), graphs (as in lps_square_complex.py)
def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)
def qconj(a): return (a[0], -a[1], -a[2], -a[3])
def qnormalise_sign(a):
    for x in a:
        if x != 0: return a if x > 0 else tuple(-y for y in a)
    return a
def gens(p):
    r = int(p**0.5) + 1; out = []
    for a0 in range(1, r + 1, 2):
        for a1, a2, a3 in product(range(-r, r + 1), repeat=3):
            if a1 % 2 or a2 % 2 or a3 % 2: continue
            if a0*a0 + a1*a1 + a2*a2 + a3*a3 == p: out.append((a0, a1, a2, a3))
    return sorted(out)
S13, S17 = gens(13), gens(17)
P = 5
def mnorm(m):
    m = tuple(x % P for x in m)
    for x in m:
        if x:
            inv = pow(x, P - 2, P); return tuple((y * inv) % P for y in m)
    raise ValueError
def mmul(m, n):
    return mnorm((m[0]*n[0] + m[1]*n[2], m[0]*n[1] + m[1]*n[3], m[2]*n[0] + m[3]*n[2], m[2]*n[1] + m[3]*n[3]))
VERTS = sorted({mnorm(m) for m in product(range(P), repeat=4) if (m[0]*m[3] - m[1]*m[2]) % P})
VIDX = {v: i for i, v in enumerate(VERTS)}; NV = len(VERTS)
def phi(a):
    a0, a1, a2, a3 = a
    return mnorm((a0 + 2*a1, a2 + 2*a3, -a2 + 2*a3, a0 - 2*a1))
IDV = VIDX[mnorm((1, 0, 0, 1))]
def build_colour(S):
    n = len(S); head = np.zeros((NV, n), dtype=int)
    for v in range(NV):
        for si, s in enumerate(S): head[v, si] = VIDX[mmul(VERTS[v], phi(s))]
    conj_idx = [S.index(qconj(s)) for s in S]
    und = -np.ones((NV, n), dtype=int); sgn = np.zeros((NV, n), dtype=int); canon = []
    for v in range(NV):
        for si in range(n):
            if und[v, si] >= 0: continue
            w, ti = head[v, si], conj_idx[si]; assert head[w, ti] == v
            k = len(canon); canon.append((v, si)); und[v, si], sgn[v, si] = k, 1; und[w, ti], sgn[w, ti] = k, -1
    return head, und, sgn, canon, conj_idx
H13, U13, G13, C13, CJ13 = build_colour(S13)
H17, U17, G17, C17, CJ17 = build_colour(S17)
NE_H = len(C13)
def adjacency(head):
    A = np.zeros((NV, NV), dtype=np.int64)
    for v in range(NV):
        for w in head[v]: A[v, w] += 1
    return A
A13, A17 = adjacency(H13), adjacency(H17)
check(NV == 120 and NE_H == 840 and len(C17) == 1080 and IDV == 20,
      "120 vertices, 840 horizontal and 1080 vertical edges; identity vertex has lexicographic index %d (prover: 20)" % IDV)
# bipartition sign eps(g) = (det g / 5) Legendre symbol on the normalised representative
def legendre5(x): return 0 if x % 5 == 0 else (1 if pow(x, 2, 5) == 1 else -1)
EPS = np.array([legendre5(v[0]*v[3] - v[1]*v[2]) for v in VERTS], dtype=np.int64)
check(all(EPS[H13[v, si]] == -EPS[v] for v in range(NV) for si in range(14)) and all(EPS[H17[v, si]] == -EPS[v] for v in range(NV) for si in range(18)),
      "eps(g) = (det g/5) changes sign along every horizontal and every vertical edge (13, 17 nonsquares mod 5)")
# reordering rules
prod_ab = {}
for ai, a in enumerate(S13):
    for bi, b in enumerate(S17): prod_ab[(ai, bi)] = qnormalise_sign(qmul(a, b))
prod_ba = {}
for bi, b in enumerate(S17):
    for ai, a in enumerate(S13): prod_ba.setdefault(qnormalise_sign(qmul(b, a)), []).append((bi, ai))
RULE = {}
uniq = True
for key, val in prod_ab.items():
    lst = prod_ba.get(val, [])
    if len(lst) != 1: uniq = False
    else: RULE[key] = lst[0]
check(uniq and len(RULE) == 252, "252 unique reordering rules")

# ---------------------------------------------------------------- D, T_1 on canonical horizontal edges
D = np.zeros((NE_H, NV), dtype=np.int64)
for k, (v, si) in enumerate(C13): D[k, v] -= 1; D[k, H13[v, si]] += 1
T1 = np.zeros((NE_H, NE_H), dtype=np.int64)
for k, (g, ai) in enumerate(C13):
    for bi in range(18):
        bpi, api = RULE[(ai, bi)]; gb = H17[g, bpi]
        T1[k, U13[gb, api]] += G13[gb, api]
check((T1 == T1.T).all() and not (T1 @ D - D @ A17).any(), "T_1 symmetric and T_1 D = D A_17 exactly")

# ---------------------------------------------------------------- the worked example's integral cycle basis Z
# BFS from the identity vertex; neighbours ordered by vertex label; tree edge to a vertex = the first
# horizontal edge (in that order) reaching it.  Chords = the remaining 721 canonical edges, in edge order.
parent = -np.ones(NV, dtype=int); parent_edge = -np.ones(NV, dtype=int); parent_sign = np.zeros(NV, dtype=int)
order = [IDV]; seen = {IDV}; qi = 0
while qi < len(order):
    v = order[qi]; qi += 1
    nbrs = sorted((int(H13[v, si]), si) for si in range(14))
    for w, si in nbrs:
        if w not in seen:
            seen.add(w); order.append(w); parent[w] = v
            parent_edge[w] = U13[v, si]; parent_sign[w] = G13[v, si]   # canonical edge id, +1 if canonical orientation is v -> w
tree_edges = sorted(set(int(e) for e in parent_edge if e >= 0))
chords = [e for e in range(NE_H) if e not in set(tree_edges)]
check(len(seen) == NV and len(tree_edges) == 119 and len(chords) == 721, "BFS spanning tree: 119 tree edges, 721 chords")
def tree_path_vector(v):
    """vector in Z^840 of the tree path from the root to v (canonical orientations, signed)"""
    x = np.zeros(NE_H, dtype=np.int64)
    while v != IDV:
        x[parent_edge[v]] += parent_sign[v]; v = parent[v]
    return x
Z = np.zeros((NE_H, 721), dtype=np.int64)
for j, e in enumerate(chords):
    v, si = C13[e]; w = int(H13[v, si])      # canonical chord e: v -> w
    Z[e, j] = 1
    Z[:, j] += tree_path_vector(v) - tree_path_vector(w)   # chord followed by the tree path from w back to v
check(not (D.T @ Z).any(), "boundary of every cycle column is zero (D^t Z = 0 exactly)")
check((Z[chords, :] == np.eye(721, dtype=np.int64)).all(), "chord rows of Z form the identity I_721 (integral basis of the cycle lattice)")
Zt = Z[tree_edges, :]                          # 119 x 721
M = Z.T @ Z
check((M == np.eye(721, dtype=np.int64) + Zt.T @ Zt).all(), "M = Z^t Z = I + Z_tree^t Z_tree exactly, hence M >= I")
evM = np.linalg.eigvalsh(M.astype(float))
check(evM.min() > 1 - 1e-9, "M positive definite: smallest eigenvalue %.6f (>= 1 exactly), largest %.4f (float diagnostic)" % (evM.min(), evM.max()))

# ---------------------------------------------------------------- exact determinants (python ints, Bareiss)
def bareiss_det(A):
    A = [[int(x) for x in row] for row in A]; n = len(A); sign = 1; prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            sw = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if sw is None: return 0
            A[k], A[sw] = A[sw], A[k]; sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
        prev = A[k][k]
    return sign * A[n - 1][n - 1]
small = np.eye(119, dtype=np.int64) + Zt @ Zt.T          # 119 x 119
detM = bareiss_det(small.tolist())
Lap = np.diag(A13.sum(1)) - A13
red = [i for i in range(NV) if i != IDV]
tau = bareiss_det(Lap[np.ix_(red, red)].tolist())
tau_formula = (28 * 10**34 * 18**34 * 12**25 * 16**25) // 120
check(detM == tau, "det M = det(I_119 + Z_t Z_t^t) (Sylvester) equals the number of spanning trees tau(Y) from the reduced Laplacian: %d digits" % len(str(detM)))
check(tau == tau_formula, "tau(Y) equals the spectral formula 28*10^34*18^34*12^25*16^25/120 (spectrum +-14, +-4^34, +-2^25)")
fac = factorint(detM)
check(fac == {2: 217, 3: 92, 5: 33, 7: 1}, "det M = 2^217 3^92 5^33 7 (factorisation %s)" % dict(sorted(fac.items())))
# adjacency spectrum certificate used in the formula
A2 = A13 @ A13
ann = (A2 - 196*np.eye(NV, dtype=np.int64)) @ (A2 - 16*np.eye(NV, dtype=np.int64)) @ (A2 - 4*np.eye(NV, dtype=np.int64))
check(not ann.any() and int(np.trace(A2)) == 1680 and int(np.trace(A2 @ A2)) == 95040,
      "(A^2-196)(A^2-16)(A^2-4) = 0, tr A^2 = 1680, tr A^4 = 95040 (certifies multiplicities 1, 34, 25)")

# ---------------------------------------------------------------- Smith normal forms: coker(M) = coker(I + Z_t Z_t^t) = critical group
def snf_diag(Mint):
    S = smith_normal_form(Matrix(Mint.tolist()), domain=ZZ)
    d = [abs(int(S[i, i])) for i in range(min(S.shape))]
    return sorted(x for x in d if x != 1)
t1 = time.time()
inv_small = snf_diag(small)
inv_lap = snf_diag(Lap[np.ix_(red, red)])
check(inv_small == inv_lap, "invariant factors of I + Z_t Z_t^t (= those of M, by coker(I+AB) = coker(I+BA)) equal those of the reduced Laplacian (critical group): %d nontrivial factors, %.1fs" % (len(inv_small), time.time() - t1))
prodinv = 1
for x in inv_small: prodinv *= x
check(prodinv == detM, "product of the invariant factors equals det M")
print("   invariant factors (nontrivial):", inv_small)
print("   component group Phi_13 = " + " x ".join("Z/%d" % x for x in inv_small))
# p-rank consistency directly on the 721 x 721 M for the primes dividing det M
def rank_mod_p(A, p):
    A = (A % p).astype(np.int64).copy(); rows, cols = A.shape; r = 0
    for c in range(cols):
        nz = np.nonzero(A[r:, c])[0]
        if len(nz) == 0: continue
        piv = r + nz[0]
        if piv != r: A[[r, piv]] = A[[piv, r]]
        A[r] = (A[r] * pow(int(A[r, c]), p - 2, p)) % p
        below = r + 1 + np.nonzero(A[r + 1:, c])[0]
        if len(below): A[below] = (A[below] - np.outer(A[below, c], A[r])) % p
        r += 1
        if r == rows: break
    return r
prank_ok = True
for p in (2, 3, 5, 7):
    pr_M = 721 - rank_mod_p(M, p); pr_S = sum(1 for x in inv_small if x % p == 0)
    prank_ok &= (pr_M == pr_S)
    print("   p = %d: p-rank of coker(M) directly = %d, from the Smith form = %d" % (p, pr_M, pr_S))
check(prank_ok, "p-ranks of coker(M) computed directly on the 721x721 M agree with the Smith form for p = 2, 3, 5, 7")

# ---------------------------------------------------------------- L and Hecke symmetry
T1Z = T1 @ Z
L = T1Z[chords, :]                                # chord rows: T_1 Z = Z L with chord block I
check(not (T1Z - Z @ L).any(), "T_1 Z = Z L exactly (L = chord rows of T_1 Z)")
check(not (L.T @ M - M @ L).any(), "L^t M = M L exactly (T_17 is M-self-adjoint: the monodromy pairing is Hecke-symmetric)")
# spectrum of L = spectrum of T on K (generalised symmetric eigenproblem Z^t T_1 Z v = a M v)
from scipy.linalg import eigh, null_space
evL = eigh(Z.T @ T1 @ Z, M.astype(float), eigvals_only=True)
Vk = null_space(D.T.astype(float)); TK = Vk.T @ T1 @ Vk; evK = np.linalg.eigvalsh((TK + TK.T) / 2)
check(np.abs(np.sort(evL) - np.sort(evK)).max() < 1e-8 and abs(evL.sum() - 18) < 1e-8,
      "spec(L) = spec(T on K) (max dev %.1e), trace 18, max |a| = %.10f, min(17 - a^2/4) = %.10f" % (np.abs(np.sort(evL) - np.sort(evK)).max(), np.abs(evL).max(), (17 - evL**2 / 4).min()))
check(rank_mod_p(T1 @ T1 - 68 * np.eye(NE_H, dtype=np.int64), 103) == 840,
      "rank_103(T_1^2 - 68 I) = 840: +-2 sqrt17 are not eigenvalues even on all edge cochains (exact strictness certificate)")
print("   (rank mod 101 = %d, the prime the prover reports as unusable)" % rank_mod_p(T1 @ T1 - 68 * np.eye(NE_H, dtype=np.int64), 101))

# ---------------------------------------------------------------- the component-group action of T_17 - 18
# critical group model: Phi = Div^0(V)/Q Z^V with Q = 14 I - A_13; the induced correspondence is A_17.
Q = 14 * np.eye(NV, dtype=np.int64) - A13
d = np.zeros(NV, dtype=object); d[0] = 1; d[IDV] -= 1
rhs = (A17 - 18 * np.eye(NV, dtype=np.int64)).astype(object) @ d
# solve Q x = rhs with x_id = 0 exactly over Q (drop row/column IDV: Q_red x_red = rhs_red; rhs has zero sum)
Qred = Matrix(Q[np.ix_(red, red)].tolist()); rr = Matrix([int(rhs[i]) for i in red])
xred = Qred.LUsolve(rr)
x0 = xred[0]   # vertex 0 is red[0]
check(x0 == sympy.Rational(-364, 135), "Q x = (A_17 - 18)(e_0 - e_id), x_id = 0: x_0 = %s (prover: -364/135), not integral => (T_17 - 18)[e_0 - e_id] != 0 in Phi" % x0)
check(not all(v.q == 1 for v in xred), "the solution is non-integral (some denominator > 1): T_17 - 18 does not kill the component group")
# order of the image of (A_17 - 18) on the critical group: |Phi| / |coker [Q_red | (A_17-18)_red]|
Aug = np.concatenate([Q[np.ix_(red, red)], (A17 - 18 * np.eye(NV, dtype=np.int64))[np.ix_(red, red)]], axis=1)   # 119 x 238
# (A_17 - 18) e_v for v in red are degree-zero vectors; restricting to the rows `red` loses nothing since the
# row IDV is minus the sum of the others on Div^0; the column IDV of (A_17-18) is minus the sum of the other columns.
t2 = time.time()
Saug = smith_normal_form(Matrix(Aug.tolist()), domain=ZZ)
daug = [abs(int(Saug[i, i])) for i in range(119)]
coker_aug = 1
for x in daug: coker_aug *= x
img_order = detM // coker_aug if coker_aug else 0
check(coker_aug and detM % coker_aug == 0 and img_order > 1,
      "image of T_17 - 18 on the component group has order %s = det M / %s (%.1fs); cokernel of the augmented lattice has invariant factors %s" % (factorint(img_order) if img_order else 0, factorint(coker_aug), time.time() - t2, sorted(x for x in daug if x != 1)))

# ---------------------------------------------------------------- directed edges, reversal, bipartite sign, two-copy cover
ND = NV * 14
def didx(v, si): return v * 14 + si
TD = np.zeros((ND, ND), dtype=np.int64)
for g in range(NV):
    for ai in range(14):
        for bi in range(18):
            bpi, api = RULE[(ai, bi)]; TD[didx(g, ai), didx(H17[g, bpi], api)] += 1
R = np.zeros((ND, ND), dtype=np.int64)
for g in range(NV):
    for ai in range(14): R[didx(g, ai), didx(H13[g, ai], CJ13[ai])] = 1
S = np.diag(np.repeat(EPS, 14)).astype(np.int64)
check(not (S @ R + R @ S).any() and not (S @ TD + TD @ S).any() and not (TD @ R - R @ TD).any(),
      "S = eps(tail): S R = -R S, S T_D = -T_D S, [T_D, R] = 0 exactly on directed edges")
OLD = np.zeros((ND, 2 * NV), dtype=np.int64)
for g in range(NV):
    for ai in range(14): OLD[didx(g, ai), g] = 1; OLD[didx(g, ai), NV + H13[g, ai]] = 1
NEW = null_space(OLD.T.astype(float))
check(NEW.shape[1] == 1442 and np.abs(OLD.T @ (S @ NEW)).max() < 1e-9, "S preserves the 1442-dimensional new space")
Rn = NEW.T @ R @ NEW; wR, VR = np.linalg.eigh((Rn + Rn.T) / 2)
plus, minus = VR[:, wR > 0], VR[:, wR < 0]; Tn = NEW.T @ TD @ NEW
ev_plus = np.sort(np.linalg.eigvalsh(plus.T @ Tn @ plus)); ev_minus = np.sort(np.linalg.eigvalsh(minus.T @ Tn @ minus))
check(np.abs(ev_minus - np.sort(evK)).max() < 1e-8 and np.abs(ev_plus - np.sort(-evK)).max() < 1e-8,
      "the R = -1 new sector is K (spec T), the R = +1 sector has the reflected spectrum -spec T (traces %.6f, %.6f)" % (ev_minus.sum(), ev_plus.sum()))
# two-copy cover: vertices (g, s), s = +-1; an edge g -> g phi(a) lifts to (g, s) -> (g phi(a), -s) (both colours flip eps)
comp = {}
for g in range(NV):
    for s in (1, -1): comp[(g, s)] = 0 if s == EPS[g] else 1
cov_ok = True
for g in range(NV):
    for si in range(14): cov_ok &= comp[(g, 1)] == comp[(H13[g, si], -1)] and comp[(g, -1)] == comp[(H13[g, si], 1)]
    for si in range(18): cov_ok &= comp[(g, 1)] == comp[(H17[g, si], -1)] and comp[(g, -1)] == comp[(H17[g, si], 1)]
sizes = [sum(1 for k, c in comp.items() if c == i) for i in (0, 1)]
check(cov_ok and sizes == [120, 120], "the two-copy cover (g, +-) splits by +-eps(g) into two edge-closed copies of 120 vertices, exchanged by (g, s) -> (g, -s)")

# ---------------------------------------------------------------- companion forms, exact
I721 = np.eye(721, dtype=np.int64); Zr = np.zeros((721, 721), dtype=np.int64)
F = np.block([[L, -17 * I721], [I721, Zr]])
OmM = np.block([[Zr, M], [-M, Zr]])
G2 = np.block([[2 * M, -(M @ L)], [-(M @ L), 34 * M]])     # 2 G_M (integral)
check(not (F.T @ OmM @ F - 17 * OmM).any(), "F^t Omega_M F = 17 Omega_M exactly")
check(not (F.T @ G2 @ F - 17 * G2).any(), "F^t (2 G_M) F = 17 (2 G_M) exactly")
check(((M @ L) == (M @ L).T).all(), "M L is symmetric (so G_M is a symmetric matrix)")
evG = np.linalg.eigvalsh(G2.astype(float) / 2)
check(evG.min() > 0 and (17 - evL**2 / 4).min() > 0,
      "G_M > 0: smallest eigenvalue %.6f (float); Schur complement M(17 - L^2/4) > 0 since min(17 - a^2/4) = %.6f > 0" % (evG.min(), (17 - evL**2 / 4).min()))
# orthonormal coordinates: Q = Z M^{-1/2} sends the coefficient metric to I and L to a symmetric matrix; compare with the worked G
w, V = np.linalg.eigh(M.astype(float)); Mh = V @ np.diag(np.sqrt(w)) @ V.T; Mhi = V @ np.diag(1/np.sqrt(w)) @ V.T
Ls = Mh @ L @ Mhi
check(np.abs(Ls - Ls.T).max() < 1e-7 and np.abs(np.sort(np.linalg.eigvalsh((Ls + Ls.T)/2)) - np.sort(evK)).max() < 1e-7,
      "M^{1/2} L M^{-1/2} is symmetric with spec T: in orthonormal cycle coordinates G_M becomes the worked example's G = [[I, -T/2],[-T/2, 17 I]]")

# ---------------------------------------------------------------- the completed Bass zeta and point counts (exact integer traces)
# Tr F^n = Tr P_n(L) with P_0 = 2, P_1 = a, P_n = a P_{n-1} - 17 P_{n-2}   (alpha^n + beta^n for the roots of x^2 - a x + 17)
Lobj = L.astype(object)
Pprev, Pcur = 2 * np.eye(721, dtype=object), Lobj.copy()
trF = []
for n in range(1, 7):
    trF.append(int(np.trace(Pcur)))
    Pprev, Pcur = Pcur, Lobj @ Pcur - 17 * Pprev
N = [1 + 17**n - trF[n - 1] for n in range(1, 7)]
check(N == [0, 11520, 10080, 126720, 1209600, 23886720], "N_n = 1 + 17^n - Tr F^n for n = 1..6: %s (worked example: 0, 11520, 10080, 126720, 1209600, 23886720)" % N)
check(N[0] == 0 and N[1] == 11520, "predicted point counts of the quotient curve C: #C(F_17) = %d, #C(F_289) = %d" % (N[0], N[1]))
mob = []
for n in range(1, 7):
    s = sum(sympy.mobius(d) * N[n // d - 1] for d in sympy.divisors(n))
    mob.append(s // n)
check(all(x >= 0 for x in mob), "Moebius-inverted primitive exponents b_n = (1/n) sum mu(d) N_{n/d} are nonnegative integers: %s (closed points of degree n)" % mob)

# ---------------------------------------------------------------- summary
npass = sum(1 for _, ok, _ in LEDGER if ok)
print("\nSUMMARY: %d checks, %d pass, %d fail; runtime %.1f s" % (len(LEDGER), npass, len(LEDGER) - npass, time.time() - T0))
