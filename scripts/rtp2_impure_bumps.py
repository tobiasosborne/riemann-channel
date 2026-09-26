#!/usr/bin/env python3
"""RTP-2 lane I, author codex:gpt-6-astra; deterministic, no RH input.
Copied/adapted from rtp1_prime_content.py: phi1, R_delta scaling, c_delta,
pole and prime closed forms, psi_general and qU. No import: that file requires
python-flint and executes its entire experiment on import. Overlapping arch
entries use the general finite-part definition, not A2's D>2delta series.
Float64 sweep with doubled quadrature; mpmath 40-digit validation and zst check.
All generated files are inside the named lane/checks directory.
"""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
import bisect, itertools, math, json, inspect, subprocess, sys
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
import numpy as np
import mpmath as mp
from scipy.integrate import quad
from scipy.special import roots_legendre
from scipy.optimize import brentq

ROOT=Path(__file__).resolve().parents[1]
CHK=ROOT/'notes/rtp-round-2/impure-bumps/checks'
mp.mp.dps=40
PASS=FAIL=0

def check(cond,msg):
    global PASS,FAIL
    ok=bool(cond); PASS+=ok; FAIL+=not ok
    print(('PASS ' if ok else 'FAIL ')+msg,flush=True)
    return ok

def sieve_pp(X):
    s=bytearray([1])*(X+1); s[:2]=b'\0\0'
    for p in range(2,math.isqrt(X)+1):
        if s[p]: s[p*p::p]=bytes(len(s[p*p::p]))
    pp={}
    for p in range(2,X+1):
        if s[p]:
            k=p
            while k<=X: pp[k]=p; k*=p
    return pp
PP=sieve_pp(1700000); KS=sorted(PP)

def phi1(t):
    return mp.exp(-1/(1-t*t)) if abs(t)<1 else mp.mpf(0)

def rho(y): return mp.exp(y/2)/(2*mp.sinh(y))

def psi_general(q,Y,breaks=()):
    # Adapted literally from A2; error estimate is not a certified bound.
    pts=sorted(set([mp.mpf(0),Y]+[b for b in breaks if 0<b<Y]))
    pole,e1=mp.quad(lambda y:q(y)*2*mp.cosh(y/2),pts,error=True)
    q0=q(mp.mpf(0))
    def ai(y):
        if y==0:return q0/4
        return (q(y)-mp.exp(-y/2)*q0)*rho(y)
    a,e2=mp.quad(ai,pts,error=True)
    arch=(mp.log(4*mp.pi)+mp.euler)*q0/2+a+q0/2*mp.log(mp.tanh(Y/2))
    cutoff=bisect.bisect_right(KS,mp.exp(Y))
    prime=mp.fsum(mp.log(PP[k])/mp.sqrt(k)*q(mp.log(k)) for k in KS[:cutoff])
    return pole-arch-prime,(pole,arch,prime),e1+e2

def qU(n,m,L):
    if n==m:return lambda y:2*(1-y/L)*mp.cos(2*mp.pi*n*y/L)
    return lambda y:(mp.sin(2*mp.pi*m*y/L)-mp.sin(2*mp.pi*n*y/L))/(mp.pi*(n-m))

def consistency():
    print('0. CONSISTENCY FIRST: general Psi against existing zst library; 40 dps')
    # Source printer copied in substance from A2, built only in allowed checks/.
    src=CHK/'zst_ab.c'; exe=CHK/'zst_ab'
    src.write_text(r'''#include <stdio.h>
#include "zst.h"
int main(void){arb_t x; arb_init(x);arb_set_ui(x,9);
 arb_ptr a=_arb_vec_init(9),b=_arb_vec_init(9);
 zst_riemann_ab(a,b,8,x,9,240);
 for(int n=0;n<9;n++){printf("%d ",n);arb_printn(a+n,35,ARB_STR_NO_RADIUS);printf(" ");arb_printn(b+n,35,ARB_STR_NO_RADIUS);printf("\n");}
 _arb_vec_clear(a,9);_arb_vec_clear(b,9);arb_clear(x);return 0;}
''')
    subprocess.run(['cc','-O2','-I'+str(ROOT/'zst/include'),str(src),str(ROOT/'zst/build/libzst.a'),'-lflint','-lmpfr','-lgmp','-lm','-o',str(exe)],check=True)
    out=subprocess.check_output([str(exe)],text=True); (CHK/'zst_ab.txt').write_text(out)
    maxdev=mp.mpf(0); maxerr=mp.mpf(0); L=mp.log(9)
    for line in out.splitlines():
        n,aa,bb=line.split(); n=int(n)
        a,_,ea=psi_general(qU(n,n,L),L)
        if n:b0,_,eb=psi_general(qU(n,0,L),L); b=n*b0
        else:b=eb=mp.mpf(0)
        dev=max(abs(a-mp.mpf(aa)),abs(b-mp.mpf(bb)))
        maxdev=max(maxdev,dev); maxerr=max(maxerr,ea,eb)
        print(f'n={n} a={mp.nstr(a,25)} b={mp.nstr(b,25)} difference={mp.nstr(dev,3)} quad_est={mp.nstr(max(ea,eb),3)}')
    check(maxdev<mp.mpf('1e-32'),f'zst a,b agree beyond printed 25 digits: max={mp.nstr(maxdev,4)}, quad_est={mp.nstr(maxerr,4)}')
    return dict(maxdev=str(maxdev),quad_est=str(maxerr))

