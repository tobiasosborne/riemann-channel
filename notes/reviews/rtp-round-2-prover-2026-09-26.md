# REFUTE review: RTP round 2, lane P (prover): bordering lemma, Baker grading, FNW exclusion, Diophantine floor

Reviewer: `claude:opus` (adversarial REFUTE lane).
Date: 2026-09-26. Subject: `notes/rtp-round-2/prover/astra-proofs.md` (author `codex:gpt-6-astra`, 2026-09-26, 643 lines,
`progress.txt` P1–P4 DONE), written against `notes/rtp-round-2/prover/astra-brief.md` and `notes/rtp-round-2/brief.md`
(orchestrator `claude:fable-5.1`). Scope: every labelled statement (P1.1–P1.4 with the exact example, P2.1–P2.4 with
H-BAKER, P3.1–P3.4, P4.1 with H-BPR/H-LOG2 and the priority/metric paragraph), the correction ledger, the numerical
checks section, and the proposed treatment of `db/claims.tsv`. Working tree as found (git not run). No lane file,
shard, database row or source was edited; only this review and the four scratch scripts below were written.

Nothing here assumes RH and no zero of zeta is used anywhere (not even in a comparison step).

## Inputs read

| file | what |
|---|---|
| `notes/rtp-round-2/prover/astra-proofs.md` | the report under review (in full) |
| `notes/rtp-round-2/prover/astra-brief.md`, `notes/rtp-round-2/brief.md` | the lane brief and round brief |
| `notes/rtp-round-2/prover/checks/{p1_p2,p3_choi,p4_bound}.{py,txt}` | the lane's checks (re-run; see below) |
| `report/sections/08i_riemann_tomography.tex` lines 1–80 | `lem:bordering-interval` as printed (status `sketched`) |
| `notes/rtp-round-1/lane-A1.md` §0–§1 | Lemma A1.1, A1.1' and proofs |
| `report/sections/08g_weil_window_extension.tex` lines 60–130 | `prop:extension-disc` and its proof |
| `notes/metric-tomography/finite-prime-language.md` (in full) | Proposition A, the quantitative remark, `L_S`, the exclusion table, §7 |
| `notes/metric-tomography/metric-as-state.md` lines 60–92, §7.1–7.3 | the organising paragraph, its correction, the contradiction pathway |
| `notes/zeta-spectral-triples/plan.md` §1.1–1.3 | Loewner data, parity blocks |
| `refs/src/2511.22755/mc2arXiv.tex` lines 380–495 | CCM: Weil class (403–409), `MF1` (436), `bombieriexplicit1bis` (445), `W_R` (450), `bombtest` (465–467), `bombtest-0` (469–471), the convolution domain (428) |
| `refs/src/coste-2002/paper.txt` lines 170–252, 745–802 | Tarski–Seidenberg (Thm 2.3 at 173, Thm 2.6 at 248), `PROJ` (757–774), Thm 2.19 (782), Thm 2.20 (799) |
| Nesterenko–Waldschmidt, arXiv:math/0002047, e-print TeX (fetched by the reviewer with `curl https://arxiv.org/e-print/math/0002047` into the session scratchpad, **not** into `refs/`) | length definition (lines 56–72), Theorem 3(1) (lines 164–168) |
| `db/claims.tsv` rows `lem:bordering-interval`, `prop:extension-disc`, `obs:prime-by-prime-blind`, `thm:weil-positivity-finite`, `prop:trace-supertrace-criterion`, `obs:factor-by-factor-limits`; `db/provenance.tsv` rows 239–244 | registration context |
| `scripts/labbook_check.py` lines 110–152, 290–315 | derived-status rule and the `VERDICT` match |
| `notes/reviews/rtp-round-1-2026-09-24.md` | format and the C1 verdict of round 1 |

## Scripts written by this review (under `notes/reviews/`; deterministic; no zeros)

| script | checks | what it does, independently of the lane |
|---|---|---|
| `scratch_rtp2_prover_p1.py` | 27 | builds the full Loewner matrix symbolically (`N = 3`, `j = 4`) and projects onto parity vectors: every `u, w, d` of P1.2 and plan.md §1.3; `N = 0` step from the `3 x 3` Loewner matrix; the exact example (`s_e`, `s_o`, both intervals, nesting, `det(5x5) = s_e s_o`, `b_ME = 0`, midpoint `9/82`, ratio `-3/sqrt337`); P1.3 condition against brute-force maximisation on 200 random quadratic pairs; a crossing example with distinct centres satisfying (P1.2); the nested-case reduction; the odd column vanishing for `b_n = kappa n`; `Delta I = 2 I_real = I_complex` |
| `scratch_rtp2_prover_p2.py` | 25 | `log q = psi(1) - (1/q) sum_{j=1}^q psi(j/q)` at 50 digits for 7 primes; `psi(1/2) = -gamma - 2 log 2`; the six kernel values of the 3-atom table from the CCM form; `A_2, A_3`, `R_fin`; P2.4 on an actual `C_c^infty` bump (`delta = 0.05`, `M = {1,2,6}`), all prime powers summed with no admissibility assumed; the regularised point mass `Q(phi_delta) = log(1/delta) - 1.95544 + O(delta)` for `delta = 1e-1 .. 1e-5` |
| `scratch_rtp2_prover_p3.py` | 30 | random unital CP maps `M_2 (x) M_d -> M_d` (`d = 2, 3`) via Stinespring isometries; stationary boundary state; Choi matrix in the report's index convention; (P4.6) against the direct FCS expectation `rho(E_A E_B(1))` (agreement `1e-17`); `tr J = d`; translation invariance; energy above Hulthén; the pinching embedding of a direct-sum auxiliary algebra into `M_d`; `k_d`, `s_d`, input-length bounds as exact integers; the Choi coordinate count `q^2 m^2` |
| `scratch_rtp2_prover_p4.py` | 15 | the CAD degree/length recurrences and their closed forms; the inequalities of steps 2, 3, 5; `H(Q) <= 2^{deg P} L(P)` on random integer factorisations; N-W Theorem 3(1) as transcribed (sanity on 24 convergents; monotonicity in the degree); `E(d)` for `d = 2, 3, 4, 8` in 100-digit and 80-digit interval arithmetic; the sharper exponent the lane's own derivation delivers |

