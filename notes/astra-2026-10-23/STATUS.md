<!-- ROLE: round status. Written 2026-10-28 (tidy session). Update when a lane, review or correction lands. -->
# Status — astra round 2026-10-23

Eight `codex:gpt-6-astra` (xhigh) lanes, launched 12:22 UTC on 2026-10-23 through `scripts/astra_lane.sh`: six ambitious conjectures from the record (K, H, C, J, A, T) and two digests of the quasi-Riemann hypothesis (Q1, Q2). All eight exited 0 between 12:46 and 13:35 UTC. Binding rules: `brief.md`. The lanes' own statuses (PROVED, REFUTED, OPEN, ...) are in each `astra-proofs.md`; they carry no verdict lines because a lane does not review itself. The round was REFUTE-reviewed by the 2026-10-25 round (same family, codex reviewing codex). **Nothing from this round is registered (`NOT REGISTERED` in db/claims.tsv); the gate is untouched.**

## Lanes
Review lanes live in `notes/astra-2026-10-25/` (mapping checked against the review briefs). Where one review lane covers two lanes the V/M/I/U count is for the pair together.

| lane | author | what it proved / refuted (one line, with the key named results) | lane state | review state | verdicts V/M/I/U | reviewed by |
|---|---|---|---|---|---|---|
| `krein` (K) | codex:gpt-6-astra | SU(1,1) Krein–Ramanujan rigidity REFUTED (nonelementary Ramanujan holonomy on the theta graph and K4); PROVED char poly is a square, balanced Krein inertia (kappa = half the real in-band multiplicity), exact K4 collision at arcosh(79/54) | DONE | SAME-FAMILY REVIEWED | 31/0/0/0 (with `haar`) | `2026-10-25/review-gauge` |
| `haar` (H) | codex:gpt-6-astra | "RH on average for every compact gauge group" REFUTED (SU(2) on the triangle: (x^3-3x)^2+1); PROVED every quaternionic irrep fails on any graph with a cycle, U(d) average = HPS d-matching polynomial, Kesten–McKay root limit | DONE | SAME-FAMILY REVIEWED | 31/0/0/0 (with `krein`) | `2026-10-25/review-gauge` |
| `canonical` (C) | codex:gpt-6-astra | PROVED graph trace/Ihara identities and Toeplitz positivity iff Ramanujan, F_q(t) Schur criterion with completion (263,694 characters); REFUTED Schur coordinates as the ladder's "finite rank per mode" datum | DONE | SAME-FAMILY REVIEWED | 26/1/0/1 (with `average`) | `2026-10-25/review-average-canonical` |
| `jacobian` (J) | codex:gpt-6-astra | K4 Ramanujan class IS a trigonal genus-4 Jacobian over F_2; every K5 orbit a hyperelliptic genus-5 Jacobian over F_3; J1 (unit in Z[F,V]) and J2 (count positivity) REFUTED; cube, Petersen, K3,3 left OPEN (K3,3 later settled by `2026-10-25/census`) | PARTIAL | SAME-FAMILY REVIEWED | 16/0/0/0 | `2026-10-25/review-jacobian` |
| `average` (A) | codex:gpt-6-astra | PROVED exact Euler-product formula for the hyperelliptic average over F_q(t), A1 for all odd q and g <= 3, reduction to an exact half-coefficient inequality (H-half); cubic isotypic average REFUTED (1+u); all-genus A1 OPEN | PARTIAL | SAME-FAMILY REVIEWED | 26/1/0/1 (with `canonical`) | `2026-10-25/review-average-canonical` |
| `tower` (T) | codex:gpt-6-astra | PROVED the torsion tower sees isogeny class + order (T1) and the strict tower exactly the genus (T2); lane-U q=7 pair is Q(sqrt(-6)), D=-24, a genus separation; blanket "tower blind to the class" REFUTED | DONE | SAME-FAMILY REVIEWED | 13/0/0/0 | `2026-10-25/review-tower` |
| `qrh-digest` (Q1) | codex:gpt-6-astra | exponent arithmetic of the quasi-RH proofs corrected (the fixed gap to 1/2 is the sparse amplifier; 6/7 even with an unrestricted mean square); Poisson = Fourier gate exactly; cubic theta as Z_3 qunaught and D-G REFUTED; large sieve = Gram positivity, not Weil positivity; three OPEN conjectures (Q1-THETA, Q1-EVAL, Q1-TRACE) | PARTIAL | SAME-FAMILY REVIEWED | 32/3/0/5 (with `qrh-transpose`) | `2026-10-25/review-qrh` |
| `qrh-transpose` (Q2) | codex:gpt-6-astra | amplifier over F_q(t) PROVED conditional on H-MS (theta = max(1/2+5a/12, 1-a/6), minimum 6/7); graph Littlewood equivalence and graph/surface amplifiers REFUTED; H-MS and C-SURF OPEN here (H-MS later attacked by `2026-10-25/shortrow`) | PARTIAL | SAME-FAMILY REVIEWED | 32/3/0/5 (with `qrh-digest`) | `2026-10-25/review-qrh` |

