#!/usr/bin/env bash
# Fetch arXiv TeX sources for every reference in notes/prior-art-quantum-ihara.md into refs/src/<id>/
# (gitignored) and record sha256 hashes in refs/manifest.sha256. Quotes in notes/ cite
# <id>:<file>:<line> against these files. Preference (TJO, 2026-09-12): TeX source, not PDF.
set -eu
cd "$(dirname "$0")"
IDS="2204.06424 2208.14032 2607.27935 1103.0605 1801.00876 2012.08759 2304.05714 2602.15180 0709.1142 0706.0556 2309.15873 2105.02677 1103.0079 2209.07024 2104.10287 2405.04361 1306.4203 1403.0256 math/0407288 math/0402356 1511.04265 1606.04560 1607.08053 1108.5659 1710.00603 math/9811068 2006.13771 1608.03679 math-ph/0505052 math/0404394 math/0506326 1905.13485 1403.0079 2009.02802 2206.03682 1707.02266"
mkdir -p src; : > manifest.sha256
for id in $IDS; do
  d=src/$id; mkdir -p "$d"
  [ -f "$d/src.tar" ] || timeout 120 curl -sSL -o "$d/src.tar" "https://arxiv.org/e-print/$id"
  ( cd "$d" && ( tar xf src.tar 2>/dev/null || gunzip -c src.tar > main.tex ) )
  find "$d" -type f \( -name '*.tex' -o -name '*.bbl' -o -name 'lambda2.txt' \) | LC_ALL=C sort | while read -r f; do sha256sum "$f"; done >> manifest.sha256
  echo "$id: $(find "$d" -name '*.tex' | wc -l) tex files"
done
