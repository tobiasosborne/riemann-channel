import numpy as np, mpmath as mp
from sympy import factorint
zs=np.load('data/zeros3000.npy'); print('zeros:',len(zs),' largest gamma =',zs[-1])
G=float(zs[-1])/3.5          # Gaussian window width in gamma; sum is converged when exp(-(gamma_max/G)^2/2) << 1
print('window G =',G,'  truncation weight at gamma_max =',np.exp(-(zs[-1]/G)**2/2))
u=np.linspace(0.3,3.3,30001)
# F(u) = sum_{gamma>0} exp(-gamma^2/2G^2) cos(gamma u)   ==  (1/2) sum_{all gamma} ghat(gamma),  ghat(r)=cos(ru) exp(-r^2/2G^2)
F=np.array([np.sum(np.exp(-(zs/G)**2/2)*np.cos(zs*uu)) for uu in u])
# Explicit formula prediction: 2F(u) = -(G/sqrt(2pi)) sum_n Lambda(n) n^{-1/2} exp(-G^2 (u-log n)^2/2) + smooth(u)
def Lambda(n):
    f=factorint(n); return float(np.log(list(f)[0])) if len(f)==1 else 0.0
pred=np.zeros_like(u)
for n in range(2,40):
    L=Lambda(n)
    if L: pred+=-(G/np.sqrt(2*np.pi))*L/np.sqrt(n)*np.exp(-G**2*(u-np.log(n))**2/2)
# smooth terms: ghat(i/2)+ghat(-i/2) = 2 cosh(u/2) e^{1/(8G^2)};  -g(0) log pi;  (1/2pi) int ghat(r) Re psi(1/4+ir/2) dr
g0=G/(2*np.sqrt(2*np.pi))*2*np.exp(-G**2*u**2/2)   # g(0) for the two-sided gaussian at +-u
smooth=2*np.cosh(u/2)*np.exp(1/(8*G**2)) - g0*np.log(np.pi)
r=np.linspace(0,8*G,20001); dr=r[1]-r[0]
repsi=np.array([float(mp.re(mp.digamma(0.25+0.5j*rr))) for rr in r])
gam=np.array([2*np.sum(np.cos(r*uu)*np.exp(-(r/G)**2/2)*repsi)*dr/(2*np.pi) for uu in u])
total=(pred+smooth+gam)/2
print('\n n   log n    F(u_n) numeric   prediction   depth ratio F/pred   Lambda(n)/sqrt(n)')
for n in (2,3,4,5,7,8,9,11,13,16,17,19,23,25,27):
    i=np.argmin(abs(u-np.log(n)))
    print(f'{n:2d}  {np.log(n):.4f}   {F[i]:9.3f}      {total[i]:9.3f}      {F[i]/total[i]:.4f}          {Lambda(n)/np.sqrt(n):.4f}')
# global agreement away from dips
mask=np.ones_like(u,bool)
for n in range(2,40):
    if Lambda(n): mask&= abs(u-np.log(n))>4/G
print('\nmax |F-prediction| away from prime dips:',np.max(abs(F-total)[mask]),'   max |F| overall:',np.max(abs(F)))
print('max |F-prediction| everywhere:',np.max(abs(F-total)))
np.savez('data/ringnorm.npz',u=u,F=F,total=total)
