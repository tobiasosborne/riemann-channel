# Brief: the Riemann Tomography Problem, round 1 (RTP-1)

Author of the brief: `claude:fable-5.1`, 2026-09-24. Lanes: `claude:opus` workers, at most two in parallel,
each with its own lane file in this directory; REFUTE review lane afterwards. Background records:
`notes/metric-tomography/metric-as-state.md` (the problem, the channels, the MaxEnt ansatz, and the
correction of 2026-09-24 on single-place restrictions) and `notes/metric-tomography/finite-prime-language.md`.

## The problem

The Weil functional `W` of `zeta` is known exactly from the primes, the pole and the archimedean place (the
explicit formula). Its positivity on the admissible test class is RH (`cit:weil-criterion`). An
*observation* is a finite family of test functions `f_1..f_n` with Gram matrix `G_ij = W(f_i * f~_j)`,
`f~(u) = u^{-1} f(1/u)` on `R_+^x`. The *posterior* after an observation is the set of positive extensions
of the data. The *MaxEnt ansatz* is the maximum-determinant extension (for Toeplitz data: the centre of the
disc of `prop:extension-disc`, shard 08g). The *learning rate* of a channel is the contraction of the
posterior as arithmetic data (more primes, wider dilation, more prime content) are added.

## Game rules (binding for every lane)

1. RH is not assumed anywhere in a computation that produces a result.
2. Zeros of `zeta` are used **only** in explicitly labelled comparison steps (as `zst/src/compare.c` does),
   never as input to a form, an ansatz, or a certificate.
3. Every number that enters a form comes from primes, the pole and the archimedean local factor.
4. Certified (ball) arithmetic where the stack provides it; elsewhere, state precision and error control.

## Conventions (shared by all lanes; do not re-derive differently)

The Weil form is the one implemented in `zst/` (Connes–Consani–Moscovici, `refs/src/2511.22755/mc2arXiv.tex`;
formula sheet `notes/zeta-spectral-triples/plan.md` section 1): `QW(f, g) = Psi(f^* * g)` with
`Psi = W_{0,2} - W_R - sum_p W_p` (eq. `bombtest`, `mc2arXiv.tex` lines 385–388). In the log coordinate
`x = log u` the window `[lambda^{-1}, lambda]` is `[0, L]`, `L = 2 log lambda`, `x_window = lambda^2`, and
prime powers `k <= lambda^2` enter. In the Fourier basis `V_n` the matrix has the Loewner form
`tau_nm = (b_n - b_m)/(n - m)`, `tau_nn = a_n`, with `(a_n, b_n)` produced as balls by `zst/src/riemann_ab.c`
(closed forms in the formula sheet: pole, prime and archimedean parts). Any lane that implements `W` on a
different test class **must reproduce `zst`'s `(a_n, b_n)` on the Fourier basis to the printed precision
before reporting anything else**; that is the cross-lane consistency check.

## Lane A1: the dilation channel's contraction rate (Step 1)

Goal: measure how much the *next* datum teaches, along the two axes of the window channel, and compare the
result with the observed first-zero law `e^{-4 pi x}` (`notes/zeta-spectral-triples/benchmark.md`;
`x = lambda^2`).

A1.1 *Lemma (ellipsoid extension).* For a positive-definite Hermitian `G_K` and a bordered matrix
`[[G_K, c],[c^*, d]]`, the admissible set of the new column is `{(c, d) : d - c^* G_K^{-1} c >= 0}`; the
maximum-determinant completion with known diagonal `d` is `c = 0`; the information carried by the true
column is `Delta I_K = log(d / (d - c^* G_K^{-1} c)) >= 0` (the log-det gain over the MaxEnt prediction).
State and prove this in the lane file (two lines; Schur complement). This is the non-Toeplitz analogue of
`prop:extension-disc`(i)–(ii).

