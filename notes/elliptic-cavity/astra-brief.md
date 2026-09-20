# Brief for the prover: two arithmetic cavities with cusps (elliptic curves over F_2 and F_3), their scattering matrices, the zeta identification, and the rebound channel

You are the prover in a mathematical research notebook (git repo, current directory). Author line
for everything you write: `codex:gpt-6-astra`. Write ONLY the file `notes/elliptic-cavity/astra-proofs.md`
(create it; overwrite if present). Do not edit anything else. Do not run git. You may run python3
(numpy, mpmath, sympy, scipy are installed) for checks, and you may read any file in the repo, especially
`report/sections/04i_cusp_graph_scattering.tex` and `report/sections/04j_cusp_graph_renewal.tex` (the
previous round: one finite core, one cusp, `R = -p/ptilde`, the one-exit contraction, the renewal channel
in discrete time), `notes/cusp-graph/astra-proofs.md` (its proofs and correction ledger),
`notes/reviews/cusp-graph-2026-09-20.md` (the review; finding 7 there is the demand you must confront in
T1(e)), `report/sections/04h_rebound_state.tex` (rebound densities, flags), and the source
`refs/src/2603.26443/final_draft.tex` (Arends--Peterson--Weich, "resonances on geometrically finite graphs
of groups"; lines 427--458 define the adjacency operator on a graph with stabiliser function, 1896--1925 the
resonance matrix, 1981--2068 the two elliptic-curve examples, 2069--2096 the four-type expectation). The
h-tail scattering matrix in the notebook's normalisation is also in `refs/src/1203.6557/` (Childs--Gosset,
Levinson's theorem for graphs II, `S(z) = -Q(z)^{-1} Q(1/z)` at line 365 and the h-tail count at 511).
Be elementary and explicit; the reader will run numerics against every formula. Do not pad.

## Why this problem

The notebook is chasing a *system* whose resonances are the Riemann zeros: an arithmetic cavity coupled
to cusps (TJO's picture: "a spiky object, like a hedgehog"; the modular surface is one candidate, not the
definition). The previous round built the toy (a finite core plus one tree-quotient ray) and proved that
the reflection coefficient is `R = -p/ptilde` with `p(z) = det((1+z^2) - z T_X - c^2 P_0)`, that the
resonances are the roots of `p` in the disc not shared with `ptilde`, and that for ANY one-exit no-event
contraction a rebound gives a renewal channel with the zeros protected. The reviewer's verdict: nothing
arithmetic was used. Arends--Peterson--Weich (APW, 2603.26443) supply the arithmetic: for the quotient of
the `(q+1)`-regular tree by `GL_2(R)`, `R` the coordinate ring of an elliptic curve minus its point at
infinity, the resonance determinant contains the Hasse--Weil numerator `P(mu^2)`, so the resonances are
the square roots of the inverse Frobenius eigenvalues, on `|mu| = q^{-1/4}` by Weil. APW leave the
Lax--Phillips / scattering reading to follow-up work. This round does exactly that reading on their two
examples, rigorously, in the notebook's normalisation, and then asks the notebook's questions: the
h-exit contraction, the renewal channel, which rebound the arithmetic picks, and whether the even sector
(the pole) ever leaks.

## The two diagrams (Section 0; hypotheses H-DIAG-2, H-DIAG-3)

A graph with stabiliser function (APW 427--458): vertices `v` with `S(v) > 0`, edges `e` with `S(e) > 0`,
measure `nu(v) = 1/S(v)`, adjacency `(A f)(v) = sum_{e: t(e) = v} (S(v)/S(e)) f(o(e))`, self-adjoint on
`l^2(V, nu)`, and `deg(v) = sum_{e at v} S(v)/S(e) = q+1` for a quotient of the `(q+1)`-regular tree.
The data below are transcribed from APW's figures (`refs/src/2603.26443/serre_example.png` and
`takahashi_example.png`; red = `S(v)`, green = `S(e)`); Takahashi's theorem that produces them is not in
the repository, so treat the data as hypotheses H-DIAG-2 / H-DIAG-3, and PROVE the two consistency checks
you can: every vertex has degree `q+1`, and the rank-one perturbed Bass determinant reproduces APW's
displayed resonance polynomial (their `det H(mu)`, lines 2007 and 2056) up to a monomial and a constant.

