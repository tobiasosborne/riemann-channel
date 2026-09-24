"""Shared helpers for the RTP-1 figure package (lane V; author line claude:opus).

Theme: the validated reference palette of the `dataviz` skill (categorical slots in fixed order, a
single-hue blue sequential ramp, a blue <-> red diverging pair with a neutral grey midpoint), selected
separately for a light and a dark surface.  Every figure is rendered twice: `<id>.{png,svg}` on the
light surface and `<id>.dark.{png,svg}` on the dark surface.

Determinism: no timestamps (SVG `Date` metadata removed, fixed `svg.hashsalt`), no randomness, fixed
DPI; the plotted numbers of every figure are also written to `figures/rtp1/data/<id>.csv` (the table
view of the figure).
"""
import csv
import io
import json
import math
import os
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt                     # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FIG = os.path.join(REPO, "figures", "rtp1")
DATA = os.path.join(FIG, "data")
OUT = os.path.join(REPO, "outputs")
MANIFEST = os.path.join(FIG, "manifest")
AUTHOR = "claude:opus"

THEMES = {
    "light": dict(
        surface="#fcfcfb", ink="#0b0b0b", ink2="#52514e", muted="#898781", grid="#e1e0d9", axis="#c3c2b7",
        series=["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"],
        mid="#f0efec", neg="#e34948", neg_deep="#9c2b2b", pos="#2a78d6", pos_deep="#104281",
        seq=["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"],
        wash=0.10, badge="#f0efec"),
    "dark": dict(
        surface="#1a1a19", ink="#ffffff", ink2="#c3c2b7", muted="#898781", grid="#2c2c2a", axis="#383835",
        series=["#3987e5", "#d95926", "#199e70", "#c98500", "#d55181", "#008300", "#9085e9", "#e66767"],
        mid="#383835", neg="#e66767", neg_deep="#f2a8a8", pos="#3987e5", pos_deep="#9ec5f4",
        seq=["#0d366b", "#184f95", "#256abf", "#3987e5", "#6da7ec", "#9ec5f4", "#cde2fb"],
        wash=0.14, badge="#2c2c2a"),
}
T = dict(THEMES["light"])      # the active theme (mutated by set_theme)


def set_theme(name):
    T.clear()
    T.update(THEMES[name])
    T["name"] = name
    plt.rcdefaults()
    plt.rcParams.update({
        "figure.facecolor": T["surface"], "axes.facecolor": T["surface"], "savefig.facecolor": T["surface"],
        "text.color": T["ink"], "axes.labelcolor": T["ink2"], "axes.edgecolor": T["axis"],
        "xtick.color": T["muted"], "ytick.color": T["muted"], "xtick.labelcolor": T["ink2"],
        "ytick.labelcolor": T["ink2"], "axes.titlecolor": T["ink"],
        "font.family": "sans-serif", "font.sans-serif": ["DejaVu Sans"], "font.size": 9,
        "axes.titlesize": 10, "axes.titleweight": "bold", "axes.titlelocation": "left", "axes.labelsize": 9,
        "xtick.labelsize": 8, "ytick.labelsize": 8, "legend.fontsize": 8, "legend.frameon": False,
        "axes.spines.top": False, "axes.spines.right": False, "axes.linewidth": 0.8,
        "axes.grid": True, "grid.color": T["grid"], "grid.linewidth": 0.6, "grid.linestyle": "-",
        "axes.axisbelow": True, "lines.linewidth": 1.6, "lines.solid_capstyle": "round",
        "lines.solid_joinstyle": "round", "lines.markersize": 5.5, "patch.linewidth": 0,
        "svg.hashsalt": "rtp1-lane-V", "svg.fonttype": "path", "figure.dpi": 100,
        "axes.prop_cycle": matplotlib.cycler(color=T["series"]),
        "legend.labelcolor": T["ink2"], "image.interpolation": "nearest",
    })


set_theme("light")


def S(i):
    """categorical slot i (1-based), fixed order"""
    return T["series"][i - 1]


