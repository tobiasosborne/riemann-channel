# Continuous transfer operators, Selberg zeta, and the modular prime comb

Author: codex:gpt-6-astra

Date: 2026-09-12. This file is a proof submission, not an independent review receipt. The tag `proved-here` means that the argument is supplied here; it does not mean the notebook's externally reviewed tag `proved`. No external sources were fetched or byte-checked. Named standard facts below are explicit inputs awaiting citations, not claims of completed provenance verification.

**H-BASE (standard, to be cited; foundational background).** We use completeness and smooth Fourier inversion for the circle Fourier basis; Fourier transformation and inversion on Schwartz functions and tempered distributions; the trace-class criterion for an absolutely summable diagonal operator; the Hilbert–Schmidt tensor identification's elementary Hilbert-space completion facts; ordinary change of variables, integration by parts, dominated convergence, and elementary holomorphic series/product theory; the differential of Lie-group conjugation; and the Haar-measure criterion that a connected Lie group with $\det\operatorname{Ad}(g)=1$ is unimodular, with its bi-invariant volume descending to a discrete left quotient. The specific Poisson formula, tensor-action formula, brackets, and convergence estimates needed here are proved below. Every `proved-here` status is relative to these stated elementary foundations. A `conditional-on` status names the additional geometric, spectral, or analytic input used in that result.

Conventions throughout: $\mathbb H$ has metric $y^{-2}(dx^2+dy^2)$ and positive Laplacian $\Delta=-y^2(\partial_x^2+\partial_y^2)$. In the compact-surface statements, $\Gamma< G=\operatorname{PSL}(2,\mathbb R)$ is discrete, torsion-free, and cocompact; $Y=\Gamma\backslash\mathbb H$ is connected of genus $g\ge2$, and $M=\Gamma\backslash G$. Torsion-freeness is an additional necessary hypothesis for the stated surface zero divisor: the orbifold case has additional elliptic terms. Put $K=\operatorname{PSO}(2)$ and $a_t=\operatorname{diag}(e^{t/2},e^{-t/2})$. A primitive $\gamma$ means a primitive periodic orbit of the oriented geodesic flow, equivalently a primitive hyperbolic conjugacy class in $\Gamma$. Opposite directions are not identified. The orbit index in every Selberg product and trace hypothesis below is this same index, so no orientation factor is introduced between formulas.

For Schwartz functions, use
$$
\widehat h(r)=\int_{\mathbb R}e^{-irt}h(t)\,dt,
\qquad
\mathcal F^{-1}b(t)=\frac1{2\pi}\int_{\mathbb R}e^{irt}b(r)\,dr.
$$
Distributional pairings are complex linear, without complex conjugation. Thus $\mathcal F^{-1}(e^{-ira})=\delta_a$ and $\mathcal F^{-1}\delta_0=1/(2\pi)$. A prime-power weight is denoted $\Lambda_{\mathrm{vM}}(n)$ to distinguish it from the flat-trace Laplace transform $\Lambda_{\mathrm{fl}}(\sigma)$. The Selberg zeta is $Z_{\mathrm{Sel}}(s)$; the notebook's compressed semigroup is $Z_{\mathrm{ch}}(t)$.

## T1. Circle comb and finite Euler products

### Proposition T1.1 — One circle has a distributional trace

**Hypotheses.** $L>0$ and $U_t v(x)=v(x+t)$ on $\mathcal H_L=L^2(\mathbb R/L\mathbb Z,dx)$. The Fourier basis and elementary Fourier inversion on the circle are the only background facts; the required Poisson identity, trace-class assertion, and generator computation are **proved here**. The statement is about smeared traces, not an ordinary trace of the unitary $U_t$.

**Statement.** For every $h\in\mathcal S(\mathbb R)$ the strong integral $U(h)=\int h(t)U_t\,dt$ is trace class, and
$$
\operatorname{Tr}U(h)
=\sum_{n\in\mathbb Z}\widehat h(-2\pi n/L)
=L\sum_{k\in\mathbb Z}h(kL).
$$
Consequently $\operatorname{Tr}_{\mathrm{dist}}U_t=L\sum_{k\in\mathbb Z}\delta(t-kL)$ in $\mathcal S'(\mathbb R)$.

<1>1. **Diagonalization of the smeared operator.**

PROOF. The orthonormal basis $e_n(x)=L^{-1/2}e^{2\pi inx/L}$ satisfies $U_te_n=e^{2\pi int/L}e_n$. Since $\int|h(t)|dt<\infty$, the strong integral exists and is bounded by $\|h\|_1$. Its eigenvalue on $e_n$ is $\widehat h(-2\pi n/L)$. Repeated integration by parts bounds these eigenvalues by $C_N(1+|n|)^{-N}$ for every $N$. Their absolute sum is finite, which proves trace class and the first trace formula. $\square$

<1>2. **Poisson identity with its normalization.**

PROOF. The periodization $P_h(x)=\sum_{k\in\mathbb Z}h(x+kL)$ and all its derivatives converge uniformly on $[0,L]$. Its $n$th Fourier coefficient is $L^{-1}\widehat h(2\pi n/L)$, by integration over the disjoint translated intervals. The coefficients decay rapidly, so evaluating the absolutely convergent Fourier series at $x=0$ gives $\sum_k h(kL)=L^{-1}\sum_n\widehat h(2\pi n/L)$. Reindex $n\mapsto-n$ and use <1>1. $\square$

<1>3. **Continuity on Schwartz space.**

PROOF. For any fixed $N>1$, $\sum_k|h(kL)|\le \sup_t(1+|t|)^N|h(t)|\sum_k(1+|kL|)^{-N}$. This is a Schwartz seminorm bound, proving the asserted tempered-distribution interpretation. $\square$

**Status:** `proved-here`.

### Proposition T1.2 — The prime circles give a local orbital trace, not a Hilbert-space trace

**Hypotheses.** The circles have lengths $L_p=\log p$ for all primes $p$; the direct-sum group is $U_t^{\mathcal P}=\bigoplus_p U_t^{(p)}$. Proposition T1.1 and unique prime factorization are used; all further claims in this proposition are **proved here**. Define the positive-time *orbital trace* by locally summing the component distributional traces.

**Statement.** In $\mathcal D'((0,\infty))$,
$$
\operatorname{Tr}_{\mathrm{orb}}U_t^{\mathcal P}
=\sum_p\sum_{k\ge1}\log p\,\delta(t-k\log p)
=\sum_{n\ge2}\Lambda_{\mathrm{vM}}(n)\,\delta(t-\log n).
$$
This is not, in general, the trace of a trace-class operator obtained by smearing the infinite direct sum. Unlike the single-circle comb, the positive prime comb, extended by zero to negative times, is not tempered.

<1>1. **Local existence and regrouping.**

PROOF. If $h\in C_c^\infty((0,\infty))$ has support in $[a,b]$ with $a>0$, a nonzero term requires $p^k\le e^b$. There are only finitely many such pairs. Thus $\sum_p\operatorname{Tr}U^{(p)}(h)$ is a finite scalar sum, although the component operators themselves need not vanish. Unique factorization identifies the weight at $\log n$ as $\log p$ when $n=p^k$, and as zero otherwise. On each compact time interval this is a finite measure, hence a distribution. $\square$

<1>2. **Failure of trace class for the infinite direct sum.**

PROOF. Take a nonnegative, nonzero $h\in C_c^\infty((0,\infty))$. Every circle has a constant unit vector on which its smeared operator has eigenvalue $\int h>0$. These vectors are mutually orthogonal in the direct sum. The smeared direct-sum operator therefore has a nonzero eigenvalue of infinite multiplicity and is not compact, hence not trace class. For $\log p>b$, the scalar trace of that component is nevertheless zero by T1.1, owing to cancellation between Fourier modes. The finite scalar sum of traces in <1>1 must not be exchanged for an operator trace. At $t=0$ even the orbital sum has the divergent coefficient $\sum_p\log p$. $\square$

<1>3. **The positive prime comb is not tempered.**

PROOF. A positive tempered measure has polynomial mass growth: apply its Schwartz seminorm bound to a fixed nonnegative cutoff equal to one on $[-1,1]$, dilated to $[-R,R]$. Polynomial mass growth implies integrability against $(1+|t|)^{-N}$ for some sufficiently large $N$, by dyadic decomposition. Here, for every $N$, the contribution of primes alone is
$$
\sum_p\frac{\log p}{(1+\log p)^N}=\infty,
$$
because its summands are at least $1/p$ for all sufficiently large $p$. For completeness, $\sum_p1/p=\infty$: if it converged, then $\prod_{p\le x}(1-1/p)^{-1}$ would stay bounded, since $-\log(1-1/p)\le 2/p$. Its expansion contains $\sum_{n\le x}1/n$, which is unbounded. This contradiction proves the claim. Thus the correct positive-time setting is local distributions, not a globally tempered prime trace. $\square$

**Status:** `proved-here` — corrected trace interpretation.

### Proposition T1.3 — Finite-prime spectrum and Euler poles

**Hypotheses.** $S$ is a finite set of primes, possibly empty. The generator is $A_S=\left.\frac d{dt}\right|_{t=0}U_t^S$, so $A_p=\partial_x$ with periodic Sobolev domain $H^1(\mathbb R/(\log p)\mathbb Z)$. The diagonal spectral computation and finite-product zero-freeness are **proved here**. Only for the additional literal disjointness from the zeros of the continued Riemann zeta, use H-ZETA and H-GAMMA (**standard, to be cited**, stated in T5.1).

**Statement.** As a set,
$$
\operatorname{spec}(A_S)
=\bigcup_{p\in S}\frac{2\pi i}{\log p}\mathbb Z
=\operatorname{Poles}\!\left(\prod_{p\in S}(1-p^{-s})^{-1}\right).
$$
The variable $s$ in this equality is the complex spectral parameter of the anti-self-adjoint generator $A_S$ itself, not a real frequency. The finite Euler product has no zeros anywhere in $\mathbb C$. Under the stated zeta/gamma inputs, $\operatorname{spec}(A_S)$ is also disjoint from the zero set of the continued Riemann zeta.

