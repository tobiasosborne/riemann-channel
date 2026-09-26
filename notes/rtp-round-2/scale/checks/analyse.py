#!/usr/bin/env python3
"""Assemble certified results, and explicitly floating descriptive regressions.
Author codex:gpt-6-astra. Never used to construct a form or certificate.
"""
from pathlib import Path
import re, subprocess, json, sys
import mpmath as mp
mp.mp.dps=70
root=Path(__file__).resolve().parents[4]
checks=Path(__file__).resolve().parent
out=Path(sys.argv[1]) if len(sys.argv)>1 else root/'outputs'
work=Path(sys.argv[2]) if len(sys.argv)>2 else checks
work.mkdir(parents=True,exist_ok=True)
points=[]
mid=lambda s:mp.mpf(s.strip('[').split()[0])
for path in sorted(out.glob('rtp2_scale_x*.txt'),key=lambda p:int(p.stem.split('x')[-1])):
 text=path.read_text()
 h=re.search(r'x=(\d+) prec=(\d+)',text)
 if not h:continue
 x,prec=map(int,h.groups())
 rows=[(int(n),s) for n,s in re.findall(r'ROW N=(\d+)\n(?:(?!ROW|FINAL).)*?eps=(\[[^\n]+\])',text,re.S)]
 final=re.search(r'FINAL N=(\d+) N_conv=(\d+) converged=1',text)
 if not final:continue
 n,nc=map(int,final.groups())
 assert rows[-1][0]==n
 assert n==nc+40
 eps=rows[-1][1]
 rat=re.findall(r'previous_over_current=([^\n]+)',text)[-1]
 cmpath=out/f'rtp2_scale_comparison_x{x}.txt'
 comparison=cmpath.read_text() if cmpath.exists() else text
 get=lambda key: re.search(r'^'+re.escape(key)+r'=(.+)$',comparison,re.M)
 err=get('first_zero_error');eratio=get('first_zero_error_over_eps')
 ctl=re.search(r'prime_free_negative_even=(\d+) odd=(\d+) prec=(\d+)',comparison)
 point=dict(x=x,prec=prec,n=n,nc=nc,eps=eps,ratio=rat,rows=rows,
            err=err[1] if err else None,err_ratio=eratio[1] if eratio else None,
            control=list(map(int,ctl.groups())) if ctl else None)
 points.append(point)
work.joinpath('points.json').write_text(json.dumps(points,indent=2)+'\n')
work.joinpath('derived_input.txt').write_text(''.join(f"{d['x']} {d['nc']} {d['n']} {d['prec']} {d['eps']}\n" for d in points))
if points:
 with work.joinpath('derived_input.txt').open() as f, (out/'rtp2_scale_derived.txt').open('w') as g:
  subprocess.run([str(checks/'derived')],stdin=f,stdout=g,check=True)
lines=['# All fits below are FLOATING descriptive fits to the certified printed midpoints.',
       '# They contain no bound on the N=infinity tail or on the prolate asymptotic remainder.']
a0=4*mp.pi/mp.log(10);C=mp.mpf(2)**14/3*mp.sqrt(2)*mp.pi**5
fmt=lambda x:mp.nstr(x,18)
for d in points:
 x=d['x'];e=mid(d['eps']);P=C*x**mp.mpf('4.5')*mp.exp(-4*mp.pi*x)
 lines.append(f'x={x} log10_eps={fmt(mp.log10(e))} eps/P={fmt(e/P)}')
for a,b in zip(points,points[1:]):
 x,y=a['x'],b['x'];de=(mp.log10(mid(a['eps']))-mp.log10(mid(b['eps'])))/(y-x)
 dp=a0-mp.mpf('4.5')*mp.log10(mp.mpf(y)/x)/(y-x)
 lines.append(f'slope {x}->{y}: eps={fmt(de)} prolate={fmt(dp)} difference={fmt(de-dp)}')
 if a['err'] and b['err']:
  lines.append(f'COMPARISON STEP zero-error slope {x}->{y}: {fmt((mp.log10(mid(a["err"]))-mp.log10(mid(b["err"])))/(y-x))}')
def fits(ds,label):
 xs=[mp.mpf(d['x']) for d in ds];ys=mp.matrix([mp.log10(mid(d['eps'])) for d in ds]);logs=[mp.log10(x) for x in xs]
 def fit(A,y):
  A=mp.matrix(A);beta=mp.lu_solve(A.T*A,A.T*y);r=y-A*beta
  return list(beta),[float(v) for v in r],mp.sqrt(sum(v*v for v in r)/len(xs))
 linear,r,rms=fit([[-x,1] for x in xs],ys)
 lines.append(f'{label} linear y=-a*x+c: a={fmt(linear[0])} c={fmt(linear[1])} rms_dex={fmt(rms)} residuals_dex={r}')
 fixed,r,rms=fit([[-x,1] for x in xs],mp.matrix([y-mp.mpf("4.5")*l for y,l in zip(ys,logs)]))
 lines.append(f'{label} fixed b=4.5: a={fmt(fixed[0])} c={fmt(fixed[1])} multiplier_10^c/C={fmt(10**fixed[1]/C)} rms_dex={fmt(rms)} residuals_dex={r}')
 if len(xs)>=3:
  free,r,rms=fit([[-x,l,1] for x,l in zip(xs,logs)],ys)
  lines.append(f'{label} free y=-a*x+b*log10(x)+c: a={fmt(free[0])} b={fmt(free[1])} c={fmt(free[2])} rms_dex={fmt(rms)} residuals_dex={r}')
 cs=[y+a0*x-mp.mpf('4.5')*l for x,y,l in zip(xs,ys,logs)]
 c=sum(cs)/len(cs);r=[z-c for z in cs]
 lines.append(f'{label} fixed a=a0,b=4.5: c={fmt(c)} multiplier_10^c/C={fmt(10**c/C)} residuals_dex={[float(v) for v in r]}')
if len(points)>=2:fits(points,'all_points')
if len(points)>=4:fits(points[-3:],'last_three')
(out/'rtp2_scale_fits.txt').write_text('\n'.join(lines)+'\n')
print(f'Analysed {len(points)} converged points: {[d["x"] for d in points]}')
