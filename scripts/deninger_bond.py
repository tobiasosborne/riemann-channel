#!/usr/bin/env python3
"""Numerics lane for notes/deninger-bond (Deninger's package on the GL_1 bond), 2026-09-22.

Independent checks of the displayed formulas of notes/deninger-bond/astra-proofs.md, Sections 2, 3, 4, 5, 7, 8.
Written without reading the author's own check scripts.  Conventions (Section 0 of the proofs): X = log y, bond
L^2(R, dX), inner products linear in the first slot; for rho = sigma + i gamma the mode m_rho(X) = e^{lambda X} 1_{X>0}
with lambda = (conj(rho) - 1)/2, C_t f(X) = f(X + t) (adjoint compression), C_t m_rho = e^{t lambda} m_rho.
Run from the repo root:  python3 scripts/deninger_bond.py  (writes nothing but stdout; ~1 min).
"""
import time, cmath, math
import numpy as np
import mpmath as mp
from sympy import factorint

T0 = time.time()
mp.mp.dps = 40
LEDGER = []


def check(desc, ok, value=""):
    tag = f"D{len(LEDGER)+1:02d}"
    LEDGER.append((tag, bool(ok), desc, value))
    print(f"{tag} {'PASS' if ok else 'FAIL'} {desc} {value}")


# ------------------------------------------------------------------ zeros
zeros = np.load("data/zeros3000.npy")
assert zeros.shape[0] == 3000
g3 = [mp.im(mp.zetazero(n)) for n in (1, 2, 3)]
check("first three ordinates from mpmath.zetazero vs data file", max(abs(float(g3[k]) - zeros[k]) for k in range(3)) < 1e-9,
      f"{[mp.nstr(g, 22) for g in g3]}")
check("data file: 3000 positive ordinates, last one", abs(zeros[-1] - 3533.3282433958198) < 1e-9, f"{zeros[-1]!r}")

# ------------------------------------------------------------------ 8.1 six modes at t = 1
def dmode(gamma, t=1.0):
    # C_t m_rho = e^{t lambda} m_rho, lambda = -1/4 - i gamma/2  (rho = 1/2 + i gamma)
    return cmath.exp(t * (-0.25 - 0.5j * gamma))

d = [dmode(float(g)) for g in g3]
d_expected = [0.551367248054149711 - 0.550022560888030452j, -0.362776434403421347 + 0.689147239967028782j,
              0.777355034172435742 + 0.047432167981283365j]
check("d_n = e^{-1/4 - i gamma_n/2} at t = 1 against the table (8.1)", max(abs(d[k] - d_expected[k]) for k in range(3)) < 1e-15,
      f"{[complex(round(x.real, 15), round(x.imag, 15)) for x in d]}")
D = np.diag([d[0], d[0].conjugate(), d[1], d[1].conjugate(), d[2], d[2].conjugate()])
blk = np.array([[0, -1j], [1j, 0]])
Om = np.kron(np.eye(3), blk)
G = np.eye(6)
J = np.diag([-1j, 1j] * 3)
Rc = np.kron(np.eye(3), np.array([[0, 1], [1, 0]]))
q1 = math.exp(-0.5)
check("D^T Omega D = e^{-1/2} Omega on the six modes", np.abs(D.T @ Om @ D - q1 * Om).max() < 1e-15, f"maxerr={np.abs(D.T @ Om @ D - q1 * Om).max():.2e}")
check("D^T G conj(D) = e^{-1/2} G with G = I (first-slot-linear Hermitian convention)", np.abs(D.T @ G @ D.conj() - q1 * G).max() < 1e-15)
check("Omega J R_c = I_6", np.abs(Om @ J @ Rc - np.eye(6)).max() == 0)
check("|d_n| = e^{-1/4} for all six modes", max(abs(abs(x) - math.exp(-0.25)) for x in np.diag(D)) < 1e-15, f"e^-1/4={math.exp(-0.25):.18f}")

