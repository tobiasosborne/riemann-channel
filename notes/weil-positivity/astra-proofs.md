# Weil positivity, spectral duality, and transfer modes

Author: codex:gpt-6-astra

The status `proved-here` means that a proof is supplied here, using the stated hypotheses and the two explicitly quoted, proved notebook corollaries. It does not mean independently reviewed. No web sources are used. The zeta dictionary in T6 is conditional and does not prove a statement about zeta or validate the analytic construction in the source note.

Throughout, multiset subtraction and union mean subtraction and addition of multiplicities. Write $A=\operatorname{spec}(X)\setminus S$, $d=|A|$, and $z=\mu/r$. In a zeroth power, including $0^0$ in a spectral trace, the value is $1$. Unless specified otherwise, coefficient vectors have finite support in $\mathbb N_0$. Empty retained spectra are allowed: their forms vanish and their spectral assertions are vacuous. No diagonalizability is assumed until T5.

## T1. Weil positivity is exactly a one-sided bound

**H-P (Fourier series of the Poisson kernel; exact statement).** “For $z\in\mathbb C$ with $|z|<1$, the function
$$
P_z(\theta)=\frac{1-|z|^2}{|1-ze^{-i\theta}|^2}
$$
has the absolutely and uniformly convergent Fourier series
$$
P_z(\theta)=1+\sum_{k=1}^{\infty}\left(z^ke^{-ik\theta}+\overline z^{\,k}e^{ik\theta}\right).
$$
It is strictly positive, has integral $2\pi$ over $[0,2\pi]$, and is identically $1$ when $z=0$.”

**H-H (Herglotz theorem on $\mathbb Z$; exact statement).** “A sequence $(b_k)_{k\in\mathbb Z}$ is positive definite if and only if there is a finite positive Borel measure $\eta$ on the unit circle such that
$$
b_k=\int_{\mathbb T}\zeta^k\,d\eta(\zeta)\qquad(k\in\mathbb Z).
$$
The measure is unique and has mass $b_0$.”

H-H supplies terminology; the proof below does not need its converse or existence assertion. H-P is also verified below.

**Lemma T1.1 (single-mode measures and the Poisson signs).**

Hypotheses: $|z|\leq1$; $c=(c_0,\ldots,c_L)$; $f_c(\zeta)=\sum_{l=0}^L c_l\zeta^l$; $z^{[k]}=z^k$ for $k\geq0$, and $z^{[k]}=\overline z^{-k}$ for $k<0$.

Claim:
$$
\sum_{l,m=0}^L c_l\overline{c_m}z^{[l-m]}
=\begin{cases}
\displaystyle\frac1{2\pi}\int_0^{2\pi}|f_c(e^{i\theta})|^2P_z(\theta)\,d\theta,&|z|<1,\\[4pt]
|f_c(z)|^2,&|z|=1.
\end{cases}
$$
In particular, both expressions are nonnegative. At $z=0$ the expression is $\sum_l|c_l|^2$.

Status: `proved-here`.

⟨1⟩1. **Verify H-P, including its Fourier orientation.**

PROOF: Expand both geometric series in
$$
P_z(\theta)=(1-|z|^2)\sum_{p,q\geq0}z^p\overline z^{\,q}e^{-i(p-q)\theta}.
$$
Their absolute sums are bounded uniformly in $\theta$, so regrouping is legitimate. For $k\geq0$, the coefficient of $e^{-ik\theta}$ is
$(1-|z|^2)z^k\sum_{q\geq0}|z|^{2q}=z^k$; the coefficient for negative $k$ is its conjugate counterpart. This gives H-P. The defining quotient is strictly positive, its constant Fourier coefficient is $1$, and substitution of $z=0$ gives $P_0=1$.

⟨1⟩2. **Integrate the polynomial square.**

PROOF: Expand $|f_c(e^{i\theta})|^2=\sum_{l,m}c_l\overline{c_m}e^{i(l-m)\theta}$. Step ⟨1⟩1 gives
$$
\frac1{2\pi}\int e^{ik\theta}P_z(\theta)\,d\theta=z^{[k]}.
$$
This proves the interior formula with the displayed signs. For $z=0$ only $l=m$ survives. For $|z|=1$, $z^{[l-m]}=z^l\overline z^{\,m}$, proving the boundary formula. Each formula is nonnegative. $\square$

**Lemma T1.2 (boundedness and discrete growth).**

Hypotheses: $(b_k)_{k\in\mathbb Z}$ is Hermitian and positive definite. Separately, $\zeta_1,\ldots,\zeta_q$ are distinct points of the unit circle and $m_1,\ldots,m_q$ are positive integers, with $q\geq1$.

Claims: $b_0\geq0$, $|b_k|\leq b_0$ for all $k$; and $a_l=\sum_{j=1}^q m_j\zeta_j^l$ does not tend to zero as $l\to\infty$.

Status: `proved-here`.

⟨1⟩1. **Prove the two-point bound.**

PROOF: One nonzero coefficient gives $b_0\geq0$. For $k>0$, use coefficients only at $0,k$. The quadratic form is
$b_0(|c_0|^2+|c_k|^2)+2\operatorname{Re}(c_k\overline{c_0}b_k)$.
Set $c_0=1$ and, if $b_k\neq0$, choose $|c_k|=1$ with $c_kb_k=-|b_k|$. Positivity gives $2b_0-2|b_k|\geq0$. This is the nonnegativity of the corresponding $2\times2$ determinant, $b_0^2-|b_k|^2\geq0$, including the case $b_0=0$. Hermitian symmetry handles negative $k$.

⟨1⟩2. **Compute the mean square of the leading modes.**

PROOF: For $\omega\in\mathbb T\setminus\{1\}$,
$$
\frac1L\sum_{l=0}^{L-1}\omega^l=\frac{1-\omega^L}{L(1-\omega)}\longrightarrow0.
$$
Consequently
$$
\frac1L\sum_{l=0}^{L-1}|a_l|^2
=\sum_{j,k}m_jm_k\frac1L\sum_{l=0}^{L-1}(\zeta_j\overline\zeta_k)^l
\longrightarrow\sum_jm_j^2>0.
$$
If $a_l\to0$, the averages of $|a_l|^2$ would tend to zero: split the average into a fixed initial segment and a uniformly small tail. This is a contradiction. $\square$

**Theorem T1.3 (finite Weil positivity).**

Hypotheses: $X$ is a linear operator on a finite-dimensional complex vector space; $S$ is any spectral sub-multiset; $r>0$; $\nu_l=\sum_{\mu\in A}(\mu/r)^l$ for $l\geq0$ and $\nu_{-l}=\overline{\nu_l}$.

Claim:
$$
\nu\text{ is positive definite}\quad\Longleftrightarrow\quad |\mu|\leq r\quad(\mu\in A).
$$
This includes zero eigenvalues and algebraic multiplicities.

Status: `proved-here`.

⟨1⟩1. **The spectral bound implies positivity.**

PROOF: Sum Lemma T1.1 over $A$, counting each eigenvalue with its algebraic multiplicity. Interior modes contribute Poisson measures and boundary modes contribute point masses. A retained zero contributes normalized Lebesgue measure, hence $\sum_l|c_l|^2$. The total measure has mass $d=\nu_0$ and every summand of the quadratic form is nonnegative.

⟨1⟩2. **Positivity rules out a mode outside the disk.**

PROOF: Lemma T1.2 gives $|\nu_l|\leq d$. Suppose the maximum normalized modulus is $R=\max_{\mu\in A}|\mu|/r>1$. Group the distinct maximal-modulus modes as $R\zeta_j$ with multiplicities $m_j$. For $l\geq1$,
$$
R^{-l}\nu_l=\sum_jm_j\zeta_j^l+b_l,
\qquad b_l\longrightarrow0,
$$
because every remaining normalized eigenvalue has modulus strictly less than $R$. This also covers zeros, whose positive powers vanish. The boundedness of $\nu_l$ implies $R^{-l}\nu_l\to0$, so $\sum_jm_j\zeta_j^l\to0$, contrary to Lemma T1.2. This proves the converse. $\square$

The trace formula is independent of Jordan blocks: a triangular form for $X$ has the eigenvalues on its diagonal, and its powers have their powers on the diagonal. This explains why algebraic multiplicity, rather than an eigenvector count, occurs throughout.

## T2. Duality turns the disk into a circle and identifies the pairing

**Theorem T2.1 (reflection duality and the inflow identity).**

Hypotheses: those of T1.3, and the retained multiset $A$ is invariant under
$$
J(\mu)=\frac{r^2}{\overline\mu}.
$$
In particular $0\notin A$. Let $Z=A/r$, $j(z)=1/\overline z$, and
$$
M(c)=\sum_{z\in Z}f_c(z)\overline{f_c(j(z))}.
$$

Claims: $W(c)=M(c)$ for every finite coefficient vector; and the following are equivalent:
$$
W\geq0\text{ on all coefficient vectors};\qquad
|\mu|=r\text{ for every }\mu\in A;\qquad
J(\mu)=\mu\text{ for every }\mu\in A.
$$

Status: `proved-here`.

⟨1⟩1. **Duality identifies negative moments with reciprocal moments.**

PROOF: For $k>0$, multiset invariance gives
$$
\sum_{z\in Z}z^{-k}=\sum_{w\in Z}(1/\overline w)^{-k}
=\sum_{w\in Z}\overline w^{\,k}=\nu_{-k}.
$$
For nonnegative $k$, the equality $\sum_z z^k=\nu_k$ holds by definition. Thus $\sum_z z^k=\nu_k$ for every integer $k$.

⟨1⟩2. **Expand the mode-pairing form.**

PROOF: Since $\overline{j(z)}=z^{-1}$,
$$
M(c)=\sum_{l,m}c_l\overline{c_m}\sum_{z\in Z}z^lz^{-m}
=\sum_{l,m}c_l\overline{c_m}\nu_{l-m}=W(c).
$$
All sums here are finite. This also proves the identity for finite Laurent coefficient vectors: translating their indices into $\mathbb N_0$ leaves $W$ invariant, and multiplication of $f$ by $z^h$ leaves each pairing summand invariant because $z^h\overline{j(z)}^{\,h}=1$.

⟨1⟩3. **The one-sided bound becomes two-sided.**