Recount against the verdict lines of the review files: 13 (tower), 16 (jacobian), 31 (gauge), 28 (average-canonical: 26/1/0/1), 40 (qrh: 32/3/0/5). All agree with HANDOFF 2026-10-25. The review of the qrh pair names the three MINOR items (Q1's 7/8 synopsis must read P_x = (2-8x/9)(1-x); a stray comma in `Q1-cube-inversion`; the Cureton–Thorner theorem numbering lacks local provenance) and the five UNVERIFIED items (the lanes' own OPEN proposals). Review state is SAME-FAMILY only: no Claude review of any lane of this round exists.

## Unfinished in this round
- HELD: cross-family (Claude) REFUTE review of the PROVED items of all eight lanes, starting with T1/T2, J, H + K (needs Claude usage); no file exists, none is fixed by a brief. Until it lands every result here is SAME-FAMILY REVIEWED and cannot be promoted or registered.
- PARTIAL: application of the record corrections listed below to the record pages (some applied 2026-10-28 as annotations; the rest are listed in HANDOFF).
- HELD: registration of the reviewed rows in db/claims.tsv (needs the cross-family review above and TJO's decision).
- OPEN: `conj:hyperelliptic-average-all-genus` (A1 / H-half for all q, g); partly attacked by `2026-10-25/hhalf` (g <= 7 proved), nothing blocks the rest.
- OPEN: J2' for cube masks 3, 5 and Petersen masks 6, 10 (K3,3 settled by `2026-10-25/census`), and whether the graph's integral polarized lattice equals a constructed Jacobian lattice.
- OPEN: `Q1-THETA`, `Q1-EVAL`, `Q1-TRACE` (qrh-digest) and `Q2-THETA-SECTORS`, `C-SURF` / `conj:surface-squarefree-local-limit` (qrh-transpose); each has a finite test stated in its lane's closing section.
- OPEN: the epsilon-uniform CM comparison of lane U with cypari2 (HANDOFF 2026-10-23 next step iii); not stated as done by any review.
- DONE: lane T's pending PARI rerun (done by `2026-10-25/review-tower`: 80/80 pairing values PARI = FLINT).

## Corrections this round asks of the record
All eight are endorsed (AGREE or AGREE-WITH-CHANGE, with wording) in the closing sections of the 2026-10-25 review files. Applied 2026-10-28 as annotations where endorsed — see the pages; unapplied ones listed in HANDOFF.
- HANDOFF 2026-10-06 finding (F): "the Weil pairing sees the class" becomes "the strict pairing tower sees the genus; class here because h = 2".
- `tower-pairing.md`, `overlap-data.md`: same genus-versus-class wording; `cm-lift.md` / `check_cm_tower.py` is the Q(sqrt(-7)) example, lane U's is Q(sqrt(-6)), D = -24.
- `gauge-groups.md`: replace the SU(1,1) and U(d)/SU(2) paragraphs (replacement text in lanes K and H; review wording in review-gauge).
- `graph-ihara.md` §8/§9: "Omega is the Casoratian, Q = 1/2 Omega (M - q M^{-1})".
- `data-ladder.md` §0: "the graph supplies an abelian-variety module; its isogeny class may or may not be a Jacobian class"; §2: the failed geometric/level dichotomy as a negative finding; §§2, 4: a metaplectic route to a strip is a different kind of statement from the ladder's positivity.
- `shard-draft/` row `prop:gkp-overlaps-see-order`: wording only.
- Added by the reviews (see 2026-10-25/STATUS.md): the graph Schur moment is a trace of M/sqrt(q), not A/sqrt(q) (`graph-ihara.md`); tutorial §6d's unconditional endpoint sentence needs the parabolic-endpoint qualification; lane U's Tate "iff N | q^k - 1" needs exp(G_k[N]); delete lane U's CM "not its conjugate".

## Files
- Deliverables per lane dir: `astra-proofs.md` (the proofs and closing sections), `checks/` (scripts with printed `output_*.txt`), `astra-brief.md` (the lane's task). Round-level: `brief.md` (binding rules). `qrh/sources/` holds the quasi-RH source PDFs (+ pdftotext; PDFs untracked, restored from backup) read by Q1/Q2; it is not a lane.
- Run artefacts (gitignored, restored from the old-machine backup on 2026-10-28, kept locally only): `astra.stdout`, `lane.log`, `session.id`, `progress.txt`, `astra-last.md`, `launcher.out`.
