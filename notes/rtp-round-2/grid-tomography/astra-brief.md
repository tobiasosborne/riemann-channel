# Brief for lane G (RTP-2, wave 2): grid tomography. Does Weil positivity on a window recover the PRIME POSITIONS, not only the weights? The window form with a free nonnegative measure on a fine grid

You are `codex:gpt-6-astra`, a prover and constructive verifier in a mathematical research notebook (git repo,
current directory). Read `notes/rtp-round-2/brief.md` first (game rules, conventions, output protocol; binding).
Then read: `notes/rtp-round-2/lattice-box/astra-proofs.md` and `progress.txt` (lane L: recession cone, box widths,
the `N -> oo` pinning statement; whatever state it is in, build on it and say what you took), `notes/rtp-round-1/lane-B2.md`
sections 2 and 4 (the positive set of prime data; the lattice box on `log n`, `n = 2..12`, where the weights at the
composites 6, 10, 12 were pinned to 0 to `1e-10`–`1e-3`), `scripts/rtp1_commutant.py` (reading `(a_n, b_n)` from
`zst` through a compiled C printer; the split pole / archimedean / prime with the cutoff argument), shard
`report/sections/08i_riemann_tomography.tex` (`num:rtp-commutant`, `obs:rtp-round-1-reading`(iv)), and
`notes/metric-tomography/metric-as-state.md` sections 2, 3, 7. Write only `notes/rtp-round-2/grid-tomography/astra-proofs.md`,
`progress.txt`, `checks/`, `scripts/rtp2_grid_tomography.py`, `outputs/rtp2_grid_tomography.txt`. Do not modify
`zst/`. Do not run git. python3 with numpy, mpmath, scipy (HiGHS LP through `scipy.optimize.linprog`), sympy,
`fractions`; 64 cores.

## 0. The question

Round 1 kept the positions `log n` and freed the weights; positivity pinned them, including the zeros at the
composites. The real tomography problem does not know the positions. Put a **free nonnegative measure on a fine grid**
of the window, `D_p = -sum_j w_j delta(y - y_j)`, `y_j = j h`, `j = 1..J`, `w_j >= 0` (the prime side of the explicit
formula is a positive measure: this sign constraint is arithmetic knowledge of the crudest kind, state it as
hypothesis `H-SIGN` and also run without it), and ask: given the pole and the archimedean data exactly, the window
`[0, L]` with `L = log x`, and Weil positivity of the window form on modes `|n| <= N`, what does the admissible set of
`w` look like? Does it concentrate on the prime powers? How does the resolution `h` interact with `N` (a grid finer
than the Fourier resolution `L/(2N)` cannot be resolved; say what the right relation is)? This is the tomography
problem in the coordinates it should be posed in.

## 1. Theory (prove or correct)

G1. The admissible set `P = {w in R^J_(>=0) : H0 + T(w) >= 0}` is a closed convex spectrahedron. Prove or refute:
(i) with `H-SIGN`, `P` is bounded for every `N >= 1` (hint: the trace or the `(0,0)` entry of `T(w)` is a fixed-sign
linear functional of `w` when `w >= 0`; find the cheapest such functional and the resulting bound
`sum_j c_j w_j <= C(H0)`); (ii) without `H-SIGN`, boundedness needs the recession cone of lane L (L1), and on a grid
with `J > 2N + 1` points the map `w -> T(w)` has a kernel (dimension count: `T(w)` lives in the `2N+1`-dimensional
kinematic space of `prop:window-kinematic-dimension`), so the admissible set contains an affine subspace of
dimension at least `J - 2N - 1` and can pin nothing along it; the boxes are then determined by the projection onto
the kinematic space only. State the exact statement: **what positivity plus the window can determine about a
measure is exactly its `2N+1` Loewner moments** (the data `(a_n, b_n)`), and the measure is recovered only through
those moments plus the sign constraint and the near-singularity. Make this precise and prove it.

G2. The true measure has atoms at `log p^m`, weights `Lambda(n)/sqrt n`. Prove the moment-matching statement: two
nonnegative measures on `[0, L]` with the same `2N+1` Loewner moments give the same window form, so the set `P`
contains, together with the truth, every nonnegative measure with the truth's moments; characterise that set
(a moment problem on the interval: the truth is an extreme point iff ... ; Carathéodory bound on the number of
atoms `<= N + 1` or so; the truth has `pi(x) + (prime powers)` atoms, compare with `N_sat`). Say when the truth is
the unique nonnegative measure with its moments (it never is for a finite moment set unless it is a Carathéodory
extreme point; decide whether it is) and what "positivity pins the primes" can then mean at best: pinning of the
moments, plus sparsity.

G3. Sparsity. Prove or refute: if the positivity constraint is tight (the true form is near-singular with `r`
near-zero eigen-directions), the admissible measures are forced to be supported near the zeros of the
nonnegative trigonometric polynomials `q_v(y)` attached to the near-kernel vectors `v` (the atoms must sit where
`q_v` is small); hence the near-kernel of the true form knows the positions. Make this the theorem: positions are
recovered from the near-kernel `{q_v}`, weights from the moments. Check it numerically (G5).

## 2. Numerics (`scripts/rtp2_grid_tomography.py`; deterministic, `check(cond, msg)` as in `scripts/gl1_bond.py`,
no timestamps; `outputs/rtp2_grid_tomography.txt`)

G4. `x = 13`, `L = log 13`. Grids: `h = L/64`, `L/128`, `L/256` (`J = 63, 127, 255` interior points; report also a grid
that contains the exact `log n` as a subset if you can construct one, e.g. the union of the fine grid and the eleven
`log n`). `N = 20, 40, 60`. With `H-SIGN`: (a) the box of each `w_j` (LP over the eigenvectors of `H_true` as lane
B2/L, re-verified at 100 digits; and the exact SDP section for a few `j` by bisection with a 100-digit inertia
test); (b) the total mass `sum w_j` bounds; (c) the minimal-norm and the maximum-entropy (`sum w log w` or log-det)
admissible measures and their distance to the truth's histogram on the grid; (d) plot data (tables) of the box
upper bounds `w_j^+` against `y_j`: do they peak at `log 2, log 3, log 4, log 5, log 7, log 8, log 9, log 11` and
vanish elsewhere? Quantify: the mass allowed within `h` of a prime power against the mass allowed elsewhere.
Without `H-SIGN`: the same at `N = 20` on the `L/64` grid (expect unboundedness along the kernel; measure the
box widths along the kinematic projection instead).

G5. The near-kernel test of G3: for the `r` smallest eigenvectors `v_i` of `H_true` at `N = 60`, tabulate `q_{v_i}(y)`
on the fine grid and its zeros/minima against the prime-power positions; report the correlation.

G6. `x = 25` at `N = 60` and `N = 134` on the `L/128` grid with `H-SIGN` (boxes and peak/elsewhere mass ratio), to see
how the position resolution improves with the window.

## 3. Output format

`notes/rtp-round-2/grid-tomography/astra-proofs.md`: ledger; G1–G3 theorems with proofs (hypotheses `H-*`; PROVED /
PROVED-conditional / REFUTED / SHARPENED / OPEN); G4–G6 tables with precision regimes; "Numerical checks for the
blind lane" (three box bounds, one mass ratio, one near-kernel zero); "What this changes in the notebook" (what the
tomography problem is, precisely, after this lane: moments plus sign plus near-kernel; candidate claim rows for
shard 08j; the next experiment). Write incrementally; `progress.txt` lines G1..G6.
