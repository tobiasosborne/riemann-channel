/* Author codex:gpt-6-astra. plan.md 1.1: after unitary rescaling
 * U_n^L -> exp(2 pi i n t), the even coefficient vectors use a common
 * orthonormal basis. Zero-pad the shorter vector and take |dot|. */
#include <stdio.h>
#include <stdlib.h>
#include <flint/arb.h>
int main(int argc,char **argv) {
 if(argc<3)return 1;
 arb_ptr prev=NULL;slong oldN=0,oldX=0;
 for(int k=1;k<argc;k++) {
  FILE *f=fopen(argv[k],"r");if(!f)return 2;long x,n,p;
  if(fscanf(f,"%ld %ld %ld",&x,&n,&p)!=3)return 3;
  arb_ptr v=_arb_vec_init(n+1);
  for(slong j=0;j<=n;j++)if(arb_load_file(v+j,f))return 4;
  fclose(f);
  if(prev) {
   arb_t d;arb_init(d);arb_dot(d,NULL,0,v,1,prev,1,FLINT_MIN(n,oldN)+1,512);arb_abs(d,d);
   flint_printf("overlap x=%wd -> %wd N=%wd -> %wd: ",oldX,(slong)x,oldN,(slong)n);arb_printn(d,16,0);flint_printf("\n");
   arb_clear(d);_arb_vec_clear(prev,oldN+1);
  }
  prev=v;oldN=n;oldX=x;
 }
 _arb_vec_clear(prev,oldN+1);flint_cleanup();return 0;
}
