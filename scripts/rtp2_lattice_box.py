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
static int conecheck(const char *input) {
 FILE *f=fopen(input,"r");char mode[32],buf[4096];int N,m;
 arb_t L,t,u;arb_init(L);arb_init(t);arb_init(u);arb_set_ui(L,13);arb_log(L,L,P);
 while(fscanf(f,"%31s %d %d",mode,&N,&m)==3){
  int d=2*N+1;arb_mat_struct *T=flint_malloc(m*sizeof(arb_mat_struct));
  arb_ptr a=_arb_vec_init(N+1),b=_arb_vec_init(N+1);
  arb_mat_t Z,C,Gram,rhs,h;arb_mat_init(Z,d,d);arb_mat_init(C,d,d);arb_mat_init(Gram,m,m);arb_mat_init(rhs,m,1);arb_mat_init(h,m,1);
  for(int k=0;k<m;k++){
   arb_mat_init(T+k,d,d);atom(a,b,N,k+2,L);
   for(int i=-N;i<=N;i++)for(int j=-N;j<=N;j++){
    if(i==j)arb_set(arb_mat_entry(T+k,i+N,j+N),a+abs(i));
    else {arb_set(t,b+abs(i));if(i<0)arb_neg(t,t);arb_set(u,b+abs(j));if(j<0)arb_neg(u,u);arb_sub(t,t,u,P);arb_div_si(arb_mat_entry(T+k,i+N,j+N),t,i-j,P);}
   }
  }
  int ok=1;
  if(!strcmp(mode,"RAY")){
   for(int k=0;k<m;k++){if(fscanf(f,"%4095s",buf)!=1)return 8;arb_set_str(t,buf,P);for(int i=0;i<d;i++)for(int j=0;j<d;j++)arb_addmul(arb_mat_entry(Z,i,j),t,arb_mat_entry(T+k,i,j),P);}
  }else{
   for(int i=0;i<d;i++)for(int j=0;j<d;j++){if(fscanf(f,"%4095s",buf)!=1)return 8;arb_set_str(arb_mat_entry(Z,i,j),buf,P);}
   for(int k=0;k<m;k++){
    for(int i=0;i<d;i++)for(int j=0;j<d;j++)arb_addmul(arb_mat_entry(rhs,k,0),arb_mat_entry(T+k,i,j),arb_mat_entry(Z,i,j),P);
    for(int l=0;l<m;l++)for(int i=0;i<d;i++)for(int j=0;j<d;j++)arb_addmul(arb_mat_entry(Gram,k,l),arb_mat_entry(T+k,i,j),arb_mat_entry(T+l,i,j),P);
   }
   ok=arb_mat_solve(h,Gram,rhs,P);
   for(int k=0;k<m;k++)for(int i=0;i<d;i++)for(int j=0;j<d;j++)arb_submul(arb_mat_entry(Z,i,j),arb_mat_entry(h,k,0),arb_mat_entry(T+k,i,j),P);
  }
  ok=ok&&arb_mat_cho(C,Z,P);printf("CONE %s N=%d m=%d certified=%d\n",mode,N,m,ok);
  for(int k=0;k<m;k++)arb_mat_clear(T+k);flint_free(T);_arb_vec_clear(a,N+1);_arb_vec_clear(b,N+1);arb_mat_clear(Z);arb_mat_clear(C);arb_mat_clear(Gram);arb_mat_clear(rhs);arb_mat_clear(h);
 }
 fclose(f);return 0;
}
static int verify(const char *ballfile,const char *basisfile) {
 FILE *f=fopen(ballfile,"r"),*b=fopen(basisfile,"r"); int m,r;if(fscanf(f,"%d %d",&m,&r)!=2)return 8;
 arb_mat_t G,B,Y,R;arb_mat_init(G,r,m);arb_mat_init(B,m,m);arb_mat_init(Y,m,1);arb_mat_init(R,m,1);
 arb_ptr c=_arb_vec_init(r); for(int i=0;i<r;i++){arb_load_file(c+i,f);for(int j=0;j<m;j++)arb_load_file(arb_mat_entry(G,i,j),f);}fclose(f);
 int k,sign,idx[m];arb_t cost;arb_init(cost);
 while(fscanf(b,"%d %d",&k,&sign)==2){
  for(int i=0;i<m;i++)if(fscanf(b,"%d",idx+i)!=1)return 8;
  arb_mat_zero(R);arb_set_si(arb_mat_entry(R,k,0),sign);
  for(int i=0;i<m;i++)for(int j=0;j<m;j++)arb_set(arb_mat_entry(B,i,j),arb_mat_entry(G,idx[j],i));
  int ok=arb_mat_solve(Y,B,R,P);arb_zero(cost);
  for(int i=0;i<m;i++){ok=ok&&arb_is_nonnegative(arb_mat_entry(Y,i,0));arb_addmul(cost,c+idx[i],arb_mat_entry(Y,i,0),P);}
  arb_mat_transpose(B,B);for(int j=0;j<m;j++)arb_set(arb_mat_entry(R,j,0),c+idx[j]);
  int opt=arb_mat_solve(Y,B,R,P);arb_t slack;arb_init(slack);
  for(int i=0;i<r;i++){
   int basic=0;for(int j=0;j<m;j++)if(i==idx[j])basic=1;
   if(!basic){arb_set(slack,c+i);for(int j=0;j<m;j++)arb_submul(slack,arb_mat_entry(G,i,j),arb_mat_entry(Y,j,0),P);opt=opt&&arb_is_nonnegative(slack);}
  }
  printf("CERT %d %d %d ",k,sign,ok);arb_printn(cost,30,0);printf(" OPT=%d\n",opt);arb_clear(slack);
 }
 fclose(b);return 0;
}
static int sectioncheck(const char *input) {
 FILE *f=fopen(input,"r");int N,k,l,sgn;char buf[4096];
 while(fscanf(f,"%d %d %d %d",&N,&k,&l,&sgn)==4){
  arb_t X,L,dt,ds,cost,t;arb_init(X);arb_init(L);arb_init(dt);arb_init(ds);arb_init(cost);arb_init(t);arb_set_ui(X,13);arb_log(L,X,P);
  if(fscanf(f,"%4095s",buf)!=1)return 8;arb_set_str(dt,buf,P);if(fscanf(f,"%4095s",buf)!=1)return 8;arb_set_str(ds,buf,P);
  arb_ptr a=_arb_vec_init(N+1),b=_arb_vec_init(N+1);arb_mat_struct H[2],Tk[2],Tl[2];
  for(int p=0;p<2;p++){int d=N+1-p;arb_mat_init(H+p,d,d);arb_mat_init(Tk+p,d,d);arb_mat_init(Tl+p,d,d);}
  zst_riemann_ab(a,b,N,X,13,P);zst_even_block(H,a,b,N,P);zst_odd_block(H+1,a,b,N,P);
  atom(a,b,N,k,L);zst_even_block(Tk,a,b,N,P);zst_odd_block(Tk+1,a,b,N,P);
  atom(a,b,N,l,L);zst_even_block(Tl,a,b,N,P);zst_odd_block(Tl+1,a,b,N,P);
  int primal=1,dual=1;
  for(int p=0;p<2;p++){
   int d=N+1-p;arb_mat_t M,C;arb_mat_init(M,d,d);arb_mat_init(C,d,d);arb_mat_set(M,H+p);
   for(int i=0;i<d;i++)for(int j=0;j<d;j++){arb_addmul(arb_mat_entry(M,i,j),dt,arb_mat_entry(Tk+p,i,j),P);arb_addmul(arb_mat_entry(M,i,j),ds,arb_mat_entry(Tl+p,i,j),P);}
   primal=primal&&arb_mat_cho(C,M,P);arb_mat_clear(M);arb_mat_clear(C);
  }
  arb_mat_t B,Y,R;arb_mat_init(B,2,2);arb_mat_init(Y,2,1);arb_mat_init(R,2,1);arb_ptr lam=_arb_vec_init(2);
  for(int z=0;z<2;z++){
   int p;if(fscanf(f,"%d",&p)!=1)return 8;int d=N+1-p;arb_ptr v=_arb_vec_init(d);
   for(int i=0;i<d;i++){if(fscanf(f,"%4095s",buf)!=1)return 8;arb_set_str(v+i,buf,P);}
   for(int i=0;i<d;i++)for(int j=0;j<d;j++){
    arb_mul(t,v+i,v+j,P);arb_addmul(lam+z,t,arb_mat_entry(H+p,i,j),P);arb_addmul(arb_mat_entry(B,0,z),t,arb_mat_entry(Tk+p,i,j),P);arb_addmul(arb_mat_entry(B,1,z),t,arb_mat_entry(Tl+p,i,j),P);
   }
   _arb_vec_clear(v,d);
  }
  arb_set_si(arb_mat_entry(R,0,0),-sgn);dual=arb_mat_solve(Y,B,R,P);
  for(int z=0;z<2;z++){dual=dual&&arb_is_nonnegative(arb_mat_entry(Y,z,0));arb_addmul(cost,lam+z,arb_mat_entry(Y,z,0),P);}
  printf("SECTIONCERT N=%d target=%d other=%d sign=%d primal=%d dual=%d ",N,k,l,sgn,primal,dual);arb_printn(cost,30,0);printf("\n");
  for(int p=0;p<2;p++){arb_mat_clear(H+p);arb_mat_clear(Tk+p);arb_mat_clear(Tl+p);}arb_mat_clear(B);arb_mat_clear(Y);arb_mat_clear(R);_arb_vec_clear(a,N+1);_arb_vec_clear(b,N+1);_arb_vec_clear(lam,2);arb_clear(X);arb_clear(L);arb_clear(dt);arb_clear(ds);arb_clear(cost);arb_clear(t);
 }
 fclose(f);return 0;
}
int main(int argc,char **argv) {
 if(!strcmp(argv[1],"verify"))return verify(argv[2],argv[3]);
 if(!strcmp(argv[1],"conecheck"))return conecheck(argv[2]);
 if(!strcmp(argv[1],"sectioncheck"))return sectioncheck(argv[2]);
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
    def audit(basis):
        B=mp.matrix([[A[i,j] for j in basis] for i in range(m)])
        y=mp.lu_solve(B,b);z=mp.lu_solve(B.T,mp.matrix([c[j] for j in basis]))
        residual=mp.norm(B*y-b,mp.inf);slack=c-A.T*z
        val=mp.fdot(y,[c[j] for j in basis]);gap=abs(val-mp.fdot(b,z))
        return val,basis,y,residual,min(slack),gap
    if warm is not None:
        out=audit(warm)
        if min(out[2])>=0 and out[4]>=-mp.mpf('1e-150'):return out
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
    return audit(basis)

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
    cache=CHECKS/f'x{x}_N{N}.json'
    warm={(q['k'],q['sign']):q['basis'] for q in json.loads(cache.read_text())['certs']} if cache.exists() else {}
    for k in range(m):
        vals=[];search=[]
        for sign in (1,-1):
            b=mp.matrix(m,1);b[k]=sign
            # Double is a search diagnostic only; never accepted as the final answer.
            gd=np.array(A.tolist(),float);cd=np.array(list(c),float)
            rr=linprog(cd,A_eq=gd,b_eq=np.array(list(b),float),bounds=(0,None),method='highs')
            search.append(float(rr.fun) if rr.success else None)
            val,ix,y,res,slack,gap=simplex(c,A,b,warm.get((k,sign)))
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
    check(all(s.endswith('OPT=1') for s in result.splitlines()),'ball primal inequalities and dual equalities certify optimality of every fixed-vector LP')
    out=dict(x=x,N=N,eps=str(lams[0]),lambda_m=str(lams[m-1]),lambda_mplus1=str(lams[m]),rows=rows,certs=certs)
    prefix.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    return out

def von_mangoldt(n):
    for p in range(2,n+1):
        if n%p==0:
            q=n
            while q%p==0:q//=p
            return mp.log(p) if q==1 else mp.mpf(0)

def atom_numpy(N,m):
    n=np.arange(-N,N+1);t=np.log(np.arange(2,m+2))/np.log(13)
    b=np.sin(2*np.pi*t[:,None]*n[None,:])/np.pi
    diff=n[:,None]-n[None,:];np.fill_diagonal(diff,1)
    T=(b[:,:,None]-b[:,None,:])/diff
    for j in range(m):np.fill_diagonal(T[j],-2*(1-t[j])*np.cos(2*np.pi*n*t[j]))
    return T

def cone_search(N,m):
    """Trace-one max-min SDP by eigenvector separation; double search only."""
    T=atom_numpy(N,m);d=T.shape[1];U,s,V=np.linalg.svd(T.reshape(m,-1),full_matrices=False)
    if m>2*N+1:return 'KERNEL',None,None,0
    S=V.reshape(m,d,d);tr=np.trace(S,axis1=1,axis2=2)
    vv=list(np.eye(d));cuts=[S[:,i,i] for i in range(d)]
    for iteration in range(1000):
        rr=linprog(np.r_[np.zeros(m),-1],A_ub=np.column_stack([-np.array(cuts),np.ones(len(cuts))]),b_ub=np.zeros(len(cuts)),A_eq=np.r_[tr,0][None,:],b_eq=[1],bounds=[(None,None)]*(m+1),method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
        if not rr.success:raise RuntimeError('cone separation LP failed')
        delta=U@(rr.x[:m]/s);M=np.einsum('k,kij->ij',delta,T);e,v=np.linalg.eigh(M)
        if e[0]>1e-9:return 'RAY',delta,None,float(e[0])
        if rr.x[-1]<-1e-9:
            alpha=-rr.ineqlin.marginals
            Z=sum(a*np.outer(v,v) for a,v in zip(alpha,vv))-rr.x[-1]*np.eye(d)
            return 'ZERO',None,Z,float(-rr.x[-1])
        for j in range(min(d,4)):
            vv.append(v[:,j]);cuts.append(np.einsum('i,kij,j->k',v[:,j],S,v[:,j]))
    raise RuntimeError('cone separation did not terminate')

def recession():
    print('L5 RECESSION: double separation search; 1280-bit ball verification; N=2..40 by nesting')
    records=[];textrows=[]
    for m in range(2,12):
        for N in range(1,41):
            kind,delta,Z,margin=cone_search(N,m)
            record=dict(m=m,N=N,kind=kind,search_margin=margin)
            if kind=='RAY':
                textrows.append('RAY '+str(N)+' '+str(m)+' '+' '.join(format(v,'.17g') for v in delta))
                record['delta']=delta.tolist()
            if kind=='ZERO':
                # Exact projection onto the atom orthogonal complement is performed in balls.
                Z=(Z+Z.T)/2
                textrows.append('ZERO '+str(N)+' '+str(m)+' '+' '.join(format(v,'.17g') for v in Z.ravel()))
            records.append(record)
            if kind=='ZERO':
                print(f'THRESHOLD m={m} first_N={N} dual_search_margin={margin:.8g}; zero cone for every N={N}..40')
                break
    inp=CHECKS/'recession.in';inp.write_text('\n'.join(textrows)+'\n')
    out=subprocess.run([str(CHECKS/'bridge'),'conecheck',str(inp)],check=True,capture_output=True,text=True).stdout
    (CHECKS/'recession.certificates').write_text(out)
    print(out,end='')
    check(len(out.splitlines())==len(textrows) and all(s.endswith('certified=1') for s in out.splitlines()),'all recession rays and positive-definite dual annihilators certified in balls')
    (CHECKS/'recession.json').write_text(json.dumps(records,indent=2)+'\n')

def saturation_one(x):
    prefix=CHECKS/f'scan_x{x}';path=prefix.with_suffix('.data')
    if not path.exists():
        with path.open('w') as f:subprocess.run([str(CHECKS/'bridge'),str(x),'200',str(prefix),'scan'],stdout=f,check=True)
    piv=[[],[]]
    for line in path.read_text().splitlines():
        s=line.split()
        if s[0]=='PIV':piv[int(s[1])].append(mp.mpf(s[3]))
    if [len(p) for p in piv]!=[201,200]:raise RuntimeError('saturation Cholesky failed')
    vals=[mp.fsum(piv[0][:N+1])+mp.fsum(piv[1][:N]) for N in range(201)]
    N=min(range(201),key=lambda n:vals[n])
    return x,N,ns(vals[N],12)

def blocks_mp(a,b,N):
    E=mp.matrix(N+1);O=mp.matrix(N);E[0,0]=a[0]
    for i in range(1,N+1):
        E[0,i]=E[i,0]=mp.sqrt(2)*b[i]/i
        E[i,i]=a[i]+b[i]/i;O[i-1,i-1]=a[i]-b[i]/i
        for j in range(1,i):
            t=(b[i]-b[j])/(i-j);u=(b[i]+b[j])/(i+j)
            E[i,j]=E[j,i]=t+u;O[i-1,j-1]=O[j-1,i-1]=t-u
    return E,O

def atom_mp(N,n,x=13):
    t=mp.log(n)/mp.log(x)
    a=[-2*(1-t)*mp.cos(2*mp.pi*j*t) for j in range(N+1)]
    b=[mp.sin(2*mp.pi*j*t)/mp.pi for j in range(N+1)]
    return blocks_mp(a,b,N)

def two_sections(N):
    """Two-coordinate SDP projections: feasible points and rank-two dual bounds.

    Whitening at 200 digits; scalar convex eigenvalue search in double, followed
    by 200-digit Rayleigh dual equations and eigenvalue feasibility checks.
    These are sections (all other coordinates fixed at truth), NOT full boxes.
    """
    D=load_case(13,N);H=blocks_mp([r[0] for r in D['ab']],[r[1] for r in D['ab']],N)
    Li=[mp.inverse(mp.cholesky(h)) for h in H]
    S={};scale={};raw={}
    for k in range(2,13):
        raw[k]=atom_mp(N,k)
        S[k]=[l*t*l.T for l,t in zip(Li,raw[k])]
        scale[k]=1/max(mp.mnorm(t,1) for t in S[k])
        S[k]=[t*scale[k] for t in S[k]]
    rows=[];certificate_input=[]
    for k,l in [(2,3),(4,5),(6,7),(8,9),(10,12),(11,12)]:
        for target,other in ((k,l),(l,k)):
            ends=[];uppers=[]
            for sign in (-1,1):
                A=[s*sign for s in S[target]];B=S[other]
                ad=[np.array(t.tolist(),float) for t in A];bd=[np.array(t.tolist(),float) for t in B]
                def ev(r):
                    ans=[]
                    for parity,(a,b) in enumerate(zip(ad,bd)):
                        e,v=np.linalg.eigh(-a-r*b);vv=v[:,-1]
                        ans.append((e[-1],-vv@b@vv,parity,vv))
                    return max(ans,key=lambda q:q[0])
                lo,hi=-1.,1.
                while ev(lo)[1]>=0:lo*=2
                while ev(hi)[1]<=0:hi*=2
                for _ in range(70):
                    mid=(lo+hi)/2
                    if mid==lo or mid==hi:break
                    if ev(mid)[1]<0:lo=mid
                    else:hi=mid
                # Widen around the minimizer to obtain two strict opposite sensitivities.
                radius=max(1,abs((lo+hi)/2))*1e-7;mid=(lo+hi)/2
                samples=[ev(mid-radius),ev(mid+radius)]
                coeff=[]
                origvecs=[]
                for val,der,p,v in samples:
                    vv=mp.matrix([mp.mpf(float(t)) for t in v]);vv/=mp.norm(vv)
                    coeff.append(((vv.T*A[p]*vv)[0],(vv.T*B[p]*vv)[0]))
                    origvecs.append((p,Li[p].T*vv))
                Y=mp.lu_solve(mp.matrix([[z[0] for z in coeff],[z[1] for z in coeff]]),mp.matrix([-1,0]))
                upper=mp.fsum(Y)
                # Construct an interior primal point by the exact ray endpoint.
                r=mp.mpf(mid)
                maxeig=max(max(mp.eigsy(-(a+r*b),eigvals_only=True)) for a,b in zip(A,B))
                xi=(1-mp.mpf('1e-12'))/maxeig;eta=r*xi
                good=min(Y)>=0 and upper>=xi and (upper-xi)/xi<mp.mpf('1e-5')
                for a,b in zip(A,B):
                    try:mp.cholesky(mp.eye(a.rows)+xi*a+eta*b)
                    except ValueError:good=False
                # Recheck in unwhitened original coordinates, so a whitening error cannot pass silently.
                dt=sign*scale[target]*xi;do=scale[other]*eta
                certificate_input.append(' '.join(map(str,[N,target,other,sign]))+' '+mp.nstr(dt,200)+' '+mp.nstr(do,200))
                for p,vv in origvecs:certificate_input.append(str(p)+' '+' '.join(mp.nstr(t,200) for t in vv))
                for p in (0,1):
                    try:mp.cholesky(H[p]+dt*raw[target][p]+do*raw[other][p])
                    except ValueError:good=False
                check(good,f'section N={N} pair={k},{l} target={target} sign={sign:+d}: relative primal-dual gap={ns((upper-xi)/xi,3)}')
                ends.append(xi*scale[target]);uppers.append(upper*scale[target])
            row=dict(N=N,pair=[k,l],n=target,inner=str(sum(ends)),outer=str(sum(uppers)))
            rows.append(row)
            print(f'SECTION N={N} pair={k},{l} n={target} width_in={ns(sum(ends),12)} width_out={ns(sum(uppers),12)}',flush=True)
    (CHECKS/f'sections_N{N}.json').write_text(json.dumps(rows,indent=2)+'\n')
    inp=CHECKS/f'sections_N{N}.in';inp.write_text('\n'.join(certificate_input)+'\n')
    result=subprocess.run([str(CHECKS/'bridge'),'sectioncheck',str(inp)],capture_output=True,text=True,check=True).stdout
    (CHECKS/f'sections_N{N}.certificates').write_text(result)
    print(result,end='')
    check(len(result.splitlines())==24 and all('primal=1 dual=1' in s for s in result.splitlines()),f'all N={N} section primal and rank-two dual witnesses certified in 1280-bit balls')
    return rows

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--case',nargs=2,type=int);parser.add_argument('--produce',nargs=2,type=int);parser.add_argument('--recession',action='store_true');parser.add_argument('--sections',type=int)
    args=parser.parse_args();build()
    if args.produce:produce(*args.produce);return
    if args.sections:two_sections(args.sections)
    elif args.recession:recession()
    elif args.case:solve_case(*args.case)
    else:
        print('RTP-2 lane L; codex:gpt-6-astra; no numerical zeros; deterministic')
        # Interior nodes only. The endpoint is identically invisible for every x.
        scans=[saturation_one(x) for x in (13,17,19,23,25)]
        for x,N,ld in scans:print(f'SATURATION x={x} N={N} logdet={ld}; scan 0..200, 1280-bit Cholesky pivots')
        sat={x:N for x,N,ld in scans}
        cases=[(13,20),(13,40)]+[(x,n) for x in sat for n in (sat[x],60)]
        with concurrent.futures.ProcessPoolExecutor(max_workers=6) as pool:
            list(pool.map(produce_pair,cases))
        for x,N in cases:solve_case(x,N)
        for N in (20,40):two_sections(N)
        recession()
    print(f'CHECKS {COUNTS[0]} FAILED {COUNTS[1]}',flush=True)
    if COUNTS[1]:sys.exit(1)

def produce_pair(pair):return produce(*pair)

if __name__=='__main__':main()
