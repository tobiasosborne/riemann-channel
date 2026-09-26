#!/usr/bin/env python3
"""Author codex:gpt-6-astra. Standalone scientific figure of measured rate fits."""
from pathlib import Path
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[4];dest=Path(__file__).resolve().parent
fig,ax=plt.subplots(2,2,figsize=(10,7),gridspec_kw={'height_ratios':[3,1.2]},layout='constrained')
for c,C,N,color in [('11a1',11,200,'#194c85'),('14a1',14,60,'#b64e1a')]:
    rows=[]
    for line in (root/f'outputs/rtp2_ellcurve_{c}_axisx_ccm_N{N}.txt').read_text().splitlines():
        if not line.startswith('EIG '):continue
        d=dict(re.findall(r'(\w+)=(\S+)',line))
        if float(d['x'])>=13:rows.append((float(d['x']),-np.log10(float(d['epsE']))))
    x,y=np.array(rows).T
    for j,v in enumerate([x,np.sqrt(x/C)]):
        X=np.column_stack([np.ones(len(x)),v]);p=np.linalg.lstsq(X,y,rcond=None)[0];r=y-X@p
        ax[0,j].plot(v,y,'o',ms=4,color=color,label=f'{c}, N={N}')
        ax[0,j].plot(v,X@p,'--',lw=1,color=color)
        ax[1,j].plot(v,r,'o-',ms=3,lw=.7,color=color,label=f'RMS {np.sqrt(np.mean(r*r)):.3f} digits')
for j,label in enumerate(['x',r'$\sqrt{x/C_E}$']):
    ax[0,j].set_xlabel(label);ax[1,j].set_xlabel(label)
    ax[0,j].set_ylabel(r'$-\log_{10}\epsilon_E$');ax[1,j].set_ylabel('residual (digits)')
    ax[1,j].set_ylim(-1.9,1.9);ax[1,j].axhline(0,color='.6',lw=.6)
    for i in range(2):ax[i,j].legend(fontsize=8);ax[i,j].grid(alpha=.2)
ax[0,0].set_title('Straight-line fit in x');ax[0,1].set_title('Straight-line fit in the predicted scale')
fig.suptitle('Weight-two dilation rate: certified eigenvalues, floating fits',fontsize=12)
for ext in ['png','pdf']:fig.savefig(dest/f'rate_fits.{ext}',dpi=180)
print('wrote rate_fits.png and rate_fits.pdf')
