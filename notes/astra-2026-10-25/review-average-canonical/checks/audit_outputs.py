#!/usr/bin/env python3
"""Read every saved/replayed output, compare, and independently audit census ranks.
The large census is parsed in full; discriminants replace the lane's Schur stopping rule.
"""
from pathlib import Path
from collections import Counter
import hashlib,re,ast,difflib,math
H=Path(__file__).resolve().parent;ROOT=H.parents[3];lines=[]
def emit(*a):v=' '.join(map(str,a));print(v,flush=True);lines.append(v)
for lane in ['average','canonical']:
 orig=ROOT/'notes/astra-2026-10-23'/lane/'checks';copy=H/('replay_'+lane)
 for src in orig.glob('*.py'):
  assert src.read_bytes()==(copy/src.name).read_bytes()
  emit('unchanged script',lane,src.name,hashlib.sha256(src.read_bytes()).hexdigest())
 for src in sorted(orig.glob('output_*.txt')):
  dst=copy/src.name
  if not dst.exists():emit('NOT YET REPLAYED',lane,src.name);continue
  a=src.read_text().splitlines();b=dst.read_text().splitlines()
  normalize=lambda ls:[v for v in ls if not v.strip().startswith('seconds=')]
  aa,bb=normalize(a),normalize(b)
  diff=list(difflib.unified_diff(aa,bb,fromfile='saved',tofile='replayed',n=1))
  emit('compare',lane,src.name,'saved_lines=',len(a),'replayed_lines=',len(b),'equal_except_timing=',aa==bb,'diff_lines=',len(diff))
  if diff:(H/f'diff_{lane}_{src.stem}.txt').write_text('\n'.join(diff)+'\n')
  elif (H/f'diff_{lane}_{src.stem}.txt').exists():(H/f'diff_{lane}_{src.stem}.txt').unlink()
# Census coefficients -> independent discriminants and counts; no alpha is used to infer rank.
counts=Counter();ranks=Counter();maxzero=0.;minnonzero=math.inf;total=0
p=ROOT/'notes/astra-2026-10-23/canonical/checks/output_ff_all.txt'
for line in p.open():
 if not re.match(r'^[35] \| ',line):continue
 q,f,param,parity,coeff,alpha=line.rstrip('\n').split(' | ')
 q=int(q);f=ast.literal_eval(f);params=ast.literal_eval(param);co=[complex(v.replace('i','j')) for v in coeff.split(',')]
 aa=[] if not alpha else [complex(v.replace('i','j')) for v in alpha.split(',')]
 d=len(co)-1;conductor=len(f)-1;assert d==conductor-1-(parity=='even')
 if d<=1:rank=d
 elif d==2:
  disc=co[1]**2-4*co[2];rank=1 if abs(disc)<1e-6 else 2
 elif d==3:
  a,b,c=co[1:];disc=a*a*b*b-4*b*b*b-4*a*a*a*c-27*c*c+18*a*b*c
  if abs(disc)<1e-5:rank=1 if abs(a*a-3*b)<1e-6 else 2
  else:rank=3
 if d>=2:
  if rank<d:maxzero=max(maxzero,abs(disc))
  else:minnonzero=min(minnonzero,abs(disc))
 assert rank==len(aa)
 counts[q,conductor]+=1;ranks[q,conductor,d,rank]+=1;total+=1
for (q,d),n in sorted(counts.items()):
 expected=q*q-2*q if d==1 else (q-1)**2*q**(2*d-2)
 assert n==expected;emit('independent conductor count',q,d,n)
emit('independent discriminant census',total,'maximum repeated discriminant residual=',maxzero,'minimum nonzero discriminant magnitude=',minnonzero)
for row,n in sorted(ranks.items()):emit('independent support rank',row,n)
assert total==263694 and ranks[5,4,2,1]==30 and ranks[5,4,3,2]==80
# AST/source audit of zeta scripts: enumerate imports and file operations.
for name in ['check_zeta.py','check_zeta_gaussian.py']:
 p=H/'replay_canonical'/name;tree=ast.parse(p.read_text());imports=[];calls=[]
 for node in ast.walk(tree):
  if isinstance(node,ast.Import):imports.extend(a.name for a in node.names)
  if isinstance(node,ast.ImportFrom):imports.append(node.module)
  if isinstance(node,ast.Call):
   f=ast.unparse(node.func)
   if any(w in f.lower() for w in ['open','read','load','zero','lfun']):calls.append(ast.unparse(node))
 emit('zeta source imports',name,imports)
 emit('zeta file/zero-like calls',name,calls)
 assert not any('zetazero' in v or 'lfun' in v or 'loadtxt' in v or 'read_text' in v or 'read_bytes' in v for v in calls)
(H/'output_audit_outputs.txt').write_text('\n'.join(lines)+'\n')
