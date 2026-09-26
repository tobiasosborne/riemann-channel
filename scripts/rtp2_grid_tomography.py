#!/usr/bin/env python3
"""Lane G, codex:gpt-6-astra. Prime-side grid tomography, deterministic.

No zeta zeros, no RH, no writes to zst. C/Arb supplies forms, eigenvectors
and sensitivities; HiGHS proposes cuts/certificates, mpmath verifies them.
All auxiliary files are under this lane's checks directory.
"""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
import argparse
import concurrent.futures
import json
from pathlib import Path
import subprocess
import sys
import mpmath as mp
import numpy as np
from scipy.optimize import linprog, minimize
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
    check(err<mp.mpf('1e-150'),f'x={x} N={N}: independent prime-atom sum agrees with zst cutoff split, error={ns(err,4)}')
    return dict(x=x,N=N,lam=lam,cost=cost,co=co,G=C,vec=vec,ab=ab,atoms=atoms)

def grid_case(c,M,union=False):
    inds=[j*256//M-1 for j in range(1,M)]
    ts=[mp.mpf(j)/M for j in range(1,M)]
    tags=[f'grid{j}/{M}' for j in range(1,M)]
    if union:
        inds+=list(range(255,255+c['x']-2))
        ts += [mp.log(n)/mp.log(c['x']) for n in range(2,c['x'])]
        tags += [f'log{n}' for n in range(2,c['x'])]
    G=c['G'][:,inds] if False else mp.matrix([[c['G'][i,j] for j in inds] for i in range(c['G'].rows)])
    # Include constant test exactly; eigenvector cuts alone need not bound mass.
    G=mp.matrix([list(G[i,:]) for i in range(G.rows)]+[[-2*(1-t) for t in ts]])
    b=mp.matrix(list(c['cost'])+[c['ab'][0][2]])
    return dict(G=G,b=b,ts=ts,tags=tags,M=M,union=union)

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

if __name__=='__main__':
    initial_run()
    print(f'CHECKS {COUNTS[0]} FAILURES {COUNTS[1]}')
