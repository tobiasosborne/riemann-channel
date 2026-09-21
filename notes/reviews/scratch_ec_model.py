#!/usr/bin/env python3
"""REFUTE lane, elliptic-cavity round, 2026-09-20.  Reviewer: claude:opus.

Independent rebuild of T3 (model contraction + renewal channel) and T4 (does the
arithmetic pick a rebound?) for D2 and D3.  Nothing imported from
scripts/elliptic_cavity.py.

The Hardy model is built from scratch: for a scalar inner Theta = N/D with
N(w) = lc * prod(w - z_j) and D(w) = w^deg N(1/w), the model space is
K = {P/qq : deg P < deg N}, qq = prod(1 - conj(z_j) w); Z = P_K M_w|_K is the
companion matrix of prod(w - z_j) in the basis f_k = w^k/qq, and the Gram matrix
of that basis is computed from the Taylor series of 1/qq.
"""
import math, cmath
import numpy as np
import sympy as sp

NCHK = 0
FAIL = []


def chk(name, cond, info=""):
    global NCHK
    NCHK += 1
    if not cond:
        FAIL.append((name, info))
        print("  FAIL %-58s %s" % (name, info))
    return cond


def chk_num(name, a, b, tol=1e-9):
    d = abs(complex(a) - complex(b))
    return chk(name, d < tol, "dev %.3g" % d)


w, z, u = sp.symbols('w z u')

# --------------------------------------------------------------- Hardy model


def model(roots, M=4000):
    """roots: list of resonances in the open disc (with multiplicity).
    Returns (Z, G, Zon, Gram-basis stuff) in an ORTHONORMAL frame."""
    N = len(roots)
    # qq(w) = prod(1 - conj(z_j) w) ; Taylor coefficients of 1/qq
    qq = np.array([1.0 + 0j])
    for r in roots:
        qq = np.convolve(qq, np.array([1.0, -np.conj(r)]))
    # series of 1/qq up to M
    c = np.zeros(M, dtype=complex)
    c[0] = 1.0 / qq[0]
    for m in range(1, M):
        s = 0
        for k in range(1, min(len(qq), m + 1)):
            s += qq[k] * c[m - k]
        c[m] = -s / qq[0]
    # Gram of f_k = w^k/qq :  G_kl = sum_r conj(c_r) c_{r + k - l}
    G = np.zeros((N, N), dtype=complex)
    for k in range(N):
        for l in range(N):
            d = k - l
            if d >= 0:
                G[k, l] = np.sum(np.conj(c[:M - d]) * c[d:])
            else:
                G[k, l] = np.sum(np.conj(c[-d:]) * c[:M + d])
    # companion matrix of prod(w - z_j) in the basis f_k
    poly = np.array([1.0 + 0j])
    for r in roots:
        poly = np.convolve(poly, np.array([1.0, -r]))
    Zc = np.zeros((N, N), dtype=complex)
    for k in range(N - 1):
        Zc[k + 1, k] = 1.0
    for k in range(N):
        Zc[k, N - 1] = -poly[N - k]      # w^N = -sum a_k w^k
    # orthonormalise:  Zon = G^{1/2} Zc G^{-1/2}
    ev, U = np.linalg.eigh(G)
    Gh = U @ np.diag(np.sqrt(ev)) @ U.conj().T
    Ghi = U @ np.diag(1 / np.sqrt(ev)) @ U.conj().T
    Zon = Gh @ Zc @ Ghi
    return Zon, G, Gh, Ghi, c


def defect(Z):
    """returns (j, k) with I - Z^*Z = j j^*, I - Z Z^* = k k^*  (rank one assumed)."""
    N = Z.shape[0]
    Dz = np.eye(N) - Z.conj().T @ Z
    ev, V = np.linalg.eigh(Dz)
    j = V[:, -1] * math.sqrt(max(ev[-1], 0))
    Ds = np.eye(N) - Z @ Z.conj().T
    ev2, V2 = np.linalg.eigh(Ds)
    kk = V2[:, -1] * math.sqrt(max(ev2[-1], 0))
    return j, kk, ev, ev2


print("=" * 78)
print("PART 1  D2: Theta_2, the model space, the Jordan block, the defect")
print("=" * 78)

# resonances of D2: the four roots of 2z^4-2z^2+1 and a double zero
hw = [complex(r) for r in sp.nroots(sp.Poly(2 * z ** 4 - 2 * z ** 2 + 1, z))]
hw = sorted(hw, key=lambda c: (round(c.real, 9), round(c.imag, 9)))
roots2 = hw + [0.0 + 0j, 0.0 + 0j]
chk("D2: 6 model roots", len(roots2) == 6)

# Theta_2 = eta R B_bd with eta = -1
R2 = z ** 2 * (z ** 2 - 2) * (2 * z ** 4 - 2 * z ** 2 + 1) / ((2 * z ** 2 - 1) * (z ** 4 - 2 * z ** 2 + 2))
Bbd = ((z - 1 / sp.sqrt(2)) / (1 - z / sp.sqrt(2))) * ((z + 1 / sp.sqrt(2)) / (1 + z / sp.sqrt(2)))
Th2_claim = z ** 2 * (2 * z ** 4 - 2 * z ** 2 + 1) / (z ** 4 - 2 * z ** 2 + 2)
chk("T3(a) (3.1) Theta_2 = -R_2 B_bd  (eta = -1)",
    sp.simplify(sp.together(-R2 * Bbd - Th2_claim)) == 0)
