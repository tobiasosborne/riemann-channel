# Adversarial review: the function-field and family lanes of the adelic-GKP session (`ff-dirichlet.md`, `family-vacuum.md`)

- **Date:** 2026-10-06
- **Reviewer:** claude:opus-5.5 (REFUTE lane)
- **Authors under review:** claude:opus-5.5, lanes J (`ff-dirichlet.md`) and M (`family-vacuum.md`); orchestrator claude:fable-5.1
- **Files under review:** `notes/adelic-gkp/ff-dirichlet.md` and `notes/adelic-gkp/family-vacuum.md`: every statement labelled *proved here* or *checked*. Context only: `data-ladder.md` §§4–4b, `gate-phases.md` §§1–2, `zn-flux.md` §2, shard 04u, `scripts/lps_square_complex.py`. Labels J1–J13 and M1–M4 are mine; J1–J4 and M1–M4 follow the orchestrator's brief, and J5–J13 are the remaining labelled statements of lane J.
- **Independent numerics:** eleven scratch scripts `notes/reviews/scratch_gkp_ffm_*.py`, written from the *statements* only. Neither `check_ff_dirichlet.py` nor `check_family_vacuum.py` was opened. The rest was built from scratch:
  - my own $\mathbb F_p[t]$ arithmetic, power-residue symbols and $L$-functions by brute force, with exact $\mathbb Z[\zeta_N]$ coefficients;
  - local root numbers from Tate's integral $\int_{\varpi^{-(a+d)}\mathcal O^\times}\chi_v^{-1}(x)|x|^{-1/2}\psi_v(x)\,dx$, evaluated by finite sums. I used **additive characters of my own choosing**, $\psi_v=\psi_0(\mathrm{Tr}\,\mathrm{Res}_v(x\,h\,dt))$ for five polynomials $h\ne1$, so that the different is non-trivial at finite places and the local factors are not the page's. Residues were obtained from the residue theorem through the expansion at $\infty$;
  - my own closure and HNF for the order $R$;
  - my own $\mathbb F_{q^r}$ point counter, with PARI's `hyperellcharpoly` called by subprocess for $N=2$;
  - my own LPS pair. It uses the *other* square root of $-1$ mod 5 ($i\mapsto3$, not 2) and Cayley graphs by *left* multiplication, so it is a different labelling from `scripts/lps_square_complex.py`;
  - mpmath for the zeros of $\zeta$.

**Headline.** Both pages hold up well. Every number I recomputed came out as stated:

- the six $L$-functions and root numbers;
- every local phase in the table of §3.2;
- the 30 of 50 failures without $\chi_P(P)$;
- the indices 5, 5, 7;
- the $\Omega_+$ denominators and Smith invariants;
- all six point-count identities with the reciprocity constant, and the failure of all six twisted controls;
- the LPS joint spectrum, 1618, 7124, 176 of 240, 6 of 10 and 0.44;
- the counts 52, 48, 46 and 26, 32, 31 for $\zeta$.

With my own additive characters, the product of Tate local factors equals $W$ to $10^{-39}$, and the conductor sum equals $\deg\Lambda$. Lane M's Proposition 1 is correct, and so is its averaging construction (rebuilt on an example of my own).

There are three defects, all in lane J:

1. **"Positivity is RH" needs $P_\chi$ squarefree.** I found power-residue characters whose $P_\chi$ has a repeated root although RH holds. The cleanest is the Fermat quartic: $q=5$, $N=4$, $f=t^4+1$, with $P_\chi=(x+1+2i)^2$. In such a case $E$ is not reduced, the Weil form is degenerate, $F$ is not semisimple on $R$, there is no vacuum, and $R$ is not the $\chi$-part of $H_1$, even rationally.
2. The table of "leading minors of the Weil form" holds the minors of the **trace form** $\mathrm{Tr}(x\sigma y)$ ($=2\times$ Weil form), and they are taken on the **companion lattice** $\mathbb Z[\zeta][F]$, not on $R$.
3. The $N=2$ paragraph overstates two things: "local phases non-trivial" (X6's are both 1) and "its lattice is $H_1$".

**Verdict counts: 14 VALID / 3 MINOR / 0 INVALID** (17 statements: 13 J, 4 M).

---

## Part J — `ff-dirichlet.md`

### J1 — $L$ is a polynomial of the stated degree and satisfies RH (§1.1, §1.2)

**Claim (one line).** For a power-residue $\chi$ mod squarefree $f$ of degree $d$, $L(u,\chi)$ has degree $d-1$ (odd) or is $(1-u)\Lambda$ with $\deg\Lambda=d-2$ (even), and all $|\alpha|=\sqrt q$.

**VERDICT J1: VALID**

- *Degree, attacked at reducible $f$.* Each component $(\cdot/P_i)_N$ has exact order $N$ (the power map onto $\mu_N$ is surjective), so $\chi$ is primitive mod $f$. The degree is then $\deg f+a_\infty-2$, and I recomputed it directly. X2 ($f=t(t^2+2)$) has $n=2$ with $c_1=0$. Over all squarefree moduli, reducible ones included, at $(5,4,3)$, $(5,4,4)$ and $(7,3,3)$ (894 characters; `scratch_gkp_ffm_repeated.py deg`), the degree is as stated every time.
- *Parity.* $\chi(c)=c^{(q-1)\deg f/N}$ holds for any $f$, not only irreducible $f$, because $c^{(Q-1)/N}=c^{\deg P\,(q-1)/N}$. The page's parenthesis "($N\mid\deg f$ for irreducible $f$)" is therefore more restrictive than it needs to be, but it is not wrong.
- *Even case.* $L(1,\chi)=\frac1{q-1}\sum_{a\in(A/f)^\times}\chi(a)=0$. Its Euler factor at $\infty$ is $(1-\chi_\infty(\pi)u)^{-1}=(1-u)^{-1}$, so $\Lambda=L/(1-u)$ is the complete $L$-function.
- *Census and digits.* All six $\Lambda$ agree with the table, coefficient by coefficient (for example X3: $1+(1+1.732i)u+(1-5.196i)u^2+(17.5-6.062i)u^3$, which is $1+(2+2z)u-(2+6z)u^2+(14-7z)u^3$ at $z=\zeta_3$). RH holds to $10^{-40}$. In my census of 1260 characters of irreducible conductor (the page's six families plus $(3,2,5)$, $(3,2,6)$, $(5,2,5)$) RH fails nowhere.

### J2 — the functional equation, $W=c_n/q^{n/2}$, and the Gauss-sum formulas (§1.3)

**Claim.** $\Lambda(u)=W(\sqrt q u)^n\overline\Lambda(1/(qu))$ with $W=c_n/q^{n/2}$ and $|W|=1$ from the FE alone. $W=G/q^{d/2}$ for even $\chi$, and $W=(G/q^{d/2})/(g/\sqrt q)$ for odd $\chi$.

**VERDICT J2: VALID**

- *Normalisation.* From $\{\bar\alpha_i\}=\{q/\alpha_i\}$, $\overline\Lambda(1/(qu))=\prod(1-1/(\alpha_iu))=(-1)^n(\prod\alpha_i)^{-1}u^{-n}\Lambda(u)$. Hence $\Lambda(u)=c_nu^n\overline\Lambda(1/(qu))$ exactly, which is the stated form. FE residual $\le3\times10^{-40}$; with $-W$ the relative residual is 2.0 in all six.
- *The two Gauss-sum formulas.* I redid the proof by splitting $a=c\,m$. Odd: $G=g\,S_{d-1}$. Even: $G=-(q-1)S_{d-1}-S_{d-1}=-qS_{d-1}=q\,c_{d-2}$. I recomputed both numerically: agreement to $10^{-40}$, and $|G|^2=q^d$.
- The extra odd factor $g/\sqrt q$, the Gauss sum of $\chi|_{\mathbb F_q^\times}$, is exactly the phase at $\infty$ (J3).

### J3 — the local gate identities, including the place at $\infty$ (§3.1)

**Claim.**

- $\varepsilon_P=\chi_P(P)G_P/\sqrt Q$ at $P\mid f$.
- At $\infty$: $\varepsilon_\infty=\bar g/\sqrt q$ for odd $\chi$; for even $\chi$, $1$, where the qunaught is squeezed by the different of $dt$ ($F1_{\mathcal O_\infty}=q1_{\mathfrak p_\infty^2}=D_{\pi^{-2}}1_{\mathcal O_\infty}$).
- The conductor exponents $a_v+d_v$ sum to $\deg\Lambda$.

**VERDICT J3: VALID**

- *Analytic recheck.*
  - $\psi_\infty(x)=\psi_0(-x_1)$ is trivial on $\mathfrak p_\infty^2$, so $\mathcal O_\infty^\perp=\mathfrak p_\infty^2$, and $\mathrm{vol}(\mathcal O_\infty)=q$ for the self-dual measure. Then $F1_{\mathcal O}=q1_{\mathfrak p^2}$, and $D_{\pi^{-2}}1_{\mathcal O}=|\pi^{-2}|^{1/2}1_{\mathfrak p^2}$ is the same function.
  - For odd $\chi$: $F\Phi_\infty(\pi y_1)=\sum_x\bar\chi(x)\psi_0(-xy_1)=\chi(-y_1)g(\bar\chi)$, and $\chi(-1)g(\bar\chi)=\bar g$, so $\lambda_\infty=\bar g/\sqrt q$.
  - $\chi_\infty(1/t)=1$ and $\chi_\infty=\chi$ on constants both follow from the product formula on monic $m$ and on $c\in\mathbb F_q^\times$; I derived both myself.
- *Independent check with a different additive character.* For $h\in\{2,\;t+1,\;t,\;t^2+3,\;t^3+2t+1\}$ I put $\psi=\psi_0\circ\mathrm{Tr}\,\mathrm{Res}(x\,h\,dt)$. This moves the different to the zeros of $h$, including into $P\mid f$ ($h=t$ for X2) and onto unramified places, where $\varepsilon=\chi(P)^{v_P(h)}$. It also changes $d_\infty$ to $-2-\deg h$.
  - Tate's integral was evaluated by finite sums at every place.
  - The product equals $W$ to $\le1.4\times10^{-39}$ for all 30 (example, $h$) pairs.
  - $\sum_v(a_v+d_v)\deg v=n$ in every case.

  So the treatment of $\infty$ and of the different is right, independently of the page's $\psi$.
- *The page's own phases.* The page's 9 local phases in §3.2 were reproduced to 5 digits, for example X1 $(0.99596+0.08981i,\;0.52573-0.85065i)$ and X3 $(0.70121-0.71295i,\;0.89595+0.44415i)$.

### J4 — the product of gate phases is $W$; the factors $\chi_P(P)$ are needed (§3.2, B3–B7)

**Claim.** $\prod_v\varepsilon_v=W$. Dropping $\chi_{P_i}(P_i)=\prod_{j\ne i}\chi_j(P_i)$ gives the wrong $W$ for 30 of the 50 moduli $f=P_1P_2$ (degrees $1\times2$) at $q=5$, $N=4$. $G=\chi_1(P_2)\chi_2(P_1)G_1G_2$ for X2.

**VERDICT J4: VALID**

- I recomputed the Gauss sums with my own enumeration of residues. The page's product equals $W$ in all 50 two-place moduli.
- **Dropping $\chi_P(P)$ fails in exactly 30 of 50.** That is consistent with reciprocity: the dropped factor is $(P_2/P_1)_4(P_1/P_2)_4=\pm(P_1/P_2)_4^2\in\{\pm1\}$.
- X2 is the one two-place example: without $\chi_P(P)$ the error is 2.0.
- The CRT factorisation for X2 holds to $10^{-39}$.
- The census gives $\prod\varepsilon_v=W$ every time: 1260 characters of irreducible conductor, made of the page's families (472, without its 60 random quartics) plus three more quadratic families.

### J5 — the comparisons with the arithmetic rung (§3.3, B8)

**Claim.** X5 has phases $(+i,-i)$ like 49a1. X1's $\varepsilon_\infty=-\tau(\chi_D)/\sqrt5=-iW(\chi_D)$, with $W(\chi_D)=0.85065+0.52573i$.

**VERDICT J5: VALID**

- I recomputed X5's phases: $(+i,-i)$.
- $\chi|_{\mathbb F_5^\times}(2)=2^3=3=2^3\mapsto-i$ (generator 2), so $\chi=\bar\chi_D$ on constants.
- $\bar g=\chi_D(-1)\tau(\chi_D)=-\tau(\chi_D)$, and $W(\chi_D)=\tau/(i\sqrt5)=0.85065+0.52573i$; both reproduced. The "reading" part is not adjudicated.

### J6 — $\sigma$, $R$, $\Omega_+$, the index, the companion lattice, $W$ as a determinant (§2.1, 2.2, 2.3 first bullets, 2.7)

**Claim.** The bullets are:

- $\sigma$ exists by the FE alone.
- $R=\mathbb Z[\zeta][F,V]$ is an order with $[R:\mathbb Z[\zeta][F]]=5,5,7,1,1,1$.
- The companion lattice is $V$-stable iff $q/c_n\in\mathbb Z[\zeta]$, hence for $n\le1$, or for $n=2$ with $W$ a root of unity.
- $\Omega_+=\mathrm{Tr}(x\sigma y/(V-F))$ is alternating, $\zeta$-invariant and a $q$-similitude, with denominators 11, 1, 29, 2, 1, 1 and Smith invariants as tabled.
- $W=(-1)^n\det_{\mathbb Q(\zeta)}F/q^{n/2}$ and $\det_{\mathbb Z}F=q^{D/2}$.

**VERDICT J6: VALID**

- *Proofs re-derived.*
  - $\Omega_+(y,x)=\mathrm{Tr}\,\sigma(\cdot)=-\Omega_+(x,y)$, and $\Omega_+(Fx,Fy)=\mathrm{Tr}(FV\cdots)=q\Omega_+$.
  - $V=-(q/c_n)(F^{n-1}+\dots+c_{n-1})$, so the integrality condition is necessary and sufficient.
  - $|q/c_n|=q^{1-n/2}$ gives the case split (Kronecker for $n=2$; norm $<1$ for $n\ge3$).
  - $c_n=(-1)^n\prod\alpha_i$ gives the determinant formula.
- *Exact recomputation* (`scratch_gkp_ffm_lattice.py`, sympy rationals):
  - $\sigma$ is a ring involution in all six.
  - My closure gives indices 5, 5, 7, 1, 1, 1.
  - $V$ is integral on the companion basis exactly for X4–X6.
  - $\Omega_+$ is alternating, $\zeta$-invariant and a $q$-similitude.
  - Denominators are 11, 1, 29, 2, 1, 1. Smith invariants of the primitive multiple: $(1,1,33,33)$, $(1,1,2,2)$, $(1,1,29,29,55941,55941)$, $(1,1)\times3$.
  - $\det_{\mathbb Z}F=25,25,343,7,7,3=q^{D/2}$.

### J7 — "positivity is RH" (§2.3, verdict bullet 3, §4 item 5)

**Claim.** The Weil form $\tfrac12\mathrm{Tr}_{E/\mathbb Q}(x\sigma y)$ is positive if and only if RH holds.

**VERDICT J7: MINOR** (true when $P_\chi$ is squarefree; false as stated, with a counterexample among power-residue characters)

- *Attack: the argument assumes $E$ is a product of fields.* "Embedding" and "$\sum|x|^2$" need $E=\mathbb Q(\zeta_N)[x]/(P_\chi)$ to be reduced. If $P_\chi$ has a repeated root, the nilradical is isotropic for $\mathrm{Tr}(x\sigma y)$, so the form is degenerate whether or not RH holds.
- *Search for such characters* (`scratch_gkp_ffm_repeated.py`). Among squarefree moduli I found repeated roots in $P_\chi$ at $(q,N,\deg f)=(5,4,4),(5,4,5),(7,3,4),(7,3,5),(3,2,6)$. All are reducible $f$; none occurred for irreducible $f$ in the census.
- *The cleanest case: the Fermat quartic* (`scratch_gkp_ffm_fermat.py`, exact). Take $q=5$, $N=4$, $f=t^4+1=(t^2+2)(t^2+3)$; $\chi$ is even.
  - $\Lambda=1+(2+4i)u+(-3+4i)u^2$ and $P_\chi=(x+1+2i)^2$. The discriminant is 0 and $|1+2i|^2=5$, so RH holds.
  - $\sigma$ exists, $[R:\mathbb Z[i][F]]=5$, and $\mathrm{charpoly}_{\mathbb Q}(F|E)=(x^2+2x+5)^2$, yet $F^2+2F+5\ne0$. So $F$ is **not semisimple** on $E$.
  - The trace form on $R$ has **rank 2 of 4**. $\Omega_+$ has Smith invariants $(0,0,1,1)$, so it is degenerate too.
  - By `family-vacuum.md` Prop. 1, (i)⇒(ii), no vacuum commutes with $F$.
  - On the curve $y^4=t^4+1$, Frobenius on $H_1$ is semisimple (Weil). So the $\chi$-part of $H_1\otimes\mathbb Q$ is $\mathbb Q(i)^2$ with $F=\alpha$, not $E$, and $R$ is not even rationally the $\chi$-part. This also bounds §4 item 4.
- *Same phenomenon at $N=2$:* $q=3$, $f=(t^2+1)(t^2+t+2)(t^2+2t+2)$ gives $\Lambda=(1+2u+3u^2)^2$.
- The six examples and the control C7 are unaffected: all have squarefree $P_\chi$, and I reproduced positivity in all six. Smallest eigenvalue of $\tfrac12\mathrm{Tr}$ on my $R$-basis: 0.245, 0.343, 0.400, 0.500, 0.646, 0.586.
- *Sentences at fault.*
  - Verdict bullet 3: "The Weil form is positive if and only if $\sigma$ is complex conjugation in every embedding, that is, if and only if RH holds."
  - §2.3: "This trace form is positive definite if $\sigma$ is complex conjugation in every embedding ($\sum|x|^2$). If it is not, $\sigma$ pairs two different embeddings and the form contains a hyperbolic plane (*sketched*). So **positivity is RH**."
  - §4 item 5: "The Weil form $\tfrac12\mathrm{Tr}(x\sigma y)$ is positive exactly when RH holds."
- *Corrected:* "When $P_\chi$ is squarefree (so $E$ is a product of CM or real fields), the Weil form $\tfrac12\mathrm{Tr}(x\sigma y)$ is positive definite iff $\sigma$ is complex conjugation in every embedding, i.e. iff RH holds. When $P_\chi$ has a repeated root, which happens for power-residue characters (Fermat quartic: $q=5$, $N=4$, $f=t^4+1$, $P_\chi=(x+1+2i)^2$), $E$ is not reduced. Then the trace form and $\Omega_+$ are degenerate even though RH holds, $F$ is not semisimple on $R$, there is no vacuum, and $R$ is not the $\chi$-part of $H_1$ even up to isogeny: the step must be built on $\mathbb Q(\zeta)[x]/(P_\chi^{\rm red})^{m}$ instead."

### J8 — the table of leading minors (§2.3)

**Claim.** "Exact leading minors of the Weil form": X1 $4,16,240,3600$; X2 $4,16,320,6400$; X3 $6,27,1062,31329,4780062,546993027$; X4 $2,3$; X5 $2,19$; X6 $2,8$; control $2,-16$.

**VERDICT J8: MINOR** (the numbers are right, but they are minors of a different form on a different lattice)

- The determinant is basis-free on $R$, so the last minor can be compared with any basis.
- My exact computation gives $\det\mathrm{Tr}(x\sigma y)|_R=144,\,256,\,11163123,\,3,\,19,\,8$. The tabled last minors are these times $[R:\mathbb Z[\zeta][F]]^2=25,25,49$.
- On the companion basis $\zeta^aF^b$ of $\mathbb Z[\zeta][F]$, the trace form reproduces **every** tabled minor exactly, including the control's $2,-16$.
- The first entry is $\mathrm{Tr}(1)=2\varphi(N)$, not $\tfrac12\mathrm{Tr}(1)$. For example $\mathbb Z[\zeta_3]$ has no element with $\tfrac12\mathrm{Tr}(b\bar b)=N(b)=2$.
- Positivity, the only use made of the table, is unaffected.
- *Sentence at fault:* "Exact leading minors of the Weil form:" (with the table that follows).
- *Corrected:* "Exact leading minors of the trace form $\mathrm{Tr}(x\sigma y)$ (twice the Weil form) on the companion lattice $\mathbb Z[\zeta_N][F]$, in the basis $\zeta^aF^b$: [table unchanged]. On $R$ the determinant of the trace form is $144,256,11163123,3,19,8$; that of the Weil form is these divided by $2^D$."

### J9 — the vacuum $J=(F-V)(4q-(F+V)^2)^{-1/2}$ on $R$ (§2.4, C5)

**Claim.** The spectrum of $F+V$ is real and lies in $(-2\sqrt q,2\sqrt q)$. $J^2=-1$, $J$ commutes with $F$ and $\zeta$, and $\Omega J$ is symmetric positive definite.

**VERDICT J9: VALID** (for the six examples; see J7 for the repeated-root case)

- All four properties hold on my $R$-basis with $\Omega=\Omega_+$.
- The smallest eigenvalue of $\Omega_+J$ is 0.140, 0.485, 0.232, 0.289, 0.296, 0.414. The page's "between 0.21 and 2" is basis-dependent and was not compared.

### J10 — $\mathrm{charpoly}_{\mathbb Z}(F|R)$, ordinarity, Deligne module (§2.5)

**Claim.** The six characteristic polynomials are as tabled, they equal $\prod_{j\in(\mathbb Z/N)^\times}P_{\chi^j}$, and their middle coefficients $11,-8,19,4,3,2$ are prime to $p$.

**VERDICT J10: VALID**

- All six reproduced exactly, from my $R$.
- "Ordinary iff the coefficient of $x^g$ is prime to $p$" is what I also recall. Deligne 1969 is recalled the same.

### J11 — the $\chi$-part of $\mathrm{Jac}(y^N=cf)$ with $c$ from reciprocity (§2.6, D1–D3)

**Claim.** $c^{(q-1)/N}=(-1)^{(q-1)d/N}$. The zeta numerator of $y^N=cf$ is $\prod_{j=1}^{N-1}\Lambda(u,\chi^j)$, and a twisted $c$ fails. $\Lambda(\chi^2)=1+3u+5u^2$ (X1) and $1-4u+5u^2$ (X2).

**VERDICT J11: VALID** (up to isogeny, as §2.6 itself says; for the repeated-root case see J7)

- *The reciprocity condition.* I re-derived it from Rosen's $N$-th power reciprocity for monic $P,Q$: $\chi(Q)=(f/Q)_N(-1)^{\frac{q-1}Nd\deg Q}$ and $(c/Q)_N=c^{\frac{q-1}N\deg Q}$.
- *My counts.* My $\mathbb F_{q^r}$ counts ($r\le g$, places at $\infty$ counted by $\gcd(N,d)$) match the prediction in all six:
  - X1 $[5,33,116]$, X2 $[2,4,122]$, X3 $[10,58,373]$, X4 $[12,48]$, X5 $[11,55]$, X6 $[6,12]$;
  - the twist by a primitive root fails in all six.
- *PARI.* `hyperellcharpoly` gives $x^2+3x+7$, $x^2+2x+3$, $x^2+3x+5$ and $x^2-4x+5$.
- $\prod_jW(\chi^j)=1$ to $10^{-30}$ in all six.

### J12 — the $N=2$ paragraph (verdict bullet 4, §3.5, §4 item 7)

**Claim.** A quadratic $\chi$ has $W=1$. Its lattice is $H_1$ of the whole hyperelliptic Jacobian. Its local phases are non-trivial but cancel. $\prod_jW(\chi^j)=1$ in general.

**VERDICT J12: MINOR**

- *What holds.* $W=1$ follows because $\Lambda(\chi)$ is a curve's zeta numerator, with top coefficient $q^g$. I checked it on 958 quadratic characters of irreducible conductor. $\prod_jW(\chi^j)=1$ is forced, since $W(\chi^{N-j})=\overline{W(\chi^j)}$ and the quadratic member has $W=1$.
- *What fails.*
  - (a) The phases are not always non-trivial. X6, on the page's own table, has phases $1$ and $1$. More generally, every even quadratic $\chi$ with $f$ irreducible has both phases equal to 1 ($\varepsilon_\infty=1$ and $\varepsilon_f=W=1$).
  - (b) "Its lattice is $H_1$ of the whole hyperelliptic Jacobian" contradicts the page's own open item (§2.6: only the isogeny class is known). It also fails rationally when $P_\chi$ has a repeated root: $q=3$, $f=(t^2+1)(t^2+t+2)(t^2+2t+2)$, $\Lambda=(1+2u+3u^2)^2$ (J7).
- *Sentence at fault:* "Its lattice is $H_1$ of the whole hyperelliptic Jacobian, so it is a curve of the existing rung read over the base $\mathbb F_q(t)$. Its local phases are non-trivial but cancel; in example X5 they are $+i$ at $f$ and $-i$ at $\infty$." The same overstatement appears in §4 item 7: "the lattice is the whole hyperelliptic $H_1$".
- *Corrected:* "When $P_\chi$ is squarefree, its lattice $R=\mathbb Z[F,V]$ is a Deligne module in the isogeny class of $H_1$ of the whole hyperelliptic Jacobian (which lattice is open, §2.6), so it is a curve of the existing rung read over the base $\mathbb F_q(t)$. Its local phases lie in $\{\pm1,\pm i\}$ and multiply to 1. They can be non-trivial ($+i$ at $f$ and $-i$ at $\infty$ in X5) or all trivial (X6, and every even quadratic $\chi$ of irreducible conductor)."

### J13 — the coefficients of $L$ as overlaps of the code (§0)

**Claim.** $\langle\Theta_K,\Phi^{(k)}\rangle=\sum_{m\text{ monic},\deg m=k}\chi(m)$.

**VERDICT J13: VALID**

- An $x\in K$ in the support is integral at every finite place, so it is a polynomial. It is a unit at each $P_i$, so it is prime to $f$, and $x\in t^k(1+\mathfrak p_\infty)$ makes it monic of degree $k$.
- The product of the charges is $\prod_i\chi_i(x)=\chi(x)$. The statement is definitional and correct.

---

## Part M — `family-vacuum.md`

### M1 — two one-mode steps (§1, (1a)–(1c))

**Claim.**

- $J_q=J_{q'}$ iff $(q,\lambda)=(q',\lambda')$, and $J_q\ne-J_{q'}$.
- $[M_q,M_{q'}]=\bigl(\begin{smallmatrix}q-q'&\lambda-\lambda'\\q'\lambda-q\lambda'&q'-q\end{smallmatrix}\bigr)$ and $M_qV_{q'}=\bigl(\begin{smallmatrix}q'&0\\q\lambda'-q'\lambda&q\end{smallmatrix}\bigr)$, so no $\Omega$ admits a common vacuum when $q\ne q'$.
- For $2\times2$ elliptic steps, a common vacuum exists iff the steps commute.

**VERDICT M1: VALID**

- I redid all identities in sympy (`scratch_gkp_ffm_m1zeta.py`): $V_q$, $J_q$, $J_q^2=-1$, $\Omega J_q=\bigl(\begin{smallmatrix}2q&\lambda\\\lambda&2\end{smallmatrix}\bigr)/\sqrt{4q-\lambda^2}$, the commutator and $M_qV_{q'}$, all exactly.
- *Attack on "any $\Omega$".* A common vacuum $J$ for $\Omega'$ makes each $S$ preserve $G_J=\Omega'J$, because $S^T\Omega'JS=S^T\Omega'SJ$. Hence $\langle S_q,S_{q'}\rangle$ would be bounded. But $S_qS_{q'}^{-1}=M_qV_{q'}/\sqrt{qq'}$ has real eigenvalues $\sqrt{q/q'}$ and $\sqrt{q'/q}$. The argument is sound.
- (1c): the centraliser of an elliptic $2\times2$ is $\mathbb R[M]\cong\mathbb C$, so $J=\pm(M-\lambda/2)/\sqrt{q-\lambda^2/4}$ and the sign is fixed by $\Omega$.
- *Not re-run:* "12 of the 15 test pairs" (the pairs are not listed on the page).

### M2 — Proposition 1 (shared vacuum iff RH for each step) and the uniqueness remark

**Claim.** For pairwise commuting similitudes of one $\Omega$, these are equivalent:

- (i) a common vacuum exists;
- (ii) each step is semisimple with $|\mu|=\sqrt{q_i}$;
- (iii) $\langle S_i\rangle$ is relatively compact.

The proof of (iii)⇒(i) averages over the compact closure and sets $J=-A(-A^2)^{-1/2}$. A unique vacuum of one step is the family's.

**VERDICT M2: VALID**

- *Attacks on (iii)⇒(i).*
  - The closure is compact by (iii). It lies in $\mathrm{Sp}(\Omega)$, which is closed, so the averaged $G$ is invariant and positive.
  - $A=G^{-1}\Omega$ is $G$-skew, and $S^{-1}AS=G^{-1}S^T\Omega S=A$, using $S^{-1}G^{-1}=G^{-1}S^T$.
  - $-A^2$ is $G$-self-adjoint and positive, so $J=-A(-A^2)^{-1/2}$ is a real function of $A$. Hence $J^2=-1$, $J$ commutes with every $S_i$ (and so with every $M_i$), and $\Omega J=G(-A^2)^{1/2}$ is symmetric positive.
- *Commutativity.* It is used only in (ii)⇒(iii), by simultaneous diagonalisation into a torus, as the page says.
- *Numerical rebuild on my own family.* Three commuting steps of norms 2, 3, 5 on $\mathbb R^8$, conjugated by a random symplectic matrix. One step has a Krein-indefinite eigenvalue (angles $\pm0.7$ on two modes). The exact Haar average is invariant, and $J$ has $J^2=-1$, commutes with all three steps, and gives $\Omega J>0$.
- *Uniqueness.* The one-line proof is right: $S_2JS_2^{-1}$ is again a vacuum of $M_1$, since $\Omega S_2JS_2^{-1}=S_2^{-T}\Omega JS_2^{-1}$.
  - The Krein condition (*sketched*) is consistent with my example. The step with the Krein-indefinite pair has a 6-dimensional $\mathfrak{sp}$-commutant (2 simple modes and $\mathfrak u(1,1)$). I exhibited a second vacuum of that step that does not commute with the other two.
  - So "one step's vacuum is the family's" really does need uniqueness.
- *The control.* $\sqrt2\bigl(\begin{smallmatrix}R&1\\0&R\end{smallmatrix}\bigr)$ preserves a non-degenerate alternating form (a 2-dimensional space of invariant forms, generic $\det\ne0$), so it is a legitimate counterexample to dropping semisimplicity.

### M3 — the LPS pair (§2)

**Claim.**

- $A_{13}$ and $A_{17}$ commute. Besides $(\pm14,\pm18)$ there are 10 joint eigenspaces: $(\pm4,\pm5)$:12, $(\pm4,\pm3)$:4, $(\pm4,0)$:18, $(\mp2,\pm2)$:15, $(\mp2,\pm6)$:10, all strictly Ramanujan.
- $M_{13}$ and $M_{17}$ are similitudes of one $\Omega$ that do not commute.
- Both Weil forms are positive on $W$, and $\max|J_{13}-J_{17}|=0.61$.
- The commutant has dimension 1618 and contains no positive element. The commutant of $M_{13}$ alone has dimension 7124.
- $M_{13}V_{17}$ is integral with eigenvalues 13 and 17. $S_{13}S_{17}$ is hyperbolic on 6 of 10 joint eigenspaces. 176 of the 240 eigenvalues of $M_{13}M_{17}$ lie off $|\mu|=\sqrt{221}$. $\min\|[S_{13},S_{17}]\|=0.44$.

**VERDICT M3: VALID**

- *Rebuild* (`scratch_gkp_ffm_lps.py`). This is my own construction:
  - $i\mapsto3$ in $\phi$, left Cayley graphs, $|S_{13}|=14$, $|S_{17}|=18$;
  - both graphs simple and symmetric; $A_{13}A_{17}=A_{17}A_{13}$ exactly;
  - the joint spectrum is exactly as stated, $\dim W=118$, integer and strictly Ramanujan.
- *Steps and Weil forms.* The similitude identities, $V=qM^{-1}$, the block commutator and $M_{13}V_{17}=\bigl(\begin{smallmatrix}17I&0\\13A_{17}-17A_{13}&13I\end{smallmatrix}\bigr)$ all hold exactly. The Weil forms equal $\tfrac12\bigl(\begin{smallmatrix}2q&A\\A&2\end{smallmatrix}\bigr)$, with minimum eigenvalue on $W$ of 0.675 ($q=13$) and 0.456 ($q=17$). On the full space they are indefinite ($-2.22$, $-3.04$, from the trivial and sign modes), as the restriction to $W$ requires.
- *The commutant.*
  - Each $2\times2$ pair spans $M_2(\mathbb R)$ (rank 4) on every plane. Distinct joint eigenvalues give inequivalent planes, so the commutant is $\bigoplus I_2\otimes M_{m_j}(\mathbb R)$, of dimension $\sum m_j^2=1618$.
  - I confirmed this by direct Kronecker solves on three sub-blocks (dimensions 160, 450, 648, each equal to $\sum m^2$).
  - $2\sum m^2$ over the $A_{13}$-eigenspaces is $7124$.
  - The no-positivity argument $\Omega(e\otimes v,(I\otimes X)e\otimes v)=\omega(e,e)v^TXv=0$ is correct.
- *Hyperbolicity.* $\mathrm{tr}(M_{13}M_{17})=\lambda\mu-30$ per plane, which gives hyperbolicity on exactly the 6 planes with $\lambda_{13}\lambda_{17}\le0$. 176 of 240 eigenvalues are off $|\mu|=\sqrt{221}$ ($2\times86$ from those planes, plus 2 each from the trivial and sign modes). The minimum Frobenius norm of the per-plane commutator is $0.4359$.
- *Both vacua* are genuine vacua of their own step on $W$, and neither commutes with the other step.
- **"$\max|J_{13}-J_{17}|=0.61$" is basis-dependent.** It is 0.614 in the vertex basis (reproduced), but 2.258 in the orthonormal joint eigenbasis and 2.90 in operator norm. The page does not name the basis. The claim it supports ("the vacua differ") stands.
- *Wording, (c).* "preserves the commutator ... has diagonal $q-q'$": conjugation preserves the commutator only up to conjugacy, and its diagonal is not invariant; its non-vanishing is. The conclusion is unaffected, so I record this as a note, not a fault.

### M4 — $\zeta$'s spectral model and the Bass-doubled control (§3)

**Claim.**

- On 50 zero pairs and $p=2,3,5$: $M_p=\sqrt p\,R(\gamma\log p)$ are commuting $p$-similitudes of $\Omega_{\rm FE}$, with modulus $\sqrt p$. They share $J=R(\pi/2)$ with $\Omega J=I$, and their Weil eigenvalues are $\sqrt p\sin(\gamma\log p)$, negative 52, 48, 46 times out of 100.
- The steps $B_p$ do not commute. $B_pB_{p'}$ is hyperbolic on 26, 32, 31 of 50 zeros, and $B_pB_{p'}^{-1}$ on all 50.

**VERDICT M4: VALID**

- Everything was reproduced with mpmath `zetazero` (`scratch_gkp_ffm_m1zeta.py`): 52/48/46 negative, 26/32/31 hyperbolic, 50/50 for the inverse products, 0/50 commuting.
- "$M_pV_{p'}=\sqrt{pp'}R(\gamma\log(p/p'))$" is immediate.
- The "reading" paragraph is labelled *heuristic* and is not adjudicated.

---

## Ledger of "from memory" theorems

| theorem (as quoted) | recalled the same? |
|---|---|
| Rosen Ch. 4: $L(u,\chi)$ polynomial, degree $\deg f+a_\infty-2$, $(1-u)\mid L$ for even $\chi$ | yes |
| Weil 1948: RH for curves; semisimplicity of Frobenius on $T_\ell$ of an abelian variety | yes (the latter is what makes J7's repeated-root case fail rationally) |
| Rosen Ch. 3: $N$-th power reciprocity $(Q/P)_N=(-1)^{\frac{q-1}N\deg P\deg Q}(P/Q)_N$ for monic $P,Q$ | yes |
| Tate's thesis for function fields (Weil, *Basic Number Theory* VII); $\varepsilon$ as Tate's integral; unramified $\varepsilon=\chi(\varpi)^{d}$ | yes |
| Deligne 1969 (ordinary ⇔ Deligne modules); Centeleghe–Stix 2015 | yes |
| Gauss–Jacobi sums for Fermat-type curves (X4) | yes, in outline: $\chi_P=\chi'\circ N$ with $\chi'$ cubic on $\mathbb F_7^\times$, then Hasse–Davenport |
| Krein theory: unique vacuum iff every eigenspace Krein-definite (*sketched* on the page) | yes, and consistent with my example in M2 |

## Not re-run

- The page's 60 random quartics at $(7,3,4)$ in the census.
- The Tate-ratio checks at $s=0.3+0.7i$ and $1.7-0.4i$ (B1, B2); I evaluated $\varepsilon$ at $s=\tfrac12$ only, but for five additive characters.
- Lane M's "12 of 15" test pairs, whose pairs are not listed.
- The page's smallest eigenvalues of $\Omega J$ (basis not given).
- The full $236^2$-unknown commutant solve: the block argument plus three direct sub-block solves stand in.

## Scripts

All scripts work from the statements alone. PARI/GP is called by subprocess only in `curves`. Run them from `notes/reviews/`.

| script | covers | runtime |
|---|---|---|
| `scratch_gkp_ffm_core.py` | library: $\mathbb F_p[t]$, power-residue characters, $L$-functions | – |
| `scratch_gkp_ffm_phases.py` | J1–J5: six examples, FE, Gauss sums, page phases, Tate products for five own $\psi$, the 30/50 count | 4 s |
| `scratch_gkp_ffm_census.py` | J1, J4, J12: census of irreducible moduli, RH, product $=W$, $W=1$ for $N=2$ (rows up to $(5,2,5)$ reported; the last row $(5,4,5)$ was not waited for) | ~10 min |
| `scratch_gkp_ffm_repeated.py` | J7, J12: squarefree moduli with repeated roots in $P_\chi$; with argument `deg`, the degree check of J1 | ~10 min |
| `scratch_gkp_ffm_lattice.py` | J6, J8, J10: $R$, index, $\sigma$, trace form, $\Omega_+$, Smith invariants, $\mathrm{charpoly}$, $\det_{\mathbb Z}F$ | 6 s |
| `scratch_gkp_ffm_fermat.py` | J7: Fermat quartic counterexample | 3 s |
| `scratch_gkp_ffm_vacuum.py` | J9, J4 (B5): vacuum on $R$, CRT factorisation | 5 s |
| `scratch_gkp_ffm_curves.py` | J11, J12: point counts of $y^N=cf$, twisted control, `hyperellcharpoly`, $\prod W(\chi^j)$ | 1 s |
| `scratch_gkp_ffm_lps.py` | M3 (pass `full` for all three commutant sub-blocks, ~4 min) | 30 s |
| `scratch_gkp_ffm_lps_vertexJ.py` | M3: $\max\lvert J_{13}-J_{17}\rvert$ in the vertex basis | 20 s |
| `scratch_gkp_ffm_m1zeta.py` | M1, M2, M4 | 4 s |
