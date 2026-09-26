# Brief for lane D (RTP-2): the discriminating experiment. A real Dirichlet L(s, chi) through the dilation-window pipeline: is the e^{-4 pi x} learning rate zeta's or the window's?

You are `codex:gpt-6-astra`, a prover and constructive verifier in a mathematical research notebook (git repo,
current directory). Read `notes/rtp-round-2/brief.md` first (game rules, conventions, output protocol; binding).
Then read, in this order: `notes/rtp-round-1/lane-A1.md` (the round-1 protocol you are repeating for another
L-function; its lemma A1.1' and the two protocols "axis N" and "axis x"), `zst/tools/rtp1_a1.c` (the driver you
adapt; read it fully), `zst/include/zst.h` (the `zst_weil_t` data model, `zst_weil_dirichlet`, `zst_weil_ab`,
`zst_block_min`, `zst_parity`-type functions, `zst_eigmin`, `zst_certify_even_simple`), `zst/tools/zst.c` (how
`--chi D` is wired, and how the reference zeros of `L(s, chi_D)` are read from `tests/data/dirichlet_ref.txt` for the
comparison step), `zst/README.md` (MVP-3 section), `notes/zeta-spectral-triples/ellcurve/report-ell.md` (what is
known about `chi_{-4}` through this stack), and the review `notes/reviews/rtp-round-1-2026-09-24.md`, item C12(iii)
(the prolate asymptotic, the measured 5.38 digits per unit of `x`). Everything you write goes to
`notes/rtp-round-2/dirichlet/astra-proofs.md` (your report), `notes/rtp-round-2/dirichlet/progress.txt`,
`notes/rtp-round-2/dirichlet/checks/` (scratch), the new driver `zst/tools/rtp2_dirichlet.c`, its run script
`zst/tools/rtp2_dirichlet_run.sh`, a build rule `build/rtp2_dirichlet` in `zst/Makefile` (NOT part of `all`; model it
on `build/rtp1_a1`), and outputs `outputs/rtp2_dirichlet_*.txt`. Do not change `zst/src/` or `zst/include/`
behaviour (`make -C zst check` must still pass). Do not run git. python3 with numpy, mpmath, scipy, sympy is
available; FLINT 3 with arb is installed system-wide; `zst/build/libzst.a` is already built; 64 cores.

## 0. The question

Round 1 measured, for zeta, that the certified minimal even eigenvalue `eps_N(x)` of the window form and the
first-zero error fall together at 5.38 decimal digits per unit of `x` (13 to 50), against the CCM prolate
asymptotic 5.39 and the bare `4 pi / log 10 = 5.46`; the kinematic Schur envelope does not decay at that rate. It
could not decide whether the rate is set by the prolate concentration of the window (kinematic) or by zeta's
primes (arithmetic). The discriminating experiment: run **the same pipeline on `L(s, chi)` for real primitive
characters** (no pole, a different prime comb `-chi(p^m) log p / p^{m/2}`, gamma factor `Gamma_R(s + kappa)`):

- if the rate (digits per unit of `x` at saturated `N`) is the same for every `chi` and for zeta, the rate is
  the window's (kinematic), and the primes only set the floor;
