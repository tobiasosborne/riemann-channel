"""Step 5 of viz-brief.md: the calibration case (lane B2.2) (lane V, second pass; claude:opus).

Certified data only; nothing is recomputed.  Graph side: the certified Ramanujan cubic graph G40 (40 vertices,
q = 2, R = 78 distinct atoms), parsed from lane B2's output `outputs/rtp1_calibration.txt`: the axis-K table
(every sixth K and K = 73..77, as printed), the certified collapse ball at K = 78, the learning exponents, the
fixed-window inertia and lambda_min tables, the prime cycle counts pi(l), l <= 16, and the like-for-like PNT table.
Zeta side: lane A1's outputs (CCM axis x at N = 60 and 120, axis N at x = 13, 25, 50, fixed window at N = 60) and
lane B2's PNT table against x (`outputs/rtp1_commutant.txt` section 5b).

Derived (exact arithmetic on printed integers, stated in the captions): the counts N_k = Tr B^k = sum_{d | k} d pi(d)
for k <= 16 and the graph PNT counts q^k + 1 + (E - V)(1 + (-1)^k); the distance |nu_(K+1) - c_K| = |tau_K| e_K.
These are checked against the printed nu_(K+1) and rho(K).

No panel uses the graph's spectrum (lane B2's COMPARISON STEP is not drawn) or zeros of zeta: none needs the
"comparison (zeros used)" label.
"""
import math
import os
import re

import numpy as np

import common as C
from common import T, S
import step4_commutant as S4

STEP = "step5"
SCRIPT = "viz/rtp1/step5_calibration.py"
B2_OUT = os.path.join(C.OUT, "rtp1_calibration.txt")
Q, V, E = 2, 40, 60
R = 78
NSAT = {13: 56, 25: 134, 50: 352}
check = S4.check


def _num(s):
    return float("inf") if s == "inf" else float(s)


def b2_calibration():
    if not os.path.exists(B2_OUT):
        raise SystemExit("lane B2 calibration output missing")
    txt = open(B2_OUT).read()
    check(re.search(r"CHECKS: (\d+) passed, 0 failed", txt) is not None, "lane B2 calibration output: 0 failed checks")
    d = {}
    sec3 = txt.split("G40 (q = 2, V = 40), R = 78 distinct atoms", 1)[1].split("ok   [L 427]", 1)[0]
    rows = []
    for line in sec3.splitlines():
        f = line.split()
        if len(f) == 10 and f[0].isdigit():
            rows.append(dict(K=int(f[0]), lam=float(f[1]), logdet=float(f[2]), e=float(f[3]), c=float(f[4]),
                             nu=float(f[5]), tau=float(f[6]), dI=_num(f[7]), dIs=_num(f[8]), ov=float(f[9])))
    d["axisK"] = rows
    m = re.search(r"lambda_min\(T_78\) = 0 \(certified ball ([-0-9.e+]+) \+- ([0-9.e+-]+) contains 0\)", txt)
    d["ball78"] = (float(m.group(1)), float(m.group(2)))
    m = re.search(r"p = ([0-9.]+) \(K = 6\.\.30\), ([0-9.]+) \(K = 30\.\.54\), ([0-9.]+) \(K = 54\.\.72\), ([0-9.]+) "
                  r"\(K = 72\.\.77\)", txt)
    d["p"] = [(6, 30, float(m.group(1))), (30, 54, float(m.group(2))), (54, 72, float(m.group(3))),
              (72, 77, float(m.group(4)))]
    m = re.search(r"prime cycle counts pi\(l\), l = 1\.\.16: \[([\d, ]+)\]", txt)
    d["pi"] = [0] + [int(t) for t in m.group(1).split(",")]
    m = re.search(r"#neg against P = 0\.\.77: \[([\d, ]+)\]", txt)
    d["neg77"] = [int(t) for t in m.group(1).split(",")]
    sec4 = txt.split("4. DATA AXIS", 1)[1].split("5. RAYLEIGH", 1)[0]
    for K in (77, 38):
        part = sec4.split("G40, window K = %d:" % K, 1)[1].split("\n\n", 1)[0]
        rr = []
        for line in part.splitlines():
            f = line.split()
            if len(f) == 6 and f[0].isdigit():
                rr.append(dict(P=int(f[0]), ncyc=int(f[1]), lam=float(f[2]), neg=int(f[3]), logdet=float(f[4]),
                               ov=float(f[5])))
        d["data%d" % K] = rr
    sec6b = txt.split("like-for-like scale", 1)[1].split("ok   [L 663]", 1)[0]
    d["rho"] = [dict(K=int(f[0]), xeq=float(f[1]), rho=float(f[2]), capt=float(f[3]))
                for f in (ln.split() for ln in sec6b.splitlines()) if len(f) == 4 and f[0].isdigit()]
    for K in (77, 38):
        m = re.search(r"K = %d: \|\|x_true\|\|_HS = [0-9.e+]+; max-det \(PNT\) prediction: lambda_min = [0-9.]+ \(= nu_0\), "
                      r"relative distance ([0-9.e+-]+), captured fraction [0-9.]+;\s+relative diameter of the whole "
                      r"positive set <= ([0-9.e+-]+); in count units \|N_k - N_k\^PNT\| / N_k <= ([0-9.e+-]+) for k >= (\d+)"
                      % K, txt)
        d["pnt%d" % K] = dict(dist=float(m.group(1)), diam=float(m.group(2)), cnt=float(m.group(3)), kmin=int(m.group(4)))
    m = re.search(r"with every cycle length except the last, lambda_min = ([-0-9.e+]+)", txt)
    d["last_missing"] = float(m.group(1))
    return d


