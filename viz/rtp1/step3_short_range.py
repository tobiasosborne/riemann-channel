"""Step 3 of viz-brief.md: short-range positivity (lane B1 statements) (lane V; claude:opus).

Panels: the Weil distribution near the origin (closed form); q = phi_delta^* * phi_delta for a bump inside
|y| < log 2 and one widened past it (floating-point autocorrelation); and the normalised form value
QW(phi_delta, phi_delta)/||phi_delta||^2 against delta split into pole, archimedean and prime parts.  The curve is
floating point (autocorrelation on a grid, trapezoid rule); for delta <= 0.2 it is checked against lane A2's
certified diagonal (scripts/rtp1_prime_content.py: entry(1, delta)), which are also drawn as dots.  No zeros.
Caption statements are lane B1's (notes/rtp-round-1/lane-B1.md sections 1-2), read at run time for existence.
"""
import math
import os

import numpy as np

import bridges
import common as C
from common import T, S
from step0_objects import R, lam_weight, rho, _R1, _SG

STEP = "step3"
SCRIPT = "viz/rtp1/step3_short_range.py"
B1 = os.path.join(C.REPO, "notes", "rtp-round-1", "lane-B1.md")
EG = 0.57721566490153286061
R10 = float(np.interp(0.0, _SG, _R1))
PP = C.prime_powers(50)


def check(cond, msg):
    print(("  ok    " if cond else "  FAIL  ") + msg)
    if not cond:
        raise SystemExit("check failed: " + msg)


def form_parts(d):
    """(pole, arch, prime) contributions to QW(phi_d, phi_d)/||phi_d||^2 (signs as they enter Psi), floating point"""
    Y = 2 * d
    y = np.linspace(0, Y, 40001)
    q = 2 * R(y, d)
    q0 = q[0]
    nrm = d * R10
    pole = np.trapezoid(q * 2 * np.cosh(y / 2), y)
    f = np.empty_like(y)
    f[1:] = (q[1:] - np.exp(-y[1:] / 2) * q0) * rho(y[1:])
    f[0] = q0 / 4                                          # limit y -> 0: (q0 y/2)(1/(2y)) + q'(0) term (q'(0) = 0)
    arch = (math.log(4 * math.pi) + EG) * q0 / 2 + np.trapezoid(f, y) + q0 / 2 * math.log(math.tanh(Y / 2))
    prime = sum(lam_weight(k) * 2 * float(R(math.log(k), d)) for k in PP if math.log(k) < Y)
    return pole / nrm, -arch / nrm, -prime / nrm


def b1_status():
    if not os.path.exists(B1):
        return None
    txt = open(B1).read()
    return dict(yoshida=("Theorem 1" in txt and "log 2 / 2" in txt), bombieri=("Theorem 12" in txt))


