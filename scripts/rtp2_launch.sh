#!/usr/bin/env bash
# Launch one RTP round 2 lane fully detached (setsid nohup) through scripts/astra_lane.sh. Usage: scripts/rtp2_launch.sh <lane-dir>
cd "$(dirname "$0")/.."; [ -f notes/rtp-round-2/STOP ] && { echo "STOP present: not launching"; exit 1; }
setsid nohup scripts/astra_lane.sh "$1" > "$1/runner.out" 2>&1 < /dev/null &
echo "launched $1 (runner pid $!)"
