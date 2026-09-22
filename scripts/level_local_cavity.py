#!/usr/bin/env python3
"""Numerics lane for notes/level-local-cavity (2026-09-22): independent checks of the displayed
formulas of astra-proofs.md, L1-L4, written without reading the prover's checks/ scripts.

Conventions (astra-proofs.md, 'Conventions'): width-one cusps (infinity, 0); ell = log q, a = q^{-1/2},
z = q^{s-1/2} (the 04k disk variable), s = 1/2 + i tau, z = e^{i ell tau}; F = [[0,1],[1,0]],
D = diag(1,-1), H = 2^{-1/2} [[1,1],[1,-1]]. Diagram scattering (04k): G = (lambda - T_X)^{-1} on the
core (W = I, C = I), Q(z) = I - z G, S = -Q(z)^{-1} Q(1/z), lambda = z + 1/z.

Run from the repo root: python3 scripts/level_local_cavity.py > outputs/level_local_cavity.txt
"""
import time
import mpmath as mp
import numpy as np

mp.mp.dps = 40
T0 = time.time()
LEDGER = []


def check(cond, desc, val=""):
    LEDGER.append((bool(cond), desc, val))
    print("D%02d %s %s %s" % (len(LEDGER), "PASS" if cond else "FAIL", desc, val))


def mat(rows):
    return mp.matrix(rows)


I2 = mp.eye(2)
F = mat([[0, 1], [1, 0]])
Dm = mat([[1, 0], [0, -1]])
Hw = mat([[1, 1], [1, -1]]) / mp.sqrt(2)


def maxabs(M):
    return max(abs(M[i, j]) for i in range(M.rows) for j in range(M.cols))


def b(c, z):
    return (z - c) / (1 - mp.conj(c) * z)


# ---------------------------------------------------------------- definitions from the sources
def B_old(q, s):
    """Oldform coefficient matrix B_q(s) = [[1, q^s],[q^s, 1]] (deninger-cusp D3.4)."""
    return mat([[1, mp.mpf(q) ** s], [mp.mpf(q) ** s, 1]])


def M_of_s(q, s):
    """M_q(s) = B_q(1-s) B_q(s)^{-1}: the rational trivial block without phi."""
    return B_old(q, 1 - s) * B_old(q, s) ** -1


def M_of_z(q, z):
    """(1.1): M(z) = (qz^2-1)^{-1} [[q-1, sqrt q (z - 1/z)],[sqrt q (z - 1/z), q-1]]."""
    sq = mp.sqrt(q)
    return mat([[q - 1, sq * (z - 1 / z)], [sq * (z - 1 / z), q - 1]]) / (q * z ** 2 - 1)


def S_diagram(T, z, W=None):
    """04k scattering matrix for a real symmetric core T with W = I, C = I: S = -Q(z)^{-1} Q(1/z)."""
    n = T.rows
    lam = z + 1 / z
    G = (lam * mp.eye(n) - T) ** -1
    Q = lambda zz: mp.eye(n) - zz * G  # G is invariant under z <-> 1/z (same lambda)
    return -(Q(z) ** -1) * Q(1 / z)


def S_t_closed(t, z):
    """(1.7): S_t = -z (I - t z F)^{-1} (z I - t F)."""
    return -z * ((I2 - t * z * F) ** -1) * (z * I2 - t * F)


# ---------------------------------------------------------------- L1.1 the matrix and its algebra
s0 = mp.mpc("0.7", "0.3")
table = {5: (mp.mpc("0.218634648327814", "-0.387681428625362"), mp.mpc("0.282655097128056", "-0.006293311464958"),
             mp.mpc("-0.182350078814851", "-0.165963512494691"), mp.mpf("1.50604826933")),
         7: (mp.mpc("0.134991110996399", "-0.379918588305854"), mp.mpc("0.238480995379373", "-0.040919736670041"),
             mp.mpc("-0.181314294000262", "-0.083054105583715"), mp.mpf("1.66362344181"))}
