#!/usr/bin/env bash
# RTP round 2 watcher (2026-09-26): every INTERVAL seconds (default 600)
#   1. commit any new or changed lane files under notes/rtp-round-2/, outputs/rtp2_*, zst/tools/rtp2_*,
#      scripts/rtp2_* as a checkpoint (--no-verify: the gate carries the 8 known Yoshida errors), so that
#      partial astra work is never lost;
#   2. read the codex quota (scripts/codex_quota.py); append to notes/rtp-round-2/quota.log; if the primary
#      window has RESET against the baseline, write notes/rtp-round-2/STOP, kill every codex exec and
#      astra_lane.sh process, make a final checkpoint commit, and exit 2.
# Exits 0 when notes/rtp-round-2/STOP exists at the start of a cycle (manual stop) or when no lane is running
# and notes/rtp-round-2/ALLDONE exists.
set -u
REPO="$(cd "$(dirname "$0")/.." && pwd)"; cd "$REPO"
INTERVAL=${INTERVAL:-600}
R=notes/rtp-round-2
checkpoint() {
  git add -A "$R" 2>/dev/null
  for g in outputs/rtp2_* zst/tools/rtp2_* scripts/rtp2_* viz/rtp2; do ls -d $g >/dev/null 2>&1 && git add -A $g; done
  if ! git diff --cached --quiet; then
    git commit -q --no-verify -m "RTP round 2 checkpoint (in progress, $(date -u +%Y-%m-%dT%H:%MZ)): lane files as they stand

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>" && echo "$(date -Is) checkpoint committed $(git rev-parse --short HEAD)" >> "$R/watch.log"
  fi
}
while true; do
  [ -f "$R/STOP" ] && { checkpoint; echo "$(date -Is) STOP present, exiting" >> "$R/watch.log"; exit 0; }
  checkpoint
  q=$(python3 scripts/codex_quota.py 2>&1); rc=$?
  echo "$q" >> "$R/quota.log"
  if [ $rc -eq 2 ]; then
    echo "$(date -Is) QUOTA RESET DETECTED: $q" | tee -a "$R/watch.log" > "$R/STOP"
    pkill -f 'codex exec' 2>/dev/null; pkill -f 'astra_lane.sh' 2>/dev/null
    sleep 5; checkpoint
    echo "QUOTA RESET: lanes killed, final checkpoint made"; exit 2
  fi
  if [ -f "$R/ALLDONE" ] && ! pgrep -f 'codex exec' >/dev/null; then checkpoint; echo "all lanes done"; exit 0; fi
  sleep "$INTERVAL"
done
