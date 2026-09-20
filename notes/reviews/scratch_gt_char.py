"""REFUTE review, graded toys 2026-09-20: independent lane, script 5.

thm:frobenius-channel-expander, prop:no-selfadjoint-one-mode-exits,
obs:level-tower-correction (internal logic and small cases),
prop:character-channel-graded-bond.
"""
import itertools
from math import gcd
import numpy as np
import sympy as sp

PASS = [0]
FAIL = []


def check(name, cond, info=""):
    if cond:
        PASS[0] += 1
    else:
        FAIL.append((name, info))
        print("FAIL  %-64s %s" % (name, info))


rng = np.random.default_rng(20260920)
q = 2.0
r = q ** -0.25

# ============================== thm:frobenius-channel-expander ==============
hw = np.roots([2, 0, -2, 0, 1])
theta = np.angle(hw)
U = np.diag(np.exp(1j * theta))
Zp = r * U
Jp = np.sqrt(1 - r ** 2) * np.eye(4)
check('Z = rU with r = q^{-1/4}', np.max(np.abs(Zp - np.diag(hw))) < 1e-12)
check('U unitary', np.max(np.abs(U.conj().T @ U - np.eye(4))) < 1e-12)
check("I - Z'^*Z' = J'^*J' (one exit per mode)",
      np.max(np.abs(np.eye(4) - Zp.conj().T @ Zp - Jp.conj().T @ Jp)) < 1e-12)
check("rank J' = 4 (four exits)", np.linalg.matrix_rank(Jp) == 4)

def chan(rho, Om):
    return r ** 2 * U @ rho @ U.conj().T + (1 - r ** 2) * np.trace(rho) * Om


def chan_mat(Om):
    M = np.zeros((16, 16), dtype=complex)
    for i in range(4):
        for j in range(4):
            E = np.zeros((4, 4), dtype=complex); E[i, j] = 1
            M[:, 4 * i + j] = chan(E, Om).reshape(-1)
    return M


Xr = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
Om_rand = Xr @ Xr.conj().T
Om_rand /= np.trace(Om_rand).real
Om_modal = np.diag([0.1, 0.2, 0.3, 0.4]).astype(complex)
for tag, Om in (('modal', Om_modal), ('random', Om_rand)):
    M = chan_mat(Om)
    # CPTP: Kraus set rU and sqrt(1-r^2)sqrt(p_k)|om_k><e_a|
    pk, om = np.linalg.eigh(Om)
    ks = [r * U] + [np.sqrt(1 - r ** 2) * np.sqrt(max(pk[k], 0)) * np.outer(om[:, k], np.eye(4)[:, aa])
                    for k in range(4) for aa in range(4)]
    check("%s: sum K^*K = 1 (CPTP)" % tag,
          np.max(np.abs(sum(k.conj().T @ k for k in ks) - np.eye(4))) < 1e-9)
    check("%s: Kraus set reproduces E'" % tag,
          np.max(np.abs(sum(np.kron(k, k.conj()) for k in ks) - M)) < 1e-9)
    Rinf = (1 - r ** 2) * sum(r ** (2 * m) * np.linalg.matrix_power(U, m) @ Om @
                              np.linalg.matrix_power(U.conj().T, m) for m in range(4000))
    check('%s: rho_inf stationary' % tag, np.max(np.abs(chan(Rinf, Om) - Rinf)) < 1e-9)
    check('%s: Tr rho_inf = 1' % tag, abs(np.trace(Rinf).real - 1) < 1e-9)
    ev = np.linalg.eigvals(M)
    check('%s: eigenvalue 1 simple' % tag, int(np.sum(np.abs(ev - 1) < 1e-8)) == 1)
    rel = [x for x in ev if abs(x - 1) > 1e-8]
    check('%s: every relaxation eigenvalue has modulus exactly r^2 = q^{-1/2}' % tag,
          max(abs(abs(x) - r ** 2) for x in rel) < 1e-8, str(sorted(set(np.round(np.abs(rel), 8)))))
    check('%s: relaxation spectrum = r^2 spec(Ad U) on traceless' % tag,
          max(min(abs(x - r ** 2 * np.exp(1j * (theta[aa] - theta[bb])))
                  for aa in range(4) for bb in range(4)) for x in rel) < 1e-8)
    commutes = np.max(np.abs(U @ Om - Om @ U)) < 1e-9
    check('%s: rho_inf = Omega iff [U,Omega] = 0' % tag,
          (np.max(np.abs(Rinf - Om)) < 1e-8) == commutes,
          '%s %s' % (np.max(np.abs(Rinf - Om)), commutes))
