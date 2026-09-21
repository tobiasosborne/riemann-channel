# Tutorial "Zeros From Counts" — file contract for the workers (2026-09-18)

An interactive tutorial (single web page, published as a Claude artifact) explaining the
Connes-Consani-Moscovici (CCM) spectral-realisation method in its MOST GENERAL form, built up from
fixed-point counting of permutations. Audience: knows the definition of the Riemann zeta and basic
linear algebra, nothing else. Reference for the mathematics: `../plan.md` Sections 1.1-1.5 (the zeta
case), `../../../ihz/README.md` and `../ihara/lanes/theory.md` (the finite/Toeplitz case).

## Files (each worker owns only its files; the orchestrator owns index.html and theme.css)

    index.html        orchestrator: prose, structure, MathJax, demo mount points, boot script
    theme.css         orchestrator: tokens and the demo chrome classes (READ IT; use these classes)
    core.js           worker A: numerics + drawing helpers, global `window.ZT`
    demos-finite.js   worker A: stations 1-4 (permutations, Newton, Toeplitz positivity, Pisarenko)
    riemann-data.js   worker B: precomputed Riemann data, global `window.ZT_RIEMANN`
    demos-riemann.js  worker B: stations 5-7 (secular explorer, Riemann realisation, the algorithm)

No build step, no modules, no external libraries except MathJax (already loaded by index.html:
`tex-svg`, so `MathJax.typesetPromise([el])` after you inject TeX into an element; prefer plain HTML
labels inside demos). Plain ES2020, works when the files are opened from disk and when served next to
index.html. Everything must work at 400px width (the demo panel is `width:100%`; SVGs use
`viewBox` + `width:100%`). Respect `prefers-reduced-motion`. Every control has a stable `id`
(prefix with the demo id). Colors ONLY through the CSS custom properties of theme.css (read them with
`getComputedStyle(document.documentElement).getPropertyValue('--accent')` in canvas/SVG code, or use
`fill="var(--accent)"` in SVG). Both light and dark themes must look right.

## Mount API

Each demo is a function `ZT.demos.<name>(root)` where `root` is the `<div class="demo" id="demo-<name>">`
already present in index.html; it fills the root with `.demo-controls`, `.demo-stage` (one or more
figures), `.demo-readout` blocks (classes in theme.css) and returns nothing. index.html calls all
mounts on DOMContentLoaded through `ZT.mountAll()` (worker A writes `mountAll`: iterate over
`ZT.demos`, mount each whose root exists, catch and print errors into the root).

## Stations and demos (the pedagogical arc; the orchestrator writes the prose around them)

1. `permCounts` (A). A permutation in cycle notation, default `(1 2)(3 4 5)` on n = 5 (editable text
   field, n up to 12; also a "random" button). Show the permutation as arrows on a circle of dots or
   as a cycle diagram; a power slider k = 1..12 highlighting the fixed points of sigma^k; the table
   N_k = #Fix(sigma^k) for k = 1..12; the zeta as a product over cycles 1/(1 - u^l) and the identity
   Z(u) = exp(sum N_k u^k / k) checked numerically (show the first 6 Taylor coefficients of both).
2. `newton` (A). The eigenvalues of the permutation matrix (roots of unity, drawn on the unit circle,
   colour-coded by cycle) and the identity N_k = sum lambda^k (power sums; the table from station 1
   reproduced from the eigenvalues). Then the inverse: Newton's identities turn N_1..N_n into the
   characteristic polynomial 1/Z(u) (show the coefficients) whose roots are the eigenvalues. Slider:
   how many counts M are used; for M < n the recovered polynomial is wrong/incomplete (show what
   happens: e.g. list the roots of the partial recovery). Message: counts <-> spectrum, but you need
   as many counts as there are eigenvalues.
3. `toeplitz` (A). The Weil (Toeplitz) form: T_{jk} = N_{|j-k|} for j,k = 0..M (with N_0 = n), shown as
   a heat-map-like grid with the numbers; its eigenvalues (all >= 0: it is the moment matrix of the
   measure sum_lambda delta_lambda on the circle; f^T T f = sum_lambda |sum_j f_j lambda^j|^2). The
   "break RH" control: replace one eigenvalue pair by r e^{+-i theta} with a slider r in [0.5, 1.5]
   (counts become N_k = sum lambda^k of the new set; show them) and watch the minimal eigenvalue of T
   go negative once M is large enough (plot: min eig vs M for the current r, and the M at which it
   turns negative). Message: positivity of the truncated Weil form is the "RH for the window".
