# Lane K: the Kraus station (quantum Ihara–Bass and the Kraus dichotomy)

Files: `demos-kraus.js` (234 lines, `WT.demos.kraus`, mount `#demo-kraus`), `lanes/check_kraus.py` (the cross-check),
this report. No other file touched.

## Built

Fixed size: n = 2 (bond), D = 4 Kraus operators, reversal 1↔3, 2↔4 (0-based `INV = [2,3,0,1]`, as in
`scripts/weil_positivity.py`), N = n² = 4, dim W = 16, k = N(D−2)/2 = 4, q = 3, r = √3, Hastings 2√3/4 = 0.8660.

Controls (all ids prefixed `demo-kraus-`):
- `family`: unitary U, U† (Haar, QR/Gram–Schmidt of a seeded complex Gaussian) / inverse-paired non-unitary /
  adjoint-paired non-unitary / the no-duality example B₁ = B₃ = diag(1,2), B₂ = B₄ = 1.
- `reroll` (seed + 1; mulberry32 PRNG, Box–Muller), `ram` (preset "Ramanujan pair" (1−iX)/√2, (1−iZ)/√2),
  `pauli` (preset X, Z), `eps` (noise ε ∈ [0,1], unitary regime only: Uᵢ → Uᵢ + ε Rᵢ with B₃ = B₁†, B₄ = B₂†, so the
  adjoint pairing survives and the inverse pairing is lost), `K` (window 1..14).
- On load: the first Haar seed in 1..50 that meets Hastings' bound (it is seed 1: max |λ| = 0.8576 ≤ 0.8660); the
  √X, √Z preset is the fallback. Switching to the inverse-paired family jumps to the first seed ≥ the current one whose
  Σ-spectrum is non-real (seed 1 is).

Panels:
- (a) spec Σ, Σ = Σᵢ Ad(Bᵢ), in the plane, with the band [−2√3, 2√3] and D = 4 as a pole-coloured ring; trivial α
  (Φ = ±1 in the unitary case, the Perron α₀ in the inverse-paired case) in pole colour. Marked *comparison*.
  Hermitian Σ (adjoint pairing) by `WT.hermEigvals`, otherwise `WT.cmat.eigvals` (4×4).
- (b) spec T (16 modes) with the circle |μ| = r. Filled: eigenvalues of the 16×16 T by a Householder–Hessenberg +
  shifted-QR solver in the module (see *Findings*, F3); hollow: Ihara–Bass (inverse-paired) or the closed form of
  prop:kraus-no-duality-example. Trivial modes in pole colour; values beyond the range pinned to the edge with a label.
  Marked *comparison*.
- (c) side A: log₁₀(1 + Tr Tˡ), l = 1..12 (all ≥ 0), with hollow markers at the explicit word sums Σ_w |Tr B_w|² for
  l ≤ 4 (enumeration of all cyclically non-backtracking words in [4]ˡ, live); below, the retained sequence
  νₗ = r⁻ˡ(Tr Tˡ − Σ_S μˡ), l = 0..13, signed-log bars.
- (d) the Toeplitz Weil matrix (ν_{k−j}) at the chosen K (`WT.toeplitz`, `WT.svg.heat`) and λ_min(K) for
  K = 1..14 (`WT.jacobiEig`), signed-log bars coloured by sign; the chosen K boxed.
