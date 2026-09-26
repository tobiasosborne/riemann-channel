/* Author codex:gpt-6-astra. First positive secular root only: prime-side
 * sign candidates, libzst interval Newton, and certified exclusion below it.
 * h_j(s)=g(s)(j-s)(j+1-s), evaluated by zst_secular_eval, has exactly
 * the same roots away from poles. Nonzero xi_j exclude roots at poles. */
static long exclusion_cells;
static int exclude_interval(arb_srcptr xi,slong N,slong j,const arb_t lo,const arb_t hi,slong p,int depth)
{
 arb_t H,h,d,m;arb_init(H);arb_init(h);arb_init(d);arb_init(m);
 arb_union(H,lo,hi,p);zst_secular_eval(h,d,H,xi,N,j,p);exclusion_cells++;
 int ok=!arb_contains_zero(h);
 if(!ok&&depth<32) {
  arb_add(m,lo,hi,p);arb_mul_2exp_si(m,m,-1);arb_get_mid_arb(m,m);
  ok=exclude_interval(xi,N,j,lo,m,p,depth+1)&&exclude_interval(xi,N,j,m,hi,p,depth+1);
 }
 arb_clear(H);arb_clear(h);arb_clear(d);arb_clear(m);return ok;
}
static void scale_first_root(arb_t root,arb_srcptr xi,slong N,slong p)
{
 arb_t a,b,h,d,old,m,basin,lo,hi;arb_init(a);arb_init(b);arb_init(h);arb_init(d);arb_init(old);arb_init(m);arb_init(basin);arb_init(lo);arb_init(hi);
 int found=0;slong jj=-1;
 /* This search uses only the certified eigenvector. It never queries zeta. */
 for(slong j=0;j<N&&!found;j++) {
  arb_set_si(a,j);zst_secular_eval(old,d,a,xi,N,j,p);
  must(!arb_contains_zero(xi+j),"nonzero coefficient at preceding pole");
  for(slong k=1;k<=32;k++) {
   arb_set_si(b,32*j+k);arb_mul_2exp_si(b,b,-5);zst_secular_eval(h,d,b,xi,N,j,p);
   if((arb_is_positive(old)&&arb_is_negative(h))||(arb_is_negative(old)&&arb_is_positive(h))) {found=1;jj=j;break;}
   arb_set(a,b);arb_set(old,h);
  }
 }
 must(found,"prime-side first-root candidate");
 /* Midpoint bisection locates the candidate; no sign decision here certifies it. */
 for(int k=0;k<48;k++) {
  arb_add(m,a,b,p);arb_mul_2exp_si(m,m,-1);zst_secular_eval(h,d,m,xi,N,jj,p);
  if((arb_is_positive(old)&&arb_is_positive(h))||(arb_is_negative(old)&&arb_is_negative(h)))arb_set(a,m);else arb_set(b,m);
 }
 arb_add(m,a,b,p);arb_mul_2exp_si(m,m,-1);
 for(int k=0;k<16;k++) {
  zst_secular_eval(h,d,m,xi,N,jj,p);arb_get_mid_arb(h,h);arb_get_mid_arb(d,d);
  must(!arb_is_zero(d),"Newton derivative nonzero");arb_div(h,h,d,p);arb_sub(m,m,h,p);arb_get_mid_arb(m,m);
 }
 must(zst_secular_verify(root,xi,N,m,p),"libzst first-root interval Newton");
 /* A wider basin around the verified root has a derivative of fixed sign. */
 int unique=0;
 for(int e=-6;e>=-32&&!unique;e--) {
  arb_set(basin,m);arb_add_error_2exp_si(basin,e);
  arb_get_lbound_arf(arb_midref(lo),basin,p);mag_zero(arb_radref(lo));
  arb_get_ubound_arf(arb_midref(hi),basin,p);mag_zero(arb_radref(hi));
  arb_set_si(a,jj);arb_set_si(b,jj+1);
  if(!arb_gt(lo,a)||!arb_lt(hi,b))continue;
  zst_secular_eval(h,d,basin,xi,N,jj,p);unique=!arb_contains_zero(d)&&arb_contains(basin,root);
 }
 must(unique,"unique root in basin");exclusion_cells=0;
 for(slong j=0;j<=jj;j++) {
  arb_set_si(a,j);if(j==jj)arb_set(b,lo);else arb_set_si(b,j+1);
  must(!arb_contains_zero(xi+j),"no polynomial root at a lower pole");
  must(exclude_interval(xi,N,j,a,b,p,0),"root-free range below basin");
 }
 flint_printf("secular_first_root_certified=1 lower_range_excluded=1 cells=%wd\n",(slong)exclusion_cells);
 arb_clear(a);arb_clear(b);arb_clear(h);arb_clear(d);arb_clear(old);arb_clear(m);arb_clear(basin);arb_clear(lo);arb_clear(hi);
}
