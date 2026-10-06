#!/usr/bin/env python3
"""Checks for 'The bridge in genus two: a cone, not a line' (notes/adelic-gkp/cone-bridge.md), lane E.

Conventions (lattice-tower.md section 1, curve-bridge.md section 1): L = Z^{2g}, Omega(x, y) = x^T Omega y, a step M with
M^T Omega M = q Omega, V = q M^{-1}.  Similitude forms: symmetric B with M^T B M = q B.  Weil form of a compatible
alternating form Om: W_Om = (1/2) Om (M - V).  Vacuum of Om: the complex structure J commuting with M with Om J > 0.
Rosati form (analytic.md Prop. 15): T(phi, psi) = Tr_{H^1}(phi(F) psi(V)), Gram T_ik = Tr(F^i V^k) in the basis 1, F, ...
Transport by a cyclic vector e: psi_e(phi) = phi(M) e, T_L = Psi^{-T} T Psi^{-1}.

Example 1: C : y^2 = x^5 + x^3 + x^2 - 2 over F_5 (shard 04w); L = O_K = Z[pi, 5/pi], basis (1, beta, pi, beta pi),
beta = pi + 5/pi, beta^2 = 3 beta + 3; canonical form Om_can(x, y) = Tr(x conj(y) / dd), dd = (pi - V) h'(beta),
h(y) = y^2 - 3y - 3; the Phi_+ form Om_+(x, y) = Tr(x conj(y) / (V - pi)).
Example 2: K_4 with one negative edge, q = 2, M = [[0, -I], [2I, A_s]], standard Omega; Howe's unit P (howe-positivity.md section 4).

Needs PARI/GP as the binary /usr/bin/gp (subprocess), sympy, numpy, mpmath.
Run:  python3 check_cone_bridge.py > output_cone_bridge.txt
"""
import itertools
import subprocess
import numpy as np
import sympy as sp
import mpmath as mp

mp.mp.dps = 40
npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


def gp(script):
    r = subprocess.run(["gp", "-q", "-f"], input=script, capture_output=True, text=True, timeout=600)
    if r.returncode != 0 or "***" in r.stderr + r.stdout:
        raise RuntimeError(r.stderr + r.stdout)
    return r.stdout


def omega(g):
    return sp.Matrix(sp.BlockMatrix([[sp.zeros(g), sp.eye(g)], [-sp.eye(g), sp.zeros(g)]]))


def Z(n):
    return sp.zeros(n)


def is_zero(X):
    return all(sp.simplify(v) == 0 for v in X)


def num(X):
    return mp.matrix([[mp.mpf(sp.N(v, 50)) for v in X.row(i)] for i in range(X.rows)])


def sim_space_dim(M, q):
    """dimension of the space of symmetric B with M^T B M = q B (exact)"""
    n = M.rows
    syms = sp.symbols(f"b0:{n * (n + 1) // 2}")
    B = sp.zeros(n)
    k = 0
    for i in range(n):
        for j in range(i, n):
            B[i, j] = B[j, i] = syms[k]
            k += 1
    eqs = list(M.T * B * M - q * B)
    A, _ = sp.linear_eq_to_matrix(eqs, syms)
    return len(syms) - A.rank()


def symplectic_eigs(G, Om):
    ev = np.linalg.eigvals(np.array(Om.tolist(), dtype=float) @ np.array(G.tolist(), dtype=float))
    return sorted(set(np.round(np.abs(ev.imag), 10)))


def signature(G):
    ev = np.linalg.eigvalsh(np.array(G.tolist(), dtype=float))
    return (int((ev > 1e-9).sum()), int((ev < -1e-9).sum()))


def vacuum(M, V, Om, projs, lams, q):
    """the invariant complex structure: on mode j, J = s_j (M - V)/sqrt(4q - lam_j^2), s_j = sign of Om(M - V) there"""
    n = M.rows
    J = mp.matrix(n, n)
    signs = []
    for P, lam in zip(projs, lams):
        Wj = num(P.T * Om * (M - V) * P)
        x = num(P) * mp.matrix([1] * n)
        if mp.norm(x) < 1e-20:
            x = num(P) * mp.matrix([i + 1 for i in range(n)])
        s = 1 if (x.T * Wj * x)[0] > 0 else -1
        signs.append(s)
        J += s * num((M - V) * P) / mp.sqrt(4 * q - mp.mpf(sp.N(lam, 50)) ** 2)
    return J, signs


def mnorm(X):
    return max(abs(v) for v in X)


