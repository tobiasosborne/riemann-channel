#!/usr/bin/env python3
"""Author claude:opus, 2026-09-26. Consistency of the regenerated x=50 files (D=8,-7,12,21,13)
with the partial versions written by the codex lane before its stop.
The partial files were overwritten by the rerun; this script uses every line of them that survives
verbatim in the lane transcript astra.stdout (grep/tail/cat output of the form
'outputs/rtp2_dirichlet_D.._axisN_x50.txt:<line>' or '==> file <==' blocks), plus the values the
REFUTE review recorded from them (correction 4; x50 audit table of the report).
Every surviving line must occur verbatim in the regenerated file."""
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
T = (ROOT/'notes/rtp-round-2/dirichlet/astra.stdout').read_text(errors='replace').splitlines()
new = {D: (ROOT/f'outputs/rtp2_dirichlet_D{D}_axisN_x50.txt').read_text().splitlines() for D in [8,-7,12,21,13]}
n = 0; bad = []; kinds = {}
for line in T:
    m = re.match(r'^(?:\S*/)?outputs/rtp2_dirichlet_D(-?\d+)_axisN_x50\.txt[:-](.*)$', line)
    if not m: continue
    D = int(m.group(1)); body = m.group(2)
    if D not in new or not body.strip(): continue
    # strip grep -n line numbers "123:" if present
    body2 = re.sub(r'^\d+[:-]', '', body)
    if not re.match(r'^(#|AB|ROW|SAT|EIG|CONTROL|RAY|REFERENCE|COMP)', body2): continue
    n += 1; k = body2.split()[0]; kinds[k] = kinds.get(k, 0) + 1
    if body2 not in new[D] and body not in new[D]:
        # allow truncation by the transcript (cut -c / long-line elision)
        if not any(l.startswith(body2) for l in new[D]): bad.append((D, body2[:160]))
print(f'transcript lines from partial x50 files (D=8,-7,12,21,13): {n} by kind {kinds}; not found verbatim in regenerated files: {len(bad)}')
for b in bad[:20]: print('  MISMATCH', b)
# values recorded by the review (correction 4) and the report's x50 audit table
rec = {8:('35/35/30','-302.47559909992','3824','5.794128371','1.34126866389e-30','2.78341006540e-32','3.88470771085e-28'),
      -7:('41/41/39','-373.15804027167','3807','5.729216772','1.27969498626e-33','3.36363897513e-35','5.95491780729e-31'),
      12:('21/21/21','-117.12155458100','3873','5.500469183','1.99821570732e-19','4.27129546329e-21','3.54390522474e-17'),
      21:('10/10/10','-31.159762225705','3906','4.905560988','4.53750087410e-10','2.43317378269e-11','4.42617513034e-8'),
      13:('21/21/15','-99.791521188752','3877','5.022479853','4.63830885392e-18','2.59928813113e-19','1.92857049372e-15')}
ok = 0
for D, (sat, ld, piv, rj, e0, e1, o1) in rec.items():
    s = '\n'.join(new[D])
    satN = '/'.join(re.search(rf'^SAT block={b} N=(\d+)', s, re.M).group(1) for b in ['full','even','odd'])
    checks = [satN == sat, f'SAT block=full N={sat.split("/")[0]} logdet={ld} ' in s, f'pivot_accuracy_bits={piv}' in s,
              re.search(rf'^ROW N=420 .* rj={re.escape(rj)} ', s, re.M) is not None,
              f'N={sat.split("/")[0]} epsE={e0} ' in s, f'N=420 epsE={e1} epsO={o1} ' in s,
              s.rstrip().endswith('# checks: 2567 run, 0 failed'), 'CHECK FAIL' not in s,
              len(re.findall(r'^RAY ', s, re.M)) > 0 and '\nRAY_TOTAL x=50 N=420' in s,
              '# COMPARISON STEP' in s and len(re.findall(r'^COMP ', s, re.M)) == 5 and '\nREFERENCE ' in s,
              len(re.findall(r'^ROW ', s, re.M)) == 420]
    ok += all(checks)
    print(f'D={D:3d}: recorded-value and completeness checks {sum(checks)}/{len(checks)}')
print(f'files passing all: {ok}/5')
