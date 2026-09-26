#!/usr/bin/env bash
# Adopt an orphaned codex lane process: wait for PID to exit, then, unless notes/rtp-round-2/STOP exists or the
# lane report already has its closing section, resume the lane through scripts/astra_lane.sh (which resumes the
# session recorded in <lane>/session.id). Usage: scripts/rtp2_adopt.sh <lane-dir> <pid>
LANE="$1"; PID="$2"; REPO="$(cd "$(dirname "$0")/.." && pwd)"; cd "$REPO"
echo "$(date -Is) adopt: waiting for pid $PID" >> "$LANE/lane.log"
while kill -0 "$PID" 2>/dev/null; do sleep 30; done
echo "$(date -Is) adopt: pid $PID exited" >> "$LANE/lane.log"
[ -f notes/rtp-round-2/STOP ] && { echo "$(date -Is) adopt: STOP present, not resuming" >> "$LANE/lane.log"; exit 0; }
if grep -q 'What this changes in the notebook' "$LANE/astra-proofs.md" 2>/dev/null; then
  echo "codex exit: 0" >> "$LANE/astra.stdout"; echo "$(date -Is) DONE (adopted)" >> "$LANE/lane.log"; exit 0
fi
echo "$(date -Is) adopt: closing section missing, resuming via astra_lane.sh" >> "$LANE/lane.log"
exec scripts/astra_lane.sh "$LANE"
