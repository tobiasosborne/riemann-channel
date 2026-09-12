"""Selberg trace formula pieces as a Lindblad / sum-of-squares story: five checks.

(A) A Lindbladian with Hermitian jumps is minus half a double commutator, and on a
    COMMUTATIVE function algebra with jumps L_j = -i X_j (X_j derivations) it acts on the
    multiplication operator M_f as multiplication by (1/2) sum_j X_j^2 f.  Checked exactly in
    sympy for X = a(x) d_x + b(y) d_y with generic a, b, f, g.
(B) Left-invariant vector fields on SL(2,R) in Iwasawa coordinates g = n(x) a(y) k(theta)
    (generators of the RIGHT action, (X_A f)(g) = d/dt f(g exp(tA))), obtained exactly by
    pushing the Iwasawa coordinate map (x,y,theta) <- M through M = g exp(tA).  On right-K-
    invariant f(g) = F(x,y) we check W f = W^2 f = 0, Omega f = c y^2 (F_xx + F_yy) with
    Omega = H^2/4 + (X_+X_- + X_-X_+)/2 = (H^2 + E^2 - W^2)/4, and that the two-jump
    Lindbladian (1/2)(H^2 + E^2) of (A) with L_1 = -iH, L_2 = -iE is a constant times the
    hyperbolic Laplacian.  Constants are printed, not assumed.
(C) The same sum-of-squares identity in the quantum (noncommutative) case: for anti-Hermitian
    X_j, S(rho) = sum_j (L_j rho L_j - {L_j^2,rho}/2) with L_j = -i X_j equals, in column-
    stacking vec convention (vec(A rho B) = (B^T (x) A) vec rho),
    (1/2) sum_j (pi (x) pibar)(X_j)^2 with (pi (x) pibar)(X) = 1 (x) X + Xbar (x) 1.
    Seeded random n=4 data, then the sl(2) generators in the 3-dimensional irrep, where the
    spectrum must be -2 j(j+1), j = 2,1,0 (Casimir of V_1 (x) V_1* = V_2 + V_1 + V_0).
(D) The Poincare map of a closed geodesic of length l on the unit tangent bundle PSL(2,R):
    Ad(a_l) on sl(2)/<H>, eigenvalues e^l, e^-l, |det(1 - P^k)| = 4 sinh^2(k l /2); the
    0-dimensional transverse space of the circle flow gives 1.  Exact in sympy.
(E) The cusp / scattering term of PSL(2,Z) is the prime comb.  With
    phi(s) = sqrt(pi) Gamma(s-1/2) zeta(2s-1) / (Gamma(s) zeta(2s)) and
    m(r) = -Re (phi'/phi)(1/2 + i r), the windowed cosine transform
    C(t) = (1/2pi) int_{-R}^{R} e^{-r^2/2G^2} cos(rt) m(r) dr
    is predicted (functional equation applied to zeta'/zeta(2ir)) to be
    C_arith(t) = 1 - (2G/sqrt(2pi)) sum_n (Lambda(n)/n) e^{-G^2 (t - 2 log n)^2/2},
    the constant 1 coming from the pole of zeta at s = 1 (each of the two Dirichlet halves needs
    a principal value, and each indented contour contributes half of it); this constant was NOT
    in the original prediction -- it was found in the residual and then derived.
    The smooth archimedean background is removed exactly, m_arch(r) = -Re[psi(ir) - psi(1/2+ir)
    + 2 chi'/chi(2ir)], chi'/chi(s) = log 2pi + (pi/2)cot(pi s/2) - psi(1-s), and also
    (cross-check) by midpoints between consecutive dips.  mpmath, mp.dps = 20.
Every check prints a numeric error or True/False and the script ends with ALL CHECKS PASS."""
import time, numpy as np, sympy as sp, mpmath as mp
from sympy import factorint
T0 = time.time(); ok = {}

