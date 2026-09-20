"""REFUTE review, graded toys 2026-09-20: independent lane, script 4.

prop:constant-mode-mixed-sheets and lem:funnel-first-order.
"""
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


z, a, qs, f = sp.symbols('z a q f')

# ------------------------- one-vertex regular cusp(a) + funnel(q+1-a) diagram
# core [0], cusp weight a, funnel weight b = q+1-a; p = (1+z^2) - 0 - C_c - C_f/q
p1 = sp.expand((1 + z ** 2) - a - (qs + 1 - a) / qs)
check('one-vertex: p = z^2 - (1+a(q-1))/q',
      sp.simplify(p1 - (z ** 2 - (1 + a * (qs - 1)) / qs)) == 0, str(sp.simplify(p1)))
r2 = sp.simplify((1 + a * (qs - 1)) / qs)
for qv in (2, 3, 5):
    for av in (0, sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(3, 4), 1,
               sp.Rational(3, 2), 2, qv, qv + 1):
        val = sp.nsimplify(r2.subs({qs: qv, a: av}))
        if av == 0:
            check('q=%d a=0: root^2 = 1/q (resonance at q^{-1/2})' % qv,
                  sp.simplify(val - sp.Rational(1, qv)) == 0)
        if av == qv + 1:
            check('q=%d a=q+1: root^2 = q so vartheta^2 = 1/q (bound at q^{-1/2})' % qv,
                  sp.simplify(val - qv) == 0)
        if av == 1:
            check('q=%d a=1: root^2 = 1 (threshold)' % qv, sp.simplify(val - 1) == 0)
        if 0 <= av < 1:
            check('q=%d a=%s: root inside the disc -> RESONANCE, in [1/q,1)' % (qv, av),
                  sp.Rational(1, qv) <= val < 1, str(val))
            th2 = sp.nsimplify(qv / (1 + av * (qv - 1)))
            check('q=%d a=%s: vartheta^2 = q/(1+a(q-1)) > 1 (the brief range was wrong)' % (qv, av),
                  th2 > 1, str(th2))
        if 1 < av <= qv + 1:
            th2 = sp.nsimplify(qv / (1 + av * (qv - 1)))
            check('q=%d a=%s: vartheta^2 in [1/q,1) -> visible bound state' % (qv, av),
                  sp.Rational(1, qv) <= th2 < 1, str(th2))
check('a light cusp (0<a<1) leaves the Perron-type mode outgoing at radius != q^{-1/2}',
      all(abs(float(sp.sqrt(r2.subs({qs: qv, a: sp.Rational(1, 2)}))) - qv ** -0.5) > 1e-3
          for qv in (2, 3, 5)))

