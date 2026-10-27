import os,sys
sys.dont_write_bytecode=True
P='/tmp/claude-1000/-home-tobias-Projects-riemann-channel/dcae8e10-414e-4cb4-8b95-d35e159cfb50/scratchpad/venv-astra/bin/python'
try: import cypari2
except ImportError: os.execv(P,[P,'-u',__file__])
from pizer_graph import pari
al=pari.alginit(pari.nfinit('y'),[-2,-37])
print('basis=',pari.algbasis(al))
print('disc=',pari.algdisc(al),'hassef=',pari.alghassef(al),'hassei=',pari.alghassei(al))
print('multable=',pari.algmultable(al))
for j in range(4):
    v=pari.Col([int(i==j) for i in range(4)])
    print('unit coord=',v,'norm=',pari.algnorm(al,v),'trace=',pari.algtrace(al,v))
L=pari.alglathnf(al,pari.matid(4))
print('L=',L,'transporter=',pari.alglatlefttransporter(al,L,L))
for name in ['qfminim','alglatlefttransporter','alglatelement']:
    print(name,getattr(pari,name).__doc__)
