# Lane L11: source extracts (paper quotes with commentary)

Scope: the six byte-verified source-extract files in `notes/extract/`. The quotes
themselves are established mathematics and are **not** ledgered; what is ledgered is the
extractor's commentary — the "relevance" notes, the "this is what the notebook wants"
remarks, the scope caveats, the gaps, the verified negatives, and every paper that was
fetched but whose relevance was never acted on.

Line numbers below are lines **in the extract file named**, not in the arXiv source.
Where an extract line itself cites an arXiv locus (`<id>:<file>:<lines>`), that locus is
repeated inside the entry so a reader can jump twice.

## Coverage

| file | lines | read fully? | ideas found |
|---|---|---|---|
| `notes/extract/cohomological-zeta-sources.md` | 1890 | yes (1–1890, in chunks) | 30 (L11-001 … L11-030) |
| `notes/extract/complex-zeta-sources.md` | 1539 | yes (1–1539, in chunks) | 26 (L11-031 … L11-056) |
| `notes/extract/notation-and-definitions.md` | 373 | yes (1–373; Tables 1–2 are pure bookkeeping, Table 3 + "Ambiguities" carry the ideas) | 22 (L11-057 … L11-078) |
| `notes/extract/riemann-cmps-sources.md` | 1107 | yes (1–1107, in chunks) | 17 (L11-079 … L11-095) |
| `notes/extract/selberg-sources.md` | 350 | yes (1–350) | 9 (L11-096 … L11-104) |
| `notes/extract/weil-positivity-sources.md` | 957 | yes (1–957, in chunks) | 14 (L11-105 … L11-118) |

Total: **118** entries.

---

## Ideas and leads

### L11-001 The zeta as a determinant on a virtual super space — Deitmar's continuous prototype
- Source: `notes/extract/cohomological-zeta-sources.md:57-171`
- Raised by: a paper (Deitmar, *Geometric zeta-functions of locally symmetric spaces*, arXiv:dg-ga/9511006), with the extractor's commentary at :160-171
- Status at last mention: noted, not used (the extract calls it "the continuous prototype of the notebook's supertrace picture")
- Content: Deitmar proves a determinant formula in which the geometric zeta of a locally symmetric space is a regularised determinant of `H + s` on the **virtual space** `⊕_p (-1)^p V_p`, raised to `(-1)^{dim N}` (`dg-ga/9511006:main.tex:864,871`). He names the analogy himself: this is "a determinant formula similar to the determinant formula of Deligne expressing the Hasse–Weil zeta function as an alternating product of determinants of the Frobenius-action on étale cohomology" (`:269`). The Ruelle zeta is literally `∏_l Z_{∧^l n}(s + l|α|)^{(-1)^l}` over exterior degree (`:1153,1168`).
- Lead: transcribe the "determinant on a virtual super space" shape onto the notebook's transfer semigroup, i.e. write the Riemann channel's zeta as `det(H+s | ⊕_p (-1)^p V_p)`. If it worked, the notebook's supertrace claim would have a theorem-level continuous ancestor rather than only an analogy.
- Related: L11-004, L11-013, L11-014, L11-022, L11-079.

### L11-002 The divisor is the *weighted* Euler characteristic, not the plain supertrace
- Source: `notes/extract/cohomological-zeta-sources.md:118-146`
- Raised by: the extractor's commentary (:143-146) on Deitmar's vanishing-order theorem
- Status at last mention: flagged as a correction/warning; not used
- Content: Deitmar's order of vanishing is `χ_1 = -Σ_p p(-1)^p dim H^p`, the **higher** Euler number, and the last sentence of the quoted theorem says the *ordinary* alternating sum `χ = Σ_p (-1)^p dim H^p` **vanishes identically**. So a naive "supertrace" bookkeeping would give zero; the divisor is carried by the degree-weighted sum.
- Lead: whatever supertrace the notebook writes must carry the degree weight `p` (a number operator), not just the sign `(-1)^p`. Consequence if ignored: the alternating count is identically zero and says nothing.
- Related: L11-013 (Shen's supertrace of the number operator), L11-012 (Knill's `k(-1)^{k+1}` weight).

### L11-003 Supersymmetry as the original engine of higher-rank continuation (Moscovici–Stanton)
- Source: `notes/extract/cohomological-zeta-sources.md:147-159` (quoting `dg-ga/9511006:main.tex:254,259`)
- Raised by: a paper (Deitmar, recording Moscovici–Stanton)
- Status at last mention: noted, not used; Moscovici–Stanton itself was never fetched
- Content: Deitmar records that the higher-rank case "seemed impenetrable until H. Moscovici and R. Stanton used supersymmetry arguments to compute traces of certain linear combinations of heat operators", which gave continuation of the Ruelle zeta for `SL_3(R)` and `SO(p,q)` with `pq` odd.
- Lead: fetch Moscovici–Stanton and see what their supersymmetric heat-trace combination looks like as an operator identity; it may be the closest existing template for a supersymmetric proof on the notebook's side. None stated in the extract.
- Related: L11-001, L11-018.

### L11-004 Dyatlov–Zworski: odd sector upstairs, even sectors downstairs — the cleanest instance of the notebook's picture
- Source: `notes/extract/cohomological-zeta-sources.md:172-284`; also `selberg-sources.md:88-104`
- Raised by: a paper (Dyatlov–Zworski, *Ruelle zeta function at zero for surfaces*, arXiv:1606.04560), commentary at :275-284
- Status at last mention: noted, not used
- Content: `ζ_R(s) = ζ_1(s)/(ζ_0(s) ζ_2(s))` — 1-forms (odd) in the numerator, 0- and 2-forms (even) in the denominator, so `m_R(0) = m_1(0) - m_0(0) - m_2(0) = -χ(Σ)`. The even sectors contribute exactly `1` each (a one-dimensional "vacuum"), the odd sector contributes `b_1(M)`. The extractor's transcription: "the pole/fixed point is even and one-dimensional, the interesting modes are odd and counted by `H^1`".
- Lead: use this as the target shape for the notebook's channel zeta — a one-dimensional even sector (the fixed point / Perron eigenvalue) and an odd sector carrying the zeros. If achieved, RH would be a statement about the odd sector alone.
- Related: L11-001, L11-006, L11-079, L11-081.

