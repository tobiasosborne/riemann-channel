"""Step 4 of viz-brief.md: the kinematic commutant (lane B2.1) (lane V, second pass; claude:opus).

Certified data (parsed from lane B2's output `outputs/rtp1_commutant.txt`, never recomputed): the exact dimension
counts (Section 2), the prediction table and its coefficient table at x = 13, N = 20 (Sections 3, 4), the N table
(Section 5), the PNT table against x (Section 5b), and the lattice box with its N table (Section 6).

Recomputed for display (the output does not contain it): the geometry of the positive set of prime data
P_N = {z : H0 + T(z) >= 0} in three 2-D sections at x = 13, N = 20.  H0 (pole + archimedean) and the true form come
from zst (`zst_riemann_ab` at window x = 13 with prime cutoff X = 1 and X = 13, through bridges.zst_ab, 300 bits,
then double); the minimal-norm, PNT and maximum-determinant points are B2's printed coefficient vectors (4 decimals).
Loewner forms are assembled in double as in step1_dilation.tau_full; the sections are evaluated on a grid from the
even and odd blocks.  Checks against B2's printed numbers stop the build if they fail.
"""
import math
import os
import re

import numpy as np

import bridges
import common as C
from common import T, S

STEP = "step4"
SCRIPT = "viz/rtp1/step4_commutant.py"
B2_NOTE = os.path.join(C.REPO, "notes", "rtp-round-1", "lane-B2.md")
B2_OUT = os.path.join(C.OUT, "rtp1_commutant.txt")
X, N = 13, 20
LOG = []


def check(cond, msg):
    LOG.append(("ok  " if cond else "FAIL") + "  " + msg)
    print(("  ok    " if cond else "  FAIL  ") + msg)
    if not cond:
        raise SystemExit("check failed: " + msg)


# ---------------------------------------------------------------------------------------------------
# parsers for outputs/rtp1_commutant.txt (lane B2.1)
# ---------------------------------------------------------------------------------------------------
def _text():
    if not (os.path.exists(B2_NOTE) and os.path.exists(B2_OUT)):
        raise SystemExit("lane B2 has not reported (notes/rtp-round-1/lane-B2.md or outputs/rtp1_commutant.txt missing)")
    txt = open(B2_OUT).read()
    check(re.search(r"CHECKS: (\d+) passed, 0 failed", txt) is not None, "lane B2 commutant output: 0 failed checks")
    return txt


def _section(txt, start, stop):
    return txt.split(start, 1)[1].split(stop, 1)[0]


def b2_dims(txt):
    """Section 2 table: name -> (formula, [dim at N = 1..6])"""
    out = {}
    sec = _section(txt, "2. B2.1(a)", "ok   [L 367]")
    for line in sec.splitlines():
        m = re.match(r"\s+((?:Herm|Loewner)\S*)\s+(.+?)\s{2,}((?:\d+\s+){5}\d+)\s*$", line)
        if m:
            out[m.group(1)] = (m.group(2), [int(t) for t in m.group(3).split()])
    return out


def b2_sec3(txt):
    sec = _section(txt, "3. B2.1(b)", "4. B2.1(c)")
    g = lambda pat: float(re.search(pat, sec).group(1))                           # noqa: E731
    lds = re.search(r"log det\(H0 \+ cI\) = ([0-9.]+), ([0-9.]+), ([0-9.]+) at c = 10, 100, 1000", sec)
    return dict(lmin_true=g(r"lambda_min\(H_true\) = ([0-9.e+-]+) > 0"), c_iso=g(r"is in P_N for c >= ([0-9.]+)"),
                logdet_c=[float(lds.group(i)) for i in (1, 2, 3)], min_hs=g(r"min \|\|z\|\|_HS = ([0-9.]+)"),
                true_hs=g(r"true \|\|z\|\|_HS = ([0-9.]+)"), one_minus_slo=g(r"1 - s_lo = ([0-9.e+-]+)"),
                shi_minus_one=g(r"s_hi - 1 = ([0-9.e+-]+)"), logdet_true=g(r"\(truth: log det = ([-0-9.]+)\)"),
                lmin_zmin=g(r"lambda_min\(H0 \+ T\(z_min\)\) = ([0-9.e+-]+),"))


def b2_predictions(txt):
    """Section 4 prediction table: name -> (norm, rel. dist, captured, cos, on neg(H0))"""
    sec = _section(txt, "4. B2.1(c)", "compression to neg(H0)")
    out = {}
    for line in sec.splitlines():
        m = re.match(r"\s{2}(\S.*?)\s{2,}([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)\s*$", line)
        if m:
            out[m.group(1)] = tuple(float(m.group(i)) for i in range(2, 7))
    return out


def b2_coefficients(txt):
    """Section 4 coefficient table, N = 20: n -> (u_true, u_minHS, u_maxdet, u_PNT, v_true, v_minHS, v_maxdet, v_PNT)"""
    sec = txt.split("coefficient table, N = 20", 1)[1]
    out = {}
    for line in sec.splitlines()[2:]:
        f = line.replace("|", " ").split()
        if not f or not f[0].isdigit():
            break
        vals = [float(t) for t in f[1:]]
        if len(vals) == 4:
            vals += [0.0] * 4                    # v_0 = 0 (b is odd)
        out[int(f[0])] = vals
    return out


def b2_Ntable(txt):
    sec = _section(txt, "5. DEPENDENCE ON N", "ok   [L 826]")
    rows = []
    for line in sec.splitlines():
        f = line.split()
        if len(f) == 15 and f[0].isdigit():
            rows.append(dict(N=int(f[0]), neg=f[1], lminH0=float(f[2]), lmin_true=float(f[3]), slo=float(f[4]),
                             shi=float(f[5]), true_hs=float(f[6]), min_hs=float(f[7]), min_dist=float(f[8]),
                             min_capt=float(f[9]), md_dist=float(f[10]), md_capt=float(f[11]), gap=float(f[12]),
                             pnt_dist=float(f[13]), pnt_capt=float(f[14])))
    return rows


