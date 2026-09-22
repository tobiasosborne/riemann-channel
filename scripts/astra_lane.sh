#!/usr/bin/env bash
# Run one codex gpt-6-astra prover lane, detached, with automatic resume after network failures.
# Usage: scripts/astra_lane.sh <lane-dir>   (lane-dir contains astra-brief.md; writes astra.stdout, session.id, lane.log)
set -u
LANE="$1"; REPO="$(cd "$(dirname "$0")/.." && pwd)"; cd "$REPO"
D="$REPO/$LANE"; OUT="$D/astra.stdout"; LOG="$D/lane.log"; SID="$D/session.id"
MAXRETRY=${MAXRETRY:-8}
run_once() {  # $1 = attempt number
  if [ "$1" -eq 1 ] || [ ! -s "$SID" ]; then
    codex exec -m gpt-6-astra -c 'model_reasoning_effort="xhigh"' -s workspace-write --skip-git-repo-check \
      -o "$D/astra-last.md" "$(cat "$D/astra-brief.md")" >> "$OUT" 2>&1
  else
    codex exec resume "$(cat "$SID")" -c 'model_reasoning_effort="xhigh"' -s workspace-write --skip-git-repo-check \
      -o "$D/astra-last.md" "You were interrupted (network failure). Resume: read $LANE/astra-proofs.md and $LANE/progress.txt, keep what is written, continue from the first PENDING claim of the brief ($LANE/astra-brief.md), and finish all sections including the closing ones. Write incrementally as instructed." >> "$OUT" 2>&1
  fi
  return $?
}
attempt=1
while [ $attempt -le $MAXRETRY ]; do
  echo "$(date -Is) attempt $attempt start" >> "$LOG"
  run_once $attempt; rc=$?
  # capture the session id from stdout (first occurrence)
  if [ ! -s "$SID" ]; then grep -m1 -oE 'session id: [0-9a-f-]{36}' "$OUT" | awk '{print $3}' > "$SID" 2>/dev/null || true; fi
  echo "$(date -Is) attempt $attempt exit $rc" >> "$LOG"
  if [ $rc -eq 0 ] && grep -q 'What this changes in the notebook' "$D/astra-proofs.md" 2>/dev/null; then
    echo "codex exit: 0" >> "$OUT"; echo "$(date -Is) DONE" >> "$LOG"; exit 0
  fi
  if [ $rc -eq 0 ]; then
    # finished without the closing section: one more resume to complete
    echo "$(date -Is) finished without closing section; resuming once more" >> "$LOG"
  fi
  attempt=$((attempt+1)); sleep 90
done
echo "codex exit: FAILED after $MAXRETRY attempts" >> "$OUT"; echo "$(date -Is) FAILED" >> "$LOG"; exit 1
