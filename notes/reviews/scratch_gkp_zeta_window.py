"""REFUTE lane, 2026-10-06: independent rebuild of the windowed Weil form of zeta-ingredients.md (statements G4, G5).
Written from the statements only. Weil's form on [0,L], L=log x, basis e_m=exp(2 pi i m u/L)/sqrt L, |m|<=N:
  Z(f,k) = sum_gamma F(gamma) conj K(gamma),  F(r)=int f(u) e^{iru} du,
evaluated by the explicit formula (validated in ef_test: Gaussians agree with the 3000-zero sum to 15 digits):
  Z(g) = ghat(i/2)+ghat(-i/2) - sum Lambda(n) n^{-1/2} (g(log n)+g(-log n))
         - (gamma_E+log pi) g(0) + int_0^inf [2e^{-2u}g(0) - e^{-u/2}(g(u)+g(-u))]/(1-e^{-2u}) du,
  g(t)=int f(t+v) conj k(v) dv.  For window Fourier modes g is closed form, so Z_mn=(R_n-R_m)/(pi(m-n)) off the diagonal.
"""
import numpy as np, mpmath as mp, sys
ZE=np.load('/home/user/riemann-channel/data/zeros3000.npy')
def vm(N):
    lam={}
    for p in range(2,N+1):
        if all(p%d for d in range(2,int(p**.5)+1)):
            q=p
            while q<=N: lam[q]=mp.log(p); q*=p
    return lam
def window(x,N,dps):
    mp.mp.dps=dps
    x=mp.mpf(x); L=mp.log(x); lam=vm(int(x))
    b=lambda k: 2*mp.pi*k/L
    def arch_odd(k):  # S_k
        if k==0: return mp.mpf(0)
        return mp.quad(lambda u: mp.e**(-u/2)*mp.sin(b(k)*u)/(1-mp.e**(-2*u)), mp.linspace(0,L,8))
    def pole_odd(k):  # C_k = int_0^L sin(b u) 2cosh(u/2)
        return mp.quad(lambda u: mp.sin(b(k)*u)*2*mp.cosh(u/2), mp.linspace(0,L,8))
    def prime_odd(k):
        return sum(l/mp.sqrt(n)*mp.sin(b(k)*mp.log(n)) for n,l in lam.items())
    R={}
    for k in range(0,2*N+1):
        R[k]=pole_odd(k)-prime_odd(k)-arch_odd(k); R[-k]=-R[k]
    def diag(m):
        gp=lambda u: 2*(1-u/L)*mp.cos(b(m)*u)
        pole=mp.quad(lambda u: gp(u)*2*mp.cosh(u/2), mp.linspace(0,L,8))
        prime=sum(l/mp.sqrt(n)*gp(mp.log(n)) for n,l in lam.items())
        arch=-(mp.euler+mp.log(mp.pi))+mp.quad(lambda u:(2*mp.e**(-2*u)-mp.e**(-u/2)*gp(u))/(1-mp.e**(-2*u)),mp.linspace(0,L,8))\
             +mp.quad(lambda u:2*mp.e**(-2*u)/(1-mp.e**(-2*u)),[L,mp.inf])
        return pole-prime+arch
    idx=list(range(-N,N+1)); n=len(idx)
    Z=mp.matrix(n,n)
    D={m:diag(m) for m in range(0,N+1)}
    for i,m in enumerate(idx):
        for j,k in enumerate(idx):
            Z[i,j]=D[abs(m)] if m==k else (R[k]-R[m])/(mp.pi*(m-k))
    # pole form from the closed-form transforms F_m(+-i/2)
    F=lambda m,r: (mp.e**(1j*(b(m)+r)*L)-1)/(1j*(b(m)+r)*mp.sqrt(L))
    P=mp.matrix(n,n)
    for i,m in enumerate(idx):
        for j,k in enumerate(idx):
            P[i,j]=F(m,0.5j)*mp.conj(F(k,-0.5j))+F(m,-0.5j)*mp.conj(F(k,0.5j))
    return Z,P,L,idx,F,b
def inertia(A,tol):
    e=mp.eighe(A)[0] if False else mp.eigh(A,eigvals_only=True)
    e=[mp.re(v) for v in e]
    return sum(v>tol for v in e),sum(v<-tol for v in e),sum(abs(v)<=tol for v in e),min(e),e
if __name__=="__main__":
    out=[]
    for N in [int(a) for a in (sys.argv[1:] or [5,10,15])]:
        Z,P,L,idx,F,b=window(13,N,50)
        n=len(idx)
        pZ,nZ,zZ,mZ,eZ=inertia(Z,mp.mpf(10)**-40)
        pP,nP,zP,_,_=inertia(P,mp.mpf(10)**-30)
        a1=inertia(Z-P,mp.mpf(10)**-40); a2=inertia(Z+P,mp.mpf(10)**-40)
        print(f"x=13 N={N} n={n}: lam_min(Z)={mp.nstr(mZ,3)} inertia Z=({pZ},{nZ},{zZ}) P=({pP},{nP},{zP}) "
              f"Z-P=({a1[0]},{a1[1]},{a1[2]}) lam-={mp.nstr(a1[3],5)}  Z+P=({a2[0]},{a2[1]},{a2[2]}) lam-={mp.nstr(a2[3],5)}",flush=True)
        if N==5:
            # zero-side check of the diagonal: 3000 zeros + smooth Riemann-von Mangoldt tail
            T=ZE[-1]
            for m in [0,3]:
                s=sum(abs(F(m,mp.mpf(g)))**2+abs(F(m,-mp.mpf(g)))**2 for g in ZE)
                tail=mp.quad(lambda t:(abs(F(m,t))**2+abs(F(m,-t))**2)*mp.log(t/(2*mp.pi))/(2*mp.pi),[T,10*T,mp.inf])
                print(f"   diag m={m}: explicit formula {mp.nstr(Z[idx.index(m),idx.index(m)],12)}  zeros+tail {mp.nstr(s+tail,12)}  (zeros only {mp.nstr(s,8)})")
            # Loewner: Omega=Z(., D^{-1} .) on mean-zero modes, D^{-1}e_k=(e_k-e_0)/(i b_k)
            i0=idx.index(0); nz=[i for i in range(n) if i!=i0]
            Om=mp.matrix(n-1,n-1)
            for r,i in enumerate(nz):
                for c,j in enumerate(nz):
                    Om[r,c]=(Z[i,j]-Z[i,i0])*mp.conj(1/(1j*b(idx[j])))
            print("   Loewner: max|Om+Om^H| =",mp.nstr(max(abs(v) for v in (Om+Om.H)),3)," max|Om| =",mp.nstr(max(abs(v) for v in Om),3))
        if N==10:
            for rho in [mp.mpc(0.75,5),mp.mpc(0.6,14.13)]:
                rs=[-1j*(r-0.5) for r in [rho,mp.conj(rho),1-rho,1-mp.conj(rho)]]
                Q=mp.matrix(n,n)
                for i,m in enumerate(idx):
                    for j,k in enumerate(idx):
                        Q[i,j]=sum(F(m,r)*mp.conj(F(k,mp.conj(r))) for r in rs)
                q1=inertia(Z+Q,mp.mpf(10)**-40); q2=inertia(Z+Q-P,mp.mpf(10)**-40); q3=inertia(Q,mp.mpf(10)**-30)
                print(f"   quartet rho={mp.nstr(rho,4)}: Q inertia ({q3[0]},{q3[1]},{q3[2]}); Z+Q ({q1[0]},{q1[1]},{q1[2]}); Z+Q-P ({q2[0]},{q2[1]},{q2[2]})")
