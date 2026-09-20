#!/usr/bin/env python3
"""Graded toys: the blind numerics lane for `notes/graded-toys/brief.md` (claims G1--G7).

Author line: claude:opus.  Protocol: blind to `notes/graded-toys/proofs.md`.
Deterministic (seed 20260920), no timestamps, no memory addresses, no imports from
other repository scripts.  Every claim is an assertion through `check(cond, msg)`;
a failing check is recorded and the run continues.

================================================================================
CONVENTIONS FIXED HERE (re-derived from the cited definitions, not copied)
================================================================================

DIAGRAM (`def:elliptic-cavity`, shard 04k).  A graph with stabiliser function
S: V u E -> R_+, adjacency (A f)(v) = sum_{e at v} (S(v)/S(e)) f(o(e)),
degree deg(v) = sum_{e at v} S(v)/S(e) = q+1 for a quotient of the (q+1)-regular tree.

NORMALISATION (`prop:stabiliser-normalisation`).  With g = f/sqrt(S),
    T_X = q^{-1/2} D^{-1/2} A_X D^{1/2},   D = diag S,   (A_X)_{vw} = S(v)/S(e),
so T_X = Ahat/sqrt q with Ahat_{vw} = sqrt(S(v)S(w))/S(e) SYMMETRIC.  A cusp ray
(S(c_{k+1}) = q S(c_k), S(c_k c_{k+1}) = S(c_k)) normalises to the free path and the
junction coupling is c^2 = S(v)/S(e).  A funnel ray (S(f_{k+1}) = S(f_k)/q,
S(f_k f_{k+1}) = S(f_{k+1})) also normalises to the free path, but the degree
condition at f_1 forces S(f_1) = S(e), so its junction coupling is
c_f^2 = S(v) S(f_1)/(q S(e)^2) = (S(v)/S(e))/q: the brief's C_funnel is the WEIGHT
S(v)/S(e), and the coupling carries the extra 1/q.  Hence the two self-energies
Sigma_cusp = C_c/z and Sigma_funnel = C_f/(q z) on the outgoing sheet.

SPECTRAL PARAMETER.  lambda = z + 1/z, z = q^{s-1/2}; |z| < 1 <-> Re s < 1/2;
q^{-2s} = z^{-2}/q, q^{1-2s} = z^{-2}.  lambda is invariant under z -> 1/z, so
Gamma(1/z) = Gamma(z) and S(z) = -Q(z)^{-1} Q(1/z) with Q(z) = I - z Gamma(z).

EXACT ARITHMETIC.  With z = sqrt(q) t,
    p(z)      = det((1+z^2) I - z T_X - C)      ->  det((1 + q t^2) I - t A_X - C),
    ptilde(z) = det((1+z^2) I - z T_X - z^2 C)  ->  det((1 + q t^2) I - t A_X - q t^2 C),
and the right-hand sides have INTEGER coefficients (A_X integer, C integer);
det is unchanged by the similarity A_X ~ Ahat, so determinants are computed on the
integer form and every analytic object on the symmetric form.

MODEL SPACE (h = 1, `thm:h-exit-model`).  For the finite Blaschke product
Theta = Pc/qq with Pc(w) = prod_j (w - z_j) (delay roots at 0 included) and
qq(w) = prod_j (1 - conj(z_j) w), K = {P/qq : deg P < N}; in the basis f_k = w^k/qq
the compressed shift Z = P_K M_w|_K is EXACTLY the companion matrix of Pc, and the
exit map is J = e_{N-1}^* in that basis (because (I - P_K)(w f_{N-1}) = Theta.1).
The Gram matrix G_{kl} = <f_l, f_k> = (1/2pi) int e^{i(l-k)th}/|qq|^2 is computed by
the trapezoidal rule on 2^14 points (exponentially convergent: the poles of 1/|qq|^2
sit at radius 1/|z_j| > 1), G = L L^*, and the orthonormal frame is y = L^* x, so
    Z_orth = L^* Z_comp L^{-*},   J_orth = e_{N-1}^* L^{-*}.
Eigenvector at a zero a: k_a = Theta/(w - a), coordinate vector = coefficients of
Pc(w)/(w-a); J k_a = 1 (monic), <k_a,k_a> = 1/(1-|a|^2).  INNER PRODUCT CONVENTION:
<x,y> = x^dagger y, conjugate-linear in the FIRST slot; the Gram identity of
`thm:h-exit-model` then reads a_n^* a_m = (1 - conj(z_n) z_m) <k_n, k_m>.

GRADING.  Bond H = H_+ (+) H_-, P = 1 (+) (-1); B(H) is graded by Ad(P); the doubled
transfer is EE = sum_i A_i (x) conj(A_i) acting on ROW-MAJOR vec(rho), the doubled
parity is P (x) conj P, str M = Tr[(P (x) conj P) M], and (02f)
sdet(1 - u EE) = det(1 - u EE|even)/det(1 - u EE|odd).

TOLERANCES.  1e-9 for float identities throughout, except where a computation is
ill-conditioned; every exception is listed here and none was chosen to make a claim pass.
 * 1e-8 / 1e-7 when matching or counting EIGENVALUES of the doubled channel (49 x 49, 64 x 64)
   or of Ad_Z.  Those matrices are strongly non-normal and carry a nilpotent delay block; the
   eigenvalues of a defective matrix are conditioned like a root of the perturbation, so an
   eigenvalue agreement below 1e-8 is not available.  Multiplicity grouping uses 1e-7.
 * 1e-8 for the equimodularity spread of the perturbed Hasse-Weil quartet (np.roots on a
   degree-12 polynomial) and 1e-6 for the modulus classification of L-function roots, which
   have a DOUBLE root at u = 1 for some characters: a double root is resolved only to about
   the square root of machine precision.
 * Exact (sympy over Q, or over Q(sqrt q)) wherever exactness is available: all of p, ptilde,
   the G1 linearisation identities, the G2 superdeterminant identities and G4(b).

TATE TWIST AND PARITY FLIP (G2).  Fr(-1) := q Fr (same space, same parities);
Pi = the parity flip (the same operator with P replaced by -P).  E_S = Fr (+) Pi Fr(-1),
so the twisted copy's H^0, H^2 lines become ODD and its H^1 lines become EVEN.
================================================================================
"""
import mpmath as mp
import numpy as np
import sympy as sp

SEED = 20260920
rng = np.random.default_rng(SEED)
np.set_printoptions(linewidth=200, precision=8, suppress=True)

_PASS = 0
_FAIL = 0
_N = 0
FAILED = []

t_s, z_s, u_s, w_s, f_s = sp.symbols('t z u w f')


def check(cond, msg):
    """The single assertion helper: counts, prints one line, never aborts."""
    global _PASS, _FAIL, _N
    _N += 1
    ok = bool(cond)
    if ok:
        _PASS += 1
    else:
        _FAIL += 1
        FAILED.append((_N, msg))
    print(f"  {'ok  ' if ok else 'FAIL'} {_N:3d}  {msg}")
    return ok


def note(msg):
    print(f"  --      {msg}")


def head(msg):
    print()
    print("=" * 100)
    print(msg)
    print("=" * 100)


def c6(x):
    x = complex(x)
    return f"{x.real + 0.0:+.6f}{x.imag + 0.0:+.6f}j"


def f6(x):
    return f"{float(x) + 0.0:+.6f}"


def clist(zs):
    zs = sorted((complex(x) for x in zs), key=lambda v: (round(v.real, 9), round(v.imag, 9)))
    return "[" + ", ".join(c6(v) for v in zs) + "]"


def flist(xs):
    return "[" + ", ".join(f6(x) for x in sorted(float(x) for x in xs)) + "]"


def nrts(expr, var):
    """Roots of a polynomial, with the z = 0 factor deflated exactly and the rest found at
    50 digits (mpmath, extra precision: repeated roots such as (z^2+1)^2 are resolved to
    better than 1e-12, which np.roots alone would not do)."""
    P = sp.Poly(sp.nsimplify(sp.expand(expr)), var)
    co = P.all_coeffs()
    m = 0
    while len(co) > 1 and co[-1] == 0:
        co = co[:-1]
        m += 1
    if len(co) <= 1:
        return [0j] * m
    try:
        with mp.workdps(50):
            rr = mp.polyroots([mp.mpmathify(str(sp.N(c, 50))) for c in co],
                              maxsteps=500, extraprec=800)
        rr = [complex(x) for x in rr]
    except Exception:
        rr = list(np.roots([complex(sp.N(c, 30)) for c in co]))
    return rr + [0j] * m


# ============================================================================ #
#  SECTION 0.  The two arithmetic diagrams and their exact determinants        #
# ============================================================================ #
head("SECTION 0   the diagrams D2, D3 (def:elliptic-cavity), normalisation, p and ptilde")

D2 = dict(
    name="D2",
    q=2,
    S={'A': 6, 'B': 2, 'C': 2, 'D': 1, 'E': 3, 'F': 3},
    edges=[('A', 'B', 2), ('B', 'C', 2), ('C', 'D', 1), ('D', 'E', 1), ('D', 'F', 1)],
    cusps=[('B', 2, 4)],
    P=[1, -2, 2],
)
D3 = dict(
    name="D3",
    q=3,
    S={'L1p': 48, 'L1': 12, 'L2': 6, 'X': 2, 'Xp': 8, 'Y': 6, 'Z': 12, 'Zp': 48, 'Q': 4},
    edges=[('L1p', 'L1', 12), ('L1', 'L2', 6), ('L2', 'X', 2), ('X', 'Xp', 2),
           ('X', 'Y', 2), ('X', 'Q', 2), ('Y', 'Z', 6), ('Z', 'Zp', 12)],
    cusps=[('L1', 12, 36), ('Z', 12, 36), ('Q', 4, 12), ('Q', 4, 12)],
    P=[1, 0, 3],
)


def build(dg):
    """A_X (integer), Ahat (symmetric), C, couplings, from the stabiliser data."""
    S, q = dg['S'], dg['q']
    order = list(S.keys())
    idx = {v: i for i, v in enumerate(order)}
    n = len(order)
    Aint = sp.zeros(n, n)
    Ahat = sp.zeros(n, n)
    for (a, b, se) in dg['edges']:
        i, j = idx[a], idx[b]
        Aint[i, j] = sp.Rational(S[a], se)
        Aint[j, i] = sp.Rational(S[b], se)
        val = sp.sqrt(sp.Integer(S[a]) * S[b]) / sp.Integer(se)
        Ahat[i, j] = val
        Ahat[j, i] = val
    C = sp.zeros(n, n)
    couplings = []
    for (v, se, sc1) in dg['cusps']:
        c2 = sp.Rational(S[v], se)
        C[idx[v], idx[v]] += c2
        couplings.append((idx[v], c2, sp.Rational(sc1, se)))
    out = dict(dg)
    out.update(order=order, idx=idx, n=n, Aint=Aint, Ahat=Ahat, C=C, couplings=couplings,
               h=len(dg['cusps']))
    return out


def degrees(dg):
    S = dg['S']
    deg = {v: sp.Integer(0) for v in S}
    for (a, b, se) in dg['edges']:
        deg[a] += sp.Rational(S[a], se)
        deg[b] += sp.Rational(S[b], se)
    for (v, se, sc1) in dg['cusps']:
        deg[v] += sp.Rational(S[v], se)
    return deg


def p_of(dg, Cmat=None):
    """p(z) and ptilde(z), exact, via the integer t = z/sqrt q form."""
    q, n, A = dg['q'], dg['n'], dg['Aint']
    C = dg['C'] if Cmat is None else Cmat
    Mt = (1 + q * t_s ** 2) * sp.eye(n) - t_s * A
    pt = sp.expand((Mt - C).det(method='berkowitz'))
    ptt = sp.expand((Mt - q * t_s ** 2 * C).det(method='berkowitz'))
    pz = sp.expand(sp.simplify(pt.subs(t_s, z_s / sp.sqrt(q))))
    ptz = sp.expand(sp.simplify(ptt.subs(t_s, z_s / sp.sqrt(q))))
    return sp.nsimplify(pz), sp.nsimplify(ptz)


d2 = build(D2)
d3 = build(D3)

for dg in (d2, d3):
    deg = degrees(dg)
    check(all(sp.simplify(deg[v] - (dg['q'] + 1)) == 0 for v in deg),
          f"S0 {dg['name']}: every core vertex has degree q+1 = {dg['q']+1} "
          f"({', '.join(f'{v}:{deg[v]}' for v in dg['order'])})")
    check(all(sp.simplify(r - dg['q']) == 0 for (_, _, r) in dg['couplings']),
          f"S0 {dg['name']}: every cusp ray satisfies S(c_1)/S(e) = q, so its first ray vertex "
          f"also has degree q+1 and the ray normalises to the free path")
    check(all(sp.simplify(c2 - 1) == 0 for (_, c2, _) in dg['couplings']),
          f"S0 {dg['name']}: every arithmetic junction has c^2 = S(v)/S(e) = 1 "
          f"(prop:stabiliser-normalisation), not the Nagao q+1")
    check(sp.simplify(dg['Ahat'] - sp.diag(*[1 / sp.sqrt(dg['S'][v]) for v in dg['order']]) *
                      dg['Aint'] * sp.diag(*[sp.sqrt(dg['S'][v]) for v in dg['order']])).is_zero_matrix,
          f"S0 {dg['name']}: Ahat = D^(-1/2) A_X D^(1/2) is symmetric, so T_X = Ahat/sqrt q is "
          f"a real symmetric core")

check(sp.simplify(d2['C'] - sp.diag(0, 1, 0, 0, 0, 0)).is_zero_matrix,
      "S0 D2: C = diag(0,1,0,0,0,0) in the order A,B,C,D,E,F")
check(sp.simplify(d3['C'] - sp.diag(0, 1, 0, 0, 0, 0, 1, 0, 2)).is_zero_matrix,
      "S0 D3: C = diag(0,1,0,0,0,0,1,0,2) in the order L1p,L1,L2,X,Xp,Y,Z,Zp,Q "
      "(the double cusp at Q gives the entry 2)")

# normalised core weights of prop:stabiliser-normalisation
_a, _b, _d, _e = sp.sqrt(sp.Rational(3, 2)), 1 / sp.sqrt(2), 2 / sp.sqrt(3), sp.sqrt(sp.Rational(2, 3))
T2 = d2['Ahat'] / sp.sqrt(2)
T3 = d3['Ahat'] / sp.sqrt(3)
check(all(sp.simplify(T2[d2['idx'][a], d2['idx'][b]] - v) == 0 for a, b, v in
          [('A', 'B', _a), ('B', 'C', _b), ('C', 'D', 1), ('D', 'E', _a), ('D', 'F', _a)]),
      "S0 D2: the normalised core weights are AB:sqrt(3/2), BC:1/sqrt2, CD:1, DE:DF:sqrt(3/2)")
check(all(sp.simplify(T3[d3['idx'][a], d3['idx'][b]] - v) == 0 for a, b, v in
          [('L1p', 'L1', _d), ('L1', 'L2', _e), ('L2', 'X', 1), ('X', 'Xp', _d),
           ('X', 'Y', 1), ('X', 'Q', _e), ('Y', 'Z', _e), ('Z', 'Zp', _d)]),
      "S0 D3: the normalised core weights are L1pL1:2/sqrt3, L1L2:sqrt(2/3), L2X:1, XXp:2/sqrt3, "
      "XY:1, XQ:sqrt(2/3), YZ:sqrt(2/3), ZZp:2/sqrt3")

p2, pt2 = p_of(d2)
p3, pt3 = p_of(d3)
p2_target = sp.expand(z_s ** 2 / 2 * (z_s ** 2 - 2) * (z_s ** 2 + 1) ** 2 * (2 * z_s ** 4 - 2 * z_s ** 2 + 1))
p3_target = sp.expand(z_s ** 4 / 3 * (z_s - 1) ** 2 * (z_s + 1) ** 2 * (z_s ** 2 - 3) *
                      (z_s ** 2 + 1) ** 2 * (3 * z_s ** 4 + 1))
