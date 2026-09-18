REVIEWER: codex:gpt-6 (independent of the continuous author lane; same OpenAI model family)

# Continuous CCM tensor network: adversarial review, round 1

**Stance.** ATTACK under `rk-light`. I independently rederived the Fourier overlap, Loewner
signs, rank-two displacement, rank-one correction, quotient determinant, grid-point cases,
Mellin--Fourier normalization, infinite smeared trace, and exact finite intertwiner. I also audited
the current central definitions in `report/sections/02i_definitions_ccm_tensor.tex` for lockstep
with the proposed continuous claims. I did not use the finite lane as authority and do not promote
any finite-lane claim here.

**Target.** `notes/ccm-tensor-network/continuous.md` (C0--C10) together with the central definition
draft `report/sections/02i_definitions_ccm_tensor.tex`. Primary sources checked directly:
`refs/src/2511.22755/mc2arXiv.tex` and
`refs/src/2511.23257/Araki-final-oct25.tex` at every range listed in C0.

**Outcome.** The mathematical core is strong. C3--C6 survive direct recomputation, including the
signs that are easiest to get wrong. I found two MAJOR integration defects and three MINOR scope or
notation defects. Both MAJORs have local fixes; neither damages the rank-one quotient theorem.

The independent checker
`notes/ccm-tensor-network/review-continuous/check_continuous_r1.py` reports
`26 PASS / 0 FAIL`. Its red mutation reverses the displacement vector and exits nonzero with
`24 PASS / 2 FAIL`, detecting both `[D,T]` and `TDxi=-beta` sign errors.

## Independent recomputation record

1. For zero-extended `U_n=L^{-1/2}exp(2 pi i n x/L)`, direct overlap integration gives

       (U_m^* * U_n)(y)+(U_m^* * U_n)(-y)
       = [sin(2 pi m y/L)-sin(2 pi n y/L)]/[pi(n-m)].

   With `b_n=-pi^{-1} D(sin(2 pi n y/L))`, this is exactly
   `(b_m-b_n)/(m-n)`. Numerical quadrature for three nonsymmetric index pairs agrees below
   `2e-9`.
2. Differentiating the symmetrized overlap at `0+` gives `-2/L` for every pair, diagonal and
   off-diagonal. Since `delta'_0(phi)=-phi'(0+)`, the matrix is
   `(2/L)|eta><eta|`. At `L` every order-zero overlap vanishes. C3's endpoint claims are correct.
3. For C5.3, the independently computed spectrum of `T` is `{0,4,9}`, `Txi=0`,
   `TDxi=-beta`, and `TD'=D'^*T`. The quotient eigenvalues are `+-sqrt(2)`, outside the input grid
   `[-1,1]`. Replacing `Q` by `Q-10I` gives eigenvalues `{-10,-6,-1}` while leaving the shifted
   metric and quotient unchanged.
4. Direct quadrature of the centered multiplicative transform agrees with C5.4 at a generic
   complex point and gives the included-grid values `sqrt(L)(-1)^j xi_j`. The source's
   normalization is also correct: if `<eta,xi>=1` and `delta_N=eta/sqrt(L)`, then the
   `delta_N(xi_b)=1` vector is `xi_b=sqrt(L)xi`.
5. A nontrivial exact-intertwiner test used `L=2 pi`,
   `H=diag(1/2,-1/2)`, and the even polynomial with coefficient vector
   `(3 sqrt(L)/8, sqrt(L)/4, 3 sqrt(L)/8)`. It obeys `xi_b(0)=1`, `A(xi_b)=0`, has a simple Gram
   radical, and satisfies `A(D' f)=H A(f)` for a generic complex coefficient vector. This check
   fixes the minus-sign Fourier convention independently of the prose.

## Objections

### O1. Central Fourier convention is opposite to the continuous proofs

- **Location.** `report/sections/02i_definitions_ccm_tensor.tex`,
  `def:ccm-tn-continuous`, the spectral feature
  `widehat f(omega)=int f(t)e^{+i omega t}dt`; versus continuous D-C4
  (`continuous.md:86-91`), C2.1, C6.1, the `-Im rho` statement in C6, and the integration-by-parts
  identity C7.2, all of which use
  `U(t)=e^{-itH}` and `widehat f(omega)=int f(t)e^{-i omega t}dt`.