# ---------------------- the constant mode on regular cusp-plus-funnel diagrams
def constant_mode_test(tag, V, S, E, cusps, funnels, qv):
    """cusps/funnels: list of (vertex, S(edge)).  Returns nothing; runs checks."""
    n = len(V)
    idx = {v: i for i, v in enumerate(V)}
    deg = {v: sp.Integer(0) for v in V}
    for (uu, vv), se in E.items():
        deg[uu] += sp.Rational(S[uu], se)
        deg[vv] += sp.Rational(S[vv], se)
    for (vv, se) in cusps + funnels:
        deg[vv] += sp.Rational(S[vv], se)
    check('%s: (q+1)-regular at every core vertex' % tag,
          all(deg[v] == qv + 1 for v in V), str(deg))
    # cusp ray: S(c1) = q S(e); funnel ray: degree condition at f1 forces S(f1) = S(e)
    for (vv, se) in cusps:
        Sc1 = qv * se
        check('%s: cusp ray c1 degree' % tag, sp.Rational(Sc1, se) + 1 == qv + 1)
    for (vv, se) in funnels:
        Sf1 = se                              # S(f1) = S(e)
        check('%s: funnel ray f1 degree (S(f1)=S(e))' % tag,
              sp.Rational(Sf1, se) + sp.Rational(Sf1, sp.Rational(Sf1, qv)) == qv + 1,
              str(sp.Rational(Sf1, se) + qv))
    Ahat = sp.zeros(n, n)
    for (uu, vv), se in E.items():
        ww = sp.sqrt(sp.Integer(S[uu]) * S[vv]) / se
        Ahat[idx[uu], idx[vv]] = ww
        Ahat[idx[vv], idx[uu]] = ww
    T = Ahat / sp.sqrt(qv)
    Cc = sp.zeros(n, n)
    Cf = sp.zeros(n, n)
    for (vv, se) in cusps:
        Cc[idx[vv], idx[vv]] += sp.Rational(S[vv], se)
    for (vv, se) in funnels:
        Cf[idx[vv], idx[vv]] += sp.Rational(S[vv], se)
    x = sp.Matrix([1 / sp.sqrt(sp.Integer(S[v])) for v in V])
    zv = 1 / sp.sqrt(qv)
    Mmix = (1 + zv ** 2) * sp.eye(n) - zv * T - zv ** 2 * Cc - Cf / qv
    res = sp.simplify(sp.expand(Mmix * x))
    check('%s: [(1+z^2) - zT - z^2 C_c - C_f/q] x = 0 at z = q^{-1/2}' % tag,
          all(sp.simplify(e) == 0 for e in res), str(res.T))
    check('%s: all entries of x nonzero' % tag, all(sp.simplify(e) != 0 for e in x))
    Mout = (1 + zv ** 2) * sp.eye(n) - zv * T - Cc - Cf / qv
    Mbd = (1 + zv ** 2) * sp.eye(n) - zv * T - zv ** 2 * Cc - zv ** 2 * Cf / qv
    outz = all(sp.simplify(e) == 0 for e in sp.simplify(Mout * x))
    bdz = all(sp.simplify(e) == 0 for e in sp.simplify(Mbd * x))
    check('%s: x null for the outgoing matrix iff C_c = 0' % tag,
          outz == (Cc == sp.zeros(n, n)), '%s %s' % (outz, Cc.diagonal()))
    check('%s: x null for the bound matrix iff C_f = 0' % tag,
          bdz == (Cf == sp.zeros(n, n)), '%s %s' % (bdz, Cf.diagonal()))
    return T, Cc, Cf


# D2 with the cusp at B replaced by a funnel (pure funnel: C_c = 0)
D2_V = ['A', 'B', 'C', 'D', 'E', 'F']
D2_S = {'A': 6, 'B': 2, 'C': 2, 'D': 1, 'E': 3, 'F': 3}
D2_E = {('A', 'B'): 2, ('B', 'C'): 2, ('C', 'D'): 1, ('D', 'E'): 1, ('D', 'F'): 1}
constant_mode_test('D2-with-funnel-at-B', D2_V, D2_S, D2_E, [], [('B', 2)], 2)
constant_mode_test('D2 (pure cusp)', D2_V, D2_S, D2_E, [('B', 2)], [], 2)
# a hand-built two-vertex 3-regular cusp(2) + funnel(2) diagram
MX_V = ['u', 'v']
MX_S = {'u': 2, 'v': 2}
MX_E = {('u', 'v'): 2}
constant_mode_test('mixed two-vertex', MX_V, MX_S, MX_E, [('u', 1)], [('v', 1)], 2)

# ------------------------------------ lem:funnel-first-order on D2
def d2_matrices():
    n = 6
    idx = {v: i for i, v in enumerate(D2_V)}
    Ahat = np.zeros((n, n))
    for (uu, vv), se in D2_E.items():
        ww = np.sqrt(D2_S[uu] * D2_S[vv]) / se
        Ahat[idx[uu], idx[vv]] = ww
        Ahat[idx[vv], idx[uu]] = ww
    T = Ahat / np.sqrt(2.0)
    C = np.zeros((n, n))
    C[idx['B'], idx['B']] = 1.0
    return T, C, idx


T2, C2, idx2 = d2_matrices()


MSYM_HOLDER = [None]


_PCACHE = {}


