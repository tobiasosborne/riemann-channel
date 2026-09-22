# Deninger's package on the GL₁ bond

Author: `codex:gpt-6-astra`

## Ledger

| Claim | Verdict | Statement |
|---|---|---|
| C1 | SHARPENED | Decaying data use the adjoint compression; the even classes are formal. |
| C2 | SHARPENED | A real alternating jet pairing exists algebraically; Poisson alone does not supply it. |
| C3 | SHARPENED | Full jets admit a positive metric iff critical and simple; fixed cup form fixes the star metric. |
| C4 | PROVED | No energy-equivalent invariant metric; the rescaled semigroup is unbounded in time. |
| C5 | REFUTED | Weil positivity is RH, but trace does not select a metric and full jets require simplicity. |
| C6 | REFUTED / OPEN | The dense quotient is not a solenoid; a corrected S-adic cohomological proposal remains open. |
| C7 | SHARPENED | Primary Frobenius gives the exact CM zeta; the Hodge metric is on the specified complex lift. |

All seven claims are saved; the proofs, numerical checks, and correction ledger are complete. Source locations are repository-relative, with one-based line numbers.

## 0. Binding conventions and scope — PROVED / SHARPENED

Author: `codex:gpt-6-astra`

We retain, without re-deriving the preceding round, `report/sections/04q_h_theta.tex:26–39`, `report/sections/04r_h_theta_channels.tex:77–105`, and `notes/h-theta/astra-proofs.md:11–18`. Put $X=\log y$. The bond is $H=L^2(\mathbb R,dX)$, and
\[
\widehat f(u)=\int_{\mathbb R}f(e^X)e^{iuX}\,dX,
\qquad f(e^X)=\int_{\mathbb R}\widehat f(u)e^{-iuX}\frac{du}{2\pi},
\qquad U_tf(e^X)=f(e^{X-t}).
\]
All Hermitian inner products are **linear in the first slot**. The outgoing space is $H_+=L^2(X>0)$, with Mellin image $H^2(\mathbb C_+)$. Set
\[
\Theta(u)=\frac{\xi(1+2iu)}{\xi(1-2iu)},\quad
K=H^2_+\ominus\Theta H^2_+,\quad
Z_t=P_KM_{e^{itu}}|_K,\quad C_t=Z_t^*.
\]
Thus $Z_t$ is the **forward compression**; the displayed damped modes in the brief belong to **$C_t$**. We do not rename $C_t$ as $Z_t$. For $\rho=\sigma+i\gamma$,
\[
w_\rho=\frac\gamma2+i\frac{1-\sigma}2,\quad
\lambda_\rho=-i\bar w_\rho=\frac{\bar\rho-1}{2},\quad
k_\rho(u)=\frac1{u-\bar w_\rho},\quad
m_\rho(X)=e^{\lambda_\rho X}1_{X>0},\quad
\widehat m_\rho=i k_\rho.
\]
On $K$ in the $X$-picture, $C_tf(X)=f(X+t)$, $X>0$. Write $e_{\rho,j}=X^jm_\rho/j!$, $0\le j<m_\rho^{\rm mult}$, reserving the superscript “mult” for the zero order. Then
\[
C_te_{\rho,j}=e^{t\lambda_\rho}\sum_{r=0}^j\frac{t^{j-r}}{(j-r)!}e_{\rho,r},
\quad De_{\rho,j}=\lambda_\rho e_{\rho,j}+e_{\rho,j-1},\quad e_{\rho,-1}=0.
\tag{0.1}
\]
The full jets are complete and minimal; ordinary modes alone are complete iff zeros are simple (`04r_h_theta_channels.tex:80–105`). A finite set below includes **full multiplicities**, is closed under both $\rho\mapsto1-\rho$ and $\rho\mapsto\bar\rho$, and $H^1_{\rm fin}$ means its complex jet span, equipped with real structure $\mathcal Rf(X)=\overline{f(X)}$. Its fixed real space is the real $H^1$ used for polarization.

The pure Blaschke property and Hermite–Biehler formula $E=\xi(1-2iu)$, $\Theta=E^\#/E$, are unconditional (`04q_h_theta.tex:82–105`). We also retain $g=y^{1/4}(\theta-1-y^{-1/2})$ and $\widehat g(u)=-\xi(1/2+2iu)/(u^2+1/16)$ (`04q_h_theta.tex:41–78`). The theta cyclic-and-cut identification was **refuted**, not established (`04q_h_theta.tex:110–129`). Consequently the present constructions are on the theta-derived **symbol model**, not a newly proved cohomology of the original bond.

The analytic counting input used below is the classical Riemann–von Mangoldt theorem: counting positive ordinates with multiplicity, $N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi e}+O(\log T)$. This external theorem is **not byte-cited as an original proof**; it is recorded, together with zero location and divisor symmetries, as analytic input in `report/sections/04b_phantasm_forced.tex:96–101`. No RH is included in this input.

Every assertion below carries a verdict at its section or paragraph. “PROVED” for a conditional assertion means its implication is proved, not its RH hypothesis. External named results explicitly described as **not byte-cited** are not represented as local-source quotations. Deninger arXiv:1001.1621 and math/0204110 are not local sources and are not used as byte-cited evidence.

## 1. C1: graded data — SHARPENED

### 1.1 Rates and the top class — PROVED

The even terms are formal/distributional classes, not vectors of the bond Hilbert space. Their pole labels $1\leftrightarrow s=0$, $y^{-1/2}\leftrightarrow s=1$ are fixed by `report/sections/04p_gl1_bond.tex:85–100`; the Mellin residues of the theta remainder are $-2,+2$ (`04q_h_theta.tex:69–76`). With the **forward** dilation,
\[
U_t1=1,\qquad U_ty^{-1/2}=e^{t/2}y^{-1/2}.
\]
The decaying convention requested in the brief is instead the action of $U_{-t}$ on these formal classes, consistent with the left translation $C_t$ on outgoing modes. In this convention set
\[
H^0=\mathbb R1,\quad H^2=\mathbb R\eta,\quad \eta=y^{-1/2},\quad
A_0(t)=1,\quad A_2(t)=q_t=e^{-t/2},\quad A_1(t)=C_t|_{H^1_{\rm fin}}.
\tag{1.1}
\]
The pole $s=1$ is the designated top class, with rate $-1/2$; the reference rates are $0,-1/2$, their midpoint is $-1/4$. Strictly speaking $q_t$ is the **ratio of exponentiated rates**, not the ratio of rates (one rate is zero). Compare `report/sections/02h_definitions_graded_ramanujan.tex:41–46,60–94`, which also distinguishes a spectral transfer from a supplied CP channel.

For $t>0$, (0.1) gives
\[
|e^{t\lambda_\rho}|=e^{-t(1-\sigma)/2}=\sqrt{q_t}=e^{-t/4}
\quad\Longleftrightarrow\quad\sigma=\tfrac12.
\tag{1.2}
\]
At $t=0$ this test says nothing. Multiplicity does not affect (1.2).

There is also a labeling distinction: $m_\rho(y)=y^{-r/2}1_{y>1}$ with $r=1-\bar\rho$, whereas the formal even monomial attached to pole $s$ is $y^{-s/2}$. The involution $\rho\mapsto1-\bar\rho$ preserves the zero divisor, so relabeling by $r$ gives one uniform rate rule $-s/2$; without that relabeling, extrapolating $\lambda_\rho=(\bar\rho-1)/2$ to $s=0,1$ interchanges the two pole labels. This does not affect the finite determinant, but is part of the comparison convention.

### 1.2 What is reproduced — SHARPENED

Given the nondegenerate alternating form constructed in C2, define $x\smile y=\Omega(x,y)\eta$, declare $1$ the unit, and set all products of degree $>2$ to zero. This is an associative graded-commutative real algebra, with trace $\tau(\eta)=1$, and $A_t$ is cup-compatible. It has the **algebraic shape** of Definition 6.1 (`notes/deninger-lps/src/manuscript.txt:644–647`). No face complex or geometric cup product on the GL₁ bond has thereby been produced.

For each finite real dimension $2g$, define
\[
\mathcal Z_t(u)=\frac{\det(1-uA_1(t))}{(1-u)(1-q_tu)}.
\]
Symplectic similitude gives
\[
\mathcal Z_t\!\left(\frac1{q_tu}\right)=q_t^{1-g}u^{2-2g}\mathcal Z_t(u).
\tag{1.3}
\]
Indeed $A^T$ is similar to $q_tA^{-1}$, and $\det A=q_t^g$; substitution in numerator and denominator proves (1.3). This is the finite note's proof (`manuscript.txt:710–718`) and works for every $q_t>0$. Its Theorem 6.2 is stated with $q>1$ (`:648–659`); here $0<q_t<1$. Under the metric criterion of C3 the numerator roots have modulus $q_t^{-1/2}$, distinct from both pole moduli for $t>0$. This is an elementary extension to contraction time, not a literal invocation of the theorem's expanding hypothesis. Reversing time gives the expanding finite algebra; negative time is not asserted to be a bounded operator on the full $K$.

