#!/usr/bin/env python3
"""Checks for 'The CM lift' (notes/adelic-gkp/cm-lift.md), lane C, 2026-10-06.

K = Q(sqrt(-7)), O_K = Z[w], w = (1 + sqrt(-7))/2, w^2 = w - 2. Unit group {+1, -1}. h_K = 1.
E-mode step of the notebook: M = [[0, -1], [2, -1]], characteristic polynomial x^2 + x + 2, a_2 = -1.
Curves: 49a1 (j = -3375, conductor 49, a_2 = +1) and its quadratic twist by -3, 441d1 (a_2 = -1).
Hecke character of 49a1: psi((alpha)) = eps(alpha) * alpha, eps(alpha) = Legendre symbol of (alpha mod sqrt(-7)) mod 7.
For 441d1: psi' = psi * (chi_{-3} o N).
Analytic normalisation: s = 1 + iE in PARI's (motivic) variable is s' = 1/2 + iE; zeros are written 1 + i*gamma.
Needs PARI/GP (/usr/bin/gp) with elldata; run time well under a minute.
"""
import os
import subprocess
import numpy as np
import mpmath as mp
from scipy.special import digamma

HERE = os.path.dirname(os.path.abspath(__file__))
npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


def gp(script):
    r = subprocess.run(["gp", "-q", "-f"], input="\\p 38\ndefault(colors,\"no\");\n" + script + "\nquit\n",
                       capture_output=True, text=True, timeout=600)
    out = {}
    for line in r.stdout.splitlines():
        if line.startswith("@"):
            k, v = line[1:].split(" ", 1)
            out[k] = v.strip()
    return out


def pnum(s):
    """parse a PARI real such as '6.3 E-39' or '0.E-58'"""
    return mp.mpf(s.replace(" ", "").replace("E", "e"))


def vec(s):
    s = s.strip().strip("[]")
    return [pnum(x) for x in s.split(",")] if s else []


def leg7(x):
    r = x % 7
    if r == 0:
        return 0
    return 1 if r in (1, 2, 4) else -1


def chi_m3(p):           # Kronecker (-3/p) = (p/3) for p != 3
    r = p % 3
    return 0 if r == 0 else (1 if r == 1 else -1)


def sieve(N):
    s = np.ones(N + 1, bool)
    s[:2] = False
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return s


# ---------------------------------------------------------------------------------------------
print("== A  which curve: the E mode, 49a1 and its twists (PARI)")
A = gp(r"""
E=ellinit("49a1"); print("@j ",E.j); print("@N ",ellglobalred(E)[1]); print("@eps ",ellrootno(E));
print("@rk ",ellanalyticrank(E)[1]); print("@L1 ",lfun(E,1));
E2=ellinit("441d1"); print("@j2 ",E2.j); print("@N2 ",ellglobalred(E2)[1]); print("@eps2 ",ellrootno(E2));
print("@rk2 ",ellanalyticrank(E2)[1]); print("@L1d2 ",lfun(E2,1,1)); print("@L1v2 ",abs(lfun(E2,1)));
print("@tw3 ",ellidentify(ellinit(ellminimalmodel(ellinit(elltwist(E,-3)))))[1][1]);
print("@tw21 ",ellidentify(ellinit(ellminimalmodel(ellinit(elltwist(E,21)))))[1][1]);
T7=ellinit(ellminimalmodel(ellinit(elltwist(E,-7)))); print("@tw7 ",ellidentify(T7)[1][1]);
T5=ellinit(ellminimalmodel(ellinit(elltwist(E,5)))); print("@tw5N ",ellglobalred(T5)[1]); print("@tw5a2 ",ellap(T5,2));
print("@tw7same ",vector(168,i,ellap(T7,prime(i)))==vector(168,i,ellap(E,prime(i))));
a=ffgen(2,'a); Em=ellinit([1,0,0,0,1],a); print("@cardEmode ",ellcard(Em));
print("@red49 ",ellinit([1,-1,0,-2,-1],2)[1..5]); print("@a2red49 ",ellap(ellinit([1,-1,0,-2,-1],2)));
R=ellinit([1,-1,1,-20,46],2); print("@redEmode ",[R.j, ellap(R), ellcard(R)]);
P=primes([2,10000]); print("@P ",P); print("@ap1 ",vector(#P,i,ellap(E,P[i]))); print("@ap2 ",vector(#P,i,ellap(E2,P[i])));
print("@an ",ellan(E,3000));
""")
check("A1 49a1: j = -3375 (CM by Q(sqrt(-7))), conductor 49, root number +1, analytic rank 0",
      A["j"] == "-3375" and A["N"] == "49" and A["eps"] == "1" and A["rk"] == "0", f"L(E,1) = {mp.nstr(pnum(A['L1']), 15)}")
