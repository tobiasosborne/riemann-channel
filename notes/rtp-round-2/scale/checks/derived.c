/* Certified comparisons with the quoted asymptotic expression, not with an
 * enclosed finite-x prolate eigenvalue. Author codex:gpt-6-astra. */
#include <stdio.h>
#include <flint/arb.h>
int main(void) {
 const slong p=512;arb_t x,L,C,P,eps,q,a,prev,dx,t;
 arb_init(x);arb_init(L);arb_init(C);arb_init(P);arb_init(eps);arb_init(q);arb_init(a);arb_init(prev);arb_init(dx);arb_init(t);
 arb_const_pi(C,p);arb_pow_ui(C,C,5,p);arb_sqrt_ui(t,2,p);arb_mul(C,C,t,p);arb_mul_ui(C,C,16384,p);arb_div_ui(C,C,3,p);
 arb_const_pi(a,p);arb_mul_ui(a,a,4,p);arb_log_ui(t,10,p);arb_div(a,a,t,p);
 printf("a0=");arb_printn(a,16,0);printf("\nC=");arb_printn(C,16,0);printf("\n");
 long X,N,Nc,prec,oldX=0;char line[4096];
 while(scanf("%ld %ld %ld %ld ",&X,&Nc,&N,&prec)==4) {
  if(!fgets(line,sizeof(line),stdin)||arb_set_str(eps,line,p))return 2;
  arb_set_si(x,X);arb_log(L,x,p);arb_mul_si(t,L,9,p);arb_mul_2exp_si(t,t,-1);
  arb_const_pi(P,p);arb_mul_ui(P,P,4*X,p);arb_sub(P,t,P,p);arb_exp(P,P,p);arb_mul(P,P,C,p);
  printf("x=%ld N_conv=%ld N_final=%ld prec=%ld\nP=",X,Nc,N,prec);arb_printn(P,16,0);printf("\n");
  arb_div(q,eps,P,p);printf("eps_over_P=");arb_printn(q,16,0);printf("\n");
  arb_mul(t,x,L,p);arb_set_si(q,Nc);arb_div(q,q,t,p);printf("N_conv_over_xlogx=");arb_printn(q,16,0);printf("\n");
  if(oldX) {
   arb_div(q,prev,eps,p);arb_log(q,q,p);arb_log_ui(t,10,p);arb_mul_si(t,t,X-oldX,p);arb_div(q,q,t,p);
   printf("slope_%ld_to_%ld=",oldX,X);arb_printn(q,16,0);printf("\n");
  }
  arb_set(prev,eps);oldX=X;
 }
 arb_clear(x);arb_clear(L);arb_clear(C);arb_clear(P);arb_clear(eps);arb_clear(q);arb_clear(a);arb_clear(prev);arb_clear(dx);arb_clear(t);flint_cleanup();return 0;
}