def b2_pnt_x(txt):
    """Section 5b: rows (x, N, rho, captured)"""
    sec = _section(txt, "5b. THE PNT PREDICTOR", "ok   [L 878]")
    rows = []
    for line in sec.splitlines():
        f = line.split()
        if len(f) == 4 and f[0].isdigit():
            rows.append(dict(x=int(f[0]), N=int(f[1]), rho=float(f[2]), capt=float(f[3])))
    return rows


def b2_box(txt):
    sec = _section(txt, "6. B2.1(d)", "TALLY")
    rows, widths = [], []
    part = sec.split("Box of Pi around the truth", 1)[1].split("ok   [L1009]", 1)[0]
    for line in part.splitlines():
        f = line.split()
        if len(f) == 5 and f[0].isdigit():
            rows.append(dict(n=int(f[0]), w=float(f[1]), lo=float(f[2]), hi=float(f[3]), width=float(f[4])))
    for line in sec.splitlines():
        m = re.match(r"\s+N =\s+(\d+): ([0-9.e+-]+) / ([0-9.e+-]+) / ([0-9.e+-]+)\s+\((\d+) eigenvalues", line)
        if m:
            widths.append(dict(N=int(m.group(1)), w7=float(m.group(2)), w10=float(m.group(3)), w12=float(m.group(4)),
                               nsmall=int(m.group(5))))
    return rows, widths


# ---------------------------------------------------------------------------------------------------
# Loewner forms (display geometry)
# ---------------------------------------------------------------------------------------------------
def loewner(af, bf, n_=N):
    """full (2N+1) x (2N+1) Loewner form: diagonal a_|n|, off-diagonal (b_n - b_m)/(n - m), b odd"""
    n = np.arange(-n_, n_ + 1)
    bb = np.sign(n) * np.asarray(bf)[np.abs(n)]
    D = n[:, None] - n[None, :]
    M = np.where(D == 0, 0.0, (bb[:, None] - bb[None, :]) / np.where(D == 0, 1, D))
    M[np.arange(2 * n_ + 1), np.arange(2 * n_ + 1)] = np.asarray(af)[np.abs(n)]
    return M


def eo_basis(n_=N):
    """orthogonal U with columns V_0, (V_j + V_-j)/sqrt2 (even), then (V_j - V_-j)/sqrt2 (odd)"""
    U = np.zeros((2 * n_ + 1, 2 * n_ + 1))
    U[n_, 0] = 1.0
    for j in range(1, n_ + 1):
        U[n_ + j, j] = U[n_ - j, j] = 1 / math.sqrt(2)
        U[n_ + j, n_ + j] = 1 / math.sqrt(2)
        U[n_ - j, n_ + j] = -1 / math.sqrt(2)
    return U


def ip(A, B):
    return float(np.sum(A * B))


def section(origin, E1, E2, P, Q):
    """eigenvalues of origin + p E1 + q E2 on the grid, from the even and odd blocks (all gamma-symmetric)"""
    U = eo_basis()
    ne = N + 1
    out = []
    for sl in (slice(0, ne), slice(ne, 2 * N + 1)):
        Us = U[:, sl]
        o, e1, e2 = (Us.T @ M @ Us for M in (origin, E1, E2))
        Mg = o[None, None] + P[..., None, None] * e1[None, None] + Q[..., None, None] * e2[None, None]
        out.append(np.linalg.eigvalsh(Mg))
    w = np.concatenate(out, axis=-1)
    return w.min(axis=-1), np.sum(np.log(np.abs(w)), axis=-1)


