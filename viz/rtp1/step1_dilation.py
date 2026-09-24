"""Step 1 of viz-brief.md: the dilation channel (lane A1) (lane V; claude:opus).

Certified data (parsed from lane A1's outputs, never recomputed): Delta I_N, log det, r_j, tau_j, eps_N, overlaps,
negative-eigenvalue counts, and, in panels labelled "comparison (zeros used)", |z_1 - gamma_1|.
Recomputed for display (the outputs do not contain them): the window matrices (x = 13, N = 30), the minimal
even eigenvectors (x = 13, 25, 50) and the exact 2-D section of the unstructured ellipsoid.  These use zst's
(a_n, b_n) (zst_riemann_ab via the C printer of bridges.py), assembled into zst's even/odd blocks
(zst/src/blocks.c) in Python; eigenvectors by inverse iteration in multiprecision midpoint arithmetic
(python-flint arb_mat, algorithm "approx"), checked against lane A1's certified eps.
"""
import math

import numpy as np
from flint import arb, arb_mat, ctx
from matplotlib.colors import SymLogNorm

import bridges
import common as C
from common import T, S

STEP = "step1"
SCRIPT = "viz/rtp1/step1_dilation.py"
XS = (13, 25, 50)
PP = C.prime_powers(100)
LOG = []


def check(cond, msg):
    LOG.append(("ok  " if cond else "FAIL") + "  " + msg)
    print(("  ok    " if cond else "  FAIL  ") + msg)
    if not cond:
        raise SystemExit("check failed: " + msg)


def even_block(a, b, N):
    """zst_even_block (zst/src/blocks.c) in arb: basis V_0, (V_j + V_-j)/sqrt2"""
    s2 = arb(2).sqrt()
    E = [[arb(0)] * (N + 1) for _ in range(N + 1)]
    E[0][0] = a[0]
    for j in range(1, N + 1):
        t = b[j] / j * s2
        E[0][j] = t
        E[j][0] = t
        E[j][j] = a[j] + b[j] / j
        for i in range(1, j):
            v = (b[i] - b[j]) / (i - j) + (b[i] + b[j]) / (i + j)
            E[i][j] = v
            E[j][i] = v
    return E


def tau_full(af, bf, N):
    n = np.arange(-N, N + 1)
    bb = np.sign(n) * bf[np.abs(n)]
    M = np.empty((2 * N + 1, 2 * N + 1))
    for i, ni in enumerate(n):
        for j, nj in enumerate(n):
            M[i, j] = af[abs(ni)] if ni == nj else (bb[i] - bb[j]) / (ni - nj)
    return M


def blocks_float(af, bf, N):
    E = np.empty((N + 1, N + 1))
    O = np.empty((N, N))
    E[0, 0] = af[0]
    for j in range(1, N + 1):
        E[0, j] = E[j, 0] = math.sqrt(2) * bf[j] / j
        E[j, j] = af[j] + bf[j] / j
        O[j - 1, j - 1] = af[j] - bf[j] / j
        for i in range(1, j):
            t, u = (bf[i] - bf[j]) / (i - j), (bf[i] + bf[j]) / (i + j)
            E[i, j] = E[j, i] = t + u
            O[i - 1, j - 1] = O[j - 1, i - 1] = t - u
    return E, O


