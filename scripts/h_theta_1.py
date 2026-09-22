#!/usr/bin/env python3
"""Numerics lane for notes/h-theta-1 (independent of notes/h-theta-1/checks/).

Checks the displayed formulas of notes/h-theta-1/astra-proofs.md (items 1-8 of its
"Numerical checks for the blind lane"): the Cauchy Gram of the Riemann model at three
zeros (T2), the cyclic-product obstruction (T4, (15)-(16)), an independent Nystrom /
shifted-Legendre implementation of the augmented cosine Sonine evaluator Gram
((17)-(23)), the synthetic bad-zero renewal laws (T6, (30)-(35)), the damped
length-two chain (T7, (37)-(41)) and the jet Gram identity (T1, (3)-(4)).

Deterministic; mpmath at 30 digits for scalars, numpy double for the one linear solve.
Run from the repo root:  python3 scripts/h_theta_1.py
"""
import sys, time, os
import numpy as np
import mpmath as mp
from numpy.polynomial import legendre as npleg

mp.mp.dps = 30
T0 = time.time()
LED = []
def check(ok, desc, val=""):
    LED.append((bool(ok), desc, str(val)))
    print("D%02d %s %s %s" % (len(LED), "PASS" if ok else "FAIL", desc, val))
def close(a, b, tol):
    return abs(mp.mpf(a) - mp.mpf(b)) <= tol if not isinstance(a, complex) and not isinstance(a, mp.mpc) and not isinstance(b, complex) and not isinstance(b, mp.mpc) else abs(mp.mpc(a) - mp.mpc(b)) <= tol

# ---------------------------------------------------------------- 1. zeros
g24 = [mp.mpf('14.13472514173469379045725'), mp.mpf('21.02203963877155499262848'),
       mp.mpf('25.01085758014568876321379')]
try:
    z = np.load(os.path.join(os.path.dirname(__file__), '..', 'data', 'zeros3000.npy'))
    dev = max(abs(float(g24[n]) - float(z[n])) for n in range(3))
    check(dev < 1e-9, "item 1: 24-digit ordinates agree with data/zeros3000.npy (max dev)", "%.2e" % dev)
except Exception as e:
    check(False, "item 1: could not load data/zeros3000.npy", repr(e))
# xi(1/2 + i gamma_n) = 0 (so Theta(w_n) = 0 at w_n = gamma_n/2 + i/4)
def xi(s):
    return mp.mpf(1)/2*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
rel = max(abs(xi(mp.mpf(1)/2 + 1j*g)) / abs(xi(mp.mpf(1)/2 + 1j*(g+mp.mpf('0.5')))) for g in g24)
check(rel < 1e-18, "item 1: xi(1/2 + i gamma_n) = 0 relative to a neighbour (max)", "%.1e" % rel)

rho = [mp.mpf(1)/2 + 1j*g for g in g24]
d = [-mp.mpf(1)/4 - 1j*g/2 for g in g24]           # d_n = -1/4 - i gamma_n/2
w = [g/2 + 1j*mp.mpf(1)/4 for g in g24]             # w_n = gamma_n/2 + i/4

# ---------------------------------------------------------------- 2. Cauchy Gram (T2)
# first-slot convention: G_ij = <k_i, k_j> = i/(w_j - conj(w_i)) = 1/(-(d_i + conj d_j))
G = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        G[i, j] = 1j/(w[j] - mp.conj(w[i]))
Gexp = [[2, mp.mpc('0.04129237', '0.28439352'), mp.mpc('0.01676583', '0.18234737')],
        [mp.mpc('0.04129237', '-0.28439352'), 2, mp.mpc('0.11826854', '0.47175165')],
        [mp.mpc('0.01676583', '-0.18234737'), mp.mpc('0.11826854', '-0.47175165'), 2]]