def cmap_div():
    """diverging: negative = red arm, zero = neutral grey, positive = blue arm"""
    return LinearSegmentedColormap.from_list(
        "rtp1_div_" + T["name"], [T["neg_deep"], T["neg"], T["mid"], T["pos"], T["pos_deep"]])


def cmap_seq():
    return LinearSegmentedColormap.from_list("rtp1_seq_" + T["name"], [T["surface"]] + T["seq"])


def ring(**kw):
    """marker style: filled series colour with a surface-coloured ring"""
    d = dict(markeredgecolor=T["surface"], markeredgewidth=1.2)
    d.update(kw)
    return d


def badge(ax, text="comparison (zeros used)", loc="upper right"):
    """the label every panel that uses zeros of zeta must carry (game rule 2)"""
    xy = {"upper right": (0.99, 0.98, "right", "top"), "lower right": (0.99, 0.03, "right", "bottom"),
          "upper left": (0.01, 0.98, "left", "top"), "lower left": (0.01, 0.03, "left", "bottom")}[loc]
    ax.text(xy[0], xy[1], text, transform=ax.transAxes, ha=xy[2], va=xy[3], fontsize=8, color=T["ink"],
            fontweight="bold", bbox=dict(boxstyle="round,pad=0.3", fc=T["badge"], ec=T["axis"], lw=0.6),
            zorder=20)


def note(ax, text, x=0.01, y=0.98, ha="left", va="top", size=8, color=None, **kw):
    ax.text(x, y, text, transform=ax.transAxes, ha=ha, va=va, fontsize=size, color=color or T["ink2"], **kw)


def vline_ticks(ax, xs, ymin=0.0, ymax=0.04, color=None, lw=0.8):
    """short ticks at the bottom of an axis (prime-power markers)"""
    for x in xs:
        ax.axvline(x, ymin=ymin, ymax=ymax, color=color or T["muted"], lw=lw, zorder=1)


# ---------------------------------------------------------------------------------------------------
# saving, tables, manifest
# ---------------------------------------------------------------------------------------------------
def savefig(fig, fid):
    os.makedirs(FIG, exist_ok=True)
    suffix = "" if T["name"] == "light" else ".dark"
    base = os.path.join(FIG, fid + suffix)
    fig.savefig(base + ".png", dpi=160, metadata={"Software": None})
    buf = io.StringIO()
    fig.savefig(buf, format="svg", metadata={"Date": None, "Creator": None})
    svg = re.sub(r"\n\s*<dc:date>.*?</dc:date>", "", buf.getvalue())
    with open(base + ".svg", "w") as fh:
        fh.write(svg)
    plt.close(fig)


def render(fid, draw):
    """draw(fig-producing callable) in both themes; returns nothing"""
    for name in ("light", "dark"):
        set_theme(name)
        fig = draw()
        savefig(fig, fid)
    set_theme("light")


def write_table(fid, header, rows, note_lines=()):
    """the table view of a figure: CSV with a commented provenance header"""
    os.makedirs(DATA, exist_ok=True)
    with open(os.path.join(DATA, fid + ".csv"), "w", newline="") as fh:
        for ln in note_lines:
            fh.write("# " + ln + "\n")
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(header)
        for r in rows:
            w.writerow([fmt(x) for x in r])


def fmt(x):
    if isinstance(x, float):
        if x == 0 or math.isnan(x) or math.isinf(x):
            return repr(x)
        return "%.10g" % x
    return str(x)


def register(step, entries):
    """write the manifest of a step: list of dict(id, title, caption, panels, sources, script, status)"""
    os.makedirs(MANIFEST, exist_ok=True)
    with open(os.path.join(MANIFEST, step + ".json"), "w") as fh:
        json.dump(entries, fh, indent=1, sort_keys=True)
        fh.write("\n")


# ---------------------------------------------------------------------------------------------------
# parsers for lane A1 outputs (formats: notes/rtp-round-1/lane-A1.md; zst/tools/rtp1_a1_summary.py)
# ---------------------------------------------------------------------------------------------------
def num(s):
    """midpoint of a printed ball or number ('1.23e-5', '[1.2 +/- 3e-4]', '[+/- 1e-209]' -> 0)"""
    s = s.strip()
    m = re.match(r"\[([-+0-9.e]+) \+/- ", s)
    if m:
        return float(m.group(1))
    if s.startswith("[+/-"):
        return 0.0
    return float(s)


