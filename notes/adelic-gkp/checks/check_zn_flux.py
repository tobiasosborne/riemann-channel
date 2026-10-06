#!/usr/bin/env python3
"""Checks for 'A Z_N flux on a graph: the finite shadow of a Dirichlet family' (zn-flux.md, lane D).

Conventions. Y a connected (q+1)-regular graph, n vertices, edge set E (pairs u<v), g = |E|-|V|+1.
A spanning tree T is fixed; a Z_N flux class is a vector a in (Z/N)^g on the cotree edges (oriented u->v, u<v),
zero on T; these are the N^g classes of H^1(Y, Z/N). zeta = exp(2 pi i/N).
  A_a[u,v] = zeta^{a_e} on a cotree edge e=(u,v), A_a[v,u] = zeta^{-a_e}; 1 on tree edges.  Hermitian.
  M_a = [[0,-1],[q,A_a]],  V_a = q M_a^{-1} = [[A_a,1],[-q,0]],  Omega = [[0,1],[-1,0]] (n x n blocks).
Restriction of scalars: Z[zeta] = Z^d (d = phi(N)) in the power basis; multiplication by zeta^k is C^k,
C the companion matrix of the cyclotomic polynomial. T_ij = Tr(zeta^(j-i)) is the Gram matrix of
(a,b) -> Tr(conj(a) b). Omega_Z = Omega (x) T is the matrix of Tr(x^dagger Omega y).
Galois: sigma_b (b in (Z/N)^*) sends the flux a to b*a.
"Ramanujan" = every eigenvalue of A_a in the OPEN band (-2 sqrt q, 2 sqrt q).
"Galois-Ramanujan" = A_{b a} Ramanujan for every b in (Z/N)^*.
"""
import itertools
from fractions import Fraction
import numpy as np
import scipy.linalg as sla
import sympy as sp
import mpmath as mp
import flint

npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