A1.2 *Axis N (resolution at fixed window).* At fixed `x` (take `x = 13, 25, 50` as far as the stack allows,
and at least `x = 13` certified), for `N = 2, 3, ..., N_max`: the window matrix on modes `|n| <= N` is a
principal submatrix of the one on `|n| <= N+1`. Compute, in ball arithmetic, the Schur complement of the two
new modes `+-(N+1)` (work in the even/odd blocks, `zst/src/blocks.c`) and `Delta I_N`. Tabulate `Delta I_N`
against `N`; report where it saturates relative to `N = 7.5 x` (the empirical saturation in the benchmark).

A1.3 *Axis x (primes at fixed resolution).* At fixed `N`, let `x` run through the prime powers
`2, 3, 4, 5, 7, 8, 9, 11, 13, ...` up to the largest affordable window. Each new prime power changes
`(a_n, b_n)` by the closed-form prime term. Record after each: the minimal eigenvalue `eps_N(x)` of the even
block, the overlap of its eigenvector with the eigenvector at the final `x`, and `log det` of the even block.
This is the learning curve of the dilation channel along the prime axis. Note that the window itself widens
with `x` (`L = log x`), so state clearly what is held fixed and what is not; if a cleaner protocol exists
(e.g. fixed `L` with the prime sum truncated below `x`, which is *not* the CCM form but is a legitimate
partial-information form), run both and say which is which.

A1.4 *Comparison step (zeros allowed, labelled).* For the same `x`, `N`, report `|z_1 - gamma_1|` from the
stack, so that `Delta I_N`, `eps_N`, and the first-zero error can be read side by side.

A1.5 Deliverables: `notes/rtp-round-1/lane-A1.md` (lemma, protocol, tables, "Findings against the brief");
code in `zst/tools/` or `zst/src/` (a new driver is fine; do not change the certified pipeline's behaviour;
`make check` must still pass); outputs under `outputs/rtp1_a1_*.txt`, byte-reproducible, no timestamps.

## Lane A2: the prime-content channel (Step 2)

Goal: build the Weil form on test functions concentrated on the `{p, q}`-lattice and measure the inter-place
structure that the dilation channel cannot separate.

A2.1 *Test class.* Fix a `C_c^infinity` bump `phi_delta(x) = exp(-1/(1 - (x/delta)^2))` on `|x| < delta`
(zero outside), in the log coordinate `x = log u`. For a finite prime set `S` and exponent box
`Lambda_S(A) = {(a_p)_{p in S} : 0 <= a_p <= A}`, the family is `phi_alpha(x) = phi_delta(x - sum_p a_p log p)`,
`alpha in Lambda_S(A)`. Then `phi_alpha^* * phi_beta` is supported within `2 delta` of `log(n_alpha / n_beta)`,
`n_alpha = prod p^{a_p}`, and `W(phi_alpha^* * phi_beta)` has prime contributions only from prime powers `k`
with `|log k - log(n_alpha/n_beta)| < 2 delta`. Choose `delta` so small that the only such `k` are the ratios
`n_alpha/n_beta` themselves when they are prime powers (which happens iff `alpha` and `beta` differ in at
most one coordinate). Compute and report the largest admissible `delta` for each `(S, A)` used (the minimal
distance from the lattice differences to the logs of all other prime powers in range).

A2.2 *Structure to verify.* (i) Every Gram entry between `alpha, beta` differing in two or more coordinates
is pole plus archimedean only. (ii) The `p`-axis entries carry the `p`-comb. (iii) Reproduce `zst`'s
`(a_n, b_n)` on the Fourier basis with the same `W` implementation (the consistency check of the
Conventions section) before anything else is reported.

A2.3 *Measurements.* For `S = {2}`, `{2,3}`, `{2,3,5}` and `A = 1, 2, 3, ...` as affordable, at two or three
values of `delta` below the admissible maximum: the Gram matrix; its minimal eigenvalue and eigenvector;
and the three decompositions

- `G` versus its block-diagonal restriction to the axis subspaces (test functions with a single prime),
  minimal eigenvalues of both: the gap is the inter-place contribution;
- `G` versus `G` with the mixed entries (two or more coordinates differing) replaced by zero: the gap is the
  contribution of the archimedean kernel sampled at logs of `S`-smooth rationals;
- `G` versus `G` with the prime terms removed (pole plus archimedean only): the contribution of the combs.

