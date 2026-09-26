/* Author codex:gpt-6-astra. COMPARISON ONLY. FLINT Hardy Z reference refinement.
 * The real character is identified by its complete residue table, not a guessed index.
 * Existing PARI values supply guesses only; interval Newton certifies a unique zero.
 * Missing discriminants are scanned in steps 1/16 at 128 bits before refinement. */
#include <flint/acb_dirichlet.h>
#include <flint/dirichlet.h>
static int ref_character(dirichlet_group_t G, dirichlet_char_t chi, slong D)
{
    ulong q=labs(D),j,n;
    fmpz_t d,m; fmpz_init(d); fmpz_init(m); fmpz_set_si(d,D);
    dirichlet_group_init(G,q); dirichlet_char_init(chi,G);
    for(j=0;j<dirichlet_group_size(G);j++) {
        int ok=1;
        dirichlet_char_index(chi,G,j);
        for(n=1;n<q;n++) {
            ulong e=dirichlet_chi(G,chi,n); int c;
            fmpz_set_ui(m,n); c=fmpz_kronecker(d,m);
            if ((c==0 && e!=DIRICHLET_CHI_NULL) || (c==1 && e!=0) ||
                (c==-1 && (e==DIRICHLET_CHI_NULL || 2*e!=G->expo))) {ok=0;break;}
        }
        if(ok) {fmpz_clear(d);fmpz_clear(m);return 1;}
    }
    fmpz_clear(d);fmpz_clear(m);return 0;
}
static int ref_guess(arb_t t, slong D, slong prec)
{
    const char *paths[]={"zst/tests/data/dirichlet_ref.txt","tests/data/dirichlet_ref.txt",
      "../tests/data/dirichlet_ref.txt"};
    FILE *f=NULL; char line[512],val[256]; long d,q,k,j; int found=0;
    for(int i=0;i<3&&!f;i++)f=fopen(paths[i],"r");
    if(!f)return 0;
    while(fgets(line,sizeof line,f)) {
        if(sscanf(line,"chi %ld %ld %ld",&d,&q,&k)==3)found=d==D;
        if(found && sscanf(line,"zero %ld %255s",&j,val)==2 && j==1) {
            arb_set_str(t,val,prec);arb_get_mid_arb(t,t);fclose(f);return 1;
        }
    }
    fclose(f);return 0;
}
static int reference_zero(arb_t root, slong D, slong prec)
{
    dirichlet_group_t G; dirichlet_char_t chi;
    acb_t z; acb_ptr zz=_acb_vec_init(2);
    arb_t m,box,nx,t; int ok=0; slong i;
    acb_init(z);arb_init(m);arb_init(box);arb_init(nx);arb_init(t);
    if(!ref_character(G,chi,D))goto done;
    if(!ref_guess(m,D,prec)) {
        int last=0;
        for(i=0;i<1600;i++) {
            arb_set_ui(m,i);arb_mul_2exp_si(m,m,-4);acb_set_arb(z,m);
            acb_dirichlet_hardy_z(zz,z,G,chi,1,128);
            int sg=arb_is_positive(acb_realref(zz))?1:arb_is_negative(acb_realref(zz))?-1:0;
            if(sg && last && sg!=last)break;
            if(sg)last=sg;
        }
        if(i==1600)goto clear_group;
    }
    /* Floating point Newton produces a guess; never accepted without interval inclusion. */
    for(i=0;i<16;i++) {
        acb_set_arb(z,m);acb_dirichlet_hardy_z(zz,z,G,chi,2,prec);
        arb_div(t,acb_realref(zz),acb_realref(zz+1),prec);
        arb_sub(m,m,t,prec);arb_get_mid_arb(m,m);
    }
    arb_set(box,m);arb_add_error_2exp_si(box,-prec/2);
    for(i=0;i<8;i++) {
        acb_set_arb(z,box);acb_dirichlet_hardy_z(zz,z,G,chi,2,prec);
        arb_set(t,acb_realref(zz+1));
        if(arb_contains_zero(t))break;
        acb_set_arb(z,m);acb_dirichlet_hardy_z(zz,z,G,chi,1,prec);
        arb_div(nx,acb_realref(zz),t,prec);arb_sub(nx,m,nx,prec);
        if(!arb_contains_interior(box,nx)) {if(!ok)break; else break;}
        ok=1;arb_set(box,nx);arb_get_mid_arb(m,box);
    }
    if(ok)arb_set(root,box);
clear_group:
    dirichlet_char_clear(chi);dirichlet_group_clear(G);
done:
    if(!ok)arb_indeterminate(root);
    acb_clear(z);_acb_vec_clear(zz,2);arb_clear(m);arb_clear(box);arb_clear(nx);arb_clear(t);
    return ok;
}
#ifdef REF_MAIN
int main(int argc,char **argv) {
    slong D=argc>1?atol(argv[1]):-7, prec=argc>2?atol(argv[2]):800;
    arb_t r;arb_init(r);int ok=reference_zero(r,D,prec);
    flint_printf("# COMPARISON ONLY; unique Hardy Z zero certified=%d; first index from PARI or floating sign scan\n",ok);
    flint_printf("chi %wd %wd %d\nzero 1 ",D,labs(D),D<0);
    arb_printn(r,prec/4,0);flint_printf("\nend\n");arb_clear(r);flint_cleanup();return !ok;
}
#endif
