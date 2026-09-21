# Lane L15: codex rollouts of 2026-09-13 and 2026-09-14 morning (drafts and messages not in the final files)

Scope: four extracted codex transcripts held outside the repo. For each I identified the
final repo file(s) the session wrote, reconstructed every `cat > ... <<` heredoc and
`apply_patch` body from the transcript, and compared the reconstructed drafts line by line
against the committed file. Items below are what the transcripts contain and the final
files do **not**, plus the orchestrator's drafted guesses that were declined, corrected or
never reached. Content already present in the final files (including their own correction
ledgers) is deliberately not repeated here.

Short names used below:
- **A** = `2026-09-13T10-23-10.txt` (simplicial-complex zeta campaign + its resume turn)
- **B** = `2026-09-13T12-11-30.txt` (open-ended session: BC generator cones, then the graded cMPS question)
- **C** = `2026-09-13T13-43-15.txt` (gpt-5.6-luna subagent, `fmd` install)
- **D** = `2026-09-14T11-00-06.txt` (ring-norm-tensor prover)

## Coverage

| transcript | lines | read fully? | final repo file | items found |
|---|---|---|---|---|
| A `2026-09-13T10-23-10.txt` | 242 | yes (all `### ` blocks; the 5 heredoc file-writes reconstructed and diffed against the committed file) | `notes/complex-zeta/astra-proofs.md` (1152 lines) | 7. Drafts are append-only and match the final file essentially line for line (only transcript truncation at the 20 000-character line limit accounts for apparent gaps), so the yield is brief-level: source leads handed to the prover and never used, one declined characterisation, one test complex asked for and not delivered, one complex computed and not reported. |
| B `2026-09-13T12-11-30.txt` | 1070 | yes | `notes/bc-symmetry-generators.md` (336 lines), `scripts/bc_symmetry_generators.py`, shards 02e/04d, and `outputs/ramanujan-boson-fermion-cmps.md` (162 lines) | 10. Richest transcript: two long research messages (the "next most consequential step" answer and the boson–fermion cMPS Ramanujan answer) plus two in-flight assertion checks that were deleted or weakened. |
| C `2026-09-13T13-43-15.txt` | 262 | yes | none (tooling only) | 0 research items. Evidence: every `### ASSISTANT`/`### EXEC` block concerns downloading, checksumming and installing the FrankenMarkdown binary (`curl` of `fmd-v0.4.3`/`v0.4.2` release tarballs, `sha256sum -c`, `install -m 0755 ... ~/.local/bin/fmd`, `fmd capabilities --json`, a math smoke test). The only durable finding is the environment note already in memory: fmd 0.4.2 at `~/.local/bin/fmd`, native PDF prints raw LaTeX, so HTML + headless Chromium is the math-preserving route (C:203, C:236). |
| D `2026-09-14T11-00-06.txt` | 470 | yes (all 6 `apply_patch` bodies reconstructed and diffed) | `notes/ring-norm-tensor/astra-proofs.md` (1184 lines), `notes/ring-norm-tensor/scratch/{t04_cutrank.py,t43_check.py,t45a_certificate.py}` | 6. Yield is the two abandoned genus-2 ansätze, the intermediate state in which the F_5 three-species statement was *open* (later closed by a certificate found in the audit pass), and the reusable certificate method. |

## Ideas and leads

### L15-001 "Links are generalised polygons" as the criterion for vertex-level Bass collapse
- Source: A:85 (orchestrator brief, task T2(i)); the refusal is visible in the final file at `notes/complex-zeta/astra-proofs.md:330` and `:346`.
- Raised by: orchestrator brief
- Status at last mention: raised, not pursued (prover declined to prove or use it)
- Content: The brief guessed that a degree-$(d+1)$ vertex-level determinant identity $\det(1-uT_1)\det(1+uT_2)^{-1} = (1-u^3)^{\chi}\det P(u)^{-1}$ holds exactly for complexes "whose vertex links are all generalised polygons / incidence graphs of the same parameters, i.e. locally building-like", and asked for a proof for that class by the Schur-complement method. The prover proved the universal Schur identity and the building case, but wrote that "Equality of numerical link parameters, or the phrase 'links are generalized polygons', is not a proved characterization of that class or of cubic collapse", and left it out of the theorem list.
- Lead: characterise exactly which finite 2-complexes admit a vertex-level (degree $d+1$) Bass polynomial with locally-determined $Q_1,Q_2$. Concretely: take the smallest non-building complexes whose links are all the same generalised polygon (e.g. incidence graphs of small projective planes glued into a 2-complex) and test numerically whether the Schur complement collapses to the vertex level. A clean "iff" here would tell you whether the numerator/denominator split of the zeta is a building phenomenon or a local-geometry phenomenon — directly relevant to whether the Phantasm needs a building at all.
- Related: L15-002.

