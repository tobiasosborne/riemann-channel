# RTP-1: draft claims for the REFUTE lane

Author: `claude:fable-5.1`, 2026-09-24. These are the statements the orchestrator intends to register in a
shard after review, each with the lane that supports it. The reviewer verdicts each one (VALID / MINOR /
INVALID) against the lane files, scripts and outputs, with an independent scratch computation per verdict.

**C1 (lemma; lane A1.1, A1.1').** For positive-definite Hermitian `G_K` and a bordered matrix `[[G_K, c],[c^*, d]]`:
the admissible set of the new column is `{d - c^* G_K^{-1} c >= 0}`; with `d` known, the maximum-determinant
completion is `c = 0` and the log-det gain of the true column over it is `Delta I = log(d/(d - c^* G_K^{-1} c))`,
twice the Gaussian mutual information. Under the Loewner structure (`tau_nm = (b_n - b_m)/(n - m)`, `tau_nn = a_n`)
the new column is fixed by the single number `b_{N+1}` given `a_{N+1}`, the admissible set is an interval, its
centre is the structured MaxEnt prediction, and its endpoints are the singular enlargements. The unstructured
point `c = 0` is not a Loewner column.

**C2 (numerical; lane A1.2, A1.4).** On the CCM window at `x = 13, 25, 50` the log-det of the even block is
minimal at `N = 56, 134, 352` (`N_sat ~ 1.7 x log x`); below `N_sat` each new mode pair carries tens of nats and
the true `b_{N+1}` sits at the edge of its interval; above, a fraction of a nat and interior; the certified
minimal even eigenvalue at saturated `N` is `3.48e-59, 2.43e-123, 2.27e-257`, falling `5.34–5.36` digits per unit
of `x` against `5.46` for `e^{-4 pi x}`; the certified first-zero error is `~1e4 x eps_N` at every `(x, N)`
(comparison step, zeros used).

**C3 (numerical; lane A1.3).** At fixed window `L = log 50`, `N = 60`, the form with pole and archimedean terms
only has 3 negative even eigenvalues; adding prime powers one at a time leaves 3 to 16 negative eigenvalues
until the last prime power `49` enters (with all but `49`: `lambda_min = -5.66e-7`); with it,
`eps = 1.75e-116`. The minimal eigenvalue is a cancellation residual: each prime power below `x = 50`
contributes at least `1e34 eps`.

**C4 (lemma; lane A2, lemma 4.1).** For the lattice test class with admissible `delta`, replacing every Gram
entry between lattice points differing in two or more coordinates by zero yields exactly the Kronecker sum of
the one-prime forms (with the shared diagonal counted once), whose minimal eigenvector is the product of the
one-prime minimal eigenvectors.

**C5 (numerical; lane A2.3).** With `delta_max(S, A)` as tabulated (binding pairs `6/7`, `36/37`, `108/109`,
`1296/1297`; `30/31`, `450/449`, ...), all 42 Gram matrices are positive definite with simple minimal
eigenvalue; the mixed entries raise `lambda_min` by an amount linear in `delta`; the Schmidt defect of the
minimal eigenvector across the cut `{p} | rest` and the eigenvector movement on adding a prime scale as
`delta^2` (fitted slopes `2.00–2.06`); inside the mixed entries the pole part exceeds the archimedean part by a
factor `2.4` to `21` with opposite sign; removing the pole part of the mixed entries makes `{2,3}, A = 1` indefinite.

**C6 (observation, sketched; correction of 2026-09-24 in metric-as-state.md, lane B1 item 3).** For
`g = sum_k c_k phi(x - k log p)`, `W(g * g~) = sum_rho |phi^(rho)|^2 |P(p^{-rho})|^2` with `P` a polynomial: the
single-place restriction of `W` sees the zeros folded on the `p`-circle, the content of Landau's formula; mixed
`{p,q}` entries have no prime term and their zero-side Landau main term vanishes.

**C7 (cited facts; lane B1).** Yoshida 1992 Thm 1 (`a = log 2 / 2`, positivity with equality only at 0,
computer-assisted); Bombieri 2000 Thm 12 (lower bound `(log(1/|I|) - log^+ log(1/|I|) - O(1)) ||F||^2` for
`|I| < log 2`); the archimedean form alone is indefinite (Connes–Consani 2020; symbol negative for
`|t| < 6.2898`); Landau 1912 Satz 1; Burg 1975 (disc centre = zero reflection coefficients = maximum entropy);
Dempster 1972 / GJSW 1984 via Vandenberghe–Andersen; Bombieri–Lagarias Li formula via Coffey; Lagarias 2002;
DMR 1976 via Yedidia–Aaronson; Hulthén via Franchini; Tarski–Seidenberg projection via Coste.

**C8 (proposition; lane B1 item 4, derivation by the lane).** For Toeplitz data `nu_0..nu_K` with positive
definite `T_K`, the maximum-determinant positive completion of the next lag is the centre `c_K` of
`prop:extension-disc`, i.e. Burg's extension (zero reflection coefficient). Needs an independent proof check.

**C9 (proposition; lane B2.1(a)).** In the basis `V_n`, `|n| <= N`: Hermitian forms commuting with the reflection
`gamma` have dimension `(N+1)^2 + N^2`; real ones `(N+1)(2N+1)`; Loewner forms with `eta = sum V_n` have
dimension `4N+1` and are automatically real; Loewner and `gamma`-commuting: `2N+1`, exactly the data
`(a_0..a_N, b_1..b_N)`; the identity is interior to the positive cone of this space, so positivity removes no
dimension.

**C10 (numerical; lane B2.1(b)–(d), x = 13, N = 20).** With pole and archimedean data fixed and the prime data
`(u, v)` free, the positive set is full-dimensional and unbounded (recession cone the whole positive cone), so no
maximum-determinant element exists; zero prime data are inadmissible (`lambda_min = -1.96`); the minimal-norm
element has norm `2.36` against the truth's `8.21` and captures `8.3%` of the true prime data (falling to `2.8%`
at `N = 60`); the PNT mean captures `22%` and is inadmissible. With positions `log n`, `n = 2..12`, fixed and
weights free, positivity confines the weights to a box of width `<= 1.1e-7` for `n <= 9` (`1.3e-3` at `n = 12`),
including the zero weights at `6, 10, 12`.

**C11 (numerical; lane B2.2).** On a certified Ramanujan cubic graph on 40 vertices with `R = 78` atoms, the
window form's `lambda_min` falls as a power law in `x_eq = 2^K` (`0.13–0.79` digits per unit `K`) and reaches
exactly zero at `K = R`; the next trace is interior to its disc for `K < 77` and on the boundary at `K = 77`;
at fixed window every partial form is indefinite until the last cycle length enters; `lambda_min` is a
cancellation residual there too; the graph PNT is the maximum-determinant element at the largest window.

**C12 (observation, the round's reading).** (i) Question 1: the prime-content channel has no contracting signal
at matched information; its inter-place effects are `O(delta)`. (ii) Question 2: the off-axis structure of the
two-prime eigenvector is product-state weight plus an `O(delta^2)` correlation carried by pole plus
archimedean, pole first. (iii) Question 3: the `e^{-4 pi x}` law is arithmetic (kinematics fix `N_sat`, the
floor is a cancellation of all prime powers below `x`; the control graph shows a power law and a collapse).
(iv) MaxEnt in the Loewner coordinates is empty; the informative coordinates are the weights at the known
positions `log n`, where positivity alone pins the primes.
