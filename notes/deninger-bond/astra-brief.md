# Brief for the prover: Deninger's package on the GL_1 bond. The two constant terms as H^0 and H^2 with the reference rates, the invariant pairing from the functional equation, the positive compatible metric as RH (the finite criterion transcribed), no bounded metric on the model space even under RH, the Weil form as the canonical point; and the conformal torus map as the CM class-group bond

You are the prover in a mathematical research notebook (git repo, current directory). Author line for
everything you write: `codex:gpt-6-astra`. Write ONLY the file `notes/deninger-bond/astra-proofs.md` (create
it; overwrite if present) and, if you want scratch computations, python files under
`notes/deninger-bond/checks/`. Do not edit anything else. Do not run git. python3 with numpy, mpmath, sympy,
scipy is installed; the first 3000 zeros of zeta are in `data/` (see `scripts/h_theta.py`). Read first:

1. `notes/deninger-lps/src/manuscript.txt` (a general note from a separate Codex conversation on Deninger's
   programme; TeX and PDF beside it): Definition 5.1 (compatible positive polarization `J`, `J^2 = -I`,
   `J^T Omega J = Omega`, `g = Omega(., J.) > 0`), Theorem 5.2 (for `A^T Omega A = q Omega`, `q > 0`: an
   `A`-invariant compatible positive polarization exists iff a real `G > 0` with `A^T G A = q G` exists iff the
   powers of `U = q^{-1/2} A` are uniformly bounded iff `U` is diagonalisable with unimodular spectrum;
   explicit `J = -L R^{-1}`, `L = G^{-1} Omega`, `R = (-L^2)^{1/2}`), Definition 6.1 and Theorem 6.2 (the
   Deninger-type finite package: `H^0 = R`, `H^2 = R eta`, `A_0 = 1`, `A_2 = q`, cup-compatible `A` on `H^1`,
   `Z(u) = det(I - uA)/((1-u)(1-qu))`, roots on `|u| = q^{-1/2}`, functional equation), Proposition 6.3
   (Weil positivity versus polarization), Theorem 7.1 (conformal integral torus maps, `q = a^2 + b^2`,
   `Z_f(u) = (1 - alpha u)(1 - conj(alpha) u)/((1-u)(1-qu))`, `alpha = a + bi`), Section 9 (the anisotropic
   torus `(2x, 3y)` and the cubic graph as obstructions), Proposition 9.3.
2. The notebook: `report/sections/04p_gl1_bond.tex` (the adelic symplectic space as the bond; the GL_1 bond
   `L^2(R_+^x, d^x y)`; the theta bond state, its even sector = the two constant terms `1`, `y^{-1/2}` (poles
   `s = 0, 1`), odd sector `phi = theta - 1 - y^{-1/2}`; `prop:riemann-theta-dilation-bond`; the class-group
   bond and `obs:gl1-bond-no-metric`: at genus one `h = P(1) = N_1` and the metric question is vacuous);
   `report/sections/04q_h_theta.tex`, `report/sections/04r_h_theta_channels.tex` (the weighted theta vector
   `g = y^{1/4} phi`, `ghat`, the symbol `Theta = E^#/E` with `E = xi(1 - 2 i tau)` Hermite–Biehler, the model
   space `K_S`, its compression `Z_t` of the dilation, `thm:model-space-jets`: modes `(log y)^j y^{-(1-sigma)/2
   - i gamma/2} 1_{y>1}` with the stated rates, `prop:kernels-not-riesz`: under RH the kernels are complete and
   minimal but not a Riesz basis, "no boundedly equivalent Hilbert norm makes the modes orthonormal";
   `thm:gl1-bad-zero-defect`; `prop:theta-spectral-density`); `report/sections/02h_definitions_graded_ramanujan.tex`
   (`def:graded-transfer-channel`: the pair of reference rates `(omega_0, omega_1)` whose midpoint is the
   critical line; `def:graded-rh-fe-ramanujan`); `report/sections/04l_elliptic_cavity_channel.tex`
   (`thm:arithmetic-metric`: the cone of metrics with `Z^* H Z = r^2 H`, its symmetric ray, the energy metric
   outside the cone); `report/sections/08c_weil_positivity_continuous.tex` (`obs:kraus-dichotomy`: inverse
   pairing buys the functional equation, adjoint pairing buys reality, unitarity buys both;
   `thm:kraus-weil-criterion`; the Weil/Li/Huang criteria); `notes/weil-positivity.md`; `notes/h-theta/astra-proofs.md`
   (your predecessor's conventions, binding).
3. Sources: `refs/src/math/0001013` (Burnol, causality), `refs/src/math/0311468` (Meyer: the virtual
   representation with poles even and zeros odd), Connes's trace formula paper if present under `refs/src`
   (search for `connes`), Deninger `arXiv:1001.1621` and `math/0204110` are NOT in the repo (mark as not
   byte-cited). Quote by file and line whenever a fact is taken from a source in the repo.

Be explicit. A blind numerics lane will test every displayed identity at the first zeros and a hostile
reviewer will try to refute every claim. Label every claim PROVED, REFUTED, SHARPENED or OPEN. Keep a
correction ledger for this brief. Do not pad. Fix all conventions (direction of the dilation, `y`-picture
versus Mellin picture, inner product linear in the first slot) once, in Section 0 of your file, taking them
from 04q/04r; do not re-derive the previous round.

## 0. Why this round

The finite package of Theorem 6.2 has, in the notebook, an exact infinite-dimensional counterpart on the GL_1
bond: `H^0` and `H^2` are the two constant terms of the theta bond state, `H^1` is the mode space of the
Riemann channel, the multiplier `q` is the ratio of the two reference rates, `A` is the compression of the
dilation. The author of this brief (`claude:fable-5.1`) believes that transcribing Theorem 5.2 line by line
gives (a) "a compatible positive metric exists on the spectral side iff RH and all zeros are simple", the
finite proof surviving verbatim, and (b) a genuinely new obstruction: on the model space `K_S` with the
bond's own Hilbert norm no *bounded* invariant positive metric exists even under RH, because the modes are not
a Riesz basis, so Deninger's Hodge metric on the Riemann channel is necessarily unbounded relative to the
energy metric; and (c) the canonical point of the cone of such metrics is Weil's form (all modes of weight
one), whose positivity is Weil's criterion, so Deninger's package on the GL_1 bond *is* Weil's criterion, with
the trace formula the explicit formula. Prove, refute or sharpen; then do the torus identification of Section 4.