# ---------------------------------------------------------------------------------------------------
def fig_window():
    N = 30
    a, b, ra, rb = bridges.zst_ab(13, N, 300)
    af = np.array([float(x) for x in a])
    bf = np.array([float(x) for x in b])
    M = tau_full(af, bf, N)
    E, O = blocks_float(af, bf, N)
    # consistency: the even/odd blocks are the full matrix in the gamma-adapted basis
    n = 2 * N + 1
    U = np.zeros((n, n))
    U[N, 0] = 1
    for j in range(1, N + 1):
        U[N + j, j] = U[N - j, j] = 1 / math.sqrt(2)
        U[N + j, N + j] = 1 / math.sqrt(2)
        U[N - j, N + j] = -1 / math.sqrt(2)
    B = U.T @ M @ U
    check(np.abs(B[:N + 1, :N + 1] - E).max() < 1e-12 and np.abs(B[N + 1:, N + 1:] - O).max() < 1e-12
          and np.abs(B[:N + 1, N + 1:]).max() < 1e-12,
          "x = 13, N = 30: U^T tau U = diag(even block, odd block) (zst/src/blocks.c conventions)")
    check(abs(af[1] - 0.0465118895436779793116060710601) < 1e-15 and abs(bf[1] - 0.0457203442394000540357853654912) < 1e-15,
          "zst (a_1, b_1) at x = 13 equal the values printed in outputs/rtp1_a1_axisN_x13.txt")
    C.write_table("s1_window", ["n", "a_n", "b_n"], [(i, af[i], bf[i]) for i in range(N + 1)],
                  ["zst_riemann_ab at x = 13, prime powers <= 13, 300 bits (midpoints); tau_nm = (b_n - b_m)/(n - m), tau_nn = a_n"])
    vmax = float(np.abs(M).max())

    def draw():
        import matplotlib.pyplot as plt
        fig = plt.figure(figsize=(11, 4.4))
        gs = fig.add_gridspec(1, 4, width_ratios=[1.35, 1, 1, 0.05], wspace=0.28)
        norm = SymLogNorm(linthresh=1e-2, vmin=-vmax, vmax=vmax, base=10)
        cm = C.cmap_div()
        mats = [(M, "tau on |n| <= 30 (61 x 61)", -N), (E, "even block (31 x 31)", 0), (O, "odd block (30 x 30)", 1)]
        for k, (Mat, title, off) in enumerate(mats):
            ax = fig.add_subplot(gs[k])
            m = Mat.shape[0]
            im = ax.imshow(Mat, cmap=cm, norm=norm, extent=(off - 0.5, off + m - 0.5, off + m - 0.5, off - 0.5))
            ax.set_title(title)
            ax.grid(False)
            ax.set_xlabel("n" if k == 0 else "j")
            if k == 0:
                ax.set_ylabel("n")
        cax = fig.add_subplot(gs[3])
        cb = fig.colorbar(im, cax=cax)
        cb.outline.set_visible(False)
        cb.set_label("entry (signed log scale, linear for |.| < 0.01)", color=T["ink2"])
        fig.suptitle("The window matrix of the CCM Weil form, x = 13, N = 30 (recomputed from zst's (a_n, b_n))",
                     x=0.05, ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.05, right=0.92, top=0.82, bottom=0.12)
        return fig
    C.render("s1_window", draw)
    return dict(id="s1_window", step="Step 1", title="The window matrix tau, x = 13, N = 30",
                caption=("Heat maps of the Loewner window matrix tau_nm = (b_n - b_m)/(n - m), tau_nn = a_n, on |n| <= 30 at "
                         "x = 13 (left), and of its even block (basis V_0, (V_j + V_-j)/sqrt2) and odd block ((V_j - V_-j)/sqrt2) "
                         "(zst/src/blocks.c). Blue positive, red negative, signed-log colour scale. Recomputed in floating point "
                         "for display from zst's certified (a_n, b_n) (zst_riemann_ab at 300 bits, midpoints); the block "
                         "decomposition is checked against the full matrix. The large diagonal a_n + b_n/n at high n dominates; "
                         "the minimal even eigenvalue near this N (lane A1, certified: 1.57e-39 at N = 20, 9.46e-54 at N = 40) is "
                         "invisible at this scale."),
                panels=["full tau (recomputed, floating point)", "even block (recomputed)", "odd block (recomputed)"],
                kind="recomputed (floating point)", sources=["zst_riemann_ab (zst/build/libzst.a) via viz/rtp1/bridges.py"],
                script=SCRIPT)


def ground_state(X, N, prec, ref):
    ctx.prec = prec
    a, b, _, _ = bridges.zst_ab(X, N, prec)
    a = [arb(x) for x in a]
    b = [arb(x) for x in b]
    E = arb_mat(even_block(a, b, N))
    v = arb_mat([[1]] * (N + 1))
    for _ in range(3):
        v = E.solve(v, algorithm="approx")
        nv = sum((v[i, 0] ** 2 for i in range(N + 1)), arb(0)).sqrt()
        v = arb_mat([[(v[i, 0] / nv).mid()] for i in range(N + 1)])
    Ev = E * v
    ray = sum((v[i, 0] * Ev[i, 0] for i in range(N + 1)), arb(0))
    rs = ray.mid().str(8, radius=False)
    lg = C.log10s(rs)
    check(abs(lg - C.log10s(ref)) < 0.01,
          "x = %d, N = %d: Rayleigh quotient of the recomputed eigenvector %s = lane A1's certified eps %s (to 2%%)" % (X, N, rs, ref))
    vf = np.array([float(v[i, 0].mid().str(20, radius=False)) for i in range(N + 1)])
    L = math.log(X)
    t = np.linspace(-L / 2, L / 2, 1601)
    f = vf[0] / math.sqrt(L) * np.ones_like(t)
    for j in range(1, N + 1):
        f += vf[j] * (-1) ** j * math.sqrt(2) / math.sqrt(L) * np.cos(2 * math.pi * j * t / L)
    if f[len(t) // 2] < 0:
        f, vf = -f, -vf
    ctx.prec = 53
    return dict(X=X, N=N, t=t, f=f, v=vf, eps=rs, L=L)


def fig_ground():
    specs = [(13, 60, 700, "1.01356e-58"), (25, 150, 1100, "6.78e-123"), (50, 360, 1700, "2.27e-257")]
    gsx = [ground_state(*s) for s in specs]
    rows = []
    for g in gsx:
        for tv, fv in zip(g["t"][::8], g["f"][::8]):
            rows.append((g["X"], g["N"], float(tv), float(fv)))
    C.write_table("s1_ground", ["x", "N", "log_u", "xi(u)"], rows,
                  ["minimal even eigenvector as a function on the centred window log u in [-L/2, L/2], unit L^2(d*u) norm;",
                   "recomputed (multiprecision midpoint inverse iteration on zst's even block); Rayleigh quotient = certified eps"])
    ov = []
    for g in gsx:
        ov.append(g)

    def draw():
        import matplotlib.pyplot as plt
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.3), gridspec_kw=dict(width_ratios=[1.35, 1], wspace=0.25))
        for i, g in enumerate(gsx):
            a1.plot(g["t"], g["f"], color=S(i + 1), label="x = %d, N = %d  (eps = %s)" % (g["X"], g["N"], g["eps"]))
            a1.axvline(g["L"] / 2, ymin=0, ymax=0.05, color=S(i + 1), lw=1.5)
            a1.axvline(-g["L"] / 2, ymin=0, ymax=0.05, color=S(i + 1), lw=1.5)
        a1.axhline(0, color=T["axis"], lw=0.8)
        a1.set_xlabel("log u  (centred window [-L/2, L/2], L = log x; ticks mark the window edges)")
        a1.set_ylabel("xi(u), unit norm in L^2(d*u)")
        a1.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=1)
        a1.set_title("Minimal even eigenvector as a function in the window", pad=52)
        for i, g in enumerate(gsx):
            j = np.arange(len(g["v"]))
            a2.semilogy(j, np.abs(g["v"]) + 1e-300, "o-", color=S(i + 1), lw=1.2, ms=3.5,
                        label="x = %d" % g["X"], **C.ring(markeredgewidth=0.6))
        a2.set_xlim(-1, 45)
        a2.set_xlabel("mode j (even basis; N = 60, 150, 360 modes computed)")
        a2.set_ylabel("|coefficient|")
        a2.set_ylim(1e-14, 2)
        a2.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=3)
        a2.set_title("Its coefficients in the even basis", pad=26)
        fig.suptitle("The ground state of the window (recomputed; Rayleigh quotient equals lane A1's certified eps)",
                     x=0.05, ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.07, right=0.985, top=0.73, bottom=0.13)
        return fig
    C.render("s1_ground", draw)
    return dict(id="s1_ground", step="Step 1", title="The ground state of the window, x = 13, 25, 50",
                caption=("Left: the minimal even eigenvector xi of the window form, drawn as the function "
                         "sum_j v_j phi_j(log u) on the centred window (phi_0 = L^(-1/2), phi_j = (-1)^j sqrt2 L^(-1/2) "
                         "cos(2 pi j log u / L); the convention of lane A1's overlap_f), at x = 13, 25, 50 with N = 60, 150, "
                         "360 (at or above lane A1's saturation N_sat ~ 1.7 x log x). Right: the absolute coefficients against "
                         "j/(x log x). Recomputed for display: zst's (a_n, b_n) at 700/1100/1700 bits, zst's even block, inverse "
                         "iteration in multiprecision midpoint arithmetic; the Rayleigh quotients (1.01e-58, 6.78e-123, "
                         "2.27e-257) reproduce lane A1's certified eps_N, which is the check that the eigenvector is the right "
                         "one. The three functions nearly coincide in log u (lane A1's certified intrinsic overlap between x = 13 and "
                         "x = 50 at N = 60 is 0.9989): the ground state sits well inside every window and is fixed early. No zeros used."),
                panels=["xi as a function (recomputed, multiprecision)", "coefficients (recomputed)"],
                kind="recomputed (multiprecision midpoint)", sources=["zst_riemann_ab via viz/rtp1/bridges.py",
                                                                        "outputs/rtp1_a1_axisN_x13.txt, _x25.txt, _x50.txt (eps check)"],
                script=SCRIPT)


