"""Step 2 of viz-brief.md: the prime-content channel (lane A2) (lane V; claude:opus).

Gram matrices and eigenvectors come from lane A2's own functions (scripts/rtp1_prime_content.py: build,
entry, min_eig, delta_grid), loaded through bridges.a2() and called exactly as lane A2 calls them (arb balls
at 200 bits; midpoints plotted).  Scaling and delta_max panels are parsed from outputs/rtp1_prime_content.txt
(not recomputed).  The explicit-formula panels are a comparison step (zeros used, labelled): the prime-side
values and the certified truncation errors are parsed from the output; the partial-sum curves are recomputed
in floating point from certified zeros (python-flint acb.zeta_zeros) and a Gauss-Legendre transform of the bump.
"""
import math

import numpy as np

import bridges
import common as C
from common import T, S

STEP = "step2"
SCRIPT = "viz/rtp1/step2_prime_content.py"
SETCOL = {(2,): 1, (2, 3): 2, (2, 3, 5): 3}          # colour follows the prime set
LOG = []


def check(cond, msg):
    print(("  ok    " if cond else "  FAIL  ") + msg)
    if not cond:
        raise SystemExit("check failed: " + msg)


def fs(S_):
    return "{" + ",".join(map(str, S_)) + "}"


def mid(a):
    return float(a.mid().str(25, radius=False))


def gram_parts(S_, A, dls):
    ns = bridges.a2()
    pts, parts, cls, mats, nrm = ns["build"](S_, A, dls)
    n = len(pts)
    G = np.zeros((n, n))
    noP = np.zeros((n, n))
    mixP = np.zeros((n, n))
    mixA = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            e = parts[(min(i, j), max(i, j))]
            G[i, j] = mid(e["total"] / nrm)
            noP[i, j] = mid((e["pole"] - e["arch"]) / nrm)
            if cls[(min(i, j), max(i, j))] >= 2:
                mixP[i, j] = mid(e["pole"] / nrm)
                mixA[i, j] = -mid(e["arch"] / nrm)
    return dict(pts=pts, mats=mats, G=G, noP=noP, mixP=mixP, mixA=mixA, mix=mixP + mixA, cls=cls)


