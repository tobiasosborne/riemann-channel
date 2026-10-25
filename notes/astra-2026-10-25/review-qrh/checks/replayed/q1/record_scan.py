"""Reproduce the Q1 record keyword audit. Writes only beside this script.

The occurrence table preserves duplicates and false positives. Dispositions are
semantic triage, not theorem certification; astra-proofs.md D3 is the claim audit.
Other concurrently written lane notes can change the hit count between runs.
"""
from pathlib import Path
import re
import csv
import hashlib
from collections import Counter

HERE = Path(__file__).resolve().parent
ROOT = Path('/home/tobias/Projects/riemann-channel')
LANE = ROOT/'notes/astra-2026-10-23/qrh-digest'
pat = re.compile(r'Siegel|zero[-–‐ ]free|quasi[-– ]?(?:Riemann|RH)|GRH|zero[-– ]density', re.I)
dbpat = re.compile(r'Siegel|zero[-–‐ ]free|quasi|conditional|GRH|zero[-– ]density', re.I)


def disposition(path, text):
    low = text.lower()
    if 'notes/astra-2026-10-23/' in path:
        return 'current-round', 'Brief or concurrent lane output; not a pre-existing conditional result.'
    if 'siegel' in low and not re.search(r'siegel.{0,20}zero|zero.{0,20}siegel', low):
        return 'homonym', 'Siegel theta/space/sets/mass or Brauer-Siegel; no near-one zero assumption.'
    if re.search(r'zero-free.{0,35}(construct|domain|description|geometric|realization|realisation)', low) or 'zero-free comparison' in low:
        return 'zero-independent', 'Construction without zero data; a zero-free strip does not construct the metric/domain.'
    if 'conditional' in low and not pat.search(text):
        return 'broad-db-hit', 'Conditional convergence/Choi positivity, other hypotheses, or the word unconditional; inspect D3 exclusions.'
    if 'software-and-algorithmic-scope' in path:
        return 'algorithmic-GRH', 'Not discharged: fixed strip does not automatically give GRH factor-base/certification bounds.'
    if 'GRH' in text:
        if 'rtp-round-' in path:
            return 'finite-check', 'The text explicitly distinguishes finite computations from GRH; no promotion.'
        if any(x in path for x in ['cm-lift', 'ellcurve', 'adelic-gkp-arithmetic', 'adelic-gkp-zeta']):
            return 'infinity-type', 'Elliptic/infinite-order Hecke or full Weil positivity: outside scope, or still requires GRH.'
        if 'deninger-cusp' in path or '04v_' in path or 'claims.tsv' in path:
            return 'critical-line', 'Critical-line metric/damping/simplicity remains open; only a strip/individual-rate range follows.'
        if 'founding' in path:
            return 'Artin-survey', 'O7 alone does not discharge Artin/Hooley input; separate claimed Artin result needs separate audit.'
        if 'finite-prime-language' in path:
            return 'logical-GRH', 'Full GRH decision predicate unchanged.'
        return 'full-GRH', 'Fixed-strip substitute only; full critical-line positivity/family assertion is not discharged.'
    if re.search(r'zero[-– ]density', low):
        return 'density-or-count', 'Usually unconditional N(T) growth; distinguish from near-one zero-density. See D3.'
    if any(x in path for x in ['what-rh-has-become', 'notation-and-definitions', 'founding', 'L12-shards', 'L11-source', 'G2-shards', 'LEDGER']):
        return 'hierarchy-survey', 'Classical spectral-gap/PNT comparison or repeated survey; add fixed strip where relevant.'
    if any(x in path for x in ['selberg/astra', 'reviews/selberg', '09b_', 'L14-codex', 'G4-sidequests']):
        return 'classical-input', 'Already classical nonvanishing/finite-Euler result; O7 is stronger than needed, not a new status.'
    if 'h-theta' in path or '04q_h_theta' in path:
        return 'other-transform', 'Incomplete theta/Hermite-Biehler or canonical factor: see D3; not automatically the zeta strip.'
    if 'weil-bond-analytic' in path:
        return 'function-field', 'Function-field edge criterion; Weil is the applicable theorem, not O7.'
    if 'rtp-' in path:
        return 'finite-check', 'Finite numerical/reference-prefix check; not a full zero-free-region assumption.'
    return 'other-use', 'No strip-only unproved hypothesis identified; exact text retained for reviewer.'


paths = [ROOT/'db/claims.tsv'] + sorted((ROOT/'report/sections').glob('*.tex')) + sorted((ROOT/'notes').rglob('*.md'))
rows = []
for p in paths:
    if p.is_relative_to(LANE):
        continue
    rel = str(p.relative_to(ROOT))
    heading = ''
    label = ''
    for lineno, line in enumerate(p.read_text().split('\n'), 1):
        if line.startswith('#'):
            heading = line.lstrip('# ').strip()
        lm = re.search(r'\\label\{([^}]+)\}', line)
        if lm:
            label = lm.group(1)
        if not (dbpat if rel == 'db/claims.tsv' else pat).search(line):
            continue
        claim = line.split('\t')[0] if rel == 'db/claims.tsv' else label if p.suffix == '.tex' else heading
        category, verdict = disposition(rel, line)
        rows.append([f'Q1-occ-{len(rows)+1:04d}', rel, lineno, claim, category, verdict, line])

with (HERE/'output_record_classification.tsv').open('w', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['occurrence_id','file','line','claim_id_or_section','category','disposition','exact_text'])
    writer.writerows(rows)
(HERE/'output_record_scan.txt').write_text(''.join(f'{r[0]} {r[1]}:{r[2]}: {r[-1]}\n' for r in rows))
print('Occurrence count:', len(rows))
for k, v in sorted(Counter(r[4] for r in rows).items()):
    print(k, v)
print('Detailed occurrence IDs and all duplicate locations: output_record_classification.tsv')

sources = ROOT/'notes/astra-2026-10-23/qrh/sources'
manifest = []
for p in sorted(sources.iterdir()):
    if p.suffix in ['.txt', '.lean', '.pdf']:
        manifest.append(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n')
(HERE/'output_source_sha256.txt').write_text(''.join(manifest))
print('Source fingerprint file: output_source_sha256.txt')