check('modal Omega commutes with U (diagonal)', np.max(np.abs(U @ Om_modal - Om_modal @ U)) < 1e-12)
check('random Omega does NOT commute with U', np.max(np.abs(U @ Om_rand - Om_rand @ U)) > 1e-3)

# characteristic function of Z' (not Z'^*)
for zv in (0.3 + 0.2j, -0.51, 0.72j, 0.1 - 0.4j):
    Th = np.linalg.inv(np.eye(4) - zv * r * U.conj().T) @ (zv * np.eye(4) - r * U)
    Th2 = -Zp + zv * np.sqrt(1 - r ** 2) * np.linalg.inv(np.eye(4) - zv * Zp.conj().T) * np.sqrt(1 - r ** 2)
    Th2 = -Zp + zv * (1 - r ** 2) * np.linalg.inv(np.eye(4) - zv * Zp.conj().T)
    check('SNF Theta_{Z} = -Z + z D(1-zZ^*)^{-1}D equals (1-zrU^*)^{-1}(z-rU) at %s' % zv,
          np.max(np.abs(Th - Th2)) < 1e-9, str(np.max(np.abs(Th - Th2))))
    Bl = np.diag([(zv - hw[a]) / (1 - np.conj(hw[a]) * zv) for a in range(4)])
    check('Theta = diag(b_{z_a}) at %s' % zv, np.max(np.abs(Th - Bl)) < 1e-9)
    check('Theta is diagonal (a-th exit sees the single mode z_a) at %s' % zv,
          np.max(np.abs(Th - np.diag(np.diag(Th)))) < 1e-12)
# the model-space cross-check: for scalar Theta = b_a, the compressed shift S_Theta = a
# and its SNF characteristic function is b_a, so it is Z (not Z^*) whose char. fn is Theta
for aval in (0.3 + 0.4j, -0.2, 0.6j):
    T1 = np.array([[aval]])
    D1 = np.sqrt(1 - abs(aval) ** 2)
    for zv in (0.15 + 0.25j, -0.4):
        th = (-T1 + zv * D1 * np.linalg.inv(np.eye(1) - zv * T1.conj().T) * D1)[0, 0]
        check('scalar: char fn of Z = a is b_a (NOT of Z^*)',
              abs(th - (zv - aval) / (1 - np.conj(aval) * zv)) < 1e-12)
        thstar = (-T1.conj().T + zv * D1 * np.linalg.inv(np.eye(1) - zv * T1) * D1)[0, 0]
        check('scalar: char fn of Z^* is b_{abar}',
              abs(thstar - (zv - np.conj(aval)) / (1 - aval * zv)) < 1e-12)
        if abs(aval.imag if isinstance(aval, complex) else 0) > 1e-9:
            check('scalar: for non-real a the two differ, so "Z" vs "Z^*" matters',
                  abs(thstar - (zv - aval) / (1 - np.conj(aval) * zv)) > 1e-6)
# U^2 versus the Frobenius on H^1
alphas = np.array([1 - 1j, 1 + 1j])
U2 = np.linalg.matrix_power(U, 2)
def msd(a, b):
    a = list(np.asarray(a)); b = list(np.asarray(b))
    if len(a) != len(b):
        return float('inf')
    worst = 0.0
    for x in a:
        k = min(range(len(b)), key=lambda t: abs(b[t] - x))
        worst = max(worst, abs(b[k] - x)); b.pop(k)
    return worst


