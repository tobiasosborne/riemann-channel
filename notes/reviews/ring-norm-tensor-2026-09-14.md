REVIEWER: claude:opus-5

# Adversarial review of `notes/ring-norm-tensor/astra-proofs.md`

Date: 2026-09-14. Stance: REFUTE — the reviewer's job was to find a reason each
proposition fails, and to default to INVALID under uncertainty. Target:
`notes/ring-norm-tensor/astra-proofs.md` (1184 lines, author `codex:gpt-6-astra`), brief
`notes/ring-norm-tensor/astra-brief.md`. Cross-check material:
`notes/ring-norm-tensor/sources.md` (byte-cited arXiv TeX, author `claude:opus-5`),
`notes/ring-norm-tensor/numerics.md` + `scripts/ring_norm_tensor.py` +
`outputs/ring_norm_tensor.txt` (independent numerics lane),
`notes/ring-norm-tensor/scratch/{weil_ring_norm_check,genus2_followup,t04_cutrank,t43_check,t45a_certificate}.py`,
`report/sections/{02f,04f,06b}*.tex`, `scripts/cmps_parity_supertrace.py`.

**Outcome of the refutation attempt: it failed.** Thirty-one labelled statements, four
observations and a thirty-six-item correction ledger were checked by hand and by
independent numerics; **no INVALID verdict was reached.** Every disputed constant, sign,
index convention, threshold and spectrum reproduces. The central corrections the brief
asked me to attack — ledger item 18 (`Tr(sum A (x) conj A) = sum |Tr A|^2`, and the
falsity of the drafted `sum_odd |mu|^2 <= 2 Tr(E_++) Tr(E_--)`), the repaired T3.2/T3.3
genus bound, the T4.3 closed form, and the T4.5a rational contraction certificate — are
all correct, and none over-corrects.

Two MAJOR issues remain, both about *what the notebook may record*, not about the algebra:
the open/closed status of T0.4's boundedness question, and the lab-book status of H-TWIST.

---

## 1. Issues

No BLOCKER issues.

### MAJ-1 — T0.4 declares open a question that has a one-line positive answer; the table as printed suggests the opposite answer
*Location:* T0.4 Statement + `<1>4`; Status line; correction-ledger item 5; Conjecture T0.C.
*Severity:* MAJOR (the brief asked precisely "stating whether it is bounded"; the file's
answer is "open here", and its table alone reads as evidence for *unbounded*).

*What is wrong.* T0.4's ranks `2,4,8,16,8,4,2` at `n = 8` are correct — I reproduced the
whole table, byte for byte including the moduli and the generators `beta`, by running the
author's own kernel (`notes/ring-norm-tensor/scratch/t04_cutrank.py`). But they are an
artefact of the basis prescription ("the first `beta` in the enumeration order of
`artin_schreier_mps.py` whose conjugate matrix has full rank"). In a **self-dual** normal
basis the answer is bounded, uniformly in `n`, and provably so:

In a normal basis `{beta^{2^i}}`, `Tr(x^3) = Tr(x·x^2) = sum_{i,j} x_i x_j c_{j+1-i}` with
`c_k = Tr(beta^{1+2^k})`. Self-duality is exactly `c_k = delta_{k,0}`, so
`Tr(x^3) = sum_i x_i x_{i-1}`: a **cyclic nearest-neighbour** form. Its polar matrix across
a contiguous cut has `F_2`-rank at most 2 (the two boundary bonds), so the cut rank is at
most `4 = D^2` with `D = 2` — for every `n`, matching T0.3's sharp `D^2` bound.

*Mitigating check I ran* (`notes/reviews/scratch_rnt_t04sd.py`): searching for genuine
self-dual normal bases of `F_{2^n}/F_2` and recomputing the author's own cut ranks:

```
n=3:  beta=(0,0,1)              cut ranks [2, 2]
n=5:  beta=(1,0,1,0,1)          cut ranks [2, 4, 4, 2]
n=6:  beta=(0,0,0,0,0,1)        cut ranks [2, 4, 4, 4, 2]
n=7:  beta=(0,0,1,0,1,0,1)      cut ranks [2, 4, 4, 4, 4, 2]
n=9 : [2,4,4,4,4,4,4,2]   n=10: [2,4,4,4,4,4,4,4,2]   n=11: [2,4,4,4,4,4,4,4,4,2]
n=4, n=8: no self-dual normal basis over F_2 (exists only for n odd or n = 2 mod 4)
```

The author's `n = 7` row is `2,4,8,8,4,2`; the self-dual row is `2,4,4,4,4,2`. The growth is
entirely basis noise. This also independently confirms the numerics lane
(`numerics.md`, verdict row "T0(b) ... consistent **only in a self-dual normal basis**").
*Fix:* add a self-dual-normal-basis row to the T0.4 table and the one-paragraph proof above;
change the Status line to "bounded (by 4) in a self-dual normal basis for `n` odd or
`n = 2 mod 4`; basis-dependent in general", and reword ledger item 5 accordingly. The
conjecture T0.C is unaffected (it already quantifies over a basis prescription), but its
motivation becomes much stronger: the quadratic case is *provably* bounded in the right
basis, which is what makes a dichotomy plausible.

### MAJ-2 — H-TWIST is imported as a settled "finite-bond input"; every theorem in the shard it cites carries `claimstatus ... sketched-conditional`
*Location:* Hypothesis register, **H-TWIST**; Status lines of T1.3, T4.3, T4.5a, T4.6, T5.2;
ledger item 17; source `report/sections/04f_cmps_twisted_supertrace.tex`.
*Severity:* MAJOR (bookkeeping; it decides what may be promoted in the lab book).

*What is wrong.* H-TWIST is stated as two things glued together:
```
||Psi_P(n)||^2  =  str_Gamma E^n  =  sum_{s_1..s_n} |Tr(P A_{s_1} ... A_{s_n})|^2
```
The **second** equality is unconditional and two lines long:
`E^n = sum_w A_w (x) conj(A_w)` and `Tr((P (x) conj P)(A_w (x) conj A_w)) = |Tr(P A_w)|^2`.
The **first** equality — that this is the Hilbert norm of the physical periodic-fermion ring
state — is the content of `thm:cmps-twisted-supertrace` in shard 04f, and
`grep claimstatus report/sections/04f_cmps_twisted_supertrace.tex` shows that *every*
theorem and proposition in that shard is `sketched-conditional`
(`prop:cmps-graded-parity`, `thm:cmps-twisted-supertrace`, `prop:cmps-twist-translation`,
`thm:cmps-sdet`). The file's phrase "the supplied finite-bond physical norm/supertrace
identification" reads as if it were proved.
*Fix:* split H-TWIST into **H-TWIST-ALG** (the supertrace/word identity, proved-here in two
lines — the author should simply prove it, it costs nothing) and **H-TWIST-PHYS** (the Fock-space
identification, `sketched-conditional` per shard 04f, numerically corroborated). Then T4.3 and
T4.5a are unconditional matrix-and-ring-norm theorems modulo only H-FROB, and only their
*physical* reading inherits `sketched-conditional`.
*Mitigating checks I ran.* I verified the algebraic half directly for a mixed even/odd `1|2`
tensor with 2 even + 2 odd species (`scratch_rnt_t44.py`): `str E^n` and
`sum_w |Tr(P A_w)|^2` agree to 1e-10 for `n = 1..5`. And I verified the *physical* half for the
certified T4.5a tensor against the explicit Jordan–Wigner Fock vector of
`scripts/cmps_parity_supertrace.py` (`scratch_rnt_t45a.py`):
`||Psi_P||^2 = 31, 117, 619, 3318` for `n = 2,3,4,5`, agreeing with `N_n` to `<= 5e-13`, with
periodic-translation residual `<= 1.3e-14`. So H-TWIST is *right*; it is merely not `proved`
in this notebook.

---

### MINOR issues, in descending order of consequence

**m1 — H-DEG is worded so that T1.6's derivation looks circular, and the fix is a two-way split.**
*Location:* register **H-DEG**; T1.1 `<1>1`; T1.6 hypotheses and `<1>2`–`<1>3`.
H-DEG is quoted verbatim from the brief as "...`[Lambda : pi Lambda] = |pi|^2 = N(pi)`, and
degree is preserved under good reduction, **so `|pi|^2 = deg(Frobenius) = q`**". The final
clause *is* RH for elliptic curves. T1.6's hypothesis line says "No RH inequality in H-HASSE
or H-WEIL is used", which is literally true, but a reader will ask whether `|pi|^2 = q` was
assumed. The author's `<1>2` in fact gives the honest lifting derivation (the map on the
universal cover is `z |-> pi z`; its oriented area ratio is `|pi|^2`; that equals the covering
degree, which is preserved under good reduction, and `deg(Frobenius) = q` has no RH content).
*Fix:* split H-DEG into **H-DEG-GEO** (`[Lambda : pi Lambda] = |pi|^2 = N_{K/Q}(pi)`, pure
lattice geometry) and **H-DEG-ARITH** (`deg(Frobenius) = q`, and degree is preserved under
good reduction). Then T1.6 derives `|pi|^2 = q` rather than restating it, and the sentence
"RH for `E` is forced by its degree" becomes a theorem of the file. Note the sources lane
already records H-DEG as **variant** needing three separate quotes
(`1208.5370:IsogenyVolcanoes.tex:273`, `1509.00797:pRH.tex:241-242`, `:248-249`); the split
matches the quotes one-for-one.