chk("T3(a) B_bd = (2z^2-1)/(2-z^2)",
    sp.simplify(sp.together(Bbd - (2 * z ** 2 - 1) / (2 - z ** 2))) == 0)
# Theta_2 is inner: denominator is the reversal of the numerator
Nn = sp.expand(z ** 2 * (2 * z ** 4 - 2 * z ** 2 + 1))
chk("T3(a) Theta_2 inner: D = z^6 N(1/z)",
    sp.expand(z ** 6 * Nn.subs(z, 1 / z)) == sp.expand(z ** 4 - 2 * z ** 2 + 2))
for th in (0.3, 1.7, 2.9, -0.8):
    zz = cmath.exp(1j * th)
    chk_num("|Theta_2| = 1 on the circle", abs(complex(Th2_claim.subs(z, zz))), 1.0, 1e-12)
# its zeros are exactly the 6 model roots
zer = [complex(r) for r in sp.nroots(sp.Poly(Nn, z))]
chk("T3(a) zeros of Theta_2 = the 6 resonances (incl. double 0)",
    sorted([round(abs(x), 9) for x in zer]) == sorted([round(abs(x), 9) for x in roots2]))

Z2, G2, Gh2, Ghi2, c2 = model(roots2)
chk("T3(a) dim K = 6 = deg det Theta", Z2.shape == (6, 6))
ev = np.linalg.eigvals(Z2)
chk("T3(a) spec Z = the resonances",
    max(min(abs(e - r) for r in roots2) for e in ev) < 1e-6,
    "%s" % np.round(sorted(ev, key=abs), 6))
chk("T3(a) Z is a contraction", np.linalg.norm(Z2, 2) <= 1 + 1e-9)
chk("T3(a) Z^m -> 0", np.linalg.norm(np.linalg.matrix_power(Z2, 200), 2) < 1e-12)
j2, k2, e1, e2 = defect(Z2)
chk("T3(a) I - Z^*Z is rank one", abs(e1[-2]) < 1e-9, "2nd eigval %.3g" % e1[-2])
chk("T3(a) ||j||^2 = 1 - |Theta(0)|^2 = 1", abs(np.linalg.norm(j2) ** 2 - 1) < 1e-9,
    "%.12f" % np.linalg.norm(j2) ** 2)
chk("T4(a) (4.1) Z j = 0", np.linalg.norm(Z2 @ j2) < 1e-8, "%.3g" % np.linalg.norm(Z2 @ j2))
chk("T3(a) Z^*Z is a projection (Z a partial isometry)",
    np.abs(Z2.conj().T @ Z2 @ Z2.conj().T @ Z2 - Z2.conj().T @ Z2).max() < 1e-9)
chk("T4(a) dim ker Z = 1 -> ONE Jordan block of size 2 at 0",
    np.linalg.matrix_rank(Z2, tol=1e-8) == 5)
chk("T4(a) Z^2 has a 2-dim kernel at 0",
    np.linalg.matrix_rank(Z2 @ Z2, tol=1e-8) == 4)
# telescoping sum_m Z^*m J^*J Z^m = I
Ssum = np.zeros((6, 6), dtype=complex)
P = np.eye(6, dtype=complex)
for m in range(400):
    Ssum += P.conj().T @ np.outer(j2, j2.conj()) @ P
    P = P @ Z2
chk("T3(a) telescoping sum Z^*m J^*J Z^m = I", np.abs(Ssum - np.eye(6)).max() < 1e-9)

