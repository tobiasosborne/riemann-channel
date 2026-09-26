#!/usr/bin/env python3
"""Author codex:gpt-6-astra. Audit certificates/identities from completed raw files.
No theorem about a limiting eigenvalue or zero distribution is assumed.
"""
from pathlib import Path
import re,sys,hashlib
import mpmath as m
m.mp.dps=70
ROOT=Path(__file__).resolve().parents[4];OUT=ROOT/'outputs'
def parse(p):
    s=p.read_text();rows={}
    for l in s.splitlines():
        if not l or l.startswith('#'):continue
        d=dict(re.findall(r'(\w+)=(\[[^]]*\]|[^\s]+)',l))
        if d:rows.setdefault(l.split()[0],[]).append(d)
    return s,rows
def ball(s):
    if s.startswith('[+/-'):return m.mpf(0),m.mpf(s[5:-1].strip())
    if s.startswith('['):
        a,b=s[1:-1].split('+/-');return m.mpf(a.strip()),m.mpf(b.strip())
    return m.mpf(s),m.mpf('1e-11')*abs(m.mpf(s)) # display rounding for 12 digits
checks=0;files=[];pending=[]
for p in sorted(OUT.glob('rtp2_ellcurve_*.txt')):
    s,r=parse(p);mch=re.search(r'# checks: (\d+) run, (\d+) failed',s)
    if not mch: print('PENDING',p.name);pending.append(p.name);continue
    assert int(mch[2])==0 and 'CHECK FAIL' not in s;checks+=1;files.append(p)
    for e in r.get('EIG',[]):
        ev,_=ball(e['epsE']);ov,_=ball(e['epsO'])
        assert (ev<ov)==(e['parity']=='1');checks+=1
    for c in r.get('COMP',[]):
        if '37a1' in p.name or '389a1' in p.name:assert 'error' not in c;checks+=1
        elif c.get('roots')!='0':assert c['N']==c['roots'];checks+=1
    for e in r.get('SPECTRUM',[]):
        assert e['certified']=='1' and int(e['upper_count'])==int(e['index']) and int(e['lower_count'])==int(e['index'])-1;checks+=1
    if 'SAT' in r:
        rows=r['ROW']
        for sat in r['SAT']:
            field={'full':'logdet','even':'logdetE','odd':'logdetO'}[sat['block']]
            # Redundant extraction check; mathematical uniqueness already ball-certified in driver.
            assert min(rows,key=lambda e:ball(e[field])[0])['N']==sat['N'];checks+=1
# Entire spectra shift exactly by log(14/11), including eigenvalue order and both blocks.
for x in [13,25,50]:
    p=OUT/f'rtp2_ellcurve_11a1_spectra_x{x}.txt';q=OUT/f'rtp2_ellcurve_14a1_spectra_x{x}.txt'
    if p not in files or q not in files:continue
    _,a=parse(p);_,b=parse(q)
    aa=[e for e in a['SPECTRUM'] if e['object']=='11a1'];bb=[e for e in b['SPECTRUM'] if e['object']=='14a1']
    assert len(aa)==len(bb)==121;checks+=1
    for u,v in zip(aa,bb):
        ua,ur=ball(u['eigenvalue']);va,vr=ball(v['eigenvalue'])
        assert abs(va-ua-m.log(m.mpf(14)/11))<ur+vr,(x,u,v);checks+=1
    # Common controls must be byte-identical in the two independent output sets.
    assert [e for e in a['SPECTRUM'] if e['object']!='11a1']==[e for e in b['SPECTRUM'] if e['object']!='14a1'];checks+=1
print('AUDIT:',len(files),'complete files,',checks,'checks passed')
for p in files:print(hashlib.sha256(p.read_bytes()).hexdigest(),p.relative_to(ROOT))

# Independent precision checks at identical curve/window/resolution, rounded display.
for c,x,n in [('11a1',13,60),('14a1',25,60),('37a1',50,60),('11a1',100,200)]:
    p=ROOT/f'notes/rtp-round-2/ellcurve/checks/recheck_{c}_x{x}_N{n}.txt'
    if not p.exists() or '# checks:' not in p.read_text():continue
    _,a=parse(p)
    source=OUT/f'rtp2_ellcurve_{c}_axisx_ccm_N{n}.txt'
    if x==25 and c=='14a1':source=OUT/'rtp2_ellcurve_14a1_axisN_x25.txt'
    if source not in files:continue
    _,b=parse(source);aa=a['EIG'][0];bb=next(r for r in b['EIG'] if int(r['N'])==n and int(r['x'])==x)
    assert all(aa[k]==bb[k] for k in ['epsE','epsO','parity']);checks+=1
    print('PRECISION_RECHECK',c,x,n,'same printed epsE,epsO,parity')
print('AUDIT_WITH_RECHECKS',checks,'passed')

if pending and "--allow-pending" not in sys.argv:
    raise SystemExit("incomplete numerical outputs: "+", ".join(pending))