PROOF: By T1.3, positivity implies $|\mu|\leq r$ for all retained modes. Apply the same bound to $J(\mu)\in A$: $r^2/|\mu|\leq r$, hence $|\mu|\geq r$. Conversely, the circle lies in the disk, so T1.3 gives positivity. Finally, $J(\mu)=\mu$ is equivalent to $|\mu|^2=r^2$. $\square$

**Proposition T2.2 (orbit contributions and an isolated negative pair).**

Hypotheses: those of T2.1. Distinct values in a $j$-orbit have their common algebraic multiplicity $m$.

Claim: a fixed orbit $\{z\}$ contributes $m|f_c(z)|^2$; a two-element orbit $\{z,j(z)\}$ contributes
$$
2m\operatorname{Re}\left(f_c(z)\overline{f_c(j(z))}\right).
$$
If any two-element orbit exists, there is a polynomial $f_c$ for which the *whole* form $W(c)$ is strictly negative.

Status: `proved-here`.

⟨1⟩1. **Group the sum by orbits.**

PROOF: The two terms of a nonfixed orbit are conjugates, and a fixed point satisfies $j(z)=z$. Apply T2.1 to obtain the stated decomposition of $W=M$.

⟨1⟩2. **Isolate a selected nonfixed orbit by interpolation.**

PROOF: List all distinct points of $Z$ as $z_1,\ldots,z_q$. Choose prescribed values $v_i=1$ at the selected $z$, $v_i=-1$ at $j(z)$, and $v_i=0$ elsewhere. The polynomial
$$
f(\zeta)=\sum_{i=1}^qv_i\prod_{h\neq i}\frac{\zeta-z_h}{z_i-z_h}
$$
has exactly these values; all denominators are nonzero. Its selected orbit contributes $-2m$ and every other orbit contributes zero. This proves negativity of the complete form, not just the possibility of a negative summand. It is a second proof of the necessity in T2.1. $\square$

**Proposition T2.3 (holomorphic reciprocal symmetry).**

Hypotheses: those of T1.3; $A$ has no zero and is invariant under $I(\mu)=r^2/\mu$.

Claims: positivity is equivalent to $|\mu|=r$ throughout $A$, without assuming conjugation symmetry. If $A$ is also invariant under complex conjugation, it is $J$-invariant and $W=M$. The map $I$ is holomorphic on $\mathbb C^\times$, not linear.

Status: `proved-here`.

⟨1⟩1. **Prove the circle criterion.**

PROOF: T1.3 and $|I(\mu)|=r^2/|\mu|$ give both inequalities exactly as in T2.1. Conversely the circle condition implies positivity by T1.3.

⟨1⟩2. **Identify the additional symmetry needed for the pairing identity.**

PROOF: Conjugation commutes with $I$, and their composition is $J$, so both invariances imply $J$-invariance with multiplicities. T2.1 applies. Reciprocal invariance alone does not identify the negative moments: with $r=1$ and $A=\{2i,-i/2\}$, one has $\nu_1=3i/2$, $\nu_{-1}=-3i/2$, whereas $\sum_{z\in A}z^{-1}=3i/2$. For $f(z)=1+z$, $W=4$ but $M=4+3i$. $\square$

Without spectral duality, $J$ still exists as a map of the punctured plane, and the assertion that every retained eigenvalue is fixed by $J$ still has a meaning. What fails is the claim that its image is another retained mode, and therefore the identification of $W$ with a pairing of retained modes. A retained zero has no finite reflected partner at all; T1 nevertheless applies to it.

## T3. Kraus families: reality, inverse pairing, and the Ramanujan circle

The conventions for $T$ are exactly those of the notebook:
$$
T(v\otimes|i\rangle)=\sum_{j\neq\bar i}\mathcal E_i(v)\otimes|j\rangle,
\qquad \Sigma=\sum_i\mathcal E_i,
\qquad D=2m.
$$

**H-QT (quoted local result: Corollary 2 of `notes/quantum-ihara-general.md`).** For $\mathcal E_i=\operatorname{Ad}(B_i)$ and $B_{\bar i}=B_i^\dagger$, for every $l\geq1$,
$$
\operatorname{Tr}_W T^l
=\sum_{\substack{(i_1,\ldots,i_l)\in[D]^l\\i_{k+1}\neq\bar i_k\ (k\in\mathbb Z/l)}}
\left|\operatorname{Tr}(B_{i_l}\cdots B_{i_1})\right|^2\geq0.
$$
This established notebook result is quoted, not reproved here. At $l=0$ the trace is $ND$, not the displayed cyclic-word sum.

**H-QI (quoted local result: Corollary 3 of that note).** For arbitrary superoperators on an $N$-dimensional space satisfying $\mathcal E_{\bar i}=\mathcal E_i^{-1}$,
$$
\det_W(1-uT)=(1-u^2)^{N(D-2)/2}\det_V(1-u\Sigma+(D-1)u^2).
$$
It is a polynomial identity, including at the apparent exceptional values $u=\pm1$ in its derivation.

**Proposition T3.1 (Kraus reality needs no pairing).**

Hypotheses: $V=M_n(\mathbb C)$ with $\langle x,y\rangle=\operatorname{Tr}(x^\dagger y)$; $\mathcal E_i(x)=B_ixB_i^\dagger$ for arbitrary matrices $B_i$; $W=\bigoplus_{i=1}^D M_n$ with its orthogonal sum inner product; a fixed-point-free reversal. Define $C_W(x)_i=x_i^\dagger$ and $C_V(x)=x^\dagger$.

Claims: $C_W,C_V$ are antiunitary involutions, $C_WT=TC_W$, and $C_V\Sigma=\Sigma C_V$. Both spectra are closed under complex conjugation with algebraic multiplicities. If in addition $B_{\bar i}=B_i^\dagger$, H-QT supplies the nonnegative ring trace.

Status: `proved-here`.

⟨1⟩1. **Verify antiunitarity and commutation.**

PROOF: Dagger is antilinear, squares to the identity, and
$$
\langle x^\dagger,y^\dagger\rangle=\operatorname{Tr}(xy^\dagger)
=\overline{\operatorname{Tr}(x^\dagger y)}.
$$
Apply this componentwise for $C_W$. Moreover
$(B_ixB_i^\dagger)^\dagger=B_ix^\dagger B_i^\dagger$, so each $\mathcal E_i$ commutes with $C_V$. The transition coefficients in the definition of $T$ are real $0$ or $1$; applying dagger to each component therefore gives $C_WT=TC_W$. Summing the same identities gives the assertion for $\Sigma$.

⟨1⟩2. **Include algebraic multiplicities.**

PROOF: For $Y=T$ or $\Sigma$, its corresponding conjugation satisfies
$C(Y-\mu I)^k=(Y-\overline\mu I)^kC$.
It is an antilinear bijection between the two generalized eigenspaces. Taking $k$ at least the dimension of the ambient space shows that their dimensions, hence their algebraic multiplicities, agree. The last claim is exactly H-QT. $\square$

**Theorem T3.2 (inverse pairing and exact multiplicities).**

Hypotheses: first allow arbitrary superoperators $\mathcal E_i$ on an $N$-dimensional complex space, with $\mathcal E_{\bar i}=\mathcal E_i^{-1}$; $D=2m\geq3$ (thus $D\geq4$). Put
$$
q=D-1>1,\qquad k=\frac{N(D-2)}2=N(m-1),\qquad
S_0=\{+1^{[k]},-1^{[k]}\}.
$$
The notation $x^{[k]}$ here denotes $k$ copies of the value $x$, not a power. Let $a_\alpha$ be the algebraic multiplicity of $\alpha$ in $\Sigma$.

Claims:
$$
\operatorname{spec}(T)=S_0\uplus
\biguplus_{\alpha\in\operatorname{spec}_{\rm distinct}(\Sigma)}
\operatorname{Roots}(\mu^2-\alpha\mu+q)^{[a_\alpha]}.
$$
Each quadratic is counted with its root multiplicities. Thus $A_0=\operatorname{spec}(T)\setminus S_0$ has $2N$ elements, no zero, and is invariant under $\mu\mapsto q/\mu$. Furthermore,
$$
A_0\text{ is conjugation-invariant}\quad\Longleftrightarrow\quad
\operatorname{spec}(\Sigma)\text{ is conjugation-invariant}.
$$
For inverse-paired Kraus matrices $B_{\bar i}=B_i^{-1}$, both sides of this last equivalence **always hold**. There is no Kraus counterexample to conjugation symmetry.

Status: `proved-here`.

⟨1⟩1. **Pass from H-QI to the characteristic polynomial.**

PROOF: A triangular form of $\Sigma$ shows
$$
\det(1-u\Sigma+qu^2)=\prod_\alpha(1-\alpha u+qu^2)^{a_\alpha}.
$$
Substitute $u=1/x$ into H-QI and multiply by $x^{ND}$; the powers cancel because $2k+2N=ND$. For $x\neq0$, and therefore as a polynomial identity,
$$
\det(xI-T)=(x^2-1)^k\prod_\alpha(x^2-\alpha x+q)^{a_\alpha}.
$$
This proves the multiset formula, including the fact that the specified $S_0$ really is a sub-multiset. The constant term of every factor is nonzero, so $T$ and $A_0$ have no zero eigenvalue.

⟨1⟩2. **Handle reciprocal pairs and collisions.**

PROOF: The two roots are
$$
\mu_\pm(\alpha)=\frac{\alpha\pm\sqrt{\alpha^2-4q}}2,
\qquad \mu_+(\alpha)\mu_-(\alpha)=q.
$$
For $\alpha\neq\pm2\sqrt q$ they are distinct and each occurs $a_\alpha$ times in $A_0$. For $\alpha=\pm2\sqrt q$, the value $\mu=\pm\sqrt q$ occurs $2a_\alpha$ times; it is fixed by $\mu\mapsto q/\mu$. In the $u$ polynomial this is the double root $u=\pm1/\sqrt q$. A double root of the determinant says nothing by itself about the size of a Jordan block of $T$.

The value $\mu=1$ comes from $\alpha=1+q=D$ and $\mu=-1$ from $\alpha=-D$. Hence their total multiplicities in $T$ are respectively $k+a_D$ and $k+a_{-D}$. Removing $S_0$ removes just $k$ copies of each; it preserves all copies furnished by the quadratic factors. Different $\alpha$ values cannot supply the same nonzero $\mu$, since $\alpha=\mu+q/\mu$.