def geometry(txt):
    a, b, ra, rb = bridges.zst_ab(X, N, 300)
    a0, b0, ra0, rb0 = bridges.zst_ab(1, N, 300, window=X)
    check(max(ra + rb + ra0 + rb0) < 1e-60, "zst balls at x = 13, N = 20 (X = 13 and X = 1): radii < 1e-60")
    at, bt = np.array([float(s) for s in a]), np.array([float(s) for s in b])
    a0, b0 = np.array([float(s) for s in a0]), np.array([float(s) for s in b0])
    H0, Ht = loewner(a0, b0), loewner(at, bt)
    Tt = Ht - H0
    s3 = b2_sec3(txt)
    lH0 = np.linalg.eigvalsh(H0)
    check(abs(lH0[0] + 1.9613) < 5e-4 and int(np.sum(lH0 < 0)) == 4,
          "H0 (pole + archimedean, zst X = 1 at window 13): lambda_min = %.4f, 4 negative eigenvalues (B2: -1.9613, 2+2)"
          % lH0[0])
    check(abs(math.sqrt(ip(Tt, Tt)) / s3["true_hs"] - 1) < 1e-6,
          "||z_true||_HS = %.6f (B2: %.6f)" % (math.sqrt(ip(Tt, Tt)), s3["true_hs"]))
    co = b2_coefficients(txt)
    col = lambda j: (np.array([co[n][j] for n in range(N + 1)]), np.array([co[n][4 + j] for n in range(N + 1)]))  # noqa: E731
    Ttab = loewner(*col(0))
    check(np.abs(Ttab - Tt).max() < 2e-4, "B2's printed true prime data (4 decimals) = zst's: max entry diff %.1e"
          % np.abs(Ttab - Tt).max())
    pts = dict(minHS=loewner(*col(1)), maxdet=loewner(*col(2)), PNT=loewner(*col(3)))
    pred = b2_predictions(txt)
    names = dict(minHS="min ||.||_HS", maxdet="max det on ||.||_HS <= ||T_true||_HS", PNT="PNT mean (pole density), no positivity")
    for k, M in pts.items():
        nrm, dist, capt = math.sqrt(ip(M, M)), math.sqrt(ip(M - Tt, M - Tt) / ip(Tt, Tt)), ip(M, Tt) / ip(Tt, Tt)
        p = pred[names[k]]
        check(abs(nrm - p[0]) < 3e-3 and abs(dist - p[1]) < 1e-3 and abs(capt - p[2]) < 1e-3,
              "%s from B2's coefficient table: norm %.4f, rel. dist %.4f, captured %.4f (B2: %.4f, %.4f, %.4f)"
              % (k, nrm, dist, capt, p[0], p[1], p[2]))
    lmin = {k: float(np.linalg.eigvalsh(H0 + M)[0]) for k, M in pts.items()}
    check(abs(lmin["PNT"] + 1.226) < 2e-3, "PNT point inadmissible: lambda_min(H0 + T_PNT) = %.4f (B2: -1.226)" % lmin["PNT"])
    check(abs(lmin["minHS"]) < 1e-3, "min-norm point (4-decimal coefficients) within 1e-3 of the boundary: lambda_min = %.1e"
          % lmin["minHS"])
    check(abs(lmin["maxdet"] - 0.891) < 2e-3, "ball max-det point: lambda_min = %.4f (B2: 0.8909)" % lmin["maxdet"])
    I = np.eye(2 * N + 1)
    for c, ld in zip((10, 100, 1000), s3["logdet_c"]):
        mine = float(np.sum(np.log(np.linalg.eigvalsh(H0 + c * I))))
        check(abs(mine - ld) < 0.01, "log det(H0 + %d I) = %.2f (B2: %.2f)" % (c, mine, ld))
    return dict(H0=H0, Ht=Ht, Tt=Tt, I=I, s3=s3, lmin=lmin, **pts)


def orthobasis(A, B):
    e1 = A / math.sqrt(ip(A, A))
    B2 = B - ip(B, e1) * e1
    return e1, B2 / math.sqrt(ip(B2, B2))


def cone_arc(E1, E2, n=7200):
    """angles theta with cos(theta) E1 + sin(theta) E2 >= 0 (the recession cone C_N cut by the plane)"""
    th = np.linspace(-math.pi, math.pi, n, endpoint=False)
    ok = np.array([np.linalg.eigvalsh(math.cos(t) * E1 + math.sin(t) * E2)[0] >= 0 for t in th])
    check(ok.any() and not ok.all(), "the recession cone meets the plane in a proper arc")
    # the arc is contiguous modulo 2 pi; rotate so that it does not wrap
    k = int(np.argmin(ok))
    th, ok = np.roll(th, -k), np.roll(ok, -k)
    idx = np.where(ok)[0]
    th = np.unwrap(th)
    return float(th[idx[0]]), float(th[idx[-1]])


# ---------------------------------------------------------------------------------------------------
def fig_dimensions(txt):
    dims = b2_dims(txt)
    Ns = list(range(1, 7))
    closed = {"Herm": lambda n: (2 * n + 1) ** 2, "Herm+gamma": lambda n: (n + 1) ** 2 + n ** 2,
              "Herm+real": lambda n: (n + 1) * (2 * n + 1), "Herm+gamma+real": lambda n: (n + 1) ** 2,
              "Loewner": lambda n: 4 * n + 1, "Loewner+real": lambda n: 4 * n + 1, "Loewner+gamma": lambda n: 2 * n + 1,
              "Loewner+gamma+real": lambda n: 2 * n + 1}
    check(set(dims) == set(closed) and all(dims[k][1] == [closed[k](n) for n in Ns] for k in closed),
          "B2 dimension table (exact ranks over Q, N = 1..6): all eight spaces equal their closed forms")
    rows = [(k, dims[k][0]) + tuple(dims[k][1]) for k in closed]
    C.write_table("s4_dimensions", ["space", "formula"] + ["N=%d" % n for n in Ns], rows,
                  ["certified (exact ranks over Q), outputs/rtp1_commutant.txt section 2"])
    shown = [("Herm", "Hermitian", "(2N+1)^2"), ("Herm+real", "real", "(N+1)(2N+1)"),
             ("Herm+gamma", "commuting with gamma", "(N+1)^2 + N^2"), ("Loewner", "Loewner (automatically real)", "4N+1"),
             ("Loewner+gamma", "Loewner and gamma = zst's data (a_0..a_N, b_1..b_N)", "2N+1")]

    def draw():
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(10, 4.9))
        for i, (k, lab, form) in enumerate(shown):
            y = dims[k][1]
            ax.plot(Ns, y, "o-", color=S(i + 1), label="%s: %s" % (lab, form), **C.ring())
            nud = {"Herm+real": 1.06, "Herm+gamma": 0.94}.get(k, 1.0)
            ax.text(6.12, y[-1] * nud, "%d  %s" % (y[-1], form), va="center", fontsize=8, color=T["ink2"])
        ax.set_yscale("log")
        ax.set_yticks([3, 5, 10, 20, 50, 100, 169])
        ax.set_yticklabels(["3", "5", "10", "20", "50", "100", "169"])
        ax.set_xticks(Ns)
        ax.set_xlim(0.8, 7.0)
        ax.set_xlabel("N  (forms on span{V_n : |n| <= N}, size 2N+1)")
        ax.set_ylabel("real dimension (exact rank over Q)")
        ax.legend(loc="upper left", fontsize=8)
        ax.set_title("(a) linear kinematic conditions: the commutant has dimension 2N+1, and positivity removes none")
        fig.suptitle("Step 4: the kinematic space K_N is exactly zst's data format", x=0.06, ha="left", fontsize=12,
                     fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.08, right=0.9, top=0.85, bottom=0.12)
        return fig
    C.render("s4_dimensions", draw)
    return dict(id="s4_dimensions", step="Step 4", title="Dimension counts of the kinematic conditions",
                caption=("Lane B2.1(a), certified (exact ranks over Q for N = 1..6, each equal to its closed form). Real "
                         "dimension of the Hermitian forms on the span of V_n, |n| <= N, under the linear kinematic "
                         "conditions: reality, commuting with the Weyl element gamma, and the Loewner condition [D, H] = "
                         "|beta><eta| - |eta><beta| (eta = sum V_n fixed). A Loewner form is automatically real (Loewner + "
                         "real = Loewner, 4N+1; also Hermitian + gamma + real = (N+1)^2, in the table), and Loewner + gamma has "
                         "dimension 2N+1: exactly the data (a_0..a_N, b_1..b_N). The identity is an interior point of the "
                         "positive cone, so positivity removes no dimension."),
                panels=["dimension against N, five spaces (certified)"],
                kind="certified data", sources=[C.rel(B2_OUT)], script=SCRIPT)