dev = max(abs(G[i, j] - Gexp[i][j]) for i in range(3) for j in range(3))
check(dev < 1e-8, "item 2: Cauchy Gram i/(w_j - conj w_i) matches the displayed 3x3 (max dev)", "%.1e" % dev)
dev = max(abs(-(d[i] + mp.conj(d[j]))*G[i, j] - 1) for i in range(3) for j in range(3))
check(dev < 1e-25, "item 2: loss matrix -(d_i + conj d_j) G_ij is identically 1 (max dev)", "%.1e" % dev)
# the same Gram from the notebook's y-picture kernel -i y^{-(1-sigma)/2 - i gamma/2} 1_{y>1}, d^x y
def gram_y(i, j):
    f = lambda X: (-1j*mp.e**(-X/4 - 1j*g24[i]*X/2)) * mp.conj(-1j*mp.e**(-X/4 - 1j*g24[j]*X/2))
    return mp.quad(f, mp.linspace(0, 240, 49))
dev = max(abs(gram_y(i, j) - G[i, j]) for i in range(3) for j in range(3))
check(dev < 1e-20, "item 2: notebook kernels (thm:model-space-jets) integrated in X=log y give the same Gram", "%.1e" % dev)
ev = mp.eigh(mp.matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))[0]
check(max(abs(ev[k] - [0, 0, 3][k]) for k in range(3)) < 1e-25, "item 2: loss spectrum (3,0,0)", [mp.nstr(ev[k], 6) for k in range(3)])

# ---------------------------------------------------------------- 3. cyclic product (T4)
prod = 1
for (i, j) in [(0, 1), (1, 2), (2, 0)]:
    prod *= -(d[i] + mp.conj(d[j]))
check(abs(prod - mp.mpc('11.4772516480', '-37.3489700175')) < 1e-9, "item 3: cyclic product of -(d_i + conj d_j)", mp.nstr(prod, 12))
a = mp.mpf(1)/4; b = [-g/2 for g in g24]
q12, q23, q31 = b[1]-b[0], b[2]-b[1], b[0]-b[2]
lhs = mp.im((2*a + 1j*q12)*(2*a + 1j*q23)*(2*a + 1j*q31))
check(abs(lhs + q12*q23*q31) < 1e-25 and abs(lhs) > 1, "item 3: (16) Im[prod (2a + i q)] = -q12 q23 q31 != 0", mp.nstr(lhs, 10))

# ---------------------------------------------------------------- 4. Sonine Gram, (17)-(23)
# Nystrom discretisation on (0,1): Gauss-Legendre nodes x_i, weights w_i; cosine kernel 2cos(2 pi x y);
# Q = projection onto mean zero; T = Q C Q; solve (I - T^2) v = r_2, r_2 = Q C q_2 (anchor t = 2).
def chi(s):
    return mp.pi**(s - mp.mpf(1)/2)*mp.gamma((1 - s)/2)/mp.gamma(s/2)
def Cq_parts(s, x):
    """(18): C q_s(x) = A(x)/(1-s) + chi(s) x^{s-1} + B_s(x); returns (A, B_s) at x (mp)."""
    A = mp.sin(2*mp.pi*x)/(mp.pi*x)
    B = -2*mp.nsum(lambda n: (-1)**n*(2*mp.pi*x)**(2*n)/(mp.factorial(2*n)*(2*n + 1 - s)), [0, 60])
    return A, B
