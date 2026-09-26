#!/usr/bin/env python3
"""Behavioural checks for the lane-S certificate (written before implementation)."""
import subprocess
from pathlib import Path
root = Path(__file__).resolve().parents[4]
binary = root / 'zst/build/rtp2_scale'
r = subprocess.run([str(binary), '--selftest'], capture_output=True, text=True)
print(r.stdout, end='')
print(r.stderr, end='')
assert r.returncode == 0
assert 'SELFTEST PASS' in r.stdout
