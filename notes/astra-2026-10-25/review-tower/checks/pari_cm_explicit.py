#!/usr/bin/env python3
"""Legacy CM assertions with the absent elldata lookup expanded to recorded ai.
The initial unmodified failure is preserved in output_legacy_cm_tower.txt.
Only ellinit("441d1") is replaced; every arithmetic GP instruction is unchanged.
"""
from pathlib import Path
import os, subprocess, sys
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
PY='/tmp/claude-1000/-home-tobias-Projects-riemann-channel/venv-astra/bin/python'
if '--worker' not in sys.argv:
    raise SystemExit(subprocess.run([PY,str(Path(__file__).resolve()),'--worker'],env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')).returncode)
sys.path.append('/home/tobias/.local/lib/python3.12/site-packages')
from cypari2 import Pari
import contextlib, hashlib, io, runpy
pari=Pari();pari.allocatemem(256000000,silent=True)
E=pari.ellinit([1,-1,1,-20,46])
assert int(pari.ellglobalred(E)[0])==441 and int(E.j())==-3375
print('PARI',pari('version()'),'explicit ai=[1,-1,1,-20,46]; conductor=441, j=-3375')
real_run=subprocess.run
counter=0;substitutions=0
def gp(args,*a,**kw):
    global counter,substitutions
    if not args or args[0]!='gp': return real_run(args,*a,**kw)
    raw=kw['input']; needle='ellinit("441d1")'
    substitutions+=raw.count(needle)
    body=raw.replace(needle,'ellinit([1,-1,1,-20,46])')
    path=HERE/f'cm_payload_{counter:02d}.gp'
    path.write_text(body);counter+=1
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf): pari.read(str(path))
    (path.with_suffix('.txt')).write_text(buf.getvalue())
    return subprocess.CompletedProcess(args,0,buf.getvalue(),'')
subprocess.run=gp
src=ROOT/'notes/adelic-gkp/checks/check_cm_tower.py'
print('Original Python source SHA256',hashlib.sha256(src.read_bytes()).hexdigest())
ns=runpy.run_path(str(src),run_name='__main__')
assert ns['nfail']==0 and ns['npass']==27 and substitutions==1
print(f'PASS {counter} original GP payloads evaluated, exactly {substitutions} missing database lookup expanded; all 27 legacy assertions pass')
