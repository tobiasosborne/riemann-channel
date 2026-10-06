# Today's ladder against the registered record

Author: `claude:opus-5.5`, 2026-10-06, lane O of an orchestrated session.

Status: **a cross-reference, not a round; nothing registered; no shard.** Nothing in `db/`, `report/`, `scripts/` or any existing note was changed.

**What was compared.** On one side is today's record: `data-ladder.md` at HEAD `8fd4aea`, 259 lines. That version already includes the corrections from the ζ REFUTE review (`notes/reviews/adelic-gkp-zeta-2026-10-06.md`). I first read an earlier 245-line version; where the difference matters it is noted. The lane pages are `lattice-tower.md`, `cone-bridge.md`, `zeta-ingredients.md`, `family-vacuum.md` and `cm-lift.md`.

On the other side is the registered record:
- shards 04q and 04t, with their rows in `db/claims.tsv`;
- the claim statements in 08b and 08c;
- `prop:ccm-tn-operator-gram`;
- every other row that a grep of `db/claims.tsv` turned up as touching the same objects (04p, 04u, 04w, 06c, 06d, 06f, 10);
- `notes/weil-bond-analytic/analytic.md` §0. This file is not registered.

**Conventions in this page.**
- A citation `file:a-b` gives the line range of the claim's `\begin…\end` block in `report/sections/` (from `grep -n`).
- A status is the derived status in the shard's `\claimstatus`. `scripts/labbook_check.py` appends `-conditional` when a dependency is assumed. The raw `db` status is added in brackets where it differs.
- Two scratch checks back statements made here for the first time. They are in `/tmp/…/scratchpad/laneO/` and are not part of the repository:
  - `check_04u.py` (sympy): 04u's certificate $G$ equals $\tfrac12\Omega_B(F_1-V_1)$, and $\Omega_BJ=G/r$.
  - `check_two_forms.py` (numpy): on the genus-two curve over $\mathbb F_5$, the Rosati Gram matrix in the rescaled basis equals 08b's Toeplitz matrix to $1.3\cdot10^{-15}$. For $M'$, 08b's form is positive semidefinite while the lattice Weil form is negative.

## 0. Verdict

1. **No registered claim is refuted or weakened by today's record.** §7 lists the fourteen closest candidates and gives the reason each one stands.
   - One registered clause is dated, though not wrong: `obs:deninger-same-gap`'s "the notebook has a canonical $B$ only on the genus-one Hodge ket".
   - One registered claim already contains today's one-mode identity without saying so: in `thm:lps-bass-frobenius`(c) the certificate $G$ is the Weil form $\tfrac12\Omega_B(F_1-V_1)$.
2. **Much of the ladder is already registered**, under other names:
   - "RH ⇔ invariant vacuum": in the abstract form in 04q, on finite spans of ζ's zeros in 04t, in the LPS instance in 04u, and as the finite lemma in 04w and 08c.
   - The cone: 04l, 04t, 04u, 04w.
   - Lane E's genus-two numbers: 04w.
   - "$B$ is the vacuum point": 04t `prop:weil-form-not-metric`(a, c) together with `thm:bond-positive-metric-criterion`(c), and in words in `obs:deninger-same-gap`.
   - The functional-equation pairing that lane G uses: 04t `thm:fe-pairing-jets`.
   - "Gate phases carry the root number, not RH": `obs:spt-protection-is-sign-data`, in general form.
   - "The lattice class is not fixed by counts": follows from `cit:latimer-macduffee` and `cit:lenstra-structure`.
3. **New relative to the record:**
   - integrality as a separate item of the ladder;
   - the orientation (CM type $\Phi_+$) condition on the lattice Weil form, and the isomorphism from compatible forms to similitude forms (lane E);
   - the genus-$g$ bridge $\Omega_+$/$\Omega_{\rm can}$;
   - "the overlaps see the order, not the class" (lane F);
   - the CM global negative finding and the gate phases (lanes C, I, J);
   - shared vacua for families (lane M);
   - the prime-step analysis for ζ, the second compatible form $\Omega_D$, and the window negative finding (lane G).
4. **Precision faults that remain in today's record when measured against the registered one** (§8.2):
   - `lattice-tower.md` §5 credits all three of its equivalences to `thm:deninger-invariant-polarisation`. That theorem has only (i)⇔(iii).
   - `data-ladder.md` §4 item 2 still says (line 139) "$B$ is the **vacuum point**" relative to $\Omega_{\rm FE}$ without the normalisation caveat. The caveat is on `zeta-ingredients.md` line 189, and its basis is `prop:weil-form-not-metric`(b).
   - §4b line 178 writes the mode as $\{\rho,1-\bar\rho\}$; for a critical zero it is $\{\rho,\bar\rho\}$ (review S3a).
   - "Weil form" names two different objects in 08b/08c and today (§2.3).
5. **Contradiction found and already corrected:**
   - The 245-line version's "what ζ lacks is … one $\Omega$ for the whole commuting family" contradicted `thm:fe-pairing-jets`, which gives one form compatible with every step on every finite zero span. The ζ review (S2b) found the same, and `8fd4aea` corrected it.
   - The same version's "no orientation makes every [CM] Weil form positive" is undercut by 04t `thm:cm-torus-class-group-bond`(b), "up to the choice of prime above $p$": choosing the prime fixes the sign. Review S3b found this as well, and it is corrected.

## 1. "RH ⇔ an invariant Gaussian vacuum for the normalised step"

Today's statement: `lattice-tower.md` §5 (lines 89–113) as corrected by lane E (`cone-bridge.md` Props 1–3, lines 55–79), and `data-ladder.md` §0 (lines 15–20). For an integral step $M$ of norm $q$ on $(L,\Omega)$, the following are equivalent: (i) $M$ is semisimple with $|\mu|=\sqrt q$; (iii) there is an invariant vacuum $J$. Statement (ii), positivity of the Weil form $\tfrac12\Omega(M-V)$, is equivalent to them only when $M$ has no real eigenvalue and $\Omega$ is of CM type $\Phi_+$. The counterexamples are $M'$ and $B\oplus2B^{-T}$.

| registered claim | where | status | relation | comparison |
|---|---|---|---|---|
| `thm:deninger-invariant-polarisation` | 04q:134-154 | proved | states (i)⇔(iii) and more; states less on (ii) | It is a continuous-time flow statement with a compatible $B$. (ii) gives "invariant polarisation ⇔ (HP)". (iv) gives existence and uniqueness: unique for simple spectrum in $(0,\pi)$; $\mathrm U(p,q)/\mathrm U(p)\times\mathrm U(q)$ for a repeated eigenvalue; the Siegel space at $\omega\in\{0,\pi\}$; none off the circle. (iv) assumes semisimplicity. It has no form $\tfrac12\Omega(M-V)$, no orientation condition and no integrality. The "Siegel space at $0,\pi$" clause covers $B\oplus2B^{-T}$: a vacuum exists while every compatible Weil form vanishes. This is why (ii) needs "no real eigenvalue" and (iii) does not. |
| the package in 04t's preamble (not a claim block) | 04t:15-18 | input from `notes/deninger-lps/src/`, not a row | states exactly (i)⇔(iii) for a step | For $A^T\Omega A=q\Omega$: an invariant compatible $J$ exists ⇔ $G>0$ with $A^TGA=qG$ ⇔ bounded powers of $q^{-1/2}A$ ⇔ diagonalisable with unimodular spectrum, and $J=-LR^{-1}$. This is the discrete-step form of lattice-tower §5 (i)⇔(iii), without integrality. It is registered only through its ζ transcription in the next row. |
| `thm:bond-positive-metric-criterion` | 04t:68-86 | proved | states the same for ζ on finite spans; states more on jets | On a finite full-jet span: a positive invariant form exists ⇔ the zeros are critical **and simple**. With $\Omega_{\rm FE}$ fixed, the four package conditions are equivalent, and $Je_\rho=-i\,\mathrm{sgn}\,\gamma\,e_\rho$. (c) distinguishes certificates (one weight per ordinate) from the compatible metric (fixed by $\Omega$). That is lane E's "cone versus vacuum of $\Omega$" in ζ's setting. "Simple" here plays the role of today's "semisimple". |
| `prop:genus-two-metric-cone` (first sentence); `prop:hp-inner-product-discrete` | 04w:67-82; 08c:72-79 | proved; proved | state lane E Prop 1(a) | "Unitary in some positive metric iff semisimple with unimodular spectrum." |
| `thm:lps-bass-frobenius`(c) | 04u:82-99 | proved | states (i)⇔(ii) and §4b's one-mode identity for one $\Phi_+$ form | The certificate $G=\bigl(\begin{smallmatrix}1&-T/2\\-T/2&17\end{smallmatrix}\bigr)$ (04u:20) equals $\tfrac12\Omega_B(F_1-V_1)$ exactly (`check_04u.py`). So "$G>0$ iff $\lVert T\rVert<2\sqrt{17}$" is "Weil form positive ⇔ RH". "$\Omega_BJ=G/r(T)$" with $r_a=\sqrt{17}\sin\theta_a$ is data-ladder §4b's "Weil form $=\sqrt q\sin\theta\cdot$ vacuum form". The Bass form $\Omega_B$ has every Krein sign $+1$, so lane E's $\Phi_+$ caveat is met and the claim is not affected. |
| `prop:cm-type-gauge`; `thm:rosati-ph-genus-two`; `thm:genus-two-cm-reference` | 06f:242-251; 06f:224-240; 04w:95-112 | proved-cond.; proved-cond.; proved-cond. (db: proved) | state the ingredients, not the consequence | "The CM type is a marking, not a gauge." The PH models "agree up to positive weights and the CM type". The reference type is $\Phi_0=\{\alpha_{1,-},\alpha_{2,+}\}$, which is mixed. None of the three says that a non-$\Phi_+$ compatible form has an indefinite Weil form while a vacuum exists. That is lane E's Theorem 5.1 and Prop 2 (Krein signs), and it is new. |