- **Severity.** MAJOR (lockstep/sign convention).
- **Independent computation.** For scalar `H=2` and `f(t)=t` on `[0,1]`,
  `int f(t)U(t)dt=int t e^{-2it}dt` equals the minus transform and differs from the plus transform
  by more than `0.5`. With the plus convention, C2 must use `U(t)=e^{+itH}`, C7.2 acquires the
  opposite generator sign, and the zeta counting measure moves from `-Im rho` to `+Im rho`.
  The checker records both the equality and the non-equality.
- **FIX DEMAND.** Choose one convention in the central definition and propagate it verbatim. The
  minimal repair matching CCM and the continuous proof is:

      U(t)=e^{-itH},
      widehat f(omega)=int f(t)e^{-i omega t}dt,
      A_f=widehat f(H).

  Then retain the C6 measure at `-Im rho`. If the plus transform is preferred centrally, change
  the flow to `e^{+itH}`, replace `H` by `-H` in C7.2, and move the measure sign everywhere.
- **SURVIVING WEAKER STATEMENT.** C2 and C6 are correct under either consistent paired convention;
  the present files cannot be merged until the sign is made single-source.

### O2. The exact-intertwiner claim omits the simple-radical hypothesis needed for the CCM quotient

- **Location.** C7 ASSUME block (`continuous.md:499-503`), Step C7 `<1>3`
  (`:519-524`), and the proposed row scope at `:636`.
- **Severity.** MAJOR (quantifier/hypothesis gap).
- **Independent computation.** Take `L=2 pi`, scalar `H=0`, and `E_1=span{U_{-1},U_0,U_1}`.
  The unshifted feature Gram has rank one and lowest eigenvalue `epsilon=0` with a
  two-dimensional radical. The even normalized function `xi(t)=cos t` satisfies `xi(0)=1` and
  `A(xi)=0`, so the displayed integration-by-parts intertwining identity is available. But
  quotienting only by `C xi` leaves a nonzero radical; it is not a Hilbert space and does not map
  isometrically onto `A(E_1)`. The checker verifies rank one and radical dimension two.
- **FIX DEMAND.** Add to the C7 ASSUME block and claim row:

      ker Q_N = ker A = C xi_b

  (equivalently in this context: the zero lowest eigenvalue is simple), together with
  `xi_b(0)=xi_b(L)=1`. Alternatively quotient by the full `ker A`; then the result is an exact
  feature-space intertwiner but need not be the CCM one-line quotient of C4.
- **SURVIVING WEAKER STATEMENT.** Under only `epsilon=0` and `A(xi_b)=0`, the algebraic identity
  `A(D' f)=H A(f)` is correct. Isometry holds from `E_N/ker A` onto `A(E_N)`. Identification with
  `E_N/C xi_b` requires the missing simple-radical hypothesis.

### O3. The regularized-determinant display reuses one symbol for two different operators

- **Location.** C5, `continuous.md:388-400`.
- **Severity.** MINOR (notation with a material spectral distinction already explained in prose).
- **Independent computation.** The full finite rank-one map
  `D-|D xi><eta|` always has the killed vector `xi` and therefore an additional algebraic zero.
  Its quotient has characteristic polynomial C4.2 and need not have zero. In C5.3,
  `P_N(0)=-2`, so the quotient has no zero although the full `D'` does. Therefore one determinant
  cannot literally denote both operators.
- **FIX DEMAND.** Reserve, for example, `D'_full` for the rank-one map on the original Fourier
  space and `D_CCM=(2pi/L)D'' direct-sum D_tail` for the self-adjoint quotient-plus-tail operator.
  Put the regularized determinant only on `D_CCM`. Keep the rank-one formula as the formula that
  induces it.
- **SURVIVING WEAKER STATEMENT.** The phase
  `-i exp(-izL/2) widehat xi_b(z)` is correct for the quotient-plus-tail operator with the stated
  spectral cut; the following prose already says this.

### O4. The fixed-window-limit row and theorem should name reflection invariance explicitly