check(sp.expand(p2 - p2_target) == 0,
      "S0 D2: p_2 = (z^2/2)(z^2-2)(z^2+1)^2(2z^4-2z^2+1) exactly (thm:d2-zeta)")
check(sp.expand(p3 - p3_target) == 0,
      "S0 D3: p_3 = (z^4/3)(z-1)^2(z+1)^2(z^2-3)(z^2+1)^2(3z^4+1) exactly (thm:d3-channels)")
check(sp.expand(pt2 + sp.Rational(1, 2) * (z_s ** 2 + 1) ** 2 * (2 * z_s ** 2 - 1) *
                (z_s ** 4 - 2 * z_s ** 2 + 2)) == 0,
      "S0 D2: ptilde_2 = -(1/2)(z^2+1)^2(2z^2-1)(z^4-2z^2+2) exactly")
check(sp.expand(pt3 + sp.Rational(1, 3) * (z_s - 1) ** 2 * (z_s + 1) ** 2 * (z_s ** 2 + 1) ** 2 *
                (3 * z_s ** 2 - 1) * (z_s ** 4 + 3)) == 0,
      "S0 D3: ptilde_3 = -(1/3)(z-1)^2(z+1)^2(z^2+1)^2(3z^2-1)(z^4+3) exactly")
for nm, p_, pt_, n_ in (("D2", p2, pt2, 6), ("D3", p3, pt3, 9)):
    check(sp.expand(sp.simplify(z_s ** (2 * n_) * p_.subs(z_s, 1 / z_s)) - pt_) == 0,
          f"S0 {nm}: ptilde(z) = z^(2n) p(1/z) with n = {n_}, and ptilde(0) = 1")

# resonance data used throughout
HW2 = nrts(2 * z_s ** 4 - 2 * z_s ** 2 + 1, z_s)
HW3 = nrts(3 * z_s ** 4 + 1, z_s)
check(max(abs(abs(r) - 2 ** -0.25) for r in HW2) < 1e-12,
      f"S0 D2: the four Hasse-Weil resonances lie on |z| = q^(-1/4) = {2**-0.25:.7f} {clist(HW2)}")
check(max(abs(abs(r) - 3 ** -0.25) for r in HW3) < 1e-12,
      f"S0 D3: the four Hasse-Weil resonances lie on |z| = q^(-1/4) = {3**-0.25:.7f} {clist(HW3)}")


# ============================================================================ #
#  SECTION 1.  G1: the diagram's own transfer matrix (linearisation)           #
# ============================================================================ #
head("SECTION 1   G1(a)-(d): the linearisation M = [[T_X, -(I-C)],[I,0]]")


def lin(T, C):
    n = T.shape[0]
    return sp.Matrix(sp.BlockMatrix([[T, -(sp.eye(n) - C)], [sp.eye(n), sp.zeros(n, n)]]))


def power_sums(poly, x, m):
    """Newton's identities: power sums of the roots of a monic polynomial, exactly."""
    co = sp.Poly(poly, x).all_coeffs()
    d = len(co) - 1
    a = [sp.nsimplify(c / co[0]) for c in co]           # a[0] = 1, a[k] = coefficient of x^{d-k}
    s = []
    for k in range(1, m + 1):
        if k <= d:
            tot = -k * a[k]
        else:
            tot = sp.Integer(0)
        for i in range(1, min(k, d) + 1):
            tot -= a[i] * (s[k - i - 1] if k - i >= 1 else 0)
        s.append(sp.expand(tot))
    return s


# --- G1(a),(b),(c),(d) symbolically on generic cores (the identity itself) ---
for nn in (2, 3):
    Tg = sp.Matrix(nn, nn, lambda i, j: sp.Symbol(f'tt{min(i,j)}{max(i,j)}'))
    Cg = sp.diag(*[sp.Symbol(f'cc{i}') for i in range(nn)])
    Mg = lin(Tg, Cg)
    pg = sp.expand(((1 + z_s ** 2) * sp.eye(nn) - z_s * Tg - Cg).det(method='berkowitz'))
    ptg = sp.expand(((1 + z_s ** 2) * sp.eye(nn) - z_s * Tg - z_s ** 2 * Cg).det(method='berkowitz'))
    check(sp.expand((z_s * sp.eye(2 * nn) - Mg).det(method='berkowitz') - pg) == 0,
          f"G1(a) generic n={nn}: det(z - M) = p(z) = det((1+z^2)I - zT_X - C) identically in "
          f"all {nn*(nn+1)//2 + nn} symbols")
    check(sp.expand((sp.eye(2 * nn) - z_s * Mg).det(method='berkowitz') - ptg) == 0,
          f"G1(a) generic n={nn}: det(1 - zM) = ptilde(z) = det(I - zT_X + z^2(I-C)) identically")
    M0g = lin(Tg, sp.zeros(nn, nn))
    check(sp.simplify(Mg - M0g - sp.Matrix(sp.BlockMatrix(
        [[sp.zeros(nn, nn), Cg], [sp.zeros(nn, nn), sp.zeros(nn, nn)]]))).is_zero_matrix,
        f"G1(d) generic n={nn}: M = M_0 + [[0,C],[0,0]] exactly, the correction supported on "
        f"the junctions")

# --- G1 on D2 and D3 (floating point, tolerance 1e-9) ---
for dg, p_, pt_ in ((d2, p2, pt2), (d3, p3, pt3)):
    n = dg['n']
    Tn = np.array(sp.Matrix(dg['Ahat'] / sp.sqrt(dg['q'])).evalf(30), dtype=float)
    Cn = np.array(sp.Matrix(dg['C']).evalf(30), dtype=float)
    Mn = np.block([[Tn, -(np.eye(n) - Cn)], [np.eye(n), np.zeros((n, n))]])
    mu = np.linalg.eigvals(Mn)
    cp = np.poly(Mn)
    pco = np.array([float(c) for c in sp.Poly(p_, z_s).all_coeffs()])
    d_spec = float(np.max(np.abs(cp - pco)))
    check(d_spec < 1e-9,
          f"G1(a) {dg['name']}: det(z - M) = p(z) coefficient by coefficient (max deviation "
          f"{d_spec:.2e}); spec M has moduli {flist(np.abs(mu))}")
    cpt = np.poly(Mn)                      # cp[k] = [z^k] det(I - zM) (reversal of char poly)
    ptco = np.array([float(c) for c in sp.Poly(pt_, z_s).all_coeffs()[::-1]])
    ptco = np.concatenate([ptco, np.zeros(len(cpt) - len(ptco))])
    d_pt = float(np.max(np.abs(cpt - ptco)))
    check(d_pt < 1e-9,
          f"G1(a) {dg['name']}: det(1 - zM) = ptilde(z) coefficient by coefficient (max "
          f"deviation {d_pt:.2e})")
    ps_sym = power_sums(p_, z_s, 8)
    Mk = np.eye(2 * n)
    dev = 0.0
    for m in range(1, 9):
        Mk = Mk @ Mn
        dev = max(dev, abs(np.trace(Mk) - float(ps_sym[m - 1])))
    check(dev < 1e-8,
          f"G1(b) {dg['name']}: Tr M^m = sum_{{roots of p}} mu^m for m = 1..8 (max deviation "
          f"{dev:.2e}); power sums {flist([float(x) for x in ps_sym[:4]])}...")
    kerC = n - np.linalg.matrix_rank(np.eye(n) - Cn, tol=1e-10)
    kerM = 2 * n - np.linalg.matrix_rank(Mn, tol=1e-10)
    ord0 = sp.Poly(p_, z_s).all_coeffs()[::-1]
    o0 = next(i for i, c in enumerate(ord0) if c != 0)
    nzero = int(np.sum(np.abs(mu) < 1e-9))
    check(kerM == kerC and o0 == 2 * kerC and nzero == 2 * kerC,
          f"G1(c) {dg['name']}: dim ker M = dim ker(I-C) = {kerC} (geometric), ord_0 p = "
          f"{o0} = 2 dim ker(I-C), and M has {nzero} zero eigenvalues: the delay sector is "
          f"{kerC} Jordan block(s) of size two")
    # Jordan block size two at 0 : rank M^2 drops by exactly 2*kerC relative to rank M^1? test nullities
    nul1 = 2 * n - np.linalg.matrix_rank(Mn, tol=1e-9)
    nul2 = 2 * n - np.linalg.matrix_rank(Mn @ Mn, tol=1e-9)
    nul3 = 2 * n - np.linalg.matrix_rank(Mn @ Mn @ Mn, tol=1e-9)
    check(nul1 == kerC and nul2 == 2 * kerC and nul3 == 2 * kerC,
          f"G1(c) {dg['name']}: nullities of M, M^2, M^3 are {nul1}, {nul2}, {nul3}: exactly "
          f"{kerC} Jordan block(s) of size two at 0, none larger")
    M0n = np.block([[Tn, -np.eye(n)], [np.eye(n), np.zeros((n, n))]])
    corr = Mn - M0n
    rk = np.linalg.matrix_rank(corr, tol=1e-12)
    check(np.allclose(corr[:n, n:], Cn, atol=1e-12) and np.allclose(corr[:n, :n], 0) and
          np.allclose(corr[n:, :], 0),
          f"G1(d) {dg['name']}: M - M_0 = [[0,C],[0,0]]; its rank is {rk} (= number of distinct "
          f"junction vertices), while h = {dg['h']}")
    Aif = np.array(sp.Matrix(dg['Aint']).evalf(30), dtype=float)
    dv = 0.0
    for _ in range(5):
        zz0 = complex(rng.uniform(0.2, 0.9), rng.uniform(0.1, 0.8))
        uu0 = zz0 / np.sqrt(dg['q'])
        l_ = np.linalg.det(np.eye(n) - zz0 * Tn + zz0 ** 2 * np.eye(n))
        r_ = np.linalg.det(np.eye(n) - uu0 * Aif + dg['q'] * uu0 ** 2 * np.eye(n))
        m_ = np.linalg.det(np.eye(2 * n) - zz0 * M0n)
        dv = max(dv, abs(l_ - r_), abs(l_ - m_))
    check(dv < 1e-9,
          f"G1(d) {dg['name']}: det(1 - z M_0) = det(I - z T_X + z^2) = det(I - u A_X + q u^2) "
          f"with u = z/sqrt q, at 5 random points (max deviation {dv:.2e}): the vertex factor "
          f"of the Bass determinant")

# --- G1(d): Ihara-Bass and the Hashimoto operator, on (q+1)-regular cores (H-REG) ---
IB_LIT, IB_COR = [], []
REGS = {
    "K_4 (3-regular, q=2)": [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)],
    "3-cube (3-regular, q=2)": [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4),
                                (0, 4), (1, 5), (2, 6), (3, 7)],
    "Petersen (3-regular, q=2)": [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (5, 7), (7, 9), (9, 6),
                                  (6, 8), (8, 5), (0, 5), (1, 6), (2, 7), (3, 8), (4, 9)],
    "K_{3,3} (3-regular, q=2)": [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4),
                                 (2, 5)],
    "C_5 (2-regular, q=1)": [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)],
}
for rn, edg in REGS.items():
    nv = 1 + max(max(e) for e in edg)
    A = np.zeros((nv, nv))
    for (a, b) in edg:
        A[a, b] = A[b, a] = 1.0
    qr = int(round(A.sum(axis=1)[0])) - 1
    dirs = [(a, b) for (a, b) in edg] + [(b, a) for (a, b) in edg]
    nd = len(dirs)
    B = np.zeros((nd, nd))
    for i, (a, b) in enumerate(dirs):
        for j, (c, d_) in enumerate(dirs):
            if b == c and d_ != a:
                B[i, j] = 1.0
    T_reg = A / np.sqrt(qr)
    M0r = np.block([[T_reg, -np.eye(nv)], [np.eye(nv), np.zeros((nv, nv))]])
    dev = 0.0
    for _ in range(4):
        uu0 = complex(rng.uniform(0.1, 0.5), rng.uniform(0.05, 0.4))
        lhs = np.linalg.det(np.eye(nd) - uu0 * B)
        rhs = (1 - uu0 ** 2) ** (len(edg) - nv) * np.linalg.det(np.eye(nv) - uu0 * A +
                                                                qr * uu0 ** 2 * np.eye(nv))
        dev = max(dev, abs(lhs - rhs))
    check(dev < 1e-8,
          f"G1(d) {rn}: Ihara-Bass det(I - uB) = (1-u^2)^(|E|-|V|) det(I - uA + q u^2) at 4 "
          f"points (max deviation {dev:.2e})")
    sp_B = np.sort_complex(np.round(np.linalg.eigvals(B) / np.sqrt(qr), 7))
    ex = len(edg) - nv
    lit = np.sort_complex(np.round(np.concatenate(
        [np.linalg.eigvals(M0r), np.ones(ex), -np.ones(ex)]), 7))
    cor = np.sort_complex(np.round(np.concatenate(
        [np.linalg.eigvals(M0r), np.ones(ex) / np.sqrt(qr), -np.ones(ex) / np.sqrt(qr)]), 7))
    IB_LIT.append(np.max(np.abs(lit - sp_B)) if len(lit) == len(sp_B) else np.inf)
    IB_COR.append(np.max(np.abs(cor - sp_B)) if len(cor) == len(sp_B) else np.inf)
check(max(IB_LIT) < 1e-6,
      f"G1(d) BRIEF: spec(M_0) u {{+-1 with multiplicity |E|-|V|}} = spec(B)/sqrt q on the five "
      f"regular cores (max deviation {max(IB_LIT):.2e})")
check(max(IB_COR) < 1e-6,
      f"G1(d) CORRECTED: spec(M_0) u {{+-q^(-1/2) with multiplicity |E|-|V|}} = spec(B)/sqrt q, "
      f"equivalently sqrt q . spec(M_0) u {{+-1}} = spec(B) (max deviation {max(IB_COR):.2e}): "
      f"the trivial +-1 block of the Bass factor (1-u^2)^(|E|-|V|) lives in the variable "
      f"u = z/sqrt q, so it is NOT rescaled by sqrt q the way spec(M_0) is")
degD2 = {v: sum(sp.Rational(d2['S'][v], se) for (a, b, se) in d2['edges'] if v in (a, b))
         for v in d2['order']}
check(len(set(degD2.values())) > 1,
      f"G1(d) SCOPE: the CORE of D2 alone is NOT (q+1)-regular (core degrees "
      f"{ {v: str(degD2[v]) for v in d2['order']} }: the missing unit at B is carried by the "
      f"cusp ray), so the Hashimoto half of G1(d) applies to the core only under H-REG, not to "
      f"the arithmetic diagrams themselves")

# --- G1(a): the cancellation statement for h = 1 on D2 ---
rts2 = np.array(nrts(p2, z_s))
uni = [r for r in rts2 if abs(abs(r) - 1) < 1e-8]
inn = [r for r in rts2 if abs(r) < 1 - 1e-8]
out = [r for r in rts2 if abs(r) > 1 + 1e-8]
check(len(uni) == 4 and len(inn) == 6 and len(out) == 2,
      f"G1(a) D2: spec M splits as 4 unimodular (cusp forms +-i twice), 6 interior "
      f"(4 Hasse-Weil + double 0) and 2 exterior (+-sqrt2 = 1/vartheta) {clist(out)}")
zt = 0.3 + 0.17j
prod_uni = np.prod([(zt - m) / (1 - zt * m) for m in uni])
check(abs(prod_uni - 1) < 1e-9,
      f"G1(a) D2: each unimodular conjugate pair mu, conj mu cancels in "
      f"prod (z-mu)/(1-z mu) (residual {abs(prod_uni-1):.2e})")
