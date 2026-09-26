#!/usr/bin/env python3
"""Author codex:gpt-6-astra. Structural and floating consistency audit of the run files.
These checks do not replace Arb certificates. They detect missing runs, parser mistakes,
nonmonotone block minima at fixed x, incorrect conductor-control behavior, or stale failures.
"""
from pathlib import Path
import re,sys
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).parent))
# Avoid importing summary.py, whose output is intentionally top-level.
ROOT=Path(__file__).resolve().parents[4]
def read(p):
    out={}
    for line in p.read_text().splitlines():
        f=dict(re.findall(r'(\w+)=(\[[^]]*\]|[^\s]+)',line))
        if f:out.setdefault(line.split()[0],[]).append(f)
    return out
n=0;failed=[]
def check(ok,msg):
    global n
    n+=1
    if not ok:failed.append(msg)
DS=[-4,-3,5,8,-7,12,-20,21,13,-8]
for D in DS:
    for x in [13,25,50]:
        p=ROOT/f'outputs/rtp2_dirichlet_D{D}_axisN_x{x}.txt'
        check(p.exists(),f'missing {p.name}')
        if not p.exists():continue
        txt=p.read_text();d=read(p)
        check(bool(re.search(r'# checks: \d+ run, 0 failed',txt)),f'failed/incomplete {p.name}')
        if not {'EIG','CONTROL','SAT','COMP'}<=d.keys():continue
        check(len(d['ROW'])=={13:200,25:260,50:420}[x],f'row count {p.name}')
        for b in ['epsE','epsO']:
            es=[float(r[b]) for r in d['EIG']]
            check(all(es[i+1]<=es[i]*(1+1e-10) for i in range(len(es)-1)),f'interlacing {b} {p.name}')
        for r in d['COMP']:
            check(int(r['roots'])==int(r['N']),f'root completeness {p.name},N={r["N"]}')
            if 'error' in r:
                e=next(v for v in d['EIG'] if v['N']==r['N'])
                check(abs(float(r['error'])/float(e['epsE'])/float(r['ratio'])-1)<2e-10,f'ratio {p.name},N={r["N"]}')
        for b in ['negE','negO']:
            ns=[int(r[b]) for r in d['CONTROL']]
            check(all(ns[i+1]>=ns[i] for i in range(len(ns)-1)),f'control interlacing {p.name}')
        for r in d['CONTROL']:
            N=int(r['N']);check(int(r['negE'])+int(r['posE'])==N+1 and int(r['negO'])+int(r['posO'])==N,f'inertia dimensions {p.name}')
    for kind,N in [('ccm',60),('ccm',120)]+([('fixedL',60)] if D in [-4,5] else []):
        p=ROOT/f'outputs/rtp2_dirichlet_D{D}_axisx_{kind}_N{N}.txt'
        check(p.exists() and bool(re.search(r'# checks: \d+ run, 0 failed',p.read_text())),f'axisx complete {p.name}')
for x in [13,25,50]:
    pp=[ROOT/f'outputs/rtp2_dirichlet_D{D}_axisN_x{x}.txt' for D in [8,-8]]
    if all(p.exists() for p in pp):
        dd=[read(p) for p in pp]
        if all('CONTROL' in d for d in dd):
            a,b=[d['CONTROL'][-1] for d in dd]
            for block in ['E','O']:
                check(float(b['min'+block])>float(a['min'+block]),f'gamma parity multiplier {x} {block}')
# At equal x,N and character parity, controls differ by an identity shift.
import math
for x in [13,25,50]:
    for D1,D2 in [(-3,-4),(-4,-7),(-7,-8),(-8,-20),(5,8),(8,12),(12,13),(13,21)]:
        paths=[ROOT/f'outputs/rtp2_dirichlet_D{D}_axisN_x{x}.txt' for D in [D1,D2]]
        if all(p.exists() and 'CONTROL' in read(p) for p in paths):
            a,b=[read(p)['CONTROL'][-1] for p in paths]
            if a['N']!=b['N']:continue
            for key in ['minE','minO']:
                check(abs(float(b[key])-float(a[key])-math.log(abs(D2)/abs(D1)))<3e-11,f'conductor identity shift {D1},{D2},x={x},{key}')
print(f'checks: {n} run, {len(failed)} failed (floating/structural audit)')
for f in failed:print('FAIL:',f)
sys.exit(bool(failed))
