# Lane L16: codex astra rollouts of 2026-09-14 afternoon, 09-15, 09-16 (drafts and messages not in the final files)

Transcripts read from
`/tmp/claude-1000/-home-tobiasosborne-Projects-riemann-channel/18bd05f5-a305-4d2f-afa3-4338fa074741/scratchpad/codex/`.
Citations below are `<transcript>.txt:<line>`; line 1 of every transcript is the rollout header,
lines 3-65 are the codex plugin boilerplate, and the orchestrator brief starts at line 66.

Method: every `apply_patch` / heredoc body in each transcript was un-escaped and extracted as a
separate draft fragment (43 fragments in total), then each fragment's added and deleted lines were
compared, after normalising LaTeX delimiters and whitespace, against the corresponding final repo
file. All `### ASSISTANT` messages and all `### USER/ORCHESTRATOR PROMPT` blocks were read in full.

## Coverage

| transcript | lines | read fully? | final repo file | items found |
| --- | --- | --- | --- | --- |
| `2026-09-14T14-56-39.txt` (Brief A, yolo Lindbladian, structure lane) | 260 | yes — brief 66-155, all 6 assistant messages, all 8 patch bodies extracted and diffed | `notes/yolo-lindblad/astra-structure.md` (+ `finite/structure_checks.py`) | 3 (L16-001, L16-002 draft/final verdict flips; L16-003 brief-level, shared with Brief B) |
| `2026-09-14T14-56-42.txt` (Brief B, yolo Lindbladian, finite model / zero hunt) | 411 | yes — brief 66-134, all 7 assistant messages, all 10 patch bodies extracted and diffed | `notes/yolo-lindblad/astra-finite-model.md` (+ 8 scripts in `finite/`) | 4 (L16-003, L16-004 declined brief items; L16-005, L16-006 message-only results) |
| `2026-09-14T16-38-51.txt` (zeta conditions, constructive lane) | 349 | yes — brief 66-196, all 7 assistant messages, all 12 patch bodies extracted and diffed | `notes/zeta-conditions/astra-constructions.md` (+ 13 scripts) | 7 (L16-007 to L16-013; four are genuine draft/final changes) |
| `2026-09-15T08-37-49.txt` (graded Ramanujan, D1-D14) | 246 | yes — brief is the repo file `notes/ramanujan-graded/astra-brief.md` (byte-identical), all 7 assistant messages, all 15 patch bodies extracted and diffed | `notes/ramanujan-graded/astra-proofs.md` (+ 3 scripts) | 7 (L16-014 to L16-020; L16-020 is a cut alternative example) |
| `2026-09-16T14-21-08.txt` (Selberg letters, D1-D8) | 302 | yes — brief 66-148 (identical to `notes/selberg-letters/astra-brief.md`), all 7 assistant messages, all 6 patch bodies extracted and diffed | `notes/selberg-letters/astra-proofs.md` (+ `finite/check_letters.py`) | 6 (L16-021 to L16-026) |

**Important negative finding, stated once for all five sessions.** The astra prover wrote these
reports essentially linearly: successive `apply_patch` drafts *add* material and almost never
delete it. After normalising the LaTeX delimiter change (`\( \)` in the drafts, `$ $` in the
Selberg final) the diff of every draft fragment against its final repo file yields **no paragraph
of mathematics that was written and then abandoned**, with the small exceptions catalogued as
L16-001, L16-002, L16-007, L16-008, L16-009, L16-010 and L16-020 below. I checked the few
apparent drops individually and found each of them present in the final file in reworded form
(examples: the character fibre-sum formula `V_p^* g_chi = 0 or p^{-1/2} sqrt(phi(b)/phi(d)) g_eta`,
`astra-structure.md:150`; the "Haar is not pure on C(Zhat)" paragraph, `astra-structure.md:265`;
the "no UNVERIFIED-MEMORY" closing of §6.4, `astra-structure.md:521`; the elliptic-conjugacy
scattering-order formula, `selberg-letters/astra-proofs.md:367`; the Green's-identity derivation
of the Maass-Selberg relation, `selberg-letters/astra-proofs.md:385`).
The four orchestrator briefs in the transcripts are byte-identical to the repo copies
(`astra-brief-A.md`, `astra-brief-B.md`, `zeta-conditions/astra-brief.md`,
`selberg-letters/astra-brief.md`), so no brief text is lost either.
Consequently this lane's yield is concentrated in (a) verdicts that *changed between drafts*,
(b) things the briefs asked for that were never built, and (c) the dead routes.

## Ideas and leads

### L16-001 The S8 "no stationary density" verdict flipped from PROVED-CONDITIONAL to CORRECTED
- Source: `2026-09-14T14-56-39.txt:221` (draft ledger row), overwritten at `:236`/`:241`; the draft row is absent from `notes/yolo-lindblad/astra-structure.md`.
- Raised by: codex prover
- Status at last mention: cut from final (replaced by a stricter verdict)
- Content: An intermediate draft of the correction ledger read "S8: forward dynamics have no normal stationary density. | **PROVED-CONDITIONAL** | Finite or summable rates; elementary valuation proof §8.2. Original 1/p cutoff fails earlier in §5.5." The final ledger downgrades this to **CORRECTED**, because with the brief's rates `lambda_p = 1/p` the generator does not define a semigroup at all (the no-jump quadratic form `sum_p lambda_p` diverges), so there is nothing to have a stationary state. The intermediate wording is the useful one: with *summable* rates, e.g. `lambda_p = p^{-beta}`, `beta > 1`, the absence of a normal stationary density is an honest theorem, proved by a valuation argument on the shell index.
- Lead: fix `lambda_p = p^{-beta}` with `beta > 1` and treat the `beta -> 1+` limit as the critical limit rather than starting at `beta = 1`; then §8.2's valuation proof applies verbatim and one can ask what the stationary object degenerates into as `beta -> 1`. Consequence if it worked: a well-posed one-parameter family whose critical endpoint is the object the brief wanted.
- Related: L16-002, L16-005.

