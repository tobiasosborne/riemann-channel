# Brief for lane E (RTP-2, wave 2): the weight-two discriminating experiment. L(E, s) for E/Q through the dilation-window pipeline: the learning rate, the window scale, and H-RATE

You are `codex:gpt-6-astra`, a prover and constructive verifier in a mathematical research notebook (git repo,
current directory). Read `notes/rtp-round-2/brief.md` first (game rules, conventions, output protocol; binding).
Then read: `notes/rtp-round-2/dirichlet/astra-proofs.md` and `notes/rtp-round-2/dirichlet/progress.txt` (lane D, the
same experiment for Dirichlet characters; whatever state it is in, reuse its driver `zst/tools/rtp2_dirichlet.c`
and its findings; if it is unfinished, say what you took and what you did not), `notes/rtp-round-1/lane-A1.md`
(round-1 protocol, lemma A1.1'), `zst/tools/rtp1_a1.c`, `zst/include/zst.h` (`zst_weil_ellcurve`, `zst_ell_ref`,
`zst_weil_ab`, `zst_block_min`, parity), `zst/tools/zst.c` (`--curve <label>`), `zst/tests/data/ell_ref.txt` (the
curves with reference data: 11a1, 14a1, 37a1, 389a1 at least; PARI ground truth), and
`notes/zeta-spectral-triples/ellcurve/report-ell.md` section 3 (**item 2: from `x = 13` to 30, 11a1 gains 5 digits
where zeta gained about 92; the natural window scale for weight 2 is conjectured to be `sqrt(x/C_E)` (Mellin kernel
`e^{-2 pi u/sqrt C_E}`) rather than `x`; H-RATE, open**; item 1: rank-positive curves have an ODD global minimum,
the construction is inapplicable; item 3: the conductor enters only through the atoms and an identity shift).
Write only `notes/rtp-round-2/ellcurve/astra-proofs.md`, `progress.txt`, `checks/`, the driver
`zst/tools/rtp2_ellcurve.c` (or a `--curve` option added to `rtp2_dirichlet.c` if lane D's driver exists and that is
cleaner; say which), its run script `zst/tools/rtp2_ellcurve_run.sh`, a `zst/Makefile` build rule (not in `all`), and
`outputs/rtp2_ellcurve_*.txt`. Do not change `zst/src/` or `zst/include/` behaviour (`make -C zst check` must pass).
Do not run git. FLINT 3 is installed; `zst/build/libzst.a` is built; 64 cores; python3 with numpy, mpmath, scipy.

## 0. The question

Round 1 and lane D ask whether the dilation channel's rate (`eps_N` and the first-zero error in decimal digits per
unit of `x` at saturated `N`; zeta: 5.38 from `x = 13` to 50, the CCM prolate asymptotic 5.39) is kinematic or
arithmetic. The weight-two case is the sharpest control available: `L(E, s)` has gamma factor `Gamma_C(s + 1/2)`
(`(Q, d, mu) = (1/(2 pi), 1, 1)` in the data model), no pole, conductor `C_E`, and atoms at the same positions
`log p^m` as zeta with weights `-(alpha_p^m + beta_p^m) log p / p^{m/2}` (F4/F5). MVP-3 saw 11a1 crawl (5 digits over
17 units of `x`) while zeta raced. Decide: (i) what the rate of `L(E, s)` is on the axes of round 1, (ii) whether
`sqrt(x / C_E)` is the right variable (H-RATE), (iii) what this says about the zeta rate (if the same window gives
wildly different rates, the rate is not kinematic in the window alone; find what it is kinematic in).

## 1. Prediction first (theory)

E1. State what the prolate heuristic of CCM predicts for `L(E, s)`: the window is the same, the Fourier basis the
same, the archimedean kernel `rho_{1,1}(y) = e^{-y}/(1 - e^{-y})` differs from zeta's `rho_{2, 1/2}`. Derive the
analogue of the `e^{-4 pi x}` law if the heuristic transfers, and the analogue if H-RATE is right (the argument in
report-ell.md: the Mellin kernel of `Gamma_C` decays like `e^{-2 pi u / sqrt C_E}` against zeta's theta kernel
`e^{-pi u^2}`; make this precise: which kernel, which variable, and what "window scale" means for the rate in
`x`). Give two labelled predictions, one per hypothesis, in digits per unit of `x` (or per unit of `sqrt x`).

E2. Predict `N_sat` for weight two from the Weyl law of `L(E, s)` (`N(T) ~ (T/pi) log(sqrt(C_E) T / 2 pi e)`, i.e.
twice zeta's density): the saturation scale should be about `2 x log x` or larger; say what you expect.

## 2. Runs (constructive)

E3. Driver as for lane D with `zst_weil_ellcurve` and the reference zeros from `zst_ell_ref` (COMPARISON STEP only).
Certify the parity of the minimum per case (rank-zero curves 11a1, 14a1 should be even; report what you find) and
report both blocks. Curves: 11a1 and 14a1 (rank 0); 37a1 for the odd-minimum record only (no first-zero comparison
is possible; report `eps` of both blocks and say so); add 15a1, 17a1, 19a1, 20a1, 21a1 if you can supply reference
data for them (extend `tests/data/ell_ref.txt` with PARI via `zst/tools/pari_ref.py` if cypari2 is available, else
with mpmath/`acb_dirichlet`-free means and say how; if you cannot, skip them). Axis N at `x = 13, 25, 50` (as
lane D); axis x (CCM protocol) at `N = 60` to `x = 50` and `N = 120` to `x = 25`; the archimedean-only control;
additionally axis x at `N = 200` to `x = 100` for 11a1 if the wall time allows (the crawl needs a long `x` range to
measure a slope). Keep the total under about 90 minutes on 64 cores; precision as lane D / `rtp1_a1_run.sh`,
raised if a certificate fails.

## 3. Analysis and verdict

E4. Tables as lane D (`N_sat`, `eps_N`, slopes in digits per unit `x` and per unit `sqrt x`, first-zero error and
its ratio to `eps`, Rayleigh decomposition, Schur envelope, archimedean-only inertia), with zeta (round 1) and the
Dirichlet characters (lane D, if available) in the same table. Fit `log10 eps` against `x`, against `sqrt x`, and
against `sqrt(x / C_E)` for the two rank-zero curves and say which variable linearises the data (with residuals).

E5. Verdict on H-RATE and on the question of section 0. If the elliptic rate is set by `sqrt(x / C_E)` while
zeta's is set by `x`, state precisely what in the explicit formula makes the difference (the archimedean kernel
`rho_{1,1}` versus `rho_{2,1/2}`; the density of atoms `2 log p` versus `log p`; the absence of the pole), by
computing the archimedean-only forms' spectra and the prime-only Rayleigh quotients side by side. Record every
discrepancy with E1/E2 in the correction ledger.

## 4. Output format

`notes/rtp-round-2/ellcurve/astra-proofs.md`: ledger; E1–E2 predictions; E3 driver description and run table; E4
tables; E5 verdict; "Numerical checks for the blind lane" (`eps_N` at three `(curve, x, N)` triples, one `N_sat`,
one slope, one inertia); "What this changes in the notebook" (H-RATE status; what `obs:rtp-round-1-reading`(iii)
becomes; candidate claim rows; next experiment). Write incrementally; `progress.txt` lines E1..E5.
