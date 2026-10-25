"""Compare every line of archived outputs with the safely relocated replays.

Run the scripts under checks/replayed first. They intentionally write only
here; original scripts that open output files must not run in their old paths.
"""
from pathlib import Path
import csv,hashlib,difflib

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
OLD=ROOT/'notes/astra-2026-10-23'
pairs=[(OLD/'qrh-digest/checks/output_exponents.txt',HERE/'output_replay_exponents.txt'),
       (OLD/'qrh-digest/checks/output_structural_checks.txt',HERE/'output_replay_structural_checks.txt'),
       (OLD/'qrh-transpose/checks/output_ff.txt',HERE/'replayed/q2/output_ff.txt'),
       (OLD/'qrh-transpose/checks/output_graph.txt',HERE/'replayed/q2/output_graph.txt'),
       (OLD/'qrh-transpose/checks/output_ff_run.txt',HERE/'output_replay_ff_run.txt'),
       (OLD/'qrh-transpose/checks/output_graph_run.txt',HERE/'output_replay_graph_run.txt')]
for a,b in pairs:
    A=a.read_bytes();B=b.read_bytes()
    print(a.relative_to(ROOT),': lines=',len(A.splitlines()),'byte-identical=',A==B)
    assert A==B

def inventory(p):
    with p.open() as f:return list(csv.DictReader(f,delimiter='\t'))
old=inventory(OLD/'qrh-digest/checks/output_record_classification.tsv')
new=inventory(HERE/'replayed/q1/output_record_classification.tsv')
key=lambda r:(r['file'],r['exact_text'])
missing={key(r) for r in old}-{key(r) for r in new}
added={key(r) for r in new}-{key(r) for r in old}
print('record scan rows: archived=',len(old),'replayed=',len(new))
print('archived file/text pairs missing=',len(missing),'new file/text pairs=',len(added))
for a in sorted(missing):print('MISSING',a)
# Current work can add matches and move lines; do not compare occurrence IDs.
assert not missing
source_manifest=OLD/'qrh-digest/checks/output_source_sha256.txt'
for line in source_manifest.read_text().splitlines():
    expected,name=line.split('  ',1)
    actual=hashlib.sha256((OLD/'qrh/sources'/name).read_bytes()).hexdigest()
    print('source sha256',name,'match=',actual==expected)
    assert actual==expected
print('PASS: all mathematical replay outputs match; scan growth is inventory, not a changed theorem.')