def sonine(nn, ndeg):
    xs, ws = npleg.leggauss(nn); xs = (xs + 1)/2; ws = ws/2          # (0,1)
    C = 2*np.cos(2*np.pi*np.outer(xs, xs))*ws[None, :]               # Nystrom of P C P
    Qm = np.eye(nn) - np.outer(np.ones(nn), ws)                       # mean-zero projection
    Tm = Qm @ C @ Qm
    # r_2 = Q C q_2 with C q_2 from (18) at s = 2 (chi(2) = -2 pi^2)
    s2 = mp.mpf(2)
    cq2 = np.array([float(Cq_parts(s2, mp.mpf(x))[0]/(1 - s2) + chi(s2)*mp.mpf(x)**(s2 - 1) + Cq_parts(s2, mp.mpf(x))[1]) for x in xs])
    r2 = Qm @ cq2
    v = np.linalg.solve(np.eye(nn) - Tm @ Tm, r2)
    # shifted-Legendre coefficients of v (orthonormal basis sqrt(2n+1) P_n(2x-1))
    coef = []
    for n in range(ndeg + 1):
        Pn = npleg.Legendre.basis(n)(2*xs - 1)*np.sqrt(2*n + 1)
        coef.append(float(np.sum(ws*v*Pn)))
    def I_s(s):  # int_0^1 (C q_s) v dx, with the x^{s-1} part by the exact moments (21)
        s = mp.mpc(s)
        A_int = mp.mpf(0); B_int = mp.mpf(0)
        for x, wt, vv in zip(xs, ws, v):
            A, B = Cq_parts(s, mp.mpf(x))
            A_int += wt*A*vv; B_int += wt*B*vv
        mom = mp.mpf(0)
        for n, c in enumerate(coef):
            mu = mp.sqrt(2*n + 1)/s
            for k in range(1, n + 1):
                mu *= (s - k)/(s + k)
            mom += c*mu
        return A_int/(1 - s) + chi(s)*mom + B_int
    def H(s):    # (17) with t = 2
        s = mp.mpc(s)
        return 1/((1 - s)*(1 - mp.mpf(2))) + 1/(s + 2 - 1) - I_s(s)
    p = lambda s: s*(s - 1); m = lambda s: mp.pi**(-s/2)*mp.gamma(s/2)
    F = lambda s: p(s)*p(2)*m(s)*m(2)*H(s)
    F2 = F(mp.mpf(2)); F2 = mp.re(F2) if abs(mp.im(F2)) < 1e-20*abs(F2) else F2; bconst = mp.sqrt(3*F2)
    E = lambda s: (s + 1)*F(s)/bconst
    return E, F2, bconst, v, coef
E64, F2, bconst, v64, coef64 = sonine(64, 40)
check(abs(mp.im(F2)) < 1e-25*abs(F2) and mp.re(F2) > 0, "item 4: F(2) real positive (structure-function normalisation (19))", mp.nstr(F2, 12))
check(abs(E64(mp.mpf(2)) - bconst) < 1e-20, "item 4: E_*(2) = b", mp.nstr(bconst, 10))
# E_*(-1) = 0 requires the pole of 1/(s+1) in (17) to cancel against the moment poles of (21): test near s = -1
eps = mp.mpf('1e-4')
Em, Ep = E64(-1 - eps), E64(-1 + eps)
check(abs(Em) < 1e-2 and abs(Ep) < 1e-2 and abs(Em + Ep) < 1e-2*abs(Em), "item 4: E_*(-1 -+ 1e-4) ~ -+1e-4 F(-1): no pole at s = -1, E_*(-1) = 0", "%s %s" % (mp.nstr(Em, 6), mp.nstr(Ep, 6)))
# convergence in the discretisation
E40, _, _, _, _ = sonine(40, 30)
conv = max(abs(E40(r)/E64(r) - 1) for r in rho)
check(conv < 1e-8, "item 4: E_*(rho_n) converged between 40 and 64 nodes (max rel dev)", "%.1e" % conv)
# (22): E_*^#(rho)/E_*(rho) = E_*(1-rho)/E_*(rho)
ratios_exp = [mp.mpc('-0.99880741', '-0.04882370'), mp.mpc('-0.99983369', '0.01823721'), mp.mpc('-0.99790571', '-0.06468528')]
Ev = [E64(r) for r in rho]; Ehv = [E64(1 - r) for r in rho]
ratios = [Ehv[n]/Ev[n] for n in range(3)]
dev = max(abs(ratios[n] - ratios_exp[n]) for n in range(3))
check(dev < 5e-8, "item 4: structure-phase ratios (22) at the three zeros (max dev)", [mp.nstr(r, 10) for r in ratios])
check(max(abs(abs(r) - 1) for r in ratios) < 1e-12, "item 4: |E_*^#/E_*| = 1 on the critical line", "%.1e" % max(abs(abs(r) - 1) for r in ratios))
check(max(abs(ratios[i] - ratios[j]) for i in range(3) for j in range(i)) > 0.03, "item 4: the three phases are distinct (min pairwise distance)", "%.4f" % min(abs(ratios[i] - ratios[j]) for i in range(3) for j in range(i)))
# Gram (10) off-diagonal, (20) diagonal, then raw values against the displayed G^Son
p = lambda s: s*(s - 1)
def Eprime(s):
    h = mp.mpf('1e-4')
    return (-E64(s + 2*h) + 8*E64(s + h) - 8*E64(s - h) + E64(s - 2*h))/(12*h)
