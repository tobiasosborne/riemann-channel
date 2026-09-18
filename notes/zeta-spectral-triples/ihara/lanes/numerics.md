# Ihara-zeta spectral triples: numerics lane

Sidequest of 2026-09-18, numerics lane. Prototype: `notes/zeta-spectral-triples/ihara/ihara_proto.py`
(numpy + sympy + mpmath, deterministic, 21 s from the repo root). Captured default run:
`notes/zeta-spectral-triples/ihara/run_ihara_proto.txt` (1470 lines, `all checks PASS`).
Options: `--graph NAME`, `--M m`, `--Mmax m`, `--dps d`. Nothing here is a registered lab-book claim.

Model for the write-up and for the code: `notes/zeta-spectral-triples/ccm_proto.py` and
`notes/zeta-spectral-triples/plan.md` §1, §5.1, §6.4. Sources: CCM arXiv:2511.22755
(`refs/src/2511.22755/mc2arXiv.tex`, Lemma `basics`, Def. `even-simple`, Lemma `key`, eq. `eq:detDp`)
and Connes-van Suijlekom (`refs/src/2511.23257/Araki-final-oct25.tex`, Lemma `basics-general`,
Lemma `key-general`, Prop. `prop:finmain`).

## 0. Summary in five lines

1. The discrete construction works, and at the **critical window** `K = R + 1` it recovers the
   nontrivial Hashimoto divisor **exactly** (to working precision) for every Ramanujan object tried.
2. The CCM perturbed operator has an exact discrete analogue, but **not** with `eta = ` all-ones.
   Two variants reproduce Lemma `key` verbatim: the multiplicative one (`D` = shift, `eta` = delta at
   the window edge), which is a companion matrix and a `(tau - eps)`-**isometry**; and the additive
   one on **Cayley nodes** `lambda_n = tan(pi n/K)` with `eta_n = (-1)^n sec(pi n/K)`, which is
   `(tau - eps)`-**self-adjoint** and returns the angles through `theta = 2 arctan s`.
3. The reality statement is **free** in the discrete case: for an arbitrary real even Toeplitz `T`
   the minimal eigenvector's polynomial has all `2M` roots on `|z| = 1` (Pisarenko; verified on 200
   random `T`). So the analogue of CCM's theorem is not where the difficulty is.
4. Everything that can fail is controlled by **positivity**, i.e. by the graph Riemann hypothesis:
   an off-circle reciprocal pair makes the **odd** block negative and leaves the even block PSD, so
   `eps_M < 0`, `xi_min` becomes odd, CCM's `even-simple` fails, and with it the entire additive
   family (`<eta|xi> = 0` because `eta` is even and `xi` is odd).
5. Two objects break the construction in ways worth reporting: non-Ramanujan graphs (the minimal
   eigenvector stops being the Caratheodory-Fejer kernel vector and the off-circle points are never
   returned) and irregular graphs (no functional equation, so the two-sided extension of the trace
   sequence is not the Weil form of the divisor at all).

## 1. Conventions, and the two-sided extension question

`(q+1)`-regular graph `G`, `B` the Hashimoto operator on directed edges,
`B[(a->b),(b->c)] = 1` iff `c != a`; `N_k = Tr B^k`; critical radius `critr = sqrt q`.
Trivial divisor: one copy of `{q, 1}` from `lambda = q+1`, one copy of `{-q,-1}` if bipartite, and
`+-1` with multiplicity `|E|-|V|` each. Retained multiset `A` = the rest; `R = #` **distinct**
points of `A`. `t^nt_k = N_k q^{-k/2} - (trivial part)` for `k >= 0`, extended by `t_{-k} = t_k`.
Window `{-M..M}`, `K = 2M+1`, Weil form `T_{jj'} = t^nt_{j-j'}` (lags `0..2M`; the Lemma-key
identity below also needs `t_{2M+1}`, i.e. `N_1..N_{2M+1}`).

**The subtlety the task asks about.** Three candidate two-sided extensions coincide here:

| extension | definition | status |
|---|---|---|
| even | `t_{-k} := t_k` | what the code uses |
| Hermitian (shard 08b `def:rescaled-trace-sequence`) | `nu_{-k} := conj(nu_k)` | equal to the even one, because `A` is closed under conjugation, so `nu_k` is real (checked: `max |Im t_k| = 0`) |
| literal | `sum_{mu in A} (mu/critr)^k` for `k < 0` | equal to the even one **iff** `A` is closed under `mu -> q/mu` |

