# The finite-prime language and the Fannes–Nachtergaele–Werner exclusion argument: a future direction

Author: `claude:fable-5.1`, 2026-09-24, from a conversation with TJO. Status: **a record of a future direction,
not a round.** Nothing is registered; no lane has run. Notebook results are cited by claim label. Standard
facts without a local source are marked "not byte-cited". Companion: `metric-as-state.md` in this directory
(the contradiction pathway; "a violation is a finite certificate computable from primes alone, so refutation
is a finite computation and proof is not"), which this note riffs on.

## 1. TJO's prompt, verbatim

> Ok here is a crazy-ass idea riffing on "A violation is a finite certificate computable from primes alone,
> so refutation is a finite computation and proof is not.": build a language (complexity class) of all
> quantities obtainable by finite computations using finite primes. Argue that contained in this language
> are certain classes of numbers, but certain other numbers are outside. (I am thinking of MIP*=RE here, and
> that whole argumentation style). Then find a value of zeta which somehow cannot belong to the language.
> Super vague I know. BUT! there is one precedent where a vestigial form of such an argument *actually was
> used*: in the Fannes Nachtergaele Werner FCS paper they use the fact that the gs energy density from bethe
> ansatz was some transcendental number and then they had a proof that FCS *could not represent the ground
> state*. Awesome argument of great insight. Please try and make something of this vagueprompt, record it as
> a future direction. then report back

And, mid-task:

> FNW argument is literally that one line: finite bond dim FCS can only produce non-transcendal energy
> denisties

## 2. The precedent, and its rigorous form

**Source status.** Fannes, Nachtergaele, Werner, *Finitely correlated states on quantum spin chains*, Comm.
Math. Phys. 144 (1992) 443–490, doi 10.1007/BF02099178. Not byte-cited: Springer, Project Euclid and
academia.edu all refuse the session proxy (bot protection, 403), Semantic Scholar reports no open copy, and
Nachtergaele's page lists the paper without a file. The argument below is TJO's statement of the precedent,
given the rigorous form it needs. The Hulthén value `e_0 = 1/4 - log 2` for the spin-1/2 Heisenberg
antiferromagnet per site (`H = sum S_i . S_{i+1}`) is standard and not byte-cited.

**The one line, read literally, needs a qualification.** A finitely correlated state with transcendental
matrix entries has transcendental energy densities (already a product state `cos(1)|0> + sin(1)|1>` does),
so "finite bond dimension produces only non-transcendental energy densities" is a statement about the
*optimum*, not about individual states. In that form it is a theorem:

**Proposition A (FNW exclusion, Tarski–Seidenberg form).** Fix a bond dimension `d` and a finite-range
interaction `h` with real algebraic matrix entries. The set `F_d` of translation-invariant finitely correlated
states with auxiliary algebra of dimension at most `d` is a semialgebraic set defined over the real algebraic
numbers (parameters: the real and imaginary parts of the Kraus tensors, or of the Choi matrix of the
generating completely positive unital map; constraints: positivity, unitality, the fixed-point equations and
the normalisation of the boundary state). The energy density `e(omega) = omega(h)` is a semialgebraic
function of these parameters with algebraic coefficients. Hence `e_d := inf_{F_d} e` is a real algebraic
number (Tarski–Seidenberg: the image of a semialgebraic set under a semialgebraic map is semialgebraic, and a
semialgebraic subset of the line defined over a real closed subfield has its endpoints in that subfield;
not byte-cited). Consequently, if the ground-state energy density `e_0` of `h` is transcendental, no ground
state of `h` is finitely correlated with any finite `d`, and moreover `e_d > e_0` strictly for every `d`.
For the Heisenberg chain `e_0 = 1/4 - log 2` is transcendental by Hermite–Lindemann (not byte-cited).

*Proof of the last step.* If a ground state `omega` lay in `F_d`, then `e_0 = omega(h) >= e_d >= e_0`, so
`e_0 = e_d` is algebraic. `[]`

**Three ingredients, which is what one must reproduce.**

1. A candidate class that is *finitely parametrised and semialgebraic over a countable real closed field*
   (so that optima are definable, hence algebraic).
2. A target quantity *known to be transcendental* (or merely known to lie outside the field of step 1).
3. The target *defined implicitly* (as the ground state of `h`, with its energy computed by an independent
   exact method, the Bethe ansatz), so that step 2 is an independent computation and not a tautology.

**Quantitative remark (untested, recorded for later).** Effective quantifier elimination bounds the degree
and height of `e_d` by explicit functions of `d` (Basu–Pollack–Roy type bounds; not byte-cited), and a
transcendence measure for `log 2` (Fel'dman/Baker type: `|log 2 - alpha| > H(alpha)^{-c(D)}` for algebraic
`alpha` of degree `D` and height `H`; not byte-cited) then gives an explicit *lower* bound on the variational
error `e_d - e_0` as a function of `d`. That is a rigorous statement that no matrix-product ansatz of bond
dimension `d` can converge to the Heisenberg energy faster than Diophantine approximation of `log 2` by
algebraic numbers of the corresponding degree and height permits. The bound is presumably astronomically
weak, but it is the first "learning-rate" statement of the kind the tomography note asks for that comes
from transcendence rather than from analysis. Nobody appears to have written it down; it is a small,
self-contained project.

## 3. The finite-prime language, made precise

"All quantities obtainable by finite computations using finitely many primes" has to say what the
computations are allowed to touch. The Weil form `W(f)` for a test function of compact dilation support is a
finite sum over prime powers below the support plus the pole term plus the archimedean term, so the natural
language is generated place by place. Define, for a finite set `S` of primes,

    L_S := the Q-bar-vector space spanned by 1, {log p : p in S}, and the archimedean values A,

where `A` is the set of values of the archimedean local factor that finite computations reach: `gamma`,
`pi`, `log` of algebraic numbers, and the polygamma values `psi^(n)(r)` at rational `r`. Three standard facts
(none byte-cited; all to be sourced before any registration) fix its structure.

- **Baker (linear forms in logarithms).** `1, i pi, log 2, log 3, log 5, ...` are linearly independent over
  `Q-bar` (the logarithms of distinct primes are `Q`-linearly independent by unique factorisation, `i pi` is
  not a rational combination of them since `exp` of such a combination is a positive real, and Baker's
  theorem upgrades `Q`-independence to `Q-bar`-independence including the constant 1). So the prime part of
  `L_S` is a **direct sum over the places in `S`**: every element has a well-defined `p`-coordinate for each
  `p in S`. This is the prime-content filtration of `metric-as-state.md` section 3 in transcendence-theoretic
  form: the single-place marginals of `obs:prime-by-prime-blind` are literally the coordinates in the Baker
  basis.
- **Gauss's digamma theorem.** `psi(r/m)` lies in `Q-bar + Q-bar gamma + Q-bar pi + sum Q-bar log(alg)`,
  since `psi(r/m) = -gamma - log 2m - (pi/2) cot(pi r/m) + 2 sum_k cos(2 pi k r/m) log sin(pi k/m)` and
  `2 sin(pi k/m)` is algebraic. So at the level of `psi` the archimedean place adds only `gamma` to the Baker
  span.
- **Polygamma at 1.** `psi^(n)(1) = (-1)^{n+1} n! zeta(n+1)` for `n >= 1`. So the archimedean local factor
  alone produces **every** `zeta(n)`, `n >= 2`. In the notebook's phrase (shard 10, "the only relation between
  primes is additive"), the archimedean place *is* the additive structure, and `sum 1/n^k` is its output.

**What is inside `L_S`, by construction.** Every value `W(f)` for a test function of compact dilation support
whose values at prime powers are algebraic and whose archimedean term reduces to `A` (in particular the
discrete/point-mass test class); every partial Euler product at rational points; every finite Dirichlet
polynomial with algebraic coefficients at algebraic points; `lambda_1 = 1 + gamma/2 - (1/2) log 4 pi`
(`cit:li-criterion`, the first Li coefficient, which sees no prime at all, consistent with the blindness
observation); all `zeta(n)`, `n >= 2`, through the archimedean place.

**What is provably outside `L_S` today: nothing of interest.** This is the central negative finding.

| quantity | status | remark |
|---|---|---|
| `log q`, `q` a prime not in `S` | provably outside `L_S` (Baker) | but says only that the Euler product has a factor at `q` |
| `zeta(2n)` | inside `A` (Euler, Lindemann) | produced by the archimedean place; also by all primes |
| `zeta(3)` | inside `A` via `psi''(1)`; irrational (Apéry); transcendence open | not a separating value |
| `gamma`, `log pi` | inside `A` by definition; transcendence open | |
| `lambda_n`, `n >= 2` (Li) | in the `Q`-span of `1, gamma, log pi, log 2, zeta(j)` and the Laurent coefficients of `zeta'/zeta` at `s = 1` beyond the constant term (Bombieri–Lagarias; local companion `lagarias2005li`; not byte-cited) | those Laurent coefficients (the Stieltjes-type constants) are global, have no known `Gamma`-closed form, transcendence open |
| any zero ordinate `gamma_n` | **not known to be irrational** | no transcendence input exists on the zero side |
| `zeta(1/2)`, `xi(1/2)`, `zeta'(1/2)` | irrationality open | |
| `pi^2` as a `Q-bar`-combination of logarithms of algebraic numbers | excluded by Schanuel's conjecture, not by any theorem known to me | Baker does not apply (the left side is not algebraic) |

So the FNW ingredient 2 is **absent on the zero side**: not a single number attached to the zeros is known to
be irrational, and the symmetric functions of the zeros that the explicit formula produces are combinations
of `gamma`, `log pi`, `zeta(j)` and Stieltjes-type constants whose transcendence is open. On the prime and
archimedean side the known transcendentals (`log p` by Baker, `zeta(2n)` by Lindemann) are each produced by a
**single place**, hence, by `obs:prime-by-prime-blind`, see no zero.

## 4. What the mechanism gives for zeta, at the three levels of the metric problem

**Level 1 and the state (side B, finite bond).** A finite graded bond has a rational zeta
(`prop:trace-supertrace-criterion`) and cannot reach a nonrational `Z`, an atomic prime comb, or infinitely
many divisor points (`obs:factor-by-factor-limits`). Proposition A adds to this a uniform statement, with
`e` replaced by any algebraic functional of the transfer data: *every optimum over a finite bond of an
algebraic variational functional is an algebraic number*. For zeta this is subsumed: the finite bond is
already excluded by the count of zeros, and `zeta(2n)` is reached by the archimedean place regardless. FNW
gives nothing new here beyond the quantitative remark of section 2, transposed: any finite-bond fit of the
first `K` Li coefficients with algebraic data has algebraic optimum, and its distance from the true values is
bounded below by the Diophantine properties of those values (which are unknown).

**Infinite, structured classes.** The classes that matter in the notebook are infinite-dimensional: product
bonds over primes (excluded by `obs:prime-by-prime-blind`), the class-group bond (`def:class-group-bond`,
shard 04p), the adelic Weyl bond (shard 04p and the symplectic-space genesis). Tarski–Seidenberg is
unavailable there. Note that `obs:prime-by-prime-blind` is itself an FNW-type theorem with a different
invariant: the class (product bonds) forces a structural property (spectrum of a partial Euler product), the
target provably violates it (zeta has zeros), and the target is given independently (by the Euler product,
not by the class). The invariant "has zeros" plays the role of "is transcendental". This suggests the useful
generalisation: **for each structured infinite class, find the invariant it forces and the arithmetic fact
that violates it.** The Baker direct-sum structure is the replacement for semialgebraicity: a class whose
outputs lie in `L_S` for a fixed finite `S` is blind to every prime outside `S`, provably, by Baker.

**The metric (Level 3), where the question is not vacuous.** Here the target is implicit (a purification
whose positivity is a theorem) and a candidate class of metrics can be finitely parametrised: the cone of
`thm:arithmetic-metric` on a finite window, the symmetric ray, finite Hodge-type constructions, the
parity-(anti)invariant polarisations of shard 04q. Proposition A applies verbatim to any *algebraic*
invariant of such a class: an optimum, a determinant, a signature-weighted trace. The missing ingredient is
again 2: an invariant of the true metric known to be transcendental. The invariants of the true metric that
are known exactly are the Weil-form values on rational test functions, hence elements of `L_S` plus
Stieltjes-type constants, all of open transcendence status. **The FNW route for the metric is therefore
blocked on a precise open input: the transcendence (or mere irrationality) of one of `gamma`, a Stieltjes
constant, or a zero ordinate.** Any one of these would give the first metric-exclusion theorem of FNW type;
the notebook cannot supply it.

## 5. The MIP* = RE analogy, placed precisely

- **What is rigorous already.** RH is a `Pi^0_1` sentence: it is equivalent to the non-existence of a
  solution of an explicit Diophantine equation (Davis–Matiyasevich–Robinson 1976), and to Lagarias's
  elementary inequality `sigma(n) <= H_n + exp(H_n) log H_n` for all `n` (2002); Kreisel observed the
  `Pi^0_1` form earlier (none byte-cited). The Weil-criterion form in `metric-as-state.md` 7.2 is the same
  fact: a violation is a `Sigma^0_1` event (a computable test function with `W(f * f~) < -2^{-k}` at some
  finite precision), so the set of refutation certificates is recursively enumerable and RH is its
  emptiness. "Refutation finite, proof not" is exactly `Pi^0_1`.
- **Where the analogy breaks.** MIP* = RE is a statement about a *family* (a decision problem over all
  games), proved by reduction from the halting problem via compression and self-testing; its corollary
  (Connes embedding fails) is that the finite-dimensional (tensor-product) values and the commuting-operator
  values of games differ, detected by a computability gap (the first is r.e. from below, the second co-r.e.
  from above through the NPA hierarchy). RH is a *single* sentence, and every quantity attached to zeta is
  computable, so no uncomputability can appear in the single-sentence problem. A family version exists (RH
  for all members of a computable family of `L`-functions; positivity of the Weil form for all test
  functions in a computable class) but is decidable in the trivial way if GRH is true, and is only r.e. if
  it is false. No reduction from the halting problem is in sight, and none is expected: the arithmetic
  objects are too explicit.
- **Where a gap of the MIP* type could live: the noncommutative bond.** The mechanism that makes the two
  values differ needs a *noncommutative* observable algebra. In the dilation-window channel the algebra is
  the convolution algebra of the abelian group `R_+^x`, and there is **no gap**: every positive window has a
  finite-dimensional (finite-atom) extension (`prop:extension-disc`(iii), the Carathéodory–Fejér boundary),
  so the finite-bond and the "commuting" positivity cones coincide level by level. A gap needs the two
  non-commuting families of the adelic picture: dilations by ideles and additive translations, the
  Heisenberg–Weyl algebra over the adeles of the `GL_1` bond round (shard 04p, `def:class-group-bond`,
  `prop:riemann-theta-dilation-bond`, `conj:h-theta`). The MIP*-style statement, in that setting, would be:
  *the arithmetic state on the adelic Weyl algebra is not a weak-* limit of finite-bond states obeying the
  kinematic constraints* (dilation and Weyl covariance, real structure, grading). That is a Level 3
  statement about the bond, of Connes-embedding type. Its negation is also informative: if the arithmetic
  state *is* such a limit, the MaxEnt programme of `metric-as-state.md` 7.3 converges on a sequence of finite
  bonds, and the contradiction search is complete in the limit.
- **The one rigorous consequence for the tomography programme.** The commutative window channel has no
  tensor-versus-commuting gap, so any Tsirelson-type phenomenon for zeta, if it exists, is invisible to Li
  coefficients and dilation windows and requires prime-content observables (the two-prime lattices of
  `metric-as-state.md` 4.2). This is the same conclusion the blindness theorem gave, reached from the other
  side.

## 6. Verdict

The FNW argument is a three-ingredient mechanism (semialgebraic class, transcendental target, implicit
definition). For zeta, ingredient 1 is available for finite bonds (already dead) and for finite-window
metric classes (alive), ingredient 3 is available only for the metric (the state is explicit), and
ingredient 2 is **absent everywhere it would matter**: no zero ordinate, Stieltjes constant or value of the
Weil form on a nontrivial test function is known to be irrational. The finite-prime language is not vague;
it is the `Q-bar`-span of `1`, `log p` (Baker-independent, one direction per prime) and the archimedean
`Gamma`-values, and its provable exclusions all reduce to "the Euler product has infinitely many factors".
A value of zeta outside the language exists conjecturally (Schanuel, the period conjecture) and provably
not at all. The MIP* = RE analogy is exact at the level of `Pi^0_1` versus `Sigma^0_1` and empty at the level
of uncomputability; its live content for this notebook is that a finite-versus-infinite-bond gap can only
appear on the noncommutative adelic bond, never in the window channel.

## 7. Future directions, in order of cost

1. **Register Proposition A** (a two-line theorem with Tarski–Seidenberg) after byte-citing a source for
   quantifier elimination over real closed fields and for the Hulthén value; it is the notebook's first
   exclusion theorem of FNW type and the template for the others.
2. **The Diophantine learning-rate bound** of section 2: effective height bounds for `e_d` plus a
   transcendence measure for `log 2`, giving a rigorous lower bound on matrix-product convergence for the
   Heisenberg chain. Small, self-contained, publishable on its own if the constants can be made explicit.
3. **The Baker grading as a theorem in the notebook:** state and prove that `W` on point-mass test functions
   at prime powers in `S` takes values in `L_S` with the `p`-coordinates given by the local terms, and that
   the grading is the prime-content filtration. Cheap; makes `obs:prime-by-prime-blind` exact at the level of
   numbers.
4. **The open input list**, kept as a standing item: irrationality of any `gamma_n`; transcendence of
   `gamma`; transcendence of the first Stieltjes constant. Any one unlocks a metric-exclusion theorem
   (section 4); none is within reach of this notebook.
5. **The noncommutative gap question** (section 5): formulate "finite-bond approximability of the arithmetic
   state on the adelic Weyl algebra under the kinematic constraints" precisely on the `GL_1` bond of shard
   04p, and test it on the function-field model where the class-group bond is finite (genus one, shard 04p),
   where the answer must be "approximable" and the rate is computable.
