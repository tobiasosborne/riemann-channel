#!/usr/bin/env python3
"""Keep the certified matrix prefix; archive unused full-root output.
This performs no numerical changes. Used for the initial pre-split runs only.
"""
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[4]
for arg in sys.argv[1:]:
 x=int(arg);p=root/f'outputs/rtp2_scale_x{x}.txt';s=p.read_text()
 if 'secular_roots=' in s:
  Path(__file__).parent.joinpath(f'fullroots_x{x}.txt').write_text(s)
  s=s.split('secular_roots=')[0]
 lines=s.splitlines()
 for i,line in enumerate(lines):
  if line.startswith('x=') and ' fast=' not in line:lines[i]=line+' fast=0'
 p.write_text('\n'.join(lines)+'\n')