GS = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        si, sj = rho[i], rho[j]
        if i != j:
            num = mp.conj(E64(si))*E64(sj) - mp.conj(E64(1 - si))*E64(1 - sj)
            GS[i, j] = num/((mp.conj(si) + sj - 1)*mp.conj(p(si))*p(sj))
        else:
            GS[i, i] = (E64(mp.conj(si))*Eprime(si) + E64(1 - mp.conj(si))*Eprime(1 - si))/abs(p(si))**2
GSexp = [[mp.mpf('2.5372715234e-10'), mp.mpf('-1.5861671773e-13'), mp.mpf('-1.0949051346e-15')],
         [mp.mpf('-1.5861671773e-13'), mp.mpf('6.0782412665e-15'), mp.mpf('5.2768178534e-17')],
         [mp.mpf('-1.0949051346e-15'), mp.mpf('5.2768178534e-17'), mp.mpf('1.2043193735e-17')]]
imax = max(abs(mp.im(GS[i, j]))/abs(GS[i, j]) for i in range(3) for j in range(3))
check(imax < 1e-9, "item 4: Sonine Gram is real on the critical line (max |Im|/|.|)", "%.1e" % imax)
rd = max(abs(mp.re(GS[i, j])/GSexp[i][j] - 1) for i in range(3) for j in range(3))
check(rd < 1e-6, "item 4: raw Sonine Gram G^Son entries (max rel dev from the displayed table)", "%.1e" % rd)
O = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        O[i, j] = mp.re(GS[i, j])/mp.sqrt(mp.re(GS[i, i])*mp.re(GS[j, j]))
Oexp = [[1, -0.12772518, -0.01980716], [-0.12772518, 1, 0.19503489], [-0.01980716, 0.19503489, 1]]
dev = max(abs(O[i, j] - Oexp[i][j]) for i in range(3) for j in range(3))
check(dev < 5e-8, "item 4: normalised Sonine Gram O (23) (max dev)", "%.1e" % dev)
L = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        L[i, j] = -(d[i] + mp.conj(d[j]))*O[i, j]
herm = max(abs(L[i, j] - mp.conj(L[j, i])) for i in range(3) for j in range(3))
evL = sorted([mp.re(e) for e in mp.eigh(L)[0]])
check(herm < 1e-20, "item 4: loss matrix -(d_i + conj d_j) O_ij is Hermitian", "%.1e" % herm)
dev = max(abs(evL[k] - [-0.09239752, 0.46931541, 1.12308212][k]) for k in range(3))
check(dev < 5e-8, "item 4: loss spectrum (23) incl. the negative eigenvalue -0.09239752", [mp.nstr(e, 9) for e in evL])
check(evL[0] < 0, "item 4: the loss matrix is NOT positive (negative eigenvalue): no contraction realisation on these evaluators", mp.nstr(evL[0], 9))
# rank-one obstruction on the actual Gram: N = -(d_i + conj d_j) G^Son has non-real cyclic product
cyc = L[0, 1]*L[1, 2]*L[2, 0]
check(abs(mp.im(cyc)) > 1e-6*abs(cyc), "item 4: cyclic product N12 N23 N31 of the actual loss matrix is not real (T4 (15))", mp.nstr(cyc, 8))
# T on L^2_0(0,1): extreme eigenvalues as diagnostics
xs, ws = npleg.leggauss(64); xs = (xs + 1)/2; ws = ws/2
Cm = 2*np.cos(2*np.pi*np.outer(xs, xs))*ws[None, :]; Qm = np.eye(64) - np.outer(np.ones(64), ws)
Tm = Qm @ Cm @ Qm
evT = np.sort(np.linalg.eigvals(Tm).real)
check(abs(evT[0] + 0.4710777795) < 1e-8 and abs(evT[-1] - 0.5623175942) < 1e-8 and np.max(np.abs(evT)) < 1,
      "item 4: extreme eigenvalues of T = Q C Q (diagnostic -0.4710777795, 0.5623175942) and ||T|| < 1", "%.10f %.10f" % (evT[0], evT[-1]))