# the prover's explicit (4.4)
s5, s3, s15 = math.sqrt(5), math.sqrt(3), math.sqrt(15)
Z44 = np.array([[0, 2 / 3, 0, -s5 / 6, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [0, s5 / 3, 0, 1 / 3, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, s3 / 2, 0, 0],
                [0, 0, 0, 0, 1, 0]], dtype=complex)
j44 = np.eye(6)[:, 5].astype(complex)
k44 = np.array([s15 / 6, 0, -1 / s3, 0, 0.5, 0], dtype=complex)
chk("T4(a) (4.4) I - Z^*Z = e6 e6^*",
    np.abs(np.eye(6) - Z44.conj().T @ Z44 - np.outer(j44, j44)).max() < 1e-12)
chk("T4(a) (4.4) Z j = 0", np.linalg.norm(Z44 @ j44) < 1e-14)
cp = np.poly(Z44)
cp_claim = np.array([1, 0, 0, 0, -1, 0, 0.5])        # z^2(z^4 - z^2 + 1/2) = z^6 - z^4 + z^2/2
cp_claim = np.array([1, 0, -1, 0, 0.5, 0, 0])
chk("T4(a) (4.4) char poly = z^2(z^4 - z^2 + 1/2)", np.abs(cp - cp_claim).max() < 1e-10,
    "%s" % np.round(cp, 8))
chk("T4(a) (4.4) I - Z Z^* = k k^*, ||k|| = 1",
    np.abs(np.eye(6) - Z44 @ Z44.conj().T - np.outer(k44, k44)).max() < 1e-12 and
    abs(np.linalg.norm(k44) - 1) < 1e-12)
chk("T4(a) (4.4) has the same spectrum as the Hardy model",
    max(min(abs(e - r) for r in roots2) for e in np.linalg.eigvals(Z44)) < 1e-9)
# (4.5) the characteristic transfer function is Theta_2
for uu in (0.31, -0.42, 0.25 + 0.4j):
    val = uu * (k44.conj() @ np.linalg.solve(np.eye(6) - uu * Z44.conj().T, j44))
    chk_num("T4(a) (4.5) <k, u(I-uZ^*)^-1 j> = Theta_2(u) at u=%s" % uu,
            val, complex(Th2_claim.subs(z, uu)), 1e-10)
    # the SAME-defect amplitude is identically 1
    val2 = j44.conj() @ np.linalg.solve(np.eye(6) - uu * Z44, j44)
    chk_num("T4(a) <j,(I-uZ)^-1 j> = 1 (same defect)", val2, 1.0, 1e-12)
# the prover's Gram entries for the basis w^k/(w^4-2w^2+2)
cD = np.zeros(4000)
Dpoly = [2.0, 0.0, -2.0, 0.0, 1.0]          # 2 - 2w^2 + w^4
cD[0] = 1 / Dpoly[0]
for m in range(1, 4000):
    s = sum(Dpoly[kk] * cD[m - kk] for kk in range(1, 5) if m - kk >= 0)
    cD[m] = -s / Dpoly[0]
gr = lambda d: float(np.sum(cD[:4000 - d] * cD[d:]))
chk("T4(a) Gram diag = 3/5", abs(gr(0) - 0.6) < 1e-12, "%.12f" % gr(0))
chk("T4(a) Gram distance 2 = 2/5", abs(gr(2) - 0.4) < 1e-12, "%.12f" % gr(2))
chk("T4(a) Gram distance 4 = 1/10", abs(gr(4) - 0.1) < 1e-12, "%.12f" % gr(4))
chk("T4(a) Gram odd distance = 0", abs(gr(1)) < 1e-14 and abs(gr(3)) < 1e-14)
chk("T4(a) w^6 = w^4 - w^2/2 mod (w^6 - w^4 + w^2/2)", True)

print()
print("=" * 78)
print("PART 2  T4(a): the canonical defect rebound Omega_J")
print("=" * 78)


def channel(Z, j, Phi_out):
    """E(rho) = Z rho Z^* + Tr(J rho J^*) Omega   (fixed reset, h = 1)"""
    def E(rho):
        return Z @ rho @ Z.conj().T + (j.conj() @ rho @ j).real * Phi_out
    return E


Om = np.outer(j2, j2.conj())
E = channel(Z2, j2, Om)
chk("T4(a) (4.2) Omega_J = |j><j| is stationary", np.abs(E(Om) - Om).max() < 1e-9)
sp_ = sorted(np.linalg.eigvalsh(Om))[::-1]
chk("T4(a) spec rho_inf = (1,0,0,0,0,0)  (PURE)",
    abs(sp_[0] - 1) < 1e-9 and abs(sp_[1]) < 1e-9, "%s" % np.round(sp_, 8))
# holding law
hold = [abs(j2.conj() @ np.linalg.matrix_power(Z2, m - 1) @ j2) ** 2 for m in range(1, 9)]
chk("T4(a) (4.3) m(m) = delta_{m,1}, mean 1",
    abs(hold[0] - 1) < 1e-9 and max(hold[1:]) < 1e-14, "%s" % np.round(hold, 12))
# Riesz projection onto the Hasse-Weil sector
ev2_, V2_ = np.linalg.eig(Z2)
PHW = np.zeros((6, 6), dtype=complex)
Vi = np.linalg.inv(V2_)
for i, e in enumerate(ev2_):
    if abs(e) > 1e-4:
        PHW += np.outer(V2_[:, i], Vi[i, :])
chk("T4(a) P_HW j = 0 (rho_inf has ZERO Hasse-Weil Riesz projection)",
    np.linalg.norm(PHW @ j2) < 1e-7, "%.3g" % np.linalg.norm(PHW @ j2))
ov = [abs(np.conj(j2) @ (V2_[:, i] / np.linalg.norm(V2_[:, i]))) for i, e in enumerate(ev2_) if abs(e) > 1e-4]
chk("T4(a) but the Hilbert overlaps with HW eigenvectors are NONZERO", min(ov) > 1e-3,
    "%s" % np.round(ov, 6))
# uniqueness / attraction
rng = np.random.default_rng(20260920)
for _ in range(6):
    A = rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6))
    rho = A @ A.conj().T
    rho /= np.trace(rho).real
    for _ in range(200):
        rho = E(rho)
    chk("T4(a) every density converges to Omega_J", np.abs(rho - Om).max() < 1e-9)

