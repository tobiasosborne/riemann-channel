#!/usr/bin/env python3
"""MVP-3 independent formula checks and mpmath spectra.

Sources: astra-review.md formula sheet; mc2arXiv.tex lines 449-495,
698-771, 817-936. Uses parent block builders, not its zeta data builder.
Run e.g. python3 -u ell_check.py checks; python3 -u ell_check.py spectrum 11a1 13 60 90.
These are floating point checks, NOT interval certificates.
"""
import sys
sys.dont_write_bytecode=True
import json
import time
from pathlib import Path
from mpmath import mp
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import ccm_proto as parent

HERE=Path(__file__).resolve().parent
def fmt(x,n=35): return mp.nstr(x,n)

def integrals(n,L,d,mu):
    d,mu=mp.mpf(d),mp.mpf(mu)
    w=2*mp.pi*n/L; A=(mu-1j*w)/d; a=mu/d
    z=mp.exp(-d*L); e=mp.exp(-mu*L)
    K=int(mp.ceil((mp.dps+10)*mp.log(10)/(d*L)))+5
    S1=S2=mp.mpc(0); S10=mp.mpf(0); zk=mp.mpf(1)
    for k in range(K):
        S1+=zk/(k+A); S2+=zk/(k+A)**2; S10+=zk/(k+a); zk*=z
    I1=-(mp.im(mp.digamma(A))+e*mp.im(S1))/d
    I2=mp.re(mp.polygamma(1,A)-e*S2)/d**2-e*L*mp.re(S1)/d
    I3=(mp.digamma(a)-mp.re(mp.digamma(A))-e*mp.re(S1)+e*S10)/d
    return I1,I2,I3

def tail(L,d,mu):
    return mp.exp(-mu*L)/d*mp.lerchphi(mp.exp(-d*L),1,mu/d)

def gamma_shift(L,d,mu,logQ):
    return 2*logQ+2*mp.digamma(mu/d)/d+2*tail(L,d,mu)

def point_ap(a,p):
    a1,a2,a3,a4,a6=a
    return p-sum((y*y+a1*x*y+a3*y-x*x*x-a2*x*x-a4*x-a6)%p==0
                 for x in range(p) for y in range(p))

def atoms(model,conductor,X,wrong=False,drop_bad=False):
    pp=[]
    for p in range(2,X+1):
        if any(p%q==0 for q in range(2,int(p**.5)+1)): continue
        ap=point_ap(model,p); good=conductor%p!=0
        if drop_bad and not good: continue
        prev,cur=2,ap; m=1; pm=p
        while pm<=X:
            raw=cur if good else ap**m
            # raw is alpha^m+beta^m in arithmetic normalisation.
            weight=-mp.mpf(raw)*mp.log(p)/(mp.sqrt(pm) if wrong else pm)
            pp.append((mp.log(pm),weight,p,m,raw))
            prev,cur=cur,ap*cur-p*prev
            m+=1; pm*=p
    return pp

def build(name,X,N,wrong=False,drop_bad=False):
    ref=json.loads((HERE/'pari_refs.json').read_text())['curves'][name]
    C=ref['conductor']; L=mp.log(X)
    pp=atoms(ref['model'],C,int(X),wrong,drop_bad)
    shift=mp.log(C)-2*mp.log(2*mp.pi)-2*mp.euler-2*mp.log1p(-mp.exp(-L))
    a=[]; b=[]
    for n in range(N+1):
        I1,I2,I3=integrals(n,L,1,1); w=2*mp.pi*n/L
        a.append(-2*(I3-I2/L)+shift+2*sum(wt*(1-y/L)*mp.cos(w*y) for y,wt,*_ in pp))
        b.append(I1/mp.pi-sum(wt*mp.sin(w*y) for y,wt,*_ in pp)/mp.pi)
    b[0]=mp.mpf(0)
    return L,a,b,pp,ref

