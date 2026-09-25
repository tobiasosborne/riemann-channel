#!/usr/bin/env python3
"""Numerics lane for notes/deninger-cusp (independent of astra's checks/).

Tests the displayed formulas of notes/deninger-cusp/astra-proofs.md:
  D3  prime-level scattering matrices (D3.5)-(D3.13), functional equation, determinant, residues;
  D4  twisted Siegel theta constant terms (D4.1)-(D4.7), Poisson (D4.6), the odd GL1 replacement (D4.8),
      the conjugation-correct inner symbol Theta_chi (D4.9)-(D4.12);
  D5  the quadratic conductor-5 modes (N.3)-(N.4), the kernel transform, C_t action;
  N5  the Eisenstein T_2, T_3 spectra for Gamma_1(11), (N.5)-(N.6).
mpmath at 25 digits for L-functions; numpy double precision for the 2-d lattice sums.
Ledger lines: D<nn> PASS/FAIL <description> <value>.
"""
import time, sys
import numpy as np
import mpmath as mp

mp.mp.dps = 25
T0 = time.time()
LEDGER = []


def check(desc, ok, val=""):
    LEDGER.append((desc, bool(ok), str(val)))
    print(f"D{len(LEDGER):02d} {'PASS' if ok else 'FAIL'} {desc} {val}")


def close(a, b, tol):
    return abs(mp.mpmathify(a) - mp.mpmathify(b)) <= tol


# ---------------------------------------------------------------- Dirichlet characters mod prime q
class Char:
    """chi(g^j) = exp(2 pi i k j/(q-1)), g a generator mod q (astra's chi_{q,k})."""

    def __init__(self, q, k, g):
        self.q, self.k, self.g = q, k, g
        self.vals = [mp.mpc(0)] * q
        x = 1
        for j in range(q - 1):
            self.vals[x] = mp.exp(2j * mp.pi * k * j / (q - 1)) if k % (q - 1) else mp.mpc(1)
            x = (x * g) % q
        self.even = abs(self.vals[q - 1] - 1) < mp.mpf(10) ** -20
        self.principal = (k % (q - 1) == 0)

    def __call__(self, n):
        return self.vals[n % self.q]

    def conj(self):
        return Char(self.q, (-self.k) % (self.q - 1), self.g)

    def gauss(self):
        q = self.q
        return mp.fsum(self(r) * mp.exp(2j * mp.pi * r / q) for r in range(1, q))

    def L(self, s):
        """L(s, chi) by Hurwitz zeta; at s = 1 by the cancelled digamma formula (N.2)."""
        q = self.q
        if self.principal:
            return mp.zeta(s) * (1 - mp.power(q, -s))
        if abs(s - 1) < mp.mpf(10) ** -18:
            return -mp.fsum(self(r) * mp.digamma(mp.mpf(r) / q) for r in range(1, q)) / q
        return mp.power(q, -s) * mp.fsum(self(r) * mp.zeta(s, mp.mpf(r) / q) for r in range(1, q))

    def Lambda(self, s):
        """Completed L-function, parity a = 0 (even) or 1 (odd)."""
        a = 0 if self.even else 1
        if self.principal:
            return mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)
        return mp.power(mp.mpf(self.q) / mp.pi, (s + a) / 2) * mp.gamma((s + a) / 2) * self.L(s)

    def eps(self):
        a = 0 if self.even else 1
        return self.gauss() / (mp.mpc(0, 1) ** a * mp.sqrt(self.q))


chi5 = Char(5, 2, 2)      # (./5), even quadratic
chi7 = Char(7, 2, 3)      # even, order 3
chi13 = Char(13, 2, 2)    # even, order 6
chi5odd = Char(5, 1, 2)   # odd, order 4
triv5 = Char(5, 0, 2)

print("=== sanity: characters ===")
check("chi_{5,2} is the Legendre symbol mod 5", all(abs(chi5(n) - mp.mpf([0, 1, -1, -1, 1][n])) < 1e-20 for n in range(1, 5)))
check("chi_{7,2} even of order 3", chi7.even and abs(chi7(3) ** 3 - 1) < 1e-20 and abs(chi7(3) - 1) > 0.5)
check("chi_{13,2} even of order 6", chi13.even and abs(chi13(2) ** 6 - 1) < 1e-20 and abs(chi13(2) ** 3 + 1) < 1e-20)
check("chi_{5,1} odd, chi(2) = i", (not chi5odd.even) and abs(chi5odd(2) - 1j) < 1e-20)
# Dirichlet functional equation Lambda_chi(s) = eps_chi Lambda_barchi(1-s) at a test point
s0 = mp.mpc("0.7", "0.3")
for ch, name in [(chi5, "chi_{5,2}"), (chi7, "chi_{7,2}"), (chi13, "chi_{13,2}"), (chi5odd, "chi_{5,1}")]:
    lhs = ch.Lambda(s0); rhs = ch.eps() * ch.conj().Lambda(1 - s0)
    check(f"Dirichlet FE Lambda_chi(s) = eps Lambda_barchi(1-s), {name}", close(lhs, rhs, 1e-20), mp.nstr(abs(lhs - rhs), 3))
