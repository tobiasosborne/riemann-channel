#!/usr/bin/env python3
"""Checks for notes/adelic-gkp/family-vacuum.md (lane M: families of steps that share a vacuum, and families that do not), 2026-10-06.

Conventions (as in check_family_weil.py).
  Omega(x, y) = x^T Omega y; one mode Omega = [[0,1],[-1,0]]; n modes Omega = [[0,I],[-I,0]] (block (x, y) coordinates) or the
  direct sum of [[0,1],[-1,0]] (interleaved coordinates), said where used.
  A step M of norm q: M^T Omega M = q Omega, V = q M^{-1}.  S = M/sqrt(q) is symplectic.
  A vacuum for M: a real J with J^2 = -1, J M = M J and G_J = Omega J symmetric positive definite.
  One-mode step M_q = [[0,-1],[q,lam]]: J_q = (M_q - V_q)/sqrt(4q - lam^2), Weil form W = (1/2) Omega (M - V).
  Graph family: vertex-level Hecke pair of the (13,17;5) LPS square complex (report shard 04u): vertices PGL_2(F_5),
  A_13 = adjacency of the 13-graph Y (14-regular, the Cayley graph of PGL_2(F_5) on phi(S_13)), A_17 = adjacency of the
  Cayley graph on phi(S_17) (18-regular), which is the vertex form of the transverse transport T_17 (04u: T_1 D = D A_17).
  Construction copied from scripts/lps_square_complex.py (quaternions S_p, phi(a) = [[a0+2a1, a2+2a3],[-a2+2a3, a0-2a1]] mod 5).
  Steps M_q = [[0,-I],[q I, A_q]] on Z^{2n}, n = 120, with Omega = [[0,I],[-I,0]].
  Zeta family: lane G's spectral model, real form: on the plane of the zero pair {1/2 + i g, 1/2 - i g} the prime step is
  M_p = sqrt(p) R(g log p), R(t) the rotation; Omega_FE on the plane = [[0,1],[-1,0]] (orientation fixed so that J = R(pi/2)
  is the positive vacuum; 04t's normalisation has weights -i sgn(gamma), the orientation only flips J -> -J).
Needs numpy, sympy, data/zeros3000.npy.  Run time a few seconds.
"""
import os
import time
from itertools import product, combinations

import numpy as np
import sympy as sp

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


def info(s):
    print("      " + s)


Om2 = np.array([[0.0, 1.0], [-1.0, 0.0]])
R90 = np.array([[0.0, -1.0], [1.0, 0.0]])
rng = np.random.default_rng(20261006)


def rot(t):
    return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])


def is_vacuum(J, M_list, Om, tol=1e-9):
    n = J.shape[0]
    G = Om @ J
    return (np.allclose(J @ J, -np.eye(n), atol=tol) and all(np.allclose(J @ M, M @ J, atol=tol * max(1, np.abs(M).max())) for M in M_list)
            and np.allclose(G, G.T, atol=tol) and np.linalg.eigvalsh((G + G.T) / 2).min() > tol)


def onemode(q, lam):
    M = np.array([[0.0, -1.0], [q, lam]])
    V = q * np.linalg.inv(M)
    J = (M - V) / np.sqrt(4 * q - lam ** 2)
    return M, V, J


# =============================================================================================
print("== M1  two one-mode steps on Z^2; the commuting case; the proposition")
q, l, q2, l2 = sp.symbols("q lambda q' lambda'", real=True)
Ms = sp.Matrix([[0, -1], [q, l]])
Ms2 = sp.Matrix([[0, -1], [q2, l2]])
Vs = sp.simplify(q * Ms.inv())
check("M1 symbolic: V_q = q M_q^{-1} = [[lambda,1],[-q,0]], M_q - V_q = [[-lambda,-2],[2q,lambda]]",
      sp.simplify(Vs - sp.Matrix([[l, 1], [-q, 0]])) == sp.zeros(2) and sp.simplify(Ms - Vs - sp.Matrix([[-l, -2], [2 * q, l]])) == sp.zeros(2))
comm = sp.expand(Ms * Ms2 - Ms2 * Ms)
check("M1 symbolic: M_q M_q' - M_q' M_q = [[q - q', lambda - lambda'],[q' lambda - q lambda', q' - q]]",
      sp.simplify(comm - sp.Matrix([[q - q2, l - l2], [q2 * l - q * l2, q2 - q]])) == sp.zeros(2), str(comm.tolist()))
