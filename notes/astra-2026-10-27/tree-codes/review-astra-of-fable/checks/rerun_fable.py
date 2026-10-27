#!/usr/bin/env python3
"""Run original scripts unchanged; all output stays in the review directory."""
from pathlib import Path
import os, re, subprocess, sys, time

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / 'fable' / 'checks'
env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='2', OMP_NUM_THREADS='2')
jobs = [('tree_codes', []), ('mub', []), ('ihara_lefschetz', []), ('ihara_lefschetz_big', ['--big'])]

def canonical(s):
    return '\n'.join(x for x in s.splitlines() if not re.fullmatch(r'\s*\[\d+\.\d+ s\]\s*', x) and x != 'exit 0')

for name, args in jobs:
    script = 'ihara_lefschetz' if name.endswith('_big') else name
    dest = HERE / ('output_rerun_' + name + '.txt')
    start = time.monotonic()
    with dest.open('w') as out:
        result = subprocess.run([sys.executable, '-B', str(SOURCE / (script + '.py')), *args], stdout=out, stderr=subprocess.STDOUT, env=env, cwd=HERE)
    saved = (SOURCE / ('output_' + name + '.txt')).read_text()
    actual = dest.read_text()
    print(name, 'exit', result.returncode, 'seconds', round(time.monotonic()-start, 2), 'exact_except_timing', canonical(actual) == canonical(saved), flush=True)
    if canonical(actual) != canonical(saved):
        import difflib
        diff = '\n'.join(difflib.unified_diff(canonical(saved).splitlines(), canonical(actual).splitlines(), fromfile='saved', tofile='rerun'))
        (HERE / ('output_diff_' + name + '.txt')).write_text(diff + '\n')
        print('difference saved; numerical differences require interpretation', flush=True)
    assert result.returncode == 0, dest
