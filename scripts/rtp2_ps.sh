#!/usr/bin/env bash
# List RTP round 2 processes (codex lanes by brief title, runners, adopters, watcher), excluding this script's own shell.
me=$$; pp=$PPID
for p in $(pgrep -f 'codex exec'); do
  [ "$p" = "$me" ] || [ "$p" = "$pp" ] && continue
  c=$(tr '\0' ' ' < /proc/$p/cmdline 2>/dev/null); echo "$c" | grep -q 'rtp2_ps' && continue
  lane=$(echo "$c" | grep -oE 'Brief for lane [DLIP]' | head -1); [ -z "$lane" ] && { echo "$c" | grep -q 'Resume: read' && lane="resume $(echo "$c" | grep -oE 'notes/rtp-round-2/[a-z-]+' | head -1)"; }
  [ -z "$lane" ] && lane="(other project)"
  echo "codex $p start=$(ps -o lstart= -p $p) $lane"
done
for pat in 'astra_lane.sh notes/rtp-round-2' 'rtp2_adopt.sh notes' 'bash scripts/rtp2_watch.sh'; do
  for p in $(pgrep -f "$pat"); do [ "$p" = "$me" ] || [ "$p" = "$pp" ] && continue; c=$(tr '\0' ' ' < /proc/$p/cmdline 2>/dev/null); echo "$c" | grep -q 'rtp2_ps' && continue; echo "proc $p: $(echo "$c" | cut -c1-90)"; done
done
