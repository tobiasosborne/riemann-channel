
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
