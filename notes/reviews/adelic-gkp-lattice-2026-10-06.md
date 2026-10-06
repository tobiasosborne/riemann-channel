# Adversarial review: the lattice lanes of the adelic-GKP session (`curve-bridge.md`, `cone-bridge.md`, `overlap-data.md`)

- **Date:** 2026-10-06
- **Reviewer:** claude:opus-5.5 (REFUTE lane)
- **Authors under review:** claude:opus-5.5, lanes A (`curve-bridge.md`), E (`cone-bridge.md`), F (`overlap-data.md`); orchestrator claude:fable-5.1
- **Files under review:** `notes/adelic-gkp/curve-bridge.md`, `notes/adelic-gkp/cone-bridge.md`, `notes/adelic-gkp/overlap-data.md`: every statement labelled *proved here* or *checked*. Context read but not reviewed: `data-ladder.md`, `lattice-tower.md` §§5–6, `howe-positivity.md` §§1–2, `notes/weil-bond-analytic/analytic.md` §§13–14.
- **Also adjudicated:** the three headline claims `data-ladder.md` takes from these pages (S1–S3 below), and one sentence of `data-ladder.md` §0 (S0) that contradicts lane E.
- **Independent numerics:** four scratch scripts `notes/reviews/scratch_gkp_lattice_*.py`, written from the *statements* only. No code from `notes/adelic-gkp/checks/` was read or reused. Everything was rebuilt from scratch: the symbolic bridge, the Riemann–Roch cokernel, a brute-force $h^0$ on E1 over $\mathbb F_4$, the genus-two order $\mathbb Z[F,V]$ from its four complex embeddings, the 5-adic types in the degree-8 Galois closure, and Weil-pairing scale sets on $E[n]$ in independently chosen bases. PARI/GP 2.15.4 was called through the `gp` binary.
  - `scratch_gkp_lattice_curve.py` (38/38): sympy with symbolic $q,a$, plus PARI groups for $k\le6$.
  - `scratch_gkp_lattice_e1h0.py`: 144 divisors, 0 mismatches.
  - `scratch_gkp_lattice_cone.py` (28/28): mpmath at 50 digits, plus PARI.
  - `scratch_gkp_lattice_overlap.py` (19/19): PARI, with $E[n]$ for $n=3,4,5,8,9,16$ over $\mathbb F_{7^k}$, $k$ up to 16.

**Headline. 22 VALID / 6 MINOR / 0 INVALID.** I could not break any of the three headline claims. Every sign, transpose and direction I attacked survived, and so did every scalar and every count I recomputed. That covers $\Omega$ against $M^T$, $V=qM^{-1}$, the direction $W\mapsto V$ of the cokernel map, the Rosati Gram matrix, the Krein signs, the determinant 441, and the weights 10.870 and 20.171. It also covers the 8 primes above 5 and their types, the scale sets $\{2\}$, $\{3,5\}$ and $\{3,5,11,13\}$, the ε-assignment $j=5$ for $s\equiv3$, and the count 22860. The six MINORs are precision faults:

- one overreach in the genus-one bridge, which reaches "the Deligne module" only for the principal class (A-5b, inherited by the synthesis as S1);
- one false "general form" proposed by lane E for `lattice-tower.md` §5 (E-X3). A step with a real eigenvalue $\pm\sqrt q$ satisfies (i) and (iii) but has *every* Weil form identically zero;
- one headline count misstated (E-H);
- one implication in Lemma 1 of lane F that is false as written, though its hypothesis is fixed by the word "Frobenius" (F-L1);
- one sentence of the synthesis's §0 that still asserts the equivalence lane E refuted (S0).

---

## Lane A: `curve-bridge.md`

### A-D: Deligne modules of E1–E3; the Weil form of a step is its Latimer–MacDuffee form (D1–D3)

**Claim (one line).** $M_{(A,B,C)}=\bigl(\begin{smallmatrix}(a-B)/2&-C\\A&(a+B)/2\end{smallmatrix}\bigr)$ has $\tfrac12\Omega(M-V)=\bigl(\begin{smallmatrix}A&B/2\\B/2&C\end{smallmatrix}\bigr)$, and $\mathrm{GL}_2(\mathbb Z)$-classes of steps correspond to proper classes of positive forms.

**VERDICT A-D: VALID**

Attacks tried and what happened.
- *Symbolic check.* I verified the formula symbolically in $A,B,C,a$ and checked $\det M_{(A,B,C)}=q$ under $B^2-4AC=a^2-4q$. The companion matrix is $(q,a,1)$.
- *Improper conjugation, the place where "$\mathrm{GL}_2$ versus proper classes" usually slips.* Conjugating by $\mathrm{diag}(1,-1)$ sends $M_{(A,B,C)}$ to $M_{(-A,B,-C)}$, whose Weil form is *negative* definite. Each $\mathrm{GL}_2(\mathbb Z)$-class therefore holds one $\mathrm{SL}_2$-class with a positive Weil form and one with a negative Weil form. The stated bijection with proper classes of *positive* forms is right, and this is exactly the mechanism behind E-X3's $M'$.
- *Reduced forms.* Discriminant $-16$ has reduced forms $(1,0,4)$ and $(2,0,2)$. Discriminant $-24$ has $(1,0,6)$ and $(2,0,3)$.
- *Cyclic vectors.* $(2,0,3)$ has no cyclic vector, because $\det[v,Mv]=2x^2+3y^2\ne\pm1$.
- *From memory.* Latimer–MacDuffee: I recall it the same way. Conjugacy classes of integer matrices with irreducible characteristic polynomial $f$ correspond to classes of $\mathbb Z[x]/(f)$-lattices in $\mathbb Q[x]/(f)$, that is, ideal classes of all orders containing $\mathbb Z[\alpha]$.