<1>1. **No missing spectrum.**

PROOF. In the Fourier basis the generator is the diagonal operator with entries $2\pi in/\log p$ and domain given by square summability after multiplication by these entries. Each finite union of these lattices is closed and has no finite accumulation point. If $z$ lies outside it, the diagonal operator with entries $(z-2\pi in/\log p)^{-1}$ is bounded and maps onto the generator domain; it is the resolvent $(z-A_S)^{-1}$. Each lattice point is an eigenvalue. This proves the spectrum equality, including the empty case. $\square$

<1>2. **Euler-product singularities and multiplicities.**

PROOF. $1-p^{-s}=0$ exactly when $s\log p\in2\pi i\mathbb Z$, and its derivative there is $\log p\ne0$. The product has numerator one, so all these singularities are poles without cancellation, and it has no zeros. At $s=0$ the pole order and generator multiplicity both equal $|S|$. Nonzero lattices for different primes do not intersect: an intersection would imply $\log p/\log q\in\mathbb Q$ and hence $p^a=q^b$ for positive integers $a,b$, impossible for distinct primes. Thus all nonzero poles and eigenvalues are simple. $\square$

<1>3. **Meaning of “blind to zeros.”**

PROOF. Every spectral point just computed is a pole of a zero-free finite meromorphic Euler product. No zero is produced by that finite construction. For the literal disjointness assertion, H-ZETA gives $\zeta(iv)=\chi(iv)\zeta(1-iv)\ne0$ for real $v\ne0$: the second factor is nonzero by the zero-free-line input, and the gamma quotient in $\chi(iv)$ is finite and nonzero by H-GAMMA. At $v=0$, H-ZETA gives $\zeta(0)=-1/2$. Thus there are no Riemann zeta zeros on the imaginary axis containing the entire finite-prime spectrum. Passing to the infinite Euler product and analytically continuing is a different operation; the finite-prime calculation does not recover its zeros. In particular a first-order translation generator is anti-self-adjoint and is not a dissipative sum-of-squares generator merely because it generates a flow. $\square$

**Status:** finite spectrum/pole equality and finite-product zero-freeness `proved-here`; disjointness from the continued Riemann zeta zero set `conditional-on H-ZETA, H-GAMMA`.

## T2. Lindblad double commutators, the Casimir, and the Laplacian

### Proposition T2.1 — Multiplication observables see a sum of squares

**Hypotheses.** A finite family of real smooth vector fields $X_1,\ldots,X_d$ acts as derivations on a smooth function $*$-algebra. On a common invariant dense test domain $\mathcal D\subset L^2(N,\mu)$, multiplication $M_f$, all derivatives in the formulas, and their compositions are defined. For formal self-adjointness of $L_j=-iX_j$, assume $\operatorname{div}_\mu X_j=0$ and use compactly supported test functions or boundary conditions that remove boundary terms. These domain/volume assumptions are part of the statement; the algebra and integration-by-parts assertion are **proved here**. No theorem about an unbounded completely positive semigroup is assumed or asserted.

**Statement.** On $\mathcal D$ the Heisenberg expression is
$$
\mathcal L(M_f)
=\sum_j\left(L_jM_fL_j-\tfrac12L_j^2M_f-\tfrac12M_fL_j^2\right)
=-\tfrac12\sum_j[L_j,[L_j,M_f]]
=M_{\frac12\sum_jX_j^2f}.
$$

<1>1. **The first commutator is multiplication.**

PROOF. Leibniz's rule gives $[X_j,M_f]v=(X_jf)v$ for $v\in\mathcal D$. Therefore $[L_j,M_f]=-iM_{X_jf}$ and
$$
[L_j,[L_j,M_f]]=(-i)^2M_{X_j^2f}=-M_{X_j^2f}.
$$
$\square$

<1>2. **Expansion and sign.**

PROOF. Direct expansion gives $[L,[L,M]]=L^2M-2LML+ML^2$. Multiply by $-1/2$ and use <1>1, then sum over $j$. Notice the plus sign in $\frac12\sum X_j^2$: the real vector fields themselves are formally anti-self-adjoint. $\square$

<1>3. **The adjoint qualification.**

PROOF. Integration of $X_j(\overline u v)$ against a preserved volume gives zero, hence $\langle X_ju,v\rangle=-\langle u,X_jv\rangle$ on the test domain. Consequently $-iX_j$ is symmetric there. Symmetry alone is not a claim of self-adjointness or a construction of a closed Lindblad generator. If the flows are complete, their unitary groups supply skew-adjoint generators; that standard operator-theoretic realization is an additional input when needed. $\square$

**Status:** `proved-here` on the stated common domain.

### Proposition T2.2 — The exact compact-surface normalization is $-2\Delta$

**Hypotheses.** Use the surface and group conventions above, and the *left-invariant* differential field
$$
Bf(g)=\left.\frac d{du}\right|_{u=0}f(g\exp(uB)).
$$
Thus its flow is right multiplication. Use
$$
H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
E=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
W=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
\Omega=\tfrac14(H^2+E^2-W^2).
$$
The Möbius action and the identification $G/K=\mathbb H$ are the specified geometric model. All differential identities below, centrality of $\Omega$, and preservation of right-$K$-invariance are **proved here**. For a closed-semigroup interpretation only, use **H-AN (standard, to be cited):** complete volume-preserving flows have their skew-adjoint unitary generators, and the positive Laplacian on a compact boundaryless Riemannian manifold has its usual self-adjoint realization and heat semigroup. Haar measure on the unimodular group, descended to $\Gamma\backslash G$, is the volume used.

**Statement.** If $f(g)=F(g\cdot i)$ is right-$K$-invariant, then
$$
Wf=0,\qquad
\Omega f(g)=y^2(F_{xx}+F_{yy})(g\cdot i),\qquad
\tfrac12(H^2+E^2)f=2\Omega f=-2\Delta F.
$$
In the middle formula $y=\operatorname{Im}(g\cdot i)$; the constant requested in T2(b) is $c=1$. The two-jump multiplication-observable Lindbladian is $-2\Delta$ on the $K$-invariant sector. Its closed heat realization there is $e^{-2t\Delta}$ under H-AN.

<1>1. **Brackets, centrality, and $K$-invariance.**

PROOF. Matrix multiplication gives
$$
[H,E]=2W,\qquad [H,W]=2E,\qquad [E,W]=-2H.
$$
The differential representation by left-invariant fields respects these brackets. For example
$$
[H,E^2]=2(WE+EW)=[H,W^2],
$$
and
$$
[E,H^2]=-2(WH+HW)=[E,W^2].
$$
Also $[W,H^2+E^2]=-2(EH+HE)+2(HE+EH)=0$. These identities prove that $\Omega$ commutes with all three basis fields, and that $H^2+E^2$ commutes with $W$. Exponentiating the latter adjoint invariance (or rotating the pair $H,E$ by $\operatorname{Ad}K$) proves that $H^2+E^2$ commutes with right translation by $K$. Since $\exp(uW)\in K$, right-$K$-invariance gives $Wf=0$. $\square$

<1>2. **Compute at a section, retaining second-order drift.**

PROOF. Represent $x+iy$ by
$$
g_{x,y}=\begin{pmatrix}\sqrt y&x/\sqrt y\\0&1/\sqrt y\end{pmatrix},
\qquad g_{x,y}\cdot z=x+yz.
$$
The two curves needed for second derivatives are
$$
g_{x,y}\exp(uH)\cdot i=x+i y e^{2u},
$$
$$
g_{x,y}\exp(uE)\cdot i
=x+y\tanh(2u)+iy\operatorname{sech}(2u).
$$
The second formula follows by substituting $\exp(uE)=\left(\begin{smallmatrix}\cosh u&\sinh u\\\sinh u&\cosh u\end{smallmatrix}\right)$ in the Möbius action and multiplying numerator and denominator by the conjugate denominator. Twice differentiating $F$ along these curves at zero gives
$$
H^2f(g_{x,y})=4y^2F_{yy}+4yF_y,
\qquad
E^2f(g_{x,y})=4y^2F_{xx}-4yF_y.
$$
In particular the first-derivative terms cancel. Squaring only the first projected tangent vectors would miss the second formula's drift and would be incorrect. Since $W^2f=0$, division by four proves the formula for $\Omega$ at the section. $\square$

<1>3. **Extend the computation to every frame.**

PROOF. Every $g$ over $x+iy$ is $g_{x,y}k$ for some $k\in K$. The operators $\Omega$ and $H^2+E^2$ preserve right-$K$-invariance by <1>1, so their values on $f$ at $g_{x,y}k$ equal their values at $g_{x,y}$. This extends <1>2 to all $g$. On $\Gamma\backslash G$ the same local computation descends, and $\tfrac12(H^2+E^2)f=2\Omega f=-2\Delta F$. $\square$

<1>4. **Formal adjoints and the compact-direction sign.**

PROOF. The brackets in <1>1 show $\operatorname{tr}\operatorname{ad}B=0$ for each basis element, hence for every $B$. Since $G$ is connected, its adjoint determinants are one, so it is unimodular. Right multiplication preserves Haar volume and its quotient volume; integration by parts therefore makes $H,E,W$ formally anti-self-adjoint. T2.1 applies with $L_1=-iH,L_2=-iE$. The identity on the whole smooth function space is
$$
\tfrac12(H^2+E^2)=2\Omega+\tfrac12W^2,
$$
not $2\Omega$. The negative coefficient of $W^2$ in $\Omega$ makes its second-order coefficient form indefinite. At any point choose a real covector annihilating $H,E$ but not $W$; the quadratic symbol of $\Omega$ then has the opposite sign from a diffusion sum of real squares. Thus this Casimir is not a scalar diffusion Lindbladian on all multiplication observables on $M$. Equality with a sum of squares holds after restricting to $Wf=0$. Under H-AN, the operator there has the stated heat realization. $\square$