@lru_cache(None)
def ratios(S,A):
    rs=set()
    for e in itertools.product(range(-A,A+1),repeat=len(S)):
        r=math.prod((Fraction(p)**a for p,a in zip(S,e)),start=Fraction(1))
        if r>=1:rs.add(r)
    return sorted(rs)

def thresholds(S,A):
    types={'E':[k for k in KS if PP[k] not in S],
           'H':[k for k in KS if PP[k] in S and k>PP[k]**A],
           'all':KS}
    rows={}
    for typ,ks in types.items():
        best=None
        for r in ratios(S,A):
            j=bisect.bisect_left(ks,r)
            for k in ks[max(0,j-1):j+2]:
                if Fraction(k)==r:continue
                # Compare ratios exactly: minimise max(k/r,r/k).
                sep=max(Fraction(k)/r,r/Fraction(k))
                if best is None or sep<best[0]:best=(sep,r,k)
        sep,r,k=best; d=mp.log(mp.mpf(sep.numerator)/sep.denominator)/2
        rows[typ]={'delta':float(d),'exact':str(sep),'ratio':str(r),'k':k,'digits':mp.nstr(d,32)}
    return rows

class FastKernel:
    def __init__(self,n=128):
        self.n=n; self.x,self.w=roots_legendre(n); self.err=0.; self.R0=self.R(0.)
    def phi(self,x):
        x=np.asarray(x); z=np.zeros_like(x,dtype=float); m=np.abs(x)<1
        z[m]=np.exp(-1/(1-x[m]**2)); return z
    def R(self,u):
        u=np.abs(np.asarray(u)); half=np.maximum(0,1-u/2)
        t=u[...,None]/2+half[...,None]*self.x
        return half*np.sum(self.w*self.phi(t)*self.phi(t-u[...,None]),axis=-1)
    def integ(self,f,lo,hi):
        if hi<=lo:return 0.
        # Fixed Gaussian quadrature; two full runs with n and 2n estimate error.
        t=(hi+lo)/2+(hi-lo)/2*self.x
        return (hi-lo)/2*np.dot(self.w,f(t))
    @lru_cache(None)
    def cd(self,d):return d*np.dot(self.w,self.phi(self.x)*np.exp(d*self.x/2))
    @lru_cache(None)
    def entry(self,r,d):
        D=math.log(r.numerator)-math.log(r.denominator); Y=D+2*d
        c=self.cd(d); po=2*math.cosh(D/2)*c*c/(d*self.R0)
        R0=float(self.R(D/d)); q0=2*d*R0
        if D>2*d:
            ar=d*d*self.integ(lambda u:self.R(u)*np.exp((D+d*u)/2)/(2*np.sinh(D+d*u)),-2,0)
            ar+=d*d*self.integ(lambda u:self.R(u)*np.exp((D+d*u)/2)/(2*np.sinh(D+d*u)),0,2)
        else:
            # Finite part from q(y)-q(0), then regular rho. No singular off-diagonal shortcut.
            def q(y):return d*(self.R((y-D)/d)+self.R((y+D)/d))
            pts=sorted(set([0.,Y,D,max(0.,2*d-D)]))
            val=0.
            for lo,hi in zip(pts,pts[1:]):
                def f(y):
                    qy=q(y)
                    return (qy-np.exp(-y/2)*q0)*np.exp(y/2)/(2*np.sinh(y))
                val+=self.integ(f,lo,hi)
            ar=(math.log(4*math.pi)+float(mp.euler))*q0/2+val+q0/2*math.log(math.tanh(Y/2))
        ar/=d*self.R0
        byq={}; active=[]
        hi=math.exp(D+2*d); lo=math.exp(max(0,D-2*d))
        for k in KS[bisect.bisect_left(KS,lo):bisect.bisect_right(KS,hi)]:
            uk=(math.log(k)-D)/d; up=(math.log(k)+D)/d
            if abs(uk)<2 or abs(up)<2:
                wt=float(self.R(uk)+self.R(up))/self.R0*math.log(PP[k])/math.sqrt(k)
                byq[PP[k]]=byq.get(PP[k],0.)+wt; active.append(k)
        h=R0/self.R0
        return po,ar,byq,active,h

