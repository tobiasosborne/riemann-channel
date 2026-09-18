# Finite CCM tensor networks and Hamiltonians — critic round 1

Reviewer: continuous-lane agent, acting as an independent critic of the
finite lane and root's Hamiltonian/example arguments; 2026-09-18.
The author and reviewer agents are from the **same OpenAI model family**.
This is independent recomputation, not cross-family review.

Workflow read: `/home/tobias/.claude/skills/rk-light/SKILL.md`.
Scope read: `notes/ccm-tensor-network/{finite,hamiltonian,examples}.md`,
`report/sections/02i_definitions_ccm_tensor.tex`,
`03g_ccm_tensor_gram.tex`, `03h_ccm_tensor_kernel.tex`,
`03j_ccm_tensor_examples.tex`, and `03k_ccm_tensor_hamiltonians.tex`.
Reused database claims checked: `thm:weil-positivity-finite`,
`thm:weil-duality-pairing`, `prop:hp-inner-product-discrete`,
`prop:weil-blind-jordan`, all already `proved`.
The Carathéodory–Fejér source was read directly at
`refs/src/2511.23257/Araki-final-oct25.tex:760–800,898–909`.

Excluded: **no review or promotion of this reviewer's own continuous CCM
claims**, even where the common checker also runs their finite fixtures.
The quotient discussion in 03k is checked only for its distinction of
spaces, conditional on the separate continuous theorem.

## 1. Independent recomputation

### R1. Metric Gram and all-window converse

ASSUME finite-dimensional `E` and `G>0`, with `E*GE=G`.
PROVE the operator Gram formula in `prop:ccm-tn-operator-gram`.

⟨1⟩1. With `S=G^(1/2)`, cyclicity gives
`Tr(G^-1 A* G B)=Tr((SAS^-1)*(SBS^-1))`, so the operator metric is
positive. `E^sharp=E^-1`, hence its powers contract to
`Tr(E^(k-j))`, with negative powers equal to the conjugate positive
traces. This matches `W_jk=t_(k-j)` and the older form convention
`sum_lk c_l conjugate(c_k) t_(l-k)` after swapping dummy indices.

⟨1⟩2. Under native equality for all powers, the Toeplitz matrix has rank
at most `d^2`. The reused finite Weil theorem puts each eigenvalue in
the closed disc. An interior eigenvalue contributes its positive Poisson
density, making every finite polynomial Gram strictly positive: a
nonzero polynomial cannot vanish almost everywhere on the circle.
This contradicts the rank bound. Thus every eigenvalue has modulus one.

⟨1⟩3. Unitary Schur triangularisation preserves the Frobenius norm.
The `j=k=1` equality says this norm squared is `d`; the `d` diagonal
entries already contribute `d`. Every strict upper entry is therefore
zero. This proves native unitarity without an additional Jordan
assumption. The idempotent `[[1,1],[0,0]]` independently gives the
claimed two-length counterexample. The main proposition and 03g proof
are correct with their all-window hypothesis.

### R2. Clock conjugation and unary MPS

⟨1⟩1. For `Omega=sum_j |j> tensor v_j`, tracing the feature gives
`rho_jk=<v_k,v_j>=W_kj`. For conjugated features it instead gives
`<bar(v_k),bar(v_j)>=<v_j,v_k>=W_jk`. This checks central definition
`def:ccm-tn-history` and both clock propositions, including the
transpose warning in 03g. Each feature has norm squared `d`.

⟨1⟩2. Multiply the proposed unary virtual blocks directly. `M0 M1=0`;
`(1,...,1;0) M1^j M0^(n-j)` has weights `z_a^j` in the second register
when `j<n`, and in the first for `j=n`. The endpoint adds exactly
`sum_a z_a^j P_a=E^j`. Every binary word not of this unary shape has
an adjacent `01` and vanishes. Conjugating all matrices and endpoint
gives central definition's conjugated feature history. The virtual
dimension is `2r`, independent of the number of clock sites.

⟨1⟩3. Distinct spectral idempotents are linearly independent:
multiplying a putative relation by `P_b` isolates its coefficient.
The Vandermonde matrix therefore gives feature rank `min(K,r)`, the
clock–feature Schmidt rank. This is an endpoint bipartition, not a
claim about every unary MPS cut or the original physical chain.

