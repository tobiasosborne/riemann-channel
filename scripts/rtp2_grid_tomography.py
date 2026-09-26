#!/usr/bin/env python3
"""Lane G, codex:gpt-6-astra. Prime-side grid tomography, deterministic.

No zeta zeros, no RH, no writes to zst. C/Arb supplies forms, eigenvectors
and sensitivities; HiGHS proposes cuts/certificates, mpmath verifies them.
All auxiliary files are under this lane's checks directory.
"""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
import concurrent.futures
import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import mpmath as mp
import numpy as np
from scipy.optimize import linprog
from scipy.linalg import null_space
from scipy.stats import spearmanr

ROOT = Path(__file__).resolve().parents[1]
CHECKS = ROOT/'notes/rtp-round-2/grid-tomography/checks'
COUNTS = [0, 0]
mp.mp.dps = 160

def check(cond, msg):
    COUNTS[0] += 1
    COUNTS[1] += not bool(cond)
    print(('PASS ' if cond else 'FAIL ') + msg, flush=True)
    return bool(cond)

def ns(x, n=12):
    return mp.nstr(x, n)

C_SOURCE = r'''
#include <stdio.h>
#include <stdlib.h>
#include <flint/acb_mat.h>
#include "zst.h"
#define P 1280
static void pr(const arb_t x){arb_printn(x,200,ARB_STR_NO_RADIUS);}
int main(int argc,char **argv){
 int x=atoi(argv[1]),N=atoi(argv[2]),M=atoi(argv[3]),D=2*N+1,J=M-1+x-2;
 arb_t X,L,t,u,s,pi,sq;arb_init(X);arb_init(L);arb_init(t);arb_init(u);arb_init(s);arb_init(pi);arb_init(sq);
 arb_set_ui(X,x);arb_log(L,X,P);arb_const_pi(pi,P);arb_sqrt_ui(sq,2,P);
 arb_ptr a=_arb_vec_init(N+1),b=_arb_vec_init(N+1),a0=_arb_vec_init(N+1),b0=_arb_vec_init(N+1);
 zst_riemann_ab(a,b,N,X,x,P);zst_riemann_ab(a0,b0,N,X,1,P);
 for(int n=0;n<=N;n++){printf("AB %d ",n);pr(a+n);printf(" ");pr(b+n);printf(" ");pr(a0+n);printf(" ");pr(b0+n);printf("\n");}
 arb_mat_t Co,F,G;arb_mat_init(Co,D,D);arb_mat_init(F,D,J);arb_mat_init(G,D,J);
 for(int parity=0;parity<2;parity++){
  int d=N+1-parity,off=parity?N+1:0;
  arb_mat_t H,C;arb_mat_init(H,d,d);arb_mat_init(C,d,d);
  if(parity)zst_odd_block(H,a,b,N,P);else zst_even_block(H,a,b,N,P);
  printf("PD %d %d\n",parity,arb_mat_cho(C,H,P));fflush(stdout);
  acb_mat_t A,R;acb_mat_init(A,d,d);acb_mat_init(R,d,d);acb_ptr eig=_acb_vec_init(d);mag_t tol;mag_init(tol);mag_set_ui_2exp_si(tol,1,-900);
  acb_mat_set_arb_mat(A,H);int ok=acb_mat_approx_eig_qr(eig,NULL,R,A,tol,0,1024);printf("QR %d %d\n",parity,ok);if(!ok)return 3;
  arb_ptr v=_arb_vec_init(D);
  for(int k=0;k<d;k++){
   arb_zero(s);for(int i=0;i<d;i++){arb_get_mid_arb(t,acb_realref(acb_mat_entry(R,i,k)));arb_addmul(s,t,t,P);}arb_sqrt(s,s,P);
   for(int i=0;i<D;i++)arb_zero(v+i);
   for(int i=0;i<d;i++){
    arb_get_mid_arb(t,acb_realref(acb_mat_entry(R,i,k)));arb_div(t,t,s,P);
    if(!parity && i==0)arb_set(v+N,t);
    else {int n=i+parity;arb_div(t,t,sq,P);arb_set(v+N+n,t);if(parity)arb_neg(t,t);arb_set(v+N-n,t);}
   }
   int row=off+k;
   for(int i=-N;i<=N;i++){
    arb_addmul(arb_mat_entry(Co,row,abs(i)),v+i+N,v+i+N,P);
    for(int j=-N;j<i;j++){
     arb_mul(t,v+i+N,v+j+N,P);arb_mul_2exp_si(t,t,1);arb_div_si(t,t,i-j,P);
     if(i){if(i>0)arb_add(arb_mat_entry(Co,row,N+i),arb_mat_entry(Co,row,N+i),t,P);else arb_sub(arb_mat_entry(Co,row,N-i),arb_mat_entry(Co,row,N-i),t,P);}
     if(j){if(j>0)arb_sub(arb_mat_entry(Co,row,N+j),arb_mat_entry(Co,row,N+j),t,P);else arb_add(arb_mat_entry(Co,row,N-j),arb_mat_entry(Co,row,N-j),t,P);}
    }
   }
   arb_zero(t);arb_zero(u);
   for(int n=0;n<=N;n++){arb_addmul(t,arb_mat_entry(Co,row,n),a+n,P);arb_addmul(u,arb_mat_entry(Co,row,n),a0+n,P);}
   for(int n=1;n<=N;n++){arb_addmul(t,arb_mat_entry(Co,row,N+n),b+n,P);arb_addmul(u,arb_mat_entry(Co,row,N+n),b0+n,P);}
   printf("ROW %d ",row);pr(t);printf(" ");pr(u);for(int i=0;i<D;i++){printf(" ");pr(arb_mat_entry(Co,row,i));}printf("\n");
   printf("VEC %d %d",row,parity);for(int i=0;i<d;i++){printf(" ");if(!parity&&i==0)arb_set(t,v+N);else arb_mul(t,v+N+i+parity,sq,P);pr(t);}printf("\n");
  }
  _arb_vec_clear(v,D);arb_mat_clear(H);arb_mat_clear(C);acb_mat_clear(A);acb_mat_clear(R);_acb_vec_clear(eig,d);mag_clear(tol);
 }
 arb_t sn,cs,z;arb_init(sn);arb_init(cs);arb_init(z);
 for(int j=0;j<J;j++){
  if(j<M-1){arb_set_ui(t,j+1);arb_div_ui(t,t,M,P);}else{arb_set_ui(t,j-(M-1)+2);arb_log(t,t,P);arb_div(t,t,L,P);}
  arb_one(u);arb_sub(u,u,t,P);
  for(int n=0;n<=N;n++){
   arb_mul_si(z,t,2*n,P);arb_sin_cos_pi(sn,cs,z,P);
   arb_mul(z,u,cs,P);arb_mul_si(arb_mat_entry(F,n,j),z,-2,P);
   if(n)arb_div(arb_mat_entry(F,N+n,j),sn,pi,P);
  }
 }
 arb_mat_mul(G,Co,F,P);
 for(int i=0;i<D;i++){printf("GRID %d",i);for(int j=0;j<J;j++){printf(" ");pr(arb_mat_entry(G,i,j));}printf("\n");}
 return 0;
}
'''