print("=== L1.1: M_q at s = 0.7 + 0.3i, two definitions ===")
for q in (5, 7):
    z = mp.mpf(q) ** (s0 - mp.mpf(1) / 2)
    Ms = M_of_s(q, s0)
    Mz = M_of_z(q, z)
    check(maxabs(Ms - Mz) < mp.mpf(10) ** -35, "q=%d: M_q(s) = B(1-s)B(s)^{-1} equals the closed form (1.1)" % q,
          mp.nstr(maxabs(Ms - Mz), 3))
    dg, od, dt, _ = table[q]
    check(abs(Ms[0, 0] - dg) < 1e-14 and abs(Ms[1, 1] - dg) < 1e-14 and abs(Ms[0, 1] - od) < 1e-14,
          "q=%d: diagonal and off-diagonal entries match the prover's table" % q,
          mp.nstr(Ms[0, 0], 15) + " " + mp.nstr(Ms[0, 1], 15))
    detM = mp.det(Ms)
    detF = (1 - mp.mpf(q) ** (2 - 2 * s0)) / (1 - mp.mpf(q) ** (2 * s0))
    check(abs(detM - dt) < 1e-14 and abs(detM - detF) < mp.mpf(10) ** -35,
          "q=%d: det M = (1 - q^{2-2s})/(1 - q^{2s}) = table value" % q, mp.nstr(detM, 15))
    # functional equation M(s) M(1-s) = I
    fe = maxabs(M_of_s(q, s0) * M_of_s(q, 1 - s0) - I2)
    check(fe < mp.mpf(10) ** -35, "q=%d: functional equation M_q(s) M_q(1-s) = I" % q, mp.nstr(fe, 3))
    # (1.2) diagonalisation by H
    a = 1 / mp.sqrt(q)
    dia = Hw.T * Mz * Hw
    mplus = (z + mp.sqrt(q)) / (z * (1 + mp.sqrt(q) * z))
    mminus = (z - mp.sqrt(q)) / (z * (1 - mp.sqrt(q) * z))
    ok = abs(dia[0, 0] - mplus) < 1e-35 and abs(dia[1, 1] - mminus) < 1e-35 and abs(dia[0, 1]) < 1e-35 and abs(dia[1, 0]) < 1e-35
    ok2 = abs(mplus - 1 / (z * b(-a, z))) < 1e-35 and abs(mminus - 1 / (z * b(a, z))) < 1e-35
    check(ok and ok2, "q=%d: H^T M H = diag(m+, m-) with m+ = 1/(z b_{-a}), m- = 1/(z b_a)" % q)
    # (1.3) det of the inverse
    L = Mz ** -1
    detL = z ** 2 * (z ** 2 - a ** 2) / (1 - a ** 2 * z ** 2)
    check(abs(mp.det(L) - detL) < 1e-35, "q=%d: det M^{-1} = z^2 (z^2 - a^2)/(1 - a^2 z^2)" % q, mp.nstr(mp.det(L), 12))

# ---------------------------------------------------------------- L1.2 impossibility at the fixed cut
print("=== L1.2: M has a pole at z = 0, every finite-core S is regular there ===")
q = 5
zs = [mp.mpf(10) ** -k for k in (3, 5, 7)]
vals = [abs(M_of_z(q, z)[0, 1] * z) for z in zs]
check(all(abs(v - mp.sqrt(q)) < mp.mpf(10) ** -5 for v in vals) and abs(vals[-1] - mp.sqrt(q)) < 1e-13,
      "q=5: z M_12(z) -> sqrt q as z -> 0 (simple pole of the off-diagonal)", mp.nstr(vals[-1], 12))
dets = [mp.det(M_of_z(q, z)) * z ** 2 for z in zs]
check(abs(dets[-1] + q) < 1e-12, "q=5: z^2 det M(z) -> -q (double pole of det M; (1.3) gives (z^2-q)/(z^2(1-qz^2)))", mp.nstr(dets[-1], 12))
# random symmetric cores with W = I: S(z) -> W^*W - I = 0 as z -> 0; with W general S(0) = W^*W - I
rng = np.random.default_rng(20260922)
worst = mp.mpf(0)
for trial in range(3):
    n = 3
    A = rng.standard_normal((n, n)); A = (A + A.T) / 2
    T = mat(A.tolist())
    Wn = rng.standard_normal((n, 2))
    W = mat(Wn.tolist())
    z = mp.mpf(10) ** -6
    lam = z + 1 / z
    G = W.T * ((lam * mp.eye(n) - T) ** -1) * W
    Q = lambda zz: I2 - zz * G
    S = -(Q(z) ** -1) * Q(1 / z)
    worst = max(worst, maxabs(S - (W.T * W - I2)))
