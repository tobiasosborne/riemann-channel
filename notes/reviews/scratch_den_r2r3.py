"""REFUTE lane for notes/deninger-cmps/reformulation.md, Propositions R2, R3, R5(b).
Independent: imports nothing from scripts/.  Run from the repository root.

 R2a  Poisson trace of a one-prime suspension; the lifted Frobenius pi on C/Gamma is a degree-p covering,
      not a diffeomorphism (so R2(a) with M = E(C), f = pi is outside R2(a)'s own hypotheses).
 R2c  Bost-Connes vectors v_rho: joint eigenvectors of the mu_p^* for EVERY rho, zeros not singled out;
      the one-prime orthogonality condition.
 R3   Deninger's coefficient (34) against the superdeterminant; rotations vs reflections, all k in Z\0;
      Deuring's theorem for p = 2..13 by enumeration; Honda-Tate: algebraic angle does not give an elliptic curve.
 R5b  measure bookkeeping on Deninger's elliptic solenoid (p = 5, pi = 1+2i).
"""
import itertools
import numpy as np
import sympy as sp

ok = 0
fail = 0


def check(name, cond, info=''):
    global ok, fail
    if cond:
        ok += 1
        print(f'  PASS {name} {info}')
    else:
        fail += 1
        print(f'  FAIL {name} {info}')


print('R2(a) Poisson trace of the suspension')
q = 5.0
Lq = np.log(q)
for mu in (1 + 2j, 3.0, np.sqrt(5) * np.exp(0.7j)):
    for (t0, s) in ((2 * Lq + 0.01, 0.1), (3 * Lq - 0.05, 0.08)):
        lam = (np.log(mu) + 2j * np.pi * np.arange(-4000, 4001)) / Lq
        lhs = np.sum(s * np.sqrt(2 * np.pi) * np.exp(t0 * lam + s * s * lam * lam / 2))
        m = np.arange(-10, 30)
        rhs = Lq * np.sum(mu ** m.astype(complex) * np.exp(-(m * Lq - t0) ** 2 / (2 * s * s)))
        check(f'R2a Poisson mu={mu:.3f} t0={t0:.3f}', abs(lhs - rhs) < 1e-10 * max(1, abs(rhs)),
              f'|diff|={abs(lhs-rhs):.1e}')
# pi = 1+2i on C/Z[i]: integer matrix of z -> pi z on basis (1, i)
M = np.array([[1, -2], [2, 1]])
check('R2a pi=1+2i acts on Z[i] with det = 5 = [Gamma:pi Gamma] (a 5-fold covering of E(C))', round(np.linalg.det(M)) == 5)
check('R2a so pi is not a diffeomorphism of E(C): degree 5 != +-1; H^2 eigenvalue 5 impossible for a diffeo',
      abs(round(np.linalg.det(M))) != 1)

