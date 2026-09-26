from pathlib import Path
src=Path('zst/tools/rtp1_a1.c').read_text()
# Preserve A1's actual bordering and certification arithmetic, not a second implementation.
head=src[src.index('#include <stdio.h>'):src.index('static void print_ab_reference')]
head=head.replace('#include "zst.h"','#include "zst.h"\n#include "../../notes/rtp-round-2/dirichlet/checks/reference.c"\nstatic slong discriminant = -4;')
prime=src[src.index('static void prime_term_ab'):src.index('static void rayleigh(')]
prime=prime.replace('arb_div(w, w, t, prec);','arb_div(w, w, t, prec);\n    fmpz_t dd,kk; fmpz_init(dd);fmpz_init(kk);fmpz_set_si(dd,discriminant);fmpz_set_ui(kk,k);\n    arb_mul_si(w,w,fmpz_kronecker(dd,kk),prec);fmpz_clear(dd);fmpz_clear(kk);')
Path('zst/tools/rtp2_dirichlet.c').write_text('''#define _POSIX_C_SOURCE 200809L
/* RTP-2 lane D, author codex:gpt-6-astra. Adapted from rtp1_a1.c (claude:opus).
 * Unchanged libzst. A1.1' bordering helpers retained verbatim. See lane report D3.
 * All reference-zero operations occur after the independent eigenpair/form computations.
 * Output tags ROW, SAT, EIG, CONTROL, COMP, RAY are consumed by checks/summary.py.
 */
'''+head+prime)