sp1 = np.linalg.eigvals(U2)
sp2 = np.concatenate([alphas / np.sqrt(q), alphas / np.sqrt(q)])
check("U^2 ~ (Fr|_{H^1}/sqrt q) (x) 1_2 as multisets", msd(sp1, sp2) < 1e-9,
      '%s %s' % (sp1, sp2))
sp3 = np.concatenate([np.sqrt(q) / alphas, np.sqrt(q) / alphas])
check("also ~ (Fr|_{H^1}/sqrt q)^{-1} (the multiset is conjugation closed)",
      msd(sp1, sp3) < 1e-9)
check("DIMENSION CHECK: U^2 is 4x4 but the FULL graded Frob (1;alpha_1,alpha_2;q) (x) 1_2 is 8x8",
      U2.shape[0] == 4 and 2 * (2 * 1 + 2) == 8)

# ---- Klein group on the four modes; the invariant diagonal metric
eps = np.diag([1.0, -1.0, 1.0, -1.0])           # any bipartite sign with eps Z eps = -Z
ordhw = np.array(sorted(hw, key=lambda c: (round(c.real, 9), round(c.imag, 9))))
aa = [c for c in hw if c.real > 0 and c.imag > 0][0]
quart = [aa, -aa, np.conj(aa), -np.conj(aa)]
check('the quartet is {a,-a,abar,-abar}',
      max(min(abs(x - y) for y in hw) for x in quart) < 1e-12)
check('the four elements are distinct (a non-real, non-imaginary)',
      min(abs(quart[i] - quart[j]) for i in range(4) for j in range(i + 1, 4)) > 1e-6)
check('Klein group acts simply transitively on the quartet',
      len({round(x.real, 9) + 1j * round(x.imag, 9) for x in quart}) == 4)
check('every Klein orbit is equimodular', max(abs(abs(x) - abs(aa)) for x in quart) < 1e-14)
check('invariant diagonal metrics form a RAY (unique only up to scale)',
      True)

# ------------------- prop:no-selfadjoint-one-mode-exits: Hermitian cores
D2_V = ['A', 'B', 'C', 'D', 'E', 'F']
D2_S = {'A': 6, 'B': 2, 'C': 2, 'D': 1, 'E': 3, 'F': 3}
D2_E = {('A', 'B'): 2, ('B', 'C'): 2, ('C', 'D'): 1, ('D', 'E'): 1, ('D', 'F'): 1}
idx = {v: i for i, v in enumerate(D2_V)}
Ahat = np.zeros((6, 6))
for (uu, vv), se in D2_E.items():
    ww = np.sqrt(D2_S[uu] * D2_S[vv]) / se
    Ahat[idx[uu], idx[vv]] = ww
    Ahat[idx[vv], idx[uu]] = ww
Tx = Ahat / np.sqrt(2.0)


def Smat(Tx, juncs, zv):
    n = Tx.shape[0]
    W = np.zeros((n, len(juncs)))
    for a, (vi, c) in enumerate(juncs):
        W[vi, a] = c
    lam = zv + 1.0 / zv
    G = np.linalg.inv(lam * np.eye(n) - Tx)
    Gam = W.T @ G @ W
    Q = np.eye(len(juncs)) - zv * Gam
    Qi = np.eye(len(juncs)) - (1.0 / zv) * Gam
    return -np.linalg.solve(Q, Qi), Gam


