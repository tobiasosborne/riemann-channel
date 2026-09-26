#!/usr/bin/env bash
# Emit one line per state change of RTP round 2: new lane.log lines (attempt/exit/DONE/FAILED/adopt), progress.txt
# changes, STOP, new quota readings. Polls every 60 s; never exits on its own.
cd "$(dirname "$0")/.."; R=notes/rtp-round-2
declare -A LL PR; Q=$(wc -l < $R/quota.log 2>/dev/null || echo 0)
for d in dirichlet lattice-box impure-bumps prover; do LL[$d]=$(wc -l < $R/$d/lane.log 2>/dev/null || echo 0); PR[$d]=$(md5sum < $R/$d/progress.txt 2>/dev/null); done
while true; do
  [ -f $R/STOP ] && { echo "STOP: $(cat $R/STOP | head -1)"; sleep 3600; }
  for d in dirichlet lattice-box impure-bumps prover; do
    n=$(wc -l < $R/$d/lane.log 2>/dev/null || echo 0)
    [ "$n" -gt "${LL[$d]}" ] && { tail -n $((n-LL[$d])) $R/$d/lane.log | sed "s|^|$d lane.log: |"; LL[$d]=$n; }
    h=$(md5sum < $R/$d/progress.txt 2>/dev/null); [ "$h" != "${PR[$d]}" ] && { echo "$d progress: $(tr '\n' ' ' < $R/$d/progress.txt | cut -c1-300)"; PR[$d]=$h; }
  done
  q=$(wc -l < $R/quota.log 2>/dev/null || echo 0); [ "$q" -gt "$Q" ] && { tail -1 $R/quota.log | sed 's|^|quota: |'; Q=$q; }
  sleep 60
done