The last is the functional equation, and for a regular graph it is automatic: the two roots of
`mu^2 - lambda mu + q` multiply to `q`. Verified for every regular object to `<= 7.7e-38` at 40 digits (and exactly `0` for
`K_{3,3}` and the Pauli curve). So with the even extension
`t^nt_k = sum_{mu in A} (mu/critr)^{|k|} = sum_{mu in A} (mu/critr)^{k}` for all `k in Z`.

The **trivial** part is where the conventions genuinely differ, and this is the trap. The pair
`{q, 1}` is reciprocal-closed (`q * 1 = q = critr^2`) so its even extension is its literal sum. The
`|E|-|V|` copies of `+-1` are **not**: their literal continuation to `k < 0` is
`(+-1)^{|k|} q^{|k|/2}`, which grows, whereas the even extension is `(+-1)^{k} q^{-|k|/2}`. One must
subtract the **even extension** of the trivial part from the **even extension** of `t_k`; doing it
any other way destroys the identity `t^nt_k = sum_A (mu/critr)^{|k|}`, which the code checks both
ways (exact integer `Tr B^k` route vs direct sum over `A`, agreement `< 2.2e-36` at 40 digits).

For irregular graphs the functional equation fails outright (dumbbell: `max_k |diff| = 123` over lags `|k| <= 22`), and
for a graph with a tail the retained divisor contains `mu = 0`, so `mu -> critr^2/mu` is not even
defined. See §6.

## 2. Identity checks (all PASS)

Per object: Ihara-Bass `det(1-uB) = (1-u^2)^{|E|-|V|} det(I - Au + Qu^2)` at three seeded random
complex `u` (`<= 1.5e-15` relative); `N_k = Tr B^k` against a direct enumeration of closed
non-backtracking cyclic walks, `k <= 7`; `N_k = sum_{d|k} d * #{prime cycles of length d}`;
`spec(B)` against the Ihara-Bass prediction (`<= 5.8e-15`); `t^nt` by the trace route vs the direct
divisor sum; `spec(T) = spec(even block) u spec(odd block)` (Cantoni-Butler); the four displacement
ranks of §4; both halves of Lemma `key` (i); Lemma `key` (ii).

## 3. Regimes: `eps_M`, kernel dimension, accuracy

`pt.err` = max over the `R` distinct retained points `z = mu/critr` of the distance to the nearest
root of `xi-hat`; `ang.err` = the same restricted to the points on the circle, in angle. `xi` is the
global minimal eigenvector, `xi_ker` the eigenvector of the eigenvalue nearest `0`, `xi_even` the
minimal eigenvector of the even block. Full tables in the run log.

### Ramanujan objects (K4, Q3, Petersen, K_{3,3}, Heawood, Pappus, necklace2, necklace3, Pauli)

| object | `R` | critical `M` | `eps` at `M_crit - 1` | `ang.err` there | `eps` at `M_crit` | `ang.err` at `M_crit` | kernel dim at `M_crit + 1` |
|---|---|---|---|---|---|---|---|
| K4 | 2 | 1 | (K=1) | - | `-1.4e-40` | `0` | 3 |
| K_{3,3} | 2 | 1 | (K=1) | - | `-1.8e-40` | `0` | 3 |
| Pauli (graded, `q=5`) | 2 | 1 | (K=1) | - | `+2.7e-41` | `0` | 3 |
| Q3 (cube, bipartite) | 4 | 2 | `3.0` | `3.6e-1` | `-4.1e-40` | `0` | 3 |
| Petersen | 4 | 2 | `9.4476568` | `6.1e-1` | `+9.5e-41` | `0` | 3 |
| Heawood (bipartite) | 4 | 2 | `12.0` | `5.2e-1` | `-9.2e-40` | `0` | 3 |
| Pappus | 6 | 3 | `4.661334` | `5.2e-1` | `-4.9e-40` | `0` | 3 |
| necklace2 | 8 | 4 | `1.965774` | `3.5e-1` | `-2.6e-40` | `0` | 3 |
| necklace3 | 8 | 4 | `2.9357842` | `2.6e-1` | `-9.1e-40` | `0` | 3 |

So, exactly as §5.1 of `plan.md` predicted:

