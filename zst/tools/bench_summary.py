#!/usr/bin/env python3
"""Summarise tools/bench.sh outputs: python3 tools/bench_summary.py OUTDIR
Per run: x, N, prec, eps_N, stage times, the certified error of the first zero, and the largest k
whose certified error is below 1e-50, 1e-30, 1e-20, 1e-10, 1e-3 (errors are upper bounds)."""
import glob, os, re, sys

def parse(path):
    t = open(path).read()
    m = re.search(r"x = ([\d.]+) .*N = (\d+), prec = (\d+)", t)
    if not m: return None
    r = {"x": float(m.group(1)), "N": int(m.group(2)), "prec": int(m.group(3)), "file": os.path.basename(path)}
    g = lambda pat, cast=float: (cast(re.search(pat, t).group(1)) if re.search(pat, t) else None)
    r["t_build"] = g(r"matrix build: ([\d.]+)s")
    r["eps"] = (re.search(r"eps_N = \[([^\s\]]+)", t) or [None, None])[1]
    r["t_eig"] = g(r"certified, ([\d.]+)s")
    r["even_simple"] = "CERTIFIED" in (re.search(r"even-simple hypothesis: (\S+)", t) or [None, ""])[1]
    r["t_inertia"] = g(r"(?:\[-1 = inconclusive\]|not certified|CERTIFIED)  \(([\d.]+)s\)")
    mm = re.search(r"positive secular roots: (\d+) certified of N = (\d+), (\d+) unresolved  ->  spectrum (\S+)  \(([\d.]+)s\)", t)
    if mm:
        r["roots"], r["unres"], r["complete"], r["t_roots"] = int(mm.group(1)), int(mm.group(3)), mm.group(4) == "COMPLETE", float(mm.group(5))
    r["t_total"] = g(r"total ([\d.]+)s")
    r["wall"] = g(r"wall ([\d.]+) s")
    r["rss_mb"] = g(r"maxrss (\d+) KB", lambda v: int(v) / 1024)
    errs = []
    for line in t.splitlines():
        mm = re.match(r"\s*(\d+)\s+[\d.]+\s+([\d.]+e[-+]?\d+|[\d.]+)\s*$", line)
        if mm: errs.append((int(mm.group(1)), float(mm.group(2))))
    r["err1"] = errs[0][1] if errs else None
    for thr, key in [(1e-50, "k50"), (1e-30, "k30"), (1e-20, "k20"), (1e-10, "k10"), (1e-3, "k3")]:
        ks = [k for k, e in errs if e < thr]
        r[key] = max(ks) if ks else 0
    r["nerr"] = len(errs)
    return r

def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "bench"
    rows = [parse(p) for p in sorted(glob.glob(os.path.join(out, "x*_N*_p*.txt")))]
    rows = [r for r in rows if r]
    rows.sort(key=lambda r: (r["x"], r["N"]))
    hdr = f"{'x':>5} {'N':>5} {'prec':>5} {'eps_N':>14} {'err(z1)':>10} {'k<1e-50':>7} {'k<1e-30':>7} {'k<1e-20':>7} {'k<1e-10':>7} {'k<1e-3':>6} {'roots':>7} {'ok':>3} {'build':>6} {'eig':>7} {'inert':>7} {'roots':>7} {'wall':>8} {'MB':>6}"
    print(hdr)
    for r in rows:
        print(f"{r['x']:>5g} {r['N']:>5} {r['prec']:>5} {str(r['eps']):>14} {r['err1'] if r['err1'] is not None else float('nan'):>10.2e} "
              f"{r['k50']:>7} {r['k30']:>7} {r['k20']:>7} {r['k10']:>7} {r['k3']:>6} {r.get('roots','?'):>7} "
              f"{'Y' if r.get('even_simple') and r.get('complete') else 'n':>3} {r['t_build'] or 0:>6.1f} {r['t_eig'] or 0:>7.1f} "
              f"{r['t_inertia'] or 0:>7.1f} {r.get('t_roots') or 0:>7.1f} {r['wall'] or 0:>8.1f} {r['rss_mb'] or 0:>6.0f}")

if __name__ == "__main__":
    main()