**D2** (`y^2 + y = x^3 + x + 1` over `F_2`, `q = 2`, one cusp; Serre, Trees, II.2.4.4). Core vertices
`A, B, C, D, E, F` with `S = 6, 2, 2, 1, 3, 3`; core edges `A-B (S=2)`, `B-C (2)`, `C-D (1)`, `D-E (1)`,
`D-F (1)`; the cusp is a ray `c_1, c_2, ...` attached at `B` by the edge `B-c_1 (S=2)`, with
`S(c_k) = 2^{k+1}` and `S(c_k - c_{k+1}) = 2^{k+1}`. (APW: `det H = (mu^2+1)^2 (mu^2-2)(2mu^4 - 2mu^2 + 1)`.)
The projective curve has `N_1 = 1`, `a = 2`, `P(T) = 1 - 2T + 2T^2`, Frobenius eigenvalues `alpha = 1 -+ i`,
`|alpha| = sqrt 2`, `|Pic(R)| = |E(F_2)| = 1`: one cusp. The function field `K = F_2(E)` has
`zeta_K(s) = P(q^{-s}) / ((1 - q^{-s})(1 - q^{1-s}))`.

**D3** (`y^2 = x^3 + x + 1` over `F_3`, `q = 3`, four cusps; Takahashi, Fig. 5). Core vertices
`L1p, L1, L2, X, Xp, Y, Z, Zp, Q` with `S = 48, 12, 6, 2, 8, 6, 12, 48, 4`; core edges `L1p-L1 (12)`,
`L1-L2 (6)`, `L2-X (2)`, `X-Xp (2)`, `X-Y (2)`, `X-Q (2)`, `Y-Z (6)`, `Z-Zp (12)`; four cusps: at `L1`
by an edge of `S = 12` to a ray with `S(c_k) = 12 * 3^k` (`36, 108, ...`) and edge stabilisers
`S(c_k - c_{k+1}) = S(c_k)`; at `Z` likewise (edge `12`, ray `36, 108, ...`); TWO at `Q`, each by an edge
of `S = 4` to a ray `12, 36, 108, ...` with `S(c_k - c_{k+1}) = S(c_k)`. (APW: `det H = (mu^2+1)^2
(mu-1)^2 (mu+1)^2 (mu^2-3)(3mu^4+1)`.) The curve has `N_1 = 4`, `a = 0`, `P(T) = 1 + 3T^2`, `alpha = +-
i sqrt 3`, `Pic(R) = E(F_3) = Z/4` (the point `(0,1)` has order 4): four cusps. NOTE the diagram has the
obvious reflection symmetry `L1p <-> Zp, L1 <-> Z, L2 <-> Y` (fixing `X, Xp, Q`) and the swap of the two
`Q`-cusps, a Klein four-group of automorphisms with cusp orbits `{L1, Z}` and `{Q_1, Q_2}`; it does NOT
have an automorphism group acting transitively on the four cusps (`S(L1) = 12 != S(Q) = 4`).

## Conventions (Section 0 must restate these and PROVE C1 to C3)

- **C1 (normalisation, h cusps).** With `g = f / sqrt(S)` the operator `A` becomes the symmetric kernel
  `sqrt(S(v) S(w)) / S(e)` on `l^2` with counting measure; divide by `sqrt q`. Prove: on every cusp ray
  (`S(c_{k+1}) = q S(c_k)` and `S(c_k - c_{k+1}) = S(c_k)` for `k >= 1`) this is the standard path
  adjacency `(T g)(k) = g(k+1) + g(k-1)`; the junction `v - c_1` becomes the coupling `c` with
  `c^2 = S(v) S(c_1) / (q S(e)^2) = S(v)/S(e)` (use the degree condition at `c_1`), i.e. APW's `c_v`;
  for the Nagao cusp of `PGL_2(F_q[T^{-1}])` this is `q+1` (shard 04i C1) and for D2, D3 every cusp
  junction has `c^2 = 1` (two cusps at `Q` give `C_{QQ} = 2`). So the notebook's operator is
  `T = T_X (+) (+)_a T_ray^{(a)} + sum_a c_a (|v_a><r_1^{(a)}| + h.c.)` on `l^2(V_X) (+) (+)_a l^2(N)`,
  `a = 1..h`, and the core matrix is `T_X = D^{-1/2} A_X D^{-1/2} / sqrt q`, `D = diag S`. Write out `T_X`
  for D2 (`6 x 6`, entries like `sqrt(3/2)`, `1/sqrt 2`, `1`) and D3 (`9 x 9`).
