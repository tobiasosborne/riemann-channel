"""REFUTE review, graded toys 2026-09-20: independent lane, script 3.

thm:renewal-graded-mps (G3), thm:glued-graded-toy, prop:shared-exit-tradeoff,
lem:even-letters-two-fixed-points.

The D2 model space is built from scratch out of the inner function
Theta_2 = Pc/qq with the basis {Theta/w^2, Theta/w, Theta/(w-a)} whose Gram is
computed EXACTLY by residues (no quadrature), and cross-checked against a
Taylor-coefficient computation.  Nothing is imported from any repository script.
"""
import itertools
import numpy as np
import sympy as sp

PASS = [0]
FAIL = []


def check(name, cond, info=""):
    if cond:
        PASS[0] += 1
    else:
        FAIL.append((name, info))
        print("FAIL  %-62s %s" % (name, info))


np.set_printoptions(linewidth=200)
w = sp.Symbol('w')

# ------------------------------------------------------------------ D2 model
q = 2.0
# resonances: double 0 and the four roots of 2z^4 - 2z^2 + 1
hw = np.roots([2, 0, -2, 0, 1])
hw = np.array(sorted(hw, key=lambda c: (round(c.real, 12), round(c.imag, 12))))
check('D2: four HW roots on |z| = q^{-1/4}',
      np.max(np.abs(np.abs(hw) - q ** -0.25)) < 1e-12, str(np.abs(hw)))
check('D2: z^2 = 1/alpha_pm', 
      min(abs(hw[0] ** 2 - 1 / (1 - 1j)), abs(hw[0] ** 2 - 1 / (1 + 1j))) < 1e-12)
roots_all = np.concatenate([[0.0, 0.0], hw])
N = 6

# Theta = Pc/qq
Pc = np.poly(roots_all)                       # monic
qq = np.poly(np.concatenate([[0.0, 0.0], 1.0 / np.conj(hw)]))  # (w - 1/conj z_j) ...
qq = np.real(np.poly(1.0 / np.conj(hw)))      # degree 4, monic
qq = qq / qq[-1]                              # normalise so qq(0) = 1 -> prod(1 - conj z_j w)
qq_rev = qq[::-1]                             # ascending coefficients, qq(0)=1
check('qq(w) = prod(1 - conj z_j w) has real coefficients', np.max(np.abs(np.imag(qq))) < 1e-12)
# Theta_2 registered form: z^2(2z^4-2z^2+1)/(z^4-2z^2+2)
num_ref = np.array([2, 0, -2, 0, 1, 0, 0], dtype=float)     # descending: 2w^6-2w^4+w^2
den_ref = np.array([1, 0, -2, 0, 2], dtype=float)
for wv in (0.3 + 0.2j, -0.5 + 0.1j, 0.7j):
    th_ref = np.polyval(num_ref, wv) / np.polyval(den_ref, wv)
    th_mine = np.polyval(Pc, wv) / np.polyval(qq[::-1][::-1], wv) * 1.0
    th_mine = np.polyval(Pc, wv) / np.polyval(qq, wv)
    check('Theta_2 = Pc/qq matches thm:h-exit-model at %s' % wv,
          abs(th_ref - th_mine) < 1e-10, '%s %s' % (th_ref, th_mine))
for th in np.linspace(0, 2 * np.pi, 17):
    wv = np.exp(1j * th)
    check('Theta_2 inner (|Theta|=1 on the circle)',
          abs(abs(np.polyval(Pc, wv) / np.polyval(qq, wv)) - 1) < 1e-10)

# basis: g1 = Theta/w^2, g2 = Theta/w, k_a = Theta/(w-a)
BAS = ['g1', 'g2'] + ['k%d' % i for i in range(4)]
def gram_entry(x, y):
    """<x,y> with the first slot conjugated; Theta inner so it reduces to <1/u,1/v>."""
    if x == 'g1' and y == 'g1':
        return 1.0
    if x == 'g2' and y == 'g2':
        return 1.0
    if {x, y} == {'g1', 'g2'}:
        return 0.0
    if x == 'g1':
        return hw[int(y[1:])]                       # <1/w^2, 1/(w-b)> = b
    if y == 'g1':
        return np.conj(hw[int(x[1:])])
    if x == 'g2':
        return 1.0                                  # <1/w, 1/(w-b)> = 1
    if y == 'g2':
        return 1.0
    a = hw[int(x[1:])]
    b = hw[int(y[1:])]
    return 1.0 / (1 - np.conj(a) * b)


G = np.array([[gram_entry(x, y) for y in BAS] for x in BAS], dtype=complex)
check('Gram Hermitian', np.max(np.abs(G - G.conj().T)) < 1e-12)
check('Gram positive definite', np.min(np.linalg.eigvalsh(G)) > 1e-9, str(np.min(np.linalg.eigvalsh(G))))

# independent cross-check of the Gram by Taylor coefficients of Theta/u
def taylor_check():
    """<Theta/u, Theta/v> = (1/2pi) int conj(1/u) (1/v); expand 1/(w-a) = sum a^m w^{-(m+1)}."""
    out = np.zeros((6, 6), dtype=complex)
    M = 4000
    def coeffs(name):
        c = np.zeros(M, dtype=complex)     # coefficient of w^{-(m+1)}
        if name == 'g1':
            c[1] = 1.0                     # 1/w^2 = w^{-2}
        elif name == 'g2':
            c[0] = 1.0
        else:
            a = hw[int(name[1:])]
            c = a ** np.arange(M)
        return c
    for i, x in enumerate(BAS):
        for j, y in enumerate(BAS):
            out[i, j] = np.sum(np.conj(coeffs(x)) * coeffs(y))
    return out


check('Gram cross-check by Taylor series', np.max(np.abs(G - taylor_check())) < 1e-9,
      str(np.max(np.abs(G - taylor_check()))))