def build():
    CHECKS.mkdir(exist_ok=True)
    src, exe = CHECKS/'bridge.c', CHECKS/'bridge'
    if not src.exists() or src.read_text()!=C_SOURCE or not exe.exists():
        src.write_text(C_SOURCE)
        subprocess.run(['cc','-O2','-I'+str(ROOT/'zst/include'),str(src),str(ROOT/'zst/build/libzst.a'),'-lflint','-lmpfr','-lgmp','-lm','-o',str(exe)], check=True)

def produce(pair):
    x,N=pair
    path=CHECKS/f'x{x}_N{N}.data'
    if not path.exists():
        with path.with_suffix('.partial').open('w') as f:
            subprocess.run([str(CHECKS/'bridge'),str(x),str(N),'256'],stdout=f,check=True)
        path.with_suffix('.partial').replace(path)
    return str(path)

def pp(x):
    ans=[]
    for n in range(2,x):
        fac=next((p for p in range(2,n+1) if n%p==0),n)
        r=n
        while r%fac==0:r//=fac
        if r==1:ans.append((n,mp.log(fac)/mp.sqrt(n)))
    return ans

def load_case(x,N):
    rows=[];grid=[];vec=[];ab=[];pd=[]
    for line in Path(produce((x,N))).read_text().splitlines():
        s=line.split()
        if s[0]=='AB':ab.append(list(map(mp.mpf,s[2:])))
        if s[0]=='PD':pd.append(int(s[2]))
        if s[0]=='ROW':rows.append(list(map(mp.mpf,s[2:])))
        if s[0]=='GRID':grid.append(list(map(mp.mpf,s[2:])))
        if s[0]=='VEC':vec.append((int(s[2]),list(map(mp.mpf,s[3:]))))
    order=sorted(range(2*N+1),key=lambda i:rows[i][0])
    rows=[rows[i] for i in order];grid=[grid[i] for i in order];vec=[vec[i] for i in order]
    lam=mp.matrix([r[0] for r in rows]);cost=mp.matrix([r[1] for r in rows]);co=mp.matrix([r[2:] for r in rows])
    C=mp.matrix(grid)
    check(pd==[1,1],f'x={x} N={N}: true blocks positive by 1280-bit Arb Cholesky')
    atoms=pp(x)
    true=mp.matrix([mp.fsum(co[i,n]*(ab[n][0]-ab[n][2]) for n in range(N+1))+mp.fsum(co[i,N+n]*(ab[n][1]-ab[n][3]) for n in range(1,N+1)) for i in range(2*N+1)])
    err=max(abs(cost[i]+mp.fsum(C[i,255+n-2]*w for n,w in atoms)-lam[i]) for i in range(2*N+1))
    check(err<mp.power(10,-mp.mp.dps+10),f'x={x} N={N}: independent prime-atom sum agrees with zst cutoff split, error={ns(err,4)}')
    return dict(x=x,N=N,lam=lam,cost=cost,co=co,G=C,vec=vec,ab=ab,atoms=atoms)