Report how the minimal eigenvector moves when a prime is added to `S` (restrict the `{2,3}` eigenvector to
the `{2}` axis and compare with the `{2}` eigenvector; likewise `{2,3,5}` to `{2,3}`).

A2.4 *Comparison step (zeros allowed, labelled).* For a few test functions, compare the prime-side value
`W(phi_alpha^* * phi_beta)` with the zero-side sum `sum_rho phi_alpha^(rho) conj phi_beta^(1 - rho-bar)`
truncated at the first `M` zeros (from `mpmath.zetazero`), as an implementation check of the explicit
formula in this normalisation. State the truncation error behaviour.

A2.5 *Precision.* Prefer `python-flint` (try `pip install python-flint`; the proxy allows PyPI) for balls;
otherwise `mpmath` at `mp.dps >= 40` with `quad` error estimates reported. The prime sums are finite and
exact up to arithmetic; the archimedean term is one integral against a smooth compactly supported function,
so control is straightforward. Say which is which.

A2.6 Deliverables: `notes/rtp-round-1/lane-A2.md` (definitions, the admissible `delta` table, the
consistency check, all measurements, "Findings against the brief"); `scripts/rtp1_prime_content.py`
(deterministic, `check(cond, msg)` helper as in `scripts/gl1_bond.py`, seed, no timestamps); output
`outputs/rtp1_prime_content.txt`, byte-reproducible.

## Lane B1: the exact theorems and their sources (Steps 3 and 6, after wave A)

Determine and byte-cite: what Bombieri (2000, *Remarks on Weil's quadratic functional in the theory of
prime numbers*) and Yoshida (1992, *On Hermitian forms attached to zeta functions*) prove about positivity
for short dilation support and about the archimedean form; Landau's formula
`sum_{0 < gamma <= T} x^rho = -(T/2 pi) Lambda(x) + O(log T)` (Landau 1912; Gonek 1993 uniform version);
Burg's maximum-entropy extension and Dempster's maximum-determinant completion; Bombieri–Lagarias 1999 on
the Li coefficients; Davis–Matiyasevich–Robinson 1976 and Lagarias 2002 on the `Pi^0_1` form of RH. For each:
local copy under `refs/src/<key>/` (PDF plus `pdftotext -layout`), exact statement with `file:line`, and a
one-paragraph reading of what it does and does not say for the steps above. Deliverable
`notes/rtp-round-1/lane-B1.md` and provenance-ready rows.

## Lane B2: the kinematic commutant and the calibration case (Steps 4 and 5, after wave A)

B2.1 On the window of lane A1 (fixed `x`, `N`), write the kinematic constraints as linear conditions on a
Hermitian form: invariance under the reflection `gamma: V_j -> V_{-j}` (the Weyl element in the window),
reality, and the Loewner (rank-two commutator) structure `[D, tau] = |beta><eta| - |eta><beta|`. Compute the
dimension of the admissible cone before any prime is seen, and the maximum-determinant element of the
window cone consistent with the pole and archimedean data alone. Report how far it is from the true form.
B2.2 Run the analogue of A1.2–A1.3 on one case where the metric is known and RH is a theorem: a Ramanujan
graph or the genus-one curve, with `scripts/weil_window_extension.py` and `ihz/` (shard 08g). Report the
learning curve there as the control signature. Deliverable `notes/rtp-round-1/lane-B2.md`, scripts and
outputs as for A2.

## Lane R: REFUTE review (after B)

Re-derive every displayed formula and every table entry independently; re-run every script; verdict per
lane item VALID / MINOR / INVALID with a scratch script per verdict. Standard protocol.

## What the round must answer

1. The two learning rates (dilation axis, prime-content axis) at matched information content (number of
   prime powers seen), and whether they agree.
2. How much of the two-prime form's minimal eigenvector lives off the axes, and whether that is carried by
   the archimedean kernel (as the correction of 2026-09-24 predicts) or by the combs.
3. Whether the `e^{-4 pi x}` convergence is explained by the kinematic envelope or is specific to the
   arithmetic (the question left open in shard 08g).