The independent checker tests all 16 binary words at four sites for
three modes, deliberately using nonorthogonal spectral idempotents.
It also rejects a copied mutation of `M0` that permits forbidden words.

### R3. Atomic support, weights and grading

⟨1⟩1. The evaluation matrix `A_aj=z_a^j` gives
`W=A* diag(m_a) A`. Positive weights preserve its rank and kernel.
Polynomial division gives precisely the three window regimes in 03h.
At the critical window the one-dimensional radical is the square-free
support polynomial. Overresolved nullvectors may have extra roots;
common zeros remove them because the square-free polynomial itself
belongs to the nullspace.

⟨1⟩2. Evaluation identifies `C[z]/(p_*)` with one complex coordinate
per distinct node. The weighted product makes multiplication by `z`
unitary and `[1]` cyclic. Its cyclic matrix elements include the
weights, whereas its plain trace counts each node once. A Vandermonde
system using the first `r` moments recovers the weights. Jordan
expansion confirms that traces contain no block-size information and
that square-free `p_*` annihilates the original matrix iff every block
has size one.

⟨1⟩3. For net signed weights `d_a`, the same calculation gives
`sum_a d_a |p(z_a)|^2`. Lagrange interpolation at degree `r-1`
isolates each weight, so `K>=r` already tests the full net criterion.
The tensor `A=P=diag(1,-1)` gives sector spectra `+I2,-I2` and
parity-closed counts `2-2(-1)^n`. Its two-length form has eigenvalues
`+4,-4`, despite nonnegative scalar ring counts and unitary sectors.
The stated net-sector non-identifiability follows by adding one equal
copy to both sectors.

⟨1⟩4. The fixed labelled tensors `(1,0)` and `(1/sqrt(2),1/sqrt(2))`
have the same scalar doubled transfer but distinct product-state
amplitudes. This proves the no-letter-reconstruction observation
with its explicit fixed-basis scope.

### R4. Pauli representative and the actual edge realization

⟨1⟩1. For `E=[[0,-5],[1,-2]]/sqrt(5)` and
`G=[[1,-1],[-1,5]]`, direct multiplication gives `E^T G E=G`.
The leading minors `1,4` give positivity. Direct squaring gives
`E^2+(2/sqrt(5))E+I=0`. The native norm squared is `6`.

⟨1⟩2. Tracing gives `(t0,t1,t2)=(2,-2/sqrt(5),-6/5)`; the
three-length matrix has characteristic polynomial
`s(s-14/5)(s-16/5)` and kernel `(1,2/sqrt(5),1)`. These computations
verify the whole explicit `prop:ccm-tn-pauli` without using a
conjectural metric or the previously sketched general Pauli theorem.

⟨1⟩3. I also recomputed the actual six-letter nonbacktracking lift,
using paired labels `(X,X,Y,Y,Z,Z)`. On the Pauli operator basis each
letter conjugation is a scalar sign. For signs `w_i` and reversal
`i -> i xor 1`, its six-edge block is
`T_ij=w_i` when `j != inverse(i)`, and zero otherwise. Direct exact
determinants give
`det(I-uT_I)=(1-u^2)^2(1-6u+5u^2)` and, for each nonidentity Pauli,
`det(I-uT_sigma)=(1-u^2)^2(1+2u+5u^2)`.
Parity `P=Z` makes `I,Z` even and `X,Y` odd. Their quotient is
`(1+2u+5u^2)/((1-u)(1-5u))`, establishing the two retained values
after net cancellation. This is the **edge** realization; the raw
doubled adjacency has eigenvalues `6,-2,-2,-2`.

### R5. Clock and propagation Hamiltonians

⟨1⟩1. `W=F*F>=0` and `ker W=ker F`. For the conjugated-feature
history centralised in 02i, `rho_clock=W`. Its kernel projector obeys
`||(Pker tensor I)Omega||^2=Tr(Pker W)=0`. Conversely a clock operator
annihilates that history iff it kills the support of this marginal.
`W` itself is generally not a parent annihilator. The root's distinction
between a ground vector of `W` and a forbidden direction of the history
is correct.

