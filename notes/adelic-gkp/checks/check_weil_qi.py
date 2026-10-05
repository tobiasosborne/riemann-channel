#!/usr/bin/env python3
"""Checks and figures for 'Weil positivity as squeeze spectroscopy of the adelic GKP code'.

Conventions. t = log of the real squeeze. Wavepacket h(t), H(E) = int h(t) e^{iEt} dt.
g = h * h~ has G(E) = H(E) conj(H(conj E)).  Zeros rho = 1/2 + i gamma.
Echo  C_h(t) = sum_rho G(gamma) e^{i gamma t};  Z(h) = C_h(0).
Explicit formula (Guinand-Weil), applied to g(. - t):
  C_h(t) = G(i/2) e^{-t/2} + G(-i/2) e^{t/2}
           - sum_n Lambda(n) n^{-1/2} [ g(log n - t) + g(-log n - t) ]
           + (1/2pi) int G(E) e^{iEt} [ Re psi(1/4 + iE/2) - log pi ] dE .
Gaussian packet: h(t) = exp(-t^2/2tau^2) exp(-i E0 t), G(E) = 2 pi tau^2 exp(-tau^2 (E-E0)^2),
g(u) = tau sqrt(pi) exp(-i E0 u) exp(-u^2/4tau^2).
"""
import os
import numpy as np
import mpmath as mp
from scipy.special import digamma
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
NOTE = os.path.dirname(HERE)          # figures are written next to the note
ZEROS = np.load(os.path.join(NOTE, "..", "..", "data", "zeros3000.npy"))
ALLZ = np.concatenate([ZEROS, -ZEROS]).astype(complex)
LOGPI = np.log(np.pi)
npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


def trapz(y, x):
    return np.sum((y[1:] + y[:-1]) * np.diff(x)) / 2


def mangoldt(N):
    """prime powers n <= N with Lambda(n)"""
    sieve = np.ones(N + 1, bool)
    sieve[:2] = False
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    primes = np.nonzero(sieve)[0]
    ns, ls = [primes.astype(float)], [np.log(primes)]
    for p in primes[primes <= int(N ** 0.5)]:
        q = int(p) * int(p)
        while q <= N:
            ns.append(np.array([float(q)]))
            ls.append(np.array([np.log(p)]))
            q *= int(p)
    n = np.concatenate(ns)
    lam = np.concatenate(ls)
    o = np.argsort(n)
    return n[o], lam[o]


def G(E, E0, tau):
    return 2 * np.pi * tau ** 2 * np.exp(-tau ** 2 * (E - E0) ** 2)


def g_time(u, E0, tau):
    return tau * np.sqrt(np.pi) * np.exp(-1j * E0 * u) * np.exp(-u ** 2 / (4 * tau ** 2))


def echo_zeros(t, E0, tau, gam=ALLZ):
    t = np.atleast_1d(t).astype(float)
    return (G(gam[:, None], E0, tau) * np.exp(1j * gam[:, None] * t[None, :])).sum(0)


def arch_density(E):
    """(1/2pi)(Re psi(1/4 + iE/2) - log pi) = theta'(E)/pi"""
    return (digamma(0.25 + 0.5j * E).real - LOGPI) / (2 * np.pi)


def echo_places(t, E0, tau, PN, PL, parts=False):
    t = np.atleast_1d(t).astype(float)
    pole = G(0.5j, E0, tau) * np.exp(-t / 2) + G(-0.5j, E0, tau) * np.exp(t / 2)
    ln = np.log(PN)[:, None]
    w = (PL / np.sqrt(PN))[:, None]
    prime = -(w * (g_time(ln - t[None, :], E0, tau) + g_time(-ln - t[None, :], E0, tau))).sum(0)
    E = np.linspace(E0 - 14 / tau, E0 + 14 / tau, 40001)
    arch = np.array([trapz(G(E, E0, tau) * np.exp(1j * E * tt) * arch_density(E), E) for tt in t])
    return (pole, prime, arch) if parts else pole + prime + arch


