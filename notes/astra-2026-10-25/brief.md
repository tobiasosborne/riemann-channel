# Brief: the 2026-10-25 astra round — three REFUTE reviews of the 2026-10-23 lanes, three new conjectures

Author of the brief: `claude:fable-5.1`, 2026-10-25. TJO: "the codex quota will be reset within 2 hours. Please exploit this to use
astra to explore and prove lots of ambitious directions. also use astras to review results. you may use up to 6 astras
concurrently." Lanes: `codex:gpt-6-astra` (xhigh), six in parallel, run detached through `scripts/astra_lane.sh notes/astra-2026-10-25/<lane>`.
Each lane has its own directory here with `astra-brief.md` (input), `astra-proofs.md` (the deliverable, written incrementally — for
the review lanes this file IS the review), `progress.txt` (one line per item, `DONE`/`PARTIAL`/`PENDING`) and `checks/`.

**Binding by reference.** The sections "Where the record stands", "Game rules", "Conventions" and "Output protocol" of
`notes/astra-2026-10-23/brief.md` apply verbatim to every lane of this round. Read them first. Additions for this round:

- **Time budget: about 60 minutes of wall clock.** Prioritise the items in the order the lane brief gives them; write each finished
  item to `astra-proofs.md` at once; if you must stop early, the closing sections ("Numerical checks for the blind lane", "What this
  changes in the notebook") are mandatory and are the completion signal. An honest PARTIAL with a printed certificate beats a
  rushed PROVED.
- **No network inside the sandbox.** PARI is pre-installed: use `/tmp/claude-1000/-home-tobias-Projects-riemann-channel/venv-astra/bin/python`
  (cypari2 with PARI 2.17, python-flint, plus the system numpy/sympy/mpmath/networkx via `--system-site-packages` is NOT enabled —
  if a script needs both PARI and numpy, run PARI in a subprocess with that interpreter and the rest with `python3`). Do not `pip install`.
- **Do not run git. Write only inside your lane directory.** The 2026-10-23 lane directories are read-only inputs (rerun their
  `checks/*.py` with `python3` and compare to their saved `checks/output_*.txt`; do not edit them).

| lane | directory | task, in one line | kind |
|---|---|---|---|
| RT | `review-tower/` | REFUTE review of lane T (`notes/astra-2026-10-23/tower/`): the order theorem T1, the strict-tower genus theorem T2, the q = 7 audit; plus the pending PARI rerun | review |
| RJ | `review-jacobian/` | REFUTE review of lane J (`.../jacobian/`): the trigonal genus-4 Jacobian class of K₄, the K₅ hyperelliptic census, the J1/J2 refutations, the resultant-one proposition | review |
| RG | `review-gauge/` | REFUTE review of lanes H (`.../haar/`) and K (`.../krein/`): exterior-kernel formula, Pfaffian sum-of-squares identity, quaternionic obstruction, root limit; SU(1,1) Pfaffian/anti-isometry, balanced inertia, K₄ collision ranks, unicyclic formulas | review |
| A2 | `hhalf/` | RH on average for the hyperelliptic ensemble over F_q(t) for every (q, g): prove or refute H-half / the monotone-coefficient conjecture; whole-curve cubic averages | theorem + exact enumeration |
| J2 | `census/` | Which Ramanujan Z₂ flux classes on cubic graphs over F₂ are Jacobian classes: K₃,₃ against the Huang–Kedlaya–Lau genus-6 census (local copy), cube masks 3 and 5, Petersen masks 6, 10, 22; the K₄ integral lattice | computation + classification |
| Q3 | `shortrow/` | The quasi-RH bottleneck over F_q(t): prove or refute the short-row mean square H-MS; the (q, D, h) = (13, 5, 5) cell; L-polynomials from Gauss sums and the functional equation | theorem + numerics |

## REFUTE review protocol (lanes RT, RJ, RG)

You are the adversary. The lane you review was written by a model of your own family; assume it is confidently wrong somewhere and
look for the place. For every candidate row in the reviewed lane's "What this changes in the notebook" table (and every PROVED or
REFUTED item in its body that the table omits), write one adjudication: restate the claim in your own words, check the proof
step by step (hidden hypotheses, convention mismatches — e.g. the record's step M = ((A, −q), (1, 0)) versus the lane's; the
raw/completed L distinction; `(f/D)` versus `(D/f)`; which object "Ramanujan" refers to), and **recompute independently**: rerun
the lane's scripts and compare with the saved outputs, then write your own script in your `checks/` that computes the same
number by a different route (different library, different formula, brute force where feasible). A verdict without a recomputation
or a derivation is UNVERIFIED, never VALID.

Verdicts: `VALID` (proof correct, numbers reproduced), `MINOR` (correct after a stated fix — give the fix), `INVALID` (give the
counterexample or the broken step, with the script that shows it), `UNVERIFIED` (say what would be needed). End the file with a
section `## Verdict lines` containing exactly one line per item in the form

    VERDICT <alias>: <VALID|MINOR|INVALID|UNVERIFIED> — <one clause>

with `<alias>` the candidate id of the reviewed lane (no spaces; e.g. `thm:ordinary-strict-tower-genus`), then the two mandatory
closing sections. Also adjudicate the lane's **proposed record corrections** (the sentences it wants changed on record pages):
`AGREE`, `AGREE-WITH-CHANGE` (give the wording) or `DISAGREE`. Do not edit any record page. Author line of the review:
`codex:gpt-6-astra` (reviewer); note that this is a same-family review and that the record's gate wants a second-family review too.
