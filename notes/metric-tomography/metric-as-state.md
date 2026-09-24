# The metric as an unknown state: observational channels, the contradiction pathway, and the MaxEnt ansatz

Author: `claude:fable-5.1`, 2026-09-24, recording a conversation with TJO of 2026-09-24. Status: **a record,
not a round.** Nothing here is registered as a claim; no prover, numerics or REFUTE lane has run. Statements
from the notebook are cited by claim label. Standard facts without a local source are marked "not
byte-cited". Companion: the explanation page *The Metric* (https://claude.ai/artifact/C1f9ZywZYyNc5vbXK6p7XZ),
which sets out the three levels of the metric problem (Level 1: zeros on the circle; Level 2: a positive form
`G` with `E^dagger G E = q G`, cheap once Level 1 holds; Level 3: a construction whose positivity is a
theorem). Everything below is at Level 2 unless said otherwise.

## 1. TJO's framing, verbatim

First message (2026-09-24):

> Now I want to speculate a little, which requires a certain willingness to suspend disbelief and cooperation,
> so work with me here for a moment. The metric is, morally speaking, an unknown object. It is positiv
> definite. I think of such things routinely as quantum states. I know it is infinite dimension, but this is
> not as salient as it might seem. So we are trying to learn about an unknown quantum state (not normalised).
> Now I cannot believe we know nothing about this hypothetical state. We must know *some things*. But we have
> some game rules here. We are not allowed to assume RH, we should not use knowledge if the zeroes themselves
> as that is a bit circular. Instead, we are required to use arithmetic data to build observable info about
> the state. I think of these as "observational" constraints. As we gain info our prior about the metric gets
> updated. The core physical question for me is thus: what kinds of observational data affect the metric *at
> all*. The moment we can find families of information channels to exploit we can start constraining the
> shape of the metric. Please give me a sense of what might work here

Second message (2026-09-24), after the answer recorded in sections 3 to 6:

> this is extremely interesting: please do record this all somewhere. The point I would like to make: The
> Weil form, for me, looks like a matrix elements of an unknown operator. Doesn't this all rather suggest a
> pathway to a *contradiction*: assume the the Weil form *is* positive, and try and find violations via matrix
> elements etc. RH is the absence of a contradiction. Sounds hopeless, *but*, and we have learnt this over
> and over in quantum info theory: gaining info by this path is extremely powerful! Make an ansatz about the
> state based on what you know via Jaynes MaxEnt: keep adding constraints, update. If you always fail to find
> a contradition you are extremel or in the convex hull. I just want that precisely recorded.

## 2. Game rules

1. RH is not assumed.
2. The zeros themselves are not used, neither their numerical values nor any statement about their
   distribution that is only known through them. (Unconditional theorems about the zeros proved from
   arithmetic, such as density theorems, are arithmetic data and are allowed; see 4.4.)
3. Only arithmetic data (primes, the archimedean place, the functional equation, the level tower) may be
   used to build observables of the state. These are the "observational constraints".
4. The object learned about is the metric, treated as an unnormalised positive functional: a quantum state
   on an algebra of observables. Infinite dimension is not treated as the salient difficulty.

## 3. What is actually unknown (the sharpening)

The candidate metric for zeta is the Weil form `W(f * f~)`, `f~(x) = x^{-1} f(1/x)`, on test functions on
the multiplicative group `R_+^x` (`cit:weil-criterion`; the notebook's discrete and continuous versions are
`thm:weil-positivity-finite` and `thm:weil-positivity-continuous`). Two facts fix the shape of the problem.

- **`W` is completely known as a linear functional.** It is the explicit formula: a sum over prime powers
  plus the pole term plus the archimedean term. It is computable from primes, no zeros needed. In the state
  language, every expectation value `<A_f> = W(f * f~)` is "measurable" from arithmetic.
- **What is unknown is whether `W` is positive**, and, at Level 3, a construction that makes its positivity
  manifest. RH is equivalent to positivity of `W` on the admissible test class (`cit:weil-criterion`).

So the problem is tomography run backwards: the full table of moments is in hand, and the question is
whether those numbers are the expectation values of any state at all, and what its purification looks
like. An observation "affects the metric" in exactly one of two ways: it is a family of test functions on
which positivity, or the value, of `W` is provable from arithmetic; or it is a structural fact that cuts the
space of candidate purifications.

