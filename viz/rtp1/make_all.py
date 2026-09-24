#!/usr/bin/env python3
"""Build every RTP-1 figure, figures/rtp1/index.html and figures/rtp1/README.md (lane V; author claude:opus).

    python3 viz/rtp1/make_all.py            # from anywhere; ~1 minute single-threaded

Deterministic: no timestamps, no randomness; running it twice gives byte-identical files (checked with cmp).
Requirements: python3 with numpy, mpmath, matplotlib, python-flint 0.9.0; a C compiler and zst/build/libzst.a
(built with `make -C zst` if absent) for zst's (a_n, b_n).
"""
import glob
import html
import json
import os
import sys
import time

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")

import common as C  # noqa: E402

STEPS = [
    ("step0", "step0_objects", "Step 0: the objects",
     "The multiplicative line, the Weil distribution, the test functions and the lattices, drawn from closed forms."),
    ("step1", "step1_dilation", "Step 1: the dilation channel (lane A1)",
     "Lane A1's certified outputs, plus window matrices and eigenvectors recomputed for display from zst's (a_n, b_n)."),
    ("step2", "step2_prime_content", "Step 2: the prime-content channel (lane A2)",
     "Lane A2's Gram matrices and eigenvectors from its own routines, its certified scaling tables, and the labelled "
     "explicit-formula comparison."),
    ("step3", "step3_short_range", "Step 3: short-range positivity (lane B1)",
     "The Weil distribution near the origin and the form value of a bump, with lane B1's statements of Yoshida and Bombieri."),
    ("step4", "step4_commutant", "Step 4: the kinematic commutant (lane B2)", "Pending lane B2."),
    ("step5", "step5_calibration", "Step 5: the calibration case (lane B2)", "Pending lane B2."),
    ("step7", "step7_maxent", "Step 7: the contradiction pathway and MaxEnt",
     "From notes/metric-tomography/metric-as-state.md section 7: the extension disc as the Schur algorithm proceeds, and "
     "the off-line pair as a saddle."),
]

RULE = ("Game rule 2 applies to the figures: zeros of zeta appear only in panels labelled \"comparison (zeros used)\" "
        "(Step 1 envelope panel b; Step 2 explicit-formula panels). Every other number comes from primes, the pole and the "
        "archimedean place.")


def clean():
    for pat in ("*.png", "*.svg", "*.html", "README.md", "data/*.csv", "manifest/*.json"):
        for p in glob.glob(os.path.join(C.FIG, pat)):
            os.remove(p)


def load_manifest():
    out = []
    for key, _mod, title, intro in STEPS:
        with open(os.path.join(C.MANIFEST, key + ".json")) as fh:
            out.append((key, title, intro, json.load(fh)))
    return out


def esc(s):
    return html.escape(s, quote=True)


