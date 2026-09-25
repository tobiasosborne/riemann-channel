"""REFUTE lane for notes/deninger-cmps/reformulation.md, Proposition R4 and S1.
Independent: imports nothing from scripts/.  Run from the repository root.

 (i)-(ii)  derivation => symplectic g_t, symmetric spectrum, but NOT the line; star commuting => skew.
 (iv)      dimension of the fixed set of g in Siegel space, by its tangent space at an invariant J0:
           distinct angles, angle 0 or pi, repeated angle with EQUAL Krein sign (the note says positive-dimensional;
           it is a point), repeated angle with opposite Krein signs, a 2+1 split.
 B-freedom invariant alternating forms and invariant metrics have the same dimension g; B -> metric is h_j = |b_j|.
 S1        the eigen-model of K_HW of D2 (z^2 = 1/alpha, 2z^4 - 2z^2 + 1 = 0): every Z-invariant B has its compatible
           polarisation inside the thm:arithmetic-metric cone; parity-(anti)invariant B gives the symmetric ray.
"""
import numpy as np
from scipy.linalg import expm, null_space

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


def rot(t):
    return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])


def blockdiag(*Ms):
    n = sum(M.shape[0] for M in Ms)
    out = np.zeros((n, n))
    i = 0
    for M in Ms:
        k = M.shape[0]
        out[i:i + k, i:i + k] = M
        i += k
    return out


def Omega(g):
    return blockdiag(*[np.array([[0., 1.], [-1., 0.]])] * g)


rng = np.random.default_rng(7)

print('R4 (i)-(ii)')
g = 3
Om = Omega(g)
J0 = blockdiag(*[rot(np.pi / 2)] * g)
check('J0 is a polarisation: J0^2=-1, J0^T Om J0 = Om, Om J0 > 0',
      np.allclose(J0 @ J0, -np.eye(2 * g)) and np.allclose(J0.T @ Om @ J0, Om)
      and np.all(np.linalg.eigvalsh((Om @ J0 + (Om @ J0).T) / 2) > 0))
alpha = 1.0
for trial in range(3):
    # random X in sp: X = Om^{-1} Ssym
    S = rng.normal(size=(2 * g, 2 * g)); S = S + S.T
    X = np.linalg.solve(Om, S)
    Th = alpha / 2 * np.eye(2 * g) + X
    der = Th.T @ Om + Om @ Th - alpha * Om
    check('(i) derivation property B(Th h,h)+B(h,Th h) = alpha B', np.allclose(der, 0))
    gt = expm(-alpha * 0.7 / 2 * np.eye(2 * g)) @ expm(0.7 * Th)
    check('(i) g_t in Sp', np.allclose(gt.T @ Om @ gt, Om))
    ev = np.linalg.eigvals(Th)
    check('(i) spectrum symmetric under l -> alpha - l',
          all(np.min(np.abs(ev - (alpha - l))) < 1e-8 for l in ev))
    check('(i) but a generic derivation has eigenvalues OFF the line Re = alpha/2 (FE without RH)',
          np.max(np.abs(ev.real - alpha / 2)) > 1e-3, f'max|Re-1/2| = {np.max(np.abs(ev.real-alpha/2)):.3f}')
    # star commuting: X in u(g) = sp cap centraliser of J0
    A = rng.normal(size=(2 * g, 2 * g))
    Xs = np.linalg.solve(Om, A + A.T)
    Xu = (Xs - J0 @ Xs @ np.linalg.inv(J0)) / 2       # project to commuting part
    Xu = (Xs + J0 @ Xs @ J0.T) / 2 if False else (Xs - J0 @ Xs @ J0) / 2
    Th2 = alpha / 2 * np.eye(2 * g) + Xu
    G = Om @ J0     # (h,h') = B(h, J0 h')
    check('(ii) [Th, *] = 0 and Th derivation', np.allclose(Th2 @ J0, J0 @ Th2) and np.allclose(Th2.T @ Om + Om @ Th2, alpha * Om))
    check('(ii) => (Th h,h)+(h,Th h) = alpha (h,h)', np.allclose(Th2.T @ G + G @ Th2, alpha * G))
    check('(ii) => spectrum on Re = alpha/2', np.allclose(np.linalg.eigvals(Th2).real, alpha / 2))