- **Location.** C9 ASSUME block (`continuous.md:578-586`), Step `<1>3` (`:599-603`), and row scope
  `:637`.
- **Severity.** MINOR (scope precision).
- **Independent computation.** Eventual evenness uses two facts in addition to a gap: every
  finite restriction commutes with Fourier reflection, and the limiting ground state is even.
  These follow when “the half-interval form” means D-C2 with a real distribution and its closure,
  but neither the proposed database scope nor the ASSUME line cites D-C2 or states the commutation.
  A generic closed semibounded form with a simple even ground vector need not have reflection-
  invariant Galerkin restrictions, so Step 3 would then fail.
- **FIX DEMAND.** Begin the claim with “Let `Q` be the closure of the real half-interval form of
  D-C2 (hence reflection invariant), and let the trigonometric polynomials be a form core ...”.
  Add `Q_N gamma=gamma Q_N` to the registered statement or dependencies.
- **SURVIVING WEAKER STATEMENT.** Norm convergence of the ground vectors follows from the form
  core and isolated simple minimum without parity. Eventual evenness and the real-zero conclusion
  require the Loewner/reflection input.

### O5. Three provenance excerpts are too fragmentary to support the proposed rows

- **Location.** C10 provenance table, `continuous.md:651-658`, especially
  `prov:ccm25-convolution-form`, `prov:ccm25-quotient-selfadjoint`, and
  `prov:ccm25-convergence-numerical`.
- **Severity.** MINOR (provenance discipline).
- **Independent computation.** The first excerpt ends with a TeX spacing fragment; the second is
  only “as quotient by null vectors” and omits both the operator and self-adjointness; the third
  stops before the verb “converge”. The source locations are correct, but these byte strings do
  not by themselves support the named cited facts.
- **FIX DEMAND.** Use short complete contiguous excerpts, for example:

  - CCM line 466: `QW(f,g)=\Psi(f^**g)`;
  - CCM lines 863-865: `The operator ... induces a selfadjoint operator ... as quotient by null
    vectors` (retain the exact source TeX between those phrases);
  - CCM line 270: `the spectra of the operators ... converge towards the zeros`.

  Keep each cited-fact statement no stronger than its exact excerpt; numerical convergence remains
  evidence reported by the source, not a theorem.
- **SURVIVING WEAKER STATEMENT.** All cited line/label locations are genuine, and the mathematical
  arguments C3--C5 were independently checked rather than inferred from these fragments.

## Claims adjudication

### `prop:ccm-tn-continuous-smeared-gram`

**PROMOTE scope after O1 lockstep repair:** finite-dimensional `H=H^*`,
`U(t)=e^{-itH}`, `f,g in L^1`, and the minus Fourier transform. Then C2.1 and the unshifted-radical
statement are proved.

`VERDICT prop:ccm-tn-continuous-smeared-gram: HOLD(O1)`

### `prop:ccm-tn-loewner-displacement`

**PROMOTE:** for the real half-interval distribution of D-C2, with one-sided endpoints, the stated
Loewner entries, parity, rank-at-most-two displacement, and endpoint examples are proved. The
displacement may have rank zero, so the target's wording is sharp.

`VERDICT prop:ccm-tn-loewner-displacement: VALID`

### `thm:ccm-tn-loewner-quotient`

**PROMOTE:** under a real symmetric Loewner matrix with a simple reflection-even lowest
eigenvector, `T=Q-epsilon I` has radical `C xi`; the normalized rank-one correction induces a
self-adjoint `2N`-dimensional quotient with characteristic polynomial C4.2 and real roots. No sign
condition on `epsilon` is needed.

`VERDICT thm:ccm-tn-loewner-quotient: VALID`

### `prop:ccm-tn-no-naive-compression`

**PROMOTE:** the displayed `N=1` example has quotient spectrum `+-sqrt(2)`, so it is not an ordinary
orthogonal compression of `diag(-1,0,1)`; the scalar shift independently refutes inference of
unshifted Weil positivity.

`VERDICT prop:ccm-tn-no-naive-compression: VALID`

### `prop:ccm-tn-infinite-smeared-gram`