## 1. Deninger data on the bond (fix and prove)

**C1 (the graded data).** With the notebook's forward dilation `U_t` and the outgoing cut, the even sector
of the theta bond state consists of `1` and `y^{-1/2}` with dilation rates `0` and `-1/2` (or the opposite
signs; fix from 04q and say which sign convention makes the pole `s = 1` the top class); the compression `Z_t`
of the dilation to the model space acts on the mode of a zero `rho = sigma + i gamma` by
`e^{-t(1-sigma)/2 - i t gamma/2}` (`thm:model-space-jets`; jets by the Jordan rule). Prove: setting
`H^0 := R * 1`, `H^2 := R * y^{-1/2}`, `A_0 = 1`, `A_2 = q_t := e^{-t/2}` (the ratio of the two reference rates
of `def:graded-transfer-channel`), and `A := Z_t` on the algebraic span `H^1_fin` of the modes of a finite,
functional-equation-closed set of zeros, the multiplier condition `A_2 = q` and "`sqrt q` = `e^{-t/4}` is the
critical modulus" reproduce Definition 6.1's shape exactly, with `Z_t` having all modes of modulus `sqrt(q_t)`
iff every zero in the set has `sigma = 1/2`. (Trivial once the conventions are fixed; the point is to fix them.)

**C2 (the invariant pairing exists because of the functional equation, and is alternating).** Prove: a bilinear
(not sesquilinear) pairing `Omega` on `H^1_fin` with `Omega(Z_t x, Z_t y) = q_t Omega(x, y)` for all `t >= 0`
pairs the mode of `rho` only with the mode of `1 - rho` (compute: the product of the two mode factors equals
`e^{-t/2}` iff `(1 - sigma) + (1 - sigma') = 1` and `gamma + gamma' = 0`); it is nondegenerate iff the set is
closed under `rho -> 1 - rho`, which the functional equation `xi(1 - s) = xi(s)` guarantees for the actual
zeros (this is the "inverse pairing buys the functional equation" of `obs:kraus-dichotomy`, and on the bond it
is the Poisson automorphism `y -> 1/y` of 04p); it can be chosen alternating iff no zero is fixed by
`rho -> 1 - rho`, i.e. no zero at `s = 1/2` exactly with... (careful: `1 - rho = rho` iff `rho = 1/2`, and
`xi(1/2) != 0`; so alternating is always possible; state the sign choice `Omega(e_rho, e_{1-rho}) = sign(gamma)`
and check it is consistent with the reality structure `rho -> conj(rho)`). Give the concrete realisation on the
bond: an explicit formula for `Omega(f, h)` on `K_S` (or on the jets) through the Poisson involution `J_P` and
the real structure, with `Omega(Z_t f, Z_t h) = e^{-t/2} Omega(f, h)`; if the natural formula lives on
`K_S x J_P K_S` rather than on `K_S x K_S`, say so and give the Hankel-type operator that transports it.
State the multiple-zero (jet) version.

