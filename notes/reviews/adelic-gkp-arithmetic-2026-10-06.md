# Adversarial review: the arithmetic lanes of the adelic-GKP session (`no-lift.md`, `cm-lift.md`, `zn-flux.md`, `gate-phases.md`)

- **Date:** 2026-10-06
- **Reviewer:** claude:opus-5.5 (REFUTE lane)
- **Authors under review:** claude:opus-5.5, lanes B (`no-lift.md`), C (`cm-lift.md`), D (`zn-flux.md`), I (`gate-phases.md`); orchestrator claude:fable-5.1
- **Files under review:** `notes/adelic-gkp/no-lift.md`, `cm-lift.md`, `zn-flux.md`, `gate-phases.md` (every statement labelled *proved here* or *checked*), and the headline claims that `notes/adelic-gkp/data-ladder.md` (§0 table, §2) takes from them. Labels B1–B12, C1–C9, D1–D9, I1–I8 are mine. S1–S3 are the synthesis sentences.
- **Independent numerics:** four scratch scripts `notes/reviews/scratch_gkp_arith_{nolift,cm,zn,gate}.py`, written from the *statements* only. None of `checks/check_{no_lift,cm_lift,zn_flux,gate_phases}.py` was opened or reused. Fluxes were rebuilt from the verbal descriptions ("one negative edge", "pentagon negative", an exhaustive search for the dodecahedral spectrum). The explicit formula was checked with my own Gaussian packets and my own archimedean term, using a prime side built from PARI's `ellap`, not from the Hecke character. The local epsilon factors were computed from Tate's integral $\int_{c^{-1}\mathcal O^\times}\chi^{-1}(x)|x|^{-1/2}\psi(x)\,dx$ by finite sums, not from the authors' gate identities. PARI/GP 2.15.4 was used, by subprocess.

**Headline.** The four lane pages hold up well. Every constant, sign, Gauss-sum normalisation and point count I attacked survived. I made two independent recomputations: the explicit formula, with packets I chose myself, closes to $10^{-15}$, and the local phases $(-i, i, -1)$ come out of Tate's integral directly. The one lane-page defect is an edge case: `zn-flux.md` Prop. 2.1(3) ("$\mathrm{charpoly}=P^2$, each mode twice") is false at $N=2$ and needs $N\ge3$.

The synthesis is weaker. It upgrades lane B's isogeny statement for $K_4$ to an equality of lattices, and that equality is **false**. The graph lattice of $K_4$ is glued at $p=2$ with index $2^4$ between the $E_2\times E_4$ block and the $S$ block. So the ordinary fourfold is *not* $E_2\times E_4\times\mathrm{Jac}(C)$, nor any product of varieties in those two isogeny classes. This is new information, and it partly answers `no-lift.md` §2's open question. Two further synthesis sentences misattribute the phase at 7 and overstate "every local step".

**Verdict counts: 37 VALID / 3 MINOR / 1 INVALID** (41 statements: 12 B, 9 C, 9 D, 8 I, 3 S).

---

## Part B — `no-lift.md`

### B1 — $K_5$ has $q=3$

**Claim (one line).** $K_5$ is 4-regular, so $q=3$; $K_4$ and Petersen have $q=2$.

**VERDICT B1: VALID**

- This is trivial, and it is used consistently: the band edge $2\sqrt3$ and the Weil form's smallest eigenvalue $0.500$ both follow from it.

### B2 — factorisations, RH, semisimplicity, point counts (N1–N3)

**Claim.** $\det(x-M)$ is $(x^2-x+2)(x^2+x+2)(x^4-x^2+4)$, $(x^2+2)^4(x^4-x^2+4)^3$ and $(x^2+3)(x^4+x^2+9)^2$. The Weil form is positive definite, with smallest eigenvalue $0.275, 0.275, 0.500$. $M$ is semisimple. $\#A(\mathbb F_q)=32, 5184, 484$.

**VERDICT B2: VALID**

- *Rebuilt from the words.* For Petersen I searched all $2^6$ cotree sign classes. Exactly **2 of 64** have $\mathrm{charpoly}(A_s)=x^4(x^2-5)^3$, as stated. $K_4$ with one negative edge and $K_5$ with the pentagon $0\!-\!1\!-\!2\!-\!3\!-\!4$ negative give $(x\mp1)(x^2-5)$ and $x(x^2-5)^2$.
- The integer factorisations of $\det(x-M)$ agree exactly. The squarefree part annihilates $M$ in all three cases, so $M$ is semisimple.
- The point counts $\det(1-M)$ are $32, 5184, 484$.
- The smallest eigenvalue of the Weil form, $\tfrac12\bigl((q+1)-\sqrt{(q-1)^2+\lambda^2}\bigr)$ at $\lambda=\sqrt5$, is $0.2753$, $0.2753$ and $0.5000$.

### B3 — Honda–Tate identifications and $p$-ranks (N5)

**Claim.** The factors are, in order, ordinary $E_2$, ordinary $E_4$, a simple ordinary surface $S$ with CM field $\mathbb Q(\sqrt{-3},\sqrt5)$, $E_{ss}$ ($\pi=\sqrt{-2}$), $S'$ with CM field $\mathbb Q(\sqrt{-7},\sqrt5)$, and $E'_{ss}$ ($\pi=\sqrt{-3}$). The $p$-ranks are 4, 6 and 4.

**VERDICT B3: VALID**

- *Recall.* I recall Honda–Tate exactly as stated, including the formula $\mathrm{inv}_v=\frac{v(\pi)}{v(q)}[\mathbb Q(\pi)_v:\mathbb Q_p]$, $\tfrac12$ at a real place, $P_A=m_\pi^e$, and $2\dim A=e[\mathbb Q(\pi):\mathbb Q]$.
- *Recomputed with PARI's `idealprimedec`/`nfeltval`.*
  - Slopes: $(0,1)$ for the ordinary factors; $\tfrac12$ for $x^2+2$ and $x^2+3$.
  - Invariants: all $\equiv0$, so $e=1$, for every factor over the prime field.
  - Over $\mathbb F_4$ and $\mathbb F_9$, the rational factors $y+2$ and $y+3$ have invariant $\tfrac12$, so $e=2$.
  - Discriminants of the quartic fields: $225=3^2 5^2$ and $1225=5^27^2$.
  - Explicitly, $x=\tfrac12(\sqrt5\pm\sqrt{-3})$ and $\tfrac12(\sqrt5\pm\sqrt{-7})$ are roots of $x^4-x^2+4$ and $x^4+x^2+9$.
- *$p$-rank* is the length of the horizontal initial segment of the Newton polygon. It is 4, 6 and 4. Petersen is $S^3\times E_{ss}^4$ with $p$-rank $3\cdot2=6$: neither ordinary (would need 10) nor almost ordinary (would need 9). Correct.

