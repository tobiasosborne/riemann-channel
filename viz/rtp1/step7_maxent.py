"""Step 7 of viz-brief.md: the contradiction pathway and MaxEnt (notes/metric-tomography/metric-as-state.md
section 7) (lane V; claude:opus).

s7_disc: the extension disc of prop:extension-disc (shard 08g) for the two explicit examples of
  scripts/weil_window_extension.py (the permutation (1 2)(3 4 5) and the Petersen graph), with that script's own
  functions `disc` and `levinson_centre` (loaded as definitions only, see bridges.defs).  Exact data, floating point.
s7_saddle: a cartoon.  A toy "zero set" (ordinates 6, 11, 15: invented, not zeros of zeta) defines
  W_toy(f * f~) = sum_rho f^(rho) conj f^(1 - rho-bar), f^(s) = int f(y) e^{(s - 1/2) y} dy (Yoshida's convention).
  On two Gaussian wave packets the form is a bowl when every toy zero is on the line and a saddle when the pair
  at ordinate 11 is moved to 1/2 +- beta.  No zeros of zeta are used.
"""
import math
import os

import numpy as np

import bridges
import common as C
from common import T, S

STEP = "step7"
SCRIPT = "viz/rtp1/step7_maxent.py"
WWE = os.path.join(C.REPO, "scripts", "weil_window_extension.py")


def check(cond, msg):
    print(("  ok    " if cond else "  FAIL  ") + msg)
    if not cond:
        raise SystemExit("check failed: " + msg)


def examples():
    """the two trace sequences of scripts/weil_window_extension.py sections 1 and 3 (same formulas)"""
    z = np.array([-1, 1, 1, np.exp(2j * np.pi / 3), np.exp(-2j * np.pi / 3)])
    t = [int(round(np.sum(z ** k).real)) for k in range(12)]
    th1 = np.arccos(1 / (2 * np.sqrt(2)))
    th2 = 3 * np.pi / 4
    tp = [10 * np.cos(k * th1) + 8 * np.cos(k * th2) for k in range(12)]
    return [("permutation (1 2)(3 4 5): t_k = #Fix(sigma^k)", t), ("Petersen graph: rescaled traces", tp)]


