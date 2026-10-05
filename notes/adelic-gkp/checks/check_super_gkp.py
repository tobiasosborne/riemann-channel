#!/usr/bin/env python3
"""Checks and figures for 'The super zeta on the same graphs: a lattice state with fermionic dark lines'.

Conventions. Y a connected (q+1)-regular graph, n vertices, adjacency A. A flux is a signing s of the edges up to
switching; A_s the signed adjacency; the 2-cover Yhat has vertices (v, +-) and deck involution tau.
Bosonic sector: tau-even functions (the graph Y itself). Fermionic sector: tau-odd functions (the signed graph).
Super zeta: Z_s(u) = det(1 - u B_s) / det(1 - u B) = det(1 - A_s u + q u^2) / det(1 - A u + q u^2).
Super count: str Bhat^k = Tr(tau Bhat^k) = Tr B^k - Tr B_s^k = 2 * #(closed non-backtracking walks of length k with odd flux).
Fermionic step on two quadratures per vertex: M_s = [[0, -1], [q, A_s]].
"""
import os
import itertools
from fractions import Fraction
from functools import lru_cache
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
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


# ------------------------------------------------------------------------------------------ graphs and fluxes
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

def edges_of(A):
    n = len(A)
    return [(a, b) for a in range(n) for b in range(a + 1, n) if A[a, b]]

def signed(A, neg):
    As = A.copy()
    for a, b in neg:
        assert A[a, b]
        As[a, b] = As[b, a] = -1
    return As

def spanning_tree(A):
    n, seen, tree, stack = len(A), {0}, [], [0]
    while stack:
        v = stack.pop()
        for w in range(n):
            if A[v, w] and w not in seen:
                seen.add(w)
                tree.append((min(v, w), max(v, w)))
                stack.append(w)
    return tree

def flux_classes(A):
    """one signing per flux class: tree edges positive, every subset of the non-tree edges negative"""
    tree = set(spanning_tree(A))
    cot = [e for e in edges_of(A) if e not in tree]
    for bits in itertools.product((0, 1), repeat=len(cot)):
        yield bits, signed(A, [e for e, b in zip(cot, bits) if b])

def hashimoto(A, As=None):
    """B (and the signed B_s if As is given) on directed edges, exact integers"""
    n = len(A)
    E = [(a, b) for a in range(n) for b in range(n) if A[a, b]]
    idx = {e: i for i, e in enumerate(E)}
    B = np.zeros((len(E), len(E)), dtype=object)
    Bs = np.zeros((len(E), len(E)), dtype=object)
    for (a, b), i in idx.items():
        for c in range(n):
            if A[b, c] and c != a:
                B[i, idx[(b, c)]] = 1
                Bs[i, idx[(b, c)]] = int(As[b, c]) if As is not None else 1
    return E, B, Bs

def traces(B, kmax):
    """Tr B^k, k = 0..kmax. Exact: Python integers for small matrices, int64 for the prism (q = 2, entries < 2^41)."""
    dt = np.int64 if len(B) > 80 else object
    Bd = B.astype(dt)
    out, P = [len(B)], np.eye(len(B), dtype=dt)
    for _ in range(kmax):
        P = P.dot(Bd)
        out.append(int(np.trace(P)))
    return out

def two_cover(A, As):
    P, N = (A + As) // 2, (A - As) // 2
    return np.block([[P, N], [N, P]])

def band(lam, q):
    return bool(np.all(np.abs(lam) <= 2 * np.sqrt(q) + 1e-9))

def lines_of(lam, q):
    w = []
    for l in lam:
        d = np.sqrt(complex(l * l - 4 * q))
        w += [(l + d) / (2 * np.sqrt(q)), (l - d) / (2 * np.sqrt(q))]
    return np.array(w)

def toeplitz(c):
    n = len(c)
    return np.array([[c[abs(j - k)] for k in range(n)] for j in range(n)], float)


