<!-- ROLE: live state. UPDATE POLICY: every session end. -->

# HANDOFF — riemann-channel

## Current state (2026-09-12)

Repo created from a single conversation in `../arithmetic-quantum-mechanics`
(session 2026-09-10/11, TJO with Claude Fable 5.1). Everything in this repo
is exploratory. No claims are registered, no checker discipline is in force
yet. The full conversation is in `transcript/transcript.md` (rendered) and
`transcript/session-2026-09-10-be21a927.jsonl` (raw).

### What was established (standard theory, numerically confirmed)

1. **Quantum Ihara–Bass.** For a unital channel with D unitary Kraus
   operators closed under adjoint, the non-backtracking edge superoperator T
   on M_n ⊗ C^D satisfies det(1 − uT) = (1 − u²)^{n²(D−2)/2} det(1 − uDΦ + (D−1)u²).
   Verified to 10⁻¹⁵ (`scripts/qihara.py`). RH for this zeta ⇔ Φ is a
   Ramanujan quantum expander (Hastings' bound). AKLT gives the K₄ Ihara zeta.
2. **Bost–Connes as MPO over the prime chain.** ℓ²(ℕ) = ⊗_p (oscillator at p);
   Gibbs state is a product state; μ_n local; e(a/b) is an MPO with bond
   space ℤ/b whose local transfer map is r ↦ p^k r (Shor's map). Transfer
   eigenvalues in the character basis are L(β, χ̄)/ζ(β). Extremal KMS states
   differ by the boundary residue; β → 1⁺ kills every nontrivial sector.
   Verified against Hurwitz-zeta sums and mpmath L-functions (`scripts/bcmpo.py`).
3. **The Riemann channel.** S(τ) = ξ(1−2iτ)/ξ(1+2iτ) is unimodular on ℝ,
   inner in Im τ < 0, zeros at γ_n/2 − iβ_n/2; its phase equals the imaginary
   part of the β = 1 BC Lévy exponent (prime sum, PNT tail; residual 10⁻³).
   The functional-model semigroup has one mode per zero, decay β_n/2,
   frequency γ_n/2; RH ⇔ uniform rate 1/4 (`scripts/scat.py`).
4. **Ring norms = primes.** Windowed zero sum over 3000 zeros matches the
   full Weil explicit formula to 0.2 on a scale of 147; dips at u = log n of
   depth ∝ Λ(n)/√n including prime powers (`scripts/ringnorm.py`).

5. **Weil–LPS channels built and verified** (2026-09-11, `scripts/weil_lps.py`,
   `notes/weil-lps-channels.md`). For (p; q) in {(5;29), (7;29), (11;5),
   (13;17,29), (17;13), (19;5,17), (29;5,13)}: the q+1 norm-q quaternions map
   into SL₂(F_p); the Weil representation is built numerically with the
   intertwining relation checked to 10⁻¹⁴; the channels on the even and odd
   Weil blocks are Ramanujan quantum expanders in every case (Hastings bound),
   with a unique fixed point; Harrow containment in the PSL₂ Cayley spectrum;
   Hecke relation A_q² − qI = A_{q²} and multiplicativity A_{q1}A_{q2} = A_{q1q2}
   exact; channels for different q commute to 10⁻¹⁵; the direct edge
   superoperator for (13,17) has |μ| ∈ {17, √17, 1}, so its quantum Ihara zeta
   satisfies RH exactly. Not done: LMFDB identification of the joint spectrum.

6. **MPS formulation of the Weil conjectures for quadratic Artin–Schreier
   curves** (2026-09-11, `scripts/artin_schreier_mps.py`,
   `notes/artin-schreier-mps.md`). In a normal basis Frobenius is the cyclic
   shift; for g(x) = Σ a_j x^{1+q^j} the exponential sum S_n is Tr(Eⁿ) for a
   q^J × q^J transfer matrix (odd n exactly; even n with the sign that makes
   S_n = −Σ α_iⁿ). E E† = q I whenever a_J ≠ 0, so RH is manifest: the
   transfer matrix is √q times a unitary. Beyond quadratic g the trace form
   is non-local and n-dependent in the shift basis; the uniform formulation
   is Dwork's p-adic transfer operator, which gives rationality and the
   functional equation but not RH.

### What is NOT established

- RH. Everything above is equivalent to, not a proof of, the uniform-rate
  statement.
- A Stinespring form of the compressed semigroup Z(t) with the prime
  dilations as jump (Kraus) operators. This is the open question isolated by
  `notes/riemann-channel-note.md` §7.
- Any identification with the Phantasm constructions in the parent repo
  (SP-PRIME, SP-BC-CONTROL are β > 1 objects).

### Ideas raised but not pursued

- Selberg as the continuum limit: MPS matrices ↔ flat U(χ) connection on a
  hyperbolic surface, rings ↔ closed geodesics, twisted Selberg zeta =
  one-loop determinant (D'Hoker–Phong, Sarnak). TJO flagged the functional
  integral framing as going too far; the "length quantisation is a flatness
  condition" reading was later matched by the product formula ∏_v |p|_v = 1.
- Shor's unitary U_a : x ↦ ax mod N is the level-N Galois symmetry of BC and
  a single-time snapshot of the dilation flow; its periods are governed by
  Dirichlet L-function zeros, not ζ's.
- Holevo's Lévy–Khinchin classification of dilation-covariant CP semigroups
  gives the *form* of any quantum lift of BC: prime jumps + Gaussian
  (archimedean) part + Hamiltonian part. Dilation theorems supply existence
  only; positivity (Weil's criterion) is where RH lives.

7. **Deligne's proof via graphs** (2026-09-12, `notes/deligne-via-graphs.md`,
   expository). The three ingredients a Hilbert–Pólya approach would have to
   replace: products (eigenvalues multiply, trivial loss fixed), slicing over
   a curve (the core theorem is about a curve with matrix coefficients, i.e.
   a twisted Ihara zeta), and the sign (interesting eigenvalues are zeros,
   not poles). Deligne exhibits no Hermitian form; Weil and Artin–Schreier do.

### Discussion 2026-09-12: circle flows

Direct sum over $p$ of rotations on circles of circumference $\log p$ has
trace $\sum_n \Lambda(n)\delta(s - \log n)$ (Poisson), dynamical zeta =
Euler product; it is side A. For finite sets of primes its spectrum is the
poles of the partial Euler product; zeros exist only in the infinite
product. Prime-by-prime ansätze (direct sums, commuting dilations) cannot
see zeros. See `docs/worklog/2026-09-12.md`.

## Steering 2026-09-11 (TJO)

TJO's deepest learning from the founding session: **RH is a Ramanujan
property**, and this gives cautious optimism because the quantum-expander
literature supplies a wealth of constructions to tinker with. Claude's
assessment, recorded for the next session:

- The equivalence chain is theorem-level at every link (Ihara/Sunada;
  quantum Ihara–Bass, to be written as a lemma; Faddeev–Pavlov for ζ).
- Ramanujan-ness has exactly three known sources: arithmetic (LPS via
  Deligne), probabilistic-asymptotic (Friedman, Hastings; "nearly", ε → 0),
  and interlacing families (Marcus–Spielman–Srivastava; real-rootedness of
  expected characteristic polynomials, no arithmetic). MSS is the one whose
  shape matches "the Hilbert–Pólya operator H is Hermitian"; Montgomery–
  Odlyzko is the hint that ξ could be an expected characteristic polynomial.
- Obstruction: the prime dilations commute, and abelian Cayley graphs are
  never expanders. LPS resolves the analogous problem: Hecke operators T_q
  also commute, and expansion comes from the arithmetic quotient. The joint
  spectrum of the commuting family is the content (Hecke eigenvalues there,
  zeros here).

**Proposed first tinkering object (Weil–LPS channels).** Harrow's
construction with G = SL₂(F_p), S = LPS generators for a prime q, π = the
Weil representation on ℓ²(F_p): Φ_q(ρ) = (1/|S|) Σ_{s∈S} π(s) ρ π(s)†.
Exactly Ramanujan (LPS + Deligne), commuting for different q, jointly
diagonal with spectrum given by Hecke eigenvalues of weight-2 forms of
level p (Eichler–Shimura). Its quantum Ihara zeta is an Artin–Ihara
L-function twisted by Ad(Weil) and satisfies RH. Compute for p = 5, 7, 11,
13 and q = 2, 5; verify the Hastings bound numerically; compare the joint
spectrum with LMFDB Hecke eigenvalues. This lands on the parent campaign's
SP-WEYL Hilbert space and is the concrete link between the two repos.

## Next useful steps, in order

1. **Weil–LPS channels, part 2.** Built and verified (item 5 above). Remaining:
   identify the joint spectra (13;17,29), (19;5,17), (29;5,13) with Hecke
   eigenvalues of weight-2 forms for the quaternion algebra ramified at {2,∞}
   via LMFDB; write the quantum Ihara–Bass lemma as a proof; decide what
   "assemble over p" should mean (the DG-GLOBAL question in this guise).
2. **The Stinespring question.** Write the compressed semigroup Z(t) on K_S
   explicitly (functional model, Cauchy kernels) and test whether a generator
   of Holevo jump form with jumps at k log p reproduces it on K_S. A negative
   answer with a reason is a result. Suggested: codex lane, gpt-5.6-sol xhigh,
   blind, with the note as the only input.
3. **Tighten §4 of the note.** The "bridge" statement (LP = BC at β=1 +
   Sz.-Nagy–Foias) is stated at the level of the boundary phase. Write the
   innerness argument in full (Phragmén–Lindelöf in Im τ < 0) rather than
   citing Lax–Phillips.
4. **Decide the repo's rules.** If this becomes more than a notebook, import
   the parent's PRD (red-green checkers, claims DAG, definitions file) before
   anything is called a claim.
5. **Remote.** Public at github.com/tobiasosborne/riemann-channel (AGPL-3.0), created 2026-09-12.

## Environment

python3 with numpy, mpmath, sympy. `fmd-report` renders `notes/*.md` to HTML
with MathML verification. Zeros: `mpmath.zetazero(n)`, ~0.5 s each near
n = 3000; `data/zeros3000.npy` caches the first 3000.