# Z and J in the basis
Zb = np.zeros((6, 6), dtype=complex)
Zb[1, 0] = 1.0                       # Z g1 = g2
for i in range(4):
    Zb[2 + i, 2 + i] = hw[i]
Jb = np.array([[0.0, 1.0, 1.0, 1.0, 1.0, 1.0]], dtype=complex)

L = np.linalg.cholesky(G)            # G = L L^*
def to_orth(M):
    return L.conj().T @ M @ np.linalg.inv(L.conj().T)


Z = to_orth(Zb)
J = Jb @ np.linalg.inv(L.conj().T)
check('J has rank 1 (h=1)', np.linalg.matrix_rank(J, tol=1e-9) == 1)
check('I - Z^*Z = J^*J', np.max(np.abs(np.eye(6) - Z.conj().T @ Z - J.conj().T @ J)) < 1e-9,
      str(np.max(np.abs(np.eye(6) - Z.conj().T @ Z - J.conj().T @ J))))
check('char poly of Z = Pc', np.max(np.abs(np.poly(Z) - Pc)) < 1e-9, str(np.max(np.abs(np.poly(Z) - Pc))))
Zp = np.linalg.matrix_power(Z, 200)
check('Z^m -> 0', np.linalg.norm(Zp) < 1e-9, str(np.linalg.norm(Zp)))
ev = np.linalg.eigvals(Z)
check('spec Z = {0,0} u HW', 
      sorted(np.round(np.abs(ev), 7).tolist()) == sorted(np.round(np.abs(roots_all), 7).tolist()))
sd = np.linalg.svd(Z, compute_uv=False)
check('D2 delay sector is one Jordan block of size two',
      (6 - np.linalg.matrix_rank(Z, tol=1e-8) == 1) and
      (6 - np.linalg.matrix_rank(Z @ Z, tol=1e-8) == 2) and
      (6 - np.linalg.matrix_rank(np.linalg.matrix_power(Z, 3), tol=1e-8) == 2))

# eigenvectors and exit amplitudes; the Gram identity
kvecs, zvals = [], []
for i in range(4):
    c = np.zeros(6, dtype=complex)
    c[2 + i] = 1.0                      # the basis vector Theta/(w - z_i)
    kvecs.append(L.conj().T @ c)
    zvals.append(hw[i])
check('four eigenvectors Theta/(w-a) of Z', len(zvals) == 4)
for i in range(4):
    check('Z k_a = z_a k_a (basis vector Theta/(w-a))',
          np.max(np.abs(Z @ kvecs[i] - zvals[i] * kvecs[i])) < 1e-9)
    check('a_n = J k_a = 1 in the Theta/(w-a) normalisation',
          abs((J @ kvecs[i])[0] - 1) < 1e-9, str((J @ kvecs[i])[0]))
for i in range(4):
    for j in range(4):
        lhs = (1 - np.conj(zvals[i]) * zvals[j]) * (kvecs[i].conj() @ kvecs[j])
        rhs = np.conj((J @ kvecs[i])[0]) * (J @ kvecs[j])[0]
        check('Gram identity (n,m)=(%d,%d)' % (i, j), abs(lhs - rhs) < 1e-8, '%s %s' % (lhs, rhs))

# normalised modal vectors and the modal Hasse-Weil reset
en = [k / np.linalg.norm(k) for k in kvecs]
delta = 1 - q ** -0.5
for i in range(4):
    check('||k_a||^2 = (1-|a|^2)^{-1}',
          abs(np.linalg.norm(kvecs[i]) ** 2 - 1 / (1 - abs(zvals[i]) ** 2)) < 1e-7,
          str(np.linalg.norm(kvecs[i]) ** 2))

# ------------------------------------------------------------ graded MPS (G3)
def build_network(Zm, Jm, Om, parity=None):
    """bond = C vac (+) K; letters A_0 = 1 (+) Z, A_(a,k) = sqrt(p_k)|om_k><j_a|."""
    n = Zm.shape[0]
    d = n + 1
    A = [np.block([[np.ones((1, 1)), np.zeros((1, n))], [np.zeros((n, 1)), Zm]])]
    pk, om = np.linalg.eigh(Om)
    h = Jm.shape[0]
    for a in range(h):
        ja = Jm.conj().T[:, a]
        for k in range(n):
            if pk[k] > 1e-13:
                v = np.zeros(d, dtype=complex)
                v[1:] = np.sqrt(pk[k]) * om[:, k]
                u = np.zeros(d, dtype=complex)
                u[1:] = ja
                A.append(np.outer(v, u.conj()))
    return A


def doubled(A):
    return sum(np.kron(a, a.conj()) for a in A)


def parity_op(dp, dm):
    return np.diag(np.concatenate([np.ones(dp), -np.ones(dm)]))


rng = np.random.default_rng(20260920)
Om_modal = sum(0.25 * np.outer(v, v.conj()) for v in en)
Xr = rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6))
Om_rand = Xr @ Xr.conj().T
Om_rand /= np.trace(Om_rand).real