- **under-resolved** `K < R`: `T > 0`, `eps_M > 0` and strictly decreasing in `M`, `xi` even and
  unique, all `2M` roots on the unit circle but at the wrong angles. Accuracy improves roughly
  geometrically: Petersen `6.1e-1` at `K = 3`; Pappus `6.6e-1, 5.2e-1` at `K = 3, 5`;
  necklace3 `1.32, 5.7e-1, 2.6e-1` at `K = 3, 5, 7`.
- **critical** `K = R + 1`: `eps_M = 0` (`|eps| < 1e-39` at 40 digits), kernel one-dimensional,
  `xi` even and unique up to scale, and the `2M = R` roots of `xi-hat` are the `R` retained points
  **exactly** (`ang.err = pt.err = 0.000e+00`, i.e. below `1e-38`). This is Caratheodory-Fejer /
  Prony, and multiplicity is irrelevant: Petersen's adjacency eigenvalue `1` has multiplicity 5 and
  `-2` multiplicity 4, but `R = 4` distinct Hashimoto points and the critical window is `K = 5`.
  Heawood needs `K = 5` although its retained multiset has 24 elements.
- **over-resolved** `K > R + 1`: kernel dimension `K - R` (`3, 5, 7, 9` at `M = M_crit+1 .. +4`),
  so `eps_M` is **not simple** and CCM's `even-simple` fails. The eigensolver returns an arbitrary
  kernel vector, which is neither even nor odd (`par(xi) = MIXED`). The recovery is still exact in
  the sense that every retained point is a root of `xi-hat` for *every* kernel vector
  (`pt.err = 0`), but `xi-hat` also has `K - 1 - R` spurious roots, which is why the count in the
  log reads e.g. `4/8` roots on the circle for Petersen at `M = 4`.

### Non-Ramanujan

`necklace6` = six copies of `K4` minus an edge joined in a cycle, 24 vertices, cubic, connected,
`max|lambda_nontrivial| = 2.86619826 > 2 sqrt 2 = 2.82842712`. `R = 20`, of which 18 on the circle
and one real reciprocal pair `mu = 1.66498945, 1.201208812` (`|mu|/critr = 1.177, 0.849`).
`twok4` = two disjoint copies of `K4`: the second Perron eigenvalue `q+1 = 3` is retained, so the
retained divisor contains `{q, 1}/sqrt q = {sqrt 2, 1/sqrt 2}`; `R = 4`, minimal and fully
controlled.

| M | K | `eps_M` (necklace6) | `eps_even` | `eps_odd` | `par(xi)` | `ang.err(xi)` | `ang.err(even)` | `pt.err(ker)` |
|---|---|---|---|---|---|---|---|---|
| 5 | 11 | `+0.62866519` | `+0.6286652` | `4.186883` | even | `2.5e-1` | `2.5e-1` | `2.5e-1` |
| 6 | 13 | `-8.2570321` | `+0.1827774` | `-8.257032` | **odd** | `1.4e-1` | `1.9e-1` | `1.9e-1` |
| 9 | 19 | `-89.053093` | `+0.005199` | `-89.05309` | odd | `1.5e-1` | `1.3e-1` | `1.3e-1` |
| 10 | 21 | `-139.13215` | `-4.5e-40` | `-139.1321` | odd | `1.3e-1` | `0.000e+00` | `0.000e+00` |
| 14 | 29 | `-624.42314` | `-1.7e-38` | `-624.4231` | odd | `8.3e-2` | `0.000e+00` | `0.000e+00` |

and `twok4`: `eps_M = -2.673, -7.679, -21.48, -52.78, -111.06, -240.05` at `M = 2..7`, growing like
`critr^{2M} * (r^2)^M` with `r = |mu|/critr`; `eps_even = O(1e-40)` throughout; `xi_min` odd from
`M = 2` on; `pt.err(xi_min) = 4.142e-1 = sqrt 2 - 1` at every `M >= 2`, i.e. the off-circle point is
never returned, while `pt.err(xi_ker) = 0` at every `M >= M_crit`.

**What this says.** The Caratheodory-Fejer content survives: the *kernel* vector of `T` still
recovers the whole divisor exactly once `K > R`, off-circle points included. What breaks is CCM's
**prescription**, which takes the *minimal* eigenvector. Under RH (Ramanujan) `T >= 0` and the two
coincide; when RH fails they are different vectors, `eps_M < 0`, and the minimal eigenvector lives
in the odd block, where the form is negative. The roots of `xi_min-hat` are then still all on the
unit circle (§4) and therefore cannot be the true divisor.