# J_q = J_q' iff equal: entry (1,2) is -2/d, so d = d'; then entries (1,1), (2,1) give lambda, q.  J_q = -J_q' impossible (-2/d = 2/d').
MV = sp.expand(Ms * sp.Matrix([[l2, 1], [-q2, 0]]))
check("M1 symbolic: M_q V_q' = [[q', 0],[q lambda' - q' lambda, q]], lower triangular with eigenvalues q', q (real), whatever lambda, lambda'",
      sp.simplify(MV - sp.Matrix([[q2, 0], [q * l2 - q2 * l, q]])) == sp.zeros(2), str(MV.tolist()))
d, d2 = sp.symbols("d d'", positive=True)
Jsym = sp.Matrix([[-l, -2], [2 * q, l]]) / d
Jsym2 = sp.Matrix([[-l2, -2], [2 * q2, l2]]) / d2
sol = sp.solve(list(Jsym - Jsym2), [d2, l2, q2], dict=True)
solm = sp.solve(list(Jsym + Jsym2), [d2, l2, q2], dict=True)
check("M1 symbolic: J_q = J_q' (with d = sqrt(4q - lambda^2) > 0) forces (d', lambda', q') = (d, lambda, q); J_q = -J_q' has no solution with d, d' > 0",
      sol == [{d2: d, l2: l, q2: q}] and solm == [], f"solutions: {sol}, {solm}")
pairs = [(2, -1), (5, -2), (7, 2), (13, 3), (13, -3), (17, 0)]
okJ = okC = okvac = True
hyp = []
for (qa, la), (qb, lb) in combinations(pairs, 2):
    Ma, Va, Ja = onemode(qa, la)
    Mb, Vb, Jb = onemode(qb, lb)
    okvac &= is_vacuum(Ja, [Ma], Om2) and is_vacuum(Jb, [Mb], Om2)
    okJ &= (np.abs(Ja - Jb).max() > 1e-3) and (np.abs(Ja + Jb).max() > 1e-3)
    okC &= np.abs(Ma @ Mb - Mb @ Ma).max() > 0.5
    t = np.trace(Ma @ Mb) / np.sqrt(qa * qb)
    if abs(t) > 2:
        hyp.append(((qa, la), (qb, lb), round(t, 4)))
check("M1 numeric, 6 steps (q,lambda) in {(2,-1),(5,-2),(7,2),(13,3),(13,-3),(17,0)}: each J_q is a vacuum for Omega = [[0,1],[-1,0]]; "
      "for all 15 pairs J_q != +-J_q' and M_q, M_q' do not commute", okvac and okJ and okC)
check("M1 2x2: a matrix with non-real eigenvalues determines its complex structure up to sign, so a common vacuum of two such steps exists iff they commute: "
      "here it fails for all 15 pairs; for some pairs the normalised product S_q S_q' is even hyperbolic (|tr| > 2), so no Omega at all admits a common vacuum",
      len(hyp) > 0, f"hyperbolic products: {hyp}")
# CM family (lane C): O_K, K = Q(sqrt-7), basis (1, w), w^2 = w - 2.  psi at p = 2: (1 + sqrt-7)/2 = w; at p = 11: (a + y sqrt-7)/2 with 44 = x^2 + 7y^2, x = 4, y = 2, a_11 = (4|7)4 = 4 -> (4 + 2 sqrt-7)/2 = 1 + 2w.


def mult(a, b):
    return np.array([[a, -2 * b], [b, a + b]], float)


sq7 = np.sqrt(7.0)
JK = mult(-1, 2) / sq7
cm = {"psi(P_2) = w": mult(0, 1), "conj = 1 - w": mult(1, -1), "psi(P_11) = 1 + 2w": mult(1, 2), "conj = 3 - 2w": mult(3, -2)}
okcm = all(np.allclose(A @ B, B @ A) for A, B in combinations(cm.values(), 2)) and is_vacuum(JK, list(cm.values()), Om2)
mods = {k: np.sqrt(abs(np.linalg.det(A))) for k, A in cm.items()}
signs = {k: int(np.sign(np.linalg.eigvalsh(0.5 * Om2 @ (A - np.linalg.det(A) * np.linalg.inv(A)) + 0.5 * (Om2 @ (A - np.linalg.det(A) * np.linalg.inv(A))).T)[0])) for k, A in cm.items()}
check("M1 CM family on O_K (lane C): the four Hecke steps commute, share the vacuum J_K, have |eigenvalue| = sqrt p, and their Weil forms for one Omega have both signs",
      okcm and np.allclose([mods[k] ** 2 for k in cm], [2, 2, 11, 11]) and set(signs.values()) == {1, -1}, f"Weil-form signs: {signs}")


