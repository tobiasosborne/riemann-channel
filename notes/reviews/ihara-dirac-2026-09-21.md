# REFUTE review: square roots of Ihara--Bass (chiral linearisation, oriented half, odd letters)

Reviewer: `claude:fable-5.1` (the orchestrator of the round; TJO's instruction for this session was
"no Opus or Sonnet subagents", so the two-family structure of the round is prover
`codex:gpt-6-astra` / reviewer `claude:fable-5.1`, and the reviewer is also the author of the brief
and of the numerics). Date: 2026-09-21. Prover: `codex:gpt-6-astra` at xhigh. Numerics:
`scripts/ihara_dirac.py`, 158 checks (137 written before the proofs were read, 21 added after the
prover's corrections, reproducing every counterexample of the correction ledger; all pass).

## Inputs read (in full)

| file | what it is |
|---|---|
| `notes/ihara-dirac/astra-brief.md` | the brief, T1--T4, drafted slightly too strong |
| `notes/ihara-dirac/astra-proofs.md` | the prover's output: hypothesis register, Lamport proofs, correction ledger |
| `notes/ihara-dirac/numerics.md`, `scripts/ihara_dirac.py`, `outputs/ihara_dirac.txt` | the numerics lane |
| `report/sections/08_quantum_ihara_general.tex` | `thm:qihara-general`, its proof (`H = SR - J`, the pair factor), `cor:qihara-unitary` |
| `report/sections/02h_definitions_graded_ramanujan.tex`, `03c_graded_ramanujan.tex` | `def:graded-hashimoto`, `def:index-two-grading`, `thm:graded-qihara-bass`, `prop:p-mode`, `num:graded-ramanujan` |
| `refs/src/1709.06052/2018_KW_JSP__Nov1.tex`, `refs/src/1307.2494/final.tex`, `refs/src/0912.3200/lsfinal-ejc16122014.tex`, `refs/src/2501.08803/main.tex` | the four sources with byte addresses in the shard |

Every algebraic step of the prover's text was re-derived by hand below or re-run numerically; the
scratch computations are in `scripts/ihara_dirac.py` (the 21 checks added after the proofs) and in
the prover's own `notes/ihara-dirac/scratch/` (not relied on).

## Verdicts

### T1ab (`prop:chiral-linearisation`)

**What I attacked.** (1) The sign and the factor `u` in the Schur complement on `V`: `A_u - S(uR) =
I + uJ - uSR = I - uH` since `H = SR - J` (shard 08, step <1>1); correct. (2) The claim that the
nonzero spectra of `XY` and `YX` agree with algebraic multiplicities: the prover's
`det(tI_W - YX) = t^{ND-N} det(tI_V - XY)` is the standard Sylvester identity for rectangular
factors; correct. (3) The prover's correction that the index `N(D-1)` is the difference of
*generalized*-kernel dimensions, not of ordinary nullities: the counterexample `V = C`, `D = 2`,
`E_1 = 1`, `E_2 = 2`, `u = 3/4` was recomputed by hand (`A_u = [[1, 3/2],[3/4, 1]]`, `det = -1/8`,
`X = (3, -3)`, `XY = 0`, `YX` nilpotent of rank one): both ordinary kernels have dimension one; the
correction is right and the brief's phrase "excess kernel" was loose. (4) `YX = u(H + J)(1 + uJ)^{-1}`:
`SR = H + J`, immediate. Numerics T1(a), T1(b) on four families agree to `1e-9`.

**VERDICT T1ab: VALID** (with the prover's correction of "kernel" to "generalized kernel", applied
to the shard).

### T1c (`prop:euler-exponent-berezinian`)

**What I attacked.** Whether the Berezinian of the *unrescaled* mass `diag(I + uJ, I)` could be
meant: it is `(1 - u^2)^{ND/2}`, not the Euler factor; the shard states the rescaled mass
`diag(I + uJ, (1 - u^2) I_V)`, as the prover requires, and the rescaling is exactly the scalar
denominator of the Bass Schur complement `I - uR(I+uJ)^{-1}S = (1-u^2)^{-1}(I - u Sigma + q u^2)`.
The sign convention: even blocks in the numerator, odd in the denominator, so edges even and
vertices odd give `ND/2 - N`; reversing the grading inverts it. The prover's remark that the
parity `k + 1` of `def:graded-geodesic-determinant` is stated there only for `k >= 1` and is here
*extended* to `k = 0` is correct and the shard says "the parity `k+1` given to `k`-cells", which
is the extension. Numerics T1(c) on a unitary family, `1e-9`.

**VERDICT T1c: VALID.**

### T1d (`prop:no-super-coupling`)

**What I attacked.** (1) The brief said the two-loop bouquet is the smallest counterexample; the
prover found one loop (`D = 2`, `H = I_2`, `(1-u)^2` against `1 - u^2`), which is smaller and
right; the shard now gives both. (2) The brief's sentence "the Berezin integral ... is not defined"
was an overclaim; the prover's replacement (the exponent is not even, so the even-Gaussian
Berezinian formula does not apply; integration of a mixed-parity superfunction is meaningful, e.g.
`int dx int dtheta e^{-x^2 + theta x} = 0`) is correct and the shard was rewritten to say exactly
that. (3) The two Schur values `p` and `b^2/p` and their equality criterion `p^2 = b^2`: recomputed;
numerics T1(d) on four families.

