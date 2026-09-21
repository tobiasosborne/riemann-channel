# Lane L13: lab book shards 05 to 11

Scope: the second half of the registered pdflatex lab book (shards 05, 06, 06b-06h, 07,
08, 08b-08g, 09, 09b, 09c, 11). Ideas, leads, conjectures, "not established" paragraphs,
reviewer/prover corrections and dead routes only; the established mathematics is not
summarised. Every open / conjectured / assumed / sketched claim in `db/claims.tsv` whose
shard column names one of these files is covered (checked by grep, see Coverage).

## Coverage

| file | lines | read fully? | ideas found |
| --- | --- | --- | --- |
| report/sections/05_weil_lps_channels.tex | 300 | yes | 7 (L13-001 … L13-007) |
| report/sections/06_artin_schreier_mps.tex | 212 | yes | 5 (L13-008 … L13-012) |
| report/sections/06b_artin_schreier_super.tex | 222 | yes | 6 (L13-013 … L13-018) |
| report/sections/06c_ring_norm_inputs.tex | 199 | yes | 7 (L13-019 … L13-025) |
| report/sections/06d_ring_norm_elliptic.tex | 130 | yes | 7 (L13-026 … L13-032) |
| report/sections/06e_ring_norm_bosonic_nogo.tex | 129 | yes | 6 (L13-033 … L13-038) |
| report/sections/06f_ring_norm_genus_two.tex | 294 | yes | 13 (L13-039 … L13-051) |
| report/sections/06g_ring_norm_examples.tex | 147 | yes | 6 (L13-052 … L13-057) |
| report/sections/06h_zeta_conditions.tex | 211 | yes | 13 (L13-058 … L13-070) |
| report/sections/07_deligne_via_graphs.tex | 297 | yes | 8 (L13-071 … L13-078) |
| report/sections/08_quantum_ihara_general.tex | 299 | yes | 5 (L13-079 … L13-083) |
| report/sections/08b_weil_positivity.tex | 188 | yes | 6 (L13-084 … L13-089) |
| report/sections/08c_weil_positivity_continuous.tex | 282 | yes | 8 (L13-090 … L13-097) |
| report/sections/08d_complex_zeta.tex | 320 | yes | 9 (L13-098 … L13-106) |
| report/sections/08e_complex_zeta_graded.tex | 211 | yes | 10 (L13-107 … L13-116) |
| report/sections/08f_complex_zeta_quantum.tex | 271 | yes | 12 (L13-117 … L13-128) |
| report/sections/08g_weil_window_extension.tex | 207 | yes | 7 (L13-129 … L13-135) |
| report/sections/09_prior_art.tex | 300 | yes | 7 (L13-136 … L13-142) |
| report/sections/09b_selberg_dictionary.tex | 244 | yes | 7 (L13-143 … L13-149) |
| report/sections/09c_selberg_tower_cusp.tex | 185 | yes | 7 (L13-150 … L13-156) |
| report/sections/11_reproducibility_map.tex | 66 | yes | 1 (L13-157); an infrastructure shard, no mathematical ideas of its own |
| db/claims.tsv (cross-check) | — | grepped for open / conjectured / assumed / sketched | all 5 open+conjectured and all 48 assumed/sketched rows of these shards appear above |

Cross-check against `db/claims.tsv`: the only rows with status `open` or `conjectured` in
these shards are `conj:weil-lps-hecke` (L13-001), `conj:quantum-lindblad-gap` (L13-148),
`conj:vertex-collapse-characterisation` (L13-127), `conj:amplitude-locality` (L13-023) and
`conj:three-letter-universal` (L13-044). The `assumed` rows are L13-016/017/018 (06b),
L13-021/024/025 (06c), L13-040/041 (06f), L13-105 (08d, eight `asm:h-*` rows) and L13-149
(09b, six rows). The `sketched` rows are L13-003, L13-008, L13-033, L13-046/047/048/049,
L13-052/053/054/055, L13-058/059/060/061/062/063/064, L13-072, L13-076, L13-079, L13-092,
L13-129/130/132/133, L13-136, L13-155.

Two conjectures that these shards *point at* but that are registered in other shards
(`sec:open`) are recorded here as leads anyway, because the pointer is the idea:
`conj:assemble-over-p` (L13-002) and `conj:kraus-ramanujan` (L13-080, L13-096).

## Ideas and leads

### L13-001 Hecke identification of the Weil--LPS joint spectra
- Source: report/sections/05_weil_lps_channels.tex:225-264, claim `conj:weil-lps-hecke`
- Raised by: orchestrator (Claude), from the founding session's handoff
- Status at last mention: registered as open
- Content: the commuting Weil--LPS channels $\Phi_q^\pm$ at a fixed odd prime $p$ have a
  joint spectrum of small-degree algebraic integers, e.g. for $(p;q_1,q_2)=(13;17,29)$ the
  even block has 19 distinct pairs $(a_{17},a_{29})$, some integral, one quadratic in
  $\mathbb Q(\sqrt{17})$, the rest of higher degree. The conjecture is that these pairs are
  Hecke eigenvalues $a_q(f)$ of weight-2 forms attached to the quaternion algebra ramified
  at $\{2,\infty\}$, with level determined by $p$, via Jacquet--Langlands.
- Lead: "The identification was *not* done here; it needs LMFDB and the Jacquet--Langlands
  bookkeeping" (05:263-264). If it worked, the finite model's spectrum would literally be
  modular-form data and the Weil--LPS channel would become an arithmetic object rather than
  an analogy.
- Related: L13-004, L13-005.

### L13-002 Assembling the Weil--LPS channels over all primes $p$
- Source: report/sections/05_weil_lps_channels.tex:290-299 ("Not established"), pointing to
  `conj:assemble-over-p` in `sec:open`
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued (registered in another shard)
- Content: nothing is said about $p\to\infty$, or about assembling the $\Phi_q$ over all
  $p$ into a single object whose rings are the primes. The shard calls this "the parent
  repository's global question in a new guise".
- Lead: build the direct integral / inductive limit over $p$ and ask whether the assembled
  object has a zeta whose primes are the rational primes. Consequence: it would turn a
  family of finite Ramanujan models into a candidate for the Phantasm's side A.
- Related: L13-001, L13-144.

### L13-003 Upgrading `prop:weil-lps-exactly-ramanujan` from sketched to proved
- Source: report/sections/05_weil_lps_channels.tex:101-128, claim
  `prop:weil-lps-exactly-ramanujan` (status sketched)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched
- Content: the two-line argument is Harrow's transfer inequality plus Lubotzky--Phillips--
  Sarnak; $(q+1)\lambda_2(\Phi_q^\pm)\le 2\sqrt q = \lambda_H$ in adjacency units. The
  status is sketched for two reasons only: LPS has no byte-verified local source in
  `refs/`, and irreducibility of the Weil blocks $W^\pm$ plus the projective-phase
  bookkeeping of Step 4 are verified numerically rather than cited.
- Lead: fetch a quotable LPS source and cite (or prove) irreducibility of the even/odd Weil
  blocks. Consequence: the notebook's one exactly-Ramanujan quantum expander becomes a
  proved claim.
- Related: L13-138 (prior art says the mechanism is known but this instance is not).

### L13-004 "Source of the bound: unknown" --- the honest row of the dictionary
- Source: report/sections/05_weil_lps_channels.tex:266-288
- Raised by: orchestrator (Claude)
- Status at last mention: raised, standing diagnosis
- Content: the reading table maps commuting prime dilations to commuting Hecke channels,
  the Weil representation to $W^\pm$ on $\ell^2(\mathbb F_p)$, joint spectrum to Hecke
  eigenvalues and RH to $|\varepsilon| = \sqrt q$. The last row is "source of the bound:
  unknown" versus "source of the bound: Deligne, via LPS". These channels are Ramanujan
  *because Deligne proved the Weil conjectures*, not because they are channels.
- Lead: none stated; it is the standing complaint that motivates the search for a
  channel-internal reason for the bound.
- Related: L13-071, L13-074, L13-077.

### L13-005 The structure a Hecke identification would predict, as a test
- Source: report/sections/05_weil_lps_channels.tex:246-252
- Raised by: orchestrator (Claude)
- Status at last mention: partially explored (observed numerically, not turned into a test)
- Content: four features are visible and were read as evidence: joint eigenvalue pairs,
  small-degree algebraic integers, multiplicities equal to the multiplicity of the
  corresponding irreducible representation of $\mathrm{PSL}_2(\mathbb F_p)$ in
  $W^\pm\otimes\overline{W^\pm}$, and every pair inside the box
  $[-2\sqrt{q_1},2\sqrt{q_1}]\times[-2\sqrt{q_2},2\sqrt{q_2}]$. The shard is explicit that
  algebraicity is not a test (the Cayley adjacency matrix is integral by construction).
- Lead: verify the multiplicity prediction representation by representation; that would be
  a cheap partial confirmation of L13-001 without LMFDB.
- Related: L13-001.

### L13-006 Quantum Ihara zeta of the Weil--LPS channel: the wording correction on poles
- Source: report/sections/05_weil_lps_channels.tex:196-223, claim `num:weil-lps-rh`
- Raised by: the codex prover lane of the graded-Ramanujan campaign (correction applied
  2026-09-15)
- Status at last mention: corrected, settled
- Content: for $(13,17)$, odd block, the edge superoperator on $M_6\otimes\mathbb C^{18}$
  has $|\varepsilon| \in \{17,\sqrt{17},1\}$ with multiplicities $1,70,577$, satisfying
  Ihara--Bass to $10^{-14}$, so every nontrivial pole sits on the critical circle. The
  wording was corrected to say that *the ungraded quantum Ihara zeta has poles only* --- no
  zeros --- which is the sign asymmetry of shard 07.
- Lead: for every other admissible pair the same conclusion follows from the quadratic
  $\varepsilon^2-\lambda\varepsilon+q=0$ without building the edge operator; i.e. the
  expensive computation never has to be repeated.
- Related: L13-074 (the sign), L13-079.

### L13-007 The Weil--LPS channel as the finite model of the Riemann channel
- Source: report/sections/05_weil_lps_channels.tex:12-19, 266-288
- Raised by: the founding session's handoff, executed by the orchestrator
- Status at last mention: pursued, positive (the object exists and is self-checking)
- Content: the programme item was to build a finite object with every ingredient of the
  Riemann channel present and checkable: commuting dilations indexed by primes, an
  arithmetic quotient supplying expansion, and the Weil representation as the Hilbert
  space. The shard reports this was achieved, is cheap to build, self-checks at every step
  and lands on the parent campaign's Hilbert space with the parent campaign's
  representation.
- Lead: none stated beyond L13-001 and L13-002.
- Related: L13-001, L13-002, L13-004.

### L13-008 Dwork's $p$-adic operator as a coarse-graining tensor-network step
- Source: report/sections/06_artin_schreier_mps.tex:176-197, claim `obs:as-nonquadratic`
  (sketched)
- Raised by: orchestrator (Claude), from the founding session's note
- Status at last mention: registered as sketched; pursued and found structurally limited
- Content: for non-quadratic $g$ the trace form in the shift basis is non-local and
  $n$-dependent, so no fixed local tensor exists. The uniform transfer operator that does
  exist is Dwork's $p$-adic operator, which has *exactly* the form of a coarse-graining
  tensor-network step: "local weight, then decimate by $q$" --- multiplication by a
  splitting function followed by $x^m \mapsto x^{m/q}$, with infinite but nuclear bond
  dimension and $L$ as a Fredholm determinant.
- Lead: none pursued. The structural verdict is that it cannot deliver the RH analogue,
  because the Newton polygon it computes is a statement about $p$-adic valuations; that is
  why Deligne's proof lives in $\ell$-adic cohomology.
- Related: L13-011, L13-071.

### L13-009 A different, $n$-uniform basis making cubic traces local
- Source: report/sections/06_artin_schreier_mps.tex:199-207 ("Not established")
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued --- "neither settled nor searched: no
  candidate was found"
- Content: a self-dual normal basis makes the *bilinear* trace form local; it says nothing
  about the trilinear one, where $\mathrm{Tr}(x^3) = \sum_{ijk}c_{ijk}x_ix_jx_k$ with
  $n$-dependent structure constants. Whether some other basis of $\mathbb F_{q^n}$, uniform
  in $n$, makes cubic traces local was never searched.
- Lead: search for such a basis. If one existed, the MPS formulation of the Weil
  conjectures would extend past degree three, i.e. past the supersingular boundary.
- Related: L13-023 (the restricted locality conjecture is the negative-side formalisation),
  L13-025.

### L13-010 The functional equation as the involution $E \mapsto q\,E^{-\dagger}$
- Source: report/sections/06_artin_schreier_mps.tex:144-147
- Raised by: the founding session's note
- Status at last mention: raised in passing, trivialised
- Content: for the quadratic Artin--Schreier transfer matrix, rationality of $Z$ holds
  because $E$ is finite, and the functional equation is recorded as the involution
  $E \mapsto q E^{-\dagger}$, which scaled unitarity ($EE^\dagger = qI$) makes trivial.
- Lead: none stated. Worth keeping because it is the cleanest "FE = an involution on the
  transfer operator" statement in the book; compare C4 of the zeta-conditions ledger, where
  the sufficient visible mechanism is $J\Gamma = \Gamma J$, $JEJ^{-1} = qE^{-1}$.
- Related: L13-059, L13-060, L13-086.

### L13-011 The boundary lesson: Ramanujan is manifest or it is arithmetic input
- Source: report/sections/06_artin_schreier_mps.tex:209-211; echoed at 07:253-260
- Raised by: orchestrator (Claude)
- Status at last mention: standing diagnosis
- Content: the boundary at degree three is "the same boundary met for graphs and for the
  Riemann channel: the Ramanujan bound is either manifest, because the transfer matrix is a
  scaled unitary, or it comes from arithmetic input that sits outside the transfer structure
  altogether." Shard 07 places the Artin--Schreier computation on the Weil side of the
  Weil/Deligne divide, since $EE^\dagger = qI$ is Parseval for the additive characters, an
  explicit inner product.
- Lead: none stated; it is the dichotomy the whole notebook is trying to break.
- Related: L13-004, L13-071, L13-077.

### L13-012 Maximal curves as a saturation phenomenon
- Source: report/sections/06_artin_schreier_mps.tex:116-120; explained at
  06b:193-208, claim `cor:as-weil-bound-fixed-space`
- Raised by: orchestrator (Claude), explained by the codex prover
- Status at last mention: pursued, resolved
- Content: the ratios $|S_n|/q^{n/2}$ are 1 at every tested $n$ except $n=4$, where they
  are $q$: the sums saturate the Weil bound, the maximal-curve phenomenon. Shard 06b
  identifies the cause: $|S_n|\le q^J q^{n/2}$ with equality iff the symplectic transfer
  map satisfies $M_g^n = 1$; for $q=3$, $g=x^4$ the map has order 4, so saturation at
  $n=4$.
- Lead: none stated. The general shape --- "saturation = finite order of a symplectic map"
  --- is a transferable idea.
- Related: L13-015.

### L13-013 The exact sign law, and the refutation of two drafted universal laws
- Source: report/sections/06b_artin_schreier_super.tex:12-19, 41-108, claims
  `thm:as-sign-law`, `cor:as-periodic-sign`, `prop:as-sign-counterexamples`
- Raised by: the numerics lane found the failures; the orchestrator proposed a replacement
  that also failed; the codex prover found and proved the exact law
- Status at last mention: pursued, positive (with two dead drafts recorded)
- Content: the founding session's $\alpha_i = -\lambda_i(E)$ is false in general; the
  orchestrator's conjugated replacement fails too. The exact law is
  $S_n(g) = (-1)^{n-1}\delta_n \mathrm{Tr}\,E_g^n$ with $\delta_n =
  \det(F|_{\mathrm{rad}_n})$, equivalently $S_n = (1-2\cdot\mathbf 1_{2h\mid n})
  \mathrm{Tr}\,E_g^n$: a periodic sign flipping exactly when $2h \mid n$. Endpoint
  criteria: the first law holds for all $n$ iff $P_g(-1)\ne0$, the second iff
  $P_g(-\eta(-1))\ne0$.
- Lead: none further; the law was confirmed in 624 checks.
- Related: L13-014 (dead routes list), L13-017.

### L13-014 The count is a supertrace, and the character-sector grading
- Source: report/sections/06b_artin_schreier_super.tex:133-148, claim
  `thm:as-super-transfer`, pointing at `obs:character-sector-grading` and
  `cor:curve-counts-graded`
- Raised by: the codex prover; framed by the orchestrator
- Status at last mention: pursued, positive
- Content: the projective curve has $N_n = \mathrm{str}\,E^n$ for a super-transfer matrix
  whose *even block is the trivial-character sector* and whose *odd block is the nontrivial
  characters*. The count is a supertrace because, by `cor:curve-counts-graded`, it cannot be
  a trace. The odd block has $FF^\dagger = q$ and its multiset is the $2g$ Frobenius
  eigenvalues with no even--odd cancellation.
- Lead: this is the concrete template for "which physical letters carry the grading" ---
  characters, not geometry. Consequence if generalised: a recipe for the graded bond of the
  Phantasm.
- Related: L13-035, L13-055, L13-126.

### L13-015 The transfer unitary is a Weil-representation operator; the Weil bound is Howe's character bound
- Source: report/sections/06b_artin_schreier_super.tex:150-208, claims
  `thm:as-symplectic-map`, `cor:as-weil-bound-fixed-space`
- Raised by: the codex prover
- Status at last mention: pursued, positive (conditional on `asm:weil-implementer-exact`)
- Content: $U_g = E_g/\sqrt q$ factors as a Fourier transform on the retiring register, then
  quadratic phases, then a cyclic relabelling, and satisfies the exact Egorov relation for
  an explicit symplectic map $M_g$. Hence $U_g = e^{i\phi}W(M_g)$, the rank deficiency
  $d_n = \dim\ker(M_g^n-1)$, and $|S_n(g)|\le q^Jq^{n/2}$ with equality iff $M_g^n=1$. The
  fermionic sign of the count on a ring of $n$ sites is the sign of the Frobenius
  permutation, corrected on the fixed space by the radical sign.
- Lead: none stated. The shard's own framing is that the prototype now carries "explicitly,
  every feature the Phantasm is supposed to have: a graded bond, a supertrace count, a
  fermionic sign that is a permutation sign, and a transfer unitary from a Weil
  representation" (06b:17-19).
- Related: L13-012, L13-014, L13-026.

### L13-016 Assumption: exact centred Weil implementers exist
- Source: report/sections/06b_artin_schreier_super.tex:171-177, claim
  `asm:weil-implementer-exact` (assumed)
- Raised by: the codex prover
- Status at last mention: registered as assumed
- Content: there is a genuine (non-projective) unitary representation $W$ of
  $\mathrm{Sp}(2J,\mathbb F_q)$, $q$ odd, with $W(M)T_{u,v}W(M)^{-1} = T_{M(u,v)}$ exactly
  for the centred Weyl operators. Gurevich--Hadani give uniqueness up to scalar
  (`cit:weil-egorov-uniqueness`), not existence of a centred lift.
- Lead: discharge it from a source, or fix the phase cocycle explicitly. Consequence:
  L13-015 and `prop:as-finite-order` stop being conditional.
- Related: L13-015, L13-024.

### L13-017 Assumption: polynomiality of the character $L$-function
- Source: report/sections/06b_artin_schreier_super.tex:63-69, claim `asm:as-lpolynomial`
  (assumed)
- Raised by: the codex prover
- Status at last mention: registered as assumed
- Content: for $\deg g = q^J+1$ and every $a\in\mathbb F_q^\times$, $L(ag,u)$ is a
  polynomial of degree exactly $q^J$ with constant term 1. Root sizes are explicitly *not*
  assumed --- this is what keeps the supersingularity theorem free of the Weil bound.
- Lead: cite or prove. Related assumption `asm:normal-basis` (06b:34-39): $\mathbb F_{q^n}$
  has a normal basis, self-dual for $n$ odd.
- Related: L13-013, L13-018.

### L13-018 Assumption: Frobenius semisimplicity on $H^1$
- Source: report/sections/06b_artin_schreier_super.tex:125-131, claim
  `asm:frobenius-semisimple` (assumed)