check("A2 the E mode y^2 + xy = x^3 + 1 over F_2: 4 points, so a_2 = 3 - 4 = -1 and the Frobenius polynomial is x^2 + x + 2",
      A["cardEmode"] == "4")
M = np.array([[0, -1], [2, -1]])
check("A2 the notebook's step M = [[0,-1],[2,-1]] has trace -1, det 2 (same polynomial)", np.trace(M) == -1 and round(np.linalg.det(M)) == 2)
check("A3 49a1 mod 2 is y^2 + xy = x^3 + x^2 + 1 with a_2 = +1: the quadratic twist over F_2 of the E mode (step -M)",
      A["red49"].replace(" ", "") == "[1,1,0,0,1]" and A["a2red49"] == "1", A["red49"])
check("A4 the twist of 49a1 by -3 (equivalently by 21) is 441d1", A["tw3"] == "441d1" and A["tw21"].startswith("441d"), "twist by 21 = " + A["tw21"] + " (same isogeny class)")
check("A4 441d1: j = -3375, conductor 441 = 3^2 7^2, root number -1, analytic rank 1",
      A["j2"] == "-3375" and A["N2"] == "441" and A["eps2"] == "-1" and A["rk2"] == "1",
      f"|L(1)| = {mp.nstr(pnum(A['L1v2']), 3)}, L'(1) = {mp.nstr(pnum(A['L1d2']), 15)}")
check("A4 441d1 has good reduction at 2 with j = 1, a_2 = -1, 4 points: over F_2 the only ordinary curve with j = 1 and a_2 = -1 is the E mode",
      A["redEmode"].replace(" ", "") == "[1,-1,4]", A["redEmode"])
check("A4 the twist by 5 also has a_2 = -1 but conductor 1225 > 441", A["tw5N"] == "1225" and A["tw5a2"] == "-1")
check("A4 the twist by the CM discriminant -7 has the same a_p (p < 1000)", A["tw7same"] == "1", "twist = " + A["tw7"])

P = [int(x) for x in A["P"].strip("[]").split(",")]
ap1 = [int(x) for x in A["ap1"].strip("[]").split(",")]
ap2 = [int(x) for x in A["ap2"].strip("[]").split(",")]


def rep(p):
    """x, y > 0 with x^2 + 7 y^2 = 4p (p split), else None"""
    y = 1
    while 7 * y * y < 4 * p:
        r = 4 * p - 7 * y * y
        x = int(round(r ** 0.5))
        if x * x == r and x > 0:
            return x, y
        y += 1
    return None


def psi(p, twist=False):
    """psi(frak p) for a split p, as (a, b) with alpha = a + b w, plus x, y. Sign: eps(alpha) alpha with eps = Legendre mod sqrt(-7)."""
    x, y = rep(p)
    s = leg7(x)                        # alpha = (x + y sqrt(-7))/2 = x/2 mod sqrt(-7); (2|7) = 1
    if twist:
        s *= chi_m3(p)
    a, b = s * (x - y) // 2, s * y   # (x + y sqrt-7)/2 = (x - y)/2 + y w
    return a, b, s * x, y


def ap_hecke(p, twist=False):
    if p == 7 or (twist and p == 3):
        return 0
    if leg7(p) == 1:                  # split ((-7/p) = (p/7))
        return psi(p, twist)[2]
    return 0                          # inert


