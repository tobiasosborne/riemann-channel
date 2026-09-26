# Lane core (orchestrator, claude:fable-5.1): stations 0–3 and 7, page assembly

## Built

`index.html` (prose, dictionaries, `.claim` boxes with claim labels, TERMS modal, mount points, boot),
`theme.css` (tokens mirrored from the artifact *The Weil Functional*, plus `.tn-*` classes and the movie
chrome), `core.js` (helpers, numerics, `WT.movie`), `data-riemann.js` (the x = 13, N = 20 CCM case copied from
`notes/zeta-spectral-triples/tutorial/riemann-data.js`, and the first 100 zero ordinates for comparison
panels), `demos-core.js` (five demos), `build.py` (inlines everything into `weil-positivity-contracted.html`,
the published single file).

Demos: `perm` (permutation network with point letters, doubled-bond transfer matrix, ring words, Weil matrix,
twisted closure), `subshift` (0/1 transition matrix, pole, rescaled sequence, one-sided bound, J-invariance),
`gram` (E = VΛV⁻¹: Toeplitz from traces vs naive HS Gram vs metric Gram; off-circle mode; Jordan block),
`riemann` (lattice-bump Gram matrix of the Weil functional from primes vs zeros; conventions of the parent
artifact), `ccm` (the precomputed window case).

## Mathematics used

- `def:transfer-matrix`, `def:ring-norm` (step 0); shard 03b `def:graded-permutation-mps`,
  `prop:permutation-rings`, `thm:permutation-induced-zeros` (step 2: point letters, twisted closure).
- `prop:ccm-tn-operator-gram` (Gram of open strips in the G-twisted HS product), `prop:hp-inner-product-discrete`
  (existence of the metric), `thm:weil-positivity-finite`, `thm:weil-duality-pairing` (step 1 and the subshift
  verdicts). Zero eigenvalues are put in the trivial set of the subshift (they contribute to no trace and the
  duality theorem requires 0 ∉ retained).
- Step 7: the explicit formula in the normalisation of *The Weil Functional* (ĝ(γ) = ∫ g e^{iγx} dx,
  ρ = ½ + iγ); `def:ccm-tn-continuous` (smeared strips); `def:ccm-tn-loewner` and shards 08g/08i for the window.

## Independent check (`check_core.py`, numpy) against the demo readouts

| quantity | Python | demo readout |
|---|---|---|
| permutation (1 2 3)(4 5 6): Tr E^k, k = 1..12 | 0,0,6,0,0,6,0,0,6,0,0,6 | same |
| its Toeplitz(8) kernel dimension | 5 (3 distinct eigenvalues) | 5 |
| golden mean: λ_max, r | 1.618034, 1.2720 | 1.6180, 1.272 |
| golden mean: ν_0..8 | 1, −0.486, 0.236, −0.115, 0.056, −0.027, 0.013, −0.006, 0.003 | same |
| golden mean: λ_min at K = 10 | 0.3531 | 0.3531 |
| golden mean: retained \|μ\| | 0.618 | 0.6180 |
| cyclic rule I + C₄: λ_max, retained \|μ\| | 2, 1.4142 ×2 | same |
| gram (κ = 1): max \|metric Gram − T\| | 1.4e-15 | 1.67e-15 |
| gram (κ = 1): max \|naive − T\| | 7.987 | 7.99 |
| gram (κ = 1): Toeplitz eigenvalues | 0,0,0, 4.149, 6.296, 7.555 | same |
| lattice Gram, n ∈ {1,2,3,4,6}, s = 0.08: eigenvalues (primes) | 0.00037627, 0.00095529, 0.0068755, 0.026846, 0.10953 | same |
| same from the first 100 zeros | identical to 5 digits; max \|G − Z\| = 9.6e-11 | same |

## Visual check

Playwright (chromium): every demo panel at 1000 px light and 400 px dark; no page errors, no horizontal
scroll at 400 px; one NaN bug in the permutation demo's window plot fixed (the sequence was one term short of
the 14-window plot). The 36×36 heat map of E and the 21×21 window matrix are legible at 400 px; SVG text in
the movies is small at that width (the captions carry the statements).

## Findings against the brief

- Three worker findings changed the prose: the Artin–Schreier sign law is `thm:as-sign-law` (the founding
  note's −(−1)^m holds only when P_g(−1) ≠ 0); a perturbed transfer matrix need not make the form negative
  (one-sided positivity); the prism C₁₆×K₂'s form first goes negative at K = 14 with the bipartite trivial set.
- The REFUTE review's verdicts are in `review.md` and were applied before publication.

## Open

- The page's step 7 states the CCM near-kernel step descriptively; the CCM correction itself (D′, the secular
  function) is only quoted, not recomputed here (it is recomputed in *Zeros From Counts*).