def log10s(s):
    """log10 of a positive printed number, robust below the double range"""
    m = re.match(r"\[?([0-9.]+)e([-+]?[0-9]+)", s.strip())
    if m:
        return math.log10(float(m.group(1))) + int(m.group(2))
    return math.log10(float(s))


def a1_axisN(x):
    """rows of outputs/rtp1_a1_axisN_x<x>.txt: main table, comparison table, Rayleigh table"""
    path = os.path.join(OUT, "rtp1_a1_axisN_x%d.txt" % x)
    rows, cmp_rows, ray = [], [], []
    sect = "main"
    for line in open(path):
        if line.startswith("# certified minimal eigenvalue"):
            sect = "cmp"
        if line.startswith("# Rayleigh"):
            sect = "ray"
        if line.startswith("#") or not line.strip():
            continue
        f = line.split()
        if sect == "ray":
            if f[0] in ("pole", "arch", "eps"):
                ray.append((f[0], f[1:]))
            elif f[0] == "k":
                ray.append(("k=" + f[2], f[3:]))
            continue
        if not f[0].isdigit():
            continue
        if sect == "cmp":
            cmp_rows.append(dict(N=int(f[0]), eps=f[1], lg_eps=log10s(f[1]), err=f[4], lg_err=log10s(f[4])))
        elif len(f) == 12:
            rows.append(dict(N=int(f[0]), s_e=num(f[1]), s_o=num(f[2]), dI=num(f[3]), dI_e=num(f[4]),
                             logdet=num(f[5]), r_e=num(f[6]), r_o=num(f[7]), r_j=num(f[8]), tau=num(f[9]),
                             dIs=num(f[10]), b=num(f[11])))
    return dict(x=x, rows=rows, cmp=cmp_rows, ray=ray, path=os.path.relpath(path, REPO))


def a1_axisx(kind, N):
    """outputs/rtp1_a1_axisx_<kind>_N<N>.txt, kind in ('ccm', 'fixedL')"""
    path = os.path.join(OUT, "rtp1_a1_axisx_%s_N%d.txt" % (kind, N))
    main, control, cmp_rows = [], [], []
    sect = "main"
    for line in open(path):
        if line.startswith("# CONTROL"):
            sect = "control"
        elif line.startswith("# Rayleigh"):
            sect = "ray"
        elif line.startswith("# COMPARISON"):
            sect = "cmp"
        if line.startswith("#") or not line.strip():
            continue
        f = line.split()
        try:
            float(f[0])
        except ValueError:
            continue
        if sect == "main" and len(f) == 12:
            d = dict(x=float(f[0]), X=int(f[1]), npp=int(f[2]), eps=f[3], neg=int(f[4]), es=f[5],
                     logdet=num(f[6]), ov_c=num(f[7]), ov_f=(num(f[8]) if f[8] != "-" else None),
                     dI=(num(f[9]) if f[9] != "-" else None), r_j=(f[10] if f[10] != "-" else None),
                     tau=(num(f[11]) if f[11] != "-" else None))
            d["eps_f"] = num(f[3]) if abs(num(f[3])) > 1e-300 else None
            d["lg_eps"] = log10s(f[3]) if not f[3].startswith("-") else None
            d["lg_rj"] = log10s(f[10]) if f[10] != "-" else None
            main.append(d)
        elif sect == "control" and len(f) == 3:
            control.append(dict(x=float(f[0]), lam=float(f[1]), neg=int(f[2])))
        elif sect == "cmp" and len(f) == 4:
            cmp_rows.append(dict(x=float(f[0]), X=int(f[1]), roots=int(f[2]), err=f[3], lg_err=log10s(f[3])))
    return dict(main=main, control=control, cmp=cmp_rows, path=os.path.relpath(path, REPO))


