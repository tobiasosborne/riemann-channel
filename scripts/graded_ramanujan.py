"""Graded Ramanujan property: the definition tested on three graded transfer channels.

Conventions (shards 02f/02g/03b): bond C^{D_+|D_-} with parity P = diag(+1,-1), homogeneous
letters A_s (P A_s P = +-A_s), doubled transfer E = sum_s A_s (x) conj(A_s) on C^D (x) C^D,
doubled-bond parity Gamma = P (x) P; even sector = block-diagonal operators, odd sector =
block-off-diagonal (parity coherences).  Ring norms: NS (antiperiodic) N_1(n) = Tr E^n,
R (periodic) N_P(n) = str E^n = Tr(Gamma E^n) = ||Psi_P||^2 >= 0.  Graded ring zeta
Z_P(u) = exp(sum_n N_P(n) u^n/n) = det(1 - u E_odd)/det(1 - u E_even): poles at net-even,
zeros at net-odd eigenvalues.  Non-backtracking (Hashimoto) lift for unitary adjoint-closed
letters with reversal i -> ibar: T on C^D (x) C^D (x) C^{Dk}, T(v (x) e_i) = sum_{j != ibar}
E_i v (x) e_j, commuting with Gamma (x) 1; graded quantum Ihara zeta 1/sdet(1 - u T).

(1) Pauli family on C^{1|1}: six letters {X,X,Y,Y,Z,Z}, P = Z: the graded quantum Ihara zeta is
    the zeta function of an elliptic curve over F_5 with 8 points.
(2) the 06h projective elliptic tensor: parity-twisted trace preservation sum_s eps_s A_s A_s^+ = r 1
    (the P-mode is the H^0 pole), odd block sqrt q times a unitary.
(3) graded Harrow expanders: PGL2(F_p) principal series I(chi, chi^-1) with chi of order 4
    (splits on PSL2 into two conjugate halves H_+, H_-; P = +-1 on them), LPS generators of
    norm q with (q/p) = -1 (they lie in PGL2 \\ PSL2, all letters odd, Cayley graph bipartite).
    Both Gamma-sectors of the channel lie in the Hastings band; the P-mode is -1; the odd
    edge eigenvalues lie on |mu| = sqrt q: a quantum expander whose parity-closed ring zeta has
    zeros on the critical circle.
(4) continuum: the jump Lindbladian of (1); spectrum is the affine image of the channel's.
Usage: python3 scripts/graded_ramanujan.py
"""
import itertools, sys
import numpy as np
import scipy.sparse as sp, scipy.sparse.linalg as spl

sys.path.insert(0, 'scripts')
from weil_lps import lps_quaternions, conj as qconj, split_matrices, quat_to_gl2

np.set_printoptions(precision=6, suppress=True, linewidth=150)
NCHK = [0, 0]
def check(cond, msg):
    NCHK[0] += 1; NCHK[1] += bool(cond)
    print(("  ok   " if cond else "  FAIL ") + msg)

def doubled(letters): return sum(np.kron(A, A.conj()) for A in letters)
def sectors(P):
    G = np.kron(P, P.conj()); D2 = G.shape[0]
    ev = np.diag(G).real
    return G, np.where(ev > 0)[0], np.where(ev < 0)[0]
def sector_eigs(E, idx): return np.linalg.eigvals(E[np.ix_(idx, idx)])
def ring_norms(E, G, nmax):
    N1, NP = [], []; M = np.eye(E.shape[0], dtype=complex)
    for n in range(1, nmax + 1):
        M = M @ E; N1.append(np.trace(M).real); NP.append(np.trace(G @ M).real)
    return np.array(N1), np.array(NP)
def word_ring_norm(letters, B, n):
    tot = 0.0
    for w in itertools.product(range(len(letters)), repeat=n):
        M = B.copy()
        for s in w: M = M @ letters[s]
        tot += abs(np.trace(M))**2
    return tot
def hashimoto(letters, rev):
    """T on (bond (x) bond) (x) C^Dk for Ad-type letters; rev[i] = index of the adjoint letter."""
    Dk = len(letters); Es = [np.kron(A, A.conj()) for A in letters]; d2 = Es[0].shape[0]
    T = np.zeros((d2 * Dk, d2 * Dk), complex)
    for i in range(Dk):
        for j in range(Dk):
            if j != rev[i]:
                T[j * d2:(j + 1) * d2, i * d2:(i + 1) * d2] += Es[i]
    return T
