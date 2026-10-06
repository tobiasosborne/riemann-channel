# A repeated root: the companion lattice against the Jacobian's lattice

Author: `claude:opus-5.5`, 2026-10-06, lane S of an orchestrated session.

Status: **a record, not a round; nothing registered in db/claims.tsv; no REFUTE review; no shard.** Each statement is labelled *standard*
(classical; "from memory" unless a `refs/src` line is given), *proved here*, *checked* (`checks/check_repeated_root.py`), *sketched*,
*heuristic*, *open* or *negative finding*. Checks: `checks/check_repeated_root.py`, output `checks/output_repeated_root.txt`,
**31 of 31 pass** (about 1 s; python-flint for the field arithmetic, sympy exact, PARI/GP 2.15.4 by subprocess).

Resolves the repeated-root case found by the review of `ff-dirichlet.md` (`notes/reviews/adelic-gkp-ff-family-2026-10-06.md`, J7): $q=5$, $N=4$,
$f=t^4+1$, $P_\chi=(x+1+2i)^2$. RH holds, but the companion order $R=\mathbb Z[i][F,V]$ has a degenerate trace form, a non-semisimple $F$ and no vacuum.

**Verdict.**

- **The curve** is the Fermat quartic $y^4=t^4+1$ over $\mathbb F_5$, of genus 3. Infinity is not a branch point. Its zeta numerator is
  $(1+2u+5u^2)^2(1-2u+5u^2)=\Lambda(\chi)\Lambda(\chi^2)\Lambda(\chi^3)$ (*checked*).
- **The Jacobian's lattice is semisimple.** On the $\chi\oplus\bar\chi$ part $A_J$ of the Jacobian, Frobenius is the CM element $-1-2\iota$, where $\iota$ is
  the automorphism $y\mapsto2y$. Its Deligne module is $\mathbb Z[i]^2$ with $F=\alpha I$, $\alpha=-1-2i$, on the nose and not only up to isogeny.
  It carries a principal form, a positive Weil form and the vacuum $J=-i$. Status: *proved here* from Kani–Rosen (quoted) and an exact group-law
  check; independently it is *standard* by Weil's semisimplicity.
- **The companion lattice $R$ is not that lattice, even rationally** (*checked*). It has the same characteristic polynomial, but $F-\alpha$ is a non-zero
  nilpotent. Its groups $R/(1-F^k)R$ differ from the geometric ones for every $k=1..6$; for $k=1$ they are $(\mathbb Z/8)^2$ against
  $(\mathbb Z/2\times\mathbb Z/4)^2$. Every compatible form on $R$ is either degenerate or has an indefinite Weil form, and $R$ has no vacuum.
- **For the ladder.** Semisimplicity is not a hypothesis beside RH on the geometric lattice. Weil gets both from one positivity, the Rosati form on
  $\mathbb Q[\pi]$. It is a hypothesis only for lattices built from the polynomial: the companion step, the order $R$, and Connes's cokernel. Connes
  states that his operator acquires a Jordan block at a multiple zero (`refs/src/math/9811068/main.tex:949-952`). This corrects the brief, which
  said Connes realises multiplicities as the dimension of an eigenspace.

---------------------------------------------------------------------------------------------------------------------------------------------

## 1. The curve

**1.1 Which curve (*proved here*; checked A1, A9).** By the reciprocity condition of `ff-dirichlet.md` §2.6, $c^{(q-1)/N}=(-1)^{(q-1)d/N}$. Here
$(q-1)/N=1$ and $d=4$, so $c=1$ and $C$ is $y^4=t^4+1$, the Fermat quartic $Y^4=T^4+Z^4$. The twists $c=2,3,4$ have different counts over $\mathbb F_5$,
$\mathbb F_{25}$ and $\mathbb F_{125}$, so matching counts also fixes $c=1$.

**1.2 Genus (*proved here*; checked A2, A3).** The map $t\colon C\to\mathbb P^1$ has degree 4.

- $t^4+1=(t^2+2)(t^2+3)$ has four distinct roots, all in $\mathbb F_{25}\setminus\mathbb F_5$. Each is totally ramified, since $v_b(t^4+1)=1$ is prime to 4.
- **Infinity is not a branch point**, because $v_\infty(t^4+1)=-4\equiv0\bmod4$. It splits into the four places $y/t\in\mu_4\subset\mathbb F_5$, all rational
  over $\mathbb F_5$.