bad1 = [p for p, a in zip(P, ap1) if ap_hecke(p) != a]
bad2 = [p for p, a in zip(P, ap2) if ap_hecke(p, True) != a]
check("A5 L(49a1) = L(psi): a_p = (x|7) x from 4p = x^2 + 7y^2 (split), 0 (inert, p = 7), all p < 10^4", not bad1, f"{len(P)} primes")
check("A5 L(441d1) = L(psi chi_{-3}oN): a_p = chi_{-3}(p)(x|7) x, all p < 10^4", not bad2, f"{len(P)} primes")

print("      split primes p <= 60: psi(p) = generator of the prime above p that is a square mod sqrt(-7)")
rows = []
for p in P:
    if p > 60:
        break
    if p != 7 and leg7(p) == 1:
        a, b, ax, y = psi(p)
        al = complex(a + b * 0.5, b * 7 ** 0.5 / 2)
        rows.append((p, a, b, ax, al))
        print(f"      p = {p:2d}: psi = ({ax:+d} {b:+d}*sqrt(-7))/2 = {a:+d} {b:+d}w,  N = {a*a + a*b + 2*b*b},"
              f" a_p(49a1) = {ax:+d}, a_p(441d1) = {ap_hecke(p, True):+d}, arg/pi = {np.angle(al)/np.pi:+.4f}")
check("A6 each psi(p) has norm p, trace a_p, and is a square mod sqrt(-7)",
      all(a * a + a * b + 2 * b * b == p and 2 * a + b == ax and leg7(2 * a + b) == 1 for p, a, b, ax, al in rows),
      f"{len(rows)} split primes <= 60: " + ", ".join(str(r[0]) for r in rows))
check("A6 eps(-1) = (-1|7) = -1, so eps(alpha) alpha = eps(-alpha)(-alpha): psi is well defined on ideals", leg7(-1) == -1)

# theta series of the Hecke character: (1/2) sum_alpha eps(alpha) alpha q^{N alpha}
an = [int(x) for x in A["an"].strip("[]").split(",")]
NM = len(an)
th = np.zeros(NM + 1)
th_even = np.zeros(NM + 1, complex)
R = int(2 * (NM ** 0.5)) + 4
for a in range(-R, R + 1):
    for b in range(-R, R + 1):
        n = a * a + a * b + 2 * b * b
        if 0 < n <= NM:
            alpha = complex(a + 0.5 * b, b * 7 ** 0.5 / 2)
            th[n] += 0.5 * leg7(2 * a + b) * alpha.real      # alpha mod sqrt(-7) = a + b/2 = (2a + b)/2
            th_even[n] += alpha
check("A7 theta series (1/2) sum_{alpha in O_K} eps(alpha) alpha q^{N(alpha)} = q-expansion of 49a1 (n <= 3000)",
      np.max(np.abs(th[1:] - np.array(an))) < 1e-9)
check("A7 without the 7-adic charge the overlap vanishes identically: sum_alpha alpha q^{N(alpha)} = 0",
      np.max(np.abs(th_even)) < 1e-9, "the angular-momentum-1 state is odd under the global unit -1")

# ---------------------------------------------------------------------------------------------
print("== B  one lattice, one vacuum: the split steps on O_K")
Bm = np.array([[1.0, 0.5], [0.0, 7 ** 0.5 / 2]])      # columns: images of 1 and w in R^2 = C
Jc = np.array([[0.0, -1.0], [1.0, 0.0]])
JK = np.linalg.inv(Bm) @ Jc @ Bm                          # multiplication by i, in the basis {1, w}
Om = np.array([[0.0, 1.0], [-1.0, 0.0]])


def mult(a, b):
    return np.array([[a, -2 * b], [b, a + b]])


g = Om @ JK
check("B1 J_K (multiplication by i on C = K (x) R) is a complex structure on the lattice phase space: J^2 = -1, J^T Omega J = Omega",
      np.allclose(JK @ JK, -np.eye(2)) and np.allclose(JK.T @ Om @ JK, Om))
check("B1 J_K is a vacuum: the metric G = Omega J_K is symmetric positive definite (orientation: Omega(1, w) = +1)",
      np.allclose(g, g.T) and np.all(np.linalg.eigvalsh(g) > 0), f"eigenvalues of Omega J_K: {np.round(np.linalg.eigvalsh(g), 4)}")
