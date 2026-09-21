# Lane L17: the 2026-09-19 astra ideation session (briefs, messages, drafts, and where the stopped agents were)

Scope note. This lane covers the codex `gpt-6-astra` orchestrator rollout of 2026-09-19 morning and its five subagents. The final lane reports under `notes/rh-strategy-2026-09-19/` are ledgered elsewhere; this file records only what is **not** on disk there: TJO's own steering wording, the orchestrator's messages and framing, draft text that was later overwritten, material written outside that directory (`HANDOFF.md`, `docs/worklog/2026-09-19.md`, `scripts/`), the state of the two stopped agents, search methods used to find objects that the notes only state, and corrections/dead ends.

**Important coverage caveat.** Every inter-agent payload in these transcripts is a Fernet token (`gAAAAA...`) or an empty `Payload:` block. That means the orchestrator's *briefs* to the five subagents, the subagents' `send_message` reports back, and the orchestrator's mid-course steering messages are **not recoverable from these transcripts**. What is recoverable is: TJO's four prompts, the orchestrator's `### ASSISTANT` messages to TJO, every `### EXEC` shell body (file writes and calculations), and the subagents' `FINAL_ANSWER` payloads. Requirement (c) of this lane — "ideas the orchestrator raised in briefs that no subagent took up" — can therefore only be answered indirectly, by noting which of the orchestrator's own written ranked tasks were still untouched at shutdown (L17-020).

## Coverage

| transcript | lines | read fully? | final repo file | items found |
|---|---|---|---|---|
| `2026-09-19T11-20-25.txt` (orchestrator) | 667 | yes | `SESSION.md`, `SYNTHESIS.md`, `cmps-renewal-bridge.md`, `RECOVERY.md`, `HANDOFF.md`, `docs/worklog/2026-09-19.md`, `scripts/research_checkpoint.py` | 14 |
| `2026-09-19T11-22-06.txt` (cusp_bridge) | 133 | yes | `cusp-bridge.md`, `cusp_bridge_diagnostic.py/.json` | 3 |
| `2026-09-19T11-22-16.txt` (positivity_products) | 132 | yes | `positivity-products.md`, `positivity-products-check.py/.json` | 1 |
| `2026-09-19T11-22-27.txt` (graded_channels) | 173 | yes | `graded-channels.md`, `graded_channels_checks.py`, `regular_cmps_decay_check.py`, `regular_cmps_decay_exact.py` | 4 |
| `2026-09-19T11-29-25.txt` (riemann_selberg_modes, stopped) | 136 | yes | `riemann-vs-selberg-operators.md`, `riemann_selberg_toy_modes.py` | 2 |
| `2026-09-19T11-30-31.txt` (cmps_decay_comparison, stopped) | 100 | yes | `riemann-vs-selberg-cmps.md`, `riemann_vs_selberg_cmps_check.py` | 3 |
| `2026-09-19T11-20-26.txt` (sandbox-approval reviewer; skipped per brief) | 1295 | targeted greps only (it is the only transcript carrying **tool results**) | — | 2 |

Total entries: 24.

## Ideas and leads

### L17-001 TJO: decay modes are the unlock, and cMPS *ought* to be the right home for them
- Source: `2026-09-19T11-20-25.txt:143`; paraphrased one clause in `SESSION.md` ("Decay modes are central; cMPS should be the physically natural setting"), exact wording absent from every final file.
- Raised by: TJO (user prompt mid-session)
- Status at last mention: in a message only
- Content: TJO's exact words were "yes, decay modes is the crucial unlock in my opinion. The cMPS interpretation *ought* to be physically natural setting to represent decay modes correctly". The emphasis is normative, not descriptive: it is a claim that a correct representation of decay modes should fall out of cMPS structure rather than be fitted into it. Everything in the second half of the session — the renewal bridge, the regular fermionic toy, both second-round lanes — descends from this single sentence.
- Lead: the concrete reading the agents took is "derive the decay modes from local cMPS letters, including the stationary state, parity and environment coupling, and make the letters force a common width". If that worked, the common width would be a property of the letters rather than an assumption about zeros.
- Related: L17-002, L17-006, L17-007.

### L17-002 TJO: "precisely why is Riemann different to Selberg"
- Source: `2026-09-19T11-20-25.txt:184`; recorded only in summary form in `SESSION.md`.
- Raised by: TJO (user prompt)
- Status at last mention: in a message only
- Content: "spawn a couple more subagents to really dig into the decay mode story: I want to understand precisely why riemann is different to selberg here". This launched `riemann_selberg_modes` (operators/domains/scattering) and `cmps_decay_comparison` (letters, jump histories, stationary states). The orchestrator's own split of the question was: which decay modes belong to square-integrable Laplace eigenfunctions, and which belong to Eisenstein scattering (`:187`).
- Lead: the answer both lanes converged on is that for a Riemann scattering pole `s = rho/2` the Laplace parameter `mu = s(1-s) = 3/16 + gamma^2/4 + i gamma/4` is **nonreal even under RH**, so the Selberg mechanism (real `mu`, plus `mu >= 1/4`) cannot be transported. If a replacement mechanism were found, it would have to be an arithmetic rigidity of resonance widths, not a Laplace lower bound.
- Related: L17-007, L17-021, L17-022.

