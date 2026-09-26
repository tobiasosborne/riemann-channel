#!/usr/bin/env python3
"""Lane L, codex:gpt-6-astra. Deterministic prime-side lattice boxes.

Run from the repository root. Generated C, binary, caches and certificates stay in
notes/rtp-round-2/lattice-box/checks. No python-flint; zst is read-only.
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

ROOT = Path(__file__).resolve().parents[1]
CHECKS = ROOT / 'notes/rtp-round-2/lattice-box/checks'
CHECKS.mkdir(exist_ok=True)
mp.mp.dps = 200
COUNTS = [0, 0]

def check(cond, msg):
    COUNTS[0] += 1
    COUNTS[1] += not bool(cond)
    print(('PASS ' if cond else 'FAIL ') + msg, flush=True)
    return bool(cond)

def ns(x, n=10):
    return mp.nstr(x, n)

C_SOURCE = r'''
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <flint/acb_mat.h>
#include "zst.h"
#define P 1280
static void pr(const arb_t x) { arb_printn(x, 220, ARB_STR_NO_RADIUS); }
static void dump(FILE *f,const arb_t x) { arb_dump_file(f,x); fputc('\n',f); }
static void atom(arb_ptr a,arb_ptr b,int N,int k,const arb_t L) {
 arb_t t,u,v,pi,c,s,d; arb_init(t);arb_init(u);arb_init(v);arb_init(pi);arb_init(c);arb_init(s);arb_init(d);
 arb_set_ui(t,k);arb_log(t,t,P);arb_div(t,t,L,P);arb_one(d);arb_sub(d,d,t,P);arb_const_pi(pi,P);
 for(int n=0;n<=N;n++) {arb_mul_si(u,t,2*n,P);arb_sin_cos_pi(s,c,u,P);arb_mul(a+n,d,c,P);arb_mul_si(a+n,a+n,-2,P);arb_div(b+n,s,pi,P);}
 arb_clear(t);arb_clear(u);arb_clear(v);arb_clear(pi);arb_clear(c);arb_clear(s);arb_clear(d);
}
static int verify(const char *ballfile,const char *basisfile) {
 FILE *f=fopen(ballfile,"r"),*b=fopen(basisfile,"r"); int m,r;fscanf(f,"%d %d",&m,&r);
 arb_mat_t G,B,Y,R;arb_mat_init(G,r,m);arb_mat_init(B,m,m);arb_mat_init(Y,m,1);arb_mat_init(R,m,1);
 arb_ptr c=_arb_vec_init(r); for(int i=0;i<r;i++){arb_load_file(c+i,f);for(int j=0;j<m;j++)arb_load_file(arb_mat_entry(G,i,j),f);}fclose(f);
 int k,sign,idx[m];arb_t cost;arb_init(cost);
 while(fscanf(b,"%d %d",&k,&sign)==2){
  for(int i=0;i<m;i++)fscanf(b,"%d",idx+i);
  arb_mat_zero(R);arb_set_si(arb_mat_entry(R,k,0),sign);
  for(int i=0;i<m;i++)for(int j=0;j<m;j++)arb_set(arb_mat_entry(B,i,j),arb_mat_entry(G,idx[j],i));
  int ok=arb_mat_solve(Y,B,R,P);arb_zero(cost);
  for(int i=0;i<m;i++){ok=ok&&arb_is_nonnegative(arb_mat_entry(Y,i,0));arb_addmul(cost,c+idx[i],arb_mat_entry(Y,i,0),P);}
  printf("CERT %d %d %d ",k,sign,ok);arb_printn(cost,30,0);printf("\n");
 }
 fclose(b);return 0;
}
int main(int argc,char **argv) {
 if(!strcmp(argv[1],"verify"))return verify(argv[2],argv[3]);
 int x=atoi(argv[1]),N=atoi(argv[2]),m=x-2;const char *prefix=argv[3];
 arb_t X,L,t,u,v,s;arb_init(X);arb_init(L);arb_init(t);arb_init(u);arb_init(v);arb_init(s);arb_set_ui(X,x);arb_log(L,X,P);
 arb_ptr a=_arb_vec_init(N+1),b=_arb_vec_init(N+1),a0=_arb_vec_init(N+1),b0=_arb_vec_init(N+1),ta=_arb_vec_init(N+1),tb=_arb_vec_init(N+1);
 zst_riemann_ab(a,b,N,X,x,P);zst_riemann_ab(a0,b0,N,X,1,P);
 for(int i=0;i<=N;i++){printf("AB %d ",i);pr(a+i);printf(" ");pr(b+i);printf(" ");pr(a0+i);printf(" ");pr(b0+i);printf("\n");}
 arb_mat_t G;arb_mat_init(G,2*N+1,m);arb_ptr costs=_arb_vec_init(2*N+1);
 char path[4096];snprintf(path,sizeof(path),"%s.vec",prefix);FILE *vf=fopen(path,"w");
 for(int parity=0;parity<2;parity++) {
  int d=N+1-parity,offset=parity?(N+1):0;
  arb_mat_t H,C,V,T,W;arb_mat_init(H,d,d);arb_mat_init(C,d,d);arb_mat_init(V,d,d);arb_mat_init(T,d,d);arb_mat_init(W,d,d);
  if(parity)zst_odd_block(H,a,b,N,P);else zst_even_block(H,a,b,N,P);
  int pd=arb_mat_cho(C,H,P);printf("PD %d %d\n",parity,pd);
  if(pd)for(int i=0;i<d;i++){arb_log(t,arb_mat_entry(C,i,i),P);arb_mul_2exp_si(t,t,1);printf("PIV %d %d ",parity,i);pr(t);printf("\n");}
  if(argc>4 && !strcmp(argv[4],"scan")){arb_mat_clear(H);arb_mat_clear(C);arb_mat_clear(V);arb_mat_clear(T);arb_mat_clear(W);continue;}
  acb_mat_t A,R;acb_mat_init(A,d,d);acb_mat_init(R,d,d);acb_ptr eig=_acb_vec_init(d);mag_t tol;mag_init(tol);mag_set_ui_2exp_si(tol,1,-1100);
  acb_mat_set_arb_mat(A,H);int ok=acb_mat_approx_eig_qr(eig,NULL,R,A,tol,0,1152);printf("QR %d %d\n",parity,ok);if(!ok)return 3;
  for(int j=0;j<d;j++) {
   arb_zero(s);for(int i=0;i<d;i++){arb_get_mid_arb(arb_mat_entry(V,i,j),acb_realref(acb_mat_entry(R,i,j)));arb_addmul(s,arb_mat_entry(V,i,j),arb_mat_entry(V,i,j),P);}arb_sqrt(s,s,P);
   for(int i=0;i<d;i++){arb_div(t,arb_mat_entry(V,i,j),s,P);arb_get_mid_arb(arb_mat_entry(V,i,j),t);if(N<=40){fprintf(vf,"%d %d %d ",parity,i,j);arb_fprintn(vf,arb_mat_entry(V,i,j),220,ARB_STR_NO_RADIUS);fputc('\n',vf);}}
  }
  arb_mat_mul(W,H,V,P);
  for(int j=0;j<d;j++){
   arb_zero(costs+offset+j);for(int i=0;i<d;i++)arb_addmul(costs+offset+j,arb_mat_entry(V,i,j),arb_mat_entry(W,i,j),P);
   printf("EIG %d ",offset+j);pr(costs+offset+j);printf("\n");
  }
  for(int k=2;k<x;k++){
   atom(ta,tb,N,k,L);if(parity)zst_odd_block(T,ta,tb,N,P);else zst_even_block(T,ta,tb,N,P);arb_mat_mul(W,T,V,P);
   for(int j=0;j<d;j++)for(int i=0;i<d;i++)arb_addmul(arb_mat_entry(G,offset+j,k-2),arb_mat_entry(V,i,j),arb_mat_entry(W,i,j),P);
  }
  arb_mat_clear(H);arb_mat_clear(C);arb_mat_clear(V);arb_mat_clear(T);arb_mat_clear(W);acb_mat_clear(A);acb_mat_clear(R);_acb_vec_clear(eig,d);mag_clear(tol);
 }
 fclose(vf);snprintf(path,sizeof(path),"%s.balls",prefix);FILE *bf=fopen(path,"w");fprintf(bf,"%d %d\n",m,2*N+1);
 for(int i=0;i<2*N+1;i++){dump(bf,costs+i);printf("G %d",i);for(int k=0;k<m;k++){dump(bf,arb_mat_entry(G,i,k));printf(" ");pr(arb_mat_entry(G,i,k));}printf("\n");}
 fclose(bf);return 0;
}
'''

def build():
    source = CHECKS/'bridge.c'
    binary = CHECKS/'bridge'
    if not source.exists() or source.read_text()!=C_SOURCE or not binary.exists():
        source.write_text(C_SOURCE)
        subprocess.run(['cc','-O2','-I'+str(ROOT/'zst/include'),str(source),str(ROOT/'zst/build/libzst.a'),'-lflint','-lmpfr','-lgmp','-lm','-o',str(binary)],check=True)
    return binary

def produce(x,N):
    prefix=CHECKS/f'x{x}_N{N}'
    path=prefix.with_suffix('.data')
    if not path.exists():
        with path.with_suffix('.partial').open('w') as f:
            subprocess.run([str(CHECKS/'bridge'),str(x),str(N),str(prefix)],stdout=f,check=True)
        path.with_suffix('.partial').replace(path)
    return path

def load_case(x,N):
    lines=produce(x,N).read_text().splitlines()
    G=[]; c=[]; ab=[]; piv=[[],[]];pd=[]
    for line in lines:
        s=line.split()
        if s[0]=='AB':ab.append(list(map(mp.mpf,s[2:])))
        if s[0]=='G':G.append(list(map(mp.mpf,s[2:])))
        if s[0]=='EIG':c.append(mp.mpf(s[2]))
        if s[0]=='PD':pd.append(int(s[2]))
        if s[0]=='PIV':piv[int(s[1])].append(mp.mpf(s[3]))
    return dict(x=x,N=N,G=mp.matrix(G),c=mp.matrix(c),ab=ab,piv=piv,pd=pd)

def simplex(c,A,b,warm=None):
    """200-digit two-phase tableau with Bland pivots; full primal/dual audit follows."""
    m,n=A.rows,A.cols
    sign=[-1 if b[i]<0 else 1 for i in range(m)]
    T=[[sign[i]*A[i,j] for j in range(n)]+[mp.mpf(i==j) for j in range(m)]+[sign[i]*b[i]] for i in range(m)]
    basis=list(range(n,n+m));tol=mp.mpf('1e-175')
    def pivot(r,s):
        p=T[r][s];T[r]=[v/p for v in T[r]]
        for i in range(m):
            if i!=r:
                f=T[i][s]
                T[i]=[v-f*u for v,u in zip(T[i],T[r])]
        basis[r]=s
    def solve(cost,allowed):
        for iteration in range(20000):
            cb=[cost[j] for j in basis]
            red=[cost[j]-mp.fsum(cb[i]*T[i][j] for i in range(m)) for j in range(allowed)]
            ent=next((j for j in range(allowed) if j not in basis and red[j]<-tol),None)
            if ent is None:return
            rr=[(T[i][-1]/T[i][ent],basis[i],i) for i in range(m) if T[i][ent]>tol]
            if not rr:raise RuntimeError('unbounded simplex phase')
            pivot(min(rr)[2],ent)
        raise RuntimeError('simplex iteration limit')
    solve([mp.mpf(0)]*n+[mp.mpf(1)]*m,n+m)
    if sum(T[i][-1] for i in range(m) if basis[i]>=n)>mp.mpf('1e-150'):
        raise RuntimeError('infeasible LP dual')
    for i in range(m):
        if basis[i]>=n:
            ent=next(j for j in range(n) if j not in basis and abs(T[i][j])>tol)
            pivot(i,ent)
    solve(list(c)+[mp.mpf(0)]*m,n)
    B=mp.matrix([[A[i,j] for j in basis] for i in range(m)]);y=mp.lu_solve(B,b);z=mp.lu_solve(B.T,mp.matrix([c[j] for j in basis]))
    residual=mp.norm(B*y-b,mp.inf);slack=c-A.T*z
    val=mp.fdot(y,[c[j] for j in basis]);gap=abs(val-mp.fdot(b,z))
    return val,basis,y,residual,min(slack),gap

def solve_case(x,N):
    D=load_case(x,N);G=D['G'];c=D['c'];m=x-2
    print(f'CASE x={x} N={N} m={m} mp_dps=200 arb_bits=1280',flush=True)
    check(D['pd']==[1,1], 'ball Cholesky certifies both true finite blocks positive')
    # Cross-check the atom convention independently of C's construction.
    err=mp.mpf(0)
    for j,(a,b,a0,b0) in enumerate(D['ab']):
        pa=pb=mp.mpf(0)
        for k in range(2,x):
            w=von_mangoldt(k)/mp.sqrt(k);t=mp.log(k)/mp.log(x)
            pa-=2*w*(1-t)*mp.cos(2*mp.pi*j*t);pb+=w*mp.sin(2*mp.pi*j*t)/mp.pi
        err=max(err,abs(a-a0-pa),abs(b-b0-pb))
    check(err<mp.mpf('1e-190'),f'prime-cutoff split reproduced, error={ns(err,3)}')
    lams=sorted(c);print('SPECTRUM eps='+ns(lams[0])+' lambda_m='+ns(lams[m-1])+' lambda_mplus1='+ns(lams[m]))
    A=G.T;rows=[];basislines=[];certs=[]
    for k in range(m):
        vals=[];search=[]
        for sign in (1,-1):
            b=mp.matrix(m,1);b[k]=sign
            # Double is a search diagnostic only; never accepted as the final answer.
            gd=np.array(A.tolist(),float);cd=np.array(list(c),float)
            rr=linprog(cd,A_eq=gd,b_eq=np.array(list(b),float),bounds=(0,None),method='highs')
            search.append(float(rr.fun) if rr.success else None)
            val,ix,y,res,slack,gap=simplex(c,A,b)
            good=min(y)>=0 and res<mp.mpf('1e-150') and slack>=-mp.mpf('1e-150') and gap<mp.mpf('1e-150')
            check(good,f'LP n={k+2} sign={sign:+d}: residual={ns(res,2)}, min_reduced={ns(slack,2)}, gap={ns(gap,2)}')
            vals.append(val);basislines.append(' '.join(map(str,[k,sign]+ix)))
            certs.append(dict(k=k,sign=sign,basis=ix,y=[str(v) for v in y],value=str(val)))
        rows.append(dict(n=k+2,lo=str(-vals[0]),hi=str(vals[1]),width=str(sum(vals)),highs=search))
        print(f'WIDTH n={k+2} LP={ns(sum(vals),12)} lower={ns(-vals[0])} upper={ns(vals[1])} highs_width={sum(v for v in search if v is not None):.6g}',flush=True)
    prefix=CHECKS/f'x{x}_N{N}'
    prefix.with_suffix('.bases').write_text('\n'.join(basislines)+'\n')
    result=subprocess.run([str(CHECKS/'bridge'),'verify',str(prefix.with_suffix('.balls')),str(prefix.with_suffix('.bases'))],capture_output=True,text=True,check=True).stdout
    prefix.with_suffix('.certificates').write_text(result)
    check(len(result.splitlines())==2*m and all(s.split()[3]=='1' for s in result.splitlines()),'ALL supported duals solved and certified nonnegative in 1280-bit balls')
    print(result,end='')
    out=dict(x=x,N=N,eps=str(lams[0]),lambda_m=str(lams[m-1]),lambda_mplus1=str(lams[m]),rows=rows,certs=certs)
    prefix.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    return out

def von_mangoldt(n):
    for p in range(2,n+1):
        if n%p==0:
            q=n
            while q%p==0:q//=p
            return mp.log(p) if q==1 else mp.mpf(0)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--case',nargs=2,type=int);parser.add_argument('--produce',nargs=2,type=int)
    args=parser.parse_args();build()
    if args.produce:produce(*args.produce);return
    if args.case:solve_case(*args.case)
    else:
        print('RTP-2 lane L; codex:gpt-6-astra; no numerical zeros; deterministic')
        # Interior nodes only. The endpoint is identically invisible for every x.
        sat={13:56,17:81,19:94,23:120,25:134}
        cases=[(13,20),(13,40)]+[(x,n) for x in sat for n in (sat[x],60)]
        with concurrent.futures.ProcessPoolExecutor(max_workers=6) as pool:
            list(pool.map(produce_pair,cases))
        for x,N in cases:solve_case(x,N)
    print(f'CHECKS {COUNTS[0]} FAILED {COUNTS[1]}',flush=True)
    if COUNTS[1]:sys.exit(1)

def produce_pair(pair):return produce(*pair)

if __name__=='__main__':main()
