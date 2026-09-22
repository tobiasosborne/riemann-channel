# Brief for the prover: the unbounded arithmetic metric of the Riemann channel is a closed positive form; is it Connes's weighted norm? The unit-coefficient form, its domain, Connes's delta-weighted Sobolev space on the bond, and the exit

You are the prover in a mathematical research notebook (git repo, current directory). Author line for
everything you write: `codex:gpt-6-astra`. Write ONLY the file `notes/connes-weighted-metric/astra-proofs.md`
(create it; overwrite if present) and, if you want scratch computations, python files under
`notes/connes-weighted-metric/checks/`. Do not edit anything else. Do not run git. python3 with numpy,
mpmath, sympy, scipy is installed; the first 3000 zeros are in `data/`. Read first:

1. `notes/deninger-bond/astra-proofs.md` (this morning's lane; binding conventions in its Section 0): C3 (a
   positive invariant metric on the full jet span iff critical and simple; the star (3.5)); **C4** (no bounded,
   boundedly invertible `G` on `K` with `C_t^* G C_t = e^{-t/2} G`; `sup_t e^{t/4} ||C_t|| = infinity`
   unconditionally by the two-close-kernel estimate (4.4); **4.4 "unbounded metric needs qualification"**: the
   biorthogonal system `b_rho` to the modes `e_rho = m_rho`, the bounded compact injective forms
   `G(f,f) = sum g_rho |<f, b_rho>|^2` with `sum g_rho ||b_rho||^2 < infinity`, and the **unit-coefficient form**
   `||bar B_0 f||^2` with `B_0(sum a_rho e_rho) = (a_rho)`, closable, closed positive form with a `C_t`-invariant
   domain satisfying the similitude); C5 (Weil's form; the evaluation map `A f = (<f, k_rho>)` is closed,
   injective, densely defined, unbounded both ways; the three spectral spaces not to be conflated).
2. `report/sections/04q_h_theta.tex` (`cit:connes-cokernel-critical`: Connes's weighted cokernel, the
   `delta`-weighted topology in which the critical zeros' characters appear with multiplicity up to
   `n < (1 + delta)/2`; `prop:theta-spectral-density`: in the unweighted bond the zeros are absorption lines,
   "they become a cokernel only in Connes's weighted topology"), `04r_h_theta_channels.tex` (`thm:model-space-jets`,
   `prop:kernels-not-riesz`, `lem:exit-one-dimensional` if present), `notes/h-theta/astra-proofs.md`.
3. Sources: `refs/src/math/9811068` (Connes, "Trace formula in noncommutative geometry and the zeros of the
   Riemann zeta function": the weighted Sobolev spaces `L^2_delta`, Theorem 1 (spectral realisation as a
   cokernel), the operator `E`, the role of `delta`), `refs/src/math/0311468` (Meyer), `refs/src/math/0001013`,
   `0203120`, `0208121` (Burnol). Quote by file and line.

Be explicit. A numerics lane will test every displayed formula and a hostile reviewer will try to refute every
claim. Label PROVED, REFUTED, SHARPENED or OPEN. Keep a correction ledger. Do not pad.

## 0. Why this round

C4 showed that Deninger's positive metric on the Riemann channel's model space `K` cannot be boundedly
equivalent to the energy metric, and that the natural candidate, the unit-coefficient form making the modes
orthonormal, is an unbounded closed positive form. Connes realised the critical zeros as a *cokernel* by
changing the topology of the bond to a `delta`-weighted Sobolev norm. The author of this brief
(`claude:fable-5.1`) suspects these are the same object seen twice: the unbounded arithmetic metric of C4 is
(boundedly equivalent to, or is the form closure of) Connes's weighted norm restricted to the outgoing model
space, with the weight exponent `delta` controlling which jets are in the domain. Settle it.

