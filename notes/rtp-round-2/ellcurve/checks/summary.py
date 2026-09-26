#!/usr/bin/env python3
"""Author codex:gpt-6-astra. Deterministic FLOATING extraction of lane-E balls.
Only completed, zero-failure outputs are used. Fits use equal weights per knot;
residuals are in decimal digits. No fit is an asymptotic certificate.
"""
from pathlib import Path
import sys,re,json,math
sys.dont_write_bytecode=True
import numpy as np
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/'outputs'
CURVES={'11a1':11,'14a1':14,'37a1':37}
def parse(p):
    s=p.read_text();rows={}
    for l in s.splitlines():
        if not l or l[0]=='#':continue
        d=dict(re.findall(r'(\w+)=(\[[^]]*\]|[^\s]+)',l))
        if d:rows.setdefault(l.split()[0],[]).append(d)
    m=re.search(r'# checks: (\d+) run, (\d+) failed',s)
    return rows, None if not m else tuple(map(int,m.groups()))
def done(p):
    if not p.exists():return None
    r,c=parse(p)
    return r if c and c[1]==0 else None
def num(s):
    if s.startswith('[+/-'):return 0.
    return float(s.lstrip('[').split()[0])
def fmt(x):return f'{x:.7g}' if isinstance(x,(float,np.floating)) else str(x)
def table(head,rows):
    print('| '+' | '.join(head)+' |\n|'+'|'.join(['---']*len(head))+'|')
    for row in rows:print('| '+' | '.join(map(fmt,row))+' |')
    print()
def slope(a,b,field='epsE',axis=lambda x:x):
    return (math.log10(num(a[field]))-math.log10(num(b[field])))/(axis(float(b['x']))-axis(float(a['x'])))
def fit(x,y):
    X=np.column_stack([np.ones(len(x)),x]);beta=np.linalg.lstsq(X,y,rcond=None)[0];r=y-X@beta
    return -beta[1],float(np.sqrt(np.mean(r*r))),float(max(abs(r)))
def latest(d,tag='EIG'):return max(d[tag],key=lambda r:int(r['N']))
def row_at(d,tag,N):return next(r for r in d[tag] if int(r['N'])==N)
print('## E4. Tables (generated; NUMERICAL unless labelled FLOATING)\n')
print('Eigenvalues and inertia are certified in the raw files. COMPARISON errors use approximate PARI zeros; all slopes, fits and ratios computed here are FLOATING. “Final N” is a finite-resolution proxy, not a bound on the infinite-N tail.\n')
statuses=[]
for p in sorted(OUT.glob('rtp2_ellcurve_*.txt')):
    r,c=parse(p);statuses.append([p.name,*(c or ('RUNNING','—'))])
print('### Run completion\n');table(['file','checks','failures'],statuses)
print('Completed checks:',sum(s[1] for s in statuses if isinstance(s[1],int)),'\n')
D={}
for c in CURVES:
    for x in [13,25,50,100]:
        d=done(OUT/f'rtp2_ellcurve_{c}_axisN_x{x}.txt')
        if d:D[c,x]=d
print('### Resolution and parity\n')
print('N_sat is certified only on 1..Nmax. A value of 1 is left-censored (N=0 is not scanned).\n')
rows=[]
for (c,x),d in D.items():
    e=latest(d);s={r['block']:int(r['N']) for r in d['SAT']};ns=s['full'];at=row_at(d,'EIG',ns)
    rows.append([c,x,e['N'],'/'.join(map(str,[s['full'],s['even'],s['odd']])),ns/(math.sqrt(x/CURVES[c])*math.log(x)),at['epsE'],e['epsE'],e['epsO'],'E' if e['parity']=='1' else 'O'])
table(['curve','x','final N','N_sat full/E/O','N_sat/[sqrt(x/C) log x]','epsE at N_sat','epsE final','epsO final','min parity'],rows)
print('### COMPARISON at final N\n')
rows=[]
for (c,x),d in D.items():
    e=latest(d);co=row_at(d,'COMP',int(e['N']))
    rows.append([c,x,e['N'],co.get('error','inapplicable'),co.get('ratio','—')])
table(['curve','x','N','first-zero error (PARI)','error/epsE'],rows)
print('### Finite-N tails and Schur envelopes\n')
rows=[]
for (c,x),d in D.items():
    e=latest(d);N=int(e['N']);es=sorted(d['EIG'],key=lambda r:int(r['N']));prev=es[-2];r=row_at(d,'ROW',N)
    n60=row_at(d,'EIG',60)
    rows.append([c,x,prev['N']+'→'+e['N'],num(prev['epsE'])/num(e['epsE']),num(prev['epsO'])/num(e['epsO']),num(n60['epsE'])/num(e['epsE']),r['rj'],r['dI'],r['tau'],r['sE'],r['sO']])