def weights(B, G, projs, n):
    """per-mode weight t_j of a similitude form B relative to G (B = sum_j t_j G restricted to mode j)"""
    out = []
    e = mp.matrix([i * i + 1 for i in range(n)])
    for P in projs:
        x = num(P) * e
        out.append((x.T * B * x)[0] / (x.T * G * x)[0])
    return out


def block_diag_ok(B, projs):
    return all(mnorm(num(projs[a]).T * B * num(projs[b])) < 1e-25 for a in range(len(projs)) for b in range(len(projs)) if a != b)


# =============================================================================================================
print("== C. The curve y^2 = x^5 + x^3 + x^2 - 2 over F_5: L-polynomial, ordinariness, CM field")
out = gp("print(Vec(hyperellcharpoly(Mod(1,5)*(x^5+x^3+x^2-2))));")
chi_coeffs = [int(c) for c in out.strip().strip("[]").split(",")]
check("C1 PARI hyperellcharpoly: chi(x) = x^4 - 3x^3 + 7x^2 - 15x + 25, i.e. P(T) = 1 - 3T + 7T^2 - 15T^3 + 25T^4 (shard 04w)",
      chi_coeffs == [1, -3, 7, -15, 25], f"{chi_coeffs}")


def count_points():
    p = 5
    # F_5 and F_25 = F_5[t]/(t^2 - 2) (2 is a non-residue mod 5); elements (a, b) = a + b t
    def f1(x):
        return (x ** 5 + x ** 3 + x ** 2 - 2) % p
    N1 = 1 + sum(1 for x in range(p) for y in range(p) if (y * y - f1(x)) % p == 0)
    def mul(u, v):
        return ((u[0] * v[0] + 2 * u[1] * v[1]) % p, (u[0] * v[1] + u[1] * v[0]) % p)
    def pw(u, k):
        r = (1, 0)
        for _ in range(k):
            r = mul(r, u)
        return r
    F25 = [(a, b) for a in range(p) for b in range(p)]
    sq = {}
    for y in F25:
        s = mul(y, y)
        sq[s] = sq.get(s, 0) + 1
    N2 = 1
    for x in F25:
        v = [pw(x, 5), pw(x, 3), pw(x, 2)]
        fx = ((v[0][0] + v[1][0] + v[2][0] - 2) % p, (v[0][1] + v[1][1] + v[2][1]) % p)
        N2 += sq.get(fx, 0)
    return N1, N2


N1, N2 = count_points()
a1, a2 = 3, 7
check("C2 brute-force counts N_1 = 3, N_2 = 31 (one point at infinity) agree with a_1 = q + 1 - N_1, N_2 = q^2 + 1 - (a_1^2 - 2 a_2)",
      (N1, N2) == (3, 31) and N1 == 5 + 1 - a1 and N2 == 25 + 1 - (a1 ** 2 - 2 * a2), f"N1={N1}, N2={N2}")
x, y = sp.symbols("x y")
chi = sp.Poly(x ** 4 - 3 * x ** 3 + 7 * x ** 2 - 15 * x + 25, x)
h = sp.Poly(y ** 2 - 3 * y - 3, y)
check("C3 chi(x) = x^2 h(x + 5/x) with h(y) = y^2 - 3y - 3; ordinary (middle coefficient 7 prime to 5); roots of h real, distinct, inside (-2 sqrt5, 2 sqrt5)",
      sp.expand(x ** 2 * h.as_expr().subs(y, x + 5 / x)) == chi.as_expr() and 7 % 5 != 0
      and all(abs(float(r)) < 2 * 5 ** 0.5 for r in sp.Poly(h).nroots()), f"lambda = (3 +- sqrt 21)/2 = {[round(float(r), 6) for r in sp.Poly(h).nroots()]}")
out = gp("f=x^4-3*x^3+7*x^2-15*x+25; print(nfdisc(f)); b=bnfinit(f,1); print(b.no);")
d_K, h_K = [int(t) for t in out.split()]
check("C4 PARI: disc O_K = 48069 = 21^2 * 109 (04w), class number h_K = 4", d_K == 48069 and h_K == 4, f"disc {d_K}, h_K {h_K}")
check("C5 no symmetric integer 2x2 A has characteristic polynomial h: the graph convention [[0,-I],[qI,A]] cannot host this class "
      "((a-c)^2 + 4b^2 = disc h = 21 has no solution)",
      not any((a - c) ** 2 + 4 * b * b == 21 for a in range(-10, 11) for c in range(-10, 11) for b in range(0, 6)))