⟨1⟩2. The whitened transfer is unitary, so its conjugate left
multiplication `V` is unitary on a feature space of dimension `d^2`.
Expanding `L_j*L_j` gives exactly the off-diagonal orientations in
03k. Zero energy is equivalent to `w_(j+1)=V w_j`, giving the stated
`d^2`-dimensional ground space.

⟨1⟩3. With `B=sum_j |j><j| tensor V^j`,
`B* (|j+1><j| tensor V) B=|j+1><j| tensor I`.
Thus the full operator is unitarily equivalent to the path Laplacian
tensored with `I_(d^2)`. The cosine vector
`cos((j+1/2) ell pi/K)` obeys the two endpoint equations as well as
the interior recurrence, proving eigenvalues
`2-2cos(ell pi/K)`, `ell=0,...,K-1`.

⟨1⟩4. The positive pinning term kills precisely initial features
in the line of normalized `vec(I)`. Intersecting with the propagation
ground space gives one history line. No gap for the pinned sum is
claimed. Locality is only adjacency of clock values; nothing here
gives physical-site locality of the original MPS.

The independent fixture checks `K=4,d=2`: unpinned nullity `4`, gap
`2-sqrt(2)`, pinned nullity `1`, and exact annihilation of the
conjugated-feature history. A copied omission of feature conjugation
is rejected. The normalization and gap statements require `d>=1`;
see F-05.

## 2. Numbered objections and in-turn adjudication

### F-01 — MAJOR, repaired during review: degenerate fitted minimum

**Location initially:** `finite.md:344–347`, paragraph “Minimal-eigenvector
correction”. It said a shifted matrix's kernel polynomial reconstructs
the fitted measure without requiring a simple least eigenvalue.
**Computation:** Three unit cube roots with unit weights give, for
`N=1`, `W=3I2`, hence shifted matrix zero. The chosen nullvector
`(1,-1/2)` has polynomial root `2`. The fitted zero measure has no
such support. **FIX DEMAND:** Require one-dimensional radical for an
individual kernel polynomial to recover the fitted support; otherwise
use common zeros/gcd and preserve arbitrary extra roots.
**SURVIVING STATEMENT:** Positive scalar subtraction gives a new
singular Toeplitz moment problem, with the same kernel-rank caveats
as the original atomic problem.
**Adjudication:** FIXED in the current `finite.md` paragraph. Root
`03h:49–55` already imposed the one-dimensional-radical condition.
The permanent checker now contains this counterexample. No remaining
major objection at this location.

### F-02 — MAJOR, repaired during review: the physical parent kernel

**Location initially:** `finite.md:454–456`, map-comparison table.
The kernel of the boundary-to-physical map was labelled a physical
parent-space relation. **Computation:** For `B=C`, `(A0,A1)=(1,0)`,
`Gamma_1(x)=x|0>`, so `ker Gamma_1=0` but the physical parent
constraint is the nonzero line `span{|1>}=ker Gamma_1*`.
**FIX DEMAND:** Identify `ker Gamma_ell` as invisible/redundant boundary
data; the physical parent space is `ker Gamma_ell*=(im Gamma_ell)^perp`.
**SURVIVING STATEMENT:** The physical parent and the length-polynomial
kernel concern different maps and different Hilbert spaces.
**Adjudication:** FIXED in the current table and following explicit
example. Root 03k's clock-parent argument did not have this defect.

### F-03 — MAJOR, repaired during review: clock projector conjugation

**Location initially:** `finite.md:459`, “a projector onto ker W_N is a
global clock constraint for the transfer-history state”, following F5's
displayed unconjugated history. **Computation:** Let `E=diag(1,i)` and
`xi=(i,-1-i,1)`. For `Omega=sum_j |j> vec(E^j)`, the normalized
projector on `xi` gives residual norm squared `2`; the projector on
`bar xi` gives zero. **FIX DEMAND:** Specify the conjugated-feature
history for `P_(ker W)`, or use `P_(conjugate ker W)` for F5's displayed
history. **SURVIVING STATEMENT:** The projector annihilates precisely
the history whose marginal has that kernel.
**Adjudication:** FIXED in the current paragraph. Central 02i and
root 03g/03k consistently use conjugated features and are correct.

### F-04 — MINOR, pending: whole generalized eigenspaces are sufficient

