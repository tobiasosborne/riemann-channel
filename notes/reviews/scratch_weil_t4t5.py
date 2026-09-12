#!/usr/bin/env python3
"""Independent checks of astra-proofs T4.1-T4.5 and T5.1-T5.3.
Reviewer claude:opus, 2026-09-12.  Own code; no reuse of scripts/weil_positivity.py."""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import expm
rng = np.random.default_rng(31415)

print("=" * 78); print("T4.1  hhat(xi) = 2b/(b^2+(xi-om)^2)  and its inverse (Lorentzian density)"); print("=" * 78)
b, om = 0.7, 2.0
t = np.linspace(-300, 300, 3000001); dt = t[1] - t[0]
h = np.exp(-b * np.abs(t) + 1j * om * t)
for xi in [0.0, 1.0, -2.5]:
    num = (h * np.exp(-1j * xi * t)).sum() * dt
    exact = 2 * b / (b ** 2 + (xi - om) ** 2)
    print(f"  b={b} om={om} xi={xi:+}: numeric {num.real:+.8f}{num.imag:+.1e}i   exact {exact:+.8f}   diff {abs(num-exact):.2e}")
xi = np.linspace(-6000, 6000, 6000001); dxi = xi[1] - xi[0]
for tt in [0.0, 0.8, -1.7]:
    inv = (np.exp(1j * tt * xi) * b / (np.pi * (b ** 2 + (xi - om) ** 2))).sum() * dxi
    exact = np.exp(-b * abs(tt) + 1j * om * tt)
    print(f"  inverse representation at t={tt:+}: {inv.real:+.8f}{inv.imag:+.6f}i   exact {exact.real:+.8f}{exact.imag:+.6f}i   diff {abs(inv-exact):.2e}")

print(); print("=" * 78); print("T4.2  F positive definite  <=>  Re rho <= a"); print("=" * 78)
def F_of(A, a):
    def F(v):
        if v >= 0: return sum(np.exp(v * (r - a)) for r in A)
        return np.conj(sum(np.exp(-v * (r - a)) for r in A))
    return F
def mineig_gram(A, a, T, m=24):
    F = F_of(A, a); ts = np.linspace(0, T, m)
    G = np.array([[F(ts[j] - ts[k]) for k in range(m)] for j in range(m)])
    return np.linalg.eigvalsh((G + G.conj().T) / 2).min()
for trial in range(5):
    A = list(rng.normal(size=4) * 0.8 + 1j * rng.normal(size=4) * 2)
    mx = max(r.real for r in A)
    for off in (+0.30, +0.02, -0.02, -0.30):
        a = mx + off
        res = [f"T={T}:{mineig_gram(A,a,T):+.2e}" for T in (10, 40, 160)]
        verdict = all(float(s.split(':')[1]) > -1e-8 for s in res)
        print(f"  trial {trial}  a - max Re rho = {off:+.2f}  ->  {'  '.join(res)}   PSD={verdict}")
print("  (the sign of a - max Re rho decides; near the threshold a longer window is needed)")

print(); print("=" * 78); print("T4.3  line duality: sum c_j bar c_k F(t_j-t_k) == sum_rho ghat(rho) conj ghat(2a - conj rho)"); print("=" * 78)
for trial in range(5):
    a = rng.normal(); A = []
    for _ in range(3):
        r = a + rng.normal() * 0.7 + 1j * rng.normal() * 2
        A += [r, 2 * a - np.conj(r)]
    A += [a + 1j * rng.normal()]
    ts = rng.normal(size=5) * 3; c = rng.normal(size=5) + 1j * rng.normal(size=5)
    F = F_of(A, a)
    W = sum(c[j] * np.conj(c[k]) * F(ts[j] - ts[k]) for j in range(5) for k in range(5))
    gh = lambda r: sum(c[j] * np.exp(ts[j] * (r - a)) for j in range(5))
    M = sum(gh(r) * np.conj(gh(2 * a - np.conj(r))) for r in A)
    print(f"  a={a:+.4f}: W={W.real:+.6e}{W.imag:+.1e}i  M={M.real:+.6e}{M.imag:+.1e}i  |W-M|={abs(W-M):.2e}")

print(); print("=" * 78); print("T4.4  Dyson expansion: free propagators between jumps are essential"); print("=" * 78)
n = 2
K = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
Rs = [rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)) for _ in range(2)]
Ad = lambda B: np.kron(B.conj(), B)
L0 = np.kron(np.eye(n), K) + np.kron(K.conj(), np.eye(n))
Q = sum(Ad(R) for R in Rs); Lg = L0 + Q
def dyson_term_exact(k, t):
    """k-th Dyson term as a superoperator, via the nilpotent block trick."""
    m = L0.shape[0]; M = np.zeros(((k + 1) * m, (k + 1) * m), dtype=complex)
    for i in range(k + 1): M[i*m:(i+1)*m, i*m:(i+1)*m] = L0
    for i in range(k): M[i*m:(i+1)*m, (i+1)*m:(i+2)*m] = Q
    return expm(t * M)[0:m, k*m:(k+1)*m]