### L15-002 The 7-vertex triangulated torus and the cone as the non-building test complexes
- Source: A:85 and A:95 (brief, tasks T2(ii) and T7); absent from `notes/complex-zeta/astra-proofs.md` (grep for "torus" and "cone" both return 0).
- Raised by: orchestrator brief
- Status at last mention: raised, not pursued
- Content: The brief twice asked for a triangulated torus (Möbius–Kantor style 7-vertex triangulation) or a cone as the smallest 2-complex where the vertex-level identity should fail, and asked for the predicted polynomial for a numerics lane. The prover instead used the boundary of the tetrahedron (4 vertices, $f=(4,6,4)$, $\chi=2$, $\det(I-uT_1)=1$, $\det(I+uT_2)=(1-u^4)^6$) as its counterexample and gave three test rows: $C_3$, filled $\Delta^2$, $\partial\Delta^3$.
- Lead: run the ordered-cell flow on the 7-vertex torus. It is the smallest complex with $\chi=0$, $b_1=2$ and no free faces, so it is the one case that can separate "the trivial factor is $(1-u^{d+1})^{\chi}$" from "the vanishing order is a Betti number" (see L15-005). If the order at $u=1$ turns out to be $b_1$ rather than $\chi$, the whole "which Euler characteristic" question of T1/T3 changes answer.
- Related: L15-003, L15-005.

### L15-003 The octahedral 2-sphere was computed twice and never reported
- Source: A:147 and A:164 (two inline `timeout 60 python3` sympy runs, both include `('octahedron', list(it.product((0,1),(2,3),(4,5))))` / `('octahedral sphere', ...)` in the test list); only the word "octahedral" survives once in the final file, with no determinants.
- Raised by: codex prover
- Status at last mention: cut from final
- Content: The prover's own sanity script computed the signed ordered-cell determinants $\det(I-(-1)^{k+1}uT_k)$ and the total graded zeta for four complexes: $C_3$, the filled triangle, $\partial\Delta^3$ and the octahedron (6 vertices, $f=(6,12,8)$, $\chi=2$). Three of the four became the published test table; the octahedron's numbers were never written down. Tool outputs are not in the transcript, so the values are lost.
- Lead: recompute the octahedral sphere. It is a second 4-valent triangulated $S^2$ with the same $\chi=2$ as $\partial\Delta^3$ but different link structure, so it is the cheapest check of whether the exponent of the trivial factor is a function of $\chi$ alone or of the $f$-vector. Cost: seconds.
- Related: L15-002.

### L15-004 Storm's bipartite-incidence route to a complex zeta was supplied and never used
- Source: A:72 (brief context, fact C6: "the hypergraph zeta is the Ihara zeta of the incidence bipartite graph at $\sqrt u$"); absent from `notes/complex-zeta/astra-proofs.md` (grep "Storm", "hypergraph", "bipartite" all return 0).
- Raised by: orchestrator brief
- Status at last mention: raised, not pursued
- Content: One of the ten literature facts handed to the prover says that for a hypergraph the "right" zeta is not a new object at all: it is the ordinary Ihara–Hashimoto zeta of the vertex/edge incidence bipartite graph, evaluated at $\sqrt u$. The prover never cited or tested this. It is a genuine competitor to the whole ordered-cell construction: it says a complex's zeta might be a *graph* zeta of the face poset's Hasse/incidence graph with a square-root change of variable, which would automatically inherit Bass, the Kraus twist of `notes/quantum-ihara-general.md`, and the positivity.
- Lead: for the three test complexes of T7 (and the tetrahedron boundary), compute the Ihara zeta of the vertex–edge–face incidence bipartite (or tripartite) graph at $u^{1/2}$ or $u^{1/3}$ and compare with the ordered graded determinant. If they agree, the "quantum zeta of a complex" reduces to the already-proved quantum Ihara–Bass theorem and the whole campaign simplifies; if they disagree, you learn exactly which cells the square-root trick loses.
- Related: L15-001.