def counts(pi, kmax=16):
    """N_k = Tr B^k = sum_{d | k} d pi(d) (exact), the PNT counts and nu_k = q^(-k/2) (N_k - PNT_k)"""
    Nk = {k: sum(dd * pi[dd] for dd in range(1, k + 1) if k % dd == 0) for k in range(1, kmax + 1)}
    pnt = {k: Q ** k + 1 + (E - V) * (1 + (-1) ** k) for k in range(1, kmax + 1)}
    nu = {k: (Nk[k] - pnt[k]) / Q ** (k / 2) for k in Nk}
    return Nk, pnt, nu


def rho_from_counts(Nk, pnt, K):
    """lane B2's rho(K): ||x_true - x_PNT|| / ||x_true||, ||x||^2 = sum_k 2 (K+1-k) x_k^2, x_k = q^(-k/2) N_k"""
    num = sum(2 * (K + 1 - k) * ((Nk[k] - pnt[k]) / Q ** (k / 2)) ** 2 for k in range(1, K + 1))
    den = sum(2 * (K + 1 - k) * (Nk[k] / Q ** (k / 2)) ** 2 for k in range(1, K + 1))
    return math.sqrt(num / den)


def secondary_xeq(ax):
    top = ax.secondary_xaxis("top", functions=(lambda k: k * math.log10(Q), lambda y: y / math.log10(Q)))
    top.set_xlabel("log10 x_eq,  x_eq = 2^K  (zeta-comparable window)", color=T["ink2"])
    top.tick_params(colors=T["muted"], labelcolor=T["ink2"])
    return top


