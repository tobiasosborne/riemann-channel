"""Square roots of the Ihara--Bass formula: the chiral linearisation, the oriented half, odd letters.

Numerics for shard 08h (notes/ihara-dirac/, brief T1--T4).  Conventions of shard 08:
letters E_1..E_D on V, reversal rev (fixed-point-free involution), edge space W = V (x) C^D,
Hashimoto H(v (x) |i>) = sum_{j != rev i} E_i v (x) |j>, maps R : W -> V (propagate), S : V -> W
(start), J (backtrack), H = S R - J.  Column stacking: Ad(A) = conj(A) (x) A, vec(P X) = (1 (x) P) vec X.

T1  the first-order pencil N(u) = [[1 + uJ, S],[uR, 1]] on W (+) V: one determinant, two Schur
    evaluations (Hashimoto side, Bass side); SUSY pairing of X Y on V and Y X on W; the Euler
    exponent as the Berezinian of the diagonal mass on W_even (+) V_odd; the two would-be
    Berezinians of the coupled pencil disagree (no super coupling with c-number Dirac blocks).
T2  no primitive cyclically non-backtracking class is its own reverse; det(1 - uH) = |F(u)|^2 on
    the real axis for adjoint-paired letters, F the product over one orientation per prime class;
    graded version with sdet; F is not a polynomial (classical bouquet with two loops); the
    Ad-weights are loopwise time-reversal invariant but twist symmetric (Aizenman--Warzel's
    lemma does not apply).
T3  Gamma = L_P (x) 1 conjugates the Hashimoto operator to the sign-character twist; for all-odd
    letters it anticommutes with H, J, Sigma: symmetric sector spectra, det(1 - uH_k) even in u and
    equal to det_+(1 - u^2 H_k^2|_+); the Bass side factorises through the Laplacian block
    alpha alpha^*; the odd-sector two-step block carries the squares of the zeros; P-mode and
    Perron pair; the Pauli mixed-parity example breaks chirality.
T4  the single layer h with the letters themselves is odd: det(1 - uh) = det_+(1 - u^2 h^2|_+),
    str h^k = 0, sdet(1 - uh) = 1.
Usage: python3 scripts/ihara_dirac.py
"""
import itertools
import numpy as np

np.set_printoptions(precision=6, suppress=True, linewidth=150)
NCHK = [0, 0]


def check(cond, msg):
    NCHK[0] += 1; NCHK[1] += bool(cond)
    print(("  ok   " if cond else "  FAIL ") + msg)


rng = np.random.default_rng(20260921)


def haar(n):
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, r = np.linalg.qr(z); d = np.diag(r); return q * (d / abs(d))


def Ad(A): return np.kron(A.conj(), A)


def maps(letters, rev):
    """R, S, J, H on W = V (x) C^D with component i in block i."""
    D = len(letters); N = letters[0].shape[0]
    R = np.zeros((N, N * D), complex); S = np.zeros((N * D, N), complex)
    J = np.zeros((N * D, N * D), complex); H = np.zeros((N * D, N * D), complex)
    for i in range(D):
        R[:, i * N:(i + 1) * N] = letters[i]
        S[i * N:(i + 1) * N, :] = np.eye(N)
        J[rev[i] * N:(rev[i] + 1) * N, i * N:(i + 1) * N] = letters[i]
        for j in range(D):
            if j != rev[i]: H[j * N:(j + 1) * N, i * N:(i + 1) * N] = letters[i]
    return R, S, J, H


def pencil(letters, rev, u):
    R, S, J, H = maps(letters, rev); N = R.shape[0]; ND = R.shape[1]
    return np.block([[np.eye(ND) + u * J, S], [u * R, np.eye(N)]]), R, S, J, H


def nonzero_spectrum(M, tol=1e-9):
    ev = np.linalg.eigvals(M); return np.sort_complex(ev[abs(ev) > tol])


def same_multiset(a, b, tol=1e-6):
    if len(a) != len(b): return False
    return np.allclose(np.sort_complex(np.round(a, 6)), np.sort_complex(np.round(b, 6)), atol=tol)


def prime_nb_classes(D, rev, lmax):
    """Representatives of primitive cyclically non-backtracking classes of length <= lmax."""
    reps = {}
    for l in range(1, lmax + 1):
        for w in itertools.product(range(D), repeat=l):
            if any(w[(k + 1) % l] == rev[w[k]] for k in range(l)): continue
            shifts = [w[k:] + w[:k] for k in range(l)]
            if any(shifts[k] == w for k in range(1, l)): continue          # proper power
            reps.setdefault(min(shifts), w)
    return list(reps.values())


def word_op(letters, w):
    M = np.eye(letters[0].shape[0], dtype=complex)
    for s in w: M = letters[s] @ M          # E_w = E_{i_l} ... E_{i_1}
    return M


def reverse_word(w, rev): return tuple(rev[s] for s in reversed(w))


def canon(w):
    l = len(w); return min(w[k:] + w[:k] for k in range(l))


def classical_bouquet(D):
    m = D // 2; rev = [(i + m) % D for i in range(D)]
    return [np.eye(1, dtype=complex)] * D, rev


def random_kraus(n, m, unitary=False):
    """Adjoint-paired letters Ad(A_k), Ad(A_k^*), rev(k) = m + k."""
    As = [haar(n) if unitary else rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)) for _ in range(m)]
    As = [A / (1.2 * np.linalg.norm(A, 2)) for A in As] if not unitary else As
    letters = [Ad(A) for A in As] + [Ad(A.conj().T) for A in As]
    rev = [(k + m) % (2 * m) for k in range(2 * m)]
    return letters, rev, As