⟨1⟩3. **Prove the exact conjugation criterion.**

PROOF: Since $q$ is real, conjugate $\alpha$ values supply conjugate quadratic root multisets, which proves one direction. Conversely, the multiset pushforward of $A_0$ by $h(\mu)=\mu+q/\mu$ is exactly two copies of $\operatorname{spec}(\Sigma)$, even at double roots. The map $h$ commutes with conjugation. Thus conjugation invariance of $A_0$ implies conjugation invariance of twice the latter multiset, and equality of integer multiplicities can be divided by two.

⟨1⟩4. **Specialize to Kraus families and distinguish arbitrary superoperators.**

PROOF: If $B_{\bar i}=B_i^{-1}$, then $\mathcal E_{\bar i}=\operatorname{Ad}(B_i^{-1})=\mathcal E_i^{-1}$, so the preceding steps apply. T3.1 gives conjugation symmetry of $\Sigma$, regardless of the pairing. Therefore $A_0$ is conjugation-invariant and, with $r=\sqrt q$, also $J$-invariant by T2.3. In particular T2.1 gives
$$
\nu(T;S_0,\sqrt q)\text{ positive definite}
\quad\Longleftrightarrow\quad |\mu|=\sqrt q\quad(\mu\in A_0)
$$
for every inverse-paired Kraus family, without an adjoint-pairing hypothesis. It does not give the real channel-eigenvalue interpretation in T3.4. For example, the inverse-paired matrices
$B_1=\operatorname{diag}(2i,1)$, $B_3=\operatorname{diag}(-i/2,1)$, $B_2=B_4=I_2$ have
$\operatorname{spec}(\Sigma)=\{25/4,4,2+3i/2,2-3i/2\}$, as follows by applying $\Sigma$ to the four matrix units. This multiset is conjugation-invariant but not entirely real.

For comparison, a counterexample exists in the larger class of arbitrary superoperators: take $N=1,D=4$, pair $(1,3),(2,4)$, and let the scalar maps be $2i,1,-i/2,1$. They are inverse paired but $\Sigma=2+3i/2$. The retained characteristic polynomial is
$$
x^2-(2+3i/2)x+3,
$$
whose roots cannot be conjugation-invariant because their sum is nonreal. These maps are not Kraus maps on $M_1$: every such Kraus map is multiplication by a nonnegative real number. $\square$

**Proposition T3.3 (simultaneous pairing means unitarity).**

Hypotheses: $B\in M_n$ is invertible. For the family statement, retain the fixed reversal and the exact matrix equations specified below.

Corrected claims:
$$
\operatorname{Ad}(B^\dagger)=\operatorname{Ad}(B)^{-1}
\quad\Longleftrightarrow\quad B^\dagger B=I
\quad\Longleftrightarrow\quad B\text{ is unitary}.
$$
Thus an adjoint-paired matrix family also obeys inverse pairing, at either the exact matrix or exact superoperator level, if and only if all its matrices are unitary. “A nonzero scalar multiple of a unitary” is insufficient. The projective variant is
$$
\operatorname{Ad}(B^\dagger)=\kappa\operatorname{Ad}(B)^{-1}
\ (\kappa>0)
\quad\Longleftrightarrow\quad B^\dagger B=\sqrt\kappa I.
$$

Status: `proved-here`.

⟨1⟩1. **Compose the superoperators.**

PROOF: Their equality is equivalent to $\operatorname{Ad}(P)=I$ with $P=B^\dagger B>0$. Evaluating at $I$ gives $P^2=I$. The positive eigenvalues of the Hermitian matrix $P$ must all be $1$, hence $P=I$. Conversely $P=I$ gives $B^\dagger=B^{-1}$ and the desired equality. The same argument with $\operatorname{Ad}(P)=\kappa I$ gives $P^2=\kappa I$, hence $P=\sqrt\kappa I$, and this condition also suffices.

⟨1⟩2. **Apply this to the pairing conventions.**

PROOF: With $B_{\bar i}=B_i^\dagger$, inverse pairing at the matrix level reads $B_i^\dagger=B_i^{-1}$; at the superoperator level it is exactly step ⟨1⟩1. Both force unitarity. If $B=cU$ for a unitary $U$, then $P=|c|^2I$ and $\operatorname{Ad}(P)=|c|^4I$; equality with $I$ requires $|c|=1$. For example, $B=2I$ has $\operatorname{Ad}(B^\dagger)=4I$ as a superoperator, whereas $\operatorname{Ad}(B)^{-1}=I/4$. $\square$

**Theorem T3.4 (the one-sided criterion and the unitary Ramanujan criterion).**

Hypotheses for the first claim: an adjoint-paired Kraus family, any spectral sub-multiset $S$, and any $r>0$.

First claim: positivity of $\nu(T;S,r)$ is exactly the bound $|\mu|\leq r$ off $S$. Ring-trace nonnegativity alone does not assert this positivity.

Additional hypotheses for the circle claim: all $B_i$ are unitary, $B_{\bar i}=B_i^\dagger$, and $D=2m\geq4$. Set $N=n^2$, $q=D-1$, $r=\sqrt q$, and $\Phi=\Sigma/D$. Write $d_+$ and $d_-$ for the multiplicities of $+1$ and $-1$ as eigenvalues of $\Phi$, taking a missing eigenvalue to have multiplicity zero. Define
$$
S=S_0\uplus\{q^{[d_+]},1^{[d_+]}\}
\uplus\{(-q)^{[d_-]},(-1)^{[d_-]}\}.
$$
Then the following are equivalent:
$$
\begin{aligned}
&\nu(T;S,\sqrt q)\text{ is positive definite};\\
&|\lambda|\leq\frac{2\sqrt{D-1}}D
\quad\text{for every eigenvalue }\lambda\text{ of }\Phi\text{ other than }\pm1;\\
&|\mu|=\sqrt q\quad\text{for every }\mu\in\operatorname{spec}(T)\setminus S;\\
&J(\mu)=\mu\quad\text{for every such retained mode}.
\end{aligned}
$$
The second line is the Ramanujan bound named in the question.

Status: `proved-here`.

⟨1⟩1. **Apply the general one-sided theorem.**

PROOF: The first claim is T1.3. H-QT says that individual unrescaled traces are nonnegative; positive definiteness additionally constrains all their rescaled cross terms and the subtraction of $S$, so it is a distinct property.

⟨1⟩2. **Establish self-adjointness, reality, and normalization of $\Phi$.**

PROOF: Cyclicity of the matrix trace gives
$\operatorname{Ad}(B)^*=\operatorname{Ad}(B^\dagger)$ in the Hilbert--Schmidt inner product. Reversal permutes the summands of $\Sigma$, so $\Sigma^*=\Sigma$ and $\Phi^*=\Phi$. In fact self-adjointness here already follows from adjoint pairing, without unitarity. A self-adjoint finite matrix has real eigenvalues: for an eigenvector its eigenvalue equals the real quotient $\langle v,\Phi v\rangle/\langle v,v\rangle$. Its orthogonal complement is invariant, so induction diagonalizes it orthogonally.

Unitarity additionally gives $\|\operatorname{Ad}(B_i)v\|_{\rm HS}=\|v\|_{\rm HS}$ and $\operatorname{Ad}(B_i)I=I$. Therefore $\|\Phi\|\leq1$, all its eigenvalues lie in $[-1,1]$, and $d_+\geq1$. Neither simplicity of $+1$ nor absence of $-1$ is assumed.

⟨1⟩3. **Perform the multiset subtraction.**

PROOF: By T3.2 with $\alpha=D\lambda$, each occurrence of $\lambda$ supplies the roots of
$\mu^2-D\lambda\mu+q=0$.
For $\lambda=1$ these are $q,1$; for $\lambda=-1$ they are $-q,-1$, distinct because $q>1$. Thus the displayed $S$ is a sub-multiset. In particular it removes $k+d_+$ copies of $1$ and $k+d_-$ copies of $-1$, including but not confusing their $S_0$ copies. It removes $d_+$ copies of $q$ and $d_-$ copies of $-q$.

The remaining multiset has size $2(N-d_+-d_-)$ and consists precisely of the quadratic pairs for $\lambda\neq\pm1$. It is reciprocal-invariant. Because these quadratics have real coefficients, it is also conjugation-invariant and hence $J$-invariant. This verifies the needed symmetry after subtraction, not just before it.

⟨1⟩4. **Relate each real channel eigenvalue to the circle.**

PROOF: For real $\alpha=D\lambda$ with $|\alpha|<2\sqrt q$, the two roots are conjugates and have product $q$, so both have modulus $\sqrt q$. At $\alpha=\pm2\sqrt q$ the double root is $\pm\sqrt q$, occurring twice per occurrence of $\lambda$. If $|\alpha|>2\sqrt q$, the roots are real, have product $q$, and cannot both have modulus $\sqrt q$: the latter condition for real roots with positive product would force both to be $\sqrt q$ or both $-\sqrt q$, giving an endpoint value of $\alpha$. Hence at least one root has modulus strictly larger than $\sqrt q$. This proves the equivalence of the channel bound and the retained circle condition. T2.1 completes the remaining equivalences. $\square$

Arbitrary scalar multiples cannot be substituted into this theorem. If all matrices have one common magnitude, $B_i=\sqrt w\,U_i$ with $w>0$ and $U_{\bar i}=U_i^\dagger$, then $T=wT_U$ and $\Phi=w\Phi_U$: the corresponding radius is $w\sqrt q$, the trivial roots are scaled by $w$, and the channel bound is $2w\sqrt q/D$ with trivial channel eigenvalues $\pm w$. This follows directly by factoring out $w$ from every $\mathcal E_i$. Unequal magnitudes generally destroy this simple quadratic relation. Normalizing individual matrices to unitaries changes the transfer operator and is not an innocuous reinterpretation of the original theorem.

**Proposition T3.5 (an adjoint-paired family with no reciprocal duality).**

