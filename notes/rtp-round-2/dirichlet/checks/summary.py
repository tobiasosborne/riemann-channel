#!/usr/bin/env python3
"""Author codex:gpt-6-astra. Deterministic FLOATING postprocessing of certified output.
Usage: python3 notes/rtp-round-2/dirichlet/checks/summary.py [outputs]
All slopes, fits and derived ratios are floating (mpmath 60 decimal digits).
"""
from pathlib import Path
import re,sys,json
sys.dont_write_bytecode=True
import mpmath as mp
mp.mp.dps=60
ROOT=Path(__file__).resolve().parents[4]
OUT=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'outputs'
DS=[-4,-3,5,8,-7,12,-20,21,13,-8]
def parse(path):
    rows={}
    for line in path.read_text().splitlines():
        if not line or line.startswith('#'):continue
        tag=line.split()[0]
        f=dict(re.findall(r'(\w+)=(\[[^]]*\]|[^\s]+)',line))
        if f:rows.setdefault(tag,[]).append(f)
    return rows

def num(s):
    if s.startswith('[+/-'):return mp.mpf(0)
    return mp.mpf(s.lstrip('[').split()[0])
def fmt(x,d=6):return mp.nstr(x,d)
def slope(a,b,field='epsE'):
    return (mp.log10(num(a[field]))-mp.log10(num(b[field])))/(int(b['x'])-int(a['x']))
def table(head,rows):
    print('| '+' | '.join(head)+' |');print('|'+ '|'.join(['---']*len(head))+'|')
    for r in rows:print('| '+' | '.join(map(str,r))+' |')
    print()

data={};runs=[]
for D in DS:
    for x in [13,25,50]:
        p=OUT/f'rtp2_dirichlet_D{D}_axisN_x{x}.txt'
        if p.exists():
            d=parse(p)
            if 'EIG' not in d or 'COMP' not in d or '# checks:' not in p.read_text():continue
            ss={s['block']:s for s in d['SAT']}
            end=max(d['EIG'],key=lambda z:int(z['N']))
            ns=ss['full']['N']; atsat=next(r for r in d['EIG'] if r['N']==ns)
            cmp=next((r for r in d['COMP'] if r['N']==end['N']),{})
            row=next(r for r in d['ROW'] if r['N']==end['N'])
            c=next(r for r in d['CONTROL'] if r['N']==end['N'])
            data[D,x]={'all':d,'end':end,'atsat':atsat,'cmp':cmp,'sat':ss,'row':row,'control':c}
for p in sorted(OUT.glob('rtp2_dirichlet_D*.txt')):
    s=p.read_text();m=re.search(r'# checks: (\d+) run, (\d+) failed',s)
    runs.append([p.name,*(m.groups() if m else ['RUNNING','-'])])
# Existing zeta results enter the same comparison tables, without a rerun.
sys.path.insert(0,str(ROOT/'zst/tools'))
from rtp1_a1_summary import axisN
zeta={}
for x in [13,25,50]:
    _,rr,cc=axisN(OUT/f'rtp1_a1_axisN_x{x}.txt')
    n,e,z=cc[-1];ns=min(rr,key=lambda r:r['logdet'])['N']
    zeta[x]={'x':str(x),'N':str(n),'epsE':e,'error':z,'ns':str(ns)}

print('# D4 run status (exact counts)\n')
table(['file','checks','failed'],runs)
print('Total completed checks:',sum(int(r[1]) for r in runs if r[1].isdigit()),'; failures:',sum(int(r[2]) for r in runs if r[2].isdigit()),'\n')
print('# D5. Saturation and final-N results\n')
print('Eigenvalues are rounded certified-ball results. N_sat is over 1..Nmax, certified unique. Final N is a finite-resolution proxy; it is not an infinite-N certificate.\n')
rows=[]
for D in DS:
    for x in [13,25,50]:
        if (D,x) not in data:continue
        d=data[D,x];e=d['end'];s=d['sat'];a=d['atsat']
        rows.append([D,x,e['N'],'/'.join(s[k]['N'] for k in ['full','even','odd']),a['epsE'],e['epsE'],e['epsO'],e['parity']])