# ---------------------------------------------------------------- 5. synthetic bad-zero pair (T6)
# rho_pm = 0.7 +- 1.5 i : delta = 0.2, w_pm = +-0.75 + 0.1 i ; forward modes h_i with Gram i/(w_i - conj w_j), d_i^+ = i w_i
wb = [mp.mpc('0.75', '0.1'), mp.mpc('-0.75', '0.1')]
dp = [1j*x for x in wb]
Gb = mp.matrix(2, 2)
for i in range(2):
    for j in range(2):
        Gb[i, j] = 1j/(wb[i] - mp.conj(wb[j]))
alpha = lambda i, j: -(dp[i] + mp.conj(dp[j]))
check(abs(alpha(0, 0) - mp.mpf('0.2')) < 1e-25 and abs(alpha(1, 1) - mp.mpf('0.2')) < 1e-25, "item 5: delta = 0.2 for both modes", mp.nstr(alpha(0, 0), 6))
# modal mixture with weights p: S(t) = sum_i p_i e^{-delta t} for normalised modes; check with p = (0.3, 0.7) via (30)
def S_of(q, t):
    return sum(q[i][j]/alpha(i, j)*mp.e**(-alpha(i, j)*t) for i in range(2) for j in range(2))
pw = [mp.mpf('0.3'), mp.mpf('0.7')]
q = [[pw[i]*alpha(i, i) if i == j else 0 for j in range(2)] for i in range(2)]   # normalised modal mixture: q_ii = p_i/<h_i,h_i> = p_i alpha_ii
check(abs(sum(q[i][j]/alpha(i, j) for i in range(2) for j in range(2)) - 1) < 1e-25, "item 5: reset trace one", "")
dev = max(abs(S_of(q, t) - mp.e**(-mp.mpf('0.2')*t)) for t in [0, 1, 3.7, 10])
check(dev < 1e-25, "item 5: modal-mixture holding law S(t) = e^{-0.2 t} for every mixture (max dev)", "%.1e" % dev)
tbar = sum(q[i][j]/alpha(i, j)**2 for i in range(2) for j in range(2))
check(abs(tbar - 5) < 1e-25, "item 5: mean holding time 5 (continuous)", mp.nstr(tbar, 8))
nbar = sum(q[i][j]/(alpha(i, j)*(1 - mp.e**(-alpha(i, j)*1))) for i in range(2) for j in range(2))
check(abs(nbar - 1/(1 - mp.e**(-mp.mpf('0.2')))) < 1e-25, "item 5: sampled (Delta = 1) mean (1 - e^{-0.2})^{-1} (33)", mp.nstr(nbar, 10))
# Cayley cogenerator h = 1 (34)-(35): built in the mode basis with the Gram metric
A = mp.diag(dp)  # generator in the (non-orthogonal) mode basis; adjoint w.r.t. Gram: A^* = Gb^{-1} A^H Gb ... work in an orthonormal basis instead
Lch = mp.cholesky(Gb)         # Gb = L L^H ; orthonormal coordinates y = L^H x
Ao = Lch.H*A*mp.inverse(Lch.H)  # generator in orthonormal coordinates
h = mp.mpf(1)
V = (mp.eye(2) + h*Ao)*mp.inverse(mp.eye(2) - h*Ao)
loss = mp.eye(2) - V.H*V
evl = sorted([mp.re(e) for e in mp.eigh(loss)[0]])
check(evl[0] > -1e-20 and abs(evl[0]) < 1e-20 and evl[1] > 0, "item 5: Cayley cogenerator I - V^*V has rank one (34)", [mp.nstr(e, 6) for e in evl])
evV = [((1 + h*x)/(1 - h*x)) for x in dp]
cay = sum(pw[i]*((1 + h*mp.mpf('0.2')/2)**2 + h**2*mp.mpf('1.5')**2/4)/(2*h*mp.mpf('0.2')) for i in range(2))
check(abs(cay - mp.mpf('4.43125')) < 1e-25, "item 5: Cayley-step mean 4.43125 (35)", mp.nstr(cay, 8))
# generator exit identity -(A + A^*) = j^* j rank one in orthonormal coordinates
lossA = -(Ao + Ao.H)
evA = sorted([mp.re(e) for e in mp.eigh(lossA)[0]])
check(abs(evA[0]) < 1e-20 and evA[1] > 0, "item 5: generator loss -(A + A^*) has rank one (scalar exit)", [mp.nstr(e, 6) for e in evA])