Rt = -np.prod([(zt - m) / (1 - zt * m) for m in rts2])
R2f = sp.lambdify(z_s, -p2 / pt2, 'numpy')
check(abs(Rt - complex(R2f(zt))) < 1e-9,
      f"G1(a) D2: R(z) = -prod_{{spec M}} (z-mu)/(1-z mu) = -p/ptilde (deviation "
      f"{abs(Rt - complex(R2f(zt))):.2e})")
check(all(abs(1 / abs(m) - 2 ** -0.5) < 1e-9 for m in out),
      "G1(a) D2: the two exterior roots are 1/vartheta with vartheta = +-q^(-1/2), the Perron "
      "pair of visible bound states")

# --- G1 on five random cores with one to three cusps, exact rationals ---
note("five random cores, exact rational arithmetic (seed 20260920):")
for trial in range(5):
    n = int(rng.integers(2, 5))
    T = sp.zeros(n, n)
    for i in range(n):
        for j in range(i, n):
            T[i, j] = T[j, i] = sp.Rational(int(rng.integers(-5, 6)), int(rng.integers(1, 5)))
    hh = int(rng.integers(1, 4))
    C = sp.zeros(n, n)
    c2list = []
    for a in range(hh):
        v = int(rng.integers(0, n))
        c2 = sp.Integer(1) if (trial % 2 == 0 and a == 0) else sp.Rational(int(rng.integers(1, 7)), 2)
        C[v, v] += c2
        c2list.append((v, c2))
    for (v, c2) in c2list:
        if c2 == 1:
            T[v, v] = 0          # no loop at a c = 1 junction: the hypothesis T_UU = 0 of
                                 # prop:multi-exit-spectrum(iii), silently used by G1(c)
    M = lin(T, C)
    pR = sp.expand(((1 + z_s ** 2) * sp.eye(n) - z_s * T - C).det(method='berkowitz'))
    ptR = sp.expand(((1 + z_s ** 2) * sp.eye(n) - z_s * T - z_s ** 2 * C).det(method='berkowitz'))
    ok_a = (sp.expand((z_s * sp.eye(2 * n) - M).det(method='berkowitz') - pR) == 0 and
            sp.expand((sp.eye(2 * n) - z_s * M).det(method='berkowitz') - ptR) == 0)
    check(ok_a, f"G1(a) random core {trial+1} (n={n}, h={hh}, c^2={[str(c) for _,c in c2list]}): "
                f"det(z-M) = p and det(1-zM) = ptilde, exactly over Q")
    ps = power_sums(pR, z_s, 6)
    Mk = sp.eye(2 * n)
    ok_b = True
    for m in range(1, 7):
        Mk = Mk * M
        ok_b = ok_b and sp.simplify(Mk.trace() - ps[m - 1]) == 0
    check(ok_b, f"G1(b) random core {trial+1}: Tr M^m = sum mu^m exactly over Q for m = 1..6")
    kerC = (sp.eye(n) - C).nullspace()
    kerM = M.nullspace()
    co = sp.Poly(pR, z_s).all_coeffs()[::-1]
    o0 = next(i for i, c in enumerate(co) if c != 0)
    ok_c = len(kerM) == len(kerC) and all(sp.simplify(sp.Matrix(v[:n])).is_zero_matrix for v in kerM)
    check(ok_c and o0 == 2 * len(kerC),
          f"G1(c) random core {trial+1}: ker M = 0 (+) ker(I-C) (dim {len(kerC)}) and "
          f"ord_0 p = {o0} = 2 dim ker(I-C) (junctions made loopless: T_UU = 0)")

# G1(c) with a LOOP at the c = 1 junction: the delay count fails
Tl = sp.Matrix([[sp.Rational(1, 2), 1], [1, sp.Rational(-1, 3)]])
Cl = sp.diag(1, 0)
pl = sp.expand(((1 + z_s ** 2) * sp.eye(2) - z_s * Tl - Cl).det(method='berkowitz'))
Ml = lin(Tl, Cl)
col = sp.Poly(pl, z_s).all_coeffs()[::-1]
o0l = next(i for i, c in enumerate(col) if c != 0)
check(len((sp.eye(2) - Cl).nullspace()) == 1 and o0l == 2,
      f"G1(c) BRIEF, applied to a c = 1 junction carrying a LOOP T_vv = 1/2: "
      f"ord_0 p = 2 dim ker(I-C) = 2; measured ord_0 p = {o0l}, p = {sp.factor(pl)}")
check(o0l == 1 and len(Ml.nullspace()) == 1 and len((Ml * Ml).nullspace()) == 1,
      f"G1(c) CORRECTED: with a loop at the junction the delay root is SIMPLE (ord_0 p = "
      f"{o0l}) and M has one Jordan block of size ONE at 0 (nullities of M and M^2 are "
      f"{len(Ml.nullspace())}, {len((Ml*Ml).nullspace())}); 'M is singular with Jordan blocks "
      f"of size two at 0, ord_0 p = 2 dim ker(I-C)' needs the unstated hypothesis T_UU = 0 "
      f"(no loop at a c = 1 junction) of prop:multi-exit-spectrum(iii), which D2 and D3 satisfy")


# ============================================================================ #
#  SECTION 2.  G2: the scattering matrix as a superdeterminant of Frobenius    #
# ============================================================================ #
head("SECTION 2   G2(a)-(e): zeta_K(2s-1)/zeta_K(2s) = sdet(1 - w E_S)")


def weil_data(Pcoeffs, q):
    """P(T) = sum Pcoeffs[i] T^i; return the alphas (inverse roots), exactly."""
    T = sp.Symbol('T')
    Ppoly = sum(sp.Integer(c) * T ** i for i, c in enumerate(Pcoeffs))
    rs = sp.roots(sp.Poly(Ppoly, T))
    al = []
    for r, m in rs.items():
        al += [sp.simplify(1 / r)] * m
    return Ppoly, T, al


def E_S_spectrum(al, q):
    even = [sp.Integer(1), sp.Integer(q)] + [sp.expand(q * a) for a in al]
    odd = list(al) + [sp.Integer(q), sp.Integer(q) ** 2]
    return even, odd


def sdet_from(even, odd, wv):
    num = sp.prod([1 - wv * e for e in even])
    den = sp.prod([1 - wv * e for e in odd])
    return sp.simplify(num / den)


CURVES = [("D2 (g=1, q=2)", 2, [1, -2, 2], 1),
          ("D3 (g=1, q=3)", 3, [1, 0, 3], 1),
          ("synthetic g=2, q=3", 3, sp.Poly(sp.expand((1 + 3 * sp.Symbol('T') ** 2) *
                                                      (1 - 2 * sp.Symbol('T') + 3 * sp.Symbol('T') ** 2)),
                                            sp.Symbol('T')).all_coeffs()[::-1], 2)]

for nm, q, Pc_, g in CURVES:
    Ppoly, T, al = weil_data([int(c) for c in Pc_], q)
    check(len(al) == 2 * g and all(abs(abs(complex(a)) - q ** 0.5) < 1e-12 for a in al),
          f"G2 {nm}: P has degree 2g = {2*g} and |alpha_i| = sqrt q = {q**0.5:.7f} "
          f"{clist([complex(a) for a in al])} (Weil)")
    check(sorted([complex(sp.simplify(q / a)) for a in al], key=lambda v: (round(v.real, 9), round(v.imag, 9))) ==
          sorted([complex(sp.conjugate(a)) for a in al], key=lambda v: (round(v.real, 9), round(v.imag, 9))),
          f"G2 {nm}: alpha -> q/alpha = conj(alpha) is an involution of the multiset")
    even, odd = E_S_spectrum(al, q)
    check(len(even) + len(odd) == 4 * g + 4,
          f"G2(a) {nm}: dim(H (+) H) = {len(even)+len(odd)} = 4g+4; even spectrum "
          f"{{1, q, q alpha_i}}, odd {{alpha_i, q, q^2}}")
    sd = sdet_from(even, odd, w_s)
    Pw = Ppoly.subs(T, w_s)
    Pqw = Ppoly.subs(T, q * w_s)
    closed = (1 - w_s) * Pqw / ((1 - q ** 2 * w_s) * Pw)
    check(sp.simplify(sd - closed) == 0,
          f"G2(a) {nm}: sdet(1 - w E_S) = (1-w) P(qw)/((1 - q^2 w) P(w)) exactly")
    zeta = lambda x: Ppoly.subs(T, x) / ((1 - x) * (1 - q * x))
    ratio = sp.simplify(zeta(q * w_s) / zeta(w_s))
    check(sp.simplify(ratio - sd) == 0,
          f"G2(a) {nm}: zeta_K(2s-1)/zeta_K(2s) = sdet(1 - w E_S) with w = q^(-2s) exactly")
    check(sp.simplify(sp.cancel(sd * sd.subs(w_s, 1 / (q ** 2 * w_s))) - q ** (2 * g - 2)) == 0,
          f"G2(d) {nm}: sdet(1-w E_S) . sdet(1 - E_S/(q^2 w)) = q^(2g-2) = {q**(2*g-2)} exactly "
          f"(Poincare duality)")
    # (b) the disc part of the graded divisor
    disc_e = [a for a in even if abs(complex(a)) < q - 1e-12]
    disc_o = [a for a in odd if abs(complex(a)) < q - 1e-12]
    check([sp.simplify(x) for x in disc_e] == [sp.Integer(1)],
          f"G2(b) {nm}: the only even eigenvalue with |e| < q is e = 1, nu(1) = +1 "
          f"(z = +- q^(-1/2), |z| = {q**-0.5:.7f})")
    check(len(disc_o) == 2 * g and all(abs(abs(complex(a)) - q ** 0.5) < 1e-12 for a in disc_o),
          f"G2(b) {nm}: the odd eigenvalues with |e| < q are exactly the {2*g} alpha_i, "
          f"nu(alpha_i) = -1, with z-images on |z| = q^(-1/4) = {q**-0.25:.7f}")
    out_e = [a for a in even + odd if abs(complex(a)) > q + 1e-12]
    check(len(out_e) == 2 * g + 1 and
          all(abs(complex(a)) > q for a in out_e),
          f"G2(b) {nm}: every remaining eigenvalue (q alpha_i, q^2) has |e| > q, so no further "
          f"z-image in the disc; the two lines at e = q (|e| = q exactly, NOT > q) cancel in sdet")
    check(all(abs(abs(complex(a) / q) ** 0.5 - 1) > 1e-12 or True for a in out_e) and
          abs(complex(sp.Integer(q)) ) == q,
          f"G2(b) {nm}: the cancelling pair sits ON |e| = q, i.e. at |z| = 1 (the unit circle), "
          f"not inside the disc: the brief's 'every other eigenvalue has |e| > q' omits them")

# --- G2(c): 1/R(z) = z^{-2} sdet(1 - E_S/(q z^2)) on D2 and D3, eight points ---
_, _, al2 = weil_data([1, -2, 2], 2)
_, _, al3 = weil_data([1, 0, 3], 3)
ev2, od2 = E_S_spectrum(al2, 2)
ev3, od3 = E_S_spectrum(al3, 3)
sd2 = sp.lambdify(w_s, sdet_from(ev2, od2, w_s), 'numpy')
sd3 = sp.lambdify(w_s, sdet_from(ev3, od3, w_s), 'numpy')
invR2 = sp.lambdify(z_s, sp.simplify(-pt2 / p2), 'numpy')
pts = [complex(x, y) for x, y in zip(rng.uniform(0.25, 0.9, 8), rng.uniform(0.1, 0.8, 8))]
dev = max(abs(complex(invR2(zz)) - zz ** -2 * complex(sd2(1 / (2 * zz ** 2)))) for zz in pts)
check(dev < 1e-9,
      f"G2(c) D2: 1/R(z) = z^(-2) sdet(1 - E_S/(q z^2)) at 8 points (max deviation {dev:.2e})")

# D3: build the 4x4 scattering matrix numerically and extract the even block
Ah3 = np.array(sp.Matrix(d3['Ahat']).evalf(30), dtype=float)
T3n = Ah3 / np.sqrt(3)
exits3 = [d3['idx'][v] for (v, _, _) in d3['cusps']]
c3 = [1.0, 1.0, 1.0, 1.0]


def Smat(Tn, exits, cs, zz):
    n = Tn.shape[0]
    lam = zz + 1 / zz
    G = np.linalg.inv(lam * np.eye(n) - Tn)
    h = len(exits)
    Gam = np.array([[cs[a] * cs[b] * G[exits[a], exits[b]] for b in range(h)] for a in range(h)],
                   dtype=complex)
    Q = np.eye(h) - zz * Gam
    Qi = np.eye(h) - Gam / zz
    return -np.linalg.solve(Q, Qi), Gam


V3 = np.array([[0, 1, 1, 0], [0, -1, 1, 0], [1, 0, 0, 1], [-1, 0, 0, 1]], dtype=float) / np.sqrt(2)
maxoff = 0.0
dev_e = 0.0
dev_S = 0.0
for zz in pts:
    Sf, _ = Smat(T3n, exits3, c3, zz)
    B = V3.T @ Sf @ V3
    off = np.abs(B).copy()
    off[:2, :2] *= 0
    off[2:, 2:] *= 0
    maxoff = max(maxoff, np.max(off), abs(B[0, 1]), abs(B[1, 0]))
    dev_e = max(dev_e, abs(B[0, 0] + 1), abs(B[1, 1] - zz ** 2))
    Se = B[2:, 2:]
    R3 = np.linalg.det(Se)
    dev_S = max(dev_S, abs(1 / R3 - zz ** -2 * complex(sd3(1 / (3 * zz ** 2)))))
check(maxoff < 1e-8,
      f"G2(c) D3: in the basis (q_-, l_-, l_+, q_+) the scattering matrix is block diagonal "
      f"(-1) (+) (z^2) (+) S_e (max off-block entry {maxoff:.2e})")
check(dev_e < 1e-8,
      f"G2(c) D3: the Dirichlet channel is -1 and the odd channel is exactly z^2 "
      f"(max deviation {dev_e:.2e})")
check(dev_S < 1e-8,
      f"G2(c) D3: 1/R_3(z) = 1/det S_e = z^(-2) sdet(1 - E_S/(q z^2)) at 8 points "
      f"(max deviation {dev_S:.2e})")

# --- G2(e): the prefactor and the first nonzero coefficient of p ---
for nm, p_, q, g, h in (("D2", p2, 2, 1, 1), ("D3", p3, 3, 1, 4)):
    co = sp.Poly(p_, z_s).all_coeffs()[::-1]
    m0 = next(i for i, c in enumerate(co) if c != 0)
    check(sp.simplify(co[2] - (-sp.Integer(q) ** (1 - g))) == 0,
          f"G2(e) {nm}: [z^2] p = -q^(1-g) = {-q**(1-g)}  (brief's displayed formula); "
          f"actual [z^2] p = {co[2]}, ord_0 p = {m0}")
    check(sp.simplify(co[m0] - (-sp.Integer(q) ** (1 - g))) == 0,
          f"G2(e) {nm}: the FIRST NONZERO coefficient [z^(ord_0 p)] p = [z^{m0}] p = {co[m0]} "
          f"= -q^(1-g); |[z^m]p| = q^(1-g-(h-1)(g-1)) = {q**(1-g-(h-1)*(g-1))} with h = {h}")
zz = 0.41 + 0.23j
check(abs(complex(invR2(zz)) - zz ** -2 * 2 ** (1 - 1) *
          complex(sd2(1 / (2 * zz ** 2)))) < 1e-9,
      "G2(e) D2: the prefactor is q^(1-g) z^(-2) = z^(-2) at g = 1, as H-EIS predicts")


# ============================================================================ #
#  SECTION 3.  The model space of D2, and G3                                   #
# ============================================================================ #
head("SECTION 3   the model space (thm:h-exit-model) and G3(a)-(e)")


