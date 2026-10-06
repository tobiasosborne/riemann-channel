#!/usr/bin/env python3
"""Checks for data-ladder.md section 4b, zeta bullet: 'the prime steps are large powers of the generator D, as F^2 is of F'.  2026-10-06.

Conventions.  Omega(x, y) = x^T Omega y;  F = M, V = q M^{-1};  Weil form of the k-th power  W_k = (1/2) Omega (F^k - V^k).
  Per mode (M = sqrt(q) e^{i theta} on a plane with Krein sign +1): F^k = q^{k/2}(cos k theta + sin k theta J), V^k = q^{k/2}(cos k theta - sin k theta J),
  so W_k = q^{k/2} sin(k theta) G_J with G_J = Omega J the vacuum form.
P1 one mode;  P2 the genus-2 curve y^2 = x^5 + x^3 + x^2 - 2 over F_5 and K_4 with one negative edge (inertia of W_k);
P3 zeta in the spectral model (generator D with frequencies gamma_n, first 200 zeros);  P4 smallest k >= 2 with W_k indefinite.
numpy / sympy / scipy only.  Run time a few seconds.
"""
import os
import numpy as np
import sympy as sp
from scipy.linalg import expm

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


def isprime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def inertia(W, tol=1e-9):
    """(n_plus, n_minus, n_zero) of a symmetric matrix, eigenvalues compared to tol * max|eig|"""
    ev = np.linalg.eigvalsh((W + W.T) / 2)
    s = tol * max(1.0, np.max(np.abs(ev)))
    return int(np.sum(ev > s)), int(np.sum(ev < -s)), int(np.sum(np.abs(ev) <= s))


_cache = {}


def weil_k(M, Om, q, k):
    """exact (sympy, rational) W_k = (1/2) Omega (M^k - V^k), V = q M^{-1}; returns a float array.  Powers are cached per (M, Omega)."""
    key = (tuple(M), tuple(Om), k)
    if key not in _cache:
        Vm = q * M.inv()
        Pm = sp.eye(M.shape[0])
        Pv = sp.eye(M.shape[0])
        for j in range(1, 13):
            Pm, Pv = Pm * M, Pv * Vm
            _cache[(tuple(M), tuple(Om), j)] = np.array((Om * (Pm - Pv) / 2).tolist(), dtype=float)
    return _cache[key]


# ---------------------------------------------------------------------------------------------
print("== P1  one mode: W_k = q^{k/2} sin(k theta) G_J")
Om2 = np.array([[0.0, 1.0], [-1.0, 0.0]])
signs_table = {}
for q, lam in [(2, -1), (5, -2), (7, 2), (13, 3)]:
    M = np.array([[0.0, -1.0], [q, lam]])
    V = q * np.linalg.inv(M)
    Om = Om2.copy()
    flipped = False
    if np.min(np.linalg.eigvalsh(0.5 * (0.5 * Om @ (M - V) + (0.5 * Om @ (M - V)).T))) < 0:
        Om = -Om
        flipped = True
    W1 = 0.5 * Om @ (M - V)
    th = np.arccos(lam / (2 * np.sqrt(q)))
    J = (M - V) / np.sqrt(4 * q - lam ** 2)
    G = Om @ J
    check(f"P1 (q,lambda)=({q},{lam}): Omega oriented so that W_1 > 0 (flipped: {flipped}); G_J = Omega J symmetric positive definite, "
          f"M^T Omega M = q Omega, theta = {th/np.pi:.5f} pi",
          np.all(np.linalg.eigvalsh(W1) > 0) and np.allclose(W1, W1.T) and np.allclose(G, G.T) and np.all(np.linalg.eigvalsh(G) > 0)
          and np.allclose(M.T @ Om @ M, q * Om))
    errs = []
    sg = []
    defin = True
    for k in range(1, 7):
        Wk = 0.5 * Om @ (np.linalg.matrix_power(M, k) - np.linalg.matrix_power(V, k))
        errs.append(np.max(np.abs(Wk - q ** (k / 2) * np.sin(k * th) * G)))
        sg.append(int(np.sign(np.sin(k * th))))
        ev = np.linalg.eigvalsh((Wk + Wk.T) / 2)
        defin &= bool(np.all(np.sign(ev) == np.sign(np.sin(k * th))) and abs(np.sin(k * th)) > 1e-6)
    signs_table[(q, lam)] = sg
    check(f"P1 (q,lambda)=({q},{lam}): W_k = q^(k/2) sin(k theta) G_J for k = 1..6 to 1e-10; each W_k definite of the sign of sin(k theta)",
          max(errs) < 1e-10 and defin, f"max err {max(errs):.1e}; sign sin(k theta), k=1..6: {['+' if s > 0 else '-' for s in sg]}")