Ms = [mult(a, b) for p, a, b, ax, al in rows]
ok = all(np.array_equal(M_.T @ Om @ M_, p * Om) for (p, *_), M_ in zip(rows, Ms))
check("B2 each split step mult(psi(p)) is an integer matrix with M^T Omega M = p Omega", ok)
ok = all(np.allclose(M_ @ JK, JK @ M_) for M_ in Ms)
ok2 = all(np.allclose((M_ / np.sqrt(p)).T @ g @ (M_ / np.sqrt(p)), g) for (p, *_), M_ in zip(rows, Ms))
check("B2 every split step commutes with the same J_K, and M/sqrt(p) is an isometry of the same vacuum metric",
      ok and ok2, "local RH at every split p from one vacuum")
ok = all(np.array_equal(X @ Y, Y @ X) for X in Ms for Y in Ms)
check("B2 the split steps commute pairwise (O_K is commutative)", ok)
mu = mult(-1, 1)                         # mu = (-1 + sqrt(-7))/2 = w - 1
Pfound = None
rng = range(-3, 4)
for p11 in rng:
    for p12 in rng:
        for p21 in rng:
            for p22 in rng:
                Pm = np.array([[p11, p12], [p21, p22]])
                d = p11 * p22 - p12 * p21
                if d in (1, -1) and np.array_equal(Pm @ mu, M @ Pm):
                    Pfound = Pm
                    break
            if Pfound is not None:
                break
        if Pfound is not None:
            break
    if Pfound is not None:
        break
check("B3 the notebook's E mode M is GL_2(Z)-conjugate to multiplication by mu = (-1+sqrt(-7))/2 on O_K",
      Pfound is not None, f"P = {Pfound.tolist() if Pfound is not None else None}, P mu P^-1 = M")
a2, b2 = psi(2)[:2]
check("B3 for 49a1, psi(p_2) = (1 + sqrt(-7))/2 = -mu-bar: the step at 2 is -M up to conjugation (a half turn of the E mode)",
      (a2, b2) == (0, 1) and np.trace(mult(a2, b2)) == -np.trace(M))
a2t, b2t = psi(2, True)[:2]
check("B3 for 441d1, psi'(p_2) = -(1 + sqrt(-7))/2 = mu-bar: the step at 2 has the E-mode polynomial x^2 + x + 2",
      np.trace(mult(a2t, b2t)) == -1 and round(np.linalg.det(mult(a2t, b2t))) == 2)
inert = [p for p in P if p <= 60 and p != 7 and leg7(p) == -1]
noK = all(not any(2 * a + b == 0 and a * a + a * b + 2 * b * b == p for a in range(-10, 11) for b in range(-20, 21)) for p in inert)
check("B4 inert p <= 60: no alpha in O_K with trace 0 and norm p, so the Q-Frobenius x^2 + p has no K-linear step on O_K",
      noK, "inert: " + ", ".join(map(str, inert)))
check("B4 inert p: psi((p)) = (p|7) p = -p, the K-step is -p (normalised: the half turn -1, which commutes with J_K)",
      all(leg7(p) * p == -p for p in inert))
ok = True
for p in inert:
    S = np.array([[0, -1], [p, 0]]) / np.sqrt(p)
    ok &= np.allclose(S @ S, -np.eye(2)) and not np.allclose(S @ JK, JK @ S)
check("B4 inert p: the step [[0,-1],[p,0]] normalised is a quarter turn (S^2 = -1); its own vacuum is S, not J_K", ok)
check("B4 inert p and p = 7 have a_p = 0 for 49a1 (p < 10^4); p = 3 is bad for 441d1",
      all(a == 0 for p, a in zip(P, ap1) if leg7(p) != 1) and ap2[1] == 0)
a7 = mult(-1, 2)                      # sqrt(-7) = 2w - 1
check("B5 the ramified prime: sqrt(-7) = 2w - 1 is an integral step of norm 7 commuting with J_K (a quarter turn times sqrt 7)",
      round(np.linalg.det(a7)) == 7 and np.trace(a7) == 0 and np.allclose(a7 @ JK, JK @ a7))