**W1 (the unit-coefficient form, concretely).** Under RH and simplicity (state exactly where each is used),
give the unit-coefficient closed form `Q_0(f) = ||bar B_0 f||^2 = sum_rho |a_rho(f)|^2` (`f = sum a_rho e_rho`) as
explicitly as possible: its domain `D(Q_0)`, its self-adjoint representing operator `G_0` (unbounded,
positive, `G_0 e_rho = ` what?), the `C_t`-similitude on the domain, and the biorthogonal system
`b_rho = c_rho C_Theta k_rho` with the constants `c_rho` (from 4.4: nonzero scalar multiples of `C_Theta k_rho`;
compute `c_rho` and `||b_rho||` in terms of `Theta'(w_rho)` and the height `1/4`: for a simple zero
`||b_rho||^2 = ` ? — the reciprocal of the derivative of the Blaschke product at the zero, `1/|Theta'(w_rho)|^2`
times the kernel norm; derive it). Then the growth: `||b_rho||` is unbounded along the zeros (this is the
non-Riesz statement); give its size in terms of the local zero spacing (`|Theta'(w_rho)|` is controlled by the
product over nearby zeros), i.e. `||b_rho|| ~ ` (distance to the nearest other zero)`^{-1}`-type; make this a
theorem with explicit constants where possible, or a two-sided estimate.

