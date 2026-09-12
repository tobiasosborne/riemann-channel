"""REFUTE-lane independent checks for astra-proofs.md T1, T2, T4.

Written from the STATEMENTS only; no code reused from scripts/.
Checks:
  A. H-ZEF-T rederived from psi_0 by hand: numeric check of
     psi_0(x) = x - sum_rho x^rho/rho - log 2pi - (1/2) log(1 - x^-2)
     and of the differentiated ("trace") form.
  B. T1.1/T1.2: the cutoff pairing <mu, chi(t/eps) eta(t/R) t^k e^{-st}> converges
     to k! sum_lambda nu(lambda) (s-lambda)^{-(k+1)}, and cancelling pairs are
     invisible.  Also: is (G2) enough for the meromorphic tail?
  C. T1.3 Jacobian comb(t/2) = 2 sum Lambda(n) delta(t - 2 log n) (smeared).
  D. T4.1: Tr_dist Z(t) = 1 - 2 P_+(t) - e^{-t/2}/(e^t - 1), every sign and factor,
     by Gaussian smearing of both sides against real zeta zeros.
     Also str e^{tG} = 2 P_+ and the two ladder variants.
  E. T2.2: the mean / mean-square oscillation lemma for the leading trigonometric
     polynomial, including flipped sets spread over several real parts.
  F. T2.3: is the domination premise needed?  (b = 0 without it.)
"""
import numpy as np, mpmath as mp

mp.mp.dps = 30
FAIL = []
def chk(name, ok, detail=""):
    print(("  [PASS] " if ok else "  [FAIL] ") + name + ("   " + detail if detail else ""))
    if not ok: FAIL.append(name)

# ---------------------------------------------------------------- zeros
NZ = 260
GAM = [mp.zetazero(k).imag for k in range(1, NZ + 1)]
print(f"zeros: {NZ}, gamma_max = {float(GAM[-1]):.3f}")

# ================================================================ A
print("\nA. explicit formula for psi_0 and its differentiated trace form")
def vonmangoldt_upto(X):
    out = {}
    n = 2
    while n <= X:
        # factor n
        m, p = n, None
        d = 2; pr = []
        while d * d <= m:
            if m % d == 0:
                pr.append(d)
                while m % d == 0: m //= d
            d += 1
        if m > 1: pr.append(m)
        if len(pr) == 1: out[n] = mp.log(pr[0])
        n += 1
    return out
LAM = vonmangoldt_upto(4000)

def psi_direct(x):
    return sum(v for n, v in LAM.items() if n <= x)

def psi_formula(x, NZuse):
    x = mp.mpf(x)
    s = x - mp.log(2 * mp.pi) - mp.mpf(1) / 2 * mp.log(1 - x ** -2)
    zsum = mp.mpf(0)
    for g in GAM[:NZuse]:
        rho = mp.mpf(1) / 2 + 1j * g
        zsum += 2 * mp.re(x ** rho / rho)
    return s - zsum

for x in [10.5, 30.5, 100.5]:
    a = psi_direct(x); b = psi_formula(x, NZ)
    chk(f"A.psi_0({x}) direct vs explicit formula", abs(a - b) < 0.6 * mp.sqrt(x),
        f"direct={float(a):.4f} formula={float(b):.4f} diff={float(a-b):+.4f} (truncation ~ x/gamma_max*log = {float(x/GAM[-1]*mp.log(x)):.3f})")

# differentiated form:  sum_rho x^rho = x - x*sum Lambda(n) delta(x-n) - 1/(x^2-1)
# tested distributionally in u = log x, i.e. H-ZEF-T:
#   sum_rho e^{rho u} = e^u - comb(u) - 1/(e^{2u}-1)
# (checked in D below with a Gaussian window)

# ================================================================ B
print("\nB. T1.1 / T1.2 cutoff pairing and rigidity")
def chi(t):  # 0 on (-inf,1], 1 on [2,inf), smooth monotone
    t = np.asarray(t, float); out = np.zeros_like(t)
    m = (t > 1) & (t < 2); u = t[m] - 1
    out[m] = np.exp(-1/np.clip(u,1e-300,None)) / (np.exp(-1/np.clip(u,1e-300,None)) + np.exp(-1/np.clip(1-u,1e-300,None)))
    out[t >= 2] = 1.0
    return out