# ---------------------------------------------------------------------------------------------------
NSAT = {13: 56, 25: 134, 50: 352}          # argmin log det, lane A1 (from the outputs, recomputed below)


def fig_axisN():
    D = {x: C.a1_axisN(x) for x in XS}
    for x in XS:
        nld = min(D[x]["rows"], key=lambda r: r["logdet"])["N"]
        check(nld == NSAT[x], "x = %d: argmin_N log det = %d (lane A1: %d)" % (x, nld, NSAT[x]))
    rows = []
    for x in XS:
        for r in D[x]["rows"]:
            rows.append((x, r["N"], r["dI"], r["logdet"], r["r_j"], r["tau"], r["dIs"]))
    C.write_table("s1_axisN", ["x", "N", "Delta_I_N", "logdet", "r_j", "tau_j", "Delta_I_s"], rows,
                  ["certified (ball midpoints) from outputs/rtp1_a1_axisN_x{13,25,50}.txt"])

    def draw():
        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(2, 2, figsize=(11, 7.4), gridspec_kw=dict(hspace=0.42, wspace=0.22))
        (a1, a2), (a3, a4) = axs
        for i, x in enumerate(XS):
            N = np.array([r["N"] for r in D[x]["rows"]])
            dI = np.array([r["dI"] for r in D[x]["rows"]])
            rj = np.array([r["r_j"] for r in D[x]["rows"]])
            tau = np.array([r["tau"] for r in D[x]["rows"]])
            xl = x * math.log(x)
            a1.semilogy(N, dI, color=S(i + 1), lw=1.1, label="x = %d" % x)
            a1.plot([NSAT[x]], [dI[N == NSAT[x]][0]], "o", color=S(i + 1), ms=7, **C.ring())
            a1.plot([7.5 * x], [dI[np.argmin(np.abs(N - 7.5 * x))]], "D", color=S(i + 1), ms=6, **C.ring())
            a2.semilogy(N / xl, dI, color=S(i + 1), lw=1.1, label="x = %d" % x)
            a3.semilogy(N, rj, color=S(i + 1), lw=1.1, label="x = %d" % x)
            k = 9
            mt = np.convolve(np.abs(tau), np.ones(k) / k, mode="valid")
            a4.plot(N / xl, np.abs(tau), ".", color=S(i + 1), ms=2.5, alpha=0.5)
            a4.plot(N[k // 2:len(N) - k // 2] / xl, mt, color=S(i + 1), lw=1.6, label="x = %d (9-row mean)" % x)
        a1.plot([], [], "o", color=T["ink2"], label="N_sat = argmin log det (~1.7 x log x)")
        a1.plot([], [], "D", color=T["ink2"], label="benchmark's 7.5 x (not the saturation)")
        a1.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=3, fontsize=7.5)
        a1.set_xlabel("N")
        a1.set_ylabel("Delta I_N  (nats)")
        a1.set_title("(a) information in the next mode pair, Delta I_N", pad=40)
        a2.axvline(1.7, color=T["ink2"], lw=0.8)
        a2.text(1.75, 60, "N = 1.7 x log x", fontsize=8, color=T["ink2"])
        a2.set_xlabel("N / (x log x)")
        a2.set_ylabel("Delta I_N  (nats)")
        a2.set_title("(b) the same against N / (x log x): the curves collapse", pad=40)
        a2.legend(loc="lower left")
        a3.set_xlabel("N")
        a3.set_ylabel("half-width r_j of the admissible interval of b_(N+1)")
        a3.set_title("(c) the Schur envelope of the next datum along N")
        a3.legend(loc="lower right")
        a4.axhline(1, color=T["axis"], lw=0.8)
        a4.axvline(1.7, color=T["ink2"], lw=0.8)
        a4.set_ylim(0, 1.08)
        a4.set_xlabel("N / (x log x)")
        a4.set_ylabel("|tau_j|  (1 = truth on the interval's edge)")
        a4.set_title("(d) where the true b_(N+1) sits in its interval")
        a4.legend(loc="center right")
        fig.suptitle("Axis N (resolution at fixed window): lane A1's certified borderings", x=0.06, ha="left",
                     fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.07, right=0.985, top=0.87, bottom=0.07)
        return fig
    C.render("s1_axisN", draw)
    return dict(id="s1_axisN", step="Step 1", title="Axis N: Delta I_N, its saturation, and the envelope",
                caption=("Lane A1.2 at fixed x = 13, 25, 50 (certified ball LDL^T; midpoints plotted). (a) Delta I_N, the "
                         "log-det gain of the bordering |n| <= N -> N+1 (Gaussian mutual information of the new mode pair with "
                         "the old ones). Circles: N_sat = argmin log det = 56, 134, 352, i.e. about 1.7 x log x. Diamonds: the "
                         "benchmark's empirical 7.5 x, which lane A1 finds is not the saturation point (it agrees only near "
                         "x = 50). (b) The same against N/(x log x): the three curves fall together near 1.7. (c) The "
                         "half-width r_j of the admissible interval of the next datum b_(N+1) (Lemma A1.1'): tiny below "
                         "saturation, O(1) above it at every x. (d) The position |tau_j| of the true b_(N+1) in that interval "
                         "(dots) and its 9-row running mean (lines): on the boundary (|tau| ~ 1, the bordered block is nearly "
                         "singular) below saturation, interior above."),
                panels=["Delta I_N (certified)", "collapse (certified)", "r_j (certified)", "|tau_j| (certified; running mean derived)"],
                kind="certified data", sources=[D[x]["path"] for x in XS], script=SCRIPT)


# ---------------------------------------------------------------------------------------------------
def fig_learning():
    ccm = {N: C.a1_axisx("ccm", N) for N in (60, 120)}
    fl = C.a1_axisx("fixedL", 60)
    rows = []
    for N in (60, 120):
        for r in ccm[N]["main"]:
            rows.append(("CCM", N, r["x"], r["npp"], r["eps"], r["logdet"], r["ov_c"], r["ov_f"], r["neg"]))
    for r in fl["main"]:
        rows.append(("fixedL", 60, r["X"], r["npp"], r["eps"], r["logdet"], r["ov_c"], "", r["neg"]))
    C.write_table("s1_learning", ["protocol", "N", "x_or_X", "n_prime_powers", "eps_or_lambda_min", "logdet_even",
                                  "overlap_c", "overlap_f", "neg"], rows,
                  ["certified, from outputs/rtp1_a1_axisx_ccm_N60.txt, _ccm_N120.txt, _fixedL_N60.txt"])
    check(all(r["neg"] > 0 for r in fl["main"][:-1]) and fl["main"][-1]["neg"] == 0,
          "fixed-L protocol: every partial form before the last prime power is indefinite, the last is positive definite")
    check(all(r["neg"] == 0 for N in (60, 120) for r in ccm[N]["main"]),
          "CCM protocol: every stage positive definite")

    def draw_ccm():
        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(3, 1, figsize=(10, 8.6), sharex=True, gridspec_kw=dict(hspace=0.3))
        a1, a2, a3 = axs
        for i, N in enumerate((60, 120)):
            m = ccm[N]["main"]
            x = [r["x"] for r in m]
            a1.plot(x, [r["lg_eps"] for r in m], "o-", color=S(i + 1), label="N = %d" % N, **C.ring())
            a2.semilogy(x[:-1], [1 - r["ov_c"] for r in m[:-1]], "o-", color=S(i + 1), label="N = %d, coefficient overlap" % N,
                        **C.ring())
            a2.semilogy(x[:-1], [1 - r["ov_f"] for r in m[:-1]], "s-", color=S(i + 1), lw=1.0, ms=4.5, alpha=0.75,
                        label="N = %d, intrinsic L^2 overlap" % N, **C.ring())
            a3.plot(x, [r["logdet"] for r in m], "o-", color=S(i + 1), label="N = %d" % N, **C.ring())
        for ax in axs:
            C.vline_ticks(ax, [k for k in PP if k <= 50])
        a1.text(50.4, ccm[60]["main"][-1]["lg_eps"], "N = 60", va="center", fontsize=8, color=T["ink2"])
        a1.text(25.4, ccm[120]["main"][-1]["lg_eps"], "N = 120", va="center", fontsize=8, color=T["ink2"])
        a1.set_ylabel("log10 eps_N(x)")
        a1.set_title("(a) certified minimal eigenvalue of the even block")
        a1.legend(loc="lower left")
        a2.set_ylabel("1 - overlap with final x")
        a2.set_title("(b) eigenvector convergence (final x = 50 for N = 60, 25 for N = 120)")
        a2.legend(loc="lower left", ncol=2)
        a3.set_ylabel("log det (even block)")
        a3.set_title("(c) log det of the even block")
        a3.set_xlabel("x  (knots = prime powers, ticked on every panel; the window L = log x widens with x)")
        a3.legend(loc="lower left")
        a3.set_xlim(0, 53)
        fig.suptitle("Axis x, CCM protocol: the learning curve along the primes at fixed N (certified)", x=0.07,
                     ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.08, right=0.97, top=0.92, bottom=0.07)
        return fig

    def draw_fixed():
        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(4, 1, figsize=(10, 10.4), sharex=True, gridspec_kw=dict(hspace=0.32))
        a1, a2, a3, a4 = axs
        m = fl["main"]
        npp = [r["npp"] for r in m]
        neg = [r["neg"] for r in m]
        a1.bar(npp, neg, width=0.62, color=S(1))
        for n_, g_ in zip(npp, neg):
            a1.text(n_, g_ + 0.3, str(g_), ha="center", fontsize=7, color=T["ink2"])
        a1.set_ylabel("negative even eigenvalues")
        a1.set_ylim(0, 18.5)
        a1.set_title("(a) number of negative eigenvalues (certified inertia) against prime powers included")
        a1.annotate("positive definite only when\nthe last prime power (49) enters", xy=(23, 0.2), xytext=(20.6, 13),
                    fontsize=8, color=T["ink"], arrowprops=dict(arrowstyle="-", color=T["ink2"], lw=0.7))
        lam = np.array([C.num(r["eps"]) for r in m])
        a2.plot(npp, lam, "o-", color=S(1), **C.ring())
        a2.set_yscale("symlog", linthresh=1e-6)
        a2.axhline(0, color=T["axis"], lw=0.8)
        a2.set_ylabel("lambda_min (symlog)")
        a2.set_title("(b) certified minimal eigenvalue: -1.37 with no primes, -5.7e-7 before 49, +1.75e-116 after")
        a2.annotate("+1.75e-116 (shown at 0)", xy=(23, 0), xytext=(15.5, -3e-5), fontsize=8, color=T["ink"],
                    arrowprops=dict(arrowstyle="-", color=T["ink2"], lw=0.7))
        a3.semilogy(npp[:-1], [r["ov_c"] for r in m[:-1]], "o-", color=S(1), **C.ring())
        a3.set_ylabel("overlap with the final eigenvector")
        a3.set_title("(c) the partial form's minimal eigenvector is unrelated to the final one until the end")
        a4.plot(npp, [r["logdet"] for r in m], "o-", color=S(1), **C.ring())
        a4.set_ylabel("log |det| (even block)")
        a4.set_title("(d) log |det| of the even block (log det in the last row, where the form is positive definite)")
        a4.set_xlabel("number of prime powers included (cutoff X = 1, 2, 3, 4, 5, 7, ..., 47, 49)")
        labels = {r["npp"]: str(r["X"]) for r in m}
        for n_ in (0, 5, 9, 13, 16, 19, 22, 23):
            a3.text(n_, 3e-52, "X=%s" % labels[n_], ha="center", fontsize=7, color=T["ink2"])
        a3.set_ylim(1e-52, 3)
        a3.set_xlim(-0.8, 25.5)
        fig.suptitle("Axis x, fixed-window protocol (L = log 50, N = 60): partial forms are indefinite until the end",
                     x=0.07, ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.08, right=0.97, top=0.93, bottom=0.06)
        return fig
    C.render("s1_learning_ccm", draw_ccm)
    C.render("s1_learning_fixedL", draw_fixed)
    e1 = dict(id="s1_learning_ccm", step="Step 1", title="Learning curve along x, CCM protocol",
              caption=("Lane A1.3, CCM protocol: N fixed (60 and 120), x runs through the prime powers, and with it the "
                       "window L = log x (so every (a_n, b_n) changes between knots; the new prime power enters with weight 0 "
                       "at x = k). (a) certified eps_N(x), log scale: it falls at 5.0 to 5.3 digits per unit of x (the e^(-4 pi x) "
                       "law is 5.46) only while N >= N_sat(x) ~ 1.7 x log x, then flattens (N = 60 beyond x ~ 13). (b) 1 - overlap "
                       "of the minimal eigenvector with the one at the final x: circles use coefficient vectors (window rescaled), "
                       "squares the intrinsic L^2(d*u) overlap on centred windows. (c) log det of the even block. Every stage is "
                       "certified positive definite. Ticks: prime powers."),
              panels=["eps_N(x) (certified)", "overlaps (certified)", "log det (certified)"],
              kind="certified data", sources=[ccm[60]["path"], ccm[120]["path"]], script=SCRIPT)
    e2 = dict(id="s1_learning_fixedL", step="Step 1", title="Learning curve along x, fixed-window protocol",
              caption=("Lane A1.3, fixed-window protocol (a partial-information form, not the CCM form except in its last "
                       "row): L = log 50 and N = 60 held fixed, prime powers added one at a time. (a) The certified number of "
                       "negative even eigenvalues against the number of prime powers included: 3 with no primes (pole plus "
                       "archimedean only), up to 16, and 0 only when the last prime power 49 enters. (b) The certified minimal "
                       "eigenvalue on a symmetric-log axis (linear below 1e-6): -1.37 with no primes, -5.66e-7 with every "
                       "prime power except 49, +1.75e-116 at the end. (c) The overlap of the partial form's minimal "
                       "eigenvector with the final one (2.7e-48 at X = 47). (d) log |det| of the even block. In this protocol the partial forms are not "
                       "posteriors: the information arrives as a step at the last prime power."),
              panels=["negative-eigenvalue count (certified inertia)", "lambda_min (certified)", "overlap (certified)",
                      "log |det| (certified)"],
              kind="certified data", sources=[fl["path"]], script=SCRIPT)
    return [e1, e2]


# ---------------------------------------------------------------------------------------------------
def fig_envelope():
    ccm = {N: C.a1_axisx("ccm", N) for N in (60, 120)}
    slope = -4 * math.pi / math.log(10)
    rows = []
    for N in (60, 120):
        errs = {r["x"]: r for r in ccm[N]["cmp"]}
        for r in ccm[N]["main"]:
            rows.append((N, r["x"], r["lg_rj"], r["lg_eps"], errs[r["x"]]["lg_err"]))
    C.write_table("s1_envelope", ["N", "x", "log10_r_j", "log10_eps", "log10_err_z1 (COMPARISON, zeros used)"], rows,
                  ["certified, outputs/rtp1_a1_axisx_ccm_N60.txt and _N120.txt; the last column is from the COMPARISON STEP blocks"])

    def draw():
        import matplotlib.pyplot as plt
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.8), sharey=True, gridspec_kw=dict(wspace=0.08))
        for i, N in enumerate((60, 120)):
            m = ccm[N]["main"]
            x = np.array([r["x"] for r in m])
            a1.plot(x, [r["lg_rj"] for r in m], "o-", color=S(i + 1), label="envelope r_j, N = %d" % N, **C.ring())
            a1.plot(x, [r["lg_eps"] for r in m], "s-", color=S(i + 1), lw=1.0, ms=4, alpha=0.7,
                    label="eps_N, N = %d" % N, **C.ring())
            e = ccm[N]["cmp"]
            a2.plot([r["x"] for r in e], [r["lg_err"] for r in e], "o-", color=S(i + 1),
                    label="|z_1 - gamma_1|, N = %d" % N, **C.ring())
            a2.plot(x, [r["lg_eps"] for r in m], "s-", color=S(i + 1), lw=1.0, ms=4, alpha=0.7, label="eps_N, N = %d" % N,
                    **C.ring())
        x0, y0 = 13, ccm[120]["main"][8]["lg_eps"]
        for ax in (a1, a2):
            xs = np.array([2, 50])
            ax.plot(xs, y0 + slope * (xs - x0), color=T["ink2"], lw=0.9)
            C.vline_ticks(ax, [k for k in PP if k <= 50])
            ax.set_xlabel("x  (prime powers ticked)")
            ax.set_xlim(0, 52)
        a1.text(33, y0 + slope * (33 - x0) + 12, "e^(-4 pi x)\n(slope -5.46 / unit x)", fontsize=8, color=T["ink2"])
        a1.set_ylim(-160, 12)
        a1.set_ylabel("log10")
        a1.set_title("(a) kinematic envelope vs eps_N and e^(-4 pi x)")
        a1.legend(loc="center right", bbox_to_anchor=(1.0, 0.6), fontsize=7.5)
        a2.set_title("(b) the first-zero error follows eps_N")
        a2.legend(loc="center right", bbox_to_anchor=(1.0, 0.72), fontsize=7.5)
        C.badge(a2, "comparison (zeros used)")
        fig.suptitle("The envelope question (round question 3): the Schur envelope does not decay like e^(-4 pi x)",
                     x=0.06, ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.07, right=0.985, top=0.86, bottom=0.12)
        return fig
    C.render("s1_envelope", draw)
    return dict(id="s1_envelope", step="Step 1", title="The envelope panel: r_j, eps_N, e^(-4 pi x) and the first-zero error",
                caption=("Lane A1's kinematic envelope is the half-width r_j of the admissible interval of the next datum "
                         "b_(N+1) (the Schur envelope of shard 08g, Lemma A1.1'). (a) Along x in the CCM protocol at N = 60 and "
                         "120: r_j (circles) against the certified eps_N (squares) and a reference line of slope e^(-4 pi x) "
                         "through eps_120(13). r_j shrinks at about 0.7 digits per unit of x at N = 60 and only because N falls "
                         "below N_sat(x); at saturated N it does not shrink at all (0.5 to 3.7 at x = 13, 25, 50; Step 1 axis-N "
                         "figure). eps_N follows e^(-4 pi x) while N >= N_sat(x). (b) Comparison (zeros used): the certified "
                         "bound on |z_1 - gamma_1| from the COMPARISON STEP blocks, against eps_N; the ratio is about 1e4 at "
                         "every x and N. Lane A1's reading: the e^(-4 pi x) convergence is arithmetic (the residual of a "
                         "cancellation using every prime power < x), not kinematic."),
                panels=["envelope and eps (certified; the reference line is drawn, not fitted)",
                        "comparison (zeros used): |z_1 - gamma_1| (certified comparison step) and eps_N"],
                kind="certified data; panel (b) comparison (zeros used)", sources=[ccm[60]["path"], ccm[120]["path"]],
                script=SCRIPT)