def fixed_dim(gm, J):
    """dim of the fixed set of J' -> gm J' gm^-1 in Siegel space, via tangent space at J (J must be fixed)."""
    n = gm.shape[0]
    Om_ = Omega(n // 2)
    assert np.allclose(gm @ J, J @ gm)
    # unknown X (n x n): X^T Om + Om X = 0 ; X J + J X = 0 ; gm X - X gm = 0
    rows = []
    E = np.eye(n * n)
    for k in range(n * n):
        X = E[k].reshape(n, n)
        rows.append(np.concatenate([(X.T @ Om_ + Om_ @ X).ravel(), (X @ J + J @ X).ravel(), (gm @ X - X @ gm).ravel()]))
    Mat = np.array(rows).T
    return null_space(Mat).shape[1]


print('R4 (iv): fixed sets in Siegel space')
cases = [
    ('distinct angles (0.4, 1.1, 2.3)', blockdiag(rot(0.4), rot(1.1), rot(2.3)), 0),
    ('angle 0 (g_1 = 1 on a plane)', blockdiag(rot(0.0)), 2),
    ('angles (0, 1.1)', blockdiag(rot(0.0), rot(1.1)), 2),
    ('angle pi', blockdiag(rot(np.pi), rot(0.9)), 2),
    ('repeated angle, SAME Krein sign  R_th + R_th', blockdiag(rot(1.1), rot(1.1)), 0),
    ('repeated angle, OPPOSITE Krein sign  R_th + R_-th', blockdiag(rot(1.1), rot(-1.1)), 2),
    ('R_th + R_th + R_-th', blockdiag(rot(1.1), rot(1.1), rot(-1.1)), 4),
    ('R_th + R_th + R_th', blockdiag(rot(1.1), rot(1.1), rot(1.1)), 0),
]
for name, gm, want in cases:
    n = gm.shape[0] // 2
    J = blockdiag(*[rot(np.pi / 2)] * n)
    d = fixed_dim(gm, J)
    check(f'(iv) {name}: dim = {want}', d == want, f'got {d}')
print('  => the note\'s "if some theta_j repeats, positive-dimensional" is false when the repeated pair has one Krein sign')

print('R4 B-freedom: invariant alternating forms vs invariant metrics')


def inv_forms(gm, sym):
    n = gm.shape[0]
    rows = []
    basis = []
    for i in range(n):
        for j in range(n):
            if sym and j < i:
                continue
            if not sym and j <= i:
                continue
            M = np.zeros((n, n)); M[i, j] = 1
            M = M + M.T if sym else M - M.T
            if sym and i == j:
                M = M / 2
            basis.append(M)
    Mat = np.array([(gm.T @ M @ gm - M).ravel() for M in basis]).T
    ns = null_space(Mat)
    return [sum(c * M for c, M in zip(v, basis)) for v in ns.T]


gm = blockdiag(rot(0.4), rot(1.1), rot(2.3))
check('B-freedom: g-invariant alternating forms, distinct angles, dim = g = 3', len(inv_forms(gm, False)) == 3)
check('B-freedom: g-invariant symmetric forms, dim = g = 3', len(inv_forms(gm, True)) == 3)
b = np.array([0.3, -2.0, 1.7])
B = blockdiag(*[bj * np.array([[0., 1.], [-1., 0.]]) for bj in b])
# compatible polarisation: on each plane the complex structure in the centraliser with B(u,*u)>0
star = blockdiag(*[np.sign(bj) * rot(np.pi / 2) for bj in b])
M = B @ star
check('B -> compatible metric is diag(|b_j|) per plane', np.allclose(M, blockdiag(*[abs(bj) * np.eye(2) for bj in b])))
check('compatible metric is g-invariant (lies in the unitarising cone)', np.allclose(gm.T @ M @ gm, M))

print('S1: eigen-model of K_HW of D2')
z = np.roots([2, 0, -2, 0, 1])
r = 2 ** -0.25
check('D2 resonances: |z| = 2^{-1/4}, args +-pi/8, +-7pi/8',
      np.allclose(np.abs(z), r) and np.allclose(sorted(np.abs(np.angle(z))), sorted([np.pi / 8] * 2 + [7 * np.pi / 8] * 2)))
a = z[np.argmin(np.abs(np.angle(z) - np.pi / 8))]
zs = np.array([a, np.conj(a), -a, -np.conj(a)])          # order: a, abar, -a, -abar
Z = np.diag(zs)
# Hermitian unitarising cone
rowsH = []
basisH = []
for i in range(4):
    for j in range(i, 4):
        for part in ((1, 0), (0, 1)):
            if i == j and part == (0, 1):
                continue
            Hm = np.zeros((4, 4), complex)
            if i == j:
                Hm[i, i] = 1
            elif part == (1, 0):
                Hm[i, j] = 1; Hm[j, i] = 1
            else:
                Hm[i, j] = 1j; Hm[j, i] = -1j
            basisH.append(Hm)
Mat = np.array([np.concatenate([(Z.conj().T @ Hm @ Z - r * r * Hm).real.ravel(), (Z.conj().T @ Hm @ Z - r * r * Hm).imag.ravel()]) for Hm in basisH]).T
check('thm:arithmetic-metric cone {Z^* H Z = r^2 H} has real dim 4', null_space(Mat).shape[1] == 4)
# complex bilinear alternating invariant forms
basisB = []
for i in range(4):
    for j in range(i + 1, 4):
        Bm = np.zeros((4, 4), complex); Bm[i, j] = 1; Bm[j, i] = -1
        basisB.append(Bm)
MatB = np.array([(Z.T @ Bm @ Z - r * r * Bm).ravel() for Bm in basisB]).T
check('Z-invariant alternating forms (Z^T B Z = r^2 B): complex dim 2 (never zero: outcome 3 of S1 cannot occur)',
      null_space(MatB).shape[1] == 2)
# real form: basis u1 = e_a + e_abar, u2 = i(e_a - e_abar), u3 = e_-a + e_-abar, u4 = i(e_-a - e_-abar)
T = np.array([[1, 1j, 0, 0], [1, -1j, 0, 0], [0, 0, 1, 1j], [0, 0, 1, -1j]])
gR = np.linalg.solve(T, Z @ T) / r
check('real form: r^{-1} Z is a real matrix on the real structure', np.allclose(gR.imag, 0))
gR = gR.real
eps = np.zeros((4, 4)); eps[0, 2] = eps[2, 0] = eps[1, 3] = eps[3, 1] = 1     # a <-> -a, abar <-> -abar
epsR = np.linalg.solve(T, eps @ T)
check('parity in the real form is real and anticommutes: eps Z eps = -Z', np.allclose(epsR.imag, 0) and np.allclose(epsR.real @ gR @ epsR.real, -gR))
epsR = epsR.real
Bs = inv_forms(gR, False)
Ss = inv_forms(gR, True)
check('real invariant alternating forms: dim 2', len(Bs) == 2)
check('real invariant symmetric forms: dim 2 (the cone after reality)', len(Ss) == 2)
# parity action on the invariant symmetric forms
Pm = np.array([[np.sum((epsR.T @ S1 @ epsR) * S2) for S2 in Ss] for S1 in Ss])
check('parity-invariant invariant metrics: dim 1 (the symmetric ray)', np.sum(np.abs(np.linalg.eigvals(Pm) - 1) < 1e-8) == 1)


def compatible_metric(Bm, gm):
    # planes: real invariant 2-planes = spans of (u1,u2) and (u3,u4) here
    star = np.zeros((4, 4))
    for idx in ((0, 1), (2, 3)):
        P = np.zeros((4, 4)); P[list(idx), list(idx)] = 1
        gp = gm[np.ix_(idx, idx)]
        th = np.arccos(np.clip(np.trace(gp) / 2, -1, 1))
        Jp = (gp - np.cos(th) * np.eye(2)) / np.sin(th)
        u = np.zeros(4); u[idx[0]] = 1
        Jfull = np.zeros((4, 4)); Jfull[np.ix_(idx, idx)] = Jp
        sgn = np.sign(u @ Bm @ Jfull @ u)
        star[np.ix_(idx, idx)] = sgn * Jp
    return Bm @ star, star


for coeffs, label in (((1.0, 0.0), 'B_1'), ((0.0, 1.0), 'B_2'), ((1.0, 1.0), 'B_1+B_2'), ((1.0, -1.0), 'B_1-B_2'), ((1.0, 0.37), 'B_1+0.37B_2')):
    Bm = coeffs[0] * Bs[0] + coeffs[1] * Bs[1]
    if abs(np.linalg.det(Bm)) < 1e-10:
        continue
    Mm, st = compatible_metric(Bm, gR)
    isstar = np.allclose(st @ st, -np.eye(4)) and np.allclose(st.T @ Bm @ st, Bm) and np.allclose(st @ gR, gR @ st)
    pos = np.all(np.linalg.eigvalsh((Mm + Mm.T) / 2) > 0)
    incone = np.allclose(gR.T @ Mm @ gR, Mm)
    onray = np.allclose(epsR.T @ Mm @ epsR, Mm)
    parB = np.allclose(epsR.T @ Bm @ epsR, Bm) or np.allclose(epsR.T @ Bm @ epsR, -Bm)
    check(f'S1 {label}: compatible * exists, metric positive and in the Z-cone', isstar and pos and incone)
    check(f'S1 {label}: on the symmetric ray iff B parity-(anti)invariant', onray == parB, f'onray={onray} parityB={parB}')

print('Deninger\'s Laplacian route [D05:856-864]: -(Theta - alpha/2)^2 = Delta^1 >= 0 on the kernel')
gams = (0.7, 1.9, 3.4)
Xg = blockdiag(*[gj * rot(np.pi / 2) for gj in gams])          # Theta - alpha/2 on the real odd bond
D = -Xg @ Xg
check('Laplacian route: D = -(Theta-1/2)^2 = diag(gamma_j^2) on the eigenplanes, >= 0',
      np.allclose(D, blockdiag(*[gj ** 2 * np.eye(2) for gj in gams])))
basis = []
n6 = 6
for i in range(n6):
    for j in range(i, n6):
        Mm = np.zeros((n6, n6)); Mm[i, j] = 1; Mm[j, i] = 1
        basis.append(Mm)
Mat = np.array([(Mm @ D - D.T @ Mm).ravel() for Mm in basis]).T
dimL = null_space(Mat).shape[1]
Mat2 = np.array([(Xg.T @ Mm + Mm @ Xg).ravel() for Mm in basis]).T
dimP = null_space(Mat2).shape[1]
check('metrics making Delta self-adjoint: dim 3g = 9 (any metric with the eigenplanes orthogonal)', dimL == 9, f'got {dimL}')
check('metrics making Theta-1/2 skew (flow-invariant): dim g = 3; with B fixed: a point', dimP == 3, f'got {dimP}')
Xbad = Xg + 0.2 * np.eye(6) * np.array([1, 1, 0, 0, 0, 0])      # push one pair off the line
Dbad = -Xbad @ Xbad
check('off the line, D is not diagonalisable with real nonnegative spectrum (no metric exists)',
      np.max(np.abs(np.linalg.eigvals(Dbad).imag)) > 1e-3)

print(f'\nscratch_den_r4: {ok} pass, {fail} fail')