### A-G: groups of points; the companion-lattice negative finding; $A(\mathbb F_{q^k})\cong T/(1-F^k)T$ (G1–G8, theorem sketched)

**Claim.** For each curve, $E(\mathbb F_{q^k})\cong\mathbb Z^2/(1-M_T^k)$ with $M_T$ the step of *its own* form class. The companion matrix fails for $y^2=x^3+4x$ over $\mathbb F_5$ at every $k$.

**VERDICT A-G: VALID**

- *PARI, $k=1..6$, every equation.* Every curve matches the Smith normal form of $1-M^k$ for its predicted class. For E2 with $b=0$ ($j=3$, groups $\mathbb Z_2\times\mathbb Z_4$, $\mathbb Z_4\times\mathbb Z_8$, $\mathbb Z_2\times\mathbb Z_{52}$, $\mathbb Z_8\times\mathbb Z_{80}$) the companion matrix fails at every $k$. For E1, E2 with $b=1,4$ ($j=1$) and E3 it matches. The two E3 curves have equal groups for all $k\le24$ (PARI on the curves themselves). That is stronger than the page's own curve check ($k\le8$), and it makes `data-ladder.md`'s "for all $k\le24$" true as written.
- *Hand counts.* $\#E(\mathbb F_5)=8$ for $y^2=x^3+4x$, with full rational 2-torsion. $\mathbb Z[i]/(2-2i)=\mathbb Z[i]/(1-i)^3\cong\mathbb Z_2\times\mathbb Z_4$. $\mathbb Z^2/(1-M_{\rm comp})\cong\mathbb Z_8$.
- *Theorem sketch.* The snake-lemma step is right: $\varphi$ is bijective on $T\otimes\mathbb Q$, so $\ker(\varphi\mid T\otimes\mathbb Q/\mathbb Z)\cong\mathrm{coker}(\varphi\mid T)$. On the non-unit-root part $F=qV^{-1}$ with $V$ a unit, so $1-F^k$ is invertible there. The status "sketched" is honest.
- *From memory.* Lenstra, *Complex multiplication structure of elliptic curves*, J. Number Theory 56 (1996): I recall it the same way, with $E(\mathbb F_q)\cong\mathcal O/(\pi-1)$ as $\mathcal O$-modules for $\mathcal O=\mathrm{End}_{\mathbb F_q}(E)$ of rank 2. Its hypothesis is rank 2 of the $\mathbb F_q$-rational endomorphism ring, and that is automatic for ordinary curves. Deligne, Invent. Math. 8 (1969): same recollection of $T=H_1$ of the canonical lift. Honda–Tate and Tate's isogeny theorem: same.

### A-3: overlaps are counts on E1 (A1–A8)

**Claim.** $\langle\Theta_K,1_{nO-E}\rangle=2^{h^0}$, and $h^0$ agrees with Riemann–Roch plus Abel–Jacobi on 144 divisors. $A(n)$ and $a_n$ follow, and $P(T)=1+T+2T^2$.

**VERDICT A-3: VALID**

- *Independent brute force* (`scratch_gkp_lattice_e1h0.py`). I wrote my own $\mathbb F_4$ arithmetic and group law for $y^2+xy=x^3+1$, and computed $h^0$ by $\mathbb F_2$-linear algebra on the stated basis of $L(nO)$. The same divisor family has exactly **144** members, with **0 mismatches** against Riemann–Roch plus Abel–Jacobi. $h^0(nO)=0,1,1,2,3,4,5,6$ for $n=-1..6$.
- *By hand.* $N_1..N_5=4,8,4,16,44$, so the place counts are $4,2,0,2,8$. $a_n=4(2^n-1)$ for $n\ge1$, and $A(0)=(q-1)/h=1/4$.

### A-4: the Theorem 12 cokernel for E1 and E2 (R1–R5)

**Claim.** At cutoff $N=5$ the cokernel has dimension 2, its solutions satisfy $Y_j-aY_{j-1}+qY_{j-2}=0$, $W=\bigl(\begin{smallmatrix}a&-q\\1&0\end{smallmatrix}\bigr)$, and both Casoratians are $q$-similitudes.

**VERDICT A-4: VALID**

- I rebuilt the admissible $c$, the orbit vectors $Ef$ from $A(n)$ (Riemann–Roch) and the orthogonal complement in exact rationals.
  - $Ef$ vanishes outside $[-5,5]$.
  - The complement has dimension 2 for both E1 and E2.
  - The recurrence holds on the whole window.
  - The Casoratian similitude $\mathcal Q(s_{j+1})=q\,\mathcal Q(s_j)$ and $W^T\Omega W=q\Omega$ hold symbolically.
- The Casoratian matrix $\bigl(\begin{smallmatrix}1&-a/2\\-a/2&q\end{smallmatrix}\bigr)$ is the one in analytic Corollary 13.

### A-5a: the maps $C$, $\psi$, $S$ (B1–B5)

**Claim.** $C:s\mapsto Y_j-Y_{j-1}F$ carries $W$ to multiplication by $V$ and $\mathcal Q$ to $\tfrac12\mathcal T$. $\psi:\varphi\mapsto\varphi(M)e_2$ carries $F$ to $M$ and $\tfrac12\mathcal T$ to $G$. $S=\psi\circ{\rm Ros}\circ C=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$, with $SWS^{-1}=M$, $S^T\Omega S=\Omega$ and $S^TGS=\mathcal Q$.

**VERDICT A-5a: VALID**

- *Direction of the cokernel map (F against V), the main attack.*
  - $C(Ws)=aY_j-qY_{j-1}-Y_jF$.
  - $V\cdot C(s)=Y_j(a-F)-qY_{j-1}$.
  - These are equal, so the shift goes to $V$, not $F$.
  - $V$ is the $\mathcal T$-adjoint of $F$: $\mathcal T(F\varphi,\psi)=\mathcal T(\varphi,V\psi)$. This agrees with analytic Proposition 14, where the shift is a transpose.