**The organising theorem.** The single-place marginals of the state are known exactly and carry nothing
(`obs:prime-by-prime-blind`; also `prop:weil-blind-jordan`). `W` is a sum of place-by-place distributions;
a test function whose prime content is a single `p` sees only that place, the pole and the archimedean term,
and the resulting form contains no zeros. RH is a property of the correlations between places. Hence the
informative observables are exactly those that mix primes, and "how much of the metric a family constrains"
means "how much inter-place correlation it sees".

**Correction (2026-09-24, later in the day).** The paragraph above conflates two statements. What
`obs:prime-by-prime-blind` says is that a single-place *ansatz* (a product bond, a `p`-comb) reproduces no
zero. It does not say that the *restriction of the true form* `W` to test functions with prime content `{p}`
is uninformative. For `g = sum_k c_k phi(x - k log p)` the transform is `g^(s) = phi^(s) P(p^{-s})` with `P`
a polynomial, so `W(g * g~) = sum_rho |phi^(rho)|^2 |P(p^{-rho})|^2`: the one-place restriction sees the
zeros **folded on the `p`-circle**, the distribution of `p^{-i gamma}` on the unit circle, which is the
content of Landau's formula `sum_{0 < gamma <= T} x^rho = -(T/2 pi) Lambda(x) + O(log T)` (not byte-cited).
Its positivity is a necessary condition for RH, and an off-line pair is visible to it unless `P` vanishes at
the pair. Two consequences for the prime-content channel of section 4.2: (a) on the prime side, the Gram
entry between lattice points `p^a q^b` and `p^{a'} q^{b'}` receives a prime contribution only when the ratio
is a prime power, that is, when `a = a'` or `b = b'`; every mixed entry (`a != a'` and `b != b'`) is pure
pole-plus-archimedean, so **the cross-place information of the two-prime channel is carried entirely by the
archimedean kernel sampled at logarithms of `{p,q}`-smooth rationals** (the additive structure, once more);
(b) on the zero side, the mixed entries are `sum_rho |phi^(rho)|^2 (p^a q^b / p^{a'} q^{b'})^{i gamma}`-type
sums, whose Landau main term vanishes because the ratio is not a prime power, so the two-prime channel
measures the *error term* of Landau's formula at composite `x`. This is what "inter-place correlation"
means concretely.

## 4. Channels that provably move the prior

### 4.1 Dilation windows

Restrict `W` to test functions supported in `[lambda^{-1}, lambda]` with finitely many Fourier modes. This is
the Connes–Consani–Moscovici window (shard 03g and following; `num:weil-window-extension`), and Li's
coefficients are the same channel in a rotated basis: RH is equivalent to the Li sequence being a moment
sequence, that is, to Toeplitz positivity (`cit:li-criterion`), and each truncation is computable from primes.
The notebook has measured the learning rate of this channel on the certified `zst` stack (HANDOFF, benchmark
of 2026-09-18; `notes/zeta-spectral-triples/benchmark.md`): with `x = lambda^2`, the primes below `x` pin the
first zero to `e^{-4 pi x}` (5.4 digits per unit of `x`, independent of the number of modes `N`); the error at
height `gamma` grows like `10^{0.37 gamma}`; `N` saturates at `7.5 x`. In the Bayesian language: each new
prime is a measurement that contracts the posterior on the low part of the spectrum exponentially, and the
window width sets the resolution. This channel constrains positions. It says little about the shape of the
purification, because in the window basis the form is the data itself.

### 4.2 Prime-content windows (untried)

The complementary slicing. Instead of a window in dilation, take smoothed test functions concentrated on the
two-prime lattice `p^a q^b`. The restricted form is explicit (pole terms, the `p`-comb, the `q`-comb, the
archimedean term), and its positivity is the first statement that is genuinely about a correlation between
two places. Adding a third prime adds a third direction. The ideation ledger flagged "a two-prime coupling
parameter invisible to all one-prime data: the natural slot for a global adelic constraint, never pushed past
two primes" (`notes/ideation-ledger-2026-09-19/LEDGER.md`, item G1-T10-7); this is the observable that would
see it. Expected reading: a mutual information between places in the state, namely how much the `{2,3}`-form
knows about where the low modes sit compared with the `{2}`-form alone. Not in the ledger; no script exists.