- **C2 (the h-exit scattering matrix).** For `|z| = 1`, `z != +-1`, let `g^{(b)}` be the generalised
  eigenfunction `T g = (z + 1/z) g` with `g^{(b)}(r_k^{(a)}) = delta_{ab} z^{-k} + S_{ab}(z) z^k`. With
  `G(lambda) = (lambda - T_X)^{-1}` and the `h x h` matrix `Gamma(lambda)_{ab} = c_a c_b G(lambda)_{v_a v_b}`,
  I get `S(z) = (z Gamma - 1)^{-1} (1 - z^{-1} Gamma)`. Prove: `S` is symmetric (`S = S^T`), rational in `z`
  with real coefficients, unitary on `|z| = 1`, `S(z) S(1/z) = 1`, `S(conj z) = conj S(z)`, and
  `det S(z) = (-1)^h p(z)/ptilde(z)` with `p(z) = det((1+z^2) - z T_X - C)`, `ptilde(z) = det((1+z^2) - z T_X
  - z^2 C) = z^{2n} p(1/z)`, `C = sum_a c_a^2 P_{v_a}` (Sylvester's identity for `det_h(1 - z Gamma) =
  det_n(1 - z G C)`). Reconcile with Childs--Gosset's `S = -Q(z)^{-1} Q(1/z)` and with APW's
  `det H(mu)`: `det H(mu) = (-1)^n (2 mu)^{-n} det((1+mu^2) - mu T_X - C)` (the reviewer's check), so
  APW's `mu` IS the notebook's `z` and their resonances are the roots of `p` in `C^x`.
- **C3 (zeros, poles, the root at `z = 0`, thresholds).** Transcribe 04i C2 to `h` cusps: poles of `det S`
  in `|z| < 1` are real and are the `l^2` eigenvalues of `T` on `Y` outside `[-2, 2]`; common factors of
  `p`, `ptilde` are the cusp forms (eigenvectors of `T_X` vanishing at every attachment vertex, extended by
  zero; for `h > 1` there may be more: eigenvectors of `T_X` orthogonal to the span of the `v_a`? decide) and
  the threshold roots `z = +-1`; the resonances are the remaining roots of `p` in `|z| < 1`. NEW: `p(0) =
  det(1 - C) = prod_v (1 - C_vv)`, which VANISHES for D2 and D3 (`c^2 = 1`). Decide and prove what a root of
  `p` at `z = 0` is: I claim it is a genuine eigenvalue `0` of the compressed operator (a mode that leaves
  after a finite delay; the model case `T_X = [0]`, `c = 1` is a ray with one extra vertex and `R = -z^2`,
  a pure delay of two steps, `K` two-dimensional, `Z` nilpotent), APW discard it (`mu in C^x`), Weil's
  circle statement excludes it. State the order of vanishing of `p` at `0` for D2 (I get 2) and D3 (4) and
  relate it to `rank(1 - C)` and the attachment geometry. For thresholds: APW count `mu = +-1` as
  resonances of multiplicity 2 in D3 ("topological"), while in 04i the common factors `(z -+ 1)^2` cancel in
  `det S`; decide whether the MATRIX `S(z)` is regular at `+-1` for D3 (I expect a nontrivial limit, with
  the multiplicity visible in the Levinson count `1203.6557:511`), and give the count of resonances (with
  multiplicity, `z = 0` included, thresholds excluded) for D2 and D3: I get `N(D2) = 6 = 4 + 2` and
  `N(D3) = 8 = 4 + 4`.

## Statements to prove or correct (Sections 1 to 6)

- **T1 (D2 exactly: the one-cusp elliptic cavity).** Prove, by finite computation from H-DIAG-2:
  (a) `p(z) = (z^2/2)(z^2 - 2)(z^2 + 1)^2 (2z^4 - 2z^2 + 1)` and `ptilde(z) = -(1/2)(z^2 + 1)^2 (2z^2 - 1)
  (z^4 - 2z^2 + 2)`, so `R(z) = z^2 (z^2 - 2)(2z^4 - 2z^2 + 1) / ((2z^2 - 1)(z^4 - 2z^2 + 2))`.
  (b) With `z = q^{s - 1/2}` (so `q^{-2s} = z^{-2}/q`, `q^{1-2s} = z^{-2}`):
  `1/R(z) = z^{-2} zeta_K(2s-1)/zeta_K(2s)` EXACTLY, `K = F_2(E)`; compare with the pure Nagao cusp,
  `1/R = q zeta_{F_q(T)}(2s-1)/zeta_{F_q(T)}(2s)` (04i C3). So the scattering matrix of the elliptic cavity is
  the zeta ratio of its function field, up to the monomial `z^{-2} = q^{1-2s}`. State the general
  prefactor you can defend: with two data points (`g = 0`: `q`; `g = 1`: `q^{1-2s}`) the pattern
  `q^{1 - 2gs}` fits; mark it H-EIS (the constant term of the Eisenstein series on `GL_2(R) \ T`, Li 1979,
  not in the repo) and do not assert it.
  (c) The spectrum: `l^2` eigenvalues of `T` on `Y`: the Perron pair `lambda = +-3/sqrt 2` (`z = +-1/sqrt 2`,
  the constant function and its bipartite twin) and the cusp forms at `lambda = 0` (`z = +-i`; APW say two
  `l^2` eigenfunctions at each of `+-i`; determine `dim ker T_X` and whether both vanish at `B`, and why
  the factor is `(z^2+1)^2`); resonances: the four roots of `2z^4 - 2z^2 + 1`, i.e. `z^2 = 1/alpha`,
  `alpha = 1 -+ i`, `|z| = 2^{-1/4}`, plus `z = 0` twice; no threshold roots. Then the structural statement:
  D2 is bipartite, so `sigma T sigma = -T` for the parity sign `sigma`, the resonances come in `+-` pairs,
  and the compressed operator `Z` (T3) satisfies `sigma Z sigma = -Z`; on the four-dimensional Hasse--Weil
  sector `Z^2` has spectrum `{1/alpha, 1/conj alpha}` each with multiplicity two: `Z` is a square root of
  the inverse Frobenius on `H^1(E)` tensored with the bipartite sign. State exactly in what sense.
  (d) Weil's RH for `E` is the statement that all four Hasse--Weil resonances share the modulus
  `q^{-1/4}`; it is TRUE here (Hasse), and it is the notebook's RH(Y) (04j) for the Hasse--Weil sector.
  Give `|z| = 2^{-1/4} = 0.840896...` and the resonance angles.
  (e) Confront the previous review's finding 7 (`notes/reviews/cusp-graph-2026-09-20.md`, table row 7):
  "with `c^2 = q+1` and the Perron pair as the only bound states, `prod |z_i| = 1`, impossible, so any
  arithmetic quotient with resonances must have `l^2` spectrum outside the band beyond the Perron pair".
  D2 has resonances and NO such spectrum. Explain: the arithmetic junction has `c^2 = S(v)/S(e) = 1`, not
  `q+1` (the cusp attaches at a vertex whose stabiliser equals the edge's, unlike the Nagao cusp), so
  `p(0) = 0` and the product identity of 04j (`prod` of all roots `= 1 - c^2`) is vacuous. Give the corrected
  identity: the product of the NONZERO roots of `p` in terms of the data (for D2 I get, from the
  factorisation, `prod_{nonzero} = (-2)(1)(1/2) = -1` in some normalisation; derive it as a determinant or
  coefficient statement valid for any core with one `c = 1` junction, e.g. the coefficient of `z^2` in `p`),
  and restate the reviewer's demand correctly for arithmetic diagrams.
- **T2 (D3 exactly: the four-cusp hedgehog).** Prove, by finite computation from H-DIAG-3:
  (a) `p(z) = (z^4/3)(z - 1)^2 (z + 1)^2 (z^2 - 3)(z^2 + 1)^2 (3z^4 + 1)` and `ptilde(z) = -(1/3)(z-1)^2
  (z+1)^2 (z^2+1)^2 (3z^2 - 1)(z^4 + 3)`; `det S = p/ptilde`.
  (b) The Klein symmetry block-diagonalises `S(z)` in a `z`-INDEPENDENT basis of the exit space `C^4`:
  the antisymmetric `Q`-combination `(Q_1 - Q_2)/sqrt 2` has `S = -1` identically (prove: it vanishes at
  `Q`, a Dirichlet end, `R = -1`); the antisymmetric `(L1 - Z)/sqrt 2` combination has `S = +z^2`
  identically (I found this numerically at three points; prove it: the odd sector is the core `{L1p, L1,
  L2}` with a Dirichlet condition at `X`, and its `p_odd`, `ptilde_odd` must satisfy `p_odd = z^2
  ptilde_odd` up to sign; find the reason, e.g. a hidden transparency of that three-vertex core); the
  symmetric two-dimensional block `S_even(z)` on `span{(L1+Z)/sqrt 2, (Q_1+Q_2)/sqrt 2}` has
  `det S_even = z^2 zeta_K(2s)/zeta_K(2s-1)`, `K = F_3(E)`, `P(T) = 1 + 3T^2`, i.e. the same form as D2's `R`
  (I checked numerically that the product of its two eigenvalues equals `1/(z^{-2} zeta_K(2s-1)/zeta_K(2s))`).
  (c) The Hasse--Weil resonances of D3 are the roots of `3z^4 + 1`, `z^2 = 1/alpha = -+ i/sqrt 3`,
  `|z| = 3^{-1/4}`, all in the even block; the root `z = 0` has order 4 (two in the even block, two in
  the odd `z^2` channel: prove the split); the thresholds `+-1` (multiplicity 2 each) cancel in `det S`;
  the `l^2` spectrum: Perron pair `z = +-1/sqrt 3`, cusp forms at `z = +-i` (`lambda = 0`, multiplicity?).
  (d) H-CLASS (the number-field pattern; Efrat/Hejhal for `SL_2(O_F)`: the scattering matrix over the
  cusps = ideal classes is diagonalised by class-group characters `chi` into `L(2s-1, chi)/L(2s, chi)`).
  Here `Pic(R) = Z/4` but the diagram's automorphisms are only the Klein group, and the even `2 x 2`
  block does NOT have `z`-independent eigenvectors (its two eigenvalues are not individually rational of
  the form monomial times zeta ratio: numerically at `z = 0.8 + 0.1i` they are `-1.19997 + 0.27727i` and
  `0.80005 + 0.10680i`). Decide: is there a diagonal monomial renormalisation `D(z) = diag(z^{a}, z^{b})`
  (the two `Q`-cusps start one step deeper than the `L1`, `Z` cusps: `12, 36, ...` versus `36, 108, ...`)
  such that `D S_even D` has `z`-independent eigenvectors, with eigenvalues `{monomial x zeta_K(2s)/zeta_K(2s-1),
  monomial}`? (For an unramified nontrivial character of a genus-one function field, `L(s, chi) = 1`, so
  H-CLASS predicts exactly one zeta block and three monomial-or-constant blocks; `-1` and `z^2` are two of
  them.) Prove or refute for D3 by exact computation. If refuted, say what the correct statement is (the
  cusps of a graph of groups are not permuted by the class group; the class-group structure lives in the
  Eisenstein normalisation, not in the ray normalisation) and mark the general form H-CLASS.
- **T3 (the h-exit contraction and the renewal channel; generic).** Transcribe 04i T1 and 04j T3--T5 to
  `h` exits, on the model side rigorously and on the geometric side under the same hypothesis as 04i
  (H-LP: the energy completion and the repair `D_+ = O_+ cap O_-^perp`, reviewer's MINOR T1c, inherited,
  not re-litigated). (a) The inner part: `S(z)` is an `h x h` rational matrix function, unitary on the
  circle, with poles in the disc at the `l^2` eigenvalues; removing them by Blaschke--Potapov factors gives
  an inner rational matrix function `Theta(z) = eta S(z) B_bd(z)` (state the order of factors and the
  constant unitary `eta`); the model space `K = H^2(C^h) (-) Theta H^2(C^h)`, `Z = P_K M_z|_K`
  (or its adjoint: fix the convention so that `spec Z` = the resonances, as in 04i), `dim K = deg det
  Theta` = the number of resonances with multiplicity INCLUDING `z = 0`, `Z^m -> 0`, `1 - Z^* Z = J^* J`
  with `J: K -> C^h` of rank `<= h` (the exit map), Jordan blocks of `Z` at `0` allowed (D2: a nilpotent
  block of size 2? decide), the Gram identity for simple nonzero resonances `<k_n, k_m>(1 - conj z_n z_m)
  = a_n^* a_m` with `a_n in C^h` the exit amplitudes, and "no mode decoupled from every cusp". (b) The
  renewal channel with an `h`-dimensional exit: for a CPTP map `Phi: B(C^h) -> B(K)` (the rebound: how the
  flux that left through the cusps is reinserted), `E_Phi(rho) = Z rho Z^* + Phi(J rho J^*)`; prove CPTP,
  Kraus form, the holding-time law now `h x h` matrix-valued (`M(m) = J Z^{m-1} Phi(.) Z^{*(m-1)} J^*`),
  finite mean, stationary density `rho_inf` by the renewal sum, uniqueness iff irreducibility, attraction
  iff aperiodicity, and the mode-diagonal criterion: every mode-diagonal rebound on a family of NONZERO
  resonances is stationary iff their moduli coincide (04j T4), mean holding time `1/(1 - r^2)`;
  a mode-diagonal rebound charging a `z = 0` mode is never stationary together with the Hasse--Weil modes
  (moduli `0 != q^{-1/4}`): so the "arithmetic" rebounds are those supported on the Hasse--Weil sector.
  (c) Symmetry: if a finite group acts on the diagram by automorphisms, `Z` and `J` are covariant, `K`
  splits into isotypic blocks, and a covariant `Phi` gives a channel that is a direct sum over blocks plus
  intertwiners only where the exit representations coincide; apply to D3: `K = K_even (+) K_odd`, the
  Hasse--Weil modes and two delay modes in `K_even`, two delay modes in `K_odd` (from `Theta_odd = z^2`),
  nothing from the `-1` channel (`K = 0` there: a Dirichlet end has no model space). Say what the hedgehog
  adds to the one-cusp cavity: for genus one, only trivial channels.
- **T4 (does the arithmetic pick the rebound? D2 concretely).** On `K(D2)` (six-dimensional: the
  Hasse--Weil sector `K_HW`, four modes, and the delay sector, two modes):
  (a) The canonical cusp rebound `Omega_J = J^* J / Tr(J^* J)` (flux returns where it left). Compute
  `rho_inf`, its spectrum, the holding-time law `m(m) = |<j| Z^{m-1} |j>|^2 / ||j||^2` (with `j = J^*
  1`), its generating function `mhat(u)` in closed form through `Theta` (Sz.-Nagy--Foias: `Theta(u) =
  [-Z + u D_{Z^*}(1 - u Z^*)^{-1} D_Z]|_{D_Z}` gives the exit-to-exit transfer function; derive `mhat`
  from it), aperiodicity (note `c = 1` here, the case 04j flagged for a modal rebound; `Omega_J` is not
  modal, decide), and whether `rho_inf` is supported on `K_HW`.
  (b) Mode-diagonal rebounds on `K_HW`: all stationary (Weil), mean holding time `1/(1 - 2^{-1/2}) = 2 +
  sqrt 2`; compare `2` for the modular surface (04h) and `1/(1 - q^{-1/2})` in general; the spectrum of
  `rho_inf = Omega` is the Gram spectrum (04h reviewer M1), not the weight list. Compute the Lax--Phillips
  Gram matrix of the four Hasse--Weil modes in closed form in terms of `alpha` (entries
  `a_n^* a_m / (1 - conj z_n z_m)` with the amplitudes from `Theta`), and the `4 x 4` `sigma`-structure.
  (c) The arithmetic inner product. `Z|_{K_HW}` is diagonalisable with all `|z_i| = q^{-1/4}`, so there
  exist inner products on `K_HW` for which `q^{1/4} Z` is unitary; the Lax--Phillips energy inner product
  is NOT one of them (the Gram matrix of (b) is not diagonal): quantify (the angles between modes, in
  closed form). Prove: `q^{1/4} Z` is unitary for `<.,.>'` iff the eigenvectors are `<.,.>'`-orthogonal;
  the set of such inner products is a cone of dimension 4 (the positive diagonal weights in the eigenbasis)
  modulo scale; the `sigma`-symmetric and real-structure-symmetric (`z -> conj z`, from the real
  coefficients) ones form a smaller cone: describe it. This is the notebook's "RH = Ramanujan = the
  compressed operator is `q^{-1/4}` times a unitary" made literal for the elliptic cavity: TRUE for a
  natural family of inner products, FALSE for the Lax--Phillips one; say which the renewal channel with a
  mode-diagonal rebound "uses" (its stationary state is diagonal in the eigenbasis with spectrum = weights
  exactly when `rho_inf` is read in an inner product of the cone).
  (d) Hecke and Bost--Connes: OPEN. One paragraph, no proofs: a Hecke operator on the diagram needs the
  double-coset structure (not only the stabiliser sizes) so it cannot be built from H-DIAG alone; say
  what data would be needed and what a Hecke-invariant rebound would mean (the Eisenstein series at a
  resonance is a Hecke eigenfunction, so a Hecke-covariant `Phi` would have to be mode-diagonal on the
  Hasse--Weil sector: is that a theorem given only that Hecke operators commute with `T` and preserve the
  cusp asymptotics? state it as H-HECKE).
- **T5 (the even sector never leaks on a finite-volume diagram).** Prove: on every graph with
  stabiliser function of finite volume (`sum_v 1/S(v) < infinity`) and bounded degree the constant function
  is an `l^2` eigenfunction of `A` (eigenvalue `q+1` if `(q+1)`-regular), hence in the notebook's
  normalisation the Perron mode is a bound state, stationary under the wave group, invisible to every cusp,
  and no choice of rebound gives it an exit: the vacuum (the pole at `s = 1`) has no exit on any
  finite-volume diagram, however many cusps (the hedgehog does not help). Then the observation (no proof
  needed, OPEN): APW's FUNNELS (infinite-volume ends, quotients by hyperbolic elements) are exits for the
  constant mode (on a funnel the constant function is not `l^2`); a diagram with one cusp and one funnel is
  the smallest candidate for "zeros from the cusp, vacuum leak from the funnel". Write the funnel
  self-energy in the notebook's normalisation (APW's `f_v /(sqrt q mu)` versus the cusp's `c_v sqrt q/mu`,
  line 1900) so the next round can build it, and say what the funnel does to `p`: `p_funnel(z) = det((1+z^2)
  - z T_X - C_cusp - q^{-1} C_funnel)`? derive.
- **T6 (genus, class number, and the number-field hedgehog).** One paragraph, no new proofs: for a curve
  of genus `g` and `h = |Pic(R)|` cusps, H-CLASS predicts one block carrying `zeta_K` (`2g` zeros, `4g`
  resonances after the square root and the bipartite doubling: check `4g = 4` on D2, D3) and `h - 1` blocks
  carrying `L(s, chi)` for the nontrivial unramified characters, polynomials of degree `2g - 2`: for `g = 1`
  no zeros (D3 confirms: `-1`, `z^2`, and a second even eigenvalue), for `g >= 2` zeros on every spike; for
  a number field (Efrat 1991 is only `PGL_2(F_q[T])`; Hejhal for `SL_2(O_F)`, not in the repo) every spike
  carries Hecke `L`-zeros. State the prediction for a genus-2 diagram as the testable consequence, and
  keep H-ARITH (the `Gamma_0(N)` / Dirichlet-`L` direction) as stated in 04j.

Declare every hypothesis you need as `H-*` (H-DIAG-2, H-DIAG-3, H-EIS, H-CLASS, H-LP, H-HECKE, ...).

## Output format

`notes/elliptic-cavity/astra-proofs.md`, in Markdown with `$...$` math (or plain ASCII math), with:
0. Author line, list of hypotheses `H-*`, and Section 0 (the diagrams, C1 to C3 with proofs, the two
   consistency checks of the transcription).
1. Sections 1 to 6 for T1 to T6, each statement labelled `T<n>` (and `T<n>(a)` etc.), each with STATUS one
   of PROVED / PROVED-CONDITIONAL (on which H-*) / CORRECTED (state the corrected version, then prove it) /
   OPEN (say exactly what is missing).
2. A **correction ledger**: a numbered table of every place where my draft was wrong, too strong, or
   needed a hypothesis, with the fix.
3. Numerical checks: any python you ran, with the numbers; keep it short. Include at least: both
   determinants, `1/R` against the zeta ratio at three points, the three eigenvalue channels of D3, the
   `Omega_J` stationary state of D2 and its holding-time law.
4. A closing list "What a refuter should attack first", 3 to 5 lines.

Standard facts (Sz.-Nagy--Foias model theory, Blaschke--Potapov factorisation, the renewal theorem,
GKLS, Hasse's theorem, Serre's description of `GL_2(R) \ T`) may be cited as "standard (no local
source)" per the notebook's convention; anything from the notebook cite by claim id and
`report/sections/<file>:<line>`; anything from APW or Childs--Gosset cite by `<arxiv-id>:<file>:<line>`.