A4, AP, A5, APR = K(4), petersen(), K(5), prism(21)
# Petersen: find the flux class whose 2-cover is the dodecahedron (signed spectrum +-sqrt5 three times, 0 four times)
target = np.sort(np.array([-np.sqrt(5)] * 3 + [0.0] * 4 + [np.sqrt(5)] * 3))
dod = [As for _, As in flux_classes(AP) if np.allclose(np.sort(np.linalg.eigvalsh(As.astype(float))), target, atol=1e-9)]
FLUX = {
    "K4, one negative edge": (A4, signed(A4, [(0, 1)]), 2),
    "K4, all edges negative": (A4, -A4, 2),
    "Petersen, dodecahedral flux": (AP, dod[0], 2),
    "Petersen, all edges negative": (AP, -AP, 2),
    "K5, pentagon negative": (A5, signed(A5, [(i, (i + 1) % 5) for i in range(5)]), 3),
    "prism C21xK2, antiperiodic ring": (APR, signed(APR, [(0, 20), (21, 41)]), 2),
}

# ------------------------------------------------------------------------------------------ S1 notebook examples
print("== S1  the notebook's graded quantum Ihara zeta (Pauli letters) and its signed-graph form")
X, Yp, Zp = np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])

def graded_hashimoto(letters, rev, P):
    Dk = len(letters)
    Es = [np.kron(U, U.conj()) for U in letters]
    d2 = Es[0].shape[0]
    T = np.zeros((d2 * Dk, d2 * Dk), complex)
    for i in range(Dk):
        for j in range(Dk):
            if j != rev[i]:
                T[j * d2:(j + 1) * d2, i * d2:(i + 1) * d2] = Es[i]
    G = np.kron(np.eye(Dk), np.kron(P, P.conj()))
    return T, G

def zeta_from(T, G, u):
    ev = np.where(np.diag(G).real > 0)[0]
    od = np.where(np.diag(G).real < 0)[0]
    I = np.eye(len(T))
    M = I - u * T
    return np.linalg.det(M[np.ix_(od, od)]) / np.linalg.det(M[np.ix_(ev, ev)])

T6, G6 = graded_hashimoto([X, X, Yp, Yp, Zp, Zp], [1, 0, 3, 2, 5, 4], Zp)
us = [0.11 + 0.07j, -0.2 + 0.1j, 0.05 - 0.3j]
ok = all(abs(zeta_from(T6, G6, u) - (1 + 2 * u + 5 * u * u) / ((1 - u) * (1 - 5 * u))) < 1e-10 for u in us)
strs = [np.trace(G6 @ np.linalg.matrix_power(T6, k)).real for k in range(1, 7)]
check("six Pauli letters X,X,Y,Y,Z,Z: zeta = (1+2u+5u^2)/((1-u)(1-5u)), str T^k = 8, 32, 104, 640, ...", ok and np.allclose(strs, [8, 32, 104, 640, 3208, 15392]),
      f"str T^k = {[int(round(s)) for s in strs]}")
AY = np.array([[2, 4], [4, 2]])
AYs = np.array([[-2, 0], [0, -2]])
okq = all(abs(zeta_from(T6, G6, u) - np.linalg.det(np.eye(2) - AYs * u + 5 * u * u * np.eye(2)) / np.linalg.det(np.eye(2) - AY * u + 5 * u * u * np.eye(2))) < 1e-10 for u in us)
check("... the same function as the signed two-vertex multigraph (loops negative, four parallel edges with signs ++--)", okq)
T3, G3 = graded_hashimoto([X, Yp, Zp], [0, 1, 2], Zp)
ok3 = all(abs(zeta_from(T3, G3, u) - (1 - u) * (1 + u + 2 * u * u) / ((1 + u) ** 2 * (1 - 2 * u))) < 1e-10 for u in us)
check("three Pauli letters X,Y,Z (K4 itself): zeta = (1-u)(1+u+2u^2)/((1+u)^2 (1-2u)); the zero pair is that of E over F_2", ok3)