Hypotheses: $n=2,D=4$, reversal $(1,3),(2,4)$, and
$$
B_1=B_3=\begin{pmatrix}1&0\\0&2\end{pmatrix},\qquad B_2=B_4=I_2.
$$
This is an invertible, adjoint-paired family, and $B_1$ is not a scalar multiple of a unitary. Define
$$
p_2=\frac{3+\sqrt{33}}2,\quad n_2=\frac{3-\sqrt{33}}2,\quad
p_4=\frac{5+\sqrt{73}}2,\quad n_4=\frac{5-\sqrt{73}}2.
$$
The full spectrum, with multiplicities, is
$$
\{1^{[5]},2^{[2]},4,3,-1,p_2^{[2]},n_2^{[2]},p_4,n_4\}.
$$
Take $S=\{1^{[5]},2^{[2]},4,3,-1\}$. The retained multiset
$$
A=\{p_2^{[2]},n_2^{[2]},p_4,n_4\}
$$
is not invariant under $\mu\mapsto c/\mu$ for any $c\in\mathbb C^\times$. Nevertheless its Weil form is well defined for every $r>0$, and is positive definite exactly when $r\geq p_4$. At $r=p_4$ it is positive although its retained modes do not all lie on the critical circle.

Status: `proved-here` (the displayed block polynomials were also checked by exact SymPy arithmetic).

⟨1⟩1. **Compute the spectrum on matrix-unit blocks.**

PROOF: Each line $\mathbb CE_{ab}\subset M_2$ is invariant under all four Kraus maps. On it their weights are $(a,1,a,1)$, with $a=1$ on $E_{11}$, $a=2$ on $E_{12},E_{21}$, and $a=4$ on $E_{22}$. In edge coordinates $(1,2,3,4)$ the resulting block is
$$
T_a=\begin{pmatrix}
a&1&0&1\\a&1&a&0\\0&1&a&1\\a&0&a&1
\end{pmatrix}.
$$
The antisymmetric vectors $(1,0,-1,0)$ and $(0,1,0,-1)$ have eigenvalues $a$ and $1$. The complementary subspace $(x,y,x,y)$ has matrix
$\begin{pmatrix}a&2\\2a&1\end{pmatrix}$, so
$$
\det(xI-T_a)=(x-a)(x-1)\big(x^2-(a+1)x-3a\big).
$$
For $a=1$ the quadratic roots are $3,-1$; the other two choices give the displayed radicals. Counting the $a=2$ block twice gives all sixteen eigenvalues and the stated multiplicities. The chosen $S$ removes all eight antisymmetric-sector eigenvalues and the two symmetric-sector eigenvalues from $E_{11}$, a common fixed matrix-unit sector. It is a specified ten-element sub-multiset, not an asserted universal choice of trivial modes.

⟨1⟩2. **Exclude every reciprocal constant.**

PROOF: The four retained values are distinct. The multiplicity-two values are exactly $p_2,n_2$; a reciprocal symmetry must permute this two-element set. Fixing both would require $p_2^2=n_2^2$, impossible because they are distinct and $p_2+n_2=3\neq0$. Swapping them requires $c=p_2n_2=-6$. The multiplicity-one values $p_4,n_4$ must likewise be swapped, since their sum is $5\neq0$, and this requires $c=p_4n_4=-12$. The requirements contradict each other. All values are nonzero; $c=0$ cannot map this multiset onto itself either. Since the spectrum is real, this also excludes a retained $J$-symmetry for any radius. The full sixteen-element spectrum has no reciprocal symmetry either: its unique multiplicity-five value $1$ would force $c=1$, but then the value $2$ would need the absent partner $1/2$.

⟨1⟩3. **Apply Weil positivity without a duality.**

PROOF: The largest retained modulus is $p_4$: in each quadratic $p_a>|n_a|$, and $p_4>p_2>0$. T1.3 gives positivity if and only if $r\geq p_4$. For example, at $r=p_4$ the $p_4$ mode is on the circle and all other retained modes are strictly inside it, so the form is positive definite in the sequence sense but there is no spectral partner symmetry. H-QT still gives the nonnegative full ring traces. $\square$

These results separate three structures: Kraus maps supply a conjugation symmetry; inverse pairing supplies reciprocal symmetry; and positivity of the rescaled trace supplies the disk bound. Adjoint pairing alone does not supply reciprocal symmetry. For completely arbitrary superoperators even the nonnegative ring-count premise is absent: a scalar superoperator with weight $i$ and $D=2$ can already give $\operatorname{Tr}T=2i$ if both weights are $i$. T1 and T2 still apply to that transfer operator with their stated hypotheses.

## T4. Continuous time: half-planes, reflection, and continuous ring norms

**H-B (Bochner theorem on $\mathbb R$; exact statement).** “A continuous function $F:\mathbb R\to\mathbb C$ is positive definite if and only if there is a finite positive Borel measure $\eta$ on $\mathbb R$ such that
$$
F(t)=\int_{\mathbb R}e^{it\xi}\,d\eta(\xi)\qquad(t\in\mathbb R).
$$
The measure is unique and has mass $F(0)$.”

**Lemma T4.1 (Lorentzian modes and continuous growth).**

Hypotheses for the first claim: $b>0$, $\omega\in\mathbb R$, $h(t)=e^{-b|t|+i\omega t}$, and the Fourier convention $\widehat h(\xi)=\int_{\mathbb R}h(t)e^{-i\xi t}\,dt$.

Hypotheses for the second claim: $\omega_1,\ldots,\omega_q$ are distinct real numbers, $q\geq1$, and $m_j$ are positive integers.

Claims:
$$
\widehat h(\xi)=\frac{2b}{b^2+(\xi-\omega)^2},\qquad
h(t)=\int_{\mathbb R}e^{it\xi}\frac{b\,d\xi}{\pi[b^2+(\xi-\omega)^2]}.
$$
Thus $h$ is positive definite; $e^{i\omega t}$ is represented by $\delta_\omega$. Also $a(t)=\sum_jm_je^{i\omega_jt}$ does not tend to zero as $t\to+\infty$.

Status: `proved-here`.

⟨1⟩1. **Compute both Fourier signs and the mass.**

PROOF: Splitting at zero gives
$$
\widehat h(\xi)=\int_0^\infty e^{-[b+i(\xi-\omega)]t}\,dt
+\int_0^\infty e^{-[b-i(\xi-\omega)]t}\,dt
=\frac1{b+i(\xi-\omega)}+\frac1{b-i(\xi-\omega)}.
$$
Their sum is the displayed Lorentzian. Its inverse representation can be proved from the already verified H-P, without invoking a further Fourier inversion theorem. For $\varepsilon>0$ define
$$
p_\varepsilon(x)=\frac{\varepsilon}{2\pi}
\frac{1-e^{-2b\varepsilon}}
{(1-e^{-b\varepsilon})^2+2e^{-b\varepsilon}(1-\cos(\varepsilon x))}
\mathbf1_{\{|x|\leq\pi/\varepsilon\}}.
$$
By the change of variables $\theta=\varepsilon x$ and H-P,
$$
\int e^{ik\varepsilon x}p_\varepsilon(x)\,dx=e^{-b\varepsilon|k|}
\qquad(k\in\mathbb Z).
$$
On every bounded $x$ interval, $p_\varepsilon$ tends uniformly to $b/[\pi(b^2+x^2)]$. There is also a common integrable bound for $b\varepsilon\leq1$: use
$1-e^{-b\varepsilon}\geq e^{-1}b\varepsilon$, $1-e^{-2b\varepsilon}\leq2b\varepsilon$, and $1-\cos\theta\geq2\theta^2/\pi^2$ for $|\theta|\leq\pi$. The last inequality follows from $\sin u\geq2u/\pi$ on $[0,\pi/2]$, which follows from concavity of sine. These inequalities give
$$
0\leq p_\varepsilon(x)\leq
\frac{b}{\pi(e^{-2}b^2+4e^{-1}x^2/\pi^2)}.
$$
For $t\neq0$ choose $\varepsilon=|t|/k$ with positive integers $k\to\infty$ and use Fourier index $k\operatorname{sgn}(t)$. Uniform convergence on compact intervals, followed by the common tail bound, permits passage to the limit in the integral. It yields
$\int e^{itx}b/[\pi(b^2+x^2)]\,dx=e^{-b|t|}$. At $t=0$ its mass is $1$ by the arctangent integral. Shifting $x=\xi-\omega$ proves the displayed representation with its exact normalization.

⟨1⟩2. **Prove positivity from the representation.**

PROOF: For any real times $t_j$,
$$
\sum_{j,k}c_j\overline{c_k}h(t_j-t_k)
=\int_{\mathbb R}\left|\sum_jc_je^{it_j\xi}\right|^2
\frac{b\,d\xi}{\pi[b^2+(\xi-\omega)^2]}\geq0.
$$
The same calculation with $\delta_\omega$ gives $e^{i\omega t}$. This proves the needed direction of H-B directly for these modes.

⟨1⟩3. **Prove continuous growth.**

PROOF: When $\omega_j\neq\omega_k$,
$$
\frac1T\int_0^Te^{i(\omega_j-\omega_k)t}\,dt
=\frac{e^{i(\omega_j-\omega_k)T}-1}{iT(\omega_j-\omega_k)}\longrightarrow0.
$$
Expanding the square therefore gives
$T^{-1}\int_0^T|a(t)|^2\,dt\to\sum_jm_j^2>0$.
If $a(t)\to0$, split the integral at a fixed time and bound the remaining tail uniformly to obtain limit zero, a contradiction. $\square$

**Theorem T4.2 (continuous Weil positivity is a half-plane bound).**

Hypotheses: $L$ is linear on a finite-dimensional complex space; $S$ is a spectral sub-multiset; $a\in\mathbb R$; $A=\operatorname{spec}(L)\setminus S$; for $t\geq0$ define
$$
F(t)=e^{-at}\left(\operatorname{Tr}e^{tL}-\sum_{\rho\in S}e^{t\rho}\right)
=\sum_{\rho\in A}e^{t(\rho-a)},
\qquad F(-t)=\overline{F(t)}.
$$

Claims: $F$ is continuous on $\mathbb R$, and
$$
F\text{ is positive definite}\quad\Longleftrightarrow\quad
\operatorname{Re}\rho\leq a\quad(\rho\in A).
$$

Status: `proved-here`.

⟨1⟩1. **Express the Hermitian extension mode by mode.**

