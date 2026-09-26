#!/usr/bin/env python3
"""Render tables with rounding checked against both endpoints of printed balls."""
from pathlib import Path
import json,re,mpmath as mp
mp.mp.dps=80
checks=Path(__file__).resolve().parent;root=checks.parents[3]
pts=json.loads(checks.joinpath('points.json').read_text())
def rounded(s,d=12):
 m=re.fullmatch(r'\[([^ ]+) \+/- ([^\]]+)\]',s)
 if not m:raise ValueError(s)
 c,r=map(mp.mpf,m.groups())
 while d>=6:
  a,b=mp.nstr(c-r,d),mp.nstr(c+r,d)
  if a==b:return a
  d-=1
 raise ValueError('rounding not certified: '+s)
der=(root/'outputs/rtp2_scale_derived.txt').read_text()
blocks={int(x):t for x,t in re.findall(r'x=(\d+)(.*?)(?=\nx=|\Z)',der,re.S)}
get=lambda x,k:re.search(r'^'+k+r'=(.+)$',blocks[x],re.M)[1]
lines=['## S2–S4. Consolidated certified tables','',
'**NUMERICAL.** All short decimal entries below are rounded identically at both endpoints of their source balls (`checks/render_tables.py`). Full enclosures remain in the outputs. `N_conv` is the lower member of the first passing pair on the stated 40-mode grid; the reported epsilon and comparison use the upper member.',
'', '| x | N_conv | final N | precision (bits) | eps_final | eps_Nconv / eps_final | N_conv / (x ln x) |',
'|---|---|---|---|---|---|---|']
for d in pts:
 lines.append('| '+ ' | '.join(map(str,[d['x'],d['nc'],d['n'],d['prec'],rounded(d['eps']),rounded(d['ratio']),rounded(get(d['x'],'N_conv_over_xlogx'))]))+' |')
lines+=['','**NUMERICAL — COMPARISON STEP (zeros used here only).** All first roots have an interval-Newton enclosure and a certificate that the preceding positive range is root-free. The final column is an independent, prime-free control (pole plus archimedean terms), certified at 512 bits.','',
'| x | first-zero error | error / eps | eps / P(x) | control negative inertia (even, odd) |','|---|---|---|---|---|']
for d in pts:
 if not d['err'] or not d['control']:continue
 ctl=','.join(map(str,d['control'][:2]))
 lines.append('| '+ ' | '.join(map(str,[d['x'],rounded(d['err']),rounded(d['err_ratio']),rounded(get(d['x'],'eps_over_P')),f'({ctl})']))+' |')
lines+=['','**NUMERICAL (certified slopes of the finite-N endpoints).**','',
'| consecutive x | digits per unit x |','|---|---|']
for label,s in re.findall(r'^(slope_\d+_to_\d+)=(.+)$',der,re.M):
 lines.append(f'| {label.removeprefix("slope_").replace("_to_"," → ")} | {rounded(s)} |')
checks.joinpath('final_tables.md').write_text('\n'.join(lines)+'\n')
print('Rendered checked rounded tables for',len(pts),'points')
