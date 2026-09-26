#!/usr/bin/env python3
"""Independent reproducibility and minimum-eigenvalue audits; codex:gpt-6-astra."""
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'scripts'))
import rtp2_lattice_box as R

for x, N, coords in [(13, 20, [0, 10]), (25, 134, [22])]:
    data = R.load_case(x, N)
    G, c, m = data['G'], data['c'], x - 2
    order = sorted(range(len(c)), key=lambda i: c[i])
    inverse = {j: i for i, j in enumerate(order)}
    A = R.mp.matrix([[G[j, i] for j in order] for i in range(m)])
    cost = R.mp.matrix([c[j] for j in order])
    saved = json.loads((R.CHECKS / f'x{x}_N{N}.json').read_text())
    warm = {(q['k'], q['sign']): q for q in saved['certs']}
    for k in coords:
        for sign in (1, -1):
            b = R.mp.matrix(m, 1)
            b[k] = sign
            cold = R.simplex(cost, A, b)
            ref = R.simplex(cost, A, b, [inverse[j] for j in warm[k, sign]['basis']])
            R.check(cold[1] == ref[1] and cold[0] == ref[0],
                    f'cold/warm audit identity x={x} N={N} n={k+2} sign={sign:+d}')

cases = [(13,20), (13,40), (13,56), (13,60), (17,83), (17,60),
         (19,94), (19,60), (23,123), (23,60), (25,134), (25,60)]
for x, N in cases:
    values = []
    for line in R.minimum_certificates(x, N).splitlines():
        if line.startswith('MIN '):
            match = re.search(r'\[([^ ]+) \+/- ([^\]]+)\]', line)
            values.append(tuple(map(R.mp.mpf, match.groups())))
    eps = min(R.load_case(x, N)['c'])
    value, error = values[0]
    R.check(abs(eps-value) <= error and value+error < values[1][0]-values[1][1],
            f'x={x} N={N}: eps lies in certified even enclosure below odd minimum')

print(f'CHECKS {R.COUNTS[0]} FAILED {R.COUNTS[1]}')
if R.COUNTS[1]:
    sys.exit(1)