The parity mechanism is exact and is worth quoting. With `B(f,g) = sum_{mu in A} f-hat(mu/critr)
g-hat(critr/mu)`, a reciprocal pair `{x, 1/x}` off the circle contributes `2 f-hat(x) f-hat(1/x)`,
which for `gamma f = f` (palindromic `f-hat`, so `f-hat(1/z) = f-hat(z)`) is `2 f-hat(x)^2 >= 0` and
for `gamma f = -f` is `-2 f-hat(x)^2 <= 0`. The probe `offcircle_block_probe` in the prototype
confirms it on a bare pair: for `x = +-1.2, +-1.6` and `M = 1..5` the even block is exactly PSD with
a kernel and the odd block carries the whole negative eigenvalue. This is the finite form of
`prop:weil-orbit-negative` in shard 08b, read in the `gamma`-grading.

**Consequence worth stating to the theory lane:** in the discrete case CCM's hypothesis
`even-simple` is not a technical nuisance, it is (equivalent to, or at least implied by) the
Riemann hypothesis for the object. `eps_M < 0` and `xi_min` odd happen precisely when the divisor
has an off-circle pair.

### Irregular graphs (no single `q`)

Stark-Terras: `R_G = 1/rho(B)`; the prototype takes `critr = sqrt(rho(B))`, the geometric mean of
the trivial pair `{rho(B), 1}` (`u = 1` is always a zero of `det(I - Au + Qu^2)`, since
`I - A + Q = D - A = L`), plus `+-1` with multiplicity `|E|-|V|`.

- `tri_pendant` (triangle with a pendant path). `rho(B) = 1`, `critr = 1`. `B` has a 4-fold zero
  eigenvalue (the tail), which is retained and contributes `4 * delta_{k0}`, i.e. `eps_M = 4`
  exactly at every `M`. `tau - eps` is the rank-2 form of the triangle, so the two circle points are
  recovered exactly at every `M >= 1` (`ang.err = 0`), and the four points at `mu = 0` are never
  recovered (`pt.err >= 1` at `M = 1`, decreasing only because spurious roots wander near the
  origin). The pendant is invisible to `Z_G` and the construction correctly sees only the 2-core;
  the price is that the retained divisor is not reciprocal-closed, so `t^nt` is not a two-sided
  divisor sum at all.
- `dumbbell` (two triangles joined by an edge, degrees 2 and 3). Functional equation **fails**
  (`max_k |diff| = 123` over the lags used). All 8 distinct retained points lie off the circle, moduli
  `|mu|/critr in [0.86, 1.13]`. `eps_M = 4.84, 2.42, 0.331, -0.169, -1.86, ..., -31.8` at
  `M = 1..10`: positive at first, then negative. `pt.err` **saturates**: `1.18, 0.345, 0.165` at
  `M = 1,2,3` and then stops improving, `0.178, 0.191, 0.197, 0.199, 0.203, 0.204, 0.208`. The
  construction cannot converge, because its output is always `2M` points on the unit circle
  (§4) and the truth is not on any circle. This is the cleanest negative control in the set:
  *the construction is structurally incapable of returning an irregular graph's divisor.*

### Graded case (Pauli qubit / elliptic curve over `F_5`)

`Z(u) = (1 + 2u + 5u^2)/((1-u)(1-5u))`, `q = 5`, numerator roots `alpha = -1 +- 2i`, `|alpha| =
sqrt 5`. Ring norms `N_n = 1 + q^n - sum alpha^n = 8, 32, 104, 640, 3208, 15392` (`N_1 = 8`, i.e.
`a_5 = -2`, matches `prop:qubit-graded-zeta` in `report/sections/03c_graded_ramanujan.tex`). The
sign-flipped Weil form is `t^nt_k = q^{k/2} + q^{-k/2} - N_k q^{-k/2}` = (trivial) - (rings), which
is exactly `sum over zeros`; cross-checked against the direct sum to `3.9e-40`. `R = 2`, critical
window `K = 3`, and the two zero angles `+-2.034443936` are recovered exactly at `M = 1`, with
`eps_1 = 2.7e-41`, `xi` even and simple, and all Lemma-key checks passing. So the graded sign
bookkeeping goes through unchanged: the only difference from the graph case is which side of the
zeta the retained divisor comes from.

