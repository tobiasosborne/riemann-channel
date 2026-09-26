# REFUTE review: RTP round 2, lane L (lattice positivity, recession, widths)

Reviewer: `claude:opus` (adversarial REFUTE lane). Date: 2026-09-26.
Subject: `notes/rtp-round-2/lattice-box/astra-proofs.md` (author `codex:gpt-6-astra`, 2026-09-26), statements L1–L6, the
numerical-checks section and the nine proposed claim rows for shard 08j.

Nothing here assumes RH except where a statement is explicitly conditional on it (L3.4, checked as mathematics, no
numerics). No zeta zeros are used anywhere. No lane file, script, output, shard or `db/` row was edited; `zst/` was not
touched (the reviewer's C printer links `zst/build/libzst.a` read-only, as `scripts/rtp1_commutant.py` does).

## Inputs read

| file | what it is |
|---|---|
| `notes/rtp-round-2/lattice-box/astra-proofs.md` | the lane report under review (all of it) |
| `notes/rtp-round-2/lattice-box/astra-brief.md`, `notes/rtp-round-2/brief.md` | lane and round briefs (conventions, game rules) |
| `scripts/rtp2_lattice_box.py` (C bridge, simplex, recession search, sections), `outputs/rtp2_lattice_box.txt` | lane script and output; not re-run (heavy, 1280-bit); `checks/replay.txt` is byte-identical to the output (`cmp`) |
| `notes/rtp-round-2/lattice-box/checks/{README.md,audit.txt,cold-start.txt,reproduction.txt,recession.certificates,sections_N*.certificates}` | lane artefacts |
| `notes/rtp-round-1/lane-B2.md` §§2, 4; `notes/rtp-round-1/lane-A1.md` (eps table, line 208) | round-1 lattice box and eps values |
| `notes/reviews/rtp-round-1-2026-09-24.md` (C10, verdict lines), `notes/reviews/scratch_rtp1_commutant.py` | previous review, its LP simplex (re-typed here) |
| `scripts/rtp1_commutant.py` (C printer, lines 138–190) | how `(a_n, b_n)` are read from `zst` |
| `report/sections/08i_riemann_tomography.tex` (`prop:window-kinematic-dimension`, `num:rtp-commutant`, `obs:rtp-round-1-reading`) | registration target |
| `notes/zeta-spectral-triples/plan.md` §1 | formula sheet (Loewner data, blocks) |
| `refs/src/2511.22755/mc2arXiv.tex` lines 398–425 (Weil class, eq. `bombieriexplicit`), 560–680 (`Hilbert1`, `thmsmallest`, `lowest`, the remark after it, `strange`) | the CCM input cited in L3.3–3.4 |
| arXiv:1702.04099 (Carneiro–Chirre) e-print TeX, fetched to the reviewer's scratchpad only (it is **not** in `refs/`), lines 183–215 | the counting input cited in L3.4 |

## Scripts written by this review (`notes/reviews/`, deterministic, no zeros)

| script | checks | what it does, independently of the lane |
|---|---|---|
| `scratch_rtp2_lattice_common.py` | (helper) | own C printer on `libzst.a` (`zst_riemann_ab` at 1000 bits, 220 digits; prime cutoff `x` and `1`), own Loewner blocks (plan.md §1.3), own atoms, own von Mangoldt |
| `scratch_rtp2_lattice_box.py` | 52 (x=13,N=20 with SDP) + 17–30 per LP-only case | eigen-decomposition by mpmath `eigsy` (not FLINT QR); eigenvector-LP box by a Bland simplex at 160–250 digits, with an independent optimality check (primal vertex from the dual support, feasibility against every cut, zero gap); the **full SDP box** (all other weights free) by a primal barrier method in whitened coordinates, with inner points (Cholesky/eigsy at 160 digits, also in the unwhitened basis) and dual certificates `Z = mu M^{-1}` (outer bounds, residual charged against the LP box); LP-vertex feasibility; the L2 positive-spanning bound with the exact null vector; the "needle" structure |
| `scratch_rtp2_lattice_recession.py` | 25 | L1's annihilator on random positions and its explicit PD dual certificate; `t -> 0` and edge cases; `||T_k||`; L5 for m = 2..11 by the reviewer's own barrier SDPs (RAY and ZERO problems), witnesses re-verified at 60 digits (exact projection onto the atom-orthogonal space, eigenvalues) |
| `scratch_rtp2_lattice_coercive.py` | 20 | L3 on a toy window form `mu I + (c e^{-y})` with the lane's atoms: `||T_k|| <= 2`, the open ball `2||delta||_1 < mu`, axis half-widths `>= mu/||T_k||`, impossibility of H-PIN under H-GAP, the diagonal `eps_N -> 0` example |
| `scratch_rtp2_lattice_saturation.py` | 3 | `N_sat` at x = 13, 17, 25 by one mpmath Cholesky of the N = 200 blocks (prefix sums of log pivots) |
| `scratch_rtp2_lattice_maxdet.py` | (numbers) | the lattice max-det optimizer at x = 13, N = 20 by damped Newton at 160 digits, against truth and the SDP box |

Runs: `python3 scratch_rtp2_lattice_box.py 13 20 sdp` (≈ 10 min on 22 cores; 53 checks, 0 failed), `... 13 40 sdp 2,12`
(58 min), and LP-only `... X N nosdp` for (13,56), (13,60), (17,60), (17,83), (19,94), (23,123), (25,60), (25,134).
One caveat on the reviewer's own check lines: two early runs flagged FAIL on the reviewer's tolerances, not on the data
(the zst/`H0 + T(w*)` agreement is limited by the 220 printed digits, `1e-219`; the x = 25, N = 134 edge LP has dual
multipliers up to `~1e67`, so its absolute residual `2.4e-184` at 250 digits is a relative `1e-251`). Both thresholds were
made relative (the final script uses `1e-(DPS-40)` times the largest multiplier); the widths agree with the lane to all
printed digits in every case.

## Table of checks

| # | statement | what was checked | result |
|---|---|---|---|
| 1 | L1 proof | annihilator `P, Q`, signs `c_k <= 0`, positivity of all `q_n`, vanishing at `e(t_k)`; zero diagonal ⇒ zero row; Chebyshev/Vandermonde injectivity incl. reflected pairs | correct; `Z = diag(q)` is an explicit PD dual certificate (4 random geometries, `tr(Z T_k) = 0` to 1e-15) |
| 2 | L1 counterexamples | one atom at `t -> 0` (`N = 5, 20, 60`), edge atom `t = 1` | `-T > 0` (λ_min 1.996); `T_L = 0` |
| 3 | L1 bound vs truth at x = 13 | `B = 4 sum r_k` | `B = 108` for the eleven atoms; actual first cutoff 6 |
| 4 | L1 lower bound (not in the lane) | `2N+1 <= m` ⇒ nonzero cone | proved below; explains the whole L5 table except m = 2 |
| 5 | L2 duality, signs, SDP/LP | weak duality, sign correction of the brief, Slater, examples 2.4 | correct |
| 6 | L2 conditioning bound | `2 a_k sum h_i lambda_i`, `r = m+1`, exact null vector | positively spanning in every case run; bound within **1.9–4.0×** of the LP width; the `2 a_k lambda_r` form is `1e13`–`1e34` too large |
| 7 | L3.1–3.2 | dual pin, converse, coercive ball, counterexamples | correct; toy confirms ball and `half-width -> mu/||T_k||` |
| 8 | L3.3–3.4 (RH ⇒ coercive) | CCM `Hilbert1`, `thmsmallest`, `lowest`; explicit formula on the core; Jensen vs distinct ordinates | correct; two citation defects (below) |
| 9 | `||T_k||` | operator norm on `E_N`, N ≤ 200 | ≤ 2; numerically `-> 2 cos(pi/(ceil(L/y_k)+1))` (1.618 at n = 2, 1.414 at n = 3, 1 for `y_k > L/2`) |
| 10 | L4 spectra | `eps`, `lambda_m`, `lambda_{m+1}` at 9 of the 10 cases | all agree with the lane's table to the printed digits |
| 11 | L4 LP widths | own LP at (13,20), (13,56), (13,60), (17,60), (17,83), (19,94), (23,123), (25,60), (25,134) | every compared width (n = 2, 6, 12, edge) agrees with the lane to all printed digits |
| 12 | L4 `r_used` | largest spectral index in optimal duals | 12 (13,56), 12 (13,60), 18 (17,60), 18 (19,94), 28 (25,60), 26 (25,134): match |
| 13 | L4 `N_sat` | argmin of log det, N ≤ 200 | 56, 83, 134 and log dets to 12 digits: match |
| 14 | L4 monotone widths | widths strictly increasing in n | true in all 9 boxes |
| 15 | **full SDP box** (lane's "one next step", left OPEN) | barrier method at x = 13, N = 20, all 11 coordinates; N = 40 for n = 2, 12 | **LP/SDP = 2.38–2.56** at N = 20, **2.01–2.02** at N = 40 |
| 16 | two-coordinate sections | against the full SDP widths | valid inner bounds but **8–9 orders** below the SDP widths |
| 17 | LP geometry | which vertices attain the box | all 2m endpoints come from **two** vertices (a needle), in all six cases tested |
| 18 | max-det optimizer (prop:rtp-lattice-maxdet) | Newton at N = 20 | exists, unique, **is not the truth** (λ_min 1.3e-27 vs 1.6e-39) |
| 19 | L5 | first zero-cone cutoffs m = 2..11 | `2,2,2,3,3,4,4,5,5,6` reproduced with certified witnesses |
| 20 | L6 | zeros in script / certificates | none |

## L1. Recession cone — VALID

The proof is correct as written. Checked step by step: `r_k s_k in [1/4, 1/4 + s_k) ⊂ [1/4, 3/4]`, so `c_k <= 0`;
each factor `1 - 2c_k z^{r_k} + z^{2 r_k}` vanishes at `e(±t_k)` and has nonnegative coefficients; `Q = P (1 + ... + z^d)`
has all `2d + 1 = B + 1` coefficients `>= 1` (constant and leading term of `P`); the real part gives
`sum_{n<=B} q_n a_n(delta) = 0`, hence `a_n = 0` for `n <= B`; the zero `(0,0)` diagonal entry kills row 0,
`tau_{0j} = b_j/j`, hence every `b_j` and every off-diagonal entry; injectivity by grouping `cos(2 pi t)` and
`sin(n theta) = sin(theta) U_{n-1}(cos theta)` is right, including `t` and `1 - t`. `scratch_rtp2_lattice_recession.py`
confirms the identity on four random geometries and makes the dual content explicit: `Z = diag(z)`, `z_0 = q_0`,
`z_{±n} = q_n/2`, is positive definite and orthogonal to every atom, which is exactly the certificate the ZERO
problem looks for. The `t -> 0` counterexample (`-T -> 2I`) and `T_L = 0` are confirmed.

Two remarks for the shard (no error in the lane):

- The proved cutoff is far from sharp: at x = 13 the eleven positions give `r = (1,1,1,1,1,2,2,2,3,4,9)`, `B = 108`,
  against the actual first cutoff 6.
- A matching **lower** bound, valid for every geometry, is one line: the real reflection-commuting Loewner space has
  dimension `2N+1` and contains `I` (`prop:window-kinematic-dimension`). If `2N+1 < m` the atom map has a kernel; if
  `2N+1 = m` it is either non-injective or onto, and then some `delta` has `T(delta) = I > 0`. So a zero cone needs
  `N >= ceil(m/2)`. At x = 13 the first cutoff equals `ceil(m/2)` for every `m = 3..11` (only `m = 2` needs one more);
  this is the whole pattern of the L5 table, including why every odd `m` has a positive definite ray one step earlier.

## L2. Dual pairs, SDP versus LP, conditioning — VALID

Weak duality and the sign correction of the brief are right (`G^T y = -e_k` bounds `+delta_k`). The SDP/LP
distinction, Slater, the optimality of `B_k(I)` for fixed cuts, the positive-spanning criterion (rank `m` plus a
strictly positive null vector), the `2 a_k sum h_i lambda_i` bound, the `eta` bound and the compressed-SDP bound are all
correct; the two diagonal examples of 2.4 are right.

Quantitative test (`scratch_rtp2_lattice_box.py`, `POSSPAN`/`L2BOUND` lines). With `r = m + 1` the null vector of
`G_r^T` is unique; in all seven cases it has one strict sign, so the `m+1` smallest eigendirections already positively
span. The bound `2 a_k sum_i h_i lambda_i` (min-norm `p_k`, `sum h = 1`) is within a factor **1.94–2.25** of the full LP
width at x = 13 and 17, and **2.7–4.0** at x = 25. The cruder `2 a_k lambda_r` is off by `1e13` (x=13, N=20, n=2) to
`1e34` (x=25, N=134, n=2), and `2 lambda_r/eta` is weaker still. So the lane's qualitative answer ("jointly the low
spectrum and the positive-spanning conditioning") is right, and the concrete controlling quantity is
`sum_{i<=m+1} h_i lambda_i` weighted by `a_k`, not `lambda_r` or `eps`. Wording only: "Equivalently put
`eta = ...`" should read "Alternatively": `eta > 0` is equivalent to positive spanning, but the bound `2 lambda_r/eta` is
a different, weaker bound.

## L3. Fixed-window limit — MINOR (mathematics correct; two citation gaps)

3.1 (H-POS + H-PIN ⇒ singleton; converse under eventual compactness and strict feasibility) is correct. 3.2 is correct:
`||T_k|| <= 2` follows from `|C_f(y)| <= ||f||^2`; under H-GAP `H(w* + delta)[f] >= (mu_L - 2||delta||_1)||f||^2`, so the
open `l1`-ball `2||delta||_1 < mu_L` is feasible for the whole window, and `delta = ±(mu_L/2) e_k` (closedness) gives
widths `>= mu_L`. H-PIN is then impossible: `tr(Z T_k) = ±1` forces `tr Z >= 1/2` and each cost `>= mu_L/2`. The
counterexamples (`D = (1/2) delta_0`; `diag(1,1,1/2,...)`) are right. The toy
(`scratch_rtp2_lattice_coercive.py`: `mu = 0.1`, `D = (mu/2) delta_0 + 0.7 e^{-y}`, the eleven x = 13 atoms, N = 10, 40,
120) confirms every step: 400 displacements in the open ball (including all `±mu/2 e_k`) stay feasible; every axis
half-width is `>= mu/||T_k||`; the cheapest eigenvector dual pair costs `0.22 >= mu`. It also shows the ball is not
sharp: the axis half-width of the atom at `log 2` converges to `mu/||T_k|| = 0.0618`, not `mu/2`, and numerically
`||T_k|| -> 2 cos(pi/(ceil(L/y_k)+1))` (agreement `8e-10` at N = 120). A sharper, still trivially proved, statement is
feasibility for `sum_k ||T_k|| |delta_k| < mu_L`.

3.3–3.4, checked with care as asked. (a) CCM `Hilbert1` (mc2arXiv.tex line 567) says verbatim that `E` is a core and
that the lower bound of `QW_lambda` is the limit of the smallest eigenvalue on `E_N`; `thmsmallest` (line 612) gives
discrete spectrum and `lowest` (line 658) an eigenvector at `mu_lambda`. So `eps_N` decreases to an attained `mu_L`.
(b) Under RH the explicit formula (eq. `bombieriexplicit`, line 415) applied to `g = f^* * f` gives
`QW(f,f) = sum_rho m_rho |f~(rho)|^2 >= 0`. The lane does not say why this holds on the core: the `V_n` are discontinuous at
the window edges. It does hold, because CCM's Weil class (lines 401–407) admits finitely many first-kind
discontinuities of `f` and `f'`, and `g = f^* * f` is continuous and piecewise `C^1`; the remark after `lowest`
(line 664) also puts the piecewise smooth functions in the form domain. (c) The passage to the eigenvector by
form-norm approximation, pointwise continuity of `f~(rho)` in window `L^2`, the Jensen count `O(T)` for a nonzero
entire function of exponential type bounded on the line, and `>> T log log T` distinct ordinates under RH
(multiplicity `<= 2 max|S| = O(log T/log log T)` from the jump of `N(t)`) are all correct. Hence under RH
`mu_L > 0` and the ball of 3.2 is nonempty: the argument is sound. (Unconditionally a positive proportion of simple
zeros would also give enough distinct ordinates; RH is needed only for the positivity itself.)

The defects are citations: (i) the explicit-formula class is not cited for the discontinuous core (give CCM lines
401–416); (ii) "Carneiro–Chirre, Section 1.1, equations (1.2)–(1.3)" is inaccurate — in the e-print TeX
(`20161109_Bounding_S_n_R3.tex`) the formula `N(t) = (t/2pi) log(t/2pi) - t/2pi + 7/8 + S(t) + O(1/t)` is an **unnumbered**
display (line 188), (1.2) is Littlewood's `S_n(t) = O(log t/(log log t)^{n+1})` (line 206; use `n = 0`), and (1.3) is the
constant `1/4` of Carneiro–Chandee–Milinovich, which is not needed. The source is not in `refs/`, so no provenance row
can be byte-checked yet.

## L4. Multi-window boxes — VALID (numbers); the lane's open question is now answered

Every number I recomputed agrees with the lane to the printed digits: eps, `lambda_m`, `lambda_{m+1}` (9 cases), LP
widths at n = 2, 6, 12 and the edge (9 of the 10 cases, including `2.328012649e-10`, `8.288468325e-12`, `2.225924060e-14`,
`4.364656164e-8`, `1.459510808e-10`), `r_used`, and `N_sat` = 56, 83, 134 with log dets to 12 digits. Widths are
strictly increasing in n in all nine boxes. The rate arithmetic (3.48128, 0.33496, 5.26603, `-0.19278`, factor 206) is
right. The precision regime is described honestly (ball certificates for fixed dyadic cuts; QR eigenvalues are
floating). The lane's own caveat that the section/LP brackets leave SDP tightness open was correct at the time; the
review closes it at x = 13:

**Full SDP box at x = 13, N = 20** (`scratch_rtp2_lattice_box.py 13 20 sdp`; barrier method, all other ten weights free;
inner and outer bounds agree to 7–8 digits; floating 160-digit arithmetic, not ball-certified):

| n | full SDP width | eigenvector-LP width (lane) | LP/SDP | lane's two-coordinate section |
|---:|---:|---:|---:|---:|
| 2 | 1.232732e-25 | 2.9844301e-25 | 2.421 | 3.557e-34 |
| 3 | 7.347969e-24 | 1.7622612e-23 | 2.398 | 7.418e-33 |
| 4 | 6.403464e-22 | 1.5258776e-21 | 2.383 | 2.345e-31 |
| 5 | 6.027370e-20 | 1.4334700e-19 | 2.378 | 2.880e-29 |
| 6 | 5.733545e-18 | 1.3625264e-17 | 2.376 | 3.223e-27 |
| 7 | 5.424567e-16 | 1.2892586e-15 | 2.377 | 8.639e-25 |
| 8 | 5.188640e-14 | 1.2349640e-13 | 2.380 | 2.146e-22 |
| 9 | 5.270599e-12 | 1.2591968e-11 | 2.389 | 1.478e-19 |
| 10 | 6.284182e-10 | 1.5136547e-9 | 2.409 | 3.977e-17 |
| 11 | 1.087681e-7 | 2.6659994e-7 | 2.451 | 2.891e-13 |
| 12 | 4.902604e-5 | 1.2528657e-4 | 2.556 | 1.408e-8 |

At **N = 40** (`scratch_rtp2_lattice_box.py 13 40 sdp 2,12`, 58 min on 4 cores): n = 2 full SDP width `1.1548047e-36`
against LP `2.3329543e-36` (**LP/SDP = 2.020**); n = 12: `2.1124249e-9` against `4.2494271e-9` (**2.012**). The
N = 56 run (same two coordinates) was stopped unfinished after about an hour (the mpmath barrier scales like `N^3`); no N = 56 SDP number is claimed.

Consequences. (a) The eigenvector LP is tight to a factor ≈ 2.4 at every coordinate; the true admissible set is the LP
box shrunk by that factor, not something 10 orders smaller. (b) The two-coordinate sections, which the lane offers
as the lower half of a bracket, are 8–9 orders below the true widths; they are correct numbers but useless as
brackets (the review-1 axis sections, `3.0e-36` to `2.4e-9`, which the shard still prints, are worse). (c) The LP box
of all m coordinates is the bounding box of **two vertices** in every case where it was tested (`NEEDLE2`: (13,20), (13,56), (13,60), (17,60), (25,60), (25,134)): one vertex gives the
upper endpoint for even n and the lower for odd n, the other the reverse; their components alternate in sign and grow
by a factor ≈ 60–420 per step in n. The SDP endpoints at N = 20 are ≈ 0.39 × (first vertex) and ≈ 0.42 × (second vertex)
coordinatewise. So at this resolution the admissible set is a thin needle through `w*`: positivity fixes the eleven
weights up to essentially **one** direction, and the eleven "widths" are the components of that one segment. The
monotone growth in n is the profile of that direction, which supports the lane's "location, not von Mangoldt weight"
reading. (d) The rate statements of 4.3 are about the LP box; with LP/SDP ≈ 2.4 at N = 20 and ≈ 2.0 at N = 40
they very likely transfer to the true widths at x = 13, but the ratio was not measured at x > 13, so the shard must say
"LP-relaxation width" wherever it quotes 3.48 or 0.335.

## L5. First recession cutoffs at x = 13 — VALID

Reproduced by a different method (`scratch_rtp2_lattice_recession.py`): the reviewer's own barrier SDPs for the RAY
(`max t: T(delta) >= tI, |delta| <= 1`) and ZERO (`max t: Z >= tI, tr Z = 1, Z ⟂ T_k`) problems, witnesses re-verified at 60
digits. Result `2,2,2,3,3,4,4,5,5,6` for m = 2..11, with the same certificate types at the previous cutoff (PD ray at
N = 1 for m = 2, 3 and at `N = (m-1)/2` for odd m; kernel for even m ≥ 4). Margins: ZERO `lambda_min(Z)` 2.03e-8 (m = 10,
N = 5) and 2.08e-9 (m = 11, N = 6); RAY 7.3e-9 (m = 11, N = 5). The lane's point that `sum delta = ±1` misses zero-sum
directions is right. See L1 for the `ceil(m/2)` lower bound that explains the table.

## L6. Comparison protocol — VALID

No zero enters the script, the bridge, the certificates or the review's scripts. L3.4 is a conditional theorem, not a
numerical comparison; it is labelled.

## Numerical checks for the blind lane — VALID

The five certified edge widths, the threshold N = 6 and the slope 3.481279430 (fit 3.481449717) are reproduced
(all five saturation-cutoff edge widths `2.328012649e-10`, `8.288468325e-12`, `2.027492338e-12`, `1.000839753e-13`, `2.225924060e-14` and the n = 2 widths at x = 13 and 25 by the reviewer's own LP). The slope is a slope of the LP
width.

## Further finding: the lattice max-det optimizer is not the truth

`scratch_rtp2_lattice_maxdet.py` (x = 13, N = 20, damped Newton at 160 digits from `w*`, 49 iterations): the unique
optimizer of `prop:rtp-lattice-maxdet` raises log det from −780.432 to −691.256 and `lambda_min` from `1.57e-39` to
`1.31e-27`. Its displacement from truth is `-2.79e-26` (n = 2), `-2.83e-18` (n = 6), `-1.98e-5` (n = 12), alternating in
sign along the needle: 23 %, 49 % and 40 % of the SDP widths. Lattice MaxEnt therefore lands in the interior of the
needle, not on the truth; the lane's "its identity with truth is not established" should become "it is not the
truth (numerically, x = 13, N = 20)".

## Verdict lines

VERDICT L1: VALID

VERDICT L2: VALID

VERDICT L3: MINOR — the proof of 3.4 applies the explicit formula to the discontinuous core functions V_n without citing CCM's Weil class (mc2arXiv.tex lines 401–416, first-kind discontinuities allowed), and "Carneiro–Chirre, Section 1.1, equations (1.2)–(1.3)" is wrong: the N(t) formula is an unnumbered display, (1.2) is Littlewood's bound (use n = 0), (1.3) is not needed, and the source is not in refs/.

VERDICT L4: VALID

VERDICT L5: VALID

VERDICT L6: VALID

VERDICT lem:rtp-lattice-recession: VALID

VERDICT prop:rtp-lattice-maxdet: MINOR — the proposition is correct, but the lane's gloss "its identity with truth is not established" is now decided: at x = 13, N = 20 the max-det optimizer differs from w* by -2.79e-26 (n = 2) to -1.98e-5 (n = 12), 23–49 % of the SDP widths (scratch_rtp2_lattice_maxdet.py); the row should say so.

VERDICT lem:rtp-lattice-width-dual: VALID

VERDICT prop:rtp-lattice-limit-dual-pin: VALID

VERDICT prop:rtp-coercive-window-nonunique: VALID

VERDICT cor:rtp-rh-window-nonunique: MINOR — same citation defects as L3 (explicit formula on the discontinuous core: cite CCM lines 401–416; Carneiro–Chirre equation numbers wrong and source not in refs/); and the companion sentence in "What this changes" ("an open neighborhood of admissible weights, even after imposing nonnegative weights") is false as worded, since w* has zero weights at 6, 10, 12 and lies on the boundary of the orthant.

VERDICT num:rtp2-lattice-widths: MINOR — the numbers are right, but the row must say that the widths and the slopes 3.48 / 0.335 are eigenvector-LP (outer) widths, and should record the review's measured LP/SDP ratio 2.38–2.56 at x = 13, N = 20 and 2.01–2.02 at N = 40 (not measured at x > 13) and the two-vertex needle structure.

VERDICT num:rtp2-lattice-recession: VALID

VERDICT num:rtp2-lattice-sections: MINOR — the sections are correct inner bounds, but "full SDP box tightness OPEN" is superseded: the full SDP widths at x = 13, N = 20 are 1.2327e-25 (n = 2) to 4.9026e-5 (n = 12), 8–9 orders above the sections and a factor 2.4 inside the LP box; the row should either be dropped or carry the SDP widths.

**Tally: 10 VALID, 5 MINOR, 0 INVALID** over 15 ids (L1–L6 and the nine proposed rows).

## Corrections to apply

1. `astra-proofs.md` §2.3, replace "Equivalently put `eta=min_{||d||_2=1} max_i(-g_i.d)>0`;" by "Alternatively, with
   `eta=min_{||d||_2=1} max_i(-g_i.d)`, which is positive exactly when the rows positively span,". Append: "In the seven
   cases computed in the review, `2 a_k sum_i h_i lambda_i` with `r = m+1` is within a factor 1.9–4.0 of the LP width,
   while `2 a_k lambda_r` exceeds it by `1e13` to `1e34`."
2. §3.4, after "The explicit formula under RH writes the form as a nonnegative sum": insert "(the explicit formula
   `bombieriexplicit` holds on CCM's Weil class, mc2arXiv.tex lines 401–416, which allows finitely many first-kind
   discontinuities; `g = f^* * f` for `f in E_N` is continuous and piecewise `C^1`)". Replace "[Carneiro–Chirre, Section 1.1,
   equations (1.2)–(1.3)]" by "Carneiro–Chirre, arXiv:1702.04099, §1.1: the unnumbered display for `N(t)` and
   Littlewood's bound (1.2) with `n = 0`" and fetch the e-print into `refs/src/1702.04099/` before any provenance row.
3. §3.2, optional sharpening after "remains feasible on the whole window": "More precisely `sum_k ||T_k|| |delta_k| < mu_L`
   suffices; numerically `||T_k|| = 2cos(pi/(ceil(L/y_k)+1))` (review, `scratch_rtp2_lattice_coercive.py`)."
4. §4.4 last paragraph, replace "Their large separation leaves the tightness of the full LP relaxation OPEN; a ratio
   between a section and an LP is not a proved relaxation gap for the full SDP." by "The review computed the full SDP
   widths at N = 20 (barrier method with dual certificates, 160 digits, not ball-certified): 1.2327e-25 (n = 2) to
   4.9026e-5 (n = 12), a factor 2.38–2.56 inside the LP widths and 8–9 orders above these sections."
5. "What this changes", `num:rtp-commutant`: replace "Its identity with truth is not established." by "It is not the truth:
   at N = 20 it differs from `w*` by `-2.79e-26` (n = 2) to `-1.98e-5` (n = 12) (review)." Replace "Full SDP widths remain
   bracketed between section lower bounds and LP upper bounds." by "The full SDP widths at N = 20 are 1.2327e-25 to
   4.9026e-5, a factor ≈ 2.4 inside the LP widths; the LP box is the bounding box of two vertices, so the admissible set is
   a needle along one alternating direction." In the shard, delete "the exact axis sections being `3.0e-36` to `2.4e-9`"
   (inner bounds 11 orders too small) in favour of the SDP widths.
6. "What this changes", `obs:rtp-round-1-reading`(iv): replace "the n=2 width contracts at 3.48 digits per unit x, the
   moving edge at 0.335, and eps at 5.27" by "the n=2 eigenvector-LP width contracts at 3.48 digits per unit x, the moving
   edge's at 0.335, and eps at 5.27 (LP/SDP 2.0–2.6 at x = 13, N = 20 and 40, measured only there)". Replace "and an open neighborhood of
   admissible weights, even after imposing nonnegative weights" by "and a neighbourhood of admissible weights (an
   `l1`-ball of radius `mu_L/2`); imposing `w >= 0` still leaves a non-singleton set, although `w*` then lies on the
   boundary of the orthant".
7. L1 text or `lem:rtp-lattice-recession`: add "Conversely no cutoff with `2N+1 <= m` works for any geometry (the Loewner
   space has dimension `2N+1` and contains `I`); at x = 13 the first cutoff is `ceil(m/2)` for `m = 3..11`. The explicit
   `B` is 108 there."

## Recommendation for shard 08j

Register `lem:rtp-lattice-recession` (with the `ceil(m/2)` converse), `prop:rtp-lattice-maxdet` (with the
"not the truth" numerics), `lem:rtp-lattice-width-dual`, `prop:rtp-lattice-limit-dual-pin` and
`prop:rtp-coercive-window-nonunique` as proved; `cor:rtp-rh-window-nonunique` as proved-conditional on RH only after the
Carneiro–Chirre source is in `refs/` with a byte-checked provenance row for the `N(t)` display and Littlewood's bound, and
CCM rows for `Hilbert1`, `lowest` and the Weil-class definition; deps should include `cit:weil-criterion`.
`num:rtp2-lattice-recession` as is. `num:rtp2-lattice-widths` with the LP label on every width and slope, the needle
statement, and the review's SDP table as the x = 13 calibration (proof script `notes/reviews/scratch_rtp2_lattice_box.py`
for those numbers, since the lane's script does not produce them). Drop `num:rtp2-lattice-sections` or merge it into the
widths row as a footnote. The headline for 08j: at x = 13 the admissible lattice set is a needle about 2.4 times shorter
than the LP box, positivity pins the weights up to one direction, lattice MaxEnt does not return the truth, and under RH
no fixed window pins them exactly. The next computation that matters is the LP/SDP ratio at x = 25 (N = 60 at least),
which decides whether the 3.48-digit rate is a property of the admissible set; the barrier code here is too slow in
mpmath for that and should be ported to arb.
