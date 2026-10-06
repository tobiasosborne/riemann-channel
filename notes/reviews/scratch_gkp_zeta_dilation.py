"""REFUTE lane, 2026-10-06: the prime-2 dilation on the window (zeta-ingredients.md G4: D2-D5), rebuilt from the statements.
Float64 rebuild of the window Weil form (same explicit formula as scratch_gkp_zeta_window.py, Gauss-Legendre panels);
cross-checked against the 50-digit build at N=5.  Step: normalised translation by a=log 2, compressed M_N=P_N chi_[0,L] U_a.
"""
import numpy as np, sys
EG=0.5772156649015329
xg,wg=np.polynomial.legendre.leggauss(30)
def integ(f,lo,hi,panels):
    e=np.linspace(lo,hi,panels+1); s=0
    for a,b in zip(e[:-1],e[1:]):
        u=(b-a)/2*xg+(a+b)/2; s=s+np.sum(wg*f(u))*(b-a)/2
    return s
def vm(N):
    lam={}
    for p in range(2,N+1):
        if all(p%d for d in range(2,int(p**.5)+1)):
            q=p
            while q<=N: lam[q]=np.log(p); q*=p
    return lam
def Zfun(gfun,ell,lam,panels=400):
    """Weil's form on g(t), g supported in [-ell,ell] (gfun vectorised, complex)."""
    pole=integ(lambda t:gfun(t)*2*np.cosh(t/2),-ell,ell,2*panels)
    prime=sum(l/np.sqrt(n)*(gfun(np.array([np.log(n)]))[0]+gfun(np.array([-np.log(n)]))[0]) for n,l in lam.items() if np.log(n)<ell)
    g0=gfun(np.array([0.0]))[0]
    arch=-(EG+np.log(np.pi))*g0+integ(lambda u:(2*np.exp(-2*u)*g0-np.exp(-u/2)*(gfun(u)+gfun(-u)))/(-np.expm1(-2*u)),1e-300,ell,panels)\
         -g0*np.log(-np.expm1(-2*ell))
    return pole-prime+arch
def window_Z(x,N):
    L=np.log(x); lam=vm(int(x)); b=lambda k:2*np.pi*k/L; P=max(400,8*N)
    R={}
    for k in range(0,2*N+1):
        C=integ(lambda u:np.sin(b(k)*u)*2*np.cosh(u/2),0,L,P)
        T=sum(l/np.sqrt(n)*np.sin(b(k)*np.log(n)) for n,l in lam.items())
        S=integ(lambda u:np.exp(-u/2)*np.sin(b(k)*u)/(-np.expm1(-2*u)),1e-300,L,P)
        R[k]=C-T-S; R[-k]=-R[k]
    idx=np.arange(-N,N+1); n=len(idx); Z=np.zeros((n,n))
    D={}
    for m in range(N+1):
        gp=lambda u:2*(1-u/L)*np.cos(b(m)*u)
        pole=integ(lambda u:gp(u)*2*np.cosh(u/2),0,L,P)
        prime=sum(l/np.sqrt(nn)*gp(np.log(nn)) for nn,l in lam.items())
        arch=-(EG+np.log(np.pi))+integ(lambda u:(2*np.exp(-2*u)-np.exp(-u/2)*gp(u))/(-np.expm1(-2*u)),1e-300,L,P)-np.log(-np.expm1(-2*L))
        D[m]=pole-prime+arch
    for i,m in enumerate(idx):
        for j,k in enumerate(idx):
            Z[i,j]=D[abs(m)] if m==k else (R[k]-R[m])/(np.pi*(m-k))
    return Z,L,idx,lam
def compress(L,idx,a):
    b=2*np.pi*idx/L; n=len(idx); M=np.zeros((n,n),complex)
    for i in range(n):
        for j in range(n):
            d=b[j]-b[i]
            I=(L-a) if i==j else (np.exp(1j*d*L)-np.exp(1j*d*a))/(1j*d)
            M[i,j]=np.exp(-1j*b[j]*a)*I/L
    return M