print('R2(c) Bost-Connes vectors')
N = 200000
n = np.arange(1, N + 1)
for rho in (0.8 + 3.3j, 0.75 - 1.0j, 0.5 + 14.134725141734693j):
    v = n.astype(complex) ** (-rho)
    for p in (2, 3, 7):
        # mu_p^* e_{pm} = e_m: (mu_p^* v)_m = v_{pm}
        lhs = v[p * np.arange(1, N // p + 1) - 1]
        rhs = p ** (-rho) * v[:N // p]
        check(f'R2c mu_{p}^* v_rho = p^-rho v_rho, rho={rho}', np.max(np.abs(lhs - rhs)) < 1e-12)
    if rho.real > 0.5:
        import mpmath as mp
        tail = float(mp.zeta(2 * rho.real)) - np.sum(n ** (-2 * rho.real))
        est = N ** (1 - 2 * rho.real) / (2 * rho.real - 1)
        check(f'R2c ||v_rho||^2 -> zeta(2 Re rho), rho={rho}: truncation tail = N^(1-2s)/(2s-1) to 1%',
              abs(tail / est - 1) < 0.01, f'tail {tail:.3e} est {est:.3e}')
print('  (the joint eigenvector v_rho exists for every rho in the half plane; nothing selects the zeros)')
g1 = 14.134725141734693
g2 = g1 + 2 * np.pi / np.log(2)
r1, r2 = 0.5 + 1j * g1, 0.5 + 1j * g2
check('R2c one prime: p=2 gives p^{rho+conj rho2} = p although rho != rho2',
      abs(2 ** (r1 + np.conj(r2)) - 2) < 1e-12)
check('R2c the condition needs two primes: p=3 separates them', abs(3 ** (r1 + np.conj(r2)) - 3) > 0.1)

print('R3 local Lefschetz coefficients')


def coeff(A, k):
    """Deninger (34): det(1 - A^k) / |det(1 - A^{|k|})| on T_x F."""
    Ak = np.linalg.matrix_power(A, k) if k > 0 else np.linalg.matrix_power(np.linalg.inv(A), -k)
    Am = np.linalg.matrix_power(A, abs(k))
    return np.linalg.det(np.eye(2) - Ak) / abs(np.linalg.det(np.eye(2) - Am))


def sdet_form(A, k):
    if k > 0:
        B = np.linalg.matrix_power(A, k)
        strL = 1 - np.trace(B) + np.linalg.det(B)
        return strL / abs(np.linalg.det(np.eye(2) - B))
    B = np.linalg.matrix_power(A, -k)
    strL = 1 - np.trace(B) + np.linalg.det(B)
    return np.linalg.det(np.linalg.inv(B)) * strL / abs(np.linalg.det(np.eye(2) - B))


rng = np.random.default_rng(1)
for trial in range(3):
    B = rng.normal(size=(2, 2))
    check('R3 str Lambda^* B = det(1-B) (2x2)', abs(1 - np.trace(B) + np.linalg.det(B) - np.linalg.det(np.eye(2) - B)) < 1e-12)
l = np.log(7.0)
th = 1.1
R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
F = np.array([[np.cos(th), np.sin(th)], [np.sin(th), -np.cos(th)]])   # reflection
for name, O in (('rotation', R), ('reflection', F)):
    A = np.exp(l / 2) * O
    for k in list(range(1, 7)) + list(range(-6, 0)):
        c, c2 = coeff(A, k), sdet_form(A, k)
        check(f'R3 (34) = superdeterminant form, {name}, k={k}', abs(c - c2) < 1e-9 * max(1, abs(c)))
        if name == 'rotation':
            want = 1.0 if k > 0 else np.exp(k * l)
        else:
            want = (-1.0) ** k if k > 0 else np.exp(k * l)
        check(f'R3 {name} k={k}: c_k = {want:.4g}', abs(c - want) < 1e-9 * max(1, abs(want)), f'got {c:.6g}')
A = np.exp(l / 2) * F
check('R3 note says c_k = -1 for all k>=1 when det O = -1: FALSE at k=2', abs(coeff(A, 2) - 1) < 1e-9,
      f'c_2 = {coeff(A, 2):.6f}')
check('R3 reflection: negative-k coefficients equal the rotation ones (e^{kl})',
      all(abs(coeff(np.exp(l / 2) * F, k) - np.exp(k * l)) < 1e-12 for k in range(-6, 0)))

print('R3(c) Deuring by enumeration (all Weierstrass curves over F_p)')


def traces(p):
    tr = set()
    F = range(p)
    for a1, a2, a3, a4, a6 in itertools.product(F, repeat=5):
        b2 = (a1 * a1 + 4 * a2) % p
        b4 = (2 * a4 + a1 * a3) % p
        b6 = (a3 * a3 + 4 * a6) % p
        b8 = (a1 * a1 * a6 + 4 * a2 * a6 - a1 * a3 * a4 + a2 * a3 * a3 - a4 * a4) % p
        disc = (-b2 * b2 * b8 - 8 * b4 ** 3 - 27 * b6 * b6 + 9 * b2 * b4 * b6) % p
        if disc == 0:
            continue
        cnt = 1
        for x in F:
            for y in F:
                if (y * y + a1 * x * y + a3 * y - x ** 3 - a2 * x * x - a4 * x - a6) % p == 0:
                    cnt += 1
        tr.add(p + 1 - cnt)
    return tr


for p in (2, 3, 5, 7):
    tr = traces(p)
    want = {a for a in range(-2 * int(np.sqrt(p)) - 1, 2 * int(np.sqrt(p)) + 2) if a * a <= 4 * p}
    check(f'R3 Deuring p={p}: every |a| <= 2 sqrt p occurs', tr == want, f'{sorted(tr)}')
for p in (11, 13):     # short Weierstrass suffices for p > 3
    tr = set()
    for a4 in range(p):
        for a6 in range(p):
            if (4 * a4 ** 3 + 27 * a6 * a6) % p == 0:
                continue
            cnt = 1 + sum(1 for x in range(p) for y in range(p) if (y * y - x ** 3 - a4 * x - a6) % p == 0)
            tr.add(p + 1 - cnt)
    want = {a for a in range(-8, 9) if a * a <= 4 * p}
    check(f'R3 Deuring p={p}', tr == want, f'{sorted(tr)}')

print('R3 Reading: "by Honda-Tate an algebraic angle is an elliptic curve over F_p"')
x = sp.symbols('x')
Pw = x ** 4 + x ** 2 + 4
check('HT x^4+x^2+4 irreducible over Q', sp.Poly(Pw, x).is_irreducible)
roots = [complex(r) for r in sp.Poly(Pw, x).nroots()]
check('HT all roots have modulus sqrt 2 (a 2-Weil number of degree 4)', all(abs(abs(r) - np.sqrt(2)) < 1e-12 for r in roots))
check('HT b = 1 is prime to 2 (ordinary): Honda-Tate gives a simple ordinary abelian SURFACE over F_2',
      sp.Poly(Pw, x).all_coeffs()[2] % 2 == 1)
tr = sorted({round(2 * r.real, 12) for r in roots})
check('HT the angle pair has trace 2 sqrt2 cos(theta) = +-sqrt3, not an integer: no elliptic curve',
      all(abs(abs(t) - np.sqrt(3)) < 1e-9 for t in tr), f'{tr}')
a = 2 * np.sqrt(2) / 3            # cos theta = 1/3: algebraic angle, not a Weil number
mp_ = sp.minimal_polynomial(sp.sqrt(2) * (sp.Rational(1, 3) + sp.I * sp.sqrt(8) / 3), x)
check('HT cos(theta)=1/3, p=2: sqrt2 e^{i theta} is not an algebraic integer (primitive min poly not monic)', sp.Poly(mp_, x).LC() != 1,
      f'min poly {mp_}')

print('R5(b) measure bookkeeping on the elliptic solenoid, p = 5, pi = 1+2i')
p = 5
# 5-adic embedding with i -> root of x^2+1 = 2 mod 5, lifted
i5 = 2
for k in range(2, 12):
    m = 5 ** k
    i5 = (i5 - (i5 * i5 + 1) * pow(2 * i5, -1, m)) % m
pi5 = (1 + 2 * i5) % 5 ** 11
v = 0
while pi5 % 5 == 0:
    pi5 //= 5
    v += 1
check('R5b |pi|_5 = 1/5 under i -> 2 (pi a 5-adic uniformiser up to unit)', v == 1)
check('R5b |pi|^2 = 5 = p', abs(abs(1 + 2j) ** 2 - 5) < 1e-12)
flat_area = abs(1 / (1 + 2j)) ** 2          # z -> pi^{-1} z
haar = 5.0 ** v                              # y -> pi^{-1} y scales Haar by |pi^{-1}|_5
check('R5b gluing preserves flat-area x Haar (the invariant measure)', abs(flat_area * haar - 1) < 1e-12)
check('R5b gluing multiplies g-area x Haar by p (e^{log p} * p^{-1} * p): no finite measure from g-area',
      abs(np.exp(np.log(p)) * flat_area * haar - p) < 1e-12)
check('R5b g-area x (e^{-t} Haar dt) is gluing-invariant and flow-invariant (transverse measure scaled by e^{-s})',
      abs(np.exp(np.log(p)) * flat_area * np.exp(-np.log(p)) * haar - 1) < 1e-12)

print(f'\nscratch_den_r2r3: {ok} pass, {fail} fail')