**VERDICT T1d: VALID** (after the two corrections, both applied).

### T2 (`prop:oriented-half`)

**What I attacked.** (1) T2(a): the involution `k -> c - k` on `Z/l`; the three cases (`l` odd;
`l` even and `c` even: a fixed point, forcing `a_k = bar a_k`; `l` even and `c` odd: `2k = c - 1`
is solvable since `c - 1` is even, and then `c - k = k + 1`, an adjacent backtrack). Complete,
including `l = 1, 2`; the brief's "check the even case carefully" is answered. Numerics: no
self-reverse class among 1218 classes for `D = 4`. (2) T2(b): the order of adjoints matches the
reversed word; Sylvester makes each factor class-invariant even for singular letters; correct.
(3) T2(c): the radius. The prover's `r = 1/((D-1) M)` improves the brief's `1/(DM)`; the
counting bound (at most `D q^{l-1}` rooted non-backtracking words of length `l`) and the log bound
`N a^l/(1-a)` are right; absolute convergence for `qa < 1`. (4) **The prover's strengthening.** For
Kraus letters `Ad(A)` preserves the real space of Hermitian matrices, so `det(1 - z E_w)` has real
coefficients and `F` does not depend on the orientation choice; then `det(1 - uH) = F(u)^2` on the
whole disc, not just `|F|^2` on the real axis. I checked this at a complex point (numerics T2(c'),
`5e-3` with classes of length `<= 8`) and the real coefficients directly. The prover's
counterexample for general adjoint pairing (`E_1 = i = -E_2`, `1 + u^2 = |1 - iu|^2 != (1 - iu)^2`)
is right. The shard now states the general `F(u) conj(F(conj u))` form, the Kraus square, and the
counterexample. (5) T2(d): the sectors are preserved by `X -> X^*`, so the reality argument
restricts; radius `1/q`; `sdet(1 - uH) = F_gr(u)^2`; numerics T2(d), `5e-3`.

**VERDICT T2: VALID** (with the prover's radius, the real-square strengthening and the
non-Kraus counterexample, all applied).

### T2e (`obs:oriented-half-not-polynomial`)

**What I attacked.** (1) Non-polynomiality: a polynomial square (or `F F^#` with `F` polynomial)
has only even-multiplicity real roots; `(1-u)^2(1+u)(1-3u)` has simple roots at `-1` and `1/3`;
correct. (2) **The brief's twist-symmetry claim for Ad-weights was wrong**, and my first numerics
tested the wrong thing (it multiplied the terminal letter of the path, which is the prover's
endpoint-inclusive identity <1>4, not the transition weight). In the transition convention the
prover's counterexample `U_e = U_f = diag(1, i)` gives path traces `0` and `4`, neither equal nor
opposite; recomputed by hand and in numerics T2(e). The classical weights are twist symmetric
(every allowed path has weight one). The corrected statement is in the shard and in the claims
row. (3) The applicability of Aizenman--Warzel's lemma: their hypotheses are for scalar flow
matrices with exact loop-reversal invariance and twist anti-symmetry; the Ad path traces are
nonnegative, so anti-symmetry would force paired traces to vanish; the lemma does not apply, and
the two-loop bouquet shows independently that no polynomial-square theorem can hold for the
untwisted operator. The four byte-cited quotes were checked against `refs/src/` (the gate
verifies them mechanically as well).

**VERDICT T2e: VALID** (after the correction of the twist claim, applied).

### T3abc (`thm:odd-letters-chiral`)

**What I attacked.** (1) `gamma E_i gamma = eps_i E_i`: `P U_i P X U_i^* = eps_i U_i X U_i^*`; the left
factor `P` and the right factor `P` of `gamma E_i gamma (X) = P U_i (P X) U_i^*` combine as `(P U_i P) X
U_i^*`; correct. (2) The balanced-grading consequence: an odd unitary is a bijection `V_+ -> V_-`; the
brief omitted it and the prover added it, together with the remark that then `n_0 = n_1` and the
`(1 - u^2)` factors cancel. (3) The square-root formula: the lower diagonal block of `I - uH_k` in the
chiral decomposition is the identity, so the Schur complement is `I - u^2 h_k h'_k`; the sector ratio
gives the first identity and `(I - uH_k)(I + uH_k) = I - u^2 H_k^2` with evenness gives the second;
uniqueness of the normalised square-root germ; correct. (4) The Bass half-block formula: with
`c = 1 + q u^2`, `det [[c, -u a],[-u a^*, c]] = c^r det(c - u^2 c^{-1} a a^*) = det(c^2 - u^2 a a^*)`
exactly because the two blocks have equal dimension `r`; the prover is right that this is essential,
and it holds by (2). (5) The band: SVD of `a_k` gives eigenvalues `+-s_j` of `Sigma_k`; the prover's
caveat that `K_k = H_k^2|_+` need not be diagonalisable is right and matters for T3cd. Numerics T3(b) on
two all-odd families at real and complex `u`, `1e-9`.

**VERDICT T3abc: VALID** (with the balanced-grading clause, the "with both path restrictions" reading
of the two-step operator, and the non-diagonalisability caveat, all applied).

### T3cd (`prop:odd-sector-two-step`)

**What I attacked.** This is where the brief was most wrong and the prover most useful. (1) The
multiplicity correspondence `det(z - H_k) = det(z^2 - K_k)`: each sign pair of multiplicity `m` gives
one eigenvalue `mu^2` of `K_1` with multiplicity `m` (the full `H_1^2` has `2m`); recomputed; numerics
T3(c). (2) **Zeros are not "the `u` with `u^2 = 1/mu^2`"**: the order of the graded zeta at such a point
is `b_1(rho) - b_0(rho)`, and the prover's all-`X` example (four letters `X`, `P = Z`) has similar even
and odd sectors, `Z_gr = 1`, `K_1 != 0`; recomputed numerically (`Z_gr = 1` to `1e-12`). The shard
now states the order formula and the example. (3) **The circle condition versus the notebook's divisor
RH**: the prover's degree-six tensor `U_i = X (x) V_i` with `cos 2t = 3/4` has adjacency modes `+-5`
outside the band in both sectors and `Z_gr = 1`; I checked the eigenvalue arithmetic (`2 + 4 cos 2t = 5`,
`6`) by hand; the shard states the entire-sector condition and its distinction from the divisor RH.
(4) **Hilbert--Polya needs semisimplicity**: the example `U_0, U_0, U_{pi/6}, U_{pi/6}` with
`Sigma_1` eigenvalues `+-2 sqrt 3` at the band edge, `q = 3`, `det(1 - uH_1) = (1-u^2)^2(1-3u^2)^2`, and
a nontrivial Jordan block of `K_1` at `3`. I recomputed `Sigma_1 = [[0, 2 + 2 e^{i pi/3}],[c.c., 0]]`,
`|2 + 2 e^{i pi/3}| = 2 sqrt 3`, the determinant at two points and the Jordan block by the rank test
`rank(K - 3) > rank((K - 3)^2)` (numerics T3'). The prover's argument via the two-dimensional invariant
subspace `span(Sv, JSv)` with companion matrix `[[2 sqrt 3, 3],[-1, 0]]` and characteristic polynomial
`(z - sqrt 3)^2`, not scalar, is right. This refutes the brief's "iff diagonalisable" clause; the shard
now says the manifest form needs semisimplicity and gives the example. (5) T3(d): the diagonal form of
`Sigma_0` on `span(1, P)` is in the basis `(1, P)`, the off-diagonal one in `(1 +- P)`; the brief had
conflated them; the trivial divisor is by sector and multiplicity, with the fixed and anti-fixed modes
`ker(Sigma_k -+ D)` (proved via `sum ||E_i X - X||^2 = 2D||X||^2 - 2<X, Sigma X>`), and `1, P` are the
only extremal modes under irreducibility (H-IRRED); all applied.

**VERDICT T3cd: VALID** (after the four corrections, applied; the drafted "iff diagonalisable" is
refuted and replaced).

### T3ef (`obs:chirality-needs-all-odd`)

**What I attacked.** (1) The block argument `(eps_i + 1) E_i` for the failure of anticommutation with
`L_P` as soon as one letter is even; correct. (2) The prover's point that another chiral involution may
exist for mixed parities: `P = Z (x) 1`, letters `X (x) X` (odd) and `1 (x) X` (even), `Q = 1 (x) Z`
anticommutes with both and commutes with `P`; checked numerically (numerics T3'). The observation was
rewritten to say "for `L_P`". (3) The continuum: the brief said "no continuum analogue"; the prover
shows that for `sum L_i^* L_i = c 1` the generator satisfies `gamma (L + c) gamma = -(L + c)`; checked
on a random odd family with three rates (numerics T3'). This is relevant to the notebook's jump
Lindbladians (`num:graded-ramanujan`(d)) and is now the statement in the shard.

**VERDICT T3ef: VALID** (after the two corrections, applied).

### T4 (`prop:single-layer-odd`)

**What I attacked.** (1) The brief wrote `sdet(1 - uh) = 1` for an odd `h`; the prover is right that
`1 - uh` is not even for commuting `u`, so no Berezinian; the defined supertrace series is `1` and
`sdet(1 - t h^2) = 1`; the shard says exactly this. (2) T4(b): the prover proved the induction identity
directly (explicit induced matrices, the two-vertex labelled multigraph `Y` with transports
`rho(t_b^{-1} s_i t_a)`, identical Hashimoto matrices, and `Ind rho^t = Ind rho`), so H-ARTIN is not
needed; I checked the cocycle relation `k(bar i, b) = k(i, a)^{-1}` and the well-definedness of the
intertwiner `g (x) v -> g t (x) v`. The rotation-sign identity `Tr(P A B) = -Tr(P B A)` for odd `A`
explains the vanishing word sums; numerics T4 (sums at lengths 2 and 4). (3) T4(c): the brief's "the
zeros are not squares of anything on the single bond" was an undefined universal; the prover's
`X, X, Y, Y` example makes it precise: `Z_gr = (1 + 3u^2)^2/((1 - u^2)(1 - 9u^2))`, single layer
`(1 - u^2)^2 (1 - 2u^2 + 9u^4)`, no single-layer edge eigenvalue squares to `-3`, `str h^2 = 0` against
`str H^2 = 32`. All four numbers recomputed (numerics T3'/T4). Applied.

**VERDICT T4: VALID** (after the three corrections, applied).

### T5 (`obs:square-root-dictionary`)

A synthesis, not a theorem; it cites registered results of 04k/04n and this shard. I checked that every
claim in it is either a cross-reference or one of the verdicts above, and that the three-level
distinction (band, circle, manifest form) is the prover's item 2 of "three statements most useful".

**VERDICT T5: VALID** as an observation; status stays `sketched` (no independent content to prove).

## Summary

| alias | claim | verdict |
|---|---|---|
| T1ab | `prop:chiral-linearisation` | VALID |
| T1c | `prop:euler-exponent-berezinian` | VALID |
| T1d | `prop:no-super-coupling` | VALID after corrections |
| T2 | `prop:oriented-half` | VALID after corrections (radius; Kraus square; non-Kraus counterexample) |
| T2e | `obs:oriented-half-not-polynomial` | VALID after correction (twist claim) |
| T3abc | `thm:odd-letters-chiral` | VALID |
| T3cd | `prop:odd-sector-two-step` | VALID after corrections (zero order; circle vs divisor; semisimplicity) |
| T3ef | `obs:chirality-needs-all-odd` | VALID after corrections |
| T4 | `prop:single-layer-odd` | VALID after corrections |
| T5 | `obs:square-root-dictionary` | VALID (observation) |

10 VALID, 0 MINOR, 0 INVALID after the corrections; 24 rows in the prover's correction ledger, all
applied to the shard and the claims database. Independent checks: 158 in `scripts/ihara_dirac.py`.
Caveat on independence: the reviewer is the author of the brief and the numerics (TJO's instruction for
the session excluded Opus and Sonnet lanes); the prover is of the other model family.