# =============================================================================================================
print("\n== K. The Deligne module O_K = Z[pi, 5/pi] with its canonical principal form, in a symplectic basis")
I4 = sp.eye(4)
Mpi = sp.Matrix([[0, 0, -5, 0], [0, 0, 0, -5], [1, 0, 0, 3], [0, 1, 1, 3]])      # columns: pi*1, pi*beta, pi*pi, pi*beta*pi
Mbeta = sp.Matrix([[0, 3, 0, 0], [1, 3, 0, 0], [0, 0, 0, 3], [0, 0, 1, 3]])
MV = Mbeta - Mpi
Cj = sp.Matrix([[1, 0, 0, 3], [0, 1, 1, 3], [0, 0, -1, 0], [0, 0, 0, -1]])        # coordinates of conj(b_k)
basisM = [I4, Mbeta, Mpi, Mbeta * Mpi]
def mult(xv):
    return sum((xv[i] * basisM[i] for i in range(4)), sp.zeros(4))
check("K1 multiplication by pi on (1, beta, pi, beta pi) has characteristic polynomial chi; V = beta - pi is integral; pi V = 5; "
      "conjugation is a ring map swapping pi and V",
      sp.Poly(Mpi.charpoly(x).as_expr(), x) == chi and Mpi * MV == 5 * I4
      and Cj * Mpi == MV * Cj and Cj * Cj == I4 and Cj * Mbeta == Mbeta * Cj)
Zpi = sp.Matrix.hstack(*[Mpi ** i * I4[:, 0] for i in range(4)])
check("K2 the companion lattice Z[pi] = span(1, pi, pi^2, pi^3) has index 5 in O_K and is not V-stable: Z[F] is not a Deligne module here "
      "(in genus one Z[F] = Z[F, V] automatically)",
      abs(Zpi.det()) == 5 and not all(v.q == 1 for v in Zpi.inv() * MV * Zpi), f"det = {Zpi.det()}")
def gram(z_mat):
    G = sp.zeros(4)
    for i in range(4):
        for k in range(4):
            G[i, k] = (basisM[i] * mult(Cj[:, k]) * z_mat).trace()
    return G
hprime_beta = 2 * Mbeta - 3 * I4
Mdd = (Mpi - MV) * hprime_beta
Gcan = gram(Mdd.inv())
Gplus = gram((MV - Mpi).inv())
Ttr = sp.Matrix(4, 4, lambda i, k: (basisM[i] * mult(Cj[:, k])).trace())
check("K3 Om_can(x, y) = Tr(x conj(y)/dd), dd = (pi - V) h'(beta): integral, alternating, unimodular (dd generates the different; Euler's lemma twice), "
      "and Om_can(pi x, pi y) = 5 Om_can(x, y)",
      all(v.q == 1 for v in Gcan) and Gcan.T == -Gcan and Gcan.det() == 1 and Mpi.T * Gcan * Mpi == 5 * Gcan, f"Gram {Gcan.tolist()}")
check("K4 Om_+(x, y) = Tr(x conj(y)/(V - pi)) is integral, alternating, a 5-similitude, of determinant disc(h)^2 = 441, and Om_+ = -Om_can(., h'(F+V) .)",
      all(v.q == 1 for v in Gplus) and Gplus.T == -Gplus and Gplus.det() == 441 and Mpi.T * Gplus * Mpi == 5 * Gplus
      and Gplus == -Gcan * hprime_beta, f"det {Gplus.det()}")
# symplectic basis for Om_can over Z
def symplectic_basis(G):
    n = G.rows
    vecs = [sp.Matrix(v) for v in itertools.product(range(-2, 3), repeat=n) if any(v)]
    w = lambda a, b: (a.T * G * b)[0]
    e1 = sp.Matrix([1] + [0] * (n - 1))
    f1 = next(v for v in vecs if w(e1, v) == 1)
    rest = [v for v in vecs if w(v, e1) == 0 and w(v, f1) == 0]
    for e2 in rest:
        for f2 in rest:
            if w(e2, f2) == 1:
                B = sp.Matrix.hstack(e1, e2, f1, f2)
                if abs(B.det()) == 1:
                    return B