check(worst < 1e-4, "three random symmetric cores (n=3, two rays): S(z) -> W^*W - I as z -> 0 (regular; no pole)",
      mp.nstr(worst, 3))

# ---------------------------------------------------------------- L1.3 the weighted-edge realisation
print("=== L1.3: S_t from the 04k definition versus the closed form (1.6)-(1.7) ===")
for q in (5, 7):
    z = mp.mpf(q) ** (s0 - mp.mpf(1) / 2)
    a = 1 / mp.sqrt(q)
    for t, name in ((a, "a"), (mp.sqrt(q), "sqrt q")):
        Sd = S_diagram(t * F, z)
        Sc = S_t_closed(t, z)
        check(maxabs(Sd - Sc) < 1e-35, "q=%d, t=%s: S_t = -Q(z)^{-1}Q(1/z) equals -z(I - tzF)^{-1}(zI - tF)" % (q, name),
              mp.nstr(maxabs(Sd - Sc), 3))
        p_t = z ** 2 * (z ** 2 - t ** 2)
        pt_t = 1 - t ** 2 * z ** 2
        check(abs(mp.det(Sd) - p_t / pt_t) < 1e-35, "q=%d, t=%s: det S_t = p_t/ptilde_t with p_t = z^2(z^2-t^2), ptilde_t = 1 - t^2 z^2" % (q, name))
    Sa = S_diagram(a * F, z)
    Mz = M_of_z(q, z)
    L = Mz ** -1
    check(maxabs(L + Dm * Sa * Dm) < 1e-35 and maxabs(Mz + Dm * (Sa ** -1) * Dm) < 1e-35,
          "q=%d: (1.8) M^{-1} = -D S_a D and M = -D S_a^{-1} D" % q)
    err_false = maxabs(Mz - Sa)
    check(abs(err_false - table[q][3]) < 1e-9, "q=%d: the raw equality M = S_a FAILS, max entry error as in the table" % q,
          mp.nstr(err_false, 12))
    # eigenchannels of S_a: symmetric (1,1) -> -z b_a, antisymmetric (1,-1) -> -z b_{-a}
    v1 = mat([[1], [1]]); v2 = mat([[1], [-1]])
    e1 = (Sa * v1)[0, 0] / v1[0, 0]; e2 = (Sa * v2)[0, 0] / v2[0, 0]
    check(maxabs(Sa * v1 - e1 * v1) < 1e-35 and abs(e1 + z * b(a, z)) < 1e-35 and maxabs(Sa * v2 - e2 * v2) < 1e-35
          and abs(e2 + z * b(-a, z)) < 1e-35, "q=%d: S_a eigenvalues -z b_a on (1,1) and -z b_{-a} on (1,-1)" % q)
    # (1.10) the genuine cusp toy
    Ssq = S_diagram(mp.sqrt(q) * F, z)
    check(maxabs(Ssq + z ** 2 * Dm * Mz * Dm) < 1e-35, "q=%d: (1.10) S_{sqrt q} = -z^2 D M D" % q)
    # bound states of the genuine cusp toy: ptilde zeros at +-a, eigenvalue +-(sqrt q + 1/sqrt q), core vector (1,+-1)
    ok = True
    for th, v in ((a, v1), (-a, v2)):
        lam = th + 1 / th
        # ray amplitudes th^k times core value: core equation (lambda - th) x = T x
        res = maxabs((lam - th) * v - mp.sqrt(q) * F * v)
        ok = ok and res < 1e-35 and abs(1 - q * th ** 2) < 1e-35
    check(ok, "q=%d: bound states of S_{sqrt q} at z = +-a (ptilde = 0), eigenvalue +-(sqrt q + 1/sqrt q), core vector (1,+-1)" % q)
    # S_a has no disk poles: ptilde_a = 1 - a^2 z^2 has zeros at |z| = sqrt q > 1
    check(abs(1 / a) > 1, "q=%d: S_a has no bound states (ptilde_a zeros at |z| = sqrt q > 1); resonances at +-a and two delays" % q)