def fig_positive_set(txt, G):
    Tt, Tmin, Tp, I, H0 = G["Tt"], G["minHS"], G["PNT"], G["I"], G["H0"]
    Z = 0 * Tt
    s3 = G["s3"]
    # (b1) plane through the pole+arch point 0 containing z_true and z_min
    e1, e2 = orthobasis(Tt, Tmin)
    p1, q1 = np.linspace(-3.5, 11.5, 301), np.linspace(-4.6, 10.0, 293)
    P1, Q1 = np.meshgrid(p1, q1, indexing="ij")
    L1, _ = section(H0, e1, e2, P1, Q1)
    xy1 = {k: (ip(M, e1), ip(M, e2)) for k, M in (("zero", Z), ("true", Tt), ("min", Tmin))}
    # (b2) plane through 0 containing z_true and the identity direction
    f1, f2 = orthobasis(Tt, I)
    p2, q2 = np.linspace(-4.0, 16.0, 321), np.linspace(-3.0, 19.0, 353)
    P2, Q2 = np.meshgrid(p2, q2, indexing="ij")
    L2, LD2 = section(H0, f1, f2, P2, Q2)
    xy2 = {k: (ip(M, f1), ip(M, f2)) for k, M in (("zero", Z), ("true", Tt), ("iso", s3["c_iso"] * I))}
    th = cone_arc(f1, f2)
    # (b3) affine plane through z_true, z_min, z_PNT (origin at z_true)
    g1, g2 = orthobasis(Tmin - Tt, Tp - Tt)
    p3, q3 = np.linspace(-3.0, 11.0, 281), np.linspace(-5.0, 6.5, 231)
    P3, Q3 = np.meshgrid(p3, q3, indexing="ij")
    L3, _ = section(G["Ht"], g1, g2, P3, Q3)
    xy3 = {k: (ip(M - Tt, g1), ip(M - Tt, g2)) for k, M in (("true", Tt), ("min", Tmin), ("PNT", Tp))}
    iso_l = float(np.linalg.eigvalsh(H0 + s3["c_iso"] * I)[0])
    check(abs(iso_l) < 1e-3, "c I with c = %.4f (B2) is on the boundary: lambda_min = %.1e" % (s3["c_iso"], iso_l))
    rmin = math.hypot(*xy1["min"])
    check(abs(rmin - s3["min_hs"]) < 3e-3, "(b1) the min-norm point is at HS distance %.4f from 0 (B2: %.4f)"
          % (rmin, s3["min_hs"]))
    check(float(L1.max()) > 0 and float(L2.max()) > 0 and float(L3.max()) > 0, "each section meets the interior of P_N")
    rows = []
    for pan, xy in (("b1", xy1), ("b2", xy2), ("b3", xy3)):
        for k, (u, v) in xy.items():
            rows.append((pan, k, u, v))
    rows.append(("b2", "recession cone angles (rad)", th[0], th[1]))
    C.write_table("s4_positive_set", ["panel", "point", "coord_1", "coord_2"], rows,
                  ["RECOMPUTED for display: in-plane HS coordinates of the marked points (x = 13, N = 20).",
                   "b1: plane through 0 spanned by z_true, z_min;  b2: through 0 spanned by z_true, I;  b3: affine plane "
                   "through z_true, z_min, z_PNT (origin z_true).",
                   "H0 and z_true from zst (300 bits, then double); z_min, z_PNT from B2's printed coefficient table.",
                   "certified numbers used in annotations: outputs/rtp1_commutant.txt sections 3, 4"])

    def region(ax, P, Q, L):
        ax.contourf(P, Q, L, levels=[0, float(L.max()) + 1], colors=[S(3)], alpha=T["wash"] * 2.2).set_rasterized(True)
        ax.contour(P, Q, L, levels=[0], colors=[S(3)], linewidths=1.6)

    def pt(ax, xy, kind, **kw):
        style = dict(zero=("s", T["ink2"]), true=("D", S(2)), min=("o", S(1)), PNT=("^", S(4)), iso=("o", T["ink2"]))
        m, c = style[kind]
        ax.plot([xy[0]], [xy[1]], m, color=c, ms=kw.pop("ms", 8), zorder=6, **C.ring())

    def draw():
        import matplotlib.pyplot as plt
        from matplotlib.patches import Circle
        fig, axs = plt.subplots(1, 3, figsize=(15, 6.0), gridspec_kw=dict(wspace=0.22))
        a1, a2, a3 = axs
        # (b1)
        region(a1, P1, Q1, L1)
        a1.add_patch(Circle((0, 0), s3["min_hs"], fill=False, ec=T["ink2"], lw=0.9))
        a1.plot([0, xy1["true"][0]], [0, 0], color=T["ink2"], lw=0.8)
        for k in ("zero", "true", "min"):
            pt(a1, xy1[k], k)
        a1.annotate("pole + archimedean alone\n(prime data 0): inadmissible,\nlambda_min(H0) = -1.96", xy=xy1["zero"],
                    xytext=(-3.2, -4.3), fontsize=7.5, color=T["ink"], va="bottom",
                    arrowprops=dict(arrowstyle="-", color=T["ink2"], lw=0.6))
        a1.annotate("minimal-norm element\n||z||_HS = %.2f, on the boundary" % s3["min_hs"], xy=xy1["min"],
                    xytext=(-3.2, 4.3), fontsize=7.5, color=T["ink"],
                    arrowprops=dict(arrowstyle="-", color=T["ink2"], lw=0.6))
        a1.annotate("true prime data, ||z||_HS = %.2f:\non the boundary, and the only\nadmissible point of its ray"
                    % s3["true_hs"], xy=xy1["true"], xytext=(3.6, -4.3), fontsize=7.5, color=T["ink"], va="bottom",
                    arrowprops=dict(arrowstyle="-", color=T["ink2"], lw=0.6))
        a1.text(3.2, 7.2, "P_N (admissible)", fontsize=8.5, color=T["ink"], fontweight="bold")
        a1.set_title("(b1) nearest admissible point to 'no primes'")
        # (b2)
        region(a2, P2, Q2, L2)
        LDm = np.where(L2 > 0, LD2, np.nan)
        cs = a2.contour(P2, Q2, LDm, levels=[0, 20, 40, 60, 80], colors=[T["ink2"]], linewidths=0.7)
        a2.clabel(cs, fmt="log det %d", fontsize=6.5, colors=[T["ink2"]], inline_spacing=2)
        for t in th:
            r = 16.0
            a2.plot([xy2["true"][0], xy2["true"][0] + r * math.cos(t)], [xy2["true"][1], xy2["true"][1] + r * math.sin(t)],
                    color=T["ink"], lw=0.9)
        a2.plot([0, xy2["true"][0]], [0, 0], color=T["ink2"], lw=0.8)
        for k in ("zero", "true", "iso"):
            pt(a2, xy2[k], k, ms=(6 if k == "iso" else 8))
        a2.annotate("T = cI admissible\nfor c >= %.2f" % s3["c_iso"], xy=xy2["iso"], xytext=(-3.7, 8.0), fontsize=7.5,
                    color=T["ink"], arrowprops=dict(arrowstyle="-", color=T["ink2"], lw=0.6))
        a2.text(11.3, 6.4, "z_true + recession\ncone C_N (any positive\nLoewner form can\nbe added)", fontsize=7.5,
                color=T["ink"], ha="left", va="top")
        a2.annotate("", xy=(10.6, 18.6), xytext=(10.6, 14.4),
                    arrowprops=dict(arrowstyle="->", color=T["ink"], lw=1.0))
        a2.text(10.2, 18.6, "log det -> +infinity:\nno maximum-determinant\nelement", fontsize=7.5, color=T["ink"],
                ha="right", va="top", fontweight="bold")
        a2.text(10.2, 16.3, "log det(H0 + cI) = %.0f, %.0f, %.0f\nat c = 10, 100, 1000" % tuple(s3["logdet_c"]),
                fontsize=7.5, color=T["ink2"], ha="right", va="top")
        a2.text(xy2["true"][0] + 0.3, -1.6, "truth: log det = %.0f" % s3["logdet_true"], fontsize=7.5, color=T["ink2"])
        a2.set_title("(b2) unbounded: the identity direction")
        # (b3)
        region(a3, P3, Q3, L3)
        a3.plot([xy3["true"][0], xy3["min"][0]], [xy3["true"][1], xy3["min"][1]], color=S(3), lw=2.6)
        for k in ("true", "min", "PNT"):
            pt(a3, xy3[k], k)
        a3.annotate("PNT mean (pole density, no prime used):\ninadmissible, lambda_min = %.2f" % G["lmin"]["PNT"],
                    xy=xy3["PNT"], xytext=(-2.6, 5.4), fontsize=7.5, color=T["ink"], va="top",
                    arrowprops=dict(arrowstyle="-", color=T["ink2"], lw=0.6))
        a3.text(xy3["min"][0] - 0.2, xy3["min"][1] + 0.45, "minimal-norm", fontsize=7.5, color=T["ink2"], ha="right")
        a3.text(xy3["true"][0] + 0.2, xy3["true"][1] + 0.45, "truth", fontsize=7.5, color=T["ink2"])
        a3.text(1.0, -1.2, "the segment truth - minimal-norm\nlies in the boundary", fontsize=7.5, color=T["ink"], va="top")
        a3.set_title("(b3) the plane through truth, minimal-norm and PNT")
        for ax, lab in ((a1, ("HS coordinate along z_true", "HS coordinate towards z_min")),
                        (a2, ("HS coordinate along z_true", "HS coordinate towards the identity")),
                        (a3, ("HS coordinate, z_true -> z_min", "HS coordinate towards z_PNT"))):
            ax.set_aspect("equal")
            ax.set_xlabel(lab[0])
            ax.set_ylabel(lab[1])
        a1.set_xlim(p1[0], p1[-1]); a1.set_ylim(q1[0], q1[-1])
        a2.set_xlim(p2[0], p2[-1]); a2.set_ylim(q2[0], q2[-1])
        a3.set_xlim(p3[0], p3[-1]); a3.set_ylim(q3[0], q3[-1])
        a1.plot([], [], "s", color=T["ink2"], label="pole + archimedean only (0)")
        a1.plot([], [], "o", color=S(1), label="minimal-norm element")
        a1.plot([], [], "D", color=S(2), label="true prime data")
        a1.plot([], [], "^", color=S(4), label="PNT mean")
        a1.plot([], [], "s", color=S(3), alpha=0.5, ms=9, label="admissible set P_N (section)")
        a1.legend(loc="upper left", bbox_to_anchor=(0.05, 0.925), bbox_transform=fig.transFigure, ncol=5, fontsize=8)
        fig.suptitle("Step 4: the positive set of prime data at x = 13, N = 20 (three exact 2-D sections of R^41)",
                     x=0.05, ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.05, right=0.99, top=0.84, bottom=0.09)
        return fig
    C.render("s4_positive_set", draw)
    return dict(id="s4_positive_set", step="Step 4", title="The positive set of prime data, x = 13, N = 20",
                caption=("Lane B2.1(b). P_N = {z : H0 + T(z) >= 0}: z = (u_0..u_20, v_1..v_20) the prime part of the "
                         "Loewner data, H0 the pole + archimedean form (fixed). Recomputed for display: three exact planar "
                         "sections of this 41-dimensional set, in Hilbert-Schmidt coordinates (so distances are true), "
                         "evaluated on a grid in double from zst's data (x = 13, cutoff X = 1 and 13); the minimal-norm and "
                         "PNT points are lane B2's printed coefficient vectors (4 decimals, so the minimal-norm point sits "
                         "within 1e-4 of the boundary). (b1) The plane through 0 (no prime data: inadmissible), the truth "
                         "and the minimal-norm element: the circle of radius %.2f about 0 touches P_N at the minimal-norm "
                         "element; the truth is a corner, the only admissible point on its own ray (B2: admissible multiples "
                         "within 1 - %.1e .. 1 + %.1e). (b2) The plane through 0, the truth and the identity: P_N contains "
                         "z_true + C_N (the recession cone, drawn from the truth) and log det grows without bound along it, so "
                         "no maximum-determinant element exists. (b3) The plane through the truth, the minimal-norm element "
                         "and the PNT mean (the pole's density, inadmissible). Annotated numbers are lane B2's certified "
                         "values." % (s3["min_hs"], s3["one_minus_slo"], s3["shi_minus_one"])),
                panels=["(b1) section through 0, truth, minimal-norm (recomputed geometry)",
                        "(b2) section through 0, truth, identity; log-det contours (recomputed geometry)",
                        "(b3) section through truth, minimal-norm, PNT (recomputed geometry)"],
                kind="recomputed for display (geometry); marked points and annotations from lane B2's output",
                sources=[C.rel(B2_OUT), "zst (zst_riemann_ab via viz/rtp1/bridges.py)"], script=SCRIPT)