# =====================================================================================
print('=' * 86)
print('(A) LINDBLAD = SUM OF SQUARES ON A COMMUTATIVE ALGEBRA  (sympy, exact, generic a,b,f,g)')
print('=' * 86)
x, y = sp.symbols('x y', real=True)
a, b, f, g = sp.Function('a'), sp.Function('b'), sp.Function('f'), sp.Function('g')
I = sp.I
X = lambda u: a(x) * sp.diff(u, x) + b(y) * sp.diff(u, y)          # derivation X
L = lambda u: -I * X(u)                                            # Hermitian jump L = -iX
F, Gt = f(x, y), g(x, y)                                           # f acts by multiplication
C1 = lambda u: L(F * u) - F * L(u)                                 # [L, M_f] u
C2 = lambda u: L(C1(u)) - C1(L(u))                                 # [L, [L, M_f]] u
lhs = sp.expand(sp.simplify(C2(Gt)))
rhs = sp.expand(sp.simplify(-X(X(F)) * Gt))
print('  [L,[L,M_f]] g            =', lhs)
print('  -X^2(f) . g              =', rhs)
ok['A1'] = sp.simplify(lhs - rhs) == 0
print('  [L,[L,M_f]] g == -X^2(f) g :', ok['A1'])
lind = sp.expand(sp.simplify(L(F * Gt) * 1 - 0))                    # build L f L - {L^2,f}/2 directly
lindb = sp.expand(sp.simplify(L(F * L(Gt)) - sp.Rational(1, 2) * (L(L(F * Gt)) + F * L(L(Gt)))))
half = sp.expand(sp.simplify(sp.Rational(1, 2) * X(X(F)) * Gt))
ok['A2'] = sp.simplify(lindb - half) == 0
print('  (L M_f L - {L^2,M_f}/2) g =', lindb)
print('  (1/2) X^2(f) . g          =', half)
print('  Lindbladian on M_f == M_{(1/2) X^2 f} :', ok['A2'])
print('  => with jumps L_j = -i X_j the Heisenberg Lindbladian is (1/2) sum_j X_j^2.')

# =====================================================================================
print()
print('=' * 86)
print('(B) CASIMIR ON K-INVARIANT FUNCTIONS = HYPERBOLIC LAPLACIAN  (sympy, exact)')
print('=' * 86)
th, t = sp.symbols('theta t', real=True)
yy = sp.Symbol('y', positive=True)
sq = sp.sqrt(yy)
n_ = sp.Matrix([[1, x], [0, 1]])
a_ = sp.Matrix([[sq, 0], [0, 1 / sq]])
k_ = sp.Matrix([[sp.cos(th), sp.sin(th)], [-sp.sin(th), sp.cos(th)]])
Gm = sp.simplify(n_ * a_ * k_)
print('  g = n(x)a(y)k(theta) =', Gm.tolist())
Hm = sp.Matrix([[1, 0], [0, -1]]); Em = sp.Matrix([[0, 1], [1, 0]]); Wm = sp.Matrix([[0, 1], [-1, 0]])
Xp = sp.Matrix([[0, 1], [0, 0]]); Xm = sp.Matrix([[0, 0], [1, 0]])
expH = sp.Matrix([[sp.exp(t), 0], [0, sp.exp(-t)]])
expE = sp.Matrix([[sp.cosh(t), sp.sinh(t)], [sp.sinh(t), sp.cosh(t)]])
expW = sp.Matrix([[sp.cos(t), sp.sin(t)], [-sp.sin(t), sp.cos(t)]])
exps = {'H': (Hm, expH), 'E': (Em, expE), 'W': (Wm, expW)}
ok['B0'] = all(sp.simplify(sp.diff(Ex, t) - A * Ex) == sp.zeros(2, 2) and
               sp.simplify(Ex.subs(t, 0) - sp.eye(2)) == sp.zeros(2, 2) for A, Ex in exps.values())
print('  exp(tA) closed forms verified (d/dt = A exp(tA), value I at 0):', ok['B0'])
# Iwasawa coordinates of a matrix M = ((A,B),(C,D)):  y = 1/(C^2+D^2), x = (AC+BD)/(C^2+D^2),
# theta = atan2(-C, D)  [bottom row of n(x)a(y)k(th) is (-sin th, cos th)/sqrt(y)].
coord_ok = []
def vfield(Ex):
    M = Gm * Ex
    A_, B_, C_, D_ = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    den = C_**2 + D_**2
    Yc, Xc = 1 / den, (A_ * C_ + B_ * D_) / den
    Tdot = (-sp.diff(C_, t) * D_ + C_ * sp.diff(D_, t)) / den        # d/dt atan2(-C,D)
    coord_ok.append(sp.simplify(Xc.subs(t, 0) - x) == 0 and sp.simplify(Yc.subs(t, 0) - yy) == 0)
    return tuple(sp.simplify(sp.diff(q, t).subs(t, 0)) for q in (Xc, Yc)) + (sp.simplify(Tdot.subs(t, 0)),)