### L11-005 The value at the special point is a torsion (Fried), read as a Lefschetz formula
- Source: `notes/extract/cohomological-zeta-sources.md:285-390`, `:495-544`, `:931-1005`
- Raised by: papers (Dang–Guillarmou–Rivière–Shen arXiv:1807.01189; Shen arXiv:1602.00664; Fried's own papers, not on arXiv, bibliographically byte-cited at :495-544)
- Status at last mention: noted, not used; the extract says "the torsion is exactly 'the supertrace of the graded complex'"
- Content: `|ζ_{X,ρ}(0)^{(-1)^{n_0}}| = τ_ρ(M)`, the Ray–Singer/Reidemeister torsion, for acyclic unitary `ρ`. Fried himself read this as "an analogue of the Lefschetz fixed point formula", answering his own question about a general connection between Ray–Singer torsion and closed orbits of a flow. Shen proves the conjecture for all odd-dimensional closed locally symmetric reductive manifolds (`R_ρ(0) = T(F)^2`).
- Lead: identify the notebook's analogue of "the special value" (`u=1` for graphs, `s=0` here) and ask what torsion it computes for a Kraus channel. If it is a torsion, the graded structure is forced rather than assumed.
- Related: L11-007, L11-012, L11-013, L11-008.

### L11-006 Warning: the alternating count is fragile — it is not topological under perturbation
- Source: `notes/extract/cohomological-zeta-sources.md:391-492` (commentary at :481-492)
- Raised by: a paper (Cekić–Delarue–Dyatlov–Paternain, arXiv:2009.08558) + the extractor's reading
- Status at last mention: flagged as a warning against over-reading the grading
- Content: In dimension 3 (5-dimensional sphere bundle) `m_R(0) = 4 - 2b_1` at the hyperbolic point but `4 - b_1` after a generic conformal perturbation — the degree-1 contribution halves and the alternating sum jumps. The extractor: "'the zeros are the odd cohomology' is a statement that can hold at a symmetric point and fail under perturbation, so any graded/supertrace realisation must be pinned by more than the alternating count."
- Lead: any claim in the notebook of the form "the zeros are the odd sector" must be accompanied by a rigidity/stability argument, not just a degree count. Consequence if ignored: the claim can be true at one channel and false at a nearby one.
- Related: L11-002, L11-004.

### L11-007 Which factor of the Ihara zeta carries the tree number (Hashimoto's `h'(1) = -2χκ`)
- Source: `notes/extract/cohomological-zeta-sources.md:566-697`
- Raised by: the extractor's synthesis (:668-697) across arXiv:2310.15619, arXiv:2405.04361, arXiv:2503.19641
- Status at last mention: used as a bookkeeping answer inside the extract; not carried into the notebook
- Content: `Z_X(u)^{-1} = (1-u^2)^{-χ(X)} h_X(u)` with `h_X = det(I - A u + (D-I)u^2)`. Both factors vanish at `u = 1`; the tree number `κ(X)` sits in `h'_X(1) = -2χ(X)κ(X)`, i.e. in the Laplacian/Hecke factor (Kirchhoff), while `(1-u^2)^χ` is the Euler-characteristic bookkeeping factor whose job is to cancel that zero.
- Lead: for the quantum Ihara zeta, compute the analogue of `h'(1)` and ask what "the number of spanning trees" becomes for a Kraus family. None stated.
- Related: L11-005, L11-012, L11-014, L11-018.

### L11-008 Hoffman: Bass's proof of the Ihara identity *is* a torsion-of-complexes computation
- Source: `notes/extract/cohomological-zeta-sources.md:698-741` (quoting `2607.21262:main.tex:351,366`)
- Raised by: a paper (J. W. Hoffman, *Remarks on the zeta function of a graph*, Discrete Contin. Dyn. Syst. 2003 — **not on arXiv**; content byte-cited from Kang–Yu)
- Status at last mention: noted, not used; the extract calls it "the direct, byte-verified answer" to "is `(1-u^2)^χ` the torsion-like factor?"
- Content: Kang–Yu say their own higher-rank proof "is inspired instead by Hoffman's reformulation of Bass's proof of the Ihara identity in terms of torsion of complexes". Euler products become determinants of successor operators on pointed `k`-facets; these assemble into a cochain complex; Laplacian-type endomorphisms compare the alternating product of successor determinants with the spherical Hecke determinant.
- Lead: obtain Hoffman's paper (not on arXiv) and redo the notebook's quantum Ihara–Bass proof as a torsion computation rather than a Schur complement. Consequence: the `χ` exponent would come out as a torsion, which is the notebook's claim.
- Related: L11-014, L11-016, L11-021.

### L11-009 A graph zeta that *is* a Reidemeister torsion already exists — via knot diagrams
- Source: `notes/extract/cohomological-zeta-sources.md:742-770`
- Raised by: a paper (Zhuang, *Ihara zeta function and twisted Alexander invariants*, arXiv:2104.00215) + commentary
- Status at last mention: noted, not used
- Content: The twisted Alexander polynomial is a Reidemeister torsion of a knot exterior, and this paper writes it as an Ihara-type zeta counting cycles on a knot diagram. So "there **is** a direct graph-zeta = torsion statement in the literature", but for the torsion of a 3-manifold via a diagram graph, not for `(1-u^2)^χ` itself.
- Lead: see whether the diagram-graph construction can be run with operator (Kraus) weights, giving a quantum twisted-Alexander/torsion. None stated.
- Related: L11-010, L11-008.

### L11-010 The `L²`-torsion obstruction: no direct relation between `L²`-torsion and matrix entries
- Source: `notes/extract/cohomological-zeta-sources.md:753-757` (quoting `2104.00215:…:721`)
- Raised by: a paper (Zhuang)
- Status at last mention: flagged as a gap / dead end for the `L²` route
- Content: Zhuang states plainly: "We cannot get a zeta function formula like the twisted Alexander case since, unlike the determinant, there is no direct relationship between the `L²`-torsion of a matrix and its entries." Fuglede–Kadison torsion resists the zeta treatment that ordinary determinants admit.
- Lead: none stated — record as a known obstruction if the notebook reaches for `L²`/von Neumann determinants.
- Related: L11-011, L11-047.

### L11-011 A ±1 sign carried by the *orbit* rather than by the coefficient space
- Source: `notes/extract/cohomological-zeta-sources.md:771-865`; also `complex-zeta-sources.md:998-1102`
- Raised by: a paper (Benard–Chaubet–Dang–Schick, arXiv:2303.11226) + commentary at :821-826 and :858-865
- Status at last mention: noted, not used; called "the strongest evidence that the graded picture survives discretisation"
- Content: The combinatorial zeta `ζ_T(z) = ∏_γ (1 - ε_γ z^{|γ|})` weights each primitive closed geodesic in the `(n-1)`-skeleton by a **reversing index** `ε_γ ∈ {-1,1}`, the parity of how often orientations flip along the orbit. The extractor stresses this is "a `Z_2`-grading carried by the orbit, not by the coefficient space". The vanishing order at `z = (n+2)^{-1}` is `b_1(M)`.
- Lead: try a per-orbit sign in the notebook's Euler product (a sign on each cyclically non-backtracking word) instead of a graded bond space. If it reproduces the same divisor, the grading may be cheaper than a fermionic bond.
- Related: L11-015, L11-017, L11-035.

### L11-012 Knill: analytic torsion of a graph **is** the super pseudo-determinant of the Dirac operator
- Source: `notes/extract/cohomological-zeta-sources.md:866-930`
- Raised by: a paper (Knill, *Analytic torsion for graphs*, arXiv:2201.09412); the extract calls it "the single most on-target source for the notebook's 'zeta = supertrace' picture on the discrete side"
- Status at last mention: noted, not used; and explicitly flagged as **not joined** to the Ihara zeta (see L11-021)
- Content: `A(G) = ∏_k Det(L_k)^{k(-1)^{k+1}} = SDet(D) = ∏_k Det(D_k)^{(-1)^k}`, and Knill says in his own words that this is the "**Fermionic**" version of the orientation-oblivious "**Bosonic**" pseudo-determinant. The combinatorial content is a generalised matrix-tree theorem: torsion = (rooted spanning trees on even simplices)/(rooted spanning trees on odd simplices). Triangle-free graphs recover Kirchhoff.
- Lead: join `SDet(D)` to the Ihara/Bass determinant identity (see L11-021); that join is exactly "zeta is a supertrace" on a graph.
- Related: L11-002, L11-007, L11-016, L11-021.

### L11-013 Analytic torsion is literally a supertrace of the form-degree number operator
- Source: `notes/extract/cohomological-zeta-sources.md:931-1005`
- Raised by: a paper (Shen, arXiv:1602.00664) + commentary at :995-1005
- Status at last mention: noted, not used; "the `str` shape the notebook wants is literally the definition of `T(F)`"
- Content: `θ(s) = -Str[N^{Λ(T*Z)} (□^Z)^{-s}]`, `T(F) = exp(θ'(0)/2) = ∏_i det(□|Ω^i)^{(-1)^i i/2}`. Milnor is credited (via `1602.00664:main.tex:241,243`) with first noticing "a remarkable similarity between the Reidemeister torsion and the Weil zeta function". The extractor notes that Deitmar's `χ_1`, Knill's `A(G)`, and Shen's `θ(s)` are "the same weighted supertrace".
- Lead: define the notebook's `str` with the number operator (degree weight) rather than the bare parity, and check that the three weights coincide.
- Related: L11-002, L11-012, L11-001.

### L11-014 `(1-u^n)^χ` is provably a determinant on cohomology — a torsion
- Source: `notes/extract/cohomological-zeta-sources.md:1008-1122`; also `complex-zeta-sources.md:309-456`
- Raised by: a paper (Kang–Yu, arXiv:2607.21262) + commentary at :1111-1122
- Status at last mention: noted, not used; the extract says this "settles the question ... **Yes, and provably so**"
- Content: `∏_i det(Φ_i | C_i)^{(-1)^i} = ∏_i det(Φ_i | H^i)^{(-1)^i} = ∏_i det(1-u^n | H^i)^{(-1)^i} = (1-u^n)^{Σ(-1)^i(i+1)V_i}`, giving `(1-u^n)^{χ(X)}` (`2607.21262:main.tex:2463,2487`). For `n=2` this is exactly Ihara: the numerator `(1-u^2)^χ` of the graph zeta is the determinant of a cochain automorphism over the whole (vertex, edge) complex.
- Lead: run the same Euler–Poincaré argument with the notebook's Kraus-weighted successor operators, to get the quantum `χ` exponent as a torsion rather than a dimension count.
- Related: L11-008, L11-016, L11-021, L11-032.

### L11-015 The `PGL(3)` chamber factor sits with the *opposite* sign — "surface vs curve"
- Source: `notes/extract/cohomological-zeta-sources.md:1123-1224`; `complex-zeta-sources.md:34-184`
- Raised by: a paper (Kang–Li, arXiv:0809.1401 / arXiv:0804.2305), with the authors' own remark quoted at `complex-zeta-sources.md:170`
- Status at last mention: noted, not used
- Content: In `Z(X_Γ,u) = (1-u^3)^χ / [det(I - A_1u + qA_2u^2 - q^3u^3 I)·det(I + L_B u)]` the chamber factor carries a **plus** sign and the transposed edge factor carries `u^2`. The authors say the resulting shape "is reminiscent of the zeta functions attached to a surface and a curve over a finite field" and that the identity "is likely to be the prototype of complex zeta functions in general".
- Lead: treat higher facet dimension as the source of extra cohomological degrees placed in numerator or denominator by parity — the notebook's "surface-like" reading. Next step: build the two-dimensional analogue for a channel.
- Related: L11-014, L11-031, L11-033, L11-056.

### L11-016 The fermionic proof of Bass's identity exists — and the `χ` exponent is an index
- Source: `notes/extract/cohomological-zeta-sources.md:1227-1365`
- Raised by: a paper (Matsuura–Ohta, *Fermions and Zeta Function on the Graph*, arXiv:2501.08803) + heavy commentary at :1298-1365
- Status at last mention: noted, not used; called "the closest thing in the literature to the notebook's 'the `χ` exponent is a supertrace'"
- Content: A Grassmann field on vertices and two per oriented edge; the Berezin integral gives `det(D̸ + M)`. One Schur decomposition gives `(1-t^2)^{n_E-n_V} det Δ_{q,u}` (Ihara/Bass), the other gives `det(I - qB_u)` (Hashimoto). Their equality **is** Bass's identity in Bartholdi-deformed form. Crucially `(1-t^2)^{-χ}` arises as `det(I_{n_E} - tJ) = (1-t^2)^{n_E}`, a fermionic determinant of the edge-reversal involution `J`, and the exponent `n_E - n_V` is **the difference of the dimensions of the two blocks of a chiral, block-off-diagonal Dirac operator**.
- Lead: redo the notebook's quantum Ihara–Bass (Theorem 1 of `notes/quantum-ihara-general.md`) as a Berezin integral over a chiral Dirac operator; the `χ` exponent would then be an index, not a bookkeeping count.
- Related: L11-012, L11-017, L11-020, L11-021, L11-070.

### L11-017 The parity is structural, not a sign in the measure — and the authors call it a Witten index
- Source: `notes/extract/cohomological-zeta-sources.md:1316-1352`
- Raised by: the extractor's explicit answer to the question "do vertex and edge fermions enter with opposite Grassmann parity or sign?"
- Status at last mention: answered inside the extract; not used
- Content: All of `ξ, ψ, ψ̃` are ordinary Grassmann variables in the same Berezin measure; the `Z_2` structure is that `D̸` is block off-diagonal between the vertex block and the edge block, with `γ_5`-hermiticity. The cycle-expansion signs are called "like the Witten index" by Matsuura–Ohta (`2501.08803:main.tex:1114`), and `γ_5`-hermiticity "allows us to construct the overlap fermion on the graph" (`:192`).
- Lead: two concrete leads left unpursued — (i) read the cycle Möbius signs as a Witten index for the notebook's channel; (ii) exploit `γ_5`-hermiticity / overlap fermions, which is a lattice-QCD technology never applied here.
- Related: L11-016, L11-019, L11-021.

### L11-018 Sign-reversing involutions are the combinatorial shadow of fermionic cancellation
- Source: `notes/extract/cohomological-zeta-sources.md:1366-1426`
- Raised by: a paper (Foata–Zeilberger, arXiv:math/9806037) + commentary at :1419-1426
- Status at last mention: noted, not used
- Content: Their proof of Bass's evaluations rests on an involution `π ↦ π'` with `deg π + deg π' = 0 mod 2` — pairing terms of opposite parity so they cancel, which "is the same cancellation that a Berezin integral performs automatically". And here too `(1-u^2)^{c_1-c_0}` comes out of `det(I - uJ) = (1-u^2)^{c_1}` with `J` the edge-reversal involution.
- Lead: for the operator-weighted case, look for the corresponding involution on words in the `A_k` and `A_k^†`; a sign-reversing involution would give a combinatorial (weight-free) proof of the quantum identity.
- Related: L11-016, L11-020.

### L11-019 `OSP(1|2)` supersymmetry on the spanning-tree side
- Source: `notes/extract/cohomological-zeta-sources.md:1427-1541`
- Raised by: papers (Caracciolo–Sokal–Sportiello arXiv:0706.1509; Caracciolo et al. arXiv:cond-mat/0403271; Abdesselam arXiv:math/0306396) + commentary at :1463-1471, :1535-1541
- Status at last mention: noted, not used
- Content: Unrooted spanning forests are generated by a non-Gaussian Grassmann theory with an honest `OSP(1|2)` supersymmetry, mapping to the `N`-vector model at `N = -1` / the `σ`-model on the unit supersphere in `R^{1|2}`, which in two dimensions is perturbatively **asymptotically free**. Abdesselam supplies all-minors and Hyperpfaffian-cactus generalisations by Grassmann–Berezin calculus.
- Lead: the extract records the exact hole — "**Not found: a paper joining the two into a single supersymmetric statement about `(1-u^2)^χ`**" (:1469-1471). Writing that join would supply a single supersymmetric proof of `h'(1) = -2χκ`.
- Related: L11-007, L11-012, L11-016.

### L11-020 "The loop ensemble has a fermionic nature" — the physics literature's own statement of the thesis
- Source: `notes/extract/cohomological-zeta-sources.md:1542-1592`
- Raised by: a paper (Aizenman–Warzel, arXiv:1709.06052, `:346`) + commentary at :1585-1592
- Status at last mention: noted, not used
- Content: The Bowen–Lanford/Ihara-type identity `det(1 - uM) = ∏_p [1 - u^{|p|} χ_M(p)]` holds for an **arbitrary non-backtracking flow matrix** `M`. Aizenman–Warzel say the reason the infinite Euler product collapses to a polynomial "is that the loop ensemble has a fermionic nature", and they use this as the engine of a short Kac–Ward derivation of the planar Ising free energy.
- Lead: the arbitrary-flow-matrix version is exactly the generality the notebook's Kraus setting needs; check whether the notebook's Theorem 1 is a special case, or whether operator weights genuinely break it.
- Related: L11-016, L11-018, L11-071.

### L11-021 **The gap**: nobody has joined Knill's `SDet` to the Ihara/Bass identity
- Source: `notes/extract/cohomological-zeta-sources.md:1624-1649` (the "What was NOT found" section), restated at `:1830-1835`
- Raised by: the extractor's commentary after negative searches
- Status at last mention: **flagged as a gap** — "That join is exactly what the notebook's 'zeta is a supertrace' would be, on a graph."
- Content: No source proves the Ihara/Hashimoto determinant identity by an explicit **supertrace** argument (a `Z_2`-graded trace with a parity operator `(-1)^F`). The two nearest are Matsuura–Ohta (parity is structural, no supertrace written) and Knill (an honest `SDet` statement, but about torsion of the Whitney complex, never mentioning Ihara — verified by `grep -c -i ihara refs/src/2201.09412/reidemeister.tex`).
- Lead: prove `Z_X(u)^{-1} = SDet(…)` for a finite graph. If it worked it would be a publishable standalone result and would justify the notebook's central metaphor.
- Related: L11-012, L11-016, L11-014.

### L11-022 One shape, four categories — Deninger / Deitmar / Kang–Yu / Dyatlov–Zworski
- Source: `notes/extract/cohomological-zeta-sources.md:1650-1678` (the observation is at :1668-1678)
- Raised by: the extractor's commentary
- Status at last mention: noted as "the only thing worth adding"; not used
- Content: `∏_{i=0}^2 (…)^{(-1)^{i+1}}` (arithmetic schemes), `∏_l Z_{σ_l}(s+l|α|)^{(-1)^l}` (locally symmetric spaces), `∏_k Z_k^ε(X,u)^{(-1)^{k+1}}` (Bruhat–Tits buildings), `ζ_R = ζ_1/(ζ_0ζ_2)` (Anosov flows) are four instances of one and the same shape in four different categories.
- Lead: state the shape once, abstractly (a zeta as an alternating product over a grading), and ask what the notebook's category contributes as a fifth instance. If the notebook can name the grading for channels, the analogy becomes a definition.
- Related: L11-001, L11-004, L11-014, L11-079.

### L11-023 Quantum walks on simplicial complexes exist but carry **no** zeta (verified negative)
- Source: `notes/extract/cohomological-zeta-sources.md:1681-1724`
- Raised by: the extractor's verified negative (`grep -c -i zeta refs/src/1507.01194/QW-simplicial.tex` → 0)
- Status at last mention: noted, not used — a paper fetched whose relevance was never acted on
- Content: Matsue–Ogurisu–Segawa (arXiv:1507.01194) construct a Szegedy-type quantum walk on simplicial complexes, observing linear spreading and localisation that "reflect not only topological but also geometric structures". No zeta, no Ihara, no backtracking term occurs anywhere in the source. A search sequel (`1707.00156`, *Quantum Search on Simplicial Complexes*) likewise has none.
- Lead: attach a zeta to this existing quantum walk on a complex — the object would be new (see L11-026). Consequence: the first quantum zeta of a complex.
- Related: L11-024, L11-026, L11-055.

### L11-024 The density-matrix graph zeta, and its authors' own Hilbert–Pólya remark
- Source: `notes/extract/cohomological-zeta-sources.md:1707-1734`
- Raised by: a paper (Bradshaw–LaBorde et al., arXiv:2307.03321) + commentary at :1725-1734
- Status at last mention: noted, not used; explicitly judged **not** a channel zeta
- Content: A density matrix is turned into edge weights on a complete graph and its edge zeta formed; there is a one-to-one correspondence between the nonzero eigenvalues of `ρ` and the singularities of the zeta, and the authors "call this 'a variant of the Hilbert-Pólya conjecture associated to this zeta function'". The extractor is blunt: it is "**not** a zeta of a quantum channel, not Kraus-weighted, and not on a complex — it is an ordinary edge zeta with `ρ`-derived scalar weights."
- Lead: none stated; the value is as prior art to distinguish the notebook's construction from.
- Related: L11-023, L11-026, L11-076.

### L11-025 "Ramanujan quantum expander" in the literature means a spectral gap, with no zeta at all
- Source: `notes/extract/cohomological-zeta-sources.md:1735-1772`
- Raised by: the extractor's verified negative on arXiv:2602.15180 (Iyer–Jain–Jordan–Somma): `grep -c -i zeta` → 0, `-i ihara` → 0, `-i simplicial` → 0
- Status at last mention: noted; confirms the notebook's usage is the standard one and that the RH reading is unclaimed
- Content: The strongest explicit-Ramanujan-quantum-expander paper defines Ramanujan purely as `λ ≤ 2√(D-1)/D` on the channel's second eigenvalue — the Hastings/Alon–Boppana bound — "and never a Riemann-hypothesis-for-a-zeta statement".
- Lead: this is the free half of the notebook's claim `RH ⇔ Ramanujan channel`; only the zeta side is unclaimed. See L11-072.
- Related: L11-072, L11-076, L11-114.

### L11-026 **Open**: a quantum (Kraus / channel) zeta of a complex or hypergraph
- Source: `notes/extract/cohomological-zeta-sources.md:1773-1804` (conclusion at :1791-1804); also `:1838`
- Raised by: the extractor's commentary after five named negative searches
- Status at last mention: **flagged as open**
- Content: Five searches are listed verbatim; all return either quantum expanders (channels, no complexes) or Ramanujan complexes (complexes, no channels), never both. The two known quantum-flavoured zetas are the `Ad(U)`-weighted Ihara zeta of a **graph** (Matsuura–Ohta, arXiv:2204.06424 — already recorded as prior art) and the density-matrix edge zeta of a **complete graph**. "The combination 'quantum zeta of a complex' — which is what a graded/supertrace quantum Ihara–Bass on a 2-complex would be — appears to be open."
- Lead: define the Kraus-weighted successor operators `T_k` on `k`-facets of a 2-complex and prove the alternating-product identity. Consequence: a genuinely new object, and the natural home for the notebook's grading.
- Related: L11-014, L11-023, L11-035, L11-041.

### L11-027 Ramanujan-complex material in the tree that carries no zeta (fetched, unacted)
- Source: `notes/extract/cohomological-zeta-sources.md:1763-1772`
- Raised by: the extractor's inventory
- Status at last mention: noted, not used
- Content: Already in `refs/src` and never exploited: `1605.02664` (First, the Ramanujan property for simplicial complexes), `1701.00154` (Kamber, `L^p`-expander complexes), `1712.02526` (Lubotzky, high-dimensional expanders), `1702.05452` (Lubetzky–Lubotzky–Parzanchevski — "this is where the higher-dimensional 'geodesic flow' non-backtracking operator lives"), `1804.08028` (Ramanujan graphs and digraphs). "None of these carries a *quantum-channel* zeta."
- Lead: mine `1702.05452` for the branching operator and re-weight it with Kraus operators (see L11-035, L11-026).
- Related: L11-026, L11-035, L11-041, L11-042.

### L11-028 First's Ramanujan property is defined with no zeta at all (verified negative)
- Source: `notes/extract/cohomological-zeta-sources.md:1824-1829`
- Raised by: the extractor's byte-level check
- Status at last mention: noted
- Content: `grep -c -i zeta refs/src/1605.02664/ram_complexes_v32.tex` → 8, but all eight are the Greek letter `ζ` used as a variable (an ordering map, a root of unity). "So First's Ramanujan-property paper defines Ramanujan-ness purely spectrally, with no zeta at all."
- Lead: none stated. Relevant as a caution when citing "Ramanujan ⇔ RH" for complexes.
- Related: L11-025, L11-042.

### L11-029 No graph-literature statement that `(1-u^2)^χ` "is a Reidemeister torsion"
- Source: `notes/extract/cohomological-zeta-sources.md:1830-1836`
- Raised by: the extractor's negative search
- Status at last mention: flagged as a gap (partly closed by L11-014)
- Content: The nearest byte-verified statements are Hoffman's torsion-of-complexes reformulation (cited second-hand) and Kang–Yu's own derivation of `(1-u^n)^χ` as `∏_i det(Φ_i|H^i)^{(-1)^i}`. Hoffman's own text is not on arXiv.
- Lead: write the sentence "`(1-u^2)^χ` is a Reidemeister torsion" as a theorem with a proof, using L11-014's mechanism.
- Related: L11-008, L11-014.

### L11-030 Non-arXiv sources named but never obtained (Fried, Juhl, Hashimoto, Bass, Northshield)
- Source: `notes/extract/cohomological-zeta-sources.md:495-565`, `:1805-1845`
- Raised by: the extractor's bibliographic bookkeeping
- Status at last mention: bibliographic data byte-cited from arXiv bibliographies; the content itself is second-hand
- Content: None of D. Fried's five papers is on arXiv; Juhl's *Cohomological Theory of Dynamical Zeta Functions* (Progress in Math. 194) is not; Hashimoto 1990, Bass 1992, Northshield 1998/1999 are not. Deitmar credits Juhl's rank-one method as "the central idea" of his own higher-rank argument (`dg-ga/9511006:main.tex:264,265`).
- Lead: Juhl's book is the single most relevant unread source for "a cohomological theory of dynamical zeta functions" — obtaining it is a concrete acquisition step.
- Related: L11-001, L11-005.

### L11-031 Ihara generalises **only** to quotients of affine buildings — the scope verdict
- Source: `notes/extract/complex-zeta-sources.md:16-32`
- Raised by: the extractor's "Short answer to the grounding question"
- Status at last mention: established as the scope of the literature; conditions everything else in the file
- Content: "Yes for **quotients of affine buildings**, and only there." The shape is always `(1-u^n)^χ / (vertex-Hecke determinant)` = an alternating product of `det(I ∓ Lu^j)` over facet dimensions, and RH is literally "the nontrivial zeros of each determinant factor sit on prescribed circles `|u| = q^{-c}`", equivalent to Ramanujan. For a **general** finite simplicial or cell complex there is no Ihara-type zeta with a Bass identity and a Ramanujan theorem.
- Lead: either restrict the notebook's complex-side ambitions to building quotients, or accept that the object it wants does not exist and must be invented (L11-026).
- Related: L11-026, L11-047, L11-049, L11-056.

### L11-032 RH for a complex is **not** a single-circle statement
- Source: `notes/extract/complex-zeta-sources.md:106-135`, `:175-183`, `:529-587`
- Raised by: papers (Kang–Li arXiv:0804.2305; Kang–Li–Wang arXiv:0809.1401v1; Fang–Li–Wang arXiv:1109.3854) + commentary at :180-183 and :584-587
- Status at last mention: noted as a structural warning
- Content: For `PGL_3`, Ramanujan is equivalent to: the vertex cubic's nontrivial zeros on `|u| = q^{-1}`; **or** the chamber factor's on the **three** circles `1, q^{-1/2}, q^{-1/4}`; **or** the edge factor's on the **two** circles `q^{-1}, q^{-1/2}`. "Note that, unlike the graph case, RH here does *not* say a single circle." For `PGSp_4` it is worse: the edge and chamber factors give only **bands** of moduli (`q^α`, `-2 ≤ α ≤ -1`) — "the first sign that 'RH ⇔ Ramanujan' in higher rank is not a single-circle statement."
- Lead: if the notebook's channel zeta is higher-rank-like, its RH may be a band statement (uniform decay within a range) rather than an exact-circle statement. That would change what "Ramanujan" must mean for the Phantasm.
- Related: L11-036, L11-037, L11-041.

### L11-033 The Rosetta stone: every determinant factor is a Langlands `L`-function
- Source: `notes/extract/complex-zeta-sources.md:458-528` (commentary at :520-528)
- Raised by: a paper (Kang–Li–Wang, arXiv:1505.00902)
- Status at last mention: noted, not used
- Content: Each determinant in the `PGL_3` and `PGSp_4` identities is identified with a Langlands `L`-function of a representation `π` of the dual group (minuscule `π_1, π_2`; spin and standard) and simultaneously with a zeta counting `π`-geodesic walks or galleries.
- Lead: ask which representation of which dual group the notebook's channel factors would correspond to. If the dictionary applies, "Ramanujan" becomes "tempered", i.e. a representation-theoretic condition rather than a spectral one.
- Related: L11-034, L11-041, L11-051.

### L11-034 The `q = 1` degeneration: the Euler-characteristic factor disappears
- Source: `notes/extract/complex-zeta-sources.md:500-508` and `:526-528`
- Raised by: a paper (Kang–Li–Wang) + the extractor's aside at :508 — "Useful for the notebook: `χ > 0` here and vanishes at the 'field with one element' `q = 1`"
- Status at last mention: noted, not used
- Content: `χ(B_Γ) = (1/3)(q-1)^2(q+1)N_0` for `PGL_3` and `(q-1)^2(q^2+q+1)N_p` for `PGSp_4`; both vanish at `q = 1`, where the building identity degenerates to the apartment identity.
- Lead: the `q → 1` (F_un) limit is a free structural handle nobody in the notebook has used; it kills the torsion factor and leaves a purely combinatorial identity. Consequence if pursued: possibly a "field with one element" reading of the notebook's `χ` exponent.
- Related: L11-014, L11-033.

### L11-035 The right higher-dimensional Hashimoto operator is a *branching* operator
- Source: `notes/extract/complex-zeta-sources.md:588-723` (commentary at :714-723)
- Raised by: a paper (Lubetzky–Lubotzky–Parzanchevski, arXiv:1702.05452)
- Status at last mention: noted, not used
- Content: The `j`-dimensional geodesic flow on pairs (basepoint, `j`-cell) of a building, multi-valued rather than a permutation, with geodicity enforced by "the next `(j+2)`-set is **not** a cell". In dimension one it is exactly the non-backtracking walk. Its digraph zeta is `det(I - uA_Y)^{-1}`, and Ramanujan complex ⇒ Ramanujan digraph ⇒ RH in the weak form `Re s ≤ 1/2` — **for every affine building**, not just `Ã_n` and `C̃_2`.
- Lead: build the Kraus-weighted version of the branching operator (see L11-026); LLP's proof is "a simple combinatorial treatment" that may survive operator weights where the representation-theoretic proofs would not.
- Related: L11-026, L11-036, L11-011, L11-043.

### L11-036 For digraphs, RH ⇔ Ramanujan is an iff — but RH is a **band**, `0 ≤ Re s ≤ 1/2`
- Source: `notes/extract/complex-zeta-sources.md:700-723`, `:724-763`
- Raised by: papers (LLP arXiv:1702.05452 remarks; Parzanchevski survey arXiv:1804.08028) + the extractor's summary at :761-763
- Status at last mention: noted, with an honesty caveat
- Content: LLP state explicitly that "the bound `|Re(s)| ≤ 1/2` is the true situation: there are poles with `|Re(s)| < 1/2`", already in the graph case at `|Re s| = 0` and in higher dimension strictly between. Parzanchevski: "a `k`-regular digraph `D` is Ramanujan if and only if every pole ... satisfies `Re s = 1` or `0 ≤ Re s ≤ 1/2`."
- Lead: if the notebook's transfer operator is non-normal (as a channel generally is), expect a band rather than a line; the "uniform decay" the programme seeks may have to be restated as a *bound*, not an equality.
- Related: L11-032, L11-035, L11-041.

### L11-037 Geodesic walks on a fixed building form an **almost-normal**, sharply `(d+1)`-normal family
- Source: `notes/extract/complex-zeta-sources.md:751-756`
- Raised by: a paper (Parzanchevski, quoting LLP Prop. 4.5, 5.3, 5.4)
- Status at last mention: noted, not used — mentioned once and never followed up
- Content: All geometric walks on quotients of a fixed building form a family of **almost-normal** digraphs; for the geodesic edge walk on `Ã_d`-Ramanujan complexes the digraphs are *sharply* `(d+1)`-normal and "can be made to be `m`-periodic for any `m` dividing `(d+1)`."
- Lead: "almost-normal" is exactly the kind of weakened-Hermiticity condition the notebook has been looking for on the channel side (a substitute for the missing Hilbert–Pólya self-adjointness). Next step: read LLP §4-5 and test whether Kraus transfer operators are almost-normal.
- Related: L11-036, L11-077, L11-117.

### L11-038 Storm's hypergraph zeta is a graph zeta in disguise
- Source: `notes/extract/complex-zeta-sources.md:764-858` (commentary at :840-858)
- Raised by: a paper (Storm, arXiv:math/0608761) + commentary
- Status at last mention: noted; judged not a new object
- Content: `ζ_H(u) = Z_{B_H}(√u)` — literally the Ihara zeta of the incidence bipartite graph in the variable `√u`. So any simplicial complex, read as a hypergraph, gets a zeta, "but it is a *graph* zeta of a derived graph, blind to the simplicial structure beyond incidence". Note the exponent placement: base `(1-u)`, not `(1-u^2)`, because of the `√u` substitution.
- Lead: this is the cheap route to "a zeta of any complex"; the question the notebook must answer is whether the blindness matters. If not, the whole complex programme collapses to graphs.
- Related: L11-039, L11-040, L11-031.

### L11-039 The "modified hypergraph RH" needs an auxiliary factor divided out
- Source: `notes/extract/complex-zeta-sources.md:823-838`
- Raised by: a paper (Storm) + commentary at :856-858
- Status at last mention: noted
- Content: `ζ_H(q^{-s})` satisfies the modified hypergraph RH iff `H` is Ramanujan — but "modified" means one first divides by `(1 + (r-1)q^{-s})^{n_2-n_1}`. The `(d,r)`-regular factorisation makes this explicit.
- Lead: the notebook's own zeta may likewise need a trivial-factor quotient before RH can be stated; record the shape of that correction.
- Related: L11-038, L11-105 ("trivial eigenvalues removed").

### L11-040 Size-graded (non-uniform) Ihara–Bass, and cubical complexes as hypergraphs
- Source: `notes/extract/complex-zeta-sources.md:859-927`
- Raised by: papers (Chodrow–Eikmeier–Haddock arXiv:2204.13586; Hiraoka–Ochiai–Shirai arXiv:2002.12099; Watanabe arXiv:2510.27134)
- Status at last mention: recorded for completeness; no Ramanujan/RH content; never used
- Content: A non-uniform Ihara–Bass with prefactor `f_H(μ) = ∏_k (1-μ)^{m_k(k-1)-n}(1+μ(k-1))^{m_k-n}` graded by hyperedge size (a data-science paper); the explicit statement that a `q`-dimensional cubical complex is a hypergraph on `(d-1)`-cubes and `d`-cubes; and a Bartholdi zeta for hypergraph coverings.
- Lead: the size-graded prefactor `f_H(μ)` is a *second* grading (by hyperedge size) distinct from the notebook's parity grading — worth a look as an alternative grading axis. None stated in the extract.
- Related: L11-038, L11-039.

### L11-041 Kamber: one Bernstein–Lusztig operator per simple coweight, with an iff
- Source: `notes/extract/complex-zeta-sources.md:930-987` (commentary at :980-987, scope caveat at :977-979)
- Raised by: a paper (Kamber, *`L_p`-Expander Complexes*, arXiv:1701.00154)
- Status at last mention: noted, not used
- Content: `ζ = 1/∏_{i=1}^n det(1 - h_{β_i} u^{l(β_i)})`, one factor per simple coweight; for `n=1` it is exactly Hashimoto; and `X` is an `L_p`-expander **iff** every pole satisfies `|λ| ≤ q^{(p-1)/p}` or `|λ| = q`. This supplies the converse LLP could not get, for buildings of general type. **Scope caveat recorded**: the abstract's "any complex" means any quotient of a building.
- Lead: the `L_p` family interpolates between "expander" and "Ramanujan" by a continuous parameter — exactly the kind of graded/tempered scale the notebook's "graded Harrow continuum = temperedness" reading wants. Next step: define `L_p`-expander for a quantum channel.
- Related: L11-031, L11-036, L11-033, L11-042.

### L11-042 "Flag-Ramanujan" / "strongly Ramanujan" are the same notion under three names
- Source: `notes/extract/complex-zeta-sources.md:984-997`, `:1449-1461`
- Raised by: papers (Kamber; First arXiv:1605.02664; Kang JNT 2016) as recorded by the extractor
- Status at last mention: noted, not used; Kang's paper **not on arXiv** and its content only reachable second-hand
- Content: Kamber's `L_2`-expander is equivalent to Kang's "strongly-Ramanujan" and First's "flag-Ramanujan". Kang's *Riemann Hypothesis and strongly Ramanujan complexes from `GL_n`* (JNT 161 (2016) 281–297) is the most general RH result for `Ã_n` buildings and is unavailable: searched via the arXiv API, two WebSearch passes, and the author's own publication list, which lists it with **no** arXiv number.
- Lead: obtain Kang JNT 2016 by other means; it is the one paper with the detailed pole locations by representation type.
- Related: L11-041, L11-032.

### L11-043 The only general-complex candidate: a combinatorial Ruelle zeta on a triangulation — with no Ramanujan notion
- Source: `notes/extract/complex-zeta-sources.md:998-1102` (commentary at :1085-1102)
- Raised by: a paper (Benard–Chaubet–Dang–Schick, arXiv:2303.11226)
- Status at last mention: noted; explicitly judged to have "**no** Ramanujan notion and **no** RH"
- Content: On any triangulation of a compact oriented `n`-manifold: count primitive closed geodesics in the `(n-1)`-skeleton (geodicity = LLP's condition), weight by `±1`, take the **direct** product (Selberg/Deitmar convention, no reciprocal). Result: a polynomial of degree `|T^{(n-1)}|` vanishing to order `b_1(M)` at `z = (n+2)^{-1}`, with an `L²` version whose leading coefficient is a Fuglede–Kadison determinant. But "the distinguished point `(n+2)^{-1}` is not `q^{-1/2}` and there is no spectral-gap statement."
- Lead: the honest question the extract leaves: can a Ramanujan/spectral-gap notion be attached to this zeta at all? If yes, the notebook gets a zeta of an arbitrary complex; if no, the two programmes (torsion-type and Ramanujan-type) are genuinely disjoint.
- Related: L11-011, L11-031, L11-035, L11-010.

### L11-044 Deitmar–Hoffman's `PGL_3` identity is deliberately weak — an unspecified power and an unspecified polynomial
- Source: `notes/extract/complex-zeta-sources.md:1106-1174` (commentary at :1167-1174)
- Raised by: a paper (Deitmar–Hoffman, arXiv:math/0407509)
- Status at last mention: noted as historical; superseded
- Content: The theorem says only that `Z(u) = det(1 - uπ_1 + u²qπ_2 - u³q³)^n / P(u)` for **some** `n ∈ N` and **some** polynomial `P`. The paper states flatly "There is no Ihara-formula for higher rank up to date" (2004). Kang–Li later pinned both down.
- Lead: the "weak identity" template (a determinant to an unspecified power over an unspecified polynomial) is a low-bar first result the notebook could aim for in its own setting before attempting the sharp identity.
- Related: L11-015, L11-014.

### L11-045 "The exponent prescribed by the trace formula is an Euler number" — Deitmar–Kang's sign argument
- Source: `notes/extract/complex-zeta-sources.md:1175-1240` (the flagged line is :1196-1197)
- Raised by: a paper (Deitmar–Kang, arXiv:1303.6848, `:803-805`), with the extractor marking it "**directly relevant to the notebook's graded/supertrace reading**"
- Status at last mention: noted, not used
- Content: Deitmar–Kang take Euler factors with a **positive** exponent, `Z_{1,+}(u) = ∏_c (1 - u^{l(c)})`, against Ihara's convention, and say there is "a deep reason for the sign in Selberg's paper ... It emerges that the exponent prescribed by the trace formula is an Euler number, in Selberg's original case the Euler number of a point."
- Lead: this is the cleanest external justification for the notebook's claim that the exponent can be negative because it is a supertrace/Euler number. Adopt the convention and cite the sentence.
- Related: L11-002, L11-014, L11-022.

### L11-046 The `χ - 1` exponent and the degree of the critical-line polynomial
- Source: `notes/extract/complex-zeta-sources.md:1218-1240`
- Raised by: a paper (Deitmar–Kang) + the extractor's note at :1239-1240
- Status at last mention: noted once, never followed up
- Content: Their RH theorem gives `Z_{2,+}(-u)/Z_{1,+}(u²) = (1-u³)^{χ-1}P_1(u)/[(1-q³u³)P_2(u)]` with `|α| = |β| = q^{1/2}` — note the exponent is `χ − 1`, **not** `χ`; and for a Ramanujan complex `P_1` has degree `N_1 - 3N_0 + 6`.
- Lead: the off-by-one in the exponent and the explicit degree count are the sort of details that break a supertrace bookkeeping; reconcile them before asserting the `χ` exponent is universal.
- Related: L11-045, L11-014.

### L11-047 The non-cocompact case, and zetas of **weighted** complexes
- Source: `notes/extract/complex-zeta-sources.md:1241-1259`
- Raised by: papers (Hong–Kwon, arXiv:2411.15489 and arXiv:2512.23276)
- Status at last mention: noted, not used
- Content: They treat a non-cocompact arithmetic lattice of `PGL_3`, and — the part that matters here — "extend the definition to **weighted** complexes ... we define the edge zeta function for those and express it in terms of a determinant, analogous to the Bass-Ihara formula" (`2411.15489:main.tex:944`). Also recorded: their pre-Kang–Yu statement that higher rank lacked a unified zeta.
- Lead: a weighted-complex Bass–Ihara formula is one step from an operator-weighted one; check whether their proof accommodates matrix weights. Consequence: a route to L11-026 that reuses existing machinery.
- Related: L11-026, L11-035, L11-071.

### L11-048 The LSV generators, concretely — "what a numerical construction needs"
- Source: `notes/extract/complex-zeta-sources.md:1307-1425` (flagged at :1343)
- Raised by: papers (Lubotzky–Samuels–Vishne, arXiv:math/0406217 and arXiv:math/0406208) + commentary at :1414-1425
- Status at last mention: noted, not used; "**No zeta function is defined in these two papers.**"
- Content: `Γ` is generated by `b_u = 1 - r z^{-1}` with `r ∈ F_{q^d}^×` of norm 1, one per `u ∈ F_{q^d}^×/F_q^×`; the quotient by a congruence subgroup is `PGL_d(F_{q^e})`; the 1-skeleton is its Cayley graph on colour-`k` products; the complex is the clique complex; the Hecke operators are the colour-shift sums `A_k`. The pairing relation `b_u b_{u'} = b_v b_{v'}` has an explicit solution.
- Lead: build an LSV complex numerically from these generators and compute a candidate quantum zeta on it — the notebook already has the `scripts/weil_lps.py` machinery for the graph case.
- Related: L11-026, L11-075.

### L11-049 Lubotzky's ICM: the complex-zeta programme is still only "a hope"
- Source: `notes/extract/complex-zeta-sources.md:1426-1445` (the extractor's "Read carefully" at :1442-1445)
- Raised by: a paper (Lubotzky, arXiv:1712.02526, `:497`)
- Status at last mention: noted as a programme-status datum
- Content: "An interesting direction of research is to try to associate to high dimensional complexes suitable 'zeta functions' with the hope that also in this context the Ramanujaness of the complex can be expressed via the RH." The extractor stresses this was still a hope, not a theorem, as of the 2018 ICM, and that the seven references cited are exactly the sources catalogued in the file.
- Lead: the programme is open and endorsed at ICM level — a positive result here would be of independent interest, quite apart from RH.
- Related: L11-026, L11-031.

### L11-050 Verified negative: Kang–Yu 2026 contains **no** RH or Ramanujan theorem
- Source: `notes/extract/complex-zeta-sources.md:450-456`
- Raised by: the extractor's grep of the source
- Status at last mention: flagged as a limitation of the newest and most general paper
- Content: Grepping `2607.21262` for `Ramanujan`/`Riemann hypothesis`/`tempered` returns only a historical remark and three bibliography titles. So the uniform `PGL_n` Ihara-type identity exists, but the RH statement for it does not, and must be sourced from Kang (unavailable), Kamber, or LLP.
- Lead: prove RH ⇔ Ramanujan for the Kang–Yu identity directly. None stated.
- Related: L11-014, L11-041, L11-042.

### L11-051 The Steinberg multiplicity is what produces the Euler-characteristic exponent
- Source: `notes/extract/complex-zeta-sources.md:275-282`
- Raised by: the extractor's reading of Kang–Li–Wang's proof (`0809.1401v1:main.tex:1183-1186`)
- Status at last mention: mentioned once in passing; never followed up
- Content: The proof is a factor-by-factor bookkeeping over five types of unitary Iwahori-spherical representations, and "the Steinberg multiplicity is what produces the Euler-characteristic exponent": the total number of Steinberg representations, with multiplicity, equals `3χ(X_Γ) - 3`.
- Lead: this is a representation-theoretic origin story for the `χ` exponent, parallel to and independent of the torsion origin story (L11-014) and the index origin story (L11-016). Reconciling the three would be informative.
- Related: L11-014, L11-016, L11-033, L11-046.

### L11-052 The source-tarball metadata hazard for `0809.1401`
- Source: `notes/extract/complex-zeta-sources.md:195-207` (the CAVEAT block)
- Raised by: the extractor's bookkeeping caveat
- Status at last mention: recorded as a citation hazard to respect
- Content: `refs/src/0809.1401/` holds the latest-version tarball carrying the **Kang–Li** title and author list, not Kang–Li–Wang, and is not byte-identical to `0804.2305`. The arXiv abs page reports the Kang–Li–Wang title for all three versions. "**Quote Kang–Li–Wang from `0809.1401v1` only.**"
- Lead: none mathematical; an operational rule for the provenance database.
- Related: -

### L11-053 The two-expression structure as the analogue of "surface vs curve"
- Source: `notes/extract/complex-zeta-sources.md:160-184`
- Raised by: the extractor's "Placement, spelled out" and plain summary
- Status at last mention: noted
- Content: The same zeta has two closed forms — a Hecke/vertex form with `(1-u^3)^χ` in the numerator and the vertex + chamber determinants in the denominator, and a Hashimoto/edge form with only edge determinants. "Note the **plus** sign in `det(I + L_B u)` and the `u²` in the transposed edge factor."
- Lead: the notebook's Theorem 1 already has two forms (`1 - uM(u)` and `1 + D - A`); ask whether they line up with the vertex/edge dichotomy here, and whether a third (chamber-like) form is missing.
- Related: L11-015, L11-071.

### L11-054 The Euler-product reading of the `PGL_3` left-hand side (`Z_-` and `Z_1`)
- Source: `notes/extract/complex-zeta-sources.md:175-184`
- Raised by: a paper (Kang–Li, arXiv:0804.2305, Theorem at `:3066-3072`)
- Status at last mention: mentioned once ("This gives another interpretation of the zeta identity"); never followed up
- Content: `Z_-(Γ,u) = det(1+L_Bu)/det(1-L_Eu²)` and `Z(Γ,u) = det(1+L_Bu)det(1+L_Bu^{1/2})/[det(1-L_Eu)det(1-L_Eu²)]`, whence `(1-u³)^χ/det(vertex cubic) = Z_1(X_Γ,u)Z_-(Γ,u)`.
- Lead: the factorisation into an "algebraic" and a "geometric" factor is a decomposition the notebook has not attempted; note the half-power `u^{1/2}` in the second expression.
- Related: L11-053, L11-015.

### L11-055 Named-only, unobtained originals (Hashimoto 1989, Bass 1992, Ihara 1966, Li 2004, Cartwright–Steger)
- Source: `notes/extract/complex-zeta-sources.md:1489-1498`
- Raised by: the extractor's not-found list
- Status at last mention: named, not quoted
- Content: Hashimoto's 1989 *Zeta functions of finite graphs and representations of p-adic groups* is "the origin of the non-backtracking operator and of the bipartite factorisation used by Storm", and is not on arXiv; nor are Bass 1992, Ihara 1966, W.-C. W. Li's *Ramanujan hypergraphs*, Cartwright–Solé–Żuk, or Cartwright–Steger (the source of the lattice `Γ` used in L11-048).
- Lead: acquire Hashimoto 1989 — everything on the bipartite/edge side descends from it, and the notebook currently relies on second-hand statements.
- Related: L11-030, L11-038, L11-048.

### L11-056 Three literature admissions that the general object does not exist
- Source: `notes/extract/complex-zeta-sources.md:1462-1480`
- Raised by: the extractor's assembly of three self-assessments
- Status at last mention: **flagged as the central gap of the complex lane**
- Content: `math/0407509:main.tex:174` (2004) — "There is no Ihara-formula for higher rank up to date"; `2411.15489:main.tex:354` (2024) — "One problem in higher rank is the lack of a unified zeta function, as in higher dimensional buildings there are several possibilities to generalize Ihara's approach"; `1712.02526:main.tex:497` (2018) — still a "hope"; and even Kang–Yu 2026's own "first Ihara-type identity uniform in `n`" is only for `PGL_n` buildings. Six named search phrasings all returned nothing of the sought kind.
- Lead: the honest position for the notebook is that the general-complex Ihara zeta is an open construction problem, and inventing it is a legitimate contribution independent of RH.
- Related: L11-026, L11-031, L11-043, L11-049.

### L11-057 **Open**: a jump-type (Holevo-form) generator on `K_S` with jumps at `k log p`
- Source: `notes/extract/notation-and-definitions.md:286` (`open-stinespring-prime-jumps`)
- Raised by: the notebook's own note RCN §7 / HANDOFF, recorded by the extractor
- Status at last mention: "Not established, and not claimed"; HANDOFF suggests a blind codex lane
- Content: Whether a Holevo-form generator with jumps at the prime lengths `k log p` reproduces the Lax–Phillips semigroup `Z(t)`. If it did, "its physical index would be the Stinespring environment" — i.e. the primes would literally be the environment of a dilation.
- Lead: construct the jump generator and compare its semigroup to `Z(t)`; run it as a blind lane. Consequence: a physical (open-system) realisation of the prime side.
- Related: L11-058, L11-091, L11-063.

### L11-058 **Open**: identification with the Phantasm constructions SP-PRIME and SP-BC-CONTROL
- Source: `notes/extract/notation-and-definitions.md:288` (`open-phantasm-identification`)
- Raised by: the notebook (RCN §7, HANDOFF)
- Status at last mention: Not established
- Content: SP-PRIME and SP-BC-CONTROL are `β > 1` objects, whereas the Riemann-channel construction is a `β = 1` phase compressed to a co-invariant subspace. No identification has been made.
- Lead: settle whether the `β = 1` compression can be obtained as a limit of the `β > 1` constructions. None stated beyond noting the mismatch.
- Related: L11-057, L11-089.

### L11-059 **Open**: identify the joint spectrum with Hecke eigenvalues (LMFDB + Jacquet–Langlands)
- Source: `notes/extract/notation-and-definitions.md:303` (`open-lmfdb-hecke-identification`)
- Raised by: the notebook (WLP §3, §5; HANDOFF "Next steps 1")
- Status at last mention: **not done**
- Content: The joint eigenvalue pairs `(a_{q_1}, a_{q_2})` of the Weil-representation channels were computed but never matched to Hecke eigenvalues `a_q(f)` of weight-2 forms for the quaternion algebra ramified at `{2, ∞}` with level determined by `p`. Doing so needs LMFDB and Jacquet–Langlands bookkeeping.
- Lead: run the LMFDB lookup. If the match holds, the channels' Ramanujan property is *derived* from modularity rather than checked numerically.
- Related: L11-060, L11-075, L11-076.

### L11-060 **Open**: assembling the channels over all `p` (the DG-GLOBAL question)
- Source: `notes/extract/notation-and-definitions.md:304` (`open-assemble-over-p`)
- Raised by: the notebook (WLP §5; HANDOFF "Next steps 1")
- Status at last mention: Not established
- Content: Nothing is known about `p → ∞`, or about assembling the `Φ_q` over all `p` into a single object with the primes as rings — "the DG-GLOBAL question in a new guise".
- Lead: this is the step that would turn a family of finite Ramanujan channels into something with a chance of seeing the actual zeros. Consequence if it worked: side A and side B joined.
- Related: L11-059, L11-063, L11-075.

### L11-061 **Open**: the Artin–Schreier unitarity lemma is not rigorously written
- Source: `notes/extract/notation-and-definitions.md:315` (`open-as-rigorous-lemma`), with the theorem row at `:311`
- Raised by: the notebook (ASM §6)
- Status at last mention: Not established (the statement has a one-line proof and `10^{-15}` numerics, but no written lemma)
- Content: `EE^† = qI` whenever `a_J ≠ 0`, because the oldest spin appears only in the linear term, so summing over it gives `qδ`. This is what delivers the Weil bound `|α_i| = √q` for the whole quadratic Artin–Schreier family "by the same mechanism as for a finite permutation".
- Lead: write the lemma with the exact hypothesis `a_J ≠ 0` and the even-`n` sign convention. Cheap and load-bearing.
- Related: L11-062, L11-064, L11-086.

### L11-062 **Open, never searched**: a basis of `F_{q^n}` uniform in `n` that makes cubic traces local
- Source: `notes/extract/notation-and-definitions.md:316` (`open-as-other-basis`)
- Raised by: the notebook (ASM §6)
- Status at last mention: Not established — "No candidate was found or searched for."
- Content: For cubic or higher `g`, `Tr(x³)` in normal-basis coordinates has non-local, `n`-dependent structure constants, so there is no fixed local tensor **in the shift basis**. Whether some *other* uniform basis restores locality was never examined.
- Lead: search for such a basis. If one exists, the MPS construction extends past the quadratic family and the "sharp dividing line" of `neg-cubic-nonlocal` dissolves.
- Related: L11-063, L11-064.

### L11-063 **Open**: an MPS with a fixed local tensor for any non-maximal curve
- Source: `notes/extract/notation-and-definitions.md:317` (`open-as-nonquadratic-mps`)
- Raised by: the notebook (ASM §6)
- Status at last mention: Not established
- Content: No MPS with a fixed local tensor is known for a non-quadratic Artin–Schreier curve, or for any curve of genus `≥ 1` not of the maximal type.
- Lead: this is the obstacle between the notebook's one worked example and a general "curves as MPS" statement. Consequence if solved: side A gets a genuinely general tensor-network model.
- Related: L11-062, L11-086, memory item "curve counts as ring norms".

### L11-064 Dead-end diagnosis: the quadratic/cubic dividing line is sharp
- Source: `notes/extract/notation-and-definitions.md:313` (`neg-cubic-nonlocal`)
- Raised by: the notebook (ASM §4, §5; HANDOFF item 6)
- Status at last mention: derived; "the dividing line is therefore sharp"
- Content: `Tr(x³) = Σ_{ijk} c_{ijk} x_i x_j x_k` with non-local, `n`-dependent structure constants in the shift basis.
- Lead: none, except via L11-062.
- Related: L11-062, L11-063.

### L11-065 Dwork's transfer operator delivers rationality and the functional equation but **not** RH
- Source: `notes/extract/notation-and-definitions.md:314` (`prop-dwork-transfer-operator`)
- Raised by: the notebook (ASM §4; HANDOFF item 6), cited to Dwork 1960
- Status at last mention: cited + assessment
- Content: `α = ψ_q ∘ M_F` gives `S_n^× = (q^n - 1)Tr(α^n)` and `L` as a Fredholm determinant — "a coarse-graining tensor-network step with nuclear bond dimension" — but it sees `p`-adic sizes (Newton polygon), not complex absolute values, so it cannot give RH.
- Lead: recorded as a dead route for the RH half; still live as a template for "transfer operator with nuclear bond dimension".
- Related: L11-061, L11-086.

### L11-066 **Open**: what replaces `μμ' = D-1` when `E_ī E_i ≠ 1`
- Source: `notes/extract/notation-and-definitions.md:340` (`open-ramanujan-without-mumu`)
- Raised by: the notebook (QIG §6; HANDOFF "Next steps 1a")
- Status at last mention: open; HANDOFF suggests a cheap counterexample hunt (random MPS, pole radii of `ζ`)
- Content: Without the inverse pairing there is no quadratic relation pairing the roots, so the general quantum Ihara–Bass theorem "gives no Ramanujan-type reading by itself". Whether the canonical form `Σ_k A_k^† A_k = 1` buys anything is open.
- Lead: run the counterexample hunt — random MPS tensors, measure the pole radii of `ζ_Φ`, and see empirically whether a Ramanujan-type circle survives. Cheap, decisive.
- Related: L11-071, L11-072, L11-078.

### L11-067 The conjecture the notebook claims as its own: RH for `ζ_Φ` ⇔ Hastings-Ramanujan
- Source: `notes/extract/notation-and-definitions.md:343` (`claim-rh-iff-hastings-ramanujan`), with the prior-art verdict at `:346`
- Raised by: the notebook (PAQ §0 claim 2; HANDOFF item 1)
- Status at last mention: prior-art verdict **not found** across ten arXiv metadata queries — "present the RH-for-channels reading ... as this notebook's contribution"
- Content: All nontrivial poles of `ζ_Φ` lie on `|u| = (D-1)^{-1/2}` iff `Φ` is a Ramanujan quantum expander in Hastings' sense. Matsuura–Ohta contain none of the words Ramanujan, expander, Riemann hypothesis; Bordenave–Collins have the operator but no determinant or zeta.
- Lead: prove it (or find the counterexample via L11-066).
- Related: L11-025, L11-066, L11-072, L11-114.

### L11-068 "Some arithmetic rigidity has to enter, playing the role weights play for curves"
- Source: `notes/extract/notation-and-definitions.md:290` (`obs-kraus-structure-insufficient`)
- Raised by: the notebook's own assessment (WRH §7)
- Status at last mention: assessment, standing
- Content: The graph lesson says the Kraus structure alone will not force degeneracy of the decay rates; something arithmetic must be added.
- Lead: identify the arithmetic input. This is the programme's central unanswered question, restated in channel language.
- Related: L11-069, L11-070, L11-074.

### L11-069 What must enter: "a positivity plus an operation under which eigenvalues multiply while the loss stays fixed"
- Source: `notes/extract/notation-and-definitions.md:332` (`obs-ramanujan-without-hermiticity`)
- Raised by: the notebook's assessment (DVG §10)
- Status at last mention: assessment
- Content: Deligne's route and the interlacing (MSS) route both reach the spectral bound **without** a Hilbert–Pólya operator; what they share is a positivity together with an operation under which eigenvalues multiply while the loss stays fixed (tensor powers for Deligne; interlacing for MSS).
- Lead: find the channel-side operation with that property — tensor powers of a channel multiply eigenvalues, and the question is what stays fixed. This is the sharpest constructive suggestion in the whole notation file.
- Related: L11-068, L11-073, L11-074, L11-077.

### L11-070 Ramanujan-ness has exactly three known sources
- Source: `notes/extract/notation-and-definitions.md:268-269` (`obs-most-graphs-not-ramanujan`, `prop-three-sources-of-ramanujan`)
- Raised by: the notebook (DVG §3; WRH §7; HANDOFF steering)
- Status at last mention: established (the negative part) + cited
- Content: There is no theorem that a `(q+1)`-regular graph is Ramanujan; most are not, and "Ramanujan-ness is never a consequence of the structure". The three known sources are arithmetic (LPS via Deligne), probabilistic-asymptotic (Friedman, Hastings), and interlacing families (Marcus–Spielman–Srivastava).
- Lead: any Phantasm must draw on one of the three, or introduce a fourth. Worth stating as a constraint on the search space.
- Related: L11-068, L11-069, L11-075.

### L11-071 The general quantum Ihara–Bass theorem, and what it does and does not deliver
- Source: `notes/extract/notation-and-definitions.md:334-339`, `:341-342` (`thm-qihara-general`, `cor-qihara-kraus`, `cor-qihara-inverse-pairing`, `cor-qihara-pole-bookkeeping`, `prop-side-a-positive`, `prop-wf-does-not-cover-bouquet`)
- Raised by: the notebook (QIG §2-§6), `proved` with numerics
- Status at last mention: proved; the Ramanujan reading is open (L11-066)
- Content: `det_W(1-uT) = ∏_{{i,ī}} det_V(1-u²E_ī E_i) · det_V(1 + D(u) - A(u))`. For a Kraus family, `Tr_W T^ℓ = Σ |Tr(A_{i_ℓ}···A_{i_1})|² ≥ 0`, so `ζ` has nonnegative Taylor coefficients and an Euler product over primitive cyclically non-backtracking classes — **side A is unconditionally positive**. Watanabe–Fukumizu's graphs are hypergraphs with two-element hyperedges, so a bouquet is not one of their graphs: Theorem 1 is the loop-admitting extension, not an instance.
- Lead: the standing task is to convert the unconditional positivity of side A into a constraint on side B (see L11-105, L11-112).
- Related: L11-016, L11-020, L11-066, L11-112.

### L11-072 Prior-art verdicts: what is known, what is not
- Source: `notes/extract/notation-and-definitions.md:344-348` (`verdict-claim1-known`, `verdict-claim3-known`, `verdict-claim2-not-found`, `verdict-claim4-mechanism-known`, `verdict-mps-reading-not-found`)
- Raised by: the notebook's prior-art pass (PAQ)
- Status at last mention: four verdicts recorded
- Content: (1) the `Ad(U)`-weighted Ihara–Bass formula is **known** (Matsuura–Ohta 2022; Watanabe–Fukumizu 2011 for loopless graphs; twisted zeta back to Sunada 1986 / Hashimoto 1989); (2) RH-for-channels ⇔ Hastings-Ramanujan is **not found**; (3) the trace formula / Artin–Ihara `L`-function reading is **known**; (4) exactly-Ramanujan channels from LPS — mechanism known (Harrow 2008 + LPS; Iyer–Jain–Jordan–Somma Feb 2026, who call explicit Ramanujan quantum expanders "a longstanding open problem"), but **no Weil-representation instance and no zeta**; (5) the MPS/ring-norm reading and "AKLT = `K_4`" are **not found**.
- Lead: claims (2), (4-instance) and (5) are the notebook's unclaimed territory; write them up as such.
- Related: L11-025, L11-067, L11-075.

### L11-073 Dead route: prime-by-prime ansätze cannot see the zeros
- Source: `notes/extract/notation-and-definitions.md:349` (`obs-circle-flows-cannot-see-zeros`)
- Raised by: a recorded discussion (HANDOFF "Discussion 2026-09-12: circle flows")
- Status at last mention: established (negative)
- Content: The direct sum over `p` of rotations on circles of circumference `log p` has trace `Σ_n Λ(n)δ(s - log n)` by Poisson, and dynamical zeta equal to the Euler product — it is pure side A. For finite sets of primes its spectrum is the poles of the partial Euler product. Hence direct sums and commuting dilations, prime by prime, cannot produce zeros.
- Lead: none — a recorded dead end that saves repeating the construction.
- Related: L11-060, L11-074.

### L11-074 Dead route: `ζ` has no `X × X`, so Deligne's "multiply" step has nothing to act on
- Source: `notes/extract/notation-and-definitions.md:330-331` (`obs-zeta-lacks-the-product`, `obs-rankin-selberg-shadow`)
- Raised by: the notebook (DVG §10), called "the standard diagnosis, stated in the terms of this note"
- Status at last mention: established (negative) + cited
- Content: `ζ` is on the curve side of the table (zeros subtracted, `Λ(n) ≥ 0`), but there is no `X × X` with `ζ` as its slice. The number-field shadow of the pointwise theorem is Rankin–Selberg, and knowing the poles of all tensor-power `L`-functions is the analogue of big monodromy, i.e. Langlands functoriality — unproved; Kim–Sarnak `7/64` is the current state.
- Lead: recorded as the reason the Deligne route is blocked; pairs with L11-069's question of what operation *could* multiply eigenvalues.
- Related: L11-069, L11-073, L11-078.

### L11-075 Deligne's step 3 is false for graphs, and must be (worked counterexample)
- Source: `notes/extract/notation-and-definitions.md:322` (`ex-bouquet-not-pure`), with context at `:319-329`
- Raised by: the notebook (DVG §5), a worked counterexample
- Status at last mention: established
- Content: On a bouquet of two loops, `ρ(a) = [[2,1],[1,1]]`, `ρ(b) = [[1,1],[1,2]]` satisfy real traces, an alternating pairing with `c = 1`, and big monodromy — yet `ρ(a)` has eigenvalue `(3+√5)/2 > 1`. So the purity step fails for graphs. Relatedly: "Deligne's proof never exhibits a Hermitian structure"; Grothendieck's standard-conjectures plan is open; above dimension one the inner product making Frobenius normal is not known to exist.
- Lead: identifies precisely which hypothesis of Deligne's argument the graph/channel setting lacks — worth stating as the missing ingredient rather than re-deriving it.
- Related: L11-069, L11-074, L11-070.

### L11-076 The channels are Ramanujan because of Deligne, not because they are channels
- Source: `notes/extract/notation-and-definitions.md:305` (`obs-ramanujan-from-deligne-not-channels`), also `:329` (`obs-lps-needs-only-curve-case`)
- Raised by: the notebook's own assessment (WLP §4, "The last row is the honest one")
- Status at last mention: assessment, standing
- Content: "These channels are exactly Ramanujan because Deligne proved the Weil conjectures, not because they are channels." And: the Ramanujan property of the LPS graphs needs only the **curve** case (Eichler–Shimura transports Hecke eigenvalues to Frobenius eigenvalues of a modular curve), so Weil's theorem suffices; Deligne's method extends it to higher weight and `τ(p)`.
- Lead: a sobriety constraint — any claimed channel-theoretic explanation of Ramanujan-ness must add something beyond transporting Deligne.
- Related: L11-068, L11-070, L11-072.

### L11-077 RH for an MPS: all correlation lengths equal, `ξ = 2/h`
- Source: `notes/extract/notation-and-definitions.md:271` (`prop-mps-rh-one-correlation-length`); the three-row hierarchy at `:184-251` (Table 2, "primitivity / spectral gap / Ramanujan hierarchy")
- Raised by: the notebook (WRH §4), status `sketched` in rk-light terms
- Status at last mention: a translation, sketched
- Content: The hierarchy is: one eigenvalue on the unit circle = primitivity (PNT, `ζ(1+it) ≠ 0`); all others strictly inside = spectral gap (zero-free region); all others on **one** circle of radius `e^{-1/ξ}` with `ξ = 2/h` = Ramanujan/RH. RH for an MPS therefore reads "all correlation lengths are equal, and equal to twice the inverse entropy rate."
- Lead: this is the notebook's crispest physical statement of RH; testing it against real MPS families (and against L11-066's counterexample hunt) is a concrete experiment.
- Related: L11-066, L11-070, L11-093.

### L11-078 Unverified founding-session numerics that no script reproduces
- Source: `notes/extract/notation-and-definitions.md:261` (`num-shift-examples-rh`), also `:263-264`
- Raised by: the founding conversation, recorded by the extractor
- Status at last mention: "quoted 'from the conversation'; **no script in this repo**"
- Content: The 4-symbol cyclic-rule shift has small-matrix eigenvalues `2, 1±i, 0` and satisfies the RH analogue; the golden-mean shift has `φ, -1/φ` and does not. Similarly the `K_4` and prism numbers are labelled "from the founding session" with no script.
- Lead: write the three-line script and register the results. Cheap; it is the notebook's simplest RH-fails example and is currently unreproducible.
- Related: L11-077, L11-070.

### L11-079 Deninger's forced grading: `H^0` and `H^2` are the poles, `H^1` carries the zeros
- Source: `notes/extract/riemann-cmps-sources.md:76-200` (relevance note at :177-180)
- Raised by: a paper (Deninger, arXiv:math/0505354), commentary by the extractor
- Status at last mention: noted as **the** citation for the notebook's `Z_2`-grading
- Content: `ζ̂_K(s) = ∏_{i=0}^2 det_∞((s-Θ)/2π | H^i_dyn)^{(-1)^{i+1}}`, with `H^0 = R` and `Θ = 0`, `H^1` infinite-dimensional with spectrum the nontrivial zeros, `H^2 ≅ R` with `Θ = id`, and `H^i = 0` for `i > 2`. The Lefschetz form is `Σ_i (-1)^i Tr(φ*|H^i) = 1 - Σ_ρ e^{tρ} + e^t` — "the supertrace with the zeros entering with a minus sign". The dictionary pairs finite places with closed orbits of length `log Np`.
- Lead: "the `Z_2`-grading of the notebook's operator is exactly Deninger's `(-1)^i`" — make that identification precise for the Riemann channel.
- Related: L11-004, L11-022, L11-080, L11-082.

### L11-080 Deninger 2018 actually constructs the spaces — the programme is live
- Source: `notes/extract/riemann-cmps-sources.md:181-199` (relevance note at :197-199)
- Raised by: a paper (Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400)
- Status at last mention: noted, not used
- Content: Deninger records that the conditions for periodic orbits to correspond to primes with `l(γ) = log p` "were written down a long time ago ... but for too many years I had no idea how to construct natural `Q^{>0}`-spaces realizing these conditions" — and the 2018 paper is where he does. The extractor: "cite it for 'this is still a live programme, not only a 1998 analogy'."
- Lead: read the 2018 construction and ask whether the constructed space admits a transfer-semigroup / channel description. That would be a direct bridge to side B.
- Related: L11-079, L11-081.

### L11-081 The generator `θ` of the flow plays the role of Frobenius
- Source: `notes/extract/riemann-cmps-sources.md:201-226`
- Raised by: a paper (Deninger, arXiv:0709.2801, `:445`, `:552-557`, `:425`)
- Status at last mention: noted, not used
- Content: `θ = lim_{t→0}(φ^{t*} - id)/t` on leafwise cohomology "plays a similar role as the Frobenius morphism on étale or crystalline cohomology"; the Ruelle zeta is `∏_i det_∞(s·id - θ | H^i_F(X))^{(-1)^{i+1}}` with `ε_γ = sgn det(1 - T_xφ^{l(γ)})`; and the dictionary line reads "Explicit formulas of analytic number theory ↔ transversal index theorem for `R`-action ... and Laplacian along the leaves".
- Lead: the notebook's Lindbladian generator is the natural candidate for `θ`; the "transversal index theorem" line is an unexplored suggestion for what the explicit formula becomes.
- Related: L11-079, L11-090, L11-096.

### L11-082 Connes: the Polya–Hilbert space appears **from its negative**, `⊖H`
- Source: `notes/extract/riemann-cmps-sources.md:273-360` (relevance note at :356-360)
- Raised by: a paper (Connes, arXiv:math/9811068, `:194-209`, `:469-476`, `:556-581`, `:3037-3040`)
- Status at last mention: noted as the citation for "the zeros are odd"
- Content: Connes identifies two mismatches with the Selberg trace formula, the first being "the overall **minus sign**", and resolves it: the analogue of the Polya–Hilbert space is `H^1_et`, which appears with a minus in the Lefschetz formula. Hence "(C) The Polya-Hilbert space `H` should appear from its negative `⊖H`" — an **absorption** spectrum, not an emission spectrum. He adds that Berry–Keating's count is off precisely because of this.
- Lead: the notebook's transfer operator should be sought as a *negative* / odd sector. Concretely: look for the zeros as *missing* lines in a continuum, not as eigenvalues of a positive object.
- Related: L11-079, L11-083, L11-004.

### L11-083 The Sonin space and the positive-by-construction functional `Tr(ρ(f)S)`
- Source: `notes/extract/riemann-cmps-sources.md:361-386`
- Raised by: a paper (Connes–Consani, arXiv:2006.13771, `:113`)
- Status at last mention: mentioned once, never followed up
- Content: Removing the absorption spectrum from "white light" gives the emission spectrum, resolving the Berry–Keating mismatch; there is "a single 'quantum cell'" unaccounted for by the Berry–Keating cutoff; and the cutoff has a clean interpretation as the orthogonal projection `S` onto the **Sonin space** (functions vanishing with their Fourier transform on `[-1,1]`). The scaling action does not restrict to that subspace, but `Tr(ρ(f)S)` is positive definite by construction, since on `f = g*g*` it is `Tr(ρ(g)Sρ(g)*)`.
- Lead: "positive definite by construction" is exactly the mechanism the Weil-positivity lane wants (L11-105, L11-112). The Sonin projection is a concrete finite-rank-like object nobody in the notebook has used.
- Related: L11-105, L11-106, L11-112, L11-082.

### L11-084 fMPS: the supertrace and the ordinary trace differ by a parity insertion
- Source: `notes/extract/riemann-cmps-sources.md:387-512` (relevance note at :502-512)
- Raised by: a paper (Bultinck–Williamson–Haegeman–Verstraete, arXiv:1610.07849)
- Status at last mention: noted, not used
- Content: The graded contraction gives `C(|i⟩ ⊗_g ⟨j|) = (-1)^{|i|}δ_{ij}` — "the famous supertrace"; to obtain the *normal* trace one must insert the fermion parity operator. Even-parity fMPS on a ring have coefficients `tr(P A^{i_1}···A^{i_N})` with the parity matrix `P`; odd-parity ones need an extra odd tensor `Y`. These are the two simple `Z_2`-graded algebras (even type / odd type), with Majorana edge modes in the odd case; the Kitaev chain has `A^1 = Y`.
- Lead: "the fMPS shadow of the notebook's even/odd split" — pick one of the two algebras (even `P`, odd `Y`) as the bond structure of the Riemann cMPS and see which reproduces the Deninger grading.
- Related: L11-079, L11-085, L11-004.

### L11-085 The fermionic cMPS grading is **not new** — only its arithmetic reading would be
- Source: `notes/extract/riemann-cmps-sources.md:513-632` (the novelty verdict is at :625-632)
- Raised by: the extractor's commentary on Verstraete–Cirac (arXiv:1002.1824) and Haegeman–Cirac–Osborne–Verstraete (arXiv:1211.3935)
- Status at last mention: **novelty assessment, standing**
- Content: The cMPS transfer operator `T = Q⊗1 + 1⊗Q̄ + Σ R_α⊗R̄_α` is a Lindbladian after gauge fixing; its fixed point is the half-chain reduced density matrix (entanglement spectrum). The fermionic case is already in the literature with the **same** `Z_2`-graded bond structure: `P` diagonal, `Q` block diagonal, fermionic `R_α` block **off**-diagonal, `B` block-diagonal (even) or block-off-diagonal (odd), and `P T P = T`. The extractor concludes: "The notebook's 'graded bond with a supertrace in PBC' is therefore *not* new as a tensor-network construction; what is proposed as new is the arithmetic reading of it."
- Lead: stop claiming the construction and claim only the reading; and reuse the existing fermionic-cMPS calculus (it already has `l_α = lP`, `r_α = Pr` eigenvector relations) rather than rebuilding it.
- Related: L11-084, L11-079, L11-095.

### L11-086 The Weil representation justifies "the Artin–Schreier transfer matrix is a Clifford operator"
- Source: `notes/extract/riemann-cmps-sources.md:633-787` (relevance note at :781-787)
- Raised by: papers (Gurevich–Hadani arXiv:math/0610818; T. Thomas arXiv:math/0610644; D. Gross arXiv:quant-ph/0602001; Appleby arXiv:quant-ph/0412001)
- Status at last mention: noted, used as justification in the notebook's Weil-LPS lane
- Content: The Egorov relation `ρ(g)π(h)ρ(g)^{-1} = π(g·h)` determines `ρ(g)` up to a scalar; Thomas's character formula gives `Tr ρ(g) = |F|^{½dim ker(g-1)}γ(1)^{…}γ(det σ_g)`, hence `|Tr ρ(g)|² = |F|^{dim ker(g-1)}` — which is the point count; Gross and Appleby give the stabiliser/Clifford dictionary for odd prime dimension.
- Lead: Howe's remark (`math/0610644:…:202-203`) that the absolute value alone follows from `ρ ⊗ ρ*` being the natural action on `L²(V)` is a cheap route to the modulus without the full character formula — unexploited.
- Related: L11-061, L11-059, L11-075.

### L11-087 **Gap**: the Stickelberger statement the notebook actually wants is not in any arXiv TeX
- Source: `notes/extract/riemann-cmps-sources.md:788-850` (the gap is stated at :836-850)
- Raised by: the extractor's negative search
- Status at last mention: **flagged as a gap**; recorded as textbook-only
- Content: The wanted statement — `disc` of a degree-`n` separable extension is a square in the base field iff `Gal ⊆ A_n`, hence for `F_{q^n}/F_q` with `q` odd, `disc` is a square iff `n` is odd (the Frobenius `n`-cycle has sign `(-1)^{n-1}`) — "was **not found stated verbatim in any arXiv TeX source**". What arXiv does supply (Auel–Biesel–Voight arXiv:2208.06138) is the *other* Stickelberger theorem `disc Z_K ≡ 0,1 (mod 4)`, whose standard proof is exactly the even/odd permutation split `disc = (P-N)²`, with `P+N` the **permanent**.
- Lead: cite a textbook (Conrad; Jacobson; Dummit–Foote) or write the two-line proof. The `(P-N)²` / permanent structure is itself a bosonic/fermionic pair worth noting.
- Related: L11-088, L11-061.

### L11-088 Self-dual normal bases confirm the same `n`-odd parity independently
- Source: `notes/extract/riemann-cmps-sources.md:851-878` (relevance note at :872-878)
- Raised by: a paper (Arnault–Pickett–Vinatier, arXiv:1007.4899, quoting Lempel–Weinberger)
- Status at last mention: noted as independent confirmation
- Content: `F_{q^n}/F_q` has a self-dual normal basis iff `n` is odd, or `n ≡ 2 (mod 4)` and `q` is even. "This is the 'even-`n` sign' the Artin–Schreier section attributes to Stickelberger."
- Lead: two independent parity criteria agreeing is evidence the even-`n` sign is structural, not a normalisation artefact — worth stating as such.
- Related: L11-087, L11-061.

### L11-089 Lidskii forces the grading: no ungraded trace-class operator can do the job
- Source: `notes/extract/riemann-cmps-sources.md:879-939` (relevance note at :934-939)
- Raised by: the extractor's argument built on Reinov–Latif (arXiv:1105.2914) and Delgado–Ruzhansky (arXiv:1303.4792)
- Status at last mention: an argument assembled inside the extract; not written up in the notebook
- Content: If `X` is trace class then `Tr X^ℓ = Σ_j μ_j^ℓ` with algebraic multiplicities. But a genus `≥ 1` curve has `#X(F_{q^ℓ}) = q^ℓ + 1 - Σα_i^ℓ` with `2g` terms of modulus `q^{1/2}` entering **negatively**. Hence the trace sequence "cannot be realised without a grading."
- Lead: write this as a short no-go lemma. It is the cleanest available *proof* that the notebook's grading is forced rather than aesthetic.
- Related: L11-079, L11-084, L11-002.

### L11-090 Landau's theorem as the positivity-forces-a-singularity tool
- Source: `notes/extract/riemann-cmps-sources.md:940-958`
- Raised by: a paper (Maurizi, arXiv:1009.0228) + the textbook Widder reference
- Status at last mention: recorded; used implicitly
- Content: A Dirichlet series with non-negative coefficients and abscissa of absolute convergence `0` does not extend holomorphically to a neighbourhood of `s = 0`; equivalently for a positive measure's Laplace transform, the abscissa of convergence is a singularity.
- Lead: apply Landau to the notebook's unconditionally positive side-A series (L11-071) to pin the radius of convergence of `ζ_Φ` to a genuine singularity — a small but rigorous step.
- Related: L11-071, L11-112.

### L11-091 The Bost–Connes KMS classification, with a citation caveat
- Source: `notes/extract/riemann-cmps-sources.md:1018-1096` (caveat at :1089-1096)
- Raised by: papers (Bost–Connes 1995, not on arXiv; the theorem quoted from Connes–Marcolli arXiv:math/0404128)
- Status at last mention: cited; one honesty caveat recorded
- Content: Unique `KMS_β` state for `0 < β ≤ 1`; for `β > 1` extreme states parameterised by embeddings `Q^ab → C` with partition function `ζ(β)`; at `β = ∞` the Galois action factors through the abelianisation and class field theory intertwines. The dictionary table pairs "System at critical temperature (Riemann's `ζ` as partition function)" with "Spectral realization (Zeros of `ζ` as absorption spectrum)" and types `III_1` ↔ `II_∞`. **Caveat:** Connes–Marcolli label the system `III_1` in a table but do not prove or restate it there.
- Lead: the `III_1` ↔ `II_∞` type change across the critical temperature is a structural fact the notebook has not used; it is a precise statement of what "compressing to a co-invariant subspace" costs.
- Related: L11-057, L11-058, L11-082.

### L11-092 The three load-bearing quotes, pre-selected
- Source: `notes/extract/riemann-cmps-sources.md:1097-1107`
- Raised by: the extractor's own summary
- Status at last mention: an editorial decision recorded
- Content: If only three quotes are used for the graded reading they should be: Deninger's Lefschetz equation (`math/0505354:main.tex:878-879`), Connes's `⊖H` / absorption passage (`math/9811068:main.tex:575-581`), and the fMPS supertrace + parity-insertion equations (`1610.07849:FermionicMPS.tex:132`, `:136`).
- Lead: none mathematical; it fixes the citation spine for the report shard.
- Related: L11-079, L11-082, L11-084.

### L11-093 The cMPS fixed point **is** the entanglement spectrum
- Source: `notes/extract/riemann-cmps-sources.md:546-549` (quoting `1002.1824:mpsQFT4.tex:81`)
- Raised by: a paper (Verstraete–Cirac)
- Status at last mention: noted; connects to the notebook's erratum (L11-094)
- Content: With open boundary conditions the eigenvalues of `ρ(x)` are exactly the squares of the Schmidt coefficients at the bipartition — so the transfer fixed point computes the entanglement entropy of intervals.
- Lead: the notebook's `ξ = 2/h` statement (L11-077) ties correlation length to entropy rate; this gives the operator whose spectrum is the entropy side. Closing the loop between them is a concrete calculation.
- Related: L11-077, L11-085, L11-094.

### L11-094 Erratum: "entanglement Hamiltonian" was the wrong name
- Source: `notes/extract/notation-and-definitions.md:291` (`erratum-entanglement-hamiltonian`)
- Raised by: the notebook, correcting an earlier draft and the founding conversation
- Status at last mention: correction recorded
- Content: The entanglement Hamiltonian is `-log ρ_A` and is Hermitian by construction; the operator whose spectrum is supposed to contain the zeros is the **non-Hermitian transfer generator**. The two must not be conflated.
- Lead: none; a standing terminological guard.
- Related: L11-093, L11-085.

### L11-095 The sixteen notation ambiguities the orchestrator must decide
- Source: `notes/extract/notation-and-definitions.md:354-372`
- Raised by: the extractor's bookkeeping
- Status at last mention: open decisions, listed
- Content: Sixteen genuine clashes, several of which are mathematical rather than typographic: (1) channel normalisation `Φ` vs `DΦ` vs `Σ`; (2) Ramanujan units (`λ_2` of a channel vs `(q+1)λ_2` vs Hastings' `λ_H` vs `2√q`) — "WLP §2's table mixes both units in one row"; (3) `q` vs `D-1` — they coincide in the LPS story and not in general; (11) whether canonical form of an MPS is the spectral condition or `Σ_k A_k^†A_k = 1`; (12) which object "Riemann channel" denotes — "No note gives a one-sentence definition — one must be written"; (13) "Bost–Connes system" is never defined in the notes, only used.
- Lead: items (2), (3), (11), (12) are substantive and can change statements, not only symbols. Decide them before the report shard.
- Related: L11-077, L11-066, L11-071.

### L11-096 Guillemin's flat trace formula with the `tr(∧^k P_γ)` weight — the graded version
- Source: `notes/extract/selberg-sources.md:15-56`
- Raised by: a paper (Dyatlov–Zworski, arXiv:1306.4203), with the extractor's convention notes at :35-56
- Status at last mention: noted; conventions fixed for use
- Content: `tr^♭ e^{-itP}|_{C^∞(X;E^k_0)} = Σ_γ T_γ^# tr(∧^k P_γ) δ(t - T_γ)/|det(I - P_γ)|`. The extractor pins every convention: `P = -iV`, the sum runs over **all** orbits (repetitions included), `P_γ = dφ_{-T_γ}` uses **negative** time so `|μ| < 1` on `E_u`, and the flat trace is `∫_X (ι*K_B)(x)dx` with a wave-front condition.
- Lead: the `∧^k` weight is the continuous form of the notebook's grading; the conversion `t ↦ real time, X = V` is spelled out so the formula can be transplanted directly.
- Related: L11-004, L11-081, L11-097.

### L11-097 Ruelle resonances come in **bands** off the Laplace spectrum
- Source: `notes/extract/selberg-sources.md:60-87`
- Raised by: a paper (Dyatlov–Faure–Guillarmou, arXiv:1403.0256)
- Status at last mention: noted, not used
- Content: For a compact hyperbolic surface, the Pollicott–Ruelle resonances in `C \ (-1 - ½N_0)` are `λ_{j,m} = -m - 1 + s_j`, `m ∈ N_0` — one band per `m`, all translates of the Laplace spectrum. The authors use the **Laplace** transform rather than the Fourier transform to keep the relation to `s` simple.
- Lead: "one band per `m`" is a structure the notebook's channel spectrum has never been tested for. If a quantum transfer generator has band structure, the notion of "uniform decay" splits per band.
- Related: L11-098, L11-032, L11-036.

### L11-098 Two halves of one fact live in two different papers (caveat)
- Source: `notes/extract/selberg-sources.md:85-87`, `:296-306`
- Raised by: the extractor's caveat
- Status at last mention: recorded as a citation hazard
- Content: "F2's 'band structure' and F2's 'Ruelle zeta = `Z(s)/Z(s+1)`' come from **different** papers (1403.0256 and 1606.04560); 1403.0256 never mentions Selberg or Ruelle zeta." Verified: the string `zeta` does not occur in that source.
- Lead: none; a bookkeeping guard when the two are used in one sentence.
- Related: L11-097, L11-099.

### L11-099 `ζ_R(s) = ζ_S(s)/ζ_S(s+1)` — the shift-by-one relation
- Source: `notes/extract/selberg-sources.md:88-104`
- Raised by: a paper (Dyatlov–Zworski, arXiv:1606.04560, `:117-119`), attributed to Marklof
- Status at last mention: noted; conventions pinned
- Content: `ζ_S(s) = ∏_γ ∏_{m≥0}(1 - e^{-(m+s)ℓ_γ})`, `ζ_R(s) = ζ_S(s)/ζ_S(s+1)`. Both products over **primitive** lengths, `m` the band index; note the `e^{-sℓ}` normalisation here versus `e^{iλT}` in arXiv:1306.4203.
- Lead: the ratio-of-shifts structure is the continuous analogue of the notebook's `μμ' = q` pairing; the shift `s → s+1` is what the notebook's grading would have to produce.
- Related: L11-097, L11-066.

### L11-100 The Poisson relation is only an **inclusion** — cancellations can occur
- Source: `notes/extract/selberg-sources.md:135-159` (the caveat is at :155-159)
- Raised by: a paper (Zelditch, arXiv:math/0402356, `:1480-1482`)
- Status at last mention: recorded as a caveat
- Content: `Sing Supp Tr U(t) ⊂ Lsp(M,g)` is known only as a containment; "cancellations could take place if a length `L` is multiple". For a compact hyperbolic surface the Selberg trace formula upgrades it to an equality, with `√Δ` replaced by `√(Δ - 1/4)`; the `-1/4` shift is **not** present in the general source.
- Lead: a warning for any "lengths = spectrum" claim in the notebook: the correspondence is an inclusion in general, and the `-1/4` shift is special to hyperbolic geometry. This is the same `-1/4` vs `-3/4` centring issue recorded in the Selberg-letters lane.
- Related: L11-102, L11-103.

### L11-101 The Laplacian sign conventions clash across the sources (hazard)
- Source: `notes/extract/selberg-sources.md:161-222` (the flagged line is :219-222)
- Raised by: the extractor's convention audit
- Status at last mention: recorded as a hazard
- Content: FGKP use `Δ f_s = s(s-1) f_s`, i.e. the *negative* Laplacian, "**the analyst-unfriendly one**"; DFG use `Spec(Δ) = {s_j(1-s_j)}`; Marklof uses `λ_j = ρ_j² + ¼ ≥ 0`. All three appear in the same lane.
- Lead: fix one sign convention for the lab book before any Selberg computation. Consequence if ignored: an off-by-a-sign in the centring of the transfer spectrum.
- Related: L11-095, L11-100.

### L11-102 The scattering determinant of `PSL(2,Z)` and `φ(1/2) = -1`
- Source: `notes/extract/selberg-sources.md:223-252`
- Raised by: papers (Friedman–Jorgenson–Smajlović arXiv:1607.08053; FGKP arXiv:1511.04265)
- Status at last mention: noted; a source of the modular-surface machinery
- Content: `φ(s) = √π Γ(s-½)/Γ(s) · ζ(2s-1)/ζ(2s)`, normalised by `φ(s)φ(1-s) = 1`, with `φ(½) = -1`; it **is** the `y^{1-s}` coefficient of the Eisenstein constant term, `ξ(2s-1)/ξ(2s)`.
- Lead: `φ(½) = -1` is a sign at the central point — precisely the kind of `-1` the notebook's grading is trying to explain. Worth checking whether it is the same sign.
- Related: L11-103, L11-100, L11-083.

### L11-103 The continuous-spectrum term and its central correction `K_0 h(¼)/4`
- Source: `notes/extract/selberg-sources.md:253-294`
- Raised by: papers (Momeni–Venkov arXiv:1108.5659; Booker–Platt arXiv:1710.00603)
- Status at last mention: noted, not used
- Content: `C = -(1/4π)∫ (φ'/φ)(½+ir) h(r²+¼) dr + (K_0/4)h(¼)` with `K_0 = tr Φ(½)`, sitting on the **spectral** side. In the cocompact case `φ ≡ 1` and `C` disappears. Booker–Platt give the fully explicit `PSL(2,Z)` version in an arithmetic normalisation where the `φ'/φ` integral is already folded into a `Λ(n)/n` sum.
- Lead: the fold of `φ'/φ` into a `Λ(n)/n` sum is exactly the prime side reappearing inside the spectral term — a structural hint for the notebook's cusp/environment story that was never pursued.
- Related: L11-102, L11-057, L11-091.

### L11-104 The Casimir → `y²(∂_x² + ∂_y²)` reduction is assembled, not stated
- Source: `notes/extract/selberg-sources.md:302-306`
- Raised by: the extractor's caveat
- Status at last mention: recorded as a gap in the byte-citable record
- Content: "F4's 'on right-`K`-invariant functions the Casimir equals `y²(∂_x² + ∂_y²)`' is assembled from two equations in 1511.04265 plus its `∂_θ = e - f`; the book does not state the one-line reduction as a displayed sentence." The standard single-display reference is Bump, *Automorphic Forms and Representations*, §2.2 (not on arXiv).
- Lead: either derive the one line in the lab book or acquire Bump §2.2.
- Related: L11-101.

### L11-105 Connes's Theorem 5: the trace formula **is** RH, via positivity of the Weil distribution
- Source: `notes/extract/weil-positivity-sources.md:30-116`
- Raised by: a paper (Connes, arXiv:math/9811068) + convention notes at :100-116
- Status at last mention: noted; the anchor of the whole lane
- Content: The asymptotic trace formula for `Trace(Q_Λ U(h))` is equivalent to RH for all `L`-functions with Grössencharakter; the mechanism is that `Δ_Λ(f * f*) ≥ 0`, i.e. the distribution is of positive type on the idele class group. The trivial contributions are the two separate terms `ĥ(0) + ĥ(1)` — "the analogue of the notebook's 'trivial eigenvalues removed'". Connes's *equivalence* is in positive characteristic; the characteristic-zero case is conjectural.
- Lead: the notebook's finite-dimensional statement is the shadow: `ν_ℓ = r^{-ℓ}(Tr X^ℓ - trivial)` positive-definite iff all nontrivial `|μ| ≤ r`. Prove that shadow cleanly.
- Related: L11-106, L11-112, L11-071, L11-083.

### L11-106 The Weil criterion in its cleanest form, with the `g^♯` involution
- Source: `notes/extract/weil-positivity-sources.md:117-181` (convention notes at :168-181)
- Raised by: a paper (Connes–Consani, arXiv:2006.13771)
- Status at last mention: noted; the citable form
- Content: `RH ⟺ Σ_v W_v(g * ḡ^♯) ≤ 0` for all `g ∈ C_c^∞(R_+^*)` with `g̃` vanishing on a finite set `F ⊇ {0,1}` disjoint from the zeros, where `g^♯(x) = x^{-1}g(x^{-1})`. **Sign caveat recorded:** they write `≤ 0` because the explicit formula puts zeros and places on opposite sides; the notebook's `≥ 0` is the spectral side. **Also:** the product identity `f̃(ρ) = g̃(ρ) conj g̃(1 - conj ρ)` is *not* displayed in this source — cite Lagarias (L11-107) for it.
- Lead: adopt one sign convention and state which side the notebook's positivity lives on.
- Related: L11-105, L11-107, L11-095.

### L11-107 The Weil scalar product, and the gap the notebook must close to say "iff"
- Source: `notes/extract/weil-positivity-sources.md:182-322` (the gap is at :310-322)
- Raised by: a paper (Lagarias, arXiv:math/0404394) + the extractor's commentary
- Status at last mention: **flagged as a gap the notebook shares**
- Content: `⟨F,G⟩_{W(π)} := Σ_{ρ∈Z(π)} F(ρ) conj G(1-conj ρ)`; RH ⇒ psd because `ρ = 1 - conj ρ` iff `Re ρ = ½`. Li's coefficients are a specialisation, and `⟨G_n,G_m⟩ = λ_n + λ_{-m} - λ_{n-m}` — so the `λ_n` are **not the diagonal** of the form but a combination of Gram entries. Critically: "One direction is elementary (RH ⇒ psd); the converse needs a test-function class rich enough to separate the zeros — the source says so explicitly. **This is the same gap the notebook must close when it asserts 'iff'.**"
- Lead: identify the test-function class (or, finite-dimensionally, the richness condition on `ν_ℓ`) that makes the converse work. This is the single most concrete open technical step in the lane.
- Related: L11-105, L11-112, L11-113.

### L11-108 Li's criterion, two independent statements, with file hazards
- Source: `notes/extract/weil-positivity-sources.md:323-380`
- Raised by: papers (Voros arXiv:math/0506326; Coffey arXiv:math-ph/0505052)
- Status at last mention: recorded; two operational caveats
- Content: `λ_n = Σ_ρ [1 - (1-1/ρ)^n]`, RH iff all `λ_n > 0`; Coffey's equivalent derivative form at `s = 1`. Caveats: Voros's file is latin-1 and GNU grep exits 1 on it without matching; Coffey's main LaTeX file is named `lambda2.txt`, not `*.tex`. Voros credits Keiper, whose results "were almost never cited".
- Lead: none mathematical; Keiper's essentially uncited prior work is a small unread thread.
- Related: L11-107, L11-112.

### L11-109 **The prior art**: Huang's Li-criterion for Ramanujan graphs
- Source: `notes/extract/weil-positivity-sources.md:381-517`
- Raised by: a paper (Huang, arXiv:1905.13485); the extract calls it "**the prior art**"
- Status at last mention: prior art that must be cited; overlap analysed
- Content: With `Ξ(u)` the Ihara zeta cleared of trivial poles and `d/du ln Ξ(q^{-1/2}u) = Σ_k h_{k+1}u^k`, Huang proves: `X` Ramanujan ⟺ `h_k ≥ 0` for all `k ≥ 1` ⟺ `h_k ≥ 0` for infinitely many even `k`. And `h_k = 2(n-1) + q^{k/2} + q^{-k/2} - q^{-k/2}N_k` (nonbipartite, odd `k`) — "precisely '`q^{-k/2}` times (cycle count minus trivial part)'".
- Lead: read before claiming novelty; the "infinitely many even `k`" clause is a striking strengthening nobody in the notebook has used.
- Related: L11-110, L11-112, L11-113.

### L11-110 The overlap with Huang is real but **not total** — termwise vs Toeplitz
- Source: `notes/extract/weil-positivity-sources.md:496-517` (the key passage at :500-513)
- Raised by: the extractor's commentary
- Status at last mention: **flagged: "the two results have to be reconciled, not identified"**
- Content: Huang proves *termwise* nonnegativity of one sequence; the notebook claims *positive-definiteness in the Herglotz/Toeplitz sense* (every Toeplitz minor `≥ 0`). "These are *different* conditions on a sequence — neither implies the other in general." Huang's file has **zero** hits for "Herglotz", "Bochner", "Toeplitz", "positive definite", "positive semidefinite". Also, Huang's `h_k` carries a `2(n-1)` constant the notebook's normalisation does not.
- Lead: do the reconciliation explicitly — state both conditions on the same sequence and prove or disprove either implication. Consequence: it determines whether the notebook has a new theorem or a repackaging.
- Related: L11-109, L11-112, L11-113.

### L11-111 Do **not** cite `λ_H` as a proved bound
- Source: `notes/extract/weil-positivity-sources.md:518-550` (the caveat at :546-550)
- Raised by: the extractor's reading of Hastings (arXiv:0706.0556)
- Status at last mention: recorded as a citation hazard
- Content: Hastings shows `|λ_2| → λ_H = 2√(D-1)/D` **in probability** for random unitaries as `N → ∞`; the rigorous bound actually proved is the weaker `λ_loose(D) = √λ_H`. "Do not cite `λ_H` as a proved bound."
- Lead: none; guard for every place the notebook writes the Ramanujan-channel threshold.
- Related: L11-025, L11-067, L11-095.

### L11-112 Herglotz/Toeplitz gives `r(n) = C* U^n C` — literally a trace of a power of a unitary
- Source: `notes/extract/weil-positivity-sources.md:551-625` (the useful remark at :615-620)
- Raised by: a paper (Alpay–Colombo–Kimsey–Sabadini, arXiv:1403.0079) recalling the classical case
- Status at last mention: noted; one remark singled out as useful
- Content: A sequence is positive definite iff every block Toeplitz matrix `T_N ⪰ 0` iff it is the moment sequence of a positive measure on `[0,2π]`. Positivity forces `r(-n) = r(n)*`, "so the notebook's `ν_{-ℓ} = conj(ν_ℓ)` is not an extra assumption but a consequence". And the representation `r(n) = C* U^n C` with `U` unitary is "literally 'trace of a power of a unitary', the `|μ| = r` case of the notebook's `Tr X^ℓ`".
- Lead: use the `C* U^n C` representation as the *construction* of the unitary the notebook wants — Herglotz hands it over for free once positive-definiteness is established. This is the most direct available route from positivity to a Hilbert–Pólya-like operator.
- Related: L11-105, L11-107, L11-110, L11-113.

### L11-113 Suzuki's screw function — prior art on the continuous side
- Source: `notes/extract/weil-positivity-sources.md:706-834` (the overlap analysis at :818-834)
- Raised by: a paper (Suzuki, arXiv:2206.03682); the extract calls it "**prior art on the continuous side**"
- Status at last mention: prior art that must be cited; the notebook's contribution "has to be located against this section and against W6"
- Content: RH ⟺ the Hermitian form built from the kernel `G_g(t,u) = g(t-u) - g(t) - g(-u) + g(0)` is non-negative definite, for every `0 < a < ∞`; the Nevanlinna/Pick/**Herglotz** class is named as the associated function class; Weil positivity appears as `W(ψ * ψ̃) ≥ 0`; Li's criterion is derived as a **special case** obtained by testing against triangular functions. What Suzuki does **not** do: arbitrary finite-dimensional transfer operators, the Toeplitz-sequence (discrete) form, graphs, or Ramanujan.
- Lead: the honest claim left for the notebook is the transcription to a discrete/operator setting. Also unexploited: "Li = Weil tested against triangular functions" gives a recipe for generating new criteria by choosing other test functions.
- Related: L11-107, L11-109, L11-110, L11-112.

### L11-114 **Not found**: any Herglotz/Toeplitz criterion for the Ramanujan property, or for a Kraus channel
- Source: `notes/extract/weil-positivity-sources.md:835-887` (items 4 and 5 at :858-876)
- Raised by: the extractor's negative arXiv full-text searches
- Status at last mention: **flagged as the lane's novelty claim**
- Content: `all:"Ramanujan graph" AND all:"positive definite"` → 0 entries; `all:"Ihara zeta" AND all:"positive definite"` → exactly one, unrelated (arXiv:1908.06563, "Energized simplicial complexes"). No paper states the criterion for an arbitrary transfer operator / Kraus channel — "the notebook's actual theorem". The nearest ingredients are Huang (regular graphs) and Hastings (quantum expanders, a bound not a criterion).
- Lead: this is the notebook's clearest unoccupied territory in this lane. Prove it, with L11-107's converse gap closed and L11-110's reconciliation done.
- Related: L11-107, L11-109, L11-110, L11-067.

### L11-115 Bender–Brody–Müller's PT proposal — and how to read it backwards
- Source: `notes/extract/weil-positivity-sources.md:652-705` (the caveat at :696-705)
- Raised by: a paper (arXiv:1608.03679) + the extractor's caveat
- Status at last mention: recorded as a proposal, not a theorem
- Content: `PT` here is the **modified** reflection `(x,p) → (x,-p)`, so `iĤ` is PT symmetric, not `Ĥ`; real spectrum of `Ĥ` requires **maximally broken** PT of `iĤ` — "the opposite of the usual 'unbroken PT ⇒ real spectrum' slogan, and easy to quote backwards". The paper assumes self-adjointness it does not prove.
- Lead: PT symmetry is a *weakened Hermiticity* — the same slot L11-037's "almost-normal" and L11-069's "positivity plus a multiplying operation" occupy. Worth listing all three as candidate substitutes for Hilbert–Pólya self-adjointness.
- Related: L11-037, L11-069, L11-077.

### L11-116 Bochner's theorem, with the distributional upgrade available
- Source: `notes/extract/weil-positivity-sources.md:626-651`
- Raised by: a paper (Norvidas, arXiv:2009.02802)
- Status at last mention: recorded; may be demoted to a `stipulated` assumption
- Content: A continuous `f` on `R` is positive definite iff it is the Fourier transform of a finite non-negative measure, with the convention `f(x) = ∫e^{-ixt}dμ(t)`. The Bochner–Schwartz distributional version (`F ∈ D'(R)` positive definite iff `F̂` is a non-negative tempered measure) is available in the same source if the continuous version is insufficient.
- Lead: the notebook's continuous-time (`Z(t)`) statements will need the distributional version, since the zero sum is a distribution not a function; that upgrade is available and unused.
- Related: L11-112, L11-105.

### L11-117 Horton–Stark–Terras and the graph explicit formula are named but unquoted
- Source: `notes/extract/weil-positivity-sources.md:848-857`
- Raised by: the extractor's not-found list
- Status at last mention: named, not quoted — never obtained
- Content: "What are zeta functions of graphs and what are they good for?" (Contemp. Math. 415 (2006) 173–190) and Stark–Terras (Adv. Math. 121 (1996), 154 (2000)) are journal-only; an arXiv API query `au:Terras_A AND cat:math.NT` returns no entries. Terras's book *Zeta Functions of Graphs: A Stroll through the Garden* (CUP 2010) is the reference for the **graph explicit formula**.
- Lead: obtain the graph explicit formula. The notebook's whole side-A/side-B framing is a statement about an explicit formula, and the graph version — the one case where it is elementary — has never been written into the notebook.
- Related: L11-109, L11-071, L11-105.

### L11-118 An arXiv identifier misattribution, corrected and recorded
- Source: `notes/extract/weil-positivity-sources.md:10-16`, `:877-880`
- Raised by: the extractor's bookkeeping
- Status at last mention: corrected; the wrong source deleted from `refs/src/`
- Content: `math-ph/0404030`, the identifier guessed for Voros in the task brief, serves an unrelated paper on `k`-decomposability of positive maps. It was fetched, identified as wrong, deleted, and removed from the `IDS` list; the Voros paper is `math/0506326`. Also recorded: Voros's earlier note `math/0404213` was **not** fetched, since `math/0506326` is its successor.
- Lead: none; a provenance-hygiene record.
- Related: L11-108.

---

## Small but possibly consequential

1. **L11-037 — geodesic walks form an *almost-normal* digraph family.** A named weakened-Hermiticity condition, mentioned once in a survey aside, sitting in exactly the slot where the notebook needs a substitute for Hilbert–Pólya self-adjointness.
2. **L11-034 — `χ` vanishes at `q = 1`.** A one-line aside; it says the torsion factor is a `q ≠ 1` artefact and hands the notebook a free degeneration limit ("field with one element") it has never taken.
3. **L11-112 — Herglotz gives `r(n) = C* U^n C`.** Flagged as "useful" in half a sentence; it is a *constructive* route from positive-definiteness to an actual unitary, i.e. the missing operator, for free.
4. **L11-083 — the Sonin projection and `Tr(ρ(f)S)` positive by construction.** Buried in one long quoted line of Connes–Consani; a concrete positive functional the notebook's Weil lane never tried.
5. **L11-017 — `γ_5`-hermiticity and overlap fermions on a graph.** One clause in Matsuura–Ohta (`:192`); overlap-fermion technology has never been applied to a zeta and would give an exact chiral symmetry on the discrete side.
6. **L11-103 — `φ'/φ` folds into a `Λ(n)/n` sum in the arithmetic normalisation.** Recorded as a "use only if you want it" footnote; it is the prime side literally reappearing inside the continuous spectral term.
7. **L11-046 — the exponent is `χ − 1`, not `χ`, in Deitmar–Kang.** A parenthetical note; an off-by-one that would break any universal supertrace bookkeeping if it is real.
8. **L11-109's "infinitely many even `k`" clause.** Huang needs `h_k ≥ 0` for only *infinitely many even* `k`, not all `k` — a very weak hypothesis that the notebook has never exploited and that might be far easier to verify for a channel.

---

## Dead routes recorded

- **Prime-by-prime ansätze (direct sums of circle rotations, commuting dilations) cannot see the zeros** — the spectrum of a finite direct sum is just the poles of the partial Euler product, i.e. pure side A. `notes/extract/notation-and-definitions.md:349`.
- **The Deligne "multiply" step has nothing to act on for `ζ`**: there is no `X × X` with `ζ` as its slice. `notes/extract/notation-and-definitions.md:330`.
- **Deligne's purity step 3 is false for graphs**, by the explicit bouquet counterexample with eigenvalue `(3+√5)/2 > 1` despite real traces, an alternating pairing and big monodromy. `notes/extract/notation-and-definitions.md:322`.
- **Cubic and higher Artin–Schreier traces are non-local in the shift basis**, so no fixed local MPS tensor exists there — "the dividing line is therefore sharp". `notes/extract/notation-and-definitions.md:313`.
- **Dwork's transfer operator cannot give RH**: it sees `p`-adic sizes (Newton polygon), not complex absolute values. `notes/extract/notation-and-definitions.md:314`.
- **Kraus structure alone will not force degeneracy of the decay rates** — the graph lesson; "some arithmetic rigidity has to enter". `notes/extract/notation-and-definitions.md:290`.
- **The `L²`/Fuglede–Kadison route to a zeta formula is blocked**: "there is no direct relationship between the `L²`-torsion of a matrix and its entries" (Zhuang). `notes/extract/cohomological-zeta-sources.md:753-757`.
- **A single cohomological degree is never a topological invariant** — only the alternating combination over all degrees is (analytic torsion / `L²`-torsion). `notes/extract/cohomological-zeta-sources.md:846-851`.
- **The plain (unweighted) alternating Euler characteristic vanishes identically** in Deitmar's setting, so a naive supertrace count is empty; only the degree-weighted `χ_1` carries the divisor. `notes/extract/cohomological-zeta-sources.md:143-146`.
- **"The zeros are the odd cohomology" is not perturbation-stable**: in dimension 3 the alternating count jumps from `4-2b_1` to `4-b_1` under a generic conformal perturbation. `notes/extract/cohomological-zeta-sources.md:481-492`.
- **No Ihara-type zeta with a Bass identity and an RH ⇔ Ramanujan theorem exists for a general finite simplicial or cell complex** — six search phrasings, all negative; only building quotients, hypergraph reductions, graph refinements, and the torsion-type combinatorial Ruelle zeta come back. `notes/extract/complex-zeta-sources.md:1462-1480`.
- **The hypergraph zeta is not a new object**: `ζ_H(u) = Z_{B_H}(√u)`, the Ihara zeta of the incidence bipartite graph, blind to simplicial structure beyond incidence. `notes/extract/complex-zeta-sources.md:840-858`.
- **The combinatorial Ruelle zeta of a triangulation has no Ramanujan notion and no RH** — its distinguished point `(n+2)^{-1}` is not `q^{-1/2}` and there is no spectral-gap statement. `notes/extract/complex-zeta-sources.md:1097-1102`.
- **Quantum walks on simplicial complexes carry no zeta** (verified: `grep -c -i zeta … → 0`), and **"Ramanujan quantum expander" papers carry no zeta, no Ihara, no simplicial structure** (verified the same way). `notes/extract/cohomological-zeta-sources.md:1715-1724`, `:1755-1762`.
- **First's Ramanujan-property paper has no zeta**: its eight `zeta` hits are all the Greek letter used as a variable. `notes/extract/cohomological-zeta-sources.md:1824-1829`.
- **Kang–Yu 2026, the most general Ihara-type identity, contains no RH or Ramanujan theorem** (grep-verified). `notes/extract/complex-zeta-sources.md:450-456`.
- **Bartholdi zeta of a simplicial complex does not exist** — the generalisation is available for graphs and hypergraphs only. `notes/extract/complex-zeta-sources.md:1482-1485`.
- **The fermionic-cMPS graded bond structure is not a novel construction** — it is already in Haegeman–Cirac–Osborne–Verstraete; only the arithmetic reading could be new. `notes/extract/riemann-cmps-sources.md:625-632`.
- **Do not cite `λ_H = 2√(D-1)/D` as a proved bound** — Hastings proves only the weaker `√λ_H` rigorously; `λ_H` is an in-probability asymptotic. `notes/extract/weil-positivity-sources.md:546-550`.
- **Termwise nonnegativity (Huang) and Herglotz/Toeplitz positive-definiteness are different conditions**; neither implies the other in general, so the two results "have to be reconciled, not identified". `notes/extract/weil-positivity-sources.md:500-513`.
- **`math-ph/0404030` is not Voros** — it serves an unrelated paper on `k`-decomposability of positive maps; fetched, identified as wrong, deleted. `notes/extract/weil-positivity-sources.md:10-16`, `:877-880`.
