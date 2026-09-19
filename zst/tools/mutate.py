#!/usr/bin/env python3
"""Mutation testing for zst (stdlib only). Run from zst/:  python3 tools/mutate.py [--max K] [--seed S]

Generates single-point mutants of src/*.c (arithmetic operator swaps, comparison flips, off-by-one
constants, dropped negations and sign flips in arb calls), rebuilds, runs `make check` with a timeout,
and reports killed / survived / timed-out mutants. A surviving mutant is a test-suite gap: it is
listed with the diff so the next red test can target it. Sources are restored after every mutant.
"""
import argparse, os, random, re, shutil, subprocess, sys, tempfile, time

MUTATIONS = [
    (r"arb_add\(", "arb_sub("), (r"arb_sub\(", "arb_add("),
    (r"arb_mul\(", "arb_div("), (r"arb_div\(", "arb_mul("),
    (r"arb_addmul\(", "arb_submul("), (r"arb_submul\(", "arb_addmul("),
    (r"acb_add\(", "acb_sub("), (r"acb_div\(", "acb_mul("),
    (r"arb_neg\(([^;]*)\);", r"arb_set(\1);"),
    (r"arb_mul_2exp_si\(([^,]+), ([^,]+), -1\)", r"arb_mul_2exp_si(\1, \2, -2)"),
    (r"arb_mul_2exp_si\(([^,]+), ([^,]+), 1\)", r"arb_mul_2exp_si(\1, \2, 2)"),
    (r"arb_mul_2exp_si\(([^,]+), ([^,]+), -2\)", r"arb_mul_2exp_si(\1, \2, -1)"),
    (r"\b(\w+) \+ 1\b", r"\1"), (r"\b(\w+) - 1\b", r"\1"),
    (r" < ", " <= "), (r" <= ", " < "), (r" > ", " >= "), (r" >= ", " > "),
    (r"\+= 8", "+= 4"), (r"k \* 2", "k * 3"),
    (r"arb_sqr\(", "arb_set(arb_t_dummy,"),  # deliberately uncompilable in most contexts: skipped
    (r"i \* i", "i * j"), (r"-2 \* i \* j", "-2 * i * i"),
    (r"arb_const_pi\(", "arb_const_e("), (r"arb_const_euler\(", "arb_const_log2("),
]

def candidates(path):
    lines = open(path).read().split("\n")
    out = []
    for ln, line in enumerate(lines):
        if line.strip().startswith(("/*", "*", "//")) or "getenv" in line or "printf" in line:
            continue
        for pat, rep in MUTATIONS:
            for m in re.finditer(pat, line):
                new = line[:m.start()] + re.sub(pat, rep, line[m.start():m.end()]) + line[m.end():]
                if new != line:
                    out.append((path, ln, line, new))
    return out

def run(cmd, timeout):
    try:
        r = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout)
        return r.returncode, r.stdout.decode(errors="replace")
    except subprocess.TimeoutExpired:
        return None, "timeout"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=40)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--timeout", type=int, default=120)
    ap.add_argument("--files", default="src/riemann_ab.c,src/blocks.c,src/eigmin.c,src/secular.c")
    args = ap.parse_args()
    files = args.files.split(",")
    # tests are built with AddressSanitizer so that memory-safety mutants (over-reads, leaks of
    # behaviourally invisible slots) are killed too
    asan = 'CFLAGS="-O1 -g -fsanitize=address -std=c11 -Wall -Iinclude" LDLIBS="-fsanitize=address -lflint -lmpfr -lgmp -lm"'
    build = f"make -s clean >/dev/null 2>&1; make -s {asan} all >/dev/null 2>&1 && make -s {asan} check"
    rc, out = run(build, args.timeout)
    if rc != 0:
        print("baseline `make check` (ASan build) fails; fix that first\n" + out); sys.exit(2)
    pool = []
    for f in files: pool += candidates(f)
    random.Random(args.seed).shuffle(pool)
    pool = pool[:args.max]
    killed = survived = nocompile = timed = 0
    survivors = []
    for (path, ln, old, new) in pool:
        src = open(path).read().split("\n")
        backup = list(src)
        src[ln] = new
        open(path, "w").write("\n".join(src))
        t0 = time.time()
        rc, out = run(build, args.timeout)
        open(path, "w").write("\n".join(backup))
        os.utime(path, None)
        tag = f"{path}:{ln+1}"
        if rc is None:
            timed += 1; print(f"TIMEOUT  {tag}")
        elif "error" in out and "FAIL" not in out and "PASS" not in out:
            nocompile += 1; print(f"NOCOMPILE {tag}")
        elif rc != 0:
            killed += 1; print(f"killed   {tag}  ({time.time()-t0:.1f}s)")
        else:
            survived += 1; survivors.append((tag, old.strip(), new.strip())); print(f"SURVIVED {tag}")
    run("make -s clean >/dev/null 2>&1; make -s all >/dev/null 2>&1 && make -s check >/dev/null 2>&1", args.timeout)
    print(f"\nmutants: {len(pool)}  killed: {killed}  survived: {survived}  timeout: {timed}  nocompile: {nocompile}")
    for tag, old, new in survivors:
        print(f"  {tag}\n    - {old}\n    + {new}")
    sys.exit(1 if survived else 0)

if __name__ == "__main__":
    main()