### L16-002 The Gram-condition-number evidence (10 -> 700 over 3000 zeros) was re-read: only *unbounded* growth refutes the Riesz property
- Source: `2026-09-14T14-56-39.txt:221` (draft row "S7: Gram growth 10 to 700 proves an obstruction or an RH conclusion. | **CORRECTED**"), superseded at `:236`/`:241`; final ledger row reads "S7: significance of the recorded Gram growth 10 to 700. | **PROVED-CONDITIONAL** | H-GRAM".
- Raised by: orchestrator brief (`:137-142`, statement S7) then corrected by the prover, then re-corrected between drafts
- Status at last mention: corrected in final (verdict flipped CORRECTED -> PROVED-CONDITIONAL)
- Content: The notebook had recorded that the Gram matrix of the candidate eigenvector system grows in condition number from about 10 to about 700 across the first 3000 zeros, and the brief asked why that bears on the converse to "uniform dephasing implies a vertical spectral line". The draft called the inference simply wrong; the final says instead that under a labelled hypothesis H-GRAM the number is a legitimate *test statistic*: a Riesz basis requires `kappa(N)` bounded as `N -> infinity`, so only unbounded growth would disprove the candidate, and growth from 10 to 700 over a finite window decides nothing.
- Lead: compute `kappa(N)` for N well beyond 3000 and fit its growth; if `kappa(N)` saturates, H-RIESZ becomes plausible and the metric converse of §7.4 (H-RIESZ, H-FREQ, H-DOM) can be attempted; if it grows like a power of N, the whole "uniform dephasing gives the line" route is dead for that vector system.
- Related: L16-001.

### L16-003 The archimedean side of the guess was never built: no oscillator ladder, no `D = x d/dx + 1/2`
- Source: brief A `2026-09-14T14-56-39.txt:92-99` (the guess includes "the Gamma-factor (harmonic-oscillator) ladder on L2(R_+^*); plus a Hamiltonian D = x d/dx + 1/2"); brief B `2026-09-14T14-56-42.txt:93-101` ("Optionally add a truncated harmonic oscillator (levels k = 0..K) on the archimedean side with translation T_{log p} realised as exp(log p * (a - a^+)) or as the shift on a grid"); final `notes/yolo-lindblad/astra-finite-model.md:62` states flatly "No harmonic oscillator or archimedean Hamiltonian is added."
- Raised by: orchestrator brief
- Status at last mention: raised, not pursued (declined by both lanes)
- Content: Both 09-14 afternoon lanes worked with the phase (profinite) factor alone. The structure lane corrected `D = x d/dx + 1/2` to "fix the measure and take the self-adjoint `-iD`" and left the oscillator ladder OPEN; the finite lane simply built no archimedean factor. So every negative result of 09-14 (no poles in the strip, no critical-line relaxation modes, no pole at `s = 1`) is a statement about the phase factor only.
- Lead: build the truncated oscillator `k = 0..K` with `T_{log p} = exp(log p (a - a^dagger))` or a log-grid shift, tensor it onto the shell ladder, and rerun the N4 hunt; the archimedean factor is exactly what supplies the completion (Gamma factor) that §5.7 showed is missing to remove the spurious pole at `s = -2`. Consequence if it worked: the first honest test of whether the completed object, not the bare phase object, has strip structure.
- Related: L16-004, L16-005.

### L16-004 The optional figures of the singularity hunt were never produced
- Source: brief B `2026-09-14T14-56-42.txt:128-131` ("figures optional (save as PNG in the same directory)"); no PNG exists under `notes/yolo-lindblad/finite/`.
- Raised by: orchestrator brief
- Status at last mention: raised, not pursued
- Content: The hunt reports argument-principle windings and interior meshes as tables only. A picture of `|F(s)|` or of the winding phase over the rectangle `Re s in [0.3,1.2]`, `Im s in [0,40]` would make the clean negative legible and would show at a glance that the only structure is the real prime-sum pole.
- Lead: `python3 notes/yolo-lindblad/finite/hunt.py` already computes the mesh; adding a contour plot is a few lines. Low value, recorded for completeness.
- Related: L16-003.

### L16-005 The exact vacuum return function of the finite model, stated first in a message
- Source: `2026-09-14T14-56-42.txt:197-201`.
- Raised by: codex prover
- Status at last mention: stated in a message, then carried into the final report
- Content: Mid-run the prover announced the closed form `F(s) = 1 / (1 - sum_{p <= P} p^{-(s + beta + 1)})`, and noted the point that matters: **it is independent of the shell cutoff** `B`. The Euler-product ("multiset") companion is `zeta_P(s + beta + 1)`. So the ordered-word resolvent has a *prime-sum* denominator and the multiset object has an Euler product, and the difference between them is exactly the word-multiplicity factor; no amount of enlarging the shell space changes this.
- Lead: since `F` does not depend on `B`, the only free knobs are the rates and the length weight. Ask which rate family `lambda_p` makes `1 - sum_p lambda_p p^{-s-1}` have zeros anywhere near the critical line; the answer is a constraint on `lambda_p` that can be written down directly, and if no admissible (positive, summable) family works, the ordered-word route is closed for good.
- Related: L16-001, L16-003.

