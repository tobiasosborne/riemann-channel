#!/usr/bin/env bash
# Stop RTP round 2 lanes only: the astra_lane.sh runners of notes/rtp-round-2/*, their codex exec processes
# (identified by the brief text in their command line), and optionally the watcher (--watcher). Never touches
# codex processes of other projects. Usage: scripts/rtp2_stop.sh [--watcher]
me=$$
for p in $(pgrep -f "astra_lane.sh notes/rtp-round-2"); do [ "$p" = "$me" ] && continue; tr "\\0" " " < /proc/$p/cmdline 2>/dev/null | grep -q rtp2_stop && continue; kill "$p" 2>/dev/null && echo "killed runner $p"; done
for p in $(pgrep -f 'codex exec'); do
  [ "$p" = "$me" ] && continue; tr "\\0" " " < /proc/$p/cmdline 2>/dev/null | grep -q rtp2_stop && continue
  tr '\0' ' ' < /proc/$p/cmdline 2>/dev/null | grep -q 'notes/rtp-round-2/brief.md\|notes/rtp-round-2/[a-z-]*/astra-brief.md' && kill "$p" 2>/dev/null && echo "killed codex $p"
done
if [ "${1:-}" = "--watcher" ]; then
  for p in $(pgrep -f 'bash scripts/rtp2_watch.sh'); do [ "$p" = "$me" ] && continue; kill "$p" 2>/dev/null && echo "killed watcher $p"; done
fi
