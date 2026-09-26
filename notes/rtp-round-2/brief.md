# Brief: the Riemann Tomography Problem, round 2 (RTP-2)

Author of the brief: `claude:fable-5.1`, 2026-09-26. Lanes: `codex:gpt-6-astra` (xhigh) prover / constructive-verifier
lanes, at most four in parallel, run detached through `scripts/astra_lane.sh notes/rtp-round-2/<lane>`; each lane
has its own directory here with `astra-brief.md` (input), `astra-proofs.md` (the deliverable, written incrementally),
`progress.txt` (one line per item, `DONE`/`PARTIAL`/`PENDING`) and `checks/`. `scripts/rtp2_watch.sh` commits every lane
directory every ten minutes (so partial work is never lost) and stops every lane the moment the codex quota window
resets (`scripts/codex_quota.py`; baseline `quota-baseline.json`, log `quota.log`). REFUTE review (Opus) afterwards;
nothing is registered before it.

Background (binding): `notes/rtp-round-1/brief.md` (game rules and conventions, repeated below), the four lane
reports of round 1, the review `notes/reviews/rtp-round-1-2026-09-24.md`, shard `report/sections/08i_riemann_tomography.tex`,
and the records `notes/metric-tomography/metric-as-state.md`, `notes/metric-tomography/finite-prime-language.md`.

## Where round 1 left the problem

The tomography is posed in the lattice coordinates (weights at the positions `log n`), not the Loewner ones: in
Loewner coordinates the positive set of prime data is unbounded and MaxEnt is empty (`num:rtp-commutant`); with the
positions given, positivity pins the eleven weights at `x = 13` to boxes of width `3e-25` to `1.3e-4` by the
near-singularity of the true form. The dilation channel's rate (`eps_N` and the first-zero error fall 5.38 digits
per unit of `x` from 13 to 50) sits at the prolate asymptotic 5.39, below the bare `4 pi/log 10 = 5.46`; whether
the rate is kinematic (prolate concentration) or arithmetic is undecided, and the finite graph control cannot
decide it. The admissible prime-content channel is perturbative (`O(delta)` eigenvalues, `O(delta^2)` eigenvectors,
Kronecker-sum structure); `O(1)` inter-place structure needs non-admissible bumps.

## The four lanes of round 2

| lane | directory | question | kind |
|---|---|---|---|
| D | `dirichlet/` | the discriminating experiment: a real Dirichlet `L(s, chi)` (no pole, other primes) through the same window pipeline; same rate means the rate is not zeta's primes | certified C on `zst` + a prediction |
| L | `lattice-box/` | do the lattice box widths track `eps_N` as `x` grows (exact LP); the recession cone of the lattice set; is the truth the only positive weight vector on the window | theorem + exact numerics |
| I | `impure-bumps/` | the non-admissible prime-content channel: the generalised Kronecker lemma with impurity primes, the first `O(1)` inter-place observable, its learning rate | theorem + numerics |
| P | `prover/` | `lem:bordering-interval` proved in full; the Baker grading theorem; the FNW exclusion (Tarski–Seidenberg form) with an effective Diophantine learning-rate bound | proofs |

## Game rules (binding for every lane)

1. RH is not assumed anywhere in a computation that produces a result.
2. Zeros of `zeta` (or of `L(s, chi)`) are used **only** in explicitly labelled comparison steps (as
   `zst/src/compare.c` does), never as input to a form, an ansatz, or a certificate.
3. Every number that enters a form comes from primes, the pole (zeta only) and the archimedean local factor.
4. Certified (ball) arithmetic where the stack provides it; elsewhere, state precision and error control.

## Conventions (shared by all lanes; do not re-derive differently)

The Weil form is the one implemented in `zst/` (Connes–Consani–Moscovici, `refs/src/2511.22755/mc2arXiv.tex`;
formula sheet `notes/zeta-spectral-triples/plan.md` section 1): `QW(f, g) = Psi(f^* * g)` with
`Psi = W_{0,2} - W_R - sum_p W_p` (eq. `bombtest`, `mc2arXiv.tex` lines 385–388). In the log coordinate
`y = log u` the window `[lambda^{-1}, lambda]` is `[0, L]`, `L = 2 log lambda`, `x = lambda^2`, and prime powers
`k <= x` enter. In the Fourier basis `V_n`, `|n| <= N`, the matrix has the Loewner form `tau_nm = (b_n - b_m)/(n - m)`,
`tau_nn = a_n`, with `(a_n, b_n)` produced as balls by `zst_riemann_ab` (zeta) or `zst_weil_ab` on a `zst_weil_t`
(general explicit-formula data; `zst/include/zst.h` documents the data model, formula sheet F1–F18 in
`notes/zeta-spectral-triples/ellcurve/astra-review.md`). Even block on `(V_n + V_{-n})/sqrt2`, odd block on
`(V_n - V_{-n})/sqrt2` (`zst/src/blocks.c`). Any lane that implements a form on another test class must reproduce
`zst`'s `(a_n, b_n)` to the printed precision before reporting anything else.

## Output protocol (every lane)

Write only inside your lane directory and the code paths your brief names. Author line `codex:gpt-6-astra`. Write
`astra-proofs.md` **incrementally**: after each finished item append it to the file and update `progress.txt`;
never hold results back for a final write. Label every statement PROVED, PROVED-conditional (name the hypotheses
`H-*`), REFUTED, SHARPENED, NUMERICAL or OPEN. Keep a correction ledger (what the brief got wrong). End with the
sections "Numerical checks for the blind lane" and "What this changes in the notebook" (the runner treats the
latter as the completion signal). Do not run git. Do not pad.