**Status:** `proved-here` for all differential and Lindblad algebra identities; `conditional-on H-AN` for the closed heat-semigroup realization.

### Proposition T2.3 — The tensor-product representation has the Lindblad sum of squares

**Hypotheses.** $\pi$ is a strongly continuous unitary representation on a complex Hilbert space $\mathcal H$, with a specified common invariant dense domain $\mathcal D$ of smooth vectors for the finitely many generators and their products. Put $A_j=d\pi(X_j)$, anti-self-adjoint generators, and $L_j=-iA_j$. Work on the span $\mathcal R(\mathcal D)$ of the rank-one operators $|v\rangle\langle w|$ with $v,w\in\mathcal D$. Products involving an unbounded operator on the right are understood via the resulting finite-rank bounded extensions. The Hilbert–Schmidt identification and all identities on this domain are **proved here**. No assertion that this domain is a core for a particular closed sum of squares is needed.

**Statement.** Under $\mathcal H\widehat\otimes\overline{\mathcal H}\cong\operatorname{HS}(\mathcal H)$,
$$
B_j:=d(\pi\otimes\bar\pi)(X_j),\qquad B_j\rho=[A_j,\rho],
$$
and
$$
\mathcal L\rho
=\sum_j\left(L_j\rho L_j-\tfrac12\{L_j^2,\rho\}\right)
=\tfrac12\sum_j[A_j,[A_j,\rho]]
=\tfrac12\sum_j B_j^2\rho.
$$
For $\mathfrak{sl}_2$ and the two noncompact jumps,
$$
\mathcal L=2\Omega_{\pi\otimes\bar\pi}+\tfrac12 B_W^2,
\qquad
\Omega_{\pi\otimes\bar\pi}=\tfrac14(B_H^2+B_E^2-B_W^2).
$$
In particular it equals $2\Omega_{\pi\otimes\bar\pi}$ on diagonal-$K$-invariant Hilbert–Schmidt vectors, not in general on all Hilbert–Schmidt operators.

<1>1. **The Hilbert–Schmidt identification and infinitesimal action.**

PROOF. With the Hilbert inner product linear in its second argument, map $v\otimes\bar w$ to $[u\mapsto v\langle w,u\rangle]$. The rank-one Hilbert–Schmidt inner products equal the tensor inner products, and finite-rank operators are dense, so this extends to a unitary identification. The tensor action becomes
$$
(\pi\otimes\bar\pi)(g)\rho=\pi(g)\rho\pi(g)^{-1}.
$$
Differentiating on $\mathcal R(\mathcal D)$ gives $B_j\rho=A_j\rho-\rho A_j$. Equivalently its action on $v\otimes\bar w$ is $A_jv\otimes\bar w+v\otimes\overline{A_jw}$; anti-self-adjointness converts the second rank-one term to $-\rho A_j$. $\square$

<1>2. **The two factors of $i$.**

PROOF. $[L_j,[L_j,\rho]]=(-i)^2[A_j,[A_j,\rho]]=-[A_j,[A_j,\rho]]$. The algebraic Lindblad identity from T2.1 therefore gives the asserted *positive* one-half coefficient in front of $B_j^2$. As a check on dissipativity, differentiating the unitary conjugation representation makes $B_j$ skew-symmetric, so
$$
\langle\rho,\mathcal L\rho\rangle_{\mathrm{HS}}
=-\tfrac12\sum_j\|[A_j,\rho]\|_{\mathrm{HS}}^2\le0
$$
on the stated domain. $\square$

<1>3. **The precise Casimir qualification.**

PROOF. The tensor representation respects the Lie brackets of T2.2. Rearranging its Casimir definition gives $\tfrac12(B_H^2+B_E^2)=2\Omega_{\pi\otimes\bar\pi}+\tfrac12B_W^2$. A diagonal-$K$-invariant operator satisfies $\pi(k)\rho\pi(k)^{-1}=\rho$, hence $B_W\rho=0$, and the correction vanishes. The same bracket calculation as T2.2 shows that this invariant sector is preserved. $\square$

**Remark (not a spectral-gap theorem).** A decomposition of $\pi\otimes\bar\pi$ into irreducibles, when supplied with appropriate direct-integral and domain theory, organizes the gap problem. The Casimir acts by its infinitesimal-character parameter, but the two-jump generator additionally has $B_W^2/2$, so its $K$-types and invariant vectors matter. The decomposition can involve parameters accumulating at zero; no positive gap follows just from writing a tensor-product Casimir. Even a formal Lindblad expression with unbounded jumps does not by itself establish a conservative completely positive semigroup on trace-class operators.

**Status:** `proved-here` on the stated smooth finite-rank domain; the spectral-gap remark makes no theorem claim.

## T3. The transverse Poincaré map

### Proposition T3.1 — Stable and unstable multipliers and the Jacobian

**Hypotheses.** Use the compact hyperbolic surface conventions. The flow is $\phi_t(\Gamma g)=\Gamma ga_t$, and $\gamma$ is a closed flow orbit of primitive period $\ell>0$. Its linearized Poincaré map is the derivative of a local return map, or equivalently the induced derivative of $\phi_\ell$ modulo the flow direction. The equivalence and all eigenvalue calculations are **proved here**, using the given homogeneous description of the geodesic flow.

**Statement.** The transverse multipliers are $e^\ell,e^{-\ell}$, and for every $k\ge1$,
$$
|\det(1-P_\gamma^k)|
=(e^{k\ell}-1)(1-e^{-k\ell})
=4\sinh^2(k\ell/2)
=e^{k\ell}(1-e^{-k\ell})^2.
$$

<1>1. **Time and tangent trivialization.**

PROOF. The curve $a_t\cdot i=i e^t$ has hyperbolic speed one, since its vertical velocity is $e^t$ and its height is $e^t$. Thus its time parameter is length. The flow direction in the specified Lie-algebra basis is $H/2$. Identify tangent vectors at $\Gamma g$ with $Y\in\mathfrak{sl}_2$ through the curve $\Gamma g\exp(uY)$. This is well-defined after quotienting on the left by $\Gamma$. Under right multiplication,
$$
g\exp(uY)a_t=ga_t\exp\big(u\operatorname{Ad}(a_t^{-1})Y\big),
$$
so the derivative in these frames is $\operatorname{Ad}(a_t^{-1})$. At a periodic point the source and target frames are the same frame on $M$: replacing $ga_\ell$ by a left-$\Gamma$ translate of $g$ does not change it. $\square$

<1>2. **Stable and unstable eigenvalues.**

PROOF. Put
$$
N_+=\tfrac12(E+W)=\begin{pmatrix}0&1\\0&0\end{pmatrix},
\qquad
N_-=\tfrac12(E-W)=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
$$
Conjugation gives $\operatorname{Ad}(a_t^{-1})N_+=e^{-t}N_+$, $\operatorname{Ad}(a_t^{-1})N_-=e^tN_-$, and $\operatorname{Ad}(a_t^{-1})H=H$. The quotient $\mathfrak{sl}_2/\mathbb RH$ therefore has the two stated multipliers. If a return map on a section is written $m\mapsto\phi_{\tau(m)}m$, differentiating produces $d\phi_\ell$ plus a multiple of the flow vector from $d\tau$. That added term vanishes in the quotient by the flow direction, proving the asserted equivalence with the Poincaré map. $\square$

<1>3. **Determinant and reversal.**

PROOF. Raising the two multipliers to the $k$th power gives determinant $(1-e^{k\ell})(1-e^{-k\ell})<0$. Taking its absolute value gives $e^{k\ell}+e^{-k\ell}-2$, which equals both expressions in the statement. Reversing the flow interchanges the two multipliers, so this absolute determinant is unchanged. This observation will make the Koopman sign convention in T4 compatible with the forward-flow Poincaré map. $\square$

**Status:** `proved-here`.

## T4. The flat determinant, Selberg tower, and the corrected first band

### Proposition T4.1 — Absolute convergence and the signed logarithmic derivative

**Hypotheses.** In addition to T3.1, use the following explicit inputs.

- **H-GEO (standard, to be cited):** a torsion-free cocompact Fuchsian group acts freely and properly discontinuously on $\mathbb H$, and the quotient map is a covering; nonidentity elements are hyperbolic with invariant axes, primitive conjugacy classes correspond to primitive oriented closed geodesics, and their periods equal their translation lengths. Hyperbolic balls have area $2\pi(\cosh R-1)$. The elementary counting consequence needed below is **proved here**, without a prime-geodesic theorem.
- **H-GUI (standard, to be cited):** Guillemin's scalar flat-trace formula for this flow and this orbit convention holds in $\mathcal D'((0,\infty))$:
  $$
  \operatorname{Tr}^{\mathrm{flat}}e^{-tX}
  =\sum_\gamma\sum_{k\ge1}
  \frac{\ell_\gamma\,\delta(t-k\ell_\gamma)}{|\det(1-P_\gamma^k)|}.
  $$
  Here $Xf=\left.\frac d{dt}\right|_0 f\circ\phi_t=(H/2)f$ and $(e^{-tX}f)(m)=f(\phi_{-t}m)$. The Poincaré determinant may be computed for the forward flow, by T3.1. This is a flat trace, not a trace-class Hilbert-space trace.
- The Euler product definition
  $$
  Z_{\mathrm{Sel}}(s)=\prod_\gamma\prod_{q\ge0}(1-e^{-(s+q)\ell_\gamma})
  $$
  is used initially only where its convergence is **proved here**.

