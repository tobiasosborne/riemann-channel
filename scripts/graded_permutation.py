#!/usr/bin/env python3
"""The graded permutation (1 2)(3 4 5): rings, gas, induced zeros, physical letters.

Evidence for report/sections/03b_graded_permutation.tex (lab-book shard RC-03B).
Deterministic (seeded); every check is an assertion, the tally is printed at the end.
Sections: 1 rings and Lambda_sigma; 2 the gas (two oscillators, bond Fock space, thermal
vector); 3 grading, closures, holonomy, fermionic cycles, Moebius; 4 physical letters
(invariance under on-site isometries, the ladder 1/2/5 letters, the word formula).
"""
import itertools
import numpy as np
import sympy as sp

rng = np.random.default_rng(20260914)
CHECKS = 0
def check(cond, msg):
    global CHECKS
    CHECKS += 1
    assert cond, msg
    print(f"  ok {CHECKS:2d}  {msg}")

NMAX = 12
u = sp.symbols('u')
def series(expr, n=NMAX):
    return sp.Poly(sp.series(expr, u, 0, n + 1).removeO(), u).all_coeffs()[::-1]
def zeta_from(seq):                       # exp(sum_n seq[n-1] u^n / n), truncated
    return series(sp.exp(sum(sp.Rational(int(s), n) * u**n for n, s in enumerate(seq, 1))))
def mpow(M, n):
    return np.linalg.matrix_power(M, n)

# ---------------------------------------------------------------- 1. the permutation and its rings
sigma = {0: 1, 1: 0, 2: 3, 3: 4, 4: 2}           # (1 2)(3 4 5) on {0,..,4}
D = 5
P = np.zeros((D, D))
for x, y in sigma.items():
    P[y, x] = 1
cycles = [[0, 1], [2, 3, 4]]
print("1. rings of the permutation (1 2)(3 4 5)")
trP = [int(round(np.trace(mpow(P, n)))) for n in range(1, NMAX + 1)]
lam = [sum(len(c) for c in cycles if n % len(c) == 0) for n in range(1, NMAX + 1)]
check(trP == lam, f"Tr P^n = Lambda_sigma(n) = sum_(l|n) l m_l : {trP}")

def point_letters():
    return [np.outer(np.eye(D)[sigma[x]], np.eye(D)[x]) for x in range(D)]
def ring_vector(letters, n, twist=None):
    """psi_n = sum_w Tr(B A_{w_n} ... A_{w_1}) |w>, B = twist or 1, as a dict word -> amplitude."""
    B = np.eye(D) if twist is None else twist
    out = {}
    for w in itertools.product(range(len(letters)), repeat=n):
        M = B.copy()
        for s in w:
            M = letters[s] @ M
        a = np.trace(M)
        if abs(a) > 1e-12:
            out[w] = a
    return out
for n in (2, 3, 4, 6):
    psi = ring_vector(point_letters(), n)
    per = [x for x in range(D) if (lambda y: [y := sigma[y] for _ in range(n)][-1])(x) == x]
    words = set()
    for x in per:
        w, y = [], x
        for _ in range(n):
            w.append(y); y = sigma[y]
        words.add(tuple(w))
    check(set(psi) == words and all(abs(a - 1) < 1e-12 for a in psi.values()),
          f"n={n}: point-letter ring = uniform superposition of the {len(words)} periodic orbits with starting point")
    check(abs(sum(abs(a)**2 for a in psi.values()) - trP[n - 1]) < 1e-12, f"n={n}: ||psi_n||^2 = Tr P^n = {trP[n-1]}")
zeta = zeta_from(trP)
check(zeta == series(1 / ((1 - u**2) * (1 - u**3))), "exp(sum Tr P^n u^n/n) = 1/((1-u^2)(1-u^3)) = 1/det(1-uP)")
check(sp.factor(sp.Matrix(P.astype(int)).charpoly(u).as_expr()) == sp.factor((u**2 - 1) * (u**3 - 1)), "poles = eigenvalues of P: {1,-1} and the cube roots of unity")