- *Rosati Gram.* $\mathcal T(1,F)=\mathrm{Tr}\,V=a$ and $\mathcal T(F,F)=\mathrm{Tr}\,FV=2q$, so the Gram matrix is $\bigl(\begin{smallmatrix}2&a\\a&2q\end{smallmatrix}\bigr)$.
- *The Rosati involution.* It is a $\mathcal T$-isometry.
- *The factorisation.* All listed identities hold symbolically in $q,a$, including the factorisation of $S$. $\det[e_2,Me_2]=1$.
- *Transpose conventions.* $\Omega(x,y)=x^T\Omega y$ and $M$ acts on columns. $M^T\Omega=\Omega V$ gives the adjunction $\Omega(Mx,y)=\Omega(x,Vy)$, so no transposes are hidden.

### A-5b: the bridge identity, and the sentence that places it on "the Deligne module" (B6–B8)

**Claim.** $\Omega(Ss,JSs)=\tfrac{2}{\sqrt{4q-a^2}}\mathcal Q(s)=\tfrac1{\sqrt{4q-a^2}}\mathcal T(Cs,Cs)$, with $J=(2M-a)/\sqrt{4q-a^2}$. The cokernel "maps to the Deligne module by the unimodular matrix $S$", and "the content is in the explicit integral map and in the exact scalar."

**VERDICT A-5b: MINOR**

- *The identity is exact.*
  - Symbolically, $J^2=-1$, $J^T\Omega J=\Omega$ and $JM=MJ$.
  - $\Omega J=2G/\sqrt{4q-a^2}$.
  - $J=(M-V)/\sqrt{4q-a^2}$.
  - The scalars are $\sqrt7$, $4$ and $2\sqrt6$.
- *The fault.* $S$ lands on the **companion lattice** $\mathbb Z[F]$, the principal class. That is the Deligne module of the curve only when $T\cong\mathbb Z[F]$. The page itself shows this is not always so: for E2 with $b=0$, and for one of the two E3 curves, $T$ is the class $(2,0,2)$ or $(2,0,3)$. For those curves:
  - I solved $gM_{\rm comp}=M_Tg$. The smallest $|\det g|$ over integral intertwiners is **2**, in both cases.
  - The pullback of the vacuum form is $g^T\Omega J_Tg=\det(g)\,\Omega J_{\rm comp}$, which is twice the companion vacuum form. This is B10, now with the reason: $g^T\Omega g=\det(g)\,\Omega$ in rank 2.
  - So neither the unimodular integral map nor the scalar $1/\sqrt{4q-a^2}$ is a statement about *the* Deligne module. They are statements about $\mathbb Z[F]$.

**Sentence at fault** (Findings, first bullet): "The cokernel phase space $(Y_j,Y_{j-1})$ of analytic §13 maps to the Deligne module by the unimodular matrix $S$ … The content is in the explicit integral map and in the exact scalar."

**Corrected statement.** "The cokernel phase space maps by the unimodular $S$ onto the companion lattice $\mathbb Z[F]$, the principal class, carrying $W\mapsto M$, $\omega_C\mapsto\Omega$ and $\mathcal Q\mapsto G$. This is the Deligne module of the curve exactly when $T\cong\mathbb Z[F]$: for E1, for E2 with $b=\pm1$, and for one of the two E3 curves, which one depending on ε. For any other curve in the isogeny class the cokernel reaches $T$ only through a rational intertwiner. The smallest integral one has $|\det|=[\mathbb Z[F]:T]$ (here 2), and the vacuum form of $T$ pulls back to that index times the companion's. The integral map and the exact scalar $1/\sqrt{4q-a^2}$ are statements about $\mathbb Z[F]$. Over $\mathbb Q$ the bridge is the same for every curve."

### A-5c: uniqueness for one mode; other lattices over $\mathbb Q$ (B9–B10)

**Claim.** The similitude forms of an elliptic one-mode $M$ form a line. Pulled back by the rational intertwiner, the non-principal vacuum is twice the companion vacuum.

**VERDICT A-5c: VALID.** The line is the $g=1$ case of my check of Proposition 1(b) (E-P1). "Times 2" holds for the index-2 integral intertwiner and scales as $\det g$ in general, as shown in A-5b. The page should say "for the integral intertwiner of index 2", but the number is right.

### A-5d: the Howe sign cancels in the Riemann form (H1–H2)

**Claim.** In each example $p$ splits. The two choices of ε give $(\Omega_\varepsilon,J_\varepsilon)=\pm(\Omega,J)$ with the same sign, so $\Omega_\varepsilon(\cdot,J_\varepsilon\cdot)=\Omega(\cdot,J\cdot)$.

**VERDICT A-5d: VALID**

- *Splitting.* 2 splits in $\mathbb Q(\sqrt{-7})$, 5 splits in $\mathbb Q(i)$, and 7 splits in $\mathbb Q(\sqrt{-6})$ because $-6\equiv1=1^2$.
- *Why the signs agree.* The sign of $J_\varepsilon$ and the sign of $\Omega_\varepsilon$ are both fixed by $\Phi_\varepsilon$, the non-unit eigenvalue acting on $\mathrm{Lie}$ of the canonical lift. In Howe's convention, positivity is $\omega(x,\iota y)>0$ with $\varphi(\iota)\in i\mathbb R_{>0}$ for $\varphi\in\Phi_\varepsilon$, which is $\Omega_\varepsilon(x,J_\varepsilon x)>0$. The product of the two signs is $+1$ for both ε.
- *Convention attack.* Under the other classical convention, $E(ix,x)>0$, the Riemann form would read $\Omega_\varepsilon(J_\varepsilon\cdot,\cdot)$. It would still be ε-independent, and it would still be the positive one of $\pm$ the vacuum form. The cancellation does not depend on the convention.
- *Principal polarisation.* Every unimodular alternating form on $\mathbb Z^2$ is $\pm\Omega$. On every lattice class, Weil-pairing scale sets equal $\det$-sets of lattice intertwiners: this is checked in F-P3 at $n=3,4,5,8,9,16$. That independently confirms the dictionary "Weil pairing $=\Omega\bmod n$".