### B4 — Weil restrictions, $\det(x-M)=Q(x^2)$ (N6)

**Claim.** A symmetric spectrum gives $\det(x-M)=Q(x^2)$. $K_4\sim\mathrm{Res}(E_1\times E')$ and Petersen $\sim\mathrm{Res}(E'^3\times E_{-2}^2)$ from $\mathbb F_4$. $K_5$ is not a Weil restriction because $\deg Q$ is odd. $E'$ (trace 1) is not a base change.

**VERDICT B4: VALID**

- *The argument.* Frobenius on the induced module is $\bigl(\begin{smallmatrix}0&\rho(F^2)\\1&0\end{smallmatrix}\bigr)$, with characteristic polynomial $\det(x^2-\rho(F^2))=Q(x^2)$; I recall the same standard formula.
- *Its use.* $Q$ is uniquely determined by $\det(x-M)$, so "not a Weil restriction" for $K_5$ is correct: a degree-5 $Q$ cannot be $2\dim B$. "Is a Weil restriction up to isogeny" needs $Q$ to be the Weil polynomial of some $B/\mathbb F_{q^2}$, and that holds:
  - $y^2+3y+4$ and $y^2-y+4$ are ordinary over $\mathbb F_4$;
  - $(y+2)^4=\bigl((y+2)^2\bigr)^2$ with $e=2$, checked in B3.
- *Recomputed:* $Q=(y^2-y+4)(y^2+3y+4)$ and $(y+2)^4(y^2-y+4)^3$. The traces over $\mathbb F_4$ of base changes from $\mathbb F_2$ are $a^2-4\in\{-4,-3,0\}$, and $E'$ has trace $+1$. The point counts $8$ and $4$ are right.
- *Remark.* $y^2+3y+4$ is itself the base change of $E_2$ (and of $E_4$), so $\mathrm{Res}\,E_1\sim E_2\times E_4$. This is consistent with the page.

### B5 — Jacobians (N7)

**Claim.** Over $\mathbb F_2$ there are 768 smooth models. 16 of them have Weil polynomial $x^4-x^2+4$, among them $y^2+(x^2+x)y=x^5+1$ with counts $3,3,9,31$. None has $x^4+3x^2+4$. Over $\mathbb F_3$, 24 of 1296 models have $x^4+x^2+9$; one is $y^2=2x^6+2x^5+x^3+x+1$, with counts $4,12,28$.

**VERDICT B5: VALID**

- *Own brute-force counter over $\mathbb F_{2^k}$*, with explicit $\mathrm{GF}(2^k)$ arithmetic and the point at infinity from $Y^2+h_3Y=f_6$: counts $[3,3,9,31]$. The prediction from $x^4-x^2+4$ is also $[3,3,9,31]$.
- *Exhaustive search with PARI.* Smoothness was tested by `hyperelldisc` mod 2 and `poldisc` mod 3, with the Weil polynomial from `hyperellcharpoly`. Results: $768$ smooth, $16$ with $x^4-x^2+4$, $0$ with $x^4+3x^2+4$; $1296$ squarefree of degree 5 or 6 over $\mathbb F_3$, $24$ with $x^4+x^2+9$. My own counter for the $\mathbb F_3$ example gives $4,12,28$.
- The absence of a Jacobian in the class $E\times E^{\rm twist}$ over $\mathbb F_2$ is consistent with what I recall of Howe–Nart–Ritzenthaler; the exhaustive search makes the recall unnecessary.

### B6 — closed form and uniqueness of the vacuum (N8)

**Claim.** $J=(M-V)(D\oplus D)$ with $D=(4q-A_s^2)^{-1/2}$. It is the unique positive invariant complex structure when RH holds strictly.

**VERDICT B6: VALID**

- $D\oplus D$ commutes with $M$ because $D$ is a function of $A_s$, and $(M-V)^2=(A^2-4q)\oplus(A^2-4q)$.
- *Uniqueness.* On each eigenline pair the form $i\Omega(\bar v,v)$ is definite once the Weil form is positive. So the $+i$ eigenspace is forced. The argument is correct.
- *Numerically* (Petersen, $K_5$): $|J^2+1|\le2\times10^{-15}$, $|[J,M]|\le1.3\times10^{-15}$, and $\mathrm{sym}(\Omega J)>0$, with smallest eigenvalue $0.318$ and $0.378$.

### B7 — on $\ker(M^2+q)$ the vacuum is $M/\sqrt q$; self-lock; Deligne's rule selects no CM type (N9)

**VERDICT B7: VALID**

- *By hand.* $M^2+q=\bigl(\begin{smallmatrix}0&-A\\qA&A^2\end{smallmatrix}\bigr)$, so $\ker(M^2+q)=\ker A\oplus\ker A$. There $V(x,y)=(y,-qx)=-M(x,y)$, and $J=2M\,(4q)^{-1/2}=M/\sqrt q$.
- *Numerically:* $|(J-M/\sqrt q)|_{\ker(M^2+q)}|\le1.4\times10^{-15}$.
- $\mu=i\sqrt q$ and $-\mu$ generate the same ideal, so they have equal valuation $\tfrac12v(q)$ at the unique, ramified prime above $p$. This is literally the statement that the rule $\{\mathrm{val}_p\varphi(F)>0\}$ selects neither embedding.
- *Caveat on the gloss, not on the statement.* "No arithmetic $J$ on the supersingular block" (§6, labelled *negative finding/open*) is not proved. A polarisation of the variety, which exists, picks $J=\pm M/\sqrt q$ through $\omega(x,Jx)>0$. What is missing is a criterion that reads its sign off $(T,F,\omega)$, and the page says exactly this.

### B8 — Centeleghe–Stix hypotheses (N4) and the recalled theorem

**VERDICT B8: VALID**

- *Recall.* I recall the theorem the same way. The category of abelian varieties over $\mathbb F_p$ whose Frobenius avoids $\pm\sqrt p$ is equivalent to pairs $(T,F)$, with $T$ finite free over $\mathbb Z$, $F\otimes\mathbb Q$ semisimple with non-real $p$-Weil eigenvalues, and $V$ with $FV=VF=p$. The functor is $A\mapsto\mathrm{Hom}(A,A_w)$ for a pro-system $A_w$, so it is **contravariant** (an anti-equivalence). The page's "I do not trust my memory of its variance" is honest, and the variance does not affect anything on the page. Squarefreeness and ordinariness are not assumed; I recall the same.
- *The hypotheses* (prime $q$; no $\pm\sqrt q$ root; $V=qM^{-1}$ integral; $M$ semisimple) hold, as verified in B2.

### B9 — gluing index $5^6$, $5^2$; $L_{ord}$ is a Deligne module (N11)

