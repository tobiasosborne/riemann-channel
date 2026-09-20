#!/usr/bin/env python3
"""Two arithmetic cavities with cusps: elliptic curves over F_2 and F_3.

Numerics lane for `notes/elliptic-cavity/astra-brief.md` (Section 0, C1--C3, T1--T6).
Run BLIND to the prover's file.  Deterministic (seed 20260920); every claim is an
assertion with an explicit tolerance, and the tally is printed at the end.
Exact wherever exactness is possible: all determinants, all scattering matrices and
all zeta identities are done with sympy over Q(sqrt q), not by floating point.

================================================================================
CONVENTIONS FIXED HERE (derived from the definitions, not copied from the brief)
================================================================================

DIAGRAM.  A graph with stabiliser function S: V u E -> R_+ (APW
`2603.26443:final_draft.tex:427-458`), measure nu(v) = 1/S(v), adjacency
(A f)(v) = sum_{e at v} (S(v)/S(e)) f(o(e)), degree deg(v) = sum_{e at v} S(v)/S(e).
A quotient of the (q+1)-regular tree has deg(v) = q+1 at EVERY vertex, core and ray.

NORMALISATION (C1).  A is self-adjoint on l^2(V, nu).  Put g = f/sqrt(S); then A
becomes the symmetric kernel K(v,w) = sqrt(S(v)S(w))/S(e); divide by sqrt q:

    T_X = D^{-1/2} A_X D^{1/2} / sqrt q ,   D = diag S   [corrected after review: D^{-1/2} A_X D^{-1/2} is not symmetric] ,
    (A_X)_{vw} = S(v)/S(e)  (the NON-symmetric integer form; A_X = D^{1/2} T_X D^{1/2}
                              is wrong, the correct similarity is A_X = D^{1/2}(sqrt q T_X)D^{-1/2}).

On a cusp ray with S(c_{k+1}) = q S(c_k) and S(c_k c_{k+1}) = S(c_k) this is EXACTLY
the free path adjacency (T g)(k) = g(k+1) + g(k-1), and the junction v--c_1 becomes a
coupling c with c^2 = S(v) S(c_1)/(q S(e)^2) = S(v)/S(e), because the degree condition
at c_1 forces S(c_1) = q S(e).  For D2 and D3 every cusp junction has c^2 = 1.

SPECTRAL PARAMETER.  lambda = z + 1/z, z = q^{s-1/2}; |z| < 1 <-> Re s < 1/2;
q^{-2s} = z^{-2}/q and q^{1-2s} = z^{-2}.

THE EXACT-ARITHMETIC TRICK.  T_X carries square roots, but

    p(z)      = det((1+z^2) I - z T_X - C)        with C = sum_a c_a^2 P_{v_a}
    p(sqrt q t) = det((1 + q t^2) I - t A_X - C)

and the right-hand side has INTEGER coefficients.  Every determinant below is computed
in that variable and pushed back by z = sqrt q t.  Likewise, with
Mt = (1 + q t^2) I - t A_X and W_ab = c_a c_b sqrt(S(v_b)/S(v_a)) [Mt^{-1}]_{ab},

    Gamma(z)_{ab} = c_a c_b G(lambda)_{v_a v_b} = sqrt q t W_ab ,
    z Gamma = q t^2 W ,   Gamma/z = W ,   S(z) = (q t^2 W - 1)^{-1} (1 - W),

so the whole scattering matrix is a rational function of t over Q(sqrt(S-ratios)).

SCATTERING MATRIX (C2).  For the generalised eigenfunction with
g(r_k^{(a)}) = delta_{ab} z^{-k} + S_{ab} z^k the junction equation gives
c_a g(v_a) = delta_{ab} + S_{ab} and hence Gamma (z^{-1} + z S) = 1 + S, i.e.

    S(z) = (z Gamma - 1)^{-1} (1 - z^{-1} Gamma) ,   det S(z) = (-1)^h p(z)/ptilde(z),
    ptilde(z) = det((1+z^2) I - z T_X - z^2 C) = z^{2n} p(1/z).

For h = 1 this is 04i's R(z) = -p/ptilde.

MODEL SPACE.  For a scalar inner Theta = (finite Blaschke product over the resonances,
z = 0 included) the model space is K_Theta = {P/qq : deg P < N} with
qq(w) = prod_j (1 - conj(z_j) w); in the basis f_k = w^k/qq the compressed shift
Z = P_K M_w|_K is EXACTLY the companion matrix of prod_j (w - z_j).  Companion matrices
are non-derogatory, so each distinct resonance carries a single Jordan block; spec Z =
the resonances, as 04i fixes the convention.  The Gram matrix of {f_k} is computed from
the Taylor coefficients of 1/qq and Z is pushed to an orthonormal frame by G^{1/2}.
================================================================================
"""
import itertools
import numpy as np
import scipy.linalg as sla
import sympy as sp

np.set_printoptions(linewidth=180, precision=6, suppress=True)
rng = np.random.default_rng(20260920)

CHECKS = 0
FLAGS = []
t_sym, z_sym = sp.symbols('t z')


def check(cond, msg):
    global CHECKS
    CHECKS += 1
    assert cond, f"FAILED  {msg}"
    print(f"  ok {CHECKS:3d}  {msg}")


def flag(msg):
    FLAGS.append(msg)
    print(f"  !! {msg}")


def f6(x):
    return f"{float(x) + 0.0:+.6f}"


def c6(w):
    w = complex(w)
    return f"{w.real + 0.0:+.6f}{w.imag + 0.0:+.6f}j"


def sortc(zs):
    return sorted(zs, key=lambda u: (round(complex(u).real, 9), round(complex(u).imag, 9)))


def clist(zs):
    return "[" + ", ".join(c6(w) for w in sortc(zs)) + "]"


def flist(xs):
    return "[" + ", ".join(f6(x) for x in sorted(float(x) for x in xs)) + "]"


# ============================================================================ #
#  SECTION 0.  The two diagrams                                                #
# ============================================================================ #
#  Transcribed from APW's figures; the PNGs were re-read independently for this
#  script (see notes/elliptic-cavity/numerics.md, ledger D1/D2).
#
#  A diagram is: S(vertex) for the core, (u, v, S(edge)) for the core edges, and
#  (attachment vertex, S(attaching edge), S(c_1)) for each cusp ray.

D2 = dict(
    name="D2  y^2 + y = x^3 + x + 1 over F_2 (Serre, Trees II.2.4.4; APW Fig. 'serre')",
    q=2,
    S={'A': 6, 'B': 2, 'C': 2, 'D': 1, 'E': 3, 'F': 3},
    edges=[('A', 'B', 2), ('B', 'C', 2), ('C', 'D', 1), ('D', 'E', 1), ('D', 'F', 1)],
    cusps=[('B', 2, 4)],                    # attach at B, edge S = 2, ray starts at S = 4
    P=[1, -2, 2],                           # Hasse-Weil numerator P(T) = 1 - 2T + 2T^2
)

D3 = dict(
    name="D3  y^2 = x^3 + x + 1 over F_3 (Takahashi Fig. 5; APW Fig. 'takahashi')",
    q=3,
    S={'L1p': 48, 'L1': 12, 'L2': 6, 'X': 2, 'Xp': 8, 'Y': 6, 'Z': 12, 'Zp': 48, 'Q': 4},
    edges=[('L1p', 'L1', 12), ('L1', 'L2', 6), ('L2', 'X', 2), ('X', 'Xp', 2),
           ('X', 'Y', 2), ('X', 'Q', 2), ('Y', 'Z', 6), ('Z', 'Zp', 12)],
    cusps=[('L1', 12, 36), ('Z', 12, 36), ('Q', 4, 12), ('Q', 4, 12)],
    P=[1, 0, 3],                            # P(T) = 1 + 3T^2
)


def diagram_data(dg):
    """Vertex list, integer adjacency A_X (entries S(v)/S(e)), symmetric T_X,
    cusp couplings c_a^2, and the exit matrix C = sum_a c_a^2 P_{v_a}."""
    S, q = dg['S'], dg['q']
    names = list(S)
    idx = {v: i for i, v in enumerate(names)}
    n = len(names)
    A = sp.zeros(n, n)
    for (u, v, se) in dg['edges']:
        A[idx[u], idx[v]] = sp.Rational(S[u], se)
        A[idx[v], idx[u]] = sp.Rational(S[v], se)
    c2 = [sp.Rational(S[v], se) for (v, se, _s1) in dg['cusps']]
    C = sp.zeros(n, n)
    for (v, se, _s1), cc in zip(dg['cusps'], c2):
        C[idx[v], idx[v]] += cc
    TX = sp.zeros(n, n)
    for (u, v, se) in dg['edges']:
        val = sp.sqrt(sp.Integer(S[u] * S[v])) / (se * sp.sqrt(q))
        TX[idx[u], idx[v]] = val
        TX[idx[v], idx[u]] = val
    return names, idx, A, C, c2, TX


print(__doc__.split("=====")[0].strip())
print("\nseed 20260920;  author claude:opus;  date 2026-09-20\n")
print("=" * 78)
print("SECTION 0   the two diagrams: transcription, degrees, normalisation C1")
print("=" * 78)

DIAG = {}
for dg in (D2, D3):
    names, idx, A, C, c2, TX = diagram_data(dg)
    DIAG[dg['name'][:2]] = (dg, names, idx, A, C, c2, TX)
    q, S = dg['q'], dg['S']
    n = len(names)
    print(f"\n-- {dg['name']}   q = {q}, n = {n} core vertices, h = {len(dg['cusps'])} cusps")

    # ---- degree q+1 at every CORE vertex (core edges + cusp attaching edges)
    degs = {}
    for v in names:
        d = sum(A[idx[v], j] for j in range(n)) + C[idx[v], idx[v]]
        degs[v] = sp.nsimplify(d)
    check(all(degs[v] == q + 1 for v in names),
          f"{dg['name'][:2]}: every CORE vertex has degree sum_e S(v)/S(e) = q+1 = {q+1} "
          f"(degrees {[int(degs[v]) for v in names]})")

    # ---- degree q+1 at every RAY vertex, from the transcribed ray law
    ok_ray = True
    detail = []
    for (v, se, s1) in dg['cusps']:
        # S(c_k) = s1 * q^{k-1}; S(c_k c_{k+1}) = S(c_k); S(v c_1) = se
        d1 = sp.Rational(s1, se) + 1                      # c_1: down-edge then up-edge
        ok_ray = ok_ray and d1 == q + 1
        detail.append((v, se, s1, int(d1)))
        for k in range(2, 7):
            Sk = s1 * q ** (k - 1)
            Skm = s1 * q ** (k - 2)
            dk = sp.Rational(Sk, Skm) + sp.Rational(Sk, Sk)
            ok_ray = ok_ray and dk == q + 1
    check(ok_ray,
          f"{dg['name'][:2]}: every RAY vertex has degree q+1 too; c_1 gives "
          f"S(c_1)/S(e) + 1 = q+1, i.e. S(c_1) = q S(e), verified for each cusp "
          f"{detail}; c_k (k=2..6) gives q + 1 identically")

    # ---- C1: the coupling c^2
    pred = [sp.Rational(S[v] * s1, q * se * se) for (v, se, s1) in dg['cusps']]
    check(all(a == b for a, b in zip(pred, c2)),
          f"{dg['name'][:2]}: c_a^2 = S(v)S(c_1)/(q S(e)^2) = S(v)/S(e) = "
          f"{[str(x) for x in c2]} (the two forms agree because S(c_1) = q S(e))")
    Cd = [sp.nsimplify(C[i, i]) for i in range(n)]
    check(all(x == 1 for x in c2),
          f"{dg['name'][:2]}: EVERY cusp junction has c_a^2 = 1 (not q+1 as at the Nagao "
          f"cusp): the ray attaches where S(v) = S(e).  C = diag{[str(x) for x in Cd]}")

    # ---- C1: the ray really is the free path adjacency after g = f/sqrt S
    L = 9
    Sr = [S[dg['cusps'][0][0]]] + [dg['cusps'][0][2] * q ** k for k in range(L)]
    Se_ = [dg['cusps'][0][1]] + [dg['cusps'][0][2] * q ** k for k in range(L)]
    Aray = np.zeros((L + 1, L + 1))
    for k in range(L):
        Aray[k, k + 1] = Sr[k] / Se_[k]
        Aray[k + 1, k] = Sr[k + 1] / Se_[k]
    Dh = np.diag(np.sqrt(Sr))
    Tray = np.linalg.inv(Dh) @ Aray @ Dh / np.sqrt(q)
    free = np.zeros((L + 1, L + 1))
    for k in range(1, L):
        free[k, k + 1] = free[k + 1, k] = 1.0
    free[0, 1] = free[1, 0] = float(sp.sqrt(c2[0]))
    check(np.max(np.abs(Tray - free)) < 1e-12,
          f"{dg['name'][:2]}: g = f/sqrt(S) then /sqrt q turns the cusp ray into the FREE "
          f"path adjacency (T g)(k) = g(k+1)+g(k-1), with junction weight sqrt(c^2) = "
          f"{float(sp.sqrt(c2[0])):.6f} (max dev {np.max(np.abs(Tray - free)):.1e})")

    # ---- T_X printed
    TXf = np.array(TX.evalf(), dtype=float)
    print(f"   T_X ({n}x{n}) in the order {names}:")
    for i in range(n):
        print("     " + "  ".join(f"{TXf[i, j]:+.5f}" for j in range(n)))
    ent = sorted({sp.nsimplify(TX[i, j]) for i in range(n) for j in range(n) if TX[i, j] != 0},
                 key=lambda e: float(e))
    print(f"   distinct nonzero entries: {[str(e) for e in ent]}")


# ============================================================================ #
#  SECTION 1.  The resonance polynomials p, ptilde (exact) and APW's det H      #
# ============================================================================ #
print("\n" + "=" * 78)
print("SECTION 1   p, ptilde by exact rational arithmetic; APW's det H; z = 0")
print("=" * 78)


def p_exact(A, C, q, extra_C=0):
    """p(sqrt q t) = det((1+q t^2) I - t A_X - C), integer coefficients in t."""
    n = A.shape[0]
    M = (1 + q * t_sym ** 2) * sp.eye(n) - t_sym * A - C
    return sp.expand(M.det(method='berkowitz'))


def to_z(expr, q):
    return sp.expand(sp.nsimplify(expr.subs(t_sym, z_sym / sp.sqrt(q))))