## 4. The perturbed operator: which variant is CCM's Lemma `key`

Notation: `gamma` = reversal `j -> -j`; `S` = forward shift (nilpotent) on the window, `Z` = cyclic
shift; `F` the unitary DFT on `Z_K`, `tau = F T F^*`, `z_n = e^{2 pi i n/K}`, `n = -M..M`;
`tau_q = tau - eps`; `xi-hat(z) = sum_j xi_j z^j`, `P(z) = z^M xi-hat(z)` of degree `2M`.

**Displacement structure** (all verified, third singular value `< 1e-14`):

| matrix | rank | meaning |
|---|---|---|
| `T - Z T Z^*` and `Z^* T Z - T` | 2 | Toeplitz displacement, supported on one row and column at a window edge |
| `(z_n - z_m) tau_nm` | 2 | multiplicative Loewner in the DFT basis |
| `(tan(pi n/K) - tan(pi m/K)) tau_nm` | 2 | **additive** Loewner for the Cayley nodes |
| `(2 pi n/K - 2 pi m/K) tau_nm` | **3** for `M >= 2` | the linear nodes are *not* Loewner nodes |

The last row is the structural reason variant (b) of the task cannot work. The anti-Hermitian
rank-two matrix `H_nm = (lambda_n - lambda_m) tau_nm` is `|beta><eta| - |eta><beta|`, and `eta` is
**not** free: it is read off from `H`. The prototype measures the distance of a candidate `eta` to
`span(beta, eta)`: all-ones sits at distance `0.82-0.98`, while `(-1)^n sec(pi n/K)` sits at
distance `<= 4e-16`.

The seven variants, at the critical window (numbers from Heawood, `M = 2`; every Ramanujan object
gives the same pattern). `T-selfadj` = `||tau_q D' - (tau_q D')^*|| / ||tau_q D'||`; `T-isometry` =
`||D'^* tau_q D' - tau_q|| / ||tau_q||`; `spec vs roots` = max distance from the expected image of
the roots of `xi-hat` to `spec(D'')`; `ang.err` vs the true Hashimoto angles.

| tag | `D` | `eta` | `T`-selfadj | `T`-isometry | spec vs roots | ang.err |
|---|---|---|---|---|---|---|
| a1 | `S` (shift) | delta at window edge `j = +M` | `1.7` | **`2.4e-41`** | **`1.5e-15`** | **`8.9e-16`** |
| a2 | `Z` (cyclic) | same | `1.7` | **`2.4e-41`** | **`1.5e-15`** | **`8.9e-16`** |
| a3 | `Z` | all-ones, position basis (task (a)) | `1.6` | `0.64` | `0.42` | `0.42` |
| b | `diag(2 pi n/K)` in DFT | all-ones in DFT (task (b)) | `1.1` | `3.4` | `0.72` | n/a (4 complex) |
| c1 | `diag(tan(pi n/K))` in DFT | all-ones in DFT (CvS `prop:finmain` literally) | `1.3` | `4.2` | `0.42` | `0.52` |
| c2 | `diag(tan(pi n/K))` in DFT | `(-1)^n sec(pi n/K)` (from the displacement) | **`4.8e-41`** | `1.4` | **`2.0e-15`** | **`1.3e-15`** |
| d | `Z` = `diag(z_n)` in DFT | all-ones in DFT | `1.6` | `0.80` | `0.89` | n/a |

**a1 = a2 exactly.** With `<eta|xi> = xi_M = 1` the wrap term of the cyclic shift cancels:
`Z' = Z - |Z xi><eta| = S - |S xi><eta| = S'`. And `S'` is precisely the **companion matrix** of
`P(z)`: in the identification `e_j <-> z^{M+j}`, `S'` is multiplication by `z` modulo `P`. Hence
`S' xi = 0` and
`Det(S'' - s) = +- s^M xi-hat(s)`, which is CCM eq. `eq:detDp` with `Det(D-s)` replaced by
`(-s)^K`. Lemma `key` (i) also holds in the form `tau_q S xi = -beta`, `beta_j = t_{M+1-j}` --
note it needs the lag `t_{2M+1}`, one beyond the window; it holds in the critical and over-resolved
regimes and fails in the under-resolved one (`relative residual 0.2 - 1.6`), where the conclusion
nevertheless still holds, so (i) is sufficient but not necessary here.

