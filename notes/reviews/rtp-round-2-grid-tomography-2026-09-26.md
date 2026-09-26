# REFUTE review: RTP round 2, lane G (grid tomography)

Reviewer: `claude:opus` (adversarial REFUTE protocol).
Date: 2026-09-26. Subject: `notes/rtp-round-2/grid-tomography/astra-proofs.md` (author `codex:gpt-6-astra`, 2026-09-26),
items G1–G6, the correction ledger, "Numerical checks for the blind lane" (117 checks) and the six candidate rows of
"What this changes in the notebook".

Nothing here assumes RH and no zero of zeta enters any computation (there is no comparison step in this review; the
only "comparison" is against `log n` and `Lambda(n)/sqrt n`, done after the blind solves). No lane file, script,
output, shard or `db/` row was edited; git was not run. Lane L's own review is being written in parallel; its files
were read, not written.

## Inputs read

| file | what it is |
|---|---|
| `notes/rtp-round-2/grid-tomography/astra-proofs.md` (in full), `astra-brief.md`, `progress.txt`, `astra-last.md`, `checks/manifest.json` | the report, its brief, progress lines, closing note, hashes |
| `notes/rtp-round-2/brief.md` | round rules and conventions |
| `scripts/rtp2_grid_tomography.py` (in full) | lane script: C/Arb bridge on `zst/build/libzst.a`, HiGHS Farkas LP, 160-digit simplex, Arb Farkas verifier, residual repair, axis sections, near-kernel profiles |
| `outputs/rtp2_grid_tomography.txt` (all non-table lines; tables spot-read) | 117 PASS, 0 FAIL |
| `checks/farkas_*.{in,json}`, `checks/boxes_*.json`, `checks/near_kernel.json`, `checks/axis_sections.json`, `checks/x13_N20.data`, `checks/x25_N60.data` (AB lines) | certificates, boxes, profiles, zst data |
| `notes/rtp-round-2/lattice-box/astra-proofs.md` (in full) | lane L: L1 recession, L2 duality, L3.2 coercivity non-uniqueness, L3.4 comparison step, L4 tables |
| `notes/rtp-round-1/lane-B2.md` §§2, 4 (headings and the lattice box) | the round-1 positive set and lattice box |
| `notes/reviews/rtp-round-1-2026-09-24.md` (header, verdict table, C2, C10, VERDICT block), `scratch_rtp1_ab.py`, `scratch_rtp1_commutant.py` (header) | format; the previous reviewer's independent `(a_n, b_n)` |
| `notes/reviews/rtp-round-2-impure-bumps-2026-09-26.md` (structure) | round-2 review format |
| `report/sections/08i_riemann_tomography.tex` l. 245–320 | `prop:window-kinematic-dimension`, `num:rtp-commutant`, `obs:rtp-round-1-reading` |
| `notes/zeta-spectral-triples/plan.md` §1.2–1.3 | closed forms of the pole/arch/prime data; even/odd blocks |

## Scripts written for this review (under `notes/reviews/`; deterministic, no timestamps)

None of them imports the lane script or calls `zst`; the lane's files are read only as data to be checked.

