#!/usr/bin/env python3
"""Checks and figures for 'The GKP reading of Weil positivity, tested on Ramanujan graphs'.

Conventions. X a connected (q+1)-regular simple graph, n vertices, adjacency A. Directed edges e = (o, t).
Hashimoto operator on edge functions: (B phi)(e) = sum over f with o(f) = t(e), f != reverse(e) of phi(f).
N_k = Tr B^k = number of closed, cyclically non-backtracking walks of length k.
Lifts: (sigma f)(e) = f(o(e)), (tau g)(e) = g(t(e)).  M = [[0, -1], [q, A]] on C^V + C^V.
Omega = [[0, 1], [-1, 0]].  Weil form Q = [[q, A/2], [A/2, 1]].  S = M / sqrt(q).
Lines: eigenvalues w = mu / sqrt(q) of S; Ramanujan iff all nontrivial w lie on the unit circle.
Echo of the nontrivial lines: C(k) = sum w^k.
"""
import os
import itertools
from fractions import Fraction
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
NOTE = os.path.dirname(HERE)          # figures are written next to the note
npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


# ------------------------------------------------------------------------------------------ graphs
def from_edges(n, edges):
    A = np.zeros((n, n), dtype=np.int64)
    for a, b in edges:
        A[a, b] = A[b, a] = 1
    return A

def K(n):
    return from_edges(n, [(a, b) for a in range(n) for b in range(a + 1, n)])