for x,z in zeta.items():rows.append(['zeta R1',x,z['N'],z['ns']+'/—/—','—',z['epsE'],'—',1])
rows.append(['zeta review',50,420,'352/—/—','—','2.80881e-258','—',1])
table(['D','x','N final','N_sat full/even/odd','epsE at N_sat','epsE final','epsO final','parity'],rows)
print('# COMPARISON: first root, final N\n')
table(['D','x','N','error (ball)','error/eps (ball)','gamma1'],[[D,x,d['end']['N'],d['cmp'].get('error','NA'),d['cmp'].get('ratio','NA'),d['all']['REFERENCE'][0]['gamma1']] for (D,x),d in data.items()])
print('# FLOATING slopes (positive digits per x)\n')
slopes=[]
for D in DS:
    row=[D]
    for a,b in [(13,25),(25,50),(13,50)]:
        if (D,a) in data and (D,b) in data:
            da,db=data[D,a],data[D,b]
            row.extend([fmt(slope(da['end'],db['end'])),fmt(slope(da['end'],db['end'],'epsO')),fmt(slope(da['cmp'],db['cmp'],'error'))])
        else:row.extend(['NA']*3)
    slopes.append(row)
for label,zs in [('zeta R1',zeta),('zeta review',{**zeta,50:{'x':'50','epsE':'2.80881e-258','error':'3.0346e-254'}})]:
    row=[label]
    for a,b in [(13,25),(25,50),(13,50)]:row.extend([fmt(slope(zs[a],zs[b])),'—',fmt(slope(zs[a],zs[b],'error'))])
    slopes.append(row)
table(['D','E 13–25','O 13–25','error 13–25','E 25–50','O 25–50','error 25–50','E 13–50','O 13–50','error 13–50'],slopes)
print('# FLOATING conductor scaling and polynomial fit\n')
print('Fit log(eps)=a+b log(x/q)-c x/q at the three final-N samples. This is a three-point interpolation, not a validated asymptotic expansion. b_fixed fixes c=4pi and uses endpoints; A_fixed uses x=50.\n')
fits=[]
for D in DS:
    if not all((D,x) in data for x in [13,25,50]):continue
    q=abs(D);ys=[mp.mpf(x)/q for x in [13,25,50]]
    logs=mp.matrix([mp.log(num(data[D,x]['end']['epsE'])) for x in [13,25,50]])
    mat=mp.matrix([[1,mp.log(y),-y] for y in ys]);a,b,c=mp.lu_solve(mat,logs)
    bf=(logs[2]-logs[0]+4*mp.pi*(ys[2]-ys[0]))/mp.log(ys[2]/ys[0])
    af=mp.exp(logs[2]-bf*mp.log(ys[2])+4*mp.pi*ys[2])
    fits.append([D,fmt(q*slope(data[D,13]['end'],data[D,50]['end'])),fmt(b),fmt(c/(4*mp.pi)),fmt(bf),fmt(af)])
table(['D','q × slope 13–50','b fitted','c/(4pi) fitted','b_fixed','A_fixed'],fits)
print('# Controls, Schur envelopes and Rayleigh totals\n')
rows=[]
for (D,x),d in data.items():
    c=d['control'];r=d['all'].get('RAY_TOTAL',[{}])[-1]
    rows.append([D,x,d['end']['N'],d['row']['rj'],c['negE']+'/'+c['negO'],c['minE'],c['minO'],r.get('arch','NA'),r.get('primes','NA')])
table(['D','x','N','joint half-width','negative E/O','control min E','control min O','Rayleigh arch','Rayleigh primes'],rows)
print('# FLOATING finite-N tail check\n')
rows=[]
for (D,x),d in data.items():
    es=sorted(d['all']['EIG'],key=lambda z:int(z['N']));e=d['end'];prev=es[-2]
    rows.append([D,x,prev['N'],e['N'],fmt(num(prev['epsE'])/num(e['epsE'])),fmt(num(d['atsat']['epsE'])/num(e['epsE']))])
