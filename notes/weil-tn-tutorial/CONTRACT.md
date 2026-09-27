# Tutorial "Weil Positivity, Contracted" — file contract for the workers (2026-09-26)

A single interactive web page (published as a Claude artifact, sources committed here) that mirrors the
artifact *The Weil Functional* (https://claude.ai/artifact/FwqdU6JyRpunBjLDuThVnV; its HTML is the style
reference: hero, sticky step nav, `.demo` panels with a `.cap`, `.dict` dictionary boxes, dotted `.term`
buttons opening a definition modal) and walks through, example by example, **how Weil positivity is posed
in tensor-network (MPS) terms**: permutations, subshifts, regular graphs via Ihara–Bass, Kraus families
(quantum Ihara–Bass), Artin–Schreier curves, and finally the Riemann case where the transfer operator is
the unknown. Audience: knows what an MPS transfer matrix is and what the Riemann zeta function is.

Mathematical reference (binding; do not re-derive with other conventions): the lab book shards
`report/sections/08b_weil_positivity.tex` (finite Weil positivity, duality, Kraus dichotomy),
`report/sections/08c_weil_positivity_continuous.tex` (`prop:hp-inner-product-discrete`),
`report/sections/03g_ccm_tensor_gram.tex` + `02i_definitions_ccm_tensor.tex` (Weil form as the Gram matrix
of open transfer powers in a unitarising metric), `report/sections/08_quantum_ihara_general.tex` +
`notes/quantum-ihara-general.md` (Ihara–Bass for arbitrary Kraus families), `report/sections/03b_graded_permutation.tex`
(permutation MPS with point letters), `notes/artin-schreier-mps.md` + `report/sections/06_artin_schreier_mps.tex`,
`notes/weil-positivity.md` (Huang's criterion X1, Kraus dichotomy X2), `db/claims.tsv` for the exact statements.

## The spine every demo serves

For an operator `X` on a finite-dimensional space with a trivial sub-multiset `S` of its spectrum and a
critical radius `r`, the *rescaled trace sequence* is `nu_l = r^{-l} (Tr X^l - sum_{mu in S} mu^l)`,
`nu_{-l} = conj(nu_l)`, and the *Weil form* is the Toeplitz form `W(c) = sum_{l,k} c_l conj(c_k) nu_{l-k}`
(`def:rescaled-trace-sequence`, `def:weil-form`). Facts (all `proved` in the lab book):

- T1 (`thm:weil-positivity-finite`): `nu` positive definite  iff  `|mu| <= r` for every retained `mu`. One-sided.
- T2 (`thm:weil-duality-pairing`): if the retained multiset is invariant under `J(mu) = r^2 / conj(mu)`,
  then `W(c) = M(c) = sum_mu p_c(mu/r) conj(p_c(J mu / r))` (mode pairing, "inflow identity") and
  positivity iff every retained `|mu| = r`. An off-circle pair makes `W` negative (`prop:weil-orbit-negative`).
- TN reading (`prop:ccm-tn-operator-gram`): if `E^* G E = G > 0` (E unitary in the metric G) then
  `t_{k-j} = Tr((E^j)^# E^k)`, `(E^j)^# = G^{-1} (E^j)^* G`: the Toeplitz matrix is the **Gram matrix of the
  open transfer strips** `E^0, E^1, ..., E^{K-1}` in the G-twisted Hilbert–Schmidt inner product, hence PSD.
  Conversely (`prop:hp-inner-product-discrete`): a unitarising metric exists iff `X` restricted to the retained
  space is diagonalisable with all eigenvalues of modulus `r`. Positivity is blind to Jordan blocks.
- Kraus families `E_i = Ad(B_i)`, `i in [D]`, reversal `i -> ibar`, edge space `W = C^D (x) End(V)`,
  non-backtracking operator `T(v (x) |i>) = sum_{j != ibar} E_i v (x) |j>`. Ring norms
  `Tr T^l = sum_{non-backtracking cyclic words w} |Tr B_w|^2 >= 0` (`cor:qihara-kraus`).
  Inverse pairing `B_ibar = B_i^{-1}`: `det(1 - uT) = (1-u^2)^{N(D-2)/2} det(1 - u Sigma + (D-1) u^2)`,
  `Sigma = sum_i E_i`, `N = dim V = n^2`; retained multiset (after the `+-1`) invariant under `mu -> q/mu`,
  `q = D-1` (`thm:kraus-inverse-pairing-duality`). Adjoint pairing `B_ibar = B_i^dagger`: `Sigma` is
  Hilbert–Schmidt self-adjoint (real spectrum) but no duality. Both iff unitary
  (`prop:kraus-both-pairings-unitary`). Unitary case: Weil positivity iff Hastings' bound
  `|lambda| <= 2 sqrt(D-1)/D` for the nontrivial eigenvalues of `Phi = Sigma/D` (`thm:kraus-weil-criterion`),
  with trivial set `{+1^[k], -1^[k]}`, `k = N(D-2)/2`, plus `{q, 1}` once per eigenvalue `+1` of `Phi` and
  `{-q, -1}` once per eigenvalue `-1`.
- Classical graphs are the Kraus family of a `(q+1)`-regular graph: `B` = Hashimoto non-backtracking matrix on
  directed edges, `det(1-uB) = (1-u^2)^{|E|-|V|} det(1 - uA + q u^2)`; retained `mu` are the roots of
  `mu^2 - a mu + q` over the nontrivial adjacency eigenvalues `a`; positivity iff Ramanujan `|a| <= 2 sqrt q`;
  Huang's `h_k = 2(n-1) + q^{k/2} + q^{-k/2} - q^{-k/2} N_k = nu_0 - nu_k >= 0` is equivalent (X1).
  Bipartite graphs have `a = -(q+1)` too: remove `{-q, -1}` as well.

Game rule (as on the parent page): **nothing computes an eigenvalue and calls it the answer**. Every Weil form
is built from ring norms / counts, and eigenvalues are shown only in panels marked *comparison*.

## Files (each worker owns only its files; the orchestrator owns index.html, theme.css, core.js)

    index.html          orchestrator: prose, structure, MathJax, demo mount points, boot
    theme.css           orchestrator: tokens and chrome (READ IT; use these classes)
    core.js             orchestrator: helpers, global `window.WT` (READ IT before writing numerics)
    tn.js               worker TN:    tensor-network diagram renderer + the four storyboard movies
    demos-graphs.js     worker G:     classical Ihara–Bass station (regular graphs)
    demos-kraus.js      worker K:     quantum Ihara–Bass / Kraus dichotomy station
    demos-as.js         worker AS:    Artin–Schreier transfer-matrix station
    demos-core.js       orchestrator: permutations, subshifts, the Gram construction, the Riemann case
    lanes/<name>.md     each worker: what was built, the maths used (with claim labels), the numbers
                        verified independently in Python (numpy is installed), and open issues
    lanes/check_<name>.py  each worker: the Python cross-check that produced those numbers

No build step, no modules, no external libraries except MathJax (loaded by index.html as `tex-svg`; call
`WT.typeset(el)` after injecting TeX into an element; prefer plain HTML/Unicode labels inside demos).
Plain ES2020, works from disk and when served. Everything must work at 400px width (SVGs: `viewBox` +
class `plot`). Respect `prefers-reduced-motion` (`WT.reducedMotion()`). Every control has a stable `id`
prefixed with the demo id. Colours ONLY through `WT.col()` (returns the token values) or `var(--token)`
in SVG attributes; both themes must look right. Keep each module under ~450 lines; no framework.

## Mount API

Each demo is `WT.demos.<name> = function(root){...}` where `root` is the `<div class="demo wide"
id="demo-<name>">` present in index.html (the orchestrator writes the `.cap` caption paragraph inside it
before the mount; append after it). Fill it with a `.controls` row (use `WT.slider`, `WT.button`,
`WT.select`, `WT.checkbox`), a `.grid2`/`.grid3` of `svg.plot` figures (`WT.svgIn`), and a `.readout`.
Return nothing. index.html calls `WT.mountAll()` on DOMContentLoaded. Modules must not touch anything
outside their root except `WT`.

Helpers in core.js: `WT.svg.{el, clear, text, polyline, axis, plane, heat, bars}`, `WT.col()`,
`WT.CYC` (12 categorical colours), `WT.fmt/fmtF/fmtC`, `WT.jacobiEig` (real symmetric),
`WT.hermEigvals(Re, Im)`, `WT.toeplitz`, `WT.toeplitzC`, `WT.toeplitzMins(t, K)` (min eigenvalue for each
window size), `WT.matmul`, `WT.powerTraces(A, K)` (Tr A^k, k = 0..K), complex pairs `WT.C`, complex
matrices `WT.cmat.{zeros, eye, fromReal, mul, add, scale, dagger, kron, trace, frob, powerTraces, ad, inv,
charpoly, eigvals}` (eigvals is charpoly + Durand–Kerner: fine to dimension ~12, do not use on larger
matrices; get large spectra from a formula such as Ihara–Bass instead), `WT.polyRoots`,
`WT.movie(root, {viewBox, duration, frames:[{t, caption}], draw(svg, t, C), autoplay})` (a scrubbable
animation with play/pause and captions), `WT.mountAll`.

## Colour semantics (keep them)

`--orbit` orbits / cycles / primes / counting side; `--spec` eigenvalues / zeros / anything negative or
broken; `--pole` the trivial set (pole, leading eigenvalue, the `+-1` of Ihara–Bass); `--arch` the
archimedean place and the doubled (bra) layer of a transfer matrix; `--bond` bond legs and Gram/strip
objects; `--metric` the metric `G` and its seams. True reference values: `--ink2` hollow markers.

## Lane reports

`lanes/<name>.md`: sections *Built*, *Mathematics used* (statement, claim label, where the demo computes
it), *Independent check* (Python numbers, and the same numbers as the demo prints them, side by side),
*Findings against the brief* (anything in the brief that turned out wrong or needed a convention fixed),
*Open*. Numbers in the demo readouts must agree with the Python check to the printed digits.
