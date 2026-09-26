#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane P, item P3 and the counts used in P4: FCS parametrisation, Choi convention,
energy polynomial (P4.6), compactness trace identity, direct-sum embedding, parameter counts. numpy. Deterministic."""
import numpy as np, itertools, math
ok = 0; bad = 0
def chk(name, cond):
    global ok, bad
    if cond: ok += 1; print("PASS", name)
    else: bad += 1; print("FAIL", name)
rng = np.random.default_rng(7)
q = 2
Sx = np.array([[0, 1], [1, 0]]) / 2; Sy = np.array([[0, -1j], [1j, 0]]) / 2; Sz = np.array([[1, 0], [0, -1]]) / 2
h = (np.kron(Sx, Sx) + np.kron(Sy, Sy) + np.kron(Sz, Sz)).real
chk("h matches the report's 4x4 matrix", np.allclose(h, [[.25, 0, 0, 0], [0, -.25, .5, 0], [0, .5, -.25, 0], [0, 0, 0, .25]]))
chk("sum |entries of 4h| = 8", abs(np.abs(4 * h).sum() - 8) < 1e-12)

def random_unital_cp(d, nk=3):
    # E(X) = V^dag (X) V, V: C^d -> C^q (x) C^d (x) C^nk isometry
    Z = rng.normal(size=(q * d * nk, d)) + 1j * rng.normal(size=(q * d * nk, d))
    V, _ = np.linalg.qr(Z)
    def E(X):   # X on C^q (x) C^d
        return V.conj().T @ np.kron(X, np.eye(nk)) @ V
    return E

for d in [2, 3]:
    E = random_unital_cp(d)
    # stationary rho: rho(E(I (x) X)) = rho(X)
    basis = [np.outer(np.eye(d)[a], np.eye(d)[c]) for a in range(d) for c in range(d)]
    Mt = np.array([[np.trace(basis[r].conj().T @ E(np.kron(np.eye(q), basis[s]))) for s in range(d * d)] for r in range(d * d)])
    # E_1 in the matrix-unit basis; left fixed vector of the dual
    w, vl = np.linalg.eig(Mt.T)
    k = np.argmin(abs(w - 1)); rv = vl[:, k]
    rho = rv.reshape(d, d).T.conj()  # rho(X) = tr(rho X); we fix normalisation below
    # solve directly instead: find rho with tr(rho E1(X)) = tr(rho X) for all X via least squares
    A = np.array([[np.trace(np.outer(np.eye(d)[b_], np.eye(d)[z_]).T @ (E(np.kron(np.eye(q), basis[s])) - basis[s]))
                   for b_ in range(d) for z_ in range(d)] for s in range(d * d)])
    ns = np.linalg.svd(A)[2].conj()[-1]
    rho = ns.reshape(d, d)                       # rho[b,z] multiplies X[b,z]?  convert: tr(rho X) = sum rho[z,b] X[b,z]
    rho = rho.T
    rho = rho / np.trace(rho)
    rho = (rho + rho.conj().T) / 2
    chk("d=%d stationary boundary state is PSD" % d, np.linalg.eigvalsh(rho).min() > -1e-10)
    chk("d=%d stationarity rho(E(I x X)) = rho(X)" % d, max(abs(np.trace(rho @ E(np.kron(np.eye(q), B))) - np.trace(rho @ B)) for B in basis) < 1e-10)
    # Choi in the report's convention J_{(i,a,b),(j,c,z)} = E(|i><j| (x) |a><c|)_{bz}
    n = q * d * d
    J = np.zeros((n, n), complex)
    for i, a, j, c in itertools.product(range(q), range(d), range(q), range(d)):
        Eij = E(np.kron(np.outer(np.eye(q)[i], np.eye(q)[j]), np.outer(np.eye(d)[a], np.eye(d)[c])))
        for b_, z_ in itertools.product(range(d), range(d)):
            J[(i * d + a) * d + b_, (j * d + c) * d + z_] = Eij[b_, z_]
    chk("d=%d Choi Hermitian PSD" % d, np.allclose(J, J.conj().T) and np.linalg.eigvalsh(J).min() > -1e-10)
    chk("d=%d tr J = tr E(I) = d (compactness bound)" % d, abs(np.trace(J) - d) < 1e-10)
    # energy by (P4.6)
    Jt = J.reshape(q, d, d, q, d, d)   # (i,a,b),(j,c,z)
    hh = h.reshape(q, q, q, q)          # h_{(i,k),(j,l)} -> hh[i,k,j,l]
    e46 = 0
    for i, k_, j, l in itertools.product(range(q), repeat=4):
        if hh[i, k_, j, l] == 0: continue
        Y = np.einsum('tatc->ac', Jt[k_, :, :, l, :, :])          # sum_t J_{(k,t,a),(l,t,c)}
        Z = np.einsum('ac,abcz->bz', Y, Jt[i, :, :, j, :, :])
        e46 += hh[i, k_, j, l] * np.einsum('zb,bz->', rho, Z)
    # direct FCS: omega(A (x) B) = rho(E_A(E_B(1)))
    def omega2(X):   # X on C^q (x) C^q
        tot = 0
        for i, k_, j, l in itertools.product(range(q), repeat=4):
            coef = X[i * q + k_, j * q + l]
            if coef == 0: continue
            Ai = np.outer(np.eye(q)[i], np.eye(q)[j]); Bk = np.outer(np.eye(q)[k_], np.eye(q)[l])
            tot += coef * np.trace(rho @ E(np.kron(Ai, E(np.kron(Bk, np.eye(d))))))
        return tot
    chk("d=%d energy polynomial (P4.6) = direct FCS expectation (|diff| %.1e)" % (d, abs(e46 - omega2(h))), abs(e46 - omega2(h)) < 1e-10)
    chk("d=%d energy >= Hulthen value 1/4 - log 2" % d, omega2(h).real >= 0.25 - np.log(2) - 1e-12)
    # translation invariance / consistency: omega(I (x) A) = omega(A (x) I) = rho(E_A(1))
    Arand = rng.normal(size=(q, q)); Arand = Arand + Arand.T
    one = np.trace(rho @ E(np.kron(Arand, np.eye(d))))
    chk("d=%d TI consistency omega(A x I) = omega(I x A) = omega(A)" % d, abs(omega2(np.kron(Arand, np.eye(q))) - one) < 1e-10 and abs(omega2(np.kron(np.eye(q), Arand)) - one) < 1e-10)

# ---- direct-sum embedding (P4 step 6): classical C (+) C (dim 2) into M_2 via pinching; local expectations agree
p0 = np.array([[0.7, 0.3], [0.4, 0.6]])       # Markov chain, rows sum 1
Ms = [np.diag([0.9, 0.1]), np.diag([0.2, 0.8])]  # emission densities per hidden state (commuting diagonal case)
# E((A (x) X))_a = sum_b P[a,b] tr(Ms_a A) X_b  (a classical FCS / HMM), unital
def Ecl(A, X):  # X diagonal vector -> vector
    return np.array([sum(p0[a, b] * np.trace(Ms[a] @ A) * X[b] for b in range(2)) for a in range(2)])
w, v = np.linalg.eig(p0.T); pi = np.real(v[:, np.argmin(abs(w - 1))]); pi = pi / pi.sum()
def Eemb(A, X):  # on M_2: pinch, apply, include
    return np.diag(Ecl(A, np.diag(X)))
A1 = np.array([[1, 2], [2, -1]]); A2 = np.array([[0, 1], [1, 3]])
v_cl = pi @ Ecl(A1, Ecl(A2, np.ones(2)))
v_em = np.trace(np.diag(pi) @ Eemb(A1, Eemb(A2, np.eye(2))))
chk("direct-sum algebra embedded in M_d by pinching reproduces local expectations", abs(v_cl - v_em) < 1e-12)

# ---- counts used in P4
for d in [2, 3, 4, 8]:
    M = 2 * d * d
    k = M * M + d * d + 1; s = (2 ** M - 1) + (2 ** d - 1) + d * d + d * d + 1 + 1
    chk("d=%d k_d = 4d^4 + d^2 + 1 = %d, s_d = 2^{2d^2} + 2^d + 2d^2" % (d, k), k == 4 * d**4 + d**2 + 1 and s == 2 ** (2 * d * d) + 2 ** d + 2 * d * d)
    # input-length bounds, exact integers: minors 2^M M!, unital 2d+1, stationary 8d^2+2, energy graph 64 d^5 + 5
    tau = 32 * d**4
    chk("d=%d every input length < 2^tau_d" % d, max(2 ** M * math.factorial(M), 2 * d + 1, 8 * d * d + 2, 64 * d**5 + 5) < 2 ** tau)
# tuple count: sum_{a,b} (q n_a n_b)^2 = q^2 m^2
for tup in [(1,), (1, 1), (2, 1), (1, 1, 1), (2, 2, 1)]:
    m = sum(t * t for t in tup)
    chk("Choi coordinate count q^2 m^2 for tuple %s" % (tup,), sum((q * a * b) ** 2 for a in tup for b in tup) == q * q * m * m)
print("checks passed %d failed %d" % (ok, bad))