### L15-005 The Benard–Chaubet–Dang–Schick signed manifold zeta (order $b_1$ at $z=(n+2)^{-1}$) was supplied and not used
- Source: A:72 (brief context, fact C8); the final file mentions $b_1$ once only, at `notes/complex-zeta/astra-proofs.md:462`, to note that $\partial\Delta^3$ has order 6 at $u=1$ although $\chi=2$ and $b_1=0$.
- Raised by: orchestrator brief
- Status at last mention: raised, not pursued
- Content: C8 says that for a triangulated closed $n$-manifold the **signed** zeta $\prod_\gamma(1-\epsilon_\gamma z^{|\gamma|})$, over primitive geodesics in the $(n-1)$-skeleton with a sign $\epsilon_\gamma$ attached to each orbit, is a polynomial vanishing to order $b_1$ at $z=(n+2)^{-1}$. That is a genuinely different construction from the prover's: the signs live on individual closed geodesics, not on the cell dimension. The prover's own $\partial\Delta^3$ number (order 6 at $u=1$, $b_1=0$) shows the ordered default is *not* this object.
- Lead: implement the $\epsilon_\gamma$-signed geodesic zeta on $\partial\Delta^3$ and on a triangulated torus and check the order-$b_1$ statement; then ask whether $\epsilon_\gamma$ can be written as a supertrace of a transport around $\gamma$, i.e. whether the per-orbit sign is the $\mathbb Z_2$ holonomy of a flat line bundle. If it is, the notebook's "grading forces a numerator" no-go acquires a second, orbit-level realisation, and a Betti number (not $\chi$) becomes the vanishing order — which is what the "surface-like qualities" framing actually wants.
- Related: L15-002, L15-006.

### L15-006 Foata–Zeilberger and Aizenman–Warzel: the fermionic loop ensemble, handed over and never cited
- Source: A:73 (brief context, facts D2 and D4); absent from `notes/complex-zeta/astra-proofs.md` (grep "Foata" and "Aizenman" both return 0).
- Raised by: orchestrator brief
- Status at last mention: raised, not pursued
- Content: D2 records that the graph trivial factor $(1-u^2)^{c_1-c_0}$ arises as $\det(1-uJ)$ with $J$ the edge-reversal involution — i.e. the trivial factor is the determinant of an involution, not a combinatorial count. D4 quotes Aizenman–Warzel that "the loop ensemble has a fermionic nature". Neither was used; the prover derived the trivial factor from cochain torsion instead.
- Lead: for complexes, ask what plays the role of $J$. The candidate is the cyclic rotation $C_k$ that the prover already isolated in $F_k = C_k + R_{k+1}S_{k+1}$ (it is an order-$(k+1)$ operator, not an involution), so the trivial factor should be $\det(1-uC_k)$-like and its exponent should be a count of rotation orbits. If that identification works, the $(1-u^{d+1})^\chi$ factor becomes a statement about a $\mathbb Z_{d+1}$ action rather than about torsion, which is a much more elementary route to T1.
- Related: L15-005.

### L15-007 The priority claim: no channel/Kraus zeta of a complex exists in the literature
- Source: A:73 (brief context, fact F2: "no quantum (channel / Kraus / unitary-weighted) zeta of a complex exists in the literature").
- Raised by: orchestrator brief
- Status at last mention: stated in a message only (as a context fact, never restated as a claim)
- Content: The brief asserts, as a result of the literature sweep, that the quantum/Kraus-weighted zeta of a simplicial complex is unoccupied territory — in contrast to the graph case, where Matsuura–Ohta 2022 already has the Ad-weighted Ihara zeta and its Bass formula. The prover's T5 then supplies exactly that object (arbitrary Kraus weights on the 1-skeleton, twisted flow operators $T_k^E$, universal Schur identity) without ever recording the priority statement.
- Lead: if the notebook ever claims novelty, this is the sentence it rests on, and it needs a byte-cited "Not found" entry in `notes/extract/` of the same kind as the one for general complexes. Otherwise the T5 construction is the one genuinely new definition in the whole simplicial sidequest and nothing in the repo says so.
- Related: -

### L15-008 The scattering-sector / Dirichlet-character mismatch, and the two papers named for it
- Source: B:101 and B:141 (assistant messages); B:105, B:109 (the searches that produced them). Absent from `notes/bc-symmetry-generators.md` (which says only "The Gamma_0(N) scattering/character calculation remains open"), and the two arXiv ids are not in `refs/`.
- Raised by: codex prover
- Status at last mention: stated in a message only
- Content: The handoff's planned next move was a finite-level $\Gamma_0(N)$ scattering-matrix computation, to be matched against Bost–Connes characters. The prover checked this and warned: "the literature does not give an automatic one-to-one match between untwisted $\Gamma_0(N)$ scattering sectors and all Dirichlet characters modulo $N$" — i.e. counting sectors by characters mod $N$ is wrong without twisting. It named two starting points: arXiv **1803.06016** (*Twist-minimal trace formulas*, for the explicit Eisenstein-series formulas, §2.7) and arXiv **1106.5741** (*Newforms and spectral multiplicities*).
- Lead: before any BC↔scattering identification, fetch those two e-prints into `refs/src/`, extract the explicit Eisenstein/scattering-matrix formulas for $\Gamma_0(N)$ with nebentypus, and write down the actual sector/character correspondence (which is a statement about *twisted* $\Gamma_0(N)$, newform level and oldform multiplicity). If the correspondence is many-to-one, the "one BC character per scattering channel" picture in the Phantasm programme is wrong as stated and the bond needs the multiplicity space.
- Related: L15-009, L15-010.