# ---------------------------------------------------------------------------------------------------
def fig_gram():
    ns = bridges.a2()
    S_, A = (2, 3), 2
    dls = ns["delta_grid"](S_, A)[0][1]
    g = gram_parts(S_, A, dls)
    check(dls == "0.01232", "{2,3}, A = 2: 0.9 delta_max rounds to lane A2's grid value 0.01232")
    check(abs(g["G"][0, 0] - 2.47301) < 1e-5, "diagonal d = %.6f = lane A2's summary value 2.47301" % g["G"][0, 0])
    ev = np.linalg.eigvalsh(g["G"])[0]
    check(abs(ev - 0.76014856) < 1e-7, "lambda_min of the plotted matrix %.8f = lane A2's certified 0.76014856" % ev)
    mixed = np.array([[g["cls"][(min(i, j), max(i, j))] >= 2 for j in range(9)] for i in range(9)])
    check(np.abs(g["G"][mixed] - g["mix"][mixed]).max() < 1e-15,
          "every mixed entry of G equals its pole part plus its archimedean part (no prime term)")
    labels = ["(%d,%d)" % p for p in g["pts"]]
    rows = []
    for i in range(9):
        for j in range(9):
            rows.append((labels[i], labels[j], g["G"][i, j], g["noP"][i, j], g["mix"][i, j], g["mixP"][i, j], g["mixA"][i, j]))
    C.write_table("s2_gram", ["alpha", "beta", "G", "G_prime_free", "mixed", "mixed_pole", "mixed_arch"], rows,
                  ["{2,3}, A = 2, delta = 0.01232, normalised by ||phi||^2; lane A2 functions (arb, midpoints)",
                   "mixed_arch is the archimedean contribution to G (= -W_R part), mixed_pole the pole contribution"])
    v1 = float(np.abs(np.r_[g["G"].ravel(), g["noP"].ravel()]).max())
    v2 = float(np.abs(np.r_[g["mixP"].ravel(), g["mixA"].ravel(), g["mix"].ravel()]).max())

    def draw():
        import matplotlib.pyplot as plt
        fig = plt.figure(figsize=(12.5, 4.5))
        gs = fig.add_gridspec(2, 7, height_ratios=[1, 0.05], width_ratios=[1, 1, 0.25, 1, 1, 1, 0.02],
                              hspace=0.55, wspace=0.12)
        panels = [(g["G"], "G", v1, 0), (g["noP"], "prime-free part\n(pole + archimedean)", v1, 1),
                  (g["mix"], "mixed entries\n(>= 2 coordinates differ)", v2, 3),
                  (g["mixP"], "pole part of\nthe mixed entries", v2, 4), (g["mixA"], "archimedean part of\nthe mixed entries", v2, 5)]
        ims = {}
        for M, title, vm, col in panels:
            ax = fig.add_subplot(gs[0, col])
            im = ax.imshow(M, cmap=C.cmap_div(), vmin=-vm, vmax=vm)
            ims[vm] = im
            ax.set_xticks(range(9))
            ax.set_xticklabels(labels, rotation=90, fontsize=7)
            ax.set_yticks(range(9))
            ax.set_yticklabels(labels if col in (0, 3) else [], fontsize=7)
            ax.grid(False)
            ax.set_title(title, fontsize=9)
            for sp in ax.spines.values():
                sp.set_visible(False)
        for vm, cols, lab in ((v1, (0, 2), "G entries (shared scale)"), (v2, (3, 6), "mixed parts (shared scale)")):
            cax = fig.add_subplot(gs[1, cols[0]:cols[1]])
            cb = fig.colorbar(ims[vm], cax=cax, orientation="horizontal")
            cb.outline.set_visible(False)
            cb.set_label(lab, color=T["ink2"])
        fig.suptitle("Gram matrix of the {2,3} lattice, A = 2, delta = 0.01232 (0.9 delta_max), normalised by ||phi||^2",
                     x=0.04, ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.06, right=0.99, top=0.8, bottom=0.1)
        return fig
    C.render("s2_gram", draw)
    return dict(id="s2_gram", step="Step 2", title="Gram matrix of the {2,3} lattice and its mixed entries",
                caption=("Lane A2's Gram matrix G_(alpha beta) = QW(phi_alpha, phi_beta)/||phi||^2 on {2,3}, A = 2 (lattice points "
                         "(a, b) = exponents of 2 and 3), at delta = 0.01232 = 0.9 delta_max. Left pair, one scale: G and its "
                         "prime-free part (pole plus archimedean; the difference is the 2- and 3-combs on the axis-type "
                         "entries). Right triple, one scale: the mixed entries (lattice points differing in both coordinates), "
                         "and their pole and archimedean parts, which sum to them exactly: the mixed entries carry no prime term. "
                         "The pole part is positive and dominates; the archimedean part is negative (lane A2's correction of the "
                         "note: the cross-place information is pole plus archimedean, pole first). Entries from lane A2's "
                         "certified routines (arb balls, 200 bits), midpoints plotted; lambda_min 0.76015 matches its table."),
                panels=["G", "prime-free part", "mixed entries", "pole part of mixed", "archimedean part of mixed"],
                kind="certified (lane A2 routines, arb midpoints)", sources=["scripts/rtp1_prime_content.py (build)",
                                                                             C.rel(C.A2_OUT) + " (lambda_min check)"],
                script=SCRIPT)


# ---------------------------------------------------------------------------------------------------
def eig_case(S_, A):
    ns = bridges.a2()
    dls = ns["delta_grid"](S_, A)[0][1]
    pts, parts, cls, mats, nrm = ns["build"](S_, A, dls)
    E = ns["min_eig"](mats["G"])
    E0 = ns["min_eig"](mats["G_nomix"])
    check(E["certified"] and E0["certified"], "%s, A = %d, delta = %s: both minimal eigenpairs certified simple" % (fs(S_), A, dls))
    v = np.array([mid(x) for x in E["vec"]])
    v0 = np.array([mid(x) for x in E0["vec"]])
    if v @ v0 < 0:
        v0 = -v0
    shape = (A + 1,) * len(S_)
    return dict(S=S_, A=A, dls=dls, pts=pts, v=v.reshape(shape), v0=v0.reshape(shape), lam=mid(E["lam"]),
                lam0=mid(E0["lam"]))


def schmidt(v, axis):
    M = np.moveaxis(v, axis, 0).reshape(v.shape[axis], -1)
    s = np.linalg.svd(M, compute_uv=False)
    return 1 - s[0] ** 2 / np.sum(s ** 2)


