#!/usr/bin/env python3
"""Independent re-derivation of the decisive facts about the phase-side Lindbladian guess
(shard RC-04G; the two codex gpt-6-astra reports under notes/yolo-lindblad/). Deterministic.

1 shells: V_p on L2(Z/N) versus the Ramanujan-shell formulas; Shor map at coprime levels.
2 grading: the prime dissipator applied to the vacuum has an odd part.
3 vacuum generating functions on the doubled shell ladder: exact shifted formulas.
4 inverse multiset sum: <v, prod_p (1 - p^{-w} V_p) v> = 1/zeta_P(w + 1/2).
5 Gibbs weights are not stationary (exact 2x2 counterexample); corrected rate ratio p^beta.
6 parity closure is not a quotient by Q^x (2-dim counterexample).
7 Galois dephasing: uniform rates give a real shift; inversion-asymmetric rates give frequencies.
"""
import itertools, cmath
import numpy as np, sympy as sp
from math import gcd

CHECKS = 0
def check(cond, msg):
    global CHECKS
    CHECKS += 1
    assert cond, msg
    print(f"  ok {CHECKS:2d}  {msg}")
def primes_upto(P):
    return [p for p in range(2, P + 1) if all(p % q for q in range(2, int(p**0.5) + 1))]
def phi(n):
    return sum(1 for a in range(1, n + 1) if gcd(a, n) == 1)

# ------------------------------------------------------------ 1. shells from L2(Z/N)
print("1. V_p on L2(Z/N) and the Ramanujan shells")
N = 360
def fourier_basis(M):          # e_r(x) = exp(2 pi i r x), r = j/M, as columns, Haar-normalised
    x = np.arange(M)
    return np.exp(2j * np.pi * np.outer(x, np.arange(M)) / M) / np.sqrt(M)
def V_matrix(p, M):            # L2(Z/(M/p)) -> L2(Z/M): (V f)(x) = sqrt(p) f(x/p) if p | x
    m = M // p
    V = np.zeros((M, m))
    for y in range(m):
        V[p * y % M, y] = 1.0   # sqrt(p) * (Haar normalisation sqrt(1/M)/sqrt(1/m) = 1/sqrt(p)) = 1
    return V