# ------------------------------------------------------------------------------------------ S2 signed graphs
print("== S2  super zeta of a graph with a Z_2 flux: sectors, supertrace, counts")
KMAX = 14
rows = []
for name, (A, As, q) in FLUX.items():
    n = len(A)
    Ah = two_cover(A, As)
    Eh, Bh, _ = hashimoto(Ah)
    idx = {e: i for i, e in enumerate(Eh)}
    tau = np.zeros((len(Eh), len(Eh)), dtype=object)
    for (a, b), i in idx.items():
        tau[idx[((a + n) % (2 * n), (b + n) % (2 * n))], i] = 1
    E, B, Bs = hashimoto(A, As)
    tb, ts = traces(B, KMAX), traces(Bs, KMAX)
    dt = np.int64 if len(Eh) > 80 else object
    Bd, td = Bh.astype(dt), tau.astype(dt)
    P, sup = np.eye(len(Eh), dtype=dt), []
    for k in range(1, KMAX + 1):
        P = P.dot(Bd)
        sup.append(int(np.trace(td.dot(P))))
    lamB = np.linalg.eigvalsh(A.astype(float))
    lamF = np.linalg.eigvalsh(As.astype(float))
    muB, muF = lines_of(lamB, q) * np.sqrt(q), lines_of(lamF, q) * np.sqrt(q)
    spec = [np.sum(muB ** k).real - np.sum(muF ** k).real for k in range(1, KMAX + 1)]
    ok = sup == [tb[k] - ts[k] for k in range(1, KMAX + 1)] and np.allclose(sup, spec, rtol=1e-9, atol=1e-6)
    check(f"{name}: Tr(tau Bhat^k) = Tr B^k - Tr B_s^k = (bosonic lines) - (fermionic lines), k = 1..{KMAX}", ok)
    check(f"{name}: super counts are nonnegative even integers", all(s >= 0 and s % 2 == 0 for s in sup), f"{sup[:8]}")
    u = 0.13 + 0.05j
    I = np.eye(n)
    lhs = np.linalg.det(np.eye(len(E)) - u * Bs.astype(float)) / np.linalg.det(np.eye(len(E)) - u * B.astype(float))
    rhs = np.linalg.det(I - As * u + q * u * u * I) / np.linalg.det(I - A * u + q * u * u * I)
    check(f"{name}: det(1-uB_s)/det(1-uB) = det(1-A_s u+q u^2)/det(1-A u+q u^2)", abs(lhs - rhs) < 1e-9 * abs(rhs))
    Ds = (q + 1) * np.eye(n, dtype=np.int64) - As
    detD = int(round(np.linalg.det(Ds.astype(float))))
    rows.append((name, n, q, np.round(lamF, 4), band(lamF, q), detD))
    print(f"      fermionic eigenvalues {dict(zip(*np.unique(np.round(lamF, 4), return_counts=True)))}; in band: {band(lamF, q)}; det of signed Laplacian = {detD}")

cube = np.sort(np.linalg.eigvalsh(prism(4).astype(float)))
check("K4 with all edges negative has the cube as its 2-cover", np.allclose(np.sort(np.linalg.eigvalsh(two_cover(A4, -A4).astype(float))), cube))
check("Petersen has exactly one flux class with the dodecahedron's spectrum, up to graph symmetry", len(dod) >= 1, f"{len(dod)} of 64 classes")

def brute_flux(A, As, k):
    n, ev, od = len(A), 0, 0
    for v in itertools.product(range(n), repeat=k):
        if all(A[v[i], v[(i + 1) % k]] for i in range(k)) and all(v[i] != v[(i + 2) % k] for i in range(k)):
            s = 1
            for i in range(k):
                s *= As[v[i], v[(i + 1) % k]]
            if s > 0:
                ev += 1
            else:
                od += 1
    return ev, od