def fig_eigvec():
    summ = {(r["S"], r["A"], r["delta"]): r for r in C.a2_summary()}
    cases = [eig_case((2, 3), 2), eig_case((2, 3), 3), eig_case((2, 3, 5), 2)]
    for c in cases:
        ref = summ[(c["S"], c["A"], float(c["dls"]))]
        sd = max(schmidt(c["v"], k) for k in range(len(c["S"])))
        check(abs(c["lam"] - ref["lam"]) < 1e-6 and abs(sd / ref["schmidt"] - 1) < 0.01,
              "%s, A = %d: lambda %.8f and Schmidt defect %.3g match lane A2's table (%.8f, %.3g)"
              % (fs(c["S"]), c["A"], c["lam"], sd, ref["lam"], ref["schmidt"]))
        c["schmidt"] = sd
        sd0 = max(schmidt(c["v0"], k) for k in range(len(c["S"])))
        check(sd0 < 1e-12, "%s, A = %d: the eigenvector with mixed entries zeroed is a product state (Schmidt defect %.1e)"
              % (fs(c["S"]), c["A"], sd0))
    rows = []
    for c in cases:
        for p, a, b in zip(c["pts"], c["v"].ravel(), c["v0"].ravel()):
            rows.append((fs(c["S"]), c["A"], c["dls"], str(p), a, b, a - b))
    C.write_table("s2_eigvec", ["S", "A", "delta", "lattice_point", "v_min(G)", "v_min(G_nomix) (product state)", "difference"],
                  rows, ["lane A2 routines (certified simple minimal eigenpairs, arb midpoints); sign: largest component positive"])

    def panel(ax, M, vmax, title, cmap, xl, yl, ticks=True):
        im = ax.imshow(M, cmap=cmap, vmin=(-vmax if cmap.name.startswith("rtp1_div") else 0), vmax=vmax, origin="lower")
        ax.set_title(title, fontsize=9)
        ax.grid(False)
        ax.set_xticks(range(M.shape[1]))
        ax.set_yticks(range(M.shape[0]))
        ax.set_xlabel(xl)
        ax.set_ylabel(yl)
        for sp in ax.spines.values():
            sp.set_visible(False)
        for (i, j), val in np.ndenumerate(M):
            r, g, b, _ = im.cmap(im.norm(val))
            lum = 0.2126 * r ** 2.2 + 0.7152 * g ** 2.2 + 0.0722 * b ** 2.2
            col = "#0b0b0b" if lum > 0.3 else "#ffffff"            # label inside a fill: ink by fill luminance
            ax.text(j, i, ("%.3f" % val) if cmap.name.startswith("rtp1_seq") else ("%.1e" % val), ha="center", va="center",
                    fontsize=6.5 if M.shape[0] <= 3 else 5.8, color=col)
        return im

    def draw23():
        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(2, 3, figsize=(11, 7.6), gridspec_kw=dict(hspace=0.45, wspace=0.3))
        for r, c in enumerate(cases[:2]):
            vm = float(max(c["v"].max(), c["v0"].max()))
            # array index [a, b]: rows = exponent of 2 (a), columns = exponent of 3 (b)
            panel(axs[r, 0], c["v"], vm, "v_min(G), %s A = %d" % (fs(c["S"]), c["A"]), C.cmap_seq(), "b (exponent of 3)",
                  "a (exponent of 2)")
            panel(axs[r, 1], c["v0"], vm, "product state (mixed entries zeroed)", C.cmap_seq(), "b", "a")
            dm = float(np.abs(c["v"] - c["v0"]).max())
            panel(axs[r, 2], c["v"] - c["v0"], dm, "difference; Schmidt defect %.2g" % c["schmidt"], C.cmap_div(), "b", "a")
        fig.suptitle("Minimal eigenvector on the {2,3} lattice vs the product state, delta = 0.9 delta_max",
                     x=0.05, ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.07, right=0.985, top=0.9, bottom=0.07)
        return fig

    def draw235():
        import matplotlib.pyplot as plt
        c = cases[2]
        fig, axs = plt.subplots(3, 3, figsize=(10, 9.6), gridspec_kw=dict(hspace=0.5, wspace=0.3))
        vm = float(max(c["v"].max(), c["v0"].max()))
        dm = float(np.abs(c["v"] - c["v0"]).max())
        for k in range(3):
            panel(axs[k, 0], c["v"][:, :, k], vm, "v_min(G), slice c = %d" % k, C.cmap_seq(), "b (exponent of 3)",
                  "a (exponent of 2)")
            panel(axs[k, 1], c["v0"][:, :, k], vm, "product state, c = %d" % k, C.cmap_seq(), "b", "a")
            panel(axs[k, 2], (c["v"] - c["v0"])[:, :, k], dm, "difference, c = %d" % k, C.cmap_div(), "b", "a")
        fig.suptitle("{2,3,5}, A = 2, delta = %s: three slices c = exponent of 5 (Schmidt defect %.2g)" % (c["dls"], c["schmidt"]),
                     x=0.05, ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.08, right=0.985, top=0.92, bottom=0.06)
        return fig
    C.render("s2_eigvec_23", draw23)
    C.render("s2_eigvec_235", draw235)
    common_src = ["scripts/rtp1_prime_content.py (build, min_eig)", C.rel(C.A2_OUT) + " (lambda and Schmidt defect checks)"]
    e1 = dict(id="s2_eigvec_23", step="Step 2", title="Minimal eigenvector on the {2,3} lattice vs the product state",
              caption=("The certified minimal eigenvector of G on the {2,3} lattice (grid a = exponent of 2, b = exponent of 3), "
                       "for A = 2 (delta = 0.01232) and A = 3 (delta = 0.004147), next to the eigenvector of G with the mixed "
                       "entries set to zero, which by lane A2's lemma 4.1 is exactly the Kronecker sum of the one-prime forms, "
                       "so its minimal eigenvector is the product state v_(2) x v_(3) (checked: Schmidt defect < 1e-12). Right: "
                       "the difference, on its own diverging scale. The inter-place part of the eigenvector is O(delta^2) in "
                       "the Schmidt defect (9.7e-4 and 1.0e-3 here) and the difference is O(delta). Lane A2 routines, arb "
                       "midpoints."),
              panels=["v_min(G) (certified)", "product state (certified)", "difference (derived)"],
              kind="certified (lane A2 routines, arb midpoints)", sources=common_src, script=SCRIPT)
    e2 = dict(id="s2_eigvec_235", step="Step 2", title="Minimal eigenvector on the {2,3,5} lattice (three slices)",
              caption=("As the previous figure for {2,3,5}, A = 2, delta = 0.001001 (0.9 delta_max): the 27 components shown "
                       "as three 3 x 3 slices c = 0, 1, 2 (exponent of 5); left the certified minimal eigenvector of G, middle "
                       "the product state of the Kronecker sum (mixed entries zeroed), right their difference. Schmidt defect "
                       "3.7e-4 (lane A2: 3.66e-4)."),
              panels=["v_min(G) slices (certified)", "product state slices (certified)", "difference (derived)"],
              kind="certified (lane A2 routines, arb midpoints)", sources=common_src, script=SCRIPT)
    return [e1, e2]


