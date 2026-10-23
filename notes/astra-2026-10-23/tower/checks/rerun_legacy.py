#!/usr/bin/env python3
"""Rerun original F/U scripts, using cypari2 at the subprocess boundary if present.

Unmodified original programs and their original assertions; backend replacement
does not change GP source. Records missing dependency honestly. Writes only here.
Run: python3 notes/astra-2026-10-23/tower/checks/rerun_legacy.py
"""
import contextlib
import hashlib
import io
import runpy
import subprocess
import traceback
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
real_run=subprocess.run

try:
    from cypari2 import Pari
except ImportError:
    Pari=None


def via_cypari(args,*a,**kw):
    if not args or args[0]!='gp':
        return real_run(args,*a,**kw)
    pari=Pari()
    pari.allocatemem(256_000_000,1_000_000_000)
    payload=HERE/'_legacy_payload.gp'
    payload.write_text(kw['input'])
    buf=io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            pari.read(str(payload))
        return subprocess.CompletedProcess(args,0,buf.getvalue(),'')
    finally:
        payload.unlink(missing_ok=True)


def main():
    incomplete=0
    for name in ('overlap_data','tower_pairing','cm_tower'):
        src=ROOT/f'notes/adelic-gkp/checks/check_{name}.py'
        out=HERE/f'output_legacy_{name}.txt'
        with out.open('w') as f,contextlib.redirect_stdout(f),contextlib.redirect_stderr(f):
            print('Original source:',src.relative_to(ROOT))
            print('SHA256:',hashlib.sha256(src.read_bytes()).hexdigest())
            print('Backend:', 'cypari2 evaluating unchanged GP source' if Pari else 'original gp subprocess; cypari2 absent')
            if Pari:
                subprocess.run=via_cypari
            try:
                ns=runpy.run_path(str(src),run_name='__main__')
                if ns.get('nfail',0):
                    raise AssertionError(f"{ns['nfail']} legacy failures")
                print('RERUN COMPLETE')
            except Exception:
                incomplete+=1
                traceback.print_exc()
                print('RERUN INCOMPLETE — do not count historical passes as new verification.')
            finally:
                subprocess.run=real_run
        print(out.relative_to(ROOT))
    if incomplete:
        print(f'INCOMPLETE: {incomplete} requested legacy reruns; inspect the logs.')
        raise SystemExit(1)


if __name__=='__main__':
    main()
