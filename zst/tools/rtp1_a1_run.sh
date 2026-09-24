#!/usr/bin/env bash
# RTP round 1, lane A1 (author claude:opus): regenerate outputs/rtp1_a1_*.txt with zst/tools/rtp1_a1.c.
#   zst/tools/rtp1_a1_run.sh            write the six outputs (runs up to four jobs in parallel)
#   zst/tools/rtp1_a1_run.sh DIR        write them into DIR instead (for byte-identity checks: cmp against outputs/)
# Single-thread wall time of the six runs, this container (FLINT 3.0.1): about 14 minutes in total.
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
out="${1:-$here/../outputs}"
mkdir -p "$out"
make -C "$here" build/rtp1_a1 >/dev/null
bin="$here/build/rtp1_a1"
run() { local name="$1"; shift; "$bin" "$@" > "$out/rtp1_a1_$name.txt" 2> /dev/null; }
# axis N (A1.2), with the certified eps_N and the labelled comparison (A1.4) at the listed N
run axisN_x50 --mode axisN --x 50 --Nmax 520 --prec 4200 --cmp 50,100,200,300,360 --cprec 2400 &
run axisN_x25 --mode axisN --x 25 --Nmax 260 --prec 1800 --cmp 25,50,100,150,190,260 --cprec 1200 &
run axisN_x13 --mode axisN --x 13 --Nmax 200 --prec 1000 --cmp 10,20,40,60,80,100,120,160,200 --cprec 700 &
wait -n
# axis x (A1.3): CCM protocol at N = 60 (to x = 50) and N = 120 (to x = 25); fixed-window protocol at N = 60
run axisx_ccm_N60 --mode axisx --N 60 --xmax 50 --prec 2700 &
wait -n
run axisx_ccm_N120 --mode axisx --N 120 --xmax 25 --prec 1800 &
wait -n
run axisx_fixedL_N60 --mode axisx --N 60 --xmax 50 --prec 2700 --fixedL 1 &
wait
grep -H "checks:" "$out"/rtp1_a1_*.txt