check("root numbers eps: chi5 = 1", close(chi5.eps(), 1, 1e-20), mp.nstr(chi5.eps(), 12))
check("root number chi7 = 0.895953219663-0.444148430342i", close(chi7.eps(), mp.mpc("0.895953219663", "-0.444148430342"), 1e-11), mp.nstr(chi7.eps(), 13))
check("root number chi13 = 0.859542535099+0.511064213535i", close(chi13.eps(), mp.mpc("0.859542535099", "0.511064213535"), 1e-11), mp.nstr(chi13.eps(), 13))

# ---------------------------------------------------------------- D3: scattering matrices
print("=== D3: prime-level scattering ===")


def R_psi(ch, s):
    return ch.Lambda(2 * s - 1) / ch.Lambda(2 * s)


def A_psi(ch, s):                      # (D3.5)
    q = ch.q
    return mp.power(q, -s) * mp.sqrt(mp.pi) * mp.gamma(s - mp.mpf(1) / 2) / mp.gamma(s) * ch.L(2 * s - 1) / ch.L(2 * s)


def A_psi_gauss(ch, s):                # (D3.7)
    q = ch.q
    return mp.power(q, mp.mpf(1) / 2 - s) * ch.gauss() / mp.sqrt(q) * ch.conj().Lambda(2 - 2 * s) / ch.Lambda(2 * s)


def A_psi_R(ch, s):                    # (D3.5) first form q^(1/2-s) R_psi(s); equals A_psi for even psi
    return mp.power(ch.q, mp.mpf(1) / 2 - s) * R_psi(ch, s)


def Phi_psi(ch, s):                    # (D3.6); the R-form so that the odd diagnostic (N.1) is well defined
    return mp.matrix([[0, A_psi_R(ch, s)], [A_psi_R(ch.conj(), s), 0]])


def phi0(s):                           # Lambda_0(2s-1)/Lambda_0(2s)
    return mp.sqrt(mp.pi) * mp.gamma(s - mp.mpf(1) / 2) * mp.zeta(2 * s - 1) / (mp.gamma(s) * mp.zeta(2 * s))


def Phi_triv(q, s):                    # (D3.11)
    qs, q1s = mp.power(q, s), mp.power(q, 1 - s)
    return phi0(s) / (mp.power(q, 2 * s) - 1) * mp.matrix([[q - 1, qs - q1s], [qs - q1s, q - 1]])


table = {
    ("chi5", "0.7+0.3i"): (mp.mpc("0.570396241478", "-0.370987747919"), mp.mpc("0.570396241478", "-0.370987747919")),
    ("chi5", "1.2+0.4i"): (mp.mpc("0.188174397267", "-0.180015889034"), mp.mpc("0.188174397267", "-0.180015889034")),
    ("chi7", "0.7+0.3i"): (mp.mpc("0.435438660235", "-0.438482464585"), mp.mpc("0.499568861119", "-0.371294296554")),
    ("chi7", "1.2+0.4i"): (mp.mpc("0.100947189666", "-0.156910809998"), mp.mpc("0.123084043639", "-0.147015786831")),
    ("chi13", "0.7+0.3i"): (mp.mpc("0.336061944278", "-0.402833597027"), mp.mpc("0.251844978419", "-0.453521926397")),
    ("chi13", "1.2+0.4i"): (mp.mpc("0.040521235773", "-0.098440230048"), mp.mpc("0.024339946416", "-0.099396432859")),
}
spts = {"0.7+0.3i": mp.mpc("0.7", "0.3"), "1.2+0.4i": mp.mpc("1.2", "0.4")}
chars = {"chi5": chi5, "chi7": chi7, "chi13": chi13}
I2 = mp.eye(2)
for (cn, sn), (a_ref, b_ref) in table.items():
    ch, s = chars[cn], spts[sn]
    P = Phi_psi(ch, s)
    check(f"(D3.6) table entry a, {cn}, s={sn}", close(P[0, 1], a_ref, 2e-12), mp.nstr(P[0, 1], 13))
    check(f"(D3.6) table entry b, {cn}, s={sn}", close(P[1, 0], b_ref, 2e-12), mp.nstr(P[1, 0], 13))
    check(f"(D3.7) Gauss-sum form = (D3.5), {cn}, s={sn}", close(A_psi_gauss(ch, s), P[0, 1], 1e-20), mp.nstr(abs(A_psi_gauss(ch, s) - P[0, 1]), 3))
    check(f"(D3.5) both forms of A_psi agree for even psi, {cn}, s={sn}", close(A_psi(ch, s), P[0, 1], 1e-20))
    prod = P * Phi_psi(ch, 1 - s)
    check(f"(D3.9) Phi_psi(s)Phi_psi(1-s) = I, {cn}, s={sn}", mp.norm(prod - I2) < 1e-20, mp.nstr(mp.norm(prod - I2), 3))
    detP = mp.det(P); det_ref = -mp.power(ch.q, 1 - 2 * s) * R_psi(ch, s) * R_psi(ch.conj(), s)
    check(f"(D3.6) det Phi_psi = -q^(1-2s) R_psi R_barpsi, {cn}, s={sn}", close(detP, det_ref, 1e-20))
