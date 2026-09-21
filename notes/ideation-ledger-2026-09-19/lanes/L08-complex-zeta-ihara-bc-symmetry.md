# Lane L08: simplicial-complex zeta, quantum Ihara, prior art, BC symmetry generators

Compiled 2026-09-19. Every idea, lead, conjecture, "what if", "open", "not done",
reviewer suggestion and dead route found in the eight assigned files. The established
mathematics is summarised only far enough to make each lead intelligible.

## Coverage

| file | lines | read fully? | ideas found |
|---|---|---|---|
| `notes/complex-zeta.md` | 238 | yes | 20 (the worker-note framing, the literature leads, the open conjecture, the verdict) |
| `notes/complex-zeta/astra-brief.md` | 33 | yes | 13 (TJO's framing questions and the drafted-but-deliberately-too-strong statements T0–T8) |
| `notes/complex-zeta/astra-proofs.md` | 1152 | yes | 36 (T0.1–T8.3, hypotheses H-*, the 34-row correction ledger) |
| `notes/reviews/complex-zeta-2026-09-13.md` | 694 | yes | 9 (two sharpenings, one recorded observation, three MINOR findings, the "Not checked" list, Round 2) |
| `notes/a2-complex-zeta/numerics.md` | 237 | yes | 11 (structural surprises, the method notes, §7 "what was not done") |
| `notes/quantum-ihara-general.md` | 118 | yes | 7 (Theorem 1 and its corollaries, §6 "what this does and does not give") |
| `notes/prior-art-quantum-ihara.md` | 137 | yes | 11 (the four founding claims, the gaps, the unfetched sources, the search limits) |
| `notes/bc-symmetry-generators.md` | 336 | yes | 14 (B0–B6, the counterexample, the open list) |

Total entries below: 81.

---

## Ideas and leads

### L08-001 The founding question: an Ihara zeta for 2-complexes that grades into an even and an odd sector
- Source: `notes/complex-zeta.md`:15-22; `notes/complex-zeta/astra-brief.md`:3
- Raised by: TJO
- Status at last mention: pursued; partially answered, mostly negative (shards `RC-08D`, `RC-08E`, `RC-08F`, definitions shard `RC-02D`)
- Content: A graph is a 1-complex; its Ihara zeta counts non-backtracking closed walks, Bass collapses the edge determinant to a vertex determinant, and "RH" is exactly the Ramanujan property. TJO asked for the same story on a 2-complex: a higher Hashimoto operator, a Bass identity, an RH-equals-Ramanujan theorem, and a grading by cell dimension into an even sector and an odd sector, "with the odd sector supplying 'fermionic zeros' the way 1-forms supply the numerator of a Ruelle zeta". The answer found: yes for quotients of affine buildings and only there.
- Lead: the concrete next step was to fix the *definition* first (T0 of the brief, "THE POINT OF T0 IS TO FIX THE DEFINITION THAT MAKES THE REST TRUE"). If the graded object existed for general complexes it would supply a supply of transfer operators with numerators, i.e. candidate Phantasms.
- Related: L08-002, L08-017, L08-037, L08-077.

### L08-002 "These zeros may be associated naturally with surface-like qualities"
- Source: `notes/complex-zeta/astra-brief.md`:3 (verbatim TJO quote); `notes/complex-zeta/astra-proofs.md`:1010; `notes/complex-zeta.md`:215-220
- Raised by: TJO
- Status at last mention: raised, partially explored; the surviving version is much weaker than the phrase suggests
- Content: TJO's intuition was that the zeros of a complex-zeta should behave like the cohomology of a surface. The prover's verdict: "The surface-like feature that survives scrutiny is the possibility of an odd chamber contribution to a graded divisor. It is not an identification with surface cohomology or a universal Betti-number formula."
- Lead: none stated beyond "check after cancellation"; the honest form of the question is whether any specified geodesic data gives an odd sector that survives cancellation (L08-018).
- Related: L08-018, L08-019, L08-034.

### L08-003 The three sub-questions: which flow, what is `(1-u^2)^chi` really, what happens with channels on edges
- Source: `notes/complex-zeta.md`:24-26
- Raised by: orchestrator (Claude), distilling TJO
- Status at last mention: all three answered (T0, T1, T5 respectively)
- Content: (a) what is the right flow on a complex; (b) is the trivial factor a torsion or a supertrace; (c) what happens when edges carry quantum channels instead of scalars. Answers: (a) there are three inequivalent flows and only the building one gives the strong theorems; (b) it is a finite determinant-line/torsion cancellation, with the exponent depending on which cochain complex you use; (c) arbitrary channel weights preserve the Schur identity and nothing else.
- Lead: none stated; each part became its own entry.
- Related: L08-015, L08-020, L08-024.

### L08-004 Kang–Yu's alternating product over facet dimension, with no RH attached
- Source: `notes/complex-zeta.md`:45-52; `notes/complex-zeta/astra-proofs.md`:183-193 (H-KY), :834-877 (T6.2 part 5)
- Raised by: a paper (Kang–Yu, arXiv:2607.21262, 2026), read by the orchestrator
- Status at last mention: registered as hypothesis H-KY; the missing RH is explicitly open
- Content: For every `PGL_n`, `(1-u^n)^chi L(Gamma, q^{(n-1)/2} u) = prod_{k=1}^{n-1} Z_k^eps(u)^{(-1)^{k+1}}` — an alternating product over facet dimension, each factor a reciprocal determinant of a successor operator on pointed `k`-facets. The Euler factor is *provably* a torsion. "The paper states **no RH**." T6.2 part 5: "In general rank, H-KY gives the determinant identity, **not** a list of prescribed RH circles for all its factors."
- Lead: prove a general-rank RH for the Kang–Yu factors (or show it fails). That would be the first higher-rank RH-equals-Ramanujan theorem with an explicit alternating/graded presentation. Needs H-STRONG (Iwahori-spherical temperedness) plus the branching hypotheses of H-LLP, per T6.2 part 5.
- Related: L08-005, L08-033, L08-081.

### L08-005 The higher-rank RH is one-sided and the interior of the band is genuinely occupied
- Source: `notes/complex-zeta.md`:53-59, :225-228; `notes/complex-zeta/astra-proofs.md`:64 (H-LLP), :906-924 (T6.4)
- Raised by: a paper (Lubetzky–Lubotzky–Parzanchevski, arXiv:1702.05452), amplified by the prover
- Status at last mention: pursued, negative for the Phantasm
- Content: On a Ramanujan complex the branching geodesic digraph is Ramanujan and its zeta satisfies RH, but only in the one-sided form `Re s <= 1/2`, and the source says explicitly that the interior `0 < |Re s| < 1/2` is occupied. Kamber (1701.00154) gives the converse as an iff in terms of Bernstein–Lusztig operators. So the higher-dimensional RH is a band, not a line, and in Weil-positivity language it is a bound without a duality.
- Lead: find the missing duality, or accept "Weil-positivity-as-bound applied block by block" (`thm:weil-positivity-finite`). If a duality were found for the chamber factor it would close the band and give a Hilbert–Pólya reading; T6.5 proves that no *single* such duality exists for the type-(e) block.
- Related: L08-034, L08-035, L08-078.

### L08-006 Storm's hypergraph zeta is the Ihara zeta of the incidence bipartite graph at `sqrt u`
- Source: `notes/complex-zeta.md`:60-63; `notes/complex-zeta/astra-brief.md`:6 (item C6)
- Raised by: a paper (Storm, math/0608761), recorded by the orchestrator
- Status at last mention: raised, not pursued
- Content: `zeta_H(u) = Z_{B_H}(sqrt u)`, so Storm's object does have a Bass identity and an iff Ramanujan theorem — but only because it *is* a graph zeta in disguise. It is the one genuinely non-building higher-dimensional object in the sweep with both properties.
- Lead: nobody asked whether the *quantum* twist of the incidence bipartite graph gives a useful channel object, or whether a hypergraph with matrix weights (the Watanabe–Fukumizu setting, L08-045) supplies a graded example. Cheap to check and it is the only known escape from the "buildings only" verdict.
- Related: L08-045, L08-011.

### L08-007 Benard–Chaubet–Dang–Schick: a combinatorial Ruelle zeta on an arbitrary triangulation, with no Ramanujan notion
- Source: `notes/complex-zeta.md`:63-67; `notes/complex-zeta/astra-brief.md`:6 (item C8)
- Raised by: a paper (arXiv:2303.11226), recorded by the orchestrator
- Status at last mention: raised, not pursued
- Content: For a triangulated closed `n`-manifold the signed zeta `prod(1 - eps_gamma z^{|gamma|})` over primitive geodesics in the `(n-1)`-skeleton is a **polynomial vanishing to order `b_1` at `z = (n+2)^{-1}`** — a Fried-type theorem. It has no Ramanujan notion and no RH.
- Lead: this is the only object in the sweep that both exists on an arbitrary complex *and* has a genuine numerator whose order is a Betti number. Ask whether its zeros can be given a spectral radius statement (a Ramanujan property), which is exactly what it lacks. If yes, it would be the general-complex graded object the lane failed to find elsewhere.
- Related: L08-008, L08-021, L08-037.

### L08-008 Deitmar's degree-weighted alternating product and the vanishing plain Euler sum
- Source: `notes/complex-zeta.md`:68-73; `notes/complex-zeta/astra-proofs.md`:466 (H-RUELLE), :468-475 (T3.7)
- Raised by: a paper (Deitmar, dg-ga/9511006), used by the prover
- Status at last mention: raised, comparison explicitly restricted
- Content: Deitmar writes a geometric zeta as an alternating product over exterior degree and calls it a Deligne-type determinant formula; its divisor is a *degree-weighted* alternating sum `-sum_p p(-1)^p dim H^p`, and the plain Euler sum vanishes there. T3.7: the parallel with the notebook's supertrace is "alternating determinant structure" only — `sum (-1)^i Tr` is not `sum i(-1)^i dim`, and neither formula imports into the other.
- Lead: none stated. But the *degree-weighted* insertion is the one insertion that makes the plain Euler sum vanish, which is exactly what a numerator-carrying zeta would want. Nobody asked what a degree-weighted flow supertrace would be on a complex.
- Related: L08-021, L08-017.

### L08-009 Knill: graph analytic torsion as the super pseudodeterminant of the Dirac operator
- Source: `notes/complex-zeta.md`:73-75; `notes/complex-zeta/astra-proofs.md`:213-226 (T1.4, H-TORS)
- Raised by: a paper (Knill, arXiv:2201.09412)
- Status at last mention: pursued, negative as an identification
- Content: `SDet(D) = prod_k Det(D_k)^{(-1)^k}` with `Det` a **pseudodeterminant** and `D_i = d_i^* d_i`, with an even/odd rooted-spanning-tree matrix-tree theorem. The tempting identification with the `u -> 1` limit of the trivial factor is false: on one edge the Ihara zeta is 1, Knill's squared torsion is 2, and `lim (1-u^2)^chi = 0` — three different numbers.
- Lead: none stated. The even-over-odd rooted spanning tree interpretation is the only place in the sweep where a genuinely combinatorial "fermionic over bosonic" count appears; nobody asked whether it has a transfer-operator reading.
- Related: L08-022, L08-019.

### L08-010 Matsuura–Ohta's fermionic proof of Bass, with the Euler exponent from the reversal involution
- Source: `notes/complex-zeta.md`:74-78; `notes/complex-zeta/astra-proofs.md`:537 (H-MO), :539-546 (T4.3); `notes/prior-art-quantum-ihara.md`:30-42
- Raised by: a paper (Matsuura–Ohta, arXiv:2501.08803 / 2204.06424)
- Status at last mention: registered as H-MO; the complex generalisation attempted and only partly achieved
- Content: A Berezin-integral proof of Bass's identity on a graph, with a Dirac operator block off-diagonal between `n_V` vertex fermions and `2 n_E` edge fermions, gamma-five hermiticity, and the Euler exponent emerging as `det(I - tJ) = (1-t^2)^{n_E}` for the edge-reversal involution `J` (Foata–Zeilberger's `(1-u^2)^{c_1-c_0}`). T4.3 corrects the tempting reading: the exponent `f_1 - f_0` is a reversal-pair count minus a vertex-denominator count, **not** `dim H_1 - dim H_0 = 2f_1 - f_0`.
- Lead: generalise the gamma-five structure to complexes. T4.5 `<1>3` says explicitly that H-MO's stronger graph structure "cannot be imported without a separate construction" — that separate construction is an open task.
- Related: L08-022, L08-023.