- Raised by: the codex prover
- Status at last mention: registered as assumed, used narrowly
- Content: Frobenius on $H^1$ of a smooth projective curve over a finite field is semisimple
  over an algebraic closure. Used *only* for operator similarity, never for net spectra ---
  a deliberate quarantine so the supertrace results do not depend on it.
- Lead: none stated.
- Related: L13-014.

### L13-019 TJO's five-item wish list for the ring-norm tensor
- Source: report/sections/06c_ring_norm_inputs.tex:12-31 ("Question (TJO, 2026-09-14)")
- Raised by: TJO
- Status at last mention: pursued across shards 06c--06g; items (1)--(5) partially answered
  at genus 1 and 2
- Content: for the absolute simplest variety without an *obvious* Polya--Hilbert
  Hamiltonian, wanted: (1) a natural tensor determined by the variety; (2) the graded
  decomposition of the bond and why; (3) a theorem that the ring norms are the counts;
  (4) the PH operator; (5) the Ramanujan property --- all modulo gauge. The notebook's
  obvious PH Hamiltonian is the quadratic Artin--Schreier transfer matrix; that family is
  supersingular (L13-020), so the first ordinary variety is an elliptic curve.
- Lead: the five items are the running scorecard for genus 1 (06d), genus 2 (06f) and the
  explicit examples (06g). Genus $\ge3$ is only the closed form, and item (1) --- a tensor
  *determined by the variety* rather than by its $L$-polynomial --- remains unanswered above
  genus 1.
- Related: L13-020, L13-026, L13-042, L13-044, L13-052.

### L13-020 The obvious Polya--Hilbert Hamiltonian only exists in the supersingular world
- Source: report/sections/06c_ring_norm_inputs.tex:132-162, claims
  `thm:as-quadratic-supersingular` (proved), `prop:as-finite-order`
- Raised by: the codex prover; the orchestrator's drafted argument was insufficient
- Status at last mention: pursued, positive (and it closes a door)
- Content: every Frobenius eigenvalue of the smooth model of $y^q-y=g(x)$ for quadratic $g$
  is $\sqrt q$ times a root of unity, in every characteristic including 2. So the one place
  the notebook had a manifestly unitary transfer matrix is supersingular throughout. The
  orchestrator's drafted reason ("the entries are roots of unity") was insufficient --- zero
  entries and the normalisation --- and the prover replaced it with the finite order of
  $E_g/\sqrt q$ inside $\mathrm{Sp}(2J,\mathbb F_q)$.
- Lead: none beyond "go to ordinary curves", which is what 06d does.
- Related: L13-019, L13-023, L13-026.

### L13-021 Assumption: the analytic setting for the infinite-bond obstruction
- Source: report/sections/06c_ring_norm_inputs.tex:121-130, claim `asm:kraus-hs-setting`
  (assumed); used at 06e:92-102
- Raised by: the codex prover; reviewer MAJ-2
- Status at last mention: registered as assumed, with the explicit rider "Not established
  for any Riemann cMPS"
- Content: separable $H_\pm$; at each $t>0$ a normal CP map on $B(H_+\oplus H_-)$ with a
  countable bounded block-diagonal Kraus family $K_s = a_s\oplus B_s$ and weakly convergent
  expansion; blocks extending to bounded $S_\pm(t), M(t)$ with $S_\pm$ trace class;
  compression to finite bond subspaces agreeing with compression of the Kraus expansion;
  the odd semigroup having the zeros as eigenmodes with multiplicity.
- Lead: establish (or refute) these hypotheses for an actual Riemann cMPS. Consequence: the
  "fermionic jumps are necessary" theorem (L13-038) would become unconditional, which is the
  notebook's strongest structural claim about the Phantasm.
- Related: L13-038, L13-047, L13-048.

### L13-022 Cut rank of a ring amplitude, and its basis dependence
- Source: report/sections/06c_ring_norm_inputs.tex:164-187, claims `prop:ring-cut-rank`
  (proved), `num:cut-rank-binary`
- Raised by: the codex prover; the reviewer closed the open half (MAJ-1); the orchestrator's
  drafted bound was wrong
- Status at last mention: pursued, resolved
- Content: for letters $A_s\in M_D$, the flattening rank of $\mathrm{Tr}(A_{s_1}\cdots
  A_{s_n})$ across two contiguous arcs is at most $D^2$, sharply, and at most $D^b$ across a
  bipartition cutting $b$ virtual edges; the drafted bound $D$ is the open-chain bound.
  Numerically, over $\mathbb F_2$ the quadratic form $\mathrm{Tr}(x^3)$ has cut rank $\le4$
  in a *self-dual* normal basis but grows (16 at $n=10$) in a plain normal basis, while the
  cubic $\mathrm{Tr}(x^{1+2+4})$ grows $2,4,8,16$. **Cut rank is basis dependent.**
- Lead: none further; but the basis dependence is exactly what makes L13-009 and L13-023
  delicate.
- Related: L13-009, L13-023.

### L13-023 Restricted amplitude locality (conjecture)
- Source: report/sections/06c_ring_norm_inputs.tex:189-198, claim `conj:amplitude-locality`
  (conjectured); scope restricted at 06f:286-294
- Raised by: orchestrator (Claude), restricted after the prover/reviewer round
- Status at last mention: registered as conjectured
- Content: with a self-dual normal-basis prescription for every $n$ and trace-invisible
  Artin--Schreier coboundaries quotiented out, a fixed finite lattice tensor with amplitudes
  $\psi(\mathrm{Tr}\,g(x))$ for all $n$ exists only when the trace function has quadratic
  degree over the prime field. It is a *necessity* conjecture about equation-local
  amplitudes only; the broad slogan "finite tensors give only supersingular zetas" is
  explicitly false.
- Lead: prove or refute. If true it would pin the exact boundary of the MPS formulation of
  the Weil conjectures; the surviving counterexamples to the broad slogan are the elliptic
  and nine-letter norm tensors.
- Related: L13-009, L13-022, L13-050.

### L13-024 Assumption: Deuring lifting
- Source: report/sections/06c_ring_norm_inputs.tex:65-73, claim `asm:deuring-lift` (assumed)
- Raised by: the codex prover
- Status at last mention: registered as assumed
- Content: for $E/\mathbb F_q$ ordinary with Frobenius $\pi$ and $\mathrm{End}(E)=O$ there
  is an elliptic curve over a number field with good reduction to $E$, endomorphism ring
  $O$, reduction an isomorphism on endomorphisms; over $\mathbb C$ it is $\mathbb C/\Lambda$
  with $\Lambda$ a proper $O$-ideal and $\tilde\pi$ multiplication by $\pi$.
- Lead: byte-cite Deuring 1941 or use the Serre--Tate form throughout. It is the hinge of
  the whole genus-one construction.
- Related: L13-026, L13-025.

### L13-025 Assumption: spectral versus Newton supersingularity
- Source: report/sections/06c_ring_norm_inputs.tex:113-119, claim
  `asm:supersingular-newton` (assumed)
- Raised by: the codex prover
- Status at last mention: registered as assumed
- Content: an abelian variety over a finite field has all Newton slopes $\tfrac12$ iff all
  its Frobenius eigenvalues are $\sqrt q$ times roots of unity; a curve is supersingular
  when its Jacobian is. This is what lets `thm:as-quadratic-supersingular` be stated as a
  supersingularity result rather than as a statement about roots of unity.
- Lead: cite. Consequence: none structural.
- Related: L13-020.

### L13-026 The natural genus-one tensor is the lifted Frobenius on the flat torus
- Source: report/sections/06d_ring_norm_elliptic.tex:19-45, claims
  `thm:toral-frobenius-count`, `prop:toral-zeta`
- Raised by: the codex prover (T1)
- Status at last mention: pursued, positive
- Content: with $M$ the integral matrix of the lifted Frobenius, $\#\mathrm{Fix}(M^n) =
  \det(1-M^n) = |1-\pi^n|^2 = N_n$, all fixed points nondegenerate of index $+1$, so $N_n$
  is a Lefschetz number and also the index $|O/(\pi^n-1)O|$, which by Lenstra *is* the point
  group $E(\mathbb F_{q^n})$ as an $O$-module. The dynamical zeta of $(\mathbb T^2,M)$ is
  the Hasse--Weil zeta, so gas side and transfer side are both carried by one dynamical
  system --- but "the bijection is noncanonical".
- Lead: the noncanonicity is the gap: primitive periodic orbits are only *equinumerous* with
  closed points, not canonically matched. A canonical matching would be a real Phantasm
  ingredient.
- Related: L13-019, L13-027, L13-050.

### L13-027 Hodge doubling is the ket/bra doubling; but the physical state has Schmidt rank one
- Source: report/sections/06d_ring_norm_elliptic.tex:48-60, claim
  `thm:hodge-doubling-tensor`
- Raised by: the codex prover
- Status at last mention: pursued, positive with a recorded limitation
- Content: the double of the Hodge ket bond is $H^*(\mathbb T^2,\mathbb C)$ graded by form
  degree, $E = \mathrm{diag}(1,\bar\pi,\pi,q)$, $\Gamma = \mathrm{diag}(1,-1,-1,1)$:
  $(+,+) = H^0$, the mixed lines are $H^{0,1},H^{1,0}$, $(-,-) = H^2$ with eigenvalue $q$,
  the degree. This answers wish-list item (2). The limitation: the fermionic modes are the
  odd-degree forms but the *physical letters are bosonic*, the physical state has Schmidt
  rank one, and its configurations do not enumerate points.
- Lead: find a tensor at genus 1 whose physical configurations *are* the points. None was
  found; the infinite-label attempt is L13-028.
- Related: L13-028, L13-056, L13-066.

### L13-028 The infinite-label Fourier tensor: honest but redundant
- Source: report/sections/06d_ring_norm_elliptic.tex:62-72, claim
  `prop:fourier-shift-flat-trace`
- Raised by: the codex prover
- Status at last mention: pursued, negative in the intended sense
- Content: the pullback $U=M^*$ on $L^2(\mathbb T^2)\otimes\Lambda^*(\mathbb C^2)$ sends
  $e_k\otimes\omega$ to $e_{M^Tk}\otimes\Lambda^*(M^T)\omega$; $k\mapsto M^Tk$ is injective
  of index $q$, *not* a permutation, and its only finite orbit is $\{0\}$. The
  infinite-label tensor $\mathsf A_k = |M^Tk\rangle\langle k|\otimes\mathrm{diag}(1,\pi)$
  has $P$-closed ring vector $(1-\pi^n)|0,\dots,0\rangle$: an honest but redundant physical
  index, since every closed ring except the vacuum mode vanishes.
- Lead: none stated. The diagnosis is that "the shift is not surjective" (06f:277-284), so
  this is not evidence that every variety's tensor is a permutation.
- Related: L13-027, L13-049.

### L13-029 The Polya--Hilbert unitary at genus one, and the missing phase branch
- Source: report/sections/06d_ring_norm_elliptic.tex:74-89, claim `thm:elliptic-ph-unitary`
- Raised by: the codex prover; review item m1 sharpened the derivation
- Status at last mention: pursued, positive with one gap flagged
- Content: $U_{\mathrm{PH}} = q^{-1/2}M^*|_{H^1}$ is unitary iff $|\pi|^2 = q$, which is
  *derived* (the lifted Frobenius is a conformal similarity whose oriented area ratio is its
  covering degree), not assumed --- so the Ramanujan property at genus 1 needs no root-size
  input. The gap: the real PH model $K\otimes_{\mathbb Q}\mathbb R\cong\mathbb C$ with
  $\mathrm{Re}(x\bar y)$ is the real form of $H^1$, not the complex $H^1$, and "a
  self-adjoint logarithm needs a phase branch the curve does not specify".
- Lead: find the phase branch, or accept that the PH *operator* (as opposed to the unitary)
  is not determined by the curve. This is exactly the obstruction to answering wish-list
  item (4) canonically.
- Related: L13-019, L13-045.

### L13-030 Gauge is the lattice basis; complex spectral data forget the ideal classes
- Source: report/sections/06d_ring_norm_elliptic.tex:91-103, claim
  `prop:integral-marking-gauge`; and 06f:242-251
- Raised by: the codex prover; review item m4
- Status at last mention: pursued, positive
- Content: $M$ changes by $\mathrm{GL}_2(\mathbb Z)$ conjugacy under a change of lattice
  basis; its class is an ideal-lattice class of $\mathbb Z[\pi]$ (Latimer--MacDuffee, all
  full ideal lattices, not only invertible ones), and the ordinary classification is
  Waterhouse's torsor. *Complex spectral data forget these classes*: all matrices in the
  isogeny class are $\mathrm{GL}_2(\mathbb C)$-conjugate. The even ket gauge $G\in
  \mathrm{GL}(1|1)$ acts by $G\otimes\bar G$ and fixes all ring norms; exchanging the two
  Hodge embeddings is *not* an even gauge.
- Lead: the arithmetic (ideal class / CM type) is strictly finer than anything the ring
  norms see. If the Phantasm is to be arithmetic, its data must include a marking, not only
  a spectrum.
- Related: L13-046, L13-051.

### L13-031 Digits in base $\pi$: bounded cyclic carries and a finite carry automaton
- Source: report/sections/06d_ring_norm_elliptic.tex:105-118, claim
  `prop:cyclic-digits-carries` (proved)
- Raised by: the codex prover; corrects an orchestrator draft
- Status at last mention: pursued, positive but not useful for counting (see L13-032)
- Content: with $D$ a residue system of $O/\pi O$, every class of $O/\pi^nO$ has a unique
  base-$\pi$ expansion; the cyclic map $D^n\to O/(\pi^n-1)O$ need not be onto (explicit
  counterexample $O=\mathbb Z[i]$, $\pi=1+2i$, i.e. $y^2 = x^3+x$ over $\mathbb F_5$). Two
  words have the same image iff they admit integral cyclic carries $d_i-e_i = \pi c_{i+1} -
  c_i$ with $c_n = c_0$, which are unique and bounded by $\max|d-e|/(\sqrt q - 1)$: the
  cyclic equivalence relation has a *finite* carry automaton. The drafted "carries must be
  unbounded" was wrong.
- Lead: none stated beyond L13-032.
- Related: L13-032.

### L13-032 What finite carries do not count
- Source: report/sections/06d_ring_norm_elliptic.tex:120-129, claim
  `prop:carry-automaton-no-count` (proved)
- Raised by: the codex prover
- Status at last mention: pursued, negative
- Content: no finite weighted adjacency matrix and no trace-class operator has power traces
  $N_n$, so no automaton with nonnegative transition counts counts the classes of
  $O/(\pi^n-1)$ by its unweighted rings. The carry automaton recognises equality of
  represented words, it does not count classes with weight one. A graded signed transfer
  ($\mathrm{diag}(1,q)$ even, $M$ odd) has supertrace $N_n$ but is not by itself a
  doubled-Kraus factorisation.
- Lead: none stated. It is the cleanest small no-go for "the points are the configurations".
- Related: L13-031, L13-027, L13-034.

### L13-033 Dead: the orchestrator's drafted Hilbert--Schmidt/trace bound
- Source: report/sections/06e_ring_norm_bosonic_nogo.tex:17-26, claim
  `obs:drafted-hs-bound-false` (sketched)
- Raised by: orchestrator (Claude); refuted independently by the codex prover and the
  numerics lane
- Status at last mention: pursued, negative (recorded as a correction)
- Content: the 2026-09-14 morning draft claimed $\sum_{\mathrm{odd}}|\mu|^2 \le
  2\,\mathrm{Tr}E_{++}\mathrm{Tr}E_{--}$ for bosonic tensors, and its script computed
  $\sum_s\|a_s\|_{\mathrm{HS}}^2$ while calling it a trace. Since $\mathrm{Tr}(A\otimes\bar
  A) = |\mathrm{Tr}A|^2$, one even letter $a=B=\mathrm{diag}(1,-1)$ on $\mathbb C^{2|2}$ has
  both traces zero and odd squared eigenvalue sum 8; 173 of 400 random instances violate it.
- Lead: none; the genus bound survives via the correct all-power word-trace inequality.
- Related: L13-034.

### L13-034 Bosonic species cannot pass genus one
- Source: report/sections/06e_ring_norm_bosonic_nogo.tex:41-57 (proof 59-66), claims
  `lem:word-trace-cs`, `thm:bosonic-genus-bound`
- Raised by: the codex prover (T3)
- Status at last mention: pursued, positive
- Content: with $s_\pm(n)$ the word-trace sums, $|\mathrm{Tr}M^n|^2 \le s_+(n)s_-(n)$ for
  every $n$. If the nonzero even spectrum is exactly $\{1,q\}$ with no cancellation and the
  odd spectrum is $2g$ values of modulus $\sqrt q$, then writing the eigenvalues of $M$ as
  $\sqrt q\beta_j$ the inequality reads $|\sum_j\beta_j^n|^2\le1$, whose Cesaro mean tends
  to $\sum_i m_i^2 \ge g$, forcing $g\le1$.
- Lead: this is the theorem that *forces* fermions past genus 1, i.e. the notebook's reason
  for a graded bond at all.
- Related: L13-033, L13-036, L13-037, L13-038.

### L13-035 Euler-characteristic bookkeeping and the true minimal bond
- Source: report/sections/06e_ring_norm_bosonic_nogo.tex:68-77, claim
  `prop:euler-bookkeeping` (proved)
- Raised by: the codex prover
- Status at last mention: pursued, positive
- Content: if a graded tensor on $\mathbb C^{m|k}$ has $\mathrm{str}\,E^n = N_n$ with net
  spectrum $\{1,q\}_+ - \{\alpha_{1..2g}\}_-$ and $z_e,z_o$ zero eigenvalues, then
  $(m-k)^2 - (z_e - z_o) = 2-2g$ and necessarily $mk\ge g$; if the odd dimension is exactly
  $2g$ then $mk = g$, no odd zero modes, no cancellation, and $m^2+k^2-2$ nilpotent even
  modes. **The minimal bond dimension is $\min\{m+k: mk\ge g\}$, not generally $g+1$; at
  genus two it is three.**
- Lead: none stated. It is a cheap constraint that should be applied before any numerical
  search at higher genus.
- Related: L13-036, L13-042, L13-043.

### L13-036 Odd letters and cancellation evade the bound --- so the failed bosonic search proves nothing
- Source: report/sections/06e_ring_norm_bosonic_nogo.tex:79-90, claim
  `prop:odd-species-cancellation` (proved)
- Raised by: the codex prover
- Status at last mention: pursued, positive (and it narrows an earlier overclaim)
- Content: odd letters add blocks between $(+,+)$ and $(-,-)$ and between the mixed sectors,
  so $E_{\mathrm{odd}}$ is no longer $M\oplus\bar M$; and with a cancelling multiset $X$ the
  inequality "bounds nothing independent of $X$". Hence fermionic letters are necessary
  **on the minimal genus-two bond $\mathbb C^{1|2}$ (no room to cancel), not on every larger
  bond**; the failed bosonic $\mathbb C^{2|2}$ search is no certificate.
- Lead: if one wants an unconditional "fermions are necessary", one has to rule out
  cancelling multisets on larger bonds. Not done.
- Related: L13-034, L13-035, L13-043, L13-048.

### L13-037 Infinite bond: bosonic species cannot carry the zeros
- Source: report/sections/06e_ring_norm_bosonic_nogo.tex:92-102, claim
  `thm:infinite-bond-bosonic-nogo`
- Raised by: the codex prover
- Status at last mention: pursued, positive but conditional
- Content: under `asm:kraus-hs-setting` and `asm:zero-count-location`, if the odd eigenmodes
  at time $t$ include $e^{t\mu_\rho}$ over the nontrivial zeros, then $\sum_\rho
  e^{2t\mathrm{Re}\mu_\rho} \le \|E_{\mathrm{odd}}(t)\|^2_{\mathrm{HS}} \le
  2\|S_+\|_{\mathrm{HS}}\|S_-\|_{\mathrm{HS}} < \infty$, impossible because the left side
  diverges. Hence a purely bosonic Kraus realisation of the Riemann semigroup does not exist
  and fermionic jumps are necessary in that setting. Recorded caveat: the trace version
  $2\mathrm{Tr}S_+\mathrm{Tr}S_-$ needs $S_\pm$ positive on Hilbert--Schmidt space, which
  complete positivity alone does not give.
