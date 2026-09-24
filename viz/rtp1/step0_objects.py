"""Step 0 of viz-brief.md: the objects (lane V; claude:opus).

Figures (all panels are closed-form drawings evaluated in floating point; no zeros of zeta):
  s0_line         the dilation line: CCM windows for x = 13 and 50, the Weil distribution D(y) on y > 0
                  (pole, archimedean, their sum) and the prime comb Lambda(k) k^{-1/2} at log k
  s0_testfns      Fourier test functions V_n in the x = 13 window; the bump phi_delta at log 6 with the
                  admissible delta of {2,3}, A = 1, against the prime powers 5 and 7
  s0_lattice      the {2,3} lattice (A <= 3) and the {2,3,5} lattice (A <= 2) on the line, foreign prime powers
  s0_convolution  phi^* * phi for bumps at log 4 and log 6: support around log(3/2), prime powers touched
Conventions: brief.md (Psi = W_{0,2} - W_R - sum_p W_p on q(y) = F(y) + F(-y), y >= 0; rho(y) = e^{y/2}/(e^y - e^{-y})).
"""
import math

import numpy as np

import common as C
from common import T, S

STEP = "step0"
SCRIPT = "viz/rtp1/step0_objects.py"
PP = C.prime_powers(2000)


def lam_weight(k):
    return math.log(PP[k]) / math.sqrt(k)


def rho(y):
    return np.exp(y / 2) / (np.exp(y) - np.exp(-y))


# bump and its autocorrelation, floating point (display only)
_TG = np.linspace(-1, 1, 8001)
_PHI = np.where(np.abs(_TG) < 1, np.exp(-1 / np.clip(1 - _TG ** 2, 1e-300, None)), 0.0)
_H = _TG[1] - _TG[0]
_SG = np.linspace(-2, 2, 2 * len(_TG) - 1)
_R1 = np.correlate(_PHI, _PHI, mode="full") * _H          # R_1(s) = int phi_1(t) phi_1(t - s) dt


def phi(x, d):
    t = np.asarray(x, float) / d
    out = np.zeros_like(t)
    m = np.abs(t) < 1
    out[m] = np.exp(-1 / (1 - t[m] ** 2))
    return out


def R(y, d):
    """R_delta(y) = delta R_1(y / delta)"""
    return d * np.interp(np.asarray(y, float) / d, _SG, _R1, left=0.0, right=0.0)