# ---------------------------------------------------------------------------------------------
print("== V1  the code is a filter: spectrum of the squeeze signal of the probe g4 is -Xi(E)/(6 pi)")
def g4(x):
    return np.exp(-np.pi * x ** 2) * (x ** 2 - (2 * np.pi / 3) * x ** 4)

check("V1 probe has no zero modes: g4(0) = 0", g4(0.0) == 0.0)
xx = np.linspace(-8, 8, 160001)
check("V1 probe has no zero modes: int g4 = 0", abs(trapz(g4(xx), xx)) < 1e-14, f"{trapz(g4(xx), xx):.1e}")
tt = np.linspace(-3.5, 3.5, 14001)
lam = np.exp(tt)
S = np.sqrt(lam) * g4(np.arange(1, 401)[:, None] * lam[None, :]).sum(0)   # overlap with the half comb
def Xi(E):
    s = mp.mpf(1) / 2 + 1j * mp.mpf(E)
    return complex(0.5 * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s))
for E in [0.0, 5.0, 10.0, 17.0, 23.0]:
    F = trapz(S * np.exp(1j * E * tt), tt)
    ex = -Xi(E) / (6 * np.pi)
    check(f"V1 signal spectrum at E = {E:g}", abs(F - ex) < 1e-13, f"num {F.real:+.6e}, -Xi/6pi {ex.real:+.6e}")
for k in range(2):
    F = trapz(S * np.exp(1j * ZEROS[k] * tt), tt)
    ref = abs(Xi(ZEROS[k] + 1.0)) / (6 * np.pi)
    check(f"V1 dark line at gamma_{k+1} = {ZEROS[k]:.4f}", abs(F) < 1e-8 * ref, f"|F| = {abs(F):.1e}, vs {ref:.1e} one unit away")

# ---------------------------------------------------------------------------------------------
print("== V2  explicit formula in echo form: zeros side = place-by-place side")
PN, PL = mangoldt(200000)
E0, tau = 25.0, 0.25
ts = np.array([0.0, 0.3, 0.7, np.log(2), 1.0, np.log(3), 1.7, 2.5, 4.0])
cz = echo_zeros(ts, E0, tau)
pole, prime, arch = echo_places(ts, E0, tau, PN, PL, parts=True)
cp = pole + prime + arch
check("V2 echo, wide packet (E0 = 25, tau = 0.25), nine values of t", np.max(np.abs(cz - cp)) < 1e-9,
      f"max |diff| = {np.max(np.abs(cz - cp)):.1e}, C(0) = {cz[0].real:.6f}")
print(f"      at t = 0: zero modes {pole[0].real:+.3e}, primes {prime[0].real:+.6f}, real place {arch[0].real:+.6f}")
E0b, taub = 21.0, 1.0
czb = echo_zeros(np.array([0.0, 1.0]), E0b, taub)
cpb = echo_places(np.array([0.0, 1.0]), E0b, taub, PN, PL)
check("V2 echo, narrow packet (E0 = 21, tau = 1)", np.max(np.abs(czb - cpb)) < 1e-7, f"max |diff| = {np.max(np.abs(czb - cpb)):.1e}")
E0c, tauc = 2.0, 0.6     # near E = 0: the zero-mode term is not negligible here
czc = echo_zeros(np.array([0.0, 0.8]), E0c, tauc)
pc, prc, ac = echo_places(np.array([0.0, 0.8]), E0c, tauc, PN, PL, parts=True)
check("V2 echo, packet near E = 0 (zero modes matter)", np.max(np.abs(czc - (pc + prc + ac))) < 1e-7,
      f"max |diff| = {np.max(np.abs(czc - (pc + prc + ac))):.1e}; zero-mode term {pc[0].real:+.4f}, total {czc[0].real:+.2e}")

# ---------------------------------------------------------------------------------------------
print("== V3  Weil positivity as a Gram matrix / echo bound, computed from the place side only")
nG, dT = 14, 0.35
tgrid = np.arange(0, nG) * dT
cgrid = echo_places(tgrid, E0, tau, PN, PL)
def toeplitz(c):
    n = len(c)
    M = np.empty((n, n), complex)
    for j in range(n):
        for k in range(n):
            d = j - k
            M[j, k] = c[d] if d >= 0 else np.conj(c[-d])
    return M