# ---------------------------------------------------------------------------------------------------
MARK = {1: "o", 2: "s", 3: "D", 4: "^"}


def fig_scaling():
    summ = [r for r in C.a2_summary() if len(r["S"]) >= 2]
    mv = C.a2_movement()
    rows = [(fs(r["S"]), r["A"], r["delta"], r["gap_mix"], r["schmidt"]) for r in summ]
    rows += [("%s->%s" % (fs(m["small"]), fs(m["big"])), m["A"], m["delta"], "", "", m["one_minus_ov"]) for m in mv]
    C.write_table("s2_scaling", ["S_or_step", "A", "delta", "gap_mix", "schmidt_defect", "1-overlap"], rows,
                  ["certified, parsed from outputs/rtp1_prime_content.txt (summary table 5b and section 6)"])

    def draw():
        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(1, 3, figsize=(12.5, 4.9), gridspec_kw=dict(wspace=0.3))
        a1, a2, a3 = axs
        for S_ in ((2, 3), (2, 3, 5)):
            for A in (1, 2, 3, 4):
                rr = sorted([r for r in summ if r["S"] == S_ and r["A"] == A], key=lambda r: r["delta"])
                d = np.array([r["delta"] for r in rr])
                a1.loglog(d, [-r["gap_mix"] for r in rr], "-", marker=MARK[A], color=S(SETCOL[S_]), **C.ring())
                a2.loglog(d, [r["schmidt"] for r in rr], "-", marker=MARK[A], color=S(SETCOL[S_]), **C.ring())
        for step in (((2,), (2, 3)), ((2, 3), (2, 3, 5))):
            for A in (1, 2, 3, 4):
                rr = sorted([m for m in mv if m["small"] == step[0] and m["A"] == A], key=lambda m: m["delta"])
                a3.loglog([m["delta"] for m in rr], [m["one_minus_ov"] for m in rr], "-", marker=MARK[A],
                          color=S(SETCOL[step[1]]), **C.ring())
        for ax, p, lab in ((a1, 1, "slope 1"), (a2, 2, "slope 2"), (a3, 2, "slope 2")):
            lo, hi = ax.get_xlim()
            ylo, yhi = ax.get_ylim()
            xs = np.array([1e-7, 1e-2])
            y0 = math.sqrt(ylo * yhi)
            ax.loglog(xs, y0 * (xs / 1e-4) ** p, color=T["ink2"], lw=0.8)
            ax.text(2e-7, y0 * (2e-7 / 1e-4) ** p * 3, lab, fontsize=7.5, color=T["ink2"])
            ax.set_xlabel("delta")
        a1.set_ylabel("-(lambda(G_nomix) - lambda(G))")
        a1.set_title("(a) mixed-entry gap: linear in delta")
        a2.set_ylabel("Schmidt defect  1 - sigma_1^2")
        a2.set_title("(b) Schmidt defect: quadratic in delta")
        a3.set_ylabel("1 - overlap on the old sublattice")
        a3.set_title("(c) eigenvector movement, prime added")
        h = [plt.Line2D([], [], color=S(2), lw=1.6, label="{2,3}  /  step {2} -> {2,3}"),
             plt.Line2D([], [], color=S(3), lw=1.6, label="{2,3,5}  /  step {2,3} -> {2,3,5}")]
        h += [plt.Line2D([], [], color=T["ink2"], lw=0, marker=MARK[A], label="A = %d" % A) for A in (1, 2, 3, 4)]
        fig.legend(handles=h, loc="upper center", bbox_to_anchor=(0.5, 0.905), ncol=6, fontsize=8, frameon=False)
        fig.suptitle("Inter-place effects are O(delta) in eigenvalues and O(delta^2) in eigenvectors (lane A2, certified)",
                     x=0.05, ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.06, right=0.985, top=0.76, bottom=0.12)
        return fig
    C.render("s2_scaling", draw)
    return dict(id="s2_scaling", step="Step 2", title="Scaling of the inter-place effects with delta",
                caption=("Lane A2's certified measurements at delta = 0.9, 0.3, 0.1 delta_max (panels a, b) and at a common "
                         "delta_c = 0.9 delta_max({2,3,5}, A), delta_c/10, delta_c/100 (panel c). Colour: prime set (or the step "
                         "that adds a prime); marker: A. (a) The gap lambda(G_nomix) - lambda(G) (negative: the mixed entries "
                         "raise lambda_min) is linear in delta; lane A2 plots it as gap/delta converging, here log-log with a "
                         "slope-1 guide. (b) The Schmidt defect of the minimal eigenvector across the cut {p} | rest, with a "
                         "slope-2 guide. (c) 1 - overlap between the old eigenvector and the restriction of the new one to the "
                         "old sublattice, for {2} -> {2,3} and {2,3} -> {2,3,5}: fitted slopes 2.00 to 2.06. Guides are drawn, "
                         "not fitted."),
                panels=["gap_mix (certified)", "Schmidt defect (certified)", "eigenvector movement (certified)"],
                kind="certified data", sources=[C.rel(C.A2_OUT) + " (sections 5b and 6)"], script=SCRIPT)


