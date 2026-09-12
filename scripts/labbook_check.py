#!/usr/bin/env python3
"""labbook_check.py -- the lab-book gate for riemann-channel (stdlib only; run from repo root).

  python3 scripts/labbook_check.py            full check; exit 1 on any ERROR
  python3 scripts/labbook_check.py --regen    rewrite report/macros.tex and report/generated/status.tex
                                              from db/notation.tsv and db/claims.tsv
  python3 scripts/labbook_check.py --quiet    ERROR/WARN lines only

Lockstep parity it enforces (each is an ERROR unless marked WARN):

  shards     report.tex \\include list == files under report/sections (both directions, same order
             as report/README.md and report/SHARD_CATALOG.md); every shard has SHARD-ID/TITLE/
             SUMMARY(2-3)/KEYWORDS/NOTES/SCRIPTS headers; <= MAX_LINES lines; no \\newcommand in shards
  notes      every notes/*.md (top level) is named by some shard's SHARD-NOTES header, and vice versa
  scripts    every scripts/*.py is named by some shard's SHARD-SCRIPTS header and has outputs/<stem>.txt
  claims     every theorem-like environment has a \\label with a kind prefix (thm: lem: prop: cor:
             conj: obs: asm: cit: num:), a row in db/claims.tsv with the same kind, and exactly one
             \\claimstatus{<label>}{<status>} whose status equals the DERIVED status of the row
             (rk-light rules: refuted/open/conjectured dep -> unsupported; assumed dep -> -conditional;
             sketched dep caps at sketched; numerical is a ceiling); proved/refuted rows need
             author != reviewer, an existing proof file and an existing review file containing
             'VERDICT <id>: VALID'; every claims row appears in exactly one shard
  defs       every definition environment has a def: label, a row in db/definitions.tsv, and appears
             exactly once; terms in db/definitions.tsv are unique (case-insensitive); 'quoted'
             definitions carry a provenance id
  notation   report/macros.tex is exactly what --regen would write from db/notation.tsv; macro names
             and symbols in the DB are unique; every DB macro is used in some shard (WARN otherwise);
             no macro used in a shard is undefined by macros.tex or the preamble
  provenance every db/provenance.tsv quote is found whole and contiguous (whitespace-normalised)
             inside refs/src/<key>/<file> within the stated line window; every provenance id
             referenced from claims/definitions exists; every \\cite key is in report/references.bib
  build      (with --build) pdflatex+bibtex succeed and the log has no undefined references or
             citations and no multiply-defined labels
"""
import os
import re
import subprocess
import sys

ROOT = os.getcwd()
MAX_LINES = int(os.environ.get("REPORT_SHARD_MAX_LINES", "320"))
KINDS = {"theorem": "thm", "lemma": "lem", "proposition": "prop", "corollary": "cor",
         "conjecture": "conj", "observation": "obs", "assumption": "asm", "citedfact": "cit",
         "numerical": "num", "definition": "def"}
CLAIM_STATUSES = {"proved", "sketched", "numerical", "conjectured", "open", "refuted", "assumed", "cited"}
DEF_STATUSES = {"quoted", "stipulated"}

LATEX_RESERVED = set("""alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda mu nu xi pi varpi rho
varrho sigma varsigma tau upsilon phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
prime hat bar vec dot tilde Re Im log exp sin cos tan det dim ker deg gcd max min sup inf lim sum prod int
S P L H O left right big Big frac sqrt over cal bf it rm sf tt em tiny small large section label ref cite input
include begin end item par newcommand def let if else fi""".split())

errors, warns = [], []
def err(m): errors.append(m)
def warn(m): warns.append(m)

def read(rel):
    p = os.path.join(ROOT, rel)
    return open(p, encoding="utf-8", errors="replace").read() if os.path.isfile(p) else None

def norm_ws(s):
    return re.sub(r"\s+", " ", s).strip()