PROOF: Write $\rho-a=-b_\rho+i\omega_\rho$ with $b_\rho,\omega_\rho$ real. The extended summand is
$e^{-b_\rho|t|+i\omega_\rho t}$, for all real $t$, whether or not $b_\rho\geq0$. There are finitely many summands, each continuous and equal to $1$ at zero. In particular $F(0)=|A|$ and the two definitions at zero agree.

⟨1⟩2. **Prove positivity under the half-plane bound.**

PROOF: The bound says $b_\rho\geq0$. Use the Lorentzian measure of T4.1 for $b_\rho>0$ and the point mass at $\omega_\rho$ for $b_\rho=0$. Their finite sum represents $F$ by a positive measure, of mass $|A|$, and gives positivity by the square-integral calculation in T4.1.

⟨1⟩3. **Use boundedness to prove the converse.**

PROOF: Applying positive definiteness to the two times $0,t$ gives $|F(t)|\leq F(0)$ by the same two-point proof as T1.2. If $A_*=\max_{\rho\in A}\operatorname{Re}(\rho-a)>0$, group the modes with this real part by their distinct frequencies $\omega_j$ and multiplicities $m_j$. Then, for $t\geq0$,
$$
e^{-A_*t}F(t)=\sum_jm_je^{i\omega_jt}+b(t),\qquad b(t)\longrightarrow0.
$$
Boundedness makes the left-hand side tend to zero. T4.1 excludes the resulting convergence of the leading sum to zero. This proves necessity. $\square$

**Theorem T4.3 (line duality and the exact continuous pairing).**

Hypotheses: those of T4.2, with $A$ invariant as a multiset under
$$
R_a(\rho)=2a-\overline\rho.
$$
For arbitrary finite real times $t_j$ and complex coefficients $c_j$, let $g=\sum_jc_j\delta_{t_j}$ and define the centered exponential transform
$$
\widehat g_L(\rho)=\sum_jc_je^{t_j(\rho-a)}.
$$

Claims:
$$
\sum_{j,k}c_j\overline{c_k}F(t_j-t_k)
=\sum_{\rho\in A}\widehat g_L(\rho)
\overline{\widehat g_L(2a-\overline\rho)};
$$
and $F$ is positive definite if and only if every retained eigenvalue has real part $a$, equivalently is fixed by $R_a$.

Status: `proved-here`.

⟨1⟩1. **Identify the two-sided exponential sum.**

PROOF: Put $\alpha_\rho=\rho-a$. Reflection sends $\alpha_\rho$ to $-\overline{\alpha_\rho}$. For $u>0$, multiset invariance gives
$$
\sum_{\rho\in A}e^{-u\alpha_\rho}
=\sum_{\rho\in A}e^{u\overline{\alpha_\rho}}
=\overline{F(u)}=F(-u).
$$
Thus $F(v)=\sum_{\rho\in A}e^{v(\rho-a)}$ for every real $v$, although without duality this formula would generally disagree with the prescribed extension when $v<0$.

⟨1⟩2. **Expand the pairing with the correct signs.**

PROOF: The complex conjugate of the reflected exponent is
$$
\overline{\big((2a-\overline\rho)-a\big)}=a-\rho=-(\rho-a).
$$
The right-hand side of the claimed identity is consequently
$$
\sum_{j,k}c_j\overline{c_k}\sum_{\rho\in A}
e^{t_j(\rho-a)}e^{-t_k(\rho-a)}
=\sum_{j,k}c_j\overline{c_k}F(t_j-t_k)
$$
by step ⟨1⟩1. This includes repeated times and negative times without an extra sign convention.

⟨1⟩3. **Use reflection to turn the half-plane into a line.**

PROOF: T4.2 gives $\operatorname{Re}\rho\leq a$ under positivity. Applying it to $R_a(\rho)$ gives $2a-\operatorname{Re}\rho\leq a$, the reverse bound. Conversely the line condition implies the half-plane condition. The fixed-point equation is exactly $\operatorname{Re}\rho=a$. $\square$

For finite spectra the same identity holds for integrable compactly supported functions $g$, with sums over $t_j$ replaced by integrals. Indeed all exponential factors are bounded on the support, the spectral sum is finite, and expansion of the two integrals repeats step ⟨1⟩2. Infinite spectra require the additional hypotheses stated in T6.

**Theorem T4.4 (Dyson expansion as continuous ring norms).**

Hypotheses: $V=M_n(\mathbb C)$, finitely many matrices $R_1,\ldots,R_p\in M_n$, an arbitrary $K\in M_n$, and
$$
\mathcal L(x)=Kx+xK^\dagger+\sum_{j=1}^pR_jxR_j^\dagger.
$$
No trace preservation is assumed. The parameter is $t\geq0$. For $k\geq1$, $0=t_0<t_1<\cdots<t_k<t$, define the matrix
$$
A_{\boldsymbol j,\boldsymbol t}
=e^{(t-t_k)K}\prod_{h=k}^{1}
\left(R_{j_h}e^{(t_h-t_{h-1})K}\right),
$$
where the product is ordered from $h=k$ at the left to $h=1$ at the right. Thus it is $e^{(t-t_1)K}R_{j_1}e^{t_1K}$ for $k=1$, and we set $A_\varnothing=e^{tK}$ for $k=0$.

Claims:
$$
\operatorname{Tr}_{M_n}e^{t\mathcal L}
=\sum_{k=0}^\infty\ \sum_{j_1,\ldots,j_k=1}^p
\int_{0<t_1<\cdots<t_k<t}
\left|\operatorname{Tr}_{\mathbb C^n}A_{\boldsymbol j,\boldsymbol t}\right|^2
\,dt_1\cdots dt_k\geq0.
$$
The $k=0$ term is $|\operatorname{Tr}e^{tK}|^2$. The series converges absolutely. Also $\mathcal L$ commutes with $C(x)=x^\dagger$, so its spectrum is conjugation-invariant with algebraic multiplicities.

Status: `proved-here`.

⟨1⟩1. **Identify the free evolution and the Duhamel identity.**

PROOF: Let $\mathcal L_0(x)=Kx+xK^\dagger$ and $\mathcal Q=\sum_j\operatorname{Ad}(R_j)$. Differentiating $e^{tK}xe^{tK^\dagger}$ and checking its value at zero gives $e^{t\mathcal L_0}=\operatorname{Ad}(e^{tK})$. Differentiating $e^{(t-s)\mathcal L_0}e^{s\mathcal L}$ with respect to $s$ and integrating from $0$ to $t$ gives
$$
e^{t\mathcal L}=e^{t\mathcal L_0}
+\int_0^t e^{(t-s)\mathcal L_0}\mathcal Qe^{s\mathcal L}\,ds.
$$

⟨1⟩2. **Iterate with every waiting-time exponential retained.**

PROOF: Repeated substitution of the Duhamel identity yields the time-ordered products
$$
e^{(t-t_k)\mathcal L_0}\operatorname{Ad}(R_{j_k})
e^{(t_k-t_{k-1})\mathcal L_0}\cdots
\operatorname{Ad}(R_{j_1})e^{t_1\mathcal L_0}.
$$
Composition of Kraus maps multiplies their matrices in the indicated order, so each product is $\operatorname{Ad}(A_{\boldsymbol j,\boldsymbol t})$.

For convergence use a submultiplicative operator norm. Set $q_0=\sum_j\|\operatorname{Ad}(R_j)\|$. The sum of norms of all length-$k$ integrals is at most
$$
e^{t\|\mathcal L_0\|}\frac{(tq_0)^k}{k!}.
$$
Indeed the free time intervals total $t$, the simplex has volume $t^k/k!$, and summing jump norms gives $q_0^k$. The analogous remainder after $k$ substitutions is bounded by a fixed exponential in $t$ times $(t\|\mathcal Q\|)^{k+1}/(k+1)!$, so it tends to zero. Thus the series equals $e^{t\mathcal L}$ in norm.

⟨1⟩3. **Take the superoperator trace.**

PROOF: In the matrix-unit basis,
$$
\operatorname{Tr}_{M_n}\operatorname{Ad}(A)
=\sum_{a,b}(AE_{ab}A^\dagger)_{ab}
=\sum_{a,b}A_{aa}\overline{A_{bb}}
=|\operatorname{Tr}_{\mathbb C^n}A|^2.
$$
The trace is a continuous linear functional on the finite-dimensional operator space; for the Hilbert--Schmidt operator norm it is bounded by $n^2$ times that norm. The bound in step ⟨1⟩2 therefore permits termwise integration, summation, and taking the trace. This proves the formula and its nonnegativity. At $t=0$ it gives $n^2$, as required.

⟨1⟩4. **Prove conjugation symmetry.**

PROOF: Dagger sends $Kx+xK^\dagger$ to $x^\dagger K^\dagger+Kx^\dagger$, and sends $R_jxR_j^\dagger$ to $R_jx^\dagger R_j^\dagger$. Hence $C\mathcal L=\mathcal LC$. Antiunitarity and the generalized-eigenspace multiplicity argument are those proved in T3.1. $\square$

The trace here is the trace of a linear map **on $M_n$**, a space of dimension $n^2$. In vectorized notation $M_n\simeq\mathbb C^n\otimes\overline{\mathbb C^n}$. The space $M_n\otimes M_n^*$ instead represents the space of superoperators and has dimension $n^4$; it is not the domain over which this trace is taken. These continuous ring norms give neither a line reflection of the generator spectrum nor positive definiteness of every shifted, subtracted trace.

**Remark T4.5 (Hamiltonian case and the precise Hilbert--Polya claim).**

Hypotheses: $H=H^\dagger$ on a finite-dimensional Hilbert space and $\mathcal L=-i[H,\cdot]$.

Statement: if $He_a=E_ae_a$, the eigenvalue on $|e_a\rangle\langle e_b|$ is $-i(E_a-E_b)$. Every eigenvalue is purely imaginary, so with $a=0$ the line condition and the fixed-point condition hold. This is an example of the Hilbert--Polya mechanism. For a general finite-dimensional transfer generator, a presentation $L=aI+iA$ with $A$ Hermitian in some inner product requires diagonalizability as well as the line condition; T5 proves the precise equivalence. In an infinite-dimensional proposed zeta presentation one additionally needs operator-domain and spectral-realization statements. A finite Hamiltonian example supplies none of those existence statements for zeta.