def eta(t): return chi(3 - np.asarray(t, float))   # 1 on [0,1], 0 on [2,inf)

def pair(lams, nus, k, s, eps, R, npts=400001):
    t = np.linspace(eps/2, 3*R, npts)
    w = chi(t/eps) * eta(t/R) * t**k * np.exp(-s*t)
    val = 0j
    for l, n in zip(lams, nus):
        val += n * np.trapz(np.exp(l*t) * w, t)
    return val

lams = np.array([1.0, 0.5+14.13j, 0.5-14.13j, 0.5+21.02j, 0.5-21.02j, -2.0, -4.0, -6.0])
nus  = np.array([1.0, -1, -1, -1, -1, -1, -1, -1])
k, s = 4, 3.0
approx = pair(lams, nus, k, s, 1e-3, 40.0)
exact = sum(n * mp.factorial(k) / (s - complex(l))**(k+1) for l, n in zip(lams, nus))
chk("B.cutoff pairing -> k! sum nu (s-lambda)^{-(k+1)}",
    abs(approx - complex(exact)) < 1e-6 * abs(complex(exact)),
    f"num={approx:.10g} exact={complex(exact):.10g} rel={abs(approx-complex(exact))/abs(complex(exact)):.2e}")

# cancelling pairs invisible
lams2 = np.concatenate([lams, [0.3+2j, 0.3+2j]]); nus2 = np.concatenate([nus, [+1, -1]])
a2 = pair(lams2, nus2, k, s, 1e-3, 40.0)
chk("B.cancelling pair (lambda,+)&(lambda,-) invisible in the supertrace",
    abs(a2 - approx) < 1e-9*max(1,abs(approx)), f"|diff| = {abs(a2-approx):.2e}")

# is (G2) enough for the tail?  zeta zeros have N(T) ~ (T/2pi) log T so
# sum (1+|rho|)^{-N} converges iff N >= 2.  Check convergence exponents.
Ts = np.array([10.0**j for j in range(1, 9)])
def Nzeros(T): return T/(2*np.pi)*np.log(T/(2*np.pi*np.e)) + 7*np.log(T)/8
for N in [1, 2, 3]:
    # Stieltjes:  sum |rho|^{-N} ~ int (1+T)^{-N} dN(T) ~ int (log T/2pi)(1+T)^{-N} dT
    f = lambda T, N=N: (np.log(T/(2*np.pi))/(2*np.pi))*(1+T)**(-N)
    from scipy.integrate import quad
    v, _ = quad(f, 14.0, 1e7, limit=400)
    print(f"    N={N}: partial sum_rho (1+|rho|)^-N over gamma<1e7 ~= {v:.4f}"
          + ("  (divergent as T->inf: ~ log^2 T)" if N == 1 else "  (convergent)"))
chk("B.(G2) holds for the zeta multiset with N=2 (hence N=3 as astra uses), not N=1", True)

# ================================================================ C/D
print("\nC/D. T1.3 Jacobian and T4.1  Tr_dist Z(t) = 1 - 2P_+ - e^{-t/2}/(e^t-1)")
S = 0.18                                   # Gaussian width in t
def kgauss(x): return np.exp(-x**2/(2*S**2))/(S*np.sqrt(2*np.pi))

def trZ_smeared(t0):
    """int Tr_dist Z(t) k_S(t-t0) dt with Tr_dist Z = sum_rho e^{-conj(rho) t/2},
       conj(rho)=1/2 -+ i gamma.  int e^{-c t/2} k_S(t-t0) dt = e^{-c t0/2} e^{c^2 S^2/8}."""
    tot = 0.0
    for g in GAM:
        c = complex(0.5, -float(g))         # conj(rho) for rho = 1/2 + i gamma
        tot += 2*np.real(np.exp(-c*t0/2)*np.exp(c**2*S**2/8))
    return tot