### 4.3 Short-range positivity

For test functions of dilation support smaller than `log 2` (no prime power in the support of `f * f~`), `W`
reduces to the pole and archimedean terms, and positivity there is a statement about the archimedean local
factor alone, not about RH. So the state is known to be positive on all short-range observables, and every
prime `p` opens a new long-range direction at dilation `log p`. The danger lives at long dilation times, and
the primes are the scales at which it enters. (Archimedean positivity: Yoshida, Bombieri; not byte-cited,
no local source; to be checked before any use.)

### 4.4 Mollifiers and density theorems

The strongest unconditional facts about the spectrum are Selberg's positive proportion on the line,
Levinson's and Conrey's two fifths, and the zero-density and zero-free-region theorems (none byte-cited; no
local source). In tomographic language: a fixed fraction of the state's spectrum is exactly where RH puts it,
and the rest is confined to a strip that narrows with height. These are obtained by choosing observables
cleverly, and the observables are Dirichlet polynomials, that is, finite prime-content windows again. The
mollifier is the best information channel anyone has found, and its form confirms that the accessible
observables are prime-content windows of bounded length. These theorems are admitted under rule 2 because
their proofs use only arithmetic data.

### 4.5 Kinematic constraints

Before any measurement, the purification must be invariant under the dilation group, under the Weyl element
(the functional equation as a unitary intertwiner; `thm:weil-duality-pairing`, `thm:weil-line-duality`),
under the real structure, and under the grading (zeros odd, with the supertrace sign; shard 04b). In the level
tower it must be Galois-covariant with the character sectors as superselection sectors (shards 04c, 04d). The
archimedean Gamma factor is the known Hodge datum at infinity (shard 04q: Deninger's `R_infty`, the odd
ladder). The Weyl law `N(T) ~ (T/2 pi) log(T/2 pi e)` is the density of states, known unconditionally (not
byte-cited). Each of these cuts the space of candidate states to a commutant; none alone selects the metric,
as the finite Bost–Connes computations showed (shard 04d: Weyl covariance collapses to the depolariser,
symplectic covariance leaves the odd rates free).

### 4.6 Family channels