**Location:** `finite.md:95–97`. The statement says an actual retained
restriction must contain whole generalized eigenspaces.
**Computation:** `E=I2` restricted to any chosen one-dimensional line
realizes a retained multiplicity of one, without retaining the full
two-dimensional eigenvalue class. **FIX DEMAND:** Say sums of full
generalized eigenspaces give a canonical spectral restriction; partial
multiplicities require an additional invariant-subspace choice.
**SURVIVING STATEMENT:** Formal spectral subtraction alone does not
specify that subspace or its native metric. Central 02i:21–23 already
has the correct weaker statement.

### F-05 — MINOR, pending: nonempty space for normalized histories

**Location:** `hamiltonian.md:58–60,82`; `03k:58–69`; normalized clock
paragraph `03g:151–154`; central 02i allows an empty retained space.
**Computation:** With `d=0` the feature Hilbert space is zero, there is
no positive eigenvalue, and `vec(I)/sqrt(d)` and `W/(Kd)` are undefined.
Metric unitarity on that zero space is vacuous. **FIX DEMAND:** State
`K,d>=1` for normalized histories, and `d>=1,K>=2` for the propagation
gap/pinning theorem, either centrally or in the relevant hypotheses.
**SURVIVING STATEMENT:** All these formulas and the claimed gap hold
for nonempty retained space; the unnormalized Gram identity extends
vacuously to the zero space.

### F-06 — MINOR, pending: name the Pauli edge realization

**Location:** `03j:12–15,73–76`; `examples.md:58–61`.
**Computation:** R4⟨1⟩3 gives the claimed retained pair from the
nonbacktracking graded edge determinant after even/odd cancellation.
The raw doubled adjacency has spectrum `6,-2,-2,-2`, not that pair.
**FIX DEMAND:** Say explicitly “six-letter nonbacktracking graded
transfer, after net cancellation”, rather than leaving the realization
implicit. **SURVIVING STATEMENT:** The displayed companion/metric
proposition is fully correct; its input pair is the retained edge
divisor of this physical example.

## 3. Reproducible checks and red capability

* Ran `python3 scripts/ccm_tensor_network.py --self-test`: initial
  version passed 99 atomic conditions and its copied boundary mutation.
* After the new F-01 regression landed, ran
  `python3 -O scripts/ccm_tensor_network.py --self-test`: 117 conditions
  passed and the copied boundary mutation returned the expected nonzero
  exit. The rerun was justified by the added regression.
* Wrote and ran the independent critic script
  `notes/ccm-tensor-network/review-finite/independent_checks.py` under
  `python3 -O`: 37 exact conditions, plus two copied finite red mutations
  (omitted conjugation and corrupted unary tensor), both rejected with
  exit 1. The script uses explicit exceptions, no bare assertions.
* The independent script's first run exposed a duplicate-substring bug
  in its mutation-target uniqueness guard. The guard was repaired to
  count complete lines; the final run exercised and rejected both
  intended mutations. No shared source was mutated.

The checks corroborate the addressable derivations; their finite fixtures
are not proofs of the general statements. The shared checker includes a
continuous-lane toy, but running it does not constitute adjudication of
this reviewer's own claims.

## 4. Per-claim decisions and exact promotion scope

All decisions concern mathematical statements at this review snapshot.
The final database/report lockstep pass remains outstanding: the new
claim rows had not yet been integrated when this review was written.
No source proof, status or dependency outside these scopes is promoted.

**PROMOTE `prop:ccm-tn-operator-gram`:** finite metric-unitary operator
Gram identity; native all-power equality implies native unitarity;
the two-length counterexample refutes an unrestricted fixed-window
converse. Proof R1 / 03g steps 1–4.

VERDICT prop:ccm-tn-operator-gram: VALID

**PROMOTE `prop:ccm-tn-clock-state`:** for the centrally defined
conjugated-feature history, marginal `W`, squared norm `Kd`, exact
operator kernel, unary virtual dimension at most `2r`, and endpoint
Schmidt rank `min(K,r)`. These are unnormalized statements; normalized
state prose must exclude `d=0`. Proof R2 / 03g steps 1–4.

VERDICT prop:ccm-tn-clock-state: VALID

**PROMOTE `thm:ccm-tn-atomic-reconstruction`:** positive finite
circle-supported measure, evaluation Gram, rank and exact three window
regimes, and separately recovered weights. An arbitrary shifted
minimal eigenvector is not added to this scope. Proof R3⟨1⟩1 / 03h.

