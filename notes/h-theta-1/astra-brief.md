# Brief for the prover: H-THETA-1. The Sonine evaluators at level one, their Gram matrix, and the rank-one exit test; the GL_1 bad-zero channel as a renewal channel; Burnol's two-dimensional causal model against the even sector

You are the prover in a mathematical research notebook (git repo, current directory). Author line for
everything you write: `codex:gpt-6-astra`. Write ONLY the file `notes/h-theta-1/astra-proofs.md` (create it;
overwrite if present) and, if you want scratch computations, python files under `notes/h-theta-1/checks/`.
Do not edit anything else. Do not run git. python3 with numpy, mpmath, sympy, scipy is installed; the first
3000 zeros of zeta are in `data/` (see `scripts/h_theta.py` for how they are loaded). You may read any file in
the repo. Read first, in this order:

1. `report/sections/04q_h_theta.tex` and `report/sections/04r_h_theta_channels.tex` (the previous round:
   the bond, the theta vector `g`, its Mellin transform `ghat`, the edge transforms, `thm:symbol-edge-quotient`,
   `thm:gl1-bad-zero-defect`, `thm:model-space-jets`, `prop:kernels-not-riesz`, the Sonine subsection and
   `conj:h-theta-1` near line 131 of 04r).
2. `notes/h-theta/astra-proofs.md` (your predecessor's ledger T1–T6; conventions fixed there are binding).
3. `report/sections/04l_elliptic_cavity_channel.tex` (`thm:h-exit-model`: the one-exit Gram identity;
   `def:h-exit-renewal-channel`, `thm:h-exit-renewal`) and `report/sections/04h_rebound_state.tex`
   (upper-half-plane conventions, the exit functional `j`, `lem:exit-one-dimensional`).
4. Sources under `refs/src/math/`: `0112254` (Burnol, two complete and minimal systems associated with the
   zeros of zeta: the Sonine spaces and the vectors `Y_{rho,k}`), `0001013` (Burnol, causality), `0602425`
   (Burnol, scattering, determinants, hyperfunctions in relation to Gamma(1-s)/Gamma(s): the de Branges
   structure of the Sonine spaces), `0203120`, `0407443`, `0208121`, `9911175`, `9809119`. Quote sources
   by file and line (`refs/src/math/0112254/<file>:<line>`) whenever you use a fact from them.

Be elementary and explicit. A blind numerics lane will test every displayed formula and a hostile reviewer
will try to refute every claim. Label every claim PROVED, REFUTED, SHARPENED (state the corrected claim and
prove it) or OPEN (say exactly what is missing). Keep a correction ledger for this brief. Do not pad.

## 0. The question

`conj:h-theta-1` (04r, status open) asks whether the algebraic semigroup `T^0_t` on the span of the level-one
Sonine evaluators `e_{rho,k} = R conj(Y^1_{rho,k})`, with `A_0 e_rho = d_rho e_rho`, `d_rho = (conj(rho) - 1)/2`
for simple zeros, extends to a strongly stable contraction semigroup *in the Sonine norm* with a scalar exit
form `-<A_0 f, h> - <f, A_0 h> = j_0(f) conj(j_0(h))` whose minimal unitary dilation is the regular dilation
`U_t` of the GL_1 bond. The conjecture records the necessary condition: for simple zeros the finite matrices
`N_{rho rho'} := -(d_rho + conj(d_rho')) G_{rho rho'}`, `G` the evaluator Gram matrix, must be positive of
rank one; the first falsification test is three zeros; a robust violation refutes the realisation in Burnol's
norm and "must not be rescued by an unspecified change of norm".

Your job: settle it. The author of this brief (`claude:fable-5.1`) believes the following.

## 1. The rank-one criterion is a Cauchy-kernel criterion (prove; this is the frame for everything)

**T1 (one-exit Gram identity, continuous time).** Let `T_t = e^{tA}` be a C_0 contraction semigroup on a
Hilbert space `K` with `-<Af,h> - <f,Ah> = j(f) conj(j(h))` for `f, h` in the domain (a scalar exit form).
If `A e_i = d_i e_i` (`Re d_i < 0`), then `-(d_i + conj(d_j)) <e_i, e_j> = j(e_i) conj(j(e_j))` (inner
product linear in the first slot; fix and state your convention). Conversely, if a family `{e_i}` in a
Hilbert space has Gram matrix `G_{ij} = c_i conj(c_j) / (-(d_i + conj(d_j)))` for some scalars `c_i != 0`,
then the map `e_i -> c_i k_{d_i}` onto the Cauchy kernels `k_d(z) = 1/(z - conj(d))` of `H^2` of the left
half-plane (or the equivalent model space) is isometric on the span, and the compression of the
translation semigroup gives a one-exit contraction with `T_t e_i = e^{d_i t} e_i`. So: **on a finite set of
simple zeros, `conj:h-theta-1` holds in a given norm iff the evaluator Gram matrix in that norm is a diagonal
congruence of the Cauchy matrix `1/(-(d_rho + conj(d_rho')))`**, i.e. iff `N` is positive of rank one. State
and prove this cleanly, including the Jordan-chain version for a multiple zero (jets) if it costs little.

**T2 (what `K_S` does).** In the model space `K_S = H^2 (-) Theta H^2` (04q/04r), with kernels `k_w` at the
zeros `w_rho` of `Theta`, `<k_w, k_w'> = (1 - Theta(w) conj(Theta(w')))/(-2 pi i (w - conj(w')))`-type
(fix constants from 04r), and `Theta(w_rho) = 0`, so the Gram matrix at zeros *is* a Cauchy matrix: the
Riemann channel is a one-exit contraction tautologically (this is `thm:h-exit-model` / `lem:exit-one-dimensional`
in the arithmetic case). Record the exact identity with the notebook's constants so the numerics lane can
check it at three zeros.

## 2. The Sonine space as a de Branges space, and the three-zero test (the main work)

**T3 (de Branges structure).** Burnol shows the Sonine spaces are de Branges spaces of entire functions in
the Mellin variable (`0602425`, and the C. R. note "Sur les espaces de Sonine associés par de Branges à la
transformation de Fourier", 2003; use what is in `refs/src` and mark anything else as not byte-cited). In a
de Branges space `H(E)` the reproducing kernel is
`K(w,z) = [E(z) conj(E(w)) - E^#(z) conj(E^#(w))] / (2 pi i (conj(w) - z))` (de Branges' convention; fix the
half-plane and the sign). If the level-one evaluators `Y^1_{rho}` are, up to a fixed nonvanishing factor
(the archimedean Gamma factor, or whatever Burnol's normalisation is; determine it from `0112254`), the
reproducing kernels of `H(E_1)` at the points `rho` (or at their images under the change of variable you
fix), then

`G_{rho rho'} = K(rho, rho')` and `N_{rho rho'} = const * [E_1(rho') conj(E_1(rho)) - E_1^#(rho') conj(E_1^#(rho))]`,

a difference of two rank-one Hermitian forms `a a^* - c c^*` with `a_rho = conj(E_1(rho))`,
`c_rho = conj(E_1^#(rho))`. **Prove: `N` is positive of rank one on a set of three or more zeros iff the
vector `c` is a multiple `lambda a` with `|lambda| < 1`, i.e. iff `E_1^#(rho)/E_1(rho)` takes one and the
same value of modulus `< 1` at every zero in the set (or `E_1^#` vanishes at all of them).** Determine the
precise objects: is `Y^1_{rho,k}` the reproducing kernel (k-th derivative) at `rho` in `H(E_1)`, or in a
twisted space, and what is the relation between `d_rho = (conj(rho) - 1)/2` and the de Branges variable.

**T4 (the verdict).** Decide whether `E_1^#/E_1` is constant on the zeros of zeta. The author expects NOT:
`E_1` is Burnol's structure function of the Sonine space (built from the Fourier/Hankel kernel on the unit
ball, `Gamma(1-s)/Gamma(s)`-type scattering, `0602425`), it has nothing to do with the zeros of zeta, and the
"inner" ratio `E_1^#/E_1` at three zeros of zeta will take three different values. If you can give a closed
form or a convergent scheme for `E_1` (Burnol writes the structure functions of the level-`a` Sonine spaces
through Fredholm determinants / hyperfunctions), evaluate `E_1^#/E_1` at the first three zeros
(`rho = 1/2 + i gamma_n`, `gamma_1 = 14.134725...`, `gamma_2 = 21.022040...`, `gamma_3 = 25.010858...`) and
state the three values. If a closed form is out of reach, prove the negative structurally (e.g. show
`E_1^# - lambda E_1` cannot vanish on infinitely many zeros of zeta for any `|lambda| < 1`, using growth or
the zero set of `E_1^#/E_1`, which is an inner function whose zeros are those of `E_1^#`, all in one
half-plane, versus the zeros of zeta on or near the critical line), and give the numerics lane a computable
substitute: the Gram matrix of the evaluators through Burnol's explicit formula for `<Y_rho, Y_rho'>`
if `0112254` provides one (it may express the Gram matrix through the Mellin transforms of the co-Poisson
images of test functions; find the cleanest computable expression).

**T5 (the sharpening; the norm that rescues it is the tautological one).** Prove: if a Hilbert norm on the
span of the evaluators makes `conj:h-theta-1` true for all finite sets of simple zeros, then the evaluators
are, up to scalars, Cauchy kernels at the points `d_rho`, so the completed span is unitarily the model space
`K_B` of the Blaschke product over the zeros; when RH holds and all zeros are simple this is `K_S` up to an
outer multiplier (Theta is a pure Blaschke product, `thm:symbol-edge-quotient`). Hence: the only norm that
rescues H-THETA-1 is the Riemann channel's own, and `conj:h-theta-1` is either refuted (Burnol's norm) or
empty (model-space norm). State the resulting theorem for the notebook and whether it should be registered as
`refuted`, `sharpened` or `proved` with a restated content.

## 3. The GL_1 bad-zero channel as a renewal channel (second target; HANDOFF item ii)

`thm:gl1-bad-zero-defect` gives `K_bad = H^2(C_+) (-) B_bad H^2(C_+)`, one Jordan chain per zero with
`sigma > 1/2`, zero iff RH. Treat `K_bad` as the bond of a renewal channel in the sense of
`def:h-exit-renewal-channel` with synthetic off-line zeros: pick a finite set `Z` of hypothetical zeros
`rho = sigma + i gamma` with `sigma > 1/2` (and their functional-equation and conjugate partners, so that the
Blaschke product is real on the axis in the notebook's sense; say which partners `B_bad` actually contains,
from 04q).

**T6.** Prove: (a) the compression `Z_t` of the forward dilation to `K_bad` (with the orientation fixed in
`thm:gl1-bad-zero-defect`(a)) is a one-exit contraction semigroup: rank-one defect `I - Z_t^* Z_t`, modes
`w_rho`, decay rates `(sigma - 1/2)/2`, exit amplitudes `a_rho` given by the Cauchy-kernel identity of T1;
(b) with a reset density `Omega` the renewal channel `E_Omega(rho) = Z rho Z^* + Tr(J rho J^*) Omega` has a
unique stationary state and the mean holding time `tbar` is the sum over the (synthetic) bad zeros of an
explicit rational expression in `sigma, gamma` (compute it for one and for two zeros in closed form; give
the general formula); (c) as `sigma -> 1/2^+` for one synthetic zero the holding time diverges like
`1/(sigma - 1/2)` and the channel degenerates to the identity on a zero-dimensional bond: "RH is the limit
in which the GL_1 renewal channel has nothing to do". State exactly what is proved and what is a definition.

## 4. Burnol's two-dimensional causal model against the even sector (third target; HANDOFF item iii)

Under RH, Burnol's scattering multiplier is `v_+^2`, `v_+(tau) = (tau - i/4)/(tau + i/4)`, with causal model
space `K_{v_+^2}` of dimension two (`thm:gl1-bad-zero-defect`(c)). The Phantasm's even sector on the bond is the
pair of constant terms `1` and `y^{-1/2}` of the theta bond state (04p, `prop:riemann-theta-dilation-bond`),
the poles `s = 0, 1`.

**T7.** Determine `K_{v_+^2}` concretely in the `y`-picture. The author's computation: the double zero of
`v_+^2` at `tau = i/4` corresponds, in the dictionary `w_rho = gamma/2 + i(sigma - 1/2)/2`, to `sigma = 1`,
`gamma = 0`: the pole `s = 1`, and `K_{v_+^2}` is the Jordan block `{1_{y>1}, log(y) 1_{y>1}}` (the constant term
cut to the outgoing half and its log-jet), NOT the pair `{1_{y>1}, y^{-1/2} 1_{y>1}}` of the two poles. Check
the conventions (04q uses `-i y^{-(1-sigma)/2 - i gamma/2} 1_{y>1}` for the kernel at a zero; apply the same
dictionary to the pole) and prove which it is. Then explain the discrepancy with the GL_2 side, where the pole
factor is `r(tau) = (tau - i/2)/(tau + i/2)` (`prop:siegel-constant-term`, a simple pole pair, model space of
dimension one per pole, not a Jordan block): the square in `v_+^2` comes from Burnol's `V = 1 - A` acting
twice (once on each side of the theta image)? Give the exact origin of the exponent 2 from `0001013` (byte-cite
his definition of `V` and `S = Z V^2 B^{-2}`), and state a clean "even-sector dictionary" theorem: GL_1
(Burnol): `v_+^2`, one pole, length-two chain; GL_2 (Eisenstein): `r`, the pole pair `s = 0, 1` of `xi`
read on the critical line; whether the second pole of GL_1 (`s = 0`, the constant `1`) is invisible to
Burnol's system because of the subtraction in his `E` (the `E_0` versus `E` step of 04q), and what the
compression of the dilation does on `K_{v_+^2}` (its `2 x 2` matrix, its exit vector, its holding-time law).

## 5. Output format

`notes/h-theta-1/astra-proofs.md` with: a ledger table (T1–T7 with verdicts); full proofs with hierarchical
steps where the argument is long; every source quote byte-cited by file and line; a section "Numerical checks
for the blind lane" listing explicit formulas with expected values (which zeros, which constants, to how many
digits); a section "Corrections to the brief" (numbered); and a closing section "What this changes in the
notebook" naming, per claim, the status it should get in `db/claims.tsv` (`proved`, `refuted`, `sharpened`,
`open`) and the one-sentence statement to register. If you refute `conj:h-theta-1`, say in one sentence what
replaces it as the open question on this lead, if anything.

## 6. Durability (the network is unreliable today; this is mandatory)

Write your output file **incrementally**: create `astra-proofs.md` with the ledger table (all verdicts
`PENDING`) before you start on the mathematics, and after finishing each claim rewrite the file with that
claim's section and its updated ledger row. Never hold finished work only in memory. If you are resumed after
an interruption (the prompt will say so), read your own `astra-proofs.md` first, keep everything already
written, and continue from the first `PENDING` row. Keep a one-line `notes/h-theta-1/progress.txt` with the
claim you are working on, updated whenever you move to the next claim.
