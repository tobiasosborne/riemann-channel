"""Re-verdict checks for reformulation.md version 2 (new or reworded statements only).
Independent: imports nothing from scripts/.  Run from the repository root."""
import numpy as np
ok = fail = 0
def check(name, cond, info=''):
    global ok, fail
    ok += bool(cond); fail += (not cond)
    print(('  PASS ' if cond else '  FAIL ') + name, info)
rng = np.random.default_rng(11)
# R4(i): Theta^# = Om^{-1} Theta^T Om, similar to Theta, and Theta^# = alpha - Theta for a derivation
g = 3; Om = np.kron(np.eye(g), np.array([[0., 1.], [-1., 0.]]))
S = rng.normal(size=(6, 6)); S = S + S.T
Th = 0.5 * np.eye(6) + np.linalg.solve(Om, S)
Tsh = np.linalg.solve(Om, Th.T @ Om)
check('R4(i) B(Th h,h\') = B(h, Th^# h\') with Th^# = Om^-1 Th^T Om', np.allclose(Th.T @ Om, Om @ Tsh))
check('R4(i) Th^# = alpha - Th for a derivation (alpha = 1)', np.allclose(Tsh, np.eye(6) - Th))
ev1, ev2 = np.sort_complex(np.linalg.eigvals(Th)), np.sort_complex(np.linalg.eigvals(np.eye(6) - Th))
check('R4(i) spec(alpha - Th) = spec(Th) as multisets (a similarity J exists)', all(np.min(np.abs(ev2 - l)) < 1e-8 for l in ev1) and all(np.min(np.abs(ev1 - l)) < 1e-8 for l in ev2))
# R4(iv): dim U(p,q)/(U(p)xU(q)) = 2pq reproduces the tangent counts 0, 2, 4, 0
for (p, q, d) in ((2, 0, 0), (1, 1, 2), (2, 1, 4), (3, 0, 0)):
    check(f'R4(iv) dim U({p},{q})/(U({p})xU({q})) = 2pq = {d}', 2 * p * q == d)
# R8(c): A (x) conj A multiplicative for the wedge for every a; an automorphism iff a != 0
def wedge(u, v):
    a0, a1, a2, a3 = u; b0, b1, b2, b3 = v
    return np.array([a0*b0, a0*b1+a1*b0, a0*b2+a2*b0, a0*b3+a3*b0+a1*b2-a2*b1])
for a in (1+2j, 0.3-0.7j, 0.0):
    F = np.diag([1, a, np.conj(a), abs(a)**2])
    mult = all(np.allclose(F @ wedge(u, v), wedge(F @ u, F @ v)) for u, v in
               ((rng.normal(size=4)+1j*rng.normal(size=4), rng.normal(size=4)+1j*rng.normal(size=4)) for _ in range(10)))
    check(f'R8(c) a={a}: multiplicative for the wedge', mult)
    check(f'R8(c) a={a}: bijective (automorphism) iff a != 0', (abs(np.linalg.det(F)) > 1e-12) == (a != 0))
# R3(b) proof, even k for a reflection
l, th = np.log(7.0), 1.1
O = np.array([[np.cos(th), np.sin(th)], [np.sin(th), -np.cos(th)]]); A = np.exp(l/2) * O
for k in (1, 2, 3, 4):
    Ak = np.linalg.matrix_power(A, k); Ami = np.linalg.inv(Ak)
    c_neg = np.linalg.det(Ami) * np.sign(np.linalg.det(np.eye(2) - Ak))
    check(f'R3(b) reflection c_(-{k}) = det(A^-k) sgn det(1-A^k) = e^(-kl)', abs(c_neg - np.exp(-k*l)) < 1e-12)
print(f'\nscratch_den_v2: {ok} pass, {fail} fail')