# unitarity on the critical line
for cn, ch in chars.items():
    tau = mp.mpf("1.7"); P = Phi_psi(ch, mp.mpf(1) / 2 + 1j * tau)
    U = P * P.transpose_conj()
    check(f"Phi_psi unitary on Re s = 1/2 (tau = 1.7), {cn}", mp.norm(U - I2) < 1e-20, mp.nstr(mp.norm(U - I2), 3))
# residue at s = 1 of the nontrivial blocks is zero; off-diagonal finite value (D3.10)
for cn, ch, ref in [("chi5", chi5, mp.mpf("0.382936203162541402645")), ("chi7", chi7, mp.mpc("0.304559716357", "-0.020318397407")), ("chi13", chi13, mp.mpc("0.199607864326", "0.016349433840"))]:
    a1 = mp.pi / ch.q * ch.L(1) / ch.L(2)
    eps_ = mp.mpf(10) ** -10
    a1lim = A_psi(ch, 1 + eps_)
    check(f"(D3.10) A_psi(1) = pi/q L(1,psi)/L(2,psi), regular at s=1, {cn}", close(a1, a1lim, 1e-8) and close(a1, ref, 2e-12), mp.nstr(a1, 15))
# trivial block
triv_table = {"0.7+0.3i": (mp.mpc("-0.779956675205", "-0.082416806284"), mp.mpc("-0.207902204851", "-0.452750031374")),
              "1.2+0.4i": (mp.mpc("-0.118871445339", "-0.189987827354"), mp.mpc("0.070583992790", "-0.370524601121"))}
for sn, (d_ref, o_ref) in triv_table.items():
    s = spts[sn]; P = Phi_triv(5, s)
    check(f"(D3.11) trivial block d, q=5, s={sn}", close(P[0, 0], d_ref, 2e-12) and close(P[1, 1], d_ref, 2e-12), mp.nstr(P[0, 0], 13))
    check(f"(D3.11) trivial block o, q=5, s={sn}", close(P[0, 1], o_ref, 2e-12) and close(P[1, 0], o_ref, 2e-12), mp.nstr(P[0, 1], 13))
    prod = P * Phi_triv(5, 1 - s)
    check(f"(D3.11) Phi_1(s)Phi_1(1-s) = I, q=5, s={sn}", mp.norm(prod - I2) < 1e-20, mp.nstr(mp.norm(prod - I2), 3))
    det_ref = phi0(s) ** 2 * (1 - mp.power(5, 2 - 2 * s)) / (1 - mp.power(5, 2 * s))
    check(f"(D3.12) det Phi_1, q=5, s={sn}", close(mp.det(P), det_ref, 1e-20))
    # eigenvalues phi_pm on (1, +-1)
    pm = [phi0(s) * (1 + sg * mp.power(5, 1 - s)) / (1 + sg * mp.power(5, s)) for sg in (1, -1)]
    v = mp.matrix([1, 1]); w = mp.matrix([1, -1])
    check(f"(D3.12) phi_pm eigenvalues on (1,+-1), q=5, s={sn}", mp.norm(P * v - pm[0] * v) < 1e-20 and mp.norm(P * w - pm[1] * w) < 1e-20)
# residue (D3.13)
for q in (5, 7):
    e_ = mp.mpf(10) ** -12
    Rm = e_ * Phi_triv(q, 1 + e_)
    ref = 3 / (mp.pi * (q + 1))
    check(f"(D3.13) Res_(s=1) Phi_1 = 3/(pi(q+1)) all-ones, q={q}", all(close(Rm[i, j], ref, 1e-10) for i in range(2) for j in range(2)), mp.nstr(Rm[0, 0], 12))
check("(N3) q=5 trivial residue entry = 1/(2 pi)", close(3 / (mp.pi * 6), mp.mpf("0.159154943091895335769"), 1e-20))
check("Res_(s=1) phi = 3/pi", close(mp.mpf(10) ** -12 * phi0(1 + mp.mpf(10) ** -12), 3 / mp.pi, 1e-10))
# full Gamma_1(5) matrix in the cusp basis (two diamond orbits of size m=2, Fourier over G = {1,2})
G = [1, 2]
psis = [triv5, chi5]


