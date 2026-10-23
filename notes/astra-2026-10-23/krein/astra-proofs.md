# Lane K: Krein–Ramanujan rigidity

Author: `codex:gpt-6-astra`. Date: 2026-10-23. Research proposals only; nothing registered.

## §0. Conventions and the sign check — PROVED

Use the setting in the lane brief, with $H=I_n\otimes\eta$, $A=A_\rho$, $A^\dagger H=HA$, and vertex-major fibre ordering. On the doubled label space set

\[
J=\begin{pmatrix}0&H\\-H&0\end{pmatrix},\quad
M=\begin{pmatrix}A&-qI\\I&0\end{pmatrix},\quad
V=qM^{-1}=\begin{pmatrix}0&qI\\-I&A\end{pmatrix}.
\]

Direct block multiplication gives
\[
M^\dagger JM=\begin{pmatrix}A^\dagger H-HA&qH\\-qH&0\end{pmatrix}=qJ,
\qquad Q=\tfrac12J(M-V)=\begin{pmatrix}H&-HA/2\\-HA/2&qH\end{pmatrix}.
\]
Thus **the similitude has the stated positive sign**, and $Q$ is an ordinary Hermitian matrix (not merely an operator self-adjoint for an indefinite form). Also $M^\dagger QM=qQ$. Here $J$ is skew-Hermitian; it is the complex sesquilinear version of the Casoratian pairing, not an additional Hermitian metric.

The tutorial 6a–6d and `graph-ihara.md` §4 actually use
$M_{\rm page}=\left(\begin{smallmatrix}0&-I\\qI&A\end{smallmatrix}\right)$, with labels $(f_k,-f_{k+1})$. The brief uses $(f_{k+1},f_k)$. They are related by the symplectic coordinate change $R=\left(\begin{smallmatrix}0&I\\-I&0\end{smallmatrix}\right)$, since $RM R^{-1}=M_{\rm page}$ and $R^\dagger JR=J$. Consequently
\[
Q_{\rm page}=R^{-\dagger}QR^{-1}=\begin{pmatrix}qH&HA/2\\HA/2&H\end{pmatrix}.
\]
There is **no overall sign reversal**. The off-diagonal sign and order of diagonal blocks change with labels. With the tutorial labels, $\Omega=-W_k$; with the brief labels the same equality holds for $W_k=f_k^\dagger Hh_{k+1}-f_{k+1}^\dagger Hh_k$. All forms here live on labels; the labelling map's kernel on edge space is not a kernel of $J$.

We distinguish full-spectrum Ramanujan (all adjacency eigenvalues in the closed band, semisimple) from reduced Ramanujan (explicit parallel/anti-parallel endpoint sectors removed). A closed-band adjacency eigenvalue at $\pm2\sqrt q$ is allowed by the brief, but produces a Jordan block of $M$ and a kernel of $Q$; it does not give a positive invariant metric for $M/\sqrt q$.

## §1. K1(a) — PROVED; bounded does not mean automatically Ramanujan

Gauge-fix a spanning tree to identity by SU(1,1) transformations. If the holonomy has compact closure, average any positive Hermitian form over that compact group to obtain $h>0$. Writing $h=L^\dagger L$, the constant gauge $L$ makes all cotree matrices unitary. Conversely a vertexwise positive invariant metric, pulled to the base vertex, makes holonomy bounded. The vertexwise similarity conjugates the whole adjacency, preserving its spectrum and Jordan structure. The transformed adjacency is Hermitian. Therefore the bounded field is Ramanujan **iff its unitary representative satisfies the same band test, with the same endpoint-sector convention**. This proves K1(a), not an implication from boundedness to the band bound.

In fact every compact subgroup of SU(1,1) fixes a point of the disc; moving it to the origin by SU(1,1) puts all holonomies in $K=\{\operatorname{diag}(e^{i\phi},e^{-i\phi})\}$. Thus the field is already SU(1,1)-gauge-equivalent to two inverse scalar fluxes. General SU(2) matrices cannot be conjugated into SU(1,1) this way; the bounded sampler must use $K$.

For the endpoint convention, put $d=q+1$. For a unitary field,
\[
d\|f\|^2-\langle f,Af\rangle=\sum_{\{x,y\}}\|f(x)-U_{xy}f(y)\|^2,
\quad d\|f\|^2+\langle f,Af\rangle=\sum_{\{x,y\}}\|f(x)+U_{xy}f(y)\|^2.
\]
Hence $+d$ is exactly the space of parallel sections, naturally isomorphic to $\operatorname{Fix}(\Gamma_x)$. The $-d$ space consists of anti-parallel sections, determined by $\rho(c)v=(-1)^{|c|}v$ for every closed walk $c$. On a bipartite graph this is the alternating partner of the parallel space. On a non-bipartite graph a nontrivial sign local system can have $-d$ without $+d$. These are the only extremal sectors for unitary fields; remove them only under an explicitly reduced convention. For a general reducible U(2) representation the multiplicities are precisely the dimensions of these two invariant spaces. In the bounded SU(1,1) defining representation a nonzero fixed vector forces all holonomy to be identity, so the parallel multiplicity is two, not one. A nontrivial unipotent holonomy can fix a null vector and has no such conclusion.