## 2. C2: the functional-equation pairing — SHARPENED

### 2.1 Existence is a spectral statement, not a canonical cup product — PROVED

For ordinary eigenvectors, invariance for **every** $t\ge0$ says
\[
\big(e^{t(\lambda_\rho+\lambda_\nu)}-e^{-t/2}\big)\Omega(e_{\rho,0},e_{\nu,0})=0.
\]
A nonzero entry therefore requires $\lambda_\rho+\lambda_\nu=-1/2$, equivalently $\nu=1-\rho$. At a single time there are phase aliases; the all-time hypothesis is essential. For generalized eigenspaces the same conclusion follows by differentiating: the Sylvester equation has an invertible scalar-plus-nilpotent left side unless the eigenvalues sum to $-1/2$.

Thus a **nondegenerate** invariant bilinear form can exist only if partner root spaces have matching Jordan types. For this scalar model there is one block of size equal to each zero order. The functional equation and conjugation symmetry of $\xi$ supply exactly matching orders. Conversely the next formula constructs the form. Closure alone does not make an arbitrary invariant form nondegenerate: the zero form remains a counterexample.

There are no real zeros of $\xi$, in particular none at $1/2$ (`report/sections/04q_h_theta.tex:93–97`). For completeness, the elementary sign check is $\eta(s)=\sum_{n\ge1}(-1)^{n-1}n^{-s}>0$ for $0<s<1$, whereas $1-2^{1-s}<0$; hence $\zeta(s)<0$ and $\xi(s)>0$. No root is fixed by $\rho\mapsto1-\rho$.

### 2.2 A real alternating form including every jet — PROVED

Let $m=m_\rho^{\rm mult}=m_{1-\rho}^{\rm mult}$. On the normalized jets of (0.1) set
\[
\boxed{\quad
\Omega(e_{\rho,j},e_{\nu,k})=
\begin{cases}
(-i\,\operatorname{sgn}\gamma)^m(-1)^j,&\nu=1-\rho,\quad j+k=m-1,\\
0,&\text{otherwise}.
\end{cases}\quad}
\tag{2.1}
\]
This defines a complex bilinear form, the complexification of a real alternating form on the fixed space of $\mathcal R$.

1. **Alternation and reality.** Replacing $\rho$ by $1-\rho$ changes the leading coefficient by $(-1)^m$; exchanging $j,k$ changes $(-1)^j$ by $(-1)^{m-1}$. The total sign is $-1$. Conjugating $\rho$ conjugates the coefficient, so $\Omega(\mathcal Rx,\mathcal Ry)=\overline{\Omega(x,y)}$. For simple zeros this is $\Omega(e_\rho,e_{1-\rho})=-i\operatorname{sgn}\gamma$. The brief's coefficient $\operatorname{sgn}\gamma$ is alternating but **anti-real**, so is not the required real symplectic form.
2. **Nondegeneracy.** Each partner block is paired by an invertible anti-diagonal matrix; distinct blocks pair to zero. The direct sum is nondegenerate.
3. **Similitude.** Write $D=\lambda_\rho+N$ on a block. The anti-diagonal matrix $B$ obeys $N^TB+BN=0$: its two potentially nonzero entries have signs $(-1)^{j-1}$ and $(-1)^j$. Since $\lambda_\rho+\lambda_{1-\rho}=-1/2$,
\[
D^T\Omega+\Omega D=-\tfrac12\Omega,
\qquad \Omega(C_tx,C_ty)=e^{-t/2}\Omega(x,y).
\tag{2.2}
\]
Exponentiating the first identity proves the second, including all polynomial factors of the jets.

The absence of a fixed root is sufficient here, not a universal necessary condition for alternating pairings: an even-dimensional fixed eigenspace can itself be symplectic. Also, the functional equation guarantees the possible pairing pattern and matching block sizes, **not** the normalization in (2.1). Pairwise nonzero factors respecting reality give other forms.

### 2.3 Concrete bond formula and the limitation of Poisson inversion — PROVED / REFUTED

Here is an explicit realization on each finite jet span in the actual bond norm. List its jets as $e_1,\ldots,e_N$, form the positive Gram matrix $M_{ab}=\langle e_a,e_b\rangle_H$, and set
\[
b_a=\sum_l(M^{-1})_{al}e_l,\qquad c_a(f)=\langle f,b_a\rangle_H
=\int_0^\infty f(X)\overline{b_a(X)}\,dX.
\]
Then $c_a(e_l)=\delta_{la}$. With $B_{ab}$ given by (2.1),
\[
\Omega(f,h)=\sum_{a,b}B_{ab}c_a(f)c_b(h).
\tag{2.3}
\]
This is an explicit finite-rank integral formula on the bond, restricting to (2.1). The restrictions for nested finite root sets agree, so (2.3) defines the form on the algebraic union of all jets. Its extension to the whole energy completion is **not** asserted. Gram inversion depends on the selected spectral data; it is not a zero-free geometric construction.

Fix two different involutions. The unitary Poisson reflection on the **weighted** bond is $J_Pf(X)=f(-X)$, or $F(u)\mapsto F(-u)$. The involution exchanging the **unweighted formal** even terms is instead $P_{1/2}f(y)=y^{-1/2}f(1/y)$. This repairs the shorthand in `04p_gl1_bond.tex:97–100`: bare inversion sends $y^{-1/2}$ to $y^{1/2}$. The symmetric weighting $g$ converts the weighted functional equation into $J_Pg=g$ (`04q_h_theta.tex:53–63`). Burnol actually proves that his theta map intertwines adelic Fourier transform with inversion (`refs/src/math/0001013/main.tex:230–235`); this is not a claim that inversion preserves the outgoing cut.

Indeed $J_PK\subset H^2_-$, orthogonal to $K\subset H^2_+$. The naive bilinear form
\[
\langle f,\mathcal R J_Ph\rangle_H
=\int_{\mathbb R}f(X)h(-X)\,dX
\tag{2.4}
\]
is zero on $K\times K$. On $K\times J_PK$ it gives a nondegenerate duality, but does not by itself give an alternating $q_t$-similitude on two copies of the same outgoing model.

The natural transport between cuts is the following explicit Hankel operator:
\[
\mathsf H_\Theta=P_+M_\Theta J_P|_{H^2_+},\qquad
(\mathsf H_\Theta F)(u)=\Theta(u)F(-u)\quad(F\in K).
\tag{2.5}
\]
On $K$ it is a linear unitary involution. To verify this, the usual model conjugation $\mathcal C_\Theta F=\Theta\overline F$ maps $K$ antiunitarily onto itself: $F\perp\Theta H^2_+$ is precisely $\overline\Theta F\in H^2_-$; conjugation proves the assertion. The bond real structure is $\mathcal RF(u)=\overline{F(-u)}$, and $\Theta(-u)=\overline{\Theta(u)}$. Thus $\mathsf H_\Theta=\mathcal C_\Theta\mathcal R$, its square is $1$, and
\[
\mathsf H_\Theta C_t\mathsf H_\Theta=Z_t.
\tag{2.6}
\]
For completeness, set $\mathcal B(f,h)=\langle f,\mathcal C_\Theta h\rangle=\int f(u)h(u)\overline{\Theta(u)}\,du/(2\pi)$. Since $\mathcal C_\Theta h\in K$, the projection in $Z_t$ can be removed in this pairing; scalar multiplication then gives $\mathcal B(Z_tf,h)=\mathcal B(f,Z_th)$. Hence $\mathcal C_\Theta Z_t^*\mathcal C_\Theta=Z_t$; combining this with the real structure, which commutes with both semigroups, proves (2.6). For example $\mathcal C_\Theta k_w=\Theta(u)/(u-w)$ is a $Z_t$-eigenvector with factor $e^{itw}$. The transport is between a semigroup and its **adjoint**, not between $C_t$ and $q_tC_t^{-1}$. The latter would require the additional spectral pairing (2.1). Formula (2.3), together with (2.5), is the concrete realization justified here; a canonical Poisson-only alternating form on all of $K$ is **not obtained**. Transporting (2.3) by $\mathsf H_\Theta$ gives the analogous form on the forward root span.

## 3. C3: positive metrics and the finite polarization criterion — SHARPENED

### 3.1 Exact finite criterion — PROVED

On a finite **full jet span**, a positive Hermitian form $G$ satisfying
\[
G(C_tx,C_ty)=q_tG(x,y)\qquad(t\ge0)
\tag{3.1}
\]
exists iff all its zeros lie on $\Re s=1/2$ **and are simple**. On a span containing just ordinary eigenvectors and discarding the jets, simplicity is not necessary; that discards part of the stated model.

