# Numerics lane, cerednik-drinfeld (PARTIAL)

Author: claude:fable-5.1 (fork). Written without reading the prover's `checks/`.
The lane was terminated by the Claude spend limit on 2026-09-22 before completing; `scripts/cerednik_drinfeld.py`
ran to D13 and stops there. Output: `outputs/cerednik_drinfeld.txt`.

| ID | Result |
|---|---|
| D01–D05 | PASS: sizes, identity vertex index 20, bipartite sign, 252 rules, T_1 symmetric with T_1 D = D A_17, BFS tree 119/721 |
| D06–D09 | PASS: integral cycle basis Z (D^t Z = 0, chord rows = I), M = I + Z_tree^t Z_tree >= I, M positive |
| D10–D13 | PASS: det M = tau(Y) exactly (Sylvester + reduced Laplacian), = spectral formula, = 2^217 3^92 5^33 7; spectrum certificate |

Not done (pending): Smith normal form of M, L^t M = M L exactly, the T_17 - 18 action on the component group
(astra's x_0 = -364/135), positivity of G_M, the reversal/bipartition identity.