def petersen():
    e = [(i, (i + 1) % 5) for i in range(5)] + [(i, i + 5) for i in range(5)] + [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    return from_edges(10, e)

def prism(m):
    e = [(i, (i + 1) % m) for i in range(m)] + [(m + i, m + (i + 1) % m) for i in range(m)] + [(i, m + i) for i in range(m)]
    return from_edges(2 * m, e)

def hashimoto(A):
    n = len(A)
    E = [(a, b) for a in range(n) for b in range(n) if A[a, b]]
    idx = {e: i for i, e in enumerate(E)}
    B = np.zeros((len(E), len(E)), dtype=object)
    for (a, b), i in idx.items():
        for c in range(n):
            if A[b, c] and c != a:
                B[i, idx[(b, c)]] = 1
    sig = np.zeros((len(E), n), dtype=object)
    tau = np.zeros((len(E), n), dtype=object)
    for (a, b), i in idx.items():
        sig[i, a] = 1
        tau[i, b] = 1
    return E, B, sig, tau

def blocks(A, q):
    n = len(A)
    I, Z = np.eye(n, dtype=object), np.zeros((n, n), dtype=object)
    Ao = A.astype(object)
    M = np.block([[Z, -I], [q * I, Ao]])
    Om = np.block([[Z, I], [-I, Z]])
    return M, Om

def walk_counts(B, kmax):
    out, P = [len(B)], np.eye(len(B), dtype=object)
    for _ in range(kmax):
        P = P.dot(B)
        out.append(int(np.trace(P)))
    return out

def is_bipartite(A):
    ev = np.linalg.eigvalsh(A.astype(float))
    return abs(ev[0] + ev[-1]) < 1e-9

def echo_from_walks(A, q, kmax):
    """C(k), k = 0..kmax, of the nontrivial lines, from walk counts, tree term and trivial pair only (exact integers)."""
    n = len(A)
    _, B, _, _ = hashimoto(A)
    N = walk_counts(B, kmax)
    r1 = n * (q - 1) // 2
    bip = is_bipartite(A)
    C = [2.0 * (n - (2 if bip else 1))]
    for k in range(1, kmax + 1):
        num = N[k] - r1 * (1 + (-1) ** k) - (q ** k + 1) - ((-q) ** k + (-1) ** k if bip else 0)
        C.append(float(Fraction(num)) / q ** (k / 2))
    return np.array(C), N

def lines(A, q):
    lam = np.linalg.eigvalsh(A.astype(float))
    w = []
    for l in lam:
        d = np.sqrt(complex(l * l - 4 * q))
        w += [(l + d) / (2 * np.sqrt(q)), (l - d) / (2 * np.sqrt(q))]
    return lam, np.array(w)

def toeplitz(c):
    n = len(c)
    return np.array([[c[abs(j - k)] for k in range(n)] for j in range(n)], float)


GRAPHS = {"K4": (K(4), 2), "Petersen": (petersen(), 2), "cube": (prism(4), 2), "K5": (K(5), 3), "prism21": (prism(21), 2)}

# ------------------------------------------------------------------------------------------ H1-H4
print("== H1  edge space, vertex-induced space, symplectic structure, Weil form")
for name, (A, q) in GRAPHS.items():
    n = len(A)
    E, B, sig, tau = hashimoto(A)
    M, Om = blocks(A, q)
    Pi = np.hstack([sig, tau])
    check(f"{name}: B [sigma tau] = [sigma tau] M", np.array_equal(B.dot(Pi), Pi.dot(M)))
    check(f"{name}: M^T Omega M = q Omega", np.array_equal(M.T.dot(Om).dot(M), q * Om))
    I, Z = np.eye(n, dtype=object), np.zeros((n, n), dtype=object)
    Ao = A.astype(object)
    CA = np.block([[Z, -I], [I, Ao]])
    Fo = np.block([[Z, -I], [I, Z]])
    Sh = np.block([[I, Z], [-Ao, I]])
    check(f"{name}: M = C_A diag(q,1), C_A = Shear(-A) F integral symplectic",
          np.array_equal(M, CA.dot(np.block([[q * I, Z], [Z, I]]))) and np.array_equal(CA, Sh.dot(Fo))
          and np.array_equal(CA.T.dot(Om).dot(CA), Om))
    Q2 = np.block([[2 * q * I, Ao], [Ao, 2 * I]])            # 2 Q
    qMinv = np.block([[Ao, I], [-q * I, Z]])
    check(f"{name}: Weil form invariant, M^T Q M = q Q, and 2Q = Omega (M - q M^-1)",
          np.array_equal(M.T.dot(Q2).dot(M), q * Q2) and np.array_equal(M.dot(qMinv), q * np.eye(2 * n, dtype=object))
          and np.array_equal(Om.dot(M - qMinv), Q2))
    lam, w = lines(A, q)
    ev = np.linalg.eigvalsh(Q2.astype(float) / 2)
    neg = int(np.sum(ev < -1e-9))
    nontriv = lam[np.abs(np.abs(lam) - (q + 1)) > 1e-9]
    ram = bool(np.all(np.abs(nontriv) <= 2 * np.sqrt(q) + 1e-12))
    off = int(np.sum(np.abs(nontriv) > 2 * np.sqrt(q) + 1e-12))
    ntriv = len(lam) - len(nontriv)
    check(f"{name}: negative index of Q = (trivial eigenvalues) + (off-band eigenvalues)", neg == ntriv + off,
          f"n = {n}, q = {q}, Ramanujan = {ram}, max nontrivial |lambda| = {np.max(np.abs(nontriv)):.4f} vs 2 sqrt q = {2*np.sqrt(q):.4f}, negative index {neg}")
I2 = np.eye(2)
S0 = np.array([[0, -1], [1, 0]]) @ np.diag([np.sqrt(2), 1 / np.sqrt(2)])
check("with A = 0 the step (Fourier after squeeze) squares to -1", np.allclose(S0 @ S0, -I2))

# ------------------------------------------------------------------------------------------ H5
print("== H5  walk counts, prime cycles, Ihara-Bass")
A, q = GRAPHS["K4"]
E, B, _, _ = hashimoto(A)
N = walk_counts(B, 12)
def brute(A, k):
    n, c = len(A), 0
    for v in itertools.product(range(n), repeat=k):
        if all(A[v[i], v[(i + 1) % k]] for i in range(k)) and all(v[i] != v[(i + 2) % k] for i in range(k)):
            c += 1
    return c
bf = [brute(A, k) for k in range(3, 9)]
check("K4: Tr B^k equals a brute-force count of closed cyclically non-backtracking walks, k = 3..8", bf == N[3:9], f"{N[3:9]}")
def mobius(m):
    res, p = 1, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            res = -res
        p += 1
    return -res if m > 1 else res
prim = {l: sum(mobius(l // d) * N[d] for d in range(1, l + 1) if l % d == 0) // l for l in range(1, 13)}
check("K4: numbers of prime cycles are nonnegative integers", all(v >= 0 for v in prim.values()) and
      all(sum(d * prim[d] for d in range(1, k + 1) if k % d == 0) == N[k] for k in range(1, 13)), f"pi(3..8) = {[prim[l] for l in range(3, 9)]}")
for name in ("K4", "Petersen", "prism21"):
    A, q = GRAPHS[name]
    n = len(A)
    _, B, _, _ = hashimoto(A)
    Nk = walk_counts(B, 14)
    lam, w = lines(A, q)
    r1 = n * (q - 1) // 2
    pred = [r1 * (1 + (-1) ** k) + np.sum((w * np.sqrt(q)) ** k).real for k in range(1, 15)]
    check(f"{name}: Tr B^k = (r-1)(1+(-1)^k) + sum mu^k (Ihara-Bass), k = 1..14", np.allclose(pred, Nk[1:], rtol=1e-10, atol=1e-6))

# ------------------------------------------------------------------------------------------ H6
print("== H6  the tree term is n times the Kesten-McKay (Plancherel) measure")
for q in (2, 3, 4):
    th = np.linspace(0, np.pi, 20001)
    dens = (q + 1) * 4 * q * np.sin(th) ** 2 / (2 * np.pi * ((q + 1) ** 2 - 4 * q * np.cos(th) ** 2))
    def integ(y):
        return np.sum((y[1:] + y[:-1]) * np.diff(th)) / 2
    ok = abs(integ(dens) - 1) < 1e-10
    for k in range(1, 9):
        val = integ(2 * np.cos(k * th) * dens)
        ok &= abs(val - (-(q - 1) * q ** (-k / 2) if k % 2 == 0 else 0.0)) < 1e-10
    check(f"q = {q}: int 2cos(k theta) dKM = -(q-1) q^(-k/2) for even k, 0 for odd k (k = 1..8)", ok)

# ------------------------------------------------------------------------------------------ H7
print("== H7  Weil positivity in echo and Gram form, from walk counts only")
KMAX = 40
res = {}
for name in ("K4", "Petersen", "cube", "K5", "prism21"):
    A, q = GRAPHS[name]
    C, Nk = echo_from_walks(A, q, KMAX)
    lam, w = lines(A, q)
    wn = w[np.abs(np.abs(lam.repeat(2)) - (q + 1)) > 1e-9]
    Cspec = np.array([np.sum(wn ** k).real for k in range(KMAX + 1)])
    check(f"{name}: echo from walk counts equals the sum over nontrivial lines, k = 0..{KMAX}", np.allclose(C, Cspec, rtol=1e-9, atol=1e-6))
    ev = np.linalg.eigvalsh(toeplitz(C[:31]))
    res[name] = (C, wn, ev)
    print(f"      {name}: C(0) = {C[0]:.0f}, max |C(k)|/C(0) for 1 <= k <= {KMAX}: {np.max(np.abs(C[1:])) / C[0]:.4f}, "
          f"31 x 31 Gram eigenvalues in [{ev.min():.3e}, {ev.max():.2f}]")
for name in ("K4", "Petersen", "cube", "K5"):
    C, wn, ev = res[name]
    check(f"{name} (Ramanujan): echo bound and Gram positivity", np.max(np.abs(C)) <= C[0] + 1e-9 and ev.min() > -1e-8)
C, wn, ev = res["prism21"]
check("prism21 (not Ramanujan): Gram matrix has a negative eigenvalue", ev.min() < -1e-3, f"min eigenvalue {ev.min():.3f}")
first = int(np.argmax(np.abs(C) > C[0] + 1e-9))
check("prism21: echo exceeds its initial value", first > 0, f"first at k = {first}; |C(40)|/C(0) = {abs(C[40]) / C[0]:.1f}")
for L in (8, 12, 16, 20, 24):
    print(f"      prism21: smallest eigenvalue of the {L+1} x {L+1} Gram matrix: {np.linalg.eigvalsh(toeplitz(C[:L+1])).min():+.4f}")
offm = np.abs(np.abs(wn) - 1) > 1e-9
eta = np.log(np.max(np.abs(wn)))
Clor = np.array([np.sum(wn[~offm] ** k).real + np.sum(np.exp(-np.abs(np.log(np.abs(wn[offm]))) * k)) for k in range(KMAX + 1)])
evl = np.linalg.eigvalsh(toeplitz(Clor[:31]))
check("prism21: Lorentzian (Poisson) form of the same lines is positive", evl.min() > -1e-8 and np.max(np.abs(Clor)) <= Clor[0] + 1e-9,
      f"off-circle lines: {int(offm.sum())}, rate eta = {eta:.4f}, min eigenvalue {evl.min():.2e}")
res["prism21_lor"] = Clor

# ------------------------------------------------------------------------------------------ H8
print("== H8  K4 and the elliptic curve y^2 + xy = x^3 + 1 over F_2")
def f4mul(a, b):
    return ((a[0] * b[0] + a[1] * b[1]) % 2, (a[0] * b[1] + a[1] * b[0] + a[1] * b[1]) % 2)
def f4add(a, b):
    return ((a[0] + b[0]) % 2, (a[1] + b[1]) % 2)
F4 = [(0, 0), (1, 0), (0, 1), (1, 1)]
cnt2 = 1 + sum(1 for x in (0, 1) for y in (0, 1) if (y * y + x * y - x ** 3 - 1) % 2 == 0)
cnt4 = 1 + sum(1 for x in F4 for y in F4 if f4add(f4add(f4mul(y, y), f4mul(x, y)), f4add(f4mul(x, f4mul(x, x)), (1, 0))) == (0, 0))
check("E has 4 points over F_2 and 8 over F_4, so its L-polynomial is 1 + u + 2u^2", cnt2 == 4 and cnt4 == 8, f"{cnt2}, {cnt4}")
lam, _ = lines(GRAPHS["K4"][0], 2)
check("K4 has adjacency eigenvalues 3, -1, -1, -1: nontrivial factor (1 + u + 2u^2)^3", np.allclose(sorted(lam), [-1, -1, -1, 3]))
s = [2, -1]
for k in range(2, 13):
    s.append(-s[-1] - 2 * s[-2])
pts = [2 ** k + 1 - s[k] for k in range(13)]
check("#E(F_2^k) from the L-polynomial matches the brute-force counts at k = 1, 2", pts[1] == cnt2 and pts[2] == cnt4)
check("N_k(K4) + 3 #E(F_2^k) = 4 (2^k + 1) + 2 (1 + (-1)^k), k = 1..12",
      all(N[k] + 3 * pts[k] == 4 * (2 ** k + 1) + 2 * (1 + (-1) ** k) for k in range(1, 13)),
      f"N_k = {N[1:9]}, #E = {pts[1:9]}")

# ------------------------------------------------------------------------------------------ H9
print("== H9  C_A is the graph-state Clifford: Hadamards, then CZ along every edge (qubits, K4)")
A, q = GRAPHS["K4"]
n = 4
X1, Z1, H1 = np.array([[0, 1], [1, 0]]), np.diag([1, -1]), np.array([[1, 1], [1, -1]]) / np.sqrt(2)
def kron(ops):
    out = np.array([[1.0]])
    for o in ops:
        out = np.kron(out, o)
    return out
def pauli(x, z):
    return kron([np.linalg.matrix_power(X1, x[i]) @ np.linalg.matrix_power(Z1, z[i]) for i in range(n)])
CZ = np.diag([(-1.0) ** sum(A[a, b] * ((s >> (n - 1 - a)) & 1) * ((s >> (n - 1 - b)) & 1) for a in range(n) for b in range(a + 1, n)) for s in range(2 ** n)])
U = CZ @ kron([H1] * n)
allp = [(x, z) for x in itertools.product((0, 1), repeat=n) for z in itertools.product((0, 1), repeat=n)]
def image(x, z):
    P = U @ pauli(x, z) @ U.conj().T
    for (x2, z2) in allp:
        if abs(abs(np.trace(pauli(x2, z2).conj().T @ P)) - 2 ** n) < 1e-9:
            return list(x2) + list(z2)
cols = [image(tuple(int(i == v) for i in range(n)), (0,) * n) for v in range(n)] + [image((0,) * n, tuple(int(i == v) for i in range(n))) for v in range(n)]
Sym = np.array(cols).T
CA2 = np.block([[np.zeros((n, n), int), np.eye(n, dtype=int)], [np.eye(n, dtype=int), A]]) % 2
check("binary symplectic matrix of CZ_G H^(x4) equals [[0, 1], [1, A]] = C_A mod 2", np.array_equal(Sym, CA2))

# ------------------------------------------------------------------------------------------ H10
print("== H10  the p + 1 stabiliser bases of one qudit are mutually unbiased (one odd vertex of the tree)")
for p in (3, 5, 7):
    om = np.exp(2j * np.pi / p)
    Xp = np.roll(np.eye(p), 1, axis=0)
    Zp = np.diag(om ** np.arange(p))
    bases = [np.eye(p)] + [np.linalg.eig(Xp @ np.linalg.matrix_power(Zp, t))[1] for t in range(p)]
    ok = True
    for a in range(p + 1):
        for b in range(a + 1, p + 1):
            ov = np.abs(bases[a].conj().T @ bases[b])
            ok &= np.allclose(ov, p ** -0.5, atol=1e-9)
    check(f"p = {p}: {p + 1} bases, all cross overlaps equal p^(-1/2)", ok)

# ------------------------------------------------------------------------------------------ figures
INK, MUTED, GRID, AXIS, SURF = "#0b0b0b", "#52514e", "#e1e0d9", "#c3c2b7", "#fcfcfb"
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": AXIS, "axes.labelcolor": MUTED,
                     "xtick.color": MUTED, "ytick.color": MUTED, "axes.spines.top": False, "axes.spines.right": False,
                     "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF})

print("== Figure 1  line density of the Petersen graph from the walk side")
A, q = GRAPHS["Petersen"]
n = len(A)
KD, tauD = 70, 5.0
_, B, _, _ = hashimoto(A)
Nk = walk_counts(B, KD)
ks = np.arange(1, KD + 1)
wt = np.exp(-ks ** 2 / (4.0 * tauD ** 2))
tree = np.array([-(q - 1) * n * q ** (-k / 2) if k % 2 == 0 else 0.0 for k in ks])
triv = np.array([-(q ** (k / 2) + q ** (-k / 2)) for k in ks])
cyc = np.array([float(Fraction(Nk[k])) / q ** (k / 2) for k in ks])
th = np.linspace(0, np.pi, 1441)
cosm = np.cos(np.outer(ks, th))
def dens(c0, ck):
    return (c0 + 2 * (wt * ck) @ cosm) / (2 * np.pi)
short = np.where(ks <= 6, 1.0, 0.0)
d_bg = dens(2 * n - 2, tree + triv)
d_short = dens(2 * n - 2, tree + triv + cyc * short)
d_all = dens(2 * n - 2, tree + triv + cyc)
lam, w = lines(A, q)
wn = w[np.abs(np.abs(lam.repeat(2)) - (q + 1)) > 1e-9]
ang = np.angle(wn)
d_spec = np.zeros_like(th)
for k in range(-KD, KD + 1):
    d_spec += np.exp(-k ** 2 / (4 * tauD ** 2)) * np.sum(np.cos(k * (th[:, None] - ang[None, :])), axis=1) / (2 * np.pi)
check("Fig1 walk-side density equals the smoothed line list", np.max(np.abs(d_all - d_spec)) < 1e-6, f"max |diff| = {np.max(np.abs(d_all - d_spec)):.1e}")
check("Fig1 walk-side density is nonnegative on [0, pi]", d_all.min() > -1e-6, f"min = {d_all.min():.1e}")

fig, ax = plt.subplots(figsize=(9.6, 4.1), dpi=200)
ax.axhline(0, color=AXIS, lw=0.8)
ax.plot(th, d_bg, color=AQUA, lw=2, label="tree term − trivial pair")
ax.plot(th, d_short, color=ORANGE, lw=2, label="… plus cycles of length ≤ 6")
ax.plot(th, d_all, color=BLUE, lw=2, label="… plus all cycles")
tl = np.unique(np.round(ang[ang > 0], 9))
ax.plot(tl, np.full_like(tl, -1.6), "|", color=INK, ms=9, mew=1.2)
ax.text(np.pi + 0.03, -1.6, "lines", color=MUTED, va="center", fontsize=9)
i1, i2 = np.searchsorted(th, 1.62), np.searchsorted(th, 1.21)
ax.annotate("tree − trivial", (th[i1], d_bg[i1]), xytext=(0, 6), textcoords="offset points", color=INK, fontsize=9, ha="center")
ax.annotate("all cycles", (th[i2], d_all[i2]), xytext=(0, 6), textcoords="offset points", color=INK, fontsize=9, ha="center")
i3 = np.searchsorted(th, 0.95)
ax.annotate("cycles ≤ 6", (th[i3], d_short[i3]), xytext=(-6, 8), textcoords="offset points", color=INK, fontsize=9, ha="right")
ax.text(0.33, 17.2, "trivial pair\n(off scale)", color=MUTED, fontsize=9, va="top")
ax.set_ylim(-3.5, 18)
ax.set_xlim(0, np.pi)
ax.set_xticks([0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi])
ax.set_xticklabels(["0", "π/4", "π/2", "3π/4", "π"])
ax.set_xlabel("angle θ of the line on the unit circle")
ax.set_ylabel("lines per unit angle")
ax.grid(axis="y", color=GRID, lw=0.6)
ax.set_axisbelow(True)
ax.legend(frameon=False, loc="upper center", fontsize=9, labelcolor=INK, bbox_to_anchor=(0.5, 1.13), ncol=3)
fig.tight_layout()
fig.savefig(os.path.join(NOTE, "fig_graph_density.png"))
plt.close(fig)

print("== Figure 2  echo: Ramanujan graphs versus the prism on 42 vertices")
fig, ax = plt.subplots(figsize=(9.6, 3.9), dpi=200)
kk = np.arange(0, 31)
ax.axhline(1, color=AXIS, lw=0.8, ls=(0, (4, 3)))
ax.text(30.3, 1, "bound", color=MUTED, va="center", fontsize=9)
Cp = res["Petersen"][0]
Cz = res["prism21"][0]
Cl = res["prism21_lor"]
ax.plot(kk, np.abs(Cp[:31]) / Cp[0], color=BLUE, lw=2, marker="o", ms=4, label="Petersen (Ramanujan)")
ax.plot(kk, np.abs(Cl[:31]) / Cl[0], color=AQUA, lw=2, marker="o", ms=4, label="prism C₂₁×K₂, Lorentzian form")
ax.plot(kk, np.abs(Cz[:31]) / Cz[0], color=ORANGE, lw=2, marker="o", ms=4, label="prism C₂₁×K₂, Weil form")
ax.annotate("Weil form: past the bound from k = 10", (12, abs(Cz[12]) / Cz[0]), xytext=(-12, 10), textcoords="offset points", color=INK, fontsize=9, ha="right")
ax.set_xlim(0, 30)
ax.set_ylim(0, 2.6)
ax.set_xlabel("number of non-backtracking steps k")
ax.set_ylabel("|C(k)| / C(0)")
ax.grid(axis="y", color=GRID, lw=0.6)
ax.set_axisbelow(True)
ax.legend(frameon=False, loc="upper center", fontsize=9, labelcolor=INK, bbox_to_anchor=(0.5, 1.14), ncol=3)
fig.tight_layout()
fig.savefig(os.path.join(NOTE, "fig_graph_echo.png"))
plt.close(fig)

print(f"\n{npass} passed, {nfail} failed")