# ---------------------------------------------------------------- 6. coherent two-zero reset (T6, (30))
d2 = [mp.mpc('-0.1', '0.75'), mp.mpc('-0.2', '-1.25')]
u = [mp.mpc(1, 0), mp.mpc('0.3', '0.2')]
al = lambda i, j: -(d2[i] + mp.conj(d2[j]))
uu = [[u[i]*mp.conj(u[j]) for j in range(2)] for i in range(2)]
norm = sum(uu[i][j]/al(i, j) for i in range(2) for j in range(2))
q2 = [[uu[i][j]/norm for j in range(2)] for i in range(2)]
tbar2 = sum(q2[i][j]/al(i, j)**2 for i in range(2) for j in range(2))
check(abs(tbar2 - mp.mpf('4.61864473922355')) < 1e-12 and abs(mp.im(tbar2)) < 1e-25, "item 6: coherent two-zero reset mean (30)", mp.nstr(tbar2, 15))
S2 = lambda t: sum(q2[i][j]/al(i, j)*mp.e**(-al(i, j)*t) for i in range(2) for j in range(2))
direct = mp.quad(S2, mp.linspace(0, 400, 81))
check(abs(direct - tbar2) < 1e-15, "item 6: direct integration of S(t) agrees", mp.nstr(direct, 15))
# and from explicit functions: modes e^{d X} on X>0, Omega = sum q_ij |h_i><h_j|, S(t) = Tr(Z_t Omega Z_t^*)
Gh = lambda i, j: mp.quad(lambda X: mp.e**(d2[i]*X)*mp.conj(mp.e**(d2[j]*X)), mp.linspace(0, 400, 81))
Sfun = lambda t: sum(q2[i][j]*mp.e**((d2[i] + mp.conj(d2[j]))*t)*Gh(i, j) for i in range(2) for j in range(2))
dev = max(abs(Sfun(t) - S2(t)) for t in [0, 0.5, 2.0])
check(dev < 1e-18, "item 6: S(t) from explicit exponential modes matches (30) (max dev)", "%.1e" % dev)