def pf_coeffs(fv, v):
    """p_f = p - (f/q) p^{(v)} (descending coefficients); the cofactor identity is
    verified symbolically below, and the two polynomials are computed exactly once."""
    if v not in _PCACHE:
        M = sp.Matrix(MSYM_HOLDER[0])
        p0e = sp.Poly(sp.expand(M.det()), zz)
        mi = sp.Matrix(M); mi.col_del(v); mi.row_del(v)
        pve = sp.Poly(sp.expand(mi.det()), zz)
        c0 = np.array([complex(p0e.as_expr().coeff(zz, k)) for k in range(12, -1, -1)])
        cv = np.array([complex(pve.as_expr().coeff(zz, k)) for k in range(12, -1, -1)])
        _PCACHE[v] = (c0, cv)
    c0, cv = _PCACHE[v]
    return c0 - (fv / 2.0) * cv


# exact cofactor identity p_f = p - (f/q) p^{(v)}
zz = sp.Symbol('zz')
aa_ = sp.sqrt(sp.Rational(3, 2)); bb_ = 1 / sp.sqrt(2)
Tsym = sp.zeros(6, 6)
for (i, j, val) in [(0, 1, aa_), (1, 2, bb_), (2, 3, sp.Integer(1)), (3, 4, aa_), (3, 5, aa_)]:
    Tsym[i, j] = val
    Tsym[j, i] = val
Csym = sp.diag(0, 1, 0, 0, 0, 0)
check('symbolic T_D2 matches the numeric one',
      max(abs(float(Tsym[i, j]) - T2[i, j]) for i in range(6) for j in range(6)) < 1e-12)
Msym = (1 + zz ** 2) * sp.eye(6) - zz * Tsym - Csym
MSYM_HOLDER[0] = Msym
p0 = sp.expand(Msym.det())
for v in range(6):
    minor = sp.Matrix(Msym)
    minor.col_del(v)
    minor.row_del(v)
    pv = sp.expand(minor.det())
    Mf = sp.Matrix(Msym)
    Mf[v, v] -= f / 2
    check('D2 vertex %s: p_f = p - (f/q) p^{(v)} exactly' % D2_V[v],
          sp.simplify(sp.expand(Mf.det() - (p0 - (f / 2) * pv))) == 0)

HW = np.roots([2, 0, -2, 0, 1])
derivs = {}
for v in range(6):
    dz = []
    p0c = np.array([complex(sp.Poly(p0, zz).as_expr().coeff(zz, k)) for k in range(12, -1, -1)])
    minor = sp.Matrix(Msym); minor.col_del(v); minor.row_del(v)
    pvc = np.array([complex(sp.Poly(sp.expand(minor.det()), zz).as_expr().coeff(zz, k))
                    for k in range(10, -1, -1)])
    dp0 = np.polyder(p0c)
    for zr in HW:
        d = (1.0 / 2.0) * np.polyval(pvc, zr) / np.polyval(dp0, zr)
        dz.append((np.conj(zr) * d).real / abs(zr))
    derivs[D2_V[v]] = dz
    check('D2 vertex %s: the four d|z_i|/df are identical' % D2_V[v],
          max(dz) - min(dz) < 1e-9, str(dz))
    check('D2 vertex %s: d|z_i|/df is nonzero' % D2_V[v], abs(dz[0]) > 1e-6, str(dz[0]))
ref = {'A': 0.0630672, 'B': 0.1261345, 'C': -0.0210224, 'D': -0.1681793,
       'E': -0.0630672, 'F': -0.0630672}
for v, val in ref.items():
    check('D2 vertex %s: d|z|/df = %.7f (numerics lane value)' % (v, val),
          abs(derivs[v][0] - val) < 2e-6, '%r vs %r' % (derivs[v][0], val))

# finite f: equimodularity and the orbit split
def quartet(fv, v):
    c = pf_coeffs(fv, v)
    r = np.roots(c)
    r = r[np.abs(r) > 1e-9]
    # discard the two roots nearest +-i (the cusp forms) and the exterior pair
    r = sorted(r, key=lambda x: abs(abs(x) - 2.0 ** -0.25))
    return np.array(r)