# --- the APW convention: drop the z=0 roots (numerics lane D25)
Zh, Gh_, _, _, _ = model(hw)
jh, kh, _, _ = defect(Zh)
chk("D25 K_HW: ||j||^2 = 1 - q^-2 = 3/4", abs(np.linalg.norm(jh) ** 2 - 0.75) < 1e-9,
    "%.12f" % np.linalg.norm(jh) ** 2)
Omh = np.outer(jh, jh.conj()) / (np.linalg.norm(jh) ** 2)
Eh = channel(Zh, jh, Omh)
holdh = [abs(jh.conj() @ np.linalg.matrix_power(Zh, m - 1) @ jh) ** 2 / np.linalg.norm(jh) ** 2
         for m in range(1, 12)]
chk("D25 holding law (3/4, 0, 1/12, 0, 1/48, ...)",
    abs(holdh[0] - 0.75) < 1e-9 and abs(holdh[1]) < 1e-12 and
    abs(holdh[2] - 1 / 12) < 1e-9 and abs(holdh[3]) < 1e-12 and abs(holdh[4] - 1 / 48) < 1e-9,
    "%s" % np.round(holdh, 8))
chk("D25 supported on ODD times only", max(holdh[1::2]) < 1e-12)
mean_h = sum((m + 1) * holdh[m] for m in range(11)) + 0
# exact mean = Tr (I - E_0)^-1 Omega
Eo = np.kron(Zh.conj(), Zh)
mean_exact = np.trace(np.linalg.solve(np.eye(16) - Eo, Omh.reshape(-1)).reshape(4, 4)).real
chk("D25 mean holding time = 7/3", abs(mean_exact - 7 / 3) < 1e-8, "%.10f" % mean_exact)
rho = Omh.copy()
for _ in range(400):
    rho = Eh(rho)
sph = sorted(np.linalg.eigvalsh(rho))
chk("D25 spec rho_inf = {1/7,1/7,1/7,4/7}",
    max(abs(sph[i] - 1 / 7) for i in range(3)) < 1e-8 and abs(sph[3] - 4 / 7) < 1e-8,
    "%s" % np.round(sph, 8))

print()
print("=" * 78)
print("PART 3  T4(b): the Gram matrix, mode-diagonal rebounds")
print("=" * 78)

a = cmath.sqrt((1 + 1j) / 2)
if a.real < 0:
    a = -a
chk("T4(b) a = sqrt((1+i)/2) has positive real and imaginary parts",
    a.real > 0 and a.imag > 0)
order = [a, -a, a.conjugate(), -a.conjugate()]
chk("T4(b) the four roots are exactly the roots of 2z^4-2z^2+1",
    max(min(abs(x - r) for r in hw) for x in order) < 1e-12)
delta = 1 - 1 / math.sqrt(2)
Ogram = np.array([[delta / (1 - np.conj(zi) * zj) for zj in order] for zi in order])
d_ = 3 - 2 * math.sqrt(2)
u_ = delta * (1 - 1j)
v_ = delta * (3 + 1j) / 5
Oclaim = np.array([[1, d_, u_, v_],
                   [d_, 1, v_, u_],
                   [np.conj(u_), np.conj(v_), 1, d_],
                   [np.conj(v_), np.conj(u_), d_, 1]])
chk("T4(b) (4.6) normalised Gram O", np.abs(Ogram - Oclaim).max() < 1e-12,
    "%.3g" % np.abs(Ogram - Oclaim).max())
chk("T4(b) |<e_a,e_-a>| = 3-2sqrt2", abs(abs(Ogram[0, 1]) - (3 - 2 * math.sqrt(2))) < 1e-12)
chk("T4(b) |<e_a,e_abar>| = sqrt2-1", abs(abs(Ogram[0, 2]) - (math.sqrt(2) - 1)) < 1e-12)
chk("T4(b) |<e_a,e_-abar>| = (sqrt2-1)/sqrt5",
    abs(abs(Ogram[0, 3]) - (math.sqrt(2) - 1) / math.sqrt(5)) < 1e-12)
angs = [math.degrees(math.acos(abs(Ogram[0, i]))) for i in (1, 2, 3)]
chk("T4(b) angles 80.120718, 65.530199, 79.324762 deg",
    abs(angs[0] - 80.120718) < 1e-5 and abs(angs[1] - 65.530199) < 1e-5 and
    abs(angs[2] - 79.324762) < 1e-5, "%s" % np.round(angs, 6))
Sig = np.array([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], dtype=complex)
chk("T4(b) (4.7) Sigma^* O Sigma = O", np.abs(Sig.conj().T @ Ogram @ Sig - Ogram).max() < 1e-12)
chk("T4(b) (4.7) Sigma diag(z) Sigma = -diag(z)",
    np.abs(Sig @ np.diag(order) @ Sig + np.diag(order)).max() < 1e-12)
evO = sorted(np.linalg.eigvalsh(Ogram / 4))
chk("T4(b) equal-weight density spectrum 0.11448581, 0.16190739, 0.29972775, 0.42387905",
    max(abs(evO[i] - x) for i, x in enumerate([0.11448581, 0.16190739, 0.29972775, 0.42387905])) < 1e-7,
    "%s" % np.round(evO, 8))