**m2 — T0.2: the Statement covers `J = 0`, the Hypotheses say `J >= 1`.**
*Location:* T0.2 Hypotheses vs Statement vs `<1>6`.
Hypotheses: "`q = p^r`, `J >= 1`, `a_J != 0`". Statement: "The nonzero `J = 0` case is also
supersingular in odd characteristic, and has genus zero in characteristic two", and `<1>6`
proves it. *Fix:* change the hypothesis to `J >= 0`, `a_J != 0`.

**m3 — T0.2 `<1>2`: the displayed radical operator is right only because the coefficients lie in `F_q`; say so.**
*Location:* T0.2 `<1>2`, the expression `2 b a_0 x + sum_j b a_j (x^{q^j} + x^{q^{-j}})`.
The second family of terms comes from `Tr(b a_j y x^{q^j}) = Tr((b a_j y)^{q^{-j}} x)`, which
equals `Tr(b a_j y^{q^{-j}} x)` **only because `b, a_j` lie in `F_q` and are therefore fixed by
the `q`-power Frobenius**. The same remark is what makes `R_b(X) = L(X)^{q^J}` have the
displayed coefficients and degree `q^{2J}`. *Fix:* add the clause "since `b, a_j in F_q` are
fixed by `x |-> x^q`".
*Mitigating check:* the rest of `<1>2`–`<1>5` is sound, including the `p = 2` branch
(`2 b a_0` drops, the leading term `b a_J X^{q^{2J}}` survives, the polar form is unchanged by
the char-2 linear part, and the char-2 Gauss-sum modulus `p^{(m+d)/2}`-or-`0` is the standard
radical computation). The eventual-periodicity/Vandermonde step in `<1>5` is correct: the
`d`-tuples of power sums live in a fixed finite set and evolve deterministically under the
fixed linear recurrence, so the sequence is eventually periodic; `sum_i m_i(beta_i^h - 1)
beta_i^n = 0` for all large `n` with distinct nonzero `beta_i` forces `beta_i^h = 1` by
Vandermonde. No RH premise enters.

**m4 — T1.7: the H-WAT qualification catches the torsor problem but not the twist/`j`-invariant one.**
*Location:* register **H-WAT**; T1.7 `<1>2`.
The author's added qualification ("the relevant classes form a torsor for `Pic(O)`, and a
labeling requires a base choice") is exactly the correction the sources lane flags. What is
*not* flagged is the second half of that flag: the quotable source
(`1208.5370:IsogenyVolcanoes.tex:278-283`) indexes `Ell_O(k)` by **`j`-invariants**, not by
`F_q`-isomorphism classes, and those differ by quadratic twists. *Fix:* add "up to quadratic
twist / indexed by `j`-invariant" to H-WAT, or cite Waterhouse 1969 §7 directly for the sharp
form, as the sources lane recommends.

**m5 — H-CM's eigenspace clause has no byte-citable arXiv source; T4.7 and T4.6 rest on it.**
*Location:* register **H-CM**; T4.7 `<1>3`–`<1>4`; T4.6 `<1>2`.
`sources.md` records H-CM as **variant** and states that the clause actually used —
`H^1(A~(C),C) = (+)_phi C_phi` with `H^{1,0} = (+)_{phi in Phi} C_phi` and `pi~` acting on
`C_phi` by `phi(pi)` — "is NOT quotable from arXiv — assumed (Shimura–Taniyama; Lang,
*Complex Multiplication*, Ch. 1)". The author's use is **covered by H-CM as stated in the
register**, so this is provenance, not a gap in the argument. *Fix:* mark H-CM
`assumed (named-not-quoted)` in the notebook's provenance table before promoting T4.7 past
`conditional-on`.

**m6 — T2.1 `<1>2`: "the same congruence argument applies at each step" is too terse.**
*Location:* T2.1 `<1>2`.
The integrality of `c_{i+1} = (c_i + d_i - e_i)/pi` at `i = 0` is proved; for `i >= 1` the file
says only "the same congruence argument applies at each step". The clean route, which should
be written: cyclic shifting gives `(pi^n - 1) c_i = sum_{j=0}^{n-1} (d_{i+j} - e_{i+j}) pi^j`
(indices mod `n`), and reducing *that* modulo `pi` gives `c_i + d_i - e_i = 0 mod pi` for every
`i` uniformly.
*Mitigating checks:* everything else in T2.1 is exact. The carry bound is right — the
recursion gives `|pi| |c_{i+1}| <= |c_i| + C_D` for every `i`, and **cyclicity** makes
`max_i |c_{i+1}| = max_i |c_i| = R`, whence `R <= C_D/(|pi| - 1)`. And the `Z[i]`, `pi = 1+2i`
example is exactly as claimed (`scratch_rnt_t2_t03.py`): `y^2 = x^3 + x` over `F_5` has
`#E = 4` by brute force, so `a = 2` and the Frobenius roots are `1 +- 2i`;
`|Z[i]/(pi-1)| = |Z[i]/(2i)| = |Z[i]/(2)| = 4`; the digits `{0,1,-1,2,-2}` are distinct mod
`pi` (they hit all five classes of `F_5`) but hit only **2 of the 4** classes mod `pi - 1`; and
`|1 - pi^2|^2 = 32 > 25 = q^2`, with `N_2 = #E(F_25) = 32`.

**m7 — the certified T4.5a tensor *looks* defective in double precision, for exactly the reason the file criticises elsewhere; say so.**
*Location:* T4.5a; contrast with T4.5 `<1>4`.
T4.5 `<1>4` (rightly) faults the supplied search for reporting "three small even eigenvalues,
not exact zeros". Rebuilding T4.5a's own tensors from the certificate's centre in double
precision (`scratch_rnt_t45a.py`) gives even eigenvalues
`{1.0, 5.0, ~1e-5, ~1e-5, ~1e-5}` — the three "zeros" appear at `1e-5`, not `1e-16`. That is
the textbook conditioning of a **triple** root (`(1e-15)^{1/3} ~ 1e-5`) and is not a defect:
the characteristic polynomial comes out as `[1, -6, 5, 0, 0, 0]` to `1e-10`, i.e. exactly
`z^3(z-1)(z-5)`. *Fix:* one sentence in T4.5a saying that the correct numerical diagnostic is
the characteristic polynomial / Newton power sums, not the eigenvalues, precisely because of
the triple zero — otherwise the file's own criticism of the search reads as applying to its own
certificate.

**m8 — T4.3, the boundary case: nothing is a "zero Kraus matrix" at `w = nu`.**
*Location:* T4.3 Construction, "Zero Kraus matrices, if any at the endpoint, may be omitted."
At `w = nu` exactly, `S = sqrt(w) (I - b_0 b_0^* / nu)` is `sqrt(w)` times the rank-3 projector
onto `b_0^perp`; the four `B_ell = unvec(S e_ell)` are generically all nonzero, merely linearly
dependent (spanning a 3-dimensional space). Cosmetic; *fix:* say "linearly dependent" rather
than "zero".