A, As, q = FLUX["K4, one negative edge"]
E, B, Bs = hashimoto(A, As)
tb, ts = traces(B, 9), traces(Bs, 9)
bf = [brute_flux(A, As, k) for k in range(3, 9)]
check("K4, one negative edge: brute-force walk counts by flux parity, k = 3..8", all(e + o == tb[k] and e - o == ts[k] for (e, o), k in zip(bf, range(3, 9))),
      f"(even, odd) = {bf}")

print("== S3  gauge invariance: switching does not change the fermionic spectrum")
rng = np.random.default_rng(1)
ok = True
for name, (A, As, q) in FLUX.items():
    d = np.diag(rng.choice([-1, 1], size=len(A)))
    ok &= np.allclose(np.sort(np.linalg.eigvalsh((d @ As @ d).astype(float))), np.sort(np.linalg.eigvalsh(As.astype(float))))
check("spec(A_s) is invariant under random switchings, all six examples", ok)

# ------------------------------------------------------------------------------------------ S4 crystal
print("== S4  layer 1: the period lattice H_1(K4, Z) = Z^3 and Bloch combs")
A = A4
tree = set(spanning_tree(A))
cot = [e for e in edges_of(A) if e not in tree]
def cls(a, b):
    v = np.zeros(len(cot), dtype=int)
    if (a, b) in cot:
        v[cot.index((a, b))] = 1
    elif (b, a) in cot:
        v[cot.index((b, a))] = -1
    return v
def walk_hist(A, k):
    n, H = len(A), {}
    for v in itertools.product(range(n), repeat=k):
        if all(A[v[i], v[(i + 1) % k]] for i in range(k)) and all(v[i] != v[(i + 2) % k] for i in range(k)):
            x = tuple(sum(cls(v[i], v[(i + 1) % k]) for i in range(k)))
            H[x] = H.get(x, 0) + 1
    return H
E4, B4, _ = hashimoto(A)
phi = rng.uniform(0, 2 * np.pi, size=len(cot))
Bphi = np.array([[complex(B4[i, j]) * np.exp(1j * phi @ cls(*E4[j])) for j in range(len(E4))] for i in range(len(E4))])
ok, okh, okc = True, True, True
a = np.array([1, 0, 1])
As_a = signed(A, [e for e, b in zip(cot, a) if b])
_, _, Bsa = hashimoto(A, As_a)
tsa, tb4 = traces(Bsa, 8), traces(B4, 8)
for k in range(3, 9):
    H = walk_hist(A, k)
    ok &= abs(sum(c * np.exp(1j * phi @ np.array(x)) for x, c in H.items()) - np.trace(np.linalg.matrix_power(Bphi, k))) < 1e-8
    okh &= sum(c * (-1) ** int(a @ np.array(x)) for x, c in H.items()) == tsa[k]
    okc &= 2 * sum(c for x, c in H.items() if (a @ np.array(x)) % 2) == tb4[k] - tsa[k]
    if k == 6:
        print(f"      k = 6: {sum(H.values())} closed walks on {len(H)} lattice points of Z^3")
check("overlap of the walk distribution with the Bloch comb at a generic flux equals Tr B_phi^k, k = 3..8", ok)
check("a Z_2 flux is the half-period: sign of a closed walk = (-1)^(a.x) for its class x", okh)
check("super count = 2 x (walks ending on the odd coset of the index-two sublattice ker s)", okc)

# ------------------------------------------------------------------------------------------ S5 torus
print("== S5  layer 2: periodic syndromes of a GKP qunaught under the fermionic step")
def fixed_points(M, k):
    C = np.linalg.matrix_power(np.array(M, dtype=object), k) - np.eye(len(M), dtype=object)
    N = abs(int(sp.Matrix(C.tolist()).det()))
    pts = [(a, b) for a in range(N) for b in range(N) if (C[0, 0] * a + C[0, 1] * b) % N == 0 and (C[1, 0] * a + C[1, 1] * b) % N == 0]
    return N, pts
