#!/usr/bin/env python3
"""Author codex:gpt-6-astra. Aggregate independent certified CCM knots, no refitting."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[4];points=Path(__file__).resolve().parent/'points'
def pp(n):
    for p in range(2,n+1):
        if any(p%d==0 for d in range(2,int(p**.5)+1)):continue
        k=p
        while k<n:k*=p
        if k==n:return True
    return False
knots=[x for x in range(2,101) if pp(x) or x==100]
data={}
for x in knots:
    s=(points/f'point_11a1_N200_x{x}.txt').read_text();m=re.search(r'# checks: (\d+) run, (\d+) failed',s)
    if not m or int(m[2]):raise RuntimeError(f'incomplete point x={x}')
    data[x]=(s,int(m[1]))
lines=['# rtp2_ellcurve parallel CCM axis x; N=200; prec=1000; independent window points',
       '# No cross-window overlap is computed. Controls are in the axisN and spectra files.']
for x,(s,count) in data.items():
    lines.append(f'# POINT x={x}')
    for line in s.splitlines():
        if line.startswith(('EIG ','KNOT ')):lines.append(line)
        if x==100 and line.startswith(('RAY ','RAY_TOTAL ')):lines.append(line)
lines.append('# COMPARISON STEP: approximate PARI references used only below')
for x,(s,count) in data.items():
    lines.extend(line for line in s.splitlines() if line.startswith(('REFERENCE ','COMP ')))
lines.append(f'# checks: {sum(c for s,c in data.values())} run, 0 failed')
(ROOT/'outputs/rtp2_ellcurve_11a1_axisx_ccm_N200.txt').write_text('\n'.join(lines)+'\n')
print('assembled',len(knots),'independent points')
