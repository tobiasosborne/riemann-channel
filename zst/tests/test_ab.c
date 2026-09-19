/* a_n, b_n at x = 9 (lambda = 3) against 50-digit mpmath reference values.
 * Ground truth: notes/zeta-spectral-triples/reference_ab_lambda3.txt, produced by build_ab() of
 * notes/zeta-spectral-triples/ccm_proto.py, whose closed forms were checked against direct
 * quadrature of the defining integrals (paper eqs. (weinfty), (bomp), (hh):
 * refs/src/2511.22755/mc2arXiv.tex lines 709, 693, 685) and which reproduces the paper's
 * lambda = sqrt 13 table (Section 6 of the paper) for all 50 zeros. */
#include <stdio.h>
#include "zst.h"

static const char *ref_a[9] = {
"0.040855198682716658866962016525192057993967970092316",
"0.04169817273369816922174896107257050399588420274449",
"0.044529765174597757601967690281275540262311080543885",
"0.050686053878670647398936158222939527826208581175347",
"0.066869791189334429856877736500723555720744932222661",
"2.2555878570606906189745010189114076480768907141192",
"0.16631247943612040207414222368104791442274218283418",
"1.535304896409860553990104245838825678703103526113",
"0.70835165341671347343683892146617771592418674160556"};
static const char *ref_b[9] = {
"0",
"0.04113320482935408156568436214592192754642607646535",
"0.084049825654443533499291065014702333686190430336304",
"0.13126799257598811545417556867287405121104313127281",
"0.18839323849514140042820252100790850902712730678215",
"0.1253579050710410397357557827272638223807611203126",
"0.35407118228242921278171280692700499049915075741344",
"0.80745213051164313335477050531164769683528894148956",
"0.18535018718030982485534420972239827258239335000968"};

int main(void)
{
    slong prec = 300, n, fails = 0;
    arb_t x, r, tol;
    arb_ptr a = _arb_vec_init(9), b = _arb_vec_init(9);
    arb_init(x); arb_init(r); arb_init(tol);
    arb_set_ui(x, 9);
    arb_set_str(tol, "1e-45", prec);
    zst_riemann_ab(a, b, 8, x, 9, prec);
    for (n = 0; n <= 8; n++)
    {
        arb_set_str(r, ref_a[n], prec);
        arb_sub(r, r, a + n, prec); arb_abs(r, r);
        if (!arb_lt(r, tol)) { flint_printf("a_%wd mismatch: ", n); arb_printn(a + n, 30, 0); flint_printf("\n"); fails++; }
        arb_set_str(r, ref_b[n], prec);
        arb_sub(r, r, b + n, prec); arb_abs(r, r);
        if (!arb_lt(r, tol)) { flint_printf("b_%wd mismatch: ", n); arb_printn(b + n, 30, 0); flint_printf("\n"); fails++; }
        if (mag_cmp_2exp_si(arb_radref(a + n), -200) > 0 || mag_cmp_2exp_si(arb_radref(b + n), -200) > 0)
        { flint_printf("radius too large at n = %wd\n", n); fails++; }
    }
    _arb_vec_clear(a, 9); _arb_vec_clear(b, 9);
    arb_clear(x); arb_clear(r); arb_clear(tol);
    flint_cleanup();
    flint_printf("test_ab: %s\n", fails ? "FAIL" : "PASS");
    return fails ? 1 : 0;
}