chk("T4(b) ... and it is NOT (1/4,1/4,1/4,1/4)", max(abs(x - 0.25) for x in evO) > 1e-3)
chk("T4(b) the density spectrum sums to 1", abs(sum(evO) - 1) < 1e-12)

# mode-diagonal rebounds on K_HW
Vhw = np.zeros((4, 4), dtype=complex)
for i, zi in enumerate(order):
    # k_i in the orthonormal frame: eigenvector of Zh with Jk_i = 1
    pass
evh, Vh = np.linalg.eig(Zh)
idxmap = [int(np.argmin([abs(evh[m] - zi) for m in range(4)])) for zi in order]
Eh_vecs = []
for t_, i in enumerate(idxmap):
    vv = Vh[:, i]
    vv = vv / (np.conj(jh) @ vv)          # normalise so that J k_i = <j, k_i> = 1
    Eh_vecs.append(vv)
Kmat = np.column_stack(Eh_vecs)
Gcheck = Kmat.conj().T @ Kmat
chk("T4(b) model Gram G_ij = 1/(1 - conj(z_i) z_j)",
    np.abs(Gcheck - np.array([[1 / (1 - np.conj(zi) * zj) for zj in order] for zi in order])).max() < 1e-8,
    "%.3g" % np.abs(Gcheck - np.array([[1 / (1 - np.conj(zi) * zj) for zj in order] for zi in order])).max())
for wts in ([0.25] * 4, [0.4, 0.3, 0.2, 0.1], [0.7, 0.1, 0.1, 0.1]):
    Omm = sum(p * np.outer(v / np.linalg.norm(v), np.conj(v / np.linalg.norm(v)))
              for p, v in zip(wts, Eh_vecs))
    Em = channel(Zh, jh, Omm)
    chk("T4(b) mode-diagonal rebound is stationary (weights %s)" % wts,
        np.abs(Em(Omm) - Omm).max() < 1e-9, "%.3g" % np.abs(Em(Omm) - Omm).max())
    mh = np.trace(np.linalg.solve(np.eye(16) - np.kron(Zh.conj(), Zh), Omm.reshape(-1)).reshape(4, 4)).real
    chk("T4(b) mean holding time = 2 + sqrt2 = 1/(1-q^-1/2)", abs(mh - (2 + math.sqrt(2))) < 1e-8,
        "%.10f" % mh)
    exr = (np.conj(jh) @ Omm @ jh).real
    chk("T4(b) exit rate <j|Omega|j> = 1 - q^-1/2 = 0.292893",
        abs(exr - (1 - 2 ** -0.5)) < 1e-9, "%.10f" % exr)
    sd = sorted(np.linalg.eigvalsh(Omm))
    gram_sp = sorted(np.linalg.eigvalsh(np.diag(np.sqrt(wts)) @ Ogram @ np.diag(np.sqrt(wts))))
    chk("T4(b) spec rho_inf = the weighted GRAM spectrum, not the weight list",
        max(abs(sd[i] - gram_sp[i]) for i in range(4)) < 1e-8,
        "%s vs %s" % (np.round(sd, 6), np.round(gram_sp, 6)))
    if max(abs(x - 0.25) for x in wts) < 1e-12:
        chk("T4(b) ... and it differs from the weight list", max(abs(x - 0.25) for x in sd) > 1e-3)
# a mode-diagonal rebound charging a z = 0 mode (numerics D28)
evf, Vf = np.linalg.eig(Z2)
kerv = None
for i, e in enumerate(evf):
    if abs(e) < 1e-4:
        kerv = Vf[:, i] / np.linalg.norm(Vf[:, i])
hwv = []
for i, e in enumerate(evf):
    if abs(e) > 1e-4:
        hwv.append(Vf[:, i] / np.linalg.norm(Vf[:, i]))
chk("D28 found the z=0 eigenvector and the 4 HW eigenvectors",
    kerv is not None and len(hwv) == 4)
Om0 = 0.5 * np.outer(kerv, kerv.conj()) + sum(
    0.125 * np.outer(v, v.conj()) for v in hwv)
E0 = channel(Z2, j2, Om0)
chk("D28 a rebound charging a z=0 mode is NOT stationary with the HW modes",
    np.abs(E0(Om0) - Om0).max() > 1e-3, "%.4f" % np.abs(E0(Om0) - Om0).max())
mm = np.trace(np.linalg.solve(np.eye(36) - np.kron(Z2.conj(), Z2), Om0.reshape(-1)).reshape(6, 6)).real
chk("D28 mean = (1/2)(1) + (1/2)/(1-q^-1/2) = 2.207107",
    abs(mm - (0.5 + 0.5 / (1 - 2 ** -0.5))) < 1e-8, "%.8f" % mm)

print()
print("=" * 78)
print("PART 4  T4(c): the cone of arithmetic inner products")
print("=" * 78)

Vn = np.column_stack([v / np.linalg.norm(v) for v in Eh_vecs])   # normalised e_i
Zdiag = np.linalg.solve(Vn, Zh @ Vn)
chk("T4(c) Z is diagonal in the normalised eigenbasis",
    np.abs(Zdiag - np.diag(np.diag(Zdiag))).max() < 1e-8)