B = symplectic_basis(Gcan)
OM = omega(2)
M = B.inv() * Mpi * B
V = B.inv() * MV * B
check("K5 a symplectic Z-basis of (O_K, Om_can) exists; in it M is an integer matrix with M^T Omega M = 5 Omega, V = 5 M^{-1} integral",
      B.T * Gcan * B == OM and all(v.q == 1 for v in M) and M.T * OM * M == 5 * OM and M * V == 5 * I4,
      f"M = {M.tolist()}")

# =============================================================================================================
print("\n== Q. The cone of similitude forms, the vacuum and the Weil form (example 1)")
check("Q1 the symmetric B with M^T B M = 5B form a 2-dimensional space (one weight per mode)", sim_space_dim(M, 5) == 2)
s21 = sp.sqrt(21)
lams = [(3 + s21) / 2, (3 - s21) / 2]
S = M + V
projs = [(S - lams[1] * I4) / (lams[0] - lams[1]), (S - lams[0] * I4) / (lams[1] - lams[0])]
check("Q2 mode projectors pi_j = (F + V - lam_k)/(lam_j - lam_k) are complementary idempotents commuting with M, and Omega-orthogonal",
      is_zero(projs[0] * projs[0] - projs[0]) and is_zero(projs[0] + projs[1] - I4) and is_zero(projs[0] * M - M * projs[0])
      and is_zero(projs[0].T * OM * projs[1]))
J, ksign = vacuum(M, V, OM, projs, lams, 5)
OMn, Mn, Vn = num(OM), num(M), num(V)
GJ = OMn * J
check("Q3 vacuum of Om_can: J^2 = -1, JM = MJ, J symplectic, G_J = Omega J symmetric positive, a 5-similitude",
      mnorm(J * J + mp.eye(4)) < 1e-30 and mnorm(J * Mn - Mn * J) < 1e-30 and mnorm(J.T * OMn * J - OMn) < 1e-30
      and mnorm(GJ - GJ.T) < 1e-30 and min(mp.eig(GJ)[0], key=lambda v: mp.re(v)).real > 0 and mnorm(Mn.T * GJ * Mn - 5 * GJ) < 1e-28,
      f"Krein signs of the modes lam = {[round(float(l), 4) for l in lams]}: {ksign}")
Wc = OM * (M - V) / 2
check("Q4 the Weil form W = (1/2) Omega (M - V) of the principal form Om_can is symmetric and a 5-similitude (exact), but INDEFINITE, signature (2, 2)",
      Wc == Wc.T and M.T * Wc * M == 5 * Wc and signature(Wc) == (2, 2), f"W = {Wc.tolist()}")
wW = weights(num(Wc), GJ, projs, 4)
check("Q5 W relative to the vacuum: weight eps_j sqrt(4q - lam_j^2)/2 = eps_j Im(alpha_j) on mode j (eps_j the Krein sign)",
      all(abs(wW[j] - ksign[j] * mp.sqrt(20 - mp.mpf(sp.N(lams[j], 50)) ** 2) / 2) < 1e-28 for j in range(2)) and block_diag_ok(num(Wc), projs),
      f"weights {[mp.nstr(w, 12) for w in wW]}")
check("Q6 Williamson: symplectic spectrum of G_J is (1, 1) (a pure state); of the positive form |W| = sum_j eps_j W|_j it is sqrt(4q - lam_j^2)/2",
      symplectic_eigs(sp.Matrix(GJ.tolist()).applyfunc(lambda v: float(v)), OM) == [1.0]
      and np.allclose(symplectic_eigs(sp.Matrix(4, 4, lambda i, k: float(sum(ksign[j] * num(projs[j].T * Wc * projs[j])[i, k] for j in range(2)))), OM),
                      sorted(float(sp.sqrt(20 - sp.N(l) ** 2) / 2) for l in lams)))

# =============================================================================================================
print("\n== R. The Rosati form on R[F], transported by the cyclic vector e = 1 of O_K")
Tg = sp.Matrix(4, 4, lambda i, k: (Mpi ** i * MV ** k).trace())
check("R1 Rosati Gram T_ik = Tr(F^i V^k) = q^min(i,k) s_|i-k| on (1, F, F^2, F^3): integer, symmetric, positive definite, T(F., F.) = 5 T",
      Tg == Tg.T and Tg.is_positive_definite and sp.Matrix(4, 4, lambda i, k: Tg[i + 1, k + 1] if i < 3 and k < 3 else 0)[:3, :3] == 5 * Tg[:3, :3],
      f"T = {Tg.tolist()}")
