# The two lattice states of one curve

Author: `claude:opus-5.5`, 2026-10-06, lane A of an orchestrated session.

Status: **a record, not a round; nothing registered in db/claims.tsv; no REFUTE review; no shard.** Each statement is labelled *standard*,
*proved here*, *checked*, *sketched*, *heuristic*, *open* or *negative finding*. Theorems quoted without a line reference are from memory;
`refs/src/` was not on disk in this session. Checks: `checks/check_curve_bridge.py`, output `checks/output_curve_bridge.txt` (82 of 82 pass;
PARI/GP 2.15.4 through the `gp` binary, sympy, numpy; about 3 s).

The notebook has two lattice pictures of a curve over $\mathbb F_q$. (i) The adelic qunaught $\Theta_K$ (`adelic-gkp.md` §11): its overlaps with
product stabiliser states are $q^{h^0(D)}$, and its Riemann–Roch cokernel (analytic §13) is a $2g$-dimensional space on which the degree shift acts
as the Frobenius companion matrix, with the Rosati form (analytic §14) as metric. (ii) The GKP lattice state of a one-mode integer step $M$ on
$\mathbb Z^2$ with $M^T\Omega M=q\Omega$ (`lattice-tower.md`): in the ordinary case a Deligne module, with RH equivalent to an invariant vacuum $J$.
This page connects the two on three elliptic curves.

**Findings.**

- **The bridge holds exactly in genus one** (proved here, checked). The cokernel phase space $(Y_j,Y_{j-1})$ of analytic §13 maps to the Deligne
  module by the unimodular matrix $S=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$. $S$ carries the window shift to $M$, the discrete
  Wronskian to $\Omega$, and the Casoratian to the Weil form. So $\Omega(Sy,JSy)=\tfrac{2}{\sqrt{4q-a^2}}\,\mathcal Q(y)=\tfrac1{\sqrt{4q-a^2}}\,\mathcal T(Cy,Cy)$:
  **the vacuum form of the GKP lattice is the Rosati form of the adelic qunaught, scaled by $1/\sqrt{4q-a^2}$.** For one mode this is close to forced,
  because the symmetric $q$-similitude forms of an elliptic $M$ form a line. The content is in the explicit integral map and in the exact scalar.
- **The Howe sign does not reach the metric** (proved here, checked). Changing the prime above $p$ replaces $\Omega$ by $-\Omega$ and $J$ by $-J$. The
  Riemann form $\Omega_\varepsilon(\cdot,J_\varepsilon\cdot)$ is then the same for both choices, and equals the vacuum form.