# ---------------------------------------------------------------------------------------------------
def fig_line():
    L13, L50 = math.log(13), math.log(50)
    y = np.linspace(0.02, 4.1, 2000)
    pole = 2 * np.cosh(y / 2)
    arch = -rho(y)
    ks = sorted(k for k in PP if k <= 50)
    rows = [(float(a), float(b), float(c), float(b + c)) for a, b, c in zip(y[::20], pole[::20], arch[::20])]
    C.write_table("s0_line", ["y", "pole_density", "arch_density", "smooth_sum"], rows,
                  ["Weil distribution D(y) on y > 0 (floating point): pole 2 cosh(y/2), archimedean -rho(y);",
                   "prime comb: -Lambda(k) k^(-1/2) at y = log k (listed below as rows with y = log k)"])
    with open(C.DATA + "/s0_line_comb.csv", "w") as fh:
        fh.write("k,log_k,Lambda(k)k^(-1/2)\n")
        for k in ks:
            fh.write("%d,%.10g,%.10g\n" % (k, math.log(k), lam_weight(k)))

    def draw():
        import matplotlib.pyplot as plt
        fig = plt.figure(figsize=(10.5, 6.6))
        gs = fig.add_gridspec(3, 1, height_ratios=[0.55, 2.2, 1.6], hspace=0.12)
        a0 = fig.add_subplot(gs[0])
        a1 = fig.add_subplot(gs[1], sharex=a0)
        a2 = fig.add_subplot(gs[2], sharex=a0)
        # windows
        for i, (L, lab) in enumerate(((L13, "x = 13"), (L50, "x = 50"))):
            yy = 1 - i
            a0.plot([0, L], [yy, yy], color=S(1 + i), lw=5, solid_capstyle="butt")
            a0.text(L + 0.05, yy, "%s: q supported in [0, log x] = [0, %.3f]" % (lab, L),
                    va="center", fontsize=8, color=T["ink2"])
        a0.set_ylim(-0.7, 1.7)
        a0.set_yticks([])
        a0.grid(False)
        a0.spines["left"].set_visible(False)
        a0.set_title("CCM windows in the dilation variable y = log(ratio)  (test functions live on log u in [-L/2, L/2], L = log x)",
                     fontsize=9, fontweight="normal", color=T["ink2"])
        plt.setp(a0.get_xticklabels(), visible=False)
        # smooth part
        a1.axhline(0, color=T["axis"], lw=0.8)
        a1.plot(y, pole, color=S(1), label="pole  +2 cosh(y/2)")
        a1.plot(y, arch, color=S(2), label="archimedean  -rho(y)")
        a1.plot(y, pole + arch, color=S(3), label="sum (smooth part of D)")
        a1.set_ylim(-4, 8.2)
        a1.set_ylabel("density on q(y)")
        a1.legend(loc="upper left", ncol=3)
        a1.text(4.12, pole[-1], "pole", va="center", fontsize=8, color=T["ink2"])
        a1.text(4.12, arch[-1], "arch", va="center", fontsize=8, color=T["ink2"])
        a1.text(4.12, pole[-1] + arch[-1] - 0.45, "sum", va="center", fontsize=8, color=T["ink2"])
        C.note(a1, "-rho(y) ~ -1/(2y) at 0: the archimedean term is a finite part plus a point mass at y = 0 (not drawn)",
               x=0.01, y=0.04, va="bottom")
        plt.setp(a1.get_xticklabels(), visible=False)
        # comb
        a2.axhline(0, color=T["axis"], lw=0.8)
        for k in ks:
            c = S(1) if k <= 13 else S(2)
            a2.plot([math.log(k)] * 2, [0, -lam_weight(k)], color=c, lw=1.6)
            a2.plot([math.log(k)], [-lam_weight(k)], "o", color=c, ms=4.5, **C.ring())
            if k <= 13 or k in (16, 25, 27, 32, 49):
                a2.text(math.log(k), -lam_weight(k) - 0.07, str(k), ha="center", va="top", fontsize=7, color=T["ink2"])
        a2.plot([], [], "o-", color=S(1), label="prime powers k <= 13 (inside the x = 13 window)")
        a2.plot([], [], "o-", color=S(2), label="13 < k <= 50 (enter only for the x = 50 window)")
        a2.legend(loc="upper right", ncol=1)
        a2.set_ylim(-0.95, 0.3)
        a2.set_ylabel("-Lambda(k) k^(-1/2)")
        a2.set_xlabel("y = log u (dilation of f^* * g)")
        a2.set_xlim(0, 5.3)
        a2.axvspan(0, math.log(2), color=T["mid"], zorder=0, lw=0)
        a2.text(math.log(2) / 2, 0.2, "no prime mass\n|y| < log 2", ha="center", va="center", fontsize=7, color=T["ink2"])
        fig.suptitle("The Weil distribution on the dilation line: smooth part and prime comb", x=0.065, ha="left",
                     fontsize=12, fontweight="bold", color=T["ink"], y=0.975)
        fig.subplots_adjust(left=0.065, right=0.985, top=0.9, bottom=0.08)
        return fig
    C.render("s0_line", draw)
    return dict(id="s0_line", step="Step 0", title="The dilation line: windows, smooth part and prime comb",
                caption=("Weil distribution D(y) on y > 0, in the brief's normalisation: Psi(F) = int_0^L q(y) D(y) dy with "
                         "q(y) = F(y) + F(-y). Top: the CCM windows for x = 13 and x = 50 (q is supported in [0, log x]; the "
                         "test functions themselves live on log u in [-L/2, L/2]). Middle: the smooth part, pole +2 cosh(y/2) "
                         "and archimedean -rho(y), drawn separately and summed; the archimedean finite part and point mass at "
                         "y = 0 are not drawn. Bottom: the prime comb, a point mass -Lambda(k) k^(-1/2) at y = log k, split "
                         "into the prime powers inside the x = 13 window and those that enter only by x = 50. The grey band "
                         "|y| < log 2 carries no prime mass."),
                panels=["windows (closed form)", "smooth part of D (closed form, floating point)", "prime comb (exact weights)"],
                kind="closed form", sources=["brief.md Conventions", "notes/zeta-spectral-triples/plan.md section 1"],
                script=SCRIPT)