def zeta_coeffs(N, nmax):
    """exp(sum N_n u^n/n) as a power series to order nmax"""
    c = np.zeros(nmax + 1); c[0] = 1
    for m in range(1, nmax + 1):
        c[m] = sum(N[k - 1] * c[m - k] for k in range(1, m + 1)) / m
    return c
def poly_from_roots_det(M, nmax):
    """coefficients of det(1 - u M) up to u^nmax via Newton's identities"""
    p = [np.trace(np.linalg.matrix_power(M, k)) for k in range(1, nmax + 1)]
    e = np.zeros(nmax + 1, complex); e[0] = 1
    for m in range(1, nmax + 1):
        e[m] = -sum(p[k - 1] * e[m - k] for k in range(1, m + 1)) / m   # det(1-uM) = sum e_m u^m
    return e.real

# ================================================================ (1) Pauli family on C^{1|1}
print("(1) Pauli letters on the qubit bond C^{1|1}, P = Z; six letters X,X,Y,Y,Z,Z with reversal pairing the copies")
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]).astype(complex); I2 = np.eye(2, dtype=complex)
P = Z
letters = [X, X, Y, Y, Z, Z]; rev = [1, 0, 3, 2, 5, 4]; Dk = 6; q = Dk - 1
for A in letters: check(np.allclose(P @ A @ P, A) or np.allclose(P @ A @ P, -A), "letter homogeneous: " + ("even" if np.allclose(P @ A @ P, A) else "odd"))
E = doubled(letters); G, ev_i, od_i = sectors(P)
check(np.allclose(E @ G, G @ E), "doubled transfer commutes with Gamma = P (x) P")
ee, eo = np.sort(sector_eigs(E, ev_i).real), np.sort(sector_eigs(E, od_i).real)
print("   even (vertex) spectrum:", ee, " odd (vertex) spectrum:", eo, "  Hastings band |lambda| <= 2 sqrt(q) =", 2 * np.sqrt(q))
check(np.allclose(ee, [-2, 6]) and np.allclose(eo, [-2, -2]), "even {6 (fixed point), -2 (P-mode = #even - #odd letters)}, odd {-2, -2}: all nontrivial in the band")
T = hashimoto(letters, rev); GT = np.kron(np.eye(Dk), G)
check(np.allclose(T @ GT, GT @ T), "Hashimoto operator commutes with Gamma (x) 1")
te = np.linalg.eigvals(T[np.ix_(np.where(np.diag(GT) > 0)[0], np.where(np.diag(GT) > 0)[0])])
to = np.linalg.eigvals(T[np.ix_(np.where(np.diag(GT) < 0)[0], np.where(np.diag(GT) < 0)[0])])
mod = lambda v: sorted(set(np.round(np.abs(v), 6)))
print("   even edge moduli:", mod(te), " odd edge moduli:", mod(to), " critical sqrt q =", round(np.sqrt(q), 6))
check(set(mod(to)) == {1.0, round(np.sqrt(q), 6)} and set(mod(te)) == {1.0, round(np.sqrt(q), 6), 5.0}, "odd edge eigenvalues on the critical circle (plus the trivial +-1); even: trivial {5,1} and the circle")
# sector-by-sector Ihara-Bass at a random u
u0 = 0.3 + 0.1j
for name, idxV, idxT, nk in (("even", ev_i, np.where(np.diag(GT) > 0)[0], len(ev_i)), ("odd", od_i, np.where(np.diag(GT) < 0)[0], len(od_i))):
    lhs = np.linalg.det(np.eye(len(idxT)) - u0 * T[np.ix_(idxT, idxT)])
    Ek = E[np.ix_(idxV, idxV)]
    rhs = (1 - u0**2)**(nk * (Dk - 2) / 2) * np.linalg.det(np.eye(nk) - u0 * Ek + q * u0**2 * np.eye(nk))
    check(abs(lhs - rhs) < 1e-9 * abs(lhs), f"graded quantum Ihara-Bass on the {name} sector: det(1-uT_k) = (1-u^2)^(n_k(D-2)/2) det(1 - u Sigma_k + q u^2)")
