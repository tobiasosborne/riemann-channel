#!/usr/bin/env python3
"""X2 (orchestrator's corrected Kraus dichotomy).  Reviewer claude:opus, 2026-09-12.
(a) ring traces and conjugation closure for ANY Ad family -- see scratch_weil_t3.py
(b) inverse pairing: reciprocal duality, reality of spec(Sigma) is NOT automatic,
    and Weil positivity <=> every retained alpha real with |alpha| <= 2 sqrt(D-1)
(c) adjoint pairing: Sigma is HS self-adjoint (but spec(T) is NOT real)
(d) both pairings <=> unitary."""
import numpy as np
rng = np.random.default_rng(90210)
Ad = lambda B: np.kron(B.conj(), B)

def transfer(Bs, rev):
    D = len(Bs); N = Bs[0].shape[0] ** 2
    T = np.zeros((D * N, D * N), dtype=complex)
    for i in range(D):
        Ei = Ad(Bs[i])
        for j in range(D):
            if j != rev[i]: T[j*N:(j+1)*N, i*N:(i+1)*N] = Ei
    return T
def strip(spec, S):
    rem = list(spec)
    for s in S:
        j = int(np.argmin([abs(s - y) for y in rem])); rem.pop(j)
    return rem
def mineig(A, r, L):
    z = np.array(A) / r
    nul = np.array([np.sum(z ** l) if l else complex(len(z)) for l in range(L + 1)])
    v = np.concatenate([np.conj(nul[:0:-1]), nul]); idx = np.arange(L + 1)
    M = v[idx[:, None] - idx[None, :] + L]
    return np.linalg.eigvalsh((M + M.conj().T) / 2).min()
def haar(n):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2)
    Q, R = np.linalg.qr(z); return Q @ np.diag(np.diag(R) / abs(np.diag(R)))

print("=" * 78); print("X2(b)  random INVERSE-paired (non-unitary) families: is spec(Sigma) real?"); print("=" * 78)
n, m = 2, 2; D = 2 * m; q = D - 1; N = n * n; k = N * (D - 2) // 2; rev = {i: (i + m) % D for i in range(D)}
for trial in range(5):
    Bs = [rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)) for _ in range(m)]
    Bs += [np.linalg.inv(B) for B in Bs]
    Sig = sum(Ad(B) for B in Bs); al = np.linalg.eigvals(Sig)
    T = transfer(Bs, rev); rem = strip(np.linalg.eigvals(T), [1.0] * k + [-1.0] * k)
    real_al = np.abs(al.imag).max() < 1e-9
    inband = real_al and max(abs(al.real)) <= 2 * np.sqrt(q) + 1e-9
    me = mineig(rem, np.sqrt(q), 80)
    print(f"  trial {trial}: spec(Sigma) = {np.round(al,4)}")
    print(f"           real={real_al}  |alpha| <= 2 sqrt q = {2*np.sqrt(q):.4f}: {inband};  "
          f"max ||mu| - sqrt q| = {max(abs(abs(z)-np.sqrt(q)) for z in rem):.3e};  min eig Weil(L=80) = {me:+.3e} -> PSD={me>-1e-8}")

print(); print("=" * 78)
print("X2(b)  inverse-paired families that ARE conjugate to unitary ones: B_i = G U_i G^{-1}")
print("=" * 78)
for trial in range(6):
    n, m = 2, (2 if trial % 2 == 0 else 3); D = 2 * m; q = D - 1; N = n * n
    k = N * (D - 2) // 2; rev = {i: (i + m) % D for i in range(D)}
    G = np.eye(n) + 0.8 * (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))
    Us = [haar(n) for _ in range(m)]; Bs = [G @ U @ np.linalg.inv(G) for U in Us]
    Bs += [np.linalg.inv(B) for B in Bs]                      # inverse pairing
    unitary_def = max(np.abs(B.conj().T @ B - np.eye(n)).max() for B in Bs)
    adj_paired = max(np.abs(Bs[(i + m) % D] - Bs[i].conj().T).max() for i in range(D))
    Sig = sum(Ad(B) for B in Bs); al = np.linalg.eigvals(Sig)
    T = transfer(Bs, rev); sp = np.linalg.eigvals(T)
    # trivial: S_0 and the pairs from alpha = +-D
    dp = int(np.sum(np.abs(al - D) < 1e-7)); dm = int(np.sum(np.abs(al + D) < 1e-7))
    S = [1.0]*k + [-1.0]*k + [float(q)]*dp + [1.0]*dp + [-float(q)]*dm + [-1.0]*dm
    rem = strip(sp, S)
    nontriv = [a for a in al if abs(abs(a) - D) > 1e-7]
    mx = max(abs(np.array(nontriv))) if nontriv else 0.0
    bound = (np.abs(np.array(nontriv).imag).max() < 1e-8 if nontriv else True) and mx <= 2 * np.sqrt(q) + 1e-9
    me = mineig(rem, np.sqrt(q), 80)
    print(f"  n={n} D={D}: |B^dag B - 1| = {unitary_def:.3f} (non-unitary), adjoint-pairing defect = {adj_paired:.3f}")
    print(f"     spec(Sigma) max|Im| = {np.abs(al.imag).max():.2e} (REAL: Sigma ~ G-conjugate of a Hermitian op);"
          f" max |alpha| off +-D = {mx:.4f} vs 2 sqrt q = {2*np.sqrt(q):.4f} -> bound={bound}")
    print(f"     retained {len(rem)} modes, max ||mu|-sqrt q| = {max(abs(abs(z)-np.sqrt(q)) for z in rem):.2e};"
          f"  min eig Weil(L=80) = {me:+.3e} -> PSD={me > -1e-8}    [equivalence {'HOLDS' if bound == (me > -1e-8) else 'FAILS'}]")