# ---------------------------------------------------------------------------------------------------
def section_ellipse(X=13, N=60, prec=700):
    """exact 2-D section of the unstructured admissible set of the new even column (Lemma A1.1) by the plane
    through the MaxEnt point (c = 0, d = d_true) that contains the Loewner line (c(b), d(b)) (Lemma A1.1')"""
    ctx.prec = prec
    j = N + 1
    a, b, _, _ = bridges.zst_ab(X, j, prec)
    a = [arb(x) for x in a]
    b = [arb(x) for x in b]
    Ej = even_block(a, b, j)
    b1 = list(b)
    b1[j] = b[j] + 1
    Ej1 = even_block(a, b1, j)
    G = arb_mat([row[:j] for row in Ej[:j]])
    c = arb_mat([[Ej[i][j]] for i in range(j)])
    w = arb_mat([[Ej1[i][j] - Ej[i][j]] for i in range(j)])
    d = Ej[j][j]
    dw = Ej1[j][j] - Ej[j][j]                     # = 1/j
    Gc = G.solve(c, algorithm="approx")
    Gw = G.solve(w, algorithm="approx")
    cc = sum((c[i, 0] * Gc[i, 0] for i in range(j)), arb(0))
    cw = sum((c[i, 0] * Gw[i, 0] for i in range(j)), arb(0))
    ww = sum((w[i, 0] * Gw[i, 0] for i in range(j)), arb(0))
    f = lambda z: float(z.mid().str(30, radius=False))
    out = dict(d=f(d), dw=f(dw), cc=f(cc), cw=f(cw), ww=f(ww), j=j, X=X, N=N, b_true=f(b[j]))
    ctx.prec = 53
    s_true = out["d"] - out["cc"]
    l = out["dw"] - 2 * out["cw"]
    Cq = out["ww"]
    bstar = l / (2 * Cq)
    sstar = s_true + l * l / (4 * Cq)
    out.update(s_true=s_true, beta_star=bstar, r=math.sqrt(sstar / Cq), tau=-bstar / math.sqrt(sstar / Cq))
    return out


