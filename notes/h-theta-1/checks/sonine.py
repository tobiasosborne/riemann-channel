# Author: codex:gpt-6-astra
"""Cosine L_1 evaluator Gram, via an anchor kernel and a compact resolvent.
All writes are confined to the authorized notebook; this script prints results.
"""
import numpy as np
import mpmath as mp
from scipy.special import roots_legendre, eval_sh_legendre
mp.mp.dps=45

def build(n, anchor=2):
    anchor=mp.mpf(anchor)
    z,w=roots_legendre(n); x=(z+1)/2; w=w/2
    rt=np.sqrt(w); Q=np.eye(n)-np.outer(rt,rt)
    C=2*np.cos(2*np.pi*np.outer(x,x))*np.outer(rt,rt)
    T=Q@C@Q
    def chi(s): return mp.power(mp.pi,s-mp.mpf('.5'))*mp.gamma((1-s)/2)/mp.gamma(s/2)
    def smooth(s,x):
        return mp.sin(2*mp.pi*x)/(mp.pi*x)/(1-s)-2*mp.fsum([(-1)**k*(2*mp.pi*x)**(2*k)/mp.factorial(2*k)/(2*k+1-s) for k in range(40)])
    r2=np.array([float(smooth(anchor,mp.mpf(float(t)))+chi(anchor)*mp.mpf(float(t))**(anchor-1)) for t in x])*rt
    v=np.linalg.solve(np.eye(n)-T@T,Q@r2)
    vv=v/rt
    coeff=np.array([(2*k+1)*np.dot(w*vv,eval_sh_legendre(k,x)) for k in range(n)])
    coeff[0]=0
    # For the smooth anchor solution, high-degree coefficients are roundoff.
    cut=min(n,24)
    def integral(s):
        moment=1/s; ans=mp.mpc(0)
        for k in range(cut):
            if k: moment*= (s-k)/(s+k)
            ans+=mp.mpf(float(coeff[k]))*moment
        regular=mp.fsum(mp.mpf(float(w[k]*vv[k]))*smooth(s,mp.mpf(float(x[k]))) for k in range(n))
        return chi(s)*ans+regular
    def raw(s): return 1/((1-s)*(1-anchor))+1/(s+anchor-1)-integral(s)
    def p(s):return s*(s-1)
    def m(s):return mp.power(mp.pi,-s/2)*mp.gamma(s/2)
    def KF(s):return p(s)*p(anchor)*m(s)*m(anchor)*raw(s)
    aa=mp.sqrt((2*anchor-1)*KF(anchor))
    def E(s):return (s+anchor-1)*KF(s)/aa
    def ratio(s):return E(1-s)/E(s)
    def gram(s,t):
        # G_ij uses s=conj(rho_i), t=rho_j.
        if abs(s+t-1)<mp.mpf('1e-35'):
            num=E(s)*mp.diff(E,t)+E(1-s)*mp.diff(E,1-t)
            return num/(p(s)*p(t))
        return (E(s)*E(t)-E(1-s)*E(1-t))/((s+t-1)*p(s)*p(t))
    return E,ratio,gram,np.linalg.eigvalsh(T),coeff

if __name__=='__main__':
    for n,anchor in ((24,2),(40,2),(64,2),(40,4)):
        E,R,G,ev,cf=build(n,anchor)
        zeros=[mp.zetazero(k) for k in (1,2,3)]
        mat=mp.matrix([[G(mp.conj(s),t) for t in zeros] for s in zeros])
        diag=[mp.sqrt(mp.re(mat[k,k])) for k in range(3)]
        norm=np.array([[complex(mat[i,j]/diag[i]/diag[j]) for j in range(3)]for i in range(3)])
        ds=np.array([complex((mp.conj(s)-1)/2) for s in zeros])
        loss=-(ds[:,None]+ds.conj()[None,:])*norm
        print('n',n,'anchor',anchor,'T eigen range',ev[0],ev[-1], 'max tail coeff',max(abs(cf[20:])))
        print('E ratios',[mp.nstr(R(s),16) for s in zeros])
        print('Gram',mp.nstr(mat,13));print('normalized Gram',norm)
        print('normalized loss eig',np.linalg.eigvalsh(loss))