### L15-009 Three-part programme for the arithmetic mixed-rebound state, including the missing invariant-sector argument
- Source: B:113–147 (long assistant message); only the reset-positivity test survives, at `notes/bc-symmetry-generators.md:332`.
- Raised by: codex prover
- Status at last mention: stated in a message only
- Content: The prover organised the "next most consequential step" as three questions, of which only the second reached the repo. (1) *What is the common arithmetic structure?* Compute a small-level scattering matrix and its symmetry action, then look for an explicit map from the BC residue/character construction. (2) *Does the induced state pass the positivity test?* In the Siemon–Holevo–Werner exit-and-reinsertion form, with $B$ the no-event generator, $C=-(B+B^\dagger)\ge0$ and $\mathcal L_\Omega(X)=BX+XB^\dagger+\mathrm{Tr}(CX)\Omega$, stationarity of a proposed arithmetic density $\sigma$ with $\mathrm{Tr}(C\sigma)>0$ *solves for* the reset state, $\Omega=-(B\sigma+\sigma B^\dagger)/\mathrm{Tr}(C\sigma)$, so existence is exactly $-(B\sigma+\sigma B^\dagger)\ge0$. (3) *Does reinsertion preserve the odd zero modes?* "Preserving $B$ as the no-event generator does not itself preserve its eigenvalues in the full Lindbladian. This needs an explicit invariant-sector argument."
- Lead: item (3) is the one nobody has written down. Concretely: for the vacuum-decay model whose odd sector already carries the zeros, add the rank-one reset $\mathrm{Tr}(CX)\Omega$ and compute whether the zero-mode subspace is still $\mathcal L_\Omega$-invariant — it is iff $\mathrm{Tr}(CX)=0$ on that subspace. That is a checkable linear condition on $\Omega$ and would decide in an afternoon whether any reset completion can keep the zeros.
- Related: L15-008, L15-010.

### L15-010 Stage the BC limit: work at $\beta>1$ or with cutoffs, and formulate $\beta=1$ as a state functional
- Source: B:145 (assistant message) and B:183–188 (the follow-up clarification message); the $\beta=1$/non-normality point is in `notes/bc-symmetry-generators.md` B0, the staging advice is not.
- Raised by: codex prover
- Status at last mention: stated in a message only
- Content: "Initially this should use controlled cutoffs or $\beta>1$. The critical BC state is not a normal density in the standard representation, so reaching $\beta=1$ requires an algebraic formulation of the limit." The companion message adds the formulation that avoids densities altogether: find a CP unital Heisenberg semigroup with $\varphi_{\rm BC}\circ T_t=\varphi_{\rm BC}$ and $T_t\circ\alpha_g=\alpha_g\circ T_t$, i.e. impose stationarity on the *state functional*, not on a density matrix. It also flags that "carrying a symplectic action does not automatically mean that the generator commutes with every symplectic transformation" — one must say which transformations are dynamical symmetries and which merely act covariantly — and that "the BC fixed state alone does not force Galois covariance; covariance is an additional requirement of the programme".
- Lead: redo the B2/B3 cone calculation at $\beta>1$, where the state is an honest density $\mathrm{diag}(p^{-\beta},(1-p^{-\beta})/(p-1),\dots)$, and watch how the cone dimensions vary with $\beta$; the $\beta\to1$ behaviour of the cone (does it grow or collapse?) is the finite-level shadow of the critical limit and is cheap to compute.
- Related: L15-009, L15-014.