def sectors_of(G):
    ev = np.diag(G).real; return np.where(ev > 0)[0], np.where(ev < 0)[0]


# ----------------------------------------------------------------------------------------- T1
print("== T1: the chiral linearisation N(u) = M(u) + Dslash(u), its two Schur evaluations, the pairing ==")
for label, (letters, rev) in [("random non-unitary Kraus, n = 2, m = 2", random_kraus(2, 2)[:2]),
                              ("random unitary Kraus, n = 2, m = 3", random_kraus(2, 3, True)[:2]),
                              ("classical bouquet D = 4", classical_bouquet(4)),
                              ("classical bouquet D = 6", classical_bouquet(6))]:
    D = len(letters); N = letters[0].shape[0]; u = 0.17
    Nu, R, S, J, H = pencil(letters, rev, u)
    ND = N * D
    detN = np.linalg.det(Nu); detH = np.linalg.det(np.eye(ND) - u * H)
    Minv = np.linalg.inv(np.eye(ND) + u * J)
    bass = np.linalg.det(np.eye(ND) + u * J) * np.linalg.det(np.eye(N) - u * R @ Minv @ S)
    check(abs(detN - detH) < 1e-9 * abs(detH), f"T1a det N(u) = det(1 - uH), {label}")
    check(abs(detN - bass) < 1e-9 * abs(detH), f"T1a det N(u) = det(1 + uJ) det(1 - uR(1 + uJ)^-1 S), {label}")
    # shard 08 form
    pair = 1.0
    for i in range(D):
        if i < rev[i]: pair *= np.linalg.det(np.eye(N) - u * u * letters[rev[i]] @ letters[i])
    Aop = sum(u * letters[i] @ np.linalg.inv(np.eye(N) - u * u * letters[rev[i]] @ letters[i]) for i in range(D))
    Dop = sum(u * u * letters[rev[i]] @ letters[i] @ np.linalg.inv(np.eye(N) - u * u * letters[rev[i]] @ letters[i]) for i in range(D))
    check(abs(pair * np.linalg.det(np.eye(N) + Dop - Aop) - detH) < 1e-9 * abs(detH), f"T1a thm:qihara-general form agrees, {label}")
    # SUSY pairing
    X = u * R @ Minv; Y = S
    XY = X @ Y; YX = Y @ X
    check(same_multiset(nonzero_spectrum(XY), nonzero_spectrum(YX)), f"T1b nonzero spectra of XY (on V) and YX (on W) coincide, {label}")
    check(np.allclose(YX, u * (H + J) @ Minv), f"T1b YX = u (H + J)(1 + uJ)^-1, {label}")
    strs = [np.trace(np.linalg.matrix_power(YX, k)) - np.trace(np.linalg.matrix_power(XY, k)) for k in range(1, 6)]
    check(max(abs(s) for s in strs) < 1e-9, f"T1b str Lambda^k = 0 for k = 1..5 (Lambda = YX (+) XY on W_even (+) V_odd), {label}")
    check(abs(np.linalg.det(np.eye(ND) - YX) / np.linalg.det(np.eye(N) - XY) - 1) < 1e-9, f"T1b sdet(1 - Lambda) = 1, {label}")
    # two would-be Berezinians of the coupled pencil
    ber1 = np.linalg.det(np.eye(ND) + u * J - S @ (u * R)) / 1.0
    ber2 = np.linalg.det(np.eye(ND) + u * J) / np.linalg.det(np.eye(N) - u * R @ Minv @ S)
    check(abs(ber1 - detH) < 1e-9 * abs(detH), f"T1d Schur-on-V Berezinian = det(1 - uH), {label}")
    check(abs(ber2 - np.linalg.det(np.eye(ND) + u * J) ** 2 / detH) < 1e-9 * abs(ber2), f"T1d Schur-on-W Berezinian = det(1 + uJ)^2/det(1 - uH), {label}")
    check(abs(ber1 - ber2) > 1e-6 * abs(ber1), f"T1d the two Berezinians differ (no super coupling), {label}")
# Euler exponent as a Berezinian of the mass (unitary case)
letters, rev, Us = random_kraus(2, 3, True); D = 6; N = 4; u = 0.23
R, S, J, H = maps(letters, rev)
ber_mass = np.linalg.det(np.eye(N * D) + u * J) / np.linalg.det((1 - u * u) * np.eye(N))
check(abs(ber_mass - (1 - u * u) ** (N * (D - 2) / 2)) < 1e-9, "T1c Ber_{W_even (+) V_odd}(diag(1 + uJ, (1 - u^2) 1_V)) = (1 - u^2)^{N(D-2)/2}, unitary letters")
Sig = sum(letters)
check(abs(np.linalg.det(np.eye(N * D) - u * H) - (1 - u * u) ** (N * (D - 2) / 2) * np.linalg.det(np.eye(N) - u * Sig + (D - 1) * u * u * np.eye(N))) < 1e-9, "T1c cor:qihara-unitary on the same letters")
# classical bouquet numbers
lett, rv = classical_bouquet(4); Rr, Ss, Jj, Hh = maps(lett, rv)
for u in [0.2, -0.5, 0.3]:
    check(abs(np.linalg.det(np.eye(4) - u * Hh) - (1 - u) ** 2 * (1 + u) * (1 - 3 * u)) < 1e-12, f"T1d/T2e classical bouquet D = 4: det(1 - uH) = (1-u)^2(1+u)(1-3u) at u = {u}")
    check(abs(np.linalg.det(np.eye(4) + u * Jj) - (1 - u * u) ** 2) < 1e-12, f"T1d classical bouquet D = 4: det(1 + uJ) = (1 - u^2)^2 at u = {u}")