# ---------------------------------------------------------------- 2. the gas
print("2. the gas: two oscillators, bond Fock space, thermal vector")
c = [sum(1 for a in range(N // 2 + 1) for b in range(N // 3 + 1) if 2 * a + 3 * b == N) for N in range(NMAX + 1)]
check(c == [int(z) for z in zeta], f"coefficient of u^N in zeta = #{{(a,b): 2a+3b = N}} = {c}")
# fixed monomials of Sym^k(P) on C^5 = gas configurations
def fixed_monomials(k):
    cnt = 0
    for m in itertools.product(range(k + 1), repeat=D):
        if sum(m) != k: continue
        if all(m[x] == m[sigma[x]] for x in range(D)): cnt += 1
    return cnt
fm = [fixed_monomials(k) for k in range(8)]
check(fm == c[:8], f"Tr Sym^k(P) = #sigma-fixed monomials = gas configurations of length k: {fm}")
# Tr_Fock u^N Gamma(P) = prod 1/(1 - u lambda) = 1/det(1-uP): from eigenvalues
ev = np.linalg.eigvals(P)
prodform = sp.prod([1 / (1 - u * sp.nsimplify(complex(round(l.real, 9), round(l.imag, 9)))) for l in ev])
check(all(abs(complex(x) - y) < 1e-9 for x, y in zip(series(prodform), c)),
      "Tr_Fock(C^5) u^N Gamma(P) = prod_lambda (1-u lambda)^{-1} = 1/((1-u^2)(1-u^3))")
beta = 0.7
Z = 1 / ((1 - np.exp(-2 * beta)) * (1 - np.exp(-3 * beta)))
K = 60
v = np.array([[np.exp(-beta * (2 * a + 3 * b) / 2) for b in range(K)] for a in range(K)])
check(abs(np.sum(v**2) - Z) < 1e-12, f"||v_beta||^2 = zeta_sigma(e^-beta) at beta={beta}: {Z:.6f}")
check(abs(np.sum(v**2) - np.sum(v[:, 0]**2) * np.sum(v[0, :]**2)) < 1e-12, "v_beta is a product vector over the two primes")
E_mean = sum(l * np.exp(-beta * n) for n, l in enumerate(lam, 1)) + sum(  # truncated tail beyond NMAX
    sum(len(cc) for cc in cycles if n % len(cc) == 0) * np.exp(-beta * n) for n in range(NMAX + 1, 400))
H_mean = np.sum(v**2 * np.array([[2 * a + 3 * b for b in range(K)] for a in range(K)])) / Z
check(abs(E_mean - H_mean) < 1e-10, "sum_n ||psi_n||^2 e^{-beta n} = <H>_beta (mean length of the gas)")
# the vector state agrees with Gibbs only on the diagonal algebra: <v|a|v> != 0 for the shift a
w2 = np.exp(-beta * np.arange(K)); w2 /= np.linalg.norm(w2)      # one oscillator, energy 2
shift = np.eye(K, k=-1)
check(abs(w2 @ shift @ w2) > 0.3 and abs(np.sum(w2**2 * np.diag(shift))) < 1e-15,
      f"vector state has coherences the Gibbs state lacks: <v|S|v> = {w2 @ shift @ w2:.4f}, Tr(rho S) = 0")

# ---------------------------------------------------------------- 3. grading, closures, holonomy
print("3. grading the 3-cycle odd: closures, holonomy, fermionic cycles, Moebius")
Pi = np.diag([1, 1, -1, -1, -1])
strP = [int(round(np.trace(Pi @ mpow(P, n)))) for n in range(1, NMAX + 1)]
check(strP == [2 * (n % 2 == 0) - 3 * (n % 3 == 0) for n in range(1, NMAX + 1)], f"str P^n = 2[2|n] - 3[3|n]: {strP}")
check(zeta_from(strP) == series((1 - u**3) / (1 - u**2)), "Ramond closure: exp(sum str P^n u^n/n) = (1-u^3)/(1-u^2) = 1/sdet(1-uP)")
check(sp.simplify((1 - u**3) / (1 - u**2) - (1 + u + u**2) / (1 + u)) == 0, "net: zeros at the primitive cube roots, pole at -1, the pole at 1 cancelled by the odd fixed vector")
check(zeta_from(trP) == series(1 / ((1 - u**2) * (1 - u**3))), "Neveu-Schwarz closure (no parity insertion): no zeros")
for h in (-1, 1j):
    # holonomy h around the odd cycle: put h on one edge of the cycle
    Ph = P.astype(complex).copy(); Ph[3, 2] = h
    poly = sp.Matrix(sp.Matrix(Ph.round(12).tolist()).applyfunc(sp.nsimplify)).charpoly(u).as_expr()
    check(sp.simplify(sp.expand(poly) - (u**2 - 1) * (u**3 - sp.nsimplify(h))) == 0,
          f"holonomy h={h} on the odd cycle: odd eigenvalues = cube roots of h")
check(sp.simplify((1 + u**3) / (1 - u**2) - (1 - u + u**2) / (1 - u)) == 0, "h=-1: zeta = (1-u+u^2)/(1-u): pole at 1 kept, zeros at exp(+-i pi/3), pole at -1 eaten")
# fermionic cycle of length l: Str_{Lambda(C^l)} u^N Gamma(P_l) = det(1 - u P_l) = 1 - u^l; occupied top form contributes -1
for l in range(2, 8):
    Pl = np.roll(np.eye(l), 1, axis=0)
    ext = 0
    for k in range(l + 1):
        # Tr Lambda^k(P_l) = e_k(eigenvalues) = coefficient of char poly
        ek = sum(np.prod(np.linalg.eigvals(Pl)[list(S)]) for S in itertools.combinations(range(l), k)) if k else 1
        ext += (-u)**k * sp.nsimplify(round(complex(ek).real))
    check(sp.expand(ext) == 1 - u**l and (-1)**l * round(np.linalg.det(Pl)) == -1,
          f"l={l}: Str_(exterior algebra) u^N Gamma(P_l) = 1 - u^l; (-1)^l sgn(cycle) = -1")
# Moebius: all primes fermionic turns zeta into 1/zeta on 13-smooth numbers, exact at s = 2
primes = [2, 3, 5, 7, 11, 13]
lhs = sp.prod([1 - sp.Rational(1, p**2) for p in primes])
rhs = sum(sp.Rational((-1)**len(S), int(np.prod([1] + [p for p in S]))**2) for r in range(len(primes) + 1) for S in itertools.combinations(primes, r))
check(lhs == rhs, "all primes fermionic: prod_p (1 - p^-s) = sum_squarefree mu(n) n^-s (13-smooth, s=2, exact)")

# ---------------------------------------------------------------- 4. physical letters
print("4. physical letters: invariance, the ladder, the word formula")
G = np.kron(Pi, Pi)
def doubled(letters):
    return sum(np.kron(A, A.conj()) for A in letters)
def ramond_norm(letters):
    Ed = doubled(letters)
    return [int(round(np.trace(G @ mpow(Ed, n)).real)) for n in range(1, NMAX + 1)]
def kraus_rank(letters):
    C = sum(np.outer(A.ravel(), A.ravel().conj()) for A in letters)
    return int(np.linalg.matrix_rank(C, tol=1e-9))
one = [P.astype(complex)]
two = [(P @ np.diag([1, 1, 0, 0, 0])).astype(complex), (P @ np.diag([0, 0, 1, 1, 1])).astype(complex)]
five = [A.astype(complex) for A in point_letters()]
r1, r2, r5 = ramond_norm(one), ramond_norm(two), ramond_norm(five)
check(kraus_rank(one) == 1 and r1 == [s * s for s in strP], f"one letter: Kraus rank 1, Ramond norm |str P^n|^2 = {r1}")
check(kraus_rank(two) == 2 and r2 == [4 * (n % 2 == 0) + 9 * (n % 3 == 0) for n in range(1, NMAX + 1)], f"cycle letters: Kraus rank 2, Ramond norm sum_c (Tr P_c^n)^2 = {r2}")
check(kraus_rank(five) == 5 and r5 == trP, f"point letters: Kraus rank 5, Ramond norm Tr P^n = {r5}")
check(zeta_from(r1) == series((1 + u**3)**2 / ((1 - u**2)**2 * (1 - u**3))), "one letter: ring zeta = 1/sdet(1 - u P(x)conj P) = (1+u^3)^2/((1-u^2)^2(1-u^3))")
# invariance: on-site unitary mixing of letters leaves E_d and every twisted trace unchanged; a padded isometry too
V = np.linalg.qr(rng.normal(size=(5, 5)) + 1j * rng.normal(size=(5, 5)))[0]
mixed = [sum(V[t, s] * five[s] for s in range(5)) for t in range(5)]
W = np.linalg.qr(rng.normal(size=(8, 5)))[0]                      # isometry C^5 -> C^8
padded = [sum(W[t, s] * five[s] for s in range(5)) for t in range(8)]
check(np.allclose(doubled(mixed), doubled(five)) and np.allclose(doubled(padded), doubled(five)) and ramond_norm(padded) == r5,
      "letters mixed by a unitary or padded by an isometry: same E_d, same Ramond norms, Kraus rank unchanged")
check(kraus_rank(padded) == 5, "the Kraus rank of E_d is the minimal letter count (8 padded letters still rank 5)")
# word formula: Ramond norm = sum_w |sum_{x periodic, orbit emits w} (-1)^{|x|}|^2, for deterministic letter assignments
def word_norm(label, n):
    per = [x for x in range(D) if (lambda y: [y := sigma[y] for _ in range(n)][-1])(x) == x]
    amp = {}
    for x in per:
        w, y = [], x
        for _ in range(n):
            w.append(label[y]); y = sigma[y]
        amp[tuple(w)] = amp.get(tuple(w), 0) + Pi[x, x]
    return sum(abs(a)**2 for a in amp.values())
for name, label, ref in (("one", [0] * 5, r1), ("cycle", [0, 0, 1, 1, 1], r2), ("point", list(range(5)), r5)):
    check([word_norm(label, n) for n in range(1, NMAX + 1)] == ref, f"word formula sum_w |sum_x (-1)^|x||^2 reproduces the {name}-letter Ramond norm")
# separated sectors: no odd contribution, twisted = untwisted norm
for L in (two, five):
    Ed = doubled(L)
    check(all(abs(np.trace(mpow(Ed, n)) - np.trace(G @ mpow(Ed, n))) < 1e-9 for n in range(1, NMAX + 1)), "letters that resolve the parity: twisted norm = untwisted norm (no odd sector populated)")

# ---------------------------------------------------------------- 5. a parity-measuring jump
print("5. a parity-measuring jump: uniform shift of the odd sector, even sector untouched")
# discrete: partial parity dephasing D_p(rho) = (1-p) rho + p Pi rho Pi composed with the one-letter channel
p = 0.3
Ed1 = doubled(one)
Dp = (1 - p) * np.eye(D * D) + p * G
Edp = Dp @ Ed1
even_tr = [np.trace(0.5 * (np.eye(D * D) + G) @ mpow(Ed1, n)).real for n in range(1, NMAX + 1)]
odd_tr = [np.trace(0.5 * (np.eye(D * D) - G) @ mpow(Ed1, n)).real for n in range(1, NMAX + 1)]
ram_p = [np.trace(G @ mpow(Edp, n)).real for n in range(1, NMAX + 1)]
check(np.allclose(ram_p, [e - (1 - 2 * p)**n * o for n, (e, o) in enumerate(zip(even_tr, odd_tr), 1)]),
      f"parity dephasing with weight p={p}: Ramond norm = Tr_even E^n - (1-2p)^n Tr_odd E^n (odd sector rescaled, even untouched)")
# continuous: L = L_0 + gamma (Gamma - 1) on the doubled bond, L_0 a random graded Lindbladian (H even, jumps of both parities)
gamma = 0.125
Pi_c = Pi.astype(complex)
H = rng.normal(size=(D, D)) + 1j * rng.normal(size=(D, D)); H = H + H.conj().T; H = 0.5 * (H + Pi_c @ H @ Pi_c)   # even Hamiltonian
R1 = rng.normal(size=(D, D)) + 1j * rng.normal(size=(D, D)); R2 = rng.normal(size=(D, D)) + 1j * rng.normal(size=(D, D))
Rs = [0.5 * (R1 + Pi_c @ R1 @ Pi_c), 0.5 * (R2 - Pi_c @ R2 @ Pi_c)]          # one even jump, one odd jump
I5 = np.eye(D)
def lind(H, Rs):
    Q = -1j * H - 0.5 * sum(R.conj().T @ R for R in Rs)
    return np.kron(Q, I5) + np.kron(I5, Q.conj()) + sum(np.kron(R, R.conj()) for R in Rs)
L0 = lind(H, Rs)
L1 = lind(H, Rs + [np.sqrt(gamma) * Pi_c])
check(np.allclose(L1, L0 + gamma * (G - np.eye(D * D))), "jump sqrt(gamma) Pi adds exactly gamma (Gamma_b - 1) to the doubled-bond generator")
Pe, Po = 0.5 * (np.eye(D * D) + G), 0.5 * (np.eye(D * D) - G)
def sector_eigs(L, Proj):
    ev = np.linalg.eigvals(Proj @ L @ Proj)
    return ev[np.abs(ev) > 1e-9]
def same_multiset(a, b, tol=1e-7):
    b = list(b)
    for x in a:
        k = int(np.argmin(np.abs(np.array(b) - x)))
        if abs(b[k] - x) > tol: return False
        b.pop(k)
    return not b
check(same_multiset(sector_eigs(L0, Pe), sector_eigs(L1, Pe)) and same_multiset(sector_eigs(L0, Po) - 2 * gamma, sector_eigs(L1, Po)),
      f"gamma={gamma}: every even-odd coherence eigenvalue shifted by -2 gamma = -{2*gamma}, every even-sector eigenvalue unchanged")
print(f"all {CHECKS} checks passed")