# Proposition (commuting family): construct a commuting elliptic family with mixed orientations and recover the common vacuum.
def random_symplectic(n):
    X = rng.normal(size=(2 * n, 2 * n))
    H = (X + X.T) / 2
    Om = np.block([[np.zeros((n, n)), np.eye(n)], [-np.eye(n), np.zeros((n, n))]])
    from scipy.linalg import expm
    return expm(Om @ H * 0.4), Om


def interleave(blocks):
    n = len(blocks)
    out = np.zeros((2 * n, 2 * n))
    for i, B in enumerate(blocks):
        out[np.ix_([i, n + i], [i, n + i])] = B
    return out


nm = 3
P, OmB = random_symplectic(nm)
check("M1 prop. setup: random P with P^T Omega P = Omega (n = 3 modes, block coordinates)", np.allclose(P.T @ OmB @ P, OmB, atol=1e-9))
fam_q = [2, 3, 5]
angles = {2: [1.1, -0.7, 2.5], 3: [-2.0, 0.4, 1.3], 5: [0.9, 2.2, -1.6]}   # mixed signs of sin(theta): mixed Weil-form signs
Mfam = [P @ interleave([np.sqrt(qq) * rot(t) for t in angles[qq]]) @ np.linalg.inv(P) for qq in fam_q]
okc = all(np.allclose(A @ B, B @ A, atol=1e-9) for A, B in combinations(Mfam, 2))
oks = all(np.allclose(M.T @ OmB @ M, qq * OmB, atol=1e-8) for M, qq in zip(Mfam, fam_q))
check("M1 prop. family: three commuting steps of norms 2, 3, 5, each semisimple with |eigenvalues| = sqrt q, compatible with one Omega", okc and oks)
# (iii) => (i): average a random positive form over the closure (the 3-torus) of the group; exact on the quarter-turn grid
G0 = rng.normal(size=(2 * nm, 2 * nm))
G0 = G0 @ G0.T + np.eye(2 * nm)
Pinv = np.linalg.inv(P)
H0 = P.T @ G0 @ P
acc = np.zeros_like(H0)
grid = list(product(range(4), repeat=nm))
for ks in grid:
    Rk = interleave([rot(k * np.pi / 2) for k in ks])
    acc += Rk.T @ H0 @ Rk
G = Pinv.T @ (acc / len(grid)) @ Pinv
okinv = all(np.allclose(M.T @ G @ M, qq * G, atol=1e-7) for M, qq in zip(Mfam, fam_q))
A = np.linalg.solve(G, OmB)                                    # Omega(x, y) = G(x, A y)
w, U = np.linalg.eig(-A @ A)
sq = (U @ np.diag(np.sqrt(w)) @ np.linalg.inv(U)).real          # (-A^2)^{1/2}
Jc = -A @ np.linalg.inv(sq)
check("M1 prop. (iii)=>(i): the torus average G of a random positive form is invariant (M^T G M = q G); J = -A(-A^2)^{-1/2}, A = G^{-1} Omega, "
      "is a common vacuum (J^2 = -1, commutes with all three, Omega J > 0)", okinv and is_vacuum(Jc, Mfam, OmB, tol=1e-7))
J0 = P @ interleave([R90] * nm) @ Pinv
check("M1 prop.: here the common vacuum is unique and equals P (+R(pi/2) per mode) P^{-1}, although the three Weil forms are indefinite",
      np.allclose(Jc, J0, atol=1e-7) and all(min(np.linalg.eigvalsh(0.5 * (OmB @ (M - qq * np.linalg.inv(M)) + (OmB @ (M - qq * np.linalg.inv(M))).T) / 2)) < 0
                                             for M, qq in zip(Mfam, fam_q)))
# a non-semisimple elliptic-spectrum step has no vacuum: Jordan block sqrt(2) [[1,1],[0,1]] in 1 mode is not a similitude-compatible elliptic ... use 2 modes
Mj = np.sqrt(2) * np.block([[R90, np.eye(2)], [np.zeros((2, 2)), R90]])
check("M1 prop.: semisimplicity is needed: sqrt2 [[R,1],[0,R]] has |eigenvalues| = sqrt 2 but its normalised powers are unbounded (no vacuum for any Omega)",
      np.abs(np.linalg.matrix_power(Mj / np.sqrt(2), 50)).max() > 40)

# =============================================================================================
print("== M2  the Hecke family of the (13,17;5) LPS complex at vertex level")


def qmul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3, a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1, a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0)