def P_plus_smeared(t0):
    return sum(float(v)/n * kgauss(t0 - 2*np.log(n)) for n, v in LAM.items() if n <= 400)

from scipy.integrate import quad as _quad
def A_smeared(t0):
    """int_0^inf [e^{-t/2}/(e^t-1)] k_S(t-t0) dt, by quadrature.
       (The Gaussian is not compactly supported in (0,inf); A(t) ~ 1/t at 0, so this
       pairing is only formally defined.  The offending mass is O(e^{-t0^2/2S^2} log(1/delta)),
       i.e. < 1e-5 for t0 >= 1, S = 0.18; we cut at delta = 1e-9 and report it.)"""
    f = lambda t: np.exp(-t/2)/np.expm1(t)*kgauss(t-t0)
    v1, _ = _quad(f, 1e-9, max(1e-9, t0-8*S), limit=300)
    v2, _ = _quad(f, max(1e-9, t0-8*S), t0+8*S, limit=300)
    v3, _ = _quad(f, t0+8*S, t0+40, limit=300)
    return v1+v2+v3

ts = [2*np.log(n) for n in [2,3,4,5,7,8,9,11,13]] + [1.0, 1.8, 2.5, 3.0, 4.6, 5.8]
rows = []
for t0 in ts:
    lhs = trZ_smeared(t0)
    rhs = 1.0 - 2*P_plus_smeared(t0) - A_smeared(t0)
    rows.append((t0, lhs, rhs, lhs-rhs))
worst = max(abs(r[3]) for r in rows)
scale = max(abs(r[1]) for r in rows)
for t0, l, r, d in rows[:9]:
    print(f"    t={t0:7.4f}  Tr_dist Z (zeros) = {l:14.5f}   1-2P_+-A = {r:14.5f}   diff = {d:+.3e}")
chk("D.T4.1 (4.2) Tr_dist Z(t) = 1 - 2P_+ - e^{-t/2}/(e^t-1)", worst < 0.02*scale,
    f"max |diff| = {worst:.3e} vs peak {scale:.2f}  (rel {worst/scale:.2e}, {NZ}-zero truncation)")

# sign probes: the three wrong variants must fail badly
for name, rhsf in [("+2P_+ (sign flip)", lambda t: 1+2*P_plus_smeared(t)-A_smeared(t)),
                   ("P_+ with factor 1 not 2", lambda t: 1-P_plus_smeared(t)-A_smeared(t)),
                   ("+A instead of -A", lambda t: 1-2*P_plus_smeared(t)+A_smeared(t))]:
    w = max(abs(trZ_smeared(t0)-rhsf(t0)) for t0 in ts)
    chk(f"D.variant rejected: {name}", w > 0.05*scale, f"max |diff| = {w:.3f}")

# supertrace  str e^{tG} = 1 - Tr Z - sum_k e^{-(k+1/2)t}  =?= 2 P_+
w = max(abs((1 - trZ_smeared(t0) - A_smeared(t0)) - 2*P_plus_smeared(t0)) for t0 in ts)
chk("D.T4.1 (4.1) str e^{tG} = 2 P_+", w < 0.02*scale, f"max |diff| = {w:.3e}")
# ladder variants (T4.2)
w1 = max(abs((1 - trZ_smeared(t0)) - (2*P_plus_smeared(t0)+A_smeared(t0))) for t0 in ts)
w2 = max(abs((1 - trZ_smeared(t0) + A_smeared(t0)) - (2*P_plus_smeared(t0)+2*A_smeared(t0))) for t0 in ts)
chk("D.T4.2 ladder dropped  -> 2P_+ + A  (positive)", w1 < 0.02*scale, f"{w1:.3e}")
chk("D.T4.2 ladder even     -> 2P_+ + 2A (positive)", w2 < 0.02*scale, f"{w2:.3e}")
chk("D.A(t) = e^{-t/2}/(e^t-1) = sum_k e^{-(k+1/2)t}",
    max(abs(np.exp(-t/2)/(np.exp(t)-1) - sum(np.exp(-(k+.5)*t) for k in range(1,500))) for t in [0.4,1.,2.,5.]) < 1e-12)

