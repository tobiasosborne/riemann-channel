#!/usr/bin/env python3
"""Author codex:gpt-6-astra. Floating independent quadrature audit, 70 and 100 dps.
Only arithmetic metadata are loaded. No zeros enter this computation.
"""
from pathlib import Path
import re
import mpmath as m
ROOT=Path(__file__).resolve().parents[4]
def ab(curve,x,dps):
    m.mp.dps=dps
    lines=(ROOT/'zst/tests/data/ell_ref.txt').read_text().splitlines()
    row=next(z.split() for z in lines if z.startswith('curve '+curve+' '))
    a1,a2,a3,a4,a6=map(int,row[2].split(','));C=int(row[3]);L=m.log(x)
    atoms=[]
    for p in range(2,x+1):
        if any(p%d==0 for d in range(2,int(p**.5)+1)):continue
        A=sum((v*v+a1*u*v+a3*v-u**3-a2*u*u-a4*u-a6)%p==0 for u in range(p) for v in range(p))
        ap=p-A;prev,cur=2,ap;k=p;raw=ap
        while k<=x:
            atoms.append((m.log(k),-m.mpf(raw)*m.log(p)/k))
            prev,cur=cur,ap*cur-p*prev
            k*=p;raw=cur if C%p else raw*ap
    shift=m.log(C)-2*m.log(2*m.pi)-2*m.euler-2*m.log(1-m.exp(-L))
    ans=[]
    for n in range(4):
        om=2*m.pi*n/L
        q=lambda y:(1-y/L)*m.cos(om*y)
        f=lambda y:(q(y)-1)/m.expm1(y) if y else -1/L
        g=lambda y:m.sin(om*y)/m.expm1(y) if y else om
        a=2*sum(w*q(y) for y,w in atoms)-2*m.quad(f,[0,L/3,2*L/3,L])+shift
        b=-sum(w*m.sin(om*y) for y,w in atoms)/m.pi+m.quad(g,[0,L/3,2*L/3,L])/m.pi
        ans.append((a,b))
    return ans
checks=0
for curve in ['11a1','14a1','37a1']:
    low=ab(curve,13,70);high=ab(curve,13,100)
    p=ROOT/f'outputs/rtp2_ellcurve_{curve}_axisN_x13.txt'
    rows=[dict(re.findall(r'(\w+)=(\S+)',l)) for l in p.read_text().splitlines() if l.startswith('AB ')]
    for i,((a,b),(aa,bb),r) in enumerate(zip(low,high,rows)):
        assert abs(a-aa)<m.mpf('1e-65') and abs(b-bb)<m.mpf('1e-65');checks+=1
        # 30 significant printed decimal digits: allow 0.6 ulp rounding.
        for key,v in [('a',aa),('b',bb)]:
            error=abs(v-m.mpf(r[key]));tol=m.mpf('6e-30')*max(1,abs(v))
            assert error<tol,(curve,i,key,error);checks+=1
        print(curve,i,'a='+m.nstr(aa,35),'b='+m.nstr(bb,35))
print('FLOATING independent quadrature:',checks,'checks passed; 70/100 dps stability < 1e-65')
print('Prediction constants: x slope',m.nstr(4*m.pi/m.log(10),14),
      'CCM 13-50',m.nstr(4*m.pi/m.log(10)-m.mpf('4.5')*m.log10(m.mpf(50)/13)/37,14),
      'sqrt slopes C11,C14',m.nstr(8*m.pi/(m.sqrt(11)*m.log(10)),14),m.nstr(8*m.pi/(m.sqrt(14)*m.log(10)),14))
