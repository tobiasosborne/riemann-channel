#!/usr/bin/env python3
"""Run unchanged T audit and legacy runner with PARI; redirect legacy writes.
Python dependencies are imported in a child using the prescribed PARI interpreter.
No original source is edited. The child adds the already-installed pure-Python
sympy location (also preserving lane T's FLINT 0.8 for exact coordinate replay).
"""
from pathlib import Path
import os, subprocess, sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SRC=ROOT/'notes/astra-2026-10-23/tower/checks'
PY='/tmp/claude-1000/-home-tobias-Projects-riemann-channel/venv-astra/bin/python'
if '--worker' not in sys.argv:
    mode=sys.argv[1] if len(sys.argv)>1 else 'audit'
    raise SystemExit(subprocess.run([PY,str(Path(__file__).resolve()),mode,'--worker'],env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')).returncode)
sys.path.insert(0,'/home/tobias/.local/lib/python3.12/site-packages')
sys.path.insert(0,str(SRC))
import runpy
mode=sys.argv[1]
if mode=='audit':
    runpy.run_path(str(SRC/'tower_audit.py'),run_name='__main__')
elif mode=='legacy':
    ns=runpy.run_path(str(SRC/'rerun_legacy.py'),run_name='rt_legacy')
    # run_path returns a copy; change the functions' true globals.
    ns['main'].__globals__['HERE']=HERE
    ns['main']()
elif mode=='u_simultaneous':
    ns=runpy.run_path(str(SRC/'rerun_legacy.py'),run_name='rt_adapter')
    ns['via_cypari'].__globals__['HERE']=HERE
    subprocess.run=ns['via_cypari']
    result=runpy.run_path(str(ROOT/'notes/adelic-gkp/checks/check_tower_pairing.py'),run_name='__main__')
    cases=maps=0
    for tag,row in result['RESULTS'].items():
        if row['weil'] is None or row['tate'] is None: continue
        N=int(tag.split('N=')[1].split()[0]);cases+=1
        for sw,st in zip(row['weil'][0],row['tate'][0]):
            assert sw & {(-s)%N for s in st}, (tag,sw,st)
            maps+=1
    assert cases==25
    print(f'PARI simultaneous Weil/Tate multipliers: {cases}/25 cases, {maps} equivariant maps, one uniform Tate sign inversion; PASS')
else: raise ValueError(mode)