def track_quartet(v, ftarget, steps=400):
    """follow the four Hasse-Weil roots continuously from f = 0."""
    cur = list(HW)
    for k in range(1, steps + 1):
        fv = ftarget * k / steps
        r = list(np.roots(pf_coeffs(fv, v)))
        new = []
        for x in cur:
            j = min(range(len(r)), key=lambda t: abs(r[t] - x))
            new.append(r[j]); r.pop(j)
        cur = new
    return np.array(cur)


for v in range(6):
    rr = track_quartet(v, 0.2, steps=40)
    check('D2 funnel f=0.2 at %s: the tracked quartet is equimodular' % D2_V[v],
          np.max(np.abs(rr)) - np.min(np.abs(rr)) < 1e-8, '%s' % (np.abs(rr),))
    check('D2 funnel f=0.2 at %s: radius has moved off q^{-1/4}' % D2_V[v],
          abs(np.abs(rr)[0] - 2.0 ** -0.25) > 1e-4, str(np.abs(rr)[0]))
    check('D2 funnel f=0.2 at %s: quartet closed under z -> -z and z -> conj z' % D2_V[v],
          all(min(abs(-x - y) for y in rr) < 1e-7 for x in rr) and
          all(min(abs(np.conj(x) - y) for y in rr) < 1e-7 for x in rr))
radii = {D2_V[v]: round(float(np.abs(track_quartet(v, 0.2, steps=40))[0]), 6) for v in range(6)}
check('D2 funnel f=1/5: radii match the numerics lane',
      radii == {'A': 0.853128, 'B': 0.864176, 'C': 0.836761, 'D': 0.807041,
                'E': 0.827557, 'F': 0.827557}, str(radii))
rD = track_quartet(idx2['D'], 1.0, steps=600)
check('D2 funnel f=1 at D: the quartet has split into two moduli',
      len(set(np.round(np.abs(rD), 6))) == 2, str(np.abs(rD)))
check('D2 funnel f=1 at D: moduli 0.618034 and 0.707107',
      sorted(set(np.round(np.abs(rD), 6))) == [0.618034, 0.707107],
      str(sorted(set(np.round(np.abs(rD), 6)))))
check('D2 funnel f=1 at D: the split quartet is real (two size-two Klein orbits)',
      max(abs(x.imag) for x in rD) < 1e-7, str(rD))
for (v, fv, split) in [('B', 5.0, False), ('C', 5.0, False), ('E', 2.0, True), ('A', 5.0, True)]:
    rq = track_quartet(idx2[v], fv, steps=800)
    check('D2 funnel f=%g at %s: split = %s (numerics lane)' % (fv, v, split),
          (len(set(np.round(np.abs(rq), 6))) == 2) == split, str(np.abs(rq)))

# the roots of p_f stay closed under z -> -z and z -> conj z  (bipartite core!)
for v in range(6):
    for fv in (0.2, 1.0, 3.0):
        c = pf_coeffs(fv, v)
        odd = [c[k] for k in range(1, 13, 2)]
        check('D2 funnel f=%g at %s: p_f is even in z (bipartite)' % (fv, D2_V[v]),
              max(abs(x) for x in odd) < 1e-9)
        check('D2 funnel f=%g at %s: p_f has real coefficients' % (fv, D2_V[v]),
              max(abs(x.imag) for x in c) < 1e-12)

# ATTACK: "Since P_v is real and diagonal, the roots of p_f stay closed under z -> -z"
# is FALSE for a non-bipartite core.  Triangle core with one cusp:
Tt = np.array([[0.0, 1.0, 1.0], [1.0, 0.0, 1.0], [1.0, 1.0, 0.0]])
Ct = np.diag([1.0, 0.0, 0.0])
Mt = (1 + zz ** 2) * sp.eye(3) - zz * sp.Matrix(Tt.tolist()) - sp.Matrix(Ct.tolist())
Mt[1, 1] -= sp.Rational(1, 2)          # a funnel of weight f = 1 at vertex 1 (q=2)
pt = sp.Poly(sp.expand(Mt.det()), zz)
codd = [pt.as_expr().coeff(zz, k) for k in range(1, 7, 2)]
check('NON-bipartite triangle core: p_f is NOT even in z',
      any(sp.simplify(x) != 0 for x in codd), str(codd))
