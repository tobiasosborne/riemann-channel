#include <stdio.h>
#include <flint/flint.h>
#include <flint/arb.h>
#include <flint/acb.h>
#include <flint/acb_dirichlet.h>
#include <flint/acb_mat.h>
#include <flint/arb_mat.h>
#include <flint/acb_hypgeom.h>
int main(void) {
    slong prec = 400;
    acb_t z, r; acb_init(z); acb_init(r);
    acb_set_d_d(z, 0.25, -1.0);          /* A = 1/4 - i pi n / L with a placeholder imaginary part */
    acb_digamma(r, z, prec); printf("digamma(1/4 - i) = "); acb_printn(r, 30, 0); printf("\n");
    acb_polygamma(r, z, z, prec);        /* placeholder call shape check */
    acb_t one; acb_init(one); acb_one(one);
    acb_polygamma(r, one, z, prec); printf("trigamma(1/4 - i) = "); acb_printn(r, 30, 0); printf("\n");
    /* first zeta zero */
    acb_t rho; acb_init(rho); fmpz_t n; fmpz_init(n); fmpz_set_ui(n, 1);
    acb_dirichlet_zeta_zero(rho, n, prec); printf("rho_1 = "); acb_printn(rho, 40, 0); printf("\n");
    /* Xi at s=1/2+14.1347i */
    acb_dirichlet_xi(r, rho, prec); printf("xi(rho_1) = "); acb_printn(r, 10, 0); printf("\n");
    /* eigen-enclosure API presence */
    acb_mat_t A, X, J; acb_mat_init(A, 2, 2); acb_mat_init(X, 2, 1); acb_mat_init(J, 1, 1);
    acb_mat_one(A); acb_set_d(acb_mat_entry(A, 1, 1), 3.0);
    acb_t lam, lam_approx; acb_init(lam); acb_init(lam_approx); acb_set_d(lam_approx, 3.0);
    acb_zero(acb_mat_entry(X, 0, 0)); acb_one(acb_mat_entry(X, 1, 0));
    acb_mat_eig_enclosure_rump(lam, J, X, A, lam_approx, X, prec);
    printf("rump enclosure of eigenvalue 3: "); acb_printn(lam, 20, 0); printf("\n");
    printf("flint version %s\n", flint_version);
    return 0;
}