**m9 — bookkeeping slips.**
(a) T4.5a's preamble says the certificate "was run ... under a 55-second `python3` timeout";
it runs in **0.17 s** on this machine. (b) T4.5a `<1>3` displays
`kappa := 10^{-50} + 2 * 81 * 10^{16} * 10^{-30}`, using `||B||_inf < 2`, while the code uses
the measured `bn = 1.49913`; both are valid, but the displayed number is the looser one.
(c) T0.1's title says "finite order in the shard's scope" and the Statement adds the
supersingularity conclusion, which needs H-SS-NP — correctly listed, but the title understates.

**m10 — cross-lane scope collision that the lab book must record explicitly.**
*Location:* T4.3 final paragraph and T4.7 final paragraph vs `numerics.md` "Surprise 5".
`numerics.md` states, as a headline surprise, "**`M` is not the Hodge Frobenius in any solution
found** ... The `M = diag(conj pi_1, conj pi_2)`, `N = 0` picture from the cohomology is a
saddle that every failing search is attracted to and no solution reaches. Whatever makes RH
manifest for this tensor, it is not the odd block being `sqrt q` times a unitary by
construction." T4.3 constructs precisely `M = conj(D)`, `N = 0` and says "the odd transfer is
already `diag(conj D, D)`; hence it is `sqrt q` times a unitary by construction." **These do not
contradict:** the numerics lane worked at `q = 5`, where T4.3's hypothesis `q + 1 >= 4 sqrt q`
fails (`6 < 8.944`), and on `C^{1|2}` with at most 3 even + 2 odd species; T4.3 needs
`q >= 16` and 5 even + 4 odd letters. *Fix:* one sentence in T4.3 and in the lab-book section
recording that the `M = conj D, N = 0` branch is provably available for `q >= 16` and
numerically unreachable at `q = 5` with few species — otherwise the two lanes will be read as
inconsistent.

---

## 2. Independent computations run (reviewer's own)

Scripts written for this review (none imports anything from the target file):
`notes/reviews/scratch_rnt_t3.py`, `scratch_rnt_t3b.py`, `scratch_rnt_t43.py`,
`scratch_rnt_t44.py`, `scratch_rnt_t45a.py`, `scratch_rnt_t0.py`, `scratch_rnt_t2_t03.py`,
`scratch_rnt_t04sd.py`.

Exact commands (all from `/home/tobiasosborne/Projects/riemann-channel`):
```
timeout 600 python3 notes/reviews/scratch_rnt_t3.py
timeout 600 python3 notes/reviews/scratch_rnt_t3b.py
timeout 900 python3 notes/reviews/scratch_rnt_t43.py
timeout 600 python3 notes/reviews/scratch_rnt_t44.py
timeout 900 python3 notes/reviews/scratch_rnt_t45a.py
timeout 600 python3 notes/reviews/scratch_rnt_t0.py
timeout 900 python3 notes/reviews/scratch_rnt_t2_t03.py
timeout 900 python3 notes/reviews/scratch_rnt_t04sd.py
PYTHONDONTWRITEBYTECODE=1 timeout 300 python3 notes/ring-norm-tensor/scratch/t45a_certificate.py
PYTHONDONTWRITEBYTECODE=1 timeout 300 python3 notes/ring-norm-tensor/scratch/t04_cutrank.py
grep -n "claimstatus" report/sections/04f_cmps_twisted_supertrace.tex
grep -n "tpp\|tmm" notes/ring-norm-tensor/scratch/weil_ring_norm_check.py
```

**C1. Ledger item 18, first half.** `Tr(sum_s A_s (x) conj A_s) = sum_s |Tr A_s|^2`, verified
on four random instances with `D = 3,4` and three species: the two agree to `1e-14`, while
`sum_s ||A_s||_HS^2` is a factor 3–7 larger (e.g. `16.436389` vs `72.488868`). **Item 18's
identity is right.** By hand it is one line: `Tr(A (x) B) = Tr A · Tr B`.

**C2. Ledger item 18, second half — the drafted inequality is FALSE.** The Pauli-diagonal
counterexample of T3.1 `<1>5` (one species, `m = k = 2`, `a = B = diag(1,-1)`) gives
`Tr S_+ = Tr S_- = 0`, so the drafted right-hand side `2 Tr(E_++) Tr(E_--)` is **0**, while
`sum_odd |mu|^2 = 8` (four odd eigenvalues of modulus 1, doubled). The repaired bounds hold with
equality: `2||M||_HS^2 = 2 tau_+ tau_- = 8`. **The drafted bound fails by an infinite factor;
the correction is right and is not an over-correction.** Confirmed independently that
`weil_ring_norm_check.py:223-224` computes `tpp`, `tmm` as `sum ||·||_F^2` while the inline
comments call them "Tr of the (++) block" — exactly the mislabelling item 18 diagnoses.

**C3. T3.1 (3.1)–(3.3), T3.2 (3.4), and the odd-block form.** 400 random instances,
`m, k in {1,2,3}`, 1–4 even species: **zero violations** of
`sum_odd |mu|^2 <= 2||M||_HS^2 <= 2 tau_+ tau_-`, of `||M||_HS^2 <= ||S_+||_HS ||S_-||_HS`
(3.2), and of `|Tr M^n|^2 <= Tr S_+^n Tr S_-^n` (3.4) for `n = 1..6`; and the odd block's
characteristic polynomial equals that of `M (+) conj M` to `1.2e-14` in every case. I also
re-derived (3.2) by hand: with `C_st = Tr(a_s^* a_t)`, `D_st = Tr(B_s^* B_t)` one has
`||M||_HS^2 = sum C_st conj(D_st)`, `||S_+||_HS^2 = sum |C_st|^2`, `||S_-||_HS^2 = sum|D_st|^2`,
and (3.2) is Cauchy–Schwarz on Gram entries. **Correct.**

**C4. T3.2's word formula.** `Tr S_+^n = sum_w |Tr a_w|^2` and
`Tr M^n = sum_w Tr(a_w) conj(Tr B_w)` verified to `6e-14` for `n = 1..4` on a `2|2` instance
with two species. So (3.4) really is Cauchy–Schwarz between two vectors of word traces, and
`s_pm(n) >= 0` for every `n`. **Correct, and this is the load-bearing repair.**

**C5. T3.3 `<1>1` — the question the brief singled out: could both `1` and `q` sit in one block?**
**No, and the argument is airtight.** If either block has no nonzero eigenvalue it is nilpotent
(finite matrix), so `s_pm(n) = 0` for all `n >= 1`; (3.4) then forces `Tr M^n = 0` for all
`n >= 1`; Newton/Vandermonde forces every eigenvalue of `M` to vanish; so the nonzero odd
spectrum is empty, contradicting `2g >= 2`. Hence each block carries at least one nonzero
eigenvalue, and since the total nonzero even spectrum is exactly the two values `{1,q}`, each
block carries exactly one. Spot-checked numerically (nilpotent `S_-` forces `spec M = {0,0}`).
**The step is forced, not merely plausible.**

**C6. T3.3 `<1>3`, the Cesàro step.** Averaging `|sum_j beta_j^n|^2` over `n <= 2·10^5`:
one `beta` -> `1.000000`; two distinct -> `1.999988`; one `beta` doubled -> `4.000000`; three
distinct -> `2.999972`. The limit is `sum_i m_i^2 >= sum_i m_i = g`, bounded by 1 by (3.5).
**`g <= 1` follows; the argument is correct including the multiplicity case.**

**C7. T3.3 `<1>5`, both counterexamples.** (a) `m=1, k=3`, `a_0=1, a_1=0`,
`B_0 = pi (+) 0_2`, `B_1 = 0 (+) e_12`: even nonzero spectrum `{1, 5}`, odd nonzero
`{1+2i, 1-2i}`, and `B_1 != 0` while `a_1 = 0`. (b) `m=1, k=2`, single
`B_0 = [[pi, b],[0,0]]`, `b = 0.7`: even spectrum `{1, 5, 0,0,0}`, odd `{pi, conj pi, 0, 0}`,
`||[M, M^*]|| = 2.32` (so `M` is **not** normal), and `str E^n = 4, 32, 148, 640` matches
`N_n = |1-pi^n|^2` exactly. **Both counterexamples are real; the drafted
"proportionality/normality" conclusion is correctly refuted, and the surviving conclusion
(proportionality of word-trace vectors) is the right one.**

