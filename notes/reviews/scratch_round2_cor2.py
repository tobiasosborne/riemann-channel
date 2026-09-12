"""Round-2 independent check of Corollary 2 as literally stated (Kraus case)."""
import itertools
import numpy as np

rng = np.random.default_rng(20260912)
n, m = 3, 2
As = [rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)) for _ in range(m)]
As = As + [A.conj().T for A in As]
D = 2*m
inv = [(i + m) % D for i in range(D)]
ad = lambda A: np.kron(A.conj(), A)          # column stacking: Ad(A) = conj(A) (x) A
Es = [ad(A)/3 for A in As]
Bs = [A/np.sqrt(3) for A in As]              # so that Es[i] = ad(Bs[i]) exactly
assert max(np.abs(ad(Bs[i]) - Es[i]).max() for i in range(D)) < 1e-12
N = n*n
T = np.zeros((N*D, N*D), complex)
for i in range(D):
    for j in range(D):
        if j != inv[i]:
            T[j*N:(j+1)*N, i*N:(i+1)*N] = Es[i]

print('--- Cor 2 trace formula as stated: Tr_W T^l = sum |Tr(A_{i_l}...A_{i_1})|^2 ---')
for ell in range(1, 6):
    lhs = np.trace(np.linalg.matrix_power(T, ell))
    tot = 0.0
    for w in itertools.product(range(D), repeat=ell):
        if all(w[(k+1) % ell] != inv[w[k]] for k in range(ell)):
            P = np.eye(n, dtype=complex)
            for i in w:
                P = Bs[i] @ P               # A_{i_l} ... A_{i_1}
            tot += abs(np.trace(P))**2
    print(f'  l={ell}: |Tr T^l - sum| = {abs(lhs-tot):.2e}; '
          f'Im(Tr T^l) = {abs(lhs.imag):.1e}; sum >= 0: {tot >= 0}')
    assert abs(lhs - tot) < 1e-8 and tot >= 0

print('--- Cor 2 bound |u| < min_k ||A_k||^{-2} equals (max_i ||E_ibar E_i||)^{-1/2} ---')
b1 = min(np.linalg.norm(Bs[k], 2)**-2 for k in range(m))
b2 = max(np.linalg.norm(Es[inv[i]] @ Es[i], 2) for i in range(D))**-0.5
print(f'  min_k ||A_k||^-2 = {b1:.6f}   (max_i ||E_ibar E_i||)^-1/2 = {b2:.6f}   '
      f'rel diff {abs(b1/b2-1):.2e}')

print('--- Cor 2 Euler product over primitive cyclically non-backtracking classes ---')
uu = 0.05
# collect primitive classes up to length 6
seen = set()
logZ = 0.0 + 0j
for ell in range(1, 7):
    for w in itertools.product(range(D), repeat=ell):
        if not all(w[(k+1) % ell] != inv[w[k]] for k in range(ell)):
            continue
        rots = {w[k:] + w[:k] for k in range(ell)}
        if len(rots) != ell:          # not primitive
            continue
        key = min(rots)
        if key in seen:
            continue
        seen.add(key)
        Aw = np.eye(n, dtype=complex)
        for i in reversed(key):        # A_{i_l}...A_{i_1} for key=(i_1..i_l)
            Aw = Aw @ Bs[i]
        logZ -= np.log(np.linalg.det(np.eye(N) - uu**ell*ad(Aw)))
zeta_exact = 1.0/np.linalg.det(np.eye(N*D) - uu*T)
print(f'  Euler product (|w|<=6) = {np.exp(logZ).real:.10f}   '
      f'det(1-uT)^-1 = {zeta_exact.real:.10f}   rel diff {abs(np.exp(logZ)/zeta_exact-1):.1e}')

print('--- Cor 2 positivity of Ad(A^dag A) and ||Ad(A^dag A)|| = ||A||^4 ---')
P = Bs[0].conj().T @ Bs[0]
ev = np.linalg.eigvals(ad(P))
print(f'  min Re eig = {ev.real.min():.2e}, max |Im eig| = {abs(ev.imag).max():.1e}, '
      f'||Ad(P)|| vs ||A||^4: {abs(np.linalg.norm(ad(P),2)/np.linalg.norm(Bs[0],2)**4 - 1):.2e}')
print('COR2 CHECKS PASS')
