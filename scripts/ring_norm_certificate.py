#!/usr/bin/env python3
"""Genus-two ring-norm tensors: the exact rational certificate and the explicit nine-letter formula.

Evidence for shard 06d (thm:f5-certified-tensor, thm:nine-letter-tensor, prop:f5-base-change).

Part A (author of the certificate: codex:gpt-6-astra, notes/ring-norm-tensor/astra-proofs.md T4.5a):
  a two-even, one-odd graded tensor on C^{1|2} for the curve y^2 = x^5 + x^3 + x^2 - 2 over F_5
  (Frobenius quartic z^4 - 3z^3 + 7z^2 - 15z + 25).  Nine of the 28 real coordinates are free;
  f(y) = (Tr E_e^n - (1 + 5^n), n <= 5; Tr E_o^n - p_n, n <= 4) is evaluated EXACTLY over Q at
  the rational centre y_0, together with its Jacobian J; a rational approximate inverse B is
  checked by exact rational comparisons to satisfy ||B|| < 2, ||B f(y_0)|| < 1e-70,
  ||1 - BJ|| < 1e-50, so that y -> y - B f(y) is a contraction of the box ||y - y_0|| <= 1e-30
  (Hessian bound 1e16).  The unique zero in the box gives chi_e = z^3 (z-1)(z-5) and
  chi_o = the Frobenius quartic, hence str E^n = N_n for every n.
Part B (author: claude:fable-5.1): the nine-letter tensor of T4.3 for q = 25 (base change of the
  same curve), q = 17 and q = 16, checked for even spectrum {1, q, 0, 0, 0}, odd block diag(conj D, D),
  normality and str E^n = N_n for n <= 8; and its failure below q + 1 = 4 sqrt q (q = 13).
Part C: the certified centre, built in floating point, gives chi_e, chi_o and str E^n = N_n to
  double precision, and the explicit Jordan-Wigner Fock vector norm for n = 2..5.

Deterministic; exits nonzero on failure.  Run from the repository root:
    python3 scripts/ring_norm_certificate.py > outputs/ring_norm_certificate.txt
"""
import sys
import numpy as np
from fractions import Fraction as F
import mpmath as mp

NCHK = 0
FAILS = []


def check(cond, msg):
    global NCHK
    NCHK += 1
    if not cond:
        FAILS.append(msg)
    print(('PASS ' if cond else 'FAIL ') + msg)