**Necessity.** A nonzero Hermitian entry between ordinary modes requires
\[
\lambda_\rho+\overline{\lambda_\nu}=-\tfrac12
\quad\Longleftrightarrow\quad\sigma+\sigma'=1,\quad\gamma=\gamma'.
\tag{3.2}
\]
Putting $\rho=\nu$ and using positivity forces $\sigma=1/2$. For a chain of length at least two, (0.1) gives $C_te_1=e^{t\lambda}(e_1+te_0)$. After division by $q_t$, its squared $G$-norm has leading coefficient $t^2G(e_0,e_0)>0$, contradicting its required constancy. **Sufficiency.** For simple critical zeros, choose any positive diagonal weights $g_\rho$; (3.1) follows term by term. Reality requires $g_\rho=g_{\bar\rho}$.

### 3.2 Transcription of Theorem 5.2 — PROVED, finite-dimensional only

Fix the real symplectic form (2.1). The following conditions are equivalent on the finite real space:

1. There is a real $J$, commuting with every $C_t$, with $J^2=-I$, $J^T\Omega J=\Omega$, and $G_J=\Omega J>0$.
2. There is a real positive symmetric certificate $G$ with $C_t^TGC_t=q_tG$ for every $t\ge0$.
3. $V_t=e^{t/4}C_t$, algebraically extended to $t\in\mathbb R$, is uniformly bounded.
4. $D+I/4$ is diagonalizable with purely imaginary spectrum (equivalently, the selected zeros are simple and critical).

For a fixed $t_0>0$, the four original single-operator conditions of Theorem 5.2 apply to $A=C_{t_0}$, $q=q_{t_0}$, and $U=q_{t_0}^{-1/2}A$. Their condition (iii) is **two-sided integer powers**, not just forward powers (`notes/deninger-lps/src/manuscript.txt:530–599`). Eigenphase aliases can enlarge the single-time metric cone, but do not change the existence criterion or eliminate any Jordan block.

Here are the steps needed for the all-time version. (1) implies (2) by cup compatibility and commutation. (2) implies (3) by equivalence of finite-dimensional norms. Bounded positive and negative time excludes eigenvalues with nonzero real part and excludes nontrivial nilpotents, proving (4). Diagonalizing proves (4) implies (3); alternatively a diagonal metric proves (4) implies (2). Given (2), in a **real basis** put
\[
L=G^{-1}\Omega,\quad R=(-L^2)^{1/2},\quad J=-LR^{-1}.
\tag{3.3}
\]
The operator $L$ is $G$-skew-adjoint and invertible, so $-L^2$ is positive and $R$ exists, commutes with $L$, and is invertible. Hence
\[
J^2=-I,\qquad \Omega J=GR>0,\qquad J^T\Omega J=\Omega.
\tag{3.4}
\]
Both similitude identities imply $LC_t=C_tL$, so $R,J$ also commute with $C_t$. This proves (1). Forward uniform boundedness alone also suffices **in this finite symplectic setting**: eigenvalues of $D+I/4$ occur in opposite pairs; forward boundedness therefore forces purely imaginary eigenvalues and no nilpotents. This is not a general assertion about arbitrary contraction semigroups.

### 3.3 The star and the distinction between certificates and compatible metrics — SHARPENED

For the simple critical modes with (2.1), the construction (3.3) gives
\[
Je_\rho=-i\operatorname{sgn}(\gamma)e_\rho,
\qquad G_J(e_\rho,e_\nu)=\delta_{\rho\nu},
\qquad V_t\text{ is }G\text{-unitary}.
\tag{3.5}
\]
Here $G_J(x,y)=\Omega(x,J\mathcal Ry)$ denotes the Hermitian extension; $\Omega(x,Jy)$ is its real bilinear version. For a positive ordinate put
\[
u=(e_++e_-)/\sqrt2,\qquad v=i(e_+-e_-)/\sqrt2.
\]
These are real vectors, $\Omega(u,v)=-1$, $Ju=-v$, $Jv=u$, and $G_J(u,u)=G_J(v,v)=1$. This verifies the sign in (3.5). A certificate $G=g_\gamma I_2$ on this plane gives $R=g_\gamma^{-1}I_2$, so $GR=I_2$. Thus the **certificate cone** has arbitrary positive weights, but for this fixed normalized $\Omega$ the invariant compatible star, and hence $\Omega J$, is fixed. Changing weights of a compatible metric requires changing the scale of $\Omega$ on the corresponding planes. The notation $G_J=\Omega J$ in Definition 5.1 is not a requirement that the matrix product of an arbitrary certificate $G$ with $J$ be positive.

The precise continuous scaling is $C_t=e^{-t/4}V_t=\sqrt{q_t}V_t$. The discrete elliptic channel's scale $q^{-1/4}$ uses a different variable (`report/sections/04l_elliptic_cavity_channel.tex:157–175`); inserting $q_t^{-1/4}$ here would be incorrect.

### 3.4 Which symmetries select a ray? — SHARPENED

In the fixed modal normalization, all **all-time** real invariant metric certificates have one scalar $g_\gamma>0$ per positive ordinate. The specified conjugation and functional-equation permutations preserve $|\gamma|$, and hence do not equate different weights. Any mode permutation commuting with the dynamics fixes each distinct frequency; one intertwining time reversal can only exchange opposite frequencies. Consequently those specified symmetries do not select a ray when there is more than one pair. This is the valid contrast with the parity/conjugation action on the four D2 modes (`04l_elliptic_cavity_channel.tex:160–164`).

The unrestricted sentence “no symmetry acts transitively” is **REFUTED**: the real diagonal commutant $e_{\pm\gamma}\mapsto a_\gamma e_{\pm\gamma}$, $a_\gamma>0$, acts transitively on positive diagonal certificates by congruence. This transitivity is on a finite space or the algebraic modal direct sum; the rescalings need not extend boundedly to $K$. It does not preserve the fixed $\Omega$. Conversely, if $\Omega$ itself is declared part of the normalized input, (3.5) already selects its compatible metric. Neither statement proves a geometrically canonical choice of that initial $\Omega$.

## 4. C4: the obstruction in the energy completion — PROVED, with a stronger semigroup conclusion

### 4.1 No equivalent invariant Hilbert metric — PROVED unconditionally

There is no bounded positive operator $G$ with a bounded inverse on $K$ such that
\[
C_t^*GC_t=e^{-t/2}G\quad\text{for all }t\ge0.
\tag{4.1}
\]
The same statement holds with $C_t$ replaced by the notebook's $Z_t$, by conjugation with the linear unitary involution $\mathsf H_\Theta$ in (2.6).

**Step 1: reduction.** A hypothetical $G$ restricts to every finite root span. C3 forces RH and simplicity. Otherwise this already contradicts an off-line mode or a jet. Hence it suffices to argue under RH and simplicity.

**Step 2: orthogonality.** Let $u_\gamma=k_\rho/\sqrt2$, so $\|u_\gamma\|_H=1$, since $\|k_{a+i/4}\|^2=2$ (binding normalization, `notes/h-theta/astra-proofs.md:997`). The similitude identity implies
\[
\langle u_\gamma,u_\delta\rangle_G
=e^{it(\delta-\gamma)/2}\langle u_\gamma,u_\delta\rangle_G.
\]
For $\gamma\ne\delta$, some $t>0$ has a nontrivial factor, so this inner product vanishes. No surjectivity or group theorem is needed.

**Step 3: equivalence implies a Riesz basis.** If $cI\le G\le CI$, then $c\le\|u_\gamma\|_G^2\le C$. For any finite coefficients,
\[
\frac cC\sum|a_\gamma|^2
\le\left\|\sum a_\gamma u_\gamma\right\|_H^2
\le\frac Cc\sum|a_\gamma|^2.
\tag{4.2}
\]
Completeness makes this a Riesz basis, contradicting `report/sections/04r_h_theta_channels.tex:94–105`. Equivalently, the close-pair overlap used below directly contradicts its lower bound. It would suffice to assume (4.1) on the dense algebraic root span: boundedness of $C_t,G$ then extends the identity to $K$.

**Meaning.** Any positive Hodge metric realizing these full mode dynamics is outside the bounded equivalence class of the energy metric. This is an obstruction to that **specified channel realization**, not a theorem excluding an unspecified cohomology in Deninger's programme. Under RH and simplicity the algebraic certificate cone is nonempty, but its intersection with the class of energy-equivalent Hilbert metrics is empty.

### 4.2 The rescaled semigroup is not uniformly bounded — PROVED unconditionally

In fact,
\[
\boxed{\quad\sup_{t\ge0}e^{t/4}\|C_t\|
=\sup_{t\ge0}e^{t/4}\|Z_t\|=\infty.\quad}
\tag{4.3}
\]
If RH fails, functional-equation symmetry supplies a zero with $\sigma>1/2$; its rescaled eigenvalue grows exponentially. If RH holds but there is a multiple zero, its normalized jet evolution has polynomial growth. It remains to treat RH with simple zeros.

