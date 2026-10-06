#!/usr/bin/env python3
"""Checks for 'The two lattice states of one curve' (notes/adelic-gkp/curve-bridge.md).

Two pictures of an ordinary elliptic curve E over F_q with Frobenius polynomial x^2 - a x + q:
 (ii) the GKP lattice state: L = Z^2, standard Omega = [[0,1],[-1,0]], integer step M with M^T Omega M = q Omega
      (lattice-tower.md); the companion convention M = [[0,-1],[q,a]] (graph-super.md, lattice-tower.md, lambda = a);
      Weil form G = (1/2) Omega (M - V), V = q M^{-1} = a - M; vacuum J = (2M - a)/sqrt(4q - a^2).
 (i)  the adelic qunaught Theta_K: overlaps <Theta_K, 1_D> = #L(D) = q^{h^0(D)} (adelic-gkp.md section 11);
      the trivial-character cutoff cokernel of analytic.md section 13 (Theorem 12): Y(m) = y(m) q^{m/2} solves
      Y_j - a Y_{j-1} + q Y_{j-2} = 0, state (Y_j, Y_{j-1}), window shift W = [[a,-q],[1,0]];
      Casoratian Q(Y_j, Y_{j-1}) = Y_j^2 - a Y_j Y_{j-1} + q Y_{j-1}^2 (Corollary 13);
      Rosati form T(phi, psi) = sum_i phi(alpha_i) psi(q/alpha_i) on R[F] (Proposition 15).

Needs PARI/GP as the binary /usr/bin/gp (called through subprocess) and sympy, numpy.
Run:  python3 check_curve_bridge.py > output_curve_bridge.txt
"""
import itertools
import math
import subprocess
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


def gp(script):
    r = subprocess.run(["gp", "-q", "-f"], input=script, capture_output=True, text=True, timeout=600)
    if r.returncode != 0 or "***" in r.stderr + r.stdout:
        raise RuntimeError(r.stderr + r.stdout)
    return r.stdout


OM = sp.Matrix([[0, 1], [-1, 0]])
EXAMPLES = [  # (name, q, a)
    ("E1, the E mode", 2, -1),
    ("E2, the Pauli six", 5, -2),
    ("E3, class number two", 7, 2),
]
KMAX = 8


def companion(q, a):
    return sp.Matrix([[0, -1], [q, a]])


def invariants(A):
    S = smith_normal_form(A, domain=sp.ZZ)
    return tuple(sorted(abs(int(S[i, i])) for i in range(A.shape[0]) if abs(int(S[i, i])) != 1))


def reduced_forms(D):
    """all positive definite binary forms (A,B,C), B^2-4AC = D < 0, reduced, up to proper equivalence (primitive or not)"""
    out = []
    A = 1
    while 3 * A * A <= -D:
        for B in range(-A + 1, A + 1):
            if (B * B - D) % (4 * A):
                continue
            C = (B * B - D) // (4 * A)
            if C < A:
                continue
            if B < 0 and (A == C):
                continue
            out.append((A, B, C))
        A += 1
    return out


