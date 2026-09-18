REVIEWER: codex:gpt-6 (same-family lockstep audit)

# Continuous CCM tensor network: round-2 lockstep verdict

**Scope.** Delta review after integration and promotion. I audited:

- `report/sections/02i_definitions_ccm_tensor.tex`;
- `report/sections/03i_ccm_tensor_algorithm.tex` and
  `report/sections/03l_ccm_tensor_continuous.tex`;
- the eight continuous positive/refuted rows in `db/claims.tsv`, their generated status rows, the
  seven CCM definitions, and the CCM notation/provenance rows;
- `notes/ccm-tensor-network/continuous.md`, `notes/ccm-tensor-network.md`, `HANDOFF.md`,
  `notes/ccm-tensor-network/ISSUES.md`, and `repair-r1-response.md`;
- the source formulas and independent checks already used in round 1.

This review adjudicates lockstep and deltas; it does not re-litigate round-1 mathematics that was
unchanged and already recomputed. The review remains same-family, as disclosed in the entry note.

## Outcome

The integrated continuous claims are mathematically and editorially sound. The minus Fourier
convention is single-source, the exact intertwiner inherits the simple-radical hypotheses, C9 now
names reflection invariance and remains unregistered, the stronger false statements are retained as
`refuted`, and the summaries do not promote a Riemann bond or increasing-window convergence.

I found two MINOR bookkeeping defects: the two refuted continuous rows omit their refuting
propositions from the dependency DAG, and two campaign ledger files still describe the already
completed review as pending. Neither changes a theorem statement or status.

Fresh verification:

- `notes/ccm-tensor-network/review-continuous/check_continuous_r1.py`: `26 PASS / 0 FAIL`;
- `scripts/ccm_tensor_network.py --self-test`: all checks pass (`157` atomic conditions and two red
  mutations);
- claim-row/report-status comparison: all eight continuous rows match exactly;
- `git diff --check`: clean;
- generated status files: current.

The full lab-book gate presently stops on source directories assigned to the separate restoration
lane and on two finite negative rows lacking explicit verdict strings. It reports no error for a
continuous CCM claim, definition, notation row, or the two new CCM provenance formulas.

## Delta objections

### R2-1. Refuted continuous rows omit the claims that refute them from `deps`

- **Location.** `db/claims.tsv:377-378`:
  `obs:ccm-tn-naive-compression` and `obs:ccm-tn-raw-infinite-gram` both have `deps=-`.
- **Severity.** MINOR (DAG bookkeeping).
- **Independent audit.** The report text itself supplies the dependencies:
  `03i_ccm_tensor_algorithm.tex:184-186` cites
  `prop:ccm-tn-no-naive-compression`, and `03l_ccm_tensor_continuous.tex:176-177` cites
  `prop:ccm-tn-infinite-smeared-gram`. Those are exactly the proved counterexample/surviving claims
  that earned the two `refuted` statuses.
- **FIX DEMAND.** Make the two dependency cells exact:

      obs:ccm-tn-naive-compression       deps=prop:ccm-tn-no-naive-compression
      obs:ccm-tn-raw-infinite-gram       deps=prop:ccm-tn-infinite-smeared-gram

- **SURVIVING STATEMENT.** Both refutations and their statuses remain valid. This repair only makes
  the DAG record the proofs already cited by the shards.

### R2-2. Campaign ledgers still say adjudication is pending

- **Location.** `notes/ccm-tensor-network/ISSUES.md:3-17` says “No adjudicated promotions yet”,
  labels TN-01--TN-07 as “Investigating”, and calls F-01 “awaiting adjudication”.
  `notes/ccm-tensor-network/repair-r1-response.md:5-7` still says “critic adjudication pending”.
  `notes/ccm-tensor-network.md:5-6` lists only the r1 review files and will omit this r2 record.
- **Severity.** MINOR (stale summary/status surface).
- **Independent audit.** `db/claims.tsv:359-378`, the six integrated CCM shards, and
  `report/generated/status.tex:361-380` now contain the adjudicated statuses. The continuous author
  note correctly points to the database and says C9 alone remains an unregistered SKETCH. HANDOFF
  and the entry note state the qualified mathematical conclusions accurately.
- **FIX DEMAND.** Either mark the first ISSUES table explicitly as an archived campaign-start
  snapshot, or replace its false introductory sentence and state cells with the adjudicated
  outcomes. In `repair-r1-response.md`, replace the three “critic adjudication pending” phrases by
  “adjudicated in `notes/reviews/ccm-tensor-finite-r1.md`”. Add
  `notes/reviews/ccm-tensor-continuous-r2.md` to the review-record sentence in the entry note.
- **SURVIVING STATEMENT.** The authoritative database and published summaries already have the
  correct claim scopes. Only the process ledger is stale.

## Exact claim/status/dependency adjudication

### Positive continuous rows

`VERDICT prop:ccm-tn-continuous-smeared-gram: VALID`