**97 independent checks, 0 failed.** The lane's three scripts were re-run: outputs byte-identical to the committed
`p1_p2.txt`, `p3_choi.txt`, `p4_bound.txt`; they wrote no files.

---

## Verdict table

| statement | verdict | script | decisive check |
|---|---|---|---|
| P1.1 unstructured bordering, Gaussian information | **VALID** | p1 | congruence; `2I` real, `I` complex, verified |
| P1.2 normalised window bordering (`u, w, l, C`, intervals; `N = 0` step) | **VALID** | p1 | every coefficient against the symbolic Loewner matrix; odd block at `N = 0` is the scalar `a_1 - b` |
| P1.3 midpoint iff-condition (+ exact example) | **VALID** | p1 | example reproduced exactly (`-3/sqrt337 = -0.16342`); 200 random pairs; condition is not "equal centres" (crossing example) |
| P1.4 zero-column obstruction | **VALID** | p1 | even column alone forces all `b_i = 0`; odd column vanishes for `b_n = kappa n` (the report says so) |
| H-BAKER as stated | **VALID** (as a hypothesis) | — | it is the standard inhomogeneous form (Baker 1966; Theorem 2.1 of Baker's 1975 book, from memory) |
| P2.1 collapse of `L_S` | **VALID**, understated | p2 | `A` contains `log q` explicitly **and** via Gauss multiplication from rational digamma values alone |
| P2.2 logarithmic direct sum `B_S` | **VALID** | — | Q-independence by unique factorisation; H-BAKER for `Q-bar` |
| P2.3 point masses outside the Weil domain | **VALID** | p2 | CCM Weil class is a function class; `W_R` log-singular at 0; `Q(phi_delta) - log(1/delta) -> -1.95544` |
| P2.4 prime remainder on admissible bumps | **VALID** | p2 | `sum_p W_p(F) = sum_p A_p log p` on a real bump to `1e-8`; `A_2 = 2sqrt2`, `A_3 = -4/sqrt3` |
| P3.1 endpoints over a real closed subfield | **VALID** | — | standard; proof complete |
| P3.2 compact semialgebraic FCS parametrisation, attained algebraic minimum | **VALID** | p3 | (P4.6) = direct FCS energy; `tr J = d`; counts |
| P3.3 FNW exclusion and strict gap | **VALID** | — | one line from P3.2; attainment correctly not needed |
| P3.4 scope of the transposition | **VALID** | — | correct; the note's "a determinant" (line 158) is rightly removed |
| P4.1 explicit Diophantine floor | **MINOR** | p3, p4 | all arithmetic and every bound reproduced; H-LOG2 is verbatim N-W Thm 3(1); **H-HULTHEN is stated for the wrong object** (finite-ring limit vs TI infimum), and "H-BPR" is not BPR but Coste's `PROJ` theorem, already on disk |
| P4 remarks (priority, metric analogue, open inputs) | **MINOR** | — | substance right; "refuted" is the wrong label for an unsupported inference; Blakaj–Wolf not verifiable here |
| Numerical checks section | **VALID** | p1–p4 | every table entry reproduced (P1 to 30 digits, P2 exactly, P4 `E(d)` to 17 digits, rounding direction correct) |
| Correction ledger items 1–6 | **VALID** | p1, p2 | see audit below; item 2's two claims are both right |

**Tally: 15 VALID, 2 MINOR, 0 INVALID.** The report is mathematically sound. The one substantive defect is a
hypothesis mis-stated in P4.1 (and P3.3's Heisenberg paragraph); the most important finding is the lane's own:
the finite-prime language `L_S` of the future-directions note is independent of `S`. This review strengthens it:
the collapse survives the removal of "logs of algebraic numbers" from `A`.

---

## Verdicts

### P1.1 (unstructured bordering): VALID

Re-derived: `L B L^* = diag(G, s)` with `L = [[I,0],[-c^*G^{-1},1]]`, `det L = 1`; `s <= d` with equality iff
`G^{-1/2}c = 0`; `I_real = (1/2) log(det G d / det B)`, `I_complex = log(det G d / det B)`. The edge cases (`d = 0`,
`d < 0`, `s = 0 < d` giving `I = +infinity`) are correct. The multi-column version and the remark that information is
additive only across independent parity blocks are correct. The brief asked "which Gaussian is the right one here";
the report answers only implicitly ("the real symmetric matrices are the covariances meant"). All window blocks are
real symmetric (P1.2's parity basis; verified symbolically), so the real Gaussian and `Delta I = 2I` is the natural
reading; the complex reading gives `Delta I = I` on the same matrix. This is a convention, not an error: see
correction C-P1b for one sentence to add. `scratch_rtp2_prover_p1.py` §7.

VERDICT P1.1: VALID

### P1.2 (normalised window bordering): VALID

Every entry checked against the full Loewner matrix `T_nm = (b_n - b_m)/(n - m)`, `T_nn = a_n`, `a_{-n} = a_n`,
`b_{-n} = -b_n`, projected onto `e_0 = V_0`, `e_i = (V_i + V_{-i})/sqrt2`, `o_i = (V_i - V_{-i})/sqrt2` (symbolic, `N = 3`,
`j = 4`): the even/odd cross entries vanish; `(w_e)_0 = sqrt2/j`, `(u_e)_i = 2 i b_i/(i^2 - j^2)`,
`(w_e)_i = -2j/(i^2 - j^2)`, `(u_o)_i = 2 j b_i/(i^2 - j^2)`, `(w_o)_i = -2i/(i^2 - j^2)`, diagonals `a_j +- b_j/j`; this also
reproduces plan.md §1.3 and lane A1's `w_e, w_o`. `l_t = sigma_t/j - 2 w_t^T G_t^{-1} c_t`, `C_t = w_t^T G_t^{-1} w_t > 0` and
the completed square are right. The `N = 0` correction is right and is a real defect of the shard's wording: from the
`3 x 3` Loewner matrix, the new odd block is the scalar `a_1 - b` (no old odd space), so `C_o = 0` and the odd admissible
set is a half-line, not an interval with a centre. The report's added case split (`s_t* < 0` empty, `= 0` singleton,
`> 0` interval) is necessary because RH is not assumed: nothing in the lemma guarantees a nonempty interval. For the
certified zeta windows nonemptiness holds whenever the enlarged window is certified positive definite (the truth is
then interior). `scratch_rtp2_prover_p1.py` §1–2.

VERDICT P1.2: VALID

### P1.3 (midpoint iff-condition) and the exact example: VALID

(P1.2) is exactly "the derivative of `log s_e + log s_o` vanishes at `m`", multiplied by `s_e(m) s_o(m) > 0`; strict
concavity from `(log s)'' = -2C/s - (s'/s)^2 < 0` makes the stationary point unique. Checked against brute-force
maximisation on 200 random rational quadratic pairs. Two remarks the report does not make but should (C-P1c): in the
**nested** case `J = I_e` (as in the example) one has `m = beta_e*` and (P1.2) reduces to `beta_e* = beta_o*`; in the
**crossing** case (P1.2) does **not** reduce to equal centres: `s_e = 4 - (b-1)^2`, `s_o = 4 - (b+1)^2` have centres
`+1, -1`, `J = [-1, 1]`, and the joint maximiser is the midpoint `0`.

Example reproduced exactly: `s_e = 1 + b/2 - 41b^2/18`, `s_o = 1 - b/2 - 4b^2/9`, `det(5x5 Loewner) = s_e s_o` (with
`G_e = I_2`, `G_o = [1]`), `I_e = [(9 - 3sqrt337)/82, (9 + 3sqrt337)/82]` strictly inside
`I_o = [(-9 - 3sqrt73)/16, (-9 + 3sqrt73)/16]`, `(log s_e s_o)'(0) = 0`, offset `-9/82`, ratio
`-3/sqrt337 = -0.163420413210852990787760114410`. `scratch_rtp2_prover_p1.py` §3–5.

VERDICT P1.3: VALID

### P1.4 (zero-column obstruction): VALID

`c_{e,0} = sqrt2 b_j/j` forces `b_j = 0`, then `2 i b_i/(i^2 - j^2) = 0` forces `b_i = 0`. The report's caveat is correct and
matters for the shard's (iii): the **odd** old-to-new column alone vanishes for the nonzero data `b_n = kappa n`
(checked, `N = 4`, `kappa = 3/7`), so (iii) must speak of the even column or the pair. `scratch_rtp2_prover_p1.py` §6.

VERDICT P1.4: VALID

### H-BAKER: VALID as a named hypothesis

The stated form (logarithms of algebraic numbers that are Q-independent, together with 1, are `Q-bar`-independent) is
Baker's 1966 theorem in its standard inhomogeneous form (Theorem 2.1 of *Transcendental Number Theory*, 1975; from the
reviewer's memory, to be byte-cited like the report says). The report's parenthetical gloss ("combining independence
of algebraic logarithms with transcendence of every nonzero algebraic linear form") is loose but harmless.

VERDICT H-BAKER: VALID

### P2.1 (collapse of `L_S`): VALID, and understated

The note defines `A` (finite-prime-language.md lines 85–86) to contain "`log` of algebraic numbers"; every prime `q`
is algebraic, so `log q in A` and `L_S = L_empty`. The table row at line 116 ("`log q` provably outside `L_S` (Baker)")
and the inference at lines 151–152 are false as written. The report's second point is stronger than it states. It
shows `log 2` in the span of `gamma` and `psi(1/2)`, and concludes that deleting the explicit logarithms "does not repair
this particular archimedean list". In fact **every** `log q` lies in the `Q`-span of rational digamma values alone, by
Gauss's multiplication formula `psi(qx) = log q + (1/q) sum_{k=0}^{q-1} psi(x + k/q)` at `x = 1/q`:

    log q = psi(1) - (1/q) sum_{j=1}^{q} psi(j/q)        (q >= 2 any integer).

Verified at 50 digits for `q = 2, 3, 5, 7, 11, 13, 97` (`scratch_rtp2_prover_p2.py` §1). So any `A` that contains
`psi(r)` for all rational `r` makes `L_S` independent of `S`; the only way to rescue a place-by-place grading is to
drop the rational-argument digamma values (and the logarithms), which removes exactly what the archimedean factor
produces. The `log pi` remark (line 119 treats `log pi` as in `A`, lines 85–86 do not list it) is correct.

VERDICT P2.1: VALID

### P2.2 (the logarithmic direct sum `B_S`): VALID

Q-independence of `i pi, log p` (imaginary parts, then unique factorisation) and H-BAKER give `Q-bar`-independence of
`1, i pi, log p`. Uniqueness of coordinates, the filtration and `B_S cap B_T = B_{S cap T}` follow. The warning that a
formal provenance sum `A_formal (+) (+)_p Q-bar [p]` is not injective under evaluation is correct and is the right
diagnosis of the note's mistake.

VERDICT P2.2: VALID

### P2.3 (point masses are not test functions of the Weil distribution): VALID

This is the second question put to this review, and the answer is yes, in the CCM normalisation.
(a) The Weil class (`mc2arXiv.tex:403–409`) consists of functions that are piecewise C^1 with first-kind
discontinuities and the stated decay. The form `QW(f, g) = Psi(f^* * g)` (`:465–467`) is applied only to
convolutions of square-integrable compactly supported functions (`:428`). A finitely supported measure is in
neither class.
(b) `W_R(F) = (log 4pi + gamma)F(1) + int_1^infty (F(x) + F(1/x) - 2x^{-1/2}F(1)) x^{1/2}/(x - x^{-1}) d*x` (`:450`). In the
log variable its kernel is `rho(y) = e^{y/2}/(e^y - e^{-y}) ~ 1/(2y)`, so `W_R` needs `F` continuous (Dini) at the origin.
For `mu = sum c_n delta_{log n}`, `F = mu^* * mu` has the atom `sum |c_n|^2` at the origin, so `F(1)` is undefined.
`W_p(F) = log p sum_m p^{-m/2}(F(p^m) + F(p^{-m}))` (`:445`) evaluates `F` pointwise, which is undefined at atoms sitting on
prime powers.
(c) Regularisation diverges. With the report's `L^2`-normalised bumps, `scratch_rtp2_prover_p2.py` §5 gives
`Q(phi_delta) = log(1/delta) - 1.95544 + O(delta)` for `delta = 1e-1 ... 1e-5`, with successive differences shrinking
tenfold per decade. With the literal point-mass (`L^1`) normalisation `F` scales by `1/delta`: the divergence becomes
`delta^{-1} log(1/delta)` and the prime evaluations also diverge like `1/delta`.
The algebraic kernel values `2cosh(D/2) = sqrt r + 1/sqrt r` and `rho(D) = sqrt r/(r - 1/r)` are right (six table
entries checked), and so is the statement that they carry no extra factor `D`. One precision the report leaves
implicit: for distinct atoms whose ratio is not a prime power, the off-diagonal pairing (pole plus archimedean at
`D != 0`) *is* well defined. The obstruction is the diagonal and the prime-power ratios, which is what the proof
says.

VERDICT P2.3: VALID

### P2.4 (prime remainder on admissible bumps): VALID

`F(k log p) = sum_{n/m = p^k} conj(c_m) c_n R_delta(0)`, with `R_delta(0) = ||phi||_2^2 = 1`, and the mirrored term gives
`A_p(c)`. The prime of a prime-power ratio of `S`-smooth integers lies in `S`. On an actual `C_c^infty` bump
(`delta = 0.05`, `M = {1, 2, 6}`, `c = (1, 2, -1)`), with all prime powers `<= 6 e^{0.1}` summed and no admissibility
assumed, `sum_p W_p(F) = 2sqrt2 log 2 - (4/sqrt3) log 3` to `1e-8`, and `R_fin = 0.57662011545316152531774764290813`
(`scratch_rtp2_prover_p2.py` §3–4). The statement is correct. It is close to a tautology (`R_fin` is `-sum W_p` by
definition); its content is (i) exact localisation under admissibility, (ii) algebraic coefficients, (iii) uniqueness
under H-BAKER. The relation to the filtration is inclusion, not identity: the support of the coordinate vector is
contained in the prime content of `M` (the primes `p` with some `n/m` a power of `p`) and may be smaller by
cancellation. The report says so, but then calls it "agrees with the filtration of metric-as-state.md:73–89". Lines
73–89 are the corrected single-place paragraph, not a definition of a filtration. See C-P2.4 for the wording and for
the row's kind (proposition, not theorem).

VERDICT P2.4: VALID

### P3.1 (endpoints over a real closed subfield): VALID

After quantifier elimination with parameters in `F` (H-TS), `Y` is a Boolean combination of sign conditions on
`P_i in F[t]`. Real roots of `P_i` lie in `F`, because `F` is real closed and `F(alpha) subset R` is an ordered algebraic
extension. Membership is constant on the components of the complement of the root set, so boundary points (hence
finite inf and sup) lie in `F`. Complete. (C-P3 shows that H-TS can be bypassed altogether with the `PROJ` argument
of P4.)

VERDICT P3.1: VALID

### P3.2 (compact semialgebraic FCS parametrisation): VALID

Checked:
- Structure. The finite list of algebra types is right. A map between direct sums is CP iff every block `E_ab` is
  CP (compose with the `*`-homomorphic inclusions and projections).
- PSD criterion. PSD iff all principal minors are `>= 0`, proved via `det(tI + J)`.
- Equation counts. Unitality gives `m` real linear equations. Stationarity `sum_a E_{ab,1}^dagger(rho_a) = rho_b` is
  exactly `rho o E_1 = rho` and gives `m` real bilinear equations.
- FCS formula. `omega = rho(E_{A_1} ... E_{A_t}(1))` is the FNW formula.
- Compactness. `sum_b tr J_ab = n_a`.
- Nonemptiness. Product channels, for which any `rho` is stationary.

Numerically (`scratch_rtp2_prover_p3.py`): for random unital CP maps `M_2 (x) M_d -> M_d` (`d = 2, 3`), the energy
polynomial (P4.6) in the report's Choi index convention equals the direct FCS expectation to `4e-17`; `tr J = d`;
`omega(A (x) I) = omega(I (x) A)`; energies lie above `1/4 - log 2`. The parameter count `sum_{a,b}(q n_a n_b)^2 = q^2 m^2`
holds on five tuples. The distinction between auxiliary-algebra dimension and matrix bond dimension is correct and
needed.

VERDICT P3.2: VALID

### P3.3 (FNW exclusion and strict gap): VALID

Correct as stated ("if `e_0 = inf_{TI states} omega(h)` is transcendental ..."). Attainment is correctly noted as not
needed. The counterexample `h = |1><1|` with transcendental individual energies is right. For Heisenberg, the
transcendence input is Hermite–Lindemann (`log 2` is transcendental), which is weaker than both H-BAKER and H-LOG2; cite
that one. The H-HULTHEN paragraph that follows is not part of P3.3's statement; its defect is treated under P4.1.

VERDICT P3.3: VALID

### P3.4 (scope of the transposition): VALID

A definable optimum of a semialgebraic function over a semialgebraic set defined over `F` lies in `F`; individual
values do not. This correctly removes "a determinant, a signature-weighted trace" from finite-prime-language.md line
158: a determinant of one member of a class with transcendental parameters is not algebraic. The exclusions
(transcendental coefficients, entropy/log-det objectives, infinitely many constraints) are right. Note that the
MaxEnt objective of the tomography programme is a log-det: P3.4 does not apply to the MaxEnt *value*. It does apply
to the MaxEnt *point* on a finite window, because the maximiser of a determinant (a polynomial) over a semialgebraic
set is definable.

VERDICT P3.4: VALID

### P4.1 (explicit Diophantine floor): MINOR

What was re-checked and holds:
- **CAD envelope.** It is derived from Coste's `PROJ` (`paper.txt:757–774`: coefficients, `PSRC_j(P, dP/dX_n)`,
  `PSRC_j(P_i, P_k)`, recursive truncations) and Thm 2.19–2.20 (`:782–800`). Degree recurrence
  `delta_{i+1} = 2 delta_i^2` (Sylvester–Habicht minors of size `<= 2 delta_i` with entries of total degree
  `<= delta_i`), closed form `(2 delta)^{2^i}/2`. Length recurrence, and the per-step inequality
  `log2((2x)!) + 2x log2 x <= 6x^2` (checked `x <= 2000`). `h_i <= delta_i(h_0/delta + 3i)`. Factor height
  `H(Q) <= 2^{deg P} L(P)` via Mahler measure. The final "parenthesis `<= tau + 4k + 1`" (grid-checked). Every step is
  right.
- **H-LOG2 is verbatim.** Nesterenko–Waldschmidt, arXiv:math/0002047, e-print `main.tex` lines 164–168: "Let `xi` be
  a real algebraic number with `d = deg xi`, `L(xi) <= L` and `L >= 3`. Then
  `|log 2 - xi| >= exp{-151000 d^2 (log L + d log d)(1 + log d)^{-1}}`", with `L(alpha)` the length of the minimal
  polynomial in `Z[x]` (lines 56–72). Replacing `d` by `D` is legitimate, since the exponent increases in `d`
  (checked). `L = (D + 1)H >= L(alpha)`.
- **Counts and heights.** `k_d = 4d^4 + d^2 + 1`, `delta_d = 2d^2`, `s_d = 2^{2d^2} + 2^d + 2d^2`, `tau_d = 32d^4`. The
  input lengths `2^M M!`, `2d + 1`, `8d^2 + 2` and `64d^5 + 5` are all `< 2^{tau_d}` as exact integers. (P4.6) matches
  the FCS energy (P3.2 above).
- **Decimal step.** `log(D + 1) + D log D <= D^2` for `D >= 4`, and `151000((tau + 1) log 2 + 1) <= 200000(tau + 2)`.
- **Values.** `E(d)` reproduced to 17 digits for `d = 2, 3, 4, 8`, with relative interval width `3e-81`. The displayed
  exponents are rounded up, which is the conservative direction.
- **Embedding.** The pinching embedding of `(+)_a M_{n_a}` into `M_d` preserves all local expectations (checked on a
  classical example).

Defects (all fixable by wording; none changes a number):
1. **H-HULTHEN names the wrong object.** The proof uses `e_d >= e_0` with `e_0 = inf_{TI states} omega(h)` (P3.3). What
   Hulthén (and the byte quotes already in `db/provenance.tsv` rows `prov:franchini17-eafm`,
   `prov:ssnt03-hulthen`) gives is the thermodynamic limit of the ground energy per site of finite rings. Equating the
   two is a standard lemma, but it is a separate step and must be stated. The short proof is in C-P4a.
2. **"H-BPR" is a misnomer and not an external input.** The envelope uses only the correctness of Coste's `PROJ`
   (Thm 2.19–2.20), which is on disk and byte-citable. It uses no BPR theorem and no big-O constant. The hypothesis
   should be renamed and discharged by a citation (C-P4b).
3. **Looser than the lane's own derivation.** `D = (2 s delta)^{2^{k+1}}` is much weaker than the
   `deg alpha <= delta_{k-1} = (2 delta)^{2^{k-1}}/2`, `log2 H <= delta_{k-1}(tau + 4k + 1)` that step 3 actually proves.
   With the latter, `log10 C <= 1.07e21, 8.17e100, 6.38e313, 1.59e4952` for `d = 2, 3, 4, 8`, against the reported
   `E(d) = 1.72e22, 1.95e102, 2.16e315, 1.44e4954` (`scratch_rtp2_prover_p4.py` §4). This is optional; the reported bound
   is valid.

VERDICT P4.1: MINOR

### P4 remarks (priority; metric analogue; open inputs): MINOR

Correct:
- Labelling priority OPEN instead of asserting "first". The note's "nobody appears to have written it down" is
  unverified.
- "Irrationality of an ordinate is insufficient for P3's exclusion, because algebraic irrational optima are allowed".
  This is the most useful correction in the section.
- A metric exclusion needs an optimal definable invariant of a specified finite class, identified with a number
  outside the coefficient field.

Wrong label: the report says the note's claim that "any one of these would give the first metric-exclusion theorem"
(finite-prime-language.md lines 162–163, 230–232) "is refuted in that unqualified form". Nothing is refuted. The
inference is unsupported (a non sequitur): no counterexample is exhibited, and the claim could still come true for
some class. Use "unsupported; SHARPENED" (C-P4c).

Not verified by this review: the Blakaj–Wolf citation (LMP 114 (2024) 28). The DOI resolver redirects to a Springer
login, and the arXiv API was unreachable from this session. It is only a priority pointer, but it must not enter a
`cited` row unverified.

VERDICT P4-remarks: MINOR

### Numerical checks section: VALID

- **P1 table.** All six rows reproduced exactly (`scratch_rtp2_prover_p1.py`).
- **P2 table.** `A_2 = 2sqrt2`, `A_3 = -4/sqrt3`, no term for the ratio 6; pole kernels `3sqrt2/2`, `4sqrt3/3`,
  `7sqrt6/6`; `rho` values `2sqrt2/3`, `3sqrt3/8`, `6sqrt6/35`; `R_fin = 0.576620115453161525317747642908...`.
- **P3 check.** Superseded by the reviewer's random-CP test.
- **P4 tables.** All reproduced.

The lane's scripts re-run byte-identically.

VERDICT N: VALID

---

## Audit of the correction ledger

| item | claim | verdict |
|---|---|---|
| 1 | Gaussian log-det needs PD; `log(d/s)` is a deficit relative to max-det, not a "gain"; `N = 0` odd block affine; empty/singleton intervals | **right** (all four) |
| 2a | `A` contains `log q` for every prime `q`, so `L_S` is independent of `S` | **right**; true twice over (explicit logs; Gauss multiplication from rational `psi` values alone) |
| 2b | a point mass is not a test function for the Weil distribution in the CCM normalisation | **right** (Weil class `:403–409`; atom of `F` at the origin against the log-singular `W_R`; pointwise prime evaluation; regularisation diverges as `log(1/delta)`, or as `delta^{-1} log(1/delta)` with `L^1` normalisation) |
| 3 | semialgebraic statements on finite parameters and finite marginals; algebra dimension vs bond dimension; individual energies not algebraic | **right** |
| 4 | numerical bounds need numerical constants; "first" unverified; irrationality insufficient | **right** |
| 5 | Coste (2002) is a local TS/CAD source | **right**; moreover `db/provenance.tsv` already holds `prov:coste02-ts-second` / `-third` (used_by `cit:tarski-seidenberg`, which has no claims row yet). Their line numbers (178–180, 258–260) do not match this machine's `paper.txt` (173–175, 248–250); re-check on registration |
| 6 | `bombtest` is at `mc2arXiv.tex:465–467`, not 385–388 | **right**; the same stale "lines 385–388" is in `notes/zeta-spectral-triples/plan.md:49` and `notes/rtp-round-2/brief.md` |

VERDICT ledger: VALID

---

## Corrections to apply

**C-P1a (shard 08i, replacement text for `lem:bordering-interval`).** Replace the lemma body (lines 34–46) by:

> Let $G_K$ be positive definite and border it by a column $c$ and diagonal $d$; write $s = d-c^*G_K^{-1}c$.
> (i) The bordered matrix is positive semidefinite iff $s\ge0$, positive definite iff $s>0$, and its determinant is
> $\det G_K\,s$; for fixed $d>0$ the unique maximum-determinant completion is $c=0$, and on positive definite
> completions the log-determinant deficit of the true column relative to it, $\varDelta I=\log(d/s)\ge0$, is twice the
> mutual information of the real centred Gaussian with this covariance (once the mutual information of the circular
> complex Gaussian); the window blocks are real symmetric, and the real reading is used. (ii) In the window form, for
> $N\ge1$, the bordering $|n|\le N\to N+1$ adds one even and one odd basis vector whose columns and diagonals are affine
> in the single new datum $b_{N+1}$ once $a_{N+1}$ is given; each block's Schur complement is a strictly concave
> quadratic $s_t(\beta)=s_t^*-C_t(\beta-\beta_t^*)^2$, so each block's admissible set is empty ($s_t^*<0$), a point
> ($s_t^*=0$), or an interval centred at that block's maximum-determinant value whose endpoints are the singular
> enlargements; the joint admissible set is the intersection. When it has interior, the joint maximum-determinant
> point (the maximiser of $s_es_o$) is unique and equals the centre $m$ of the intersection iff
> $C_e(m-\beta_e^*)s_o(m)+C_o(m-\beta_o^*)s_e(m)=0$; for nested intervals this is $\beta_e^*=\beta_o^*$, and it fails
> in general (exact rational example: offset $-3/\sqrt{337}$ half-widths). At $N=0$ the odd block is the scalar
> $a_1-b_1$ and its admissible set is a half-line. (iii) The even old-to-new column (hence the pair of parity columns)
> vanishes iff $b_1=\dots=b_{N+1}=0$; the odd column alone vanishes for $b_n=\kappa n$.

Replace the proof line by: "Proof: `notes/rtp-round-2/prover/astra-proofs.md`, Theorems P1.1–P1.4 (reviewed,
`notes/reviews/rtp-round-2-prover-2026-09-26.md`, alias P1)." The parenthetical "(offsets of 0.3 half-widths at small
N)" is a numerical observation of the round-1 review (`-0.30, +0.30, -0.29` at `(x, N) = (13,10), (25,20), (50,50)`). It
must leave the proved lemma: move it to `num:rtp-dilation-channel` or to a remark citing
`notes/reviews/scratch_rtp1_axisN.py`.

**C-P1a' (`db/claims.tsv`, row `lem:bordering-interval`).**
- **deps.** Set to `-`. The current dependency `prop:extension-disc` (sketched) is an analogy, not a logical input.
  Under `labbook_check.py:derive` it would force the derived status to `sketched` even after the upgrade.
- **proof.** `notes/rtp-round-2/prover/astra-proofs.md`.
- **review.** This file.
- **note.** `review-alias=P1; reviewer=claude:opus`.
- **statement.** Summarise C-P1a, including "for `N >= 1`" and "deficit".

**C-P1b (report, P1.1, one sentence after the complex case).** "All window blocks are real symmetric; the notebook
uses the real Gaussian, `Delta I = 2I`."

**C-P1c (report, P1.3, after the proof).** "If one interval contains the other, `m` is the inner centre and (P1.2)
reduces to `beta_e* = beta_o*`. For crossing intervals (P1.2) does not reduce to equal centres: `s_e = 4 - (b - 1)^2`,
`s_o = 4 - (b + 1)^2` have the midpoint `0` of `J = [-1, 1]` as joint maximiser."

**C-P2.1 (report, P2.1, replace "Thus even deleting ... does not repair this particular archimedean list.").** "Gauss's
multiplication formula gives `log q = psi(1) - (1/q) sum_{j=1}^q psi(j/q)` for every integer `q >= 2`. So every `log q`
lies in the `Q`-span of rational-argument digamma values, and `L_S` stays independent of `S` even after the logarithms
of algebraic numbers are deleted from `A`."

**C-P2.1' (finite-prime-language.md).**
- **Table row, line 116.** Replace with "`log q`, `q` any prime | inside `A` (by definition, and via
  `psi(j/q)` by Gauss multiplication); `L_S` does not depend on `S` | the Baker grading is a statement about
  `B_S` = span(1, i pi, log p : p in S), not about `L_S`".