Outside the bounded case, the numerical value $q+1$ does not by itself identify a trivial sector: cancellation can produce it without any fixed vector. For example theta with the fixed $h$ below and $g=\left(\begin{smallmatrix}9&4\sqrt5\\4\sqrt5&9\end{smallmatrix}\right)$ has $A^2=9I$ but $\det(g-I)=-16\ne0$. Its $\pm3$ modes are nontrivial and outside the $q=2$ band. “Remove trivial modes” must therefore refer to geometrically identified parallel sectors, not a numerical eigenvalue filter.

The brief's phrase “equivalently, the Ramanujan locus is exactly the bounded locus” does not follow even from its conjectured K1(b): a bounded field must also pass the unitary band test. Below, K1(b) itself is refuted.

### K1(b) — REFUTED, including nonelementary holonomy on K₄

The smallest loopless multigraph counterexample is the two-edge cycle $(q=1)$: put $I$ and $u=\left(\begin{smallmatrix}1+i&1\\1&1-i\end{smallmatrix}\right)$ on its two forward edges. This is noncentral unipotent holonomy, but $A^2=4I$, so the adjacency is semisimple with eigenvalues $+2,-2$, each twice. It passes the brief's **closed-band** definition. The transfer $M$ is defective at these band edges. Thus even one-cycle rigidity needs an ordinary simple cycle or a strict-band qualification.

A strict-band, nonelementary counterexample has two vertices and three parallel edges $theta, (q=2)$. Put the three forward matrices equal to $I,g,h$, where
\[
g=\begin{pmatrix}5/4&3/4\\3/4&5/4\end{pmatrix},\qquad
h=\operatorname{diag}((-3+4i)/5,(-3-4i)/5).
\]
They are exactly in SU(1,1). The eigenvalues of $g$ are $2,1/2$, so holonomy is unbounded. The hyperbolic $g$ has boundary fixed points $\{1,-1\}$; the disc rotation $h$ does not preserve that pair, and fixes no boundary point. Thus the group generated by $g,h$ is nonelementary. A group containing a hyperbolic element and having a finite boundary orbit would have to preserve its endpoint pair, which proves the assertion without a numerical group test.

Set $S=I+g+h$. For two-by-two matrices adjugation is linear; hence the reverse-edge sum is $T=I+g^{-1}+h^{-1}=\operatorname{adj}S$. Thus
\[
A=\begin{pmatrix}0&S\\T&0\end{pmatrix},\quad
A^2=\det(S)I_4,\quad \det S=3+\operatorname{tr}g+\operatorname{tr}h+\operatorname{tr}(gh^{-1})=14/5.
\]
The spectrum is $\{\sqrt{14/5},\sqrt{14/5},-\sqrt{14/5},-\sqrt{14/5}\}$, strictly in the band, and the minimal polynomial divides $x^2-14/5$, which is squarefree. This is an exact certificate, with no precision assumption. An even simpler elementary unbounded example is $I,g,-I$, for which $A^2=I$. With two parallel edges $(q=1)$, hyperbolic holonomy instead fails the band test; three edges are minimal for this strict-band, loopless two-vertex construction.

**Smallest simple regular graph example.** On K₄ use tree edges $01,02,03$ with identity, and cotree matrices
\[
\rho(12)=-I,\quad \rho(13)=g,\quad \rho(23)=h.
\]
The same holonomy argument gives a nonelementary group. Exact rational-complex arithmetic gives
\[
\det(xI-A)=p(x)^2,\quad
p(x)=(x-1)(x^3+x^2-5x-29/5),\qquad p(A)=0.
\]
The cubic has one root in each of $(-21/10,-2)$, $(-13/10,-6/5)$, $(22/10,24/10)$: the signs at each pair of rational endpoints differ, these intervals are disjoint, and a cubic has only three roots. The remaining root is 1. All intervals lie strictly in $(-2\sqrt2,2\sqrt2)$, and $p$ is squarefree, proving both real spectrum and semisimplicity exactly. The check script prints the endpoint signs, the annihilator identity, and high-precision roots. No eigenvalue is a trivial endpoint. Among simple connected regular graphs with $q\ge1$, the smaller graphs are cycles, so K₄ is minimal by vertex count.

There is also an **unbounded isospectral family**: replace $h$ by $I$, keep $\rho(12)=-I$, and let $\rho(13)=g_t=\exp(t\sigma_x)$. Then for every real $t$,
\[
\det(xI-A_t)=[(x^2-1)(x^2-5)]^2,\quad (A_t^2-I)(A_t^2-5I)=0.
\]
Thus the hyperbolic translation length can grow without bound while the spectrum remains strictly Ramanujan. This disproves even a putative monotone spectral escape principle. The nonelementary family with $h$ as above is analysed in §3.