VERDICT thm:ccm-tn-atomic-reconstruction: VALID

**PROMOTE `prop:ccm-tn-trace-semisimplification`:** the weighted cyclic
moment shift, distinct support once, square-free annihilator iff
semisimple, recovered integer weights determining the semisimple
similarity class, no Jordan/eigenvector recovery. Proof R3⟨1⟩2.

VERDICT prop:ccm-tn-trace-semisimplification: VALID

**PROMOTE `prop:ccm-tn-graded-net-criterion`:** circle-supported sector
trace moments are positive for all windows iff every net weight is
nonnegative; `K>=r` detects this; the physical one-letter parity example
and sector-cancellation obstruction have the stated scope. Proof R3⟨1⟩3.

VERDICT prop:ccm-tn-graded-net-criterion: VALID

**PROMOTE `obs:ccm-tn-no-letter-reconstruction`:** ring norms fail to
identify letters in a fixed labelled physical basis, as shown by the
two scalar-bond tensors. Do not convert this into a classification of
all realizations modulo arbitrary physical transformations. Proof R3⟨1⟩4.

VERDICT obs:ccm-tn-no-letter-reconstruction: VALID

**PROMOTE `prop:ccm-tn-pauli`:** the explicitly displayed two-dimensional
companion and positive metric, its three-length Gram/kernel/spectrum,
and native-HS mismatch. The edge interpretation is independently
verified by R4⟨1⟩3 but must be named as in F-06; this does not promote
every assertion of the older general graded-Pauli proposition.

VERDICT prop:ccm-tn-pauli: VALID

**PROMOTE `prop:ccm-tn-clock-hamiltonian`:** metric-unitary retained
operator, central conjugated history, `W=F*F>=0`, polynomial-relation
ground space, and its clock-kernel projector annihilating the history.
This is a clock constraint, not a physical-site parent construction.
Proof R5⟨1⟩1.

VERDICT prop:ccm-tn-clock-hamiltonian: VALID

**HOLD `prop:ccm-tn-history-hamiltonian` only for F-05:** the proof is
correct for `d>=1,K>=2`, including full ground space, gap, unique
ground line after pinning, and clock-only locality. Add that nonempty
space hypothesis before promotion; no further proof is missing.

**SOURCE VERIFIED `cit:ccm-cf-vandermonde` if integrated:** the proposed
finite positive Toeplitz Vandermonde factorization and exact source
quotation match the checked local source at lines 772–786. Do not add
uniqueness in the full-rank case; it was neither proposed nor reviewed.

No `VERDICT` entry for any continuous-lane claim, or for a combined
numerical row whose final statement has not yet been registered.

**REFUTE `obs:ccm-tn-unqualified-kernel`.** Exact rejected statement:
“The critical trace-moment null polynomial always annihilates the
original retained operator.” For `E=[[1,1],[0,1]]`, all trace moments
equal `2`; the critical two-length matrix is `2*ones(2,2)`, whose
null polynomial is `z-1`, while `E-I` is nonzero. This is an exact
counterexample satisfying circle support and positive trace moments.
Retain this stronger statement with status **REFUTED**. Its surviving
replacement is `prop:ccm-tn-trace-semisimplification`, including the
semisimplicity condition.

VERDICT obs:ccm-tn-unqualified-kernel: REFUTED

**REFUTE `obs:ccm-tn-positive-supertrace`.** Exact rejected statement:
“Unitary even and odd transfer blocks imply a positive supertrace Weil
form.” For the physical one-letter tensor `A=P=diag(1,-1)`, its
doubled transfer has even block `I2`, odd block `-I2`. Both are unitary,
but the supertrace two-length form is `[[0,4],[4,0]]`, negative on
`(1,-1)`. Retain the stronger statement with status **REFUTED**. Its
surviving replacement is `prop:ccm-tn-graded-net-criterion`, using
nonnegative net weights or a separately specified odd-sector form.

VERDICT obs:ccm-tn-positive-supertrace: REFUTED

PASS (F-01–F-03 repaired; no open FATAL/MAJOR; F-04–F-06 require the stated minor scope edits before the final lockstep pass).