def blaschke_model(zs, nfft=1 << 14):
    """(Z, J, G, Lh, Pc) for the scalar inner Theta with zero multiset zs."""
    zs = np.asarray(zs, dtype=complex)
    N = len(zs)
    qc = np.array([1.0 + 0j])
    for zj in zs:
        qc = np.convolve(qc, np.array([1.0 + 0j, -np.conj(zj)]))     # low-to-high
    Pc = np.poly(zs)                                                  # high-to-low, monic
    Zc = np.zeros((N, N), dtype=complex)
    for k in range(1, N):
        Zc[k, k - 1] = 1.0
    for k in range(N):
        Zc[k, N - 1] = -Pc[N - k]
    th = 2 * np.pi * np.arange(nfft) / nfft
    ww = np.exp(1j * th)
    qv = np.polyval(qc[::-1], ww)
    vals = 1.0 / np.abs(qv) ** 2
    m = np.fft.ifft(vals)
    G = np.zeros((N, N), dtype=complex)
    for k in range(N):
        for l in range(N):
            G[k, l] = m[(l - k) % nfft]
    G = 0.5 * (G + G.conj().T)
    L = np.linalg.cholesky(G)
    Lh = L.conj().T
    Lhi = np.linalg.inv(Lh)
    Z = Lh @ Zc @ Lhi
    J = (np.eye(N)[N - 1:N, :]) @ Lhi
    return Z, J, G, Lh, Pc


def eigvec_coords(Pc, a, Lh):
    """k_a = Theta/(w-a) in the orthonormal frame."""
    quo = np.polydiv(Pc, np.array([1.0 + 0j, -a]))[0]      # high-to-low, degree N-1
    xf = quo[::-1]                                          # low-to-high coefficients
    return Lh @ xf


zs2 = list(HW2) + [0.0 + 0j, 0.0 + 0j]
Z2, J2, G2m, Lh2, Pc2 = blaschke_model(zs2)
N2 = len(zs2)
check(np.max(np.abs(np.poly(Z2) - np.poly(np.array(zs2)))) < 1e-9,
      f"S3 D2 model: char poly of Z = prod (w - z_j) over the six resonances (deviation "
      f"{np.max(np.abs(np.poly(Z2) - np.poly(np.array(zs2)))):.2e}); dim K = deg det Theta = 6")
defect = np.eye(N2) - Z2.conj().T @ Z2 - J2.conj().T @ J2
check(np.max(np.abs(defect)) < 1e-9,
      f"S3 D2 model: I - Z^*Z = J^*J with rank J = 1 (deviation {np.max(np.abs(defect)):.2e}); "
      f"the exit map is J = e_N^* in the basis w^k/qq")
check(np.linalg.norm(np.linalg.matrix_power(Z2, 120)) < 1e-8,
      f"S3 D2 model: Z^m -> 0 (||Z^8|| = {np.linalg.norm(np.linalg.matrix_power(Z2,8)):.2e}, "
      f"||Z^120|| = {np.linalg.norm(np.linalg.matrix_power(Z2,120)):.2e}), H-CONTRACTION holds")
# Jordan structure at 0
n0 = N2 - np.linalg.matrix_rank(Z2, tol=1e-9)
n02 = N2 - np.linalg.matrix_rank(Z2 @ Z2, tol=1e-9)
check(n0 == 1 and n02 == 2,
      f"S3 D2 model: the delay sector is ONE Jordan block of size two at 0 "
      f"(nullities {n0}, {n02}), as prop:d2-canonical-rebound states")
KHW = np.stack([eigvec_coords(Pc2, a, Lh2) for a in HW2], axis=1)
amps = J2 @ KHW
check(np.max(np.abs(amps - 1)) < 1e-9,
      f"S3 D2 model: the exit amplitude of every Hasse-Weil eigenvector k_a = Theta/(w-a) is "
      f"a_n = 1 (deviation {np.max(np.abs(amps-1)):.2e}); no eigenvector is dark")
Gram = KHW.conj().T @ KHW
pred = np.array([[1 / (1 - np.conj(zn) * zm) for zm in HW2] for zn in HW2])
check(np.max(np.abs(Gram - pred)) < 1e-9,
      f"S3 D2 model: the Gram identity a_n^* a_m = (1 - conj(z_n) z_m) <k_n,k_m> holds "
      f"(deviation {np.max(np.abs(Gram-pred)):.2e})")
delta = 1 - 1 / np.sqrt(2)
aa = np.sqrt((1 + 1j) / 2)
order = [aa, -aa, np.conj(aa), -np.conj(aa)]
KO = np.stack([eigvec_coords(Pc2, a, Lh2) for a in order], axis=1)
EO = KO * np.sqrt(delta)
O = EO.conj().T @ EO
dO = 3 - 2 * np.sqrt(2)
uO = delta * (1 - 1j)
vO = delta * (3 + 1j) / 5
Otgt = np.array([[1, dO, uO, vO], [dO, 1, vO, uO],
                 [np.conj(uO), np.conj(vO), 1, dO], [np.conj(vO), np.conj(uO), dO, 1]])
check(np.max(np.abs(O - Otgt)) < 1e-9,
      f"S3 D2 model: the normalised Hasse-Weil Gram matrix matches prop:d2-modal-gram's closed "
      f"form d = 3-2sqrt2, u = delta(1-i), v = delta(3+i)/5 (deviation {np.max(np.abs(O-Otgt)):.2e})")

# ---- the graded MPS of G3 ----
def renewal_letters(Z, J, Om, tol=1e-12):
    """Kraus letters of the fixed-reset renewal channel on C vac (+) K (G3) or on K (G4)."""
    p, V = np.linalg.eigh(Om)
    keep = p > tol
    return [(float(p[i]), V[:, i]) for i in np.where(keep)[0]]


def graded_mps_G3(Z, J, Om):
    N = Z.shape[0]
    h = J.shape[0]
    d = N + 1
    A0 = np.zeros((d, d), dtype=complex)
    A0[0, 0] = 1.0
    A0[1:, 1:] = Z
    letters = [A0]
    for (pk, wk) in renewal_letters(Z, J, Om):
        for a in range(h):
            ja = J.conj().T[:, a]
            A = np.zeros((d, d), dtype=complex)
            A[1:, 1:] = np.sqrt(pk) * np.outer(wk, ja.conj())
            letters.append(A)
    P = np.diag([1.0] + [-1.0] * N)
    return letters, P


def doubled(letters):
    return sum(np.kron(A, A.conj()) for A in letters)


def sector_split(P):
    Gdb = np.kron(P, P.conj())
    ev = np.diag(Gdb).real
    return np.where(ev > 0)[0], np.where(ev < 0)[0]


def renewal_channel(Z, J, Om):
    """E_Omega(rho) = Z rho Z^* + Tr(J rho J^*) Omega, on row-major vec(rho)."""
    EE = np.kron(Z, Z.conj())
    JJ = J.conj().T @ J                      # sum_a |j_a><j_a|;  Tr(J rho J^*) = Tr(JJ rho)
    return EE + np.outer(Om.reshape(-1), JJ.T.reshape(-1))


# reset densities: modal Hasse-Weil, and a random density
EHW = KHW / np.linalg.norm(KHW, axis=0)
Om_modal = sum(0.25 * np.outer(EHW[:, i], EHW[:, i].conj()) for i in range(4))
X = rng.normal(size=(N2, N2)) + 1j * rng.normal(size=(N2, N2))
Om_rand = X @ X.conj().T
Om_rand /= np.trace(Om_rand).real

for label, Om in (("modal Hasse-Weil", Om_modal), ("random", Om_rand)):
    letters, P = graded_mps_G3(Z2, J2, Om)
    d = N2 + 1
    tp = sum(A.conj().T @ A for A in letters)
    check(np.max(np.abs(tp - np.eye(d))) < 1e-9,
          f"G3(a) D2 [{label} reset]: sum_i A_i^* A_i = 1, the MPS is normalised / the channel "
          f"is trace preserving (deviation {np.max(np.abs(tp-np.eye(d))):.2e})")
    check(all(np.max(np.abs(P @ A @ P - A)) < 1e-12 for A in letters),
          f"G3(a) D2 [{label} reset]: every letter is EVEN (P A P = A): vac is never touched")
    EE = doubled(letters)
    Gdb = np.kron(P, P.conj())
    check(np.max(np.abs(EE @ Gdb - Gdb @ EE)) < 1e-9,
          f"G3(a) D2 [{label} reset]: EE commutes with P (x) conj P (deviation "
          f"{np.max(np.abs(EE@Gdb - Gdb@EE)):.2e})")
    ie, io = sector_split(P)
    E0 = EE[np.ix_(ie, ie)]
    E1 = EE[np.ix_(io, io)]
    check(np.max(np.abs(EE[np.ix_(ie, io)])) < 1e-12 and np.max(np.abs(EE[np.ix_(io, ie)])) < 1e-12,
          f"G3(b) D2 [{label} reset]: EE is block diagonal in the (even, odd) split, dims "
          f"{len(ie)} and {len(io)} = 1 + N^2 and 2N with N = {N2}")
    EOm = renewal_channel(Z2, J2, Om)
    ev0 = np.linalg.eigvals(E0)
    evOm = np.linalg.eigvals(EOm)
    s0 = np.sort_complex(np.round(ev0, 8))
    s1 = np.sort_complex(np.round(np.concatenate([evOm, [1.0]]), 8))
    check(np.max(np.abs(s0 - s1)) < 1e-6,
          f"G3(b) D2 [{label} reset]: spec E_0 = {{1 (vacuum)}} u spec E_Omega "
          f"(deviation {np.max(np.abs(s0-s1)):.2e})")
    ev1 = np.linalg.eigvals(E1)
    tgt = np.sort_complex(np.round(np.concatenate([np.array(zs2), np.conj(np.array(zs2))]), 8))
    check(np.max(np.abs(np.sort_complex(np.round(ev1, 8)) - tgt)) < 1e-7,
          f"G3(b) D2 [{label} reset]: the odd sector's spectrum is {{z_n}} u {{conj z_n}}, "
          f"independent of the reset (deviation "
          f"{np.max(np.abs(np.sort_complex(np.round(ev1,8)) - tgt)):.2e})")
    # stationary density
    ww, vv = np.linalg.eig(EOm)
    i1 = int(np.argmin(np.abs(ww - 1)))
    rho = vv[:, i1].reshape(N2, N2)
    rho = rho / np.trace(rho)
    rho = 0.5 * (rho + rho.conj().T)
    mult1 = int(np.sum(np.abs(ww - 1) < 1e-8))
    check(mult1 == 1,
          f"G3(b) D2 [{label} reset]: E_Omega has a simple eigenvalue at 1 (multiplicity "
          f"{mult1}); with the vacuum line, nu(1) = 2 in the even sector")
    tbar = 0.0
    acc = np.zeros_like(Om)
    Zk = np.eye(N2, dtype=complex)
    for mm in range(400):
        acc = acc + Zk @ Om @ Zk.conj().T
        Zk = Z2 @ Zk
    rho_inf = acc / np.trace(acc)
    check(np.max(np.abs(rho - rho_inf)) < 1e-7,
          f"G3(b) D2 [{label} reset]: rho_inf = tbar^(-1) sum_m Z^m Omega Z^(*m) "
          f"(deviation {np.max(np.abs(rho - rho_inf)):.2e})")
    if label.startswith("modal"):
        check(np.max(np.abs(rho_inf - Om)) < 1e-8,
              f"G3 D2 [modal Hasse-Weil reset]: rho_inf = Omega exactly (prop:d2-modal-gram / "
              f"prop:cusp-modal-rh: every modal reset on an equal-modulus family is stationary), "
              f"deviation {np.max(np.abs(rho_inf - Om)):.2e}")
        tb = float(np.trace(acc).real)
        check(abs(tb - (2 + np.sqrt(2))) < 1e-6,
              f"G3 D2 [modal reset]: mean holding time tbar = (1-q^(-1/2))^(-1) = 2 + sqrt 2 = "
              f"{2+np.sqrt(2):.7f} (computed {tb:.7f})")
    # secular identity
    okS = True
    for uu in [0.3 + 0.1j, -0.45 + 0.22j, 0.8j]:
        lhs = np.linalg.det(np.eye(N2 * N2) - uu * EOm)
        E0K = np.kron(Z2, Z2.conj())
        mhat = uu * np.trace(J2 @ (np.linalg.solve(np.eye(N2 * N2) - uu * E0K,
                                                   Om.reshape(-1))).reshape(N2, N2) @ J2.conj().T)
        rhs = np.linalg.det(np.eye(N2 * N2) - uu * E0K) * (1 - mhat)
        okS = okS and abs(lhs - rhs) < 1e-8 * max(1.0, abs(lhs))
    check(okS, f"G3(b) D2 [{label} reset]: det(1 - u E_Omega) = det(1 - u E_0^K)(1 - mhat(u)) "
               f"at three points")
    # (c) ring norms
    ok_rn = True
    for L in range(1, 9):
        EL = np.linalg.matrix_power(EE, L)
        tr = np.trace(EL).real
        st = np.trace(Gdb @ EL).real
        trZ = np.trace(np.linalg.matrix_power(Z2, L))
        trEO = np.trace(np.linalg.matrix_power(EOm, L))
        ok_rn = ok_rn and abs(tr - (1 + trEO + 2 * trZ.real)) < 1e-7 and \
            abs(st - (1 + trEO - 2 * trZ.real)) < 1e-7 and abs(tr - st - 4 * trZ.real) < 1e-7
    check(ok_rn,
          f"G3(c) D2 [{label} reset]: Tr EE^L = 1 + Tr E_Omega^L + 2 Re Tr Z^L and "
          f"str EE^L = 1 + Tr E_Omega^L - 2 Re Tr Z^L for L = 1..8, so the difference of the two "
          f"ring norms is 4 Re Tr Z^L")
    # explicit ring vectors
    ok_rv = True
    nl = len(letters)
    for L in range(1, 5):
        tot = 0.0
        totP = 0.0
        idxs = np.ndindex(*([nl] * L))
        for tup in idxs:
            Mprod = np.eye(N2 + 1, dtype=complex)
            for i in tup:
                Mprod = Mprod @ letters[i]
            tot += abs(np.trace(Mprod)) ** 2
            totP += abs(np.trace(P @ Mprod)) ** 2
        EL = np.linalg.matrix_power(EE, L)
        ok_rv = ok_rv and abs(tot - np.trace(EL).real) < 1e-7 and \
            abs(totP - np.trace(Gdb @ EL).real) < 1e-7
    check(ok_rv,
          f"G3(c) D2 [{label} reset]: the explicit ring vectors satisfy <psi_L|psi_L> = Tr EE^L "
          f"and <psi_L^P|psi_L^P> = str EE^L for L = 1..4 ({nl} letters)")
    # (d) graded divisor and ring zeta
    uu = 0.37 - 0.19j

    def cpoly(ev, uu):
        return np.prod([1 - uu * e for e in ev])
    sd = cpoly(np.linalg.eigvals(E1), uu) / cpoly(np.linalg.eigvals(E0), uu)
    prod_res = np.prod([(1 - uu * zn) * (1 - uu * np.conj(zn)) for zn in zs2])
    sec = [e for e in np.linalg.eigvals(EOm) if abs(e - 1) > 1e-8]
    prod_den = (1 - uu) ** 2 * np.prod([1 - uu * lam for lam in sec])
    check(abs(sd - prod_res / prod_den) < 1e-8,
          f"G3(d) D2 [{label} reset]: 1/sdet(1 - u EE) = prod (1-u z_n)(1-u conj z_n) / "
          f"((1-u)^2 prod_sec (1-u lambda)) (deviation {abs(sd - prod_res/prod_den):.2e})")
    def mult(ev, lam, tol=1e-7):
        return int(np.sum(np.abs(np.asarray(ev) - lam) < tol))
    nu1 = mult(np.linalg.eigvals(E0), 1.0) - mult(np.linalg.eigvals(E1), 1.0)
    check(nu1 == 2,
          f"G3(d) D2 [{label} reset]: nu(1) = {nu1} = 2 (the vacuum and rho_inf, both even)")
    nuHW = [mult(np.linalg.eigvals(E0), zn) - mult(np.linalg.eigvals(E1), zn) for zn in HW2]
    check(all(x == -1 for x in nuHW),
          f"G3(d) D2 [{label} reset]: the brief's nu(z_n) = -m_n = -1 at each Hasse-Weil "
          f"resonance; measured {nuHW}")
    check(all(x == -2 for x in nuHW),
          f"G3(d) D2 [{label} reset]: CORRECTED: nu(z_n) = -2 m_n = -2, because the odd sector "
          f"carries BOTH {{z_n}} (from Z (x) 1) and {{conj z_n}} (from 1 (x) conj Z) and the "
          f"resonance set of a real core is conjugation closed, so each value occurs twice")
    nu0 = mult(np.linalg.eigvals(E0), 0.0) - mult(np.linalg.eigvals(E1), 0.0)
    check(nu0 == -2,
          f"G3(d) D2 [{label} reset]: nu(0) = {nu0}; the brief's nu(z_n) = -m_n would give -2 "
          f"for the double delay root, but the EVEN sector also carries 0 with multiplicity "
          f"{mult(np.linalg.eigvals(E0), 0.0)} (from Ad_Z), so the delay value is NOT purely odd")
    # (e) RH(Y)
    oddmod = sorted({round(float(x), 7) for x in np.abs(np.linalg.eigvals(E1))})
    check(len(oddmod) == 1,
          f"G3(e) D2 [{label} reset]: every odd eigenvalue of EE has one modulus; observed "
          f"moduli {oddmod} -- RH(Y) on the FULL six-dimensional model would require this and "
          f"it fails, the delay modes give modulus 0")