- **Lines 151–152.** Replace the Baker sentence by a reference to P2.4 (operational blindness to foreign comb weights).
- **Line 158.** Delete "a determinant, a signature-weighted trace" (P3.4).
- **Lines 105–107.** Delete "(in particular the discrete/point-mass test class)" (P2.3).

**C-P2.4 (report, P2.4, and the proposed row).**
- **Kind.** Make it a proposition: `prop:baker-prime-remainder`, not `thm:`.
- **Wording.** Replace "It agrees with the arithmetic prime-content filtration of `metric-as-state.md:73–89` for the
  finite-place remainder" by: "The support of the coordinate vector `(-A_p(c))_p` is contained in the prime content
  of `M`, the primes `p` for which some ratio `n/m` of elements of `M` is a power of `p`; the inclusion is strict
  exactly when the `A_p(c)` cancel."

**C-P4a (report, H-HULTHEN; also P3.3's last paragraph).** State it as: "H-HULTHEN. For
`h = S.S (x) S.S`-per-bond, `S = sigma/2`, `lim_{N -> infinity} E_0(N)/N = 1/4 - log 2`, with `E_0(N)` the ground
energy of the `N`-site ring (byte quotes: `prov:franchini17-eafm`, `prov:ssnt03-hulthen`)." Then add:

> **Lemma.** For finite-range TI `h`, `inf_{TI states} omega(h) = lim_N E_0(N)/N`.
>
> **Proof.**
> 1. (`>=`) Restrict a TI state to `N + ell` consecutive sites. Its energy on the open chain of `N` bonds is
>    `>= E_0^{open}(N)`, and `E_0^{open}(N) >= E_0(N + ell) - c` with a constant `c = O(ell ||h||)` (close the ring;
>    `||h||` bounds the missing bonds). Divide by `N`.
> 2. (`<=`) Take the periodically extended ring ground states, average over translations, and take a weak-* limit
>    point. The result is a TI state whose energy density is the limit.

Without this lemma P4.1's inequality `e_d >= e_0` is not connected to the cited value.

**C-P4b (report, P4).**
- **Rename.** Rename "H-BPR" to "the CAD projection theorem (Coste 2002, Thm 2.19–2.20, with `PROJ` as defined at
  `refs/src/coste-2002/paper.txt:757–774`)". Drop the BPR Theorem 14.16 pointer from the hypothesis list; it is not
  used.
