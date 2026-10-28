<!-- ROLE: round status. Written 2026-10-28 (tidy session). Update when a lane, review or correction lands. -->
# Status — astra round 2026-10-25

Nine `codex:gpt-6-astra` lanes launched 06:06–06:36 UTC+1 on 2026-10-25 through `scripts/astra_lane.sh`, all exited 0 by 07:02 (19–55 min, no resumes): five REFUTE reviews of the whole 2026-10-23 round and four new conjectures (J2' for K3,3; H-half; irreps; short-row H-MS). Binding rules: `brief.md` (incorporates the 2026-10-23 rules and adds the REFUTE protocol with `VERDICT <alias>: ...` lines). All reviews are codex reviewing codex. **Nothing from this round is registered (`NOT REGISTERED` in db/claims.tsv); the gate is untouched.**

## Lanes
Review mapping verified from the review briefs: review-tower to `2026-10-23/tower`; review-jacobian to `jacobian`; review-gauge to `haar` (H) + `krein` (K); review-average-canonical to `average` (A) + `canonical` (C); review-qrh to `qrh-digest` (Q1) + `qrh-transpose` (Q2). The new-conjecture lanes have no verdict lines (nobody has reviewed them).

| lane | author | what it proved / refuted (one line, with the key named results) | lane state | review state | verdicts V/M/I/U | reviewed by |
|---|---|---|---|---|---|---|
| `review-tower` | codex:gpt-6-astra | reviews `2026-10-23/tower`: all 13 items VALID; PARI rerun done (80/80 pairing values PARI = FLINT); new D=-84 and D=-32 tests; lane T's same-order F_41 pair has no separating k | DONE | SAME-FAMILY REVIEWED (it is itself a review; its own verdicts are unreviewed) | 13/0/0/0 | n/a (it reviews the tower lane); itself UNREVIEWED |
| `review-jacobian` | codex:gpt-6-astra | reviews `jacobian`: 16 VALID; 13 outputs byte-identical on rerun; independent K4 trigonal counts and PARI K5 L-polynomials; the N2 shortcut for excluding a hyperelliptic K4 is invalid, the 264-class census is what proves it | DONE | SAME-FAMILY REVIEWED (as above) | 16/0/0/0 | n/a; itself UNREVIEWED |
| `review-gauge` | codex:gpt-6-astra | reviews `haar` + `krein`: 31 VALID (18 candidate rows + 13 body claims); K4 SU(2) average x^8-12x^6+42x^4-32x^2+12 by two routes; both `gauge-groups.md` paragraphs AGREE-WITH-CHANGE | DONE | SAME-FAMILY REVIEWED (as above) | 31/0/0/0 | n/a; itself UNREVIEWED |
| `review-average-canonical` | codex:gpt-6-astra | reviews `average` + `canonical`: 26 VALID, 1 MINOR (certificate sentence must say H-half for odd cells, band certificates for both parities), 1 UNVERIFIED (the open all-genus row); graph Schur moment is a trace of M/sqrt(q) | DONE | SAME-FAMILY REVIEWED (as above) | 26/1/0/1 | n/a; itself UNREVIEWED |
| `review-qrh` | codex:gpt-6-astra | reviews `qrh-digest` + `qrh-transpose`: 32 VALID, 3 MINOR (Q1 7/8 synopsis P_x=(2-8x/9)(1-x); stray comma; Cureton–Thorner numbering), 5 UNVERIFIED (the lanes' own OPEN proposals) | DONE | SAME-FAMILY REVIEWED (as above) | 32/3/0/5 | n/a; itself UNREVIEWED |
| `census` | codex:gpt-6-astra | THEOREM via the complete Huang–Kedlaya–Lau genus-6 census (38,327 classes): neither Ramanujan K3,3 flux class is a Jacobian class over F_2, so J2' is REFUTED; Petersen mask 22 (genus-10 trigonal y^3=x^12+x^9+x^6+x^3+1) and prism mask 6 ARE Jacobian classes; cube 3, 5 and Petersen 6, 10 OPEN | PARTIAL | UNREVIEWED | n/a (no verdict lines) | none |
| `hhalf` | codex:gpt-6-astra | PROVED RH on average for the hyperelliptic ensemble over F_q(t), every odd prime power q and every genus g <= 7 (both conductor parities) by symbolic sign certificates; exact certificates to g=25 at q=3; fixed-genus large-q theorem; whole-cubic averages on the circle in five cells; all-genus A1 / H-half OPEN | PARTIAL | UNREVIEWED | n/a | none |
| `irreps` | codex:gpt-6-astra | THEOREM: the Haar average equals the HPS d-matching polynomial on all finite simple graphs iff HPS's P1, iff on the triangle alone; brief's classification REFUTED in every form; SU(d) average formula; new OPEN `conj:conformal-sp4-average-real-rooted` (U(1)·USp(4), verified on 971 connected cyclic graphs <= 7 vertices + cube + Petersen) | DONE | UNREVIEWED | n/a | none |
| `shortrow` | codex:gpt-6-astra | PROVED exact short-row Poisson formula for the sextic Mobius family over F_q(t); S(13,5,5) = 1 528 527 342 888 by two routes, 100 exact cells; Weil implies H-MS (labelled comparison); a Weil-free proof of H-MS OPEN; two brief shortcuts REFUTED | PARTIAL | UNREVIEWED | n/a | none |

Recount from the verdict lines: 13, 16, 31, 28 (26/1/0/1) and 40 (32/3/0/5) lines; all agree with HANDOFF 2026-10-25. Minor discrepancy: the worklog `docs/worklog/2026-10-25.md` is headed "Six astra lanes: three REFUTE reviews ... three new conjectures" but its body, HANDOFF and this directory have nine lanes (five reviews, four new). The "0 INVALID anywhere" statement of HANDOFF holds for the reviews.

## Unfinished in this round
- HELD: cross-family (Claude) REFUTE review of the four new lanes (`census`, `hhalf`, `irreps`, `shortrow`) — census theorem and witnesses; genus <= 7 certificates; the P1 converse; the short-row formula; needs Claude usage; no file exists.
- HELD: cross-family review of the 2026-10-23 PROVED items (the five review lanes above are same-family only); see `2026-10-23/STATUS.md`.
- PARTIAL: application of the endorsed record corrections to the record pages (some applied 2026-10-28 as annotations; unapplied ones in HANDOFF).
- HELD: registration of reviewed rows in db/claims.tsv (needs the cross-family reviews and TJO's decision).
- OPEN: `conj:conformal-sp4-average-real-rooted` (prove interlacing, or search graphs with >= 8 vertices).
- OPEN: H-half / A1 uniform in g (control the adjacent nonsquare corrections at m proportional to g; compute m = 13 and genera 26–27 at q = 3); `conj:whole-squarefree-cubic-average`.
- OPEN: cube masks 3, 5 and Petersen masks 6, 10 as Jacobian classes (degree-2 covers of genus-4 bases, tetragonal models); the integral polarized lattice of the K4 trigonal and Petersen-22 Jacobians versus the graph's Omega.
- OPEN: a Weil-free proof of H-MS (function-field analogues of source Prop. 6.2 / 5.4: the uniform theta/transfer estimate).
- Not tracked in git: the 4.6 GB HKL genus-6 clone `census/sources/hkl-genus-6/` and compiled search binaries (gitignored; clone restored from the old-machine backup); the `.cpp` sources are committed.

## Corrections this round asks of the record
Endorsed in the review lanes' closing sections, in addition to the 2026-10-23 list (see `2026-10-23/STATUS.md`). Applied 2026-10-28 as annotations where endorsed — see the pages; unapplied ones listed in HANDOFF.
- `graph-ihara.md` (§8/§9): the graph Schur moment is a trace of M/sqrt(q) (corrected Hashimoto trace), not of A/sqrt(q); both roots of each trivial mode removed.
- Tutorial `notes/adelic-gkp/tutorial/page.html` §6d: the unconditional endpoint sentence needs the parabolic-endpoint qualification.
- `tower-pairing.md` / lane U: Tate "iff N | q^k - 1" needs exp(G_k[N]); delete the CM "not its conjugate".
- `ff-dirichlet.md` / lane A text: the finite-certificate sentence must say H-half for odd cells and band certificates for both parities.
- Lane Q1 text: the 7/8 synopsis must read P_x = (2-8x/9)(1-x); remove a stray comma in the cube exponent; the Cureton–Thorner theorem numbering (31/32) lacks local provenance.
- `gauge-groups.md`: wording from review-gauge (SU(1,1) uses C^2 = +1 plus a separate Pfaffian doubling, not SU(2)'s J^2 = -1).
- Brief-error ledger for future briefs (not record pages): theta graph with three parallel edges is 3-regular; both K3,3 masks are nonordinary; averaged traces are coefficients of the averaged logarithm; HPS standard S_d has dimension d-1; the simplified short-row diagonal holds only for h >= D-1; lane T's same-order F_41 pair has no separating k.

## Files
- Deliverables per lane dir: `astra-proofs.md`, `checks/` (scripts and printed `output_*.txt`), `astra-brief.md`. Round-level: `brief.md`. Review lanes: the VERDICT lines and the closing sections of `astra-proofs.md` are the deliverable.
- Run artefacts (gitignored, restored from the old-machine backup on 2026-10-28, kept locally only): `astra.stdout`, `lane.log`, `session.id`, `progress.txt`, `astra-last.md`, `launcher.out`. Also gitignored: `census/sources/` (HKL clone) and compiled search binaries.