print("      sign of sin(k theta), k = 1..6:")
for key, sg in signs_table.items():
    print(f"        (q,lambda)={key}: " + " ".join('+' if s > 0 else '-' for s in sg))
check("P1 W_1 is positive for all four (sin theta > 0 by construction of the orientation); in every case some k <= 6 has sign - (so W_k negative definite there)",
      all(sg[0] > 0 for sg in signs_table.values()) and all(-1 in sg for sg in signs_table.values()))

# ---------------------------------------------------------------------------------------------
print("\n== P2a  genus-2 curve: companion step of P(T) = 1 - 3T + 7T^2 - 15T^3 + 25T^4 over F_5")
x = sp.symbols("x")
q = 5
chi = x ** 4 - 3 * x ** 3 + 7 * x ** 2 - 15 * x + 25          # x^4 P(1/x)
Mc = sp.Matrix([[0, 0, 0, -25], [1, 0, 0, 15], [0, 1, 0, -7], [0, 0, 1, 3]])   # companion matrix of chi
check("P2a companion matrix has characteristic polynomial x^4 - 3x^3 + 7x^2 - 15x + 25 and det = q^2 = 25",
      sp.expand(Mc.charpoly(x).as_expr() - chi) == 0 and Mc.det() == 25)
# alternating Omega with M^T Omega M = q Omega
syms = sp.symbols("w01 w02 w03 w12 w13 w23")
Oa = sp.zeros(4)
idx = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
for s_, (i, j) in zip(syms, idx):
    Oa[i, j] = s_
    Oa[j, i] = -s_
eqs = list(Mc.T * Oa * Mc - q * Oa)
sol = sp.linsolve([e for e in eqs if e != 0], *syms)
sol = list(sol)[0]
free = sorted(set().union(*[v.free_symbols for v in sol]), key=str)
basis = []
for f in free:
    sub = {g: (1 if g == f else 0) for g in free}
    basis.append(sp.Matrix(4, 4, lambda i, j: 0) + Oa.subs(dict(zip(syms, [v.subs(sub) for v in sol]))))
check("P2a compatible alternating forms (M^T Omega M = q Omega) form a 2-dimensional space (g = 2)", len(basis) == 2, f"dimension {len(basis)}")
Vc = q * Mc.inv()
Wlin = [np.array((B * (Mc - Vc) / 2).tolist(), dtype=float) for B in basis]
best = (-1e99, None)
for phi in np.linspace(0, 2 * np.pi, 7201):
    Wt = np.cos(phi) * Wlin[0] + np.sin(phi) * Wlin[1]
    Wt = (Wt + Wt.T) / 2
    m = np.min(np.linalg.eigvalsh(Wt)) / np.linalg.norm(Wt, 2)
    if m > best[0]:
        best = (m, phi)