CSS = """
:root { color-scheme: light;
  --surface:#fcfcfb; --page:#f9f9f7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781; --rule:#e1e0d9;
  --badge:#f0efec; --accent:#2a78d6; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { color-scheme: dark;
  --surface:#1a1a19; --page:#0d0d0d; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --rule:#2c2c2a;
  --badge:#2c2c2a; --accent:#3987e5; } }
:root[data-theme="dark"] { color-scheme: dark;
  --surface:#1a1a19; --page:#0d0d0d; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --rule:#2c2c2a;
  --badge:#2c2c2a; --accent:#3987e5; }
* { box-sizing: border-box; }
body { margin:0; background:var(--page); color:var(--ink);
  font: 15px/1.55 system-ui, -apple-system, "Segoe UI", sans-serif; }
main { max-width: 1180px; margin: 0 auto; padding: 32px 16px 64px; }
h1 { font-size: 26px; margin: 0 0 6px; }
h2 { font-size: 20px; margin: 44px 0 4px; padding-top: 12px; border-top: 1px solid var(--rule); }
p.lede, p.intro { color: var(--ink2); margin: 4px 0 14px; max-width: 78ch; }
nav ul { list-style:none; padding:0; margin: 14px 0 0; display:flex; flex-wrap:wrap; gap:6px 16px; }
nav a, a { color: var(--accent); }
figure { margin: 18px 0 28px; background: var(--surface); border: 1px solid var(--rule); border-radius: 10px;
  padding: 14px 14px 12px; }
figure img { display:block; width:100%; height:auto; }
figcaption { margin-top: 10px; }
figcaption h3 { font-size: 16px; margin: 0 0 4px; }
figcaption p { margin: 4px 0; color: var(--ink2); max-width: 100ch; }
dl.meta { display:grid; grid-template-columns: max-content 1fr; gap: 2px 12px; margin: 8px 0 0; font-size: 13px; }
dl.meta dt { color: var(--muted); }
dl.meta dd { margin: 0; color: var(--ink2); overflow-wrap: anywhere; }
code { font: 12.5px/1.4 ui-monospace, SFMono-Regular, Menlo, monospace; }
.badge { display:inline-block; font-size:12px; padding:1px 8px; border-radius:9px; background:var(--badge);
  color:var(--ink); border:1px solid var(--rule); margin-left:6px; vertical-align:2px; }
.placeholder { border-style: dashed; }
.fid { color: var(--muted); font-weight: normal; font-size: 13px; }
"""


def build_html(man):
    parts = ["<!doctype html>", "<html lang=\"en\">", "<head>", "<meta charset=\"utf-8\">",
             "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">",
             "<title>RTP-1 figures</title>", "<style>" + CSS + "</style>", "</head>", "<body>", "<main>",
             "<h1>RTP-1 figures</h1>",
             "<p class=\"lede\">Figures for round 1 of the Riemann Tomography Problem "
             "(<code>notes/rtp-round-1/brief.md</code>, <code>notes/rtp-round-1/viz-brief.md</code>), one set per step. "
             "Figures are secondary sources: each caption says which panels plot certified data from a lane's committed "
             "output and which are recomputed for display. Author: <code>claude:opus</code> (lane V). Built by "
             "<code>python3 viz/rtp1/make_all.py</code>.</p>",
             "<p class=\"lede\">" + esc(RULE) + "</p>",
             "<p class=\"lede\">Each figure has a dark-surface variant (<code>&lt;id&gt;.dark.png/.svg</code>, shown when the "
             "system is in dark mode) and a table view <code>data/&lt;id&gt;.csv</code> with the plotted numbers.</p>",
             "<nav><ul>"]
    for key, title, _i, _e in man:
        parts.append("<li><a href=\"#%s\">%s</a></li>" % (key, esc(title)))
    parts.append("</ul></nav>")
    for key, title, intro, entries in man:
        parts.append("<h2 id=\"%s\">%s</h2>" % (key, esc(title)))
        parts.append("<p class=\"intro\">%s</p>" % esc(intro))
        for e in entries:
            parts.append(card_html(e))
    parts += ["</main>", "</body>", "</html>", ""]
    return "\n".join(parts)


def card_html(e):
    fid = e["id"]
    if e.get("placeholder"):
        return ("<figure class=\"placeholder\" id=\"%s\"><figcaption><h3>%s <span class=\"badge\">placeholder</span> "
                "<span class=\"fid\">%s</span></h3><p>%s</p><dl class=\"meta\"><dt>script</dt><dd><code>%s</code></dd>"
                "</dl></figcaption></figure>" % (fid, esc(e["title"]), fid, esc(e["caption"]), esc(e["script"])))
    zeros = "zeros used" in e["kind"]
    badge = "<span class=\"badge\">comparison (zeros used) in part</span>" if zeros else ""
    img = ("<picture><source srcset=\"%s.dark.svg\" media=\"(prefers-color-scheme: dark)\">"
           "<img src=\"%s.svg\" alt=\"%s\" loading=\"lazy\"></picture>" % (fid, fid, esc(e["title"])))
    meta = ["<dt>panels</dt><dd>%s</dd>" % esc("; ".join(e["panels"])),
            "<dt>kind</dt><dd>%s</dd>" % esc(e["kind"]),
            "<dt>data source</dt><dd>%s</dd>" % "<br>".join("<code>%s</code>" % esc(s) for s in e["sources"]),
            "<dt>script</dt><dd><code>%s</code></dd>" % esc(e["script"]),
            "<dt>files</dt><dd><a href=\"%s.png\">png</a> &middot; <a href=\"%s.svg\">svg</a> &middot; "
            "<a href=\"%s.dark.png\">dark png</a> &middot; <a href=\"data/%s.csv\">table (csv)</a></dd>" % (fid, fid, fid, fid)]
    return ("<figure id=\"%s\">%s<figcaption><h3>%s %s <span class=\"fid\">%s</span></h3><p>%s</p><dl class=\"meta\">%s"
            "</dl></figcaption></figure>" % (fid, img, esc(e["title"]), badge, fid, esc(e["caption"]), "".join(meta)))


