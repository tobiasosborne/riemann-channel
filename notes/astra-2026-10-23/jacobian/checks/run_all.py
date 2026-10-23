#!/usr/bin/env python3
"""Rerun all lane J certificates in dependency order, without network access."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent
NAMES=['jac_fluxes.py','jac_hyperelliptic.py','jac_howe.py','jac_trigonal.py',
       'jac_hyperelliptic_f3.py','jac_genus6.py','jac_verify.py']
lines=[]
for name in NAMES:
    run=subprocess.run([sys.executable,str(HERE/name)],capture_output=True,text=True)
    if run.returncode:
        print(run.stdout);print(run.stderr);raise SystemExit(run.returncode)
    lines.append('PASS '+name)
    print(lines[-1],flush=True)
rows=json.loads((HERE/'output_fluxes.json.txt').read_text())
ram=[r for r in rows if r['ramanujan']]
assert len(ram)==17
assert sum(r['multiplicity'] for r in ram)==176
ok=[r for r in ram if not r['negative_a']]
assert len(ok)==13 and sum(r['multiplicity'] for r in ok)==145
lines.append('17 Ramanujan orbits / 176 switching classes; 13 count-positive orbits / 145 switching classes')
for path in sorted(HERE.glob('output_*.json.txt')):
    lines.append(hashlib.sha256(path.read_bytes()).hexdigest()+'  '+path.name)
(HERE/'output_audit.txt').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines[len(NAMES):]))