def resid(A,G):
    c=np.real(np.vdot(G,A))/np.real(np.vdot(G,G))
    return c,np.linalg.norm(A-c*G)/np.linalg.norm(G),np.linalg.norm(A-c*G)/np.linalg.norm(A)
def cutlimit(L,lam,a,ms):
    """W(chi U_a e_m, chi U_a e_n) = Weil form of e^{-i b_m a} e_m 1_[a,L] against the same for n."""
    b=lambda k:2*np.pi*k/L; s,e=a,L; ell=e-s
    W=np.zeros((len(ms),len(ms)),complex)
    for i,m in enumerate(ms):
        for j,k in enumerate(ms):
            al,be=b(m),b(k); d=al-be
            I=(lambda lo,hi:(hi-lo)) if abs(d)<1e-14 else (lambda lo,hi:(np.exp(1j*d*hi)-np.exp(1j*d*lo))/(1j*d))
            def g(t,al=al,I=I):
                t=np.atleast_1d(t); out=np.zeros(t.shape,complex)
                pos=(t>=0)&(t<=ell); neg=(t<0)&(t>=-ell)
                out[pos]=np.exp(1j*al*t[pos])*I(s,e-t[pos]); out[neg]=np.exp(1j*al*t[neg])*I(s-t[neg],e)
                return out/L
            W[i,j]=np.exp(-1j*b(m)*a)*np.conj(np.exp(-1j*b(k)*a))*Zfun(g,ell,lam)
    return W
if __name__=="__main__":
    a=np.log(2)
    for x in [13,100]:
        print(f"x={x}  log2/L={a/np.log(x):.3f}")
        for N in [5,10,20,40,80,160]:
            Z,L,idx,lam=window_Z(x,N)
            M=compress(L,idx,a); A=M.conj().T@Z@M
            c,r1,r2=resid(A,Z)
            sv=np.linalg.svd(M,compute_uv=False)
            lo=np.abs(idx)<=3; Al=A[np.ix_(lo,lo)]
            extra=""
            if N==5: extra=f" min eig Z={np.linalg.eigvalsh(Z)[0]:.2e} (50-digit: 7.13e-17 at x=13)"
            print(f"  N={N:3d} n={len(idx)}: best c={c:.3f} resid/|G|={r1:.3f} resid/|A|={r2:.3f}; #sv<1/2={np.sum(sv<0.5)} vs n a/L={len(idx)*a/L:.1f}; sv_min={sv.min():.1e}{extra}",flush=True)
            if N in (20,160):
                if N==20: Wl=cutlimit(L,lam,a,list(range(-3,4)))
                print(f"     low modes |n|<=3: |A_low - W_cut|_F={np.linalg.norm(Al-Wl.T):.2e}; cut limit best-c resid/|G_low|={resid(Wl,Z[np.ix_(lo,lo)])[1]:.3f} c={resid(Wl,Z[np.ix_(lo,lo)])[0]:.3f}")
        # D5: smooth bump supported in [0.1, L-a-0.1], c=1 residual
        for N in [20,80,160]:
            Z,L,idx,lam=window_Z(x,N); M=compress(L,idx,a)
            u=np.linspace(0,L,20001); lo_,hi_=0.1,L-a-0.1
            h=np.where((u>lo_)&(u<hi_),np.exp(-1/np.maximum((u-lo_)*(hi_-u),1e-3)),0)*np.cos(3*u)
            coef=np.array([np.trapezoid(h*np.exp(-2j*np.pi*k*u/L),u)/np.sqrt(L) for k in idx])
            v=M@coef
            print(f"  smooth bump, N={N}: |Z(Mh,Mh)/Z(h,h)-1| = {abs(np.vdot(v,Z@v).real/np.vdot(coef,Z@coef).real-1):.1e}")