vH, vE, vW = vfield(expH), vfield(expE), vfield(expW)
vXp = tuple((p + q) / 2 for p, q in zip(vE, vW))                     # X_+ = (E + W)/2
vXm = tuple((p - q) / 2 for p, q in zip(vE, vW))                     # X_- = (E - W)/2
ok['B1'] = all(coord_ok)
print('  Iwasawa coordinate map reproduces (x,y) at t=0:', ok['B1'])
for nm, v in (('X_H  ', vH), ('X_E  ', vE), ('X_W  ', vW), ('X_{+}', vXp), ('X_{-}', vXm)):
    print(f'   {nm} = ({sp.simplify(v[0])}) d_x + ({sp.simplify(v[1])}) d_y + ({sp.simplify(v[2])}) d_theta')
ap = lambda v, u: sp.expand(v[0] * sp.diff(u, x) + v[1] * sp.diff(u, yy) + v[2] * sp.diff(u, th))
# sanity: left-invariant fields must satisfy [X_A, X_B] = X_[A,B]
def bracket(v, w, u): return sp.simplify(ap(v, ap(w, u)) - ap(w, ap(v, u)))
probe = sp.Function('P')(x, yy, th)
vmap = {'H': (Hm, vH), 'E': (Em, vE), 'W': (Wm, vW)}
def vof(A):                                                          # expand A in H, E, W basis
    cH = A[0, 0]; cE = (A[0, 1] + A[1, 0]) / 2; cW = (A[0, 1] - A[1, 0]) / 2
    return tuple(cH * vH[i] + cE * vE[i] + cW * vW[i] for i in range(3))
comm_err = []
for n1, (A1, v1) in vmap.items():
    for n2, (A2, v2) in vmap.items():
        comm_err.append(sp.simplify(bracket(v1, v2, probe) - ap(vof(A1 * A2 - A2 * A1), probe)))
ok['B2'] = all(e == 0 for e in comm_err)
print('  [X_A, X_B] = X_[A,B] for A,B in {H,E,W} (left-invariance):', ok['B2'])
Fk = sp.Function('F')(x, yy)                                         # right-K-invariant function
print('  H f  (theta=0) =', sp.simplify(ap(vH, Fk).subs(th, 0)))
print('  E f  (theta=0) =', sp.simplify(ap(vE, Fk).subs(th, 0)))
print('  W f            =', sp.simplify(ap(vW, Fk)))
H2 = sp.simplify(ap(vH, ap(vH, Fk))); E2 = sp.simplify(ap(vE, ap(vE, Fk)))
W1 = sp.simplify(ap(vW, Fk)); W2 = sp.simplify(ap(vW, ap(vW, Fk)))
ok['B3'] = (W1 == 0) and (W2 == 0)
print('  (i)  W f = 0 and W^2 f = 0 on K-invariant f :', ok['B3'])
print('  H^2 f =', H2)
print('  E^2 f =', E2)
print('  (H^2 + E^2) f =', sp.simplify(H2 + E2), '   <- theta cancels')
lap = (yy**2 * (sp.Derivative(Fk, x, 2) + sp.Derivative(Fk, yy, 2))).doit()
Om = sp.simplify(sp.Rational(1, 4) * (H2 + E2 - W2))
OmX = sp.simplify(sp.Rational(1, 4) * ap(vH, ap(vH, Fk))
                  + sp.Rational(1, 2) * (ap(vXp, ap(vXm, Fk)) + ap(vXm, ap(vXp, Fk))))