4. `pisarenko` (A). For the true (unitary) counts: T has a kernel once M >= number of distinct
   eigenvalues; the kernel vector xi gives the polynomial xi(z) = sum xi_j z^j whose roots are EXACTLY
   the eigenvalues. Slider M: below the critical window there is no kernel; the minimal eigenvector
   still has all its roots ON the unit circle (draw them, with the true eigenvalues as hollow
   circles) and they approximate/bracket the true ones; eps = min eigenvalue shown, with eps -> 0
   at the critical window. Also show that the kernel vector is palindromic (xi_j = xi_{M-j}, real
   coefficients) which is why the roots come in conjugate pairs / are on the circle.
5. `secular` (B). Standalone: given a symmetric vector xi_{-N..N} (N = 4..8, sliders or a "random
   positive-ish" button, normalised so sum xi_j = 1), plot g(s) = sum_j xi_j/(j - s) with its poles at
   the integers and its 2N real roots (marked); explain interactively that the roots are the
   eigenvalues of D - |D xi><eta| (show the (2N+1)x(2N+1) matrix D' = diag(j) - (D xi) eta^T for
   small N and its numerically computed eigenvalues next to the roots: they agree). Message: for
   Fourier modes on an interval the "roots of the polynomial" of station 4 become the roots of a
   secular function; they are provably real.
6. `riemann` (B). The real thing, precomputed: for lambda^2 = x in {9, 13, 20, 30} and N in {20, 40}
   (whatever B can compute; N = 20 and 40 at x = 9, 13 at least): the Loewner matrix's minimal
   eigenvector xi (bar chart, log scale of |xi_j| with sign colour), eps, the secular roots
   z_k = 2 pi s_k / L against the first 20 Riemann zeros (table with |z_k - gamma_k|, and a
   number-line figure: ticks for zeros, dots for recovered), selector for (x, N). Plus the
   convergence plot: log10 |z_1 - gamma_1| vs x, the "5.5 digits per unit x" law.
7. `algorithm` (B). The whole method as one panel: five steps with the finite (permutation) and the
   Riemann instance side by side, each step a small live figure or number reused from the other
   demos (call the helpers of core.js): (i) counts in a window -> (ii) Weil form matrix (Toeplitz /
   Loewner) -> (iii) positivity eps -> (iv) minimal eigenvector -> (v) roots (polynomial / secular)
   = spectrum. A "run" button that animates through the steps for the permutation case.

Worker A must also expose in `ZT`: `parseCycles(str, n)`, `permPower`, `fixedPoints`, `countsOf(perm, K)`,
`eigenvaluesOfPerm(perm)` (as {re, im, cycleIndex}), `newtonToPoly(counts)`, `toeplitz(counts, M)`,
`symEig(A)` (Jacobi; returns {values (ascending), vectors}), `polyRootsDK(coeffs)` (Durand-Kerner,
complex), `svg` helpers (`ZT.svg.el(tag, attrs)`, `ZT.svg.axes(...)`, `ZT.svg.circlePlot(...)`),
`ZT.fmt(x, digits)`. Worker B reuses these; B's `demos-riemann.js` is loaded after `core.js`.

Worker B computes the Riemann data with the mpmath prototype `../ccm_proto.py` (functions
`build_ab(lam, N)`, `even_block`, `secular_roots`; see its `main()`), or with the C tool
`../../../zst/build/zst --x 13 --N 40 --zeros 20` (prints certified roots; xi_0, xi_1, xi_N only) and
`mpmath.zetazero` for the true zeros; writes the numbers (as JS floats; xi as full arrays) into
`riemann-data.js` with a comment recording the command that produced them.

## Style

Panel chrome from theme.css: `.demo` (panel), `.demo-eyebrow` (small caps label, e.g. "Demo 3 ·
Positivity"), `.demo-controls` (flex row, wraps), `.demo-stage` (figures grid), `.demo-readout`
(monospace numbers strip), `.demo-note` (one-line hint). Controls: native `<input type=range>`,
`<input type=text>`, `<button class="btn">`, `<select>`; label every control with `<label for>`.
Tabular numbers: class `.num`. Eigenvalue/zero colour: `--accent`; poles/trivial: `--pole`;
negative/broken: `--bad`; true reference values: `--ink-2` hollow markers. Keep each demo under
~250 lines; no framework.