def Phi_full_gamma1_5(s):
    M = mp.matrix(4, 4)
    blocks = {0: Phi_triv(5, s), 1: Phi_psi(chi5, s)}
    for a in range(2):
        for b in range(2):
            for gi, g in enumerate(G):
                for gj, g2 in enumerate(G):
                    M[2 * a + gi, 2 * b + gj] = mp.fsum(psis[k](g) * mp.conj(psis[k](g2)) * blocks[k][a, b] for k in range(2)) / 2
    return M


s = spts["0.7+0.3i"]
M4 = Phi_full_gamma1_5(s) * Phi_full_gamma1_5(1 - s)
check("Gamma_1(5) 4x4 cusp-basis matrix: Phi(s)Phi(1-s) = I", mp.norm(M4 - mp.eye(4)) < 1e-20, mp.nstr(mp.norm(M4 - mp.eye(4)), 3))
e_ = mp.mpf(10) ** -12
R4 = e_ * Phi_full_gamma1_5(1 + e_)
check("(N3) Gamma_1(5) residue entries all 1/(4 pi)", all(close(R4[i, j], 1 / (4 * mp.pi), 1e-10) for i in range(4) for j in range(4)), mp.nstr(R4[0, 0], 12))
sv = mp.svd_r(mp.matrix([[float(mp.re(R4[i, j])) for j in range(4)] for i in range(4)]), compute_uv=False)
check("(N3) Gamma_1(5) residue has rank one", sv[0] > 1e-3 and all(x < 1e-8 for x in sv[1:]), [mp.nstr(x, 4) for x in sv])
d16 = mp.det(Phi_full_gamma1_5(s))
d16_ref = phi0(s) ** 2 * (1 - mp.power(5, 2 - 2 * s)) / (1 - mp.power(5, 2 * s)) * (-1) ** (2 - 1) * mp.power(5, (1 - 2 * s) * (2 - 1)) * R_psi(chi5, s) ** 2
check("(D3.16) det Phi_Gamma_1(5) formula (m = 2)", close(d16, d16_ref, 1e-20), mp.nstr(abs(d16 - d16_ref), 3))
# odd character fed formally into (D3.6): B(s)B(1-s) = I holds algebraically (diagnostic, N.1)
Bo = Phi_psi(chi5odd, s); Bo2 = Bo * Phi_psi(chi5odd, 1 - s)
check("(N.1) formal odd-completion matrix B(0.7+0.3i) entries", close(Bo[0, 1], mp.mpc("0.584013007860", "-0.328765368425"), 2e-12) and close(Bo[1, 0], mp.mpc("0.509530467411", "-0.425768800372"), 2e-12), mp.nstr(Bo[0, 1], 13))
check("(N.1) formal B(s)B(1-s) = I (algebraic only; not weight-zero scattering)", mp.norm(Bo2 - I2) < 1e-20)
check("(N.1) odd eps = 0.850650808352+0.525731112119i", close(chi5odd.eps(), mp.mpc("0.850650808352", "0.525731112119"), 1e-11), mp.nstr(chi5odd.eps(), 13))

# ---------------------------------------------------------------- D4: twisted theta
print("=== D4: twisted theta edges ===")


def theta_chi_direct(ch, v, a=0, nmax=400):
    """theta_{chi,a}(v) = sum_n n^a chi(n) exp(-pi n^2 v/f), direct summation (mpmath)."""
    f = ch.q
    return mp.fsum((mp.mpf(n) ** a) * ch(n) * mp.exp(-mp.pi * n * n * v / f) + ((-1) ** a) * (mp.mpf(n) ** a) * ch(-n) * mp.exp(-mp.pi * n * n * v / f) for n in range(1, nmax + 1))


def theta_chi(ch, v, a=0):
    """Even/odd primitive twisted theta, with Poisson (D4.6)/(D4.8) for v < 1 (tested below)."""
    v = mp.mpf(v)
    if v >= 1:
        return theta_chi_direct(ch, v, a)
    return ch.eps() * mp.power(v, -a - mp.mpf(1) / 2) * theta_chi_direct(ch.conj(), 1 / v, a)


# Poisson (D4.6) / (D4.8) by direct summation on both sides
for ch, name, a in [(chi5, "chi5", 0), (chi7, "chi7", 0), (chi13, "chi13", 0), (chi5odd, "chi5odd", 1)]:
    for v in (mp.mpf("0.3"), mp.mpf("0.7") / mp.mpf("1.3"), mp.mpf("2.5")):
        lhs = theta_chi_direct(ch, v, a); rhs = ch.eps() * mp.power(v, -a - mp.mpf(1) / 2) * theta_chi_direct(ch.conj(), 1 / v, a)
        check(f"(D4.6)/(D4.8) Poisson theta_chi,a(v) = eps v^(-a-1/2) theta_barchi,a(1/v), {name}, v={mp.nstr(v,4)}", close(lhs, rhs, 1e-18), mp.nstr(abs(lhs - rhs), 3))