# ---------------------------------------------------------------- L1.6 comb, cancelled point, constant
print("=== L1.6: combs, the cancelled point, M_q(1) ===")
spacing_tab = {5: mp.mpf("3.90396253166234"), 7: mp.mpf("3.22891851416156")}
Lneg_tab = {5: mp.mpf("-0.402359478108525"), 7: mp.mpf("-0.324318358175886")}
for q in (5, 7):
    ell = mp.log(q); a = 1 / mp.sqrt(q)
    Lm = lambda tau: (lambda u: u * b(a, u))(mp.exp(1j * ell * tau))
    Lp = lambda tau: (lambda u: u * b(-a, u))(mp.exp(1j * ell * tau))
    r = lambda tau: (tau - 0.5j) / (tau + 0.5j)
    worst = mp.mpf(0)
    for k in range(-4, 5):
        worst = max(worst, abs(Lm(2 * mp.pi * k / ell + 0.5j)), abs(Lp((2 * k + 1) * mp.pi / ell + 0.5j)))
    check(worst < 1e-35, "q=%d: L_- vanishes at 2 pi k/ell + i/2 and L_+ at (2k+1) pi/ell + i/2, k = -4..4 (height 1/2)" % q,
          mp.nstr(worst, 3))
    check(abs(2 * mp.pi / ell - spacing_tab[q]) < 1e-13, "q=%d: comb spacing 2 pi/log q" % q, mp.nstr(2 * mp.pi / ell, 15))
    # the point k = 0 of L_- is cancelled by r: the limit of L_-/r at i/2
    lim = mp.limit(lambda t: Lm(0.5j + t) / r(0.5j + t), 0)
    # cross-check with the derivative formula L_-'(i/2)/r'(i/2), r'(i/2) = -i
    dLm = mp.diff(Lm, 0.5j)
    check(abs(lim + ell / (q - 1)) < 1e-12 and abs(lim - Lneg_tab[q]) < 1e-12 and abs(dLm - 1j * ell / (q - 1)) < 1e-12,
          "q=%d: (N.1) (L_-/r)(i/2) = -log q/(q-1), L_-'(i/2) = i log q/(q-1)" % q, mp.nstr(lim, 15))
    # M_q(1) = all-ones/(q+1); regular at s = 1
    M1 = M_of_s(q, mp.mpf(1))
    check(maxabs(M1 - mat([[1, 1], [1, 1]]) / (q + 1)) < 1e-35, "q=%d: M_q(1) = (q+1)^{-1} all-ones (no pole of M at s = 1)" % q)

# ---------------------------------------------------------------- L2.2 disk model, delay space
print("=== L2.2: the disk model (2.10), the geometric norm sum, the delay Gram ===")
for c in (1 / mp.sqrt(5), -1 / mp.sqrt(7)):
    Zc = mat([[0, 0], [mp.sqrt(1 - c ** 2), c]])
    Jc = mat([[-c, mp.sqrt(1 - c ** 2)]])
    check(maxabs(I2 - Zc.T * Zc - Jc.T * Jc) < 1e-35, "c=%s: I - Z_c^* Z_c = J_c^* J_c" % mp.nstr(c, 6))
    ev = sorted([abs(e) for e in mp.eig(Zc)[0]])
    check(abs(ev[0]) < 1e-35 and abs(ev[1] - abs(c)) < 1e-35, "c=%s: spec Z_c = {0, c} (delay mode and resonance)" % mp.nstr(c, 6))
    check(abs((1 - c ** 2) * mp.nsum(lambda n: c ** (2 * n), [0, mp.inf]) - 1) < 1e-30, "c=%s: (1 - c^2) sum c^{2n} = 1" % mp.nstr(c, 6))
ell = mp.log(5)
js = list(range(-3, 5))
G = mp.matrix(len(js), len(js))
for i, j1 in enumerate(js):
    for k, j2 in enumerate(js):
        G[i, k] = mp.quad(lambda X: mp.exp(2j * mp.pi * (j1 - j2) * X / ell), [0, ell]) / ell
