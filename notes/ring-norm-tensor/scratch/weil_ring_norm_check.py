#!/usr/bin/env python3
"""Double-check of the 2026-09-14 discussion "Weil numerator as a boson-fermion ring norm".

Claims under test (HANDOFF.md, section "Discussion 2026-09-14"):
  C1  For an elliptic curve E/F_q with Frobenius eigenvalue alpha, the bosonic graded MPS
      A_s = diag(a_s, c a_s), sum |a_s|^2 = 1, |c|^2 = q, c = alpha, with the P-closed
      (periodic-fermion / Ramond) ring has ||Psi_P||^2 = |1 - c^n|^2 = #E(F_{q^n}) exactly.
  C2  The untwisted closure gives 1 + q^n + alpha^n + conj(alpha)^n, which is not the count
      (thm:no-ungraded-trace).
  C3  Cauchy-Schwarz on the cross transfer gives |alpha| <= sqrt(q) "for free" when the two
      bond blocks are decoupled; equality (the functional equation alpha*conj(alpha) = q)
      iff the blocks are proportional.
  C4  Genus >= 2 "needs cancellations in the (-,-) block and presumably fermionic couplings".
      Sharpened here to a theorem: for block-diagonal (purely bosonic) tensors on any C^{m|k}
      with net even doubled spectrum exactly {1,q} and no even-odd cancellation,
      sum_{odd eigenvalues} |mu|^2 <= 2 * Tr(++) * Tr(--) = 2q, so 2 g q <= 2q, g <= 1.
      Then a numerical search: bosonic-only C^{1|2} (must fail), bosonic-only C^{2|2}
      (cancellation allowed), and C^{1|2} with two fermionic species.
  C5  For the only genus-1 quadratic Artin-Schreier curve (q=3, g=x^2, supersingular) the
      honest "indicator" MPS built from the curve (bond dim 3, bosonic, periodic closure)
      has norm (N_n - 1)/q only at odd n; at even n it has the wrong sign of alpha^n+conj^n.

All counts are brute force in F_{p^n}.  Deterministic.  Run from the repo root.
"""
import sys, itertools, time
import numpy as np
sys.path.insert(0, 'scripts')
from artin_schreier_mps import irreducible, polymulmod, polypow

rng = np.random.default_rng(20260914)
NCHK = 0
FAILS = []


def check(cond, msg):
    global NCHK
    NCHK += 1
    if not cond:
        FAILS.append(msg)
    print(('PASS ' if cond else 'FAIL ') + msg)


def banner(s):
    print('\n' + '=' * 100 + '\n' + s + '\n' + '=' * 100)