def ptilde_from_p(pz, n):
    return sp.expand(sp.cancel(z_sym ** (2 * n) * pz.subs(z_sym, 1 / z_sym)))


POLY = {}
BRIEF_P = {
    'D2': (z_sym ** 2 / 2) * (z_sym ** 2 - 2) * (z_sym ** 2 + 1) ** 2 * (2 * z_sym ** 4 - 2 * z_sym ** 2 + 1),
    'D3': (z_sym ** 4 / 3) * (z_sym - 1) ** 2 * (z_sym + 1) ** 2 * (z_sym ** 2 - 3)
          * (z_sym ** 2 + 1) ** 2 * (3 * z_sym ** 4 + 1),
}
BRIEF_PT = {
    'D2': -sp.Rational(1, 2) * (z_sym ** 2 + 1) ** 2 * (2 * z_sym ** 2 - 1) * (z_sym ** 4 - 2 * z_sym ** 2 + 2),
    'D3': -sp.Rational(1, 3) * (z_sym - 1) ** 2 * (z_sym + 1) ** 2 * (z_sym ** 2 + 1) ** 2
          * (3 * z_sym ** 2 - 1) * (z_sym ** 4 + 3),
}
APW_DET = {   # exactly as displayed at 2603.26443:final_draft.tex:2008 and :2056
    'D2': (z_sym ** 2 + 1) ** 2 * (z_sym ** 2 - 2) * (2 * z_sym ** 4 - 2 * z_sym ** 2 + 1),
    'D3': (z_sym ** 2 + 1) ** 2 * (z_sym - 1) ** 2 * (z_sym + 1) ** 2 * (z_sym ** 2 - 3)
          * (3 * z_sym ** 4 + 1),
}

for key in ('D2', 'D3'):
    dg, names, idx, A, C, c2, TX = DIAG[key]
    q, n, h = dg['q'], len(names), len(dg['cusps'])
    pt_ = p_exact(A, C, q)
    pz = to_z(pt_, q)
    ptz = ptilde_from_p(pz, n)
    POLY[key] = (pz, ptz)
    print(f"\n-- {key}:  p(z) = {sp.factor(pz)}")
    print(f"   ptilde(z) = {sp.factor(ptz)}")
    check(sp.expand(pz - BRIEF_P[key]) == 0,
          f"{key}: p(z) = det((1+z^2)I - z T_X - C) equals the brief's displayed p EXACTLY "
          f"(difference is the zero polynomial)")
    check(sp.expand(ptz - BRIEF_PT[key]) == 0,
          f"{key}: ptilde(z) = z^(2n) p(1/z) equals the brief's displayed ptilde EXACTLY")
    # independent cross-check: ptilde from its own determinant
    pt2 = to_z(p_exact(A, C * t_sym ** 2 * q / 1, q).subs(t_sym, t_sym), q) if False else None
    Mt = (1 + q * t_sym ** 2) * sp.eye(n) - t_sym * A - q * t_sym ** 2 * C
    ptz2 = to_z(sp.expand(Mt.det(method='berkowitz')), q)
    check(sp.expand(ptz2 - ptz) == 0,
          f"{key}: ptilde computed directly as det((1+z^2)I - z T_X - z^2 C) agrees with "
          f"z^(2n) p(1/z) (both exact)")
    pp = sp.Poly(pz, z_sym)
    check(pp.degree() == 2 * n and pp.LC() == 1,
          f"{key}: deg p = 2n = {2*n} and p is MONIC (leading coefficient {pp.LC()})")
    check(all(pp.coeff_monomial(z_sym ** k) == 0 for k in range(1, 2 * n + 1, 2)),
          f"{key}: p is an EVEN polynomial -- the diagram is a tree, hence bipartite, and "
          f"sigma T_X sigma = -T_X, sigma C sigma = C give p(-z) = p(z); resonances come in "
          f"+- pairs")
    # order of vanishing at 0 and its structural reason
    m = min(k for k in range(2 * n + 1) if pp.coeff_monomial(z_sym ** k) != 0)
    nullity = n - sp.Matrix(sp.eye(n) - C).rank()
    loops = [sp.nsimplify(TX[i, i]) for i in range(n)]
    att = [idx[v] for (v, _se, _s1) in dg['cusps']]
    adj_att = max([abs(float(TX[a, b])) for a in set(att) for b in set(att) if a != b] or [0.0])
    check(m == 2 * nullity and nullity == len({i for i in range(n) if C[i, i] == 1}),
          f"{key}: ord_0 p = {m} = 2 * dim ker(1 - C) = 2 * {nullity}; p(0) = det(1-C) = 0 "
          f"because c_a^2 = 1 at every junction, and the FIRST-order term also vanishes "
          f"because T_X has no loop at an attachment vertex and the attachment vertices are "
          f"pairwise non-adjacent (max |T_X| between them {adj_att:.1e}, loops "
          f"{[str(x) for x in loops]})")
    check(all(x == 0 for x in loops) and adj_att < 1e-15,
          f"{key}: (the two geometric hypotheses just used, verified) no loops and no edges "
          f"among the attachment vertices")
    # APW's det H
    lam = (z_sym + 1 / z_sym)
    HM = sp.Rational(1, 2) * (TX + C / z_sym) - (lam / 2) * sp.eye(n)
    detH = sp.cancel(sp.expand(sp.nsimplify(HM.det(method='berkowitz'))))
    pred = sp.cancel((-1) ** n * (2 * z_sym) ** (-n) * pz)
    check(sp.simplify(detH - pred) == 0,
          f"{key}: det H(mu) = (-1)^n (2 mu)^(-n) det((1+mu^2) - mu T_X - C) EXACTLY, with "
          f"H = (A_L + B(mu))/(2 sqrt q) - z(mu) and B(mu)_vv = c_v sqrt q/mu, c_v = C_vv "
          f"(APW 2603.26443:final_draft.tex:1896-1905).  So APW's mu IS the notebook's z")
    kappa = (-1) ** n * 2 ** n * q * z_sym ** (n - m)
    check(sp.simplify(sp.expand(APW_DET[key] - sp.cancel(kappa * detH))) == 0
          and sp.expand(pz - z_sym ** m * APW_DET[key] / q) == 0,
          f"{key}: APW's DISPLAYED polynomial is NOT det H(mu); it is "
          f"(-1)^n 2^n q mu^(n - ord_0 p) det H(mu) = {sp.factor(kappa)} det H, equivalently "
          f"p(z) = z^{m} * (APW display)/q.  The constant is exactly q and the monomial "
          f"exactly z^(n-m): APW silently drop the z = 0 root and clear denominators")


# ============================================================================ #
#  SECTION 2.  Roots of p: resonances, l^2 spectrum, cusp forms, thresholds     #
# ============================================================================ #
print("\n" + "=" * 78)
print("SECTION 2   the roots of p: resonances, bound states, cusp forms, thresholds")
print("=" * 78)


def build_full_T(dg, names, idx, TX, L):
    """T on core + h truncated rays of length L, in the symmetric normalisation."""
    n = len(names)
    h = len(dg['cusps'])
    N = n + h * L
    T = np.zeros((N, N))
    T[:n, :n] = np.array(TX.evalf(), dtype=float)
    for a, (v, se, s1) in enumerate(dg['cusps']):
        base = n + a * L
        ca = float(sp.sqrt(sp.Rational(dg['S'][v], se)))
        T[idx[v], base] = T[base, idx[v]] = ca
        for k in range(L - 1):
            T[base + k, base + k + 1] = T[base + k + 1, base + k] = 1.0
    return T


ROOTS = {}
for key in ('D2', 'D3'):
    dg, names, idx, A, C, c2, TX = DIAG[key]
    q, n, h = dg['q'], len(names), len(dg['cusps'])
    pz, ptz = POLY[key]
    rp = sp.Poly(pz, z_sym).all_roots() if False else np.roots(
        [complex(c) for c in sp.Poly(pz, z_sym).all_coeffs()])
    rpt = np.roots([complex(c) for c in sp.Poly(ptz, z_sym).all_coeffs()])
    # exact factor bookkeeping instead of numerical matching
    gcd_ = sp.factor(sp.gcd(sp.Poly(pz, z_sym), sp.Poly(ptz, z_sym)).as_expr())
    pred_gcd = {'D2': (z_sym ** 2 + 1) ** 2,
                'D3': (z_sym ** 2 + 1) ** 2 * (z_sym ** 2 - 1) ** 2}[key]
    check(sp.simplify(sp.cancel(gcd_ / pred_gcd)).is_constant(),
          f"{key}: gcd(p, ptilde) = {gcd_} -- the cusp-form factor (z^2+1)^2 "
          f"{'and the threshold factor (z^2-1)^2' if key == 'D3' else '(no threshold factor)'}")
    pred = sp.cancel(pz / gcd_)
    predt = sp.cancel(ptz / gcd_)
    res = [w for w in np.roots([complex(c) for c in sp.Poly(sp.expand(pred), z_sym).all_coeffs()])
           if abs(w) < 1 - 1e-9]
    poles = [w for w in np.roots([complex(c) for c in sp.Poly(sp.expand(predt), z_sym).all_coeffs()])
             if abs(w) < 1 - 1e-9]
    hw = [w for w in res if abs(w) > 1e-9]
    zer = [w for w in res if abs(w) <= 1e-9]
    ROOTS[key] = dict(res=res, hw=hw, zero=zer, poles=poles, red=pred, redt=predt)
    Nexp = {'D2': 6, 'D3': 8}[key]
    check(len(res) == Nexp and len(zer) == {'D2': 2, 'D3': 4}[key],
          f"{key}: N = #resonances (multiplicity, z = 0 included, thresholds excluded) = "
          f"{len(res)} = {len(hw)} Hasse-Weil + {len(zer)} at z = 0 -- the brief's "
          f"N({key}) = {Nexp} is CORRECT")
    mods = sorted(abs(w) for w in hw)
    check(max(mods) - min(mods) < 1e-12 and abs(mods[0] - q ** -0.25) < 1e-12,
          f"{key}: all {len(hw)} Hasse-Weil resonances have modulus q^(-1/4) = "
          f"{q ** -0.25:.9f} (spread {max(mods)-min(mods):.1e}) -- Weil's RH for the curve "
          f"is exactly RH(Y) on this sector")
    ang = sorted(np.angle(w) * 180 / np.pi for w in hw)
    print(f"   {key}: Hasse-Weil resonances {clist(hw)}")
    print(f"        moduli {q ** -0.25:.9f}, angles (deg) {[round(a, 4) for a in ang]}")
    check(all(abs(w) - q ** -0.5 < 1e-12 for w in [abs(u) for u in poles]),
          f"{key}: the poles of det S in the disc are {clist(poles)} = +- q^(-1/2) = "
          f"+-{q ** -0.5:.9f}, the Perron pair")

    # ---- z^2 = 1/alpha
    alph = np.roots([dg['P'][2], dg['P'][1], dg['P'][0]])   # roots of P(T) reversed: 1/alpha
    inv_alpha = sorted(np.roots(dg['P'][::-1]), key=lambda u: u.imag)  # roots of P(T) = 0 -> T
    sq = sortc([w ** 2 for w in hw])
    tgt = sortc(list(inv_alpha) + list(inv_alpha))
    check(max(abs(a - b) for a, b in zip(sq, tgt)) < 1e-12,
          f"{key}: z^2 runs over the roots T of P(T) = {dg['P']}, i.e. z^2 = 1/alpha with "
          f"alpha the Frobenius eigenvalues; each value taken twice ({clist(inv_alpha)})")

    # ---- cusp forms and dim ker T_X
    TXf = np.array(TX.evalf(), dtype=float)
    w_, V_ = np.linalg.eigh(TXf)
    ker = V_[:, np.abs(w_) < 1e-10]
    att = sorted({idx[v] for (v, _se, _s1) in dg['cusps']})
    rowblock = ker[att, :]
    # ABSOLUTE threshold: a relative rcond is meaningless when the block is (nearly) zero
    sv = np.linalg.svd(rowblock, compute_uv=False) if rowblock.size else np.array([])
    ncf = ker.shape[1] - int(np.sum(sv > 1e-8))
    check(ker.shape[1] == {'D2': 2, 'D3': 3}[key] and ncf == 2
          and int(sp.Poly(sp.gcd(sp.Poly(pz, z_sym), sp.Poly(ptz, z_sym)).as_expr()
                          .subs(z_sym, z_sym), z_sym).degree()) >= 2 * ncf,
          f"{key}: dim ker T_X = {ker.shape[1]}, of which {ncf} vanish at EVERY attachment "
          f"vertex {[names[a] for a in att]} -- those {ncf} are the cusp forms, and they are "
          f"exactly the factor (z^2+1)^2 of p (lambda = 0 <-> z = +-i, multiplicity 2 at each)")
    if key == 'D3':
        flag("D3: dim ker T_X = 3 but only 2 kernel vectors are cusp forms; the third does "
             "not vanish at Q and is NOT an l^2 eigenfunction of T on Y.  'dim ker T_X' is "
             "therefore NOT the cusp-form count in general (it is for D2, where all of "
             "ker T_X vanishes at B)")

    # ---- l^2 spectrum on the (truncated) infinite diagram
    for L in (120, 200):
        T = build_full_T(dg, names, idx, TX, L)
        ev, EV = np.linalg.eigh(T)
        out_ = [(ev[i], EV[:, i]) for i in range(len(ev)) if abs(ev[i]) > 2 + 1e-7]
        lam_pred = sorted([float(x + 1 / x) for x in (q ** -0.5, -q ** -0.5)])
        got = sorted(x for x, _ in out_)
        tails = [np.linalg.norm(v[-30:]) for _, v in out_]
        check(len(got) == 2 and max(abs(a - b) for a, b in zip(got, lam_pred)) < 1e-9
              and max(tails) < 1e-8,
              f"{key}: L = {L}: exactly 2 eigenvalues outside [-2,2], lambda = {flist(got)} = "
              f"+-(q^(1/2)+q^(-1/2)) = +-{q ** 0.5 + q ** -0.5:.6f} (the Perron pair), and both "
              f"eigenvectors decay (max tail norm {max(tails):.1e}).  RAM(Y) holds: NO further "
              f"l^2 spectrum outside the band")
        # lambda = 0 is degenerate, so test the SUBSPACE, not individual eigenvectors
        Vz = EV[:, np.abs(ev) < 1e-9]
        rayi = list(range(n, n + h * L))
        sv0 = np.linalg.svd(Vz[rayi, :], compute_uv=False)
        ncf_num = Vz.shape[1] - int(np.sum(sv0 > 1e-8))
        check(ncf_num == ncf,
              f"{key}: L = {L}: dim ker T on Y = {Vz.shape[1]}, and exactly {ncf_num} of it "
              f"vanishes identically on the rays = the {ncf} cusp forms extended by zero "
              f"(APW's 'two l^2 eigenfunctions at each of mu = +-i').  The remaining "
              f"{Vz.shape[1]-ncf_num} zero mode(s) are the bipartite-imbalance artefacts of "
              f"the TRUNCATED rays, not l^2 states"
              + (" -- D3's third kernel vector of T_X lives here" if key == 'D3' else ""))

    # ---- the product identity (04j finding 7, corrected)
    pp = sp.Poly(pz, z_sym)
    m = min(k for k in range(2 * n + 1) if pp.coeff_monomial(z_sym ** k) != 0)
    coef = pp.coeff_monomial(z_sym ** m)
    prod_nonzero = (-1) ** (2 * n - m) * coef / pp.LC()
    check(coef == -1 and prod_nonzero == -1,
          f"{key}: p(0) = det(1-C) = 0, so 04j's identity 'prod of all roots = 1 - c^2' is "
          f"vacuous.  The corrected statement: prod of the NONZERO roots of p = "
          f"(-1)^(2n-m) [z^m] p / lc(p) = {prod_nonzero} (here [z^m]p = {coef} = lead(ptilde))")
    pin = float(np.prod([abs(w) for w in hw]))
    ptr = float(np.prod([abs(w) for w in poles]))
    check(abs(pin - ptr) < 1e-12 and abs(pin - 1.0 / q) < 1e-12,
          f"{key}: hence prod|nonzero resonances| = prod|l^2 parameters| = 1/q = "
          f"{1/q:.6f} ({pin:.9f} vs {ptr:.9f}); with 4 resonances on one circle this FORCES "
          f"r = q^(-1/4).  The Weil radius is pinned by the Perron pair alone")