- Riemann–Hurwitz gives $2g-2=4(-2)+4\cdot3=4$, so $g=3$. The plane model is smooth in characteristic 5, also of genus $(4-1)(4-2)/2=3$, and gives the
  same counts.

**1.3 Counts and the $L$-polynomial (*checked* A3, A4, A8, A11, A14).** Brute force over $\mathbb F_{5^k}$ (affine points plus 4 at infinity):

| $k$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $\#C(\mathbb F_{5^k})$ | 8 | 44 | 104 | 668 | 3208 | 14924 |
| $\#E$, $y^2=x^3+x$ | 4 | 32 | 148 | 640 | 3044 | 15392 |
| $\#E'$, $y^2=x^3+4x$ | 8 | 32 | 104 | 640 | 3208 | 15392 |
| $\#J=\prod_j(1-\alpha_j^k)$ | 256 | 32768 | 1600768 | 262144000 | 31326607616 | 3646575116288 |

- $N_1,N_2,N_3$ give $L_C(u)=(1+2u+5u^2)^2(1-2u+5u^2)$. This predicts $N_4,N_5,N_6$, which the brute force confirms.
- From character sums, with $\chi=\prod_P(\cdot/P)_4$ and $2\mapsto i$:
  - $\Lambda(u,\chi)=1+(2+4i)u+(-3+4i)u^2$, the review's polynomial, with $P_\chi=(x-\alpha)^2$ and $\alpha=-1-2i$;
  - $\Lambda(u,\chi^3)=\overline{\Lambda(u,\chi)}$;
  - $\Lambda(u,\chi^2)=1-2u+5u^2$.

  All three characters are even, and the product of the three $\Lambda$ is $L_C$ exactly.
- $\#J=\#E\cdot\#E'^2$ for $k=1..6$.

**1.4 The Klein-four quotients (*standard*, Kani–Rosen, from memory: E. Kani, M. Rosen, *Idempotent relations and factors of Jacobians*, Math. Ann.
284 (1989); checked A11–A13).** Take $\sigma_1\colon y\mapsto-y$, $\sigma_2\colon t\mapsto-t$ and $\sigma_3=\sigma_1\sigma_2$.

| quotient | model | Weierstrass form | role |
|---|---|---|---|
| $C/\sigma_1$ | $w^2=t^4+1$ | $E\colon Y^2=X^3+X$ | the $\chi^2$-part, $a_E=2$ |
| $C/\sigma_2$ | $z^2=r^4-1$ ($r=y$, $z=t^2$) | $E'\colon Y^2=X^3+4X$ | part of the $\chi\oplus\bar\chi$ part, $a_{E'}=-2$ |
| $C/\sigma_3$ | $z^2=r^4-1$ ($r=y/t$) | $E''=E'$ | the rest of the $\chi\oplus\bar\chi$ part |
| $C/\langle\sigma_1,\sigma_2\rangle$ | the conic $w^2=s^2+1$ | — | genus 0 |

- The transform $X=2(z+r^2)$, $Y=4r(z+r^2)$ takes $z^2=r^4+b$ to $Y^2=X^3-4bX$.
- Since the quotient by the whole group has genus 0, Kani–Rosen gives $J\sim E\times E'\times E''$ over $\mathbb F_5$.
- Each quotient map commutes with $\iota\colon y\mapsto\zeta y$. On $E'$ and $E''$, $\iota$ acts as $r\mapsto\zeta r$, which is $(X,Y)\mapsto(1/X,\zeta Y/X^2)$. It moves the origin to $(0,0)$, so the
  group automorphism $[\iota]$ is $\iota$ followed by translation by $(0,0)$.
- $E'$ is the curve $y^2=x^3+4x$ of `curve-bridge.md` §2, with $j=1728$ and $\mathrm{End}=\mathbb Z[i]$.

## 2. Semisimplicity: what is proved, what is checked, what is quoted

**2.1 Weil's semisimplicity (*standard*; byte-cited from Milne's survey, `refs/src/1509.00797/pRH.tex:1593-1594, 1605-1618, 1635-1641`).**
$\mathrm{End}^0(A)$ is semisimple. $\mathbb Q[\pi]$ is stable under a Rosati involution $\dagger$, which satisfies $\mathrm{Tr}(\beta\beta^\dagger)>0$, so $\mathbb Q[\pi]$ is "semisimple, and hence a
product of fields". The same corollary gives $|\rho(\pi)|=q^{1/2}$.