table(['D','x','previous N','final N','eps(previous)/eps(final)','eps(N_sat)/eps(final)'],rows)
print('# Zeta round 1 (existing output only; no rerun)\n')
# Import the existing read-only parser.
sys.path.insert(0,str(ROOT/'zst/tools'))
from rtp1_a1_summary import axisN
zr=[]
for x in [13,25,50]:
    _,rr,cc=axisN(OUT/f'rtp1_a1_axisN_x{x}.txt');n,e,z=cc[-1]
    ns=min(rr,key=lambda r:r['logdet'])['N'];r=next(r for r in rr if r['N']==n)
    zr.append([x,n,ns,e,z,r['rj']])
table(['x','N','N_sat','epsE','error upper (COMPARISON)','joint half-width'],zr)
print('Review supplement (not recomputed): zeta x=50,N=420 eps=2.80881e-258; error=3.0346e-254; 13–50 slopes 5.379 and 5.373, source notes/reviews/rtp-round-1-2026-09-24.md, lines 649–651. The existing x50 driver output stops eigenpair comparisons at N=360.\n')
print('# Axis x and fixed-L outcomes\n')
rows=[]
for D in DS:
    for kind,N in [('ccm',60),('ccm',120),('fixedL',60)]:
        p=OUT/f'rtp2_dirichlet_D{D}_axisx_{kind}_N{N}.txt'
        if not p.exists() or '# checks:' not in p.read_text():continue
        d=parse(p)
        if 'EIG' not in d:continue
        es=d['EIG'];last=es[-1];neg=[r for r in es if int(r['negE'])+int(r['negO'])>0]
        odd=[r for r in es if r['parity']=='-1']
        rows.append([D,kind,N,len(es),len(neg),','.join(r['X'] for r in odd) or 'none',last['epsE'],last['epsO']])
table(['D','protocol','N','knots','indefinite knots','odd-minimum cutoffs','final epsE','final epsO'],rows)
print('# FLOATING fixed-resolution slopes and loss relative to final-N proxy\n')
rows=[]
for D in DS:
    for N in [60,120]:
        p=OUT/f'rtp2_dirichlet_D{D}_axisx_ccm_N{N}.txt'
        if not p.exists() or '# checks:' not in p.read_text():continue
        d=parse(p);es={int(r['x']):r for r in d['EIG']};xm=max(es)
        s1=fmt(slope(es[13],es[25]))
        s2=fmt(slope(es[25],es[50])) if 50 in es else '—'
        loss=fmt(mp.log10(num(es[xm]['epsE'])/num(data[D,xm]['end']['epsE']))) if (D,xm) in data else 'pending'
        rows.append([D,N,s1,s2,xm,loss])
table(['D','N fixed','slope 13–25','slope 25–50','terminal x','decimal digits lost vs final-N proxy'],rows)
print('# x50 determinant and precision audit\n')
print('These LDL/bordering certificates complete before the expensive eigenpair comparisons. All values below are ball-certified; N_sat is the unique argmin over 1..420.\n')
rows=[]
for D in DS:
    p=OUT/f'rtp2_dirichlet_D{D}_axisN_x50.txt'
    if not p.exists():continue
    txt=p.read_text();d=parse(p)
    if 'SAT' not in d or len(d.get('ROW',[]))!=420:continue
    s={r['block']:r for r in d['SAT']}
    acc=re.search(r'pivot_accuracy_bits=(\d+)',txt)
    rows.append([D,'/'.join(s[k]['N'] for k in ['full','even','odd']),s['full']['logdet'],acc[1],d['ROW'][-1]['rj']])
table(['D','N_sat full/even/odd','minimum full logdet','worst pivot accuracy (bits of 4200)','joint half-width at N420'],rows)