# odd unsigned theta vanishes identically
check("odd chi: unsigned theta_chi(v) = 0 exactly", abs(theta_chi_direct(chi5odd, mp.mpf("0.5"), 0)) < 1e-22)
val = theta_chi_direct(chi5odd, mp.mpf("0.7") / mp.mpf("1.3"), 1)
check("(N2) odd GL1 theta_{chi_{5,1},1}(0.7/1.3) = 1.390329535856+0.747945730562i", close(val, mp.mpc("1.390329535856", "0.747945730562"), 2e-12), mp.nstr(val, 13))
# (D4.8) Mellin transform of the odd theta equals Lambda_chi(u)
u0 = mp.mpc("0.7", "0.3")
mel = mp.quad(lambda v: theta_chi(chi5odd, v, 1) * mp.power(v, (u0 + 1) / 2 - 1), [0, 1, mp.inf]) / 2
check("(D4.8) (1/2) int theta_{chi,1}(v) v^((u+1)/2) dv/v = Lambda_chi(u), odd chi mod 5, u=0.7+0.3i", close(mel, chi5odd.Lambda(u0), 1e-15), mp.nstr(abs(mel - chi5odd.Lambda(u0)), 3))

# table values at y = 1.3, t = 0.7 (D4.3)/(D4.5)
y, t = mp.mpf("1.3"), mp.mpf("0.7")
tabD4 = {"chi5": (mp.mpf("0.822880294170"), mp.mpf("0.156238589167"), mp.mpf("1.246242825365")),
         "chi7": (mp.mpc("1.053699131048", "-0.429880215401"), mp.mpc("0.156253315445", "-0.000025506630"), mp.mpc("1.509098455595", "-0.397658610120")),
         "chi13": (mp.mpc("1.848617210324", "0.689306227046"), mp.mpc("0.156282767983", "0.000025506630"), mp.mpc("2.513603987405", "0.722293789760"))}
for cn, (A_ref, C_ref, B_ref) in tabD4.items():
    ch = chars[cn]; f = ch.q
    A = theta_chi_direct(ch, t / y); C = mp.sqrt(y / t) * theta_chi_direct(ch, f * t * y); B = mp.sqrt(y / t) * theta_chi_direct(ch, t * y)
    check(f"(N2) A_chi = theta_chi(t/y), {cn}", close(A, A_ref, 2e-12), mp.nstr(A, 13))
    check(f"(N2) C_chi = sqrt(y/t) theta_chi(f t y), {cn}", close(C, C_ref, 2e-12), mp.nstr(C, 13))
    check(f"(N2) B_chi = sqrt(y/t) theta_chi(t y), {cn}", close(B, B_ref, 2e-12), mp.nstr(B, 13))
    # weighted involution (D4.6): W A_chi = eps B_barchi at the same (t, y): W F(t) = t^{-1} F(1/t)
    WA = (1 / t) * theta_chi_direct(ch, (1 / t) / y)
    Bbar = mp.sqrt(y / t) * theta_chi_direct(ch.conj(), t * y)
    check(f"(D4.6) W A_chi = eps_chi B_barchi at (t,y), {cn}", close(WA, ch.eps() * Bbar, 1e-18), mp.nstr(abs(WA - ch.eps() * Bbar), 3))


# direct 2-d lattice sums (numpy double) and x-averages, (D4.1), (D4.3)
def lattice_T(chvals, f, x, yy, tt, M=14, N=260):
    """T_chi(z,t) = sum_{m,n} chi(n) exp(-pi t |f m z + n|^2/(f y)), double precision."""
    m = np.arange(-M, M + 1)[:, None]
    n = np.arange(-N, N + 1)[None, :]
    chi_n = chvals[np.mod(n, f)]
    re = f * m * x + n
    im = f * m * yy
    return np.sum(chi_n * np.exp(-np.pi * tt * (re ** 2 + im ** 2) / (f * yy)))


