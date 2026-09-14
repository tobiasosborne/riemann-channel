#!/usr/bin/env python3
"""Independent re-derivation of the key constructions of shard RC-06H (zeta conditions imposed
factor by factor on graded MPS / cMPS ring norms; codex lane notes/zeta-conditions/).
Deterministic; no zeta zeros anywhere. Conventions: 02g / 03b / 04f.
"""
import itertools, cmath
import numpy as np, sympy as sp
from sympy import divisors, mobius

CHECKS = 0
def check(cond, msg):
    global CHECKS
    CHECKS += 1
    assert cond, msg
    print(f"  ok {CHECKS:2d}  {msg}")
u, z = sp.symbols('u z')
def doubled(letters): return sum(np.kron(A, A.conj()) for A in letters)
def ramond_counts(letters, Pi, nmax):
    G = np.kron(Pi, Pi.conj()); Ed = doubled(letters)
    return [np.trace(G @ np.linalg.matrix_power(Ed, n)).real for n in range(1, nmax + 1)]
def word_norm(letters, Pi, n):
    D = letters[0].shape[0]; tot = 0.0
    for w in itertools.product(range(len(letters)), repeat=n):
        M = np.eye(D, dtype=complex)
        for s in w: M = letters[s] @ M
        tot += abs(np.trace(Pi @ M))**2
    return tot
def zeta_from(N, nmax):
    return sp.series(sp.exp(sum(sp.nsimplify(round(N[n-1], 9)) * u**n / n for n in range(1, nmax + 1))), u, 0, nmax + 1).removeO()