| script | checks | what it does |
|---|---|---|
| `scratch_rtp2_grid_common.py` | 6 | the reviewer's `(a_n, b_n)` in mpmath: pole by direct exponentials, archimedean by the `psi(1/2) - psi(A)`, `psi'(A)`, Lerch arrangement of `scratch_rtp1_ab.py` (not zst's `I_2/I_3/C(L)` split), atoms `A_n = -2(1-t)cos 2 pi n t`, `B_n = sin(2 pi n t)/pi`; agrees with zst's cutoff-1 and total data to 1e-59 at `x = 13, N = 20` and `x = 25, N = 60`, and with quadrature of the defining integrals to 1e-40 |
| `scratch_rtp2_grid_farkas.py` | 13 | all eleven lane Farkas certificates re-verified with the reviewer's `H0` and atom matrices, through the reviewer's closed form for the adjoint of the block assembly (tested against direct evaluation); rigorous constant-test repair of any residual |
| `scratch_rtp2_grid_blind.py` | 11 | **blind** problem `tau*(grid, N) = -max_{w>=0} lambda_min(H0 + T(w))` by Kelley cutting planes (cuts = eigenvectors of the current iterate, never of the true form); the reviewer's own emptiness certificates re-verified at 40 digits; the union grid containing `log n`; onset in `N` of emptiness for `M = 64, 128, 256`; grids shifted by `h/2` |
| `scratch_rtp2_grid_moments.py` | 13 | G1 span dimension and uniform-grid rank; constant test versus the actual mass bound; G2 annihilator `p` at `x = 13` (degree 16, in `span A_0..A_16`, `p >= 0`, zero set `{t_k, 1-t_k, 1}`), exact-moment LP on a 3999-point grid `∪` atoms `∪` reflections for `N = 1..20`; G3 autocorrelation identity by quadrature, single-mode counterexample |
| `scratch_rtp2_grid_kernel.py` | 10 | `lambda_min(H_true)` at `x = 13, N = 20` (80 digits); G5 at `x = 13, N = 60` from the reviewer's `H_true` at 140 digits (mpmath `eigsy`): eight smallest eigenpairs, `q_v` on the `L/256` grid, crossings refined by bisection, `v^T H0 v = int q_v dmu* + lambda` |
| `scratch_rtp2_grid_discover.py` | 3 | blind coarse-to-fine refinement from the uniform `L/256` grid (`x = 13, N = 20`) and the `L/128` grid (`x = 25, N = 60`); group masses and centroids compared with `Lambda(n)/sqrt n` and `log n` only after solving |

All scripts pass (56 checks, 0 failed). Float64 is used only in the blind cutting-plane searches; every emptiness
claim made from them is re-verified at 40 digits with a repair margin argument (below).

---

## Verdict table

| item | verdict | supporting script | one line |
|---|---|---|---|
| ledger 1–7 | correct | all | item 6 ("all eleven uniform grids infeasible") reproduced with independent certificates |
| G1 | **MINOR** | `moments` | factorisation, span `2N+1`, rank `min(M-1, 2N+1)`, compactness, lineality all right; "cheapest mass bound is the constant test" is false as worded (95.6 against an actual bound 4.41 at `M = 64`) |
| G2 | VALID | `moments` | extremality, `2N+1`-atom bound, exact-moment uniqueness for `N >= 2s` (16 / 26), endpoint caveat: all proved correctly; the bound is sufficient, empirically the `x = 13` measure is pinned from `N = 11` |
| G3 | VALID | `moments`, `kernel` | the brief's "nonnegative trigonometric polynomial" premise is false (autocorrelation, sign-indefinite); the replacement (trace against PSD `Z` with `q_Z >= 0`) is a correct one-line Markov bound, and it is exactly the form of G4's certificates |
| G4 | **MINOR** | `farkas`, `blind` | all eleven certificates re-verified with an independent `H0`; the union boxes are valid outer bounds; but "every pure grid is empty" is read as a discretisation failure when it is the positional signal, and the sentence "the prescribed displacement of all atoms onto the grid destroys feasibility" understates what is certified (every nonnegative measure on the grid is excluded) |
| G5 | VALID | `kernel` | eigenvalues, parities, all 32 crossings (to 1e-20) and the prime-power values reproduced; 0 crossings within `h` of a prime power |
| G6 | VALID | `farkas` | both `x = 25` certificates re-verified; factor 33241.58 |
| numerical checks section | VALID | — | 117 PASS counted; the five blind-lane targets are in `checks/boxes_*.json` / `near_kernel.json` as stated |
| "What this changes" (closing self-assessment) | **needs correction** | `blind`, `discover` | "the union controls do not discover positions independently" is fair for the union controls; but the report's own proposed relaxation, run blind on the report's own pure grids, **does** discover all eight positions to within `h` and the weights to 2% (below) |
| candidate rows | 5 VALID, 1 MINOR | | `obs:near-kernel-support-correction` carries a double status "PROVED / REFUTED" |

---

## G1. What the window sees: MINOR

*Factorisation.* `H(mu) = H0 + K(M mu)` with `K` the Loewner assembly, injective because the diagonal gives `a_n` and
row zero gives `b_n = n H_{n0}` (`b_0 = 0` since `B_0 = 0`). Correct. The span of the atom moment functions has
dimension exactly `2N+1` (the reflection argument `t -> 1-t` is right: `C(1-t) = C(t)`, `S(1-t) = -S(t)`, so
`(1-t)C + S = 0` and `tC - S = 0` add to `C = 0`); confirmed on random points for `N = 1..12`.

*Rank.* `rank M_N = min(M-1, 2N+1)` on the even-`M` uniform grid: the pair change of variables
`(w_t, w_{1-t}) -> ((1-t)w_t + t w_{1-t}, w_t - w_{1-t})` has determinant `-1`, cosine moments see only the first
coordinate (`M/2` distinct `c = cos 2 pi t`), sine moments only the second (`M/2 - 1` distinct `c` with `sin != 0`),
and the Chebyshev/`U` Vandermonde ranks add to `min(N+1, M/2) + min(N, M/2-1) = min(M-1, 2N+1)`. Confirmed by SVD for
nine `(M, N)` pairs including the boundary cases `M - 1 = 2N+1` (smallest retained singular value >= 0.69, next
exactly 0). "Every coordinate participates in a null vector" is right (a degree-20 polynomial cannot vanish at 31 of
32 distinct nodes).

*Compactness.* `E_00 = a_0 = a0_0 - 2 sum (1-t_j) w_j`, so `2 sum (1-t_j) w_j <= C` with `C = a0_0 = 2.98765` at
`x = 13`; compactness under H-SIGN and H-INT at every `N >= 0` follows. The endpoint argument (arbitrary mass can be
parked close enough to `L` because `||T(y)|| -> 0`) is right, and so is the continuity bound
`||T(y+delta) - T(y)|| <= (2N+1)(2+4 pi N)|delta|/L` (entry derivatives are bounded by `2 + 4 pi n` on the diagonal
and by `2(|n|+|m|)/|n-m| <= 4N` off it).

*Signed control and lineality.* Lineality space `ker M` (from injectivity of `K`), the signed `H(w) = I` construction,
and the projected moment intervals `[-a_n^0, +oo)` / `(-oo, +oo)` are correct.

*The defect.* "The grid set ... Its **cheapest** mass bound is already the constant test" is false as worded. The
constant test is the *simplest* fixed-sign functional; it is far from the cheapest. On the uniform `M = 64` grid it
gives `sum w <= C M/2 = 95.6`, while the actual mass maximum (the lane's own union LP, an outer bound, at `N = 20`) is
4.41, a factor 22 smaller; at `M = 256` the ratio is 382 against 6.93. The optimal bound on a linear mass functional
is the SDP dual `min tr(Z H0)` over PSD `Z` with `tr(Z T(t_j)) <= -c_j`, of which the constant test is the single
choice `Z = e_0 e_0^T`. The brief asked for the cheapest functional; the report answers a different question.
(`scratch_rtp2_grid_moments.py`, G1 lines.)

## G2. Moment fibres and exact-moment uniqueness: VALID

*Extremality* (finitely atomic with independent occupied moment vectors; `<= 2N+1` atoms; no atom at `L` since
`phi(1) = 0`) and the conic Carathéodory reduction are proved correctly; the perturbation `sigma = sum c_i 1_{E_i} mu`
with `|sigma| <= max|c| mu` is the right device for non-atomic `mu`.

*Uniqueness.* Checked line by line and numerically at `x = 13`: `p(t) = (1-t) prod_k (cos 2 pi t - c_k)^2` has cosine
degree `16 = 2s`, equals `sum alpha_n A_n` to 1.9e-39 on 998 points, is nonnegative on `[0,1]`, vanishes exactly on
`{t_k, 1-t_k}` and at `t = 1` (its 16 interior near-zero minima all lie within 2e-5 of those points), and
`int p dmu* = 0`. Any nonnegative `nu` with the same moments has `int p dnu = 0`, hence lives on the zero set; the
cosine/sine Vandermonde step then fixes both weights of each reflected pair (and `t = 1/2` alone, relevant at `x = 25`
where `log 5 = L/2`). The atom counts are right: `s = 8` at `x = 13` (2, 3, 4, 5, 7, 8, 9, 11; 13 is the invisible
endpoint), `s = 13` at `x = 25`, so `N >= 16` / `N >= 26`. The saturation cutoffs 56 and 134 are the full-window
argmins reproduced in the round-1 review.

*Sharpness (not claimed by the report, which says "sufficient, not claimed sharp").* The exact-moment LP on a
3999-point grid `∪` atoms `∪` reflections leaves `(1-t)`-weighted off-atom mass 1.47 up to `N = 7` and 1.24 at `N = 8`,
is numerically unresolved by HiGHS at `N = 9, 10` (status 4), and is zero to LP tolerance for every `N = 11..20`. So the
`x = 13` measure is pinned by its exact moments from about `N = 11 = s + 3`, well below `2s = 16`.

*Keeping moments and positivity apart (the brief's point (b)).* The report keeps them apart correctly and
consistently: ledger item 2, the last paragraph of G2 ("recovering those moments from the positivity inequality
remains the separate question"; "if `H* > 0` ... small new positive atoms remain feasible ... exact support recovery
from this inequality alone fails at every such cutoff"), and "What this changes". There is no conflict with lane L's
L3.2 / L3.4: G2 is an equality-constrained statement, L3.2 an inequality-constrained one, and G2 itself states the
L3.2 consequence in the grid setting.

## G3. The near-kernel premise refuted; replacement: VALID

The identity `q_v(y) = -v^T T(y) v = 2 Re int conj f(u) f(u+y) du` was checked by quadrature at three shifts for a
random `N = 3` vector (to 1e-15), and the single-mode counterexample `q = 2(1-t)cos 2 pi n t = -1` at `n = 1, t = 1/2`
is right. So `q_v` is a positive-definite (Bochner) function, not pointwise nonnegative, and not a trigonometric
polynomial (the envelope `1-t` is affine). The second gap the report names is real and quantitatively decisive: a null
vector gives only `int q_v dmu* = v^T H0 v - lambda`, and the reviewer's values of `v^T H0 v` for the eight smallest
eigenvectors at `x = 13, N = 60` are `0.0614, -0.335, 0.417, -0.104, 0.583, 0.145, 0.854, 0.526`: order one and of
both signs, so nothing forces `q_v` to vanish at an atom. The refutation stands.

The replacement (for PSD `Z` with `q_Z = -tr(Z T(.)) >= 0` on the allowed set, `int q_Z dmu <= tr(Z H0)`, hence
`mu({q_Z >= eta}) <= tr(Z H0)/eta`) is a correct one-line consequence of `tr(Z H(mu)) >= 0`. The report does not say
the one thing that makes it more than a remark: **every one of its own G4 infeasibility certificates is an instance of
this theorem with negative cost** (`q_Z(t_j) >= 0` on the grid and `tr(Z H0) < 0`, so no nonnegative measure on the
grid exists). The dual localisation is not hypothetical; it is what G4 computed.

## G4. Uniform grids empty; union boxes; axis sections: MINOR

### (a) The infeasibility certificates, independently

`scratch_rtp2_grid_farkas.py` reads the lane's frozen vectors and weights from `checks/farkas_*.in` as exact
decimals (so `Z = sum y_i v_i v_i^T + y_c e_0 e_0^T` is PSD whatever the vectors are), computes `co = K^*(Z)` by the
reviewer's closed form for the adjoint of the block assembly, and evaluates `tr(Z H0) = co . (a0, b0)` with the
reviewer's own pole/archimedean data and `q_Z(t_j) = co . phi(t_j)` with the reviewer's own atoms. Positive residuals
are repaired by adding `rho = max_j q_j^+ / (2(1-t_j))` to the constant-test weight (valid because `A_0(t) < 0` on the
interior), which raises the cost by `rho a0_0`. Result, all eleven cases:

| x | N | M | `max_j q_Z(t_j)` (40 digits) | repair `rho` | `tr(Z H0)` after repair | report |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 20 | 64 | 1.4e-42 | 2.1e-32 | -1.77218006360e-4 | -1.77218006360e-4 |
| 13 | 20 | 128 | 2.4e-42 | 2.1e-32 | -5.22841053980e-5 | -5.22841053980e-5 |
| 13 | 20 | 256 | -1.3e-42 | 2.0e-32 | -8.15313837417e-6 | -8.15313837417e-6 |
| 13 | 40 | 64/128/256 | <= 9.4e-42 | <= 2.7e-32 | -1.76874875812e-4 / -5.19936149409e-5 / -7.99157226501e-6 | same |
| 13 | 60 | 64/128/256 | <= 5.7e-42 | <= 8.0e-32 | -1.77041384553e-4 / -5.15631496452e-5 / -8.00093935025e-6 | same |
| 25 | 60 | 128 | 5.9e-42 | 1.4e-32 | -8.49321221948e-5 | -8.49321221948e-5 |
| 25 | 134 | 128 | 1.3e-42 | 1.6e-32 | -8.47189232157e-5 | -8.47189232157e-5 |

All eleven certificates are valid with data that share no code with `zst`, and every cost agrees with the report to
1e-10 relative. (The positive residuals of 1e-42 are the 1e-120-scale LP slack at active grid points seen at 40
digits; the repair is 28 orders below the cost.)

**Independent certificates that use no prime information.** The lane's Farkas LP is built from eigenvectors of the
*true* form, which encode the prime positions. For a certificate of emptiness that is legitimate (the origin of a
certificate is irrelevant), but it hides how robust the statement is. `scratch_rtp2_grid_blind.py` solves the blind
problem `max_{w >= 0 on grid} lambda_min(H0 + T(w))` with cuts taken only from eigenvectors of its own iterates, and
the LP dual is again a PSD `Z` with `tr Z = 1`: at `x = 13, N = 20` it certifies emptiness (40-digit re-verification,
same repair) with `tau* >= 1.7917e-4, 5.2528e-5, 8.2537e-6` for `M = 64, 128, 256`, and brackets
`tau* in [1.7968e-4, 1.7976e-4]`, `[5.2538e-5, 5.2556e-5]`, `[8.2537e-6, 8.2550e-6]`. The report's certificate costs
(`tr Z = 1` up to the repair, `Z` restricted to be diagonal in the true eigenbasis) are therefore lower bounds on the
minimal uniform relaxation `tau*` that are tight to 1.4%, 0.5% and 1.2%. Grids shifted by `h/2` are empty too
(`tau* >= 1.48e-4, 1.88e-5, 1.18e-5`).

**What infeasibility means.** No nonnegative measure supported on the grid (not merely the nearest-grid rounding of
the truth) makes the `N`-section PSD. It says nothing about measures off the grid, and the grid containing the exact
positions is feasible, as it must be: on the union grid (`M = 64` plus `log 2 .. log 12`) the blind solve has no
negative upper bound (bracket `[-3.5e-8, +3.6e-11]` after 300 rounds, i.e. feasible to float resolution), the truth
has float64 `lambda_min = -1.9e-15` (rounding), and its exact `lambda_min = 1.56610785511e-39` is reproduced at 80
digits (`scratch_rtp2_grid_kernel.py`) and certified positive by the lane's 1280-bit Cholesky.

**When it sets in.** The report computes only `N >= 20`. The blind onset scan (`N = 1..20`, emptiness re-verified at
40 digits at the first negative upper bound) gives the first `N` at which each uniform grid is certified empty:

| M (h = L/M) | 64 | 128 | 256 |
|---|---:|---:|---:|
| first certified-empty `N` | 7 | 8 | 9 |
| upper bound on `max lambda_min` one step earlier | +1.68e-4 (`N = 6`) | +2.82e-5 (`N = 7`) | +2.29e-6 (`N = 8`) |

(the earlier positive upper bounds are consistent with feasibility, not proofs of it). The onset sits at `N ≈ s = 8`,
next to the exact-moment pinning threshold (`N ≈ 11`, G2), not at a spectral-margin scale: `lambda_min(H_true)` is
`1.6e-39` already at `N = 20`, while the separating margin `tau*` is `1e-4 .. 1e-5` and almost independent of `N`
between 20 and 60 (the report's own table). Reading (not proved): the obstruction is moment geometry (the truth's
moment vector sits on a face of the moment cone that a grid missing the atoms cannot reach, cf. the annihilator `p` of
G2), not the near-singularity of the true form.

### (b) The report's reading of emptiness is wrong-footed

The report states that emptiness "exposes the failure of the chosen discretization" and that the optimizer tables are
"undefined". The second is true of the brief's literal request. The first is the wrong reading: emptiness is exactly
the event that the report's own proposed next experiment (the relaxation `H(mu) >= -tau I`, "track the minimum
required tau versus h, and the recovered support versus tau") converts into a blind position estimator, and that
experiment works on the report's own grids. See "Point (d)" below; it is the main finding of this review.

Also: "the prescribed small displacement of all atoms onto any of these grids destroys feasibility" understates what
the certificate proves. The script's `HISTOGRAM` lines (nearest-grid truth fails a true-eigenvector cut by
0.028–0.135) are that statement; the Farkas certificates exclude **every** nonnegative measure on the grid.

### (c) Union controls, axis sections, optimizers

The union LP is a valid outer relaxation (20 / 30 true-eigenvector cuts, occupied coordinates freed), weak duality is
applied correctly, and the 180-digit residual repair uses the genuine a priori scale `W_j = H0_00/(2(1-t_j))` with the
correct sign split (`r_j (w_j - w*_j) <= r_j (W_j - w*_j)` for `r_j > 0`, `<= -r_j w*_j` for `r_j < 0`). The report is
careful that these are not full-SDP projections, that the eigenvectors are selected with true data, and that the far
mass is dominated by the last grid point (checked: `far_upper` equals the `63L/64` and `255L/256` coordinate upper
bounds, 4.46197e-5 and 0.108468 at `N = 60`). The three blind-lane box targets (`L/64`: 1.19432844295e-25; `17L/64`:
4.53241895983e-22; `log 6`: 6.62432918801e-19, all `x = 13, N = 60, M = 64` union) are in `checks/boxes_x13_N60_M64.json`
as stated. The axis sections are the full PSD condition on a line, correctly called inner bounds. The existence and
strict positivity of the `sum w log w` minimiser on a feasible union grid is correctly argued.

## G5. Near-kernel profiles: VALID

Recomputed from the reviewer's `H_true` at 140 digits (no zst): eigenvalues `1.01356e-58, 8.54688e-55, 3.70021e-51,
1.07551e-47, 2.53815e-44, 4.59682e-41, 5.10118e-38, 3.39568e-35`, parities `0,1,0,1,0,1,0,1`, crossing counts
`0,1,2,3,4,5,8,9` (32 in all), every crossing equal to the lane's to 1e-20, none within `h` of a prime power;
`q_0(log 2, log 3, log 11) = 0.124124192448681281, 0.000882317836679668784, 1.0919383252618063e-34`, first root of
`q_1` at `0.307108616089253715988577`. The Spearman column measures envelope decay, as the report concedes; it should
not be carried into a shard. One reading the report does not draw: crossing number equal to eigenvalue rank for the
first six vectors is the Sturm pattern of a kinematic (prolate-type) eigenbasis, which is another reason the
near-kernel vectors cannot be expected to encode positions one by one.

## G6. x = 25: VALID

Both certificates re-verified (table above). `8.9594283855217e-6 / 2.695247303846e-10 = 33241.58`; ratio lower bound
2.6571300973791e10, `log 6` / `log 12` upper bounds `2.46551636223e-57` / `1.13084665287e-48` and the `log 23` interval
are in `checks/boxes_x25_N134_M128.json` as stated. The deduplication of `log 5 = L/2` is right and necessary.

## Numerical checks section: VALID

117 `PASS`, 0 `FAIL` in the committed output; the manifest hashes and counts match. The reviewer did not re-run the
lane script (it rebuilds its bridge and the LP boxes take tens of minutes); its data were instead checked from
independent code as above.

---

## Point (d): positivity discovers the positions blindly on the report's own grids

The closing claim, "The union controls show strong interior concentration ... they do not discover positions
independently, since the true logarithmic positions and eigenvectors enter their construction", is a fair description
of the union controls. It is not a fair description of what the lane's data can do, because the pure-grid problem the
lane found empty becomes, after the relaxation the lane itself proposes, a blind estimator that works.

**Experiment** (`scratch_rtp2_grid_blind.py`, `scratch_rtp2_grid_discover.py`). Inputs: pole and archimedean data
`H0` (reviewer's own), the window `[0, log x]`, H-SIGN, a uniform interior grid. Nothing else: no prime position, no
eigenvector of the true form, no weight. Solve `max_{w >= 0} lambda_min(H0 + sum_j w_j T(t_j))` (Kelley cutting planes,
cuts from the iterates' own eigenvectors). Only afterwards compare with `log n` and `Lambda(n)/sqrt n`.

**Result at `x = 13, N = 20`, grid `L/256` (h = 0.0100), `tau* = 8.254e-6`.** All mass above `1e-4` of the total sits
on exactly 16 grid points, the two grid neighbours of each of `log 2, 3, 4, 5, 7, 8, 9, 11`; there is no mass
anywhere else, including the edge strip and the composites. Per pair:

| n | centroid − log n | pair mass / (Lambda(n)/sqrt n) − 1 |
|---:|---:|---:|
| 2 | +7.8e-5 | +3.7e-4 |
| 3 | +3.0e-4 | +1.4e-3 |
| 4 | +1.2e-3 | +4.0e-3 |
| 5 | +7.1e-4 | -1.3e-3 |
| 7 | +1.4e-3 | +1.2e-2 |
| 8 | +4.1e-3 | -1.8e-2 |
| 9 | +1.9e-3 | -6.4e-3 |
| 11 | +2.2e-3 | +1.9e-2 |

Total mass 4.27829 against 4.26050. The same pattern (two points per atom, each within `h`, nothing else) appears on
the `L/128` grid and on the `L/128`, `L/256` grids shifted by `h/2`; on the coarsest grids (`L/64`, h = 0.040, plain and
shifted) the atoms 8 and 9 (0.118 = 2.9 h apart) share four support points, one of them up to 2.2 h from `log 9`
(script output of `scratch_rtp2_grid_blind.py`). One refinement level (17 points at spacing `h/8` around each support
point, warm-started cuts, bracket `[-2.410e-7, -2.082e-7]`) brings every centroid except `log 11` within `1.0e-4` of
`log n` (`log 2`: 2.1e-6; `log 3`: 5.8e-6; `log 5`: 1.2e-5) and every mass except `log 11` within `1.2e-3` of
`Lambda(n)/sqrt n`; `log 11`, the atom nearest the invisible edge, is the worst (1.0e-3 in position, 1.7% in mass).
A second level (spacing `h/64 = 1.57e-4`, bracket `[-1.72e-8, -3.6e-9]`, not fully converged) gives:

| n | 2 | 3 | 4 | 5 | 7 | 8 | 9 | 11 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| centroid − log n | 2.7e-8 | 1.6e-7 | 1.8e-7 | 1.8e-7 | -3.0e-7 | -3.4e-5 | -6.6e-5 | 7.8e-4 |
| mass / weight − 1 | 1.1e-7 | 7.8e-7 | -3.6e-6 | 3.0e-6 | -2.6e-5 | -5.0e-4 | -2.2e-4 | 1.3e-2 |

The recovery degrades monotonically towards the edge, which is lane L's L4.3 edge mechanism seen from the blind side.

**Where it fails, and why that matters for the next round.** At `x = 25, N = 60` on the `L/128` grid (h = 0.0251) the
blind maximiser (bracket `[-8.70e-5, -8.57e-5]`) finds twelve clusters, every centroid within `h` of a prime power,
no mass elsewhere; the first nine (2 .. 13) have centroids within `2.4e-2` and masses within 7%. But `log 16` and
`log 17` (0.0606 = 2.4 h apart) are not separated (one cluster, centroid `0.021` below `log 17`), and the clusters at
19 (five points) and 23 carry +35% and +38% excess: total mass 7.453 against 7.162, the missing weight of 16 plus
cheap mass on the edge side of the window. Resolution `h` and the edge are the two limits, exactly the two the
report identifies for its outer boxes.

**What this shows and what it does not.** It shows that positivity of the finite window form, with pole and
archimedean data exact and H-SIGN, is by itself a position-finding device at the resolution of the grid (run here at `N = 20` and `60`; the grids are
empty, hence carry the signal, from `N ≈ s` on): the most-positive grid measure is an honest estimator of the prime measure. It does not show exact
recovery (G2 and lane L3.2 forbid that at any finite `N` with a positive margin, and under RH at the infinite window
too), it does not show that the maximiser is unique (at the refined levels the cutting-plane iterate is only near
optimal), and it is float64: below `tau ~ 1e-9` a multiprecision SDP is needed. The honest experiment the notebook
should now run is this one, with a certified SDP solver in place of Kelley, movable atoms in place of the fixed
refinement, and a stability theorem as its target (below).

---

## Corrections to apply

1. **G1, "cheapest".** Replace "Its cheapest mass bound is already the constant test:" by
   "The simplest fixed-sign mass functional is the constant test (it is not the cheapest: the optimal bound on a
   linear mass functional is the SDP dual `min tr(Z H0)` over PSD `Z` with `tr(Z T(t_j)) <= -c_j`, and at `x = 13`,
   `M = 64` the constant test gives `sum w <= 95.6` against an actual maximum `<= 4.41` at `N = 20`):".

2. **G3, last paragraph.** Append: "Every G4 infeasibility certificate is an instance of this bound with negative
   cost: `q_Z >= 0` on the grid and `tr(Z H0) < 0`, so no nonnegative grid measure exists."

3. **G4, positional sentence.** Replace "This is already a positional observation: the prescribed small displacement of
   all atoms onto any of these grids destroys feasibility." by "This is already a positional observation: no
   nonnegative measure supported on any of these grids (not only the nearest-grid rounding of the truth) is feasible.
   The emptiness sets in at `N = 7, 8, 9` for `M = 64, 128, 256` (review, `scratch_rtp2_grid_blind.py`), near the
   atom count `s = 8`, and the separating margin (`tau* = 1.797e-4, 5.25e-5, 8.25e-6` at `N = 20`) is independent of
   `N` from 20 to 60, so it is not set by the near-singularity of the true form."

4. **G4, certificate costs.** After "these are certificate costs, not claimed optimal separating margins" add "; with
   `tr Z = 1` they are lower bounds on the minimal relaxation `tau*` in `H(w) >= -tau I`, tight to 1.4%, 0.5%, 1.2% at
   `x = 13, N = 20` (review)".

5. **"What this changes", second paragraph.** Replace "It also exposes the failure of the chosen discretization: every
   prescribed pure grid is empty. The union controls show strong interior concentration and a weaker edge region;
   they do not discover positions independently, since the true logarithmic positions and eigenvectors enter their
   construction." by "Every prescribed pure grid is empty. This is the positional signal, not a failure of the
   discretization: the relaxed problem `max_{w >= 0} lambda_min(H0 + T(w))` on the same grids, which uses no prime
   position and no true eigenvector, puts all its mass on the two grid neighbours of each visible prime power at
   `x = 13` (centroids within `h`, masses within 2%; review, `scratch_rtp2_grid_discover.py`). The union controls, by
   contrast, do not discover positions independently, since the true logarithmic positions and eigenvectors enter
   their construction."

6. **Candidate row `obs:near-kernel-support-correction`.** Status "PROVED / REFUTED" is not a single status. Make it
   `proved`, with content "Individual `q_v` are signed autocorrelations and `int q_v dmu* = v^T H0 v - lambda` is of
   order one and either sign at `x = 13, N = 60`; the brief's near-kernel support rule is refuted; localisation
   requires PSD `Z` with `q_Z >= 0` and small known cost (and with negative cost it certifies emptiness)."

7. **Candidate row `prop:loewner-sparse-measure-uniqueness`.** Add "sufficient, not sharp (at `x = 13` exact moments
   pin the measure from `N ≈ 11`)".

8. **G5.** Drop the Spearman column from anything registered; it measures the envelope.

---

## Recommendation for shard 08j

**What the tomography problem is, after lanes L and G.** Unknown: a nonnegative measure `mu` on the open window
`(0, L)`, `L = log x` (the endpoint is invisible and must be quotiented out; near it only `(1-t)`-weighted mass is
controlled). Known exactly: the pole and archimedean data `H0`. Constraint: `H_N(mu) = H0 + K(M_N mu) >= 0` for the
cutoffs `N` used. The window sees `mu` only through the `2N+1` moments `M_N mu` (G1). Four facts now frame it:

1. *Exact moments would suffice.* An `s`-atom interior measure is the unique nonnegative measure with its moments for
   `N >= 2s` (G2), empirically from `N ≈ s + 3` at `x = 13`.
2. *Positivity never gives exact moments.* At every finite `N` with `H_N(mu*) > 0` the feasible set contains a
   neighbourhood of the truth in weights **and positions** (G2 last paragraph, lane L3.2); under RH the same holds for
   the infinite window at fixed `x` (lane L3.4, comparison step). "Positivity pins the primes" can only mean
   resolution, never exact recovery at fixed `x`.
3. *The feasible set is nonetheless extremely thin in position.* No measure on a uniform grid of spacing
   `L/64 .. L/256` is feasible once `N >= 7 .. 9` (G4/G6, certified; review onset scan).
4. *The most-positive measure is a blind estimator.* On those grids the maximiser of `lambda_min(H_N(mu))` finds every
   visible prime power at `x = 13` to within `h` and its von Mangoldt weight to 2%, with no mass elsewhere; refinement
   improves this (review). At `x = 25, L/128`, resolution and the edge limit it.

The problem is therefore: **the stability of the most-positive (or maximum-determinant) measure** — bound the
distance of its support from `{log n}` and of its weights from `Lambda(n)/sqrt n` in terms of the relaxation `tau`,
the cutoff `N` and the window, uniformly as the grid is refined, with the edge strip excluded. The natural route
combines the exact-moment annihilator `p` of G2 with the PSD dual certificates of G3/G4: a `Z >= 0` whose `q_Z`
approximates `p` (nonnegative, vanishing only at the atoms) with small `tr(Z H0)`.

**Rows to register (after the corrections):** `prop:window-measure-moment-factorization`,
`prop:window-sign-grid-compactness` (with correction 1 in the text), `prop:loewner-sparse-measure-uniqueness`
(correction 7), `obs:near-kernel-support-correction` (correction 6), `num:rtp-grid-infeasibility` (add the onset
`N = 7, 8, 9` and the `tau*` brackets as review-computed values), `num:rtp-grid-union-localization` (as proposed,
"outer bounds, true positions and eigenvectors seeded").

**A new row, reviewer-computed, `numerical`:** `num:rtp-grid-blind-recovery` — "`x = 13, N = 20`, uniform `L/256`
grid, pole/arch data only, H-SIGN: the maximiser of `lambda_min` over grid measures (`tau* = 8.25e-6`) is supported on
the 16 grid neighbours of the eight visible prime powers; pair centroids within `4.1e-3` of `log n`, pair masses
within 2% of `Lambda(n)/sqrt n`; two refinement levels bring `log 2 .. log 7` within `3e-7` (masses within `3e-5`)
and `log 11` within `8e-4`; float64 cutting planes, emptiness of the grid re-verified at 40 digits; at `x = 25,
N = 60, L/128` twelve clusters (16 and 17 unresolved, edge excess at 19 and 23)." Scripts: `notes/reviews/scratch_rtp2_grid_blind.py`,
`scratch_rtp2_grid_discover.py`. It should be re-derived by a lane with a certified SDP before it is promoted beyond
`numerical`.

**Next experiment (one).** The blind estimator with a multiprecision SDP (the lane's Arb stack for the cuts,
movable atoms seeded from the level-0 clusters), at `x = 13, 25, 50`, edge strip `[L - 2h, L]` excluded; record
position and weight error against `tau*` and `N`. That is the tomography problem in the coordinates it should be posed
in, and it is now known to have signal.

---

VERDICT G1: MINOR — "Its cheapest mass bound is already the constant test" is false as worded: the constant test is the simplest fixed-sign functional, not the cheapest (95.6 against an actual mass maximum <= 4.41 at x = 13, M = 64, N = 20); everything else in G1 (factorisation, span 2N+1, rank min(M-1, 2N+1), compactness, lineality, continuity bound) is correct.

VERDICT G2: VALID

VERDICT G3: VALID

VERDICT G4: MINOR — all eleven certificates re-verified with independent data, union boxes valid outer bounds; but "every pure grid is empty" is read as a discretisation failure although the relaxed pure-grid problem blindly recovers the positions, and "the prescribed displacement of all atoms onto the grid destroys feasibility" understates the certificate, which excludes every nonnegative measure on the grid.

VERDICT G5: VALID

VERDICT G6: VALID

VERDICT prop:window-measure-moment-factorization: VALID

VERDICT prop:window-sign-grid-compactness: VALID

VERDICT prop:loewner-sparse-measure-uniqueness: VALID

VERDICT obs:near-kernel-support-correction: MINOR — the status "PROVED / REFUTED" must be a single status: register as proved, with the brief's premise recorded as refuted in the text (correction 6).

VERDICT num:rtp-grid-infeasibility: VALID

VERDICT num:rtp-grid-union-localization: VALID