def fig_testfns():
    L = math.log(13)
    t = np.linspace(-L / 2, L / 2, 1200)
    ns = (0, 1, 2, 5)
    d = [r["dmax"] for r in C.a2_admissible() if r["S"] == (2, 3) and r["A"] == 1][0]   # lane A2 table (certified)
    l6, l5, l7 = math.log(6), math.log(5), math.log(7)
    xs = np.linspace(1.5, 2.1, 1500)
    bump = phi(xs - l6, d)
    corr = R(xs - l6, d)
    corr = corr / corr.max()
    rows = [(float(a),) + tuple(float(math.cos(2 * math.pi * n * (a + L / 2) / L) / math.sqrt(L)) for n in ns)
            for a in t[::12]]
    C.write_table("s0_testfns", ["log_u"] + ["Re V_%d" % n for n in ns], rows,
                  ["Re V_n(u) = L^(-1/2) cos(2 pi n (log u + L/2)/L) on the x = 13 window (floating point)"])

    def draw():
        import matplotlib.pyplot as plt
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.2), gridspec_kw=dict(width_ratios=[1.1, 1], wspace=0.22))
        for i, n in enumerate(ns):
            yv = np.cos(2 * math.pi * n * (t + L / 2) / L) / math.sqrt(L)
            a1.plot(t, yv, color=S(i + 1), label="n = %d" % n)
        a1.axhline(0, color=T["axis"], lw=0.8)
        a1.set_xlim(-L / 2, L / 2)
        a1.set_xlabel("log u  (window [-L/2, L/2], L = log 13)")
        a1.set_ylabel("Re V_n(u)")
        a1.legend(loc="lower center", ncol=4, bbox_to_anchor=(0.5, 1.0))
        a1.set_title("Fourier test functions V_n, x = 13", pad=24)
        # bump
        a2.fill_between(xs, 0, bump, color=S(1), alpha=T["wash"], lw=0)
        a2.plot(xs, bump, color=S(1), label="phi_delta(log u - log 6),  delta = 0.0771")
        a2.plot(xs, corr, color=S(2), label="(phi^* * phi)(y - log 6), support 2 delta (scaled)")
        for k, lk in ((5, l5), (7, l7), (6, l6)):
            if k == 6:
                a2.axvline(lk, color=T["axis"], lw=0.8)
                a2.text(lk, 1.12, "log 6", ha="center", fontsize=8, color=T["ink2"])
            else:
                a2.plot([lk, lk], [0, 0.9], color=T["ink2"], lw=1.2)
                a2.plot([lk], [0.9], "o", color=T["ink2"], ms=4.5, **C.ring())
                a2.text(lk, 0.97, "log %d" % k, ha="center", fontsize=8, color=T["ink2"])
        a2.annotate("", xy=(l6 + 2 * d, 0.45), xytext=(l6, 0.45),
                    arrowprops=dict(arrowstyle="<->", color=T["ink2"], lw=0.8))
        a2.text(l6 + d, 0.48, "2 delta_max", ha="center", fontsize=8, color=T["ink2"])
        a2.set_ylim(0, 1.55)
        a2.set_xlim(1.52, 2.08)
        a2.set_xlabel("log u")
        a2.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=1)
        a2.set_title("Why admissibility bounds delta", pad=34)
        C.note(a2, "2 delta_max = log 7 - log 6: at delta_max\nthe support of phi^* * phi reaches log 7", x=0.02, y=0.99)
        fig.subplots_adjust(left=0.07, right=0.985, top=0.8, bottom=0.13)
        return fig
    C.render("s0_testfns", draw)
    return dict(id="s0_testfns", step="Step 0", title="Test functions: the Fourier basis and the lattice bump",
                caption=("Left: real parts of the Fourier test functions V_n(u) = L^(-1/2) exp(2 pi i n (log u + L/2)/L) on the "
                         "centred x = 13 window, n = 0, 1, 2, 5. Right: the C_c^infinity bump phi_delta centred at log 6 "
                         "(the lattice point 2 * 3 of {2,3}, A = 1) with delta = delta_max = 0.07708 from lane A2's admissible "
                         "table, and its autocorrelation phi^* * phi (scaled to peak 1), supported within 2 delta. At "
                         "delta_max the support reaches log 7 exactly (2 delta_max = log 7 - log 6); any larger delta lets the "
                         "foreign prime power 7 into the Gram entry of the ratio 6. log 5 is further away."),
                panels=["V_n (closed form)", "bump and autocorrelation (floating-point quadrature); delta_max from lane A2 (certified)"],
                kind="closed form", sources=[C.rel(C.A2_OUT) + " (admissible delta table)"], script=SCRIPT)


