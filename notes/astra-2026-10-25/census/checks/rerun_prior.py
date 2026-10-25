#!/usr/bin/env python3
"""Rerun the four requested lane-J scripts without writing to the input lane."""
import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
from census_lookup import HERE,FLUX

def main():
    source=FLUX.parent;dest=HERE/'prior_rerun';dest.mkdir(exist_ok=True)
    for p in source.glob('*.py'):shutil.copyfile(p,dest/p.name)
    for p in source.glob('output_*.json.txt'):shutil.copyfile(p,dest/p.name)
    out=[]
    for name in ['fluxes','trigonal','genus6','verify']:
        command=[sys.executable,str(dest/f'jac_{name}.py')]
        proc=subprocess.run(command,check=True,capture_output=True,text=True)
        a=(source/f'output_{name}.txt').read_bytes()
        b=(dest/f'output_{name}.txt').read_bytes()
        assert a==b,(name,'transcript differs')
        line=f'jac_{name}.py: exact output byte match; SHA256={hashlib.sha256(b).hexdigest()}'
        print(line,flush=True);out.append(line)
    (HERE/'output_prior_rerun.txt').write_text('\n'.join(out)+'\n')

if __name__=='__main__':main()