Psi = B.inv() * Zpi
TL = Psi.inv().T * Tg * Psi.inv()
check("R2 transported T_L = Psi^{-T} T Psi^{-1} (Psi = [e, Me, M^2 e, M^3 e], e = 1): a 5-similitude, positive, and integral on O_K "
      "although Psi maps Z[F] onto Z[pi], of index 5",
      M.T * TL * M == 5 * TL and TL.is_positive_definite and all(v.q == 1 for v in TL), f"T_L = {TL.tolist()}")
check("R3 on O_K the transported form is the trace form: T_L = B^T (Tr(x conj y)) B", TL == B.T * Ttr * B)
wT = weights(num(TL), GJ, projs, 4)
pred = [mp.sqrt(21) * mp.sqrt(20 - mp.mpf(sp.N(l, 50)) ** 2) for l in lams]
ratio = wT[1] / wT[0]
check("R4 T_L is NOT proportional to G_J; T_L = sum_j |h'(lam_j)| sqrt(4q - lam_j^2) G_J|_j, i.e. the vacuum weight relative to Rosati is "
      "1/(sqrt21 d_j) (04w's c_j^0 = 0.0919994481, 0.0495772273)",
      block_diag_ok(num(TL), projs) and all(abs(wT[j] - pred[j]) < 1e-27 for j in range(2)) and abs(ratio - 1) > 0.5,
      f"T/G_J weights {[mp.nstr(w, 12) for w in wT]}; 1/weights {[mp.nstr(1 / w, 10) for w in wT]}")
R0 = (25 + 3 * mp.sqrt(21)) / (2 * mp.sqrt(109))
check("R5 the ratio of the two weights is d_1/d_2 or its inverse = 04w's R_0 = (25 + 3 sqrt21)/(2 sqrt109) = 1.8556795747",
      abs(max(ratio, 1 / ratio) - R0) < 1e-28, f"ratio {mp.nstr(max(ratio, 1 / ratio), 12)}")
Gp_L = B.T * Gplus * B
Wp = Gp_L * (M - V) / 2
check("R6 THE GENUS-g BRIDGE (exact): the Weil form of Om_+ = Tr(x conj y/(V - F)) is half the transported Rosati form, (1/2) Om_+ (M - V) = T_L / 2",
      Wp == TL / 2)
Jp, ksp = vacuum(M, V, Gp_L, projs, lams, 5)
GJp = num(Gp_L) * Jp
wTp = weights(num(TL), GJp, projs, 4)
check("R7 the vacuum of Om_+ is the Rosati form with weight 1/sqrt(4q - lam_j^2) on mode j; Om_+ has the Krein signs (+, +) (type Phi_+)",
      ksp == [1, 1] and all(abs(wTp[j] - mp.sqrt(20 - mp.mpf(sp.N(lams[j], 50)) ** 2)) < 1e-27 for j in range(2)),
      f"Rosati/vacuum weights {[mp.nstr(w, 12) for w in wTp]}")
check("R8 genus-two accident: |h'(lam_1)| = |h'(lam_2)| = sqrt(disc h), so the two vacua are proportional, G_{J_+} = sqrt21 G_{J_can}",
      mnorm(GJp - mp.sqrt(21) * GJ) < 1e-27)
def genus_one(q, a):
    """Z[F] = Z[F, V], basis (1, F); Om_+ = Tr(x conj y/(V - F)) is Om_can (h' = 1); returns (det, Rosati/vacuum weight, lane A's S-map test)"""
    MF = sp.Matrix([[0, -q], [1, a]])
    MVv = a * sp.eye(2) - MF
    Cc = sp.Matrix([[1, a], [0, -1]])                                  # conj(1) = 1, conj(F) = a - F
    bas = [sp.eye(2), MF]
    mul = lambda v: v[0] * bas[0] + v[1] * bas[1]
    zm = (MVv - MF).inv()
    Gr = sp.Matrix(2, 2, lambda i, k: (bas[i] * mul(Cc[:, k]) * zm).trace())
    Tl = sp.Matrix(2, 2, lambda i, k: (bas[i] * mul(Cc[:, k])).trace())
    Wl = Gr * (MF - MVv) / 2
    Jl = (MF - MVv) / sp.sqrt(4 * q - a * a)
    s_ = 1 if (Gr * Jl)[0, 0] > 0 else -1
    Gv = s_ * Gr * Jl
    return Gr.det(), sp.simplify(Tl[0, 0] / Gv[0, 0]), Wl == Tl / 2 and sp.simplify(Tl - sp.sqrt(4 * q - a * a) * Gv) == sp.zeros(2)