for cn in ("chi5", "chi7", "chi13"):
    ch = chars[cn]; f = ch.q
    chvals = np.array([complex(ch(n)) for n in range(f)])
    K = 96
    xs = (np.arange(K) + 0.5) / K
    yf, tf = float(y), float(t)
    # cusp infinity
    avg_inf = np.mean([lattice_T(chvals, f, xx, yf, tf) for xx in xs])
    ref_inf = complex(theta_chi_direct(ch, t / y))
    check(f"(D4.3) int_0^1 T_chi(x+iy,t) dx = theta_chi(t/y), direct lattice sum, {cn}", abs(avg_inf - ref_inf) < 1e-12, f"{abs(avg_inf - ref_inf):.2e}")
    # cusp zero: z -> W_f z = -1/(f z)
    vals = []
    for xx in xs:
        z = xx + 1j * yf; w = -1 / (f * z)
        vals.append(lattice_T(chvals, f, w.real, w.imag, tf, M=16, N=400))
    avg_0 = np.mean(vals)
    ref_0 = complex(mp.sqrt(y / t) * theta_chi_direct(ch, f * t * y))
    check(f"(D4.3) int_0^1 T_chi(W_f(x+iy),t) dx = sqrt(y/t) theta_chi(f t y), direct lattice sum, {cn}", abs(avg_0 - ref_0) < 1e-11, f"{abs(avg_0 - ref_0):.2e}")
    # periodicity and the m=0 term
    d = abs(lattice_T(chvals, f, 0.37, yf, tf) - lattice_T(chvals, f, 1.37, yf, tf))
    check(f"(D4.1) T_chi periodic in x with period one, {cn}", d < 1e-13, f"{d:.1e}")
# odd character: unsigned lattice sum vanishes
chvals = np.array([complex(chi5odd(n)) for n in range(5)])
check("(D4.2) odd chi: T_chi(z,t) = 0 identically (unsigned lattice sum)", abs(lattice_T(chvals, 5, 0.31, 1.3, 0.7)) < 1e-14)

# Mellin edges (D4.7) and (D4.4)/(D3.5) quotient
for cn in ("chi5", "chi7"):
    ch = chars[cn]; f = ch.q
    s = spts["0.7+0.3i"]
    inc = mp.quad(lambda tt: theta_chi(ch, tt / y) * mp.power(tt, s - 1), [0, 1, mp.inf]) / 2
    check(f"(D4.7) (1/2) int A_chi(t;y) t^s dt/t = Lambda_chi(2s) y^s, {cn}", close(inc, ch.Lambda(2 * s) * mp.power(y, s), 1e-14), mp.nstr(abs(inc - ch.Lambda(2 * s) * mp.power(y, s)), 3))
    outB = mp.quad(lambda tt: mp.sqrt(y / tt) * theta_chi(ch, tt * y) * mp.power(tt, s - 1), [0, 1, mp.inf]) / 2
    check(f"(D4.7) (1/2) int B_chi(t;y) t^s dt/t = Lambda_chi(2s-1) y^(1-s), {cn}", close(outB, ch.Lambda(2 * s - 1) * mp.power(y, 1 - s), 1e-14))
    outC = mp.quad(lambda tt: mp.sqrt(y / tt) * theta_chi(ch, f * tt * y) * mp.power(tt, s - 1), [0, 1, mp.inf]) / 2
    ref = mp.power(f, mp.mpf(1) / 2 - s) * ch.Lambda(2 * s - 1) * mp.power(y, 1 - s)
    check(f"(D4.4) physical edge (1/2) int C_chi t^s dt/t = f^(1/2-s) Lambda_chi(2s-1) y^(1-s), {cn}", close(outC, ref, 1e-14))
    check(f"(D4.4) edge quotient (physical/incoming) y^(2s-1) = A_chi(s) of (D3.5), {cn}", close(outC / inc * mp.power(y, 2 * s - 1), A_psi(ch, s), 1e-13))
    # same-character outgoing rewritten: eps Lambda_barchi(2-2s) y^{1-s}
    check(f"(D4.7) Lambda_chi(2s-1) = eps_chi Lambda_barchi(2-2s), {cn}", close(ch.Lambda(2 * s - 1), ch.eps() * ch.conj().Lambda(2 - 2 * s), 1e-20))

# (D4.9)-(D4.12): the inner symbol
print("=== D4.3: inner symbol Theta_chi ===")


def Theta_chi(ch, tau):
    return ch.Lambda(1 + 2j * tau) / ch.conj().Lambda(1 - 2j * tau)