---

## Lane E: `cone-bridge.md`

### E-P1: Proposition 1, the cone is the open orthant and RH is the cone being non-empty

**Claim (one line).** $\mathcal C(M)\ne\emptyset$ iff $M$ is semisimple with all eigenvalues of modulus $\sqrt q$. Under squarefree $\chi$ and $|\lambda_j|<2\sqrt q$, the similitude forms are $g$-dimensional and block-diagonal over the modes, and $\mathcal C$ is the positive orthant.

**VERDICT E-P1: VALID**

- The pairing argument works: $B$ pairs $\mu$ only with $q/\mu=\bar\mu$, and $\alpha^2\ne q$. On $V_j$, symmetry plus realness makes $B(v,\bar v)$ real, which gives one real parameter per mode.
- Computed on the genus-two $M$: the solution space of $M^TBM=5B$ has dimension 2.
- Part (a) holds even outside the standing hypotheses. For my $M_r$ of E-X3 the cone is non-empty. This matters below.

### E-P2: Proposition 2, the Weil form has weights $\varepsilon_j\,\mathrm{Im}\,\alpha_j$ on the vacuum

**Claim.** $J_{\Omega'}=\sum_j\varepsilon_j(M-V)\pi_j/\sqrt{4q-\lambda_j^2}$ and $W_{\Omega'}=\sum_j\varepsilon_j\tfrac12\sqrt{4q-\lambda_j^2}\,G_{\Omega'}|_{V_j}$.

**VERDICT E-P2: VALID**

- *The algebra.* $(2M-\lambda)^2=\lambda^2-4q$ on $V_j$. The commutant of an elliptic block is $\mathbb C$, so the vacuum is unique and the Krein sign fixes it.
- *Numerics.* For $\Omega_{\rm can}$ the Weil weights are $-1.18597$ and $+2.20079$, which are $(-\mathrm{Im}\,\alpha_1,+\mathrm{Im}\,\alpha_2)$ to 30 digits.
- *Krein-sign bookkeeping.* I computed the signs independently by diagonalising the restriction of $\Omega'(\cdot,(M-V)\cdot)$ to each mode. $\Omega_{\rm can}$ gives $(-,+)=-\mathrm{sgn}\,h'(\lambda_j)$. $\Omega_+$ gives $(+,+)$.
- *Precision, not counted.* The statement tacitly needs $\Omega'$ to be non-degenerate on every $V_j$. The space of compatible forms in Proposition 3 contains degenerate ones, which have no vacuum.

### E-P3: Proposition 3, $\Omega'\mapsto W_{\Omega'}$ is an isomorphism onto the similitude forms; in the cone iff $\Phi_{\Omega'}=\Phi_+$

**VERDICT E-P3: VALID**

- *Is the Weil form $M$-invariant?* Symmetry follows from $M^T\Omega'=\Omega'V$:
  $W(y,x)=-\tfrac12[\Omega'(x,Vy)-\Omega'(x,My)]=W(x,y)$.
- *Similitude:* $M^TWM=\tfrac12\Omega'V(M-V)M=qW$.
- *Injectivity* needs $M-V$ invertible, which holds iff no eigenvalue is real. The standing hypothesis guarantees this. Outside it, the map fails (E-X3).

### E-P4: Proposition 4, the Rosati transport sweeps the cone

**VERDICT E-P4: VALID**

- $\mathcal T=\sum 2|x_j|^2$ and $\Omega'(x,Jx)=\sum2|\varphi_j(\zeta)||x_j|^2$, with $\zeta_{ue}=u\bar u\zeta_e$.
- *Unit orbit.* $\varepsilon=(5+\sqrt{21})/2=1+y$ evaluated at $\lambda_{1,2}$ gives $4.7913$ and $0.2087$, a product of 1. The moved weights are $0.473489$ and $463.044$, matching the page's 0.4735 and 463.04.
- Generators differ by all units, so the orbit is $\{u\bar u\}$, which contains the $\eta^2$ of the page and may be larger when the Hasse unit index is 2. The sentence as written is still true.

### E-T5: Theorem 5, the genus-$g$ bridge

**Claim.** $\Omega_{\rm can}=\mathrm{Tr}(x\bar y/\mathfrak d)$ is unimodular with Krein signs $-\mathrm{sgn}\,h'(\lambda_j)$. $\Omega_+=\mathrm{Tr}(x\bar y/(V-F))$ has type $\Phi_+$, $\det=\mathrm{disc}(h)^2$, and Weil form exactly $\tfrac12\mathcal T_L$. Hence $\mathcal T_L=\sum\sqrt{4q-\lambda_j^2}\,G_{\Omega_+}|_j=\sum|h'(\lambda_j)|\sqrt{4q-\lambda_j^2}\,G_{\rm can}|_j$.

**VERDICT E-T5: VALID**

- *Exact integer Gram matrices.* I built $\mathbb Z[F,V]$ on the basis $(1,y,F,yF)$ from the four complex embeddings at 50 digits. The rounding error is below $10^{-30}$.
  - $\Omega_{\rm can}$ is integral, alternating and of determinant **1**.
  - $\Omega_+$ is integral, alternating and of determinant **441**.
  - The trace form has determinant **48069**, which equals PARI's `nfdisc`. So $\mathbb Z[F,V]=\mathcal O_K$.
  - `poldisc` gives $1201725=25\cdot48069$. So $[\mathcal O_K:\mathbb Z[F]]=5$, confirming K2.
- *The identities.*
  - $W_{\Omega_+}=\tfrac12\mathcal T_L$ holds exactly.
  - $G_{\Omega_+}=\sqrt{21}\,G_{\rm can}$.
  - $\mathcal T_L=\sum d_jG_{\Omega_+}|_j$, with weights $10.8696$ and $20.1706$ against $G_{\rm can}$ and ratio $1.85568$.
- *Euler's lemma applied twice (from memory).* I recall it the same way: the trace dual of a monogenic $R[\theta]$ is $f'(\theta)^{-1}R[\theta]$. With trace transitivity this gives the dual $\mathfrak d^{-1}$ for the tower, which the unimodularity confirms.
- *"For $g\ge3$ the two vacua are no longer proportional."* I attacked this as possibly over-general. It holds for every real-rooted $h$ with $g\ge3$. For $\lambda_1<\lambda_2$,
  $|h'(\lambda_1)|/|h'(\lambda_2)|=\prod_{k\ge3}(\lambda_k-\lambda_1)/(\lambda_k-\lambda_2)>1$,
  so $|h'|$ is never constant. A random test of 2000 cases found none.

### E-C: genus-two data and the small negative findings (C1–C5, K1–K5, R1–R9, U1–U2)

**VERDICT E-C: VALID**

- *Data.* PARI `hyperellcharpoly` gives $x^4-3x^3+7x^2-15x+25$, with $h_K=4$.
- *The 4×4 matrix of the page* satisfies $M^T\Omega M=5\Omega$ for $\Omega=\bigl(\begin{smallmatrix}0&I\\-I&0\end{smallmatrix}\bigr)$ and has characteristic polynomial $\chi$.
- *Graph convention.* $(a-c)^2+4b^2=21$ has no integer solution.
- *Not checked.* I did not check the identification with 04w's $E_0$ and $\xi_0$.

### E-H: 5-adic types and the principal forms on $\mathcal O_K$ (H1–H2)

**Claim (headline).** "Of the eight primes above 5 in the Galois closure, four give the archimedean CM type $\Phi_+$ and four give the mixed type of $\Omega_{\rm can}$." The principal forms on $\mathcal O_K$ are exactly $\pm\varepsilon^k\Omega_{\rm can}$.

**VERDICT E-H: MINOR** (wording of a checked count)

- *PARI.* `nfsplitting` has degree 8 and the group is $D_4$. There are 8 primes above 5. With the roots ordered $(\alpha_1,\alpha_2,\bar\alpha_2,\bar\alpha_1)$, the sets $S_{\mathfrak P}$ are $\Phi_+$ (2 primes), $\overline{\Phi_+}$ (2), $\{\bar\alpha_1,\alpha_2\}$, the type of $\Omega_{\rm can}$ (2), and its conjugate (2).
- *Why 2 each.* $D_4$ is transitive on the four CM types.
- *Principal forms.* The unit argument is right: $\bar\xi=-\xi$ forces $u=\bar u$. The fundamental unit of $\mathbb Q(\sqrt{21})$ is $(5+\sqrt{21})/2$ of norm $+1$; I recall it the same way. Both its conjugates are positive, so every principal form keeps the mixed type.

**Sentence at fault** (Findings, fourth bullet): "Of the eight primes above 5 in the Galois closure, four give the archimedean CM type $\Phi_+$ and four give the mixed type of $\Omega_{\rm can}$."

**Corrected statement.** "Of the eight primes above 5, two give $\Phi_+$ and two $\overline{\Phi_+}$ (so four give a principal polarisation with a definite Weil form, up to the sign of $\Omega$), two give the type of $\Omega_{\rm can}$ and two its conjugate." The body (§3) states it correctly. Only the headline drops the conjugates.

### E-G: $K_4$ with one negative edge (G1–G10)

**VERDICT E-G: VALID**, with one wording note.

- $A_s$ has its negative edge on $(1,2)$. This is the only edge for which the page's $P$ commutes with $A_s$. I checked the other five.
- *Spectrum and $P$.* The spectrum is $\{\pm1,\pm\sqrt5\}$. $P=\tfrac12(1+2A_s-A_s^2)$ with $p(\lambda)=(-\varphi^3,-1,1,\varphi^{-3})$ and $\det P=1$.
- *The Weil form of $\Omega_P$* has signature $(4,4)$, and $|p||h'|=(75.78,8,8,4.22)$.
- *Strengthening of the negative finding (G8).* It holds for *every* principal polarisation, not only for $P$. A unit $p'$ with $|p'||h'|$ constant would need $|p'(1)|=5^{1/4}$, but $p'(\pm1)$ is rational.
- *Wording note.* "There the Riemann form of Howe's principal polarisation is the vacuum with weights $(\varphi^3,1,1,\varphi^{-3})$" uses a definite article. It is one point of an infinite unit orbit, for one of the four primes.

### E-X3: the precision on `lattice-tower.md` §5

**Claim.** (i) does not imply (ii) in general, with the counterexample $M'=\bigl(\begin{smallmatrix}0&1\\-5&-2\end{smallmatrix}\bigr)$. "The general form is '(i) ⇔ (iii) ⇔ the Weil form of some compatible form is positive'."

**VERDICT E-X3: MINOR**

- *The counterexample is right.*
  - $M'^T\Omega M'=5\Omega$.
  - The eigenvalues are $-1\pm2i$, of modulus $\sqrt5$.
  - $\tfrac12\Omega(M'-V')=\bigl(\begin{smallmatrix}-5&-1\\-1&-1\end{smallmatrix}\bigr)$ is negative definite.
  - It is the improper conjugate of the Pauli-six step (A-D).
- *The proposed general form is false.* Take $B=\bigl(\begin{smallmatrix}0&2\\1&0\end{smallmatrix}\bigr)$ and $M_r=B\oplus2B^{-T}$ on $\mathbb Z^4$ with the standard $\Omega$.
  - $M_r$ is an integral step: $M_r^T\Omega M_r=2\Omega$.
  - It is semisimple with eigenvalues $\pm\sqrt2$, so (i) holds.
  - Its $\pm1$-eigenspaces of $M_r/\sqrt2$ are $\Omega$-orthogonal symplectic planes, so an invariant vacuum exists and (iii) holds.
  - But $M_r^2=2$, so $V=M_r$ and $M_r-V=0$. **Every** compatible form has Weil form identically zero, and none is positive.
  - The failure is exactly at a real eigenvalue $\pm\sqrt q$ ($\lambda=\pm2\sqrt q$). The page's standing hypothesis excludes this case, but the "general form" sentence corrects a page (`lattice-tower.md` §5) whose (i) includes it.
  - This is not an exotic case: $\pi=\pm\sqrt q$ is a real Weil number, the supersingular counterpart of lane B's quarter turn.

**Sentence at fault** (§5, item 3): "The general form is "(i) $\Leftrightarrow$ (iii) $\Leftrightarrow$ the Weil form of some compatible form is positive"."

**Corrected statement.** "The general form is (i) ⇔ (iii). If moreover no eigenvalue of $M$ is real (no $\lambda_j=\pm2\sqrt q$), these are equivalent to: the Weil form of some compatible form is positive. At a real eigenvalue $\pm\sqrt q$, $M=V$ on that block and every Weil form is degenerate there, although (i) and (iii) hold."

For non-real but repeated $\lambda$, the existence of such a form follows from the vacuum: take $\Omega'=\Omega(\cdot,\mathrm{sgn}(\sin\Theta)\cdot)$ in the unitary frame of $J$. That proof is mine, and I did not run a check of it.

---

## Lane F: `overlap-data.md`

### F-C1: Criterion 1, the degree-2 and degree-3 isogenies swap the classes (C3–C5, C9)

**VERDICT F-C1: VALID**

- *PARI.* $E_4: y^2=x^3+3x+3$ has $j=4$ and $E_5: y^2=x^3+x+3$ has $j=5$. Both have $a=2$ and $E(\mathbb F_7)\cong\mathbb Z_6$, with one rational point of order 2 and one rational subgroup of order 3. The Vélu quotients send $E_4\mapsto j=5$ and $E_5\mapsto j=4$ in both degrees.
- $\mathfrak p_2=(2,\pi-1)$ with $\pi-1=\sqrt{-6}$.
- *Kernel ideals (Waterhouse 1969, from memory).* I recall it the same way, with the class moved by $[\mathfrak a]^{\pm1}$. The sign is irrelevant here because the class has order 2.

### F-C2: Criterion 2, which curve is principal depends on ε

**Claim.** $j(\sqrt{-6})=2417472+1707264\sqrt2$, the roots of $H_{-24}$ are $4,5\bmod7$, $j(\mathcal O_K)\equiv1-\sqrt2$, and $\varepsilon(s)=+\sqrt2$ with $s\equiv3$ makes $j=5$ principal.

**VERDICT F-C2: VALID**

- *PARI.* `polclass(-24)` is $x^2-4834944x+14670139392$, with roots $\{4,5\}$ mod 7 and $h(-24)=2$. `ellj(sqrt(-6))` is $4831907.90335$ and `ellj(sqrt(-6)/2)` is $3036.09665$. `algdep` returns $H_{-24}$.
- *Mod 7.* $2417472\equiv1$ and $1707264\equiv-1\pmod 7$. With $s\equiv3$, $j\equiv5$; with $s\equiv4$, $j\equiv4$.
- *Logic.* $T_\varepsilon(E)\cong\Lambda$ as $\mathcal O_K$-modules through the embedding in $\Phi_\varepsilon$. Conjugation does not matter, because $\mathrm{Cl}$ is 2-torsion.
- *From memory.* Deligne's $T=H_1$ of the canonical lift, Serre–Tate $\mathrm{End}(E^{\rm can})=\mathrm{End}(E)$, and Deuring/Waterhouse torsors: I recall all three the same way.

### F-L1: Lemma 1, the overlap function is the $\mathbb Z[\pi]$-module $E(\overline{\mathbb F}_q)$

**Claim.** The overlaps are $q^{kh^0(D)}$. "A relabelling of places that is compatible with base change is a $\pi$-equivariant bijection $\psi$ of $E(\overline{\mathbb F}_q)$." $\psi$ preserves $h^0$ at every level iff $\psi=\tau\circ\Psi$.

**VERDICT F-L1: MINOR**

- *The third bullet is right.* Taking $R=P+Q$ and $S=O$ gives $\psi(P)+\psi(Q)=\psi(P+Q)+\psi(O)$, so $\psi-\psi(O)$ is additive. The converse holds because a divisor of degree 0 kills the translation. $\psi(O)$ is $\pi$-fixed by equivariance.
- *The second bullet is false as written.* Compatibility with base change constrains only *sets*: the places above $v$ go to the places above $\psi(v)$. Over a place of prime degree $d$ it allows any permutation of the $d$ geometric points. Swapping $\pi P$ and $\pi^2P$ in an orbit of size 3 is base-change compatible and not $\pi$-equivariant. What is needed is compatibility with the Frobenius (Galois) action on the places of $E_{\mathbb F_{q^k}}$. That is what the page's own headline ("compatible with Frobenius") and the synthesis ("Frobenius-compatible relabelling") say.
- *Open.* Whether $h^0$-preservation together with base change alone forces equivariance is not shown on the page, and I did not settle it. An additive $\psi$ that maps orbits to orbits conjugates $\pi$ to an orbit-preserving automorphism, and I did not prove that this must be $\pi$ itself. With the Frobenius hypothesis the conclusion stands. The $h^0$ brute force (R1–R2) is the same method as A-3, which I reproduced on E1.

**Sentence at fault** (Lemma 1, second bullet): "A relabelling of places that is compatible with base change is a $\pi$-equivariant bijection $\psi$ of $E(\overline{\mathbb F}_q)$."

**Corrected statement.** "A relabelling of places at all levels that is compatible with base change *and with the Frobenius action on the places of each $E_{\mathbb F_{q^k}}$* is the same as a $\pi$-equivariant bijection $\psi$ of $E(\overline{\mathbb F}_q)$. Base change alone allows permutations inside each Frobenius orbit."

### F-T2: Theorem 2, the modules are isomorphic iff $\mathrm{End}(E)=\mathrm{End}(E')$; the overlaps see the order and not the class

**VERDICT F-T2: VALID**

- *Tate's-theorem step.* $\mathrm{End}(E)\otimes\mathbb Z_\ell=\mathrm{End}_{\mathbb Z_\ell[\pi]}(T_\ell E)$. Because $\pi$ is regular this commutant is the multiplier ring of $T_\ell$ in $K_\ell$, so $T_\ell E$ is proper.
- *Local-freeness step.* For a quadratic order, proper is the same as invertible (Gorenstein). An invertible ideal over the semilocal $\mathcal O_\ell$ is principal. I recall both facts the same way.
- *At $p$.* $p\nmid a^2-4q$ because $p\nmid a$, so every order is maximal at $p$, and the étale part $\mathbb Q_p/\mathbb Z_p$ with the unit root depends only on $(a,q)$.
- *The ⇒ direction* recovers $T_\ell$ as $\mathrm{Hom}(\mathbb Q_\ell/\mathbb Z_\ell,\cdot)$, and an order is the intersection of its completions.
- *Implicit hypothesis.* The theorem needs $E,E'$ isogenous, so that $\pi$ is the same. Its statement says so; the synthesis's paraphrase omits it.
- *Independent evidence.* On $E[n]$ the number of $\pi$-equivariant isomorphisms $E_4[n]\to E_5[n]$ is $6,8,16,32,54,128$ for $n=3,4,5,8,9,16$. These are exactly $|(\mathcal O_K/n)^\times|$, so the set of equivariant isomorphisms is an $(\mathcal O_K/n)^\times$-torsor, as Theorem 2 predicts. $\mathbb Z^2/N$ for $(1,0,6)$ and $(2,0,3)$ are isomorphic $\mathbb Z[M]$-modules for all $N\le20$.

### F-O: the explicit pair, the gluing map and the overlap statistics (O1–O3, T1)

**VERDICT F-O: VALID**

- *The equivariant isomorphism $E_4(\overline{\mathbb F}_7)\to E_5(\overline{\mathbb F}_7)$ (attacked).*
  - $\varphi_2$ is an isomorphism on odd torsion and $\varphi_3$ on the 2-part. Both are $\mathbb F_7$-rational.
  - $u:(x,y)\mapsto(4x,y)$ is the twist-free isomorphism with $u=2$, since $2^2=4$ and $2^3=8\equiv1$. It sends $(A,B)\mapsto(2A,B)$, e.g. $x^3+4x+3\mapsto x^3+x+3$.
  - The torsor counts above confirm independently that equivariant isomorphisms exist at every level tested.
  - $\#E(\mathbb F_{7^4})=2400$.
- *O1 by my own enumeration of $E(\mathbb F_{7^4})$.* Both curves have 1170 degree-2 places over $\mathbb F_{49}$, with identical fibre multisets.
  - $\sum_cn_c^2=22860$ for both, which is the page's number.
  - That number counts *ordered pairs including $P=Q$*. The off-diagonal count is 21690. The page should say so; this is a wording note.

### F-P3: Proposition 3, the polarised refinement (W1–W3, T2–T3)

**Claim.** The scale sets are $\{2\}$ ($n=3$), $\{3,5\}$ ($n=8$), $\{2,5,8\}$ ($n=9$), $\{3,5,11,13\}$ ($n=16$), and all units for $n=2,4,5$. No equivariant isomorphism $E_4[8]\to E_5[8]$ respects $e_8^{\pm1}$. Every equivariant isomorphism $E_4[3]\to E_5[3]$ inverts $e_3$.

**VERDICT F-P3: VALID**

- *Method.* I chose my own Weil-normalised bases by random sampling and independence through $e_n$. I avoided PARI's `ellgroup` generators, which are not of the stated orders: over $\mathbb F_{343}$, PARI's second generator has order 21 for cyclic structure $[126,3]$. I wrote Frobenius as a matrix and enumerated all $g\in\mathrm{GL}_2(\mathbb Z/n)$ with $gF_4=F_5g$.
- *Result.* Scale $=c\cdot\det g$, with $e_5$-normalisation $c$. The sets are exactly $\{2\}$, $\{1,3\}$, $\{1,2,3,4\}$, $\{3,5\}$, $\{2,5,8\}$ and $\{3,5,11,13\}$. They equal the lattice-side sets $\{\det g: gM_{(1,0,6)}=M_{(2,0,3)}g\bmod n\}$.
- *Arithmetic.* $N((\mathcal O_K/8)^\times)=\{1,7\}$ and $N((\mathcal O_K/3)^\times)=\{1\}$, as used in the proof.
- *Wording note.* The headline's "The polarised local data see the *genus* of the form" is the sketched item 4 of §3 (Gauss genus theory). I recall genus theory the same way: the principal genus is $\mathrm{Cl}^2$, and $D=-24$ has 2 genera. The headline should carry the label *sketched*.

### F-P: the Pauli-six pair (P1–P5)

**VERDICT F-P: VALID.**
- *PARI.* $b=0$ has $j=3$ and $\mathbb Z_2\times\mathbb Z_4$, with 2 pairs $\{P,-P\}$ of distinct affine points. $b=1$ has $j=1$ and $\mathbb Z_8$, with 3 pairs.
- $(M-1)/2$ is integral on $(2,0,2)$ and not on $(1,0,4)$.

---

## The synthesis (`data-ladder.md`): the three claims it took, and §0

### S1: claim (1), the one-mode bridge carries the Riemann–Roch cokernel to the Deligne module, and the Howe sign cancels in the metric

**VERDICT S1: MINOR.** The identity, the scalar, the maps and the sign cancellation are all VALID (A-5a, A-5b, A-5d). §1 item 5 inherits the overreach of A-5b.

**Sentence at fault:** "the unimodular map $S$ … carries the Riemann–Roch cokernel state $(Y_j,Y_{j-1})$ of `analytic.md` §13 to the Deligne module".

**Corrected statement.** "… to the companion lattice $\mathbb Z[F]$, which is the Deligne module of the curve exactly when $T\cong\mathbb Z[F]$; otherwise only rationally, with index $[\mathbb Z[F]:T]$ entering the scalar."

The table entry "Rosati form $=$ vacuum form $\times\sqrt{4q-a^2}$" needs the same qualifier.

### S2: claim (2), the cone, the Weil weights $\varepsilon_j\tfrac12\sqrt{4q-\lambda_j^2}$, and RH ⇔ a non-empty cone, with the Weil form positive iff additionally Φ = Φ+

**VERDICT S2: VALID** under lane E's standing hypotheses (squarefree $\chi$, $|\lambda_j|<2\sqrt q$). For curves, semisimplicity is a theorem, so "RH ⇔ the cone is non-empty" holds as stated. The $M'$ counterexample to `lattice-tower.md` §5 (i)⇒(ii) is correct (E-X3).

### S0: `data-ladder.md` §0 still asserts the equivalence that lane E refuted

**VERDICT S0: MINOR.**

**Sentence at fault** (§0): "RH is one further datum, an invariant Gaussian vacuum $J$ … equivalently the positivity of the Weil form $\tfrac12\Omega(M-V)$ (`lattice-tower.md` §5)."

The synthesis's own §1 item 5 says the Weil form is positive only if additionally $\Phi_\Omega=\Phi_+$. $M'$ is a counterexample, and $M_r$ of E-X3 is a second one.

**Corrected statement.** "… an invariant Gaussian vacuum $J$. When $\Omega$ has CM type $\Phi_+$ (as for the graph steps) and no eigenvalue is real, this is equivalent to the positivity of the Weil form $\tfrac12\Omega(M-V)$."

### S3: claim (3), the overlaps are the $\mathbb Z[\pi]$-module $E(\overline{\mathbb F}_q)$, they see the order and never the class, and the Weil pairing separates the classes at $q=7$, $a=2$

**VERDICT S3: VALID.**
- The synthesis's wording "up to Frobenius-compatible relabelling" is the correct hypothesis (compare F-L1).
- "iff $\mathrm{End}(E)=\mathrm{End}(E')$" is meant within an isogeny class, where $\pi$ is the same.
- Separation by the Weil pairing is confirmed at $n=8$ and $n=16$, and at $n=3$ up to inversion. The pairing does *not* separate at $n=4$, where the scale set is $\{1,3\}$ and contains 1. The detecting 2-adic level is 8.

---

## From-memory theorems: my recollection

| theorem as quoted | where | my recollection |
|---|---|---|
| Latimer–MacDuffee | A §1 | same |
| Lenstra 1996 (JNT 56): $E(\mathbb F_q)\cong\mathcal O/(\pi-1)$ | A §2 | same; hypothesis rank-2 $\mathrm{End}_{\mathbb F_q}$ |
| Deligne 1969: $T=H_1$ of the canonical lift; unit-root splitting at $p$ | A §2, F §1 | same |
| Honda–Tate; Tate's isogeny theorem | A §6, F Thm 2 | same |
| Howe 1995, Φ_ε-positivity | A §5 (via `howe-positivity.md`) | same |
| Euler's lemma; the different of a tower | E Thm 5 | same; confirmed by unimodularity |
| fundamental unit of $\mathbb Q(\sqrt{21})$ is $(5+\sqrt{21})/2$ | E §3 | same |
| Deuring/Waterhouse torsor; kernel ideals | F §1 | same |
| proper = invertible for quadratic orders (Gorenstein) | F Thm 2 | same |
| Serre–Tate $\mathrm{End}(E^{\rm can})=\mathrm{End}(E)$; Katz 1981 | F §§1, 3 | same |
| Mumford 1966: $e_n$ is the commutator form of the theta group of $\mathcal O(nO)$ | F §3.6 | same, up to the sign convention of $e_n$ |
| Gauss genus theory: genera $=\mathrm{Cl}/\mathrm{Cl}^2$ | F §3.4 | same |

## Files

- `notes/reviews/scratch_gkp_lattice_curve.py`: the bridge (symbolic), Latimer–MacDuffee, $M'$, B10 determinants, groups for $k\le6$ on six equations, and the Theorem 12 cokernel. 38/38.
- `notes/reviews/scratch_gkp_lattice_e1h0.py`: brute-force $h^0$ on E1, 144 divisors, 0 mismatches.
- `notes/reviews/scratch_gkp_lattice_cone.py`: $\mathbb Z[F,V]$ for the genus-two curve, Krein signs, weights, 5-adic types, $K_4$, and the $M_r$ counterexample. 28/28.
- `notes/reviews/scratch_gkp_lattice_overlap.py`: $j$-invariants, $H_{-24}$, ε-assignment, isogenies, Weil scale sets for $n=3,4,5,8,9,16$, lattice det-sets, degree-2 place statistics, the Pauli-six pair, and groups to $k=24$. 19/19.