# ------------------------------------------------------------------ Part A: the certificate
mp.mp.dps = 110
base_text = "0.26071183 -0.77630597 0.1256142 0.57129743 0.23357458 -0.48921698 -1.34760956 -0.05591677 -0.94940643 -0.38739751 -0.67840262 -1.61862569 0.09572017 -0.36950433 -0.80102781 0.32500101 -1.0690133 -0.50378403 0.0903946 -0.85610066 -0.89848953 -0.00971177 -0.9517933 -0.63028434 0.30058661 1.43919288 0.38038457 -1.21909557".split()
sel = [18, 15, 11, 19, 14, 2, 22, 4, 3]
pos = [(s, i, j) for s in range(3) for i in range(3) for j in range(3) if (s < 2) == ((i == 0) == (j == 0))]
idxs = ([0, 4, 5, 7, 8], [1, 2, 3, 6])
ns = (5, 4)
target = [6, 26, 126, 626, 3126, 3, -5, 9, 7]
active = [
    '0.0903946022326197086918581936003652642108422681757834121198569509935751292079285209190880028',
    '0.325001015712151197553026743073611383028909263869300480901353211781331926553983584722142652',
    '-1.61862568848573412561085612335033964354282729706378489347434769629526938804341538871295182',
    '-0.856100671883734631506405289461842300801039252464833047343784570879130428726933907333213827',
    '-0.80102781481057057826927943665335609983310469191396383065095317561795085119201793039066329',
    '0.125614201299343247797946104304359812581511668431930091377412797232085492448163457526247418',
    '-0.951793304521566588362992674206553375775973049960369410863894719514069329407054372830229032',
    '0.233574566527024915170370648357379441749679527579971848850435885749412325417262635189600452',
    '0.571297437238715211680159923446246584732241927298292338354479377560643476028340257150472248',
]
zero = (F(0), F(0)); one = (F(1), F(0))
add = lambda a, b: (a[0] + b[0], a[1] + b[1])
mul = lambda a, b: (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
conj = lambda a: (a[0], -a[1])


def matmul(a, b):
    out = [[zero for _ in b[0]] for _ in a]
    for i in range(len(a)):
        for k in range(len(b)):
            if a[i][k] == zero:
                continue
            for j in range(len(b[0])):
                if b[k][j] != zero:
                    out[i][j] = add(out[i][j], mul(a[i][k], b[k][j]))
    return out


def trace(a):
    z = zero
    for i in range(len(a)):
        z = add(z, a[i][i])
    assert z[1] == 0
    return z[0]


def traced_product(a, b):
    z = zero
    for i in range(len(a)):
        for j in range(len(a)):
            z = add(z, mul(a[i][j], b[j][i]))
    assert z[1] == 0
    return z[0]


x = list(map(F, base_text))
for l, v in zip(sel, active):
    x[l] = F(v)
As = [[[zero] * 3 for _ in range(3)] for _ in range(3)]
for l, (s, i, j) in enumerate(pos):
    As[s][i][j] = (x[2 * l], x[2 * l + 1])
Es = []
for idx in idxs:
    E = []
    for r in idx:
        row = []
        for c in idx:
            z = zero
            for A in As:
                z = add(z, mul(A[r // 3][c // 3], conj(A[r % 3][c % 3])))
            row.append(z)
        E.append(row)
    Es.append(E)
ps = []
for E, n in zip(Es, ns):
    p = [[[one if i == j else zero for j in range(len(E))] for i in range(len(E))]]
    for _ in range(n):
        p.append(matmul(p[-1], E))
    ps.append(p)
f = [trace(p[n]) - t for (p, n), t in zip(((p, n) for p, nn in zip(ps, ns) for n in range(1, nn + 1)), target)]
J = [[F(0)] * 9 for _ in range(9)]
for col, l in enumerate(sel):
    s, i, j = pos[l // 2]
    d = [[zero] * 3 for _ in range(3)]
    d[i][j] = one if l % 2 == 0 else (F(0), F(1))
    A = As[s]
    des = [[[add(mul(d[r // 3][c // 3], conj(A[r % 3][c % 3])), mul(A[r // 3][c // 3], conj(d[r % 3][c % 3]))) for c in idx] for r in idx] for idx in idxs]
    vals = [n * traced_product(p[n - 1], de) for p, de, nn in zip(ps, des, ns) for n in range(1, nn + 1)]
    for row, v in enumerate(vals):
        J[row][col] = v
to_mp = lambda z: mp.mpf(z.numerator) / z.denominator
BM = mp.inverse(mp.matrix([[to_mp(z) for z in row] for row in J]))
B = [[F(mp.nstr(BM[i, j], 60)) for j in range(9)] for i in range(9)]
bn = max(sum(map(abs, row)) for row in B)
eta = max(abs(sum(B[i][j] * f[j] for j in range(9))) for i in range(9))
eps = max(sum(abs(F(i == j) - sum(B[i][k] * J[k][j] for k in range(9))) for j in range(9)) for i in range(9))
radius = F(1, 10 ** 30); H = F(10 ** 16); kappa = eps + bn * 81 * H * radius
print('Part A: exact residual and inverse defect (rational arithmetic)')
print(f'  ||B|| = {float(bn):.6f}, ||B f(y0)|| = {float(eta):.3e}, ||1 - BJ|| = {float(eps):.3e}, kappa = {float(kappa):.3e}')
check(max(map(abs, x)) < 2, '  A1 all centre coordinates have |.| < 2')
check(bn < 2, '  A2 ||B||_inf < 2')
check(eta < F(1, 10 ** 70), '  A3 ||B f(y0)||_inf < 1e-70')
check(eps < F(1, 10 ** 50), '  A4 ||1 - B J||_inf < 1e-50')
check(kappa < F(1, 4), '  A5 contraction constant kappa < 1/4')
check(eta + kappa * radius < radius, '  A6 the box of radius 1e-30 maps into itself: CERTIFIED')

# ------------------------------------------------------------------ Part C: the certified centre in floating point
q = 5
Af = [np.array([[complex(float(a[0]), float(a[1])) for a in row] for row in A]) for A in As]
E = sum(np.kron(A, A.conj()) for A in Af)
par = np.array([1, -1, -1]); G = np.kron(par, par)
ev, od = np.where(G == 1)[0], np.where(G == -1)[0]
chi_e = np.poly(E[np.ix_(ev, ev)]); chi_o = np.poly(E[np.ix_(od, od)])
print('Part C: the certified centre in floating point')
print('  chi_e coefficients', np.round(chi_e.real, 9), '  chi_o coefficients', np.round(chi_o.real, 9))
check(np.allclose(chi_e, [1, -6, 5, 0, 0, 0], atol=1e-7), '  C1 chi_e = z^3 (z-1)(z-5)')
check(np.allclose(chi_o, [1, -3, 7, -15, 25], atol=1e-7), '  C2 chi_o = z^4 - 3 z^3 + 7 z^2 - 15 z + 25')
alphas = np.roots([1, -3, 7, -15, 25])
for n in range(1, 13):
    Nn = q ** n + 1 - np.sum(alphas ** n).real
    st = np.trace(G[:, None] * np.linalg.matrix_power(E, n)).real
    check(abs(st - Nn) < 1e-8 * max(1, abs(Nn)), f'  C3 str E^{n} = N_{n} = {Nn:.0f}')
sys.path.insert(0, 'scripts')
import cmps_parity_supertrace as cps
D = 3
P3 = np.diag([1.0, -1.0, -1.0]).astype(complex)
Q = Af[0] - np.eye(D)
Rs = [Af[1], Af[2], np.zeros((D, D), complex)]
for n in (2, 3, 4, 5):
    cre = cps.creation_ops(n)
    psiP = cps.mps_state(n, 1.0, Q, Rs, P3, cre)
    nP = np.vdot(psiP, psiP).real
    Nn = q ** n + 1 - np.sum(alphas ** n).real
    check(abs(nP - Nn) < 1e-7 * Nn, f'  C4 explicit Jordan-Wigner Fock vector: ||Psi_P||^2 = {nP:.6f} = N_{n} = {Nn:.0f}')
    T = cps.translation_op(n, antiperiodic=False)
    check(np.linalg.norm(T @ psiP - psiP) < 1e-9, f'  C5 n={n}: Psi_P invariant under the periodic fermion translation')

# ------------------------------------------------------------------ Part B: the nine-letter tensor


def nine_letter(q, pi1, pi2):
    t = (q + 1) / 2; w = (q + 1) / 4; h = (q - 1) / (2 * np.sqrt(2))
    Dm = np.diag([pi1, pi2]); B0 = Dm / np.sqrt(t)
    b0 = B0.reshape(-1, 1)
    nu = (b0.conj().T @ b0)[0, 0].real
    if w < nu - 1e-12:
        return None
    S = np.sqrt(w) * np.eye(4) + ((np.sqrt(w - nu) - np.sqrt(w)) / nu) * (b0 @ b0.conj().T)
    assert np.allclose(S @ S, w * np.eye(4) - b0 @ b0.conj().T)
    Bs = [B0] + [(S @ np.eye(4)[:, l]).reshape(2, 2) for l in range(4)]
    As_ = []
    A = np.zeros((3, 3), complex); A[0, 0] = np.sqrt(t); A[1:, 1:] = B0; As_.append(A)
    for l in range(1, 5):
        A = np.zeros((3, 3), complex); A[1:, 1:] = Bs[l]; As_.append(A)
    for j in range(2):
        A = np.zeros((3, 3), complex); A[0, 1 + j] = np.sqrt(h); As_.append(A)
        A = np.zeros((3, 3), complex); A[1 + j, 0] = np.sqrt(h); As_.append(A)
    return As_


def check_nine(q, pi1, pi2, label):
    As_ = nine_letter(q, pi1, pi2)
    check(As_ is not None, f'  B0 {label}: q + 1 >= 4 sqrt q, construction exists')
    if As_ is None:
        return
    E = sum(np.kron(A, A.conj()) for A in As_)
    le = np.sort_complex(np.linalg.eigvals(E[np.ix_(ev, ev)]))
    lo = np.sort_complex(np.linalg.eigvals(E[np.ix_(od, od)]))
    check(np.allclose(np.sort(np.abs(le)), [0, 0, 0, 1, q], atol=1e-6), f'  B1 {label}: even spectrum {{1, q, 0, 0, 0}}')
    tgt = np.sort_complex(np.array([pi1, pi2, np.conj(pi1), np.conj(pi2)]))
    check(np.allclose(lo, tgt, atol=1e-8), f'  B2 {label}: odd spectrum = the four Frobenius values')
    check(np.linalg.norm(E @ E.conj().T - E.conj().T @ E) < 1e-9, f'  B3 {label}: doubled transfer is normal')
    for n in range(1, 9):
        Nn = 1 + q ** n - (pi1 ** n + pi2 ** n + np.conj(pi1) ** n + np.conj(pi2) ** n).real
        st = np.trace(G[:, None] * np.linalg.matrix_power(E, n)).real
        check(abs(st - Nn) < 1e-9 * max(1, abs(Nn)), f'  B4 {label}: str E^{n} = N_{n}')


print('Part B: the nine-letter tensor')
reps = []
for a in alphas:
    if not any(abs(np.conj(a) - b) < 1e-8 for b in reps):
        reps.append(a)
check_nine(25, reps[0] ** 2, reps[1] ** 2, 'q=25 (F_25 base change of the F_5 curve)')
check_nine(17, np.sqrt(17) * np.exp(0.3j), np.sqrt(17) * np.exp(2.1j), 'q=17 generic phases')
check_nine(16, 4 * np.exp(1.0j), 4 * np.exp(-2.5j), 'q=16 generic phases')
check(nine_letter(13, np.sqrt(13) * np.exp(0.3j), np.sqrt(13) * np.exp(2.1j)) is None, '  B5 q=13: construction fails (w < nu), as q + 1 < 4 sqrt q')

print(f'\n{NCHK} checks, {len(FAILS)} failures')
for m in FAILS:
    print('  FAIL', m)
sys.exit(1 if FAILS else 0)