def gens(p):
    r = int(p ** 0.5) + 1
    out = []
    for a0 in range(1, r + 1, 2):
        for a1, a2, a3 in product(range(-r, r + 1), repeat=3):
            if a1 % 2 or a2 % 2 or a3 % 2:
                continue
            if a0 * a0 + a1 * a1 + a2 * a2 + a3 * a3 == p:
                out.append((a0, a1, a2, a3))
    return sorted(out)


PP = 5


def mnorm(m):
    m = tuple(x % PP for x in m)
    for x in m:
        if x:
            inv = pow(x, PP - 2, PP)
            return tuple((y * inv) % PP for y in m)
    raise ValueError


def mmul(m, n):
    return mnorm((m[0] * n[0] + m[1] * n[2], m[0] * n[1] + m[1] * n[3], m[2] * n[0] + m[3] * n[2], m[2] * n[1] + m[3] * n[3]))


def phi(a):
    a0, a1, a2, a3 = a
    return mnorm((a0 + 2 * a1, a2 + 2 * a3, -a2 + 2 * a3, a0 - 2 * a1))


VERTS = sorted({mnorm(m) for m in product(range(PP), repeat=4) if (m[0] * m[3] - m[1] * m[2]) % PP})
VIDX = {v: i for i, v in enumerate(VERTS)}
NV = len(VERTS)
S13, S17 = gens(13), gens(17)
check("M2 |S_13| = 14, |S_17| = 18, |PGL_2(F_5)| = 120, phi multiplicative on the generators",
      len(S13) == 14 and len(S17) == 18 and NV == 120 and all(phi(qmul(a, b)) == mmul(phi(a), phi(b)) for a in S13 + S17 for b in S13 + S17))


def cayley(S):
    A = np.zeros((NV, NV), dtype=np.int64)
    for v in range(NV):
        for s in S:
            A[v, VIDX[mmul(VERTS[v], phi(s))]] += 1
    return A


A13, A17 = cayley(S13), cayley(S17)
check("M2 A_13, A_17 symmetric 0/1 matrices, regular of degree 14 and 18, and they commute (exactly, integer arithmetic)",
      (A13 == A13.T).all() and (A17 == A17.T).all() and A13.max() == 1 and A17.max() == 1 and (A13.sum(1) == 14).all()
      and (A17.sum(1) == 18).all() and (A13 @ A17 == A17 @ A13).all())
# joint eigenbasis
Cmix = A13 + (np.pi / 10) * A17
_, U = np.linalg.eigh(Cmix.astype(float))
D13 = U.T @ A13 @ U
D17 = U.T @ A17 @ U
check("M2 one orthogonal U diagonalises both (off-diagonal < 1e-9)", np.abs(D13 - np.diag(np.diag(D13))).max() < 1e-9 and np.abs(D17 - np.diag(np.diag(D17))).max() < 1e-9)
lam13 = np.round(np.diag(D13), 8)
lam17 = np.round(np.diag(D17), 8)
joint = {}
for i, key in enumerate(zip(lam13, lam17)):
    joint.setdefault((float(key[0]) + 0.0, float(key[1]) + 0.0), []).append(i)
nontriv = {k: v for k, v in joint.items() if abs(k[0]) != 14}
info("joint eigenvalues (lambda_13, lambda_17): multiplicity  " + ", ".join(f"({a:g},{b:g}): {len(v)}" for (a, b), v in sorted(joint.items())))
check("M2 trivial (14, 18) and bipartite sign (-14, -18) eigenvalues have multiplicity one; the other 118 dimensions split into 10 joint eigenspaces, all integral eigenvalues",
      len(joint.get((14.0, 18.0), [])) == 1 and len(joint.get((-14.0, -18.0), [])) == 1 and len(nontriv) == 10
      and sum(len(v) for v in nontriv.values()) == 118 and all(float(a).is_integer() and float(b).is_integer() for a, b in nontriv))
check("M2 Ramanujan, strictly: |lambda_13| < 2 sqrt 13 = 7.211 and |lambda_17| < 2 sqrt 17 = 8.246 on the 118-dimensional part W",
      all(abs(a) < 2 * np.sqrt(13) and abs(b) < 2 * np.sqrt(17) for a, b in nontriv))
n = NV
I = np.eye(n)
Z = np.zeros((n, n))
OmN = np.block([[Z, I], [-I, Z]])


def step(qq, A):
    return np.block([[Z, -I], [qq * I, A.astype(float)]])


