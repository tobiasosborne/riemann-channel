#!/usr/bin/env python3
"""Reproduce lane J2 checks offline, with writes confined to this directory."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
JOBS=[('census_lookup.py',[],'census'),('lowgenus.py',[],'lowgenus'),
      ('obstructions.py',[],'obstructions'),('genus8_search.py',[],'genus8'),
      ('genus8_search.py',['--graph','K33'],'trigonal_K33'),
      ('genus8_search.py',['--graph','Petersen'],'trigonal_Petersen'),
      ('verify_petersen.py',[],'petersen_witness'),('plane_nodes.py',[],'plane_nodes'),
      ('ruled_nodes.py',[],'ruled_nodes'),('plane_smooth.py',[],'plane_smooth'),
      ('double_covers.py',[],'double_covers'),('prism.py',[],'prism'),
      ('rerun_prior.py',[],'prior_rerun')]

def main():
    lines=[]
    for script,args,stem in JOBS:
        command=[sys.executable,str(HERE/script)]+args
        result=subprocess.run(command,check=True,capture_output=True,text=True)
        assert not result.stderr,result.stderr
        (HERE/f'output_{stem}.txt').write_text(result.stdout)
        msg='PASS '+' '.join([script]+args)
        print(msg,flush=True);lines.append(msg)
    def data(name):return json.loads((HERE/f'output_{name}.json.txt').read_text())
    cc=data('census');assert [r['verdict'] for r in cc['targets']]==['NO','NO']
    assert all(len(r['near_misses'])==272 for r in cc['targets'])
    assert data('genus8')['hits']==[]
    assert len(data('trigonal_Petersen')['hits'])==32
    assert all(h['mask']==22 for h in data('trigonal_Petersen')['hits'])
    for name in ['plane_nodes','ruled_nodes','plane_smooth','double_covers']:
        assert data(name)['hits']==[]
    assert [(r['mask'],r['verdict']) for r in data('prism')['orbits']]==[(1,'NO'),(2,'NO'),(5,'NO'),(6,'YES')]
    lines.append('PASS all expected verdicts, counts, witness and empty-search certificates')
    manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(HERE.iterdir())
              if p.is_file() and (p.suffix in ['.py','.cpp'] or p.name.startswith('output_'))
              and p.name not in ['output_audit.txt','output_manifest.json.txt','output_census_console.txt']}
    (HERE/'output_manifest.json.txt').write_text(json.dumps(manifest,indent=2)+'\n')
    lines.append(f'SHA256 manifest: {len(manifest)} source/output files; output_manifest.json.txt')
    (HERE/'output_audit.txt').write_text('\n'.join(lines)+'\n')
    print('\n'.join(lines[-2:]),flush=True)

if __name__=='__main__':main()
