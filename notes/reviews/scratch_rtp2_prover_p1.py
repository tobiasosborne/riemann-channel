#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane P, item P1 (bordering lemma, Loewner interval, midpoint condition).
Independent of notes/rtp-round-2/prover/checks/. Exact arithmetic (sympy). Deterministic. No zeros used."""
import sympy as sp
import itertools, random
ok = 0; bad = 0
def chk(name, cond):
    global ok, bad
    if cond: ok += 1; print("PASS", name)
    else: bad += 1; print("FAIL", name)

# ---- 1. Parity blocks of the full Loewner matrix vs the report's u, w, d (symbolic, N = 3, j = 4)
N = 3; j = N + 1
a = sp.symbols('a0:%d' % (j + 1)); b = sp.symbols('b0:%d' % (j + 1))
def A(n): return a[abs(n)]
def B(n): return sp.sign(n) * b[abs(n)] if n != 0 else 0
idx = list(range(-j, j + 1))
T = sp.Matrix(len(idx), len(idx), lambda r, c: A(idx[r]) if r == c else (B(idx[r]) - B(idx[c])) / (idx[r] - idx[c]))
pos = {n: k for k, n in enumerate(idx)}
def V(n):
    v = sp.zeros(len(idx), 1); v[pos[n]] = 1; return v
s2 = sp.sqrt(2)
ev = [V(0)] + [(V(i) + V(-i)) / s2 for i in range(1, j + 1)]
od = [(V(i) - V(-i)) / s2 for i in range(1, j + 1)]
E = sp.Matrix(j + 1, j + 1, lambda r, c: sp.simplify((ev[r].T * T * ev[c])[0]))
O = sp.Matrix(j, j, lambda r, c: sp.simplify((od[r].T * T * od[c])[0]))
cross = max(abs(sp.simplify((ev[r].T * T * od[c])[0])) != 0 for r in range(j + 1) for c in range(j))
chk("even-odd cross entries vanish", not cross)
bj = b[j]
we = [s2 / j] + [sp.Rational(-2 * j, i * i - j * j) for i in range(1, N + 1)]
ue = [0] + [2 * i * b[i] / (i * i - j * j) for i in range(1, N + 1)]
wo = [sp.Rational(-2 * i, i * i - j * j) for i in range(1, N + 1)]
uo = [2 * j * b[i] / (i * i - j * j) for i in range(1, N + 1)]
chk("even column = u_e + b w_e", all(sp.simplify(E[r, j] - (ue[r] + bj * we[r])) == 0 for r in range(j)))
chk("odd column = u_o + b w_o", all(sp.simplify(O[r, j - 1] - (uo[r] + bj * wo[r])) == 0 for r in range(N)))
chk("even diagonal a_j + b_j/j", sp.simplify(E[j, j] - (a[j] + bj / j)) == 0)
chk("odd diagonal a_j - b_j/j", sp.simplify(O[j - 1, j - 1] - (a[j] - bj / j)) == 0)
# plan.md 1.3 formulas
chk("plan.md E_ij formula", all(sp.simplify(E[r, c] - ((b[r] - b[c]) / (r - c) + (b[r] + b[c]) / (r + c))) == 0
                              for r in range(1, j + 1) for c in range(1, j + 1) if r != c))

# ---- 2. N = 0 step: odd block is affine (C_o = 0), even block quadratic
a0, a1, bb = sp.symbols('a0 a1 bb', positive=True)
se0 = sp.expand(a1 + bb - (s2 * bb) ** 2 / a0)
chk("N=0 even Schur complement a1 + b - 2 b^2/a0", sp.simplify(se0 - (a1 + bb - 2 * bb**2 / a0)) == 0)
T1 = sp.Matrix(3, 3, lambda r, c: [a1, a0, a1][r] if r == c else ([-bb, 0, bb][r] - [-bb, 0, bb][c]) / ([-1, 0, 1][r] - [-1, 0, 1][c]))
o1 = sp.Matrix([1, 0, -1]) / s2; e1 = sp.Matrix([1, 0, 1]) / s2; e0 = sp.Matrix([0, 1, 0])
chk("N=0 odd block is the scalar a1 - b (affine: C_o = 0, a half-line, not an interval)", sp.simplify((o1.T * T1 * o1)[0] - (a1 - bb)) == 0)
chk("N=0 even block [[a0, sqrt2 b],[sqrt2 b, a1 + b]]", sp.simplify((e0.T * T1 * e1)[0] - s2 * bb) == 0 and sp.simplify((e1.T * T1 * e1)[0] - (a1 + bb)) == 0)

# ---- 3. The exact example (N = 1, a = 1, b1 = 0)
x = sp.symbols('x', real=True)
Ge = sp.eye(2); Go = sp.Matrix([[1]])
ce = sp.Matrix([s2 * x / 2, sp.Rational(4, 3) * x]); co = sp.Matrix([sp.Rational(2, 3) * x])
se = sp.expand(1 + x / 2 - (ce.T * Ge.inv() * ce)[0]); so = sp.expand(1 - x / 2 - (co.T * Go.inv() * co)[0])
chk("s_e = 1 + b/2 - 41 b^2/18", sp.simplify(se - (1 + x / 2 - sp.Rational(41, 18) * x**2)) == 0)
chk("s_o = 1 - b/2 - 4 b^2/9", sp.simplify(so - (1 - x / 2 - sp.Rational(4, 9) * x**2)) == 0)
# check against a direct 5x5 Loewner determinant factorisation: det(full) = det(E) det(O)
aa = {0: 1, 1: 1, 2: 1}; bv = {0: 0, 1: 0, 2: x}
idx2 = [-2, -1, 0, 1, 2]
T2 = sp.Matrix(5, 5, lambda r, c: aa[abs(idx2[r])] if r == c else
               ((sp.sign(idx2[r]) * bv[abs(idx2[r])]) - (sp.sign(idx2[c]) * bv[abs(idx2[c])])) / (idx2[r] - idx2[c]))
chk("det(5x5 Loewner) = det G_e det G_o s_e s_o", sp.simplify(T2.det() - se * so) == 0)
re = sorted(sp.solve(se, x), key=lambda t: float(t)); ro = sorted(sp.solve(so, x), key=lambda t: float(t))
chk("I_e endpoints (9 -+ 3 sqrt337)/82", sp.simplify(re[0] - (9 - 3 * sp.sqrt(337)) / 82) == 0 and sp.simplify(re[1] - (9 + 3 * sp.sqrt(337)) / 82) == 0)
chk("I_o endpoints (-9 -+ 3 sqrt73)/16", sp.simplify(ro[0] - (-9 - 3 * sp.sqrt(73)) / 16) == 0 and sp.simplify(ro[1] - (-9 + 3 * sp.sqrt(73)) / 16) == 0)
chk("I_e strictly inside I_o", float(ro[0]) < float(re[0]) and float(re[1]) < float(ro[1]))
chk("s_o > 0 at both even endpoints", all(float(so.subs(x, r)) > 0 for r in re))
dlog = sp.diff(sp.log(se) + sp.log(so), x)
chk("(log s_e s_o)'(0) = 0", sp.simplify(dlog.subs(x, 0)) == 0)
chk("log s_e s_o strictly concave on J (second derivative < 0 on 200 points)",
    all(float(sp.diff(dlog, x).subs(x, re[0] + (re[1] - re[0]) * sp.Rational(k, 201))) < 0 for k in range(1, 201)))
m = (re[0] + re[1]) / 2
chk("midpoint 9/82", sp.simplify(m - sp.Rational(9, 82)) == 0)
chk("offset / half-width = -3/sqrt(337)", sp.simplify((0 - m) / ((re[1] - re[0]) / 2) + 3 / sp.sqrt(337)) == 0)
print("   offset/half-width =", sp.N(-3 / sp.sqrt(337), 30))

# ---- 4. P1.3 condition: it is NOT "equal centres". Crossing case with distinct centres and midpoint maximiser.
Ce, Co, bE, bO, sE, sO = 1, 1, 1, -1, 4, 4
Se = sE - Ce * (x - bE)**2; So = sO - Co * (x - bO)**2   # I_e=[-1,3], I_o=[-3,1], J=[-1,1], m=0
cond = Ce * (0 - bE) * So.subs(x, 0) + Co * (0 - bO) * Se.subs(x, 0)
chk("crossing example: distinct centres, condition (P1.2) holds at m = 0", cond == 0 and sp.diff(sp.log(Se * So), x).subs(x, 0) == 0)
# nested case: J = I_e  =>  m = beta_e*, condition reduces to beta_e* = beta_o*
be, bo, se_, so_, ce_, co_ = sp.symbols('be bo se so ce co', positive=True)
condn = ce_ * (be - be) * (so_ - co_ * (be - bo)**2) + co_ * (be - bo) * se_
chk("nested case: (P1.2) reduces to C_o (beta_e* - beta_o*) s_e* = 0", sp.simplify(condn - co_ * (be - bo) * se_) == 0)

# ---- 5. random check of P1.3 vs brute-force maximisation (exact rationals, 200 trials)
random.seed(1)
agree = 0
for t in range(200):
    Ce, Co = sp.Rational(random.randint(1, 9), random.randint(1, 9)), sp.Rational(random.randint(1, 9), random.randint(1, 9))
    bE, bO = sp.Rational(random.randint(-9, 9), 4), sp.Rational(random.randint(-9, 9), 4)
    sE, sO = sp.Rational(random.randint(1, 30), 3), sp.Rational(random.randint(1, 30), 3)
    rE, rO = sp.sqrt(sE / Ce), sp.sqrt(sO / Co)
    Aa, Bb = max(bE - rE, bO - rO, key=float), min(bE + rE, bO + rO, key=float)
    if float(Aa) >= float(Bb): agree += 1; continue
    f = (sE - Ce * (x - bE)**2) * (sO - Co * (x - bO)**2)
    crit = [r for r in sp.Poly(sp.diff(f, x), x).nroots(n=40) if abs(sp.im(r)) < 1e-30 and float(Aa) < float(sp.re(r)) < float(Bb)]
    xm = max(crit, key=lambda r: float(f.subs(x, sp.re(r))))
    mm = (Aa + Bb) / 2
    c = Ce * (mm - bE) * (sO - Co * (mm - bO)**2) + Co * (mm - bO) * (sE - Ce * (mm - bE)**2)
    agree += int((abs(float(sp.re(xm) - mm)) < 1e-25) == (abs(float(c)) < 1e-25)) and len(crit) == 1
chk("P1.3 iff-condition agrees with brute-force maximiser (200 random quadratic pairs; unique interior critical point)", agree == 200)

# ---- 6. P1.4: odd column alone can vanish for nonzero data (b_n = kappa n)
kap = sp.Rational(3, 7)
N = 4; j = 5
bvec = {i: kap * i for i in range(1, j + 1)}
uo_ = [2 * j * bvec[i] / (i * i - j * j) - 2 * i * bvec[j] / (i * i - j * j) for i in range(1, N + 1)]
chk("odd old-to-new column vanishes for b_n = kappa n (so (iii) needs the even column or the pair)", all(v == 0 for v in uo_))

# ---- 7. Gaussian information identities (P1.1): real 2I, complex I
import numpy as np
rng = np.random.default_rng(3)
for t in range(3):
    X = rng.normal(size=(4, 4)); Bm = X @ X.T + 0.1 * np.eye(4)
    G, c, d = Bm[:3, :3], Bm[:3, 3], Bm[3, 3]
    s = d - c @ np.linalg.solve(G, c)
    DI = np.log(d / s)
    Ireal = 0.5 * (np.linalg.slogdet(G)[1] + np.log(d) - np.linalg.slogdet(Bm)[1])
    Icplx = (np.linalg.slogdet(G)[1] + np.log(d) - np.linalg.slogdet(Bm)[1])
    chk("Delta I = 2 I_real = I_complex (trial %d)" % t, abs(DI - 2 * Ireal) < 1e-12 and abs(DI - Icplx) < 1e-12)
print("checks passed %d failed %d" % (ok, bad))