for tag, Om in (('modal', Om_modal), ('random', Om_rand)):
    A = build_network(Z, J, Om)
    S = sum(a.conj().T @ a for a in A)
    check('%s: sum A_i^* A_i = 1' % tag, np.max(np.abs(S - np.eye(7))) < 1e-9,
          str(np.max(np.abs(S - np.eye(7)))))
    P = parity_op(1, 6)
    check('%s: every letter even' % tag, all(np.max(np.abs(P @ a @ P - a)) < 1e-12 for a in A))
    EE = doubled(A)
    PP = np.kron(P, P.conj())
    check('%s: EE commutes with P (x) Pbar' % tag, np.max(np.abs(PP @ EE - EE @ PP)) < 1e-9)
    # sector split
    ev_mask = np.diag(PP).real > 0
    od_mask = ~ev_mask
    check('%s: even/odd dims = 1+N^2, 2N' % tag,
          ev_mask.sum() == 1 + 36 and od_mask.sum() == 12, '%d %d' % (ev_mask.sum(), od_mask.sum()))
    E0 = EE[np.ix_(ev_mask, ev_mask)]
    E1 = EE[np.ix_(od_mask, od_mask)]
    check('%s: EE block diagonal in the sectors' % tag,
          np.max(np.abs(EE[np.ix_(ev_mask, od_mask)])) < 1e-12 and
          np.max(np.abs(EE[np.ix_(od_mask, ev_mask)])) < 1e-12)
    # E_Omega on B(K)
    EOm = np.zeros((36, 36), dtype=complex)
    for i in range(6):
        for j in range(6):
            E = np.zeros((6, 6), dtype=complex)
            E[i, j] = 1
            out = Z @ E @ Z.conj().T + np.trace(J @ E @ J.conj().T) * Om
            EOm[:, 6 * i + j] = out.reshape(-1)
    sp0 = np.sort_complex(np.linalg.eigvals(E0))
    sp1 = np.sort_complex(np.concatenate([[1.0], np.linalg.eigvals(EOm)]))
    def msd(a, b):
        a = list(a); b = list(b)
        worst = 0.0
        for x in a:
            k = min(range(len(b)), key=lambda t: abs(b[t] - x))
            worst = max(worst, abs(b[k] - x)); b.pop(k)
        return worst
    check('%s: spec E_0 = {1} u spec E_Omega' % tag, msd(np.linalg.eigvals(E0),
          np.concatenate([[1.0], np.linalg.eigvals(EOm)])) < 1e-7,
          str(msd(np.linalg.eigvals(E0), np.concatenate([[1.0], np.linalg.eigvals(EOm)]))))
    check('%s: spec E_1 = spec Z u conj spec Z' % tag,
          msd(np.linalg.eigvals(E1), np.concatenate([np.linalg.eigvals(Z), np.conj(np.linalg.eigvals(Z))])) < 1e-7,
          str(msd(np.linalg.eigvals(E1), np.concatenate([np.linalg.eigvals(Z), np.conj(np.linalg.eigvals(Z))]))))
    # (c) the two closures
    EEp = np.eye(49, dtype=complex)
    EOp = np.eye(36, dtype=complex)
    Zp_ = np.eye(6, dtype=complex)
    for Lc in range(1, 9):
        EEp = EEp @ EE
        EOp = EOp @ EOm
        Zp_ = Zp_ @ Z
        tr = np.trace(EEp)
        st = np.trace(PP @ EEp)
        check('%s: Tr EE^%d = 1 + Tr E_Om^L + 2Re Tr Z^L' % (tag, Lc),
              abs(tr - (1 + np.trace(EOp) + 2 * np.trace(Zp_).real)) < 1e-6,
              str(abs(tr - (1 + np.trace(EOp) + 2 * np.trace(Zp_).real))))
        check('%s: str EE^%d = 1 + Tr E_Om^L - 2Re Tr Z^L' % (tag, Lc),
              abs(st - (1 + np.trace(EOp) - 2 * np.trace(Zp_).real)) < 1e-6)
        check('%s: difference = 4 Re Tr Z^%d' % (tag, Lc),
              abs((tr - st) - 4 * np.trace(Zp_).real) < 1e-6)
    # explicit ring vectors
    for Lc in range(1, 5):
        tot = 0.0
        tot_p = 0.0
        for word in itertools.product(range(len(A)), repeat=Lc):
            M = np.eye(7, dtype=complex)
            for i in word:
                M = M @ A[i]
            tot += abs(np.trace(M)) ** 2
            tot_p += abs(np.trace(P @ M)) ** 2
        EEL = np.linalg.matrix_power(EE, Lc)
        check('%s: <psi_%d|psi_%d> = Tr EE^L' % (tag, Lc, Lc), abs(tot - np.trace(EEL).real) < 1e-7,
              '%s %s' % (tot, np.trace(EEL)))
        check('%s: <psi^P|psi^P> = str EE^L (L=%d)' % (tag, Lc),
              abs(tot_p - np.trace(PP @ EEL).real) < 1e-7, '%s %s' % (tot_p, np.trace(PP @ EEL)))
    # (d) ring zeta product formula and the divisor
    for uu in (0.13, 0.37 + 0.11j, -0.23):
        lhs = np.linalg.det(np.eye(12) - uu * E1) / np.linalg.det(np.eye(37) - uu * E0)
        zs = np.linalg.eigvals(Z)
        rhs = np.prod(1 - uu * zs) * np.prod(1 - uu * np.conj(zs)) / \
              ((1 - uu) * np.linalg.det(np.eye(36) - uu * EOm))
        check('%s: 1/sdet(1-u EE) product formula at u=%s' % (tag, uu),
              abs(lhs - rhs) < 1e-9 * max(1, abs(rhs)), '%s %s' % (lhs, rhs))
    def mult(vals, lam, tol=1e-7):
        return int(np.sum(np.abs(np.asarray(vals) - lam) < tol))
    e0v, e1v = np.linalg.eigvals(E0), np.linalg.eigvals(E1)
    check('%s: nu(1) = 2' % tag, mult(e0v, 1.0) - mult(e1v, 1.0) == 2,
          '%d %d' % (mult(e0v, 1.0), mult(e1v, 1.0)))
    for zz in zvals:
        check('%s: nu(z_n) = -2' % tag, mult(e0v, zz) - mult(e1v, zz) == -2,
              '%d %d' % (mult(e0v, zz), mult(e1v, zz)))
    nu0 = mult(e0v, 0.0) - mult(e1v, 0.0)
    check('%s: nu(0) > 0 (the delay value is NOT an odd divisor point, F8)' % tag, nu0 > 0, str(nu0))
    # (e) RH on the retained divisor
    odd_nonzero = [x for x in e1v if abs(x) > 1e-7]
    check('%s: every nonzero odd eigenvalue has modulus q^{-1/4}' % tag,
          max(abs(abs(x) - q ** -0.25) for x in odd_nonzero) < 1e-7,
          str(sorted(set(np.round(np.abs(e1v), 6)))))
    check('%s: the FULL odd spectrum has two moduli {0, q^{-1/4}} (F9)' % tag,
          len(set(np.round(np.abs(e1v), 6))) == 2)
    check('%s: exactly two even fixed points' % tag, mult(e0v, 1.0) == 2)