for cn in ("chi5", "chi7", "chi13"):
    ch = chars[cn]; f = ch.q
    devs = [abs(abs(Theta_chi(ch, mp.mpf(x))) - 1) for x in np.linspace(-6, 6, 13)]
    check(f"(D4.9) |Theta_chi| = 1 on the real line (13 points), {cn}", max(devs) < 1e-20, mp.nstr(max(devs), 3))
    ins = [abs(Theta_chi(ch, mp.mpc(x, yv))) for x in np.linspace(-5, 5, 6) for yv in (0.1, 0.5, 1.0, 2.0)]
    check(f"(D4.9) |Theta_chi| < 1 in the upper half-plane (24 grid points), {cn}", max(ins) < 1, mp.nstr(max(ins), 6))
    tau = mp.mpc("0.9", "0.35")
    check(f"(D4.10) Theta_chi = eps Lambda_chi(1+2i tau)/Lambda_chi(2i tau), {cn}", close(Theta_chi(ch, tau), ch.eps() * ch.Lambda(1 + 2j * tau) / ch.Lambda(2j * tau), 1e-18))
    tr = mp.mpf("1.3")
    lhs = A_psi(ch, mp.mpf(1) / 2 + 1j * tr); rhs = mp.power(f, -1j * tr) * ch.eps() / Theta_chi(ch, tr)
    check(f"(D4.10) A_chi(1/2+i tau) = f^(-i tau) eps Theta_chi^(-1), {cn}", close(lhs, rhs, 1e-18), mp.nstr(abs(lhs - rhs), 3))
    v = mp.mpf(40)
    ratio = Theta_chi(ch, 1j * v) / (ch.eps() * mp.sqrt(mp.pi / (f * v)))
    check(f"(D4.12) Theta_chi(iv)/(eps sqrt(pi/(f v))) -> 1 (v=40, within 2%), {cn}", abs(ratio - 1) < 0.02, mp.nstr(ratio, 8))
# the wrong conjugation placement is not unimodular for a complex character
wrong = [abs(abs(chi7.Lambda(1 + 2j * mp.mpf(x)) / chi7.Lambda(1 - 2j * mp.mpf(x))) - 1) for x in (0.5, 1.0, 2.0)]
check("(D4.3) Lambda_chi(1+2i tau)/Lambda_chi(1-2i tau) is NOT unimodular for chi7 (astra's warning)", max(wrong) > 1e-3, mp.nstr(max(wrong), 4))
# trivial character: Theta_1 = xi(1+2i tau)/xi(1-2i tau), r factor
xi = lambda s: s * (s - 1) / 2 * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)
tau = mp.mpf("0.8")
check("Theta_1 = xi(1+2i tau)/xi(1-2i tau) unimodular on R", close(abs(xi(1 + 2j * tau) / xi(1 - 2j * tau)), 1, 1e-20))

# ---------------------------------------------------------------- D5: quadratic conductor-5 modes
print("=== D5: modes of the (./5) channel ===")


def hardy5(tt):
    return mp.re(chi5.Lambda(mp.mpf(1) / 2 + 1j * tt))


imag_max = max(abs(mp.im(chi5.Lambda(mp.mpf(1) / 2 + 1j * mp.mpf(tt)))) for tt in (1.0, 3.3, 7.7))
check("Lambda_(./5)(1/2+it) is real (eps = 1)", imag_max < 1e-20, mp.nstr(imag_max, 3))
grid = [mp.mpf(k) / 10 for k in range(1, 121)]
vals = [hardy5(g) for g in grid]
roots = []
for i in range(len(grid) - 1):
    if vals[i] * vals[i + 1] < 0:
        roots.append(mp.findroot(hardy5, (grid[i], grid[i + 1]), solver="bisect", tol=1e-40))
check("first two zero ordinates of L(s,(./5)) (scan to 12)", len(roots) >= 2, [mp.nstr(r, 22) for r in roots[:4]])
g1, g2 = roots[0], roots[1]
check("(N.3) gamma_1 = 6.648453344727714716123", close(g1, mp.mpf("6.648453344727714716123"), 1e-18), mp.nstr(g1, 22))
check("(N.3) gamma_2 = 9.831444432886669616348", close(g2, mp.mpf("9.831444432886669616348"), 1e-18), mp.nstr(g2, 22))
check("L(rho_j,(./5)) residuals", max(abs(chi5.L(mp.mpf(1) / 2 + 1j * g)) for g in (g1, g2)) < 1e-18)
for j, g in enumerate((g1, g2), 1):
    w = g / 2 + 1j / mp.mpf(4)
    check(f"(D4.11) Theta_(./5)(w_{j}) = 0 at w = gamma/2 + i/4", abs(Theta_chi(chi5, w)) < 1e-17, mp.nstr(abs(Theta_chi(chi5, w)), 3))
    m13 = mp.power(mp.mpf("1.3"), -mp.mpf(1) / 4 - 1j * g / 2)
    ref = [mp.mpc("0.602342616987", "-0.717106262048"), mp.mpc("0.259788594167", "-0.899759915560")][j - 1]
    check(f"(N.4) m_{j}(1.3) = y^(-1/4 - i gamma/2)", close(m13, ref, 2e-12), mp.nstr(m13, 13))
    # C_t m = e^{-t/4 - i t gamma/2} m  (C_t f(X) = f(X+t), X = log y)
    tt = mp.mpf("0.6"); yy = mp.mpf("2.1")
    lhs = mp.power(yy * mp.exp(tt), -mp.mpf(1) / 4 - 1j * g / 2); rhs = mp.exp(-tt / 4 - 1j * tt * g / 2) * mp.power(yy, -mp.mpf(1) / 4 - 1j * g / 2)
    check(f"(D5.11) C_t m_{j} = exp(-t/4 - i t gamma/2) m_{j}", close(lhs, rhs, 1e-22))
    # Fourier transform hat m(tau) = int_0^inf e^{(-1/4 - i gamma/2 + i tau) X} dX = i/(tau - conj(w))
    tau = mp.mpf("1.1")
    ft = mp.quad(lambda X: mp.exp((-mp.mpf(1) / 4 - 1j * g / 2 + 1j * tau) * X), list(range(0, 301, 10)))  # e^{-75} tail dropped
    check(f"(N.4) kernel: hat m_{j}(tau) = i/(tau - conj w_{j})", close(ft, 1j / (tau - mp.conj(w)), 1e-18), mp.nstr(abs(ft - 1j / (tau - mp.conj(w))), 3))