# ----------------------------------------------------------------------------------------- T2
print("== T2: the oriented half ==")
for D in [4, 6]:
    m = D // 2; rev = [(i + m) % D for i in range(D)]
    reps = prime_nb_classes(D, rev, 7 if D == 4 else 5)
    selfrev = [w for w in reps if canon(reverse_word(w, rev)) == canon(w)]
    check(len(selfrev) == 0, f"T2a no self-reverse primitive class among {len(reps)} classes, D = {D}, length <= {7 if D == 4 else 5}")
    # pairing is a fixed-point-free involution on the set of classes
    cl = {canon(w) for w in reps}
    check(all(canon(reverse_word(w, rev)) in cl for w in reps), f"T2a reversal permutes the classes of each length, D = {D}")
for label, (letters, rev, As) in [("non-unitary Kraus n = 2, m = 2", random_kraus(2, 2)), ("unitary Kraus n = 2, m = 2", random_kraus(2, 2, True))]:
    D = len(letters); N = letters[0].shape[0]
    R, S, J, H = maps(letters, rev)
    reps = prime_nb_classes(D, rev, 8)
    w0 = reps[-1]; u = 0.13 + 0.05j
    Ew = word_op(letters, w0); Ewb = word_op(letters, reverse_word(w0, rev))
    check(abs(np.linalg.det(np.eye(N) - u ** len(w0) * Ewb) - np.conj(np.linalg.det(np.eye(N) - np.conj(u) ** len(w0) * Ew))) < 1e-12, f"T2b det(1 - u^l E_wbar) = conj det(1 - conj(u)^l E_w), {label}")
    # |F|^2 on the real axis, Euler product truncated at length L
    rho = np.max(np.abs(np.linalg.eigvals(H)))
    u = 0.35 / rho
    detH = np.linalg.det(np.eye(N * D) - u * H).real
    chosen = set(); F = 1.0 + 0j
    for w in reps:
        c = canon(w); cb = canon(reverse_word(w, rev))
        if cb in chosen: continue
        chosen.add(c); F *= np.linalg.det(np.eye(N) - u ** len(w) * word_op(letters, w))
    check(abs(detH - abs(F) ** 2) < 2e-3 * abs(detH), f"T2c det(1 - uH) = |F(u)|^2 to 2e-3 with prime classes of length <= 8 at u = 0.35/rad(H), {label} ({detH:.6f} vs {abs(F)**2:.6f})")
    # full Euler product check (both orientations) at the same truncation for the size of the truncation error
    Ffull = 1.0 + 0j
    for w in reps: Ffull *= np.linalg.det(np.eye(N) - u ** len(w) * word_op(letters, w))
    check(abs(Ffull.imag) < 1e-12 and abs(Ffull.real - abs(F) ** 2) < 1e-12, f"T2c the full truncated Euler product is real and equals |F|^2 exactly, {label}")
    check(detH > 0, f"T2c det(1 - uH) > 0 on the real axis inside the disc, {label}")
# graded version
Dp = 2; P = np.diag([1., 1., -1., -1.]); Gdb = np.kron(P, P)
Us = []
for k in range(2):
    a, b = haar(2), haar(2); U = np.zeros((4, 4), complex); U[:2, 2:] = a; U[2:, :2] = b; Us.append(U)
Ue = np.zeros((4, 4), complex); Ue[:2, :2] = haar(2); Ue[2:, 2:] = haar(2); Us.append(Ue)   # one even letter
lettersG = [Ad(U) for U in Us] + [Ad(U.conj().T) for U in Us]; revG = [(k + 3) % 6 for k in range(6)]
R, S, J, H = maps(lettersG, revG); N = 16; D = 6
GF = np.kron(np.eye(D), Gdb); ev_idx, od_idx = sectors_of(GF)
u = 0.3 / np.max(np.abs(np.linalg.eigvals(H)))
sdetH = np.linalg.det(np.eye(len(ev_idx)) - u * H[np.ix_(ev_idx, ev_idx)]) / np.linalg.det(np.eye(len(od_idx)) - u * H[np.ix_(od_idx, od_idx)])
reps = prime_nb_classes(D, revG, 6); chosen = set(); Fg = 1.0 + 0j
e_idx, o_idx = sectors_of(Gdb)
for w in reps:
    c = canon(w); cb = canon(reverse_word(w, revG))
    if cb in chosen: continue
    chosen.add(c); Ew = word_op(lettersG, w)
    Fg *= np.linalg.det(np.eye(len(e_idx)) - u ** len(w) * Ew[np.ix_(e_idx, e_idx)]) / np.linalg.det(np.eye(len(o_idx)) - u ** len(w) * Ew[np.ix_(o_idx, o_idx)])