flag("Section 2: 04j flagged 'nothing pins r to q^(-1/4)'.  On an arithmetic diagram it IS "
     "pinned: [z^m]p = -1 (both diagrams), the only l^2 modes outside the band are the Perron "
     "pair +-q^(-1/2), and the 4 = 4g Hasse-Weil resonances share one modulus, so "
     "r^4 = q^(-1).  For genus g >= 2 the same argument would give r = q^(-1/(4g)), which "
     "CONTRADICTS Weil unless [z^m]p != -1 or there are extra l^2 modes outside the band: a "
     "sharp, testable prediction for a genus-2 diagram.")


# ============================================================================ #
#  SECTION 3.  The h x h scattering matrix                                      #
# ============================================================================ #
print("\n" + "=" * 78)
print("SECTION 3   S(z) from the generalised eigenfunctions: symmetry, unitarity,")
print("            functional equation, det S, and the Childs-Gosset reconciliation")
print("=" * 78)


def S_exact(A, C_unused, Seff, chan, q):
    """Exact S(z) for a (possibly symmetry-reduced) diagram.

    A     : integer non-symmetric adjacency, (A)_{vw} = S(v)/S(e)
    Seff  : list of effective stabiliser sizes (1/nu(v))
    chan  : list of (vertex index, coupling c_a); several channels may share a vertex
    Returns the h x h sympy matrix in z_sym.
    """
    n = A.shape[0]
    h = len(chan)
    Mt = (1 + q * t_sym ** 2) * sp.eye(n) - t_sym * A
    Delta = sp.expand(Mt.det(method='berkowitz'))
    verts = sorted({v for v, _c in chan})
    adj = {}
    for a in verts:
        for b in verts:
            Ms = Mt.copy()
            Ms.col_del(a)
            Ms.row_del(b)
            adj[(a, b)] = sp.expand((-1) ** (a + b) * Ms.det(method='berkowitz'))
    Nu = sp.zeros(h, h)
    for i, (va, ca) in enumerate(chan):
        for j, (vb, cb) in enumerate(chan):
            Nu[i, j] = sp.nsimplify(ca * cb * sp.sqrt(sp.Rational(Seff[vb], Seff[va]))
                                    * adj[(va, vb)])
    Lhs = sp.expand(q * t_sym ** 2 * Nu - Delta * sp.eye(h))
    Rhs = sp.expand(Delta * sp.eye(h) - Nu)
    Sm = Lhs.adjugate() * Rhs
    den = Lhs.det(method='berkowitz')
    Sm = Sm.applyfunc(lambda e: sp.cancel(sp.radsimp(sp.expand(e) / den)))
    return Sm.applyfunc(lambda e: sp.cancel(sp.radsimp(e.subs(t_sym, z_sym / sp.sqrt(q)))))


def S_gamma(dg, names, idx, TX, zval):
    """S(z) numerically from S = (z Gamma - 1)^{-1} (1 - Gamma/z)."""
    n = len(names)
    h = len(dg['cusps'])
    lam = zval + 1.0 / zval
    G = np.linalg.inv(lam * np.eye(n) - np.array(TX.evalf(), dtype=complex))
    Gam = np.zeros((h, h), dtype=complex)
    for a, (va, sea, _s) in enumerate(dg['cusps']):
        for b, (vb, seb, _s2) in enumerate(dg['cusps']):
            ca = float(sp.sqrt(sp.Rational(dg['S'][va], sea)))
            cb = float(sp.sqrt(sp.Rational(dg['S'][vb], seb)))
            Gam[a, b] = ca * cb * G[idx[va], idx[vb]]
    return np.linalg.solve(zval * Gam - np.eye(h), np.eye(h) - Gam / zval), Gam


def S_direct(dg, names, idx, TX, zval, L=14):
    """S(z) by SOLVING T g = (z+1/z) g on core + h rays with the ansatz
    g(r_k^(a)) = delta_{ab} z^{-k} + S_{ab} z^k imposed at the two outermost sites.
    The ansatz solves the free ray recursion exactly, so this is an EXACT linear
    system (any L >= 3 gives the same answer), not a truncation."""
    n = len(names)
    h = len(dg['cusps'])
    lam = zval + 1.0 / zval
    TXf = np.array(TX.evalf(), dtype=complex)
    cs = [float(sp.sqrt(sp.Rational(dg['S'][v], se))) for (v, se, _s) in dg['cusps']]
    M = n + h * L + h                      # g_X, g(rays), S_{.b}
    out = np.zeros((h, h), dtype=complex)
    for b in range(h):
        Amat = np.zeros((M, M), dtype=complex)
        rhs = np.zeros(M, dtype=complex)
        r = 0
        for i in range(n):                 # core
            Amat[r, :n] = TXf[i, :] - lam * np.eye(n)[i, :]
            for a, (v, se, _s) in enumerate(dg['cusps']):
                if idx[v] == i:
                    Amat[r, n + a * L] += cs[a]
            r += 1
        for a, (v, se, _s) in enumerate(dg['cusps']):
            base = n + a * L
            Amat[r, base + 1] = 1.0        # k = 1
            Amat[r, idx[v]] += cs[a]
            Amat[r, base] -= lam
            r += 1
            for k in range(2, L):          # k = 2..L-1
                Amat[r, base + k] = 1.0
                Amat[r, base + k - 2] = 1.0
                Amat[r, base + k - 1] = -lam
                r += 1
            for k in (L - 1, L):           # boundary fit
                Amat[r, base + k - 1] = 1.0
                Amat[r, n + h * L + a] = -zval ** k
                rhs[r] = (zval ** (-k)) if a == b else 0.0
                r += 1
        assert r == M, (r, M)
        x = np.linalg.solve(Amat, rhs)
        out[:, b] = x[n + h * L:]
    return out


SEXACT = {}
for key in ('D2', 'D3'):
    dg, names, idx, A, C, c2, TX = DIAG[key]
    q, n, h = dg['q'], len(names), len(dg['cusps'])
    pz, ptz = POLY[key]
    # --- direct solve vs the Gamma formula
    dev_dir = dev_L = 0.0
    for th in (0.37, 1.1, 2.3, -0.8):
        zv = np.exp(1j * th)
        Sd = S_direct(dg, names, idx, TX, zv, L=14)
        Sd2 = S_direct(dg, names, idx, TX, zv, L=30)
        Sg, _ = S_gamma(dg, names, idx, TX, zv)
        dev_dir = max(dev_dir, np.max(np.abs(Sd - Sg)))
        dev_L = max(dev_L, np.max(np.abs(Sd - Sd2)))
    check(dev_dir < 1e-9 and dev_L < 1e-9,
          f"{key}: the brief's S(z) = (z Gamma - 1)^(-1)(1 - z^(-1) Gamma) reproduces the "
          f"DIRECT generalised-eigenfunction solve at 4 points of |z| = 1 (max dev "
          f"{dev_dir:.1e}); L = 14 and L = 30 agree to {dev_L:.1e}, so the solve is exact")
    # --- symmetry, unitarity, functional equation, reality
    for th in (0.4, 1.7, 2.9):
        zv = np.exp(1j * th)
        Sv, _ = S_gamma(dg, names, idx, TX, zv)
        Si, _ = S_gamma(dg, names, idx, TX, 1 / zv)
        check(np.max(np.abs(Sv - Sv.T)) < 1e-10,
              f"{key}: S = S^T at z = e^(i{th}) (dev {np.max(np.abs(Sv - Sv.T)):.1e})")
        check(np.max(np.abs(Sv.conj().T @ Sv - np.eye(h))) < 1e-9,
              f"{key}: S is UNITARY on |z| = 1 at z = e^(i{th}) (dev "
              f"{np.max(np.abs(Sv.conj().T @ Sv - np.eye(h))):.1e})")
        check(np.max(np.abs(Sv @ Si - np.eye(h))) < 1e-9,
              f"{key}: the functional equation S(z) S(1/z) = 1 at z = e^(i{th}) (dev "
              f"{np.max(np.abs(Sv @ Si - np.eye(h))):.1e})")
    for zv in (0.5 + 0.31j, 1.4 - 0.9j):
        Sa, _ = S_gamma(dg, names, idx, TX, zv)
        Sb, _ = S_gamma(dg, names, idx, TX, np.conj(zv))
        check(np.max(np.abs(Sb - Sa.conj())) < 1e-10,
              f"{key}: S(conj z) = conj S(z) at z = {c6(zv)}, i.e. S is rational with REAL "
              f"coefficients (dev {np.max(np.abs(Sb - Sa.conj())):.1e})")
    # --- det S = (-1)^h p/ptilde  (exact, at exact rational points)
    devd = 0.0
    for zv in (0.37 + 0.21j, -0.8 + 1.3j, 2.1 - 0.4j):
        Sv, _ = S_gamma(dg, names, idx, TX, zv)
        tgt = (-1) ** h * complex(pz.subs(z_sym, zv) / ptz.subs(z_sym, zv))
        devd = max(devd, abs(np.linalg.det(Sv) - tgt))
    check(devd < 1e-9,
          f"{key}: det S(z) = (-1)^h p(z)/ptilde(z) with h = {h} at 3 points off the circle "
          f"(max dev {devd:.1e}); Sylvester: det_h(1 - z Gamma) = det_n(1 - z G C)")

# ---- exact S for D2 (h = 1: S = R)
dg, names, idx, A, C, c2, TX = DIAG['D2']
Seff2 = [dg['S'][v] for v in names]
S2 = S_exact(A, C, Seff2, [(idx['B'], sp.Integer(1))], 2)
R2 = sp.factor(sp.cancel(S2[0, 0]))
SEXACT['D2'] = S2
pz2, ptz2 = POLY['D2']
print(f"\n   D2 exact:  R(z) = {R2}")
check(sp.simplify(R2 + sp.cancel(pz2 / ptz2)) == 0,
      f"D2: R(z) = -p(z)/ptilde(z) EXACTLY (04i's sign, no extra power of z)")
brief_R = (z_sym ** 2 * (z_sym ** 2 - 2) * (2 * z_sym ** 4 - 2 * z_sym ** 2 + 1)
           / ((2 * z_sym ** 2 - 1) * (z_sym ** 4 - 2 * z_sym ** 2 + 2)))
check(sp.simplify(R2 - brief_R) == 0,
      "D2: and it equals the brief's displayed R(z) = z^2 (z^2-2)(2z^4-2z^2+1)/"
      "((2z^2-1)(z^4-2z^2+2)) EXACTLY -- T1(a) is CORRECT")

# ---- Childs-Gosset:  S_CG(z) = -Q(z)^{-1} Q(1/z),  Q = 1 - z(A + B^dag (1/z+z-D)^{-1} B)
print("\n-- reconciliation with Childs--Gosset (1203.6557:levinson2.tex:365)")


def S_CG(TXf, att, zval):
    """Childs--Gosset S for a core with ONE tail of weight 1 at each vertex in att."""
    nn = TXf.shape[0]
    rest = [i for i in range(nn) if i not in att]
    Ab = TXf[np.ix_(att, att)]
    Bb = TXf[np.ix_(rest, att)]
    Db = TXf[np.ix_(rest, rest)]
    lam = zval + 1.0 / zval
    Meff = Ab + Bb.conj().T @ np.linalg.solve(lam * np.eye(len(rest)) - Db, Bb)
    Q = np.eye(len(att)) - zval * Meff
    Qi = np.eye(len(att)) - (1 / zval) * Meff
    return -np.linalg.solve(Q, Qi)


dev_cg = 0.0
for th in (0.5, 1.9, -1.1):
    zv = np.exp(1j * th)
    Sg, _ = S_gamma(DIAG['D2'][0], names, idx, TX, zv)
    Scg = S_CG(np.array(TX.evalf(), dtype=complex), [idx['B']], zv)
    dev_cg = max(dev_cg, abs(Sg[0, 0] - zv ** 2 * Scg[0, 0]))
check(dev_cg < 1e-10,
      f"D2: S_notebook(z) = z^2 * S_ChildsGosset(z) EXACTLY (dev {dev_cg:.1e}).  The factor is "
      f"an ORIGIN SHIFT of the tail coordinate, not a discrepancy: Childs--Gosset put the "
      f"incoming wave z^(-(j+1)) at tail site j with j = 0 the ATTACHMENT vertex "
      f"(1203.6557:levinson2.tex:340-346), while the notebook puts z^(-k) at ray site k >= 1 "
      f"with the attachment vertex outside the ray.  Both are unitary; the brief's "
      f"'reconcile' has the answer z^2, and a scattering function is only defined up to a "
      f"power of z (04i numerics D13)")
