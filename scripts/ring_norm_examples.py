#!/usr/bin/env python3
"""Explicit matrix product states of curves of genus 0..3: matrices, entanglement, parent Hamiltonians.

Evidence for shard 06g (num:ring-norm-examples).  Author: claude:fable-5.1, 2026-09-14.

The states (all with the P-closed / Ramond ring of shard 02g, str E^n = #C(F_{q^n})):
  genus 0  P^1/F_5:                 bond C^2 ungraded, letters {inf} u F_5, A_inf = e11, A_s = e22
  genus 1  y^2 = x^3+x+1 / F_5:     bond C^{1|1}, A_s = phi_s diag(1, pi), phi = (1,1)/sqrt2, pi = (-3 + i sqrt 11)/2
  genus 2  y^2 = x^5+x^3+x^2-2 / F_5: bond C^{1|2}, the certified 2 even + 1 odd letters (shard 06f)
  genus 2  same curve over F_25:      bond C^{1|2}, the closed-form 5 even + 4 odd letters (thm:nine-letter-tensor)
  genus 3  y^2 = x^7+x+1 / F_37:      bond C^{1|3}, the closed form with 10 even + 6 odd letters
For each: transfer spectrum and correlation lengths (RH reads: every odd mode has xi = 2/log q);
block Schmidt spectra and entropies of the P-closed ring from the D^2 x D^2 Gram formula, checked
against explicit vectors; injectivity length; parent Hamiltonian (projectors onto the complement
of the k-site support), its ring ground space and gap; for the fermionic examples the block
entropies of the explicit Jordan--Wigner Fock vector against the Kronecker (spin) contraction.
Deterministic; exits nonzero on any FAIL.  Run from the repository root:
    python3 scripts/ring_norm_examples.py > outputs/ring_norm_examples.txt
"""
import sys, itertools
import numpy as np
sys.path.insert(0, 'scripts')
from artin_schreier_mps import irreducible, polymulmod, polypow

np.set_printoptions(precision=5, suppress=True, linewidth=150)
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


