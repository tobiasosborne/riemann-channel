# Brief: visualisation package for the Riemann Tomography Problem, round 1 (lane V)

Author of the brief: `claude:fable-5.1`, 2026-09-24. Worker: `claude:opus`. Purpose: one figure set per
step of `brief.md`, so that the objects (test functions, windows, lattices, forms, posteriors) and the
results of lanes A1, A2, B1, B2 can be *seen*. Figures are secondary sources: every number plotted comes
from a committed output file or is recomputed by the figure script with the same conventions, and the
caption says which.

## Ground rules

- Package: `viz/rtp1/` (Python, matplotlib, numpy, mpmath, python-flint where needed), one script per
  step, `make_all.py` that runs them, figures written to `figures/rtp1/<step>_<name>.{png,svg}`.
  Deterministic; no timestamps; runtime under ten minutes in total.
- Load the `dataviz` skill before writing any chart code and follow it (one palette, light and dark
  safe, no chart junk).
- Game rules of `brief.md` apply to figures too: zeros of `zeta` appear only in panels explicitly
  labelled "comparison (zeros used)".
- Conventions: those of `brief.md` (the CCM Weil form, window `[lambda^{-1}, lambda]`, log coordinate,
  Loewner data `(a_n, b_n)` from `zst`). Reuse `scripts/rtp1_prime_content.py` for the prime-content
  forms (import its functions; do not re-derive) and read lane A1's outputs `outputs/rtp1_a1_*.txt` for
  the dilation channel (parse, do not recompute what is certified there; recompute only for pictures the
  outputs do not contain, e.g. matrices and eigenvectors, and say so).
- An index page `figures/rtp1/index.html` with every figure, its caption, its data source and the
  script that made it; also `figures/rtp1/README.md` with the same in Markdown.

## Step 0: the objects

- The multiplicative line in the log coordinate with the CCM window for `x = 13` and `x = 50`, the
  prime-power point masses `Lambda(k) k^{-1/2}` at `log k` (the "prime comb"), and the smooth part of the
  Weil distribution `D(y)` (pole and archimedean, drawn separately and summed), on the same axis.
- The Fourier test functions `V_n` in the window for a few `n`, and a `C_c^infinity` bump `phi_delta`
  centred at `log 6` with the admissible `delta` for `{2,3}, A = 1` (`0.077`), against the neighbouring
  prime powers `5, 7` (why admissibility bounds `delta`).
- The `{2,3}` lattice as points `log(2^a 3^b)` on the line for `A <= 3`, coloured by `a + b`, with the
  foreign prime powers marked; the same for `{2,3,5}`, `A <= 2`.
- The convolution picture: for two bumps at `log 4` and `log 6`, the support of `phi^* * phi` around
  `log(3/2)` and which prime powers it touches for two values of `delta` (one admissible, one not).

## Step 1: the dilation channel (lane A1)

- Heat maps of the window matrix `tau` (Loewner form) for `x = 13`, `N = 30`: full, even block, odd block;
  and the minimal even eigenvector `xi` drawn as a function in the window (the "ground state of the
  window") for `x = 13, 25, 50`.
- `Delta I_N` against `N` at fixed `x` (three curves), with the empirical saturation `N = 7.5 x` marked.
- The learning curve along `x`: minimal eigenvalue `eps_N(x)`, eigenvector overlap with the final `x`,
  and `log det` of the even block, with a vertical tick at every prime power; both protocols of lane A1
  (CCM window and fixed `L`) as separate panels.
- The envelope panel: whatever lane A1 reports as the kinematic envelope, against `e^{-4 pi x}` and
  against `|z_1 - gamma_1|` (the last labelled "comparison (zeros used)").
- The posterior picture: for one `N`, the admissible ellipsoid of the next column (lemma A1.1) projected
  onto the two dominant directions, with the MaxEnt point (the centre, `c = 0`) and the true column.

## Step 2: the prime-content channel (lane A2)

- Gram-matrix heat maps for `{2,3}`, `A = 2`, at `0.9 delta_max`: `G`, its prime-free part, its mixed
  entries, and the pole and archimedean parts of the mixed entries side by side (same colour scale).
- The minimal eigenvector of `G` on the `(a, b)` grid for `{2,3}`, `A = 2, 3` and on the `(a, b, c)` grid
  for `{2,3,5}`, `A = 2` (three slices), next to the product-state (Kronecker-sum) eigenvector.
- Scaling panels from `outputs/rtp1_prime_content.txt`: the mixed-entry gap against `delta` (linear), the
  Schmidt defect against `delta` (quadratic, log-log with slope 2), the eigenvector movement `{2} -> {2,3}`
  and `{2,3} -> {2,3,5}` against `delta`.
- The admissible `delta_max` against `A` for the three prime sets (log scale), annotated with the binding
  pairs (`6 vs 7`, `36 vs 37`, ...).
- The explicit-formula comparison: prime-side value against the zero-side partial sums as `M` grows for
  two entries, labelled "comparison (zeros used)".

## Step 3: short-range positivity (lane B1)

- The Weil distribution near the origin: the interval `|y| < log 2` with no prime mass, the archimedean
  kernel `rho(x)`, and the pole term; a bump supported inside it and its (positive) form value; then the
  same bump widened past `log 2`, with the `2`-comb entering. Caption states what Bombieri and Yoshida
  prove, as lane B1 reports it (read `notes/rtp-round-1/lane-B1.md` if it exists; otherwise caption
  "statement pending lane B1").

## Step 4: the kinematic commutant (lane B2, if its outputs exist by the time you run; otherwise skip
with a placeholder page that says so)

- A 3-dimensional slice of the window's positive cone with the kinematic subspace, the maximum-determinant
  element from pole and archimedean data only, and the true form.

## Step 5: the calibration case (lane B2, same proviso)

- The learning curves of Step 1 for a Ramanujan graph or the genus-one curve next to those of `zeta`.

## Step 7: the contradiction pathway and MaxEnt (from `notes/metric-tomography/metric-as-state.md`)

- The disc of `prop:extension-disc` (shard 08g) as the Schur algorithm proceeds: nested admissible discs
  for the next trace at lags `K = 1, 2, 3, ...` for a small example where everything is explicit
  (use the graph or permutation example of `scripts/weil_window_extension.py`), with the centre (MaxEnt
  prediction) and the true next trace marked; the picture of "keep adding constraints, update".
- The off-line pair cartoon: for a toy sequence with one pair `rho, 1 - rho-bar` off the line, the `2 x 2`
  indefinite block and the test function that exposes it, drawn as the Weil form restricted to a
  two-dimensional span (a saddle), versus the on-line case (a bowl).

## Deliverables

`viz/rtp1/` with scripts and `make_all.py`; `figures/rtp1/` with figures, `index.html` and `README.md`;
`notes/rtp-round-1/lane-V.md` listing every figure, its data source, its script, and a "Findings against
the brief" section (anything that could not be drawn, and why). Do not commit; the orchestrator commits.