Lemma `key` (ii) becomes **isometry**, not self-adjointness: `S'^T tau_q S' = tau_q` exactly. Proof
(two lines, independent of positivity and of the functional equation): extend the bilinear form
`B(f,g) = f^T T g` to the window `{-M..M+1}`; then `S' f = z f - lead(f) * z P` and
`B~(zP, zg) = B(P, g) = (tau_q xi) . g = 0`. So the only hypothesis is `tau_q xi = 0`, which is
automatic for the minimal eigenvector. Since `tau_q >= 0` always (it is `tau` minus its own minimum)
this makes `S''` a **unitary** on the quotient Hilbert space whenever `eps` is simple, hence

> all `2M` roots of `xi-hat` lie on the unit circle.

This is the discrete analogue of CCM's reality theorem, and it is **free**: the prototype verifies
it on 200 random real even Toeplitz matrices with no positivity and no divisor behind them
(`max ||root| - 1| = 6.1e-13` in double), together with the isometry (`2.4e-14`). Classically this
is Pisarenko's theorem; here it means the "spectrum is real" half of the CCM package is not the
difficulty in the discrete case.

**c2 is the faithful transcription of CCM/CvS Lemma `key`.** The nodes must be the Cayley images
`lambda_n = tan(theta_n / 2)`, `theta_n = 2 pi n/K`, which are simple, real and satisfy
`lambda_{-n} = -lambda_n` as CvS `basics-general` requires; the displacement is then rank two with
`eta_n = (1 - i tan(pi n/K)) z_n^{-M} = (-1)^n / cos(pi n/K)`. With that `eta`:
`tau_q D - D tau_q = |beta><eta| - |eta><beta|` with `beta = -tau_q D xi` (residual `2.7e-41`),
`<beta|xi> = 0` (`1.3e-41`), `tau_q D'` is Hermitian (`5.4e-41`), and
`Det(D'' - s) = const * R(s)`, `R(s) = sum_j xi_j (1+is)^{M+j} (1-is)^{M-j}`, whose roots are the
Cayley images `s = -i(z-1)/(z+1)` of the roots of `xi-hat`. So `theta = 2 arctan s` returns the
Hashimoto angles to `1.3e-15`. Derivation of the constant: `R` interpolates
`sqrt K e^{-iM theta_n} cos^{-2M}(theta_n/2) c_n` at the nodes and `Det(D-s) <eta|(D-s)^{-1} xi>`
interpolates `conj(eta_n) c_n W'(lambda_n)` with
`W'(lambda_n) = (-1)^M K cos(M theta_n) cos^{-2M}(theta_n/2)`; the ratio is
`(-1)^M sqrt K (1+i lambda_n) e^{iM theta_n} cos(M theta_n) = (-1)^M sqrt K`, a constant, because
`2M = K-1` forces `e^{2iM theta_n} = e^{-i theta_n}`.

**c1 is CvS `prop:finmain` taken literally** (`eta =` all-ones). Its determinant is the interpolant
of `c_n W'(lambda_n)`, which differs from `R` by the `n`-dependent factor `cos(M theta_n)`. The
roots are still real (Lemma `key` does not care whether `eta` is the right vector for
*self-adjointness* once `tau_q >= 0`: measured `T-selfadj = 1.3`, so in fact they are real for the
other reason, the Pisarenko fact above), but they are the **wrong** reals: `ang.err = 0.52` at the
critical window where the truth is recoverable exactly. So the paper's `prop:finmain` does not
apply verbatim to the Toeplitz form, for two independent reasons: `tau` is complex Hermitian rather
than real symmetric in the DFT basis, and the displacement vector is not all-ones.

**a3 is the task's variant (a), and it is degenerate in an instructive way.** With
`eta = ` all-ones in the **position** basis, `<eta|xi> = xi-hat(1)` and
`Det(Z'' - s) = +- (s^K - 1)/(s - 1)` *independently of `xi`*: the spectrum is the set of nontrivial
`K`-th roots of unity. Checked to `1e-15` at every window. That `eta` transports no information at
all. (For K4 at `M = 1` this predicts `ang.err = |2 pi/3 - 1.932163| = 0.162`, which is exactly what
the log prints.)