def fig_lattice():
    cases = [((2, 3), 3), ((2, 3, 5), 2)]
    binding = {((2, 3), 3): (108, 109), ((2, 3, 5), 2): (450, 449)}
    adm = {(r["S"], r["A"]): r for r in C.a2_admissible()}
    tab = []
    for Sset, A in cases:
        import itertools
        for e in itertools.product(range(A + 1), repeat=len(Sset)):
            n = 1
            for p, a in zip(Sset, e):
                n *= p ** a
            tab.append(("{" + ",".join(map(str, Sset)) + "}", A, "(" + ",".join(map(str, e)) + ")", n, sum(e), math.log(n)))
    C.write_table("s0_lattice", ["S", "A", "exponents", "n", "degree", "log_n"], tab,
                  ["lattice points log(prod p^a_p), exact"])

    def draw():
        import itertools
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(2, 1, figsize=(10, 6.4), gridspec_kw=dict(hspace=0.55))
        for ax, (Sset, A) in zip(axes, cases):
            pts = []
            for e in itertools.product(range(A + 1), repeat=len(Sset)):
                n = 1
                for p, a in zip(Sset, e):
                    n *= p ** a
                pts.append((n, sum(e), e))
            maxdeg = A * len(Sset)
            nmax = max(p[0] for p in pts)
            ramp = T["seq"][1:] if T["name"] == "light" else T["seq"][2:]
            foreign = [k for k in PP if k <= nmax * 1.05 and all(q not in Sset for q in [PP[k]])]
            for k in foreign:
                ax.plot([math.log(k)] * 2, [-1.05, -0.55], color=T["muted"], lw=0.8)
            ax.text(-0.05, -0.8, "foreign\nprime powers", ha="right", va="center", fontsize=7, color=T["ink2"])
            for n, deg, e in pts:
                c = ramp[min(len(ramp) - 1, int(round(deg * (len(ramp) - 1) / maxdeg)))]
                ax.plot([math.log(n)], [deg], "o", color=c, ms=7, **C.ring())
                if len(Sset) == 2 or deg <= 2 or n in binding[(Sset, A)]:
                    ax.text(math.log(n), deg + 0.32, str(n), ha="center", va="bottom", fontsize=6.5, color=T["ink2"])
            r, k = binding[(Sset, A)]
            ax.annotate("binding pair %d vs %d:\ndelta_max = %.4g" % (r, k, adm[(Sset, A)]["dmax"]),
                        xy=(math.log(r), -0.55), xytext=(math.log(r) - 1.6, -0.2 + maxdeg * 0.25),
                        fontsize=7.5, color=T["ink"], arrowprops=dict(arrowstyle="-", color=T["ink2"], lw=0.7))
            ax.set_ylim(-1.3, maxdeg + 1.0)
            ax.set_yticks(range(maxdeg + 1))
            ax.set_ylabel("degree  sum a_p")
            ax.set_xlim(-0.3, math.log(nmax) + 0.3)
            ax.set_xlabel("log n,  n = prod p^(a_p)")
            ax.set_title("{%s}, 0 <= a_p <= %d: %d lattice points; colour = degree (light = low)"
                         % (",".join(map(str, Sset)), A, len(pts)))
        fig.subplots_adjust(left=0.1, right=0.985, top=0.93, bottom=0.08)
        return fig
    C.render("s0_lattice", draw)
    return dict(id="s0_lattice", step="Step 0", title="The prime-content lattices on the line",
                caption=("Lattice points log(prod p^(a_p)) of the prime-content channel, one row per degree sum a_p (colour "
                         "repeats the degree on a one-hue ramp). Top: {2,3}, A <= 3 (16 points). Bottom: {2,3,5}, A <= 2 "
                         "(27 points; only degree <= 2 and the binding point are labelled). Grey ticks: prime powers not "
                         "built from the lattice primes (foreign prime powers), up to the largest lattice point. Annotated: "
                         "the binding pair of lane A2's admissible-delta table (a lattice ratio next to a foreign prime power), "
                         "which sets delta_max."),
                panels=["{2,3} lattice (exact)", "{2,3,5} lattice (exact); delta_max from lane A2 (certified)"],
                kind="exact", sources=[C.rel(C.A2_OUT) + " (admissible delta table)"], script=SCRIPT)