def parse_tsv(rel, cols):
    text = read(rel)
    if text is None:
        err(f"{rel}: missing"); return []
    rows = []
    lines = [l for l in text.splitlines() if l.strip() and not l.startswith("#")]
    if not lines:
        err(f"{rel}: empty"); return []
    header = lines[0].split("\t")
    if header != cols:
        err(f"{rel}: header {header} != expected {cols}"); return []
    for n, l in enumerate(lines[1:], 2):
        cells = l.split("\t")
        if len(cells) != len(cols):
            err(f"{rel}:{n}: {len(cells)} cells, expected {len(cols)}"); continue
        rows.append(dict(zip(cols, cells)))
    return rows

def strip_comments(t):
    return re.sub(r"(?<!\\)%.*", "", t)

def mask_detokenize(t):
    """Blank the argument of every \\detokenize{...} (balanced braces) so quoted TeX is not scanned."""
    out, i = [], 0
    while True:
        j = t.find("\\detokenize{", i)
        if j < 0:
            out.append(t[i:]); break
        k = j + len("\\detokenize{"); depth = 1
        while k < len(t) and depth:
            depth += {"{": 1, "}": -1}.get(t[k], 0); k += 1
        out.append(t[i:j] + "\\detokenize{" + " " * (k - j - len("\\detokenize{") - 1) + "}")
        i = k
    return "".join(out)

# ---------------------------------------------------------------- databases
NOTATION_COLS = ["macro", "latex", "meaning", "domain", "defined_in", "note"]
DEF_COLS = ["id", "term", "shard", "status", "provenance", "merged_from"]
CLAIM_COLS = ["id", "kind", "status", "deps", "shard", "statement", "proof", "author", "review", "note"]
PROV_COLS = ["id", "key", "file", "lines", "quote", "used_by"]

def load_dbs():
    return (parse_tsv("db/notation.tsv", NOTATION_COLS), parse_tsv("db/definitions.tsv", DEF_COLS),
            parse_tsv("db/claims.tsv", CLAIM_COLS), parse_tsv("db/provenance.tsv", PROV_COLS))

# ---------------------------------------------------------------- derived status (rk-light rules)
def split_deps(cell):
    cell = cell.strip()
    if not cell or cell == "-":
        return []
    return [[d.strip() for d in alt.split("|")] for alt in cell.split(";")]

def derive(claims):
    by_id = {c["id"]: c for c in claims}
    eff, cond = {}, {}
    def rec(i, stack):
        if i in eff:
            return eff[i], cond[i]
        if i in stack:
            err(f"claims: dependency cycle at {i}"); eff[i] = "unsupported"; cond[i] = set(); return eff[i], cond[i]
        c = by_id[i]; st = c["status"]; asm = set()
        if st == "assumed":
            asm.add(i)
        worst = st
        rank = {"proved": 0, "cited": 0, "assumed": 0, "numerical": 1, "sketched": 2, "conjectured": 3, "open": 3, "refuted": 3}
        for group in split_deps(c["deps"]):
            best, best_asm = None, set()
            for d in group:
                if d not in by_id:
                    err(f"claims: {i} depends on unknown {d}"); continue
                s, a = rec(d, stack | {i})
                if best is None or rank.get(s.split("-")[0], 3) < rank.get(best.split("-")[0], 3):
                    best, best_asm = s, a
            if best is None:
                continue
            b = best.split("-")[0]
            if b in ("refuted", "open", "conjectured", "unsupported"):
                worst = "unsupported"
            elif b == "sketched" and worst in ("proved", "cited", "numerical"):
                worst = "sketched"
            elif b == "numerical" and worst in ("proved", "cited"):
                worst = "numerical"
            asm |= best_asm
        out = worst
        if out not in ("unsupported", "assumed", "cited") and asm - {i}:
            out = out + "-conditional"
        eff[i], cond[i] = out, asm
        return out, asm
    for c in claims:
        rec(c["id"], frozenset())
    return eff, cond

# ---------------------------------------------------------------- generation
def gen_macros(notation):
    out = ["% GENERATED by scripts/labbook_check.py --regen from db/notation.tsv. Do not edit.",
           "% One macro per notation row; the meaning column is the single source of truth."]
    for r in notation:
        nargs = "[1]" if "#1" in r["latex"] else ""
        out.append(f"\\newcommand{{\\{r['macro']}}}{nargs}{{{r['latex']}}}")
    return "\n".join(out) + "\n"