table(['curve','x','tail N','epsE(previous)/final','epsO(previous)/final','epsE(60)/final','joint radius','Delta I (nats)','truth tau','sE next','sO next'],rows)
print('### Final-N endpoint slopes (FLOATING, positive digits gained)\n')
rows=[]
for c in CURVES:
    for a,b in [(13,25),(25,50),(13,50),(50,100),(13,100)]:
        if (c,a) not in D or (c,b) not in D:continue
        da,db=D[c,a],D[c,b];ea,eb=latest(da),latest(db);ca,cb=latest(da,'COMP'),latest(db,'COMP')
        ss=slope(ea,eb,axis=math.sqrt)
        rows.append([c,f'{a}–{b}',slope(ea,eb),ss,ss*math.sqrt(CURVES[c]),slope(ea,eb,'epsO'),slope(ca,cb,'error') if 'error' in ca else '—'])
table(['curve','range x','E digits/x','E digits/sqrt x','E digits/sqrt(x/C)','O digits/x','error digits/x'],rows)
print('### CCM axis-x coverage\n');A={};rows=[]
for c in CURVES:
    for N in [60,120,200]:
        p=OUT/f'rtp2_ellcurve_{c}_axisx_ccm_N{N}.txt';d=done(p)
        if not d:continue
        A[c,N]=d;es=d['EIG'];end=es[-1]
        rows.append([c,N,len(es),end['x'],end['epsE'],end['epsO'],sum(int(e['negE'])+int(e['negO'])>0 for e in es),','.join(e['x'] for e in es if e['parity']=='-1') or 'none'])
table(['curve','N','knots','last x','last epsE','last epsO','indefinite knots','odd-minimum windows'],rows)
print('### Linearising variable: equal-weight least squares (FLOATING)\n')
print('Fit log10(epsE)=intercept−slope×variable over every printed knot with x≥13. RMS and max residuals are in decimal digits. The last two variables necessarily have identical residuals within each curve.\n')
rows=[];poly=[];fitdata={}
for (c,N),d in A.items():
    if c=='37a1':continue
    es=[e for e in d['EIG'] if float(e['x'])>=13];x=np.array([float(e['x']) for e in es]);y=np.array([math.log10(num(e['epsE'])) for e in es]);z=np.sqrt(x/CURVES[c])
    for name,v in [('x',x),('sqrt(x)',np.sqrt(x)),('sqrt(x/C)',z)]:
        s,r,m=fit(v,y);rows.append([c,N,f'{x[0]:g}–{x[-1]:g}',len(x),name,s,r,m]);fitdata[c,N,name]=(s,r,m)
    # Model ln eps = a + b ln z - k z. This adds one parameter, explicitly reported.
    ln=y*math.log(10);X=np.column_stack([np.ones(len(z)),np.log(z),-z]);beta=np.linalg.lstsq(X,ln,rcond=None)[0];res=(ln-X@beta)/math.log(10)
    cons=[]
    for k in [8*math.pi,4*math.pi]:
        X2=np.column_stack([np.ones(len(z)),np.log(z)]);be=np.linalg.lstsq(X2,ln+k*z,rcond=None)[0];r=(ln+k*z-X2@be)/math.log(10);cons.extend([be[1],np.sqrt(np.mean(r*r))])
    poly.append([c,N,beta[1],beta[2]/(8*math.pi),np.sqrt(np.mean(res*res)),*cons])
table(['curve','N','range','knots','variable','slope','RMS residual','max residual'],rows)
print('### Exponential with an algebraic prefactor (FLOATING)\n')
print('Fit ln eps=a+b ln z−k z, z=sqrt(x/C), on the same knots (three parameters). Also fit a,b at fixed k=8pi and k=4pi (two parameters). These are finite-range empirical fits, not proofs of a limiting k.\n')
table(['curve','N','b free','k/(8pi) free','RMS free','b at k=8pi','RMS 8pi','b at k=4pi','RMS 4pi'],poly)
print('### Archimedean controls and Rayleigh cancellation\n')
rows=[]
for (c,x),d in D.items():
    e=latest(d);co=latest(d,'CONTROL');r=d['RAY_TOTAL'][0]
    rows.append([c,x,e['N'],co['N'],co['minE'],co['minO'],co['negE']+'/'+co['negO'],r['arch'],r['primes'],r['sum']])