# ------------------------------------------------------------------ finite fields and counts
class GF:
    def __init__(self, p, n):
        self.p, self.n, self.f = p, n, irreducible(p, n)
        self.elems = [list(c) for c in itertools.product(range(p), repeat=n)]

    def mul(self, a, b):
        return polymulmod(a, b, self.f, self.p)

    def add(self, a, b):
        return [(x + y) % self.p for x, y in zip(a, b)]

    def const(self, c):
        return [c % self.p] + [0] * (self.n - 1)

    def chi(self, z):
        if not any(z):
            return 0
        w = polypow(z, (self.p ** self.n - 1) // 2, self.f, self.p)
        return 1 if w == self.const(1) else -1


def count_hyper(p, n, coeffs):
    F = GF(p, n)
    tot = 0
    for x in F.elems:
        val, xp = F.const(0), F.const(1)
        for c in coeffs:
            if c:
                val = F.add(val, [(c * t) % p for t in xp])
            xp = F.mul(xp, x)
        tot += 1 + F.chi(val)
    return tot + 1


def lpoly_roots(q, counts, g):
    s = [q ** k + 1 - counts[k - 1] for k in range(1, g + 1)]
    e = [1.0]
    for k in range(1, g + 1):
        e.append(sum((-1) ** (i - 1) * e[k - i] * s[i - 1] for i in range(1, k + 1)) / k)
    coeffs = [(-1) ** k * e[k] for k in range(g + 1)]
    full = coeffs + [q ** (k - g) * coeffs[2 * g - k] for k in range(g + 1, 2 * g + 1)]
    return np.roots(full)


# ------------------------------------------------------------------ the tensors
def closed_form(q, pis):
    g = len(pis)
    t = (q + 1) / 2; w = (q + 1) / (2 * g); h = (q - 1) / (2 * np.sqrt(g))
    D = np.diag(pis); B0 = D / np.sqrt(t); b0 = B0.reshape(-1, 1)
    nu = (b0.conj().T @ b0)[0, 0].real
    assert w >= nu - 1e-12
    S = np.sqrt(w) * np.eye(g * g) + ((np.sqrt(w - nu) - np.sqrt(w)) / nu) * (b0 @ b0.conj().T)
    Bs = [B0] + [(S @ np.eye(g * g)[:, l]).reshape(g, g) for l in range(g * g)]
    As = []
    A = np.zeros((g + 1, g + 1), complex); A[0, 0] = np.sqrt(t); A[1:, 1:] = B0; As.append(A)
    for l in range(1, g * g + 1):
        A = np.zeros((g + 1, g + 1), complex); A[1:, 1:] = Bs[l]; As.append(A)
    for j in range(g):
        A = np.zeros((g + 1, g + 1), complex); A[0, 1 + j] = np.sqrt(h); As.append(A)
        A = np.zeros((g + 1, g + 1), complex); A[1 + j, 0] = np.sqrt(h); As.append(A)
    return As


def certified_f5():
    base = "0.26071183 -0.77630597 0.1256142 0.57129743 0.23357458 -0.48921698 -1.34760956 -0.05591677 -0.94940643 -0.38739751 -0.67840262 -1.61862569 0.09572017 -0.36950433 -0.80102781 0.32500101 -1.0690133 -0.50378403 0.0903946 -0.85610066 -0.89848953 -0.00971177 -0.9517933 -0.63028434 0.30058661 1.43919288 0.38038457 -1.21909557".split()
    sel = [18, 15, 11, 19, 14, 2, 22, 4, 3]
    active = ['0.09039460223261970869', '0.32500101571215119755', '-1.61862568848573412561', '-0.85610067188373463151', '-0.80102781481057057827', '0.12561420129934324780', '-0.95179330452156658836', '0.23357456652702491517', '0.57129743723871521168']
    x = list(map(float, base))
    for l, v in zip(sel, active):
        x[l] = float(v)
    pos = [(s, i, j) for s in range(3) for i in range(3) for j in range(3) if (s < 2) == ((i == 0) == (j == 0))]
    As = [np.zeros((3, 3), complex) for _ in range(3)]
    for l, (s, i, j) in enumerate(pos):
        As[s][i, j] = x[2 * l] + 1j * x[2 * l + 1]
    return As


# ------------------------------------------------------------------ MPS machinery (Kronecker / spin contraction)
def transfer(As):
    return sum(np.kron(A, A.conj()) for A in As)


def ring_vector(As, B, n):
    """sum_w Tr(B A_w) |w>, sites left to right, no statistics signs."""
    D = As[0].shape[0]
    M = B.reshape(1, D, D)
    for _ in range(n):
        M = np.einsum('cij,sjk->csik', M, np.array(As)).reshape(-1, D, D)
    return np.einsum('cii->c', M)


def word_matrices(As, k):
    D = As[0].shape[0]
    M = np.eye(D, dtype=complex).reshape(1, D, D)
    for _ in range(k):
        M = np.einsum('cij,sjk->csik', M, np.array(As)).reshape(-1, D, D)
    return M                                              # shape (d^k, D, D)


def block_spectrum_gram(As, P, n, l):
    """Nonzero spectrum of the reduced state of sites 1..l in the P-closed ring of length n."""
    D = As[0].shape[0]
    E = transfer(As)
    GX = np.linalg.matrix_power(E, l)                      # GX[(a a'),(b b')] = <X_{a'b'}|X_{ab}>
    GY = np.linalg.matrix_power(E, n - l) @ np.kron(P, P.conj())   # GY[(b b'),(a a')] = <Y_{b'a'}|Y_{ba}>
    # K[(ab),(a'b')] = GY[(ba),(b'a')]; rho on coefficient vectors = K @ G_X^T with G_X[(ab),(a'b')] = GX[(a a'),(b b')]
    GXm = GX.reshape(D, D, D, D).transpose(0, 2, 1, 3).reshape(D * D, D * D)      # [(a b),(a' b')]
    GYm = GY.reshape(D, D, D, D).transpose(0, 2, 1, 3).reshape(D * D, D * D)      # [(b a),(b' a')]
    K = GYm.reshape(D, D, D, D).transpose(1, 0, 3, 2).reshape(D * D, D * D)       # [(a b),(a' b')]
    ev = np.linalg.eigvals(K @ GXm.T)
    ev = np.sort(ev.real)[::-1]
    ev = ev[ev > 1e-12 * ev.max()]
    return ev / ev.sum()


def block_spectrum_exact(psi, d, n, l):
    M = psi.reshape(d ** l, d ** (n - l))
    s = np.linalg.svd(M, compute_uv=False) ** 2
    s = s[s > 1e-12 * s.max()]
    return s / s.sum()


def entropy(p):
    p = p[p > 1e-15]
    return float(-(p * np.log(p)).sum())


def injectivity_ranks(As, kmax):
    D = As[0].shape[0]
    out = []
    for k in range(1, kmax + 1):
        W = word_matrices(As, k).reshape(-1, D * D)
        out.append(np.linalg.matrix_rank(W, tol=1e-9))
    return out


def parent_hamiltonian_data(As, P, k, n, twist=False, eta=None):
    """Local term = projector onto the complement of the k-site support S_k; ring of n sites.
    twist=True conjugates every term that wraps the boundary by the site parities eta_s of the sites
    lying after the wrap (the Jordan--Wigner image of the periodic fermion ring)."""
    d = len(As); D = As[0].shape[0]
    W = word_matrices(As, k)                                   # (d^k, D, D): X_{ab} = W[:, a, b]
    X = W.reshape(d ** k, D * D)                               # columns span S_k
    U, s, _ = np.linalg.svd(X, full_matrices=False)
    r = int((s > 1e-9 * s.max()).sum())
    Pi = U[:, :r] @ U[:, :r].conj().T                          # projector onto S_k
    h = np.eye(d ** k) - Pi
    dim = d ** n
    H = np.zeros((dim, dim), complex)
    idx = np.arange(dim).reshape([d] * n)
    for i in range(n):                                         # place h on sites i..i+k-1 (mod n)
        sites = [(i + j) % n for j in range(k)]
        rest = [j for j in range(n) if j not in sites]
        perm = sites + rest
        t = idx.transpose(perm).reshape(d ** k, d ** (n - k))
        hh = h
        if twist and i + k > n:                                # wrapped term: conjugate by Z on the wrapped sites
            Z = np.ones(1)
            for j in range(k):
                Z = np.kron(Z, eta if (i + j) >= n else np.ones(d))
            hh = np.diag(Z) @ h @ np.diag(Z)
        for c in range(d ** (n - k)):
            rows = t[:, c]
            H[np.ix_(rows, rows)] += hh
    return H, r


def ground_space(H, tol=1e-7):
    w, v = np.linalg.eigh((H + H.conj().T) / 2)
    zero = w < tol
    return int(zero.sum()), v[:, zero], (w[~zero].min() if (~zero).any() else np.nan)


def in_span(vecs, psi):
    if vecs.shape[1] == 0:
        return False
    c = vecs.conj().T @ psi
    return np.linalg.norm(vecs @ c - psi) < 1e-7 * np.linalg.norm(psi)


def study(name, As, P, q, alphas, nmax_exact, ring_ns, kpar, npar, fermionic_letters=None):
    banner(name)
    d = len(As); D = As[0].shape[0]
    E = transfer(As)
    G = np.kron(np.diag(P), np.diag(P)).real
    ev_i, od_i = np.where(G == 1)[0], np.where(G == -1)[0]
    le = np.linalg.eigvals(E[np.ix_(ev_i, ev_i)]); lo = np.linalg.eigvals(E[np.ix_(od_i, od_i)]) if len(od_i) else np.array([])
    print(f'  letters d = {d}, bond D = {D}; even spectrum {np.round(np.sort_complex(le), 4)}')
    if len(lo):
        print(f'  odd spectrum {np.round(np.sort_complex(lo), 4)}')
    lam = np.abs(le).max()
    ev_sub = sorted([abs(x) for x in le if abs(x) < lam - 1e-9], reverse=True)
    if ev_sub:
        print(f'  even correlation length 1/log(lambda_1/lambda_2) = {1 / np.log(lam / ev_sub[0]):.5f}  (1/log q = {1 / np.log(q):.5f})')
    if len(lo):
        xis = [1 / np.log(lam / abs(x)) for x in lo if abs(x) > 1e-9]
        print(f'  odd correlation lengths {np.round(xis, 5)};  2/log q = {2 / np.log(q):.5f}')
        check(np.allclose(xis, 2 / np.log(q), atol=1e-6), f'  {name}: every odd mode has correlation length 2/log q (RH for this curve)')
    # counts
    for n in range(1, 5):
        st = np.trace(G[:, None] * np.linalg.matrix_power(E, n)).real
        Nn = 1 + q ** n - np.sum(alphas ** n).real if len(alphas) else 1 + q ** n
        check(abs(st - Nn) < 1e-8 * max(1, Nn), f'  {name}: str E^{n} = N_{n} = {Nn:.0f}')
    # injectivity
    ranks = injectivity_ranks(As, 4)
    print(f'  rank of span{{A_w : |w| = k}} for k = 1..4: {ranks}  (D^2 = {D * D})')
    # entanglement: Gram formula vs exact vector
    for n in range(2, nmax_exact + 1):
        psi = ring_vector(As, P, n)
        for l in (1, n // 2):
            if l < 1 or l >= n:
                continue
            pg = block_spectrum_gram(As, P, n, l); pe = block_spectrum_exact(psi, d, n, l)
            m = max(len(pg), len(pe)); pg2 = np.pad(pg, (0, m - len(pg))); pe2 = np.pad(pe, (0, m - len(pe)))
            check(np.allclose(np.sort(pg2), np.sort(pe2), atol=1e-8), f'  {name}: block spectrum (n={n}, l={l}) Gram formula = explicit vector; S = {entropy(pe):.5f}')
    print('  half-ring entanglement entropy S(n/2 | n) of the P-closed ring for larger n (Gram formula):')
    for n in ring_ns:
        pg = block_spectrum_gram(As, P, n, n // 2)
        print(f'    n={n:3d}: S = {entropy(pg):.5f}, Schmidt rank {len(pg)}, Schmidt weights {np.round(pg, 5)}')
    print(f'  bound 2 log D = {2 * np.log(D):.5f}')
    # parent Hamiltonian
    if kpar:
        eta = np.array([1.0 if np.allclose(P @ A @ P, A) else -1.0 for A in As])
        psi1 = ring_vector(As, np.eye(D, dtype=complex), npar); psiP = ring_vector(As, P, npar)
        for twist in ([False, True] if (eta < 0).any() else [False]):
            H, r = parent_hamiltonian_data(As, P, kpar, npar, twist=twist, eta=eta)
            g0, V, gap = ground_space(H)
            print(f'  parent Hamiltonian ({"parity-twisted boundary term" if twist else "untwisted"}): k = {kpar}-site terms, '
                  f'support dimension {r} of {d ** kpar}; ring n = {npar}: ground-space dimension {g0}, gap {gap:.5f}')
            print(f'    antiperiodic ring Psi_1 in kernel: {in_span(V, psi1)};  periodic (P-closed) ring Psi_P in kernel: {in_span(V, psiP)}')
            if (eta < 0).any():
                check(in_span(V, psiP) == twist and in_span(V, psi1) == (not twist), f'  {name}: Psi_P is a ground state exactly of the twisted parent Hamiltonian, Psi_1 of the untwisted one')
            else:
                check(in_span(V, psiP) and in_span(V, psi1), f'  {name}: both closures are ground states of the parent Hamiltonian')
    return None, None


# ================================================================== genus 0
q = 5
As0 = [np.diag([1.0, 0.0]).astype(complex)] + [np.diag([0.0, 1.0]).astype(complex)] * q
P0 = np.eye(2)
study('GENUS 0: P^1 over F_5 (bond C^2, ungraded, GHZ-type cat of two product states)', As0, P0, 5, np.array([]), 5, [6, 10, 20], 2, 5)
print('  block entropy is the binary entropy H(1/(1+5^n)) of the two orthogonal branches:')
for n in (2, 4, 8):
    p = 1 / (1 + 5.0 ** n); pg = block_spectrum_gram(As0, P0, n, n // 2)
    check(abs(entropy(pg) - entropy(np.array([p, 1 - p]))) < 1e-9, f'  genus 0: S(n={n}) = H(1/(1+q^n)) = {entropy(pg):.6f}')

# ================================================================== genus 1
N1 = count_hyper(5, 1, [1, 1, 0, 1]); a = 5 + 1 - N1
pi = (a + np.sqrt(complex(a * a - 20))) / 2
phi = np.array([1, 1]) / np.sqrt(2)
As1 = [phi[s] * np.diag([1.0, pi]) for s in range(2)]
P1 = np.diag([1.0, -1.0])
study(f'GENUS 1: y^2 = x^3 + x + 1 over F_5 (bond C^(1|1), pi = {pi:.4f}, letters phi_s diag(1, pi))', As1, P1, 5, np.array([pi, np.conj(pi)]), 6, [6, 10, 20], 1, 6)
psiP = ring_vector(As1, P1, 6)
check(np.linalg.matrix_rank(psiP.reshape(8, 8), tol=1e-9) == 1, '  genus 1: Psi_P is a product state (Schmidt rank one), entropy 0')

# ================================================================== genus 2 over F_5 (certified)
r5 = np.roots([1, -3, 7, -15, 25])
As2 = certified_f5(); P2 = np.diag([1.0, -1.0, -1.0])
study('GENUS 2: y^2 = x^5 + x^3 + x^2 - 2 over F_5, certified 2 even + 1 odd letters (bond C^(1|2))', As2, P2, 5, r5, 7, [8, 12, 20, 40], 3, 6)
# fermionic check: Jordan-Wigner Fock vector block entropies (contiguous block starting at site 1)
import cmps_parity_supertrace as cps
print('  explicit Jordan-Wigner Fock vector (fermionic letter as a real fermion) versus the spin contraction:')
Q = As2[0] - np.eye(3); Rs = [As2[1], As2[2], np.zeros((3, 3), complex)]
for n in (3, 4, 5):
    cre = cps.creation_ops(n)
    psiF = cps.mps_state(n, 1.0, Q, Rs, P2.astype(complex), cre)
    for l in (1, n // 2):
        M = psiF.reshape(4 ** l, 4 ** (n - l)); s = np.linalg.svd(M, compute_uv=False) ** 2; s = s[s > 1e-12 * s.max()]; s /= s.sum()
        pg = block_spectrum_gram(As2, P2, n, l)
        m = max(len(s), len(pg))
        check(np.allclose(np.sort(np.pad(s, (0, m - len(s)))), np.sort(np.pad(pg, (0, m - len(pg)))), atol=1e-7), f'  genus 2 F_5: fermionic block spectrum (n={n}, l={l}) = spin/Gram spectrum, S = {entropy(s):.5f}')

# ================================================================== genus 2 over F_25 (closed form)
reps = []
for al in r5:
    if not any(abs(np.conj(al) - b) < 1e-8 for b in reps):
        reps.append(al)
pis25 = [reps[0] ** 2, reps[1] ** 2]
As25 = closed_form(25, pis25)
study('GENUS 2: same curve over F_25, closed-form 5 even + 4 odd letters (bond C^(1|2))', As25, P2, 25, np.array(pis25 + [np.conj(x) for x in pis25]), 4, [6, 10, 20, 40], 2, 4)

# ================================================================== genus 3 over F_37 (closed form)
q3 = 37; f7 = [1, 1, 0, 0, 0, 0, 0, 1]
counts3 = [count_hyper(q3, n, f7) for n in (1, 2, 3)]
al3 = lpoly_roots(q3, counts3, 3)
reps3 = []
for al in al3:
    if not any(abs(np.conj(al) - b) < 1e-6 for b in reps3):
        reps3.append(al)
As37 = closed_form(q3, reps3); P3 = np.diag([1.0, -1.0, -1.0, -1.0])
print(f'\n  genus 3 counts N_1..N_3 = {counts3}')
study('GENUS 3: y^2 = x^7 + x + 1 over F_37, closed-form 10 even + 6 odd letters (bond C^(1|3))', As37, P3, 37, al3, 3, [6, 10, 20], None, None)

print(f'\n{NCHK} checks, {len(FAILS)} failures')
for m in FAILS:
    print('  FAIL', m)
sys.exit(1 if FAILS else 0)