def tex_escape(s):
    return s.replace("\\", "\\textbackslash{}").replace("_", "\\_").replace("#", "\\#").replace("&", "\\&").replace("%", "\\%").replace("^", "\\^{}").replace("{", "\\{").replace("}", "\\}").replace("|", "$|$").replace("<", "$<$").replace(">", "$>$")

def gen_notation_table(notation):
    out = ["% GENERATED by scripts/labbook_check.py --regen from db/notation.tsv. Do not edit.",
           "{\\small\\begin{longtable}{p{2.3cm}p{7.6cm}p{2.4cm}p{1.3cm}}\\toprule",
           "symbol & meaning & domain & where \\\\ \\midrule\\endhead"]
    for r in notation:
        shown = r["latex"].replace("#1", "\\cdot")
        out.append(f"${shown}$ & {tex_escape(r['meaning'])} & {tex_escape(r['domain'])} & {tex_escape(r['defined_in'])} \\\\")
    out += ["\\bottomrule\\end{longtable}}"]
    return "\n".join(out) + "\n"

def gen_status(claims, eff, cond):
    out = ["% GENERATED by scripts/labbook_check.py --regen from db/claims.tsv. Do not edit.",
           "{\\small\\begin{longtable}{llll}\\toprule",
           "id & kind & derived status & assumptions \\\\ \\midrule\\endhead"]
    for c in claims:
        a = ", ".join(sorted(cond[c['id']] - {c['id']})) or "--"
        out.append(f"\\texttt{{{c['id']}}} & {c['kind']} & \\texttt{{{eff[c['id']]}}} & \\texttt{{{a}}} \\\\")
    out += ["\\bottomrule\\end{longtable}}"]
    return "\n".join(out).replace("_", "\\_") + "\n"

# ---------------------------------------------------------------- checks
ENV_RE = re.compile(r"\\begin\{(theorem|lemma|proposition|corollary|conjecture|observation|assumption|citedfact|numerical|definition)\}(.*?)\\end\{\1\}", re.S)

