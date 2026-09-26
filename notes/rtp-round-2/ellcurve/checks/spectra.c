/* Author codex:gpt-6-astra. Certified complete spectra of controls, no zeros.
 * QR provides candidates only. Exact lower/upper inertia counts certify each
 * ordered eigenvalue in its printed interval. */
static void spectrum_block(const arb_mat_t B,const char *name,char parity,slong prec)
{
    slong n=arb_mat_nrows(B);acb_mat_t A;acb_ptr ev=_acb_vec_init(n);
    arb_ptr seeds=_arb_vec_init(n);mag_t tol;arb_t lo,hi,rad,t;arf_t al,ah;
    acb_mat_init(A,n,n);mag_init(tol);arb_init(lo);arb_init(hi);arb_init(rad);arb_init(t);arf_init(al);arf_init(ah);
    for(slong i=0;i<n;i++)for(slong j=0;j<n;j++)arb_get_mid_arb(acb_realref(acb_mat_entry(A,i,j)),arb_mat_entry(B,i,j));
    mag_set_ui_2exp_si(tol,1,-150);
    check(acb_mat_approx_eig_qr(ev,NULL,NULL,A,tol,0,192),"control spectrum QR candidates converge");
    for(slong i=0;i<n;i++)arb_get_mid_arb(seeds+i,acb_realref(ev+i));
    for(slong i=1;i<n;i++)for(slong j=i;j>0&&arf_cmp(arb_midref(seeds+j),arb_midref(seeds+j-1))<0;j--)arb_swap(seeds+j,seeds+j-1);
    for(slong i=0;i<n;i++) {
        arb_one(rad);arb_mul_2exp_si(rad,rad,-38);int ok=0;slong il=-1,iu=-1;
        for(slong k=0;k<8&&!ok;k++) {
            arb_sub(lo,seeds+i,rad,prec);arb_get_mid_arb(lo,lo);
            arb_add(hi,seeds+i,rad,prec);arb_get_mid_arb(hi,hi);
            il=zst_inertia_neg(B,lo,prec);iu=zst_inertia_neg(B,hi,prec);
            ok=il==i&&iu==i+1;if(!ok)arb_mul_2exp_si(rad,rad,2);
        }
        check(ok,"individual ordered control eigenvalue isolated by inertia");
        arf_set(al,arb_midref(lo));arf_set(ah,arb_midref(hi));arb_set_interval_arf(t,al,ah,prec);
        flint_printf("SPECTRUM object=%s block=%c index=%wd eigenvalue=%s lower_count=%wd upper_count=%wd certified=%d\n",name,parity,i+1,sb(t,14),il,iu,ok);
    }
    acb_mat_clear(A);_acb_vec_clear(ev,n);_arb_vec_clear(seeds,n);mag_clear(tol);arb_clear(lo);arb_clear(hi);arb_clear(rad);arb_clear(t);arf_clear(al);arf_clear(ah);
}
static void mode_spectra(double xd,slong N)
{
    const slong prec=384;arb_t x;arb_init(x);arb_set_d(x,xd);
    arb_ptr a=_arb_vec_init(N+1),b=_arb_vec_init(N+1);arb_mat_t E,O;
    arb_mat_init(E,N+1,N+1);arb_mat_init(O,N,N);
    for(int family=0;family<4;family++) {
        zst_weil_t W;fmpz_t D;fmpz_init(D);const char *label;
        if(family==0){label=curve;zst_weil_ellcurve(&W,ainvs,conductor,x,1,prec);}
        else if(family==1){label="chi_-4";fmpz_set_si(D,-4);zst_weil_dirichlet(&W,D,x,1,prec);}
        else {
            label=family==2?"zeta_gamma":"zeta_gamma_poles";zst_weil_riemann(&W,x,1,prec);
            if(family==2)for(slong k=0;k<W.npoles;k++)W.pmult[k]=0;
        }
        zst_weil_ab(a,b,N,&W,prec);zst_even_block(E,a,b,N,prec);zst_odd_block(O,a,b,N,prec);
        flint_printf("# CONTROL_SPECTRUM object=%s x=%g N=%wd prec=%wd; gamma includes conductor shift; no atoms\n",label,xd,N,prec);
        spectrum_block(E,label,'E',prec);spectrum_block(O,label,'O',prec);
        zst_weil_clear(&W);fmpz_clear(D);
    }
    arb_clear(x);_arb_vec_clear(a,N+1);_arb_vec_clear(b,N+1);arb_mat_clear(E);arb_mat_clear(O);
}