# energy metric (8.2): M_ab = <m_{s_a}, m_{s_b}> = 2/(1 + i(s_a - s_b)), s = signed ordinate; check by quadrature and non-similitude
s6 = [float(g3[0]), -float(g3[0]), float(g3[1]), -float(g3[1]), float(g3[2]), -float(g3[2])]
M = np.array([[2 / (1 + 1j * (sa - sb)) for sb in s6] for sa in s6])
lam = [-0.25 - 0.5j * s for s in s6]
Mq = np.array([[complex(mp.quad(lambda X: mp.exp((la + mp.conj(lb)) * X), mp.linspace(0, 120, 241))) for lb in lam] for la in lam])   # tail beyond 120 is e^{-60}
check("energy Gram (8.2) M_ab = 2/(1+i(s_a-s_b)) equals the direct integral of the modes", np.abs(M - Mq).max() < 1e-12, f"maxerr={np.abs(M-Mq).max():.1e}")
res = np.abs(D.T @ M @ D.conj() - q1 * M)
check("energy Gram is NOT a q_t-similitude: off-diagonal residual of D^T M conj(D) - e^{-1/2} M", res.max() > 0.1, f"max residual={res.max():.4f}, diagonal residual={np.abs(np.diag(res)).max():.1e}")

# ------------------------------------------------------------------ 2.2 jets: the anti-diagonal pairing (2.1) at a synthetic off-line partner pair
def Ct_block(lam_, m, t):
    # (0.1): C_t e_{rho,j} = e^{t lambda} sum_{r<=j} t^{j-r}/(j-r)! e_{rho,r}; matrix acts on coefficient columns
    B = np.zeros((m, m), dtype=complex)
    for j in range(m):
        for r in range(j + 1):
            B[r, j] = cmath.exp(t * lam_) * t ** (j - r) / math.factorial(j - r)
    return B

def pairing_block(gamma, m):
    # Omega(e_{rho,j}, e_{nu,k}) = (-i sgn gamma)^m (-1)^j for j + k = m - 1, nu = 1 - rho
    B = np.zeros((m, m), dtype=complex)
    c = (-1j * np.sign(gamma)) ** m
    for j in range(m):
        B[j, m - 1 - j] = c * (-1) ** j
    return B

worst = 0.0
for m in (1, 2, 3, 4):
    rho = 0.7 + 3.1j                      # synthetic off-line zero; partner nu = 1 - rho
    lr = (rho.conjugate() - 1) / 2
    ln = ((1 - rho).conjugate() - 1) / 2
    assert abs(lr + ln + 0.5) < 1e-15
    B = pairing_block(rho.imag, m)        # block Omega(e_rho, e_nu)
    # full form on (rho-jets, nu-jets): [[0, B], [-B^T, 0]] (alternating)
    Ofull = np.block([[np.zeros((m, m)), B], [-B.T, np.zeros((m, m))]])
    for t in (0.7, 1.0, 2.3):
        C = np.block([[Ct_block(lr, m, t), np.zeros((m, m))], [np.zeros((m, m)), Ct_block(ln, m, t)]])
        worst = max(worst, np.abs(C.T @ Ofull @ C - math.exp(-t / 2) * Ofull).max())
check("jet pairing (2.1) is an e^{-t/2}-similitude for chains of length 1..4 (synthetic partner pair rho, 1-rho)", worst < 1e-12, f"max residual={worst:.1e}")
# alternation with the sign rule: Omega(e_nu,k, e_rho,j) = -Omega(e_rho,j, e_nu,k) when both computed from (2.1) directly
alt_ok = True
for m in (1, 2, 3, 4):
    Brho = pairing_block(3.1, m)          # rho has gamma = +3.1
    Bnu = pairing_block(-3.1, m)          # nu = 1 - rho has gamma = -3.1; Omega(e_nu,k, e_rho,j) = (-i sgn(-3.1))^m (-1)^k
    alt_ok &= np.abs(Bnu - (-Brho.T)).max() < 1e-15