cB = sp.simplify(Om / lap)
cB2 = sp.simplify(OmX / lap)
print('  Omega f = (1/4)(H^2+E^2-W^2) f =', Om)
print('  c  in  Omega f = c * y^2 (F_xx + F_yy)   :  c =', cB, '   (from H^2/4 + (X_+X_-+X_-X_+)/2 :', cB2, ')')
ok['B4'] = (cB == cB2) and cB.is_number and sp.simplify(sp.Abs(cB) - 1) == 0
print('  (ii) Omega f = c y^2(F_xx+F_yy) with |c| = 1 :', ok['B4'], '  sign of c:', '+' if cB > 0 else '-')
LindB = sp.simplify(sp.Rational(1, 2) * (H2 + E2))                   # Lindbladian of (A), L_1=-iH, L_2=-iE
cL = sp.simplify(LindB / lap)
ok['B5'] = sp.simplify(LindB - 2 * Om) == 0
print('  (iii) Lindbladian (1/2)(H^2+E^2) f =', LindB)
print('        (1/2)(H^2+E^2) f = 2 Omega f :', ok['B5'])
print('        Lindblad-to-Laplacian constant: (1/2)(H^2+E^2) f =', cL, '* y^2 (F_xx + F_yy)')

# =====================================================================================
print()
print('=' * 86)
print('(C) QUANTUM LINDBLADIAN = TENSOR-PRODUCT SUM OF SQUARES  (numerical, seeded)')
print('=' * 86)
rng = np.random.default_rng(20260912)
def lind_super(Ls):
    n = Ls[0].shape[0]; Id = np.eye(n); S = np.zeros((n * n, n * n), complex)
    for Lj in Ls:
        S += np.kron(Lj.T, Lj) - 0.5 * (np.kron(Id, Lj @ Lj) + np.kron((Lj @ Lj).T, Id))
    return S
def sos_super(Xs):
    n = Xs[0].shape[0]; Id = np.eye(n)
    return 0.5 * sum(np.linalg.matrix_power(np.kron(Id, Xj) + np.kron(Xj.conj(), Id), 2) for Xj in Xs)
def direct_check(label, Xs):
    Ls = [-1j * Xj for Xj in Xs]
    herm = max(np.abs(Lj - Lj.conj().T).max() for Lj in Ls)
    S1, S2 = lind_super(Ls), sos_super(Xs)
    # brute-force application to random rho, column stacking vec
    n = Xs[0].shape[0]; e = 0.0
    for _ in range(5):
        rho = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        img = sum(Lj @ rho @ Lj - 0.5 * (Lj @ Lj @ rho + rho @ Lj @ Lj) for Lj in Ls)
        e = max(e, np.abs(S1 @ rho.reshape(-1, order='F') - img.reshape(-1, order='F')).max())
    err = np.abs(S1 - S2).max()
    print(f'  {label}')
    print(f'    max |L_j - L_j^dag| (jumps Hermitian)                 : {herm:.2e}')
    print(f'    max |vec(S(rho)) - S_mat vec(rho)| (vec convention)   : {e:.2e}')
    print(f'    max |S_mat - (1/2) sum_j (1(x)X + Xbar(x)1)^2|        : {err:.2e}')
    return max(err, e, herm), S1
n = 4
Xs = []
for _ in range(3):
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Xs.append(A - A.conj().T)
eC1, _ = direct_check(f'random anti-Hermitian X_1..X_3, n = {n}', Xs)
s2 = np.sqrt(2.0)
Hr = np.diag([2.0, 0.0, -2.0]).astype(complex)
Xpr = s2 * np.array([[0, 1, 0], [0, 0, 1], [0, 0, 0]], complex)
Xmr = Xpr.conj().T
rel_err = max(np.abs(Xpr @ Xmr - Xmr @ Xpr - Hr).max(),
              np.abs(Hr @ Xpr - Xpr @ Hr - 2 * Xpr).max(),
              np.abs(Hr @ Xmr - Xmr @ Hr + 2 * Xmr).max())
