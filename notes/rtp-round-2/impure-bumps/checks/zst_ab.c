#include <stdio.h>
#include "zst.h"
int main(void){arb_t x; arb_init(x);arb_set_ui(x,9);
 arb_ptr a=_arb_vec_init(9),b=_arb_vec_init(9);
 zst_riemann_ab(a,b,8,x,9,240);
 for(int n=0;n<9;n++){printf("%d ",n);arb_printn(a+n,35,ARB_STR_NO_RADIUS);printf(" ");arb_printn(b+n,35,ARB_STR_NO_RADIUS);printf("\n");}
 _arb_vec_clear(a,9);_arb_vec_clear(b,9);arb_clear(x);return 0;}