check("B5 ... but eps(sqrt(-7)) = 0: psi is ramified at (sqrt(-7)) and the Euler factor at 7 is 1 (a_7 = 0)",
      leg7(2 * (-1) + 2) == 0 and ap1[P.index(7)] == 0)

# ---------------------------------------------------------------------------------------------
print("== C  functional equation; Hecke/Tate: L is the Mellin transform of the theta overlap")
C = gp(r"""
E=ellinit("49a1"); E2=ellinit("441d1");
print("@feq1 ",lfuncheckfeq(E)); print("@feq2 ",lfuncheckfeq(E2));
s=0.3+5*I; print("@r1 ",abs(lfunlambda(E,s)-ellrootno(E)*lfunlambda(E,2-s))/abs(lfunlambda(E,s)));
s=1.7-3*I; print("@r2 ",abs(lfunlambda(E2,s)-ellrootno(E2)*lfunlambda(E2,2-s))/abs(lfunlambda(E2,s)));
print("@L1 ",lfun(E,1)); z=lfun(E,1.3+2*I); print("@Lsr ",real(z)); print("@Lsi ",imag(z));
z1=lfunzeros(E,70); z2=lfunzeros(E2,70); print("@z1 ",z1); print("@z2 ",z2);
print("@chk1 ",vector(20,k,abs(lfun(E,1+I*z1[k])))); print("@chk2 ",vector(20,k,abs(lfun(E2,1+I*z2[k+1]))));
print("@nb1 ",vector(20,k,abs(lfun(E,1+I*(z1[k]+0.1))))); 
""")
check("C1 lfuncheckfeq: functional equation holds to 2^-100 or better (49a1, 441d1)",
      int(C["feq1"]) <= -100 and int(C["feq2"]) <= -100, f"{C['feq1']} and {C['feq2']} bits")
check("C1 Lambda(s) = eps Lambda(2 - s) at s = 0.3 + 5i (49a1, eps = +1) and 1.7 - 3i (441d1, eps = -1)",
      pnum(C["r1"]) < 1e-30 and pnum(C["r2"]) < 1e-30, f"relative errors {mp.nstr(pnum(C['r1']), 2)}, {mp.nstr(pnum(C['r2']), 2)}")
an_arr = np.array(an, float)
nn = np.arange(1, NM + 1)
mp.mp.dps = 20
Nc = 49
fiy = lambda y: mp.fsum(mp.mpf(an[k]) * mp.exp(-2 * mp.pi * (k + 1) * y) for k in range(min(NM, int(12 / float(y)) + 10)))
errs = []
for y in [mp.mpf("0.08"), mp.mpf("0.12")]:
    lhs = fiy(1 / (Nc * y))
    rhs = Nc * y ** 2 * fiy(y)
    errs.append(abs(lhs - rhs) / abs(rhs))
check("C2 theta overlap: f(i/(49y)) = +49 y^2 f(iy) (the Fourier/S-gate symmetry of code + charged vacuum), y = 0.08, 0.12",
      max(errs) < 1e-15, f"relative errors {mp.nstr(max(errs), 2)}")
def Lam_int(s):
    y0 = mp.mpf(1) / 7
    i1 = mp.quad(lambda y: fiy(y) * y ** (s - 1), [y0, 1, 3, 8])
    i2 = mp.quad(lambda y: fiy(y) * y ** (1 - s), [y0, 1, 3, 8])
    return mp.mpf(Nc) ** (s / 2) * (i1 + mp.mpf(Nc) ** (1 - s) * i2)
for s, Lp in [(mp.mpf(1), pnum(C["L1"])), (mp.mpc(1.3, 2), mp.mpc(pnum(C["Lsr"]), pnum(C["Lsi"])))]:
    lam_pari = mp.mpf(Nc) ** (s / 2) * 2 * (2 * mp.pi) ** (-s) * mp.gamma(s) * Lp
    lam_th = 2 * Lam_int(s)
    check(f"C3 Mellin transform of the theta overlap = Gamma_C(s) N^(s/2) L(E,s) at s = {mp.nstr(s, 3)}",
          abs(lam_th - lam_pari) / abs(lam_pari) < 1e-12, f"{mp.nstr(lam_th, 14)} vs PARI {mp.nstr(lam_pari, 14)}")