print(f'  sl(2) 3-dim irrep (unitary normalisation, X_-=X_+^dag): [X_+,X_-]=H, [H,X_+-]=+-2X_+- err {rel_err:.2e}')
Xsl = [1j * Hr, Xpr - Xmr, 1j * (Xpr + Xmr)]
eC2, Ssl = direct_check('sl(2) generators iH, X_+ - X_-, i(X_+ + X_-) in the 3-dim irrep', Xsl)
ev = np.sort(np.linalg.eigvals(Ssl).real)
pred = np.sort(np.array([-2 * j * (j + 1) for j, mult in ((2, 5), (1, 3), (0, 1)) for _ in range(mult)], float))
eC3 = np.abs(ev - pred).max()
imax = np.abs(np.linalg.eigvals(Ssl).imag).max()
print('    spectrum of S  :', np.array2string(ev, precision=6, suppress_small=True))
print('    predicted -2j(j+1), j=2(x5),1(x3),0(x1) (Casimir of V_1 (x) V_1bar = V_2+V_1+V_0):')
print('                   :', np.array2string(pred, precision=6, suppress_small=True))
print(f'    max |spectrum - prediction| = {eC3:.2e}   max |Im eigenvalue| = {imax:.2e}')
ok['C'] = max(eC1, eC2, eC3, imax, rel_err) < 1e-10
print('  (C) all errors < 1e-10 :', ok['C'])

# =====================================================================================
print()
print('=' * 86)
print('(D) POINCARE MAP OF A CLOSED GEODESIC  (sympy, exact)')
print('=' * 86)
ell, kk = sp.symbols('ell k', positive=True)
at = sp.Matrix([[sp.exp(ell / 2), 0], [0, sp.exp(-ell / 2)]])
basis = [Hm, Xp, Xm]
def adm(A):                                                          # Ad(A) on sl(2) in basis H,X_+,X_-
    cols = []
    for B in basis:
        C = sp.simplify(A * B * A.inv())
        cols.append([sp.simplify(C[0, 0]), sp.simplify(C[0, 1]), sp.simplify(C[1, 0])])
    return sp.Matrix(cols).T
Ad = sp.simplify(adm(at))
print('  Ad(a_l) on basis (H, X_+, X_-)  =', Ad.tolist())
ok['D1'] = sp.simplify(Ad - sp.diag(1, sp.exp(ell), sp.exp(-ell))) == sp.zeros(3, 3)
print('  Ad(a_l) = diag(1, e^l, e^-l)  (H is the flow direction) :', ok['D1'])
P = Ad[1:, 1:]                                                        # transverse space sl(2)/<H>
print('  transverse (Poincare) map P = Ad(a_l)|_{sl(2)/<H>} =', P.tolist())
print('  eigenvalues of P :', sorted(sp.simplify(sp.Matrix(list(P.eigenvals().keys()))), key=str))
Pk = sp.simplify(sp.diag(sp.exp(kk * ell), sp.exp(-kk * ell)))
det = sp.simplify((sp.eye(2) - Pk).det())
print('  det(1 - P^k) =', sp.simplify(sp.expand(det)))
target = (sp.exp(kk * ell / 2) - sp.exp(-kk * ell / 2))**2
ok['D2'] = sp.simplify(sp.expand(-det - target)) == 0 and sp.simplify(target - 4 * sp.sinh(kk * ell / 2)**2) == 0
print('  |det(1 - P^k)| = (e^{kl/2}-e^{-kl/2})^2 = 4 sinh^2(kl/2) :', ok['D2'],
      '   (det itself is negative: det =', sp.simplify(sp.expand(det)), ')')
circ = sp.Matrix(0, 0, [])                                            # circle: no transverse space
ok['D3'] = sp.simplify((sp.eye(0) - circ).det() - 1) == 0
print('  circle flow, 0-dimensional transverse space: det of the empty matrix =',
      (sp.eye(0) - circ).det(), ' == 1 :', ok['D3'])

# =====================================================================================
print()
print('=' * 86)
print('(E) THE CUSP TERM OF THE MODULAR SURFACE IS THE PRIME COMB  (mpmath)')
print('=' * 86)
mp.mp.dps = 20
Gw, R, dr = 40.0, 240.0, 0.05                                         # window, cutoff = 6G, step
Nr = int(round(R / dr))
rg = (np.arange(Nr) + 0.5) * dr                                       # offset grid, avoids the r=0 pole
print(f'  window G = {Gw}, cutoff R = {R} = {R/Gw:.1f} G, step dr = {dr}, {Nr} r-points'
      f' ({4*Nr} zeta/zeta\' calls), tail weight e^(-R^2/2G^2) = {np.exp(-R**2/(2*Gw**2)):.2e}')