check("(2.1) applied to both orderings is alternating: Omega(e_nu,k, e_rho,j) = -Omega(e_rho,j, e_nu,k)", alt_ok)
# reality: conjugating rho conjugates the coefficient
c_rho = [(-1j * 1) ** m for m in (1, 2, 3, 4)]
c_conj = [(-1j * -1) ** m for m in (1, 2, 3, 4)]   # conj(rho) has gamma -> -gamma
check("reality: coefficient at conj(rho) is the conjugate of the coefficient at rho, m = 1..4", all(abs(c_conj[k] - c_rho[k].conjugate()) < 1e-15 for k in range(4)))

# ------------------------------------------------------------------ 3.1 positive metric criterion on modes; Jordan violation
def sim_solutions(Cs, q_of_t, ts, n):
    """Real dimension of the space of Hermitian G with C_t^* G C_t = q_t G for the listed times (columns = vec(G))."""
    rows = []
    for t in ts:
        C = Cs(t)
        q = q_of_t(t)
        # linear map G -> C^* G C - q G on Hermitian matrices, parametrised by real coordinates
        basis = []
        for i in range(n):
            E = np.zeros((n, n), dtype=complex); E[i, i] = 1; basis.append(E)
        for i in range(n):
            for j in range(i + 1, n):
                E = np.zeros((n, n), dtype=complex); E[i, j] = 1; E[j, i] = 1; basis.append(E)
                E = np.zeros((n, n), dtype=complex); E[i, j] = 1j; E[j, i] = -1j; basis.append(E)
        cols = [(C.conj().T @ E @ C - q * E).reshape(-1) for E in basis]
        A = np.array(cols).T
        rows.append(np.vstack([A.real, A.imag]))
    A = np.vstack(rows)
    return n * n - np.linalg.matrix_rank(A, tol=1e-10), basis, A

# (a) six critical simple modes: solution space = 6 real diagonal weights (three pairs, no reality imposed here)
dimA, _, _ = sim_solutions(lambda t: np.diag([dmode(s, t) for s in s6]), lambda t: math.exp(-t / 2), (0.5, 1.0, 1.7, 2.9), 6)
check("all-time invariant Hermitian forms on six simple critical modes: real dimension 6 (one weight per mode)", dimA == 6, f"dim={dimA}")
# (b) an off-line zero rho = 0.7 + 3.1i: the Hermitian similitude pairs rho only with 1 - conj(rho) = 0.3 + 3.1i (3.2);
#     on the four-element set {rho, 1-rho, conj(rho), 1-conj(rho)} the invariant forms have zero diagonal, so none is positive
four = [complex(0.7, 3.1), complex(0.3, -3.1), complex(0.7, -3.1), complex(0.3, 3.1)]
lam4 = [(z.conjugate() - 1) / 2 for z in four]
dimB, basisB, AB = sim_solutions(lambda t: np.diag([cmath.exp(t * l) for l in lam4]), lambda t: math.exp(-t / 2), (0.5, 1.0, 1.7, 2.9), 4)
u_, sv, vh = np.linalg.svd(AB)
null = vh[np.sum(sv > 1e-10):]
diag_forced_zero = all(np.abs(v[:4]).max() < 1e-9 for v in null)            # first four coordinates = diagonal weights
check("off-line quartet {rho,1-rho,conj rho,1-conj rho}, rho=0.7+3.1i: invariant Hermitian forms have zero diagonal (no positive metric), pairing rho with 1-conj(rho)",
      dimB == 4 and diag_forced_zero, f"dim={dimB} (two complex off-diagonal entries)")
# (c) a double critical zero (Jordan chain of length 2): the eigenvector's diagonal entry is forced to zero, so no positive form
dimC, basisC, AC = sim_solutions(lambda t: Ct_block(-0.25 - 0.5j * 3.1, 2, t), lambda t: math.exp(-t / 2), (0.5, 1.0, 1.7), 2)
u_, sv, vh = np.linalg.svd(AC)
nullC = vh[np.sum(sv > 1e-10):]
check("double critical zero (length-two jet chain): every invariant Hermitian form has G(e_0,e_0) = 0, hence none is positive definite",
      all(abs(v[0]) < 1e-9 for v in nullC) and dimC >= 1, f"dim={dimC} (G_11 free, G_01 imaginary, G_00 = 0)")