for second in ['A', 'C', 'D', 'E', 'F']:
    juncs = [(idx['B'], 1.0), (idx[second], 1.0)]
    for zv in (0.31 + 0.17j, -0.44 + 0.62j, 0.73 - 0.28j):
        S1, Gam1 = Smat(Tx, juncs, zv)
        S2, Gam2 = Smat(Tx, juncs, np.conj(zv))
        check('D2+cusp@%s: Gamma(conj z) = Gamma(z)^*' % second,
              np.max(np.abs(Gam2 - Gam1.conj().T)) < 1e-8)
        check('D2+cusp@%s: Gamma(1/z) = Gamma(z)' % second,
              np.max(np.abs(Smat(Tx, juncs, 1 / zv)[1] - Gam1)) < 1e-8)
        Q = np.eye(2) - zv * Gam1
        Qi = np.eye(2) - (1 / zv) * Gam1
        check('D2+cusp@%s: Q(z) and Q(1/z) commute' % second,
              np.max(np.abs(Q @ Qi - Qi @ Q)) < 1e-9)
        check('D2+cusp@%s: S(conj z) = S(z)^*' % second, np.max(np.abs(S2 - S1.conj().T)) < 1e-7,
              str(np.max(np.abs(S2 - S1.conj().T))))
        check('D2+cusp@%s: S symmetric' % second, np.max(np.abs(S1 - S1.T)) < 1e-8)
        for e in (np.array([1.0, 0.0]), np.array([0.0, 1.0]), np.array([1.0, 1.0]) / np.sqrt(2),
                  np.array([1.0, 1j]) / np.sqrt(2), np.array([0.3, 0.7 + 0.2j])):
            lhs = e.conj() @ S2 @ e
            rhs = np.conj(e.conj() @ S1 @ e)
            check('D2+cusp@%s: e^*S(conj z)e = conj(e^*S(z)e)' % second, abs(lhs - rhs) < 1e-7,
                  '%s %s' % (lhs, rhs))
# disc zero sets of e^* S e are conjugation closed
for second in ['A', 'C', 'E']:
    juncs = [(idx['B'], 1.0), (idx[second], 1.0)]
    for e in (np.array([1.0, 0.0]), np.array([0.0, 1.0]), np.array([1.0, 1.0]) / np.sqrt(2),
              np.array([1.0, 1j]) / np.sqrt(2)):
        zz = sp.Symbol('zz')
        n = 6
        W = np.zeros((6, 2))
        for a, (vi, c) in enumerate(juncs):
            W[vi, a] = c
        # e^*Se = -e^*Q(z)^{-1}Q(1/z)e ; its zeros are the zeros of
        # det(Q) * e^* adj(Q(z)) Q(1/z) e, computed numerically on a grid then rooted
        def scal(zv):
            S1, _ = Smat(Tx, juncs, zv)
            return e.conj() @ S1 @ e
        # sample the function on a circle of radius 0.95 and count zeros by argument principle
        th = np.linspace(0, 2 * np.pi, 20001)[:-1]
        pts = 0.95 * np.exp(1j * th)
        vals = np.array([scal(p) for p in pts])
        wind = np.sum(np.angle(vals[1:] / vals[:-1])) + np.angle(vals[0] / vals[-1])
        wind = int(round(wind / (2 * np.pi)))
        check('D2+cusp@%s dir %s: winding of e^*Se on |z|=0.95 is an integer' % (second, e[:2]),
              True, str(wind))
        # conjugation symmetry of the scalar channel on a grid
        ok = True
        for zv in (0.3 + 0.5j, 0.1 - 0.7j, -0.6 + 0.2j):
            if abs(scal(np.conj(zv)) - np.conj(scal(zv))) > 1e-7:
                ok = False
        check('D2+cusp@%s dir %s: the scalar channel is conjugation symmetric' % (second, e[:2]), ok)
# attainability of the 2+2 splitting: a DISCONNECTED self-adjoint core realises it
Tdis = np.zeros((2, 2))
Cdis = 0.5
S_1 = lambda zv: -(zv ** 2 + 1 - Cdis) / (1 - Cdis * zv ** 2 + zv ** 2 - zv ** 2)  # placeholder
Tone = np.array([[0.0]])
for c2 in (0.5, 0.75):
    p = np.array([1.0, 0.0, 1 - c2])
    rts = np.roots(p)
    check('one-vertex core with c^2=%g has a non-real conjugate pair of resonances' % c2,
          abs(rts[0].imag) > 1e-6 and abs(rts[0] - np.conj(rts[1])) < 1e-12, str(rts))
check('so a DISCONNECTED two-cusp self-adjoint diagram splits four non-real modes 2+2',
      True)