- Readout: family and seed; the numeric pairing tests ‖B_ī Bᵢ − 1‖, ‖B_ī − Bᵢ†‖ → inverse-/adjoint-paired/unitary;
  the rescaling (adjoint-only); spec Φ; Hastings max |λ| off ±1 vs 0.8660 and "holds/fails"; S and r; side A (Tr Tˡ vs
  word sums for l ≤ 4 with word counts, positivity of Tr Tˡ for l ≤ 16, |Im Tr Tˡ|); side B (QR vs Ihara–Bass, and the
  Newton-identity route's error); the retained multiset (count, J-invariance, max ||μ| − r|, max |μ|); λ_min at the
  chosen K and at K = 4, 8, 12; the verdict sentence per regime.

Game rule: the Weil form is built only from Tr Tˡ (side A) and the trivial set S; eigenvalues enter only through S
(which, as in the unitary theorem, is read off Σ) and the *comparison* panels/lines.

The numerics are exported as `WT.demos.kraus.model` (`model`, `family`, `readout`, `eigQR`, ...) and run headless in
node with the stubs `window = {matchMedia}`, `document = {getElementById: () => null}`.

## Mathematics used

| statement | label | where |
|---|---|---|
| T(v⊗\|i⟩) = Σ_{j≠ī} Eᵢ v ⊗ \|j⟩, Eᵢ = Ad(Bᵢ) = conj(Bᵢ)⊗Bᵢ (column stacking) | notes/quantum-ihara-general.md §1 | `buildT`, `WT.cmat.ad` |
| Tr Tˡ = Σ over cyclically non-backtracking words of \|Tr B_{w_l}⋯B_{w_1}\|² ≥ 0, no pairing needed | cor:qihara-kraus, prop:kraus-conjugation-symmetry | panel (c), `wordSum`, readout "side A" |
| spec Σ, spec T conjugation-closed for every Ad family (so Tr Tˡ and ν real) | prop:kraus-conjugation-symmetry | ν uses Re Tr Tˡ; readout prints max \|Im Tr Tˡ\|/\|Tr Tˡ\| ≈ 1e-16 |
| inverse pairing: spec T = {+1^[4], −1^[4]} ∪ roots of μ² − αμ + 3 over α ∈ spec Σ; retained set invariant under μ ↦ 3/μ and conjugation, hence J-invariant | thm:kraus-inverse-pairing-duality (Cor. 3) | hollow markers of (b), `ref`; J-test |
| both pairings iff every Bᵢ unitary | prop:kraus-both-pairings-unitary | the family *kind* is decided by the two numeric pairing tests, not by the menu |
| (i) adjoint pairing: Weil positivity ⇔ one-sided bound \|μ\| ≤ r off S; (ii) unitary: S = {±1^[4]} ∪ {3,1} per Φ-eigenvalue +1 ∪ {−3,−1} per Φ-eigenvalue −1, positivity ⇔ Hastings | thm:kraus-weil-criterion | trivial set, verdicts |
| B₁ = B₃ = diag(1,2), B₂ = B₄ = 1: charpoly ∏_{a∈{1,2,2,4}} (x−a)(x−1)(x² − (a+1)x − 3a); no μ ↦ c/μ symmetry; positive iff r ≥ p₄ = (5+√73)/2 | prop:kraus-no-duality-example (review T3.5) | closed form in (b), S and r of that regime |
| B = G U G⁻¹ gives real Σ-spectrum under inverse pairing | notes/weil-positivity.md X2 | used in F2 below |

## Independent check

`python3 notes/weil-tn-tutorial/lanes/check_kraus.py` runs the demo in node on seven fixed states, exports the raw
matrices B₁..B₄ and every printed number, recomputes from the *identical* matrices with numpy (eig, eigvalsh, matrix
powers, itertools word sums) and prints both in the demo's format. **Result: 0 mismatches** over 7 × 16 compared rows
(pairings, rescale factor, spec Σ, Hastings max and verdict, S, r, Tr Tˡ for l ≤ 4, word counts, retained multiset,
J-invariance, max ||μ|−r|, max |μ|, all 16 eigenvalues of T, λ_min for K = 1..14). Further, per case:

| case (state) | kind | Hastings max \|λ\| | S | λ_min K = 4, 8, 12 (python = demo) | extra |
|---|---|---|---|---|---|
| unitary Haar, seed 1 (default) | unitary | 0.8576 (holds) | ±1^[4], {3,1} | 0.079659, 0, 0 | IB det rel. err 8.9e-16; J-inv. yes; max \|\|μ\|−r\| = 0.0000 |
| preset (1−iX)/√2, (1−iZ)/√2 | unitary | 0.5000 (holds) | ±1^[4], {3,1} | 0.34159, 0, 0 | IB 1.2e-15; spec Φ = {0, ½, ½, 1} |
| preset X, Z | unitary | 0.0000 (holds) | ±1^[4], {−3,−1}, {3,1} | 0, 0, 0 | IB 3.3e-16; 4 retained modes ±i√3 (twice) |
| Haar seed 1, ε = 0.3 | adjoint-only | 1.1456 (n/a) | {3} after s = 0.889420 | 12.156, 9.5706, 9.0598 | J-inv. no; max \|μ\| = 1.5036 ≤ √3 → positive |
| inverse-paired, seed 1 | inverse-only | 4.7893 (n/a) | ±1^[4], Perron pair {18.9994, 0.1579} | −28.613, −3475.6, −3.4451e5 | IB 1.4e-15; spec Σ = 19.1573, 6.0158, −0.5061 ± 1.5063i; J-inv. yes; max \|\|μ\|−r\| = 3.7350 |
| adjoint-paired, seed 1 | adjoint-only | 1.4763 (n/a) | {3} after s = 0.984176 | 13.654, 12.595, 12.392 | J-inv. no; max \|μ\| = 1.4087 |
| no-duality example | adjoint-only | 2.5000 (n/a) | {1^5, 2², 4, 3, −1} | 3.9549, 3.6546, 3.5762 (r = p₄ = 6.7720) | at r = √3: λ_min(12) = −3.5536e6; J-inv. no |

- Tr Tˡ = Σ_w |Tr B_w|² for l ≤ 5 in every case, max relative difference 1.6e-15; word counts 4, 12, 28, 84, 244.
- Tr Tˡ ≥ 0 for l ≤ 16 in every case (Pauli: Tr T¹ = Tr T³ = 0 exactly).
- Ihara–Bass det(1−uT) = (1−u²)⁴ det(1 − uΣ + 3u²) at u = 0.13, 0.21+0.09i, −0.17 in all four inverse-paired cases,
  max relative error 1.4e-15; numpy eig vs Ihara–Bass ≤ 2.1e-14, the demo's QR vs Ihara–Bass ≤ 1.4e-14.
- Extra demo checks (node): unitary Haar seeds 4 and 12 fail the bound (0.8990, 0.9911) and the form goes negative
  from K = 6 and K = 3; seed 8 passes (0.5895) and stays ≥ 0. Positivity ⇔ Hastings in every case looked at.
- Preset search (check script): X,Z → max nontrivial |λ| 0 (Φ has eigenvalue −1); X,H → 0.7071 (Φ = −1 again);
  √X,√Z → 0.5; X, e^{iπ/8 Y} → 0.8536; tetrahedral rotations (angle arccos(−1/3) about x and z) → 1/3.
  Haar pairs meeting the bound: 0.590 of 2000 numpy draws (the demo's seeds 1..30: 19 of 30).

The Newton-identity numbers (last line of "side B") are round-off diagnostics and are compared only in order of
magnitude: demo (Durand–Kerner) 4e-3, 5e-3, 5e-3, 3e-8, 8e-1, 6e-6, 2e-2 against numpy's np.roots 5e-3, 3e-3, 6e-4,
6e-9, 1e0, 6e-6, 1e-3.

## Findings against the brief

- **F1 (trivial set outside the unitary case).** The set of thm:kraus-weil-criterion (ii) is a sub-multiset of spec T only
  for unitary families. For an adjoint-only family T has no ±1^[4] (and no {3,1}); subtracting them from Tr Tˡ gives
  a sequence with negative "multiplicities", to which neither T1 nor (i) applies. Resolved: the trivial set follows
  the family *kind*, which the demo decides from the numeric pairing tests:
  unitary → the (ii) set; inverse-only → {±1^[4]} plus the **Perron pair** {μ₊, μ₋} of the largest Σ-eigenvalue α₀
  (the analogue of {3,1} for α = D; it is a J-orbit, so the retained set stays J-invariant); adjoint-only →
  S = {μ₀}, the Perron root of T, as in the notebook's T1 test; no-duality example → the ten values of the
  proposition, r = p₄.
- **F1' (adjoint-only normalisation).** The brief asked to rescale so that Σ's top eigenvalue is D. That does not put
  the Perron root of T at 3, so r = √3 would not be the natural radius. Resolved: rescale Bᵢ → s·Bᵢ so that the Perron
  root of T is q = 3 (T scales by s²); then S = {3}, r = √3 exactly, and ε → 0 joins the unitary case continuously
  (s → 1). The readout prints s and the raw Perron root.
- **F2 (inverse pairing with |det Bᵢ| = 1 gives a real Σ-spectrum for n = 2).** With the brief's normalisation the
  Σ-spectrum came out real in 400 of 400 draws (check script), so the regime could not show "non-real Σ, modes off
  the circle". Reason: for |det B| = 1, Ad(B) acts on Hermitian 2×2 matrices as a Lorentz transformation Λ, and
  Ad(B⁻¹) = Λ⁻¹ = ηΛᵀη, so Σ is self-adjoint for the Minkowski form η. Σ maps the forward cone into itself, its Perron
  vector is timelike, and on the η-orthogonal complement (spacelike, where η is definite) Σ is self-adjoint, so the
  rest of the spectrum is real too. This is the indefinite-metric version of X2's G U G⁻¹. Resolved: B₁, B₂ are
  complex Gaussians with no det normalisation (the notebook's T3 convention); Σ-spectrum is then non-real in 0.56 of
  draws, and the demo jumps to such a seed on entering the regime. The verdict line adapts to whichever case shows.
- **F3 (the spectrum of T from power sums is ill-conditioned).** Newton's identities from Tr T¹..Tr T¹⁶ followed by
  polynomial roots are exact in exact arithmetic but lose δ^{1/m} at the four-fold ±1 (errors about 5e-3) and wipe out
  the small roots once the spectrum spans a range (inverse-paired seed 1: Perron root 19.0, so Tr T¹⁶ ≈ 3e20; errors
  about 1). np.roots does the same, so it is not an implementation problem. Resolved: panel (b) uses a 16×16
  Hessenberg-QR solver in the module (agrees with Ihara–Bass to 1e-14 and with numpy's eig to the printed digits). The
  Newton route is kept only as a diagnostic line in the readout. `WT.cmat.eigvals` on 16×16 was not tried: it is the
  same polynomial route.
- **F4 (λ_min digits).** For inverse-paired families Tr Tˡ − μ₀ˡ cancels about 16 digits at l = 13, so λ_min has only
  about 8 correct significant digits there. The demo prints λ_min to 5 significant digits (and 0 below
  1e-9 · max|ν|), which is what agrees with Python.
- **F5 (rank).** In the unitary case with the bound holding there are only 6 retained modes, so the Toeplitz form has rank ≤ 6
  and λ_min = 0 (printed 0) for K ≥ 7. It is positive semidefinite, not definite, and the verdict tests ≥ 0.
- **F6 (finite window).** A mode just outside the circle can stay invisible at K ≤ 14 (T1 is a statement about all K;
  notebook T1a2). The verdicts say so when the bound and the K ≤ 14 minima disagree. No such case came up among the
  states checked.
- **F7 (brief's word count).** "D(D−1)^{l−1} minus backtracks at the seam": the cyclically non-backtracking counts
  are 4, 12, 28, 84, 244 = 3ˡ + 1 + 2·[l even] (the trace of the 4×4 letter matrix). The demo and the check count by
  enumeration.
- **Self-inverse presets.** The Pauli pair has B₃ = B₁ = X, B₄ = B₂ = Z (allowed: the reversal still pairs 1↔3, 2↔4).
  Its Φ has the eigenvalue −1, so it exercises the {−3,−1} clause of (ii). The "Ramanujan pair" preset is
  (1−iX)/√2, (1−iZ)/√2 (π/2 rotations about x and z, not self-inverse, irreducible: Φ = {1, ½, ½, 0}). The default is
  still a Haar pair, since one passes at seed 1. Haar pairs pass about 59% of the time, so "often fail" in the brief
  overstates how often they fail.
- The brief's regime (4) was listed without S or r; the proposition's own S and r = p₄ are used (one mode on the circle,
  the rest inside: positive with no duality). λ_min at r = √3 is also printed.

## Visual check

Playwright (node module at /opt/node22/lib/node_modules/playwright, chromium-1194): scratch page loading theme.css,
core.js, demos-kraus.js with `#demo-kraus` and `WT.mountAll()`. Screenshots taken of the default (light), the
inverse-paired family (dark), ε = 0.3 (light), and the no-duality example and the default at 400 px width. No page or
console errors, and no horizontal scroll at 400 px (scrollWidth = 400). One fix pass was applied after the first screenshots:
clipped subtitles were shortened, and outliers (the inverse-paired Perron mode at 19) are now pinned to the plot edge so
that the circle stays readable.

## Open

- At 400 px the SVG labels are small (9–10 px in a 440-wide viewBox shown at about 330 px). They are legible, but the
  orchestrator may want the grid stacked earlier.
- Pinned-outlier labels in (a)/(b) can overlap the band labels when α₀ is large.
- No live control for r (e.g. to sweep the no-duality example through p₄); the readout prints both r = p₄ and r = √3.
