# Finite CCM tensor networks — final repair and lockstep review

Reviewer: continuous-lane agent, reviewing the other finite/root authors;
2026-09-18. Proposers and critic are from the same OpenAI model family.
This is an independent same-family review, not cross-family evidence.

This round adjudicates changes since
`notes/reviews/ccm-tensor-finite-r1.md`; unchanged proofs retain precisely
their r1 scopes. **No claim authored by this reviewer in the continuous
lane is reviewed or promoted here.** In particular the continuous
quotient theorem, infinite Gram theorem and their negative rows remain
under the other critic's review.

Reviewed final sources: central definitions in 02i; finite shards 03g,
03h, 03j, 03k; `finite.md`, `hamiltonian.md`, `examples.md`; the finite
claim/definition/notation database entries; the campaign entry note;
the active CCM focus and corrected proposal in `HANDOFF.md`; and the
repair table. Source-restoration and full-document build work outside
this scope are not mathematical objections to the statements below.

## 1. Repair adjudication

### F-04: retained invariant spaces — FIXED

`finite.md`, “Retained subtraction is not automatically a physical
contraction”, now says a union of full generalized eigenspaces is a
sufficient canonical spectral choice and that partial multiplicities
require an additional invariant-subspace choice. I rechecked the
counterexample `E=I2` restricted to a line. This agrees with
`def:ccm-tn-spaces`; neither artifact falsely makes whole eigenvalue
classes necessary. No remaining objection.

### F-05: nonempty normalized histories — FIXED

Central `def:ccm-tn-spaces` now imposes `d>=1` for the history-state
constructions, and `def:ccm-tn-feature` now specifies `K>=1`.
`hamiltonian.md` explicitly begins on a nonzero retained space.
`prop:ccm-tn-history-hamiltonian` additionally assumes `K>=2`.
Consequently `vec(I)/sqrt(d)` and `W/(Kd)` are defined, the feature
identity has nonzero dimension, and the path Laplacian has a positive
eigenvalue. These are exactly the missing hypotheses; the r1 proof
needs no further change.

### F-06: Pauli realization — FIXED

03j's opening and reconstruction paragraph now specify the graded
nonbacktracking edge lift and cancellation of common even/odd factors.
`examples.md` states the same input and explicitly distinguishes the
raw doubled adjacency spectrum `6,-2,-2,-2`. This agrees with the
independently computed six-edge determinants in r1 R4. The explicit
two-dimensional companion proposition has not acquired any broader
claim about reconstructing the Pauli letters.

### F-01–F-03: already repaired in r1 — PRESERVED

The final files retain the simple-radical qualification for shifted
kernel reconstruction; physical parent space `ker Gamma*`, distinct
from redundant boundary data `ker Gamma`; and the matched conjugation
of the history and its kernel projector. Central definitions and the
shards use the conjugated-feature history, whose marginal is `W`.
No changed text reintroduces the earlier defects.

## 2. New summary-only objection and its repair

### F-07 — MAJOR, fixed during this delta pass

**Initial location:** the new CCM summary in `HANDOFF.md`, former
lines 209–211. It combined a nullvector of the shifted coefficient
Hamiltonian with the parent constraint on the transfer history.

**Independent computation:** In the existing three-root fixture, the
two-length unshifted matrix is `W=3I2`, whereas `T=W-3I2=0`.
Every vector is null for `T`. The original transfer history has
clock marginal `W`; for any normalized rank-one projector `P`,
`||(P tensor I)Omega||^2=Tr(PW)=3`, not zero. Thus an arbitrary
shifted nullvector does not constrain the original history.

**FIX DEMAND:** Distinguish an exact unshifted nullvector, whose
projector annihilates the original transfer history, from a minimum
made null by scalar subtraction. The latter constrains only a newly
constructed purification of the shifted Gram matrix, unless further
conditions are supplied.

**SURVIVING STATEMENT:** A positive Gram matrix's kernel projector
annihilates its own purification; scalar subtraction changes that
Gram matrix and in general changes the compatible history.

**Adjudication:** The repaired HANDOFF now states this distinction
explicitly, including the new-purification qualification and the
removal of the shifted vector in the CCM quotient. This matches
03k's full-rank-window discussion and `hamiltonian.md` step ⟨1⟩4.
The response and issue ledgers record F-07. The major objection is
resolved, with no outstanding summary inflation.

## 3. Database, definition and summary alignment

⟨1⟩1. The eight previously promoted finite positive rows have the
same scope as the r1 authorizations. Their report `claimstatus`
markers agree with `db/claims.tsv`; their proof and review paths exist.
The history-Hamiltonian row remained `sketched` during this check,
pending the receipt below. No new finite assertion was silently
included in a promoted row.

⟨1⟩2. The two finite negative rows retain the literal rejected
assertions, with `refuted` status in both the database and 03h.
Their counterexamples and surviving replacements match r1. Nothing
in the audited finite dependency rows relies on either rejected
assertion as a positive input.