# growth of the rescaled jet norm: e^{t/2} ||C_t e_1||^2 has leading t^2 coefficient G(e_0,e_0) for diagonal G = I
tvals = np.array([10.0, 20.0, 40.0])
grow = [math.exp(t / 2) * np.linalg.norm(Ct_block(-0.25 - 0.5j * 3.1, 2, t)[:, 1]) ** 2 for t in tvals]
check("rescaled jet norm e^{t/2}||C_t e_1||^2 grows like t^2 (ratio at t=40 vs t=20 close to 4)", abs(grow[2] / grow[1] - 4) < 0.02, f"ratio={grow[2]/grow[1]:.4f}")

# ------------------------------------------------------------------ 3.3 the star, (3.5), and the construction (3.3)
# complex modes e_+, e_- (gamma > 0): Omega(e_+, e_-) = -i, J e_+ = -i e_+, J e_- = i e_-; real vectors u, v
Om2 = np.array([[0, -1j], [1j, 0]])
J2 = np.diag([-1j, 1j])
u = np.array([1, 1]) / math.sqrt(2)
v = 1j * np.array([1, -1]) / math.sqrt(2)
R2 = lambda x: np.array([x[1], x[0]]).conj()      # real structure exchanges e_+ and e_- with conjugation
GJ = lambda x, y: x @ Om2 @ (J2 @ R2(y))          # G_J(x, y) = Omega(x, J R y), bilinear Omega
check("(3.5): Omega(u,v) = -1, Ju = -v, Jv = u, G_J(u,u) = G_J(v,v) = 1, G_J(u,v) = 0",
      abs(u @ Om2 @ v + 1) < 1e-15 and np.abs(J2 @ u + v).max() < 1e-15 and np.abs(J2 @ v - u).max() < 1e-15
      and abs(GJ(u, u) - 1) < 1e-15 and abs(GJ(v, v) - 1) < 1e-15 and abs(GJ(u, v)) < 1e-15,
      f"Omega(u,v)={u @ Om2 @ v:.3f}, G_J(u,u)={GJ(u,u):.3f}, G_J(v,v)={GJ(v,v):.3f}")
check("u, v are real vectors (fixed by the real structure R)", np.abs(R2(u) - u).max() < 1e-15 and np.abs(R2(v) - v).max() < 1e-15)
# (3.3) in the real basis (u_1, v_1, u_2, v_2, u_3, v_3): Omega(u,v) = -1 -> Omega_real = kron(I, [[0,-1],[1,0]]); certificate G = diag weights
OmR = np.kron(np.eye(3), np.array([[0, -1], [1, 0]]))
w = np.array([1.0, 1.0, 2.5, 2.5, 0.3, 0.3])
GR = np.diag(w)
L = np.linalg.inv(GR) @ OmR
R = None
# -L^2 is G-selfadjoint positive; compute its positive square root via the G-orthonormal eigenbasis
S = np.diag(np.sqrt(w))
Ls = S @ L @ np.linalg.inv(S)                 # G-orthonormal coordinates: Ls is real skew
ev, V = np.linalg.eigh(-Ls @ Ls)
Rs = V @ np.diag(np.sqrt(ev)) @ V.T
R = np.linalg.inv(S) @ Rs @ S
Jc = -L @ np.linalg.inv(R)
ok33 = (np.abs(Jc @ Jc + np.eye(6)).max() < 1e-12 and np.abs(Jc.T @ OmR @ Jc - OmR).max() < 1e-12
        and np.all(np.linalg.eigvalsh((OmR @ Jc + (OmR @ Jc).T) / 2) > 0) and np.abs(OmR @ Jc - GR @ R).max() < 1e-12)
check("(3.3)-(3.4): J = -L R^{-1} from a weighted certificate G gives J^2 = -I, J^T Omega J = Omega, Omega J = G R > 0", ok33,
      f"Omega J = {np.round(OmR @ Jc, 6).tolist()[0]} ... (compatible metric is I regardless of the weights)")
