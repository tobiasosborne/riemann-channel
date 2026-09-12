#!/usr/bin/env python3
"""Independent checks of astra-proofs T3.1-T3.5 (Kraus dichotomy).
Reviewer claude:opus, 2026-09-12.  Own construction of T, no reuse of scripts/weil_positivity.py."""
import numpy as np, itertools, sympy as sp
rng = np.random.default_rng(5150)

def Ad(B):                      # column stacking: vec(B X B^dag) = (conj(B) kron B) vec(X)
    return np.kron(B.conj(), B)

def transfer(Bs, rev):
    """T on V tensor C^D with T(v ox |i>) = sum_{j != rev[i]} Ad(B_i) v ox |j>."""
    D = len(Bs); N = Bs[0].shape[0] ** 2
    T = np.zeros((D * N, D * N), dtype=complex)
    for i in range(D):
        Ei = Ad(Bs[i])
        for j in range(D):
            if j != rev[i]:
                T[j*N:(j+1)*N, i*N:(i+1)*N] = Ei
    return T

def match(a, b):
    """max over a of nearest distance in b (greedy multiset matching)."""
    b = list(b); worst = 0.0
    for x in a:
        k = int(np.argmin([abs(x - y) for y in b])); worst = max(worst, abs(x - b[k])); b.pop(k)
    return worst

def nu_toeplitz_mineig(A, r, L):
    z = np.array(A) / r
    nul = np.array([np.sum(z ** l) if l > 0 else complex(len(z)) for l in range(L + 1)])
    full = np.concatenate([np.conj(nul[:0:-1]), nul])
    idx = np.arange(L + 1); K = idx[:, None] - idx[None, :]
    M = full[K + L]
    return np.linalg.eigvalsh((M + M.conj().T) / 2).min()

print("=" * 78); print("T3.1  conjugation closure and HS self-adjointness"); print("=" * 78)
for n, m in [(2, 2), (2, 3), (3, 2)]:
    D = 2 * m; rev = {i: (i + m) % D for i in range(D)}
    Bs = [rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)) for _ in range(m)]
    Bs = Bs + [B.conj().T for B in Bs]                      # ADJOINT pairing
    T = transfer(Bs, rev); sp_T = np.linalg.eigvals(T)
    Sig = sum(Ad(B) for B in Bs)
    print(f"  n={n} D={D} adjoint-paired: d(spec T, conj spec T) = {match(sp_T, np.conj(sp_T)):.2e}"
          f"   |Sigma - Sigma^dag| = {np.abs(Sig - Sig.conj().T).max():.2e}"
          f"   max |Im spec(T)| = {np.abs(sp_T.imag).max():.3f}   max |Im spec(Sigma)| = {np.abs(np.linalg.eigvals(Sig).imag).max():.2e}")
    # ring traces for an arbitrary (unpaired) Ad family
    Bs2 = [rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)) for _ in range(D)]   # NO pairing at all
    T2 = transfer(Bs2, rev)
    tr = [np.trace(np.linalg.matrix_power(T2, l)) for l in range(1, 6)]
    word = []
    for l in range(1, 6):
        s = 0.0
        for w in itertools.product(range(D), repeat=l):
            if any(w[(k + 1) % l] == rev[w[k]] for k in range(l)): continue
            M = np.eye(n)
            for i in w: M = Bs2[i] @ M
            s += abs(np.trace(M)) ** 2
        word.append(s)
    print(f"     UNPAIRED Ad family: Tr T^l (l=1..5) = {[f'{t.real:.4f}{t.imag:+.1e}i' for t in tr]}")
    print(f"     word sum sum_w |Tr B_w|^2       = {[f'{w:.4f}' for w in word]}   -> X2(a) holds without any pairing")