**W2 (Connes's weighted norm on the bond, transported).** Transport Connes's `L^2_delta` (his weight
`(1 + log^2|x|)^{delta/2}` or `(1+|x|)^delta`-type; read `9811068` and state it exactly, with the variable
change to the notebook's `X = log y`) to the bond `L^2(R, dX)`: it is a Sobolev-type weight `(1 + X^2)^{delta/2}`
in `X` (a polynomial weight in `log y`), i.e. in the Fourier variable `u` a *derivative* norm of order `delta/2`.
Prove: on the outgoing model space `K` (or on `H^2_+`), the `delta`-weighted norm restricted to the span of the
modes `m_rho = e^{lambda_rho X} 1_{X>0}` is `||m_rho||_delta^2 = int_0^infty (1 + X^2)^{delta/2} e^{-X/2} dX`-type,
the same for every critical zero (the weight does not see `gamma`), so the weighted norm is NOT diagonal in the
modes but its diagonal is constant; compute the weighted Gram `<m_rho, m_rho'>_delta` in closed form (a
`Gamma`-function / confluent hypergeometric expression in `gamma - gamma'` and `delta`) and its decay in
`|gamma - gamma'|` (faster than the unweighted `1/|gamma - gamma'|`: the weight smooths the kernel). Then the
question: for which `delta` (if any) is the weighted Gram matrix of the normalised modes bounded above and
below on `l^2` (a Riesz system in the weighted norm) — the author expects: the weighted Gram is a Toeplitz-like
matrix in `gamma` with symbol given by the Fourier transform of `(1 + X^2)^{delta/2} e^{-X/2} 1_{X>0}`, whose
decay `|gamma - gamma'|^{-1-delta}` (or so) combined with the zero density `T log T` gives Schur-test
boundedness iff `delta > ` some threshold, but NO lower bound because the density is unbounded (gaps to 0):
prove or refute; if the lower bound fails for every `delta`, then Connes's weighted norm is *also* not
equivalent to the unit-coefficient form on the mode span, and the two "unbounded metrics" are genuinely
different — say which one Deninger's programme should mean.

**W3 (Connes's cokernel versus the model space).** Connes's Theorem 1 (`9811068`): the critical zeros appear
as a cokernel of the map `E` on `L^2_delta`, with multiplicity `n < (1 + delta)/2`, so for `delta` in `(1, 3)`
each simple zero appears once. Prove: the cokernel's dual (the annihilator of the range of `E` in the weighted
dual space) is spanned by the characters `y^{-i gamma/2}`-type distributions (Connes's `|x|^{-1/2 - i gamma}`),
which are the *unweighted, uncut* absorption characters, and compare with `thm:model-space-jets` (the cut and
damped characters `y^{-1/4 - i gamma/2} 1_{y > 1}` span `K`): the map "cut to `y > 1` and damp by `y^{-1/4}`" sends
Connes's cokernel basis to the mode basis of `K`. Is this map the inverse of the evaluation map `A` of C5 (up to
the constants of W1), and is it bounded from the weighted dual to `K`? State the exact relation as a theorem
or refute it. What is the role of `delta` for the *jets* (multiple zeros): Connes's `n < (1 + delta)/2` versus
the notebook's "all jets are in `K` unconditionally".

**W4 (the exit in the arithmetic metric).** In the unit-coefficient form the compression `C_t` becomes
`e^{-t/4}` times a unitary (under RH, simple zeros), so the exit `-(A + A^*) = j^* j` in the *energy* metric
becomes, in the arithmetic metric, the loss `I/2` (generator) and `(1 - e^{-t/2}) I` (finite time), of
infinite rank (this is the last remark of D5.5 in `notes/deninger-cusp/astra-proofs.md`; check it): one exit
per mode instead of one exit for all modes (`lem:exit-one-dimensional`). Prove the exact relation between the
two exits: the single energy exit functional `j(f) = f(0)` (the value at `X = 0`) in mode coordinates is
`j(sum a_rho e_rho) = sum a_rho` (all modes couple with weight one; the "all-ones loss matrix" of
`notes/h-theta-1/astra-proofs.md` T2), whereas the arithmetic exit is the identity in mode coordinates; hence
the arithmetic metric is the energy metric *conjugated by the exit*: `G_0 = ` (the map `a -> sum a`)... make
this precise: the Gram of the modes in the energy metric is the Cauchy matrix `i/(w_j - bar w_i)`, whose
"loss" `-(d_i + bar d_j) G_ij = 1` is the all-ones matrix; the unit-coefficient metric has loss `I/2`; relate
the two by the explicit factorisation `Cauchy = D^* (1/(...)) D` and say what "one exit versus one exit per
mode" means as a statement about the two metrics (the energy metric is the unique one in the cone with a
rank-one generator loss? prove or refute: among all positive forms in the C3 cone, which have a rank-one
generator loss — by T1 of `notes/h-theta-1/astra-proofs.md` exactly the diagonal rescalings of the Cauchy
Gram, i.e. the energy metric's diagonal congruence class; is that class one point in the cone or many?).

**W5 (what this changes).** One structured page: the dictionary (energy metric, one exit, Cauchy Gram, not
Riesz) versus (arithmetic/unit-coefficient metric, one exit per mode, unbounded) versus (Connes's weighted
norm, cokernel, `delta`), which of these Deninger's positive Hodge structure should mean, and the precise
statement of what is still missing (a zero-free description of the unbounded metric's domain).

## Output format

`notes/connes-weighted-metric/astra-proofs.md`: ledger table (W1–W5, verdicts); full proofs with hierarchical
steps; sources quoted by file and line; a section "Numerical checks for the blind lane" (explicit: `||b_rho||`
for the first ten zeros versus `1/|Theta'(w_rho)|`; the weighted Gram of the first ten modes at `delta = 1, 2`
and its extreme eigenvalues versus the unweighted Cauchy Gram; the all-ones loss versus `I/2`); a section
"Corrections to the brief"; and a closing "What this changes in the notebook" with statuses and one-sentence
statements.

## Durability (the network is unreliable today; this is mandatory)

Write your output file **incrementally**: create `astra-proofs.md` with the ledger table (all verdicts
`PENDING`) before you start, and after finishing each claim rewrite the file with that claim's section and its
updated ledger row. If you are resumed after an interruption, read your own `astra-proofs.md` first, keep
everything already written, and continue from the first `PENDING` row. Keep a one-line
`notes/connes-weighted-metric/progress.txt` with the claim you are working on.