**Claim.** $[L:L_{ss}\oplus L_{ord}]=5^6$ for Petersen and $5^2$ for $K_5$, with $\det\Omega|_{L_{ss}}=\det\Omega|_{L_{ord}}$ equal to the same. The variety is therefore not the product of its supersingular and ordinary parts. $(L_{ord},M)$ has characteristic polynomials $(x^4-x^2+4)^3$ and $(x^4+x^2+9)^2$, with middle coefficients $-25$ and $19$.

**VERDICT B9: VALID**

- *Recomputed with PARI `matkerint`.* Ranks $8+12$ and $2+8$; index $5^6$ and $5^2$; $\det\Omega$ on each block $5^6$ and $5^2$; middle coefficients $-25$ and $19$.
- *The inference "not a product" is sound,* and stronger than the page says. Suppose $(L,M)\cong(L_a,M_a)\oplus(L_b,M_b)$ with characteristic polynomials those of the ss and ord parts. The image of $L_a$ lies in $\ker(M^2+q)$ and the image of $L_b$ in $\ker h_{ord}(M)$, so the index would be 1. This uses only additivity of the equivalence, not exactness. So the variety is not isomorphic to **any** product $B_{ss}\times B_{ord}$ in those isogeny classes.
- The same test applied to $K_4$ gives a positive result that the synthesis contradicts; see S1.

### B10 — rank-2 sign uniqueness (proved here)

**Claim.** For a single supersingular elliptic factor exactly one of $\pm\Omega$ is a polarisation, because every alternating form on $\mathbb Z^2$ is compatible and the commutant has only positive determinants.

**VERDICT B10: VALID**

- The statement is true. "At most one" is automatic: $-\lambda$ is never ample. "At least one" holds because a principal polarisation exists and every unimodular alternating form on $\mathbb Z^2$ is $\pm\Omega$. The automorphism argument (norms $a^2+pb^2>0$) shows something else: the sign is not removable by an automorphism of $(T,F)$, so the question "which sign" is meaningful.
- The commutant is $\mathbb Z[F]$ only for the lattice at hand. For other lattices it can be the maximal order, e.g. $\mathbb Z[\tfrac{1+\sqrt{-3}}2]$ at $p=3$. Its norms are still positive, so nothing changes.

### B11 — no sign-changing unit in $R=\mathbb Q[A_s]\cap M_n(\mathbb Z)$ (proved here, N12)

**Claim.** $R=\mathbb Z[A_s]$ for Petersen and $\mathbb Z[A_s]+\mathbb Z\tfrac{A_s+A_s^2}2$ for $K_5$. In both, $p(\sqrt5)\equiv p(0)\pmod{\sqrt5}$, so the norm of a unit is $\equiv1\pmod5$ and is never $-1$.

**VERDICT B11: VALID**

- *The order, independently.* The Smith form of the $n^2\times3$ matrix of $\{I,A,A^2\}$ has elementary divisors $(1,1,1)$ for Petersen ($R=\mathbb Z[A]$) and $(2,1,1)$ for $K_5$ (index 2). A direct search for $(a+bA+cA^2)/m$ with $m\in\{2,3,5\}$ finds only $(A+A^2)/2$, for $K_5$.
- *The congruence* holds in $\mathcal O_{\mathbb Q(\sqrt5)}$ for both orders: $(\sqrt5+5)/2=\sqrt5\cdot\tfrac{1+\sqrt5}2$.
- *Unimodularity.* $\det C=p(0)^{m_0}N^{m}$, so it forces $p(0)=\pm1$ and $N=\pm1$. Hence $N\equiv1\pmod 5$, so $N=+1$, and $p(\sqrt5)$, $p(-\sqrt5)$ have the same sign. The proof is complete.

### B12 — the $K_5$ twist $C$; commutant ranks (N12)

**Claim.** The displayed $C$ is symmetric, has $\det C=-1$ and commutes with $A_s$. It is positive definite on $E(\sqrt5)$ and negative definite on $E(-\sqrt5)$. The Rosati-fixed commutant has rank 34 and 9, against 22 and 7 for the subfamily $C\oplus C$, and both ranks are 4 for $K_4$.

**VERDICT B12: VALID**

- $C$ commutes with *my* $A_s$ (pentagon $0\!-\!1\!-\!2\!-\!3\!-\!4$) without relabelling. 40 of the $5!\cdot2^5$ relabelings and gauges commute with it.
- The eigenvalues of $C$ are $\{0.043, 8.901\}$ on $E(\sqrt5)$, $\{-8.641,-0.303\}$ on $E(-\sqrt5)$, and $-1$ on $E(0)$. $\det C=-1$.
- *Ranks, by a dimension count rather than the authors' lattice computation.* The symmetric commutant of $A_s$ has dimension $\sum m(m+1)/2=6+6+10=22$ and $3+3+1=7$. The commutant of $M$ has dimension $\sum m^2$ over the distinct eigenvalues of $M$: $2\cdot16+4\cdot9=68$ and $18$. Hermitian-type fixed parts are half of that, 34 and 9. For $K_4$ the commutant has dimension 8 and the fixed part 4.
- I did not re-run the Petersen search for a unimodular sign-changing $C$. It is labelled *negative finding by search*, not a proof, and the page says so.

---

## Part C — `cm-lift.md`

### C1 — which curve (A1–A4)

**Claim.** 49a1 $=[1,-1,0,-2,-1]$, $a_2=+1$, reduces mod 2 to $y^2+xy=x^3+x^2+1$, the $\mathbb F_2$-twist of the E mode. 441d1 is the twist by $-3$, with conductor 441, $\varepsilon=-1$, rank 1, and it reduces to the E mode. The twist by 21 lies in the same class, the twist by 5 has conductor 1225, and the twist by $-7$ is 49a3.

**VERDICT C1: VALID**

- *PARI* (`ellidentify` of `elltwist`): the $-3$ twist is exactly **441d1**, the $21$ twist is 441d3, the $5$ twist has conductor 1225, and the $-7$ twist is 49a3.
- `ellrootno` gives $+1$ and $-1$. $L(1)=0.966656$ and $L'(1)=1.294559$. $a_2=+1$ and $-1$.
- 441d1 mod 2 is $[1,1,1,0,0]$ with $j=1$ and $a_2=-1$, so it is isomorphic over $\mathbb F_2$ to $y^2+xy=x^3+1$: one ordinary curve per trace, as the page says.
- *Remark.* "Every elliptic curve over $\mathbb Q$ with CM by $\mathcal O_K$ is a quadratic twist of 49a1 or of its isogenous 49a2" is true as a disjunction, but the second clause is idle. 49a2 has $j=255^3$ (checked) and CM by $\mathbb Z[\sqrt{-7}]$, not by $\mathcal O_K$. "Twist of 49a1" ($j=-3375$) suffices. This is not a defect.
- "441d1 lifts the E mode" is true but not unique: non-CM curves such as 15a also have $a_2=-1$. The page never claims uniqueness.

