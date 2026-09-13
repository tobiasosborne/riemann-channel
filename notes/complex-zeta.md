# An Ihara zeta for simplicial complexes: what exists, what the prover proved, what the numerics say

Worker note, 2026-09-13. Companion to the lab-book shards `RC-08D`, `RC-08E`,
`RC-08F` and the definitions shard `RC-02D`. Sources:
`notes/extract/complex-zeta-sources.md` (the literature sweep, sections C1–C10),
`notes/extract/cohomological-zeta-sources.md` (the torsion/fermion sweep,
sections A1–A2, B3–B7, C1, D1–D4, F1–F2), `notes/complex-zeta/astra-proofs.md`
(the prover's T0–T8), and `notes/a2-complex-zeta/numerics.md` with
`outputs/a2_complex_zeta.txt` (the PGL_3(F_3) lane).

---

## 1. The question

TJO asked, in effect: the Ihara zeta of a graph counts non-backtracking closed
walks, Bass's identity collapses that edge determinant to a vertex determinant,
and "RH" for it is exactly the Ramanujan property. A graph is a 1-complex.
What is the same story for a 2-complex? Is there a higher-dimensional Hashimoto
operator, a Bass identity, an RH-equals-Ramanujan theorem — and does the whole
thing grade by cell dimension into an even sector and an odd sector, with the
odd sector supplying "fermionic zeros" the way 1-forms supply the numerator of a
Ruelle zeta?

Three sub-questions fall out: (a) what is the right flow; (b) what is the
`(1-u^2)^chi` factor really (a torsion? a supertrace?); (c) what happens when
the edges carry quantum channels rather than scalars.

## 2. What the literature actually has

The short answer: **yes for quotients of affine buildings, and only there.**

* **Kang–Li (arXiv:0804.2305), Kang–Li–Wang (0809.1401v1).** For a torsion-free
  cocompact type-preserving `Gamma ⊂ PGL_3(F)`, the complex `X_Gamma = Gamma\B`
  has a zeta counting tailless primitive closed geodesics made of *same-type*
  edges, by *algebraic* length. It equals
  `(1-u^3)^chi / (det P_3(u) · det(I + L_B u))` with
  `P_3(u) = I - A_1 u + q A_2 u^2 - q^3 u^3 I`, and equally
  `1/(det(I - L_E u) det(I - L_E^t u^2))`. Note the base `(1-u^3)`, the **plus**
  sign in the chamber factor, and the `u^2` on the transposed edge factor.
* **RH is four-way equivalent to Ramanujan** — but it is not a single circle.
  The vertex cubic's nontrivial zeros lie on `|u| = q^{-1}`; the chamber
  factor's on **three** circles `1, q^{-1/2}, q^{-1/4}`; the edge factor's on
  **two**, `q^{-1}, q^{-1/2}`. In type `C~_2` (Fang–Li–Wang, 1109.3854) it
  degrades further to *bands*.
* **Kang–Yu (2607.21262, 2026)** give the uniform statement for every `PGL_n`:
  `(1-u^n)^chi L(Gamma, q^{(n-1)/2} u) = prod_{k=1}^{n-1} Z_k^eps(u)^{(-1)^{k+1}}`,
  an **alternating product over facet dimension**, each factor a plain
  reciprocal determinant of a successor operator on pointed `k`-facets. The
  Euler factor is *provably* a torsion: the alternating product of `det Phi_i`
  on cochains equals the same product on cohomology, where `Phi_i` acts by
  `1 - u^n`. This is Hoffman's reformulation of Bass, generalised. The paper
  states **no RH**.
* **Lubetzky–Lubotzky–Parzanchevski (1702.05452)** give the right
  higher-dimensional Hashimoto operator: a *branching* geodesic flow on pairs
  (basepoint, `j`-cell), geodicity being "the union must not be a cell". On a
  Ramanujan complex the digraph is Ramanujan and the zeta satisfies RH — but in
  the **one-sided** form `Re s ≤ 1/2`, and they say explicitly that the interior
  `0 < |Re s| < 1/2` really is occupied. **Kamber (1701.00154)** supplies the
  converse as an iff, in terms of Bernstein–Lusztig operators.
* **Off the buildings, nothing of the sort exists.** Storm's hypergraph zeta
  (math/0608761) does have a Bass identity and an iff Ramanujan theorem, but
  only because `zeta_H(u) = Z_{B_H}(sqrt u)` — it *is* the Ihara zeta of the
  incidence bipartite graph. Benard–Chaubet–Dang–Schick (2303.11226) give a
  combinatorial Ruelle zeta on an arbitrary triangulation with a Fried-type
  theorem, but no Ramanujan notion and no RH. Four papers say in their own
  words that the general object does not exist (Deitmar–Hoffman 2004,
  Lubotzky's 2018 ICM survey, Hong–Kwon 2024, Kang–Yu 2026).
* **The graded reading is in the literature, but elsewhere.** Deitmar
  (dg-ga/9511006) writes a geometric zeta as an alternating product over
  exterior degree and calls it a Deligne-type determinant formula; its divisor
  is a *degree-weighted* alternating sum, the plain Euler sum vanishing.
  Dyatlov–Zworski (1606.04560) have `zeta_R = zeta_1/(zeta_0 zeta_2)` on a
  surface, order `-chi`. Knill (2201.09412) shows graph analytic torsion is the
  **super** pseudodeterminant of the Dirac operator. Matsuura–Ohta (2501.08803)
  give a genuinely fermionic proof of Bass's identity on a graph, in which the
  Euler exponent `n_E - n_V` emerges as `det(I - tJ) = (1-t^2)^{n_E}` for the
  edge-reversal involution. None of these is about complexes.

No quantum-channel zeta of a complex exists anywhere in the literature.

## 3. What the prover formulated, and what it corrected

`codex:gpt-6-astra` was given the orchestrator's draft and the extracts. Its
first move was to separate three objects the draft had conflated:

1. the **ordered-cell flow** `T_k` of an arbitrary complex (drop the oldest
   vertex, append a new one, forbid the step a `(k+1)`-cell would short-cut);
2. the **pointed opposition flow** of a building (cyclic type ordering,
   algebraic step length `lambda_0`, successors *opposite* in the link);
3. Kang–Li's **edge-only** zeta.

They are different. In rank three the unrestricted ordered edge rule has
outdegree `2q^2+q = 21` where `L_E` has `q^2 = 9`; opposition is strictly
stronger than non-incidence; all `3!` chamber orderings give two
transpose-related orientation blocks, so `det(I + uT_2) = det(I + uL_B)^2`, not
`det(I + uL_B)`. And the `u^2` on the reversed-edge factor is an **algebraic
length**, not a matrix square or a multiplicity.

The main positive results:

* **T2.2, the universal Bass–Schur identity.** On *every* finite complex,
  `T_k = S_k R_k - F_k` with `F_k = C_k + R_{k+1} S_{k+1}`, and
  `det(I - zT_k) = det K_k(z) · det(I - z R_k K_k(z)^{-1} S_k)`. This is a
  *rational* compression by one dimension, not a polynomial vertex determinant.
  For `d = 1` it is Bass, with no regularity assumption.
* **T2.4, the tetrahedron obstruction.** On `∂Δ^3`, `T_1 = 0` and
  `det(I + uT_2) = (1-u^4)^6`; the demanded cubic collapse would force
  `det P = (1-u^3)^2/(1-u^4)^6`, which has poles. So there is **no** universal
  cubic vertex Bass identity for 2-complexes. Vertex collapse is a *building*
  phenomenon.
* **T1.1, the cochain cancellation**, in full generality (no `h^2 = 0`, no
  `h = d^*`). The exponent it produces is the dimension count of whichever
  complex you use: `chi` for ordinary cochains, `sum (-1)^i (i+1)! f_i` for
  ordered cells, `sum (-1)^i (i+1) f_i` for pointed cochains. A single edge
  already separates these (`chi = 1`, ordered `= 0`).
* **T3.1, the superdeterminant.** `Z_ord = sdet(I - u Theta)^{-1}` with
  `Theta = (+)_k (-1)^{k+1} T_k`, and `log Z_ord = sum_m u^m/m str(Theta^m)`.
* **T4.1/T4.2, the Dirac-type block matrix.** One explicit incidence matrix
  with two Schur evaluations reproducing both sides of the compression; but the
  *total* object is a Berezinian over auxiliary copies, not one ordinary
  Grassmann integral. Cell chirality and flow superparity are different
  gradings.
* **T5.2/T5.3, arbitrary weights.** Putting an arbitrary endomorphism on each
  directed edge preserves the Schur identity exactly — no positivity, pairing,
  invertibility or flatness needed. And `Tr(T^E_k)^m = sum |Tr(B_m...B_1)|^2 ≥ 0`
  for `Ad`-weights: **adjoint pairing is not required** for ring positivity.
* **T5.6/T5.7, the Artin decomposition and Euler bookkeeping**, on the *voltage
  quotient*, with exponents `a_rho` (not `d_rho`) for `R = pi ⊗ conj(pi)`.
* **T6.2, Harrow-type transfer.** The colour channels
  `Phi_k(X) = |S_k|^{-1} sum_{s in S_k} pi(s) X pi(s)^†` are commuting, normal,
  unital, trace-preserving, with common fixed space `pi(G)'`; their joint
  spectrum is a sub-multiset of the vertex joint spectrum. So a Ramanujan
  complex gives a **Ramanujan quantum expander of type Ã_{n-1} automatically**.

### The correction ledger (what was refuted)

The prover marked a long list FALSE-as-drafted. The ones that matter:

| drafted | correction |
|---|---|
| the total graded zeta equals Kang–Li's zeta | it equals `D_B/D_E = (1-u^3)^chi/det P_3`, the **completed vertex L-function**; Kang–Li's is `1/D_E` (T0.4) |
| the ordered flow is `k!` copies of the building flow | opposition is stricter than non-incidence; already the rank-three outdegrees differ (T0.3, T0.5) |
| Kang–Yu's cochain product has exponent `chi` | it has `sum (-1)^i (i+1) f_i`; `chi` appears only after subtracting the local `i f_i` terms (T1.2, T1.3) |
| universal cubic vertex Bass identity for every 2-complex | false on `∂Δ^3` (T2.4) |
| the zeros are exactly the odd eigenvalues | zeros are at *reciprocals* of *signed* eigenvalues, with net multiplicity after cancellation (T3.1) |
| chamber roots are uncancelled zeros of the vertex L-function | `L_vertex = 1/det P_3` is a reciprocal polynomial: they **all** cancel (T3.3) |
| `k`-cells realise `H^{k-1}` with Weil weight `k-1` | only the parity exponents match (T3.4, T3.5) |
| one pure fermion determinant gives the supertrace | a Berezinian with auxiliary copies is needed (T4.2) |
| adjoint pairing is needed for ring positivity | complete positivity suffices (T5.3) |
| the full-cover connection is a representation block | it is **pure gauge**; `C_4` with a 1-dim `pi` is a counterexample (T5.5) |
| removing channel fixed points removes all trivial modes | type characters survive and violate the tempered bound; remove the *exceptional space* (T6.1, T6.2) |
| one faithful `pi` detects Ramanujan | false on the `Z/28` Cayley graph with `S = {±1, ±3}` (T6.3) |
| the LLP condition says `|s| = 1` | the invariant statement is `Re s = 1`; the imaginary part is only defined mod `2pi/log b` (T6.4) |
| Kamber's bound is an upper bound on pole radii | it inverts: `|u| ≥ q^{-(p-1)/p}` (T6.4) |
| higher-rank RH has a duality | the tempered nonspherical chamber block has radii `q^{-1/2}` (×1) and `q^{-1/4}` (×2); no single `u -> c/u` fixes or exchanges them (T6.5) |

## 4. The numerics: PGL_3(F_3), 5616 vertices

An independent agent built the smallest Ã_2 Ramanujan complex exactly
(`scripts/a2_complex_zeta.py`, ~90 s, deterministic): the LSV Cayley complex of
`PGL_3(F_3)` at `q = 3, d = 3, e = 1`.

* `|G| = 5616`, f-vector `(5616, 73008, 97344)`, `chi = 29952 = |G|·16/3`,
  every vertex link the incidence graph of `PG(2,3)`.
* **Not 3-colourable** — `PGL_3(F_3)` is simple, so no epimorphism onto `Z/3`
  exists, and Kang–Li's hypothesis (I) *fails* on this quotient. A
  type-preserving 3-fold cover (16848 vertices, `chi = 89856`) is built too.
* All 13 generators have **order 3**, so the 24336 triangles carry `Z/3`
  stabilisers: `G` is free on vertices and edges but **not** on unpointed
  2-cells. This is precisely the caveat in the prover's T5.7.
* **Vertex spectrum:** exactly one trivial eigenvalue (13); all 5615 others
  tempered by Cohn's criterion (defect `2e-14`); `max|lambda| = 7.1269 < 9`. So
  the complex is Ramanujan and the vertex-cubic RH holds outright.
* **The identity.** Exact integer traces (free `G`-action, sparse int64 matvecs,
  no eigendecomposition) give, verified to `u^18` on the base **and** the cover:

  ```
  det P_3(u) · det(I + u L_B) = (1-u^3)^chi · det(I - u L_E) · det(I - u^2 L_E^t)
  ```

  degree 308880 on both sides, residual fitting `chi` exactly at every order.
  The placement written in the orchestrator's brief fails at `u^3` (residual
  `-59904`) and fails the degree count. `det(I - uL_B)` instead of
  `det(I + uL_B)` first fails at `u^15`. Notably the identity holds on the base
  even though type preservation fails there.
* **Prover cross-checks confirmed:** unrestricted ordered outdegree 21 (not 9);
  `Tr(T_2^m) = 2 Tr(L_B^m)` for `m ≤ 18`, i.e. `det(I+uT_2) = det(I+uL_B)^2`;
  and on `∂Δ^3`, `T_1 = 0` with `T_2` a permutation of cycle type `4^6`.
* **The three circles, exactly**, on two isotypic blocks: `L_B` radii
  `{1, 3^{1/4}, 3^{1/2}}`, `L_E` radii `{3, sqrt 3}` — and nothing else.
* **The quantum twist.** `pi` = the 12-dimensional irrep (the 13 points of
  `P^2(F_3)` minus the constant). The channels are unital, trace-preserving and
  commuting; the largest nontrivial `|13 mu| = 6.4817`, below `3q = 9` and below
  Hastings' `2 sqrt(D-1) = 6.9282` at `D = 13`; all 143 nontrivial joint
  eigenvalues sit inside the tempered deltoid. A Ramanujan quantum expander of
  type Ã_2, and it cannot fail, because `Phi_1 = A_1^{(pi ⊗ conj pi)}/13`.
* **Gauge and voltage.** The forward weights `pi(s)` are *not* flat (39 of 52
  chambers fail); the covariant weights `pi(s^{-1})` on the full complex are
  pure gauge, giving `det(I - uL_E)^{12}`. The genuine Artin object is the
  13-state voltage quotient. Euler bookkeeping per block, as `(1-u)^a (1-u^3)^c`:
  trivial `(13, 1)`, `1 ⊕ pi` `(13, 65)`, `pi` `(0, 64)`. For `pi` the naive
  `chi·dim/|G| = 64` is exactly right; the whole anomaly sits in the trivial
  block, where the fractional `16/3` is replaced by `(1-u)^13 (1-u^3)^1` —
  exactly the stabiliser caveat of T5.7, seen.

## 5. Verdict

The natural object is the **graded geodesic determinant of a complex with
specified geodesic data** — states, successor incidences, algebraic lengths,
transports — and not an unqualified "Ihara zeta of every complex". On an
arbitrary complex the universal statement is a *rational* compression that still
mentions the forbidden transitions; the polynomial vertex collapse is a building
phenomenon and dies on a four-vertex sphere.

The odd sector is real as a graded **presentation** and unreal as a **divisor**:
the superdeterminant identity is exact, but on the building vertex side the
chamber factor cancels completely, so "fermionic zeros" names a net odd
multiplicity that has to be checked *after* cancellation. The parallel with the
Ruelle picture and with Knill's supertrace is parity and alternating structure,
not an identification of spaces or weights.

The quantum version is the voltage-quotient Artin block; the connection on the
full cover is pure gauge and carries nothing. Harrow transfer then hands you
Ramanujan quantum expanders of type Ã_2 for free from a Ramanujan complex — the
channel adds no spectral values. But higher-rank RH is one-sided, the interior
of the band is genuinely occupied, and there is no universal duality to close
it. What remains is Weil-positivity-as-bound, `thm:weil-positivity-finite`
applied block by block.

None of this touches the Riemann side directly. What it buys is a supply of
exactly-solvable graded transfer operators with a Ramanujan property, and a
sharp negative: there is no zeta of a general complex to build a Phantasm on.

**Open.** A combinatorial characterisation of the complexes admitting a
prescribed low-degree vertex collapse (`conj:vertex-collapse-characterisation`).
Building quotients are sufficient; the tetrahedron gives a necessary
polynomiality condition; matching generalised-polygon link parameters is *not*
known to suffice.
