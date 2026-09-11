<!-- ROLE: live state. UPDATE POLICY: every session end. -->

# HANDOFF — riemann-channel

## Current state (2026-09-11)

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

## Next useful steps, in order

1. **The Stinespring question.** Write the compressed semigroup Z(t) on K_S
   explicitly (functional model, Cauchy kernels) and test whether a generator
   of Holevo jump form with jumps at k log p reproduces it on K_S. A negative
   answer with a reason is a result. Suggested: codex lane, gpt-5.6-sol xhigh,
   blind, with the note as the only input.
2. **Tighten §4 of the note.** The "bridge" statement (LP = BC at β=1 +
   Sz.-Nagy–Foias) is stated at the level of the boundary phase. Write the
   innerness argument in full (Phragmén–Lindelöf in Im τ < 0) rather than
   citing Lax–Phillips.
3. **Decide the repo's rules.** If this becomes more than a notebook, import
   the parent's PRD (red-green checkers, claims DAG, definitions file) before
   anything is called a claim.
4. **Remote.** No git remote yet. `gh repo create tobiasosborne/riemann-channel --private --source=. --push` when wanted.

## Environment

python3 with numpy, mpmath, sympy. `fmd-report` renders `notes/*.md` to HTML
with MathML verification. Zeros: `mpmath.zetazero(n)`, ~0.5 s each near
n = 3000; `data/zeros3000.npy` caches the first 3000.
