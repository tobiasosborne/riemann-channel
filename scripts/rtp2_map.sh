#!/usr/bin/env bash
# Print "<lane-dir> <pid> <start>" for every live codex lane process of RTP round 2 (node processes whose command
# line carries the brief title or, for resumed sessions, the lane path). Excludes shells.
for p in $(pgrep -f 'bin/codex exec'); do
  exe=$(readlink /proc/$p/exe 2>/dev/null); case "$exe" in *node*) ;; *) continue;; esac
  c=$(tr '\0' ' ' < /proc/$p/cmdline 2>/dev/null) || continue
  lane=""
  case "$c" in
    *"Brief for lane D"*) lane=notes/rtp-round-2/dirichlet;;
    *"Brief for lane L"*) lane=notes/rtp-round-2/lattice-box;;
    *"Brief for lane I"*) lane=notes/rtp-round-2/impure-bumps;;
    *"Brief for lane P"*) lane=notes/rtp-round-2/prover;;
    *"notes/rtp-round-2/"*) lane=$(echo "$c" | grep -oE 'notes/rtp-round-2/[a-z-]+' | head -1);;
  esac
  [ -n "$lane" ] && echo "$lane $p $(ps -o lstart= -p $p)"
done