Status: `proved-here` (immediate diagonal-basis computation; no additional proof requested).

## T5. The Hilbert--Polya inner product and Jordan blocks

**Proposition T5.1 (discrete unitarizability on the retained space).**

Hypotheses: $X$ acts on a finite-dimensional complex space; $S$ contains either every occurrence or no occurrence of each distinct eigenvalue of $X$; $V'$ is the sum of the generalized eigenspaces for the retained eigenvalue classes; $r>0$. Write $X'=X|_{V'}$.

Claim: the following are equivalent:

1. $X'$ is diagonalizable and all its eigenvalues have modulus $r$.
2. There is a positive definite Hermitian inner product on $V'$ for which $X'/r$ is unitary.

Status: `proved-here`.

⟨1⟩1. **Construct the inner product from an eigenbasis.**

PROOF: Under condition 1 choose an eigenbasis $v_1,\ldots,v_d$, and declare it orthonormal: $\langle\sum a_iv_i,\sum b_iv_i\rangle'=\sum_i\overline{a_i}b_i$. The diagonal entries of $X'/r$ all have modulus one, so this operator preserves the new inner product and is invertible. It is unitary.

⟨1⟩2. **Obtain an orthonormal eigenbasis from unitarity.**

PROOF: Let $U=X'/r$ be unitary for such an inner product. Any eigenvector $v$ satisfies $\|Uv\|=\|v\|$, hence its eigenvalue has modulus one. The orthogonal complement of its eigenline is invariant: if $w\perp v$, then $\langle v,Uw\rangle=\langle U^*v,w\rangle=0$, because $U^*v=U^{-1}v$ lies on the same eigenline. On the complement the restriction remains unitary. A complex matrix on a nonzero finite-dimensional space has an eigenvector, by the characteristic polynomial and a nonzero kernel at a root. Induction on the dimension therefore produces an orthonormal eigenbasis. This proves condition 1, and also handles dimension zero. $\square$

**Proposition T5.2 (continuous skew-adjoint realization).**

Hypotheses: $L$ and its retained invariant space $V'$ are defined with the same full-eigenvalue-class convention as in T5.1; $a\in\mathbb R$; $L'=L|_{V'}$.

Claim: $L'-aI$ is skew-adjoint in some positive definite Hermitian inner product if and only if $L'$ is diagonalizable and all its eigenvalues have real part $a$. Equivalently, in that inner product $L'=aI+iA$ with $A$ Hermitian.

Status: `proved-here`.

⟨1⟩1. **Use a diagonalizing basis for sufficiency.**

PROOF: Declare an eigenbasis orthonormal. The diagonal entries of $L'-aI$ are purely imaginary, so its adjoint is its negative. If $B=L'-aI$, then $A=-iB$ satisfies $A^*=A$ and $B=iA$.

⟨1⟩2. **Use skew-adjointness for necessity.**

PROOF: For an eigenvector $Bv=\beta v$, skew-adjointness makes $\langle v,Bv\rangle$ purely imaginary, so $\operatorname{Re}\beta=0$. The orthogonal complement of the eigenline is $B$-invariant because $B^*v=-Bv$ lies on that line. The restriction remains skew-adjoint. The same induction as in T5.1 yields an orthonormal eigenbasis of $B$, and hence of $L'$, proving the claim. $\square$

**Proposition T5.3 (Weil forms do not see Jordan blocks).**

Hypotheses: take $S=\varnothing$, $r>0$, and
$$
X=r\begin{pmatrix}1&1\\0&1\end{pmatrix}.
$$
For the continuous example take $a\in\mathbb R$ and
$$
L=aI+\begin{pmatrix}0&1\\0&0\end{pmatrix}.
$$

Claims: the discrete sequence is $\nu_l=2$ for every integer $l$ and is positive definite; no inner product makes $X/r$ unitary. The continuous function is $F(t)=2$ for every real $t$ and is positive definite; no inner product makes $L-aI$ skew-adjoint.

Status: `proved-here`.

⟨1⟩1. **Compute the two trace forms.**

PROOF: Each spectrum has the appropriate boundary eigenvalue twice. Thus
$$
W(c)=2\left|\sum_lc_l\right|^2,\qquad
\sum_{j,k}c_j\overline{c_k}F(t_j-t_k)=2\left|\sum_jc_j\right|^2.
$$
Both are nonnegative, and both spectra satisfy the relevant reflection invariance.

⟨1⟩2. **Exclude the desired inner products.**

PROOF: Put $N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$. Since $N^2=0$, $(X/r)^ke_2=e_2+ke_1$. In any positive definite inner product its norm is at least $k\|e_1\|-\|e_2\|$, tending to infinity. Unitarity would keep the norm equal to $\|e_2\|$, a contradiction. Similarly $e^{t(L-aI)}e_2=e_2+te_1$. If $L-aI$ were skew-adjoint, differentiation of $\|e^{t(L-aI)}v\|^2$ would give zero for every $v$, contradicting this unbounded norm. $\square$

Thus a finite spectral “RH,” meaning the circle or line condition with algebraic multiplicities, is equivalent to Weil positivity **under the relevant spectral duality**. Its equivalence with a Hilbert--Polya inner product requires semisimplicity in addition. With partial subtraction of an eigenvalue class, the multiset forms still make sense, but there is no canonical space $V'$ of the stated kind; T5 deliberately excludes that ambiguity.

## T6. The zeta instance: a conditional dictionary, not a theorem

Author: codex:gpt-6-astra

Status: `sketched` / `conditional-on H-ZD, H-ZM, H-ZEF, H-ZW` below. H-BS is the explicitly stated distributional replacement for H-B. No analytic assertion about zeta or about the compressed semigroup is proved in this section.

Use $s$ or $\rho$ for a zeta zero and $\eta$ for a generator mode, to avoid confusing the two spectral parameters. All nontrivial zeros, with both signs of the ordinate and with algebraic multiplicities, must be included. A list containing only positive ordinates is insufficient for the stated forms and constants.

**H-ZD (assumed completed-zeta analytic data).** Assume the classical analytic data for the completion used in the source note:
$$
\xi(s)=\tfrac12s(s-1)\Lambda_\zeta(s),\qquad
\Lambda_\zeta(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s).
$$
The function $\xi$ is entire and has the nontrivial zero multiset $\mathcal Z$; $\Lambda_\zeta$ has simple poles at $0,1$. Assume $\mathcal Z$ lies in $0<\operatorname{Re}\rho<1$, is invariant under $\rho\mapsto\overline\rho$ and $\rho\mapsto1-\overline\rho$, and has counting function $O(T\log(2+T))$ for $|\operatorname{Im}\rho|\leq T$. These are analytic inputs, not consequences of the finite-dimensional proofs.

**H-ZM (assumed spectral realization and distributional trace).** Assume the compressed semigroup $Z(t)$ of the source note, for $t>0$, has generator $L_Z$ with modes
$$
\eta(\rho)=-\frac{\overline\rho}{2}
=-\frac{\sigma}{2}+i\frac\gamma2,\qquad\rho=\sigma+i\gamma\in\mathcal Z,
$$
with the specified multiplicities. Also assume that its intended regularized trace is exactly the spectral distribution
$$
\tau(v)=\operatorname{Tr}_{\rm dist}Z(v)=\sum_{\rho\in\mathcal Z}e^{-v\overline\rho/2},\qquad v>0,
$$
meaning equality after testing against smooth functions of compact support in $(0,\infty)$. This equality and completeness of the asserted mode description are hypotheses about the proposed model, not consequences of listing its eigenvalues. The source's formula for $Z(t)^*$ has the conjugate frequency; the present convention is the one specified in the question for $Z(t)$ itself.

**Dictionary T6.1 (generator, reflection, and trivial terms).**

⟨1⟩1. **Center at the single desired decay rate.**

PROOF (formal algebra, conditional on H-ZM): Set $a=-1/4$. Then
$$
\eta(\rho)-a=\frac{1/2-\overline\rho}{2},\qquad
\operatorname{Re}\eta(\rho)=a\quad\Longleftrightarrow\quad\sigma=\frac12.
$$
The one-sided condition of T4.2 would be $-\sigma/2\leq-1/4$, namely $\sigma\geq1/2$. Zeta reflection supplies the other inequality; the direction of this one-sided inequality is important.

⟨1⟩2. **Transport the reflection.**

PROOF (algebra): For $j_\zeta(\rho)=1-\overline\rho$,
$$
\eta(j_\zeta(\rho))=-\frac{1-\rho}{2}
=-\frac12-\overline{\eta(\rho)}
=2a-\overline{\eta(\rho)}.
$$
Thus the generator reflection is $\eta\mapsto-1/2-\overline\eta$, whose fixed line is $\operatorname{Re}\eta=-1/4$.

⟨1⟩3. **Correct the proposed trivial sub-multiset.**

PROOF (bookkeeping under H-ZD and H-ZM): The displayed $\xi$ has no poles at $0,1$. Its prefactor removes the poles of $\Lambda_\zeta$. The actual model in H-ZM has only modes indexed by $\mathcal Z$, so its trivial sub-multiset for this dictionary is $S=\varnothing$. The two positive endpoint terms in the explicit formula come from the poles of $\Lambda_\zeta$, not from two asserted eigenmodes of this $Z$.

One may *artificially augment* the formal spectrum by $\eta(0)=0$ and $\eta(1)=-1/2$, each once, and then take $S=\{0,-1/2\}$ to remove them. They form a reflection pair about $a=-1/4$. This auxiliary convention gives the same retained zero modes, but is an added construction, not a spectral fact about $Z$. The archimedean Gamma contribution remains a separate geometric-side distribution, not a list of discrete modes in this completion convention.

**H-BS (Bochner--Schwartz theorem, positive-type distribution version; exact statement).** “Let $K\in\mathcal D'(\mathbb R)$ and put $\widetilde g(t)=\overline{g(-t)}$ for $g\in C_c^\infty(\mathbb R)$. The condition
$$
\langle K,g*\widetilde g\rangle\geq0\qquad(g\in C_c^\infty(\mathbb R))
$$
holds if and only if there is a positive Borel measure $m$ of at most polynomial growth such that
$$
\langle K,h\rangle=\int_{\mathbb R}\left(\int_{\mathbb R}h(v)e^{iv\xi}\,dv\right)dm(\xi)
\qquad(h\in C_c^\infty(\mathbb R)).
$$
Such a distribution is tempered. Here ‘at most polynomial growth’ means that $\int(1+|\xi|)^{-N}\,dm(\xi)<\infty$ for some $N$.”

Pairings with distributions are linear in the test function in this convention. A temperedness assumption on an off-line zero sum must not silently be borrowed from the finite-dimensional Bochner theorem; H-BS concerns distributions of positive type and gives temperedness as a conclusion.

**Dictionary T6.2 (test transform and the exact formal autocorrelation).**

Take $g\in C_c^\infty(\mathbb R)$ and define the holomorphic, centered transform with the required factor of two:
$$
\widehat g_\zeta(s)=\int_{\mathbb R}g(t)e^{(s-1/2)t/2}\,dt.
$$
In this section the symbol $\widehat g$ in the question must mean this transform if the time variable of $Z$ is retained. It is neither the uncentered Laplace transform nor the transform with exponent $(s-1/2)t$. Define
$$
\varphi_g(v)=(g*\widetilde g)(v)=\int_{\mathbb R}g(s+v)\overline{g(s)}\,ds,
\qquad
\mathcal K(v)=\sum_{\rho\in\mathcal Z}e^{(\rho-1/2)v/2}
$$
as a distributional sum.

⟨1⟩1. **Make the spectral testing meaningful under H-ZD.**

PROOF (conditional): Integration by parts in a compactly supported smooth test gives, for every $M$, decay $O((1+|\operatorname{Im}\rho|)^{-M})$ for its exponential transform, uniformly for $0\leq\operatorname{Re}\rho\leq1$. The boundary terms vanish and derivatives of $e^{(\operatorname{Re}\rho-1/2)v/2}$ are uniformly bounded on the fixed support. H-ZD's counting bound makes the tested spectral series absolutely summable, and the resulting bounds in test-function seminorms define an element of $\mathcal D'(\mathbb R)$. The same estimates give absolute convergence of the pairing below. They do not assert an ordinary trace at any single time.

⟨1⟩2. **Relate $\mathcal K$ to the positive-time trace and prescribe negative time.**

PROOF (conditional): By reflection invariance and H-ZM, on $v>0$,
$$
\mathcal K(v)=\sum_\rho e^{(1/2-\overline\rho)v/2}
=e^{v/4}\tau(v).
$$
Reflection also gives $\mathcal K(-v)=\overline{\mathcal K(v)}$ distributionally. Conjugation invariance separately makes $\mathcal K$ real and even. The full-line distribution is defined by the spectral test formula, which fixes its behavior at zero as well; an extension from two open half-lines alone could leave distributions supported at zero undetermined.

For the formal full-line notation in the question, define
$$
\tau(v):=e^{-v/4}\mathcal K(v)\qquad(v\in\mathbb R)
$$
as a distribution. In particular, for $u>0$ it obeys
$$
\tau(-u)=e^{u/2}\overline{\tau(u)}.
$$
This is a reflected, exponentially weighted extension. It does **not** assert that $Z(-u)$ exists as a bounded inverse semigroup, and it is not the naive extension $\tau(-u)=\overline{\tau(u)}$.

⟨1⟩3. **Derive the exact pairing identity.**

PROOF (conditional, with justified spectral testing as in step ⟨1⟩1): For each zero,
$$
\begin{aligned}
\widehat g_\zeta(\rho)\overline{\widehat g_\zeta(1-\overline\rho)}
&=\int\!\int g(t)\overline{g(s)}
e^{(\rho-1/2)t/2}e^{-(\rho-1/2)s/2}\,dt\,ds\\
&=\int\varphi_g(v)e^{(\rho-1/2)v/2}\,dv.
\end{aligned}
$$
Summing gives the precise distributional interpretation of the requested identity:
$$
\boxed{
\sum_{\rho\in\mathcal Z}\widehat g_\zeta(\rho)
\overline{\widehat g_\zeta(1-\overline\rho)}
=\langle\mathcal K,\varphi_g\rangle
=\int\!\int g(t)\overline{g(s)}e^{(t-s)/4}
\operatorname{Tr}_{\rm dist}Z(t-s)\,dt\,ds .}
$$
The final double integral denotes $\langle e^{v/4}\tau(v),\varphi_g(v)\rangle$; it is not an asserted pointwise integral of a trace-class semigroup.

⟨1⟩4. **Check compatibility with the literal transform in T4.3.**

PROOF (algebra): Its transform on generator modes is
$$
\widehat g_L(\eta(\rho))=\int g(t)e^{t(1/2-\overline\rho)/2}\,dt
=\widehat g_\zeta(1-\overline\rho).
$$
Thus the generator pairing is
$\sum_\rho\widehat g_\zeta(1-\overline\rho)\overline{\widehat g_\zeta(\rho)}$.
Reindexing by $\rho\mapsto1-\overline\rho$ gives exactly the left-hand side in step ⟨1⟩3. This accounts for both the conjugation in $\eta=-\overline\rho/2$ and the half-time scaling. For a Mellin convention, the same transform is $\int_0^\infty h(x)x^{s-1}\,dx$ with $h(x)=2x^{-1/2}g(2\log x)$.

**H-ZEF (assumed explicit formula in this normalization).** For every $h\in C_c^\infty(\mathbb R)$, put $H_h(s)=\int h(v)e^{(s-1/2)v/2}\,dv$ and assume
$$
\begin{aligned}
\sum_{\rho\in\mathcal Z}H_h(\rho)
={}&H_h(0)+H_h(1)-2(\log\pi)h(0)\\
&+\frac1{2\pi}\int_{\mathbb R}H_h(1/2+iy)
\operatorname{Re}\psi(1/4+iy/2)\,dy\\
&-2\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}
\big[h(2\log n)+h(-2\log n)\big],
\end{aligned}
$$
where $\psi=\Gamma'/\Gamma$ and $\Lambda(n)$ is the von Mangoldt function, distinct from the completed function $\Lambda_\zeta$. This is an explicit analytic input, not a result proved here. The prime sum is finite on each compactly supported test. Assume the Gamma integral has the usual convergent test-function interpretation displayed above.

**Dictionary T6.3 (where the prime and Gamma terms actually sit).**

⟨1⟩1. **Identify all pieces of the trace distribution.**

PROOF (bookkeeping under H-ZEF): In distribution notation, the formula says
$$
\mathcal K(v)=2\cosh(v/4)-2(\log\pi)\delta_0(v)+\mathcal A_\Gamma(v)
-2\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}
\big[\delta_{2\log n}(v)+\delta_{-2\log n}(v)\big],
$$
where $\langle\mathcal A_\Gamma,h\rangle$ is exactly the Gamma integral in H-ZEF. The first term is the endpoint contribution, since $H_h(0)+H_h(1)=\int h(v)2\cosh(v/4)\,dv$. The Gamma integral and the displayed contact term are archimedean contributions, not discrete modes of $L_Z$.

