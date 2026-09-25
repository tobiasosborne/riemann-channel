# Numerics lane, connes-weighted-metric (PARTIAL)

Author: claude:fable-5.1 (fork). Written without reading the prover's `checks/`.
The lane was terminated by the Claude spend limit on 2026-09-22; `scripts/connes_weighted_metric.py` passes D01–D34
and then crashes at line 264 (parsing a complex string with `mp.mpc`, a bug in the script, not a failed check).
Output: `outputs/connes_weighted_metric.txt`.

| ID | Result |
|---|---|
| D01–D07 | PASS: Theta'(w_j) formula, Theta(w_j) = 0, |Theta| = 1 on R, ||k||^2 = 2, ||b_j|| = sqrt2/|Theta'(w_j)| (ten zeros) |
| D08–D17 | PASS: truncated Blaschke products for ||b_j|| (monotone in the cutoff, tail 2.4e-4 at 3000), finite-family biorthogonal norms increase to the global value, nearest-gap lower bound |
| D18–D27 | PASS: F_{delta,c} closed forms and Tricomi series against quadrature; the tail |F| ~ 1/|tau| (1/gap, not 1/gap^{1+delta}) |
| D28–D34 | PASS: weighted Gram extremes on 10 modes for (delta, c) in {(0,1),(1,1),(2,1),(1,2),(2,2)} |

Not done (pending): N = 20, 40 growth of the weighted Gram extremes, the all-ones vs I/2 losses, the cut-and-damp checks.
Fix line 264 (`mp.mpc(complex(t12))`) and rerun.