phi = best[1]
# pick an exact rational combination near the best angle
a1, a2 = sp.Rational(round(np.cos(phi) * 100), 100), sp.Rational(round(np.sin(phi) * 100), 100)
Omc = a1 * basis[0] + a2 * basis[1]
Wc1 = weil_k(Mc, Omc, q, 1)
check("P2a a compatible alternating Omega exists whose Weil form (1/2)Omega(F - V) is positive definite (rational coefficients a1, a2 = "
      f"{a1}, {a2})",
      np.all(np.linalg.eigvalsh((Wc1 + Wc1.T) / 2) > 1e-6) and Mc.T * Omc * Mc == q * Omc and Omc.T == -Omc,
      f"eigenvalues of W_1: {np.round(np.linalg.eigvalsh((Wc1 + Wc1.T) / 2), 4)}")
ev = np.linalg.eigvals(np.array(Mc.tolist(), dtype=float))
thc = np.sort(np.angle(ev[np.imag(ev) > 0]))
lamc = np.sort(2 * np.sqrt(q) * np.cos(thc))
check("P2a the eigenvalues of M are sqrt(5) e^{+-i theta_j}, theta_j/pi = 0.17795, 0.55662; lambda_j = (3 +- sqrt 21)/2",
      np.allclose(np.abs(ev), np.sqrt(q)) and np.allclose(thc / np.pi, [0.17795, 0.55662], atol=1e-5)
      and np.allclose(np.sort(lamc), [(3 - np.sqrt(21)) / 2, (3 + np.sqrt(21)) / 2]),
      f"theta/pi = {np.round(thc/np.pi, 5)}")

# ---------------------------------------------------------------------------------------------
print("\n== P2b  K_4 with one negative edge (q = 2): M = [[0,-I],[2I,A_s]], standard Omega")
As = sp.ones(4) - sp.eye(4)
As[0, 1] = As[1, 0] = -1
q4 = 2
Mk = sp.Matrix(sp.BlockMatrix([[sp.zeros(4), -sp.eye(4)], [q4 * sp.eye(4), As]]))
Omk = sp.Matrix(sp.BlockMatrix([[sp.zeros(4), sp.eye(4)], [-sp.eye(4), sp.zeros(4)]]))
check("P2b M^T Omega M = 2 Omega; characteristic polynomial (x^4 + 3x^2 + 4)(x^4 - x^2 + 4)",
      Mk.T * Omk * Mk == q4 * Omk and sp.expand(Mk.charpoly(x).as_expr() - (x ** 4 + 3 * x ** 2 + 4) * (x ** 4 - x ** 2 + 4)) == 0)
evk = np.linalg.eigvals(np.array(Mk.tolist(), dtype=float))
thk = np.sort(np.angle(evk[np.imag(evk) > 1e-9]))
check("P2b the four angles are theta/pi = 0.210, 0.385, 0.615, 0.790 (lattice-tower.md section 5), all eigenvalues of modulus sqrt 2",
      np.allclose(np.abs(evk), np.sqrt(2)) and len(thk) == 4 and np.allclose(thk / np.pi, [0.210, 0.385, 0.615, 0.790], atol=6e-4),
      f"theta/pi = {np.round(thk/np.pi, 4)}")
Wk1 = weil_k(Mk, Omk, q4, 1)
check("P2b W_1 = (1/2)Omega(F - V) = [[2I, A_s/2],[A_s/2, I]] is positive definite",
      np.all(np.linalg.eigvalsh(Wk1) > 1e-6) and np.allclose(Wk1[:4, :4], 2 * np.eye(4)) and np.allclose(Wk1[:4, 4:], np.array(As.tolist(), float) / 2),
      f"min eigenvalue {np.min(np.linalg.eigvalsh(Wk1)):.4f}")