### L16-006 "Individual edge jumps" as a repair that does make Gibbs weights stationary
- Source: `2026-09-14T14-56-42.txt:241-243` (message), carried into `astra-finite-model.md:391` in one sentence.
- Raised by: codex prover
- Status at last mention: stated in a message and recorded in one line of the final; not developed
- Content: The brief's detailed-balance proposal (reverse jumps `V_p^dagger` at rate `lambda_p p^{-beta}`) fails twice: the orientation of the rates is backwards (the required ratio is `d_p/u_p = p^beta`), and even after reversing it the *phase* jumps keep creating off-diagonal shell coherences, so the diagonal Gibbs state is not stationary. The prover's separately labelled repair replaces the global prime isometries by **resolved individual edge jumps** `b -> pb` (one Lindblad operator per edge of the shell graph rather than one per prime), which does preserve the diagonal Gibbs state.
- Lead: write the edge-jump generator out explicitly and ask whether it still has any arithmetic content — it is a classical birth-death chain on the divisor lattice, so the question is whether anything of the Bost-Connes structure survives the resolution. If nothing does, that is a clean statement of the cost of imposing detailed balance.
- Related: L16-001.

### L16-007 The "half-entropy is RH" reading was reversed between drafts: it is C5 without C4
- Source: `2026-09-14T16-38-51.txt:291` (draft table rows "half entropy regular | ... | N at κ=2 | ..." and "half entropy TP alternative | ... | N at κ=-1 | ...", plus the paragraph "λ_-=λ_+/2 is true in the growth convention but is **not** C5"), deleted at `:298`; final rows read "Y at prescribed κ=2" / "Y at transported κ=-2" (`astra-constructions.md:156-157`) with the explanation at `:160`.
- Raised by: codex prover (both versions)
- Status at last mention: corrected in final
- Content: The notebook's slogan "the odd sector is a sub-system with half the entropy, therefore RH" was first judged outright false for the continuum half-entropy cMPS, on the grounds that RH is an *additive central line fixed by a functional equation*, not a ratio of growth exponents. The final judgement is more precise and more useful: `lambda_- = lambda_+/2` does pass the central-line test, but only relative to an *explicitly prescribed* reflection `lambda -> 2 - lambda`, and the divisor does not obey that reflection. So the example has **C5 without C4** — RH-shaped spectrum with no functional equation selecting the centre. Shifting the spectrum by `-2` transports the target to `lambda -> -2 - lambda`, showing that "half of a growth exponent" is not invariant under growth shifts.
- Lead: whenever a candidate is described as "half entropy = RH", first ask which FE fixes the centre; if none is exhibited, the claim is empty. Conversely, look for a graded cMPS where the FE and the half-entropy relation pick out the *same* centre — that is the missing C4+C5 example.
- Related: L16-008, L16-014.

### L16-008 Failure of `R_b R_f = -R_f R_b` is a failure of the regular-matrix ansatz, not a proof of infinite kinetic energy
- Source: `2026-09-14T16-38-51.txt:329` (final patch replacing the earlier sentence "this alternative fails finite-kinetic-energy regularity"); final text at `astra-constructions.md:335`.
- Raised by: codex prover
- Status at last mention: corrected in final at the last edit
- Content: The TP alternative for the half-entropy cMPS uses a fermionic jump `R_f = [[0,1],[0,0]]` and a bosonic `R_b = Pi/2`; these do not anticommute, so the standard algebraic kinetic-regularity relation `R_a R_b = (-1)^{p_a p_b} R_b R_a` fails. The draft concluded the cMPS "fails finite-kinetic-energy regularity"; the last edit weakens this deliberately — the *ansatz* fails, and nothing has been shown about the kinetic energy of the state itself.
- Lead: look for a larger-bond or non-minimal presentation of the same ring state whose `(Q, R)` do satisfy the graded commutation relation. If one exists, the half-entropy cMPS becomes a fully regular example and the "K fails" column of the C1-C10 table changes.
- Related: L16-007.

### L16-009 `C6curve` was renamed `C6projective` and its content changed
- Source: `2026-09-14T16-38-51.txt:291` ("A requirement that the only other nonzero even eigenvalue be exactly `1` is an **additional curve-divisor constraint**, denoted C6curve here"); absent from the final, which at `astra-constructions.md:98` instead says "Requiring the full projective even pair `{1,q}` is a stronger divisor constraint, denoted C6projective here."
- Raised by: codex prover
- Status at last mention: cut from final (superseded by a different condition)
- Content: Two inequivalent strengthenings of the ergodicity condition C6 were in play. The draft's C6curve says: apart from the Perron root `q`, the only other nonzero even eigenvalue is `1` (the `H^0` pole). The final's C6projective says: the even spectrum contains the full pair `{1, q}`. The first is a *prohibition* on extra even modes, the second a *requirement* that a specific pair be present. Both are "curve normal form" conditions but they cut different examples.
- Lead: keep both names in the condition ledger; a tensor satisfying C6curve but not C6projective (no `H^0` at all, e.g. the affine rungs) and one satisfying C6projective but not C6curve (extra subleading even modes) would separate them cleanly.
- Related: L16-010.