# ---------------------------------------------------------------- 7. damped length-two chain (T7)
beta = mp.mpf(1)/4
b0 = lambda X: mp.sqrt(2*beta)*mp.e**(-beta*X)
b1 = lambda X: mp.sqrt(2*beta)*(1 - 2*beta*X)*mp.e**(-beta*X)
ip = lambda f, g: mp.quad(lambda X: f(X)*g(X), [0, mp.inf])
gram = [[ip(b0, b0), ip(b0, b1)], [ip(b1, b0), ip(b1, b1)]]
check(max(abs(gram[i][j] - (1 if i == j else 0)) for i in range(2) for j in range(2)) < 1e-25, "item 7: b0, b1 orthonormal", "")
# backward translation C_t f(X) = f(X+t): matrix in (b0,b1): C_t b_k = sum_l (C_t)_{lk} b_l
def Ct_matrix(t):
    M = mp.matrix(2, 2)
    for k, bk in enumerate([b0, b1]):
        shifted = lambda X, bk=bk: bk(X + t)
        for l, bl in enumerate([b0, b1]):
            M[l, k] = ip(shifted, bl)
    return M
Ct1 = Ct_matrix(mp.mpf(1))
Ct1_exp = mp.e**(-beta)*mp.matrix([[1, -2*beta], [0, 1]])
check(max(abs(Ct1[i, j] - Ct1_exp[i, j]) for i in range(2) for j in range(2)) < 1e-20, "item 7: C_1 matrix (37)", "")
AC = mp.matrix([[-beta, -2*beta], [0, -beta]])
jrow = mp.matrix([[mp.sqrt(2*beta), mp.sqrt(2*beta)]])
check(max(abs((-(AC + AC.H) - jrow.H*jrow)[i, j]) for i in range(2) for j in range(2)) < 1e-25, "item 7: -(A_C + A_C^*) = j^* j (38)", "")
loss1 = mp.eye(2) - Ct1_exp.H*Ct1_exp
loss1_exp = [[0.39346934, 0.30326533], [0.30326533, 0.24183668]]
check(max(abs(loss1[i, j] - loss1_exp[i][j]) for i in range(2) for j in range(2)) < 1e-8, "item 7: I - C_1^* C_1 (39) at t = 1", "")
evl1 = sorted([mp.re(e) for e in mp.eigh(loss1)[0]])
check(abs(evl1[0] - 0.00505426) < 1e-8 and abs(evl1[1] - 0.63025175) < 1e-8 and evl1[0] > 0, "item 7: its spectrum (0.00505426, 0.63025175), both positive: finite-time rank one refuted", [mp.nstr(e, 9) for e in evl1])
det_pos = all(((1 - mp.e**(-2*beta*t))**2 - (2*beta*t)**2*mp.e**(-2*beta*t)) > 0 for t in [0.01, 0.5, 1, 5, 20])
check(det_pos, "item 7: det(I - C_t^* C_t) > 0 for t > 0 (sample)", "")
Om = mp.matrix([[1, 1], [1, 1]])/2
Ct = lambda t: mp.e**(-beta*t)*mp.matrix([[1, -2*beta*t], [0, 1]])
Sj = lambda t: sum((Ct(t)*Om*Ct(t).H)[i, i] for i in range(2))
mj = lambda t: (jrow*Ct(t)*Om*Ct(t).H*jrow.H)[0, 0]
check(abs(Sj(1) - mp.mpf('0.379081662320396')) < 1e-14 and abs(mj(1) - mp.mpf('0.341173496088356')) < 1e-14, "item 7: S_j(1), m_j(1) (41)", "%s %s" % (mp.nstr(Sj(1), 15), mp.nstr(mj(1), 15)))
check(abs(mp.quad(mj, [0, mp.inf]) - 1) < 1e-20 and abs(mp.quad(Sj, [0, mp.inf]) - 2) < 1e-20, "item 7: int m_j = 1, mean 2", "")
X = mp.matrix(2, 2)
for i in range(2):
    for j in range(2):
        X[i, j] = mp.quad(lambda t, i=i, j=j: (Ct(t)*Om*Ct(t).H)[i, j], [0, mp.inf])
