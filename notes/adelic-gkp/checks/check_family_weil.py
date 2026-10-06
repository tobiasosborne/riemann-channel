#!/usr/bin/env python3
"""Checks for data-ladder.md section 4b, 'One step against a family' (lane G/C/E synthesis), 2026-10-06.

Conventions (fixed here).
  Omega(x, y) = x^T Omega y with Omega = [[0,1],[-1,0]].  V = q M^{-1} = adj(M) (the other Frobenius root).
  Weil form W = (1/2) Omega (M - V).  J_formula = (M - V)/sqrt(4q - lambda^2).
  Vacuum metric G_J = Omega J (symmetric positive definite exactly when Omega(x, Jx) > 0 for all x != 0);
  in the other writing G_J = -Omega^T J.  For a given Omega the vacuum is J_vac = s J_formula with s = +-1 chosen so that Omega J_vac > 0.
  Then W = (sqrt(4q - lambda^2)/2) * s * G_J: the sign of the Weil form is s, i.e. sin(theta) with the orientation of Omega.
CM part: K = Q(sqrt(-7)), O_K = Z[w], w = (1 + sqrt(-7))/2, basis (1, w); Omega(x, y) = Tr_{K/Q}(conj(x) y / sqrt(-7)), which is
  [[0,1],[-1,0]] in this basis; J_K = multiplication by i on K (x) R = C (sqrt(-7) = i sqrt 7).
Needs PARI/GP (/usr/bin/gp) for the a_p comparison; numpy only otherwise.  Run time a few seconds.
"""
import os
import subprocess
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


def leg7(x):
    r = x % 7
    if r == 0:
        return 0
    return 1 if r in (1, 2, 4) else -1


def isprime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


Om = np.array([[0.0, 1.0], [-1.0, 0.0]])
rng = np.random.default_rng(20261006)


def vacuum_data(M, Omega):
    """returns V, W = (1/2) Omega (M - V), J_formula, s, J_vac, G = Omega J_vac"""
    M = np.array(M, float)
    q = np.linalg.det(M)
    lam = np.trace(M)
    V = q * np.linalg.inv(M)
    W = 0.5 * Omega @ (M - V)
    Jf = (M - V) / np.sqrt(4 * q - lam ** 2)
    s = 1.0 if np.all(np.linalg.eigvalsh((Omega @ Jf + (Omega @ Jf).T) / 2) > 0) else -1.0
    Jv = s * Jf
    return V, W, Jf, s, Jv, Omega @ Jv


# ---------------------------------------------------------------------------------------------
print("== F1  one mode: the Weil form is sqrt(q) sin(theta) times the vacuum metric")
for q, lam in [(2, -1), (5, -2), (7, 2), (13, 3)]:
    M = np.array([[0.0, -1.0], [q, lam]])
    V, W, Jf, s, Jv, G = vacuum_data(M, Om)
    th = np.arccos(lam / (2 * np.sqrt(q)))                 # in (0, pi), sin(theta) > 0
    c = np.sqrt(q) * np.sin(th)
    X = rng.normal(size=(2, 2000))
    pos = np.min(np.einsum("ik,ij,jk->k", X, Om, Jf @ X)) > 0
    check(f"F1 (q,lambda)=({q},{lam}): J^2 = -1, JM = MJ, M V = q, M + V = lambda",
          np.allclose(Jf @ Jf, -np.eye(2), atol=1e-12) and np.allclose(Jf @ M, M @ Jf, atol=1e-12)
          and np.allclose(M @ V, q * np.eye(2), atol=1e-12) and np.allclose(M + V, lam * np.eye(2), atol=1e-12))
    check(f"F1 (q,lambda)=({q},{lam}): G_J = Omega J symmetric positive definite, Omega(x,Jx) > 0 for 2000 random x (s = {s:+.0f}, so J_vac = J_formula)",
          np.allclose(G, G.T, atol=1e-12) and np.all(np.linalg.eigvalsh(G) > 0) and pos and s == 1.0 and np.allclose(G, -Om.T @ Jf),
          f"eigenvalues of G_J: {np.round(np.linalg.eigvalsh(G), 4)}")
    check(f"F1 (q,lambda)=({q},{lam}): (1/2) Omega (M - V) = sqrt(q) sin(theta) G_J to 1e-12, cos(theta) = lambda/(2 sqrt q), theta = {th/np.pi:.4f} pi",
          np.max(np.abs(W - c * G)) < 1e-12 and abs(np.cos(th) - lam / (2 * np.sqrt(q))) < 1e-15,
          f"max |diff| = {np.max(np.abs(W - c * G)):.1e}; W = {W.tolist()}")
    check(f"F1 (q,lambda)=({q},{lam}): M = sqrt(q)(cos(theta) + sin(theta) J), the step is the rotation by theta about the vacuum",
          np.allclose(M, np.sqrt(q) * (np.cos(th) * np.eye(2) + np.sin(th) * Jf), atol=1e-12))