⟨1⟩2. **Verify the prime signs and the factor from $v=2u$.**

PROOF (change of variables, conditional on the explicit formula): If the undoubled time test is $q(u)=2h(2u)$, then $\int q(u)e^{(s-1/2)u}\,du=H_h(s)$. Its prime term
$-\sum_{n\geq2}\Lambda(n)n^{-1/2}[q(\log n)+q(-\log n)]$
becomes the final line of H-ZEF, and $-(\log\pi)q(0)$ becomes $-2(\log\pi)h(0)$. This fixes the signs and the factors of two. On positive times, multiplying the prime part of $\mathcal K$ by $e^{-v/4}$ gives the prime part of $\tau$:
$$
\tau_{\rm prime}(v)=-2\sum_{n\geq2}\frac{\Lambda(n)}n\delta_{2\log n}(v),\qquad v>0.
$$
The full trace therefore is not a nonnegative pure prime-atom measure, and it is not supported only at prime-power lengths: endpoint and archimedean terms also occur. Even the prime atoms have negative coefficients on the zero-sum side of this explicit formula. The positive arithmetic weights can be moved to the other side of the identity, but this operation does not identify the full trace with a nonnegative Kraus ring count.

**H-ZW (the Weil converse supplied as an analytic input).** For the zero multiset and the test class above, assume the converse assertion in Weil's criterion: if
$$
\sum_{\rho\in\mathcal Z}\widehat g_\zeta(\rho)
\overline{\widehat g_\zeta(1-\overline\rho)}\geq0
\quad\text{for every }g\in C_c^\infty(\mathbb R),
$$
then every $\rho\in\mathcal Z$ has real part $1/2$. Equivalently, any off-line zero admits a test in this class giving a negative total pairing. This infinite-spectrum separation assertion is not established by the finite interpolation in T2.2 and is not a consequence claimed here from Bochner--Schwartz alone.

**Dictionary T6.4 (what is conditional and what a rigorous realization needs).**

⟨1⟩1. **Read positivity as a distributional spectral statement.**

PROOF (conditional): Under the line condition the pairing is $\sum_\rho|\widehat g_\zeta(\rho)|^2\geq0$, with convergence under H-ZD. The frequency measure is
$\sum_{\rho\in\mathcal Z}\delta_{\operatorname{Im}\rho/2}$, with multiplicities, which has polynomial growth under H-ZD. H-BS gives the distributional positivity language. The reverse implication is precisely the unproved input H-ZW. Thus, with that input, the formal dictionary reads
$$
\mathrm{RH}\quad\Longleftrightarrow\quad
\mathcal K\text{ is a distribution of positive type}
\quad\Longleftrightarrow\quad
\text{the displayed Weil pairings are nonnegative}.
$$
It is not legitimate to use the finite boundedness proof with $F(0)=\#\mathcal Z$, which is infinite, or to interpolate away infinitely many unwanted modes by a finite polynomial.

⟨1⟩2. **State the remaining analytic requirements.**

