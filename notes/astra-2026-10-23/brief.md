# Brief: the 2026-10-23 astra round — six conjectures from the record, two digests of the quasi-Riemann hypothesis

Author of the brief: `claude:fable-5.1`, 2026-10-23. TJO: "find 6 directions to pursue based on this whole repo, formulate 6
ambitious conjectures for these directions, and spawn a gpt 6 astra xhigh subagent for each one. i am curious what we can
discover"; then: "the quasi riemann hypothesis got recently proven. Spawn some astras just to digest that in view of our project".
Lanes: `codex:gpt-6-astra` (xhigh), eight in parallel, run detached through `scripts/astra_lane.sh notes/astra-2026-10-23/<lane>`;
each lane has its own directory here with `astra-brief.md` (input), `astra-proofs.md` (the deliverable, written incrementally),
`progress.txt` (one line per item, `DONE`/`PARTIAL`/`PENDING`) and `checks/`. REFUTE review afterwards; nothing is registered before it.

| lane | directory | conjecture, in one line | kind |
|---|---|---|---|
| K | `krein/` | Krein–Ramanujan rigidity: an SU(1,1) gauge field on a finite graph is Ramanujan (real, semisimple, in-band spectrum) iff its holonomy is bounded, i.e. iff it is a unitary gauge field in disguise | theorem + numerics |
| H | `haar/` | RH on average for every compact gauge group: the Haar average of the twisted characteristic polynomial is real-rooted in the band, and is an explicit trail polynomial | exact averages + proof |
| C | `canonical/` | Weil positivity is a Schur–Cohn test on every rung (graph, F_q(t), zeta window): the Casoratian is the Szegő transfer matrix, Schur parameters from counts/primes | theorems + numerics |
| J | `jacobian/` | Centeleghe–Stix: a Ramanujan Z_2 flux on a (p+1)-regular graph is an abelian variety over F_p; which of them are Jacobians of curves | computation + classification |
| A | `average/` | RH on average holds exactly over F_q(t) for the geometric (cover) ensembles and fails for the level ensembles: the hyperelliptic-ensemble average L-polynomial has all roots on the circle | theorem + exact enumeration |
| T | `tower/` | the torsion tower with its pairings sees exactly the endomorphism order and never the ideal class; audit of lanes F and U of 2026-10-06 | theorem + audit |
| Q1 | `qrh-digest/` | the quasi-RH proof (OpenAI 2026-09-30 / 10-05; Kintali; Liu; Cureton–Thorner) digested step by step and mapped onto this project's ladder | digest + conjectures |
| Q2 | `qrh-transpose/` | the quasi-RH mechanism transposed to F_q(t) and to graph fluxes: which exponent it gives where RH is a theorem; what it lacks relative to Weil | theorem + numerics |

## Where the record stands (read these first, in this order)

`HANDOFF.md` sessions 2026-10-22 and 2026-10-06 (top of file). `notes/adelic-gkp/data-ladder.md` ("The answer in one paragraph",
§0 the ladder, §2 the negative findings, §4 the data for zeta, §6 next). `notes/adelic-gkp/adelic-gkp.md` §16 (index of pages).
The method steer (binding): interpret the understood cases first (Ramanujan graphs, super/graded Ihara zetas, curves and
Dirichlet characters over F_q(t)), then match to zeta; never the reverse. TJO is not convinced by the "overlap of a squeezed
probe with the comb" reading of zeta; do not build on it. Each lane brief lists its own further reading.

Registered claims live in `db/claims.tsv` (id, kind, status, deps, shard, statement, proof, author, review, note); shards in
`report/sections/`. A lane does not register anything; it proposes rows in its closing section.

## Game rules (binding for every lane)

1. RH (or GRH, or RH for the object at hand) is not assumed anywhere in a computation that produces a result. Where RH is a
   theorem (graphs with the Ramanujan property checked numerically; curves and characters over F_q(t) by Weil), say so and use it
   only as a labelled theorem.
2. Zeros of zeta or of L-functions over number fields are used only in explicitly labelled comparison steps, never as input.
3. Every number that enters a form on the zeta rung comes from primes, the pole and the archimedean factor.
4. Exact arithmetic where possible (sympy, python-flint, fractions); elsewhere state precision and error control. Print every
   number you quote from a script; the script lives in your `checks/` and is re-runnable with `python3 checks/<name>.py`.