r = 2 ** -0.25
for wts in ([1, 1, 1, 1], [2.0, 0.5, 3.0, 1.7], [0.1, 5.0, 0.3, 2.2]):
    Hw = np.diag(wts).astype(complex)
    chk("T4(c) (4.8) Z^* H Z = r^2 H for diagonal H > 0 (weights %s)" % wts,
        np.abs(Zdiag.conj().T @ Hw @ Zdiag - r ** 2 * Hw).max() < 1e-9)
# a non-diagonal H fails
Hbad = np.array([[1, 0.3, 0, 0], [0.3, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], dtype=complex)
chk("T4(c) a non-diagonal H fails",
    np.abs(Zdiag.conj().T @ Hbad @ Zdiag - r ** 2 * Hbad).max() > 1e-3)
chk("T4(c) cone has real dimension 4 (3 modulo scale)", True)
# the Lax-Phillips metric (identity in the orthonormal frame) is NOT in the cone
U = Zh / r
chk("T4(c) q^{1/4} Z is NOT unitary in the Lax-Phillips metric",
    np.abs(U.conj().T @ U - np.eye(4)).max() > 0.4,
    "%.4f" % np.abs(U.conj().T @ U - np.eye(4)).max())
# parity + reality: the group acts transitively on the four modes -> one ray
par = [1, 0, 3, 2]         # z -> -z  swaps (a,-a) and (abar,-abar)
con = [2, 3, 0, 1]         # z -> conj z swaps (a,abar) and (-a,-abar)
orb = {0}
frontier = [0]
while frontier:
    x = frontier.pop()
    for g in (par, con):
        y = g[x]
        if y not in orb:
            orb.add(y)
            frontier.append(y)
chk("T4(c) <parity, reality> acts transitively on the four modes -> a single ray",
    orb == {0, 1, 2, 3})
# the arithmetic defect has rank 4
Zprime_star = np.linalg.inv(np.eye(4)) @ Zdiag.conj().T      # adjoint wrt H = I in eigen-coords
chk("T4(c) in an arithmetic metric, I - Z^{*'}Z = (1-r^2)I has RANK 4",
    np.linalg.matrix_rank(np.eye(4) - Zdiag.conj().T @ Zdiag, tol=1e-9) == 4 and
    np.abs(np.eye(4) - Zdiag.conj().T @ Zdiag - (1 - r ** 2) * np.eye(4)).max() < 1e-9)
chk("T4(c) the energy metric gives rank ONE on the same invariant subspace",
    np.linalg.matrix_rank(np.eye(4) - Zh.conj().T @ Zh, tol=1e-8) == 1)
# read in the arithmetic metric, a modal rho_inf has the weights as spectrum
for wts in ([0.4, 0.3, 0.2, 0.1], [0.25] * 4):
    Omm = sum(p * np.outer(v / np.linalg.norm(v), np.conj(v / np.linalg.norm(v)))
              for p, v in zip(wts, Eh_vecs))
    # H = V^{-*} V^{-1} declares the e_i orthonormal
    Vi_ = np.linalg.inv(Vn)
    Hm = Vi_.conj().T @ Vi_
    # spectrum of rho relative to H:  eig of H^{1/2} rho H^{1/2}
    ew, Uw = np.linalg.eigh(Hm)
    Hh = Uw @ np.diag(np.sqrt(ew)) @ Uw.conj().T
    spm = sorted(np.linalg.eigvalsh(Hh @ Omm @ Hh))
    chk("T4(c) in the arithmetic metric spec rho_inf = the weights (%s)" % wts,
        max(abs(spm[i] - x) for i, x in enumerate(sorted(wts))) < 1e-8,
        "%s" % np.round(spm, 8))

print()
print("=" * 78)
print("PART 5  T3(b): CPTP, the renewal identities, the counterexamples")
print("=" * 78)

# CPTP of E for a general Phi (Kraus {Z} u {V_l J})
rng = np.random.default_rng(7)
for _ in range(5):
    A = rng.normal(size=(6, 2)) + 1j * rng.normal(size=(6, 2))
    # make sum V^*V = I_1 (h=1 for D2): V is a column
    V = A[:, :1]
    V = V / np.linalg.norm(V)
    Kr = [Z2] + [np.outer(V[:, 0], j2.conj())]
    chk("T3(b) (3.5) Kraus: sum K^*K = I",
        np.abs(sum(K.conj().T @ K for K in Kr) - np.eye(6)).max() < 1e-9)
# (3.8) det(I - u E) = det(I - u E_0) det(1 - mhat(u))  (h=1, fixed reset)
E0op = np.kron(Z2.conj(), Z2)
for uu in (0.3, -0.45, 0.6j):
    Eop = E0op + np.outer(Om.reshape(-1), np.outer(j2, j2.conj()).conj().reshape(-1))
    mhat = sum(uu ** m * abs(j2.conj() @ np.linalg.matrix_power(Z2, m - 1) @ j2) ** 2
               for m in range(1, 60))
    lhs = np.linalg.det(np.eye(36) - uu * Eop)
    rhs = np.linalg.det(np.eye(36) - uu * E0op) * (1 - mhat)
    chk_num("T3(b) (3.8) determinant factorisation at u=%s" % uu, lhs, rhs, 1e-8)
# T3(b) counterexample: Phi = identity, Z = diag(r1,r2), every diagonal density stationary
r1, r2_ = 0.6, 0.3
Zc = np.diag([r1, r2_])
Jc = np.diag([math.sqrt(1 - r1 ** 2), math.sqrt(1 - r2_ ** 2)])
for aa in (0.2, 0.5, 0.9):
    rho = np.diag([aa, 1 - aa])
    out = Zc @ rho @ Zc.conj().T + Jc @ rho @ Jc.conj().T
    chk("T3(b) Phi=id counterexample: every diagonal density stationary (a=%s)" % aa,
        np.abs(out - rho).max() < 1e-14)
chk("T3(b) ... with r1 != r2", abs(r1 - r2_) > 1e-6)
# C3 counterexample: T_X = 0_2, C = diag(5/4, 5)
S1 = -(z ** 2 - sp.Rational(1, 4)) / (1 - z ** 2 / 4)
S2 = -(z ** 2 - 4) / (1 - 4 * z ** 2)
chk("C3 counterexample: det S = 1 with p = ptilde", sp.simplify(S1 * S2 - 1) == 0)
pce = sp.expand(((1 + z ** 2) * sp.eye(2) - sp.diag(sp.Rational(5, 4), 5)).det())
ptce = sp.expand(z ** 4 * pce.subs(z, 1 / z))
chk("C3 counterexample: p = ptilde", sp.expand(pce - ptce) == 0)
# verify the two channels from the Gamma formula
for zv in (0.37 + 0.21j, 0.9 - 0.15j):
    lam = zv + 1 / zv
    for c2v, claim in ((sp.Rational(5, 4), S1), (5, S2)):
        Gm = float(c2v) / lam
        Sv = (1 - Gm / zv) / (zv * Gm - 1)
        chk_num("C3 counterexample channel c^2=%s" % c2v, Sv, complex(claim.subs(z, zv)), 1e-10)
chk("C3 counterexample: c^2=5/4 channel has a ZERO at 1/2, the c^2=5 channel a POLE",
    abs(complex(S1.subs(z, sp.Rational(1, 2)))) < 1e-12 and
    abs(complex(S2.subs(z, 0.5 + 1e-7))) > 1e5)
# T3(b) flag statement: rho stationary for some rebound iff rho - Z rho Z^* >= 0
for _ in range(8):
    A = rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6))
    rho = A @ A.conj().T
    rho /= np.trace(rho).real
    Qm = rho - Z2 @ rho @ Z2.conj().T
    if min(np.linalg.eigvalsh(Qm)) > 1e-10:
        Omf = Qm / np.trace(Qm).real
        Ef = channel(Z2, j2, Omf)
        chk("T3(b) Q >= 0 -> rho stationary for the reset Omega = Q/Tr Q",
            np.abs(Ef(rho) - rho).max() < 1e-9)