def fig_deltamax():
    adm = C.a2_admissible()
    C.write_table("s2_deltamax", ["S", "A", "dim", "delta_max", "binding_ratio", "foreign_prime_power"],
                  [(fs(r["S"]), r["A"], r["dim"], r["dmax"], r["r"], r["k"]) for r in adm],
                  ["certified (balls of radius < 1e-59), parsed from outputs/rtp1_prime_content.txt section 2"])

    def draw():
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(10, 5.2))
        for S_ in ((2,), (2, 3), (2, 3, 5)):
            rr = [r for r in adm if r["S"] == S_]
            A = [r["A"] for r in rr]
            d = [r["dmax"] for r in rr]
            ax.semilogy(A, d, "o-", color=S(SETCOL[S_]), label=fs(S_), ms=7, **C.ring())
            for r in rr:
                if S_ == (2,) and r["A"] == 6:
                    continue
                if S_ == (2,):
                    ax.text(r["A"] + 0.06, r["dmax"] * 1.35, "%d vs %d" % (r["r"], r["k"]), fontsize=7.5, color=T["ink2"],
                            va="center")
                else:
                    ax.text(r["A"] - 0.07, r["dmax"] * 0.55, "%d vs %d" % (r["r"], r["k"]), fontsize=7.5, color=T["ink2"],
                            va="center", ha="right")
            ax.text(A[-1] + 0.1, d[-1], "  " + fs(S_), fontsize=8, color=T["ink"], va="center", fontweight="bold")
        ax.set_xlabel("A (exponent box 0 <= a_p <= A)")
        ax.set_ylabel("delta_max")
        ax.set_xticks(range(1, 7))
        ax.set_xlim(0.2, 7.1)
        ax.legend(loc="lower right")
        ax.set_title("Admissible delta_max against A, annotated with the binding pair (lattice ratio vs foreign prime power)")
        fig.subplots_adjust(left=0.09, right=0.98, top=0.9, bottom=0.11)
        return fig
    C.render("s2_deltamax", draw)
    return dict(id="s2_deltamax", step="Step 2", title="Admissible delta_max against A",
                caption=("Lane A2's admissible delta_max(S, A) = (1/2) min |log k - log r| over lattice ratios r and prime "
                         "powers k != r (log scale), for S = {2}, {2,3}, {2,3,5}. Each point is annotated with its binding pair "
                         "r vs k: a lattice ratio next to a foreign prime power (6 vs 7, 36 vs 37, 108 vs 109, 1296 vs 1297, ..., "
                         "405000 vs 405001). delta_max falls roughly like the reciprocal of the largest lattice ratio, which is "
                         "why the inter-place effects this channel can see are small. {2}, A = 6 repeats the A = 5 value "
                         "(32 vs 31). Certified balls, radius < 1e-59."),
                panels=["delta_max (certified)"], kind="certified data", sources=[C.rel(C.A2_OUT) + " (section 2)"],
                script=SCRIPT)