### L16-010 The FE-failing / RH-satisfying witness was simplified: the extra even pole at `u = 1/2` is not needed
- Source: `2026-09-14T16-38-51.txt:258` (draft `independence.py` family with `('FT', r=2, x=4, y=4, FE=False, RH=True)` and the comment "FT has an extra even pole at 1/2, so it is not curve normal form"), corrected at `:324`; message `:320` ("the FE-failing, RH-satisfying example can use the allowed affine spectrum {q}, with an even zero mode, so no extra pole is needed"); final at `astra-constructions.md:1742` ("FT has only the pole at 1/16: the even zero mode is invisible to positive powers").
- Raised by: codex prover
- Status at last mention: corrected in final
- Content: The brief (D6) asked for tensors realising every combination of (C4 FE, C5 RH, C6 unique fixed point). The first attempt at the FE-fails / RH-holds corner used a second even eigenvalue `r = 2`, which bought an extra pole at `u = 1/2` and pushed the example out of curve normal form. The consistency pass found that `r = 0` works: the even zero mode contributes nothing to any positive power trace, so it is invisible in the counts, and the example stays inside the allowed affine spectrum `{q}`. All eight (C4, C5, C6) combinations then fit with the intended presence or absence of `H^0`.
- Lead: the general principle worth recording is that **even zero modes are free**: they change the bond and the fixed-point structure without moving any divisor point in the `u`-plane. This is the cheapest way to decouple C6 from C4 and C5, and it is the same trick as the "idle qubit" that destroys uniqueness without moving the divisor.
- Related: L16-009.