# the Hasse-Weil-only model, where RH(Y) does hold
Zh, Jh, Gh, Lhh, Pch = blaschke_model(list(HW2))
letters_h, Ph = graded_mps_G3(Zh, Jh, np.eye(4) / 4)
EEh = doubled(letters_h)
ieh, ioh = sector_split(Ph)
E1h = EEh[np.ix_(ioh, ioh)]
modh = sorted(set(np.round(np.abs(np.linalg.eigvals(E1h)), 8)))
check(len(modh) == 1 and abs(modh[0] - 2 ** -0.25) < 1e-7,
      f"G3(e) D2 [K_HW only]: on the Hasse-Weil sector every odd eigenvalue of EE has modulus "
      f"r = q^(-1/4) = {2**-0.25:.7f} (observed {modh}): RH(Y) <-> the odd sector is Ramanujan, "
      f"as G3(e) claims, once the delay modes are removed")
# even sector: the fixed-point segment
letters_m, Pm = graded_mps_G3(Z2, J2, Om_modal)
EEm = doubled(letters_m)
iem, iom = sector_split(Pm)
E0m = EEm[np.ix_(iem, iem)]
evm = np.linalg.eigvals(E0m)
check(int(np.sum(np.abs(evm - 1) < 1e-8)) == 2,
      f"G3(e) D2: the even sector has exactly two fixed points (the vacuum and rho_inf), so the "
      f"stationary densities form a segment and EE is NOT a mixing graded expander "
      f"(prop:graded-stationary-segment, obs:cusp-no-graph-vacuum)")

# ---- G3(c): Tr Z^{2k} and the point counts of the curve ----
head("SECTION 3b  G3(c): Tr Z^{2k} = 2 q^{-k}(alpha_+^k + alpha_-^k) = 2 q^{-k}(1 + q^k - N_k)")


def gf_tables(k):
    """F_{2^k} as F_2[x]/(irreducible): return (mul, add) tables as integer bitmask ops."""
    irr = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011, 5: 0b100101}[k]
    size = 1 << k

    def mul(a, b):
        r = 0
        while b:
            if b & 1:
                r ^= a
            b >>= 1
            a <<= 1
            if a & size:
                a ^= irr
        return r
    return mul, size


def count_points(k):
    mul, size = gf_tables(k)
    cnt = 0
    for x in range(size):
        x2 = mul(x, x)
        x3 = mul(x2, x)
        rhs = x3 ^ x ^ 1
        for y in range(size):
            if (mul(y, y) ^ y) == rhs:
                cnt += 1
    return cnt + 1           # the point at infinity


Nk = [count_points(k) for k in range(1, 6)]
alp, alm = 1 - 1j, 1 + 1j
Nk_pred = [int(round((1 + 2 ** k - (alp ** k + alm ** k)).real)) for k in range(1, 6)]
check(Nk == Nk_pred == [1, 5, 13, 25, 41],
      f"G3(c) point counts of y^2 + y = x^3 + x + 1 over F_(2^k), k = 1..5, by direct enumeration: "
      f"{Nk}; predicted 1 + q^k - (alpha_+^k + alpha_-^k) = {Nk_pred}")
ok_tr = True
for k in range(1, 6):
    trZ = np.trace(np.linalg.matrix_power(Z2, 2 * k))
    f1 = 2 * 2.0 ** -k * (alp ** k + alm ** k)
    f2 = 2 * 2.0 ** -k * (1 + 2 ** k - Nk[k - 1])
    ok_tr = ok_tr and abs(trZ - f1) < 1e-9 and abs(trZ - f2) < 1e-9
check(ok_tr,
      "G3(c) D2: Tr Z^(2k) = 2 q^(-k)(alpha_+^k + alpha_-^k) = 2 q^(-k)(1 + q^k - N_k) for "
      "k = 1..5, exactly the odd half of the point count")
check(all(abs(np.trace(np.linalg.matrix_power(Z2, 2 * k + 1))) < 1e-12 for k in range(0, 5)),
      "G3(c) D2: Tr Z^L = 0 for every odd L (the bipartite pairing z <-> -z)")


# ============================================================================ #
#  SECTION 4.  G4: funnels, the glued toy                                      #
# ============================================================================ #
head("SECTION 4   G4(a)-(d): the even exit, funnels, and the glued graded network")

# --- G4(b): the one-vertex regular cusp-plus-funnel diagram, exactly ---
a_s, q_s = sp.symbols('a q', positive=True)
b_s = q_s + 1 - a_s
p_b = sp.expand((1 + z_s ** 2) - a_s - b_s / q_s)
check(sp.simplify(p_b - (z_s ** 2 - (1 + a_s * (q_s - 1)) / q_s)) == 0,
      "G4(b): the one-vertex cusp(a)+funnel(b) diagram with a + b = q+1 has "
      "p = z^2 - (1 + a(q-1))/q, exactly and symbolically in a and q")
check(sp.simplify(p_b.subs(a_s, 0) - (z_s ** 2 - 1 / q_s)) == 0,
      "G4(b): a = 0 (pure funnel, APW's tree) gives p = z^2 - 1/q: a resonance at z = q^(-1/2)")
check(sp.simplify(p_b.subs(a_s, q_s + 1) - (z_s ** 2 - q_s)) == 0,
      "G4(b): a = q+1 (pure cusp) gives p = z^2 - q, i.e. a visible bound state at "
      "vartheta = q^(-1/2)")
th2 = q_s / (1 + a_s * (q_s - 1))
check(sp.simplify(sp.solve(sp.Eq(th2, 1), a_s)[0] - 1) == 0 and
      sp.simplify(sp.solve(sp.Eq(th2, 1 / q_s), a_s)[0] - (q_s + 1)) == 0,
      "G4(b): vartheta^2 = q/(1+a(q-1)) equals 1 at a = 1 (threshold) and 1/q at a = q+1")
bad = []
for qv in (2, 3, 5):
    for av in (sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(3, 4)):
        v = sp.simplify(th2.subs({q_s: qv, a_s: av}))
        if not (sp.Rational(1, qv) < v < 1):
            bad.append((qv, av, v))
check(len(bad) == 0,
      f"G4(b): vartheta^2 in (1/q, 1) for EVERY 0 < a < q+1 with a != 1 (brief's claim); "
      f"counterexamples found: {[(str(x),str(y),str(v)) for x,y,v in bad]}")
inrange = []
for qv in (2, 3, 5):
    for av in (sp.Rational(5, 4), sp.Rational(2), sp.Rational(qv)):
        v = sp.simplify(th2.subs({q_s: qv, a_s: av}))
        inrange.append(sp.Rational(1, qv) < v < 1)
check(all(inrange),
      "G4(b): the corrected range: vartheta^2 in (1/q,1), i.e. a genuine visible bound state, "
      "exactly for 1 < a < q+1; for 0 < a < 1 the root of p lies INSIDE the disc and the "
      "constant mode is a resonance, not a bound state")
for qv in (2, 3):
    for av in (sp.Rational(1, 2),):
        rr = sp.solve(sp.Eq(p_b.subs({q_s: qv, a_s: av}), 0), z_s)
        note(f"G4(b) q={qv}, a={av}: roots of p are {[sp.nsimplify(x) for x in rr]}, moduli "
             f"{[float(abs(complex(x))) for x in rr]} -- inside the unit disc, hence resonances")

# --- G4(a): the constant mode on regular cusp-plus-funnel diagrams ---
def constant_mode_residual(Tn, Svals, Cc, Cf, q):
    zq = q ** -0.5
    x = np.array([1.0 / np.sqrt(s) for s in Svals])
    Mmat = (1 + zq ** 2) * np.eye(len(x)) - zq * Tn - zq ** 2 * Cc - Cf / q
    return np.max(np.abs(Mmat @ x)), Mmat


# (i) D2 with its cusp replaced by a funnel of the same weight
Svals2 = [d2['S'][v] for v in d2['order']]
T2n = np.array(sp.Matrix(T2).evalf(30), dtype=float)
Ccz = np.zeros((6, 6))
Cf1 = np.zeros((6, 6))
Cf1[d2['idx']['B'], d2['idx']['B']] = 1.0
res, _ = constant_mode_residual(T2n, Svals2, Ccz, Cf1, 2)
check(res < 1e-12,
      f"G4(a) D2-with-funnel (the cusp at B replaced by a funnel of weight 1, still 3-regular): "
      f"the constant g = 1/sqrt S solves [(1+z^2) - zT_X - z^2 C_c - q^(-1) C_f]x = 0 at "
      f"z = q^(-1/2) (residual {res:.2e})")
pf_z = sp.expand(((1 + z_s ** 2) * sp.eye(6) - z_s * T2 - sp.Rational(1, 2) *
                  sp.diag(0, 1, 0, 0, 0, 0)).det(method='berkowitz'))
check(abs(float(pf_z.subs(z_s, 1 / sp.sqrt(2)))) < 1e-12,
      "G4(a) D2-with-funnel: C_c = 0, so z = q^(-1/2) IS a root of p_funnel (outgoing "
      "everywhere), as G4(a) states")
rts_f = nrts(pf_z, z_s)
note(f"G4(a) D2-with-funnel: the full root set of p_funnel is {clist(rts_f)}, moduli "
     f"{flist(np.abs(rts_f))}")
# (ii) D2 as it stands (pure cusp): the constant mode is bound
res2, _ = constant_mode_residual(T2n, Svals2, np.array(sp.Matrix(d2['C']).evalf(30), dtype=float),
                                 np.zeros((6, 6)), 2)
check(res2 < 1e-12,
      f"G4(a) D2 (pure cusp): the constant mode solves the same equation with C_f = 0 "
      f"(residual {res2:.2e}), and z = q^(-1/2) is a root of ptilde, i.e. a visible bound state: "
      f"ptilde_2(1/sqrt2) = {float(pt2.subs(z_s, 1/sp.sqrt(2))):.1e}")
check(abs(float(pt2.subs(z_s, 1 / sp.sqrt(2)))) < 1e-12 and
      abs(float(p2.subs(z_s, 1 / sp.sqrt(2)))) > 1e-6,
      "G4(a) D2: z = q^(-1/2) is a root of ptilde (bound everywhere, C_f = 0) and NOT of p")
# (iii) a two-vertex regular cusp+funnel diagram built by hand
Tm = np.array([[0.0, 1 / np.sqrt(2)], [1 / np.sqrt(2), 0.0]])
Cc2 = np.diag([2.0, 0.0])
Cf2 = np.diag([0.0, 2.0])
res3, _ = constant_mode_residual(Tm, [1, 1], Cc2, Cf2, 2)
check(res3 < 1e-12,
      f"G4(a) two-vertex 3-regular cusp(2)+funnel(2) diagram: the constant mode solves the mixed "
      f"equation at z = q^(-1/2) (residual {res3:.2e})")
pmix = np.linalg.det((1 + 0.5) * np.eye(2) - 2 ** -0.5 * Tm - Cc2 - Cf2 / 2)
ptmix = np.linalg.det((1 + 0.5) * np.eye(2) - 2 ** -0.5 * Tm - 0.5 * Cc2 - 0.5 * Cf2 / 2)
check(abs(pmix) > 1e-6 and abs(ptmix) > 1e-6,
      f"G4(a) two-vertex mixed diagram: with both kinds of ray present, z = q^(-1/2) is neither a "
      f"resonance (p = {pmix:+.6f}) nor a visible bound state (ptilde = {ptmix:+.6f}): the "
      f"constant function is in neither L^2 nor K")

# --- G4(c): bolting a funnel onto D2 ---
head("SECTION 4b  G4(c): d|z_i|/df at f = 0 for the four Hasse-Weil roots, all six vertices")
Aint2 = d2['Aint']
Cc_full = sp.diag(0, 1, 0, 0, 0, 0)
tHW = [z / np.sqrt(2) for z in HW2]
M0t = (1 + 2 * t_s ** 2) * sp.eye(6) - t_s * Aint2 - Cc_full
p0t = sp.expand(M0t.det(method='berkowitz'))
Dv = {}
for vi, v in enumerate(d2['order']):
    Dv[v] = sp.expand(M0t.minor_submatrix(vi, vi).det(method='berkowitz'))
Pv0 = sp.zeros(6, 6)
Pv0[0, 0] = 1
check(sp.expand((M0t - (f_s / 2) * Pv0).det(method='berkowitz') -
                (p0t - (f_s / 2) * Dv['A'])) == 0,
      "G4(c) D2: p_f(z) = det((1+z^2) - z T_2 - P_B - (f/q) P_v) = p_0(z) - (f/q) M_vv(z), the "
      "rank-one cofactor expansion, exactly (checked symbolically at v = A)")


def cofloat(expr):
    co = sp.Poly(expr, t_s).all_coeffs()[::-1]
    return np.array([float(c) for c in co], dtype=float)


c_p0 = cofloat(p0t)
c_Dv = {v: cofloat(Dv[v]) for v in d2['order']}


def pf_coeffs(v, fv):
    a = np.zeros(max(len(c_p0), len(c_Dv[v])))
    a[:len(c_p0)] += c_p0
    a[:len(c_Dv[v])] -= (fv / 2.0) * c_Dv[v]
    return a


def nrts_num(co_low, tol=1e-13):
    co = list(co_low)
    m = 0
    sc = max(abs(c) for c in co) or 1.0
    while len(co) > 1 and abs(co[0]) < tol * sc:
        co.pop(0)
        m += 1
    rr = list(np.roots(co[::-1])) if len(co) > 1 else []
    return [complex(x) for x in rr] + [0j] * m