### C2 — $\psi((\alpha))=\varepsilon(\alpha)\alpha$, $a_p=(x|7)x$, theta series (A5–A7)

**VERDICT C2: VALID**

- *Sign conventions.* $\alpha=(x+y\sqrt{-7})/2\equiv x/2\pmod{\sqrt{-7}}$ and $(2|7)=+1$, so $\varepsilon(\alpha)=(x|7)$. Then $a_p=\varepsilon(\alpha)(\alpha+\bar\alpha)=(x|7)x$, which is invariant under $x\to-x$ because $(-1|7)=-1$. The infinity type is irrelevant for $a_n$, since the $a_n$ are real.
- *Against `ellap`:* 0 mismatches for all $p<10^4$ (608 split primes), for both formulas including the factor $(p|3)$ for 441d1. The representation $4p=x^2+7y^2$ with $x,y>0$ is unique in every case.
- *My own theta series* $\tfrac12\sum\varepsilon(\alpha)\alpha q^{N\alpha}$ (with $w\equiv4\pmod{\sqrt{-7}}$) agrees with `ellan` to $2.7\times10^{-15}$ for $n\le600$.

### C3 — the E mode is multiplication by $\mu=w-1$ on $\mathcal O_K$ (B3)

**VERDICT C3: VALID**

- By hand: multiplication by $w-1$ on $\{1,w\}$ is $\bigl(\begin{smallmatrix}-1&-2\\1&0\end{smallmatrix}\bigr)$, and $P^{-1}(\cdot)P=\bigl(\begin{smallmatrix}0&-1\\2&-1\end{smallmatrix}\bigr)=M$ with $P=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$.

### C4 — inert Frobenius is a quarter turn not compatible with $\mathcal O_K$; over $K$ the step is $-p$ (B4)

**VERDICT C4: VALID**

- $\psi((p))=(p|7)p=-p$ for inert $p$.
- A $K$-linear step with polynomial $x^2+p$ needs $\alpha=b\sqrt{-7}$, i.e. $p=7b^2$.
- An antilinear step has real eigenvalues.
- The proof is complete.

### C5 — the charge at 7 is forced by the parity of the $\ell=1$ state (proved here)

**VERDICT C5: VALID**

- The unit $-1$ fixes $\Theta_K$ and acts diagonally. The $\ell=1$ archimedean state is odd under it, so the overlap vanishes unless the finite part is odd.
- The instance $\sum_\alpha\alpha q^{N\alpha}=0$ is immediate from $\alpha\to-\alpha$. "Must sit at 7" is *sketched*, and I accept the sketch: quadratic characters of $\mathbb F_{p^2}^\times$ are even on $-1$.

### C6 — Mellin transform and functional equation of the overlap (C1–C3)

**VERDICT C6: VALID**

- $\int_0^\infty\sum a_ne^{-2\pi ny}y^{s-1}dy=(2\pi)^{-s}\Gamma(s)L(s)=\tfrac12\Gamma_{\mathbb C}(s)L(s)$, so the factor 2 is right.
- *Sign of the overlap functional equation.* With $f|W_N=\eta f$ and $\Lambda(s)=i^k\eta\Lambda(k-s)$ at $k=2$, one gets $f(i/(Ny))=\varepsilon Ny^2f(iy)$.
- *Numerically,* from PARI's $a_n$ ($n\le3000$) and my own sum, the relative error is $1\text{–}10\times10^{-31}$ for both curves at $y=0.9/\sqrt N$ and $1.3/\sqrt N$. With $-\varepsilon$ the relative error is 2.

### C7 — explicit formula with no zero-mode term, Hecke prime side (D0, D1)

**Claim.** $C_h(t)=-\sum\Lambda_E(n)n^{-1/2}[g(\log n-t)+g(-\log n-t)]+\frac1{2\pi}\int G e^{iEt}[\log N-2\log2\pi+2\mathrm{Re}\,\psi_\Gamma(1+iE)]$. Here $c(p^k)=2\cos k\theta_p$ (split), $i^k+(-i)^k$ (inert), and $0$ at bad primes.

**VERDICT C7: VALID**