M13, M17 = step(13, A13), step(17, A17)
check("M2 M_q = [[0,-I],[qI,A_q]] is integral with M_q^T Omega M_q = q Omega for Omega = [[0,I],[-I,0]], q = 13, 17 (one Omega for both)",
      np.array_equal(M13.T @ OmN @ M13, 13 * OmN) and np.array_equal(M17.T @ OmN @ M17, 17 * OmN))
Cm = M13 @ M17 - M17 @ M13
check("M2 the steps do not commute: M_13 M_17 - M_17 M_13 equals the block form of the 2x2 formula [[q - q', A - A'],[q' A - q A', q' - q]] "
      "= [[-4 I, A_13 - A_17],[17 A_13 - 13 A_17, 4 I]]",
      np.array_equal(Cm, np.block([[(13 - 17) * I, (A13 - A17).astype(float)], [(17 * A13 - 13 * A17).astype(float), (17 - 13) * I]])),
      f"max |entry| = {np.abs(Cm).max():.0f}")
# project to W (x) R^2 in the joint eigenbasis, interleaved per eigenvector: block i is the 2x2 m_q(i) = [[0,-1],[q, lam_q(i)]]
Wi = [i for i in range(n) if abs(lam13[i]) != 14]


def vac_matrix(qq, lam):
    """J_q on W (x) R^2 in block coordinates, assembled from the eigenbasis: J = (M - V)(4q - A^2)^{-1/2}"""
    UW = U[:, Wi]
    s = 1.0 / np.sqrt(4 * qq - lam[Wi] ** 2)
    Af = UW @ np.diag(lam[Wi] * s) @ UW.T
    Sf = UW @ np.diag(s) @ UW.T
    return np.block([[-Af, -2 * Sf], [2 * qq * Sf, Af]])


J13, J17 = vac_matrix(13, lam13), vac_matrix(17, lam17)
PW = np.block([[U[:, Wi] @ U[:, Wi].T, Z], [Z, U[:, Wi] @ U[:, Wi].T]])
OmW = PW @ OmN @ PW


def vac_ok(J, M):
    G = OmN @ J
    ev = np.linalg.eigvalsh((G + G.T) / 2)
    return (np.allclose(J @ J, -PW, atol=1e-9) and np.allclose(J @ M @ PW, M @ J, atol=1e-8) and np.allclose(G, G.T, atol=1e-9)
            and np.sum(ev > 1e-9) == 236 and np.sum(np.abs(ev) < 1e-9) == 4)


check("M2 (a) J_q = (M_q - V_q)(4q - A_q^2)^{-1/2} on W (x) R^2 (236 dims) is a vacuum of M_q for q = 13 and q = 17 (J^2 = -1 on W, commutes, Omega J > 0 on W)",
      vac_ok(J13, M13) and vac_ok(J17, M17))
W13 = 0.5 * PW @ OmN @ (M13 - 13 * np.linalg.inv(M13)) @ PW
W17 = 0.5 * PW @ OmN @ (M17 - 17 * np.linalg.inv(M17)) @ PW
e13 = np.linalg.eigvalsh((W13 + W13.T) / 2)
e17 = np.linalg.eigvalsh((W17 + W17.T) / 2)
check("M2 (a) the Weil form (1/2) Omega (M_q - V_q) of each step is positive definite on W for the shared Omega (every mode has sin(theta) > 0): "
      "the mirror image of the CM family (shared vacuum, Weil forms of both signs)",
      np.sum(e13 > 1e-9) == 236 and np.sum(e17 > 1e-9) == 236, f"min positive eigenvalue: {e13[e13 > 1e-9].min():.3f}, {e17[e17 > 1e-9].min():.3f}")
check("M2 (a) the vacua differ: ||J_13 - J_17|| > 0, J_17 does not commute with M_13 nor J_13 with M_17",
      np.abs(J13 - J17).max() > 0.1 and np.abs(J17 @ M13 - M13 @ J17).max() > 0.1 and np.abs(J13 @ M17 - M17 @ J13).max() > 0.1,
      f"max |J_13 - J_17| = {np.abs(J13 - J17).max():.3f}")


# (b) the commutant, computed exactly in the joint eigenbasis: X = (X_ik) 2x2 blocks with m_q(i) X_ik = X_ik m_q(k) for both q
def m2(qq, lam):
    return np.array([[0.0, -1.0], [qq, lam]])


