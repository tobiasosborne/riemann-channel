"""REFUTE lane, 2026-10-06: validation of the explicit-formula convention used by scratch_gkp_zeta_window.py and _dilation.py
(Gaussian tests of width 0.1, 0.2, 0.3 against the 3000-zero sum; agreement to 15 digits)."""
import numpy as np, mpmath as mp
mp.mp.dps=30
Z=np.load('/home/user/riemann-channel/data/zeros3000.npy')
def vmtab(N):
    lam=np.zeros(N+1); isp=np.ones(N+1,bool); isp[:2]=False
    for p in range(2,N+1):
        if isp[p]:
            isp[2*p::p]=False; q=p
            while q<=N: lam[q]=np.log(p); q*=p
    return lam
for sig in [0.1,0.2,0.3]:
    sig=mp.mpf(sig)
    g=lambda u: mp.e**(-u**2/(2*sig**2))
    gh=lambda r: sig*mp.sqrt(2*mp.pi)*mp.e**(-sig**2*r**2/2)
    zs=2*sum(gh(mp.mpf(t)) for t in Z)
    pole=2*sig*mp.sqrt(2*mp.pi)*mp.e**(sig**2/8)
    N=int(float(mp.e**(11*sig)))+2; lam=vmtab(N)
    prime=sum(mp.mpf(lam[n])/mp.sqrt(n)*2*g(mp.log(n)) for n in range(2,N+1) if lam[n]>0)
    arch=-(mp.euler+mp.log(mp.pi))*g(0)+mp.quad(lambda u:(2*mp.e**(-2*u)*g(0)-mp.e**(-u/2)*2*g(u))/(1-mp.e**(-2*u)),[0,sig,1,10,mp.inf])
    print(float(sig), mp.nstr(zs,15), mp.nstr(pole-prime+arch,15))