- *Derivation.* With $\Lambda(s)=N^{s/2}\Gamma_{\mathbb C}(s+\tfrac12)L(s)$ (analytic $s$), the archimedean density is $\log N+2\mathrm{Re}(\Gamma_{\mathbb C}'/\Gamma_{\mathbb C})(1+iE)=\log N-2\log2\pi+2\mathrm{Re}\,\psi(1+iE)$, as stated.
- *Bad primes.* 7 for both curves and 3 for 441d1 are additive, so $a_{p^k}=0$ and $c=0$.
- *Test functions.* Real $c(n)$ make the formula valid for non-even $h$, which the page needs for $t\ne0$.
- *My own test.* Packets $h(r)=e^{-\tau^2(r-E_0)^2}e^{irt}$ with $(E_0,\tau)\in\{(15,.3),(40,.5),(2,.8),(0,1)\}$ and $t\in\{0,0.7,2.3\}$, 24 cases. The zero side uses PARI zeros up to $T=90$, both signs, and the central zero of 441d1 once. The prime side uses `ellap` (not the character) for $p\le4\times10^5$ with all prime powers. The archimedean side was integrated with mpmath.
  - Agreement: $|\Delta|\le1.2\times10^{-14}$ in 22 cases. The two cases with $\tau=1,t=2.3$ give $9.5\times10^{-14}$ and $2.7\times10^{-13}$. That is the size of my prime truncation, $e^{-(\log X-t)^2/4}$, not a defect.
  - The low packet $E_0=0$ closes with no zero-mode term. This confirms "no $2\cosh(t/2)$ pair".

### C8 — windowed Gram form PSD from the prime side; one off-line pair gives $-6.19$ (E1, E2)

**VERDICT C8: VALID**

- Not re-run. But note what it shows. Given C7, the prime-side Toeplitz matrix equals $\sum_\rho G(\gamma_\rho)e^{i\gamma_\rho(t_j-t_k)}$ with real $\gamma$ and $G\ge0$, and that is PSD term by term. So E1 adds no evidence for GRH beyond the PARI zero list. It is a consistency check of the explicit formula. The page does not claim more.

### C9 — same lattice and vacuum, different zeros (§3.4, proved here)

**VERDICT C9: VALID**

- $\psi'(\mathfrak p)=(p|3)\psi(\mathfrak p)$ at split $p$, and $\psi'((p))=\psi((p))$ at inert $p\ne3$, since $\chi_{-3}(p^2)=1$.
- The zero lists differ: PARI's first zeros are $3.457740\ldots$ against $0, 1.990687\ldots$.
- The page correctly restricts to $p\ne3$. The synthesis drops that restriction; see S2.

---

## Part D — `zn-flux.md`

### D1 — $q=2$ for $K_4$, cube and Petersen

**VERDICT D1: VALID** (all three are 3-regular).

### D2 — $L(u,\bar\rho)=L(u,\rho)$ (proved here)

**VERDICT D2: VALID**

- $A_{\bar\rho}=\overline{A_\rho}=A_\rho^T$ because $A_\rho$ is Hermitian, so the two have the same characteristic polynomial. That polynomial has real coefficients in $\mathcal O\cap\mathbb R$.
- *Numerically:* $\max|\mathrm{spec}(\rho)-\mathrm{spec}(\bar\rho)|=1.8\times10^{-15}$ over random fluxes on $K_4$, the cube and Petersen, for $N=3,5,7,8$.
- The Euler-product reading (orientation reversal) is also correct.

### D3 — Proposition 2.1 (similitude, $\Omega_{\mathbb Z}$, $\mathrm{charpoly}=P^2$, Weil form $\Leftrightarrow$ Galois-Ramanujan, vacuum)

**VERDICT D3: MINOR**

What holds:

- *Item 1.* $M^\dagger\Omega M=\bigl(\begin{smallmatrix}0&q\\-q&A^\dagger-A\end{smallmatrix}\bigr)$ is right. Numerically $|M^\dagger\Omega M-q\Omega|=10^{-16}$, and with the plain transpose the residual is $1.90$, as the page warns.
- *Item 2, built independently* (restriction of scalars in the power basis, $T_{ij}=\mathrm{Tr}(\zeta^{j-i})$):
  - $\Omega_{\mathbb Z}$ is integral and alternating, and $M_{\mathbb Z}^T\Omega_{\mathbb Z}M_{\mathbb Z}=q\Omega_{\mathbb Z}$ exactly;
  - $V$ is integral and $W$ is symmetric;
  - this holds for $K_4$ ($N=5$), the cube ($N=3$), $K_4$ ($N=4$) and $K_4$ ($N=2$).
- *Item 4.* "Positive definite iff every $A_{a\varphi}$ is in the open band" is correct. $\sigma(\bar z)=\overline{\sigma(z)}$ in the abelian CM field, and the Schur complement is $1-A^2/4q$. Exactly confirmed in the census (D6).
- *Item 5* is correct.

What fails: **item 3 at $N=2$.** At $N=2$ the group $(\mathbb Z/2)^\times$ has one element and $a=-a$, so the product has a single factor. For $K_4$ with one negative edge the integral characteristic polynomial is $(x^2-x+2)(x^2+x+2)(x^4-x^2+4)$, which is squarefree; my script reports "charpoly a square: False". The proposition, the §2 summary and verdict bullet 3 state the doubling without the restriction $N\ge3$. The page elsewhere mixes $N=2$ into the same tables: the $L^\perp/L$ table has an $N=2$ row, and the theorem is stated "for every $N\ge2$". Item 4's proof ($K\otimes\mathbb R\cong\mathbb C^{d/2}$, sum over a CM type) also presupposes $N\ge3$, although item 4's conclusion holds trivially at $N=2$.

- *Sentence at fault:* "3. $\mathrm{charpoly}_{\mathbb Z}(M)=\prod_{a\in(\mathbb Z/N)^\times}\det(x^2-A_{a\varphi}x+q)=P(x)^2$ with $P\in\mathbb Z[x]$." Also: "Each mode occurs twice in $L$, once for $\rho$ and once for $\bar\rho$", and the verdict bullet "every eigenvalue appears twice".
- *Corrected:* "3. $\mathrm{charpoly}_{\mathbb Z}(M)=\prod_{a\in(\mathbb Z/N)^\times}\det(x^2-A_{a\varphi}x+q)$. **For $N\ge3$** this is $P(x)^2$ with $P=N_{K^+/\mathbb Q}\det(x^2-A_\varphi x+q)\in\mathbb Z[x]$, and every mode occurs twice. For $N=2$ it is the single factor $\det(x^2-A_sx+q)$, which need not be a square." The synthesis row is unaffected, since it restricts to $N=3,4,5,6$.

### D4 — $L^\perp/L\cong(\mathcal O/\mathfrak D)^{2n}$; $N=4$ unimodular after $\delta=\tfrac12$; no scalar repair for $N=3,6$ (L0)

**VERDICT D4: VALID**

- $\det T=1,3,4,125$ for $N=2,3,4,5$, with Smith forms $(1)$, $(1,3)$, $(2,2)$, $(1,5,5,5)$. This gives logical dimensions per vertex of 1, 3, 4 and 125.
- The dual of $\mathcal O$ under $\mathrm{Tr}(\bar xy)$ is $\overline{\mathfrak D^{-1}}=\mathfrak D^{-1}$.
- For $N=3$, $\delta\in\mathbb Q$ with $\mathrm{Tr}(\delta\mathcal O)\subseteq\mathbb Z$ forces $\delta\in\mathbb Z$: $\mathrm{Tr}(1/3)=2/3$ and $\mathrm{Tr}(\zeta/2)=-1/2$.

### D5 — ordinariness $\Leftrightarrow N_{K/\mathbb Q}(\det A_\rho)$ prime to $p$; flux-independent for $N=p^k$ (D1, D4)

**VERDICT D5: VALID**

- *Proof check.* Modulo $p\mathcal O$, $\prod_a\det(x^2-A_{a\varphi}x+p)\equiv x^{nd}\prod_a\det(x-A_{a\varphi})$. The coefficient of $x^{nd}$ is $(-1)^{nd}N(\det A_\rho)$, and $p\mathcal O\cap\mathbb Z=p\mathbb Z$. The ordinary criterion is "the coefficient of $x^g$ is prime to $p$", which I recall the same way.
- *Against the exact integral characteristic polynomial:* 0 mismatches on 24 Galois-Ramanujan classes of $K_4$ ($N=3,4,5,6$).
- $\det A=-3$, $9$, $48$ from the spectra $3(-1)^3$; $3\cdot1^3(-1)^3(-3)$; $3\cdot1^5(-2)^4$. At $N=2$, $\det A_s(K_4)=5$ is odd and $\det A_s(\text{Petersen})=0$, consistent with `no-lift.md`.

### D6 — census table (§3)

**VERDICT D6: VALID** (for the rows I recomputed)

| graph, $N$ | classes | Ramanujan | Galois-Ramanujan | ordinary |
|---|---|---|---|---|
| $K_4$, 3 | 27 | 26 | 26 | 12 |
| $K_4$, 4 | 64 | 62 | 62 | 62 |
| $K_4$, 5 | 125 | 118 | 112 | 88 |
| $K_4$, 6 | 216 | 190 | 190 | 78 |
| cube, 3 | 243 | 242 | 242 | 162 |
| cube, 4 | 1024 | 993 | 993 | 993 |
| Petersen, 3 | 729 | 678 | 678 | 474 |
| Petersen, 4 | 4096 | 3914 | 3914 | 0 |

- All of these match. No eigenvalue lies within $10^{-9}$ of $\pm2\sqrt2$.
- $K_4$ at $N=3$ has four spectra with multiplicities 1, 12, 8, 6, and the characteristic polynomials match the page.
- The rows cube $N=6$ and Petersen $N=6$ were not recomputed.

### D7 — Theorem 4.1: $N$-torsion average $=$ Haar average $=$ matching polynomial for every $N\ge2$

**VERDICT D7: VALID**

- *The brief's question: is the grid average really the Haar average for every $N\ge2$, including the constant term and cross terms?* Yes.
  - The classes are parametrised bijectively by the product grid $\mu_N^g$ of cotree values, so the class average is the grid average.
  - In the Sachs expansion every term is a product, over the edge-disjoint cycles of an elementary subgraph, of $(z^{c_C}+z^{-c_C})$ with $c_C\in\{0,\pm1\}^g$ and $c_C\neq0$. Every monomial therefore has exponents in $\{-1,0,1\}^g$.
  - The grid average of a monomial factorises over coordinates: $\prod_e\frac1N\sum_{z\in\mu_N}z^{k_e}$. That product is 0 as soon as one $k_e=\pm1$, because $N\nmid1$ for $N\ge2$. This covers cross terms such as $z_1z_2^{-1}$. The constant monomial averages to 1.
  - The constant term is the sum over cycle-free elementary subgraphs, which is $\mu(Y,x)$.
- The proof does not need simplicity of $Y$. Parallel edges give $|\sum z_e|^2=m+\sum_{e\ne f}z_ez_f^{-1}$, still with exponents in $\{-1,0,1\}$.
- *Exact enumeration:* maximum coefficient error $\le7\times10^{-14}$ for $K_4$ ($N=2..7$), the cube ($N=2..4$) and Petersen ($N=2,3$). The matching polynomials are $x^4-6x^2+3$, $x^8-12x^6+42x^4-44x^2+9$ and $x^{10}-15x^8+75x^6-145x^4+90x^2-6$.
- *Wording, not a defect.* §5 item 8 and the synthesis say "degree at most 1 in each coordinate". The accurate phrase is "Laurent exponents in $\{-1,0,1\}$"; degree $\le1$ in $z_e$ alone would exclude the $z_e^{-1}$ terms, which are present. §4 of the page states it correctly.
- *Heilmann–Lieb,* from memory: the roots of $\mu(Y,x)$ are real and lie in $|x|<2\sqrt{\Delta-1}=2\sqrt q$. I recall the same.

### D8 — counts selection, Artin factorisation, Euler-product cancellation (C1–C3)

**VERDICT D8: VALID**

- My own enumeration of closed non-backtracking walks on $K_4$ gives $\mathrm{Tr}B^k=24,24,0,96,168,168,528$ for $k=3..9$. The number with class in $3H_1$ is $0$ for $k\le8$ and **24 of 528** at $k=9$: the four triangles $\times$ 2 orientations $\times$ 3 starting edges, each traversed three times.
- The orthogonality argument is immediate. I did not re-run the Artin factorisation (C2). It is standard, and I recall it the same way.
- *Recall of the Dirichlet comparisons.*
  - $\varphi(N)^{-1}\sum_\chi L(s,\chi)=N^{-s}\zeta(s,1/N)$ is correct.
  - Davenport–Heilbronn: $\zeta(s,\alpha)$ has zeros in $\mathrm{Re}\,s>1$ for rational $\alpha\ne\tfrac12,1$, and for transcendental $\alpha$. I recall the same, so "for $N\ge3$" is right.

### D9 — no forced lock of order $N$ (K1, K2; negative finding)

**VERDICT D9: VALID**

- The structural argument is correct: multiplication by $\zeta$ is the scalar $\sigma(\zeta)$ on each isotypic part, and it does not move eigenvalues of $M$.
- I did not re-run the lock census K1, whose definition of a lock lives in `locks.md`. The table's specific counts are unreviewed.

---

## Part I — `gate-phases.md`

### I1 — local components: $\psi_\infty=|z|/z$, $\psi_7|_{\mathcal O^\times}=\varepsilon$, $\psi_7(\sqrt{-7})=+i$ (B1)

**VERDICT I1: VALID**

- *Derivation.* Triviality on $K^\times$ forces $\psi_\infty(\alpha)\psi_7(\alpha)=\psi_u((\alpha))^{-1}$. $\mathbb C^\times$ is connected, so the split between $\infty$ and 7 is unique.
- *My own product-formula test,* over all $\alpha\in\mathcal O_K$ with $N\alpha\le400$, with the $\pi$-adic part stripped off and the unramified part read from $\psi_u$: $\max|\prod_v\psi_v(\alpha)-1|=2.3\times10^{-16}$ with $\psi_7(\pi)=+i$, and $2.0$ with $-i$.
- *The CM-type convention* ($\pi\mapsto i\sqrt7$) is used consistently on both sides.

### I2 — $F\Phi_7=i\,D_7\Phi_7$; $\varepsilon_7=i$; $N_7=49$ (B2–B4)

**VERDICT I2: VALID**

- *Self-dual measure.* $\mathfrak d_7=(\pi)$, since $\mathrm{Tr}(\pi^{-1}\mathcal O)=2\mathbb Z_7$ and $\mathrm{Tr}(\pi^{-2})\notin\mathbb Z_7$. So $\mathrm{vol}(\mathcal O_7)=7^{-1/2}$, as stated.
- *Explicit transform.* I summed directly over $\mathcal O/7^s\mathcal O$ ($s=1,2$) with $\psi(\mathrm{Tr}\,xy)$, $\mathrm{Tr}(a+b\pi)=2a$. The result agrees with $i\,D_7\Phi_7$ to $1.2\times10^{-14}$, including vanishing off the shell $v=-2$.
- *Tate's integral* with $c=\pi^2$ gives $\varepsilon_7=+i$ exactly. $g_7=i\sqrt7$ for $\psi_7=e^{2\pi i\{x\}}$.
- *Both factorisations hold.* With $c=\pi^2$: $\chi(c)=-1$ and Gauss phase $-i$. With $c=7$: $\chi(c)=+1$ and Gauss phase $+i$.

### I3 — $\varepsilon_\infty=-i$ (B5, B6)

**VERDICT I3: VALID**

- *Wirtinger computation by hand.* The kernel is $e^{-2\pi i(zw+\bar z\bar w)}$, $\partial_w$ brings down $-2\pi iz$, and $F[ze^{-2\pi|z|^2}]=\tfrac{i}{2\pi}\partial_w e^{-2\pi w\bar w}=-i\bar we^{-2\pi|w|^2}$.
- *My 2D quadrature,* with measure $2\,dx\,dy$, agrees to 12 digits at two values of $w$. The ratio of zeta integrals at $s=\tfrac12$ with $\chi_\infty=|z|/z$ is $-i$.
- *Convention check.* $\psi_\infty=e^{-2\pi ix}$ and $\psi_p=e^{+2\pi i\{x\}_p}$ make $\prod_v\psi_v$ trivial on $\mathbb Q$ (Tate). Flipping both flips $\varepsilon_\infty$ and $\varepsilon_7$ together and leaves $W$ unchanged.

### I4 — $\eta$ quadratic on $\mathbb F_9^\times$; $g_9=3=-g_3^2$; $\varepsilon_3(\psi')=-1$; $N_3=9$ (C1–C4)

**VERDICT I4: VALID**

- *$\mathbb F_9=\mathbb F_3[i]$.* $\eta(u)=(Nu|3)$ is quadratic and non-trivial. $g_9=\sum\eta(u)e^{2\pi i\mathrm{Tr}(u)/3}=3$ and $-g_3^2=3$. Hasse–Davenport, $-g(\chi\circ N)=(-g(\chi))^2$, I recall the same way.
- $\psi'_3(3)=\psi_u((3))\cdot\chi_{-3,3}(9)=(3|7)\cdot1=-1$. Here $\chi_{-3,3}(3)=1$ by the product formula, since 3 is a positive unit at every other place.
- *Tate's integral with $c=3$* gives $\varepsilon_3=-1$. The control, $\psi'_3(3)=+1$, gives $+1$.
- $\eta(-1)=1$, so the sign convention of $\psi$ inside the Gauss sum is immaterial here.

### I5 — $\prod_v\varepsilon_v=+1,-1$ equals `ellrootno`; functional equation with $W$, $N=\prod N_v$ (B7, C5, C7)

**VERDICT I5: VALID**

- My local values multiply to $(-i)(i)=1$ and $(-i)(i)(-1)=-1$. PARI gives $[1,-1]$.
- $N=\prod N_v$: $49=N(\mathfrak p^2)$ and $441=49\cdot9$, consistent with $\varepsilon(s)=\varepsilon(\tfrac12)N_v^{1/2-s}$, $N_v=N(\mathfrak f_v\mathfrak d_v)$.
- The functional equation with $W$ is my C6 (theta form, $10^{-31}$), and it fails at $O(1)$ with $-W$.

### I6 — Langlands $\lambda$-factors; $w_3=\varepsilon(\chi_{-3,3})^2\det\rho_3(\mathrm{Frob})$ (C6)

**VERDICT I6: VALID**

- $\lambda_7=\varepsilon(\chi_{-7,7},\psi_7)=g_7/\sqrt7=i$. $\lambda_\infty=\varepsilon(\mathrm{sgn},e^{-2\pi ix})=-i$.
- PARI's local root numbers: $w_7(49\mathrm a1)=-1=i\cdot i$, $w_3(441\mathrm d1)=-1$, $w_7(441\mathrm d1)=-1$. All are consistent.
- The unramified-twist formula $\varepsilon(\rho\otimes\omega)=\varepsilon(\omega)^{\dim\rho}\det\rho(\varpi)^{a(\omega)}$ I recall the same way. $\varepsilon(\chi_{-3,3})^2=\chi_{-3,3}(-1)=-1$.

### I7 — the half turn moves from the Euler factor into the gate phase; the step at 3 is uniformiser-dependent (proved here)

**Claim.** "The half turn that 49a1 spends in its Euler factor, 441d1 spends in its gate phase."

**VERDICT I7: VALID**

- $a_9(49\mathrm a1)=-3$ and $a_3=0$ (PARI), so the Euler factor at 3 is $(1+3\cdot9^{-s})^{-1}$. For 441d1, $a_3=a_9=0$.
- The page's factorisation $\varepsilon_3=(-1)\cdot(+1)$ is uniformiser-dependent, and the page says so. *A uniformiser-free form exists and makes the statement sharper than the page's:* for $\mu$ unramified and any $\eta$, $\varepsilon(\mu\eta,\psi)=\mu(\varpi)^{a(\eta)+n(\psi)}\varepsilon(\eta,\psi)$. Here $\mu=\psi_3$ (unramified, $\mu(3)=-1$), $\eta=\chi_{-3,3}\circ N$ ($a=1$), $n(\psi)=0$, and $\varepsilon(\eta)=\eta(3)\,g_9/3=+1$. So $\varepsilon_3(\psi')=\psi_3(3)^{1}=-1$ **is** 49a1's half turn, raised to the conductor exponent. Adopting this form would remove the "artefact" discussion of §4.1.

### I8 — the gate phases do not see the split-prime signs; $W$ fixes only the central parity (negative finding)

**VERDICT I8: VALID** (elementary: $\varepsilon_v=1$ wherever $\psi_v$, $\psi_{K,v}$ and the measure are unramified).

---

## Part S — headline claims of `data-ladder.md` taken from these lanes

### S1 — the $K_4$ lattice "$=H_1$ of the lift of $E_2\times E_4\times\mathrm{Jac}(C)$" (§0 table)

**Claim (one line).** The graph lattice of $K_4$ with one negative edge *is* $H_1$ of the canonical lift of the product $E_2\times E_4\times\mathrm{Jac}(y^2+(x^2+x)y=x^5+1)$.

**VERDICT S1: INVALID**

- *Attack: the gluing test of B9 applied to $K_4$.* In $L=\mathbb Z^8$, let $L_{12}=L\cap\ker\bigl((M^2-M+2)(M^2+M+2)\bigr)$ (rank 4) and $L_3=L\cap\ker(M^4-M^2+4)$ (rank 4). PARI `matkerint` gives $[L:L_{12}\oplus L_3]=2^4$. Inside the first block $L_{12}=L_1\oplus L_2$ (index 1), so the whole gluing is between the $E_2\times E_4$ block and the $S$ block, at $p=2$.
- *Consequence.* Deligne's functor is an additive equivalence. An isomorphism $(L,M)\cong(T_a,F_a)\oplus(T_b,F_b)$, with characteristic polynomials $(x^2-x+2)(x^2+x+2)$ and $x^4-x^2+4$, would send $T_a$ into $L_{12}$ and $T_b$ into $L_3$, forcing index 1. So the ordinary fourfold of $K_4$ is **not** isomorphic to $E_2\times E_4\times\mathrm{Jac}(C)$, nor to $B\times S'$ for any $B\sim E_2\times E_4$ and $S'\sim S$. It is isogenous to such a product by an isogeny of degree $2^4$.
- *The lane page is not at fault.* `no-lift.md` says "up to isogeny" and leaves the isomorphism class open. The synthesis turned "$\sim$" into "$=$".
- *Bonus for `no-lift.md` §2 "open".* Whatever the fourfold is (Jacobian, Prym or neither), it is not a product of a surface in the class of $E_2\times E_4$ and a surface in the class of $S$. Unlike Petersen and $K_5$, where the gluing is at 5 and prime to $p$, here it is at $p$ itself.
- *Sentence at fault* (`data-ladder.md` §0, row "$\mathbb Z_2$ flux on a graph, ordinary"): "$\mathbb Z^{2n}$ from the graph $=H_1$ of the lift of $E_2\times E_4\times\mathrm{Jac}(y^2+(x^2+x)y=x^5+1)$".
- *Corrected:* "$\mathbb Z^{2n}$ from the graph $=H_1$ of the canonical lift of an ordinary fourfold **isogenous** to $E_2\times E_4\times\mathrm{Jac}(y^2+(x^2+x)y=x^5+1)$. The lattice is glued at $p=2$, $[L:L_{E_2\times E_4}\oplus L_S]=2^4$, so the fourfold is not that product."

### S2 — "share $\mathcal O_K$, $J_K$ and every local step up to sign" (§2)

**VERDICT S2: MINOR**

- At $p=3$, 441d1 has no unramified local step. The twist makes $\psi'_3$ ramified (I4), and that is precisely the difference that lane I locates. `cm-lift.md` §3.4 correctly says "at every prime $p\neq3$", and `gate-phases.md` §6 already flags the brief on this point.
- *Sentence at fault:* "49a1 and 441d1 share $\mathcal O_K$, $J_K$ and every local step up to sign, and have different zeros".
- *Corrected:* "49a1 and 441d1 share $\mathcal O_K$, $J_K$, and the local step at every prime $p\ne3$ up to the sign $\chi_{-3}(p)$; at 3, 441d1 has a charged local state and no step. They have different zeros."

### S3 — "$i$ at 7 from the conductor squeeze" (§2)

**VERDICT S3: MINOR**

- The squeeze $D_7$ is unitary. It accounts for $N_7=49$, not for the phase. The phase is the normalised Gauss sum. With $c=7$ (the squeeze in $F\Phi_7=iD_7\Phi_7$), $\chi_7(7)=+1$ and $\varepsilon_7=g_7/\sqrt7=i$. With $c=\pi^2$ the split is $(-1)(-i)$. `gate-phases.md` says "$+i$ (Gauss sum)"; the synthesis misattributes it.
- *Sentence at fault:* "($-i$ at $\infty$ from the Hermite function, $i$ at 7 from the conductor squeeze, $\pm1$ at 3, …)".
- *Corrected:* "($-i$ at $\infty$ from the Hermite function; $i$ at 7, the normalised quadratic Gauss sum $g_7/\sqrt7$, with the conductor squeeze $D_7$ supplying $N_7=49$; $1$ at 3 for 49a1 and $-1$ for 441d1, which is 49a1's half turn $\psi_3(3)$ raised to the conductor exponent; …)".

---

## Ledger of "from memory" theorems

Each was compared with my own recollection; none was byte-cited, because `refs/src/` is absent here too.

| theorem (as quoted) | recalled the same? |
|---|---|
| Tate isogeny theorem; Honda–Tate with $\mathrm{inv}_v=\frac{v(\pi)}{v(q)}[\mathbb Q(\pi)_v:\mathbb Q_p]$, $\tfrac12$ at real places, $P_A=m_\pi^e$ | yes |
| Weil restriction: Frobenius $\bigl(\begin{smallmatrix}0&\rho(F^2)\\1&0\end{smallmatrix}\bigr)$, polynomial $Q(x^2)$ | yes |
| Deligne 1969 (ordinary $\Leftrightarrow$ Deligne modules) | yes |
| Centeleghe–Stix 2015 (ANT): $\mathbb F_p$, no $\pm\sqrt p$, $(T,F)$ with $F$ semisimple and $FV=p$ | yes; the functor $\mathrm{Hom}(A,A_w)$ is contravariant (anti-equivalence) |
| Deuring lifting; Chai–Conrad–Oort (2014) CM lifting up to isogeny and field extension | yes |
| Oswal–Shankar (J. LMS 2020); Bergström–Karemaker–Marseglia (IMRN 2023) | titles and venues as I recall; hypotheses not checked |
| every CM-by-$\mathcal O_K$ curve is a twist of 49a1 "or 49a2" | true, but 49a2 ($j=255^3$) has CM by $\mathbb Z[\sqrt{-7}]$; the clause is idle (C1) |
| Hecke: $L(E,s)=L(\psi,s)$, conductor $|d_K|\,N\mathfrak f$ | yes |
| Weil criterion for entire self-dual $L$ | yes |
| Tate local functional equation; $\varepsilon(s)=\varepsilon(\tfrac12)N_v^{1/2-s}$; $\varepsilon=\chi(c)\tau$ | yes |
| Hasse–Davenport $-g(\chi\circ N)=(-g(\chi))^m$; Langlands $\lambda$; unramified-twist formula | yes |
| Ihara–Bass (twisted); Sachs/Godsil–Gutman; Heilmann–Lieb | yes |
| Davenport–Heilbronn (Hurwitz zeros in $\mathrm{Re}\,s>1$ for rational $\alpha\ne\tfrac12,1$) | yes |
| Terras completion $\Lambda(1/(qu))=(-1)^n\Lambda(u)$ (gate-phases §5.2) | yes (not re-run) |

## Not re-run

The census rows cube $N=6$ and Petersen $N=6$; the lock census K1 of `zn-flux.md`; the off-line-pair Gram value $-6.19$ and the zero counts $N(T)$ of `cm-lift.md`; the Petersen unimodular-$C$ search of `no-lift.md` §6; `gate-phases.md` D1–D5, except the quartic character mod 5, whose root number $0.85065+0.52573i$ was reproduced with PARI.

## Scripts

All four scripts run from the statements alone; PARI/GP is called by subprocess.

| script | covers | output read here | runtime |
|---|---|---|---|
| `scratch_gkp_arith_nolift.py` | B2–B12, S1 | — | about 3 min |
| `scratch_gkp_arith_cm.py` | C1, C2, C6, C7 | writes `ap.txt` and `zeros_*.txt` in the working directory on first run | about 6 min, mostly PARI zeros to $T=90$ |
| `scratch_gkp_arith_zn.py` | D2–D8 | — | about 4 min |
| `scratch_gkp_arith_gate.py` | I1–I5 | — | under 1 min |