So Frobenius is semisimple on $V_\ell$, and semisimplicity and RH come out of **one** positivity. The brief's attribution, Tate 1966 (*Endomorphisms of
abelian varieties over finite fields*, Invent. Math. 2), is for $\mathrm{End}^0\otimes\mathbb Q_\ell\cong\mathrm{End}_{\mathbb Q_\ell[\pi]}V_\ell$. It is not needed here.

**2.2 A direct proof for this curve (*proved here*, given Kani–Rosen; checked B1–B3).**

- $E'$ is ordinary with $\mathrm{End}(E')=\mathbb Z[\iota]\cong\mathbb Z[i]$. So $\pi_{E'}\in\{-1\pm2\iota\}$.
- With $\iota_2\colon r\mapsto2r$, the endomorphism $\pi+1+2[\iota_2]$ kills every point of $E'(\mathbb F_{5^k})$ for $k=1,2,3$. The conjugate $\pi+1-2[\iota_2]=-4[\iota_2]$
  fails on 16 of 32 points over $\mathbb F_{25}$ and 96 of 104 points over $\mathbb F_{125}$. So $\pi_{E'}=-1-2\iota_2$ exactly. The same holds for $E''$, with the same model
  and the same $\iota$.
- Kani–Rosen's isogeny commutes with $\iota$ and $\pi$. Hence on $A_J:=(1-\iota^2)J$, the abelian surface where $\iota^2=-1$, we have
  $\pi=-1-2\iota$ in $\mathrm{End}^0(A_J)$, and so in $\mathrm{End}(A_J)$.
- Frobenius is therefore semisimple on $V_\ell(J)\cong V_\ell(E)\oplus V_\ell(E')^2$. Each block is $2\times2$ with an irreducible characteristic polynomial.

That $\iota_2$ goes with $\alpha=-1-2i$ under $2\mapsto i$ matches the convention for $\chi$. I observed this and did not derive it.

**2.3 The lattice of $A_J$ is $L=\mathbb Z[i]^2$ with $F=\alpha I$, on the nose (*proved here*, given Deligne's theorem, `lattice-tower.md` §6).**

- $J$ is ordinary: the middle coefficient of $P_C=x^6+2x^5+11x^4+12x^3+55x^2+50x+125$ is 12, prime to 5 (A10). So $A_J$ has a Deligne module $T$.
- $\iota$ acts on $T$ with $\iota^2=-1$, so $T$ is a torsion-free $\mathbb Z[i]$-module of rank 2. It is free because $\mathbb Z[i]$ is a PID.
- $F=-1-2\iota$ acts on it as the scalar $\alpha$.
- With Deligne's group identification (*standard*, from memory; Lenstra for $g=1$), $A_J(\mathbb F_{5^k})\cong(\mathbb Z[i]/(1-\alpha^k))^2$.

**2.4 What the counts can and cannot see (*checked* A14, B4–B6; *negative finding* for counts).**

- Orders such as $\#J$, $\#E'$ and $|L/(1-F^k)L|=|R/(1-F^k)R|$ are traces and determinants. They are the same for a Jordan block and for $\alpha I$, so
  **no count can test semisimplicity**.
- What does test it is a group structure.
  - $E'(\mathbb F_{5^k})\cong\mathbb Z[i]/(1-\alpha^k)$ for $k=1..6$: $\mathbb Z_2\times\mathbb Z_4$, $\mathbb Z_4\times\mathbb Z_8$, $\mathbb Z_2\times\mathbb Z_{52}$, $\mathbb Z_8\times\mathbb Z_{80}$,
    $\mathbb Z_2\times\mathbb Z_{1604}$, $\mathbb Z_4\times\mathbb Z_{3848}$.
  - So $E'\times E''$, which is in the isogeny class of $A_J$ with the same $\mathbb Z[\iota]$-action, has the groups of $L$ for every $k$:

    | $k$ | $L/(1-F^k)L$ | $R/(1-F^k)R$ |
    |---|---|---|
    | 1 | $(\mathbb Z_2\times\mathbb Z_4)^2$ | $\mathbb Z_8^2$ |
    | 2 | $(\mathbb Z_4\times\mathbb Z_8)^2$ | $(\mathbb Z_2\times\mathbb Z_{16})^2$ |
    | 3 | $(\mathbb Z_2\times\mathbb Z_{52})^2$ | $\mathbb Z_8\times\mathbb Z_{1352}$ |

    The groups also differ for $k=4,5,6$.
- **Not computed:** the group $J(\mathbb F_{5^k})$ itself and the $\ell$-adic Tate module. A divisor-class computation on the plane quartic was not attempted.
  §2.2 replaces it by Kani–Rosen together with the group law on $E'$.
- **The same phenomenon in genus one (*checked* B6).** $y^2=x^3+1$ over $\mathbb F_{25}$ is supersingular, with $P=(x+5)^2$ and $\pi=-5$ (the scalar).
  - Its group is $\mathbb Z_6\times\mathbb Z_6=\mathbb Z^2/6\mathbb Z^2$.
  - The companion of $(x+5)^2$ gives $\mathbb Z_{36}$.
  - The one-mode rung's companion step at $\lambda^2=4q$ is a Jordan block, and the curve's lattice is $-5I$.

## 3. The two lattices side by side (checked C1–C10)

$L=\mathbb Z[i]^2$ with $F=\alpha I$ and $V=\bar\alpha I$. $R=\mathbb Z[i]e_0+\mathbb Z[i]e_1$ with $e_1=(F-\alpha)/(2-i)$, inside $E=\mathbb Q(i)[x]/(x-\alpha)^2$. Then
$Fe_0=\alpha e_0+(2-i)e_1$, $Fe_1=\alpha e_1$, and $Ve_0=\bar\alpha e_0+(2+i)e_1$. This $R$ is the review's: $[R:\mathbb Z[i][F]]=5$ (C3).

| | $L$ (geometric) | $R$ (companion order) |
|---|---|---|
| $FV=VF=5$, $V$ integral | yes | yes |
| $\mathrm{charpoly}_{\mathbb Z}F$ | $(x^2+2x+5)^2$ | $(x^2+2x+5)^2$ |
| $F^2+2F+5$ | $0$: semisimple, $F=\alpha I$ | rank 2: $F-\alpha\ne0$, $(F-\alpha)^2=0$ |
| trace form $\mathrm{Tr}(x\sigma y)$ | the recipe copy by copy: $\tfrac12\mathrm{Tr}(x\sigma y)=\sum\lvert x_k\rvert^2$, positive definite | rank 2 of 4 (the nilradical is isotropic) |
| $\Omega_+=\mathrm{Tr}(x\,\sigma y/(V-F))$ | $\tfrac12\omega$, with $\omega=-\mathrm{Im}(x^\dagger y)$ of det 1 (principal) | degenerate, rank 2 |
| all compatible alternating forms | $\omega_H=-\mathrm{Im}(x^\dagger Hy)$, $H$ Hermitian: dimension 4 | dimension 2; generic member non-degenerate |
| Weil form $\tfrac12\Omega(F-V)$ | $2\,\mathrm{Re}(x^\dagger Hy)$: definite iff $H$ definite; for $\omega$ it is $2I_4=\lvert\mathrm{Im}\,\alpha\rvert\,G_J$ | inertia $(2,2)$ on 6 random non-degenerate members; never definite |
| vacuum | $J=-i$ (that is $-\iota$): $J^2=-1$, $JF=FJ$, $G_J=I_4$; equals $(F-V)(4q-(F+V)^2)^{-1/2}$ | none: $\lVert(F/\sqrt5)^k\rVert=10.1,\ 100.0,\ 1000.0$ at $k=10,100,1000$ |

**3.1 No definite Weil form and no vacuum on $R$ (*proved here*).** Let $\Omega$ be any compatible form. Its Weil form $B=\tfrac12\Omega(\cdot,(F-V)\cdot)$ is
symmetric and satisfies $B(Fx,Fy)=5B(x,y)$.

- If $B$ were definite, $F/\sqrt5$ would be orthogonal for a positive form, hence semisimple. It is not.
- A vacuum $J$ would give the positive form $G_J=\Omega J$ with $S^TG_JS=G_J$ for $S=F/\sqrt5$. The same argument applies.
- A degenerate $\Omega$ has $\Omega(x,Jx)=0$ on its kernel.

This is `family-vacuum.md` Prop. 1, (i)⇒(ii), applied to $R$.

**3.2 Two corrections to the brief's recipe for $L$ (*checked* C6, C7).**

- (a) The Hermitian form $\mathrm{Tr}_{\mathbb Z[i]/\mathbb Z}(x^\dagger J_{\rm std}y)$ with the standard alternating $J_{\rm std}$ on $\mathbb Z[i]^2$ is a compatible form, with
  $H=-iJ_{\rm std}$. But $H$ is indefinite, and its Weil form has inertia $(2,2)$. It is not "positive or negative definite".
  - The definite Weil forms are exactly the $\omega_H$ with $H$ definite. That is the CM-type condition of lane E (`cone-bridge.md`), here a 4-dimensional
    open cone.
  - $H=\mathrm{diag}(1,-1)$ has an indefinite Weil form and still a vacuum ($-i\oplus i$). This is the precision recorded in `data-ladder.md` §0.
- (b) In the orientation where the Weil form is positive ($\omega=-\mathrm{Im}\,x^\dagger y$), the vacuum is multiplication by $-i$, not $+i$. The vacuum
  $J=-\iota$ is the same for every $H>0$.

**3.3 The algebra that acts (*proved here*, from 2.1).** The map $E\to\mathrm{End}^0(A_J)$, $x\mapsto\pi$, is not injective: it kills the nilradical $(x-\alpha)$. The
algebra that acts on the geometric lattice is its image $\mathbb Q[\pi,\iota]=\mathbb Q(i)$. There the trace form is the Rosati form, which is positive.

So the degenerate form of review J7 is the trace form of an algebra that is not $\mathbb Q[\pi]$. "Positivity is RH" (`ff-dirichlet.md` §2.3) is correct for the
algebra that actually acts.

## 4. The ladder statement

- **L1 (*proved here*; checked C2, A10).** The companion/cokernel constructions build the lattice from the polynomial alone. These are lane A's companion
  step on the Riemann–Roch cokernel (`curve-bridge.md` §4) and lane J's order $R=\mathbb Z[\zeta][F,V]$ (`ff-dirichlet.md` §2.2).
  - Rationally they give $\bigoplus_i\mathbb Q(\zeta)[x]/(p_i^{m_i})$, while the $\chi$-part of $H_1$ is $\bigoplus_i(\mathbb Q(\zeta)[x]/(p_i))^{m_i}$.
  - The two agree if and only if $P$ is squarefree.
- **L2 (*checked*; negative finding).** With a repeated root, the construction gives a non-semisimple module that is not the Jacobian's.
  - For the Fermat quartic: $R$ against $L$. The groups differ for $k=1..6$, and no compatible form on $R$ has a definite Weil form.
  - The same happens already for the trivial character: the curve's own $P_C=(x^2+2x+5)^2(x^2-2x+5)$ has a non-semisimple companion step on $\mathbb Z^6$.
- **L3 (*proved here*, given Kani–Rosen; also *standard* by 2.1).** The geometric lattice is semisimple: $F=\alpha I$ on $\mathbb Z[i]^2$. It has a principal
  $\omega$, a positive Weil form $2I_4$ and the vacuum $J=-i$.
- **L4 (*standard*, 2.1; the reading is *proved here*).** In the ladder, "RH with semisimplicity" (`lattice-tower.md` §5 (i); `data-ladder.md` §0) is
  one condition on the **geometric** lattice. Weil derives both halves from the positivity of the Rosati form on $\mathbb Q[\pi]$. Semisimplicity is a separate
  hypothesis only for a lattice built from $P$, and there it fails at every repeated root whether or not RH holds.
- **L5 (*proved here* on the example; *standard* in general).** The finite analogue of a multiple zero is a repeated Frobenius eigenvalue.
  - It costs nothing geometrically: $F=\alpha I$, the multiplicity is the dimension of the eigenspace, and the vacuum and the positive Weil form persist.
  - It breaks the companion construction, which turns the multiplicity into a Jordan block.
  - It is not rare: it happens whenever the Jacobian has a repeated isogeny factor, as $E'^2$ does here, or in the supersingular genus-one case $\pi=\pm p$.
- **L6 (*standard*, from memory: Weil's explicit formula).** For $\zeta$, a multiple zero enters Weil's functional with its multiplicity as a weight. Take
  $g=h*\tilde h$ with $\tilde h(x)=\overline{h(x^{-1})}$.
  - In general the zero side is $\sum_\rho m_\rho\,\hat h(\rho)\overline{\hat h(1-\bar\rho)}$, a sum over distinct zeros.
  - Under RH it is $\sum_\rho m_\rho|\hat h(\rho)|^2\ge0$. Positivity is unchanged by multiplicities, since $m_\rho\ge1$.
  - Off-line pairs contribute indefinite cross terms whatever their multiplicity.
- **L7 (*standard* spectral theorem; the reading is *heuristic*).** On a Hilbert space where the squeeze flow is unitary with spectrum the zeros, the
  generator is self-adjoint, hence diagonalisable. Multiplicities are then eigenspace dimensions, as with $F=\alpha I$, and semisimplicity is automatic.
  So for $\zeta$ semisimplicity is not a separate datum: it is part of what a geometric (unitary) realisation would be.
- **L8 (*standard*, byte-cited; a correction to the brief).** Connes's cokernel is a construction of the companion type. In the weighted space
  $L^2_\delta$, $\delta>1$, "When the zeros of $L$ have multiplicity and $\delta$ is large enough the operator $D$ is *not* semisimple and has a non trivial
  Jordan form ... compatible with the almost unitary condition (22) but not with skew symmetry for $D$" (`refs/src/math/9811068/main.tex:949-952`;
  the multiplicity clause of Theorem 1 is at :882-885).
  - So Connes realises a multiple zero as a Jordan block, not as the dimension of an eigenspace. That is the finite picture of $R$, not of $L$.
  - Theorem 1 "has a similar formulation" in positive characteristic (:888). That the Fermat quartic's double eigenvalue would appear there as a
    $2\times2$ Jordan block is my inference (*heuristic*).

## 5. Status and checks

| statement | status | checks |
|---|---|---|
| $c=1$; genus 3; $\infty$ unramified, four rational places; counts $k=1..6$ | proved here; checked | A1–A3, A9 |
| $L_C=(1+2u+5u^2)^2(1-2u+5u^2)=\prod_j\Lambda(\chi^j)$, $P_\chi=(x-\alpha)^2$ | checked exactly | A4–A8 |
| $J\sim E\times E'\times E''$ | standard (Kani–Rosen, from memory); hypotheses and $L$-factorisation checked | A11–A13 |
| $\#J$ for $k=1..6$; counts are blind to semisimplicity | checked; elementary | A14 |
| $\pi_{E'}=-1-2\iota_2$ in $\mathrm{End}(E')$ | checked (group law), proved with $\mathrm{End}(E')=\mathbb Z[i]$ | B1–B3 |
| Frobenius semisimple on $V_\ell(J)$ | proved here given Kani–Rosen; standard (Weil, via Milne `pRH.tex:1605-1618`) | — |
| Deligne module of $A_J$ is $\mathbb Z[i]^2$, $F=\alpha I$ | proved here given Deligne's theorem (quoted) | B4 (for $E'$) |
| groups: $E'\times E''$ match $L$, never $R$ ($k=1..6$); genus-one supersingular analogue | checked | B5, B6 |
| $L$: principal $\omega$, positive Weil form, vacuum $-i$; the cone of $H>0$; indefinite $H$ | checked exactly | C1, C4–C7 |
| $R$: non-semisimple; trace form rank 2; $\Omega_+$ degenerate; compatible forms never with definite Weil form; no vacuum | checked; proved (3.1) | C2, C3, C8–C10 |
| L1–L5 | proved here / checked on the example | as above |
| L6, L7 | standard; the reading is heuristic | — |
| L8 | standard, byte-cited (Connes `math/9811068:main.tex:949-952`) | D1 |

Not done: the group $J(\mathbb F_{5^k})$ and the Tate module of $J$ itself; the $\chi$-convention matching $\iota_2\leftrightarrow i$ (observed, not derived);
the inertia $(2,2)$ on $R$ as a theorem (checked on random members only).

## 6. Next

- Annotate `ff-dirichlet.md` §2.3/§2.6 and `data-ladder.md` §0. The Dirichlet row's lattice should be the $\chi$-part of $H_1$, which is
  $\bigoplus(\mathbb Z[\zeta][x]/p_i)^{m_i}$ up to isogeny. It equals $R$ only for squarefree $P_\chi$, and the "degenerate for a repeated root" entry belongs
  to $R$, not to the rung.
- Lane A's genus-one dictionary (`curve-bridge.md` §4) should note the supersingular case $a^2=4q$, where the cokernel shift is a Jordan block and the
  curve's lattice is $\pm\sqrt q\,I$.
- For $\zeta$: test whether any proposed integral or Hilbert structure on Connes's cokernel semisimplifies it, that is, replaces the Jordan
  form by eigenspaces. That is the one place where L7 and L8 would have to meet.
- Optional: a divisor-class computation on the plane quartic, to check $(\pi+1+2\iota)(1-\iota^2)=0$ on $J$ directly without Kani–Rosen.
