#define _POSIX_C_SOURCE 200809L
/* RTP-2 lane S. Author codex:gpt-6-astra.
 * Form: unchanged libzst, plan.md 1.1--1.5. Certificate proof in lane report.
 * No zero is used before comparison(). OpenMP only in this driver.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <omp.h>
#include "zst.h"
static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC,&t); return t.tv_sec+1e-9*t.tv_nsec; }
static void pr(const char *key,const arb_t x) { flint_printf("%s=",key); arb_printn(x,16,0); flint_printf("\n"); }
static void must(int ok,const char *s) { if(!ok) { fprintf(stderr,"FAIL %s\n",s); exit(2); } }
/* L is unit lower triangular. At step i, w_k=L_ik d_k and
 * d_i=A_ii-shift-dot(L_i,w); L_ji=(A_ji-dot(L_j,w))/d_i.
 * Every operation is a ball operation. Only independent output cells parallelise. */
static slong ldl(arb_mat_t L,arb_ptr d,const arb_mat_t A,const arb_t shift,slong p,int midpoint)
{
 slong n=arb_mat_nrows(A),neg=0; arb_ptr w=_arb_vec_init(n); arb_t t; arb_init(t);
 for(slong i=0;i<n;i++) {
  for(slong k=0;k<i;k++) { arb_mul(w+k,arb_mat_entry(L,i,k),d+k,p); if(midpoint) arb_get_mid_arb(w+k,w+k); }
  arb_sub(t,arb_mat_entry(A,i,i),shift,p); if(midpoint) arb_get_mid_arb(t,t);
  arb_dot(d+i,t,1,arb_mat_entry(L,i,0),1,w,1,i,p); if(midpoint) arb_get_mid_arb(d+i,d+i);
  if(arb_contains_zero(d+i)) { neg=-1; break; }
  neg+=arb_is_negative(d+i); arb_one(arb_mat_entry(L,i,i));
  #pragma omp parallel for schedule(static) if(n>80)
  for(slong j=i+1;j<n;j++) {
   arb_ptr q=arb_mat_entry(L,j,i);
   arb_dot(q,arb_mat_entry(A,j,i),1,arb_mat_entry(L,j,0),1,w,1,i,p);
   if(midpoint) arb_get_mid_arb(q,q); arb_div(q,q,d+i,p); if(midpoint) arb_get_mid_arb(q,q);
  }
 }
 _arb_vec_clear(w,n); arb_clear(t); return neg;
}
static slong inertia(const arb_mat_t A,const arb_t shift,slong p)
{
 slong n=arb_mat_nrows(A); arb_mat_t L; arb_mat_init(L,n,n); arb_ptr d=_arb_vec_init(n);
 slong r=ldl(L,d,A,shift,p,0); arb_mat_clear(L); _arb_vec_clear(d,n); return r;
}
/* Approximate inverse application; certification is entirely in residuals/inertia. */
static void solve(arb_ptr u,const arb_mat_t L,arb_srcptr d,slong n,slong p)
{
 for(slong i=0;i<n;i++) { arb_dot(u+i,u+i,1,arb_mat_entry(L,i,0),1,u,1,i,p); arb_get_mid_arb(u+i,u+i); }
 for(slong i=0;i<n;i++) { arb_div(u+i,u+i,d+i,p); arb_get_mid_arb(u+i,u+i); }
 for(slong i=n-1;i>=0;i--) {
  arb_dot(u+i,u+i,1,arb_mat_entry(L,i+1<n?i+1:i,i),n,u+i+1,1,n-i-1,p);
  arb_get_mid_arb(u+i,u+i);
 }
}
/* Rigorous residual of the unit vector obtained by normalising exact dyadic u. */
static void residual(arb_t rho,arb_t r,arb_ptr v,const arb_mat_t A,arb_srcptr u,slong p)
{
 slong n=arb_mat_nrows(A); arb_ptr y=_arb_vec_init(n); arb_t norm,t; arb_init(norm);arb_init(t);
 arb_dot(norm,NULL,0,u,1,u,1,n,p); arb_sqrt(norm,norm,p);
 for(slong i=0;i<n;i++) arb_div(v+i,u+i,norm,p);
 #pragma omp parallel for schedule(static) if(n>80)
 for(slong i=0;i<n;i++) arb_dot(y+i,NULL,0,arb_mat_entry(A,i,0),1,v,1,n,p);
 arb_dot(rho,NULL,0,v,1,y,1,n,p); arb_zero(r);
 for(slong i=0;i<n;i++) { arb_mul(t,rho,v+i,p);arb_sub(t,y+i,t,p);arb_sqr(t,t,p);arb_add(r,r,t,p); }
 arb_sqrt(r,r,p); _arb_vec_clear(y,n);arb_clear(norm);arb_clear(t);
}
static int certified(arb_t eps,arb_ptr v,const arb_mat_t E,slong p)
{
 slong n=arb_mat_nrows(E); arb_mat_t L;arb_mat_init(L,n,n);
 arb_ptr d=_arb_vec_init(n),u=_arb_vec_init(n); arb_t zero,rho,r,s,t,gap,err;
 arb_init(zero);arb_init(rho);arb_init(r);arb_init(s);arb_init(t);arb_init(gap);arb_init(err);
 int ok=0; double tm=now(); slong ne=ldl(L,d,E,zero,p,0);
 fprintf(stderr,"factor n=%ld p=%ld neg=%ld seconds=%.6f\n",n,p,ne,now()-tm);
 if(ne!=0) goto done;
 /* Recompute midpoint factors: reusing interval-factor midpoints can inherit
  * the precision that arb_dot discards when radii are large. */
 if(ldl(L,d,E,zero,p,1)!=0) goto done;
 /* Discard radii only in the approximate solver. */
 for(slong i=0;i<n;i++) { arb_get_mid_arb(d+i,d+i); for(slong j=0;j<=i;j++) arb_get_mid_arb(arb_mat_entry(L,i,j),arb_mat_entry(L,i,j)); arb_one(u+i); arb_div_ui(u+i,u+i,(i+1)*(i+1),p); arb_get_mid_arb(u+i,u+i); }
 for(slong it=0;it<160;it++) {
  solve(u,L,d,n,p);slong m=0;
  for(slong i=1;i<n;i++) if(arf_cmpabs(arb_midref(u+i),arb_midref(u+m))>0) m=i;
  arb_set(t,u+m);
  for(slong i=0;i<n;i++) { arb_div(u+i,u+i,t,p);arb_get_mid_arb(u+i,u+i); }
  if(it%4==3) {
   residual(rho,r,v,E,u,p);
   /* Need vector error r/eps much smaller than eps for zero-error comparison. */
   arb_sqr(t,rho,p);arb_mul_2exp_si(t,t,-100);
   if(arb_lt(r,t)) { fprintf(stderr,"iteration n=%ld count=%ld seconds=%.6f\n",n,it+1,now()-tm);break; }
  }
 }
 residual(rho,r,v,E,u,p);
 if(!arb_is_positive(rho)) goto done;
 arb_get_mid_arb(s,rho);arb_mul_2exp_si(s,s,1);
 arb_add(t,rho,r,p);if(!arb_lt(t,s)) goto done;
 arb_sub(t,rho,r,p);if(!arb_is_positive(t)) goto done;
 ne=inertia(E,s,p); fprintf(stderr,"gap n=%ld neg=%ld seconds=%.6f\n",n,ne,now()-tm);
 if(ne!=1) goto done;
 /* Exactly one eigenvalue below s, and a spectral value in rho+/-r.
  * Distance of unit v to signed true unit eigenvector <=2r/(s-rho). */
 arb_set(eps,rho);arb_get_mag(arb_radref(t),r);arb_add_error_mag(eps,arb_radref(t));
 arb_sub(gap,s,rho,p);arb_div(err,r,gap,p);arb_mul_2exp_si(err,err,1);
 for(slong i=0;i<n;i++) arb_add_error(v+i,err);
 pr("residual_norm",r);pr("eigenvector_component_error",err);ok=1;
 done:
 arb_mat_clear(L);_arb_vec_clear(d,n);_arb_vec_clear(u,n);
 arb_clear(zero);arb_clear(rho);arb_clear(r);arb_clear(s);arb_clear(t);arb_clear(gap);arb_clear(err);return ok;
}
/* Form-only initial root: bracket by a positive real grid before any zeta query.
 * Full libzst secular-root pipeline used for the endpoint comparison. */