rho_inf = X/(X[0, 0] + X[1, 1])
check(max(abs(rho_inf[i, j] - (mp.mpf(1)/2 if i == j else 0)) for i in range(2) for j in range(2)) < 1e-20, "item 7: stationary density I/2 for the exit reset", "")
for k, (mean_exp) in enumerate([2, 6]):
    Ok = mp.matrix(2, 2); Ok[k, k] = 1
    mean = mp.quad(lambda t: sum((Ct(t)*Ok*Ct(t).H)[i, i] for i in range(2)), [0, mp.inf])
    check(abs(mean - mean_exp) < 1e-20, "item 7: basis reset b%d for C_t has mean %d (40)" % (k, mean_exp), mp.nstr(mean, 8))
# (40) general formula against direct computation for a sample density
pp, cc = mp.mpf('0.3'), mp.mpc('0.2', '0.1')
Og = mp.matrix([[pp, cc], [mp.conj(cc), 1 - pp]])
Sg = lambda t: mp.re(sum((Ct(t)*Og*Ct(t).H)[i, i] for i in range(2)))
S40 = lambda t: mp.e**(-2*beta*t)*(1 - 4*beta*t*mp.re(cc) + 4*beta**2*t**2*(1 - pp))
dev = max(abs(Sg(t) - S40(t)) for t in [mp.mpf(0), mp.mpf('0.7'), mp.mpf(3)])
tbar40 = (1 + 2*(1 - pp) - 2*mp.re(cc))/(2*beta)
check(dev < 1e-25 and abs(mp.quad(Sg, [0, mp.inf]) - tbar40) < 1e-18, "item 7: (40) S_Omega and mean for a general density", mp.nstr(tbar40, 8))

# ---------------------------------------------------------------- 8. jet check (T1, (3)-(4))
dj = mp.mpc('-0.3', '0.7'); c0 = mp.mpc(1, '0.4'); c1 = mp.mpc('0.2', '-0.3')
q0 = lambda X: mp.e**(dj*X)*c0
q1 = lambda X: mp.e**(dj*X)*(c1 + X*c0/2)
Gj = {}
for (k, fk) in [(0, q0), (1, q1)]:
    for (l, fl) in [(0, q0), (1, q1)]:
        Gj[(k, l)] = mp.quad(lambda X: fk(X)*mp.conj(fl(X)), [0, mp.inf])
cj = [c0, c1]
ok = True; worst = 0
for k in range(2):
    for l in range(2):
        val = -(dj + mp.conj(dj))*Gj[(k, l)]
        if k >= 1: val -= mp.mpf(k)/2*Gj[(k - 1, l)]
        if l >= 1: val -= mp.mpf(l)/2*Gj[(k, l - 1)]
        worst = max(worst, abs(val - cj[k]*mp.conj(cj[l])))
check(worst < 1e-22, "item 8: jet Gram identity (3) with lowering coefficients 1/2 (max dev)", "%.1e" % worst)
# closed form (4)
def G4(k, l):
    tot = 0
    for r in range(k + 1):
        for vv in range(l + 1):
            n = k + l - r - vv
            tot += mp.binomial(k, r)*mp.binomial(l, vv)*cj[r]*mp.conj(cj[vv])*mp.factorial(n)/(2**n*(-(dj + mp.conj(dj)))**(n + 1))
    return tot
worst = max(abs(G4(k, l) - Gj[(k, l)]) for k in range(2) for l in range(2))
check(worst < 1e-22, "item 8: closed form (4) for the jet Gram (max dev)", "%.1e" % worst)

# ---------------------------------------------------------------- summary
npass = sum(1 for ok, _, _ in LED if ok)
print("\n%d checks, %d pass, %d fail; runtime %.1f s" % (len(LED), npass, len(LED) - npass, time.time() - T0))
