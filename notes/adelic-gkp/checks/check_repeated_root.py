#!/usr/bin/env python3
"""Checks for 'A repeated root' (notes/adelic-gkp/repeated-root.md), lane S, 2026-10-06.

The Fermat quartic case of ff-dirichlet.md: q = 5, N = 4, f = t^4 + 1 = (t^2 + 2)(t^2 + 3), chi = prod_i (./P_i)_4, the quartic
power-residue symbol sent to C by 2 -> i (2 generates F_5^x). P_chi = (x + 1 + 2i)^2 (review J7).
A. the curve C: y^4 = c (t^4 + 1): c, genus, point counts over F_{5^k} (k = 1..6, brute force), L-polynomial, factorisation into
   Lambda(u, chi^j) from character sums; the Klein-four quotients E, E', E'' and #J(F_{5^k}).
B. Frobenius on the quotient E' (the chi + chibar part up to isogeny) as an element of Z[i] (group law, PARI); groups of points
   against the semisimple lattice L and the companion lattice R; a genus-one supersingular example.
C. the lattices: L = Z[i]^2 with F = alpha I against R = Z[i][F, V] inside E = Q(i)[x]/(x - alpha)^2: forms, Weil forms, vacua.
D. the Connes citation (Jordan form for multiple zeros), byte-checked in refs/src.
Needs python-flint, sympy, numpy, PARI/GP (/usr/bin/gp). Runs in a few seconds.
"""
import itertools
import os
import random
import subprocess

import flint
import numpy as np
import sympy as sp

npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


def gp(script):
    r = subprocess.run(["/usr/bin/gp", "-q", "-f"], input='default(colors,"no");\n' + script + "\nquit\n",
                       capture_output=True, text=True, timeout=120)
    return r.stdout


q, N = 5, 4
I = sp.I
u, x = sp.symbols("u x")