check(maxabs(G - mp.eye(len(js))) < 1e-14, "delay space L^2(0, log 5): eight functions ell^{-1/2} e^{2 pi i j X/ell} have identity Gram",
      mp.nstr(maxabs(G - mp.eye(len(js))), 3))

# ---------------------------------------------------------------- L2.1/2.3/2.4: cascade on a finite disk model
print("=== L2: K_{AB} = K_A + A K_B and the triangular cascade on finite Blaschke models ===")
# Hardy space of the disk, <f,g> = int f conj(g); k_c(z) = 1/(1 - conj(c) z), <f, k_c> = f(c).
c1, c2 = mp.mpc("0.3", "0.2"), mp.mpc("-0.5", "0.1")
kc = lambda c: (lambda z: 1 / (1 - mp.conj(c) * z))
A = lambda z: b(c1, z)
# K_A = span{k_c1}, A K_B = span{A k_c2}; orthogonality: <k_c1, A k_c2> = conj(<A k_c2, k_c1>) = conj(A(c1) k_c2(c1)) = 0
ip_cross = mp.conj(A(c1) * kc(c2)(c1))
check(abs(ip_cross) < 1e-35, "K_A perp A K_B for A = b_{c1}, B = b_{c2} (reproducing-kernel evaluation)")
# K_{AB} = span{k_c1, k_c2}; compressed shift Z f = P_K (w f), computed exactly via Gram matrices
# basis u1 = k_c1, u2 = k_c2; w k_c = (k_c - 1)/conj(c); P_K 1 = sum_i alpha_i k_ci with Gram solve of <1, k_ci> = 1
Gram = mat([[kc(c1)(c1), kc(c2)(c1)], [kc(c1)(c2), kc(c2)(c2)]])  # G_ij = <k_i, k_j> = k_i(c_j)... careful:
# <k_ci, k_cj> = k_ci(c_j) = 1/(1 - conj(c_i) c_j)
Gram = mat([[1 / (1 - mp.conj(c1) * c1), 1 / (1 - mp.conj(c1) * c2)], [1 / (1 - mp.conj(c2) * c1), 1 / (1 - mp.conj(c2) * c2)]])
# projection coefficients of 1: <1, k_cj> = 1 for both, solve Gram^T alpha = (1,1)
alpha = (Gram.T) ** -1 * mat([[1], [1]])
# Z k_ci = (k_ci - P1)/conj(c_i): matrix in basis (k_c1, k_c2)
Zb = mp.matrix(2, 2)
for i, ci in enumerate((c1, c2)):
    col = [mp.mpc(0)] * 2
    col[i] += 1
    for j in range(2):
        col[j] -= alpha[j]
    for j in range(2):
        Zb[j, i] = col[j] / mp.conj(ci)
# change to the orthonormal basis e1 = sqrt(1-|c1|^2) k_c1, e2 = A k_c2 / ||A k_c2|| = sqrt(1-|c2|^2) A k_c2
# express A k_c2 in the basis (k_c1, k_c2): A k_c2 = (z - c1)/((1 - conj(c1) z)(1 - conj(c2) z)) = x k_c1 + y k_c2 by partial fractions
# (z - c1)/((1-conj(c1)z)(1-conj(c2)z)): evaluate at two points to solve
def Ak2(z): return A(z) * kc(c2)(z)
z1, z2 = mp.mpc("0.1", "0.05"), mp.mpc("-0.2", "0.3")
sol = mat([[kc(c1)(z1), kc(c2)(z1)], [kc(c1)(z2), kc(c2)(z2)]]) ** -1 * mat([[Ak2(z1)], [Ak2(z2)]])
x, y = sol[0], sol[1]
z3 = mp.mpc("0.4", "-0.2")
check(abs(x * kc(c1)(z3) + y * kc(c2)(z3) - Ak2(z3)) < 1e-30, "A k_{c2} = x k_{c1} + y k_{c2} (partial fractions) checked at a third point")
n1 = mp.sqrt(1 - abs(c1) ** 2); n2 = mp.sqrt(1 - abs(c2) ** 2)
P = mat([[n1, n2 * x], [0, n2 * y]])  # columns: e1, e2 in basis (k_c1, k_c2)
Zon = P ** -1 * Zb * P
check(abs(Zon[0, 1]) < 1e-30 and abs(Zon[0, 0] - c1) < 1e-30 and abs(Zon[1, 1] - c2) < 1e-30,
      "(2.13)/(2.15): U_A^* Z_{AB} U_A is lower triangular with diagonal Z_A = c1, Z_B = c2", mp.nstr(Zon[1, 0], 12))