Status `proved` is exact. The statement requires finite self-adjoint `H`, the central minus Fourier
convention, and compactly supported integrable tests. The shard proves both the operator Gram and
the unshifted radical statement. No further claim dependency is needed.

`VERDICT prop:ccm-tn-loewner-displacement: VALID`

Status `proved` is exact. Its scope is the real one-sided half-interval form of
`def:ccm-tn-window-form`. The Loewner entries, reflection, rank-at-most-two displacement, and
boundary covector are proved. The formula provenance is supplementary; the proof is internal.

`VERDICT thm:ccm-tn-loewner-quotient: VALID`

Status `proved` and dependency `prop:ccm-tn-loewner-displacement` are exact. The registered
statement includes the shifted metric, nonzero normalization, correction, quotient polynomial,
reality, and the absence of any `epsilon>=0` assumption, all proved in 03i.

`VERDICT prop:ccm-tn-no-naive-compression: VALID`

Status `proved` and dependency `thm:ccm-tn-loewner-quotient` are exact. The `N=1` example has
quotient roots `+-sqrt(2)` outside `[-1,1]`; the `-10I` shift separately proves that real output
does not certify positivity of the unshifted input.

`VERDICT prop:ccm-tn-infinite-smeared-gram: VALID`

Status `proved` is exact. Pure-point self-adjointness, local finite polynomial counting growth, and
smooth compact support imply Hilbert--Schmidt smearing and a trace-class product. The raw unitary
obstruction is the diagonal identity trace, with no regularized trace silently substituted.

`VERDICT prop:ccm-tn-exact-continuous-intertwiner: VALID`

Status `proved` and dependencies
`thm:ccm-tn-loewner-quotient;prop:ccm-tn-continuous-smeared-gram` are exact. The theorem explicitly
inherits even-simplicity, adds a supplied finite spectral model and `epsilon=0`, and proves the
simple-radical quotient isometry and scaled-generator intertwining. It does not assert an infinite
or arithmetic realization.

### Negative rows

`VERDICT obs:ccm-tn-naive-compression: VALID`

Status `refuted` and statement scope are exact. Add the dependency requested in R2-1. The shard
preserves the surviving corrected quotient in the `T` metric.

`VERDICT obs:ccm-tn-raw-infinite-gram: VALID`

Status `refuted` and statement scope are exact. Add the dependency requested in R2-1. The shard
preserves the valid smeared form under explicit summability.

### Open and omitted scopes

`obs:ccm-tn-riemann-bond-open` correctly remains `open`: no arithmetic retained flow, physical
letters, metric, distributional trace, grading, or increasing-window intertwiner has been
constructed. C9's fixed-window limit remains a source-backed author SKETCH and has no claim row;
no status surface silently promotes it.

## Definition, notation, provenance, and summary audit

1. `def:ccm-tn-continuous` fixes
   `U(t)=e^{-itH}` and `widehat f(omega)=int f(t)e^{-i omega t}dt`; every occurrence in 03l uses
   that sign. The zeta-side conditional measure is consequently at `-Im rho`, as stated in the
   author note.
2. `def:ccm-tn-loewner` distinguishes the shifted metric from the original form and declares
   quotient self-adjointness an assertion rather than a definition. The theorem discharges it.
3. The physical auxiliary, doubled transfer, operator feature, and cyclic moment spaces remain
   distinct in definitions, notation, shards, entry note, and HANDOFF.
4. The notation descriptions match the definitions, including nonempty retained dimension,
   `W_{jk}=t_{k-j}`, conjugated history, least window vector, response vector, and spectral measure.
5. `prov:ccm25-tn-correlation` and `prov:ccm25-tn-displacement` are exact formula provenance rows
   attached to independently proved claims. They are not `citedfact` rows built from fragmentary
   excerpts. The lab-book provenance check finds the quoted strings when the local CCM source is
   present.
6. HANDOFF and `notes/ccm-tensor-network.md` state only the qualified results: supplied metrics,
   square-free support, signed grading, shifted versus unshifted histories, valid smearing, and the
   still-open Riemann bond. No summary strengthens a conditional intertwiner into an arithmetic
   construction or finite-window reality into RH.
7. The four stronger rejected formulations listed in the entry note correspond exactly to the four
   `refuted` rows. The continuous two have complete counterexamples in their shards.

## External gate notes, not continuous objections

- The lab-book gate also reports that the two **finite** rows
  `obs:ccm-tn-unqualified-kernel` and `obs:ccm-tn-positive-supertrace` point to a review lacking the
  exact required `VERDICT ...: VALID` strings. Their mathematical counterexamples were reviewed,
  but the gate requires those literal adjudication lines or review aliases.
- Missing source-tree errors are assigned to the separate restoration lane, per the coordinator.
- Two bare-notation warnings in 03k concern the Hamiltonian shard, outside this continuous delta.

## Final verdict

No FATAL or MAJOR objection remains. Apply R2-1 and R2-2 as bookkeeping repairs; neither positive
claim needs weakening and neither refuted row needs reopening.

`PASS (2 MINOR bookkeeping repairs)`