# ------------------------------------------------------------------------------------------ graphs and fluxes
def graph(name):
    if name == "K4":
        return 4, 2, [(a, b) for a in range(4) for b in range(a + 1, 4)]
    if name == "cube":
        return 8, 2, sorted({tuple(sorted((a, a ^ (1 << i)))) for a in range(8) for i in range(3)})
    if name == "Petersen":
        e = [(i, (i + 1) % 5) for i in range(5)] + [(i, i + 5) for i in range(5)] + [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
        return 10, 2, sorted(tuple(sorted(x)) for x in e)
    raise ValueError(name)


def tree_cotree(n, E):
    adj = {v: [] for v in range(n)}
    for a, b in E:
        adj[a].append(b)
        adj[b].append(a)
    seen, tree, stack = {0}, [], [0]
    while stack:
        v = stack.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                tree.append(tuple(sorted((v, w))))
                stack.append(w)
    return tree, [e for e in E if e not in tree]


class G:
    def __init__(self, name):
        self.name = name
        self.n, self.q, self.E = graph(name)
        self.tree, self.cot = tree_cotree(self.n, self.E)
        self.g = len(self.cot)
        assert self.g == len(self.E) - self.n + 1

    def A(self, a, N):
        z = np.exp(2j * np.pi / N)
        A = np.zeros((self.n, self.n), complex)
        for u, v in self.tree:
            A[u, v] = A[v, u] = 1
        for (u, v), k in zip(self.cot, a):
            A[u, v] = z ** k
            A[v, u] = z ** (-k)
        return A

    def dir_edges(self, a, N):
        """directed edges (u, v, exponent of zeta)"""
        ph = {e: 0 for e in self.tree}
        ph.update({e: k for e, k in zip(self.cot, a)})
        out = []
        for (u, v), k in ph.items():
            out += [(u, v, k % N), (v, u, (-k) % N)]
        return out

    def B(self, a, N):
        z = np.exp(2j * np.pi / N)
        D = self.dir_edges(a, N)
        B = np.zeros((len(D), len(D)), complex)
        for i, (u, v, k) in enumerate(D):
            for j, (u2, v2, k2) in enumerate(D):
                if u2 == v and v2 != u:
                    B[i, j] = z ** k
        return B

    def fluxes(self, N):
        return itertools.product(range(N), repeat=self.g)


def units(N):
    return [b for b in range(1, N) if np.gcd(b, N) == 1]


def galois(a, b, N):
    return tuple((b * k) % N for k in a)


# ------------------------------------------------------------------------------------------ restriction of scalars
def companion(N):
    x = sp.symbols("x")
    c = sp.Poly(sp.cyclotomic_poly(N, x), x).all_coeffs()[::-1]   # c_0..c_d, c_d = 1
    d = len(c) - 1
    C = np.zeros((d, d), dtype=object)
    for i in range(d - 1):
        C[i + 1, i] = 1
    for i in range(d):
        C[i, d - 1] = -int(c[i])
    return C.astype(np.int64), d


def zpow(C, k, N):
    d = len(C)
    return np.linalg.matrix_power(C, k % N) if k % N else np.eye(d, dtype=np.int64)


def restrict(Gr, a, N):
    """A_Z, M_Z, V_Z, Omega_Z, T for the flux a, all integer matrices"""
    C, d = companion(N)
    n, q = Gr.n, Gr.q
    AZ = np.zeros((n * d, n * d), dtype=np.int64)
    for u, v, k in Gr.dir_edges(a, N):
        AZ[u * d:(u + 1) * d, v * d:(v + 1) * d] += zpow(C, k, N)
    I = np.eye(n * d, dtype=np.int64)
    Z0 = np.zeros_like(I)
    MZ = np.block([[Z0, -I], [q * I, AZ]])
    VZ = np.block([[AZ, I], [-q * I, Z0]])
    T = np.array([[int(np.trace(zpow(C, j - i, N))) for j in range(d)] for i in range(d)], dtype=np.int64)
    Om = np.block([[np.zeros((n, n), np.int64), np.eye(n, dtype=np.int64)], [-np.eye(n, dtype=np.int64), np.zeros((n, n), np.int64)]])
    OmZ = np.kron(Om, T)
    return AZ, MZ, VZ, OmZ, T, d


def fmpz_charpoly(Mint):
    return [int(c) for c in flint.fmpz_mat(Mint.tolist()).charpoly().coeffs()]    # low degree first


def galois_product_poly(Gr, a, N, dps=60):
    """prod over b in (Z/N)^* of det(x^2 - A_{ba} x + q), high precision, low degree first, rounded"""
    mp.mp.dps = dps
    poly = [mp.mpf(1)]
    for b in units(N):
        A = Gr.A(galois(a, b, N), N)
        Am = mp.matrix([[mp.mpc(np.exp(2j * np.pi / N) ** 0) * 0 + 0 for _ in range(Gr.n)] for _ in range(Gr.n)])
        z = mp.exp(2j * mp.pi / N)
        for u, v, k in Gr.dir_edges(galois(a, b, N), N):
            Am[u, v] += z ** k
        ev = mp.eighe(Am, eigvals_only=True)
        for lam in ev:
            f = [mp.mpf(Gr.q), -lam, mp.mpf(1)]
            new = [mp.mpf(0)] * (len(poly) + 2)
            for i, c in enumerate(poly):
                for j, fj in enumerate(f):
                    new[i + j] += c * fj
            poly = new
    resid = max(abs(c - mp.nint(c)) for c in poly)
    return [int(mp.nint(c)) for c in poly], resid


def ramanujan(Gr, a, N, tol=1e-9):
    ev = np.linalg.eigvalsh(Gr.A(a, N))
    return np.max(np.abs(ev)) < 2 * np.sqrt(Gr.q) - tol, ev


def galois_ramanujan(Gr, a, N):
    return all(ramanujan(Gr, galois(a, b, N), N)[0] for b in units(N))


def matching_poly(Gr):
    n, E = Gr.n, Gr.E
    m = [0] * (n // 2 + 1)
    for r in range(n // 2 + 1):
        for S in itertools.combinations(E, r):
            vs = [v for e in S for v in e]
            if len(set(vs)) == 2 * r:
                m[r] += 1
    c = [0] * (n + 1)          # high degree first
    for r, mr in enumerate(m):
        c[2 * r] = (-1) ** r * mr
    return c


GRAPHS = {nm: G(nm) for nm in ["K4", "cube", "Petersen"]}

# ================================================================================ 1. Ihara-Bass for the twisted zeta
print("== 1. Ihara-Bass for Z_N fluxes (det(1-uB) = (1-u^2)^{|E|-|V|} det(1 - A u + q u^2))")
rng = np.random.default_rng(1)
for nm, Ns in [("K4", [3, 4, 5, 6]), ("cube", [3, 4, 6]), ("Petersen", [3, 4, 6])]:
    Gr = GRAPHS[nm]
    worst = 0.0
    for N in Ns:
        for _ in range(3):
            a = tuple(rng.integers(0, N, Gr.g))
            B, A = Gr.B(a, N), Gr.A(a, N)
            check_herm = np.allclose(A, A.conj().T)
            for u in [0.3, 0.17 + 0.41j, -0.55 + 0.1j]:
                lhs = np.linalg.det(np.eye(len(B)) - u * B)
                rhs = (1 - u * u) ** (len(Gr.E) - Gr.n) * np.linalg.det((1 + Gr.q * u * u) * np.eye(Gr.n) - A * u)
                worst = max(worst, abs(lhs - rhs) / max(1, abs(rhs)))
            assert check_herm
    check(f"I1 {nm}: Ihara-Bass for 3 random fluxes each, N in {Ns}, 3 values of u", worst < 1e-10, f"max rel. error {worst:.1e}")

# ================================================================================ 2. the lattice state over Z[zeta_N]
print("\n== 2. lattice state: L = Z[zeta_N]^{2n} restricted to Z")
for N in [3, 4, 5, 6]:
    C, d = companion(N)
    _, _, _, _, T, _ = restrict(GRAPHS["K4"], (0,) * 3, N)
    snf = [int(sp.Matrix(T).applyfunc(int).det())]
    from sympy.matrices.normalforms import smith_normal_form
    S = smith_normal_form(sp.Matrix(T.tolist()), domain=sp.ZZ)
    inv = [abs(int(S[i, i])) for i in range(d)]
    disc = int(sp.discriminant(sp.cyclotomic_poly(N, sp.Symbol("x"))))
    check(f"L0 N={N}: Gram of Tr(conj(a)b) on Z[zeta_N] has det |disc Q(zeta_N)| = {abs(disc)}; Smith invariants {inv}",
          abs(snf[0]) == abs(disc), f"T = {T.tolist()}")
# N = 4 with the twist delta = 1/2 is unimodular
_, _, _, _, T4, _ = restrict(GRAPHS["K4"], (0,) * 3, 4)
check("L0' N=4: (1/2) Tr(conj(a) b) = Re(conj(a) b) is integral and unimodular on Z[i]",
      np.all(T4 % 2 == 0) and round(abs(np.linalg.det(T4 / 2))) == 1)

examples = []   # (graph, N, flux) for detailed checks
for nm, N in [("K4", 3), ("K4", 4), ("K4", 5), ("K4", 6), ("cube", 3), ("cube", 4), ("cube", 6), ("Petersen", 3)]:
    Gr = GRAPHS[nm]
    rr = np.random.default_rng(7 + N)
    allf = list(Gr.fluxes(N))
    rr.shuffle(allf)
    good = [a for a in allf[:400] if galois_ramanujan(Gr, a, N)]
    bad = [a for a in allf[:400] if any(k % N for k in a) and not galois_ramanujan(Gr, a, N)]
    examples.append((nm, N, good[0], True))
    if bad:
        examples.append((nm, N, bad[0], False))

print("-- integrality, similitude, characteristic polynomial, Weil form, vacuum")
for nm, N, a, isgood in examples:
    Gr = GRAPHS[nm]
    q, n = Gr.q, Gr.n
    AZ, MZ, VZ, OmZ, T, d = restrict(Gr, a, N)
    I2 = np.eye(2 * n * d, dtype=np.int64)
    tag = f"{nm} N={N} flux {a} ({'Galois-Ramanujan' if isgood else 'not Galois-Ramanujan'})"
    ok1 = np.array_equal(MZ @ VZ, q * I2) and np.array_equal(VZ @ MZ, q * I2)
    ok2 = np.array_equal(MZ.T @ OmZ @ MZ, q * OmZ) and np.array_equal(OmZ.T, -OmZ) and np.all(np.diag(OmZ) == 0)
    cp = fmpz_charpoly(MZ)
    gp, resid = galois_product_poly(Gr, a, N)
    ok3 = cp == gp and resid < mp.mpf(10) ** -30
    # square: the flux and its conjugate have the same spectrum
    P = flint.fmpz_poly(cp)
    fac = P.factor()
    ok_sq = all(e % 2 == 0 for _, e in fac[1])
    W2 = OmZ @ (MZ - VZ)              # = 2 W_Z
    ok_sym = np.array_equal(W2, W2.T)
    wmin = np.linalg.eigvalsh(W2.astype(float) / 2).min()
    check(f"L1 {tag}: M_Z, V_Z integral with M_Z V_Z = q; M_Z^T Omega_Z M_Z = q Omega_Z, Omega_Z alternating integral", ok1 and ok2,
          f"rank {2 * n * d}")
    check(f"L2 {tag}: charpoly_Z(M_Z) = prod over Galois conjugates of det(x^2 - A x + q), exactly; it is a square", ok3 and ok_sq,
          f"degree {len(cp) - 1}, rounding residue {mp.nstr(resid, 3)}")
    check(f"L3 {tag}: Weil form (1/2) Omega_Z (M_Z - V_Z) symmetric; positive definite iff Galois-Ramanujan",
          ok_sym and ((wmin > 1e-9) == isgood), f"min eigenvalue {wmin:.4f}")
    if isgood:
        A2 = (AZ.astype(float) @ AZ.astype(float))
        F = np.real(sla.inv(sla.sqrtm(4 * q * np.eye(n * d) - A2)))
        J = (MZ - VZ).astype(float) @ np.kron(np.eye(2), F)
        Zeta = np.kron(np.eye(2 * n), companion(N)[0]).astype(float)
        G2 = OmZ.astype(float) @ J
        okJ = (np.allclose(J @ J, -np.eye(len(J)), atol=1e-9) and np.allclose(J @ MZ, MZ @ J, atol=1e-8)
               and np.allclose(J @ Zeta, Zeta @ J, atol=1e-9) and np.allclose(G2, G2.T, atol=1e-8)
               and np.linalg.eigvalsh((G2 + G2.T) / 2).min() > 1e-9)
        check(f"L4 {tag}: J = (M-V)(4q - A^2)^(-1/2): J^2 = -1, JM = MJ, J zeta = zeta J, Omega_Z(.,J.) symmetric positive", okJ)

print("-- the Weil form against Galois-Ramanujan on every flux class of K4 (N = 3,4,5,6) and the cube (N = 3)")
for nm, Ns in [("K4", [3, 4, 5, 6]), ("cube", [3])]:
    Gr = GRAPHS[nm]
    for N in Ns:
        agree = tot = 0
        for a in Gr.fluxes(N):
            AZ, MZ, VZ, OmZ, T, d = restrict(Gr, a, N)
            wmin = np.linalg.eigvalsh((OmZ @ (MZ - VZ)).astype(float) / 2).min()
            agree += (wmin > 1e-9) == galois_ramanujan(Gr, a, N)
            tot += 1
        check(f"L5 {nm} N={N}: Weil form positive definite <=> Galois-Ramanujan, on all {tot} flux classes", agree == tot)

print("-- locks: root-of-unity relations between distinct modes")


def lock_orders(Gr, a, N, maxord=120):
    lams = []
    for b in units(N):
        for lam in np.linalg.eigvalsh(Gr.A(galois(a, b, N), N)):
            if all(abs(lam - l) > 1e-7 for l in lams):
                lams.append(lam)
    q = Gr.q
    mus = [(l + 1j * np.sqrt(4 * q - l * l)) / 2 for l in lams]
    orders = set()
    for i in range(len(lams)):
        for j in range(i + 1, len(lams)):
            for r in [mus[j] / mus[i], mus[j] / np.conj(mus[i])]:
                th = np.angle(r) / (2 * np.pi)
                for m in range(1, maxord + 1):
                    if abs(m * th - round(m * th)) < 1e-9:
                        orders.add(m)
                        break
    return orders, len(lams)


lockrows = {}
for nm, Ns in [("K4", [3, 4, 5, 6]), ("cube", [3, 4, 6])]:
    Gr = GRAPHS[nm]
    for N in Ns:
        stats = {"fluxes": 0, "with order N": 0, "orders": {}}
        for a in Gr.fluxes(N):
            if not galois_ramanujan(Gr, a, N):
                continue
            o, _ = lock_orders(Gr, a, N)
            stats["fluxes"] += 1
            stats["with order N"] += (N in o)
            for m in o:
                stats["orders"][m] = stats["orders"].get(m, 0) + 1
        lockrows[(nm, N)] = stats
        print(f"     {nm} N={N}: {stats['fluxes']} Galois-Ramanujan classes; lock orders found (order: #classes) "
              f"{dict(sorted(stats['orders'].items()))}; classes with a lock of order N: {stats['with order N']}")
check("K1 a Z_N flux does not force a lock of order N: on K4 (not bipartite) some Galois-Ramanujan class has no lock of order N, for N = 3,4,5,6",
      all(lockrows[("K4", N)]["with order N"] < lockrows[("K4", N)]["fluxes"] for N in [3, 4, 5, 6]))
check("K2 on the cube (bipartite) every Galois-Ramanujan class has the half-turn lock (order 2)",
      all(lockrows[("cube", N)]["orders"].get(2, 0) == lockrows[("cube", N)]["fluxes"] for N in [3, 4, 6]))

# ================================================================================ 3. census and Deligne modules
print("\n== 3. census: Ramanujan, Galois-Ramanujan, ordinary (Deligne modules)")
census = {}
for nm, Ns in [("K4", [3, 4, 5, 6]), ("cube", [3, 4, 6]), ("Petersen", [3, 4, 6])]:
    Gr = GRAPHS[nm]
    q = Gr.q
    for N in Ns:
        d = len(units(N))
        ram = gram = ordin = bdry = 0
        for a in Gr.fluxes(N):
            r, ev = ramanujan(Gr, a, N)
            ram += r
            bdry += np.min(np.abs(np.abs(ev) - 2 * np.sqrt(q))) < 1e-7
            if all(ramanujan(Gr, galois(a, b, N), N)[0] for b in units(N)):
                gram += 1
                # ordinary <=> Norm(det A) prime to p (middle coefficient of charpoly = (-1)^{nd} Norm(det A) mod p)
                nrm = np.prod([np.linalg.det(Gr.A(galois(a, b, N), N)) for b in units(N)])
                ordin += (round(nrm.real) % q != 0)
        census[(nm, N)] = (N ** Gr.g, ram, gram, ordin, Gr.n * d, bdry)
        print(f"     {nm} N={N}: classes {N ** Gr.g}, Ramanujan {ram}, Galois-Ramanujan {gram}, of which ordinary {ordin}; "
              f"abelian variety dimension n*phi(N) = {Gr.n * d}; eigenvalue on the band edge in {bdry} classes")
# ordinariness formula against the exact charpoly
okord = True
for nm, N, a, isgood in examples:
    Gr = GRAPHS[nm]
    AZ, MZ, VZ, OmZ, T, d = restrict(Gr, a, N)
    cp = fmpz_charpoly(MZ)
    g_ = Gr.n * d
    mid = cp[g_]
    nrm = int(flint.fmpz_mat(AZ.tolist()).det())     # det of the restriction = Norm(det A)
    okord &= (mid - (-1) ** g_ * nrm) % Gr.q == 0
check("D1 middle coefficient of charpoly_Z(M_Z) = (-1)^{n phi(N)} Norm(det A) mod p, on all detailed examples", okord)
check("D2 every class has Ramanujan <=> Galois-Ramanujan when phi(N) = 2 (N = 3,4,6: the conjugate flux has the same spectrum)",
      all(census[(nm, N)][1] == census[(nm, N)][2] for (nm, N) in census if N in (3, 4, 6)))
check("D3 no class has an eigenvalue on the band edge +-2 sqrt q (so the open/closed band distinction does not arise here)",
      all(c[5] == 0 for c in census.values()))

par = {nm: round(np.linalg.det(GRAPHS[nm].A((0,) * GRAPHS[nm].g, 4)).real) % 2 for nm in ["K4", "cube", "Petersen"]}
check("D4 N=4, p=2: a Galois-Ramanujan class is ordinary iff det A (untwisted) is odd, for every class (zeta = i = 1 mod (1+i))",
      all(census[(nm, 4)][3] == (census[(nm, 4)][2] if par[nm] else 0) for nm in par),
      "det A: K4 -3, cube 9, Petersen 48; ordinary classes " + str({nm: census[(nm, 4)][3] for nm in par}))

# ================================================================================ 4. RH on average over the N-torsion
print("\n== 4. average of det(x - A_a) over the N-torsion of the Brillouin torus")
x = sp.Symbol("x")
for nm in ["K4", "cube"]:
    Gr = GRAPHS[nm]
    mu = matching_poly(Gr)
    for N in [3, 4, 6]:
        tot = [Fraction(0)] * (Gr.n + 1)
        cert = True
        for a in Gr.fluxes(N):
            c = np.round(np.real(np.poly(np.linalg.eigvalsh(Gr.A(a, N))))).astype(np.int64)   # high first; in Z[x] since phi(N) = 2
            AZ = restrict(Gr, a, N)[0]
            sq = flint.fmpz_poly([int(v) for v in c[::-1]]) ** 2
            cert &= (sq == flint.fmpz_mat(AZ.tolist()).charpoly())
            for i in range(Gr.n + 1):
                tot[i] += int(c[i])
        avg = [t / N ** Gr.g for t in tot]
        check(f"R1 {nm} N={N}: average of det(x - A) over all {N ** Gr.g} classes = matching polynomial, exactly",
              cert and avg == [Fraction(v) for v in mu], f"mu = {mu}; per-class det certified by det^2 = charpoly(A_Z)")
# N = 5 on K4, numerically
Gr = GRAPHS["K4"]
tot = np.zeros(5, complex)
for a in Gr.fluxes(5):
    tot += np.poly(np.linalg.eigvalsh(Gr.A(a, 5)))
err = np.max(np.abs(tot / 125 - np.array(matching_poly(Gr))))
check("R2 K4 N=5: average over 125 classes = matching polynomial (float)", err < 1e-9, f"max error {err:.1e}")
# N = 2 (Godsil-Gutman) for comparison
for nm in ["K4", "cube"]:
    Gr = GRAPHS[nm]
    tot = np.zeros(Gr.n + 1)
    for a in Gr.fluxes(2):
        tot += np.real(np.poly(np.linalg.eigvalsh(Gr.A(a, 2))))
    check(f"R3 {nm} N=2 (Godsil-Gutman): the same polynomial", np.max(np.abs(tot / 2 ** Gr.g - matching_poly(Gr))) < 1e-9)

# the reason: multi-affine Laurent polynomial in the cotree variables
Gr = GRAPHS["K4"]
zs = sp.symbols("z1:%d" % (Gr.g + 1))
ws = sp.symbols("w1:%d" % (Gr.g + 1))       # w_i stands for 1/z_i
Ms = sp.zeros(Gr.n, Gr.n)
for u, v in Gr.tree:
    Ms[u, v] = Ms[v, u] = 1
for (u, v), z, w in zip(Gr.cot, zs, ws):
    Ms[u, v], Ms[v, u] = z, w
D = sp.expand((x * sp.eye(Gr.n) - Ms).det(method="berkowitz"))
D = sp.expand(D.subs({w: 1 / z for z, w in zip(zs, ws)}))
Pz = sp.Poly(sp.expand(D * sp.prod(zs)), *zs, x)
expo_ok = all(all(e in (0, 1, 2) for e in mon[:Gr.g]) for mon in Pz.monoms())
const = sp.expand(sum(c * x ** mon[-1] for mon, c in zip(Pz.monoms(), Pz.coeffs()) if all(e == 1 for e in mon[:Gr.g])))
check("R4 K4: det(x - A_z) is a Laurent polynomial of degree <= 1 in each cotree variable z_e^{+-1}; constant term = matching polynomial",
      expo_ok and sp.expand(const - (x ** 4 - 6 * x ** 2 + 3)) == 0, f"{len(Pz.monoms())} monomials")

# U(1) Haar average by Gauss-Legendre quadrature (not a torsion grid)
for nm, nodes in [("K4", 12), ("cube", 12)]:
    Gr = GRAPHS[nm]
    t, w = np.polynomial.legendre.leggauss(nodes)
    th, wt = np.pi * (t + 1), w / 2            # nodes on [0, 2 pi), weights summing to 1
    acc = np.zeros(Gr.n + 1, complex)
    for idx in itertools.product(range(nodes), repeat=Gr.g):
        phis = th[list(idx)]
        A = np.zeros((Gr.n, Gr.n), complex)
        for u, v in Gr.tree:
            A[u, v] = A[v, u] = 1
        for (u, v), p in zip(Gr.cot, phis):
            A[u, v], A[v, u] = np.exp(1j * p), np.exp(-1j * p)
        acc += np.prod(wt[list(idx)]) * np.poly(np.linalg.eigvalsh(A))
    err = np.max(np.abs(acc - matching_poly(Gr)))
    check(f"R5 {nm}: U(1) Haar average of det(x - A_phi) (Gauss-Legendre, {nodes} nodes per angle) = matching polynomial", err < 1e-9,
          f"max error {err:.1e}")

# roots of the average: real, in the band (Heilmann-Lieb)
for nm in ["K4", "cube", "Petersen"]:
    Gr = GRAPHS[nm]
    r = np.roots(matching_poly(Gr))
    check(f"R6 {nm}: roots of the matching polynomial are real and inside (-2 sqrt q, 2 sqrt q)",
          np.max(np.abs(r.imag)) < 1e-9 and np.max(np.abs(r.real)) < 2 * np.sqrt(Gr.q),
          f"largest root {np.max(np.abs(r.real)):.4f} < {2 * np.sqrt(Gr.q):.4f}")

# the count-level average: orthogonality picks walks with homology class in N.H_1
print("-- count-level orthogonality (the Dirichlet n = 1 mod N analogue)")
Gr = GRAPHS["K4"]
N = 3
cotidx = {e: i for i, e in enumerate(Gr.cot)}
D0 = Gr.dir_edges((0,) * Gr.g, N)


def walk_class_counts(K):
    """closed non-backtracking walks of length K (as cyclic sequences with a start), split by class mod N"""
    good = 0
    total = 0
    for start in range(len(D0)):
        stack = [(start, [0] * Gr.g, 1)]
        while stack:
            cur, cls, L = stack.pop()
            u, v, _ = D0[cur]
            if L == K:
                if v == D0[start][0] and not (D0[start][1] == u):
                    total += 1
                    good += all(c % N == 0 for c in cls_add(cls, cur))
                continue
            for j, (u2, v2, _) in enumerate(D0):
                if u2 == v and v2 != u:
                    stack.append((j, cls_add(cls, cur), L + 1))
    return good, total


def cls_add(cls, j):
    u, v, _ = D0[j]
    e = tuple(sorted((u, v)))
    if e in cotidx:
        cls = list(cls)
        cls[cotidx[e]] += 1 if u < v else -1
    return cls


ok = True
rows = []
for K in range(3, 10):
    good, total = walk_class_counts(K)
    avg = sum(np.trace(np.linalg.matrix_power(Gr.B(a, N), K)) for a in Gr.fluxes(N)) / N ** Gr.g
    ok &= abs(avg - good) < 1e-6
    rows.append((K, total, good))
check("C1 K4 N=3: (1/N^g) sum over characters of Tr B_chi^k = #closed non-backtracking walks with class in N.H_1, k = 3..9",
      ok, "(k, all, class in 3H_1): " + str(rows))
# Artin factorisation: the H_1/N cover
n, E = Gr.n, Gr.E
idx = {}
for v in range(n):
    for h in itertools.product(range(N), repeat=Gr.g):
        idx[(v, h)] = len(idx)
AY = np.zeros((len(idx), len(idx)))
for (v, h), i in idx.items():
    for u2, v2, _ in D0:
        if u2 != v:
            continue
        e = tuple(sorted((u2, v2)))
        h2 = list(h)
        if e in cotidx:
            h2[cotidx[e]] = (h2[cotidx[e]] + (1 if u2 < v2 else -1)) % N
        AY[i, idx[(v2, tuple(h2))]] += 1
evY = np.sort(np.linalg.eigvalsh(AY))
evchi = np.sort(np.concatenate([np.linalg.eigvalsh(Gr.A(a, N)) for a in Gr.fluxes(N)]))
check("C2 K4 N=3: spectrum of the H_1/3H_1-cover (108 vertices) = union over all 27 characters of spec(A_chi) (Artin factorisation)",
      np.allclose(evY, evchi, atol=1e-9))
# det-level average is N-independent
u0 = [0.31, 0.2 + 0.37j]
vals = {}
for N_ in [2, 3, 4, 5, 6]:
    vals[N_] = [np.mean([np.linalg.det(np.eye(2 * len(E)) - u * Gr.B(a, N_)) for a in Gr.fluxes(N_)]) for u in u0]
target = [(1 - u * u) ** (len(E) - n) * u ** n * np.polyval(matching_poly(Gr), (1 + Gr.q * u * u) / u) for u in u0]
check("C3 K4: average of det(1 - u B_chi) over the N-torsion is the same for N = 2..6 and equals (1-u^2)^{|E|-|V|} u^n mu((1+qu^2)/u)",
      all(np.allclose(vals[N_], target, atol=1e-10) for N_ in vals))

print(f"\n{npass} of {npass + nfail} pass" + ("" if nfail == 0 else f"  ({nfail} FAIL)"))