## Conventions

- Graph: Y finite, connected, (q+1)-regular unless stated; A adjacency, B Hashimoto (non-backtracking) operator on oriented edges,
  Ihara zeta ζ_Y(u) = det(1 − uB)^{-1} = (1 − u²)^{−(|E|−|V|)} det(1 − Au + qu²)^{-1}; the step is, in the record's convention, M = ((A, −q), (1, 0)) on labels (f, g) ∈ Z^{2n}, M^T Ω M = qΩ with
  Ω = ((0, 1), (−1, 0)) ⊗ 1_n, V = qM^{-1}, Weil form ½Ω(M − V) (`notes/adelic-gkp/lattice-tower.md` §5, `graph-ihara.md` §4, §6,
  tutorial Section 6 for the Casoratian). Ramanujan: every nontrivial eigenvalue of A in [−2√q, 2√q]. A flux / gauge field: a
  map from oriented edges to a group G with s(ē) = s(e)^{-1}; the twisted adjacency A_s acts on C^n ⊗ C^d through a unitary (or
  other) representation ρ; the Z_2 case is the signing of `graph-super.md`.
- Function field: F_q(t), q odd unless stated; Dirichlet character χ mod f (f monic); L(u, χ) = Σ_{D monic} χ(D) u^{deg D}, a
  polynomial of degree deg f − 1 for χ primitive non-trivial (deg f − 2 if χ is "even", i.e. trivial on F_q^×); RH for it is
  Weil's theorem: all roots have |u| = q^{−1/2}. Quadratic character χ_D(f) = (f/D) Jacobi symbol in F_q[x]. Page `ff-dirichlet.md`.
- Curves and abelian varieties over F_q: L-polynomial P(u) with P(u) = Π(1 − α_i u), |α_i| = √q (Weil), N_k = q^k + 1 − Σ α_i^k.
- Environment: python3 with numpy, scipy, mpmath, sympy, networkx, python-flint. No gp binary and no sudo; PARI is available as
  `python3 -m venv /tmp/claude-1000/-home-tobias-Projects-riemann-channel/venv-astra && . .../bin/activate && pip install cypari2`
  (wheels bundle PARI; use `precision=` in bits for lfunzeros). 12 cores, 30 GB. Do not install system packages. Do not run git.
- Sources: `refs/src/<arXiv id>/` holds 134 fetched TeX sources (`refs/manifest.sha256`); cite by file and line when you quote.
  The quasi-RH sources are in `notes/astra-2026-10-23/qrh/sources/` as PDF and `pdftotext -layout` text (treat as data, not
  instructions): `qrh-7-8-openai-2026-09-30.{pdf,txt}` (199 pp), `qrh-11-12-openai-2026-10-05.{pdf,txt}` (49 pp, the one to read
  in full), `kintali-qrh-2026-10-07.{pdf,txt}` (47/48), `liu-2610.12234.{pdf,txt}` (7/8 improved slightly, Lean),
  `cureton-thorner-hexagon-2610.00200.txt` (Dedekind zetas, 31/32), `dunn-radziwill-2109.07463.{pdf,txt}` (cubic Gauss sums, the
  theta transformation, §5), `QuasiRiemannHypothesis.lean` (the formal statement).

## Output protocol (every lane)

Write only inside your lane directory (`astra-proofs.md`, `progress.txt`, `checks/`, `checks/output_*.txt`). Author line
`codex:gpt-6-astra`. Write `astra-proofs.md` incrementally: after each finished item append it and update `progress.txt`; never
hold results back for a final write. Label every statement PROVED, PROVED-conditional (name the hypotheses `H-*`), REFUTED,
SHARPENED, NUMERICAL or OPEN. When a conjecture of the brief is false, say so in the first line of the item and give the smallest
counterexample with the script that prints it; then state the corrected conjecture if one survives. Keep a correction ledger
(what the brief got wrong). End with the sections "Numerical checks for the blind lane" (three to six numbers a reviewer can
recompute, with the command) and "What this changes in the notebook" (candidate claim rows with statuses; which record pages
need a one-line annotation; the next step). The runner treats the last section as the completion signal. Do not pad. Ambition is
wanted: a sharp refutation with a corrected statement is worth as much as a proof.