r9 = [genus_one(q_, a_) for q_, a_ in [(2, -1), (5, -2), (7, 2)]]
check("R9 genus one (E1, E2, E3 of curve-bridge.md): Om_+ = Om_can is unimodular on Z[F], its Weil form is T/2 and Rosati/vacuum = sqrt(4q - a^2): lane A's scalar",
      all(d == 1 and ok_ for d, _, ok_ in r9), f"weights {[w for _, w, _ in r9]}")

# =============================================================================================================
print("\n== U. Integral markings do not fix a point: the real unit eps = 1 + beta = (5 + sqrt21)/2")
eps = sp.Matrix([1, 1, 0, 0])
Meps = mult(eps)
check("U1 eps = 1 + beta is a unit of O_K (norm 1, both real embeddings positive); e' = eps.1 also generates O_K over Z[pi, V]",
      abs(Meps.det()) == 1 and all((1 + l).evalf() > 0 for l in lams) and all(v.q == 1 for v in Meps.inv()))
Psi2 = B.inv() * sp.Matrix.hstack(*[Mpi ** i * eps for i in range(4)])
TL2 = Psi2.inv().T * Tg * Psi2.inv()
wT2 = weights(num(TL2), GJ, projs, 4)
e1v = [1 + mp.mpf(sp.N(l, 50)) for l in lams]
check("U2 transporting by e' = eps e divides the weights by eps_j^2: a different point of the cone; the ratio moves by eps_1^4 = (527 + 115 sqrt21)/2 (04w)",
      all(abs(wT2[j] - wT[j] / e1v[j] ** 2) < 1e-25 for j in range(2)) and abs((wT2[1] / wT2[0]) / (wT[1] / wT[0]) - e1v[0] ** 4) / e1v[0] ** 4 < 1e-25,
      f"new weights {[mp.nstr(w, 10) for w in wT2]}")

# =============================================================================================================
print("\n== H. Which CM type the arithmetic picks (PARI: primes above 5 in the Galois closure)")
out = gp("""f=x^4-3*x^3+7*x^2-15*x+25; spl=nfsplitting(f); N=nfinit(subst(spl,x,y)); rts=nfroots(N,f); th=polroots(N.pol)[1];
for(i=1,#rts, z=subst(lift(rts[i]),y,th); print(real(z)," ",imag(z)));
P=idealprimedec(N,5); print(#P); for(k=1,#P, print(vector(#rts,i,idealval(N,rts[i],P[k]))));""")
lines = out.strip().split("\n")
roots = [complex(float(l.split()[0]), float(l.split()[1])) for l in lines[:4]]
nP = int(lines[4])
SP = [frozenset(i for i, v in enumerate(eval(l)) if v > 0) for l in lines[5:5 + nP]]
Phip = frozenset(i for i, r in enumerate(roots) if r.imag > 0)
conj = lambda S_: frozenset(min(range(4), key=lambda k: abs(roots[k] - roots[i].conjugate())) for i in S_)
def dd(a):
    return (a - 5 / a) * (2 * (a + 5 / a) - 3)
Phican = frozenset(i for i, r in enumerate(roots) if (1 / dd(r)).imag > 0)
n_plus = sum(1 for s_ in SP if s_ in (Phip, conj(Phip)))
n_can = sum(1 for s_ in SP if s_ in (Phican, conj(Phican)))
check("H1 eight primes above 5; every S_P is a CM type; 4 of them give Phi_+ (or its conjugate), the other 4 the type of Om_can (or conjugate)",
      nP == 8 and all(len(s_) == 2 and conj(s_) == frozenset(range(4)) - s_ for s_ in SP) and n_plus == 4 and n_can == 4 and Phican not in (Phip, conj(Phip)),
      f"Phi_+ = {sorted(Phip)}, Phi_can = {sorted(Phican)}, S_P = {[sorted(s_) for s_ in SP]}")
check("H2 hence for half of the choices eps the arithmetic polarisation has the mixed type (its Weil form is indefinite, as Q4), "
      "for the other half it has type Phi_+ (its Weil form is positive); on O_K every principal form is +-eps^k Om_can, mixed type",
      n_plus == 4 and n_can == 4)