def block_commutant(mats_i, mats_k):
    rows = []
    for Ai, Ak in zip(mats_i, mats_k):
        rows.append(np.kron(Ai, np.eye(2)) - np.kron(np.eye(2), Ak.T))   # vec_row(A X - X B)
    Mx = np.vstack(rows)
    s = np.linalg.svd(Mx, compute_uv=False)
    _, _, Vt = np.linalg.svd(Mx)
    k = int(np.sum(s < 1e-9))
    return k, Vt[4 - k:] if k else np.zeros((0, 4))


labels = {i: (lam13[i], lam17[i]) for i in Wi}
dim_fam = dim_13 = 0
okI = True
for i in Wi:
    for k in Wi:
        kf, basis = block_commutant([m2(13, lam13[i]), m2(17, lam17[i])], [m2(13, lam13[k]), m2(17, lam17[k])])
        k13, _ = block_commutant([m2(13, lam13[i])], [m2(13, lam13[k])])
        dim_fam += kf
        dim_13 += k13
        if kf:
            v = basis[0].reshape(2, 2)
            okI &= (labels[i] == labels[k]) and kf == 1 and np.allclose(v / v[0, 0], np.eye(2), atol=1e-9)
mult = sorted(len(v) for v in nontriv.values())
mult13 = {}
for i in Wi:
    mult13[lam13[i]] = mult13.get(lam13[i], 0) + 1
check("M2 (b) commutant of {M_13, M_17} on W (x) R^2 has dimension sum_j m_j^2 = 1618, and every element is I_2 (x) X_j on each joint eigenspace",
      dim_fam == sum(m * m for m in mult) == 1618 and okI, f"computed {dim_fam}; multiplicities {mult}")
check("M2 (b) for comparison the commutant of M_13 alone has dimension 2 sum m^2 over eigenvalues of A_13 (C-linear maps per eigenspace) = 7124",
      dim_13 == 2 * sum(m * m for m in mult13.values()) == 7124, f"computed {dim_13}; A_13 multiplicities {sorted(mult13.items())}")
# positivity: for J = I_2 (x) X on a joint eigenspace, Omega(e (x) v, J e (x) v) = omega(e, e) v.Xv = 0
okzero = True
for (a, b), idx in nontriv.items():
    m = len(idx)
    X = rng.normal(size=(m, m))
    X = X - X.T        # any X; antisymmetric is the only way Omega J can be symmetric
    Jb = np.kron(np.eye(2), X)          # interleaved (e (x) v) ordering: R^2 (x) E_j
    Omb = np.kron(Om2, np.eye(m))
    e = rng.normal(size=2)
    v = rng.normal(size=m)
    x = np.kron(e, v)
    okzero &= abs(x @ Omb @ Jb @ x) < 1e-9
check("M2 (b) no element of the commutant is positive for Omega: Omega(e (x) v, (I (x) X)(e (x) v)) = omega(e,e) v^T X v = 0 on every joint eigenspace",
      okzero)
check("M2 (b) two joint eigenspaces have odd multiplicity (15): there the commutant contains no complex structure at all",
      sorted(m for m in mult if m % 2) == [15, 15], f"odd multiplicities: {[m for m in mult if m % 2]}")
# Omega-independent obstruction: hyperbolic products
hyps = []
for (a, b), idx in sorted(nontriv.items()):
    t = np.trace(m2(13, a) @ m2(17, b)) / np.sqrt(13 * 17)
    hyps.append(((a, b), round(t, 4), abs(t) > 2))
nh = sum(h[2] for h in hyps)
info("normalised trace of S_13 S_17 per joint eigenspace: " + ", ".join(f"({a:g},{b:g}): {t}" for (a, b), t, _ in hyps))
P13_17 = M13 @ M17
ev = np.linalg.eigvals(P13_17)
off = np.sum(np.abs(np.abs(ev) - np.sqrt(221)) > 1e-6)
check("M2 (b) Omega-independent obstruction: on 6 of the 10 joint eigenspaces S_13 S_17 is hyperbolic (|tr| > 2: lambda_13 lambda_17 <= 0 gives tr <= -(r + 1/r) < -2, r = sqrt(13/17)); "
      "the integral product M_13 M_17 has eigenvalues off |mu| = sqrt 221, so no compatible form of any kind admits a vacuum invariant under the family",
      nh == 6 and off == 2 * sum(len(nontriv[k]) for k, t, h in hyps if h) + 4, f"eigenvalues of M_13 M_17 (240 of them) with |mu| != sqrt 221: {off} (4 of these come from the trivial and sign modes)")