**PROMOTE exact scope after O1 convention repair:** pure-point self-adjoint `H`, locally finite
counting measure of polynomial growth, and `C_c^infinity` tests. Smeared features are HS, their
cross product is trace class, and raw infinite-dimensional unitaries are not HS.

`VERDICT prop:ccm-tn-infinite-smeared-gram: HOLD(O1)`

### `prop:ccm-tn-exact-continuous-intertwiner`

**HOLD.** Add `ker Q_N=ker A=C xi_b` for the claimed CCM quotient-isometry. With that repair and
the O1 minus convention, promote C7.2 and the invariant function-of-`H` module exactly as written.

`VERDICT prop:ccm-tn-exact-continuous-intertwiner: MAJOR(O1,O2)`

### `prop:ccm-tn-fixed-window-limit`

**HOLD for exact scope repair.** With O4's explicit D-C2/reflection hypothesis, the form-core
Galerkin argument, eventual simplicity/evenness, locally uniform Fourier convergence, and Hurwitz
conclusion are proved. It remains a fixed-`L` theorem and gives no `L -> infinity` or RH result.

`VERDICT prop:ccm-tn-fixed-window-limit: MINOR(O4)`

## Source and non-overclaim audit

- CCM `bombtest`, `formN/basicexpli`, `basics/key`, `four`, and `finmain` support exactly the scopes
  claimed after distinguishing the full rank-one map from its quotient-plus-tail realization.
- CvS `matrixcomp`, `nuance`, `basics-general`, `key-general`, `prop:finmain`, and `main` support the
  half-interval, endpoint, finite quotient, and fixed-window statements. The lane correctly repairs
  CvS `main`'s too-quick parity sentence by using commutation and the spectral gap.
- CCM `dirichlet1` has the correct definition `delta_N=L^{-1/2}sum V_n`; its proof line 989 has the
  factor error identified in C10. No reviewed argument relies on that line.
- No RH assumption is hidden in C3--C5 or C9. C6 marks the Riemann spectral measure realization as
  conditional on RH, and the text correctly states that convergence as `L -> infinity` is absent.
- The unshifted/shifted distinction is maintained correctly: when `epsilon>0`, the natural
  unshifted feature does not kill `xi`; subtracting `epsilon I` constructs a different metric.
- The physical cMPS, doubled transfer, operator-feature, and quotient spaces remain distinct. No
  entanglement-spectrum or physical-odd-block identification is smuggled in.

## Overall verdict

`FAIL(O1,O2)`

The repair is narrow: unify the Fourier sign and add the simple-radical hypothesis to C7. O3--O5
should be fixed in the same pass because they affect lockstep notation, exact claim scope, and
provenance quality. After those deltas, only the changed passages need re-adjudication.

---

## Integration delta pass

**Scope.** While this review was running, the coordinator integrated the continuous material into
`report/sections/03i_ccm_tensor_algorithm.tex` and
`report/sections/03l_ccm_tensor_continuous.tex`, and repaired
`report/sections/02i_definitions_ccm_tensor.tex`. I reviewed those integrated texts directly. This
delta block supersedes the round-1 verdicts above for the integrated artifacts; it does not pretend
that the author-lane file itself was retroactively edited.

### Disposition of round-1 objections

- **O1 — FIXED.** `def:ccm-tn-continuous` now states
  `U(t)=e^{-itH}` and `widehat f(omega)=int f(t)e^{-i omega t}dt`
  (`02i:129-136`). The finite Gram, infinite smearing, and integration-by-parts signs in 03l now
  agree with the single source definition.
- **O2 — FIXED.** The integrated exact-intertwiner theorem begins “In addition to the hypotheses
  of `thm:ccm-tn-loewner-quotient`” (`03l:103-106`). Those inherited hypotheses give
  `ker Q_N=C xi`; with `epsilon=0` and the unshifted Gram realization,
  `ker A=ker Q_N=C xi`, exactly the missing condition. The quotient-isometry conclusion is now
  quantified correctly.
- **O3 — FIXED BY OMISSION.** The integrated algorithm shard does not reuse one symbol for the full
  rank-one map and a regularized determinant of the quotient-plus-tail operator. It states the
  finite quotient polynomial and entire transform, which are the proved pieces needed there.
