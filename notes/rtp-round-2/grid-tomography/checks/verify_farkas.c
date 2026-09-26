
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