**"The positive metric as RH plus simplicity"** is the title phrase of 04t. Its content is `thm:bond-positive-metric-criterion`(a) and `thm:no-energy-equivalent-metric` (04t:88-97, proved-conditional [db: proved]). Today's (i) says "semisimple" where 04t says "simple". For an integral step with squarefree characteristic polynomial (lane E's standing hypothesis) the two coincide. On jets they do not: a multiple zero is a Jordan chain, which 04t excludes and today's pages never meet. `prop:weil-blind-jordan` (08c:89-98) is the registered statement that the trace form does not see this distinction.

**Verdict.**
- No conflict.
- The (i)⇔(iii) half of today's statement is registered four times.
- The (ii) half, with its $\Phi_+$ and "no real eigenvalue" hypotheses and lane E's isomorphism $\Omega'\mapsto W_{\Omega'}$, is not registered. It is registered only as the $\Phi_+$ instance in 04u.
- `lattice-tower.md` §5 calls `thm:deninger-invariant-polarisation` "the abstract form" of all three equivalences. That is accurate for (i)⇔(iii) only.

## 2. "The Weil form of ζ is the vacuum point / the Rosati form of the family's algebra"

Today's statement: `zeta-ingredients.md` §3.1 (lines 91–115) and `data-ladder.md` §4 item 2 (131–146) and §4b (165–199). After the ζ review the reading is:
- "vacuum point" means that $B$ is invariant under the whole family (review G3);
- Weil's criterion is that the functional $\omega$ is a state on the squeeze $*$-algebra, not that the involution is positive (review S3c).

### 2.1 Against 04t and 04q

| registered claim | where | status | relation | comparison |
|---|---|---|---|---|
| `prop:weil-form-not-metric` | 04t:136-160 | proved | (a, c) state lane G's vacuum point; (b) forces the normalisation caveat | (a): under RH, $W=\sum m_\rho F_f(\rho)\overline{F_g(\rho)}$, the counting norm of evaluations. (c) names three spaces. In the second, the diagonal semisimplification $\ell^2\{(\rho,j)\}$, "$G=1$ invariant iff RH … with the pairing and star". That is exactly lane G's model. (b): "unit weights are tied to a chosen evaluation normalisation". Hence "$B=G_J$ for 04t's $J$" holds only once the jets $e_\rho$ are matched to the evaluations $\hat h(\rho)$ at unit scale (review G3). |
| `thm:bond-positive-metric-criterion`(c, d) | 04t:68-86 | proved | states the identification and why it is cheap | (c): $G_J(e_\rho,e_\nu)=\delta_{\rho\nu}$ for $\Omega_{\rm FE}$. (d): the diagonal commutant acts transitively on certificates. So every positive form invariant under every step is the vacuum form of some compatible $\Omega$, and "vacuum point" carries no information beyond invariance. |
| `obs:deninger-same-gap` | 04q:226-244 | sketched | states the same in other words | "No candidate metric emerges beyond the inequivalent diagonal form on mode coefficients, which is RH." That diagonal form is lane G's $B$ in its vacuum reading. |
| `thm:ks-not-deninger-h1`; `thm:no-energy-equivalent-metric` | 04q:186-206; 04t:88-97 | proved; proved-cond. | state more (analytic) | The diagonal form is not equivalent to the energy or Hardy norm on $K_S$: the kernels are not a Riesz basis. Today's pages work in the diagonal model or on a window and make no claim about $K_S$. |

### 2.2 The Rosati reading against 03g, 08c and analytic §0

- **`prop:ccm-tn-operator-gram`** (03g:58-69, proved) is the registered one-generator, finite form of "the Weil (trace) form of the step algebra is a Rosati-type trace form". If $E^*\mathcal GE=\mathcal G>0$, then $(\mathrm{Gram})_{jk}=\mathrm{Tr}((E^j)^\sharp E^k)$ and $c^*\mathrm{Gram}\,c=\lVert p_c(E)\rVert^2_{{\rm HS},\mathcal G}$. The trace functional is a state on the algebra generated by $E$ *because* $\sharp$ is the adjoint for an invariant positive metric, that is, because a vacuum exists.
  - The claim states **more** than today in one respect. Its converse says that Gram equality for all powers forces native unitarity.
  - It states **less** in two respects: one generator, not a family; and the metric is assumed, not derived.
  - Lane G's reading, as corrected by S3c, generalises it from the group algebra of $\mathbb Z$ to that of $\mathbb R_+^\times$.
- **`obs:weil-zeta-dictionary`** (08c:109-122, sketched) and **`thm:weil-positivity-continuous`** (08c:17-28, proved) treat ζ's Weil form as the Bochner form of one flow: the autocorrelation of the centred trace. That is the same object as lane G's $B$ on the group algebra of $\mathbb R_+^\times$. Lane G finds that $B$ is a Weil-form point only for the generator $D$, with Williamson weights $|\gamma|$. This is the symplectic counterpart of `prop:hp-inner-product-continuous` (08c:81-87): $L'-a$ is skew-adjoint in some inner product iff $L'=a+iH$. Lane G calls it tautological, and the registered claim agrees, since it is an "iff" that needs the spectrum.
- **`analytic.md` §0, L13** (line 71; unregistered) already has the dictionary $\mathbb R[F]\leftrightarrow$ test algebra, Rosati $\leftrightarrow h\mapsto\tilde h$, $\mathcal T\leftrightarrow Z$. Lane G's reading is L13 with the family made explicit. Review S3c's correction ("positivity of ω, not of the involution") is in L13's own wording: "an involutive algebra whose *trace* is positive".

### 2.3 Two objects called "Weil form"

There are two forms with this name:
- In 08b/08c (`def:weil-form`, 02b:249), the Weil form is the Toeplitz form $\sum c_l\bar c_k\nu_{l-k}$ of the rescaled trace sequence, on test coefficients.
- Today, it is $\tfrac12\Omega(M-V)$ on the lattice.

They are related exactly by a cyclic vector:
- Write $u_i=(F/\sqrt q)^i$. Then $\mathcal T(u_i,u_k)=\mathrm{Tr}(F^iV^k)\,q^{-(i+k)/2}=\nu_{i-k}$. So the Rosati form on $\mathbb R[F]$ is 08b's form restricted to real $c$ of length $2g$, with an empty trivial set and $r=\sqrt q$. This is checked to $1.3\cdot10^{-15}$ on the $\mathbb F_5$ curve.
- Lane E's Theorem 5.2 gives $\mathcal T_L=2\,W_{\Omega_+}$ under $e=1$.

Hence **08b's Weil form on a window of length $2g$ is twice the lattice Weil form of the particular compatible form $\Omega_+$**. Consequences:

| 08b/08c claim | where | status | statement | today | affected? |
|---|---|---|---|---|---|
| `thm:weil-positivity-finite` | 08b:50-56 | proved | positive definiteness of the trace sequence ⇔ the one-sided bound | the lattice form needs $\Omega$, which already forces $\mu\mapsto q/\mu$ symmetry (04q thm (i)); so today is always in 08b's two-sided case | no |
| `thm:weil-duality-pairing` | 08b:72-79 | proved | with the duality, $W=\mathcal M$ (mode pairing); $W\ge0$ ⇔ circle ⇔ every mode is its own partner | lane E's per-mode decomposition is this identity read on the lattice through $\Omega_+$ | no; consistent |
| `prop:kraus-no-duality-example` | 08b:177-183 | proved | the Weil form is defined without a duality; its positivity is the one-sided bound | without a compatible $\Omega$ the lattice Weil form is undefined; no counterpart today | no |
| `thm:kraus-weil-criterion`, `obs:kraus-dichotomy` | 08b:159-171; 08c:234-251 | proved | inverse pairing gives the FE, adjoint pairing gives reality, both together give unitarity of the Kraus letters | today's $\Omega$ is the FE half (04q thm (i), `obs:gl1-bond-no-metric`: "the automorphism gives the functional equation, not the circle"). Today's vacuum is unitarity of the normalised *step*, not of the Kraus letters; 04q (ii) states this contrast explicitly | no |

The trace form is blind to orientation; the lattice form is not. $M'=\bigl(\begin{smallmatrix}0&1\\-5&-2\end{smallmatrix}\bigr)$ has a positive semidefinite trace form, of rank 2, and a negative definite lattice form for the standard $\Omega$ (`check_two_forms.py`). So a statement about one form transfers to the other only through $\Omega_+$, which is of type $\Phi_+$ by construction.

## 3. The functional-equation pairing $\Omega_{\rm FE}$ as ζ's symplectic datum

**What 04t states.** The claim is `thm:fe-pairing-jets` (04t:42-64), status proved, unconditional; its db dependency is `thm:model-space-jets`.
- **The space.** $H^1_{\rm fin}$ (04t:19-23) is the jet span of a finite set of zeros. The set carries full multiplicities and is closed under $\rho\mapsto1-\rho$ and $\rho\mapsto\bar\rho$.
- **Compatibility with the whole flow.** $\Omega(C_tx,C_ty)=e^{-t/2}\Omega(x,y)$ for **all** $t\ge0$, jet factors included. This follows from $D^T\Omega+\Omega D=-\tfrac12\Omega$ (b, line 54).
- **Rigidity.** Any all-time similitude pairs the root space of $\rho$ only with that of $1-\rho$. "A single time has phase aliases, all times are needed" (a). The normalisation $(-i\,\mathrm{sgn}\,\gamma)^m(-1)^j$ is a choice, so compatible forms have one free weight per pair.
- **Scope.**
  - On the bond, $\Omega_{\rm FE}$ is a finite-rank biorthogonal form, consistent across nested sets.
  - Its extension to the energy completion is not asserted, and Poisson inversion does not supply it (c).
  - "A canonical geometric cup pairing on the bond remains open" (d, line 63).

**Lane G's use**, at `zeta-ingredients.md` §3.1 and §5 item 2 (line 170).
1. "Compatible with the whole flow, but only on finite spans of zeros." This matches 04t.
2. Lane G works in the diagonal semisimplification over the first 3000 zeros, in evaluation coordinates, not on full jets. That is 04t's second space (`prop:weil-form-not-metric`(c)), where 04t places "the pairing and star" too. The difference from the full-jet setting is harmless numerically, since the zeros used are simple.
3. "Two multiplicatively independent steps force the diagonal form." This is the discrete version of 04t (a)'s "all times are needed", and it is sharper: two primes remove every phase alias on any finite set.
4. Lane G's prime steps are the samples $C_t$ at $t=2\log p$, up to the direction convention ($M_a$ has multiplier $a$, while $C_t$ has $e^{-t/2}$). 04t's sign convention only flips $J\to-J$ (`family-vacuum.md` §3).
5. Lane G and the review add a second form, $\Omega_D=B(\cdot,D^{-1}\cdot)$.
   - It is compatible with every $M_a$ on the test algebra ($\hat k(\tfrac12)=0$) before RH. This was checked for $a=2,3,5$ with an off-line quartet.
   - **It is not registered.**
   - It is built from $B$, so it is not an independent geometric datum. 04t (d)'s open "canonical geometric cup pairing" is not answered by it.

**The contradiction already corrected.** The 245-line `data-ladder.md` §4 item 2 said "what ζ lacks is … one $\Omega$ for the whole commuting family of prime steps". Read literally, it is false by `thm:fe-pairing-jets`. The current text (lines 141–146) says the opposite, with $\Omega_{\rm FE}$ and $\Omega_D$ (review S2b).

## 4. "Nothing supplies a polarisation for ζ" (04t) against "a global integral structure plus a reason for positivity" (today)

There is no single registered sentence "nothing supplies a polarisation for ζ". 04t's version of the gap is spread over four places:
- `thm:fe-pairing-jets`(d), 04t:63: "a canonical geometric cup pairing on the bond remains open";
- `thm:no-energy-equivalent-metric`, 04t:88-97: "this obstructs the specified channel realisation, not an unspecified cohomology";
- `prop:weil-form-not-metric`(b, d), 04t:146-148 and 158-159: "a trace selects no metric … a zero-free positive geometric comparison is what is open";
- `obs:deninger-bond-next`, 04t:211-220, sketched: "the functional equation supplies the pairing but not a cup product; the trace formula does not select the metric; the finite LPS model has both because of an arithmetic surface".

04q adds `obs:deninger-same-gap` (04q:226-244) and `thm:deninger-invariant-polarisation`(v): "$B$ removes the cone's freedom only when $B$ is canonical".

Today's version is `data-ladder.md` §4 items 1–2 (lines 123–146) and §4b (178–191): "an integral structure on the cokernel on which the steps act", plus "a reason for the family-invariant point $B$ to be positive", i.e. for $\omega$ to be a state.

| aspect | registered | today | relation |
|---|---|---|---|
| RH as a positive invariant structure | `thm:bond-positive-metric-criterion`, `prop:weil-form-not-metric`(a) | the vacuum, the cone, $B$ | **coincide** |
| what is missing for positivity | "a zero-free positive geometric comparison" (04t:159); "a cup product" (04t:217); LPS "has both because of an arithmetic surface" (04t:218) | "a reason for $\omega$ to be a state"; "in every understood case with global zeros that reason is geometric and carried by the lattice" (ampleness of Θ) | **coincide**, in different words. Both say the reason is geometric and is absent for ζ. |
| the symplectic datum | present on finite spans (`thm:fe-pairing-jets`); not canonical | present ($\Omega_{\rm FE}$, $\Omega_D$); explicitly *not* the missing item (S2b) | coincide; today is more explicit that $\Omega$ is not what is missing |
| canonicity of $B$ | "the notebook has a canonical $B$ only on the genus-one Hodge ket" (04q:237-238); (v) | lane E: the principal form $\Omega_{\rm can}$ on $\mathbb Z[F,V]$ is canonical only up to the real unit orbit, which is infinite for $g\ge2$, so it does not remove the cone's freedom | today **confirms** (v) with a computation; 04w `prop:no-rational-symmetric-marking` already had the unit rescaling |
| **integrality** | absent from 04q and 04t; appears only in 04w `obs:bond-h1-comparison-open` (ideal classes of $O_K$, a marked lift) | an item of its own: a lattice with an integral step, finite rank per mode; the polarisation decides integrality, not RH (lane E) | **today is more specific**: it separates integrality from positivity |
| where the datum cannot come from | the trace selects no *metric* (`prop:weil-form-not-metric`(b)); prime-by-prime ansätze are blind (`obs:prime-by-prime-blind`, 10:97-106, sketched) | counts do not fix the *lattice* (class number; lane A). Overlaps see the order, not the class (lane F). Local data do not fix global zeros (lane C). The tower is blind (lattice-tower §4). The code lattice $\mathbb Q^2$ cannot serve (S2a). | today is **more specific**. "Counts do not fix the lattice" is the integral analogue of 04t's "the trace does not fix the metric", and it follows from `cit:latimer-macduffee` (06c:101-111) and `cit:lenstra-structure` (06c:93-99). |
| phase data | `obs:spt-protection-is-sign-data` (10:112-127, sketched): "root numbers as products of local epsilon-factors … RH is modulus data … SPT-type protection cannot deliver it" | gate phases (lanes I, J): the product of local Fourier-gate phases is the root number; they coexist with a positive Weil form and do not carry RH | same statement; today supplies checked instances (49a1/441d1; six characters of $\mathbb F_q(t)$ and a census of 532) |
| the analytic side | `thm:no-energy-equivalent-metric`, `thm:rescaled-semigroup-unbounded`, `prop:unit-coefficient-form`: obstructions on $K_S$ | only the window finding (residual ≈ 0.4; lane G §3.2) | **04t is more specific**. The window residual parallels `num:deninger-bond`'s energy-Gram residual 0.4956 (04t:202) for a different form; neither implies the other. |

**Verdict.** On positivity, today and 04t state the same gap. Today adds an integrality half, together with a list of excluded sources (counts, overlaps, local data, gate phases, tower, code lattice). 04t adds analytic obstructions on $K_S$ that today's pages do not touch. Neither contradicts the other.

## 5. "$K_S$ is not Deninger's $H^1$" (04q) against "two levels: local and global" (today §3)

The registered claims are:
- `thm:ks-not-deninger-h1` (04q:186-206, proved): no inner product equivalent to the Hardy one makes $Z_t$ normal with the kernels as eigenvectors, because the Carleson condition fails;
- `obs:deninger-same-gap` (sketched).

Today's version is `data-ladder.md` §3 (lines 92–110), as corrected by review S1. Each finite case has two readings:
- as a reduction, it is the local level over $\mathbb Q$, where its zeros are poles of an Euler factor;
- as a global field, its zeros are eigenvalues of an integral step on a finite-rank $H^1$.

The question for ζ is "what plays $H^1$ of the function field for the global zeros".

- **Where they coincide.** Both say that the notebook's global space for ζ is not an $H^1$ carrying a positive invariant structure with the zeros as eigenvectors. 04q puts the defect in the inner product on a given space ($K_S$ exists, but its geometry is wrong). Today puts it in the missing integral object.
- **Registered statements of today's local-level facts.**
  - `prop:deninger-suspension-ring`(b) (04q:99-118, proved): a product leaf space admits a common exponent only at $\rho=0$.
  - `obs:prime-by-prime-blind`: partial Euler products have no zeros.
  
  These are the registered form of "for ζ the local level is empty of zeros". Review S1 notes that this holds for every $L$-function.
- **The converse direction.** `prop:deninger-local-coefficient`(c) (04q:120-132, proved) says one rotation angle per prime is "data the explicit formula never sees", so the global object does not see local angles. Lane C shows the converse: the local data (lattice, vacuum, steps up to sign) do not fix the global zeros. The two together make local and global mutually underdetermined. Neither is registered as a pair.
- **What today adds.**
  - The function-field reading as the global model: lane J, and `analytic.md` §14, which is unregistered.
  - The discrete-against-continuous step group as the real divide (S1).
  
  04q has the second implicitly: the prime letters as "one flow sampled at $\log p$" (04q:238-239).

Verdict: the same gap seen from two sides, analytic in 04q and structural today. No conflict.

## 6. The CM torus (04t) against lane C (one lattice, one vacuum) and lane M (shared vacua)

The registered claim is `thm:cm-torus-class-group-bond` (04t:175-195, proved). Its four parts:
- (a) $z\mapsto\alpha z$ on $\mathbb C/\mathbb Z[i]$ preserves $\Omega_T$, $J_T$ and $G_T=\Omega_TJ_T$ up to $q$, with "positivity from the geometry, without an eigenvalue bound".
- (b) At each split $p\equiv1\pmod4$ the Frobenius of $y^2=x^3-x$ is the primary $\pi$, "up to the choice of prime above $p$". The other associates are the quartic twists.
- (c) Equality of zeta functions, "not an identification of underlying spaces".
- (d) The metric cone is one ray (vacuous).

| today | registered counterpart | relation |
|---|---|---|
| lane C: one lattice $\mathcal O_K$ and one vacuum $J_K$ for every split prime, so local RH is free (`cm-lift.md` lines 12, 181) | (a) and (b) for $K=\mathbb Q(i)$. Every $\pi_p$ acts on the same $\mathbb C/\mathbb Z[i]$ with the same $J_T$. | **states the same** for $\mathbb Q(i)$, prime by prime. The family statement is implicit in 04t. |
| twists share lattice, vacuum and local steps up to a unit | (b): "other associates are the Frobenii of the quartic twists" | **states the local half** |
| 49a1 and 441d1 have different global zeros (lane C); the difference sits in the gate phase at a ramified place (lane I) | not registered. 04t has no global $L(\psi,s)$. In (b) the associate is pinned by a congruence at the ramified prime $1+i$. That is the 04t analogue of lane I's charged local state, by my reading (*heuristic*). | **today states more** |
| §4b: the Weil form of $\psi(\mathfrak p)$ is $\mathrm{Im}\,\psi(\mathfrak p)\,G_{J_K}$; it is orientable with one prime per $p$ (S3b) | (b)'s "up to the choice of prime above $p$" is the choice that fixes the sign of $\mathrm{Im}\,\pi$ (the examples have $b=2,2,4>0$) | consistent with the corrected §4b; it undercuts the 245-line version |
| lane A: in genus one the Rosati form is the vacuum form times $\sqrt{4q-a^2}$ | (d): one ray, vacuous; `obs:gl1-bond-no-metric` (04p:112-122) | **same** |
| lane F: the overlaps see $\mathrm{End}$, not the class | (c): "$h$ is not the Gaussian class number". Here $\mathrm{End}=\mathbb Z[i]$ has class number 1, so by `cit:lenstra-structure` the fixed-point groups $\mathbb Z[i]/(\pi^n-1)$ are $E(\mathbb F_{p^n})$ as $\mathbb Z[i]$-modules. | consistent. Today makes (c)'s caution precise: it is needed only when $\mathrm{cl}(\mathrm{End})\ne1$. |
| lane M: commuting similitudes of one $\Omega$ share a vacuum iff each satisfies RH; one-mode steps of different norms never commute | (a) is an instance: all $\alpha\in\mathbb Z[i]$ lie in $\mathbb R[J_T]\cong\mathbb C$, and RH is automatic. `prop:deninger-suspension-ring`(c) (04q:114-117) is the $\ell^2(\mathbb N)$ (Bost–Connes) version: a metric making every $p^{-1/2}F_p^*$ unitary forces orthogonality except for $\rho+\bar\rho'=1$. | consistent. Lane M's general criterion is new. |
| lane M: the LPS vertex pair $A_{13}$, $A_{17}$ has no shared vacuum, and both Weil forms are positive | 04u registers only $T_{17}$ on $K\oplus K$ (`thm:lps-bass-frobenius`, `prop:lps-metric-cone`). Lane M works at vertex level (`family-vacuum.md` §2). | a different space; no conflict; new |

## 7. Registered claims tested against today's negative findings

| claim | where | status | statement (quoted or condensed) | today's finding that bears on it | affected? |
|---|---|---|---|---|---|
| `thm:toral-frobenius-count` | 06d:18-27 | proved-cond. (db: proved) | "$N_n=\lvert O/(\pi^n-1)O\rvert$ … which under `cit:lenstra-structure` is the point group $E(\mathbb F_{q^n})$ itself as an $O$-module" | counts do not fix the lattice class (lane A) | **no**: the statement is class-independent; `def:lifted-frobenius-torus` (02g:40) takes $\Lambda$ to be any proper $O$-ideal |
| `prop:theta-functional-bond-state` | 04p:50-62 | proved | "$\Theta(x1_{O_A})=q^{h^0(\mathrm{div}\,x)}$" | lane F: these overlaps see the order, not the class | **no**: lane F builds on it |
| `prop:deninger-elliptic-hodge-ket` | 04q:171-184 | proved-cond. (db: proved) | ordinary $E$ with a CM lift; "Deninger takes the maximal order" | lane A: the class is free; lane B: non-ordinary has no canonical lift | **no**: the identifications are over $\mathbb C$ and class-independent; non-ordinary curves are outside its hypothesis |
| `thm:elliptic-ph-unitary` | 06d:73-88 | proved-cond. (db: proved) | "$a^2<4q$ from the positive definite degree form $m^2+amn+qn^2$" | lane A: the vacuum form is that degree (Casoratian) form divided by $\sqrt{4q-a^2}$ | **no**; consistent |
| `thm:rosati-ph-genus-two` | 06f:224-240 | proved-cond. (db: proved) | the PH models "agree up to positive weights and the CM type" | lane E: Rosati is not proportional to the vacuum (10.870, 20.171); the CM type decides the sign of the Weil form | **no**; lane E quantifies it |
| `obs:deninger-same-gap` | 04q:226-244 | sketched | "the notebook has a canonical $B$ only on the genus-one Hodge ket" | 04w's $E_0$ and lane E's $\Omega_{\rm can}$ are integral unimodular compatible forms in genus two | **dated, not weakened**: canonical only up to the unit orbit, so (v)'s point stands |
| `thm:lps-bass-frobenius`(c) | 04u:82-99 | proved | "$G>0$ iff $\lVert T\rVert<2\sqrt{17}$" | lane E: a positive Weil form needs $\Phi_+$; $M'$ is a counterexample | **no**: $G$ is the Weil form of $\Omega_B$, which has every Krein sign $+1$ |
| `thm:weil-positivity-finite`, `thm:kraus-weil-criterion`, `obs:huang-boundedness` | 08b:50-56, 159-171; 08c:221-232 | proved | Weil positivity of the trace sequence is the one-sided bound; Huang's $h_k\ge0$ is its boundedness form | lattice-tower §4: "the tower is blind"; $M'$ | **no**. These concern the trace form, which is orientation-blind. "The tower is blind" refers to its structure (codes, Cliffords, places); its *sizes* $h_k/q^k$ decide RH (lattice-tower §4 table), in agreement with these claims. |
| `obs:prime-by-prime-blind` | 10:97-106 | sketched | "no prime-by-prime ansatz can see [zeros]" | lane C: local data up to sign do not fix the global zeros | **no**; same direction |
| `obs:spt-protection-is-sign-data` | 10:112-127 | sketched | phase data are protected, RH is modulus data | lanes I, J: gate phases give the root number and do not enter positivity | **no**; supported with instances |
| `prop:weil-form-not-metric`(b) | 04t:146-148 | proved | "the explicit formula cannot select all weights one" | lane G: "$B$ is the vacuum point of $\Omega_{\rm FE}$" | **no**. The claim limits lane G's phrase (G3), not the other way round. |
| `thm:fe-pairing-jets` | 04t:42-64 | proved | one all-time compatible pairing on finite spans | the 245-line §4 item 2 "ζ lacks one $\Omega$ for the family" | **no**. The claim was right, and the page has been corrected (S2b). |
| `thm:cm-torus-class-group-bond`(c) | 04t:186-188 | proved | "not an identification of underlying spaces" | lane F, Lenstra | **no** (see §6) |
| `thm:arithmetic-metric`, `obs:gl1-bond-no-metric` | 04l:157-176; 04p:112-122 | proved-cond.; proved | single ray at genus one; the test is vacuous | lane A, genus one | **no**; consistent |

I found no registered claim that says counts determine the metric or the lattice, that the tower sees RH, that local data determine the zeros, or that the Weil form for an arbitrary compatible form is positive under RH. The registered statements nearest to each of these say the opposite or are restricted correctly: `prop:weil-form-not-metric`(b), `obs:prime-by-prime-blind`, `thm:lps-bass-frobenius`(c) for $\Omega_B$ only, and `cit:latimer-macduffee`.

## 8. What would need to change in the shards if today's record were registered

### 8.1 Rows to add (proposed; none written)

Prerequisites are listed before the table. The proposed ids use a `gkp-` stem, which does not occur among existing ids.

| proposed id | kind | status | statement | proved or checked on | deps (registered) |
|---|---|---|---|---|---|
| `def:lattice-weil-form` | definition | – | for an integral step $M$ of norm $q$ on $(L,\Omega)$, $V=qM^{-1}$, the lattice Weil form is $W_\Omega=\tfrac12\Omega(\cdot,(M-V)\cdot)$; it is distinct from `def:weil-form` | `cone-bridge.md` §1 | – |
| `prop:gkp-vacuum-weil-form-cm-type` | proposition | proved | Hypotheses: squarefree characteristic polynomial and no real eigenvalue. (i) $M$ semisimple with $\lvert\mu\rvert=\sqrt q$ ⇔ (iii) an invariant vacuum exists. Moreover $W_{\Omega}=\sum_j\varepsilon_j\,\mathrm{Im}\,\alpha_j\,G_\Omega\vert_{V_j}$, so $W_\Omega>0$ ⇔ RH and $\Phi_\Omega=\Phi_+$. The map $\Omega'\mapsto W_{\Omega'}$ is an isomorphism from compatible forms onto similitude forms. $M'$ and $B\oplus2B^{-T}$ show that both hypotheses are needed. | `cone-bridge.md` Props 1–3; `lattice-tower.md` §5 corrected; lattice review; `check_cone_bridge.py` 42/42 | `thm:deninger-invariant-polarisation`, `prop:genus-two-metric-cone`, `thm:lps-bass-frobenius` |
| `thm:gkp-genus-g-bridge` | theorem | proved | On $\mathbb Z[F,V]$, $e=1$: (1) $\Omega_+=\mathrm{Tr}(x\bar y/(V-F))$ is integral, of type $\Phi_+$, with determinant $\mathrm{disc}(h)^2$, and $W_{\Omega_+}=\tfrac12\mathcal T_L$. (2) $\Omega_{\rm can}=\mathrm{Tr}(x\bar y/\mathfrak d)$ is principal, with alternating Krein signs, so it is never $\Phi_+$ for $g\ge2$. (3) $\mathcal T_L=\sum_j\lvert h'(\lambda_j)\rvert\sqrt{4q-\lambda_j^2}\,G_{\Omega_{\rm can}}\vert_{V_j}$. For the $\mathbb F_5$ curve this gives 10.870 and 20.171, with ratio $R_0$. | `cone-bridge.md` Thm 5; K3–K4, R6–R9 | `thm:genus-two-cm-reference`; a `cit:` row for the trace dual of a monogenic tower |
| `prop:gkp-rosati-cone-orbit` | proposition | proved | The Rosati form transported by a cyclic vector is $\sum_j\lvert\varphi_j(\zeta_e)\rvert^{-1}G\vert_{V_j}$. It sweeps the open cone as $e$ varies, and integral generators move it along the real unit orbit (infinite for $g\ge2$). | `cone-bridge.md` Prop 4; U1–U2, G10 | `prop:no-rational-symmetric-marking` |
| `thm:gkp-genus-one-bridge` | theorem | proved | The unimodular $S$ carries the Riemann–Roch cokernel state to $\mathbb Z[F]$, and $\Omega(Ss,JSs)=2\mathcal Q(s)/\sqrt{4q-a^2}$. On a non-principal lattice the smallest integral intertwiner has determinant 2. | `curve-bridge.md` §5; lattice review | needs `analytic.md` §13 (Casoratian) registered first; `thm:elliptic-ph-unitary` |
| `num:gkp-counts-not-lattice` | numerical | numerical | At $q=7$, $a=2$, two curves have equal counts, equal $E(\mathbb F_{7^k})$ for $k\le24$, and non-isomorphic Deligne modules | `curve-bridge.md`; `check_curve_bridge.py` | `cit:latimer-macduffee`, `cit:lenstra-structure` |
| `prop:gkp-overlaps-see-order` | proposition | proved-conditional | The overlap function $D\mapsto q^{h^0(D)}$ at all levels determines $E(\bar{\mathbb F}_q)$ as a $\mathbb Z[\pi]$-module, up to Frobenius-compatible relabelling. Two such modules are isomorphic iff $\mathrm{End}(E)=\mathrm{End}(E')$. So the overlaps see the order, not the class; the Weil pairing sees the class. | `overlap-data.md` Thm 2, Prop 3; lattice review | `prop:theta-functional-bond-state`, `cit:lenstra-structure` |
| `prop:gkp-cm-local-not-global` | proposition | proved; numerical part | 49a1 and 441d1 share $\mathcal O_K$, $J_K$ and every split-prime step up to sign ($p\ne3$), and have different zeros (441d1 has a central zero) | `cm-lift.md`; `check_cm_lift.py` 50/50; arithmetic review | `thm:cm-torus-class-group-bond`, `obs:prime-by-prime-blind` |
| `prop:gkp-gate-phases-root-number` | proposition | proved; checked | The root number is the product of the local Fourier-gate phases. For Dirichlet characters of $\mathbb F_q(t)$ the phases $\chi_P(P)G_P/\sqrt Q$ multiply to $W$ and coexist with a positive Weil form. | `gate-phases.md` (I); `ff-dirichlet.md` (J) | `obs:spt-protection-is-sign-data` |
| `prop:gkp-commuting-shared-vacuum` | proposition | proved | Commuting similitudes of one $\Omega$ share a vacuum iff each is RH. One-mode steps of different norms never commute and generate an unbounded normalised group. For the LPS vertex pair both Weil forms are positive and the vacua differ. | `family-vacuum.md`; 39/39 | `thm:deninger-invariant-polarisation`, `thm:lps-bass-frobenius` |
| `prop:gkp-zeta-prime-steps` | proposition | proved (spectral model), numerical (signs) | In the diagonal semisimplification: forms compatible with two independent dilations are diagonal. The $\Omega$-Weil form of $M_p$ has weights $w_\gamma\sqrt p\sin(\gamma\log p)$. No compatible $\Omega$ makes $M_2$ and $M_3$ both positive; the signs already disagree at the first zero, and on 50.1% of 3000. $B$ is invariant under every step. $\Omega_D=B(\cdot,D^{-1}\cdot)$ is compatible with every step before RH, with Williamson weights $\lvert\gamma\rvert$. | `zeta-ingredients.md` §3.1; `family-vacuum.md` §3; ζ review G3, S2b, S3b | `thm:fe-pairing-jets`, `thm:bond-positive-metric-criterion`, `prop:weil-form-not-metric` |
| `num:gkp-window-prime-step` | numerical | numerical (negative finding) | The compressed dilation by 2 on the CCM window has residual near 0.4 for $N\le160$ and $x\in\{13,100\}$. It is a similitude only on functions supported in $[0,L-\log2]$. $Z_N\mp P_N$ have inertia $(n-1,1,0)$, and each off-line pair adds one. | `zeta-ingredients.md` §§3.2, 4; ζ review G4 | `obs:window-is-compression` (08g:52) |
| `obs:gkp-tower-blind` | observation | proved/checked | The GKP tower (period-$k$ syndrome codes, logical Cliffords, places) exists for every integral step of norm $q$. Its sizes decide RH; its structure does not. | `lattice-tower.md` §4; `check_lattice_tower.py` | `thm:weil-positivity-finite` |
| `obs:gkp-two-readings` | observation | sketched | Each finite case has a reduction reading (the local level over $\mathbb Q$) and a global-field reading (global zeros on a finite-rank $H^1$). The oscillator reading holds wherever the step group is discrete. | `data-ladder.md` §3; ζ review S1 | `prop:deninger-suspension-ring`, `thm:ks-not-deninger-h1` |
| `obs:gkp-missing-datum` | observation | sketched | For ζ the steps, the adjoints, the compatible forms and the invariant point $B$ exist. What is absent is an integral structure with a step on the cokernel, and a reason for $\omega$ to be a state. Counts, overlaps, local data, gate phases, the tower and the code lattice are excluded as sources. | `data-ladder.md` §§4, 4b | `obs:deninger-same-gap`, `obs:deninger-bond-next`, `prop:weil-form-not-metric`, `obs:spt-protection-is-sign-data` |

**Prerequisites before any of these rows is written** (`data-ladder.md` §6):
- the REFUTE review of `family-vacuum.md` (lane M) and of `ff-dirichlet.md` (lane J). Neither has a review file in `notes/reviews/`; my check found `adelic-gkp-{lattice,arithmetic,zeta}` only. `gate-phases.md` (lane I) is covered by the arithmetic review;
- the byte-citations of `citations-2026-10-06.md` carried into `cit:` rows. This covers Deligne, Howe, Centeleghe–Stix, Lenstra (already `cit:lenstra-structure`), Shimura–Taniyama, and Euler's lemma on trace duals.

Lanes B and D (`no-lift.md`, `zn-flux.md`) were not cross-checked here.

### 8.2 Wording precisions

**In registered claims.** None is required. Three are optional:
- `obs:deninger-same-gap` (04q:237-238). After "only on the genus-one Hodge ket", add "(in genus two the principal Riemann form of `thm:genus-two-cm-reference` is canonical only up to the real unit orbit, `prop:no-rational-symmetric-marking`, so (v) still applies)".
- `thm:lps-bass-frobenius`(c) (04u:93-98). Add the identity $G=\tfrac12\Omega_B(F_1-V_1)$. That makes it the registered $\Phi_+$ instance of the proposed `prop:gkp-vacuum-weil-form-cm-type`.
- `def:weil-form` (02b:249). A one-line cross-reference to `def:lattice-weil-form` and to the identity of §2.3: on a window of length $2g$, the trace form is $2W_{\Omega_+}$ under the cyclic vector.

**In today's pages, before registration.**
- `lattice-tower.md` §5: "the abstract form is `thm:deninger-invariant-polarisation`" should become "of (i)⇔(iii); (ii) is lane E's".
- `data-ladder.md` §4 item 2, line 139: after "vacuum point", insert "(in the evaluation normalisation; in general: invariant under every step, review G3)".
- `data-ladder.md` §4b, line 178: $\{\rho,1-\bar\rho\}$ should be $\{\rho,\bar\rho\}$.
- Use "lattice Weil form" wherever today's pages and 08b/08c could be read together.

### 8.3 Shard recommendation

**Recommendation: one new shard**, placed in the Phantasm series after 04z. A suggested name is `report/sections/04za_adelic_gkp_ladder.tex`. It would hold the rows of §8.1, with a short cross-reference paragraph pointing to 04q, 04t, 04u, 04w and 08b. I recommend against extending 04t or 08b, for three reasons.

1. **The object is different.**
   - 04t is a closed round about ζ's jets on the GL$_1$ bond. Its spaces are $H^1_{\rm fin}$, $K_S$ and $\ell^2$(zeros).
   - 08b is about the trace Weil form of an arbitrary transfer operator.
   - The ladder's core object is $(L,M,\Omega,J)$ with integrality, across curves, graphs, CM and function-field characters. Placing it in 04t would mix finite arithmetic into an analytic ζ shard. Placing it in 08b would put two "Weil forms" in one section without the cyclic-vector map that relates them.
2. **The dependencies point into the new shard.** Its rows depend on 04q, 04t, 04u and 04w. None of their rows needs to depend on it.
3. **One part could go either way.** The ζ part (`prop:gkp-zeta-prime-steps`, `num:gkp-window-prime-step`) could be an appendix subsection of 04t, since it uses 04t's $\Omega_{\rm FE}$ and its three spaces. I would still keep it in the new shard: its content is the family-against-step comparison, which only makes sense next to lanes C, E and M.

If the arithmetic part (lanes C, I, J) makes the shard too long, the natural split is a second shard for the local and global phase data, next to `obs:spt-protection-is-sign-data`.

## 8. Lanes B and D (cross-checked separately, Sonnet)

Author: `claude:sonnet-5.5`, 2026-10-06, lane T. This section was appended after lane O's page. It cross-checks `no-lift.md` (lane B) and `zn-flux.md` (lane D) against the registered record. Nothing else was changed, and nothing was registered, committed or pushed. The grep scratch is in `…/scratchpad/laneT/`.

**What was searched.**
- All of `db/claims.tsv` (638 lines) for: graded or $\mathbb Z_2$ Ramanujan; Pauli; Petersen; $K_5$; matching polynomial, Heilmann–Lieb or Haar/U(1) averages; twisted, voltage or Artin Ihara zetas; supersingular, Weil restriction, Deligne module, Deuring or Serre–Tate lifts, CM type; locks and half turns; `thm:toral-frobenius-count`.
- The five shards named in the brief. The db has rows for 03c, 08, 08h and 04u. It has **no row for 02h**: the definitions `def:graded-transfer-channel`, `def:graded-rh-fe-ramanujan`, `def:graded-quantum-expander`, `def:graded-hashimoto` and `def:index-two-grading` exist only in the shard.
- No registered row mentions Weil restrictions, Honda–Tate, Centeleghe–Stix, glued lattices, the matching polynomial, Heilmann–Lieb, U(1) or $\mathbb Z_N$ flux averages, or $\mathbb Z[\zeta_N]$. So those parts of lanes B and D are unregistered ground (see "Not registered" below).
- Statuses are the db statuses. The shard's derived status is added in brackets where it differs.

### 8.1 Claims that touch a statement of lane B or lane D

Lane B is `no-lift.md`, lane D is `zn-flux.md`. "Agrees" means the same statement, or an instance of the registered one. "States more" and "states less" are read from today's page.

| registered claim (db status) | statement (quoted) | touches | today's page |
|---|---|---|---|
| `thm:hashimoto-lift-metric` (proved) | "$G_C=\bigl[\begin{smallmatrix}1&\Sigma/2\\\Sigma/2&q\end{smallmatrix}\bigr]$ satisfy $C^*G_CC=qG_C$, $G_C$ positive iff the strict band $\lvert a\rvert<2\sqrt q$ … at an endpoint $C$ has a size-two Jordan block and no positive form unitarises the full band." | B §1, §3; D Prop. 2.1(4) | **Agrees.** The Weil form $\bigl[\begin{smallmatrix}q&A/2\\A/2&1\end{smallmatrix}\bigr]$ is $G_C$ in the other coordinate order, and the open-band criterion is the same. B and D state more (lattice, $\Omega$, integrality, the Galois orbit over $\mathbb Z[\zeta_N]$). The registered claim states more at the endpoint (Jordan block). D3 (no class has an eigenvalue on $\pm2\sqrt q$) makes that moot in their data. |
| `obs:rh-graph-ramanujan` (sketched) | "RH for the Ihara zeta holds iff $\lvert\lambda\rvert\le2\sqrt q$ for all nontrivial $\lambda$ (Ramanujan)." | B verdict; D §1, Prop. 2.1(4) | **Agrees, with a difference in the band.** The registered claim is the closed band, for the untwisted zeta. D's open band is the condition for *positivity of the Weil form* (a vacuum), which is the strict case of `thm:hashimoto-lift-metric`. D states more (twisted zeta; Galois-conjugate condition). D's headline "RH is again an invariant vacuum" needs the strict band; the registered endpoint remark is the reason. |
| `thm:qihara-general`, `cor:qihara-unitary` (proved; proved) | "$\det(1-uT)=(1-u^2)^{N(D-2)/2}\det(1-u\Sigma+(D-1)u^2)$" for $E_{\bar i}=E_i^{-1}$ | D §1 (check I1); B §1 | **Agrees (instance).** D's Ihara–Bass for a $\mathbb Z_N$ flux has exponent $\lvert E\rvert-\lvert V\rvert=n(q-1)/2$, the registered exponent for $D=q+1$. The scalar-phase twist is the one-dimensional case. |
| `thm:artin-voltage-decomposition` (proved); `obs:character-sector-grading` (sketched [sketched-conditional]) | "$\det(I-s_kT_k(u))=\prod_\rho\det(I-s_kT_{k,\rho}(u))^{d_\rho}$ … exponents $a_\rho$"; "the graded object computes the zeta of the cover (the Dedekind zeta of the cyclotomic field at level $N$), not zeta alone" | D §4 (C2), §5.2 | **Agrees.** D's "$\prod_\chi L(u,\chi)$ is the Ihara zeta of the $H_1/NH_1$ cover" is the abelian case ($a_\rho=1$). D's "$\prod_\chi L(s,\chi)=\zeta_{\mathbb Q(\zeta_N)}$" is the registered `obs:character-sector-grading` analogy. D states more (the explicit cover and counts). |
| `prop:oriented-half` (proved) | "no primitive … class is self-reverse … $\det(1-uH)=F(u)\overline{F(\bar u)}$ … $F$ is not the real square root in general ($E_1=i=-E_2$)" | D §1 ($L(u,\bar\rho)=L(u,\rho)$, coefficients in $\mathbb Q(\zeta_N)\cap\mathbb R$) | **Agrees (scalar-phase instance).** D's reversal argument is the registered one. D's "$\mathrm{charpoly}_{\mathbb Z}=P^2$" is a different squaring (over the lattice, from $\rho\leftrightarrow\bar\rho$), not the registered $F^2$ for Kraus letters, so there is no clash. |
| `lem:tree-matching-determinant` (proved) | "$p(z)=\sum$ over matchings $M$ of $(-z^2)^{\lvert M\rvert}\prod T_{ij}^2\prod_{\rm unmatched}(1+z^2-C_{vv})$" (weighted tree core) | D Thm 4.1 | **Agrees on trees only.** The matching expansion of $\det$ on a cycle-free graph is the registered lemma. D's theorem (average over $H^1(Y,\mathbb Z/N)$ equals the matching polynomial for every $N\ge2$) states far more and is **not registered**. |
| `thm:odd-letters-chiral` (proved); `obs:chirality-needs-all-odd` (proved); `prop:odd-sector-two-step` (proved); `obs:square-root-dictionary` (sketched) | "all letters odd … $\Gamma_c$ anticommutes with $H,J,\Sigma$ … spectra symmetric … $\det(1-uH_k)=\det_+(1-u^2K_k)$ … $\det(1-u\Sigma_k+qu^2)=\det_+((1+qu^2)^2-u^2a_ka_k^*)$ (equal block dimensions essential)"; "$\Gamma_c=L_P\otimes1$ anticommutes with $H$ iff every letter is odd" | B §1, §2, §3; D Locks (c) | **Agrees; states less than B on the arithmetic.** The spectrum symmetry $\lambda\leftrightarrow-\lambda$, $\det(x-M)=Q(x^2)$, and the factor $1+qu^2$ at $\lambda=0$ (roots $\pm i\sqrt q$) are B's half turn and supersingular mode. The Weil restriction from $\mathbb F_{q^2}$, Honda–Tate and the CM-type statement are not registered. "Equal block dimensions essential" fits B's remark that $K_5$ (odd $n$, $\lambda=0$ of odd multiplicity) is not a Weil restriction. `obs:chirality-needs-all-odd` only treats $\Gamma_c=L_P\otimes1$, so non-bipartite $K_4$ and $K_5$ with symmetric spectra do not contradict it. |
| `thm:deninger-invariant-polarisation` (proved) | "(iv) … unique for simple spectrum in $(0,\pi)$; for a repeated $e^{i\omega}$ with Krein signature $(p,q)$ the invariant polarisations form $\mathrm U(p,q)/(\mathrm U(p)\times\mathrm U(q))$, a point iff $pq=0$; at $\omega\in\{0,\pi\}$ the Siegel space" | B §3 ("unique when RH holds strictly … multiplicities allowed"), D Prop. 2.1(5) | **Agrees, but B's wording hides a hypothesis.** B's uniqueness with multiplicities is the case $pq=0$. It holds because $W>0$ makes the Hermitian form on each eigenspace definite. For a general compatible $\Omega$ with repeated eigenvalues, uniqueness fails. B and D have no real eigenvalues, so the Siegel clause does not arise. |
| `thm:lps-bass-frobenius`(c) (proved) | "$G>0$ iff $\lVert T\rVert<2\sqrt{17}$ strictly, the compatible metric is $\Omega_BJ=G/r(T)$ (not $G$)" | B §3 closed form of $J$; D Prop. 2.1(4),(5) | **Agrees.** D's $\Omega_{\mathbb Z}J=2W(4q-A^2)^{-1/2}=W/(\sqrt q\sin\theta)$ is the same identity, with $r=\sqrt q\sin\theta$. Same as lane O §1. |
| `prop:ccm-tn-pauli` (proved) | $E=\tfrac1{\sqrt5}\bigl[\begin{smallmatrix}0&-5\\1&-2\end{smallmatrix}\bigr]$, "$\TNmetric=\bigl[\begin{smallmatrix}1&-1\\-1&5\end{smallmatrix}\bigr]$ … positive and $E^*\TNmetric E=\TNmetric$" | B/D Weil form, $n=1$ | **Agrees (genus-one instance).** With $q=5$, $A=-2$ the lattice Weil form is $\bigl[\begin{smallmatrix}5&-1\\-1&1\end{smallmatrix}\bigr]$, the same form with the coordinates swapped. B and D do not mention the Pauli curve. |
| `num:graded-ramanujan`(a) (numerical); `prop:qubit-graded-zeta`; `prop:p-mode` (sketched) | "Pauli letters $X,X,Y,Y,Z,Z$ on $\mathbb C^{1|1}$ … $\operatorname{str}T^n=8,32,104,640,3208,15392$ = elliptic curve counts over $\mathbb F_5$, zeta $(1+2u+5u^2)/((1-u)(1-5u))$"; "$-2$ for the Pauli letters (inside the band)" | none | **Not affected.** Neither lane makes a statement about the Pauli six or those counts. B's $\#A(\mathbb F_2)=32$ for $K_4$ is a coincidence of numbers: a different object, a fourfold over $\mathbb F_2$. |
| `thm:graded-qihara-bass`, `cor:graded-band-circle`, `thm:graded-harrow` (all sketched); `obs:graded-ramanujan-status` (sketched); `def:graded-rh-fe-ramanujan`, `def:graded-hashimoto`, `def:index-two-grading` (02h; no db row) | "odd product of quadratics over the even product"; "retained NET divisor … lies on $\lvert u\rvert=q^{-1/2}$ iff every adjacency eigenvalue outside $\pm(q+1)$ with nonzero net multiplicity lies in the Hastings band"; "(HP) … $G$-unitary; equivalent to … diagonalisable with spectrum on the circle" | B and D, via the $\mathbb Z_2$ ($N=2$) flux | **Different object, no conflict.** The registered graded Ramanujan property is about Clifford-graded channels with $\mathrm{Ad}$ letters and net divisors. No registered row is about a signed graph or a flux class. The shapes agree: an odd-sector factor $\det(1-u\Sigma_1+qu^2)$, a band condition, and (HP) = semisimple with spectrum on the circle = B's and D's vacuum $J$. |
| `thm:toral-frobenius-count` (proved; shard proved-conditional) | "the toral endomorphism $M^n$ has exactly $\det(1-M^n)=\lvert1-\pi^n\rvert^2=N_{K/\mathbb Q}(1-\pi^n)=N_n$ fixed points … $N_n=\lvert O/(\pi^n-1)O\rvert$, which under `cit:lenstra-structure` is the point group $E(\mathbb F_{q^n})$ itself as an $O$-module." Deps: `asm:deuring-lift`, … | B §1 ($\#A(\mathbb F_q)=\det(1-M)$ = 32, 5184, 484) | **Agrees; not affected.** B's counts are $\det(1-M)$ for a step of dimension up to 20. I checked the three values from B's factorisations: $2\cdot4\cdot4$, $3^4\cdot4^3$, $4\cdot11^2$. They are the Weil-polynomial value at 1, not a consequence of the toral theorem. The registered theorem is genus one, ordinary, with a lifted torus. B's Petersen and $K_5$ have no canonical lift, so the theorem does not apply, and B makes no Lenstra module claim for them. |
| `cit:serre-tate-lift` (cited); `asm:deuring-lift` (assumed) | "an ordinary abelian variety over $\mathbb F_q$ has a canonical (Serre–Tate) lift … Frobenius lifts to an endomorphism of $T=H_1(A_{\mathbb C},\mathbb Z)$"; "an ordinary $E/\mathbb F_q$ with $\mathrm{End}=O$ lifts with its endomorphisms" | B §4, §5, §7 | **Agrees.** B: the ordinary part has a canonical lift (Deligne), the supersingular part does not ("no lift" should read "no canonical lift"). B's "Deuring lifting" is a different statement (a supersingular curve with one endomorphism), and the registered assumption is the ordinary case. The two names do not conflict, but they are easy to confuse. |
| `asm:supersingular-newton` (assumed); `thm:as-quadratic-supersingular`, `prop:as-finite-order` (proved) | "all Newton slopes 1/2 iff all its Frobenius eigenvalues are $\sqrt q$ times roots of unity" | B §2, §3 ($x^2+2$, $x^2+3$; $\pm i\sqrt q$) | **Agrees (instance).** B's supersingular blocks have $\pi=\sqrt{-2},\sqrt{-3}$, which are $\sqrt q\cdot i$, slope 1/2. |
| `asm:cm-hodge-type` (assumed) | "For a simple ordinary abelian variety of dimension $g$ … $K=\mathbb Q(\pi)$ is CM of degree $2g$, $\mathrm{End}\otimes\mathbb Q=K$ … CM type $\Phi$" | B §2, §6 | **Agrees on the part it covers; states less.** B's $S$ and $S'$ are simple ordinary surfaces with $K=\mathbb Q(\sqrt{-3},\sqrt5)$ and $\mathbb Q(\sqrt{-7},\sqrt5)$. The registered assumption says nothing for non-simple or non-ordinary varieties, so B's "the supersingular block selects no CM type" is outside it. |
| `prop:integral-marking-gauge` (proved [proved-conditional]); `cit:latimer-macduffee` (cited) | "its class is an ideal-lattice class of $\mathbb Z[\pi]$"; Latimer–MacDuffee for an *irreducible* characteristic polynomial | B §5 (glued lattice), D §2 | **Agrees; states less.** The registered classification is for an irreducible characteristic polynomial (genus one). B's and D's characteristic polynomials are reducible and repeated, so Latimer–MacDuffee does not apply as stated. Neither page claims a class. |
| `obs:abelian-obstruction` (sketched) | "Commuting holonomies produce uncontrolled invariants in tensor powers … any Ramanujan lift of the prime dilations must break commutativity by a quotient." | D (abelian $\mathbb Z_N$ holonomy; 26 of 27 Ramanujan for $K_4$, $N=3$) | **Different object, no conflict.** The registered claim is about $\mathrm{Ad}$ or tensor-power channels, where commuting unitaries have a large commutant. D twists the adjacency of a fixed graph by a one-dimensional character, where the base graph supplies the non-commutativity. A reader could take D's census as a counterexample. It is not one. |

### 8.2 Objects that share a name or a graph with lanes B and D, and are not affected

- `prop:cusp-ram-rh-independent` (04j, proved): "the 3-cube and the Petersen graph fail RH (moduli 0.882647, 0.900780 and 0.828751, 0.900342)". These are resonances of the cusp-graph renewal channel with $c^2=q+1$, not the Ihara zeta of the graph. Petersen with the trivial flux is Ramanujan (eigenvalues $3,1,-2$), which is consistent with D's census and with 08g. Lane B's "RH holds" for the dodecahedral flux concerns another object.
- `obs:rescaling-and-zeta`, `num:weil-window-extension` (08g): Petersen at $q=2$, untwisted. This agrees with D's $q=2$ correction.
- `num:selberg-letters` (03f): "the metric identity and its positivity exactly on the strict band, … graded Bass determinants" for Petersen and $K_4$. This is the registered instance of `thm:hashimoto-lift-metric`. It agrees with D and B on the strict band.
- `prop:pure-gauge-full-complex`, `num:a2-voltage-euler` (08f): pure-gauge twists are trivial. D works modulo coboundaries, so this is consistent.
- `prop:character-channel-graded-bond` (04o): function-field Dirichlet characters, where $L(u,\bar\chi)\ne L(u,\chi)$ in general. D §5.4's "the finite rung has no non-self-dual character" is meant for the graph rung. Read literally it overreaches, because the function-field rung does have such characters. Suggested wording: "the graph rung".
- `obs:deligne-ingredients`: about Deligne's proof of the Weil conjectures, not the ordinary-modules paper that B and D use.

### 8.3 Not registered (new relative to the record)

Lane B: the isogeny factorisations of the $K_4$, Petersen and $K_5$ fluxes; Weil restriction from $\mathbb F_{q^2}$ and its parity obstruction; the supersingular mode $J=M/\sqrt q$ and the equal $p$-adic valuations of $\mu$ and $-\mu$; the Centeleghe–Stix lattice; the glued lattice with gluing index $5^6$ and $5^2$; the twisted-form search ($K_5$ exists, Petersen none found in a subfamily). Lane D: the $\mathbb Z[\zeta_N]$ lattice and $\Omega_{\mathbb Z}$; Galois-Ramanujan; the no-lock-of-order-$N$ negative finding; the ordinariness rule; the flux-class census; Theorem 4.1 (the $N$-torsion average equals the matching polynomial, Heilmann–Lieb roots); the Euler-product cancellation. No registered row, and no registered claim in the five shards, bears on these.

### 8.4 Wording precisions for lanes B and D (none needed in the registered shards)

1. B §3 "unique when RH holds strictly": add "because the Krein form is definite, $pq=0$ in `thm:deninger-invariant-polarisation`(iv)".
2. D headline "RH is again an invariant vacuum": add "for the strict band; `thm:hashimoto-lift-metric` has a Jordan block at the endpoint".
3. D §5.4 "the finite rung has no non-self-dual character": read "the graph rung" (compare `prop:character-channel-graded-bond`).
4. B and D use "Weil form" for the lattice form $\tfrac12\Omega(M-V)$, as in §2.3 above. It is not `def:weil-form` of 02b.
5. D's graph "$L(u,\chi)$" is the pole-type object $1/\det$. The graded zeta of 03c puts the odd-sector determinant in the numerator (zeros). D §5.7 says this explicitly, but the two conventions should not be merged.

### 8.5 Verdict

**Contradictions found: no.** I read the db rows listed above (from two keyword greps of all 638 lines) and the shard text of 02h, 03c, 08, 08h and 04u. None states the opposite of a lane B or lane D statement.
- **Agreements and instances.** The registered claims that touch them are mostly agreements or instances: the strict-band Weil form (`thm:hashimoto-lift-metric`, `thm:lps-bass-frobenius`(c), `prop:ccm-tn-pauli`), Ihara–Bass with a voltage (`thm:qihara-general`, `thm:artin-voltage-decomposition`), orientation reversal (`prop:oriented-half`), the half-turn structure (`thm:odd-letters-chiral`), the uniqueness of the vacuum (`thm:deninger-invariant-polarisation`(iv)), and the ordinary lift, supersingular slope and CM-type assumptions.
- **States less.** The registered claims say less than B and D wherever B and D leave genus one or the ordinary case.
- **Different objects.** Three groups look similar but concern different objects: the graded Ramanujan family of 03c and 02h (Clifford-graded channels, no flux class); `obs:abelian-obstruction` (the $\mathrm{Ad}$ channel); and 04j's "Petersen fails RH" (renewal-channel resonances).
- **Pauli six.** The Pauli six, with counts 8, 32, 104, 640, and its elliptic curve are not touched by either lane. Their only link is that the genus-one lattice Weil form equals the metric of `prop:ccm-tn-pauli`.
- **`thm:toral-frobenius-count`** is unaffected: B's point counts are $\det(1-M)$ for non-ordinary varieties, outside that theorem's hypotheses.
- **Precisions.** The five precisions of §8.4 are for B and D. The first three are the ones a reader could mistake for a conflict. The matching-polynomial theorem and the Weil-restriction and Centeleghe–Stix material are unregistered.

The cross-lane checks I ran agree with lane O's: B and D give the same Weil form, the same vacuum formula and the same ordinariness rule. D4's $\det A$ at $N=2$ gives K_4 ordinary and Petersen not ordinary, as B finds.