### L17-003 TJO: "I want the agent work to be continuously written so it is not lost"
- Source: `2026-09-19T11-20-25.txt:37`; consequences live in `scripts/research_checkpoint.py` and `RECOVERY.md`, not in a lane report.
- Raised by: TJO (user prompt, issued after only two agents had been spawned)
- Status at last mention: acted on
- Content: This directive changed the working method for the whole session: every agent was told to write its report to disk before reporting anything in chat, and the orchestrator built an atomic, checksummed snapshot tool (`--scope full` / `--scope session`) that captures the git-ignored `refs/src/` cache as well as the working tree. Each snapshot is re-read byte by byte before it is advertised as complete; a deliberately corrupted archive was verified to be rejected (`:426`).
- Lead: the snapshots are on the same disk as the repo, so they do not survive disk loss; the orchestrator explicitly said a completed archive plus its `.sha256` receipt should be copied to another disk. That copy was never made.
- Related: L17-018, L17-019.

### L17-004 The session's gap, in one sentence: no arithmetic reason forcing equal decay rates
- Source: `2026-09-19T11-20-25.txt:99`; absent from `SYNTHESIS.md` and every lane report in that wording.
- Raised by: orchestrator (message to TJO)
- Status at last mention: absent from final
- Content: "the repository can represent zeros as decay modes, but it has not found an arithmetic reason forcing equal decay rates. The agents are testing candidate mechanisms against the existing counterexamples." This is the sharpest available statement of what the whole riemann-channel programme is missing: representation is solved, rigidity is not. The final synthesis says the same thing over several paragraphs and a table, but never this compactly.
- Lead: none stated; it is a framing. Its operational form is the ranked task list in `SYNTHESIS.md`.
- Related: L17-007, L17-022.

### L17-005 The orchestrator's original four-lane design, including a parent audit lane
- Source: `2026-09-19T11-20-25.txt:27` (first `SESSION.md` draft); overwritten at `:298`, absent from the final `SESSION.md`.
- Raised by: orchestrator
- Status at last mention: absent from final
- Content: The first `SESSION.md` listed four planned lanes: (1) cusp/scattering bridge and spectral positivity; (2) Weil positivity, tensor amplification, arithmetic product substitutes; (3) graded channels, Lindbladians, finite models and no-go constraints; (4) **parent: repository/status audit, source preservation, cross-review, ranked synthesis**. The fourth lane is the one that disappeared from the record: the parent explicitly assigned itself cross-review and audit duties, which is why `cmps-renewal-bridge.md` exists and why lane reports carry cross-review sections.
- Lead: the design principle worth keeping is that a fan-out of this kind needs an explicit fourth "parent" lane for audit, provenance and synthesis, not just a dispatcher.
- Related: L17-018.

