#!/usr/bin/env bash
# Fetch arXiv TeX sources for every reference in notes/prior-art-quantum-ihara.md,
# notes/extract/weil-positivity-sources.md, notes/extract/riemann-cmps-sources.md,
# notes/extract/selberg-sources.md, notes/extract/complex-zeta-sources.md and
# notes/ring-norm-tensor/sources.md into refs/src/<id>/
# (gitignored) and record sha256 hashes in refs/manifest.sha256. Quotes in notes/ cite
# <id>:<file>:<line> against these files. Preference (TJO, 2026-09-12): TeX source, not PDF.
set -eu
cd "$(dirname "$0")"
IDS="0706.0556 0706.1509 0709.1142 0709.2801 0804.2305 0809.1401 0809.1401v1 0809.3479 0809.3481 0810.1855 0903.2156 1002.1824 1007.4899 1009.0228 1103.0079 1103.0605 1105.2914 1108.5659 1109.3854 1208.5370 1211.3935 1303.4792 1303.6847 1303.6848 1306.4203 1307.3851 1402.4759 1403.0079 1403.0256 1412.3327 1505.00902 1507.01194 1509.00797 1511.04265 1602.00664 1605.02664 1606.04560 1606.07317 1607.08053 1608.03679 1610.07849 1701.00154 1701.07742 1702.05452 1706.00851 1707.02266 1709.06052 1710.00603 1712.02526 1801.00876 1804.08028 1807.01189 1807.06400 1905.13485 2002.12099 2003.05380 2006.00637 2006.13771 2009.02802 2009.08558 2012.08759 2104.00215 2104.10287 2105.02677 2201.09412 2204.06424 2204.13586 2205.02094 2206.03682 2208.06138 2208.14032 2209.07024 2303.11226 2304.05714 2307.03321 2309.15873 2310.15619 2405.04361 2405.14395 2411.15489 2501.08803 2503.19641 2510.27134 2512.23276 2602.15180 2605.07626 2607.21262 2607.27935 2609.12284 2609.13121 cond-mat/0403271 dg-ga/9511006 math-ph/0505052 math/0306396 math/0402356 math/0404128 math/0404394 math/0406208 math/0406217 math/0407288 math/0407509 math/0505354 math/0506326 math/0608761 math/0610644 math/0610818 math/9806037 math/9811068 quant-ph/0412001 quant-ph/0602001"
mkdir -p src; : > manifest.sha256
for id in $IDS; do
  d=src/$id; mkdir -p "$d"
  [ -f "$d/src.tar" ] || timeout 120 curl -sSL -o "$d/src.tar" "https://arxiv.org/e-print/$id"
  ( cd "$d" && ( tar xf src.tar 2>/dev/null || gunzip -c src.tar > main.tex ) )
  find "$d" -type f \( -name '*.tex' -o -name '*.bbl' -o -name 'lambda2.txt' \) | LC_ALL=C sort | while read -r f; do sha256sum "$f"; done >> manifest.sha256
  echo "$id: $(find "$d" -name '*.tex' | wc -l) tex files"
done