# (D5.13) overlap of normalised kernels at height 1/4
a, ap, b = g1 / 2, g2 / 2, mp.mpf(1) / 4
w1, w2 = a + 1j * b, ap + 1j * b
ip = mp.quad(lambda X: mp.exp((-b - 1j * a) * X) * mp.conj(mp.exp((-b - 1j * ap) * X)), [0, mp.inf])
nrm = mp.quad(lambda X: mp.exp(-2 * b * X), [0, mp.inf])
check("(D5.13) |<k~, k~'>| = 2b/sqrt((a-a')^2 + 4 b^2) for the two modes", close(abs(ip) / nrm, 2 * b / mp.sqrt((a - ap) ** 2 + 4 * b * b), 1e-18), mp.nstr(abs(ip) / nrm, 10))

# ---------------------------------------------------------------- N5: Eisenstein T_2, T_3 for Gamma_1(11)
print("=== N5: Eisenstein Hecke spectra, N = 11 ===")
zeta5 = mp.exp(2j * mp.pi / 5)
# even characters mod 11: chi_k(2) = zeta5^k (2 generates (Z/11)^x, order 10; even chars = squares of ... : chi(-1) = chi(2^5) = zeta5^{5k} = 1)
for p in (2, 3):
    # exponent of 2 giving p: 3 = 2^8 mod 11
    e = {2: 1, 3: 8}[p]
    check(f"p = {p}: p = 2^{e} mod 11", pow(2, e, 11) == p)
    spec = [mp.mpf(p + 1)]
    for k in range(1, 5):
        c = zeta5 ** (e * k)
        spec += [1 + p * c, p + c]           # (chi_1, chi_2) = (1, chi) and (chi, 1): chi_1(p) + p chi_2(p)
    x = mp.mpf(0)  # placeholder
    poly_roots = mp.polyroots(None) if False else None
    # (N.6): det(x - T_p) = (sum_{j=0}^4 (x-p)^j) ((x-1)^5 - p^5)
    def N6(xx):
        return mp.fsum((xx - p) ** j for j in range(5)) * ((xx - 1) ** 5 - p ** 5)
    res = max(abs(N6(lam)) for lam in spec)
    check(f"(N.6) every eigenvalue of (N.5) is a root of the closed-form polynomial, p={p}", res < 1e-18, mp.nstr(res, 3))
    tr = mp.fsum(spec)
    check(f"(N.5) trace = 4(p+1) = {4*(p+1)}, not 9(p+1), p={p}", close(tr, 4 * (p + 1), 1e-20), mp.nstr(tr, 8))
    check(f"(N.5) dim Eis = 9 = h - 1 with h = 10 cusps of Gamma_1(11), p={p}", len(spec) == 9 and (10 == (sum((10 if d == 1 or d == 11 else 0) for d in (1, 11)) // 2)))
    if p == 2:
        pairs = [mp.mpc("1.618033988750", "1.902113032590"), mp.mpc("-0.618033988750", "1.175570504585"), mp.mpc("2.309016994375", "0.951056516295"), mp.mpc("1.190983005625", "0.587785252292")]
        ok = all(min(abs(lam - pr) for lam in spec) < 2e-12 and min(abs(lam - mp.conj(pr)) for lam in spec) < 2e-12 for pr in pairs)
        check("(N.5) the four listed conjugate pairs of T_2 eigenvalues", ok)
    check(f"T_p on Eis is not (p+1) I, p={p}", max(abs(lam - (p + 1)) for lam in spec) > 0.5)

# ---------------------------------------------------------------- summary
npass = sum(1 for _, ok, _ in LEDGER if ok)
print(f"=== {npass}/{len(LEDGER)} checks pass; runtime {time.time() - T0:.1f} s ===")