print(); print("=" * 78); print("X2(b')  a HAND-MADE inverse-paired family with real spec(Sigma) OUTSIDE the band")
print("=" * 78)
# B_1 = diag(s, 1/s) real: Ad(B_1) + Ad(B_1^{-1}) has eigenvalues s^2 + s^-2 (twice) and 2
for s in (1.2, 1.6, 2.0):
    B1 = np.diag([s, 1 / s]).astype(complex); Bs = [B1, np.eye(2), np.linalg.inv(B1), np.eye(2)]
    Sig = sum(Ad(B) for B in Bs); al = np.sort(np.linalg.eigvals(Sig).real)
    T = transfer(Bs, {0: 2, 1: 3, 2: 0, 3: 1}); rem = strip(np.linalg.eigvals(T), [1.0] * 4 + [-1.0] * 4)
    me = mineig(rem, np.sqrt(3.0), 200)
    print(f"  s={s}: spec(Sigma) = {np.round(al,4)} (real);  max|alpha| = {max(abs(al)):.4f} vs 2 sqrt 3 = {2*np.sqrt(3):.4f}"
          f"  -> band={max(abs(al))<=2*np.sqrt(3)+1e-9};  min eig Weil = {me:+.3e} -> PSD={me>-1e-8}")

print(); print("=" * 78); print("X2(c)/(d)  adjoint pairing: Sigma self-adjoint but spec(T) NOT real; both pairings <=> unitary")
print("=" * 78)
for trial in range(4):
    n, m = 2, 2; D = 4; rev = {i: (i + m) % D for i in range(D)}
    Bs = [rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)) for _ in range(m)]
    Bs += [B.conj().T for B in Bs]
    Sig = sum(Ad(B) for B in Bs); T = transfer(Bs, rev); sp = np.linalg.eigvals(T)
    print(f"  adjoint-paired trial {trial}: |Sigma - Sigma^dag| = {np.abs(Sig-Sig.conj().T).max():.2e}, "
          f"max|Im spec(Sigma)| = {np.abs(np.linalg.eigvals(Sig).imag).max():.2e}, "
          f"max|Im spec(T)| = {np.abs(sp.imag).max():.4f}  <- spec(T) is NOT real")
    inv_defect = max(np.abs(Ad(Bs[i].conj().T) - np.linalg.inv(Ad(Bs[i]))).max() for i in range(D))
    print(f"     superoperator inverse-pairing defect |Ad(B^dag) - Ad(B)^-1| = {inv_defect:.3f};"
          f"  |B^dag B - 1| = {max(np.abs(B.conj().T@B-np.eye(n)).max() for B in Bs):.3f}")
U = haar(2); c = 1.7
for B, lab in [(U, "unitary U"), (c * U, "1.7 * U"), (np.diag([1, 2]).astype(complex), "diag(1,2)")]:
    print(f"  B = {lab:<12}: |Ad(B^dag) - Ad(B)^-1| = {np.abs(Ad(B.conj().T)-np.linalg.inv(Ad(B))).max():.4f};"
          f"  |B^dag B - 1| = {np.abs(B.conj().T@B-np.eye(2)).max():.4f}")