def check_shards(notation, defs, claims, prov):
    master = read("report.tex")
    if master is None:
        err("report.tex missing"); return
    m = strip_comments(master)
    includes = re.findall(r"\\include\{([^}]+)\}", m)
    if re.search(r"^\s*\\(sub)*section\{", m, re.M):
        err("report.tex contains sectioning commands; prose belongs in report/sections/")
    files_on_disk = sorted(f for f in os.listdir(os.path.join(ROOT, "report/sections")) if f.endswith(".tex"))
    inc_files = [i.split("/")[-1] + ".tex" for i in includes]
    if inc_files != files_on_disk:
        err(f"report.tex include order {inc_files} != files on disk {files_on_disk}")
    readme = read("report/README.md") or ""; catalog = read("report/SHARD_CATALOG.md") or ""
    hs = shard_headers()
    if readme != gen_readme(hs): err("report/README.md is stale; run --regen")
    if catalog != gen_catalog(hs): err("report/SHARD_CATALOG.md is stale; run --regen")
    notes_named, scripts_named, ids = set(), set(), set()
    envs_seen = {}      # label -> (kind, shard)
    env_text = {}       # label -> raw environment body
    status_tags = {}    # label -> [status,...]
    macros_used = set()
    cites = set()
    for f in files_on_disk:
        rel = f"report/sections/{f}"; raw = read(rel); n = raw.count("\n")
        if n > MAX_LINES:
            err(f"{rel}: {n} lines > {MAX_LINES}")
        hdr = lambda k: [x.strip() for x in re.findall(rf"^% SHARD-{k}:\s*(.+)$", raw, re.M)]
        sid = hdr("ID"); title = hdr("TITLE"); summ = hdr("SUMMARY"); kw = hdr("KEYWORDS"); nts = hdr("NOTES"); scr = hdr("SCRIPTS")
        if not sid or not re.match(r"^RC-\d{2}[A-Z]?-[A-Z0-9-]+$", sid[0]):
            err(f"{rel}: missing/invalid SHARD-ID"); sid = ["?"]
        elif sid[0][3:5] != f[:2]:
            err(f"{rel}: SHARD-ID {sid[0]} prefix != file prefix {f[:2]}")
        if sid[0] in ids:
            err(f"duplicate SHARD-ID {sid[0]}")
        ids.add(sid[0])
        if not title: err(f"{rel}: missing SHARD-TITLE")
        if not (2 <= len(summ) <= 3): err(f"{rel}: need 2-3 SHARD-SUMMARY lines, found {len(summ)}")
        if not kw: err(f"{rel}: missing SHARD-KEYWORDS")
        if not nts: err(f"{rel}: missing SHARD-NOTES (list notes/*.md distilled here, or 'none')")
        if not scr: err(f"{rel}: missing SHARD-SCRIPTS (list scripts/*.py evidenced here, or 'none')")
        for x in nts:
            for p in x.split(","):
                p = p.strip()
                if p and p != "none":
                    notes_named.add(p)
                    if not os.path.isfile(os.path.join(ROOT, p)): err(f"{rel}: SHARD-NOTES names missing {p}")
        for x in scr:
            for p in x.split(","):
                p = p.strip()
                if p and p != "none":
                    scripts_named.add(p)
                    if not os.path.isfile(os.path.join(ROOT, p)): err(f"{rel}: SHARD-SCRIPTS names missing {p}")
        for v in [sid[0]] + title + kw + summ:
            if v not in catalog: err(f"report/SHARD_CATALOG.md does not contain '{v}' from {rel}")
        if f"`{rel}`" not in readme or f"`{sid[0]}`" not in readme:
            err(f"report/README.md does not list {rel} / {sid[0]}")
        body = strip_comments(raw)
        if re.search(r"\\(re)?newcommand|\\def\\", body):
            err(f"{rel}: defines macros; put notation in db/notation.tsv")
        for env, inner in ENV_RE.findall(body):
            labels = re.findall(r"\\label\{([^}]+)\}", mask_detokenize(inner))
            if len(labels) != 1:
                err(f"{rel}: {env} environment with {len(labels)} labels (need exactly one): {inner[:60]!r}"); continue
            lab = labels[0]; pref = lab.split(":")[0]
            want = KINDS[env]
            if not (pref == want or (env == "theorem" and pref == "cit")):
                err(f"{rel}: label {lab} prefix does not match environment {env}")
            if lab in envs_seen: err(f"label {lab} appears in {envs_seen[lab][1]} and {rel}")
            envs_seen[lab] = (env, rel); env_text[lab] = inner
            tags = re.findall(r"\\claimstatus\{([^}]+)\}\{([^}]+)\}", mask_detokenize(inner))
            if env != "definition":
                if len(tags) != 1 or tags[0][0] != lab:
                    err(f"{rel}: {lab} needs exactly one \\claimstatus{{{lab}}}{{...}} inside the environment")
                else:
                    status_tags[lab] = tags[0][1]
            else:
                if tags: err(f"{rel}: definition {lab} must not carry a \\claimstatus")
        masked = mask_detokenize(body)
        macros_used |= set(re.findall(r"\\([A-Za-z]+)", masked))
        for c in re.findall(r"\\cite[tp]?\{([^}]+)\}", masked):
            cites |= {k.strip() for k in c.split(",")}
    # notes parity
    top_notes = {f"notes/{f}" for f in os.listdir(os.path.join(ROOT, "notes")) if f.endswith(".md")}
    for p in sorted(top_notes - notes_named): err(f"{p} is not distilled by any shard (add to a SHARD-NOTES header)")
    for p in sorted(notes_named - top_notes): err(f"SHARD-NOTES names {p} which is not a top-level note")
    # scripts parity
    top_scripts = {f"scripts/{f}" for f in os.listdir(os.path.join(ROOT, "scripts")) if f.endswith(".py") and f != "labbook_check.py" and f != "transcript_to_md.py"}
    for p in sorted(top_scripts - scripts_named): err(f"{p} is not evidenced by any shard (add to a SHARD-SCRIPTS header)")
    for p in sorted(scripts_named):
        stem = os.path.splitext(os.path.basename(p))[0]
        outs = [o for o in os.listdir(os.path.join(ROOT, "outputs")) if o.startswith(stem)]
        if not outs: err(f"{p}: no captured output under outputs/{stem}*.txt")
    # claims parity
    eff, cond = derive(claims)
    ids_db = {c["id"]: c for c in claims}
    for lab, (env, rel) in envs_seen.items():
        if env == "definition":
            continue
        if lab not in ids_db:
            err(f"{rel}: {lab} has no row in db/claims.tsv"); continue
        c = ids_db[lab]
        if c["kind"] != env and not (env == "theorem" and c["kind"] == "citedfact"):
            err(f"{lab}: kind {c['kind']} in db != environment {env}")
        if c["shard"] != rel: err(f"{lab}: db shard {c['shard']} != {rel}")
        if status_tags.get(lab) != eff[lab]:
            err(f"{lab}: printed status {status_tags.get(lab)} != derived {eff[lab]}")
    for c in claims:
        if c["id"] not in envs_seen: err(f"claims row {c['id']} has no environment in any shard")
        if c["status"] not in CLAIM_STATUSES: err(f"{c['id']}: bad status {c['status']}")
        if c["status"] in ("proved", "refuted"):
            if not c["proof"] or not os.path.isfile(os.path.join(ROOT, c["proof"])): err(f"{c['id']}: proved needs an existing proof file, got {c['proof']!r}")
            rv = c["review"]
            if not rv or not os.path.isfile(os.path.join(ROOT, rv)): err(f"{c['id']}: proved needs an existing review file")
            else:
                alias = re.search(r"review-alias=([^;\s]+)", c["note"])
                names = [c["id"]] + ([alias.group(1)] if alias else [])
                if not any(f"VERDICT {n}: VALID" in (read(rv) or "") for n in names):
                    err(f"{c['id']}: {rv} has no 'VERDICT {c['id']}: VALID' (or the review-alias named in the note column)")
                rm = re.search(r"reviewer=([^;\s]+)", c["note"])
                if not rm: err(f"{c['id']}: note column must name reviewer=<family:model> for a proved claim")
                elif rm.group(1).strip() == c["author"].strip(): err(f"{c['id']}: reviewer equals author")
            if c["author"].split(":")[0] == "" or c["author"] == "-": err(f"{c['id']}: author required")
        if c["status"] == "cited":
            pr = next((p for p in prov if p["id"] == c["proof"]), None)
            if pr is None: err(f"{c['id']}: cited claims put a provenance id in the proof column")
            elif c["id"] in env_text and norm_ws(pr["quote"]) not in norm_ws(env_text[c["id"]]):
                err(f"{c['id']}: the citedfact environment must reproduce the provenance quote {pr['id']} verbatim (e.g. inside \\texttt{{\\detokenize{{...}}}})")
    # definitions parity
    terms = {}
    for d in defs:
        if d["status"] not in DEF_STATUSES: err(f"{d['id']}: bad status {d['status']}")
        if not d["id"].startswith("def:"): err(f"definitions: id {d['id']} must start with def:")
        t = d["term"].lower()
        if t in terms: err(f"definitions: duplicate term '{d['term']}' ({terms[t]} and {d['id']})")
        terms[t] = d["id"]
        if d["id"] not in envs_seen: err(f"definition {d['id']} has no environment in any shard")
        elif envs_seen[d["id"]][1] != d["shard"]: err(f"{d['id']}: db shard {d['shard']} != {envs_seen[d['id']][1]}")
        if d["status"] == "quoted" and not any(p["id"] == d["provenance"] for p in prov): err(f"{d['id']}: quoted definition needs a provenance id")
    for lab, (env, rel) in envs_seen.items():
        if env == "definition" and lab not in {d["id"] for d in defs}: err(f"{rel}: {lab} has no row in db/definitions.tsv")
    # notation parity
    want = gen_macros(notation)
    have = read("report/macros.tex")
    if have != want: err("report/macros.tex is stale or hand-edited; run: python3 scripts/labbook_check.py --regen")
    seen_m, seen_l = {}, {}
    for r in notation:
        if r["macro"] in seen_m: err(f"notation: duplicate macro \\{r['macro']}")
        if r["latex"] in seen_l: err(f"notation: symbol {r['latex']} defined twice (\\{seen_l[r['latex']]} and \\{r['macro']}); dedup")
        seen_m[r["macro"]] = 1; seen_l[r["latex"]] = r["macro"]
        if not re.match(r"^[A-Za-z]+$", r["macro"]): err(f"notation: macro name {r['macro']} must be letters only")
        if r["macro"] in LATEX_RESERVED: err(f"notation: macro name \\{r['macro']} is a LaTeX/amsmath control sequence; rename")
        if r["macro"] not in macros_used: warn(f"notation: \\{r['macro']} is never used in a shard")
    reserved = {r["latex"]: r["macro"] for r in notation if re.fullmatch(r"\\[A-Za-z]+", r["latex"])}
    for f in files_on_disk:
        raw_lines = read(f"report/sections/{f}").splitlines()
        body = mask_detokenize(strip_comments("\n".join("" if l.rstrip().endswith("% bare-ok") else l for l in raw_lines)))
        for cs, mac in reserved.items():
            for mm in re.finditer(re.escape(cs) + r"(?![A-Za-z])", body):
                warn(f"report/sections/{f}: bare {cs} at offset {mm.start()}; use \\{mac} (db/notation.tsv)")
    preamble_macros = set(re.findall(r"\\(?:re)?newcommand\{\\([A-Za-z]+)\}", strip_comments(master))) | {"claimstatus"}
    # macros that appear in shards and look like ours (start with capital? no: check against DB + preamble + a LaTeX whitelist)
    user_like = {m for m in macros_used if m in seen_m or m in preamble_macros}
    defined = set(seen_m) | preamble_macros
    # detect undefined project macros: any \Word where Word is in notation 'macro' style but not defined -> only catch via build log; here check regen consistency
    st_want = gen_status(claims, eff, cond)
    if read("report/generated/status.tex") != st_want: err("report/generated/status.tex is stale; run --regen")
    if read("report/generated/notation_table.tex") != gen_notation_table(notation): err("report/generated/notation_table.tex is stale; run --regen")
    # provenance
    pids = set()
    for p in prov:
        if p["id"] in pids: err(f"provenance: duplicate id {p['id']}")
        pids.add(p["id"])
        src = read(f"refs/src/{p['key']}/{p['file']}")
        if src is None:
            err(f"{p['id']}: refs/src/{p['key']}/{p['file']} not present (run refs/fetch_sources.sh)"); continue
        try:
            a, b = (p["lines"].split("-") + [None])[:2]; a = int(a); b = int(b) if b else a
        except ValueError:
            err(f"{p['id']}: bad line window {p['lines']}"); continue
        window = norm_ws(" ".join(src.splitlines()[a - 1:b]))
        if norm_ws(p["quote"]) not in window:
            err(f"{p['id']}: quote not found whole and contiguous in {p['key']}:{p['file']}:{p['lines']}")
    for c in claims:
        if c["status"] == "cited" and c["proof"] not in pids: err(f"{c['id']}: provenance {c['proof']} unknown")
    bib = read("report/references.bib") or ""
    bibkeys = set(re.findall(r"@\w+\{([^,]+),", bib))
    for k in sorted(cites - bibkeys): err(f"\\cite{{{k}}} has no entry in report/references.bib")
    for k in sorted(bibkeys):
        m = re.search(r"@\w+\{" + re.escape(k) + r",(.*?)\n\}", bib, re.S)
        body = m.group(1) if m else ""
        am = re.search(r"eprint\s*=\s*\{([^}]+)\}", body)
        if am and not os.path.isdir(os.path.join(ROOT, "refs/src", am.group(1))): warn(f"bib {k}: arXiv {am.group(1)} has no refs/src directory")
        if not am and "note" not in body: warn(f"bib {k}: no eprint and no note = {{no local source}}")
    return eff, cond