print(); print("=" * 78); print("T3.2  inverse pairing: det(xI-T) = (x^2-1)^k prod (x^2 - alpha x + q)^{a_alpha}"); print("=" * 78)
for n, m in [(2, 2), (2, 3), (3, 2)]:
    D = 2 * m; q = D - 1; rev = {i: (i + m) % D for i in range(D)}
    N = n * n; k = N * (D - 2) // 2
    Bs = [rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)) for _ in range(m)]
    Bs = Bs + [np.linalg.inv(B) for B in Bs]                # INVERSE pairing
    T = transfer(Bs, rev); Sig = sum(Ad(B) for B in Bs)
    al = np.linalg.eigvals(Sig)
    pred = [1.0] * k + [-1.0] * k
    for a in al:
        disc = np.sqrt(complex(a * a - 4 * q))
        pred += [(a + disc) / 2, (a - disc) / 2]
    spT = np.linalg.eigvals(T)
    A0 = sorted(spT, key=lambda z: -abs(z))[: 2 * N]        # remove the k copies of +-1 by matching
    rem = list(spT); S0 = [1.0] * k + [-1.0] * k
    for s in S0:
        j = int(np.argmin([abs(s - y) for y in rem])); rem.pop(j)
    print(f"  n={n} D={D} q={q}: match(spec T, predicted) = {match(spT, pred):.2e};"
          f"  removal residual for S_0 = {max(abs(abs(x)-1) for x in [z for z in spT if min(abs(z-1),abs(z+1))<1e-6][:2*k]) if k else 0:.1e}")
    print(f"     retained A_0: {len(rem)} modes (2N = {2*N}); d(A_0, q/A_0) = {match(rem, [q/z for z in rem]):.2e};"
          f"  d(A_0, conj A_0) = {match(rem, np.conj(rem)):.2e}")
    print(f"     max |Im spec(Sigma)| = {np.abs(al.imag).max():.4f}  (inverse pairing does NOT make Sigma self-adjoint:"
          f" |Sigma-Sigma^dag| = {np.abs(Sig-Sig.conj().T).max():.3f})")

print("  astra's explicit example B_1=diag(2i,1), B_3=B_1^{-1}, B_2=B_4=I:")
B1 = np.diag([2j, 1]); Bs = [B1, np.eye(2), np.linalg.inv(B1), np.eye(2)]
Sig = sum(Ad(B) for B in Bs); print("     spec(Sigma) =", np.round(np.linalg.eigvals(Sig), 6),
                                    "  (astra: 25/4, 4, 2+-3i/2)")

print(); print("=" * 78); print("T3.3  Ad(B^dag) = Ad(B)^{-1}  iff  B^dag B = I"); print("=" * 78)
for B, lab in [(2 * np.eye(2), "2*I"), (np.array([[0, 1], [1, 0]], dtype=complex), "swap (unitary)"),
               (np.diag([1, 2]).astype(complex), "diag(1,2)")]:
    lhs = Ad(B.conj().T); rhs = np.linalg.inv(Ad(B))
    print(f"  B = {lab:<16} |Ad(B^dag) - Ad(B)^-1| = {np.abs(lhs-rhs).max():.4f}"
          f"   |B^dag B - I| = {np.abs(B.conj().T@B-np.eye(2)).max():.4f}"
          f"   |Ad(B^dag)-kappa Ad(B)^-1| with kappa=|c|^4: {np.abs(lhs-16*rhs).max():.2e}" if lab=="2*I"
          else f"  B = {lab:<16} |Ad(B^dag) - Ad(B)^-1| = {np.abs(lhs-rhs).max():.4f}   |B^dag B - I| = {np.abs(B.conj().T@B-np.eye(2)).max():.4f}")

print(); print("=" * 78); print("T3.4  unitary families: Weil positivity == Hastings bound"); print("=" * 78)
def haar(n, rng):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2)
    Q, R = np.linalg.qr(z); return Q @ np.diag(np.diag(R) / abs(np.diag(R)))
for trial in range(8):
    n, m = (2, 2) if trial % 2 == 0 else (2, 3)
    D = 2 * m; q = D - 1; N = n * n; k = N * (D - 2) // 2; rev = {i: (i + m) % D for i in range(D)}
    Us = [haar(n, rng) for _ in range(m)]; Bs = Us + [U.conj().T for U in Us]
    T = transfer(Bs, rev); Phi = sum(Ad(B) for B in Bs) / D
    lam = np.sort(np.linalg.eigvals(Phi).real)
    dp = int(np.sum(np.abs(lam - 1) < 1e-9)); dm = int(np.sum(np.abs(lam + 1) < 1e-9))
    S = [1.0] * k + [-1.0] * k + [float(q)] * dp + [1.0] * dp + [-float(q)] * dm + [-1.0] * dm
    rem = list(np.linalg.eigvals(T))
    for s in S:
        j = int(np.argmin([abs(s - y) for y in rem])); rem.pop(j)
    nontriv = [l for l in lam if abs(abs(l) - 1) > 1e-9]
    bound = (max(abs(np.array(nontriv))) if nontriv else 0.0) <= 2 * np.sqrt(q) / D + 1e-12
    me = nu_toeplitz_mineig(rem, np.sqrt(q), 60)
    circ = max(abs(abs(z) - np.sqrt(q)) for z in rem) if rem else 0.0
    print(f"  n={n} D={D}: |S|={len(S)} retained={len(rem)} (2(N-d+-d-)={2*(N-dp-dm)})  max|lam| off +-1 = "
          f"{max(abs(np.array(nontriv))) if nontriv else 0:.4f} vs {2*np.sqrt(q)/D:.4f} -> bound={bound};"
          f"  max||mu|-r| = {circ:.2e};  min eig Weil(L=60) = {me:+.3e} -> PSD={me > -1e-8}")