def fig_disc():
    ns = bridges.defs(WWE)
    exs = examples()
    check(exs[0][1][:12] == [5, 0, 2, 3, 2, 0, 5, 0, 2, 3, 2, 0], "permutation traces as in weil_window_extension.py")
    data = []
    rows = []
    for name, t in exs:
        ds = []
        for K in (1, 2, 3, 4):
            c, r = ns["disc"](t, K)
            if K < 4:
                check(abs(c - ns["levinson_centre"](t, K)) < 1e-9, "%s, K = %d: disc centre = Levinson predictor" % (name[:11], K))
                dr = np.linalg.det(ns["toeplitz"](t, K)) / np.linalg.det(ns["toeplitz"](t, K - 1))
                check(abs(r - dr) < 1e-9, "%s, K = %d: radius = det T_K / det T_(K-1) = %.4f" % (name[:11], K, r))
            ds.append((K, c, r, t[K + 1]))
            rows.append((name.split(":")[0], K, c, r, t[K + 1], abs(t[K + 1] - c) / r if r > 1e-9 else float("nan")))
        data.append((name, ds))
    C.write_table("s7_disc", ["example", "K", "centre_c_K (MaxEnt)", "radius_r_K", "true_next_trace", "|t - c|/r"], rows,
                  ["prop:extension-disc for the examples of scripts/weil_window_extension.py (its disc and levinson_centre)"])

    def draw():
        import matplotlib.pyplot as plt
        from matplotlib.patches import Circle
        fig, axs = plt.subplots(2, 3, figsize=(12, 8.2), gridspec_kw=dict(width_ratios=[1.25, 1, 0.8], hspace=0.42,
                                                                          wspace=0.3))
        ramp = [T["seq"][2], T["seq"][3], T["seq"][5]] if T["name"] == "light" else [T["seq"][6], T["seq"][4], T["seq"][3]]
        for row, (name, ds) in enumerate(data):
            a1, a2, a3 = axs[row]
            for (K, c, r, tru), col in zip(ds[:3], ramp):
                a1.add_patch(Circle((c, 0), r, fc=col, alpha=T["wash"], ec="none"))
                a1.add_patch(Circle((c, 0), r, fc="none", ec=col, lw=1.6))
                a1.plot([c], [0], "o", color=col, ms=7, **C.ring())
                a1.plot([tru], [0.0], "D", color=S(2), ms=7, **C.ring())
                a1.text(c, r + 0.04 * ds[0][2], "K = %d" % K, ha="center", va="bottom", fontsize=7.5, color=T["ink2"])
                a2.add_patch(Circle((0, 0), r, fc="none", ec=col, lw=1.6))
                a2.plot([tru - c], [0], "D", color=S(2), ms=7, **C.ring())
                a2.text(0, r, " K = %d" % K, ha="left", va="bottom", fontsize=7.5, color=T["ink2"])
            K4, c4, r4, t4 = ds[3]
            a1.plot([c4], [0], "*", color=T["ink"], ms=11, **C.ring())
            a1.annotate("K = 4: radius 0 (%.0e in floating point),\nthe disc is a point: the next trace is pinned (%s)"
                        % (r4, "%g" % round(t4, 4)) if r4 > 0 else
                        "K = 4: radius 0, the disc is a point:\nthe next trace is pinned (%s)" % ("%g" % round(t4, 4)),
                        xy=(c4, 0), xytext=(c4 - 0.2 * ds[0][2], -0.85 * ds[0][2]), fontsize=7.5, color=T["ink"],
                        arrowprops=dict(arrowstyle="-", color=T["ink2"], lw=0.7))
            R0 = ds[0][2]
            lo = min(c - r for _, c, r, _ in ds[:3])
            hi = max(c + r for _, c, r, _ in ds[:3])
            a1.set_xlim(lo - 0.1 * R0, hi + 0.1 * R0)
            a1.set_ylim(-1.1 * R0, 1.2 * R0)
            a1.set_aspect("equal")
            a1.axhline(0, color=T["axis"], lw=0.8)
            a1.set_xlabel("Re (next trace)")
            a1.set_ylabel("Im")
            a1.set_title("(%s) %s" % ("a" if row == 0 else "d", name), fontsize=9.5)
            a2.set_xlim(-1.15 * R0, 1.15 * R0)
            a2.set_ylim(-1.15 * R0, 1.15 * R0)
            a2.set_aspect("equal")
            a2.axhline(0, color=T["axis"], lw=0.8)
            a2.plot([0], [0], "o", color=T["ink2"], ms=6, **C.ring())
            a2.set_xlabel("next trace - MaxEnt centre")
            a2.set_title("(%s) recentred: nested discs" % ("b" if row == 0 else "e"), fontsize=9.5)
            Ks = [d[0] for d in ds]
            rs = [d[2] for d in ds]
            a3.bar(Ks, rs, width=0.55, color=[*ramp, T["ink2"]])
            for k_, r_ in zip(Ks, rs):
                a3.text(k_, r_ + 0.02 * R0, "%.3g" % r_ if r_ > 1e-9 else "0", ha="center", fontsize=7.5, color=T["ink2"])
            a3.set_xticks(Ks)
            a3.set_xlabel("K (lags known)")
            a3.set_ylabel("radius r_K = det T_K / det T_(K-1)")
            a3.set_title("(%s) radius, non-increasing" % ("c" if row == 0 else "f"), fontsize=9.5)
        h = [plt.Line2D([], [], color=T["seq"][3], marker="o", lw=1.6, label="disc of the next trace; dot = centre = MaxEnt (Burg) prediction"),
             plt.Line2D([], [], color=S(2), marker="D", lw=0, label="true next trace (always inside; on the edge when the next window is singular)"),
             plt.Line2D([], [], color=T["ink"], marker="*", lw=0, ms=10, label="K = 4: singular window, zero radius")]
        fig.legend(handles=h, loc="upper center", bbox_to_anchor=(0.5, 0.945), ncol=2, fontsize=8, frameon=False)
        fig.suptitle("Keep adding constraints, update: the extension disc of the next trace as the Schur algorithm proceeds",
                     x=0.05, ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.06, right=0.985, top=0.86, bottom=0.07)
        return fig
    C.render("s7_disc", draw)
    return dict(id="s7_disc", step="Step 7", title="The extension disc as the Schur algorithm proceeds",
                caption=("prop:extension-disc (shard 08g) for the two explicit examples of scripts/weil_window_extension.py, "
                         "computed with that script's own disc and levinson_centre functions. Given the Toeplitz window up to lag K, "
                         "the admissible next trace t_(K+1) is a closed disc in the complex plane; its centre is the Levinson "
                         "one-step predictor, i.e. Burg's maximum-entropy extension (the MaxEnt prediction of "
                         "metric-as-state.md 7.3), and its radius r_K = det T_K / det T_(K-1) does not increase. (a, d) Discs for "
                         "K = 1, 2, 3 in place, with the true next trace (diamond). (b, e) The same discs recentred on their MaxEnt "
                         "centres: nested, with the truth inside each. (c, f) The radius. Both examples have four distinct atoms, "
                         "so T_4 is singular: at K = 3 the truth sits on the boundary of the disc, and at K = 4 the disc has "
                         "radius 0 and pins the next trace. Upper row: the permutation (1 2)(3 4 5) (t_k = number of fixed points "
                         "of sigma^k). Lower row: the Petersen graph, rescaled retained traces. Exact data, floating point."),
                panels=["discs in place", "recentred (nested)", "radius"], kind="exact examples (floating point)",
                sources=["scripts/weil_window_extension.py (disc, levinson_centre, toeplitz)"], script=SCRIPT)


