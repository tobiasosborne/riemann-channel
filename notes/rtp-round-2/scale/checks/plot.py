#!/usr/bin/env python3
"""Floating plots of certified endpoints. Not a numerical certificate."""
import os
from pathlib import Path
checks=Path(__file__).resolve().parent
os.environ.setdefault('MPLCONFIGDIR',str(checks/'mpl-cache'))
import re,json,math
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.hashsalt']='rtp2-scale'
import matplotlib.pyplot as plt
root=checks.parents[3];mp.mp.dps=60
points=json.loads(checks.joinpath('points.json').read_text())
C=mp.mpf(2)**14/3*mp.sqrt(2)*mp.pi**5
mid=lambda s:mp.mpf(s.lstrip('[').split()[0])
fig,ax=plt.subplots(1,3,figsize=(13.5,3.8),layout='constrained')
for point in points:
 x=point['x'];rows=point['rows'];N=[n for n,s in rows];e=[mid(s) for n,s in rows];P=C*x**mp.mpf('4.5')*mp.exp(-4*mp.pi*x)
 ax[0].plot([n/(x*math.log(x)) for n in N],[float(mp.log10(t/P)) for t in e],'.-',label=f'x={x}')
 ax[1].semilogy(N[1:],[float(e[i-1]/e[i]-1) for i in range(1,len(e))],'.-',label=f'x={x}')
ax[0].set(xlabel='N / (x ln x)',ylabel='log10(eps_N / P(x))',title='Resolution at each scale')
ax[0].legend(fontsize=8)
ax[1].axhline(.01,color='black',linestyle='--',linewidth=1)
ax[1].set(xlabel='Upper N of a 40-mode pair',ylabel='eps_(N-40) / eps_N − 1',title='The specified local stopping test')
xs=[d['x'] for d in points];R=[float(mid(d['eps'])/(C*d['x']**mp.mpf('4.5')*mp.exp(-4*mp.pi*d['x']))) for d in points]
ax[2].plot(xs,R,'o-',color='black')
ax[2].set(xlabel='x',ylabel='eps_final / P(x)',title='Prefactor at the stopping endpoints')
for a in ax:a.grid(alpha=.2)
fig.savefig(checks/'scale.svg',metadata={'Date':None,'Creator':'codex:gpt-6-astra'})
fig.savefig(checks/'scale.png',dpi=160)
print('Wrote checks/scale.svg and checks/scale.png; plots are floating.')