**Statement.** For $\operatorname{Re}\sigma>0$,
$$
\Lambda_{\mathrm{fl}}(\sigma)
:=\int_0^\infty e^{-\sigma t}\operatorname{Tr}^{\mathrm{flat}}e^{-tX}\,dt
=\sum_\gamma\sum_{k\ge1}
\frac{\ell_\gamma e^{-\sigma k\ell_\gamma}}{4\sinh^2(k\ell_\gamma/2)}.
$$
The integral means the absolutely convergent Laplace integral of the positive atomic measure in H-GUI. The product
$$
D(\sigma)=\prod_{j\ge1}Z_{\mathrm{Sel}}(\sigma+j)
$$
converges absolutely and locally uniformly, without zeros, in this half-plane, and
$$
\boxed{\ \Lambda_{\mathrm{fl}}(\sigma)=\frac{D'(\sigma)}{D(\sigma)}\ }.
$$
The minus sign proposed for this particular $D$ is false. Equivalently $\Lambda_{\mathrm{fl}}=-\partial_\sigma\log(D^{-1})$.

<1>1. **A systole and an elementary orbit-counting bound.**

PROOF. Fix $o\in\mathbb H$. Cocompactness gives $R_0$ such that every point is within $R_0$ of $\Gamma o$. An axis point of each hyperbolic conjugacy class can therefore be moved to within $R_0$ of $o$ by conjugating the representative. Its displacement at $o$ is at most $\ell_\gamma+2R_0$. Properness and freeness give $\epsilon>0$ with $d(o,\eta o)>\epsilon$ for all $\eta\ne1$. The balls of radius $\epsilon/3$ about distinct orbit points are disjoint. Comparing their total area to the ball of radius $R+\epsilon/3$ gives
$$
\#\{\eta\in\Gamma:d(o,\eta o)\le R\}\le C e^R\quad(R\ge1).
$$
Choosing one representative of each primitive conjugacy class with length at most $R$ injects those classes into the displacement ball of radius $R+2R_0$. Hence $N(R):=\#\{\gamma:\ell_\gamma\le R\}\le C'e^R$. In particular only finitely many such classes have length at most any given positive bound. Their positive lengths, together with a bound such as $1$, give a uniform positive lower bound $\ell_*>0$ on primitive lengths. Thus for every $a>1$ and nonnegative integer $b$,
$$
\sum_\gamma\ell_\gamma^b e^{-a\ell_\gamma}<\infty,
$$
by splitting the lengths into intervals $[n,n+1)$; the tail is bounded by a multiple of $\sum_n(n+1)^b e^{-(a-1)n}$. $\square$

<1>2. **Convergence of the Selberg logarithm.**

PROOF. For $\operatorname{Re}s>1$, every factor has $|e^{-(s+q)\ell}|<1$. Choose the logarithm tending to zero as $\operatorname{Re}s\to+\infty$. Expanding $\log(1-z)=-\sum_{k\ge1}z^k/k$ gives
$$
\log Z_{\mathrm{Sel}}(s)
=-\sum_\gamma\sum_{k\ge1}
\frac{e^{-sk\ell_\gamma}}{k(1-e^{-k\ell_\gamma})}.
$$
Absolute convergence is uniform on $\operatorname{Re}s\ge1+\eta$ for $\eta>0$: the denominator is at least $1-e^{-\ell_*}$ and the $k$-sum is bounded by a constant times $e^{-(1+\eta)\ell_\gamma}$. Summability follows from <1>1. Polynomial factors in $k\ell_\gamma$ from any fixed number of derivatives are absorbed by reducing $\eta$ to $\eta/2$. This also justifies local uniform differentiation and proves the Euler product is holomorphic and nonzero there. $\square$

<1>3. **Laplace transform and the transverse expansion.**

PROOF. T3.1 and H-GUI give the displayed series for $\Lambda_{\mathrm{fl}}$. If $a=\operatorname{Re}\sigma>0$, its absolute sum is
$$
\sum_{\gamma,k}\frac{\ell_\gamma e^{-(a+1)k\ell_\gamma}}{(1-e^{-k\ell_\gamma})^2},
$$
which is bounded by a constant depending on $a,\ell_*$ times $\sum_\gamma\ell_\gamma e^{-(a+1)\ell_\gamma}<\infty$. There is no contribution near $t=0$, because every period is at least $\ell_*$. This proves that cutoffs tending to one in the Laplace pairing have a well-defined absolutely convergent limit. For $x>0$, differentiating the geometric series gives
$$
\frac1{4\sinh^2(x/2)}=\frac{e^{-x}}{(1-e^{-x})^2}
=\sum_{m\ge0}(m+1)e^{-(m+1)x}.
$$
The same bounds justify using this expansion in the Laplace series. $\square$

<1>4. **The tower, its logarithm, and the sign.**

PROOF. Summing the absolutely convergent logarithms from <1>2 at $s=\sigma+j$ gives
$$
\begin{aligned}
\log D(\sigma)
&=-\sum_{\gamma,k}\frac1k
  \frac{e^{-(\sigma+1)k\ell_\gamma}}{(1-e^{-k\ell_\gamma})^2}\\
&=-\sum_{\gamma,k}\sum_{m\ge0}
  \frac{m+1}{k}e^{-(\sigma+m+1)k\ell_\gamma}.
\end{aligned}
$$
Absolute local uniform convergence follows exactly as in <1>3, without the factor $\ell_\gamma$. It also shows that the sum of absolute values of the individual factor logarithms is finite, the asserted meaning of absolute product convergence. Differentiating cancels the minus sign and introduces $k\ell_\gamma$, yielding $D'/D=\Lambda_{\mathrm{fl}}$. In particular both are positive for real $\sigma>0$. Equivalently, the tower can be written
$$
D(\sigma)=\prod_\gamma\prod_{m\ge0}
\bigl(1-e^{-(\sigma+m+1)\ell_\gamma}\bigr)^{m+1}.
$$
This is an equality of convergent products here, not just a formal rearrangement. $\square$

<1>5. **What determinant has been constructed.**

PROOF. Dividing the orbit measure by $t$ replaces the primitive numerator $\ell_\gamma$ at $t=k\ell_\gamma$ by $1/k$. Thus the preceding calculation is exactly
$$
D(\sigma)=\exp\left(-\int_0^\infty\frac{e^{-\sigma t}}t
\operatorname{Tr}^{\mathrm{flat}}e^{-tX}\,dt\right),
\qquad \operatorname{Re}\sigma>0.
$$
This defines a flat dynamical determinant with a fixed normalization $D(\sigma)\to1$ as real $\sigma\to+\infty$. It does not identify $D$ with an ordinary Fredholm determinant on $L^2(M)$ or construct an anisotropic-space resolvent. Those are additional assertions with additional analytic hypotheses. $\square$

**Status:** `conditional-on H-GEO, H-GUI`; all convergence, product, and sign calculations are proved here. The proposed logarithmic-derivative sign is corrected.

### Proposition T4.2 — Global zero divisor and the nonconstant first band

**Hypotheses.** Use T4.1 and these explicit standard inputs.

- **H-LAP (standard, to be cited):** the positive Laplacian on the connected compact hyperbolic surface has a complete discrete spectrum $0=\lambda_0<\lambda_1\le\lambda_2\le\cdots\to\infty$, with repetitions for multiplicity. Write $\lambda_j=1/4+r_j^2$, choosing $r_j\ge0$ real for $\lambda_j\ge1/4$, and $r_j=i\nu_j$ with $0<\nu_j<1/2$ for $0<\lambda_j<1/4$. For the constant eigenfunction take $r_0=i/2$. Simplicity of zero also follows directly by integrating $\langle F,\Delta F\rangle=\int|\nabla F|^2$ and using connectedness.
- **H-SZ (standard, to be cited):** the Euler product in T4.1 extends to an **entire** function on $\mathbb C$ with precisely the following additive zero divisor:
  $$
  \operatorname{div}_0 Z_{\mathrm{Sel}}
  =\sum_{j\ge0}\bigl([\tfrac12+ir_j]+[\tfrac12-ir_j]\bigr)
  +(2g-2)\sum_{n\ge0}(2n+1)[-n].
  $$
  Here $[z]$ means a unit point of the divisor, and repetitions are added. In particular an eigenvalue $1/4$ of multiplicity $d$ gives order $2d$ at $s=1/2$; $s=0$ has order $2g-1$ (one constant-mode contribution plus $2g-2$ topological contributions), and $s=1$ is simple. There are no additional zeros or poles. Meromorphic continuation alone, without this entire-function and complete-divisor assertion, would not suffice for the conclusion below.

**Statement.** The same product $D(\sigma)=\prod_{j\ge1}Z_{\mathrm{Sel}}(\sigma+j)$ continues to an entire function by locally normally convergent tails. Its logarithmic derivative is meromorphic on $\mathbb C$. Define *trace resonances* here to mean the poles of this continued $\Lambda_{\mathrm{fl}}$; no separate assertion about a chosen operator realization of Pollicott–Ruelle resonances is being made. The divisor of $D$ is the sum of the shifted Selberg divisors:
$$
\sigma=-\tfrac12-k\pm ir_j\quad(k\ge0,\ j\ge0),
$$
together with
$$
\sigma=-N\quad(N\ge1),\qquad
\text{topological contribution }(2g-2)N^2.
$$
At a zero of $D$ of total order $m$, $\Lambda_{\mathrm{fl}}$ has a **simple** pole of residue $m$; “multiplicity” refers to that residue/divisor, not the pole order. The constant eigenfunction contributes a simple zero at $\sigma=0$ and order two at every negative integer. In particular the total order at $-N$ is $(2g-2)N^2+2$.

Define the nonconstant first band as the multiset
$$
\mathcal B_0=\{-\tfrac12\pm ir_j:j\ge1\}.
$$
It is exactly the pole multiset in the open strip $-1<\operatorname{Re}\sigma<0$. Then
$$
\boxed{\ \mathcal B_0\subset\{\operatorname{Re}\sigma=-\tfrac12\}
\iff r_j\in\mathbb R\ \text{for all }j\ge1
\iff\operatorname{spec}\Delta\cap(0,1/4)=\varnothing.\ }
$$
The qualification $j\ge1$ is essential: $r_0=i/2$ is never real.

<1>1. **Continuation of the infinite product, with a nonvanishing tail.**

PROOF. Fix a compact set $Q\subset\mathbb C$ and let $b=\inf_{\sigma\in Q}\operatorname{Re}\sigma$. Choose an integer $J\ge1$ with $b+J>1$. The logarithmic series for every $Z_{\mathrm{Sel}}(\sigma+j)$ with $j\ge J$ is valid on a neighborhood of $Q$. For $q=j-J\ge0$, its absolute value is bounded by
$$
e^{-q\ell_*}
\sum_{\gamma,k}\frac{e^{-(b+J)k\ell_\gamma}}{k(1-e^{-k\ell_\gamma})}.
$$
The second factor is finite by T4.1. Hence the tail logarithms converge uniformly and absolutely, and their exponential is holomorphic and nowhere zero. Multiplying by the finitely many entire initial factors, supplied by H-SZ, defines $D$ near $Q$. These definitions agree on overlaps because splitting off a finite number of Euler-region tail factors does not change a product. They agree with T4.1 on $\operatorname{Re}\sigma>0$, proving a global entire continuation and showing that only finitely many initial factors can contribute at any given zero. $\square$

<1>2. **The shifted spectral and topological divisors.**

PROOF. A zero $s_*$ of the $j$th factor occurs at $\sigma=s_*-j$. For a spectral zero, put $j=k+1$ to obtain $-1/2-k\pm ir_a$. At $\sigma=-N$, the topological zeros come from $s_*=-n$, $j+n=N$, with $j\ge1$ and $0\le n\le N-1$. Their orders add to
$$
(2g-2)\sum_{n=0}^{N-1}(2n+1)=(2g-2)N^2.
$$
The constant-mode zeros $s_*=1,0$ give respectively $\sigma=1-j, -j$. At zero only the first family contributes once; at every $-N$, $N\ge1$, both contribute once. No nonconstant spectral zero produces an integer: nonreal spectral roots have nonzero imaginary part, the $r_a=0$ roots shift to half-integers, and exceptional nonconstant roots have real parts strictly between zero and one. The nonvanishing tail in <1>1 rules out any additional zero. $\square$

<1>3. **Logarithmic derivative and the meaning of multiplicity.**

PROOF. Near a zero $\sigma_*$ of order $m$, write $D(\sigma)=(\sigma-\sigma_*)^m h(\sigma)$ with $h$ holomorphic and nonzero. Then $D'/D=m/(\sigma-\sigma_*)+h'/h$. At a nonzero point $D'/D$ is holomorphic. Since all local contributions come from zeros and none from poles of the factors, there is no cancellation. Thus the list in <1>2 is exactly the pole set, with additive residues. Coincident signs at $r_j=0$ and coincident eigenvalues must be counted with the indicated repetitions. $\square$

<1>4. **Locate and characterize the first band.**

PROOF. For a nonconstant eigenvalue above or at $1/4$, the $k=0$ points have real part $-1/2$. For an exceptional $r_j=i\nu_j$ with $0<\nu_j<1/2$, they are the two real points $-1/2\pm\nu_j$, in $(-1,0)$ but off its midpoint. All $k\ge1$ translates of nonconstant points have real part less than $-1$. The constant-mode points and topological points lie on the boundary integers or further left. Thus the open strip contains exactly $\mathcal B_0$, and its entire pole multiset lies on the midpoint line exactly when there are no exceptional positive eigenvalues. H-LAP ensures the parametrization accounts for every eigenvalue, proving both equivalences. $\square$

**Remark.** The assertion “every $r_j$ is real” including $j=0$ is false on every compact connected surface. With $j=0$ included the alleged first band contains $0$ and $-1$, and cannot lie on $\operatorname{Re}\sigma=-1/2$. The corrected property is the absence of **nonconstant** complementary-series parameters, the continuous counterpart of removing the constant adjacency mode (and the bipartite extremal mode when present) in a graph's Ramanujan condition. This establishes an equivalence, not that a given surface has the $1/4$ property.

**Status:** `conditional-on H-GEO, H-GUI, H-LAP, H-SZ`; the continuation-of-product argument, divisor bookkeeping, and corrected equivalence are proved here.

### Proposition T4.3 — The graph comparison and the Ruelle quotient

**Hypotheses.** For the graph part let $T$ be the ordinary unweighted Hashimoto matrix of a finite undirected graph, acting on directed edges, with a fixed-point-free edge-reversal involution. A cyclic word is required to be nonbacktracking also across its closing edge; primitive cyclic classes are taken modulo cyclic rotation, with reverse orientation distinct. These definitions and finite matrix algebra suffice; the formulas here are **proved here**. The usual regular-graph Ihara–Bass factorization is background for the comparison and is already established in the specified notebook context. For the Ruelle part use the convergent Selberg product of T4.1; continuation of its quotient additionally uses H-SZ.

**Statement.** For sufficiently small $|u|$,
$$
\operatorname{Tr}T^m
=\sum_\gamma\sum_{k\ge1:\,k\ell_\gamma=m}\ell_\gamma,
\qquad
\det(1-uT)=\prod_\gamma(1-u^{\ell_\gamma}),
$$
and
$$
u\partial_u\log\det(1-uT)^{-1}
=\sum_{m\ge1}\operatorname{Tr}T^m u^m.
$$
Thus, with the corrected sign convention of T4.1, the graph analogue of $D$ is **$\det(1-uT)$**. The inverse $\det(1-uT)^{-1}$ is the graph dynamical zeta and corresponds to $D^{-1}$, not to $D$. No shifted tower occurs in this scalar graph trace.

With the direct-product convention specified in the question, define
$$
\zeta_R(s):=\prod_\gamma(1-e^{-s\ell_\gamma}).
$$
Then, for $\operatorname{Re}s>1$ and subsequently as a meromorphic quotient under H-SZ,
$$
\boxed{\ \zeta_R(s)=\frac{Z_{\mathrm{Sel}}(s)}{Z_{\mathrm{Sel}}(s+1)}\ }.
$$
Some authors call the reciprocal the Ruelle zeta; the convention here is the displayed direct product.

<1>1. **Count rooted closed edge sequences.**

PROOF. A diagonal entry of $T^m$ counts an admissible edge sequence of $m$ transitions returning to its starting directed edge. Summing diagonal entries counts closed nonbacktracking words with a specified starting position. Each is a $k$th power of a unique primitive cyclic word of length $\ell$ with $k\ell=m$. It has exactly $\ell$ distinct rooted sequences, not $m$, because the repeated pattern has period $\ell$. This proves the trace formula. It includes no transverse derivative or determinant. $\square$

<1>2. **The graph determinant and the variable change.**

PROOF. Finite matrix differentiation, or expansion of the logarithm for $\|uT\|<1$, gives
$$
\log\det(1-uT)=-\sum_{m\ge1}\frac{u^m}{m}\operatorname{Tr}T^m
=-\sum_{\gamma,k}\frac{u^{k\ell_\gamma}}k
=\sum_\gamma\log(1-u^{\ell_\gamma}).
$$
All rearrangements are absolutely convergent for sufficiently small $|u|$; the number of words of length $m$ is bounded exponentially by a finite alphabet bound. Exponentiation proves the product and differentiation proves the logarithmic-derivative formula. If $u=e^{-\sigma}$, then $\partial_\sigma=-u\partial_u$, so
$$
\partial_\sigma\log\det(1-e^{-\sigma}T)
=\sum_{m\ge1}\operatorname{Tr}T^m e^{-\sigma m}.
$$
This has exactly the same sign as $\partial_\sigma\log D(\sigma)$ in T4.1. It proves the stated correction to the proposed inverse-determinant analogy. $\square$

<1>3. **Telescope the Selberg product.**

PROOF. For each $\gamma$, the finite quotient over $q=0,\ldots,Q$ telescopes to
$$
\frac{\prod_{q=0}^Q(1-e^{-(s+q)\ell_\gamma})}
     {\prod_{q=0}^Q(1-e^{-(s+1+q)\ell_\gamma})}
=\frac{1-e^{-s\ell_\gamma}}{1-e^{-(s+Q+1)\ell_\gamma}}.
$$
For $\operatorname{Re}s>1$, the logarithmic absolute convergence of T4.1 lets us take $Q\to\infty$ and multiply over $\gamma$. The denominator tail tends to one locally uniformly, proving the identity. Equivalently subtract the logarithmic series and cancel the factor $1-e^{-k\ell_\gamma}$. This also proves the identity as a formal orbit expansion. Under H-SZ the quotient gives a meromorphic continuation; its zeros and poles must allow cancellations between numerator and denominator. $\square$

<1>4. **What the continuous analogy does and does not say.**

PROOF. The scalar graph trace is a count of a discrete set of rooted periodic sequences. In the smooth geodesic flow, H-GUI instead weights a transverse fixed point by the reciprocal Jacobian from its two stable/unstable directions. Expanding that Jacobian creates the multiplicities $m+1$ and hence the tower. The informal phrase “the tree is one-dimensional” does not prove this distinction; the precise distinction is discrete counting versus the smooth transverse fixed-point determinant. On a $(q+1)$-regular graph the Ihara–Bass relation further factors the graph determinant through $1-uA+qu^2$ and a topological factor, as in the notebook. Nothing in T4.1 alone constructs an analogous finite vertex-space determinant or proves a quadratic operator relation. The concrete continuous identities obtained here are the tower, its shifted spectral divisor, and
$$
\frac{D(\sigma)}{D(\sigma+1)}=Z_{\mathrm{Sel}}(\sigma+1),
$$
first in $\operatorname{Re}\sigma>0$ by removing the first factor and then meromorphically. The Laplace variable is $\sigma$; the first Selberg factor has variable $s=\sigma+1$; the independent Ruelle quotient above uses its own variable $s$. $\square$

**Status:** graph identities `proved-here`; Ruelle and tower product identities `conditional-on H-GEO` for convergence, with H-SZ additionally for continuation; interpretation of the tower as the flat-trace determinant additionally uses H-GUI through T4.1. The inverse-determinant analogy is corrected.

## T5. The modular scattering term and the signed prime comb

### Proposition T5.1 — Exact Fourier identity, including the boundary correction

**Hypotheses.** This proposition concerns the modular group, not the torsion-free compact group of T2–T4. The following inputs are independent of H-GUI and H-SZ.

- **H-PHI (standard, to be cited):** the modular scattering determinant is the meromorphic function
  $$
  \phi(s)=\sqrt\pi\,
  \frac{\Gamma(s-1/2)\zeta(2s-1)}{\Gamma(s)\zeta(2s)}.
  $$
  The prime denotes differentiation in the complex variable $s$, not in $r$.
- **H-ZETA (standard, to be cited):** $\zeta$ continues meromorphically, is regular at zero with $\zeta(0)=-1/2$, has Laurent expansion $\zeta(1+w)=1/w+\gamma_E+O(w)$, satisfies conjugation symmetry and
  $$
  \zeta(z)=\chi(z)\zeta(1-z),\qquad
  \chi(z)=\pi^{z-1/2}\frac{\Gamma((1-z)/2)}{\Gamma(z/2)},
  $$
  and is zero-free on $\operatorname{Re}z=1$ away from its pole. We also take the explicit boundary estimate
  $$
  \left|\frac{\zeta'}{\zeta}(1+\epsilon+iv)\right|
  \le C\log^2(3+|v|),\qquad |v|\ge1,\quad0\le\epsilon\le\epsilon_0,
  $$
  for some fixed $\epsilon_0>0$. This is a standard consequence of the classical zero-free region; the estimate, rather than an unspecified appeal to “boundedness,” is the input used here. Near $v=0$ the pole is separated explicitly below. This zero-free-line input is unconditional standard zeta theory, not RH.
- **H-GAMMA (standard, to be cited):** $\Gamma$ is meromorphic with no zeros and with simple poles exactly at the nonpositive integers, satisfies conjugation symmetry, is regular and nonzero in the right half-plane, $\Gamma(z)=1/z+O(1)$ near zero, $\Gamma(1/2)=\sqrt\pi$, and $\psi=\Gamma'/\Gamma$ satisfies, for $\operatorname{Re}z>0$,
  $$
  \psi(z)=-\gamma_E+\int_0^\infty
  \frac{e^{-u}-e^{-zu}}{1-e^{-u}}\,du.
  $$
  Its fixed-right-half-plane vertical growth is $O(\log(3+|\operatorname{Im}z|))$ (the digamma form of Stirling's estimate).
- The absolutely convergent Dirichlet identity for $\zeta'/\zeta$ in $\operatorname{Re}z>1$, the boundary-distribution calculation, and the Fourier constants are **proved here** from these inputs and elementary Fourier analysis.

**Statement.** Define the ordinary smooth real-line multiplier by its removable value at $r=0$,
$$
m(r)=-\tfrac12\frac{\phi'}{\phi}(\tfrac12+ir),
\qquad C=\mathcal F^{-1}m\in\mathcal S'(\mathbb R).
$$
Then $m$ is real, even, smooth, and of at most polynomial growth, and the corrected prime identity is
$$
\boxed{\quad C(t)=-P(t)+A(t),\qquad
P(t)=\sum_{n\ge2}\frac{\Lambda_{\mathrm{vM}}(n)}n
\bigl[\delta(t-2\log n)+\delta(t+2\log n)\bigr].\quad}
$$
The archimedean-plus-boundary distribution $A$ is specified completely, including its extension at zero, by
$$
\begin{aligned}
\langle A,h\rangle
={}&\tfrac12\int_{\mathbb R}h(t)\,dt
-(\gamma_E+\log\pi)h(0)\\
&+\int_0^\infty
\frac{e^{-u}h(0)-\frac12e^{-u/2}(h(u)+h(-u))}{1-e^{-u}}\,du,
\qquad h\in\mathcal S(\mathbb R).
\end{aligned}
$$
In particular, away from zero it is the smooth function
$$
A(t)=\frac12-\frac{1}{4\sinh(|t|/2)},\qquad t\ne0.
$$
At zero the displayed pairing specifies a finite-part singularity of type $-1/(2|t|)$ and fixes its delta normalization. The $+1/2$ smooth term comes from the pole of $\zeta$ at $1$ when comparing ordinary boundary values with Abel boundary distributions; it must not be omitted or described as a digamma contribution. With the stipulated minus sign in $m$, the prime atoms of $C$ are **dips**, of weight $-\Lambda_{\mathrm{vM}}(n)/n$. Positive peaks instead occur in $-C$ with archimedean term $-A$.

<1>1. **Logarithmic differentiation, keeping the chain-rule factors.**

PROOF. Write $q(z)=\zeta'(z)/\zeta(z)$. Logarithmic differentiation of H-PHI away from its zeros and poles gives
$$
\frac{\phi'}{\phi}(s)
=\psi(s-\tfrac12)-\psi(s)+2q(2s-1)-2q(2s).
$$
The factors $2$ arise because the zeta arguments are $2s-1$ and $2s$. Evaluating at $s=1/2+ir$ and multiplying by $-1/2$ gives, for $r\ne0$,
$$
m(r)=-\tfrac12\psi(ir)+\tfrac12\psi(\tfrac12+ir)
-q(2ir)+q(1+2ir).
$$
Every sign here follows from differentiation with respect to $s$; differentiating $\phi(1/2+ir)$ with respect to $r$ instead would introduce an additional $i$. $\square$

<1>2. **Use the functional equation before taking the boundary at zero.**

PROOF. H-ZETA and logarithmic differentiation give
$$
q(z)=\frac{\chi'}\chi(z)-q(1-z),\qquad
\frac{\chi'}\chi(z)=\log\pi-\tfrac12\psi((1-z)/2)-\tfrac12\psi(z/2).
$$
Substitute $z=2ir$ in <1>1. The $\psi(ir)$ terms cancel exactly, yielding
$$
\boxed{\ m(r)=a(r)+b(r),\quad
a(r)=-\log\pi+\tfrac12\bigl[\psi(\tfrac12+ir)+\psi(\tfrac12-ir)\bigr],\quad
b(r)=q(1+2ir)+q(1-2ir).\ }
$$
These formulas initially hold for $r\ne0$. Write $q(1+w)=-1/w+h_\zeta(w)$ with $h_\zeta$ analytic near zero and $h_\zeta(0)=\gamma_E$. The pole parts cancel in the *ordinary pointwise sum*, so $b$ has smooth extension $b(0)=2\gamma_E$. Likewise $a$ is smooth. Directly from H-PHI and the local expansions, $\phi(1/2)=-1$ after removal of the singularity: the numerator behaves as $\sqrt\pi(-1/2)/w$ and the denominator as $\sqrt\pi/(2w)$ when $s=1/2+w$. It is nonzero there. For $r\ne0$, H-ZETA, its functional equation, and the nonzero gamma factors show that $\phi(1/2+ir)$ is also nonzero and finite. Thus this smooth extension equals the originally specified logarithmic derivative everywhere on the real line. $\square$

<1>3. **Temperedness and the value at zero.**

PROOF. Conjugation in H-ZETA and H-GAMMA makes $a$ and $b$ real and even. H-GAMMA bounds $a(r)$ by $O(\log(3+|r|))$, and H-ZETA bounds $b(r)$ by $O(\log^2(3+|r|))$ for $|r|\ge1$; <1>2 supplies boundedness near zero. Thus $m$ defines a regular tempered distribution and has a well-defined inverse Fourier transform. As a normalization check, the integral in H-GAMMA gives $\psi(1/2)=-\gamma_E-2\log2$: subtract $\psi(1)=-\gamma_E$ and substitute $v=e^{-u/2}$ to obtain $-2\int_0^1(1+v)^{-1}dv$. Hence
$$
m(0)=-\log\pi+\psi(1/2)+2\gamma_E
=\gamma_E-\log\pi-2\log2.
$$
This check uses the removable sum, not either singular term separately. $\square$

<1>4. **The prime expansion is first an Abel-regularized identity.**

PROOF. In $\operatorname{Re}z>1$, the absolutely convergent Euler product follows by expanding the finite prime products and passing to the absolutely convergent series $\sum_{n\ge1}n^{-z}$. Expanding each logarithm and differentiating on smaller right half-planes gives
$$
q(z)=-\sum_p\sum_{k\ge1}\log p\,p^{-kz}
=-\sum_{n\ge2}\Lambda_{\mathrm{vM}}(n)n^{-z}.
$$
The differentiated series converges absolutely because $\Lambda_{\mathrm{vM}}(n)\le\log n$ and $\sum_{n\ge2}\log n/n^{1+\epsilon}<\infty$ for $\epsilon>0$. Define
$$
b_\epsilon(r)=q(1+\epsilon+2ir)+q(1+\epsilon-2ir),\qquad\epsilon>0.
$$
Termwise inverse Fourier transformation is therefore valid, even as a transform of a finite signed measure:
$$
\mathcal F^{-1}b_\epsilon
=-\sum_{n\ge2}\frac{\Lambda_{\mathrm{vM}}(n)}{n^{1+\epsilon}}
\bigl[\delta(t-2\log n)+\delta(t+2\log n)\bigr]
=:-P_\epsilon.
$$
The argument $2ir$ produces $e^{\mp ir(2\log n)}$, so the atoms occur at $\pm2\log n$ with coefficient exactly $-\Lambda_{\mathrm{vM}}(n)n^{-1-\epsilon}$. No extra factor $1/2$ arises in this Fourier transform: it is an exponential with frequency $2\log n$, not a rescaled delta in $t$. $\square$

<1>5. **Temperedness of the weighted comb and passage to the boundary.**

PROOF. For $N>2$,
$$
\sum_{n\ge2}\frac{\Lambda_{\mathrm{vM}}(n)}n
\bigl(|h(2\log n)|+|h(-2\log n)|\bigr)
\le 2\sup_t(1+|t|)^N|h(t)|
\sum_{n\ge2}\frac{\log n}{n(1+2\log n)^N}<\infty.
$$
The final series converges by the integral test with variable $\log n$. Thus $P$ is tempered, and dominated convergence gives $P_\epsilon\to P$ in the distributional sense on Schwartz tests.

The frequency-side limit is **not** the ordinary function $b$ alone. Near zero, the Laurent expansion used in <1>2 gives
$$
b_\epsilon(r)
=-\frac{1}{\epsilon+2ir}-\frac{1}{\epsilon-2ir}
 +h_\zeta(\epsilon+2ir)+h_\zeta(\epsilon-2ir)
=-\frac{2\epsilon}{\epsilon^2+4r^2}+	ext{regular part}.
$$
The regular part tends locally uniformly to $b$. The first term tends to $-\pi\delta_0$ in distributions: after $r=\epsilon v/2$, its pairing with a Schwartz function $v_0(r)$ is $-\int_{\mathbb R}v_0(\epsilon v/2)(1+v^2)^{-1}dv$, which tends by dominated convergence to $-\pi v_0(0)$. Outside a fixed neighborhood of zero, H-ZETA supplies a uniform logarithmic-square bound, and on compact sets away from zero the convergence is uniform. A cutoff at zero and dominated convergence on the complement therefore prove, on the whole Schwartz space,
$$
b_\epsilon\longrightarrow b-\pi\delta_0.
$$
Continuity of the Fourier transform on tempered distributions and <1>4 now give
$$
\mathcal F^{-1}(b-\pi\delta_0)=-P,
\qquad
\boxed{\ \mathcal F^{-1}b=-P+\tfrac12.\ }
$$
This is the source of the extra smooth constant. Treating both boundary Dirichlet series as ordinary convergent series and simply cancelling their poles would lose it. $\square$

<1>6. **The archimedean distribution with its fixed extension at zero.**

PROOF. The digamma integral in H-GAMMA gives
$$
a(r)=-\gamma_E-\log\pi
+\int_0^\infty\frac{e^{-u}-e^{-u/2}\cos(ru)}{1-e^{-u}}\,du.
$$
First truncate the integral to $\eta<u<R$. Its inverse Fourier transform is a sum/integral of delta measures, since $\mathcal F^{-1}1=\delta_0$ and $\mathcal F^{-1}\cos(ru)=(\delta_u+\delta_{-u})/2$. Pairing the truncated transform with $h$ and then taking $\eta\downarrow0$, $R\uparrow\infty$ yields
$$
\langle\mathcal F^{-1}a,h\rangle
=-(\gamma_E+\log\pi)h(0)
+\int_0^\infty\frac{e^{-u}h(0)-\frac12e^{-u/2}(h(u)+h(-u))}{1-e^{-u}}\,du.
$$
To justify the limits, the numerator near zero is $O(u)|h(0)|+O(u^2)\sup_{|t|\le1}|h''(t)|$, by the symmetric Taylor expansion of $h$. The denominator is comparable to $u$, so the integrand is bounded by these seminorms. At infinity it decays exponentially times bounded test-function values. These estimates prove a tempered distribution and justify the limit of the truncated transforms; on the frequency side the analogous bound by a constant times $1+r^2$ justifies convergence against Schwartz tests as well.

For tests supported away from zero only the terms $h(\pm u)$ remain, so the kernel there is $-e^{-|t|/2}/[2(1-e^{-|t|})]=-1/[4\sinh(|t|/2)]$. Adding $1/2$ as prescribed by <1>5 gives exactly the formula for $A$. $\square$

<1>7. **Assemble the identity and fix the interpretation of peaks.**

PROOF. From <1>2, $C=\mathcal F^{-1}a+\mathcal F^{-1}b$. Substituting <1>5 and <1>6 proves $C=-P+A$. The distribution $A$ is smooth in a neighborhood of every nonzero prime time, so it cannot change the delta coefficient at such a time. Thus the negative sign of each prime atom is forced by the given multiplier. Reversing the sign of the scattering multiplier reverses the whole identity, giving $-C=P-A$. Merely reversing the Fourier exponential does not change these signs because $m$ is even. $\square$

**Status:** `conditional-on H-PHI, H-ZETA, H-GAMMA`; all Fourier manipulations, convergence statements, the negative prime sign, and the $+1/2$ boundary correction are proved here. The drafted positive-comb identity for this $m$ is corrected.

### Proposition T5.2 — What the rate-$1/4$ damping identity actually identifies

**Hypotheses.** Define the positive-time measures
$$
P_{\mathrm{ch,prime}}(t):=\sum_{n\ge2}\Lambda_{\mathrm{vM}}(n)n^{-1/2}\delta(t-2\log n),
\qquad
P_+(t):=\sum_{n\ge2}\frac{\Lambda_{\mathrm{vM}}(n)}n\delta(t-2\log n).
$$
These are well-defined locally finite measures on $(0,\infty)$, **proved here** by their local finiteness. The first is the prime measure with the weights specified in the question and in the narrative of the notebook's section 5. Identifying it with the *full* trace of $Z_{\mathrm{ch}}(t)$ is **not** a hypothesis of this proposition and is **not** proved. For its identification with the scattering calculation, use T5.1 and its stated standard hypotheses.

**Statement (corollary of T5.1 for the scattering identification).** In $\mathcal D'((0,\infty))$,
$$
\boxed{\quad
e^{-t/4}P_{\mathrm{ch,prime}}(t)=P_+(t)
=-\bigl(C-A\bigr)\big|_{(0,\infty)}.\quad}
$$
This is precisely an equality of prime atomic measures after subtracting the specified archimedean-plus-boundary term and choosing positive prime weights. It is not an equality of the full cusp distribution $C$ with a semigroup trace, nor an equality of operators or of their spectra. It implies nothing about RH.

<1>1. **Multiply the atoms by the damping function.**

PROOF. On the support point $t_n=2\log n$, one has $e^{-t_n/4}=n^{-1/2}$. Multiplication of a distribution by a smooth function obeys $a(t)\delta(t-t_n)=a(t_n)\delta(t-t_n)$. Pairing with any compactly supported positive-time test function, only finitely many atoms occur; their weights become $n^{-1/2}\Lambda_{\mathrm{vM}}(n)n^{-1/2}=\Lambda_{\mathrm{vM}}(n)/n$. This proves the first equality without any zeta theory. $\square$

<1>2. **Identify the signed scattering prime part.**

PROOF. Restrict T5.1 to $t>0$. The negative-time atoms disappear, leaving $(C-A)|_{(0,\infty)}=-P_+$. Combine with <1>1. The term $A$ does not disappear on $t>0$: it equals the explicit nonzero smooth function $1/2-1/[4\sinh(t/2)]$ there. Thus retaining the full cusp distribution would invalidate the proposed pure-comb statement. $\square$

<1>3. **Audit the notebook's full-trace interpretation.**

PROOF. The notebook's section 3 supplies a model for $Z_{\mathrm{ch}}(t)$ and section 5 writes a zero-side distribution, but its own displayed explicit formula has pole terms, a digamma term, and a **negative** prime term. It does not imply that the full trace is supported only at the prime times with the positive weights $\Lambda_{\mathrm{vM}}(n)n^{-1/2}$. There is also a delta scaling when changing $u$ to $t/2$.

More explicitly, suppose one uses the notebook's displayed symmetric zero explicit formula with the conventional transform pair
$$
h(r)=\int_{\mathbb R}e^{iru}g(u)\,du,
\qquad g(u)=\frac1{2\pi}\int_{\mathbb R}e^{-iru}h(r)\,dr.
$$
Its term $-2\sum_n\Lambda_{\mathrm{vM}}(n)n^{-1/2}g(\log n)$ on even tests is the even distribution
$$
-\sum_{n\ge2}\Lambda_{\mathrm{vM}}(n)n^{-1/2}
\bigl[\delta(u-\log n)+\delta(u+\log n)\bigr]
$$
in the full symmetric zero sum $\sum_\gamma e^{i\gamma u}$. Pulling this distribution back by $u=t/2$ uses $\delta(t/2-\log n)=2\delta(t-2\log n)$. Under the further RH-dependent mode expression $\operatorname{Tr}Z_{\mathrm{ch}}(t)=e^{-t/4}\sum_\gamma e^{i\gamma t/2}$ written in that section, this would give **$-2\Lambda_{\mathrm{vM}}(n)/n$** for its positive-time prime part, along with the transformed pole and archimedean terms. This is a consistency check on that displayed formula under its full-symmetric-zero convention, not an independent construction of the trace or an invocation of RH as a proved fact. Summing only positive ordinates and taking a real part would introduce a further factor one-half and would be a different trace convention.

Accordingly, <1>1–<1>2 prove the requested weight-damping fact for explicitly defined prime measures. The unqualified sentence “the cusp term is the trace of the Riemann channel damped at rate $1/4$” requires both a subtraction/sign convention and a separately justified channel trace formula. It is not established here and cannot be deduced from the stated notebook passage. $\square$

**Status:** damping of the defined prime measures `proved-here`; scattering identification `conditional-on H-PHI, H-ZETA, H-GAMMA`. The asserted identity of full cusp and channel traces is corrected to an identity of their specified prime measures; no full-trace theorem is claimed.

## T6. Dependency and correction ledger

### Proposition T6.1 — Exact scope of the proof submission

**Hypotheses.** The statements, proofs, conventions, and explicit standard inputs in T1–T5 are the data of this audit. Its classification is **proved here** by inspecting the displayed dependencies. None of the standard inputs has been externally cited or byte-checked in this file. H-BASE explicitly lists the elementary standard background used throughout; all entries below inherit it. The additional geometric and analytic inputs are enumerated separately.

**Statement.** The file establishes the following precisely delimited results.

| Proposition | What is established here | Standard input needing citation |
|---|---|---|
| T1.1 | Circle Poisson comb and trace-class smearing | Elementary Fourier-series background only; Poisson identity proved here |
| T1.2 | Locally finite prime orbital trace; infinite direct-sum trace-class obstruction; failure of temperedness for the undamped prime comb | None beyond elementary T1.1 background and unique factorization |
| T1.3 | Finite generator spectrum equals finite Euler pole set; finite product is zero-free; that spectrum contains no continued Riemann zeta zero | H-ZETA and H-GAMMA only for the last assertion |
| T2.1 | Multiplication-observable double commutator equals one-half the real sum of squares on a common domain | None beyond derivations and integration by parts; analytic semigroup existence is not asserted |
| T2.2 | Central Casimir, $c=1$, preservation of the right-$K$-invariant sector, and generator $-2\Delta$ there | H-AN only for a closed operator/heat-semigroup realization |
| T2.3 | Lindblad expression is the tensor-product sum of squares; the $B_W^2/2$ correction is explicit | A common smooth invariant domain is assumed; no representation decomposition or gap theorem is used |
| T3.1 | Poincaré multipliers and exact reciprocal-Jacobian normalization | The specified homogeneous geodesic-flow model; no trace theorem |
| T4.1 | Laplace convergence for $\operatorname{Re}\sigma>0$, Selberg tower, and $\Lambda_{\mathrm{fl}}=D'/D$ | H-GEO and H-GUI |
| T4.2 | Entire tower, full shifted divisor and residues, corrected nonconstant first-band equivalence | H-GEO, H-GUI, H-LAP, H-SZ |
| T4.3 | Finite graph orbit/determinant identities; Selberg/Ruelle quotient and exact comparison | Graph part is elementary; H-GEO for convergent hyperbolic products; H-SZ for continuation; H-GUI for the flat-trace interpretation |
| T5.1 | Tempered scattering transform, negative prime comb, explicit archimedean distribution, and $+1/2$ boundary correction | H-PHI, H-ZETA, H-GAMMA |
| T5.2 | Rate-$1/4$ damping equality of defined prime measures and signed scattering identification | No standard input for the weight multiplication; H-PHI, H-ZETA, H-GAMMA for the scattering identification |
| T6.1 | This dependency and correction audit | The preceding propositions only |

<1>1. **Standard facts that must be supplied, and facts not used.**

PROOF. T4.1 invokes H-GUI exactly once, to turn the flat trace into an orbit measure; its remaining steps use the determinant in T3.1 and the counting consequence of H-GEO. T4.2 adds the full entire Selberg zero divisor and compact Laplace spectral theory; it does not derive them from Guillemin's formula. T5 invokes only the stipulated modular scattering formula, the specifically enumerated zeta analytic facts including the zero-free-line bound, and the gamma identities. H-AN is isolated to the closed-heat interpretation in T2.2. These are the additional research-level analytic/geometric inputs, and none has been silently proved by a formal product manipulation.

The **Selberg trace formula itself is not invoked** as a separate input. H-SZ is a substantial standard theorem which is commonly proved using that trace formula; taking its conclusion as an explicit hypothesis does not reproduce its proof. No prime-geodesic theorem, anisotropic-resolvent identification, functional-model theorem, trace-class theorem for $Z_{\mathrm{ch}}$, RH, or $1/4$ conjecture is proved or used to establish the main identities. The explicit-formula discussion in T5.2 <1>3 audits the supplied notebook formula; it is not an additional hypothesis for the measure-damping corollary. $\square$

<1>2. **Corrections to false or imprecise drafted statements.**

PROOF. Each correction is forced by a displayed calculation above:

1. A cocompact Fuchsian group need not be torsion-free. The compact surface zero-divisor and genus formulas here require torsion-freeness. The modular calculation is a separate orbifold-with-cusp case.
2. The all-prime direct sum has a locally defined positive-time **orbital** trace. Generic smeared direct-sum operators are not trace class because their constant modes give a nonzero eigenvalue of infinite multiplicity. The undamped prime comb is not globally tempered, and its coefficient at time zero would diverge.
3. A circle translation is a unitary flow, with anti-self-adjoint first-order generator. Calling that generator a dissipative Lindbladian without an additional construction confuses it with a sum of squares.
4. The vector fields in T2 are left-invariant fields with flows $g\exp(tB)$. Under precisely those conventions, the constant is $c=1$ and the two-jump scalar generator is $-2\Delta$. The compact-direction coefficient in the Casimir is negative, so the unrestricted Casimir is not that diffusion generator.
5. The tensor-product Lindbladian has $+\frac12\sum d(\pi\otimes\bar\pi)(X_j)^2$, because its anti-self-adjoint generators carry two factors of $i$ when converted to self-adjoint jumps. For the two noncompact jumps it is $2\Omega_{\pi\otimes\bar\pi}+B_W^2/2$, not simply the Casimir. Domains and any closed completely positive realization require separate attention; a gap is not established.
6. With $D=\prod_{j\ge1}Z_{\mathrm{Sel}}(\sigma+j)$, the correct identity is $\Lambda_{\mathrm{fl}}=+D'/D$. A negative derivative applies to $D^{-1}$. Absolute convergence already holds for $\operatorname{Re}\sigma>0$.
7. Meromorphic continuation of each factor alone does not identify poles with shifted zeros without allowing cancellations or new poles. H-SZ supplies **entireness and the full divisor**; a normally convergent nonvanishing tail is also proved. A logarithmic derivative has simple poles with residues equal to zero orders, not poles whose orders equal those multiplicities.
8. The constant eigenvalue has $r_0=i/2$, giving $\sigma=0,-1$ in its first translate. Remove that mode for the first-band $1/4$ criterion. A positive exceptional eigenvalue has $r_j=i\nu_j$ with $0<\nu_j<1/2$, and $\lambda_j=1/4$ has $r_j=0$ and doubled coincident spectral zeros. Spectral and topological orders add at $s=0$ and at their shifted images.
9. For the corrected flat-determinant convention, the graph counterpart of $D$ is $\det(1-uT)$; the counterpart of $D^{-1}$ is $\det(1-uT)^{-1}$. The missing graph Jacobian is a discrete-counting fact, not a deduction from the phrase “the tree is one-dimensional.” The Ruelle zeta in this file is the direct Euler product and equals $Z_{\mathrm{Sel}}(s)/Z_{\mathrm{Sel}}(s+1)$.
10. For the stipulated scattering multiplier $-\frac12\phi'/\phi$, the prime atoms have **negative** weights. The exact identity is $C=-P+A$. Fourier-sign reversal alone cannot make them positive, since the multiplier is even.
11. The ordinary real-line value of $q(1+2ir)+q(1-2ir)$ differs from its common right-Abel boundary distribution by $+\pi\delta_0(r)$. In time this is $+1/2$. The archimedean-plus-boundary term must specify its finite-part extension and this smooth pole correction, as T5.1 does. Neither individual boundary logarithmic derivative is an ordinary bounded function near zero.
12. $e^{-t/4}$ changes the defined prime weights $\Lambda_{\mathrm{vM}}(n)n^{-1/2}$ at $2\log n$ into $\Lambda_{\mathrm{vM}}(n)/n$. This proves a measure identity after subtraction and sign choice. It does not validate the notebook's pure-prime description of the **full** compressed-semigroup trace, whose own explicit formula includes other terms and different sign/scaling bookkeeping. It proves nothing about RH.

These corrections are assertions with proofs in the indicated propositions, not alternative conjectural normalizations. $\square$

<1>3. **No promotion of conditional or unproved claims.**

PROOF. Every proposition has a complete argument for its stated conclusion under its displayed inputs. The representation gap discussion is explicitly a remark. A literal operator-theoretic continuous Ihara–Bass compression, actual anisotropic resonant spaces, a full channel/scattering trace identity, and a proof of any Ramanujan/$1/4$/RH property remain unestablished. They are not marked `proved-here` or silently rounded up to a theorem. $\square$

**Status:** `proved-here` as an audit of the preceding conditional and direct proofs.

**Sanity checks (not proofs).** Inline, non-writing Python calculations checked the scattering multiplier against logarithmic differentiation of H-PHI at $r=0.03,0.7,2.3$, with residuals below $5\cdot10^{-41}$ at 40-digit precision. Pairing T5.1 with $h(t)=e^{-t^2/2}$ gives $\langle A,h\rangle\approx-0.487137717291990449$, $\langle P,h\rangle\approx0.342066654304729763$, and hence $\langle C,h\rangle\approx-0.829204371596720212$. Independent quadrature of the original scattering multiplier against the Fourier-transformed Gaussian agreed to $3\cdot10^{-14}$. This checks both the negative prime sign and the $+1/2$ term, without replacing the distributional proof.

RESULT: T1.1–T1.3's finite-product claims, T2.1–T2.3 on their stated algebraic domains, T3.1, the graph part of T4.3, the prime-measure damping part of T5.2, and T6.1 are `proved-here` over H-BASE; T1.3's disjointness from the continued Riemann zeta zeros uses H-ZETA and H-GAMMA; the closed heat realization uses H-AN; T4.1–T4.2 and the hyperbolic continuation comparisons are conditional on their explicit geometric/trace/Selberg inputs; T5.1 and the scattering identification in T5.2 are conditional on H-PHI, H-ZETA, H-GAMMA. The trace interpretation, determinant sign and graph inverse, constant-mode first band, zero multiplicities, scattering prime sign and boundary constant, and full-channel-trace claim are corrected explicitly. No RH, $1/4$ property, spectral gap, or full operator-trace identification is claimed.
