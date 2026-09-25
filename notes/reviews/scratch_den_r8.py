"""REFUTE lane for notes/deninger-cmps/reformulation.md, Proposition R8 (and R6(a)).
Independent: imports nothing from scripts/.  Run from the repository root.

 1. c Ad(U) with c != 1 is not multiplicative; a nonzero multiplicative map is unital; X -> A X A^dag (A invertible,
    not unitary) is not multiplicative; X -> A X A^{-1} is multiplicative but not CP (Choi matrix indefinite).
 2. R6(a)'s identification V (x) Vbar = Lambda^*(C dz + C dzbar) = H^*(T^2) (thm:hodge-doubling-tensor): the doubled
    transfer diag(1, conj pi, pi, p) = A (x) conj A with A = diag(1, pi) is a ring automorphism of the EXTERIOR
    (cup) product, although A is not a scalar times a unitary.  So R8(c)'s class is not "exactly" the scalar-times-
    automorphism transfers: the product that Deninger's mechanism uses is the cup product, not composition in End(V).
"""
import numpy as np

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


rng = np.random.default_rng(3)


def rand_c(n):
    return rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))


def rand_u(n):
    q, r = np.linalg.qr(rand_c(n))
    return q * (np.diag(r) / abs(np.diag(r)))


n = 3
X, Y = rand_c(n), rand_c(n)
U = rand_u(n)
for c in (2.0, 5.0):
    E = lambda Z: c * U @ Z @ U.conj().T
    check(f'1. c Ad(U), c={c}: E(XY) != E(X)E(Y)', not np.allclose(E(X @ Y), E(X) @ E(Y)))
    check(f'1. c Ad(U), c={c}: E(XY) = c^-1 E(X)E(Y) (projectively multiplicative only)', np.allclose(E(X @ Y), E(X) @ E(Y) / c))
E = lambda Z: U @ Z @ U.conj().T
check('1. Ad(U) multiplicative and unital', np.allclose(E(X @ Y), E(X) @ E(Y)) and np.allclose(E(np.eye(n)), np.eye(n)))
A = np.diag([1.0, 1 + 2j, 0.3])
E = lambda Z: A @ Z @ A.conj().T
check('1. X -> A X A^dag, A invertible non-unitary: not multiplicative', not np.allclose(E(X @ Y), E(X) @ E(Y)))
Ainv = np.linalg.inv(A)
E = lambda Z: A @ Z @ Ainv
check('1. X -> A X A^{-1} is multiplicative', np.allclose(E(X @ Y), E(X) @ E(Y)))
# Choi matrix of X -> A X A^{-1}
Ch = np.zeros((n * n, n * n), complex)
for i in range(n):
    for j in range(n):
        Eij = np.zeros((n, n)); Eij[i, j] = 1
        Ch += np.kron(Eij, E(Eij))
ev = np.linalg.eigvalsh((Ch + Ch.conj().T) / 2)
check('1. ... but not CP unless A is a scalar times a unitary: Choi matrix indefinite or non-Hermitian',
      (not np.allclose(Ch, Ch.conj().T)) or ev.min() < -1e-9)

print('2. the cup product on the doubled bond (R6(a)) versus composition in End(V)')
p = 5
pi = 1 + 2j
# exterior algebra on (e1 = dz, e2 = dzbar): basis 1, e1, e2, e12 ; product table
def wedge(u, v):
    # u, v coefficient vectors on (1, e1, e2, e12)
    a0, a1, a2, a3 = u
    b0, b1, b2, b3 = v
    return np.array([a0 * b0,
                     a0 * b1 + a1 * b0,
                     a0 * b2 + a2 * b0,
                     a0 * b3 + a3 * b0 + a1 * b2 - a2 * b1])


F = np.diag([1, pi, np.conj(pi), p])          # pi^* on (1, dz, dzbar, dz^dzbar)
okm = True
for _ in range(20):
    u = rng.normal(size=4) + 1j * rng.normal(size=4)
    v = rng.normal(size=4) + 1j * rng.normal(size=4)
    okm &= np.allclose(F @ wedge(u, v), wedge(F @ u, F @ v))
check('2. pi^* = diag(1, pi, conj pi, p) is a ring automorphism of Lambda^*(dz, dzbar) (cup product)', okm)
Ak = np.diag([1, pi])
Edb = np.kron(Ak, np.conj(Ak))                # thm:hodge-doubling-tensor: basis (1, dzbar, dz, dz^dzbar)
check('2. A (x) conj A = diag(1, conj pi, pi, p) = thm:hodge-doubling-tensor', np.allclose(Edb, np.diag([1, np.conj(pi), pi, p])))
E = lambda Z: Ak @ Z @ Ak.conj().T            # the same map on End(V), V = C + C dz
X2, Y2 = rand_c(2), rand_c(2)
check('2. the same doubled transfer, read on End(V) with composition, is NOT multiplicative',
      not np.allclose(E(X2 @ Y2), E(X2) @ E(Y2)))
sv = np.linalg.svd(Ak, compute_uv=False)
check('2. A = diag(1, pi) is not a scalar times a unitary (singular values 1 and sqrt 5)', abs(sv.max() / sv.min() - np.sqrt(5)) < 1e-12)
# odd sector restriction is sqrt p times a unitary: (HP) on the odd sector
odd = np.diag([np.conj(pi), pi]) / np.sqrt(p)
check('2. odd-sector restriction / sqrt p is unitary ((HP) holds on the odd sector) without the channel being c Ad(U)',
      np.allclose(odd @ odd.conj().T, np.eye(2)))

print(f'\nscratch_den_r8: {ok} pass, {fail} fail')