**d** (multiplicative with `eta` = all-ones in the DFT basis, i.e. `sqrt K` times the delta at the
*centre* `j = 0` of the window) gives the interpolant of `xi-hat(z_n)/z_n`, i.e. the polynomial with
the coefficients of `xi` cyclically rotated by one: wrong roots, `ang.err = 0.89`.

**When `xi` is odd the whole additive family dies.** `eta` is `gamma`-even in every additive variant
(all-ones, `(-1)^n sec`), so `<eta|xi> = 0` and the normalisation `<eta|xi> = 1` is impossible.
This is exactly what happens for the non-Ramanujan objects (necklace6 from `M = 6`, twok4 from
`M = 2`): the log shows `a3, b, c1, c2, d` all reporting `<eta|xi> = 0, no normalisation`, while
`a1/a2` survive because their `eta` (delta at a window edge) is not a parity eigenvector. Repeating
the variant table with the minimal **even**-block eigenvector, which is what CCM actually
diagonalise, restores everything: at necklace6 `M = 10` (critical) `a1/a2` and `c2` return all 20
retained points to `2.7e-15` and `1.7e-14`, including the two off the circle (they show up as
`2/20` eigenvalues off the unit circle, resp. off the real axis) -- but `eps_even = 0` is then not
the minimum of the form, `tau - eps_even` is indefinite, and `c2`'s self-adjointness is
self-adjointness for a Krein form, so reality is lost exactly where it should be.

## 5. Precision

`Tr B^k` is computed exactly in integer arithmetic, so the only cancellation is
`t^nt_k = N_k q^{-k/2} - q^{k/2} - ...`, about `q^{k/2}/R` (for a cubic graph with `M = 14`,
`2^{14}/20 ~ 800`, under 3 digits). Everything downstream runs at `mp.dps = 40`.

The double-precision probe (`precision_probe`, printed per object) compares the float64 Toeplitz
eigenproblem with the mpmath one:

- `eps_M` agrees to `<= 2.3e-13` absolute everywhere, including `eps_M ~ -624` for necklace6.
  **Double is sufficient for `eps_M` in every case tried.**
- The roots agree to `<= 7e-15` whenever the kernel is simple (under-resolved and critical
  windows).
- The roots differ by `O(1)` in every **over-resolved** window (e.g. Petersen `M = 3,4,5`:
  `7.2e-1, 7.1e-1, 1.2`). This is **not** a precision failure: the kernel has dimension `K - R > 1`
  and the two eigensolvers return different kernel vectors, whose spurious roots differ. Both still
  contain the true divisor.
- The one thing double genuinely cannot do is certify `eps_M = 0`. At the critical window
  `cond(T) ~ 1e16 - 1e18` and float64 returns `eps_M ~ +-1e-15` with an arbitrary sign; mpmath at
  40 digits returns `~1e-40`. Distinguishing "exactly zero, so the window resolves a Ramanujan
  divisor" from "small and negative, so the graph is not Ramanujan" is a precision question, and a
  graph with `lambda_2` just above `2 sqrt q` would need `eps_M` resolved below
  `(lambda_2/(2 sqrt q))^{2M}`-ish. That is the argument for doing this in arb.

## 6. What failed, and surprises

1. **Neither of the two variants the task proposed works.** (a) is `xi`-independent; (b) fails
   already at the structure level, because `(theta_n - theta_m) tau_nm` has rank 3. The two that
   work were found by reading `eta` off the displacement rather than positing it.
2. **`eta` is not all-ones.** In CCM's own setting `eta = sum_n V_n` because the Loewner nodes are
   `lambda_n = n`, for which `(b_n - b_m)` really is `|b><1| - |1><b|`. On `Z` the corresponding
   nodes are `tan(pi n/K)` and the second displacement vector is `(-1)^n sec(pi n/K)`. Getting this
   wrong costs an `O(1)` error in the recovered angles at a window where the answer is otherwise
   exact.
3. **Reality is free.** The Pisarenko fact makes CCM's hardest-looking finite-dimensional output
   (real spectrum for every window) automatic in the discrete case. Correspondingly it carries no
   information: for the irregular dumbbell the construction returns `2M` points on the unit circle
   at every window although nothing in the true divisor is within `0.13` of the circle.
4. **Positivity, not reality, is the whole content.** `eps_M >= 0` for all `M` iff the retained
   divisor is on the circle (`thm:weil-positivity-finite`), and the failure is a *parity* failure:
   off-circle pairs are negative on the odd block and PSD on the even block. That is why
   `even-simple` and RH are the same hypothesis here.