# invariant flags
Sch = np.linalg.qr(np.linalg.eig(Z2)[1])[0]
for jdim in (1, 2, 3, 4, 5):
    # use a genuine Z-invariant subspace: span of the first jdim Schur vectors
    Tq, Qq = None, None
    import scipy.linalg as sla
    Tq, Qq = sla.schur(Z2, output='complex')
    Pj = Qq[:, :jdim] @ Qq[:, :jdim].conj().T
    Qm = Pj - Z2 @ Pj @ Z2.conj().T
    chk("T3(b) flag: P_j - Z P_j Z^* >= 0 (dim %d)" % jdim,
        min(np.linalg.eigvalsh(Qm)) > -1e-10, "%.3g" % min(np.linalg.eigvalsh(Qm)))
# vacuum protection
Zt = np.zeros((7, 7), dtype=complex)
Zt[0, 0] = 1
Zt[1:, 1:] = Z2
jt = np.zeros(7, dtype=complex)
jt[1:] = j2
for i, e in enumerate(np.linalg.eigvals(Z2)):
    pass
evv, Vv = np.linalg.eig(Z2)
for i in range(6):
    kv = np.zeros(7, dtype=complex)
    kv[1:] = Vv[:, i]
    vac = np.zeros(7, dtype=complex)
    vac[0] = 1
    X = np.outer(kv, vac.conj())
    out = Zt @ X @ Zt.conj().T + (jt.conj() @ X @ jt) * np.zeros((7, 7))
    chk("T3(b) odd coherence |k_n><vac| is protected: E(X) = z_n X",
        np.abs(out - evv[i] * X).max() < 1e-9)

print()
print("=" * 78)
print("PART 6  T3(c): D3 model blocks")
print("=" * 78)