# ---------------------------------------------------------------------------------------------
print("== F2  M -> -M (theta -> theta + pi) and Omega -> -Omega: the vacuum form is orientation-independent, the Weil form is not")
for q, lam in [(2, -1), (5, -2), (7, 2), (13, 3)]:
    M = np.array([[0.0, -1.0], [q, lam]])
    V0, W0, Jf0, s0, Jv0, G0 = vacuum_data(M, Om)
    th = np.arccos(lam / (2 * np.sqrt(q)))
    c = np.sqrt(q) * np.sin(th)
    res = {}
    for lab, Mx, Ox in [("M, Om", M, Om), ("-M, Om", -M, Om), ("M, -Om", M, -Om), ("-M, -Om", -M, -Om)]:
        res[lab] = vacuum_data(Mx, Ox)
    V1, W1, Jf1, s1, Jv1, G1 = res["-M, Om"]
    V2, W2, Jf2, s2, Jv2, G2 = res["M, -Om"]
    V3, W3, Jf3, s3, Jv3, G3 = res["-M, -Om"]
    check(f"F2 (q,lambda)=({q},{lam}): M -> -M: V -> -V, J_formula -> -J_formula, Weil form -> -Weil form (rotation theta + pi: sin -> -sin)",
          np.allclose(V1, -V0) and np.allclose(Jf1, -Jf0, atol=1e-12) and np.allclose(W1, -W0, atol=1e-12)
          and np.allclose(W1, np.sqrt(q) * np.sin(th + np.pi) * G0, atol=1e-12))
    check(f"F2 (q,lambda)=({q},{lam}): M -> -M: the positive vacuum for Omega is still J (J_vac = -J_formula, s = -1) and G_J is unchanged",
          s1 == -1.0 and np.allclose(Jv1, Jv0, atol=1e-12) and np.allclose(G1, G0, atol=1e-12), f"s = {s1:+.0f}")
    check(f"F2 (q,lambda)=({q},{lam}): Omega -> -Omega, same M: J_formula unchanged, Weil form -> -Weil form, but the positive vacuum flips (J_vac -> -J_vac) and G_J = (-Omega)(-J) is unchanged",
          np.allclose(Jf2, Jf0, atol=1e-12) and np.allclose(W2, -W0, atol=1e-12) and s2 == -1.0
          and np.allclose(Jv2, -Jv0, atol=1e-12) and np.allclose(G2, G0, atol=1e-12))
    check(f"F2 (q,lambda)=({q},{lam}): both flipped: Weil form = + original, J_vac flips, G_J unchanged: the four (M, Omega) orientations share one vacuum metric, Weil form carries sign s",
          np.allclose(W3, W0, atol=1e-12) and np.allclose(G3, G0, atol=1e-12) and s3 == 1.0
          and np.allclose(Jv3, -Jv0, atol=1e-12) and all(np.allclose(r[5], G0, atol=1e-12) for r in res.values())
          and all(np.allclose(r[1], r[3] * c * G0, atol=1e-12) for r in res.values()))

