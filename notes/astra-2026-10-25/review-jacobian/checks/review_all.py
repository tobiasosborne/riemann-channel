#!/usr/bin/env python3
"""Audit the existing outputs; --rerun regenerates everything in this lane only.
No git, no downloads, no writes to source lane. python3 checks/review_all.py --rerun
"""
from pathlib import Path
import hashlib,json,os,subprocess,sys

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parents[2]/'astra-2026-10-23/jacobian/checks'
JOBS=[('review_k4.py','k4'),('review_hyperelliptic_f2.py','hyperelliptic_f2'),('review_k5.py','k5'),('review_polarizations.py','polarizations'),('review_arithmetic.py','arithmetic'),('review_gluing.py','gluing'),('review_genus6.py','genus6'),('review_canonical.py','canonical')]

def main():
    lines=[]
    # Scripts are exact copies; the output directory changes only by relocation.
    for src in sorted(SOURCE.glob('*.py')):
        dst=HERE/'rerun'/src.name
        assert src.read_bytes()==dst.read_bytes()
    if '--rerun' in sys.argv:
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
        with (HERE/'output_rerun.txt').open('w') as f:
            subprocess.run([sys.executable,str(HERE/'rerun/run_all.py')],stdout=f,stderr=subprocess.STDOUT,env=env,check=True)
        for script,label in JOBS:
            with (HERE/f'output_independent_{label}.txt').open('w') as f:
                subprocess.run([sys.executable,str(HERE/script)],stdout=f,stderr=subprocess.STDOUT,env=env,check=True)
    for src in sorted(SOURCE.glob('output_*.txt')):
        dst=HERE/'rerun'/src.name
        assert src.read_bytes()==dst.read_bytes(),src.name
        # Parse every JSON in full, including every recorded matrix and witness.
        if '.json.' in src.name:assert json.loads(src.read_text())==json.loads(dst.read_text())
        lines.append('IDENTICAL '+src.name+' sha256='+hashlib.sha256(dst.read_bytes()).hexdigest())
    for script,label in JOBS:
        out=HERE/f'output_independent_{label}.txt'
        assert out.is_file() and out.stat().st_size and 'Traceback' not in out.read_text(),script
        lines.append('INDEPENDENT '+script+' output_sha256='+hashlib.sha256(out.read_bytes()).hexdigest())
    data=json.loads((HERE/'output_independent_arithmetic.json.txt').read_text())
    assert len(data['orbits'])==17 and data['tally']['graphs']==20 and data['tally']['partition_one']==0
    assert len(json.loads((HERE/'output_independent_hyperelliptic_f2.json.txt').read_text()))==264
    k5=json.loads((HERE/'output_independent_k5.json.txt').read_text())
    assert [len(k5['hits'][str(m)]) for m in (1,3,11,12,13)]==[6,42,6,42,24]
    assert len(json.loads((HERE/'output_independent_canonical.json.txt').read_text()))==24
    lines.append('PASS: all original outputs identical; 8 independent checks; 17 flux orbits; 264 F2 hyperelliptic classes; 120 F3 matching equations; 24 canonical cubic classes; 20 random graphs.')
    text='\n'.join(lines)+'\n';(HERE/'output_review_audit.txt').write_text(text);print(text)

if __name__=='__main__':main()