# predicted coupling k_0^B J_A: J_A e1 = sqrt(1-|c1|^2), <k_0^B, e2'> with e2' = sqrt(1-|c2|^2) k_c2: = sqrt(1-|c2|^2)
check(abs(Zon[1, 0] - n1 * n2) < 1e-30, "coupling entry equals k_0^B J_A = sqrt(1-|c1|^2) sqrt(1-|c2|^2)", mp.nstr(n1 * n2, 12))
# exit: I - Z^*Z = J^*J rank one with norm 1 - |I(0)|^2 = 1 - |c1 c2|^2  (2.16); Z in an orthonormal basis is Zon
Ex = mp.eye(2) - Zon.H * Zon
ev = sorted([mp.re(e) for e in mp.eig(Ex)[0]])
check(abs(ev[0]) < 1e-30 and abs(ev[1] - (1 - abs(c1 * c2) ** 2)) < 1e-30,
      "(2.16): I - Z_{AB}^* Z_{AB} has rank one with norm 1 - |I(0)|^2 = 1 - |c1 c2|^2", mp.nstr(ev[1], 12))
# J_{AB}(f,g) = conj(B(0)) J_A f + J_B g: check the rank-one factor against this row in the orthonormal basis
JA = n1  # J_A e1
JB = n2  # J_B e2 (same computation for a single Blaschke factor)
row = mat([[mp.conj(-c2) * JA, JB]])
check(maxabs(Ex - row.H * row) < 1e-30, "J_{AB} = conj(B(0)) J_A (+) J_B reproduces the defect operator")

# ---------------------------------------------------------------- L3: N = 35 tensor and Walsh channels
print("=== L3: N = 35 ===")
q1, q2 = 5, 7
B35 = lambda s: kron(B_old(q1, s), B_old(q2, s))


def kron(A, B):
    C = mp.matrix(A.rows * B.rows, A.cols * B.cols)
    for i in range(A.rows):
        for j in range(A.cols):
            for k in range(B.rows):
                for l in range(B.cols):
                    C[i * B.rows + k, j * B.cols + l] = A[i, j] * B[k, l]
    return C


M35 = B35(1 - s0) * B35(s0) ** -1
MM = kron(M_of_s(q1, s0), M_of_s(q2, s0))
check(maxabs(M35 - MM) < 1e-33, "(3.1) B_35(1-s) B_35(s)^{-1} = M_5(s) (x) M_7(s)", mp.nstr(maxabs(M35 - MM), 3))
HH = kron(Hw, Hw)
Dg = HH.T * M35 * HH
off = max(abs(Dg[i, j]) for i in range(4) for j in range(4) if i != j)
z5 = mp.mpf(5) ** (s0 - mp.mpf(1) / 2); z7 = mp.mpf(7) ** (s0 - mp.mpf(1) / 2)
mps = lambda q, z, sg: (z + sg * mp.sqrt(q)) / (z * (1 + sg * mp.sqrt(q) * z))
pred = [mps(5, z5, 1) * mps(7, z7, 1), mps(5, z5, 1) * mps(7, z7, -1), mps(5, z5, -1) * mps(7, z7, 1), mps(5, z5, -1) * mps(7, z7, -1)]
okd = all(abs(Dg[i, i] - pred[i]) < 1e-33 for i in range(4))
check(off < 1e-33 and okd, "Walsh transform H(x)H diagonalises M_35 with eigenvalues m_{5,e5} m_{7,e7}", mp.nstr(off, 3))
check(abs(mp.det(M35) - mp.det(M_of_s(5, s0)) ** 2 * mp.det(M_of_s(7, s0)) ** 2) < 1e-33,
      "det M_35 = (det M_5)^2 (det M_7)^2")