5. **`even-simple` fails in the over-resolved regime too**, for a different and benign reason:
   the kernel becomes `(K-R)`-dimensional. CCM's normalisation `<eta|xi> = 1` can then fail outright
   (`xi_M = 0` was hit for Heawood and Pauli at `M >= 2`; the prototype reports and skips).
   The right discrete statement is that `even-simple` holds **exactly at** `K = R+1`, which is the
   Caratheodory-Fejer window.
6. **Surprise:** the multiplicative variant is exactly a companion matrix, so the "spectral triple"
   here is nothing but the Frobenius/companion form of the secular polynomial, and the CCM inner
   product `tau - eps` is precisely the one that makes it unitary. That is the discrete shadow of
   the notebook's "side B is a scalar times a unitary on its nontrivial part".
7. **Surprise:** for a disconnected regular graph the second Perron eigenvalue is retained and
   produces an off-circle reciprocal pair `{sqrt q, 1/sqrt q}` at angle `0`, which makes `twok4` the
   minimal fully-controlled non-Ramanujan test (critical window `K = 5`). Worth keeping as a unit
   test for any C implementation.

## 7. Questions for the theory lane

1. Is "minimal eigenvector of a real even Toeplitz matrix has all zeros of `xi-hat` on `|z| = 1`"
   (Pisarenko) the exact discrete analogue of CCM Theorem `finmain`, or does the continuous
   statement have content that the discrete one loses? The discrete proof uses only shift
   invariance of the bilinear form plus `(tau - eps) xi = 0`; what is the continuous counterpart of
   `B~(zP, zg) = B(P, g)`, i.e. of using the lag `t_{2M+1}` one step outside the window?
2. Is `even-simple` **equivalent** to the graph RH, or only implied by it? Numerically: off-circle
   pair `=>` odd block negative `=>` `even-simple` fails. Conversely, can `even-simple` fail for a
   Ramanujan graph (other than through the over-resolved kernel degeneracy)? If the equivalence
   holds, CCM's hypothesis is not an auxiliary technical assumption but a restatement of the target.
3. The Cayley nodes `tan(pi n/K)` with `eta_n = (-1)^n sec(pi n/K)`: is this a special case of a
   CvS-type theorem with a general `eta` read off from the displacement, i.e. does Lemma
   `key-general` hold with `|beta><eta| - |eta><beta|` for an arbitrary pair rather than
   `eta = sum_i e_i`? The prototype verifies (i), (ii) and (iii) in that generality for every window
   with `gamma xi = xi`; a clean statement would cover both the zeta and the graph case at once.
4. Multiplicative versus additive: the multiplicative Lemma key needs no parity at all (`a1/a2`
   work for odd `xi`), the additive one needs `gamma xi = xi` twice over (for `<eta|xi> != 0` and
   for `<beta|xi> = 0`). Is the parity hypothesis in CCM avoidable by working with a unitary `U'`
   and a Cayley transform at the end?
5. Under-resolution. The accuracy at `K < R` is the graph analogue of the paper's `lambda`-limited
   regime, on an object where the truth is known. Empirically the angle error falls roughly
   geometrically in `M` (necklace3: `1.32, 0.57, 0.26`), and the minimiser is the degree-`2M`
   polynomial of unit coefficient norm minimising `sum_mu |xi-hat(mu/critr)|^2` -- a discrete
   prolate/Slepian problem. Is `1 - chi_4(lambda)` (CCM §7) the continuous limit of this rate?
6. `eps_M` for the dumbbell changes sign at `M = 4` and `pt.err` saturates at `0.20`. Is there a
   sharp statement of the form "the construction converges iff the retained divisor is
   reciprocal-closed", i.e. is the functional equation a *necessary* input, as shard 08b's
   `thm:weil-duality-pairing` suggests?
7. What should the trivial divisor of an irregular graph be? The choice here
   (`{rho(B), 1}` plus `+-1^{|E|-|V|}`, `critr = sqrt(rho(B))`) is the naive Stark-Terras one and
   leaves a retained divisor that is neither reciprocal- nor circle-closed. Is there a choice that
   restores a functional equation (e.g. weighting by a Perron eigenvector, or passing to the
   universal cover's spectral radius)?
