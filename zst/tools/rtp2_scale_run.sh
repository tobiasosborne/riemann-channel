#!/usr/bin/env bash
# RTP-2 lane S; author codex:gpt-6-astra. Regenerate the certified outputs.
# Optional first argument: output directory (e.g. lane checks/reproduce).
# Thread caps add to 64. Timings are kept separately in the lane's checks.
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
root="$(cd "$here/.." && pwd)"
checks="$root/notes/rtp-round-2/scale/checks"
out="${1:-$root/outputs}"
work="${2:-$checks/regenerated}"
mkdir -p "$out" "$work"
make -C "$here" build/rtp2_scale >/dev/null
cc -O2 -std=c11 -fopenmp -I"$here/include" "$checks/first_comparison.c" "$here/build/libzst.a" -lflint -lmpfr -lgmp -lm -o "$checks/first_comparison"
cc -O2 "$checks/derived.c" -lflint -lmpfr -lgmp -o "$checks/derived"
cc -O2 "$checks/overlap.c" -lflint -lmpfr -lgmp -o "$checks/overlap"
"$here/build/rtp2_scale" --selftest > "$work/selftest.txt" 2> "$work/selftest.stderr.txt"
run() {
 local x="$1" start="$2" end="$3" prec="$4" threads="$5" fast="$6"
 "$here/build/rtp2_scale" --x "$x" --start "$start" --end "$end" --prec "$prec" --threads "$threads" --fast "$fast" --compare 0 --vector "$work/vector_x$x.arb" > "$out/rtp2_scale_x$x.txt" 2> "$work/x$x.stderr.txt"
 # An exhausted sweep is not convergence. The completion helper checks matching final N and even-simplicity.
 "$checks/first_comparison" "$work/vector_x$x.arb" "$out/rtp2_scale_x$x.txt" > "$out/rtp2_scale_comparison_x$x.txt" 2> "$work/comparison_x$x.stderr.txt"
}
run 13 200 1000 1000 4 0 & p13=$!
run 25 260 1100 1800 4 0 & p25=$!
run 50 420 1420 4200 4 0 & p50=$!
run 60 418 1538 5200 4 0 & p60=$!
run 70 506 1146 4600 16 1 & p70=$!
run 85 642 1122 5500 32 1 & p85=$!
for pid in "$p13" "$p25" "$p50" "$p60" "$p70" "$p85"; do wait "$pid"; done
"$checks/overlap" "$work/vector_x13.arb" "$work/vector_x25.arb" "$work/vector_x50.arb" "$work/vector_x60.arb" "$work/vector_x70.arb" "$work/vector_x85.arb" > "$out/rtp2_scale_overlaps.txt"
python3 "$checks/analyse.py" "$out" "$work"
make -C "$here" check > "$work/make-check.txt" 2>&1