@lru_cache(None)
def geometry(S,A):
    pts=list(itertools.product(range(A+1),repeat=len(S)))
    ns=[math.prod(p**a for p,a in zip(S,t)) for t in pts]
    rr=[[Fraction(max(x,y),min(x,y)) for y in ns] for x in ns]
    mask=np.array([[sum(a!=b for a,b in zip(x,y))>=2 for y in pts] for x in pts])
    return pts,rr,mask

def build(ker,S,A,d):
    pts,rr,mix=geometry(S,A); n=len(pts)
    po=np.zeros((n,n)); ar=po.copy(); h=po.copy(); qp={}; active=set()
    for i in range(n):
        for j in range(i,n):
            p,a,qs,ks,hh=ker.entry(rr[i][j],float(d)); active.update(ks)
            po[i,j]=po[j,i]=p; ar[i,j]=ar[j,i]=a; h[i,j]=h[j,i]=hh
            for q,z in qs.items():
                if q not in qp:qp[q]=np.zeros((n,n))
                qp[q][i,j]=qp[q][j,i]=z
    prime=sum(qp.values(),np.zeros((n,n))); G=po-ar-prime; K=G*(~mix)
    return dict(G=G,K=K,po=po*mix,ar=-ar*mix,imp=-prime*mix,qp=qp,active=sorted(active),H=h,mix=mix)

def eig(G):
    w,v=np.linalg.eigh(G); x=v[:,0]
    if x[np.argmax(np.abs(x))]<0:x=-x
    return w,x

def schmidt(v,S,A):
    t=v.reshape((A+1,)*len(S)); vals=[]
    for j in range(len(S)):
        sv=np.linalg.svd(np.moveaxis(t,j,0).reshape(A+1,-1),compute_uv=False)
        vals.append(float(np.sum(sv[1:]**2)))
    return max(vals) if len(S)>1 else 0.

def row(ker,S,A,d,verbose=True):
    b=build(ker,S,A,d); w,v=eig(b['G']); wn,v0=eig(b['K'])
    parts=[b[k] for k in ('po','ar','imp')]
    first=[float(v0@M@v0) for M in parts]; along=[float(v@M@v) for M in parts]
    relax=float(v@b['K']@v-wn[0]); total=float(w[0]-wn[0])
    # Exact path ordered increments, explicitly order dependent.
    path=[]; mat=b['K'].copy(); prev=wn[0]
    for M in parts:
        mat+=M; z=np.linalg.eigvalsh(mat)[0]; path.append(float(z-prev)); prev=z
    lg=float(np.linalg.slogdet(b['K'])[1]-np.linalg.slogdet(b['G'])[1]) if wn[0]>0 and w[0]>0 else None
    ext=sorted(q for q in b['qp'] if q not in S)
    r=dict(S=list(S),A=A,delta=float(d),lam=float(w[0]),gap=float(w[1]-w[0]),nomix=float(wn[0]),schmidt=schmidt(v,S,A),
           product_overlap=abs(float(v@v0)),logdet_gap=lg,first=first,along=along,relax=relax,exact_path=path,
           shift=total,external=ext,active_k=b['active'],vector=v.tolist(),product_vector=v0.tolist(),
           Hmin=float(np.linalg.eigvalsh(b['H'])[0]),residual=float(np.linalg.norm(b['G']@v-w[0]*v)))
    M=b['G']-b['K']; eps=float(np.linalg.norm(M,2)); g=float(wn[1]-wn[0]); Q=np.eye(len(v))-np.outer(v0,v0)
    eta=float(np.linalg.norm(Q@M@v0)); r.update(normM=eps,gap0=g,eta=eta,perturbative=eps<g/2)
    check(abs(total-sum(along)-relax)<2e-11 and abs(total-sum(path))<2e-11,'exact decomposition '+str(S)+f' A={A} delta={d:.9g}') if verbose else None
    if verbose:
        print('SWEEP '+json.dumps(r,sort_keys=True),flush=True)
    return r