def grid_case(c,M,union=False):
    inds=[j*256//M-1 for j in range(1,M)]
    ts=[mp.mpf(j)/M for j in range(1,M)]
    tags=[f'grid{j}/{M}' for j in range(1,M)]
    lattice_idx={}
    if union:
        for n in range(2,c['x']):
            t=mp.log(n)/mp.log(c['x']);j=int(mp.nint(M*t))
            if 1<=j<M and n**M==c['x']**j:
                lattice_idx[n]=j-1
            else:
                lattice_idx[n]=len(ts);inds.append(255+n-2);ts.append(t);tags.append(f'log{n}')
    G=mp.matrix([[c['G'][i,j] for j in inds] for i in range(c['G'].rows)])
    # Include constant test exactly; eigenvector cuts alone need not bound mass.
    G=mp.matrix([list(G[i,:]) for i in range(G.rows)]+[[-2*(1-t) for t in ts]])
    b=mp.matrix(list(c['cost'])+[c['ab'][0][2]])
    return dict(G=G,b=b,ts=ts,tags=tags,M=M,union=union,lattice_idx=lattice_idx)

def farkas(g):
    """G w+b>=0,w>=0; y>=0,G.T y<=0,b.y<0 proves emptiness."""
    G=np.array(g['G'].tolist(),float);b=np.array(list(g['b']),float)
    r=linprog(b,A_ub=G.T,b_ub=np.zeros(G.shape[1]),A_eq=np.ones((1,len(b))),b_eq=[1],bounds=(0,None),method='highs')
    if not r.success or r.fun>=-1e-10:return None
    # Treat proposed decimals as exact; repair any residual with constant cut.
    y=[mp.mpf(str(max(0.,v))) for v in r.x]
    residual=[mp.fsum(y[i]*g['G'][i,j] for i in range(len(y))) for j in range(G.shape[1])]
    repair=max([mp.mpf(0)]+[residual[j]/(2*(1-g['ts'][j])) for j in range(G.shape[1])])+mp.mpf('1e-120')
    y[-1]+=repair
    cost=mp.fsum(y[i]*g['b'][i] for i in range(len(y)))
    slack=max(mp.fsum(y[i]*g['G'][i,j] for i in range(len(y))) for j in range(G.shape[1]))
    return dict(cost=cost,slack=slack,repair=repair,y=y) if cost<0 and slack<0 else None

def initial_run():
    build()
    pairs=[(13,20),(13,40),(13,60),(25,60),(25,134)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for path in pool.map(produce,pairs):print('DATA '+str(Path(path).name),flush=True)
    for x,N in pairs:
        c=load_case(x,N)
        print(f'CASE x={x} N={N} min_eig={ns(c["lam"][0])}',flush=True)
        for M in ([64,128,256] if x==13 else [128]):
            for union in [False,True]:
                g=grid_case(c,M,union)
                f=farkas(g)
                print(f'GRID M={M} union={union} FARKAS '+('none' if f is None else f'cost={ns(f["cost"])} residual={ns(f["slack"],4)}'),flush=True)
                if f:
                    (CHECKS/f'farkas_x{x}_N{N}_M{M}.json').write_text(json.dumps({k:([ns(v,160) for v in val] if k=='y' else ns(val,160)) for k,val in f.items()},indent=2)+'\n')

def lp_tableau(c,g,rcount=None):
    """Primal feasible tableau centered at truth; free true weights split +/-.

    Only the chosen smallest-eigenvalue cuts are used. This is an explicit
    outer relaxation; all sign constraints at zero coordinates are retained.
    True occupied weights are free in this relaxation, enlarging the set.
    """
    if rcount is None:rcount=2*len(c['atoms'])+4
    rcount=min(rcount,2*c['N']+1)
    J=len(g['ts']);pidx=[g['lattice_idx'][n] for n,w in c['atoms']]
    qidx=[j for j in range(J) if j not in pidx]
    mapping=[(j,1) for j in qidx+pidx]+[(j,-1) for j in pidx]
    nv=len(mapping)
    A=mp.matrix([[-sign*g['G'][i,j] for j,sign in mapping] for i in range(rcount)])
    lam=c['lam'][:rcount,:]
    T=[[A[i,j] for j in range(nv)]+[mp.mpf(i==j) for j in range(rcount)]+[lam[i]] for i in range(rcount)]
    return dict(T=T,basis=list(range(nv,nv+rcount)),A=A,b=lam,mapping=mapping,nv=nv,r=rcount,pidx=pidx)

def tableau_max(state,objective):
    T=state['T'];basis=state['basis'];r=state['r'];nv=state['nv'];n=nv+r
    cost=[mp.mpf(sign)*objective[j] for j,sign in state['mapping']]+[mp.mpf(0)]*r
    tol=mp.mpf('1e-125')
    for iteration in range(20000):
        cb=[cost[j] for j in basis]
        red=[cost[j]-mp.fsum(cb[i]*T[i][j] for i in range(r)) for j in range(n)]
        # Dantzig pivots with Bland tie breaking; deterministic and audited.
        ent=max(range(n),key=lambda j:red[j] if j not in basis else -mp.inf)
        if red[ent]<=tol:break
        choices=[(T[i][-1]/T[i][ent],basis[i],i) for i in range(r) if T[i][ent]>tol]
        if not choices:raise RuntimeError('unbounded chosen-cut relaxation')
        row=min(choices)[2];p=T[row][ent];T[row]=[v/p for v in T[row]]
        for i in range(r):
            if i!=row:
                f=T[i][ent]
                if f:T[i]=[v-f*u for v,u in zip(T[i],T[row])]
        basis[row]=ent
    else:raise RuntimeError('simplex iteration limit')
    # Solve the returned basis afresh (160 dps), instead of trusting a tableau.
    B=mp.matrix([[state['A'][i,j] if j<nv else mp.mpf(i==j-nv) for j in basis] for i in range(r)])
    y=mp.lu_solve(B.T,mp.matrix([cost[j] for j in basis]))
    x=mp.lu_solve(B,state['b'])
    residual=max(abs(v) for v in B.T*y-mp.matrix([cost[j] for j in basis]))
    primal=min(x)
    dual=min([y[i] for i in range(r)]+[mp.fsum(y[i]*state['A'][i,j] for i in range(r))-cost[j] for j in range(nv)])
    value=mp.fdot(y,state['b'])
    if primal < -mp.mpf('1e-110') or dual < -mp.mpf('1e-110') or residual > mp.mpf('1e-110'):
        raise RuntimeError(f'LP audit failed: {ns(primal)} {ns(dual)} {ns(residual)}')
    return value,y,dict(primal=primal,dual=dual,residual=residual,iterations=iteration)

def box_run(pair):
    x,N,M=pair
    saved=CHECKS/f'boxes_x{x}_N{N}_M{M}.json'
    if saved.exists():return json.loads(saved.read_text())
    mp.mp.dps=160
    c=load_case(x,N);g=grid_case(c,M,True);J=len(g['ts']);state=lp_tableau(c,g)
    truth=[mp.mpf(0)]*J
    for n,w in c['atoms']:truth[g['lattice_idx'][n]]=w
    bounds=[];certs=[];audit=[mp.mpf(0),mp.mpf(0),mp.mpf(0)]
    def bound(obj):
        val,y,a=tableau_max(state,obj)
        audit[0]=max(audit[0],a['residual']);audit[1]=min(audit[1],a['dual']);audit[2]=min(audit[2],a['primal'])
        certs.append(dict(objective=[ns(v,170) for v in obj],y=[ns(v,170) for v in y],value=ns(val,170)))
        return val+mp.fdot(obj,truth)
    for j in range(J):
        obj=[mp.mpf(0)]*J;obj[j]=1;hi=bound(obj)
        lo=mp.mpf(0)
        if truth[j]:obj[j]=-1;lo=max(mp.mpf(0),-bound(obj))
        bounds.append([lo,hi])
    ones=[mp.mpf(1)]*J
    mass_hi=bound(ones);mass_lo=-bound([-v for v in ones])
    pts=[mp.log(n)/mp.log(x) for n,w in c['atoms']]
    near=[min(abs(t-p) for p in pts)<=mp.mpf(1)/M for t in g['ts']]
    near_hi=bound([mp.mpf(v) for v in near]);near_lo=-bound([-mp.mpf(v) for v in near])
    far_hi=bound([mp.mpf(not v) for v in near])
    result=dict(x=x,N=N,M=M,cuts=state['r'],mass=[ns(mass_lo,20),ns(mass_hi,20)],near=[ns(near_lo,20),ns(near_hi,20)],far_upper=ns(far_hi,20),true_mass=ns(sum(truth),20),ratio_lower=ns(max(0,near_lo)/far_hi,20),audit=[ns(v,8) for v in audit],boxes=[[tag,ns(t*mp.log(x),20),ns(truth[j],20),ns(lo,24),ns(hi,24)] for j,(tag,t,(lo,hi)) in enumerate(zip(g['tags'],g['ts'],bounds))])
    name=f'boxes_x{x}_N{N}_M{M}'
    (CHECKS/(name+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    (CHECKS/(name+'_certificates.json')).write_text(json.dumps(certs,separators=(',',':'))+'\n')
    return result

def run_boxes():
    pairs=[(13,N,M) for N in [20,40,60] for M in [64,128,256]]+[(25,N,128) for N in [60,134]]
    with concurrent.futures.ProcessPoolExecutor(max_workers=11) as pool:
        for r,transcript,counts in pool.map(box_task,pairs):
            check(counts[1]==0,f'LP boxes x={r["x"]} N={r["N"]} M={r["M"]}: generated or loaded; dual re-verification follows')
            keys=['x','N','M','cuts','mass','near','far_upper','true_mass','ratio_lower','audit']
            print('BOX '+json.dumps({k:r[k] for k in keys}),flush=True)

def box_task(pair):
    COUNTS[:]=[0,0];stream=io.StringIO()
    with contextlib.redirect_stdout(stream):result=box_run(pair)
    return result,stream.getvalue(),COUNTS[:]

def moments(N,t):
    return [-2*(1-t)*mp.cos(2*mp.pi*n*t) for n in range(N+1)]+[mp.sin(2*mp.pi*n*t)/mp.pi for n in range(1,N+1)]

def blocks(a,b,N):
    E=mp.matrix(N+1);O=mp.matrix(N);E[0,0]=a[0]
    for i in range(1,N+1):
        E[0,i]=E[i,0]=mp.sqrt(2)*b[i]/i
        E[i,i]=a[i]+b[i]/i;O[i-1,i-1]=a[i]-b[i]/i
        for j in range(1,i):
            t=(b[i]-b[j])/(i-j);u=(b[i]+b[j])/(i+j)
            E[i,j]=E[j,i]=t+u;O[i-1,j-1]=O[j-1,i-1]=t-u
    return E,O

def atom_blocks(N,t):
    z=moments(N,t)
    return blocks(z[:N+1],[mp.mpf(0)]+z[N+1:],N)

def signed_run():
    c=load_case(13,20);N=20;M=64
    F=mp.matrix([moments(N,mp.mpf(j)/M) for j in range(1,M)]).T
    H0=mp.matrix([r[2] for r in c['ab']]+[r[3] for r in c['ab'][1:]])
    target=-H0+mp.matrix([1]*(N+1)+[0]*N)
    w=F.T*mp.lu_solve(F*F.T,target)
    resid=mp.norm(F*w-target,mp.inf)
    sv=np.linalg.svd(np.array(F.tolist(),float),compute_uv=False)
    null=null_space(np.array(F.tolist(),float))
    check(resid<mp.mpf('1e-140'),'signed grid: explicit feasible weights assemble H=I to 140 digits')
    check(null.shape==(63,22) and min(np.linalg.norm(null,axis=1))>1e-3,'signed grid: rank 41, nullity 22, every weight varies in the kernel')
    print(f'SIGNED rank=41 nullity=22 smallest_singular={sv[-1]:.10e} H_identity_residual={ns(resid,6)} negative_weights={sum(v<0 for v in w)}')
    print('SIGNED_PROJECTION a_n in [-H0_nn,+infinity), b_n in (-infinity,+infinity); all weight boxes (-infinity,+infinity)')
    (CHECKS/'signed_x13_N20_M64.json').write_text(json.dumps(dict(weights=[ns(v,160) for v in w],residual=ns(resid,20),moment_lower=[ns(-r[2],30) for r in c['ab']],singular_values=sv.tolist()),indent=2)+'\n')

def near_kernel_run():
    c=load_case(13,60);N=60;L=mp.log(13);M=256;ts=np.arange(1,M)/M
    primes=np.array([float(mp.log(n)/L) for n,w in c['atoms']])
    dist=np.min(abs(ts[:,None]-primes[None,:]),axis=1)
    mask=dist<=1/M
    G=np.array(c['G'].tolist(),float)
    tab=[]
    for r in range(8):
        co=list(c['co'][r,:])
        def q(t):return -mp.fdot(co,moments(N,mp.mpf(t)))
        qs=-G[r,:255]
        zeros=[]
        for j in range(254):
            if qs[j]*qs[j+1]<0:
                a=mp.mpf(j+1)/M;b=mp.mpf(j+2)/M
                for _ in range(180):
                    m=(a+b)/2
                    if q(a)*q(m)<=0:b=m
                    else:a=m
                zeros.append((a+b)/2)
        primevals=[q(mp.log(n)/L) for n,w in c['atoms']]
        normalized=[abs(float(v))/max(abs(qs)) for v in primevals]
        corr=float(spearmanr(-abs(qs),-dist).statistic)
        hit=int(sum(min(abs(float(z)-primes))<=1/M for z in zeros))
        record=dict(vector=r,eigenvalue=ns(c['lam'][r],16),parity=c['vec'][r][0],q_min=float(min(qs)),q_max=float(max(qs)),negative_fraction=float(np.mean(qs<0)),spearman_small_q_near_prime=corr,zeros_y=[ns(z*L,24) for z in zeros],zero_hits_within_h=hit,prime_values=[ns(v,18) for v in primevals],prime_abs_relative=normalized,nearest_zero_distance_y=[min((float(abs(z*L-mp.log(n))) for z in zeros),default=None) for n,w in c['atoms']])
        record['pole_arch_cost']=ns(c['cost'][r],18)
        check(abs(q(0)-2)<mp.mpf('1e-140'),f'near-kernel vector {r}: normalization q(0)=2; interior sign changes={len(zeros)}')
        print('NEAR_KERNEL '+json.dumps(record),flush=True)
        tab.append(record)
    (CHECKS/'near_kernel.json').write_text(json.dumps(tab,indent=2)+'\n')
    with (CHECKS/'near_kernel_profiles.tsv').open('w') as f:
        f.write('y\tdistance_to_prime\t'+'\t'.join(f'q{i}' for i in range(8))+'\n')
        for j,t in enumerate(ts):f.write(f'{float(t*float(L)):.17g}\t{dist[j]*float(L):.17g}\t'+'\t'.join(f'{-G[i,j]:.17g}' for i in range(8))+'\n')

def positive_ldl(H):
    """Unpivoted LDL inertia test, stopping at the first nonpositive pivot."""
    d=H.rows;A=H.copy();piv=[]
    for k in range(d):
        pivot=A[k,k]
        if pivot<=0:return False,pivot
        piv.append(pivot)
        for i in range(k+1,d):
            for j in range(k+1,i+1):A[i,j]=A[j,i]=A[i,j]-A[i,k]*A[j,k]/pivot
    return True,min(piv)

def sections_run():
    with mp.workdps(100):
        c=load_case(13,20);N=20
        H=blocks([r[0] for r in c['ab']],[r[1] for r in c['ab']],N)
        out=[]
        for label,t in [('grid1/64',mp.mpf(1)/64),('grid17/64',mp.mpf(17)/64),('grid63/64',mp.mpf(63)/64),('log2',mp.log(2)/mp.log(13))]:
            T=atom_blocks(N,t)
            def feasible(delta):return all(positive_ldl(h+delta*a)[0] for h,a in zip(H,T))
            bounds=[]
            for sign in ([-1,1] if label=='log2' else [1]):
                lo=mp.mpf(0);hi=mp.mpf('1e-50')
                while feasible(sign*hi):lo=hi;hi*=10
                for _ in range(80):
                    m=(lo+hi)/2
                    if feasible(sign*m):lo=m
                    else:hi=m
                check(feasible(sign*lo) and not feasible(sign*hi),f'SDP axis {label} sign={sign}: 100-digit LDL brackets boundary')
                bounds.append(dict(sign=sign,inside=ns(lo,30),outside=ns(hi,30)))
            row=dict(point=label,y=ns(t*mp.log(13),30),bounds=bounds)
            print('AXIS_SECTION '+json.dumps(row),flush=True);out.append(row)
        (CHECKS/'axis_sections.json').write_text(json.dumps(out,indent=2)+'\n')

def supplemental_run():
    signed_run();near_kernel_run();sections_run()

VERIFY_C = r'''
#include <stdio.h>
#include <stdlib.h>
#include "zst.h"
#define P 1024
int main(int argc,char **argv){
 FILE *f=fopen(argv[1],"r");int x,N,M,D;if(fscanf(f,"%d %d %d",&x,&N,&M)!=3)return 2;D=2*N+1;
 arb_t X,L,t,u,s,pi,sq,weight,cost,extra,sn,cs,ty,q;arb_init(X);arb_init(L);arb_init(t);arb_init(u);arb_init(s);arb_init(pi);arb_init(sq);arb_init(weight);arb_init(cost);arb_init(extra);arb_init(sn);arb_init(cs);arb_init(ty);arb_init(q);
 arb_set_ui(X,x);arb_log(L,X,P);arb_const_pi(pi,P);arb_sqrt_ui(sq,2,P);
 arb_ptr a=_arb_vec_init(N+1),b=_arb_vec_init(N+1),v=_arb_vec_init(D),co=_arb_vec_init(D);
 zst_riemann_ab(a,b,N,X,1,P);char buf[4096];int ok=1;
 for(int k=0;k<D;k++){
  int parity;if(fscanf(f,"%d %4095s",&parity,buf)!=2)return 3;arb_set_str(weight,buf,P);ok=ok&&arb_is_nonnegative(weight);
  int d=N+1-parity;for(int i=0;i<D;i++)arb_zero(v+i);
  for(int i=0;i<d;i++){
   if(fscanf(f,"%4095s",buf)!=1)return 3;arb_set_str(t,buf,P);
   if(!parity&&i==0)arb_set(v+N,t);else{int n=i+parity;arb_div(t,t,sq,P);arb_set(v+N+n,t);if(parity)arb_neg(t,t);arb_set(v+N-n,t);}
  }
  for(int i=-N;i<=N;i++){
   arb_mul(t,v+i+N,v+i+N,P);arb_addmul(co+abs(i),weight,t,P);
   for(int j=-N;j<i;j++){
    arb_mul(t,v+i+N,v+j+N,P);arb_mul_2exp_si(t,t,1);arb_div_si(t,t,i-j,P);arb_mul(t,t,weight,P);
    if(i){if(i>0)arb_add(co+N+i,co+N+i,t,P);else arb_sub(co+N-i,co+N-i,t,P);}
    if(j){if(j>0)arb_sub(co+N+j,co+N+j,t,P);else arb_add(co+N-j,co+N-j,t,P);}
   }
  }
 }
 if(fscanf(f,"%4095s",buf)!=1)return 3;arb_set_str(extra,buf,P);ok=ok&&arb_is_nonnegative(extra);arb_add(co,co,extra,P);
 for(int n=0;n<=N;n++)arb_addmul(cost,co+n,a+n,P);
 for(int n=1;n<=N;n++)arb_addmul(cost,co+N+n,b+n,P);
 ok=ok&&arb_is_negative(cost);
 for(int j=1;j<M;j++){
  arb_set_ui(ty,j);arb_div_ui(ty,ty,M,P);arb_one(u);arb_sub(u,u,ty,P);arb_zero(q);
  for(int n=0;n<=N;n++){
   arb_mul_si(t,ty,2*n,P);arb_sin_cos_pi(sn,cs,t,P);arb_mul(t,u,cs,P);arb_mul_si(t,t,-2,P);arb_addmul(q,co+n,t,P);
   if(n){arb_div(t,sn,pi,P);arb_addmul(q,co+N+n,t,P);}
  }
  ok=ok&&arb_is_negative(q);
 }
 printf("FARKAS_BALL x=%d N=%d M=%d certified=%d cost=",x,N,M,ok);arb_printn(cost,30,0);printf("\n");return !ok;
}
'''

def verify_farkas():
    src=CHECKS/'verify_farkas.c';exe=CHECKS/'verify_farkas'
    src.write_text(VERIFY_C)
    subprocess.run(['cc','-O2','-I'+str(ROOT/'zst/include'),str(src),str(ROOT/'zst/build/libzst.a'),'-lflint','-lmpfr','-lgmp','-lm','-o',str(exe)],check=True)
    for x,N in [(13,20),(13,40),(13,60),(25,60),(25,134)]:
        c=load_case(x,N)
        for M in ([64,128,256] if x==13 else [128]):
            f=json.loads((CHECKS/f'farkas_x{x}_N{N}_M{M}.json').read_text())
            lines=[f'{x} {N} {M}']
            for i,(p,vec) in enumerate(c['vec']):lines.append(f'{p} {f["y"][i]} '+' '.join(ns(v,170) for v in vec))
            lines.append(f['y'][-1])
            path=CHECKS/f'farkas_x{x}_N{N}_M{M}.in';path.write_text('\n'.join(lines)+'\n')
            proc=subprocess.run([str(exe),str(path)],capture_output=True,text=True)
            print(proc.stdout.strip(),flush=True)
            check(proc.returncode==0,f'grid x={x} N={N} M={M}: exact Farkas contradiction certified with 1024-bit balls')

def verify_box(pair):
    x,N,M=pair;mp.mp.dps=180
    c=load_case(x,N);g=grid_case(c,M,True)
    path=CHECKS/f'boxes_x{x}_N{N}_M{M}.json';res=json.loads(path.read_text())
    certs=json.loads((CHECKS/f'boxes_x{x}_N{N}_M{M}_certificates.json').read_text())
    J=len(g['ts']);truth=[mp.mpf(0)]*J
    for n,w in c['atoms']:truth[g['lattice_idx'][n]]=w
    W=[g['b'][-1]/(2*(1-t)) for t in g['ts']]
    vals=[];maxcorr=mp.mpf(0);maxnegative=mp.mpf(0)
    for cert in certs:
        obj=list(map(mp.mpf,cert['objective']));oldy=list(map(mp.mpf,cert['y']));y=[max(0,v) for v in oldy]
        maxnegative=max(maxnegative,max(-v for v in oldy))
        r=[obj[j]+mp.fsum(y[i]*g['G'][i,j] for i in range(len(y))) for j in range(J)]
        # The constant test supplies an independent coordinate scale. This
        # repairs *all* residuals; small residuals alone are not certificates.
        corr=mp.fsum(v*(W[j]-truth[j]) if v>0 else -v*truth[j] for j,v in enumerate(r))
        guard=mp.mpf('1e-170')*(1+sum(y))*(1+sum(W)+sum(truth))
        value=mp.fdot(y,list(c['lam'])[:len(y)])+mp.fdot(obj,truth)+corr+guard
        vals.append(value);maxcorr=max(maxcorr,abs(value-(mp.mpf(cert['value'])+mp.fdot(obj,truth))))
    k=0
    for j,row in enumerate(res['boxes']):
        row[4]=ns(vals[k],24);k+=1
        if truth[j]:row[3]=ns(max(0,-vals[k]),24);k+=1
    mass_hi,mass_neglo,near_hi,near_neglo,far_hi=vals[k:]
    res.update(mass=[ns(-mass_neglo,20),ns(mass_hi,20)],near=[ns(-near_neglo,20),ns(near_hi,20)],far_upper=ns(far_hi,20),ratio_lower=ns(max(0,-near_neglo)/far_hi,20),residual_correction_max=ns(maxcorr,12),negative_dual_clipped=ns(maxnegative,12),verification_dps=180)
    check(all(mp.mpf(row[3])-mp.mpf('1e-18')<=mp.mpf(row[2])<=mp.mpf(row[4])+mp.mpf('1e-18') for row in res['boxes']),f'boxes x={x} N={N} M={M}: truth contained, residuals repaired using constant-test mass scale')
    path.write_text(json.dumps(res,indent=2)+'\n')
    return {k:v for k,v in res.items() if k!='boxes'}

def verification_run():
    verify_farkas()
    pairs=[(13,N,M) for N in [20,40,60] for M in [64,128,256]]+[(25,N,128) for N in [60,134]]
    with concurrent.futures.ProcessPoolExecutor(max_workers=11) as pool:
        for result,transcript,counts in pool.map(verify_task,pairs):
            print(transcript,end='');COUNTS[0]+=counts[0];COUNTS[1]+=counts[1]
            print('VERIFIED_BOX '+json.dumps(result),flush=True)

def verify_task(pair):
    COUNTS[:]=[0,0];stream=io.StringIO()
    with contextlib.redirect_stdout(stream):result=verify_box(pair)
    return result,stream.getvalue(),COUNTS[:]

def report_tables():
    print('UNIFORM_GRID_OPTIMIZERS: all eleven feasible sets empty; weight boxes, mass ranges, min-norm/entropy measures and histogram distances undefined.')
    print('UNION_GRID_BOXES: high-precision outer bounds; selected cuts=20 (x13),30 (x25); exact coordinate SDP projections not claimed.')
    for x,N in [(13,20),(13,40),(13,60),(25,60),(25,134)]:
        c=load_case(x,N)
        for M in ([64,128,256] if x==13 else [128]):
            g=grid_case(c,M,False);hist=[mp.mpf(0)]*(M-1);displacement=mp.mpf(0)
            for n,w in c['atoms']:
                t=mp.log(n)/mp.log(x);j=max(1,min(M-1,int(mp.nint(M*t))))
                hist[j-1]+=w;displacement=max(displacement,abs(t-mp.mpf(j)/M)*mp.log(x))
            ray=g['b']+g['G']*mp.matrix(hist)
            check(min(ray)<0,f'x={x} N={N} M={M}: nearest-grid truth histogram fails a true-eigenvector cut')
            print(f'HISTOGRAM x={x} N={N} M={M} max_displacement={ns(displacement)} minimum_cut={ns(min(ray))}')
            r=json.loads((CHECKS/f'boxes_x{x}_N{N}_M{M}.json').read_text())
            print('UNION_SUMMARY '+json.dumps({k:v for k,v in r.items() if k!='boxes'}))
            print('point\ty\ttrue_weight\tlower_outer\tupper_outer')
            for row in sorted(r['boxes'],key=lambda row:mp.mpf(row[1])):print('\t'.join(row))
            near=[row for row in r['boxes'] if min(abs(mp.mpf(row[1])-mp.log(n)) for n,w in c['atoms'])<=mp.log(x)/M]
            far=[row for row in r['boxes'] if row not in near]
            print('LARGEST_OFF_PRIME_BOX '+json.dumps(max(far,key=lambda row:mp.mpf(row[4]))))
    print('NEAR_KERNEL_PROFILE_FILE notes/rtp-round-2/grid-tomography/checks/near_kernel_profiles.tsv')

if __name__=='__main__':
    if '--boxes' in sys.argv:run_boxes()
    elif '--supplemental' in sys.argv:supplemental_run()
    elif '--verify' in sys.argv:verification_run()
    elif '--prepare' in sys.argv:initial_run()
    elif '--report' in sys.argv:report_tables()
    else:
        print('RTP-2 LANE G / codex:gpt-6-astra / no RH, no zero ordinates / deterministic')
        print('PRECISION: 1280-bit Arb input and PD; 1024-bit ball Farkas; 160-digit LP; 180-digit residual repair; 100-digit axis inertia.')
        initial_run();run_boxes();verification_run();supplemental_run();report_tables()
    print(f'CHECKS {COUNTS[0]} FAILURES {COUNTS[1]}')
    sys.exit(bool(COUNTS[1]))