- **P3.1 without H-TS.** The same argument makes P3.1 independent of the coefficient-field form of H-TS. Every
  polynomial in `PROJ` has coefficients that are integer polynomial expressions in the input coefficients. With
  inputs in `F = Q-bar cap R`, the final univariate polynomials therefore lie in `F[t]`, and their real roots lie in
  `F`.
- **Byte-citation.** Byte-cite H-LOG2 from the e-print by fetching it into `refs/src/math/0002047/` (TeX, one file,
  gzip). The quote is lines 164–168 of the single `.tex`.
- **Optional.** Report the sharper `deg alpha <= delta_{k-1}`, `log2 H <= delta_{k-1}(tau + 4k + 1)` exponents
  alongside.

**C-P4c (report, "Priority and the metric analogue").** Replace "is therefore refuted in that unqualified form" by "is
unsupported in that unqualified form (SHARPENED): transcendence, or membership outside the coefficient field, of an
optimal definable invariant of a specified finite class is needed, not irrationality of a listed constant." Mark the
Blakaj–Wolf reference "not byte-checked".

**C-misc.**
- `notes/zeta-spectral-triples/plan.md:49` and `notes/rtp-round-2/brief.md`: "lines 385–388" → "lines 465–467".
- `db/claims.tsv` row `prop:extension-disc`: add the conjugate, `c_K = -conj((W_K^{-1} w)_0)/(W_K^{-1})_{00}`, as in the
  shard (verified: the row still omits it).