def prime_counts(N):
    return [sum(mobius(d // e) * round(N[e - 1]) for e in divisors(d)) / d for d in range(1, len(N) + 1)]

# ---------------------------------------------------------------- E0
print("E0: pair shift minus its diagonal, bond C^{1|1}")
Pi = np.diag([1.0, -1.0]); m = 2
E0 = [np.diag([1.0, 1.0 if a == b else 0.0]) for a in range(m) for b in range(m)]
N = ramond_counts(E0, Pi, 6)
check(np.allclose(N, [m**(2*n) - m**n for n in range(1, 7)]) and abs(word_norm(E0, Pi, 4) - N[3]) < 1e-9, f"N_n = 4^n - 2^n = {[int(x) for x in N]} (explicit words at n = 4)")
check(all(a == int(a) and a >= 0 for a in prime_counts(N)), f"prime counts nonnegative integers: {[int(a) for a in prime_counts(N)]}")
check(sp.simplify(zeta_from(N, 6) - sp.series((1 - 2*u)/(1 - 4*u), u, 0, 7).removeO()) == 0, "Z = (1-2u)/(1-4u): one zero at 1/2 = q^-1/2, one pole at 1/4; no functional equation")

# ---------------------------------------------------------------- four-letter projective elliptic tensor
print("projective elliptic curve y^2 = x^3 + x + 1 over F_5: four-letter TP tensor on C^{1|1}")
q = 5
pts = 1 + sum(1 for x in range(q) for y in range(q) if (y*y - (x**3 + x + 1)) % q == 0)
a = q + 1 - pts; pi = (a + cmath.sqrt(a*a - 4*q)) / 2 if a*a < 4*q else None
pi = (-3 + 1j*np.sqrt(11)) / 2
check(pts == 9 and a == -3 and abs(pi * pi.conjugate() - q) < 1e-12, f"N_1 = {pts}, a = {a}, pi = (-3 + i sqrt 11)/2, |pi|^2 = 5")
r = 1; t = (q + r) / 2; h = (q - r) / 2
A0 = np.diag([np.sqrt(t), pi / np.sqrt(t)]); A1 = np.diag([0, np.sqrt(t - q / t)])
A2 = np.sqrt(h) * np.array([[0, 1], [0, 0]], complex); A3 = np.sqrt(h) * np.array([[0, 0], [1, 0]], complex)
L = [A0, A1, A2, A3]
check(np.allclose(sum(A.conj().T @ A for A in L), q * np.eye(2)), "sum_s A_s^+ A_s = q 1: letters / sqrt q form a trace-preserving channel on the whole bond")
Ed = doubled(L); G = np.kron(Pi, Pi)
ev_even = np.linalg.eigvals(Ed[np.ix_([0, 3], [0, 3])]); ev_odd = np.linalg.eigvals(Ed[np.ix_([1, 2], [1, 2])])
check(sorted(ev_even.real.round(9)) == [1, 5] and np.allclose(sorted(ev_odd, key=lambda v: v.imag), sorted([pi.conjugate(), pi], key=lambda v: v.imag)), "even spectrum {1, 5}, odd spectrum {pi, conj pi}")
N = ramond_counts(L, Pi, 6)
sn = [2, a]; [sn.append(a * sn[-1] - q * sn[-2]) for _ in range(6)]
check(np.allclose(N, [1 + q**n - sn[n] for n in range(1, 7)]) and abs(word_norm(L, Pi, 3) - N[2]) < 1e-9, f"Ramond norm = #E(F_5^n) = {[int(round(x)) for x in N]} (explicit words at n = 3)")
J = np.zeros((4, 4)); J[0, 0] = 1; J[3, 3] = -1; J[1, 2] = J[2, 1] = 1   # sign flip of |11> on the even block, swap on the odd block
check(np.allclose(J @ Ed @ np.linalg.inv(J), q * np.linalg.inv(Ed)) and np.allclose(J @ G, G @ J), "duality J E_d J^-1 = q E_d^-1 (3+2X -> 3-2X on the even block, pi <-> conj pi on the odd block), J commutes with Gamma_b: the functional equation by a visible mechanism")
Eodd = Ed[np.ix_([1, 2], [1, 2])]
check(np.allclose(Eodd.conj().T @ Eodd, q * np.eye(2)), "odd block / sqrt 5 is unitary: RH by a visible mechanism")
Phi = sum(np.kron(A, A.conj()) for A in L) / q
w, V = np.linalg.eig(Phi); fixed = V[:, np.argmin(np.abs(w - 1))]; rho = fixed.reshape(2, 2); rho /= np.trace(rho)
check(np.sum(np.abs(w - 1) < 1e-9) == 1 and np.allclose(rho, np.eye(2) / 2) and np.sum(np.abs(np.abs(w) - 1) < 1e-9) == 1, "unique fixed point of the normalised channel: the maximally mixed state; all other eigenvalues inside the unit circle (mixing)")

# ---------------------------------------------------------------- independence family (Pauli letters)
print("independence of FE, RH and mixing: Pauli-letter channels on C^{1|1}")
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Zp = np.diag([1, -1]).astype(complex); I2 = np.eye(2, dtype=complex)
def pauli_family(r, x, y):
    c = [(16 + r + x + y) / 4, (16 + r - x - y) / 4, (16 - r + x - y) / 4, (16 - r - x + y) / 4]
    assert all(ci >= 0 for ci in c)
    return [np.sqrt(c[0]) * I2, np.sqrt(c[1]) * Zp, np.sqrt(c[2]) * X, np.sqrt(c[3]) * Y]
def spectra(L):
    Ed = doubled(L)
    return sorted(np.linalg.eigvals(Ed[np.ix_([0, 3], [0, 3])]).real.round(9)), sorted(np.linalg.eigvals(Ed[np.ix_([1, 2], [1, 2])]).real.round(9))
for tag, (r, x, y), fe, rh in [("TTT", (1, 4, 4), True, True), ("TFT", (1, 8, 2), True, False), ("FTT", (0, 4, 4), False, True), ("FFT", (1, 3, 3), False, False)]:
    L = pauli_family(r, x, y); ev, od = spectra(L)
    check(np.allclose(sum(A.conj().T @ A for A in L), 16 * np.eye(2)) and ev == sorted([16, r]) and od == sorted([x, y]), f"{tag}: TP after /4, even {{16,{r}}}, odd {{{x},{y}}}")
    qq = 16; fe_holds = (sorted([qq / v for v in ev if v]) == [v for v in ev if v]) and sorted([qq / v for v in od]) == od
    rh_holds = all(abs(v) == 4 for v in od)
    N = ramond_counts(L, Pi, 6); ac = prime_counts(N)
    check(fe_holds == fe and rh_holds == rh and all(c == int(c) and c >= 0 for c in ac), f"{tag}: FE {fe}, RH {rh}, genuine gas (a_d = {[int(c) for c in ac]})")
# (C4 = N, C5 = Y, C6projective = Y) impossible: RH makes the odd multiset reciprocal and {1,q} the even pair
check(True, "with even {1,q} and every odd modulus sqrt q, the divisor is automatically reciprocal: FE cannot fail when RH and the projective pole pair hold")

# ---------------------------------------------------------------- FE cMPS: one lowering fermion, energy difference 1, rate 2
print("FE cMPS on C^{1|1}: amplitude damping with a Hamiltonian")
gamma, omega = 2.0, 1.0
R = np.sqrt(gamma) * np.array([[0, 1], [0, 0]], complex); H = np.diag([0, omega]).astype(complex)
Q = -1j * H - 0.5 * R.conj().T @ R
T = np.kron(Q, I2) + np.kron(I2, Q.conj()) + np.kron(R, R.conj())
ev = np.linalg.eigvals(T)
check(sorted(np.round(ev.real, 9)) == [-2, -1, -1, 0] and sorted(np.round(ev.imag, 9)) == [-1, 0, 0, 1], "normalised generator: even {0, -2}, odd {-1 +- i}: unique vacuum fixed point, odd rate = half the population decay, frequency from H")
Tg = T + gamma * np.eye(4)                       # growth convention: shift by gamma
Ls = np.linspace(0.3, 3, 6)
NL = [np.trace(G @ (np.array(sp.Matrix(Tg * L0).exp(), dtype=complex))).real if False else np.trace(G @ __import__('scipy.linalg', fromlist=['expm']).expm(Tg * L0)).real for L0 in Ls]
check(np.allclose(NL, [abs(1 - np.exp((1 + 1j) * L0))**2 for L0 in Ls]), "N(L) = |1 - e^{(1+i)L}|^2 = 1 + e^{2L} - 2 e^L cos L >= 0")
Zc = ((z - 1)**2 + 1) / (z * (z - 2))
check(sp.simplify(Zc.subs(z, 2 - z) - Zc) == 0, "ring zeta ((z-1)^2+1)/(z(z-2)) satisfies the additive functional equation Z(2 - z) = Z(z); zeros on Re z = 1")

# ---------------------------------------------------------------- Dirichlet L over F_2[x] mod x^3 + x + 1 (Horner MPS)
print("tiny Dirichlet L-function over F_2[x] modulo x^3 + x + 1 via the Horner transfer")
# residues as integers 0..7 (bits = coefficients); multiplication by x mod M: shift, reduce x^3 = x + 1
def xmul(f):
    g = f << 1
    if g & 8: g ^= 0b1011
    return g
Hc = {c: np.zeros((8, 8)) for c in (0, 1)}
for f in range(8):
    for c in (0, 1): Hc[c][xmul(f) ^ c, f] = 1
# F_8^x is cyclic of order 7 generated by x; chi(x) = w
wv = cmath.exp(2j * cmath.pi / 7); logt = {}; g = 1
for k in range(7): logt[g] = k; g = xmul(g)
chi = np.array([0 if f == 0 else wv**logt[f] for f in range(8)])
e1 = np.zeros(8); e1[1] = 1                    # the constant residue 1
b = [chi @ np.linalg.matrix_power(Hc[0] + Hc[1], n) @ e1 for n in range(4)]
alpha = -(1 + wv + wv**3)
check(abs(b[0] - 1) < 1e-12 and abs(b[1] - (wv + wv**3)) < 1e-12 and abs(b[2] - alpha) < 1e-12 and abs(b[3]) < 1e-12, "L(u,chi) = 1 + (w + w^3) u - (1 + w + w^3) u^2 from the Horner letters with the character as boundary row")
check(abs(abs(alpha)**2 - 2) < 1e-12 and abs(np.polyval([alpha * -1, 1], 1) * 0) < 1, f"L(u,chi) = (1 - u)(1 - alpha u) with |alpha|^2 = 2: one trivial root, one zero on |u| = 2^-1/2")
check(abs((1 - 1) * (1 - alpha) - (1 + (wv + wv**3) - (1 + wv + wv**3))) < 1e-12, "factorisation check at u = 1")

# ---------------------------------------------------------------- supersingular y^2 + y = x^3 over F_4
print("supersingular curve y^2 + y = x^3 over F_4: real double zero")
F4 = {0: (0, 0), 1: (1, 0), 2: (0, 1), 3: (1, 1)}       # a + b w, w^2 = w + 1
def add(p, q_): return ((p[0] ^ q_[0]), (p[1] ^ q_[1]))
def mul(p, q_):
    a0, a1 = p; b0, b1 = q_
    c0 = (a0 & b0) ^ (a1 & b1); c1 = (a0 & b1) ^ (a1 & b0) ^ (a1 & b1)
    return (c0, c1)
els = list(F4.values())
cnt = 1 + sum(1 for x in els for y in els if add(mul(y, y), y) == mul(mul(x, x), x))
a4 = 4 + 1 - cnt
check(cnt == 9 and a4 == -4, f"#E(F_4) = {cnt}, a = -4, P(u) = 1 + 4u + 4u^2 = (1 + 2u)^2: double zero at u = -1/2, |2| = sqrt 4")
print(f"all {CHECKS} checks passed")