# =============================================================================================================
print("\n== G. Example 2: K_4 with one negative edge (q = 2, rank 8)")
As = sp.ones(4) - sp.eye(4)
As[0, 1] = As[1, 0] = -1
q2 = 2
I8 = sp.eye(8)
M2 = sp.Matrix(sp.BlockMatrix([[Z(4), -sp.eye(4)], [q2 * sp.eye(4), As]]))
V2 = q2 * M2.inv()
OM4 = omega(4)
check("G1 M^T Omega M = 2 Omega; char poly (x^4 + 3x^2 + 4)(x^4 - x^2 + 4); F + V = A_s (+) A_s with eigenvalues +-1, +-sqrt5",
      M2.T * OM4 * M2 == q2 * OM4 and sp.expand(M2.charpoly(x).as_expr() - (x ** 4 + 3 * x ** 2 + 4) * (x ** 4 - x ** 2 + 4)) == 0
      and M2 + V2 == sp.diag(As, As) and sorted(As.eigenvals()) == sorted([1, -1, sp.sqrt(5), -sp.sqrt(5)]))
check("G2 the similitude forms form a 4-dimensional space (four Williamson modes)", sim_space_dim(M2, q2) == 4)
lams2 = [-sp.sqrt(5), -1, 1, sp.sqrt(5)]
pA = []
for l in lams2:
    P_ = sp.eye(4)
    for m in lams2:
        if m != l:
            P_ = P_ * (As - m * sp.eye(4)) / (l - m)
    pA.append(sp.simplify(P_))
projs2 = [sp.diag(P_, P_) for P_ in pA]
J2, ks2 = vacuum(M2, V2, OM4, projs2, lams2, q2)
G2 = num(OM4) * J2
W2 = OM4 * (M2 - V2) / 2
check("G3 the Weil form of the standard Omega is [[qI, A/2],[A/2, I]], positive, a similitude; all Krein signs +; vacuum G_J positive; "
      "W = sum_j sqrt(8 - lam_j^2)/2 G_J|_j",
      W2 == sp.Matrix(sp.BlockMatrix([[q2 * sp.eye(4), As / 2], [As / 2, sp.eye(4)]])) and W2.is_positive_definite and M2.T * W2 * M2 == q2 * W2
      and ks2 == [1, 1, 1, 1] and all(abs(w - mp.sqrt(8 - mp.mpf(sp.N(l, 50)) ** 2) / 2) < 1e-27 for w, l in zip(weights(num(W2), G2, projs2, 8), lams2)))
P = sp.Matrix([[-1, -2, 1, 1], [-2, -1, 1, 1], [1, 1, -1, 0], [1, 1, 0, -1]])
pvals = []
for j in range(4):
    col = next(c for c in range(4) if any(v != 0 for v in pA[j][:, c]))
    v = pA[j][:, col]
    k = next(i for i in range(4) if v[i] != 0)
    pvals.append(sp.nsimplify(sp.simplify((P * v)[k] / v[k]), [sp.sqrt(5)]))
phi = (1 + sp.sqrt(5)) / 2
check("G4 Howe's unit P (howe-positivity.md section 4) commutes with A_s, det 1; its value on the modes lam = -sqrt5, -1, 1, sqrt5 is "
      "(-phi^3, -1, 1, phi^-3): opposite signs at lam and -lam",
      P * As == As * P and P.det() == 1 and all(sp.simplify(pv - t) == 0 for pv, t in zip(pvals, [-phi ** 3, -1, 1, phi ** -3])),
      f"p(lam_j) = {pvals}")
OMP = OM4 * sp.diag(P, P)
check("G5 Om_P = Omega (P (+) P) is alternating, unimodular, a 2-similitude", OMP.T == -OMP and OMP.det() == 1 and M2.T * OMP * M2 == q2 * OMP)
JP, ksP = vacuum(M2, V2, OMP, projs2, lams2, q2)
RP = num(OMP) * JP
wRP = weights(RP, G2, projs2, 8)
check("G6 the Riemann form Om_P(., J_P .) of the principal polarisation: J_P = sigma J with sigma = sign p(lam_j); weights |p(lam_j)| = (phi^3, 1, 1, phi^-3) relative to G_J",
      ksP == [int(sp.sign(pv)) for pv in pvals] and mnorm(RP - RP.T) < 1e-28 and block_diag_ok(RP, projs2)
      and all(abs(w - abs(mp.mpf(sp.N(pv, 50)))) < 1e-27 for w, pv in zip(wRP, pvals)),
      f"sigma = {ksP}, weights {[mp.nstr(w, 10) for w in wRP]}")
WP = OMP * (M2 - V2) / 2
check("G7 the Weil form of the principal polarisation, (1/2) Om_P (M - V), is a similitude but indefinite, signature (4, 4)",
      WP == WP.T and M2.T * WP * M2 == q2 * WP and signature(WP) == (4, 4))