def form_to_step(f, a):
    """Latimer-MacDuffee: the integer matrix of trace a whose Weil form (1/2) Omega (M - V) is the form f"""
    A, B, C = f
    return sp.Matrix([[(a - B) // 2, -C], [A, (a + B) // 2]])


def weil_form(M, q, a):
    V = a * sp.eye(2) - M
    return (OM * (M - V)) / 2


# ------------------------------------------------------------------------------------------------------------
print("== D. The Deligne modules of the three examples (companion convention M = [[0,-1],[q,a]])")
for name, q, a in EXAMPLES:
    M = companion(q, a)
    x = sp.symbols("x")
    ok = (M.T * OM * M == q * OM) and sp.expand(M.charpoly(x).as_expr() - (x**2 - a * x + q)) == 0
    ok = ok and (a % q != 0) and (a * a < 4 * q)
    check(f"D1 {name}: M^T Omega M = q Omega, charpoly x^2 - ({a})x + {q}, ordinary (a != 0 mod q), a^2 < 4q", ok,
          f"M = {M.tolist()}")
    forms = reduced_forms(a * a - 4 * q)
    check(f"D2 {name}: Weil form of the companion step is the principal-class form q x^2 + a xy + y^2",
          weil_form(M, q, a) == sp.Matrix([[q, sp.Rational(a, 2)], [sp.Rational(a, 2), 1]]),
          f"disc {a*a-4*q}; all lattice classes (reduced forms) = {forms}")
    for f in forms:
        Mf = form_to_step(f, a)
        ok = Mf.trace() == a and Mf.det() == q and Mf.T * OM * Mf == q * OM and weil_form(Mf, q, a) == sp.Matrix(
            [[f[0], sp.Rational(f[1], 2)], [sp.Rational(f[1], 2), f[2]]])
        check(f"D3 {name}: form {f} -> integer step {Mf.tolist()}, a symplectic similitude with Weil form = that form", ok)

# ------------------------------------------------------------------------------------------------------------
print("\n== G. Group of points versus Z^2/(1 - M^k) Z^2, k = 1..8, every Weierstrass equation in the isogeny class")
GP_CURVES = r"""
listq2(a)={ my(v); forvec(c=vector(5,i,[0,1]), E=ellinit(c*Mod(1,2)); if(#E==0, next); if(ellap(E)!=a, next);
   v=vector(%d,k, ellgroup(ellinit(c, ffgen(2^k,'t)))); print("C|",c,"|",lift(E.j),"|",v)); }
listodd(q,a)={ my(v); for(A=0,q-1, for(B=0,q-1, if((4*A^3+27*B^2)%%q==0, next); E=ellinit([A,B]*Mod(1,q)); if(ellap(E)!=a, next);
   v=vector(%d,k, ellgroup(ellinit([A,B], ffgen(q^k,'t)))); print("C|",[0,0,0,A,B],"|",lift(E.j),"|",v))); }
""" % (KMAX, KMAX)


def parse_groups(s):
    s = s.strip()[1:-1]
    groups, depth, cur = [], 0, ""
    for ch in s:
        if ch == "[":
            depth += 1
            cur = ""
        elif ch == "]":
            depth -= 1
            groups.append(tuple(sorted(int(t) for t in cur.split(",") if t.strip()) if cur.strip() else ()))
        elif depth == 1:
            cur += ch
    return [tuple(sorted(d for d in g if d != 1)) for g in groups]


curve_data = {}
for name, q, a in EXAMPLES:
    call = f"listq2({a})" if q == 2 else f"listodd({q},{a})"
    out = gp(GP_CURVES + call + "\n")
    curves = []
    for line in out.splitlines():
        if line.startswith("C|"):
            _, coeffs, j, grp = line.split("|")
            curves.append((coeffs, int(j), parse_groups(grp)))
    curve_data[name] = curves
    forms = reduced_forms(a * a - 4 * q)
    lat = {f: [invariants(sp.eye(2) - form_to_step(f, a) ** k) for k in range(1, KMAX + 1)] for f in forms}
    js = sorted(set(c[1] for c in curves))
    print(f"   {name}: {len(curves)} Weierstrass equations with trace {a}; j-invariants {js}")
    for f in forms:
        print(f"     lattice {f}: Z^2/(1-M^k)Z^2 = " + ", ".join("x".join(f"Z{d}" for d in g) or "0" for g in lat[f]))
    # orders must match for every curve and every lattice
    ok = all(math.prod(c[2][k]) == math.prod(lat[f][k]) for c in curves for f in forms for k in range(KMAX))
    check(f"G1 {name}: #E(F_q^k) = det(1 - M^k) for every equation, every lattice class, k = 1..{KMAX}", ok)
    for j in js:
        seqs = set(tuple(c[2]) for c in curves if c[1] == j)
        check(f"G2 {name}, j = {j}: all equations with this j have the same group sequence", len(seqs) == 1)
        seq = list(seqs)[0]
        match = [f for f in forms if lat[f] == list(seq)]
        print(f"     j = {j}: E(F_q^k) = " + ", ".join("x".join(f"Z{d}" for d in g) or "0" for g in seq)
              + f"   matches lattice classes {match}")
        first_fail = {f: next((k + 1 for k in range(KMAX) if lat[f][k] != seq[k]), None) for f in forms}
        print(f"       first k where the lattice class fails: {first_fail}")
    comp_form = reduced_forms(a * a - 4 * q)[0]
    # the companion lattice is the principal form (1, b, c); record whether it matches every curve
    all_match_comp = all(lat[comp_form] == c[2] for c in curves)
    every_curve_some = all(any(lat[f] == c[2] for f in forms) for c in curves)
    check(f"G3 {name}: every curve's group sequence equals Z^2/(1-M^k) for SOME lattice class of the isogeny class",
          every_curve_some)
    expected_comp = {"E1, the E mode": True, "E2, the Pauli six": False, "E3, class number two": True}[name]
    check(f"G4 {name}: the companion lattice alone matches every curve = {expected_comp} (expected)",
          all_match_comp == expected_comp)

# the E-mode table of lattice-tower.md section 2
E1seq = curve_data["E1, the E mode"][0][2]
check("G5 E1: groups agree with the table of lattice-tower.md section 2 (Z4, Z8, Z4, Z16, Z44, Z56, Z116, Z3 x Z96)",
      E1seq == [(4,), (8,), (4,), (16,), (44,), (56,), (116,), (3, 96)])
# E2: j = 1 (End = Z[2i], since j(2i) = 287496 = 1 mod 5) gives Z8; j = 1728 = 3 mod 5 (End = Z[i]) gives Z2 x Z4
E2 = {c[1]: c[2] for c in curve_data["E2, the Pauli six"]}
check("G6 E2: j = 287496 mod 5 = 1 curve has E(F_5) = Z8 (companion lattice Z[2i]); j = 1728 mod 5 = 3 curve has Z2 x Z4 (lattice Z[i])",
      287496 % 5 == 1 and 1728 % 5 == 3 and E2.get(1, [None])[0] == (8,) and E2.get(3, [None])[0] == (2, 4))
# E3: two lattice classes (1,0,6), (2,0,3) give identical group sequences, so groups cannot tell them apart
f1, f2 = reduced_forms(2 * 2 - 28)
same = all(invariants(sp.eye(2) - form_to_step(f1, 2) ** k) == invariants(sp.eye(2) - form_to_step(f2, 2) ** k)
           for k in range(1, 25))
check("G7 E3: the two lattice classes of disc -24 have isomorphic groups Z^2/(1-M^k) for k = 1..24 (invertible ideals)", same)
M1, M2 = form_to_step(f1, 2), form_to_step(f2, 2)
xs = range(-6, 7)
cyc2 = min(abs((sp.Matrix([u, v]).row_join(M2 * sp.Matrix([u, v]))).det()) for u in xs for v in xs if (u, v) != (0, 0))
check("G8 E3: the (2,0,3) step is not GL2(Z)-conjugate to the companion: no cyclic vector (|det(v, Mv)| = 2u^2+3v^2 >= 2)",
      cyc2 >= 2, f"min |det(v, M v)| on a box = {cyc2}")

# ------------------------------------------------------------------------------------------------------------
print("\n== A. The adelic side on E1: y^2 + xy = x^3 + 1 over F_2; overlaps <Theta_K, 1_D> = #L(D) by brute force")
IRRED = {1: 0b11, 2: 0b111}


class GF2d:
    def __init__(s, d):
        s.d, s.mod, s.n = d, IRRED[d], 1 << d

    def mul(s, x, y):
        r = 0
        while y:
            if y & 1:
                r ^= x
            y >>= 1
            x <<= 1
            if x >> s.d & 1:
                x ^= s.mod
        return r

    def pw(s, x, e):
        r = 1
        while e:
            if e & 1:
                r = s.mul(r, x)
            x = s.mul(x, x)
            e >>= 1
        return r

    def inv(s, x):
        return s.pw(x, s.n - 2)

    def frob(s, x):
        return s.mul(x, x)


A1, A2, A3, A4, A6 = 1, 0, 0, 0, 1   # y^2 + a1 xy + a3 y = x^3 + a2 x^2 + a4 x + a6 over F_2


def points(F):
    m = F.mul
    return [(x, y) for x in range(F.n) for y in range(F.n)
            if m(y, y) ^ m(x, y) ^ m(m(x, x), x) ^ A6 == 0]


def add(F, P, Q):
    """Weierstrass group law (characteristic 2: minus = plus); None is O"""
    m = F.mul
    if P is None:
        return Q
    if Q is None:
        return P
    (x1, y1), (x2, y2) = P, Q
    if x1 == x2:
        if y2 == y1 ^ m(A1, x1) ^ A3:   # Q = -P
            return None
        num = m(3 % 2, m(x1, x1)) ^ m(2 % 2, m(A2, x1)) ^ A4 ^ m(A1, y1)
        den = m(2 % 2, y1) ^ m(A1, x1) ^ A3
    else:
        num, den = y2 ^ y1, x2 ^ x1
    lam = m(num, F.inv(den))
    x3 = m(lam, lam) ^ m(A1, lam) ^ A2 ^ x1 ^ x2
    nu = y1 ^ m(lam, x1)
    y3 = m(lam ^ A1, x3) ^ nu ^ A3
    return (x3, y3)


# places of degree 1 and 2
F1, F2 = GF2d(1), GF2d(2)      # F_2 and F_4 (rational points have coordinates 0, 1 in both)
P1 = points(F1)
P2 = points(F2)
N1, N2 = len(P1) + 1, len(P2) + 1
deg2 = []
seen = set()
for (x, y) in P2:
    if x in (0, 1) and y in (0, 1):
        continue
    if (x, y) in seen:
        continue
    conj = (F2.frob(x), F2.frob(y))
    seen |= {(x, y), conj}
    deg2.append(((x, y), conj))
places = [("P%d" % i, 1, [pt]) for i, pt in enumerate(P1)] + [("Q%d" % i, 2, list(o)) for i, o in enumerate(deg2)]
check("A1 E1: #E(F_2) = 4, #E(F_4) = 8, so 3 affine rational points and 2 places of degree 2", N1 == 4 and N2 == 8
      and len(deg2) == 2, f"rational affine points {P1}")


def place_sum(pl):
    """sum in the group law of the geometric points of a place; lies in E(F_2), computed in F_4"""
    S = None
    for pt in pl[2]:
        S = add(F2, S, pt)
    return S


def monomials(n):
    """basis of L(nO): x^i (2i <= n), x^i y (2i+3 <= n); pole orders of x, y at O are 2, 3 (standard)"""
    return [(i, 0) for i in range(n // 2 + 1)] + [(i, 1) for i in range(max(0, (n - 3) // 2 + 1)) if 2 * i + 3 <= n] if n >= 0 else []


def evalf(F, coeffs, mons, pt):
    x, y = pt
    r = 0
    for c, (i, e) in zip(coeffs, mons):
        if c:
            t = F.pw(x, i)
            if e:
                t = F.mul(t, y)
            r ^= t
    return r


def count_L(n, E):
    """#{f in K : (f) + nO - E >= 0} for E a reduced effective divisor of affine places"""
    mons = monomials(n)
    cnt = 0
    for coeffs in itertools.product((0, 1), repeat=len(mons)):
        ok = True
        for pl in E:
            F = F1 if pl[1] == 1 else F2
            if evalf(F, coeffs, mons, pl[2][0]) != 0:
                ok = False
                break
        cnt += ok
    return cnt


def rr_prediction(n, E):
    d = n - sum(pl[1] for pl in E)
    if d > 0:
        return d
    if d < 0:
        return 0
    S = None
    for pl in E:
        S = add(F2, S, place_sum(pl))
    return 1 if S is None else 0     # nO - E ~ 0 iff the points of E sum to O (Abel-Jacobi)


rows, bad = [], []
classes = {}   # (degree, class in E(F_2)) -> h^0 values seen
for n in range(-1, 7):
    for r in range(0, len(places) + 1):
        for E in itertools.combinations(places, r):
            dE = sum(pl[1] for pl in E)
            if dE > n + 1:
                continue
            c = count_L(n, E)
            h0 = round(math.log2(c))
            pred = rr_prediction(n, E)
            rows.append((n, [pl[0] for pl in E], n - dE, c, h0, pred))
            if 2 ** h0 != c or h0 != pred:
                bad.append(rows[-1])
            S = None
            for pl in E:
                S = add(F2, S, place_sum(pl))
            negS = None if S is None else (S[0], S[1] ^ S[0])     # -(x,y) = (x, y + x) here
            classes.setdefault((n - dE, negS), set()).add(h0)
print(f"   {len(rows)} divisors D = nO - E (n = -1..6, E a reduced effective divisor of affine places of degree <= 2)")
for (n, E, d, c, h0, pred) in rows:
    if n in (-1, 0, 1, 4) or d == 0:
        if len(E) <= 2 and (d >= 0 or n <= 0):
            print(f"     D = {n}O - ({' + '.join(E) if E else '0'}):  deg {d:2d}   #L(D) = {c:3d} = 2^{h0}   RR+Abel predicts h0 = {pred}")
check("A2 E1: <Theta_K, 1_D> = #L(D) is a power of q and h^0(D) agrees with Riemann-Roch + Abel-Jacobi on every divisor",
      not bad, f"{len(rows)} divisors, {len(bad)} disagreements")
check("A3 E1: h^0(nO) = 1, 1, 2, 3, 4, 5, 6 for n = 0..6 and 0 for n = -1",
      [r[4] for r in rows if not r[1]] == [0, 1, 1, 2, 3, 4, 5, 6])
check("A4 E1: h^0 is a function of the class in Pic (degree, point of E(F_2)) on all divisors tested",
      all(len(v) == 1 for v in classes.values()), f"{len(classes)} classes met")
pic0 = {k[1]: list(v)[0] for k, v in classes.items() if k[0] == 0}
check("A5 E1: in degree 0, h^0 = 1 on the trivial class and 0 on the three others (Pic^0 = E(F_2), order 4)",
      len(pic0) == 4 and pic0.get(None) == 1 and sum(pic0.values()) == 1)

# a_n and P(T) from the h^0 table: A(n) = (1/h) sum_{c in Pic^n} (q^{h0(c)} - 1), a_n = h A(n)/(q-1)
q, a, h = 2, -1, 4
Avals = {}
for d in range(-1, 6):
    cl = {k[1]: list(v)[0] for k, v in classes.items() if k[0] == d}
    if len(cl) == h:
        Avals[d] = sp.Rational(sum(q ** v - 1 for v in cl.values()), h)
check("A6 E1: A(n) from the overlap table: A(-1) = 0, A(0) = (q-1)/h = 1/4, A(n) = q^n - 1 for n = 1..5",
      Avals.get(-1) == 0 and Avals.get(0) == sp.Rational(1, 4) and all(Avals.get(n) == q ** n - 1 for n in range(1, 6)),
      f"{ {k: str(v) for k, v in sorted(Avals.items())} }")
T = sp.symbols("T")
an = [sp.Rational(h, q - 1) * Avals[n] for n in range(0, 6)]
Zs = sum(an[n] * T ** n for n in range(6))
Ps = sp.expand(sp.series(Zs * (1 - T) * (1 - q * T), T, 0, 6).removeO())
check("A7 E1: Z(T) = sum a_n T^n from the overlaps gives P(T) = Z (1-T)(1-qT) = 1 + T + 2T^2 (to order T^5)",
      sp.expand(Ps - (1 - a * T + q * T ** 2)) == 0, f"a_n = {an}")
# effective divisors counted from places (independent of h^0): places of degree d from N_k
Nk = {k: 2 ** k + 1 - sum(complex(r) ** k for r in np.roots([1, -a, q])).real for k in range(1, 6)}
Bd = {d: round(sum(sp.mobius(d // e) * Nk[e] for e in sp.divisors(d)) / d) for d in range(1, 6)}
Zplaces = sp.prod([(1 - T ** d) ** (-Bd[d]) for d in range(1, 6)])
an_pl = [sp.series(Zplaces, T, 0, 6).removeO().coeff(T, n) for n in range(6)]
check("A8 E1: a_n from the overlaps equals the number of effective divisors counted from places (Euler product)",
      an_pl == an, f"places by degree {Bd}; a_n = {an_pl}")

# ------------------------------------------------------------------------------------------------------------
print("\n== R. The Riemann-Roch cokernel of analytic section 13 (Theorem 12), exactly, cutoff N = 5")


def cokernel(q, a, h, N=5):
    """Y-space orthogonal to E(B) in the trivial-character sector. A(n) from Riemann-Roch in genus one."""
    def A(n):
        if n < 0:
            return sp.Integer(0)
        if n == 0:
            return sp.Rational(q - 1, h)
        return sp.Integer(q ** n - 1)
    js = list(range(-N, N + 1))
    # y perp Ef for all admissible c  <=>  T(j) = sum_m Y(m) A(j-m) lies in span{1, q^j} on j in [-N, N]
    Ys = sp.symbols(f"Y0:{2*N+1}")
    al, be = sp.symbols("alpha beta")
    eqs = [sum(Ys[mi] * A(j - m) for mi, m in enumerate(js)) - al - be * sp.Integer(q) ** j for j in js]
    Mat, _ = sp.linear_eq_to_matrix(eqs, list(Ys) + [al, be])
    ns = Mat.nullspace()
    Ybasis = [v[:2 * N + 1, 0] for v in ns]
    return js, Ybasis, A


# check the image really lies in S_N (support of Ef) for a random admissible c, then the cokernel
for name, q, a in EXAMPLES[:2]:
    h = q + 1 - a
    N = 5
    js, Yb, A = cokernel(q, a, h, N)
    # admissible c: sum c = 0, sum c q^j = 0
    cs = sp.Matrix([[1] * (2 * N + 1), [sp.Integer(q) ** j for j in js]]).nullspace()
    supp_ok = True
    for c in cs[:3]:
        for m in list(range(-N - 6, -N)) + list(range(N + 1, N + 7)):
            if sum(c[i] * A(j - m) for i, j in enumerate(js)) != 0:
                supp_ok = False
    check(f"R1 {name}: Ef = sum_j c_j q^(m/2) A(j-m) vanishes outside [-N, N] for admissible c (image in S_N)", supp_ok)
    check(f"R2 {name}: the cutoff cokernel has dimension 2g = 2", len(Yb) == 2)
    rec_ok = all(Y[i] - a * Y[i - 1] + q * Y[i - 2] == 0 for Y in Yb for i in range(2, 2 * N + 1))
    check(f"R3 {name}: every cokernel vector satisfies Y_j - a Y_(j-1) + q Y_(j-2) = 0 on the whole window", rec_ok)
    # window shift on the state s_j = (Y_j, Y_{j-1})
    S0 = sp.Matrix([[Yb[0][5], Yb[1][5]], [Yb[0][4], Yb[1][4]]])
    S1 = sp.Matrix([[Yb[0][6], Yb[1][6]], [Yb[0][5], Yb[1][5]]])
    W = sp.simplify(S1 * S0.inv())
    check(f"R4 {name}: transfer matrix on (Y_j, Y_(j-1)) is W = [[a, -q], [1, 0]]", W == sp.Matrix([[a, -q], [1, 0]]),
          f"W = {W.tolist()}")
    # Casoratian similitude along the computed cokernel vectors
    Qf = lambda u, v: u * u - a * u * v + q * v * v
    sim = all(sp.simplify(Qf(Y[i + 1], Y[i]) - q * Qf(Y[i], Y[i - 1])) == 0 for Y in Yb for i in range(1, 2 * N))
    wr = all(sp.simplify((Yb[0][i + 1] * Yb[1][i] - Yb[0][i] * Yb[1][i + 1]) - q * (Yb[0][i] * Yb[1][i - 1] - Yb[0][i - 1] * Yb[1][i])) == 0
             for i in range(1, 2 * N))
    check(f"R5 {name}: Casoratian Q and the antisymmetric Casoratian (discrete Wronskian) both scale by q per step", sim and wr)

# ------------------------------------------------------------------------------------------------------------
print("\n== B. The bridge: cokernel phase space -> R[F] -> the Deligne module")
x = sp.symbols("x")
for name, q, a in EXAMPLES:
    D = a * a - 4 * q
    M = companion(q, a)
    V = a * sp.eye(2) - M
    W = sp.Matrix([[a, -q], [1, 0]])
    S = sp.Matrix([[0, -1], [1, 0]])
    G = weil_form(M, q, a)
    Qm = sp.Matrix([[1, sp.Rational(-a, 2)], [sp.Rational(-a, 2), q]])
    check(f"B1 {name}: S = [[0,-1],[1,0]] intertwines the window shift with the step: S W S^-1 = M", S * W * S.inv() == M)
    check(f"B2 {name}: S pulls back Omega to the antisymmetric Casoratian (S^T Omega S = Omega) and the Weil form to Q",
          S.T * OM * S == OM and S.T * G * S == Qm)
    # Rosati form on R[F], basis (1, F), from the eigenvalues numerically, and exactly
    al = np.roots([1, -a, q])
    basis = [lambda t: 1, lambda t: t]
    Tnum = np.array([[sum(f(r) * g(q / r) for r in al) for g in basis] for f in basis])
    Tex = sp.Matrix([[2, a], [a, 2 * q]])
    check(f"B3 {name}: Rosati Gram on (1, F) is [[2, a], [a, 2q]] (numerically, from the Frobenius eigenvalues)",
          np.allclose(Tnum, np.array(Tex.tolist(), dtype=float)), f"max |imag| = {np.abs(Tnum.imag).max():.1e}")
    # (Y_j, Y_{j-1}) -> Y_j - Y_{j-1} F, coordinates (m, n) in basis (1, F): matrix C = [[1, 0], [0, -1]]
    Cm = sp.Matrix([[1, 0], [0, -1]])
    Fm = sp.Matrix([[0, -q], [1, a]])     # multiplication by F on R[F] in basis (1, F)
    Vm = a * sp.eye(2) - Fm
    check(f"B4 {name}: (Y_j, Y_(j-1)) -> Y_j - Y_(j-1) F carries Q to (1/2) Rosati and W to multiplication by V",
          Cm.T * Tex * Cm / 2 == Qm and Cm * W == Vm * Cm)
    # cyclic vector map R[F] -> Z^2: phi -> phi(M) e2; composed with Rosati involution phi(F) -> phi(V)
    psi = sp.Matrix.hstack(sp.Matrix([0, 1]), M * sp.Matrix([0, 1]))        # columns: images of 1, F
    rosati_inv = sp.Matrix([[1, a], [0, -1]])                              # m + nF -> m + n(a - F)
    check(f"B5 {name}: S = psi o (Rosati involution) o (cokernel -> R[F]); psi carries F to M and (1/2) Rosati to the Weil form",
          psi * rosati_inv * Cm == S and psi * Fm == M * psi and psi.T * G * psi == Tex / 2)
    # the vacuum
    J = (2 * M - a * sp.eye(2)) / sp.sqrt(-D)
    gJ = OM * J
    check(f"B6 {name}: J = (2M - a)/sqrt(4q - a^2) has J^2 = -1, JM = MJ, and Omega(., J .) = 2 G / sqrt(4q - a^2) > 0",
          sp.simplify(J * J + sp.eye(2)) == sp.zeros(2) and sp.simplify(J * M - M * J) == sp.zeros(2)
          and sp.simplify(gJ - 2 * G / sp.sqrt(-D)) == sp.zeros(2) and gJ[0, 0] > 0 and sp.simplify(gJ.det()) > 0)
    # independent numerical vacuum: normal form of M / sqrt(q)
    ev, P = np.linalg.eig(np.array(M.tolist(), dtype=float) / math.sqrt(q))
    i0 = int(np.argmax(ev.imag))
    v = P[:, i0]
    B = np.column_stack([v.real, v.imag])          # M/sqrt q acts on span(Re v, Im v) as a rotation
    Jn = B @ np.array([[0, -1], [1, 0]]) @ np.linalg.inv(B)
    Om = np.array([[0, 1], [-1, 0]], float)
    if (Om @ Jn)[0, 0] < 0:
        Jn = -Jn
    check(f"B7 {name}: vacuum from the normal form of M/sqrt(q) agrees with the closed form",
          np.allclose(Jn, np.array(J.evalf().tolist(), dtype=float)))
    # the bridge identity: (vacuum form) o S = Q * 2/sqrt|D| = Rosati o C / sqrt|D|
    lhs = sp.simplify(S.T * gJ * S)
    check(f"B8 {name}: BRIDGE  Omega(Sy, J Sy) = (2/sqrt(4q-a^2)) Q(y) = Rosati(Cy)/sqrt(4q-a^2) on the cokernel phase space",
          sp.simplify(lhs - 2 * Qm / sp.sqrt(-D)) == sp.zeros(2) and sp.simplify(lhs - Cm.T * Tex * Cm / sp.sqrt(-D)) == sp.zeros(2),
          f"scalar sqrt(4q - a^2) = sqrt({-D})")
    # uniqueness: symmetric q-similitude forms of M form a 1-dim space (one elliptic mode)
    s11, s12, s22 = sp.symbols("s11 s12 s22")
    Bs = sp.Matrix([[s11, s12], [s12, s22]])
    sol = sp.linsolve(list(M.T * Bs * M - q * Bs), [s11, s12, s22])
    dim = len(list(sol)[0].free_symbols)
    check(f"B9 {name}: the symmetric forms B with M^T B M = q B form a line (so any two such positive forms are proportional)",
          dim == 1)
    # for every lattice class, the same holds after the rational change of basis
    for f in reduced_forms(D)[1:]:
        Mf = form_to_step(f, a)
        # rational P with P M P^-1 = Mf: map cyclic vector e2 of M to any nonzero u
        u = sp.Matrix([1, 0])
        Pm = sp.Matrix.hstack(u, Mf * u) * sp.Matrix.hstack(sp.Matrix([0, 1]), M * sp.Matrix([0, 1])).inv()
        Jf = (2 * Mf - a * sp.eye(2)) / sp.sqrt(-D)
        ratio = sp.simplify((Pm.T * OM * Jf * Pm)[0, 0] / gJ[0, 0])
        check(f"B10 {name}: lattice class {f}: its vacuum form pulled back to the companion lattice is a positive multiple",
              sp.simplify(Pm * M * Pm.inv() - Mf) == sp.zeros(2)
              and sp.simplify(Pm.T * OM * Jf * Pm - ratio * gJ) == sp.zeros(2) and ratio > 0, f"factor {ratio}")

# ------------------------------------------------------------------------------------------------------------
print("\n== H. The Howe sign: which choice of prime above p makes Omega (rather than -Omega) a polarisation")
for name, q, a in EXAMPLES:
    out = gp(f"nf=nfinit(x^2-({a})*x+{q}); r=nf.roots[1]; print(imag(r)>0); dec=idealprimedec(nf,{q}); "
             f"for(i=1,#dec, print(nfeltval(nf,x,dec[i]),\" \",nfeltval(nf,({a})-x,dec[i])));\n")
    lines = out.split()
    up = lines[0] == "1"
    vals = [(int(lines[1 + 2 * i]), int(lines[2 + 2 * i])) for i in range((len(lines) - 1) // 2)]
    # Phi_eps = Phi_+ iff the root in the upper half plane (x under nf.roots[1] when up) is the p-adic non-unit
    signs = [(+1 if ((vF > 0) == up) else -1) for (vF, vV) in vals]
    check(f"H1 {name}: two primes above {q}; at each, exactly one of F, V is a non-unit; Omega for one, -Omega for the other",
          len(vals) == 2 and all((vF > 0) != (vV > 0) for vF, vV in vals) and sorted(signs) == [-1, 1],
          f"valuations (F, V) = {vals}, signs = {signs}")
    M = companion(q, a)
    V = a * sp.eye(2) - M
    J = (2 * M - a * sp.eye(2)) / sp.sqrt(4 * q - a * a)
    ok = True
    for s in (+1, -1):
        Oe, Je, iota = s * OM, s * J, s * (M - V)
        R = Oe * iota
        ok &= R == R.T and R[0, 0] > 0 and R.det() > 0                       # Phi_eps-positivity of Omega_eps
        ok &= sp.simplify(Oe * Je - OM * J) == sp.zeros(2)                   # the Riemann form is sign-independent
    check(f"H2 {name}: Omega_eps = s Omega, J_eps = s J (s = +-1): Omega_eps(., iota_eps .) > 0 and Omega_eps(., J_eps .) = Omega(., J .)", ok)

print(f"\n{npass} of {npass + nfail} pass" + ("" if nfail == 0 else f"  ({nfail} FAIL)"))
