#!/usr/bin/env bash
# Impromptu benchmark: run the pipeline over a grid of (x, N, prec) and keep every output.
# Usage: tools/bench.sh OUTDIR [x:N:prec ...]    (defaults below); summarise with tools/bench_summary.py OUTDIR
set -u
OUT="${1:-bench}"; shift || true
mkdir -p "$OUT"
GRID=("$@")
if [ ${#GRID[@]} -eq 0 ]; then
  GRID=(13:120:700 13:240:800 20:200:900 30:300:1300 40:400:1700 50:500:2100)
fi
for g in "${GRID[@]}"; do
  IFS=: read -r x N prec <<< "$g"
  f="$OUT/x${x}_N${N}_p${prec}.txt"
  echo "== $(date +%H:%M:%S) x=$x N=$N prec=$prec -> $f"
  t0=$(date +%s.%N)
  "${BIN:-./build/zst}" --x "$x" --N "$N" --prec "$prec" --zeros "$N" > "$f" 2>&1
  t1=$(date +%s.%N)
  echo "wall $(echo "$t1 - $t0" | bc) s  maxrss $(grep -m1 VmHWM /proc/self/status 2>/dev/null | awk '{print $2}' || echo 0) KB" >> "$f"
  tail -2 "$f" | head -1
done