def checks():
    mp.dps=70
    print('mpmath dps=',mp.dps)
    worst=mp.mpf(0)
    for L in [mp.log(8),mp.log(13)]:
        for d,mu in [(mp.mpf(1),mp.mpf(1)),(mp.mpf(2),mp.mpf('.5'))]:
            rho=lambda y:mp.exp(-mu*y)/(-mp.expm1(-d*y))
            for n in [1,3]:
                w=2*mp.pi*n/L
                I=integrals(n,L,d,mu)
                J=[mp.quad(lambda y:mp.sin(w*y)*rho(y),[0,L]),
                   mp.quad(lambda y:y*mp.cos(w*y)*rho(y),[0,L]),
                   mp.quad(lambda y:-2*mp.sin(w*y/2)**2*rho(y),[0,L])]
                err=max(abs(i-j) for i,j in zip(I,J)); worst=max(worst,err)
                print('I123 quadrature L=',fmt(L,12),'d,mu=',d,mu,'n=',n,'errors=',[fmt(abs(i-j),5) for i,j in zip(I,J)])
                assert err<mp.mpf('1e-60')
        for n in [0,1,3]:
            E=integrals(n,L,1,1); R1=integrals(n,L,2,1); R2=integrals(n,L,2,2)
            err=max(abs(a-b-c) for a,b,c in zip(E,R1,R2))
            print('duplication I123 n=',n,'error=',fmt(err,5)); assert err<mp.mpf('1e-60')
        zshift=gamma_shift(L,mp.mpf(2),mp.mpf('.5'),-mp.log(mp.pi)/2)
        err=abs(zshift+2*(parent.w_of_L(L)+parent.C_of_L(L)))
        print('zeta shift vs implemented -2(w+C):',fmt(err,5)); assert err<mp.mpf('1e-60')
        eshift=gamma_shift(L,mp.mpf(1),mp.mpf(1),-mp.log(2*mp.pi))
        edup=gamma_shift(L,mp.mpf(2),mp.mpf(1),-mp.log(mp.pi)/2)+gamma_shift(L,mp.mpf(2),mp.mpf(2),-mp.log(mp.pi)/2)
        print('duplication shift:',fmt(abs(eshift-edup),5)); assert abs(eshift-edup)<mp.mpf('1e-60')
        # Build zeta from generic gamma data plus the same pole and atom formulas.
        _,za,zb=parent.build_ab(mp.exp(L/2),4)
        K=32*L*mp.sinh(L/4)**2
        for n in range(5):
            I1,I2,I3=integrals(n,L,2,mp.mpf('.5')); w=2*mp.pi*n/L
            den=L*L+16*mp.pi**2*n*n
            aa=-2*(I3-I2/L)+zshift+K*(L*L-16*mp.pi**2*n*n)/den**2
            bb=I1/mp.pi+K*n/den
            for k,lk in parent.prime_powers(int(mp.nint(mp.exp(L)))):
                aa-=2*lk/mp.sqrt(k)*(1-mp.log(k)/L)*mp.cos(w*mp.log(k))
                bb+=lk/mp.sqrt(k)*mp.sin(w*mp.log(k))/mp.pi
            assert max(abs(aa-za[n]),abs(bb-zb[n]))<mp.mpf('1e-60')
        print('generic zeta a,b n=0..4: PASS')
    # Direct defining distribution, including endpoint subtraction and tail.
    for X in [8,13]:
        L,a,b,pp,ref=build('11a1',X,4)
        s=mp.log(ref['conductor'])-2*mp.log(2*mp.pi)-2*mp.euler-2*mp.log1p(-mp.exp(-L))
        for n,m in [(0,0),(1,1),(3,3),(0,1),(1,3),(-2,3)]:
            def q(y):
                if n==m: return 2*(1-y/L)*mp.cos(2*mp.pi*n*y/L)
                return (mp.sin(2*mp.pi*m*y/L)-mp.sin(2*mp.pi*n*y/L))/(mp.pi*(n-m))
            q0=q(mp.mpf(0))
            val=s*q0/2-mp.quad(lambda y:(q(y)-q0)/mp.expm1(y),[0,L])+sum(wt*q(y) for y,wt,*_ in pp)
            err=abs(val-parent.tau_entry(a,b,n,m))
            print('ell tau quadrature X,n,m=',X,n,m,'error=',fmt(err,5)); assert err<mp.mpf('1e-60')
    print('ALL FORMULA CHECKS PASS; maximum I123 quadrature error=',fmt(worst,8))