### The two-by-two symmetry the proposed simple-spectrum search misses — PROVED

Every SU(1,1) matrix has the form $\left(\begin{smallmatrix}a&b\\\bar b&\bar a\end{smallmatrix}\right)$. Let $C=(I_n\otimes\sigma_x)\circ\text{conjugation}$. Then
\[
C^2=1,\quad CA=AC,\quad [Cu,Cv]_H=-\overline{[u,v]_H}.
\]
Every real generalized eigenspace is $C$-invariant and has balanced positive/negative inertia. A real semisimple eigenspace is nondegenerate for $H$: it is orthogonal to all other generalized eigenspaces and their sum is the whole space. Consequently its signature is $(m_\lambda,m_\lambda)$, not a single sign. In particular **real simple eigenvalues do not occur** in this defining representation. Individual eigenvectors in a mixed eigenspace can have either sign or be null; counting the arbitrary vectors returned by `eig` is invalid.

For an algebraic version let $E=I_n\otimes\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$. The determinant-one identity on every edge implies $A^TE=EA$. Hence $E(xI-A)$ is skew-symmetric and
\[
\det(xI-A)=\left[\operatorname{pf}(E(xI-A))/\operatorname{pf}(E)\right]^2=:p_\rho(x)^2.
\]
The monic degree-$n$ polynomial $p_\rho$ is real because $CA=AC$. If its roots are simple, $A$ is semisimple: each two-dimensional generalized eigenspace is nondegenerate for the alternating form $E$, and a self-adjoint endomorphism of a two-dimensional symplectic space is scalar. This also provides a stable numerical certificate: isolate the $n$ reduced roots, rather than test numerical splitting of $2n$ double roots.

**SHARPENED local statement.** If $p_\rho$ has distinct real roots strictly inside the band, the same holds in an open neighbourhood in SU(1,1) gauge-field space. Reality follows from continuity and conjugation symmetry of a real polynomial with simple roots. Therefore Ramanujan fields with unbounded, nonelementary holonomy occur in open sets, not merely isolated cancellations. Boundedness remains equivalent to a *vertexwise* positive parallel metric; real semisimple spectrum gives a positive metric for the whole adjacency, which need not be vertexwise.

### One-cycle correction — PROVED

For Cₙ, $n\ge3$, let $T$ be the twisted forward shift, so $T^n$ is conjugate to the holonomy $g$ on each fibre and $A=T+T^{-1}$. If $\nu$ is an eigenvalue of $g$, the correct formula is
\[
\operatorname{spec}A=\{r+r^{-1}:r^n=\nu,\ \nu\in\operatorname{spec}g\}.
\]
The brief omitted the $n$-th root: $\zeta\mu$ is correct only if $\mu^n=\nu$. Hyperbolic holonomy has $|\nu|\ne1$; its roots give a non-real eigenvalue or a real one outside $[-2,2]$. Noncentral parabolic holonomy has $\nu=\pm1$ and nontrivial Jordan blocks in $T$. Applying $r+r^{-1}$ preserves a size-two block whenever $1-r^{-2}\ne0$. For $n\ge3$ such a root exists, so $A$ has a nontrivial Jordan block. At $r=\pm1$ the derivative vanishes and that particular block disappears. This is why a blanket claim that every parabolic mode is defective would be false. The two-edge cycle is also handled directly: $A^2=(2+\operatorname{tr}g)I$; for trace $+2$ one obtains a boundary semisimple example even for noncentral parabolic $g$. Thus the cycle rigidity statement requires the ordinary simple-cycle hypothesis $n\ge3$, and the minimality claim above concerns strict interior-band counterexamples or hyperbolic holonomy.

## §2. K2 — SHARPENED; the unconditional bounded count and lower-semicontinuity conjectures are REFUTED

The well-defined multiplicity convention is
\[
\kappa_B(A)=\sum_{\lambda\in[-2\sqrt q,2\sqrt q]}n_-(H|_{E_\lambda}),
\]
when the real eigenspaces in question are semisimple, with $E_\lambda=\ker(A-\lambda I)$. It is invariant under SU(1,1) vertex gauges by congruence. A general GL(2,C) gauge requires transporting $H$ along with $A$; keeping the old coordinate matrix $H$ would be a different question.