- if it differs, say how (with conductor? with parity `kappa`? with the first zero's height?).

## 1. Prediction first (theory; write it before you run anything)

D1. Work out what the CCM prolate heuristic predicts for `L(s, chi)`. In the paper (`refs/src/2511.22755/mc2arXiv.tex`,
section 7 and the review's C12(iii)) the rate comes from the concentration defect of prolate functions on the
window, `1 - chi_4(lambda) ~ (2^14/3) sqrt2 pi^5 lambda^9 e^{-4 pi lambda^2}` (as quoted in the review; check the
exponent and the polynomial prefactor against the source and say what you find). State, as a labelled
prediction, whether and why that asymptotic should be independent of the L-function (the same window, the same
Fourier basis; the archimedean kernel `rho_{d, mu}` differs only by `mu = kappa + 1/2`), and what prefactor
differences the conductor `log |D|` and the parity could introduce. Also predict the saturation scale `N_sat`
(round 1: `~1.7 x log x` for zeta, a Weyl-count scale): the Weyl law of `L(s, chi)` has the same leading term
with `log(|D| T / 2 pi e)`, so predict how `N_sat` shifts with `|D|`.

D2. State the exact analogue of lane A1's lemma A1.1' for a form without pole terms (nothing changes in the
algebra; say so, or say what does), and note that the trivial set of `L(s, chi)` is empty (no `+-1/2` pole
directions), which changes the kinematic control: the "pole plus archimedean" control of round 1 becomes
"archimedean only", which round 1 found indefinite for zeta's window. Predict the inertia of the archimedean-only
form on the window as a function of `N` and `kappa` if you can, otherwise measure it (item D4).

## 2. The driver (constructive)

D3. Write `zst/tools/rtp2_dirichlet.c` by adapting `rtp1_a1.c`: replace `zst_riemann_ab(a, b, N, x, X, prec)` by
`zst_weil_dirichlet(&W, D, x, X, prec); zst_weil_ab(a, b, N, &W, prec)`, keep the two modes `--mode axisN` and
`--mode axisx` (with `--fixedL 1`), add `--D <fundamental discriminant>`. Comparison step: the low zeros of
`L(s, chi_D)` from `tests/data/dirichlet_ref.txt` (as `zst.c` reads them; if a discriminant you need is absent,
generate its reference zeros in a labelled `checks/` script with `mpmath` root isolation of the Hardy Z function,
or with `acb_dirichlet_hardy_z` in a small C program, and add them to the file in the same format, saying so).
**Parity.** `L(s, chi)` may have its global minimum in the odd block (round 1 of `zst` found this for 37a1 and
389a1). Certify per case which block carries the minimum (`zst_block_min` on both blocks; the parity function in
`zst/src/parity.c`) and report `eps_N` for **both** blocks; the first-zero comparison is against the block that
carries the minimum. If the minimum is odd, say so and still report the rates.
Byte-reproducible output (no timings, no addresses; timings to stderr). Print a `checks:` line as `rtp1_a1.c` does.

D4. Runs (`zst/tools/rtp2_dirichlet_run.sh`, parallel jobs as `rtp1_a1_run.sh`; keep total wall time under
about 90 minutes on 64 cores; start with the cheap ones and write results as they finish):
- characters: `D = -4, -3, 5, 8, -7, 12` at least (three even, three odd; conductors 3 to 12); add `D = -20, 21, 13`
  if affordable;
- axis N at `x = 13` (`Nmax` about 200) and `x = 25` (`Nmax` about 260) for every `D`; at `x = 50` (`Nmax` about
  420, `prec` 4200) for `D = -4` and `D = 5` at least;
- axis x (CCM protocol, window and primes grow together) at `N = 60` to `x = 50` and `N = 120` to `x = 25` for
  every `D`; the fixed-`L` (partial-information) protocol at `N = 60` for `D = -4` and `D = 5`;
- the archimedean-only control (cutoff `X = 1`, no primes) alongside, as `rtp1_a1.c` does for pole plus archimedean.
Precision: follow `rtp1_a1_run.sh` (1000 bits at `x = 13`, 1800 at `x = 25`, 4200 at `x = 50`); if a certificate
fails, raise it and say so.

## 3. What to extract (analysis; a `checks/summary.py` in the style of `rtp1_a1_summary.py`)

D5. For every `D`: `N_sat(x)` (argmin of `log det`, full window and each block), `eps_N(x)` at saturated `N`,
the slope in decimal digits per unit of `x` between 13 and 25, 25 and 50, 13 and 50 (where run), the same for
`|z_1 - gamma_1|` (labelled COMPARISON), the ratio `|z_1 - gamma_1| / eps_N`, the Rayleigh decomposition of `eps` into
archimedean and prime terms at the final `x`, the structured interval half-width for the next datum (the Schur
envelope), and the inertia of the archimedean-only control. Put zeta's round-1 numbers in the same table
(`outputs/rtp1_a1_*.txt`; do not rerun zeta).

D6. Verdict on the question of section 0, with the evidence: is the rate `chi`-independent to the precision
you have (state the spread across `D` in digits per unit `x`), does it match the prolate asymptotic, and how do
`N_sat` and the prefactor depend on `|D|` and `kappa`? Compare with your predictions D1 and record every
discrepancy in the correction ledger. If the rate is the same to within the spread, say plainly that the
`e^{-4 pi x}` law is kinematic and that the arithmetic content of the dilation channel is the floor, not the
rate; if not, say what differs and offer the simplest explanation consistent with the data.

## 4. Output format

`notes/rtp-round-2/dirichlet/astra-proofs.md`: ledger; D1–D2 as labelled statements with proofs or predictions;
D3 as a precise description of the driver (options, what is certified, what is floating); D4 run table; D5
results tables (every printed digit certified unless a column is labelled floating); D6 verdict; "Numerical
checks for the blind lane" (the numbers a reviewer must reproduce: `eps_N` at three `(D, x, N)` triples, one
`N_sat`, one slope, one inertia count); "What this changes in the notebook" (which round-1 statements in shard
08i, `obs:rtp-round-1-reading`(iii) in particular, are confirmed, sharpened or refuted, and the one next
experiment). Write incrementally; update `progress.txt` (D1..D6) as you go.
