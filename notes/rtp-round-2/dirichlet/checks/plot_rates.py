#!/usr/bin/env python3
"""Author codex:gpt-6-astra. Publication-style plot; all derived rates are floating.
Plots only completed x13 and x50 final-N measurements. PDF/PNG output stays in checks/.
"""
from pathlib import Path
import re,math,os
P=Path(__file__).resolve().parent
os.environ.setdefault('MPLCONFIGDIR',str(P/'mplconfig'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=P.parents[3]
Ds=[-3,-4,5,-7,8,-8,12,13,-20,21]
rows=[]
for D in Ds:
    vals=[]
    for x,N in [(13,200),(50,420)]:
        p=ROOT/f'outputs/rtp2_dirichlet_D{D}_axisN_x{x}.txt'
        if not p.exists() or '# checks:' not in p.read_text():break
        s=p.read_text();r=re.search(rf'EIG x={x} X={x} N={N} epsE=([^ ]+)',s)
        vals.append(float(r[1]))
    if len(vals)==2:
        rate=math.log10(vals[0]/vals[1])/37
        rows.append((D,rate))
assert len(rows)==10,'Wait for all ten completed x50 outputs'
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42,'figure.dpi':140})
fig,ax=plt.subplots(1,2,figsize=(10,4),layout='constrained')
K=math.log10(50/13)/37
for D,s in rows:
    k=D<0;color='#b34b31' if k else '#246d97';mark='s' if k else 'o'
    ax[0].scatter(1/abs(D),s,color=color,marker=mark,s=48,zorder=3)
    ax[0].annotate(str(D),(1/abs(D),s),xytext=(4,4),textcoords='offset points',fontsize=8)
    # Correcting by the heuristic lowest-sector powers 1+kappa is explicitly labelled.
    ax[1].scatter(abs(D),abs(D)*(s+(1+int(k))*K),color=color,marker=mark,s=48,zorder=3)
    ax[1].annotate(str(D),(abs(D),abs(D)*(s+(1+int(k))*K)),xytext=(4,4),textcoords='offset points',fontsize=8)
xs=[0.04+i*.003 for i in range(105)]
for k,color,label in [(0,'#246d97','even character; heuristic b=1'),(1,'#b34b31','odd character; heuristic b=2')]:
    ax[0].plot(xs,[4*math.pi/math.log(10)*t-(1+k)*K for t in xs],color=color,lw=1,alpha=.65,label=label)
ax[0].set(xlabel=r'$1/|D|$',ylabel='Digits gained per unit x',title='Measured slopes, x = 13 to 50')
ax[0].legend(fontsize=8,loc='upper left')
ax[1].axhline(4*math.pi/math.log(10),color='black',lw=1,ls='--',label=r'$4\pi/\log 10$')
ax[1].set(xlabel='Conductor |D|',ylabel=r'$|D|[s+(1+\kappa)\log_{10}(50/13)/37]$',title='Conductor scaling plus heuristic power correction')
ax[1].legend(fontsize=8)
for a in ax:a.grid(alpha=.2)
fig.savefig(P/'conductor_rates.pdf',metadata={'Creator':'codex:gpt-6-astra','CreationDate':None,'ModDate':None})
fig.savefig(P/'conductor_rates.png',metadata={'Software':'codex:gpt-6-astra'})
