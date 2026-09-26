# Brief for lane I (RTP-2): the non-admissible prime-content channel. The Kronecker lemma with impurity primes, the first O(1) inter-place observable, and its learning rate

You are `codex:gpt-6-astra`, a prover and constructive verifier in a mathematical research notebook (git repo,
current directory). Read `notes/rtp-round-2/brief.md` first (game rules, conventions, output protocol; binding).
Then read fully: `notes/rtp-round-1/lane-A2.md` (definitions 1.1–1.2, the closed forms per entry, the Kronecker
lemma 4.1, the admissibility table, section "Findings against the brief" item 3: "To see inter-place structure at
O(1), the channel would need test functions whose supports overlap prime powers other than the ratio, that is, a
non-admissible delta with the full prime sum. The implementation handles that"), `scripts/rtp1_prime_content.py`
(reuse its functions: bump `phi_delta`, `R_delta`, the pole, archimedean and prime closed forms, `psi_general`;
import it or copy what you need into your script and say which), the review `notes/reviews/rtp-round-1-2026-09-24.md`
items C4–C5 and its script `notes/reviews/scratch_rtp1_lattice.py` (the reviewer's independent real-space
implementation, prime term summed over ALL prime powers with `|log k -+ D| < 2 delta`, no admissibility assumed),
shard `report/sections/08i_riemann_tomography.tex` (`lem:mixed-entries-kronecker`, `num:rtp-prime-content`,
`obs:rtp-round-1-reading`(i)–(ii)), and `notes/metric-tomography/metric-as-state.md` sections 3 (with the
Correction), 4.2 and 6. Write only `notes/rtp-round-2/impure-bumps/astra-proofs.md`, `progress.txt`, `checks/`, the
script `scripts/rtp2_impure_bumps.py` and its output `outputs/rtp2_impure_bumps.txt`. Do not run git. python3 with
numpy, mpmath, scipy, sympy is available (no python-flint; use mpmath at `mp.dps >= 30` and report quadrature
error estimates); 64 cores.

## 0. Setting and the gap left by round 1

Test class: bumps `phi_alpha(y) = phi_delta(y - t_alpha)`, `t_alpha = sum_p a_p log p`, on the lattice
`Lambda_S(A) = {0..A}^r` of `S = {p_1 < ... < p_r}`; Gram entry `G_{alpha beta} = pole - arch - prime` with
`prime = sum over prime powers k of Lambda(k) k^{-1/2} [R_delta(log k - D) + R_delta(log k + D)]`,
`D = |log(n_beta/n_alpha)|`, `R_delta` supported in `|s| < 2 delta`. **Admissible** `delta` (round 1): the only prime
powers within `2 delta` of any lattice ratio `D` are the ratios themselves; then the mixed entries carry no prime
term, `G = (Kronecker sum of the one-prime forms) + (mixed pole and archimedean entries)`, and everything
inter-place is `O(delta)`. Admissibility forces `delta` down like the inverse of the largest lattice ratio
(`1.2e-6` at `{2,3,5}, A = 4`), so the admissible channel is perturbative and blind to `O(1)` inter-place structure.
Round 2 asks what happens when `delta` is **not** admissible: the supports then overlap prime powers `k` that are
not lattice ratios (impurities), and the prime sum couples lattice points through third primes.

## 1. Theory (prove or correct)

I1 (the generalised Kronecker lemma). Write `G = G_nomix(S, A, delta) + M_pole + M_arch + sum_k Lambda(k) k^{-1/2} P_k`,
where `P_k` is the matrix of the impurity prime power `k` (entries `R_delta(log k - D) + R_delta(log k + D)` over
all pairs, including pairs with `D` on an axis and the diagonal `D = 0`). Prove: (i) `P_k` depends on `k` only
through the set of pairs `(alpha, beta)` with `|log k - D_{alpha beta}| < 2 delta`, its entries are nonnegative, and
`P_k` has rank at most the number of distinct `D` values it touches (give the exact structure: for a single
impurity it is a symmetric 0/1-pattern matrix weighted by `R_delta` values); (ii) `P_k` for `k` a power of a prime
`p in S` is already inside the one-prime forms (so the impurities are exactly the `k` with a prime factor
outside `S`, plus the `S`-smooth `k` that are not lattice ratios because the exponent exceeds `A`; separate the two
kinds); (iii) the exact `delta`-threshold at which the first impurity of each kind enters for `S = {2}`, `{2,3}`,
`{2,3,5}` and `A = 1..4` (a table; it is `min over lattice ratios D and non-ratio prime powers k of |log k - D| / 2`).

I2 (what the impurity measures). Prove: the impurity block `P_k` is a rank-one-per-pattern object whose weight
`Lambda(k) k^{-1/2}` is the datum of a third place `q | k`, and the two-prime form on `Lambda_{{2,3}}(A)` with
impurities is a linear functional of the weights of finitely many primes `q` outside `{2, 3}` (list them for
`A = 2, 3` and a few `delta`). Hence the "inter-place correlation" of the impure channel is, to first order, the
**explicit-formula contribution of the third primes at the lattice ratios**, not a correlation between 2 and 3 alone.
State this as a proposition and say what remains genuinely two-place (the pole and archimedean mixed entries,
and the second-order effects). Then give the perturbation-theoretic lower and upper bounds on the Schmidt defect of
the minimal eigenvector of `G` in terms of the impurity block (spectral gap of `G_nomix`, `||P_perp M v_0||`), so
that "O(1) inter-place structure" has a theorem behind it rather than a fit.

I3 (positivity of the impure form). The impure form is still the true Weil form restricted to a legitimate test
class, so its positivity is a necessary condition for RH and holds unconditionally where the reviewer's real-space
check certified it. Prove that for every `delta` the impure two-prime form is `sum_rho |...|^2`-type on the zero side
(the explicit formula for `G_{alpha beta}`, as lane A2 section 6 checked numerically), so that a negative eigenvalue
at some `delta` would be an RH violation (labelled: this is the contradiction pathway of `metric-as-state.md` 7.2
on the impure lattice class). Do not compute with zeros except in a labelled comparison step.

## 2. Numerics (`scripts/rtp2_impure_bumps.py`; deterministic, `check(cond, msg)` as in `scripts/gl1_bond.py`, no
timestamps, print quadrature error estimates; `outputs/rtp2_impure_bumps.txt`)