table(['curve','x','N form','N control','control min E','control min O','negative E/O','Rayleigh gamma+log C','Rayleigh primes','sum'],rows)
print('### Complete control spectra, N=60\n')
rows=[]
for c in ['11a1','14a1']:
    for x in [13,25,50]:
        d=done(OUT/f'rtp2_ellcurve_{c}_spectra_x{x}.txt')
        if not d:continue
        for obj in [c,'chi_-4','zeta_gamma','zeta_gamma_poles']:
            if c=='14a1' and obj!=c:continue
            for b in ['E','O']:
                ss=[r for r in d['SPECTRUM'] if r['object']==obj and r['block']==b]
                rows.append([obj,x,b,len(ss),sum(num(r['eigenvalue'])<0 for r in ss),', '.join(fmt(num(r['eigenvalue'])) for r in ss[:3]),fmt(num(ss[-1]['eigenvalue']))])
table(['control','x','block','dimension','negative','first three eigenvalues','maximum'],rows)
print('### Cross-object comparison on round-1 axes (FLOATING slopes)\n')
rows=[]
sys.path.insert(0,str(ROOT/'zst/tools'));from rtp1_a1_summary import axisN
zd={}
for x in [13,25,50]:
    _,rs,cs=axisN(OUT/f'rtp1_a1_axisN_x{x}.txt');n,e,err=cs[-1];zd[x]=(min(rs,key=lambda r:r['logdet'])['N'],n,e,err)
# Supplement from the reviewed certified tail; preserve provenance and precision.
zd[50]=(zd[50][0],420,'2.80881e-258','3.0346e-254')
rows.append(['zeta',','.join(str(zd[x][0]) for x in [13,25,50]),*[zd[x][2] for x in [13,25,50]],(math.log10(float(zd[13][2]))-math.log10(float(zd[25][2])))/12,(math.log10(float(zd[13][2]))-math.log10(float(zd[50][2])))/37,'review N=420 at x50'])
for dsc in [-4,-3,5,8,-7,12,-20,21,13,-8]:
    ds=[done(OUT/f'rtp2_dirichlet_D{dsc}_axisN_x{x}.txt') for x in [13,25,50]]
    if ds[0] is None:continue
    ns=','.join(next(r['N'] for r in d['SAT'] if r['block']=='full') if d else 'pending' for d in ds)
    eps=[latest(d)['epsE'] if d else 'pending' for d in ds]
    s=slope(latest(ds[0]),latest(ds[2])) if ds[2] else 'pending'
    rows.append([f'chi_{dsc}',ns,*eps,slope(latest(ds[0]),latest(ds[1])) if ds[1] else 'pending',s,'completed lane D only'])
for c in CURVES:
    ds=[D.get((c,x)) for x in [13,25,50]]
    if not all(ds):continue
    rows.append([c,','.join(next(r['N'] for r in d['SAT'] if r['block']=='full') for d in ds),*[latest(d)['epsE'] for d in ds],slope(latest(ds[0]),latest(ds[1])),slope(latest(ds[0]),latest(ds[2])),'E block; 37a1 global O'])
table(['object','N_sat at 13,25,50','epsE at 13','epsE at 25','epsE at 50','digits/x 13–25','digits/x 13–50','provenance'],rows)
print('Zeta uses existing A1 outputs and the certified N=420 supplement in notes/reviews/rtp-round-1-2026-09-24.md:651. Other lanes are read only; pending results are not extrapolated.\n')
print('### Rayleigh parts at matched x=50, N=60\n')
rows=[]
# Read original zeta printed decomposition; additions are floating.
s=(OUT/'rtp1_a1_axisx_ccm_N60.txt').read_text()
pole=float(re.search(r'^\s+pole\s+(\S+)',s,re.M)[1]);arch=float(re.search(r'^\s+arch\s+(\S+)',s,re.M)[1]);primes=sum(float(m[1]) for m in re.finditer(r'^\s+k =\s*\d+\s+(\S+)',s,re.M))
rows.append(['zeta',pole,arch,primes,'1.7501e-116'])
for label,p in [('chi_-4',OUT/'rtp2_dirichlet_D-4_axisx_ccm_N60.txt'),('chi_5',OUT/'rtp2_dirichlet_D5_axisx_ccm_N60.txt')]+[(c,OUT/f'rtp2_ellcurve_{c}_axisx_ccm_N60.txt') for c in CURVES]:
    d=done(p)
    if d and d.get('RAY_TOTAL'):
        r=d['RAY_TOTAL'][0];rows.append([label,0,r['arch'],r['primes'],r['sum']])