# ---------------------------------------------------------------------------------------------------
# parsers for lane A2 output (outputs/rtp1_prime_content.txt)
# ---------------------------------------------------------------------------------------------------
A2_OUT = os.path.join(OUT, "rtp1_prime_content.txt")


def _set(s):
    return tuple(int(t) for t in re.findall(r"\d+", s))


def a2_admissible():
    rows = []
    txt = open(A2_OUT).read().split("2. TEST CLASS")[1].split("3. BUMP")[0]
    for line in txt.splitlines():
        m = re.match(r"\s+(\{[\d, ]+\})\s+(\d+)\s+(\d+)\s+(\d+)\s+([0-9.e-]+) \(\+/- [0-9.e-]+\)\s+(\d+) vs (\d+)\s+([0-9.]+)", line)
        if m:
            rows.append(dict(S=_set(m.group(1)), A=int(m.group(2)), dim=int(m.group(3)), dmax=float(m.group(5)),
                             r=int(m.group(6)), k=int(m.group(7)), minlogr=float(m.group(8))))
    return rows


def a2_summary():
    rows = []
    txt = open(A2_OUT).read().split("5b. SUMMARY TABLE")[1].split("mixed gap / delta")[0]
    for line in txt.splitlines():
        m = re.match(r"\s+(\{[\d, ]+\})\s+(\d+)\s+(.*)$", line)
        if not m:
            continue
        f = m.group(3).split()
        if len(f) != 10:
            continue
        rows.append(dict(S=_set(m.group(1)), A=int(m.group(2)), delta=float(f[0]), d=float(f[1]), lam=float(f[2]),
                         lamX=float(f[3]), lambd=float(f[4]), lamnomix=float(f[5]), lamnoP=float(f[6]),
                         gap_mix=float(f[7]), offaxis=float(f[8]), schmidt=float(f[9])))
    return rows


def a2_movement():
    rows = []
    for line in open(A2_OUT):
        m = re.match(r"\s+A = (\d), delta =\s+([0-9.e-]+):\s+(\{[\d, ]+\}) ->\s+(\{[\d, ]+\}): 1 - overlap =\s+([0-9.e+-]+), "
                     r"weight on old sublattice ([0-9.]+) \(Kronecker prediction ([0-9.]+)\), lambda ([0-9.]+) -> ([0-9.]+)", line)
        if m:
            rows.append(dict(A=int(m.group(1)), delta=float(m.group(2)), small=_set(m.group(3)), big=_set(m.group(4)),
                             one_minus_ov=float(m.group(5)), weight=float(m.group(6)), kron=float(m.group(7)),
                             lam_small=float(m.group(8)), lam_big=float(m.group(9))))
    return rows


def a2_comparison():
    """section 7 (zeros used): for each (delta, r): Psi, M list, |Psi - Z_M|, absolute tails"""
    txt = open(A2_OUT).read().split("7. COMPARISON STEP")[1]
    out = []
    lines = txt.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"\s+delta =\s+([0-9.]+), r =\s+([0-9/]+) \(D = ([0-9.]+), prime powers \[([\d, ]*)\]\): Psi = ([-0-9.e]+)", line)
        if m:
            Ms = [int(t) for t in lines[i + 1].split(":")[1].split()]
            errs = [float(t) for t in lines[i + 2].split(":")[1].split()]
            tails = [float(t) for t in lines[i + 3].split(":")[1].split()]
            out.append(dict(delta=float(m.group(1)), r=m.group(2), D=float(m.group(3)),
                            ks=[int(t) for t in m.group(4).replace(",", " ").split()], psi=float(m.group(5)),
                            M=Ms, err=errs, tail=tails))
    return out


# ---------------------------------------------------------------------------------------------------
# number theory helpers (display only)
# ---------------------------------------------------------------------------------------------------
def prime_powers(X):
    """dict k -> p for prime powers k <= X"""
    s = bytearray([1]) * (X + 1)
    s[0] = s[1] = 0
    for i in range(2, int(X ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    out = {}
    for p in range(2, X + 1):
        if s[p]:
            k = p
            while k <= X:
                out[k] = p
                k *= p
    return out


def rel(path):
    return os.path.relpath(path, REPO)