def sweep(ker):
    out=[]; crossings=[]; scans=[]
    for S,A in [((2,3),2),((2,3),3),((2,3,5),2)]:
        start=thresholds(S,A)['all']['delta']; ds=np.geomspace(start,.345,12)
        rs=[row(ker,S,A,float(d)) for d in ds]; out+=rs
        # Additional scan establishes earliest sampled bracket; no monotonicity theorem claimed.
        grid=np.geomspace(start,.345,401); last=float(grid[0]); old=row(ker,S,A,last,False)['schmidt']
        scan=[row(ker,S,A,last,False)]
        crossing=None
        for dd in grid[1:]:
            rr=row(ker,S,A,float(dd),False); scan.append(rr); new=rr['schmidt']
            if old<=.1<new:
                root=brentq(lambda d:row(ker,S,A,d,False)['schmidt']-.1,last,float(dd),xtol=2e-11)
                crossing=dict(S=list(S),A=A,bracket=[last,float(dd)],delta=root,at=row(ker,S,A,root,False),
                              above=row(ker,S,A,root*1.001,False));break
            last=float(dd);old=new
        crossings.append(crossing)
        print('CROSSING '+json.dumps(crossing,sort_keys=True),flush=True)
        peak=max(scan,key=lambda r:r['schmidt'])
        scans.append(dict(S=list(S),A=A,count=len(scan),max_schmidt=peak['schmidt'],delta_at_max=peak['delta'],min_gap=min(r['gap'] for r in scan)))
        print('DENSE_SCAN '+json.dumps(scans[-1],sort_keys=True),flush=True)
    return out,crossings,scans

def sensitivity(ker,S,A,d):
    b=build(ker,S,A,d); w,v=eig(b['G']); result=[]
    for q,P in sorted(b['qp'].items()):
        if q in S:continue
        wm,vm=eig(b['G']+P)
        # Scale the true negative q block: derivative d/dtheta G=-P.
        first=-float(v@P@v)
        ww,V=np.linalg.eigh(b['G']); proj=V[:,1:].T@(-P@v)
        deriv=float(np.linalg.norm(proj/(ww[0]-ww[1:])))
        result.append(dict(q=q,lam_off=float(wm[0]),shift=float(wm[0]-w[0]),one_minus_overlap=max(0.,1-abs(float(v@vm))),
                           schmidt_off=schmidt(vm,S,A),dlam_dtheta=first,dv_norm=deriv))
    print('SENSITIVITY '+json.dumps(dict(S=list(S),A=A,delta=d,baseline=w[0],rows=result),sort_keys=True),flush=True)
    return result

def learning(ker,delta):
    result=[]
    for A,chain in [(2,[(2,3),(2,3,5)]),(1,[(2,3),(2,3,5),(2,3,5,7)])]:
        for d in (delta,delta/2,delta/4,.001,.0005):
            for small,big in zip(chain,chain[1:]):
                bs=build(ker,small,A,d); bb=build(ker,big,A,d)
                es,vs=eig(bs['G']); eb,vb=eig(bb['G']); restr=vb.reshape((A+1,)*len(big))[...,0].flatten()
                weight=float(restr@restr); ov=abs(float(restr@vs))/math.sqrt(weight)
                result.append(dict(A=A,delta=d,small=list(small),big=list(big),overlap=ov,movement=1-ov,
                                   weight=weight,lam_small=float(es[0]),lam_big=float(eb[0])))
    for r in result:print('LEARNING '+json.dumps(r,sort_keys=True),flush=True)
    return result