PROOF (scope audit): H-ZD supplies a test space and convergence; H-ZEF supplies the arithmetic evaluation, including all endpoint, Gamma, and contact terms; H-ZM supplies the asserted link to the particular compressed semigroup; and H-ZW supplies the infinite-dimensional converse. Verifying those inputs would make the corresponding distributional identities and equivalence rigorous. A further Hilbert--Polya conclusion would require a suitable spectral realization by a self-adjoint operator, with its domain and multiplicities specified; a mode list alone is insufficient. None of these analytic verifications is attempted here. For the asserted infinitely many semigroup eigenmodes, the moduli at a fixed $t>0$ satisfy $|e^{t\eta(\rho)}|=e^{-t\operatorname{Re}\rho/2}\geq e^{-t/2}$; they cannot be an absolutely summable trace-class eigenvalue list. Distributional testing is essential, and no bounded negative-time operator has been assumed.

## T7. CORRECTION LEDGER and what is established

Author: codex:gpt-6-astra

Every substantive change to a drafted statement or to the contextual identification used by that statement is recorded here. Added proof details that leave a claim unchanged are distinguished from corrections.

| Draft item | Correction or necessary qualification | Reason and location |
|---|---|---|
| T1, including a zero outside $S$ | The assertion is true as drafted. Specify $0^0=1$, $P_0=1$, and its contribution $\sum_l\lvert c_l\rvert^2$. | T1.1--T1.3 prove the exact claim; no exclusion of zero or semisimplicity is needed. |
| T2(a),(b) | The assertions are true with multiplicity-preserving $J$-invariance of the **retained** multiset. Orbit contributions include their common multiplicity. | T2.1--T2.2. Interpolating zero at every other distinct retained value is necessary to infer negativity of the entire form from one off-circle pair. |
| T2(c), “linear map” | $\mu\mapsto r^2/\mu$ is a holomorphic reciprocal map, not a linear map. The circle criterion needs only this symmetry; $W=M$ additionally follows from conjugation symmetry. | T2.3 proves both claims and gives a reciprocal-only example with $W\neq M$. |
| T3(a), conjugation symmetry | Strengthened: conjugation symmetry holds for **every** Kraus family, not just an adjoint-paired one. The cyclic ring formula quoted from the notebook has $l\geq1$. | T3.1; H-QT. The antiunitary is defined componentwise to make its antilinearity on $W$ unambiguous. |
| T3(b), requested inverse-Kraus counterexample to conjugation closure | No such example exists. The stated “if and only if” is true for arbitrary inverse-paired superoperators; in the Kraus case both spectra are always conjugation-invariant. | T3.2 supplies the proof and a scalar counterexample only in the larger, non-Kraus superoperator class. |
| T3(b), double roots and subtraction | Specify $k=N(D-2)/2$, $2N$ retained roots, $2a_\alpha$ copies at $\alpha=\pm2\sqrt{D-1}$, and extra $\pm1$ copies from $\alpha=\pm D$. | T3.2. A root of the determinant does not determine Jordan structure. Fixed-point-free reversal makes $D$ even, so $D\geq3$ here means $D\geq4$. |
| T3(c), “both iff nonzero scalar multiple of a unitary”; $B^\dagger B$ merely scalar | False for exact matrix pairing and false for exact superoperator pairing. Replace by $B^\dagger B=I$, hence actual unitarity. Scalar $B^\dagger B$ characterizes only a projective equality with the explicit factor $\kappa$. | T3.3; $B=2I$ directly disproves the draft. |
| T3(d), unitary-up-to-scalar families with the unmodified $r,\Phi,S$ | Replace by actual unitary, adjoint-paired families. Arbitrary scalar magnitudes change the transfer operator, its radius, its trivial roots, and its channel normalization. | T3.4 also states the corrected common-scale version. General unequal scales need not preserve the quadratic duality. |
| T3(d), $S_0$ union with the channel-trivial pairs | Interpret the union as addition of multiplicities and remove the pairs for **all** occurrences of $\lambda=\pm1$. | T3.4: $\lvert A\rvert=2(N-d_+-d_-)$; multiplicities of $\pm1$ in $T$ are $k+d_\pm$. No simplicity or mixing assumption is added. |
| T3(e), “has no partner to refer to” | Replace the literal wording: reflection exists on the punctured plane but need not take a mode to another retained mode. The fixed-point assertion is still meaningful, but is not equivalent to Weil positivity without duality. | T2's closing paragraph and T3.5. A concrete non-scalar-unitary $n=2,D=4$ example excludes every nonzero reciprocal constant on its explicitly specified retained multiset. An $n=1$ matrix could not satisfy the requested non-scalar-unitary premise. |
| T4(a),(b) | The finite assertions are true as drafted once the centered transform, Fourier normalization, and Hermitian extension are explicit. | T4.1--T4.3 compute all signs and use continuous mean-square growth. There is no differentiability assertion at $t=0$. |
| T4(c), the Dyson product | Every interval between jumps must contain its free propagator $e^{(t_{j+1}-t_j)K}$. The draft's product, if read literally without these factors, is false for noncommuting $K,R_j$. | T4.4 supplies the full time-ordered product, the $k=0$ term, a finite jump-list hypothesis, and absolute convergence. |
| T4(c), trace subscript $M_n\otimes M_n^*$ | The intended superoperator trace is $\operatorname{Tr}_{M_n}$, equivalently a trace on $\mathbb C^n\otimes\overline{\mathbb C^n}$. | $M_n\otimes M_n^*$ has dimension $n^4$ and is the space of superoperators, not the $n^2$-dimensional state space on which $e^{t\mathcal L}$ acts. |
| T4(d), Hamiltonian and Hilbert--Polya wording | Require $H=H^\dagger$. A scalar-plus-$i$-Hermitian presentation requires diagonalizability in the finite case and further realization/domain information in the infinite case. | T4.5 and T5. It is an existence mechanism, not a consequence of the line condition alone for arbitrary operators. |
| T5, “RH iff Weil positivity” | Qualify by the relevant duality. The inner-product equivalences themselves are true with the full-eigenvalue-class hypothesis already requested. | T5.1--T5.3 prove the statements; explicit Jordan blocks distinguish spectral location from unitarizability/skew-adjointness. |
| T6, poles of $\xi$ and two trivial modes of $Z$ | The $\xi$ defined in the source is entire. The poles at $0,1$ belong to $\Lambda_\zeta$. For the stated zero-mode semigroup take $S=\varnothing$; $\{0,-1/2\}$ can be removed only after an explicitly artificial spectral augmentation. | H-ZD, H-ZM, T6.1. Endpoint terms on the explicit-formula side are not automatically eigenmodes. |
| T6, Gamma terms | Keep the Gamma integral and its normalization/contact terms on the geometric side, not as discrete zero modes. | H-ZEF and T6.3 give their exact placement for this completion convention. |
| T6, transform and reflection | Use $\eta=-\overline\rho/2$, $a=-1/4$, reflection $\eta\mapsto-1/2-\overline\eta$, and $\widehat g_\zeta(s)=\int g(t)e^{(s-1/2)t/2}dt$. | T6.1--T6.2. The literal generator transform is the zeta transform at the reflected zero; reindexing proves the identity. An unspecified Mellin/Laplace normalization would hide a sign or factor of two. |
| T6, $\operatorname{Tr}Z(t-s)$ for negative differences | Define the full-line trace distribution spectrally, with $\tau(-u)=e^{u/2}\overline{\tau(u)}$, and interpret the double integral as a distributional autocorrelation pairing. | A forward semigroup does not supply negative-time bounded operators; even the naive conjugate extension of the uncentered trace has the wrong exponential factor. The spectral test convention fixes contact terms at zero. |
| T6 and contextual section 5, trace “supported at prime lengths with positive weights” | False for the full zero trace in the displayed explicit formula. There are endpoint and archimedean distributions; the prime part of the centered trace is $-2\Lambda(n)/\sqrt n$ at each of $\pm2\log n$, and the positive-time uncentered prime part is $-2\Lambda(n)/n$. | T6.3 derives the sign and factor from the explicitly fixed transform convention. Positive prime weights on the opposite side of an identity are not a proof that the full trace is a nonnegative ring measure. |
| T6, finite-to-infinite passage | Add test-space convergence, a distributional trace-realization hypothesis, the complete explicit formula, and an infinite Weil-converse input. | H-ZD, H-ZM, H-ZEF, H-ZW. H-BS replaces Bochner, but the finite growth and interpolation proofs do not establish the infinite converse. |
| Opening scope, nonnegative side A for every arbitrary transfer family | Nonnegative ring traces hold in the stated Kraus settings; they are not a property of arbitrary superoperators, and are distinct from Weil positive definiteness even when available. | T3's closing observation, T3.4, and T4.4. The one-sided theorems themselves need no positive ring-count premise. |

The explicit H-* inputs introduced are:

| Label | Exact role and status |
|---|---|
| H-P | Standard Poisson-kernel Fourier series, also proved in T1.1. |
| H-H | Standard Herglotz theorem, stated for comparison; its existence/converse is not needed by the finite proofs. |
| H-QT | Already-proved local notebook Corollary 2, quoted for the discrete Kraus ring trace. |
| H-QI | Already-proved local notebook Corollary 3, quoted for the inverse-paired determinant identity. |
| H-B | Standard Bochner theorem, stated with the chosen Fourier sign; the required finite-mode positive representations are constructed explicitly. |
| H-BS | Standard Bochner--Schwartz theorem in its positive-type distribution form, used only in the conditional zeta dictionary. |
| H-ZD | Unproved-here completed-zeta analytic data, symmetries, strip and counting bound; sufficient for the displayed compact-test spectral convergence. |
| H-ZM | Unproved-here generator-mode realization and identification of its regularized trace with the spectral distribution. |
| H-ZEF | Unproved-here explicit formula, stated in full in the time normalization used here. |
| H-ZW | Unproved-here infinite Weil converse for the declared test class; no finite theorem in this file replaces it. |

**RESULT:** T1.1--T1.3, T2.1--T2.3, T3.1--T3.5, T4.1--T4.4, and T5.1--T5.3 are `proved-here`; T4.5 is the stated elementary Hamiltonian remark. The finite result is positivity $\Longleftrightarrow$ a disk/half-plane bound, strengthened to a circle/line under the stated retained-spectrum duality. A Hilbert--Polya inner product additionally requires semisimplicity. T6 is a `sketched`, conditional dictionary on H-ZD, H-ZM, H-ZEF, and H-ZW, using H-BS; it proves no zeta theorem, no RH assertion, and no new spectral realization of the proposed compressed semigroup.