print(); print("=" * 78); print("T3.5  the n=2 D=4 adjoint-paired example with no reciprocal duality"); print("=" * 78)
x, a = sp.symbols('x a')
Ta = sp.Matrix([[a, 1, 0, 1], [a, 1, a, 0], [0, 1, a, 1], [a, 0, a, 1]])
cp = sp.factor(sp.expand(Ta.charpoly(x).as_expr()))
print("  char poly of T_a (symbolic) =", cp)
print("  astra's claim               =", sp.factor((x - a) * (x - 1) * (x**2 - (a + 1) * x - 3 * a)))
print("  difference =", sp.simplify(cp - (x - a) * (x - 1) * (x**2 - (a + 1) * x - 3 * a)))
B1 = np.diag([1.0, 2.0]).astype(complex); Bs = [B1, np.eye(2), B1.conj().T, np.eye(2)]
T = transfer(Bs, {0: 2, 1: 3, 2: 0, 3: 1})
sp_T = np.sort_complex(np.linalg.eigvals(T))
print("  numeric spec(T) =", np.round(np.sort(sp_T.real), 4), " max|Im| =", np.abs(sp_T.imag).max())
p2, n2 = (3 + np.sqrt(33)) / 2, (3 - np.sqrt(33)) / 2
p4, n4 = (5 + np.sqrt(73)) / 2, (5 - np.sqrt(73)) / 2
print(f"  p2={p2:.6f} n2={n2:.6f} p4={p4:.6f} n4={n4:.6f}")
S = [1.0] * 5 + [2.0] * 2 + [4.0, 3.0, -1.0]
rem = list(sp_T)
for s in S:
    j = int(np.argmin([abs(s - y) for y in rem])); rem.pop(j)
print("  retained A =", np.round(np.sort(np.array(rem).real), 6), " (expect p2,p2,n2,n2,p4,n4)")
for c in [-6.0, -12.0, p2 * n2, p4 * n4, 1.0]:
    print(f"    c = {c:+.4f}: d(A, c/A) = {match(rem, [c / z for z in rem]):.4f}")
for r in [p4 * 0.98, p4 * 0.999, p4, p4 * 1.001, p4 * 1.05]:
    me = nu_toeplitz_mineig(rem, r, 400)
    print(f"    r = {r:.6f} (p4 = {p4:.6f}): min eig Weil form (L=400) = {me:+.4e}")

print(); print("=" * 78); print("T3.4 with d_- > 0: the Pauli family U = X, Z (D=4, n=2), where Phi has eigenvalue -1")
print("=" * 78)
X = np.array([[0, 1], [1, 0]], dtype=complex); Z = np.diag([1, -1]).astype(complex)
Bs = [X, Z, X, Z]; rev = {0: 2, 1: 3, 2: 0, 3: 1}
D, q, N, k = 4, 3, 4, 4
T = transfer(Bs, rev); Phi = sum(Ad(B) for B in Bs) / D
lam = np.sort(np.linalg.eigvals(Phi).real)
dp = int(np.sum(np.abs(lam - 1) < 1e-9)); dm = int(np.sum(np.abs(lam + 1) < 1e-9))
S = [1.0] * k + [-1.0] * k + [float(q)] * dp + [1.0] * dp + [-float(q)] * dm + [-1.0] * dm
rem = list(np.linalg.eigvals(T))
for s in S:
    j = int(np.argmin([abs(s - y) for y in rem])); rem.pop(j)
print(f"  spec(Phi) = {np.round(lam,6)};  d_+ = {dp}, d_- = {dm};  |S| = {len(S)} (= 2k + 2d_+ + 2d_- = {2*k+2*dp+2*dm})")
print(f"  retained {len(rem)} modes (2(N-d_+-d_-) = {2*(N-dp-dm)}): {np.round(np.array(rem),6)}")
print(f"  max ||mu| - sqrt q| = {max(abs(abs(z)-np.sqrt(q)) for z in rem):.2e};  min eig Weil(L=60) = {nu_toeplitz_mineig(rem, np.sqrt(q), 60):+.3e}")