# ------------------------------------------ point counts of y^2+y = x^3+x+1 / F_2
def gf2k(k):
    """F_{2^k} as F_2[x]/(f) for a Conway-ish irreducible f; returns elements as int bitmasks."""
    POLY = {1: 0b10, 2: 0b111, 3: 0b1011, 4: 0b10011, 5: 0b100101, 6: 0b1000011}
    f = POLY[k]
    def mul(a, b):
        r = 0
        while b:
            if b & 1:
                r ^= a
            b >>= 1
            a <<= 1
            if a >> k & 1:
                a ^= f
        return r & ((1 << k) - 1)
    return list(range(1 << k)), mul


def count_points(k):
    els, mul = gf2k(k)
    n = 1                      # point at infinity
    for x in els:
        rhs = mul(mul(x, x), x) ^ x ^ 1        # x^3 + x + 1
        for y in els:
            if mul(y, y) ^ y == rhs:
                n += 1
    return n


Nk = [count_points(k) for k in range(1, 6)]
check('N_k = 1,5,13,25,41 by enumeration in F_{2^k}', Nk == [1, 5, 13, 25, 41], str(Nk))
ap, am = 1 - 1j, 1 + 1j
for k in range(1, 6):
    check('N_%d = 1 + q^k - (alpha_+^k + alpha_-^k)' % k,
          abs(Nk[k - 1] - (1 + 2 ** k - (ap ** k + am ** k))) < 1e-9)
    trZ = np.trace(np.linalg.matrix_power(Z, 2 * k))
    check('Tr Z^{2k} = 2 q^{-k}(alpha_+^k+alpha_-^k), k=%d' % k,
          abs(trZ - 2 * 2.0 ** (-k) * (ap ** k + am ** k)) < 1e-7, str(trZ))
    check('Tr Z^{2k} = 2 q^{-k}(1+q^k-N_k), k=%d' % k,
          abs(trZ - 2 * 2.0 ** (-k) * (1 + 2 ** k - Nk[k - 1])) < 1e-7)
for Lodd in (1, 3, 5, 7):
    check('Tr Z^%d = 0 (odd L)' % Lodd, abs(np.trace(np.linalg.matrix_power(Z, Lodd))) < 1e-9)



# ==================================================== thm:glued-graded-toy
# K_+ : APW's tree, one vertex, one funnel of weight q+1.  p_+ = z^2 - 1/q.
hwp = np.array([q ** -0.5, -q ** -0.5])
Pcp = np.poly(hwp)
Gp = np.array([[1.0 / (1 - np.conj(a) * b) for b in hwp] for a in hwp], dtype=complex)
Lp = np.linalg.cholesky(Gp)
Zpb = np.diag(hwp).astype(complex)
Jpb = np.array([[1.0, 1.0]], dtype=complex)
Zp2 = Lp.conj().T @ Zpb @ np.linalg.inv(Lp.conj().T)
Jp2 = Jpb @ np.linalg.inv(Lp.conj().T)
check('K_+ : p_+ = z^2 - 1/q', abs(Pcp[-1] + 1 / q) < 1e-12 and abs(Pcp[1]) < 1e-12)
check('K_+ : dim K_+ = 2 and spec Z_+ = {+-q^{-1/2}}',
      Zp2.shape == (2, 2) and np.max(np.abs(np.sort(np.linalg.eigvals(Zp2).real) - np.sort(hwp))) < 1e-9)
check('K_+ : I - Z^*Z = J^*J',
      np.max(np.abs(np.eye(2) - Zp2.conj().T @ Zp2 - Jp2.conj().T @ Jp2)) < 1e-9)
check('K_+ : R_+ = -(z^2-1/q)/(1-z^2/q) is inner',
      all(abs(abs((zz ** 2 - 1 / q) / (1 - zz ** 2 / q)) - 1) < 1e-10
          for zz in np.exp(1j * np.linspace(0, 2 * np.pi, 13))))
for Lc in range(1, 9):
    check('K_+ : Tr Z_+^%d = q^{-L/2}(1+(-1)^L)' % Lc,
          abs(np.trace(np.linalg.matrix_power(Zp2, Lc)) - q ** (-Lc / 2) * (1 + (-1) ** Lc)) < 1e-9)

# glued bond K = K_+ (+) K_-,  P = 1 (+) (-1)
dp, dm = 2, 6
Zg = np.block([[Zp2, np.zeros((2, 6))], [np.zeros((6, 2)), Z]])
Jg = np.block([[Jp2, np.zeros((1, 6))], [np.zeros((1, 2)), J]])     # one exit block per sector
Pg = parity_op(dp, dm)
check('glued: I - Z^*Z = J^*J', np.max(np.abs(np.eye(8) - Zg.conj().T @ Zg - Jg.conj().T @ Jg)) < 1e-9)
check('glued: Z even', np.max(np.abs(Pg @ Zg @ Pg - Zg)) < 1e-12)

