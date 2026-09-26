#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane E (claude:opus, 2026-09-26).  Byte-identity reruns of six cheap cases of the lane's
run script (zst/tools/rtp2_ellcurve_run.sh, same arguments), with the driver compiled from the committed source into a
temporary directory (the lane's zst/build binary is not used or touched).  Prints cmp results and the source hash."""
import hashlib, os, subprocess, tempfile, filecmp
from concurrent.futures import ThreadPoolExecutor
root = '/home/tobiasosborne/Projects/riemann-channel'; z = root + '/zst'
tmp = tempfile.mkdtemp(prefix='rtp2_ell_rerun_'); B = tmp + '/rtp2_ellcurve'
print('source sha256', hashlib.sha256(open(z + '/tools/rtp2_ellcurve.c', 'rb').read()).hexdigest())
subprocess.run(['gcc', '-O2', '-std=c11', '-Wall', '-Wextra', '-Wno-unused-parameter', '-Iinclude', 'tools/rtp2_ellcurve.c',
                'build/libzst.a', '-lflint', '-lmpfr', '-lgmp', '-lm', '-o', B], cwd=z, check=True)
cases = [('outputs/rtp2_ellcurve_11a1_spectra_x13.txt', ['--curve', '11a1', '--mode', 'spectra', '--x', '13', '--N', '60']),
         ('outputs/rtp2_ellcurve_14a1_spectra_x25.txt', ['--curve', '14a1', '--mode', 'spectra', '--x', '25', '--N', '60']),
         ('outputs/rtp2_ellcurve_389a1_record.txt', ['--curve', '389a1', '--mode', 'point', '--N', '60', '--xmax', '13', '--prec', '700']),
         ('outputs/rtp2_ellcurve_11a1_axisN_x13.txt', ['--curve', '11a1', '--x', '13', '--Nmax', '200', '--prec', '1000', '--cprec', '700', '--cmp', '20,40,60,120,200', '--control-cap', '0']),
         ('outputs/rtp2_ellcurve_37a1_axisN_x13.txt', ['--curve', '37a1', '--x', '13', '--Nmax', '200', '--prec', '1000', '--cprec', '700', '--cmp', '20,40,60,120,200', '--control-cap', '0']),
         ('notes/rtp-round-2/ellcurve/checks/points/point_11a1_N200_x13.txt', ['--curve', '11a1', '--mode', 'point', '--N', '200', '--xmax', '13', '--prec', '1000', '--control-cap', '120'])]
def run(c):
    ref, args = c; out = os.path.join(tmp, os.path.basename(ref))
    with open(out, 'w') as f: subprocess.run([B, *args], stdout=f, stderr=subprocess.DEVNULL, check=True)
    return ref, filecmp.cmp(out, os.path.join(root, ref), shallow=False)
with ThreadPoolExecutor(6) as p:
    res = list(p.map(run, cases))
for ref, same in res: print(('IDENTICAL ' if same else 'DIFFERENT ') + ref)
print(f'# checks: {len(res)} run, {sum(not s for _, s in res)} failed')
