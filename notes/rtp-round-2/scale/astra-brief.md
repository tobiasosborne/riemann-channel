# Brief for lane S (RTP-2, wave 2): the rate at scale. eps_N converged in N at x = 50, the dilation-channel rate to x = 70 and beyond, and the certified comparison with the prolate asymptotic

You are `codex:gpt-6-astra`, a constructive verifier in a mathematical research notebook (git repo, current
directory). Read `notes/rtp-round-2/brief.md` first (game rules, conventions, output protocol; binding). Then read:
`notes/rtp-round-1/lane-A1.md` (section 0; A1.2 axis N; the certified `eps_N`), the review
`notes/reviews/rtp-round-1-2026-09-24.md` items C2 (defect 4: `eps_N` not converged in `N` at `x = 50`, `N = 360`:
6.59e-257 at 352, 2.27e-257 at 360, 3.31e-258 at 400, 2.81e-258 at 420) and C12(iii) (slopes 5.346 (13→25), 5.397
(25→50), 5.379 (13→50) against the prolate asymptotic 5.386 and the bare 5.458; `scratch_rtp1_prolate.py`,
`scratch_rtp1_tail.py`), `zst/tools/rtp1_a1.c` and `rtp1_a1_run.sh`, `zst/README.md`, `notes/zeta-spectral-triples/plan.md`
(section on M4 scale: OpenMP, displacement structure; the prolate heuristic in section 1), and
`refs/src/2511.22755/mc2arXiv.tex` section 7 (the asymptotic `1 - chi_4(lambda)`; quote it by line). Write only
`notes/rtp-round-2/scale/astra-proofs.md`, `progress.txt`, `checks/`, `zst/tools/rtp2_scale.c` (if `rtp1_a1.c` is not
enough; a thin wrapper or new modes are fine), `zst/tools/rtp2_scale_run.sh`, a `zst/Makefile` rule (not in `all`),
`outputs/rtp2_scale_*.txt`. You MAY add OpenMP parallelism to the driver only (not to `zst/src/`), or a faster
certified LDL^T in the driver; `make -C zst check` must pass. Do not run git. FLINT 3 installed; 64 cores; 62 GB RAM.

## 0. The question

The dilation channel's rate is the one number that decides whether the CCM window learns the zeros at the
prolate (kinematic) rate or at an arithmetic one. Round 1 has three points (`x = 13, 25, 50`), the last not converged in
`N`, and slopes that straddle the prolate asymptotic. Deliver: (i) `eps_N(x = 50)` converged in `N` (certified, to
the point where the next 40 modes change it by less than 1%); (ii) `eps_N` at saturated `N` for `x = 60` and `x = 70`
(and `x = 85`, `x = 100` if the stack allows within about two hours on 64 cores; report wall times); (iii) the
slopes between consecutive points and the fit against the prolate asymptotic, with the prefactor; (iv) the
first-zero error at the same points (COMPARISON STEP, labelled) and its ratio to `eps`.

## 1. Before running: the cost model and the precision

S1. From `rtp1_a1.c`'s timings (stderr) and the review's `N = 420` run, estimate the cost of the even-block
certified minimal eigenvalue at `(x, N, prec) = (50, 520, 4200)`, `(60, 650, 5200)`, `(70, 800, 6200)`, `(100, 1300, 9000)`
(precision must exceed the digits of `eps`: `eps ~ 10^{-5.4 x}`, so `prec >= 3.33 * 5.4 x + margin` bits; say the
margin you use and why). Decide the plan (which points, which `N` sweep) and write it down with the estimate before
running. If the `O(N^3)` ball LDL^T at thousands of bits is the bottleneck, consider computing `eps_N` for a sparse set
of `N` (every 40) rather than the full pivot sequence, and using `zst_eigmin` (Rump) only at the end points.

S2. Convergence criterion in `N`: `eps_N` decreases in `N` (principal submatrices; prove the monotonicity in one line
and use it); call `eps` converged at `N` when `eps_{N} / eps_{N+40} < 1.01`. Report the `N` at which this happens for
`x = 13, 25, 50` (round-1 data plus your runs) and the ratio `N_conv / (x log x)`.

## 2. Runs

S3. `x = 50`: `N = 420, 460, 500, 540, ...` until converged (S2), certified. `x = 60, 70`: axis N to convergence (start
at `1.7 x log x` and go up). `x = 85` and `x = 100`: attempt if S1 says under about an hour each; otherwise report the
estimate and stop. Also, at every `x`, the archimedean-plus-pole control's inertia (no primes) at the final `N`.
Output byte-reproducible; timings to stderr and copied into the report as floating numbers.

S4. Comparison step (zeros; labelled): `|z_1 - gamma_1|` at the final `(x, N)` of each `x` (the secular-root pipeline
as in `rtp1_a1.c`); report the ratio to `eps` and its trend.

## 3. Analysis

S5. Slopes (digits per unit `x`) between consecutive `x`, the least-squares slope over all points, and the fit
`log10 eps = -a x + b log10 x + c` (the prolate asymptotic has `a = 4 pi / log 10 = 5.458`, a polynomial prefactor
`lambda^9 = x^{4.5}`: quote the exact form from the source and fit with the prefactor fixed, then free). Report
whether the converged data are consistent with the prolate asymptotic (same `a`, prefactor ratio constant in `x`,
as the review found `12.7` and `14.4` at `x = 13, 25`) or drift from it. Also the eigenvector: the overlap of the
minimal even eigenvector at consecutive `x` after rescaling to the common window, if that is defined in the
formula sheet; otherwise skip and say so.

S6. Verdict on the rate: kinematic (prolate) or not, at the precision reached; and the one number a further round
would need.

## 4. Output format

`notes/rtp-round-2/scale/astra-proofs.md`: ledger; S1 plan and cost model; S2 monotonicity and the convergence
table; S3–S4 tables (every printed digit certified unless labelled floating); S5 fits; S6 verdict; "Numerical
checks for the blind lane" (`eps` at `x = 50` converged, at `x = 60`, at `x = 70`, with `N` and prec; one slope);
"What this changes in the notebook" (`num:rtp-dilation-channel`(b) update; `obs:rtp-round-1-reading`(iii);
candidate rows; next step). Write incrementally; `progress.txt` lines S1..S6.
