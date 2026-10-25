#!/usr/bin/env python3
"""Assemble/audit the extra q=7,D=7 full table; rerun missing inputs."""
from shortrow_exact import *
from shortrow_reconstruct import run
from shutil import copyfile
q=7;D=7
fn=HERE/'cells_7_reconstruct_D7_h7.json'
if not fn.exists():
    canonical=HERE/'cells_7_reconstruct.json'
    if canonical.exists() and '7,7' in json.loads(canonical.read_text()):copyfile(canonical,fn)
    else:
        run(q,D,7)
        copyfile(canonical,fn)
rec=json.loads(fn.read_text())
fn=HERE/'cells_7_7_poisson.json'
if not fn.exists():fn.write_text(json.dumps(poisson(Field(q,D),D,8),indent=2)+'\n')
po={int(h):int(s) for h,s in json.loads(fn.read_text()).items()}
old=json.loads((HERE/'cells_all.json').read_text())
checked=0
for key,s in rec.items():
    d,h=map(int,key.split(','));k=f'{q},{d},{h}'
    if k in old:assert int(s)==old[k],(key,s,old[k]);checked+=1
print('EXTENSION_OVERLAP_WITH_ORIGINAL_TABLE',checked,'PASS')
rows={h:int(rec[f'{D},{h}']) if f'{D},{h}' in rec else po[h] for h in range(2*D+1)}
lines=['| q | D | h | exact S | exact R | log_q(R)/D |','|---:|---:|---:|---:|---:|---:|']
for h,s in rows.items():
    R=Fraction(s,q**(D+h+1));line=f'| {q} | {D} | {h} | {s} | {R} | {log(float(R),q)/D:.12f} |'
    print(line);lines.append(line)
for j in range(6):
    h=(5+j)*D//5;s=rows[h];R=Fraction(s,q**(D+h+1))
    print('EXTENDED_GROWTH target_theta=',Fraction(j,5),'h=',h,'actual_theta=',Fraction(h-D,D),'R=',R,'c=',f'{log(float(R),q)/D:.12f}')
(HERE/'table_extension.md').write_text('\n'.join(lines)+'\n')
(HERE/'cells_7_7_extension.json').write_text(json.dumps(rows,indent=2)+'\n')
combined=dict(old)
combined.update({f'{q},{D},{h}':s for h,s in rows.items()})
(HERE/'cells_all_extended.json').write_text(json.dumps(combined,indent=2)+'\n')
print('TOTAL_EXACT_CELLS_INCLUDING_D0_AND_EXTENSION',len(combined))
print('EXTENSION PASS; degree-seven critical cell uses Gauss/FE reconstruction; h>=8 uses signed pair Poisson.')