# ---------------------------------------------------------------------------------------------------
def fig_explicit():
    from flint import acb, ctx
    cmp_rows = C.a2_comparison()
    pick = [c for c in cmp_rows if c["delta"] == 0.1 and c["r"] in ("2", "3/2")]
    ctx.prec = 64
    gam = np.array([float(z.imag.mid().str(20, radius=False)) for z in acb.zeta_zeros(1, 2000)])
    ctx.prec = 53
    tq, wq = np.polynomial.legendre.leggauss(1600)
    ph1 = np.exp(-1 / (1 - tq ** 2))

    def phihat(d, g):
        return d * (np.cos(np.outer(d * g, tq)) * ph1) @ wq
    curves = {}
    for c in pick:
        d = c["delta"]
        num, _, den = c["r"].partition("/")
        Dex = math.log(int(num)) - math.log(int(den or 1))       # exact D = log r (the output prints D to 6 digits)
        terms = 2 * np.cos(gam * Dex) * phihat(d, gam) ** 2
        Z = np.cumsum(terms)
        curves[c["r"]] = Z
        for M, e in zip(c["M"], c["err"]):
            fl = abs(c["psi"] - Z[M - 1])
            if e > 1e-14:
                check(abs(fl / e - 1) < 6e-3, "delta = 0.1, r = %s, M = %d: floating |Psi - Z_M| = %.4g vs certified %.3g "
                      "(agree to the 3 printed digits)"
                      % (c["r"], M, fl, e))
    rows = []
    for c in pick:
        for M in range(1, 2001):
            rows.append((c["r"], M, gam[M - 1], curves[c["r"]][M - 1], c["psi"]))
    C.write_table("s2_explicit", ["r", "M", "gamma_M", "Z_M (zero side, floating)", "Psi (prime side, certified)"], rows,
                  ["COMPARISON STEP (zeros of zeta used HERE ONLY): Z_M = sum_(k<=M) 2 cos(gamma_k D) phihat_delta(gamma_k)^2,",
                   "delta = 0.1; Psi from outputs/rtp1_prime_content.txt section 7; zeros from python-flint acb.zeta_zeros"])
    allc = [c for c in cmp_rows]

    def draw():
        import matplotlib.pyplot as plt
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.5, 4.9), gridspec_kw=dict(wspace=0.25))
        M = np.arange(1, 2001)
        for i, c in enumerate(pick):
            col = S(4 + i)
            a1.semilogx(M, curves[c["r"]] * 1e3, color=col, lw=1.4,
                        label="zero side Z_M, r = %s (%s)" % (c["r"], "2-comb entry" if c["r"] == "2" else "mixed-type ratio"))
            a1.axhline(c["psi"] * 1e3, color=col, lw=0.9, alpha=0.8)
            a1.text(2400, c["psi"] * 1e3, "prime side\nPsi = %.4g" % c["psi"], fontsize=7.5, color=T["ink2"], va="center")
        a1.set_xlim(1, 2000)
        a1.set_xlabel("M (number of zeros)")
        a1.set_ylabel("value x 1e3")
        a1.set_title("(a) partial sums converge to the prime-side value, delta = 0.1")
        a1.legend(loc="center right", bbox_to_anchor=(1.0, 0.35), fontsize=7.5)
        C.badge(a1)
        for i, c in enumerate(pick):
            err = np.abs(c["psi"] - curves[c["r"]])
            ok = err > 1e-14
            a2.loglog(M[ok], err[ok], color=S(4 + i), lw=0.9, alpha=0.8)
        for c in allc:
            col = S(4) if (c["delta"] == 0.1 and c["r"] == "2") else S(5) if (c["delta"] == 0.1 and c["r"] == "3/2") else T["muted"]
            mk = "o" if c["delta"] == 0.1 else "s"
            a2.loglog(c["M"], c["err"], mk, color=col, ms=5, **C.ring())
        a2.plot([], [], "o", color=T["muted"], label="certified |Psi - Z_M|, other entries, delta = 0.1")
        a2.plot([], [], "s", color=T["muted"], label="certified, delta = 0.05")
        a2.plot([], [], "-", color=S(4), label="r = 2 (floating curve + certified dots)")
        a2.plot([], [], "-", color=S(5), label="r = 3/2")
        a2.set_xlabel("M")
        a2.set_ylabel("|Psi - Z_M|")
        a2.set_title("(b) truncation error ~ exp(-2.2 sqrt(delta gamma_M))")
        a2.legend(loc="lower left", fontsize=7.5)
        C.badge(a2)
        fig.suptitle("Explicit-formula check of the lattice-bump normalisation (implementation check, not an input)",
                     x=0.05, ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.07, right=0.93, top=0.85, bottom=0.12)
        return fig
    C.render("s2_explicit", draw)
    return dict(id="s2_explicit", step="Step 2", title="Explicit-formula comparison (zeros used)",
                caption=("Comparison (zeros used), lane A2.4: an implementation check of the explicit formula in this "
                         "normalisation, never an input to a form. (a) The zero-side partial sums "
                         "Z_M = sum_(k<=M) 2 cos(gamma_k D) phihat_delta(gamma_k)^2 for two Gram entries at delta = 0.1 (the ratio "
                         "r = 2, which carries the 2-comb, and r = 3/2, pole plus archimedean only), against the certified "
                         "prime-side values Psi from lane A2's output (horizontal lines). The curves are recomputed in floating "
                         "point (certified zeros from python-flint, Gauss-Legendre transform of the bump) and reproduce the "
                         "certified errors to their 3 printed digits wherever those exceed 1e-14. (b) |Psi - Z_M|: dots are lane A2's certified values for all ten "
                         "entries (delta = 0.1 circles, 0.05 squares), lines the floating curves (drawn down to 1e-14, the floating-point floor). The "
                         "error decays like exp(-2.2 sqrt(delta gamma_M)) (lane A2's fit)."),
                panels=["comparison (zeros used): partial sums (floating) vs certified Psi",
                        "comparison (zeros used): certified truncation errors + floating curves"],
                kind="comparison (zeros used)", sources=[C.rel(C.A2_OUT) + " (section 7)", "python-flint acb.zeta_zeros"],
                script=SCRIPT)


def run():
    entries = [fig_gram()]
    entries += fig_eigvec()
    entries += [fig_scaling(), fig_deltamax(), fig_explicit()]
    C.register(STEP, entries)
    return entries


if __name__ == "__main__":
    run()