By the zero-density argument already proved in `04r_h_theta_channels.tex:99–103` (detailed in `notes/h-theta/astra-proofs.md:745–774`), there are distinct ordinates with gaps tending to zero. Put $a=\gamma/2$, $a'=\delta/2$, and let
\[
r=|\langle u_\gamma,u_\delta\rangle_H|
=\frac{1/2}{\sqrt{(a-a')^2+1/4}}.
\]
Choose $|c|=1$ with $\langle u_\gamma,cu_\delta\rangle_H=r$, and $f=u_\gamma-cu_\delta$. Then $\|f\|^2=2(1-r)$. At the positive time $t_* =\pi/|a-a'|=2\pi/|\gamma-\delta|$, the two eigenphases differ by a minus sign, so
\[
\|e^{t_*/4}C_{t_*}\|
\ge\frac{\|u_\gamma+cu_\delta\|}{\|u_\gamma-cu_\delta\|}
=\sqrt{\frac{1+r}{1-r}}\longrightarrow\infty.
\tag{4.4}
\]
Thus the missing step suggested in the brief has an elementary two-mode proof. No assertion about the exact value of $\|Z_t\|$ at each fixed time is needed.

### 4.3 The correct general semigroup principle — PROVED

For clarity, a uniformly bounded strongly continuous semigroup on a Hilbert space with a **dense span of eigenvectors of purely imaginary generator eigenvalues** does admit an equivalent invariant Hilbert metric. Thus the brief's parenthetical doubt about this implication is also unnecessary in this setting.

Let its bound be $M$. For any finite sum of these eigenvectors, simultaneous recurrence of finitely many phases supplies arbitrarily large $t_n$ with $T_{t_n}f\to f$. (Partition a finite torus into small boxes and apply the pigeonhole principle to integer multiples of its phase vector.) For $s\ge0$,
\[
\|f\|=\lim_n\|T_{t_n-s}T_sf\|\le M\|T_sf\|.
\]
Density extends the lower bound to all $f$. Each $T_s$ has closed range, and its range contains all eigenvectors, hence is onto. Its inverses have norm at most $M$, giving a uniformly bounded group. The positive averages
\[
G_T=\frac1T\int_0^T T_t^*T_t\,dt
\]
obey $M^{-2}I\le G_T\le M^2I$. A weak-operator convergent subnet exists by weak compactness of bounded scalar matrix coefficients; the boundary intervals show $T_s^*G_TT_s-G_T\to0$ in norm for each fixed $s\ge0$. Its limit $G$ is positive, boundedly invertible, and invariant. Distinct eigenvalues become orthogonal, so any complete normalized simple eigenvector system is a Riesz basis. Dense unimodular eigenvectors **without uniform boundedness** do not have this consequence.

### 4.4 “Unbounded metric” needs qualification — SHARPENED

The theorem excludes **boundedly equivalent** metrics, not all bounded positive injective operators. Under RH and simplicity let $b_\rho$ be the global biorthogonal system to $e_\rho=m_\rho$. It is complete: it consists of nonzero scalar multiples of $\mathcal C_\Theta k_\rho$, whose completeness follows from that of the kernels (`04r_h_theta_channels.tex:97–99`). Choose positive conjugation-symmetric weights with
\[
\sum_\rho g_\rho\|b_\rho\|^2<\infty.
\]
Then $G(f,f)=\sum g_\rho|\langle f,b_\rho\rangle|^2$ is a bounded, positive, injective, compact form operator. Its restriction to the modal span is invariant, so boundedness extends the identity to all $K$. Its inverse is unbounded. This is a genuine bounded metric form, but an incomplete norm on the old underlying vector space and not equivalent to the energy norm. Its compatible cup normalization differs from (2.1).

For the particular **unit coefficient** norm, the coefficient operator $B_0(\sum a_\rho e_\rho)=(a_\rho)$ is densely defined and closable: convergence in $K$ forces convergence of each coordinate through its continuous biorthogonal functional. The close-pair argument makes $B_0$ unbounded. Its closure defines a densely defined closed positive quadratic form $\|\overline B_0 f\|_{\ell^2}^2$, represented by an unbounded positive self-adjoint operator. Approximating by finite modal sums and using closedness gives $\overline B_0 C_t f=\operatorname{diag}(e^{t\lambda_\rho})\overline B_0f$ on $\mathcal D(\overline B_0)$, so this form domain is $C_t$-invariant and its form satisfies the similitude identity there. This precise form statement, not an everywhere-defined matrix identity with an unbounded operator, is the appropriate meaning of the unit-weight Hodge metric relative to energy.

## 5. C5: Weil's form, spectral completions, and the failed identification — REFUTED as stated; corrected statements PROVED

### 5.1 Exact test-function form — PROVED using the stated Weil theorem

For $f\in C_c^\infty(\mathbb R)$ define
\[
F_f(s)=\int_{\mathbb R}f(t)e^{(s-1/2)t/2}\,dt,\qquad
\widetilde f(t)=\overline{f(-t)},\qquad h=f*\widetilde f.
\]
Then $F_h(s)=F_f(s)\overline{F_f(1-\bar s)}$, by changing variables in the convolution. This is precisely the half-time normalization in `report/sections/08c_weil_positivity_continuous.tex:109–121` and `notes/weil-positivity/astra-proofs.md:877–890`, and the pairing in `notes/weil-positivity.md:13–18,27–39`. Set
\[
W(f,g)=\sum_\rho m_\rho^{\rm mult}F_f(\rho)\overline{F_g(1-\bar\rho)},
\qquad W(f)=W(f,f)=\sum_\rho m_\rho^{\rm mult}F_h(\rho),
\tag{5.1}
\]
where in this display $\rho$ ranges over **distinct** zeros. All other sums written “with multiplicity” mean the same convention without the extra $m_\rho^{\rm mult}$. Integration by parts gives decay faster than every power of $|\gamma|$, uniformly in $0\le\sigma\le1$; $N(T)=O(T\log T)$ makes these sums absolutely convergent. Reindexing by $\rho\mapsto1-\bar\rho$ proves Hermitian symmetry.

**External theorem (Weil criterion; not byte-cited as an original source).** For the completed Riemann zeta function, (5.1) is nonnegative for every complex $f\in C_c^\infty(\mathbb R)$ iff every nontrivial zero has real part $1/2$. The change $x=e^{t/2}$ identifies this test class with smooth compactly supported multiplicative tests, with the corresponding half-density factor. The notebook states the criterion at `08c_weil_positivity_continuous.tex:128–138`; Meyer states the equivalent positive-definiteness criterion for the modified Weil distribution at `refs/src/math/0311468/main.tex:270–287`. We use that infinite converse, not finite-dimensional interpolation as a substitute.

Under RH, and without a simplicity assumption,
\[
W(f,g)=\sum_\rho m_\rho^{\rm mult}F_f(\rho)\overline{F_g(\rho)}.
\tag{5.2}
\]
It is a positive **semidefinite** form on tests; it is an inner product on the quotient by the kernel of evaluation and its completion. It is the ordinary counting norm of evaluations if zeros are counted with multiplicity, or the weight-$m_\rho^{\rm mult}$ norm on distinct zero coordinates. Off RH it is not the unit diagonal positive metric: it pairs distinct coordinates. On the full counting-coordinate space it is represented by the self-adjoint permutation involution $P:v_\rho\mapsto v_{1-\bar\rho}$, which has a negative direction for each nontrivial two-cycle.

The label `thm:kraus-weil-criterion` is actually in `report/sections/08b_weil_positivity.tex:159–170` and is finite and discrete. Its continuous finite counterparts are `08c_weil_positivity_continuous.tex:17–44`; neither proves the infinite Weil converse. This distinction is already stated in `notes/weil-positivity.md:107–112`.

### 5.2 Trace normalization; no metric is selected by a trace — SHARPENED

The exact completed explicit formula used here is the following standard theorem, **not byte-cited as an original proof**; its normalization is transcribed from `notes/weil-positivity/astra-proofs.md:879–890`. For the above $h$, writing $\psi=\Gamma'/\Gamma$,
\[
\begin{aligned}
\sum_\rho^{\rm mult}F_h(\rho)
={}&F_h(0)+F_h(1)-2\log(\pi)h(0)\\
&+\frac1{2\pi}\int_{\mathbb R}F_h(1/2+ir)\Re\psi(1/4+ir/2)\,dr\\
&-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\big[h(2\log n)+h(-2\log n)\big].
\end{aligned}
\tag{5.3}
\]
Here $\Lambda(n)$ is von Mangoldt, not the completed zeta. The prime sum is finite for compactly supported $h$. The factors $2$ come from the notebook time $t=2\log x$. This identity follows from the standard explicit formula by that substitution; it also holds for the Gaussian test used below by its absolutely convergent extension. With $\widehat h(u)=F_h(1/2+2iu)$, the gamma term is $\pi^{-1}\int\widehat h(u)\Re\psi(1/4+iu)\,du$.

Testing the centered decaying-time even action directly assigns $F_h(1)$ to $H^0$ and $F_h(0)$ to $H^2$; reversing centered time assigns them according to their theta pole labels. Their sum is unchanged. On the odd divisor, functional-equation and conjugation reindexing likewise leave the tested trace unchanged. Thus the centered **supertrace** (even poles minus odd zeros) is
\[
F_h(0)+F_h(1)-\sum_\rho^{\rm mult}F_h(\rho)
=2\log(\pi)h(0)-\mathcal A_\Gamma(h)
+2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}[h(2\log n)+h(-2\log n)].
\tag{5.4}
\]
It includes the archimedean/contact terms. “Supertrace equals a sum over primes” omitting these terms is false. The ordinary operators at a fixed $t>0$ are not trace class: their infinitely many eigenvalues have modulus at least $e^{-t/2}$. These are **tested distributional** traces. On the abstract diagonal model, the operator with entries $F_h(\rho)$ is trace class by the preceding decay estimate; its trace is the zero sum. Integrating the normalized $C_t$ group in the diagonal realization instead gives entries $F_h(\bar\rho)$; conjugation reindexes the same zero sum.

A trace is independent of a positive diagonal modal metric. For any positive weights $g_\rho$, the rescaled vectors $e_\rho/\sqrt{g_\rho}$ give the very same diagonal entries $F_h(\rho)$. All these metrics produce (5.3). Therefore the explicit formula cannot select all weights $1$. Once the evaluation map itself is fixed, Weil's form specifies its counting measure and hence gives a natural unit-weight **coordinate** form under RH; rescaling that comparison changes the modal weights. This is extra normalization data, not a uniqueness theorem for invariant metrics.

The theta Mellin transform has residues $-2,+2$ at $0,1$; dividing it by $2$ gives the classical completed zeta with residues $-1,+1$ (`04p_gl1_bond.tex:94–99`, `04q_h_theta.tex:74`). Pole **orders**, not those residues, yield coefficient $1$ for each even trace term in (5.3). One may set $\tau(\eta)=1$ as in C1, but no theorem identifies this chosen cup trace with a uniquely forced residue normalization of a geometric $H^2$.

### 5.3 Three spectral spaces that must not be conflated — PROVED / REFUTED

1. **Full model jets.** The algebraic $K$-root representation has a positive all-time invariant metric iff RH **and simplicity** (C3 applied to every finite block). Under those hypotheses completing its modal coefficient norm gives an abstract $\ell^2$ representation with $G=I$, (2.1), and the star (3.5). Its comparison with the energy model is unbounded (C4). If there is a multiple zero, no completion retaining that nontrivial Jordan block has the stated positive similitude.
2. **Diagonal semisimplification.** Define independently $\mathcal H_{\rm diag}=\ell^2\{(\rho,j):1\le j\le m_\rho^{\rm mult}\}$, with $T_te_{\rho,j}=e^{t\lambda_\rho}e_{\rho,j}$ and the conjugate-copy real structure. Then $G=I$ is an invariant $q_t$-metric iff RH, regardless of multiplicity. Pair each copy with its $1-\rho$ copy using $-i\operatorname{sgn}\gamma$, and use the star (3.5). These are bounded symplectic/polarization operators on this chosen spectral Hilbert space under RH. Together with the formal even spaces and $\tau(\eta)=1$ of C1, this is the precise **RH-only algebraic package**, but it has replaced every jet block by a scalar multiplicity space. Its diagonal generator is closed on $\mathcal D(D)=\{v:\sum_{\rho,j}|\lambda_\rho|^2|v_{\rho,j}|^2<\infty\}$. Under RH, $D=-I/4+iH$ with self-adjoint $H=\operatorname{diag}(-\gamma/2)$ on its maximal diagonal domain, so $e^{t/4}T_t$ is a strongly continuous unitary group. The identities are therefore proved directly in this specified infinite completion, not by transferring finite-dimensional norm equivalence. A fixed-time Hilbert determinant for the zeta function is still not supplied; (5.3) is its tested trace statement.
3. **Weil test quotient.** If a zero has order $m>1$, the map $f\mapsto(F_f(\rho))_{(\rho,j)}$ repeats the same value on all $m$ copies. Its image is not dense in those multiplicity directions and detects no derivatives. This cannot identify the full model jets with the diagonal multiplicity space. The distinction is exactly the trace's blindness to Jordan blocks (`notes/deninger-lps/src/manuscript.txt:733–758`; `08c_weil_positivity_continuous.tex:89–105`).

Nor are these arbitrary $\ell^2$ choices already Connes's or Meyer's Hilbert realization. Connes's weighted representation is explicitly nonunitary (`refs/src/math/9811068/main.tex:755–765`); its Theorem 1 detects only critical zeros, with multiplicity the largest integer $n<(1+\delta)/2$ not exceeding the zero order (`:873–885`). At weight zero the theta map is onto the bond (`:2549–2556`), giving no such cokernel. Meyer gives a virtual representation with poles even and zeros odd (`refs/src/math/0311468/main.tex:208–227,425–458`), proves its distributional character equals the explicit formula (`:249–269`), and works on a nuclear bornological space while explicitly noting the obstruction from off-line or multiple zeros (`:298–316`). His construction does not assert the unit diagonal Hilbert structure requested in the brief.

### 5.4 The kernel-analysis comparison is only densely defined — SHARPENED

Assume RH and simplicity. The map actually proposed in the brief is
\[
\mathcal A f=(\langle f,k_\rho\rangle_H)_\rho,
\qquad
\mathcal D(\mathcal A)=\{f\in K:\sum_\rho|\langle f,k_\rho\rangle|^2<\infty\}.
\tag{5.5}
\]
It is **not** an everywhere-defined map $K\to\ell^2$, and it is different from the coefficient map $B_0$ in C4.

To check every domain claim:

* The global biorthogonal vectors $b_\rho^k$, satisfying $\langle b_\rho^k,k_\nu\rangle=\delta_{\rho\nu}$, belong to $\mathcal D(\mathcal A)$. They are complete, by model conjugation as in C4. Hence the domain is dense and the range contains all finite sequences, so is dense.
* Each coordinate functional is continuous on $K$. Therefore convergence in $K\times\ell^2$ preserves all the coordinates: $\mathcal A$ is closed. Completeness of the kernels makes it injective.
* The kernels are **not Bessel**. Zero density $N(T)\asymp T\log T$ forces arbitrarily many ordinates $a=\gamma/2$ in intervals of fixed length $1$. Taking a unit kernel centered at any member of such a cluster, its squared overlaps with the other normalized kernels in the cluster are at least $1/5$. Thus no upper analysis bound is possible. If the closed operator (5.5) had domain all of $K$, the closed graph theorem would give such a bound. Its domain is proper and the operator is unbounded.
* Its inverse on its range is unbounded too. For unit kernels $u,v$ with overlap modulus $r\to1$, the biorthogonal vector $b_u\perp v$, $\langle b_u,u\rangle=1$, has norm at least $(1-r^2)^{-1/2}$. Yet its analysis vector is one coordinate vector (up to the fixed normalization $\sqrt2$).

Finally $\mathcal A Z_t f=(e^{itw_\rho}(\mathcal Af)_\rho)_\rho$ on its domain: use $\langle Z_tf,k_\rho\rangle=\langle f,C_tk_\rho\rangle$ and linearity in the first slot. This is an evaluation transform for the **forward** compression with conjugate mode factors, not the coefficient transform for $C_t$. Under RH it preserves the domain. Ordinary evaluations lose injectivity if one omits necessary jets at multiple zeros.

### 5.5 Interpretation for Deninger's programme — OPEN observation

A zero-independent positive construction realizing the right pairing, comparison, and full dynamics would be substantive. Merely declaring the zeros orthonormal supplies a conditional spectral Hilbert space and repackages RH; it supplies neither a geometric cup product nor simplicity for the jet realization. Weil's explicit formula already gives an arithmetic expression for the test form, but positivity of that expression is the unresolved part. The finite conformal torus has an independently positive flat Hodge metric; any analogous surface/Petersson construction would have to prove its comparison with the arithmetic form. The metric is **not forced by the trace or the listed symmetries alone**. Deninger's own conjectural cup/star formalism uses an antilinear Hodge star: in our real notation it would be $J\mathcal R$, not $J$ alone ([Deninger, 1001.1621, pp. 3–4](https://arxiv.org/pdf/1001.1621), external, **not byte-cited**). No identification of his hypothetical cohomology with this nonnormal model is claimed.

## 6. C6: what could replace faces — REFUTED literally; OPEN as a geometric programme

**PROVED obstruction.** For distinct primes $p,r$, the translations $U_{\log p}$, $U_{\log r}$ commute. In $X=\log y$, their orbit subgroup is $\mathbb Z\log p+\mathbb Z\log r$. Its ratio is irrational, since $p^m=r^n$ forces $m=n=0$; the subgroup is dense. Thus $\mathbb R/(\mathbb Z\log p+\mathbb Z\log r)$ is non-Hausdorff and is **not a solenoid**. If one instead means principal rational ideles, their action on the idele **class** group is already trivial. Neither interpretation establishes the proposed object. Prime scaling in the idele variable $x=\sqrt y$ corresponds to time $2\log p$, not $\log p$, in our $y$-convention.

**SHARPENED possible replacement.** A genuine compact $S$-adic solenoid is the Pontryagin dual of $\mathbb Z[1/(pr)]$, equivalently
\[
\Sigma_{p,r}=(\mathbb R\times\mathbb Q_p\times\mathbb Q_r)/\mathbb Z[1/(pr)].
\]
Multiplication by $p,r$ gives commuting automorphisms. One may use its action groupoid or a suspension $(\Sigma_{p,r}\times\mathbb R^2)/\mathbb Z^2$, with the group acting by those automorphisms and by integer translations in the second factor. This is new data, not the preceding dense quotient. Deninger's laminated spaces are locally Euclidean times totally disconnected spaces; his classical example is an inverse-limit solenoid, not that non-Hausdorff quotient ([Deninger, math/0204110, §5.1](https://arxiv.org/pdf/math/0204110), external, **not byte-cited**).

**OPEN ideation.** With a specified function module $M$, the two commuting transports $P,Q$ have the square/Koszul complex
\[
M\xrightarrow{d_0}M\oplus M\xrightarrow{d_1}M,
\quad d_0f=((P-I)f,(Q-I)f),\quad
 d_1(g,h)=(Q-I)g-(P-I)h,
\quad d_1d_0=0.
\]
Its first cohomology is a possible meaning of horizontal cohomology; the second direction acts as transverse transport. Leafwise de Rham cohomology on a chosen suspension is another, requiring a topology and a closed-range/reduced-cohomology convention. Bass doubling would mean an **added** two-copy companion transfer after specifying a suitable adjacency/operator; it does not manufacture a native cup pairing. The finite warning is exact: for symmetric $T$, the companion $\left(\begin{smallmatrix}T&-qI\\I&0\end{smallmatrix}\right)$ has positive polarization iff $\|T\|<2\sqrt q$, while its critical-circle divisor allows equality, with a Jordan obstruction at equality (`notes/deninger-lps/src/manuscript.txt:1188–1254`).

**REFUTED claimed zeta identification.** Commutation alone supplies neither a Lefschetz trace nor the two reference rates. The partial Euler product $(1-p^{-s})^{-1}(1-r^{-s})^{-1}$ has no numerator zeros at all; it is not the full theta pole/zero package. Two isolated primitive periodic orbits with these lengths would formally give that product, but no such orbit description has been proved for the solenoid action. Its coefficient modules are already infinite-dimensional, and any leafwise trace needs further analytic work. The proposed cohomology, metric, and determinant comparison remain **OPEN**; no two-prime RH theorem follows.

## 7. C7: the CM torus and the genus-one class-group bond — SHARPENED

### 7.1 The exact torus calculation — PROVED

Let $\alpha=a+bi\in\mathbb Z[i]$, $q=|\alpha|^2>1$, and $f_\alpha(z)=\alpha z$ on $T=\mathbb C/\mathbb Z[i]$. On coordinates its real matrix is $A=\left(\begin{smallmatrix}a&-b\\b&a\end{smallmatrix}\right)$; on coefficient columns of $dx,dy$, its pullback is $A^T$. The finite note uses the transpose coordinate map so that its cohomology matrix is $A$ (`notes/deninger-lps/src/manuscript.txt:765–785,812–819`); either convention gives the same eigenvalue pair and zeta.

Orient the unit square by $dx\wedge dy$ and use the flat metric. The cup form, Hodge star, and metric on real one-forms are
\[
\Omega_T=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
J_T=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
G_T=\Omega_TJ_T=I_2.
\tag{7.1}
\]
Both $A$ and $A^T$ preserve $\Omega_T,G_T$ up to $q$; both commute with $J_T$. Thus positivity is supplied by the actual torus geometry.

For every $n\ge1$, the kernel of $f_\alpha^n-I$ has
\[
\#\operatorname{Fix}(f_\alpha^n)=|\alpha^n-1|^2
=1+q^n-\alpha^n-\bar\alpha^n
\]
points: the lattice map has determinant $\det(A^n-I)=|\alpha^n-1|^2>0$. Exponentiating its fixed-point series gives, as a formal power series or near $u=0$,
\[
Z_{f_\alpha}(u)=\exp\sum_{n\ge1}\frac{\#\operatorname{Fix}(f_\alpha^n)}n u^n
=\frac{(1-\alpha u)(1-\bar\alpha u)}{(1-u)(1-qu)}.
\tag{7.2}
\]
This proves the finite note's formula (`manuscript.txt:788–820`) without an eigenvalue bound as an input. Arbitrary integers $a,b$ need not give a finite-field cardinality $q$; no assertion about an elliptic curve over $\mathbb F_q$ is made for every norm, e.g. $q=10$.

### 7.2 Which Gaussian associate is Frobenius? — PROVED using CM reduction

Let now $q=p\equiv1\pmod4$ be a rational prime and $E/\mathbb F_p:y^2=x^3-x$. The exact choice is
\[
\boxed{\quad \pi=a+bi,\quad \pi\bar\pi=p,\quad
\pi\equiv1\pmod{(1+i)^3}.
\quad}
\tag{7.3}
\]
Equivalently $a$ is odd, $b$ is even, and $a+b\equiv1\pmod4$. For each prime ideal above $p$ this selects exactly one of its four associate generators; the other prime gives $\bar\pi$. A choice of reduction of $i$ distinguishes the two roots, but the zeta does not. In particular the real part is generally **not positive**.

**External CM input (Deuring's ordinary CM reduction theorem, precise specialization; not byte-cited).** The good reduction of the characteristic-zero CM curve $y^2=x^3-x$ at a split prime $p\equiv1\pmod4$ is ordinary, its endomorphism ring over the algebraic closure is $\mathbb Z[i]$, and its $p$-power Frobenius endomorphism is an element $\pi\in\mathbb Z[i]$ of norm $p$. The pullback of this Frobenius endomorphism on $H^1_{\mathrm{et}}$ has characteristic polynomial $\chi(T)=T^2-(\pi+\bar\pi)T+p$; the zeta numerator is $P(u)=u^2\chi(1/u)=1-(\pi+\bar\pi)u+pu^2$. A primary-source formulation of the point-count normalization is Jeong–Kim–Kim, §2.1 and Lemma 3.1 / Proposition 3.2 ([arXiv:2001.06321](https://arxiv.org/pdf/2001.06321)); external, **not byte-cited**.

The remaining **associate normalization** can also be checked directly, avoiding an unexplained sign convention. For the endomorphism $[i](x,y)=(-x,iy)$, the kernel of $[1+i]$ is $\{O,(0,0)\}$. The eight points
\[
O,\ (0,0),\ (1,0),\ (-1,0),\quad
(i,\pm(1-i)),\ (-i,\pm(1+i))
\]
are $\ker[(1+i)^3]$. Indeed the duplication formula gives $x(2P)=(x(P)^2+1)^2/[4x(P)(x(P)^2-1)]$, so the last four points double to $(0,0)$; all eight lie in this kernel, which has degree $8$. They are rational over $\mathbb F_p$ after choosing $i\in\mathbb F_p$, and are distinct for odd $p$. Frobenius fixes this separable kernel, so $\pi-1$ factors through $[(1+i)^3]$; since the endomorphism ring is $\mathbb Z[i]$, (7.3) follows. Unique factorization and the four distinct unit residues modulo $(1+i)^3$ give uniqueness of the associate. This proves the normalization needed in (7.2).

Other unit associates are Frobenius roots of appropriate **quartic twists** $E_d:y^2=x^3-dx$. To see existence without a quartic-symbol sign ambiguity, choose $v^4=d$ and conjugate Frobenius by the isomorphism $(x,y)\mapsto(v^2x,v^3y)$. Its extra automorphism runs through all four units as $d$ runs through $\mathbb F_p^\times/(\mathbb F_p^\times)^4$, because $v^{p-1}=d^{(p-1)/4}$ does. Thus an arbitrary associate is allowed only after specifying the corresponding twist; it is not automatically the Frobenius of the fixed equation $E_1$.

### 7.3 The exact class-group conclusion and its scope — PROVED / SHARPENED

Taking $\alpha=\pi$ in (7.2) gives the Hasse–Weil zeta of $E$, and
\[
h=|\operatorname{Pic}^0(E)(\mathbb F_p)|=\#E(\mathbb F_p)
=P(1)=|\pi-1|^2=(a-1)^2+b^2.
\tag{7.4}
\]
The first equality uses the origin to identify $E\cong\operatorname{Pic}^0(E)$; the second also follows directly from the separable isogeny $\pi-I$, whose degree is its norm. The genus-one class-group bond is therefore exactly the one in `report/sections/04p_gl1_bond.tex:27–47`: its effective-divisor generating function is (7.2), with degree-$n\ge1$ counts $h(p^n-1)/(p-1)$. This is a proved equality of zeta functions and their graded cohomological data. It is **not an identification of underlying bond spaces**: that bond is $\ell^2(\operatorname{Pic}^0(E)(\mathbb F_p))\otimes\ell^2(\mathbb Z)$, whereas $H^1(T,\mathbb R)$ is two-dimensional. Also $h$ is not the ideal class number of $\mathbb Z[i]$, which is $1$. “CM class-group bond” must retain this distinction.

### 7.4 Flat Hodge metric and the D2 comparison — SHARPENED

On the complex lift $E(\mathbb C)\cong\mathbb C/(c\mathbb Z[i])$, pullback along a homothety identifies the conformal Hodge star on one-forms with (7.1). In the eigenbasis $\omega_+=dz/\sqrt2$, $\omega_-=d\bar z/\sqrt2$ for the unit-square normalization,
\[
f_\alpha^*\omega_+=\alpha\omega_+,\quad
f_\alpha^*\omega_-=\bar\alpha\omega_-,\quad
J_T\omega_+=-i\omega_+,\quad J_T\omega_-=i\omega_-,\quad
\Omega_T(\omega_+,\omega_-)=-i,\quad G_T=\operatorname{diag}(1,1).
\tag{7.5}
\]
The Hermitian metric here is the extension $\Omega_T(x,J_T\bar y)$, exactly as in (3.5). For $b\ne0$, the two eigenvalues are distinct. The off-diagonal entry of an invariant Hermitian metric vanishes since its multiplier is $\alpha^2\ne p$; reality makes the two diagonal weights equal. Thus the invariant real **certificate cone** is one ray, and the flat Hodge metric belongs to that ray. Fixing the cup normalization selects its compatible scale. If $b=0$ in the general torus family, the dynamics is scalar and this uniqueness-of-ray assertion fails; split primes in (7.3) have $b\ne0$.

There is no intrinsic real Hodge metric on an unspecified $H^1_{\mathrm{et}}(E/\mathbb F_p)$. The assertion just proved is on the chosen complex CM lift and its real Betti cohomology; comparison with the finite-field Frobenius polynomial is supplied by CM reduction. Deninger himself discusses this lifted ordinary-elliptic torus/solenoid example and its conformal metric ([math/0204110, pp. 28–29](https://arxiv.org/pdf/math/0204110), external, **not byte-cited**). An arbitrary identification of complexified étale eigenlines does not canonically transport a real metric.

The notebook's **D2** is $y^2+y=x^3+x+1$ over $\mathbb F_2$, not $y^2=x^3-x$ (`report/sections/04k_elliptic_cavity_scattering.tex:35–40`). It has numerator $1-2u+2u^2$, roots $1\pm i$ (`04p_gl1_bond.tex:42–46`). The naive characteristic-two equation $y^2=x^3-x$ is singular at $(1,0)$. D2's four channel modes are a bipartite/inverse-Frobenius realization, whose parity and reality select a ray (`04l_elliptic_cavity_channel.tex:145–175`), not the two Betti eigenlines themselves. With a specified comparison and normalized conjugate vectors, both symmetry conditions lead to equal weights, but this is the single-pair, genus-one test already declared vacuous in `04p_gl1_bond.tex:112–121`. The torus **does** independently supply a positive cup-compatible flat metric; equality with the unique symmetric ray supplies no further spectral theorem or new arithmetic metric selection principle.

## 8. Numerical checks for the blind lane — PROVED identities; numerical evaluations only

Author: `codex:gpt-6-astra`

Reproduce with `python3 notes/deninger-bond/checks/check_identities.py`. The script reads only `data/zeros3000.npy` and uses 50-digit mpmath for analytic quantities; the stored 3000 positive ordinates are float64, ending at $3533.3282433958198$. It also computes the first three zeros independently with `mpmath.zetazero`. All reported decimals are rounded. These are finite consistency checks, not proofs of RH or simplicity of all zeros.

### 8.1 Six modes at $t=1$

For $\rho_n=1/2+i\gamma_n$, $d_n=e^{-1/4-i\gamma_n/2}$:

| $n$ | $\gamma_n$ | $d_n$ |
|---|---:|---|
| 1 | 14.13472514173469379046 | $0.551367248054149711-0.550022560888030452i$ |
| 2 | 21.02203963877155499263 | $-0.362776434403421347+0.689147239967028782i$ |
| 3 | 25.01085758014568876321 | $0.777355034172435742+0.047432167981283365i$ |

In the ordered **physical** basis $(m_{+\gamma_1},m_{-\gamma_1},m_{+\gamma_2},m_{-\gamma_2},m_{+\gamma_3},m_{-\gamma_3})$, take
\[
D=\operatorname{diag}(d_1,\bar d_1,d_2,\bar d_2,d_3,\bar d_3),\quad
\Omega=\begin{pmatrix}
0&-i&0&0&0&0\\i&0&0&0&0&0\\
0&0&0&-i&0&0\\0&0&i&0&0&0\\
0&0&0&0&0&-i\\0&0&0&0&i&0
\end{pmatrix},\quad G=I_6,
\]
\[
J=\operatorname{diag}(-i,i,-i,i,-i,i),\qquad
R_c=\operatorname{diag}\left(
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\begin{pmatrix}0&1\\1&0\end{pmatrix}\right).
\]
Here $\mathcal R x=R_c\bar x$. The exact checks are
\[
D^T\Omega D=e^{-1/2}\Omega,\quad
D^TG\bar D=e^{-1/2}G,\quad
\Omega JR_c=I_6,\quad
|d_n|=e^{-1/4}\approx0.778800783071404868,\quad e^{-1/2}\approx0.606530659712633424.
\tag{8.1}
\]
The first-slot-linear Hermitian matrix convention is $G(x,y)=x^TG\bar y$. Maximum entry errors in double precision were $2.61\times10^{-17}$, $1.14\times10^{-16}$, and zero, respectively. For the actual energy metric instead, if the signed ordinates are $s_a$,
\[
M_{ab}=\langle m_{s_a},m_{s_b}\rangle_H
=\frac{2}{1+i(s_a-s_b)};
\tag{8.2}
\]
its off-diagonal entries do not satisfy (8.1). Replacing $m_\rho$ by $k_\rho=-i\widehat m_\rho$ also changes the coordinate matrix of the **bilinear** form by the square of that scalar; one must not silently mix these bases. The script tests the anti-diagonal pairing of jets of lengths $1,2,3,4$ at a synthetic off-line partner pair; maximum residual $3.70\times10^{-16}$. This checks the polynomial rule and does not posit actual off-line zeros.

### 8.2 Weil form against 3000 positive zeros and their conjugates

Use the Gaussian, an admissible rapidly decreasing extension of the compact test class,
\[
a=\tfrac1{50},\quad f(t)=(4\pi a)^{-1/2}e^{-t^2/(4a)},\quad
F_f(s)=e^{a(s-1/2)^2/4},\quad
h(t)=(8\pi a)^{-1/2}e^{-t^2/(8a)}.
\]
Direct completion of the square proves these transforms. At the supplied critical zeros,
\[
W_{3000}(f)=2\sum_{n=1}^{3000}e^{-a\gamma_n^2/2}
\approx0.2993960225075590798332207898.
\tag{8.3}
\]
The factor $2$ includes negative ordinates; “3000 zeros” in the data means 3000 **positive** ordinates. Formula (5.3) gives the following independent analytic-side values:

| Contribution | Value |
|---|---:|
| $F_h(0)+F_h(1)=2e^{a/8}$ | 2.0050062552115901699492440148 |
| $-2\log\pi\,h(0)$ | −3.2292233878602183844073696831 |
| gamma integral | 1.5236299541478742837918519217 |
| prime powers $n\le1000$ | −0.0000167989916869135445623098 |
| total | 0.2993960225075591557891639435 |

The difference is $-7.60\times10^{-17}$, consistent with the float64 zero data. A decreasing-integrand bound for the omitted prime powers is
\[
4h(0)\int_{1000}^{\infty}\frac{\log x}{\sqrt x}
 e^{-(\log x)^2/(2a)}\,dx<3.0\times10^{-518}.
\]
This bound uses $\Lambda(n)\le\log n$ and bounds all integers, so it does not need a prime-density estimate. For a directly verifiable tail estimate, let $L=\log1000$, $\kappa=L/a-1/2>0$; the integral including its prefactor is at most $4h(0)e^{L/2-L^2/(2a)}(a+a/(2\kappa))<2.962\times10^{-518}$. This follows by integrating $u e^{u/2-u^2/(2a)}=-a(d/du)e^{u/2-u^2/(2a)}+(a/2)e^{u/2-u^2/(2a)}$ and bounding the last exponential by its tangent exponential for $u\ge L$. The zero tail is absolutely convergent, even without RH: for $0<\sigma<1$, $|F_h(\sigma+i\gamma)|\le e^{a/8}e^{-a\gamma^2/2}$, and $N(T)=O(T\log T)$ bounds its tail by $O(T\log T\,e^{-aT^2/2})$. The displayed decimal is a computation from the listed zeros, not a new certified global zero census or a certified high-precision bound on its data errors.

### 8.3 CM point counts

Enumerate all affine pairs and add the point at infinity. For the fixed equation $E:y^2=x^3-x$, the primary associates with positive imaginary part and the resulting zeta numerators are:

| $p$ | primary $\pi$ | trace $2a$ | $P(u)$ | $\#E(\mathbb F_p)=P(1)=\lvert \pi-1\rvert^2$ |
|---|---|---:|---|---:|
| 5 | $-1+2i$ | −2 | $1+2u+5u^2$ | 8 |
| 13 | $3+2i$ | 6 | $1-6u+13u^2$ | 8 |
| 17 | $1+4i$ | 2 | $1-2u+17u^2$ | 16 |

In every row $Z_E(u)=P(u)/((1-u)(1-pu))$. The script checks the counts by exhaustive enumeration, the primary congruence, and $A^TA=pI$, $A^T\Omega_TA=p\Omega_T$ exactly as integer matrices. Every assertion in the script passed. In particular choosing $1+2i$ at $p=5$ would describe a twist, not this equation.

## 9. Corrections to the brief

All entries below are **PROVED corrections** to the stated claims, except the geometric tasks explicitly marked OPEN.

| Item | Correction |
|---|---|
| C1 / time | $U_t f(y)=f(e^{-t}y)$ gives even rates $0,+1/2$. Decaying rates $0,-1/2$ use reverse dilation and $C_t=Z_t^*$. |
| C1 / modes | The damped outgoing kernels and jets are modes of $C_t$, not $Z_t$. Forward modes are obtained by model conjugation/Hankel transport. |
| C1 / constants | Neither formal even class belongs to the unweighted full bond Hilbert space. They are added graded classes, not two more eigenvectors of $K$. |
| C1 / labels | The kernel label has rate $-(1-\bar\rho)/2$; relabel by $1-\bar\rho$ before comparing with the even monomial rule $-s/2$. |
| C1 / rates | $q_t$ is a ratio of exponentials of reference rates, not a ratio of the rates themselves. |
| C1 / finite theorem | The finite note states $q>1$; contraction time has $q_t<1$. Its algebraic determinant proof extends, but the original hypothesis is not literally satisfied. |
| C1 / geometry | Specifying $x\smile y=\Omega(x,y)\eta$ constructs a graded algebra. It does not establish a geometric cohomology or restore the refuted theta cyclic-and-cut conjecture. |
| C2 / existence | FE closure with matching Jordan types permits a nondegenerate form; it does not make every invariant form nondegenerate. |
| C2 / reality | Use $-i\operatorname{sgn}\gamma$ on simple physical modes. The proposed real sign coefficient is anti-real. |
| C2 / jets | Pair anti-diagonals with alternating signs as in (2.1); pairing only the two eigenvectors is degenerate for multiple zeros. |
| C2 / fixed roots | No actual root is fixed by $\rho\mapsto1-\rho$. Abstractly a fixed even-dimensional root space can still support an alternating form. |
| C2 / Poisson | Unweighted constant terms are exchanged by $y^{-1/2}f(1/y)$. Unit reflection belongs to the weighted bond and changes the cut. |
| C2 / Hankel | $M_\Theta J_P$ intertwines the adjoint and forward compressions, not the conformal inverse. A geometric, canonical cup pairing remains OPEN. |
| C3 / simplicity | Simplicity is necessary for the full jet model, not for a semisimple representation with repeated scalar eigenvalues. |
| C3 / compatibility | The invariant certificate $G$ and the compatible metric $G_J=\Omega J=GR$ need not coincide. For fixed (2.1), the simple critical star fixes $G_J$. |
| C3 / normalization | Continuous channel scale is $q_t^{1/2}=e^{-t/4}$. Do not substitute the discrete cavity's $q^{-1/4}$ using the same $q_t$. |
| C3 / symmetries | The specified mode permutations do not link different positive ordinates; arbitrary diagonal commuting rescalings do act transitively on the certificate cone. |
| C4 / boundedness | No bounded **and boundedly invertible** metric exists. Bounded injective noncoercive invariant forms can exist; unit modal weights give an unbounded closed form. |
| C4 / semigroup | Uniform boundedness is decisively false, even with RH and simplicity, by the two-close-kernel estimate (4.4). |
| C4 / general principle | A uniformly bounded Hilbert semigroup with dense imaginary eigenvectors does unitarize; forward recurrence supplies the inverse bound. |
| C5 / Weil | Weil positivity is RH, including multiplicities, and says nothing about the model's Jordan blocks. |
| C5 / canonical point | The trace formula is independent of diagonal metric weights. Unit weights are tied to a specified evaluation normalization, not forced by trace or FE. |
| C5 / trace | Include gamma/contact terms, even pole terms, signs, and the factor $2$ at prime times $\pm2\log n$. Untested fixed-time operators are not trace class. |
| C5 / trace on top class | Pole orders give unit multiplicities; theta residues $-2,+2$ do not uniquely normalize a cup trace. |
| C5 / sources | Connes's weighted cokernel and Meyer's bornological virtual representation are not asserted unit-diagonal $\ell^2$ models. |
| C5 / theorem label | `thm:kraus-weil-criterion` is finite/discrete in 08b; use the stated infinite Weil criterion for the zeta converse. |
| C5 / comparison | Kernel analysis is closed, injective, densely defined with dense range, and unbounded in both directions under RH and simplicity. It is not defined on all $K$, and is not the modal coefficient map. |
| C5 / programme | A zero-independent positive geometric comparison is OPEN; “the metric is forced, only its second description is missing” is too strong. |
| C6 / quotient | The real two-prime orbit quotient is non-Hausdorff. A genuine $S$-adic solenoid adds transverse data and has no established claimed partial-Euler-product cohomology. |
| C7 / finite field | Restrict the exact ordinary CM reduction statement to split primes; arbitrary Gaussian norms are not even always prime powers. |
| C7 / associate | The fixed equation has primary $\pi\equiv1\pmod{(1+i)^3}$, up to conjugation. Other associates require quartic twists. |
| C7 / bond | Equality of zetas and Frobenius data does not identify the class-group bond with two-dimensional $H^1$; $h$ is not the Gaussian ideal class number. |
| C7 / metric | The flat Hodge metric lives on the specified complex lift; genus-one equal weights are the single-pair case, not a new arithmetic constraint. |
| C7 / D2 | D2 is $y^2+y=x^3+x+1$ over $\mathbb F_2$, not the singular characteristic-two model $y^2=x^3-x$. |

## 10. What this changes in the notebook

Author: `codex:gpt-6-astra`

| Claim | Status to register | One-sentence statement |
|---|---|---|
| C1 | SHARPENED | Formal pole classes and the adjoint zero-mode semigroup give finite graded Poincaré algebras with reference rates $0,-1/2$, but no new geometric cohomology identification. |
| C2 | SHARPENED | FE and reality give the explicit real alternating full-jet pairing (2.1), while a canonical bond cup product is still OPEN. |
| C3 | PROVED with qualifications | The full finite jet package has a positive invariant polarization iff its zeros are critical and simple; invariant certificate weights must be distinguished from compatibility with a fixed cup form. |
| C4 | PROVED | Neither compression has a positive invariant metric equivalent to energy, and $\sup_{t\ge0}e^{t/4}\|Z_t\|=\infty$ unconditionally. |
| C5 | REFUTED / SHARPENED | Weil positivity is RH for evaluation data, whereas polarization of the full channel additionally needs simplicity and is not selected by a trace formula. |
| C6 | REFUTED / OPEN | The naive two-prime quotient is not a solenoid; constructing cohomology, a trace formula, and a positive cup-compatible metric on a corrected object remains open. |
| C7 | PROVED with qualifications | At split primes the primary CM torus map has the elliptic zeta and class number (7.4), with an independently positive flat metric on its complex lift and only a vacuous genus-one ray comparison. |

The mandatory progress file and the Python check are the only additional authored files; no notebook shard is edited. Bare source filenames beginning with `04`, `02`, or `08` in citations above abbreviate `report/sections/`; bare `manuscript.txt` abbreviates `notes/deninger-lps/src/manuscript.txt`. All line numbers refer to the local files read for this round.