check(maxabs(M35 * (B35(s0) * B35(1 - s0) ** -1) - mp.eye(4)) < 1e-33, "M_35(s) M_35(1-s) = I")
# residual orders at tau = i/2 of the reduced local factors B_eps (3.3)
ell5, ell7 = mp.log(5), mp.log(7)
a5, a7 = 1 / mp.sqrt(5), 1 / mp.sqrt(7)
Lq = lambda q, c: (lambda tau: (lambda u: u * b(c, u))(mp.exp(1j * mp.log(q) * tau)))
r = lambda tau: (tau - 0.5j) / (tau + 0.5j)
def order_at(f, t0, tol=1e-20):
    """order of vanishing of f at t0 via values on a shrinking circle (log-log slope)."""
    h1, h2 = mp.mpf("1e-4"), mp.mpf("1e-5")
    v1 = max(abs(f(t0 + h1 * mp.exp(2j * mp.pi * k / 6))) for k in range(6))
    v2 = max(abs(f(t0 + h2 * mp.exp(2j * mp.pi * k / 6))) for k in range(6))
    return mp.log(v1 / v2) / mp.log(h1 / h2)
chans = {"++": lambda t: Lq(5, -a5)(t) * Lq(7, -a7)(t),
         "+-": lambda t: Lq(5, -a5)(t) * Lq(7, a7)(t) / r(t),
         "-+": lambda t: Lq(5, a5)(t) * Lq(7, -a7)(t) / r(t),
         "--": lambda t: Lq(5, a5)(t) * Lq(7, a7)(t) / r(t)}
orders = {k: order_at(f, mp.mpc(0, 0.5)) for k, f in chans.items()}
check(all(abs(orders[k] - o) < 0.01 for k, o in (("++", 0), ("+-", 0), ("-+", 0), ("--", 1))),
      "residual orders at i/2 of the reduced channels ++, +-, -+, --: 0, 0, 0, 1",
      " ".join("%s:%s" % (k, mp.nstr(v, 4)) for k, v in orders.items()))
# incommensurability: log5/log7 irrational is exact; report the continued-fraction sanity (no small integer relation)
rat = mp.log(5) / mp.log(7)
best = min(abs(rat - mp.mpf(p) / qq) for qq in range(1, 200) for p in range(1, 400))
check(best > 1e-6, "no integer relation m log 5 = n log 7 with n < 200 (incommensurate periods)", mp.nstr(best, 3))

# ---------------------------------------------------------------- L4: phase derivative and the prime-power comb
print("=== L4: phase derivative of the local channels ===")
for q in (5, 7):
    ell = mp.log(q); a = 1 / mp.sqrt(q); tau0 = mp.mpf("0.23")
    for c in (a, -a):
        f = lambda t: (lambda u: u * b(c, u))(mp.exp(1j * ell * t))
        lhs = mp.diff(lambda t: mp.log(f(t)), tau0) / 1j
        rhs = ell * (2 + 2 * mp.nsum(lambda n: c ** n * mp.cos(n * ell * tau0), [1, mp.inf]))
        check(abs(lhs - rhs) < 1e-25, "q=%d, c=%s: (1/i) d/dtau log(u b_c(u)) = ell[2 + 2 sum c^n cos(n ell tau)] at tau = 0.23" % (q, mp.nstr(c, 5)),
              mp.nstr(mp.re(lhs), 15))
    fsum = lambda t: mp.log((lambda u: u * b(a, u) * u * b(-a, u))(mp.exp(1j * ell * t)))
    lhs = mp.diff(fsum, tau0) / 1j
    rhs = 4 * ell * (1 + mp.nsum(lambda m: mp.mpf(q) ** (-m) * mp.cos(2 * m * ell * tau0), [1, mp.inf]))
    check(abs(lhs - rhs) < 1e-25, "q=%d: phase derivative of L_+ L_- = 4 ell [1 + sum q^{-m} cos(2 m ell tau)] (odd harmonics cancel)" % q,
          mp.nstr(mp.re(lhs), 15))

# ---------------------------------------------------------------- summary
npass = sum(1 for ok, _, _ in LEDGER if ok)
print("=== %d checks, %d pass, %d fail; %.1f s ===" % (len(LEDGER), npass, len(LEDGER) - npass, time.time() - T0))