# ---------------------------------------------------------------- A. the curve
# A1 c from the reciprocity condition c^((q-1)/N) = (-1)^((q-1) d/N), d = deg f = 4
d = 4
cands = [c for c in range(1, q) if pow(c, (q - 1) // N, q) == (-1) ** ((q - 1) * d // N) % q]
check("A1 reciprocity c^((q-1)/N) = (-1)^((q-1)d/N) = +1 fixes c = 1 (the only 4th power in F_5^x is 1): C is y^4 = t^4 + 1",
      cands == [1], f"solutions {cands}")


def field(k):
    F = flint.fq_default_ctx(q, k)
    els = [F(list(v)) for v in itertools.product(range(q), repeat=k)]
    return F, els


def count_C(k, c=1):
    """#C(F_{5^k}) for the smooth model of y^4 = c (t^4 + 1): affine points + the places over infinity."""
    F, els = field(k)
    Q = q ** k
    aff = 0
    for t in els:
        v = c * (t ** 4 + 1)
        if v == 0:
            aff += 1
        elif v ** ((Q - 1) // 4) == 1:
            aff += 4
    # infinity: y^4/t^4 -> c; unramified since 4 | deg f; points = #{w: w^4 = c} over F_{5^k}
    cF = F(c)
    inf = 4 if cF ** ((Q - 1) // 4) == 1 else 0
    return aff + inf


# A2 genus by Riemann-Hurwitz: branch points = roots of t^4+1 (in F_25, none in F_5), each totally ramified; infinity unramified
F25, els25 = field(2)
roots25 = [t for t in els25 if t ** 4 + 1 == 0]
F5, els5 = field(1)
roots5 = [t for t in els5 if t ** 4 + 1 == 0]
g_RH = (4 * (-2) + len(roots25) * (4 - 1)) // 2 + 1
check("A2 Riemann-Hurwitz: t^4+1 has 4 distinct roots, all in F_25 \\ F_5 (t^2 = 2, 3); each is totally ramified (v(t^4+1) = 1, prime to 4); "
      "infinity is NOT a branch point (v_inf(t^4+1) = -4 = 0 mod 4), it splits into 4 places; 2g-2 = 4(-2) + 4*3 = 4, g = 3",
      len(roots25) == 4 and len(roots5) == 0 and g_RH == 3, f"roots in F_25: {len(roots25)}, in F_5: {len(roots5)}, g = {g_RH}")

# A3 smooth plane model Y^4 = T^4 + Z^4: projective count over F_5, F_25 equals the count above; smooth (char 5 != 2)
def count_plane(k):
    F, els = field(k)
    pts = 0
    for (a, b) in itertools.product(els, els):           # Z = 1
        if b ** 4 == a ** 4 + 1:
            pts += 1
    for a in els:                                         # Z = 0, T = 1
        if a ** 4 == 1:
            pts += 1
    # Z = 0, T = 0: (0:1:0) needs 1 = 0, not on the curve
    return pts


counts = [count_C(k) for k in range(1, 7)]
check("A3 brute-force counts #C(F_{5^k}), k = 1..6 (affine + 4 rational places at infinity); the plane quartic Y^4 = T^4 + Z^4 gives the same for k = 1, 2",
      counts[:2] == [count_plane(1), count_plane(2)], f"counts {counts}")


def Lpoly_from_counts(Ns, g):
    """zeta numerator 1 + a1 u + ... + q^g u^2g from N_1..N_g (Newton + functional equation)."""
    S = [q ** k + 1 - Ns[k - 1] for k in range(1, g + 1)]          # power sums of the alpha_j
    a = [sp.Integer(1)]
    for k in range(1, g + 1):                                        # e_k from Newton (with signs for prod(1 - alpha u))
        a.append(sp.Rational(-sum(a[k - i] * S[i - 1] for i in range(1, k + 1)), k))
    for k in range(g + 1, 2 * g + 1):
        a.append(q ** (k - g) * a[2 * g - k])
    return a


aC = Lpoly_from_counts(counts[:3], 3)
LC = sp.expand(sum(c * u ** k for k, c in enumerate(aC)))
roots_all = sp.Poly(sp.expand(u ** 6 * LC.subs(u, 1 / u)), u).all_roots()


def pred(k):
    return sp.expand(q ** k + 1 - sum(r ** k for r in roots_all))


preds = [int(sp.nsimplify(sp.N(pred(k), 40))) for k in range(1, 7)]
check("A4 the L-polynomial of C from N_1..N_3 (degree 2g = 6, top coefficient 5^3) predicts N_4, N_5, N_6, which the brute force confirms",
      preds == counts and aC[6] == 125, f"L_C(u) = {sp.factor(LC)}")

# A5 Lambda(u, chi^j) from character sums: chi(m) = prod_P (m mod P)^((25-1)/4), P = t^2+2, t^2+3; 2 -> i
def pmod(a, P):
    a = [v % q for v in a]
    while len(a) >= len(P):
        if a[-1]:
            c = a[-1]
            sh = len(a) - len(P)
            for i, pv in enumerate(P):
                a[sh + i] = (a[sh + i] - c * pv) % q
        a.pop()
    return a


def pmulmod(a, b, P):
    r = [0] * (len(a) + len(b))
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            r[i + j] += av * bv
    return pmod(r, P)


def resid4(m, P):
    a = pmod(m, P)
    if not any(a):
        return None
    r = [1]
    for _ in range(6):
        r = pmulmod(r, a, P)
    r = (r + [0, 0])[:2]
    assert r[1] == 0
    return {1: 0, 2: 1, 4: 2, 3: 3}[r[0]]                # dlog base 2 in F_5


Ps = [[2, 0, 1], [3, 0, 1]]


def chi_exp(m):
    e = 0
    for P in Ps:
        v = resid4(m, P)
        if v is None:
            return None
        e += v
    return e % 4


def Lambda_chi(j):
    S = []
    for k in range(0, 4):                                  # deg L <= deg f - 1 = 3
        s = 0
        for coeffs in itertools.product(range(q), repeat=k):
            m = list(coeffs) + [1]
            e = chi_exp(m)
            if e is not None:
                s += I ** ((j * e) % 4)
        S.append(sp.expand(s))
    L = sum(S[k] * u ** k for k in range(4))
    Lam, rem = sp.div(sp.expand(L), 1 - u, u)              # even chi: Lambda = L/(1-u)
    return sp.expand(Lam), sp.expand(rem), S


Lams = {}
for j in (1, 2, 3):
    Lam, rem, S = Lambda_chi(j)
    Lams[j] = Lam
check("A5 chi, chi^2, chi^3 are even (L(1) = 0): Lambda = L/(1-u) exactly, each of degree d - 2 = 2",
      all(sp.Poly(Lams[j], u).degree() == 2 for j in (1, 2, 3)), "; ".join(f"Lambda(chi^{j}) = {Lams[j]}" for j in (1, 2, 3)))
check("A6 Lambda(u, chi) = 1 + (2+4i)u + (-3+4i)u^2 (as in review J7), chi^3 = conj(chi) gives the conjugate, chi^2 gives 1 - 2u + 5u^2",
      sp.expand(Lams[1] - (1 + (2 + 4 * I) * u + (-3 + 4 * I) * u ** 2)) == 0
      and sp.expand(Lams[3] - sp.conjugate(Lams[1]).subs(sp.conjugate(u), u)) == 0
      and sp.expand(Lams[2] - (1 - 2 * u + 5 * u ** 2)) == 0)
Pchi = sp.expand(x ** 2 * Lams[1].subs(u, 1 / x))
alpha = -1 - 2 * I
check("A7 P_chi(x) = (x - alpha)^2 with alpha = -1 - 2i: discriminant 0, |alpha|^2 = 5 (RH holds, with a double root)",
      sp.expand(Pchi - (x - alpha) ** 2) == 0 and sp.discriminant(Pchi, x) == 0 and sp.expand(alpha * sp.conjugate(alpha)) == 5,
      f"P_chi = {sp.factor(Pchi, extension=I)}")
prodL = sp.expand(Lams[1] * Lams[2] * Lams[3])
check("A8 L_C(u) = Lambda(chi) Lambda(chi^2) Lambda(chi^3) = (1 + 2u + 5u^2)^2 (1 - 2u + 5u^2) exactly",
      sp.expand(prodL - LC) == 0 and sp.expand(LC - (1 + 2 * u + 5 * u ** 2) ** 2 * (1 - 2 * u + 5 * u ** 2)) == 0)
twist_ok = [c for c in (2, 3, 4) if [count_C(k, c) for k in (1, 2, 3)] == counts[:3]]
check("A9 control: the twists y^4 = c (t^4+1), c = 2, 3, 4, have different counts over F_5..F_125 (so c = 1 is also fixed by matching counts)",
      twist_ok == [], f"counts for c = 2, 3, 4: {[[count_C(k, c) for k in (1, 2, 3)] for c in (2, 3, 4)]}")

# A10 the companion matrix of P_C(x) = x^6 L_C(1/x) is not semisimple (a companion matrix is cyclic: min poly = charpoly)
PC = sp.Poly(sp.expand(x ** 6 * LC.subs(u, 1 / x)), x)
cf = PC.all_coeffs()                                       # leading first
Cmp = sp.zeros(6, 6)
for i in range(1, 6):
    Cmp[i, i - 1] = 1
for i in range(6):
    Cmp[i, 5] = -cf[6 - i]
rad = sp.Poly((x ** 2 + 2 * x + 5) * (x ** 2 - 2 * x + 5), x)
radC = sp.zeros(6, 6)
for k, c in enumerate(reversed(rad.all_coeffs())):
    radC += c * Cmp ** k
mid = cf[3]
check("A10 the trivial-character companion step on Z^6 (lane A's Riemann-Roch cokernel shift for this curve) is NOT semisimple: "
      "rad(P_C)(C) != 0, with P_C = (x^2+2x+5)^2 (x^2-2x+5); its middle coefficient is prime to 5 (J is ordinary)",
      radC != sp.zeros(6, 6) and (Cmp.charpoly(x).as_expr() - PC.as_expr()).expand() == 0 and mid % 5 != 0,
      f"P_C = {PC.as_expr()}, middle coefficient {mid}")

# A11 Klein-four quotients: sigma1: y -> -y, sigma2: t -> -t, sigma3 = sigma1 sigma2.
#  C/sigma1: w^2 = t^4 + 1 (w = y^2)              -> E  : Y^2 = X^3 + X   (X = 2(w + t^2), Y = 4 t (w + t^2))
#  C/sigma2: z^2 = r^4 - 1 (r = y, z = t^2)        -> E' : Y^2 = X^3 + 4X  (X = 2(z + r^2), Y = 4 r (z + r^2))
#  C/sigma3: z^2 = r^4 - 1 (r = y/t, z = t^2(r^4-1)) -> E'' = E'
#  C/<sigma1, sigma2>: w^2 = s^2 + 1 (s = t^2, w = y^2), a conic: genus 0
def count_quartic(k, b):
    """smooth model of z^2 = r^4 + b: affine + 2 points at infinity (leading coefficient 1 is a square)."""
    F, els = field(k)
    Q = q ** k
    n = 2
    for r in els:
        v = r ** 4 + b
        n += 1 if v == 0 else (2 if v ** ((Q - 1) // 2) == 1 else 0)
    return n


def count_conic(k):
    F, els = field(k)
    Q = q ** k
    n = 2                                                   # w/s -> +-1 at infinity
    for s in els:
        v = s ** 2 + 1
        n += 1 if v == 0 else (2 if v ** ((Q - 1) // 2) == 1 else 0)
    return n


out = gp("""{for(k=1,6, my(g=ffgen(5^k,'a), e1=ellinit([0,0,0,1,0],g), e2=ellinit([0,0,0,4,0],g));
  print(k,"|",ellcard(e1),"|",ellcard(e2),"|",ellgroup(e1),"|",ellgroup(e2)))};
print("HC ", hyperellcharpoly(Mod(1,5)*(x^4+1)), " ", hyperellcharpoly(Mod(1,5)*(x^4-1)));""")
grp = {}
for line in out.strip().splitlines():
    if line.startswith("HC"):
        hc = line
        continue
    k, n1, n2, g1, g2 = line.split("|")
    grp[int(k)] = (int(n1), int(n2), eval(g1), eval(g2))
qE = [count_quartic(k, 1) for k in range(1, 7)]
qE2 = [count_quartic(k, -1) for k in range(1, 7)]
check("A11 the quotient models match their Weierstrass forms: #(w^2 = t^4+1) = #E(Y^2 = X^3+X), #(z^2 = r^4-1) = #E'(Y^2 = X^3+4X), k = 1..6",
      qE == [grp[k][0] for k in range(1, 7)] and qE2 == [grp[k][1] for k in range(1, 7)],
      f"#E = {qE}, #E' = {qE2}; PARI hyperellcharpoly: {hc[3:]}")
check("A12 C/<sigma1, sigma2> is the conic w^2 = s^2 + 1: 5^k + 1 points for k = 1..6 (genus 0, the Kani-Rosen hypothesis)",
      [count_conic(k) for k in range(1, 7)] == [q ** k + 1 for k in range(1, 7)])
LE = 1 - 2 * u + 5 * u ** 2
LE2 = 1 + 2 * u + 5 * u ** 2
okL = all(q ** k + 1 - grp[k][0] == sp.expand(sum(r ** k for r in sp.Poly(x ** 2 - 2 * x + 5, x).all_roots())) for k in (1, 2))
check("A13 genera 1 + 1 + 1 = 3 and L_C = L_E L_E' L_E'' with L_E = 1 - 2u + 5u^2 (a_E = 2), L_E' = L_E'' = 1 + 2u + 5u^2 (a_E' = -2): "
      "J ~ E x E' x E'' over F_5 (Kani-Rosen, quoted)",
      sp.expand(LE * LE2 ** 2 - LC) == 0 and grp[1][0] == 4 and grp[1][1] == 8 and okL)
Jk = []
okJ = True
for k in range(1, 7):
    nJ = sp.expand(sp.prod([1 - r ** k for r in roots_all]))
    nJ = int(sp.nsimplify(sp.N(nJ, 60)))
    Jk.append(nJ)
    okJ &= nJ == grp[k][0] * grp[k][1] ** 2
check("A14 #J(F_{5^k}) = prod_j (1 - alpha_j^k) from L_C equals #E * #E'^2 over F_{5^k}, k = 1..6 (orders only: they cannot see semisimplicity)",
      okJ, f"#J = {Jk}")

# ---------------------------------------------------------------- B. Frobenius on E' as an element of Z[i]
gpid = r"""
idtest(k,z,s)={my(g=ffgen(5^k,'a), e=ellinit([0,0,0,4,0],g), T=[0*g,0*g], bad=0, n=1, off=0);
 my(iota=(P)->if(#P==1, T, if(P[1]==0, [0], [1/P[1], z*P[2]/P[1]^2])));
 for(j=0,5^k-1, my(d=digits(j,5), x=0*g); for(m=1,#d, x=x*g+d[m]);
   my(r=x^3+4*x, L=List());
   if(r==0, listput(L,[x,r]), if(issquare(r), my(y=sqrt(r)); listput(L,[x,y]); listput(L,[x,-y])));
   for(i=1,#L, my(P=L[i]); n++; if(!ellisoncurve(e,iota(P)), off++);
     my(fP=[P[1]^5,P[2]^5], iP=elladd(e,iota(P),T));
     my(Q=elladd(e,elladd(e,fP,P),ellmul(e,iP,2*s))); if(Q!=[0], bad++)));
 [n, ellcard(e), bad, off]};
for(k=1,3, for(z=2,3, for(s=-1,1, if(s, print(k,"|",z,"|",s,"|",idtest(k,z,s))))));
print("SS|", ellgroup(ellinit([0,0,0,0,1],ffgen(25,'w))), "|", ellcard(ellinit([0,0,0,0,1],ffgen(5,'v))));
"""
res = {}
for line in gp(gpid).strip().splitlines():
    if line.startswith("SS"):
        ss = line
        continue
    k, z, s, v = line.split("|")
    res[(int(k), int(z), int(s))] = eval(v)
check("B1 the CM automorphism: r -> zeta r on z^2 = r^4 - 1 is (X, Y) -> (1/X, zeta Y/X^2) on E'; it maps E'(F_{5^k}) to itself (k = 1..3); "
      "[iota] = iota - iota(O), iota(O) = (0, 0)",
      all(v[3] == 0 and v[0] == v[1] for v in res.values()))
check("B2 Frobenius of E' is the element -1 - 2[iota_2] of Z[iota] (iota_2: r -> 2r, the automorphism induced by y -> 2y on C): "
      "pi + 1 + 2[iota_2] kills every point of E'(F_{5^k}), k = 1..3",
      all(res[(k, 2, 1)][2] == 0 for k in (1, 2, 3)))
check("B3 control: pi + 1 - 2[iota_2] (the conjugate) fails on 16 of 32 points over F_25 and 96 of 104 over F_125 "
      "(over F_5 the two agree, since 4[iota] kills E'(F_5) = Z/2 x Z/4)",
      res[(2, 2, -1)][2] > 0 and res[(3, 2, -1)][2] > 0 and res[(1, 2, -1)][2] == 0,
      f"failures {[res[(k, 2, -1)][2] for k in (1, 2, 3)]}")


def zmat(z):
    z = sp.expand(z)
    a, b = sp.re(z), sp.im(z)
    return sp.Matrix([[a, -b], [b, a]])


def snf_diag(M):
    from sympy.matrices.normalforms import smith_normal_form
    D = smith_normal_form(sp.Matrix(M), domain=sp.ZZ)
    return sorted([abs(D[i, i]) for i in range(min(D.shape)) if abs(D[i, i]) != 1])


# the lattices, over Z: L = Z[i]^2 with F = alpha I;  R = Z[i] e0 + Z[i] e1, e1 = n/(2 - i), n = F - alpha, F e0 = alpha e0 + (2 - i) e1
FL = sp.diag(zmat(alpha), zmat(alpha))
FR = sp.zeros(4, 4)
FR[0:2, 0:2] = zmat(alpha)
FR[2:4, 2:4] = zmat(alpha)
FR[2:4, 0:2] = zmat(2 - I)
iota = sp.diag(zmat(I), zmat(I))
ok_lenstra, rows = True, []
for k in range(1, 7):
    sL1 = snf_diag(sp.eye(2) - zmat(alpha) ** k)
    sL = snf_diag(sp.eye(4) - FL ** k)
    sR = snf_diag(sp.eye(4) - FR ** k)
    gE2 = sorted(grp[k][3])
    ok_lenstra &= (sL1 == sorted([v for v in gE2 if v != 1]))
    rows.append((k, gE2, sL, sR))
check("B4 E'(F_{5^k}) = Z[i]/(1 - alpha^k) as groups (Lenstra, quoted), k = 1..6: the Deligne module of E' is Z[i] with F = alpha",
      ok_lenstra, "; ".join(f"k={k}: E' {g}" for k, g, _, _ in rows))
diff = [k for k, g, sL, sR in rows if sL != sR]
check("B5 E' x E'' (in the isogeny class of the chi + chibar part, with the same Z[iota]-action) has groups (Z[i]/(1 - alpha^k))^2 = L/(1 - F^k)L; "
      "the companion lattice gives R/(1 - F^k)R, a different group for every k = 1..6 (same order)",
      all(sorted([v for v in g + g if v != 1]) == sL for k, g, sL, sR in rows)
      and diff == [1, 2, 3, 4, 5, 6]
      and all(sp.prod(sL) == sp.prod(sR) for k, g, sL, sR in rows),
      "; ".join(f"k={k}: L {sL}, R {sR}" for k, g, sL, sR in rows[:3]))
ssg = eval(ss.split("|")[1])
check("B6 genus one, the same phenomenon: y^2 = x^3 + 1 over F_25 is supersingular with P = (x + 5)^2 (a = -10); its group is "
      "Z/6 x Z/6 = Z^2/(1 + 5)Z^2 (F = -5 I, semisimple), not Z/36 = Z^2/(1 - C)Z^2 for the companion C of (x + 5)^2",
      sorted(ssg) == [6, 6] and int(ss.split("|")[-1]) == 6
      and snf_diag(sp.eye(2) - sp.Matrix([[0, -25], [1, -10]])) == [36],
      f"E(F_25) = {ssg}, #E(F_5) = {ss.split('|')[-1]}")

# ---------------------------------------------------------------- C. the two lattices
V_L = 5 * FL.inv()
V_R = 5 * FR.inv()
check("C1 FV = VF = 5 with V integral on both: V = conj(alpha) I on L; on R, V e0 = conj(alpha) e0 + (2 + i) e1, V e1 = conj(alpha) e1",
      FL * V_L == 5 * sp.eye(4) and FR * V_R == 5 * sp.eye(4) and all(v.is_integer for v in V_L) and all(v.is_integer for v in V_R)
      and V_R[2:4, 0:2] == zmat(2 + I))
cpL = FL.charpoly(x).as_expr()
cpR = FR.charpoly(x).as_expr()
mL = FL ** 2 + 2 * FL + 5 * sp.eye(4)
mR = FR ** 2 + 2 * FR + 5 * sp.eye(4)
nilR = FR - sp.diag(zmat(alpha), zmat(alpha))
check("C2 same characteristic polynomial (x^2 + 2x + 5)^2 = x^4 + 4x^3 + 14x^2 + 20x + 25 on L and R; F^2 + 2F + 5 = 0 on L (semisimple, F = alpha I), "
      "!= 0 on R; on R, F - alpha is nilpotent and non-zero ((F - alpha)^2 = 0), so L (x) Q and R (x) Q are not isomorphic Q[F]-modules",
      sp.expand(cpL - cpR) == 0 and sp.expand(cpL - (x ** 2 + 2 * x + 5) ** 2) == 0 and mL == sp.zeros(4, 4)
      and mR != sp.zeros(4, 4) and nilR != sp.zeros(4, 4) and nilR ** 2 == sp.zeros(4, 4) and mR.rank() == 2)
# index of Z[i][F] in R: Z[i][F] has Z[i]-basis 1, F = alpha e0 + (2 - i) e1
B = sp.zeros(4, 4)
B[0:2, 0:2] = sp.eye(2)
B[0:2, 2:4] = zmat(alpha)
B[2:4, 2:4] = zmat(2 - I)
check("C3 R = Z[i] + Z[i] (F - alpha)/(2 - i) is the review's R: closed under F, V, i, and [R : Z[i][F]] = |N(2 - i)| = 5",
      abs(B.det()) == 5 and FR * iota == iota * FR and V_R * iota == iota * V_R)

omega_blk = sp.Matrix([[0, -1], [1, 0]])                   # -Im(conj(x) y) on Z[i]


def omega_H(H):
    """omega_H(x, y) = -Im(x^dagger H y) on Z[i]^2, as a 4x4 matrix in the basis 1, i, e, i e (H Hermitian, 2x2)."""
    M = sp.zeros(4, 4)
    for a in range(2):
        for b in range(2):
            h = sp.expand(H[a, b])
            # -Im(conj(x_a) h y_b): conj(x_a) h y_b = x_a^T [[1,0],[0,-1]]... use the real form: -Im(conj(x) h y) = x^T (omega_blk * zmat(h)) y
            M[2 * a:2 * a + 2, 2 * b:2 * b + 2] = omega_blk * zmat(h)
    return M


om = omega_H(sp.eye(2))
check("C4 on L, omega(x, y) = -Im(x^dagger y): alternating, integral, det 1 (principal), F^T omega F = 5 omega, iota^T omega iota = omega",
      om.T == -om and om.det() == 1 and FL.T * om * FL == 5 * om and iota.T * om * iota == om)
# ff-dirichlet's recipe Omega_+(x, y) = Tr(x sigma(y)/(V - F)) on each copy of K = Q(i) (sigma = complex conjugation)
def tr_form(fun):
    basis = [1, I]
    M = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            xa = [0, 0]; yb = [0, 0]
            xa[a // 2] = basis[a % 2]; yb[b // 2] = basis[b % 2]
            M[a, b] = sp.nsimplify(sp.expand(sum(2 * sp.re(sp.expand(fun(xa[c], yb[c]))) for c in range(2))))
    return M


Omp = tr_form(lambda s, t: s * sp.conjugate(t) / (sp.conjugate(alpha) - alpha))
WeilL = (om * (FL - V_L)) / 2
check("C5 ff-dirichlet's recipe Tr(x sigma(y)/(V - F)), applied copy by copy, gives Omega_+ = omega/2; its Weil form (1/2)Tr(x sigma y) "
      "is the Euclidean form I_4 (positive definite), and the Weil form of omega itself is (1/2) omega (F - V) = 2 I_4 = |Im alpha| I_4",
      Omp == om / 2 and WeilL == 2 * sp.eye(4) and tr_form(lambda s, t: s * sp.conjugate(t) / 2) == sp.eye(4))
J = sp.diag(zmat(-I), zmat(-I))
Jform = (FL - V_L) * ((4 * 5 * sp.eye(4) - (FL + V_L) ** 2) ** -1).applyfunc(sp.sqrt)
GJ = om * J
check("C6 the vacuum on L: J = multiplication by -i (= -iota): J^2 = -1, JF = FJ, J iota = iota J, omega(Jx, Jy) = omega, "
      "G_J = omega(., J .) = I_4 > 0; it equals zn-flux's (F - V)(4q - (F + V)^2)^(-1/2); Weil form = |Im alpha| G_J",
      J * J == -sp.eye(4) and J * FL == FL * J and J * iota == iota * J and J.T * om * J == om and GJ == sp.eye(4)
      and Jform == J and WeilL == 2 * GJ)
# the cone of compatible forms on L: all alternating Omega with F^T Omega F = 5 Omega
def compatible(Fm):
    a = sp.symbols("a0:6")
    Om = sp.zeros(4, 4)
    idx = 0
    for i_ in range(4):
        for j_ in range(i_ + 1, 4):
            Om[i_, j_] = a[idx]; Om[j_, i_] = -a[idx]; idx += 1
    eqs = list(Fm.T * Om * Fm - 5 * Om)
    sol = sp.linsolve(eqs, a)
    (s,) = sol
    free = sorted(set().union(*[sp.sympify(v).free_symbols for v in s]), key=str)
    return Om.subs(dict(zip(a, s))), free


OmL, freeL = compatible(FL)
OmR, freeR = compatible(FR)


def inertia(S):
    ev = np.linalg.eigvalsh(np.array(S.evalf(), dtype=float))
    return (int((ev > 1e-9).sum()), int((ev < -1e-9).sum()), int((abs(ev) <= 1e-9).sum()))


Hind = sp.diag(1, -1)
omI = omega_H(Hind)
WI = (omI * (FL - V_L)) / 2
JI = sp.diag(zmat(-I), zmat(I))
Jstd = sp.Matrix([[0, 1], [-1, 0]])
omS = omega_H(-I * Jstd)                                    # Tr-type form x^dagger J y with the standard alternating J on Z[i]^2
WS = (omS * (FL - V_L)) / 2
check("C7 on L the compatible alternating forms are omega_H = -Im(x^dagger H y), H Hermitian (a 4-dimensional space, all iota-invariant); "
      "Weil form = 2 Re(x^dagger H y): definite iff H is definite. H = diag(1, -1): non-degenerate, Weil form of inertia (2, 2), "
      "and still a vacuum (J = -i (+) i): the CM-type precision of lane E. The brief's Tr(x^dagger J_std y) is H = -i J_std, also inertia (2, 2)",
      len(freeL) == 4 and all((iota.T * OmL * iota - OmL).expand() == sp.zeros(4, 4) for _ in [0])
      and inertia(WI) == (2, 2, 0) and JI * JI == -sp.eye(4) and JI * FL == FL * JI and JI.T * omI * JI == omI
      and inertia(omI * JI) == (4, 0, 0) and inertia(WS) == (2, 2, 0) and omS.det() != 0,
      f"dim = {len(freeL)}; inertia: H = I {inertia(WeilL)}, H = diag(1,-1) {inertia(WI)}, H = -i J_std {inertia(WS)}")

# R: the trace form, Omega_+, the compatible forms
# E = Q(i)[n]/(n^2); elements (a, b) = a + b n; sigma(n) = V - conj(alpha) = ((3 + 4i)/5) n
uR = sp.Rational(3, 5) + sp.Rational(4, 5) * I


def emul(p, r):
    return (sp.expand(p[0] * r[0]), sp.expand(p[0] * r[1] + p[1] * r[0]))


def esig(p):
    return (sp.conjugate(p[0]), sp.expand(sp.conjugate(p[1]) * uR))


def einv(p):
    return (1 / p[0], sp.expand(-p[1] / p[0] ** 2))


def etr(p):
    return sp.nsimplify(sp.expand(4 * sp.re(sp.expand(p[0]))))


Rb = [(1, 0), (I, 0), (0, 1 / (2 - I)), (0, I / (2 - I))]
Rb = [(sp.expand(a), sp.expand(b)) for a, b in Rb]
VmF = (sp.conjugate(alpha) - alpha, uR - 1)                # V - F = (conj(alpha) - alpha) + (u - 1) n
TrR = sp.Matrix(4, 4, lambda a, b: etr(emul(Rb[a], esig(Rb[b]))))
OmpR = sp.Matrix(4, 4, lambda a, b: etr(emul(emul(Rb[a], esig(Rb[b])), einv(VmF))))
check("C8 on R (review J7 reproduced): the trace form Tr(x sigma y) has rank 2 of 4 (the nilradical is isotropic); "
      "ff-dirichlet's Omega_+ is alternating, F^T Omega_+ F = 5 Omega_+, and degenerate (rank 2)",
      TrR.rank() == 2 and OmpR.T == -OmpR and FR.T * OmpR * FR == 5 * OmpR and OmpR.rank() == 2,
      f"Tr form = {TrR.tolist()}")
okR, infs = True, []
random.seed(1)
for _ in range(6):
    vals = {s: random.randint(-9, 9) for s in freeR}
    Om = OmR.subs(vals)
    if Om.det() == 0:
        continue
    W = (Om * (FR - V_R)) / 2
    okR &= (W.T == W) and inertia(W) == (2, 2, 0)
    infs.append(inertia(W))
check(f"C9 on R the compatible alternating forms form a {len(freeR)}-dimensional space whose generic member is NON-degenerate, "
      "but every non-degenerate one tried has Weil form of inertia (2, 2): never definite (proved: a definite Weil form makes F/sqrt5 orthogonal, hence semisimple)",
      len(freeR) == 2 and okR and len(infs) >= 4, f"{len(infs)} random members, inertia {set(infs)}")
S = np.array((FR / sp.sqrt(5)).evalf(), dtype=complex)
norms = [np.linalg.norm(np.linalg.matrix_power(S, k), 2) for k in (10, 100, 1000)]
SL = np.array((FL / sp.sqrt(5)).evalf(), dtype=complex)
normsL = [np.linalg.norm(np.linalg.matrix_power(SL, k), 2) for k in (10, 100, 1000)]
check("C10 no vacuum on R: ||(F/sqrt5)^k|| grows linearly in k on R (a Jordan block on the unit circle; no compact closure, so no invariant J), "
      "while on L it is 1 for every k",
      norms[2] > 50 * norms[0] / 10 and all(abs(v - 1) < 1e-9 for v in normsL),
      "R: " + ", ".join(f"{v:.1f}" for v in norms) + " at k = 10, 100, 1000")

# ---------------------------------------------------------------- D. the Connes citation
src = "/home/user/riemann-channel/refs/src/math/9811068/main.tex"
ok = False
if os.path.exists(src):
    with open(src, encoding="utf-8", errors="replace") as fh:
        lines = fh.read().splitlines()
    blk = " ".join(lines[948:952])
    thm = " ".join(lines[881:885])
    ok = ("is {\\it not} semisimple" in blk and "Jordan form" in blk and "multiplicity of $\\rho$ in ${\\rm Sp} \\, D$" in thm)
check("D1 Connes 1998, math/9811068:main.tex:949-952: 'When the zeros of L have multiplicity and delta is large enough the operator D is "
      "not semisimple and has a non trivial Jordan form'; Theorem 1 multiplicity clause at :882-885", ok)

print(f"\n{npass} of {npass + nfail} pass")