# for every Omega: on each plane the normalised 2x2 steps generate an unbounded group (a hyperbolic word of length <= 4 in S^{+-1})
def hyperbolic_word(a, b):
    s13, s17 = m2(13, a) / np.sqrt(13), m2(17, b) / np.sqrt(17)
    letters = {"S13": s13, "S13^-1": np.linalg.inv(s13), "S17": s17, "S17^-1": np.linalg.inv(s17)}
    for L in range(1, 5):
        for w in product(letters, repeat=L):
            X = np.eye(2)
            for x in w:
                X = X @ letters[x]
            if abs(np.trace(X)) > 2 + 1e-9:
                return w, np.trace(X)
    return None, None


V17 = 17 * np.linalg.inv(M17)
check("M2 (b) exact identity: V_17 = [[A_17, I],[-17 I, 0]] and M_13 V_17 = [[17 I, 0],[13 A_17 - 17 A_13, 13 I]] (integral, block lower triangular, "
      "eigenvalues 17 and 13, each 120 times): S_13 S_17^{-1} has real eigenvalues sqrt(17/13), sqrt(13/17) on every mode",
      np.allclose(V17, np.block([[A17.astype(float), I], [-17 * I, Z]]), atol=1e-9)
      and np.allclose(M13 @ np.block([[A17.astype(float), I], [-17 * I, Z]]), np.block([[17 * I, Z], [(13 * A17 - 17 * A13).astype(float), 13 * I]])))
words = {k: hyperbolic_word(*k) for k in sorted(nontriv)}
info("shortest hyperbolic word per plane: " + "; ".join(f"({a:g},{b:g}): {'.'.join(w)} tr {t:.3f}" for (a, b), (w, t) in words.items()))
check("M2 (b) on every one of the 10 joint eigenspaces some word of length <= 4 in S_13^{+-1}, S_17^{+-1} (integral up to scale: V_q = q M_q^{-1}) is hyperbolic, "
      "so the family has no common vacuum for any compatible Omega on any joint eigenspace", all(w is not None for w, t in words.values()))
# (c) per-joint-eigenspace coordinates: the 2x2 steps on one plane never commute (diagonal q - q')
okc = True
cnorms = []
for (a, b) in nontriv:
    s13, s17 = m2(13, a) / np.sqrt(13), m2(17, b) / np.sqrt(17)
    c = s13 @ s17 - s17 @ s13
    cnorms.append(np.linalg.norm(c))
    okc &= np.linalg.norm(c) > 0.1
check("M2 (c) on each joint eigenspace the normalised 2x2 steps S_13, S_17 do not commute (diagonal of [M,M'] is q - q' = -4 != 0), so no choice of "
      "plane coordinates makes both rotations of one plane", okc, f"min ||[S_13, S_17]|| over the 10 planes = {min(cnorms):.4f}")
# the CM-ified family: replace each step on plane j by sqrt(q) R(theta), any choice of sign of theta per (q, j)
okr = True
for (a, b) in nontriv:
    for s1, s2 in product([1, -1], repeat=2):
        t13 = s1 * np.arccos(a / (2 * np.sqrt(13)))
        t17 = s2 * np.arccos(b / (2 * np.sqrt(17)))
        R13, R17 = np.sqrt(13) * rot(t13), np.sqrt(17) * rot(t17)
        okr &= np.allclose(R13 @ R17, R17 @ R13) and is_vacuum(R90, [R13, R17], Om2)
        okr &= np.allclose(np.sort_complex(np.linalg.eigvals(R13)), np.sort_complex(np.linalg.eigvals(m2(13, a))))
check("M2 (c) the rotation family sqrt(q) R(+-theta_q^j) on each plane commutes and shares R(pi/2) for all four sign choices, with the same spectra as M_q; "
      "it is a different family (not simultaneously conjugate to (M_13, M_17), whose commutator is non-zero)", okr)

# =============================================================================================
print("== M3  the zeta family: prime steps on the first 50 zero pairs")
zeros = np.load(os.path.join(ROOT, "data", "zeros3000.npy"))
g = zeros[:50]
check("M3 data/zeros3000.npy: first 50 ordinates, gamma_1 = 14.1347, gamma_50 = 143.1118", abs(g[0] - 14.134725) < 1e-5 and abs(g[49] - 143.111846) < 1e-5,
      f"gamma_50 = {g[49]:.6f}")
K = len(g)


def blockdiag(blocks):
    out = np.zeros((2 * len(blocks), 2 * len(blocks)))
    for i, B in enumerate(blocks):
        out[2 * i:2 * i + 2, 2 * i:2 * i + 2] = B
    return out