**C8. T4.1 index/vectorisation conventions against a direct `E = sum A (x) conj A`.** With
row-major vectorisation and `P = diag(1,-1,-1)`, the even index set is `{0,4,5,7,8}` and the odd
`{1,2,3,6}`, exactly as the certificate uses. On a random `1|2` tensor with 2 even + 2 odd
species, the block predictions of (4.1)–(4.2) reproduce the direct Kronecker sum to `1.7e-16`:
`M = sum_s a_s conj(B_s)`, `N = sum_f conj(d_f) c_f`, `t = sum|a_s|^2`,
`u = sum_f c_f (x) conj c_f`, `v = sum_f d_f (x) conj d_f`, `W = sum_s B_s (x) conj B_s`.
**All conjugations and both transposes in T4.1 are right.** I also re-derived them by hand from
`X |-> A X A^*`.

**C9. T4.3 rebuilt from (4.5)–(4.6) alone.** At `q = 25` with `D = diag(pi_1^2, pi_2^2)` (the
`T4.4` base change): `min spec R = 2.653846...` (the author's quoted value **to every printed
digit**), even spectrum `{1, 25, 0, 0, 0}`, `E_o - diag(conj D, D) = 0` exactly,
`||[E, E^*]|| = 2.8e-15`, even block Hermitian to `3.2e-16`, depolarising identity (4.7)
residual `5.8e-15`, and `str E^n = N_n` for `n <= 12` with max relative error `1.2e-15`.
Repeated for `q = 16, 17, 19, 23, 27, 32, 49, 10^4` with random unit-modulus phases: identical
outcome each time. **T4.3 is correct as stated, with five even and four odd letters.**

**C10. The threshold is exactly `q + 1 >= 4 sqrt q`.** `R` is PSD for `q = 13.929` and fails for
`q = 13.928`; `7 + 4 sqrt 3 = 13.928203...`. Failures at `q = 4,5,7,8,9,11,13`; successes from
`q = 16`. **The stated equivalence and the "every prime power `q >= 16`" claim are both right.**

**C11. Two favourable structural facts the author did not state.** (i) The condition
`q + 1 >= 2g sqrt q` is *exactly* `q + 1 - 2g sqrt q >= 0`, i.e. the Weil **lower** bound on
`N_1` is nonnegative. (ii) The author's symmetric split `t = wg = (q+1)/2` is **optimal for the
ansatz**: the even `2x2` block is `[[t, h sqrt g],[h sqrt g, wg]]` with `t + wg = q+1` and
`t·wg - h^2 g = q`, and positivity of `R` is `w >= nu = gq/t`, i.e. `t(q+1-t) >= g^2 q`, whose
left side is maximised at `t = (q+1)/2` giving exactly `(q+1)^2 >= 4g^2 q`. So (4.3) is the best
this construction can do, not an artefact of a lazy choice. Worth recording.

**C12. The `C^{1|g}` sentence, `g = 3`.** With `t = (q+1)/2`, `w = (q+1)/(2g)`,
`h = (q-1)/(2 sqrt g)`: `q = 37, 41, 49, 64, 121` all give `10 = g^2+1` even and `6 = 2g` odd
letters, even spectrum `{1, q, 0^8}`, `E_o = diag(conj D, D)` exactly, normal transfer,
`str E^n = N_n` for `n <= 9` to `1.4e-15`; and `q = 25, 31, 32` fail, with the threshold
`(3 + 2 sqrt 2)^2 = 33.9706` matching `q + 1 >= 6 sqrt q`. I also re-derived the three constants
from `trace = q+1`, `det = q` on the surviving `2x2`. **The generalisation sentence is exactly
right, including all three formulas and the condition.**

**C13. T4.4.** `a' = a^2 - 2b = -5`, `b' = b^2 - 2 a (qa) + 2q^2 = 49 - 90 + 50 = 9`, giving
`z^4 + 5z^3 + 9z^2 + 125z + 625`, which I confirmed is the characteristic polynomial of the
squared roots. The six norms `31, 619, 15991, 390739, 9759526, 244128859` reproduce exactly, and
they are `N_2, N_4, N_6, N_8, N_10, N_12` of the `F_5` curve (`N_n/F_5 = 3, 31, 117, 619, 3318,
15991, ...`). Irreducibility mod 2: both quartics reduce to `z^4+z^3+z^2+z+1 = Phi_5`, which is
irreducible over `F_2` since `ord_5(2) = 4` — the author's reasoning (no linear factor, not
divisible by the sole irreducible quadratic) is a valid alternative. **All correct.**

**C14. T4.5a — the certificate runs and CERTIFIES.** Output:
`B norm 1.4991299396460234, eta 1.0064686513913206e-90, eps 3.5157778735872134e-58,
kappa 1.214295251113279e-12` — matching the file's quoted `1.49913`, `1.01e-90`, `3.52e-58` to
every printed digit. The asserted inequalities **are** what the code tests: `bn` is the maximum
absolute row sum of `B`, `eta = ||B f(y_0)||_inf`, `eps = ||I - BJ||_inf`, and the asserts are
`bn < 2`, `eta < 1e-70`, `eps < 1e-50`, `kappa < 1/4`, `eta + kappa·r < r` — exactly (4.10) plus
the contraction conditions. The targets `[6,26,126,626,3126, 3,-5,9,7]` are
`1 + 5^n` (`n=1..5`) and the Newton power sums of `z^4-3z^3+7z^2-15z+25` (`p_1..p_4 = 3,-5,9,7`,
which I recomputed). The even/odd index sets and the 14 nonzero positions match the file's
displayed lexicographic list.

**C15. T4.5a — the contraction logic, checked line by line.**
*Hessian bound `H = 10^16`:* valid. With `|x_i| <= 3` each complex entry has modulus `< 5`;
`||E||_inf <= 9·3·25 = 675 < 1000`; `||d_j E||_inf <= 2·(3·5) = 30` (a single-position `d`
contributes to at most one sector-row family); `||d_i d_j E||_inf <= 2`; and
`d_i d_j Tr(T^n) = n Tr(T^{n-1} d_i d_j T) + n sum_{m} Tr(T^m d_i T T^{n-2-m} d_j T)` gives
`<= d n((n-1)||T||^{n-2} 30^2 + 2||T||^{n-1})`, which at `n = 5, d = 5` is
`25(4·10^9·900 + 2·10^{12}) = 1.4·10^{14} < 10^{16}`. **The displayed estimate does justify `H`.**
*Mean value in nine variables with the max-row-sum norm:* `(Df(y)-J)_{ik} = sum_j d_j d_k f_i(xi)
(y-y_0)_j`, so each entry is `<= 9 H r` and each row sum `<= 81 H r`. **Correct**, and the
per-component `xi_i` freedom is harmless because the bound is uniform on the box.
*Contraction:* `||I - B Df(y)||_inf <= eps + ||B||_inf · 81 H r < 2e-12 < 1/4`;
`||N(y) - y_0||_inf <= eta + kappa r < r`, so `N` maps the closed `ell_inf` box into itself and
is a strict contraction, hence has a unique fixed point there; `||I - BJ||_inf < 1` makes `BJ`
and so `B` invertible, so the fixed point is a zero of `f`, and zeros of `f` in the box are
exactly fixed points of `N`. **Uniqueness in the box is correct.** Newton's identities then give
both characteristic polynomials (`d = 5` from `n = 1..5`; `d = 4` from `n = 1..4`). **The whole
certificate is sound.**

**C16. T4.5a — floating-point confirmation from the certified centre.**
`chi_e = [1, -6, 5, 0, 0, 0]` to `1e-10` (i.e. `z^3(z-1)(z-5)`), `chi_o = [1, -3, 7, -15, 25]`
to `1e-10`, odd eigenvalues `1.89564392 +- 1.18597391 i` and `-0.39564392 +- 2.20078756 i` with
`|mu|^2 = 5.0000000000` for all four (the Ramanujan property), and
`str E^n = N_n` for `n = 1..12`: `3, 31, 117, 619, 3318, 15991, 77997, 390739, 1955043,
9759526, 48801327, 244128859`, every one with relative error `< 6e-16`. `str E^n` also equals
`sum_w |Tr(P A_w)|^2` for `n <= 5`. **The certified tensor is exactly what T4.5a claims.**
(`||[E,E^*]|| = 50.9`, i.e. this tensor is *not* normal — T4.5a claims no normality, unlike
T4.3.)

