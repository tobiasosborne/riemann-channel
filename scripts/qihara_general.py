"""Ihara–Bass formula for the non-backtracking superoperator of an ARBITRARY Kraus family.

Setting. Superoperators E_1..E_D on M_n (any linear maps, not assumed unitary-conjugation,
not assumed invertible) and a fixed-point-free involution i -> ibar on {1..D}.  The edge
space is M_n (x) C^D and the non-backtracking operator is
    T(rho (x) |i>) = sum_{j != ibar} E_i(rho) (x) |j>.
Claim (notes/quantum-ihara-general.md, Theorem 1): for every u with all 1 - u^2 E_ibar E_i
invertible,
    det(1 - uT) = prod_{pairs {i,ibar}} det(1 - u^2 E_ibar E_i)
                  * det_{M_n}( 1 - u sum_i (E_i - u E_ibar E_i)(1 - u^2 E_ibar E_i)^{-1} ).
Both the 1 - u M(u) form (proof step <1>6) and the displayed 1 + D(u) - A(u) form are evaluated.
Cases: (b) Kraus pairing E_ibar = E_i^dagger (Hilbert-Schmidt adjoint), A_ibar = A_i^dagger, plus
the trace formula Tr T^m = sum over cyclically non-backtracking words of |Tr A_w|^2;
(b') canonical-form MPS tensors; (d) generic superoperators with a generic involution;
(c) D = 2, where T = E_1 (+) E_2; (a) E_ibar = E_i^{-1} recovers the unitary formula
det(1-uT) = (1-u^2)^{n^2(D-2)/2} det(1 - u D Phi + (D-1) u^2).
Checks: floating point with Haar/Gaussian data; exact rational arithmetic with sympy for
small (n, D)."""
import itertools, numpy as np, sympy as sp
rng = np.random.default_rng(7)

def ad(A):                       # superoperator rho -> A rho A^dagger, column stacking
    return np.kron(A.conj(), A)

def hashimoto(Es, inv):
    N = Es[0].shape[0]; D = len(Es); T = np.zeros((N*D, N*D), complex)
    for i in range(D):
        for j in range(D):
            if j != inv[i]: T[j*N:(j+1)*N, i*N:(i+1)*N] = Es[i]
    return T

def rhs(Es, inv, u):
    N = Es[0].shape[0]; I = np.eye(N); pairs = {tuple(sorted((i, inv[i]))) for i in range(len(Es))}
    pref = np.prod([np.linalg.det(I - u*u*Es[b]@Es[a]) for a, b in pairs])
    M = sum((Es[i] - u*Es[inv[i]]@Es[i]) @ np.linalg.inv(I - u*u*Es[inv[i]]@Es[i]) for i in range(len(Es)))
    Aop = u*sum(Es[i] @ np.linalg.inv(I - u*u*Es[inv[i]]@Es[i]) for i in range(len(Es)))          # displayed A(u)
    Dop = u*u*sum(Es[inv[i]]@Es[i] @ np.linalg.inv(I - u*u*Es[inv[i]]@Es[i]) for i in range(len(Es)))  # displayed D(u)
    r1, r2 = pref*np.linalg.det(I - u*M), pref*np.linalg.det(I + Dop - Aop)
    assert abs(r1/r2 - 1) < 1e-10, 'the two forms of the right-hand side disagree'
    return r2

def check(label, Es, inv, us=(0.13, 0.21+0.09j, -0.17)):
    T = hashimoto(Es, inv)
    worst = max(abs(np.linalg.det(np.eye(T.shape[0]) - u*T)/rhs(Es, inv, u) - 1) for u in us)
    print(f'{label}: max |lhs/rhs - 1| over u = {worst:.1e}')
    return worst

def trace_formula(Es, inv, m):
    D = len(Es); T = hashimoto(Es, inv); lhs = np.trace(np.linalg.matrix_power(T, m))
    tot = 0
    for w in itertools.product(range(D), repeat=m):
        if all(w[(k+1) % m] != inv[w[k]] for k in range(m)):
            P = np.eye(Es[0].shape[0])
            for i in w: P = Es[i] @ P
            tot += np.trace(P)
    return abs(lhs - tot)

# ---- (b) arbitrary Kraus operators, adjoint pairing -------------------------------------
n, m = 3, 2                       # D = 2m Kraus operators: A_1..A_m and their adjoints
As = [rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)) for _ in range(m)]
As = As + [A.conj().T for A in As]; D = len(As); inv = [(i+m) % D for i in range(D)]
Es = [ad(A)/2 for A in As]        # scaled so the u's are inside the convergence region
w1 = check(f'(b) Gaussian Kraus, adjoint pairing, n={n}, D={D}', Es, inv)
print(f'    trace formula m=1..4: max error {max(trace_formula(Es, inv, k) for k in range(1,5)):.1e}')

