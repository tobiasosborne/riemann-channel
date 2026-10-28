<!-- ROLE: live state. UPDATE POLICY: every session end. -->

# HANDOFF — riemann-channel

## Start here (updated 2026-10-28)

A research notebook on the Riemann hypothesis through graphs (Ihara zeta), curves over finite fields, GKP codes and tensor networks; `README.md` has more.
- **Reading order for state:** this register (below) → the round status files `notes/astra-2026-10-23/STATUS.md`, `notes/astra-2026-10-25/STATUS.md`, `notes/astra-2026-10-27/STATUS.md` → the session entries below (newest first) → `docs/handoff-archive.md` (sessions 2026-09-11 to 2026-10-02, verbatim). `docs/notes-index.md` maps `notes/`; `docs/worklog/` has the dated logs.
- **Labels:** `HELD` waiting on Claude usage or a TJO decision (stated per item) · `OPEN` not started, nothing blocks · `PARTIAL` started, remainder stated · `BLOCKED: <blocker>` · `OPEN (unverified since <date>)` listed as Next once and not checked against later work · `DONE` / `SUPERSEDED` rows only in the last register subsection.
- **Rule:** "Next" lists inside the session entries and the archive are historical; this register is authoritative.

## State at a glance

- **Machine:** new since 2026-10-27; backup of the old home at `~/old` (SquashFS); `refs/src/` and the gitignored run artefacts restored from it on 2026-10-28 (local only, incl. the 4.6 GB HKL clone `notes/astra-2026-10-25/census/sources/hkl-genus-6/`). PARI/FLINT venv `/tmp/claude-1000/-home-tobias-Projects-riemann-channel/dcae8e10-414e-4cb4-8b95-d35e159cfb50/scratchpad/venv-astra` is wiped by a reboot (rebuild with uv: cypari2, python-flint); no `gp` binary.
- **Gate (`make check`):** 13 errors (261 on the new machine before the 2026-10-28 recovery), 305 warnings. The 13: 8 `prov:yosh92-*` rows (`refs/src/yoshida-1992/paper.txt` is not an arXiv source and exists on neither machine; needs a manual copy of Yoshida 1992) and 5 scripts evidenced by no shard (`scripts/rtp2_{blind_recovery,grid_tomography,impure_bumps,lattice_box}.py` await shard 08j; `scripts/codex_quota.py` is a utility). Nothing from rounds 2026-10-23, 10-25, 10-27 is registered.
- **Round 2026-10-23** (8 astra lanes; `notes/astra-2026-10-23/STATUS.md`): all lanes done; SAME-FAMILY REVIEWED by the 2026-10-25 round (0 INVALID); no cross-family review.
- **Round 2026-10-25** (9 astra lanes; `notes/astra-2026-10-25/STATUS.md`): five reviews and four new lanes done; reviews are SAME-FAMILY; the four new lanes are unreviewed.
- **Round 2026-10-27** (tree of codes, Pizer; `notes/astra-2026-10-27/STATUS.md`): Fable proofs CROSS-FAMILY REVIEWED (astra); both astra proofs UNREVIEWED (Fable reviews never run).
- **Corrected pages** (endorsed record corrections annotated 2026-10-28) are endorsed same-family only; not cross-family reviewed.
- **HELD:** all Claude work, by TJO on 2026-10-27 15:30 (Claude usage credits); lifting it is TJO's call. Codex lanes were not held. Registration in `db/claims.tsv` is also TJO's call.
- **Pushed:** `master` pushed to origin at 6684aad on 2026-10-28 (TJO). The five stale remote branches (all contained in `master`): `ccr-2c2701e9-3nhoug`, `claude/beautiful-bohr-e84nm9`, `claude/inspiring-ride-n5binf`, `claude/project-familiarization-8gondy`, `claude/weil-bond-analytic` — deletion approved by TJO 2026-10-28, to be run by TJO (the agent's push --delete was blocked by the permission classifier).

## Open-work register

Sources merged: the facts of the 2026-10-28 tidy, every "Next" list in this file and in `docs/handoff-archive.md` (incl. "Next useful steps", "Steering 2026-09-11", "Current state 2026-09-18"), and the "Unfinished" sections of the three STATUS files. Items sit under the line of work; most actionable first. Items of September 2026 that nothing since mentions are `OPEN (unverified since <date>)`.

### Round 2026-10-27 (tree of codes, Pizer)
- **HELD** — Fable REFUTE review of the astra tree-codes proof, giving `notes/astra-2026-10-27/tree-codes/review-fable-of-astra.md` (protocol in `brief.md` "Design") — Claude usage · origin: 2026-10-27 · where: `notes/astra-2026-10-27/tree-codes/astra/astra-proofs.md`
- **HELD** — Fable REFUTE review of the astra Pizer proof, giving `notes/astra-2026-10-27/pizer/review-fable-of-astra.md`; until both exist the astra proofs are UNREVIEWED and nothing in the round is registrable — Claude usage · origin: 2026-10-27 · where: `notes/astra-2026-10-27/pizer/astra/astra-proofs.md`
- **HELD** — record page `notes/adelic-gkp/tree-of-codes.md` from the VALID items (T1, T2, T4a, code-trace theorem; P1, P2, P3a, half-loop lemma, det Ω = n² obstruction) with the INVALID items as negative findings, then annotations to `graph-ihara.md` §2(b)/§3/§5 and `data-ladder.md` §0 (a Pizer rung), §1.2 — Claude usage, after the two reviews · origin: 2026-10-27 · where: `notes/astra-2026-10-27/STATUS.md`
- **PARTIAL** — tree-codes T5 (Casoratian/boundary Poisson pairing): Fable T5 is a sketch (INVALID in the astra review), astra T5 PARTIAL; remains a proof or a refutation · origin: 2026-10-27 · where: `notes/astra-2026-10-27/tree-codes/`
- **OPEN** — four reviewer remarks inside VALID tree-codes items, unapplied (Lemma 1.2 "not the trivial cocycle"; `1_L` versus δ₀ by √p; Γ_γ\Axis(γ) in the §4(b) table; Prop 2.1(ii) "refers to L") · origin: 2026-10-28 · where: `notes/astra-2026-10-27/tree-codes/fable/fable-proofs.md`
- **OPEN** — the two UNVERIFIED pizer items `P1-weighted-zeta` (no weighted edge operator specified) and `P3c-freeness` (citation from memory) · origin: 2026-10-27 · where: `notes/astra-2026-10-27/pizer/fable/fable-proofs.md`
- **OPEN** — `conj:intrinsic-automorphic-boundary-pairing`; nothing blocks it except a next round · origin: 2026-10-27 · where: `notes/astra-2026-10-27/tree-codes/astra/astra-proofs.md`
- **OPEN** — `question:pizer-reduced-jacobian-lattice` (polarized comparison for J₀(37), primes 2 and 3) · origin: 2026-10-27 · where: `notes/astra-2026-10-27/pizer/astra/astra-proofs.md`

### Reviews and promotion (gate)
- **HELD** — second-family (Claude) REFUTE review of the 2026-10-23 PROVED items, now with same-family reviews attached: T1/T2, J, H + K first, then A + C and Q1 + Q2 — Claude usage · origin: 2026-10-23, 2026-10-25 · where: `notes/astra-2026-10-23/STATUS.md`, `notes/astra-2026-10-25/review-*/astra-proofs.md`
- **HELD** — second-family REFUTE review of the four 2026-10-25 lanes: `census` theorem and witnesses, `hhalf` genus ≤ 7 certificates, `irreps` P1 converse, `shortrow` formula; no review file exists — Claude usage · origin: 2026-10-25 · where: `notes/astra-2026-10-25/STATUS.md`
- **HELD** — cross-family review of the pages carrying the 2026-10-28 endorsed-correction annotations (the endorsements are codex on codex) — Claude usage · origin: 2026-10-28 · where: `notes/adelic-gkp/{overlap-data,tower-pairing,cm-lift,no-lift,data-ladder,gauge-groups,graph-ihara,howe-positivity,graph-super}.md`
- **HELD** — registration of reviewed rows of all three astra rounds in `db/claims.tsv` — TJO's decision, after cross-family review · origin: 2026-10-23, 2026-10-25, 2026-10-27 · where: `db/claims.tsv`
- **HELD** — register `notes/adelic-gkp/shard-draft/` (shard 04za, 20 rows, dry-run gate clean); promotion to `proved` needs a reviewer of another model — TJO's decision · origin: 2026-10-06 · where: `notes/adelic-gkp/shard-draft/README.md`
- **PARTIAL** — REFUTE review of lanes R, S, U: a partial one by Fable exists (12 VALID); the 42 lane-U comparisons got an independent FLINT replay and PARI audit in `2026-10-25/review-tower`, but lanes R and S have no full review · origin: 2026-10-06, 2026-10-23 · where: `notes/reviews/adelic-gkp-rsu-fable-2026-10-06.md`
- **OPEN (unverified since 2026-10-05)** — REFUTE review of `graph-ihara.md` and `graph-super.md` before registering anything (T-b); the 2026-10-25 `review-gauge` covered the gauge pages only · origin: 2026-10-05 · where: `notes/adelic-gkp/graph-ihara.md`, `graph-super.md`
- **OPEN (unverified since 2026-10-02)** — REFUTE review of `adelic-gkp.md` before registering Proposition 3 (rigidity), Theorem 4 (level-N Bell pair), Proposition 5 (p-adic codes) next to 04p (G-b) · origin: 2026-10-02 · where: `notes/adelic-gkp/adelic-gkp.md`
- **OPEN (unverified since 2026-09-22)** — REFUTE reviews for shards 04v, 04y, 04z (`notes/reviews/<lane>-2026-09-22.md` with `VERDICT` lines, then restore `proved`); `db/claims.tsv` still has them `sketched`/`numerical` · origin: 2026-09-22, 2026-09-25 · where: `report/sections/04{v,y,z}_*.tex`
- **OPEN (unverified since 2026-09-22)** — review, numerics and shards for `genus-two-quotient-graph`, `h-arith-fqt`, `lps-graded-cp` · origin: 2026-09-22, 2026-09-25 · where: `notes/genus-two-quotient-graph*`, `notes/h-arith-fqt*`, `notes/lps-graded-cp*`
- **OPEN (unverified since 2026-09-26)** — REFUTE review of `notes/rtp-round-2/blind-recovery/lane.md`, then its row `num:rtp-grid-blind-recovery-certified` in 08j · origin: 2026-09-26 · where: `notes/rtp-round-2/blind-recovery/lane.md`
- **OPEN (unverified since 2026-09-24)** — REFUTE lane before registering sections 7.2–7.4 of the metric-as-unknown-state note; byte-cite Burg/Dempster, Bombieri/Yoshida, Selberg/Levinson/Conrey · origin: 2026-09-24 · where: `docs/handoff-archive.md` (2026-09-24 entry)
- **OPEN (unverified since 2026-09-18)** — Opus REFUTE review of `ihz` `lanes/theory.md` before any claim is registered · origin: 2026-09-18 · where: `ihz/`
- **OPEN (unverified since 2026-09-14)** — Opus REFUTE reviews of 02h/03c/03d against `astra-proofs.md`, of 06h, of 04g, of shard 03b · origin: 2026-09-14, 2026-09-15 · where: `report/sections/`
- **OPEN (unverified since 2026-10-05)** — byte-cite Stark–Terras, Godsil–Gutman, Heilmann–Lieb, Hall–Puder–Sawin, Kesten, Marcus–Spielman–Srivastava (`zn-flux.md` still says "from memory") · origin: 2026-10-05 · where: `notes/adelic-gkp/gauge-groups.md`, `zn-flux.md`
- **OPEN (unverified since 2026-09-24)** — byte-cite the remaining sources of the 2026-09-24 and 2026-10-06 notes (quantifier elimination, Hulthén value; the 15 bibliographic citations of `citations-2026-10-06.md`) · origin: 2026-09-24, 2026-10-06 · where: `notes/adelic-gkp/citations-2026-10-06.md`

### Record corrections
- **OPEN** — tutorial §6d: replace the unconditional sentence "RH for the graph says that every non-trivial mode is in the first case ..." (too strict, Ramanujan allows |λ| = 2√q) by the endorsed wording of `review-average-canonical` §C6 (Ω is the Casoratian, Ω = −W_k with labels (x_k, −x_{k+1}); Q = ½Ω(M − qM⁻¹); in-band endpoints give degenerate energy and parabolic blocks), plus the remark that the label form does not descend through the kernel of the label-to-edge map; needs `test.js`, headless render, republish of https://claude.ai/artifact/2KbsLkFaW2pBBHs5r1NQxc · origin: 2026-10-23, 2026-10-25, 2026-10-28 · where: `notes/adelic-gkp/tutorial/page.html`
- **OPEN** — `shard-draft/` tsv and tex wording for `prop:gkp-overlaps-see-order` and `obs:gkp-missing-datum`: recorded in the README ("Pending wording corrections (2026-10-28)"), not applied to the draft files · origin: 2026-10-23, 2026-10-25, 2026-10-28 · where: `notes/adelic-gkp/shard-draft/`
- **OPEN** — "the graph Schur moment is a trace of M/√q, not A/√q" (`review-average-canonical` ledger item 5): a correction to lane C's own text, not to a record page (no record page states the A/√q form; checked 2026-10-28) · origin: 2026-10-25 · where: `notes/astra-2026-10-23/canonical/astra-proofs.md`
- **OPEN** — lane texts that carry wrong wording: lane A (finite-certificate sentence must say H-half for odd cells and band certificates for both parities); lane Q1 (7/8 synopsis P_x = (2 − 8x/9)(1 − x); stray comma in the cube exponent; Cureton–Thorner 31/32 numbering lacks local provenance); the lanes' own pages, not record pages · origin: 2026-10-25 · where: `notes/astra-2026-10-23/{average,canonical,qrh-digest}/astra-proofs.md`
- **OPEN** — optional: an explicit K₄ SU(1,1) family for `gauge-groups.md` "Next" · origin: 2026-10-28 · where: `notes/adelic-gkp/gauge-groups.md`
- **OPEN** — optional: carry the rank remark (the label span has rank 2n − 1, 2n − 2 bipartite) into `graph-ihara.md` §4; not found there · origin: 2026-10-22 · where: `notes/adelic-gkp/graph-ihara.md`
- **OPEN** — ledger for future briefs (not record pages): theta graph with three parallel edges is 3-regular; both K₃,₃ masks nonordinary; averaged traces are coefficients of the averaged logarithm; HPS standard S_d has dimension d − 1; simplified short-row diagonal only for h ≥ D − 1; lane T's same-order F₄₁ pair has no separating k · origin: 2026-10-25 · where: `notes/astra-2026-10-25/STATUS.md`

### Open mathematical problems with finite tests
- **PARTIAL** — hyperelliptic-average H-half / A1 / `conj:hyperelliptic-average-all-genus` for all (q, g): proved for odd q, g ≤ 7 (`hhalf`); remains control of the adjacent nonsquare corrections at m ∝ g, m = 13 and genera 26–27 at q = 3 · origin: 2026-10-23, 2026-10-25 · where: `notes/astra-2026-10-25/hhalf/`
- **OPEN** — `conj:whole-squarefree-cubic-average` (on the circle in five tested cells) · origin: 2026-10-25 · where: `notes/astra-2026-10-25/hhalf/astra-proofs.md`
- **OPEN** — `conj:conformal-sp4-average-real-rooted`: prove interlacing or search graphs with ≥ 8 vertices (true on cycles and 971 graphs ≤ 7 vertices) · origin: 2026-10-25 · where: `notes/astra-2026-10-25/irreps/`
- **PARTIAL** — J2′ (nonnegative a_k ⟹ Jacobian class): refuted by the K₃,₃ census; cube masks 3, 5 and Petersen masks 6, 10 remain (degree-2 covers of genus-4 bases, tetragonal models) · origin: 2026-10-23, 2026-10-25 · where: `notes/astra-2026-10-25/census/`
- **OPEN** — integral polarized lattice of the K₄ trigonal and Petersen-22 Jacobians versus the graph's Ω; whether the graph's lattice equals a constructed Jacobian lattice · origin: 2026-10-23, 2026-10-25 · where: `notes/astra-2026-10-25/census/`
- **OPEN** — a Weil-free proof of H-MS (function-field analogues of source Prop. 6.2 / 5.4: the uniform theta/transfer estimate); Weil ⟹ H-MS is done · origin: 2026-10-25 · where: `notes/astra-2026-10-25/shortrow/`
- **OPEN** — `Q1-THETA`, `Q1-EVAL`, `Q1-TRACE` (digest) and `Q2-THETA-SECTORS`, `C-SURF` / `conj:surface-squarefree-local-limit` (transpose); each has a finite test in its lane's closing section; these are the five UNVERIFIED rows of `review-qrh` · origin: 2026-10-23, 2026-10-25 · where: `notes/astra-2026-10-23/{qrh-digest,qrh-transpose}/astra-proofs.md`
- **OPEN** — the ε-uniform CM comparison of lane U with cypari2 (only the reduced one-lattice form, 27/27, exists; no review states it done) · origin: 2026-10-06, 2026-10-23 · where: `notes/adelic-gkp/tower-pairing.md`, `checks/check_cm_tower.py`
- **OPEN (unverified since 2026-10-06)** — open items on the pages: which ideal class and principal form belong to Jac(C) for the genus-two curve (E); Petersen twist and a Howe-type criterion for Centeleghe–Stix objects (B); the CM version of the vacuum-point reading (G); J(F_{5^k}) of the Fermat quartic (S); the twist family and higher infinity types (I) · origin: 2026-10-06 · where: `notes/adelic-gkp/{curve-bridge,no-lift,zeta-ingredients,repeated-root,gate-phases}.md`
- **OPEN** — the one question of 2026-10-06: what plays the finite-field geometry over Q (a global H¹ with integral squeeze action and a positivity reason) · origin: 2026-10-06 · where: `notes/adelic-gkp/data-ladder.md` ("The answer in one paragraph")
- **OPEN (unverified since 2026-10-05)** — T-a′: tower and vacuum on the half lattice for bipartite graphs (one quadrature per vertex, form B_s, Frobenius two steps; `locks.md` has the half lattice and ω₊ but not the tower); fluxes with det B_s = ±1; the order-four symmetry of K₄ as a Z[i]-structure; the unit twist P in general; Jacobian or Prym for the K₄ example; the non-ordinary examples · origin: 2026-10-05 · where: `notes/adelic-gkp/locks.md`, `howe-positivity.md`
- **OPEN (unverified since 2026-10-05)** — T-a″: the matching question in the notebook's terms (an invariant vacuum on the odd bond of shard 04t) · origin: 2026-10-05 · where: `notes/adelic-gkp/lattice-tower.md`
- **OPEN (unverified since 2026-10-05)** — T-c: the arithmetic graded examples (graded Weil–LPS of 03c): identify the flux and the torus · origin: 2026-10-05 · where: `notes/adelic-gkp/graph-super.md`
- **OPEN (unverified since 2026-10-02)** — G-a: are the prime terms of the explicit formula the leakage between levels N and pN under D_p (compression lemma, analytic §5) · origin: 2026-10-02 · where: `notes/adelic-gkp/adelic-gkp.md`
- **OPEN (unverified since 2026-10-01)** — N1 calibration (bond proof of RH for an elliptic curve from Riemann–Roch plus one geometric input; Mumford's Θ^{g−1}·φ*Θ for g = 1, 2); N1′ genus two, Rosati form in recurrence coordinates (shard 04w); N2 weighted edge content with the LPS cut for Q; N2′ Wronskian kernel of Ξ on RTP prime-content windows; N3 rank-≤3 leakage versus the notebook's exits; N4 two-period HB pairs on the genus-one bond · origin: 2026-10-01, 2026-10-02 · where: `docs/handoff-archive.md` (2026-10-01 entry)

### Lab book / shards / gate
- **BLOCKED: Project Euclid serves a bot wall (Incapsula) to curl** — download Yoshida 1992 (ASPM 21, doi 10.2969/aspm/02110281) in a browser to `refs/src/yoshida-1992/paper.pdf`, then `pdftotext -layout` to `paper.txt` and compare with `refs/manifest-extra.sha256` (e05bd254…); clears the 8 `prov:yosh92-*` gate errors · origin: 2026-09-25, 2026-10-05, 2026-10-06, 2026-10-28 · where: `refs/fetch_extra_sources.sh`, `db/provenance.tsv`
- **OPEN** — shard 08j (Riemann tomography, round 2): apply the six reviews' replacement texts to the lane reports; register the recommended rows (`lem:bordering-interval` as proved with `deps -`; lattice recession/width/coercivity; grid moment; impure Kronecker; Dirichlet and elliptic numerical; H-CONCENTRATION-TRANSFER open); byte-cite Baker, Coste, Nesterenko–Waldschmidt, Hulthén, Carneiro–Chirre; regen, gate, rebuild `report.pdf`; clears 4 of the 5 script errors (`scripts/rtp2_*.py`) · origin: 2026-09-26, 2026-10-05, 2026-10-06 · where: `notes/rtp-round-2/`, `notes/reviews/rtp-round-2-*-2026-09-26.md`
- **OPEN** — evidence for `scripts/codex_quota.py` (utility; the 5th script error): cite it in a shard or allow-list it · origin: 2026-10-28 · where: `scripts/codex_quota.py`
- **OPEN (unverified since 2026-09-22)** — fix `scripts/connes_weighted_metric.py:264`; extend `scripts/cerednik_drinfeld.py` past D13; resume the Sonine enclosure · origin: 2026-09-22 · where: `scripts/`, `report/`
- **OPEN (unverified since 2026-09-26)** — RTP round 2 numerics: LP/SDP width ratio at x = 25 (port the reviewer's barrier to arb); lane S at x = 60, 70, 85 (`zst/tools/rtp2_scale.c`) and the 8π constant for weight two with x > 250 · origin: 2026-09-26 · where: `zst/`, `notes/rtp-round-2/`
- **OPEN (unverified since 2026-09-24)** — RTP round 1 leads: Dirichlet L(s, χ) through the window pipeline (zst M3); lattice box widths against x with an exact LP; non-admissible prime-content bumps via the Kronecker lemma; N-convergence of ε at x = 50 beyond N = 420 · origin: 2026-09-24 · where: `zst/`, `report/sections/08i_riemann_tomography.tex`
- **OPEN (unverified since 2026-09-24)** — metric-lead numerics: the `r_K` diagnostic of shard 08g on `zst` against e^{−4πx}; the prime-content window on {2}, {2,3}, {2,3,5}; Proposition A (FNW exclusion) after byte-citing; the Baker grading of W; finite-bond approximability of the arithmetic state on the genus-one class-group bond; the standing list of open inputs (irrationality of a zero ordinate, of γ, of a Stieltjes constant) · origin: 2026-09-24 · where: `docs/handoff-archive.md` (2026-09-24 entry)
- **OPEN (unverified since 2026-09-18)** — `zst`/`ihz` follow-ups: M3 explicit-formula data model beyond MVP-3, `(λ, N)` accuracy map, x = 100 run (M4), `det_reg → Ξ` and the prolate side (M5); `Q-2` under-resolved law, anti-palindromic search `Q-3`, fuzz and mutation for `ihz`, M3/G5 shared data model · origin: 2026-09-17, 2026-09-18 · where: `zst/README.md`, `ihz/`
- **OPEN (unverified since 2026-09-19)** — repair the defects of `notes/ideation-ledger-2026-09-19/LEDGER.md` §5 (shard 04 sign errors, dependency rot, unreviewed load-bearing claims, the BLAS-thread CI fixture, unresolved provenance addresses); act on the 40 ranked leads of §3.1 · origin: 2026-09-19 · where: `notes/ideation-ledger-2026-09-19/`

### Early programme leads (2026-09-11 to 2026-09-24; none mentioned since)
- **OPEN (unverified since 2026-09-12)** — Bost–Connes reframe, programme 0a′–0f: Γ₀(N) model space and the scattering determinant (`conj:galois-graded-bond`); both halves with a mixed rebound state on K_S (`conj:phantasm-both-halves`); infinite parity rigidity (`obs:parity-infinite-open`); Mayer cusp tail; Suzuki's prime-defined screw kernel; Bonthonneau–Weich, Lewis–Zagier, Chang–Mayer · origin: 2026-09-12 · where: `docs/handoff-archive.md` ("CENTRAL PRIORITY")
- **OPEN (unverified since 2026-09-12)** — Weil–LPS channels part 2: joint spectra (13;17,29), (19;5,17), (29;5,13) against Hecke eigenvalues of weight-2 forms for the quaternion algebra ramified at {2, ∞} (LMFDB API is captcha-blocked; PARI via the cypari2 venv is the route), and what "assemble over p" means · origin: 2026-09-11, 2026-09-12 · where: `docs/handoff-archive.md` ("Next useful steps" 1)
- **OPEN (unverified since 2026-09-12)** — continuous Harrow channel (was `conj:quantum-lindblad-gap`): fetch Nelson/CHH/Repka TeX, state the gap formula as a theorem, codex prover then Opus refute; Repka threshold 3/4 must be byte-checked; the quantum lattice version is not formulated · origin: 2026-09-12 · where: `docs/handoff-archive.md` ("Next useful steps" 1b)
- **OPEN (unverified since 2026-09-12)** — general Kraus zeta part 2: inverse-paired non-unitary families B_ī = B_i⁻¹ (PT-type reality); experiments B_i = G U_i G⁻¹ and random invertible B_i; Bartholdi deformation (Matsuura–Ohta) · origin: 2026-09-12 · where: `docs/handoff-archive.md` ("Next useful steps" 1a)
- **OPEN (unverified since 2026-09-12)** — the Stinespring question (compressed semigroup Z(t) on K_S as a Holevo jump generator with jumps at k log p; a negative answer with a reason is a result); tighten §4 of the note (innerness by Phragmén–Lindelöf) · origin: 2026-09-12 · where: `notes/riemann-channel-note.md`
- **OPEN (unverified since 2026-09-24)** — canonical alternating form on K_HW; graded-commutative product / finite model of K_S; the cusp-orbit return map of D2, D3 on the odd sector; Deninger's Laplacian route on the modular surface; the p-fibre of the 2018 system in the Bost–Connes MPOs of 04d · origin: 2026-09-23 · where: `docs/handoff-archive.md` (2026-09-23 entry)
- **OPEN (unverified since 2026-09-21)** — H-THETA numerically (Sonine evaluator Gram at level one; rank-one loss test); GL₁ bad-zero channel as a renewal channel; Burnol's two-dimensional causal model; level-N Eisenstein constant term (H-ARITH); genus-two class-group bond and theta divisor; Frobenius channel on the class-group bond; the two GL₁ cusps folded · origin: 2026-09-21 · where: `docs/handoff-archive.md` (2026-09-21 entries)
- **OPEN (unverified since 2026-09-21)** — square-roots-of-Ihara–Bass leads: two-step block K₁ of the graded Weil–LPS expanders; sign-twisted reversal as the channel analogue of the spinor twist; centred continuum reflection for the jump Lindbladians · origin: 2026-09-21 · where: `docs/handoff-archive.md` (2026-09-21 evening entry)
- **OPEN (unverified since 2026-09-20)** — cusp-toy leads: Γ₁(N) Eisenstein constant terms over F_q[T] (H-ARITH-1); glued toy as a fermionic MPS; Frobenius channel as a Weil-representation expander at p = 2; non-self-adjoint core for Θ′; cusp-plus-funnel toy; genus-two diagram (Lorscheid's Z/2 × Z/2 curve); Γ₀(N) with N a product of two primes; Arends–Peterson–Weich elliptic diagram over F₂; the even exit · origin: 2026-09-20 · where: `docs/handoff-archive.md` (2026-09-20 entries)
- **OPEN (unverified since 2026-09-19)** — give the vacuum an exit (unique mixed stationary state); arithmetic identification of the flag isometry U with the Bost–Connes bond; the necessary bound on |H_ab| as a filter · origin: 2026-09-19 · where: `docs/handoff-archive.md` (2026-09-19 entry)
- **OPEN (unverified since 2026-09-13)** — Lindblad/Phantasm leads: arithmetic representation or CP comparison map to the scattering bond; review of the ‖Z_t‖ = 1 argument, truncated-zero numerics, cutoff for Weil–LPS (Lubetzky–Peres); regular graded Q,R algebra with BC stationarity; Selberg-side H-CUSP-BRIDGE (Dyatlov–Guillarmou); circle-type graded expander from a representation; K-type grading of a PSL₂(R) channel; test (e) in the covariant cones of 04d; bond-cutoff family for 06h; summable-rate local model for 04g; an elliptic surface over F_q(t) as the next rung · origin: 2026-09-13 to 2026-09-16 · where: `docs/handoff-archive.md` (entries of 2026-09-13 to 2026-09-16)

### Tutorials and artifacts
- **OPEN** — Part E of the super-Ihara tutorial: the Ramanujan locus of K₄ on its three-torus and an SU(1,1) Krein mode (optional) · origin: 2026-10-05 · where: `notes/adelic-gkp/tutorial/`, `notes/adelic-gkp/gauge-groups.md`
- **OPEN (unverified since 2026-09-26)** — "Weil Positivity, Contracted" tutorial: a shard distilling the "Weil form = Gram of strips" dictionary table; the unexplained on-circle eigenvalue of the perturbed a = (0,1) Artin–Schreier matrix; Weil–LPS channels as a preset in the Kraus demo (needs n = p) · origin: 2026-09-26 · where: `notes/weil-tn-tutorial/`

### Housekeeping
- **HELD** — push the 7 unpushed commits (and this HANDOFF commit) to `origin/master` — TJO's decision · origin: 2026-10-28
- **HELD** — delete the five contained remote branches (list in State at a glance) — TJO's decision; all have 0 unique commits by `git cherry` · origin: 2026-10-28
- **HELD** — lift the hold on Claude work (usage credits) — TJO · origin: 2026-10-27
- **OPEN** — rebuild the PARI venv after a reboot (uv: cypari2, python-flint); no `gp` · origin: 2026-10-27, 2026-10-28 · where: `notes/astra-2026-10-27/brief.md`
- **OPEN** — gitignored local-only data (HKL clone, run artefacts, PDFs, `refs/src/`) exists only here and in `~/old`; keep `~/old` until backed up elsewhere · origin: 2026-10-28 · where: `notes/astra-2026-10-25/census/sources/`, `refs/src/`

### Done since listed
- **DONE 2026-10-28 (2b4deb6, bc3c9f5)** — astra reviews' MINOR fixes annotated on both 2026-10-27 Fable pages (2026-10-27 Next ii; INVALID/UNVERIFIED flagged in place, banners added).
- **DONE 2026-10-28 (9cbbc47, 124f036)** — endorsed record corrections annotated on `gauge-groups`, `graph-ihara`, `howe-positivity`, `graph-super`, `overlap-data`, `tower-pairing`, `cm-lift`, `no-lift`, `data-ladder` (2026-10-23 and 10-25 Next ii; `ff-dirichlet.md` needed none; remainder in Record corrections). Includes "Ω is the Casoratian, Q = ½Ω(M − qM⁻¹)" (2026-10-22 optional).
- **DONE 2026-10-28** — HANDOFF 2026-10-06 finding (F) correction annotated (below).
- **DONE 2026-10-28 (72cce0c)** — note on the `docs/worklog/2026-10-25.md` heading (nine lanes, not six).
- **DONE 2026-10-28 (d7d66d8)** — merge `refs/manifest-2026-10-06-pending.txt` (2026-10-06 Next ii): five ids re-fetched, 9/9 sha256 verified, in `refs/fetch_sources.sh` and `refs/manifest.sha256`.
- **DONE 2026-10-28** — stray `weil-bond-analytic.patch` deleted (patch-ids equal 5203468, 02d9eb2, 3e7ddb9; 2026-10-05 note).
- **DONE 2026-10-25 (027cece)** — lane T's pending PARI rerun (80/80 pairing values PARI = FLINT).
- **DONE 2026-10-25 (6be6518 to 17f9bd7)** — same-family REFUTE reviews of the 2026-10-23 round (0 INVALID); the cross-family part stays HELD.
- **DONE 2026-10-25 (2e3a1b9)** — J2′ for K₃,₃ by the HKL genus-6 census (refuted); cube and Petersen masks stay open.
- **DONE 2026-10-23 (272d160), checked 2026-10-25 (0609c6d)** — exact SU(2) Haar average for K₄ (two routes in review-gauge) (2026-10-05 Next iii).
- **DONE 2026-10-06 (31cf375)** — reduced one-lattice CM check of lane U (27/27); the ε-uniform form stays OPEN.
- **DONE 2026-09-27 (0997873)** — merge `claude/project-familiarization-8gondy` (2026-09-26 Next v).
- **DONE 2026-09-12** — `prop:ringnorm-trace` restated in shard 04 (archive "Next useful steps" 1c).
- **SUPERSEDED** — q = 8, a = 3 genus-blind case (F), 2026-10-06: pairing question answered by lane U.
- **SUPERSEDED** — 2026-10-23 correction wording "the Weil pairing sees the class": replaced by the genus statement.

## Session 2026-10-28: tidy-up after the 2026-10-27 hold (Haiku and Sonnet workers; no new mathematics)

TJO: "because of the messy stop: could you tidy everything up, integrate what can be done so cleanly, clearly demarcate unfinished/incomplete work. use haikus
and sonnets to do the work. goal in this session is to tidy up, reorg for clarity, recover, store and label". Orchestrator `claude:opus-5.5`; workers Haiku and
Sonnet subagents. No codex lanes, no Fable agents; `db/` and `report/` untouched. Worklog `docs/worklog/2026-10-28.md`.

**Done (7 commits on master, not pushed).** b30e363 sessions 2026-09-11 to 2026-10-02 moved verbatim from this file to `docs/handoff-archive.md` (diff-checked), restored
PDFs gitignored. Recovery from the X1 backup (`~/old`) by `rsync --ignore-existing`: `refs/src/`, the HKL clone, all lanes' run artefacts, compiled census binaries, the five
quasi-RH source PDFs; all gitignored, local only. d7d66d8 the five 2026-10-06 pending arXiv ids re-fetched and merged (9/9 sha256), `docs/notes-index.md`. 2b4deb6 and bc3c9f5
the astra reviews' verdicts annotated on both 2026-10-27 Fable pages, UNREVIEWED banners on both astra pages, `notes/astra-2026-10-27/STATUS.md`. 9cbbc47 and 124f036 the
endorsed record corrections of the 2026-10-23/25 rounds annotated on nine pages; `notes/astra-2026-10-23/STATUS.md`, `notes/astra-2026-10-25/STATUS.md`. 72cce0c worklog
note. This commit: this file (start-here, state, register; 2026-10-06 (F) annotated).

**Deliberately not done.** Tutorial §6d correction (published artifact: needs `test.js`, render, republish); `shard-draft/` wording (recorded in its README); four reviewer
remarks in tree-codes VALID items; the optional K₄ SU(1,1) family; no review, no proof, no registration. All endorsements are same-family: corrected pages are not
cross-family reviewed. Five remote branches fully contained in master (deletion awaits TJO). Everything unfinished is in the register above.

Nothing registered; gate 13 errors (was 261 before recovery).

## Session 2026-10-27: new machine, the 2026-10-25 round pushed; round `notes/astra-2026-10-27/` (tree of local GKP codes; Pizer graph as H¹ of X₀(p)); HELD before the Fable reviews

TJO: lattice Q² ⊂ A² and symplectic geometry yes, the overlap reading no; connect that space to the Ihara zeta; "two fable subagents and two astra
subagents ... each pair works out a proof, then they exchange and review"; then "hold all claude work; we are on usage credits". Worklog
`docs/worklog/2026-10-27.md`. Round `notes/astra-2026-10-27/` (`brief.md` binding; `tree-codes/lane-brief.md`, `pizer/lane-brief.md`; per topic a
blind astra prover `astra/` and a blind Fable prover `fable/`, each with `*-proofs.md`, `progress.txt`, `checks/`). **Nothing registered; gate
untouched; no record page edited.** Machine: PARI venv at `/tmp/claude-1000/-home-tobias-Projects-riemann-channel/dcae8e10-414e-4cb4-8b95-d35e159cfb50/scratchpad/venv-astra`
(uv; rebuild after reboot); no `gp`; `refs/src/` not fetched; old home at `~/old` (SquashFS).

**Done (all four provers and both astra cross-reviews finished; Fable reviews NOT run).**
- T, Fable (`tree-codes/fable/fable-proofs.md`): colours = code dimensions, neighbours = the p + 1 WH mutually unbiased bases, geodesics = transverse
  Lagrangian pairs, Ihara's Euler product over the primitive hyperbolic classes, the code-tower trace Tr(P_n D_a P_n) = |a|_p^{1/2} p^{min(v_p(1−a),2n)}
  (the orbit weight p^{−ℓ/2} as a trace of the squeeze D_{λ(γ)} with λ the eigenvalue ratio), explicit formula checked on X^{5,11}, X^{5,13}, X^{5,29};
  ledger: symmetric phase +uv/2; no Clifford implements a homothety; the squeeze belongs to γ²/det γ; X^{5,13} is bipartite. Astra review
  (`tree-codes/review-astra-of-fable/`): 12 VALID / 7 MINOR / 6 INVALID — INVALID: `prop:geodesic-squeeze` (nonsquare determinant unit obstructs a
  symplectic lift), `thm:ihara-zeta-squeeze-lefschetz` as displayed, the bundled claims of T4b (compression theorem VALID), the T5 sketch, C3, the
  Casoratian–intertwiner conjecture. T, astra (`tree-codes/astra/astra-proofs.md`): T1–T4 DONE, T5 PARTIAL; **unreviewed**.
- P, Fable (`pizer/fable/fable-proofs.md`): det(1 − B(ℓ)u + ℓu²) = (1−u)(1−ℓu) P_{X₀(p)/F_ℓ}(u) with every normalisation, 20 exact cells; Ramanujan =
  Weil for J₀(p); Ihara–Bass corrected for half-loops; G(p, ℓ) = Γ\T_ℓ for all p; the label lattice L₀ = {Σf = Σg = 0} has det Ω = n² = |Φ_p|² and
  is a third lattice in the isogeny class of J₀(37) (3-part at ℓ = 7), Ω|L₀ sketched as the doubled monodromy pairing. Astra review
  (`pizer/review-astra-of-fable/`): 9 VALID / 13 MINOR / 1 INVALID (the "iff q ∤ (p−1)/12" conjecture, refuted both ways) / 2 UNVERIFIED;
  `thm:pizer-ihara-zeta-x0p` and the half-loop lemma VALID; MINOR fixes listed in its verdict lines (displayed Weil form, #X₀(109)(F₇) = 10, edge
  indices at nontrivial stabilisers, the explicit degree-four isogeny J₀(37) → E₁ × E₂). P, astra (`pizer/astra/astra-proofs.md`): all items DONE
  (same half-loop and ℓ = 7 findings independently); **unreviewed**.

**Next (in order), when Claude usage allows.** (i) The two Fable REFUTE reviews of the astra proofs (`<topic>/review-fable-of-astra.md`; protocol in
`brief.md` "Design"). (ii) Apply the MINOR fixes of the astra reviews to the Fable pages (not record pages). (iii) Write the record page
`notes/adelic-gkp/tree-of-codes.md` from the VALID items of both topics (T1, T2, T4a, the code-trace theorem; P1, P2, P3a, the half-loop lemma, the
det Ω = n² obstruction) with the INVALID items as negative findings, then annotations to `graph-ihara.md` §2(b)/§3/§5, `data-ladder.md` §0 (a Pizer
rung) and §1.2. (iv) Then the list of 2026-10-25 below.

## Session 2026-10-25: nine astra lanes — five REFUTE reviews of the whole 2026-10-23 round, four new conjectures; all finished; record only

TJO: exploit the codex quota before its reset; up to six astras concurrently; use astras to review; stop launching at the reset
and land what was obtained; keep the work recoverable. Worklog `docs/worklog/2026-10-25.md` (one entry per lane, with numbers).
Round directory `notes/astra-2026-10-25/` (`brief.md` binding, incorporating the 2026-10-23 rules and adding the REFUTE review
protocol with `VERDICT <alias>: …` lines; lanes `review-tower`, `review-jacobian`, `review-gauge`, `review-average-canonical`,
`review-qrh`, `hhalf`, `census`, `irreps`, `shortrow`; each has `astra-proofs.md`, `progress.txt`, `checks/`). Nine lanes launched
06:06–06:36 UTC+1, all exited 0 by 07:02 (19–55 min), no resumes; each landed in its own commit as it finished. The HKL genus-6
census clone (`census/sources/hkl-genus-6/`, 4.6 GB) and compiled search binaries are gitignored. **Nothing registered; gate
untouched; no record page edited.** All reviews are SAME-FAMILY (`codex:gpt-6-astra` reviewing `codex:gpt-6-astra`); the gate
still wants a second-family review before promotion.

**Reviews of the 2026-10-23 round: 0 INVALID anywhere.** T: 13 VALID (the pending PARI rerun is done, 80/80 pairing values PARI =
FLINT; new D = −84 four-genus and D = −32 isolated-level tests). J: 16 VALID. H + K: 31 VALID. A + C: 26 VALID, 1 MINOR (wording of the
finite-certificate sentence), 1 UNVERIFIED (= the open all-genus row). Q1 + Q2: 32 VALID, 3 MINOR (Q1's 7/8 synopsis must read
P_x = (2 − 8x/9)(1 − x); a stray comma; the Cureton–Thorner theorem numbering lacks local provenance), 5 UNVERIFIED (= the five
OPEN proposals). Every record correction listed under 2026-10-23 below is endorsed (AGREE or AGREE-WITH-CHANGE with wording in
each review's closing section); additional ones: the graph Schur moment is a trace of M/√q, not A/√q; tutorial §6d's unconditional
endpoint sentence needs the parabolic-endpoint qualification; lane U's Tate "iff N | q^k − 1" needs exp(G_k[N]); delete lane U's
CM "not its conjugate".

**New results (all PROVED unless stated, none reviewed).**
- `census`: **neither Ramanujan K₃,₃ flux class is a Jacobian class over F₂** (complete Huang–Kedlaya–Lau census, 38,327 classes,
  cross-validated against the six strata; P₁ = 1 + 3T² + 4T⁴ + 8T⁶ + 16T⁸ + 48T¹⁰ + 64T¹², P₆ = 1 + 3T² + 12T⁴ + 24T⁶ + 48T⁸ +
  48T¹⁰ + 64T¹²), so **J2′ (nonnegative a_k ⟹ Jacobian class) is REFUTED**; **Petersen mask 22 IS a Jacobian class** (genus-10
  y³ = x¹² + x⁹ + x⁶ + x³ + 1, despite its supersingular factor); prism mask 6 (plane quintic) too, while K₃,₃ mask 6 shares its
  genus, 2-rank and first five counts: Jacobian-ness is not determined by rank and five counts. Cube 3, 5 and Petersen 6, 10 OPEN.
- `hhalf`: **RH on average for the hyperelliptic ensemble over F_q(t) for every odd prime power q and every genus g ≤ 7**, both
  conductor parities, by universal symbolic certificates on exact degree-reduced formulas; exact certificates to g = 25 at q = 3;
  fixed-genus large-q theorem. All-genus A1 / H-half OPEN (obstruction: adjacent nonsquare corrections at m ∝ g). Whole-cubic
  averages on the circle in all five tested cells; `conj:whole-squarefree-cubic-average` stated.
- `irreps`: the brief's classification refuted in every form; theorem: **the Haar average equals the HPS d-matching polynomial on all
  finite simple graphs iff Hall–Puder–Sawin's P1, iff equality on the triangle alone**; for irreps of dimension ≤ 3, uniform
  real-rootedness ⟺ matching equality ⟺ nontrivial determinant; every nontrivial real determinant-one representation fails on every
  cycle; SU(3) defining fails on C₃ though all its balanced moments match U(3); SU(d) average = Σ_C [2(−1)^d]^{|C|} μ_{d, Y∖V(C)}.
  **New OPEN `conj:conformal-sp4-average-real-rooted`:** the U(1)·USp(4) (= U(2) Sym³) average Σ_C μ_{4, Y∖V(C)} is real-rooted on
  every graph — proved on cycles, exact on all 971 connected cyclic graphs ≤ 7 vertices plus cube and Petersen, and NOT a matching
  polynomial: first candidate for a non-HPS universal RH-on-average family.
- `shortrow`: exact short-row Poisson formula for the sextic Möbius family (signed divisor-norm sum with gcd masks); the missing
  cell S(13, 5, 5) = 1 528 527 342 888 by two routes, 100 exact cells, ratio to the volume scale ≈ 0.85 with a small negative
  off-diagonal; **Weil ⟹ H-MS** (labelled comparison), so H-MS is true over F_q(t) and only a Weil-free proof is open (the uniform
  theta/transfer estimate); the proved complete-row estimate alone gives exponent 4/3 (nothing). Two shortcuts in the brief refuted.

**Brief errors caught by the lanes** (ledger for future briefs): the theta graph with three parallel edges is 3-regular; SU(1,1)
uses C² = +1 plus a separate Pfaffian doubling, not SU(2)'s J² = −1; both K₃,₃ masks are nonordinary; averaged traces are
coefficients of the averaged logarithm, not of the logarithm of the average; HPS standard S_d has dimension d − 1; the
simplified short-row diagonal holds only for h ≥ D − 1; lane T's same-order F₄₁ pair has no separating k.

**Next (in order).** (i) Second-family REFUTE review (claude:opus or human) of the 2026-10-23 PROVED items, now with same-family
reviews attached, starting with T1/T2, J, H + K; then of the four new lanes (census theorem and witnesses; genus ≤ 7 certificates;
the P1 converse; the short-row formula). (ii) Apply the endorsed record corrections (2026-10-23 list plus the additions above) to
`overlap-data.md`, `tower-pairing.md`, `cm-lift.md`, `gauge-groups.md` (wording in RG K6 and lane I §4), `graph-ihara.md` §8/§9,
`data-ladder.md` §0/§2/§4, `no-lift.md`, `howe-positivity.md`, `graph-super.md` §6/§9, `ff-dirichlet.md`, tutorial §6d, HANDOFF
2026-10-06 (F), `shard-draft/` row `prop:gkp-overlaps-see-order`; then register the reviewed rows. (iii) Open problems with finite
tests: `conj:conformal-sp4-average-real-rooted` (prove interlacing, or search ≥ 8 vertices); H-half uniform in g (control the adjacent
nonsquare corrections; compute m = 13 and genera 26–27 at q = 3); cube masks 3, 5 and Petersen 6, 10 (degree-2 covers of genus-4
bases, tetragonal models); a Weil-free H-MS (function-field Prop. 6.2 / 5.4 analogues); the integral polarized lattice of the K₄
trigonal and Petersen-22 Jacobians versus the graph Ω. (iv) Then the lists of 2026-10-23 and 2026-10-22 below.

## Session 2026-10-23: eight astra lanes (six conjectures from the record, two quasi-RH digests); all finished; record only

TJO: six ambitious directions from the whole repo, one `codex:gpt-6-astra` xhigh lane each; then two more to digest the
quasi-Riemann hypothesis (OpenAI 2026-09-30 / 10-05: every Dirichlet L-function zero-free in Re s > 7/8, statement Lean-formalised;
Kintali 47/48; Liu 0.874957…; Cureton–Thorner 31/32 for Dedekind zetas). Worklog `docs/worklog/2026-10-23.md` (headlines per lane).
Round directory `notes/astra-2026-10-23/` (`brief.md` binding; lanes `krein`, `haar`, `canonical`, `jacobian`, `average`, `tower`,
`qrh-digest`, `qrh-transpose`; each has `astra-proofs.md`, `progress.txt`, `checks/` with printed outputs). Sources in
`notes/astra-2026-10-23/qrh/sources/`. All eight exited 0 between 12:46 and 13:35 UTC. **Nothing registered; gate untouched; no
REFUTE review; no record page edited.** Every result is `codex:gpt-6-astra` on its own page.

**Headlines.** Five of the six brief conjectures were refuted with exact certificates, each leaving a sharper theorem: SU(1,1)
rigidity false (nonelementary Ramanujan holonomy exists; κ = half the real in-band multiplicity); RH on average fails for every
quaternionic irrep (Kramers squares) and holds for U(d) (= Hall–Puder–Sawin); Schur coordinates are not the "finite rank per
mode" datum (probe-dependent on the zeta window); the K₄ Ramanujan flux is a trigonal genus-4 Jacobian class over F₂ and every K₅
orbit a hyperelliptic genus-5 Jacobian class over F₃, but the unit-in-Z[F,V] and count-positivity conjectures fail; the hyperelliptic
average is on the circle for g ≤ 3 (all odd q) and reduces to an exact half-coefficient inequality, while cubic isotypic averages
fail; the torsion tower sees the order, the strict tower exactly the genus — lane U's q = 7 pair is Q(√−6), D = −24, h = 2, so its
separation stands as a genus separation. Quasi-RH: the fixed gap to 1/2 is the sparse amplifier (6/7 even with an unrestricted
mean square); Poisson is the Fourier gate exactly; the cubic theta is not a Z₃ qunaught; the large sieve is Gram positivity, not
Weil positivity; on F_q(t) the mechanism gives θ = 11/12 conditional on H-MS; on graphs the amplifier is refuted by equidistribution.

**Corrections the record needs (not yet applied; see each lane's closing section).** HANDOFF 2026-10-06 finding (F): "the Weil
pairing sees the class" → "the strict pairing tower sees the genus; class here because h = 2"; `tower-pairing.md` and
`overlap-data.md` likewise; `cm-lift.md`/`check_cm_tower.py` is the Q(√−7) example, lane U's is Q(√−6). `gauge-groups.md`: the
SU(1,1) and U(d)/SU(2) paragraphs (replacement text in lanes K and H). `graph-ihara.md` §8/§9: "Ω is the Casoratian,
Q = ½Ω(M − qM^{-1})". `data-ladder.md` §0: "the graph supplies an abelian-variety module; its isogeny class may or may not be a
Jacobian class"; §2: the failed geometric/level dichotomy as a negative finding; §§2, 4: the metaplectic family route to a strip
is a different kind of statement from the ladder's positivity. `shard-draft/` row `prop:gkp-overlaps-see-order`: wording only.

**Next (in order).** (i) REFUTE review (another model) of the PROVED items, lane by lane, starting with T1/T2 (the genus
theorem), J (the trigonal curve and the K₅ census), H (exterior-kernel formula, Pfaffian identity), K (Pfaffian/anti-isometry
argument). (ii) Apply the corrections above to the record pages. (iii) Open conjectures with finite tests: hyperelliptic-average
H-half for all (q, g); J2′ for Petersen, K₃,₃, cube (Huang–Kedlaya–Lau genus-6 census for K₃,₃); Q1-TRACE, Q1-EVAL,
Q2-THETA-SECTORS, C-SURF; the ε-uniform CM comparison of lane U with cypari2. (iv) Then the list of 2026-10-22 below.

## Session 2026-10-22: tutorial Section 6 expanded (the nullspace of the labelling, Ω as the Casoratian); record only

TJO: stuck for weeks on "Part B · 6 Phase space: two numbers per vertex" of the super-Ihara tutorial; "I don't get the symplectic
form, it seems like that there are nullspaces and stuff?" Worklog `docs/worklog/2026-10-22.md`. **Nothing registered; gate untouched.**

**Review finding.** The page claimed the span of σf, τg is 2n-dimensional. It is 2n − 1 (2n − 2 bipartite): σ1 = τ1, and the label
(1, −1) is an eigenvector of M with eigenvalue 1 (the trivial mode's line μ = 1), carried on the edge space by the cycle space instead.
So the phase space is the label space R^{2n}, Ω lives there and does not descend to the edge space, where B is self-adjoint for u·Fv.
Checked on all five graphs (ranks 7, 19, 14, 9, 83).

**Expansion.** Section 6 is now 6a–6d (`notes/adelic-gkp/tutorial/page.html`): the nullspace; M as the second-order recurrence
f_{k+2} = A f_{k+1} − q f_k (why two numbers per vertex); Ω as the Casoratian with M^T Ω M = qΩ as Abel's formula and S = M/√q as the
damping-removed Chebyshev recurrence; rotation / shear / squeeze; a table of which form lives on which space. Demo 6 shades and prints
the areas Ω(v_k, v_{k+1}). Built, tested (`test.js` all pass), rendered headlessly at 1280 and 390 px (no errors), artifact
https://claude.ai/artifact/2KbsLkFaW2pBBHs5r1NQxc republished in place.

**Next.** Unchanged from 2026-10-06 (below). Optional: carry the rank remark into `graph-ihara.md` §4, and decide whether that record's
"Q is the Casoratian" (§9) should read "Ω is the Casoratian, Q = ½Ω(M − qM^{-1})".

## Session 2026-10-06: orchestrated GKP session (Fable steering, Opus lanes, four REFUTE reviews); what data the zeros of ζ need (record only)

TJO: "install what you need ... orchestrate work ... explore the GKP connection comprehensively and build on the ideas of the previous sessions
... build up enough examples to understand what data we need for the classic Riemann zeta zeroes in the terms we discover here, ie the qunaught,
gkp, weil positivity ... use [the quota] all up today ... work until the quota reset then stop". Worklog `docs/worklog/2026-10-06.md` (second entry).
**Nothing registered; no shard; a draft shard exists.** Gate: 43 errors in this container with `refs/src/` fetched (5 script errors + 38 provenance
rows whose non-arXiv sources are absent); unchanged by the session.

**Read first:** `notes/adelic-gkp/data-ladder.md` ("The answer in one paragraph", then §§0–4d). Index of everything: `notes/adelic-gkp/adelic-gkp.md` §16.

**Pages** (`notes/adelic-gkp/`, each with `checks/check_<name>.py` and output; all checks pass; statuses inside): A `curve-bridge.md` (82), B `no-lift.md` (50),
C `cm-lift.md` (50), D `zn-flux.md` (87), E `cone-bridge.md` (42), F `overlap-data.md` (40), G `zeta-ingredients.md` (32), I `gate-phases.md` (32),
J `ff-dirichlet.md` (118), M `family-vacuum.md` (39), R `window-similitude.md` (25), S `repeated-root.md` (31), U `tower-pairing.md` (22); Fable's checks `check_family_weil.py` (51),
`check_step_powers.py` (38). Records: `citations-2026-10-06.md` (28 of 43 quoted theorems byte-cited after `refs/fetch_sources.sh`; five new sources in
`refs/manifest-2026-10-06-pending.txt`, to merge into the script and manifest), `registered-record.md` (today against `db/claims.tsv`: no registered
claim refuted or weakened; several items already registered, notably 04t `prop:weil-form-not-metric` for "Weil's form is the vacuum point"),
`shard-draft/` (04za, 20 claim rows, dry-run gate clean; reviewed-VALID statements stay `sketched` because every reviewer was Opus on Opus pages,
the gate's reviewer-equals-author rule). Reviews `notes/reviews/adelic-gkp-{lattice,arithmetic,zeta,ff-family}-2026-10-06.md`: 79 VALID / 17 MINOR /
3 INVALID; all three INVALIDs were Fable's readings in the synthesis and are corrected there; every MINOR is annotated on its page.

**Findings** (one line each; statuses on the pages). (A) The Riemann–Roch cokernel of the adelic qunaught maps by $S=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$
onto the companion lattice $\mathbb Z[F]$; Rosati $=$ vacuum form $\times\sqrt{4q-a^2}$; the Howe sign cancels; counts do not fix the lattice (class number).
Correction: the Pauli-six lattice is that of $y^2=x^3+4x\pm1$. (E) In genus $g$ the positive similitude forms are a cone; RH is its non-emptiness, witnessed by
the Weil form (positive iff $\Omega$ has type $\Phi_+$ and no real eigenvalue); the polarisation is a further point deciding integrality. (F) Overlaps see the
order, never the class; the Weil pairing sees the class. *[Correction 2026-10-28, endorsed by notes/astra-2026-10-25/review-tower: the strict pairing tower sees the genus; the class here only because h = 2 (lane U's pair is Q(√−6), D = −24).]* (B) Petersen and $K_5$ are Centeleghe–Stix objects with glued lattices and no arithmetic $J$ on the
supersingular block; "no lift" means "no canonical lift". (D) $\mathbb Z_N$ fluxes: lattice over $\mathbb Z[\zeta_N]$, $N$-torsion average $=$ matching polynomial
for every $N$. (C) The E mode lifts to 441d1; one lattice $\mathcal O_K$ and one vacuum for every Euler factor; 49a1 and 441d1 share them and differ in their
zeros. (I) The root number is the product of local Fourier-gate phases; the twins differ by a charged local state at 3. (J) Dirichlet characters of
$\mathbb F_q(t)$ have every ladder item at once (lattice, vacuum, charged states, gate phases, RH); needs $P_\chi$ squarefree. (M) Commuting similitudes share
a vacuum iff each satisfies RH; the LPS Hecke family shares none; $\zeta$'s prime family does. (G, R) For $\zeta$ the steps have exact adjoints, $\Omega_{\rm FE}$
and $\Omega_D$ are compatible with every step, Weil's form is the family-invariant point, the prime steps are exact similitudes (the window residual was an
artefact), and what is missing is finite rank: one atom per zero on every window against $2g$. (S) Companion constructions need squarefree $P$; Connes's
cokernel is of companion type (Jordan blocks for multiple zeros). (U) The tower's logical commutator with the step is the Weil/Tate pairing exactly and
separates the $q=7$ lattices at $N=8$: the tower is blind to RH but sees the lattice class; $\zeta$'s level-$N$ Bell pairs have a commutator but no step.

**The answer** (`data-ladder.md`, head): the data for the zeros of $\zeta$ in these terms are a finite-rank-per-mode integral structure on a global $H^1$
on which the squeeze generator acts integrally, plus a polarisation-type reason for its Lefschetz trace to be positive; the examples exclude the code's
overlaps and level tower, local lattices and vacua, Connes's cokernel as constructed, and Hecke-type families as sources.

**Fable-only stretch (from 09:29 UTC, TJO: "Only use fable from now on. No other subagents").** The REFUTE review of lanes R, S, U and a
Sonnet check of the one-lattice CM version of lane U were stopped unfinished and are listed under Next. Done by Fable alone: a coherence pass over
`data-ladder.md`; all fifteen check scripts re-run from the committed tree (739 checks, all pass); independent spot checks of lanes S and U
recorded on their pages; the reduced one-lattice CM check of lane U written and run (`checks/check_cm_tower.py`, 27/27); TeX Live installed and the lab book built in the dry-run copy with the draft shard registered (293 pages, no
errors, no undefined references; `shard-draft/README.md`).

**Next (in order).** (i) TJO's decision on registering `shard-draft/` (promotion to `proved` needs a reviewer of another model, per the gate). (ii) Merge
`refs/manifest-2026-10-06-pending.txt`. (iii) Full REFUTE review of lanes R, S, U (a partial one by Fable exists: `notes/reviews/adelic-gkp-rsu-fable-2026-10-06.md`, 12 VALID on the
recomputable or derivable statements, the pairing identities included; the 42 comparisons and the $N=8$ separation of lane U are unadjudicated); the $\varepsilon$-uniform version of the one-lattice CM check (`check_cm_tower.py` does the reduced form, 27/27). (iv) Shard 08j (unchanged). (v) Open items on the pages: which ideal class and principal form belong to
$\mathrm{Jac}(C)$ for the genus-two curve (E); the genus-blind case $q=8$, $a=3$ (F; the pairing question is answered by U); the Petersen twist and a Howe-type criterion for
Centeleghe–Stix objects (B); the CM version of the vacuum-point reading (G); $J(\mathbb F_{5^k})$ of the Fermat quartic (S); the twist family and higher
infinity types (I). (vi) The one question the day leaves: what plays the finite-field geometry over $\mathbb Q$.

**Environment this session.** numpy, scipy, mpmath, sympy, networkx, python-flint by pip; PARI/GP 2.15.4 with elldata by apt (cypari2 does not build;
`gp` by subprocess); `refs/src/` fetched (125 arXiv sources plus five new ones). Quota: only the unified seven-day window is visible to the session
(91% at 06:33 UTC, reset 16:00 UTC); no separate Fable line.

## Session 2026-10-05/06: the tutorial "super Ihara zeta from the ground up", Ihara–Bass by vectorisation, other gauge groups; everything merged onto master (Fable alone; record only)

TJO (cloud session): familiarise; see the day's GKP work; "create me a detailed artifact explaining this stuff in totally elementary yet
correct terms ... start with the graph, basic linear algebra ... animations, interactive demos"; "add a subsection that proves the ihara bass
formula ... using vectorisation / choi superoperators"; "what happens if we add a U(1), or an SU(2), or ... SU(1,1)"; "create handoff and merge
everything to main/master". Worklogs `docs/worklog/2026-10-05.md` (evening entry) and `2026-10-06.md`. **Nothing registered; no REFUTE
review; no shard.** Gate unchanged: 13 real errors (8 Yoshida rows, 5 round-2 scripts awaiting 08j).

**Merge.** `claude/weil-bond-analytic` (2026-10-01 analytic record; 2026-10-02/05 adelic-GKP note; the eight companion pages of 2026-10-05) was
a clean fast-forward of master and is now on master together with this session's files. The untracked `weil-bond-analytic.patch` on TJO's
machine is redundant with commits 5203468, 02d9eb2, 3e7ddb9.

**The tutorial** (`notes/adelic-gkp/tutorial/`, artifact https://claude.ai/artifact/2KbsLkFaW2pBBHs5r1NQxc, private). Eighteen sections,
fourteen live demos, every number computed in the browser from the chosen graph; the numerical core (`core.js`) is tested headlessly against
the recorded check outputs (`test.js`, all pass) and the page was rendered headlessly at desktop and phone width with no errors. Route: graph
and matrix → eigenvalues and walks → non-backtracking `B` → Ihara zeta and Ihara–Bass → the critical circle and RH for graphs → the phase-space
step `M`, the Weil form and Ramanujan → the three-gate circuit → flux, double cover, bosons and fermions, the super zeta, dark lines → RH on
average → GKP codes from scratch → the flux qubit on the cycle lattice → the syndrome torus and the E mode's counts → the tower and its
blindness → RH as an invariant vacuum and Deligne modules → dictionary, status table, glossary. The status table repeats the record's statuses.

**Ihara–Bass by vectorisation** (Section 4b of the page; elementary, standard in content, the shard-08 proof specialised). The edge space is the
vectorised adjacency pattern `P_A(V ⊗ V)`; the Hashimoto operator is the superoperator `B(Ψ) = A ∘ ((J − 1)Ψ^T)`, i.e. `B = P_A (K ⊗ 1) F`
with `K = J − 1` and `F` the swap; the rank-one `J` factors through the vertex space, so `B = τσ^T − F` with `σ^Tτ = A`, `τ^Tτ = σ^Tσ = D`,
`F² = 1`; factoring `1 + uF` (determinant `(1 − u²)^{|E|}`) and one Sylvester step give `det(1 − uB) = (1 − u²)^{|E|−|V|} det(1 − Au + (D − 1)u²)`
for any graph. Demo 4b checks each step on the running graph. Nothing used unitarity, so the identity holds for every gauge group.

**Other gauge groups** (`notes/adelic-gkp/gauge-groups.md`; discussion, statuses inside). U(1): gauge classes are the Brillouin torus of lattice
state 1 (Z_2 the half-periods, Z_N the N-th periods and GKP qudits); RH cannot hold near φ = 0 (continuity from q + 1; Kesten); RH on average
survives (matching polynomial); lattice state 2 needs roots of unity (CM by Z[ζ_N]). Nonabelian: holonomy sees π_1 and the tree, not H_1; no
comb; Fourier inversion over G replaces dark/bright by the phases χ_ρ(C); the U(d) Haar average is not the matching polynomial (balanced
tree-like trails survive), SU(2) more so (pseudoreal); S_d is known (Hall–Puder–Sawin); lattice state 2 needs finite image with an integral
representation. Noncompact SU(1,1): a squeeze on every edge; the Weil form becomes a Krein form (`η`-Hermitian `A_ρ`, similitude of `Ω ⊗ η`);
**RH and positivity separate** (a mode on the circle with negative Krein signature: the Krein-definite distinction of 04q, on a finite graph);
SL(2, Z) holonomy gives cat maps on the syndrome torus; no Haar average; temperedness (weak containment in the regular representation) is a
sufficient condition for the band, never met by finite-dimensional ρ.

**Next (in order).** (i) Shard 08j (unchanged, first). (ii) The record's T-a′, T-a″, T-b (REFUTE review of `graph-ihara.md`, `graph-super.md`
before registering anything). (iii) If wanted: a Part E of the tutorial (the Ramanujan locus of K_4 on its three-torus; an SU(1,1) Krein mode);
the exact SU(2)/U(2) Haar averages of `det(x − A_ρ)` for K_4 by Weingarten before any claim about their roots; byte-cite Stark–Terras,
Godsil–Gutman, Heilmann–Lieb, Hall–Puder–Sawin, Kesten.

## Session 2026-10-05: the GKP reading tested on graphs; the super Ihara zeta has two lattice states; the tower of lattices (Fable alone; record only)

Two parts. Morning (claude.ai sandbox): §14 of `notes/adelic-gkp/adelic-gkp.md`, the field extension $\mathbb Q(\sqrt2)$ (checks 14/14). Then a local session
(Claude Code), eight companion pages in `notes/adelic-gkp/` with rendered HTML, indexed in §15 of the note; checks `notes/adelic-gkp/checks/`
(`check_weil_qi.py` 29/29, `check_graph_gkp.py` 56/56, `check_super_gkp.py` 50/50, `check_lattice_tower.py` 45/45, `check_howe_positivity.py` 14/14, `check_sign_vector.py` 19/19, `check_locks.py` 7/7). Worklog `docs/worklog/2026-10-05.md`.
**Nothing registered; no REFUTE review; no shard.** Gate unchanged: 13 errors (8 Yoshida rows, 5 round-2 scripts awaiting 08j).

**Steer on method (TJO, verbatim; binding for the next sessions).** "Let us find the natural QI interpreations on the cases we understand *then* try to match
to corresponding analogous setting for standard RH. Not the other way around. I am not convincd by the overlap thing in the case of standard zeta."
So: the overlap/filter reading of the standard zeta (`weil-positivity-spectroscopy.md` §1, note Part II) is provisional and not to be built on;
`graph-super.md` and `lattice-tower.md` are the pages to build on.

**Findings (statuses in the pages).**
- `functional-equation-gate.md`: $\Theta$ is a qunaught because $\mathbb Q^2$ is Lagrangian; divisibility of $\mathbb Q$ is the separate rigidity statement. The gate
  behind the functional equation is the Fourier gate: modular $S$, the GKP Hadamard, not the GKP phase gate (the note's "S-gate" is annotated).
- `weil-positivity-spectroscopy.md`: explicit formula in echo form, $C_h(t)=$ zero modes $-$ primes $+$ real place (density $\theta'(E)/\pi$); seven equivalent forms of
  Weil positivity; an off-line zero is a gain–loss pair, Weil form versus Lorentzian (harmonic-measure) form. Standard material reorganised; checked.
- `graph-ihara.md`: a graph has no GKP code (its only lattice is $\pi_1$ in the tree, the analogue of the primes). What it has: on two quadratures per vertex the
  non-backtracking step is $M=\bigl(\begin{smallmatrix}0&-1\\q&A\end{smallmatrix}\bigr)$, $M^T\Omega M=q\Omega$, $M/\sqrt q=$ CZ along every edge $\cdot$ Hadamard on every mode
  $\cdot$ squeeze by $\sqrt q$ (the graph-state Clifford times a squeeze; literature not searched). Weil form $\mathcal Q=\bigl(\begin{smallmatrix}q&A/2\\A/2&1\end{smallmatrix}\bigr)=\tfrac12\Omega(M-qM^{-1})$,
  positive off the uniform mode iff $A^2\le4q$; negative index $=$ trivial eigenvalues $+$ off-band eigenvalues. Lines are bright (ordinary trace).
  $N_k(K_4)+3\,\#E(\mathbb F_{2^k})=4(2^k+1)+2(1+(-1)^k)$, $E:y^2+xy=x^3+1$ (spectral coincidence). Real violation: prism $C_{21}\times K_2$, invisible in Gram
  matrices of size $\le9$. Negative finding: the lattice index $|\det(m-nM)|$ carries no sign, so the count mechanism of curves does not transfer.
- `graph-super.md`: graph plus $\mathbb Z_2$ flux (a 2-cover; the notebook's graded quantum Ihara zeta in graph form, verified on the Pauli examples of 03c).
  (i) **Flux qubit:** the period lattice $H_1(Y,\mathbb Z)$ of the maximal abelian cover; bosonic sector $=$ comb, fermionic $=$ comb displaced by half a reciprocal
  vector, supertrace $=$ comb on the odd coset, so super counts $=2\times$ walks of odd flux; fermionic RH $\iff$ even and odd flux walks equinumerous up to
  $2nq^{k/2}$. (ii) **Syndrome torus:** $M_s$ preserves $\mathbb Z^{2n}$ (the lattice of $n$ GKP qunaughts); points are periodic syndromes,
  $\#=\det(1-M_s^k)$; $H^\bullet$ of the torus is the fermionic Fock space; for one fermionic mode the super zeta is the zeta of the toral map; the
  Pauli-qubit elliptic curve of 03c is the syndrome torus of one mode ($M=\bigl(\begin{smallmatrix}0&-1\\5&-2\end{smallmatrix}\bigr)$: 8, 32, 104, 640);
  $M=\bigl(\begin{smallmatrix}0&-1\\2&-1\end{smallmatrix}\bigr)$ gives $\#E(\mathbb F_{2^k})$. (iii) **RH on average over fluxes:** the flux-averaged fermionic
  numerator is the matching polynomial (roots strictly in the band, Heilmann–Lieb); for $K_4$, Petersen, $K_5$ only the zero flux and the all-negative
  flux fail. Lines are dark again with the signs of $\zeta$; the fermionic Weil form is positive definite outright. Still no Tate-type formula.

- `lattice-tower.md` (T-a, done the same session; checks 45/45). For an integer step $M$ on $L=\mathbb Z^{2n}$, $M^T\Omega M=q\Omega$, $V=qM^{-1}$: $(1-V^k)L$ is the
  stabiliser lattice of a GKP code $\mathcal C_k$ with basis $W(e)|L\rangle$, $e$ a syndrome of period $k$; $\dim=\det(1-M^k)$; logical Paulis $=$ Heisenberg group of
  $L/(1-M^k)L$; the step is a logical Clifford $\Phi$ of order $k$ (the Galois group), its orbits are the places, $\mathrm{Tr}(\Phi^j|\mathcal C_k)=h_{\gcd(j,k)}$, and
  Lefschetz reads "code trace $=$ Fock supertrace". Second tower $M^kL$ (index $q^{nk}$, the step nilpotent); torsion syndromes $=$ periodic $\oplus$ killed.
  **The tower is blind to RH**: the hyperbolic step $\bigl(\begin{smallmatrix}0&-1\\5&5\end{smallmatrix}\bigr)$ has all of it; only $h_k/q^{nk}$ leaves the Weil window.
  **RH is an invariant vacuum**: (RH, semisimple) $\iff$ Weil form $>0$ $\iff$ $S=M/\sqrt q$ fixes a pure Gaussian state (`thm:deninger-invariant-polarisation` with
  polarisation $=$ vacuum); then the zeros are oscillator frequencies, the trivial pair is the inverted oscillator $\tfrac12(xp+px)$, the one-mode lattice is the
  form $qx^2+\lambda xy+y^2$ (E mode: $\mathbb Z[\tfrac{1+\sqrt{-7}}2]$; Pauli six: $\mathbb Z+2i\mathbb Z$) and the tower is self-similar. **Ordinary case is a
  theorem**: $(L,M)$ is a Deligne module, so an ordinary abelian variety over $\mathbb F_q$ (Goresky–Tai `1701.07742:main.tex:561-591`, on disk): E mode, Pauli
  six, $K_4$ with one negative edge (rank 8 over $\mathbb F_2$); Petersen and $K_5$ examples are not ordinary. Not checked: Howe's positivity for $\Omega$; the group
  isomorphism $A(\mathbb F_{q^k})\cong L/(1-M^k)L$ (from memory). **Reading to carry over (§7 of the page, not a result):** look for the vacuum, not the tower; in
  the understood case the zeros are oscillator frequencies and the squeeze belongs to the poles, unlike the squeeze-frequency reading of the spectroscopy page.

- `howe-positivity.md` (T-a′, done the same session; `checks/check_howe_positivity.py`, 14/14, needs PARI via cypari2 in a scratch venv). $\Omega$ is positive
  for $\Phi_+=\{\mathrm{Im}\,\varphi(F)>0\}$ (the vacuum); Howe: it is a polarisation of Deligne's variety iff $\Phi_+=\Phi_\varepsilon=\{\mathrm{val}_p\varphi(F)>0\}$
  (Goresky–Tai `:3474-3497`, `:3556-3590`). Computed prime by prime in the splitting field: E mode and Pauli six, yes up to the sign of $\Omega$;
  **$K_4$ with one negative edge, no at all four primes** — proved in general when $\lambda$ and $-\lambda$ both occur (valuations do not see the sign, imaginary
  parts do); a $K_6$ flux with $q=5$ (eigenvalues $-2.759,-1^3,1.695,4.064$), yes at one of 16 primes: a principally polarised abelian 6-fold over
  $\mathbb F_5$ with the standard form. Repair for $K_4$: compatible forms are $\Omega(x,p(A_s)y)$; $P=A_s$ gives degree 25; the unit
  $P=\bigl(\begin{smallmatrix}-1&-2&1&1\\-2&-1&1&1\\1&1&-1&0\\1&1&0&-1\end{smallmatrix}\bigr)$ (eigenvalues $1,-1,\varphi^{-3},-\varphi^3$) gives a principal polarisation. Symmetry:
  a signed permutation $D$ with $DA_sD^{-1}=-A_s$, $D^2=-1$; $\Gamma=\mathrm{diag}(D,-D)$ anticommutes with the step, is antisymplectic, $\Gamma^2=-1$.
  **Correction to `lattice-tower.md` §6 (applied):** the vacuum $J_+$ and the lift's complex structure $J_\varepsilon$ differ by a sign per mode; they agree for one
  mode and for the $K_6$ flux, not for $K_4$ with one negative edge. Weil positivity is unaffected (the arithmetic Riemann form is $2\mathcal Q(x,|P|y)$).
  Isogeny class of the $K_4$ example over $\mathbb F_2$: $E_{2\,\rm pts}\times E_{4\,\rm pts}\times$ a simple surface; over $\mathbb F_4$: $E_1^2\times E_2^2$.

- `sign-vector.md` (done the same session; `checks/check_sign_vector.py`, 19/19, PARI). **One mode: the sign is free** (it is Deligne's $\varepsilon$); it compares
  the two ways of telling $\mu^\pm$ apart: the recursion $u\mapsto\lambda-q/u$ is a rotation at the real place ($+i0$ selects $\mu^+$, the vacuum) and a contraction
  at $p$ (it converges to the unit root; $\mathbb Z_p^2$ splits; the step moves one edge along a line of the tree of $p$-adic lattices). **Several modes: locking
  theorem (proved).** $D_j=\lambda_j^2-4q$ ($-D_j/4$ is the Weil-form determinant of mode $j$), $N^+$ the real field of the eigenvalues, $\mathrm{Rel}=\{I:\prod_ID_j\in(N^+)^{\times2}\}$;
  above a prime $\mathfrak p^+$ the realised sign vectors are exactly the solutions of $\prod_I\sigma_j=\tau_I$, $\tau_I=+1$ iff
  $\mathrm{val}(\rho_I-1)>\mathrm{val}(\rho_I+1)$, $\rho_I=(-1)^{|I|/2}\sqrt{\prod_ID_j}/\prod_I\lambda_j$. $\Omega$ is a polarisation iff all $\tau_I=+1$ at some
  $\mathfrak p^+$. Rational eigenvalues: locked iff same squarefree part $d$ of $4q-\lambda^2=dm^2$; same sign iff $\lambda/m\equiv\lambda'/m'$ mod $p$ ($q=5$: 2,4 anti-locked,
  $-2$,4 locked; $q=7$: 1,5 locked, 1,4 anti-locked). Agrees with PARI on 13 spectra. Scan: 527 ordinary Ramanujan flux classes of $K_4$, $K_5$, cube, $K_6$;
  $\Omega$ is a polarisation only for 120 $K_6$ classes (spectrum $(x+1)^3(x^3-3x^2-9x+19)$ or its mirror: four groups, no locks, all 16 sign vectors).

- `locks.md` (done the same session; `checks/check_locks.py`, 7/7, PARI and networkx). **A pairwise lock is a root-of-unity relation** (when $N^+$ has one
  prime above $p$): locked iff $\mu'_+=\zeta\mu_\pm$; sign $+1$ for $\zeta\mu_+$ (rotation), $-1$ for $\zeta\mu_-$ (rotation and reflection); proved. Integer
  eigenvalues: only half turn ($\pm\lambda$), quarter turn ($4q-\lambda^2=m^2$, partner $\pm m$; the Hadamard of the square GKP lattice) and sixth turn
  ($4q-\lambda^2=3m^2$, partners $\pm\tfrac12(\lambda\pm3m)$); checked for $q<400$. Prime-dependent lock: $q=11$, $\lambda=\tfrac12(-1\pm\sqrt5)$, $\mathbb Q(\zeta_5)$, signs $-1,+1$ at the
  two primes, no obstruction. **Bipartite graphs:** $D=\pm1$ by side, $\Gamma=\mathrm{diag}(D,-D)$ antisymplectic involution with $\Gamma M=-M\Gamma$; half lattice
  $T_+=\mathbb Z^{A}\oplus\mathbb Z^{B}$ Lagrangian; $\omega_+=\Omega(\cdot,(F+V)\cdot)|_{T_+}=\bigl(\begin{smallmatrix}0&B_s\\-B_s^T&0\end{smallmatrix}\bigr)$ (signed biadjacency), compatible with
  $F^2$, a GKP code of dimension $|\det B_s|$; for the cube all 31 ordinary Ramanujan fluxes are polarised by $\omega_+$ over $\mathbb F_4$ (15 principally). $K_4$:
  the anticommuting signed permutations have order four, no real half. No graph symmetry found behind quarter and sixth turns. **Scan** of 21069 ordinary
  Ramanujan flux classes (cubic $\le8$ vertices, 4-regular $\le7$, $K_7$): 8373 with a $\pm\lambda$ pair, 3274 lock-free, 1260 locked with all signs $+1$, 422 locked
  with a $-1$ (in $K_7$: $-1$ with $\tfrac12(1\pm\sqrt{57})$ in $\mathbb Q(\sqrt{-3},\sqrt{-19})$), 7740 undecided (real field too large). Smallest lock-free
  examples: a cubic graph on 8 vertices with one negative edge; the octahedron with three.

**Next.** (T-a′) Redo tower and vacuum on the half lattice for bipartite graphs (one quadrature per vertex, form $B_s$, Frobenius two steps); fluxes with
$\det B_s=\pm1$; the order-four symmetry of $K_4$ as a $\mathbb Z[i]$-structure; existence of the unit twist $P$ in general; Jacobian or Prym for the $K_4$
example; the non-ordinary examples. (T-a″) The matching question in the notebook's terms: an invariant vacuum on the odd bond of shard 04t. (T-b) REFUTE review of `graph-ihara.md` and `graph-super.md` before registering anything; byte-cite
Godsil–Gutman, Heilmann–Lieb, Marcus–Spielman–Srivastava. (T-c) The arithmetic graded examples (graded Weil–LPS of 03c): identify the flux and the
torus. Earlier next steps (G-a, G-b, N1′ genus two, N2′, shard 08j) unchanged. `weil-bond-analytic.patch` in the repository root is untracked and
redundant (its three patches are the three commits 5203468, 02d9eb2, 3e7ddb9 by patch-id).

## Older sessions

Sessions 2026-09-11 to 2026-10-02 (and the 2026-09-18 "Current state", the 2026-09-11 steering, the old "Next useful steps" and
"Environment" sections) are in `docs/handoff-archive.md`, moved verbatim on 2026-10-28.