---

## Recommendation for shard 08j

Registration rule used: a `proved` row needs a `VERDICT <alias>: VALID` line here (`labbook_check.py:310`) and deps
whose derived status is proved or cited. A `-conditional` status needs an `assumed` dependency row.

| row | kind | recommended status | alias | conditions before registering |
|---|---|---|---|---|
| `lem:bordering-interval` | lemma | **proved** (upgrade from sketched) | P1 | apply C-P1a and C-P1a' (text, deps `-`, proof/review/note columns; remove the 0.3 half-width parenthetical) |
| `prop:loewner-midpoint-condition` | proposition | **fold into the lemma** (C-P1a already states it); if kept separate: proved | P1.3 | none beyond C-P1c |
| `obs:finite-prime-language-collapse` | observation | **proved** | P2.1 | use the strengthened statement (C-P2.1): independent of `S` even without the logarithms in `A` |
| `prop:atomic-weil-domain-obstruction` | proposition | **proved** | P2.3 | deps: the existing CCM citation row(s) for `bombtest`/`W_R` |
| `prop:baker-prime-remainder` (proposed as `thm:`) | proposition | **proved-conditional** | P2.4 | new `asm:h-baker` (assumed) unless Baker is byte-cited; wording C-P2.4 |
| `prop:finite-bond-semialgebraic-optimum` | proposition | **proved** with `cit:tarski-seidenberg` (provenance rows exist; add the claims row, re-check the line numbers) plus the `PROJ` citation, or **proved-conditional** on `asm:h-ts` | P3.2 | covers P3.1, P3.2, P3.4 |
| `thm:fnw-transcendental-exclusion` | theorem | **proved** (general form: hypothesis "`e_0` transcendental" is part of the statement); Heisenberg instance needs `cit:hulthen-energy` (claims row missing; provenance rows exist) + the TI-infimum lemma of C-P4a + Lindemann | P3.3 | C-P4a for the Heisenberg sentence |
| `thm:diophantine-heisenberg-floor` | theorem | **sketched** until C-P4a/C-P4b are applied and re-reviewed; then proved-conditional on `asm:h-log2` (or proved with a `cit:` row once N-W is in `refs/src`) | P4.1 (MINOR) | C-P4a, C-P4b |
| `num:diophantine-heisenberg-floor` | numerical | **numerical** | N | cite `notes/rtp-round-2/prover/checks/p4_bound.py` and this review's `scratch_rtp2_prover_p4.py` |
| priority of P4 | — | **no row**; OPEN | — | — |
| `prop:extension-disc` | proposition | unchanged (sketched) | — | sync the conjugate (C-misc) |
| `obs:prime-by-prime-blind` | observation | unchanged (sketched) | — | do not upgrade from P2 |
| `thm:weil-positivity-finite`, `prop:trace-supertrace-criterion`, `obs:factor-by-factor-limits` | — | unchanged | — | — |