static void comparison(arb_srcptr v,slong N,const arb_t x,const arb_t eps,slong p)
{
 arb_ptr xi=_arb_vec_init(N+1),roots=_arb_vec_init(N);arb_t t,sum,L,z,gamma,err,ratio;
 arb_init(t);arb_init(sum);arb_init(L);arb_init(z);arb_init(gamma);arb_init(err);arb_init(ratio);
 arb_sqrt_ui(t,2,p);arb_set(xi,v);
 for(slong i=1;i<=N;i++) arb_div(xi+i,v+i,t,p);
 arb_set(sum,xi);for(slong i=1;i<=N;i++) { arb_mul_2exp_si(t,xi+i,1);arb_add(sum,sum,t,p); }
 must(!arb_contains_zero(sum),"edge normalisation nonzero");
 for(slong i=0;i<=N;i++) arb_div(xi+i,xi+i,sum,p);
 slong unresolved=0,nr=zst_secular_roots(roots,N,&unresolved,xi,N,p);
 flint_printf("secular_roots=%wd unresolved=%wd\n",nr,unresolved);
 must(nr==N && unresolved==0,"all N positive secular roots certified");
 zst_window_L(L,x,p);arb_const_pi(t,p);arb_mul_2exp_si(t,t,1);arb_div(t,t,L,p);arb_mul(z,roots,t,p);
 flint_printf("# COMPARISON STEP: zeros used only from here\n");
 zst_zeta_zeros(gamma,1,p);arb_sub(err,z,gamma,p);arb_abs(err,err);arb_div(ratio,err,eps,p);
 pr("first_zero_error",err);pr("first_zero_error_over_eps",ratio);
 _arb_vec_clear(xi,N+1);_arb_vec_clear(roots,N);
 arb_clear(t);arb_clear(sum);arb_clear(L);arb_clear(z);arb_clear(gamma);arb_clear(err);arb_clear(ratio);
}
static void selftest(void)
{
 arb_mat_t A;arb_mat_init(A,3,3);arb_ptr v=_arb_vec_init(3),vr=_arb_vec_init(3);
 arb_t e,er,t;arb_init(e);arb_init(er);arb_init(t);
 /* Eigenvalues 1,6,7; nontrivial 2-by-2 block. */
 arb_set_ui(arb_mat_entry(A,0,0),5);arb_set_ui(arb_mat_entry(A,0,1),2);arb_set_ui(arb_mat_entry(A,1,0),2);arb_set_ui(arb_mat_entry(A,1,1),2);arb_set_ui(arb_mat_entry(A,2,2),7);
 must(inertia(A,t,512)==0,"positive matrix inertia");
 arb_set_ui(t,2);must(inertia(A,t,512)==1,"one negative shifted eigenvalue");
 arb_set_ui(t,13);arb_mul_2exp_si(t,t,-1);must(inertia(A,t,512)==2,"two negative shifted eigenvalues");
 must(certified(e,v,A,512),"residual eigenpair");must(arb_contains_si(e,1),"exact eigenvalue contained");
 /* 1/sqrt(5), -2/sqrt(5), 0 up to overall sign. */
 arb_set_ui(t,5);arb_sqrt(t,t,512);arb_inv(t,t,512);
 if(arb_is_negative(v)) arb_neg(t,t);
 must(arb_overlaps(v,t),"first component");arb_mul_si(t,t,-2,512);must(arb_overlaps(v+1,t),"second component");must(arb_contains_zero(v+2),"third component");
 must(zst_eigmin(er,vr,A,100,512),"Rump reference");must(arb_overlaps(er,e),"Rump eigenvalue agreement");
 arb_zero(t);arb_zero(arb_mat_entry(A,2,2));must(inertia(A,t,512)==-1,"zero pivot rejected");
 flint_printf("SELFTEST PASS\n");arb_mat_clear(A);_arb_vec_clear(v,3);_arb_vec_clear(vr,3);arb_clear(e);arb_clear(er);arb_clear(t);
}
int main(int argc,char **argv)
{
 slong X=13,start=200,end=1000,p=1000,step=40;int endpoint=0,rump=0,threads=4;const char *vecpath=NULL;
 for(int i=1;i<argc;i++) {
  if(!strcmp(argv[i],"--selftest")) { selftest();return 0; }
  must(i+1<argc,"option argument");const char *key=argv[i++],*val=argv[i];
  if(!strcmp(key,"--x"))X=atol(val);else if(!strcmp(key,"--start"))start=atol(val);else if(!strcmp(key,"--end"))end=atol(val);
  else if(!strcmp(key,"--prec"))p=atol(val);else if(!strcmp(key,"--step"))step=atol(val);else if(!strcmp(key,"--endpoint"))endpoint=atoi(val);
  else if(!strcmp(key,"--rump"))rump=atoi(val);else if(!strcmp(key,"--threads"))threads=atoi(val);else if(!strcmp(key,"--vector"))vecpath=val;else must(0,"unknown option");
 }
 must(X>1&&start>0&&end>=start&&p>=256&&step>0&&threads>0,"parameters");omp_set_num_threads(threads);
 setvbuf(stdout,NULL,_IOLBF,0);double total=now();
 arb_t x,eps,prev,ratio,threshold,t,zero;arb_init(x);arb_init(eps);arb_init(prev);arb_init(ratio);arb_init(threshold);arb_init(t);arb_init(zero);
 arb_set_si(x,X);arb_set_ui(threshold,101);arb_div_ui(threshold,threshold,100,p);
 flint_printf("# RTP-2 scale author codex:gpt-6-astra FLINT %s\n# All numeric enclosures are arb balls; timings only on stderr.\n",FLINT_VERSION);
 flint_printf("x=%wd prec=%wd start=%wd end=%wd step=%wd\n",X,p,start,end,step);
 int haveprev=0,converged=0;
 for(slong N=start;N<=end;N+=step) {
  double row=now();arb_ptr a=_arb_vec_init(N+1),b=_arb_vec_init(N+1),v=_arb_vec_init(N+1);arb_mat_t E,O;arb_mat_init(E,N+1,N+1);arb_mat_init(O,N,N);
  zst_riemann_ab(a,b,N,x,X,p);zst_even_block(E,a,b,N,p);
  flint_printf("ROW N=%wd\n",N);fprintf(stderr,"build x=%ld N=%ld seconds=%.6f\n",X,N,now()-row);
  must(certified(eps,v,E,p),"minimal even eigenpair (raise precision on failure)");pr("eps",eps);
  if(haveprev) {
   arb_div(ratio,prev,eps,p);pr("previous_over_current",ratio);
   must(arb_ge(prev,eps)||arb_overlaps(prev,eps),"monotonicity");
   converged=arb_lt(ratio,threshold);
  }
  arb_set(prev,eps);haveprev=1;
  int final=endpoint||(converged&&step==40);
  if(final) {
   flint_printf("FINAL N=%wd N_conv=%wd converged=%d\n",N,converged?N-step:-1,converged);
   zst_odd_block(O,a,b,N,p);arb_get_mid_arb(t,eps);arb_mul_2exp_si(t,t,1);slong odd=inertia(O,t,p);
   flint_printf("odd_below_twice_eps=%wd\n",odd);must(odd==0,"even-simple odd gap");
   if(rump) {
    arb_t er;arb_init(er);arb_ptr vr=_arb_vec_init(N+1);double rt=now();
    must(zst_eigmin(er,vr,E,120,p),"Rump cross-check");must(arb_overlaps(er,eps),"Rump/residual overlap");
    pr("rump_eps",er);fprintf(stderr,"rump x=%ld N=%ld seconds=%.6f\n",X,N,now()-rt);arb_clear(er);_arb_vec_clear(vr,N+1);
   }
   if(vecpath) {
    FILE *fp=fopen(vecpath,"w");must(fp!=NULL,"vector file");fprintf(fp,"%ld %ld %ld\n",X,N,p);
    for(slong i=0;i<=N;i++) { arb_dump_file(fp,v+i);fputc('\n',fp); }fclose(fp);
   }
   comparison(v,N,x,eps,p);
   /* Prime-free control uses original zst builder with cutoff one. */
   zst_riemann_ab(a,b,N,x,1,512);zst_even_block(E,a,b,N,512);zst_odd_block(O,a,b,N,512);
   slong ne=inertia(E,zero,512),no=inertia(O,zero,512);
   flint_printf("prime_free_negative_even=%wd odd=%wd prec=512\n",ne,no);must(ne>=0&&no>=0,"control inertia");
  }
  fprintf(stderr,"row x=%ld N=%ld seconds=%.6f\n",X,N,now()-row);
  _arb_vec_clear(a,N+1);_arb_vec_clear(b,N+1);_arb_vec_clear(v,N+1);arb_mat_clear(E);arb_mat_clear(O);
  if(final)break;
 }
 fprintf(stderr,"total x=%ld seconds=%.6f\n",X,now()-total);
 arb_clear(x);arb_clear(eps);arb_clear(prev);arb_clear(ratio);arb_clear(threshold);arb_clear(t);arb_clear(zero);flint_cleanup();return 0;
}
