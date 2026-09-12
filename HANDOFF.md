<!-- ROLE: live state. UPDATE POLICY: every session end. -->

# HANDOFF — riemann-channel

## Current state (2026-09-12, night)

Repo created from a single conversation in `../arithmetic-quantum-mechanics`
(session 2026-09-10/11, TJO with Claude Fable 5.1). Everything in this repo
is exploratory. No claims are registered, no checker discipline is in force
yet. The full conversation is in `transcript/transcript.md` (rendered from
the raw session log, which is kept out of the repository).

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

8. **Prior art and the general Kraus Ihara–Bass formula** (2026-09-12,
   `notes/prior-art-quantum-ihara.md`, `notes/quantum-ihara-general.md`,
   `refs/`). Literature check with byte-verified TeX quotes: the
   Ad(U)-weighted Ihara zeta and its Bass formula are Matsuura–Ohta 2022
   (arXiv:2204.06424); arbitrary-weight Bass for loopless graphs is
   Watanabe–Fukumizu 2011; twisted zetas go back to Sunada 1986. NOT found:
   any zeta of a quantum channel, "RH ⇔ Ramanujan quantum expander", the
   MPS/ring-norm reading. Exactly-Ramanujan channels from LPS via Harrow are
   in Iyer–Jain–Jordan–Somma arXiv:2602.15180 (SU(2) irreps); the Weil
   instance is ours. Then proved: Ihara–Bass for the non-backtracking
   superoperator of an ARBITRARY Kraus family (Theorem 1, Lamport proof,
   Corollaries 2–4: adjoint pairing + positive trace formula; unitary case;
   pole bookkeeping). Numerics float 1e-15 and exact sympy. Adversarial
   review by Opus (author Fable): round 1 algebra VALID, provenance fixes
   applied; round 2 receipt in `notes/reviews/round2-2026-09-12.md`.
   Convention: status `proved` requires a reviewer ≠ author; both are Claude
   models (single family declared), no codex lane used.

9. **The continuous (Selberg) dictionary** (2026-09-12 night,
   `notes/selberg-dictionary.md`, `notes/selberg/astra-proofs.md`, lab-book
   shards 09b/09c, `scripts/selberg_lindblad.py`). Proved by the codex prover
   (`gpt-6-astra`), reviewed by Opus: circle comb and its blindness to zeros
   (orbital trace only); Lindbladian of the sl2 vector fields = 2Ω = −2Δ on
   the K-invariant sector (Casimir has the compact direction with a minus
   sign); Poincaré Jacobian 4 sinh²(kℓ/2); flat trace ↔ tower
   D(ς)=∏_{j≥1}Z(ς+j) with Λ_fl = +D'/D; tower zeros in bands −½−k±ir_j,
   nonconstant first band on Re ς = −½ iff no eigenvalue in (0,¼); Ruelle =
   Z(s)/Z(s+1); modular cusp term = prime comb with dips Λ(n)/n at 2 log n
   plus an exact +½ from the pole of ζ; e^{−t/4}·(channel prime measure) =
   cusp prime measure. Six standard inputs are `assumed` rows (dependants
   print -conditional). Open: conj:quantum-lindblad-gap (the continuous
   Harrow construction, gap of 2Ω_{π⊗π̄} + ½B_W²), and an operator-level
   continuous Ihara–Bass (the tower as a Laplacian determinant). Opus REFUTE
   review: 13/13 VALID (`notes/reviews/selberg-2026-09-12.md`). Two action
   items from the review: (a) H-SZ (Selberg zeta entire with full divisor)
   and H-LAP have no byte-cited quote; fetch a source and convert the
   `assumed` rows to `cited`, which lifts the -conditional suffix; (b) the
   reviewer confirms that `notes/riemann-channel-note.md` §5's prime weight
   +Λ(n)n^{-1/2} is off by a factor −2 against the note's own explicit
   formula and double-counts the e^{-t/4} damping: correct §5 of that note
   (shard 04 already carries the corrected statement via prop:damping-identity).

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
   via LMFDB; decide what "assemble over p" should mean (the DG-GLOBAL
   question in this guise). The Ihara–Bass lemma is done (item 8), in the
   general Kraus form; cite Matsuura–Ohta for the unitary case.
1b. **Continuous Harrow channel (was conj:quantum-lindblad-gap).** Assessment
   2026-09-12 night: not hard, theorem-shaped. On each constituent σ of π⊗π̄
   and diagonal K-type m, −𝓛 = 2λ_σ + m²/2 with λ_σ = s_σ(1−s_σ), so
   gap = min(½, 2·s(1−s) over complementary-series constituents); for
   tempered π the spherical part of π⊗π̄ is tempered (Cowling–Haagerup–Howe:
   L^{2+ε} coefficients) and the gap is exactly ½ = 2·¼, the continuous
   Ramanujan value; e^{t𝓛} is a mixed-unitary channel averaged over the
   hypoelliptic heat kernel of ½(H²+E²) (Nelson, Hörmander). Complementary
   π_s: Repka 1978 decides when π_s⊗π_s contains π_{2s−1} (threshold s>¾ from
   memory, must be byte-checked). The SL(2,F_p) half of the conjecture is
   void (no vector fields; that case is Harrow + LPS, item 5). To do: fetch
   Nelson/CHH/Repka TeX, restate as a theorem with the gap formula, run the
   codex prover, Opus refute. The real difficulty is the lattice version
   (gap of −2Δ on Γ\H = 2λ₁, Ramanujan ⇔ Selberg ¼), already the first-band
   criterion of shard 09c; a quantum (operator-level) lattice version is not
   yet formulated.
1a. **General Kraus zeta, part 2.** Theorem 1 replaces (D−1)u² by 𝒟(u) and
   uDΦ by 𝒜(u). Open: what "Ramanujan" means without the relation μμ' = D−1;
   whether canonical form Σ A_k†A_k = 1 constrains the poles; whether the
   Bartholdi deformation (Matsuura–Ohta arXiv:2208.14032) helps. A
   counterexample hunt (random MPS, pole radii of ζ) is cheap.
2. **The Stinespring question.** Write the compressed semigroup Z(t) on K_S
   explicitly (functional model, Cauchy kernels) and test whether a generator
   of Holevo jump form with jumps at k log p reproduces it on K_S. A negative
   answer with a reason is a result. Suggested: codex lane, gpt-5.6-sol xhigh,
   blind, with the note as the only input.
3. **Tighten §4 of the note.** The "bridge" statement (LP = BC at β=1 +
   Sz.-Nagy–Foias) is stated at the level of the boundary phase. Write the
   innerness argument in full (Phragmén–Lindelöf in Im τ < 0) rather than
   citing Lax–Phillips.
4. **Repo rules: decided 2026-09-12 evening.** The lab book `report.tex`
   with shards under `report/sections/`, the four databases under `db/`
   (notation, definitions, claims, provenance), the gate
   `scripts/labbook_check.py` and the local CI `scripts/ci_local.sh`
   (pre-commit via `make hooks`) are the discipline from now on. A statement
   is a claim only when it has a row in `db/claims.tsv`; `proved` needs a
   reviewer file; every quote needs a provenance row. Notes under `notes/`
   stay free-form but every note must be distilled by a shard (the gate
   checks both directions).
5. **Remote.** Public at github.com/tobiasosborne/riemann-channel (AGPL-3.0), created 2026-09-12.

## Environment

python3 with numpy, mpmath, sympy. `fmd-report` renders `notes/*.md` to HTML
with MathML verification. Zeros: `mpmath.zetazero(n)`, ~0.5 s each near
n = 3000; `data/zeros3000.npy` caches the first 3000.