# ---------------------------------------------------------------------------------------------------
TOY_GAMMA = (6.0, 11.0, 15.0)            # invented ordinates for the cartoon, NOT zeros of zeta
PACKETS = [(-2.0, 0.6, 11.0, 0.0), (2.0, 0.6, 11.0, math.acos(0.6))]   # (centre, width, frequency, phase)
BETA = 0.4


def packet(y, c, s, om, ph):
    return np.exp(-(y - c) ** 2 / (2 * s * s)) * np.cos(om * y - ph)


def transform(z, c, s, om, ph):
    """int packet(y) e^{z y} dy, with z = s - 1/2"""
    return 0.5 * sum(np.exp(-sg * 1j * ph) * math.sqrt(2 * math.pi) * s * np.exp((z + sg * 1j * om) * c + s * s * (z + sg * 1j * om) ** 2 / 2)
                     for sg in (1, -1))


def toy_gram(beta):
    zs = []
    for g in TOY_GAMMA:
        b = beta if g == 11.0 else 0.0
        for z in (b + 1j * g, -b + 1j * g, b - 1j * g, -b - 1j * g):
            if z not in zs:
                zs.append(z)
    M = np.array([[sum(transform(z, *PACKETS[i]) * transform(-z, *PACKETS[j]) for z in zs) for j in range(2)]
                  for i in range(2)])
    check(np.abs(M.imag).max() < 1e-12, "toy Gram matrix is real (zero set closed under conjugation)")
    return M.real


