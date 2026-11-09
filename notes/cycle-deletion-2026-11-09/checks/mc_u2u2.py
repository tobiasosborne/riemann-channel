"""Monte Carlo sanity check (not a proof): is E det(x - A_{U (x) V}) over independent Haar U_e, V_e in U(2) on K4
equal to Phi = mu_4(K4) + 4x^4 + 3 (the conformal-Sp4 polynomial) rather than mu_4(K4)?"""
import numpy as np, sys
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
def haar(n, N):
    Z = (rng.standard_normal((N, n, n)) + 1j * rng.standard_normal((N, n, n))) / np.sqrt(2)
    Q, R = np.linalg.qr(Z)
    ph = np.diagonal(R, axis1=1, axis2=2); ph = ph / np.abs(ph)
    return Q * ph[:, None, :]
edges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
def sample(N, mode):
    A = np.zeros((N, 16, 16), dtype=complex)
    for (u, v) in edges:
        if mode == 'u2u2':
            U = haar(2, N); V = haar(2, N)
            B = np.einsum('nij,nkl->nikjl', U, V).reshape(N, 4, 4)
        else:
            B = haar(4, N)
        A[:, 4*u:4*u+4, 4*v:4*v+4] = B
        A[:, 4*v:4*v+4, 4*u:4*u+4] = np.conj(np.transpose(B, (0, 2, 1)))
    return A
mu4 = lambda x: x**16 - 24*x**14 + 228*x**12 - 1092*x**10 + 2781*x**8 - 3654*x**6 + 2230*x**4 - 495*x**2 + 75/4
phi = lambda x: mu4(x) + 4*x**4 + 3
xs = [0.0, 0.5, 1.0]
N = 200000; reps = 10
for mode in ('u4', 'u2u2'):
    acc = {x: [] for x in xs}
    for _ in range(reps):
        A = sample(N, mode)
        ev = np.linalg.eigvalsh(A)
        for x in xs: acc[x].append(np.prod(x - ev, axis=1).mean())
    for x in xs:
        a = np.array(acc[x]); print('%-5s x=%.1f  MC mean %.3f +- %.3f   mu_4 = %.3f   Phi = %.3f' % (mode, x, a.mean(), a.std(ddof=1) / np.sqrt(reps), mu4(x), phi(x)))