### L08-011 No quantum-channel zeta of a complex exists anywhere in the literature
- Source: `notes/complex-zeta.md`:79; `notes/complex-zeta/astra-brief.md`:7 (item F2); `notes/prior-art-quantum-ihara.md`:22-26
- Raised by: orchestrator (Claude), from the literature sweeps
- Status at last mention: recorded as a gap, and explicitly *not* used as a theorem
- Content: There is no Ihara-type zeta for a general (non-building) complex and none with channel/Kraus weights. Four papers say so in their own words (Deitmar–Hoffman 2004, Lubotzky ICM 2018, Hong–Kwon 2024, Kang–Yu 2026). The prover's last ledger row is blunt: "A literature search finding no general/quantum zeta proves nonexistence — It does not."
- Lead: the gap is the notebook's opening. The concrete consequence if it worked: the twisted graded object would be new mathematics. But an actual impossibility proof (as opposed to a failed search) has never been attempted.
- Related: L08-049, L08-051, L08-057, L08-075.

### L08-012 `conj:vertex-collapse-characterisation` — which complexes admit a prescribed low-degree vertex collapse
- Source: `notes/complex-zeta.md`:234-238; `notes/complex-zeta/astra-proofs.md`:328-347 (T2.5), :1032-1035 (T7.1 `<1>2`), :1119-1122 (T8.2 `<1>2`)
- Raised by: orchestrator (Claude), sharpened by the prover
- Status at last mention: registered as a conjecture, sketched/unestablished
- Content: Building quotients are sufficient; the tetrahedron boundary gives a necessary polynomiality condition; "matching generalised-polygon link parameters is *not* known to suffice". T2.5 refuses to assert a link-parameter classification and refuses the converse (accidental determinant identities do not imply that links are buildings).
- Lead: find a combinatorial characterisation, or at least a non-building example that collapses. Consequence if it worked: a much larger supply of exactly-solvable graded transfer operators with a Ramanujan property than the building family.
- Related: L08-013, L08-014, L08-016.

### L08-013 `B_X(u)` — the exact algebraic (but non-combinatorial) criterion for vertex collapse
- Source: `notes/complex-zeta/astra-proofs.md`:342-347 (T2.5 `<1>3`)
- Raised by: codex prover (`codex:gpt-6-astra`)
- Status at last mention: proved-here as a criterion; not turned into a classification
- Content: Form `B_X(u) = (1-u^{d+1})^{chi(X)} / Z_ord(X,u)`. A proposed polynomial matrix `I - uA + sum_{j>=2} u^j Q_{j-1}` works exactly when its determinant equals `B_X`. Necessary conditions: `B_X` polynomial of degree at most `(d+1) f_0`, and the coefficient constraint `[u] det = -Tr A`.
- Lead: compute `B_X` over a census of small 2-complexes and look for the ones where it is polynomial of the right degree. That is a finite, scriptable search for a non-building collapse, and nobody ran it.
- Related: L08-012, L08-016, L08-038.