def fig_posterior():
    D = C.a1_axisN(13)
    byN = {r["N"]: r for r in D["rows"]}
    sec = section_ellipse()
    rN = byN[sec["N"]]
    check(abs(sec["s_true"] / rN["s_e"] - 1) < 1e-3,
          "x = 13, N = 60: recomputed even Schur complement %.5g = certified s_e %.5g" % (sec["s_true"], rN["s_e"]))
    check(abs(sec["r"] / rN["r_e"] - 1) < 1e-3,
          "x = 13, N = 60: recomputed even-block interval half-width %.5g = certified r_e %.5g" % (sec["r"], rN["r_e"]))
    Ns = [5, 10, 20, 30, 40, 50, 56, 60, 70, 100, 150, 200]
    rows = [(n, byN[n]["r_j"], byN[n]["tau"], byN[n]["b"], byN[n]["dIs"]) for n in Ns]
    C.write_table("s1_posterior", ["N", "r_j", "tau_j", "b_true(N+1)", "Delta_I_s"], rows,
                  ["certified, outputs/rtp1_a1_axisN_x13.txt (joint even/odd admissible interval of b_(N+1));",
                   "section panel recomputed: d=%.10g cc=%.10g cw=%.10g ww=%.10g (x=13, N=60, even block)"
                   % (sec["d"], sec["cc"], sec["cw"], sec["ww"])])

    def draw():
        import matplotlib.pyplot as plt
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.5, 5.2), gridspec_kw=dict(width_ratios=[1.15, 1], wspace=0.3))
        for k, n in enumerate(Ns):
            r = byN[n]
            yk = len(Ns) - 1 - k
            a1.plot([-1, 1], [yk, yk], color=S(1), lw=5, solid_capstyle="butt", alpha=0.35)
            a1.plot([-1, 1], [yk, yk], "|", color=S(1), ms=12, mew=1.6)
            a1.plot([0], [yk], "o", color=S(1), ms=7, **C.ring())
            a1.plot([r["tau"]], [yk], "D", color=S(2), ms=7, **C.ring())
            a1.text(1.12, yk, "r = %.2g" % r["r_j"], va="center", fontsize=7.5, color=T["ink2"])
            a1.text(1.62, yk, "%.2f" % r["dIs"], va="center", fontsize=7.5, color=T["ink2"])
        a1.text(1.12, len(Ns) - 0.35, "half-width", fontsize=7.5, color=T["ink2"], va="bottom")
        a1.text(1.62, len(Ns) - 0.35, "Delta I^s", fontsize=7.5, color=T["ink2"], va="bottom")
        a1.set_yticks(range(len(Ns)))
        a1.set_yticklabels([("N_sat = 56" if n == 56 else "N = %d" % n) for n in Ns[::-1]])
        a1.set_xlim(-1.25, 2.05)
        a1.set_xticks([-1, -0.5, 0, 0.5, 1])
        a1.set_ylim(-0.7, len(Ns) + 0.3)
        a1.axhline(len(Ns) - 1 - Ns.index(56) + 0.5, color=T["ink2"], lw=0.8)
        a1.plot([], [], "o", color=S(1), label="centre = structured MaxEnt prediction")
        a1.plot([], [], "D", color=S(2), label="true b_(N+1)")
        a1.plot([], [], "|", color=S(1), ms=10, mew=1.6, label="edge = singular enlargement")
        a1.legend(loc="lower center", bbox_to_anchor=(0.45, 1.0), ncol=2, fontsize=7.5)
        a1.set_xlabel("(b - centre) / r  (each row in its own units)")
        a1.set_title("(a) admissible interval of the next datum b_(N+1), x = 13", pad=36)
        a1.grid(False)
        # section
        s_ = np.linspace(-1.9, 1.9, 700)
        t_ = np.linspace(-6, 6, 900)
        SS, TT = np.meshgrid(s_, t_, indexing="ij")
        Q = sec["d"] + TT * sec["dw"] - (SS ** 2 * sec["cc"] + 2 * SS * TT * sec["cw"] + TT ** 2 * sec["ww"])
        a2.contourf(TT, SS, Q, levels=[0, Q.max() + 1], colors=[S(3)], alpha=T["wash"] * 2).set_rasterized(True)
        a2.contour(TT, SS, Q, levels=[0], colors=[S(3)], linewidths=1.6)
        a2.axhline(1, color=T["ink2"], lw=0.9)
        lo, hi = sec["beta_star"] - sec["r"], sec["beta_star"] + sec["r"]
        a2.plot([lo, hi], [1, 1], color=S(1), lw=4, solid_capstyle="butt")
        a2.plot([sec["beta_star"]], [1], "o", color=S(1), ms=7, **C.ring())
        a2.plot([0], [1], "D", color=S(2), ms=7, **C.ring())
        a2.plot([0], [0], "s", color=T["ink2"], ms=7, **C.ring())
        a2.text(0.2, -0.1, "c = 0, d = d_true: the MaxEnt point of\nLemma A1.1 (not a Loewner column)", fontsize=7.5,
                color=T["ink"], va="top")
        a2.text(-5.8, 1.08, "Loewner line: c = c(b), d = d(b)", fontsize=7.5, color=T["ink2"], va="bottom")
        a2.text(hi + 0.15, 0.9, "admissible\ninterval (even block)", fontsize=7.5, color=T["ink"], va="top")
        a2.text(-5.8, -1.5, "unstructured admissible set\n{d - c^T G^(-1) c >= 0}, exact section", fontsize=7.5,
                color=T["ink"])
        a2.set_xlabel("t = b - b_true  (moves along the Loewner direction)")
        a2.set_ylabel("s  (0: c = 0;  1: the true column)")
        a2.set_title("(b) unstructured ellipsoid (A1.1), 2-D section, N = 60", pad=36)
        fig.suptitle("The posterior of the next datum: an interval, not a free ellipsoid", x=0.06, ha="left",
                     fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.09, right=0.985, top=0.8, bottom=0.11)
        return fig
    C.render("s1_posterior", draw)
    return dict(id="s1_posterior", step="Step 1", title="The posterior of the next datum (Lemma A1.1')",
                caption=("(a) Certified (lane A1, x = 13): for each N, the joint admissible interval of the next datum "
                         "b_(N+1) given a_(N+1) and the window |n| <= N (Lemma A1.1', the exact analogue of the extension disc "
                         "of prop:extension-disc), drawn in its own units: centre (circle) = the structured MaxEnt prediction, "
                         "diamond = the true b_(N+1), edge = the singular enlargement (a bordered block with a kernel). Labels: "
                         "half-width r_j and the log-det gain Delta I^s of the truth over the MaxEnt prediction. Below N_sat = 56 "
                         "the truth sits on the edge; above it, inside. (b) Recomputed for display (multiprecision midpoint, "
                         "x = 13, N = 60, even block): the unconstrained admissible set of Lemma A1.1, {(c, d): d - c^T G^(-1) c "
                         ">= 0}, cut by the plane through the MaxEnt point (c = 0, d = d_true) that contains the Loewner line of "
                         "admissible columns. The line crosses the set in the admissible interval; the point c = 0 is not on the "
                         "line: the unstructured MaxEnt prediction is not a Loewner column (lane A1's correction). The recomputed "
                         "Schur complement and half-width reproduce the certified s_e and r_e."),
                panels=["intervals (certified)", "unstructured ellipsoid section (recomputed, labelled as such)"],
                kind="certified data + recomputed section", sources=[D["path"], "zst_riemann_ab via viz/rtp1/bridges.py"],
                script=SCRIPT)


def run():
    entries = [fig_window(), fig_ground(), fig_axisN()]
    entries += fig_learning()
    entries += [fig_envelope(), fig_posterior()]
    C.register(STEP, entries)
    return entries


if __name__ == "__main__":
    run()