def fig_convolution():
    l4, l6 = math.log(4), math.log(6)
    D = l6 - l4
    deltas = [(0.01232, "delta = 0.01232 (0.9 delta_max, {2,3} A = 2): admissible"),
              (0.16, "delta = 0.16: not admissible")]
    xs = np.linspace(1.0, 2.2, 3000)
    ys = np.linspace(0, 1.25, 3000)
    rows = []
    for d, _ in deltas:
        q = R(ys - D, d) + R(ys + D, d)
        for yv, qv in zip(ys[::30], q[::30]):
            rows.append((d, float(yv), float(qv / q.max())))
    C.write_table("s0_convolution", ["delta", "y", "q_scaled"], rows,
                  ["q(y) = R_delta(y - log 3/2) + R_delta(y + log 3/2), scaled to peak 1 (floating point)"])

    def draw():
        import matplotlib.pyplot as plt
        fig, (a1, a2) = plt.subplots(2, 1, figsize=(10, 5.8), gridspec_kw=dict(hspace=0.5))
        for i, (d, lab) in enumerate(deltas):
            for c0 in (l4, l6):
                b = phi(xs - c0, d)
                a1.fill_between(xs, 0, b, color=S(i + 1), alpha=T["wash"], lw=0, rasterized=True)
                a1.plot(xs, b, color=S(i + 1), label=lab if c0 == l4 else None)
        for k in (3, 4, 5, 7, 8):
            a1.plot([math.log(k)] * 2, [0, 0.55], color=T["muted"], lw=0.9)
            a1.text(math.log(k), 0.6, "log %d" % k, ha="center", fontsize=7.5, color=T["ink2"])
        a1.set_xlim(1.0, 2.2)
        a1.set_ylim(0, 0.5)
        a1.set_ylim(0, 0.72)
        a1.set_xlabel("log u")
        a1.set_title("Two lattice bumps, phi_alpha at log 4 = log 2^2 and phi_beta at log 6 = log 2*3 (a mixed pair)", pad=26)
        a1.legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2)
        a1.set_yticks([0, 0.2])
        for i, (d, lab) in enumerate(deltas):
            q = R(ys - D, d) + R(ys + D, d)
            a2.fill_between(ys, 0, q / q.max(), color=S(i + 1), alpha=T["wash"], lw=0, rasterized=True)
            a2.plot(ys, q / q.max(), color=S(i + 1))
        for k in (2, 3):
            lk = math.log(k)
            a2.plot([lk, lk], [0, -lam_weight(k)], color=T["ink2"], lw=1.4)
            a2.plot([lk], [-lam_weight(k)], "o", color=T["ink2"], ms=4.5, **C.ring())
            a2.text(lk + 0.015, -lam_weight(k), "-Lambda(%d) %d^(-1/2)" % (k, k), va="center", fontsize=7.5, color=T["ink2"])
        a2.axhline(0, color=T["axis"], lw=0.8)
        a2.axvline(D, color=T["axis"], lw=0.8)
        a2.text(D - 0.01, 0.9, "log(6/4)\n= log(3/2)", ha="right", fontsize=8, color=T["ink2"])
        for i, (d, lab) in enumerate(deltas):
            yb = 1.32 - 0.14 * i
            a2.plot([D - 2 * d, D + 2 * d], [yb, yb], color=S(i + 1), lw=3, solid_capstyle="butt")
            a2.text(0.76, yb, "support [log 3/2 - 2 delta, log 3/2 + 2 delta], delta = %g" % d,
                    va="center", fontsize=7.5, color=T["ink2"])
        a2.plot([math.log(2)] * 2, [-lam_weight(2), 1.1], color=T["ink2"], lw=0.7)
        a2.text(math.log(2) + 0.012, 0.45, "log 2: at delta = 0.16 the support\ncrosses it and the 2-comb enters\na mixed entry",
                fontsize=7.5, color=T["ink"], va="center")
        C.note(a2, "admissible delta: no prime power in the support;\nthe mixed entry is pole + archimedean only",
               x=0.01, y=0.06, va="bottom")
        a2.set_xlim(0, 1.25)
        a2.set_ylim(-0.8, 1.45)
        a2.set_xlabel("y  (dilation of f^* * g)")
        a2.set_ylabel("q(y), scaled")
        a2.set_title("q(y) = (phi_alpha^* * phi_beta)(y) + (phi_alpha^* * phi_beta)(-y) and the prime comb")
        fig.subplots_adjust(left=0.08, right=0.985, top=0.86, bottom=0.09)
        return fig
    C.render("s0_convolution", draw)
    return dict(id="s0_convolution", step="Step 0", title="The convolution picture for a mixed pair",
                caption=("Bumps phi_alpha at log 4 and phi_beta at log 6 (lattice points (2,0) and (1,1) of {2,3}, A = 2, which "
                         "differ in both coordinates: a mixed entry). phi_alpha^* * phi_beta is supported within 2 delta of "
                         "log(6/4) = log(3/2) = 0.405. At the admissible delta = 0.01232 (0.9 delta_max of lane A2) the support "
                         "touches no prime power, so the Gram entry is pole plus archimedean only. At delta = 0.16 the support "
                         "(half-width 0.32) crosses log 2 = 0.693 and the 2-comb enters a mixed entry: admissibility fails. "
                         "q is scaled to peak 1 for each delta; comb weights are exact."),
                panels=["bumps on the log u line (closed form)", "q(y) (floating-point autocorrelation) and comb (exact)"],
                kind="closed form", sources=[C.rel(C.A2_OUT) + " (delta grid)"], script=SCRIPT)


def run():
    entries = [fig_line(), fig_testfns(), fig_lattice(), fig_convolution()]
    C.register(STEP, entries)
    return entries


if __name__ == "__main__":
    run()