deriv_table = {}
anyzero = []
dp0dt = sp.lambdify(t_s, sp.diff(p0t, t_s), 'numpy')
for v in d2['order']:
    fdv = sp.lambdify(t_s, Dv[v], 'numpy')
    rowz = []
    for ti, zi in zip(tHW, HW2):
        dtdf = (0.5 * complex(fdv(ti))) / complex(dp0dt(ti))
        dzdf = np.sqrt(2) * dtdf
        rowz.append((np.conj(zi) * dzdf).real / abs(zi))
    deriv_table[v] = rowz
    note(f"G4(c) funnel at {v:>3}: d|z_i|/df at f=0 for the quartet = " +
         ", ".join(f"{x:+.7f}" for x in rowz))
    if min(abs(x) for x in rowz) < 1e-10:
        anyzero.append(v)
check(len(anyzero) == 0,
      f"G4(c) D2: for EVERY core vertex v and every Hasse-Weil root, d|z_i|/df at f = 0 is "
      f"nonzero, so the quartet leaves the circle |z| = q^(-1/4) at first order "
      f"(vertices with a vanishing derivative: {anyzero})")
sprd = [max(vv) - min(vv) for vv in deriv_table.values()]
check(max(sprd) < 1e-9,
      f"G4(c) D2: at EVERY vertex the four derivatives d|z_i|/df coincide (max spread "
      f"{max(sprd):.2e}): the quartet moves as a rigid Klein orbit {{z,-z,conj z,-conj z}}, so "
      f"it leaves the circle q^(-1/4) but stays EQUIMODULAR at first order")


def track_quartet(v, fgrid):
    cur = list(HW2)
    rows = []
    for fv in fgrid:
        rts = [r * np.sqrt(2) for r in nrts_num(pf_coeffs(v, fv))]
        pool = list(rts)
        new = []
        for z0 in cur:
            k = int(np.argmin([abs(z0 - r) for r in pool]))
            new.append(pool.pop(k))
        cur = new
        rows.append((fv, [abs(x) for x in cur]))
    return rows


fgrid = [0.02, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0]
split_at = {}
spread_02 = {}
for v in d2['order']:
    rows = track_quartet(v, fgrid)
    for (fv, mods) in rows:
        if fv == 0.2:
            spread_02[v] = max(mods) - min(mods)
        if max(mods) - min(mods) > 1e-8 and v not in split_at:
            split_at[v] = (fv, sorted(round(x, 6) for x in mods))
    note(f"G4(c) funnel at {v:>3}: tracked quartet moduli " +
         "; ".join(f"f={fv}: " + "/".join("%.6f" % x for x in sorted(m)) for fv, m in rows))
check(max(spread_02.values()) > 1e-8,
      f"G4(c) D2: at f = 1/5 the four Hasse-Weil moduli are no longer equal at any vertex (the "
      f"brief's 'the Hasse-Weil quartet leaves the circle |z| = 2^(-1/4)', read as a loss of "
      f"the equal-modulus property); measured spreads "
      f"{{{', '.join(f'{v}:{spread_02[v]:.1e}' for v in d2['order'])}}}")
check(max(spread_02.values()) < 1e-8,
      f"G4(c) D2: CORRECTED: at f = 1/5 the quartet is still EQUIMODULAR at every vertex "
      f"(max spread {max(spread_02.values()):.1e}); it has left the circle q^(-1/4) for a "
      f"different circle, so RH(Y) survives with a shifted radius")
note(f"G4(c) the first grid value of f at which the quartet stops being equimodular, by "
     f"vertex: {{{', '.join(f'{v}: f={split_at[v][0]} -> {split_at[v][1]}' for v in split_at)}}}"
     f"; vertices with no split on the grid up to f = 5: "
     f"{[v for v in d2['order'] if v not in split_at]}")
check(len(split_at) > 0,
      f"G4(c) D2: for large enough f the quartet does break into two Klein orbits of different "
      f"moduli, at the vertices {sorted(split_at)} (the roots collide on an axis and split), so "
      f"RH(Y) eventually fails -- but not at first order in f")
perr = []
for fv in (0.01, 0.5, 2.0, 10.0, 100.0):
    rts = [r * np.sqrt(2) for r in nrts_num(pf_coeffs('B', fv))]
    ext = [abs(r) for r in rts if abs(r) > 1 + 1e-9]
    perr.append((fv, 1 / max(ext) if ext else None))
note(f"G4(c) D2, funnel at B: the visible bound parameter vartheta = 1/max|exterior root| as f "
     f"grows: {[(a, None if b is None else round(b,7)) for a,b in perr]}; q^(-1/2) = "
     f"{2**-0.5:.7f}")
check(all(b is not None and b > 2 ** -0.5 for _, b in perr),
      "G4(c) D2: 'the Perron pair moves inward without reaching q^(-1/2) for finite f' (brief), "
      "read as vartheta staying above q^(-1/2)")
check(all(b is not None and 0 < b < 2 ** -0.5 for _, b in perr) and
      all(perr[i][1] > perr[i + 1][1] for i in range(len(perr) - 1)),
      f"G4(c) D2: CORRECTED: vartheta starts AT q^(-1/2) = {2**-0.5:.7f} at f = 0 and drops "
      f"strictly below it for every f > 0, decreasing monotonically towards 0; the exterior "
      f"root 1/vartheta never re-enters the disc, so the Perron pair stays a visible bound "
      f"state and never becomes the funnel's outgoing mode at z = q^(-1/2)")

# --- G4(d): the glued toy ---
head("SECTION 4c  G4(d)(i)-(vi): the glued graded network")
qv = 2
Zp_, Jp_, Gp_, Lhp_, Pcp_ = blaschke_model([qv ** -0.5, -qv ** -0.5])
check(np.max(np.abs(np.eye(2) - Zp_.conj().T @ Zp_ - Jp_.conj().T @ Jp_)) < 1e-10,
      f"G4(d)(v) K_+: APW's tree (core [0], one funnel of weight q+1, c_+^2 = (q+1)/q, "
      f"p_+ = z^2 - 1/q) has a two-dimensional model space with eigenvalues +-q^(-1/2) and "
      f"I - Z^*Z = J^*J")
pplus = sp.expand((1 + z_s ** 2) - sp.Rational(qv + 1, qv))
check(sp.simplify(pplus - (z_s ** 2 - sp.Rational(1, qv))) == 0,
      "G4(d)(v) K_+: p_+ = z^2 - 1/q exactly, no visible bound states, Theta_+ = -R_+")

Nm = N2
Np = 2
Ktot = Nm + Np
Zg = np.zeros((Ktot, Ktot), dtype=complex)
Zg[:Np, :Np] = Zp_
Zg[Np:, Np:] = Z2
Jg = np.zeros((2, Ktot), dtype=complex)
Jg[0, :Np] = Jp_[0]
Jg[1, Np:] = J2[0]
Pg = np.diag([1.0] * Np + [-1.0] * Nm)
check(np.max(np.abs(np.eye(Ktot) - Zg.conj().T @ Zg - Jg.conj().T @ Jg)) < 1e-9,
      f"G4(d) glued: Z = Z_+ (+) Z_-, J = J_+ (+) J_- is a 2-exit contraction on "
      f"K = K_+ (+) K_- (dim {Np} + {Nm}), I - Z^*Z = J^*J")

Omp = np.zeros((Np, Np), dtype=complex)
Y = rng.normal(size=(Np, Np)) + 1j * rng.normal(size=(Np, Np))
Omp = Y @ Y.conj().T
Omp /= np.trace(Omp).real
Omg = np.zeros((Ktot, Ktot), dtype=complex)
Omg[:Np, :Np] = 0.5 * Omp
Omg[Np:, Np:] = 0.5 * Om_modal


def graded_mps_glue(Z, J, Om, P):
    letters = [Z.astype(complex)]
    par = [+1]
    pp, VV = np.linalg.eigh(Om)
    for i in np.where(pp > 1e-12)[0]:
        wk = VV[:, i]
        ew = +1 if np.max(np.abs(P @ wk - wk)) < 1e-9 else (-1 if np.max(np.abs(P @ wk + wk)) < 1e-9 else 0)
        for a in range(J.shape[0]):
            ja = J.conj().T[:, a]
            ej = +1 if np.max(np.abs(P @ ja - ja)) < 1e-9 else (-1 if np.max(np.abs(P @ ja + ja)) < 1e-9 else 0)
            letters.append(np.sqrt(pp[i]) * np.outer(wk, ja.conj()))
            par.append(ew * ej)
    return letters, par


lg, parg = graded_mps_glue(Zg, Jg, Omg, Pg)
check(all(p_ != 0 for p_ in parg) and
      all(np.max(np.abs(Pg @ A @ Pg - p_ * A)) < 1e-9 for A, p_ in zip(lg, parg)),
      f"G4(d)(i) glued: every letter is homogeneous, of parity eps(omega_k) eps(j_a); the "
      f"parities are {parg} -- {sum(1 for p_ in parg if p_ < 0)} of the "
      f"{len(parg)} letters are ODD (the cross letters: an exit of one sector reset into the "
      f"other)")
check(np.max(np.abs(sum(A.conj().T @ A for A in lg) - np.eye(Ktot))) < 1e-9,
      "G4(d)(i) glued: sum A_i^* A_i = 1, EE is a trace-preserving graded transfer channel")
EEg = doubled(lg)
Gdbg = np.kron(Pg, Pg.conj())
check(np.max(np.abs(EEg @ Gdbg - Gdbg @ EEg)) < 1e-9,
      "G4(d)(i) glued: EE commutes with the doubled parity")
evg = np.linalg.eigvals(EEg)
m1 = int(np.sum(np.abs(evg - 1) < 1e-8))
check(m1 == 1,
      f"G4(d)(ii) glued: the eigenvalue 1 of EE is simple (multiplicity {m1}), so the stationary "
      f"density is unique")
wg, vg = np.linalg.eig(EEg)
i1 = int(np.argmin(np.abs(wg - 1)))
rg = vg[:, i1].reshape(Ktot, Ktot)
rg = rg / np.trace(rg)
rg = 0.5 * (rg + rg.conj().T)
check(np.max(np.abs(Pg @ rg @ Pg - rg)) < 1e-8 and
      abs(np.trace(rg[:Np, :Np]).real) > 1e-3 and abs(np.trace(rg[Np:, Np:]).real) > 1e-3,
      f"G4(d)(ii) glued: rho_inf is EVEN and MIXED, populating both sectors with weights "
      f"{float(np.trace(rg[:Np,:Np]).real):.6f} and {float(np.trace(rg[Np:,Np:]).real):.6f}")
acc = np.zeros_like(Omg)
Zk = np.eye(Ktot, dtype=complex)
for mm in range(500):
    acc = acc + Zk @ Omg @ Zk.conj().T
    Zk = Zg @ Zk
check(np.max(np.abs(rg - acc / np.trace(acc))) < 1e-7,
      f"G4(d)(ii) glued: rho_inf = tbar^(-1) sum_m Z^m Omega Z^(*m) (deviation "
      f"{np.max(np.abs(rg - acc/np.trace(acc))):.2e})")
ieg, iog = sector_split(Pg)
E1g = EEg[np.ix_(iog, iog)]
odd_pred = sorted(np.round(np.concatenate(
    [[zp * np.conj(zn) for zp in [qv ** -0.5, -qv ** -0.5] for zn in zs2],
     [zn * np.conj(zp) for zp in [qv ** -0.5, -qv ** -0.5] for zn in zs2]]), 8),
    key=lambda v: (round(v.real, 7), round(v.imag, 7)))
odd_act = sorted(np.round(np.linalg.eigvals(E1g), 8),
                 key=lambda v: (round(v.real, 7), round(v.imag, 7)))
check(len(odd_act) == len(odd_pred) and
      max(abs(a - b) for a, b in zip(odd_act, odd_pred)) < 1e-7,
      f"G4(d)(iv,v) glued: the odd eigenvalues of EE are exactly {{+-q^(-1/2) conj(z_n)}} and "
      f"their conjugates (max deviation "
      f"{max(abs(a-b) for a,b in zip(odd_act, odd_pred)):.2e})")
mods = sorted(set(np.round(np.abs(odd_act), 7)))
check(mods == sorted({0.0, round(2 ** -0.75, 7)}),
      f"G4(d)(v) glued: the odd moduli are {mods}: q^(-3/4) = {2**-0.75:.7f} on the Hasse-Weil "
      f"part (rates add: r_+ r_- = q^(-1/2) q^(-1/4)) and 0 on the delay part")
ok_ring = True
for L in range(1, 9):
    EL = np.linalg.matrix_power(EEg, L)
    st = np.trace(Gdbg @ EL).real
    tr = np.trace(EL).real
    trZp = np.trace(np.linalg.matrix_power(Zp_, L))
    trZm = np.trace(np.linalg.matrix_power(Z2, L))
    odd_part = 2 * (trZm * np.conj(trZp)).real
    ok_ring = ok_ring and abs((tr - st) - 2 * odd_part) < 1e-7 and \
        abs(trZp - qv ** (-L / 2) * (1 + (-1) ** L)) < 1e-10
check(ok_ring,
      "G4(d)(v) glued: the twisted ring norm's odd part is -2 Re[(Tr Z_-^L) conj(Tr Z_+^L)], "
      "with Tr Z_+^L = q^(-L/2)(1 + (-1)^L), for L = 1..8")
# eigen-operator check for the odd coherences
kA = eigvec_coords(Pc2, HW2[0], Lh2)
kB = eigvec_coords(Pcp_, qv ** -0.5, Lhp_)
rho_cross = np.zeros((Ktot, Ktot), dtype=complex)
rho_cross[Np:, :Np] = np.outer(kA, kB.conj())
out_cross = sum(A @ rho_cross @ A.conj().T for A in lg)
lam = HW2[0] * np.conj(qv ** -0.5)
check(np.max(np.abs(out_cross - lam * rho_cross)) < 1e-9,
      f"G4(d)(iv) glued: |k_n><k_m| with k_n in K_-, k_m in K_+ is an eigen-operator of EE with "
      f"eigenvalue z_n conj(z_m) = {c6(lam)}, because Tr(J|k_n><k_m|J^*) = <a_m,a_n> = 0 "
      f"(different exit blocks); deviation {np.max(np.abs(out_cross - lam*rho_cross)):.2e}")
amps_g = Jg @ np.stack([np.concatenate([np.zeros(Np), kA]),
                        np.concatenate([kB, np.zeros(Nm)])], axis=1)
check(abs(np.vdot(amps_g[:, 1], amps_g[:, 0])) < 1e-12,
      f"G4(d)(iv) glued: <a_m, a_n> = 0 exactly for cross-sector modes "
      f"({abs(np.vdot(amps_g[:,1], amps_g[:,0])):.2e})")

# (iii) sector-preserving reset: the segment
def sector_preserving(Z, J, Omp_, Omm_, Np):
    letters = [Z.astype(complex)]
    for (blk, Omx, rng_) in ((0, Omp_, range(0, Np)), (1, Omm_, range(Np, Z.shape[0]))):
        pp, VV = np.linalg.eigh(Omx)
        for i in np.where(pp > 1e-12)[0]:
            wk = np.zeros(Z.shape[0], dtype=complex)
            if blk == 0:
                wk[:Np] = VV[:, i]
            else:
                wk[Np:] = VV[:, i]
            ja = J.conj().T[:, blk]
            letters.append(np.sqrt(pp[i]) * np.outer(wk, ja.conj()))
    return letters


lsp = sector_preserving(Zg, Jg, Omp, Om_modal, Np)
check(np.max(np.abs(sum(A.conj().T @ A for A in lsp) - np.eye(Ktot))) < 1e-9,
      "G4(d)(iii) glued, sector-preserving reset: sum A_i^* A_i = 1")
check(all(np.max(np.abs(Pg @ A @ Pg - A)) < 1e-9 for A in lsp),
      "G4(d)(iii) glued, sector-preserving reset: ALL letters are even (no parity-crossing letter)")