check("compatible metric Omega J = I_6 for every positive certificate G (weights change R, not Omega J)", np.abs(OmR @ Jc - np.eye(6)).max() < 1e-12)

# ------------------------------------------------------------------ 4.2 unbounded rescaled semigroup: the two-mode estimate (4.4)
gaps = np.diff(zeros)
k = int(np.argmin(gaps))
ga, gb = zeros[k], zeros[k + 1]
a, ap = ga / 2, gb / 2
r = 0.5 / math.sqrt((a - ap) ** 2 + 0.25)
tstar = 2 * math.pi / (gb - ga)
# unit modes u_gamma = k_rho/sqrt2 in the X-picture: m_rho/||m_rho||, Gram entry r e^{i phi}
lam_a, lam_b = -0.25 - 0.5j * ga, -0.25 - 0.5j * gb
gram = np.array([[1, (1 / (-(lam_a + np.conj(lam_b)))) / 2], [(1 / (-(lam_b + np.conj(lam_a)))) / 2, 1]])
check("closest pair among 3000 zeros: |<u_gamma,u_delta>| = (1/2)/sqrt((a-a')^2+1/4) equals the Gram modulus", abs(abs(gram[0, 1]) - r) < 1e-12,
      f"gamma={ga:.6f}, delta={gb:.6f}, gap={gb-ga:.6f}, r={r:.6f}")
c = gram[0, 1].conjugate() / abs(gram[0, 1])     # <u, c v> = r  (first slot linear: <u, c v> = conj(c) <u,v>)
c = (gram[0, 1] / abs(gram[0, 1]))               # then <u, c v> = conj(c) g01 = |g01|
coef_f = np.array([1, -c]); coef_g = np.array([1, c])
nf = math.sqrt((coef_f.conj() @ gram.T @ coef_f).real) if False else None
# norm^2 of sum a_i u_i with Gram g_ij = <u_i, u_j> (first slot linear): sum a_i conj(a_j) g_ij
norm2 = lambda cf: (cf[:, None] * cf.conj()[None, :] * gram).sum().real
ratio = math.sqrt(norm2(coef_g) / norm2(coef_f))
Cts = np.diag([cmath.exp(tstar * lam_a), cmath.exp(tstar * lam_b)])
img = Cts @ coef_f
lhs = math.exp(tstar / 4) * math.sqrt(norm2(img) / norm2(coef_f))
check("(4.4): e^{t*/4}||C_{t*} f||/||f|| = sqrt((1+r)/(1-r)) for f = u - c v at t* = 2 pi/|gamma - delta|",
      abs(lhs - math.sqrt((1 + r) / (1 - r))) < 1e-9 and abs(ratio - math.sqrt((1 + r) / (1 - r))) < 1e-9, f"value={lhs:.6f}, t*={tstar:.3f}")
check("cluster overlap bound: |a - a'| <= 1 gives squared overlap >= 1/5", (0.25 / (1 + 0.25)) >= 0.2 - 1e-15, f"{0.25/1.25:.3f}")
bu = (np.array([1, 0]) - np.array([0, gram[0, 1].conjugate()])) / (1 - abs(gram[0, 1]) ** 2)   # b_u = (u - conj(<v,u>) v)/(1-r^2) ... check numerically instead
# numerically: b_u = x u + y v with <b_u, v> = 0, <b_u, u> = 1; solve
A2 = np.array([[gram[0, 0], gram[1, 0]], [gram[0, 1], gram[1, 1]]])   # <x u + y v, u> = x g00 + y g10 ; <., v> = x g01 + y g11
xy = np.linalg.solve(A2, np.array([1, 0]))
check("biorthogonal vector norm ||b_u|| = (1 - r^2)^{-1/2} for a unit pair with overlap r", abs(math.sqrt(norm2(xy)) - (1 - r ** 2) ** -0.5) < 1e-9,
      f"||b_u||={math.sqrt(norm2(xy)):.4f}")