print("  m(r) = -Re (phi'/phi)(1/2+ir),  phi'/phi(s) = psi(s-1/2) - psi(s) + 2 z'/z(2s-1) - 2 z'/z(2s)")
def m_full(r):
    s = mp.mpf(1) / 2 + 1j * mp.mpf(r)
    v = (mp.digamma(s - mp.mpf(1) / 2) - mp.digamma(s)
         + 2 * (mp.zeta(2 * s - 1, derivative=1) / mp.zeta(2 * s - 1)
                - mp.zeta(2 * s, derivative=1) / mp.zeta(2 * s)))
    return -mp.re(v)
def m_arch(r):
    # chi'/chi(s) = log 2pi + (pi/2) cot(pi s/2) - psi(1-s);  at s = 2ir the cot term is purely imaginary
    rr = mp.mpf(r)
    return -mp.re(mp.digamma(1j * rr) - mp.digamma(mp.mpf(1) / 2 + 1j * rr)
                  + 2 * (mp.log(2 * mp.pi) - mp.digamma(1 - 2j * rr)))
# functional equation z'/z(s) + z'/z(1-s) = chi'/chi(s) turns the 2 z'/z(2s-1) term into a second
# copy of the prime sum, so m_full - m_arch must be exactly 4 Re z'/z(1 + 2ir).
fe = 0.0
for rt in (0.37, 1.9, 6.5, 21.0, 57.3, 133.7, 239.5):
    fe = max(fe, abs(float(m_full(rt) - m_arch(rt)
                          - 4 * mp.re(mp.zeta(1 + 2j * mp.mpf(rt), derivative=1) / mp.zeta(1 + 2j * mp.mpf(rt))))))
print(f"  functional-equation split: max |m(r) - m_arch(r) - 4 Re z'/z(1+2ir)| over 7 sample r = {fe:.2e}")
tic = time.time()
mv = np.array([float(m_full(r)) for r in rg])
av = np.array([float(m_arch(r)) for r in rg])
print(f'  m(r), m_arch(r) evaluated on the grid in {time.time()-tic:.1f} s;  m({rg[0]}) = {mv[0]:.6f},'
      f'  m({rg[-1]}) = {mv[-1]:.6f}')
wg = np.exp(-rg**2 / (2 * Gw**2))
# even integrand => (1/2pi) int_{-R}^{R} = (1/pi) int_0^R ; offset grid = trapezoid on +-(k+1/2)dr
def transform(vals, ts):
    w = wg * vals * dr / np.pi
    return np.array([np.dot(w, np.cos(rg * tt)) for tt in np.atleast_1d(ts)])
def Lam(nn):
    fac = factorint(nn)
    return float(np.log(list(fac)[0])) if len(fac) == 1 else 0.0
ns = (2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27)
tns = np.array([2 * np.log(nn) for nn in ns])
mids = (tns[:-1] + tns[1:]) / 2
mids = np.concatenate([[2 * tns[0] - mids[0]], mids, [2 * tns[-1] - mids[-1]]])   # outer half-steps too
tg = np.concatenate([np.arange(0.5, 7.0 + 1e-9, 0.002), tns, mids])
order = np.argsort(tg); tg = tg[order]
C_full, C_arch = transform(mv, tg), transform(av, tg)
C_ar = C_full - C_arch
Kpred = -2 * Gw / np.sqrt(2 * np.pi)
print()
print('  PREDICTION.  A unit-weight term cos(r t_n) in m(r) contributes to C(t), at t near t_n,')
print(f'    (1/2pi)(1/2) G sqrt(2pi) e^(-G^2 (t-t_n)^2/2) = {Gw/(2*np.sqrt(2*np.pi)):.6f} e^(-G^2(t-t_n)^2/2).')
print('    The weight of n is -4 Lambda(n)/n (2 from -2 z\'/z(1+2ir), 2 from its functional-equation')
print(f'    mirror 2 z\'/z(2ir)), so K = -4 * G/(2 sqrt(2pi)) = -2G/sqrt(2pi) = {Kpred:.6f}.')
print("    PLUS a pole term: 2 z'/z(1+-2ir) has a simple pole at r=0 (the pole of zeta at s=1) with")
print('    residue -+i; splitting m - m_arch into the two Dirichlet halves needs principal values,')
print('    and each indented contour gives -/+ i pi (residue) = pi, i.e. (1/2pi)(pi + pi) = +1 exactly.')
print('    So C_arith(t) := C(t) - C_arch(t) = 1 + K sum_n (Lambda(n)/n) e^(-G^2 (t - 2 log n)^2/2).')
pred_curve = np.ones_like(tg)
for nn in range(2, 80):
    Ln = Lam(nn)
    if Ln:
        tn = 2 * np.log(nn)
        pred_curve += Kpred * (Ln / nn) * (np.exp(-Gw**2 * (tg - tn)**2 / 2)
                                           + np.exp(-Gw**2 * (tg + tn)**2 / 2))