### L08-014 "Links are generalised polygons of the same parameters" as the collapse class
- Source: `notes/complex-zeta/astra-brief.md`:19 (T2(i), the orchestrator's expectation); `notes/complex-zeta/astra-proofs.md`:328-341 (T2.5), :338-340 (`<1>2`)
- Raised by: orchestrator (Claude) in the brief
- Status at last mention: raised, refuted as an assertion, left unestablished as a question
- Content: The brief expected the collapse class to be "those whose vertex links are all 'generalised polygons / incidence graphs of the same parameters', i.e. locally building-like". T2.5 `<1>2`: a link-parameter condition supplies neither a cyclic type structure nor an identified Bruhat–Tits universal cover; even a theorem that the universal cover is an affine building would need a further argument identifying the Hecke/cochain data.
- Lead: what *would* be needed is a recognition theorem (local links ⇒ building universal cover) plus a transfer of the Hecke data. Neither is assumed nor proved in the note.
- Related: L08-012.

### L08-015 T2.2, the universal Bass–Schur compression: the general-complex Bass identity that always exists
- Source: `notes/complex-zeta/astra-proofs.md`:245-279 (T2.2), :229-243 (T2.1); `notes/complex-zeta.md`:101-105; review `notes/reviews/complex-zeta-2026-09-13.md`:125-147
- Raised by: codex prover, answering the brief's demand "WRITE IT DOWN, it is the general-complex Bass identity"
- Status at last mention: proved-here; reviewer VALID; exact on all 13 test complexes
- Content: On *every* finite complex, `T_k = S_k R_k - F_k` with `F_k = C_k + R_{k+1} S_{k+1}`, and `det(I - zT_k) = det K_k(z) det(I - z R_k K_k(z)^{-1} S_k)` with `K_k(z) = I + zF_k`. This is a *rational* compression by one dimension, not a polynomial vertex determinant; for `d=1` it is Bass with no regularity assumption. The `d=2` total is `Z_ord = det K_2(-u) det M_2(-u) / [det K_1(u) det M_1(u)]`.
- Lead: this is the object to build on for arbitrary complexes. The honest caveat: "Calling `M_1` a 'vertex determinant' is valid only if its rational dependence on the full forbidden-transition matrix is stated." Nobody has asked what the poles of `M_k` mean spectrally.
- Related: L08-016, L08-022, L08-024.

### L08-016 T2.4, the tetrahedron obstruction: no universal cubic vertex Bass identity for 2-complexes
- Source: `notes/complex-zeta/astra-proofs.md`:300-327 (T2.4); `notes/complex-zeta.md`:106-110; review :157-168
- Raised by: codex prover, refuting the brief's deliberately-too-strong T2 draft
- Status at last mention: FALSE-as-drafted; corrected statement proved-here; reviewer VALID
- Content: On `∂Δ^3`, `T_1 = 0` and `det(I + uT_2) = (1-u^4)^6`. The demanded cubic collapse would force `det P = (1-u^3)^2/(1-u^4)^6`, which has poles at `u = -1` and `u = ±i`, so is not a polynomial of any size or degree. Vertex collapse is a *building* phenomenon and dies on a four-vertex sphere.
- Lead: none (this is the negative). See Dead routes.
- Related: L08-012, L08-013, L08-022.

### L08-017 T3.1, the superdeterminant presentation: the graded zeta as `sdet(I - u Theta)^{-1}`
- Source: `notes/complex-zeta/astra-proofs.md`:350-375 (T3.1), :985-1011 (T7.1); `notes/complex-zeta.md`:116-117
- Raised by: orchestrator in the brief (T3), proved by the prover
- Status at last mention: proved-here; reviewer VALID including the sign law `s_k^{m+1}`
- Content: `Z_ord = sdet_W(I - u Theta)^{-1}` with `W_+ = ⊕_{k odd} H_k`, `W_- = ⊕_{k even, k>=2} H_k`, `Theta = ⊕_k (-1)^{k+1} T_k`, and `log Z_ord = sum_m (u^m/m) str(Theta^m) = sum_m (u^m/m) sum_k s_k^{m+1} Tr(T_k^m)`. The order at `u_0 != 0` is the odd algebraic multiplicity minus the even algebraic multiplicity of `u_0^{-1}`.
- Lead: this is the exact graded presentation TJO wanted; the caution is L08-018. The reviewer checked the sign law against the plausible wrong variant `s_k^m`, which fails — a fact worth keeping if anyone re-derives it.
- Related: L08-001, L08-018, L08-025.

### L08-018 The odd sector is real as a presentation and unreal as a divisor: the chamber factor cancels completely
- Source: `notes/complex-zeta/astra-proofs.md`:391-400 (T3.3), :1010 (T7.1 closing); `notes/complex-zeta.md`:215-220; review :198-207
- Raised by: codex prover, correcting the drafted reading
- Status at last mention: FALSE-as-drafted (the drafted "chamber roots are uncancelled zeros"); the corrected statement is proved-here and reviewer VALID
- Content: `L_vertex(u) = D_B(u)/[(1-u^3)^chi D_E(u)] = 1/det P_3(u)` is a *reciprocal polynomial*, so it has **no finite zeros**: every apparent numerator zero cancels against an edge or Euler factor. "'Fermionic zeros' therefore describes net odd multiplicity in a specified graded presentation and must be checked after cancellation."
- Lead: find geodesic data where the odd sector survives cancellation. That is the sharp form of TJO's question and it is completely open. The reviewer records the extra twist (L08-028): in a twisted block the Euler factor is not even a power of `1-u^3`, so the cancellation bookkeeping changes block by block.
- Related: L08-002, L08-017, L08-028, L08-037.

### L08-019 The cell-dimension ↔ cohomology dictionary is parity only; no canonical cohomological realisation
- Source: `notes/complex-zeta/astra-proofs.md`:401-418 (T3.4), :1119-1122 (T8.2 `<1>2`); `notes/complex-zeta.md`:147
- Raised by: orchestrator in the brief (T3: "`k`-cells ↔ `H^{k-1}`, so a graph is 'H^0 only'"), refuted by the prover
- Status at last mention: FALSE-as-drafted as a literal identification; the parity comparison is proved-here; a canonical realisation is "sketched/unestablished"
- Content: The substitution `i = k-1` matches the Grothendieck–Lefschetz exponents `(-1)^{i+1}` but identifies no spaces and assigns no Weil weight. A 3-cycle already disproves the literal reading: six ordered-edge states versus one-dimensional ordinary `H^0`, and the graph also has nonzero `H^1`. "The word '`H^0` only' can describe the absence of an odd **flow** sector, not the ordinary cohomology of a graph."
- Lead: "None of these results constructs ordinary cohomology whose Frobenius is the cell flow" (T7.1 `<1>2`). Constructing one is the open task; it would be the actual Weil-cohomology analogue the Phantasm wants.
- Related: L08-002, L08-020, L08-035.

### L08-020 Which representation constituents supply which of the three chamber circles
- Source: `notes/complex-zeta/astra-proofs.md`:419-447 (H-KL-TABLE, T3.5); `notes/complex-zeta.md`:40-44; review :216-232 (byte-checked row by row)
- Raised by: orchestrator in the brief (T3 asked "which part of `det(I + L_B u)` is the honest weight-1 sector"), answered by the prover
- Status at last mention: conditional-on H-KL-TABLE; reviewer VALID, all four rows byte-exact
- Content: The circle `q^{-1/2}` contains all principal-series chamber roots and one root from each tempered nonspherical type-(e) constituent; `q^{-1/4}` comes from the other two type-(e) roots; the unit circle comes from Steinberg twists; one-dimensional constituents give *trivial* roots at `q^{-1}`, outside the three nontrivial circles. "A full type-(e) constituent contributes to two circles simultaneously. Extracting its single `q^{-1/2}` root is a spectral factorization, not a canonical simplicial cohomology group."
- Lead: the "weight-1, curve-like" sector exists only as a spectral factorization. If someone wants a curve analogy they must first make that factorization canonical. Also recorded: the non-tempered type-(d) row has chamber roots `±q^{3/4} chi^{-1/2}`, outside the unit disc, which is where the stale numerical prediction `q^{3/4}` came from.
- Related: L08-019, L08-034, L08-073.

### L08-021 The vanishing order at `u^n = 1` is `chi - ord det P_n`, with no universal Betti formula
- Source: `notes/complex-zeta/astra-proofs.md`:448-465 (T3.6); review :233-240
- Raised by: orchestrator in the brief (T3: "is the vanishing order the plain `chi` or a weighted one?"), answered by the prover
- Status at last mention: conditional-on H-KY for the building case; the general no-formula implication proved-here
- Content: `ord_{u_0} Z_pt = chi(X) - ord_{u_0} det P_n` at `u_0^n = 1`; on a connected rank-three Ramanujan quotient this is `chi - 1` at each cube root of unity. But for the ordered default there is no formula at all: `Z_ord(Δ^2) = 1` despite `chi = 1`, and `Z_ord(∂Δ^3)` has order **6** at `u = 1` despite `chi = 2` and `b_1 = 0`.
- Lead: the order-6 on the tetrahedron boundary is a naked combinatorial number with no topological interpretation. Finding what it counts (six chamber 4-cycles) in general might be a small structural theorem.
- Related: L08-008, L08-016, L08-038.

### L08-022 T4.1/T4.2, the Dirac block matrix, and the distinction between cell chirality and flow superparity
- Source: `notes/complex-zeta/astra-proofs.md`:478-536 (T4.1, T4.2); `notes/complex-zeta.md`:118-122; review :253-270
- Raised by: orchestrator in the brief (T4 asked for a single gamma-five Dirac operator giving both forms), partially delivered by the prover
- Status at last mention: T4.1 proved-here and reviewer VALID; the drafted single-fermion-determinant claim is FALSE-as-drafted
- Content: One explicit `3x3` incidence matrix `D_k(z)` on `H_{k-1} ⊕ H_k ⊕ H_{k+1}` has two Schur evaluations giving both the flow determinant and the compressed form. But the *total* object is `sdet D_flow(u) = Z_ord(u)^{-1}` and needs auxiliary copies of some cell spaces: an ordinary Grassmann integral gives `det D`, not a ratio. "Cell chirality and flow superparity are distinct gradings": a `(k-1)`-cell used as an auxiliary variable in `D_k` has a different parity from the same cell as a flow state in `D_{k-1}`.
- Lead: construct geodesic data in which the two gradings do coincide. That is precisely what would make "fermionic zeros" a statement about cells rather than about an auxiliary bookkeeping device.
- Related: L08-010, L08-017, L08-023.

### L08-023 The doubled cochain linearisation `B(u)`, and why `delta^2 != 0` blocks the naive Laplacian
- Source: `notes/complex-zeta/astra-proofs.md`:547-600 (T4.4, T4.5), :597-599 (`<1>3`); review :279-296
- Raised by: codex prover
- Status at last mention: conditional-on H-KY; reviewer VALID (byte-checked that Kang–Yu state `delta_i ∘ delta_{i+1} != 0`)
- Content: `B(u)` on `C ⊕ C[1] ⊕ C[1]` with blocks `(cI, d, delta; -delta, I, 0; -d, 0, I)` is an even operator whose Berezinian is `c^{chi_pt}`. It exists because `(d+delta)^2 = d delta + delta d + delta^2` carries an *extra degree-(-2) term*, so the building "Laplacian" is not a square of a Dirac operator.
- Lead: "H-MO's stronger graph structure cannot be imported without a separate construction." Constructing a genuine self-adjoint/gamma-five Dirac operator for building cochains is an open task; it is the piece that would make the Berezinian a physics object rather than a bookkeeping trick.
- Related: L08-010, L08-022.

### L08-024 T5.2/T5.3: arbitrary (non-positive, non-invertible, non-flat) weights preserve the Schur identity and give a positive ring
- Source: `notes/complex-zeta/astra-proofs.md`:603-668 (T5.1–T5.3); `notes/complex-zeta.md`:123-126; review :305-320
- Raised by: orchestrator in the brief (T5), proved by the prover
- Status at last mention: proved-here; reviewer VALID
- Content: Putting an arbitrary endomorphism on each directed edge preserves `T_k^E = S_k^E R_k - F_k^E` and the Schur factorisation exactly — "without any positivity, pairing, invertibility, or flatness assumption". And `Tr(T_k^E)^m = sum_{based closed walks} Tr_V(E_m···E_1)`, which for `Ad`-weights is `sum |Tr(B_m···B_1)|^2 >= 0`. **Adjoint pairing is not needed** — complete positivity suffices.
- Lead: the notebook now has, for free, a quantum twist of *every* complex. The unexploited part: the pair factor `det_V(I - u^2 E_{(y,x)}E_{(x,y)})` for non-inverse-paired weights, which in dimensions above one does *not* remove the upper-face term `R_{k+1}S_{k+1}^E`.
- Related: L08-025, L08-029, L08-045.

### L08-025 Side A is a positive ring norm for *every* `k`, so the numerator must come from the alternating signs between `k`'s
- Source: `notes/complex-zeta/astra-brief.md`:25 (T5(c), stated as the target proposition); `notes/complex-zeta/astra-proofs.md`:641-668 (T5.3), :669-680 (T5.4)
- Raised by: orchestrator in the brief, proved by the prover
- Status at last mention: proved-here
- Content: By the notebook's no-go argument, since each single flow `T_k^E` has a nonnegative Kraus trace sequence, "the zeros-as-odd-sector structure of T3 must come from the alternating signs between different `k`, not from any single `T_k`". T5.4 restates it: "In this finite-transfer model the numerator of the graded zeta comes from net odd multiplicity between sectors, not from an unsigned individual Kraus flow."
- Lead: this is the lane's sharpest structural statement for the Phantasm: a grading is not optional. It is exactly the parent notebook's `thm:no-ungraded-trace`, arrived at independently.
- Related: L08-026, L08-017, L08-048.

### L08-026 Positivity alone does *not* forbid a numerator: `(1-u)/(1-2u)`
- Source: `notes/complex-zeta/astra-proofs.md`:669-680 (T5.4); review :321-330 (adjudication against the registered notebook theorem)
- Raised by: codex prover; adjudicated by the Opus reviewer
- Status at last mention: proved-here; reviewer VALID and explicitly checked for conflict with `report/sections/04b_phantasm_forced.tex`
- Content: `(1-u)/(1-2u)` has nonnegative Taylor coefficients and positive log-coefficients `(2^m-1)/m` yet a nonconstant reduced numerator. So the brief's loose phrase "no bosonic (positive) ring norm can produce a zeta with a numerator" is false as worded. The reviewer's adjudication: the registered `thm:no-ungraded-trace` proof is a **residue-sign** argument that never uses positivity, and the prover's example is an *instance* of it (`N_m = 2^m - 1^m`), so this is a sharpening, not a contradiction. The operative hypothesis is "is an honest trace", not "is positive".
- Lead: the wording in the notebook's own framing should be fixed wherever it says "positive"; the correct hypothesis is "is a trace sequence". Also recorded: T5.4 argues only finite-dimensionally, whereas the registered theorem covers trace-class operators via Lidskii.
- Related: L08-025.

### L08-027 The full-cover connection is pure gauge; the genuine Artin object is the voltage quotient
- Source: `notes/complex-zeta/astra-proofs.md`:681-708 (T5.5), :709-738 (T5.6); `notes/a2-complex-zeta/numerics.md`:181-198; `notes/complex-zeta.md`:127-128, :197-204; review :331-359
- Raised by: codex prover, refuting the brief's T5(a) draft
- Status at last mention: FALSE-as-drafted; corrected statements proved-here; reviewer VALID (exact on `Z/4`, `Cay(S_3,·)` in degrees 1 and 2, `Cay(Q_8,·)`)
- Content: The covariant weights `pi(s^{-1})` on the full Cayley complex satisfy `E_{(g,gs)} = F_{gs}F_g^{-1}` with `F_g = pi(g^{-1})`, so they are pure gauge: `det(I - uT_k^E) = det(I - uT_k)^{dim V}`. Every closed full-complex walk has identity holonomy. The interesting Artin factor lives on the **voltage quotient** (13 states, 9 successors each, in the PGL_3(F_3) case), with `det(I - s_k T_k(u)) = prod_rho det(I - s_k T_{k,rho}(u))^{d_rho}` — exponent `d_rho` for the regular decomposition, `a_rho` for `R = pi ⊗ conj pi`.
- Lead: whenever the notebook wants a genuine twisted zeta it must use quotient voltages, not a connection on the cover. The `C_4` counterexample (`(1-u^4)^2` versus `(1-u)^2`) is the minimal witness.
- Related: L08-029, L08-028, L08-041.

### L08-028 T5.7, Euler-factor bookkeeping per block: `F_rho = c^{m_{0,rho}} prod_{i>=1} w_{i,rho}^{(-1)^i}`, and the stabiliser caveat
- Source: `notes/complex-zeta/astra-proofs.md`:749-786 (T5.7); `notes/a2-complex-zeta/numerics.md`:200-226; `notes/complex-zeta.md`:197-204; review :360-371
- Raised by: codex prover; confirmed numerically
- Status at last mention: conditional-on H-KY, H-KY-LOCAL; the block bookkeeping proved-here; partially verified numerically
- Content: The simple power `c^{d_rho chi/|G|}` requires freeness on **unpointed** simplices; "a fractional power `c^{chi (dim pi)^2/|G|}` is not a rational determinant and must not be asserted." Measured on PGL_3(F_3): the 12-dimensional irrep gives exactly `(1-u^3)^{64} = (1-u^3)^{chi·dim/|G|}` with no `(1-u)` factor, while the trivial block gives `(1-u)^{13}(1-u^3)^1` where the naive `16/3` would sit. 24336 of the 97344 triangles carry `Z/3` stabilisers.
- Lead: the global check `prod_rho F_rho^{d_rho} = c^{chi}` forces the remaining irreps to contribute `(1-u)^{-13}` in total, and "only the two blocks above were built, so that sum is not checked here". Building a third block (or the whole character table of PGL_3(F_3)) would settle it.
- Related: L08-027, L08-042, L08-074.

### L08-029 Flat local systems get the full cochain identity; arbitrary Kraus weights do not
- Source: `notes/complex-zeta/astra-proofs.md`:787-812 (T5.8), :801-806 (`<1>4`); review :372-381
- Raised by: codex prover, answering the brief's expectation "the torsion form needs flatness"
- Status at last mention: conditional-on H-KY, H-KY-LOCAL; reviewer VALID
- Content: For an invertible flat local system of rank `r`, `Z_pt,E(u) = (1-u^n)^{r chi}/det P_{n,E}(u)`. "There is no corresponding assertion for arbitrary nonflat Kraus weights." And adjoint pairing supplies neither flatness nor the cancellation: a unitary, inverse-paired channel connection on a filled triangle (`B_01 = [[0,1],[1,0]]`, `B_12 = diag(1,-1)`, `B_02 = I`) has nonzero curvature.
- Lead: **open** — what the Euler/torsion factor becomes for non-flat channel weights. This is the direct quantum analogue of the question the notebook cares about, and the answer is simply not known.
- Related: L08-024, L08-027, L08-047.

### L08-030 The exceptional space `E_R` versus the fixed-point space `F_R` on partite complexes
- Source: `notes/complex-zeta/astra-proofs.md`:825-833 (T6.1), :871-873 (T6.2 `<1>6`); review :384-391, :400-402
- Raised by: codex prover, refuting the brief's "removing channel fixed points removes all trivial modes"
- Status at last mention: FALSE-as-drafted; corrected definition proved-here; reviewer VALID but notes the example is conditional
- Content: If `X` has a nonconstant type character `chi` with `chi(s) = omega^k` on `S_k`, then for `pi = 1 ⊕ chi` the off-diagonal matrix units carry channel eigenvalues `omega^{±k}`, so they are *not* common fixed points, yet their unnormalised first eigenvalue has modulus `q^2+q+1 > 3q` — outside the tempered bound. So the fixed-point-complement definition fails on a partite Ramanujan complex; one must remove the *exceptional space*.
- Lead: the reviewer records that astra never exhibits such an `X` ("such `X` do exist, e.g. `PGL_3(F_q)` with `3 | q-1`, but astra does not exhibit one"). Building one — the smallest 3-colourable Ramanujan complex — is a concrete, small, unfinished task, and it is the only setting where the correction bites.
- Related: L08-040, L08-031.

### L08-031 Harrow transfer: a Ramanujan complex gives Ramanujan quantum expanders of type `Ã_{n-1}` for free
- Source: `notes/complex-zeta/astra-proofs.md`:834-877 (T6.2); `notes/a2-complex-zeta/numerics.md`:162-179; `notes/complex-zeta.md`:129-133, :221-225
- Raised by: orchestrator in the brief (T6), proved by the prover, verified numerically
- Status at last mention: conditional-on H-LSV, parts 1–3; verified numerically on the 12-dimensional irrep of PGL_3(F_3)
- Content: The colour channels `Phi_k(X) = |S_k|^{-1} sum_{s in S_k} pi(s) X pi(s)^†` are commuting, normal, unital, trace-preserving, with common fixed space `pi(G)'`; their joint spectrum is a sub-multiset of the vertex joint spectrum. Numerically: largest nontrivial `|13 mu| = 6.4817 < 3q = 9` and below Hastings' `2 sqrt(D-1) = 6.9282` at `D = 13`; all 143 nontrivial joint eigenvalues inside the tempered deltoid.
- Lead: "**it cannot fail**, because `Phi_1 = A_1^{(pi ⊗ conj pi)}/13`" — i.e. the channel adds no spectral values. That is the limitation, not the achievement: see L08-041.
- Related: L08-041, L08-050, L08-032.

### L08-032 The exact converse criterion: `B_X ∩ supp(R) = ∅`, and why one faithful `pi` is not enough
- Source: `notes/complex-zeta/astra-proofs.md`:878-901 (T6.3); review :407-414
- Raised by: orchestrator in the brief ("I expect yes iff every nontrivial irreducible occurs in `pi ⊗ conj pi`"), corrected by the prover
- Status at last mention: proved-here as a finite-group spectral criterion; the faithful-only converse FALSE-as-drafted; reviewer VALID
- Content: Let `B_X` be the irreducibles with a nonexceptional joint eigenvalue outside `Aspec_n`. Then `R` satisfies the quantum condition iff `B_X ∩ supp(R) = ∅`, and `X` is vertex-Ramanujan iff `B_X = ∅`. Counterexample to the faithful-only version: `Cay(Z/28, {±1,±3})` is 4-regular bipartite, not Ramanujan (`2cos(pi/14)+2cos(3pi/14) = 3.5135 > 2 sqrt 3`), yet a faithful character `pi` has `pi ⊗ conj pi = 1` so the quantum condition is vacuous. "For an irreducible `pi`, central elements act by scalars, so its adjoint representation can in particular miss all irreducibles with nontrivial central character."
- Lead: coverage is the right hypothesis. The consequence for the notebook: a quantum-expander certificate is only as strong as the support of `pi ⊗ conj pi`.
- Related: L08-031, L08-030.

### L08-033 The one-sided RH in the correct variable, and the inversion of Kamber's bound
- Source: `notes/complex-zeta/astra-proofs.md`:902-924 (H-KAMBER, T6.4); review :415-426, :625-649 (Round 2)
- Raised by: codex prover, correcting two readings in the brief
- Status at last mention: conditional-on H-LLP, H-KAMBER; MINOR in Round 1, VALID after a one-word fix in Round 2
- Content: With `u = b^{-s}`, `|lambda| = b^{Re s}`, so peripheral means `Re s = 1` and the bound means `Re s <= 1/2`; the source's printed `|s| = 1` is not a well-defined invariant because `Im s` is only defined mod `2pi/log b`. And Kamber's bound **inverts**: actual nontrivial `u`-poles satisfy `|u| >= q^{-(p-1)/p}` — a lower bound on pole radii, not an upper one. "These are lower bounds on pole radii, or upper bounds on eigenvalue radii, not forced equalities."
- Lead: any downstream reading of Kamber's Corollary (which calls an eigenvalue a "pole") as a bound on `|u|` would be wrong. Use the eigenvalue theorem.
- Related: L08-005, L08-081.

### L08-034 The duality question: which rank-three factors have a functional equation, and why the type-(e) block cannot
- Source: `notes/complex-zeta/astra-proofs.md`:925-946 (T6.5); `notes/complex-zeta.md`:155 (correction ledger row); review :427-434
- Raised by: orchestrator in the brief (T6: "identify which factors have a genuine duality `u -> c/u`, i.e. a Hilbert–Pólya reading"), answered by the prover
- Status at last mention: proved-here for the algebra and the obstruction; reviewer VALID
- Content: `p_a(u) = 1 - au + q conj(a) u^2 - q^3 u^3` satisfies `p_a(u) = -q^3u^3 conj(p_a(1/(q^2 conj u)))`, so its zero multiset is invariant under `u -> q^{-2}/conj u` with fixed circle `|u| = q^{-1}` — "the precise single-circle, Hilbert–Pólya-style spectral reading". Principal-series edge and chamber factors inherit dualities at `q^{-2}` and `q^{-1}`. But the type-(e) chamber block has one root at radius `q^{-1/2}` and two at `q^{-1/4}`: fixing both radii needs `c = q^{-1}` and `c = q^{-1/2}` at once; exchanging them needs multiplicities `1 = 2`. No single duality exists.
- Lead: "Separate restricted circles can be given separate normalizations, but this is not a functional equation for the entire factor." A *multi-scale* functional equation (one normalisation per circle) has never been written down and is the only route left to a two-sided statement here.
- Related: L08-005, L08-020, L08-035.

### L08-035 Weil positivity is a bound until a duality is supplied; and it is blind to Jordan blocks
- Source: `notes/complex-zeta/astra-proofs.md`:947-962 (T6.6), :960-962 (`<1>3`); `notes/complex-zeta.md`:225-228; review :435-442
- Raised by: orchestrator (via `notes/weil-positivity.md`), reproved finitely by the prover
- Status at last mention: proved-here; reviewer VALID (including a numerical Toeplitz test)
- Content: For a retained finite transfer block, `nu_m = sum_j (mu_j/r)^m` is positive definite on `Z` exactly when all `|mu_j| <= r`; with the extra involution `mu -> r^2/conj mu` the bound forces every retained eigenvalue onto `|mu| = r`. It applies to each retained *ordinary* block, "not automatically to an alternating sum with negative spectral multiplicities". And: "positivity alone does not construct a Hilbert–Pólya inner product for a nonsemisimple transfer matrix."
- Lead: two open pieces. (i) The graded/alternating case — Weil positivity for a supertrace with negative multiplicities is not covered. (ii) A canonical self-adjoint realisation was not constructed: "repeated roots can make a companion matrix nonsemisimple, and logarithms require branch choices."
- Related: L08-005, L08-034, L08-078.

### L08-036 The type-cover descent: the identity holds without type preservation
- Source: `notes/complex-zeta/astra-proofs.md`:963-984 (H-COVER, T6.7); `notes/a2-complex-zeta/numerics.md`:36-54, :136-139; review :443-452
- Raised by: codex prover, prompted by the numerics lane's discovery that Kang–Li's hypothesis (I) fails on PGL_3(F_3)
- Status at last mention: conditional-on H-COVER, H-KY, H-KY-LOCAL; reviewer VALID; numerically confirmed to `u^18` on base and cover
- Content: For `Gamma` torsion-free cocompact with descended cyclic type-difference data but **not** type-preserving, the pointed determinant identity descends from the type-preserving cover `Gamma_0 = Gamma ∩ ker tau`, using `chi(X_0) = |H| chi(X)` and the fact that characters of `H ⊂ Z/n` extend to unitary characters of `PGL_n(F)` through `tau` and preserve temperedness.
- Lead: this is a genuinely new little theorem produced by a numerical surprise. It widens the class of quotients on which the Kang–Li machinery applies; nobody has asked how far it widens it (e.g. to quotients with torsion, or with simplex identifications).
- Related: L08-040, L08-043.

### L08-037 T7.1, the recommended object: the graded geodesic determinant of a complex with *specified geodesic data*
- Source: `notes/complex-zeta/astra-proofs.md`:985-1011 (T7.1); `notes/complex-zeta.md`:208-213; review :455-462
- Raised by: codex prover, as the verdict of the whole brief
- Status at last mention: proved-here as a finite graded construction; uniqueness explicitly **not** proved
- Content: Specify per degree `k` a state set `S_k`, a successor relation with multiplicities, a positive integer algebraic length `l_k(sigma)`, a step transport `U_{sigma tau}` on a fibre `V`, and give the degree-`k` space parity `k+1`. Then `Z = sdet_W(I - ⊕_k (-1)^{k+1} T_k^U(u))^{-1}`. "The word 'natural' here means functorial under isomorphisms preserving these specified data. This note does not prove uniqueness among all possible choices of higher-dimensional geodesics."
- Lead: prove (or disprove) uniqueness. If some naturality axiom pinned the geodesic data down, "the zeta that wants to exist" would become a theorem rather than a recommendation.
- Related: L08-001, L08-015, L08-018.

### L08-038 The three (four) smallest exact test complexes, and the octahedron escape hatch
- Source: `notes/complex-zeta/astra-proofs.md`:1012-1035 (T7.2), :1032-1035 (`<1>3`); review :463-479
- Raised by: codex prover, answering the brief's T7 demand for numerical targets
- Status at last mention: proved-here; every entry recomputed independently by the reviewer
- Content: `C_3` graph `(1-u^3)^2`; filled triangle `Z_ord = 1` (both flows vanish, but the Schur factors `det K_1 = (1+2u)(1-u)^2` and `det K_2(-u) = (1-u^3)^2` are nontrivial and test cancellation at singular points); `∂Δ^3` `(1-u^4)^6`. Optional fourth, for pipelines that only accept clique complexes: the octahedron `= K_{2,2,2}` clique complex, `f = (6,12,8)`, giving `(1-u^6)^8/(1-u^4)^6` with reduced degrees 36 and 12.
- Lead: these are the standing regression tests for any future graded-zeta code. Note the trap flagged in `<1>2`: the clique complex of `K_4` is the *filled* `Δ^3` with all flows zero, a different object from `∂Δ^3`. "This distinction is essential for interpreting a 'surface-like' effect of the odd sector."
- Related: L08-013, L08-016, L08-076.

### L08-039 The brief's predicted counts for PGL_3(F_3), and what the degree audit buys
- Source: `notes/complex-zeta/astra-proofs.md`:1036-1058 (T7.3); `notes/a2-complex-zeta/numerics.md`:23-33; review :480-505
- Raised by: codex prover; verified by the numerics lane and independently by the reviewer
- Status at last mention: proved-here conditional on the construction; every number confirmed
- Content: `|G| = 5616`, `f_1 = 73008`, `f_2 = 97344`, `chi = 29952`; pointed edge space 146016, pointed chamber space 292032, all-ordered chamber space 584064; all-ordered edge outdegree **21**, Kang–Li's **9**; cleared identity of degree 308880 on each side.
- Lead: the degree audit `3chi + 3f_1 = 3f_0 + 3f_2` is the cheapest sanity filter on any proposed placement of the factors, and it is what killed the orchestrator's original placement (L08-073).
- Related: L08-073, L08-042.

### L08-040 The smallest Ã_2 Ramanujan complex is not 3-colourable, and this was not anticipated
- Source: `notes/a2-complex-zeta/numerics.md`:34-44, :136-139; `notes/complex-zeta.md`:165-167
- Raised by: the numerics agent (independent worker)
- Status at last mention: verified; explained afterwards by T6.7
- Content: LSV's `r = ord(y/(1+y))` is 1 here, and `PGL_3(F_3)` is simple so there is no epimorphism onto `Z/3`; hence Kang–Li's hypothesis (I) **fails** on this quotient, and "for `q = 3` no `e` repairs this (`3 | q^e - 1` is impossible)". Yet the identity holds anyway on the base. Types of *directed* edges are still globally defined via `S_1` vs `S_2`, which is all the combinatorics of `L_E`, `L_B` needs.
- Lead: "Type preservation is apparently not needed for the identity itself; the colour only controls where the traces vanish." Two unexplored consequences: (i) what else in the Kang–Li package survives without hypothesis (I); (ii) the smallest *3-colourable* Ramanujan complex is still unbuilt and is exactly what L08-030 needs.
- Related: L08-036, L08-030, L08-043.

### L08-041 The channel adds no spectral values — a limitation, not a feature
- Source: `notes/a2-complex-zeta/numerics.md`:176-179; `notes/complex-zeta.md`:191-196, :222-225
- Raised by: the numerics agent; restated as a verdict by the orchestrator
- Status at last mention: verified; recorded as a negative for the Phantasm
- Content: "*Reason it cannot fail:* `Phi_1 = (1/13) Σ_s pi(s) ⊗ conj(pi(s))` is literally `A_1^{(pi ⊗ π̄)}/13`, so `13·spec(Phi_1)` is a sub-multiset of `spec(A_1)` on `C[G]`. Ramanujan complex ⇒ Ramanujan quantum expander, automatically. The channel adds no new spectral values."
- Lead: if the quantum twist is ever to *do* something, the weights must not be of the form `pi ⊗ conj pi` on a Cayley complex — i.e. they must be non-flat, non-representation weights, which is exactly the case where T5.8 says nothing (L08-029).
- Related: L08-029, L08-031, L08-047.

### L08-042 What the numerics lane did not do
- Source: `notes/a2-complex-zeta/numerics.md`:227-237 (§7)
- Raised by: the numerics agent
- Status at last mention: explicitly not done
- Content: three items. (i) The `pi ⊗ conj(pi)` 144-dimensional block was never built as a separate block; the `L_B` block for it would be `7488 x 7488` and "was judged not worth the time". (ii) Full-space spectra of `L_E` (beyond the top 40) and of `L_B` "would need the whole character table of `PGL_3(F_3)`". (iii) The identity is a power series check to `u^18` on the full complexes (degrees 308880), not a polynomial identity; only the trivial block is exact.
- Lead: (ii) is the blocker for L08-028's global Euler-factor check; the character table of `PGL_3(F_3)` is classical and available, so this is a bounded task.
- Related: L08-028, L08-074.

### L08-043 The type-preserving 3-fold cover (16848 vertices) and the colour-vanishing of traces
- Source: `notes/a2-complex-zeta/numerics.md`:51-54, :136-139; `notes/complex-zeta.md`:167
- Raised by: the numerics agent
- Status at last mention: built and verified
- Content: `Gamma~ = Gamma(I) ∩ Gamma_1` with `Gamma/Gamma~ = PGL_3(F_3) x Z/3` by Goursat; `V = 16848`, `chi = 89856`. Its closed-walk counts are `3x` the base counts restricted to total colour shift `0`; on the cover `Tr(L_E^m) = Tr(L_B^m) = 0` unless `3 | m`.
- Lead: the colour grading gives a `Z/3` grading of the trace sequence. Nobody asked whether that grading is the "letters" grading of the notebook's other lanes.
- Related: L08-036, L08-040.

### L08-044 Cohn's criterion as the stable temperedness test
- Source: `notes/a2-complex-zeta/numerics.md`:63-68
- Raised by: the numerics agent
- Status at last mention: used, verified (max defect `2.0e-14`)
- Content: The cubic `z^3 - (l/q)z^2 + (conj l/q)z - 1` is self-inversive, so all its roots are unimodular iff both roots of `3z^2 - 2sz + conj s` lie in the closed disc. "This is stable, unlike `np.roots` on the near-degenerate cubic, which gave spurious 1e-7 defects."
- Lead: a reusable numerical technique for any future temperedness check in the notebook. Small, but it is the difference between a clean `2e-14` and a fake `1e-7` failure.
- Related: L08-042.

### L08-045 Theorem 1: the Ihara–Bass formula for an *arbitrary* family of superoperators
- Source: `notes/quantum-ihara-general.md`:25-35 (statement), :55-96 (proof); `notes/complex-zeta/astra-brief.md`:8
- Raised by: orchestrator (Claude Fable 5.1)
- Status at last mention: `proved` (two Opus reviews VALID) + `numerical`
- Content: For arbitrary `E_1..E_D in End(V)` with a fixed-point-free reversal `sigma`, `det_W(1-uT) = prod_{pairs} det_V(1 - u^2 E_{ī}E_i) · det_V(1 + D(u) - A(u))` with `A(u) = u sum_i E_i (1-u^2 E_{ī}E_i)^{-1}` and `D(u) = u^2 sum_i E_{ī}E_i (1-u^2 E_{ī}E_i)^{-1}`. No invertibility, positivity or unitarity.
- Lead: this is the bouquet analogue of Watanabe–Fukumizu's arbitrary-weight corollary, which is stated only for loopless graphs. It is the general machine the notebook uses whenever a channel becomes a transfer matrix.
- Related: L08-046, L08-047, L08-056.

### L08-046 Corollaries 3 and 4: which factor carries the spectrum, and the `D = 2` degeneration
- Source: `notes/quantum-ihara-general.md`:47-53
- Raised by: orchestrator
- Status at last mention: `proved`
- Content: Under inverse pairing, `det_W(1-uT) = (1-u^2)^{N(D-2)/2} det_V(1 - u Sigma + (D-1)u^2)`. Corollary 4: the poles of `zeta` are among the roots of the second factor together with `u^2 = 1/lambda`, `lambda in spec(E_{ī}E_i)\{0}`; these may cancel (in Corollary 3, exponent `ND/2` against `-N`, total cancellation at `D = 2`). At `D = 2`, `T = E_1 ⊕ E_2` because the only non-backtracking successor of `i` is `i` itself.
- Lead: the cancellation bookkeeping between the pair factor and the compressed factor is exactly the same phenomenon as the chamber-factor cancellation of L08-018, in the simplest possible setting. Nobody connected the two.
- Related: L08-018, L08-045.

### L08-047 **Open**: what replaces the Ramanujan relation `mu mu' = D-1` when the weights are not inverse-paired, and whether MPS canonical form buys anything
- Source: `notes/quantum-ihara-general.md`:117 (§6, verbatim "is open")
- Raised by: orchestrator
- Status at last mention: raised, explicitly open
- Content: "It does not give a Ramanujan-type reading by itself: without `E_{ī}E_i = 1` there is no quadratic relation `mu mu' = D-1` pairing the eigenvalues of `T` with those of `Sigma`. What replaces it, and whether canonical form (`sum_k A_k^† A_k = 1`) buys anything, is open."
- Lead: this is the single most direct open question in the lane for the notebook's side-B programme: a Ramanujan reading for general (non-unitary) MPS transfer matrices. Canonical form is the obvious first hypothesis to test and it has not been tested.
- Related: L08-029, L08-041, L08-051.

### L08-048 Side A is unconditionally positive; the primes are cyclically non-backtracking words with multiplicities `|Tr A_w|^2`
- Source: `notes/quantum-ihara-general.md`:41-45 (Cor. 2), :118 (§6)
- Raised by: orchestrator
- Status at last mention: `proved`
- Content: `Tr_W T^l = sum_{cyclically non-backtracking words} |Tr(A_{i_l}···A_{i_1})|^2 >= 0`, so `zeta` has nonnegative Taylor coefficients, with Euler product `prod_{[w]} det_V(1 - u^{|w|} Ad(A_w))^{-1}` over primitive classes.
- Lead: "The primes are the primitive cyclically non-backtracking words in the `A_k` and `A_k^†`, with real nonnegative multiplicities `|Tr A_w|^2`." This is the lane's concrete side-A prime gas; combined with L08-025 it says a numerator needs grading.
- Related: L08-025, L08-051.

### L08-049 Claim 2 of the founding session — RH for `zeta_Phi` ⟺ Hastings-Ramanujan — has no prior art
- Source: `notes/prior-art-quantum-ihara.md`:10, :22, :26
- Raised by: orchestrator, from three literature agents
- Status at last mention: "not found" — recorded as the notebook's own contribution
- Content: Zero hits for any zeta/Ihara combined with channel, Kraus, CP-map or expander. Matsuura–Ohta contain none of the words Ramanujan, expander, Riemann hypothesis; Bordenave–Collins have the operator but no determinant and no zeta.
- Lead: "present the RH-for-channels reading, the MPS dictionary, and the Weil–LPS instance as this notebook's contribution."
- Related: L08-050, L08-051, L08-011.

### L08-050 Claim 4 — an exactly Ramanujan channel from the Weil representation of `SL_2(F_p)` with LPS generators
- Source: `notes/prior-art-quantum-ihara.md`:12, :23, :83-96
- Raised by: TJO/orchestrator in the founding session
- Status at last mention: "mechanism known, instance not"
- Content: Harrow 2008 gives `lambda_2(E) <= lambda_2(W_Gamma)`, which with LPS generators in `PSL_2(F_p)` gives exactly Ramanujan channels for any irrep — but the word Ramanujan does not occur in Harrow's paper. Iyer–Jain–Jordan–Somma (Feb 2026) state it with `SU(2)` irreps and call explicit Ramanujan quantum expanders "a longstanding open problem". No Weil-representation instance and no zeta anywhere.
- Lead: the Weil-representation instance is the notebook's own (`scripts/weil_lps.py`). Noted coincidence worth following: "their Appendix C example `p = 5`, `D = 6` uses the same norm-5 quaternions as `scripts/weil_lps.py`."
- Related: L08-049, L08-031.

### L08-051 The MPS / ring-norm reading, and AKLT `= K_4`
- Source: `notes/prior-art-quantum-ihara.md`:14, :24
- Raised by: TJO/orchestrator in the founding session
- Status at last mention: "not found" in the literature; not developed further in these files
- Content: channel = transfer matrix, `zeta` = generating function of ring norms, RH = one correlation length, AKLT gives `K_4`. No hits for Ihara/zeta combined with matrix product state, transfer matrix, or AKLT.
- Lead: the dictionary is unexploited here. "RH = one correlation length" is the most physical statement of the Phantasm in the whole lane and nothing in these files tests it.
- Related: L08-047, L08-048.

### L08-052 Bordenave–Collins: operator-valued non-backtracking operators, and their stated drawbacks
- Source: `notes/prior-art-quantum-ihara.md`:66-75
- Raised by: a literature agent, byte-checked by the orchestrator
- Status at last mention: RELATED; not pursued
- Content: They have the matrix-coefficient non-backtracking operator and a resolvent spectral correspondence, explicitly aimed at quantum expanders, but no determinant and no zeta. Their follow-up 2304.05714 §9 is the only place the words appear: "This formula is closely related to various spectral identities known as Ihara-Bass identities; ... it is an identity in its strongest form, i.e., between two operators." And the recorded drawbacks: "they are not self-adjoint, the spectral correspondence is established only for `A_1 = M_n(C)`".
- Lead: an operator-valued Ihara–Bass "in its strongest form" is exactly what the notebook's Theorem 1 is a special case of. Comparing the two (and seeing whether the strongest-form identity gives anything Theorem 1 does not) was never done.
- Related: L08-045.

### L08-053 The unfetched, unverified origins: Sunada 1986, Hashimoto 1989/90, Bass 1992, Stark–Terras, Terras's book
- Source: `notes/prior-art-quantum-ihara.md`:124-131
- Raised by: orchestrator
- Status at last mention: `[UNVERIFIED]`, no arXiv source
- Content: Sunada's L-functions paper is cited by Matsuura–Ohta and Komatsu–Konno–Sato as the origin of the representation-twisted zeta; Hashimoto, Bass, Stark–Terras I–III and Terras's Theorem 18.15 are all cited only secondarily.
- Lead: a byte-verified provenance for the twisted zeta is still missing, contra the notebook's own "prefer TeX sources" rule. Also unverified: Ben-Aroya–Schwartz–Ta-Shma's remark that "we believe our first construction has the potential of being improved to a construction of a quantum Ramanujan expander".
- Related: L08-054.

### L08-054 The notebook's object is not literally a Stark–Terras `L`-function, because `Ad(U_i)` generates an infinite group
- Source: `notes/prior-art-quantum-ihara.md`:113-122
- Raised by: orchestrator
- Status at last mention: recorded as a scope note
- Content: In Stark–Terras the representation is of the Galois group of a covering of finite graphs, hence of a *finite* group; `Ad(U_i)` for generic unitaries generates an infinite group, "though the formula is the same".
- Lead: the infinite-group case is where the notebook's object genuinely departs from the classical theory. Nobody asked what the Artin-`L` bookkeeping (T5.6's `d_rho` versus `a_rho`) becomes for an infinite image.
- Related: L08-027, L08-045.

