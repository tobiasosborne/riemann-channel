#!/usr/bin/env python3
"""One-time adaptation of lane D; retained as an audit of the initial port."""
from pathlib import Path
import hashlib
root=Path(__file__).resolve().parents[4]
s=(root/'zst/tools/rtp2_dirichlet.c').read_text()
(root/'notes/rtp-round-2/ellcurve/checks/driver-source.sha256').write_text(hashlib.sha256(s.encode()).hexdigest()+'  zst/tools/rtp2_dirichlet.c (port snapshot)\n')
s=s.replace('RTP-2 lane D','RTP-2 lane E').replace('See lane report D3.','See lane report E3.').replace('#include "../../notes/rtp-round-2/dirichlet/checks/reference.c"\nstatic slong discriminant = -4;', '''static const char *curve = "11a1";
static const char *reference_path = "zst/tests/data/ell_ref.txt";
static fmpz *ainvs;
static fmpz_t conductor;
static slong curve_rank;
static int root_number;

/* K=0 reads only arithmetic metadata. Zero ordinates are read later, in COMPARISON. */
static int reference_zero(arb_t gamma, slong prec)
{
    fmpz *ai=_fmpz_vec_init(5);fmpz_t C;fmpz_init(C);int w;slong rank;
    int ok=zst_ell_ref(ai,C,&w,&rank,gamma,1,curve,reference_path,prec);
    _fmpz_vec_clear(ai,5);fmpz_clear(C);
    return ok&&arb_is_finite(gamma);
}''')
s=s.replace('''    arb_log_ui(w, p, prec); arb_sqrt_ui(t, k, prec); arb_div(w, w, t, prec);
    fmpz_t dd,kk; fmpz_init(dd);fmpz_init(kk);fmpz_set_si(dd,discriminant);fmpz_set_ui(kk,k);
    arb_mul_si(w,w,fmpz_kronecker(dd,kk),prec);fmpz_clear(dd);fmpz_clear(kk);''','''    /* F4/F5: arithmetic t_m / p^m, NOT t_m / sqrt(p^m).
     * Independent local recurrence, checked against zst_weil_ellcurve below. */
    slong ap=zst_ell_ap(ainvs,p), t0=2, t1=ap, raw=ap;
    for(ulong pm=p;pm<k;pm*=p) {
        if(fmpz_fdiv_ui(conductor,p)) {slong tn=ap*t1-(slong)p*t0;t0=t1;t1=tn;raw=tn;}
        else raw*=ap;
    }
    arb_log_ui(w,p,prec);arb_mul_si(w,w,raw,prec);arb_div_ui(w,w,k,prec);''')
s=s.replace('dir_ab','ell_ab')
s=s.replace('''    zst_weil_t W;fmpz_t D;fmpz_init(D);fmpz_set_si(D,discriminant);
    zst_weil_dirichlet(&W,D,x,X,prec);zst_weil_ab(a,b,N,&W,prec);
    zst_weil_clear(&W);fmpz_clear(D);''','''    zst_weil_t W;
    zst_weil_ellcurve(&W,ainvs,conductor,x,X,prec);zst_weil_ab(a,b,N,&W,prec);
    zst_weil_clear(&W);''')
s=s.replace('character-weighted','elliptic local').replace('gamma + log(q) I','gamma + log(C) I').replace('zero character weights','zero elliptic weights')
s=s.replace('D=%wd kappa=%d','curve=%s C=%wd').replace('discriminant,discriminant<0','curve,fmpz_get_si(conductor)')
s=s.replace('D=%ld','curve=%s').replace('(long)discriminant','curve')
s=s.replace('''arb_init(gamma);check(reference_zero(gamma,discriminant,cprec),"Hardy Z interval Newton reference zero");
    flint_printf("REFERENCE D=%wd gamma1=%s certified_unique=1 index=PARI_or_sign_scan\\n",discriminant,sb(gamma,30));''','''arb_init(gamma);
    if(curve_rank==0)check(reference_zero(gamma,cprec),"PARI reference read in comparison only");
    flint_printf("REFERENCE curve=%s gamma1=%s certified_unique=0 index=PARI radius=1e-38 rank=%wd\\n",curve,sb(gamma,30),curve_rank);''')
s=s.replace('''arb_init(gamma);check(reference_zero(gamma,discriminant,prec),"Hardy Z interval Newton reference zero");
    flint_printf("REFERENCE D=%wd gamma1=%s certified_unique=1 index=PARI_or_sign_scan\\n",discriminant,sb(gamma,30));''','''arb_init(gamma);
    if(curve_rank==0)check(reference_zero(gamma,prec),"PARI reference read in comparison only");
    flint_printf("REFERENCE curve=%s gamma1=%s certified_unique=0 index=PARI radius=1e-38 rank=%wd\\n",curve,sb(gamma,30),curve_rank);''')
s=s.replace('''if(p->ok&&p->par>0)nr=first_root''','''if(curve_rank>0) {
        flint_printf("COMP x=%g X=%wu N=%wd parity=%d roots=0 status=RANK_POSITIVE_NO_COMPARISON\\n",xd,X,p->N,p->par);
        arb_clear(z);arb_clear(err);arb_clear(ratio);return;
    }
    if(p->ok&&p->par>0)nr=first_root''')
s=s.replace('''if(!strcmp(argv[i],"--D"))discriminant=atol(argv[i+1]);''','''if(!strcmp(argv[i],"--curve"))curve=argv[i+1];
        else if(!strcmp(argv[i],"--ref"))reference_path=argv[i+1];''')
a=s.index('    slong d=discriminant, r=');b=s.index('    if(!strcmp(mode,"axisN"))',a)
s=s[:a]+'''    if(xd<=1||xd>250||xmax<=1||xmax>250||N<1||Nmax<3||prec<128||cprec<128)return 2;
    ainvs=_fmpz_vec_init(5);fmpz_init(conductor);
    if(!zst_ell_ref(ainvs,conductor,&root_number,&curve_rank,NULL,0,curve,reference_path,prec)) {
        fprintf(stderr,"curve metadata absent: %s\\n",curve);return 2;
    }
    flint_printf("# rtp2_ellcurve; author codex:gpt-6-astra; FLINT %s; certified forms/eigenpairs; PARI comparisons approximate\\n",FLINT_VERSION);
    flint_printf("# curve=%s C=%wd rank=%wd root_number=%d; gamma (Q,d,mu)=(1/(2pi),1,1); no poles\\n",curve,fmpz_get_si(conductor),curve_rank,root_number);
'''+s[b:]
s=s.replace('flint_cleanup();return n_fail?1:0;','_fmpz_vec_clear(ainvs,5);fmpz_clear(conductor);flint_cleanup();return n_fail?1:0;')
assert 'discriminant' not in s
assert 'dirichlet' not in s
(root/'zst/tools/rtp2_ellcurve.c').write_text(s)