# ---------------------------------------------------------------------------------------------
print("== F3  the CM family on O_K, K = Q(sqrt(-7)): conjugate primes give opposite Weil forms, one vacuum J_K")


def gp_ap(curve, primes):
    script = f'P={primes}; E=ellinit("{curve}"); print(vector(#P,i,ellap(E,P[i])));\nquit\n'
    r = subprocess.run(["gp", "-q", "-f"], input=script, capture_output=True, text=True, timeout=120)
    return [int(v) for v in r.stdout.strip().strip("[]").split(",")]


def rep(p):
    y = 1
    while 7 * y * y < 4 * p:
        r = 4 * p - 7 * y * y
        x = int(round(r ** 0.5))
        if x * x == r and x > 0:
            return x, y
        y += 1
    return None


def mult(a, b):
    """multiplication by a + b w on O_K in the basis (1, w), w^2 = w - 2: columns are images of 1 and w"""
    return np.array([[a, -2 * b], [b, a + b]], float)


split = [p for p in range(2, 101) if isprime(p) and p != 7 and leg7(p) == 1]
check("F3 split primes p <= 100 ((-7|p) = (p|7) = +1)", split == [2, 11, 23, 29, 37, 43, 53, 67, 71, 79], str(split))
ap_pari49 = gp_ap("49a1", split)
ap_pari441 = gp_ap("441d1", split)
xy = {p: rep(p) for p in split}
ap_formula = [leg7(xy[p][0]) * xy[p][0] for p in split]
ap_tw = [(1 if p % 3 == 1 else -1) * a for p, a in zip(split, ap_formula)]
check("F3 a_p = (x|7) x from 4p = x^2 + 7y^2 equals PARI ellap(ellinit(\"49a1\"), p) for the 10 split primes p <= 100", ap_formula == ap_pari49,
      f"formula {ap_formula}")
check("F3 441d1 (the quadratic twist by -3, the E mode's lift): ellap = (p|3)(x|7) x  (PARI ellap(ellinit(\"441d1\"), p))", ap_tw == ap_pari441,
      f"PARI {ap_pari441}")

# lattice data
sq7 = np.sqrt(7.0)
Bm = np.array([[1.0, 0.5], [0.0, sq7 / 2]])               # w -> (1 + i sqrt 7)/2 in R^2 = C, columns = images of 1 and w
Jc = np.array([[0.0, -1.0], [1.0, 0.0]])
JK = np.linalg.inv(Bm) @ Jc @ Bm                          # multiplication by i in the basis (1, w)
T = np.array([[2.0, 1.0], [1.0, 4.0]])                    # Tr(x conj(y)): Tr 1 = 2, Tr conj(w) = 1, Tr(w conj w) = 2 N(w) = 4
# Omega(x,y) = Tr(conj(x) y / sqrt(-7)): Omega(1, w) = Tr(w/sqrt(-7)) = Tr((1 + sqrt(-7))/(2 sqrt(-7))) = 1
sqm7 = 1j * sq7
wv = (1 + sqm7) / 2
OmK = np.array([[2 * (np.conj(a) * b / sqm7).real for b in (1, wv)] for a in (1, wv)])
check("F3 Omega(x,y) = Tr_{K/Q}(conj(x) y / sqrt(-7)) in the basis (1, w) is [[0,1],[-1,0]] (integral, unimodular)", np.allclose(OmK, Om), str(np.round(OmK, 12).tolist()))
check("F3 J_K = multiplication by i = sqrt(-7)/sqrt(7) in the basis (1, w): J_K = mult(2w - 1)/sqrt 7, J_K^2 = -1",
      np.allclose(JK, mult(-1, 2) / sq7, atol=1e-12) and np.allclose(JK @ JK, -np.eye(2)), str(np.round(JK, 6).tolist()))