**C17. T4.5a — the Jordan–Wigner Fock vector.** Feeding the certified tensors into
`scripts/cmps_parity_supertrace.py` in the manner of `genus2_followup.py`
(`Q = A_0 - I`, `R = (A_1, A_2, 0)`, boundary `P = diag(1,-1,-1)`, `eps = 1`):
`||Psi_P||^2 = 31.000000000, 117.000000000, 619.000000000, 3318.000000000` for `n = 2,3,4,5`,
against `N_n`, with differences `<= 4.6e-13`, and periodic-translation residual `<= 1.3e-14`.
**The explicit fermionic Fock-space norm of the certified tensor is the curve count.**

**C18. T4.2.** Re-derived by hand from (4.2): a `q`-eigenvector `0 (+) I_2` needs vacuum output
`sum_f ||c_f||^2 = 0`, so all `c_f = 0` and `N = 0`; an invariant vacuum line needs
`sum_f d_f d_f^* = 0`, so all `d_f = 0` and `v = 0`. In either case the even block is triangular
with diagonal blocks `t, W` and the odd block is `M (+) conj M`, so deleting all odd species
leaves the *same* spectra — a purely bosonic genus-2 tensor with even spectrum `{1,q}`, odd
spectrum the four Frobenius values (moduli `sqrt q != 1, q`, so no cancellation), contradicting
T3.3. **The triangular-deletion argument is valid and the hypotheses of T3.3 are genuinely met
by the deleted tensor.** For `<1>3`: the suggested ansatz gives `M = 1·conj(B_1) = 0`; then
`E_o = [[0, N],[conj N, 0]]` is similar to `-E_o` via `diag(I,-I)`, so its spectrum is symmetric
under `z |-> -z` and `Tr E_o = 0 != 3`. With one odd species `N = conj(d) c` has rank `<= 1`, so
`E_o` has rank `<= 2`. **Correct, and unconditional given the required spectra.**

**C19. T0.1 / T0.2, numerically.** For 15 cases `(q, a)` with `q = 3,5,7` and `J = 1,2`
(including the six `q=3` cases of `artin_schreier_super.py`): `E_g/sqrt q` is unitary to
`4.4e-16`, has finite order `h in {4, 8, 10, 12, 20, 28, 30, 36, 48, 84}`, all eigenvalues have
modulus 1 to `4e-15`, and `lambda^h = 1` to `3.2e-13`. **Every eigenvalue of `E_g` is `sqrt q`
times a root of unity in every tested case.** By hand, T0.1's determinant argument is sound:
`F_a^2 f(x) = f(-x)` so `F_a^4 = 1` and `det F_a in mu_4`; diagonal additive-character phases
and permutations have root-of-unity determinants; `W(M_g)^h = W(M_g^h) = 1` since
`Sp(2J,F_q)` is finite; hence `c_g^{q^J} = det U_g / det W(M_g)` is a root of unity and so is
`c_g`.

**C20. T0.3.** The matrix-unit alphabet at `n = 2` gives flattening rank `D^2` (4 at `D=2`,
9 at `D=3`). The unit-modulus example `A_0 = |0>(<0|+<1|)`, `A_1 = |1>(<0|-<1|)` does have ring
amplitude `(-1)^{sum_i s_i s_{i+1}}` for every word (verified at `n = 4, 6`), and its contiguous
`2|2` cut at `n = 4` has flattening rank **4 = D^2**. **The `D^2` bound is sharp and the `D`
bound is genuinely wrong for a ring; ledger item 4 is right.**

**C21. T0.4.** The author's kernel reproduces the printed table exactly, including the
irreducible moduli in increasing-power convention (`n=8`: `[1,0,0,0,1,1,0,1,1]` =
`X^8+X^7+X^5+X^4+1`) and the generators. See MAJ-1 for the self-dual-basis contrast.

---

## 3. Convention and cross-lane reconciliation

| Quantity | `astra-proofs.md` | reviewer's independent build | verdict |
|---|---|---|---|
| Doubled transfer | `E = sum_s A_s (x) conj A_s`, row-major vec, `X |-> A X A^*` | same; block formulas (4.1)–(4.2) reproduce to `1.7e-16` | agree |
| Parity sectors on `1\|2` | even `{0,4,5,7,8}`, odd `{1,2,3,6}` | same | agree |
| `str_Gamma E^n` | `= sum_w \|Tr(P A_w)\|^2` | verified to `1e-10`, `n <= 5`, mixed parity | agree (and it is a 2-line theorem, see MAJ-2) |
| `Tr(sum A (x) conj A)` | `sum \|Tr A\|^2` (ledger 18) | verified; `!= sum \|\|A\|\|_HS^2` | agree; the script's comment was wrong |
| Drafted `2 Tr(E_++)Tr(E_--)` bound | **FALSE**, Pauli-diagonal counterexample | `8 <= 0` fails | agree, refuted |
| Repaired bound | `2\|\|M\|\|_HS^2 <= 2 tau_+ tau_-` | 0 violations / 400 random instances | agree |
| All-power bound (3.4) | `\|Tr M^n\|^2 <= Tr S_+^n Tr S_-^n` | 0 violations, `n <= 6` | agree |
| T4.3 threshold | `q+1 >= 4 sqrt q`, i.e. `q >= 7+4 sqrt 3` | boundary bracketed at `13.928 / 13.929` | agree; and it is the ansatz-optimal split (C11) |
| T4.3 spectra | even `{1,q,0,0,0}`, odd `diag(conj D, D)`, normal | reproduced for 9 values of `q`, residuals `<= 1e-14` | agree |
| `C^{1\|g}` extension | `t=(q+1)/2, w=(q+1)/(2g), h=(q-1)/(2 sqrt g)`, `q+1 >= 2g sqrt q` | verified for `g = 3`, threshold `33.97` | agree |
| T4.4 base change | `z^4+5z^3+9z^2+125z+625`; six norms | exact | agree |
| T4.5a certificate | `\|\|B\|\|=1.49913`, `eta=1.01e-90`, `eps=3.52e-58` | reproduced digit for digit; CERTIFIED | agree |
| T4.5a spectra | `chi_e = z^3(z-1)(z-5)`, `chi_o` the Frobenius quartic | `1e-10`; `str E^n = N_n`, `n <= 12`, `6e-16` | agree (see m7 on the `1e-5` "zeros") |
| T4.5a physical norm | `N_n` via H-TWIST | explicit JW Fock vector, `n = 2..5`, `<= 5e-13` | agree |
| T0.4 cut ranks | `2,4,8,16,8,4,2` at `n=8`, "open" | reproduced; but `<= 4` for all `n` in a self-dual normal basis | **MAJ-1** |
| T4.3 `M = conj D, N = 0` | achieved for `q >= 16` | `numerics.md` says unreachable at `q = 5` | different scopes; **m10** |
| H-DEURING / H-DEG / H-WAT / H-CM / H-SCHUR | stated verbatim + author's qualifications | sources lane: variant / variant / variant / variant / no source | author's H-LM and H-WAT qualifications *anticipate* the flags; H-SCHUR is proved in T3.1; H-CM's eigenspace clause stays assumed (**m5**) |

---

## 4. Per-label verdicts

**VERDICT T0.1: VALID** — the determinant argument (`F_a^4 = 1`; phases and permutations;
`W(M_g)^h = 1`) really does give `c_g^{q^J}` a root of unity, hence `c_g`, hence finite order.
Confirmed numerically on 15 transfer matrices. Correctly scoped to odd prime `q`.

**VERDICT T0.2: MINOR** — the Gauss-sum/radical/recurrence proof is sound for all `p`
including 2 (radical dimension `<= 2rJ` from `deg R_b = q^{2J}`; char-2 modulus `p^{(m+d)/2}`
or 0; eventual periodicity + Vandermonde with no RH premise). Fixes: state `J >= 0` in the
hypotheses (m2) and note that the displayed radical operator needs `b, a_j in F_q` (m3).