def build():
    env = dict(os.environ, TEXINPUTS=ROOT + "//:")
    for cmd in (["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "report.tex"],
                ["bibtex", "report"],
                ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "report.tex"],
                ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "report.tex"]):
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=600, env=env)
        if r.returncode != 0 and cmd[0] != "bibtex":
            err(f"build: {' '.join(cmd)} failed; see report.log"); return
        if cmd[0] == "bibtex" and r.returncode != 0 and "I found no" in r.stdout:
            pass
    log = read("report.log") or ""
    for pat, msg in ((r"Warning: (Reference|Citation) `[^']+' on page", "undefined reference/citation"),
                     (r"multiply defined", "multiply-defined label"),
                     (r"There were undefined references", "undefined references")):
        if re.search(pat, log): err(f"build: {msg} (see report.log)")

def shard_headers():
    out = []
    for f in sorted(x for x in os.listdir(os.path.join(ROOT, "report/sections")) if x.endswith(".tex")):
        raw = read(f"report/sections/{f}")
        h = lambda k: [x.strip() for x in re.findall(rf"^% SHARD-{k}:\s*(.+)$", raw, re.M)]
        out.append(dict(file=f"report/sections/{f}", id=(h("ID") or ["?"])[0], title=(h("TITLE") or ["?"])[0],
                        summaries=h("SUMMARY"), keywords=(h("KEYWORDS") or ["?"])[0], notes=(h("NOTES") or ["?"])[0], scripts=(h("SCRIPTS") or ["?"])[0]))
    return out