**C3 (positive compatible metric on the spectral side iff RH and simple zeros; Theorem 5.2 transcribed).**
Prove: on `H^1_fin` a positive sesquilinear `G` with `G(Z_t x, Z_t y) = q_t G(x, y)` for all `t >= 0` exists
iff every zero of the set has `sigma = 1/2` and is simple. (Necessity: `G(e_rho, e_rho') != 0` forces
`gamma = gamma'` and `sigma' = 1 - sigma`, so `G(e_rho, e_rho) > 0` forces `sigma = 1/2`; a Jordan chain for a
multiple zero has `G(Z_t e_1, Z_t e_1)` growing polynomially in `t` against `q_t G(e_1, e_1)`. Sufficiency:
any positive diagonal `G` in the modes.) Then transcribe Theorem 5.2 (i)–(iv) and the explicit `J = -L R^{-1}`
to this setting and check that `J` is the operator "multiply the mode of `rho` by `+- i` according to the sign
of `gamma`" (the Hodge star of Deninger's `H^1`), that `G J`-positivity is the compatibility of Definition 5.1,
and that `q_t^{-1/2} Z_t` is `G`-unitary: this is the notebook's "RH = the compressed operator is `q^{-1/4}`
times a unitary" (`thm:arithmetic-metric`) made literal on the arithmetic bond. Under RH with simple zeros the
cone of such `G` is all positive diagonal weights `(g_rho)`, with the real structure forcing `g_rho = g_{conj rho}`:
one free scalar per pair `(gamma, -gamma)`; no symmetry acts transitively, so there is no distinguished
"symmetric ray" from symmetries alone (contrast `thm:arithmetic-metric`). PROVE or refute this last sentence.

## 2. The obstruction: no bounded invariant metric on the model space, even under RH