def build_md(man):
    L = ["# RTP-1 figures", "",
         "Figures for round 1 of the Riemann Tomography Problem (`notes/rtp-round-1/brief.md`, "
         "`notes/rtp-round-1/viz-brief.md`), one set per step. Author: `claude:opus` (lane V). Built by "
         "`python3 viz/rtp1/make_all.py` (deterministic, no timestamps). Each caption says which panels plot certified "
         "data and which are recomputed for display. Every figure also exists on a dark surface (`<id>.dark.png`, "
         "`<id>.dark.svg`), and its plotted numbers are in `data/<id>.csv`. The same content with dark-mode switching: "
         "`index.html`.", "", RULE, ""]
    for key, title, intro, entries in man:
        L += ["## " + title, "", intro, ""]
        for e in entries:
            if e.get("placeholder"):
                L += ["### %s (placeholder)" % e["title"], "", e["caption"], "", "Script: `%s`." % e["script"], ""]
                continue
            L += ["### %s (`%s`)" % (e["title"], e["id"]), "", "![%s](%s.png)" % (e["title"], e["id"]), "", e["caption"], "",
                  "- Panels: " + "; ".join(e["panels"]),
                  "- Kind: " + e["kind"],
                  "- Data source: " + "; ".join("`%s`" % s for s in e["sources"]),
                  "- Script: `%s`" % e["script"],
                  "- Files: `%s.png`, `%s.svg`, `%s.dark.png`, `%s.dark.svg`, `data/%s.csv`" % ((e["id"],) * 5), ""]
    return "\n".join(L)


def main():
    t0 = time.time()
    clean()
    timing = []
    for key, mod, _t, _i in STEPS:
        t = time.time()
        __import__(mod).run()
        timing.append((key, time.time() - t))
        print("%-6s %6.1f s" % (key, timing[-1][1]), flush=True)
    man = load_manifest()
    with open(os.path.join(C.FIG, "index.html"), "w") as fh:
        fh.write(build_html(man))
    with open(os.path.join(C.FIG, "README.md"), "w") as fh:
        fh.write(build_md(man))
    for key, _t, _i, entries in man:
        for e in entries:
            if e.get("placeholder"):
                with open(os.path.join(C.FIG, e["id"] + ".html"), "w") as fh:
                    fh.write("<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" "
                             "content=\"width=device-width, initial-scale=1\"><title>%s</title><style>%s</style></head>"
                             "<body><main><h1>%s</h1><p class=\"lede\">%s</p><p class=\"lede\"><a href=\"index.html#%s\">"
                             "Back to the index</a></p></main></body></html>\n"
                             % (esc(e["title"]), CSS, esc(e["title"]), esc(e["caption"]), key))
    n = sum(1 for _k, _t, _i, es in man for e in es if not e.get("placeholder"))
    print("figures: %d (plus %d placeholders); total %.1f s" % (
        n, sum(1 for _k, _t, _i, es in man for e in es if e.get("placeholder")), time.time() - t0))


if __name__ == "__main__":
    main()