table(['object','pole','gamma plus conductor','primes','epsilon (actual minimizing block)'],rows)
print('The displayed O(1) parts must not be subtracted at their printed precision to recover epsilon; the raw ball computations verify the cancellation before rounding.\n')
print('### Shared conductor-scaled slope test (FLOATING)\n')
print('Both rank-zero curves at N=60, x≥13: separate intercepts, one common slope. Each model has three parameters and uses exactly the same knots.\n')
if all((c,60) in A for c in ['11a1','14a1']):
    pooled=[]
    for c in ['11a1','14a1']:
        for e in A[c,60]['EIG']:
            if float(e['x'])>=13:pooled.append((c,float(e['x']),math.log10(num(e['epsE']))))
    rows=[]
    for kind in ['sqrt(x)','sqrt(x/C)']:
        X=np.array([[float(c=='11a1'),float(c=='14a1'),-math.sqrt(x/(CURVES[c] if kind=='sqrt(x/C)' else 1))] for c,x,y in pooled]);Y=np.array([y for c,x,y in pooled]);b=np.linalg.lstsq(X,Y,rcond=None)[0];r=Y-X@b
        rows.append([kind,len(Y),b[2],np.sqrt(np.mean(r*r)),max(abs(r))])
    table(['common variable','points','common slope','RMS residual','max residual'],rows)
print('### Error fits and late-window robustness (FLOATING)\n')
rows=[]
for (c,N),d in A.items():
    if c=='37a1':continue
    for field,tag in [('epsE','EIG'),('error','COMP')]:
        for start in ([13,50] if N==200 else [13]):
            es=[e for e in d[tag] if float(e['x'])>=start and field in e]
            if len(es)<3:continue
            x=np.array([float(e['x']) for e in es]);y=np.array([math.log10(num(e[field])) for e in es]);sx,rx,_=fit(x,y);sz,rz,_=fit(np.sqrt(x/CURVES[c]),y)
            rows.append([c,N,field,f'{x[0]:g}–{x[-1]:g}',sx,rx,sz,rz])
table(['curve','N','quantity','range','digits/x','RMS x','digits/sqrt(x/C)','RMS sqrt'],rows)
print('### Individual prime-power Rayleigh terms at x=50,N=60\n')
zterms={int(m[1]):m[2] for m in re.finditer(r'^\s+k =\s*(\d+)\s+(\S+)',s,re.M)}
parts={'zeta':zterms}
for label,p in [('chi_-4',OUT/'rtp2_dirichlet_D-4_axisx_ccm_N60.txt')]+[(c,OUT/f'rtp2_ellcurve_{c}_axisx_ccm_N60.txt') for c in CURVES]:
    d=done(p)
    if d:parts[label]={int(r['term'][1:]):r['value'] for r in d.get('RAY',[]) if r['term'].startswith('k')}
table(['prime power',*parts],[[k,*[pp.get(k,'—') for pp in parts.values()]] for k in [2,3,4,5,7,11,23,49]])
print('### Leading phase-space normalization (FLOATING)\n')
print('S_max=x for zeta, x/q for primitive degree one, 2 sqrt(x/C) for weight two. The conditional universal prediction is 4pi/log(10)=5.457505 digits per unit S_max.\n')
rows=[]
for a,b in [(13,25),(13,50)]:
    rows.append(['zeta',f'{a}–{b}',(math.log10(float(zd[a][2]))-math.log10(float(zd[b][2])))/(b-a)])
for dsc in [-4,-3,5,8,-7,12,-20,21,13,-8]:
    for a,b in [(13,25),(13,50)]:
        da=done(OUT/f'rtp2_dirichlet_D{dsc}_axisN_x{a}.txt');db=done(OUT/f'rtp2_dirichlet_D{dsc}_axisN_x{b}.txt')
        if da and db:rows.append([f'chi_{dsc}',f'{a}–{b}',abs(dsc)*slope(latest(da),latest(db))])
for c in ['11a1','14a1']:
    for a,b in [(13,25),(13,50),(50,100)]:
        if (c,a) in D and (c,b) in D:
            rows.append([c,f'{a}–{b}',slope(latest(D[c,a]),latest(D[c,b]),axis=lambda x:2*math.sqrt(x/CURVES[c]))])
table(['object','range','digits per S_max'],rows)
print('### Fixed-N Schur envelope at matched windows\n')
rows=[]
for c in ['11a1','14a1']:
    d=A.get((c,60))
    if not d:continue
    for r in d['KNOT']:
        if int(r['x']) in [13,25,50]:
            e=next(q for q in d['EIG'] if q['x']==r['x']);co=next(q for q in d['COMP'] if q['x']==r['x'])
            rows.append([c,r['x'],60,e['epsE'],r['rj'],r['dI'],r['tau'],co['error'],co['ratio']])
table(['curve','x','N','epsE','joint radius','Delta I','truth tau','first-zero error (PARI)','error/eps'],rows)