### L16-011 A weighted MPS can have the right point-count norm without enumerating points as words
- Source: `2026-09-14T16-38-51.txt:225-227` (message).
- Raised by: codex prover
- Status at last mention: stated in a message; the distinction is preserved in the final's C9 column ("`W` is a weighted physical norm, `P` is a literal count state") but the general remark is not spelled out
- Content: Before choosing any tensors the prover flagged two constraints the drafts had to respect. First: a *weighted* MPS can reproduce a curve's point counts as its Ramond norm while its words are not in bijection with the points — the counts come out right but the state is not a literal enumeration. Second: a simple Perron eigenvalue does not by itself give a trace-preserving normalisation on the whole bond; TP is an extra equation on the letters, not a consequence of ergodicity.
- Lead: for any "the MPS counts the points of X" claim in the notebook, state explicitly which of the two it is (P or W in the final's table). The physical reading — correlation lengths, entanglement spectrum, what the odd sector *is* — only makes sense for the literal-count (P) version.
- Related: L16-013.

### L16-012 Horner letters give an open-chain character-weighted MPS: amplitude sum vs squared norm are different objects
- Source: `2026-09-14T16-38-51.txt:250-252` (message).
- Raised by: codex prover
- Status at last mention: stated in a message; the final reports both quantities but does not put the warning this way
- Content: For the tiny Dirichlet L-functions over `F_2[x]/(x^3+x+1)` and `F_3[x]/(x^2+1)`, the Horner transfer `f -> x f + c mod M` on the bond `F_q[x]/M` with letters `c in F_q` naturally produces an **open-chain, character-weighted MPS**, not a closed ring. Summing its amplitudes gives the L-polynomial; taking the squared norm of the same state gives a different quantity altogether. So the character amplitudes are not positive ring norms.
- Lead: whenever a tiny L-function is realised this way, say which of "sum of amplitudes" (side A, open chain, monic polynomials) and "squared Ramond norm" (side B, Frobenius orbits) is being asserted. The two presentations are related but the relation is not "same object seen twice" — that relation is the thing to write down.
- Related: L16-011.

### L16-013 A SymPy simplification failure forced a change of verification strategy
- Source: `2026-09-14T16-38-51.txt:278-280` (message).
- Raised by: codex prover
- Status at last mention: method note, stated in a message only
- Content: The first full run of the 13 example scripts had exactly one failing check: SymPy would not simplify a square root arising in a sampled-channel expression under the assumption `t > 0`. Rather than fight the CAS, the prover replaced that check by **direct Kraus completeness checks** (`sum_a R_a^dagger R_a + Q + Q^dagger = 0` and the nilpotency of the fermionic jump).
- Lead: for cMPS checks, verify the defining Kraus/Lindblad identities symbolically and evaluate the norm numerically, rather than asking a CAS to simplify a symbolic time-dependent norm. Recorded because the same trap will recur in every continuous-length example.
- Related: -

### L16-014 A graded divisor records only even-minus-odd multiplicity, so it can hide modes that violate the band
- Source: `2026-09-15T08-37-49.txt:98-100` (message).
- Raised by: codex prover
- Status at last mention: stated in a message; the consequences appear as the D4 correction in the final but the general warning does not
- Content: Before touching D1-D14 the prover noted the structural weakness of the notebook's divisor `nu = m_0 - m_1`: it is a *difference*, so an even mode and an odd mode at the same point cancel. A pair of such modes sitting outside the Ramanujan band therefore leaves the zeta, and hence the divisor, untouched. This is precisely what makes D4 ("band iff circle sector by sector") false: even a *mixing* qubit channel can have matching even and odd modes outside the band that cancel from its zeta.
- Lead: any Ramanujan statement in the notebook must say whether it is about the divisor (cancelled) or about the retained spectrum (uncancelled), and the two should get different names. The same distinction is what later separates "divisor Ramanujan" from "operator unitarity" in the Selberg lane (L16-018).
- Related: L16-018, L16-019.

### L16-015 Why the graded Alon-Boppana lower bound fails: Hastings' argument needs nonnegative word traces
- Source: `2026-09-15T08-37-49.txt:123-125` (message).
- Raised by: codex prover
- Status at last mention: stated in a message (the refutation is in the final; this one-line *reason* is the useful part)
- Content: D5 proposed an odd-sector lower bound of Alon-Boppana type. It is false as written, and the message gives the mechanism in one sentence: Hastings' quantum Alon-Boppana proof counts closed words and relies on those word traces being **nonnegative**, whereas odd-sector traces (`Tr(Gamma E^n)` restricted to the off-diagonal blocks) can be negative. The whole counting argument therefore has no analogue sector by sector.
- Lead: if a graded Alon-Boppana bound is wanted, it must be proved for the *sum* `Tr E^n` (nonnegative) and only then split, or a genuinely different argument is needed. Recording the obstruction saves re-attempting the direct translation.
- Related: L16-014.

### L16-016 The LPS examples' printed genus and curve-denominator claims are wrong by a wide margin
- Source: `2026-09-15T08-37-49.txt:164-166` and `:188-190` (messages).
- Raised by: codex prover
- Status at last mention: corrected in final (ledger row on the D6 induced-PGL examples), but the numbers are only in the messages
- Content: `scripts/graded_ramanujan.py` passes all 79 of its checks, but those checks never test the *printed genus claims*. Reducing the first LPS example gives a zeta numerator of **degree 4, not 36**; the second LPS example has **uncancelled poles on the critical circle**, so its reduced zeta has no curve-shaped denominator either. Two independent reasons why "Weil-LPS channel = curve" should not be asserted.
- Lead: add the genus/degree assertions to the script's check list so they cannot drift again, and state the LPS examples as "period-two graded expanders" with net multiplicities subtracted, not as curves.
- Related: L16-017.

### L16-017 A primitive unitary channel can have an integral Weil numerator that no curve can have (-2 rational points)
- Source: `2026-09-15T08-37-49.txt:212-214` (message).
- Raised by: codex prover
- Status at last mention: stated in a message; the correction is in the final, the striking witness is in the message
- Content: A verified counterexample to the hope that "integral Weil numerator + critical circle = curve L-polynomial": a primitive unitary channel whose numerator is an integer polynomial with all roots on the circle, but for which the hypothetical curve would have `-2` rational points over the base field. Integrality and the circle condition are jointly insufficient; positivity of the point counts is an independent constraint.
- Lead: add "the implied point counts `N_n` are nonnegative integers" as an explicit condition (it is essentially the C2 "genuine gas" condition of the zeta-conditions brief) whenever a channel is being proposed as a curve. Cheap to check, and it kills candidates fast.
- Related: L16-016, L16-011.

### L16-018 Temperedness threshold `1/(2d)` vs `1/2`: two different walk normalisations were being conflated
- Source: `2026-09-15T08-37-49.txt:164-166` (message).
- Raised by: codex prover
- Status at last mention: stated in a message; the final states the corrected rate but not the diagnosis
- Content: The displayed Lie-group (continuum Harrow) walk has a tempered threshold of `1/(2d)`, while the notebook's shard 09b quotes `1/2`. The discrepancy is not an error in either: `1/2` belongs to the **faster, two-jump normalisation** used in 09b. The same object, two time normalisations, two thresholds.
- Lead: fix one normalisation per shard and state it at the top; every "gap 1/2" claim in the continuum should carry the jump convention. Otherwise the Fell-absorption/temperedness argument appears to give contradictory gaps.
- Related: L16-014.

### L16-019 The reflection heat supertrace is not an ordinary trace, and the weight-1 limit needs a covering group
- Source: `2026-09-15T08-37-49.txt:188-190` (message).
- Raised by: codex prover
- Status at last mention: stated in a message
- Content: Two obstructions in the continuous (D11/D12) part, both structural. First: the reflection heat supertrace that the notebook wants to use is **not an ordinary trace** — it needs its own definition (regularisation, weight, or flat trace) before any cancellation argument runs. Second: taking the weight down to `1` in the discrete-series decompositions `D_k^+ (x) D_k^{+/-}` requires either a **covering group** of `PSL_2(R)` or a **projective representation**; the naive limit does not exist inside `PSL_2(R)`.
- Lead: if the weight-1 discrete series is wanted (it is the one nearest the Maass spectrum), work on the metaplectic-type cover from the start; and supply a definition of the reflection supertrace analogous to def:distributional-trace of shard 02c before using it.
- Related: L16-018.

### L16-020 Alternative period-two graded Ramanujan example cut: grading `P = X` with odd peripheral eigenoperator `Z`
- Source: `2026-09-15T08-37-49.txt:192` and `:230` (draft `finite_checks.py` block using `F = doubled([X,Y])/2`, `zvec = (1,0,0,-1)`, "period-two channel with grading P=X has an odd peripheral eigenoperator Z"); replaced by the `P = Z` / letters `{P, Y}` / `xvec = (0,1,1,0)` version now at `notes/ramanujan-graded/finite/finite_checks.py:161`. The draft phrase "for a bipartite one it gives a period-two version, allowing the even eigenvalue `-1`" (`:192`) is also absent from the final.
- Raised by: codex prover
- Status at last mention: cut from final (replaced by an equivalent example with a different grading)
- Content: Two inequivalent qubit witnesses for the period-two phenomenon were written. The cut one grades the bond by `P = X` (so the Pauli `Z` is the odd peripheral eigenoperator of the channel built from letters `X, Y`); the kept one grades by `P = Z` with `X` odd. They are unitarily equivalent as abstract examples but not as *notebook* examples, because the notebook's grading is always `P = diag(+1,-1) = Z`. The cut draft also contained the cleaner statement of the bipartite case: a bipartite Ramanujan Cayley graph gives a period-two graded channel in which the even eigenvalue `-1` is *allowed* rather than excluded.
- Lead: keep the `P = X` version as a reminder that the grading is a choice: the same channel is a mixing graded expander or a period-two one depending on which Pauli is called the parity. Any theorem that quantifies over gradings should say so.
- Related: L16-014.

### L16-021 The transverse supertrace gives the Ruelle zeta, whose two retained bands cannot satisfy a single-line Ramanujan condition
- Source: `2026-09-16T14-21-08.txt:199-201` (message), stated before the corresponding proof block was drafted.
- Raised by: codex prover
- Status at last mention: stated in a message, then proved in the final
- Content: The obvious construction — take the full transverse exterior algebra and its flat supertrace — produces the direct-product Ruelle zeta `zeta_R(s) = Z_S(s)/Z_S(s+1)`. Its retained zeros and poles occupy **two bands shifted by one unit**, so reflection about the midpoint sends one band to a place where no band exists. The notebook's single-line Ramanujan condition is therefore unsatisfiable for `zeta_R`, no matter what the surface is. The fix is the **two-term transverse complex** (even generator `A = -X`, odd generator `A + 1`), which gives `Z_S` directly.
- Lead: the general moral is that a graded zeta with two shifted bands can never have a single critical line; before asking for RH, count the bands. This is a cheap structural test applicable to every candidate in the notebook.
- Related: L16-014, L16-022.

### L16-022 The proposed pullback form is degenerate: both first-band partners push forward to the same Laplace eigenfunction
- Source: `2026-09-16T14-21-08.txt:199-201` (message).
- Raised by: orchestrator draft (the form), diagnosed by the prover
- Status at last mention: corrected in final (the fix is "orthogonal sum of branchwise pullbacks")
- Content: The draft's positive form was to pull back the `L^2` inner product of the surface through the pushforward `pi_*`. This is degenerate on paired first-band states, for a simple reason: the two resonances `lambda_+ = s_+ - 1` and `lambda_- = s_- - 1` attached to one Laplace eigenvalue `sigma` push forward to *the same* eigenfunction, so their difference is in the kernel. A positive form needs **separate, orthogonal copies for the two branches** — i.e. pull back branchwise and take the orthogonal sum, not the sum of the pushforwards.
- Lead: the same degeneracy appears in the finite (graph / Hashimoto) case, where the untagged metric `<Ru, Rv>` has as kernel exactly the differences of partner lifts. Any future "positive form from a pushforward" construction should be written branchwise from the start.
- Related: L16-021, L16-023.

### L16-023 The critical-band metric written down explicitly: `[[I, A/2],[A/2, qI]]`
- Source: `2026-09-16T14-21-08.txt:245-247` (message).
- Raised by: codex prover
- Status at last mention: stated in a message, then proved in the final (D7)
- Content: For the companion operator `C_a` of the quadratic `mu^2 - a mu + q` (the Hashimoto / non-backtracking block attached to an adjacency eigenvalue `a`), the metric `G = [[I, A/2],[A/2, qI]]` makes `C` unitary, and `G` is positive **exactly inside the open Ramanujan band** `|a| < 2 sqrt q`. At the endpoint `a = 2 eps sqrt q` the matrix `C_a - eps sqrt q I` is a nonzero square-zero matrix, i.e. a size-two Jordan block, and a positive-metric unitary is diagonalisable — so the endpoint is impossible on the whole block. This is a constructive "strict band iff positive form" statement.
- Lead: the metric is explicit and finite-dimensional, so it can be assembled for any graded Hashimoto operator in the notebook and its positivity tested numerically as a *certificate* of the Ramanujan property, instead of computing eigenvalues. Consequence: a positivity certificate is the quantum analogue of a Weil positivity statement in this setting.
- Related: L16-022, L16-024.

### L16-024 Explicit endpoint counterexamples: `K_3 (box) Q_3` and a ten-letter Pauli channel have verified Jordan blocks
- Source: `2026-09-16T14-21-08.txt:245-247` (message).
- Raised by: codex prover
- Status at last mention: stated in a message; the phenomenon is in the final, the two named witnesses are only here and in `finite/check_letters.out`
- Content: Two concrete Ramanujan objects whose Hashimoto operators fail the positive-form claim *at the endpoint*: the Cartesian product `K_3 (box) Q_3` (a graph) and a ten-letter Pauli channel (a quantum one). Both are Ramanujan in the closed sense, both have a verified size-two Jordan block at the band edge, and therefore neither admits a positive form making the full algebraic band unitary. Together they show the endpoint gap is not an artefact of one category.
- Lead: keep both as the standing counterexamples whenever "Ramanujan implies unitarisable" is proposed; and note that both are *products/tensor constructions*, which suggests endpoint degeneracy is generic for products of Ramanujan objects.
- Related: L16-023.

### L16-025 The `1/4` bound for the full modular group is a theorem, not an open conjecture
- Source: `2026-09-16T14-21-08.txt:266-268` (message); final ledger corrects the draft's claim.
- Raised by: orchestrator draft (as an open conjecture), corrected by the prover
- Status at last mention: dead (false statement, corrected in final)
- Content: The Selberg draft asserted that `lambda_1 >= 1/4` for the modular surface is open. It is not: the property is known for the **full modular group** `PSL_2(Z)`; what is open is the Selberg eigenvalue conjecture for general **congruence subgroups**. The prover also verified that the supplied Friedman-Jorgenson-Smajlovic source already contains the cusp-divisor theorem the draft wanted to prove.
- Lead: when the notebook cites "Selberg 1/4" as a hypothesis (H-COERC), it should say for which group; for the modular surface itself the hypothesis is discharged, and the genuinely open direction is congruence covers.
- Related: L16-026.

### L16-026 Positivity of truncated Eisenstein norms does not imply RH, and the draft's decay rate was wrong
- Source: `2026-09-16T14-21-08.txt:288` (draft executive-summary bullet), reworded into `notes/selberg-letters/astra-proofs.md:10`.
- Raised by: orchestrator draft (D6), corrected by the prover
- Status at last mention: corrected in final; the draft bullet's phrasing (kept here) is the sharpest one-line version
- Content: In the modular (noncompact) case the first-band states at a scattering pole are given by the **leading Laurent coefficient** of the Eisenstein series, not by a value `E(z, s_0)`; that coefficient has a nonzero `y^{1-s_0}` constant term and is not in `L^2`. Truncated (Maass-Selberg) norms are positive throughout `0 < Re s_0 < 1/2`, not only at the critical line, and their growth in the truncation height `Y` is exactly the missing Haar integrability. So truncation positivity is not the RH coercivity. The draft's proposed decay rate in D6(c) is also wrong for flow resonances.
- Lead: the missing object is H-CUSP-BRIDGE (`astra-proofs.md:358`): a noncompact flow-resolvent realisation with finite-rank resonant data at `s_0 - 1`, a multiplicity-preserving first-band pushforward to Eisenstein Laurent data, and a compatible positive pairing. Nothing in the compact DFG material supplies it. This is the single named gap between the compact success and the modular case.
- Related: L16-025, L16-022.

## Small but possibly consequential

1. **`F(s)` is independent of the shell cutoff** (L16-005) — the finite model's negative result cannot be blamed on truncation, which makes it much stronger than a numerical scan.
2. **Even zero modes are free** (L16-010) — they change the bond and the fixed-point structure without moving any divisor point, the cheapest way to decouple C6 from C4/C5.
3. **Count the bands before asking for RH** (L16-021) — a graded zeta with two shifted bands can never have a single critical line; a one-line structural test for any candidate.
4. **The divisor cancels** (L16-014) — every Ramanujan claim must say whether it is about the (cancelled) divisor or the (uncancelled) retained spectrum; this is the root of the D4 failure and of the Selberg endpoint subtlety.
5. **Nonnegative implied point counts** (L16-017) — adding "the `N_n` are nonnegative integers" to the curve checklist immediately kills candidates that integrality plus the circle condition let through.
6. **The Gram condition number is a test, not evidence** (L16-002) — only unbounded growth refutes the Riesz property, so the recorded 10 -> 700 decides nothing and the computation should be extended.
7. **Pull back branchwise** (L16-022) — the same degeneracy (partners with a common image) breaks the naive positive form in both the continuum and the finite graph case.
8. **The phase-only negatives of 09-14 are not negatives about the guess** (L16-003) — no archimedean factor was ever built, so the completion that would remove the spurious pole at `s = -2` was never in the model.

## Dead routes recorded

Orchestrator statements shown false in these five rollouts. Row format: where the statement was
drafted, and what replaced it. (The full verdict tables live in the four final reports; listed here
are the ones whose falsification is the point, with the transcript line where the prover announced
it.)

| Drafted statement | Where drafted | Announced false at | Correction |
| --- | --- | --- | --- |
| S3: the prime Lindbladian acts as a *scalar* on vacuum/Gauss and Gauss/Gauss coherences, with real part `-sum_p lambda_p (1 - Re chi chi'(p))`. | brief A, `14-56-39.txt:108-117` | `14-56-39.txt:182`, `14-56-42.txt:163` | No invariant scalar. Explicit mod-3, `p = 2` counterexample; even the one-dimensional compression carries an extra factor `1/p`, and the orthogonal residual is nonzero *before* any truncation. |
| S4: the critical Bost-Connes state is the **pure** vector state of `e_0` on `C(Zhat)`. | brief A, `14-56-39.txt:118-121` | `14-56-39.txt:197` | Haar is represented by `e_0` but is not pure on `C(Zhat)`: `omega(1_{2Zhat}) = 1/2 != 1/4`. Weak-* convergence to Haar is proved instead. |
| S5: the vacuum-to-shell overlaps of the prime-jump dynamics have `1/zeta(s)` as a factor (`c_b(1) = mu(b)` read as an overlap). | brief A, `14-56-39.txt:122-130` | `14-56-39.txt:197` | Overlaps are `<b|V_n|1> = sqrt(phi(b)/n) [b | n] >= 0`; their Dirichlet series is `sqrt(phi(b)) b^{-(s+1/2)} zeta(s+1/2)` — zeta in the **numerator**. Reciprocal zeta comes only from the inverse of a *separate* multiset sum `A(w)^{-1} = prod_p (1 - p^{-w} V_p)`. |
| S5: commuting prime jumps, the shell "stay" term, or the parity closure restore one-copy-per-multiset Euler weights. | brief A, `14-56-39.txt:122-130` | `14-56-39.txt:197` | `pq` occurs twice as an ordered two-letter word; the word multiplicity is `Omega(n)!/prod_p k_p!`. Only the multiset product `prod_p (1 - z_p V_p)^{-1}` or an occupation-space trace changes it. |
| S6: closing the ring with a parity insertion performs the quotient by `Q^x`. | brief A, `14-56-39.txt:131-136` | `14-56-39.txt:218` | Two-dimensional counterexample: `W_q = diag(1, e^{i theta v_p(q)})`, `Pi = diag(1,-1)` commute, yet the parity-closed norm of the word `W_p` is `|1 - e^{i theta}|^2` while that of the identity is `0`. Parity closure changes a boundary functional; it imposes no quotient. |
| S6: Connes 1999 identifies this ring norm with an unconditional periodic-orbit trace. | brief A, `14-56-39.txt:131-136` | `14-56-39.txt:187` (source fetched), `:218` | The paper proves a *local cutoff* trace formula (§V Thm 3) and a finite-set-of-places formula (§VII Thm 4); it supplies no unconditional global heat trace. Verified against arXiv math/9811068 rather than quoted from memory. |
| S7: a spectral line conversely supplies anti-Hermiticity. | brief A, `14-56-39.txt:137-142` | `14-56-39.txt:218` | Needs diagonalisability and permits a changed positive metric; explicit Jordan counterexample. H-INV, H-SA (skew-**adjointness**, not formal skew-symmetry) are the real hypotheses. |
| S8: reverse jumps at rate `lambda_p p^{-beta}` restore detailed balance and Gibbs shell weights are stationary. | brief A, `14-56-39.txt:143-155`; brief B N6, `14-56-42.txt:124-126` | `14-56-42.txt:163`, `:241` | The rate orientation is backwards: the required ratio is `d_p/u_p = p^beta`. After reversing it, the classical populations are stationary but the phase jumps still create shell coherences; only resolved edge jumps fix it (L16-006). |
| Overall guess: `sum_p (1/p) D_{V_p (x) T_{log p}}` is an already defined normal Lindbladian, and a finite prime cutoff makes its ring supertrace an ordinary trace. | brief A, `14-56-39.txt:92-99` | `14-56-39.txt:182`, `:207` | The no-jump quadratic form diverges at rates `1/p`; and on the infinite doubled bond `e^{t L_F}` is bounded with bounded inverse, hence non-compact and not trace class, so `Tr[Gamma_b e^{t L_F}]` is not an ordinary trace. |
| D1 (zeta conditions): the sub-system rule makes the odd sector a sub-MPS with `a_d = a_d^+ - a_d^- >= 0` automatically. | zeta brief, `16-38-51.txt:144-147` | `16-38-51.txt:225` | A weighted MPS can have the right counts without enumerating points as words; and a simple Perron root does not give a TP normalisation on the whole bond. Both are extra conditions (L16-011). |
| D4 (zeta conditions): letters closed under `B -> B^{-1}` give the functional equation for the ring zeta. | zeta brief, `16-38-51.txt:157-159` | `16-38-51.txt:233` | True for the **non-backtracking / Hashimoto** transfer after removing the Bass factors, false for a raw `sum_s A_s (x) conj A_s`. Exact counterexample `B = diag(1,2)`: even spectrum `{2, 17/4}` fixes `q = 17/2`, odd spectrum `{5/2, 5/2}` fails it. |
| D5 (zeta conditions): `L(u, sgn) = ((1 - mu)/(1 - m^2 u))^{1/2}` for the `Z/2` swap on the pair shift. | zeta brief, `16-38-51.txt:160-164` (the brief itself flags it as "probably wrong") | `16-38-51.txt:250` | The pair shift is not a `Z/2` cover. The genuine tiny example is the two-loop rose with voltages `0,0,1,1`, whose sign-Hashimoto factor is a real Artin L-function. |
| D4 (graded Ramanujan): band iff circle, sector by sector. | `notes/ramanujan-graded/definition.md` | `15T08-37-49.txt:123` | False: a mixing qubit channel can have matching even and odd modes outside the band that cancel from the zeta (L16-014). |
| D5 (graded Ramanujan): an odd-sector Alon-Boppana lower bound. | `notes/ramanujan-graded/definition.md` | `15T08-37-49.txt:123` | REFUTED. Hastings' argument needs nonnegative word traces; odd-sector traces can be negative (L16-015). |
| The Weil-LPS examples are curves (printed genus 36 etc.). | notebook shard / `scripts/graded_ramanujan.py` | `15T08-37-49.txt:164`, `:188` | First example reduces to numerator degree **4**; second has uncancelled poles on the critical circle. Call them period-two graded expanders, not curves (L16-016). |
| D3/D7 (Selberg): the pullback of the `L^2` form through the pushforward is positive on the first band. | `notes/selberg-letters/draft.md` | `16T14-21-08.txt:199` | Degenerate: the two branch partners have the same image. Use the orthogonal sum of branchwise pullbacks (L16-022). |
| D2 (Selberg): the full transverse (Ruelle) supertrace satisfies the notebook's single-line Ramanujan condition. | `notes/selberg-letters/draft.md` | `16T14-21-08.txt:199` | Its two retained bands are shifted by one unit; reflection maps one onto a nonexistent band. The two-term complex giving `Z_S` is the right object (L16-021). |
| D3/D7 (Selberg): Ramanujan (closed band) implies the resonant operator is unitarisable. | `notes/selberg-letters/draft.md` | `16T14-21-08.txt:221`, `:245` | Only the **strict** band. At `Delta = 1/4` the Selberg zero has twice the Laplace multiplicity, forcing a Jordan block; finite witnesses `K_3 (box) Q_3` and a ten-letter Pauli channel (L16-023, L16-024). |
| D6 (Selberg): `lambda_1 >= 1/4` for the modular surface is an open conjecture; truncated Eisenstein positivity would give RH; the stated D6(c) rate. | `notes/selberg-letters/draft.md` | `16T14-21-08.txt:266`, `:288` | Known for the full modular group (open only for congruence covers); truncated positivity holds throughout `0 < Re s_0 < 1/2` and is not RH coercivity; the rate is wrong for flow resonances (L16-025, L16-026). |
| D8 (Selberg): K-type parity is the Hodge form degree and grades the geodesic flow. | `notes/selberg-letters/draft.md` | `16T14-21-08.txt:288` | K-type parity makes `X` odd, so it does not commute with the flow and is not a grading for it; and Hodge degree uses two weight-zero copies plus weights `+/-2`, a different vector space. |