def comparison(ker):
    print('I6 COMPARISON STEP: zeros loaded ONLY here, never used in any form or certificate.')
    zs=np.load(ROOT/'data/zeros3000.npy')[:2000]
    check(len(zs)==2000 and np.all(np.diff(zs)>0),'2000 increasing cached float64 zero ordinates')
    print(f'cached zeros dtype={zs.dtype}; gamma1={zs[0]:.15g}; gamma2000={zs[-1]:.15g}; no certified ordinate radii')
    x,w=roots_legendre(1024); d=.1
    ph=d*(np.cos(d*zs[:,None]*x)@(w*ker.phi(x)))
    x2,w2=roots_legendre(1536)
    ph2=d*(np.cos(d*zs[:,None]*x2)@(w2*ker.phi(x2)))
    print(f'Fourier quadrature 1024 vs 1536 max |difference|={np.max(np.abs(ph-ph2)):.3e}')
    rows=[]
    for r in [Fraction(6),Fraction(8)]:
        po,ar,byq,ks,_=ker.entry(r,d); val=(po-ar-sum(byq.values()))*d*ker.R0
        terms=2*np.cos(zs*math.log(r))*ph2**2; cum=np.cumsum(terms)
        Ms=[10,30,100,300,1000,2000]
        er=[abs(val-cum[M-1]) for M in Ms]
        rr=dict(ratio=str(r),delta=d,prime_side=val,active=ks,Ms=Ms,errors=er,
                finite_absolute_tails=[float(np.sum(np.abs(terms[M:]))) for M in Ms])
        rows.append(rr);print('COMPARISON '+json.dumps(rr,sort_keys=True))
        check(er[-1]<2e-13,'2000-zero comparison within float64 ordinate and quadrature floor at r='+str(r))
    return rows

def main():
    CHK.mkdir(exist_ok=True)
    con=consistency()
    print('1. EXACT RATIONAL THRESHOLDS, mpmath log at 40 dps')
    ts=[]
    for S in [(2,),(2,3),(2,3,5)]:
        for A in range(1,5):
            t=dict(S=list(S),A=A,values=thresholds(S,A));ts.append(t)
            print('THRESHOLD '+json.dumps(t,sort_keys=True))
    ker=FastKernel(128); fine=FastKernel(256)
    # No prime side result was printed before convention calibration.
    print(f'2. QUADRATURE: float64 Gaussian levels 128/256; mp.dps={mp.mp.dps}; no ball certification')
    Rmp,e=mp.quad(lambda t:phi1(t)**2,[-1,0,1],error=True)
    print(f'R1(0)={mp.nstr(Rmp,32)}, mp quad estimate={mp.nstr(e,3)}, float discrepancy={abs(ker.R0-float(Rmp)):.3e}')
    # Numeric counterexample to rank claim.
    pk=float(ker.R(math.log(3/2)/.21))/ker.R0
    check(pk>0 and np.linalg.matrix_rank([[0,pk],[pk,0]])==2,'single-distance impurity k=3 has rank 2')
    rows,cross,scans=sweep(ker)
    # Repeat every requested sweep matrix at doubled quadrature order.
    errs=[]
    for r in rows:
        S=tuple(r['S']);A=r['A'];d=r['delta']
        b=build(ker,S,A,d);bf=build(fine,S,A,d)
        err=float(np.max(np.abs(b['G']-bf['G']))); lamf=eig(bf['G'])[0][0]
        errs.append(dict(S=list(S),A=A,delta=d,max_entry_diff=err,norm_bound=len(b['G'])*err,lam_fine=float(lamf)))
    print('QUADRATURE_DOUBLING '+json.dumps(errs,sort_keys=True))
    check(max(x['max_entry_diff'] for x in errs)<2e-10,'all 36 sweep matrices stable under 128/256 quadrature')
    check(all(r['lam']>10*e['norm_bound'] for r,e in zip(rows,errs)),'all sweep minimum eigenvalues positive above empirical quadrature estimates')
    dstar=next((c['delta']*1.001 for c in cross if c and c['S']==[2,3] and c['A']==2),.2)
    learn=learning(fine,dstar)
    sens=sensitivity(fine,(2,3),2,dstar)
    # Which part is responsible? Hold K fixed and ablate mixed sectors.
    b=build(fine,(2,3),2,dstar); ablations={}
    for name,mat in [('full',b['G']),('no_external',b['G']+sum((P for q,P in b['qp'].items() if q not in (2,3)),np.zeros_like(b['G']))),
                     ('no_mixed_prime',b['G']-b['imp']),('no_mixed_pole',b['G']-b['po']),('no_mixed_arch',b['G']-b['ar'])]:
        w,v=eig(mat);ablations[name]=dict(lam=float(w[0]),schmidt=schmidt(v,(2,3),2))
    print('ABLATIONS '+json.dumps(dict(delta=dstar,values=ablations),sort_keys=True))
    comp=comparison(fine)
    data=dict(consistency=con,thresholds=ts,sweep=rows,crossings=cross,dense_scans=scans,quadrature=errs,learning=learn,sensitivity=sens,delta_star=dstar,ablations=ablations,comparison=comp)
    (CHK/'results.json').write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    print(f'CHECKS: {PASS} passed, {FAIL} failed')
    if FAIL:sys.exit(1)

if __name__=='__main__':main()
