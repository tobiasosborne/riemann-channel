# Author: codex:gpt-6-astra
"""Independent Gaussian quadrature and local-factor checks; stdout only."""
import sys
sys.dont_write_bytecode = True
from verify import *
import numpy as np

y=mp.mpf('1.3');t=mp.mpf('.7')
for q,k in [(5,2),(5,1),(7,2),(13,2)]:
    c=character(q,k)
    x=np.arange(512)/512
    ns=np.arange(-100,101)
    cs=np.array([complex(c[int(n)%q]) for n in ns])
    incoming=np.zeros(len(x),complex)
    outgoing=np.zeros(len(x),complex)
    for m in range(-18,19):
        incoming += np.exp(-np.pi*float(t)*((q*m*x[:,None]+ns[None,:])**2+(q*m*float(y))**2)/(q*float(y)))@cs
        outgoing += complex(c[m%q])*np.exp(-np.pi*float(t)*((m*x[:,None]+ns[None,:])**2+(m*float(y))**2)/float(y)).sum(axis=1)
    ct1=theta(t/y,c)
    ct2=mp.sqrt(y/t)*theta(q*t*y,c)
    errs=(abs(np.mean(incoming)-complex(ct1)),abs(np.mean(outgoing)-complex(ct2)))
    print('physical_CT',q,k,show(ct1),show(ct2),'independent_errors',errs)
    assert max(errs)<2e-14

for q in (5,7,11,13):
    for w in (mp.mpc('.2','.4'),mp.mpc('2','.3')):
        s=mp.mpf('.5')+1j*w
        ph=phi0(s,q)
        pp,pm=ph[0,0]+ph[0,1],ph[0,0]-ph[0,1]
        u=mp.exp(1j*w*mp.log(q));a=1/mp.sqrt(q)
        lp=u*(u+a)/(1+a*u);lm=u*(u-a)/(1-a*u)
        r=(w-.5j)/(w+.5j)
        def xi(v):return v*(v-1)*mp.pi**(-v/2)*mp.gamma(v/2)*mp.zeta(v)/2
        th=xi(1+2j*w)/xi(1-2j*w)
        err=max(abs(1/pp-th*lp/r),abs(1/pm-th*lm/r))
        assert err<mp.mpf('1e-37')
        assert abs(th*lp)<1 and abs(th*lm/r)<1
    print('local_inner_and_matrix_identities',q,'PASS')

x=sp.symbols('x')
for p in (2,3):
    pol=sp.expand(sum((x-p)**j for j in range(5))*((x-1)**5-p**5))
    print('Eis_characteristic_N11_p',p,pol)
print('PASS: independent theta integration, local factorization, and strict innerness at sample points.')
