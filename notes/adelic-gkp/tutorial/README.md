# Tutorial: the super Ihara zeta and its two lattice states, from the ground up

Author: `claude:fable-5.1`, 2026-10-05, at TJO's request ("a detailed artifact explaining this stuff in totally elementary
yet correct terms ... start with the graph, basic linear algebra ... animations, interactive demos"). Explains
`../graph-ihara.md`, `../graph-super.md` and `../lattice-tower.md` for a reader with a physics background and no graph
theory. Status: **an exposition of a record.** It registers nothing; its status table repeats the record's statuses
(standard / checked / reading / negative finding; nothing reviewed).

Published as a Claude artifact: https://claude.ai/artifact/2KbsLkFaW2pBBHs5r1NQxc (private until shared).

## Files

| file | role |
|---|---|
| `page.html` | the page: prose, MathJax (tex-svg from cdnjs), CSS, and the demo scripts; `/*CORE*/` marks where the core is inlined |
| `core.js` | the numerical core, DOM-free: graphs, Jacobi eigensolver, Faddeev–LeVerrier characteristic polynomial, Hashimoto operator and traces, flux classes, matching polynomial, homology classes of closed walks, periodic syndromes of a one-mode step, the Ihara–Bass step-by-step check, exact (BigInt Bareiss) and LU determinants |
| `test.js` | headless checks of the core against the numbers recorded in `../checks/output_*.txt` (`node test.js`, all pass) |
| `build.js` | `node build.js` inlines `core.js` into `page.html` and writes the published file |
| `super-ihara-zeta-primer.html` | the built page, as published |

## Route of the page

Part A (graphs): adjacency matrix, eigenvalues and closed walks, non-backtracking walks and `B`, the Ihara zeta and
Ihara–Bass, zeros on the critical circle and RH for graphs. Section 4b proves Ihara–Bass by vectorisation: the edge
space is the vectorised adjacency pattern `P_A(V ⊗ V)`, the Hashimoto operator is the superoperator
`Ψ ↦ A ∘ ((J − 1) Ψ^T)`, the rank-one all-ones matrix factors it through the vertex space as `B = τσ^T − F`, and one
Sylvester step gives `det(1 − uB) = (1 − u²)^{|E|−|V|} det(1 − Au + (D − 1)u²)` for any graph. Part B (phase space):
the step `M = [[0, −1], [q, A]]`; Section 6 (expanded 2026-10-22 at TJO's request) in four parts: 6a the labelling
`(f, g) ↦ σf + τg` has rank `2n − 1` (`2n − 2` bipartite) with kernel `(1, −1)` (and `(χ, χ)`), the lost eigenvalue `μ = 1`
(`−1`) of the trivial mode being carried by the cycle space, so the phase space is the label space and `Ω` does not descend
to the edge space (where `B` is self-adjoint for `u·Fv`); 6b `M` is the second-order recurrence `f_{k+2} = A f_{k+1} − q f_k`
on labels `(f_k, −f_{k+1})`, which is why there are two numbers per vertex; 6c `Ω` is the Casoratian (discrete Wronskian)
and `M^T Ω M = qΩ` is Abel's formula, `S = M/√q` the damping-removed Chebyshev recurrence; 6d the three cases rotation /
shear / squeeze by the trace; a table of which forms live on which space. Demo 6 now shades the triangles `Ω(v_k, v_{k+1})`
and prints them (constant under `S`, `× q` under `M`). Then `M^T Ω M = qΩ`, the Weil form and its positivity as Ramanujan,
the three-gate factorisation. Part C (fermions): flux, double cover, bosonic and fermionic sectors, the super zeta, dark lines, RH on
average (matching polynomial). Part D (lattice states): GKP codes from scratch, the flux qubit on the cycle lattice,
the syndrome torus with the E mode's point counts 4, 8, 4, 16, 44, 56, the tower of codes and its blindness, RH as an
invariant vacuum, Deligne modules. Appendix: dictionary, status table, glossary.

Fourteen demos, every number computed live from the graph chosen (`K_4`, `K_5`, cube, Petersen, prisms `C_6 × K_2`
and `C_21 × K_2`). Headless render (Playwright) at desktop and phone width: no script errors, no MathJax errors; the only element wider than a
phone is the pre-existing Demo 2 walk table, inside its scrolling `.tablewrap`. Scratch check of the rank/kernel statements of 6a
on the five graphs (numpy, 2026-10-22): rank `[σ τ]` = 7, 19, 14, 9, 83 for K4, Petersen, cube, K5, prism21; kernel `M`-invariant.