N1, NP = ring_norms(T, GT, 6)
check(np.all(NP >= -1e-9) and np.allclose(NP, [1 + 5**n - 2 * ((-1 + 2j)**n).real for n in range(1, 7)]), f"str T^n = {[int(round(x)) for x in NP]} = 1 + 5^n - (mu^n + conj mu^n), mu = -1 + 2i: the point counts of an elliptic curve over F_5 with 8 points")
# Z_R(u) = det(1-uT_odd)/det(1-uT_even) = (1 + 2u + 5u^2)/((1-u)(1-5u)) as a power series
cz = zeta_coeffs(NP, 6)
inv_den = np.array([sum(5**k for k in range(m + 1)) for m in range(7)], float)      # 1/((1-u)(1-5u)) = sum_m (5^{m+1}-1)/4 u^m
ser = np.convolve([1, 2, 5], inv_den)[:7]
check(np.allclose(cz, ser), "graded quantum Ihara zeta = (1 + 2u + 5u^2)/((1-u)(1-5u)): curve normal form, genus 1, balanced grading cancels the (1-u^2) factors")
curves = [(a, b) for a in range(5) for b in range(5) if (4 * a**3 + 27 * b**2) % 5 and 1 + sum(1 for x in range(5) for y in range(5) if (y * y - x**3 - a * x - b) % 5 == 0) == 8]
check(len(curves) > 0, f"elliptic curves y^2 = x^3 + ax + b over F_5 with 8 points, (a,b) in {curves[:4]}...: the Pauli non-backtracking ring counts their points")
# word check of positivity: str T^n = sum over cyclically non-backtracking closed words of |Tr(P U_w)|^2
def nb_words(n, Dk, rev):
    for w in itertools.product(range(Dk), repeat=n):
        if all(w[(k + 1) % n] != rev[w[k]] for k in range(n)): yield w
for n in (1, 2, 3):
    tot = 0.0
    for w in nb_words(n, Dk, rev):
        M = P.copy()
        for s in w: M = M @ letters[s]
        tot += abs(np.trace(M))**2
    check(abs(tot - NP[n - 1]) < 1e-9, f"n = {n}: str T^n = sum_(cyclically non-backtracking words) |Tr(P U_w)|^2 = {tot:.0f} (a ring norm)")

# ================================================================ (2) the 06h elliptic tensor
print("(2) the shard-06h four-letter projective elliptic tensor on C^{1|1} (q = 5, r = 1, pi = (-3 + i sqrt 11)/2)")
q5 = 5; r = 1; t = (q5 + r) / 2; h = (q5 - r) / 2; pi = (-3 + 1j * np.sqrt(11)) / 2
A0 = np.diag([np.sqrt(t), pi / np.sqrt(t)]); A1 = np.diag([0, np.sqrt(t - q5 / t)])
A2 = np.sqrt(h) * np.array([[0, 1], [0, 0]], complex); A3 = np.sqrt(h) * np.array([[0, 0], [1, 0]], complex)
L6 = [A0, A1, A2, A3]; eps = [1, 1, -1, -1]
check(np.allclose(sum(A.conj().T @ A for A in L6), q5 * I2), "sum_s A_s^+ A_s = q 1 (trace preservation up to q: the fixed point / pole at s = 1)")
check(np.allclose(sum(e * A @ A.conj().T for e, A in zip(eps, L6)), r * I2), "sum_s eps_s A_s A_s^+ = r 1: parity-twisted preservation, E(P) = r P, the P-mode is the H^0 pole at 1")
E6 = doubled(L6)
check(np.allclose(E6 @ np.kron(P, P) @ np.array([1, 0, 0, 1]), r * np.kron(P, P) @ np.array([1, 0, 0, 1])) or np.allclose(E6 @ np.array([1, 0, 0, -1]), r * np.array([1, 0, 0, -1])), "P (as a vector of the doubled bond) is an even eigenvector with eigenvalue r")
G6, ev6, od6 = sectors(P)
print("   even:", np.sort(sector_eigs(E6, ev6).real), " odd:", sector_eigs(E6, od6))
Eo = E6[np.ix_(od6, od6)]
check(np.allclose(Eo.conj().T @ Eo, q5 * np.eye(2)), "odd block: E_1^+ E_1 = q, i.e. E_1 = sqrt q times a unitary (Hilbert-Polya form on the odd sector)")
check(np.allclose(np.abs(sector_eigs(E6, od6)), np.sqrt(q5)) and set(np.round(sector_eigs(E6, ev6).real, 9)) == {1.0, 5.0}, "divisor: even = trivial {q, r} exactly, odd on |mu| = sqrt q: RH with an empty nontrivial even sector")
# graded Weil (Hodge) inequality |Tr E_1^n| <= Tr E_0^n
N1_6, NP_6 = ring_norms(E6, G6, 8)
check(np.all(np.abs(N1_6 - NP_6) / 2 <= (N1_6 + NP_6) / 2 + 1e-9), "|Tr E_odd^n| <= Tr E_even^n for n <= 8 (both closures are ring norms)")