Omp = np.zeros((2, 2), dtype=complex)
Omp[0, 0] = 0.6
Omp[1, 1] = 0.4
Omm = 0.25 * sum(np.outer(v, v.conj()) for v in en)
Omg = np.block([[0.4 * Omp, np.zeros((2, 6))], [np.zeros((6, 2)), 0.6 * Omm]])
check('glued: Omega even, Tr Om_+ > 0, Tr Om_- > 0',
      np.max(np.abs(Pg @ Omg @ Pg - Omg)) < 1e-12 and
      np.trace(Omg[:2, :2]).real > 0 and np.trace(Omg[2:, 2:]).real > 0)

pk, om = np.linalg.eigh(Omg)
Ag = [Zg]
pars = [1]
for a in range(2):
    ja = Jg.conj().T[:, a]
    for k in range(8):
        if pk[k] > 1e-13:
            Ag.append(np.sqrt(pk[k]) * np.outer(om[:, k], ja.conj()))
            eo = 1 if np.max(np.abs(om[2:, k])) < 1e-9 else -1        # parity of omega_k
            ej = 1 if np.max(np.abs(ja[2:])) < 1e-9 else -1
            pars.append(eo * ej)
check('glued: sum A_i^*A_i = 1', np.max(np.abs(sum(a.conj().T @ a for a in Ag) - np.eye(8))) < 1e-9)
homog = [np.max(np.abs(Pg @ a @ Pg - pars[i] * a)) < 1e-9 for i, a in enumerate(Ag)]
check('glued: every letter homogeneous of parity eps(om)eps(j)', all(homog), str(homog))
check('glued: cross letters (exit of one sector reset into the other) are odd', -1 in pars,
      str(pars))
check('glued: there IS at least one odd letter', pars.count(-1) > 0)

EEg = doubled(Ag)
PPg = np.kron(Pg, Pg.conj())
check('glued: EE commutes with the doubled parity', np.max(np.abs(PPg @ EEg - EEg @ PPg)) < 1e-9)
evg = np.linalg.eigvals(EEg)
check('glued: eigenvalue 1 of EE is simple (unique stationary density)',
      int(np.sum(np.abs(evg - 1) < 1e-7)) == 1, str(int(np.sum(np.abs(evg - 1) < 1e-7))))
# rho_inf
Rinf = sum(np.linalg.matrix_power(Zg, m) @ Omg @ np.linalg.matrix_power(Zg.conj().T, m)
           for m in range(400))
tbar = np.trace(Rinf).real
Rinf = Rinf / tbar
out = Zg @ Rinf @ Zg.conj().T + np.trace(Jg @ Rinf @ Jg.conj().T) * Omg
check('glued: rho_inf = tbar^{-1} sum Z^m Om Z^{*m} is stationary',
      np.max(np.abs(out - Rinf)) < 1e-9, str(np.max(np.abs(out - Rinf))))
check('glued: rho_inf even', np.max(np.abs(Pg @ Rinf @ Pg - Rinf)) < 1e-9)
check('glued: rho_inf mixed (both sectors populated)',
      np.trace(Rinf[:2, :2]).real > 1e-6 and np.trace(Rinf[2:, 2:]).real > 1e-6,
      '%g %g' % (np.trace(Rinf[:2, :2]).real, np.trace(Rinf[2:, 2:]).real))
check('glued: rho_inf >= tbar^{-1} Omega', np.min(np.linalg.eigvalsh(Rinf - Omg / tbar)) > -1e-9)
check('glued: rank rho_inf >= 2', np.linalg.matrix_rank(Rinf, tol=1e-8) >= 2,
      str(np.linalg.matrix_rank(Rinf, tol=1e-8)))
# odd sector
evm = np.diag(PPg).real > 0
odm = ~evm
E1g = EEg[np.ix_(odm, odm)]
E0g = EEg[np.ix_(evm, evm)]
check('glued: even/odd dims 2^2+6^2=40, 2*2*6=24', evm.sum() == 40 and odm.sum() == 24)
odd_pred = np.concatenate([np.outer(np.linalg.eigvals(Z), np.conj(np.linalg.eigvals(Zp2))).reshape(-1),
                           np.outer(np.linalg.eigvals(Zp2), np.conj(np.linalg.eigvals(Z))).reshape(-1)])
def msd2(a, b):
    a = list(np.asarray(a)); b = list(np.asarray(b))
    if len(a) != len(b):
        return float('inf')
    worst = 0.0
    for x in a:
        k = min(range(len(b)), key=lambda t: abs(b[t] - x))
        worst = max(worst, abs(b[k] - x)); b.pop(k)
    return worst
check('glued: odd spectrum = {z_n conj z_m} u {z_m conj z_n}',
      msd2(np.linalg.eigvals(E1g), odd_pred) < 1e-7, str(msd2(np.linalg.eigvals(E1g), odd_pred)))
mods = sorted(set(np.round(np.abs(np.linalg.eigvals(E1g)), 6)))
check('glued: odd moduli are {0, q^{-3/4}}',
      len(mods) == 2 and abs(mods[0]) < 1e-6 and abs(mods[1] - q ** -0.75) < 1e-6, str(mods))
# odd coherences are eigen-operators; <a_m,a_n> = 0 across blocks
for i in range(4):
    kn = np.concatenate([np.zeros(2), kvecs[i]])
    for jdx in range(2):
        c = np.zeros(2, dtype=complex); c[jdx] = 1.0
        km = np.concatenate([Lp.conj().T @ c, np.zeros(6)])
        X = np.outer(kn, km.conj())
        an = Jg @ kn
        am = Jg @ km
        check('glued: <a_m,a_n> = 0 across exit blocks', abs(am.conj() @ an) < 1e-12)
        EX = Zg @ X @ Zg.conj().T + np.trace(Jg @ X @ Jg.conj().T) * Omg
        lam = zvals[i] * np.conj(hwp[jdx])
        check('glued: |k_n><k_m| eigen-operator with eigenvalue z_n conj z_m',
              np.max(np.abs(EX - lam * X)) < 1e-9, str(np.max(np.abs(EX - lam * X))))
        check('glued: |z_n conj z_m| = r_+ r_- = q^{-3/4}', abs(abs(lam) - q ** -0.75) < 1e-9)