def gen_readme(hs):
    out = ["# Report Source Map", "",
           "GENERATED by `scripts/labbook_check.py --regen` from the `% SHARD-*` headers of `report/sections/*.tex`; do not edit.",
           "The compiled lab book is rooted at `report.tex` (preamble and include order only). Body prose lives in the shards below,",
           "notation in `db/notation.tsv` (rendered to `report/macros.tex`), definitions in `db/definitions.tsv`, claims in `db/claims.tsv`,",
           "quotes in `db/provenance.tsv`. `make check` is the gate, `make ci` the local CI (gate + fresh build + output diff), `make hooks` installs it as a pre-commit hook.",
           "", "## Shard order", "", "| Order | Label | Source | Title | Notes distilled | Scripts evidenced |", "|---:|---|---|---|---|---|"]
    for i, h in enumerate(hs):
        out.append(f"| {i} | `{h['id']}` | `{h['file']}` | {h['title']} | {h['notes']} | {h['scripts']} |")
    return "\n".join(out) + "\n"

def gen_catalog(hs):
    out = ["# Report Shard Catalog", "", "GENERATED by `scripts/labbook_check.py --regen`; do not edit. Stable labels, summaries and search keywords, mirrored from the shard headers.", ""]
    for h in hs:
        out += [f"## `{h['id']}`", "", f"- Source: `{h['file']}`", f"- Title: {h['title']}"]
        out += [f"- Summary: {x}" for x in h["summaries"]]
        out += [f"- Keywords: {h['keywords']}", f"- Notes: {h['notes']}", f"- Scripts: {h['scripts']}", ""]
    return "\n".join(out)