- Lead: discharge L13-021 and this becomes the notebook's headline structural statement
  about the Riemann cMPS.
- Related: L13-021, L13-048.

### L13-038 Explicitly not shown: that odd jumps *suffice*
- Source: report/sections/06f_ring_norm_genus_two.tex:265-272, claim
  `obs:fermionic-jumps-necessary` (sketched-conditional)
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued
- Content: excluding the all-even Kraus class does not imply that odd jumps suffice, that
  finitely many do, or that a distributional regularisation is a Hilbert norm; the finite
  supertrace theorem is a finite-bond statement.
- Lead: a sufficiency construction. Consequence if it worked: an actual fermionic cMPS whose
  ring norm is the Riemann count.
- Related: L13-037, L13-047, L13-050.

### L13-039 Dead: the literal geometric placement and the vacuum ansatz at genus two
- Source: report/sections/06f_ring_norm_genus_two.tex:89-99, claim
  `prop:vacuum-ansatz-impossible`
- Raised by: orchestrator (Claude) drafted the ansatz; the codex prover refuted it
- Status at last mention: pursued, negative
- Content: if the odd spectrum is the four Frobenius values and the even spectrum
  $\{1,q,0,0,0\}$, then the pure trace line $0\oplus1_2$ is not a $q$-eigenvector and the
  vacuum line is not invariant --- either would force all $c_f=0$ or all $d_f=0$ and
  contradict the genus bound. Both coupling directions must occur. The drafted ansatz
  $a_1=1,B_1=0,a_2=0,B_2=B$ makes $M=0$ and fails for every curve with $e_1\ne0$.
- Lead: none; it rules out the "put the cohomology where it geometrically belongs" strategy.
- Related: L13-042, L13-043.

### L13-040 Assumption: CM type and the Hodge decomposition of the canonical lift
- Source: report/sections/06f_ring_norm_genus_two.tex:52-61, claim `asm:cm-hodge-type`
  (assumed)
- Raised by: the codex prover
- Status at last mention: registered as assumed
- Content: for a simple ordinary $A/\mathbb F_q$ of dimension $g$, $K=\mathbb Q(\pi)$ is CM
  of degree $2g$, $\mathrm{End}(A)\otimes\mathbb Q = K$, and $H^1(\tilde A(\mathbb C),
  \mathbb C) = \bigoplus_\phi \mathbb C_\phi$ with $H^{1,0} = \bigoplus_{\phi\in\Phi}
  \mathbb C_\phi$. Explicitly flagged: "the eigenspace statement is not quotable from the
  fetched TeX".
- Lead: fetch a quotable Shimura--Taniyama source.
- Related: L13-041, L13-045.

### L13-041 Assumption bundle: polarised lift, Hodge adjunction, Jacobian comparison, real closure, functoriality
- Source: report/sections/06f_ring_norm_genus_two.tex:63-75, claim `asm:cm-polarised-lift`
  (assumed)
- Raised by: the codex prover
- Status at last mention: registered as assumed (four separate items in one row)
- Content: (i) a polarisation lifts along the canonical lift and identifies Rosati
  adjunction with adjunction for the positive Hodge form on $H^{1,0}$, plus the
  curve-in-Jacobian comparison facts; (ii) $H^*(A) = \Lambda^*H^1(A)$ with Frobenius acting
  by exterior powers; (iii) a finite real semialgebraic system with a real solution has a
  real algebraic solution; (iv) multiplicativity of Frobenius characteristic polynomials in
  exact sequences, and preservation of ordinarity under finite base extension.
- Lead: split and discharge. Item (iii) is what makes the three-letter feasibility statement
  ("then an algebraic solution exists") meaningful.
- Related: L13-043, L13-045, L13-050.

### L13-042 The nine-letter closed-form tensor, and its arbitrariness
- Source: report/sections/06f_ring_norm_genus_two.tex:103-119, claim
  `thm:nine-letter-tensor`
- Raised by: the codex prover (T4/T5)
- Status at last mention: pursued, positive with an honesty rider
- Content: for $q+1\ge4\sqrt q$ (every prime power $q\ge16$) an explicit nine-letter tensor
  on $\mathbb C^{1|2}$ has even spectrum $\{1,q,0,0,0\}$, odd block $\mathrm{diag}(\bar
  D,D)$, normal transfer, and $\mathrm{str}\,E^n = N_n(C)$ for every $n$. The even letters
  realise the depolarising map, the odd letters couple vacuum and trace, and neither
  eigenvector is the pure vacuum nor the pure polarisation line. It generalises to
  $\mathbb C^{1|g}$ with $w=(q+1)/2g$, $h=(q-1)/(2\sqrt g)$ whenever $q+1\ge2g\sqrt q$.
  Rider: "the letters have no equation-local meaning and their number is not claimed
  minimal."
- Lead: find letters that *do* have equation-local meaning, i.e. answer wish-list item (1)
  at genus $\ge2$. Consequence: the tensor would be determined by the curve rather than by
  its $L$-polynomial.
- Related: L13-019, L13-023, L13-044, L13-052.

### L13-043 The three-letter problem as a finite real feasibility problem, and the one certified curve
- Source: report/sections/06f_ring_norm_genus_two.tex:131-156, claims
  `prop:three-letter-feasibility`, `thm:f5-certified-tensor`
- Raised by: the codex prover; the numerics lane supplied the seed
- Status at last mention: pursued, positive for one curve
- Content: two even and one odd letter on $\mathbb C^{1|2}$ realise $N_n(C)$ for all $n$ iff
  two characteristic polynomials match (28 real unknowns), and then an algebraic solution
  exists. For $y^2 = x^5+x^3+x^2-2$ over $\mathbb F_5$ an exact rational Newton--Kantorovich
  contraction certificate proves existence in a box of radius $10^{-30}$. Explicit
  methodological warning: "Least-squares residuals and four-digit printouts certify nothing."
- Lead: "This is a computer-assisted existence proof for one curve, not a formula." The next
  step is the universal statement, L13-044.
- Related: L13-044, L13-041, L13-053.

### L13-044 Universal three-letter tensor (conjecture)
- Source: report/sections/06f_ring_norm_genus_two.tex:158-165, claim
  `conj:three-letter-universal` (conjectured)
- Raised by: the codex prover / orchestrator
- Status at last mention: registered as conjectured, both parts open
- Content: (a) for every ordinary simple genus-two curve the three-letter feasibility problem
  has a solution; (b) some solution is selected *naturally* by the equation or by the
  polarised CM data. Explicit caveat: "failed smaller-alphabet searches prove no lower bound
  on the number of letters."
- Lead: part (b) is the real prize --- it is wish-list item (1) at genus two. A natural
  selection rule would make the tensor a functor of the curve.
- Related: L13-019, L13-042, L13-043, L13-046.

### L13-045 Rosati positivity supplies the moduli and the Polya--Hilbert metric; the gauge question left open
- Source: report/sections/06f_ring_norm_genus_two.tex:224-240, claim
  `thm:rosati-ph-genus-two`
- Raised by: the codex prover
- Status at last mention: pursued, positive with one explicit gap
- Content: for a simple ordinary polarised abelian variety, Rosati acts as complex
  conjugation on each factor of $K\otimes\mathbb R\cong\prod_j\mathbb C$, so $\pi\pi^\dagger
  = q$ gives $|\phi_j(\pi)|^2 = q$ at every place and $q^{-1/2}\tilde\pi^*$ is unitary on
  $H^{1,0}$: the root sizes come from positivity with no use of the Weil conjectures. But:
  "in `thm:nine-letter-tensor` the odd block is $\sqrt q$ times a unitary by construction, so
  RH is manifest only after the moduli are supplied; the arithmetic proof of those moduli is
  Rosati (Hodge index on $C\times C$), not complete positivity of a transfer." And for the
  certified tensor, "whether that similarity is an even ket gauge carrying the arithmetic
  Hodge metric is not determined by the count equations."
- Lead: decide the gauge question for the certified $\mathbb F_5$ tensor. Consequence: it
  would say whether the *count equations alone* can carry the arithmetic metric, which is
  the crux of whether a transfer operator can prove RH.
- Related: L13-029, L13-030, L13-004, L13-011.

### L13-046 CM types are markings, not gauge
- Source: report/sections/06f_ring_norm_genus_two.tex:242-251, claim `prop:cm-type-gauge`
- Raised by: the codex prover
- Status at last mention: pursued, positive
- Content: the even gauge $G=\mathrm{diag}(g_0,H)$ fixes all ring norms; same-parity unitary
  rotations of the letters fix $E$ itself. But replacing a selected $\pi_j$ by $\bar\pi_j$
  changes the mixed-sector eigenvalues and is not an even gauge; a coupled solution with
  $N\ne0$ mixes the two coherences and its counts do not recover a marked half.
- Lead: none stated; it is the genus-two version of L13-030 and constrains what "modulo
  gauge" in TJO's wish list can mean.
- Related: L13-030, L13-044.

### L13-047 Candidate Phantasm bond: $\mathbb C \oplus H_{>0}$, one odd mode per positive-height zero
- Source: report/sections/06f_ring_norm_genus_two.tex:255-263, claim
  `obs:phantasm-bond-candidate` (sketched-conditional)
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued (labelled observation, deliberately not a
  theorem)
- Content: a plausible ket is $\mathbb C\oplus H_{>0}$ with one odd mode per positive-height
  zero, the bra supplying the conjugates. Two problems are stated in the same breath: its
  $(-,-)$ sector is far larger than the pole sector and what kills or regularises those modes
  is unspecified; and ket/bra exchange is complex conjugation, whereas the functional
  equation also involves $\rho\mapsto1-\rho$, which coincides with conjugation on each pair
  *only on the critical line* --- so **reading the functional equation as ket/bra exchange
  would assume RH**.
- Lead: find the regularisation of the $(-,-)$ sector, and a symmetry that implements
  $\rho\mapsto1-\rho$ without presupposing RH. This is the most direct Phantasm lead in the
  lane.
- Related: L13-038, L13-050, L13-093.

### L13-048 The genus-two ring norms are Hilbert norms of fermionic ring states
- Source: report/sections/06f_ring_norm_genus_two.tex:197-206, claim
  `cor:genus-two-physical-norm` (sketched-conditional)
- Raised by: the codex prover / orchestrator
- Status at last mention: registered as sketched-conditional
- Content: via `thm:cmps-twisted-supertrace` on the lattice, the supertraces of the
  nine-letter and certified tensors are the squared norms of physical periodic-fermion
  rings; the explicit Jordan--Wigner check confirms it for $n\le5$. So "the count of a
  genus-two curve is literally the norm of a graded matrix product state with a
  three-dimensional bond and a fermionic letter."
- Lead: upgrade `thm:cmps-twisted-supertrace` from sketched. Consequence: item (3) of the
  wish list becomes a theorem at genus two.
- Related: L13-019, L13-056.

### L13-049 The curve sits inside the Jacobian as a non-product boundary
- Source: report/sections/06f_ring_norm_genus_two.tex:210-222, claim
  `prop:jacobian-curve-projector`
- Raised by: the codex prover
- Status at last mention: pursued, positive
- Content: the tensor product of two elliptic norm tensors has ring norm $\#J(\mathbb
  F_{q^n})$; inside it the Frobenius-invariant graded subspace $\mathcal S = \mathbb C 1
  \oplus H^1(J)\oplus\mathbb C\omega$ has $\mathrm{str}\,F^n|_{\mathcal S} = N_n(C)$. But
  the rank-six projector onto $\mathcal S$ is *not* of the form $B\otimes\bar B'$ (a product
  range would have dimension $\ge9$): extracting the curve from the Jacobian ring needs a
  non-product boundary, which the single fermionic rings avoid. Explicit rider: "This does
  not say every boundary with the same scalar counts is that projector."
- Lead: the "bosonic product of tori plus a non-product boundary" is an alternative
  architecture for higher genus that was not developed.
- Related: L13-026, L13-042.

### L13-050 The locality dichotomy must be restricted; the infinite-bond cMPS is only motivated
- Source: report/sections/06f_ring_norm_genus_two.tex:286-294, claim
  `obs:locality-dichotomy-restricted` (sketched-conditional)
- Raised by: orchestrator (Claude), self-correction
- Status at last mention: correction applied; the positive programme not pursued
- Content: "Fixed finite lattice tensors give only supersingular zetas" is false --- the
  Hodge doubling tensor and the nine-letter tensor are finite ordinary norm tensors. Only
  the equation-local amplitude question survives, as `conj:amplitude-locality`. And:
  "Infinitely many zeros and dilation time motivate an infinite-bond cMPS, but supply none
  of the domains, regularised trace, tensor factorisation or positivity it would need."
- Lead: supply exactly those four things. That is the analytic core of the Phantasm.
- Related: L13-023, L13-021, L13-047.

### L13-051 Base change as a trick to enter the closed-form regime
- Source: report/sections/06f_ring_norm_genus_two.tex:121-129, claim `prop:f5-base-change`
- Raised by: the codex prover
- Status at last mention: pursued, positive
- Content: the $\mathbb F_5$ curve has $\chi_F = z^4-3z^3+7z^2-15z+25$, below the
  nine-letter threshold; over $\mathbb F_{25}$ the threshold $q+1\ge4\sqrt q$ is met and the
  closed form applies, with first six norms $31,619,15991,390739,9759526,244128859$. Both
  quartics are irreducible over $\mathbb Q$ so both Jacobians are simple; ordinarity is
  preserved.
- Lead: base change is a general way to reach the closed form for any curve. It changes the
  field, so it does not answer the small-$q$ question.
- Related: L13-042, L13-043.