The future-directions note (`finite-prime-language.md`) should keep Proposition A (now P3.2–P3.3) and replace §3's
grading by `B_S` with P2.4. Its §7 item 3 is done in corrected form (P2.2 + P2.4). Item 2 is done conditionally
(P4.1). Item 4's "any one unlocks" becomes the sharpened requirement of C-P4c.

## Verdict lines

VERDICT P1.1: VALID

VERDICT P1.2: VALID

VERDICT P1.3: VALID

VERDICT P1.4: VALID

VERDICT P1: VALID (the lemma `lem:bordering-interval` in the replacement wording C-P1a; not the current shard wording)

VERDICT H-BAKER: VALID

VERDICT P2.1: VALID

VERDICT P2.2: VALID

VERDICT P2.3: VALID

VERDICT P2.4: VALID

VERDICT P3.1: VALID

VERDICT P3.2: VALID

VERDICT P3.3: VALID

VERDICT P3.4: VALID

VERDICT P4.1: MINOR — H-HULTHEN must be stated as the finite-ring limit together with the lemma identifying it with the TI infimum (C-P4a); "H-BPR" is Coste's `PROJ` theorem and should be cited as such (C-P4b). No number changes.

VERDICT P4-remarks: MINOR — "refuted" should read "unsupported (SHARPENED)"; Blakaj–Wolf not byte-checked (C-P4c).

VERDICT N: VALID

VERDICT ledger: VALID