print("\n  inertia of W_k = (1/2) Omega (F^k - V^k), k = 1..6, against the number of modes with sin(k theta_j) > 0 / < 0 (each mode is a plane: 2 dimensions)")
tables = {}
for name, Msym, Osym, qq, th, g in [("curve", Mc, Omc, 5, thc, 2), ("K_4", Mk, Omk, 2, thk, 4)]:
    rows = []
    ok_all = True
    ok_ratio = True
    W1 = weil_k(Msym, Osym, qq, 1)
    for k in range(1, 7):
        Wk = weil_k(Msym, Osym, qq, k)
        inn = inertia(Wk / qq ** (k / 2))
        sk = np.sin(k * th)
        pred = (2 * int(np.sum(sk > 1e-9)), 2 * int(np.sum(sk < -1e-9)), 2 * int(np.sum(np.abs(sk) <= 1e-9)))
        ok_all &= (inn == pred)
        # W_1^{-1} W_k has eigenvalue q^{(k-1)/2} sin(k theta_j)/sin(theta_j) on mode j
        ev_ = np.sort(np.linalg.eigvals(np.linalg.solve(W1, Wk)).real)
        pe = np.sort(np.repeat(qq ** ((k - 1) / 2) * np.sin(k * th) / np.sin(th), 2))
        ok_ratio &= np.allclose(ev_, pe, rtol=1e-8, atol=1e-8 * qq ** (k / 2))
        rows.append((k, inn, pred, "".join('+' if s > 0 else '-' for s in sk)))
    tables[name] = rows
    check(f"P2 {name}: inertia (n+, n-, n0) of W_k equals 2 x (#modes with sin(k theta_j) >0, <0, =0) for k = 1..6", ok_all)
    check(f"P2 {name}: the eigenvalues of W_1^(-1) W_k are q^((k-1)/2) sin(k theta_j)/sin(theta_j), each twice (W_k = sum_j q^(k/2) sin(k theta_j) G_J|_j), k = 1..6", ok_ratio)
    print(f"      {name}: theta_j/pi = {np.round(th/np.pi, 4)}")
    for k, inn, pred, sg in rows:
        print(f"        k = {k}: signs of sin(k theta_j) = {sg}; inertia (n+, n-, n0) = {inn}; predicted {pred}; {'definite' if (inn[1] == 0 and inn[2] == 0) or (inn[0] == 0 and inn[2] == 0) else 'INDEFINITE' if inn[0] and inn[1] else 'degenerate'}")
check("P2 curve: sin(2 theta_j) has both signs (2 theta_1 = 0.356 pi, 2 theta_2 = 1.113 pi), so W_2 is indefinite with inertia (2, 2, 0)",
      tables["curve"][1][1] == (2, 2, 0), f"inertia {tables['curve'][1][1]}")
check("P2 K_4: sin(2 theta_j) has both signs (2 theta/pi = 0.42, 0.77, 1.23, 1.58), so W_2 is indefinite with inertia (4, 4, 0)",
      tables["K_4"][1][1] == (4, 4, 0), f"inertia {tables['K_4'][1][1]}")
check("P2 W_1 positive (inertia (2g, 0, 0)) for both",
      tables["curve"][0][1] == (4, 0, 0) and tables["K_4"][0][1] == (8, 0, 0))

# ---------------------------------------------------------------------------------------------
print("\n== P3  zeta in the spectral model: D = (+) gamma_n [[0,-1],[1,0]], Omega_FE = standard form per pair, vacuum G = (+) I_2")
zeros = np.load(os.path.join(ROOT, "data", "zeros3000.npy"))
N = 200
gam = zeros[:N]
rot = np.array([[0.0, -1.0], [1.0, 0.0]])
Omn = np.kron(np.eye(N), np.array([[0.0, 1.0], [-1.0, 0.0]]))
D = np.kron(np.diag(gam), rot)


_wd = {}


def weil_D(t, via_expm=False):
    if (t, via_expm) not in _wd:
        _wd[(t, via_expm)] = _weil_D(t, via_expm)
    return _wd[(t, via_expm)]


def _weil_D(t, via_expm=False):
    E = expm(t * D) if via_expm else np.kron(np.diag(np.cos(gam * t)), np.eye(2)) + np.kron(np.diag(np.sin(gam * t)), rot)
    Einv = expm(-t * D) if via_expm else E.T
    return 0.5 * Omn @ (E - Einv)