⟨1⟩3. The central moment matrix uses `t_(k-j)`, the operator metric
is `Tr(G^-1 A* G B)`, and the history conjugates the whitened
features. The new notation entries and macros preserve these
conventions. The replacement of the nullvector's bare symbol by
`TNnull=boldsymbol(xi)` in the finite example/Hamiltonian shards is
typographical and does not alter any equality or hypothesis.

⟨1⟩4. The campaign entry note correctly separates four spaces,
support from weights, native from supplied metrics, raw adjacency
from Pauli edge data, and clock locality from physical-site locality.
The repaired HANDOFF has the same finite content. Its statement that
the Riemann bond remains open is not weakened by the finite results.
The research notes' initial-author-SKETCH labels are historical
proposal labels; the central database is the current status ledger.

⟨1⟩5. The response table's old “critic adjudication pending” cells
for F-01–F-03 may now be replaced by references to r1/r2. That is
recordkeeping after this receipt, not an unresolved mathematical
condition. Likewise the entry note may list this r2 review alongside
r1 once the final promotion is applied.

## 4. Changed checker verification

Since r1 the permanent checker added the physical-parent adjoint
fixture, unary automaton, conjugated canonical history, pinning, and
the copied clock-conjugation mutation. I inspected those additions
and ran

```
python3 -O scripts/ccm_tensor_network.py --self-test
```

Result: **157 atomic conditions passed; both copied mutations were
rejected with the intended nonzero exits**. The printed output agrees
with `outputs/ccm_tensor_network.txt`. Assertions are implemented by
explicit exceptions and survive optimized Python. This rerun was
justified by changed checker coverage; no unchanged proof was
reopened because of unrelated source-restoration work.

The independent r1 critic checker remains the separate exact check
of a four-clock gap, nonorthogonal-projector unary instance, and the
six Pauli edge determinants, with its two finite copied mutations.
Running the shared continuous fixture is not adjudication of this
reviewer's own continuous arguments.

## 5. Final promotion scope and gate receipts

**PROMOTE `prop:ccm-tn-history-hamiltonian` to PROVED with this exact
scope:** Let `E*GE=G>0` on a finite retained space of dimension
`d>=1`, and let `K>=2`. On the centrally defined conjugate feature
space, the positive propagation Hamiltonian has ground space
`{sum_(j=0)^(K-1) |j> tensor V^j w : w in conjugate End(V_ret)}`,
of dimension `d^2`, and first positive eigenvalue
`2-2cos(pi/K)`. Adding the stated boundary projector that pins the
initial normalized identity feature leaves the unique ground-state
line of the transfer history. Locality is only between adjacent
clock values. No physical-site locality or gap of the pinned sum is
asserted.

The central hypotheses now justify the unchanged path-conjugacy and
pinning proof checked in r1 R5. Include metric unitarity explicitly
when copying the scope into the database statement.

VERDICT prop:ccm-tn-history-hamiltonian: VALID

**MAINTAIN the other eight finite positive promotions at their r1
scopes**, with only the repaired nonempty-space qualifications and
precise Pauli edge terminology. These receipts authorize no stronger
claims than the registered final statements examined above.

VERDICT prop:ccm-tn-operator-gram: VALID

VERDICT prop:ccm-tn-clock-state: VALID

VERDICT thm:ccm-tn-atomic-reconstruction: VALID

VERDICT prop:ccm-tn-trace-semisimplification: VALID

VERDICT prop:ccm-tn-graded-net-criterion: VALID

VERDICT obs:ccm-tn-no-letter-reconstruction: VALID

VERDICT prop:ccm-tn-pauli: VALID

VERDICT prop:ccm-tn-clock-hamiltonian: VALID

**Required gate convention for the next two receipts:** `VALID`
means the **refutation is valid**, not that the rejected assertion is
true. Both database and report statuses must remain **REFUTED**.

For `obs:ccm-tn-unqualified-kernel`, the rejected assertion is that
every critical trace-moment null polynomial annihilates its original
retained operator. The Jordan matrix `[[1,1],[0,1]]` has constant
trace moments `2`, null polynomial `z-1`, and nonzero `E-I`.
The original statement is false; the refutation is valid. The
semisimple-qualified replacement remains
`prop:ccm-tn-trace-semisimplification`.

VERDICT obs:ccm-tn-unqualified-kernel: VALID

For `obs:ccm-tn-positive-supertrace`, the rejected assertion is that
unitary even and odd transfer blocks imply a positive supertrace Weil
form. The physical letter `A=P=diag(1,-1)` has unitary even/odd
blocks `I2,-I2`, but its two-length form is `[[0,4],[4,0]]`, negative
on `(1,-1)`. The original statement is false; the refutation is
valid. The net-weight-qualified replacement remains
`prop:ccm-tn-graded-net-criterion`.

VERDICT obs:ccm-tn-positive-supertrace: VALID

No HOLD remains for a finite claim in the reviewed scope. No new
cited-fact or continuous-lane row is adjudicated by this document.

PASS (all F-01–F-07 repairs adjudicated; finite statements, definitions, database scopes and final summaries agree).
