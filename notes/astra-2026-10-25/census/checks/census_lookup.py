#!/usr/bin/env python3
"""Offline exact HKL label audit. No Sage execution or eval of source data.

Run from any directory. Outputs are confined to this checks directory.
The six stratum count lists independently reconstruct every label, and
their multiplicities are compared with the assembled LMFDB file.
"""
import collections
import hashlib
import json
from pathlib import Path
import re
import sympy as S

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = HERE.parent / 'sources/hkl-genus-6'
FLUX = ROOT / 'notes/astra-2026-10-23/jacobian/checks/output_fluxes.json.txt'
STRATA = ['hyperelliptic', 'trigonal_maroni_0', 'trigonal_maroni_2',
          'bielliptic', 'plane_quintic', 'generic']

def decode_word(word):
    assert word and all('a' <= c <= 'z' for c in word)
    value = 0
    for c in word:
        value = 26*value + ord(c)-97
    return -value if word.startswith('a') else value

def encode_word(n):
    if not n:
        return 'a'
    sign = 'a' if n < 0 else ''
    n = abs(n)
    digits = ''
    while n:
        n, digit = divmod(n, 26)
        digits = chr(97+digit)+digits
    return sign+digits

def decode_label(label):
    g, q, words = label.split('.')
    g, q = int(g), int(q)
    first = [1]+[decode_word(w) for w in words.split('_')]
    assert len(first) == g+1
    return first+[q**i*first[g-i] for i in range(1,g+1)]

def label_from_coeff(c, q=2):
    g = (len(c)-1)//2
    return f'{g}.{q}.'+'_'.join(encode_word(a) for a in c[1:g+1])

def coeff_from_counts(N, q=2):
    g = len(N)
    tr = [0]+[q**k+1-N[k-1] for k in range(1,g+1)]
    c = [1]
    for k in range(1,g+1):
        v = -sum(c[k-i]*tr[i] for i in range(1,k+1))
        assert v % k == 0
        c.append(v//k)
    return c+[q**i*c[g-i] for i in range(1,g+1)]

def counts_from_coeff(c, K=31, q=2):
    degree = len(c)-1
    tr = [0]
    for k in range(1,K+1):
        v = sum(c[i]*tr[k-i] for i in range(1,min(k,degree+1)))
        if k <= degree:
            v += k*c[k]
        tr.append(-v)
    return [q**k+1-tr[k] for k in range(1,K+1)]

def parse_stratum(line):
    match = re.fullmatch(r"\[\[\s*([\d,\s]+)\s*\],\s*'([^']+)',(.*)\]\s*",line)
    assert match, line[:100]
    counts = tuple(map(int,match[1].split(',')))
    assert len(counts) == 6
    return counts, match[2], match[3]

def main():
    out=[]
    def say(*s):
        line=' '.join(map(str,s)); print(line,flush=True); out.append(line)
    assert [decode_word(s) for s in ['a','b','z','ba','bb','ac','ag','aba']] == [0,1,25,26,27,-2,-6,-26]
    for i in range(-10000,10001):
        assert decode_word(encode_word(i)) == i
    say('Decoder round trips: -10000..10000 PASS; a=0 ac=-2 ag=-6 ba=26 aba=-26')
    datafile=SOURCE/'lmfdbgenus6_curves_F2.txt'
    rows={}
    for line_no,line in enumerate(datafile.read_text().splitlines(),1):
        fields=line.split('|')
        assert len(fields)==5
        label=fields[0]; c=decode_label(label)
        assert label_from_coeff(c)==label and label not in rows
        rows[label]=dict(line=line_no,coeff=c,N=counts_from_coeff(c,6),
                         curves=int(fields[2]),hyperelliptic=int(fields[3]))
    say('LMFDB rows',len(rows),'curve multiplicity sum',sum(v['curves'] for v in rows.values()))
    assert len(rows)==38327 and sum(v['curves'] for v in rows.values())==72227
    by_label=collections.defaultdict(list)
    manifest={str(datafile.relative_to(HERE.parent)):hashlib.sha256(datafile.read_bytes()).hexdigest()}
    for stratum in STRATA:
        path=SOURCE/f'Census/{stratum}/data_{stratum}.txt'
        manifest[str(path.relative_to(HERE.parent))]=hashlib.sha256(path.read_bytes()).hexdigest()
        count=0
        for line_no,line in enumerate(path.read_text().splitlines(),1):
            N,aut,eq=parse_stratum(line)
            c=coeff_from_counts(N); label=label_from_coeff(c)
            assert label in rows and list(N)==rows[label]['N']
            by_label[label].append(dict(stratum=stratum,line=line_no,N=N,aut=aut,equation=eq))
            count+=1
            if line_no==1:
                say('FIRST STRATUM ROW',stratum,'N=',N,'label=',label)
        say('STRATUM TOTAL',stratum,count)
    assert set(by_label)==set(rows)
    for label,rr in rows.items():
        assert len(by_label[label])==rr['curves']
        assert sum(v['stratum']=='hyperelliptic' for v in by_label[label])==rr['hyperelliptic']
    say('All 72227 stratum rows reconstruct all 38327 labels, with exact multiplicities: PASS')
    for label,rr in list(rows.items())[:8]:
        say('FIRST LMFDB ROW',rr['line'],label,'N=',rr['N'],'stratum references=',
            [(v['stratum'],v['line']) for v in by_label[label]])
    targets=[]
    t=S.Symbol('T')
    for r in json.loads(FLUX.read_text()):
        if r['graph']!='K33' or not r['ramanujan']:
            continue
        A=S.Matrix(r['A']); x=S.Symbol('x')
        # Independent n by n determinant via its characteristic polynomial.
        cp=A.charpoly(x).as_expr()
        P=S.Poly(S.cancel(t**6*cp.subs(x,(1+2*t*t)/t)),t)
        c=[int(P.nth(i)) for i in range(13)]
        assert c==r['weil_coefficients']
        N=counts_from_coeff(c,31)
        assert N==[r['N'][str(k)] for k in range(1,32)]
        label=label_from_coeff(c)
        say('TARGET K33 mask',r['mask'],'P(T)=',P.as_expr())
        say('LABEL',label,'PRESENT' if label in rows else 'ABSENT')
        say('N1..12',N[:12],'p-rank',max(i for i,a in enumerate(c) if a%2))
        exact=[v for vs in by_label.values() for v in vs if tuple(v['N'])==tuple(N[:6])]
        assert len(exact)==0 and label not in rows
        say('Independent six-count search across all strata: ABSENT')
        near=[]
        for lab,rr in rows.items():
            if rr['N'][:3]==N[:3]:
                kinds=collections.Counter(v['stratum'] for v in by_label[lab])
                near.append(dict(label=lab,N=rr['N'],curves=rr['curves'],strata=dict(kinds)))
        near.sort(key=lambda rr:(rr['N'],rr['label']))
        say('NEAR MISSES N1..3=',N[:3],'isogeny classes=',len(near),'curves=',sum(v['curves'] for v in near))
        for rr in near:
            say(json.dumps(rr,sort_keys=True))
        targets.append(dict(mask=r['mask'],label=label,coeff=c,N=N[:12],verdict='NO',near_misses=near))
    (HERE/'output_census.json.txt').write_text(json.dumps(dict(targets=targets,sha256=manifest),indent=2)+'\n')
    say('SHA256',json.dumps(manifest,sort_keys=True))
    (HERE/'output_census.txt').write_text('\n'.join(out)+'\n')

if __name__=='__main__':
    main()
