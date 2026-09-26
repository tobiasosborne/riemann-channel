# Lane TN: tensor-network renderer and the four storyboard movies (2026-09-26)

## Built

`tn.js` (243 lines, plain ES2020, no libraries) defines:

- `WT.tn`, a small SVG tensor-network renderer. Interpolation: `clamp, ease, seg(t,a,b), lerp, lerpPt, live(t,a,b)`.
  Primitives: `label` (text where `^{..}`/`_{..}` become raised/lowered tspans, with whitespace preserved),
  `box` (classes `tn-box`, `bar`, `metric`, `trivial`), `leg` / `dangle` / `path` (classes `tn-leg bond|phys|doubled`;
  `path` can be drawn progressively), `chain` (L sites, physical legs up or down, open bond ends), `doubled`
  (ket over bra with contracted physical legs; `merge` fuses each column into a tall `E` box and turns the two
  bond lines into a violet doubled leg), `ring` (periodic closure below a chain), `glue` (arc joining two strip
  ends; returns its apex, where the metric seams sit), `loop` (a small ring of n transfer boxes), `g`.
  Numerics for movie 4: `circleModes(t)` and `circleData(t)` (mode set, t_l and Toeplitz minima at time t).
  All colours come from theme.css classes or `var(--token)` attributes, and both themes were checked.
- Four movies, each `WT.demos.<name>(root)` → `WT.movie(root, {id: <name>, ...})`, autoplay false. Controls get
  the ids `<name>_play`, `<name>_t` and `<name>_step`. Each draw is pure in t, and every scene is interpolated
  (positions, widths, opacities, progressive strokes), so scrubbing is smooth.
  - `movieRing` (940×300, 14 s, 4 scenes): ket chain of L = 5 sites A_{s_i} with physical legs up → the bra layer
    slides in and the physical legs contract → the columns fuse into E = Σ_s A_s ⊗ Ā_s (doubled legs) → the chain
    closes into a ring, ‖ψ_L‖² = Tr E^L = Σ_w |Tr A_{s_L}⋯A_{s_1}|² → the ring shrinks into the L = 5 slot of a
    row of loops t_1..t_6. The last caption states ζ_E(u) = exp(Σ t_L u^L/L) = 1/det(1 − uE).
  - `movieGram` (940×320, 16 s, 5 scenes): strips E^2 (top) and E^4 (bottom) with open ends → the top strip
    card-flips (mirror about its centre; the index labels 1, 2 swap) into (E^j)^* with shaded `bar` boxes →
    both ends are glued by progressively drawn arcs, Tr((E^j)^*E^k) → the E^*E pairs fade out from the left seam
    and the loop retracts to a ring of k − j = 2 boxes → a 5×5 grid of mini glued diagrams labelled t_{k−j},
    ending on the statement "T_{jk} = Tr((E^j)^*E^k) = t_{k−j}: a Gram matrix, so T ⪰ 0".
  - `movieMetric` (940×320, 16 s, 5 scenes): the glued diagram, with "≠ t_{k−j}" → a G box on the left seam and
    G^{−1} on the right → each seam splits into G^{½} / G^{−½} tokens that slide along the strips, and every
    box grows metric caps and becomes Ẽ → Ẽ^*Ẽ = 1 cancellation, with prop:hp-inner-product-discrete and the
    Jordan-block example on the board → a lone metric box "G ?" (strips known, metric unknown).
  - `movieCircle` (940×320, 16 s, 4 scenes): the complex plane (`WT.svg.plane`, r = 1) on the left. On the right,
    λ_min(T_K) for K = 1..14 is computed live with `WT.toeplitzMins`, drawn on a signed log scale
    sign(v)·log10(1+|v|) with a zero axis, green where ≥ 0 and orange where negative. Below it is the readout
    "|μ| = …  λ_min(T_14) = …  negative from K = …".

## Mathematics used

| Statement | Label | Where |
|---|---|---|
| Tr(Σ_s A_s⊗Ā_s)^n = Σ_{s_1..s_n} \|Tr A_{s_1}⋯A_{s_n}\|² (MPS norm network) | 03g, first display | movieRing scenes 2–3 |
| exp(Σ t_L u^L/L) = 1/det(1 − uE) for t_L = Tr E^L | standard; def:transfer-matrix | movieRing scene 4 caption |
| E^*GE = G > 0 ⇒ (T_K)_{jk} = Tr((E^j)^♯E^k) = t_{k−j}, c^*Tc = ‖p_c(E)‖²_{HS,G} | prop:ccm-tn-operator-gram | movieGram scenes 3–5, movieMetric scene 3 |
| A^♯ = G^{−1}A^*G, ⟨A,B⟩_{HS,G} = Tr(A^♯B) = HS product of Ẽ = G^{½}·G^{−½} conjugates | def:ccm-tn-feature | movieMetric scenes 2–3 |
| Unitarising inner product exists iff X′ is diagonalisable with all eigenvalues of modulus r | prop:hp-inner-product-discrete | movieMetric scene 4 |
| r(1 1; 0 1): ν_l = 2 for all l, positive definite, not unitarisable | prop:weil-blind-jordan | movieMetric scene 4 |
| ν positive definite iff every retained \|μ\| ≤ r | thm:weil-positivity-finite | movieCircle scenes 1–2 (live) |
| J-invariant retained set: W = M(c) = Σ p_c(μ/r)·conj p_c(Jμ/r); W ≥ 0 iff all \|μ\| = r | thm:weil-duality-pairing | movieCircle scene 3 |
| An off-circle J-orbit makes W negative | prop:weil-orbit-negative | movieCircle scene 3 (live: still negative) |