def fig_saddle():
    G0 = toy_gram(0.0)
    G1 = toy_gram(BETA)
    e0, V0 = np.linalg.eigh(G0)
    e1, V1 = np.linalg.eigh(G1)
    check(e0[0] > 0, "all toy zeros on the line: the 2 x 2 form is positive definite (eigenvalues %.3g, %.3g)" % tuple(e0))
    check(e1[0] < 0 < e1[1], "pair at 1/2 +- %.1f + 11 i: the form is indefinite (eigenvalues %.3g, %.3g)" % ((BETA,) + tuple(e1)))
    v = V1[:, 0]
    if v[0] < 0:
        v = -v
    y = np.linspace(-4, 4, 1600)
    fexp = v[0] * packet(y, *PACKETS[0]) + v[1] * packet(y, *PACKETS[1])
    C.write_table("s7_saddle", ["case", "G11", "G12", "G22", "lambda_min", "lambda_max"],
                  [("on the line", G0[0, 0], G0[0, 1], G0[1, 1], e0[0], e0[1]),
                   ("pair at 1/2 +- %.1f" % BETA, G1[0, 0], G1[0, 1], G1[1, 1], e1[0], e1[1])],
                  ["toy zero set with invented ordinates %s (not zeros of zeta); packets (centre, width, freq, phase) %s"
                   % (TOY_GAMMA, [tuple(round(p, 4) for p in q) for q in PACKETS])])

    def draw():
        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(1, 3, figsize=(12.5, 4.6), gridspec_kw=dict(width_ratios=[1, 1, 1.25], wspace=0.3))
        s_ = np.linspace(-1, 1, 401)
        SS, TT = np.meshgrid(s_, s_)
        for ax, G, lab in ((axs[0], G0, "(a) every toy zero on the line: a bowl"),
                           (axs[1], G1, "(b) one pair off the line: a saddle")):
            Q = G[0, 0] * SS ** 2 + 2 * G[0, 1] * SS * TT + G[1, 1] * TT ** 2
            vm = float(np.abs(Q).max())
            ax.contourf(SS, TT, Q, levels=np.linspace(-vm, vm, 23), cmap=C.cmap_div()).set_rasterized(True)
            ax.contour(SS, TT, Q, levels=np.linspace(-vm, vm, 23)[1::2], colors=[T["surface"]], linewidths=0.5)
            if Q.min() < 0:
                ax.contour(SS, TT, Q, levels=[0], colors=[T["ink"]], linewidths=1.2)
            ax.set_aspect("equal")
            ax.grid(False)
            ax.set_xlabel("coefficient of f_1")
            ax.set_ylabel("coefficient of f_2")
            ax.set_title(lab, fontsize=9.5)
        axs[1].annotate("", xy=(0.9 * v[0], 0.9 * v[1]), xytext=(0, 0),
                        arrowprops=dict(arrowstyle="-|>", color=T["ink"], lw=1.4))
        axs[1].text(0.9 * v[0] + 0.03, 0.9 * v[1] - 0.12, "exposing\ndirection", fontsize=7.5, color=T["ink"])
        box = dict(boxstyle="round,pad=0.25", fc=T["surface"], ec=T["axis"], lw=0.6)
        C.note(axs[0], "blue: Q > 0 everywhere", x=0.03, y=0.03, va="bottom", color=T["ink"], bbox=box)
        C.note(axs[1], "red: Q < 0   black: Q = 0", x=0.03, y=0.03, va="bottom", color=T["ink"], bbox=box)
        a3 = axs[2]
        a3.plot(y, packet(y, *PACKETS[0]), color=S(1), lw=1.0, alpha=0.8, label="f_1 (packet at y = -2)")
        a3.plot(y, packet(y, *PACKETS[1]), color=S(3), lw=1.0, alpha=0.8, label="f_2 (packet at y = +2, phase shifted)")
        a3.plot(y, fexp, color=S(2), lw=1.8, label="exposing f = v_1 f_1 + v_2 f_2 (W(f * f~) < 0)")
        a3.axhline(0, color=T["axis"], lw=0.8)
        a3.set_xlabel("y = log u")
        a3.set_ylim(-1.3, 1.9)
        a3.legend(loc="upper center", fontsize=7.5)
        a3.set_title("(c) the test function that exposes the pair", fontsize=9.5)
        fig.suptitle("The off-line pair cartoon: the Weil form on a two-dimensional span (toy zeros, not zeta's)",
                     x=0.05, ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.06, right=0.985, top=0.83, bottom=0.13)
        return fig
    C.render("s7_saddle", draw)
    return dict(id="s7_saddle", step="Step 7", title="The off-line pair cartoon: bowl versus saddle",
                caption=("A cartoon of metric-as-state.md 7.2 and 7.4. A toy zero set with invented ordinates 6, 11, 15 (not zeros "
                         "of zeta) defines W_toy(f * f~) = sum_rho f^(rho) conj f^(1 - rho-bar), f^(s) = int f(y) e^((s - 1/2) y) dy. "
                         "On the span of two Gaussian wave packets f_1, f_2 (width 0.6, frequency 11, centred at y = -2 and +2, "
                         "phase offset arccos 0.6) the form is the quadratic Q(s, t) = W((s f_1 + t f_2) * (s f_1 + t f_2)~). "
                         "(a) All toy zeros on the line: each zero adds |f^(rho)|^2 >= 0 and Q is a bowl. (b) The pair at ordinate "
                         "11 moved to 1/2 +- 0.4: it contributes an indefinite 2 x 2 block, here with off-diagonal entry "
                         "proportional to cosh(0.4 * 4) cos(phase offset) > 1, and Q becomes a saddle (black: Q = 0). (c) The test "
                         "function along the negative eigenvector: the finite, checkable certificate of a violation. The pair is "
                         "invisible to test functions whose transforms vanish at it; here the two packets are separated in "
                         "log u, which is what makes the factors e^(+-beta y) differ. Exact closed forms (Gaussian transforms), "
                         "floating point."),
                panels=["bowl", "saddle", "exposing test function"], kind="toy model (closed form)",
                sources=["notes/metric-tomography/metric-as-state.md section 7"], script=SCRIPT)


def run():
    entries = [fig_disc(), fig_saddle()]
    C.register(STEP, entries)
    return entries


if __name__ == "__main__":
    run()
