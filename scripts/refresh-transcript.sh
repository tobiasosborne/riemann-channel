#!/usr/bin/env bash
# Re-copy the founding session log from the Claude Code project dir and re-render it.
set -e
cd "$(dirname "$0")/.."
SRC=~/.claude/projects/-home-tobias-Projects-arithmetic-quantum-mechanics/be21a927-f4da-4a9f-ad12-808ab694ae21.jsonl
cp "$SRC" transcript/session-2026-09-10-be21a927.jsonl
python3 scripts/transcript_to_md.py transcript/session-2026-09-10-be21a927.jsonl transcript/transcript.md
fmd-report transcript/transcript.md -o transcript/transcript.html