The Toeplitz convention is that of def:ccm-tn-moments: T_{jk} = t_{k−j} with t_{−l} = conj(t_l). The movieCircle
sequence is real, so T is symmetric and `WT.toeplitzMins` (real Jacobi) applies.

## Independent check

`lanes/check_tn.py` computes the complex sums t_l = Σ w_μ μ^l with numpy, asserts that the imaginary parts vanish,
and takes `eigvalsh` of every window. It then runs `core.js` and `tn.js` under node with a stub `window`/`document`,
calls `WT.tn.circleData(t)` at the matching movie times, and compares. The worst discrepancy over all t_l and all
minima is 2.4e-13.

| configuration (movie t) | t_0..t_4 (python) | λ_min(T_K), K = 7, 8, 14 (python) | first K < 0 | demo readout (browser) |
|---|---|---|---|---|
| start, pair on circle R = 1 (t = 0) | 8, −0.2957, −2.0187, −0.6842, −1.5669 | 1.6473, 1.2285, 0.0000 (rank 8: zero from K = 9) | none | λ_min(T14) = 0.0000, ≥ 0 for all K ≤ 14 |
| inside R = 0.55 (t = 0.3) | 8, −0.5364, −0.8234, 0.5261, −2.4181 | 1.9984, 1.9090, 0.9059 | none | λ_min(T14) = 0.9059, ≥ 0 |
| outside R = 1.35 (t = 0.6) | 8, −0.1084, −3.4283, −2.8045, 0.6085 | 0.8269, −5.4674, −112.0221 | 8 | λ_min(T14) = −112.0221, negative from K = 8 |
| outside + partners 1/1.35 (t = 0.8) | 10, 0.2879, −4.3687, −3.3946, 0.8906 | 1.9691, −3.5357, −108.9045 | 8 | λ_min(T14) = −108.9045, negative from K = 8 |
| merged on circle, double mode (t = 1) | 10, 0.2393, −3.7325, −2.1361, −0.6298 | 1.9729, 1.4864, 0.0000 | none | λ_min(T14) = 0.0000, ≥ 0 |

`python3 lanes/check_tn.py` prints the full sequences l = 0..13 and all fourteen minima.

## Visual check

I built a scratch page in the session scratchpad (`tn.html`: theme.css, core.js, tn.js, the four mount divs,
`WT.mountAll()`) and screenshotted it with the global Playwright package (`/opt/node22/lib/node_modules/playwright`,
chromium from `/opt/pw-browsers`). I looked at each movie at t = 0, .2, .25, .3, .36, .5, .56, .62, .7, .8, .9, 1
in light mode and at t = .5 in dark mode, calling `setT` through `page.evaluate`. For every frame the script also
checked each SVG `<text>` bounding box against the viewBox, and checked for `draw error` text and console errors.
**Found and fixed in one pass:**
- movieRing scene 2: the ket labels were printed twice while two layers crossfaded. The ket now carries through.
- The blackboard formula lines crossfaded on top of each other. They now fade out and in sequentially (`T.live`).
- SVG whitespace was collapsed in the readout. Labels now use `white-space:pre`.
- The combining macron μ̄ rendered badly in the mono font. The legend now reads `conj(μ)`.
- The t_1..t_6 row was off centre.
- The circle readout was clipped by 1 px at the bottom.

**Final state:** no text outside any viewBox, no console errors, and both themes legible.

## Findings against the brief

- **Which E is meant.** In movieRing, E is the MPS transfer matrix Σ A_s⊗Ā_s. In movieGram and movieMetric it is
  the rescaled retained operator of def:ccm-tn-spaces (trivial modes removed, divided by r); only for that operator
  is t_{k−j} = Tr E^{k−j} the Weil sequence. The first movieGram caption says so.
- **Which seam carries G.** Tr((E^j)^♯E^k) = Tr(G^{−1}(E^j)^*G E^k). G sits where the adjoint strip's last factor
  meets E^k (the left glue, where the cancellation starts), and G^{−1} sits on the other glue.
- **Partner weight in scene 3.** For continuity, the reflected partners enter with a weight that ramps 0 → 1 over
  t ∈ [0.60, 0.68], a positive measure throughout. Between the frames it is a weighted sequence, not a multiset;
  the checked configurations use weight 0 or 1. With the partners at full weight the set is J-invariant, and λ_min
  stays negative from K = 8 on, as prop:weil-orbit-negative requires.
- **Scene 4 ends on a double mode.** The pair and its partners keep J-invariance (partner radius 1/R) and merge on
  the circle, so the final state is a double mode. On the circle the window has rank 8, so λ_min = 0 exactly for
  K ≥ 9. The readout clamps |v| < 1e-9·t_0 to 0.0000 instead of printing about 1e-15.
- **Unicode notation.** The brief's `#` is rendered as ♯ (the notebook's \sharp). Negative lags in the grid are
  shown as t_{−l}, and the caption says t_{−l} = conj t_l.

## Open

- At widths near 400 px the 940-wide viewBoxes scale the 10–12 px SVG text down to about 5 px. The movies stay
  readable in outline, and the captions (HTML) carry the statements.
- The strips in movieGram and movieMetric draw each wire as a single `bond` line, following the colour contract
  (bond = Gram/strip objects). Each wire is a doubled-bond index, and the first caption says so; movieRing draws
  those same legs as violet doubled lines.