hp = lambda l: 4 * l ** 3 - 12 * l                                   # h(y) = (y^2 - 1)(y^2 - 5)
r1 = [abs(mp.mpf(sp.N(pv, 50))) * abs(mp.mpf(sp.N(hp(l), 50))) for pv, l in zip(pvals, lams2)]
check("G8 NOT the function of example 1: |p(lam_j)| is not c/|h'(lam_j)| (the principal-vs-Phi_+ weight of example 1); |p| |h'| is not constant",
      max(r1) / min(r1) > 2, f"|p(lam)| |h'(lam)| = {[mp.nstr(v, 8) for v in r1]}")
cP = sp.Matrix.hstack(*[(As ** i).reshape(16, 1) for i in range(4)]).solve_least_squares(P.reshape(16, 1))
check("G9 P is not in Z[A_s] (coefficients not integral), so Z^8 is not a free Z[F, V]-module: no integral cyclic generator e exists",
      not all(sp.Rational(c).q == 1 for c in cP), f"P = {list(cP)} in the basis 1, A, A^2, A^3")
T2 = sp.Matrix(8, 8, lambda i, k: (M2 ** i * V2 ** k).trace())
e2 = sp.Matrix([0, 0, 0, 0, 1, 2, 3, 5])
Psi_2 = sp.Matrix.hstack(*[M2 ** i * e2 for i in range(8)])
TL2b = Psi_2.inv().T * T2 * Psi_2.inv()
wK = weights(num(TL2b), G2, projs2, 8)
predK = [2 / (num(projs2[j] * e2).T * G2 * num(projs2[j] * e2))[0] for j in range(4)]
check("G10 Rosati transported by a rational cyclic vector e: a similitude, positive; weights relative to G_J are 2/G_J(pi_j e) (e-dependent)",
      Psi_2.det() != 0 and M2.T * TL2b * M2 == q2 * TL2b and all(abs(wK[j] - predK[j]) / predK[j] < 1e-25 for j in range(4)),
      f"e = {list(e2)}, weights {[mp.nstr(w, 8) for w in wK]}")

# =============================================================================================================
print("\n== X. Item 3: RH, the cone, and the Weil form")
ok = True
for (MM, OO, qq, nm) in [(M, OM, 5, "example 1"), (M2, OM4, q2, "K_4")]:
    n = MM.rows
    g = n // 2
    SS = MM + qq * MM.inv()
    comp = [OO * (SS ** k) for k in range(g)]                      # compatible alternating forms Omega (F+V)^k
    Ws = [C_ * (MM - qq * MM.inv()) / 2 for C_ in comp]
    ok &= all(C_.T == -C_ and MM.T * C_ * MM == qq * C_ for C_ in comp)
    ok &= all(W_.T == W_ and MM.T * W_ * MM == qq * W_ for W_ in Ws)
    ok &= sp.Matrix.hstack(*[W_.reshape(n * n, 1) for W_ in Ws]).rank() == g == sim_space_dim(MM, qq)
check("X1 for any compatible alternating Om, (1/2) Om (M - V) is symmetric and a q-similitude; Om -> W_Om is a linear isomorphism from the g-dim space "
      "of compatible forms onto the g-dim space of similitude forms (both examples)", ok)
Mh = sp.Matrix([[0, -1], [5, 5]])
Wh = omega(1) * (Mh - 5 * Mh.inv()) / 2
check("X2 RH failing (hyperbolic step x^2 - 5x + 5): the cone is empty (only similitude forms are indefinite) and the Weil form is indefinite",
      sim_space_dim(Mh, 5) == 1 and Mh.T * Wh * Mh == 5 * Wh and signature(Wh) == (1, 1))
Mb = sp.Matrix([[0, 1], [-5, -2]])
Wb = omega(1) * (Mb - 5 * Mb.inv()) / 2
check("X3 RH holding but the Weil form NEGATIVE definite: M' = [[0,1],[-5,-2]], M'^T Omega M' = 5 Omega, chi = x^2 + 2x + 5 "
      "(so lattice-tower section 5 (i) => (ii) needs the orientation: true for the graph steps, not for every compatible Omega)",
      Mb.T * omega(1) * Mb == 5 * omega(1) and signature(Wb) == (0, 2))

print(f"\n{npass} of {npass + nfail} pass" + ("" if nfail == 0 else f"  ({nfail} FAIL)"))