I4. For `S = {2,3}`, `A = 2, 3` and for `S = {2,3,5}`, `A = 2`: sweep `delta` from the admissible maximum up to
`delta = 0.35` (the bump half-width at which `log 2 / 2` is reached and the bumps at 1 and 2 overlap; stop before
`2 delta >= log 2` or say what happens there) on about 12 log-spaced values. At each `delta`: `lambda_min(G)` and
its eigenvector; the Schmidt defect of the eigenvector (as lane A2 defines it) against `G_nomix`'s product
eigenvector; the decomposition `lambda_min(G) - lambda_min(G_nomix)` into mixed-pole, mixed-arch and impurity parts
(first order along the eigenvector, then exact); the list of impurity primes active; the "mutual information
between places" `log det G_nomix - log det G` (say whether it is a mutual information in the Gaussian sense, cf.
lane A1 lemma A1.1(4), or only a log-det gap). Identify the smallest `delta` at which the Schmidt defect exceeds
`0.1` (an `O(1)` observable) and which impurity primes drive it.

I5. Learning rate along primes. At the `delta` of the `O(1)` observable: restrict the `{2,3,5}` eigenvector to the
`{2,3}` sublattice and compare with the `{2,3}` eigenvector (overlap, as A2 did), and repeat for `{2,3,5,7}` at
`A = 1` if affordable; report how the minimal eigenvector moves as a prime is added, at fixed `delta`, against the
`O(delta^2)` law of the admissible regime. Separately, switch the impurity primes off one at a time (remove the
`P_k` of a single `q`) and report the eigenvalue and eigenvector response: this is the sensitivity of the impure
two-prime observable to each third prime, the number `metric-as-state.md` section 6 asks for.

I6. Comparison step (zeros allowed, labelled). For two impure entries, compare the prime-side value with the
zero-side sum over the first 2000 zeros (as lane A2 section 6 did; `mpmath.zetazero` or a cached zero table under
`data/`), and report the truncation behaviour; this is the implementation check of I3.

## 3. Output format

`notes/rtp-round-2/impure-bumps/astra-proofs.md`: ledger; I1–I3 as propositions with proofs (hypotheses `H-*`;
PROVED / SHARPENED / REFUTED / OPEN); I4–I6 tables with precision regimes; "Numerical checks for the blind lane"
(three eigenvalues, one Schmidt defect, one threshold `delta`); "What this changes in the notebook" (what
`obs:rtp-round-1-reading`(i)–(ii) and `lem:mixed-entries-kronecker` become; candidate claim rows for shard 08j
with kind and status; whether the impure prime-content channel is a genuine correlation channel or a disguised
third-prime channel, in one paragraph; the next step). Write incrementally; `progress.txt` lines I1..I6.
