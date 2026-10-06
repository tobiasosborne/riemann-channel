# Other gauge groups on the super Ihara zeta: U(1), SU(2), S_d, SU(1,1)

Author: `claude:fable-5.1`, 2026-10-05, answering TJO ("the gauge field we add for super ihara totally suggests other
gauge groups. What happens if we add a U(1), or an SU(2), or ... some noncompact group like SU(1,1)"). Status: **a
discussion record, not a round.** Nothing computed beyond what the tutorial's demos compute for `Z_2`; each statement
carries a status: *standard*, *elementary* (follows from the vectorised proof in the tutorial's Section 4b), *reading*
(mine), *open* (I do not know). Nothing registered. Continues `graph-super.md`.

## Setting

A gauge field is a holonomy homomorphism `ρ: π_1(Y) → G`, equivalently `g_e ∈ G` on each directed edge with
`g_ē = g_e^{-1}`, modulo gauge changes at vertices. The twisted adjacency `A_ρ` acts on `C^n ⊗ V_ρ`.

- **Ihara–Bass holds for every group and every representation** (elementary): the proof of Section 4b used only
  `Fτ = σ`, i.e. `ρ(g_ē) ρ(g_e) = 1`, never unitarity. So
  `det(1 − uB_ρ) = (1 − u²)^{(|E|−|V|) dim ρ} det(1 − A_ρ u + q u²)`. This is the Artin–Ihara L-function
  (standard: Stark–Terras; matrix weights: Watanabe–Fukumizu, cited in the prior-art shard). The `Z_2` flux is the
  sign representation of a double cover.
- **The arithmetic ladder** (reading): trivial `ρ` is `ζ`; U(1) characters are Dirichlet and Hecke L-functions
  (RTP lane D); two-dimensional `ρ` are the GL_2 L-functions of elliptic curves (lane E). The HANDOFF remark "one
  state per Hecke character, the target is GRH for the family" is the U(1) gauge field in this language.

## U(1)

- **Gauge classes are the Brillouin torus** (standard): `H^1(Y, U(1)) = (R/2πZ)^g`, the torus of the tutorial's lattice
  state 1. A U(1) flux is a general momentum displacement of the comb on the cycle lattice `Z^g`; `Z_2` fluxes are its
  half-periods, `Z_N` fluxes its `N`-th periods (index-`N` sublattices `{a·x ≡ 0 mod N}`, GKP qudits, cyclic `N`-covers).
- `A_φ` is Hermitian, the Weil form `Q_φ` is Hermitian, RH at `φ` is `Q_φ > 0`, with no pole plane for `φ ≠ 0`
  (elementary).
- **RH cannot hold on all of the torus** (elementary): at `φ = 0` the eigenvalue `q + 1` is present, eigenvalues are
  continuous in `φ`, so a neighbourhood of `0` violates the band; the Ramanujan fluxes form a closed proper subset.
  The bands traced as `φ` varies are the Bloch bands of the maximal abelian cover, whose spectral radius is `q + 1`
  because `Z^g` is amenable (Kesten; standard).
- **RH on average survives** (standard, Godsil–Gutman with phases): with independent Haar phases every permutation
  term containing a cycle of length `≥ 3` is unbalanced and averages to zero; only dimers survive; the average of
  `det(x − A_φ)` over the torus is the matching polynomial. Equivalently it is the constant term of `det(x − A_φ)` as a
  Laurent polynomial on the torus, and in a graph disjoint simple cycles are homologically independent, so nothing
  else is null-homologous. Heilmann–Lieb puts the roots in the band.
- **Lattice state 2 needs roots of unity** (elementary): `M_φ` has entries `e^{iφ}` and preserves no lattice for
  generic `φ`; at `N`-th roots of unity it preserves `Z[ζ_N]^{2n}`, a `Z`-lattice of rank `2n φ(N)`, so the syndrome
  torus returns with complex multiplication by `Z[ζ_N]` (reading: the new part of the Jacobian of a cyclic cover).

## SU(2), U(d), S_d

- **Nonabelian holonomy sees `π_1`, not `H_1`** (elementary): the weight of a walk is `ρ` of its class in the free
  group `F_g`. The crystal of lattice state 1 is replaced by the universal cover, the tree, whose deck group is the
  lattice `graph-ihara.md` identified with the primes. No comb, no GKP structure. What remains is Fourier inversion
  over `G`: closed walks of length `k` with holonomy in a conjugacy class `C` number `(|C|/|G|) Σ_ρ χ_ρ(C)^* Tr B_ρ^k`
  (standard). "Dark" and "bright" generalise to the phases `χ_ρ(C)`; `Z_2` is `χ_sgn(−1) = −1`.
- **The averaging theorem changes** (elementary for the mechanism; open for the conclusion): for U(d), `d ≥ 2`, the
  U(1) centre still kills unbalanced terms, but a trail that goes out along a path and back using both spin indices
  (`a→b→c→b→a`) is balanced and survives with Weingarten weights, so the Haar average of `det(x − A_ρ)` is not the
  matching polynomial. For SU(2) there is no U(1) centre and more survives (the doublet is pseudoreal; for one edge
  `E[g_11 g_22] = E|α|² = 1/2 ≠ 0`). I know no Heilmann–Lieb theorem for these averages. For `S_d` (random `d`-covers)
  the answer is known: Hall–Puder–Sawin, the expected characteristic polynomial of the new part is the `d`-matching
  polynomial with roots in the band, giving Ramanujan `d`-covers of every graph (standard, from memory, not byte-cited).
- **Lattice state 2 returns only for finite image with an integral representation** (elementary): binary polyhedral
  subgroups of SU(2) over their rings of integers; generic SU(2) holonomy preserves no lattice.

## Noncompact groups: SU(1,1) and friends

- **SU(1,1) is the natural one** (reading): its two-dimensional representation acts on `(a, a†)`; an SU(1,1) gauge
  field puts a squeeze on every edge, on top of the global squeeze by `√q` in the step.
- **The Weil form becomes a Krein form** (elementary): with `η = diag(1, −1)`, `ρ(g)^{-1} = η ρ(g)^† η`, so `A_ρ` is
  `η`-Hermitian, the step is a similitude of `Ω ⊗ η` (`M^† (Ω ⊗ η) M = q (Ω ⊗ η)`), and `Q_ρ` is Hermitian for the
  indefinite inner product on `C^n ⊗ C²`. Eigenvalues are real or in conjugate pairs.
- **RH and positivity separate** (elementary): a positive invariant form still forces unimodular eigenvalues, but RH
  no longer forces positivity. If `A_ρ` has an eigenvector `v` with `λ` in the band and `⟨v, ηv⟩ < 0`, the mode's two
  lines lie on the critical circle while `Q_ρ` is negative definite on that plane. This is the Krein-definite
  distinction of shard 04q (`thm:deninger-invariant-polarisation`) and the Pontryagin-index remark of HANDOFF
  2026-09-26, realised on a finite graph.
- **Integral noncompact holonomy exists** (elementary): `SL(2, Z) ⊂ SL(2, R)`. The syndrome torus then exists and
  hyperbolic elements are cat maps, so the step generically violates RH on the edges; `lattice-tower.md`'s hyperbolic
  step is the one-mode case.
- **No Haar average, so no RH on average.** For infinite-dimensional unitary `ρ`, `A_ρ` is Hermitian but `A_ρ` is not
  trace class, so there is no determinant; the right question is the spectrum. Sufficient condition (standard,
  Kesten-type): if `ρ` is weakly contained in the regular representation of `π_1(Y)`, the spectrum of `A_ρ` lies in
  the tree band, because the regular representation is the tree. Ramanujan as temperedness, the Langlands form.
  Finite-dimensional unitary `ρ` are never tempered for a nonamenable `F_g` (`ρ ≺ λ` would give `1 ≺ λ`), so
  Ramanujan fluxes with finite gauge groups need a different mechanism (Deligne for the arithmetic ones, interlacing
  for existence).

## Next, if wanted

- A Part E of the tutorial: the Ramanujan locus of `K_4` on its three-torus and the Bloch bands of the lines as `φ`
  moves; an SU(1,1) demo of a mode on the circle with negative Krein signature.
- Compute the exact SU(2) and U(2) Haar averages of `det(x − A_ρ)` for `K_4` (Weingarten) before saying anything about
  their roots.
- Byte-cite Stark–Terras, Godsil–Gutman, Heilmann–Lieb, Hall–Puder–Sawin, Kesten before any registration.