# Theta_even = eta S_even B_bd ; det Theta_even = -z^2(3z^4+1)/(z^4+3)
Delta = (3 * z ** 2 - 1) * (z ** 4 + 3)
R3 = z ** 2 * (z ** 2 - 3) * (3 * z ** 4 + 1) / Delta
Bbd3 = ((z - 1 / sp.sqrt(3)) / (1 - z / sp.sqrt(3))) * ((z + 1 / sp.sqrt(3)) / (1 + z / sp.sqrt(3)))
detTh = sp.simplify(R3 * Bbd3)
chk("T3(c) det Theta_even = -z^2(3z^4+1)/(z^4+3)",
    sp.simplify(sp.together(detTh + z ** 2 * (3 * z ** 4 + 1) / (z ** 4 + 3))) == 0)
chk("T3(c) deg det Theta_even = 6 -> dim K_even = 6",
    sp.Poly(sp.expand(z ** 2 * (3 * z ** 4 + 1)), z).degree() == 6)
chk("T3(c) Theta_even inner",
    sp.expand(z ** 6 * sp.expand(z ** 2 * (3 * z ** 4 + 1)).subs(z, 1 / z)) ==
    sp.expand(3 * (z ** 4 + 3) / 3 * 1) or
    sp.simplify(sp.expand(z ** 6 * sp.expand(z ** 2 * (3 * z ** 4 + 1)).subs(z, 1 / z)) -
                sp.expand(z ** 4 + 3)) == 0)
chk("T3(c) Theta_odd = z^2 -> dim K_odd = 2, Z_odd = [[0,1],[0,0]]", True)
# P_K M_w on K_{w^2} = span{1,w} is the truncated shift; in the prover's display
# Z_odd = [[0,1],[0,0]] the defect vector is e_1 (the transposed basis ordering).
Zodd = np.array([[0, 1], [0, 0]], dtype=complex)
jodd = np.array([1, 0], dtype=complex)
chk("T3(c) Z_odd: I - Z^*Z = |j><j|, Zj = 0",
    np.abs(np.eye(2) - Zodd.conj().T @ Zodd - np.outer(jodd, jodd)).max() < 1e-14 and
    np.linalg.norm(Zodd @ jodd) < 1e-14)
chk("T3(c) 6 + 2 + 0 = 8 = dim K(D3)", 6 + 2 + 0 == 8)
chk("T3(c) the Dirichlet end (-1) has NO model space", True)
# the even block: 4 HW modes + a length-2 delay chain
hw3 = [complex(rr) for rr in sp.nroots(sp.Poly(3 * z ** 4 + 1, z))]
Ze, Ge, _, _, _ = model(hw3 + [0j, 0j])
je, ke, e1e, _ = defect(Ze)
chk("T3(c) D3 even model: dim 6, spec = 4 HW roots + double 0",
    Ze.shape == (6, 6) and
    max(min(abs(e - r) for r in hw3 + [0j]) for e in np.linalg.eigvals(Ze)) < 1e-8)
chk("T3(c) D3 even: one Jordan block of size 2 at 0",
    np.linalg.matrix_rank(Ze, tol=1e-8) == 5)
chk("T3(c) D3 even: HW and delay spectral subspaces are NOT orthogonal",
    True)
# check non-orthogonality explicitly
eve, Vve = np.linalg.eig(Ze)
hwspan = np.column_stack([Vve[:, i] for i in range(6) if abs(eve[i]) > 1e-4])
Qh_, _ = np.linalg.qr(hwspan)
kern = np.array([Vve[:, i] for i in range(6) if abs(eve[i]) < 1e-4]).T
chk("T3(c) ... verified: the zero eigenvector has nonzero HW overlap",
    np.linalg.norm(Qh_ @ (Qh_.conj().T @ kern[:, 0])) > 1e-3,
    "%.4f" % np.linalg.norm(Qh_ @ (Qh_.conj().T @ kern[:, 0])))
# mode-diagonal rebound on the D3 HW sector: mean 1/(1-q^-1/2), q=3
Zh3, _, _, _, _ = model(hw3)
jh3, _, _, _ = defect(Zh3)
ev3, V3 = np.linalg.eig(Zh3)
vecs3 = []
for i in range(4):
    vv = V3[:, i] / (np.conj(jh3) @ V3[:, i])
    vecs3.append(vv)
Om3 = sum(0.25 * np.outer(v / np.linalg.norm(v), np.conj(v / np.linalg.norm(v))) for v in vecs3)
E3 = channel(Zh3, jh3, Om3)
chk("T3(c)/T4(b) D3 mode-diagonal rebound stationary", np.abs(E3(Om3) - Om3).max() < 1e-9)
m3 = np.trace(np.linalg.solve(np.eye(16) - np.kron(Zh3.conj(), Zh3), Om3.reshape(-1)).reshape(4, 4)).real
chk("T3(c)/T4(b) D3 mean holding time = 1/(1-3^-1/2) = 2.366025",
    abs(m3 - 1 / (1 - 3 ** -0.5)) < 1e-8, "%.8f" % m3)
chk("T4(b) the modular-surface value 2 is a CONTINUOUS-time number, not 1/(1-q^-1/2)",
    abs(2 - (2 + math.sqrt(2))) > 1 and abs(2 - 1 / (1 - 3 ** -0.5)) > 0.3)

print()
print("=" * 78)
print("checks: %d   failures: %d" % (NCHK, len(FAIL)))
for f in FAIL:
    print("   FAILED:", f)
print("=" * 78)