### L08-055 Grover/Zeta correspondence and open quantum random walks — not read in full
- Source: `notes/prior-art-quantum-ihara.md`:105-111
- Raised by: a literature agent
- Status at last mention: "NOT for claims 1–4"; partially unread
- Content: Komatsu–Konno–Sato build zeta functions from the unitary evolution matrix of a quantum walk (Grover walk), not from Kraus operators; arXiv:2104.10287 extends to **open quantum random walks on the torus by Fourier analysis** and "not read in full".
- Lead: open quantum random walks are the closest published thing to a channel zeta. The unread extension is the single cheapest place in the prior-art file where the "not found" verdict could turn out to be wrong.
- Related: L08-011, L08-049.

### L08-056 The Watanabe–Fukumizu shape-matching is only `numerical`, and the hypergraph-free proof was never fetched
- Source: `notes/quantum-ihara-general.md`:110 (last sentence); `notes/prior-art-quantum-ihara.md`:64
- Raised by: orchestrator
- Status at last mention: status `numerical` (reviewer's script `scratch_wf_mo_conventions.py`); NeurIPS 2009 supplement "not fetched"
- Content: Theorem 1's right-hand side matches Watanabe–Fukumizu's after a push-through identity and a relabelling, plus two conventions that wash out of `det(1 - u·)` (they compose prime cycles in the reverse order; their edge operator weights the target where `T` weights the source). But their graphs are hypergraphs with two-element hyperedges, so a bouquet is not one of them, and their scalar reduction "does not evaluate correctly there".
- Lead: fetch the NeurIPS 2009 supplement, which has a hypergraph-free proof — it might cover the bouquet directly and change the novelty claim.
- Related: L08-045, L08-011.

### L08-057 The searches that returned nothing, and their stated limit
- Source: `notes/prior-art-quantum-ihara.md`:135-137
- Raised by: orchestrator
- Status at last mention: recorded, with the limitation stated
- Content: Ten arXiv metadata queries returned zero hits (`"Ihara zeta" AND "quantum channel"`, `"zeta" AND "quantum expander"`, `"non-backtracking" AND "superoperator"`, `"AKLT" AND "zeta"`, …). "Limits: arXiv search is metadata-only; a formula inside a paper body would not surface."
- Lead: a full-text search (Google Scholar full text, or a local full-text grep over fetched sources) has never been run. Given that the whole novelty claim rests on these negatives, this is the obvious cheap insurance.
- Related: L08-011, L08-075.

### L08-058 The BC inverse problem: a Lindbladian with the BC state stationary, Galois symmetry, and adelic symplectic structure
- Source: `notes/bc-symmetry-generators.md`:3-9
- Raised by: TJO
- Status at last mention: first finite-level constraint calculation done; the construction itself open; all written arguments `sketched` and **unreviewed**
- Content: "The no-event generator and the jump map are both unknown. A fixed scattering generator with a chosen reset map is only one possible ansatz." The note "does not construct the adelic bond, identify it with the scattering model, or prove RH."
- Lead: the note's own answer to "what next" is L08-069.
- Related: L08-063, L08-069, L08-070.

### L08-059 The critical BC phase marginal is uniform at every level, and the marginals are compatible under reduction
- Source: `notes/bc-symmetry-generators.md`:40-64 (B0.1)
- Raised by: orchestrator (Claude), from Connes–Marcolli
- Status at last mention: `sketched`, unreviewed
- Content: `w_beta(0) = p^{-beta}`, `w_beta(x) = (1-p^{-beta})/(p-1)` for `x != 0`; at `beta = 1` the BC formula vanishes on every nontrivial finite-order phase at every level `N`, so the critical restriction is uniform on `Z/N` and the marginals are compatible under reduction. The diagonal extension to `M_p` is `I/p`.
- Lead: compatibility under reduction is the hook for an adelic (inverse-limit) construction; L08-068 shows compatibility alone does not determine the couplings.
- Related: L08-062, L08-068.

### L08-060 No finite-dimensional representation of the full BC algebra retains the nontrivial phases
- Source: `notes/bc-symmetry-generators.md`:66-80 (B0.2)
- Raised by: orchestrator
- Status at last mention: `sketched`; a clean negative with an explicit scope
- Content: In finite dimension `mu_n^* mu_n = I` makes `mu_n` unitary, and `I = mu_n mu_n^* = (1/n) sum_k e(k/n)` is the spectral projection onto eigenvalue 1 of `e(1/n)`, so `e(1/n) = I` for every `n`. The critical phase state has `phi(e(1/n)) = 0` for `n > 1` and cannot be realised. "This excludes an exact finite representation, not finite restrictions, CP compressions, or asymptotic approximations."
- Lead: the three escape hatches are named in the last sentence and none has been tried: finite restrictions, CP compressions, asymptotic approximations.
- Related: L08-063.

### L08-061 Parity as a local grading, and whether it is the Phantasm's grading
- Source: `notes/bc-symmetry-generators.md`:106-110
- Raised by: orchestrator
- Status at last mention: raised, explicitly not pursued
- Content: Parity `P|x> = |-x>` implements the central symplectic element `-I` and also `U_{-1}`, so the local models already preserve even and odd operator sectors of dimensions `(p^2+1)/2` and `(p^2-1)/2`. "Identifying this local grading with the Phantasm's grading is still additional work."
- Lead: this is the only place in the whole lane where a concrete, arithmetically natural `Z_2` grading appears on the BC side. If it *is* the Phantasm's grading, the odd sector of L08-017 and the odd sector of B4.1 are the same object; if not, it should be ruled out. Nobody has tried either.
- Related: L08-017, L08-067.

### L08-062 The unique Weil-invariant matrix extension `sigma_beta = aI + (r-a)P`, and why the naive no-go is false
- Source: `notes/bc-symmetry-generators.md`:112-139 (B1.1)
- Raised by: orchestrator
- Status at last mention: `sketched`
- Content: The same residue probabilities have a unique Weil-invariant matrix extension `sigma_beta = aI + (r-a)P` with `r = p^{-beta}`, `a = (1-r)/(p-1)`, positive iff `beta >= log((p+1)/2)/log p`; parity-block eigenvalues `r` and `2a-r`; at criticality it is `I/p`; full Weyl invariance forces `I/p`. "These statements prevent a false no-go: failure of the **diagonal** extension to be symplectic invariant does not exclude every extension."
- Lead: "None of the coherent extensions has been identified with the full BC bond state." Doing that identification is open. Also recorded: for `beta > 1` a symmetry-broken extremal state can belong to a stationary family, so uniqueness is the premise of the obstruction.
- Related: L08-059, L08-061.

### L08-063 B2.1, the stationary covariant GKLS cone — the concrete deliverable
- Source: `notes/bc-symmetry-generators.md`:143-178 (B2.1), :313 ("The concrete deliverable is the cone B2.1 with the orbit reduction B3.1")
- Raised by: orchestrator
- Status at last mention: `sketched`, unreviewed; presented as the note's deliverable
- Content: `C_U(sigma) = {L : L(X^*) = L(X)^*, Tr L(X) = 0, L(sigma) = 0, [L, Ad U_g] = 0, Q C_L Q >= 0}` with `C_L` the Choi matrix and `Q = I - |Omega><Omega|`. Linear equations plus one PSD constraint, necessary and sufficient. Equivalently `L(X) = -i[H,X] + sum A_{ij}(F_i X F_j^* - {F_j^*F_i, X}/2)` with `A >= 0`, `H` in the commutant of `U`, `A` in the commutant of the induced representation on traceless operators.
- Lead: the cone is the right object to impose *further* arithmetic constraints on — see L08-069. The parametrisation is unique once `Tr H = 0`.
- Related: L08-065, L08-069, L08-070.

### L08-064 State plus symmetry alone cannot select the dynamics: the depolarizing interior point
- Source: `notes/bc-symmetry-generators.md`:180-184
- Raised by: orchestrator
- Status at last mention: `sketched`; a clean structural negative
- Content: Every invariant faithful `sigma` has an interior feasible point `L_sigma(X) = sigma Tr X - X`, with conditional Choi matrix `Q(I ⊗ sigma)Q`, strictly positive on `range Q`. "This elementary existence observation does not give scattering modes. It shows that state and symmetry alone cannot select the wanted dynamics."
- Lead: because the cone has interior, small perturbations in *every* permitted direction stay GKLS; so positivity never shrinks the dimensions of B3.1 and no amount of symmetry-plus-state will pin the generator down. Extra arithmetic input is mandatory.
- Related: L08-063, L08-065, L08-069.

### L08-065 B3.1, the dimension table: how much freedom survives at the critical residue state
- Source: `notes/bc-symmetry-generators.md`:188-207 (B3.1)
- Raised by: orchestrator
- Status at last mention: `sketched` + `numerical` (orbit counts by BFS and independently by Burnside)
- Content: At `sigma = I/p`, real dimensions of the spans of the finite GKLS cones: Galois torus `(p-1)(p+1)^2`; full Weil/`SL_2` `2p-2`; Weyl translations + Galois torus `p+1`; Weyl translations + full Weil **1**. "These are dimensions of cones' spans, not claims that every coefficient in an orbit basis can be chosen nonnegative independently."
- Lead: the collapse from `(p-1)(p+1)^2` to 1 as symmetries are added is the quantitative form of the obstruction; the useful regime is the Galois-torus-only row, which is large and unexplored.
- Related: L08-063, L08-066.

### L08-066 Full affine (Weyl + Weil) symmetry removes all oscillatory zero-like modes
- Source: `notes/bc-symmetry-generators.md`:215-238 (B3.2), :236-238
- Raised by: orchestrator
- Status at last mention: `sketched`; a conditional obstruction
- Content: All Weyl-covariant GKLS generators on `M_p` are `L(X) = sum_{v!=0} c_v(W_v X W_v^* - X)` with `c_v >= 0`; Galois covariance makes `c_v` constant on the `p+1` torus orbits and forces `c_v = c_{-v}`, so "their Weyl eigenvalues are real and nonpositive"; full symplectic covariance gives exactly the depolarizer `L(X) = gamma(Tr(X)I/p - X)`. "Full affine symmetry in this model removes all oscillatory zero-like modes. It is a conditional obstruction to imposing those extra *commuting* symmetries, not an obstruction to an adelic symplectic structure as such."
- Lead: the escape is to make the symplectic structure act *non-commutingly* with the dynamics (covariance rather than commutation), which is explicitly left open.
- Related: L08-065, L08-067.

### L08-067 B4.1, the `p = 7` counterexample: symmetry does not force equal odd decay rates
- Source: `notes/bc-symmetry-generators.md`:242-273 (B4.1), :269-273
- Raised by: orchestrator
- Status at last mention: `sketched` + `numerical` (exact spectrum checked)
- Content: `L = D - id + eps R_a` with `eps = 1/(4p^2)` and `R_a(W_v) = W_{av)`, `a` a primitive root, is CPTP with unique stationary state `I/p`, commutes with the entire Weil action and with parity, and at `p = 7` has odd-sector eigenvalues `-1-eps`, `-1+eps/2 ± i sqrt3 eps/2`, each of multiplicity 8. "Thus all the prescribed finite state, linear symplectic and Galois symmetries coexist with **unequal odd decay rates**. ... No zeta zeros were used."
- Lead: "The script also constructs class-averaged Weil-unitary jump generators and adds `H = hP`, an invariant Hamiltonian. These supply further freely variable frequencies. In the tested shear classes at `p = 3,5,7` the odd real parts happen to coincide; those class examples alone do **not** refute an equal-rate statement." So the shear-class coincidence at `p = 3,5,7` is unexplained and could be a real phenomenon worth isolating.
- Related: L08-061, L08-066.

### L08-068 Two prime levels: marginal compatibility does not select the coupling
- Source: `notes/bc-symmetry-generators.md`:277-300 (B5.1)
- Raised by: orchestrator
- Status at last mention: `sketched` + `numerical`
- Content: `L_c = (gamma_p - c)(D_p - id)⊗id + (gamma_q - c) id⊗(D_q - id) + c(D_p⊗D_q - id)` for `0 <= c <= min(gamma_p, gamma_q)` all have unique stationary state `I/(pq)`, full local Weyl and Weil covariance, and the **same** one-prime restrictions, while the joint traceless sector decays at `gamma_p + gamma_q - c`. Under CRT these are compatible prime-residue models. "The statement concerns two prime levels only; an infinite consistent, conservative adelic system has not been constructed."
- Lead: construct the infinite adelic system (or prove it cannot be conservative). The one-parameter family `c` is exactly the freedom an arithmetic constraint would have to fix.
- Related: L08-059, L08-069.

### L08-069 The next target: a CP comparison map from the finite phase/Weil data to a scattering bond
- Source: `notes/bc-symmetry-generators.md`:302-330 (B6), especially :322-330
- Raised by: orchestrator, as the note's stated next step
- Status at last mention: open
- Content: "The next target is therefore an explicit representation or CP comparison map linking the finite phase/Weil data to a scattering bond, respecting the actual character action and the arithmetic boundary state. Only with that map can one impose the scattering odd-sector condition on the cone rather than fit an operator to known zeros." Explicitly still open beside it: the `Gamma_0(N)` scattering/character calculation; prime powers; the real place; metaplectic compatibility; the critical operator-algebra limit; and "The standard BC time flow has not been identified with the unknown cMPS transfer flow."
- Lead: six named open sub-problems, any of which is a self-contained task. The phrase "rather than fit an operator to known zeros" is the methodological rule the lane wants to keep.
- Related: L08-058, L08-063, L08-070.

### L08-070 The reset-ansatz matrix test `-(B sigma + sigma B^*) >= 0` is not a no-go for the general problem
- Source: `notes/bc-symmetry-generators.md`:332-336 (last paragraph)
- Raised by: TJO (the test came "from the conversation"), scoped by the orchestrator
- Status at last mention: scoped; the test is not binding
- Content: "the matrix test `-(B sigma + sigma B^*) >= 0` from the conversation is necessary and sufficient only for a **fixed** finite no-event `B` with the scalar reset ansatz and positive exit flux. B2.1 allows `B`, Hamiltonian, and all jump terms to vary. Failure of that reset test is not a no-go for this larger inverse problem."
- Lead: anyone who reaches for that test in a future session should read this first; failing it proves nothing about the cone.
- Related: L08-063, L08-058.

### L08-071 Reviewer sharpening: the colour-preserving part of the unrestricted edge rule *is* `L_E` exactly
- Source: `notes/reviews/complex-zeta-2026-09-13.md`:50, :589-593
- Raised by: Opus reviewer
- Status at last mention: verified exactly for `q = 2, 3, 5`; recorded as a sharpening, not registered as a claim
- Content: Of the `2q^2+q` unrestricted successors of a colour-1 directed edge, exactly `q^2` preserve the directed-edge colour and exactly `N-1 = q^2+q` flip it. So the prover's "the colour classes are not invariant blocks" can be strengthened to: "the colour-preserving part is precisely `L_E`; the `q^2+q` colour-flipping transitions are the entire discrepancy."
- Lead: this says the unrestricted ordered flow is `L_E` plus a colour-flipping perturbation of known size. A *colour-graded* version of the ordered flow — block-triangular in the colour grading — has never been written down and might interpolate between the two flows.
- Related: L08-015, L08-043.

### L08-072 Reviewer observation: the chronological (non-flat) convention still gives the pure-gauge determinant numerically
- Source: `notes/reviews/complex-zeta-2026-09-13.md`:340
- Raised by: Opus reviewer, recorded explicitly "not a defect"
- Status at last mention: numerical observation, unexplained
- Content: On `Cay(Q_8, {±i,±j,±k})`, where **192 of 192** ordered 2-cells violate flatness for the 2-dimensional irrep, the determinant conclusion survives anyway: `det(I - uT_1^{E,chrono}) = det(I - uT_1)^2` to `1.1e-15` (96×96 versus 48×48 eigenvalue multisets). "a reader should not infer from `<1>3` that the chronological convention breaks the pure-gauge determinant; in my tests it does not."
- Lead: is there a theorem here? A determinant identity that holds for a totally non-flat representation connection would be a genuinely new fact; at present it is one numerical coincidence on one group.
- Related: L08-027, L08-029.

### L08-073 The orchestrator's original placement of the Kang–Li identity was wrong, and so was a chamber-radius prediction
- Source: `notes/a2-complex-zeta/numerics.md`:128-135, :141-145; `notes/complex-zeta/astra-proofs.md`:1052-1058 (T7.3 `<1>3`); review :480-505, :650-663
- Raised by: the numerics agent and the prover; adjudicated by the reviewer
- Status at last mention: corrected in both places
- Content: The brief's form `(1-u^3)^chi det(cubic) det(I+L_Bu) = det(I-L_Eu)det(I-L_E^t u^2)` fails at `u^3` (residual `-59904`) and fails the degree count (398736 vs 219024); the correct cleared form is `det P_3 · det(I + uL_B) = (1-u^3)^chi det(I - uL_E) det(I - u^2 L_E^t)`. Separately, `det(I - uL_B)` instead of `det(I + uL_B)` first fails at `u^15`. And the predicted chamber eigenvalue radius `q^{3/4}` was stale (traceable to the non-tempered type-(d) row); the correct radii are `{1, q^{1/4}, q^{1/2}}`, observed as `1.316074 = 3^{1/4}`.
- Lead: none — recorded so the wrong placements are not re-derived. See Dead routes.
- Related: L08-020, L08-039.

### L08-074 What the adversarial review explicitly did **not** check
- Source: `notes/reviews/complex-zeta-2026-09-13.md`:612
- Raised by: Opus reviewer
- Status at last mention: recorded as unverified
- Content: four items. The PGL_3(F_3) complex was not rebuilt from the LSV generators (only the vertex link was); H-KY's `thm:Phi-determinants` and H-KY-LOCAL's factorisation `Phi_i = c W_i^{-1} J_i (I - s_i Sigma_i) J_i^{-1} Q_i^{-1}` were confirmed to exist at the cited addresses but not verified line by line; T5.7's global identity `prod_rho F_rho^{d_rho} = c^chi` was confirmed only on two isotypic blocks; T6.7's descent was checked only through order `u^18`.
- Lead: these four are the remaining soft spots in an otherwise 47/47 VALID note. The first two are the load-bearing ones, since everything conditional-on-H-KY rests on an unverified technical proof.
- Related: L08-028, L08-042, L08-036.

### L08-075 "A literature search finding no general/quantum zeta proves nonexistence — it does not"
- Source: `notes/complex-zeta/astra-proofs.md`:1118 (last row of T8.2); review :560-561
- Raised by: codex prover
- Status at last mention: recorded as a methodological correction
- Content: "No such impossibility hypothesis is used. The exact finite obstructions proved here concern specific identities and conventions."
- Lead: an actual impossibility theorem for a general-complex zeta would be a real result. The lane has only obstructions to *specific prescribed shapes* (the cubic collapse, the Euler-factor-only fermion determinant).
- Related: L08-011, L08-016, L08-057.

### L08-076 The brief's requested non-building tests (4-simplex boundary, 7-vertex triangulated torus) were substituted, not run
- Source: `notes/complex-zeta/astra-brief.md`:29 (T7); `notes/complex-zeta/astra-proofs.md`:1012-1035 (T7.2 delivers `C_3`, `Δ^2`, `∂Δ^3`, octahedron instead)
- Raised by: orchestrator in the brief
- Status at last mention: not done as specified
- Content: The brief asked for "one NON-building 2-complex (e.g. the boundary of the 4-simplex, or a 7-vertex triangulated torus) and what the identity predicts there numerically". The prover supplied `∂Δ^3` and the octahedron instead, both non-building, both smaller.
- Lead: a triangulated torus is the one test with `b_1 != 0`, which is the only case where a Betti number could show up in a vanishing order (cf. L08-007's `b_1` theorem and L08-021's failed Betti formula). It has never been computed.
- Related: L08-007, L08-021, L08-038.

### L08-077 The strategic verdict: what this lane buys the Riemann programme, and what it does not
- Source: `notes/complex-zeta.md`:230-232
- Raised by: orchestrator
- Status at last mention: recorded as the lane's summary
- Content: "None of this touches the Riemann side directly. What it buys is a supply of exactly-solvable graded transfer operators with a Ramanujan property, and a sharp negative: there is no zeta of a general complex to build a Phantasm on."
- Lead: use the building family as a *testbed* for graded-transfer machinery rather than as a candidate Phantasm. Every identity that a real Phantasm must satisfy can be checked here first, exactly.
- Related: L08-001, L08-037, L08-078.

### L08-078 "What remains is Weil-positivity-as-bound, `thm:weil-positivity-finite` applied block by block"
- Source: `notes/complex-zeta.md`:225-228
- Raised by: orchestrator
- Status at last mention: stated as the residue of the lane
- Content: Since higher-rank RH is one-sided with an occupied interior and no universal duality, the only surviving statement is the registered finite Weil-positivity theorem applied to each retained block.
- Lead: apply it block by block on the PGL_3(F_3) data (the two isotypic blocks already built) and see what the positivity certificate actually looks like on a real graded example. That has not been done.
- Related: L08-005, L08-035, L08-034.

### L08-079 Kamber's `L_p`-expander criterion as a one-parameter family of Ramanujan notions
- Source: `notes/complex-zeta/astra-brief.md`:6 (item C7); `notes/complex-zeta.md`:57-59; `notes/complex-zeta/astra-proofs.md`:902-905 (H-KAMBER)
- Raised by: a paper (Kamber, arXiv:1701.00154), recorded by the orchestrator
- Status at last mention: registered as H-KAMBER, used only for the one-sided bound
- Content: `zeta = 1/prod_i det(1 - h_{beta_i} u^{l(beta_i)})` over Bernstein–Lusztig operators, and the complex is an `L_p`-expander **iff** every eigenvalue satisfies the one-sided bound `|theta| <= q^{l(beta_i)(p-1)/p}` (or `|lambda| = q`). At `p = 2` this is Ramanujan; larger `p` interpolates.
- Lead: this is a *continuum* of Ramanujan-type properties indexed by `p`, with an iff spectral criterion, and the notebook uses only the endpoint. A graded/`L_p` version of the Phantasm's uniform-decay property has never been formulated, and Kamber's criterion is the one place where the interpolation is already a theorem.
- Related: L08-005, L08-033.

### L08-080 T3.2: algebraic lengths need either a polynomial transfer operator or a delay space
- Source: `notes/complex-zeta/astra-proofs.md`:376-390 (T3.2); review :190-197
- Raised by: codex prover
- Status at last mention: proved-here; reviewer VALID
- Content: A transfer matrix that is *linear in `u`* can be recovered from one with algebraic lengths `l(sigma)` by giving each state a chain of `l(sigma)` delay states of the **same parity**, weight 1 along the chain and `s_k` on the exit arrow. Eliminating the delay coordinates restores `det(I - s_k T_k(u))`. Critically, "the sign `s_k` is inserted once per successor arrow, not at every delay tick" — a sign per tick would give `-u^2` instead of `+u^2` on colour-2 edges and break the identity.
- Lead: this is a general recipe for converting a zeta with unequal prime lengths into an ordinary linear transfer operator. The notebook's side-B objects have lengths `log p`; the delay-space trick is the finite model of exactly that, and nobody has asked whether it transfers.
- Related: L08-017, L08-037.

### L08-081 In type `C~_2` the RH-equals-Ramanujan statement degrades from circles to bands
- Source: `notes/complex-zeta.md`:43-44
- Raised by: a paper (Fang–Li–Wang, arXiv:1109.3854), recorded by the orchestrator
- Status at last mention: raised once, not pursued
- Content: The four-way RH ⟺ Ramanujan equivalence in rank three already puts zeros on several circles (one for the vertex cubic, three for the chamber factor, two for the edge factor); "In type `C~_2` (Fang–Li–Wang, 1109.3854) it degrades further to *bands*."
- Lead: nobody looked at the `C~_2` paper. If the degradation from circles to bands is generic outside type `Ã`, that is a strong structural hint that "zeros on a line" is a type-`A` accident — directly relevant to whether the Phantasm should expect a line at all.
- Related: L08-005, L08-020, L08-034.

---

## Small but possibly consequential

1. **L08-007** — Benard–Chaubet–Dang–Schick's combinatorial Ruelle zeta is a *polynomial* on an arbitrary triangulation vanishing to order `b_1`: the only object in the whole sweep with a genuine Betti-number numerator on a general complex, and nobody asked whether it has a Ramanujan reading.
2. **L08-047** — the explicitly-open question of what replaces `mu mu' = D-1` for non-inverse-paired weights, and whether MPS canonical form helps, is the lane's most direct unanswered side-B question.
3. **L08-061** — the `(p^2±1)/2` parity grading on the BC side is the only arithmetically natural `Z_2` grading in the lane, and identifying or excluding it as "the Phantasm's grading" was left as "additional work".
4. **L08-071** — the reviewer's observation that the colour-preserving part of the unrestricted flow is exactly `L_E` suggests a colour-graded flow interpolating between the ordered and building rules; raised once, never pursued.
5. **L08-072** — a totally non-flat representation connection nonetheless reproduced the pure-gauge determinant to `1.1e-15`; if that is a theorem rather than a coincidence it would widen the twisted-zeta class considerably.
6. **L08-055** — the unread arXiv:2104.10287 extension to *open* quantum random walks is the cheapest place the "no quantum channel zeta exists" verdict could break.
7. **L08-013** — `B_X(u) = (1-u^{d+1})^chi / Z_ord` is a fully computable test for vertex collapse; a census over small 2-complexes is a bounded script that was never run.
8. **L08-067 (second half)** — the odd real parts coincided in every tested shear class at `p = 3,5,7` and the note says explicitly that those examples "do not refute an equal-rate statement"; the coincidence is unexplained.

---

## Dead routes recorded

- **Universal cubic vertex Bass identity for every 2-complex.** False on `∂Δ^3`: the identity would force `det P = (1-u^3)^2/(1-u^4)^6`, which has poles at `u = -1` and `u = ±i`. `notes/complex-zeta/astra-proofs.md`:300-327; review :157-168; `notes/complex-zeta.md`:112-118.
- **The ordered flow as `k!` copies of the Kang–Yu / LLP flow.** Opposition is strictly stronger than non-incidence; already in rank three the outdegrees differ (21 versus 9). `astra-proofs.md`:119-130; review :71-78.
- **The total graded zeta equals Kang–Li's edge zeta.** It equals `D_B/D_E = (1-u^3)^chi/det P_3`, the completed vertex `L`-function; Kang–Li's is `1/D_E`. `astra-proofs.md`:105-118.
- **Kang–Yu's cochain product has exponent `chi`.** It has `chi_pt = sum (-1)^i (i+1) f_i`; `chi` appears only after subtracting the local `i f_i` terms. `astra-proofs.md`:157-182, :195-212.
- **Ordered-cochain torsion universally gives the ordinary `chi`.** The exponent is `sum (-1)^i (i+1)! f_i`, already wrong for a single edge (`chi = 1`, `chi_ord = 0`). `astra-proofs.md`:173-176.
- **Knill's super pseudodeterminant as the `u -> 1` limit of the zeta or the Euler factor.** One edge separates three different numbers: 1, 2 and 0. `astra-proofs.md`:213-226; review :107-114.
- **"Chamber roots are uncancelled zeros of the vertex `L`-function."** `L_vertex = 1/det P_3` is a reciprocal polynomial with no finite zeros; they all cancel. `astra-proofs.md`:391-400.
- **`k`-cells literally realise `H^{k-1}` with Weil weight `k-1`.** Only the parity exponents match; a 3-cycle and the three chamber radii both kill the literal reading. `astra-proofs.md`:401-447.
- **One pure fermion (ordinary Grassmann) determinant gives the total supertrace, with flow parity equal to cell chirality.** An ordinary Berezin integral gives `det D`, not a ratio; the total needs auxiliary copies and chirality ≠ flow superparity. `astra-proofs.md`:513-536.
- **"No polynomial multiplier could clear the rational total."** Too broad as first written: `p(u) = (1-u^4)^6` clears it on `∂Δ^3`. The surviving obstruction is Euler-factor-only. `astra-proofs.md`:1059-1070 (T8.1).
- **The building "Laplacian" as `(d+delta)^2`.** `delta^2 != 0` in Kang–Yu (byte-verified at `2607.21262:main.tex:2377-2378`), so a degree-(-2) term appears; the doubled linearisation is needed. `astra-proofs.md`:597-599.
- **Adjoint pairing is needed for Kraus ring positivity.** Complete positivity suffices; `Tr(T^E_k)^m = sum |Tr(B_m···B_1)|^2 >= 0` without any pairing. `astra-proofs.md`:641-668.
- **"Nonnegative coefficients forbid a numerator."** False: `(1-u)/(1-2u)`. The operative hypothesis is "is an honest trace sequence". `astra-proofs.md`:669-680; review :321-330.
- **Arbitrary Kraus weights preserve the building Euler/Hecke formula.** They preserve only the Schur identity; the cochain cancellation needs an invertible *flat* local system. `astra-proofs.md`:787-812.
- **`E_{(g,gs)} = rho(s)` is a flat connection.** It is not, in the chronological convention (a representation gives `rho(st) = rho(s)rho(t)`, flatness asks `rho(t)rho(s)`); on `Cay(Q_8,{±i,±j,±k})` 192 of 192 ordered 2-cells fail. `astra-proofs.md`:697-700; review :338.
- **The full-cover connection is a representation-isotypic block.** It is pure gauge; `C_4` with a one-dimensional `pi` gives `(1-u^4)^2` versus `(1-u)^2`. `astra-proofs.md`:701-708.
- **`R = pi ⊗ conj pi` embeds in a single regular representation.** Only spectral support transfers; `pi = 1 ⊕ 1` gives `R = 1^{⊕4}` against one trivial copy. `astra-proofs.md`:726-729.
- **A fractional Euler exponent `c^{chi (dim pi)^2/|G|}` on a quantum block.** Not a rational determinant when the deck group has simplex stabilisers; measured `(1-u)^{13}(1-u^3)^1` on the trivial block where `16/3` was predicted. `astra-proofs.md`:749-786; `notes/a2-complex-zeta/numerics.md`:200-226.
- **A scalar global determinant identity restricts automatically to every irreducible.** It does not; only matrix identities and equivariant closed-path arguments restrict. `astra-proofs.md`:442-447.
- **Removing the channel fixed points removes all spectrally trivial modes.** Type characters survive and violate the tempered bound (`q^2+q+1 > 3q` for `q > 1`); remove the exceptional space `E_R`. `astra-proofs.md`:825-833, :871-873.
- **One faithful `pi` detects Ramanujan.** False on `Cay(Z/28, {±1,±3})`: a faithful character has `pi ⊗ conj pi = 1` and a vacuous quantum condition on a non-Ramanujan graph. `astra-proofs.md`:878-901.
- **All-rank Kang–Yu supplies factor-by-factor RH.** That paper supplies a determinant identity and states no RH. `astra-proofs.md`:183-193, :834-877; review :403-404.
- **LLP's condition is an invariant `|s| = 1`.** `Im s` is defined only mod `2pi/log b`; the invariant peripheral statement is `Re s = 1`. `astra-proofs.md`:906-924.
- **Kamber's bound is an upper bound on pole radii.** It inverts: `|u| >= q^{-(p-1)/p}`. The source's own corollary calls an eigenvalue a "pole". `astra-proofs.md`:902-924.
- **Higher-rank RH automatically has a duality.** The tempered nonspherical (type-e) chamber block has radii `q^{-1/2}` (×1) and `q^{-1/4}` (×2); no `u -> c/u` or `u -> c/conj u` fixes or exchanges them. `astra-proofs.md`:925-946.
- **A non-type-preserving Cayley quotient automatically satisfies the quoted type-preserving theorem.** A separate cover/descent argument (T6.7) is required. `astra-proofs.md`:965-984.
- **The numerical chamber eigenvalue radius `q^{3/4}`.** Stale; the correct radii are `{1, q^{1/4}, q^{1/2}}`; `q^{3/4}` comes from the non-tempered type-(d) row, absent on a Ramanujan quotient. `notes/a2-complex-zeta/numerics.md`:141-145; review :488-489.
- **The brief's placement of the Kang–Li identity.** Fails at `u^3` (residual `-59904`) and fails the degree count (398736 vs 219024); also `det(I - uL_B)` in place of `det(I + uL_B)` fails at `u^15`. `notes/a2-complex-zeta/numerics.md`:128-135.
- **An exact finite-dimensional unital `*`-representation of the full BC algebra retaining the nontrivial phases.** Impossible: `mu_n mu_n^* = I` forces `e(1/n) = I`. (Finite *restrictions*, CP compressions and asymptotic approximations are **not** excluded.) `notes/bc-symmetry-generators.md`:66-80.
- **Imposing Weyl-translation plus full Weil covariance on the BC Lindbladian.** The cone collapses to the one-parameter depolarizer `gamma(Tr(X)I/p - X)`; "full affine symmetry in this model removes all oscillatory zero-like modes". `notes/bc-symmetry-generators.md`:215-238.
- **Hoping that the prescribed symmetries force equal odd decay rates.** They do not: the `p = 7` scalar-orbit perturbation `L = D - id + eps R_a` is CPTP, Weil- and parity-covariant, with three distinct odd eigenvalues. `notes/bc-symmetry-generators.md`:242-273.
- **Selecting the adelic coupling by marginal compatibility alone.** The family `L_c` has identical one-prime restrictions for every `c in [0, min(gamma_p,gamma_q)]`. `notes/bc-symmetry-generators.md`:277-300.
- **Using `-(B sigma + sigma B^*) >= 0` as a no-go.** It is necessary and sufficient only for a fixed no-event `B` with the scalar reset ansatz; failing it says nothing about the full GKLS cone. `notes/bc-symmetry-generators.md`:332-336.
- **Treating the "not found" literature verdicts as nonexistence proofs.** Explicitly refused by the prover; arXiv search is metadata-only. `notes/complex-zeta/astra-proofs.md`:1118; `notes/prior-art-quantum-ihara.md`:137.