- **"$E(\mathbb F_{q^k})\cong\mathbb Z^2/(1-M^k)\mathbb Z^2$ with $M$ the companion matrix" is false in general** (negative finding, checked). What holds is
  $E(\mathbb F_{q^k})\cong T/(1-F^k)T$, with $T$ the Deligne module of *that* curve (sketched below; for elliptic curves it is Lenstra's theorem, from memory).
  The companion lattice is the right $T$ only when $T\cong\mathbb Z[F]$. For E1 it is, at every $k=1..8$. In the Pauli-six isogeny class the curve
  $y^2=x^3+4x$ ($j=1728$, $\mathrm{End}=\mathbb Z[i]$) has $E(\mathbb F_5)=\mathbb Z_2\times\mathbb Z_4$, whereas the companion lattice gives $\mathbb Z_8$. The two
  disagree at every $k=1..8$. Shard 03c's equations $y^2=x^3+4x+b$, $b\in\{0,1,4\}$, cover both lattices.
- **The counts do not determine the lattice** (checked). The adelic trivial-character sector sees only $P(T)$. Its cokernel carries the companion
  lattice $\mathbb Z[F]$ (the principal binary form). The curve chooses a class of positive binary forms of discriminant $a^2-4q$. For E3 ($q=7$, $a=2$, class
  number 2) the two classes give isomorphic groups at every level tested, so even the group structures cannot tell them apart.

---------------------------------------------------------------------------------------------------------------------

## 1. Conventions and the three examples

Conventions follow `lattice-tower.md`. $L=\mathbb Z^2$, $\Omega=\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$, $\Omega(x,y)=x^T\Omega y$. The companion step is $M=\bigl(\begin{smallmatrix}0&-1\\q&a\end{smallmatrix}\bigr)$ with
$\lambda=a$, where $a=q+1-\#E(\mathbb F_q)$ is the trace of Frobenius, so that $\det(x-M)=x^2-ax+q$. Further, $V=qM^{-1}=a-M$. The Weil form is
$G=\tfrac12\Omega(M-V)=\bigl(\begin{smallmatrix}q&a/2\\a/2&1\end{smallmatrix}\bigr)$, the form $qx^2+axy+y^2$.

| | curve | $q$ | $a$ | $x^2-ax+q$ | disc | $\mathbb Z[F]$ | lattice classes (reduced forms) |
|---|---|---|---|---|---|---|---|
| E1, the E mode | $y^2+xy=x^3+1$ | 2 | $-1$ | $x^2+x+2$ | $-7$ | maximal, $h=1$ | $(1,1,2)$ |
| E2, the Pauli six | $y^2=x^3+4x+b$ | 5 | $-2$ | $x^2+2x+5$ | $-16$ | $\mathbb Z[2i]$, conductor 2 | $(1,0,4)$, $(2,0,2)$ |
| E3, class number two | $y^2=x^3+Ax+B$, $j\in\{4,5\}$ | 7 | $2$ | $x^2-2x+7$ | $-24$ | $\mathbb Z[\sqrt{-6}]$, maximal, $h=2$ | $(1,0,6)$, $(2,0,3)$ |

All three are ordinary ($a\not\equiv0\bmod q$) and satisfy $a^2<4q$ (D1).

**Lattice classes** (standard, Latimer–MacDuffee; the form dictionary is proved here and checked, D2–D3). A positive binary form $(A,B,C)$ of
discriminant $a^2-4q$ gives the integer step
$$
M_{(A,B,C)}=\begin{pmatrix}(a-B)/2&-C\\A&(a+B)/2\end{pmatrix},\qquad \tfrac12\Omega\bigl(M_{(A,B,C)}-V\bigr)=\begin{pmatrix}A&B/2\\B/2&C\end{pmatrix}.
$$
So **the Weil form of a step is its Latimer–MacDuffee form.** $\mathrm{GL}_2(\mathbb Z)$-conjugacy classes of steps correspond to proper classes of
positive forms, primitive or not. These are the $F$-stable lattices in $\mathbb Q(F)$ up to scaling, that is, the ideal classes of all orders
containing $\mathbb Z[F]$. The companion step is the principal form $(q,a,1)\sim(1,\cdot,\cdot)$.

## 2. The group of points (task item 2)

PARI computed, for every Weierstrass equation in each isogeny class, `ellgroup` over $\mathbb F_{q^k}$ for $k=1..8$. Separately, the Smith normal form of
$1-M^k$ was computed for every lattice class (G1–G8).

| | curve(s) | $E(\mathbb F_{q^k})$, $k=1..8$ | lattice class that matches |
|---|---|---|---|
| E1 | all 4 equations, $j=1$ | $\mathbb Z_4,\mathbb Z_8,\mathbb Z_4,\mathbb Z_{16},\mathbb Z_{44},\mathbb Z_{56},\mathbb Z_{116},\mathbb Z_3{\times}\mathbb Z_{96}$ | companion $(1,1,2)$, all $k$ |
| E2 | $b=1,4$, $j=1$ ($=287496$ mod 5, $\mathrm{End}=\mathbb Z[2i]$) | $\mathbb Z_8,\ \mathbb Z_2{\times}\mathbb Z_{16},\ \mathbb Z_{104},\ \mathbb Z_4{\times}\mathbb Z_{160},\dots,\ \mathbb Z_{24}{\times}\mathbb Z_{16320}$ | companion $(1,0,4)$ only |
| E2 | $b=0$, $j=1728\equiv3$ ($\mathrm{End}=\mathbb Z[i]$) | $\mathbb Z_2{\times}\mathbb Z_4,\ \mathbb Z_4{\times}\mathbb Z_8,\ \mathbb Z_2{\times}\mathbb Z_{52},\ \mathbb Z_8{\times}\mathbb Z_{80},\dots,\ \mathbb Z_{48}{\times}\mathbb Z_{8160}$ | $(2,0,2)$ only; the companion fails at every $k=1..8$ |
| E3 | $j=4$ and $j=5$ | $\mathbb Z_6,\ \mathbb Z_2{\times}\mathbb Z_{30},\ \mathbb Z_3{\times}\mathbb Z_{126},\ \mathbb Z_{20}{\times}\mathbb Z_{120},\dots$ | both classes, all $k$ (they agree to $k=24$) |

- *Checked.* The E1 row reproduces the table of `lattice-tower.md` §2 (G5). That table is right.
- *Negative finding.* The sentence of `lattice-tower.md` §6, "the group of points is $L/(1-M^k)L$ as a group", is correct only when $L$ is the Deligne
  module of the curve in question. With $L$ the companion lattice it fails for $y^2=x^3+4x$ over $\mathbb F_5$, already at $k=1$. The Pauli-six step of
  `graph-super.md` / `lattice-tower.md` is the Deligne module of $y^2=x^3+4x\pm1$ ($j=1$), not of $y^2=x^3+4x$. The two curves are isogenous, so their zeta
  functions agree, which is all that shard 03c asserts.
- *Checked (E3).* The two lattice classes of discriminant $-24$ are not $\mathrm{GL}_2(\mathbb Z)$-conjugate: $(2,0,3)$ has no cyclic vector (G8). Yet their quotients
  $L/(1-M^k)L$ agree for every $k$ tested. The reason (standard) is that for an invertible ideal $\mathfrak a$ of $\mathcal O$, $\mathfrak a/x\mathfrak a\cong\mathcal O/x\mathcal O$. The two
  curves $j=4$, $j=5$ have non-isomorphic Deligne modules, and their groups of points cannot show which is which. Which curve goes with which class
  depends on Deligne's embedding $\varepsilon$; *open*, not needed here.

**Theorem (sketched; inputs from memory).** Let $A/\mathbb F_q$ be ordinary with Deligne module $(T,F)$. Then $A(\mathbb F_{q^k})\cong T/(1-F^k)T$ as groups, for all $k\ge1$.

*Sketch.* $A(\mathbb F_{q^k})=\ker(1-\pi^k)$ on $A(\overline{\mathbb F}_q)=\bigoplus_\ell A[\ell^\infty]$. For an endomorphism $\varphi$ that is injective on $T\otimes\mathbb Q$, the
snake lemma on $0\to T\to T\otimes\mathbb Q\to T\otimes\mathbb Q/\mathbb Z\to0$ gives $\ker(\varphi\,|\,T\otimes\mathbb Q/\mathbb Z)\cong T/\varphi T$, one prime at a time. For $\ell\ne p$, Deligne's
construction gives $T\otimes\mathbb Z_\ell\cong T_\ell A$ compatibly with Frobenius (from memory: $T=H_1$ of the canonical lift, plus the comparison of Betti and
étale homology, plus injectivity of reduction on prime-to-$p$ torsion). For $\ell=p$, $T\otimes\mathbb Z_p=T'\oplus T''$, with $F$ a unit on $T'\cong T_p^{\text{ét}}A$ and
$F\in q\,\mathrm{End}(T'')$. On $T''$ the operator $1-F^k$ is invertible, and $A[p^\infty](\overline{\mathbb F}_q)$ is the étale part, so the $p$-part of both sides is
$T'/(1-F^k)T'$. ∎

This is not a one-paragraph consequence of the bare equivalence of categories: it uses how the equivalence is built (the comparison isomorphisms
and the unit-root splitting at $p$). For elliptic curves the same statement, $E(\mathbb F_{q^k})\cong\mathrm{End}(E)/(1-\pi^k)$ as $\mathrm{End}(E)$-modules for $E$ ordinary, is
Lenstra's theorem (H. W. Lenstra, *Complex multiplication structure of elliptic curves*, J. Number Theory 1996; from memory). It agrees with the
Deligne form because $T$ is an invertible $\mathrm{End}(E)$-ideal. The E2 data are what Lenstra predicts: $\mathbb Z[2i]/(1-\pi)\cong\mathbb Z_8$ and $\mathbb Z[i]/(2-2i)\cong\mathbb Z_2\times\mathbb Z_4$.

## 3. The adelic side on E1: overlaps are counts

$K=\mathbb F_2(E1)$ and $\Theta_K=\sum_{x\in K}\delta_x$. For $D=\sum d_vv$, $\langle\Theta_K,1_D\rangle=\#\{x\in K:v(x)\ge-d_v\ \forall v\}=\#L(D)$. This is the
definition, as in `adelic-gkp.md` §11.

*Checked by brute force* (A1–A5). The divisors are $D=nO-E$ with $n=-1..6$ and $E$ any reduced effective divisor of affine places of degree $\le2$, with
$\deg E\le n+1$: 144 divisors in all. The places used are the three rational affine points $P_0=(0,1)$, $P_1=(1,0)$, $P_2=(1,1)$ and the two places
$Q_0,Q_1$ of degree 2. $L(nO)$ has basis $x^i$ ($2i\le n$) and $x^iy$ ($2i+3\le n$); this uses the pole orders 2 and 3 of $x$ and $y$ at $O$, which is
*standard*. The vanishing at each place of $E$ was tested by evaluating over $\mathbb F_4$. The results:

- Every overlap is a power of $q$.
- $h^0(nO)=0,1,1,2,3,4,5,6$ for $n=-1..6$.
- On all 144 divisors, $h^0$ agrees with Riemann–Roch ($h^0=\deg D$ for $\deg D>0$, and $0$ for $\deg D<0$) combined with Abel–Jacobi in degree 0, where
  $nO-E\sim0$ iff the points of $E$ sum to $O$ in the group law. Examples: $h^0(2O-P_1-P_2)=1$, since $P_2=-P_1$ and the divisor is that of $x-1$.
  $h^0(3O-P_1-Q_0)=1$. $h^0(2O-Q_0)=0$. $h^0(4O-Q_0-Q_1)=1$.
- $h^0$ is a function of the class in $\mathrm{Pic}$. In degree 0 it is 1 on the trivial class and 0 on the other three classes of
  $\mathrm{Pic}^0=E(\mathbb F_2)\cong\mathbb Z_4$.

**In the sense of analytic §13** (A6–A8, checked). $A(n)=\frac1h\sum_{c\in\mathrm{Pic}^n}(q^{h^0(c)}-1)$, read off the overlap table, is $A(-1)=0$,
$A(0)=\tfrac14=(q-1)/h$, and $A(n)=2^n-1$ for $n=1..5$. Then $a_n=\tfrac h{q-1}A(n)=1,4,12,28,60,124$. These are the numbers of effective divisors,
counted independently from the places ($4,2,0,2,8$ places of degree $1..5$). And $Z(T)(1-T)(1-2T)=1+T+2T^2=P(T)$ to order $T^5$.

## 4. The Riemann–Roch cokernel as a 2×2 matrix (analytic §13, Theorem 12)

*Checked exactly* (R1–R5, cutoff $N=5$, rational arithmetic). For E2, $A(n)$ is taken from Riemann–Roch rather than from a brute-force table. For
admissible $c$ ($\sum c_j=0$, $\sum c_jq^j=0$), the vectors $Ef(m)=q^{m/2}\sum_jc_jA(j-m)$ vanish outside $[-N,N]$. The orthogonal complement of their
span in $\ell^2([-N,N])$ is 2-dimensional. In $Y(m)=y(m)q^{m/2}$ every element satisfies $Y_j-aY_{j-1}+qY_{j-2}=0$ on the whole window. In the basis of
analytic §13, the state $s_j=(Y_j,Y_{j-1})$, the window shift is
$$
W=\begin{pmatrix}a&-q\\1&0\end{pmatrix}:\qquad W_{E1}=\begin{pmatrix}-1&-2\\1&0\end{pmatrix},\qquad W_{E2}=\begin{pmatrix}-2&-5\\1&0\end{pmatrix}.
$$
Two forms on the state space are $q$-similitudes of $W$ along the computed solutions:

- the Casoratian $\mathcal Q(s_j)=Y_j^2-aY_jY_{j-1}+qY_{j-1}^2$ (Corollary 13), with matrix $\bigl(\begin{smallmatrix}1&-a/2\\-a/2&q\end{smallmatrix}\bigr)$;
- the antisymmetric Casoratian (discrete Wronskian) $\omega_C(s_j,s'_j)=Y_jY'_{j-1}-Y_{j-1}Y'_j$, whose multiplier is $\det W=q$.

## 5. The bridge (task item 3)

There are three real 2-dimensional spaces, each with a $q$-similitude:

| space | operator | symmetric form | antisymmetric form |
|---|---|---|---|
| (A) cokernel phase space, $s=(Y_j,Y_{j-1})$ | $W$ | Casoratian $\mathcal Q$ | discrete Wronskian $\omega_C$ |
| (B) $\mathbb R[F]$, basis $(1,F)$ | multiplication by $F$ | Rosati $\mathcal T$, Gram $\bigl(\begin{smallmatrix}2&a\\a&2q\end{smallmatrix}\bigr)$ | (none needed) |
| (C) Deligne module $\mathbb Z^2\otimes\mathbb R$ | $M$ | vacuum form $\Omega(\cdot,J\cdot)$, $J=\dfrac{2M-a}{\sqrt{4q-a^2}}$ | $\Omega$ |

**Maps** (proved here, checked B1–B5):

- $C:(A)\to(B)$, $s\mapsto Y_j-Y_{j-1}F$. This is the identification of Corollary 13.3. It carries $\mathcal Q$ to $\tfrac12\mathcal T$, and $W$ to multiplication by
  $V$, not $F$. This matches Proposition 14: the cokernel is the dual of $\mathbb R[F]$ and the shift is a transpose.
- $\psi:(B)\to(C)$, $\varphi\mapsto\varphi(M)e_2$. The vector $e_2$ is cyclic for $M$. The map carries $F$ to $M$ and $\tfrac12\mathcal T$ to the Weil form $G$.
- The composite $S=\psi\circ(\text{Rosati involution})\circ C$ is $s\mapsto(-Y_{j-1},Y_j)$, that is, $S=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)\in\mathrm{SL}_2(\mathbb Z)$. It
  satisfies $SWS^{-1}=M$, $S^T\Omega S=\Omega$ (so $\omega_C$ goes to $\Omega$), and $S^TGS=\mathcal Q$.

**The bridge identity** (proved here; checked exactly and against a numerically computed vacuum, B6–B8). For $s$ in the cokernel phase space,
$$
\Omega(Ss,\,J\,Ss)\;=\;\frac{2}{\sqrt{4q-a^2}}\;\mathcal Q(s)\;=\;\frac{1}{\sqrt{4q-a^2}}\;\mathcal T(Cs,Cs).
$$
The scalar is $\sqrt7$ for E1, $4$ for E2 and $\sqrt{24}$ for E3. It is positive exactly when $a^2<4q$, and that is the only case in which $J$ exists.
The proof is the identity $\Omega(M-V)=2G$ together with $J=(M-V)/\sqrt{4q-a^2}$.

- **Why it had to hold, and what it does not say** (proved here, B9). For one elliptic mode the symmetric forms $B$ with $M^TBM=qB$ form a line. Any two
  positive similitude forms are therefore proportional. The genus-one bridge has no freedom except the scalar. In genus $g\ge2$ (not done here) the
  similitude forms form a cone: a Rosati form and a vacuum form agree up to a positive weight on each mode, and need not be proportional. *Sketched.*
- **Other lattices in the class** (checked, B10). For the non-principal classes $(2,0,2)$ of E2 and $(2,0,3)$ of E3, the vacuum form, pulled back to the
  companion lattice by the rational intertwiner, is the companion vacuum form times 2. Over $\mathbb Q$ the bridge is the same for every curve in the isogeny
  class. Only the integral structure differs.
- **The Howe sign** (checked with PARI, H1–H2; proved here). In each example $p$ splits in $\mathbb Q(F)$. At one prime $F$ is the non-unit, at the other $V$
  is. So $\Phi_\varepsilon=\Phi_+$ for one choice of $\varepsilon$ and $\Phi_\varepsilon=\overline{\Phi_+}$ for the other. The polarisation is $\Omega_\varepsilon=\pm\Omega$ and the arithmetic
  complex structure is $J_\varepsilon=\pm J$, with the same sign (`howe-positivity.md` §§1–2, §5). Then
  $$
  \Omega_\varepsilon(x,J_\varepsilon y)=\Omega(x,Jy)\qquad\text{for both choices of }\varepsilon .
  $$
  The sign lives on the symplectic form and on the complex structure, and cancels in the Riemann form. **The positive form that Howe's theorem
  produces is the vacuum form, which is the Rosati form transported, independently of $\varepsilon$.** This is the one-mode case of the remark in
  `howe-positivity.md` §5 that "positivity is unaffected".

So the bridge statement holds as stated, with two precisions. (a) The scalar is $1/\sqrt{4q-a^2}$, relative to $\mathcal T$. (b) The Howe sign cancels in
the metric rather than having to be inserted.

## 6. The data ladder for the curve case (task item 4)

Ordered by what determines what, for an ordinary elliptic curve $E/\mathbb F_q$.

1. **Counts.** The degree-resolved overlaps $\langle\Theta_K,1_D\rangle=q^{h^0(D)}$ give $A(n)$, then $a_n$, then $Z(T)$, then $P(T)$, which is equivalent to the counts
   $N_k$ (*standard*; checked on E1, §3).
2. **The transfer matrix and the rational module.** $P(T)$ determines the cokernel, its shift $W$ (the integral companion matrix), the discrete
   Wronskian and the Casoratian (§4). Through $S$ it also determines $(\mathbb Q^2,M)$ up to $\mathrm{GL}_2(\mathbb Q)$, which is the isogeny class
   (Honda–Tate, *standard*, from memory). Over $\mathbb R$ it determines $\Omega$ up to scale, and the Weil form, and with them $J$ (§5).
3. **The lattice $L=H_1$ of the canonical lift.** This is an $F$-stable lattice in $\mathbb Q(F)$, equivalently a class of positive forms of discriminant
   $a^2-4q$. **It is not determined by step 1** (checked). E2 has two classes with identical counts, distinguished by the groups of points. E3 has two
   classes with identical counts and identical groups for every $k$ tested. The trivial-character cokernel supplies only the principal class
   $\mathbb Z[F]$. The $D$-resolved overlaps also see which degree-0 divisors are principal, hence $E(\mathbb F_q)$ as a group, so they separate the E2
   pair. Whether they determine $L$ in general: *open*.
4. **$\Omega$ on $L$.** This is the Weil pairing, i.e. the principal polarisation of $E$. In rank 2 the alternating forms on $L$ form a line, so $\Omega$ is
   fixed by $L$ up to sign. The adjunction $\Omega(Fx,y)=\Omega(x,Vy)$ is automatic: $\Omega(Mx,My)=\det M\cdot\Omega(x,y)$ (*elementary*). Its sign is
   Howe's $\varepsilon$ (§5).
5. **$J$ from the polarisation.** $J_\varepsilon$ is the complex structure of the lift, and the vacuum is $J=\pm J_\varepsilon$. The Riemann form
   $\Omega_\varepsilon(\cdot,J_\varepsilon\cdot)=\Omega(\cdot,J\cdot)$ is the Rosati form transported (§5). **This step carries RH.** $J$ exists iff $a^2<4q$, and
   its positivity is Rosati positivity, which comes from geometry (ampleness, analytic §14) and not from steps 1–4. Step 1 *decides* RH, since $P$
   is known, but does not *prove* it. The "fake curve" of analytic §13 ($q=2$, $h=6$) passes steps 2 and 4 formally (an integer step with
   $M^T\Omega M=q\Omega$ exists) and fails at step 5.

**What `adelic-gkp.md` §12 says has no analogue for $\mathbb Q$.**

- Step 5 has none. §12.2: "No polarisation … nothing in the code supplies a structural reason for $\omega$ to be a state."
- Step 1 survives only in degraded form. §12.1: overlaps are Gaussian sums, not counts; there is no exact Riemann–Roch; the cutoff has a plunge layer.
  So the finite-dimensional cokernel of step 2 is not available as such (analytic §13, "What this says for $\mathbb Q$").
- §12 does not discuss analogues of steps 3–4, and this page does not either.

## 7. Status and checks

| statement | status | checks |
|---|---|---|
| Deligne modules of E1, E2, E3; the Weil form of a step is its Latimer–MacDuffee form; lattice classes = reduced positive forms | standard / proved here; checked | D1–D3 |
| $E(\mathbb F_{q^k})\cong\mathbb Z^2/(1-M^k)$ for the companion $M$: holds for E1 and for E3, fails for $y^2=x^3+4x$ over $\mathbb F_5$ at every $k=1..8$ | checked (PARI); negative finding for the general claim | G1–G6 |
| every curve matches exactly the lattice class predicted by its endomorphism ring; E3's two classes have the same groups | checked | G3, G7, G8 |
| $A(\mathbb F_{q^k})\cong T/(1-F^k)T$ for the curve's own Deligne module | sketched (inputs from memory); Lenstra 1996 for elliptic curves, from memory | consistent with G1–G6 |
| overlaps $=q^{h^0(D)}$, $h^0$ matches Riemann–Roch + Abel–Jacobi on 144 divisors of E1 | checked (brute force; $L(nO)$ basis standard) | A1–A5 |
| $A(n)$, $a_n$, $P(T)$ from the overlaps; agreement with the Euler product | checked | A6–A8 |
| Theorem 12 cokernel for E1, E2: dimension 2, recurrence, $W=\bigl(\begin{smallmatrix}a&-q\\1&0\end{smallmatrix}\bigr)$, both Casoratians are $q$-similitudes | checked exactly (Theorem 12 itself from analytic §13) | R1–R5 |
| maps $C$, $\psi$, $S$; $S$ unimodular, intertwines $W$ and $M$, carries $\omega_C\to\Omega$ and $\mathcal Q\to G$ | proved here; checked exactly | B1–B5 |
| bridge identity $\Omega(Ss,JSs)=2\mathcal Q(s)/\sqrt{4q-a^2}=\mathcal T(Cs,Cs)/\sqrt{4q-a^2}$ | proved here; checked exactly and numerically | B6–B8 |
| uniqueness of the similitude form for one mode; the same over $\mathbb Q$ for every lattice class | proved here; checked | B9–B10 |
| the Howe sign cancels in the Riemann form | proved here; primes checked with PARI | H1–H2 |
| the bridge in genus $\ge2$ is only "same cone", not proportionality | sketched | none |
| whether the $D$-resolved overlaps determine $L$; which E3 curve has which class | open | none |
| data ladder (§6) | reformulation of the above; the §12 reading is quoted, not extended | none |

`checks/check_curve_bridge.py`: **82 of 82 pass**, in about 3 s. Exact arithmetic throughout except B3 and B7 (float64).

## 8. Next

- **Genus two.** Repeat §5 on the curve of shard 04w ($y^2=x^5+x^3+x^2-2$ over $\mathbb F_5$). The cokernel is 4-dimensional and the similitude forms
  form a cone. Find where in that cone the Rosati form $\mathcal T$ sits relative to the vacuum forms of the integral Deligne modules in the isogeny
  class. This is where "proportional" is expected to become "same cone" and the bridge acquires content.
- **The E3 assignment.** Decide which of $j=4,5$ over $\mathbb F_7$ has the principal Deligne module for a given $\varepsilon$, using the action of the class group on
  CM lifts.
- **Repair the two sentences** that identify the Pauli-six lattice with "the" curve of shard 03c (`lattice-tower.md` §1 table and §6, `adelic-gkp.md`
  G12(ii)). It is $y^2=x^3+4x\pm1$, not $y^2=x^3+4x$. Left for the page owners; not edited here.