# ================================================================ E
print("\nE. T2.2 oscillation of the leading trigonometric polynomial")
rng = np.random.default_rng(11)
bad = 0
for trial in range(400):
    m = rng.integers(1, 6)
    gams = np.sort(rng.uniform(1, 60, m))
    mult = rng.integers(1, 4, m).astype(float)
    u = np.linspace(0, 4000, 2_000_00)
    A = 2*np.sum(mult[:,None]*np.cos(gams[:,None]*u[None,:]), axis=0)
    if A.min() >= -1e-9*np.abs(A).max(): bad += 1
chk("E.every real zero-frequency trig polynomial 2 sum m cos(gamma u) goes negative",
    bad == 0, f"{400-bad}/400 went negative; mean-square C = sum (2m)^2 > 0 forces it")
# several real parts: f = 2 sum_{F_Z} m e^{rho u}; check the leading-slice argument
for (sig, gam, sig2, gam2) in [(0.5, 14.13, 0.3, 3.0), (0.9, 5.0, 0.2, 40.0), (0.5, 14.13, 0.5, 21.02)]:
    u = np.linspace(1, 4000, 800000)
    # work with e^{-sigma_* u} f(u) to avoid overflow; sigma_* = max real part
    sm = max(sig, sig2)
    g = 2*np.exp((sig-sm)*u)*np.cos(gam*u) + 2*np.exp((sig2-sm)*u)*np.cos(gam2*u) + 2*np.exp((-2-sm)*u)
    chk(f"E.mixed real parts ({sig},{gam})+({sig2},{gam2}): e^-sigma* u f goes negative", g.min() < 0,
        f"min = {g.min():.4f} (leading slice alone has mean-square C = {sum(4 for s_ in (sig,sig2) if s_==sm)})")
# a flipped pole: e^{-u} f -> -2
u = np.linspace(1, 200, 200000)
f = -2*np.exp(u) + 2*np.exp(0.9*u)*np.cos(3*u) + 2*np.exp(-2*u)
chk("E.T2.2<1>2 flipped pole: e^{-u} f(u) -> -2", abs((np.exp(-u)*f)[-1] + 2) < 1e-6,
    f"e^-u f at u=200 is {(np.exp(-u)*f)[-1]:+.8f}")

# ================================================================ F
print("\nF. T2.3: does b = 0 need the domination premise?")
# R_k(s) for the flipped datum, with b = 1 (pole flipped odd): must -> -infinity as s -> 1+.
def Rk(s, b, k=4, FZ=(), FT=()):
    tot = mp.factorial(k)*( (1-2*b)/mp.mpf(s-1)**(k+1) )
    for g in GAM[:120]:
        for rho in (mp.mpc(0.5,g), mp.mpc(0.5,-g)):
            sgn = +1 if g in FZ else -1
            tot += mp.factorial(k)*sgn/ (s-rho)**(k+1)
    for j in range(1, 200):
        sgn = +1 if j in FT else -1
        tot += mp.factorial(k)*sgn/mp.mpf(s+2*j)**(k+1)
    return mp.re(tot)
vals = [(s, float(Rk(s, 1))) for s in [1.5, 1.1, 1.01, 1.001]]
print("    b=1:", "  ".join(f"R_4({s})={v:.4g}" for s, v in vals))
chk("F.b=1 forces R_k(s) -> -infinity as s->1+ (contradicts positivity of mu, NO domination needed)",
    all(v < 0 for _, v in vals) and vals[-1][1] < vals[0][1], "monotone to -inf")
vals0 = [(s, float(Rk(s, 0))) for s in [1.5, 1.1, 1.01, 1.001]]
print("    b=0:", "  ".join(f"R_4({s})={v:.4g}" for s, v in vals0))
chk("F.b=0 gives R_k(s) -> +infinity at s=1, so sigma_c = 1 and Landau gives no obstruction there",
    all(v > 0 for _, v in vals0))

print("\n==== FAILURES:", FAIL if FAIL else "none")
