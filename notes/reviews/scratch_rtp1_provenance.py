#!/usr/bin/env python3
"""REFUTE lane R, RTP-1 (claude:opus, 2026-09-24).  Claim C7: byte-check every proposed provenance row of
lane B1 (notes/rtp-round-1/lane-B1-provenance-rows.tsv) with the containment test of scripts/labbook_check.py
(re-implemented here: lines by Python str.splitlines(), window = lines a..b joined by spaces, whitespace
normalised, quote must be a substring), plus: (i) the quote must NOT already be found by the grep-style
numbering if that differs (reports the offset), (ii) the number of occurrences of the normalised quote in the
whole file, (iii) whether the row is already present in db/provenance.tsv and identical.  Prints each window
for the reader's reading.  Deterministic."""
import os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
def norm_ws(s): return re.sub(r'\s+', ' ', s).strip()
def read(rel):
    p = os.path.join(ROOT, rel)
    return open(p, encoding='utf-8', errors='replace').read() if os.path.isfile(p) else None
def rows(rel):
    t = read(rel); out = []
    lines = [l for l in t.splitlines() if l.strip() and not l.startswith('#')]
    hdr = lines[0].split('\t')
    for l in lines[1:]:
        c = l.split('\t'); out.append(dict(zip(hdr, c)))
    return out
NCHK = [0, 0]
def check(c, m):
    NCHK[0] += 1; NCHK[1] += (not c); print(('PASS ' if c else 'FAIL ') + m)
R = rows('notes/rtp-round-1/lane-B1-provenance-rows.tsv')
DB = {r['id']: r for r in rows('db/provenance.tsv')}
print(f'{len(R)} proposed rows; {sum(r["id"] in DB for r in R)} already present in db/provenance.tsv (working tree)')
ids = [r['id'] for r in R]
check(len(ids) == len(set(ids)), 'proposed ids unique')
clash = [i for i in ids if i in DB and DB[i] != [r for r in R if r['id'] == i][0]]
check(not clash, f'no proposed id clashes with a different existing db row ({clash})')
verbose = '-v' in sys.argv
for r in R:
    src = read(f"refs/src/{r['key']}/{r['file']}")
    if src is None:
        check(False, f"{r['id']}: source missing refs/src/{r['key']}/{r['file']}"); continue
    a, b = (r['lines'].split('-') + [None])[:2]; a = int(a); b = int(b) if b else a
    L = src.splitlines()
    win = norm_ws(' '.join(L[a - 1:b]))
    q = norm_ws(r['quote'])
    ok = q in win
    nocc = norm_ws(src).count(q)
    # grep -n style numbering (split on \n only)
    G = src.split('\n')
    gwin = norm_ws(' '.join(G[a - 1:b]))
    check(ok, f"{r['id']}: {r['key']}:{r['file']}:{r['lines']} contained (occurrences in file: {nocc}; also at same grep -n lines: {q in gwin})")
    if verbose or not ok:
        print('    QUOTE :', q[:300])
        print('    WINDOW:', win[:400])
print(f'# checks: {NCHK[0]} run, {NCHK[1]} failed')