rt = np.roots([complex(pt.as_expr().coeff(zz, k)) for k in range(6, -1, -1)])
negclosed = True
for x in rt:
    if min(abs(-x - y) for y in rt) > 1e-6:
        negclosed = False
check('NON-bipartite triangle core: the roots are NOT closed under z -> -z', not negclosed,
      str(np.sort_complex(rt)))
# but they ARE closed under conjugation (real coefficients)
conjclosed = all(min(abs(np.conj(x) - y) for y in rt) < 1e-8 for x in rt)
check('NON-bipartite triangle core: roots still closed under conjugation', conjclosed)
# and without the funnel too: the closure under z->-z fails already for the bare core
Mt0 = (1 + zz ** 2) * sp.eye(3) - zz * sp.Matrix(Tt.tolist()) - sp.Matrix(Ct.tolist())
pt0 = sp.Poly(sp.expand(Mt0.det()), zz)
check('NON-bipartite triangle core: p_0 already not even in z',
      any(sp.simplify(pt0.as_expr().coeff(zz, k)) != 0 for k in range(1, 7, 2)))

# the Klein-orbit criterion: a 4-set closed under z->-z, z->conj z with four distinct
# non-real non-imaginary elements is a SINGLE orbit, hence equimodular; a split needs
# a real or imaginary element.
rng = np.random.default_rng(20260920)
for t in range(200):
    x = complex(rng.normal(), rng.normal())
    if abs(x.real) < 1e-3 or abs(x.imag) < 1e-3:
        continue
    orb = [x, -x, np.conj(x), -np.conj(x)]
    check('Klein orbit %d: four distinct elements' % t,
          min(abs(orb[i] - orb[j]) for i in range(4) for j in range(i + 1, 4)) > 1e-6)
    check('Klein orbit %d: automatically equimodular' % t,
          max(abs(abs(y) - abs(x)) for y in orb) < 1e-12)
    if t > 4:
        break
# size-two orbits force a real or imaginary element
for x in (0.7 + 0j, 0.7j, 0.0 + 0j):
    orb = set(np.round([x, -x, np.conj(x), -np.conj(x)], 12))
    check('orbit of %s has size <= 2 (real/imaginary/zero)' % x, len(orb) <= 2)
# a 4-set of two size-two orbits can have two moduli
check('two size-two orbits can have different moduli',
      len({round(abs(v), 9) for v in [0.618034, -0.618034, 0.707107, -0.707107]}) == 2)

# ---- the Perron pair under a funnel at B
for fv in (0.01, 0.5, 2.0, 10.0, 100.0):
    c = pf_coeffs(fv, idx2['B'])
    r = np.roots(c)
    ext = [x for x in r if abs(x) > 1 + 1e-9 and abs(x.imag) < 1e-8]
    check('D2 funnel f=%g at B: exterior real pair exists (Perron stays a bound state)' % fv,
          len(ext) == 2, str(sorted(np.abs(r))))
    th = 1.0 / max(abs(x) for x in ext)
    check('D2 funnel f=%g at B: vartheta < q^{-1/2}' % fv, th < 2.0 ** -0.5 - 1e-6, str(th))
vths = []
for fv in (0.01, 0.5, 2.0, 10.0, 100.0):
    r = np.roots(pf_coeffs(fv, idx2['B']))
    ext = [x for x in r if abs(x) > 1 + 1e-9 and abs(x.imag) < 1e-8]
    vths.append(1.0 / max(abs(x) for x in ext))
check('D2 funnel at B: vartheta decreases strictly in f',
      all(vths[i] > vths[i + 1] for i in range(len(vths) - 1)), str(vths))
check('D2 funnel at B: vartheta values match the numerics lane',
      abs(vths[0] - 0.706576) < 1e-5 and abs(vths[-1] - 0.138712) < 1e-5, str(vths))

print("\nscratch_gt_funnel: %d passed, %d failed" % (PASS[0], len(FAIL)))
