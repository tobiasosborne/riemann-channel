# Author: codex:gpt-6-astra
"""Independent elementary checks for T1/T2, T6 and T7."""
import numpy as np
import mpmath as mp
from scipy.linalg import expm
from scipy.integrate import quad
mp.mp.dps=40
count=0
def ck(a,b,tol=2e-11):
    global count
    assert np.max(np.abs(np.asarray(a)-np.asarray(b)))<tol,(a,b)
    count+=1

gam=np.array([float(mp.im(mp.zetazero(k))) for k in (1,2,3)])
d=-.25-.5j*gam
G=1/(-(d[:,None]+d.conj()[None,:]))
ck(-(d[:,None]+d.conj()[None,:])*G,np.ones((3,3)))
cyc=np.prod([-(d[i]+d[j].conjugate()) for i,j in ((0,1),(1,2),(2,0))])
print('gammas', [mp.nstr(mp.im(mp.zetazero(k)),25) for k in (1,2,3)])
print('Cauchy Gram',G)
print('cyclic prefactor',cyc)
ck(cyc.imag,-np.prod([(gam[i]-gam[j])/2 for i,j in ((0,1),(1,2),(2,0))]))
# Nonzero exit data on a synthetic length-two chain.
z=-.3+.7j;c=np.array([1+.4j,.2-.3j]);
f=lambda k,t: np.exp(z*t)*(c[k]+(t*c[0]/2 if k==1 else 0))
JG=np.empty((2,2),complex)
for k in range(2):
    for l in range(2):
        val=lambda t:f(k,t)*np.conj(f(l,t))
        JG[k,l]=quad(lambda t:val(t).real,0,np.inf)[0]+1j*quad(lambda t:val(t).imag,0,np.inf)[0]
N=-(z+z.conjugate())*JG
N[1,:]-=.5*JG[0,:];N[:,1]-=.5*JG[:,0]
ck(N,np.outer(c,c.conj()))
# T7 matrices, all reset laws, physical holding means.
b=.25;A=np.array([[-b,-2*b],[0,-b]]);j=np.sqrt(2*b)*np.ones((1,2))
ck(-(A+A.T),j.T@j)
for p,cx in ((1,0),(0,0),(.5,.5),(.4,.2+.1j)):
    Om=np.array([[p,cx],[np.conj(cx),1-p]])
    for t in (0,.5,1,4,7):
        C=expm(t*A)
        ck(C,np.exp(-b*t)*np.array([[1,-2*b*t],[0,1]]))
        S=np.trace(C@Om@C.T).real
        m=(j@C@Om@C.T@j.T)[0,0].real
        ck(S,np.exp(-2*b*t)*(1-4*b*t*np.real(cx)+4*b*b*t*t*(1-p)))
        ck(m,2*b*np.exp(-2*b*t)*(p+(1-p)*(1-2*b*t)**2+2*np.real(cx)*(1-2*b*t)))
    mean=quad(lambda t:np.trace(expm(t*A)@Om@expm(t*A.T)).real,0,np.inf)[0]
    ck(mean,(1+2*(1-p)-2*np.real(cx))/(2*b))
ck(A/2+A.T/2+np.trace(j@(.5*np.eye(2))@j.T)*(.5*np.ones((2,2))),np.zeros((2,2)))
t=1;D=np.eye(2)-expm(A.T*t)@expm(A*t)
ck(np.linalg.det(D),(1-np.exp(-2*b*t))**2-(2*b*t)**2*np.exp(-2*b*t))
print('T7 finite loss t=1',D,'eigenvalues',np.linalg.eigvalsh(D))
print('T7 exit reset S(1), m(1)',np.exp(-.5)*.625,np.exp(-.5)*.75**2)
# T6 modal and coherent resets, forward convention.
ds=np.array([-.1+.75j,-.2-1.25j]);alpha=-(ds[:,None]+ds.conj()[None,:]);gg=1/alpha
u=np.array([1,.3+.2j]);q=np.outer(u,u.conj());q/=np.sum(q*gg).real
mean=np.sum(q/alpha**2).real
ck(mean,quad(lambda t:np.sum(q/alpha*np.exp(-alpha*t)).real,0,np.inf,epsabs=1e-12,epsrel=1e-12,limit=500)[0])
ck(1,quad(lambda t:np.sum(q*np.exp(-alpha*t)).real,0,np.inf,epsabs=1e-12,epsrel=1e-12,limit=500)[0])
for h in (.3,1):
    zz=(1+h*ds)/(1-h*ds)
    ck(1/(1-abs(zz)**2),abs(1-h*ds)**2/(-4*h*ds.real))
print('T6 coherent mean',mean,'q',q)
print('checks passed',count)