### L13-052 TJO's question: one explicit MPS per genus
- Source: report/sections/06g_ring_norm_examples.tex:12-22 ("Question (TJO, 2026-09-14,
  evening")
- Raised by: TJO
- Status at last mention: pursued, answered
- Content: how hard is it to describe a specific example of each genus and write down the
  actual matrices, and what are their usual entanglement properties and parent Hamiltonians?
  Answer: genus 0 and 1 are one-liners, genus 2 is the closed form above $q\ge16$ and the
  certified decimals below, and every genus $g$ is the same closed form on $\mathbb C^{1|g}$
  once $q+1\ge2g\sqrt q$. "The only input at every genus is the $L$-polynomial."
- Lead: that last clause is the standing limitation --- the construction consumes the
  answer. Compare L13-042's rider about equation-local meaning.
- Related: L13-019, L13-042.

### L13-053 RH for a curve as a single odd correlation length
- Source: report/sections/06g_ring_norm_examples.tex:43-56, claim
  `prop:example-correlation-lengths` (sketched-conditional)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched-conditional
- Content: for any graded tensor with net even spectrum $\{1,q\}$ and odd spectrum the
  Frobenius eigenvalues, the even correlation length is $1/\log q$ and an odd mode
  $\alpha_j$ has $1/\log(q/|\alpha_j|)$. Hence **RH for the curve is the statement that
  every odd (fermionic) mode has the same correlation length $2/\log q$, exactly twice the
  even one.** Verified to $10^{-6}$ in the five examples.
- Lead: none stated. It is the cleanest physical restatement of the RH analogue in the book
  and the natural thing to try to prove by a physical argument (a Lieb--Robinson or
  area-law-style bound on the odd sector).
- Related: L13-054, L13-055.

### L13-054 Block Schmidt spectrum of a twisted ring from the doubled bond
- Source: report/sections/06g_ring_norm_examples.tex:60-80 (proof 73-80), claim
  `prop:example-block-spectrum` (sketched)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched
- Content: for a graded tensor with Kronecker contraction, the reduced state of a contiguous
  $l$-site block in a $P$-closed ring of length $n$ has at most $D^2$ nonzero Schmidt
  weights, equal to the spectrum of $K G_X^T$ with $G_X$ and $K$ built from $E^l$ and
  $E^{n-l}\Gamma$; block entropy is at most $2\log D$. The fermionic (Jordan--Wigner) reduced
  state has the same spectrum, because the string acting on the block is a parity sign.
- Lead: none stated; the formula is the tool for L13-055.
- Related: L13-053, L13-055.

### L13-055 What the entanglement looks like at each genus
- Source: report/sections/06g_ring_norm_examples.tex:82-100, claim
  `obs:example-entanglement` (sketched)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched
- Content: genus 0 is a cat state of two orthogonal product states, Schmidt rank two, entropy
  vanishing exponentially, GHZ-like doubly degenerate parent Hamiltonian; genus 1 is a
  *product state*, zero entanglement, the whole count in the normalisation; genus $\ge2$
  saturates a flat spectrum (exactly $\{\tfrac14,\tfrac18^{\times4},\tfrac1{16}^{\times4}\}$
  for the nine letters over $\mathbb F_{25}$; $\{\tfrac14,\tfrac1{12}^{\times6},
  \tfrac1{36}^{\times9}\}$ at genus 3), the signature of depolarising even letters. "The odd
  sector contributes to the entanglement only through the doubled bond."
- Lead: none stated. The genus-1 product state is a warning that entanglement is not where
  the arithmetic lives in the current tensors; a tensor where it *is* would be new.
- Related: L13-027, L13-053, L13-069.

### L13-056 Parent Hamiltonians: one local Hamiltonian with Ramond and Neveu--Schwarz boundary conditions
- Source: report/sections/06g_ring_norm_examples.tex:104-125, claim
  `prop:example-parent-hamiltonian` (sketched)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched, numerically checked
- Content: with $h = 1 - \Pi_{S_k}$ and $H = \sum_i h_i$ wrapping the ring, every ring
  $\Psi_B$ with $B$ commuting with the letters is annihilated by the non-wrapping terms;
  the wrapping term sees $B$. When odd letters are present, $A_sPA_t = \eta_s PA_sA_t$, so
  $\Psi_P$ is the ground state exactly of the Hamiltonian whose wrapping terms are conjugated
  by the site parities (the Jordan--Wigner image of the periodic fermion ring), and $\Psi_1$
  (antiperiodic) of the untwisted one. The fermionic parent Hamiltonian is *one* local
  Hamiltonian with two boundary conditions.
- Lead: the twisted/untwisted gap pair was measured (0.239 / 0.232 for the certified genus-2
  letters; 0.639 / 0.636 for the nine letters). A gap that stays open in the thermodynamic
  limit would be a physical handle on the curve's zeta.
- Related: L13-048, L13-057.

### L13-057 The genus-three parent Hamiltonian was not diagonalised
- Source: report/sections/06g_ring_norm_examples.tex:141-142, claim `num:ring-norm-examples`
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not run
- Content: "genus 3 has sixteen letters and its parent Hamiltonian is not diagonalised."
- Lead: run it; it would extend the gap data of L13-056 to a third genus and test whether
  the gap shrinks with $g$.
- Related: L13-056.

### L13-058 TJO's question: impose every zeta condition factor by factor
- Source: report/sections/06h_zeta_conditions.tex:12-19 ("Question (TJO, 2026-09-14,
  night")
- Raised by: TJO
- Status at last mention: pursued, delivered as a ledger plus a catalogue
- Content: line up all the conditions a zeta should obey (functional equation,
  RH/Ramanujan, unique fixed point, ...) and impose them factor by factor on the cMPS ring
  norm, including tiny $L$-functions; the deliverable is completely concrete MPS/cMPS that
  any practitioner would understand. Delivered by one codex `gpt-6-astra` lane (1882-line
  report, 13 scripts, 461 checks) plus 26 orchestrator re-derivations.
- Lead: **the whole shard is unreviewed by a second model family; every row is
  `sketched`/`numerical`** (06h:19). Getting it reviewed is the stated next step.
- Related: L13-059 … L13-070.

### L13-059 The ten zeta conditions as exact algebraic statements (C1--C10)
- Source: report/sections/06h_zeta_conditions.tex:27-63, claim `obs:zeta-condition-ledger`
  (sketched)
- Raised by: the codex prover lane, framed by TJO's question
- Status at last mention: registered as sketched
- Content: C1 positivity automatic, integrality separate; C2 "genuine gas" ($a_d =
  \frac1d\sum_{e|d}\mu(d/e)N_e \in \mathbb Z_{\ge0}$) *not* automatic; C3 rationality
  automatic, poles net even and zeros net odd; C4 FE as parity-preserving invariance under
  $\lambda\mapsto q/\lambda$, with the visible mechanism $J\Gamma=\Gamma J$,
  $JEJ^{-1}=qE^{-1}$, additive $\lambda\mapsto\kappa-\lambda$ for cMPS; C5 RH as
  $|\lambda|^2=q$ with a positive metric $M$, $E|_-^\dagger M E|_- = qM$, necessary if
  semisimple; C6 *three* separate requirements (simple Perron root, a trace-preserving gauge
  on the whole bond, mixing); C7 Galois grading and Artin $L$-functions; C8 sign structure
  automatic; C9 physical realisability, including cMPS kinetic regularity $R_aR_b=\pm
  R_bR_a$, $R_f^2=0$; C10 exact lattice-in-cMPS embedding needs $E = e^{h T}$ with Choi
  conditional positivity.
- Lead: each condition is now a testable algebraic property of a tensor, so a search for a
  tensor satisfying all ten simultaneously is well posed. Nobody ran that search.
- Related: L13-060 … L13-070.

### L13-060 Correction: inverse-closed letters do not give the functional equation
- Source: report/sections/06h_zeta_conditions.tex:39-43 (C4)
- Raised by: the codex prover lane, correcting the reading of shard 08b
- Status at last mention: correction applied
- Content: inverse-closed letters do *not* give the FE for the raw doubled transfer. Explicit
  counterexample: $B=\mathrm{diag}(1,2)$, $B^{-1}$ gives even spectrum $\{2,17/4\}$, odd
  $\{5/2,5/2\}$. The reciprocal quadratics arise in the *non-backtracking* construction after
  the Bass factors are removed.
- Lead: none; it sharpens where the FE actually comes from.
- Related: L13-010, L13-086, L13-070.

### L13-061 E0: a zero from destructive interference with a subshift
- Source: report/sections/06h_zeta_conditions.tex:67-81, claim `prop:e0-pair-shift`
  (sketched)
- Raised by: the codex prover lane
- Status at last mention: registered as sketched
- Content: letters $K_{(a,b)} = \mathrm{diag}(1,[a=b])$ on $\mathbb C^{1|1}$ give $N_n =
  m^{2n}-m^n$, $Z = (1-mu)/(1-m^2u)$: one pole at $1/m^2$, one *zero* at $1/m = q^{-1/2}$
  ("RH by half entropy"), a genuine gas, no FE, no whole-bond channel gauge. For $m=2$ it
  equals $Z(\mathbb A^1/\mathbb F_4)/Z(\mathbb A^1/\mathbb F_2)$ in an identified degree
  variable. Correction recorded: "the swap is a symmetry with fixed letters, not an Artin
  cover."
- Lead: the mechanism "a zero is the removal of a full subshift" is a candidate for how
  fermionic zeros should arise generally.
- Related: L13-065, L13-070.

### L13-062 Four-letter trace-preserving elliptic tensors with FE, RH and mixing by visible mechanisms
- Source: report/sections/06h_zeta_conditions.tex:83-107, claim `prop:four-letter-elliptic`
  (sketched-conditional)
- Raised by: the codex prover lane
- Status at last mention: registered as sketched-conditional
- Content: four explicit Kraus letters on $\mathbb C^{1|1}$ give $\sum K_s^\dagger K_s = q$,
  even spectrum $\{q,r\}$, odd $\{\pi,\bar\pi\}$, Ramond norm $r+q^n-\pi^n-\bar\pi^n$ --- the
  affine ($r=0$) or projective ($r=1$) elliptic count. For $r=1$ the FE comes from an
  explicit duality $J$, RH from $E|_-^\dagger E|_- = q$, and the normalised channel is
  *mixing with the maximally mixed state as its unique fixed point*. This fixes C6, which
  the bare $\mathrm{diag}(1,\pi)$ tensor fails, without changing $Z$.
- Lead: this is the notebook's best small "all conditions at once" object; testing whether
  the pattern extends to higher genus is the obvious next step.
- Related: L13-059, L13-042.

### L13-063 FE, RH and mixing are mutually independent
- Source: report/sections/06h_zeta_conditions.tex:109-124, claim
  `prop:fe-rh-mixing-independent` (sketched)
- Raised by: the codex prover lane
- Status at last mention: registered as sketched
- Content: with Pauli letters $\sqrt{c_i}\{1,Z,X,Y\}$ on $\mathbb C^{1|1}$ the even spectrum
  is $\{16,r\}$ and the odd $\{x,y\}$, and four parameter choices realise (FE,RH,mixing) =
  (Y,Y,Y), (Y,N,Y), (N,Y,Y), (N,N,Y); tensoring with an idle even qubit keeps FE and RH and
  destroys uniqueness. The one excluded combination is (FE=N, RH=Y) with the exact projective
  pair $\{1,q\}$, since RH already makes the odd multiset reciprocal. **Positivity of norms
  plus FE does not force RH.**
- Lead: none stated; it is a negative structural result that constrains any attempt to derive
  RH from the other conditions.
- Related: L13-085, L13-059.

### L13-064 Tiny $L$-functions as MPS: Horner, Gauss, Kloosterman, graph cover
- Source: report/sections/06h_zeta_conditions.tex:126-155, claim `prop:tiny-l-functions`
  (sketched)
- Raised by: the codex prover lane; corrects two orchestrator drafts
- Status at last mention: registered as sketched
- Content: (i) a Horner MPS on bond $\mathbb F_q[x]/M$ with letters $f\mapsto xf+c$ produces
  Dirichlet $L$-polynomials over $\mathbb F_2$ and $\mathbb F_3$ with $|\lambda|^2 = q$; (ii)
  a Gauss factor $1+iu\sqrt3$; (iii) a Kloosterman factor over $\mathbb F_4$ realised as the
  affine count of $y^2+xy = x^3+1$; (iv) a $\mathbb Z/2$ voltage graph cover with an Artin
  decomposition. Two corrections: closing the Horner automaton into a trace imposes a return
  condition and *is wrong* (the ring presentation is the Euler product over prime
  polynomials); and "the correct tiny $\mathbb Z/2$ Artin example is a directed voltage cover
  ..., not the drafted square root for the pair shift".
- Lead: the Horner construction is the notebook's only *open-chain* $L$-function MPS; whether
  a genuine ring (trace) presentation of a Dirichlet $L$-function exists is left open.
- Related: L13-061, L13-065, L13-120.

### L13-065 Correction: "even = trivial, odd = nontrivial" is geometric input, not a theorem
- Source: report/sections/06h_zeta_conditions.tex:51-56 (C7)
- Raised by: the codex prover lane
- Status at last mention: correction applied
- Content: a unitary $G$-action commuting with the closure and permuting letters splits
  $E = \oplus_\chi 1\otimes E_\chi$ and $Z = \prod L(u,\chi)^{\dim\chi}$. But calling a
  factor an Artin $L$-function needs an actual cover with Frobenius weights on primitive
  orbits; and "even = trivial, odd = nontrivial" is geometric input (curves), not a theorem
  about group actions --- the Ihara cover in the catalogue has *every* mode even.
- Lead: this is a direct caution for the character-sector grading of L13-014: it works for
  curves for a geometric reason, not automatically.
- Related: L13-014, L13-126.

### L13-066 A literal count state needs $\mathrm{Tr}(\Pi K_w) \in \{0,1\}$
- Source: report/sections/06h_zeta_conditions.tex:56-60 (C9)
- Raised by: the codex prover lane
- Status at last mention: raised in passing
- Content: Choi positivity per parity block plus parity covariance gives homogeneous Kraus
  letters; but a *literal* count state (configurations = points) needs
  $\mathrm{Tr}(\Pi K_w)\in\{0,1\}$, and "the curve tensors are weighted norms, not point
  enumerations".
- Lead: search for tensors with 0/1 word traces realising a curve count. That is the missing
  link between the gas picture and the transfer picture; the genus-0 example (06g:28-31) is
  the only place in the lane where "the configurations are the points".
- Related: L13-027, L13-032, L13-055.

### L13-067 Exact lattice-in-cMPS embedding, and Poissonisation
- Source: report/sections/06h_zeta_conditions.tex:60-62 (C10)
- Raised by: the codex prover lane
- Status at last mention: raised in passing
- Content: exact embedding of a lattice channel in a cMPS needs $E = e^{hT}$ with Choi
  conditional positivity; a singular $E$ (the affine tensor) has none. Poissonisation
  $Q = -c/2$, $R_s = K_s$ always exists but changes FE/RH.
- Lead: the discrete-to-continuum passage is therefore not free. Any Phantasm that starts
  from a lattice model and wants dilation time has to face this.
- Related: L13-068, L13-050.

### L13-068 Two explicit cMPS: half entropy, and an additive functional equation
- Source: report/sections/06h_zeta_conditions.tex:157-177, claim `prop:cmps-half-and-fe`
  (sketched)
- Raised by: the codex prover lane
- Status at last mention: registered as sketched
- Content: (i) $Q=\tfrac12$, $R=\mathrm{diag}(1,0)$ gives $N(L) = e^{2L}-e^L$; a normalised
  finite-norm alternative gives $N(L) = 1-e^{-L}$ but fails kinetic regularity, and "on
  homogeneous regular $\mathbb C^{1|1}$ data, regularity, Lindblad normalisation, uniqueness
  and the exact half difference cannot all hold". (ii) one lowering fermion $R = \sqrt2
  |0\rangle\langle1|$, $H=\mathrm{diag}(0,1)$ gives ring zeta $((z-1)^2+1)/(z(z-2))$ with
  additive FE $\mathcal Z(2-z) = \mathcal Z(z)$ and both zeros on $\mathrm{Re}\,z = 1$: FE,
  RH and unique fixed point by one visible mechanism (odd damping is half the population
  decay, the frequency comes from $H$).
- Lead: recorded limitation --- "the ring vector has only its vacuum amplitude: the zeta data
  sit in the length-dependent vacuum normalisation, and no nontrivial entanglement spectrum
  is produced." Making a cMPS whose zeta data live in the state, not the normalisation, is
  the open task.
- Related: L13-055, L13-067, L13-069.

### L13-069 What a finite bond cannot reach
- Source: report/sections/06h_zeta_conditions.tex:179-199, claim
  `obs:factor-by-factor-limits` (sketched-conditional)
- Raised by: the codex prover lane
- Status at last mention: registered as sketched-conditional; standing limitation
- Content: a finite bond can have infinitely many Euler primes (E0 does) but cannot produce a
  nonrational $Z$, an atomic prime comb, or infinitely many distinct divisor points:
  $u = q^{-s}$ gives periodic copies of finitely many points, not Riemann's zeros. Also: the
  bosonic no-go concerns plain power traces and graded norms evade it by negative net
  coherence multiplicities; a single simple pole at $1/q$ is incompatible with the
  uncompleted self-reciprocal FE, so the completion must be declared. Factor by factor "does
  not make an infinite product converge, supply the continuation or the archimedean factor,
  select an entanglement spectrum, or prove RH for an unidentified infinite object."
- Lead: the list is a specification for what an infinite-bond construction must add.
- Related: L13-050, L13-059, L13-068.

### L13-070 The lane's correction ledger D1--D8
- Source: report/sections/06h_zeta_conditions.tex:195-199
- Raised by: the codex prover lane, correcting orchestrator drafts
- Status at last mention: corrections applied
- Content: four named items are quoted: inverse pairing alone gives no FE; the swap
  $L$-function was not an Artin factor; unique stationarity, gauge and mixing are three
  conditions, not one; the affine rung needs its own tensor.
- Lead: none; recorded as a dead-route list.
- Related: L13-060, L13-061, L13-062, L13-065.

### L13-071 What varieties have that graphs lack: products, slicing, the sign
- Source: report/sections/07_deligne_via_graphs.tex:92-99, 212-243, 269-277, claim
  `obs:deligne-ingredients` (sketched)
- Raised by: orchestrator (Claude), expository
- Status at last mention: registered as sketched; standing diagnosis
- Content: there is no theorem that a $(q+1)$-regular graph is Ramanujan --- most are not,
  the prism is a counterexample --- so the right question is what varieties have that graphs
  lack. Three things: varieties can be *multiplied*, *sliced* over a curve, and their
  interesting eigenvalues enter the count with a *minus sign*. A graph has none of the three.
  A Hilbert--Polya approach would have to replace all three.
- Lead: supply an operation on the Riemann channel under which eigenvalues multiply while the
  trivial loss stays fixed. That is the missing "product".
- Related: L13-004, L13-011, L13-073, L13-074, L13-077.

### L13-072 The abelian obstruction is inside Deligne's proof
- Source: report/sections/07_deligne_via_graphs.tex:163-193, claim `obs:abelian-obstruction`
  (sketched)
- Raised by: orchestrator (Claude), connecting to the founding session
- Status at last mention: registered as sketched
- Content: commuting holonomies produce uncontrolled invariants in tensor powers, exactly as
  commuting Kraus unitaries never give an expander: a common eigenvector with eigenvalue
  $\chi(w)$ becomes invariant in $\hol^{\otimes N}$ as soon as $\chi^N=1$, carrying an
  unknown scalar, so the trivial poles sit where the argument cannot control them. The same
  obstruction appears on both sides of the dictionary.
- Lead: "**Any Ramanujan lift of the prime dilations must break the commutativity by a
  quotient**, as LPS does with the arithmetic lattice and as Deligne does with the shears of
  a generic slicing." That is a concrete design constraint on the Phantasm: the prime
  dilations commute, so the lift cannot.
- Related: L13-071, L13-002, L13-144.

### L13-073 $\zeta$ has the sign and the positivity but not the product
- Source: report/sections/07_deligne_via_graphs.tex:279-284
- Raised by: orchestrator (Claude)
- Status at last mention: standing diagnosis ("the standard diagnosis, stated in the terms of
  this section")
- Content: the zeros are subtracted from the prime count, so $\zeta$ is on the *curve* side
  of the table, not the graph side, and the positivity $\Lambda(n)\ge0$ is the right kind.
  The sign and the positivity are present; the product is absent, since there is no
  $X\times X$ with $\zeta$ as its slice, so the "multiply" step has nothing to act on.
- Lead: find the missing product. If one existed, Deligne's engine (count, fixed loss, roots)
  would run on $\zeta$.
- Related: L13-071, L13-074.

### L13-074 The sign: poles versus zeros, and why positivity bounds only one of them
- Source: report/sections/07_deligne_via_graphs.tex:46-73, 195-210
- Raised by: orchestrator (Claude), expository
- Status at last mention: standing framing
- Content: graph and curve match in every row except the sign of the error term, hence
  whether the interesting eigenvalues are poles or zeros. On the graph side positivity
  constrains the sum of everything, which is the Perron bound and no more; on the curve side
  the interesting eigenvalues are *subtracted*, so positivity bounds them above by the
  trivial ones and even tensor powers squeeze to equality. "The two-loop bouquet is not a
  curve because its walk counts cannot be written with the interesting part subtracted."
- Lead: none stated. It is the reason the whole notebook wants *graded* (supertrace) objects:
  a minus sign in the count.
- Related: L13-014, L13-073, L13-113, L13-126.

### L13-075 The two-loop bouquet counterexample to Deligne's pointwise theorem for graphs
- Source: report/sections/07_deligne_via_graphs.tex:153-161
- Raised by: orchestrator (Claude), from the note
- Status at last mention: settled example
- Content: $\hol(a) = \binom{2\ 1}{1\ 1}$, $\hol(b) = \binom{1\ 1}{1\ 2}$ satisfy (a)
  integral traces, (b) determinant 1 pairing with weight 1, and (c) big monodromy inside
  $\mathrm{SL}_2(\mathbb Z)$ --- yet $\hol(a)$ has eigenvalue $(3+\sqrt5)/2>1$, so the twist
  is not pure. It breaks the third step, and must, since the theorem is false for graphs.
- Lead: none; it is the diagnostic that isolates which step of Deligne's argument a
  channel-based approach would have to supply.
- Related: L13-071, L13-074, L13-076.

### L13-076 A quantum expander is a Ramanujan twist of a bouquet
- Source: report/sections/07_deligne_via_graphs.tex:114-131
- Raised by: orchestrator (Claude)
- Status at last mention: framing, used throughout
- Content: the quantum Ihara zeta is the Artin--Ihara $L$-function of a bouquet of $D$ loops
  with $\hol = \mathrm{Ad}(U_i)$ on the $i$-th loop; a quantum expander is a *Ramanujan twist
  of a bouquet*. Two kinds of side-B eigenvalue then live together: the global ones
  (eigenvalues of the twisted edge operator, poles of $L$) and the pointwise ones
  (eigenvalues of each $\hol(\gamma)$), and "pure with constant $w$" means every pointwise
  eigenvalue of every prime cycle has modulus $w^{\ell(\gamma)}$.
- Lead: the global/pointwise distinction has not been exploited for channels; a "pointwise
  purity" condition on $\mathrm{Ad}(U_\gamma)$ would be a strictly different requirement from
  the Ramanujan bound on $\Sigma$.
- Related: L13-079, L13-075.

### L13-077 Ramanujan without Hermiticity is possible
- Source: report/sections/07_deligne_via_graphs.tex:245-256, 293-296
- Raised by: orchestrator (Claude)
- Status at last mention: standing steering conclusion
- Content: Deligne's proof exhibits no Hermitian structure --- no form, no operator, only
  positivity and a limit. Weil's proof for curves does (Hodge index on $C\times C$), and
  Grothendieck's plan (standard conjectures) is still open. Both Deligne's route and the
  interlacing route (Marcus--Spielman--Srivastava) reach the spectral bound with no
  Hilbert--Polya operator. "For the steering question of where Hermiticity enters, this is
  the cleanest evidence that it need not enter at all; what must enter is a positivity plus
  an operation under which eigenvalues multiply at fixed loss."
- Lead: stop looking for a Hermitian form; look for positivity plus a multiplying operation.
  This is the single most consequential steering statement in the lane.
- Related: L13-071, L13-073, L13-092.

### L13-078 Rankin--Selberg as the number-field shadow of the pointwise theorem
- Source: report/sections/07_deligne_via_graphs.tex:285-290
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued
- Content: for a modular form the Euler product of $L(f\times\bar f)$ has nonnegative
  coefficients and a known pole, and dominating one local factor gives $|a_p|\le
  p^{(k-1)/2}\cdot p^{1/2}$ --- the same fixed loss; each symmetric-power $L$-function whose
  poles are known shaves it (Kim--Sarnak's $7/64$ is the current state). "Knowing the poles
  of all the tensor-power $L$-functions is the analogue of big monodromy; over number fields
  that is Langlands functoriality, unproved."
- Lead: none pursued; it names the exact obstruction on the number-field side.
- Related: L13-071, L13-073.

### L13-079 RH for the quantum Ihara zeta is exactly Hastings' bound
- Source: report/sections/08_quantum_ihara_general.tex:288-299, claim
  `obs:rh-iff-ramanujan-channel` (sketched)
- Raised by: orchestrator (Claude), from the founding session's item 2
- Status at last mention: registered as sketched, explicitly "tagged sketched because it has
  had no reviewer"
- Content: for unitary Kraus operators closed under adjoint, each eigenvalue $\lambda$ of
  $\Sigma = D\Phi$ gets the quadratic $1-\lambda u + qu^2$ with $\varepsilon\varepsilon' = q
  = D-1$; both roots have $|\varepsilon| = \sqrt q$ exactly when $|\lambda|\le2\sqrt q$.
  Hence every nontrivial pole of $\zeta_q$ lies on $|u| = q^{-1/2}$ iff $D\lambda_2 \le
  2\sqrt{D-1}$, which is Hastings' bound. "The note records this as an observation, not found
  in the literature in this form."
- Lead: get it reviewed. It is the load-bearing bridge between the zeta language and the
  channel language.
- Related: L13-003, L13-088, L13-136.

### L13-080 What the general Ihara--Bass does not give: `conj:kraus-ramanujan`
- Source: report/sections/08_quantum_ihara_general.tex:275-286
- Raised by: orchestrator (Claude)
- Status at last mention: raised, deferred to `sec:open`
- Content: the arbitrary-Kraus Ihara--Bass gives the compression for *every* MPS transfer
  matrix, at the price of two $u$-dependent operators $\mathcal A(u), \mathcal D(u)$ in place
  of the adjacency matrix and the degree. But it gives no Ramanujan reading by itself:
  without $E_{\bar i}E_i = 1$ there is no quadratic relation pairing the eigenvalues of the
  edge operator with those of $\Sigma$. "What replaces it, and whether canonical form buys
  anything, is `conj:kraus-ramanujan`."
- Lead: the two concrete sub-questions are (a) what replaces the pairing, and (b) whether MPS
  canonical form buys anything. Sharpened later as L13-096.
- Related: L13-096, L13-089.

### L13-081 Side A is unconditionally positive for any Kraus family
- Source: report/sections/08_quantum_ihara_general.tex:81-98, 285-286, claim
  `cor:qihara-kraus`
- Raised by: orchestrator (Claude)
- Status at last mention: pursued, positive
- Content: $\mathrm{Tr}\,B^\ell = \sum_\gamma |\mathrm{Tr}\,K_\gamma|^2 \ge 0$ for *any*
  Kraus family, with no pairing hypothesis --- the proof uses only $\mathrm{Ad}(A)
  \mathrm{Ad}(B) = \mathrm{Ad}(AB)$ and $\mathrm{Tr}\,\mathrm{Ad}(A) = |\mathrm{Tr}A|^2$. So
  "the primes of this zeta are the primitive cyclically non-backtracking words in the $K_k$
  and $K_k^\dagger$, with real nonnegative multiplicities."
- Lead: none stated; it is the reusable positivity that feeds every Weil-positivity argument
  in 08b, 08c and 08e.
- Related: L13-084, L13-085, L13-112.

### L13-082 Which factor carries the spectrum
- Source: report/sections/08_quantum_ihara_general.tex:113-124, claim `cor:qihara-poles`
- Raised by: orchestrator (Claude)
- Status at last mention: pursued, positive
- Content: the poles of $\zeta_T$ lie among the roots of $\det(1+\mathcal D - \mathcal A)$
  together with $u^2 = 1/\lambda$ for nonzero $\lambda\in\mathrm{spec}(E_{\bar i}E_i)$; the
  latter may cancel, as they do in the unitary case (a total cancellation when $D=2$). For
  $D=2$ the edge operator splits as $E_1\oplus E_2$. "Conversely a pole of the second factor
  ... is not a pole of $\zeta_T$ unless it survives multiplication by the first."
- Lead: none stated; the cancellation bookkeeping is the same phenomenon as the "fermionic
  zeros cancel" caution of L13-126.
- Related: L13-126, L13-113.

### L13-083 Provenance gaps around the general Ihara--Bass
- Source: report/sections/08_quantum_ihara_general.tex:219-239
- Raised by: the round-1 provenance review (`claude:opus`)
- Status at last mention: correction applied; one item still numerical only
- Content: Watanabe--Fukumizu's corollary is stated for loopless graphs (their graphs are
  hypergraphs with two-element hyperedges), so a bouquet is not one of their graphs and
  their corollary does not apply to it; the notebook's theorem is the loop-admitting
  analogue, not an instance. **"The shape-matching itself is checked numerically only"**
  (`notes/reviews/scratch_wf_mo_conventions.py`). No local source covers arbitrary weights on
  a bouquet.
- Lead: do the shape-matching symbolically. Small, cheap, and it would close the last
  provenance gap on the book's load-bearing theorem.
- Related: L13-137, L13-138.

### L13-084 TJO's question: what does "every mode is its own partner" mean for an arbitrary Kraus family?
- Source: report/sections/08b_weil_positivity.tex:13-24
- Raised by: TJO (2026-09-12)
- Status at last mention: pursued, answered in three layers
- Content: the reflection $\rho\mapsto 1-\bar\rho$ pairs the mode of the Riemann channel at a
  zero with the mode at its mirror image; RH says every mode is its own partner, and Weil's
  criterion is the positivity of that pairing written on the primes. The answer: without a
  duality, Weil positivity is exactly a one-sided bound; a duality turns it into a circle and
  the Weil form into the mode-pairing form; and for Kraus families the two pairings of the
  index buy the two halves *separately*.
- Lead: none further in this shard; it opens L13-085 … L13-089.
- Related: L13-085, L13-089, L13-096.

### L13-085 Weil positivity alone is only a spectral gap
- Source: report/sections/08b_weil_positivity.tex:50-68, claim `thm:weil-positivity-finite`
- Raised by: the codex prover `gpt-6-astra`; reviewed by `claude:opus`
- Status at last mention: pursued, positive
- Content: for any operator, any trivial multiset and any critical radius, the rescaled trace
  sequence is positive definite iff $|\varepsilon|\le r$ on the retained multiset. "The point
  of the theorem is what it does not say: an eigenvalue inside the disc passes. Weil
  positivity alone is a spectral-gap statement, and the circle needs a second input."
- Lead: the "second input" is the recurring theme --- in the Kraus world it is inverse
  pairing, in the arithmetic world it is the functional equation.
- Related: L13-063, L13-086, L13-113.

### L13-086 The inflow identity: a duality makes the Weil form a mode-pairing form
- Source: report/sections/08b_weil_positivity.tex:70-100, claims
  `thm:weil-duality-pairing`, `prop:weil-orbit-negative`, `prop:weil-reciprocal-only`
- Raised by: the codex prover
- Status at last mention: pursued, positive
- Content: if the retained multiset is invariant under $J(\varepsilon) = r^2/\bar\varepsilon$
  then the Weil form equals the mode-pairing form, and positivity is equivalent to every mode
  being $J$-fixed, i.e. on the circle. A two-element orbit makes the form negative (Weil's
  off-line pair argument in finite form, proved by interpolating the test polynomial to
  vanish at every other retained value). Reciprocal symmetry without conjugation still gives
  the circle but the two forms can differ.
- Lead: none further stated; this is the finite skeleton of the explicit formula.
- Related: L13-085, L13-091, L13-060.

### L13-087 Dead: an inverse-paired counterexample to conjugation closure
- Source: report/sections/08b_weil_positivity.tex:114-131, claim
  `prop:kraus-conjugation-symmetry`
- Raised by: orchestrator (Claude), in the draft sent to the prover
- Status at last mention: pursued, negative --- no such example exists
- Content: the draft asked for an inverse-paired counterexample to conjugation closure; none
  exists inside the Kraus class, and the independent numerics found the same. Every
  $\mathrm{Ad}$-type family has spectra closed under conjugation and nonnegative ring traces
  with no pairing hypothesis. "So every Kraus-type family, however paired, has a positive
  side A and a real-structured side B."
- Lead: none.
- Related: L13-081, L13-096.

### L13-088 Inverse pairing gives the FE, adjoint pairing gives reality, both is unitarity
- Source: report/sections/08b_weil_positivity.tex:133-175, claims
  `thm:kraus-inverse-pairing-duality`, `prop:kraus-both-pairings-unitary`,
  `thm:kraus-weil-criterion`
- Raised by: the codex prover
- Status at last mention: pursued, positive
- Content: inverse pairing makes the retained edge multiset $J$-invariant for $r=\sqrt q$;
  adjoint pairing makes $\Sigma$ Hilbert--Schmidt self-adjoint, hence real-spectrum; both at
  once forces every Kraus operator unitary ($\mathrm{Ad}(B^\dagger) = \mathrm{Ad}(B)^{-1}$
  iff $B^\dagger B = 1$; $B=2$ disproves "unitary up to a scalar"). In the unitary case Weil
  positivity is exactly Hastings' bound --- "the Ramanujan property is the statement that the
  rescaled ring norms form a positive definite sequence". Bookkeeping caveat: a double root
  at $\sigma = \pm2\sqrt q$ gives doubled copies of $\pm\sqrt q$, and $\sigma = \pm D$ gives
  extra $\pm1$'s.
- Lead: opens L13-096 (non-unitary inverse-paired families).
- Related: L13-079, L13-096.

### L13-089 For a general channel, "every mode is its own partner" has no partner to refer to
- Source: report/sections/08b_weil_positivity.tex:177-188, claim
  `prop:kraus-no-duality-example`
- Raised by: the codex prover
- Status at last mention: pursued, negative
- Content: for $n=2$, $D=4$, $B_1=B_3=\mathrm{diag}(1,2)$, $B_2=B_4=1$, the retained edge
  spectrum is invariant under $\varepsilon\mapsto c/\varepsilon$ for *no* nonzero $c$. The
  Weil form is still defined and its positivity is still the one-sided bound; but the
  reflection exists on the punctured plane and need not send a mode to a mode. "What remains
  is a spectral-gap statement, the analogue of $\mathrm{Re}\,\rho\le\frac12$ without the
  functional equation."
- Lead: none; it sets the price of generality.
- Related: L13-085, L13-088.

### L13-090 Dyson expansion as continuous ring norms (and a drafting correction)
- Source: report/sections/08c_weil_positivity_continuous.tex:46-68, claim
  `thm:cmps-ring-norms`
- Raised by: the codex prover; corrects an orchestrator draft
- Status at last mention: pursued, positive
- Content: for $\mathcal L(x) = Kx+xK^\dagger+\sum_jR_jxR_j^\dagger$ the trace of
  $e^{t\mathcal L}$ is an absolutely convergent time-ordered integral of
  $|\mathrm{Tr}(e^{(t-t_k)K}R_{j_k}\cdots R_{j_1}e^{t_1K})|^2 \ge 0$. **"The free propagators
  between jumps were missing from the draft; without them the product is wrong for
  noncommuting $K$ and $R_j$."** This is continuous side A.
- Lead: "the content of RH in this language is the existence of a presentation in which the
  transfer generator is a scalar plus $i$ times a Hermitian operator."
- Related: L13-091, L13-092.

### L13-091 The continuous inflow identity and line duality
- Source: report/sections/08c_weil_positivity_continuous.tex:17-44, claims
  `thm:weil-positivity-continuous`, `thm:weil-line-duality`
- Raised by: the codex prover
- Status at last mention: pursued, positive
- Content: continuous Weil positivity (via Bochner) is a half-plane bound
  $\mathrm{Re}\,\lambda\le a$; a mode off the line contributes a Lorentzian
  $2b/(b^2+(x-\omega)^2)$, a mode on the line a point mass. If the retained multiset is
  invariant under $\lambda\mapsto 2a-\bar\lambda$, the autocorrelation of the rescaled trace
  equals $\sum_\lambda \hat g(\lambda)\overline{\hat g(2a-\bar\lambda)}$ --- Weil's form.
- Lead: none further; the extension to distributions is L13-093.
- Related: L13-086, L13-093.

### L13-092 Weil positivity is blind to Jordan blocks
- Source: report/sections/08c_weil_positivity_continuous.tex:70-105, claims
  `prop:hp-inner-product-discrete`, `prop:hp-inner-product-continuous`,
  `prop:weil-blind-jordan`
- Raised by: the codex prover
- Status at last mention: pursued, positive
- Content: a Hilbert--Polya inner product exists iff the retained part is semisimple with all
  modes on the circle (or line). But $X = r\binom{1\ 1}{0\ 1}$ has $\nu_\ell = 2$ for all
  $\ell$, positive definite, yet is not unitarisable. So "all modes on the critical circle" is
  equivalent to Weil positivity, while "there is a Hilbert space in which the transfer
  operator is $r$ times a unitary" is strictly stronger --- by exactly the absence of Jordan
  blocks. **"For the Riemann channel the distinction is the multiplicity of the zeros: a
  multiple zero of $S$ gives a Jordan block of $Z_t$."**
- Lead: simplicity of the zeros is therefore an *extra* requirement beyond RH for any
  Hilbert--Polya realisation. Nobody followed this up.
- Related: L13-077, L13-093.

### L13-093 The zeta dictionary entry, and what the passage to $\zeta$ needs
- Source: report/sections/08c_weil_positivity_continuous.tex:109-126, claim
  `obs:weil-zeta-dictionary` (sketched)
- Raised by: orchestrator (Claude); reviewed in the same file
- Status at last mention: registered as sketched
- Content: for the compressed semigroup $Z_t$ with modes $\eta = -\bar\rho/2$ the critical
  real part is $a = -\frac14$, the reflection becomes $\eta\mapsto-\frac12-\bar\eta$, and
  Weil's form is the autocorrelation of the centred trace distribution, whose full-line
  extension is $T_Z(-u) = e^{u/2}\overline{T_Z(u)}$. The trivial modes at $0$ and $-\frac12$
  and the Gamma-factor terms are *not* eigenmodes; they stay on the geometric side. "The
  passage from finitely many modes to $\zeta$ needs the completed-zeta data, a distributional
  trace realisation, the full explicit formula and the infinite Weil converse, with
  Bochner--Schwartz in place of Bochner."
- Lead: those four items are a concrete four-part programme. None is done.
- Related: L13-047, L13-050, L13-091, L13-135.

### L13-094 Huang's criterion is the boundedness form of Weil positivity
- Source: report/sections/08c_weil_positivity_continuous.tex:221-232, claim
  `obs:huang-boundedness` (status proved)
- Raised by: orchestrator (Claude)
- Status at last mention: pursued, positive
- Content: in finite dimensions, for a conjugation-closed retained multiset, positive
  definiteness, boundedness, $|\nu_\ell|\le\nu_0$, and the termwise $\mathrm{Re}\,\nu_\ell
  \le \nu_0$ are all equivalent; Huang's graph sequence is exactly $h_k = \nu_0-\nu_k$ with
  $\nu_0 = 2(n-1)$. "The Toeplitz form is what survives when the trace is a distribution and
  boundedness has no meaning."
- Lead: that last sentence is the reason the whole Toeplitz machinery is used for $\zeta$
  rather than the simpler boundedness criterion.
- Related: L13-129, L13-130.

### L13-095 The Kraus dichotomy
- Source: report/sections/08c_weil_positivity_continuous.tex:234-251, claim
  `obs:kraus-dichotomy` (status proved)
- Raised by: orchestrator (Claude)
- Status at last mention: pursued, positive
- Content: (a) any $\mathrm{Ad}$-family has positive rings and conjugation-closed spectra;
  (b) inverse pairing buys the functional equation; (c) adjoint pairing buys reality of
  $\mathrm{spec}(\Sigma)$ for free, but the edge spectrum need not be real and there is in
  general no functional equation; (d) both pairings at once is unitarity, where the trivial
  eigenvalue $D$ always violates the band so the trivial set must be enlarged. **"Reality of
  $\mathrm{spec}(\Sigma)$ is the Hilbert--Polya half; the functional equation is the other
  half; a Kraus family gets the two from two different pairings, and gets both only by being
  unitary."**
- Lead: opens L13-096.
- Related: L13-088, L13-096.

### L13-096 Inverse-paired non-unitary families as an unbroken PT symmetry
- Source: report/sections/08c_weil_positivity_continuous.tex:253-257, with
  `cit:pt-real-spectrum` at 203-211
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued --- it explicitly "reopens
  `conj:kraus-ramanujan` in a sharper form"
- Content: inverse-paired non-unitary families, for instance $B_i = GU_iG^{-1}$ with a common
  similarity $G$ (which keeps $\Sigma$ similar to a self-adjoint operator), have a genuine
  two-sided Ramanujan property with a positive side A; and their non-Hermitian $\Sigma$ with
  real spectrum is **the transfer-matrix version of an unbroken PT symmetry**. The cited fact
  is Bender--Brody--M\"uller, whose own paper links maximally broken PT symmetry to RH.
- Lead: study the family $B_i = GU_iG^{-1}$: it is the smallest class where FE and reality
  coexist without unitarity, which is exactly what a Phantasm transfer operator would need.
  If it worked, one would have Ramanujan behaviour without Hermiticity --- L13-077's
  prescription realised.
- Related: L13-077, L13-080, L13-088, L13-095.

### L13-097 Numerics caveat: finite-$L$ positivity masks a mode just outside the circle
- Source: report/sections/08c_weil_positivity_continuous.tex:278-282
- Raised by: orchestrator (Claude)
- Status at last mention: recorded caveat
- Content: positivity at a fixed finite $L$ is weaker than the theorem --- a mode slightly
  outside the circle is masked by the positive contribution of the interior modes until $L$
  is large. The threshold radius approaches $\max|\varepsilon|$ from below like $L^{-3/2}$
  (relative gap $3\cdot10^{-2}$, $5\cdot10^{-3}$, $4.7\cdot10^{-4}$ at $L=40,160,640$). Also
  recorded: $\{X,Z,X^\dagger,Z^\dagger\}$ is an exact Ramanujan example with channel spectrum
  $\{1,0,0,-1\}$, exercising the $-1$ branch of the trivial set.
- Lead: the $L^{-3/2}$ rate is a quantitative statement about how much window one needs; it
  is the discrete cousin of the extension-disc radius of L13-131.
- Related: L13-131, L13-134.

### L13-098 TJO's question: does the Ihara machinery survive for simplicial complexes, and does it grade by dimension?
- Source: report/sections/08d_complex_zeta.tex:12-17
- Raised by: TJO (2026-09-13)
- Status at last mention: pursued; literature answer negative in general, positive on a thin
  class
- Content: whether the Hashimoto operator, the Bass identity and "RH $\Leftrightarrow$
  Ramanujan" survive when a graph becomes a finite simplicial complex, and whether the answer
  grades by cell dimension into even and odd sectors. Answer: an Ihara-type zeta with a Bass
  identity and an RH-iff-Ramanujan theorem exists for finite quotients of affine buildings
  and nowhere else.
- Lead: opens 08d/08e/08f.
- Related: L13-099 … L13-128.

### L13-099 Higher-rank RH is one-sided, and the interior of the band is genuinely occupied
- Source: report/sections/08d_complex_zeta.tex:81-89, claim `cit:llp-one-sided-rh`; restated
  at 08f:88-97 (`prop:one-sided-rh-variable`) and 08f:252-254
- Raised by: a paper (Lubetzky--Lubotzky--Parzanchevski 2017)
- Status at last mention: cited fact; the consequence for the notebook is standing
- Content: for *every* building, a pole at $u = k^{-s}$ has $|s|=1$ or $\mathrm{Re}\,s\le
  \tfrac12$. The inequality is not an equality: poles with $|\mathrm{Re}\,s|<\tfrac12$ occur,
  already with $|\mathrm{Re}\,s| = 0$ in the graph case and with $0<|\mathrm{Re}\,s|<\tfrac12$
  in higher dimension. The notebook's correction: the source's printed $|s|=1$ cannot
  literally replace $\mathrm{Re}\,s = 1$, since the imaginary part is only defined modulo
  $2\pi/\log b$.
- Lead: since the interior is occupied, no universal duality can close the bound; what remains
  is Weil-positivity-as-bound block by block (L13-113).
- Related: L13-113, L13-124.

### L13-100 Kamber's $L_p$ criterion as the converse, and its inverted bound
- Source: report/sections/08d_complex_zeta.tex:91-101 (`cit:kamber-lp`), 282-289
  (`asm:h-kamber`); used at 08f:95-96
- Raised by: a paper (Kamber 2017)
- Status at last mention: cited fact, used as an assumption row
- Content: with one Bernstein--Lusztig operator per simple coweight, $X$ is an $L_p$-expander
  iff every pole $\lambda$ of the zeta satisfies $|\lambda|\le q^{(p-1)/p}$ or $|\lambda|=q$;
  Ramanujan means $L_2$-expander. The notebook's correction: the bound is on *eigenvalues*, so
  it inverts to a *lower* bound $|u|\ge q^{-(p-1)/p}$ on pole radii.
- Lead: this is the only if-and-only-if in higher rank; a channel version of it was not
  attempted.
- Related: L13-099, L13-121.

### L13-101 Off the buildings, every zeta degenerates
- Source: report/sections/08d_complex_zeta.tex:103-129, claims `cit:storm-reduction`,
  `cit:bcds-triangulation`
- Raised by: papers (Storm 2006; B\'enard--Chaubet--Dang--Schick 2023)
- Status at last mention: cited facts; a standing negative
- Content: Storm's hypergraph zeta has a Bass identity and an iff-Ramanujan theorem, but only
  because $\zeta_H(u) = Z_{B_H}(\sqrt u)$ --- it is the Ihara zeta of the incidence bipartite
  graph in $\sqrt u$, blind to the simplicial structure beyond incidence. The combinatorial
  Ruelle zeta of a triangulation is a polynomial vanishing to order $b_1(M)$ at
  $z=(n+2)^{-1}$, a Fried-type torsion theorem --- "that point is not $q^{-1/2}$, and there is
  no spectral-gap statement".
- Lead: none; it is the reason the campaign stays on buildings.
- Related: L13-098, L13-102.

### L13-102 "No Ihara-type zeta of a general finite complex exists" is a record of what was searched
- Source: report/sections/08d_complex_zeta.tex:131-146, claim `cit:no-general-complex-zeta`
- Raised by: four papers, assembled by the orchestrator
- Status at last mention: cited, with an explicit epistemic caveat
- Content: Deitmar--Hoffman (2004) "There is no Ihara-formula for higher rank up to date";
  Lubotzky's 2018 ICM survey still calls it a direction of research "with the hope that";
  Hong--Kwon name "the lack of a unified zeta function"; Kang--Yu claim only that theirs is
  the first identity uniform in $n$. **"This is a record of what was searched, not an
  impossibility theorem."**
- Lead: prove an actual impossibility theorem, or find the missing zeta. The tetrahedron
  obstruction (L13-110) is the closest the notebook gets to the former.
- Related: L13-110, L13-127.

### L13-103 Kang--Yu's all-rank identity states no RH
- Source: report/sections/08d_complex_zeta.tex:55-67, claim `cit:kangyu-alternating`
- Raised by: a paper (Kang--Yu 2026)
- Status at last mention: cited; the gap noted
- Content: $(1-u^n)^{\chi}L(\Gamma,q^{(n-1)/2}u) = \prod_k Z_k^\epsilon(X,u)^{(-1)^{k+1}}$,
  an alternating product over facet dimension, each factor a reciprocal determinant of a
  successor operator with a parity sign. "The Euler factor is literally a torsion", the
  strategy inspired by Hoffman's reformulation of Bass's proof. **"The source states *no*
  RH."**
- Lead: supply the RH statement for the all-rank identity. That is a well-posed open problem
  the notebook noticed and did not attempt.
- Related: L13-099, L13-107, L13-108.

### L13-104 The graded reading exists in four separate literatures that do not cite each other
- Source: report/sections/08d_complex_zeta.tex:148-205, claims `cit:deitmar-alternating`,
  `cit:dz-order-chi`, `cit:knill-sdet`, `cit:mo-dirac`, plus `cit:hashimoto-hprime`
- Raised by: papers (Deitmar; Dyatlov--Zworski; Knill; Matsuura--Ohta), assembled by the
  orchestrator
- Status at last mention: cited; the connection is the observation
- Content: Deitmar's Ruelle zeta is an alternating product over exterior degree with a
  *degree-weighted* divisor (the plain Euler sum vanishing identically); Dyatlov--Zworski's
  $\zeta_R = \zeta_1/(\zeta_0\zeta_2)$ has order $-\chi$ at 0, even sectors contributing 1
  each and the odd sector $b_1$ --- "the continuous prototype of the graded reading"; Knill's
  graph analytic torsion is a super pseudodeterminant of the Dirac blocks and **"Knill never
  mentions the Ihara zeta, nor the Ihara literature SDet"**; Matsuura--Ohta prove Bass's
  identity with Grassmann fields, the Euler exponent being the fermionic determinant of the
  edge-reversal involution.
- Lead: the explicit gap --- Knill's torsion and the Ihara supertrace are the same shape and
  nobody has joined them --- is an unclaimed connection.
- Related: L13-111, L13-114, L13-126.

### L13-105 The hypothesis register: eight external theorems used but not reproved
- Source: report/sections/08d_complex_zeta.tex:207-289, claims `asm:h-point`, `asm:h-llp`,
  `asm:h-kl`, `asm:h-ky`, `asm:h-ky-local`, `asm:h-kl-table`, `asm:h-lsv`, `asm:h-strong`,
  `asm:h-kamber` (all assumed)
- Raised by: the codex prover (register T8.3)
- Status at last mention: registered as assumed, byte-cited
- Content: pointed-facet successor conventions; LLP branching flows and the digraph bound;
  the Kang--Li rank-three identity and its four-way RH; the Kang--Yu pointed cochain identity
  and its *local* factorisation; the Iwahori-spherical constituent table; the LSV joint Hecke
  spectrum and explicit complexes; Iwahori-spherical temperedness (H-STRONG: "this can be
  strictly stronger than the vertex condition"); and Kamber's normalised criterion.
- Lead: H-STRONG is the interesting one --- it says LLP's Ramanujan condition may be strictly
  stronger than the vertex condition, which would make "Ramanujan complex" ambiguous.
- Related: L13-100, L13-121, L13-122.

### L13-106 The two flows are not the same flow
- Source: report/sections/08d_complex_zeta.tex:291-320, claims `thm:ordered-vs-building`,
  `thm:total-zeta-vertex-l`
- Raised by: the codex prover; refutes an orchestrator draft
- Status at last mention: pursued, positive; draft refuted
- Content: the unrestricted ordered-cell flow $T_1$ is not the block sum $uL_E\oplus u^2L_E^t$
  even after replacing $u^2$ by $u$ --- its outdegree is $2q^2+q$ against $q^2$ for $L_E$ ---
  and its directed-colour classes are not invariant. "The $u^2$ is an algebraic length, not a
  matrix square, and the $3!$ orderings do not realise $L_B$ once." And: the graded total is
  the *completed vertex $L$-function*, not Kang--Li's edge-only zeta. **"The orchestrator's
  draft asserted that the total graded zeta equals Kang--Li's $Z$; the prover refuted that."**
- Lead: opposition, not non-incidence, is the building's successor rule. Any attempt to define
  a higher-dimensional Hashimoto operator by "don't backtrack" is the wrong rule.
- Related: L13-109, L13-116, L13-123.

### L13-107 A universal ordered-cell Bass--Schur compression for every finite complex
- Source: report/sections/08e_complex_zeta_graded.tex:44-66, claims
  `thm:universal-bass-schur`, `cor:bass-every-graph`
- Raised by: the codex prover
- Status at last mention: pursued, positive
- Content: for every finite abstract simplicial complex and every $k$, with $R_k$ the
  first-vertex deletion, $S_k$ the append map, $C_k$ cyclic rotation and $F_k = C_k +
  R_{k+1}S_{k+1}$: $T_k = S_kR_k - F_k$ and $\det(I-zT_k) = \det K_k(z)\det(I -
  zR_kK_k(z)^{-1}S_k)$. "This is an explicit *rational* compression by one dimension ...; it
  is not a degree-$(d+1)$ polynomial on vertices." At $d=1$ it is Bass for every graph with no
  regularity assumption, trees and isolated vertices included by rational cancellation.
- Lead: what survives universally is a rational compression; the polynomial vertex collapse is
  a *building* phenomenon.
- Related: L13-110, L13-114, L13-127.

### L13-108 Finite cochain determinant cancellation (torsion), with the right exponent
- Source: report/sections/08e_complex_zeta_graded.tex:19-42, claims
  `thm:cochain-cancellation`, `thm:pointed-euler-exponent`
- Raised by: the codex prover; corrects an orchestrator draft
- Status at last mention: pursued, positive
- Content: for a bounded cochain complex over $\mathbb C(u)$, any degree $-1$ map $h$ and any
  $c$, $\prod_i\det(F_i|C^i)^{(-1)^i} = \prod_i\det(F_i|H^i)^{(-1)^i} = c^{\sum(-1)^i\dim
  C^i}$; **neither $h^2=0$ nor $h = d^*$ is required**. The exponent is the dimension count of
  the complex used, e.g. $\sum(-1)^i(i+1)f_i$ for pointed cochains, already $\chi=1$ against
  $0$ on a single edge. "The draft's identification of the cochain product's exponent with
  $\chi$ was wrong."
- Lead: the freedom in $h$ is unexploited --- the theorem holds for *any* degree $-1$ map, so
  there is a whole family of torsion identities nobody has looked at.
- Related: L13-103, L13-107.

### L13-109 Dead: a universal cubic vertex Bass identity on every 2-complex (the tetrahedron obstruction)
- Source: report/sections/08e_complex_zeta_graded.tex:68-79, claim
  `prop:tetrahedron-obstruction`
- Raised by: orchestrator (Claude) asked for it; the codex prover refuted it
- Status at last mention: pursued, negative
- Content: on $X = \partial\Delta^3$, $T_1 = 0$, $\det(I+uT_2) = (1-u^4)^6$, and there is *no*
  matrix polynomial $P(u)$ of any size or degree with $\gzeta = (1-u^3)^\chi/\det P(u)$ ---
  that would force $\det P = (1-u^3)^2/(1-u^4)^6$, which has poles at $u=-1,\pm i$. The
  octahedron $K_{2,2,2}$ gives the same phenomenon.
- Lead: this is the notebook's necessary polynomiality condition and the seed of
  `conj:vertex-collapse-characterisation`.
- Related: L13-102, L13-107, L13-127.

### L13-110 The exact graded superdeterminant identity, and what it does not say about zeros
- Source: report/sections/08e_complex_zeta_graded.tex:82-105, claims
  `thm:graded-superdeterminant`, `prop:vertex-l-no-zeros`
- Raised by: the codex prover; refutes two orchestrator drafts
- Status at last mention: pursued, positive; drafts refuted
- Content: $\gzeta_{\mathrm{ord}} = \mathrm{sdet}(I-u\Theta)^{-1}$ exactly, with
  $\log\gzeta = \sum_m \frac{u^m}{m}\mathrm{str}(\Theta^m)$; the order at $u_0\ne0$ is the
  odd minus the even algebraic multiplicity of $u_0^{-1}$. **"The draft's 'the zeros are
  exactly the odd eigenvalues' is false without the reciprocal, sign, multiplicity and
  cancellation qualifications."** And on the building vertex side every finite zero of the
  chamber determinant cancels against an edge or Euler factor, so "calling the chamber zeros
  uncancelled zeros of $L_{\mathrm{vertex}}$, as the draft did, is wrong."
- Lead: this is the central caution for the whole "fermionic zeros" programme --- see L13-126.
- Related: L13-126, L13-074, L13-082.

### L13-111 The total object needs a Berezinian, not one fermion determinant
- Source: report/sections/08e_complex_zeta_graded.tex:130-152, claims
  `thm:incidence-two-schur`, `thm:berezinian-total`
- Raised by: the codex prover; refutes an orchestrator draft
- Status at last mention: pursued, positive; draft refuted
- Content: an explicit incidence matrix $\mathbb D_k(z)$ on $H_{k-1}\oplus H_k\oplus H_{k+1}$
  has two Schur evaluations giving both sides of the compression; giving its auxiliary space
  parity $k+1$ gives $\mathrm{sdet}\,\mathbb D_{\mathrm{flow}} = \gzeta^{-1}$. But "an
  ordinary Berezin integral gives $\det D$, not a reciprocal or a superdeterminant merely
  because $D$ has chiral blocks"; the construction uses separate auxiliary copies, so **cell
  chirality and flow superparity are distinct gradings**. "The draft's universal ordinary
  fermion determinant with flow parity equal to cell chirality does not exist."
- Lead: the two-gradings distinction is a real warning for any "the grading is the geometry"
  ansatz.
- Related: L13-104, L13-110, L13-113.

### L13-112 Arbitrary weights preserve the compression, and positivity needs no pairing
- Source: report/sections/08e_complex_zeta_graded.tex:155-176, claims
  `thm:twisted-bass-schur`, `thm:kraus-ring-positivity`
- Raised by: the codex prover
- Status at last mention: pursued, positive
- Content: with a Kraus connection the identity holds verbatim over $V\otimes H_k$, "with no
  positivity, pairing, invertibility or flatness hypothesis and no inverse of any $E_e$". And
  $\mathrm{Tr}(T^E_k)^m = \sum|\mathrm{Tr}(B_m\cdots B_1)|^2 \ge 0$: **adjoint pairing is not
  needed**, complete positivity of the step maps suffices.
- Lead: stated generalisation: "Any other successor rule with the same overlap admits the same
  construction, by letting $F$ be the sum of its forbidden weighted transitions." That is an
  open invitation --- the machinery is not tied to non-backtracking or to opposition.
- Related: L13-081, L13-107, L13-117.

### L13-113 Positivity of a ring sequence alone does not force a numerator
- Source: report/sections/08e_complex_zeta_graded.tex:178-186, claim
  `prop:positivity-no-go-scope`; and 08f:111-121 `prop:weil-positivity-blocks`
- Raised by: the codex prover
- Status at last mention: pursued, positive
- Content: a single finite transfer matrix contributes a reciprocal polynomial, so it has no
  nonconstant reduced numerator; a numerator comes from *net odd multiplicity between
  sectors*. Positivity of a numerical ring sequence alone does not force this:
  $(1-u)/(1-2u)$ has nonnegative coefficients and positive logarithmic coefficients
  $(2^m-1)/m$, yet a genuine numerator. And Weil positivity applies to each retained
  *ordinary* block but **"does not transfer automatically to an alternating product with
  negative spectral multiplicities."**
- Lead: a *graded* Weil positivity --- positivity for a supertrace sequence with negative
  multiplicities --- is not established and would be needed for any graded Phantasm.
- Related: L13-085, L13-110, L13-124, L13-126.

### L13-114 The graded geodesic determinant is natural but not proved unique
- Source: report/sections/08e_complex_zeta_graded.tex:188-198, claim
  `obs:graded-determinant-natural`
- Raised by: the codex prover
- Status at last mention: pursued, positive with an explicit non-uniqueness caveat
- Content: the definition is functorial under isomorphisms preserving states, lengths,
  successor incidences and transports; "it is not proved unique among possible choices of
  higher-dimensional geodesic". For a graph the default is Hashimoto's operator with only an
  even flow sector; for a building quotient it is the completed vertex product; Kang--Li's
  zeta is obtained by retaining only the edge factor.
- Lead: prove uniqueness, or exhibit a genuinely different higher-dimensional geodesic and
  compare the zetas.
- Related: L13-106, L13-112, L13-127.

### L13-115 The three smallest exact tests, plus an optional fourth
- Source: report/sections/08e_complex_zeta_graded.tex:201-211, claim `num:small-complex-tests`
- Raised by: the codex prover / orchestrator
- Status at last mention: run
- Content: $C_3$ unfilled gives $(1-u^3)^{-2}$; the filled $\Delta^2$ gives total 1 --- "there
  is no forced $(1-u^3)$ factor"; $\partial\Delta^3$ gives $(1-u^4)^6$. The optional
  clique-only fourth test, the octahedron $K_{2,2,2}$, gives $(1-u^6)^8/(1-u^4)^6$, again with
  a pole at $u=-1$ in the would-be vertex expression.
- Lead: the filled-simplex result (no forced Euler factor) is the small surprise; it says the
  $(1-u^{d+1})^\chi$ shape is not universal.
- Related: L13-109.

### L13-116 A representation connection on the full complex is pure gauge
- Source: report/sections/08f_complex_zeta_quantum.tex:20-31, claim
  `prop:pure-gauge-full-complex`; numerics at 08f:207-224
- Raised by: the codex prover; refutes an orchestrator draft
- Status at last mention: pursued, positive; draft refuted
- Content: on a Cayley complex the forward weights $E_{(g,gs)} = \hol(s)$ are generally *not*
  flat; the covariant convention $\hol(s^{-1})$ is pure gauge, so $\det(I-uT^E_k) =
  \det(I-uT_k)^{\dim V}$ --- every closed straight walk of the full complex has identity
  holonomy. The four-cycle with $G=\mathbb Z/4$ separates the full twist $(1-u^4)^2$ from the
  trivial-block determinant $(1-u)^2$. Numerically: 39 of 52 chambers fail flatness, and the
  pure-gauge identity holds exactly.
- Lead: **the genuine Artin object is the voltage quotient, not a connection on the full
  cover.** That is a design rule for any "twist the complex by a representation" construction.
- Related: L13-117, L13-123.

### L13-117 Artin decomposition of a voltage quotient: exponents are $a_\hol$, not $d_\hol$
- Source: report/sections/08f_complex_zeta_quantum.tex:33-44, claim
  `thm:artin-voltage-decomposition`
- Raised by: the codex prover
- Status at last mention: pursued, positive
- Content: with a free action on states, $\det(I-s_kT_k(u)) = \prod_\hol \det(I -
  s_kT_{k,\hol}(u))^{d_\hol}$. But for $R = \bigoplus a_\hol\hol$ the Artin determinant has
  exponents $a_\hol$, not $d_\hol$: $R = \pi\otimes\bar\pi$ need not embed in a single regular
  representation. "What always transfers is spectral support. An equivariant *matrix* identity
  restricts to every block; a scalar determinant equality need not."
- Lead: none stated; it is a bookkeeping trap for the graded Artin programme.
- Related: L13-116, L13-118, L13-065.

### L13-118 Euler-factor bookkeeping on finite-group blocks: the stabiliser caveat
- Source: report/sections/08f_complex_zeta_quantum.tex:46-56, claim
  `thm:euler-block-bookkeeping`; seen numerically at 08f:207-224
- Raised by: the codex prover
- Status at last mention: pursued, positive, and observed
- Content: $\gzeta_\hol = F_\hol/\det(P_n|C_{0,\hol})$ with $\prod_\hol F_\hol^{d_\hol} =
  c^{\chi(X)}$. "Only if the action is free on *unpointed* simplices does this collapse to
  $F_\hol = c^{d_\hol\chi/|G|}$; with simplex stabilisers the fractional power is not a
  rational determinant and must not be asserted." The $\tilde A_2$ numerics show it exactly:
  for the 12-dimensional $\pi$ the naive $c = \chi\dim\pi/|G| = 64$ is right, while the whole
  anomaly sits in the trivial block, where $\chi/|G| = 16/3$ is replaced by
  $(1-u)^{13}(1-u^3)^1$.
- Lead: none stated.
- Related: L13-117, L13-123.

### L13-119 Ramanujan complexes give Ramanujan quantum expanders for free --- and the channel adds nothing
- Source: report/sections/08f_complex_zeta_quantum.tex:59-73 (`thm:quantum-vertex-transfer`),
  192-205 (`num:a2-quantum-twist`), 248-252
- Raised by: the codex prover; numerics by the orchestrator
- Status at last mention: pursued, positive, with a deflating rider
- Content: Harrow-type transfer makes the vertex channels $\Phi_k$ commuting, normal, unital,
  trace-preserving, with $\Phi_k^* = \Phi_{n-k}$ and common fixed space the commutant
  $\pi(G)'$; they satisfy the $\tilde A_2$ Ramanujan condition relative to the *exceptional*
  space. The 12-dimensional irrep of $\mathrm{PGL}_3(\mathbb F_3)$ gives a genuine Ramanujan
  quantum expander of type $\tilde A_2$, all 143 nontrivial joint eigenvalues inside the
  tempered deltoid. **"It cannot fail: $\Phi_1 = A_1^{(\pi\otimes\bar\pi)}/13$, so its
  spectrum is a sub-multiset of $\mathrm{spec}(A_1)$"** --- the channel adds no spectral
  values.
- Lead: correction recorded: "Removing only the channel fixed points, as the draft did, leaves
  type characters that violate the tempered bound" --- the *exceptional space*, not the
  fixed-point space, is the right thing to remove.
- Related: L13-003, L13-120, L13-128.

### L13-120 The exact converse criterion, and why faithfulness is not enough
- Source: report/sections/08f_complex_zeta_quantum.tex:75-86, claim `prop:coverage-converse`
- Raised by: the codex prover
- Status at last mention: pursued, positive
- Content: with $\mathcal B_X$ the irreducibles having a nonexceptional joint eigenvalue
  outside the tempered spectrum, $R$ is Ramanujan iff $\mathcal B_X\cap\mathrm{supp}(R) =
  \varnothing$, and $X$ is vertex-Ramanujan iff $\mathcal B_X = \varnothing$; *coverage* of
  every nonexceptional irreducible by $\pi\otimes\bar\pi$ is sufficient for the converse.
  Faithfulness is not: $G = \mathbb Z/28$, $S=\{\pm1,\pm3\}$ gives a non-Ramanujan Cayley
  graph while a faithful character has $\pi\otimes\bar\pi = 1$ and a vacuous quantum
  condition.
- Lead: "coverage" is the right notion for transferring Ramanujanness back from a channel to a
  graph; it has not been used elsewhere in the book.
- Related: L13-119.

### L13-121 Higher-rank RH has no universal functional equation
- Source: report/sections/08f_complex_zeta_quantum.tex:99-109, claim
  `prop:rank-three-dualities`
- Raised by: the codex prover
- Status at last mention: pursued, negative
- Content: with $A_2 = A_1^*$ the vertex zero multiset is invariant under $u\mapsto
  q^{-2}/\bar u$ before imposing Ramanujan, and the principal-series parts of the edge and
  chamber factors inherit dualities at $q^{-2}$ and $q^{-1}$. But the *full* edge and chamber
  factors do not: a tempered nonspherical block has one root at radius $q^{-1/2}$ and two at
  $q^{-1/4}$, so no $u\mapsto c/\bar u$ or $u\mapsto c/u$ can fix or exchange them.
- Lead: since there is no duality, the one-sided bound cannot be closed in higher rank; the
  "second input" of L13-085 is simply absent.
- Related: L13-085, L13-099, L13-122.

### L13-122 Which constituents supply the three chamber circles
- Source: report/sections/08f_complex_zeta_quantum.tex, via 08e:117-127
  (`prop:three-circles`); numerics at 08f:179-190
- Raised by: the codex prover; verified numerically
- Status at last mention: pursued, positive
- Content: tempered principal series give chamber roots $\pm q^{-1/2}\alpha_i^{-1/2}$ and edge
  roots $q^{-1}\alpha_i^{-1}$; the tempered nonspherical type gives one chamber root at
  $q^{-1/2}$ and two at $q^{-1/4}$; Steinberg twists give the unit circle; one-dimensional
  constituents give *trivial* roots at $q^{-1}$. **"So the circle $q^{-1/2}$ is not 'the odd
  sector', and a single constituent can contribute to two circles at once."** The $\tilde A_2$
  numerics reproduce exactly the radii $\{1,3^{1/4},3^{1/2}\}$ for $L_B$ and $\{3,\sqrt3\}$
  for $L_E$ and nothing else.
- Lead: it kills the tempting identification "one circle = one parity sector". Also
  `prop:parity-only` (08e:107-115): the cohomology dictionary is *parity only* --- the
  reindexing matches the Grothendieck--Lefschetz exponents but does not identify the spaces
  with cohomology nor assign Weil weight $k-1$.
- Related: L13-110, L13-126.

### L13-123 The identity holds on a complex where Kang--Li's hypothesis fails
- Source: report/sections/08f_complex_zeta_quantum.tex:124-138, 150-165, claims
  `num:a2-complex`, `num:a2-identity`
- Raised by: orchestrator (Claude), from the numerics
- Status at last mention: observed, unexplained
- Content: the smallest $\tilde A_2$ Ramanujan complex, the LSV Cayley complex of
  $\mathrm{PGL}_3(\mathbb F_3)$ on 5616 vertices, is **not 3-colourable** (the group is
  simple), so Kang--Li's type-preservation hypothesis fails on it; and all 13 generators have
  order 3, so the 24336 triangles carry $\mathbb Z/3$ stabilisers and $G$ is not free on
  unpointed 2-cells. A type-preserving 3-fold cover was built alongside. **Yet the corrected
  identity holds exactly to $u^{18}$ on the base as well as on the cover**, degree 308880 on
  both sides, with $\chi$ fitting exactly at every order.
- Lead: explain why. Either type preservation is not needed for the identity, or the base is
  accidentally special. "Two facts not anticipated in the brief."
- Related: L13-118, L13-124.

### L13-124 Corrections found by the $\tilde A_2$ numerics
- Source: report/sections/08f_complex_zeta_quantum.tex:150-177, claims `num:a2-identity`,
  `num:a2-flow-operators`
- Raised by: orchestrator (Claude)
- Status at last mention: corrections applied
- Content: the placement written in the orchestrator's brief fails at $u^3$ (residual
  $-59904$) and fails the degree count (398736 against 219024); $\det(I-uL_B)$ in place of
  $\det(I+uL_B)$ first fails at $u^{15}$. The unrestricted ordered edge rule has outdegree
  $2q^2+q = 21$ against $L_E$'s $q^2 = 9$: it is not Kang--Li's operator. On all six orderings
  of a chamber, $\det(I+uT_2) = \det(I+uL_B)^2$.
- Lead: none; a dead-route record.
- Related: L13-106, L13-123.

### L13-125 The sign in $\det(I+uL_B)$
- Source: report/sections/08d_complex_zeta.tex:28-41 (`cit:kl-identity`, "Note the base
  $(1-u^3)$, the *plus* sign ... and the $u^2$ on the transposed edge factor")
- Raised by: a paper (Kang--Li), flagged by the orchestrator
- Status at last mention: noted and used
- Content: the $\mathrm{PGL}_3$ Bass identity carries a plus sign on the chamber factor and a
  $u^2$ on the transposed edge factor; the numerics confirm the plus sign is essential
  (L13-124).
- Lead: none stated. The plus sign is a graded/parity sign in disguise and connects to the
  alternating-product reading of L13-104.
- Related: L13-104, L13-124.

### L13-126 "Fermionic zeros" names a net odd multiplicity that must be checked after cancellation
- Source: report/sections/08f_complex_zeta_quantum.tex:238-245, 256-258
- Raised by: orchestrator (Claude), summarising the prover's corrections
- Status at last mention: standing caution
- Content: "The odd sector is real as a graded *presentation* and unreal as a divisor": the
  graded superdeterminant identity is exact, but on the building vertex side the chamber
  factor cancels completely, so "fermionic zeros" names a net odd multiplicity that must be
  checked *after* cancellation. The parallel with Ruelle and with Knill's supertrace is parity
  and alternating structure, "not an identification of spaces or weights". And: "None of this
  touches the Riemann side directly. It is a supply of exactly-solvable graded transfer
  operators with a Ramanujan property, not a channel whose zeta is $\zeta(s)$."
- Lead: any Phantasm claim of the form "the zeros are the odd modes" has to survive this
  cancellation test.
- Related: L13-110, L13-113, L13-122, L13-047.

### L13-127 Characterising vertex collapse for a general complex (conjecture)
- Source: report/sections/08f_complex_zeta_quantum.tex:260-271, claim
  `conj:vertex-collapse-characterisation` (conjectured)
- Raised by: the codex prover / orchestrator
- Status at last mention: registered as conjectured
- Content: there is a combinatorial characterisation of the finite complexes $X$ for which
  $B_X(u) = (1-u^{d+1})^{\chi}/\gzeta_{\mathrm{ord}}(X,u)$ is the determinant of a matrix
  polynomial $I - uA + \sum_{j\ge2}u^jQ_{j-1}$ with $Q_{j-1}$ built from local link data.
  Building quotients are sufficient; the tetrahedron obstruction gives a necessary
  polynomiality condition; "matching generalised-polygon link parameters is *not* known to
  suffice, and no recognition theorem for Bruhat--Tits universal covers is assumed here."
- Lead: prove it, or find a non-building complex with a polynomial vertex collapse. That would
  be a genuinely new zeta.
- Related: L13-102, L13-109, L13-107.

### L13-128 Higher-rank Weil positivity is only a bound
- Source: report/sections/08f_complex_zeta_quantum.tex:111-121, 252-256
- Raised by: the codex prover / orchestrator
- Status at last mention: standing conclusion
- Content: what one has in higher rank is Weil-positivity-as-bound, the finite theorem applied
  block by block, because RH is one-sided, the interior is genuinely occupied and there is no
  universal duality to close it.
- Lead: see L13-113 --- a graded version with negative multiplicities is what would be needed.
- Related: L13-099, L13-113, L13-121.

### L13-129 TJO's question: can one build a better estimator of $\mathrm{Tr}\,X^\ell$ beyond the window?
- Source: report/sections/08g_weil_window_extension.tex:12-22
- Raised by: TJO (2026-09-19)
- Status at last mention: pursued, answered negatively (the disc is optimal)
- Content: the Connes--Consani--Moscovici construction seems to (1) assume a form for the
  traces, (2) collect data up to some lag, (3) build a model for the higher traces, and
  (4) use positivity and Toeplitz structure to read information off the minimal eigenvector.
  Could one be cleverer and build a better estimator of $\mathrm{Tr}\,X^\ell$ for $\ell>K$
  from the traces up to $K$?
- Lead: opens L13-130 … L13-135.
- Related: L13-094.

### L13-130 The window is an exact compression; the implicit model of the higher traces is Pisarenko's
- Source: report/sections/08g_weil_window_extension.tex:51-67, claim
  `obs:window-is-compression` (sketched)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched
- Content: in the CCM chain and its graph analogue the window quadratic form is the *exact*
  restriction of the full Weil form to test functions supported in the window --- no value is
  assigned to the traces beyond it. The perturbed operator of the chain has as spectrum
  exactly the roots of the kernel polynomial of $W_K - \varepsilon_K$, so the only model the
  chain commits to is the Pisarenko extension: $K$ atoms on the circle plus a white-noise
  floor $\varepsilon_K$ at lag zero. "This is the minimal-support extension of the data, and
  it is the appropriate prior exactly because the true spectral measure is pure point."
- Lead: none further; it identifies what the chain is implicitly assuming.
- Related: L13-129, L13-131.

### L13-131 The admissible next trace fills a disc, and nothing beats it
- Source: report/sections/08g_weil_window_extension.tex:83-132, claim `prop:extension-disc`
  (sketched)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched (the algebra is checked numerically to
  $10^{-9}$ rather than carried out)
- Content: the admissible set for $\nu_{K+1}$ is a closed disc whose centre is the Levinson
  one-step predictor and whose radius is $\det W_K/\det W_{K-1}$, non-increasing in $K$;
  boundary points are exactly the singular windows with $K+1$ atoms on the circle
  (Carath\'eodory--Fej\'er). If the retained measure has exactly $K+1$ distinct atoms the true
  value lies on the boundary and every later trace is determined by the kernel recurrence.
  **"No estimator of $\nu_{K+1}$ from $\nu_0,\dots,\nu_K$ and positivity alone can do better
  than the disc"**; the centre is the minimax choice and the maximum-entropy (Burg) extension.
- Lead: complete the algebra so the status can rise above sketched.
- Related: L13-129, L13-133, L13-134.

### L13-132 Newton congruence: the counts add information positivity cannot see
- Source: report/sections/08g_weil_window_extension.tex:139-152, claim
  `prop:newton-congruence` (sketched)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched
- Content: for an integer matrix $X$ with $N_k = \mathrm{Tr}\,X^k$, $N_{K+1} \equiv
  -\sum_{i=1}^K c_iN_{K+1-i} \pmod{K+1}$, so **the traces up to lag $K$ determine the next
  trace modulo $K+1$**.
- Lead: combine with the disc and nonnegativity. For the permutation $(1\,2)(3\,4\,5)$ the
  three constraints pin the next trace at $K=3$, one lag *before* the critical window.
- Related: L13-131, L13-133.

### L13-133 Rescaling defeats integrality for graphs
- Source: report/sections/08g_weil_window_extension.tex:154-166, claim
  `obs:rescaling-and-zeta` (i)-(ii) (sketched)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched
- Content: for a permutation ($r=1$) the disc, the half-line $N_{K+1}\ge0$ and the congruence
  act on the same integer and can pin it early. For a $(q+1)$-regular graph the disc lives in
  the rescaled variable and has radius $q^{(K+1)/2}r_K$ in count units, which exceeds one on
  every positive-definite window of the Petersen graph (35.5, 40.6, 49.4 at $K=1,2,3$), "so
  integrality pins nothing; only the Ramanujan-side information (positivity) and the exact
  critical window remain."
- Lead: none stated. It says the arithmetic bonus is lost exactly when the critical radius is
  not 1 --- i.e. always in the interesting cases.
- Related: L13-131, L13-132.

### L13-134 For $\zeta$, a better higher-trace estimator means more primes
- Source: report/sections/08g_weil_window_extension.tex:166-177, claim
  `obs:rescaling-and-zeta` (iii) (sketched)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched; explicitly "an argument, not a theorem"
- Content: for $\zeta$ the traces are $\Lambda(n)$. The *mean* of the traces beyond the window
  is the prime number theorem, which is exactly the pole term of the explicit formula and
  already enters the window form exactly; the higher powers $p^m>\lambda^2$ of known primes
  lie outside the support and are invisible; what is unknown beyond the window is the
  fluctuation $\Lambda(n)-1$, which by the explicit formula *is* the zeros. **"A better
  estimator of the higher traces of $\zeta$ therefore means more primes, i.e. a larger
  window."** The remaining freedom is the choice of extremal extension, and the content of
  Connes--Consani--Moscovici is the rate at which the Pisarenko atoms converge (about 5.4
  digits per unit of $\lambda^2$).
- Lead: this is the answer to TJO's question and it is negative in the cleanest way: the
  estimator question is circular for $\zeta$.
- Related: L13-129, L13-131, L13-135.

### L13-135 Two proposed computations, not run
- Source: report/sections/08g_weil_window_extension.tex:198-207 ("Not established, and one
  computation proposed")
- Raised by: orchestrator (Claude)
- Status at last mention: **proposed, not run**
- Content: (a) in the `ihz` sidequest the disc radius $r_K$ is one determinant ratio per
  window; combined with the congruence and nonnegativity it would show how far below the
  critical window a graph divisor is already forced. (b) For `zst`, the analogous quantity ---
  the Schur-complement radius of the window Loewner form as $\lambda$ grows --- "would bound
  rigorously what the primes beyond $\lambda^2$ can do to the form; comparing its decay in
  $\lambda$ with the observed $e^{-4\pi\lambda^2}$ convergence of the first zero would say
  whether that convergence is explained by the shrinking envelope or by something specific to
  the arithmetic."
- Lead: exactly as stated; both are cheap and both are outstanding. (b) is the more
  interesting: it would distinguish a generic approximation-theoretic effect from genuine
  arithmetic.
- Related: L13-131, L13-134, L13-097.

### L13-136 The prior-art verdict: no zeta has been attached to a quantum channel
- Source: report/sections/09_prior_art.tex:254-277, claim `obs:prior-art-verdict` (sketched)
- Raised by: three literature agents, assembled by the orchestrator
- Status at last mention: registered as sketched
- Content: no source found attaches a zeta function, or an analogue of RH, to a quantum
  channel; none states the poles-on-the-critical-circle iff Hastings-bound equivalence; none
  gives the MPS ring-norm reading or the identification of AKLT with $K_4$. What *is* known:
  the $\mathrm{Ad}$-weighted Ihara--Bass formula and the free-group $L$-function reading
  (Matsuura--Ohta), arbitrary matrix weights for loopless graphs (Watanabe--Fukumizu), and the
  matrix-valued non-backtracking operator (Bordenave--Collins).
- Lead: none stated; it establishes what is the notebook's own.
- Related: L13-079, L13-137, L13-083.

### L13-137 The standing limit of the prior-art search: arXiv search is metadata-only
- Source: report/sections/09_prior_art.tex:279-293
- Raised by: orchestrator (Claude)
- Status at last mention: recorded limitation
- Content: ten arXiv metadata queries returned zero hits (listed verbatim in the shard), as
  did web/Scholar searches for "quantum Ihara zeta", Ihara zeta with noncommutative/quantum
  graphs (Weaver, Duan--Severini--Winter), Ihara zeta with MPS/tensor networks, and a
  MathOverflow search. **"arXiv search is metadata-only, so a formula inside a paper body
  would not surface, and the absence claims are weaker than its presence claims."**
- Lead: a full-text search (e.g. over downloaded TeX) would strengthen the absence claims.
  Not done.
- Related: L13-136.

### L13-138 Ben-Aroya--Schwartz--Ta-Shma: the one unverified source near the Ramanujan claim
- Source: report/sections/09_prior_art.tex:249-253
- Raised by: a literature agent
- Status at last mention: unverified, read only from the publisher PDF
- Content: an agent read that they "believe their first construction has the potential of
  being improved to a quantum Ramanujan expander". This is the one source near claim 2 that
  has no byte-verified local TeX.
- Lead: verify it. If their construction does reach the bound, the notebook's claim of novelty
  for exactly-Ramanujan quantum expanders would need adjusting.
- Related: L13-003, L13-136, L13-140.

### L13-139 Bordenave--Collins have the operator but as a resolvent identity, not a determinant
- Source: report/sections/09_prior_art.tex:155-178, claim `cit:bc-nonbacktracking`
- Raised by: a literature agent, verified by the orchestrator
- Status at last mention: verdict RELATED
- Content: their matrix-valued non-backtracking operator is the same operator as the quantum
  Hashimoto operator, introduced explicitly because "This extension is especially relevant in
  the context of quantum expanders", and the later work names the connection to Ihara--Bass
  identities --- "but as a resolvent identity rather than a determinant: no zeta and no
  Riemann hypothesis." Separately, they record that a family of tensor-squared permutations is
  a nearly optimal quantum expander in Hastings' sense.
- Lead: the tensor-squared permutation family is a cheap alternative source of near-Ramanujan
  channels that the notebook never used.
- Related: L13-136, L13-079.

### L13-140 $\mathrm{Ad}(U_i)$ generates an infinite group, so this is not literally a Stark--Terras $L$-function
- Source: report/sections/09_prior_art.tex:237-243
- Raised by: orchestrator (Claude)
- Status at last mention: recorded distinction
- Content: in Stark and Terras the representation is one of the Galois group of a covering of
  finite graphs, hence of a *finite* group, whereas $\mathrm{Ad}(U_i)$ for generic unitaries
  generates an infinite group. So the quantum Hashimoto object is not literally a
  Stark--Terras $L$-function, although the determinant formula is the same.
- Lead: none stated. The infinite-group case is exactly where the Artin-decomposition
  bookkeeping of L13-117 would have to be redone.
- Related: L13-117, L13-076.

### L13-141 The quantum-walk zeta line is not on point
- Source: report/sections/09_prior_art.tex:245-249
- Raised by: a literature agent
- Status at last mention: verdict NOT
- Content: Konno and Komatsu et al. build zetas from the *unitary evolution matrix of a
  quantum walk* rather than from Kraus operators, one paper extending to open quantum random
  walks on the torus by Fourier analysis; the value of the line here is the Sunada pointer.
- Lead: none stated; but "open quantum random walks on the torus by Fourier analysis" is the
  nearest neighbour to the notebook's cMPS/Lindblad direction and was not followed.
- Related: L13-136.

### L13-142 Correction: the authorship of arXiv:2309.15873
- Source: report/sections/09_prior_art.tex:295-300
- Raised by: orchestrator (Claude), correcting a literature agent
- Status at last mention: corrected
- Content: one agent attributed arXiv:2309.15873 to Kudo and Li; the TeX header gives Mason
  Eyler and Jaiung Jun, and every citation was corrected on 2026-09-12.
- Lead: none; a provenance-hygiene record.
- Related: —

### L13-143 TJO's question: replace channels by Lindblad generators
- Source: report/sections/09b_selberg_dictionary.tex:12-23
- Raised by: TJO
- Status at last mention: pursued; delivered as a dictionary with one open conjecture
- Content: the simplest continuous instance is the generator of rotations on a circle of
  circumference $\log p$, whose trace is a Poisson comb at multiples of $\log p$; the Selberg
  analogue should be a Lindbladian built from the vector fields on $\mathrm{PSL}_2(\mathbb R)$
  with the Laplacian as the small operator, and a formal analogue of the comb.
- Lead: opens L13-144 … L13-156.
- Related: L13-144, L13-147, L13-148.

### L13-144 The prime comb is an orbital trace, and the missing ingredient is transverse expansion
- Source: report/sections/09b_selberg_dictionary.tex:161-186, claims
  `prop:prime-circles-orbital`, `prop:finite-euler-spectrum`
- Raised by: the codex prover; corrects the worklog's wording
- Status at last mention: pursued, negative for the naive construction
- Content: the direct sum over primes of circles of circumference $\log p$ gives the comb
  $\sum_n \Lambda(n)\delta(t-\log n)$ as a *locally summed component trace*, but the smeared
  direct-sum operator is never trace class (the constant modes give a nonzero eigenvalue of
  infinite multiplicity) and the positive prime comb is not tempered. Finite sets of primes
  see only Euler poles and *no zeros at all*. **"The missing ingredient is transverse
  expansion: a circle has no Poincar\'e map, so no Jacobian, so no resonances."**
- Lead: this is the sharpest diagnosis in the lane of why the naive "primes as circles"
  picture cannot produce zeros. Any Phantasm needs a transverse direction.
- Related: L13-072, L13-002, L13-150.

### L13-145 The Lindbladian of the $\mathfrak{sl}_2$ vector fields is the Casimir, but not a diffusion
- Source: report/sections/09b_selberg_dictionary.tex:188-218, claims
  `prop:lindblad-sum-of-squares`, `prop:casimir-laplacian`
- Raised by: the codex prover
- Status at last mention: pursued, positive with a limitation
- Content: for real vector fields acting as derivations and jumps $L_j=-iX_j$, the dissipator
  on multiplication observables is $M_{\frac12\sum_jX_j^2f}$. On the $K$-invariant sector
  $\tfrac12(H^2+E^2) = 2\,\mathrm{Cas} = -2\Delta$. But on all functions $\tfrac12(H^2+E^2) =
  2\,\mathrm{Cas}+\tfrac12W^2$: **"the Casimir carries the compact direction with a minus sign
  and is not a diffusion Lindbladian on all of $L^2(\Gamma\backslash G)$"**; the two-jump
  Lindbladian preserves the $K$-invariant sector and equals $-2\Delta$ there.
- Lead: the drift matters --- "squaring the projected tangent vectors alone would miss the
  drift and give the wrong operator". Extending beyond the $K$-invariant sector is unresolved.
- Related: L13-146, L13-148.

### L13-146 The continuous Harrow construction
- Source: report/sections/09b_selberg_dictionary.tex:220-234, claim
  `prop:quantum-lindblad-tensor`
- Raised by: the codex prover
- Status at last mention: pursued, positive
- Content: for a unitary representation $\pi$ with $A_j = d\pi(X_j)$ and jumps $L_j=-iA_j$,
  the dissipator is $\tfrac12\sum_jB_j^2\rho$ with $B_j\rho = [A_j,\rho]$ the generators of
  $\pi\otimes\bar\pi$ on Hilbert--Schmidt operators; for $\mathfrak{sl}_2$ with the two
  non-compact jumps it is $2\,\mathrm{Cas}_{\pi\otimes\bar\pi}+\tfrac12B_W^2$. "This is the
  continuous Harrow construction: a channel from a representation becomes a Lindbladian from a
  representation, and its gap is a question about $\pi\otimes\bar\pi$."
- Lead: opens L13-148.
- Related: L13-119, L13-148.

### L13-147 Six standard inputs carried as assumptions
- Source: report/sections/09b_selberg_dictionary.tex:28-84, claims `asm:fuchsian-geometry`,
  `asm:laplace-spectrum-compact`, `asm:selberg-zeta-entire`, `asm:heat-semigroup`,
  `asm:zeta-standard`, `asm:gamma-standard` (all assumed)
- Raised by: the codex prover
- Status at last mention: registered as assumed, "printed as such because no local source
  quotes them in full"
- Content: Fuchsian geometry; the Laplace spectrum of a compact hyperbolic surface; Selberg
  zeta entire with known divisor; closed realisations of flows and the heat semigroup;
  standard facts about $\zeta$ (including the $\log^2$ growth bound on $\zeta'/\zeta$ near
  $\mathrm{Re}=1$); standard facts about $\Gamma$.
- Lead: fetch quotable sources; every claim depending on one prints `-conditional`.
- Related: L13-150, L13-152.

### L13-148 Gap of the representation Lindbladian (conjecture)
- Source: report/sections/09b_selberg_dictionary.tex:236-244, claim
  `conj:quantum-lindblad-gap` (open)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as open; listed again in 09c's "Not established"
- Content: for an irreducible unitary $\pi$ of $\mathrm{SL}_2(\mathbb R)$, or of
  $\mathrm{SL}_2(\mathbb F_p)$, the two-jump Lindbladian
  $2\,\mathrm{Cas}_{\pi\otimes\bar\pi}+\tfrac12B_W^2$ has a spectral gap governed by the
  decomposition of $\pi\otimes\bar\pi$; **for the Weil representation this is the continuous
  shadow of the Weil--LPS channels**.
- Lead: compute the decomposition of $\pi\otimes\bar\pi$ for the Weil representation and read
  off the gap. Consequence: a continuous-time Ramanujan object matching the finite Weil--LPS
  model, i.e. the dilation-time version of the finite model.
- Related: L13-007, L13-146, L13-156.

### L13-149 The `sl_2` irrep check: Lindbladian spectrum $-2j(j+1)$
- Source: report/sections/09c_selberg_tower_cusp.tex:102-120, claim `num:selberg-lindblad`
- Raised by: orchestrator (Claude) / the numerics
- Status at last mention: run, positive
- Content: for the three-dimensional $\mathfrak{sl}_2$ irrep the Lindbladian spectrum is
  $\{0,-4^{\times3},-12^{\times5}\} = -2j(j+1)$; the quantum tensor identity holds to
  $7\cdot10^{-15}$.
- Lead: this is the smallest datum bearing on L13-148 --- the gap for a finite irrep is
  explicitly $4$. Scaling it in $\dim\pi$ was not attempted.
- Related: L13-148.

### L13-150 The flat trace of the geodesic flow is the continuous Ihara--Bass; the sign was drafted wrong
- Source: report/sections/09c_selberg_tower_cusp.tex:17-42, claims `prop:poincare-jacobian`,
  `prop:flat-tower`
- Raised by: the codex prover; corrects an orchestrator draft
- Status at last mention: pursued, positive
- Content: the flat trace is $\sum_\gamma\sum_k \ell_\gamma e^{-\lambda k\ell_\gamma}/
  (4\sinh^2(k\ell_\gamma/2))$, and the tower $D(\lambda) = \prod_{j\ge1}Z_S(\lambda+j)$
  converges absolutely without zeros, with $\mathrm{flat\ trace} = +D'/D$. The tower comes
  from $1/(4\sinh^2(x/2)) = \sum_m(m+1)e^{-(m+1)x}$: **"the Jacobian of the two transverse
  directions is what a graph does not have."** Two corrections: the sign was drafted as a
  minus and is a plus; and the graph counterpart of the tower is $\det(1-uH)$, not the zeta.
- Lead: none further; it completes the L13-144 diagnosis on the positive side.
- Related: L13-144, L13-151, L13-153.

### L13-151 Continuous Ramanujan is Selberg's $\tfrac14$ property, after removing the constant mode
- Source: report/sections/09c_selberg_tower_cusp.tex:44-62, claim `prop:tower-divisor-band`
- Raised by: the codex prover
- Status at last mention: pursued, positive
- Content: the tower is entire with zeros at $\lambda = -\tfrac12-k\pm ir_j$ and at $-N$ with
  order $(2g-2)N^2+2$; the nonconstant first band is exactly the pole multiset in
  $-1<\mathrm{Re}\,\lambda<0$, and it lies on $\mathrm{Re} = -\tfrac12$ iff every $r_j$,
  $j\ge1$, is real iff $\Delta$ has no eigenvalue in $(0,\tfrac14)$. **The constant mode must
  be removed, exactly as the constant adjacency mode is removed in the Ramanujan condition of
  a graph.** Explicit caveat: the proposition makes no claim about operator realisations, only
  about the poles of the continued flat trace.
- Lead: L13-155 asks for the operator statement.
- Related: L13-150, L13-155.

### L13-152 The cusp of the modular surface *is* the prime comb
- Source: report/sections/09c_selberg_tower_cusp.tex:76-100, claim `prop:cusp-prime-comb`
- Raised by: the codex prover
- Status at last mention: pursued, positive (conditional)
- Content: the continuous-spectrum multiplier decomposes as $C = -P + A$ where
  $P(t) = \sum_n \frac{\Lambda(n)}{n}[\delta(t-2\log n)+\delta(t+2\log n)]$ and $A$ is an
  explicit archimedean background with $A(t) = \tfrac12 - 1/(4\sinh(|t|/2))$ away from 0.
  **"The prime atoms are dips"**; and the constant $\tfrac12$ is the pole of $\zeta$ at 1 (the
  ordinary boundary value differs from the Abel boundary distribution by $\pi\delta_0$), *not*
  a digamma term.
- Lead: numerically confirmed with a Gaussian window to $3\cdot10^{-8}$; the ratio
  $-2G/\sqrt{2\pi}$ matched to six digits. Nothing further proposed.
- Related: L13-153, L13-154.

### L13-153 Correction: the "damped Riemann channel trace" claim
- Source: report/sections/09c_selberg_tower_cusp.tex:122-138, claim `prop:damping-identity`
- Raised by: the codex prover; corrects the previous session's wording
- Status at last mention: correction applied
- Content: the previous session's sentence "the cusp term of the modular trace formula is the
  trace of the Riemann channel damped at rate $\tfrac14$" is corrected: what is proved is that
  the *prime measure* written in the Riemann-channel note, damped at rate $\tfrac14$, is the
  *prime part* of the cusp distribution --- an equality of prime atomic measures after
  subtracting the archimedean background and choosing positive weights. "It is not an equality
  of the full cusp distribution with a semigroup trace, nor of operators or spectra, and it
  implies nothing about the Riemann hypothesis." Also: **"the rate $\tfrac14$ is the uniform
  rate only under the Riemann hypothesis."**
- Lead: none; a dead-route/overclaim record.
- Related: L13-152, L13-155.

### L13-154 The primes enter only through the cusp, as the scattering term, not as closed geodesics
- Source: report/sections/09c_selberg_tower_cusp.tex:142-172, claim
  `obs:continuous-dictionary` (sketched-conditional)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched-conditional
- Content: the dictionary maps edge space to $\Gamma\backslash\mathrm{PSL}_2(\mathbb R)$, the
  Hashimoto operator to the geodesic generator, the adjacency matrix to the Casimir (equal to
  $-\Delta$ on the $K$-invariant sector), Ihara--Bass to the tower, and Ramanujan to "no
  eigenvalue in $(0,\tfrac14)$". The closing row is the structural point: **the primes of
  $\zeta$ enter only through the cusp of the modular surface, as the scattering term, not as
  closed geodesics.**
- Lead: none stated. It says the geodesic side and the prime side of the Selberg picture are
  disjoint, which is a serious obstacle to reading $\zeta$ as a Selberg-type transfer
  spectrum.
- Related: L13-144, L13-152, L13-155.

### L13-155 The continuous Ihara--Bass as an identity of operators, not divisors
- Source: report/sections/09c_selberg_tower_cusp.tex:174-185 ("Not established")
- Raised by: orchestrator (Claude)
- Status at last mention: raised, partially addressed elsewhere
- Content: not established: a literal operator-theoretic compression from $\Gamma\backslash G$
  to the $K$-invariant sector turning the tower into a Laplacian determinant (its first-band
  operator form --- a quadratic intertwining through the fibre pushforward plus the horocyclic
  ladder --- is `prop:selberg-ladder-ihara` in the Selberg-letters shard, with the
  anisotropic-space realisation assumed there); a trace formula for the full compressed
  semigroup $Z_t$; any gap for the Lindbladian conjecture; and anything about RH or the
  $\tfrac14$ property of a given surface.
- Lead: four concrete open items, the first now partly addressed by the Selberg-letters lane.
- Related: L13-148, L13-151, L13-156.

### L13-156 A trace formula for the full compressed semigroup $Z_t$
- Source: report/sections/09c_selberg_tower_cusp.tex:135-138, 181-183
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued
- Content: "The full trace of $Z_t$ is not established as a pure prime comb (its own explicit
  formula has pole, archimedean and sign bookkeeping)", and a trace formula for the full
  compressed semigroup is listed as not established.
- Lead: write down the explicit formula for $Z_t$ with all three bookkeeping terms. That is
  the prerequisite for any comparison with the Selberg trace formula and for L13-093.
- Related: L13-093, L13-153, L13-155.

### L13-157 The reproducibility discipline itself
- Source: report/sections/11_reproducibility_map.tex:1-66 (whole shard)
- Raised by: orchestrator (Claude)
- Status at last mention: infrastructure, in force
- Content: one row per evidence script, its captured output under `outputs/`, and the claims it
  backs; scripts run from the repository root with only numpy/scipy/mpmath/sympy, random data
  seeded, local CI re-running the fast scripts and diffing against captured output; every
  quote byte-checked at `<id>:<file>:<line>`; a `proved` claim names its review file and the
  gate checks for `VERDICT <id>: VALID`. No mathematical ideas of its own.
- Lead: none stated. The one substantive gap it exposes is that "proved" in this book means
  author $\ne$ reviewer *inside one model family* for the campaigns where only one family was
  declared (stated at 08:18-22).
- Related: L13-079, L13-058.

## Small but possibly consequential

1. **L13-053 (RH as a single odd correlation length)** --- the statement "every fermionic mode
   has correlation length exactly twice the bosonic one" is a physics statement that could be
   attacked with physics tools (area laws, Lieb--Robinson), and it was written down once and
   never used again.
2. **L13-096 (inverse-paired non-unitary families as unbroken PT symmetry)** --- one paragraph
   at the end of 08c naming a concrete family $B_i = GU_iG^{-1}$ that would give Ramanujan
   behaviour without Hermiticity, which is exactly what L13-077 says is needed; nobody built
   one.
3. **L13-092 (Weil positivity is blind to Jordan blocks)** --- it quietly implies that a
   Hilbert--Polya realisation needs *simple* zeros, an extra hypothesis beyond RH that the rest
   of the notebook does not track.
4. **L13-135 (the two proposed, unrun window computations)** --- the `zst` one would settle
   whether the observed $e^{-4\pi\lambda^2}$ convergence of the first zero is generic
   approximation theory or genuine arithmetic; that is a cheap, decisive experiment.
5. **L13-123 (the $\tilde A_2$ identity holding where its hypothesis fails)** --- a concrete,
   exactly-verified anomaly (not 3-colourable, stabilisers on triangles, identity holds
   anyway) that nobody explained.
6. **L13-066 (a literal count state needs 0/1 word traces)** --- one clause in the C9 row; it
   is the precise statement of the gap between the gas picture and every tensor the notebook
   actually built.
7. **L13-104 (Knill's super pseudodeterminant never meets the Ihara literature)** --- the
   shard explicitly notes the two literatures do not cite each other despite computing the same
   shape; joining them is an unclaimed connection.
8. **L13-108 (torsion cancellation holds for *any* degree $-1$ map)** --- the theorem needs
   neither $h^2=0$ nor $h=d^*$, so there is an unexplored family of Bass-type identities
   parametrised by the choice of $h$.

## Dead routes recorded

- The claim $\alpha_i = -\lambda_i(E)$ "uniformly in $n$" for Artin--Schreier curves:
  false in general, holds iff $P_g(-1)\ne0$ --- 06:75-84, 06b:80-83, counterexamples at
  06b:85-92.
- The orchestrator's conjugated replacement law $S_n = -(-\eta(-1))^n\overline{\mathrm{Tr}E^n}$:
  also false, holds iff $P_g(-\eta(-1))\ne0$ --- 06b:80-83, 06b:85-92.
- The orchestrator's drafted argument for finite order of the transfer unitary ("the entries
  are roots of unity"): insufficient because of zero entries and the normalisation ---
  06c:159-162.
- The drafted cut-rank bound $D$ across a ring cut: that is the *open-chain* bound; the ring
  bound is $D^2$ --- 06c:168-170.
- The broad slogan "fixed finite lattice tensors give only supersingular zetas": explicitly
  false --- 06f:286-290, 06c:195-198.
- "Carries must be unbounded" in the base-$\pi$ digit picture: wrong, cyclic carries are
  bounded --- 06d:126-128.
- Counting the points of an elliptic curve by a nonnegative-weight automaton, or by any finite
  weighted adjacency matrix / trace-class operator: impossible --- 06d:120-128.
- The orchestrator's drafted Hilbert--Schmidt/trace bound
  $\sum_{\mathrm{odd}}|\mu|^2\le2\mathrm{Tr}E_{++}\mathrm{Tr}E_{--}$: false, 173 of 400 random
  instances violate it --- 06e:17-26.
- The trace version of the infinite-bond bound ($2\mathrm{Tr}S_+\mathrm{Tr}S_-$): needs
  positivity of $S_\pm$ on Hilbert--Schmidt space, which complete positivity alone does not
  give --- 06e:100-102.
- The literal geometric placement of the genus-two cohomology, and the vacuum ansatz
  $a_1=1,B_1=0,a_2=0,B_2=B$: both impossible --- 06f:89-99.
- Reading the functional equation as ket/bra exchange: would assume RH --- 06f:259-263.
- "Inverse-closed letters give the functional equation for the raw doubled transfer": false,
  counterexample $B=\mathrm{diag}(1,2)$ --- 06h:40-43.
- Closing the Horner automaton into a trace to present a Dirichlet $L$-function as a ring norm:
  wrong (it imposes a return condition) --- 06h:135-138.
- The drafted square-root $\mathbb Z/2$ Artin factor for the pair shift: not an Artin factor;
  the correct example is a directed voltage cover --- 06h:74-76, 06h:146-149.
- Treating unique stationarity, the whole-bond gauge and mixing as one condition: they are
  three --- 06h:195-199.
- Deligne's pointwise theorem for graphs: false, the two-loop bouquet with
  $\binom{2\,1}{1\,1},\binom{1\,1}{1\,2}$ satisfies (a),(b),(c) yet is not pure --- 07:153-161.
- Commuting Kraus unitaries as a source of expansion: never gives an expander; commuting
  holonomies produce uncontrolled invariants in tensor powers --- 07:174-188.
- An inverse-paired Kraus counterexample to conjugation closure: none exists --- 08b:127-131.
- The Dyson-expansion draft without free propagators between jumps: wrong for noncommuting $K$
  and $R_j$ --- 08c:61-63.
- "The total graded zeta equals Kang--Li's $Z(X_\Gamma,u)$": refuted by the prover; it is the
  completed vertex $L$-function --- 08d:310-320.
- The unrestricted ordered-cell flow as the building's edge successor: outdegree $2q^2+q$
  against $q^2$, colour classes not invariant --- 08d:302-308, 08f:170-172.
- Identifying the cochain product's Euler exponent with $\chi$: wrong, it is the weighted
  $\sum(-1)^i(i+1)f_i$ --- 08e:40-41.
- A universal cubic vertex Bass identity on every 2-complex with local coefficients: refuted by
  $\partial\Delta^3$ --- 08e:68-79.
- "The zeros are exactly the odd eigenvalues": false without the reciprocal, sign, multiplicity
  and cancellation qualifications --- 08e:91-93.
- Calling the chamber zeros uncancelled zeros of the vertex $L$-function: wrong, they all
  cancel --- 08e:96-105.
- A universal ordinary fermion determinant with flow parity equal to cell chirality: does not
  exist; the total is a Berezinian --- 08e:141-152.
- "The full representation twist is a representation block": refuted by the four-cycle with
  $G=\mathbb Z/4$; the covariant weights are pure gauge --- 08f:20-31.
- Removing only the channel fixed points in the Harrow-type transfer: leaves type characters
  violating the tempered bound; remove the exceptional space --- 08f:70-72.
- Asserting the fractional Euler exponent $c^{d_\hol\chi/|G|}$ when simplex stabilisers exist:
  not a rational determinant --- 08f:53-56.
- The pole placement written in the orchestrator's $\tilde A_2$ brief: fails at $u^3$ and fails
  the degree count; $\det(I-uL_B)$ for $\det(I+uL_B)$ fails at $u^{15}$ --- 08f:160-164.
- Beating the extension disc: no estimator of the next trace from the traces up to lag $K$ and
  positivity alone can do better --- 08g:104-107.
- Using integrality to pin the next trace of a $q$-regular graph: defeated by rescaling, the
  disc radius exceeds one in count units --- 08g:161-166.
- "The Poisson trace of the direct sum" over prime circles: does not name a trace-class
  operator; the smeared direct-sum operator is never trace class and the comb is not tempered
  --- 09b:161-171, 09b:183-186.
- Squaring the projected tangent vectors to get the Selberg Lindbladian: misses the drift and
  gives the wrong operator --- 09b:213-218.
- The Casimir as a diffusion Lindbladian on all of $L^2(\Gamma\backslash G)$: it carries the
  compact direction with a minus sign --- 09b:205-209.
- The drafted minus sign in the flat-trace/tower relation: it is a plus --- 09c:39-42.
- "The cusp term of the modular trace formula is the trace of the Riemann channel damped at
  rate $\tfrac14$": corrected to a statement about prime measures only, implying nothing about
  RH --- 09c:132-138.