gx, gw = leggauss(60)
def simplex_trace(k, t):
    """sum_j int_{0<t_1<..<t_k<t} |Tr A|^2, A = e^{(t-t_k)K} R_{j_k} ... R_{j_1} e^{t_1 K}."""
    if k == 0: return abs(np.trace(expm(t * K))) ** 2
    if k == 1:
        s = (gx + 1) * t / 2; w = gw * t / 2; tot = 0.0
        for j, R in enumerate(Rs):
            for si, wi in zip(s, w):
                Amat = expm((t - si) * K) @ R @ expm(si * K)
                tot += wi * abs(np.trace(Amat)) ** 2
        return tot
    if k == 2:
        tot = 0.0
        s2 = (gx + 1) * t / 2; w2 = gw * t / 2
        for j2, R2 in enumerate(Rs):
            for j1, R1 in enumerate(Rs):
                for b_, wb in zip(s2, w2):
                    s1 = (gx + 1) * b_ / 2; w1 = gw * b_ / 2
                    for a_, wa in zip(s1, w1):
                        Amat = expm((t - b_) * K) @ R2 @ expm((b_ - a_) * K) @ R1 @ expm(a_ * K)
                        tot += wb * wa * abs(np.trace(Amat)) ** 2
        return tot
for t in (0.05, 0.2, 0.5):
    ex = [np.trace(dyson_term_exact(k, t)).real for k in (0, 1, 2)]
    qd = [simplex_trace(k, t) for k in (0, 1, 2)]
    # k=1 collapses (the two free propagators recombine by cyclicity), so the draft's omission
    # first bites at k=2: without propagators the integrand would be |Tr(R_{j2} R_{j1} e^{tK})|^2.
    naive2 = (t ** 2 / 2) * sum(abs(np.trace(R2 @ R1 @ expm(t * K))) ** 2 for R2 in Rs for R1 in Rs)
    tot = np.trace(expm(t * Lg)).real
    print(f"  t={t}:  Tr e^{{tL}} = {tot:.8f};  Dyson traces k=0,1,2 exact = {[f'{v:.8f}' for v in ex]}")
    print(f"         ring-norm quadrature      k=0,1,2       = {[f'{v:.8f}' for v in qd]}  (max diff {max(abs(e-q) for e,q in zip(ex,qd)):.2e})")
    print(f"         partial sum k<=2 = {sum(ex):.8f}   remainder = {tot-sum(ex):+.2e}")
    print(f"         k=2 term WITHOUT the free propagators between jumps = {naive2:.8f}  (vs exact {ex[2]:.8f}) -> draft form is wrong")
print(f"  conjugation symmetry of L: d(spec, conj spec) = ", end="")
sp = np.linalg.eigvals(Lg); b_ = list(np.conj(sp)); w = 0.0
for x in sp:
    i = int(np.argmin([abs(x - y) for y in b_])); w = max(w, abs(x - b_[i])); b_.pop(i)
tt = np.linspace(0, 3, 61); tr = np.array([np.trace(expm(x * Lg)) for x in tt])
print(f"{w:.2e};  Tr e^{{tL}} on t in [0,3]: min Re = {tr.real.min():.6f} > 0, "
      f"max |Im|/|Tr| = {np.abs(tr.imag / np.abs(tr)).max():.2e}")

print(); print("=" * 78); print("T5.1 / T5.3  unitarizability vs Jordan blocks"); print("=" * 78)
r = 1.3; X = r * np.array([[1.0, 1.0], [0.0, 1.0]])
nul = [np.trace(np.linalg.matrix_power(X / r, l)).real for l in range(0, 41)]
print(f"  X = r[[1,1],[0,1]]:  nu_l for l=0..6 = {nul[:7]}  (all 2)")
full = np.array(nul + [0] * 0); L = 40
v = np.array([nul[abs(k)] for k in range(-L, L + 1)], dtype=complex)
idx = np.arange(L + 1); Kk = idx[:, None] - idx[None, :]
print(f"  min eig of the Weil/Toeplitz form (L={L}) = {np.linalg.eigvalsh(v[Kk+L].real).min():+.3e}  -> positive definite")
print(f"  ||(X/r)^k e_2|| in the standard inner product, k=1,10,100: "
      f"{[float(np.linalg.norm(np.linalg.matrix_power(X/r,k)@np.array([0,1.0]))) for k in (1,10,100)]}  -> unbounded, so no unitarising inner product")
# T5.1 sufficiency: diagonalisable with |mu| = r  =>  an inner product making X/r unitary
P = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
Dg = np.diag(np.exp(1j * rng.normal(size=3))) * r
Y = P @ Dg @ np.linalg.inv(P)
G = np.linalg.inv(P @ P.conj().T)        # <x,y>' = x^dag G y makes the columns of P orthonormal
U = Y / r
print(f"  T5.1: |U^dag G U - G| for a random diagonalisable Y with |mu|=r : {np.abs(U.conj().T@G@U - G).max():.2e}")