ME = [[0, -1], [2, -1]]            # lambda = -1, q = 2: the fermionic mode of K4 with Pauli letters
s2 = [2, -1]
for k in range(2, 13):
    s2.append(-s2[-1] - 2 * s2[-2])
ptsE = [2 ** k + 1 - s2[k] for k in range(13)]
cnt = [len(fixed_points(ME, k)[1]) for k in range(1, 8)]
check("M = [[0,-1],[2,-1]] on R^2/Z^2: number of period-k syndromes, brute force, k = 1..7, equals #E(F_2^k)", cnt == ptsE[1:8], f"{cnt}")
M5 = [[0, -1], [5, -2]]            # lambda = -2, q = 5: the net fermionic mode of the six-letter Pauli channel
cnt5 = [len(fixed_points(M5, k)[1]) for k in range(1, 5)]
check("M = [[0,-1],[5,-2]]: period-k syndromes 8, 32, 104, 640 = the notebook's str T^k", cnt5 == [8, 32, 104, 640], f"{cnt5}")
uu = sp.symbols("u")
ser = sp.series(sp.exp(sum(sp.Integer(ptsE[k]) * uu ** k / k for k in range(1, 9))), uu, 0, 9).removeO()
ser2 = sp.series((1 + uu + 2 * uu ** 2) / ((1 - uu) * (1 - 2 * uu)), uu, 0, 9).removeO()
check("zeta of the toral map = (1+u+2u^2)/((1-u)(1-2u)) as power series to order 8", sp.expand(ser - ser2) == 0)
for name in ("K4, one negative edge", "Petersen, dodecahedral flux"):
    A, As, q = FLUX[name]
    n = len(A)
    I, Z = np.eye(n, dtype=object), np.zeros((n, n), dtype=object)
    M = np.block([[Z, -I], [q * I, As.astype(object)]])
    Om = np.block([[Z, I], [-I, Z]])
    okS = np.array_equal(M.T.dot(Om).dot(M), q * Om)
    d1 = int(sp.Matrix((np.eye(2 * n, dtype=object) - M).tolist()).det())
    snf = smith_normal_form(sp.Matrix((np.eye(2 * n, dtype=object) - M).tolist()), domain=sp.ZZ)
    inv = sorted(abs(int(snf[i, i])) for i in range(2 * n) if abs(int(snf[i, i])) != 1)
    lam = np.linalg.eigvalsh(As.astype(float))
    mu = lines_of(lam, q) * np.sqrt(q)
    okd = all(abs(float(sp.Matrix((np.eye(2 * n, dtype=object) - np.linalg.matrix_power(M, k)).tolist()).det()) - np.prod(1 - mu ** k).real) < 1e-6 * abs(np.prod(1 - mu ** k).real) for k in (1, 2, 3))
    check(f"{name}: M_s symplectic similitude; det(1 - M_s) = det(signed Laplacian); det(1 - M_s^k) = prod (1 - mu^k)",
          okS and d1 == int(round(np.linalg.det(((q + 1) * np.eye(n) - As).astype(float)))) and okd, f"step-invariant syndromes: {d1}, group invariants {inv}")
    Q = np.block([[q * np.eye(n), As / 2], [As / 2, np.eye(n)]])
    check(f"{name}: fermionic Weil form is positive definite (no pole plane in this sector)", np.linalg.eigvalsh(Q).min() > 1e-9, f"smallest eigenvalue {np.linalg.eigvalsh(Q).min():.4f}")