# ------------------------------------------------------------------ finite fields F_{p^n}
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
        """Quadratic character of F_{p^n}: z^{(p^n-1)/2} in {0, +1, -1}."""
        if not any(z):
            return 0
        w = polypow(z, (self.p ** self.n - 1) // 2, self.f, self.p)
        if w == self.const(1):
            return 1
        assert w == self.const(self.p - 1), w
        return -1

    def trace(self, z):
        t = [0] * self.n
        w = z
        for _ in range(self.n):
            t = self.add(t, w)
            w = polypow(w, self.p, self.f, self.p)
        assert all(c == 0 for c in t[1:])
        return t[0]


def count_hyperelliptic(p, n, coeffs):
    """#{(x,y) in F_{p^n}^2 : y^2 = f(x)} + 1 (odd-degree f, one point at infinity).
    coeffs = [c_0, ..., c_d] low -> high."""
    F = GF(p, n)
    tot = 0
    for x in F.elems:
        val = F.const(0)
        xp = F.const(1)
        for c in coeffs:
            if c:
                val = F.add(val, F.scal(c, xp))
            xp = F.mul(xp, x)
        tot += 1 + F.chi(val)
    return tot + 1


def count_artin_schreier_q3(n):
    """#{(x,y) in F_{3^n}^2 : y^3 - y = x^2} + 1 = 1 + 3 * #{x : tr(x^2) = 0}."""
    F = GF(3, n)
    k = sum(1 for x in F.elems if F.trace(F.mul(x, x)) == 0)
    return 1 + 3 * k, k


# ------------------------------------------------------------------ MPS machinery
def doubled_transfer(As):
    return sum(np.kron(A, A.conj()) for A in As)


def graded_sectors(m, k):
    """Index sets of the even and odd sectors of C^{m|k} (x) conj C^{m|k}."""
    D = m + k
    par = np.array([1] * m + [-1] * k)
    G = np.kron(par, par)                      # doubled-bond parity Gamma = P (x) conj P
    return np.where(G == 1)[0], np.where(G == -1)[0], G


def str_powers(As, m, k, nmax):
    E = doubled_transfer(As)
    ev, od, G = graded_sectors(m, k)
    out = []
    En = np.eye(E.shape[0], dtype=complex)
    for n in range(1, nmax + 1):
        En = En @ E
        out.append(np.trace(G[:, None] * En))
    return np.array(out)


def mps_vector(As, B, n):
    """Psi_B = sum_s Tr[B A_{s1} ... A_{sn}] |s>, bosonic (no statistics signs)."""
    d = len(As)
    D = As[0].shape[0]
    M = B.reshape(1, D, D)                     # accumulate B A_{s1} ... over configurations
    for _ in range(n):
        M = np.einsum('cij,sjk->csik', M, np.array(As)).reshape(-1, D, D)
    return np.einsum('cii->c', M)


def frobenius_eigs_genus1(p, N1):
    a = p + 1 - N1
    disc = a * a - 4 * p
    return (a + np.sqrt(complex(disc))) / 2


# ================================================================== C1, C2: genus 1
banner('C1/C2  Elliptic curves: brute-force counts vs |1 - alpha^n|^2 vs explicit MPS norms')
curves = [(5, [1, 1, 0, 1]), (7, [1, 1, 0, 1]), (11, [1, 1, 0, 1]), (7, [3, 2, 0, 1])]
for p, coeffs in curves:
    disc = (4 * coeffs[1] ** 3 + 27 * coeffs[0] ** 2) % p
    assert disc != 0, 'singular'
    nmax = 5 if p <= 7 else 3
    counts = [count_hyperelliptic(p, n, coeffs) for n in range(1, nmax + 1)]
    alpha = frobenius_eigs_genus1(p, counts[0])
    print(f'\ny^2 = x^3 + {coeffs[1]} x + {coeffs[0]} over F_{p}:  N_n = {counts},  alpha = {alpha:.6f}, |alpha|^2 = {abs(alpha)**2:.6f}')
    check(abs(abs(alpha) ** 2 - p) < 1e-9, f'  |alpha|^2 = q  (Hasse, p={p})')
    hasse = [abs(1 - alpha ** n) ** 2 for n in range(1, nmax + 1)]
    check(np.allclose(hasse, counts, atol=1e-6), f'  N_n = |1 - alpha^n|^2 for n<=({nmax})  (p={p})')

    # the minimal graded bond C^{1|1}, bosonic tensor A_s = diag(a_s, c a_s), c = alpha
    d = 3
    a = rng.standard_normal(d) + 1j * rng.standard_normal(d)
    a /= np.linalg.norm(a)
    As = [np.diag([a[s], alpha * a[s]]) for s in range(d)]
    P = np.diag([1.0, -1.0]).astype(complex)
    strs = str_powers(As, 1, 1, nmax)
    trs = [np.trace(np.linalg.matrix_power(doubled_transfer(As), n)) for n in range(1, nmax + 1)]
    check(np.allclose(strs.real, counts, atol=1e-6) and np.allclose(strs.imag, 0, atol=1e-9),
          f'  str E^n = N_n on the doubled C^(1|1) bond  (p={p})')
    untw = [1 + p ** n + alpha ** n + np.conj(alpha) ** n for n in range(1, nmax + 1)]
    check(np.allclose(trs, untw, atol=1e-6), f'  Tr E^n = 1 + q^n + alpha^n + conj  (untwisted, p={p})')
    check(not np.allclose(trs, counts, atol=1e-6), f'  Tr E^n != N_n  (untwisted closure is not the count, p={p})')
    for n in range(1, min(nmax, 4) + 1):
        psiP = mps_vector(As, P, n)
        psi1 = mps_vector(As, np.eye(2, dtype=complex), n)
        psip = mps_vector(As, np.diag([1.0, 0.0]).astype(complex), n)
        psim = mps_vector(As, np.diag([0.0, 1.0]).astype(complex), n)
        check(abs(np.vdot(psiP, psiP).real - counts[n - 1]) < 1e-8, f'  ||Psi_P||^2 = N_{n} as an explicit vector in C^{d**n}  (p={p})')
        check(abs(np.vdot(psi1, psi1).real - untw[n - 1].real) < 1e-8, f'  ||Psi_1||^2 = 1+q^n+alpha^n+conj  (n={n}, p={p})')
        check(np.allclose(psiP, psip - psim), f'  Psi_P = Psi_+ - Psi_-  (n={n})')
        check(np.allclose(psim, alpha ** n * psip), f'  Psi_- = alpha^n Psi_+ : the two closures are parallel  (n={n})')
        # the physical state is a product state: Psi_P is rank one under every bipartition
        Mx = psiP.reshape(d, -1)
        sv = np.linalg.svd(Mx, compute_uv=False)
        check(sv[1] < 1e-10 * sv[0] if len(sv) > 1 else True, f'  Psi_P is a product state (Schmidt rank 1)  (n={n})')

# ================================================================== C3: Cauchy-Schwarz for free
banner('C3  Decoupled bosonic C^(1|1): str E^n = ||a||^{2n} + ||b||^{2n} - <a,b>^n - conj, |<a,b>| <= ||a|| ||b||')
for trial in range(3):
    d = 4
    a = rng.standard_normal(d) + 1j * rng.standard_normal(d)
    b = rng.standard_normal(d) + 1j * rng.standard_normal(d)
    a /= np.linalg.norm(a)
    b *= np.sqrt(5.0) / np.linalg.norm(b)          # ||b||^2 = q = 5
    As = [np.diag([a[s], b[s]]) for s in range(d)]
    ab = np.vdot(a, b)                              # <a,b>, conjugate-linear in a
    strs = str_powers(As, 1, 1, 6)
    pred = [1 + 5.0 ** n - ab ** n - np.conj(ab) ** n for n in range(1, 7)]
    check(np.allclose(strs, pred), f'  trial {trial}: str E^n = 1 + q^n - <a,b>^n - conj')
    check(abs(ab) ** 2 < 5.0, f'  trial {trial}: |<a,b>|^2 = {abs(ab)**2:.4f} < q = 5 strictly (blocks not proportional)')
    # the odd eigenvalues alpha = conj<a,b>, beta = <a,b>: alpha*beta = |<a,b>|^2 != q, so the
    # functional equation (alpha beta = q) FAILS unless equality in Cauchy-Schwarz
print('  Reading: the functional equation alpha*conj(alpha) = q is exactly equality in Cauchy-Schwarz,')
print('  i.e. b = c a; then |alpha| = sqrt(q) is automatic (RH manifest) but alpha = c is put in by hand.')

# ================================================================== C4: no-go, block diagonal bosonic
banner('C4a  Bosonic block-diagonal C^(m|k): sum_odd |mu|^2 <= 2 Tr(++) Tr(--)  (Schur + Cauchy-Schwarz), random instances')
for (m, k, d) in [(1, 1, 3), (1, 2, 4), (2, 2, 3), (1, 3, 5), (3, 2, 4)]:
    for trial in range(20):
        As = []
        for s in range(d):
            A = np.zeros((m + k, m + k), complex)
            A[:m, :m] = rng.standard_normal((m, m)) + 1j * rng.standard_normal((m, m))
            A[m:, m:] = rng.standard_normal((k, k)) + 1j * rng.standard_normal((k, k))
            As.append(A)
        E = doubled_transfer(As)
        ev, od, G = graded_sectors(m, k)
        Eodd = E[np.ix_(od, od)]
        Eeven = E[np.ix_(ev, ev)]
        tpp = sum(np.linalg.norm(A[:m, :m]) ** 2 for A in As)   # Tr of the (++) block
        tmm = sum(np.linalg.norm(A[m:, m:]) ** 2 for A in As)   # Tr of the (--) block
        lhs = np.sum(np.abs(np.linalg.eigvals(Eodd)) ** 2)
        hs = np.linalg.norm(Eodd) ** 2
        ok = lhs <= hs + 1e-9 and hs <= 2 * tpp * tmm + 1e-9
        if not ok or trial == 0:
            check(ok, f'  C^({m}|{k}), d={d}: sum|mu|^2={lhs:.3f} <= ||odd||_HS^2={hs:.3f} <= 2 t+ t- = {2*tpp*tmm:.3f}')
print('  Hence with net even spectrum {1,q} and no cancellation: 2 g q = sum_odd |alpha|^2 <= 2q, i.e. g <= 1.')
print('  Odd (fermionic) species add Hilbert-Schmidt mass to the odd block but NO trace to the even block,')
print('  so the bound is void for them; cancellation (extra even-odd pairs) also evades it.')

# ================================================================== genus 2 data
banner('C4b  A genus-2 curve over F_5: brute-force counts, L-polynomial, Frobenius eigenvalues')
p = 5
from sympy import Poly, symbols, gcd
X = symbols('x')
# pick an ORDINARY genus-2 curve: four distinct Frobenius eigenvalues with nonzero real parts
for f5 in ([1, 1, 0, 0, 0, 1], [1, 2, 0, 0, 0, 1], [1, 0, 1, 0, 0, 1], [2, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1], [3, 0, 1, 1, 0, 1]):
    fp = Poly(sum(c * X ** i for i, c in enumerate(f5)), X, modulus=p)
    if gcd(fp, fp.diff(X)).degree() != 0:
        continue
    N = [count_hyperelliptic(p, n, f5) for n in range(1, 5)]
    s1, s2 = p + 1 - N[0], p ** 2 + 1 - N[1]
    e1, e2 = s1, (s1 * s1 - s2) / 2
    Lrev = [1, -e1, e2, -p * e1, p * p]        # z^4 - e1 z^3 + e2 z^2 - q e1 z + q^2
    alphas = np.roots(Lrev)
    if np.min(np.abs(alphas.real)) > 0.3 and np.min(np.abs(alphas[:, None] - alphas[None, :])[~np.eye(4, dtype=bool)]) > 0.3:
        break
print(f'y^2 = {fp.as_expr()} over F_5: N_n = {N}')
print(f'L-polynomial 1 - {e1} u + {e2:.0f} u^2 - {p*e1} u^3 + {p*p} u^4 ; alphas = {np.round(alphas, 5)}')
check(np.allclose(np.abs(alphas) ** 2, p), '  all |alpha_j|^2 = q (RH for the curve)')
pred = [p ** n + 1 - np.sum(alphas ** n).real for n in range(1, 5)]
check(np.allclose(pred, N, atol=1e-6), '  N_3, N_4 predicted from N_1, N_2 agree with brute force')
jac = [np.prod(1 - alphas ** n).real for n in range(1, 4)]
print(f'  #Jac(F_{{5^n}}) = prod_j (1 - alpha_j^n) = {np.round(jac, 3)}')
# one representative per conjugate pair
reps = []
for al in alphas:
    if not any(abs(np.conj(al) - r) < 1e-8 for r in reps):
        reps.append(al)
assert len(reps) == 2, reps
As1 = [np.diag([1.0, reps[0]])]
As2 = [np.diag([1.0, reps[1]])]
Atp = [np.kron(A1, A2) for A1 in As1 for A2 in As2]
Ptp = np.kron(np.diag([1, -1]), np.diag([1, -1])).astype(complex)
E = doubled_transfer(Atp)
Gtp = np.kron(np.diag(Ptp), np.diag(Ptp))
st = [np.trace(Gtp[:, None] * np.linalg.matrix_power(E, n)).real for n in range(1, 4)]
check(np.allclose(st, jac), '  str over the product bond C^(1|1)(x)C^(1|1) = #Jac(F_{q^n})  (doubled bond = Lambda* H^1 = H*(Jac))')

# ================================================================== C4c: numerical search
banner('C4c  Search for a single P-closed ring norm with str E^n = N_n (genus 2), three tensor classes')
from scipy.optimize import least_squares

NMAX = 12


def build(params, m, k, nb, nf):
    """Tensors on C^{m|k}: nb even (block-diagonal) species, nf odd (block-off-diagonal) species."""
    D = m + k
    As = []
    idx = 0
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
    assert idx == len(params)
    return As


def nparams(m, k, nb, nf):
    return nb * 2 * (m * m + k * k) + nf * 4 * m * k


def residual(params, m, k, nb, nf, target):
    As = build(params, m, k, nb, nf)
    st = str_powers(As, m, k, NMAX)
    w = np.array([p ** (-n / 2) for n in range(1, NMAX + 1)])
    r = (st - target) * w
    r = np.concatenate([r.real, r.imag])
    return np.where(np.isfinite(r), r, 1e6)


target = np.array([p ** n + 1 - np.sum(alphas ** n) for n in range(1, NMAX + 1)])


def search(m, k, nb, nf, restarts, label):
    best = None
    t0 = time.time()
    for r in range(restarts):
        x0 = rng.standard_normal(nparams(m, k, nb, nf)) * 0.7
        try:
            res = least_squares(residual, x0, args=(m, k, nb, nf, target), bounds=(-4, 4), max_nfev=3000, xtol=1e-15, ftol=1e-15, gtol=1e-15)
        except Exception as e:
            print(f'    restart {r}: optimiser failed ({type(e).__name__})')
            continue
        if best is None or res.cost < best.cost:
            best = res
        if best.cost < 1e-20:
            break
    print(f'  {label}: best cost {best.cost:.3e} after {r+1} restarts ({time.time()-t0:.1f}s)')
    return best


def report_solution(res, m, k, nb, nf, label):
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
    return As, st, tgt


resA = search(1, 2, 3, 0, 12, 'bosonic only, C^(1|2), 3 species')
check(resA.cost > 1e-6, '  bosonic-only C^(1|2) cannot reach the count (as the no-go requires)')
resB = search(2, 2, 3, 0, 8, 'bosonic only, C^(2|2), 3 species (cancellation allowed)')
print(f'  (bosonic-only C^(2|2) residual {resB.cost:.3e}: {"reached" if resB.cost < 1e-16 else "not reached"} within the budget)')
resC = search(1, 2, 2, 2, 12, 'C^(1|2), 2 even + 2 odd (fermionic) species')
foundC = resC.cost < 1e-16
check(foundC, '  a genus-2 count IS a single P-closed ring norm with fermionic tensors on C^(1|2)')
if foundC:
    AsC, stC, tgtC = report_solution(resC, 1, 2, 2, 2, 'fermionic C^(1|2)')
if resB.cost < 1e-16:
    report_solution(resB, 2, 2, 3, 0, 'bosonic C^(2|2)')

# explicit fermionic lattice vector: norm of the Ramond ring with Jordan-Wigner fermions
if foundC:
    banner('C4d  The found genus-2 tensors: ||Psi_P||^2 as the norm of an explicit Jordan-Wigner Fock vector')
    import cmps_parity_supertrace as cps
    # species: cps uses local {empty, boson, f1, f2}; A_k = A0 (x) 1 + sum_alpha R_alpha (x) c^dag_{alpha,k}
    A_empty, A_bos, A_f1, A_f2 = AsC
    D = 3
    Q = A_empty - np.eye(D)
    P3 = np.diag([1.0, -1.0, -1.0]).astype(complex)
    for n in (2, 3, 4):
        cre = cps.creation_ops(n)
        psiP = cps.mps_state(n, 1.0, Q, [A_bos, A_f1, A_f2], P3, cre)
        psi1 = cps.mps_state(n, 1.0, Q, [A_bos, A_f1, A_f2], np.eye(D, dtype=complex), cre)
        nP = np.vdot(psiP, psiP).real
        n1 = np.vdot(psi1, psi1).real
        E = doubled_transfer(AsC)
        G = np.kron(np.diag(P3), np.diag(P3)).real
        trn = np.trace(np.linalg.matrix_power(E, n)).real
        check(abs(nP - tgtC[n - 1].real) < 1e-7 * max(1, abs(tgtC[n - 1])), f'  n={n}: ||Psi_P||^2 = {nP:.6f} = N_{n} = {tgtC[n-1].real:.6f} (explicit Fock vector, JW signs)')
        check(abs(n1 - trn) < 1e-7 * max(1, abs(trn)), f'  n={n}: ||Psi_1||^2 = {n1:.6f} = Tr E^n (untwisted ring)')
        # Ramond translation invariance
        T = cps.translation_op(n, antiperiodic=False)
        Tap = cps.translation_op(n, antiperiodic=True)
        check(np.allclose(T @ psiP, psiP), f'  n={n}: Psi_P is invariant under the periodic fermion translation')
        check(np.allclose(Tap @ psi1, psi1), f'  n={n}: Psi_1 is invariant under the antiperiodic translation')

# ================================================================== C5: Artin-Schreier genus 1
banner('C5  y^3 - y = x^2 over F_3 (genus 1, supersingular): the honest indicator MPS vs the count')
alpha3 = 1j * np.sqrt(3)
for n in range(1, 7):
    Nn, kn = count_artin_schreier_q3(n)
    twisted = 1 + 3 ** n - alpha3 ** n - np.conj(alpha3) ** n
    untwisted = 1 + 3 ** n + alpha3 ** n + np.conj(alpha3) ** n
    # indicator MPS: Phi = (1/3) sum_a (sum_s psi(a s^2)|s>)^{(x)n}; ||Phi||^2 = #{x in F_3^n : sum x_i^2 = 0}
    # equals #{x : tr(x^2) = 0} only when a self-dual normal basis exists (n odd)
    kdiag = sum(1 for x in itertools.product(range(3), repeat=n) if sum(v * v for v in x) % 3 == 0)
    print(f'  n={n}: N_n = {Nn:3d}; twisted 1+q^n-a^n-conj = {twisted.real:6.0f}; untwisted 1+q^n+a^n+conj = {untwisted.real:6.0f}; '
          f'1 + 3 * #{{sum x_i^2 = 0}} = {1 + 3 * kdiag:4d}')
    check(abs(twisted.real - Nn) < 1e-9, f'  n={n}: N_n = twisted (P-closed) formula')
    check((1 + 3 * kdiag == Nn) == (n % 2 == 1), f'  n={n}: the periodic bosonic indicator MPS matches iff n is odd')

# ================================================================== summary
banner('SUMMARY')
print(f'{NCHK} checks, {len(FAILS)} failures')
for f_ in FAILS:
    print('  FAIL', f_)
