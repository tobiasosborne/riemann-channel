# Square roots of Ihara--Bass: proofs and corrections

Prover: `codex:gpt-6-astra`. Date: 2026-09-21. This note audits T1--T4 of `astra-brief.md`. All spectra below are over **ℂ**, and all spectral multiplicities are algebraic unless explicitly called geometric. No diagonalizability is implicit. The proofs use the Ihara--Bass and Euler-product identities authorized in the brief.

Three gradings must be distinguished: the auxiliary grading $W_{\rm even}\oplus V_{\rm odd}$ in T1; the bond grading $\Gamma_b=\operatorname{Ad}(P)$ on $\mathcal V=\operatorname{End}(V_{\rm bond})$; and the additional involution $\gamma=L_P$, with edge extension $\Gamma=\gamma\otimes I_D$, in T3. In T3--T4 write $Z_{\rm gr}(u)=\det(I-uH_1)/\det(I-uH_0)$. An eigenvalue of $H_1$ is only a **candidate** zero: common even-sector factors cancel.

## Hypothesis register and conventions

Each item is invoked only where indicated. Conditions defining an optional strengthening are not silently assumed elsewhere.

| Label | Hypothesis / convention | Use |
|---|---|---|
| **H-BASE** | $V$ is finite-dimensional complex, $N=\dim V$; $D=2m\ge2$; reversal is fixed-point-free; $E_i\in\operatorname{End}(V)$; $W,R,S,J,H$ have the conventions of the brief. $u$ is a commuting complex variable. | T1--T2; applied to the appropriate fibre in T3--T4. |
| **H-RES** | At a point $u$, $A_u:=I_W+uJ$ is invertible. Equivalently all $I_V-u^2E_{\bar i}E_i$ are invertible. | Expressions containing $A_u^{-1}$. |
| **H-SCHUR** | H-RES and $p(u):=\det(I_W-uH)\ne0$. | Pointwise comparison of both proposed Schur Berezinians in T1(d). |
| **H-INV** | $E_{\bar i}=E_i^{-1}$ for all $i$. | T1(c) and the authorized inverse-paired Bass identity. |
| **H-ADJ** | A fixed positive definite Hermitian inner product on $V$, with $E_{\bar i}=E_i^*$. Norms are its operator norms. | T2(b)--(c). |
| **H-KRAUS** | $V=M_n(\mathbb C)$, $E_i=\operatorname{Ad}(A_i)$, $A_{\bar i}=A_i^*$, with Hilbert--Schmidt inner product. | The stronger reality assertion and path comparisons in T2. Implies H-ADJ. |
| **H-UNIT** | A nonzero finite-dimensional orthogonally graded Hilbert space $V_{\rm bond}=V_+\oplus V_-$, $P=I\oplus(-I)$, homogeneous unitary letters $U_i$ with $PU_iP=\epsilon_iU_i$, $\epsilon_i\in\{\pm1\}$, and $U_{\bar i}=U_i^*$. On the doubled bond, $\mathcal V=\operatorname{End}(V_{\rm bond})$, $E_i=\operatorname{Ad}(U_i)$, and $\mathcal V_k$ are the $\Gamma_b$-sectors. | T2(d), T3, T4. |
| **H-ODD** | In addition to H-UNIT, every letter has parity $-1$. | T3(b)--(d), T4. Forces $D_+=D_-=d\ge1$; this is proved below. |
| **H-TRIV** | Trivial factors are removed with their **specified sector multiplicities**, as described in T3(d). Unless a smaller structural subspace is specified, use the full common $+1$ and common $-1$ eigenspaces of the letters, together with the Bass topological factors. Retained subspaces/factors are closed under chirality. | Statements using “nontrivial.” This choice is data, not permission to discard all modes sharing a numerical value. |
| **H-IRRED** | The common commutant of the $U_i$ is $\mathbb C I$, equivalently the unitary family acts irreducibly. | Optional conclusion that the only extremal adjacency modes are $I,P$, both even. |
| **H-SS** | The specified retained part of $K_1:=H_1^2\vert _{W_1^+}$ is diagonalizable. | The strengthened Hilbert--Pólya equivalence in T3(c). Not implied by the closed Ramanujan band. |
| **H-NOCANCEL** | No retained odd spectral factors under discussion cancel with even factors. | Only if inferring an entire odd-sector bound from a statement about the actual zeros. |
| **H-REP** | $G$ is a group, $G_0\triangleleft G$ has index two, inverse-labelled generators $s_i\in G\setminus G_0$ generate $G$, and $\pi=\operatorname{Ind}_{G_0}^G\rho$ is finite-dimensional unitary. Set $U_i=\pi(s_i)$. The Cayley cover is the **labelled voltage multigraph** of the bouquet, retaining all edge labels and multiplicities. If finite-cover Artin terminology is required, assume additionally that $G$ is finite; the direct local-system proof does not need finiteness of $G$. | T4(b). The relevant induction formula is proved directly; no unproved **H-ARTIN** is needed. |
| **H-CONT** | In the continuum remark, $L_i$ are odd jump operators and the displayed Lindblad generator has no extra Hamiltonian term. | T3(f); a counterexample to the blanket claim of no continuum analogue. |

Notation: $q=D-1\ge1$, $D_\pm=\dim V_\pm$, $n_k=\dim\mathcal V_k$, $n_0=D_+^2+D_-^2$, $n_1=2D_+D_-$, and $a_k=n_k(D-2)/2$. Write $f^\#(u)=\overline{f(\bar u)}$ for the holomorphic conjugate of a power series. A Berezinian over the purely even coefficient field $\mathbb C$ is assigned here to an **even invertible** endomorphism $T=T_0\oplus T_1$, with
\[
\operatorname{Ber}(T)=\det T_0/\det T_1.
\]
Rational continuations of determinant ratios are distinguished from pointwise Berezinians at singular matrices. Supertrace $\operatorname{Tr}(PT)$ makes sense for every $T$, including odd $T$, but the notation $\operatorname{sdet}(I-uT)$ in the brief requires $T$ to be even.

## T1. Chiral linearisation and the mass Berezinian

### T1(a) -- PROVED

**Statement.** Recall $W=V\otimes\mathbb C^D$,
\[
R(v\otimes|i\rangle)=E_iv,\qquad Sv=\sum_jv\otimes|j\rangle,\qquad
J(v\otimes|i\rangle)=E_iv\otimes|\bar i\rangle,\qquad H=SR-J.
\]
On $W\oplus V$, let
\[
N(u)=\begin{pmatrix}I_W+uJ&S\\uR&I_V\end{pmatrix}
=M(u)+\not D(u),\quad
M(u)=\operatorname{diag}(I_W+uJ,I_V),\quad
\not D(u)=\begin{pmatrix}0&S\\uR&0\end{pmatrix}.
\]
Under H-BASE, $N(u)$ is an affine matrix pencil and
\[
\det N(u)=\det(I_W-uH).
\]
Under H-RES this also equals
\[
\det A_u\,\det\bigl(I_V-uRA_u^{-1}S\bigr).
\]
The latter identity extends as an identity of rational functions. The off-diagonal part is odd for the auxiliary $W/V$ grading; no self-adjoint Dirac structure is asserted.

**<1>1. Claim: eliminating the vertex block gives $I-uH$.**

**Proof.** The vertex block is $I_V$, so its Schur complement is
\[
A_u-S(uR)=I_W+uJ-uSR=I_W-uH.
\]
Block elimination uses unit triangular matrices of determinant one and therefore proves the first identity for every $u$. This also verifies directly the signs and the factor $u$. For the auxiliary parity $Q=\operatorname{diag}(I_W,-I_V)$, direct block multiplication gives $QM(u)Q=M(u)$ and $Q\not D(u)Q=-\not D(u)$, proving the asserted even/odd decomposition. □

**<1>2. Claim: eliminating the edge block gives the deformed Bass determinant.**

**Proof.** Under H-RES, the other Schur complement is $I_V-uRA_u^{-1}S$. Hence
\[
\det N=\det A_u\det(I_V-uRA_u^{-1}S).
\]
The authorized general Ihara--Bass computation identifies the last determinant with $\det(I+D(u)-A(u))$. On every reversal pair, block elimination gives
\[
\det A_u|_{V\oplus V}=\det(I-u^2E_{\bar i}E_i).
\]
This proves both H-RES's equivalence and the stated formula. The excluded set is finite, because the determinant of $A_u$ is a polynomial equal to one at zero; equality therefore holds rationally. □

**<1>3. Claim: the literature comparison is a comparison of determinant mechanisms.**