# ------------------------------------------------------------------ 5.1-5.2 Weil form with the Gaussian test (8.2)-(8.3)
aW = mp.mpf(1) / 50
Ff = lambda s: mp.exp(aW * (s - mp.mpf(1) / 2) ** 2 / 4)
h0 = 1 / mp.sqrt(8 * mp.pi * aW)
hfun = lambda t: h0 * mp.exp(-t ** 2 / (8 * aW))
ffun = lambda t: mp.exp(-t ** 2 / (4 * aW)) / mp.sqrt(4 * mp.pi * aW)
# transforms by quadrature
check("F_f(s) = e^{a(s-1/2)^2/4} is the transform int f(t) e^{(s-1/2)t/2} dt (s = 0.3 + 0.8i)",
      abs(mp.quad(lambda t: ffun(t) * mp.exp((mp.mpc(0.3, 0.8) - 0.5) * t / 2), [-mp.inf, mp.inf]) - Ff(mp.mpc(0.3, 0.8))) < mp.mpf(10) ** -25)
hconv = lambda t: mp.quad(lambda u: ffun(u) * ffun(u - t), [-mp.inf, mp.inf])   # h = f * f~ with f real even: (f*f~)(t) = int f(u) f(u-t) du
check("h = f * f~ equals (8 pi a)^{-1/2} e^{-t^2/(8a)} at t = 0.37", abs(hconv(mp.mpf('0.37')) - hfun(mp.mpf('0.37'))) < mp.mpf(10) ** -25)
Fh = lambda s: Ff(s) * mp.conj(Ff(1 - mp.conj(s)))
check("F_h(s) = F_f(s) conj(F_f(1 - conj s)) equals the transform of h at s = 0.3 + 0.8i",
      abs(mp.quad(lambda t: hfun(t) * mp.exp((mp.mpc(0.3, 0.8) - 0.5) * t / 2), [-mp.inf, mp.inf]) - Fh(mp.mpc(0.3, 0.8))) < mp.mpf(10) ** -25)
W3000 = 2 * float(np.sum(np.exp(-float(aW) * zeros ** 2 / 2)))
W3000_mp = 2 * mp.fsum(mp.exp(-aW * mp.mpf(float(g)) ** 2 / 2) for g in zeros)
check("W_3000(f) = 2 sum e^{-a gamma^2/2} over the 3000 positive ordinates (8.3)", abs(W3000_mp - mp.mpf('0.2993960225075590798332207898')) < mp.mpf(10) ** -15,
      f"{mp.nstr(W3000_mp, 20)}")
tail_zero = 2 * sum(mp.exp(-aW * g ** 2 / 2) for g in [mp.mpf(3540)])
# analytic side (5.3)
even = Fh(0) + Fh(1)
logpi = -2 * mp.log(mp.pi) * hfun(0)
gam = mp.quad(lambda r_: Fh(mp.mpf(1) / 2 + 1j * r_) * mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * r_ / 2)), [-mp.inf, mp.inf]) / (2 * mp.pi)
prime = mp.mpf(0)
for n in range(2, 1001):
    f = factorint(n)
    if len(f) == 1:
        p = next(iter(f))
        prime += mp.log(p) / mp.sqrt(n) * (hfun(2 * mp.log(n)) + hfun(-2 * mp.log(n)))
prime = -2 * prime
total = even + logpi + gam + prime
check("(5.3) even terms F_h(0)+F_h(1) = 2 e^{a/8}", abs(even - 2 * mp.exp(aW / 8)) < mp.mpf(10) ** -30, mp.nstr(even, 20))
check("(5.3) -2 log(pi) h(0)", abs(logpi - mp.mpf('-3.2292233878602183844073696831')) < mp.mpf(10) ** -25, mp.nstr(logpi, 20))
check("(5.3) gamma integral", abs(gam - mp.mpf('1.5236299541478742837918519217')) < mp.mpf(10) ** -20, mp.nstr(gam, 20))
check("(5.3) prime powers n <= 1000", abs(prime - mp.mpf('-0.0000167989916869135445623098')) < mp.mpf(10) ** -25, mp.nstr(prime, 12))
check("explicit formula: analytic side (5.3) minus the zero sum over 3000 zeros", abs(total - W3000_mp) < mp.mpf(10) ** -14,
      f"total={mp.nstr(total, 20)}, difference={mp.nstr(total - W3000_mp, 5)}")
