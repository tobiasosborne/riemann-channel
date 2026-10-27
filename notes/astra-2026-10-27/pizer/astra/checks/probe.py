import os, sys
sys.dont_write_bytecode = True
try:
    from cypari2 import Pari
except ImportError:
    os.execv('/tmp/claude-1000/-home-tobias-Projects-riemann-channel/dcae8e10-414e-4cb4-8b95-d35e159cfb50/scratchpad/venv-astra/bin/python', ['/tmp/claude-1000/-home-tobias-Projects-riemann-channel/dcae8e10-414e-4cb4-8b95-d35e159cfb50/scratchpad/venv-astra/bin/python', '-u', __file__])
pari=Pari()
pari.allocatemem(256000000, silent=True)
for name in ['ellisogeny','ellisogenyapply','elldivpol','ffembed','ffmap','algbasis','algdisc','algnorm','algtrace','alglathnf','alglatrighttransporter','alginit']:
    method=getattr(pari,name,None)
    print('\nFUNCTION',name)
    print((method.__doc__ or '')[:14000] if method else 'absent')
print('TEST ff',pari('ffgen(ffinit(37,2),t)'))
print('TEST eigenbasis', pari('mfeigenbasis(mfinit([37,2],1))'))
print('TEST Hecke', pari('mfheckemat(mfinit([37,2],1),2)'))