check("P3 the first 200 zeros: gamma_1 = 14.1347, gamma_200 = 396.3819, increasing",
      abs(gam[0] - 14.134725) < 1e-5 and abs(gam[-1] - 396.381854) < 1e-5 and np.all(np.diff(gam) > 0))
t_test = 0.37
check("P3 e^{tD} is the pair-wise rotation by gamma_n t (scipy expm against the closed form) and its Weil form is (+) sin(gamma_n t) I_2",
      np.allclose(weil_D(t_test, True), weil_D(t_test), atol=1e-10)
      and np.allclose(weil_D(t_test), np.kron(np.diag(np.sin(gam * t_test)), np.eye(2)), atol=1e-12))
# (a)
ev_small = {}
for t in (1e-6, 1e-8):
    Wn = weil_D(t, True) / t
    ev_small[t] = np.linalg.eigvalsh(Wn)
    rel = np.max(np.abs(np.diag(Wn)[::2] / gam - 1))
    check(f"P3a t = {t:g}: (1/t)(1/2)Omega(e^(tD) - e^(-tD)) -> (+) gamma_n I_2 (max relative deviation of the diagonal {rel:.1e}), positive definite, off-diagonal blocks zero",
          rel < 1e-6 and np.all(ev_small[t] > 0) and np.allclose(Wn, np.kron(np.diag(np.diag(Wn)[::2]), np.eye(2)), atol=1e-6 * gam[-1]),
          f"min eigenvalue {ev_small[t].min():.4f} (gamma_1 = {gam[0]:.4f}), max {ev_small[t].max():.4f}")
check("P3a the weights are |gamma_n| > 0: D itself has a positive Weil form (t = 1e-8: eigenvalues are gamma_n, each twice)",
      np.allclose(ev_small[1e-8], np.repeat(gam, 2), rtol=1e-6))
# (b)
frac = {}
for p in (2, 3, 5):
    S = np.sin(gam * np.log(p))
    frac[p] = float(np.mean(S > 0))
    S3 = np.sin(zeros * np.log(p))
    print(f"      t = log {p} = {np.log(p):.4f}: fraction of the first 200 pairs with sin(gamma_n t) > 0 = {frac[p]:.3f} ({int(np.sum(S>0))} +, {int(np.sum(S<0))} -); "
          f"over 3000 zeros: {np.mean(S3 > 0):.3f}")
check("P3b fraction of pairs with sin(gamma_n log p) > 0 is near one half for p = 2, 3, 5 (within [0.4, 0.6])", all(0.4 < f < 0.6 for f in frac.values()),
      ", ".join(f"p={p}: {f:.3f}" for p, f in frac.items()))
inn3 = {p: inertia(weil_D(np.log(p))) for p in (2, 3, 5)}
check("P3b the Weil forms of e^{tD}, t = log 2, log 3, log 5, are indefinite (both signs among the 200 pairs, none zero), via inertia of the 400 x 400 matrices",
      all(v[0] > 0 and v[1] > 0 and v[2] == 0 for v in inn3.values()), ", ".join(f"p={p}: inertia {v}" for p, v in inn3.items()))
# (c)
gmax = gam[-1]
tstar = np.pi / gmax
eps = 1e-9
check(f"P3c the Weil form of e^(tD) is positive definite for 0 < t < pi/gamma_200 = {tstar:.6f} and the pair 200 turns negative just above it (sin(gamma_200 t) > 0 below, < 0 above, all other sin > 0 up to t*)",
      np.all(np.sin(gam * tstar * (1 - eps)) > 0) and np.sin(gmax * tstar * (1 + eps)) < 0 and np.all(np.sin(gam * np.linspace(1e-7, tstar * (1 - eps), 20000)[:, None]) > 0),
      f"t* = pi/gamma_200 = {tstar:.6f} (about 0.0079)")