**VERDICT T0.3: VALID** — `D^2` for a contiguous ring cut, `D^b` in general, and the bound is
sharp: two explicit rank-`D^2` examples verified, including a unit-modulus one.

**VERDICT T0.4: MINOR** — the eight-row table is exactly reproducible and the `F_2`-rank
interpretation is right. But the boundedness question is *not* open: `<= 4` for every `n` in a
self-dual normal basis, by a one-line nearest-neighbour argument (MAJ-1). Fix as in MAJ-1.

**VERDICT T0.C: VALID (as an open conjecture)** — explicitly `Status: open`, explicitly a
necessity-only claim, with the basis prescription, the coboundary quotient and "quadratic =
function degree" all spelled out, and with the disclaimer that it says nothing against the
finite ordinary norm tensors. No overclaim.

**VERDICT T1.1: VALID** — `chi_M = X^2 - aX + q`; `#Fix(M^n) = |Z^2/(M^n-1)Z^2| =
det(1-M^n) = |1-pi^n|^2 > 0`, so every fixed point is nondegenerate of index `+1`; the
cohomological degrees `1, M^T, q` give the Lefschetz number `1 - Tr M^n + q^n = N_n` (the
transpose is invisible to the trace, and T1.4 gets it right where it matters). `N_n` as the
index of `(1-pi^n)` in `O` is correct without H-LENSTRA. No circularity: `|pi|^2 = q` enters
only through H-DEG, which is an input (see m1 for the wording).

**VERDICT T1.2: VALID** — the zeta identity is immediate from T1.1; the orbit-count identity
`#Fix(M^n) = sum_{d|n} d c_d` and Möbius inversion are correct; and the refusal to call the
resulting bijection canonical (ledger 7) is the right caution.

**VERDICT T1.3: VALID** — `E = diag(1, conj pi, pi, q)`, `Gamma = diag(1,-1,-1,1)`,
`Tr(P A_{s_1}...A_{s_n}) = (1-pi^n) prod a_{s_i}`, `||Psi_P||^2 = |1-pi^n|^2 = N_n`, untwisted
`|1+pi^n|^2`. The `Lambda^*(C dz) (x) Lambda^*(C d bar z) ~ Lambda^*(H^1)` identification is
right and the "bond-odd vs physically-fermionic" distinction (ledger 11) is an important and
correct clarification. Physical reading inherits MAJ-2.

**VERDICT T1.4: VALID** — `U(e_k (x) omega) = e_{M^T k} (x) Lambda^*(M^T) omega`; `M^T` is
injective of index `q`, **not** a permutation (ledger 8, a genuine correction to the brief);
`ker(M^{nT}-1) = 0` over `Q` leaves the single orbit `{0}`; `str Lambda^* B = det(1-B)`.

**VERDICT T1.5: VALID** — `A_k = |M^T k><k| (x) F`; only the constant cycle survives; surviving
amplitude `Tr(P F^n) = 1 - pi^n`. The honest caveats (an operator kernel with two labels is not
a finite physical tensor; no new arithmetic content) are correct and required.

**VERDICT T1.6: VALID** — `M^*` scales the Hodge metric by `|pi|^2`, so `M^*/sqrt q` is unitary;
`deg(m+n pi) = m^2 + a mn + q n^2` is positive definite because `1, pi` is an `R`-basis of `C`,
whence `q - a^2/4 > 0` and `a^2 < 4q` strictly in the ordinary case. The `K (x) R` vs
`H^1(T^2,C)` type discipline in `<1>4` is exactly right. See m1 on the wording of H-DEG.

**VERDICT T1.7: MINOR** — every distinction drawn is correct (`GL_2(Z)` conjugacy vs `GL_2(C)`
conjugacy; `M^T` on the dual lattice; `Tr(P G X G^{-1}) = Tr(P X)` for even `G`; CM-type exchange
is not an even ket gauge). The author's H-LM and H-WAT qualifications *pre-empt* the sources
lane's flags. Missing: H-WAT's `j`-invariant/quadratic-twist gloss (m4).

**VERDICT T2.1: VALID** — unique `pi`-adic digit expansions; the cyclic-carry characterisation;
the bound `|c_i| <= C_D/(|pi|-1)` (correct, and the cyclicity is what makes the one-line
argument work); and the `Z[i]`, `pi = 1+2i` example verified in full by brute force, including
`#E(F_5) = 4`, Frobenius roots `1 +- 2i`, `|O/(pi-1)| = 4` with only 2 classes represented, and
`|1-pi^2|^2 = 32 > 25`. Terseness at `<1>2` noted in m6.

**VERDICT T2.2: VALID** — the residue argument is correct (a finite/trace-class `B` gives
residue `-m_B(lambda)/lambda` at `u = 1/lambda`, while a numerator eigenvalue demands
`+m_C(alpha)/alpha`, and the pole sets are disjoint because `|alpha| = sqrt q != 1, q`). The
graded `2|2` supertrace realisation and the sharp statement of what a carry automaton does and
does not count (ledger 16) are right, and the "carries are bounded, the failure is elsewhere"
correction is a real improvement on the brief.