# Hermitian symmetry W(f,g) = conj W(g,f) with two Gaussians of different widths (under RH the sum is over rho with F_f(rho) conj F_g(rho))
Ff2 = lambda s, a_: mp.exp(a_ * (s - mp.mpf(1) / 2) ** 2 / 4)
Wfg = lambda a1, a2: mp.fsum(Ff2(mp.mpc(0.5, sg * g), a1) * mp.conj(Ff2(mp.mpc(0.5, sg * g), a2)) for g in zeros[:400] for sg in (1, -1))
check("W(f,g) = conj(W(g,f)) on 400 zero pairs for Gaussians a = 1/50, 1/80", abs(Wfg(mp.mpf(1) / 50, mp.mpf(1) / 80) - mp.conj(Wfg(mp.mpf(1) / 80, mp.mpf(1) / 50))) < mp.mpf(10) ** -30)

# ------------------------------------------------------------------ 7. CM torus and y^2 = x^3 - x
def count_Fp(p):
    sq = {}
    for y in range(p):
        sq[y * y % p] = sq.get(y * y % p, 0) + 1
    return 1 + sum(sq.get((x ** 3 - x) % p, 0) for x in range(p))

def count_Fp2(p):
    # F_{p^2} = F_p[t]/(t^2 - c), c a non-residue
    c = next(z for z in range(2, p) if pow(z, (p - 1) // 2, p) == p - 1)
    mul = lambda u, v: ((u[0] * v[0] + c * u[1] * v[1]) % p, (u[0] * v[1] + u[1] * v[0]) % p)
    sq = {}
    for a_ in range(p):
        for b_ in range(p):
            z = mul((a_, b_), (a_, b_))
            sq[z] = sq.get(z, 0) + 1
    total = 1
    for a_ in range(p):
        for b_ in range(p):
            x = (a_, b_)
            w = mul(mul(x, x), x)
            w = ((w[0] - x[0]) % p, (w[1] - x[1]) % p)
            total += sq.get(w, 0)
    return total

def primary(p):
    for a_ in range(-p, p + 1):
        for b_ in range(-p, p + 1):
            if a_ * a_ + b_ * b_ == p and a_ % 2 == 1 and b_ % 2 == 0 and (a_ + b_) % 4 == 1:
                yield complex(a_, b_)

table = {5: (-1 + 2j, -2, 8), 13: (3 + 2j, 6, 8), 17: (1 + 4j, 2, 16)}
for p, (pi_exp, tr_exp, N_exp) in table.items():
    prim = [z for z in primary(p)]
    pi_pos = [z for z in prim if z.imag > 0]
    check(f"p={p}: primary associates pi = 1 mod (1+i)^3 are a conjugate pair; the one with Im > 0 is {pi_exp}",
          len(prim) == 2 and abs(prim[0] - prim[1].conjugate()) < 1e-12 and len(pi_pos) == 1 and pi_pos[0] == pi_exp, f"{prim}")
    pi = pi_pos[0]
    N1 = count_Fp(p)
    N2 = count_Fp2(p)
    check(f"p={p}: #E(F_p) = P(1) = |pi-1|^2 = {N_exp} (trace {tr_exp}) by exhaustive count", N1 == N_exp and abs(abs(pi - 1) ** 2 - N1) < 1e-9 and round(2 * pi.real) == tr_exp, f"N1={N1}")
    check(f"p={p}: #E(F_p^2) = |pi^2-1|^2 = 1 + p^2 - pi^2 - conj(pi)^2 by exhaustive count over F_(p^2)", N2 == round(abs(pi ** 2 - 1) ** 2), f"N2={N2}, |pi^2-1|^2={abs(pi**2-1)**2:.0f}")
    A = np.array([[pi.real, -pi.imag], [pi.imag, pi.real]])
    OmT = np.array([[0, 1], [-1, 0]]); JT = np.array([[0, -1], [1, 0]])
    check(f"p={p}: A^T A = p I, A^T Omega_T A = p Omega_T, A J_T = J_T A, G_T = Omega_T J_T = I",
          np.abs(A.T @ A - p * np.eye(2)).max() == 0 and np.abs(A.T @ OmT @ A - p * OmT).max() == 0 and np.abs(A @ JT - JT @ A).max() == 0 and np.abs(OmT @ JT - np.eye(2)).max() == 0)
    # (7.2): Z(u) = exp(sum |pi^n - 1|^2 u^n / n) = (1 - pi u)(1 - conj(pi) u)/((1-u)(1-pu)) as power series to order 8
    fix = [round(abs(pi ** n - 1) ** 2) for n in range(1, 9)]
    detfix = [round(np.linalg.det(np.linalg.matrix_power(A, n) - np.eye(2))) for n in range(1, 9)]
    ser_lhs = [mp.mpf(0)] * 9
    # exp of sum: use mpmath taylor of log-series
    logs = [mp.mpf(0)] + [mp.mpf(fix[n - 1]) / n for n in range(1, 9)]
    # power series exponential
    e = [mp.mpf(1)] + [mp.mpf(0)] * 8
    for n in range(1, 9):
        e[n] = mp.fsum(k * logs[k] * e[n - k] for k in range(1, n + 1)) / n
    rhs = mp.taylor(lambda uu: (1 - pi * uu) * (1 - pi.conjugate() * uu) / ((1 - uu) * (1 - p * uu)), 0, 8)
    check(f"p={p}: (7.2) exp(sum #Fix(f^n) u^n/n) = (1-pi u)(1-conj(pi) u)/((1-u)(1-pu)) to order 8, #Fix = det(A^n - I)",
          fix == detfix and max(abs(e[n] - rhs[n]) for n in range(9)) < mp.mpf(10) ** -20, f"#Fix={fix[:4]}")

# (7.5): eigenbasis omega_+, omega_-: J_T omega_+ = -i omega_+, Omega_T(omega_+, omega_-) = -i, G_T = diag(1,1)
omp = np.array([1, 1j]) / math.sqrt(2)   # dz = dx + i dy on the (dx, dy) coefficient basis
omm = omp.conj()
OmT = np.array([[0, 1], [-1, 0]]); JT = np.array([[0, -1], [1, 0]])
check("(7.5): J_T omega_+ = -i omega_+, J_T omega_- = i omega_-, Omega_T(omega_+, omega_-) = -i, G_T(omega_+, omega_+) = G_T(omega_-, omega_-) = 1, cross term 0",
      np.abs(JT @ omp + 1j * omp).max() < 1e-15 and np.abs(JT @ omm - 1j * omm).max() < 1e-15 and abs(omp @ OmT @ omm + 1j) < 1e-15
      and abs(omp @ OmT @ (JT @ omp.conj()) - 1) < 1e-15 and abs(omm @ OmT @ (JT @ omm.conj()) - 1) < 1e-15 and abs(omp @ OmT @ (JT @ omm.conj())) < 1e-15)
A5 = np.array([[-1, -2], [2, -1]])   # pi = -1 + 2i
check("(7.5): pullback A^T (p = 5) has omega_+ , omega_- as eigenvectors with eigenvalues pi, conj(pi) (up to the stated transpose convention)",
      (np.abs(A5.T @ omp - (-1 + 2j) * omp).max() < 1e-15) or (np.abs(A5 @ omp - (-1 + 2j) * omp).max() < 1e-15),
      f"A omega_+ = {np.round(A5 @ omp, 6).tolist()}, A^T omega_+ = {np.round(A5.T @ omp, 6).tolist()}")

# ------------------------------------------------------------------ summary
npass = sum(1 for x in LEDGER if x[1]); nfail = len(LEDGER) - npass
print(f"\n{len(LEDGER)} checks, {npass} pass, {nfail} fail; runtime {time.time() - T0:.1f} s")
