# Adversarial review: Theorem 1 and Corollaries 2–4 of `notes/quantum-ihara-general.md`

Reviewer: REFUTE-stance verifier (not the author of the proof). Date 2026-09-12.
Stance: attack the algebra; default INVALID when uncertain. Everything below was
re-derived or recomputed independently of `scripts/qihara_general.py`.

## 0. Summary

I could not break Theorem 1. Every Lamport step ⟨1⟩1–⟨1⟩8 was re-derived by hand,
and the identity was re-verified symbolically from the *statement* (not from the
author's code) on nine instances including the cases the author's script does not
cover (D = 2; nilpotent E; zero E; non-diagonalisable E; singular E; u = 0; u far
outside the Neumann disc; a second involution pattern (1 3)(2 4)). The specific
attack vectors listed in the review brief were all checked and all of them fail to
land — see §3. What remains are four MINOR, cosmetic issues.

## 1. Issues

**I1. `⟨1⟩8` / Theorem 1 statement — the "identity of rational functions" clause is
redundant and mildly misleading. Severity MINOR (cosmetic).**
Steps ⟨1⟩1–⟨1⟩7 are pure finite-dimensional linear algebra: each is valid *pointwise*
at any single `u` satisfying ASSUME, and nothing in them needs `|u|` small, a Neumann
series, or analytic continuation. ⟨1⟩8 then says "the identity of rational functions
follows because both sides are rational in `u` and agree on a disc", which reads as if
the algebraic identity were only established on a disc and then continued. It is not:
the ASSUME set is the complement of the zero set of the polynomial
`Π_p det(1 − u²E_ī E_i)` (non-zero, since it equals 1 at u = 0), hence cofinite, and
the identity holds at every point of it directly.
*Fix:* replace the last sentence of ⟨1⟩8 by: "⟨1⟩1–⟨1⟩7 hold at every `u` satisfying
ASSUME. The ASSUME set is cofinite (the excluded set is the zero locus of a polynomial
that is 1 at u = 0), and contains the disc `|u| < (max_i‖E_ī E_i‖)^{-1/2}` by the
Neumann series; both sides are rational, so the identity is an identity of rational
functions." Verified numerically at `|u|/r` up to 32 outside the Neumann disc
(rel. err ≤ 1e-14), so the pointwise reading is the right one.

**I2. Theorem 1 statement — the bound `|u| < min_i ‖E_ī E_i‖^{-1/2}`. Severity MINOR
(cosmetic).**
(a) Undefined when some `E_ī E_i = 0` (e.g. nilpotent Kraus data, or `A_k = 0`); needs
the convention `0^{-1/2} = ∞`. (b) `min_i ‖E_ī E_i‖^{-1/2} = (max_i ‖E_ī E_i‖)^{-1/2}`,
which is the clearer way to write it. (c) `‖·‖` must be a submultiplicative
(e.g. induced) norm for the Neumann series step; the note never says which norm.
*Fix:* write `|u| < (max_i ‖E_ī E_i‖)^{-1/2}` with `‖·‖` the operator norm and
`(0)^{-1/2} := ∞`.

**I3. Corollary 3 proof — division by `1 − u²` without stating the exclusion.
Severity MINOR (cosmetic).**
The derivation writes `A(u) = uΣ/(1−u²)`, `D(u) = Du²/(1−u²)` and
`det(1+D−A) = (1−u²)^{-N} det(1−uΣ+(D−1)u²)`, all of which require `u² ≠ 1`; the stated
conclusion is an identity of polynomials. It does extend to `u² = ±1` by continuity
(both sides are polynomials agreeing off a finite set), but the corollary as written
never says so, and the hypothesis of Theorem 1 genuinely fails at `u² = 1` here.
*Fix:* append "for `u² ≠ 1`, hence for all `u` since both sides are polynomials."
(Verified symbolically for D = 2, 4, 6 with N = 2: `det(1−uT) = (1−u²)^{N(D−2)/2}
det(1−uΣ+(D−1)u²)` exactly, including at u = ±1.)

**I4. Corollary 4 — "as they partly do in Corollary 3" is false at D = 2.
Severity MINOR (cosmetic).**
At `D = 2` the exponent is `N(D−2)/2 = 0`: the cancellation `ND/2` against `−N` is
*total*, not partial. ("Partly" is correct for D ≥ 4.)
*Fix:* "…as they do in Corollary 3, completely when D = 2 and partially when D ≥ 4."
Secondary nit, same step: the written justification ("each factor is analytic away
from the points named") skips the case where the second factor has a *pole* at some
`u₀`; there the conclusion still holds because `det_W(1−uT)` is a polynomial, so
`Π_p det(1−u²E_ī E_i)` must vanish at `u₀`, putting `u₀` in the named set anyway.
Worth one sentence.

No BLOCKER and no MAJOR issues found.

## 2. Independent instances computed

All in `notes/reviews/scratch_thm1_indep.py`, `scratch_thm1_edge.py`,
`scratch_cor2.py`, `scratch_outside.py` — written from the note's *statement*, with
`T` built as `T[block j, block i] = E_i` for `j ≠ ī` (which is what
`T(v⊗|i⟩) = Σ_{j≠ī} E_i v ⊗ |j⟩` means) and the RHS built with `E_ī E_i` in that order
and the inverse multiplied **on the right**.

| instance | outcome |
|---|---|
| **D = 2, N = 1, fully symbolic** (`e₁,e₂,u`): T = diag(e₁,e₂), LHS = (1−ue₁)(1−ue₂). RHS = (1−u²e₁e₂)·[1 − u(e₁+e₂) + u²e₁e₂]/(1−u²e₁e₂) | **equal** ✓ |
| **D = 2, N = 2, fully symbolic** (8 free entries, non-commuting — this is the instance that would expose a left/right or E_i↔E_ī ordering error, and the author's script never tests D = 2) | **equal** ✓ |
| **D = 4, N = 1, fully symbolic** (`f₁..f₄`), σ = (1 2)(3 4): both sides equal `1 − Σf_i u + (f₁f₂+f₃f₄)u² + Σ_{|S|=3}f_S u³ − 3f₁f₂f₃f₄u⁴` | **equal** ✓ |
| D = 4, N = 1 symbolic with the *other* pairing σ = (1 3)(2 4) | **equal** ✓ |
| D = 4, N = 2 and D = 6, N = 2, exact rationals | **equal** ✓ |
| **Discrimination control**: same tests with `(1−u²E_i E_ī)^{-1}` substituted inside A and D | **unequal** — tests are ordering-sensitive ✓ |
| **Discrimination control**: same tests with the resolvent multiplied on the left | **unequal** — tests are side-sensitive ✓ |
| edge: all `E_i = 0` (D=4) | equal (both = 1) ✓ |
| edge: nilpotent `E` with `E_ī E_i = 0` (D = 2 and D = 4) | equal ✓ |
| edge: non-diagonalisable (Jordan) `E`, D = 4 | equal ✓ |
| edge: singular rank-1 `E₁`, D = 2 | equal ✓ |
| edge: `E_i = 0` at one index only, D = 4 | equal ✓ |
| edge: `u = 0` | both sides 1 ✓ |
| `u` admissible but far outside the Neumann disc (`|u|/r` = 2.7, 9.9, 17, 32) | equal to 1e-14 ✓ |
| degree check: `det_W(1−uT)` has degree exactly `ND` generically (leading coeff = (−1)^{ND} det T) — "≤ ND" is correct | ✓ |
| **Cor 2 trace formula** as literally stated, `ℓ = 1..5`, D = 4, n = 3: `Tr_W T^ℓ` vs `Σ |Tr(A_{i_ℓ}⋯A_{i_1})|²` over `i_{k+1} ≠ ī_k` cyclically | **equal** to 1e-14, real and ≥ 0 ✓ |
| **Cor 2 Euler product** truncated at `|w| ≤ 6`, u = 0.05: `Π_{[w]} det(1−u^{|w|}Ad(A_w))^{-1}` vs `det(1−uT)^{-1}` | agrees to 1e-8, converging ✓ |
| **Cor 2 norms**: `‖Ad(A†A)‖ = ‖A‖⁴`, spectrum real and ≥ 0 | ✓ |
| **Cor 3**, D = 2, 4, 6 with `E_ī = E_i^{-1}` exact rationals | ✓ |
| author's `scripts/qihara_general.py` re-run | all pass, ≤ 3e-15 |

## 3. Attack vectors from the brief, and why each fails

- **"invertibility of `1 − u²E_ī E_i` at the index ī used but not declared" — does not
  land.** ⟨1⟩4 needs `Q = (1−u²E_i E_ī)^{-1}`, which is the hypothesis evaluated at the
  index `ī ∈ [D]` (since `σ(ī) = i`), and the hypothesis is stated "for every `i ∈ [D]`".
  The proof says exactly this. It is in fact *weaker* than needed: `det(1−BC) = det(1−CB)`
  already makes the hypothesis at one representative of each pair imply it at the other,
  so "for all i" could be relaxed to "for one i per pair" without changing anything.
- **Ordering in the block product / which component gets which E — does not land.**
  `J(v⊗|i⟩) = E_i v⊗|ī⟩` sends component i to component ī via `E_i`, so on the ordered
  basis (component at i, component at ī) the matrix is `[[0, E_ī],[E_i, 0]]`: correct, the
  off-diagonal entry in *row i* is what acts on the component at ī. The inverse in ⟨1⟩4
  was re-multiplied by hand and by sympy. ⟨1⟩6's assignment of `(E_i − uE_ī E_i)P` to the
  index `i` and `(E_ī − uE_i E_ī)Q` to the index `ī` is correct because
  `Q = (1 − u²E_{σ(ī)}E_ī)^{-1}`. My D = 2, N = 2 fully symbolic test is exactly the
  minimal instance that would catch any such transposition, and it passes; the two
  deliberately-wrong variants I wrote both fail, so the test is discriminating.
- **Missing case D = 2 — does not land.** The author's script never tests it, so I did:
  `T = diag(E₁, E₂)` and the single pair factor `det(1−u²E₂E₁)` cancels exactly against
  the denominator of the second factor, symbolically, for N = 1 and N = 2. ⟨1⟩1–⟨1⟩7 make
  no use of D > 2.
- **Nilpotent / non-diagonalisable / singular E, u = 0 — do not land.** The whole proof is
  determinant-and-inverse algebra; no spectral hypothesis is used anywhere. Verified.
- **Sylvester misapplied (dimensions of X: V→W, Y: W→V) — does not land.**
  In ⟨1⟩5, `X = u(1+uJ)^{-1}S : V→W` and `Y = R : W→V`, so `det_W(1−XY) = det_V(1−YX) =
  det_V(1 − uR(1+uJ)^{-1}S)`. Directions and spaces are right.
- **"Product over unordered pairs well defined" — does not land.**
  `det(1−u²E_ī E_i) = det(1−u²E_i E_ī)` by Sylvester, which the note states.
- **Cor 2 `Ad(A†A)` positivity and norm — does not land.** `⟨ρ, Ad(P)ρ⟩_HS = ‖P^{1/2}ρP^{1/2}‖²_HS ≥ 0`
  for `P ≥ 0`; `Ad(P) = P̄⊗P` has eigenvalues `p_a p_b ≥ 0`; `‖Ad(A†A)‖ = ‖A†A‖² = ‖A‖⁴`.
  Confirmed numerically.
- **Cor 2 direction of `i_{k+1} ≠ ī_k` versus the order `A_{i_ℓ}⋯A_{i_1}`, and the cyclic
  condition — do not land.** Induction gives `T^ℓ(v⊗|i_1⟩) = Σ E_{i_ℓ}⋯E_{i_1}v ⊗ |i_{ℓ+1}⟩`
  over `i_{k+1} ≠ ī_k`, `k = 1..ℓ`; the trace sets `i_{ℓ+1} = i_1`, adding exactly
  `i_1 ≠ ī_ℓ`, i.e. `k ∈ ℤ/ℓ`. Checked against `Tr T^ℓ` for `ℓ = 1..5`. (At `ℓ = 1` the
  condition is `i_1 ≠ ī_1`, vacuous since σ is fixed-point-free, and indeed
  `Tr T = Σ_i Tr E_i = Σ_i |Tr A_i|²`.)
- **Cor 2 Euler regrouping — does not land.** A primitive cyclic word `w` of length `d` has
  exactly `d` distinct rotations, so `Σ_ℓ (u^ℓ/ℓ)Σ_{|seq|=ℓ} Tr E_seq =
  Σ_{[w]}Σ_k (u^{kd}/(kd))·d·Tr(E_w^k) = Σ_{[w]} −log det(1−u^{d}Ad(A_w))`. Checked numerically.
- **Cor 3 exponent arithmetic — does not land.** `m = D/2` pair factors `(1−u²)^N` give
  `(1−u²)^{ND/2}`; the second factor contributes `(1−u²)^{-N}`; `ND/2 − N = N(D−2)/2`. ✓
- **Cor 4 cancellation remark — lands only as the cosmetic I4 above.**

## 4. Audit of `scripts/qihara_general.py`

The script tests the theorem **as stated**, with one gap in coverage.

- `hashimoto`: `T[j*N:(j+1)*N, i*N:(i+1)*N] = Es[i]` for `j ≠ inv[i]` — column block `i`,
  row block `j`, i.e. `T(v⊗|i⟩) = Σ_{j≠ī} E_i v⊗|j⟩`. **Consistent** with the note.
- `rhs`: `pairs = {tuple(sorted((i, inv[i])))}` — genuinely one factor per unordered pair,
  and `det(I − u²·Es[b]@Es[a])` with `b = ā`, i.e. `det(1 − u²E_ā E_a)`. **Correct order**,
  and order-independent anyway by Sylvester.
- `rhs`: `M = Σ_i (Es[i] − u·Es[inv[i]]@Es[i]) @ inv(I − u²·Es[inv[i]]@Es[i])` — this is
  ⟨1⟩6 verbatim, `E_ī E_i` in the right order and the resolvent on the **right**.
  Equals `1 − uM = 1 + D(u) − A(u)`, so it tests the theorem's RHS, not a variant.
- `trace_formula`: `P = Es[i] @ P` accumulating left-to-right gives `E_{i_ℓ}⋯E_{i_1}`, and
  `all(w[(k+1)%m] != inv[w[k]])` is the cyclic condition. **Consistent**. It checks the
  `Tr_V E_w` form; the step `Tr_V Ad(A_w) = |Tr A_w|²` is not exercised (I checked it
  separately, §2).
- Coverage gap: every case uses `D = 4` or `D = 6`, `inv` of the form `(i+m)%D` or
  `(0 1)(2 3)`. **`D = 2` is never tested**, nor are singular/nilpotent/zero `E`, nor `u`
  outside the Neumann disc. I covered all of those; they pass. Recommend adding a `D = 2`
  line to the script.
- Minor: `exact_check` draws random rationals from a numpy RNG that is also consumed by
  the float checks, so the "exact" instances are not reproducible independently of
  execution order. Cosmetic.

## 5. Verdict

PREMISES thm1: <V a finite-dimensional complex vector space (needed for determinants and
for "right inverse ⟹ inverse" in ⟨1⟩4); D = |[D]| with σ a fixed-point-free involution on
[D] (forces D even, gives the size-2 σ-orbits of ⟨1⟩2 and i ≠ ī); E_1,…,E_D ∈ End(V)
arbitrary — no invertibility, positivity, normality, diagonalisability or unitarity; and
u ∈ ℂ with 1 − u²E_ī E_i invertible for every i ∈ [D] (equivalently, by Sylvester, for one
representative i of each pair {i,ī}). For the norm-bound sentence only: ‖·‖ a
submultiplicative operator norm. NEW: none — I found no hypothesis used in ⟨1⟩1–⟨1⟩8 that
is not declared in §1–§2; in particular the invertibility at the index ī is the declared
hypothesis at ī ∈ [D], not an extra assumption, and the "for all i" form is if anything
stronger than the proof needs.>
VERDICT thm1: VALID
VERDICT cor2: VALID
VERDICT cor3: VALID
VERDICT cor4: VALID

RESULT: VALID — Theorem 1 and Corollaries 2–4 survive independent re-derivation and symbolic recomputation (incl. the untested D=2 case); only four cosmetic MINOR issues.

Files written: notes/reviews/theorem1-algebra-2026-09-12.md, notes/reviews/scratch_thm1_indep.py, notes/reviews/scratch_thm1_edge.py, notes/reviews/scratch_cor2.py, notes/reviews/scratch_outside.py