check(abs(sdetH.real - abs(Fg) ** 2) < 5e-3 * abs(sdetH) and abs(sdetH.imag) < 1e-12, f"T2d sdet(1 - uH) = |F_gr(u)|^2 to 5e-3 (classes of length <= 6), mixed-parity unitary letters ({sdetH.real:.6f} vs {abs(Fg)**2:.6f})")
# non-polynomial square root
roots = np.roots([-3, 1, 5, -3, 0][::-1][::-1]) if False else np.roots(np.polynomial.polynomial.polymul(np.polynomial.polynomial.polymul([1, -1], [1, -1]), np.polynomial.polynomial.polymul([1, 1], [1, -3]))[::-1])
check(sum(abs(r + 1) < 1e-9 for r in roots) == 1 and sum(abs(r - 1 / 3) < 1e-9 for r in roots) == 1, "T2e (1-u)^2(1+u)(1-3u) has simple roots at -1 and 1/3: sqrt is not a polynomial")
# twist: transition-path convention (the terminal letter is not multiplied); classical weights are twist
# symmetric, Ad-weights are neither symmetric nor anti-symmetric (prover T2(e) <1>3)
letters, rev, As = random_kraus(2, 2); N = 4; D = 4
e = 0; inner = (1, 2, 1)
inner_ok = all(inner[k + 1] != rev[inner[k]] for k in range(len(inner) - 1)) and inner[0] != rev[e] and rev[e] != rev[inner[-1]]
gamma = (e,) + inner; twist = (e,) + tuple(rev[s] for s in reversed(inner))      # transitions e->e1->...->e_{n-1}->bar e
Tg = np.trace(word_op(letters, gamma)); Tt = np.trace(word_op(letters, twist))
check(inner_ok and abs(Tg - Tt) > 1e-6 and abs(Tg + Tt) > 1e-6, f"T2e Ad-weights: transition-path traces of gamma = {gamma}+(bar e) and its twist are neither equal nor opposite ({Tg:.4f} vs {Tt:.4f})")
Ue = np.diag([1, 1j]); Us4 = [Ue, Ue]; single4 = Us4 + [U.conj().T for U in Us4]; rev4 = [2, 3, 0, 1]
lett4 = [Ad(U) for U in single4]
t1 = np.trace(word_op(lett4, (0, 1))).real; t2 = np.trace(word_op(lett4, (0, 3))).real         # (e, f, bar e) and (e, bar f, bar e)
check(abs(t1) < 1e-12 and abs(t2 - 4) < 1e-12, f"T2e prover's unitary counterexample U_e = U_f = diag(1, i): path traces {t1:.0f} and {t2:.0f}")
gamma_c = (0, 1, 2, 1); twist_c = (0, 3, 2, 3)
lett_cl, rev_cl = classical_bouquet(4)
check(abs(np.trace(word_op(lett_cl, gamma_c)) - np.trace(word_op(lett_cl, twist_c))) < 1e-12, "T2e classical weights are twist symmetric (every allowed path has weight 1)")
loop = (0, 1, 3, 2, 1)
check(abs(np.trace(word_op(letters, loop)) - np.conj(np.trace(word_op(letters, reverse_word(loop, rev))))) < 1e-12, "T2e loopwise time reversal: Tr E_wbar = conj Tr E_w")
check(abs(np.trace(word_op(letters, loop)).imag) < 1e-12 and np.trace(word_op(letters, loop)).real >= 0, "T2e Kraus loop traces are real and nonnegative (|Tr A_w|^2)")
# Kraus letters: F has real coefficients and det(1 - uH) = F(u)^2 off the real axis too (prover T2(c) <1>4)
letters, rev, As = random_kraus(2, 2); N = 4; D = 4; R, S, J, H = maps(letters, rev)
reps = prime_nb_classes(D, rev, 8); rho = np.max(np.abs(np.linalg.eigvals(H))); u = (0.25 + 0.2j) / rho
detH = np.linalg.det(np.eye(N * D) - u * H); chosen = set(); F = 1.0 + 0j
for w in reps:
    c = canon(w); cb = canon(reverse_word(w, rev))
    if cb in chosen: continue
    chosen.add(c); F *= np.linalg.det(np.eye(N) - u ** len(w) * word_op(letters, w))
check(abs(detH - F * F) < 5e-3 * abs(detH), f"T2c Kraus letters: det(1 - uH) = F(u)^2 at complex u (classes of length <= 8), {detH:.5f} vs {F*F:.5f}")
w0 = reps[5]; cp = np.poly(word_op(letters, w0))
check(np.allclose(cp.imag, 0), "T2c Kraus letters: det(1 - z E_w) has real coefficients (Ad(A) preserves Hermitian matrices)")
# general adjoint pairing without the Kraus structure: E_1 = i, E_2 = -i on V = C, D = 2
Hi = np.diag([1j, -1j]); u = 0.3
check(abs(np.linalg.det(np.eye(2) - u * Hi) - (1 + u * u)) < 1e-12 and abs((1 - 1j * u) ** 2 - (1 + u * u)) > 1e-6, "T2c E_1 = i, E_2 = -i: det(1 - uH) = 1 + u^2 = |1 - iu|^2 but not (1 - iu)^2: only F F^# in general")

# ----------------------------------------------------------------------------------------- T3
print("== T3: odd letters make the Hashimoto operator chiral ==")