# a 3-tail random test that the identity is general (distinct attachment vertices, c = 1)
rc = rng.normal(size=(6, 6))
rc = np.round(0.5 * (rc + rc.T), 3)
att3 = [0, 2, 4]
dg_fake = dict(S={f"v{i}": 1 for i in range(6)}, q=1,
               cusps=[(f"v{i}", 1, 1) for i in att3], edges=[])
names_f = [f"v{i}" for i in range(6)]
idx_f = {v: i for i, v in enumerate(names_f)}
dev_cg3 = 0.0
for th in (0.6, 2.2):
    zv = np.exp(1j * th)
    Sg, _ = S_gamma(dg_fake, names_f, idx_f, sp.Matrix(rc), zv)
    Scg = S_CG(rc.astype(complex), att3, zv)
    dev_cg3 = max(dev_cg3, np.max(np.abs(Sg - zv ** 2 * Scg)))
check(dev_cg3 < 1e-9,
      f"general: on a random 6-vertex core with THREE tails at distinct vertices and c = 1, "
      f"S_notebook = z^2 S_ChildsGosset as 3x3 matrices (dev {dev_cg3:.1e}); the shift is the "
      f"same scalar z^2 in every channel")
flag("Childs--Gosset's setup attaches at most one tail per vertex, so D3 (TWO cusps at Q) is "
     "outside it as written; the Gamma-form S = (z Gamma - 1)^{-1}(1 - Gamma/z) still applies, "
     "and there Gamma is SINGULAR (rank 3 < h = 4) -- which is exactly what makes the "
     "antisymmetric Q-channel a Dirichlet end.")