# twisted ring norm odd part
for Lc in range(1, 9):
    lhs = np.trace(PPg @ np.linalg.matrix_power(EEg, Lc)).real - \
          np.trace(np.linalg.matrix_power(E0g, Lc)).real
    rhs = -2 * (np.trace(np.linalg.matrix_power(Z, Lc)) *
                np.conj(np.trace(np.linalg.matrix_power(Zp2, Lc)))).real
    check('glued: str EE^%d - Tr E_0^L = -2Re[(Tr Z_-^L) conj(Tr Z_+^L)]' % Lc,
          abs(lhs - rhs) < 1e-6, '%s %s' % (lhs, rhs))

# ------------------------------------- lem:even-letters-two-fixed-points
# (iii) sector-preserving reset: all letters even, two stationary densities
Omp2 = np.block([[Omp, np.zeros((2, 6))], [np.zeros((6, 2)), np.zeros((6, 6))]])
Omm2 = np.block([[np.zeros((2, 2)), np.zeros((2, 6))], [np.zeros((6, 2)), Omm]])
def sector_channel(X):
    return Zg @ X @ Zg.conj().T + np.trace(Jg[:, :2] @ X[:2, :2] @ Jg[:, :2].conj().T) * Omp2 + \
        np.trace(Jg[:, 2:] @ X[2:, 2:] @ Jg[:, 2:].conj().T) * Omm2
Msec = np.zeros((64, 64), dtype=complex)
for i in range(8):
    for jj in range(8):
        E = np.zeros((8, 8), dtype=complex); E[i, jj] = 1
        Msec[:, 8 * i + jj] = sector_channel(E).reshape(-1)
evs = np.linalg.eigvals(Msec)
check('sector-preserving reset: eigenvalue 1 has multiplicity 2 (segment)',
      int(np.sum(np.abs(evs - 1) < 1e-7)) == 2, str(int(np.sum(np.abs(evs - 1) < 1e-7))))

# general lemma on random even-letter channels
for t in range(6):
    dpp, dmm = int(rng.integers(1, 4)), int(rng.integers(1, 4))
    d = dpp + dmm
    ks = []
    for _ in range(3):
        Xp_ = rng.normal(size=(dpp, dpp)) + 1j * rng.normal(size=(dpp, dpp))
        Xm_ = rng.normal(size=(dmm, dmm)) + 1j * rng.normal(size=(dmm, dmm))
        ks.append(np.block([[Xp_, np.zeros((dpp, dmm))], [np.zeros((dmm, dpp)), Xm_]]))
    S = sum(k.conj().T @ k for k in ks)
    Sinv = np.linalg.inv(np.linalg.cholesky(S).conj().T)
    ks = [k @ Sinv.conj().T for k in ks]
    ks = [k @ np.linalg.inv(np.linalg.cholesky(sum(a.conj().T @ a for a in ks)).conj().T) for k in ks]
    S2 = sum(k.conj().T @ k for k in ks)
    if np.max(np.abs(S2 - np.eye(d))) > 1e-8:
        continue
    Pt = parity_op(dpp, dmm)
    check('random even-letter channel %d: letters even' % t,
          all(np.max(np.abs(Pt @ k @ Pt - k)) < 1e-9 for k in ks))
    M = sum(np.kron(k, k.conj()) for k in ks)
    ev2 = np.linalg.eigvals(M)
    check('random even-letter channel %d: eigenvalue 1 has multiplicity >= 2' % t,
          int(np.sum(np.abs(ev2 - 1) < 1e-7)) >= 2, str(int(np.sum(np.abs(ev2 - 1) < 1e-7))))

# the unstated step: a channel commuting with Ad(P) HAS a homogeneous Kraus representation
for t in range(5):
    dpp, dmm = 2, 3
    d = 5
    Pt = parity_op(dpp, dmm)
    ks = []
    for _ in range(4):
        X = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        # deliberately NON-homogeneous letters, but symmetrised so the channel commutes with Ad(P)
        ks.append(X)
    ks = ks + [Pt @ k @ Pt for k in ks]
    Snorm = sum(k.conj().T @ k for k in ks)
    R = np.linalg.cholesky(Snorm).conj().T
    ks = [k @ np.linalg.inv(R) for k in ks]
    chan = sum(np.kron(k, k.conj()) for k in ks)
    PPt = np.kron(Pt, Pt.conj())
    check('constructed channel %d commutes with Ad(P)' % t,
          np.max(np.abs(PPt @ chan - chan @ PPt)) < 1e-8)
    nonhom = sum(1 for k in ks if min(np.max(np.abs(Pt @ k @ Pt - k)),
                                      np.max(np.abs(Pt @ k @ Pt + k))) > 1e-8)
    check('channel %d: the given letters are NOT homogeneous' % t, nonhom > 0)
    # Choi matrix and its diagonalisation inside the P (x) P eigenspaces
    Choi = np.zeros((d * d, d * d), dtype=complex)
    for i in range(d):
        for jj in range(d):
            E = np.zeros((d, d), dtype=complex); E[i, jj] = 1
            out = sum(k @ E @ k.conj().T for k in ks)
            Choi[np.ix_(range(i * d, (i + 1) * d), range(jj * d, (jj + 1) * d))] = out
    Pd = np.kron(Pt, Pt)
    check('channel %d: Choi commutes with P (x) P' % t,
          np.max(np.abs(Pd @ Choi @ Pd - Choi)) < 1e-8, str(np.max(np.abs(Pd @ Choi @ Pd - Choi))))
    evc, vc = np.linalg.eigh(Choi)
    newk = []
    for i in range(d * d):
        if evc[i] > 1e-9:
            Amat = np.sqrt(evc[i]) * vc[:, i].reshape(d, d).T
            newk.append(Amat)
    check('channel %d: reconstructed Kraus set reproduces the channel' % t,
          np.max(np.abs(sum(np.kron(a, a.conj()) for a in newk) - chan)) < 1e-7)
    check('channel %d: every reconstructed letter is homogeneous' % t,
          all(min(np.max(np.abs(Pt @ a @ Pt - a)), np.max(np.abs(Pt @ a @ Pt + a))) < 1e-7
              for a in newk),
          str([min(np.max(np.abs(Pt @ a @ Pt - a)), np.max(np.abs(Pt @ a @ Pt + a))) for a in newk]))