def main():
    argv = sys.argv[1:]
    notation, defs, claims, prov = load_dbs()
    if "--regen" in argv:
        eff, cond = derive(claims)
        os.makedirs(os.path.join(ROOT, "report/generated"), exist_ok=True)
        open(os.path.join(ROOT, "report/macros.tex"), "w").write(gen_macros(notation))
        open(os.path.join(ROOT, "report/generated/status.tex"), "w").write(gen_status(claims, eff, cond))
        open(os.path.join(ROOT, "report/generated/notation_table.tex"), "w").write(gen_notation_table(notation))
        hs = shard_headers()
        open(os.path.join(ROOT, "report/README.md"), "w").write(gen_readme(hs))
        open(os.path.join(ROOT, "report/SHARD_CATALOG.md"), "w").write(gen_catalog(hs))
        print("regenerated report/macros.tex, report/generated/{status,notation_table}.tex, report/README.md, report/SHARD_CATALOG.md")
        return 0
    if os.path.isdir(os.path.join(ROOT, "report/sections")):
        res = check_shards(notation, defs, claims, prov)
    else:
        err("report/sections missing"); res = None
    if "--build" in argv and not errors:
        build()
    quiet = "--quiet" in argv
    for w in warns: print("WARN", w)
    for e in errors: print("ERROR", e)
    if not quiet:
        eff = res[0] if res else {}
        print(f"labbook check: {len(claims)} claims, {len(defs)} definitions, {len(notation)} notation rows, {len(prov)} provenance rows; "
              f"{sum(1 for v in eff.values() if v.startswith('proved'))} proved; {len(errors)} errors, {len(warns)} warnings")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