The metric is known in three neighbouring cases, and its shape there is the prior for its shape here. For
curves it is the intersection form of `C x C` restricted to the fibre-orthogonal classes: a natural global
metric restricted to an arithmetically defined subspace, positive by the Hodge index theorem
(`thm:rosati-ph-genus-two`, `thm:elliptic-ph-unitary`). For Selberg the metric is Haar on `L^2(Gamma \ H)`,
known, with the bound missing; partial coercivity (Kim–Sarnak's `7/64`, not byte-cited) comes from
symmetric-power `L`-functions, which is Deligne's tensor-power positivity at the archimedean place. That
channel is **empty for `GL_1`**: zeta has no symmetric powers, and the zeros are not local eigenvalues. This
is a useful diagnosis: the tensor-power trick constrains local data (Hecke eigenvalues at finite places); the
zeros are global data of the state and need the correlation channel (4.2) instead.

## 5. What does not move the prior

- Symmetry alone (shard 04d; `thm:arithmetic-metric`: the unitarising metrics form a cone with one symmetric
  ray, and the physical Lax–Phillips metric lies outside it).
- The metric defined by the channel's own stationary state (`obs:gl1-bond-no-metric`).
- Any bounded renorming of the energy metric: the Gram matrix of the Cauchy kernels has unbounded condition
  number, and the zero-mode kernels are not a Riesz basis (`thm:ks-not-deninger-h1`).
- Any finite set of single-place marginals (`obs:prime-by-prime-blind`).
- Under rule 2, numerical zeros.

## 6. The experiment proposed first

Prime-content tomography on the certified FLINT stack in `zst/`: the Weil form restricted to smoothed test
functions on the lattices generated by `{2}`, `{2,3}`, `{2,3,5}`, ... at fixed dilation width; certify the
minimal eigenvalue and track the minimal eigenvector as primes are added; then compare with the
dilation-window sequence at matched information content (number of prime powers seen). If the blindness
theorem is the whole story, the one-prime forms will be positive and structureless, the two-prime forms will
show the first nontrivial eigenvector, and the rate at which the eigenvector stabilises against further
primes is the learning rate of the state along the correlation direction. That number does not exist in the
ledger, and it is the one the Bayesian picture needs.

## 7. TJO's point, made precise: the contradiction pathway and the MaxEnt ansatz

This section restates the second message of section 1 in the notebook's terms. Each step marks what is
TJO's, what is a standard fact, and what is already in the notebook.

### 7.1 The Weil form as matrix elements of an unknown operator (TJO)

Let `A` be the involutive convolution algebra of admissible test functions on `R_+^x` with involution
`f -> f~`, or any finite-dimensional truncation of it (a finite family `f_1, ..., f_n`). The Weil form is the
sesquilinear form `G_{ij} = W(f_i * f~_j)`, a known Hermitian matrix for every finite family. Positivity of
`W` on the span is `G >= 0`. If `W` is positive, the GNS construction (standard; not byte-cited) gives a
Hilbert space `H_W`, a cyclic vector `Omega`, and a representation `pi` with `W(a) = <Omega, pi(a) Omega>`:
the Weil form is then literally the table of matrix elements of an operator algebra in a state. Under RH,
`W(f * f~) = sum_rho |f^(rho)|^2`, `H_W` is `l^2` of the zeros with multiplicity, `pi` of a dilation is
diagonal with the zeros as eigenvalues, and the unknown operator is the Hilbert–Pólya operator. The
existence of the GNS space **is** the positivity; the operator is unknown exactly to the extent that the
positivity is unproved.

### 7.2 The contradiction pathway (TJO)

Assume `W` is positive. A **violation** is an element `a = sum_i f_i * f~_i` of the positive cone of `A`
with `W(a) < 0`; equivalently a finite family with `G` not positive semidefinite; equivalently, in the
window channel, a next trace outside the disc of `prop:extension-disc`. Since `W` is known, a violation is a
finite, checkable certificate computed from primes alone, with no reference to the zeros: refuting RH by this
route is a finite computation, establishing it is not. **RH is the absence of a contradiction**, in the
precise sense of `cit:weil-criterion`: no admissible `a` has `W(a) < 0`. What the notebook adds is the
shape of a violation when one exists: an off-line pair `rho, 1 - rho-bar` contributes an indefinite `2 x 2`
block to `G` (`thm:weil-positivity-finite`, `prop:weil-orbit-negative`), so a violation, if there is one, is
localised in the two-dimensional span of the corresponding modes and is invisible to every family of test
functions whose transforms vanish at that pair.

### 7.3 The Jaynes MaxEnt ansatz and the update (TJO; the precise form is the notebook's)

Jaynes: among all states consistent with the constraints in hand, take the one of maximal entropy; add a
constraint, update. In the present setting the constraints are linear in the state (the known moments
`W(a_i)`), and the ansatz is a **positive completion problem**: given the known entries of `G` on a
finite family, choose the extension to further test functions that maximises entropy. For the Gaussian
(determinant) entropy this is the maximum-determinant positive completion (Dempster 1972, Grone–Johnson–Sá–
Wolkowicz 1984; for Toeplitz data Burg's maximum-entropy spectral extension; all standard, not byte-cited).
For the dilation-window channel the notebook already contains this object without the name:

- The admissible next trace, given the window up to lag `K`, is the closed disc of `prop:extension-disc`.
- Its **centre** `c_K` is the Yule–Walker one-step predictor (`prop:extension-disc`(ii)), which is exactly
  Burg's maximum-entropy extension: the MaxEnt ansatz sets the next reflection coefficient to zero, and
  that is the centre of the disc.
- Its **radius** `r_K = det W_K / det W_{K-1}` is the rigorous measure of remaining ignorance, non-increasing
  in `K` (`prop:extension-disc`(ii); shard 08g calls it "a rigorous measure of ignorance about the next lag").
- The **update** on learning the true next trace is the Schur (Levinson) step: recentre, shrink.
- A **contradiction** is the true next trace, computed from the primes, falling outside the disc; the
  boundary of the disc is the set of extensions by exactly `K+1` atoms on the circle
  (`prop:extension-disc`(iii), `cit:cf-kernel-circle`).

So, for the window channel, "make a MaxEnt ansatz, add a constraint, update, look for a contradiction" is
the Schur algorithm on the Li/Toeplitz data, and the diagnostic `r_K` proposed but not run in shard 08g
(compare the decay of `r_K` in `lambda` with the observed `e^{-4 pi x}` convergence of the first zero) is
precisely the rate at which the MaxEnt posterior contracts. For the prime-content channel (4.2) the same
completion problem has a non-Toeplitz pattern (the lattice `p^a q^b`), and the maximum-determinant
completion is the ansatz there; its contraction rate as primes are added is the number section 6 asks for.

### 7.4 "Extremal or in the convex hull" (TJO), made precise

The extremal positive functionals on the involutive convolution algebra of the abelian group `R_+^x` (with
`f -> f~`) are its hermitian characters, `f -> f^(s)` with `s = 1 - s-bar`, that is, `Re s = 1/2`: the
points of the critical line. "Never finding a contradiction" means `W(a) >= 0` for every admissible `a`.
The naive Bochner theorem does not apply: in the logarithmic coordinate `u = log x` the prime side of `W`
carries the weight `Lambda(n) n^{-1/2} = e^{u/2}`-growth, so `W` is not a tempered distribution and
Bochner–Schwartz gives nothing directly. The statement that plays Bochner's role is Weil's criterion itself
(`cit:weil-criterion`), whose proof is the localised block argument of 7.2: if some `rho` is off the line,
a test function whose transform is concentrated at the pair `rho, 1 - rho-bar` makes the indefinite `2 x 2`
block dominate and `W(f * f~) < 0`. Hence:

- `W` **in the closed convex hull** of the extremal states, in the sense `W(f * f~) = sum_rho |f^(rho)|^2`
  with every `rho` on the line (a positive combination of characters, one atom per zero), **is** RH.
- `W` itself is not extremal: it is a specific mixture with one atom per zero. Extremality of `W` would
  mean a single zero, which is false. The correct reading of TJO's disjunction is therefore "in the closed
  convex hull", and the decomposition into extremals is the zero set.
- Off the line, the pair `rho, 1 - rho-bar` is not a hermitian character, and its contribution to `W` is the
  indefinite block: the failure of the convex-hull representation is localised, which is what makes the
  contradiction search finite in each window.

### 7.5 What this pathway does and does not deliver

- It is a **Level 2** programme: it constrains the state through provable positivity on families, and it
  produces certificates of the form "no violation on this family". Each family that comes back positive
  narrows the admissible region (the disc, or its non-Toeplitz analogue) but does not close it; closing it
  for all families is RH.
- It does not produce the **Level 3** construction. The family channels (4.6) are the only ones that speak
  to the construction, and they say: look for a natural global metric and an arithmetically defined
  subspace, with definiteness on the subspace as the theorem. That is Weil's shape, and every proved case
  has it.
- Its value, as TJO says, is informational: the MaxEnt posterior after each update is a concrete candidate
  metric built from primes alone, and its contraction rate along each channel is a measurable quantity that
  says which arithmetic data carry information about the zeros and how fast. This is consistent with the
  game rules: the ansatz lives in the test-function (prime) basis and never touches the zeros.

## 8. Concrete next steps, if this is taken up

1. **Run the `r_K` diagnostic of shard 08g on `zst`** (the Schur-complement radius of the window Loewner form
   as `lambda` grows) and compare its decay with `e^{-4 pi x}`. This is the MaxEnt contraction rate of the
   dilation channel and requires no new theory.
2. **Build the prime-content window** (section 6): the Weil form on smoothed test functions on
   `{2}`, `{2,3}`, `{2,3,5}` lattices at fixed dilation width, with certified minimal eigenvalue and
   eigenvector; the maximum-determinant completion as the ansatz; contraction rate as primes are added.
3. **Byte-cite the standard inputs** before any claim is registered: Weil/Bombieri/Yoshida for the
   archimedean positivity of 4.3, Burg and Dempster for 7.3, Weil's block argument for 7.4, Selberg/Levinson/
   Conrey for 4.4.
4. **Register** the precise statements of 7.2 to 7.4 as claims only after a REFUTE lane; in particular the
   identification of the disc centre with Burg's extension should be checked against a source and against
   the `num:weil-window-extension` data.