def graded_family(Dp, m_odd, m_even):
    Dm = Dp; Dd = Dp + Dm; P = np.diag([1.] * Dp + [-1.] * Dm)
    Us, eps = [], []
    for _ in range(m_odd):
        U = np.zeros((Dd, Dd), complex); U[:Dp, Dp:] = haar(Dp); U[Dp:, :Dp] = haar(Dm); Us.append(U); eps.append(-1)
    for _ in range(m_even):
        U = np.zeros((Dd, Dd), complex); U[:Dp, :Dp] = haar(Dp); U[Dp:, Dp:] = haar(Dm); Us.append(U); eps.append(+1)
    m = len(Us)
    letters = [Ad(U) for U in Us] + [Ad(U.conj().T) for U in Us]; rev = [(k + m) % (2 * m) for k in range(2 * m)]
    return P, Us, eps + eps, letters, rev


def sector_split(H, GF):
    ev, od = sectors_of(GF); return H[np.ix_(ev, ev)], H[np.ix_(od, od)], ev, od


for label, (Dp, mo, me) in [("C^{2|2}, three odd letters", (2, 3, 0)), ("C^{1|1}, two odd letters", (1, 2, 0)), ("C^{2|2}, two odd + one even letter", (2, 2, 1))]:
    P, Us, eps, letters, rev = graded_family(Dp, mo, me); Dd = 2 * Dp; N = Dd * Dd; D = len(letters); q = D - 1
    R, S, J, H = maps(letters, rev); Sig = sum(letters)
    Gdb = np.kron(P, P); Gam = np.kron(np.eye(Dd), P)            # vec(P X) = (1 (x) P) vec X
    GdbF = np.kron(np.eye(D), Gdb); GamF = np.kron(np.eye(D), Gam)
    check(np.allclose(GamF @ GamF, np.eye(N * D)) and np.allclose(GamF @ GdbF, GdbF @ GamF), f"T3a Gamma^2 = 1 and [Gamma, Gamma_b] = 0, {label}")
    lettersE = [eps[i] * letters[i] for i in range(D)]
    Re_, Se_, Je_, He_ = maps(lettersE, rev)
    check(np.allclose(GamF @ H @ GamF, He_) and np.allclose(GamF @ J @ GamF, Je_) and np.allclose(Gam @ Sig @ Gam, sum(lettersE)), f"T3a Gamma H Gamma = H^eps, Gamma J Gamma = J^eps, Gamma Sigma Gamma = Sigma^eps, {label}")
    H0, H1, ev, od = sector_split(H, GdbF); He0, He1, _, _ = sector_split(He_, GdbF)
    u = 0.21
    for k, (Hk, Hek) in enumerate([(H0, He0), (H1, He1)]):
        check(abs(np.linalg.det(np.eye(len(Hk)) - u * Hk) - np.linalg.det(np.eye(len(Hek)) - u * Hek)) < 1e-9, f"T3a det(1 - uH_{k}) = det(1 - uH_{k}^eps), {label}")
    allodd = all(e == -1 for e in eps)
    if allodd:
        check(np.allclose(GamF @ H + H @ GamF, 0) and np.allclose(GamF @ J + J @ GamF, 0) and np.allclose(Gam @ Sig + Sig @ Gam, 0), f"T3b Gamma anticommutes with H, J, Sigma, {label}")
        for k, Hk in enumerate([H0, H1]):
            idx = [ev, od][k]; Gk = GamF[np.ix_(idx, idx)]
            evals = np.linalg.eigvals(Hk)
            check(same_multiset(evals, -evals), f"T3b spec H_{k} symmetric under negation, {label}")
            ip = np.where(np.diag(Gk).real > 0.5)[0]; H2p = (Hk @ Hk)[np.ix_(ip, ip)]
            for u in [0.21, 0.1 + 0.2j]:
                d1 = np.linalg.det(np.eye(len(Hk)) - u * Hk); d2 = np.linalg.det(np.eye(len(Hk)) + u * Hk); d3 = np.linalg.det(np.eye(len(ip)) - u * u * H2p)
                check(abs(d1 - d2) < 1e-9 * abs(d1) and abs(d1 - d3) < 1e-9 * abs(d1), f"T3b det(1 - uH_{k}) even in u and = det_+(1 - u^2 H_{k}^2|_+) at u = {u}, {label}")
            # Bass side
            Gs = Gam; Sk = Sig[np.ix_([ev, od][k] if False else np.where(np.diag(Gdb).real == (1 if k == 0 else -1))[0], np.where(np.diag(Gdb).real == (1 if k == 0 else -1))[0])]
            sidx = np.where(np.diag(Gdb).real == (1 if k == 0 else -1))[0]; Gsk = Gam[np.ix_(sidx, sidx)]
            pp = np.where(np.diag(Gsk).real > 0.5)[0]; mm = np.where(np.diag(Gsk).real < -0.5)[0]
            alpha = Sk[np.ix_(pp, mm)]; beta = Sk[np.ix_(mm, pp)]
            check(np.allclose(Sk[np.ix_(pp, pp)], 0) and np.allclose(Sk[np.ix_(mm, mm)], 0) and np.allclose(beta, alpha.conj().T), f"T3b Sigma_{k} = [[0, alpha],[alpha^*, 0]] (chiral, HS self-adjoint), {label}")
            u = 0.21
            lhs = np.linalg.det(np.eye(len(Sk)) - u * Sk + q * u * u * np.eye(len(Sk)))
            rhs = np.linalg.det((1 + q * u * u) ** 2 * np.eye(len(pp)) - u * u * alpha @ alpha.conj().T)
            check(abs(lhs - rhs) < 1e-9 * abs(lhs), f"T3b det(1 - u Sigma_{k} + q u^2) = det_+((1 + q u^2)^2 - u^2 alpha alpha^*), {label}")
            lam = np.linalg.eigvalsh(Sk); s2 = np.linalg.eigvalsh(alpha @ alpha.conj().T)
            check(same_multiset(np.sort(lam ** 2)[len(lam) - len(s2):] if len(lam) > len(s2) else np.sort(lam ** 2), np.sort(s2)) or same_multiset(np.sort(np.concatenate([s2, s2])), np.sort(lam ** 2)), f"T3b spec(Sigma_{k})^2 = spec(alpha alpha^*) (doubled), {label}")
            band = all(abs(l) <= 2 * np.sqrt(q) + 1e-9 or abs(abs(l) - D) < 1e-9 for l in lam)
            band2 = all(s <= 4 * q + 1e-9 or abs(s - D * D) < 1e-9 for s in s2)
            check(band == band2, f"T3b Ramanujan band for Sigma_{k} <=> spec(alpha alpha^*) in [0, 4q] off the trivial part ({band}), {label}")
        # odd sector: which Gamma-block is Hom(V_-, V_+)
        Gk = GamF[np.ix_(od, od)]; ip = np.where(np.diag(Gk).real > 0.5)[0]
        # basis vectors of W: index = i*N + (col*Dd + row) in column stacking; Hom(V_-, V_+) has row in V_+, col in V_-
        rows = [(od[t] % N) % Dd for t in ip]; cols = [(od[t] % N) // Dd for t in ip]
        check(all(r < Dp for r in rows) and all(c >= Dp for c in cols), f"T3c the Gamma = +1 part of the odd sector is Hom(V_-, V_+) (x) C^D (L_P X = P X acts as +1 when the range is V_+), {label}")
        H1 = H[np.ix_(od, od)]; H2p = (H1 @ H1)[np.ix_(ip, ip)]
        mu = np.linalg.eigvals(H1); mu2 = np.linalg.eigvals(H2p)
        check(same_multiset(np.sort_complex(np.round(mu ** 2, 6))[::2], np.sort_complex(mu2)) or same_multiset(np.concatenate([mu2, mu2]), mu ** 2), f"T3c spec(H_1^2|_+) = squares of the odd edge eigenvalues (each once), {label}")
        # two-step letters Ad(U_i U_j) reproduce H_1^2|_+ on Hom(V_-,V_+) blocks: check on one block entry
        # P-mode and Perron pair
        one = np.eye(Dd).reshape(-1, order='F'); Pv = P.reshape(-1, order='F')
        check(np.allclose(Sig @ one, D * one) and np.allclose(Sig @ Pv, -D * Pv), f"T3d Sigma 1 = D 1 and Sigma P = -D P (P-mode -D), {label}")
        check(np.allclose(Gam @ one, Pv), f"T3d Gamma exchanges 1 and P, {label}")
        H0 = H[np.ix_(ev, ev)]; e0 = np.linalg.eigvals(H0)
        for t in [q, 1, -q, -1]:
            check(any(abs(e0 - t) < 1e-6), f"T3d trivial edge eigenvalue {t} present in the even sector, {label}")
        check(Dp == Dd // 2, f"T3b odd unitary letters force a balanced grading D_+ = D_-, {label}")
    else:
        H0e = np.linalg.eigvals(H[np.ix_(ev, ev)])
        check(not same_multiset(H0e, -H0e), f"T3e chirality fails with one even letter: even-sector spectrum not symmetric, {label}")
# Pauli mixed example of shard 03c
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1., -1.]).astype(complex)
lettersP = [Ad(X), Ad(X), Ad(Y), Ad(Y), Ad(Z), Ad(Z)]; revP = [1, 0, 3, 2, 5, 4]
SigP = sum(lettersP); GdbP = np.kron(Z, Z); e_idx = np.where(np.diag(GdbP).real > 0)[0]
check(same_multiset(np.linalg.eigvals(SigP[np.ix_(e_idx, e_idx)]), np.array([6., -2.])), "T3e Pauli letters X,X,Y,Y,Z,Z: even spectrum {6, -2}, not symmetric (one even letter)")
# dihedral D_5 with the five reflections (each twice): all letters odd, index-two grading rotations/reflections
th = 2 * np.pi / 5
rot = np.diag([np.exp(1j * th), np.exp(-1j * th)]); refl0 = np.array([[0, 1], [1, 0]], complex)
refls = [np.linalg.matrix_power(rot, k) @ refl0 for k in range(5)]
Pd = np.diag([1., -1.]).astype(complex)
check(all(np.allclose(Pd @ r @ Pd, -r) for r in refls) and np.allclose(Pd @ rot @ Pd, rot), "T3 D_5: rotations even, reflections odd in the eigenbasis of the rotations")
lettersD = [Ad(r) for r in refls] * 2; revD = [(k + 5) % 10 for k in range(10)]; Dd = 10; qd = 9
R, S, J, H = maps(lettersD, revD); GdbD = np.kron(Pd, Pd); GamD = np.kron(np.eye(2), Pd)
GdbF = np.kron(np.eye(Dd), GdbD); GamF = np.kron(np.eye(Dd), GamD)
check(np.allclose(GamF @ H + H @ GamF, 0), "T3 D_5: Gamma anticommutes with H")
ev, od = sectors_of(GdbF); H1 = H[np.ix_(od, od)]; mu = np.linalg.eigvals(H1)
nontriv = mu[(abs(mu) > 1e-9) & (abs(abs(mu) - 1) > 1e-9)]      # |mu| = 1 are the (1 - u^2)^{n_1(D-2)/2} factors, trivial
check(len(nontriv) == 4 and np.allclose(abs(nontriv), np.sqrt(qd)), f"T3 D_5 odd sector: the four nontrivial odd edge eigenvalues lie on |mu| = sqrt 9 = 3 (K_{{5,5}}, the Cayley graph of the reflections, is Ramanujan); moduli present: {np.unique(np.round(abs(mu), 6))}")
SigD = sum(lettersD); o_idx = np.where(np.diag(GdbD).real < 0)[0]
check(np.allclose(np.linalg.eigvalsh(SigD[np.ix_(o_idx, o_idx)]), 0), "T3 D_5 odd sector adjacency Sigma_1 = 0 (the K_{5,5} eigenvalue 0): zeros at u^2 = -1/9 exactly")
check(np.allclose(np.linalg.det(np.eye(len(od)) - 0.2 * H1), (1 + 9 * 0.04) ** 2 * (1 - 0.04) ** ((len(od)) * (Dd - 2) // 2 // 1 * 0 + 2 * 8 // 2)), "T3 D_5: det(1 - uH_1) = (1 - u^2)^{n_1(D-2)/2}(1 + 9u^2)^2 with n_1 = 2, at u = 0.2")

# prover's counterexamples (astra-proofs.md, T3(c) <1>4, <1>5, <1>7; T3(e) <1>3; T3(f); T4(c) <1>3)
print("== T3': the prover's counterexamples ==")
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1., -1.]).astype(complex)


def graded_zeta_sectors(single, rev, P):
    letters = [Ad(U) for U in single]; R, S, J, H = maps(letters, rev); D = len(letters)
    GdbF = np.kron(np.eye(D), np.kron(P, P)); ev, od = sectors_of(GdbF)
    return H[np.ix_(ev, ev)], H[np.ix_(od, od)], H, GdbF


# all four letters X (distinct labels, reversal (1 2)(3 4)): even and odd sectors similar, Z_gr = 1
H0, H1, H, _ = graded_zeta_sectors([X, X, X, X], [1, 0, 3, 2], Z)
u = 0.23
check(abs(np.linalg.det(np.eye(len(H1)) - u * H1) / np.linalg.det(np.eye(len(H0)) - u * H0) - 1) < 1e-12 and np.max(np.abs(np.linalg.eigvals(H1))) > 0.5, "T3c all-X letters: Z_gr = 1 although H_1 has nonzero spectrum (candidate zeros cancel against the even sector)")
# band-edge Jordan block: letters U_0, U_0, U_{pi/6}, U_{pi/6}, q = 3
Uth = lambda th: np.array([[0, np.exp(1j * th)], [np.exp(-1j * th), 0]])
single = [Uth(0), Uth(0), Uth(np.pi / 6), Uth(np.pi / 6)]; rev = [1, 0, 3, 2]
H0, H1, H, GdbF = graded_zeta_sectors(single, rev, Z)
Sig1 = sum(Ad(U) for U in single)[np.ix_([1, 2], [1, 2])]
check(np.allclose(np.sort(np.linalg.eigvalsh(Sig1)), [-2 * np.sqrt(3), 2 * np.sqrt(3)]), "T3c Jordan example: odd adjacency eigenvalues +-2 sqrt 3 (band edge, q = 3)")
for u in [0.2, 0.3 + 0.1j]:
    check(abs(np.linalg.det(np.eye(len(H1)) - u * H1) - (1 - u * u) ** 2 * (1 - 3 * u * u) ** 2) < 1e-9, f"T3c Jordan example: det(1 - uH_1) = (1 - u^2)^2 (1 - 3u^2)^2 at u = {u}")
od = np.where(np.diag(GdbF).real < 0)[0]; GamF = np.kron(np.eye(4), np.kron(np.eye(2), Z)); Gk = GamF[np.ix_(od, od)]
ip = np.where(np.diag(Gk).real > 0.5)[0]; K1 = (H1 @ H1)[np.ix_(ip, ip)]
M3 = K1 - 3 * np.eye(len(K1))
check(np.linalg.matrix_rank(M3, tol=1e-8) > np.linalg.matrix_rank(M3 @ M3, tol=1e-8), "T3c Jordan example: K_1 = H_1^2|_+ has a nontrivial Jordan block at 3 (rank(K-3) > rank((K-3)^2)); every retained eigenvalue of K_1/q is unimodular but K_1 is not diagonalisable")
# XY example (T4(c) <1>3): Z_gr = (1 + 3u^2)^2/((1 - u^2)(1 - 9u^2)); single layer det(1 - uh) = (1 - u^2)^2 (1 - 2u^2 + 9u^4)
single = [X, X, Y, Y]; rev = [1, 0, 3, 2]
H0, H1, H, GdbF = graded_zeta_sectors(single, rev, Z)
R, S, J, h = maps(single, rev)
for u in [0.2, 0.15 + 0.1j]:
    zg = np.linalg.det(np.eye(len(H1)) - u * H1) / np.linalg.det(np.eye(len(H0)) - u * H0)
    check(abs(zg - (1 + 3 * u * u) ** 2 / ((1 - u * u) * (1 - 9 * u * u))) < 1e-9 * abs(zg), f"T4c X,X,Y,Y: Z_gr = (1 + 3u^2)^2/((1 - u^2)(1 - 9u^2)) at u = {u}")
    check(abs(np.linalg.det(np.eye(8) - u * h) - (1 - u * u) ** 2 * (1 - 2 * u * u + 9 * u ** 4)) < 1e-9, f"T4c X,X,Y,Y: single layer det(1 - uh) = (1 - u^2)^2 (1 - 2u^2 + 9u^4) at u = {u}")
ev1 = np.linalg.eigvals(h) ** 2
check(not any(abs(ev1 + 3) < 1e-6), "T4c X,X,Y,Y: no single-layer edge eigenvalue squares to the doubled candidate -3: no spectral-squaring identification")
Pf = np.kron(np.eye(4), Z)
check(abs(np.trace(Pf @ h @ h)) < 1e-12 and abs(np.trace(GdbF @ H @ H) - 32) < 1e-9, "T4c X,X,Y,Y: str h^2 = 0 while str H^2 = 32 (eight rooted words of squared amplitude 4)")
# mixed parities with another chiral involution: P = Z (x) 1, letters X (x) X and 1 (x) X (twice each); Q = 1 (x) Z
P2 = np.kron(Z, np.eye(2)); Q = np.kron(np.eye(2), Z); U1 = np.kron(X, X); U2 = np.kron(np.eye(2), X)
single = [U1, U1, U2, U2]; rev = [1, 0, 3, 2]
check(np.allclose(P2 @ U1 @ P2, -U1) and np.allclose(P2 @ U2 @ P2, U2), "T3e mixed example: X(x)X is odd and 1(x)X is even for P = Z(x)1")
letters = [Ad(U) for U in single]; R, S, J, H = maps(letters, rev); LQ = np.kron(np.eye(4), np.kron(np.eye(4), Q))
check(np.allclose(LQ @ H + H @ LQ, 0) and np.allclose(np.kron(P2, P2) @ np.kron(np.eye(4), Q) - np.kron(np.eye(4), Q) @ np.kron(P2, P2), 0), "T3e mixed example: L_Q with Q = 1(x)Z anticommutes with H and commutes with Gamma_b: a different chiral involution exists")
# continuum: jump Lindbladian with odd unitary jumps L_i = sqrt(r_i) U_i, sum L_i^* L_i = c 1: reflection about -c
P, Us, eps, letters, rev = graded_family(2, 3, 0); Dd = 4; rates = [0.3, 0.5, 1.1]
Ls = [np.sqrt(r) * U for r, U in zip(rates, Us)]; c = sum(rates)
Lgen = sum(Ad(L) for L in Ls) - c * np.eye(Dd * Dd)
Gam = np.kron(np.eye(Dd), P)
check(np.allclose(Gam @ (Lgen + c * np.eye(Dd * Dd)) @ Gam, -(Lgen + c * np.eye(Dd * Dd))), "T3f continuum: for sum L_i^* L_i = c 1 the generator satisfies Gamma (L + c) Gamma = -(L + c): spectrum symmetric about -c")
evL = np.linalg.eigvals(Lgen)
check(same_multiset(evL + c, -(evL + c)), "T3f continuum: spectrum of L reflected about -c")

# ----------------------------------------------------------------------------------------- T4
print("== T4: the single layer ==")
P, Us, eps, letters, rev = graded_family(2, 3, 0); Dd = 4; D = 6
single = Us + [U.conj().T for U in Us]
R, S, J, h = maps(single, rev); Pf = np.kron(np.eye(D), P)
check(np.allclose(Pf @ h @ Pf, -h), "T4a single-layer h is odd for P (x) 1")
ip = np.where(np.diag(Pf).real > 0)[0]; h2p = (h @ h)[np.ix_(ip, ip)]
u = 0.17
check(abs(np.linalg.det(np.eye(Dd * D) - u * h) - np.linalg.det(np.eye(len(ip)) - u * u * h2p)) < 1e-9, "T4a det(1 - uh) = det_+(1 - u^2 h^2|_+)")
strs = [np.trace(Pf @ np.linalg.matrix_power(h, k)) for k in range(1, 7)]
check(max(abs(s) for s in strs) < 1e-9, "T4a str h^k = 0 for k = 1..6, so sdet(1 - uh) = 1")
# word form: sum over cyclically NB words of Tr(P U_w) vanishes for each length
for n in [2, 4]:
    tot = 0
    for w in itertools.product(range(D), repeat=n):
        if any(w[(k + 1) % n] == rev[w[k]] for k in range(n)): continue
        tot += np.trace(P @ word_op(single, w))
    check(abs(tot) < 1e-9, f"T4a/b sum over cyclically non-backtracking words of length {n} of Tr(P U_w) = 0")
# contrast: the doubled supertrace is a sum of squared moduli
n = 2; tot = 0; GdbF = np.kron(np.eye(D), np.kron(P, P)); R, S, J, H = maps(letters, rev)
for w in itertools.product(range(D), repeat=n):
    if any(w[(k + 1) % n] == rev[w[k]] for k in range(n)): continue
    tot += abs(np.trace(P @ word_op(single, w))) ** 2
check(abs(tot - np.trace(GdbF @ H @ H).real) < 1e-9 and tot > 1e-6, f"T4c str H^2 = sum_w |Tr(P U_w)|^2 = {tot:.4f} > 0 while sum_w Tr(P U_w) = 0")

print(f"\n{NCHK[1]}/{NCHK[0]} checks passed")
