/* Reference zeros: acb_dirichlet_zeta_zeros (FLINT/arb, certified enclosures of rho_k = 1/2 + i gamma_k).
 * The paper's table (Section 6, refs/src/2511.22755/mc2arXiv.tex l.1140-1220) compares the
 * eigenvalues of D_log^{(lambda,N)} with these gamma_k. */
#include <flint/acb_dirichlet.h>
#include "zst.h"

void zst_zeta_zeros(arb_ptr gamma, slong K, slong prec)
{
    acb_ptr rho = _acb_vec_init(K);
    fmpz_t one;
    slong k;
    fmpz_init(one); fmpz_one(one);
    acb_dirichlet_zeta_zeros(rho, one, K, prec);
    for (k = 0; k < K; k++) arb_set(gamma + k, acb_imagref(rho + k));
    _acb_vec_clear(rho, K);
    fmpz_clear(one);
}
