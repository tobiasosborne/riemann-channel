# Brief for the prover: a certified enclosure of the level-one Sonine evaluator Gram at three zeros, closing obs:sonine-enclosure-open. Rigorous bounds on the resolvent scheme, a proof that the phases E_*^#/E_* at the first three zeros are distinct, and a proof that the prescribed evaluator dynamics is not even a contraction

You are the prover in a mathematical research notebook (git repo, current directory). Author line for
everything you write: `codex:gpt-6-astra`. Write ONLY the file `notes/sonine-enclosure/astra-proofs.md` (create
it; overwrite if present) and, if you want scratch computations, python files under
`notes/sonine-enclosure/checks/`. Do not edit anything else. Do not run git. python3 with mpmath (which has
interval arithmetic `mpmath.iv`), numpy, sympy, scipy is installed. Read first:

1. `notes/h-theta-1/astra-proofs.md` (this morning's lane; binding): T3 (the augmented cosine space `L_1`, the de
   Branges space `p M_f`, the kernel formula (10), the variable (11), the reality of the critical-line Gram (14)),
   **T4 §3 (the compact-resolvent scheme (17)–(21))**: `P` restriction to `(0,1)`, `Q = P - |1><1|`, `T = Q C Q` on
   `L^2_0(0,1)` (compact, `||T|| < 1`), `q_s`, `r_s = Q C q_s`, the bilinear kernel `H(s,t) = 1/((1-s)(1-t)) + 1/(s+t-1)
   - int r_s (I - T^2)^{-1} r_t`, the continuation (18) with `chi(s)`, the anchor `t = 2`, `F(s) = p(s)p(2)m(s)m(2)H(s,2)`,
   `b = sqrt(3 F(2))`, `E_*(s) = (s+1)F(s)/b`, the shifted-Legendre scheme with the exact moments (21); the numerical
   values (22)–(23): phases `-0.99880741 - 0.04882370i`, `-0.99983369 + 0.01823721i`, `-0.99790571 - 0.06468528i`, the
   normalised Gram `O` with off-diagonals `-0.12772518`, `-0.01980716`, `0.19503489`, the loss spectrum
   `(-0.09239752, 0.46931541, 1.12308212)`; **the OPEN statement**: "A rigorous enclosure of the resolvent and scalar
   evaluations in (17)–(21) is still required to register either numerical conclusion as a proved theorem."