**VERDICT T3.1: VALID** — block structure, (3.1), (3.2), (3.3), the proof of H-SCHUR from Schur
triangularisation (which closes the sources lane's "no arXiv source" gap), and the exact
counterexample refuting the drafted trace bound. Verified by hand and on 400 random instances.

**VERDICT T3.2: VALID** — `s_pm(n) = sum_w |Tr a_w|^2 >= 0` and
`|Tr M^n|^2 <= s_+(n) s_-(n)` are Cauchy–Schwarz on word-trace vectors. Verified numerically.
This lemma is the load-bearing replacement for the false drafted estimate.

**VERDICT T3.3: VALID** — `<1>1` is forced (see C5), `<1>2`–`<1>3` give `g <= 1` via the
Cesàro limit `sum m_i^2 >= g` (C6), `<1>4` gives the `1|1` equality case, and `<1>5`'s two
counterexamples are genuine (C7). The corrected equality statement (word-trace vectors, not
matrices) is right.

**VERDICT T3.4: VALID** — (3.6) is the two-way count of nonzero net multiplicities;
`mk >= g`; with odd dimension exactly `2g`, `mk = g`, `z_o = 0`, `z_e = m^2+k^2-2`, and
`g^2-1` nilpotent even modes on `C^{1|g}`; the minimisation correction (`min(m+k)` subject to
`mk >= g`, not `g+1`; `2|2` beats `1|4` at `g = 4`) is right, and genus two does need bond
dimension 3.

**VERDICT T3.5: VALID** — the odd-species block couplings, the zero length-one trace of the
new even off-diagonal blocks (but not of higher powers), the modified bounds (3.7) with
`2 Re Tr M^n = sum_j alpha_j^n + sum_x x^n`, and the scope statement ("fermions proved
necessary on the minimal `1|2` bond, not on every larger one") are all correct.

**VERDICT T3.6: VALID (conditional-on H-KRAUS-HS, H-ZERO)** — the compression argument, the
finiteness of `sum_s ||P K_s P||_HS^2 = Tr(Phi(P)P)`, the HS-eigenvalue bound for compact
operators, and the divergence step (`e^{2t Re mu_rho} > e^{-t}` in the notebook normalisation,
`> 1` unshifted) are correct. The corrected constant `2||S_+||_HS ||S_-||_HS` and the precise
statement of when the trace version is legitimate (positive self-adjoint on HS space) are right.
H-KRAUS-HS is a heavy hypothesis and the file says so.

**VERDICT T4.1: VALID** — (4.1) and (4.2) reproduce a direct `sum A (x) conj A` to `1.7e-16`
with the stated ordering and row-major vectorisation, for a mixed even/odd tensor. Both the
`M = sum a_s conj(B_s)` and `N = sum conj(d_f) c_f` conjugation patterns are right, as is the
"no Koszul sign is added" remark.

**VERDICT T4.2: VALID** — see C18. `<1>1` and `<1>2` are valid triangular-deletion reductions
to T3.3 whose hypotheses really are met by the deleted tensor, and `<1>3`'s `M = 0` argument
(rank `<= 2` with one odd letter; `z |-> -z` symmetry and zero trace in general) kills the
suggested vacuum ansatz unconditionally.

**VERDICT T4.3: VALID** — rebuilt from (4.5)–(4.6) alone at nine values of `q` and confirmed in
every detail (C9, C10, C12): the depolarising identity, the `[[t, sqrt2 h],[sqrt2 h, 2w]] =
[[(q+1)/2,(q-1)/2],[(q-1)/2,(q+1)/2]]` reduction with eigenvalues `q, 1`, `M = conj D`, `N = 0`,
normality, `str E^n = N_n`. The `C^{1|g}` sentence is right for `g = 3`. Only cosmetic m8, plus
the two favourable observations of C11.

**VERDICT T4.4: VALID** — base-change symmetric functions, the quartic, the six norms, the
`min spec R`, and the mod-2 irreducibility/simplicity/ordinarity discussion all check out.

**VERDICT T4.5: VALID** — the feasibility equivalence (28 real unknowns, degree-2 polynomial
entries, real characteristic polynomials, and T3.4 forbidding cancellation on `1|2`), the
H-RCF algebraicity transfer, and the sharp criticism of what a small least-squares residual
does and does not certify. The last is exactly right and the notebook should adopt it.

**VERDICT T4.5a: VALID** — the certificate runs and certifies; the tested inequalities are
(4.10); `H = 10^16` is justified by the displayed estimate; the nine-variable mean-value step in
the max-row-sum norm is correct; existence *and uniqueness in the box* follow from the
contraction; Newton's identities deliver both characteristic polynomials. Rebuilt in floating
point: `chi_e`, `chi_o`, `str E^n = N_n` for `n <= 12`, all four `|mu|^2 = 5`, and the explicit
Jordan–Wigner Fock norm `= N_n` for `n = 2..5` (C14–C17). Only the presentational m7 and m9.
**This is the strongest result in the file and it holds up completely.**

**VERDICT T4.6: VALID** — `Tr(P_J (Lambda^* D)^n) = (1-pi_1^n)(1-pi_2^n)`; `F omega = q omega`
for `omega = e_1 ^ f_1 + e_2 ^ f_2`; `str F^n|_S = N_n(C)` on the six-dimensional
`S = C1 (+) H^1(J) (+) C omega`; and the product-range contradiction (the five listed vectors
force factors of dimension `>= 3` each, so `>= 9 > 6`) is a correct use of "a nonzero pure
tensor in `U (x) W` has both factors in `U`, `W`". The normalisation
`int_J theta^2 = 2 = g!` for a principally polarised abelian surface, hence
`int_C i^* theta = int_J theta ^ [C] = 2` and `i^* theta = 2[pt]`, is right, as is the insistence
that `i^*` is restriction and not the subalgebra inclusion (ledger 31).

**VERDICT T4.7: VALID** — Rosati is an `R`-algebra involution of `K (x) R = C^g`; it cannot
permute distinct primitive idempotents (`Tr(e_j e_k) = 0` contradicts positivity) and cannot be
the identity on a factor (`(i e_j)(i e_j)^dagger = -e_j` has trace `-2 < 0`), so it is complex
conjugation at each place; applying the embeddings to `pi pi^dagger = q` gives
`|phi_j(pi)|^2 = q`. This is a genuine derivation of the modulus from positivity — unlike T1.6 it
does not have the conclusion inside its hypotheses. The trace form `2 sum_j Re(x_j conj y_j)` is
right. Provenance caveat m5.

**VERDICT T4.8: VALID** — the even gauge action `a_s |-> a_s`, `B_s |-> H B_s H^{-1}`,
`c_f |-> g_0 c_f H^{-1}`, `d_f |-> H d_f g_0^{-1}` is correct, as is the observation that for
T4.3 the scalar `g_0` cancels out of the mixed sector so the gauge cannot move `spec M`, and
that same-parity unitary rotations of the physical letters leave `E` exactly invariant.

**VERDICT T5.1: VALID (observation)** — labelled `Observation`, `Status: open`. `conj(rho) =
1 - rho` iff `Re rho = 1/2`, so the claim that ket/bra exchange is not the functional equation
off the critical line is correct, and the refusal to treat it as automatic is the right call.

**VERDICT T5.2: VALID (observation)** — correctly states that T3.6 excludes the all-even Kraus
class *in that analytic setting only*, and that necessity does not give sufficiency, finiteness
or an ordinary Hilbert norm.

**VERDICT T5.3: VALID (observation)** — the toral picture's content and its two honest limits
(the shift is not surjective; the abelian surface counts `J`, not `C`) are stated correctly.

**VERDICT T5.4: VALID (observation)** — and the self-correction here is right and important:
"fixed finite lattice tensors give only supersingular zetas" **is false**, refuted by the file's
own T1.3 and T4.3. Nothing false is asserted.

**VERDICT LEDGER (36 items): VALID, with two MINOR wording fixes** — I checked all 36. The
central item 18 is correct in both halves (C1, C2) and correctly diagnoses the script's
mislabelling; items 4, 7, 8, 16, 19, 20, 21, 22, 24, 26, 27, 29, 31, 36 were each verified by
hand or numerically; items 1, 2, 3, 14, 25, 30, 33 are accurate scope corrections. Fixes:
**item 5** should record that the cut rank *is* bounded in a self-dual normal basis (MAJ-1);
**item 17** should distinguish the algebraic and physical halves of H-TWIST (MAJ-2).
No item is an over-correction and none is wrong.

---

## 5. Summary verdict table

| label | verdict |
|---|---|
| T0.1 | VALID |
| T0.2 | MINOR (m2, m3) |
| T0.3 | VALID |
| T0.4 | MINOR (MAJ-1) |
| T0.C | VALID (stated open) |
| T1.1 | VALID |
| T1.2 | VALID |
| T1.3 | VALID |
| T1.4 | VALID |
| T1.5 | VALID |
| T1.6 | VALID (m1 wording) |
| T1.7 | MINOR (m4) |
| T2.1 | VALID (m6 terseness) |
| T2.2 | VALID |
| T3.1 | VALID |
| T3.2 | VALID |
| T3.3 | VALID |
| T3.4 | VALID |
| T3.5 | VALID |
| T3.6 | VALID (conditional-on H-KRAUS-HS, H-ZERO) |
| T4.1 | VALID |
| T4.2 | VALID |
| T4.3 | VALID (m8 cosmetic) |
| T4.4 | VALID |
| T4.5 | VALID |
| T4.5a | VALID (m7, m9 presentational) |
| T4.6 | VALID |
| T4.7 | VALID (m5 provenance) |
| T4.8 | VALID |
| T5.1 | VALID (observation) |
| T5.2 | VALID (observation) |
| T5.3 | VALID (observation) |
| T5.4 | VALID (observation) |
| LEDGER (36 items) | VALID (fix items 5 and 17) |

---

## 6. Overall assessment

The refutation failed: thirty-one labelled statements, four observations and thirty-six ledger
items survive adversarial re-derivation, and every number I could check independently — the
Pauli-diagonal counterexample, the `q + 1 = 4 sqrt q` threshold bracketed at `13.928/13.929`,
`min spec R = 2.653846...`, the base-changed quartic `z^4+5z^3+9z^2+125z+625` and its six norms,
the certificate's `1.49913 / 1.01e-90 / 3.52e-58`, `chi_e = z^3(z-1)(z-5)`,
`str E^n = N_n` through `n = 12`, and the Jordan–Wigner Fock norms `31, 117, 619, 3318` —
reproduces to every printed digit. **What should be recorded in the lab book as proved** (in each
case conditional only on the named external inputs, and with the physical Fock-space reading
inheriting shard 04f's `sketched-conditional` status per MAJ-2): the Tier-A package
T1.1–T1.7 (Frobenius on the lifted torus, `N_n = N_{K/Q}(1-pi^n)`, the Lefschetz/index-`+1`
count, the dynamical zeta, the `C^{1|1}` tensor `A_s = a_s diag(1,pi)` with
`||Psi_P(n)||^2 = N_n`, the Hodge PH unitary `M^*/sqrt q`, and the gauge/ideal-class
distinctions) conditional on H-DEURING, H-DEG, H-FROB, H-LEF (+H-LENSTRA, H-LM, H-WAT where
cited); the **repaired** bosonic no-go T3.1–T3.5, where the drafted Hilbert–Schmidt/trace
inequality is *false* and the all-power word-trace inequality
`|Tr M^n|^2 <= Tr S_+^n · Tr S_-^n` plus a Cesàro average proves `g <= 1` without cancellation,
together with the Euler-characteristic bookkeeping `(m-k)^2 - (z_e - z_o) = 2 - 2g` and
`mk >= g`; T4.1–T4.2 (block equations and the death of the vacuum ansatz); the explicit
nine-letter algebraic construction T4.3 for every `q` with `q + 1 >= 2g sqrt q` — a condition
which, as noted in C11, is exactly nonnegativity of the Weil lower bound on `N_1` and is the
optimal split for that ansatz — with T4.4 giving the `F_25` instance of the supplied curve;
the computer-assisted **exact** two-even, one-odd `C^{1|2}` tensor T4.5a for the supplied
`F_5` curve, whose rational contraction certificate I re-ran and whose logic I checked step by
step; T4.6's non-product curve-cohomology projector; and T4.7, which is the one place in the
file where RH is *derived* rather than assumed (Rosati positivity forces conjugation at each CM
place, hence `|phi_j(pi)|^2 = q`). **What must stay sketched or open:** T0.C and the whole
amplitude-locality dichotomy; the universal three-species conjecture T4.C and any natural
geometric selection of the T4.5a entries; genus-two existence for `q < 16` beyond the single
certified example, and species optimality; purely bosonic realisations with extra cancelling
spectrum on bonds larger than `1|2`; T3.6 and T5.2's fermion-necessity claim, which are
conditional on the strong analytic hypothesis H-KRAUS-HS and prove no existence; and all of
T5.1/T5.3/T5.4, which are labelled observations and correctly claim nothing. Two things must be
fixed before promotion: T0.4's boundedness question is **not** open (bounded by `4` in a
self-dual normal basis, MAJ-1), and H-TWIST must be split into its unconditional algebraic half
and its `sketched-conditional` physical half (MAJ-2), since every "conditional-on H-TWIST"
status line currently understates that dependence.

Files written by this review:
- `notes/reviews/ring-norm-tensor-2026-09-14.md` (this file)
- `notes/reviews/scratch_rnt_t3.py`, `scratch_rnt_t3b.py` (ledger 18, T3.1–T3.3)
- `notes/reviews/scratch_rnt_t43.py` (T4.3 rebuilt from (4.5)–(4.6); threshold; `C^{1|g}`, `g=3`)
- `notes/reviews/scratch_rnt_t44.py` (T4.4 numbers; T4.1 conventions; H-TWIST word identity)
- `notes/reviews/scratch_rnt_t45a.py` (T4.5a tensors, `chi_e`, `chi_o`, `str E^n`, Jordan–Wigner)
- `notes/reviews/scratch_rnt_t0.py` (T0.1 roots of unity on the `artin_schreier_super` cases)
- `notes/reviews/scratch_rnt_t2_t03.py` (T2.1 `Z[i]` example; T0.3 counterexamples)
- `notes/reviews/scratch_rnt_t04sd.py` (T0.4 in a self-dual normal basis — MAJ-1)

---

## 7. Post-fix re-verdict (2026-09-14, after the shard corrections)

I re-read the applied text in `report/sections/06c_ring_norm_inputs.tex`,
`06d_ring_norm_elliptic.tex`, `06f_ring_norm_genus_two.tex` and
`02g_definitions_ring_norm_tensor.tex`. All five items I raised are applied correctly, in the
shards, with the prover's file left as written. Specifically:

- **m2, m3 — applied.** `thm:as-quadratic-supersingular` now reads "$\qs = p^r$, $J\ge0$,
  $a_J\ne0$", removing the hypothesis/statement mismatch, and its proof sketch now says the
  radical computation uses "that $b,a_j\in\Fq$ are fixed by $x\mapsto x^{\qs}$", which is
  exactly the missing justification for the displayed $\qs$-linearised operator and for
  $R_b = L^{\qs^J}$ having degree $\qs^{2J}$. The rest of the sketch (radical dimension
  $\le 2rJ$; Gauss-sum modulus $0$ or $p^{(m+d)/2}$ with phase in $\{\pm1,\pm i\}$; finite
  value set independent of $n$; eventual periodicity; Vandermonde; "no root size is assumed")
  matches what I verified. The appeal to additive Hilbert 90 for
  $y^{\qs}-y = c$ is the right name for the solvability criterion used.

- **m4 — applied.** `prop:integral-marking-gauge` now glosses Waterhouse's torsor as "indexed
  by $j$-invariants, up to quadratic twist", which is precisely the second half of the sources
  lane's flag on H-WAT. With the existing "all full ideal lattices, not only invertible ones"
  gloss on Latimer--MacDuffee, both integral-classification caveats are now stated.

- **m1 — applied** (beyond what I asked). `thm:elliptic-ph-unitary` now says $|\pi|^2 = \qs$
  is "derived, not assumed", from $[\Lambda:\pi\Lambda] = |\pi|^2$
  (`cit:degree-norm-index`) plus $\deg\Frob = \qs$ preserved under good reduction
  (`cit:hasse-degree-bound`). That is the two-way split I proposed, realised as two distinct
  byte-cited facts. One line of polish, not blocking: the clause actually used from
  `cit:hasse-degree-bound` is the quoted `Then $d=\deg(\pi)=q$`, **not** the quoted
  `$c^{2}\leq4d$`; a half-sentence saying so would make the non-circularity self-evident to a
  reader who sees Hasse's bound sitting in the same citedfact.

- **MAJ-1 — applied and closed.** `num:cut-rank-binary` now records the self-dual normal basis
  result in full: $\Tr(x^3) = \Tr(x\cdot x^2) = \sum_i x_ix_{i-1}$ is a cyclic
  nearest-neighbour form, contiguous-cut rank $\le 4 = D^2$ for every $n$, checked for
  $n = 3,5,6,7,9,10,11$, with the correct caveat that no self-dual normal basis exists over
  $\mathbb F_2$ for $n = 4,8$; it states that the prover's $n$-dependent prescription reaches
  $16$ at $n = 8$ and left the question open, and that "cut rank is basis dependent". It also
  contrasts the cubic ($2,4,8,16$ at $n = 3,5,7,9$), which is the dichotomy the campaign wanted.
  `conj:amplitude-locality` correctly now quantifies over a **self-dual** normal-basis
  prescription. The question is no longer open, and the numerical row states the boundedness
  correctly.

- **MAJ-2 — applied.** The split is implemented exactly as requested: the algebraic identity
  $\str_{\Gdb}\Edb^n = \sum_w|\Tr(PA_w)|^2$ is built into `def:graded-lattice-tensor`, while
  the physical Fock identification is `thm:cmps-twisted-supertrace` and enters **only**
  `cor:genus-two-physical-norm`, which carries `claimstatus ... sketched-conditional`. The
  tensor theorems `thm:nine-letter-tensor` and `thm:f5-certified-tensor` are
  `proved-conditional`, no longer inheriting the sketched status through H-TWIST. The intro
  paragraph of `06c` states the split in the same terms.
  *One strengthening available, recorded for later and not blocking:* both the intro paragraph
  and `def:graded-lattice-tensor` hedge the algebraic identity to "all-even letters" and
  attribute the odd-letter case to `thm:cmps-twisted-supertrace`. The identity is in fact
  **unconditional**, odd letters included: $\Edb^n = \sum_w A_w\otimes\bar A_w$ by ordinary
  Kronecker multiplicativity (no statistics sign is inserted, by the definition itself), and
  $\Tr\bigl((P\otimes\bar P)(A_w\otimes\bar A_w)\bigr) = \Tr(PA_w)\overline{\Tr(PA_w)}$. I
  verified this numerically for a $1|2$ tensor with two even and two odd letters
  (`notes/reviews/scratch_rnt_t44.py`): $\str\Edb^n = \sum_w|\Tr(PA_w)|^2$ exactly for
  $n = 1..5$. The shards are therefore conservative, not wrong; the hedge can be dropped.

Nothing in the applied text introduces a new error, and no verdict moves in the unfavourable
direction. Re-verdicts:

VERDICT T0.2: VALID
VERDICT T0.4: VALID
VERDICT T1.7: VALID

All other verdicts of §5 stand unchanged, and the overall assessment of §6 stands with its two
MAJOR caveats now discharged.