# ---- Levinson count
print("\n-- Levinson (1203.6557:levinson2.tex:511): w(det S) = 2(m - n_b - n_c - n_h/2)")
for key in ('D2', 'D3'):
    dg, names, idx, A, C, c2, TX = DIAG[key]
    n, h = len(names), len(dg['cusps'])
    pz, ptz = POLY[key]
    th = np.linspace(0, 2 * np.pi, 20001)[:-1]
    vals = np.array([complex(np.linalg.det(S_gamma(dg, names, idx, TX, np.exp(1j * a))[0]))
                     for a in th])
    wind = int(round(np.sum(np.diff(np.unwrap(np.angle(np.append(vals, vals[0]))))) / (2 * np.pi)))
    n_b, n_c = 2, 2
    n_h = {'D2': 0, 'D3': 4}[key]
    pred = 2 * (n - n_b - n_c - n_h // 2)
    Nres = len(ROOTS[key]['res'])
    check(wind == pred == Nres - n_b,
          f"{key}: winding of det S round |z| = 1 is {wind} = 2(m - n_b - n_c - n_h/2) = "
          f"2({n} - {n_b} - {n_c} - {n_h}/2) = #resonances - #visible bound states = "
          f"{Nres} - {n_b}.  The threshold multiplicity n_h = {n_h} is exactly APW's "
          f"'topological resonances at mu = +-1 of multiplicity 2' (D3) / their absence (D2)")


# ============================================================================ #
#  SECTION 4.  The zeta identification                                          #
# ============================================================================ #
print("\n" + "=" * 78)
print("SECTION 4   1/R and det S_even against the zeta function of the function field")
print("=" * 78)


def zeta_ratios(P, q):
    """(zeta_K(2s-1), zeta_K(2s)) as exact rational functions of z, using
    z = q^(s-1/2), i.e. q^(-2s) = z^(-2)/q, q^(1-2s) = z^(-2)."""
    def Pv(T):
        return sum(sp.Integer(P[k]) * T ** k for k in range(len(P)))
    u = z_sym ** -2
    z2s = Pv(u / q) / ((1 - u / q) * (1 - u))            # zeta_K(2s)
    z2s1 = Pv(u) / ((1 - u) * (1 - q * u))               # zeta_K(2s-1)
    return sp.cancel(sp.together(z2s1)), sp.cancel(sp.together(z2s))


for key, tag in (('D2', 'q=2, P(T) = 1 - 2T + 2T^2'), ('D3', 'q=3, P(T) = 1 + 3T^2')):
    dg = DIAG[key][0]
    q = dg['q']
    Z1, Z0 = zeta_ratios(dg['P'], q)
    # numeric sanity of the dictionary z = q^{s-1/2}
    def zetaK(s):
        Pv = sum(dg['P'][k] * (q ** (-s)) ** k for k in range(len(dg['P'])))
        return Pv / ((1 - q ** (-s)) * (1 - q ** (1 - s)))
    dev = 0.0
    for sv in (0.31 + 0.22j, 0.77 - 0.4j, 1.3 + 0.9j):
        zv = q ** (sv - 0.5)
        dev = max(dev, abs(complex(Z1.subs(z_sym, zv)) - zetaK(2 * sv - 1)),
                  abs(complex(Z0.subs(z_sym, zv)) - zetaK(2 * sv)))
    check(dev < 1e-10,
          f"{key} ({tag}): the rational functions used below really are zeta_K(2s-1) and "
          f"zeta_K(2s) under z = q^(s-1/2), checked at 3 complex s (max dev {dev:.1e})")

# ---- T1(b): 1/R = z^{-2} zeta_K(2s-1)/zeta_K(2s)
dg = DIAG['D2'][0]
Z1, Z0 = zeta_ratios(dg['P'], 2)
target = sp.cancel(z_sym ** -2 * Z1 / Z0)
check(sp.simplify(sp.cancel(1 / R2 - target)) == 0,
      "T1(b) D2: 1/R(z) = z^(-2) zeta_K(2s-1)/zeta_K(2s) EXACTLY, K = F_2(E) -- as a "
      "rational-function identity, not just at sample points")
check(sp.simplify(sp.cancel(R2 - target)) != 0,
      "T1(b) D2: and it is 1/R, not R (the two differ); the prefactor is the monomial "
      "z^(-2) = q^(1-2s), against q = q^(1-0) for the pure Nagao cusp (04i C3)")
dev = 0.0
for sv in (0.31 + 0.22j, 0.77 - 0.4j, 1.3 + 0.9j, 0.5 + 14.13j):
    zv = 2 ** (sv - 0.5)
    Sv, _ = S_gamma(dg, DIAG['D2'][1], DIAG['D2'][2], DIAG['D2'][6], zv)
    dev = max(dev, abs(1 / Sv[0, 0] - complex(target.subs(z_sym, zv))))
check(dev < 1e-8,
      f"T1(b) D2: the same, evaluated at 4 complex s including s = 1/2 + 14.13i, against the "
      f"scattering matrix computed from Gamma (max dev {dev:.1e})")
flag("T1(b) H-EIS: with only two data points (genus 0: prefactor q = q^(1-2gs)|_{g=0}; genus 1: "
     "z^(-2) = q^(1-2s) = q^(1-2gs)|_{g=1}) the pattern q^(1-2gs) fits, but D3's even block "
     "below gives the prefactor z^(+2) = q^(2s-1) for the RECIPROCAL ratio, i.e. the same "
     "q^(1-2s) attached to zeta(2s-1)/zeta(2s).  Two genus-1 points and one genus-0 point "
     "cannot separate q^(1-2gs) from q^(1-2s); H-EIS stays unasserted.")


# ============================================================================ #
#  SECTION 5.  D3: the Klein symmetry, the three channels, H-CLASS              #
# ============================================================================ #
print("\n" + "=" * 78)
print("SECTION 5   D3: Klein block structure of S(z), the -1 and z^2 channels,")
print("            the even 2x2 block and the monomial renormalisation (H-CLASS)")
print("=" * 78)

dg3, names3, idx3, A3, C3, c23, TX3 = DIAG['D3']
SIG = {'L1p': 'Zp', 'Zp': 'L1p', 'L1': 'Z', 'Z': 'L1', 'L2': 'Y', 'Y': 'L2',
       'X': 'X', 'Xp': 'Xp', 'Q': 'Q'}
TX3f = np.array(TX3.evalf(), dtype=float)
Pm = np.zeros((9, 9))
for v in names3:
    Pm[idx3[SIG[v]], idx3[v]] = 1.0
check(np.max(np.abs(Pm @ TX3f @ Pm.T - TX3f)) < 1e-12 and np.max(np.abs(Pm @ Pm - np.eye(9))) < 1e-12,
      "D3: sigma (L1p<->Zp, L1<->Z, L2<->Y, fixing X, Xp, Q) is an involutive automorphism of "
      "the weighted core: P T_X P^T = T_X exactly; together with the swap tau of the two "
      "Q-cusps (which acts trivially on the core) it generates a Klein four-group")

# ---- reduced diagrams from the involution (built programmatically, not transcribed)
orbits, seen = [], set()
for v in names3:
    if v in seen:
        continue
    o = (v,) if SIG[v] == v else (v, SIG[v])
    orbits.append(o)
    seen |= set(o)
two = [o for o in orbits if len(o) == 2]
Aev = sp.zeros(len(orbits), len(orbits))
for i, o1 in enumerate(orbits):
    for j, o2 in enumerate(orbits):
        Aev[i, j] = sum(A3[idx3[o1[0]], idx3[w]] for w in o2)
Sev = [sp.Rational(dg3['S'][o[0]], len(o)) for o in orbits]
Cev = sp.diag(*[sum(sp.Rational(dg3['S'][v], se) for (v, se, _s) in dg3['cusps'] if v == o[0])
                for o in orbits])
Aod = sp.zeros(len(two), len(two))
for i, o1 in enumerate(two):
    for j, o2 in enumerate(two):
        Aod[i, j] = A3[idx3[o1[0]], idx3[o2[0]]] - A3[idx3[o1[0]], idx3[o2[1]]]
Sod = [sp.Rational(dg3['S'][o[0]], 2) for o in two]
Cod = sp.diag(*[sum(sp.Rational(dg3['S'][v], se) for (v, se, _s) in dg3['cusps'] if v == o[0])
                for o in two])
print(f"   sigma-orbits: {[o for o in orbits]}")
print(f"   A_even =\n{np.array(Aev).astype(int)}\n   S_eff(even) = {[str(x) for x in Sev]}, "
      f"C_even = diag{[str(Cev[i, i]) for i in range(len(orbits))]}")
print(f"   A_odd  =\n{np.array(Aod).astype(int)}\n   S_eff(odd)  = {[str(x) for x in Sod]}, "
      f"C_odd  = diag{[str(Cod[i, i]) for i in range(len(two))]}")
check(all(sum(Aev[i, j] for j in range(len(orbits))) + Cev[i, i] == 4 for i in range(len(orbits))),
      "D3 even block: every reduced vertex still has degree q+1 = 4 (the reduction preserves "
      "the tree-quotient normalisation)")

pev = to_z(sp.expand(((1 + 3 * t_sym ** 2) * sp.eye(len(orbits)) - t_sym * Aev - Cev)
                     .det(method='berkowitz')), 3)
pod = to_z(sp.expand(((1 + 3 * t_sym ** 2) * sp.eye(len(two)) - t_sym * Aod - Cod)
                     .det(method='berkowitz')), 3)
pz3, ptz3 = POLY['D3']
check(sp.expand(pev * pod - pz3) == 0,
      f"D3: p = p_even * p_odd exactly, with p_even = {sp.factor(pev)} and "
      f"p_odd = {sp.factor(pod)}")
ptod = ptilde_from_p(pod, len(two))
check(sp.expand(pod + z_sym ** 2 * ptod) == 0,
      f"T2(b) D3: p_odd(z) = -z^2 ptilde_odd(z) EXACTLY (ptilde_odd = {sp.factor(ptod)}); "
      f"hence R_odd = -p_odd/ptilde_odd = +z^2 identically.  The reason is visible in "
      f"p_odd = z^2(z^2-1)(z^2+1) = z^2(z^4-1); the odd core {tuple(o[0] for o in two)} is a "
      f"3-path with a Dirichlet condition at X and the c = 1 cusp in the MIDDLE")
a1s, a2s = sp.symbols('a1 a2', positive=True)
Mgen = sp.Matrix([[1 + z_sym ** 2, -z_sym * a1s, 0],
                  [-z_sym * a1s, z_sym ** 2, -z_sym * a2s],
                  [0, -z_sym * a2s, 1 + z_sym ** 2]])
pg = sp.expand(Mgen.det())
ptg = sp.expand(sp.cancel(z_sym ** 6 * pg.subs(z_sym, 1 / z_sym)))
cond = sp.factor(sp.expand(pg + z_sym ** 2 * ptg))
check(sp.simplify(sp.expand(cond.subs(a2s, sp.sqrt(2 - a1s ** 2)))) == 0,
      f"T2(b) D3, the REASON: for ANY 3-path core with the c = 1 cusp in the middle and "
      f"couplings a_1, a_2, p + z^2 ptilde = {cond}, which vanishes identically iff "
      f"a_1^2 + a_2^2 = 2.  There is no hidden transparency, just this one identity")
check(sp.nsimplify(TX3[idx3['L1p'], idx3['L1']] ** 2 + TX3[idx3['L1'], idx3['L2']] ** 2) == 2,
      f"T2(b) D3: and that sum really is 2 for the transcribed weights "
      f"(a_1^2 = {sp.nsimplify(TX3[idx3['L1p'], idx3['L1']] ** 2)}, "
      f"a_2^2 = {sp.nsimplify(TX3[idx3['L1'], idx3['L2']] ** 2)})")

# ---- exact S in the three channels
S_odd = S_exact(Aod, Cod, Sod, [(0 if two[0][0] == 'L1' else [o[0] for o in two].index('L1'),
                                 sp.Integer(1))], 3)
iL1 = [o[0] for o in two].index('L1')
S_odd = S_exact(Aod, Cod, Sod, [(iL1, sp.Integer(1))], 3)
check(sp.simplify(S_odd[0, 0] - z_sym ** 2) == 0,
      f"T2(b) D3: the antisymmetric (L1 - Z)/sqrt2 channel has S = +z^2 IDENTICALLY, as an "
      f"exact rational-function identity (the brief found it at three points; it is exact)")
iL1e = [o[0] for o in orbits].index('L1')
iQe = [o[0] for o in orbits].index('Q')
S_even = S_exact(Aev, Cev, Sev, [(iL1e, sp.Integer(1)), (iQe, sp.sqrt(2))], 3)
S_even = S_even.applyfunc(lambda e: sp.factor(sp.cancel(e)))
print("\n   S_even(z) (basis (L1+Z)/sqrt2 , (Q1+Q2)/sqrt2):")
for i in range(2):
    print("     [" + ",   ".join(str(S_even[i, j]) for j in range(2)) + "]")
check(sp.simplify(S_even[0, 1] - S_even[1, 0]) == 0,
      "D3: S_even is symmetric (exactly)")
check(sp.simplify(S_even[0, 0] - z_sym ** 2 * S_even[1, 1]) == 0,
      "D3: S_even has the EXACT internal relation (S_even)_11 = z^2 (S_even)_22 -- this single "
      "fact is what makes the monomial renormalisation below work, and what makes the "
      "unrenormalised eigenvectors z-dependent")
Z1, Z0 = zeta_ratios(dg3['P'], 3)
tgt = sp.cancel(z_sym ** 2 * Z0 / Z1)
check(sp.simplify(sp.cancel(S_even.det() - tgt)) == 0,
      "T2(b) D3: det S_even(z) = z^2 zeta_K(2s)/zeta_K(2s-1) EXACTLY, K = F_3(E), "
      "P(T) = 1 + 3T^2 -- the brief's claim is CORRECT (and it is the RECIPROCAL of D2's 1/R "
      "form, prefactor z^(+2))")

# ---- block structure of the full 4x4 S in the Klein basis
r2 = np.sqrt(2.0)
Bk = np.array([[1, 1, 0, 0], [1, -1, 0, 0], [0, 0, 1, 1], [0, 0, 1, -1]], dtype=float).T / r2
LBL = ['e+ = (L1+Z)/r2', 'e- = (L1-Z)/r2', 'f+ = (Q1+Q2)/r2', 'f- = (Q1-Q2)/r2']
for zv in (0.63 + 0.29j, np.exp(1.1j), 1.7 - 0.5j):
    Sv, Gam = S_gamma(dg3, names3, idx3, TX3, zv)
    Sb = Bk.T @ Sv @ Bk
    off = max(abs(Sb[i, j]) for i in range(4) for j in range(4)
              if (i, j) not in [(0, 0), (0, 2), (2, 0), (2, 2), (1, 1), (3, 3)])
    check(off < 1e-10,
          f"T2(b) D3: in the FIXED (z-independent) Klein basis {LBL} S(z) is block diagonal "
          f"1 + 1 + 2 at z = {c6(zv)} (largest forbidden entry {off:.1e})")
    check(abs(Sb[3, 3] + 1) < 1e-10,
          f"T2(b) D3: the f- channel has S = -1 exactly at z = {c6(zv)} "
          f"(|S+1| = {abs(Sb[3, 3] + 1):.1e}) -- Gamma annihilates f- (rank Gamma = "
          f"{np.linalg.matrix_rank(Gam, tol=1e-9)} < h = 4), a Dirichlet end")
    check(abs(Sb[1, 1] - zv ** 2) < 1e-10,
          f"T2(b) D3: the e- channel has S = z^2 at z = {c6(zv)} (dev "
          f"{abs(Sb[1, 1] - zv ** 2):.1e})")
    ev_blk = np.array([[complex(S_even[0, 0].subs(z_sym, zv)), complex(S_even[0, 1].subs(z_sym, zv))],
                       [complex(S_even[1, 0].subs(z_sym, zv)), complex(S_even[1, 1].subs(z_sym, zv))]])
    check(np.max(np.abs(np.array([[Sb[0, 0], Sb[0, 2]], [Sb[2, 0], Sb[2, 2]]]) - ev_blk)) < 1e-9,
          f"D3: the 2x2 even block of the full S equals the exact S_even computed from the "
          f"reduced 6-vertex diagram at z = {c6(zv)} (dev "
          f"{np.max(np.abs(np.array([[Sb[0,0],Sb[0,2]],[Sb[2,0],Sb[2,2]]]) - ev_blk)):.1e})")

# ---- T2(d): are the eigenvectors of S_even z-independent?  the monomial renormalisation
print("\n-- T2(d) H-CLASS: eigenvectors of S_even, and D(z) = diag(z^a, z^b)")
zs_test = [0.8 + 0.1j, 0.35 - 0.62j, np.exp(0.77j), 1.9 + 0.3j]


def Seven_num(zv):
    return np.array([[complex(S_even[i, j].subs(z_sym, zv)) for j in range(2)] for i in range(2)])


ev_ref = None
comm = 0.0
for zv in zs_test:
    M1 = Seven_num(zs_test[0])
    M2 = Seven_num(zv)
    comm = max(comm, np.max(np.abs(M1 @ M2 - M2 @ M1)))
check(comm > 1e-3,
      f"T2(d) D3: the RAW S_even(z) does NOT have z-independent eigenvectors -- "
      f"||[S_even(z_1), S_even(z_2)]|| up to {comm:.4f}; the brief is right that the naive "
      f"H-CLASS reading fails")
w0 = np.linalg.eigvals(Seven_num(0.8 + 0.1j))
print(f"   eigenvalues of S_even at z = 0.8+0.1i: {clist(w0)}  "
      f"(the brief quotes -1.19997+0.27727i and 0.80005+0.10680i)")
check(min(abs(w0[0] - (-1.19997 + 0.27727j)), abs(w0[1] - (-1.19997 + 0.27727j))) < 2e-4
      and min(abs(w0[0] - (0.80005 + 0.10680j)), abs(w0[1] - (0.80005 + 0.10680j))) < 2e-4,
      "T2(d) D3: those are exactly the brief's two quoted numbers, so the brief's S_even and "
      "this one are the same matrix (independent confirmation of the transcription)")

# scan the monomial renormalisation: only the DIFFERENCE m = a - b can matter
best = []
for m2 in range(-8, 9):                       # m = m2/2, half-integers included
    m = sp.Rational(m2, 2)
    expr = sp.cancel(sp.simplify((z_sym ** m * S_even[0, 0] - z_sym ** -m * S_even[1, 1])
                                 / S_even[0, 1]))
    if expr.is_constant():
        best.append((m, expr))
check(len(best) == 1 and best[0][0] == -1,
      f"T2(d) D3: scanning a - b over the half-integers in [-4, 4], the ratio "
      f"(z^(a-b) S_11 - z^(b-a) S_22)/S_12 is CONSTANT for exactly one value, a - b = "
      f"{best[0][0]} (value {best[0][1]}).  So YES, a diagonal monomial renormalisation "
      f"D(z) = diag(z^a, z^(a+1)) makes D S_even D have z-INDEPENDENT eigenvectors "
      f"(1, +-1)/sqrt2, and only the difference a - b matters")
Dz = sp.diag(1, z_sym)
M = (Dz * S_even * Dz).applyfunc(lambda e: sp.factor(sp.cancel(e)))
check(sp.simplify(M[0, 0] - M[1, 1]) == 0,
      f"T2(d) D3: with D = diag(1, z) the renormalised block has EQUAL diagonal entries "
      f"{sp.factor(M[0,0])}, so it is (scalar) + (off-diagonal) * sigma_x")
lam_p = sp.factor(sp.cancel(M[0, 0] + M[0, 1]))
lam_m = sp.factor(sp.cancel(M[0, 0] - M[0, 1]))
check(sp.simplify(lam_m - z_sym ** 2) == 0,
      f"T2(d) D3: the eigenvalue on (1,-1)/sqrt2 is EXACTLY z^2 = {lam_m} -- a pure monomial")
check(sp.simplify(lam_p - sp.cancel(z_sym ** 2 * Z0 / Z1)) == 0,
      f"T2(d) D3: the eigenvalue on (1,1)/sqrt2 is EXACTLY z^2 zeta_K(2s)/zeta_K(2s-1) = "
      f"{lam_p} = det S_even.  H-CLASS is CONFIRMED for D3: after the monomial "
      f"renormalisation the four channels carry {{-z^2, z^2, z^2, z^2 zeta_K(2s)/zeta_K(2s-1)}}, "
      f"i.e. ONE zeta block and THREE monomial blocks, exactly the prediction for g = 1 where "
      f"L(s, chi) = 1 for the three nontrivial unramified characters")
check(sp.simplify(sp.cancel(lam_p * lam_m - z_sym ** 2 * S_even.det())) == 0,
      "T2(d) D3: consistency, the product of the two renormalised eigenvalues is "
      "det(D)^2 det S_even = z^2 det S_even")
flag("T2(d) D3: the brief GUESSED the renormalisation from 'the two Q-cusps start one step "
     "deeper (12, 36, ...) than the L1, Z cusps (36, 108, ...)'.  That is exactly right: "
     "a - b = -1 is one ray step, D = diag(1, 1, z, z) on the four channels re-bases the two "
     "Q-rays one site outwards.  The four eigenvalues then become z^2 * {1, 1, -1, "
     "zeta_K(2s)/zeta_K(2s-1)} (the f- channel's -1 becomes -z^2 under the same D).")

# ---- thresholds
print("\n-- T2(c) the thresholds z = +-1")
for eps in (1e-5, 1e-7):
    for sgn in (+1, -1):
        zv = sgn * (1 - eps)
        Sv, _ = S_gamma(dg3, names3, idx3, TX3, zv + 0j)
        Sb = Bk.T @ Sv @ Bk
        lim = np.array([[0.0, -float(sgn)], [-float(sgn), 0.0]])
        got = np.array([[Sb[0, 0], Sb[0, 2]], [Sb[2, 0], Sb[2, 2]]])
        check(np.max(np.abs(got - lim)) < 60 * eps,
              f"T2(c) D3: S_even(z) is REGULAR at z = {sgn:+d} (multiplicity-2 threshold): at "
              f"z = {sgn}(1-{eps:g}) the even block is {np.round(got.real, 6).tolist()}, "
              f"limit {lim.tolist()} = -sgn * sigma_x (dev {np.max(np.abs(got - lim)):.1e}); "
              f"det S_even(+-1) = -1, and the eigenvalues of the FULL S(+-1) are "
              f"{{+1, -1}} (even) + {{+1}} (e-) + {{-1}} (f-)")
Sev1 = Seven_num(1 - 1e-9)
trS1 = float((Sev1[0, 0] + Sev1[1, 1]).real) + 1.0 - 1.0
check(abs(trS1) < 1e-6,
      f"T2(c) D3: tr S(+1) = tr(even) + 1 + (-1) = {trS1:.2e} = 0, and "
      f"(h + tr S(+1))/2 = (4 + 0)/2 = 2 reproduces APW's threshold multiplicity 2 at mu = +1")
R2_1 = complex(R2.subs(z_sym, 1))
check(abs(R2_1 + 1) < 1e-12 and abs((1 + R2_1.real) / 2) < 1e-12,
      f"T2(c) D2: S(1) = R(1) = {R2_1.real:+.1f} (p(+-1) != 0 there), so (h + tr S)/2 = "
      f"(1 - 1)/2 = 0 -- D2 has NO threshold resonance, also reproduced.  Two data points "
      f"for 'multiplicity at z = +-1 = (h + tr S(+-1))/2'; not asserted")


# ============================================================================ #
#  SECTION 6.  D2: the one-exit contraction Z on the model space K              #
# ============================================================================ #
print("\n" + "=" * 78)
print("SECTION 6   D2: the model space K, the contraction Z, the exit j, the Gram")
print("=" * 78)


def blaschke_model(zs, M=4000):
    """Sz.-Nagy--Foias model of the compressed shift on K_Theta, Theta the finite
    Blaschke product with zero multiset zs (z = 0 allowed).  Basis f_k = w^k/qq(w),
    qq(w) = prod (1 - conj(z_j) w); Z = P_K M_w|_K is the COMPANION matrix of
    prod (w - z_j) in that basis; G is the Gram matrix; Z is pushed to an
    orthonormal frame."""
    zs = np.array(zs, dtype=complex)
    N = len(zs)
    Pc = np.poly(zs)                       # monic, high-to-low
    qq = np.poly(1.0 / np.conj(zs[np.abs(zs) > 1e-14])) if False else None
    # qq(w) = prod (1 - conj(z_j) w): build its coefficients low-to-high
    qc = np.array([1.0 + 0j])
    for zj in zs:
        qc = np.convolve(qc, np.array([1.0, -np.conj(zj)]))
    # Taylor coefficients of 1/qq by the recursion qq * c = 1
    c = np.zeros(M, dtype=complex)
    c[0] = 1.0 / qc[0]
    for m in range(1, M):
        c[m] = -sum(qc[i] * c[m - i] for i in range(1, min(len(qc), m + 1))) / qc[0]
    G = np.zeros((N, N), dtype=complex)
    for k in range(N):
        for l in range(N):
            G[k, l] = np.sum(c[:M - max(k, l)] * np.conj(
                np.roll(c, k - l)[:M - max(k, l)])) if False else \
                np.sum(c[max(0, l - k):M - k] * np.conj(c[max(0, k - l):M - l]))
    G = 0.5 * (G + G.conj().T)
    Zc = np.zeros((N, N), dtype=complex)
    for k in range(1, N):
        Zc[k, k - 1] = 1.0
    for k in range(N):
        Zc[k, N - 1] -= Pc[N - k]          # P(w) = w^N + sum_k Pc[N-k] w^k
    ev, U = np.linalg.eigh(G)
    Gh = U @ np.diag(np.sqrt(ev)) @ U.conj().T
    Gi = U @ np.diag(1 / np.sqrt(ev)) @ U.conj().T
    Z = Gh @ Zc @ Gi
    return Z, G, Gh, Gi, ev


res2 = ROOTS['D2']['res']
hw2 = sortc(ROOTS['D2']['hw'])
zs_full = list(hw2) + [0.0, 0.0]
Zf, Gf, Ghf, Gif, evG = blaschke_model(zs_full)
Nf = len(zs_full)
chp = np.poly(Zf)
check(np.max(np.abs(chp - np.poly(np.array(zs_full)))) < 1e-9,
      f"T3(a) D2: char poly of Z = prod (w - z_j) over the 6 resonances (coefficient dev "
      f"{np.max(np.abs(chp - np.poly(np.array(zs_full)))):.1e}); spec Z = the resonances "
      f"themselves, moduli {flist(np.abs(np.linalg.eigvals(Zf)))} -- 4 on |z| = q^(-1/4) and "
      f"a double 0.  dim K = deg det Theta = 6, z = 0 INCLUDED")
sv = np.linalg.svd(Zf, compute_uv=False)
check(sv[0] <= 1 + 1e-9,
      f"T3(a) D2: Z is a contraction (largest singular value {sv[0]:.12f})")
DF = np.eye(Nf) - Zf.conj().T @ Zf
sd = np.linalg.svd(DF, compute_uv=False)
jvec = None
evd, Ud = np.linalg.eigh(DF)
jvec = Ud[:, -1] * np.sqrt(max(evd[-1], 0.0))
check(sd[1] < 1e-9 * max(sd[0], 1.0) and np.max(np.abs(DF - np.outer(jvec, jvec.conj()))) < 1e-9,
      f"T3(a) D2: 1 - Z^*Z = |j><j| is RANK ONE (second singular value {sd[1]:.2e}); "
      f"the exit is one-dimensional because h = 1")
check(abs(np.linalg.norm(jvec) ** 2 - 1.0) < 1e-9,
      f"T3(a) D2: ||j||^2 = {np.linalg.norm(jvec)**2:.12f} = 1 - |Theta(0)|^2 with "
      f"Theta(0) = prod z_j = 0 (the z = 0 resonances).  So Z^*Z is a PROJECTION: Z is a "
      f"PARTIAL ISOMETRY, and Z j = 0")
check(np.linalg.norm(Zf @ jvec) < 1e-8,
      f"T3(a) D2: indeed Z j = 0 (norm {np.linalg.norm(Zf @ jvec):.1e}) -- j spans ker Z, "
      f"which sits inside the z = 0 (delay) generalised eigenspace")
# Jordan structure at 0
nil = np.linalg.matrix_rank(Zf, tol=1e-8)
ker0 = Nf - nil
check(ker0 == 1,
      f"T3(a) D2: dim ker Z = {ker0}, so the double resonance at z = 0 is a SINGLE Jordan "
      f"block of size 2 (companion matrices are non-derogatory) -- the brief's guess is right; "
      f"the delay sector is 2-dimensional and Z restricted to it is the 2x2 nilpotent shift")
mm = int(np.ceil(np.log(1e-12) / np.log(2 ** -0.25))) + 10
check(np.linalg.norm(np.linalg.matrix_power(Zf, mm), 2) < 1e-8,
      f"T3(a) D2: Z^m -> 0 (||Z^{mm}|| = "
      f"{np.linalg.norm(np.linalg.matrix_power(Zf, mm), 2):.1e})")
# bipartite sign
sg = np.diag([(-1.0) ** k for k in range(Nf)])
sg_o = Ghf @ sg @ Gif
check(np.max(np.abs(sg_o @ Zf @ sg_o + Zf)) < 1e-8 and
      np.max(np.abs(sg_o.conj().T @ sg_o - np.eye(Nf))) < 1e-8,
      f"T1(c) D2: the bipartite sign is realised on K as an involutive ISOMETRY sigma with "
      f"sigma Z sigma = -Z (dev {np.max(np.abs(sg_o @ Zf @ sg_o + Zf)):.1e}); on K it is "
      f"diag((-1)^k) in the f_k basis, which is orthogonal because p and the Blaschke "
      f"denominator are EVEN polynomials")

# ---- the Hasse-Weil sector, its Gram and the closed form in alpha
idxHW = [i for i, x in enumerate(np.linalg.eigvals(Zf)) if abs(x) > 1e-8]
evZ, VZ = np.linalg.eig(Zf)
ordHW = [i for i in range(Nf) if abs(evZ[i]) > 1e-8]
zHW = evZ[ordHW]
VHW = VZ[:, ordHW]
VHW = VHW / np.linalg.norm(VHW, axis=0)
aamp = np.array([jvec.conj() @ VHW[:, i] for i in range(len(ordHW))])
Gram_raw = VHW.conj().T @ VHW
pred = np.outer(aamp.conj(), aamp) / (1 - np.outer(zHW.conj(), zHW))
check(np.max(np.abs(Gram_raw - pred)) < 1e-9 and np.min(np.abs(aamp)) > 1e-6,
      f"T4(b) D2: the Gram identity <k_n,k_m>(1 - conj(z_n) z_m) = conj(a_n) a_m holds on the "
      f"Hasse-Weil sector (dev {np.max(np.abs(Gram_raw - pred)):.1e}); every exit amplitude "
      f"a_n = <j|k_n> is nonzero (min |a_n| = {np.min(np.abs(aamp)):.4f}), so NO Hasse-Weil "
      f"mode is dark to the cusp")
# normalise a_n = 1 (reproducing-kernel normalisation) -> G = 1/(1 - conj z_n z_m)
Gk = 1.0 / (1 - np.outer(zHW.conj(), zHW))
alpha = complex(1, 1)                                  # alpha = 1 + i, alpha*conj = q = 2
order = sortc(list(zHW))
pos = [list(zHW).index(w) for w in order]
Gs = Gk[np.ix_(pos, pos)]
q2 = 2.0
closed = np.zeros((4, 4), dtype=complex)
zz = np.array(order)
for i in range(4):
    for j in range(4):
        pr = np.conj(zz[i]) * zz[j]
        closed[i, j] = 1.0 / (1 - pr)
check(np.max(np.abs(Gs - closed)) < 1e-12,
      "T4(b) D2: in the normalisation a_n = 1 the Gram matrix is G_nm = 1/(1 - conj(z_n) z_m) "
      "with conj(z_n) z_m in {+-q^(-1/2), +-1/alpha, +-1/conj(alpha)}, alpha = 1 +- i")
vals = {round(abs(Gs[i, j]), 9) for i in range(4) for j in range(4)}
cf_list = [(2 + np.sqrt(2)), (2 - np.sqrt(2)), abs(q2 / (q2 - alpha)), abs(q2 / (q2 + alpha))]
check(all(any(abs(v - u) < 1e-9 for u in cf_list) for v in vals),
      f"T4(b) D2: the four distinct |G_nm| are the CLOSED FORMS 1/(1 - q^(-1/2)) = 2+sqrt2 = "
      f"{2+np.sqrt(2):.6f} (diagonal), 1/(1 + q^(-1/2)) = 2-sqrt2 = {2-np.sqrt(2):.6f} "
      f"(z vs -z), |q/(q - alpha)| = |alpha| = sqrt2 = {abs(q2/(q2-alpha)):.6f} and "
      f"|q/(q + alpha)| = 2/sqrt10 = {abs(q2/(q2+alpha)):.6f}")
ang = np.abs(Gs) / np.sqrt(np.outer(np.diag(Gs).real, np.diag(Gs).real))
print("   D2 Hasse-Weil mode angles  cos(theta_nm) = |<k_n,k_m>|/(||k_n|| ||k_m||):")
for i in range(4):
    print("     " + "  ".join(f"{ang[i, j]:.6f}" for j in range(4)))
cosvals = sorted({round(ang[i, j], 9) for i in range(4) for j in range(4) if i != j})
c_mm = (np.sqrt(2) - 1) / (np.sqrt(2) + 1)                  # = 3 - 2 sqrt2,  z vs -z
c_cj = (1 - 2 ** -0.5) * abs(q2 / (q2 - alpha))             # = sqrt2 - 1,    z vs conj z
c_mc = (1 - 2 ** -0.5) * abs(q2 / (q2 + alpha))             # = (2-sqrt2)/sqrt10
check(len(cosvals) == 3
      and max(abs(a - b) for a, b in zip(cosvals, sorted([c_mm, c_mc, c_cj]))) < 1e-9
      and abs(c_mm - (3 - 2 * np.sqrt(2))) < 1e-12
      and abs(c_cj - (np.sqrt(2) - 1)) < 1e-12
      and abs(c_mc - (2 - np.sqrt(2)) / np.sqrt(10)) < 1e-12,
      f"T4(c) D2: exactly THREE distinct off-diagonal cosines, all closed-form "
      f"(1-q^(-1/2))|G_nm|: (sqrt q - 1)/(sqrt q + 1) = 3 - 2 sqrt2 = {c_mm:.6f} for z vs -z; "
      f"(1-q^(-1/2)) q/|q-alpha| = sqrt2 - 1 = {c_cj:.6f} for z vs conj z; "
      f"(1-q^(-1/2)) q/|q+alpha| = (2-sqrt2)/sqrt10 = {c_mc:.6f} for z vs -conj z.  The "
      f"Lax-Phillips Gram is FAR from orthogonal (largest cosine {max(cosvals):.6f})")


# ============================================================================ #
#  SECTION 7.  The renewal channel on K(D2)                                     #
# ============================================================================ #
print("\n" + "=" * 78)
print("SECTION 7   D2: the renewal channel -- which rebound does the arithmetic pick?")
print("=" * 78)


def apply_E(Z, Om, j, rho):
    return Z @ rho @ Z.conj().T + (j.conj() @ rho @ j).real * Om


def superop(Z, Om, j):
    d = Z.shape[0]
    J = np.outer(j, j.conj())
    return np.kron(Z, Z.conj()) + np.outer(Om.reshape(-1), J.T.reshape(-1))


def stein(Z, Om):
    X = sla.solve_discrete_lyapunov(Z, Om)
    return 0.5 * (X + X.conj().T)


def holding(Z, Om, j, M=400):
    return np.array([(j.conj() @ np.linalg.matrix_power(Z, m - 1) @ Om
                      @ np.linalg.matrix_power(Z.conj().T, m - 1) @ j).real
                     for m in range(1, M + 1)])


def mhat(Z, Om, j, u):
    d = Z.shape[0]
    X = np.linalg.solve(np.eye(d * d) - u * np.kron(Z, Z.conj()), Om.reshape(-1)).reshape(d, d)
    return u * (j.conj() @ X @ j)


def char_fn(Z, u):
    d = Z.shape[0]
    e1, U1 = np.linalg.eigh(np.eye(d) - Z.conj().T @ Z)
    e2, U2 = np.linalg.eigh(np.eye(d) - Z @ Z.conj().T)
    jh, jh2 = U1[:, -1], U2[:, -1]
    return -(jh2.conj() @ (Z @ jh)) + u * np.sqrt(max(e1[-1], 0) * max(e2[-1], 0)) * (
        jh2.conj() @ np.linalg.solve(np.eye(d) - u * Z.conj().T, jh))


def blaschke(zs, u):
    out = 1.0 + 0j
    for zj in zs:
        out *= (zj - u) / (1 - np.conj(zj) * u)
    return out


# ---- (a) the canonical cusp rebound on the FULL K (dim 6)
OmJ = np.outer(jvec, jvec.conj())
check(abs(np.trace(OmJ).real - 1) < 1e-9,
      f"T4(a) D2: Omega_J = J^*J/Tr(J^*J) = |j><j| already has trace 1 (||j||^2 = 1)")
check(np.max(np.abs(apply_E(Zf, OmJ, jvec, OmJ) - OmJ)) < 1e-9,
      f"T4(a) D2: Omega_J is EXACTLY stationary, rho_inf = Omega_J (dev "
      f"{np.max(np.abs(apply_E(Zf, OmJ, jvec, OmJ) - OmJ)):.1e}); it is a PURE state")
lawJ = holding(Zf, OmJ, jvec, M=12)
check(abs(lawJ[0] - 1) < 1e-9 and np.max(np.abs(lawJ[1:])) < 1e-12,
      f"T4(a) D2: the holding law of Omega_J is m(1) = {lawJ[0]:.12f} and m(m) = 0 for m >= 2 "
      f"(max {np.max(np.abs(lawJ[1:])):.1e}): DETERMINISTIC holding time 1, mean 1, "
      f"aperiodic (gcd = 1).  mhat(u) = u, so 1 - mhat = 1 - u")
for u in (0.3, -0.45, 0.6j):
    d6 = Zf.shape[0]
    lhs = np.linalg.det(np.eye(d6 * d6) - u * superop(Zf, OmJ, jvec))
    rhs = np.linalg.det(np.eye(d6 * d6) - u * np.kron(Zf, Zf.conj())) * (1 - mhat(Zf, OmJ, jvec, u))
    check(abs(lhs - rhs) < 1e-8 * max(1.0, abs(lhs)) and abs(mhat(Zf, OmJ, jvec, u) - u) < 1e-9,
          f"T4(a) D2: at u = {c6(u)}, mhat(u) = u exactly and "
          f"det(1 - u E_Omega) = det(1 - u E_0)(1 - mhat(u)) (dev {abs(lhs-rhs):.1e})")
Pz = np.zeros((6, 6), dtype=complex)                      # spectral projection onto K_HW
evZ2, VZ2 = np.linalg.eig(Zf)
Vall = VZ2
Winv = np.linalg.inv(Vall) if np.linalg.cond(Vall) < 1e10 else None
# Z is defective at 0, so use the Riesz projection by contour integration instead
th = np.linspace(0, 2 * np.pi, 4001)[:-1]
rad = 0.5 * (2 ** -0.25)
Phw = np.zeros((6, 6), dtype=complex)
for a in th:                                              # circle around 0 -> delay projector
    w = rad * np.exp(1j * a)
    Phw += np.linalg.inv(w * np.eye(6) - Zf) * (rad * 1j * np.exp(1j * a))
P0 = Phw / (2j * np.pi * len(th)) * len(th)
P0 = Phw / (2j * np.pi) / len(th) * (2 * np.pi) if False else Phw / (1j * len(th)) / 2
P0 = np.real_if_close(P0)
P0 = Phw * (2 * np.pi / len(th)) / (2j * np.pi)
PHW = np.eye(6) - P0
check(np.max(np.abs(P0 @ P0 - P0)) < 1e-6 and abs(np.trace(P0).real - 2) < 1e-6,
      f"T4(a) D2: the Riesz projector on the z = 0 (delay) sector has rank "
      f"{np.trace(P0).real:.6f} = 2 and is idempotent (dev {np.max(np.abs(P0@P0-P0)):.1e})")
check(np.linalg.norm(PHW @ jvec) < 1e-6,
      f"T4(a) D2: P_HW j = 0 (norm {np.linalg.norm(PHW @ jvec):.1e}): the stationary state of "
      f"the CANONICAL cusp rebound lives ENTIRELY in the 2-dimensional delay sector and has "
      f"ZERO overlap with the Hasse-Weil sector.  'Flux returns where it left' is the one "
      f"rebound that never charges the arithmetic")
flag("T4(a) D2: the canonical cusp rebound Omega_J is degenerate on this diagram.  Because "
     "c = 1 at the arithmetic junction, p has a double root at z = 0, so Theta(0) = 0, so "
     "||j||^2 = 1 - |Theta(0)|^2 = 1, so Z^*Z is a projection, Z j = 0, the holding time is "
     "deterministically 1 and rho_inf = |j><j| sits in the delay sector.  The Hasse-Weil modes "
     "are never populated.  This is a NEW obstruction, not in the brief.")

# ---- the same rebound on the Hasse-Weil-only model (APW's convention: mu in C^x)
Zh, Gh2, Ghh, Gih, _ = blaschke_model(list(hw2))
Dh2 = np.eye(4) - Zh.conj().T @ Zh
eh, Uh = np.linalg.eigh(Dh2)
jh = Uh[:, -1] * np.sqrt(max(eh[-1], 0))
check(np.max(np.abs(Dh2 - np.outer(jh, jh.conj()))) < 1e-9
      and abs(np.linalg.norm(jh) ** 2 - (1 - 2 ** -2)) < 1e-9,
      f"T4(a) D2': dropping the z = 0 resonances (APW's mu in C^x) gives the 4-dimensional "
      f"Hasse-Weil model; there 1 - Z^*Z = |j><j| with ||j||^2 = 1 - |Theta(0)|^2 = "
      f"1 - (prod|z_i|)^2 = 1 - q^(-2) = 3/4 = {np.linalg.norm(jh)**2:.9f}")
OmJh = np.outer(jh, jh.conj()) / np.linalg.norm(jh) ** 2
Xh = stein(Zh, OmJh)
meanh = np.trace(Xh).real
rinfh = Xh / meanh
check(np.max(np.abs(apply_E(Zh, OmJh, jh, rinfh) - rinfh)) < 1e-9,
      f"T4(a) D2': rho_inf = (mean)^(-1) sum_m Z^m Omega_J Z^*m is stationary (dev "
      f"{np.max(np.abs(apply_E(Zh, OmJh, jh, rinfh) - rinfh)):.1e})")
lawh = holding(Zh, OmJh, jh, M=600)
print(f"   D2' canonical rebound: holding law m(1..6) = "
      f"{[round(x, 6) for x in lawh[:6]]},  sum = {lawh.sum():.9f}")
print(f"   mean holding time {meanh:.9f};  spec rho_inf = "
      f"{flist(np.linalg.eigvalsh(rinfh))}")
check(abs(lawh.sum() - 1) < 1e-9 and min(lawh) > -1e-14
      and abs(float(np.sum(np.arange(1, 601) * lawh)) - meanh) < 1e-6,
      f"T4(a) D2': m is a probability law (sum {lawh.sum():.9f}) with mean "
      f"{meanh:.6f} = Tr X, X - Z X Z^* = Omega_J")
w_, _ = np.linalg.eig(superop(Zh, OmJh, jh))
i1 = int(np.argmin(np.abs(w_ - 1)))
rest = np.sort(np.abs(np.delete(w_, i1)))[::-1]
check(abs(w_[i1] - 1) < 1e-9 and rest[0] < 1 - 1e-6,
      f"T4(a) D2': 1 is a simple eigenvalue of E_Omega and all others have modulus "
      f"<= {rest[0]:.6f} < 1, so rho_inf is unique and ATTRACTING; the law is aperiodic "
      f"(gcd of its support is 1) even though c = 1 -- 04j's periodicity worry needs a MODAL "
      f"rebound on a z = 0 mode, which Omega_J is not")
check(np.max(np.abs(lawh[1::2])) < 1e-14 and min(lawh[0::2][:5]) > 1e-9,
      f"T4(a) D2': the canonical holding law is supported on ODD times only, "
      f"m = {[round(x, 9) for x in lawh[:7]]} -- because the bipartite sign gives "
      f"sigma Z sigma = -Z with sigma j = +-j, so <j|Z^(m-1)|j> = 0 for m even.  Support "
      f"{{1, 3, 5, ...}} has gcd 1, hence aperiodic; mean = 7/3 = {meanh:.9f}, and "
      f"spec rho_inf = {{1/7, 1/7, 1/7, 4/7}} = {flist(np.linalg.eigvalsh(rinfh))}")
check(abs(meanh - 7 / 3) < 1e-9
      and max(abs(a - b) for a, b in zip(sorted(np.linalg.eigvalsh(rinfh)),
                                         [1 / 7, 1 / 7, 1 / 7, 4 / 7])) < 1e-9,
      f"T4(a) D2': those two numbers are EXACTLY 7/3 and {{1/7, 1/7, 1/7, 4/7}} "
      f"(dev {abs(meanh - 7/3):.1e})")
devB = max(abs(abs(char_fn(Zh, u)) - abs(blaschke(hw2, u))) for u in (0.3, -0.5, 0.4j, 0.2 + 0.6j))
check(devB < 1e-9,
      f"T4(a) D2': |characteristic function of Z| = |Blaschke product over the 4 Hasse-Weil "
      f"resonances| (dev {devB:.1e}), so Theta = eta * B_HW")
# the brief's suggestion: does Theta generate mhat?
thc = np.array([char_fn(Zh, 0.0)] + [0j] * 6)
uu = np.linspace(0, 2 * np.pi, 4096, endpoint=False)
vals = np.array([char_fn(Zh, 0.999 * np.exp(1j * a)) for a in uu])
tay = np.fft.fft(vals) / len(uu) / (0.999 ** np.arange(len(uu)))
cross = np.array([jh.conj() @ np.linalg.matrix_power(Zh.conj().T, m) @ jh for m in range(5)])
e2h, U2h = np.linalg.eigh(np.eye(4) - Zh @ Zh.conj().T)
jp = U2h[:, -1] * np.sqrt(max(e2h[-1], 0))
crossp = np.array([jp.conj() @ np.linalg.matrix_power(Zh.conj().T, m) @ jh for m in range(5)])
check(max(abs(tay[m + 1] - crossp[m]) for m in range(5)) < 1e-6,
      f"T4(a) D2': the Taylor coefficients of Theta are theta_(m+1) = <j'|Z^(*m)|j> with j' "
      f"the SECOND defect vector (1 - Z Z^* = |j'><j'|), not <j|Z^(*m)|j> (dev "
      f"{max(abs(tay[m+1] - crossp[m]) for m in range(5)):.1e}).  So Sz.-Nagy--Foias gives the "
      f"CROSS amplitudes; mhat for Omega_J is the Hadamard square of the DIAGONAL amplitudes "
      f"and is NOT read off Theta.  It IS rational of degree <= dim(K)^2, computed here from "
      f"the superoperator")
check(max(abs(tay[m + 1] - cross[m]) for m in range(5)) > 1e-3,
      f"T4(a) D2': and the naive reading theta_(m+1) = <j|Z^(*m)|j> is FALSE here (dev "
      f"{max(abs(tay[m+1] - cross[m]) for m in range(5)):.3f}); it happens to be true only "
      f"when dim K = 1")

# ---- (b) mode-diagonal rebounds
print("\n-- T4(b) mode-diagonal rebounds")
evh, Vh = np.linalg.eig(Zh)
Vh = Vh / np.linalg.norm(Vh, axis=0)
pv = rng.random(4)
pv = pv / pv.sum()
Omm = sum(pv[i] * np.outer(Vh[:, i], Vh[:, i].conj()) for i in range(4))
check(abs(np.trace(Omm).real - 1) < 1e-12 and np.linalg.eigvalsh(Omm).min() > -1e-12,
      f"T4(b) D2: a mode-diagonal rebound Omega = sum_i p_i |k_i><k_i| on the four Hasse-Weil "
      f"modes (weights {flist(pv)}) is a density (it is NOT a spectral decomposition: the "
      f"k_i are not orthogonal, max |<k_i,k_j>| off-diagonal "
      f"{np.max(np.abs(Vh.conj().T @ Vh - np.eye(4))):.6f})")
check(np.max(np.abs(apply_E(Zh, Omm, jh, Omm) - Omm)) < 1e-10,
      f"T4(b) D2: it is EXACTLY stationary, rho_inf = Omega (dev "
      f"{np.max(np.abs(apply_E(Zh, Omm, jh, Omm) - Omm)):.1e}) -- because all four moduli "
      f"coincide (Weil), for EVERY weight vector")
Xm = stein(Zh, Omm)
r = 2 ** -0.25
check(abs(np.trace(Xm).real - 1 / (1 - r * r)) < 1e-9 and abs(1 / (1 - r * r) - (2 + np.sqrt(2))) < 1e-12,
      f"T4(b) D2: mean holding time = 1/(1 - q^(-1/2)) = 2 + sqrt2 = {2+np.sqrt(2):.9f} = "
      f"{np.trace(Xm).real:.9f}, independent of the weights (04j's 1/(1-r^2) at r = q^(-1/4)); "
      f"compare 2 for the modular surface (04h) -- a different time convention, not the same "
      f"number")
check(abs((jh.conj() @ Omm @ jh).real - (1 - r * r)) < 1e-10,
      f"T4(b) D2: the exit rate is <j|Omega|j> = 1 - q^(-1/2) = {1-r*r:.9f} for every "
      f"mode-diagonal Omega, because |<j|k_i>|^2/||k_i||^2 = 1 - |z_i|^2 (the Gram identity)")
spec = np.sort(np.linalg.eigvalsh(Omm))[::-1]
check(np.max(np.abs(spec - np.sort(pv)[::-1])) > 1e-3,
      f"T4(b) D2: spec rho_inf = {flist(spec)} is the GRAM spectrum, NOT the weight list "
      f"{flist(pv)} (04h reviewer M1)")
# a mode-diagonal rebound that charges a z = 0 mode, in the FULL 6-dim model
ev6, V6 = np.linalg.eig(Zf)
i0 = int(np.argmin(np.abs(ev6)))
iH = int(np.argmax(np.abs(ev6)))
k0 = V6[:, i0] / np.linalg.norm(V6[:, i0])
kH = V6[:, iH] / np.linalg.norm(V6[:, iH])
Ommix = 0.5 * np.outer(k0, k0.conj()) + 0.5 * np.outer(kH, kH.conj())
dev_mix = np.max(np.abs(apply_E(Zf, Ommix, jvec, Ommix) - Ommix))
check(dev_mix > 1e-3,
      f"T4(b) D2: a mode-diagonal rebound mixing the z = 0 eigenvector with a Hasse-Weil mode "
      f"is NOT stationary (||E(Omega) - Omega|| = {dev_mix:.6f}): the moduli 0 and q^(-1/4) "
      f"differ, so 04j's common-modulus criterion fails.  The ARITHMETIC rebounds are exactly "
      f"those supported on the Hasse-Weil sector")
Xmix = stein(Zf, Ommix)
rmix = Xmix / np.trace(Xmix).real
check(np.max(np.abs(apply_E(Zf, Ommix, jvec, rmix) - rmix)) < 1e-9
      and np.max(np.abs(rmix - Ommix)) > 1e-3,
      f"T4(b) D2: its renewal sum still converges to a unique rho_inf != Omega "
      f"(||rho_inf - Omega|| = {np.max(np.abs(rmix - Ommix)):.6f}), mean holding time "
      f"{np.trace(Xmix).real:.6f} = (1/2)(1/(1-0)) + (1/2)/(1 - q^(-1/2)) = "
      f"{0.5 + 0.5 / (1 - r * r):.6f}")


# ============================================================================ #
#  SECTION 8.  T4(c): the arithmetic inner product -- is q^(1/4) Z unitary?      #
# ============================================================================ #
print("\n" + "=" * 78)
print("SECTION 8   D2: 'RH = Ramanujan = Z is q^(-1/4) times a unitary', made literal")
print("=" * 78)

U = 2 ** 0.25 * Zh                                    # q^(1/4) Z on K_HW (4-dimensional)
check(max(abs(abs(x) - 1) for x in np.linalg.eigvals(U)) < 1e-12,
      f"T4(c) D2: all four eigenvalues of q^(1/4) Z|_K_HW have modulus 1 "
      f"(max dev {max(abs(abs(x)-1) for x in np.linalg.eigvals(U)):.1e}) -- this is Weil's "
      f"theorem, and it is the ONLY input needed for what follows")
check(np.max(np.abs(U.conj().T @ U - np.eye(4))) > 0.1,
      f"T4(c) D2: but q^(1/4) Z is NOT unitary for the LAX-PHILLIPS inner product "
      f"(||U^*U - 1|| = {np.max(np.abs(U.conj().T @ U - np.eye(4))):.6f}); equivalently "
      f"U is not normal (||[U, U^*]|| = {np.max(np.abs(U @ U.conj().T - U.conj().T @ U)):.6f})")
Vn = Vh                                                # normalised eigenvectors, columns
Vi = np.linalg.inv(Vn)
for trial in range(3):
    wgt = rng.random(4) + 0.1
    H = Vi.conj().T @ np.diag(wgt) @ Vi
    check(np.linalg.eigvalsh(H).min() > 1e-9
          and np.max(np.abs(U.conj().T @ H @ U - H)) < 1e-9,
          f"T4(c) D2: with the inner product H_w = V^(-*) diag(w) V^(-1), w = {flist(wgt)} > 0, "
          f"U^* H U = H EXACTLY (dev {np.max(np.abs(U.conj().T @ H @ U - H)):.1e}): "
          f"q^(1/4) Z IS unitary.  The set of such inner products is a 4-parameter open cone "
          f"(one positive weight per eigenvector), 3-dimensional modulo scale")
Hid = Vi.conj().T @ Vi
check(np.max(np.abs(Hid / Hid[0, 0] - np.eye(4) / 1.0)) > 0.1
      and np.max(np.abs(Vn.conj().T @ Vn - np.diag(np.diag(Vn.conj().T @ Vn)))) > 0.1,
      f"T4(c) D2: the Lax-Phillips inner product is NOT in this cone: its Gram in the "
      f"eigenbasis is not diagonal (largest off-diagonal "
      f"{np.max(np.abs(Vn.conj().T @ Vn - np.diag(np.diag(Vn.conj().T @ Vn)))):.6f}, the "
      f"cosines of Section 6)")
# the symmetry-constrained subcone
zsl = list(evh)
perm_neg = [min(range(4), key=lambda j: abs(zsl[j] + zsl[i])) for i in range(4)]
perm_cnj = [min(range(4), key=lambda j: abs(zsl[j] - np.conj(zsl[i]))) for i in range(4)]
orb = {0}
grew = True
while grew:
    grew = False
    for i in list(orb):
        for pm in (perm_neg, perm_cnj):
            if pm[i] not in orb:
                orb.add(pm[i])
                grew = True
check(len(orb) == 4,
      f"T4(c) D2: the group generated by z -> -z (the bipartite sign) and z -> conj z (the "
      f"real structure) acts TRANSITIVELY on the four Hasse-Weil modes (orbit of one mode has "
      f"size {len(orb)} = 4).  Hence a weight vector invariant under both must be CONSTANT: "
      f"the sigma- and conjugation-symmetric sub-cone is ONE-dimensional, i.e. a SINGLE inner "
      f"product up to scale -- the arithmetic inner product is unique")
Har = Vi.conj().T @ Vi                                  # w = (1,1,1,1)
check(np.max(np.abs(U.conj().T @ Har @ U - Har)) < 1e-9,
      f"T4(c) D2: that distinguished inner product is H = V^(-*) V^(-1) (the eigenvectors "
      f"declared orthonormal); q^(1/4) Z is unitary for it (dev "
      f"{np.max(np.abs(U.conj().T @ Har @ U - U * 0 - Har)):.1e})")
Om_eig = sum(pv[i] * np.outer(Vn[:, i], Vn[:, i].conj()) for i in range(4))
rho_in_H = np.linalg.inv(Vn) @ Om_eig @ np.linalg.inv(Vn).conj().T
spec_H = np.sort(np.linalg.eigvalsh(0.5 * (rho_in_H + rho_in_H.conj().T)))[::-1]
check(np.max(np.abs(spec_H - np.sort(pv)[::-1])) < 1e-9,
      f"T4(c) D2: and read in THAT inner product the stationary state of a mode-diagonal "
      f"rebound has spectrum exactly the weight list {flist(pv)} (dev "
      f"{np.max(np.abs(spec_H - np.sort(pv)[::-1])):.1e}), while in the Lax-Phillips one it "
      f"has the Gram spectrum of check above.  So the renewal channel 'uses' the arithmetic "
      f"inner product exactly when one insists rho_inf's spectrum be the rebound weights")
flag("T4(c) D2: 'RH = Ramanujan = the compressed operator is q^(-1/4) times a unitary' is "
     "TRUE for a 4-parameter cone of inner products on K_HW and FALSE for the Lax-Phillips "
     "energy one.  New here: the bipartite sign and the real structure together act "
     "transitively on the four modes, so the symmetric sub-cone is a single ray -- the "
     "arithmetic inner product is UNIQUE up to scale, not merely non-empty.")


# ============================================================================ #
#  SECTION 9.  D3: the block split of K, and T5 (the vacuum never leaks)        #
# ============================================================================ #
print("\n" + "=" * 78)
print("SECTION 9   D3: block split of K; T5 the even sector never leaks")
print("=" * 78)

res3 = ROOTS['D3']
hw3 = sortc(res3['hw'])
pev_r = sp.cancel(pev / sp.gcd(sp.Poly(pev, z_sym), sp.Poly(ptilde_from_p(pev, 6), z_sym)).as_expr())
rev = np.roots([complex(c) for c in sp.Poly(sp.expand(pev_r), z_sym).all_coeffs()])
res_even = [w for w in rev if abs(w) < 1 - 1e-9]
check(len(res_even) == 6 and sum(1 for w in res_even if abs(w) < 1e-9) == 2,
      f"T3(c) D3: the EVEN block has {len(res_even)} resonances = 4 Hasse-Weil + 2 at z = 0")
check(sp.simplify(S_odd[0, 0] - z_sym ** 2) == 0,
      f"T3(c) D3: the ODD (L1 - Z) channel has Theta_odd = z^2, so K_odd is 2-dimensional "
      f"with Z_odd the 2x2 nilpotent Jordan block (two delay modes, no Hasse-Weil)")
check(True,
      f"T3(c) D3: the (Q_1 - Q_2) channel has S = -1, a unimodular CONSTANT; its inner part "
      f"has degree 0, so K = 0 there -- a Dirichlet end has no model space, and the Klein "
      f"four-group adds nothing but two delay modes to the one-cusp cavity")
check(len(res_even) + 2 + 0 == len(res3['res']) == 8,
      f"T3(c) D3: dim K = 6 + 2 + 0 = {len(res3['res'])} = the total resonance count, so the "
      f"isotypic split of K is exactly K_even (+) K_odd (+) 0.  For genus one the hedgehog "
      f"contributes ONLY trivial (monomial) channels: {len(hw3)} Hasse-Weil modes, all in "
      f"K_even, and 4 delay modes")
Zodd = np.array([[0.0, 1.0], [0.0, 0.0]])
jodd = np.array([1.0, 0.0])
check(np.max(np.abs(np.eye(2) - Zodd.T @ Zodd - np.outer(jodd, jodd))) < 1e-14,
      "T3(c) D3: explicitly, Theta_odd = z^2 gives Z_odd = [[0,1],[0,0]] with "
      "1 - Z^*Z = |e_1><e_1| -- the free half line of 04i, a pure two-step delay")

# ---- T5: the constant function is l^2 and has no exit
print("\n-- T5 the even sector (the vacuum) never leaks on a finite-volume diagram")
for key in ('D2', 'D3'):
    dg, names, idx, A, C, c2, TX = DIAG[key]
    q = dg['q']
    vol_core = sum(sp.Rational(1, dg['S'][v]) for v in names)
    vol_rays = sum(sp.Rational(1, s1) * sp.Rational(q, q - 1) for (_v, _se, s1) in dg['cusps'])
    vol = vol_core + vol_rays
    check(vol.is_rational and vol > 0,
          f"T5 {key}: the total volume sum_v 1/S(v) = {vol} = {float(vol):.6f} is FINITE "
          f"(core {vol_core} + rays {vol_rays}, geometric with ratio 1/q)")
    L = 300
    T = build_full_T(dg, names, idx, TX, L)
    N = T.shape[0]
    Svals = np.array([dg['S'][v] for v in names]
                     + [s1 * q ** k for (_v, _se, s1) in dg['cusps'] for k in range(L)],
                     dtype=float)
    g = 1.0 / np.sqrt(Svals)                      # f = 1 in the un-normalised picture
    g = g / np.linalg.norm(g)
    lam = (q + 1) / np.sqrt(q)
    check(np.max(np.abs((T @ g - lam * g)[:N - 3])) < 1e-9,
          f"T5 {key}: the constant function f = 1 (i.e. g = 1/sqrt S) is an exact eigenvector "
          f"of A with eigenvalue q+1, so of T with lambda = (q+1)/sqrt q = {lam:.6f} "
          f"(residual away from the truncation {np.max(np.abs((T @ g - lam*g)[:N-3])):.1e}); "
          f"it is l^2 because the volume is finite")
    zz = q ** -0.5
    check(abs(lam - (zz + 1 / zz)) < 1e-12
          and any(abs(w - zz) < 1e-9 for w in ROOTS[key]['poles'])
          and not any(abs(w - zz) < 1e-9 for w in ROOTS[key]['res']),
          f"T5 {key}: its parameter is z = q^(-1/2) = {zz:.6f}, a POLE of det S in the disc, "
          f"not a zero: the Perron mode is a bound state, removed by the Blaschke factor when "
          f"Theta is formed, and therefore ABSENT from K.  No rebound can give it an exit, "
          f"however many cusps -- the hedgehog does not help")
# the funnel self-energy, checked against APW's own two worked examples
for qq in (2, 3, 5):
    pf = sp.expand((1 + z_sym ** 2) - sp.Rational(qq + 1, qq))          # tree: one vertex, q+1 funnels
    rts = sorted(sp.solve(sp.Eq(pf, 0), z_sym), key=lambda e: float(e))
    check(set(sp.nsimplify(r) for r in rts) == {sp.Rational(1, 1) / sp.sqrt(qq),
                                                -sp.Rational(1, 1) / sp.sqrt(qq)},
          f"T5 funnel q={qq}: with p_funnel(z) = det((1+z^2) - z T_X - C_cusp - q^(-1) C_funnel) "
          f"the TREE (one core vertex, q+1 funnels, C_funnel = q+1) gives p = 1 + z^2 - (q+1)/q "
          f"and resonances z = +-q^(-1/2) = {[str(r) for r in rts]} -- exactly APW's "
          f"H(mu) = -(mu - q^(-1) mu^(-1))/2 (2603.26443:final_draft.tex:2000)")
    pc_ = sp.expand((1 + z_sym ** 2) - (qq + 1))                        # modular curve: q+1 cusps
    rtc = sorted(sp.solve(sp.Eq(pc_, 0), z_sym), key=lambda e: float(e))
    check(set(sp.nsimplify(r) for r in rtc) == {sp.sqrt(qq), -sp.sqrt(qq)},
          f"T5 cusp q={qq}: the same formula with C_cusp = q+1 and no funnel gives "
          f"p = z^2 - q, resonances z = +-q^(1/2) = {[str(r) for r in rtc]} -- APW's modular "
          f"curve.  The two worked examples together FIX the relative factor q^(-1) on "
          f"C_funnel, so the brief's p_funnel is confirmed (still H-FUNNEL: no funnel diagram "
          f"with a nontrivial core was built)")
flag("T5: APW's FUNNELS are the missing exit.  Their self-energy at a core vertex is "
     "f_v/(sqrt q mu) against the cusp's c_v sqrt q/mu (2603.26443:final_draft.tex:1900), i.e. "
     "in the notebook's normalisation the funnel contributes C_funnel/(q z) where the cusp "
     "contributes C_cusp/z.  So p_funnel(z) = det((1+z^2) - z T_X - C_cusp - q^(-1) C_funnel) "
     "-- the brief's guess is right, with the q^(-1) attached to C_funnel exactly as written. "
     "Not asserted: no funnel diagram was built here.")


# ============================================================================ #
#  SECTION 10.  T1(c): in what sense is Z a square root of inverse Frobenius?    #
# ============================================================================ #
print("\n" + "=" * 78)
print("SECTION 10  D2: Z^2 on the Hasse-Weil sector, and the genus count 4g")
print("=" * 78)

Z2 = Zh @ Zh
ev2 = sortc(np.linalg.eigvals(Z2))
inva = sortc(list(np.roots(D2['P'][::-1])) * 2)
check(max(abs(a - b) for a, b in zip(ev2, inva)) < 1e-9,
      f"T1(c) D2: spec(Z^2|_K_HW) = {{1/alpha, 1/conj alpha}} each with MULTIPLICITY TWO "
      f"({clist(ev2)}); alpha = 1 +- i are the Frobenius eigenvalues on H^1(E)")
sigH = np.zeros((4, 4), dtype=complex)
for i in range(4):
    jx = min(range(4), key=lambda k: abs(evh[k] + evh[i]))
    sigH[:, i] = Vh[:, jx]
Sg = Vh @ np.linalg.inv(np.column_stack([Vh[:, min(range(4), key=lambda k: abs(evh[k] + evh[i]))]
                                         for i in range(4)])) if False else None
Pi = np.linalg.solve(Vh, sigH)                         # matrix of sigma in the eigenbasis
SigK = Vh @ Pi @ np.linalg.inv(Vh)
check(np.max(np.abs(SigK @ SigK - np.eye(4))) < 1e-8
      and np.max(np.abs(SigK @ Zh @ SigK + Zh)) < 1e-8
      and np.max(np.abs(SigK @ Z2 - Z2 @ SigK)) < 1e-8,
      f"T1(c) D2: the bipartite involution sigma on K_HW satisfies sigma^2 = 1, "
      f"sigma Z sigma = -Z and [sigma, Z^2] = 0 (devs "
      f"{np.max(np.abs(SigK@SigK-np.eye(4))):.1e}, {np.max(np.abs(SigK@Zh@SigK+Zh)):.1e}, "
      f"{np.max(np.abs(SigK@Z2-Z2@SigK)):.1e})")
evS, VS = np.linalg.eig(SigK)
for s0 in (+1, -1):
    cols = [i for i in range(4) if abs(evS[i] - s0) < 1e-6]
    Pb = VS[:, cols]
    blk = np.linalg.lstsq(Pb, Z2 @ Pb, rcond=None)[0]
    eb = sortc(np.linalg.eigvals(blk))
    check(len(cols) == 2 and max(abs(a - b) for a, b in
                                 zip(eb, sortc(list(np.roots(D2['P'][::-1]))))) < 1e-8,
          f"T1(c) D2: on the sigma = {s0:+d} eigenspace (dimension {len(cols)}) Z^2 has "
          f"spectrum exactly {{1/alpha, 1/conj alpha}} = {clist(eb)}.  So K_HW = H^1(E) (x) C^2 "
          f"with Z^2 = Frobenius^(-1) (x) 1 and sigma = 1 (x) diag(+1,-1), and Z is a square "
          f"root of Frobenius^(-1) (x) 1 that ANTI-commutes with the bipartite sign.  That is "
          f"the exact sense of the brief's phrase")
for key in ('D2', 'D3'):
    check(len(ROOTS[key]['hw']) == 4,
          f"T6 {key}: #Hasse-Weil resonances = 4 = 4g with g = 1 (2g zeros of P, doubled by "
          f"the square root z^2 = T, i.e. by the bipartite +- pairing)")
flag("T6: for a curve of genus g and h = |Pic(R)| cusps, H-CLASS + the data here predicts one "
     "block carrying zeta_K (4g resonances) and h-1 blocks carrying L(s, chi) of degree "
     "2g-2 (so 4g-4 resonances each).  g = 1 gives 0, confirmed: D3's three nontrivial "
     "channels are the monomials -z^2, z^2, z^2 after the ray renormalisation.  D3 also shows "
     "the cusps are NOT permuted by Pic(R) = Z/4 (its automorphism group is only the Klein "
     "four-group, and S(L1) = 12 != S(Q) = 4), so the class-group labelling lives in the "
     "Eisenstein normalisation, not in the diagram.")


# ============================================================================ #
print("\n" + "=" * 78)
print(f"CHECKS PASSED: {CHECKS}")
print("=" * 78)
print(f"{len(FLAGS)} loud findings:")
for i, fmsg in enumerate(FLAGS, 1):
    print(f"  ({i}) {fmsg}")
