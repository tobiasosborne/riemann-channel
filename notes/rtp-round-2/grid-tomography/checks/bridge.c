
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