mask = np.ones_like(tg, bool)
for nn in range(2, 80):
    if Lam(nn):
        mask &= np.abs(tg - 2 * np.log(nn)) > 6 / Gw
pole = C_ar[mask]
print(f'  measured pole constant: mean C_arith away from the dips (>6/G) = {pole.mean():.8f}'
      f'   sd = {pole.std(ddof=1):.2e}   (predicted exactly 1)')
idx = {round(tt, 9): i for i, tt in enumerate(tg)}
Cv = lambda arr, tt: arr[idx[round(tt, 9)]]
print()
print('   n  |  t_n = 2 log n |  C_arith(t_n)-1 |  Lambda(n)/n  |   ratio    | midpoint-bkg ratio')
rats, rats2 = [], []
for i, nn in enumerate(ns):
    tn = tns[i]
    amp = Cv(C_ar, tn) - 1.0
    w = Lam(nn) / nn
    lo, hi = Cv(C_full, mids[i]), Cv(C_full, mids[i + 1])
    amp2 = Cv(C_full, tn) - 0.5 * (lo + hi)
    rats.append(amp / w); rats2.append(amp2 / w)
    print(f'  {nn:3d} |    {tn:8.5f}   |   {amp:12.6f}  |   {w:9.6f}   | {amp/w:10.5f} |  {amp2/w:10.5f}')
rats = np.array(rats); rats2 = np.array(rats2)
print(f'  mean ratio (exact archimedean + pole background) = {rats.mean():.6f}   sd = {rats.std(ddof=1):.2e}'
      f'   spread (max-min) = {rats.max()-rats.min():.2e}')
print(f'  mean ratio (midpoint background, no theory input) = {rats2.mean():.6f}   sd = {rats2.std(ddof=1):.2e}')
print(f'  predicted K = {Kpred:.6f}    predicted/measured = {Kpred/rats.mean():.8f}')
print(f'  SIGN CONVENTION: the measured amplitudes and the ratio are '
      f'{"NEGATIVE -> the prime powers appear as DIPS" if rats.mean() < 0 else "POSITIVE -> the prime powers appear as PEAKS"}'
      f' in C(t), since Lambda(n)/n > 0.')
resid = C_ar - pred_curve
print(f'  max |C_arith - (1 + comb)| everywhere on [0.5,7]     = {np.abs(resid).max():.3e}')
print(f'  max |C_arith - (1 + comb)| away from the dips (>6/G) = {np.abs(resid[mask]).max():.3e}')
print(f'  max |C_arith| overall = {np.abs(C_ar).max():.3f}   max |C_arch| = {np.abs(C_arch).max():.3f}')
ok['E0'] = fe < 1e-12
ok['E1'] = abs(Kpred / rats.mean() - 1) < 1e-3
ok['E2'] = rats.std(ddof=1) / abs(rats.mean()) < 1e-3
ok['E3'] = np.abs(resid).max() < 2e-3 * np.abs(C_ar).max()
ok['E4'] = abs(pole.mean() - 1) < 1e-4 and pole.std(ddof=1) < 1e-4
print(f'  (E) functional-equation split exact : {ok["E0"]};  predicted/measured within 0.1% : {ok["E1"]};')
print(f'      relative spread < 0.1% : {ok["E2"]};  residual < 0.2% of peak : {ok["E3"]};'
      f'  pole constant = 1 : {ok["E4"]}')

print()
print('=' * 86)
for kname in sorted(ok):
    print(f'  {kname}: {ok[kname]}')
print(f'  total runtime {time.time()-T0:.1f} s')
print('ALL CHECKS PASS' if all(ok.values()) else 'CHECK FAILURE')
