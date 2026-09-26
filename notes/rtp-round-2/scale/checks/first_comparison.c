/* Standalone completion from a certified vector dump, with no repeated eigenproblem.
 * Driver definitions are shared, never copied into zst/src/. */
#define main scale_unused_main
#include "../../../../zst/tools/rtp2_scale.c"
#undef main
#include "first_root.h"
int main(int argc,char **argv)
{
 if(argc!=3)return 1;double tm=now();omp_set_num_threads(4);
 FILE *f=fopen(argv[1],"r");must(f!=NULL,"vector input");long X,N,p;
 must(fscanf(f,"%ld %ld %ld",&X,&N,&p)==3,"vector header");arb_ptr v=_arb_vec_init(N+1),xi=_arb_vec_init(N+1);
 for(slong i=0;i<=N;i++)must(arb_load_file(v+i,f)==0,"vector load");fclose(f);
 arb_t x,eps,L,root,t,z,g,err,ratio,zero;arb_init(x);arb_init(eps);arb_init(L);arb_init(root);arb_init(t);arb_init(z);arb_init(g);arb_init(err);arb_init(ratio);arb_init(zero);
 f=fopen(argv[2],"r");must(f!=NULL,"eigenvalue output input");char line[4096];int have=0,even_simple=0;long lastN=-1,finalN=-1,fileX=-1;
 while(fgets(line,sizeof(line),f)) {
  if(!strncmp(line,"eps=",4)){must(arb_set_str(eps,line+4,p)==0,"eigenvalue enclosure parse");have=1;}
  if(!strncmp(line,"x=",2))sscanf(line,"x=%ld",&fileX);
  if(!strncmp(line,"ROW N=",6))sscanf(line,"ROW N=%ld",&lastN);
  if(!strncmp(line,"FINAL N=",8))sscanf(line,"FINAL N=%ld",&finalN);
  if(!strcmp(line,"odd_below_twice_eps=0\n"))even_simple=1;
 }
 fclose(f);must(have&&fileX==X&&lastN==N&&finalN==N&&even_simple,"matching certified even-simple endpoint");
 arb_set_si(x,X);arb_log(L,x,p);arb_sqrt_ui(t,2,p);arb_set(xi,v);
 for(slong i=1;i<=N;i++)arb_div(xi+i,v+i,t,p);
 flint_printf("# RTP-2 scale first-root completion author codex:gpt-6-astra\nx=%wd N=%wd prec=%wd\n",(slong)X,(slong)N,(slong)p);
 pr("eps_input",eps);scale_first_root(root,xi,N,p);
 arb_const_pi(t,p);arb_mul_2exp_si(t,t,1);arb_mul(z,root,t,p);arb_div(z,z,L,p);
 flint_printf("# COMPARISON STEP: zeros used only from here\n");zst_zeta_zeros(g,1,p);arb_sub(err,z,g,p);arb_abs(err,err);arb_div(ratio,err,eps,p);pr("first_zero_error",err);pr("first_zero_error_over_eps",ratio);
 arb_ptr a=_arb_vec_init(N+1),b=_arb_vec_init(N+1);arb_mat_t E,O;arb_mat_init(E,N+1,N+1);arb_mat_init(O,N,N);
 zst_riemann_ab(a,b,N,x,1,512);zst_even_block(E,a,b,N,512);zst_odd_block(O,a,b,N,512);
 slong ne=inertia(E,zero,512),no=inertia(O,zero,512);must(ne>=0&&no>=0,"control inertia");flint_printf("prime_free_negative_even=%wd odd=%wd prec=512\n",ne,no);
 fprintf(stderr,"first_comparison x=%ld N=%ld seconds=%.6f\n",X,N,now()-tm);
 arb_mat_clear(E);arb_mat_clear(O);_arb_vec_clear(a,N+1);_arb_vec_clear(b,N+1);_arb_vec_clear(v,N+1);_arb_vec_clear(xi,N+1);
 arb_clear(x);arb_clear(eps);arb_clear(L);arb_clear(root);arb_clear(t);arb_clear(z);arb_clear(g);arb_clear(err);arb_clear(ratio);arb_clear(zero);flint_cleanup();return 0;
}