mp.mp.dps = 15

z1 = np.array([float(x) for x in vec(C["z1"])])
z2 = np.array([float(x) for x in vec(C["z2"])])
print("      first 20 zeros 1 + i*gamma of L(49a1, s) (motivic s; 1/2 + i*gamma in the analytic normalisation):")
print("      " + ", ".join(f"{g:.6f}" for g in z1[:20]))
print("      first 20 nonzero zeros of L(441d1, s), plus a simple zero at gamma = 0:")
print("      " + ", ".join(f"{g:.6f}" for g in z2[1:21]))
c1 = [float(x) for x in vec(C["chk1"])]
c2 = [float(x) for x in vec(C["chk2"])]
nb = [float(x) for x in vec(C["nb1"])]
check("C4 |L(1 + i gamma)| < 1e-25 at the first 20 zeros of each curve (vs >= 1e-3 at gamma + 0.1 for 49a1)",
      max(c1) < 1e-25 and max(c2) < 1e-25 and min(nb) > 1e-3, f"max {max(c1 + c2):.1e}; min off-zero {min(nb):.1e}")
check("C4 zero counts below T = 70 agree with N(T) ~ (T/pi) log(sqrt(N) T / (2 pi e)) to within 2",
      abs(len(z1) - 70 / np.pi * np.log(7 * 70 / (2 * np.pi * np.e))) < 2 and abs(len(z2) - 1 - 70 / np.pi * np.log(21 * 70 / (2 * np.pi * np.e))) < 2,
      f"49a1: {len(z1)} zeros, 441d1: {len(z2)} (incl. gamma = 0)")
check("C4 441d1 has a zero at the centre (gamma = 0), as root number -1 forces", z2[0] == 0.0 and z1[0] > 3)