def ramanujan(b, M):           # c_b as a vector on Z/M (b | M): sum over primitive a/b of e_{a/b}
    E = fourier_basis(M); v = np.zeros(M, complex)
    for a in range(1, b + 1):
        if gcd(a, b) == 1: v += E[:, (a * (M // b)) % M] * np.sqrt(M)
    return v / np.sqrt(M)      # Haar-normalised e_r have norm 1
for p in (2, 3, 5):
    V = V_matrix(p, N); m = N // p
    check(np.allclose(V.T @ V, np.eye(m)), f"p={p}: V_p is an isometry L2(Z/{m}) -> L2(Z/{N})")
    Em, EN = fourier_basis(m), fourier_basis(N)
    ok = True
    for j in range(m):          # r = j/m ; preimages s = (j + k m)/N... i.e. s = (j + k*m)/(p*m)
        img = V @ Em[:, j]
        pre = sum(EN[:, (j + k * m) % N] for k in range(p)) / np.sqrt(p)
        ok &= np.allclose(img, pre)
    check(ok, f"p={p}: V_p e_r = p^(-1/2) sum over the p preimages e_s (Fourier picture)")
    for b in [d for d in range(1, m + 1) if m % d == 0][:12]:
        cb = ramanujan(b, m); img = V @ cb
        if b % p:
            want = (ramanujan(b, N) + ramanujan(p * b, N)) / np.sqrt(p)
        else:
            want = ramanujan(p * b, N) / np.sqrt(p)
        assert np.allclose(img, want), (p, b)
    check(True, f"p={p}: V_p c_b = p^(-1/2)(c_b + c_pb) for p not | b, = p^(-1/2) c_pb for p | b (on all divisors b of {m})")
# normalised: |b> = c_b/sqrt(phi(b)) gives V_p|b> = p^{-1/2}(|b> + sqrt(p-1)|pb>) resp. |pb>
check(abs(np.sqrt(phi(6)) / np.sqrt(phi(2)) - np.sqrt(2)) < 1e-12 and phi(4) / phi(2) == 2, "normalisation: phi(pb)/phi(b) = p-1 (p not | b) or p (p | b)")
# Shor map: sqrt(p) V_p^+ on level b, p coprime to b, permutes e_{a/b} -> e_{pa/b}
b = 15; Eb = fourier_basis(b)
for p in (2, 7):
    Vb = V_matrix(p, p * b)                       # L2(Z/b) -> L2(Z/(pb)); V^+ : L2(Z/(pb)) -> L2(Z/b)
    Epb = fourier_basis(p * b)
    S = np.sqrt(p) * Vb.T @ Epb[:, [j * p % (p * b) for j in range(b)]]   # images of e_{j/b} under sqrt(p) V^+
    perm = np.array([[abs(np.vdot(Eb[:, k], S[:, j])) for j in range(b)] for k in range(b)])
    check(np.allclose(perm, np.eye(b)[:, [(p * j) % b for j in range(b)]]) , f"p={p}, b={b}: sqrt(p) V_p^+ restricted to level b is the Shor permutation r -> pr")

# ------------------------------------------------------------ shell ladder (exact formulas) for 2-7
def shell_ops(P, Bmax):
    ps = primes_upto(P); D = Bmax
    Vs = {}
    for p in ps:
        V = np.zeros((D, D))
        for b in range(1, D + 1):
            if b % p:
                V[b - 1, b - 1] = 1 / np.sqrt(p)
                if p * b <= D: V[p * b - 1, b - 1] = np.sqrt((p - 1) / p)
            else:
                if p * b <= D: V[p * b - 1, b - 1] = 1.0
        Vs[p] = V
    return ps, Vs
print("2. the grading is not preserved")
ps, Vs = shell_ops(5, 30)
P0 = np.zeros((30, 30)); P0[0, 0] = 1
Pi = -np.eye(30); Pi[0, 0] = 1
for p in ps:
    LP0 = Vs[p] @ P0 @ Vs[p].T - P0
    odd = 0.5 * (LP0 - Pi @ LP0 @ Pi)
    check(np.linalg.norm(odd) > 0.1 and abs(odd[0, p - 1] - np.sqrt(p - 1) / p) < 1e-12,
          f"p={p}: L_p(|1><1|) has odd part with entry sqrt(p-1)/p at (1,p): [L, Gamma_b] != 0")

print("3. vacuum generating functions on the doubled shell ladder")
P, Bmax, beta = 5, 64, 1.0
ps, Vs = shell_ops(P, Bmax); D2 = Bmax * Bmax
I2 = np.eye(D2); vac = np.zeros(D2); vac[0] = 1
def S_P(z): return sum(p**(-z) for p in ps)
def zeta_P(z): return np.prod([1 / (1 - p**(-z)) for p in ps])
for s in (0.5 + 14.1347j, 0.8 + 3j, 1.1):
    K = sum(p**(-beta) * p**(-s) * np.kron(Vs[p], Vs[p]) for p in ps)
    F = vac @ np.linalg.solve(I2 - K, vac)
    FE = vac.copy()
    for p in ps:
        FE = np.linalg.solve(I2 - p**(-beta - s) * np.kron(Vs[p], Vs[p]), FE)
    FE = vac @ FE
    check(abs(F - 1 / (1 - S_P(s + beta + 1))) < 1e-10, f"s={s}: ordered-word vacuum resolvent = 1/(1 - S_P(s+beta+1))")
    check(abs(FE - zeta_P(s + beta + 1)) < 1e-10, f"s={s}: multiset (Euler) vacuum function = zeta_P(s+beta+1), shifted by beta+1")
check(all(abs(S_P(s + 2)) < 1 for s in np.linspace(0.3, 1.2, 10)), "|S_P(s+2)| < 1 on Re s in [0.3,1.2]: the ordered resolvent has no pole in the strip (beta = 1)")

print("4. the inverse multiset sum")
for w in (1.3, 2.0 + 1j):
    x = np.zeros(Bmax); x[0] = 1
    for p in ps: x = x - p**(-w) * (Vs[p] @ x)
    lhs = x[0]
    check(abs(lhs - 1 / zeta_P(w + 0.5)) < 1e-12, f"w={w}: <v, prod_p (1 - p^-w V_p) v> = 1/zeta_P(w + 1/2) (exact, from <v,V_n v> = n^-1/2)")

print("5. Gibbs weights are not stationary under the phase jumps")
s2 = sp.sqrt(2)
V2 = sp.Matrix([[1, 0], [1, 0]]) / s2      # V_2 on shells {1, 2}
rho = sp.diag(sp.Rational(4, 5), sp.Rational(1, 5))   # weights b^-beta, beta = 2
def diss(A, X): return A * X * A.T - (A.T * A * X + X * A.T * A) / 2
lam = sp.Rational(1, 2); b2 = 2
L = lam * (diss(V2, rho) + sp.Rational(1, 4) * diss(V2.T, rho))
check(sp.simplify(L - sp.Matrix([[-sp.Rational(3, 16), sp.Rational(27, 160)], [sp.Rational(27, 160), sp.Rational(3, 16)]])) == sp.zeros(2, 2),
      "exact 2x2 counterexample: L_db(rho_Gibbs) = [[-3/16, 27/160],[27/160, 3/16]] != 0 (beta = 2, lambda_2 = 1/2)")
# classical population balance along 1 -> 2 needs down/up rate ratio p^beta
edge = lam * (1 - sp.Rational(1, b2)); up = edge * sp.Rational(4, 5); down_needed = up / sp.Rational(1, 5)
check(sp.simplify(down_needed / edge - 4) == 0, "population balance on the first edge needs rate ratio down/up = p^beta = 4, not p^-beta")

print("6. a parity closure is not a quotient by Q^x")
th = 0.7
W = np.diag([1, np.exp(1j * th)]); Pi2 = np.diag([1, -1])
check(abs(abs(np.trace(Pi2 @ W))**2 - abs(1 - np.exp(1j * th))**2) < 1e-12 and abs(np.trace(Pi2 @ np.eye(2))) < 1e-12,
      "commuting W_p and Pi: parity-closed norm of the word W_p is |1-e^{i theta}|^2, of the identity 0: W_p is not identified with 1")

print("7. Galois dephasing with symmetric and asymmetric rates")
b = 5; G = [a for a in range(1, b) if gcd(a, b) == 1]
chars = {}
gen = 2; log = {pow(gen, k, b): k for k in range(4)}
for j in range(4): chars[j] = {a: cmath.exp(2j * cmath.pi * j * log[a] / 4) for a in G}
def coeff(rates, chi, chi2): return sum(rates[a] * chi[a] * chi2[a].conjugate() for a in G) - sum(rates.values())
uni = {a: 0.25 for a in G}
c_same = coeff(uni, chars[1], chars[1]); c_cross = coeff(uni, chars[1], chars[2])
check(abs(c_same) < 1e-12 and abs(c_cross + 1) < 1e-12, "uniform rates: 0 within a character sector, -gamma (= -1) on cross-character coherences, real")
asym = {1: 0.1, 2: 0.6, 3: 0.2, 4: 0.1}      # not symmetric under a -> a^-1 (2 <-> 3)
c_as = coeff(asym, chars[1], chars[0])
check(abs(c_as.imag) > 0.1, f"inversion-asymmetric rates: cross coherence coefficient {c_as:.3f} has a nonzero imaginary part (a frequency)")
sym = {1: 0.1, 2: 0.4, 3: 0.4, 4: 0.1}
check(abs(coeff(sym, chars[1], chars[0]).imag) < 1e-12, "inversion-symmetric rates: the coefficient is real")
print(f"all {CHECKS} checks passed")