# ------------------------------------------ prop:shared-exit-tradeoff
# random three-vertex core, ONE shared cusp: six distinct nonzero resonances
def model_from_roots(rts):
    n = len(rts)
    Gm = np.array([[1.0 / (1 - np.conj(a) * b) for b in rts] for a in rts], dtype=complex)
    Lm = np.linalg.cholesky(Gm)
    Zm = Lm.conj().T @ np.diag(rts) @ np.linalg.inv(Lm.conj().T)
    Jm = np.ones((1, n), dtype=complex) @ np.linalg.inv(Lm.conj().T)
    return Zm, Jm, Lm


# take six distinct resonances of a random real core with one cusp
found = None
for _ in range(200):
    T3 = rng.normal(size=(3, 3)) * 0.8
    T3 = (T3 + T3.T) / 2
    c2 = float(rng.uniform(0.3, 0.9))
    C3m = np.diag([c2, 0.0, 0.0])
    coeffs = np.poly(np.zeros(0))
    zz = sp.Symbol('zz')
    Mz = (1 + zz ** 2) * sp.eye(3) - zz * sp.Matrix(T3.tolist()) - sp.Matrix(C3m.tolist())
    pp = sp.Poly(sp.expand(Mz.det()), zz)
    cf = [complex(pp.as_expr().coeff(zz, k)) for k in range(6, -1, -1)]
    rr = np.roots(cf)
    inside = rr[np.abs(rr) < 1 - 1e-6]
    if len(inside) == 6 and np.min([abs(a - b) for i, a in enumerate(inside)
                                    for b in inside[i + 1:]]) > 1e-3:
        found = (T3, c2, inside)
        break
check('found a random 3-vertex core with six interior resonances', found is not None)
T3, c2, rts = found
Zs, Js, Ls = model_from_roots(rts)
check('shared exit: I - Z^*Z = J^*J',
      np.max(np.abs(np.eye(6) - Zs.conj().T @ Zs - Js.conj().T @ Js)) < 1e-8,
      str(np.max(np.abs(np.eye(6) - Zs.conj().T @ Zs - Js.conj().T @ Js))))
Xs = rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6))
Oms = Xs @ Xs.conj().T
Oms /= np.trace(Oms).real
for i in range(6):
    for jdx in range(6):
        ci = np.zeros(6, dtype=complex); ci[i] = 1
        cj = np.zeros(6, dtype=complex); cj[jdx] = 1
        kn = Ls.conj().T @ ci
        km = Ls.conj().T @ cj
        an, am = (Js @ kn)[0], (Js @ km)[0]
        check('shared exit: a_n = 1 for every mode', abs(an - 1) < 1e-8)
        lhs = np.conj(am) * an
        rhs = (1 - np.conj(rts[jdx]) * rts[i]) * (km.conj() @ kn)
        check('shared exit: <a_m,a_n> = (1-conj(z_m)z_n)<k_m,k_n> (%d,%d)' % (i, jdx),
              abs(lhs - rhs) < 1e-8, '%s %s' % (lhs, rhs))
        X = np.outer(kn, km.conj())
        EX = Zs @ X @ Zs.conj().T + np.trace(Js @ X @ Js.conj().T) * Oms
        res = EX - rts[i] * np.conj(rts[jdx]) * X
        check('shared exit: residue = <a_m,a_n> Omega (%d,%d)' % (i, jdx),
              np.max(np.abs(res - lhs * Oms)) < 1e-8, str(np.max(np.abs(res - lhs * Oms))))
# multiplicity bookkeeping
Ad = np.kron(Zs, Zs.conj())
Msh = Ad + np.outer(Oms.reshape(-1), (Js.conj().T @ Js).reshape(-1).conj())
ev0 = np.linalg.eigvals(Ad)
ev1 = np.linalg.eigvals(Msh)
for i in range(6):
    for jdx in range(6):
        lam = rts[i] * np.conj(rts[jdx])
        m0 = int(np.sum(np.abs(ev0 - lam) < 1e-6))
        m1 = int(np.sum(np.abs(ev1 - lam) < 1e-6))
        check('shared exit: multiplicity drops by exactly one at z_n conj z_m',
              m1 == m0 - 1, '%d -> %d' % (m0, m1))
        break
    break

# ---- ATTACK: the persistence criterion in the DEGENERATE case
# Ad(Z) with Z = diag(z1,z2,z3,z4) chosen so z1 conj z2 = z3 conj z4 (a degenerate value),
# and Omega chosen so that the SUM of the two residues vanishes while each is nonzero.
zA = 0.6
zB = 0.5 * np.exp(1j * 0.7)
zC = 0.75
zD = 0.4 * np.exp(1j * 0.7)
Zd = np.diag([zA, zB, zC, zD]).astype(complex)
lam = zA * np.conj(zB)
check('degenerate probe: z1 conj z2 = z3 conj z4', abs(zA * np.conj(zB) - zC * np.conj(zD)) < 1e-12,
      '%s %s' % (zA * np.conj(zB), zC * np.conj(zD)))