# ---------------------------------------------------------------------------------------------
print("== D  explicit formula in echo form: zeros side = place-by-place side (no zero-mode term)")
NMAX = 2_000_000
isp = sieve(NMAX)
# split primes from the norm form: x^2 + 7 y^2 = 4p, x, y > 0
ys = np.arange(1, int((4 * NMAX / 7) ** 0.5) + 2)
xs = np.arange(1, int((4 * NMAX) ** 0.5) + 2)
X, Y = np.meshgrid(xs, ys, indexing="ij")
V = X * X + 7 * Y * Y
msk = (V % 4 == 0) & (V // 4 <= NMAX)
V, X, Y = V[msk] // 4, X[msk], Y[msk]
msk = isp[V] & (V != 7)
SP, SX = V[msk], X[msk]
check("D0 each split prime p < 2*10^6 has exactly one representation 4p = x^2 + 7y^2 with x, y > 0 (h_K = 1, units +-1)",
      len(np.unique(SP)) == len(SP) == int(sum(1 for p in np.nonzero(isp)[0] if p != 7 and leg7(int(p)) == 1)), f"{len(SP)} split primes")
eps_sp = np.array([leg7(int(x)) for x in SX])
theta_sp = np.arccos(np.clip(eps_sp * SX / (2 * np.sqrt(SP)), -1, 1))          # psi(p)/sqrt(p) = e^{i theta}
chi_sp = np.array([chi_m3(int(p)) for p in SP])
allp = np.nonzero(isp)[0]
inert_p = np.array([p for p in allp if p != 7 and leg7(int(p)) == -1])


def kicks(twist=False):
    """list of (log n, Lambda_L(n)/sqrt(n)) for n = p^k <= NMAX"""
    L, W = [], []
    for k in range(1, 22):
        # split: Lambda(p^k) = 2 cos(k theta) log p (times chi(p)^k for the twist)
        m = SP ** k <= NMAX if k < 3 else np.array([float(p) ** k <= NMAX for p in SP])
        if not m.any():
            break
        c = 2 * np.cos(k * theta_sp[m]) * (chi_sp[m] ** k if twist else 1)
        L.append(k * np.log(SP[m].astype(float)))
        W.append(c * np.log(SP[m].astype(float)) / SP[m].astype(float) ** (k / 2))
        # inert: (i^k + (-i)^k) log p; p = 3 is bad for the twist
        mi = np.array([float(p) ** k <= NMAX and not (twist and p == 3) for p in inert_p])
        if k % 2 == 0 and mi.any():
            c = 2 * (-1) ** (k // 2)
            L.append(k * np.log(inert_p[mi].astype(float)))
            W.append(c * np.log(inert_p[mi].astype(float)) / inert_p[mi].astype(float) ** (k / 2))
    return np.concatenate(L), np.concatenate(W)


def trapz(y, x):
    return np.sum((y[1:] + y[:-1]) * np.diff(x)) / 2


def G(E, E0, tau):
    return 2 * np.pi * tau ** 2 * np.exp(-tau ** 2 * (E - E0) ** 2)


def g_time(u, E0, tau):
    return tau * np.sqrt(np.pi) * np.exp(-1j * E0 * u) * np.exp(-u ** 2 / (4 * tau ** 2))


def all_zeros(z):
    pos = z[z > 0]
    return np.concatenate([-pos[::-1], z[z == 0], pos])


def echo_zeros(t, E0, tau, gam):
    t = np.atleast_1d(t).astype(float)
    return (G(gam[:, None], E0, tau) * np.exp(1j * gam[:, None] * t[None, :])).sum(0)


def arch_density(E, Ncond):
    """(1/2pi)[log N - 2 log 2pi + 2 Re psi(1 + iE)]: Gamma_C(s'+1/2) and the conductor"""
    return (np.log(Ncond) - 2 * np.log(2 * np.pi) + 2 * digamma(1 + 1j * E).real) / (2 * np.pi)


def echo_places(t, E0, tau, KL, KW, Ncond, parts=False):
    t = np.atleast_1d(t).astype(float)
    w = KW[:, None]
    ln = KL[:, None]
    prime = -(w * (g_time(ln - t[None, :], E0, tau) + g_time(-ln - t[None, :], E0, tau))).sum(0)
    E = np.linspace(E0 - 14 / tau, E0 + 14 / tau, 40001)
    arch = np.array([trapz(G(E, E0, tau) * np.exp(1j * E * tt) * arch_density(E, Ncond), E) for tt in t])
    return (prime, arch) if parts else prime + arch


KL1, KW1 = kicks(False)
KL2, KW2 = kicks(True)
Z1, Z2 = all_zeros(z1), all_zeros(z2)
results = []
for lab, Zs, KL, KW, Nc_, E0, tau, ts in [
        ("49a1", Z1, KL1, KW1, 49, 12.0, 0.25, np.array([0.0, 0.3, np.log(2), 1.0, np.log(11), 3.0])),
        ("49a1", Z1, KL1, KW1, 49, 20.0, 1.0, np.array([0.0, 1.0])),
        ("49a1", Z1, KL1, KW1, 49, 2.0, 0.6, np.array([0.0, 0.8])),
        ("441d1", Z2, KL2, KW2, 441, 10.0, 0.25, np.array([0.0, 0.5, np.log(2), 2.0])),
        ("441d1", Z2, KL2, KW2, 441, 1.0, 0.6, np.array([0.0, 0.8]))]:
    cz = echo_zeros(ts, E0, tau, Zs)
    pr, ar = echo_places(ts, E0, tau, KL, KW, Nc_, parts=True)
    err = np.max(np.abs(cz - pr - ar))
    digits = -np.log10(err / abs(cz[0]))
    results.append(digits)
    check(f"D1 {lab}: packet E0 = {E0:g}, tau = {tau:g}, {len(ts)} values of t: zero sum = prime kicks + real place",
          err < 1e-7 * max(1, abs(cz[0])), f"max |diff| = {err:.1e}, C(0) = {cz[0].real:.8f} (primes {pr[0].real:+.6f}, real place {ar[0].real:+.6f}), {digits:.1f} digits")

# ---------------------------------------------------------------------------------------------
print("== E  windowed Weil form (Toeplitz Gram matrix of the echo) from the place side; an off-line pair")


def toeplitz(c):
    n = len(c)
    Mx = np.empty((n, n), complex)
    for j in range(n):
        for k in range(n):
            d = j - k
            Mx[j, k] = c[d] if d >= 0 else np.conj(c[-d])
    return Mx


nG, dT = 14, 0.35
E0w, tauw = 20.0, 0.25
tg = np.arange(nG) * dT
cg = echo_places(tg, E0w, tauw, KL1, KW1, 49)
Gm = toeplitz(cg)
ev = np.linalg.eigvalsh(Gm)
check("E1 49a1: the 14 x 14 Gram matrix [C_h(t_j - t_k)] from the prime side is Hermitian and PSD (E0 = 20, tau = 0.25, step 0.35)",
      np.max(np.abs(Gm - Gm.conj().T)) < 1e-12 and ev.min() > -1e-8, f"eigenvalues in [{ev.min():.2e}, {ev.max():.3f}]")
tf = np.linspace(0, 6, 301)
cf = echo_places(tf, E0w, tauw, KL1, KW1, 49)
check("E1 49a1: echo bound |C_h(t)| <= C_h(0) on [0, 6]", np.max(np.abs(cf)) <= abs(cf[0]) + 1e-9,
      f"max |C(t)|/C(0) for t >= 0.5: {np.max(np.abs(cf[25:])) / abs(cf[0]):.4f}")
cg2 = echo_places(tg, 10.0, 0.25, KL2, KW2, 441)
ev2 = np.linalg.eigvalsh(toeplitz(cg2))
check("E1 441d1: same Gram matrix (E0 = 10) is PSD", ev2.min() > -1e-8, f"eigenvalues in [{ev2.min():.2e}, {ev2.max():.3f}]")
ia = int(np.argmin(np.abs(z1 - 19.9)))
ib = ia + 1
g0, eta = 0.5 * (z1[ia] + z1[ib]), 0.5


def removed(t):
    return sum(G(s * z1[i], E0w, tauw) * np.exp(1j * s * z1[i] * t) for i in (ia, ib) for s in (1, -1))


def weil_pair(t):
    return sum(G(sg * (g0 + s * 1j * eta), E0w, tauw) * np.exp(1j * sg * (g0 + s * 1j * eta) * t) for s in (1, -1) for sg in (1, -1))


def lorentz_pair(t):
    E = np.linspace(E0w - 14 / tauw, E0w + 14 / tauw, 80001)
    Lz = (eta / np.pi) / ((E - g0) ** 2 + eta ** 2)
    return np.array([2 * trapz(G(E, E0w, tauw) * np.exp(1j * E * x) * Lz, E) for x in np.atleast_1d(t)])


base = cg - removed(tg)
evw = np.linalg.eigvalsh(toeplitz(base + weil_pair(tg)))
evl = np.linalg.eigvalsh(toeplitz(base + lorentz_pair(tg)))
check(f"E2 49a1 with gamma = {z1[ia]:.4f}, {z1[ib]:.4f} replaced by {g0:.4f} +- {eta}i, Weil form: Gram matrix has a negative eigenvalue",
      evw.min() < -1e-3, f"min eigenvalue {evw.min():.4f} (true list: {ev.min():.1e})")
check("E2 same pair, Lorentzian (width eta) form: Gram matrix PSD", evl.min() > -1e-8, f"min eigenvalue {evl.min():.2e}")
cw = cf - removed(tf) + weil_pair(tf)
check("E2 same pair, Weil form: the echo exceeds its initial value", np.max(np.abs(cw)) > abs(cw[0]),
      f"max |C(t)|/C(0) on [0,6] = {np.max(np.abs(cw)) / abs(cw[0]):.2f}")
Hz = np.array([[0, 1], [1, 0]], complex)
check("E2 one off-line pair {rho, 1 - rho-bar} contributes 2 Re(z w-bar): a block of signature (1,1)", np.allclose(np.linalg.eigvalsh(Hz), [-1, 1]))

print(f"\n{npass} of {npass + nfail} pass")