def fig_lattice_box(txt):
    rows, widths = b2_box(txt)
    pp = C.prime_powers(12)
    for r in rows:
        exact = (math.log(pp[r["n"]]) / math.sqrt(r["n"])) if r["n"] in pp else 0.0
        r["exact"] = exact
    check([r["n"] for r in rows] == list(range(2, 13)) and all(abs(r["w"] - r["exact"]) < 1e-6 for r in rows),
          "B2 lattice box: rows n = 2..12, printed truth = Lambda(n)/sqrt(n) (zero at 6, 10, 12)")
    check(all(r["lo"] <= 0 <= r["hi"] for r in rows), "every certified interval contains the truth")
    check(max(r["width"] for r in rows) < 1.3e-3 and len(widths) == 5, "N = 20 widths <= 1.3e-3; N table has 5 rows")
    C.write_table("s4_lattice_box", ["n", "Lambda(n)/sqrt(n)", "w_minus_wtrue_lower", "w_minus_wtrue_upper", "width"],
                  [(r["n"], r["w"], r["lo"], r["hi"], r["width"]) for r in rows]
                  + [("N=%d max width n<=7 / n<=10 / n<=12" % w["N"], w["w7"], w["w10"], w["w12"], w["nsmall"]) for w in widths],
                  ["certified outer bounds (100-digit dual certificates), outputs/rtp1_commutant.txt section 6, x = 13, N = 20;",
                   "the last rows: max widths against N (last column: eigenvalues of H_true below 1e-6)"])
    zero = [6, 10, 12]

    def draw():
        import matplotlib.pyplot as plt
        fig = plt.figure(figsize=(14, 5.4))
        gs = fig.add_gridspec(1, 3, width_ratios=[1.0, 1.25, 0.9], wspace=0.3)
        a1, a2, a3 = (fig.add_subplot(gs[0, i]) for i in range(3))
        ns = [r["n"] for r in rows]
        for r in rows:
            c = S(4) if r["n"] in zero else S(2)
            a1.plot([r["n"], r["n"]], [0, r["w"]], color=T["axis"], lw=1.0, zorder=1)
            a1.plot([r["n"], r["n"]], [r["w"] + r["lo"], r["w"] + r["hi"]], color=S(1), lw=6, solid_capstyle="butt", zorder=2)
            a1.plot([r["n"]], [r["w"]], "D" if r["n"] not in zero else "o", color=c, ms=7.5, zorder=3, **C.ring())
        for n in zero:
            a1.text(n, 0.035, "0", ha="center", fontsize=7.5, color=T["ink2"])
        a1.set_xticks(ns)
        a1.set_ylim(-0.03, 0.85)
        a1.set_xlabel("n  (position log n fixed)")
        a1.set_ylabel("weight w_n")
        a1.set_title("(c1) admissible weights w_n")
        a1.plot([], [], "D", color=S(2), label="Lambda(n)/sqrt(n), prime power")
        a1.plot([], [], "o", color=S(4), label="0: not a prime power (6, 10, 12)")
        a1.plot([], [], "-", color=S(1), lw=6, label="certified interval (thinner than the markers)")
        a1.legend(loc="upper left", fontsize=7.5)
        # (c2) deviation from the truth, symlog
        for r in rows:
            c = S(4) if r["n"] in zero else S(2)
            a2.plot([r["n"], r["n"]], [r["lo"], r["hi"]], color=S(1), lw=5, solid_capstyle="butt", alpha=0.85)
            a2.plot([r["n"]], [0], "D" if r["n"] not in zero else "o", color=c, ms=6.5, zorder=4, **C.ring())
            a2.text(r["n"] + 0.18, r["hi"] if r["hi"] > 1e-13 else 3e-15, "%.0e" % r["width"], fontsize=6.5,
                    color=T["ink2"], va="bottom", rotation=90)
        a2.set_yscale("symlog", linthresh=1e-15)
        a2.set_ylim(-3e-3, 5e-2)
        a2.set_yticks([-1e-3, -1e-6, -1e-9, -1e-12, 0, 1e-12, 1e-9, 1e-6, 1e-3])
        a2.axhline(0, color=T["axis"], lw=0.8)
        a2.set_xticks(ns)
        a2.set_xlabel("n")
        a2.set_ylabel("w_n - true w_n  (symlog, linear below 1e-15)")
        a2.set_title("(c2) the intervals around the truth (labels: width)")
        # (c3) widths against N
        Nw = [w["N"] for w in widths]
        for i, (key, lab) in enumerate((("w7", "n <= 7"), ("w10", "n <= 10"), ("w12", "n <= 12"))):
            a3.semilogy(Nw, [w[key] for w in widths], "o-", color=S(i + 1), label="max width, " + lab, **C.ring())
        a3.set_xlabel("N (x = 13)")
        a3.set_ylabel("largest certified interval width")
        a3.set_xticks(Nw)
        a3.legend(loc="upper right", fontsize=7.5)
        a3.set_title("(c3) against N")
        C.note(a3, "N >= 30: limited by the certificate\nconstruction, not by the set (B2)", x=0.98, y=0.66, ha="right")
        fig.suptitle("Step 4: with the positions log n known, positivity pins the von Mangoldt weights (x = 13, N = 20)",
                     x=0.05, ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.text(0.05, 0.895, "Pole, archimedean place and the lattice {log n, n = 2..12} fixed; 11 weights free. In the free "
                 "Loewner coordinates the same positivity leaves an unbounded set.", fontsize=8.5, color=T["ink2"])
        fig.subplots_adjust(left=0.05, right=0.99, top=0.8, bottom=0.1)
        return fig
    C.render("s4_lattice_box", draw)
    return dict(id="s4_lattice_box", step="Step 4", title="The weight box with the lattice known",
                caption=("Lane B2.1(d), certified outer bounds (LP duals re-verified at 100 digits). With the pole, the "
                         "archimedean place and the possible positions log n, n = 2..12, fixed and the 11 weights w_n free, "
                         "Weil positivity of the x = 13 window (N = 20) confines each weight to the drawn interval around "
                         "Lambda(n)/sqrt(n), including the zero weights at the non-prime-powers 6, 10, 12. (c1) weights on "
                         "their natural scale: the intervals are thinner than the markers. (c2) the intervals as deviations "
                         "from the truth on a symmetric-log axis, labelled with the widths lane B2 computed; these are the tolerance of its double-precision LP, and the exact LP of the RTP-1 review gives 3e-25 at n = 2 to 1.3e-4 at n = 12, so the true boxes are 1 to 18 orders tighter than drawn (1e-12 at n = 4 to 1.3e-3 at "
                         "n = 12). (c3) the largest width over n <= 7, 10, 12 against N; for N >= 30 the widths are "
                         "limited by lane B2's certificate construction, not by the set. The same positivity in the free "
                         "Loewner coordinates leaves an unbounded set (Step 4 positive-set figure)."),
                panels=["weights and intervals (certified)", "deviation intervals, symlog (certified)",
                        "widths against N (certified)"],
                kind="certified data", sources=[C.rel(B2_OUT)], script=SCRIPT)


def fig_capture(txt):
    Nt = b2_Ntable(txt)
    co = b2_coefficients(txt)
    check([r["N"] for r in Nt] == [10, 20, 30, 40, 60], "B2 N table: N = 10, 20, 30, 40, 60")
    check(all(Nt[i]["min_capt"] > Nt[i + 1]["min_capt"] for i in range(len(Nt) - 1)),
          "captured fraction of the min-norm prediction decreases with N (B2)")
    prod = [r["min_capt"] * r["true_hs"] ** 2 for r in Nt]
    kappa = sum(prod) / len(prod)
    rows = [(r["N"], r["true_hs"], r["min_hs"], r["min_dist"], r["min_capt"], r["md_dist"], r["md_capt"],
             r["pnt_dist"], r["pnt_capt"], r["lmin_true"]) for r in Nt]
    C.write_table("s4_capture", ["N", "norm_true_HS", "min_norm_HS", "minnorm_rel_dist", "minnorm_captured",
                                 "maxdet_ball_rel_dist", "maxdet_ball_captured", "PNT_rel_dist", "PNT_captured",
                                 "lambda_min_true"], rows,
                  ["certified, outputs/rtp1_commutant.txt section 5 (x = 13); coefficient table (section 4, N = 20) in the "
                   "panels (d3), (d4)",
                   "derived for the reference curve: mean of captured * ||z_true||^2 = %.4f" % kappa])

    def draw():
        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(2, 2, figsize=(12, 8.2), gridspec_kw=dict(hspace=0.42, wspace=0.2))
        (a1, a2), (a3, a4) = axs
        Ns = np.array([r["N"] for r in Nt])
        ser = [("min", "minimal-norm element", S(1), "o"), ("md", "max det on the ball ||z|| <= ||z_true||", S(5), "s"),
               ("pnt", "PNT mean (inadmissible)", S(4), "^")]
        for key, lab, c, m in ser:
            a1.plot(Ns, [r[key + "_capt"] for r in Nt], m + "-", color=c, label=lab, **C.ring())
            a2.plot(Ns, [r[key + "_dist"] for r in Nt], m + "-", color=c, label=lab, **C.ring())
        nn = np.linspace(10, 60, 200)
        th = np.interp(nn, Ns, [r["true_hs"] for r in Nt])
        a1.plot(nn, kappa / th ** 2, color=T["ink2"], lw=0.9)
        a1.text(21, 0.018, "grey reference: %.2f / ||z_true||^2" % kappa, fontsize=7.5, color=T["ink2"])
        a1.text(Ns[0] - 0.9, Nt[0]["min_capt"], "%.1f%%" % (100 * Nt[0]["min_capt"]), ha="right", va="center",
                fontsize=7.5, color=T["ink2"])
        a1.text(Ns[-1] + 0.8, Nt[-1]["min_capt"] - 0.012, "%.1f%%" % (100 * Nt[-1]["min_capt"]), ha="left", va="top",
                fontsize=7.5, color=T["ink2"])
        a1.set_ylim(0, 0.5)
        a1.set_xlim(4, 64)
        a1.set_xlabel("N (x = 13)")
        a1.set_ylabel("captured fraction <z_p, z_true> / ||z_true||^2")
        a1.set_title("(d1) fraction of the true prime data captured")
        a1.legend(loc="upper right", fontsize=7.5)
        a2.axhline(1, color=T["ink2"], lw=0.9)
        a2.text(60, 1.015, "1 = predicting no prime data", ha="right", fontsize=7.5, color=T["ink2"])
        a2.set_ylim(0.7, 1.5)
        a2.set_xlabel("N (x = 13)")
        a2.set_ylabel("relative distance ||z_p - z_true|| / ||z_true||")
        a2.set_title("(d2) relative distance from the truth")
        n = np.arange(N + 1)
        for ax, off, lab in ((a3, 0, "u_n (prime part of a_n)"), (a4, 4, "v_n (prime part of b_n)")):
            sl = slice(0, N + 1) if off == 0 else slice(1, N + 1)
            ax.axhline(0, color=T["axis"], lw=0.8)
            ax.plot(n[sl], [co[k][off + 0] for k in n[sl]], "D-", color=S(2), lw=1.0, label="truth", **C.ring())
            ax.plot(n[sl], [co[k][off + 1] for k in n[sl]], "o-", color=S(1), label="minimal-norm", **C.ring())
            ax.plot(n[sl], [co[k][off + 3] for k in n[sl]], "^-", color=S(4), lw=1.0, label="PNT mean", **C.ring())
            ax.plot(n[sl], [co[k][off + 2] for k in n[sl]], "s-", color=S(5), lw=1.0, label="max det on the ball",
                    **C.ring(ms=4.5))
            ax.set_xlabel("n")
            ax.set_ylabel(lab)
            ax.set_xticks(range(0, N + 1, 2))
        a3.set_title("(d3) the coefficients at N = 20: u_n")
        a4.set_title("(d4) v_n: the truth is full-band, the prediction a smooth bump")
        a3.legend(loc="lower right", ncol=2, fontsize=7.5)
        fig.suptitle("Step 4: how much of the true prime data the kinematic predictions capture (x = 13)", x=0.06,
                     ha="left", fontsize=12, fontweight="bold", color=T["ink"])
        fig.subplots_adjust(left=0.07, right=0.985, top=0.9, bottom=0.07)
        return fig
    C.render("s4_capture", draw)
    return dict(id="s4_capture", step="Step 4", title="Captured fraction of the true prime data",
                caption=("Lane B2.1(c), certified (x = 13; Hilbert-Schmidt inner product on the window). (d1) Fraction of "
                         "the true prime contribution captured by each prediction against N: the minimal-norm element "
                         "captures 16%%, 8.3%%, 5.6%%, 4.1%%, 2.8%% at N = 10, 20, 30, 40, 60. The grey curve is %.2f / "
                         "||z_true||^2, derived from B2's columns: the correction positivity demands is fixed (norm about "
                         "2.37) while the truth's norm grows. (d2) Relative distance from the truth; the ball-relaxed "
                         "maximum-determinant element is farther than predicting no prime data (1.25 to 1.39). (d3, d4) B2's "
                         "coefficient table at N = 20: the minimal-norm prediction matches (u_1, u_2, v_1, v_2) to about 6%%, "
                         "misses u_0 (0 against -2.94) and is a smooth decaying tail where the true data are O(1) at every "
                         "n; the ball max-det element raises every u_n by about 1 (\"add the identity\")." % kappa),
                panels=["captured fraction against N (certified; reference curve derived)", "relative distance (certified)",
                        "u_n at N = 20 (certified)", "v_n at N = 20 (certified)"],
                kind="certified data", sources=[C.rel(B2_OUT)], script=SCRIPT)


def run():
    txt = _text()
    G = geometry(txt)
    entries = [fig_dimensions(txt), fig_positive_set(txt, G), fig_lattice_box(txt), fig_capture(txt)]
    C.register(STEP, entries)
    return entries


if __name__ == "__main__":
    run()