- **O4 — OUT OF MERGE SCOPE.** The optional fixed-window-limit claim was omitted, as stated by the
  coordinator. It receives no database promotion from this review. If later restored, the O4
  reflection hypothesis remains the required wording.
- **O5 — NOT A CLAIM BLOCKER IN THE SHARDS.** The integrated proofs are complete and use normal
  bibliography citations rather than the three fragmentary provenance proposals. Any future
  `citedfact` database rows should still use the fuller exact excerpts demanded in O5.

### Re-adjudicated positive rows

`VERDICT prop:ccm-tn-continuous-smeared-gram: VALID`

Exact scope: finite-dimensional self-adjoint `H`, minus Fourier convention fixed in 02i, and
compactly supported integrable tests. The operator Gram and its unshifted radical are proved in
03l.

`VERDICT prop:ccm-tn-loewner-displacement: VALID`

Exact scope: the real one-sided half-interval form of `def:ccm-tn-window-form`; the Loewner entries,
reflection, rank-at-most-two displacement, and boundary covector reading are proved in 03i.

`VERDICT thm:ccm-tn-loewner-quotient: VALID`

Exact scope: real Loewner data and an even-simple minimum; the shifted metric, normalization,
rank-one correction, self-adjoint quotient, even characteristic polynomial, and real roots are
proved in 03i without assuming `epsilon>=0`.

`VERDICT prop:ccm-tn-no-naive-compression: VALID`

Exact scope: the displayed `N=1` example. Its quotient polynomial is `s^2-2`, excluding ordinary
orthogonal compression of `diag(-1,0,1)`, and the scalar shift shows real quotient output does not
imply positivity of the unshifted form.

`VERDICT prop:ccm-tn-infinite-smeared-gram: VALID`

Exact scope: a pure-point self-adjoint `H` with locally finite polynomial-growth counting measure
and `C_c^infinity` tests. The smeared operators are Hilbert--Schmidt; their product is trace class;
the unsmeared unitary on an infinite-dimensional Hilbert space is neither Hilbert--Schmidt nor
trace class.

`VERDICT prop:ccm-tn-exact-continuous-intertwiner: VALID`

Exact scope: all hypotheses of the Loewner quotient theorem, a finite self-adjoint `H` realizing
the unshifted window Gram, and `epsilon=0`. The inherited simple radical makes the CCM quotient
isometric to the feature range, and integration by parts proves intertwining of `(2pi/L)D''` with
left multiplication by `H`.

### Adjudication of proposed negative DAG rows

**`obs:ccm-tn-naive-compression` — VALID negative row.** Exact refuted formulation:

> “For every finite CCM Loewner window, the corrected quotient `D''` is an ordinary Euclidean
> orthogonal compression of the input diagonal frequency operator `D`.”

The C5/03i example is a sharp refutation: an orthogonal compression of `D=diag(-1,0,1)` has spectrum
in `[-1,1]`, while the CCM quotient has `+-sqrt(2)`. Surviving statement: `D''` is the quotient of
the rank-one-corrected `D'` in the shifted `T` metric; it is not generally a Euclidean compression.

`VERDICT obs:ccm-tn-naive-compression: VALID`

**`obs:ccm-tn-raw-infinite-gram` — VALID negative row.** Exact refuted formulation:

> “For an infinite-dimensional unitary flow, the unsmeared expression
> `Tr(U(s)^*U(t))` is a finite Hilbert--Schmidt Gram kernel.”

At `s=t`, it is `Tr I=infinity`; indeed every infinite-dimensional unitary has infinite
Hilbert--Schmidt norm and cannot be trace class. Surviving statement: after smearing against tests
whose spectral transforms are square-summable, `F_f` is Hilbert--Schmidt and
`Tr(F_f^*F_g)` is well defined; oscillatory raw traces require a distributional interpretation.

`VERDICT obs:ccm-tn-raw-infinite-gram: VALID`

### Integrated verdict

No FATAL or MAJOR objection remains in the integrated continuous definitions and shards. The two
negative rows above are approved only at the exact refuted scopes quoted here. The optional
fixed-window-limit row remains unadjudicated/omitted, and no convergence-to-zeta or Riemann-bond
claim is promoted.

`PASS (integrated continuous artifacts)`