# ================================================================ (3) graded Harrow expanders from PGL2(F_p)
def gl2_elements(p):
    return [(a, b, c, d) for a, b, c, d in itertools.product(range(p), repeat=4) if (a * d - b * c) % p]
def mul(g, h, p):
    a, b, c, d = g; e, f, gg, hh = h
    return ((a * e + b * gg) % p, (a * f + b * hh) % p, (c * e + d * gg) % p, (c * f + d * hh) % p)
def inv(g, p):
    a, b, c, d = g; di = pow((a * d - b * c) % p, p - 2, p)
    return ((d * di) % p, (-b * di) % p, (-c * di) % p, (a * di) % p)
def det(g, p): return (g[0] * g[3] - g[1] * g[2]) % p
def pgl_canon(g, p):
    """representative of the scalar class: first nonzero entry = 1"""
    for v in g:
        if v: vi = pow(v, p - 2, p); return tuple((x * vi) % p for x in g)
def legendre(a, p): return 1 if pow(a % p, (p - 1) // 2, p) == 1 else -1

def principal_series(p, chi):
    """I(chi, chi^-1) of GL2(F_p): basis = cosets B\\G <-> P^1(F_p); pi(g)_{ij} = chi_B(r_i g r_j^-1) if in B."""
    reps = [(0, 1, 1, 0)] + [(1, 0, x, 1) for x in range(p)]            # bottom rows (1,0) and (x,1)
    def coset_of(g):                                                   # bottom row (c,d) up to scalar
        c, d = g[2], g[3]
        if d == 0: return 0
        di = pow(d, p - 2, p); return 1 + (c * di) % p
    def chiB(b): a, _, c, d = b; assert c == 0; return chi[a] * np.conj(chi[d])
    def rep(g):
        M = np.zeros((p + 1, p + 1), complex)
        for i, ri in enumerate(reps):
            x = mul(ri, g, p); j = coset_of(x); b = mul(x, inv(reps[j], p), p)
            M[i, j] = chiB(b)
        return M
    return rep

def graded_harrow(p, q, nmax=4, ihara=True):
    print(f"(3) PGL2(F_{p}) with the {q + 1} LPS generators of norm {q}; (q/p) = {legendre(q, p)}")
    assert legendre(q, p) == -1 and p % 4 == 1 and q % 4 == 1
    gen = next(g for g in range(2, p) if len({pow(g, k, p) for k in range(1, p)}) == p - 1)
    chi = np.zeros(p, complex); chi[0] = 0
    for k in range(p - 1): chi[pow(gen, k, p)] = np.exp(2j * np.pi * k / 4)      # order-4 character of F_p^*
    check(abs(chi[gen]**4 - 1) < 1e-12 and abs(chi[gen]**2 + 1) < 1e-12, "chi has order 4, chi^2 = the quadratic character")
    rep = principal_series(p, chi); G = gl2_elements(p); D = p + 1
    # representation checks on random pairs, centre trivial
    rng = np.random.default_rng(1)
    ok = all(np.allclose(rep(G[i]) @ rep(G[j]), rep(mul(G[i], G[j], p))) for i, j in rng.integers(0, len(G), (30, 2)))
    okc = all(np.allclose(rep((z, 0, 0, z)), np.eye(D)) for z in range(1, p))
    check(ok and okc, f"pi is a unitary representation of GL2(F_{p}), trivial on the centre: a representation of PGL2(F_{p}) of dimension {D}")
    chars = {g: np.trace(rep(g)) for g in G}
    check(abs(sum(abs(v)**2 for v in chars.values()) / len(G) - 1) < 1e-9, "irreducible: <chi_pi, chi_pi> = 1")
    G0 = [g for g in G if legendre(det(g, p), p) == 1]
    check(abs(sum(abs(chars[g])**2 for g in G0) / len(G0) - 2) < 1e-9, "restricted to G_0 = {det a square} = PSL2 x centre it splits into two irreducibles (Clifford theory, index 2)")
    # commutant of pi(G_0) by exact group averaging of a random Hermitian matrix: C = a 1 + b P
    H0 = rng.normal(size=(D, D)) + 1j * rng.normal(size=(D, D)); H0 = H0 + H0.conj().T
    reps0 = {g: rep(g) for g in G0}
    C = sum(M @ H0 @ M.conj().T for M in reps0.values()) / len(G0)
    C = C - np.trace(C) / D * np.eye(D); C = (C + C.conj().T) / 2
    w, V = np.linalg.eigh(C)
    check(np.allclose(np.abs(w), np.abs(w[0])) and np.sum(w > 0) == D // 2, "the averaged operator has two eigenvalues of opposite sign and equal multiplicity: commutant = span(1, P)")
    # rotate everything into the P-eigenbasis so that Gamma = P (x) P is diagonal on the doubled bond
    order = np.argsort(-w); V = V[:, order]
    rep0 = rep
    rep_rot = lambda g: V.conj().T @ rep0(g) @ V
    Pm = np.diag([1.0] * (D // 2) + [-1.0] * (D // 2)).astype(complex)
    check(np.allclose(V.conj().T @ C @ V, np.diag(w[order])), "P diagonal in the rotated basis")
    rep = rep_rot
    gOdd = next(g for g in G if legendre(det(g, p), p) == -1)
    check(all(np.allclose(Pm @ rep(g) @ Pm, legendre(det(g, p), p) * rep(g)) for g in [G0[3], G0[11], gOdd, mul(gOdd, G0[5], p)]), "P pi(g) P = (det g / p) pi(g): elements of the nontrivial coset are odd, of PSL2 even")
    # LPS generators
    I_, J_ = split_matrices(p); Q = lps_quaternions(q); assert len(Q) == q + 1
    S = [tuple(int(v) for v in quat_to_gl2(a, p, I_, J_).flatten()) for a in Q]
    Sinv = [tuple(int(v) for v in quat_to_gl2(qconj(a), p, I_, J_).flatten()) for a in Q]
    rev = [S.index(next(s for s in S if pgl_canon(s, p) == pgl_canon(Sinv[i], p))) for i in range(len(S))]
    check(all(legendre(det(s, p), p) == -1 for s in S), f"all {q + 1} generators have non-square determinant {q} mod {p}: every letter is odd")
    check(len({pgl_canon(s, p) for s in S}) == q + 1 and all(rev[rev[i]] == i and rev[i] != i for i in range(len(S))), "distinct in PGL2, closed under inverse, fixed-point-free reversal")
    # Cayley graph of PGL2(F_p)
    els = sorted({pgl_canon(g, p) for g in G}); idx = {e: i for i, e in enumerate(els)}; n = len(els)
    rows, cols = [], []
    for i, e in enumerate(els):
        for s in S: rows.append(i); cols.append(idx[pgl_canon(mul(e, s, p), p)])
    Ad = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
    lam = np.linalg.eigvalsh(Ad.toarray()) if n <= 3000 else None
    if lam is not None:
        nontriv = lam[np.abs(np.abs(lam) - (q + 1)) > 1e-6]
        check(abs(lam[-1] - (q + 1)) < 1e-9 and abs(lam[0] + (q + 1)) < 1e-9, f"Cayley graph on {n} vertices, {q + 1}-regular, bipartite (eigenvalue -(q+1))")
        check(np.max(np.abs(nontriv)) <= 2 * np.sqrt(q) + 1e-9, f"Ramanujan: max nontrivial |lambda| = {np.max(np.abs(nontriv)):.4f} <= 2 sqrt q = {2 * np.sqrt(q):.4f}")
    # the graded channel
    Ws = [rep(s) for s in S]; Sig = doubled(Ws)                       # Sigma = (q+1) Phi, unnormalised
    Gm, evi, odi = sectors(Pm)
    check(np.allclose(Sig @ Gm, Gm @ Sig), "channel commutes with Gamma = Ad(P)")
    se = np.sort(sector_eigs(Sig, evi).real); so = np.sort(sector_eigs(Sig, odi).real)
    band = 2 * np.sqrt(q)
    se_nt = se[np.abs(np.abs(se) - (q + 1)) > 1e-6]
    print(f"   even sector ({len(evi)}): extremes {se[:2]} ... {se[-2:]};  odd sector ({len(odi)}): [{so[0]:.4f}, {so[-1]:.4f}];  band {band:.4f}")
    check(np.sum(np.abs(se - (q + 1)) < 1e-6) == 1 and np.sum(np.abs(se + (q + 1)) < 1e-6) == 1, "even sector: the fixed point q+1 (simple) and the P-mode -(q+1) = eps(W_S) (all letters odd)")
    check(np.max(np.abs(se_nt)) <= band + 1e-9, f"even nontrivial eigenvalues in the Hastings band (max {np.max(np.abs(se_nt)):.4f})")
    check(np.max(np.abs(so)) <= band + 1e-9, f"odd sector (parity coherences) entirely in the Hastings band (max {np.max(np.abs(so)):.4f}): a graded Ramanujan quantum expander")
    if lam is not None:
        allc = np.sort(np.concatenate([se, so]))
        check(all(np.min(np.abs(lam - v)) < 1e-6 for v in allc), "Harrow containment: every channel eigenvalue (both sectors) is a Cayley-graph eigenvalue")
    # ring norms and words
    N1, NP = ring_norms(Sig, Gm, nmax)
    check(np.all(NP >= -1e-9) and np.all(np.abs(N1[1::2] - NP[1::2]) / 2 <= (N1[1::2] + NP[1::2]) / 2 + 1e-9), f"str Sigma^n = {[round(x, 6) for x in NP]} >= 0 and |Tr odd| <= Tr even")
    check(np.allclose(NP[:3], [word_ring_norm(Ws, Pm, k) for k in (1, 2, 3)]) and np.allclose(N1[:3], [word_ring_norm(Ws, np.eye(D), k) for k in (1, 2, 3)]), "str = sum_w |Tr(P pi(w))|^2 and Tr = sum_w |Tr pi(w)|^2 on words of length <= 3")
    check(abs(NP[0]) < 1e-9 and abs(N1[0]) < 1e-9, "odd length: both ring norms vanish (chi_pi is supported on G_0; bipartite)")
    if ihara:
        Dk = len(Ws); T = hashimoto(Ws, rev); GT = np.kron(np.eye(Dk), Gm)
        iT_e = np.where(np.diag(GT) > 0)[0]; iT_o = np.where(np.diag(GT) < 0)[0]
        check(np.allclose(T @ GT, GT @ T), f"Hashimoto operator ({T.shape[0]} x {T.shape[0]}) commutes with Gamma (x) 1")
        te = np.linalg.eigvals(T[np.ix_(iT_e, iT_e)]); to = np.linalg.eigvals(T[np.ix_(iT_o, iT_o)])
        onc = lambda v: np.abs(np.abs(v) - np.sqrt(q)) < 1e-6
        triv = lambda v: (np.abs(np.abs(v) - 1) < 1e-6) | (np.abs(np.abs(v) - q) < 1e-6)
        check(np.all(onc(to) | (np.abs(np.abs(to) - 1) < 1e-6)), f"odd edge eigenvalues: {np.sum(onc(to))} on |mu| = sqrt q, {np.sum(np.abs(np.abs(to) - 1) < 1e-6)} at |mu| = 1 (the (1-u^2) factor), none elsewhere")
        check(np.all(onc(te) | triv(te)), f"even edge eigenvalues: {np.sum(onc(te))} on the circle, {np.sum(np.abs(np.abs(te) - q) < 1e-6)} at |mu| = q (trivial +-q), {np.sum(np.abs(np.abs(te) - 1) < 1e-6)} at |mu| = 1")
        u0 = 0.05 + 0.02j
        for name, iV, iT, nk in (("even", evi, iT_e, len(evi)), ("odd", odi, iT_o, len(odi))):
            lhs = np.linalg.det(np.eye(len(iT)) - u0 * T[np.ix_(iT, iT)])
            rhs = (1 - u0**2)**(nk * (Dk - 2) / 2) * np.linalg.det(np.eye(nk) - u0 * Sig[np.ix_(iV, iV)] + q * u0**2 * np.eye(nk))
            check(abs(lhs - rhs) < 1e-8 * abs(lhs), f"graded quantum Ihara-Bass on the {name} sector at u = {u0}")
        NT1, NTP = ring_norms(T, GT, 6)
        check(np.all(NTP >= -1e-6), f"non-backtracking parity-closed ring norms str T^n = {[round(x) for x in NTP]} >= 0")
        # NET divisor: even and odd sectors share eigenvalues; only nu = m_even - m_odd survives in the zeta
        def net(ev_e, ev_o, tol=1e-6):
            vals = list(ev_e) + list(ev_o); reps = []
            for v in vals:
                if not any(abs(v - r) < tol for r in reps): reps.append(v)
            return [(r, int(np.sum(np.abs(ev_e - r) < tol)), int(np.sum(np.abs(ev_o - r) < tol))) for r in reps]
        nv = net(sector_eigs(Sig, evi), sector_eigs(Sig, odi))
        poles = sum(max(m0 - m1, 0) for _, m0, m1 in nv); zeros = sum(max(m1 - m0, 0) for _, m0, m1 in nv)
        cancelled = sum(min(m0, m1) for _, m0, m1 in nv)
        print(f"   NET vertex divisor: {poles} net-even (poles, incl. +-(q+1)), {zeros} net-odd (zeros), {cancelled} cancelled pairs;"
              f" reduced graded Ihara zeta: numerator degree {2 * zeros}, denominator degree {2 * poles} (of which 4 structural)")
        check(np.sum(onc(to)) == 2 * len(odi) and np.sum(np.abs(np.abs(to) - 1) < 1e-6) == len(odi) * (Dk - 2), "raw odd edge count = 2 dim(odd) (two roots per quadratic) plus dim(odd)(D-2) trivial ones; the raw count is NOT the reduced numerator degree (prover correction)")
graded_harrow(5, 13, nmax=4, ihara=True)
graded_harrow(13, 5, nmax=4, ihara=True)

# ================================================================ (4) continuum: jump Lindbladian of the Pauli letters
print("(4) continuum limit of (1): jump Lindbladian L = sum_s g_s (Ad sigma_s - 1), Gamma-graded; spectrum = affine image")
g = {"X": 0.3, "Y": 0.5, "Z": 0.2}
Lb = sum(gs * (np.kron(S_, S_.conj()) - np.eye(4)) for gs, S_ in ((g["X"], X), (g["Y"], Y), (g["Z"], Z)))
G4, e4, o4 = sectors(P)
check(np.allclose(Lb @ G4, G4 @ Lb), "L commutes with Gamma: the grading survives the continuum limit (odd letters are jumps of finite rate)")
le, lo = np.sort(sector_eigs(Lb, e4).real), np.sort(sector_eigs(Lb, o4).real)
check(np.allclose(le, sorted([0, -2 * (g["X"] + g["Y"])])) and np.allclose(lo, sorted([-2 * (g["Z"] + g["Y"]), -2 * (g["Z"] + g["X"])])), f"even {{0, -2(g_X+g_Y)}} (fixed point, P-mode), odd {{-2(g_Z+g_Y), -2(g_Z+g_X)}}: the P-mode rate is twice the odd-letter rate")
eps_ = 1e-3; Phi_eps = np.eye(4) + eps_ * Lb
for n in (100, 1000):
    Ln = n * eps_; ex = spl.expm(Ln * Lb) if False else None
from scipy.linalg import expm
for Lr in (0.5, 2.0):
    n = int(round(Lr / eps_))
    NPd = np.trace(G4 @ np.linalg.matrix_power(Phi_eps, n)).real; NPc = np.trace(G4 @ expm(Lr * Lb)).real
    check(abs(NPd - NPc) < 5e-3 * max(1, abs(NPc)), f"graded Chernoff: str (1 + eps L)^(L/eps) -> str e^(L T) at L = {Lr} ({NPd:.6f} vs {NPc:.6f})")
check(np.all(np.array([np.trace(G4 @ expm(s * Lb)).real for s in np.linspace(0, 5, 26)]) >= -1e-12), "str e^{tL} >= 0 for t in [0,5]: the periodic ring norm of the graded cMPS")

print(f"\n{NCHK[1]}/{NCHK[0]} checks passed")