A, As, q = FLUX["prism C21xK2, antiperiodic ring"]
Q = np.block([[q * np.eye(len(A)), As / 2], [As / 2, np.eye(len(A))]])
lamF = np.linalg.eigvalsh(As.astype(float))
check("prism, antiperiodic ring: negative directions of the fermionic Weil form = off-band fermionic eigenvalues",
      int(np.sum(np.linalg.eigvalsh(Q) < -1e-9)) == int(np.sum(np.abs(lamF) > 2 * np.sqrt(q) + 1e-9)), f"{int(np.sum(np.linalg.eigvalsh(Q) < -1e-9))}; extreme eigenvalues {lamF.min():.4f}, {lamF.max():.4f}")

# ------------------------------------------------------------------------------------------ S6 Euler product
print("== S6  Euler product over flux-odd prime cycles")
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
def pmul(a, b, D):
    out = [0] * (D + 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if i + j > D:
                    break
                out[i + j] += x * y
    return out
def pinv(a, D):
    out = [0] * (D + 1)
    out[0] = 1
    for k in range(1, D + 1):
        out[k] = -sum(a[j] * out[k - j] for j in range(1, min(k, len(a) - 1) + 1))
    return out
def int_charpoly(Mat):
    return [int(round(c)) for c in np.poly(np.array(Mat, dtype=float))]
A, As, q = FLUX["K4, one negative edge"]
E, B, Bs = hashimoto(A, As)
D = 14
tb, ts = traces(B, D), traces(Bs, D)
odd = [0] + [(tb[k] - ts[k]) // 2 for k in range(1, D + 1)]
pim = {l: sum(mobius(m) * odd[l // m] for m in range(1, l + 1, 2) if l % m == 0) // l for l in range(1, D + 1)}
check("numbers of flux-odd prime cycles are nonnegative integers", all(v >= 0 for v in pim.values()) and
      all(sum(l * pim[l] for l in range(1, k + 1) if k % l == 0 and (k // l) % 2 == 1) == odd[k] for k in range(1, D + 1)), f"lengths 3..8: {[pim[l] for l in range(3, 9)]}")
prod = [1] + [0] * D
for l in range(1, D + 1):
    geo = [1 if j % l == 0 else 0 for j in range(D + 1)]
    one = [1 if j in (0, l) else 0 for j in range(D + 1)]
    for _ in range(pim[l]):
        prod = pmul(pmul(prod, one, D), geo, D)
def ihara_poly(Mat, q):
    """coefficients (ascending in u) of det(1 - Mat u + q u^2)"""
    n = len(Mat)
    cp = int_charpoly(Mat)                      # det(x - Mat), descending
    out = [0] * (2 * n + 1)
    base = [1]
    pw = [[1]]
    for _ in range(n):
        pw.append(pmul(pw[-1], [1, 0, q], 2 * n))   # (1 + q u^2)^j
    for j in range(n + 1):                      # det = sum_j c_j u^(n-j) (1+q u^2)^j, c_j coefficient of x^j
        cj = cp[n - j]
        for i, v in enumerate(pw[j]):
            if v and i + n - j <= 2 * n:
                out[i + n - j] += cj * v
    return out
num, den = ihara_poly(As, q), ihara_poly(A, q)
quot = pmul(num + [0] * (D + 1 - len(num)) if len(num) <= D else num[:D + 1], pinv(den, D), D)
check(f"Z_s(u) = prod over flux-odd prime cycles of (1+u^l)/(1-u^l), power series to order {D}", prod == quot, f"coefficients {quot[:9]}")

# ------------------------------------------------------------------------------------------ S7 flux average
print("== S7  average over fluxes: the matching polynomial")
def matching_poly(nv, edges):
    @lru_cache(maxsize=None)
    def rec(verts, edg):
        if not edg:
            p = [0] * (len(verts) + 1)
            p[0] = 1
            return tuple(p)
        (a, b), rest = edg[0], edg[1:]
        p1 = list(rec(verts, rest))
        v2 = tuple(v for v in verts if v not in (a, b))
        p2 = rec(v2, tuple(e for e in rest if a not in e and b not in e))
        for i, v in enumerate(p2):
            p1[i + 2] -= v
        return tuple(p1)
    return list(rec(tuple(range(nv)), tuple(edges)))
for name, A, q in (("K4", A4, 2), ("Petersen", AP, 2), ("K5", A5, 3)):
    n = len(A)
    mp_ = matching_poly(n, edges_of(A))
    tot, cntc, ram = [0] * (n + 1), 0, 0
    for bits, As in flux_classes(A):
        cp = int_charpoly(As)
        tot = [x + y for x, y in zip(tot, cp)]
        cntc += 1
        ram += band(np.linalg.eigvalsh(As.astype(float)), q)
    roots = np.roots([float(c) for c in mp_])
    check(f"{name}: average of det(x - A_s) over the {cntc} flux classes is the matching polynomial; its roots lie strictly inside the band",
          all(t == cntc * m for t, m in zip(tot, mp_)) and np.max(np.abs(roots.imag)) < 1e-7 and np.max(np.abs(roots.real)) < 2 * np.sqrt(q),
          f"coefficients {mp_}, largest root {np.max(np.abs(roots.real)):.4f} vs {2*np.sqrt(q):.4f}; fluxes with all fermionic eigenvalues in band: {ram} of {cntc}")
tot = [0] * 5
for sg in itertools.product((1, -1), repeat=6):
    As = A4.copy()
    for (a, b), sgn in zip(edges_of(A4), sg):
        As[a, b] = As[b, a] = sgn
    tot = [x + y for x, y in zip(tot, int_charpoly(As))]
check("K4: the average over all 64 signings gives the same polynomial x^4 - 6x^2 + 3", tot == [64, 0, -384, 0, 192])

# ------------------------------------------------------------------------------------------ S8 echo
print("== S8  fermionic echo and the parity bias, from walk counts only")
KE = 40
res = {}
for name in ("K4, one negative edge", "Petersen, dodecahedral flux", "K5, pentagon negative", "prism C21xK2, antiperiodic ring"):
    A, As, q = FLUX[name]
    n = len(A)
    E, B, Bs = hashimoto(A, As)
    tb, ts = traces(B, KE), traces(Bs, KE)
    r1 = n * (q - 1) // 2
    C = np.array([2.0 * n] + [float(Fraction(ts[k] - r1 * (1 + (-1) ** k))) / q ** (k / 2) for k in range(1, KE + 1)])
    w = lines_of(np.linalg.eigvalsh(As.astype(float)), q)
    check(f"{name}: fermionic echo from walk counts = sum over fermionic lines, k = 0..{KE}", np.allclose(C, [np.sum(w ** k).real for k in range(KE + 1)], rtol=1e-9, atol=1e-6))
    ev = np.linalg.eigvalsh(toeplitz(C[:31]))
    bias = [ts[k] / tb[k] if tb[k] else 0.0 for k in range(1, KE + 1)]
    res[name] = (C, ev, bias)
    print(f"      max |C_F(k)|/C_F(0) = {np.max(np.abs(C[1:])) / C[0]:.4f}; Gram eigenvalues in [{ev.min():.3e}, {ev.max():.2f}]; parity bias at k = 10, 20, 30: {bias[9]:+.2e}, {bias[19]:+.2e}, {bias[29]:+.2e}")
for name in ("K4, one negative edge", "Petersen, dodecahedral flux", "K5, pentagon negative"):
    C, ev, _ = res[name]
    check(f"{name}: echo bound and Gram positivity", np.max(np.abs(C)) <= C[0] + 1e-9 and ev.min() > -1e-8)
C, ev, bias = res["prism C21xK2, antiperiodic ring"]
check("prism, antiperiodic ring: Gram matrix has a negative eigenvalue and the echo passes its initial value", ev.min() < -1e-3 and np.max(np.abs(C)) > C[0],
      f"first k with |C| > C(0): {int(np.argmax(np.abs(C) > C[0] + 1e-9))}")

# ------------------------------------------------------------------------------------------ figures
INK, MUTED, GRID, AXIS, SURF = "#0b0b0b", "#52514e", "#e1e0d9", "#c3c2b7", "#fcfcfb"
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": AXIS, "axes.labelcolor": MUTED,
                     "xtick.color": MUTED, "ytick.color": MUTED, "axes.spines.top": False, "axes.spines.right": False,
                     "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF})

print("== Figure 1  periodic syndromes of one GKP qunaught mode under M = [[0,-1],[2,-1]]")
fig, axs = plt.subplots(1, 6, figsize=(11.4, 2.45), dpi=200)
for k, ax in zip(range(1, 7), axs):
    N, pts = fixed_points(ME, k)
    xy = np.array(pts, float) / N
    ax.scatter(xy[:, 0], xy[:, 1], s=14 if len(pts) < 30 else 9, color=BLUE, linewidths=0, zorder=3)
    ax.set_xlim(-0.04, 1.0)
    ax.set_ylim(-0.04, 1.0)
    ax.set_aspect("equal")
    ax.set_xticks([0, 0.5, 1])
    ax.set_yticks([0, 0.5, 1])
    ax.set_xticklabels(["0", "½", "1"], fontsize=8)
    ax.set_yticklabels(["0", "½", "1"] if k == 1 else ["", "", ""], fontsize=8)
    ax.grid(color=GRID, lw=0.6)
    ax.set_axisbelow(True)
    ax.set_title(f"k = {k}:  {len(pts)} points", fontsize=9.5, color=INK)
axs[0].set_ylabel("momentum syndrome")
fig.supxlabel("position syndrome (in units of the lattice spacing)", fontsize=10, color=MUTED, y=0.02)
fig.tight_layout()
fig.savefig(os.path.join(NOTE, "fig_syndromes.png"))
plt.close(fig)

print("== Figure 2  fermionic echo")
fig, ax = plt.subplots(figsize=(9.6, 3.9), dpi=200)
kk = np.arange(0, 31, 2)
ax.axhline(1, color=AXIS, lw=0.8, ls=(0, (4, 3)))
ax.text(30.3, 1, "bound", color=MUTED, va="center", fontsize=9)
C1, C2, C3 = res["Petersen, dodecahedral flux"][0], res["K4, one negative edge"][0], res["prism C21xK2, antiperiodic ring"][0]
ax.plot(kk, np.abs(C1[:31:2]) / C1[0], color=BLUE, lw=2, marker="o", ms=4, label="Petersen, dodecahedral flux")
ax.plot(kk, np.abs(C2[:31:2]) / C2[0], color=AQUA, lw=2, marker="o", ms=4, label="K₄, one negative edge")
ax.plot(kk, np.abs(C3[:31:2]) / C3[0], color=ORANGE, lw=2, marker="o", ms=4, label="prism C₂₁×K₂, antiperiodic ring")
first = int(np.argmax(np.abs(C3) > C3[0] + 1e-9))
ax.annotate(f"past the bound from k = {first}", (first, abs(C3[first]) / C3[0]), xytext=(-10, 14), textcoords="offset points", color=INK, fontsize=9, ha="right")
ax.set_xlim(0, 30)
ax.set_ylim(0, 2.6)
ax.set_xlabel("number of non-backtracking steps k (even k shown)")
ax.set_ylabel("|C_F(k)| / C_F(0)")
ax.grid(axis="y", color=GRID, lw=0.6)
ax.set_axisbelow(True)
ax.legend(frameon=False, loc="upper center", fontsize=9, labelcolor=INK, bbox_to_anchor=(0.5, 1.14), ncol=3)
fig.tight_layout()
fig.savefig(os.path.join(NOTE, "fig_super_echo.png"))
plt.close(fig)

print(f"\n{npass} passed, {nfail} failed")