check('degenerate probe: lam has Ad(Z)-multiplicity exactly two',
      int(np.sum(np.abs(np.linalg.eigvals(np.kron(Zd, Zd.conj())) - zA * np.conj(zB)) < 1e-7)) == 2,
      str(int(np.sum(np.abs(np.linalg.eigvals(np.kron(Zd, Zd.conj())) - zA * np.conj(zB)) < 1e-7))))
fvec = np.ones(4, dtype=complex) / 2.0
fl = np.outer(fvec, fvec.conj())      # flux functional X -> <f|X|f> = Tr(F^* X), F = |f><f|
Add = np.kron(Zd, Zd.conj())
# eigen-operators X_1 = |e1><e2|, X_2 = |e3><e4|; duals the same (Z diagonal, orthonormal)
X1 = np.zeros((4, 4), dtype=complex); X1[0, 1] = 1
X2 = np.zeros((4, 4), dtype=complex); X2[2, 3] = 1
# choose Omega with Omega_{21} = t, Omega_{43} = s  (dual_X(Omega) = <l_n|Omega|l_m> = Omega_{nm}?)
def perturbed(Om, F):
    # E(X) = Z X Z^* + <f|X|f> Omega  (a rank-one perturbation of Ad(Z))
    M = np.kron(Zd, Zd.conj()).astype(complex)
    for i in range(4):
        for jj in range(4):
            E = np.zeros((4, 4), dtype=complex); E[i, jj] = 1
            M[:, 4 * i + jj] += (fvec.conj() @ E @ fvec) * Om.reshape(-1)
    return M
base = np.diag([0.25, 0.25, 0.25, 0.25]).astype(complex)
t = 0.03
Om1 = base.copy(); Om1[0, 1] = t; Om1[1, 0] = t
Om2 = base.copy(); Om2[2, 3] = -t; Om2[3, 2] = -t
Omboth = base.copy()
Omboth[0, 1] = t; Omboth[1, 0] = t
Omboth[2, 3] = -t; Omboth[3, 2] = -t
for nm, Om in (('only pair 1 charged', Om1), ('only pair 2 charged', Om2),
               ('both charged with opposite signs', Omboth)):
    check('%s: Omega is a density' % nm, np.min(np.linalg.eigvalsh(Om)) > -1e-12 and
          abs(np.trace(Om).real - 1) < 1e-12)
    Mp = perturbed(Om, fl)
    m0 = int(np.sum(np.abs(np.linalg.eigvals(Add) - lam) < 1e-7))
    m1 = int(np.sum(np.abs(np.linalg.eigvals(Mp) - lam) < 1e-7))
    if nm == 'both charged with opposite signs':
        check('DEGENERATE CASE: each dual_X(Omega) != 0 yet multiplicity does NOT drop',
              m0 == 2 and m1 == 2, '%d -> %d' % (m0, m1))
    else:
        check('%s: multiplicity drops by one' % nm, m1 == m0 - 1, '%d -> %d' % (m0, m1))
check('degenerate probe: both individual residues nonzero in the cancelling case',
      abs(Omboth[0, 1]) > 1e-9 and abs(Omboth[2, 3]) > 1e-9)
check('degenerate probe: the SUM of the two residues vanishes',
      abs(np.conj(fvec[0]) * fvec[1] * Omboth[0, 1] +
          np.conj(fvec[2]) * fvec[3] * Omboth[2, 3]) < 1e-14)
# the same degeneracy is present on D2 itself: with the quartet {a,-a,abar,-abar},
# z_1 conj z_2 = a conj(-a) = -|a|^2 = abar conj(-abar) = z_3 conj z_4
aa = hw[0]
quart = [aa, -aa, np.conj(aa), -np.conj(aa)]
check('D2: the value -|a|^2 is carried by two distinct odd coherences',
      abs(quart[0] * np.conj(quart[1]) - np.conj(aa) * np.conj(-np.conj(aa))) < 1e-12 or
      abs(quart[0] * np.conj(quart[1]) - quart[2] * np.conj(quart[3])) < 1e-12,
      '%s %s' % (quart[0] * np.conj(quart[1]), quart[2] * np.conj(quart[3])))
check('D2: Ad(Z) on K_HW has -q^{-1/2} with multiplicity >= 2',
      int(np.sum(np.abs(np.linalg.eigvals(np.kron(np.diag(quart), np.conj(np.diag(quart)))) +
                        q ** -0.5) < 1e-8)) >= 2,
      str(int(np.sum(np.abs(np.linalg.eigvals(np.kron(np.diag(quart), np.conj(np.diag(quart)))) +
                            q ** -0.5) < 1e-8))))

# glued toy: peripheral spectrum / aperiodicity and attraction
peri = [x for x in np.linalg.eigvals(EEg) if abs(abs(x) - 1) < 1e-7]
check('glued instance: the only peripheral eigenvalue is 1 (aperiodic, attracting)',
      len(peri) == 1 and abs(peri[0] - 1) < 1e-7, str(peri))
mm = [float(np.trace(Jg @ np.linalg.matrix_power(Zg, m - 1) @ Omg @
                     np.linalg.matrix_power(Zg.conj().T, m - 1) @ Jg.conj().T).real)
      for m in range(1, 400)]
check('glued instance: holding law is a probability law', abs(sum(mm) - 1) < 1e-6, str(sum(mm)))
supp = [m + 1 for m, v in enumerate(mm) if v > 1e-12]
from math import gcd as _gcd
g_ = 0
for m in supp:
    g_ = _gcd(g_, m)
check('glued instance: holding law aperiodic (gcd of its support is 1)', g_ == 1, str((g_, supp[:6])))
check('glued instance: tbar finite', tbar < 1e6 and tbar > 0, str(tbar))

print("\nscratch_gt_net: %d passed, %d failed" % (PASS[0], len(FAIL)))
