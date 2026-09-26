#!/usr/bin/env bash
# Author codex:gpt-6-astra. Pilot, diagnostic and independent precision reruns.
set -euo pipefail
root="$(cd "$(dirname "$0")/../../../.." && pwd)"
cd "$root"
make -C zst build/rtp2_ellcurve
bin="$root/zst/build/rtp2_ellcurve"
ck="$root/notes/rtp-round-2/ellcurve/checks"
"$bin" --curve 11a1 --x 13 --Nmax 60 --prec 1000 --cprec 700 --cmp 20,40,60 > "$ck/pilot_repeat.txt" 2> "$ck/pilot_repeat.log"
cmp outputs/rtp2_ellcurve_pilot_11a1.txt "$ck/pilot_repeat.txt"
"$bin" --curve 11a1 --x 2 --Nmax 200 --prec 1000 --cprec 700 > outputs/rtp2_ellcurve_diagnostic_x2_N200.txt 2> "$ck/diagnostic_x2.log" &
for spec in '11a1 13 60 1600' '14a1 25 60 1600' '37a1 50 60 1600' '11a1 100 200 2000'; do
    read -r curve x n p <<< "$spec"
    "$bin" --curve "$curve" --mode point --N "$n" --xmax "$x" --prec "$p" --control-cap 1 > "$ck/recheck_${curve}_x${x}_N${n}.txt" 2> "$ck/recheck_${curve}_x${x}_N${n}.log" &
done
wait
python3 "$ck/independent_ab.py" > "$ck/independent_ab.txt"
python3 "$ck/audit.py" > "$ck/audit.txt"