tgrid = np.arange(tstar * (1 + 1e-6), 10.0, 1e-4)
npos = np.zeros(len(tgrid), int)
for a in range(0, len(tgrid), 5000):
    npos[a:a + 5000] = np.sum(np.sin(np.outer(tgrid[a:a + 5000], gam)) > 0, axis=1)
check(f"P3c the Weil form of e^(tD) is indefinite (both signs, 200 pairs) at all {len(tgrid)} grid points t in (pi/gamma_200, 10], step 1e-4",
      np.all((npos > 0) & (npos < N)), f"min #positive = {npos.min()}, max #positive = {npos.max()} of {N}")
nontriv = tgrid[(npos > 0) & (npos < N)]
print(f"      #positive pairs over the grid t in (t*, 10]: min {npos.min()}, max {npos.max()}; the grid point with fewest negative pairs is t = {tgrid[np.argmax(npos)]:.4f} ({N - npos.max()} negative)")
primes = [p for p in range(2, 100000) if isprime(p)]
lp = np.log(np.array(primes, float))
pp = np.zeros(len(primes), int)
for a in range(0, len(primes), 2000):
    pp[a:a + 2000] = np.sum(np.sin(np.outer(lp[a:a + 2000], gam)) > 0, axis=1)
definite = [p for p, c in zip(primes, pp) if c == 0 or c == N]
check(f"P3c no prime p < 10^5 ({len(primes)} primes) has a definite Weil form for e^(t D), t = log p, on the first 200 pairs (smallest prime-like t with definite form: none)",
      len(definite) == 0, f"min #positive pairs {pp.min()} (p = {primes[int(np.argmin(pp))]}), max {pp.max()} (p = {primes[int(np.argmax(pp))]}) of {N}; "
      f"fraction positive over primes: mean {pp.mean()/N:.3f}")
allint = np.arange(2, 100000)
lq = np.log(allint.astype(float))
qq_ = np.zeros(len(allint), int)
for a in range(0, len(allint), 2000):
    qq_[a:a + 2000] = np.sum(np.sin(np.outer(lq[a:a + 2000], gam)) > 0, axis=1)
check("P3c likewise for t = log n for every integer 2 <= n < 10^5 (prime powers and composites included): none definite",
      not np.any((qq_ == 0) | (qq_ == N)), f"min #positive {qq_.min()}, max {qq_.max()} of {N}")
check("P3c the smallest t with an indefinite form is t* = pi/gamma_200 = 0.0079, 88 times smaller than log 2 = 0.693; log 2 > t* and every log p > log 2",
      tstar < 0.008 and np.log(2) / tstar > 80, f"log 2 / t* = {np.log(2)/tstar:.1f}")

# ---------------------------------------------------------------------------------------------
print("\n== P4  smallest k >= 2 with W_k indefinite")
for name, Msym, Osym, qq, th in [("curve", Mc, Omc, 5, thc), ("K_4", Mk, Omk, 2, thk)]:
    kmin = None
    for k in range(2, 13):
        inn = inertia(weil_k(Msym, Osym, qq, k) / qq ** (k / 2))
        if inn[0] and inn[1]:
            kmin = k
            break
    pred = next(k for k in range(2, 13) if np.any(np.sin(k * th) > 1e-9) and np.any(np.sin(k * th) < -1e-9))
    check(f"P4 {name}: the smallest k >= 2 with W_k indefinite is k = 2 (numerical inertia up to k = 12; angle prediction k = {pred})", kmin == 2 and pred == 2,
          f"numerical k_min = {kmin}")
check("P4 one mode (P1): W_k is never indefinite (scalar times G_J), but it is negative definite when sin(k theta) < 0 (see the sign table); "
      "indefiniteness needs two modes of opposite sign, as for the curve and K_4",
      all(-1 in sg for sg in signs_table.values()))

print(f"\n{npass} of {npass + nfail} pass")