# ---------------------------------------------------------------------------------------------------
def fig_learning(G):
    ak = G["axisK"]
    ccm = {N: C.a1_axisx("ccm", N) for N in (60, 120)}
    K = np.array([r["K"] for r in ak])
    lg = np.log10([r["lam"] for r in ak])
    check(K[0] == 0 and K[-1] == 77 and len(K) == 18, "G40 axis-K rows as printed: K = 0, 6, .., 72, 73..77")
    check(all(lg[i] > lg[i + 1] for i in range(len(lg) - 1)), "G40 lambda_min decreasing along the printed rows")
    lo, rad = G["ball78"]
    check(lo - rad <= 0 <= lo + rad, "G40 lambda_min(T_78): certified ball [%.3g +- %.3g] contains 0" % (lo, rad))
    rows = [("G40", r["K"], r["K"] * math.log10(Q), r["lam"]) for r in ak]
    rows.append(("G40", 78, 78 * math.log10(Q), 0.0))
    for N in (60, 120):
        rows += [("zeta CCM N=%d" % N, r["x"], math.log10(r["x"]), "1e%.6f" % r["lg_eps"]) for r in ccm[N]["main"]]
    C.write_table("s5_learning", ["case", "K_or_x", "log10_window_x", "lambda_min"], rows,
                  ["certified. G40: outputs/rtp1_calibration.txt section 3 (rows as printed; K = 78: certified ball "
                   "%.3e +- %.3e contains 0)" % (lo, rad),
                   "zeta: lane A1 eps_N(x), outputs/rtp1_a1_axisx_ccm_N60.txt and _N120.txt (log10 given as 1e<exp>)"])
    slope = -4 * math.pi / math.log(10)
    y0 = ccm[120]["main"][8]["lg_eps"]

    def draw():
        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(1, 3, figsize=(15.5, 5.4), gridspec_kw=dict(wspace=0.28, width_ratios=[1.2, 1, 1]))
        a1, a2, a3 = axs
        a1.plot(K, lg, "o-", color=S(1), label="G40, lambda_min(T_K)", **C.ring())
        a1.axvline(R, color=T["ink2"], lw=0.9)
        a1.annotate("K = R = 78:\nlambda_min = 0 exactly\n(certified ball contains 0)", xy=(R - 0.3, -21.3), xytext=(26, -21.3), va="center",
                    fontsize=7.5, color=T["ink"], arrowprops=dict(arrowstyle="->", color=T["ink"], lw=0.9))
        for k1, k2, p in G["p"]:
            km = 0.5 * (k1 + k2)
            ym = np.interp(km, K, lg)
            if k2 == 77:
                a1.text(70.5, -19.3, "x_eq^-%.2f" % p, fontsize=7.5, color=T["ink2"], ha="right")
            else:
                a1.text(km + 1.0, ym + 0.8, "x_eq^-%.2f" % p, fontsize=7.5, color=T["ink2"])
        a1.set_xlim(-2, 82)
        a1.set_ylim(-22, 3)
        a1.set_xlabel("K  (window = data cutoff: cycles of length <= K)")
        a1.set_ylabel("log10 lambda_min")
        a1.set_title("(a) calibration: G40, power law, then collapse", pad=34)
        secondary_xeq(a1)
        for i, N in enumerate((60, 120)):
            m = ccm[N]["main"]
            a2.plot([r["x"] for r in m], [r["lg_eps"] for r in m], "s-", color=S(i + 3), ms=4.5,
                    label="zeta eps_N(x), N = %d" % N, **C.ring())
        xs = np.array([2, 50])
        a2.plot(xs, y0 + slope * (xs - 13), color=T["ink2"], lw=0.9)
        a2.text(30, y0 + slope * (30 - 13) - 4, "e^(-4 pi x)", fontsize=8, color=T["ink2"], ha="left", va="top")
        C.note(a2, "eps_N(x) > 0 at every x: no collapse\n(N = 60 flattens once N < N_sat(x))", x=0.97, y=0.97, ha="right")
        a2.set_xlabel("x  (window [1/sqrt x, sqrt x]; prime powers <= x)")
        a2.set_ylabel("log10 eps_N(x)")
        a2.set_title("(b) zeta (lane A1, CCM protocol)", pad=34)
        a2.set_ylim(-125, 5)
        a2.legend(loc="lower left", fontsize=7.5)
        a3.plot(K * math.log10(Q), lg, "o-", color=S(1), label="G40 against x_eq = 2^K", **C.ring())
        for i, N in enumerate((60, 120)):
            m = ccm[N]["main"]
            a3.plot([math.log10(r["x"]) for r in m], [r["lg_eps"] for r in m], "s-", color=S(i + 3), ms=4.5,
                    label="zeta, N = %d, against x" % N, **C.ring())
        lx = np.linspace(math.log10(2), math.log10(50), 100)
        a3.plot(lx, y0 + slope * (10 ** lx - 13), color=T["ink2"], lw=0.9)
        a3.text(2.4, -104, "e^(-4 pi x)", fontsize=8, color=T["ink2"])
        a3.annotate("graph: a power law is a straight\nline here; it ends at the collapse", xy=(12, np.interp(40, K, lg)),
                    xytext=(6.5, -45), fontsize=7.5, color=T["ink"],
                    arrowprops=dict(arrowstyle="-", color=T["ink2"], lw=0.6))
        a3.set_xlim(-0.5, 24.5)
        a3.set_ylim(-125, 5)
        a3.set_xlabel("log10 of the window x  (graph: x_eq = 2^K)")
        a3.set_ylabel("log10 lambda_min")
        a3.set_title("(c) both against the window, log-log", pad=34)
        a3.legend(loc="lower right", fontsize=7.5)
        fig.suptitle("Step 5: learning curves, calibration graph against zeta (certified; no spectral data used)",
                     x=0.05, ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.05, right=0.99, top=0.8, bottom=0.11)
        return fig
    C.render("s5_learning", draw)
    return dict(id="s5_learning", step="Step 5", title="Learning curves: G40 against zeta",
                caption=("Certified, lanes B2.2 and A1. (a) The certified Ramanujan cubic graph G40 (40 vertices, q = 2, "
                         "R = 78 distinct atoms): lambda_min of the Toeplitz window form T_K against K, which is at once the "
                         "window and the data cutoff (the analogue of lane A1's CCM axis x), at the rows lane B2 prints "
                         "(every sixth K and K = 73..77). The top axis is the zeta-comparable window x_eq = 2^K. The curve "
                         "is a power law in x_eq whose exponent steepens (lane B2's fitted exponents 0.44, 0.83, 1.56, 2.64 "
                         "on K = 6..30, 30..54, 54..72, 72..77) and then collapses: lambda_min(T_78) = 0, a certified ball "
                         "of radius 3.7e-175 containing 0. (b) Zeta, lane A1's certified eps_N(x) in the CCM protocol at "
                         "N = 60 and 120, with an e^(-4 pi x) reference line through eps_120(13) (drawn, not fitted): "
                         "positive at every x, no collapse. (c) Both against log10 of the window: the graph's power law is a "
                         "straight line over 23 decades of x_eq; zeta falls 118 decades between x = 2 and 25. The two "
                         "forms are normalised differently (graph nu_0 = 78, zeta O(1)); compare shapes, not heights."),
                panels=["G40 lambda_min against K and x_eq (certified)", "zeta eps_N(x) (certified; reference line drawn)",
                        "both against log10 window (certified)"],
                kind="certified data", sources=[C.rel(B2_OUT), ccm[60]["path"], ccm[120]["path"]], script=SCRIPT)