M = toeplitz(cgrid)
ev = np.linalg.eigvalsh(M)
check("V3 Gram matrix [C(t_j - t_k)] is Hermitian", np.max(np.abs(M - M.conj().T)) < 1e-12)
check("V3 Gram matrix is positive semidefinite (14 x 14, step 0.35)", ev.min() > -1e-9, f"eigenvalues in [{ev.min():.3e}, {ev.max():.3f}]")
tfine = np.linspace(0, 6, 601)
cfine = echo_places(tfine, E0, tau, PN, PL)
check("V3 echo bound |C(t)| <= C(0) on [0, 6]", np.max(np.abs(cfine)) <= abs(cfine[0]) + 1e-9, f"max |C(t)|/C(0) for t >= 0.5: {np.max(np.abs(cfine[50:])) / abs(cfine[0]):.4f}")

# ---------------------------------------------------------------------------------------------
print("== V4  a made-up line list with one off-line pair: Weil form versus Lorentzian form")
ia, ib = 3, 4                       # gamma_4 = 30.4249, gamma_5 = 32.9351 merge and leave the axis
g0, eta = 0.5 * (ZEROS[ia] + ZEROS[ib]), 0.8
E0f, tauf = g0, 0.3
PNf, PLf = PN, PL
def echo_true(t):
    return echo_places(t, E0f, tauf, PNf, PLf)
def removed(t):
    t = np.atleast_1d(t)
    return sum(G(ZEROS[i], E0f, tauf) * np.exp(1j * ZEROS[i] * t) for i in (ia, ib))
def weil_pair(t):
    t = np.atleast_1d(t)
    return sum(G(g0 + s * 1j * eta, E0f, tauf) * np.exp(1j * (g0 + s * 1j * eta) * t) for s in (1, -1))
def lorentz_pair(t):
    t = np.atleast_1d(t)
    E = np.linspace(E0f - 14 / tauf, E0f + 14 / tauf, 80001)
    L = (eta / np.pi) / ((E - g0) ** 2 + eta ** 2)
    return np.array([2 * trapz(G(E, E0f, tauf) * np.exp(1j * E * x) * L, E) for x in t])
tg = np.arange(0, nG) * dT
base = echo_true(tg) - removed(tg)
ev_true = np.linalg.eigvalsh(toeplitz(echo_true(tg)))
ev_weil = np.linalg.eigvalsh(toeplitz(base + weil_pair(tg)))
ev_lor = np.linalg.eigvalsh(toeplitz(base + lorentz_pair(tg)))
check("V4 true line list: Gram matrix PSD", ev_true.min() > -1e-9, f"min eigenvalue {ev_true.min():.3e}")
check("V4 off-line pair, Weil (evaluation) form: Gram matrix has a negative eigenvalue", ev_weil.min() < -1e-3, f"min eigenvalue {ev_weil.min():.4f}")
check("V4 off-line pair, Lorentzian (harmonic-measure) form: Gram matrix PSD", ev_lor.min() > -1e-9, f"min eigenvalue {ev_lor.min():.3e}")
tf = np.linspace(0, 4, 401)
c_true = echo_true(tf)
c_weil = c_true - removed(tf) + weil_pair(tf)
c_lor = c_true - removed(tf) + lorentz_pair(tf)
check("V4 off-line pair, Weil form: echo exceeds its initial value", np.max(np.abs(c_weil)) > abs(c_weil[0]),
      f"max |C(t)|/C(0) on [0,4] = {np.max(np.abs(c_weil)) / abs(c_weil[0]):.2f}")
check("V4 off-line pair, Lorentzian form: echo bound holds", np.max(np.abs(c_lor)) <= abs(c_lor[0]) + 1e-9)
z, w = 0.7 - 0.2j, -0.3 + 1.1j
Mh = np.array([[0, 1], [1, 0]], complex)
check("V4 one off-line pair contributes a form of signature (1,1)", np.allclose(np.linalg.eigvalsh(Mh), [-1, 1]),
      f"2 Re(z conj w) = {2 * (z * np.conj(w)).real:+.2f} for a sample (z, w)")