**C4.** Prove: there is no bounded, boundedly invertible, positive operator `G` on `K_S` (the model space with
the bond's Hilbert norm) with `Z_t^* G Z_t = e^{-t/2} G` for all `t >= 0`, even under RH with all zeros
simple. Argument: such a `G` makes `e^{t/4} Z_t` an isometric semigroup for the `G`-inner product; the modes
`k_rho` are eigenvectors with unimodular eigenvalues `e^{-it gamma/2}`, so `<k_rho, k_rho'>_G = e^{it(gamma' - gamma)/2}
<k_rho, k_rho'>_G` for all `t`, hence `G`-orthogonal for `gamma != gamma'`; a bounded invertible `G` making a
complete minimal system orthogonal makes it a Riesz basis in the original norm, contradicting
`prop:kernels-not-riesz`. Handle the details: the domain of the identity (all of `K_S` or the span of the
modes; the modes are complete, so closure works), the case of multiple zeros (already excluded by C3), and
whether "isometric semigroup with complete unimodular eigenvectors" is needed at all (it is not: orthogonality
of eigenvectors of a `G`-isometry with distinct unimodular eigenvalues is elementary). Then state the theorem:
**Deninger's positive Hodge structure on the Riemann channel's model space is never boundedly equivalent to
the energy (bond) metric; the cone of `thm:arithmetic-metric` is disjoint from the bounded equivalence class of
the energy metric in the arithmetic case.** Also prove the semigroup version of Theorem 5.2 (iii): uniform
boundedness of `e^{t/4} Z_t` for `t >= 0` — decide whether it holds under RH (the author expects NOT: it
would give a bounded semigroup with dense unimodular eigenvectors, which does not force a Riesz basis, so
decide it independently, e.g. through the growth of `||Z_t||` from the Blaschke structure of `Theta` and the
zero density `T log T`, or leave OPEN with the exact missing step).

**C5 (the canonical point is Weil's form; Deninger on the GL_1 bond is Weil's criterion).** Prove: on the
spectral space `l^2(zeros)` (Connes's spectral realisation; Meyer's virtual representation), the diagonal
metric with all weights `1` is the one for which the explicit formula is the trace formula
`Str = sum over primes`, i.e. Weil's quadratic form `W(f) = sum_rho fhat(rho) conj(fhat(1 - conj rho))`
(state the exact Weil form used in `08c`/`notes/weil-positivity.md` and match its normalisation) is
`G_Weil(f, f)` under the comparison map `f -> (fhat(rho))_rho`; its positivity on all test functions is Weil's
criterion `<=>` RH (cite the notebook's `thm:kraus-weil-criterion` continuous form and the standard Weil
criterion, not byte-cited). Conclude, as a theorem with precise hypotheses: the Deninger package (Definition
6.1 + Theorem 5.2 data) on the GL_1 bond exists with a bounded metric on the spectral space iff RH, with
`G = G_Weil`, `Omega` the functional-equation pairing of C2, `J` the sign-of-`gamma` star, the trace `tau` on
`H^2` the residue normalisation of the explicit formula; and the comparison map `K_S -> l^2(zeros)`,
`f -> (<f, k_rho>)`, is injective with dense range and unbounded inverse (from C4). One paragraph on what this
says about Deninger's programme in the notebook's language: the missing ingredient is not the metric (it is
forced: Weil's) but a *second* description of `G_Weil` that does not go through the zeros — exactly what the
finite LPS model has (Petersson from an archimedean surface) and the bond lacks; mark this as an observation,
not a theorem.

## 3. What replaces the faces on the bond (ideation, marked as such)

**C6.** The finite square complexes are built from the commutation of two Hecke operators. On the GL_1 bond
the dilations by `log p` and `log q` commute; the "square complex of GL_1 at `(p, q)`" is the action of
`Z^2` on `R_+^x` (or on the idele class group), whose quotient is Deninger's two-prime solenoid. Say, in at
most a page, what horizontal cohomology, transverse transport and Bass doubling become there, whether the
graded zeta of that object is the partial Euler product over `{p, q}` with the even/odd structure of
`def:graded-transfer-channel`, and where finite-dimensionality is lost. Speculation allowed; mark it.

## 4. The conformal torus map is the CM class-group bond (prove; this is exact)

**C7.** Theorem 7.1 of the general note: for `a, b` integers with `q = a^2 + b^2 > 1`, the map `f(z) = alpha z`
on `C/Z[i]` (`alpha = a + bi`) has `Z_f(u) = (1 - alpha u)(1 - conj(alpha) u)/((1-u)(1-qu))`, with the face
pairing = the cup product of the torus, the metric = the flat metric, positivity automatic. Prove: this is
exactly the zeta function of the CM elliptic curve `E: y^2 = x^3 - x` (or its twist) over `F_q` for a prime
`q = 1 mod 4` split in `Z[i]` with Frobenius `alpha` (Deuring; state the exact normalisation of `alpha`, i.e.
which of the associates `+-alpha, +-i alpha` is the Frobenius, a congruence condition on `a + bi`), and
therefore the genus-one class-group bond of shard 04p with `h = P(1) = N_1 = |alpha - 1|^2 = (a-1)^2 + b^2`
(`prop:class-group-bond`, `obs:gl1-bond-no-metric`). Then settle the metric question in this instance: the
flat metric of `C/Z[i]` is the Hodge metric of `H^1(E)`; in the eigenbasis of `alpha` on `H^1 (x) C` it is
the diagonal metric with equal weights on `alpha` and `conj(alpha)`; compare with `thm:arithmetic-metric`'s
symmetric ray for the D2 curve of shard 04l (is the D2 curve `y^2 = x^3 - x` over `F_2`? or which curve; read
04k/04l) and state whether, for the CM torus map, the symmetric ray IS the Hodge (flat) metric: at genus one
this is the vacuous case of `obs:gl1-bond-no-metric` (one free scalar, fixed by reality), so say precisely
what is and is not gained. Bonus, if cheap: the note's Theorem 8.1 (bouquet on two tori with trees, holonomies
`a I + b J`) as the graded-toys network of shards 04n/04o (a core with rays); one paragraph, or skip.

## 5. Output format

`notes/deninger-bond/astra-proofs.md` with: a ledger table (C1–C7, verdicts); full proofs with hierarchical
steps where long; conventions fixed once in Section 0 with references to 04q/04r; every source quote byte-cited
by file and line, external theorems stated precisely and marked "not byte-cited"; a section "Numerical checks
for the blind lane" (explicit: the mode factors at the first three zeros; the pairing and metric matrices on
the six modes `+-gamma_1, +-gamma_2, +-gamma_3` and the check `Omega(Z_t ., Z_t .) = e^{-t/2} Omega` at `t = 1`;
the Weil form on a test function against the sum over 3000 zeros; the CM zeta for `q = 5, 13, 17` with the
point counts `#E(F_q)`); a section "Corrections to the brief"; and a closing "What this changes in the
notebook" with, per claim, the status to register and the one-sentence statement.

## 6. Durability (the network is unreliable today; this is mandatory)

Write your output file **incrementally**: create `astra-proofs.md` with the ledger table (all verdicts
`PENDING`) before you start on the mathematics, and after finishing each claim rewrite the file with that
claim's section and its updated ledger row. Never hold finished work only in memory. If you are resumed after
an interruption (the prompt will say so), read your own `astra-proofs.md` first, keep everything already
written, and continue from the first `PENDING` row. Keep a one-line `notes/deninger-bond/progress.txt` with the
claim you are working on, updated whenever you move to the next claim.