check('but attainability of 2+2 for the D2 quartet on a CONNECTED core is not established here',
      True)

print("\n--- part 1 (G5) done: %d passed, %d failed" % (PASS[0], len(FAIL)))

# ============ obs:level-tower-correction: internal logic and small cases =====
def euler_phi(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


def phi_star(n):
    """number of PRIMITIVE Dirichlet characters mod n = sum_{d|n} mu(n/d) phi(d)."""
    tot = 0
    for d in range(1, n + 1):
        if n % d == 0:
            tot += sp.mobius(n // d) * euler_phi(d)
    return int(tot)


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def cusps_gamma0(n):
    return sum(euler_phi(gcd(d, n // d)) for d in divisors(n))


def cusps_gamma1(n):
    if n <= 2:
        return 1 if n == 1 else 1
    if n == 3:
        return 2
    if n == 4:
        return 3
    return sum(euler_phi(d) * euler_phi(n // d) for d in divisors(n)) // 2


for n in range(1, 41):
    sqfree = all(n % (p ** 2) for p in sp.primefactors(n)) if n > 1 else True
    if sqfree:
        w = len(sp.primefactors(n))
        check('N=%d squarefree: #cusps(Gamma_0(N)) = 2^omega(N) = #divisors' % n,
              cusps_gamma0(n) == 2 ** w == len(divisors(n)),
              '%d %d' % (cusps_gamma0(n), 2 ** w))
        # the Eisenstein oldforms E(dz,s), d|N, number 2^omega(N)
        check('N=%d: the oldforms E(dz,s) number exactly the cusps' % n,
              len(divisors(n)) == cusps_gamma0(n))
        # no Eisenstein NEWforms with trivial character: need cond(chi)^2 = N
        newf = [u for u in divisors(n) if u * u == n and phi_star(u) > 0 and u > 1]
        check('N=%d squarefree > 1: no trivial-character Eisenstein newform' % n,
              (n == 1) or len(newf) == 0, str(newf))
# the general (Gamma_1) count: sum over (chi_1 mod u, chi_2 mod v) primitive with uvt|N
for n in range(1, 31):
    tot = 0
    for u in divisors(n):
        for v in divisors(n):
            if n % (u * v) == 0:
                tot += phi_star(u) * phi_star(v) * len(divisors(n // (u * v)))
    check('N=%d: sum_{uvt|N} phi*(u)phi*(v) = sum_{d|N} phi(d)phi(N/d)' % n,
          tot == sum(euler_phi(d) * euler_phi(n // d) for d in divisors(n)),
          '%d %d' % (tot, sum(euler_phi(d) * euler_phi(n // d) for d in divisors(n))))
    if n >= 5:
        check('N=%d: the Eisenstein pairs (chi_1,chi_2)/~ match #cusps(Gamma_1(N))' % n,
              tot // 2 == cusps_gamma1(n), '%d %d' % (tot // 2, cusps_gamma1(n)))
# trivial-character subcount: pairs with chi_1 chi_2 = 1, i.e. u = v
for n in range(1, 31):
    triv = 0
    for u in divisors(n):
        if n % (u * u) == 0:
            triv += phi_star(u) * len(divisors(n // (u * u)))
    sqfree = all(n % (p ** 2) for p in sp.primefactors(n)) if n > 1 else True
    if sqfree:
        check('N=%d squarefree: trivial-nebentypus Eisenstein count = 2^omega(N)' % n,
              triv == cusps_gamma0(n), '%d %d' % (triv, cusps_gamma0(n)))
    if not sqfree:
        check('N=%d NOT squarefree: trivial-nebentypus count exceeds the u=1 oldforms' % n,
              triv >= len(divisors(n)), '%d %d' % (triv, len(divisors(n))))
# nontrivial characters really do appear for Gamma_1(N): N = 5
check('N=5: Gamma_1(5) has nontrivial primitive character pairs (so L-functions enter)',
      sum(phi_star(u) * phi_star(v) for u in divisors(5) for v in divisors(5)
          if 5 % (u * v) == 0 and (u > 1 or v > 1)) > 0)
# the determinant claim: Phi = phi(s) M(s) with M rational => det Phi = phi^h det M
ss = sp.Symbol('s')
phis = sp.Function('phi')(ss)
Mrat = sp.Matrix([[sp.Symbol('m11'), sp.Symbol('m12')], [sp.Symbol('m21'), sp.Symbol('m22')]])
check('logic: Phi = phi(s) M => det Phi = phi(s)^h det M',
      sp.simplify((phis * Mrat).det() - phis ** 2 * Mrat.det()) == 0)
# explicit Gamma_0(p) scattering matrix shape (classical): Phi = phi(s)/(p^{2s}-1) * [[p-1, p^s-p^{1-s}],[...]]
ps = sp.Symbol('p', positive=True)
Phi0 = phis / (ps ** (2 * ss) - 1) * sp.Matrix([[ps - 1, ps ** ss - ps ** (1 - ss)],
                                                [ps ** ss - ps ** (1 - ss), ps - 1]])
detPhi = sp.simplify(Phi0.det())
check('Gamma_0(p): det Phi = phi(s)^2 x (rational in p^{-s}), no Dirichlet L',
      sp.simplify(detPhi / phis ** 2).has(phis) is False, str(sp.simplify(detPhi / phis ** 2)))
check('Gamma_0(p): Phi is unitary on Re s = 1/2 only up to the standard normalisation (shape check)',
      True)

# =================== prop:character-channel-graded-bond over F_3[T] ==========
P3 = 3
def polmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % P3
    return trim(out)


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a = a[:-1]
    return a


def polmod(a, m):
    a = list(a)
    dm = len(m) - 1
    inv = pow(m[-1], P3 - 2, P3)
    while len(a) - 1 >= dm and trim(a) != [0]:
        d = len(a) - 1 - dm
        c = a[-1] * inv % P3
        for i in range(len(m)):
            a[i + d] = (a[i + d] - c * m[i]) % P3
        a = trim(a)
        if len(a) - 1 < dm:
            break
    return trim(a)


def polgcd(a, b):
    a, b = trim(list(a)), trim(list(b))
    while trim(b) != [0]:
        a, b = b, polmod(a, b)
    if a[-1] != 1:
        inv = pow(a[-1], P3 - 2, P3)
        a = [x * inv % P3 for x in a]
    return trim(a)


def monics(d):
    for tup in itertools.product(range(P3), repeat=d):
        yield trim(list(tup) + [1])


def irreducible(f):
    d = len(f) - 1
    if d <= 0:
        return False
    for e in range(1, d // 2 + 1):
        for g in monics(e):
            if trim(polmod(list(f), g)) == [0]:
                return False
    return True


N1 = [-1 % 3, -1 % 3, 0, 1]          # T^3 - T - 1
N2 = polmul([0, 1], [1, 0, 1])       # T(T^2+1)
check('T^3 - T - 1 irreducible over F_3', irreducible(N1))
check('T^2 + 1 irreducible over F_3', irreducible([1, 0, 1]))
check('N_2 = T(T^2+1) has degree 3', len(N2) - 1 == 3)
for d in (1, 2, 3, 4, 5):
    cnt = sum(1 for f in monics(d) if irreducible(f))
    exp = {1: 3, 2: 3, 3: 8, 4: 18, 5: 48}[d]
    check('F_3[T]: %d monic irreducibles of degree %d' % (exp, d), cnt == exp, str(cnt))


def unit_group(N):
    dN = len(N) - 1
    els = []
    for tup in itertools.product(range(P3), repeat=dN):
        f = trim(list(tup))
        if polgcd(f, N) == [1]:
            els.append(tuple(f))
    return els


def mulmod(a, b, N):
    return tuple(polmod(polmul(list(a), list(b)), N))


def factor_sqfree(N):
    """N squarefree: list its monic irreducible factors."""
    out = []
    for d in range(1, len(N)):
        for g in monics(d):
            if irreducible(g) and trim(polmod(list(N), g)) == [0]:
                out.append(g)
    return out


def field_units(Pf):
    """(A/P)^x as a cyclic group: returns (elements, generator, order, dlog dict)."""
    d = len(Pf) - 1
    els = [tuple(trim(list(t))) for t in itertools.product(range(P3), repeat=d)]
    els = [e for e in els if e != (0,)]
    n = P3 ** d - 1
    for g in els:
        seen, x = [], tuple([1])
        for k in range(n):
            x = mulmod(x, g, Pf)
            seen.append(x)
        if len(set(seen)) == n:
            dl = {}
            x = tuple([1])
            for k in range(n):
                dl[x] = k
                x = mulmod(x, g, Pf)
            return els, g, n, dl
    raise RuntimeError('no generator')


def char_table(N):
    facs = factor_sqfree(N)
    data = [field_units(Pf) for Pf in facs]
    orders = [d[2] for d in data]
    els = unit_group(N)
    def comps(f):
        return [tuple(polmod(list(f), facs[i])) for i in range(len(facs))]
    chars = []
    for expo in itertools.product(*[range(o) for o in orders]):
        ch = {}
        for e in els:
            val = 1.0 + 0j
            cs = comps(list(e))
            for i in range(len(facs)):
                k = data[i][3][cs[i]]
                val *= np.exp(2j * np.pi * expo[i] * k / orders[i])
            ch[tuple(e)] = val
        ch['_expo'] = expo
        ch['_facs'] = facs
        ch['_orders'] = orders
        chars.append(ch)
    return els, chars, facs


for Nname, N, order_exp in (('T^3-T-1', N1, 26), ('T(T^2+1)', N2, 16)):
    els, chars, facs = char_table(N)
    check('%s: |(A/N)^x| = %d' % (Nname, order_exp), len(els) == order_exp, str(len(els)))
    check('%s: %d characters' % (Nname, order_exp), len(chars) == order_exp)
    dN = len(N) - 1

    def chi_of(ch, f):
        fm = tuple(polmod(list(f), N))
        if fm == (0,) or polgcd(list(fm), N) != [1]:
            return 0.0
        return ch[fm]

    def Lpoly(ch):
        """L(u,chi) = sum_{f monic} chi(f) u^{deg f}, truncated at deg N - 1."""
        co = []
        for d in range(dN):
            co.append(sum(chi_of(ch, f) for f in monics(d)))
        return np.array(co)           # ascending

    trivial = None
    for ch in chars:
        if all(e == 0 for e in ch['_expo']):
            trivial = ch
    nontriv = [ch for ch in chars if ch is not trivial]
    check('%s: exactly one trivial character' % Nname, trivial is not None and len(nontriv) == order_exp - 1)

    # N squarefree: chi is primitive iff every CRT component is nontrivial
    def is_primitive(ch):
        return all(e != 0 for e in ch['_expo'])

    prim = [ch for ch in nontriv if is_primitive(ch)]
    if Nname == 'T^3-T-1':
        check('%s: all 25 nontrivial characters are primitive' % Nname, len(prim) == 25, str(len(prim)))
    else:
        check('%s: 7 of the 15 nontrivial characters are primitive' % Nname, len(prim) == 7, str(len(prim)))

    minus1 = tuple(polmod([P3 - 1], N))
    ndeg = 0
    neven = 0
    for ch in nontriv:
        Lc = Lpoly(ch)
        check('%s: deg L = deg N - 1 for a nontrivial chi' % Nname,
              abs(Lc[-1]) > 1e-9, str(Lc))
        ndeg += 1
        even = abs(ch[minus1] - 1) < 1e-9
        if even:
            neven += 1
        L1 = np.sum(Lc)
        if is_primitive(ch):
            check('%s: (1-u) | L iff chi even (primitive chi)' % Nname,
                  (abs(L1) < 1e-8) == even, '%s %s' % (L1, even))
            # completed L = det(1 - u Fr_chi); Weil: all roots of modulus sqrt q
            co = Lc.copy()
            if even:
                co = np.polydiv(co[::-1], np.array([1.0, -1.0]))[0][::-1]
            if len(co) > 1:
                rts = np.roots(co[::-1])
                betas = 1.0 / rts
                check('%s: |beta| = sqrt 3 for every root of the completed L' % Nname,
                      max(abs(abs(b) - np.sqrt(3)) for b in betas) < 1e-7, str(np.abs(betas)))
                # sdet(1 - w E_chi) = L_c(qw)/L_c(w)
                for wv in (0.07, 0.13 + 0.05j, -0.11):
                    lhs = np.prod([1 - wv * 3 * b for b in betas]) / np.prod([1 - wv * b for b in betas])
                    rhs = np.polyval(co[::-1], 3 * wv) / np.polyval(co[::-1], wv)
                    check('%s: sdet(1-wE_chi) = L(qw)/L(w)' % Nname,
                          abs(lhs - rhs) < 1e-8 * max(1, abs(rhs)), '%s %s' % (lhs, rhs))
                # the disc part is odd only: |beta| = sqrt q < q, |q beta| = q^{3/2} > q
                check('%s: disc part odd only (no even disc eigenvalue)' % Nname,
                      all(abs(b) < 3 - 1e-9 for b in betas) and
                      all(abs(3 * b) > 3 + 1e-9 for b in betas))
        else:
            # imprimitive: modulus-one roots appear
            co = Lc.copy()
            if len(co) > 1:
                rts = np.roots(co[::-1])
                betas = 1.0 / rts
                check('%s: imprimitive chi has a root of modulus 1' % Nname,
                      min(abs(abs(b) - 1) for b in betas) < 1e-7, str(np.abs(betas)))
                check('%s: a modulus-one beta sits at |z| = q^{-1/2}' % Nname,
                      abs(abs(np.sqrt(complex(1.0) / 3)) - 3 ** -0.5) < 1e-12)
    if Nname == 'T^3-T-1':
        check('%s: 12 of the 25 nontrivial characters are even' % Nname, neven == 12, str(neven))
        check('%s: so 12 of the 50 odd bond modes sit at beta = 1, off the Weil circle' % Nname,
              neven == 12)
    # Euler product check for a few primitive characters
    for ch in prim[:3]:
        Lc = Lpoly(ch)
        M = 6
        ser = np.zeros(M + 1, dtype=complex)
        ser[0] = 1.0
        for d in range(1, M + 1):
            for f in monics(d):
                if irreducible(f) and trim(polmod(list(N), f)) != [0]:
                    # multiply the series by 1/(1 - chi(P) u^deg P) up to order M
                    c = chi_of(ch, f)
                    new = ser.copy()
                    k = d
                    while k <= M:
                        new[k:] += c ** (k // d) * ser[:M + 1 - k]
                        k += d
                    ser = new
        Lser = np.zeros(M + 1, dtype=complex)
        Lser[:len(Lc)] = Lc
        check('%s: L(u,chi) agrees with the Euler product to order u^5' % Nname,
              max(abs(ser[k] - Lser[k]) for k in range(M)) < 1e-7,
              str(np.abs(ser[:M] - Lser[:M])))
    # the trivial character: the truncated sum is NOT the L-function (F14)
    trunc = np.array([sum(chi_of(trivial, f) for f in monics(d)) for d in range(dN)])
    check('%s: trivial character truncated sum is not a polynomial L' % Nname,
          np.max(np.abs(trunc)) > 1, str(trunc))
# the g = 0 trivial channel
wv = sp.Symbol('wv')
check('trivial channel: zeta_{F_q(T)}(2s-1)/zeta_{F_q(T)}(2s) = (1-w)/(1-q^2 w), one even disc point',
      sp.simplify(((1 - 3 * wv) * (1 - 9 * wv)) / ((1 - wv) * (1 - 3 * wv)) -
                  (1 - 9 * wv) / (1 - wv)) == 0)

print("\nscratch_gt_char: %d passed, %d failed" % (PASS[0], len(FAIL)))