### L17-006 "Which observable should carry the Riemann modes?"
- Source: `2026-09-19T11-20-25.txt:286`; absent from final in this form.
- Raised by: orchestrator (message to TJO, after the graded lane's Checkpoint 5)
- Status at last mention: absent from final
- Content: "a regular fermionic cMPS has a mixed stationary bond and two decay bands, but its physical fermion two-point function sees only one band. That selection comes from the field insertions, without imposing a spectral projection. ... This may clarify which observable should carry the Riemann modes." The reframing is the important part: instead of asking which operator has the zeros as eigenvalues, ask which *observable* has them as poles. The full odd transfer of the `2|2` toy has eight modes; the emitted-fermion two-point function has four.
- Lead: for a prime-defined construction, specify the field insertion first and compute its observable subquotient, rather than computing a full transfer spectrum and then discarding modes. If it worked, the "extra" fast modes would never need to be explained away.
- Related: L17-007, L17-021, L17-023.

### L17-007 The orchestrator's closing diagnosis: three separate requirements, and the open one
- Source: `2026-09-19T11-20-25.txt:387-389`; the underlying facts are in the final files, this framing is not.
- Raised by: orchestrator (message to TJO)
- Status at last mention: absent from final
- Content: "Selberg's first-band argument connects decay modes to a self-adjoint Laplacian through a precise quadratic relation; the Riemann modes belong to the cusp scattering sector, where that spectral argument does not apply. ... fermionic structure explains why the observable sees only four modes, but a small admissible perturbation splits their decay rates. The remaining question is which arithmetic relation could enforce equal widths." The finite toy therefore separates three requirements that are easy to conflate: observable closure (from CAR / quadratic Hamiltonians), reflection symmetry (an involution `J` with `JNJ = -N`), and coercivity (`S >= 0`). Only the third is RH-sized.
- Lead: look for the arithmetic source of the *third* ingredient only. Symmetry and closure are cheap; the inequality is the theorem. If an arithmetic sum-of-squares or boundary-flux identity gave `S >= 0`, the finite mechanism would become a proof scheme.
- Related: L17-004, L17-021, L17-023.

### L17-008 The `HANDOFF.md` session entry: the session's lead in three sentences
- Source: `2026-09-19T11-20-25.txt:471` (heredoc that appends to `HANDOFF.md`); on disk at `HANDOFF.md:5` and following, i.e. **outside** `notes/rh-strategy-2026-09-19/`.
- Raised by: orchestrator
- Status at last mention: on disk but outside the ledgered directory
- Content: The `HANDOFF.md` insert states the main lead as: a regular fermionic cMPS with a faithful mixed stationary bond has a physical two-point function selecting a closed four-mode sector; its quadratic fermion structure supplies observable closure; a separate reflection and coercivity condition enforce a common width; perturbations distinguish these requirements. It also states what the operator lane delivered: separation of Selberg's `L^2` Laplace mechanism from Riemann's cusp wave/scattering leakage, an explicit candidate flow-to-wave intertwiner, and the location of Uetake's 2007 modal/completeness theorem.
- Lead: this is the paragraph a future session will actually read first; it is worth checking that it still matches whatever the ledger concludes.
- Related: L17-009, L17-021.

### L17-009 The worklog entry, and the validation it records
- Source: `2026-09-19T11-20-25.txt:471` and `:618`; on disk at `docs/worklog/2026-09-19.md`, outside the ledgered directory.
- Raised by: orchestrator
- Status at last mention: on disk but outside the ledgered directory
- Content: The worklog records the validation actually performed at shutdown: the reference manifest passed; `make check` passed with 357 claims and zero errors/warnings; six saved diagnostics reran successfully; session recovery extraction/hash verification passed and a deliberately corrupted archive was rejected. It also records the two infrastructure changes (recovery snapshots; exempting `research_checkpoint.py` from mathematical-evidence script parity) and the BLAS thread episode.
- Lead: none stated. The claim-status snapshot taken at the start of the session (`claim-status-summary.json`) is a useful baseline: 357 rows — 124 proved, 96 sketched, 59 cited, 34 numerical, 34 assumed, 7 open, 3 conjectured.
- Related: L17-016, L17-017.

### L17-010 Subagent shells had no direct network egress; only the parent's escalated `curl` and the web tool worked
- Source: `2026-09-19T11-22-06.txt:60` (the `urllib` attempt) and its receipt `notes/rh-strategy-2026-09-19/cusp-bridge-sources/1712.07832/retrieval.json`; the failure is mentioned in `cusp-bridge.md` but its cause is only in the transcript and the receipt.
- Raised by: subagent (cusp_bridge)
- Status at last mention: resolved by the parent
- Content: The cusp lane tried to fetch `https://arxiv.org/src/1712.07832` from inside its own sandbox and got `urlopen error [Errno -3] Temporary failure in name resolution`. The parent then fetched the same e-print with an escalated `curl` (`:126`) and unpacked it to `refs/src/1712.07832/`. The same pattern repeated for Uetake: the subagent could open pages with the web tool but could not download; the parent downloaded the publisher PDF under escalation (`:325`) and ran `pdfinfo`/`pdftotext` on it.
- Lead: in future fan-outs, route all downloads through the parent from the start; subagents should use the web tool for discovery only and hand URLs up. Doing otherwise costs a round trip per source.
- Related: L17-018.

### L17-011 The wrong shard formulas were diagnosed but deliberately left unrepaired
- Source: `2026-09-19T11-22-06.txt:80` (cusp lane Checkpoint 4); the diagnosis is in `cusp-bridge.md`, but the repair was explicitly deferred and has not happened.
- Raised by: subagent (cusp_bridge), confirmed independently by `riemann_selberg_modes` (`2026-09-19T11-29-25.txt:50`, point 5)
- Status at last mention: open action item, not executed
- Content: `report/sections/04_riemann_channel.tex:71-75` writes `Z(t)* k_lambda = exp(-i t conj(lambda)) k_lambda` and calls it decaying; for `lambda = gamma/2 - i beta/2` the real exponent is `+beta t/2`, i.e. growth. The same error is at `notes/riemann-channel-note.md:59-64`. The correct formula for the defined lower-half-plane compression is `Z(t) k_lambda = exp(i t conj(lambda)) k_lambda`, generator eigenvalue `-conj(rho)/2`, consistent with shard 04b:249-252. Numerically at `beta = 1/2, t = 1`: old modulus `exp(1/4)`, corrected `exp(-1/4)`.
- Lead: apply the correction to shard 04 and to `notes/riemann-channel-note.md` under the usual review discipline. Both lanes checked it independently, so the evidence is already there.
- Related: L17-022.

### L17-012 How the involution `J` was actually found: brute force over signed permutations
- Source: `2026-09-19T11-30-31.txt:64` and `:68`; the notes state `J` but not the search.
- Raised by: subagent (cmps_decay_comparison)
- Status at last mention: method absent from final
- Content: The reflection symmetry in `riemann-vs-selberg-cmps.md` is presented as "derived directly from the letters, with no diagonalization". It was in fact found by an exhaustive SymPy search over all 4! x 2^4 = 384 signed permutation matrices `J`, testing `J N + N J = 0` symbolically in the parameters `a, c, d`, and taking the first hit. A second inline computation then rotated to the `J`-eigenbasis with a fixed `U` and read off the off-diagonal blocks `A, B` and the product `AB`.
- Lead: this is a cheap reusable recipe for any candidate arithmetic letter family — search a small finite group of signed permutations (or the relevant Clifford/Majorana monomials) for an involution anticommuting with the centered drift, before attempting any spectral computation. It turns "is there a functional equation here?" into a finite check.
- Related: L17-013, L17-021.

### L17-013 How the positive metric `G` was found: a linear solve on the companion basis
- Source: `2026-09-19T11-22-27.txt:132` (an inline `linsolve` over a symmetric 4x4 ansatz) and `:136`; the notes state `G` but not the derivation.
- Raised by: subagent (graded_channels)
- Status at last mention: method absent from final
- Content: The rational metric `G = [[10496/27,0,-32/3,0],[0,32/3,0,-1],[-32/3,0,1,0],[0,-1,0,1]]` satisfying `K_comp* G + G K_comp = 0` on the letter-generated Krylov basis was obtained by writing a general symmetric matrix with ten unknowns and solving the linear system `K^T G + G K = 0` for the companion matrix `K_comp = [[0,0,0,-9/256],[1,0,0,0],[0,1,0,-11/8],[0,0,1,0]]`, then checking the leading principal minors are positive.
- Lead: same recipe for arithmetic letters: build the Krylov space from the physical insertion `R sigma`, reduce to companion form, solve the linear Lyapunov-type system for an invariant form, and test positivity by minors. The positivity, not the existence, is the content.
- Related: L17-012, L17-023.

### L17-014 The orchestrator's own renewal note carried a caveat that is easy to lose
- Source: `2026-09-19T11-20-25.txt:165` (the `cmps-renewal-bridge.md` draft); the sentence survived into the final file, which another lane ledgers, but it is the pivot of the whole session and is recorded here for cross-reference.
- Raised by: orchestrator
- Status at last mention: in final (cross-reference only)
- Content: "Identifying an actual fermionic output correlation requires the correct parity insertion; this note does not assume that every odd bond observable is already a physical local field insertion." The orchestrator drew the distinction between (i) no-jump modes of `Q`, (ii) physical transfer modes of `L`, and (iii) poles visible to specified correlation insertions, and demanded that a physical construction say which of the three carries the zeta divisor. Three days of prior repo work had not made that distinction.
- Lead: every future claim of the form "the zeros are the eigenvalues of X" should be forced to name which of the three objects `X` is.
- Related: L17-006, L17-021.

### L17-015 Reinsertion changes the physical spectrum even when the no-jump generator is preserved
- Source: `2026-09-19T11-20-25.txt:298` (parent's appended check); numbers are in `cmps-renewal-bridge.md`, the interpretive warning is worth repeating.
- Raised by: orchestrator
- Status at last mention: in final (cross-reference only)
- Content: For `B = -iX - diag(1,0)/2` the no-jump modes are `-1/4 +/- i sqrt(15)/4`. Resetting to `I/2` gives physical transfer modes `{0, -1/2, -1/2 +/- 2i}`; resetting to `diag(1,0)` gives `{0, -1/2, -1/4 +/- i sqrt(63)/4}`. Same no-jump object, different physical decay modes. Additionally, for target `sigma = diag(p, 1-p)` the required reset numerator has determinant exactly `-(1-2p)^2`, so **every biased diagonal target fails positivity and only the uniform target succeeds**.
- Lead: any proposal that builds the divisor into `Q` and then "adds a stationary state" must recompute the observable spectrum after reinsertion; it is not preserved.
- Related: L17-014, L17-024.

### L17-016 Two committed CI fixtures were BLAS-thread-dependent
- Source: `2026-09-19T11-20-25.txt:536-618` and the tool results in `2026-09-19T11-20-26.txt:905, 933-935, 1109, 1132-1133`; recorded only in `docs/worklog/2026-09-19.md`.
- Raised by: orchestrator (discovered while trying to commit)
- Status at last mention: partially fixed
- Content: The pre-commit hook re-runs seeded scripts and diffs them against `outputs/`. Two fixtures turned out not to be thread-count-invariant. `scripts/qihara_general.py` prints "trace formula m=1..4: max error 5.5e-12" at 2, 4 and 8 BLAS threads but **3.7e-12 at one thread**, so a single-threaded CI run fails. `scripts/graded_ramanujan.py` prints `str Sigma^n = [0.0, 0.0, 0.0, -0.0]` in the committed fixture but `[0.0, 0.0, 0.0, 0.0]` at 4 and 8 threads. Only the second was fixed, by adding `+ 0.0` after rounding in the printed string (a display-only change; the assertions use the unrounded array).
- Lead: `qihara_general.py` still embeds a thread-dependent printed rounding error in a committed fixture. Either print fewer digits, assert a bound instead of a value, or pin the thread count in `scripts/ci_local.sh`. This is a live reproducibility bug in the repo's own gate.
- Related: L17-017, L17-019.

### L17-017 `labbook_check.py` now exempts a third maintenance script
- Source: `2026-09-19T11-20-25.txt:410`.
- Raised by: orchestrator
- Status at last mention: applied
- Content: The gate previously required every `scripts/*.py` except `labbook_check.py` and `transcript_to_md.py` to have a matching `outputs/` fixture. `research_checkpoint.py` asserts no mathematical claim and produces no evidence, so the exemption list became a named set `maintenance_scripts = {labbook_check.py, transcript_to_md.py, research_checkpoint.py}` with a comment explaining the criterion.
- Lead: the criterion ("maintenance tools do not assert mathematical claims or produce evidence") is now the documented rule for future additions.
- Related: L17-016.

### L17-018 The recovery tool's design: verified-before-advertised snapshots including git-ignored sources
- Source: `2026-09-19T11-20-25.txt:80` (full script body), `:139` (`RECOVERY.md` body), `:426` (the verification/corruption test).
- Raised by: orchestrator
- Status at last mention: on disk as `scripts/research_checkpoint.py`, `.recovery/` git-ignored
- Content: Snapshots are written to a `.partial` file, then every archived byte is read back and checked against an embedded per-file SHA-256 manifest, and only then renamed and given an external `.sha256` receipt plus a `LATEST-{full,session}.json` pointer. Archives exclude `.git`, `.recovery`, caches and symlinks (symlinks are listed in the manifest as skipped), reject absolute or `..` member paths, and record the base commit. They restore the working tree, not git history. Crucially they include `refs/src/`, which is git-ignored, so the third-party source cache survives even though it is never published.
- Lead: the stated residual risk — same-disk storage — was never mitigated. One `cp` of the latest full archive and its receipt to another disk closes it.
- Related: L17-003, L17-010.

### L17-019 The gate was consuming ~64 cores and had to be killed and rerun
- Source: `2026-09-19T11-20-25.txt:526-538`.
- Raised by: orchestrator
- Status at last mention: worked around, not fixed
- Content: During shutdown the pre-commit hook's numerical suite stalled; `ps` showed a single Python check (PID 28154) oversubscribing about 64 CPU cores through BLAS. The orchestrator killed it and reran the identical hook with `OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2`, which completed and reproduced the recorded outputs (one thread did not — see L17-016).
- Lead: pin BLAS threads inside `scripts/ci_local.sh` (to 2, the value shown to reproduce the fixtures) rather than relying on the caller's environment. Commit `30ed6b6` was produced under the two-thread setting.
- Related: L17-016.

### L17-020 Ranked tasks that no agent reached before shutdown
- Source: orchestrator's `SYNTHESIS.md` ranked list (`2026-09-19T11-20-25.txt:344`), cusp lane's ranked tests (`2026-09-19T11-22-06.txt:105`), positivity lane's ranked tests (`2026-09-19T11-22-16.txt:113`); the tasks are on disk, the fact that they were untouched is only inferable from the transcripts.
- Raised by: orchestrator and subagents
- Status at last mention: raised, not taken up
- Content: Four written-down tasks had no agent working on them when TJO said "shut it all down". (i) Extend the cusp Gram/exit identity from leading Laurent modes to **generalized Laurent/Jordan data** at a synthetic double scattering pole — flagged as "the quickest useful theorem" and the one that avoids silently assuming zero simplicity. (ii) Test **SHW-style mixed rebound** on the finite Gram realization, to see which coherence sectors survive reinsertion. (iii) The **arithmetic product / Deligne tensor amplification** lane, explicitly deferred in the synthesis until a product with sublinear growth loss `epsilon_k = o(k)` is identified. (iv) The positivity lane's **nonlinear Schur/innovation recurrence** for the sparse prime Toeplitz updates.
- Lead: (i) is the cheapest and most informative: a single synthetic double pole, all bivariate Maass-Selberg Laurent coefficients including logarithmic cusp terms, the resulting confluent Cauchy matrix, and a comparison with repeated-zero Hardy kernel derivatives. Success gives a positive Gram identity with matching Jordan chain length; failure isolates a genuine obstruction.
- Related: L17-022, L17-024.

### L17-021 The four-mode selection is robust in the quadratic class and destroyed by one quartic term
- Source: `2026-09-19T11-30-31.txt:57, 72, 91, 100`; the conclusions are in `riemann-vs-selberg-cmps.md` (this entry records the perturbation ladder as a compact checklist).
- Raised by: subagent (cmps_decay_comparison)
- Status at last mention: in final (cross-reference), method worth reusing
- Content: For `H = diag(aX+bZ, cX+dZ)`, `R = X (x) |0><1|`, `P = Z (x) I`, the signed Heisenberg transfer preserves the four-dimensional Majorana span, and `R*` lies in it, so the output response can only have those four poles. Centering by `y = z + 1/4` gives `y^4 + alpha y^2 - 2bd y + beta`, so **`bd = 0` is necessary** for a common width. Perturbation ladder: `b = 1/100` keeps the four-pole selection but splits widths to `0.246221...` and `0.253778...`; `a = c = 1/20, d = 1/2` keeps the reflection but has discriminant exactly `-2399/10000`, so widths are `0.00608` and `0.49392`; adding `0.01 P` (a quartic fermion interaction, parity-even, stationary state unchanged) breaks observable closure and makes all eight odd poles visible with exactly degree-eight coprime denominator.
- Lead: the "smallest immediate arithmetic experiment" the lane named is to take the first proposed prime/cusp output letter, compute its signed Heisenberg image and first two commutators, and measure the component lying **outside** the proposed generating family. A nonzero uncontrolled component is the arithmetic analogue of the `P/100` term and kills the mechanism before any spectral numerics.
- Related: L17-006, L17-012, L17-023.

### L17-022 The exact algebraic candidate intertwiner between geodesic flow and the automorphic wave equation
- Source: `2026-09-19T11-29-25.txt:112` (Checkpoint 4); in `riemann-vs-selberg-operators.md` (cross-reference), recorded here because it is the single most concrete unexecuted lemma of the session.
- Raised by: subagent (riemann_selberg_modes)
- Status at last mention: algebraic identity proved, analytic theorem open
- Content: The automorphic wave equation `u_tt = (1/4 - Delta) u` has first-order form `W = [[0, I], [1/4 - Delta, 0]]`; for `Delta f = s(1-s) f` the decaying outgoing exponent is `q = s - 1/2`, while the geodesic first-band exponent is `lambda = s - 1`, whence `q = lambda + 1/2`. Setting `A = -X`, `C = A + 1/2` and `T u = (P u, P C u)` for a first-band Poisson pushforward `P`, block multiplication gives exactly `W T = T C`. So the missing flow-to-wave bridge has a concrete map to test rather than a matching of spectra. The lane also derived the cusp reduction: with `r = log y` and `u_0 = y^{1/2} v(r,t)`, `(1/4 - Delta) u_0 = y^{1/2} v_rr`, so `v_tt = v_rr` and the residue profile `v(r) = c e^{-q r}` is a free escape wave down the cusp.
- Lead: the four analytic conditions were listed: (a) the Bonthonneau-Weich pole exists with the claimed finite multiplicity; (b) `P` matches the Eisenstein Laurent chain and is injective on it; (c) `T` satisfies the outgoing cusp asymptotics; (d) the Lax-Phillips regular-data projection maps the chain into the genuine half-line generator domain preserving chain length. Proving (a)-(d) would connect two established resonance pictures **without using RH**.
- Related: L17-011, L17-020, L17-024.

### L17-023 The finite analogue of "quadratic relation then spectral bound"
- Source: `2026-09-19T11-30-31.txt:72` (Checkpoint 3), `2026-09-19T11-20-25.txt:445` (parent's synthesis insert); in final files, recorded here as the session's template.
- Raised by: subagent (cmps_decay_comparison), adopted by the orchestrator
- Status at last mention: in final (cross-reference)
- Content: With `b = 0` and `q = 1/4`, the involution `J` gives `J N J = -N`, `N` is off-diagonal in the `J`-eigenspaces, and for `a > q` the product of the blocks is self-adjoint in the positive metric `G = diag(a+q, a-q)`. In those coordinates minus the square is the real symmetric `S = [[(a-c)^2+d^2-q^2, -2d sqrt(a^2-q^2)], [-2d sqrt(a^2-q^2), (a+c)^2+d^2-q^2]]`, and `S >= 0` forces the common width. At the base point `S` has eigenvalues `11/16 +/- sqrt(7)/4`, both positive. This is a literal finite analogue of `lambda(lambda+1) = -mu` followed by `mu >= 1/4`.
- Lead: the arithmetic programme is now five explicit steps — closure of a finite odd observable family under the signed transfer; a letter-derived `J` with `J(A+1/4)J = -(A+1/4)`; reduction of the centered square to minus an arithmetic self-adjoint `S` in an independently defined positive form; a divisor identity for the selected output including archimedean factors; and a regulator theorem passing all of it to the infinite/critical limit. The third step is the RH-sized one.
- Related: L17-007, L17-012, L17-013, L17-021.

### L17-024 Uniform width as an exit-energy ratio, and why the cusp Gram does not supply it
- Source: `2026-09-19T11-22-16.txt:91` (positivity lane Checkpoint 6); in `positivity-products.md` (cross-reference).
- Raised by: subagent (positivity_products)
- Status at last mention: in final (cross-reference)
- Content: For a passive realization `A* G + G A = -C* C` with `G = int_0^inf e^{tA*} C* C e^{tA} dt`, an eigenmode `Av = lambda v` satisfies exactly `-Re(lambda) = ||Cv||^2 / (2 <v, Gv>)`. Uniform decay is therefore uniform exit energy per stored modal energy — a modal statement that needs no normality and no simplicity of zeros. But for the cusp data `A = diag(s_i - 1)`, `G_ij = 1/(1 - conj(s_i) - s_j)` the identity is `A* G + G A = -G - 11*`, whose modal width is `1/2 + 1/(2 G_ii)`: a mode-dependent extra escape term that exists throughout the strip and does **not** force equal widths.
- Lead: the operator lane sharpened this into the exact quantifier statement — demanding `||jv||^2 >= (1/2) ||v||^2` for *every* vector of a finite modal span is impossible for a one-row `j` in dimension above one, so "find a scalar dissipator" is the wrong target; the needed statement is **modewise**, for retained resonant eigenmodes only, and combined with the functional-equation pairing `b -> -1/2 - conj(b)` it would force width `1/4`.
- Related: L17-015, L17-020, L17-022.

## Where the stopped agents were

Both second-round agents had, in fact, finished writing their reports before `interrupt_agent` reached them (`2026-09-19T11-20-25.txt:455, 457`). Neither was cut off mid-derivation; both were cut off mid-housekeeping. The orchestrator then inserted the line "Final status: saved at user-requested shutdown" into both files (`:471`).

**`riemann_selberg_modes` (operators lane), `2026-09-19T11-29-25.txt`.** Last three actions:
1. `:112` — appended Checkpoint 4 to `riemann-vs-selberg-operators.md`: the Uetake verification (Theorems 4.2, 4.4, 5.1; `F(p) = xi(2p)/xi(-2p)`; eigenvalues of `-2 A_c` are the nontrivial zeros with algebraic multiplicity; the imaginary-spectrum criterion for `2 A_c + 1/2` is exactly RH), the normalization audit `S(tau) = [(2i tau - 1)/(2i tau + 1)] phi(1/2 + i tau)`, the domain caution against importing `dom(A_c) = dom(L) ∩ K`, and the exact wave intertwiner `W T = T C` (L17-022).
2. `:113, :117` — rendered PDF pages 12 and 16 of the cached Uetake paper to PNG and viewed them, to confirm the exact rational factor, the domain wording and the Theorem 4.4 formulas against the typeset original rather than the `pdftotext` extraction.
3. `:121, :122, :136` — wrote and ran `riemann_selberg_toy_modes.py` (the three-regime two-state passive model: `g = 1/2`, underdamped `w > 1/4` both widths `1/4`; overdamped `0 < w < 1/4` unequal widths summing to `1/2`, at `w = 1/8` exactly `1/4 +/- sqrt(3)/8`; threshold `w = 1/4` equal width with a nonzero nilpotent), then appended Checkpoints 5 and the final comparison table plus "Two precise next lemmas", ending "**Lane status: COMPLETE.**"

What it was about to establish: the tail of its last command was `rg --files refs/src/1403.0256` and `wc -l` on its own note — it was verifying that the local path it had cited for the compact first-band primary source (`refs/src/1403.0256/RuelleResonForHn.tex`) actually exists, having hedged in the note that "exact local source filename availability should be taken from `rg --files refs/src/1403.0256` if this catalog path differs". **That citation is therefore unverified.** It should be checked before the note's source register is trusted.

**`cmps_decay_comparison` (cMPS lane), `2026-09-19T11-30-31.txt`.** Last three actions:
1. `:91` — appended Checkpoint 4: exact rational recomputation of both output resolvents, reproducing `F(z) = 8z(z^2+z+1)/[5(8z^4+8z^3+14z^2+6z+1)]` at the base point and an exactly coprime degree-eight denominator under `H -> H + P/100`.
2. `:96` — appended to its script the exact weak-drive failure (`alpha = 77/200`, `beta = 621/6400`, discriminant `-2399/10000`) and a verification that the signed and plus-sign single-copy transfers are similar by **left** multiplication by the parity `P`, while their physical meaning and admissible insertions differ.
3. `:100` — appended the "Compact theorem and proof" (finite physical decay-selection theorem with full proof), the Riemann-vs-Selberg comparison table, the mixed-stationarity/critical-BC discussion, the five-step arithmetic programme, and the completion section; then ran `sha256sum` over its nine source inputs into `riemann-vs-selberg-cmps-sources.sha256`.

What it was about to establish: nothing further was queued — the `sha256sum` was the last step of its own completion checklist and it did produce the file on disk. The nearest thing to unfinished business is the item it named as the *next* experiment (L17-021): the signed Heisenberg image and first two commutators of the first prime/cusp output letter, and the size of the component outside the proposed generating family. It also left two questions explicitly open in its own text: whether the critical BC state admits a type-III/GNS formulation with specified domains (it refused to assert a type classification), and whether the toy's parity-closed ring norm can be identified with the Riemann explicit formula (it said neither it nor the physical correlation has been).

## Small but possibly consequential

1. `scripts/qihara_general.py` still prints a BLAS-thread-dependent rounding error (`5.5e-12` vs `3.7e-12`) into a committed fixture — the repo's own reproducibility gate can fail on a machine with a different thread count (L17-016).
2. The committed `outputs/graded_ramanujan.txt` was edited to turn `-0.0` into `0.0` and the script now adds `+0.0` after rounding; this is display-only, but it means a fixture was changed during a shutdown rather than during review (L17-016).
3. `refs/src/1403.0256` is cited in `riemann-vs-selberg-operators.md` as the compact first-band primary source, but the agent was interrupted at the exact moment it went to verify that path exists.
4. The cusp diagnostic's three-mode on-line centered defect norm was first written as "about 2.59" and silently corrected to "about 2.2544" (`2026-09-19T11-22-06.txt:100`); the number is load-bearing for the claim that the defect is nonzero under RH.
5. The recovery archives live on the same disk as the repository and were never copied off it, which the orchestrator itself flagged as the one residual risk (L17-018).
6. The four-lane plan's fourth lane — parent audit, source preservation, cross-review and ranked synthesis — was written down, executed, and then erased from `SESSION.md` when it was rewritten (L17-005).
7. Every inter-agent message in this session is unrecoverable ciphertext; if the briefs contained ideation the subagents did not act on, it is gone. Future fan-outs should have the parent write each brief to disk as it sends it.
8. `make check` recorded 357 claim rows with 7 open and 3 conjectured at the start of this session; no status was promoted by any of the five lanes, by design.

## Dead routes recorded

- **Naive Hadamard finite part of the cusp pairing gives the zero matrix.** `2026-09-19T11-22-06.txt:51, 61`. Subtracting the entire constant-term divergence entrywise from the unnormalized Maass-Selberg cross pairing leaves identically zero, not a positive resonance norm. Correction: use the normalized Cauchy Gram `K_ij = 1/(1 - conj(s_i) - s_j)` instead; different pairings, subleading Laurent data or nonlocal boundary terms are not ruled out.
- **The natural physical Gram cannot centered-unitarize more than one mode, even under RH.** `2026-09-19T11-22-06.txt:61`. `(A + 3/4)* K + K (A + 3/4) = (1/2) K - 11*`, and for `N >= 2` the right-hand side cannot vanish since `K` has rank `N` and `11*` has rank one. Correction: uniform widths with one exit *require* nonnormality; demanding centered unitarity in the physical norm would wrongly exclude the physically natural model.
- **"RH because the odd relaxation is an extremal expander rate" is unsupported.** `2026-09-19T11-22-27.txt:42`, citing `03c_graded_ramanujan.tex:132-144`. `E = (Ad I + Ad P)/2` kills the odd block, so no universal odd-sector Alon-Boppana floor exists.
- **Independent positive prime blocks cannot assemble Suzuki's kernel.** `2026-09-19T11-22-16.txt:56`. Each prime-power contribution at its first visibility on a symmetric interval is `w(2A-a)[[0,1],[1,0]]`, eigenvalues `+/- w(2A-a)`, i.e. indefinite. Correction: positivity must come from correlated cross-prime/archimedean compensation, not a sum of independent Gram blocks.
- **No bounded generator with a finite-energy boundary vector can realize the exact Suzuki covariance.** `2026-09-19T11-22-16.txt:102`. `Psi'(a+) - Psi'(a-) = -log p / sqrt(p^k)` at each prime-power time, so the diagonal has genuine kinks, whereas `V(t) = int_0^t e^{rB} b dr` is entire for bounded `B` and Hilbert `b`. Correction: the physical bridge needs an unbounded generator, distributional boundaries, or explicit prime-length delays; the cheap stopping test is to compute the jump at `log 2`.
- **Ordinary tensoring gives no amplification.** `2026-09-19T11-22-16.txt:63`. From `||T(t)|| <= M e^{ct}` one gets only `epsilon_k = kc`, recovering `Re lambda <= c` with no improvement. Correction: only the coefficient of `t` must be sublinear in `k`; prefactors `M_k` may be exponential. Test the exponential loss, not the dimension.
- **Adding dissipative prime noise after parity dephasing has spent the decay budget is impossible in the HS metric.** `2026-09-19T11-22-27.txt:57, 69`. If `L|_O + 2 gamma I` is HS-skew-adjoint then all jumps are scalar and `D = 0`, because the commutant of all off-diagonal block matrices is `C I`. Correction: the real letter problem is the tight-frame identity `C_O* C_O = 2c I_O`; `R = sqrt(gamma) P` supplies `4 gamma I_O` and exhausts a target `c = 1/4` at `gamma = 1/8`, so other noises must *share* the budget.
- **Finite positivity need not survive regulator removal.** `2026-09-19T11-22-27.txt:65, 140`. `C_n = [[2 - 1/n, 1], [-1, 0]]` has a positive invariant `G_n` with `lambda_min(G_n) = 1/(2n) -> 0`; the limiting companion has a nonzero Jordan nilpotent and admits no positive invariant metric.
- **The `2|2` Pauli two-jump toy is not a regular fermionic cMPS.** `2026-09-19T11-22-27.txt:69`. The two odd Pauli jumps `sqrt(1/8) X, sqrt(1/8) Y` violate kinetic regularity (`R_X^2 != 0`), and unitary remixing to raising/lowering jumps makes each square vanish but their anticommutator nonzero. Correction: the `C^{2|2}` one-fermion construction with `R = X (x) |0><1|` was built to replace it.
- **Reflection symmetry alone does not give uniform widths.** `2026-09-19T11-30-31.txt:72, 92`. At `a = c = 1/20, b = 0, d = 1/2` the involution `J` still satisfies `JNJ = -N` but the discriminant is exactly `-2399/10000` and the widths are `0.00608` and `0.49392`.
- **Passivity, complete positivity, one exit, stability and the functional equation together do not force a common width.** `2026-09-19T11-29-25.txt:122`. The two-state model with `g = 1/2` and `w = 1/8` is CPTP-completable, FE-symmetric about `-1/4` and strictly stable, yet has widths `1/4 +/- sqrt(3)/8`.
- **Uetake's stated generator domain must not be imported verbatim.** `2026-09-19T11-29-25.txt:112`. The p. 110 assertion `dom(A_c) = dom(L) ∩ K` is unsafe: the generator of a compressed half-line translation normally allows nonzero boundary traces whose zero extension is not in the whole-line derivative domain. This is a warning about an inference, not a refutation of the paper's meromorphic-model theorem.
- **Three tooling errors caught in flight, all fixed.** A NumPy `int64` broke JSON export of the odd-commutant dimension (`2026-09-19T11-22-27.txt:69`); SymPy matrix equality on unsimplified entries printed stationarity as `False` when it is identically zero (`:121`); SymPy's integer-polynomial `gcd` retains the constant factor `5`, so the simple-pole assertion had to test `degree(gcd) == 0` rather than `gcd == 1` (`:156`).