# ---- (b') canonical-form MPS: sum_i A_i^dagger A_i = 1 -------------------------------------
X = rng.normal(size=(2*n, n)) + 1j*rng.normal(size=(2*n, n)); Q, _ = np.linalg.qr(X)
Bs = [Q[:n], Q[n:]]               # isometry columns: B_1^dag B_1 + B_2^dag B_2 = 1
Bs = Bs + [B.conj().T for B in Bs]; invB = [(i+2) % 4 for i in range(4)]
w2 = check('(b\') canonical MPS tensors + adjoints, n=3, D=4', [ad(B) for B in Bs], invB)

# ---- (d) fully generic superoperators, generic involution (no adjoint relation at all) ----
Fs = [rng.normal(size=(n*n, n*n))/4 for _ in range(4)]; invF = [1, 0, 3, 2]
w3 = check('(d) generic real superoperators, involution (0 1)(2 3), n=3, D=4', Fs, invF)

# ---- (c) D = 2, a single pair: the total-cancellation case of Corollary 4 --------------
A2 = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); E2 = [ad(A2)/2, ad(A2.conj().T)/2]
w5 = check('(c) D=2 single Kraus pair, n=3', E2, [1, 0])
T2 = hashimoto(E2, [1, 0]); u = 0.19-0.05j     # for D=2, T = E_1 (+) E_2, so det(1-uT) factorises
w5 = max(w5, abs(np.linalg.det(np.eye(2*n*n) - u*T2)/(np.linalg.det(np.eye(n*n) - u*E2[0])*np.linalg.det(np.eye(n*n) - u*E2[1])) - 1))
print(f'    D=2: det(1-uT) = det(1-uE_1) det(1-uE_2): rel err {w5:.1e}')

# ---- (a) unitary case recovers the known formula ---------------------------------------
def haar(k):
    z = (rng.normal(size=(k, k)) + 1j*rng.normal(size=(k, k)))/np.sqrt(2); q, r = np.linalg.qr(z); return q*(np.diag(r)/abs(np.diag(r)))
Us = [haar(n) for _ in range(2)]; Us = Us + [U.conj().T for U in Us]; invU = [2, 3, 0, 1]
EU = [ad(U) for U in Us]; T = hashimoto(EU, invU); N = n*n; Dd = 4; Phi = sum(EU)/Dd
w4 = 0
for u in (0.13, 0.21+0.09j):
    lhs = np.linalg.det(np.eye(N*Dd) - u*T)
    old = (1-u*u)**(N*(Dd-2)/2)*np.linalg.det(np.eye(N) - u*Dd*Phi + (Dd-1)*u*u*np.eye(N))
    w4 = max(w4, abs(lhs/old - 1), abs(rhs(EU, invU, u)/old - 1))
print(f'(a) unitary Kraus: new formula vs (1-u^2)^(n^2(D-2)/2) det(1-uDPhi+(D-1)u^2): max rel err {w4:.1e}')

# ---- exact rational check with sympy: n=1 (scalars) D=4 and n=2 D=4 --------------------
u = sp.symbols('u')
def exact_check(N, D, inv):
    Es = [sp.Matrix(N, N, lambda a, b: sp.Rational(rng.integers(-3, 4), rng.integers(1, 4))) for _ in range(D)]
    T = sp.zeros(N*D, N*D)
    for i in range(D):
        for j in range(D):
            if j != inv[i]: T[j*N:(j+1)*N, i*N:(i+1)*N] = Es[i]
    lhs = (sp.eye(N*D) - u*T).det()
    pairs = {tuple(sorted((i, inv[i]))) for i in range(D)}
    pref = sp.prod([(sp.eye(N) - u**2*Es[b]*Es[a]).det() for a, b in pairs])
    M = sum(((Es[i] - u*Es[inv[i]]*Es[i]) * (sp.eye(N) - u**2*Es[inv[i]]*Es[i]).inv() for i in range(D)), sp.zeros(N, N))
    r = pref*(sp.eye(N) - u*M).det()
    return sp.simplify(lhs - r) == 0
print('exact (sympy, rational entries): N=1,D=4:', exact_check(1, 4, [1, 0, 3, 2]), ' N=2,D=4:', exact_check(2, 4, [1, 0, 3, 2]), ' N=2,D=6:', exact_check(2, 6, [1, 0, 3, 2, 5, 4]))
print('ALL FLOAT CHECKS PASS' if max(w1, w2, w3, w4, w5) < 1e-10 else 'FLOAT CHECK FAILURE')