Mp = {p: blockdiag([np.sqrt(p) * rot(gg * np.log(p)) for gg in g]) for p in (2, 3, 5)}
OmZ = blockdiag([Om2] * K)
JZ = blockdiag([R90] * K)
check("M3 M_2, M_3, M_5 (100 x 100) commute pairwise", all(np.allclose(Mp[a] @ Mp[b], Mp[b] @ Mp[a], atol=1e-12) for a, b in combinations(Mp, 2)))
check("M3 M_p^T Omega_FE M_p = p Omega_FE; M_p/sqrt(p) orthogonal; all eigenvalues of modulus sqrt(p)",
      all(np.allclose(M.T @ OmZ @ M, p * OmZ, atol=1e-11) and np.allclose((M / np.sqrt(p)).T @ (M / np.sqrt(p)), np.eye(2 * K), atol=1e-12)
          and np.allclose(np.abs(np.linalg.eigvals(M)), np.sqrt(p), atol=1e-10) for p, M in Mp.items()))
check("M3 J = R(pi/2) on every pair: J^2 = -1, Omega_FE J = I > 0, and J commutes with M_2, M_3, M_5: one vacuum for the family",
      is_vacuum(JZ, list(Mp.values()), OmZ, tol=1e-11) and np.allclose(OmZ @ JZ, np.eye(2 * K)))
negs = {}
for p, M in Mp.items():
    Wp = 0.5 * OmZ @ (M - p * np.linalg.inv(M))
    Wp = (Wp + Wp.T) / 2
    ev = np.linalg.eigvalsh(Wp)
    pred = np.repeat(np.sqrt(p) * np.sin(g * np.log(p)), 2)
    negs[p] = (int(np.sum(ev < 0)), np.allclose(np.sort(ev), np.sort(pred), atol=1e-10))
check("M3 the Weil form of each M_p for Omega_FE has eigenvalues sqrt(p) sin(gamma log p) (each twice): indefinite for p = 2, 3, 5 (lane G)",
      all(v[1] and 0 < v[0] < 2 * K for v in negs.values()), f"negative eigenvalues of 100: {[(p, v[0]) for p, v in negs.items()]}")
okMV = all(np.allclose(Mp[a] @ (b * np.linalg.inv(Mp[b])), blockdiag([np.sqrt(a * b) * rot(gg * np.log(a / b)) for gg in g]), atol=1e-9)
           for a, b in combinations(Mp, 2))
check("M3 M_p V_p' = sqrt(pp') R(gamma log(p/p')) on every pair: elliptic (contrast M2, where M_q V_q' has real eigenvalues q, q')", okMV)
okprod = all(np.allclose(np.abs(np.linalg.eigvals(Mp[a] @ Mp[b])), np.sqrt(a * b), atol=1e-9) for a, b in combinations(Mp, 2))
check("M3 every product M_p M_p' is sqrt(pp') times a rotation (by gamma log pp'): the normalised semigroup is bounded, no hyperbolic element (contrast M2)", okprod)
# contrast: Bass-doubled zeta steps from the same spectral data lambda_p = 2 sqrt(p) cos(gamma log p)
lamz = {p: 2 * np.sqrt(p) * np.cos(g * np.log(p)) for p in (2, 3, 5)}
Bz = {p: blockdiag([m2(p, x) for x in lamz[p]]) for p in (2, 3, 5)}
okB = all(np.allclose(np.sort_complex(np.linalg.eigvals(Bz[p])), np.sort_complex(np.linalg.eigvals(Mp[p])), atol=1e-9) for p in Bz)
nc = all(np.abs(Bz[a] @ Bz[b] - Bz[b] @ Bz[a]).max() > 0.5 for a, b in combinations(Bz, 2))
nhyp = {}
for a, b in combinations((2, 3, 5), 2):
    tr = np.array([np.trace(m2(a, x) @ m2(b, y)) for x, y in zip(lamz[a], lamz[b])]) / np.sqrt(a * b)
    nhyp[(a, b)] = int(np.sum(np.abs(tr) > 2))
check("M3 contrast: Bass-doubled steps [[0,-1],[p, 2 sqrt(p) cos(gamma log p)]] per zero have the same spectra as M_p but do not commute, and their products are "
      "hyperbolic on many zeros (and B_p B_p'^{-1} on all, by the M1 identity), exactly as the graph family: the difference is the realisation, not the spectral data",
      okB and nc and all(v > 0 for v in nhyp.values()), f"zeros (of 50) with S_p S_p' hyperbolic: {nhyp}")

print()
print(f"{npass} of {npass + nfail} pass  ({time.time() - T0:.1f} s)")
