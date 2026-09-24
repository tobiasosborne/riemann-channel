#!/usr/bin/env python3
"""RTP round 1, lane A1 (author claude:opus): derived numbers for notes/rtp-round-1/lane-A1.md from
outputs/rtp1_a1_*.txt. Pure post-processing of the certified tables (midpoints of certified balls, so the
derived numbers are floating point); deterministic, no timestamps.
    python3 zst/tools/rtp1_a1_summary.py [outputs_dir]
"""
import math
import os
import re
import sys

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "..", "outputs")


def num(s):
    """midpoint of a printed ball or number ('1.23e-5' or '[1.2 +/- 3e-4]')"""
    s = s.strip()
    m = re.match(r"\[([-+0-9.e]+) \+/- ", s)
    if m:
        return float(m.group(1))
    if s.startswith("[+/-"):
        return 0.0
    return float(s)


def log10(s):
    """log10 of a positive printed number, robust to exponents below the double range"""
    m = re.match(r"\[?([0-9.]+)e([-+]?[0-9]+)", s.strip())
    if m:
        return math.log10(float(m.group(1))) + int(m.group(2))
    return math.log10(float(s))


def axisN(path):
    rows, cmp_rows, x = [], [], None
    in_cmp = False
    for line in open(path):
        if line.startswith("# fixed: x = lambda^2 ="):
            x = float(line.split("=")[2].split(",")[0])
        if line.startswith("# certified minimal eigenvalue"):
            in_cmp = True
        if line.startswith("#") or not line.strip():
            if line.startswith("# Rayleigh"):
                in_cmp = False
            continue
        f = line.split()
        if not f[0].isdigit():
            continue
        if in_cmp:
            cmp_rows.append((int(f[0]), f[1], f[4]))
        elif len(f) == 12:
            rows.append(dict(N=int(f[0]), dI=num(f[3]), logdet=num(f[5]), rj=f[8], tau=num(f[9])))
    return x, rows, cmp_rows


def main():
    print("# rtp1_a1_summary: derived numbers (floating point, from certified midpoints)")
    print("#\n# axis N: saturation of Delta I_N")
    print("#   N_ld  = argmin_N log det (window matrix |n| <= N)")
    print("#   N_1   = smallest N from which the 10-row moving average of Delta I stays below 1 nat")
    print("#   <dI>  = mean Delta I over the last 100 rows;  tau_pre = mean |tau_j| for N < N_ld, tau_post for N > N_1")
    print("%4s %6s %6s %7s %8s %12s %8s %11s %8s %9s %10s" % ("x", "N_ld", "N_1", "7.5x", "N_ld/x", "N_ld/(xlogx)",
          "N_1/x", "N_1/(xlogx)", "<dI>", "tau_pre", "tau_post"))
    cmp_all = []
    for x in (13, 25, 50):
        p = os.path.join(OUT, "rtp1_a1_axisN_x%d.txt" % x)
        if not os.path.exists(p):
            continue
        x, rows, cmp_rows = axisN(p)
        nld = min(rows, key=lambda r: r["logdet"])["N"]
        # moving average over 10 consecutive borderings
        ma = [sum(r["dI"] for r in rows[i:i + 10]) / 10 for i in range(len(rows) - 9)]
        n1 = None
        for i in range(len(ma)):
            if all(m < 1 for m in ma[i:]):
                n1 = rows[i]["N"]
                break
        tail = rows[-100:]
        mdi = sum(r["dI"] for r in tail) / len(tail)
        pre = [abs(r["tau"]) for r in rows if r["N"] < nld]
        post = [abs(r["tau"]) for r in rows if n1 is not None and r["N"] > n1]
        print("%4g %6d %6s %7.1f %8.2f %12.2f %8.2f %11.2f %8.3f %9.4f %10.3f" % (
            x, nld, n1, 7.5 * x, nld / x, nld / (x * math.log(x)), n1 / x, n1 / (x * math.log(x)), mdi,
            sum(pre) / len(pre), sum(post) / len(post) if post else float("nan")))
        cmp_all.append((x, cmp_rows))
    print("#\n# axis N: certified eps_N and the labelled comparison |z1 - g1| (ratio err/eps)")
    print("%4s %5s %14s %12s %10s" % ("x", "N", "eps_N", "|z1-g1|<=", "err/eps"))
    for x, cr in cmp_all:
        for N, e, z in cr:
            print("%4g %5d %14s %12s %10.3g" % (x, N, e, z, 10 ** (log10(z) - log10(e))))
    print("#\n# axis x (CCM protocol): slopes d log10(.)/dx between knots (4 pi / ln 10 = %.3f)" % (4 * math.pi / math.log(10)))
    for N in (60, 120):
        p = os.path.join(OUT, "rtp1_a1_axisx_ccm_N%d.txt" % N)
        if not os.path.exists(p):
            continue
        knots, errs = [], {}
        sect = "main"
        for line in open(p):
            if line.startswith("# CONTROL"):
                sect = "control"
            if line.startswith("# COMPARISON"):
                sect = "cmp"
            if line.startswith("#") or not line.strip():
                continue
            f = line.split()
            try:
                xv = float(f[0])
            except ValueError:
                continue
            if sect == "main" and len(f) >= 9:
                knots.append((xv, f[3], 1 - num(f[7])))
            if sect == "cmp" and len(f) == 4 and f[3] != "-":
                errs[xv] = f[3]
        print("# N = %d" % N)
        print("%6s %8s %12s %12s %12s" % ("x", "#", "slope eps", "slope err", "1-overlap_c"))
        prev = None
        for xv, e, ov in knots:
            if prev is not None and xv >= 5:
                se = (log10(e) - log10(prev[1])) / (xv - prev[0])
                sz = (log10(errs[xv]) - log10(errs[prev[0]])) / (xv - prev[0])
                print("%6g %8s %12.3f %12.3f %12.3g" % (xv, "", se, sz, ov))
            prev = (xv, e)


if __name__ == "__main__":
    main()