def fig_short():
    st = b1_status()
    ns = bridges.a2()
    cert = []
    for dls in ("0.02", "0.05", "0.1", "0.15", "0.2"):
        e = ns["entry"](__import__("fractions").Fraction(1), dls)
        nrm = float(dls) * float(ns["R10"].mid().str(30, radius=False))
        tot = float((e["total"]).mid().str(30, radius=False)) / nrm
        pole = float(e["pole"].mid().str(30, radius=False)) / nrm
        cert.append((float(dls), tot, pole))
        fp = form_parts(float(dls))
        check(abs(sum(fp) - tot) < 2e-4 and abs(fp[0] - pole) < 2e-5,
              "delta = %s: floating form value %.6f (pole %.6f) vs lane A2 certified %.6f (pole %.6f)"
              % (dls, sum(fp), fp[0], tot, pole))
    ds = np.round(np.linspace(0.02, 0.8, 157), 6)
    parts = np.array([form_parts(d) for d in ds])
    C.write_table("s3_short_range", ["delta", "pole", "archimedean", "prime", "total"],
                  [(float(d), p[0], p[1], p[2], float(sum(p))) for d, p in zip(ds, parts)],
                  ["QW(phi_delta, phi_delta)/||phi_delta||^2 split by term, floating point (autocorrelation on a grid);",
                   "certified check points from lane A2 (entry(1, delta)) at delta = 0.02, 0.05, 0.1, 0.15, 0.2"])
    yosh = math.log(2) / 2
    tot_all = parts.sum(axis=1)
    check(bool(np.all(tot_all > 0)), "the single-bump form value stays positive on the whole delta grid (floating point)")
    far = ds > 0.5
    i_min = int(np.argmin(np.where(far, tot_all, np.inf)))
    v_yosh = sum(form_parts(yosh))
    in_d, out_d = 0.25, 0.45
    v_in = sum(form_parts(in_d))
    v_out = form_parts(out_d)

    def draw():
        import matplotlib.pyplot as plt
        fig = plt.figure(figsize=(11.5, 8.2))
        gs = fig.add_gridspec(2, 2, height_ratios=[1, 1.05], hspace=0.42, wspace=0.22)
        a1 = fig.add_subplot(gs[0, 0])
        a2 = fig.add_subplot(gs[0, 1])
        g2 = gs[1, :].subgridspec(1, 2, width_ratios=[1.55, 1], wspace=0.22)
        a3 = fig.add_subplot(g2[0])
        a4 = fig.add_subplot(g2[1])
        y = np.linspace(0.01, 1.45, 900)
        a1.axvspan(0, math.log(2), color=T["mid"], lw=0, zorder=0)
        a1.plot(y, 2 * np.cosh(y / 2), color=S(1), label="pole +2 cosh(y/2)")
        a1.plot(y, -rho(y), color=S(2), label="archimedean -rho(y)")
        a1.plot(y, 2 * np.cosh(y / 2) - rho(y), color=S(3), label="sum")
        for k in (2, 3, 4):
            lk = math.log(k)
            a1.plot([lk, lk], [0, -lam_weight(k)], color=T["ink2"], lw=1.4)
            a1.plot([lk], [-lam_weight(k)], "o", color=T["ink2"], ms=4.5, **C.ring())
            a1.text(lk, -lam_weight(k) - 0.25, "log %d" % k, ha="center", fontsize=7.5, color=T["ink2"], va="top")
        a1.axhline(0, color=T["axis"], lw=0.8)
        a1.text(0.02, 2.9, "|y| < log 2:\nno prime mass", fontsize=7.5, color=T["ink2"])
        a1.set_ylim(-3, 3.4)
        a1.set_xlim(0, 1.45)
        a1.set_xlabel("y")
        a1.set_title("(a) the Weil distribution near the origin")
        a1.legend(loc="lower right", fontsize=7.5)
        yy = np.linspace(0, 1.2, 1200)
        a2.axvspan(0, math.log(2), color=T["mid"], lw=0, zorder=0)
        for i, (d, lab) in enumerate(((in_d, "delta = %.2f: 2 delta < log 2, QW/||phi||^2 = %+.3f" % (in_d, v_in)),
                                      (out_d, "delta = %.2f: 2 delta > log 2, 2-comb part %+.4f" % (out_d, v_out[2])))):
            q = 2 * R(yy, d)
            a2.fill_between(yy, 0, q / q.max(), color=S(4 + i), alpha=T["wash"], lw=0)
            a2.plot(yy, q / q.max(), color=S(4 + i), label=lab)
        lk = math.log(2)
        a2.plot([lk, lk], [0, -lam_weight(2)], color=T["ink2"], lw=1.4)
        a2.plot([lk], [-lam_weight(2)], "o", color=T["ink2"], ms=4.5, **C.ring())
        a2.text(lk + 0.02, -lam_weight(2), "-Lambda(2) 2^(-1/2)", fontsize=7.5, color=T["ink2"], va="center")
        a2.axhline(0, color=T["axis"], lw=0.8)
        a2.set_ylim(-0.7, 1.15)
        a2.set_xlabel("y")
        a2.set_ylabel("q(y) = 2 (phi^* * phi)(y), scaled")
        a2.set_title("(b) a bump inside, and widened past log 2")
        a2.legend(loc="upper right", fontsize=7.5)
        cols = [S(1), S(2), S(6), S(7)]
        labs = ["pole", "archimedean (-W_R)", "prime (-sum W_p)", "total QW / ||phi||^2"]
        for j in range(3):
            a3.plot(ds, parts[:, j], color=cols[j], lw=1.4, label=labs[j])
        a3.plot(ds, parts.sum(axis=1), color=cols[3], lw=2.0, label=labs[3])
        a3.plot([c[0] for c in cert], [c[1] for c in cert], "o", color=cols[3], ms=7,
                label="lane A2 certified diagonal (delta <= 0.2)", **C.ring())
        a3.axhline(0, color=T["axis"], lw=0.8)
        a3.axvline(yosh, color=T["ink2"], lw=0.9)
        a3.text(yosh - 0.006, -1.9, "delta = log 2 / 2:\nYoshida's range ends,\nthe 2-comb enters", fontsize=7.5,
                color=T["ink"], va="top", ha="right")
        for k, lab in ((3, "log 3 / 2"),):
            a3.axvline(math.log(k) / 2, color=T["axis"], lw=0.8)
            a3.text(math.log(k) / 2 + 0.004, -2.3, lab, fontsize=7.5, color=T["ink2"])
        a3.set_xlabel("delta (bump phi_delta supported in [-delta, delta]; phi^* * phi in [-2 delta, 2 delta])")
        a3.set_ylabel("contribution to QW(phi, phi) / ||phi||^2")
        a3.set_xlim(0, 0.81)
        a3.set_ylim(-2.6, 3.4)
        a3.set_title("(c) the form value of one bump, split by term")
        a3.legend(loc="upper right", ncol=1, fontsize=7.5)
        tot = parts.sum(axis=1)
        a4.semilogy(ds, tot, color=cols[3], lw=2.0)
        a4.semilogy([c[0] for c in cert], [c[1] for c in cert], "o", color=cols[3], ms=7, **C.ring())
        a4.axvline(yosh, color=T["ink2"], lw=0.9)
        a4.axvline(math.log(3) / 2, color=T["axis"], lw=0.8)
        a4.set_xlabel("delta")
        a4.set_ylabel("total QW / ||phi||^2 (log scale)")
        a4.set_title("(d) the total: a near-cancellation")
        a4.set_xlim(0, 0.81)
        fig.suptitle("Short-range positivity: below log 2 the form is pole plus archimedean only", x=0.06, ha="left",
                     fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.07, right=0.985, top=0.92, bottom=0.07)
        return fig
    C.render("s3_short_range", draw)
    if st and st["yoshida"] and st["bombieri"]:
        stmt = ("Statements as lane B1 reports them (notes/rtp-round-1/lane-B1.md sections 1-2, byte-cited there): "
                "Yoshida 1992, Theorem 1 (k = Q, a = log 2 / 2): <phi, phi> = T_Q(phi * phi~) >= 0 for every smooth phi "
                "supported in [-a, a], with equality only for phi = 0; unconditional and computer-assisted. On that space "
                "the prime sum vanishes, so the theorem is about the pole plus archimedean form; beyond width log 2 nothing "
                "is proved. Bombieri 2000, Theorem 12: for F supported in an interval of length |I| < log 2, "
                "T[F * F(-x)-bar] >= (log(1/|I|) - log^+ log(1/|I|) - O(1)) ||F||^2, with the O(1) unspecified, so it "
                "gives positivity only for |I| small enough; the log 2 range is Yoshida's. The archimedean term alone is "
                "not positive on this space (lane B1: for the even box of width log 2 the archimedean part is -1.217, the "
                "pole part +1.400). ")
    else:
        stmt = "Statement pending lane B1. "
    return dict(id="s3_short_range", step="Step 3", title="Short-range positivity",
                caption=(stmt + "Figure: (a) the Weil distribution near y = 0 (pole, archimedean, their sum; grey: |y| < log 2, "
                         "where the prime comb has no mass). (b) q(y) = 2 (phi_delta^* * phi_delta)(y) for the bump at "
                         "delta = 0.25 (support of q inside log 2; its normalised form value is positive) and widened to "
                         "delta = 0.45 (support past log 2: the 2-comb enters with weight R_delta(log 2)). (c) The normalised "
                         "form value of one centred bump against delta, split into its pole, archimedean and prime parts. The "
                         "prime part is zero up to delta = log 2 / 2, where Yoshida's range ends (vertical line; the second line "
                         "is log 3 / 2, where the 3-comb enters). The archimedean part carries the logarithmic self-energy: "
                         "positive for small delta, negative past delta ~ 0.135, and it nearly cancels the growing pole part. "
                         "(d) The total on a log scale: it grows like -log delta as delta -> 0 (lane A2: d = -log delta - "
                         "1.9555 + O(delta)), the growth of Bombieri's lower bound, and it falls to %.1e at log 2 / 2 and to "
                         "%.1e near delta = %.3f while staying positive for this one bump. One test function only: a positive "
                         "value here is a single diagonal entry, not a theorem. Curves: floating point; dots: lane A2's certified values."
                         % (v_yosh, tot_all[i_min], ds[i_min])),
                panels=["Weil distribution near 0 (closed form)", "q for two widths (floating point)",
                        "form value split by term (floating point; certified dots from lane A2)",
                        "total, log scale (floating point; certified dots)"],
                kind="closed form + floating point; certified check points",
                sources=["notes/rtp-round-1/lane-B1.md (statements)", "scripts/rtp1_prime_content.py (entry, certified dots)"],
                script=SCRIPT, b1=bool(st))


def run():
    entries = [fig_short()]
    C.register(STEP, entries)
    return entries


if __name__ == "__main__":
    run()