**Proof.** Matsuura--Ohta use vertex and edge Grassmann fields and a massive graph Dirac matrix whose ordinary determinant produces the graph-zeta denominator; see §2.3, especially equations (2.35)--(2.42), in [*Fermions and Zeta Function on the Graph*, arXiv:2501.08803v2](https://arxiv.org/html/2501.08803v2#S2.SS3). The two block eliminations above give the corresponding bouquet/matrix-weight mechanism directly. This is not a claim that their displayed Dirac matrix is literally $N(u)$, nor that their graph hypotheses automatically include every weighted bouquet here. □

### T1(b) -- PROVED-CORRECTED

**Statement.** Under H-RES let $X=uRA_u^{-1}$, $Y=S$. The nonzero spectra of $YX$ and $XY$, including algebraic multiplicities, agree. On $W_{\rm even}\oplus V_{\rm odd}$,
\[
\Lambda=\operatorname{diag}(YX,XY),\qquad
\operatorname{str}\Lambda^k=0\quad(k\ge1),\qquad
\operatorname{sdet}(I-\Lambda)=1.
\]
The last equality holds wherever the Berezinian is defined, and identically as a rational continuation. The index $N(D-1)$ is the excess **algebraic zero multiplicity / generalized-kernel dimension**, not necessarily the difference of ordinary nullities. Also
\[
\det(I-uH)=\det A_u\det(I-YX)=\det A_u\det(I-XY).
\]

**<1>1. Claim: a single characteristic-polynomial identity proves the spectral pairing.**

**Proof.** Sylvester's identity gives, for $t\ne0$,
\[
\det(tI_W-YX)=t^{ND-N}\det(tI_V-XY).
\]
Both sides are polynomials, so this holds also at zero. It proves the nonzero multiplicity assertion and that the zero multiplicities differ by $ND-N$. In finite dimension the algebraic zero multiplicity equals the dimension of the generalized zero eigenspace. □

**<1>2. Claim: all positive-power supertraces vanish, and the determinant ratio is one.**

**Proof.** Rectangular cyclicity of trace gives
\[
\operatorname{Tr}_W(YX)^k
=\operatorname{Tr}_V\bigl(X(YX)^{k-1}Y\bigr)
=\operatorname{Tr}_V(XY)^k.
\]
Sylvester also gives $\det(I-YX)=\det(I-XY)$. Their quotient is one where its denominator is nonzero, and has rational continuation one through any common zeros. A singular $I-\Lambda$ does not itself have an invertible-operator Berezinian. □

**<1>3. Claim: ordinary kernel dimensions need not have the asserted difference.**

**Proof.** Because $S$ is injective,
\[
\dim\ker(YX)-\dim\ker(XY)
=ND-N-\operatorname{rank}X+\operatorname{rank}(XY).
\]
For an explicit counterexample take $V=\mathbb C$, $D=2$, $E_1=1$, $E_2=2$, and $u=3/4$. Then
\[
A_u=\begin{pmatrix}1&3/2\\3/4&1\end{pmatrix},\quad
X=(3,-3),\quad Y=\binom11,\quad XY=0,\quad
YX=\begin{pmatrix}3&-3\\3&-3\end{pmatrix}.
\]
Here $\det A_u=-1/8\ne0$, $YX\ne0$, $(YX)^2=0$, and both ordinary kernels have dimension one. Their difference is zero although $N(D-1)=1$. The generalized-kernel dimensions are two and one, as required. □

**<1>4. Claim: the edge factorization has the drafted order.**

**Proof.** $YX=uSRA_u^{-1}=u(H+J)A_u^{-1}$, so
\[
(I-YX)A_u=A_u-uSR=I-uH.
\]
Taking determinants and then applying Sylvester proves the remaining identities. □

### T1(c) -- PROVED-CORRECTED

**Statement.** Under H-INV and $u^2\ne1$, the **rescaled diagonal mass**
\[
\widetilde M(u)=\operatorname{diag}\bigl(I_W+uJ,(1-u^2)I_V\bigr)
\]
is an even automorphism of $W_{\rm even}\oplus V_{\rm odd}$, and
\[
\operatorname{Ber}\widetilde M(u)=(1-u^2)^{ND/2-N}.
\]
This is not the Berezinian of the original $M(u)=\operatorname{diag}(I+uJ,I)$, whose Berezinian is $(1-u^2)^{ND/2}$. The equality has a rational, here polynomial, continuation to $u=\pm1$.

**<1>1. Claim: the numerator has exponent $ND/2$.**

**Proof.** H-INV implies $J^2=I_W$ and $E_{\bar i}E_i=I_V$. Each of the $D/2$ reversal pairs contributes $(1-u^2)^N$, by T1(a). Thus $\det(I+uJ)=(1-u^2)^{ND/2}$. □

**<1>2. Claim: the parity convention subtracts the vertex exponent.**

**Proof.** Even blocks occur in the numerator of the Berezinian and odd blocks in the denominator. The odd block contributes $\det((1-u^2)I_V)=(1-u^2)^N$, giving exponent $N(m-1)$. A bouquet has $m$ unoriented edges and one vertex, so this is $-N\chi$. Cell parity $k+1\pmod2$ makes edges $(k=1)$ even and vertices $(k=0)$ odd. This agrees with the sign convention of `def:graded-geodesic-determinant`, extended here to degree zero; reversing the grading inverts this Berezinian. The oriented edge space has $2mN$ dimensions, but its paired determinant contributes $mN$ powers of $1-u^2$, not $2mN$. □

**<1>3. Claim: the mass interpretation includes a necessary rescaling and domain qualification.**

**Proof.** The Bass Schur complement is
\[
I-uR(I+uJ)^{-1}S
=(1-u^2)^{-1}(I-u\Sigma+qu^2I).
\]
Its scalar denominator is exactly the vertex factor included in $\widetilde M$. Thus “mass Berezinian” is accurate for this rescaled diagonal mass. At $u=\pm1$, the displayed blocks are singular, so only the continued scalar identity is asserted. □

### T1(d) -- PROVED-CORRECTED

**Statement.** Put $b(u)=\det A_u$. Under H-SCHUR, the two c-number Schur expressions are $p(u)$ and $b(u)^2/p(u)$, and agree precisely when $p(u)^2=b(u)^2$. They do not define a common Berezinian of $N(u)$. A conventional parity-even boson/fermion Gaussian action cannot have these nonzero c-number mixed blocks. It is too strong to say that integration of a mixed-parity superfunction is mathematically undefined, or that no other super formulation can exist.

**<1>1. Claim: the two expressions have the stated values.**

**Proof.** The first is $\det(A_u-uSR)/\det I=p(u)$. The ordinary Schur identity gives $\det(I-uRA_u^{-1}S)=p(u)/b(u)$, so the second is $b(u)^2/p(u)$. Both denominators are nonzero under H-SCHUR, making the asserted equivalence immediate. As rational functions the same equality criterion is valid. □

**<1>2. Claim: the proposed equality fails even for one classical loop.**

**Proof.** For $V=\mathbb C$, $D=2$, $E_1=E_2=1$, the only allowed successor of a letter is itself, so $H=I_2$. Hence $p=(1-u)^2$ and $b=1-u^2$. At $u=1/2$ the two expressions are $1/4$ and $9/4$. Thus the requested two-loop example is not the smallest counterexample to the Schur-Berezinian claim. □

**<1>3. Claim: the requested two-loop calculation is also a counterexample.**

**Proof.** For $D=4$ and all $E_i=1$, let $T$ be reversal on $\mathbb C^4$, and let $B$ be the all-ones matrix. Then $H=B-T$. On the constant vector it is $3$; on the reversal-even subspace perpendicular to constants it is $-1$; on the two-dimensional reversal-odd subspace it is $+1$. Consequently
\[
p(u)=(1-u)^2(1+u)(1-3u),\qquad b(u)=(1-u^2)^2.
\]
These have different squared polynomials. This two-loop bouquet will be the smallest positive-loop classical bouquet witnessing the **nonpolynomial square root** in T2(e); one loop has the polynomial square root $1-u$. □

**<1>4. Claim: the obstruction is parity of an even supermatrix, not existence of integration.**

**Proof.** An even matrix over a supercommutative algebra must have odd coefficients in its off-diagonal parity blocks. Over $\mathbb C$, such coefficients are zero; $S$ and $uR$ are c-number maps, so $N(u)$ is generally not even. A term pairing a commuting bosonic coordinate with an anticommuting fermionic coordinate via a c-number coefficient is odd, hence is not part of a parity-even Gaussian action. Nevertheless exponential and Berezin integration of a general superfunction are algebraically meaningful. For example, with one Grassmann variable $\theta$, real variable $x$, and $\int d\theta\,\theta=1$,
\[
\int_{\mathbb R}dx\int d\theta\,e^{-x^2+\theta x}
=\int_{\mathbb R}x e^{-x^2}\,dx=0
\]
is perfectly defined despite the odd term. The standard even-Gaussian Berezinian formula is what fails to apply. Assigning fermions to both edge and vertex blocks instead gives an ordinary determinant, as in the Matsuura--Ohta construction cited in T1(a). The cellular parity used for a mass Berezinian is not automatically a field-statistics assignment. In this calculation the valid mass Berezinian is diagonal; neither this observation nor the Schur counterexample excludes other super constructions. Indeed T1(b) already supplies another valid even super-operator, $\Lambda$. □

## T2. Reversal pairs and the oriented half

### T2(a) -- PROVED

**Statement.** Under H-BASE, no nonempty cyclically non-backtracking word is cyclically equivalent to its reverse. Primitivity is unnecessary.

**<1>1. Claim: a hypothetical equivalence gives a reflected label relation.**

**Proof.** Reversal preserves cyclic non-backtracking and is an involution on cyclic classes. It also preserves primitivity: reversing a proper power gives the same power of the reversed word. Index the cyclic word by $k\in\mathbb Z/\ell\mathbb Z$, with label $a_k$. Equivalence to its reversed, barred word means that for some $c\in\mathbb Z/\ell\mathbb Z$,
\[
a_k=\overline{a_{c-k}}\quad\text{for every }k.
\]
The index map $k\mapsto c-k$ is an involution. □

**<1>2. Claim: all possibilities contradict the word hypotheses.**

**Proof.** If $\ell$ is odd, $2k=c$ has a solution, forcing $a_k=\bar a_k$. If $\ell$ is even and $c$ is even, the same equation again has a solution. If $\ell$ is even and $c$ is odd, $2k=c-1\pmod\ell$ has a solution, and then $c-k=k+1\pmod\ell$. The relation becomes $a_k=\bar a_{k+1}$, a forbidden adjacent backtrack, including the cyclic closing adjacency. These cases exhaust all possibilities, also for $\ell=1,2$. □

### T2(b) -- PROVED

**Statement.** Under H-ADJ,
\[
E_{\bar w}=E_w^*,\qquad
\det(I-u^\ell E_{\bar w})
=\overline{\det(I-\bar u^\ell E_w)}.
\]

**<1>1. Claim: the order of adjoints is exactly the order of the reversed word.**

**Proof.** For $E_w=E_{i_\ell}\cdots E_{i_1}$,
\[
E_w^*=E_{i_1}^*\cdots E_{i_\ell}^*
=E_{\bar i_1}\cdots E_{\bar i_\ell}=E_{\bar w}.
\]
Taking determinants of $(I-\bar u^\ell E_w)^*=I-u^\ell E_w^*$ proves the second assertion. □

**<1>2. Claim: each determinant factor is well-defined on a cyclic class.**

**Proof.** A cyclic shift replaces a product $AB$ by $BA$. Sylvester's identity $\det(I-zAB)=\det(I-zBA)$ proves invariance even if the letters are singular. The corresponding invariance of traces follows from cyclicity. □

### T2(c) -- PROVED-CORRECTED

**Statement.** Under H-ADJ let $M=\max_i\|E_i\|$. A sufficient radius of absolute convergence is
\[
r=\frac1{(D-1)M}\quad(M>0),\qquad r=+\infty\quad(M=0).
\]
Choose one member of each reversal pair of primitive cyclic classes and call the resulting set $\Pi$. Then the product
\[
F(u)=\prod_{[w]\in\Pi}\det(I-u^{\ell(w)}E_w)
\]
defines a nonvanishing holomorphic function on $|u|<r$, normalized by $F(0)=1$, and
\[
\det(I-uH)=F(u)F^\#(u).
\]
In particular, for real $|u|<r$, $\det(I-uH)=|F(u)|^2>0$. Thus $1/F$ is the oriented amplitude for the **zeta**, while $F$ is the amplitude for its reciprocal. In general $F$ is not the positive real square root; its modulus is. Under H-KRAUS, the stronger identity $\det(I-uH)=F(u)^2$ holds throughout the complex convergence disk, independently of the orientation choices.

**<1>1. Claim: logarithms of all prime factors converge absolutely and locally uniformly.**

**Proof.** Let $a=|u|M$, so $qa<1$ and $a<1$. A word of length $\ell$ has $\|E_w\|\le M^\ell$, and the logarithm normalized at zero satisfies
\[
\log\det(I-u^\ell E_w)
=-\sum_{j\ge1}\frac{u^{j\ell}}j\operatorname{Tr}(E_w^j),\qquad
\left|\log\det(I-u^\ell E_w)\right|
\le\frac{N a^\ell}{1-a}.
\]
There are at most $Dq^{\ell-1}$ rooted non-backtracking words of length $\ell$, hence at most that many prime classes. Therefore the sum of absolute logarithms is bounded by
\[
\frac{ND}{1-a}\sum_{\ell\ge1}q^{\ell-1}a^\ell
=\frac{NDa}{(1-a)(1-qa)}<\infty.
\]
The same bound on smaller closed disks gives local uniform convergence. Exponentiating the sum gives a nonzero holomorphic product. If $M=0$, all factors and the determinant are one. □

**<1>2. Claim: grouping reversal pairs yields the asserted factorization.**

**Proof.** T2(a) partitions the primes into two-element orbits. Absolute convergence permits regrouping. T2(b) identifies the second factor in each pair with the holomorphic conjugate of the first. The authorized Euler product therefore gives $\det(I-uH)=FF^\#$. On the real interval this is a squared modulus, strictly positive because $F\ne0$. Reciprocating gives $\zeta_H=|1/F|^2$. □

**<1>3. Claim: general adjoint pairing does not make $F$ a real square root.**

**Proof.** Take $D=2$, $V=\mathbb C$, $E_1=i$, $E_2=-i=E_1^*$. The only prime classes are the two single letters. Choosing the first gives $F(u)=1-iu$, while $\det(I-uH)=1+u^2$. On the real interval $|F|^2=1+u^2$, but $F^2\ne1+u^2$. □

**<1>4. Claim: Kraus letters give a stronger real structure.**

**Proof.** The conjugate-linear involution $C(X)=X^*$ commutes with every $\operatorname{Ad}(A)$. Thus $E_w=\operatorname{Ad}(A_w)$ preserves the real vector space of Hermitian matrices; its complex matrix in a real Hermitian basis has real entries. Its characteristic polynomial, and $\det(I-zE_w)$, have real coefficients. T2(b) now says that the two reversal factors are identical as polynomials, not merely conjugate on the real axis. Hence $F^\#=F$, the orientation choices do not change $F$, and $FF^\#=F^2$ on the whole disk. For real $|u|<r$, this $F$ is the positive square root, by nonvanishing, continuity, and $F(0)=1$. This local analytic square root need not be a polynomial or a global single-valued entire function. □

### T2(d) -- PROVED-CORRECTED

**Statement.** Under H-UNIT, the conclusions of T2(c) hold in each bond sector, with the sufficient radius $1/q$. With
\[
F_k(u)=\prod_{[w]\in\Pi}\det_{\mathcal V_k}(I-u^{\ell(w)}E_w),\qquad
F_{\rm gr}=F_0/F_1,
\]
one has
\[
\operatorname{sdet}(I-uH)=F_{\rm gr}(u)^2
\quad (|u|<1/q).
\]
In particular it equals $|F_{\rm gr}(u)|^2$ on the real interval. $Z_{\rm gr}=F_{\rm gr}^{-2}$ there. These are analytic identities near zero; no polynomial-square conclusion follows.

**<1>1. Claim: adjoint pairing and the real structure restrict to both sectors.**

**Proof.** Homogeneity gives $\Gamma_b E_i=E_i\Gamma_b$. The orthogonal sector restrictions therefore satisfy $(E_i|_k)^*=E_{\bar i}|_k$ and have norm at most one. The involution $C(X)=X^*$ preserves both sectors because $PXP=(-1)^kX$ implies $PX^*P=(-1)^kX^*$. Each sector is the complexification of its Hermitian part, so the reality argument of T2(c), step <1>4, works sector by sector. □

**<1>2. Claim: taking the sector ratio proves the graded formula.**

**Proof.** The sector Euler products and T2(c) give $\det(I-uH_k)=F_k^2$, with each $F_k\ne0$ in the disk. Division gives the stated equality. Since $F_k$ is real on the real axis, so is $F_{\rm gr}$, and its square is its squared modulus. The per-prime ratio is exactly $\operatorname{sdet}_{\mathcal V}(I-u^\ell E_w)$, because $E_w$ is even for the bond grading. □

### T2(e) -- PROVED-CORRECTED

**Statement.** The oriented factor need not be polynomial; the two-loop bouquet proves this. General adjoint pairing gives conjugate loop traces, and Kraus pairing gives equal real loop traces. The classical operator is twist symmetric. However, **general Ad-weighted Hashimoto path traces are not twist symmetric in the actual source-weight convention**. Endpoint-inclusive word traces obey a different symmetric identity. There is no general Kac--Ward polynomial-square theorem for these operators.

**<1>1. Claim: the two-loop oriented half is nonpolynomial.**

**Proof.** In the example of T1(d), all prime factors have real coefficients, so $F^2=p$ near zero. Explicitly the normalized germ is
\[
F(u)=(1-u)\sqrt{(1+u)(1-3u)}.
\]
The polynomial $p=(1-u)^2(1+u)(1-3u)$ has simple zeros at $-1$ and $1/3$. A polynomial square has only even zero multiplicities, so this germ cannot be polynomial. Even if one used only $|F|^2=p$ on a real interval, a polynomial $F$ would imply the polynomial identity $FF^\#=p$; a real root of $FF^\#$ has even multiplicity, giving the same contradiction. Determinants of finite affine/polynomial matrix pencils and Pfaffians of finite skew-symmetric affine/polynomial pencils are polynomials; this $F$ cannot be one. This does not exclude representations by matrices with nonpolynomial entries. □

**<1>2. Claim: the appropriate loop reversal identity is exact.**

**Proof.** T2(b) gives $\operatorname{Tr}E_{\bar w}=\overline{\operatorname{Tr}E_w}$. Under H-KRAUS,
\[
\operatorname{Tr}_{M_n}E_w=|\operatorname{Tr}A_w|^2,
\]
so the loop traces are real, nonnegative, and equal on reversal. A general adjoint-paired family only has conjugate equality, not the exact equality of scalar loop weights appearing in the Aizenman--Warzel hypothesis. □

**<1>3. Claim: the actual path weight does not include the terminal edge letter.**

**Proof.** For an allowed path $p=(e,e_1,\ldots,e_{n-1},\bar e)$ of $n$ transitions, the contribution to the $(\bar e,e)$ block of $H^n$ is
\[
T_p=E_{e_{n-1}}\cdots E_{e_1}E_e.
\]
Writing $B=E_{e_{n-1}}\cdots E_{e_1}$, the twisted path has weight $T_{p_T}=B^*E_e$ under H-ADJ. There is no general identity between $\operatorname{Tr}(BE_e)$ and $\operatorname{Tr}(B^*E_e)$. For an explicit **unitary Kraus** counterexample take distinct reversal pairs $e,\bar e$ and $f,\bar f$, and
\[
U_e=U_f=\begin{pmatrix}1&0\\0&i\end{pmatrix},\qquad
U_{\bar e}=U_{\bar f}=U_e^*.
\]
Both paths $(e,f,\bar e)$ and $(e,\bar f,\bar e)$ are non-backtracking. Their actual superoperator traces are respectively
\[
|\operatorname{Tr}(U_fU_e)|^2=|1-1|^2=0,
\qquad
|\operatorname{Tr}(U_f^*U_e)|^2=|2|^2=4.
\]
They are neither equal nor negatives. Repeated matrices at distinct labels are allowed by H-BASE. □

**<1>4. Claim: an endpoint-inclusive trace identity explains the tempting but inapplicable symmetry.**

**Proof.** If the terminal letter is also multiplied, the weights become $E_e^*BE_e$ and $E_e^*B^*E_e$, whose traces are conjugates since $E_eE_e^*$ is self-adjoint. In the Kraus case both traces are real, hence equal. On the single bond this reads
\[
|\operatorname{Tr}(A_e^* A_{e_{n-1}}\cdots A_{e_1}A_e)|^2
=|\operatorname{Tr}(A_e^* A_{\bar e_1}\cdots A_{\bar e_{n-1}}A_e)|^2,
\]
because the middle products are adjoints and $A_eA_e^*$ is self-adjoint. This is a valid identity for endpoint-inclusive words, but it is not the transition path weight from step <1>3. In the classical case every allowed path weight is one, so actual twist symmetry holds and twist antisymmetry fails whenever such a path exists, as it does for two loops. □

**<1>5. Claim: the cited polynomial-square criterion cannot be applied in general.**

**Proof.** [Aizenman--Warzel, arXiv:1709.06052, Definition 3.3 and Lemma 3.4](https://arxiv.org/html/1709.06052#S3.SS1) require a scalar non-backtracking flow matrix with exact loop reversal invariance and twist antisymmetry; for unoriented edge weights their determinant is a polynomial square. Matrix-block trace identities alone are not those hypotheses. In an Ad path expansion all individual path traces are nonnegative, so antisymmetry of those traces would force both paired traces to vanish. The classical example and step <1>3 explicitly violate that requirement, and the nonsquare classical determinant independently disproves any universal polynomial-square claim here. The surface/spin and rotation data in [Loebl--Somberg, arXiv:0912.3200](https://arxiv.org/abs/0912.3200) and the Kac--Ward/Kasteleyn/discrete-Dirac correspondences in [Cimasoni, arXiv:1307.2494](https://arxiv.org/abs/1307.2494) provide additional structures, not an automatic Pfaffian for this Hashimoto operator. The proved replacement is $FF^\#$, strengthened to a local analytic $F^2$ for Kraus letters. The per-word amplitude interpretation is proved precisely in T4(c). □

## T3. Odd-letter chirality and the two-step operator

### T3(a) -- PROVED

**Statement.** Under H-UNIT, $\gamma=L_P$ is a self-adjoint unitary involution on $\mathcal V$, commutes with $\Gamma_b$, and satisfies
\[
\gamma E_i\gamma=\epsilon_i E_i.
\]
Consequently $\Gamma H\Gamma=H^\epsilon$, $\Gamma J\Gamma=J^\epsilon$, and $\gamma\Sigma\gamma=\Sigma^\epsilon$. The sector determinants of $H$ and its sign twist agree. The twist is a linear-operator twist; a negatively signed $\operatorname{Ad}(U_i)$ is not itself a unitary conjugation channel.

**<1>1. Claim: the two involutions commute and preserve the stated sectors.**

**Proof.** $\gamma^2X=P^2X=X$, and $\gamma$ is self-adjoint for the Hilbert--Schmidt inner product since $P=P^*$. Moreover
\[
\gamma\Gamma_b X=P(PXP)=XP=\Gamma_b(PX).
\]
Thus $\gamma$ and its edge extension preserve both bond-parity sectors. □

**<1>2. Claim: conjugating a letter produces its parity sign.**

**Proof.** For every $X$,
\[
\gamma E_i\gamma(X)=PU_iPXU_i^*
=\epsilon_i U_iXU_i^*=\epsilon_i E_i(X).
\]
Apply this identity separately to each source-labelled summand in $H,J$, and sum over $i$ for $\Sigma$. Since $\Gamma$ preserves each $W_k$, its restrictions implement similarities $H_k\sim H_k^\epsilon$. Similar matrices have the same determinant polynomials. □

### T3(b) -- PROVED-CORRECTED

**Statement.** Under H-ODD, $\Gamma$ anticommutes with $H,J$ and $\gamma$ anticommutes with $\Sigma$, also on each bond sector. The sector spectra are symmetric under sign, with algebraic multiplicities. Put
\[
\mathcal V_k^\pm=\ker(\gamma\mp I)\cap\mathcal V_k,\qquad
W_k^\pm=\mathcal V_k^\pm\otimes\mathbb C^D.
\]
Necessarily $D_+=D_-=d$, and each $\mathcal V_k^\pm$ has dimension $d^2$. In these decompositions,
\[
H_k=\begin{pmatrix}0&h_k\\h'_k&0\end{pmatrix},\quad
K_k:=H_k^2|_{W_k^+}=h_kh'_k,\quad
\det(I-uH_k)=\det(I-u^2K_k).
\]
The graded zeta satisfies the rational identities
\[
Z_{\rm gr}(u)
=\frac{\det(I-u^2K_1)}{\det(I-u^2K_0)},\qquad
Z_{\rm gr}(u)^2
=\frac1{\operatorname{sdet}_{\Gamma_b}(I-u^2H^2)}.
\tag{3.1}
\]
It is the unique square-root germ normalized by $Z_{\rm gr}(0)=1$, and is already a rational function of $u^2$. This is a square root of the **two-step zeta evaluated at $u^2$**, not a polynomial-square assertion about the original zeta.

On the vertex fibre,
\[
\Sigma_k=\begin{pmatrix}0&\alpha_k\\\alpha_k^*&0\end{pmatrix},\qquad
\det(I-u\Sigma_k+qu^2I)
=\det_{\mathcal V_k^+}\bigl((1+qu^2)^2I-u^2\alpha_k\alpha_k^*\bigr).
\tag{3.2}
\]
With H-TRIV, the sector Ramanujan band is equivalent to $0\le\alpha_k\alpha_k^*\le4qI$ on the retained part. The two-step path operator retains the original adjacency constraints, as specified in T3(c).

**<1>1. Claim: odd unitaries force balanced dimensions and give the block decompositions.**

**Proof.** An odd unitary maps $V_+$ isometrically onto $V_-$ and conversely, so their dimensions are equal, say $d$. Left multiplication by $P$ records the parity of the **range** of an operator. Thus
\[
\begin{array}{ll}
\mathcal V_0^+=\operatorname{End}(V_+),&
\mathcal V_0^-=\operatorname{End}(V_-),\\
\mathcal V_1^+=\operatorname{Hom}(V_-,V_+),&
\mathcal V_1^-=\operatorname{Hom}(V_+,V_-).
\end{array}
\]
Each dimension is $d^2$. T3(a) with every $\epsilon_i=-1$ gives anticommutation, forcing the diagonal blocks of $H_k,\Sigma_k$ to vanish. It also gives $n_0=n_1=2d^2$, so the Bass topological factors cancel in $Z_{\rm gr}$. □

**<1>2. Claim: chirality gives sign-symmetric spectra and even determinant polynomials.**

**Proof.** More explicitly than similarity,
\[
\Gamma_k(H_k-\mu I)^r=(-1)^r(H_k+\mu I)^r\Gamma_k
\]
identifies the generalized eigenspaces at $\mu$ and $-\mu$. Thus multiplicities and Jordan block sizes pair. Conjugating $I-uH_k$ proves equality of its determinant at $u,-u$. The same argument applies to $I-u\Sigma_k+qu^2I$. □

**<1>3. Claim: block elimination proves the one-half determinant and both zeta identities.**

**Proof.** The lower diagonal block of $I-uH_k$ is an identity, so
\[
\det\begin{pmatrix}I&-uh_k\\-uh'_k&I\end{pmatrix}
=\det_{W_k^+}(I-u^2h_kh'_k).
\]
Taking the odd/even ratio proves the first equality in (3.1). Also
\[
I-u^2H_k^2=(I-uH_k)(I+uH_k),
\]
so evenness gives $\det(I-u^2H_k^2)=\det(I-uH_k)^2$. Taking sector ratios proves the second equality. A square-root germ with constant term one is unique: if $f^2=g^2$ and $f(0)=g(0)=1$, then $(f-g)(f+g)=0$ and $f+g$ is invertible near zero. These equalities extend rationally. □

**<1>4. Claim: the Bass off-diagonal blocks are adjoints, with no missing scalar power in (3.2).**

**Proof.** $\Sigma^*=\sum_iE_i^*=\sum_iE_{\bar i}=\Sigma$. Its orthogonal $\gamma$-eigenspace decomposition therefore gives lower block $\alpha_k^*$. Put $c=1+qu^2$ and $r_k=\dim\mathcal V_k^+=\dim\mathcal V_k^-$. For $c\ne0$, Schur elimination gives
\[
\det\begin{pmatrix}cI&-u\alpha_k\\-u\alpha_k^*&cI\end{pmatrix}
=c^{r_k}\det(cI-u^2c^{-1}\alpha_k\alpha_k^*)
=\det(c^2I-u^2\alpha_k\alpha_k^*).
\]
Both sides are polynomials, so this also holds at $c=0$. Equal dimensions are essential to the absence of an extra power of $c$; here they are a consequence of odd unitarity. □

**<1>5. Claim: the band is a singular-value bound on the even two-step adjacency block.**

**Proof.** A singular-value decomposition of $\alpha_k$, with independent unitary bases in $\mathcal V_k^\pm$, puts $\Sigma_k$ into the orthogonal sum
\[
\begin{pmatrix}0&s_j\\s_j&0\end{pmatrix},\qquad s_j\ge0.
\]
Its eigenvalues are $\pm s_j$, and those of $\alpha_k\alpha_k^*$ are $s_j^2$. A zero singular value gives two zero adjacency eigenvalues. Removing specified complete chiral pairs as in H-TRIV preserves the correspondence. Therefore $|\lambda|\le2\sqrt q$ iff $s_j^2\le4q$. The operator $\alpha_k\alpha_k^*=\Sigma_k^2|_{\mathcal V_k^+}$ is self-adjoint positive, whereas $K_k=H_k^2|_{W_k^+}$ need not be self-adjoint or diagonalizable. □

**<1>6. Claim: the retained adjacency band is equivalent to the retained edge circle.**

**Proof.** A real adjacency eigenvalue $\lambda$ contributes the two roots of $\mu^2-\lambda\mu+q=0$ through Bass. If $|\lambda|\le2\sqrt q$, these roots are a conjugate pair with product $q$, or the repeated real root $\pm\sqrt q$, so both have modulus $\sqrt q$. If both roots have that modulus, write one as $\sqrt q\,e^{it}$; their product forces the other to be $\sqrt q\,e^{-it}$ and therefore $\lambda=2\sqrt q\cos t$. The topological and designated extremal factors are removed as in H-TRIV. This is an eigenvalue statement including the band endpoints, not a semisimplicity statement. □

### T3(c) -- PROVED-CORRECTED

**Statement.** Under H-ODD,
\[
W_1^+=\operatorname{Hom}(V_-,V_+)\otimes\mathbb C^D,\qquad
W_1^-=\operatorname{Hom}(V_+,V_-)\otimes\mathbb C^D.
\]
The spectrum of $K_1$ consists of the squares of one representative of each sign pair of eigenvalues of $H_1$, with the multiplicity of **one** member of the pair. Actual zeros satisfy the multiplicity criterion below, not merely membership in this spectrum. Under H-TRIV,
\[
\begin{split}
&\text{every retained odd edge eigenvalue has modulus }\sqrt q\\
&\quad\Longleftrightarrow\quad
\text{every retained eigenvalue of }K_1\text{ has modulus }q.
\end{split}
\tag{3.3}
\]
These are entire-sector conditions. They imply the corresponding assertion about retained zeros; the converse from zeros requires H-NOCANCEL. Diagonalizable unimodular $q^{-1}K_1$ is equivalent to (3.3) **plus H-SS**, not to (3.3) alone.

**<1>1. Claim: the exact two-step formula has even transports and inherited path restrictions.**

**Proof.** Two applications of the source-weight rule give
\[
H^2(X\otimes|i\rangle)
=\sum_{\substack{j\ne\bar i\\k\ne\bar j}}
\operatorname{Ad}(U_jU_i)(X)\otimes|k\rangle.
\tag{3.4}
\]
The transport order is $U_jU_i$. Products of two odd letters are even and preserve the displayed mixed blocks. Formula (3.4) restricted to $W_1^+$ is exactly $K_1$. It is a two-step Hashimoto-type operator, not automatically an ordinary Hashimoto operator on a freely enlarged alphabet of even pairs: both intermediate and next-step restrictions remain. □

**<1>2. Claim: these Hashimoto operators are invertible.**

**Proof.** Let $T$ be reversal on $\mathbb C^D$, and let $B$ be the all-ones matrix minus $T$. On the constant line $B$ has eigenvalue $q$; on the reversal-even subspace perpendicular to constants, eigenvalue $-1$; on the reversal-odd subspace, eigenvalue $+1$. These spaces span and $q\ge1$, so $B$ is invertible. The source-weight rule gives
\[
H=(I_{\mathcal V}\otimes B)\operatorname{diag}(E_1,\ldots,E_D).
\]
Each $E_i$ is invertible, hence so are $H$, its invariant sector restrictions, and their squares. An invertible off-diagonal $H_k$ has isomorphisms $h_k,h'_k$ in its two blocks. Thus $h'_kh_k$ is similar to $K_k=h_kh'_k$. The same argument applies to the single-layer $h$ in T4. □

**<1>3. Claim: squaring gives the precise multiplicity correspondence.**

**Proof.** Block elimination, initially at $z\ne0$ and then polynomially, gives
\[
\det(zI_{W_k}-H_k)=\det(z^2I_{W_k^+}-K_k).
\tag{3.5}
\]
An eigenvalue $\rho\ne0$ of $K_k$ of multiplicity $a$ contributes $(z^2-\rho)^a$, hence multiplicity $a$ at each of $\mu,-\mu$. Conversely this accounts for every edge eigenvalue. The full $H_k^2$ has multiplicity $2a$ at $\rho$. Equation (3.3) follows from $|\mu^2|=|\mu|^2$, with the same retained pairs on both sides. □

**<1>4. Claim: zero multiplicities require subtraction of the even sector.**

**Proof.** Let $b_k(\rho)$ be the algebraic multiplicity of $\rho\ne0$ in $K_k$. At either $u_0$ with $u_0^2=\rho^{-1}$, equation (3.1) yields
\[
\operatorname{ord}_{u_0}Z_{\rm gr}=b_1(\rho)-b_0(\rho).
\tag{3.6}
\]
The derivative of $u\mapsto u^2$ is nonzero there, so the local order is unchanged. A positive difference is a zero, a negative difference a pole, and zero means cancellation. For an explicit cancellation example take $\mathbb C^{1|1}$, $P=Z$, $D=4$, and all four letters $U_i=X$, with distinct labelled reversal pairs. On $(I,Z)$ and on $(X,Y)$, $\operatorname{Ad}(X)$ has the same eigenvalues $1,-1$. The edge sectors are therefore similar and $Z_{\rm gr}\equiv1$, although $H_1,K_1$ have nonempty spectra. No candidate point is a zero. □

**<1>5. Claim: a zero-divisor condition does not imply the entire retained odd-sector bound.**

**Proof.** Here is a counterexample even after the default trivial removal. On an ungraded two-dimensional fibre $B$, set $V_1=V_2=I$, $V_3=V_4=\operatorname{diag}(e^{it},e^{-it})$, and $V_5=V_6=\operatorname{diag}(e^{-it},e^{it})$, with reversal $(1\,2)(3\,5)(4\,6)$. Choose $\cos(2t)=3/4$. Then $\sum_i\operatorname{Ad}(V_i)$ has eigenvalue $6$ on diagonal matrices and $2+4\cos(2t)=5$ on both off-diagonal matrix units. Set
\[
V_{\rm bond}=\mathbb C^2\otimes B,\quad P=Z\otimes I,\quad
U_i=X\otimes V_i,\quad D=6,\quad q=5.
\]
All letters are odd and adjoint paired. The actions of $\operatorname{Ad}(X)$ on $\operatorname{span}(I,Z)$ and $\operatorname{span}(X,Y)$ are equivalent, so the doubled even and odd Hashimoto sectors are equivalent and $Z_{\rm gr}=1$. Both sectors nevertheless have adjacency eigenvalues $\pm5$, which are not extremal $\pm6$ and violate $5>2\sqrt5$. These modes survive H-TRIV within each sector but cancel in the net divisor. Thus the assertion that all retained zeros are on the circle, here vacuous, cannot imply the sector condition without a no-cancellation hypothesis. □

**<1>6. Claim: a Hilbert--Pólya form requires diagonalizability as well as the circle bound.**

**Proof.** For a finite-dimensional invertible $T$, diagonalizability with unimodular spectrum is equivalent to a positive definite Hermitian form $G$ satisfying $T^*GT=G$. If $T=CDC^{-1}$ with $D$ diagonal unitary, take $G=(C^{-1})^*C^{-1}$. Conversely $G^{1/2}TG^{-1/2}$ is unitary, hence diagonalizable with unimodular spectrum. Apply this to the specified retained part of $q^{-1}K_1$. A spectral modulus condition alone does not control nilpotent Jordan parts; that is the additional content of H-SS. □

**<1>7. Claim: diagonalizability fails in an explicit all-odd unitary channel at the band edge.**

**Proof.** On $\mathbb C^{1|1}$ with $P=Z$, put
\[
U_\theta=\begin{pmatrix}0&e^{i\theta}\\e^{-i\theta}&0\end{pmatrix},\qquad
(U_1,U_2,U_3,U_4)=(U_0,U_0,U_{\pi/6},U_{\pi/6}),
\]
with reversal $(1\,2)(3\,4)$. These are odd self-adjoint unitaries. On the odd basis $(E_{01},E_{10})$,
\[
\Sigma_1=
\begin{pmatrix}
0&2+2e^{i\pi/3}\\
2+2e^{-i\pi/3}&0
\end{pmatrix},
\]
whose eigenvalues are $\pm2\sqrt3$. The even adjacency eigenvalues are $\pm4$. With $q=3$, Bass and (3.1) give
\[
\det(I-uH_1)=(1-u^2)^2(1-3u^2)^2,\qquad
\det(I-tK_1)=(1-t)^2(1-3t)^2.
\tag{3.7}
\]
This polynomial alone does not prove nonsemisimplicity, so choose $v\ne0$ with $\Sigma_1v=2\sqrt3\,v$. Since $J^2=I$ and $RJS=DI$,
\[
H(Sv)=2\sqrt3\,Sv-JSv,\qquad H(JSv)=qSv.
\tag{3.8}
\]
The vectors $Sv,JSv$ are independent: if $JSv=cSv$, then $c^2=1$ and applying $R$ gives $D=c\lambda$, impossible for $D=4$, $\lambda=2\sqrt3$. Their span therefore carries
\[
C=\begin{pmatrix}2\sqrt3&3\\-1&0\end{pmatrix}.
\]
It has characteristic polynomial $(z-\sqrt3)^2$ and is not scalar, so $C=\sqrt3 I+N$ with $N\ne0$, $N^2=0$. Its square is $3I+2\sqrt3 N$, a nontrivial Jordan block at $3$. Chirality sends this generalized eigenspace of $H_1$ at $\sqrt3$ to one at $-\sqrt3$, disjoint from it. The injective map $x\mapsto x+\Gamma x$ sends the first into $W_1^+$ and intertwines $H_1^2$ with $K_1$. Thus $K_1$ has a nontrivial Jordan block at $3$. This is retained, not a topological $1$ or a Perron square $9$. All retained eigenvalues of $q^{-1}K_1$ are unimodular, but it is not diagonalizable and has no positive definite invariant form. This refutes the drafted final equivalence within the stated channel class. □

**<1>8. Claim: the repository's divisor RH must be distinguished from the sector condition.**

**Proof.** Equation (3.6) is the actual divisor formula. The repository definition “graded RH, functional equation, Ramanujan, manifest form” concerns the retained **net** divisor, with a one-sided bound called RH. The phrase “every nontrivial odd edge eigenvalue has modulus $\sqrt q$” in this brief is the stronger, entire-odd-sector circle condition (3.3). The proofs establish its exact two-step reformulation and preserve the distinction from a zero-only assertion or a condition on the full signed divisor. □

### T3(d) -- PROVED-CORRECTED

**Statement.** Under H-ODD, $I,P$ are linearly independent even adjacency eigenvectors with eigenvalues $D,-D$. In the basis $(I,P)$ the matrix is $\operatorname{diag}(D,-D)$; in the $\gamma$-eigenbasis $(I+P,I-P)$ it is $\left(\begin{smallmatrix}0&D\\D&0\end{smallmatrix}\right)$. They supply the edge factors
\[
(1-u)(1-qu)(1+u)(1+qu).
\]
They need not exhaust the extremal modes without H-IRRED. The complete structural prescription is by sector and multiplicity.

**<1>1. Claim: unitality, oddness, and left parity give the Perron pair.**

**Proof.** Each $E_iI=I$, and $U_iP=-PU_i$ gives $E_iP=-P$. Hence $\Sigma I=DI$, $\Sigma P=-DP$. Left multiplication gives $\gamma I=P$, $\gamma P=I$, proving the matrices in the two bases. Balanced nonzero $V_\pm$ make $I,P$ independent. Both lie in $\mathcal V_0$, not $\mathcal V_1$. □

**<1>2. Claim: the extremal adjacency spaces have an exact structural description.**

**Proof.** Define
\[
\mathcal T_k^+=\{X\in\mathcal V_k:E_iX=X\ \forall i\},\qquad
\mathcal T_k^-=\{X\in\mathcal V_k:E_iX=-X\ \forall i\}.
\]
Unitarity gives
\[
\sum_i\|E_iX-X\|_{\rm HS}^2
=2D\|X\|_{\rm HS}^2-2\langle X,\Sigma X\rangle_{\rm HS}.
\]
The final inner product is real. Thus $\Sigma X=DX$ forces every $E_iX=X$, and the converse is immediate. Using $\|E_iX+X\|^2$ proves the negative case. Hence $\mathcal T_k^\pm=\ker(\Sigma_k\mp DI)$. Chirality gives a sector-preserving isomorphism $\mathcal T_k^+\to\mathcal T_k^-$, so $t_k^+:=\dim\mathcal T_k^+$ equals $t_k^-:=\dim\mathcal T_k^-$. Under H-IRRED, the common fixed algebra is $\mathbb CI$, since $U_iXU_i^*=X$ iff $X$ commutes with all $U_i$. Thus $\mathcal T_0^+=\mathbb CI$, $\mathcal T_0^-=\mathbb CP$, and $\mathcal T_1^\pm=0$. Without irreducibility there can be additional even or odd extremal modes. □

**<1>3. Claim: the default trivial edge divisor is explicit, including coincident values.**

**Proof.** Let $\mathcal T_k=\mathcal T_k^+\oplus\mathcal T_k^-$. Self-adjointness and Bass give
\[
\begin{split}
\det(I-uH_k)
={}&(1-u^2)^{a_k}
[(1-u)(1-qu)]^{t_k^+}
[(1+u)(1+qu)]^{t_k^-}\\
&\times\prod_{\lambda\in\operatorname{spec}(\Sigma_k|_{\mathcal T_k^\perp})}
(1-\lambda u+qu^2),
\end{split}
\tag{3.9}
\]
counting multiplicities, because
\[
1-Du+qu^2=(1-u)(1-qu),\quad
1+Du+qu^2=(1+u)(1+qu).
\]
The topological factor contributes $a_k$ copies each of $\mu=+1,-1$; every designated $+D$ mode contributes one each of $q,1$; every designated $-D$ mode contributes one each of $-q,-1$. For $q=1$ ($D=2$) the numerical values coincide and their multiplicities must be added; also $a_k=0$. A four-element set would lose this information. For $q>1$, passage to $K_k$ turns the topological part into $\rho=1$ with multiplicity $a_k$, and each extremal chiral pair contributes one $\rho=1$ and one $\rho=q^2$.

Subtract sector multiplicities to obtain the graded divisor, after the specified trivial subtraction. Since $a_0=a_1$, topological factors cancel completely. The $I,P$ pair is even and gives poles before any odd cancellation; it is not an odd zero mode. If H-TRIV designates a smaller structural space, undesignated copies remain, even at the same numerical eigenvalues. Equation (3.9) specifies a divisor, not merely a value set. □

### T3(e) -- PROVED-CORRECTED

**Statement.** T3(a) is the general identity under H-UNIT. The specified involution $\Gamma=L_P\otimes I_D$ anticommutes with $H,J$ exactly when all letters are odd; the analogous equivalence holds for $\Sigma$ in this unitary Ad setting. Mixed parity gives no general spectral sign symmetry, but does not forbid a different chiral involution.

**<1>1. Claim: any even letter destroys anticommutation with the specified involution.**

**Proof.** In source column $i$, choose an allowed target $j\ne\bar i$. The $(j,i)$ block of $\Gamma H\Gamma+H$ is $(\epsilon_i+1)E_i$. Since $E_i$ is invertible, all such blocks vanish iff every $\epsilon_i=-1$. The same argument works for $J$. Also
\[
\gamma\Sigma\gamma+\Sigma=2\sum_{\epsilon_i=+1}E_i.
\]
Applied to $I$ this is twice the number of even letters times $I$, nonzero if any even letter occurs. □

**<1>2. Claim: the stated Pauli example lacks sector sign symmetry.**

**Proof.** With $P=Z$, letters $X,X,Y,Y,Z,Z$, and duplicate-pair reversal, $\mathcal V_0=\operatorname{span}(I,Z)$. All six letters fix $I$. Conjugation by $X,Y$ negates $Z$, whereas conjugation by $Z$ fixes it. Hence
\[
\Sigma_0I=6I,\qquad\Sigma_0Z=(-2-2+2)Z=-2Z.
\]
The spectrum $\{6,-2\}$ is not sign-symmetric. □

**<1>3. Claim: mixed parity does not exclude every possible chirality.**

**Proof.** On $\mathbb C^2\otimes\mathbb C^2$ take $P=Z\otimes I$ and two copies each of $X\otimes X$ and $I\otimes X$, with duplicate-pair reversal. Their $P$-parities are mixed. However $Q=I\otimes Z$ anticommutes with every letter and commutes with $P$. By the calculation of T3(a), $L_Q$ anticommutes with all $\operatorname{Ad}(U_i)$ and preserves the $\operatorname{Ad}(P)$ sectors. Its edge extension is another chiral involution. Thus “chirality fails” must specify the involution. □

### T3(f) -- PROVED-CORRECTED (continuum remark)

**<1>1. Claim and explanation.** Under H-CONT, write $\mathcal L=\mathcal J-\mathcal C$, where $\mathcal J(X)=\sum_iL_iXL_i^*$ and $\mathcal C(X)=\tfrac12\{\sum_iL_i^*L_i,X\}$. Oddness gives $\gamma\mathcal J\gamma=-\mathcal J$, while $\gamma\mathcal C\gamma=\mathcal C$, so generally $\gamma\mathcal L\gamma=-\mathcal J-\mathcal C\ne-\mathcal L$. Nevertheless “no continuum analogue” is too strong. If $\sum_iL_i^*L_i=cI$, then $\mathcal L=\mathcal J-cI_{\mathcal V}$ and $\gamma(\mathcal L+cI_{\mathcal V})\gamma=-(\mathcal L+cI_{\mathcal V})$, giving spectral reflection about $-c$. This includes $L_i=\sqrt{r_i}U_i$ with odd unitaries. Equivalently $\gamma e^{t\mathcal L}\gamma=e^{-2ct}e^{-t\mathcal L}$. The literal unshifted transfer symmetry is a lattice statement; a centered continuum reflection can survive. □

## T4. The single layer and its supertrace series

### T4(a) -- PROVED-CORRECTED

**Statement.** Under H-ODD, put $\mathcal B=V_{\rm bond}\otimes\mathbb C^D$, $\mathcal P=P\otimes I_D$, and let $h$ be the single-layer Hashimoto operator. Then
\[
\mathcal P h\mathcal P=-h,\qquad
\det(I-uh)=\det_{\mathcal B_+}(I-u^2h^2|_{\mathcal B_+}),\qquad
\operatorname{str}_{\mathcal P}h^n=0\quad(n\ge1).
\]
Consequently the **defined supertrace generating function**
\[
Z_{\rm str,h}(u):=\exp\left(\sum_{n\ge1}
\frac{u^n}{n}\operatorname{str}_{\mathcal P}h^n\right)
\]
is identically one. However $\operatorname{Ber}(I-uh)$ is **undefined in the even-operator convention of the brief**, because $h$ is odd and $u$ is commuting. A genuine related identity is
\[
\operatorname{sdet}_{\mathcal P}(I-th^2)=1
\]
where defined, with rational continuation one. There is no nontrivial zeta furnished by this single-layer supertrace series. This does not prohibit all other single-layer constructions or every possible relation to doubled data.

**<1>1. Claim: $h$ is odd and its ordinary determinant has the asserted form.**

**Proof.** For every source-labelled vector,
\[
\mathcal P h\mathcal P(v\otimes|i\rangle)
=\sum_{j\ne\bar i}PU_iPv\otimes|j\rangle
=-h(v\otimes|i\rangle).
\]
Thus $h=\left(\begin{smallmatrix}0&a\\b&0\end{smallmatrix}\right)$ on $\mathcal B_+\oplus\mathcal B_-$ and $h^2=\operatorname{diag}(ab,ba)$. Eliminating the identity block of $I-uh$ gives $\det(I-uh)=\det_{\mathcal B_+}(I-u^2ab)$, with no diagonalizability assumption. □

**<1>2. Claim: the supertrace of every positive power vanishes.**

**Proof.** Odd powers have zero diagonal blocks and hence zero supertrace. For even powers,
\[
\operatorname{str}_{\mathcal P}h^{2r}
=\operatorname{Tr}_{\mathcal B_+}(ab)^r
-\operatorname{Tr}_{\mathcal B_-}(ba)^r=0
\]
by rectangular cyclicity of trace. This proof works for any finite-dimensional odd operator, without unitarity or equal dimensions. Substitution into the defining formal series gives $Z_{\rm str,h}=1$. The power series also converges near zero and gives the same analytic identity. □

**<1>3. Claim: this series must not be mislabeled an ordinary Berezinian.**

**Proof.** For a nonzero commuting $u$,
\[
\mathcal P(I-uh)\mathcal P=I+uh\ne I-uh.
\]
Here $h\ne0$, indeed it is invertible by the source-block argument in T3(c). Thus $I-uh$ is not even, and the brief's determinant-ratio definition does not apply. If one introduces the separate notation $\exp[-\sum_n u^n\operatorname{str}h^n/n]$, its value is one, but that is a new supertrace prescription, not a Berezinian of $I-uh$. On the other hand $I-th^2$ is even and Sylvester gives
\[
\operatorname{sdet}(I-th^2)
=\frac{\det(I-tab)}{\det(I-tba)}=1
\]
where the denominator is nonzero, with continuation through common zeros. This is consistent with T1(d). □

### T4(b) -- PROVED-CORRECTED

**Statement.** Under H-REP, let $B_m$ be the labelled $m$-loop bouquet, $X_G$ its voltage cover with deck group $G$, and $Y=X_G/G_0$ the two-vertex intermediate cover. Set $\rho=\pi_+$ and $\rho^t(g)=\rho(t^{-1}gt)$ for any $t\in G\setminus G_0$, so $\pi_-=\rho^t$ after choosing the induced-model bases. Then
\[
L(u,\pi;X_G/B_m)
=\det(I-uh)^{-1}
=L(u,\rho;X_G/Y)
=L(u,\rho^t;X_G/Y).
\tag{4.1}
\]
The right side is the twisted $L$-function on the **two-vertex cover with its induced local system**, not an $L$-function formed by pretending that $\rho$ acts on the odd generators in the base bouquet. Lengths are inherited from base edges. The induction identity is proved below, so no unproved H-ARTIN is used.

**<1>1. Claim: a concrete induced representation gives the edge transports on $Y$.**

**Proof.** Choose coset representatives $t_0=1,t_1=t$. The induced space is $F_0\oplus F_1$, where each $F_a$ is a copy of the space of $\rho$, and the summand $a$ is represented by $t_a\otimes F$ in $\mathbb C[G]\otimes_{\mathbb C[G_0]}F$. For a letter $s_i$ and $a\in\{0,1\}$, put $b=1-a$ and
\[
k(i,a)=t_b^{-1}s_it_a\in G_0.
\]
Then
\[
\pi(s_i)(t_a\otimes v)=t_b\otimes\rho(k(i,a))v.
\tag{4.2}
\]
The graph $Y$ has an oriented edge $(a,i)$ from $a$ to $b$, with reverse $(b,\bar i)$; its transport is $\rho(k(i,a))$. Since
\[
k(\bar i,b)=t_a^{-1}s_i^{-1}t_b=k(i,a)^{-1},
\]
reverse transport is inverse transport. The graph is a labelled multigraph even if some generators are involutions or repeated. Collapsing parallel edges would change the non-backtracking operator and is not allowed. □

**<1>2. Claim: the two transfer operators are the same after identifying their state spaces.**

**Proof.** The twisted edge state space on $Y$ is the direct sum of the source fibres $F_a$ over all $(a,i)$. Identify a vector in this state with $(t_a\otimes v)\otimes|i\rangle$ in $\mathcal B$. Traversing $(a,i)$ applies (4.2), then chooses any next letter $j\ne\bar i$ at vertex $b$. This is exactly the defining action of $h$. Therefore the twisted Hashimoto operator on $Y$ and the induced-representation Hashimoto operator on the bouquet have identical matrices in these bases. Their determinant reciprocals agree. □

**<1>3. Claim: these determinant reciprocals are the asserted Euler-product $L$-functions.**

**Proof.** On either graph, expand
\[
-\log\det(I-uT)=\sum_{n\ge1}\frac{u^n}{n}\operatorname{Tr}T^n
\]
for $|u|$ sufficiently small. The trace sums fibre holonomy traces over rooted cyclically non-backtracking closed paths. Each closed path is a power of a unique primitive cyclic class; a primitive path of length $\ell$ contributes $\ell$ rooted shifts to each of its powers. Regrouping gives, for a primitive holonomy $M_p$,
\[
\sum_{r\ge1}\frac{u^{r\ell}}r\operatorname{Tr}(M_p^r)
=-\log\det(I-u^\ell M_p).
\]
The product of these determinant reciprocals is the Artin--Ihara $L$-function for the relevant local system. The same counting bound as T2(c), with the finite number of vertices included, gives absolute convergence for $|u|<1/q$ for these unitary transports. On the bouquet $M_p=\pi(s_{i_\ell}\cdots s_{i_1})$; on $Y$ it is the product of the transports (4.2), representing the corresponding $G_0$ holonomy. Step <1>2 proves the equality of their products near zero and hence rationally. This is the needed induction formula, proved without a covering-theory black box. □

**<1>4. Claim: replacing $\rho$ by its odd-coset conjugate does not change the $L$-function.**

**Proof.** The map
\[
\mathbb C[G]\otimes_{G_0}F_{\rho^t}\longrightarrow
\mathbb C[G]\otimes_{G_0}F_\rho,\qquad
g\otimes v\longmapsto gt\otimes v
\]
is well-defined: the relation $gh\otimes v=g\otimes\rho^t(h)v$ is preserved since $ht=t(t^{-1}ht)$. It is invertible and $G$-equivariant. Thus $\operatorname{Ind}\rho^t\cong\operatorname{Ind}\rho$, giving equal bouquet edge determinants. Applying the already proved transfer identity to each representation gives the last equality in (4.1). For finite covers this is the standard Artin formalism developed by [Stark--Terras, *Zeta Functions of Finite Graphs and Coverings, Part II*, Advances in Mathematics 154 (2000), 132–195](https://doi.org/10.1006/aima.2000.1917). The preceding proof supplies the particular induction statement needed here. □

**<1>5. Claim: cancellation of the single-layer supertraces is an aggregate word identity, not pointwise equality of the characters.**

**Proof.** On $g\in G_0$, the induced representation is block diagonal with restrictions $\rho(g),\rho^t(g)$, so
\[
\operatorname{Tr}(P\pi(g))=\chi_+(g)-\chi_-(g).
\]
For an odd-coset element this trace is zero. By the trace expansion of $h^n$ and T4(a),
\[
\sum_{\substack{(i_1,\ldots,i_n)\\\text{cyclically non-backtracking}}}
\operatorname{Tr}(P\,U_{i_n}\cdots U_{i_1})=0.
\tag{4.3}
\]
One can also see this without induction: for an odd matrix $A$ and any $B$,
\[
\operatorname{Tr}(PAB)=\operatorname{Tr}(BPA)
=-\operatorname{Tr}(PBA).
\tag{4.4}
\]
One-place cyclic rotation of a labelled word therefore changes its supertrace sign, and rotation permutes the rooted words in (4.3). For odd $n$ the product is odd and each supertrace is already zero. For even $n$ the sum cancels, although individual amplitudes need not vanish. Equality of the two $L$-functions does not assert $\chi_+=\chi_-$ pointwise. □

### T4(c) -- PROVED-CORRECTED

**Statement.** Under H-ODD (indeed H-UNIT suffices for the displayed doubled trace formula),
\[
\operatorname{str}_{\Gamma_b\otimes I_D}H^n
=\sum_{\substack{(i_1,\ldots,i_n)\\\text{cyclically non-backtracking}}}
\left|\operatorname{Tr}(P U_{i_n}\cdots U_{i_1})\right|^2\ge0.
\tag{4.5}
\]
The doubled ring norm is the squared Euclidean norm of the **vector of single-word amplitudes**, not the square of their sum. Its square root is that vector norm; per word, its summand has square root $|\operatorname{Tr}(PU_w)|$. The single-layer supertrace series is trivial, whereas the doubled even operator can have a nontrivial graded zeta with zeros. No universal operator-level square-root or spectral-squaring identification follows.

**<1>1. Claim: the superoperator supertrace is a squared single-bond supertrace.**

**Proof.** For any matrix $A$, column stacking gives $\operatorname{Ad}(A)=\overline A\otimes A$, hence
\[
\operatorname{Tr}_{\operatorname{End}(V_{\rm bond})}\operatorname{Ad}(A)
=\overline{\operatorname{Tr}A}\operatorname{Tr}A.
\]
Also $\Gamma_b\operatorname{Ad}(U_w)=\operatorname{Ad}(PU_w)$. It follows that
\[
\operatorname{str}_{\Gamma_b}\operatorname{Ad}(U_w)
=|\operatorname{Tr}(PU_w)|^2.
\]
Expanding $H^n$ and taking the edge trace forces the last edge label to equal the first, imposing precisely the cyclic non-backtracking condition. Summing the identity proves (4.5). Homogeneity ensures that $H$ is even for $\Gamma_b$, so its supertrace exponential is the genuine determinant-ratio zeta:
\[
Z_{\rm gr}(u)
=\exp\left(\sum_{n\ge1}\frac{u^n}{n}
\operatorname{str}_{\Gamma_b\otimes I_D}H^n\right)
\]
near zero. □

**<1>2. Claim: individual amplitudes can survive the aggregate single-layer cancellation.**

**Proof.** Take $P=Z$ and four odd letters $X,X,Y,Y$, with identical copies paired as reversals. For a word using one $X$ label followed by one $Y$ label,
\[
U_w=YX=-iZ,\qquad \operatorname{Tr}(PU_w)=-2i.
\]
The rotated word has product $XY=iZ$ and amplitude $2i$. Both are allowed. Their amplitudes cancel, but their squared moduli add to eight. There are eight rooted length-two words with one $X$ and one $Y$ label, all of squared amplitude four; other allowed length-two words have zero amplitude. Thus $\operatorname{str}h^2=0$ and $\operatorname{str}H^2=32$. More generally (4.4) shows that the single-layer supertrace amplitude need not be a function of an unbased cyclic class: it changes sign under a one-place rotation. Its squared modulus is class-invariant. □

**<1>3. Claim: the same example has explicit doubled zeros and no spectral-squaring identification with $h$.**

**Proof.** Here $\Sigma_0$ has eigenvalues $4,-4$. On the odd basis $(X,Y)$ the two conjugations cancel, so $\Sigma_1=0$. The equal topological factors cancel, and Bass gives
\[
Z_{\rm gr}(u)=\frac{(1+3u^2)^2}{(1-u^2)(1-9u^2)}.
\tag{4.6}
\]
Its finite zeros are $u=\pm i/\sqrt3$, each of order two. The candidate squared odd edge eigenvalue is $\rho=-3$. By contrast, single-layer adjacency is $2X+2Y$, with eigenvalues $\pm2\sqrt2$. Applying the authorized inverse-paired Bass identity with letters $U_i$ on the two-dimensional single bond gives
\[
\det(I-uh)=(1-u^2)^2(1-2u^2+9u^4).
\tag{4.7}
\]
The squares of the single-layer edge eigenvalues are $1$ and $1\pm2\sqrt2\,i$, none equal to $-3$. Thus even a proposed equality between the doubled candidate squares and the single-layer edge squares fails in this smallest odd-unitary example. The trivial series $Z_{\rm str,h}=1$ certainly cannot supply the zeros (4.6), whereas the ordinary single-layer determinant remains nontrivial. The precise surviving amplitude statement is (4.5), not a claim about “anything” constructible from a single bond. □

Exact supplemental checks: [scratch/astra_exact_checks.py](scratch/astra_exact_checks.py) verifies the kernel and twist counterexamples, the retained Jordan block, and the Pauli single/doubled example using exact symbolic arithmetic. All checks passed. These checks are not premises of the proofs above.

## Correction ledger

The status PROVED-CORRECTED means the corrected statement above is proved under its registered hypotheses. Counterexamples inside those proofs refute the indicated stronger clauses of the draft.

| Label | What was drafted | What is true | Why / witness |
|---|---|---|---|
| T1(b)-kernel | $N(D-1)$ counts the excess ordinary kernel of $YX$. | It is the excess algebraic zero multiplicity, or generalized-kernel dimension. Ordinary nullities can differ by less. | $D=2$, $E_1=1,E_2=2,u=3/4$: $XY=0$, $YX\ne0$ is nilpotent; both ordinary nullities are one. |
| T1(b)-domain | $\operatorname{sdet}(I-\Lambda)=1$ pointwise without qualifications. | A Berezinian needs an even automorphism; the ratio is one where defined and continues rationally through common zeros. | Both determinant factors may vanish. |
| T1(c)-mass | The Euler factor is the Berezinian of the mass $M$ as defined in T1. | It is the Berezinian of the **rescaled** diagonal mass $\widetilde M$, with vertex block $(1-u^2)I$. | Original $M$ gives exponent $ND/2$; vertex rescaling subtracts $N$. |
| T1(c)-singular | The displayed Berezinian is available also at $u=\pm1$. | Only the scalar continuation is available at these singular blocks. | An ordinary Berezinian here is defined on even invertible operators. |
| T1(d)-domain | Compare both proposed Schur ratios everywhere. | Pointwise comparison requires H-SCHUR; otherwise use rational identities. | The second ratio divides by both the edge block determinant and the Schur determinant. |
| T1(d)-smallest | Two loops are the smallest classical Schur-Berezinian counterexample. | One loop already fails; two loops are the smallest positive-loop bouquet needed for the nonsquare-polynomial example. | For one loop, the ratios at $u=1/2$ are $1/4$ and $9/4$. |
| T1(d)-integral | A Gaussian Berezin integral with these c-number mixed blocks is undefined. | These blocks do not give a conventional **even** boson/fermion Gaussian action or its Berezinian formula; integration of mixed-parity superfunctions can still be defined. | The explicit integral of $e^{-x^2+\theta x}$ exists. |
| T1(d)-exclusivity | The diagonal mass is the only super-object in Ihara--Bass. | It is the valid mass Berezinian in this decomposition; no universal exclusion of other super formulations follows. | T1(b)'s even $\Lambda$ and the genuine bond-graded determinant are already other super-objects. |
| T2(c)-square-root | The oriented half itself is a real-axis square root of the zeta. | $FF^\#=\det(I-uH)$; on the real axis $\vert F\vert $ is its positive square root, and $1/F$ is the zeta amplitude. | $E_1=i,E_2=-i$ gives $F=1-iu$, determinant $1+u^2$. |
| T2(c,d)-Kraus | Only a modulus-square identity is available for Kraus/graded unitary letters. | Here the oriented product is real and orientation-independent; $F^2$ and $F_{\rm gr}^2$ are analytic identities in the complex convergence disk. | Ad maps preserve the real Hermitian subspaces, sector by sector. |
| T2(e)-reversal | Trace conjugation is the full scalar Aizenman--Warzel time-reversal hypothesis. | It is conjugate equality in general, exact real equality for Kraus loop traces; block traces still are not scalar path weights. | T2(b) and $\operatorname{Tr}\operatorname{Ad}(A)=\vert \operatorname{Tr}A\vert ^2$. |
| T2(e)-twist | Ad-weighted Hashimoto paths are twist symmetric. | Actual source-weighted transition paths need not be; an endpoint-inclusive word identity is symmetric in the Kraus case. | Distinct labels $e,f$ with $U_e=U_f=\operatorname{diag}(1,i)$ give twisted path traces $0$ and $4$. |
| T2(e)-Pfaffian | The cited Dirac/Pfaffian constructions identify this square root. | They require additional scalar sign/rotation/spin structures; no universal finite polynomial-pencil determinant or Pfaffian realizes $F$. | Classical two-loop determinant has simple real roots and no polynomial square root. |
| T3(b)-dimensions | The displayed Bass half-block formula has no stated dimension condition. | Its chiral halves have equal dimension because odd unitarity forces $D_+=D_-$. | An odd unitary is a bijection between the two bond parity spaces. |
| T3(b,c)-two-step | $H^2$ is a Hashimoto operator obtained just by treating even two-letter products as new letters. | It is the explicit two-step operator (3.4), with both original path restrictions and order $U_jU_i$. | Direct iteration of the source-weighted definition. |
| T3(c)-multiplicity | The half-block spectrum is simply the spectrum of $H_1$ squared. | Each sign pair contributes the multiplicity of one member; the full squared operator has twice that multiplicity. | Characteristic identity (3.5). |
| T3(c)-zeros | Every odd edge eigenvalue gives a graded-zeta zero. | The zero order is odd multiplicity minus even multiplicity at the same point. | Formula (3.6); the all-$X$ example has $Z_{\rm gr}=1$. |
| T3(c)-RH | The entire odd-sector circle condition is identical to the notebook's graded/divisor RH. | Entire-sector, zero-only, and retained signed-divisor conditions must be distinguished; converse from zeros needs H-NOCANCEL. | The degree-six tensor example cancels retained adjacency modes $\pm5$ outside the $q=5$ band. |
| T3(c)-HP | Modulus $q$ for the two-step spectrum is equivalent to diagonalizable unimodular normalized spectrum. | Diagonalizability is additional H-SS; together they are equivalent to a positive definite invariant Hermitian form. | The $U_0,U_0,U_{\pi/6},U_{\pi/6}$ example has a retained Jordan block at $3$. |
| T3(d)-basis | The $\gamma$-eigenvectors and a diagonal adjacency matrix are listed without naming the two different bases. | Diagonal form is in $(I,P)$; chiral off-diagonal form is in $(I+P,I-P)$. | Direct change of basis. |
| T3(d)-trivial | The set $\{q,1,-q,-1\}$ and topological $\pm1$ fully describes triviality. | Record sector multiplicities, additional fixed/anti-fixed modes, and value coincidences; only H-IRRED makes $I,P$ the complete extremal pair. | Formula (3.9); for $q=1$ several values coincide. |
| T3(e)-chirality | Any even letter rules out chirality altogether. | It rules out the specified $L_P$ chirality; another commuting grading may implement it. | Mixed $X\otimes X,I\otimes X$ letters admit $L_{I\otimes Z}$. |
| T3(f)-continuum | Odd Lindblad jumps have no continuum chiral analogue. | Unshifted chirality generally fails, but scalar loss permits reflection about the decay center. | $\mathcal L=\mathcal J-cI$ has chiral $\mathcal L+cI$. |
| T4(a)-Berezinian | $\operatorname{sdet}(I-uh)=1$ for odd $h$. | That Berezinian is not defined with commuting $u$; the explicitly defined supertrace series is one, and the genuine $\operatorname{sdet}(I-th^2)$ is one. | $I-uh$ is not even; rectangular trace and determinant identities prove the corrected statements. |
| T4(a,c)-no-single-layer | There is no single-layer zeta, and doubled zeros are not squares of “anything” on the single bond. | This particular single-layer supertrace prescription is trivial; the ordinary determinant is nontrivial, and no general exclusion of other constructions follows. | Equations (4.6)--(4.7) refute a natural spectral-squaring identification without making an undefined universal claim. |
| T4(b)-Artin-data | Write $L(u,\pi_\pm;Y)$ without specifying transports or cover conventions. | Use the local systems induced from $X_G/Y$, preserving labelled edges, multiplicities, and base-edge lengths. The induction identity is proved directly. | Explicit induced matrices (4.2) identify the edge transfer operators. |
| T4(b,c)-amplitude | Vanishing single-layer supertrace suggests pointwise character cancellation or a single operator square root of the ring norm. | Cancellation is over rooted words. The doubled trace is the squared norm of the word-amplitude vector; the amplitude can change sign under cyclic rotation. | Equations (4.3)--(4.5); the $XY/YX$ amplitudes are $2i,-2i$. |

## Three statements most useful for the lab book

1. **Exact two-step zero formula.** With all letters odd, the grading is balanced and
   \[
   Z_{\rm gr}(u)=\frac{\det(I-u^2K_1)}{\det(I-u^2K_0)},\qquad
   K_1=H_1^2|_{\operatorname{Hom}(V_-,V_+)\otimes\mathbb C^D}.
   \]
   Actual zeros have order $b_1(\rho)-b_0(\rho)>0$ at $u^2=\rho^{-1}$. This identifies the mixed block while retaining the cancellation essential to a zeta divisor.

2. **Band, circle, and manifest form are distinct levels.** The sector band is exactly the positive-block bound $\alpha_k\alpha_k^*\le4qI$ after specified trivial removal. It gives the two-step circle $|\rho|=q$; a positive definite Hilbert--Pólya form additionally requires semisimplicity. Band-edge Jordan blocks occur even for odd unitary qubit letters.

3. **Word amplitudes explain why doubling creates a nontrivial graded zeta.** The single-layer supertrace sums vanish, while $\operatorname{str}H^n=\sum_w|\operatorname{Tr}(PU_w)|^2$ can be positive and yield zeros after sector subtraction. The oriented Euler half is a convergent analytic square root in the Kraus setting, generally nonpolynomial; it must be kept separate from both a Pfaffian construction and the two-step identity.
