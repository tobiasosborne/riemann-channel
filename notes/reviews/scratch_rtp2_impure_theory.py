#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane I (claude:opus, 2026-09-26): the algebraic statements of I1-I3 tested on random
and adversarial instances.  (a) rank-two counterexample and tensor-shift ranks (I1); (b) I2b two-sided rotation
bounds and the Schmidt upper bound; (c) I2c Schur-complement bounds, including instances violating a >= ||T||_2;
(d) no lower Schmidt bound from eta alone (M_L x I); (e) I3: Fourier identity for f^* * g at complex z, the paired
zero formula (real, indefinite off the line), linear independence of overlapping translates.  numpy/mpmath; seed 20260926."""
import numpy as np, mpmath as mp, itertools
rng = np.random.default_rng(20260926)
NC = [0, 0]
def check(c, m):
    NC[0] += 1; NC[1] += (not c); print(('PASS ' if c else 'FAIL ') + m, flush=True)
def defect(v, dims):
    s = np.linalg.svd(v.reshape(dims), compute_uv=False); return 1 - s[0] ** 2 / np.sum(s ** 2)
# (a) tensor-shift description of B_D and its rank
S, A = (2, 3), 2
pts = list(itertools.product(range(A + 1), repeat=2)); t = [sum(a * np.log(p) for a, p in zip(q, S)) for q in pts]
ok = True; ranks = []
for e in itertools.product(range(-A, A + 1), repeat=2):
    if e == (0, 0): continue
    D = abs(e[0] * np.log(2) + e[1] * np.log(3))
    B = np.array([[1. if abs(abs(t[i] - t[j]) - D) < 1e-12 else 0. for j in range(9)] for i in range(9)])
    T = lambda s, n: np.eye(n, k=s)
    Te = np.kron(T(e[0], 3), T(e[1], 3)); Tm = np.kron(T(-e[0], 3), T(-e[1], 3))
    ok &= np.array_equal(B, Te + Tm)
    ok &= np.linalg.matrix_rank(Te) == (A + 1 - abs(e[0])) * (A + 1 - abs(e[1]))
    ranks.append(np.linalg.matrix_rank(B))
check(ok, f'B_D = T_e + T_-e (tensor shifts), rank T_e = prod(A+1-|e_p|); ranks of B_D on {{2,3}} A=2: {sorted(set(ranks))} (never 1)')
P3 = np.array([[0, 1.], [1., 0]])
check(np.linalg.matrix_rank(P3) == 2 and np.allclose(np.linalg.eigvalsh(P3), [-1, 1]) and np.log(1.5) < 2 * 0.21 and np.log(3) > 2 * 0.21,
      'S={2}, A=1, k=3, delta=0.21: only D=log 2 touched (|log 3 - log 2| = 0.405 < 0.42, log 3 > 0.42), P_3 = c[[0,1],[1,0]] rank 2, eigenvalues +-c')
# (b),(c) random perturbations of a Kronecker sum
viol_b = viol_c = 0; nb = nc = 0; notcond = 0
for trial in range(4000):
    n1, n2 = rng.integers(2, 5, 2)
    A1 = rng.normal(size=(n1, n1)); A1 = A1 + A1.T; A2m = rng.normal(size=(n2, n2)); A2m = A2m + A2m.T
    K = np.kron(A1, np.eye(n2)) + np.kron(np.eye(n1), A2m)
    w, V = np.linalg.eigh(K); g = w[1] - w[0]
    if g < 1e-3: continue
    v0 = V[:, 0]; Wd = w[-1] - w[0]
    M = rng.normal(size=K.shape); M = M + M.T
    scale = rng.uniform(0.01, 1.0) * g / 2 / np.linalg.norm(M, 2) if trial % 2 == 0 else rng.uniform(0.01, 3.0) * g / np.linalg.norm(M, 2)
    M *= scale; eps = np.linalg.norm(M, 2)
    ww, VV = np.linalg.eigh(K + M); v = VV[:, 0]
    if v @ v0 < 0: v = -v
    a = v @ v0; u = v - a * v0; Q = np.eye(len(v0)) - np.outer(v0, v0); eta = np.linalg.norm(Q @ M @ v0)
    dft = defect(v, (n1, n2))
    if eps < g / 2:
        nb += 1; tt = np.linalg.norm(u) / a
        good = eta / (Wd + 2 * eps) - 1e-12 <= tt <= eta / (g - 2 * eps) + 1e-12 and dft <= np.linalg.norm(u) ** 2 + 1e-12 <= eta ** 2 / ((g - 2 * eps) ** 2 + eta ** 2) + 2e-12
        viol_b += not good
    # I2c in local bases starting with the factors of v0
    U, s, Vt = np.linalg.svd(v0.reshape(n1, n2)); C = U.T @ v.reshape(n1, n2) @ Vt.T
    if C[0, 0] < 0: C = -C
    a = C[0, 0]
    if a <= 1e-9: continue
    x = C[1:, 0]; y = C[0, 1:]; T = C[1:, 1:] - np.outer(x, y) / a
    hF = np.linalg.norm(T); up = hF ** 2
    nc += 1
    good = dft <= up + 1e-12
    if a >= np.linalg.norm(T, 2):
        lo = (hF / ((1 + np.linalg.norm(x) / a) * (1 + np.linalg.norm(y) / a))) ** 2
        good &= lo <= dft + 1e-12
    else:
        notcond += 1
    viol_c += not good
check(viol_b == 0 and nb > 1000, f'I2b: t in [eta/(W+2eps), eta/(g-2eps)] and defect <= ||u||^2 <= eta^2/((g-2eps)^2+eta^2): {nb} random instances with eps<g/2, {viol_b} violations')
check(viol_c == 0 and nc > 3000, f'I2c: sqrt-defect bounds, {nc} instances ({notcond} with a < ||T||_2, upper bound only), {viol_c} violations')
# is the hypothesis a >= ||T||_2 needed?  search for a lower-bound failure when it is dropped
fails = 0
for trial in range(20000):
    n1, n2 = 3, 3
    C = rng.normal(size=(n1, n2)); C /= np.linalg.norm(C)
    if C[0, 0] < 0: C = -C
    a = C[0, 0]
    if a < 1e-3: continue
    x = C[1:, 0]; y = C[0, 1:]; T = C[1:, 1:] - np.outer(x, y) / a
    if a >= np.linalg.norm(T, 2): continue
    s = np.linalg.svd(C, compute_uv=False); dft = 1 - s[0] ** 2
    lo = (np.linalg.norm(T) / ((1 + np.linalg.norm(x) / a) * (1 + np.linalg.norm(y) / a))) ** 2
    fails += lo > dft + 1e-12
print(f'    without a >= ||T||_2 the lower bound fails in {fails} of the random 3x3 draws (hypothesis is load-bearing)')
# epsilon < g/4 => a >= ||T||_2 (claimed): random check
bad = 0; cnt = 0
for trial in range(3000):
    n1, n2 = rng.integers(2, 5, 2)
    A1 = rng.normal(size=(n1, n1)); A1 += A1.T; A2m = rng.normal(size=(n2, n2)); A2m += A2m.T
    K = np.kron(A1, np.eye(n2)) + np.kron(np.eye(n1), A2m); w, V = np.linalg.eigh(K); g = w[1] - w[0]
    if g < 1e-3: continue
    M = rng.normal(size=K.shape); M += M.T; M *= rng.uniform(0.5, 0.999) * g / 4 / np.linalg.norm(M, 2)
    v0 = V[:, 0]; v = np.linalg.eigh(K + M)[1][:, 0]
    U, s, Vt = np.linalg.svd(v0.reshape(n1, n2)); C = U.T @ v.reshape(n1, n2) @ Vt.T
    if C[0, 0] < 0: C = -C
    a = C[0, 0]; x = C[1:, 0]; y = C[0, 1:]; T = C[1:, 1:] - np.outer(x, y) / a
    cnt += 1; bad += a < np.linalg.norm(T, 2)
check(bad == 0, f'eps < g/4 implies a >= ||T||_2: {cnt} random instances near eps = g/4, {bad} violations')
# quadratic law defect = s^2 ||N z||^2 + O(s^3)
n1, n2 = 3, 4
A1 = rng.normal(size=(n1, n1)); A1 += A1.T; A2m = rng.normal(size=(n2, n2)); A2m += A2m.T
K = np.kron(A1, np.eye(n2)) + np.kron(np.eye(n1), A2m); w, V = np.linalg.eigh(K); v0 = V[:, 0]
M = rng.normal(size=K.shape); M += M.T
Q = np.eye(12) - np.outer(v0, v0); B = Q @ (K - w[0] * np.eye(12)) @ Q
z = np.linalg.lstsq(B, Q @ M @ v0, rcond=None)[0]; z = Q @ z
vL = np.linalg.eigh(A1)[1][:, 0]; vR = np.linalg.eigh(A2m)[1][:, 0]
N = np.kron(np.eye(n1) - np.outer(vL, vL), np.eye(n2) - np.outer(vR, vR)); c = np.linalg.norm(N @ z) ** 2
rat = []
for s in (1e-2, 5e-3, 2.5e-3):
    v = np.linalg.eigh(K + s * M)[1][:, 0]; rat.append(defect(v, (n1, n2)) / s ** 2)
check(abs(rat[-1] - c) / c < 1e-2 and abs(rat[-1] - c) < abs(rat[0] - c), f'defect/s^2 -> ||N z||^2 = {c:.6f}: {[round(r, 6) for r in rat]}')
# (d) M = M_L x I: rotates the ground vector (eta > 0), defect stays 0
ML = rng.normal(size=(n1, n1)); ML += ML.T; ML *= 0.1 * (w[1] - w[0]) / np.linalg.norm(ML, 2)
Mt = np.kron(ML, np.eye(n2)); v = np.linalg.eigh(K + Mt)[1][:, 0]
check(np.linalg.norm(Q @ Mt @ v0) > 1e-3 and defect(v, (n1, n2)) < 1e-20, f'M_L x I: eta = {np.linalg.norm(Q@Mt@v0):.3e} > 0 but defect = {defect(v,(n1,n2)):.1e}: no lower bound from eta alone')
# (e) I3 identities
mp.mp.dps = 30
d = mp.mpf('0.3')
phi = lambda x: mp.exp(-1 / (1 - (x / d) ** 2)) if abs(x) < d else mp.mpf(0)
def fhat(ta, z): return mp.quad(lambda x: phi(x - ta) * mp.exp(-1j * z * x), [ta - d, ta, ta + d])
ta, tb = mp.mpf('0.1'), mp.log(2)
z = mp.mpc('3.7', '0.21')
Dp = tb - ta
Fstar = lambda y: mp.quad(lambda x: phi(x - y - ta) * phi(x - tb), [tb - d, tb, tb + d])   # (f^* * g)(y) = int conj f(x-y) g(x) dx
lhs = mp.quad(lambda y: Fstar(y) * mp.exp(-1j * z * y), [Dp - 2 * d, Dp, Dp + 2 * d])
rhs = mp.conj(fhat(ta, mp.conj(z))) * fhat(tb, z)
check(abs(lhs - rhs) < 1e-20, f'hat(f^* * g)(z) = conj(hat f(conj z)) hat g(z) at complex z: |diff| = {mp.nstr(abs(lhs-rhs),3)}')
# paired formula with a fictitious off-line quadruple: rho = 1/2 + 0.1 + 14 i and 1 - conj(rho) etc.
def pairsum(c, zs):
    tot = 0
    for zz in zs:
        tot += mp.conj(mp.fsum(ci * fhat(tt, mp.conj(zz)) for ci, tt in c)) * mp.fsum(ci * fhat(tt, zz) for ci, tt in c)
    return tot
zs_on = [mp.mpf(14), mp.mpf(-14)]
beta = mp.mpf('0.1'); gam = mp.mpf(14)
rhos = [mp.mpf('0.5') + beta + 1j * gam, mp.mpf('0.5') - beta + 1j * gam, mp.mpf('0.5') + beta - 1j * gam, mp.mpf('0.5') - beta - 1j * gam]
zs_off = [1j * (r - mp.mpf('0.5')) for r in rhos]
tt3 = [mp.mpf(k) * mp.log(2) / 3 for k in range(3)]
def formmat(zs):
    # matrix of c -> sum_z conj(fhat_c(conj z)) fhat_c(z) on real coefficient vectors c
    Mz = mp.matrix(3, 3)
    for zz in zs:
        for i in range(3):
            for j in range(3): Mz[i, j] += mp.conj(fhat(tt3[i], mp.conj(zz))) * fhat(tt3[j], zz)
    return Mz
Mon, Moff = formmat(zs_on), formmat(zs_off)
imag = max(abs(mp.im(x)) for x in list(Mon) + list(Moff))
Son = mp.matrix([[mp.re(Mon[i, j] + Mon[j, i]) / 2 for j in range(3)] for i in range(3)])
Soff = mp.matrix([[mp.re(Moff[i, j] + Moff[j, i]) / 2 for j in range(3)] for i in range(3)])
eon, eoff = mp.eigsy(Son)[0], mp.eigsy(Soff)[0]
check(imag < 1e-15 and min(eon) > -1e-25 and min(eoff) < 0 < max(eoff),
      f'paired sum as a form on 3 translates: on-line pair PSD (eigs {[mp.nstr(x,3) for x in eon]}); off-line quadruple (beta=0.1, gamma=14) real and indefinite (eigs {[mp.nstr(x,3) for x in eoff]})')
# linear independence of overlapping translates: L2 Gram of 5 heavily overlapping translates is nonsingular
tt = [mp.mpf(k) / 20 for k in range(5)]
H = mp.matrix(5, 5)
for i in range(5):
    for j in range(5):
        H[i, j] = mp.quad(lambda x: phi(x - tt[i]) * phi(x - tt[j]), [max(tt[i], tt[j]) - d, (tt[i] + tt[j]) / 2, min(tt[i], tt[j]) + d])
check(min(mp.eigsy(H)[0]) > 0, f'5 translates with spacing 0.05 at delta = 0.3: L2 Gram min eigenvalue {mp.nstr(min(mp.eigsy(H)[0]),4)} > 0')
print(f'# checks: {NC[0]} run, {NC[1]} failed')