**PROVED general formula (no boundedness needed).** If all real eigenvalues in the closed band are semisimple, then
\[
\boxed{\kappa_B(A)=\tfrac12\sum_{\lambda\in B}\dim E_\lambda
=\#\{\text{real roots of }p_\rho\text{ in }B\},}
\]
with algebraic multiplicities in the last count. This follows from the anti-isometry $C$ and nondegeneracy proved in §1. For a bounded field every eigenvalue is real and semisimple, so **$\kappa_B=n$ iff the field is full-spectrum Ramanujan**. The *total* negative index over all eigenspaces is always $n$; the in-band index need not be. After removing trivial sectors, subtract their negative inertia from $n$ before making the analogous assertion.

**Exact bounded counterexample to the proposed unconditional $\kappa=n$.** On theta take the forward edges $I,I,R$, where $R=\operatorname{diag}((4+3i)/5,(4-3i)/5)$. The holonomy is compact with no fixed vector, but $A^2=(41/5)I$. Both distinct eigenvalues are outside the $q=2$ band, so $\kappa_B=0$, whereas $n=2$. This also disproves “bounded locus equals Ramanujan locus” in its other direction. Even diagonal inverse-U(1) fluxes give $\kappa=n$ only when *all* their scalar modes pass the band test.

### Lollipops / arbitrary unicyclic graphs — PROVED formulas, with the regularity correction

A finite connected graph with exactly one cycle and genuine attached trees is **not regular**: it has leaves. The only connected finite regular unicyclic graphs are cycles with $q=1$. Thus the request “lollipop, any $q$” cannot literally use the fixed regular setting. The following is an adjacency formula on the irregular graph; $b=2\sqrt q$ may be an externally chosen cutoff, but is not an Ihara regular-graph parameter. The true irregular Bass term uses $D-I$, not $qI$.

Let $Y$ have unique simple cycle $C_m$, $m\ge3$, $N$ vertices, and $F=Y\setminus V(C_m)$, including all remaining attached forest vertices. Write $\chi_G(z)=\det(zI-A_G)$, with $\chi_\varnothing=1$. Gauge all edges except a closing cycle edge to identity and give that edge holonomy $g$. Then
\[
\boxed{p_g(z)=\chi_Y(z)+(2-\operatorname{tr}g)\chi_F(z),\qquad
\det(zI-A_\rho)=p_g(z)^2.}
\]
For diagonalizable $g$, diagonalize the fibre: the two scalar flux determinants depend only on $w+w^{-1}=\operatorname{tr}g$. In the determinant expansion the only flux-dependent terms traverse the whole cycle in one of its two orientations, contributing $-(w+w^{-1})\chi_F$. This proves the formula; polynomial continuation proves it also for noncentral parabolic $g$. At semisimple real roots,
\[
\kappa_b=\sum_{\lambda\in[-b,b]}\operatorname{mult}_\lambda p_g.
\]
This is a finite explicit formula in graph characteristic polynomials, valid for arbitrarily shaped attached trees. For a cycle with a single path of $\ell$ extra vertices attached at a cycle vertex, set $U_{-1}=0$, and use Chebyshev polynomials $T_m,U_\ell$:
\[
p_g(z)=U_\ell(z/2)\bigl(2T_m(z/2)-\operatorname{tr}g\bigr)
-U_{\ell-1}(z/2)U_{m-1}(z/2).
\]
For $\ell=0$, this recovers the corrected cycle formula. It also provides a direct root count via Sturm's theorem whenever the trace is rational.

For parabolic $g=\varepsilon(I+N)$, $N^2=0\ne N$, $\varepsilon=\pm1$, the characteristic polynomial alone does not decide Jordan structure. In a fibre Jordan basis,
\[
A\sim\begin{pmatrix}B_\varepsilon&\varepsilon K\\0&B_\varepsilon\end{pmatrix},\qquad
K=E_{uv}-E_{vu},
\]
where $B_\varepsilon$ is the real symmetric scalar adjacency with closing-edge sign $\varepsilon$. If $P_\lambda$ is its orthogonal spectral projector and $m_\lambda$ its eigenvalue multiplicity, put $r_\lambda=\operatorname{rank}(P_\lambda K P_\lambda)$. Off-resonant blocks can be removed by a Sylvester equation. There are exactly $r_\lambda$ Jordan blocks of size two at $\lambda$, and $2m_\lambda-2r_\lambda$ of size one. Thus semisimplicity holds exactly when every compression vanishes. In particular **a simple spectrum of $B_\varepsilon$ makes the parabolic twisted adjacency semisimple**, since the diagonal of a real skew matrix vanishes. Trees can destroy the scalar cycle degeneracies that produced parabolic Jordan blocks.

At a defective root the brief's Krein-sign count is not defined on the degenerate eigenspace. If extended to the negative inertia of the eigenspace anyway, its inertia is $(m_\lambda-r_\lambda,m_\lambda-r_\lambda,r_\lambda)$. To see this, choose the unipotent-invariant fibre form $\left(\begin{smallmatrix}0&i\alpha\\-i\alpha&0\end{smallmatrix}\right)$, $\alpha\ne0$; on the kernel the second component belongs to $\ker(P_\lambda K P_\lambda)$, and the remaining first-component directions are radical. This extended count must not be confused with the inertia $(m_\lambda,m_\lambda)$ on the full generalized eigenspace.

### Theta — PROVED complete formulas

With tree edge $I$ and cotree edges $g,h$, put
\[
\delta=3+\operatorname{tr}g+\operatorname{tr}h+\operatorname{tr}(gh^{-1})\in\mathbb R.
\]
Then $A^2=\delta I$. For $\delta>0$, the eigenvalues are $\pm\sqrt\delta$, each with signature $(1,1)$, and
\[
\kappa_B=\begin{cases}2,&0<\delta\le8,\\0,&\delta>8.\end{cases}
\]
For $\delta<0$, the spectrum is $\pm i\sqrt{-\delta}$, each twice, and $\kappa_B=0$. For $\delta=0$, either $S=I+g+h=0$, in which case $A=0$ is semisimple and $\kappa_B=2$, or $S\ne0$, in which case $S$ and $\operatorname{adj}S$ have rank one, $A$ has two size-two nilpotent blocks, and the real eigenspace is totally null (the original count is undefined; its inertia extension is zero). Thus theta is Ramanujan exactly for $0<\delta\le8$ or $S=0$, regardless of boundedness.

### “Maslov-type lower semicontinuity” — REFUTED; corrected local principle PROVED

Already on the *unbounded nonelementary locus*, take $g=g_t$, and $h$ from §1. Then $\delta=(9+4\cosh t)/5$. At $\cosh t=31/4$, $\kappa_B=2$, but on the adjacent outside-band side $\kappa_B=0$. The use of a **closed** band therefore contradicts lower semicontinuity.

Even deleting band edges does not give a global lower-semicontinuity theorem at semisimple collisions. On theta let $r=e^{2\pi i/3}$, $R=\operatorname{diag}(r,\bar r)$, and use $I,e^{t\sigma_x}R,R^{-1}$. At zero their sum is zero, so $A_0=0$, $\kappa_B=2$. For every nonzero $t$,
\[
S_t=(e^{t\sigma_x}-I)R,\quad \delta_t=2-2\cosh t<0,
\]
so $\kappa_B=0$. The holonomy is unbounded for $t\ne0$, because the product of the two cotree generators is $e^{t\sigma_x}$. This interior example has a bounded central field; the preceding edge example is wholly unbounded.

The correct general statement is the root-count formula above, with local constancy on strata having simple reduced real roots, separated from each other and from the band edges. Changes are root crossings or real/non-real collisions of the reduced polynomial, not a new holonomy index. The inertia of a real root space is always balanced. No additional general conjecture is needed for this count; a global classification of which holonomies realize prescribed reduced spectra remains **OPEN**.

## §3. K3 — PROVED with strict-band and multiplicity qualifications

On the label plane over a real eigenvector $v$, with $[v,v]_H=s\ne0$,
\[
Q|_{(\mathbb Cv)^2}=s\begin{pmatrix}1&-\lambda/2\\-\lambda/2&q\end{pmatrix}.
\]
For $|\lambda|<2\sqrt q$ this is positive definite iff $s>0$, and negative definite iff $s<0$. For a whole semisimple eigenspace of signature $(a,b)$, the label-space signature is $(2a,2b)$. At a band edge it is $(a,b,a+b)$; “positive” must then mean semidefinite, not definite. For an out-of-band real eigenspace of dimension $m$, it is $(m,m)$. Thus the page's assertion about a *chosen negative vector's mode plane* is right in the strict band, even though the whole SU(1,1) adjacency eigenspace is mixed, not definite.

**PROVED general semisimple inertia formula.** For any $H$-self-adjoint semisimple adjacency, let $r_+,r_-$ count the positive/negative directions over strictly in-band real eigenspaces, $e_+,e_-$ the directions at band edges, $o$ the total multiplicity of real out-of-band eigenvalues, and $z$ the total multiplicity of non-real eigenvalues (both conjugate halves included). Then
\[
\boxed{\operatorname{In}(Q)=
(2r_++e_++o+z,\ 2r_-+e_-+o+z,\ e_++e_-).}
\]
With the brief's *closed-band* $\kappa=r_-+e_-$, the negative index is $2\kappa-e_-+o+z$. Every non-real conjugate pair of multiplicities $m,m$ contributes $(2m,2m)$ on labels. This follows either by its neutral paired form or by the following Schur congruence:
\[
Q\ \cong\ H\oplus H(qI-A^2/4).
\]
The second matrix is Hermitian because $A^\dagger H=HA$. On a real scalar eigenspace its sign is the sign of $q-\lambda^2/4$ times the $H$-sign. On a non-real pair its nondegenerate off-diagonal pairing has equal positive/negative inertia, even when $\lambda^2$ happens to be real negative.

**Stronger formula for this SU(1,1) representation, including defective fields.** The anti-linear involution $\widetilde C=C\oplus C$ is an anti-isometry of $Q$ too, so its positive and negative indices are equal. The Schur congruence gives
\[
d_0=\dim\ker(A-2\sqrt q I)+\dim\ker(A+2\sqrt q I),\qquad
\boxed{\operatorname{In}(Q)=(2n-d_0/2,\ 2n-d_0/2,\ d_0).}
\]
Here geometric multiplicities are used even at defective eigenvalues; $q>0$. Thus **away from adjacency band-edge eigenvalues the full Weil form always has signature $(2n,2n)$**, whether the spectrum is Ramanujan, out of band, complex, or defective. Its full index cannot detect spectral escape in this balanced representation. Positivity on selected positive-type planes and positivity of the full form are different statements.

Consequently “RH and positivity separate” survives, and is stronger than merely a bounded/unbounded distinction. Both the bounded and unbounded full-spectrum Ramanujan examples have an indefinite canonical $Q$. On the other hand $M/\sqrt q$ does have *some* positive invariant Hermitian metric whenever $A$ is real semisimple and strictly in band: diagonalize $M/\sqrt q$, whose eigenvalues are then on the unit circle, and pull back the Euclidean metric. This does not make the fixed $Q$ positive. At an adjacency band edge or a nontrivial adjacency Jordan block that invariant positive metric does not exist. Compactifying the holonomy changes neither the inherited indefinite form nor this distinction.

### Exact interior Krein collision on K₄ — PROVED, numerically checked

Keep the star tree and $\rho(12)=-I$, $\rho(23)=h$ of §1, and set
\[
\rho(13)=g_t=e^{tX},\qquad X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad t\ge0.
\]
For every $t>0$ the holonomy is unbounded and nonelementary. Write $c=\cosh t$. Exact half-trace Newton identities (also directly the Pfaffian) give
\[
p_t(x)=(x-1)\left(x^3+x^2-5x-\frac{9+16c}{5}\right),\qquad
\operatorname{disc}(\text{cubic})=-\frac{64}{25}(2c+3)(54c-79).
\]
At $t=0$ the distinct reduced eigenvalues are $-\sqrt5,-1,1,\sqrt5$. The first non-real eigenvalues appear just after
\[
\boxed{t_* = \operatorname{arcosh}(79/54)
=\log\frac{79+5\sqrt{133}}{54}
=0.9285326263124587\ldots.}
\]
At this parameter
\[
p_{t_*}(x)=(x-1)(x-7/3)(x+5/3)^2.
\]
The colliding modes meet at $-5/3$, **strictly inside the band**. They started at $-\sqrt5$ and $-1$, while the positive moving root increases only to $7/3<2\sqrt2$; differentiating the cubic shows these motions are monotone up to the collision. Thus no earlier band-edge escape occurs. Exact rank calculations give
\[
\operatorname{rank}(A_{t_*}+5I/3)=6,\qquad
\operatorname{rank}(A_{t_*}+5I/3)^2=4.
\]
The colliding full eigenvalue has algebraic multiplicity four and two size-two Jordan blocks. Before collision each of the two real eigenspaces has signature $(1,1)$; their combined $(2,2)$ space supplies both signs. At collision the eigenspace is totally null within this four-dimensional generalized space; afterwards there is a complex conjugate pair, each of multiplicity two. This is the SU(1,1) version of an opposite-sign Krein collision, with the forced doubling retained.

For $\delta=c-79/54>0$ small, the two reduced roots have expansions
\[
x_\pm=-5/3-\delta/10+O(\delta^2)
\ \pm i\left(\frac2{\sqrt5}\sqrt\delta+O(\delta^{3/2})\right).
\]
On the two sides of the first collision, $\kappa_B$ drops from $4$ to $2$, while $\operatorname{In}(Q)=(8,8,0)$ throughout, including at the defective parameter. The first *real* root crosses the upper band edge later, at $\cosh t=(31+30\sqrt2)/16$. The isospectral family in §1 shows that this collision scenario is a property of the chosen other generators, not of hyperbolic $g_t$ alone.

## Correction ledger

| Brief or record assertion | Status and correction |
|---|---|
| Unbounded holonomy prevents Ramanujan adjacency | **REFUTED.** Nonelementary rational examples on theta and K₄; an open locus and an unbounded isospectral K₄ family. |
| Ramanujan locus equals bounded locus | **REFUTED in both directions.** Boundedness still needs the unitary spectral band test. |
| General SU(2), conjugated by a hyperbolic element, supplies bounded SU(1,1) samples | **REFUTED.** Use the common compact torus $U(1)\oplus U(1)^{-1}$, conjugated by a single SU(1,1) element. |
| Search for real simple full adjacency spectrum | **IMPOSSIBLE here.** The characteristic polynomial is a square; the degree-$n$ reduced polynomial can have simple roots. |
| Assign a Krein sign to every numerical eigenvector | **ILL-DEFINED at multiplicity.** Use inertia of the entire real eigenspace; all semisimple ones are balanced. |
| Every bounded field has in-band $\kappa=n$ | **REFUTED.** This is true iff its entire spectrum passes the band test; the total, unfiltered index is always $n$. |
| $\kappa$ is lower semicontinuous on the unbounded locus | **REFUTED.** A closed-band crossing on nonelementary theta already violates it. |
| Lollipops with trees are finite regular graphs for arbitrary $q$ | **INCONSISTENT.** Supply the irregular adjacency formula and an external cutoff, or restrict to cycles. |
| Cycle formula uses a holonomy eigenvalue directly as $\mu$ | **MISSING ROOT.** It needs $\mu^n=\nu$, with $\nu$ a holonomy eigenvalue. |
| Every parabolic one-cycle adjacency is defective | **QUALIFY.** True for ordinary simple cycles, false for the two-edge multicycle; attached trees may also remove scalar degeneracies. |
| The brief and page use the same $M$ matrix | **COORDINATE MISMATCH.** They are symplectically conjugate; the Weil form has different cross terms, with no overall sign reversal. |
| $Q$ is Hermitian “for the indefinite inner product” | **CLARIFY.** $Q=\tfrac12J(M-V)$ is an ordinary Hermitian sesquilinear form. $A$ is $H$-self-adjoint. |
| Closed-band adjacency RH equals semisimple critical-circle transfer | **FALSE AT THE EDGE.** At $\lambda=\pm2\sqrt q$, adjacency can be semisimple while the companion transfer is defective and $Q$ is singular. |
| A degree-valued eigenvalue is automatically trivial | **FALSE outside the unitary argument.** Identify parallel/anti-parallel sections geometrically. |
| The full negative index of $Q$ detects spectral escape | **FALSE for the defining SU(1,1) representation.** Away from band edges it is always $2n$, even through interior Krein collisions. |

## Source and verification scope

All graph identities, counterexamples, inertia formulas, and the collision parameter above are proved here without assuming RH. The finite-dimensional background is Gohberg–Lancaster–Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), especially Chapter 5, “Canonical Forms”, pp. 73–123, and the chapters on stability and definite invariant subspaces; bibliographic metadata and chapter scope were checked against the [publisher's contents](https://link.springer.com/book/10.1007/b137517). No inaccessible theorem text is quoted or used in place of the elementary arguments. The related primary reference [Lancaster–Rodman, “Canonical forms for symmetric/skew-symmetric real matrix pairs under strict equivalence and congruence”](https://doi.org/10.1016/j.laa.2005.03.035) treats the skew-Hamiltonian canonical-form setting; the Pfaffian and two-dimensional arguments here suffice for the needed doubling.

Notebook inputs read: the binding brief; HANDOFF.md sessions 2026-10-22 and 2026-10-06; the requested portions of data-ladder.md and the page index; gauge-groups.md SU(1,1)/Next; graph-ihara.md §§4,6; lattice-tower.md §5 and its precision; tutorial 6a–6d and the Ω glossary entry; and thm:deninger-invariant-polarisation in report/sections/04q_deninger_cmps.tex. The registered theorem concerns existence and multiplicity of invariant polarisations; it does not assert positivity of this particular fixed $Q$. Nothing in this lane refutes that registered distinction.

## Numerical checks for the blind lane

Run from the repository root:

    python3 notes/astra-2026-10-23/krein/checks/krein_scan.py

Or from this lane:

    python3 checks/krein_scan.py

The script writes [checks/output_krein_scan.txt](checks/output_krein_scan.txt). It prints exact certificates first, the one-parameter family next, then every random sample's spectrum, eigenspace inertia, $\kappa$, eigenvector condition number, residual, and $Q$ inertia. Every unbounded Ramanujan candidate includes all cotree generators to 15 decimal places, exact decimal-rational Cayley parameters, and an independent 80-digit reconstruction of the reduced polynomial and its real roots. Exact certificates use SymPy over rational-complex/algebraic fields; random high-precision checks use mpmath and are **NUMERICAL, not interval-certified**. The rigorous refutation does not depend on the random sample.

**NUMERICAL scan results.** Seed 20261023, 64 samples per graph in each ensemble. Compact angles are uniform before rounding their Cayley coordinates to 12 decimal places; hyperbolic radial parameters are uniform on $[0.05,1]$. These are sampling-law-dependent fractions, not Haar probabilities on a noncompact group. Bounded samples use a common fixed hyperbolic conjugate of the diagonal compact torus. Every unbounded sample is certified noncommuting in exact rational arithmetic, which excludes compact holonomy.

| Graph | Fundamental-cycle rank | Bounded: real / Ramanujan | Unbounded: real / Ramanujan | Unbounded Ramanujan fraction | MP80-verified candidates |
|---|---:|---:|---:|---:|---:|
| K₄ | 3 | 64 / 62 | 45 / 43 | 0.671875 | 43 |
| Petersen | 6 | 64 / 63 | 7 / 6 | 0.09375 | 6 |
| K₅ | 6 | 64 / 61 | 30 / 28 | 0.4375 | 28 |
| Cube | 5 | 64 / 64 | 26 / 22 | 0.34375 | 22 |
| Theta | 2 | 64 / 58 | 57 / 50 | 0.78125 | 50 |

All sampled eigenvector condition numbers passed the stated $10^8$ screening threshold, with normalized eigenpair residual below $10^{-10}$. Reality and relative inertia tolerances are $10^{-8}$; clustering tolerance is $10^{-7}$. These thresholds are diagnostic only. For every accepted unbounded sample, the high-precision reconstruction finds $n$ distinct real reduced roots, disjoint real sign brackets of radius $10^{-50}$, positive band margin, and polynomial residual below $10^{-60}$. Distinct reduced roots imply full-adjacency semisimplicity by the proved two-by-two symmetry. The log prints the actual gaps, margins, and residuals. All random real eigenspaces have balanced inertia, and every random full $Q$ has inertia $(2n,2n,0)$; separate exact edge examples test the singular formula.

Six compact checks for a blind reviewer:

1. Theta nonelementary example: $\delta=14/5$, eigenvalue magnitude $1.67332005306815109595634405157\ldots$.
2. K₄ exact example: largest eigenvalue $2.28979824583255790705308826249\ldots$, with $p(A)=0$ exactly and $Q$ inertia $(8,8,0)$.
3. First K₄ collision: $t_*=0.928532626312458727195051893512\ldots$, at $\lambda=-5/3$.
4. At that collision: the two exact ranks are $6$ and $4$, proving two length-two Jordan chains.
5. Bounded theta counterexample: $\delta=41/5$ and $\kappa=0$, although $n=2$.
6. Reproduce the unbounded accepted counts $(43,6,28,22,50)$ out of 64, in the graph order of the table. Each has its own MP80 verification in the log.

## What this changes in the notebook

**Candidate rows only; no registration or record edits performed.**

| Candidate id | Kind | Proposed status | Statement / dependency |
|---|---|---|---|
| prop:su11-gauge-compact-unitary | proposition | PROVED | Bounded holonomy iff vertexwise unitarizable; spectral equivalence with matched endpoint conventions. |
| cex:su11-krein-ramanujan-rigidity | counterexample | PROVED; K1(b) REFUTED | Exact nonelementary theta and K₄ fields have real semisimple strict-band adjacency spectrum. |
| prop:su11-adjacency-pfaffian | proposition | PROVED | Characteristic polynomial is a real monic square; a simple reduced spectrum forces semisimplicity. |
| prop:su11-balanced-krein-count | proposition | PROVED; K2 SHARPENED | Every semisimple real eigenspace has balanced inertia; $\kappa$ is half the real in-band multiplicity. |
| prop:su11-unicyclic-theta-formulas | proposition | PROVED | Unicyclic determinant and parabolic Jordan compression formulas; complete theta classification. |
| cex:su11-krein-count-semicontinuity | counterexample | PROVED; proposed semicontinuity REFUTED | Closed-band theta crossing, plus an interior semisimple collision counterexample on the full field space. |
| prop:su11-weil-inertia | proposition | PROVED | $Q$ has inertia $(2n-d_0/2,2n-d_0/2,d_0)$, including defective fields; $d_0$ is total geometric band-edge multiplicity. |
| prop:su11-k4-interior-collision | proposition | PROVED | Exact family with first spectral failure at $\operatorname{arcosh}(79/54)$, interior collision at $-5/3$. |
| check:su11-five-graph-scan | computation | NUMERICAL | Seeded scan and MP80 verifications; evidence supplementary to the exact counterexamples. |

The SU(1,1) paragraph of gauge-groups.md should say: **“Unbounded, even nonelementary, holonomy can have a real semisimple Ramanujan adjacency spectrum. In the defining representation the characteristic polynomial is a square and each real semisimple eigenspace has equally many positive and negative directions. The canonical Weil form is therefore indefinite even when all modes lie strictly on the critical circle.”** Its “Next” can use the explicit K₄ family above as both the negative-sign demonstration and an interior collision demonstration.

“RH and positivity separate” **survives as a statement about this fixed canonical form**, with two qualifications: use a negative-type vector plane inside a mixed eigenspace, and use the strict band for definite positivity/semisimple critical-circle transfer. Existence of some invariant positive metric remains a different, spectral statement. Neither boundedness nor replacing the field by a unitary representative makes the inherited $Q$ positive.

The brief and any restatement of graph-ihara.md should align the companion-label convention; no sign correction is needed in the tutorial's own formula. The band-edge distinction in lattice-tower.md §5 should be retained explicitly, alongside its existing polarisation-orientation qualification. No edit to the registered invariant-polarisation theorem is proposed.

**Next step:** independent REFUTE review of the Pfaffian/anti-isometry argument, the exact K₄ annihilator and collision ranks, and the unicyclic parabolic Jordan compression formula; then decide which candidate rows to register. The rigidity question and the proposed global $\kappa$ semicontinuity are settled negatively. Classifying attainable reduced spectra and the geometry of their real-rooted chambers remains OPEN.