# ---------------------------------------------------------------------------------------------
print("== V5  response-function form and the real-place background")
mp.mp.dps = 30
def xi(s):
    return 0.5 * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
s = mp.mpc(2.5, 3.0)
lhs = mp.diff(xi, s) / xi(s)
PN6, PL6 = mangoldt(2000000)
dirich = -np.sum(PL6 * np.exp(-complex(s) * np.log(PN6)))
rhs = 1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2 + mp.digamma(s / 2) / 2 + complex(dirich)
check("V5 xi'/xi(s) = 1/s + 1/(s-1) - (log pi)/2 + psi(s/2)/2 - sum Lambda(n) n^-s at s = 2.5 + 3i",
      abs(lhs - rhs) < 1e-7, f"|diff| = {float(abs(lhs - rhs)):.1e}")
vals = [float(mp.re(mp.diff(xi, mp.mpc(0.5 + d, e)) / xi(mp.mpc(0.5 + d, e)))) for d in (0.01, 0.1, 1.0) for e in (0.0, 14.0, 14.1347, 20.0, 31.7)]
check("V5 Re xi'/xi > 0 at 15 sample points right of the line", min(vals) > 0, f"min = {min(vals):.4f}")
for E in (10.0, 30.0):
    num = mp.diff(mp.siegeltheta, E) / mp.pi
    check(f"V5 real-place density at E = {E:g} is theta'(E)/pi", abs(num - arch_density(E)) < 1e-12, f"{float(num):.6f}")
E = mp.mpf(12)
ph = mp.pi ** (-1j * E) * mp.gamma(mp.mpf(1) / 4 + 1j * E / 2) / mp.gamma(mp.mpf(1) / 4 - 1j * E / 2)
check("V5 Gamma_R(1/2+iE)/Gamma_R(1/2-iE) = exp(2 i theta(E)) at E = 12", abs(ph - mp.exp(2j * mp.siegeltheta(E))) < 1e-25)
mp.mp.dps = 15

# ---------------------------------------------------------------------------------------------
print("== Figure 1  dark-line density from the place-by-place budget")
tauD = 1.5
PNd, PLd = mangoldt(3000000)
Eg = np.linspace(0, 52, 1041)
bg_arch = np.array([trapz((tauD / np.sqrt(np.pi)) * np.exp(-tauD ** 2 * (Ei - Eg[k]) ** 2) * arch_density(Ei), Ei)
                    for k in range(len(Eg)) for Ei in [np.linspace(Eg[k] - 9, Eg[k] + 9, 3601)]])
bg_pole = (tauD / np.sqrt(np.pi)) * 2 * np.exp(-tauD ** 2 * (Eg ** 2 - 0.25)) * np.cos(tauD ** 2 * Eg)
wts = PLd / np.sqrt(PNd) * np.exp(-np.log(PNd) ** 2 / (4 * tauD ** 2)) / np.pi
def prime_part(mask):
    out = np.zeros_like(Eg)
    n, w = PNd[mask], wts[mask]
    for a in range(0, len(n), 20000):
        out -= (w[a:a + 20000, None] * np.cos(np.log(n[a:a + 20000])[:, None] * Eg[None, :])).sum(0)
    return out
small = np.zeros(len(PNd), bool)
for p in (2, 3, 5, 7):
    k = np.round(np.log(PNd) / np.log(p))
    small |= np.abs(p ** k - PNd) < 1e-6 * PNd
d_bg = bg_arch + bg_pole
d_small = d_bg + prime_part(small)
d_all = d_bg + prime_part(np.ones(len(PNd), bool))
d_zero = (tauD / np.sqrt(np.pi)) * np.exp(-tauD ** 2 * (ALLZ.real[:, None] - Eg[None, :]) ** 2).sum(0)
check("Fig1 place-side density equals the smoothed line list (primes <= 3e6)", np.max(np.abs(d_all - d_zero)) < 1e-5, f"max |diff| = {np.max(np.abs(d_all - d_zero)):.1e}")
check("Fig1 place-side density is nonnegative on [0, 52]", d_all.min() > -1e-5, f"min = {d_all.min():.1e}")
check("Fig1 real place + zero modes alone go negative near E = 0", d_bg.min() < -0.1, f"min = {d_bg.min():.3f}")

