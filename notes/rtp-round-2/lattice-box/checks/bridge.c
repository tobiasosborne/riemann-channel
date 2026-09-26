
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