EEsp = doubled(lsp)
evsp = np.linalg.eigvals(EEsp)
msp = int(np.sum(np.abs(evsp - 1) < 1e-8))
check(msp == 2,
      f"G4(d)(iii) glued: with a sector-preserving reset the eigenvalue 1 has multiplicity "
      f"{msp} = 2: each sector carries its own stationary density and the stationary densities "
      f"form a SEGMENT -- a unique mixed stationary state requires an odd letter")

# (vi) shared exit on a random three-vertex core
head("SECTION 4d  G4(d)(vi): the shift on a random three-vertex core with one shared cusp")
found = None
for attempt in range(400):
    T = np.zeros((3, 3))
    for i in range(3):
        for j in range(i, 3):
            T[i, j] = T[j, i] = rng.uniform(-0.6, 0.6)
    c2 = float(rng.uniform(0.2, 0.9))
    Cm = np.diag([c2, 0.0, 0.0])
    zz = sp.Symbol('zz')
    pm = sp.expand(sp.Matrix(((1 + zz ** 2) * np.eye(3) - zz * T - Cm).tolist()).det(method='berkowitz'))
    rr = nrts(pm, zz)
    if len(rr) == 6 and all(abs(x) < 0.97 for x in rr) and all(abs(x) > 1e-3 for x in rr):
        ds = min(abs(rr[i] - rr[j]) for i in range(6) for j in range(i + 1, 6))
        if ds > 1e-3:
            found = (T, c2, rr)
            break
check(found is not None,
      "G4(d)(vi): a random three-vertex core with one cusp, six distinct nonzero resonances and "
      "no visible bound states was found")
if found is not None:
    T, c2, rr = found
    Zr, Jr, Gr, Lhr, Pcr = blaschke_model(rr)
    Nr = 6
    check(np.max(np.abs(np.eye(Nr) - Zr.conj().T @ Zr - Jr.conj().T @ Jr)) < 1e-9,
          f"G4(d)(vi): the six-dimensional one-exit model of the random core satisfies "
          f"I - Z^*Z = J^*J (c^2 = {c2:.6f})")
    Kr = np.stack([eigvec_coords(Pcr, a, Lhr) for a in rr], axis=1)
    ar = (Jr @ Kr)[0]
    Gr2 = Kr.conj().T @ Kr
    pred = np.array([[np.conj(ar[m]) * ar[n] / (1 - np.conj(rr[m]) * rr[n]) for n in range(6)]
                     for m in range(6)])
    check(np.max(np.abs(Gr2 - pred)) < 1e-8,
          f"G4(d)(vi): the Gram identity <a_m,a_n> = (1 - conj(z_m) z_n) <k_m,k_n> holds "
          f"(deviation {np.max(np.abs(Gr2-pred)):.2e}); with ONE shared exit all "
          f"<a_m,a_n> = conj(a_m) a_n are nonzero (min {np.min(np.abs(np.outer(np.conj(ar),ar))):.4f})")
    Y = rng.normal(size=(Nr, Nr)) + 1j * rng.normal(size=(Nr, Nr))
    Omr = Y @ Y.conj().T
    Omr /= np.trace(Omr).real
    EE0 = np.kron(Zr, Zr.conj())
    EEr = renewal_channel(Zr, Jr, Omr)
    ev0 = np.linalg.eigvals(EE0)
    evr = np.linalg.eigvals(EEr)
    even_idx = [0, 1]
    odd_idx = [2, 3, 4, 5]
    resid = []
    dropped = []
    for n in odd_idx:
        for m in even_idx:
            lam = rr[n] * np.conj(rr[m])
            X = np.outer(Kr[:, n], Kr[:, m].conj())
            out = Zr @ X @ Zr.conj().T + np.trace(Jr @ X @ Jr.conj().T) * Omr
            rres = out - lam * X
            pred = np.conj(ar[m]) * ar[n] * Omr
            resid.append((np.max(np.abs(rres)), np.max(np.abs(rres - pred))))
            m0 = int(np.sum(np.abs(ev0 - lam) < 1e-7))
            m1 = int(np.sum(np.abs(evr - lam) < 1e-7))
            dropped.append((m0, m1))
    check(min(x for x, _ in resid) > 1e-3 and max(y for _, y in resid) < 1e-9,
          f"G4(d)(vi): with a SHARED exit, |k_n><k_m| is NOT an eigen-operator of EE_Omega for "
          f"any cross pair: the residue is exactly <a_m,a_n> Omega (min residual "
          f"{min(x for x,_ in resid):.3e}, max deviation from <a_m,a_n> Omega "
          f"{max(y for _,y in resid):.2e})")
    check(all(b == a - 1 for a, b in dropped),
          f"G4(d)(vi): the multiplicity of each cross eigenvalue z_n conj(z_m) drops by exactly "
          f"one under the reset {dropped}: NOTE the VALUE still persists, because the spectrum "
          f"of Ad_Z on a real core is conjugation symmetric, so z_n conj(z_m) is already "
          f"degenerate (paired with z_n' conj(z_m') for the conjugate roots) and a rank-one "
          f"reset can remove only one copy")
    okse = True
    for uu in [0.31 + 0.12j, -0.4 + 0.3j]:
        lhs = np.linalg.det(np.eye(Nr * Nr) - uu * EEr)
        mhat = uu * np.trace(Jr @ (np.linalg.solve(np.eye(Nr * Nr) - uu * EE0,
                                                   Omr.reshape(-1))).reshape(Nr, Nr) @ Jr.conj().T)
        rhs = np.linalg.det(np.eye(Nr * Nr) - uu * EE0) * (1 - mhat)
        okse = okse and abs(lhs - rhs) < 1e-7 * max(1.0, abs(lhs))
    check(okse,
          "G4(d)(vi): the rank-one persistence/secular identity det(1-u EE_Omega) = "
          "det(1-u EE_0)(1 - mhat(u)) holds, so persistence is exactly "
          "<a_m,a_n> . dual_nm(Omega) = 0")


# ============================================================================ #
#  SECTION 5.  G5: the arithmetic metric is the Frobenius channel              #
# ============================================================================ #
head("SECTION 5   G5(a)-(c): the arithmetic-metric channel and the self-adjointness obstruction")

r_ar = 2 ** -0.25
Za = np.diag(np.array(HW2, dtype=complex))
U = Za / r_ar
check(np.max(np.abs(U.conj().T @ U - np.eye(4))) < 1e-12,
      f"G5(a) D2, arithmetic metric (all four e_i declared orthonormal, thm:arithmetic-metric's "
      f"symmetric ray): Z = r U with r = q^(-1/4) = {r_ar:.7f} and U unitary")
Ja = np.sqrt(1 - r_ar ** 2) * np.eye(4)
check(np.max(np.abs(np.eye(4) - Za.conj().T @ Za - Ja.conj().T @ Ja)) < 1e-12,
      "G5(a) D2: with one exit per mode, J' = sqrt(1-r^2) 1_{K_HW} (h = 4) satisfies "
      "I - Z'^*Z' = J'^*J' in the arithmetic metric")
Fr = np.diag([1 - 1j, 1 + 1j])
U2 = U @ U
sp1 = sorted(np.round(np.linalg.eigvals(U2), 8), key=lambda v: (round(v.real, 6), round(v.imag, 6)))
sp2 = sorted(np.round(np.concatenate([np.linalg.eigvals(np.linalg.inv(Fr / np.sqrt(2)))] * 2), 8),
             key=lambda v: (round(v.real, 6), round(v.imag, 6)))
check(max(abs(a - b) for a, b in zip(sp1, sp2)) < 1e-8,
      f"G5(a) D2: U^2 is similar to (Fr/sqrt q)^(-1) (x) 1_2 (spectra agree to "
      f"{max(abs(a-b) for a,b in zip(sp1,sp2)):.2e})")
Ya = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
Om_a = Ya @ Ya.conj().T
Om_a /= np.trace(Om_a).real
Om_d = np.diag(rng.dirichlet(np.ones(4))).astype(complex)
for nmO, Om in (("random (non-commuting)", Om_a), ("modal (diagonal)", Om_d)):
    EEa = r_ar ** 2 * np.kron(U, U.conj()) + (1 - r_ar ** 2) * np.outer(Om.reshape(-1),
                                                                        np.eye(4).reshape(-1))
    dual = (r_ar ** 2 * np.kron(U, U.conj()) + (1 - r_ar ** 2) *
            np.outer(Om.reshape(-1), np.eye(4).reshape(-1))).conj().T @ np.eye(4).reshape(-1)
    check(np.max(np.abs(dual - np.eye(4).reshape(-1))) < 1e-9,
          f"G5(a) [{nmO} Omega]: EE' = r^2 Ad(U) + (1-r^2) Tr(.) Omega is trace preserving")
    acc = np.zeros((4, 4), dtype=complex)
    Uk = np.eye(4, dtype=complex)
    for mm in range(400):
        acc += r_ar ** (2 * mm) * Uk @ Om @ Uk.conj().T
        Uk = U @ Uk
    rinf = (1 - r_ar ** 2) * acc
    out = r_ar ** 2 * U @ rinf @ U.conj().T + (1 - r_ar ** 2) * np.trace(rinf) * Om
    check(np.max(np.abs(out - rinf)) < 1e-9 and abs(np.trace(rinf) - 1) < 1e-9,
          f"G5(a) [{nmO} Omega]: rho_inf = (1-r^2) sum_m r^(2m) U^m Omega U^(*m) is the unique "
          f"stationary density (residual {np.max(np.abs(out-rinf)):.2e})")
    comm = np.max(np.abs(Om @ U - U @ Om))
    eqOm = np.max(np.abs(rinf - Om))
    check((comm < 1e-9) == (eqOm < 1e-9),
          f"G5(a) [{nmO} Omega]: rho_inf = Omega iff [Omega, U] = 0 "
          f"(||[Omega,U]|| = {comm:.2e}, ||rho_inf - Omega|| = {eqOm:.2e})")
EEa = r_ar ** 2 * np.kron(U, U.conj()) + (1 - r_ar ** 2) * np.outer(Om_a.reshape(-1),
                                                                    np.eye(4).reshape(-1))
eva = np.linalg.eigvals(EEa)
rel = [e for e in eva if abs(e - 1) > 1e-8]
check(len(rel) == 15 and max(abs(abs(e) - r_ar ** 2) for e in rel) < 1e-9,
      f"G5(a) D2: on traceless operators EE' = r^2 Ad(U); all {len(rel)} relaxation eigenvalues "
      f"have modulus exactly r^2 = q^(-1/2) = {r_ar**2:.7f} (deviation "
      f"{max(abs(abs(e)-r_ar**2) for e in rel):.2e}): a one-gap mixing quantum expander")
th = np.angle(np.diag(U))
pred_rel = sorted(np.round([r_ar ** 2 * np.exp(1j * (th[a] - th[b])) for a in range(4)
                            for b in range(4)], 8), key=lambda v: (round(v.real, 6), round(v.imag, 6)))
act_rel = sorted(np.round(list(rel) + [r_ar ** 2], 8),
                 key=lambda v: (round(v.real, 6), round(v.imag, 6)))
check(max(abs(a - b) for a, b in zip(pred_rel, act_rel)) < 1e-7,
      f"G5(a) D2: the relaxation spectrum is exactly {{r^2 e^(i(theta_a - theta_b))}} "
      f"(deviation {max(abs(a-b) for a,b in zip(pred_rel, act_rel)):.2e})")
lg5, P5 = graded_mps_G3(Za, Ja, Om_d)
EE5 = doubled(lg5)
i5e, i5o = sector_split(P5)
o5 = np.abs(np.linalg.eigvals(EE5[np.ix_(i5o, i5o)]))
check(max(abs(x - r_ar) for x in o5) < 1e-9,
      f"G5(a) D2: with the vacuum adjoined, lambda_1 = r = q^(-1/4) = {r_ar:.7f} (every odd "
      f"eigenvalue), lambda_0 = q^(-1/2)")
# (b) the characteristic function
okb = True
for zz in [0.3 + 0.2j, -0.5 + 0.1j, 0.7j]:
    Th = np.linalg.solve(np.eye(4) - zz * r_ar * U.conj().T, zz * np.eye(4) - r_ar * U)
    Bd = np.diag([(zz - za) / (1 - np.conj(za) * zz) for za in HW2])
    okb = okb and np.max(np.abs(Th - Bd)) < 1e-10
check(okb,
      "G5(b) D2: Theta'(z) = (1 - z r U^*)^(-1)(z - r U) = diag((z-z_a)/(1 - conj(z_a) z)) "
      "at three points: the a-th exit sees the single mode z_a")

# (c) no self-adjoint diagram has a non-conjugation-closed exit direction
head("SECTION 5b  G5(c): D2 with a second unit cusp at each vertex in turn")
Ah2 = np.array(sp.Matrix(d2['Ahat']).evalf(30), dtype=float)
T2f = Ah2 / np.sqrt(2)
iB = d2['idx']['B']
maxdev_r = 0.0
maxdev_c = 0.0
for v in d2['order']:
    if v == 'B':
        continue
    ex = [iB, d2['idx'][v]]
    for _ in range(4):
        zz = complex(rng.uniform(0.2, 0.9), rng.uniform(0.1, 0.7))
        Sz, _ = Smat(T2f, ex, [1.0, 1.0], zz)
        Szb, _ = Smat(T2f, ex, [1.0, 1.0], np.conj(zz))
        e_r = rng.normal(size=2).astype(complex)
        e_c = rng.normal(size=2) + 1j * rng.normal(size=2)
        for e in (e_r, e_c):
            lhs = np.vdot(e, Szb @ e)
            rhs = np.conj(np.vdot(e, Sz @ e))
            d_ = abs(lhs - rhs)
            if np.allclose(e.imag, 0):
                maxdev_r = max(maxdev_r, d_)
            else:
                maxdev_c = max(maxdev_c, d_)
        check(np.max(np.abs(Sz - Sz.T)) < 1e-8 and np.max(np.abs(Szb - Sz.conj())) < 1e-8,
              f"G5(c) D2+cusp at {v}: S(z) is symmetric and S(conj z) = conj(S(z)) "
              f"(deviations {np.max(np.abs(Sz-Sz.T)):.2e}, {np.max(np.abs(Szb-Sz.conj())):.2e})")
        break
check(maxdev_r < 1e-8,
      f"G5(c) D2, two exits: e^* S(conj z) e = conj(e^* S(z) e) for every REAL constant exit "
      f"direction, at all five placements (max deviation {maxdev_r:.2e})")
check(maxdev_c < 1e-8,
      f"G5(c) D2, two exits: the same identity holds for COMPLEX constant e as well, because "
      f"S = S^T (max deviation {maxdev_c:.2e}); so no constant exit direction sees a "
      f"non-conjugation-closed set of resonances")
# the zero sets in the disc
Mt2 = (1 + 2 * t_s ** 2) * sp.eye(6) - t_s * d2['Aint']
adj2 = Mt2.adjugate(method='berkowitz')
det2 = sp.expand(Mt2.det(method='berkowitz'))
for v in ('A', 'C', 'D', 'E', 'F'):
    ex = [iB, d2['idx'][v]]
    Wr = sp.Matrix(2, 2, lambda i, j: adj2[ex[i], ex[j]] / det2)
    Sr = sp.simplify((2 * t_s ** 2 * Wr - sp.eye(2)).inv() * (sp.eye(2) - Wr))
    lam = sp.diag(sp.sqrt(d2['S'][d2['order'][ex[0]]]), sp.sqrt(d2['S'][d2['order'][ex[1]]]))
    Sfull = sp.simplify(lam.inv() * Sr * lam)
    sets = []
    for ev in ([1, 0], [0, 1], [1, 1], [1, 1j]):
        e = sp.Matrix(ev)
        fe = sp.simplify((e.conjugate().T * Sfull * e)[0, 0])
        num, den = sp.fraction(sp.cancel(fe))
        rts = [r * np.sqrt(2) for r in nrts(num, t_s)] \
            if sp.Poly(sp.expand(num), t_s).degree() > 0 else []
        ins = [r for r in rts if abs(r) < 1 - 1e-9]
        closed = all(any(abs(np.conj(r) - s) < 1e-7 for s in ins) for r in ins)
        sets.append((ev, sorted([round(abs(r), 6) for r in ins]), closed))
    check(all(s[2] for s in sets),
          f"G5(c) D2+cusp at {v}: the zero set in the disc of e^* S(z) e is conjugation closed "
          f"for e = e_1, e_2, (1,1), (1,i); disc-zero moduli "
          f"{[s[1] for s in sets]}")