INK, MUTED, GRID, AXIS, SURF = "#0b0b0b", "#52514e", "#e1e0d9", "#c3c2b7", "#fcfcfb"
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": AXIS, "axes.labelcolor": MUTED,
                     "xtick.color": MUTED, "ytick.color": MUTED, "axes.spines.top": False, "axes.spines.right": False,
                     "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF})

fig, ax = plt.subplots(figsize=(9.6, 4.3), dpi=200)
ax.axhline(0, color=AXIS, lw=0.8)
ax.plot(Eg, d_bg, color=AQUA, lw=2, label="real place + zero modes")
ax.plot(Eg, d_small, color=ORANGE, lw=2, label="… minus the places 2, 3, 5, 7")
ax.plot(Eg, d_all, color=BLUE, lw=2, label="… minus all finite places")
zs = ZEROS[ZEROS < 52]
ax.plot(zs, np.full_like(zs, -0.10), "|", color=INK, ms=9, mew=1.2)
ax.text(52.4, -0.10, "zeros of ζ", color=MUTED, va="center", fontsize=9)
for yy, lab in ((d_bg[-1], "∞ + zero modes"), (d_small[-1] + 0.02, "− 2, 3, 5, 7"), (d_all[-1] - 0.02, "− all primes")):
    ax.text(52.4, yy, lab, color=INK, va="center", fontsize=9)
ax.set_xlim(0, 52)
ax.set_ylim(-0.42, 0.95)
ax.set_xlabel("squeeze frequency E")
ax.set_ylabel("dark lines per unit E (resolution 0.47)")
ax.grid(axis="y", color=GRID, lw=0.6)
ax.set_axisbelow(True)
ax.legend(frameon=False, loc="upper right", fontsize=9, labelcolor=INK, bbox_to_anchor=(1.0, 1.08), ncol=3)
fig.tight_layout()
fig.savefig(os.path.join(NOTE, "fig_density.png"))
plt.close(fig)

print("== Figure 2  the echo for the true line list and for a made-up off-line pair")
fig, ax = plt.subplots(figsize=(9.2, 3.9), dpi=200)
ax.axhline(1, color=AXIS, lw=0.8, ls=(0, (4, 3)))
ax.text(4.03, 1, "bound", color=MUTED, va="center", fontsize=9)
ax.plot(tf, np.abs(c_true) / abs(c_true[0]), color=BLUE, lw=2, label="ζ, from the place-by-place formula")
ax.plot(tf, np.abs(c_lor) / abs(c_lor[0]), color=AQUA, lw=2, label="off-line pair, Lorentzian form")
ax.plot(tf, np.abs(c_weil) / abs(c_weil[0]), color=ORANGE, lw=2, label="off-line pair, Weil form")
iw = np.searchsorted(np.abs(c_weil) / abs(c_weil[0]), 2.0)
ax.annotate("Weil form: grows", (tf[iw], 2.0), xytext=(-8, 0), textcoords="offset points", color=INK, fontsize=9, ha="right", va="center")
ax.annotate("ζ: beats, never above 1", (2.52, 1.0), xytext=(0, 7), textcoords="offset points", color=INK, fontsize=9, ha="center")
ax.annotate("Lorentzian form: decays", (2.6, np.abs(c_lor[260]) / abs(c_lor[0])), xytext=(0, 7), textcoords="offset points", color=INK, fontsize=9, ha="left")
ax.set_xlim(0, 4)
ax.set_ylim(0, 2.3)
ax.set_xlabel("log-squeeze t")
ax.set_ylabel("|C(t)| / C(0)")
ax.grid(axis="y", color=GRID, lw=0.6)
ax.set_axisbelow(True)
ax.legend(frameon=False, loc="upper center", fontsize=9, labelcolor=INK, bbox_to_anchor=(0.5, 1.12), ncol=3)
fig.tight_layout()
fig.savefig(os.path.join(NOTE, "fig_echo.png"))
plt.close(fig)

print(f"\n{npass} passed, {nfail} failed")
