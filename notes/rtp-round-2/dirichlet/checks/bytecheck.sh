#!/usr/bin/env bash
# Author codex:gpt-6-astra. Three representative complete driver outputs, run twice.
set -euo pipefail
cd "$(dirname "$0")/../../../.."
checkdir=notes/rtp-round-2/dirichlet/checks
for spec in '-4 13 40 1000 700' '12 25 40 1800 1400' '-20 13 3 1000 700'; do
    read -r D x N p cp <<< "$spec"
    for pass in a b; do
        zst/build/rtp2_dirichlet --D "$D" --mode axisN --x "$x" --Nmax "$N" --prec "$p" --cprec "$cp" > "$checkdir/byte_D${D}_${pass}.txt" 2> "$checkdir/byte_D${D}_${pass}.log"
    done
    cmp "$checkdir/byte_D${D}_a.txt" "$checkdir/byte_D${D}_b.txt"
    echo "byte-identical D=$D x=$x N=$N"
done