GK = Om @ JK
check("F3 G_{J_K} = Omega J_K is symmetric positive definite (= -Omega^T J_K), Omega(x, ix) = 2|x|^2/sqrt 7 > 0",
      np.allclose(GK, GK.T, atol=1e-12) and np.all(np.linalg.eigvalsh(GK) > 0), str(np.round(GK, 6).tolist()))
check("F3 Rosati/trace form Tr_{K/Q}(x conj(y)) = [[2,1],[1,4]] is a positive multiple of G_{J_K}: T = sqrt(7) G_{J_K}, positive definite",
      np.allclose(T, sq7 * GK, atol=1e-12) and np.all(np.linalg.eigvalsh(T) > 0), f"scalar sqrt 7 = {sq7:.6f}, det T = 7")

rows = []
okint = okdet = okcomm = okV = okOm = okW = okopp = okscal = True
for p, ax in zip(split, ap_formula):
    x, y = xy[p]
    a_p = ax
    # psi(frak p) = (a_p + y sqrt(-7))/2 = alpha, conjugate (a_p - y sqrt(-7))/2; in the basis: (a_p + y sqrt-7)/2 = (a_p - y)/2 + y w
    a_, b_ = (a_p - y) // 2, y
    assert (a_p - y) % 2 == 0
    Ma = mult(a_, b_)
    Mb = mult((a_p + y) // 2, -y)                  # conjugate (a_p - y sqrt(-7))/2 = (a_p + y)/2 - y w
    alpha = (a_p + y * sqm7) / 2
    okint &= np.array_equal(Ma, np.round(Ma)) and np.array_equal(Mb, np.round(Mb))
    okdet &= round(np.linalg.det(Ma)) == p and round(np.linalg.det(Mb)) == p and abs(abs(alpha) ** 2 - p) < 1e-9
    okcomm &= np.allclose(Ma @ JK, JK @ Ma, atol=1e-12) and np.allclose(Mb @ JK, JK @ Mb, atol=1e-12)
    Va, Vb = p * np.linalg.inv(Ma), p * np.linalg.inv(Mb)
    okV &= np.allclose(Va, Mb, atol=1e-12) and np.allclose(Vb, Ma, atol=1e-12)         # V_p = M_{pbar}: the other Frobenius root is the conjugate prime
    okOm &= np.allclose(Ma.T @ Om @ Ma, p * Om) and np.allclose(Mb.T @ Om @ Mb, p * Om)
    Wa, Wb = 0.5 * Om @ (Ma - Va), 0.5 * Om @ (Mb - Vb)
    imp = alpha.imag
    okW &= np.allclose(Wa, imp * GK, atol=1e-12) and np.allclose(Wb, -imp * GK, atol=1e-12)   # fixed positive scalar = 1
    okopp &= np.allclose(Wa, -Wb, atol=1e-12) and imp > 0
    # the ideal P_+ = ((x + y sqrt-7)/2) (generator with y > 0): psi(P_+) = (x|7) * that generator
    sgn_char = leg7(x)
    rows.append((p, x, y, a_p, sgn_char))
check("F3 psi(frak p) = (a_p + y sqrt(-7))/2 and its conjugate, as 2x2 matrices on O_K = Z + Z w: integral for all 10 split p <= 100", okint)
check("F3 each has determinant p (norm), M^T Omega M = p Omega, and V_p = p M^{-1} equals the matrix of the conjugate prime", okdet and okOm and okV)
check("F3 J_K commutes with every multiplication matrix M_frak p, M_frak pbar (10 split p, both primes)", okcomm)
check("F3 Weil form (1/2) Omega (M_p - V_p) = Im psi(frak p) * G_{J_K} (the fixed positive scalar is exactly 1 for this Omega), with Im psi = y sqrt 7 / 2",
      okW, "for p, pbar: +y sqrt7/2 G and -y sqrt7/2 G")
check("F3 conjugate primes have opposite Weil forms: W(frak p) = -W(frak pbar) for every split p <= 100 (so for a fixed Omega no labelling of ideals makes both positive)", okopp)
Ms = [(mult((a_p - y) // 2, y)) for (p, x, y, a_p, sg) in rows]
check("F3 the multiplication matrices all commute pairwise (O_K commutative): one commuting family, one vacuum J_K, Weil forms vary in sign", all(np.array_equal(A @ B, B @ A) for A in Ms for B in Ms))
sgn_line = ", ".join(f"{p}:{'+' if y > 0 else '-'}/{'+' if sg > 0 else '-'}" for (p, x, y, a_p, sg) in rows)
print("      p : sign Im psi for the generator with a_p = (x|7) x, y > 0 (and its conjugate is the opposite) / sign Im psi(P_+) for the ideal P_+ = ((x + y sqrt-7)/2), = (x|7)")
print("      " + sgn_line)
print("      generator normalised by the character (a_p = (x|7)x, y > 0): Im psi = +y sqrt7/2 > 0 at all 10 primes; conjugate generator: < 0 at all 10")
print("      for the fixed ideal P_+ the sign of Im psi(P_+) is (x|7): " + ", ".join(f"{p}:{'+' if sg > 0 else '-'}" for (p, x, y, a_p, sg) in rows))
check("F3 sign of Im psi: + for the character's generator at every p; the sign attached to a fixed ideal P_+ = ((x+y sqrt-7)/2) is (x|7), taking both values among p <= 100",
      all(r[2] > 0 for r in rows) and {r[4] for r in rows} == {1, -1})

# ---------------------------------------------------------------------------------------------
print("== F4  the zeta family: sign statistics of sin(gamma log p) over the first 200 zeros")
gam = np.load(os.path.join(ROOT, "data", "zeros3000.npy"))
check("F4 data/zeros3000.npy: 3000 positive increasing imaginary parts, gamma_1 = 14.1347", len(gam) == 3000 and np.all(np.diff(gam) > 0) and abs(gam[0] - 14.134725) < 1e-5)
g200 = gam[:200]
primes = [2, 3, 5]
S = {p: np.sin(g200 * np.log(p)) for p in primes}
frac = {p: float(np.mean(S[p] > 0)) for p in primes}
for p in primes:
    print(f"      p = {p}: fraction of the first 200 pairs with sin(gamma log p) > 0 = {frac[p]:.3f}  ({int(np.sum(S[p] > 0))} positive, {int(np.sum(S[p] < 0))} negative, min |sin| = {np.min(np.abs(S[p])):.2e})")
check("F4 fraction with sin(gamma_n log p) > 0 is about one half for p = 2, 3, 5", all(0.4 < frac[p] < 0.6 for p in primes),
      ", ".join(f"p={p}: {frac[p]:.3f}" for p in primes))
check("F4 both signs occur for each p, so no global sign makes all sin(gamma_n log p) positive (or all negative) for even one p; no sin vanishes",
      all(np.any(S[p] > 0) and np.any(S[p] < 0) and np.all(S[p] != 0) for p in primes))
agree = {}
for a, b in [(2, 3), (2, 5), (3, 5)]:
    agree[(a, b)] = int(np.sum(np.sign(S[a]) == np.sign(S[b])))
    print(f"      p, p' = {a}, {b}: sign patterns agree on {agree[(a, b)]} of 200 zeros (equal would be 200, opposite 0)")
check("F4 for each pair of primes the sign patterns over n are neither equal nor opposite (0 < agreements < 200), so no per-pair orientation serves two primes",
      all(0 < v < 200 for v in agree.values()), ", ".join(f"({a},{b}): {v}/200" for (a, b), v in agree.items()))
check("F4 agreements are near 100 of 200 (independent-looking signs): within 30 of 100 for the three pairs", all(abs(v - 100) < 30 for v in agree.values()))

print(f"\n{npass} of {npass + nfail} pass")