def fig_disc(G):
    ak = G["axisK"]
    D = {x: C.a1_axisN(x) for x in (13, 25, 50)}
    for r in ak:
        r["dist"] = abs(r["tau"]) * r["e"]
    big = [r for r in ak if r["e"] > 0.1]
    check(all(abs(abs(r["nu"] - r["c"]) - r["dist"]) <= 0.01 * r["e"] + 1e-4 for r in big),
          "G40: |tau_K| e_K = |nu_(K+1) - c_K| on the %d printed rows with e_K > 0.1 (below that the 4-decimal nu and c "
          "cannot resolve it)" % len(big))
    check(abs(ak[-1]["tau"]) == 1.0 and all(abs(r["tau"]) < 1 for r in ak[:-1]),
          "G40: truth interior for K < 77, on the boundary at K = 77")
    rows = [("G40", r["K"], r["e"], r["dist"], r["tau"]) for r in ak]
    for x in (13, 25, 50):
        rows += [("zeta x=%d" % x, r["N"], r["r_j"], "", r["tau"]) for r in D[x]["rows"]]
    C.write_table("s5_disc", ["case", "K_or_N", "radius_e_K_or_half_width_r_j", "abs(nu_next - centre) = abs(tau) e_K (derived)", "tau"],
                  rows, ["certified: G40 from outputs/rtp1_calibration.txt section 3 (printed rows); zeta from "
                         "outputs/rtp1_a1_axisN_x{13,25,50}.txt; the distance column is |tau| e_K from the printed columns"])

    def draw():
        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(2, 2, figsize=(12.5, 8.4), gridspec_kw=dict(hspace=0.45, wspace=0.22))
        (a1, a2), (a3, a4) = axs
        K = [r["K"] for r in ak]
        a1.semilogy(K, [r["e"] for r in ak], "o-", color=S(1), label="disc radius e_K", **C.ring())
        a1.semilogy(K, [r["dist"] for r in ak], "D-", color=S(2), lw=1.0, ms=5.5,
                    label="|nu_(K+1) - c_K|: truth's distance from the centre", **C.ring())
        a1.axvline(R, color=T["ink2"], lw=0.9)
        a1.text(R - 1, 3e2, "K = 78:\nradius 0", ha="right", va="top", fontsize=7.5, color=T["ink2"])
        a1.set_xlabel("K")
        a1.set_ylabel("rescaled trace units")
        a1.set_xlim(-2, 82)
        a1.set_ylim(2e-9, 1e3)
        a1.set_title("(a) G40: disc of the next trace nu_(K+1)", pad=40)
        a1.legend(loc="lower left", fontsize=7.5)
        secondary_xeq(a1).set_xlabel("log10 x_eq = K log10 2", color=T["ink2"])
        a2.bar(K, [abs(r["tau"]) for r in ak], width=2.2, color=S(1))
        a2.axhline(1, color=T["ink2"], lw=0.9)
        a2.plot([0, 38.5], [0.189, 0.189], color=T["ink"], lw=1.2)
        a2.plot([39, 76.5], [0.372, 0.372], color=T["ink"], lw=1.2)
        a2.text(1, 0.21, "mean over all K < 39: 0.19", fontsize=7.5, color=T["ink2"])
        a2.text(39.5, 0.39, "mean, 39 <= K < 77: 0.37", fontsize=7.5, color=T["ink2"])
        a2.text(77, 1.03, "K = 77: on the edge", ha="right", fontsize=7.5, color=T["ink"])
        a2.set_ylim(0, 1.12)
        a2.set_xlim(-2, 82)
        a2.set_xlabel("K  (bars: printed rows; means over every K, lane B2)")
        a2.set_ylabel("|tau_K|  (1 = truth on the edge)")
        a2.set_title("(b) G40: where the true next trace sits", pad=40)
        for i, x in enumerate((13, 25, 50)):
            rr = D[x]["rows"]
            Nn = np.array([r["N"] for r in rr])
            a3.semilogy(Nn, [r["r_j"] for r in rr], color=S(i + 3), lw=1.2, label="zeta r_j, x = %d" % x)
            j = int(np.where(Nn == NSAT[x])[0][0])
            a3.plot([NSAT[x]], [rr[j]["r_j"]], "o", color=S(i + 3), ms=7, **C.ring())
            tau = np.abs([r["tau"] for r in rr])
            k = 9
            mt = np.convolve(tau, np.ones(k) / k, mode="valid")
            a4.plot(Nn, tau, ".", color=S(i + 3), ms=2.5, alpha=0.5)
            a4.plot(Nn[k // 2:len(Nn) - k // 2], mt, color=S(i + 3), lw=1.5, label="x = %d (9-row mean)" % x)
            a4.plot([NSAT[x]], [np.interp(NSAT[x], Nn[k // 2:len(Nn) - k // 2], mt)], "o", color=S(i + 3), ms=7,
                    **C.ring())
        for ax in (a3, a4):
            ax.set_xscale("log")
            ax.set_xlabel("N  (resolution at fixed window; circles: N_sat = argmin log det)")
        a3.plot([], [], "o", color=T["ink2"], label="N_sat")
        a3.set_ylabel("half-width r_j of the interval of b_(N+1)")
        a3.set_title("(c) zeta: admissible interval of the next datum (lane A1)")
        a3.legend(loc="lower right", fontsize=7.5)
        a4.axhline(1, color=T["ink2"], lw=0.9)
        a4.set_ylim(0, 1.08)
        a4.set_ylabel("|tau_j|  (1 = truth on the edge)")
        a4.set_title("(d) zeta: where the true b_(N+1) sits")
        a4.legend(loc="lower left", fontsize=7.5)
        fig.suptitle("Step 5: the posterior of the next datum, graph against zeta (certified)", x=0.06, ha="left",
                     fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.07, right=0.985, top=0.87, bottom=0.07)
        return fig
    C.render("s5_disc", draw)
    return dict(id="s5_disc", step="Step 5", title="The disc of the next datum: G40 against zeta",
                caption=("Certified, lanes B2.2 and A1. (a) G40: the radius e_K = det T_K / det T_(K-1) of the disc of the "
                         "next rescaled trace nu_(K+1) (prop:extension-disc; for Toeplitz data the disc is already the "
                         "structured section), and the true trace's distance from the disc centre (the Levinson / MaxEnt "
                         "prediction), |tau_K| e_K from lane B2's printed columns (checked against |nu_(K+1) - c_K| where the printed digits resolve it). The radius falls from nu_0 = 78 to 1.8e-7 "
                         "and is 0 at K = 78. (b) The position |tau_K| of the truth in its disc at the printed rows, with lane "
                         "B2's means over every K: interior until K = 77, on the edge there. (c) Zeta: the half-width r_j of "
                         "the admissible interval of the next datum b_(N+1) against N at x = 13, 25, 50 (lane A1.2; circles "
                         "N_sat): tiny below saturation, O(1) above it. (d) Zeta: |tau_j| (dots) and its 9-row running mean: "
                         "on the edge below N_sat, interior above. The graph has no resolution axis; its analogue of N_sat is "
                         "the collapse at K = R."),
                panels=["G40 disc radius and truth's distance (certified; distance derived)", "G40 |tau_K| (certified)",
                        "zeta r_j (certified)", "zeta |tau_j| (certified; running mean derived)"],
                kind="certified data", sources=[C.rel(B2_OUT)] + [D[x]["path"] for x in (13, 25, 50)], script=SCRIPT)


def fig_inertia(G):
    fl = C.a1_axisx("fixedL", 60)
    neg = G["neg77"]
    check(len(neg) == 78 and neg[-1] == 0 and all(n > 0 for n in neg[:-1]),
          "G40, K = 77: 78 certified negative counts (P = 0..77), 0 only at P = 77")
    check(all(neg[r["P"]] == r["neg"] for r in G["data77"]), "G40, K = 77: the negative-count list agrees with the table rows")
    check(G["data38"][-1]["neg"] == 0 and all(r["neg"] > 0 for r in G["data38"][:-1]),
          "G40, K = 38: indefinite until P = 38")
    check(abs(G["data77"][-2]["lam"] - G["last_missing"]) < 1e-3 * abs(G["last_missing"]),
          "G40, K = 77: last-missing lambda_min %.4g" % G["last_missing"])
    m = fl["main"]
    rows = [("G40 K=77", P, neg[P], "") for P in range(78)]
    rows += [("G40 K=77 table", r["P"], r["neg"], r["lam"]) for r in G["data77"]]
    rows += [("G40 K=38 table", r["P"], r["neg"], r["lam"]) for r in G["data38"]]
    rows += [("zeta fixed L=log 50, N=60", r["npp"], r["neg"], C.num(r["eps"])) for r in m]
    C.write_table("s5_inertia", ["case", "P_or_prime_powers_included", "negative_eigenvalues", "lambda_min"], rows,
                  ["certified: G40 from outputs/rtp1_calibration.txt section 4 (negative counts and lambda_min certified);",
                   "zeta from outputs/rtp1_a1_axisx_fixedL_N60.txt (even block)"])

    def draw():
        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(2, 2, figsize=(12.5, 8.2), gridspec_kw=dict(hspace=0.42, wspace=0.2))
        (a1, a2), (a3, a4) = axs
        a1.bar(range(78), neg, width=0.8, color=S(1), label="window K = 77, every P")
        d38 = G["data38"]
        a1.plot([r["P"] for r in d38], [r["neg"] for r in d38], "D", color=S(2), ms=6,
                label="window K = 38 (printed P)", **C.ring())
        a1.set_xlabel("P = longest prime-cycle length included  (P < 4: kinematic data only)")
        a1.set_ylabel("negative eigenvalues (certified)")
        a1.set_title("(a) G40: inertia against cycle lengths included")
        a1.legend(loc="upper right", fontsize=7.5)
        a1.annotate("0 only when length 77 enters", xy=(77, 0.3), xytext=(52, 30), fontsize=7.5, color=T["ink"],
                    arrowprops=dict(arrowstyle="-", color=T["ink2"], lw=0.6))
        npp = [r["npp"] for r in m]
        a2.bar(npp, [r["neg"] for r in m], width=0.62, color=S(3))
        a2.set_xlabel("prime powers included (L = log 50, N = 60; last: 49)")
        a2.set_ylabel("negative even eigenvalues (certified)")
        a2.set_title("(b) zeta: inertia against prime powers included (lane A1)")
        a2.annotate("0 only when 49 enters", xy=(23, 0.2), xytext=(17.5, 13), fontsize=7.5, color=T["ink"],
                    arrowprops=dict(arrowstyle="-", color=T["ink2"], lw=0.6))
        for key, c, mk, lab in (("data77", S(1), "o", "K = 77"), ("data38", S(2), "D", "K = 38")):
            rr = G[key]
            a3.plot([r["P"] for r in rr], [r["lam"] for r in rr], mk + "-", color=c, label=lab, **C.ring())
        a3.set_yscale("symlog", linthresh=1.0)
        a3.axhline(0, color=T["axis"], lw=0.8)
        a3.set_ylim(-3e12, 10)
        a3.set_xlabel("P")
        a3.set_ylabel("lambda_min (symlog, linear below 1)")
        a3.set_title("(c) G40: lambda_min; with only the last length missing: %.2g" % G["last_missing"])
        a3.text(76, -2e3, "+7.0e-21 at P = 77\n(+3.3e-4 at P = 38)\nshown at 0", ha="right", fontsize=7.5, color=T["ink2"])
        a3.legend(loc="center left", fontsize=7.5)
        lam = [C.num(r["eps"]) for r in m]
        a4.plot(npp, lam, "o-", color=S(3), **C.ring())
        a4.set_yscale("symlog", linthresh=1e-6)
        a4.axhline(0, color=T["axis"], lw=0.8)
        a4.set_xlabel("prime powers included")
        a4.set_ylabel("lambda_min (symlog, linear below 1e-6)")
        a4.set_title("(d) zeta: lambda_min; with only 49 missing: -5.7e-7")
        a4.text(22.5, -3e-5, "+1.75e-116 at the end\nshown at 0", ha="right", fontsize=7.5, color=T["ink2"])
        fig.suptitle("Step 5: fixed window, data added: indefinite until the last datum, in both (certified)", x=0.06,
                     ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.07, right=0.985, top=0.9, bottom=0.07)
        return fig
    C.render("s5_inertia", draw)
    return dict(id="s5_inertia", step="Step 5", title="Fixed-window inertia: G40 against zeta",
                caption=("Certified, lanes B2.2 (G40, section 4) and A1.3 (zeta, fixed-window protocol). (a) G40, window K = "
                         "77: the certified number of negative eigenvalues of the partial form built from the kinematic data "
                         "and the prime cycles of length <= P, for every P (bars), and at the printed P for window K = 38 "
                         "(diamonds). One negative direction (the pole) with kinematic data only, up to 39, then exactly one "
                         "fewer per added length over the last 39, and 0 only when the last length enters. (b) Zeta, L = log 50, "
                         "N = 60: the negative even eigenvalues against prime powers included: 3 with none, up to 16, 0 only "
                         "when 49 enters. (c, d) The certified lambda_min on symmetric-log axes. With only the last datum "
                         "missing it is -3.9e11 for the graph (the lag-K corner of a Toeplitz form carries full weight) "
                         "against -5.7e-7 for zeta (the prime power at the window edge enters with weight 1 - log k / L -> "
                         "0). Lane B2 read the difference as a continuous-versus-discrete edge effect; the RTP-1 review showed it is a resolution effect instead: at L = log 50 with all prime powers but 49 the value is -5.7e-7 at N = 60 and -2.0e-2 at N = 240, with the negative count rising from 3 to 8."),
                panels=["G40 negative counts (certified)", "zeta negative counts (certified)", "G40 lambda_min (certified)",
                        "zeta lambda_min (certified)"],
                kind="certified data", sources=[C.rel(B2_OUT), fl["path"]], script=SCRIPT)


def fig_pnt(G):
    Nk, pnt, nu = counts(G["pi"])
    ak = {r["K"]: r for r in G["axisK"]}
    for K in (0, 6, 12):
        k = K + 1
        check(abs(nu[k] - ak[K]["nu"]) < 6e-5, "nu_%d from the printed pi(l) = %.4f (B2 prints %.4f)" % (k, nu[k], ak[K]["nu"]))
    rho = {r["K"]: r for r in G["rho"]}
    for K in [k for k in rho if k <= 16]:
        mine = rho_from_counts(Nk, pnt, K)
        check(abs(mine - rho[K]["rho"]) < 6e-5 * max(1, rho[K]["rho"]),
              "rho(%d) from the printed pi(l) = %.4f (B2: %.4f)" % (K, mine, rho[K]["rho"]))
    check(all(abs(v) <= 2 * V - 2 for v in nu.values()), "|nu_k| <= nu_0 = 78 for k <= 16 (moment-space bound)")
    zeta = S4.b2_pnt_x(open(S4.B2_OUT).read())
    rows = [("G40 count", k, Nk[k], pnt[k], nu[k]) for k in range(1, 17)]
    rows += [("G40 rho(K)", r["K"], r["xeq"], r["rho"], r["capt"]) for r in G["rho"]]
    rows += [("zeta rho(x)", r["x"], r["N"], r["rho"], r["capt"]) for r in zeta]
    rows += [("G40 posterior K=%d" % K, K, G["pnt%d" % K]["dist"], G["pnt%d" % K]["diam"], G["pnt%d" % K]["cnt"])
             for K in (38, 77)]
    C.write_table("s5_pnt", ["series", "k_or_K_or_x", "col_a", "col_b", "col_c"], rows,
                  ["G40 count: k, N_k = sum_{d|k} d pi(d), PNT count q^k + 1 + (E-V)(1+(-1)^k), nu_k (DERIVED exactly from "
                   "the printed pi(l), outputs/rtp1_calibration.txt section 2)",
                   "G40 rho(K): K, x_eq, rho, captured (certified, section 6b); zeta rho(x): x, N, rho, captured "
                   "(outputs/rtp1_commutant.txt section 5b)",
                   "G40 posterior: K, relative distance of the max-det (PNT) element, relative diameter bound of the "
                   "positive set, count-unit bound (section 6b)"])

    def draw():
        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(1, 3, figsize=(15.5, 5.2), gridspec_kw=dict(wspace=0.27))
        a1, a2, a3 = axs
        ks = np.arange(1, 17)
        a1.plot(ks, [pnt[k] for k in ks], "-", color=S(4), lw=1.6, label="PNT: q^k + 1 + (E - V)(1 + (-1)^k)")
        a1.plot(ks, [Nk[k] for k in ks], "D", color=S(2), ms=6.5, label="truth: N_k = Tr B^k", **C.ring())
        a1.set_yscale("symlog", linthresh=10)
        a1.set_xlabel("k (closed non-backtracking walks of length k)")
        a1.set_ylabel("count (symlog, linear below 10)")
        a1.set_xticks(range(1, 17))
        a1.set_title("(a) G40: counts against the graph PNT")
        a1.legend(loc="upper left", fontsize=7.5)
        C.note(a1, "girth 4: N_1 = N_2 = N_3 = 0", x=0.98, y=0.04, ha="right", va="bottom")
        a2.axhspan(-(2 * V - 2), 2 * V - 2, color=S(3), alpha=T["wash"] * 1.6, lw=0)
        a2.axhline(0, color=T["axis"], lw=0.8)
        a2.plot(ks, [nu[k] for k in ks], "D-", color=S(2), lw=1.0, ms=6, **C.ring())
        a2.text(16.3, 70, "|nu_k| <= nu_0 = 78: the positive set\nis the moment space (bounded)", ha="right", va="top",
                fontsize=7.5, color=T["ink"])
        a2.set_ylim(-90, 90)
        a2.set_xticks(range(1, 17))
        a2.set_xlabel("k")
        a2.set_ylabel("nu_k = 2^(-k/2) (N_k - PNT_k)")
        a2.set_title("(b) G40: the PNT error, square-root rescaled")
        a3.loglog([r["xeq"] for r in G["rho"]], [r["rho"] for r in G["rho"]], "o-", color=S(1),
                  label="G40: max-det element (= graph PNT), x_eq = 2^K", **C.ring())
        zN = [r for r in zeta if r["N"] == 40]
        zs = [r for r in zeta if r["N"] != 40]
        a3.loglog([r["x"] for r in zN], [r["rho"] for r in zN], "s-", color=S(3), label="zeta: PNT mean, N = 40", **C.ring())
        a3.loglog([r["x"] for r in zs], [r["rho"] for r in zs], "^-", color=S(4), label="zeta: PNT mean, N = N_sat(x)",
                  **C.ring())
        for Kp in (38, 77):
            a3.plot([Q ** Kp], [G["pnt%d" % Kp]["diam"]], "o", mfc="none", mec=S(1), ms=9, mew=1.4)
        a3.plot([], [], "o", mfc="none", mec=S(1), ms=8, mew=1.4, label="G40: relative diameter of the whole positive set")
        a3.axhline(1, color=T["ink2"], lw=0.9)
        a3.text(2e22, 1.3, "1 = no better than no prediction", ha="right", fontsize=7.5, color=T["ink2"])
        a3.set_xlabel("window x  (graph: x_eq = 2^K)")
        a3.set_ylabel("relative error rho of the prediction")
        a3.set_title("(c) prediction error against the window")
        a3.legend(loc="lower left", fontsize=7)
        fig.suptitle("Step 5: the graph PNT is the maximum-determinant element; how well it predicts (certified)",
                     x=0.05, ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.05, right=0.99, top=0.86, bottom=0.12)
        return fig
    C.render("s5_pnt", draw)
    p77 = G["pnt77"]
    return dict(id="s5_pnt", step="Step 5", title="The graph PNT against the truth",
                caption=("Lane B2.2 section 6b. With G40's kinematic data fixed, the positive set of prime data is the "
                         "moment space (bounded) and its maximum-determinant element is nu = (nu_0, 0, .., 0), i.e. the graph "
                         "prime number theorem N_k = q^k + 1 + (E - V)(1 + (-1)^k). (a) The true counts N_k = Tr B^k against "
                         "that prediction for k <= 16, and (b) the rescaled error nu_k, inside the band |nu_k| <= nu_0 = 78; "
                         "both derived exactly from lane B2's printed prime-cycle counts pi(l), l <= 16 (checked against its "
                         "printed nu_(K+1) and rho(K)). (c) Certified: the relative error rho of the prediction against the "
                         "window, for G40 (x_eq = 2^K) and for zeta's PNT mean (x = 13..200 at N = 40 and at N = N_sat(x); "
                         "lane B2 section 5b). At comparable windows (x_eq = 16..256) the graph PNT is worse than no "
                         "prediction (rho = 6.7 .. 2.2); it reaches %.1e at K = 77, where the whole positive set has relative "
                         "diameter <= %.1e (open circles: K = 38 and 77). Zeta's positive set in Loewner coordinates has no "
                         "maximum-determinant element (Step 4)." % (p77["dist"], p77["diam"])),
                panels=["G40 counts vs PNT (derived exactly from certified pi(l))", "G40 rescaled error (derived)",
                        "rho against the window (certified)"],
                kind="certified data (panels a, b derived exactly from printed counts)",
                sources=[C.rel(B2_OUT), C.rel(S4.B2_OUT)], script=SCRIPT)


def run():
    G = b2_calibration()
    entries = [fig_learning(G), fig_disc(G), fig_inertia(G), fig_pnt(G)]
    C.register(STEP, entries)
    return entries


if __name__ == "__main__":
    run()