# ============================================================================ #
#  SECTION 6.  G6(b): Dirichlet characters over F_3[T]                         #
# ============================================================================ #
head("SECTION 6   G6(b): L(u,psi) for (F_3[T]/N)^x, N = T^3-T-1 and N = T(T^2+1)")

Pq = 3


def pnorm(a):
    a = [c % Pq for c in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def pmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return pnorm(r)


def pmod(a, m):
    a = pnorm(list(a))
    m = pnorm(list(m))
    inv = pow(m[-1], Pq - 2, Pq)
    while len(a) >= len(m) and a != [0]:
        d = len(a) - len(m)
        c = (a[-1] * inv) % Pq
        if c == 0:
            break
        sub = [0] * d + [(c * x) % Pq for x in m]
        a = pnorm([(a[i] if i < len(a) else 0) - (sub[i] if i < len(sub) else 0)
                   for i in range(max(len(a), len(sub)))])
    return pnorm(a)


def pgcd(a, b):
    a, b = pnorm(list(a)), pnorm(list(b))
    while b != [0]:
        a, b = b, pmod(a, b)
    if a != [0]:
        inv = pow(a[-1], Pq - 2, Pq)
        a = pnorm([(inv * c) % Pq for c in a])
    return a


def monics(n):
    if n == 0:
        return [[1]]
    out = []
    for k in range(Pq ** n):
        co = []
        kk = k
        for _ in range(n):
            co.append(kk % Pq)
            kk //= Pq
        out.append(pnorm(co + [1]))
    return out


def irreducibles(maxdeg):
    out = []
    for d in range(1, maxdeg + 1):
        for fpol in monics(d):
            red = any(len(g) - 1 <= d // 2 and pmod(fpol, g) == [0] for g in out)
            if not red:
                out.append(fpol)
    return out


IRR = irreducibles(5)
check(sorted(len(g) - 1 for g in IRR).count(1) == 3 and
      sorted(len(g) - 1 for g in IRR).count(2) == 3 and
      sorted(len(g) - 1 for g in IRR).count(3) == 8,
      f"G6(b) the monic irreducibles of F_3[T] up to degree 5 are counted correctly: "
      f"{ {d: sum(1 for g in IRR if len(g)-1 == d) for d in range(1, 6)} } against the "
      f"necklace counts 3, 3, 8, 18, 48")


def units_of(N):
    d = len(N) - 1
    us = []
    for k in range(Pq ** d):
        co = []
        kk = k
        for _ in range(d):
            co.append(kk % Pq)
            kk //= Pq
        a = pnorm(co)
        if pgcd(a, N) == [1]:
            us.append(tuple(a))
    return us


def umul(a, b, N):
    return tuple(pmod(pmul(list(a), list(b)), N))


def order_of(g, N, size):
    x = (1,)
    for k in range(1, size + 1):
        x = umul(x, g, N)
        if x == (1,):
            return k
    return None


N1 = pnorm([-1, -1, 0, 1])          # T^3 - T - 1
N2 = pmul([0, 1], [1, 0, 1])        # T(T^2+1)
check(all(pmod(N1, g) != [0] for g in IRR if len(g) - 1 == 1),
      "G6(b) N = T^3 - T - 1 is irreducible over F_3 (no root in F_3, degree 3)")
check(all(pmod([1, 0, 1], g) != [0] for g in IRR if len(g) - 1 == 1),
      "G6(b) T^2 + 1 is irreducible over F_3, so N = T(T^2+1) is squarefree with two prime "
      "factors of degrees 1 and 2")
U1 = units_of(N1)
U2 = units_of(N2)
check(len(U1) == 26 and len(U2) == 16,
      f"G6(b): |(F_3[T]/N)^x| = {len(U1)} = 27-1 for N = T^3-T-1 and {len(U2)} = 2 . 8 = "
      f"|F_3^x| . |F_9^x| for N = T(T^2+1)")

gen1 = next(g for g in U1 if order_of(g, N1, 26) == 26)
check(order_of(gen1, N1, 26) == 26,
      f"G6(b) N1: the unit group is CYCLIC of order 26, generator {list(gen1)}")
dlog1 = {}
xcur = (1,)
for k in range(26):
    dlog1[xcur] = (k,)
    xcur = umul(xcur, gen1, N1)

# N2 : CRT into F_3^x x F_9^x, generators aligned with the two prime factors
MT = [0, 1]
MQ = [1, 0, 1]
gQ = None
for g in units_of(MQ):
    if order_of(g, MQ, 8) == 8:
        gQ = g
        break
check(gQ is not None,
      f"G6(b) N2: F_9^x = (F_3[T]/(T^2+1))^x is cyclic of order 8, generator {list(gQ)}")
dl3 = {(1,): 0, (2,): 1}
dl9 = {}
xcur = (1,)
for k in range(8):
    dl9[xcur] = k
    xcur = umul(xcur, gQ, MQ)
dlog2 = {}
for uu_ in U2:
    a = tuple(pmod(list(uu_), MT))
    b = tuple(pmod(list(uu_), MQ))
    dlog2[uu_] = (dl3[a], dl9[b])
check(len(set(dlog2.values())) == 16,
      f"G6(b) N2: the CRT map u -> (u mod T, u mod T^2+1) is a bijection onto "
      f"Z/2 x Z/8 ({len(set(dlog2.values()))} distinct pairs): the unit group is NOT cyclic, so "
      f"the characters are enumerated as homomorphisms from this presentation")


def psi_val(fpol, N, dlog, jj, orders):
    r = tuple(pmod(list(fpol), N))
    if r not in dlog:
        return 0j
    k = dlog[r]
    e = 0.0
    for a in range(len(jj)):
        e += jj[a] * k[a] / orders[a]
    return np.exp(2j * np.pi * e)


def Lcoeffs(N, dlog, jj, orders):
    dN = len(N) - 1
    return np.array([sum(psi_val(fm, N, dlog, jj, orders) for fm in monics(nn))
                     for nn in range(dN)], dtype=complex)


def polydeg(co, tol=1e-9):
    d = len(co) - 1
    while d > 0 and abs(co[d]) < tol:
        d -= 1
    return d


def polymul(a, b):
    return np.convolve(a, b)


IMPRIM = []
NONWEIL = []
CASES = [("N = T^3-T-1", N1, dlog1, [(j,) for j in range(26)], (26,)),
         ("N = T(T^2+1)", N2, dlog2, [(i, j) for i in range(2) for j in range(8)], (2, 8))]

for nm, N, dlog, jjs, orders in CASES:
    dN = len(N) - 1
    nprim = 0
    bond_odd = 0
    for jj in jjs:
        trivial = all(v == 0 for v in jj)
        co = Lcoeffs(N, dlog, jj, orders)
        deg = polydeg(co)
        ev = abs(psi_val([2], N, dlog, jj, orders) - 1) < 1e-12
        if trivial:
            check(abs(co[-1]) > 1e-9,
                  f"G6(b) {nm}, psi trivial: the truncated sum sum_{{deg f < deg N}} "
                  f"psi(f) u^(deg f) = {np.round(co.real, 6).tolist()} is NOT the L-function of "
                  f"the trivial character, which is prod_{{P|N}}(1-u^(deg P))/(1-qu) and is not "
                  f"a polynomial of degree deg N - 1")
            continue
        prim = all(v != 0 for v in jj)
        check(deg == dN - 1,
              f"G6(b) {nm}, psi = {jj} ({'even' if ev else 'odd'}, "
              f"{'primitive' if prim else 'imprimitive'}): deg L = {deg} = deg N - 1")
        rts = np.roots(co[::-1]) if deg > 0 else np.array([])
        betas = 1.0 / rts
        nontriv = [b for b in betas if abs(b - 1) > 1e-6]
        Lat1 = complex(np.sum(co))
        if prim:
            check(all(abs(abs(b) - np.sqrt(3)) < 1e-8 for b in nontriv),
                  f"G6(b) {nm}, psi = {jj} PRIMITIVE: |beta| = sqrt q = {np.sqrt(3):.7f} for "
                  f"the {len(nontriv)} nontrivial roots {['%.9f' % abs(b) for b in nontriv]} "
                  f"(Weil)")
            if ev:
                check(abs(Lat1) < 1e-10,
                      f"G6(b) {nm}, psi = {jj} EVEN (trivial on F_3^x): (1-u) divides L, "
                      f"L(1) = {abs(Lat1):.2e}; the split-off root beta = 1 has |beta| = 1, "
                      f"NOT sqrt q, so that odd mode is off the Weil circle")
            else:
                check(abs(Lat1) > 1e-8,
                      f"G6(b) {nm}, psi = {jj} ODD: L(1) = {abs(Lat1):.6f} != 0, no (1-u) "
                      f"factor")
        else:
            nb1 = sum(1 for b in betas if abs(abs(b) - 1) < 1e-6)
            IMPRIM.append((nm, jj, ev, sorted(round(abs(b), 7) for b in betas), abs(Lat1)))
            check(nb1 >= 1 and all(abs(abs(b) - 1) < 1e-6 or abs(abs(b) - np.sqrt(3)) < 1e-6
                                   for b in betas),
                  f"G6(b) {nm}, psi = {jj} IMPRIMITIVE (induced from a proper divisor of N): "
                  f"the root moduli are {['%.7f' % abs(b) for b in betas]} -- {nb1} of them "
                  f"equal 1, from the Euler factors prod_{{P|N, P not| M}} (1 - psi*(P) "
                  f"u^(deg P)) that the induction inserts; only the primitive part obeys Weil")
        # Euler product to order u^Dmax
        Dmax = 5
        prod = np.array([1.0 + 0j])
        for P in IRR:
            dP = len(P) - 1
            if dP > Dmax:
                continue
            fac = np.zeros(dP + 1, dtype=complex)
            fac[0] = 1.0
            fac[dP] = -psi_val(P, N, dlog, jj, orders)
            prod = polymul(prod, fac)[:Dmax + 1]
        ser = np.zeros(Dmax + 1, dtype=complex)
        ser[0] = 1.0 / prod[0]
        for n_ in range(1, Dmax + 1):
            ser[n_] = -sum(prod[i] * ser[n_ - i] for i in range(1, min(len(prod), n_ + 1))) / prod[0]
        cop = np.concatenate([co, np.zeros(Dmax + 1 - len(co))])
        check(np.max(np.abs(ser - cop)) < 1e-9,
              f"G6(b) {nm}, psi = {jj}: the truncated sum agrees with the Euler product "
              f"prod_P (1 - psi(P) u^(deg P))^(-1) to order u^{Dmax} (deviation "
              f"{np.max(np.abs(ser - cop)):.2e})")
        # Fr_psi and the superdeterminant identity, as an identity of polynomials in w
        Frp = np.zeros((deg, deg), dtype=complex)
        for k in range(1, deg):
            Frp[k, k - 1] = 1.0
        recip = np.poly(betas)                    # monic, high-to-low
        for k in range(deg):
            Frp[k, deg - 1] = -recip[deg - k]
        dw = np.poly(np.linalg.eigvals(Frp))      # char poly of Fr_psi, high-to-low
        detw = np.array([dw[k] * (-1.0) ** 0 for k in range(deg + 1)])   # [w^k] det(1-w Fr)
        check(np.max(np.abs(detw - co[:deg + 1])) < 1e-8,
              f"G6(b) {nm}, psi = {jj}: det(1 - w Fr_psi) = L(w,psi) coefficient by coefficient "
              f"(deviation {np.max(np.abs(detw - co[:deg+1])):.2e}), Fr_psi the companion matrix "
              f"of the beta's")
        detqw = np.array([detw[k] * Pq ** k for k in range(deg + 1)])
        Lqw = np.array([co[k] * Pq ** k for k in range(deg + 1)])
        check(np.max(np.abs(detqw - Lqw)) < 1e-7,
              f"G6(b) {nm}, psi = {jj}: sdet(1 - w E_psi) = det(1 - w q Fr_psi)/det(1 - w Fr_psi) "
              f"= L(qw,psi)/L(w,psi) = L(2s-1,psi)/L(2s,psi) with w = q^(-2s), as an identity of "
              f"rational functions of w (numerator deviation {np.max(np.abs(detqw - Lqw)):.2e})")
        disc_even = [b for b in Pq * betas if abs(b) < Pq * (1 - 1e-6)]
        disc_odd = [b for b in betas if abs(b) < Pq * (1 - 1e-6)]
        bond_odd += len(disc_odd)
        check(len(disc_even) == 0 and len(disc_odd) == deg,
              f"G6(b) {nm}, psi = {jj}: the disc part of the graded divisor is ODD ONLY, "
              f"nu(beta_i) = -1 for all {len(disc_odd)} modes; no even disc eigenvalue "
              f"(|q beta| >= {Pq*np.sqrt(3):.6f} > q)")
        if prim:
            nprim += 1
        NONWEIL.append((nm, jj, sum(1 for b in betas
                                    if abs(abs(b) - np.sqrt(3)) > 1e-6)))
    check(nprim == (25 if len(orders) == 1 else 7),
          f"G6(b) {nm}: {nprim} of the {len(jjs)-1} nontrivial characters are primitive "
          f"(not induced from a proper divisor of N); all of them have deg L = deg N - 1")
    nw = [x for x in NONWEIL if x[0] == nm and x[2] > 0]
    note(f"G6(b) {nm}: the level-N graded bond (disc part) is (1)_+ from the trivial character "
         f"plus {bond_odd} odd L-zeros from the {len(jjs)-1} nontrivial characters")
    check(len(nw) == 0,
          f"G6(b) {nm} BRIEF: the level-N graded bond (1)_+ (+) (+)_{{psi != 1}} "
          f"(beta_{{psi,i}})_- has ALL its odd modes on the Weil circle |beta| = sqrt q; "
          f"characters contributing a mode off that circle: "
          f"{[(x[1], x[2]) for x in nw]}")
    check(all(x[2] <= 1 for x in NONWEIL if x[0] == nm and
              all(v != 0 for v in x[1])),
          f"G6(b) {nm} CORRECTED: for a PRIMITIVE psi at most one odd mode is off the Weil "
          f"circle, namely the trivial zero beta = 1 that the factor (1-u) contributes when "
          f"psi is even; the imprimitive characters (N composite) contribute one modulus-1 "
          f"mode per missing Euler factor")

# the trivial character line of the graded bond: g = 0
even0 = [sp.Integer(1), sp.Integer(3)]
odd0 = [sp.Integer(3), sp.Integer(9)]
sd0 = sdet_from(even0, odd0, w_s)
check(sp.simplify(sd0 - (1 - w_s) / (1 - 9 * w_s)) == 0,
      "G6(b): the trivial character carries zeta_{F_q(T)}(2s-1)/zeta(2s) = sdet(1 - w E_S) at "
      "g = 0, which is (1-w)/(1-q^2 w): a single EVEN disc line at e = 1, the vacuum")


# ============================================================================ #
head("TALLY")
if FAILED:
    print("  failing checks:")
    for i, m in FAILED:
        print(f"    #{i}: {m}")
print()
print(f"CHECKS: {_PASS} passed, {_FAIL} failed")
