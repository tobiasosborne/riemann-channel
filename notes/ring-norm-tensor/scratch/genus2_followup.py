#!/usr/bin/env python3
"""Follow-up to weil_ring_norm_check.py.  Usage: python3 genus2_followup.py {fermionic|bosonic}

fermionic: a GENERIC ordinary genus-2 curve (e1 != 0), search on C^{1|2} for the minimal
           species sets (nb even, nf odd) in {(1,1),(1,2),(2,1),(2,2)}, verify the explicit
           Jordan-Wigner Fock vector norm for the best one, print the tensors.
bosonic:   the same curve, bosonic-only C^{2|2} (cancellation allowed), more effort, report
           the even/odd spectra of the best point.
"""
import sys, time, itertools
import numpy as np
sys.path.insert(0, 'scripts')
sys.path.insert(0, '/tmp/claude-1000/-home-tobiasosborne-Projects-riemann-channel/16d23615-d982-4d9c-af10-3aa1daaee0e5/scratchpad')
from scipy.optimize import least_squares

mode = sys.argv[1]
rng = np.random.default_rng(7 if mode == 'fermionic' else 11)

# ---- copy of the helpers (kept local so this file is self-contained)
from artin_schreier_mps import irreducible, polymulmod, polypow


class GF:
    def __init__(self, p, n):
        self.p, self.n = p, n
        self.f = irreducible(p, n)
        self.elems = [list(c) for c in itertools.product(range(p), repeat=n)]

    def mul(self, a, b):
        return polymulmod(a, b, self.f, self.p)

    def add(self, a, b):
        return [(x + y) % self.p for x, y in zip(a, b)]

    def scal(self, c, a):
        return [(c * x) % self.p for x in a]

    def const(self, c):
        return [c % self.p] + [0] * (self.n - 1)

    def chi(self, z):
        if not any(z):
            return 0
        w = polypow(z, (self.p ** self.n - 1) // 2, self.f, self.p)
        return 1 if w == self.const(1) else -1


def count_hyperelliptic(p, n, coeffs):
    F = GF(p, n)
    tot = 0
    for x in F.elems:
        val, xp = F.const(0), F.const(1)
        for c in coeffs:
            if c:
                val = F.add(val, F.scal(c, xp))
            xp = F.mul(xp, x)
        tot += 1 + F.chi(val)
    return tot + 1


def doubled_transfer(As):
    return sum(np.kron(A, A.conj()) for A in As)


def graded_sectors(m, k):
    par = np.array([1] * m + [-1] * k)
    G = np.kron(par, par)
    return np.where(G == 1)[0], np.where(G == -1)[0], G


def str_powers(As, m, k, nmax):
    E = doubled_transfer(As)
    ev, od, G = graded_sectors(m, k)
    out, En = [], np.eye(E.shape[0], dtype=complex)
    for n in range(1, nmax + 1):
        En = En @ E
        out.append(np.trace(G[:, None] * En))
    return np.array(out)


def build(params, m, k, nb, nf):
    D = m + k
    As, idx = [], 0
    for s in range(nb):
        A = np.zeros((D, D), complex)
        npp, nmm = m * m, k * k
        A[:m, :m] = (params[idx:idx + npp] + 1j * params[idx + npp:idx + 2 * npp]).reshape(m, m); idx += 2 * npp
        A[m:, m:] = (params[idx:idx + nmm] + 1j * params[idx + nmm:idx + 2 * nmm]).reshape(k, k); idx += 2 * nmm
        As.append(A)
    for s in range(nf):
        A = np.zeros((D, D), complex)
        npm = m * k
        A[:m, m:] = (params[idx:idx + npm] + 1j * params[idx + npm:idx + 2 * npm]).reshape(m, k); idx += 2 * npm
        A[m:, :m] = (params[idx:idx + npm] + 1j * params[idx + npm:idx + 2 * npm]).reshape(k, m); idx += 2 * npm
        As.append(A)
    return As


def nparams(m, k, nb, nf):
    return nb * 2 * (m * m + k * k) + nf * 4 * m * k


p = 5
NMAX = 12


def residual(params, m, k, nb, nf, target):
    st = str_powers(build(params, m, k, nb, nf), m, k, NMAX)
    w = np.array([p ** (-n / 2) for n in range(1, NMAX + 1)])
    r = (st - target) * w
    r = np.concatenate([r.real, r.imag])
    return np.where(np.isfinite(r), r, 1e6)


def search(m, k, nb, nf, restarts, label, target, nfev=3000):
    best, t0 = None, time.time()
    for r in range(restarts):
        x0 = rng.standard_normal(nparams(m, k, nb, nf)) * 0.7
        try:
            res = least_squares(residual, x0, args=(m, k, nb, nf, target), bounds=(-4, 4), max_nfev=nfev, xtol=1e-15, ftol=1e-15, gtol=1e-15)
        except Exception as e:
            print(f'    restart {r}: optimiser failed ({type(e).__name__})'); continue
        if best is None or res.cost < best.cost:
            best = res
        if best.cost < 1e-22:
            break
    print(f'  {label}: best cost {best.cost:.3e} after {r+1} restarts ({time.time()-t0:.1f}s)', flush=True)
    return best


def report(res, m, k, nb, nf, label, alphas):
    As = build(res.x, m, k, nb, nf)
    E = doubled_transfer(As)
    ev, od, G = graded_sectors(m, k)
    le = np.linalg.eigvals(E[np.ix_(ev, ev)])
    lo = np.linalg.eigvals(E[np.ix_(od, od)])
    st = str_powers(As, m, k, 20)
    tgt = np.array([p ** n + 1 - np.sum(alphas ** n) for n in range(1, 21)])
    print(f'  {label}: even eigenvalues {np.round(np.sort_complex(le), 4)}')
    print(f'  {label}: odd  eigenvalues {np.round(np.sort_complex(lo), 4)}')
    print(f'  {label}: target alphas    {np.round(np.sort_complex(alphas), 4)}')
    print(f'  {label}: max |str E^n - N_n| / q^(n/2), n<=20: {np.max(np.abs(st - tgt) / p ** (np.arange(1, 21) / 2)):.2e}')
    return As, tgt


# ---- a generic ordinary genus-2 curve over F_5
from sympy import Poly, symbols, gcd
X = symbols('x')
for f5 in ([1, 0, 1, 0, 0, 1], [2, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1], [3, 0, 1, 1, 0, 1], [1, 3, 0, 1, 0, 1], [4, 1, 0, 0, 1, 1]):
    fp = Poly(sum(c * X ** i for i, c in enumerate(f5)), X, modulus=p)
    if gcd(fp, fp.diff(X)).degree() != 0:
        continue
    N = [count_hyperelliptic(p, n, f5) for n in range(1, 5)]
    s1, s2 = p + 1 - N[0], p ** 2 + 1 - N[1]
    e1, e2 = s1, (s1 * s1 - s2) / 2
    alphas = np.roots([1, -e1, e2, -p * e1, p * p])
    if e1 != 0 and e2 != 0 and np.min(np.abs(alphas.real)) > 0.2:
        break
print(f'curve y^2 = {fp.as_expr()} over F_5: N_n = {N}; L(u) = 1 - ({e1}) u + ({e2:.0f}) u^2 - ({p*e1}) u^3 + 25 u^4')
print(f'alphas = {np.round(alphas, 5)}, |alpha|^2 = {np.round(np.abs(alphas)**2, 6)}')
pred = [p ** n + 1 - np.sum(alphas ** n).real for n in range(1, 5)]
assert np.allclose(pred, N, atol=1e-6)
target = np.array([p ** n + 1 - np.sum(alphas ** n) for n in range(1, NMAX + 1)])

if mode == 'fermionic':
    results = {}
    for (nb, nf) in [(1, 1), (2, 1), (1, 2), (2, 2)]:
        results[(nb, nf)] = search(1, 2, nb, nf, 10, f'C^(1|2), {nb} even + {nf} odd species', target)
    ok = {key: r.cost < 1e-20 for key, r in results.items()}
    print('solvable:', ok)
    best_key = min((k_ for k_ in results if ok[k_]), key=lambda k_: sum(k_), default=None)
    if best_key is None:
        best_key = min(results, key=lambda k_: results[k_].cost)
    nb, nf = best_key
    As, tgt = report(results[best_key], 1, 2, nb, nf, f'C^(1|2) {best_key}', alphas)
    np.set_printoptions(precision=4, suppress=True, linewidth=150)
    for i, A in enumerate(As):
        print(f'  tensor {i} ({"even" if i < nb else "odd"}):\n{A}')
    # explicit Jordan-Wigner check with the parity script's lattice model (local: empty, boson, f1, f2)
    import cmps_parity_supertrace as cps
    D = 3
    P3 = np.diag([1.0, -1.0, -1.0]).astype(complex)
    even = As[:nb] + [np.zeros((D, D), complex)] * (2 - nb)
    odd = As[nb:] + [np.zeros((D, D), complex)] * (2 - nf)
    Q = even[0] - np.eye(D)
    Rs = [even[1], odd[0], odd[1]]
    for n in (2, 3, 4, 5):
        cre = cps.creation_ops(n)
        psiP = cps.mps_state(n, 1.0, Q, Rs, P3, cre)
        nP = np.vdot(psiP, psiP).real
        print(f'  n={n}: ||Psi_P||^2 (explicit JW Fock vector) = {nP:.8f}   N_n = {tgt[n-1].real:.8f}   diff {nP - tgt[n-1].real:.1e}')
        T = cps.translation_op(n, antiperiodic=False)
        print(f'        periodic translation invariance: {np.linalg.norm(T @ psiP - psiP):.1e}')
        occ = cps.occupations(n)
        nf_ = (occ >= 2).sum(axis=0)
        w = np.abs(psiP) ** 2
        print(f'        weight by fermion number: ' + ', '.join(f'F={f}: {w[nf_ == f].sum():.4f}' for f in range(n + 1)))
else:
    res = search(2, 2, 3, 0, 6, 'bosonic only, C^(2|2), 3 species', target, nfev=8000)
    report(res, 2, 2, 3, 0, 'bosonic C^(2|2)', alphas)
    res = search(2, 2, 4, 0, 4, 'bosonic only, C^(2|2), 4 species', target, nfev=8000)
    report(res, 2, 2, 4, 0, 'bosonic C^(2|2) 4sp', alphas)