def low_roots(xi,N,smax):
    # Search independently of PARI zeros. Include a logarithmic mesh by 0.
    def g(s): return -xi[0]/s+2*s*sum(xi[j]/(j*j-s*s) for j in range(1,N+1))
    roots=[]; eps=mp.power(10,-mp.dps//2)
    for j in range(min(N,int(mp.ceil(smax)))):
        lo=mp.mpf(j)+eps; hi=min(mp.mpf(j+1)-eps,smax)
        grid=[lo+(hi-lo)*k/80 for k in range(81)]
        if j==0: grid=sorted(set(grid+[mp.power(10,-k) for k in range(1,mp.dps//2)]))
        vals=[g(s) for s in grid]
        for k in range(len(grid)-1):
            if vals[k]*vals[k+1]<0:
                r=mp.findroot(g,(grid[k],grid[k+1]),solver='bisect',maxsteps=mp.dps*5,
                              tol=mp.power(10,-mp.dps+12),verify=False)
                r=mp.findroot(g,r,tol=mp.power(10,-mp.dps+12),verify=False)
                if 0<r<smax and all(abs(r-v)>mp.mpf('1e-20') for v in roots): roots.append(r)
    return sorted(roots)

def spectrum(name,X,N,dps,wrong=False,drop_bad=False):
    mp.dps=dps; start=time.time()
    print('curve=',name,'x=',X,'lambda=',fmt(mp.sqrt(X)),'N=',N,'dps=',dps,'wrong_atoms=',wrong,'drop_bad=',drop_bad,flush=True)
    L,a,b,pp,ref=build(name,X,N,wrong,drop_bad)
    print('atoms (p,m,raw,weight)=',[(p,m,r,fmt(wt,14)) for y,wt,p,m,r in pp])
    print('a,b pins n=0..3:',[(fmt(a[n],60),fmt(b[n],60)) for n in range(4)],flush=True)
    E=parent.even_block(a,b,N); O=parent.odd_block(a,b,N)
    ev,U=mp.eigsy(E); ov=mp.eigsy(O,eigvals_only=True)
    print('min E=',fmt(ev[0],50),'next E=',fmt(ev[1],30),'min O=',fmt(ov[0],50),'next O=',fmt(ov[1],30),'even_simple_approx=',ev[0]<ov[0],flush=True)
    xi=[U[0,0]]+[U[j,0]/mp.sqrt(2) for j in range(1,N+1)]
    if xi[0]<0: xi=[-v for v in xi]
    print('xi0 unit-L2=',fmt(xi[0],40),'edge sum=',fmt(xi[0]+2*sum(xi[1:]),40))
    norm=xi[0]+2*sum(xi[1:]); xi=[v/norm for v in xi]
    print('xi0 sum-normalised=',fmt(xi[0],50),flush=True)
    roots=low_roots(xi,N,mp.mpf(20)*L/(2*mp.pi))
    zeros=[mp.mpf(z) for z in ref['zeros'] if mp.mpf(z)>mp.mpf('1e-30')]
    print('s1=',fmt(roots[0],45) if roots else 'NONE','(positive real root of even candidate)',flush=True)
    for i,s in enumerate(roots):
        z=2*mp.pi*s/L
        nearest=min(zeros,key=lambda t:abs(t-z))
        print('root',i+1,'s=',fmt(s,40),'z=',fmt(z,45),'nearest PARI=',fmt(nearest,45),'abs error=',fmt(abs(z-nearest),8),flush=True)
    test_t=xi[0]/(2*sum(xi[j]/j**2 for j in range(1,N+1)))
    print('central h(t) linear estimate t=xi0/(2 sum xi_j/j^2):',fmt(test_t,40))
    if ev[0]>ov[0] and test_t<0:
        def H(t): return -xi[0]+2*t*sum(xi[j]/(j*j-t) for j in range(1,N+1))
        t=mp.findroot(H,test_t)
        print('forced-even imaginary pair s=+-i*',fmt(mp.sqrt(-t),40),'residual H=',fmt(abs(H(t)),5))
    print('elapsed seconds=',round(time.time()-start,3),flush=True)

if __name__=='__main__':
    if sys.argv[1]=='checks': checks()
    elif sys.argv[1]=='spectrum':
        spectrum(sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),
                 wrong='--wrong-atoms' in sys.argv,drop_bad='--drop-bad' in sys.argv)
    else: raise SystemExit('checks | spectrum CURVE X N DPS [--wrong-atoms] [--drop-bad]')
