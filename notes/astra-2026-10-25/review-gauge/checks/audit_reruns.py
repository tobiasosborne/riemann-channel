#!/usr/bin/env python3
"""Compare the byte-identical copied lane programs and all their saved outputs.
Copies are used because three original programs write next to __file__.
"""
from pathlib import Path
import hashlib,json,re,difflib
import sympy as s

HERE=Path(__file__).resolve().parent
OLD=HERE.parents[2]/'astra-2026-10-23'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def normal(t):
    t=re.sub(r'elapsed [0-9.]+s','elapsed <time>s',t)
    t=re.sub(r'elapsed=[0-9.]+s','elapsed=<time>s',t)
    t=re.sub(r'elapsed_seconds= [0-9.]+','elapsed_seconds= <time>',t)
    return t

for lane in ['haar','krein']:
    original=OLD/lane/'checks';rerun=HERE/f'rerun_{lane}'
    for p in sorted(original.glob('*.py')):
        assert digest(p)==digest(rerun/p.name)
        print('SOURCE BYTE-IDENTICAL',lane,p.name,digest(p))
    for p in sorted(original.glob('output_*.json')):
        assert json.loads(p.read_text())==json.loads((rerun/p.name).read_text())
        print('JSON EXACTLY EQUAL',lane,p.name)
    for p in sorted(original.glob('output_*.txt')):
        a=normal(p.read_text());b=normal((rerun/p.name).read_text())
        if a==b:print('TEXT EQUAL after elapsed-time normalization',lane,p.name)
        else:
            diff=list(difflib.unified_diff(a.splitlines(),b.splitlines(),n=0))
            print('TEXT DIFFERENCES',lane,p.name,'diff lines',len(diff))
            for line in diff[:45]:print(line)
            # Preserve the full difference, rather than silently filtering it.
            (HERE/('diff_'+lane+'_'+p.name)).write_text('\n'.join(diff)+'\n')
    if lane=='krein':
        a=[z for z in (original/'output_krein_scan.txt').read_text().splitlines() if z.startswith('SUMMARY')]
        b=[z for z in (rerun/'output_krein_scan.txt').read_text().splitlines() if z.startswith('SUMMARY')]
        assert a==b
        print('KREIN ALL TEN ENSEMBLE SUMMARIES EXACTLY EQUAL')
        for line in b:print(line)

x=s.Symbol('x')
data=json.loads((HERE/'rerun_haar/output_finite.json').read_text())
for graph,rows in data.items():
    for kind,coeff in rows.items():
        p=s.Poly.from_list(list(map(s.Rational,coeff)),x)
        factors=p.sqf_list()[1]
        real=sum(m*f.count_roots(-s.oo,s.oo) for f,m in factors)
        cutoff=s.Rational(14,5) # a stricter rational interval inside the band
        outside=sum(m*(f.count_roots(-s.oo,-cutoff)+f.count_roots(cutoff,s.oo)) for f,m in factors)
        print('INDEPENDENT STURM CHECK',graph,kind,'degree',p.degree(),'real roots with multiplicity',real,'outside [-14/5,14/5]',outside)
        assert outside==0
print('PASS source identity, output comparison and independent finite-table root counts')
