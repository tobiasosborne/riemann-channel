# Lane G: the classical Ihara–Bass station (regular graphs), 2026-09-26

## Built

`demos-graphs.js` (232 lines, plain ES2020). It holds the numerics in `WT.graphNum` (`LIST, KT, analyse, spectra,
closedWalk, toeplitzMins`), which run without a DOM, plus two demos.

Graphs (all built by code): K4, cube Q3 (= C4 × K2), Petersen, K3,3, Heawood (LCF [5,−5]^7), prism C6 × K2,
prism C16 × K2, prism C21 × K2 (added: the reviewer's non-bipartite, non-Ramanujan CL_21), K5, octahedron K2,2,2, and
circulant C8(1,2). The Paley graph on 9 vertices was skipped. Both demos default to Petersen, and each keeps its own selection.

* `WT.demos.graphWalk` (`#demo-graphWalk`). Controls: `-graph` (select), `-L` (3..12), `-new`, `-play`. It draws the graph
  (circular or two-ring layout) and a random closed non-backtracking walk found by a randomized DFS. The DFS is pruned by the
  counts `(B^k)[e][e1] > 0`, so it never hits a dead end. Played edges are drawn in orbit colour and the current directed edge
  in bond colour with an arrow. The MPS ring shows L boxes labelled `u→v`, a bond ring and physical legs `e1..eL`. The
  readout gives `Tr(A_{e_L}...A_{e_1}) = 1 for this word; ring norm Tr B^L = … closed non-backtracking walks of length L
  (each counted from every starting edge); all closed walks, backtracking allowed, Tr A^L = …`. When `Tr B^L = 0` it says
  that no such walk exists. A table lists Tr B^l and Tr A^l for l = 1..12. Play respects reduced motion.
* `WT.demos.graphs` (`#demo-graphs`). Controls: `-graph`, `-K` (2..16, default 12).
  - (a) Adjacency spectrum from Jacobi, with the band [−2√q, 2√q] shaded and ±(q+1) in pole colour. Marked *comparison*.
  - (b) Hashimoto modes, i.e. the roots of μ² − aμ + q, on the plane with the circle √q. The trivial q, 1 (and −q, −1) are
    in pole colour, and the ±1 × (|E|−|V|) are shown as pole squares. Marked *comparison*.
  - (c) ν_l for l = 0..24, with the window 0..K emphasised and a dashed ν₀ line. Below it, Huang's h_k = ν₀ − ν_k for
    k = 1..24, coloured by sign.
  - (d) Heat map of the Toeplitz matrix (ν_|j−k|), j,k = 0..K, and λ_min of every window 0..K′ (orbit colour if ≥ −1e−9,
    spec colour if negative).
  - Readout: |V|, |E|, |E|−|V|, q, bipartite or not, the trivial set, √q, ν₀ = 2|V|−2 (or 2|V|−4), the ν formula,
    λ_min at K, min h_k over k ≤ 24, Ramanujan or not (comparison), max retained |μ| (comparison), the retained-sum check,
    and the required sentence (thm:weil-duality-pairing; inverse pairing).
  - Option (e), "break the graph", was dropped, as the brief allowed.

## Mathematics used

* Hashimoto operator (`def:hashimoto-operator`): `B[e][f] = 1` iff head(e) = tail(f) and f ≠ reverse(e). Dart i+|E| is the
  reverse of dart i. Tr B^l = N_l, the number of closed non-backtracking walks (`def:ihara-zeta`). As a TN: the bond space is
  C^{2|E|}, and `A_e = Σ_{e' follows e} |e'><e|`.
* Rescaled trace sequence (`def:rescaled-trace-sequence`) with r = √q:
  `ν_l = q^{−l/2}(Tr B^l − q^l − 1 − (|E|−|V|)(1+(−1)^l) − [bipartite]((−q)^l + (−1)^l))`.
  It is computed only from `Tr B^l` (the powers `B^k = B·B^{k−1}`), plus q, |E|−|V| and bipartiteness. Bipartiteness comes
  from BFS 2-colouring, which is structural, not spectral. The graphs are connected, so the trivial pair is removed once.
* Ihara–Bass (`def:ihara-bass`) is used only in the comparison panels and the checks.
* T1/T2: `thm:weil-positivity-finite`, `thm:weil-duality-pairing`, `prop:weil-orbit-negative`. The Ramanujan property is
  `def:ramanujan-graph`. Huang's criterion is X1 in `notes/weil-positivity.md`.
* Trivial set (as in `thm:kraus-weil-criterion` (ii) for the graph case): {q, 1} for a = q+1, {−q, −1} for a = −(q+1) if
  bipartite, and ±1 with multiplicity |E|−|V| each.

## Independent check (`lanes/check_graphs.py`, numpy; output reproduced by `node` on `WT.graphNum`)

* Tr B^l from matrix powers equals Ihara–Bass (Σ over all a of both roots, plus (|E|−|V|)(1+(−1)^l)) for l ≤ 24 on every
  graph. The largest difference is 2.8e−7, on the octahedron, where Tr B^24 ≈ 3e11.
* The Tr B^l and Tr A^l lists for l = 1..12 are identical, as integers, in Python and JS for all 11 graphs.
* Max over l ≤ 16 of |Σ_retained μ^l − q^{l/2} ν_l| / q^{l/2} (should be below 1e−9 on every graph):

| graph | Python | demo | graph | Python | demo |
|---|---|---|---|---|---|
| K4 | 7.6e−15 | 5.3e−15 | C16×K2 | 6.6e−13 | 1.6e−11 |
| Q3 | 2.1e−14 | 4.5e−14 | C21×K2 | 9.4e−12 | 1.5e−10 |
| Petersen | 2.8e−14 | 4.5e−14 | K5 | 1.1e−14 | 1.9e−15 |
| K3,3 | 1.8e−14 | 4.3e−15 | octahedron | 9.6e−15 | 2.6e−14 |
| Heawood | 3.2e−14 | 2.0e−13 | C8(1,2) | 8.3e−15 | 1.9e−14 |
| C6×K2 | 2.0e−14 | 4.8e−14 | | | |

  (These are comparison-side residuals from the eigenvalue solvers, not printed digits. Over l ≤ 24 the JS figure for C21×K2
  would be 2.5e−9, so the check is stated over the window range l ≤ 16.)

* The Weil numbers. Python and the demo readout print the same values to the digits shown. λ_min is for the (K+1)×(K+1)
  window; "0.0000" means |λ| < 5e−5, with the true values being round-off near zero of either sign.

| graph | |E|−|V| | bip | ν₀ | λ_min K=4 | K=8 | K=12 | K=16 | min h_k (k≤24) | Ramanujan |
|---|---|---|---|---|---|---|---|---|---|
| K4 | 2 | no | 6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0006 (k=13) | yes |
| Q3 | 4 | yes | 12 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3125 (k=10) | yes |
| Petersen | 5 | no | 18 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2305 (k=16) | yes |
| K3,3 | 3 | yes | 8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 (k=4) | yes |
| Heawood | 7 | yes | 24 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 (k=6) | yes |
| C6×K2 | 6 | yes | 20 | 4.6916 | 0.1221 | 0.0000 | 0.0000 | 0.4922 (k=16) | yes |
| C16×K2 | 16 | yes | 60 | 37.0570 | 24.0990 | 1.2122 | −29.1705 | −8.5146 (k=22) | no (a = 2.8478) |
| C21×K2 | 21 | no | 82 | 53.5708 | 6.0387 | −144.4253 | −689.4374 | −5268.6877 (k=24) | no (a = 2.9777) |
| K5 | 5 | no | 8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.1811 (k=10) | yes |
| octahedron | 6 | no | 10 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.1311 (k=20) | yes |
| C8(1,2) | 8 | no | 14 | 0.4380 | 0.0000 | 0.0000 | 0.0000 | 6.0741 (k=6) | yes |

  Petersen ν_0..16 (both): 18.0000 −2.1213 −7.5000 −3.1820 −6.7500 15.3796 5.6250 −11.4021 −1.6875 −6.7617 8.9063
  13.0594 −11.6719 −4.3421 −3.3984 1.9390 16.7695.
  `F()` in the script rounds exact binary ties away from zero, the way `toFixed` does (for example 8.90625 → 8.9063).
  numpy's default printing would give 8.9062.

## Findings against the brief

1. **Prism C16 × K2 at K = 12.** The "−60.46" in the brief is the 12×12 window (lags 0..11) with {−q, −1} *not*
   removed. The check reproduces −60.4628 for that wrong trivial set, and −104.7982 at size 13. With the correct bipartite
   trivial set, λ_min is +1.2122 at K = 12 (13×13). It first turns negative at K = 14 (−13.3842) and is −29.1705 at K = 16.
   The demo's K slider reaches 16, so the failure is visible. The readout at K = 16 shows −29.1705 and "not Ramanujan
   (a = 2.8478 > 2√q = 2.8284)".
2. **Huang's h_k is not negative within k ≤ 16 for the prism.** The prism's ν stays below ν₀ = 60 up to k = 21. The first
   negative h_k is at k = 22 (−8.5146), then k = 26 and 28. The demo therefore always shows ν and h for l ≤ 24, independent
   of K. The Toeplitz form detects the failure earlier (K = 14) than the termwise test (k = 22). CL_21 fails both early
   (h_10 = −2.7812, λ_min < 0 from K = 9).
3. **What N_k means in X1.** In Huang's `h_k = 2(n−1) + q^{k/2} + q^{−k/2} − q^{−k/2} N_k`, N_k is **not** Tr B^k. It is
   `N_k = Tr B^k − (|E|−|V|)(1+(−1)^k)`, i.e. Tr B^k for odd k and Tr B^k − n(q−1) for even k. That is how the reviewer's
   `notes/reviews/scratch_weil_x1.py` codes it. (`scripts/weil_positivity.py` has no graph/Huang check; the K4/Petersen
   check lives in the review scratch.) With that N_k, the literal formula equals ν₀ − ν_k to ≤ 1.2e−10 on every
   non-bipartite graph here. The formula, as written, is for **non-bipartite** graphs. For bipartite ones the demo uses
   h_k = ν₀ − ν_k with ν₀ = 2|V| − 4 and {−q, −1} also removed.
4. **Walk search.** The walk is found by a randomized DFS pruned by (B^k)[e][e₁] > 0. It is still depth-first but never
   backtracks. The random walk is not uniform over closed walks.
5. **Label wording.** "backtracking closed walks Tr A^L" is printed as "all closed walks, backtracking allowed, Tr A^L".
   Tr A^L counts all closed walks, not only backtracking ones.
6. **Extra graph.** Added the prism C21 × K2 (non-bipartite, non-Ramanujan). It lets the literal Huang formula be shown
   failing, and it matches the reviewer's min h_k = −5268.7.

## Tests

* `node`: the stub pattern loads core.js and demos-graphs.js. All numbers above come from `WT.graphNum`. For every graph and
  every L = 3..12, the walk is closed and non-backtracking, and `null` is returned iff Tr B^L = 0.
* Playwright (node, chromium 1194 at /opt/pw-browsers):
  - light theme at 1000 px, prism C16 × K2 at K = 16, play pressed;
  - dark theme at 400 px.
  There were no console or page errors. Page scrollWidth equals the viewport (no horizontal scroll). The counts table
  scrolls inside its own `overflow-x:auto` box on phones. One fix pass: badges and titles de-overlapped, multiplicity labels
  thinned, heat-map title shortened, the left column stacks (a), (c) and h next to the plane (b), and round-off labels on
  the λ_min axis were suppressed.

## Open

* Stacked dots in (a) show multiplicities up to 6. Beyond that, a "×m" label is printed.
* The plane panel omits the "×m" labels when there are more than 12 distinct modes (the prisms), where every mode is double.
* Timing: the largest graph (126 darts, B^24) takes about 20 ms in node.
