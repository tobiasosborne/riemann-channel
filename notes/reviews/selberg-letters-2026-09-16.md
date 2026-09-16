REVIEWER: claude:opus-5

# Adversarial (REFUTE) review of `notes/selberg-letters/astra-proofs.md`

**Stance.** REFUTE. For each labelled item I tried to break it: I recomputed every sign,
ordering, normalisation and integer multiplicity from independently written scripts
(`notes/reviews/scratch_sl_*.py`, none of which import or re-run the author's
`notes/selberg-letters/finite/check_letters.py`), and I byte-checked every `file:line`
citation in the target against the source text. Default under uncertainty is INVALID.

**Target.** `notes/selberg-letters/astra-proofs.md` (655 lines; D1–D8, ledger L01–L40, two
labelled-input theorems, script `notes/selberg-letters/finite/check_letters.py` with output
`finite/check_letters.out`). Draft under correction: `notes/selberg-letters/draft.md`;
brief: `notes/selberg-letters/astra-brief.md`. Author: `codex:gpt-6-astra`.

**New source fetched.** Booker–Lee–Strömbergsson, arXiv:1803.06016, e-print unpacked into
`refs/src/1803.06016/main.tex`. Theorem 1.1 (`\label{thm:SEC}`) is at
`refs/src/1803.06016/main.tex:120–123` and reads verbatim: *"The Selberg eigenvalue
conjecture is true for $\Gamma_1(N)$ for $N\leq 880$, and for $\Gamma(N)$ for $N\leq 226$."*
This confirms the target's H-MOD-GAP and hence ledger row L28.

## Outcome summary

The report survived the attack. I found **no BLOCKER and no MAJOR**. Everything load-bearing
that I could recompute independently came out exactly as the report states:

* the Casimir ordering $\Omega=X^2+U_+U_--X$ (and the draft's $+X$ is wrong), the first-band
  eigenvalue $\lambda(1+\lambda)$, the ladder coefficient $m(2z-m+1)$ and its identification
  with DFG's $m!\prod_j(2\lambda+m+j)$, the vanishing set $-1-\tfrac12\mathbb N_0$, the FE sign
  $JXJ^{-1}=1-X$ (the draft's $-1-X$ is wrong), the diffusion commutator $(2\lambda-1)U_+$,
  and the impossibility of a positive $G$ with $A^*G+GA=-G$ on a Jordan block
  (`scratch_sl_algebra.py`, 30/0);
* the *entire* D2 divisor table, recomputed from Marklof's divisor theorem alone:
  $\operatorname{ord}_1\zeta_R=1$, $\operatorname{ord}_0\zeta_R=c$ (a zero, not a pole),
  $2c-1$ at $-1$, $2c$ below; $\operatorname{ord}_0D_{\rm tow}=1$,
  $\operatorname{ord}_{-N}D_{\rm tow}=cN^2+2$; $\operatorname{ord}_{1/2}Z_S=2d_{1/4}$ and
  $\operatorname{ord}_{-1/2}D_{\rm tow}=2d_{1/4}$; all four ring-zeta rows verified as
  convergent orbital sums; $\phi(1/2)=-1$; $\zeta(\rho-1)\ne0$; FJS's two forms of $m_n$;
  the Maass–Selberg leading coefficient (`scratch_sl_divisor.py`, 47/0);
* the whole D7 finite theorem including $C^*G_CC=qG_C$, the Schur complement, $F_C$, the
  companion intertwining, $F_\mu$ as a two-sided inverse *at* $\mu=\pm\sqrt q$, the
  $K_3\square Q_3$ nullities $(2,4)$ at $-2$ on a $120$-dimensional edge space and the
  ten-letter odd nullities $(1,2)$ at $3$, and $N_P(1..6)=8,32,104,640,3208,15392$ recomputed
  by brute force over cyclically non-backtracking words (`scratch_sl_finite.py`, 64/0);
* the D8 theta counterexample to 12 digits, the Poisson-summation identity, the weight shift
  $L_{\rm adj}=2\Omega-m^2/2$ and the Hodge supertrace identity (`scratch_sl_ktype.py`, 12/0).

I re-ran the author's `check_letters.py`: it reproduces `FINAL TALLY: 131 PASS / 0 FAIL`, and
its committed `.out` matches the fresh run line for line (modulo printed float residuals).

Provenance is unusually good: I spot-checked **31** `file:line` citations (all nine DFG ones,
both DZ ranges, all three Marklof ranges, all six FJS ranges including the 370–401 divisor
theorem and the line-371 Venkov/Hejhal attribution, Momeni–Venkov, Harrow, Hastings, and
twelve notebook-shard ranges). **All 31 point at text that says what is claimed**, with one
status overstatement (Issue 3). No misattribution and no invented citation was found; the
report's corrections to the draft's own DFG line numbers (ledger L16) are themselves correct.

Six MINOR issues follow. None changes the truth of any statement; three of them are
provenance or wording, three are scope/attribution.

## Issues

### 1. The D3 statement's $\lambda$-set is displayed without its parameter restriction
* **Location.** D3 "Statement (as proved)", the display
  $\lambda\in[-1,0]\cup(-\tfrac12+i\mathbb R)$, and the following sentence "The first-band
  nonconstant divisor lies on $-1/2+i\mathbb R$ iff H-COERC holds."
* **Severity.** MINOR.
* **What is wrong.** As displayed this reads as an exhaustive description of the first-band
  parameters, but the report's own H-DFG-POIS is declared only for
  $\lambda\notin-1-\mathbb N_0$, and the Rayleigh argument of Step 4 needs $\pi_*u\ne0$. The
  report itself shows in Step 9 that a first-band state at $\lambda=-1$ has $\pi_*u=0$, i.e.
  "first band $\Rightarrow$ nonzero pushforward" is false in general. At
  $\lambda\in\{-2,-3,\dots\}$ nothing in the cited material excludes first-band states, and
  those parameters are *not* in the displayed set: the tower carries genuine extra order there
  ($\operatorname{ord}_{-N}D_{\rm tow}=cN^2+2$, against the band prediction $2$), so the
  exceptional points are not empty. The sentence "None of the negative parameters at or below
  $-1$ belongs to the nonconstant first band in the open strip" (Step 9) is true but vacuous —
  it restricts to the open strip, which already excludes them.
* **Evidence.** DFG `refs/src/1403.0256/RuelleResonForHn.tex:635` ("known to be an isomorphism
  for $\lambda\notin-1-\mathbb N$"); target D3 Step 9 (the $\pi_*u=0$ argument at $\lambda=-1$);
  `scratch_sl_divisor.py` ("g=2: ord_-N D_tow = c N^2 + 2 for N=1..8", giving $6,18,38,\dots$
  at $-1,-2,-3$ against the band prediction $2$).
* **Proposed fix.** Insert the restriction: "for $\lambda\notin-1-\mathbb N_0$,
  $\lambda\in[-1,0]\cup(-\tfrac12+i\mathbb R)$", and state the divisor sentence as "the
  nonconstant first-band divisor in $\mathbb C\setminus(-1-\mathbb N_0)$ lies on
  $-\tfrac12+i\mathbb R$ iff H-COERC". Nothing else in D3, D4 or the labelled-input theorem
  changes.

### 2. The order of the modular Selberg zero at $\rho/2$ is not in the cited FJS text
* **Location.** D6 "Statement (as proved)": "the scattering determinant has a pole of order $m$
  at $s_0=\rho/2$, and $Z_S$ has a zero there of order $m$"; H-CUSP-DIV.
* **Severity.** MINOR.
* **What is wrong.** FJS's divisor items 1, 2, 3, 4 and 7 all carry explicit multiplicities;
  item 6, the one used here, does not — it reads only "Zeros at each $s=1-\rho,1-\bar\rho$
  where $\rho$ is a zero of $\phi(s)$ with $\Re(\rho)>\tfrac12$ and $\Im(\rho)>0$". The order-$m$
  claim is standard and almost certainly right, but it is an inference, and the report is
  elsewhere scrupulous about marking exactly that kind of inference (it does so for the
  Venkov/Hejhal book pages two lines earlier).
* **Evidence.** `refs/src/1607.08053/main.tex:388` (item 6, no multiplicity) versus `:374`,
  `:376–377`, `:381–384`, `:385–386`, `:389–391` (the items that do carry multiplicities). The
  pole of $\phi$ at
  $\rho_1/2$ and $\zeta(\rho-1)\ne0$ are independently confirmed in
  `scratch_sl_divisor.py` ("phi blows up at s0 = rho_1/2", $|\phi|\sim5.1\times10^7$ at
  distance $10^{-8}$; $|\zeta(\rho_1-1)|=1.2254631$).
* **Proposed fix.** Either mark the multiplicity as inherited-but-unverified in the same style
  as the book pages, or derive it (equate the residues of $Z'/Z$ and $\phi'/\phi$). The
  RH-equivalence in the same paragraph does not depend on the order, so no conclusion moves.

### 3. H-CP-NORM calls a `sketched-conditional` shard theorem "proved"
* **Location.** D5 hypothesis block, H-CP-NORM: "its ring supertrace is the nonnegative squared
  norm **proved** in `04f_cmps_twisted_supertrace.tex:50–59`".
* **Severity.** MINOR (provenance).
* **What is wrong.** The cited lines are `thm:cmps-twisted-supertrace`, whose shard status line
  is `\claimstatus{thm:cmps-twisted-supertrace}{sketched-conditional}`. The report's own
  convention elsewhere is to name the status of a cited notebook claim.
* **Evidence.** `report/sections/04f_cmps_twisted_supertrace.tex:50–59`; the status line
  `\claimstatus{thm:cmps-twisted-supertrace}{sketched-conditional}` is at `:52`, and part (iv)
  — the nonnegativity actually used — begins at `:57`.
* **Proposed fix.** Write "asserted with status `sketched-conditional` in
  `04f…:50–59` (part (iv))". The D5 conclusion is unaffected: it needs only the *sign*
  convention of a cMPS ring norm, and the flat supertraces $-C$ and $-C/(1-e^{-t})$ are
  negative measures regardless (`scratch_sl_ktype.py`).

### 4. Ledger L06 does not correct an error in the draft; five further rows report the draft's
questions as claims
* **Location.** Correction ledger, rows L06; also L04, L05, L20, L23, L26.
* **Severity.** MINOR.
* **What is wrong.** L06's "claimed" column is "Function flow's ring zeta is its tower
  determinant". The draft already describes the flow on functions as *"the 'all odd' graded
  spectral transfer of the flow on functions"* with tower $D_{\rm tow}$ — which is exactly the
  report's own all-odd row. So L06 corrects nothing; it adds the even-convention sign
  ($1/D_{\rm tow}$), which is a clarification. Separately, L04, L05, L20, L23 and L26 attribute
  to the draft claims that the draft explicitly posed as open questions or instructions
  ("state whether they should be designated trivial…", "Say (i) whether this satisfies
  def:graded-transfer-channel…", "state the divisor … marked unverified; do not invent a
  citation"). The *true statement* column is correct in every one of these rows; only the
  "claimed" column over-attributes.
* **Evidence.** `notes/selberg-letters/draft.md:83–87` (L04/L05/L06: "state whether they should
  be designated trivial … or whether $Z_S$ itself is the better ring zeta (of the tower
  $D_{\rm tow}$ …): the 'all odd' graded spectral transfer of the flow on functions"),
  `:146–149` (L20: "Say (i) whether this satisfies def:graded-transfer-channel …"),
  `:141–143` (L23), `:160–163` (L26: "marked unverified; do not invent a citation").
* **Proposed fix.** Retitle the "claimed" column "drafted or asked", or add "(drafted as an
  option)" to those six rows; consider dropping L06 or relabelling it "clarification". This
  matters because the lab book reads the ledger as a list of *errors found*.

### 5. "Stable" for $\eta_+$ collides with DFG's dual-bundle naming
* **Location.** D2, the paragraph after the transfer table: "'Stable' here labels the covector
  dual to $U_+$".
* **Severity.** MINOR (cosmetic, but the reader will trip).
* **What is wrong.** The label is consistent with DFG, who call $U_+$ the stable field
  (`RuelleResonForHn.tex:643–645`). But as a *covector*, $\eta_+$ annihilates $X$ and $U_-$,
  i.e. $E_0\oplus E_u$, and therefore lies in what DFG call $E_u^*$
  (`:2071–2073`: "$E_u^*(y)$ consists of covectors annihilating $E_0(y)\oplus E_u(y)$" with the
  explicit warning "note that $E_u,E_s$ are switched places"). A reader checking D2 against D5's
  $B_\perp$ or against the draft's "$E_u^*, E_s^*$" will mis-assign the $e^{t}$ weight.
* **Evidence.** DFG `:643–645` and `:2071–2073`; the report's own D3 Step 3 correctly identifies
  the annihilator of $\{X,U_-\}$ with $E_u^*$.
* **Proposed fix.** One clause: "…dual to $U_+$ (DFG's stable field; as a covector this line is
  DFG's $E_u^*$, their $\ast$-convention switching $u$ and $s$)".

### 6. The "derived from the letters" headline for the positive form is stronger than the proof
* **Location.** "Main conclusions", second bullet: "The positive first-band form is derived using
  Haar, the Lie algebra, and DFG analysis."
* **Severity.** MINOR (framing).
* **What is wrong.** The construction is honest in the body (Steps 6–7 say the branch
  orthogonalisation is "an explicit modal choice" and that the completion is "the transported
  modal one"), but the headline hides that, once every retained $\lambda$ has $\Re\lambda=-1/2$
  and the block is semisimple, the *existence* of a $G$ with $A^{*G}+A=-1$ is the notebook's own
  equivalence (`def:graded-rh-fe-ramanujan` (HP), "equivalent to those operators being
  diagonalisable with spectrum on the circle", `prop:hp-inner-product-discrete`). What the
  letters genuinely supply is (i) the branch norms $\|\pi_*u\|_{L^2(M)}$, from Haar through
  $\pi_*$, and (ii) the reality/line location; the rest is the standard equivalence plus the
  threshold analysis, which is the report's real new content.
* **Evidence.** `report/sections/02h_definitions_graded_ramanujan.tex:79–84` ((HP) and its
  stated equivalence); target D3 Steps 6–7.
* **Proposed fix.** Reword to "The positive first-band form is *constructed*, with its branch
  norms derived from Haar through $\pi_*$; its existence, given the line, is the notebook's (HP)
  equivalence, and the new content is the threshold obstruction."

## Remarks that are not issues (recorded so they are not re-litigated)

* The two-term complex's rightmost rate is carried by the **odd** block ($\lambda+1=1$ at the
  constant), so `def:graded-transfer-channel`'s "growth is even and simple" fails for this
  object. The report discloses this ("they are not claimed to satisfy the CP definition's even
  Perron requirement") and files the object as a graded *spectral* transfer, which is the right
  bin.
* I checked the net divisor of the two-term complex directly, $\nu(z)=m_A(z)-m_A(z-1)$, against
  the Selberg divisor at $z=1,0,-n,1/2\pm ir,-1/2\pm ir$: all agree
  ($\nu(0)=1-(c+2)=-(2g-1)$, $\nu(-n)=-c(2n+1)$, $\nu(-1/2+ir)=d-d=0$). The "$d$ pairs even
  level $m$ with odd level $m+1$, the odd level zero survives" picture of D2 Step 4 is
  consistent with the arithmetic, not merely decorative.
* D3 Step 8's threshold argument is correct and sharp: at $\lambda=-1/2$ the ladder gives only
  $m=0$ (since $m=1$ would need a Laplace eigenvalue $-3/4$), so geometric multiplicity is
  $d_{1/4}$; $-1/2$ is exactly the first point of DFG's `t:noalg` exceptional set
  $-\tfrac12-\tfrac12\mathbb N_0$ (`:364–367`); and $\operatorname{ord}_{-1/2}D_{\rm tow}=2d_{1/4}$
  is confirmed independently in `scratch_sl_divisor.py`.
* D7's "$\mu=\pm\sqrt q$ is not an exception to the eigenspace isomorphism" is correct: my
  script verifies $F_\mu$ as a two-sided inverse on *every* retained root including the double
  roots, for K_4 (6 lifts), Petersen (18 lifts) and the six-letter Pauli channel.
* The quantum convention correction (ledger L35, $\mathrm{Ad}(U_i)$ not $\mathrm{Ad}(U_i^*)$) is
  exactly the notebook's: `08_quantum_ihara_general.tex:34–36` and `:50–52` give
  $\Hash(v\otimes|i\rangle)=\sum_{j\ne\bar i}\Eop{i}v\otimes|j\rangle$ and
  $\Rmap(v\otimes|i\rangle)=\Eop{i}v$.
* `refs/src/1803.06016/` was created (e-print unpacked); no other file outside
  `notes/reviews/` was touched.

## Verdict

```
VERDICT D1: VALID
VERDICT D2: VALID
VERDICT D3: MINOR
VERDICT D4: VALID
VERDICT D5: MINOR
VERDICT D6: MINOR
VERDICT D7: VALID
VERDICT D8: VALID
VERDICT LT-SELBERG: VALID
VERDICT LT-FINITE: VALID
VERDICT LEDGER: MINOR
```

D3: MINOR = Issue 1 (add "for $\lambda\notin-1-\mathbb N_0$" to the displayed $\lambda$-set);
Issue 6 is a wording remark on the same item's headline. D5: MINOR = Issue 3 (H-CP-NORM calls a
`sketched-conditional` shard theorem "proved"); every mathematical conclusion of D5 stands.
D6: MINOR = Issue 2 (the order-$m$ multiplicity of the Selberg zero at $\rho/2$ is an inference,
not in the cited FJS text); the OPEN verdict of the item itself is the right one and its
corrections L26–L31 are sound. LEDGER: MINOR = Issue 4; bad rows are **L06** (corrects nothing) and, in the weaker
sense of over-attributing the draft's questions as claims, **L04, L05, L20, L23, L26**. All
other rows (L01–L03, L07–L19, L21, L22, L24, L25, L27–L40) are correct corrections of real
defects in `draft.md`.

## Scratch scripts written for this review

| Script | What it checks | Printed tally |
|---|---|---|
| `notes/reviews/scratch_sl_algebra.py` | independent lowest-weight $\mathfrak{sl}_2$ realisation on $\mathbb C[x]$; brackets; three Casimir orderings (and the draft's wrong one); $\Omega u=\lambda(1+\lambda)u$; ladder to $m=6$ and its DFG form; the vanishing set; $L_{\rm adj}=2\Omega+\tfrac12W^2$; $[U_-,\tfrac12(H^2+E^2)]u=(2\lambda-1)U_+u$; $JXJ^{-1}=1-X$ vs the draft's $-1-X$; the degenerate $[[1,1],[1,1]]$ Gram; no positive $G$ on a Jordan block | `TALLY scratch_sl_algebra.py: 30 PASS / 0 FAIL` |
| `notes/reviews/scratch_sl_divisor.py` | Selberg divisor taken only from Marklof `zetathm`; all $\zeta_R$, $D_{\rm tow}$, threshold and tower integer orders for $g=2,3,5$; all four ring-zeta rows as convergent orbital sums; the sampled adjacency $a_\tau(\sigma)$; $\phi(1/2)=-1$, $\phi(s)\phi(1-s)=1$, $\zeta(\rho-1)\ne0$, the pole at $\rho_1/2$; FJS $m_n$ in both forms; the Maass–Selberg leading coefficient | `TALLY scratch_sl_divisor.py: 47 PASS / 0 FAIL` |
| `notes/reviews/scratch_sl_finite.py` | D7 from scratch in the notebook's source-letter convention: (D7-data), $RT=\Sigma R-RJ_0$, $RJ_0T=qR$, $\Sigma R=R(T+qT^{-1})$, $F_\mu$ two-sided on every retained root incl. $\pm\sqrt q$, $TL=LC$, $L^*L$, $C^*G_CC=qG_C$, Schur $\leftrightarrow$ strict band, all of (D7-FE); $K_3\square Q_3$ exact spectrum and Hashimoto nullities $2,4$ at $-2$; six-Pauli sector spectra, reduced zeta and $N_P(1..6)$ by brute force over cyclically non-backtracking words; ten-letter endpoint, odd nullities $1,2$ at $3$ | `TALLY scratch_sl_finite.py: 64 PASS / 0 FAIL` |
| `notes/reviews/scratch_sl_ktype.py` | D8 theta counterexample at four times against Poisson summation; the printed value $0.730000328323$; positivity of the Poisson side; $L_{\rm adj}=2\Omega-m^2/2$ and its agreement with `03d` obs:continuous-harrow-tempered; the Hodge-bundle diffusion supertrace identity; negativity of both D2 flat supertraces | `TALLY scratch_sl_ktype.py: 12 PASS / 0 FAIL` |

Author's script re-run for independence of the claim, not as my evidence:
`OPENBLAS_NUM_THREADS=1 python3 notes/selberg-letters/finite/check_letters.py` reproduces
`FINAL TALLY: 131 PASS / 0 FAIL`, matching the committed `finite/check_letters.out`.

---

# Round 2 (re-verdict after the six MINOR fixes were applied)

**Scope.** The coordinator applied all six MINOR items and asked for fresh verdicts on D3, D5, D6
and LEDGER, and for confirmation of D2's cosmetic clause. I re-read the corrected wording in
`notes/selberg-letters/astra-proofs.md` ("Post-review corrections", lines 655–681) and in the three
lab-book shards named, and re-checked the new citation against the source bytes. The proof bodies
of `astra-proofs.md` are unchanged, as intended; the registered statements are the shard ones.

**The Round 2 verdict block below supersedes the Round 1 block for D2, D3, D5, D6 and LEDGER.**
(Coordinator: if the gate greps the *first* `VERDICT <item>:` match rather than the last, the
Round 1 block must be neutralised by hand — I was told to append only.)

## Fix-by-fix verification

| Round 1 issue | Where applied | Verified |
|---|---|---|
| 1 — D3 $\lambda$-range | `03e_selberg_letters.tex:153–157`, thm:selberg-first-band-form (i) | **Yes, verbatim my proposed fix**: "so for $\lambda\notin-1-\mathbb N_0$ (the range of the Poisson isomorphism; at $\lambda=-1$ a first-band state has $\pi_*u=0$) the first-band divisor lies in $(-\tfrac12+i\mathbb R)\cup[-1,0]$". The exclusion is the safe one (DFG's own is $-1-\mathbb N$, `1403.0256/RuelleResonForHn.tex:635`), and $-1$ is inside it, so the parenthetical is consistent. Statement now true as written. |
| 2 — D6 order $m$ | `03f_selberg_letters_finite.tex:31–33`, obs:modular-scattering-sector | **Yes**: "(its location is item~6 of `asm:cusp-divisor-theorem`; the order $m$ is inferred from the residues of $Z_S'/Z_S$ and $\phi'/\phi$, not stated in the source)". This is exactly the distinction I asked for, and the RH sentence that follows uses only the location. |
| 3 — H-CP-NORM status | `03e_selberg_letters.tex:217–218`, prop:selberg-no-cp-realisation | **Yes in substance**: "(\cref{thm:cmps-twisted-supertrace}(iv), itself `sketched`; only the sign is used; L23)". The material misrepresentation ("proved") is gone. One-word residue: see R1 below. `astra-proofs.md` post-review item 3 names the status correctly. |
| 4 — ledger attribution | `03e_selberg_letters.tex:19`; `astra-proofs.md` post-review item 4 | **Yes**: the intro now reads "a $40$-row correction ledger of which $34$ rows correct the draft and $6$ answer questions the draft had posed", and the appendix names exactly the six rows I flagged (L04, L05, L06, L20, L23, L26). $40-6=34$ ✓. |
| 5 — $\eta_+$ / $E_u^*$ | `02h_definitions_graded_ramanujan.tex:145–147`, def:stable-transverse-complex | **Yes, verbatim**: "it annihilates $E_0\oplus E_u$ and so lies in the bundle Dyatlov–Faure–Guillarmou call $E_u^*$, ``stable'' referring to the naming of $\Uhor{+}$". Checked against DFG `:643–645` (U₊ is the stable field) and `:2071–2073` ("$E_u^*(y)$ consists of covectors annihilating $E_0(y)\oplus E_u(y)$ … note that $E_u,E_s$ are switched places"). Correct. |
| 6 — "derived from the letters" | `03e_selberg_letters.tex:165–169`, thm:selberg-first-band-form (ii) | **Yes, verbatim my proposed fix**: "What the letters supply here is the branch norms and the reality and line of (i); once the line holds and the block is semisimple, the existence of *some* positive form is the (HP) equivalence of `def:graded-rh-fe-ramanujan`, and the new content is that this particular form is the transported Haar form, together with the threshold obstruction of (iv)". |

**New citation, byte-checked.** `cit:bls-selberg-level-one`
(`03f_selberg_letters_finite.tex:17–24`, status `cited`) quotes, detokenized, *"The Selberg
eigenvalue conjecture is true for $\Gamma_1(N)$ for $N\leq 880$, and for $\Gamma(N)$ for
$N\leq 226$."* with provenance `1803.06016:main.tex:121-122`. I diffed this against the two source
lines: **byte-exact**, and `db/provenance.tsv:152` carries the same quote and locator. The
"reported, unverified" wording is indeed gone. `db/claims.tsv:358` attributes the check to
`claude:opus-5`, which is accurate — I fetched and line-checked it.

**No new mathematical error was introduced.** I re-derived each amended sentence: the amended (i)
is exactly the statement I verified in Round 1 once restricted; (ii)'s new sentence is an accurate
statement of what `def:graded-rh-fe-ramanujan` (HP) already asserts; the 03f order-$m$ sentence is
the correct attribution; the 02h clause is correct against DFG. I also re-ran the promoted script
`scripts/selberg_letters.py`: `FINAL TALLY: 131 PASS / 0 FAIL`, matching `outputs/selberg_letters.txt`,
so the intro's "$131$ checks" is right, as is its "four independent scripts, $153$ checks"
($30+47+64+12=153$).

## Residual cosmetic items (none verdict-changing; please fix in passing)

* **R1.** `03e_selberg_letters.tex:217` calls `thm:cmps-twisted-supertrace` "`sketched`", but its
  `\claimstatus` is `sketched-conditional` (`04f_cmps_twisted_supertrace.tex:52`). This lab book
  uses both tags as distinct live statuses (73 uses of `sketched`, 28 of `sketched-conditional`
  across `report/sections/`), so a reader or a status audit will see the wrong tag. **Fix:** one
  word. I considered MINOR and judged it below threshold, because the substance of Round 1 Issue 3
  — an unproved claim being called proved — is fully repaired; only the suffix is dropped. Say so
  if you want it graded MINOR instead.
* **R2.** Both `03e_selberg_letters.tex:21` and `astra-proofs.md`'s post-review header report my
  Round 1 outcome as "$8$ VALID, $3$ MINOR". The Round 1 block was **7 VALID** (D1, D2, D4, D7,
  D8, LT-SELBERG, LT-FINITE) and **4 MINOR** (D3, D5, D6, LEDGER). **Fix:** "7 VALID, 4 MINOR" in
  both places (or, after this round, "Round 1: 7 VALID, 4 MINOR; Round 2: all VALID").
* **R3.** `astra-proofs.md` post-review item 1 says the restriction "is now stated with the
  display", but the D3 display in that file (line 193) is deliberately unchanged. **Fix:** "is
  recorded here and stated with the display in `03e`, thm:selberg-first-band-form (i)".

## Round 2 verdict

```
VERDICT D2: VALID
VERDICT D3: VALID
VERDICT D5: VALID
VERDICT D6: VALID
VERDICT LEDGER: VALID
```

All six Round 1 MINOR items are correctly and completely applied; four of them use my proposed
wording verbatim. D2's cosmetic clause is confirmed. The Round 1 verdicts for the items not
re-opened stand unchanged: D1 VALID, D4 VALID, D7 VALID, D8 VALID, LT-SELBERG VALID,
LT-FINITE VALID. Nothing in the target is now INVALID or MINOR in my judgement; the three residual
items R1–R3 are wording and bookkeeping.