2. `report/sections/04s_h_theta_1.tex` (the registered shard: `prop:sonine-augmented-gram-resolvent`,
   `obs:sonine-enclosure-open`, `thm:h-theta-1-refuted`), `notes/h-theta-1/numerics.md` and `scripts/h_theta_1.py`
   (an independent Nystr\"om implementation on 40 and 64 Gauss--Legendre nodes reproducing every digit; the
   reviewer's third implementation at N = 32, 48), `notes/reviews/h-theta-1-2026-09-22.md`.
3. Sources: `refs/src/math/0203120` (Burnol), `0208121` (the de Branges structure of the Sonine spaces), `0112254`.

This is a rigorous-numerics lane: the deliverable is a theorem with a computer-assisted proof whose every
floating-point step is replaced by an interval enclosure or an explicit error bound. A hostile reviewer will try
to break the error analysis; a numerics lane will re-run your enclosure code. Label PROVED, REFUTED, SHARPENED or
OPEN. Keep a correction ledger. Do not pad.

## 0. The task

Prove, with certified error bounds, the two statements left numerical this morning:

**S1 (phases distinct).** The three values `E_*^#(rho_n)/E_*(rho_n)`, `n = 1, 2, 3`, at `rho_n = 1/2 + i gamma_n` are
pairwise distinct (equivalently, the normalised Sonine Gram `O` is not a diagonal congruence of a Cauchy matrix with
a common phase; but the direct statement is about the three unimodular numbers). A certified enclosure of each
phase to `10^{-4}` suffices since they differ by more than `0.03`.

**S2 (not contractive).** The generator loss matrix `-(d_i + conj d_j) O_ij` has a negative eigenvalue, certified:
enclose the `3 x 3` real symmetric matrix entrywise and prove its smallest eigenvalue is `< 0` (e.g. exhibit a
rational vector `v` with `v^T N v < 0` certified by interval arithmetic). Consequence: the prescribed evaluator
dynamics `T^0_t` of `conj:h-theta-1` is not a contraction semigroup on the Sonine norm for any exit, scalar or not
(dissipativity fails on three modes), which upgrades `thm:h-theta-1-refuted` from "no scalar exit" to "no
contraction at all", the replacement open question of shard 04s.

## 1. What must be certified

**R1 (the operator).** `T = Q C Q` on `L^2_0(0,1)`, `C` the cosine transform with kernel `2 cos(2 pi x y)`. Give a
certified bound `||T|| <= t_0 < 1` (the scheme needs `(I - T^2)^{-1}`); this morning's numerics found extreme
eigenvalues `-0.4710777795`, `0.5623175942`; a rigorous bound may come from a certified Galerkin/Nystr\"om
approximation plus an explicit bound on the approximation error (the kernel is entire; truncation of its Taylor or
Legendre expansion has explicit remainders), or from a Schur test with a rigorous integral. Also certify the
convergence of the shifted-Legendre discretisation: bound `||T - T_N||` explicitly in `N` (Legendre coefficients of
`cos(2 pi x y)` decay super-exponentially; give the bound).

**R2 (the vectors).** Enclose `r_2 = Q C q_2` and the solution `v = (I - T^2)^{-1} r_2` in the Legendre basis with a
certified tail bound; enclose `int r_s v` for `s = rho_n` (complex) and for the anchor values needed by (19)–(20),
using the exact moments (21) with interval arithmetic and a certified tail for the truncated Legendre expansion
of `v`; enclose the continuation (18) (`C q_s` as the series with `chi(s)`) at the needed points, with a certified
remainder for the truncated `n`-sum.

**R3 (the assembled quantities).** Enclose `F(2)` (must be `> 0`), `b`, `E_*(rho_n)`, `E_*^#(rho_n) = E_*(1 - rho_n)`
(or however `#` acts in the `s`-variable: fix from T3), the phases, the Gram entries by the de Branges formula
(with the diagonal by the derivative limit (20): enclose `E_*'` via a certified difference quotient or a certified
derivative of the scheme), the normalised `O`, and the loss matrix `N`. Then S1 and S2.

**R4 (zeros).** The zeros `gamma_1, gamma_2, gamma_3` are inputs; use the 24-digit values from the morning lane
(item 1 of its numerical checks) and state that their correctness is assumed from the literature (or certify them
with an interval Newton step on `xi` if cheap).

If a full certification is out of reach in one lane, deliver a **partial** theorem: certify S1 and S2 modulo an
explicitly stated, numerically checked but uncertified hypothesis (e.g. `||T|| <= 0.6`), and state exactly what
remains. Do not present floating-point agreement as certification.

## 2. Output format

`notes/sonine-enclosure/astra-proofs.md`: ledger (S1, S2, R1–R4, verdicts); the theorem statements with their
certified bounds (intervals printed); the error analysis as a proof with hierarchical steps; the enclosure code
described precisely enough that the numerics lane can re-run it (put the code in `checks/`; it may use `mpmath.iv`
or a hand-rolled interval type; say which and why); a section "Numerical checks for the blind lane" (the intervals
to reproduce); a section "Corrections to the brief"; a closing "What this changes in the notebook" with the status
to register for `obs:sonine-enclosure-open` and the one-sentence statement of the upgraded refutation.

## 3. Durability (the network is unreliable today; this is mandatory)

Write your output file **incrementally**: create `astra-proofs.md` with the ledger table (all verdicts `PENDING`)
before you start, and after finishing each item rewrite the file with that item's section and its updated ledger
row. If you are resumed after an interruption, read your own `astra-proofs.md` first, keep everything already
written, and continue from the first `PENDING` row. Keep a one-line `notes/sonine-enclosure/progress.txt` with the
item you are working on.