### L15-011 The boxed Ramanujan criterion for a graded cMPS: $A^\dagger G+GA=-2\Delta G$, $G>0$
- Source: B:541–634 (long assistant message), specifically B:593, B:595; preserved verbatim in `outputs/ramanujan-boson-fermion-cmps.md:88` and summarised in `HANDOFF.md`, but not in `notes/bc-symmetry-generators.md` and not registered as a claim.
- Raised by: codex prover (answering TJO's question "what is the general shape of the Ramanujan property for fermion+boson cMPS? I am hoping it is a condition on Q, R")
- Status at last mention: stated in a message only (exported, unreviewed, unregistered)
- Content: For a translation-invariant boson–fermion cMPS with bond parity $P$, the fermionic correlations propagate with the **parity-twisted** transfer generator $\mathcal K_f(X)=Q^\dagger X+XQ+\sum_b R_b^\dagger XR_b-\sum_f R_f^\dagger XR_f$ (minus signs on fermionic species only; the ordinary norm transfer has all plus signs and is CP, and $X\mapsto PX$ intertwines the two). Restrict to an invariant sector $\mathcal E$ meant to carry the zeros and set $A=\mathcal K_f|_{\mathcal E}$. The one-sided Ramanujan condition is $\mathrm{Re}\,\lambda\le-\Delta$; with an arithmetic reflection $\lambda\mapsto-2\Delta-\bar\lambda$ it becomes $\mathrm{Re}\,\lambda=-\Delta$ (with $\Delta=1/4$ in the Riemann normalisation). The matrix form is $A^\dagger G+GA=-2\Delta G$ with $G>0$, equivalently $e^{tA}=e^{-\Delta t}U_t$ with $U_t$ unitary in the metric $G$; in finite dimension this is exactly "critical-line spectrum **and** diagonalizability", so it is strictly stronger than the spectral statement only by excluding Jordan blocks.
- Lead: the open half is $G$. "Choosing $G$ from the BC and symplectic structure would give it arithmetic content; the stationary density does not automatically provide the required metric." Concrete next step: ask whether the Weil/metaplectic representation on the bond supplies a canonical invariant positive form, and whether that form is the one that makes the shifted transfer skew-adjoint. If yes, RH becomes a covariance statement about a representation rather than a spectral statement about an operator.
- Related: L15-012, L15-013.

### L15-012 Regularity ($R_\alpha R_\beta=(-1)^{p_\alpha p_\beta}R_\beta R_\alpha$, $R_f^2=0$) is an extra condition the BC generator cone never imposed
- Source: B:525–533 and B:552 (assistant messages); preserved in `outputs/ramanujan-boson-fermion-cmps.md` and `HANDOFF.md`, absent from `notes/bc-symmetry-generators.md` and from `scripts/bc_symmetry_generators.py`.
- Raised by: codex prover
- Status at last mention: corrected in final (recorded in HANDOFF as a refinement of the same session's own B0–B6 calculation)
- Content: The prover found, while answering the cMPS question, "a restriction absent from the earlier Lindbladian analysis: a regular mixed cMPS requires the $R_\alpha$ to obey the species' commutation and anticommutation relations. Parity covariance alone does not impose that." Explicitly: $PQP=Q$, $PR_\alpha P=(-1)^{p_\alpha}R_\alpha$ **and** $R_\alpha R_\beta=(-1)^{p_\alpha p_\beta}R_\beta R_\alpha$, so $R_f^2=0$, with $Q=-iH-\tfrac12\sum_\alpha R_\alpha^\dagger R_\alpha$ in left canonical form. This is a real narrowing of the B2/B3 cone result: the $(p-1)(p+1)^2$- and $(2p-2)$-dimensional cones were computed without the regularity constraint, so they overcount the physically realisable graded cMPS generators.
- Lead: re-run the B3 dimension count with the regularity relations imposed as extra polynomial constraints (they are quadratic in the jump operators, so this becomes a variety inside the cone, not a linear section). If the regular locus is much smaller, the "Galois + Weil covariance leaves too much freedom" conclusion of B6 may need revising in the direction the programme wants.
- Related: L15-011, L15-014.

### L15-013 The $\sigma$-metric dissipation identity, and why it kills instantaneous coercivity on any sector containing a jump operator
- Source: B:541–634 (same message), with the numerical/symbolic checks at B:530 and B:536; preserved in `outputs/ramanujan-boson-fermion-cmps.md` and `HANDOFF.md`, not registered as a claim and with no evidence script.
- Raised by: codex prover
- Status at last mention: stated in a message only
- Content: With $\|X\|_\sigma^2=\mathrm{Tr}(\sigma X^\dagger X)$ and $\sigma$ the stationary bond density, stationarity gives the exact identity $-2\,\mathrm{Re}\langle X,\mathcal K_fX\rangle_\sigma=\sum_b\|[R_b,X]\|_\sigma^2+\sum_f\|\{R_f,X\}\|_\sigma^2$. Regularity ($R_f^2=0$, so $\{R_f,R_f\}=0$) makes the right-hand side vanish at $X=R_f$. Hence **no strictly positive instantaneous dissipation bound in the BC-state metric can hold on a sector containing a nonzero $R_f$**, even though the spectral decay rates on that sector can all be strictly positive. This is the precise reason the Ramanujan condition must be spectral (or in a *different* metric $G$), not a Dirichlet-form coercivity bound.
- Lead: this is a clean, checkable obstruction and deserves promotion to a proposition with an evidence script; it also tells you that the natural Hilbert–Pólya metric $G$ is **not** the GNS metric of the stationary state, which contradicts the most obvious guess in the Phantasm programme. Worth testing whether $G$ can be taken to be $\sigma^{-1}$-weighted or a Weil-invariant form instead.
- Related: L15-011, L15-012.

### L15-014 The two-fermion example: elementary odd modes and full odd sector have different decay rates
- Source: B:541–634, specifically B:610 and B:620, with the exact sympy verification at B:536; preserved in `outputs/ramanujan-boson-fermion-cmps.md` and `HANDOFF.md`. HANDOFF explicitly says "These scratch checks are described in the export, not yet a registered evidence script or independently reviewed theorem."
- Raised by: codex prover
- Status at last mention: stated in a message only (unregistered numerical/symbolic check)
- Content: Take two fermionic bond modes, $R_1=\sqrt\kappa\,c_1$, $R_2=\sqrt\kappa\,c_2$, $H=g(c_1^\dagger c_2^\dagger+c_2c_1)$, $Q=-iH-\tfrac\kappa2(n_1+n_2)$. On the elementary odd sector $\mathcal E=\mathrm{span}\{c_1,c_2,c_1^\dagger,c_2^\dagger\}$ the parity-twisted transfer eigenvalues are $-\kappa/2\pm ig$; but the **full** odd operator space also contains $-3\kappa/2\pm ig$. The exact characteristic polynomial of the full odd block is $[((z+\kappa/2)^2+g^2)((z+3\kappa/2)^2+g^2)]^2$. Consequence: a Ramanujan property demanding one uniform decay rate on the *whole* odd sector is false even for a perfectly regular fermionic cMPS; the condition must be imposed on an arithmetically identified sector, with the remaining odd spectrum satisfying only a one-sided bound.
- Lead: identify $\mathcal E$ arithmetically. The example shows the higher operator sectors are integer multiples ($1\times$, $3\times$) of the elementary rate, which looks like a "multi-particle" tower; if the zeros are to be the elementary modes, one needs a physical reason (a Krylov space generated by single insertions, say) to project onto them. Turn this into a registered evidence script — it is three lines of sympy and it constrains every later Ramanujan formulation.
- Related: L15-011, L15-013.

### L15-015 The abandoned "$q$-eigenvector in the polarisation trace line" genus-2 ansatz
- Source: D:125 and D:132 (two inline `least_squares` runs), with the verdict at D:129 (assistant message); the impossibility is recorded in the final file at `notes/ring-norm-tensor/astra-proofs.md:692` and `:759`, but the attempted numerical ansatz itself is not.
- Raised by: orchestrator brief (task T4(a) "suggested ansatz"), tested and rejected by the prover
- Status at last mention: dead (false as drafted)
- Content: The brief proposed that the even block of the doubled transfer be $\begin{pmatrix}t&u\\v&W\end{pmatrix}$ with the eigenvalue $q$ sitting in "the trace line of $\mathrm{End}(H^{1,0})$ (the polarisation class)" and the three nilpotent modes in the traceless part. The prover coded this directly: a $5\times5$ even block with $E_{00}=t=e^{x_0}$, $E_{01}=E_{10}=h=\sqrt{21}/2$, and $E_{1:,1:}=M\otimes M/t+B\otimes\bar B$ where $M=\begin{pmatrix}3/2&\sqrt5\\-\sqrt5&0\end{pmatrix}$, fitting the characteristic polynomial to $(1,-6,5,0,0,0)$ — first with real $B$ (D:125), then with $B=\begin{pmatrix}a&ib\\ic&d\end{pmatrix}$ (D:132). Both searches were abandoned. The final file then proves the structural reason: "The $q$-eigenvector cannot be the pure trace-line operator $0\oplus I_2$. The vacuum line cannot itself be an invariant line carrying the eigenvalue 1", and gives the actual eigenvectors $(\sqrt2,I_2)$ and $(-\sqrt2,I_2)$ for eigenvalues $q$ and $1$.
- Lead: none stated; the useful residue is that the cohomological labelling of eigenvectors (vacuum $\leftrightarrow$ 1, polarisation class $\leftrightarrow$ $q$) is *not* preserved by any tensor with active fermionic couplings — the true eigenvectors mix the vacuum with the trace line in the ratio $\pm\sqrt2$. Any future "the bond is $H^*(J)$" story has to accommodate that mixing.
- Related: L15-016.

### L15-016 The F_5 three-species statement was open, then closed in the audit pass by a rational contraction certificate
- Source: D:150 (first full draft: "The proposed three-species existence theorem over $\mathbb F_5$ ... remain open here"), D:176–282 (the certificate script), D:283 (assistant message announcing it), D:462 and D:465 (the two patches that rewrote the summary, the conjecture and the RESULT line).
- Raised by: codex prover
- Status at last mention: corrected in final (upgraded from open to proved for the particular curve; the conjecture was simultaneously widened)
- Content: For most of the session the deliverable was: an explicit nine-species construction on $C^{1|2}$ for every prime power $q\ge16$ (five even, four odd letters, valid because $q+1\ge4\sqrt q$), plus an exact 28-real-unknown polynomial feasibility system (4.9) for the requested two-even/one-odd tensor over $\mathbb F_5$, declared **open**, with Conjecture T4.C stated only for the supplied curve. In the final audit the prover found a certificate and reversed this: T4.5a proves exact existence over $\mathbb F_5$, and Conjecture T4.C was **restated as the universal claim** ("for every ordinary simple genus-two curve") with status open. The patch also added, in the same pass, that "Total degree in dimension two would only give $|\pi_1|^2|\pi_2|^2=q^2$; it does not supply the two separate equalities" — i.e. the genus-1 degree argument does not generalise, and Rosati positivity is genuinely needed.
- Lead: what is left after the reversal is the *selection* problem, stated in the revised conjecture: "Whether those entries can be selected naturally from the equation or the polarized CM data is a further unresolved requirement." The certified $\mathbb F_5$ tensor is a numerically located algebraic point with 90-digit coordinates and no geometric meaning. Finding a closed form for it (or proving none exists over $\mathbb Q(\pi_1,\pi_2)$ in a normal form) is the next concrete step for Tier B.
- Related: L15-017.

### L15-017 The certificate method is reusable and was not applied to the remaining open cases
- Source: D:176–282 (the full script, stored in-session as `q5_cert_script` and later committed as `notes/ring-norm-tensor/scratch/t45a_certificate.py`), D:371 (the 90-digit active coordinates).
- Raised by: codex prover
- Status at last mention: raised, not pursued (for the other open cases)
- Content: The method: run `least_squares` on all 28 real unknowns; use QR-with-column-pivoting on the $9\times28$ Jacobian to select 9 active coordinates (`sel=[18,15,11,19,14,2,22,4,3]`); Newton-iterate those 9 in `mpmath` at 110 decimal places; then re-evaluate $F$ and $J$ in **exact rationals**, invert $J$ approximately to get $B$, and verify the Kantorovich/Krawczyk-style bounds $\eta=\|Bf\|_\infty<10^{-70}$, $\epsilon=\|I-BJ\|_\infty<10^{-50}$, $\kappa=\epsilon+\|B\|\cdot81H\cdot r<1/4$, $\eta+\kappa r<r$ with $r=10^{-30}$ — a strict contraction of a rational box into itself, hence an exact solution.
- Lead: the same machinery answers the other open feasibility questions of the same file at almost no cost — (i) three-species existence over $\mathbb F_7,\mathbb F_9,\mathbb F_{11},\mathbb F_{13}$ (the gap between $q=5$ and the $q\ge16$ closed form); (ii) the purely bosonic $C^{2|2}$ genus-2 realisation with cancellation allowed, listed as open; (iii) whether a two-species (one even, one odd) solution is genuinely infeasible rather than merely not found. Each is the same shape of problem: a square polynomial system in a box.
- Related: L15-016.

## Small but possibly consequential

1. **`fmd` native PDF prints raw LaTeX** (C:203, C:236) — every math export must go fmd→HTML→headless Chromium; this is already in memory but the transcript is where it was established, with the verified binary hash.
2. **The `x^3` cut-rank probe was self-defeating** (D:114): the brief asked for the cut rank of $\psi(\mathrm{tr}_{q^n/q}(x^3))$ over $\mathbb F_2$ to test non-quadratic amplitudes, but $x^3=x^{1+2}$ *is* quadratic in characteristic 2, so the test could not probe what it was meant to probe. The prover ran it anyway (ranks through $n=8$, max 16) and said so.
3. **The doubled-transfer trace was mis-stated in the brief** (D:114): $\mathrm{Tr}$ of a block of $\mathcal E=\sum_s A_s\otimes\bar A_s$ is $\sum_s|\mathrm{Tr}\,A_s|^2$, *not* $\sum_s\|A_s\|_{\rm HS}^2$ — which is why the drafted Hilbert–Schmidt proof of the bosonic genus bound is false (the bound itself survives via all-power traces).
4. **A $p=5$ assertion was written, failed and deleted** (B:217, B:230): the check `"full Weil symmetry does not force equal odd decay rates"` was first coded at $p=5$ on class-averaged generators, failed, and was removed; the counterexample only exists at $p=7$ via a scalar-orbit perturbation. So the smallest odd prime where the freedom is visible is 7, not 5.
5. **An "invariant Hamiltonian changes frequencies by $O(1)$" claim was weakened** (B:217, B:225): from `max|Im λ| > 0.5` to a relative shift `> 0.05`. The invariant Hamiltonian $H=hP$ moves frequencies, but not by an $O(1)$ amount at these $p$.
6. **The scalar-orbit trick** (B:230, in a code comment): scalar multiplication $v\mapsto av$ on phase space commutes with $SL_2$ although it is not itself symplectic — that is the whole mechanism of the $p=7$ counterexample, and it suggests a general recipe for building covariant-but-non-symplectic perturbations of any Weyl-covariant generator.
7. **The $\Gamma_0(N)$ sector/character mismatch** (L15-008) invalidates the simplest form of the BC↔scattering dictionary before anyone has computed a scattering matrix; cheap to settle, expensive to discover late.
8. **The BC-state metric is probably the wrong metric for Hilbert–Pólya** (L15-013): the stationarity Dirichlet identity vanishes on jump operators, so the natural GNS inner product cannot certify uniform decay. Every "the zeros are the decay rates in the state's own metric" formulation needs re-examining.

## Dead routes recorded

- **"For every finite 2-complex there is a vertex-level $P(u)=1-uA+u^2Q_1-u^3Q_2$ with $\det(1-uT_1)\det(1+uT_2)^{-1}=(1-u^3)^{\chi}\det P(u)^{-1}$"** (A:85, brief T2). False. Correction: on $\partial\Delta^3$ the ordered edge flow is identically zero and the chamber flow gives $(1-u^4)^6$, so no polynomial vertex compression of degree $3f_0$ can exist; the universal replacement is the forbidden-transition Schur complement over $C^{\Omega_k}\oplus C^{\Omega_{k-1}}$, which always exists. (Announced in the transcript at A:142 before being written up.)
- **"Vertex links are generalised polygons of the same parameters $\Leftrightarrow$ cubic collapse"** (A:85, brief T2(i)). Not false but not proved, and explicitly declined: the prover wrote that the phrase "is not a proved characterization of that class or of cubic collapse". Recorded as open, not as a theorem. (L15-001.)
- **"The Cayley/Kraus twist is the $\pi\otimes\bar\pi$-isotypic block of the untwisted determinant"** (A:72–97, brief T5(a)). Announced false at A:142: "the Cayley twist draft conflates a connection on the full complex with a representation block on its quotient; their determinant multiplicities differ." Correction: a covariant full-cover representation connection is pure gauge; Artin factors use quotient voltages. Also, the brief's guessed exponent $\chi\dim(\pi)^2/|G|$ for the trivial factor is not a rational determinant and "the factor does not live only in the trivial block."
- **"The zeros of the total zeta are exactly the eigenvalues of the odd sector"** (A:76, brief T3). False as drafted; announced at A:178: "chamber factors can cancel against edge factors: the rank-three vertex $L$-function remains a reciprocal polynomial and has no uncancelled finite zeros." Correction requires reciprocal, sign, multiplicity and cancellation qualifications.
- **"$\mathrm{Tr}\,\mathcal E_{++}=\sum_s\|a_s\|_{\rm HS}^2$", hence the Hilbert–Schmidt proof of the genus bound** (D brief T3(a), corrected at D:114). False: the correct trace is $\sum_s|\mathrm{Tr}\,a_s|^2$. The genus bound $g\le1$ for purely bosonic tensors without cancellation survives, but by a Cauchy–Schwarz argument on the ring amplitudes applied to traces of *all* powers.
- **"Place the eigenvalue $q$ in the polarisation trace line of $\mathrm{End}(H^{1,0})$ and the nilpotents in the traceless part"** (D brief T4, corrected at D:129). False whenever the fermionic couplings are active: the $q$-eigenvector cannot be $0\oplus I_2$ and the vacuum line is not invariant. Two least-squares ansätze built on this labelling (D:125, D:132) were abandoned. (L15-015.)
- **"The requested cut rank of $\psi(\mathrm{tr}(x^3))$ over $\mathbb F_2$ probes a non-quadratic obstruction"** (D brief T0(b), corrected at D:114). False: $x^3=x^{1+2}$ is quadratic in characteristic 2, so the test is inside the supersingular family it was meant to escape.
- **"Exact three-species existence over $\mathbb F_5$ is open"** (D:150, the prover's own first draft). Superseded within the same session by the rational contraction certificate (D:283, D:462); the statement that is actually open is now the *universal* version plus the natural-selection requirement. (L15-016.)
- **"Full linear Weil covariance does not force equal odd decay rates" tested at $p=5$** (B:217, B:230). The class-averaged generators at $p=3,5,7$ all have coinciding odd real parts; the assertion was deleted at $p=5$ and re-established only at $p=7$ with a scalar-orbit perturbation of size $\epsilon=1/(4p^2)$.
