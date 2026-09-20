Author: `codex:gpt-6-astra`

# 0. Hypotheses, diagrams, and conventions

All inner products are conjugate linear in the first variable. Multiplicities are algebraic unless explicitly called dimensions. The variable $z$ is the notebook's wave multiplier; the adjacency eigenvalue is $\lambda=z+z^{-1}$. “Resonance” below means a mode of the pole-removed model in the open disk, including zero. APW also count exterior bound-state parameters, cusp forms, and thresholds as resonances, and exclude zero. These are different counting conventions.

The hypotheses used are:

* **H-DIAG-2 / H-DIAG-3:** the stabiliser-labelled diagrams specified below are the indicated arithmetic quotients. Their arithmetic provenance is assumed; their degrees and determinants are checked here. Takahashi's theorem is not available locally. APW describe that provenance at `2603.26443:final_draft.tex:1983`.
* **H-LP:** the energy completion, translation representation, and repaired spaces $D_-=\mathcal O_-$, $D_+=\mathcal O_+\cap\mathcal O_-^\perp$ identify the geometric wave compression with the matrix Hardy model constructed in T3. This inherits exactly the unproved geometric step in `thm:cusp-wave-contraction`, `report/sections/04i_cusp_graph_scattering.tex:197`, and review T1c, `notes/reviews/cusp-graph-2026-09-20.md:51`. No assertion about that completion is proved here.
* **H-EIS:** a general Eisenstein constant-term normalisation supplies the proposed genus-dependent prefactor. The two computations here do not establish this hypothesis or a formula attributed to Li (1979).
* **H-CLASS:** after a specified arithmetic normalisation of incoming and outgoing cusp data, class characters give scalar factors of the proposed form $L(2s-1,\chi)/L(2s,\chi)$ in the modular $\phi$ orientation, and their reciprocals in our $S$ orientation, up to specified monomials. The actual theorem must fix character inversion/powers and any pairing of characters, as well as cancellations; the genus prediction in T6 assumes precisely the character divisors stated there. Neither that global Eisenstein theorem nor its conventions are supplied by the diagrams. T2(d) verifies a concrete diagonalisation, not this general theorem.
* **H-HECKE:** additional double-coset correspondences, their action on completed wave/exit spaces, adjoints, and joint spectral separation justify the proposed Hecke selection of rebounds. Commutation with adjacency alone is insufficient.
* **H-ARITH:** the $\Gamma_0(N)$ scattering/$L$-function identification, complete retained divisor, diamond grading, and prime comb stated in `obs:cusp-arith-next`, `report/sections/04j_cusp_graph_renewal.tex:161`. It remains open here.
* **H-CORE:** a finite real symmetric core, finitely many standard rays, and positive real junction couplings, as specified in C1. This is the generic scattering premise.
* **H-CONTRACTION:** a finite-dimensional contraction $Z$ with $Z^m\to0$ and $I-Z^*Z=J^*J$. T3(a) proves this premise for the inner model; T3(b) also applies to any system satisfying it.
* **H-RESET:** $\Phi(X)=\operatorname{Tr}(X)\Omega$, used only for the scalar holding law and the modal common-radius criterion. General exit-dependent rebounds need not satisfy it.
* **H-REG:** the graph in T5(a) is $(q+1)$-regular, with $q>1$, as well as having finite volume and bounded degree. Finite volume alone is insufficient.

The last four hypotheses name structural premises, not additional unverified arithmetic identifications. Standard matrix inner-function/model theory, finite-dimensional quantum channel facts, and the curve zeta theorem are used as standard (no local source where none is cited).

## The two diagrams

**D2:** $q=2$, vertex order $(A,B,C,D,E,F)$, stabilisers $(6,2,2,1,3,3)$, edges $AB:2$, $BC:2$, $CD:1$, $DE:1$, $DF:1$. The edge $B c_1$ has stabiliser $2$; $S(c_k)=2^{k+1}$ and $S(c_kc_{k+1})=2^{k+1}$. The curve is $y^2+y=x^3+x+1$ over $\mathbb F_2$.

**D3:** $q=3$, vertex order $(L1p,L1,L2,X,Xp,Y,Z,Zp,Q)$, stabilisers $(48,12,6,2,8,6,12,48,4)$, edges $L1pL1:12$, $L1L2:6$, $L2X:2$, $XXp:2$, $XY:2$, $XQ:2$, $YZ:6$, $ZZp:12$. Junctions at $L1,Z$ have stabiliser $12$, with ray stabilisers $12\cdot3^k$; two junctions at $Q$ have stabiliser $4$, with ray stabilisers $4\cdot3^k$. On each ray the forward edge has the stabiliser of its origin. The curve is $y^2=x^3+x+1$ over $\mathbb F_3$.

**Consistency check 1 — STATUS: PROVED.** The core degree sums $\sum_{e\ni v}S(v)/S(e)$, including junctions, are respectively

$$
\begin{array}{c|rrrrrr}
D2&A&B&C&D&E&F\\\hline
&3&1+1+1&1+2&1+1+1&3&3
\end{array}
$$

and

$$
\begin{array}{c|rrrrrrrrr}
D3&L1p&L1&L2&X&Xp&Y&Z&Zp&Q\\\hline
&4&1+2+1&1+3&1+1+1+1&4&3+1&2+1+1&4&2+1+1.
\end{array}
$$

Every ray vertex has backward index $q$ and forward index $1$, including $c_1$. Thus the degrees are $q+1$ everywhere. The volume is finite because all ray measures form geometric series.

## C1. Normalisation — STATUS: CORRECTED

For APW's coordinate adjacency $A_{vw}=S(v)/S(e)$, the unitary map from $\ell^2(V,1/S)$ to counting measure is $Uf(v)=f(v)/\sqrt{S(v)}$. Consequently

$$
(UAU^{-1})_{vw}=\frac{\sqrt{S(v)S(w)}}{S(e)},\qquad
T_X=q^{-1/2}D^{-1/2}A_XD^{1/2},\quad D=\operatorname{diag}S.
$$

The draft's $D^{-1/2}A_XD^{-1/2}$ is correct only if $A_X$ denotes the **measure kernel** $S(v)S(w)/S(e)$, not the coordinate adjacency. This distinction is explicit in `2603.26443:final_draft.tex:442` and `:452`.

On an interior ray edge the normalised entry is $\sqrt{S(c_k)qS(c_k)}/(\sqrt q S(c_k))=1$. At $c_1$, its forward index is $1$, so regularity gives $S(c_1)/S(e)=q$. Hence the junction satisfies

$$
c^2=\frac{S(v)S(c_1)}{qS(e)^2}=\frac{S(v)}{S(e)}.
$$

This is the individual contribution to APW's $c_v$. All junctions of D2 and D3 have $c=1$. Nagao has $c^2=q+1$, as proved in C1 of the previous round and recorded at `report/sections/04i_cusp_graph_scattering.tex:46`.

Put $W_{va}=c_a\delta_{v,v_a}$ and $C=WW^*=\sum_a c_a^2P_{v_a}$. Then

$$
T=T_X\oplus\bigoplus_{a=1}^h T_{\rm ray}^{(a)}
 +\sum_a c_a(|v_a\rangle\langle r_1^{(a)}|+|r_1^{(a)}\rangle\langle v_a|).
$$

Here $C_2=\operatorname{diag}(0,1,0,0,0,0)$ and $C_3=\operatorname{diag}(0,1,0,0,0,0,1,0,2)$. With $a=\sqrt{3/2}$, $b=1/\sqrt2$,

$$
T_2=\begin{pmatrix}
0&a&0&0&0&0\\a&0&b&0&0&0\\0&b&0&1&0&0\\
0&0&1&0&a&a\\0&0&0&a&0&0\\0&0&0&a&0&0
\end{pmatrix}.
$$

With $d=2/\sqrt3$, $e=\sqrt{2/3}$,

$$
T_3=\begin{pmatrix}
0&d&0&0&0&0&0&0&0\\
d&0&e&0&0&0&0&0&0\\
0&e&0&1&0&0&0&0&0\\
0&0&1&0&d&1&0&0&e\\
0&0&0&d&0&0&0&0&0\\
0&0&0&1&0&0&e&0&0\\
0&0&0&0&0&e&0&d&0\\
0&0&0&0&0&0&d&0&0\\
0&0&0&e&0&0&0&0&0
\end{pmatrix}.
$$

## C2. Matrix scattering and the APW determinant — STATUS: PROVED

Let $G=(\lambda-T_X)^{-1}$ and $\Gamma=W^*GW$. For incoming amplitude $u$ and outgoing amplitude $v$, the first ray equation and the core equation give

$$
W^*x=u+v,\qquad x=GW(z^{-1}u+zv).
$$

Solving proves, initially where the inverses exist and hence as a rational identity,

$$
S(z)=(z\Gamma-I)^{-1}(I-z^{-1}\Gamma)
      =-Q(z)^{-1}Q(1/z),\qquad Q(z)=I-z\Gamma.
\tag{0.1}
$$

This is precisely Childs--Gosset with their boundary block $A=0$, their $B=W$, and their $D=T_X$; the first ray vertices are their boundary vertices. See `1203.6557:levinson2.tex:365` and `:369`. All functions of $\Gamma$ in (0.1) commute. Since $\Gamma^T=\Gamma$, $\Gamma(1/z)=\Gamma(z)$, and the coefficients are real, it follows that

$$
S^T=S,\quad S(z)S(1/z)=I,\quad S(\bar z)=\overline{S(z)}.
$$

On the circle, $1/z=\bar z$, so these identities give $S^*S=I$. Rational continuation supplies removable values at exceptional core eigenvalues. In fact any apparent singularity on the unit circle, including a threshold, is removable: every entry is bounded by one along a punctured circle arc, which excludes a rational pole there.

Sylvester's determinant identity gives

$$
\det S=(-1)^h\frac{p(z)}{\widetilde p(z)},\quad
p=\det((1+z^2)I-zT_X-C),\quad
\widetilde p=\det((1+z^2)I-zT_X-z^2C)=z^{2n}p(1/z).
\tag{0.2}
$$

Indeed $\det_h(I-tW^*GW)=\det_n(I-tGC)$, and multiplying the two numerator/denominator core determinants by $z^n$ gives (0.2). The polynomial $p$ is monic of degree $2n$, and $\widetilde p(0)=1$.

APW's energy variable in $H(\mu)$ is $(\mu+\mu^{-1})/2$; their parameter $\mu$ is our $z$, not our $\lambda$. Conjugating their coordinate adjacency and multiplying their matrix by $-2\mu$ gives

$$
\det H(\mu)=(-1)^n(2\mu)^{-n}p(\mu).
\tag{0.3}
$$

See `2603.26443:final_draft.tex:1899`, `:1907`, `:1911`. Thus their nonzero zeros are the nonzero roots of the **unreduced** $p$, including cusp forms, thresholds, and exterior roots. A physical bound-state pole at $z=\beta$ is represented among those roots by $\mu=\beta^{-1}$; this does not change the parameter identification in (0.3).

## C3. Bound states, cancellations, zero, and thresholds — STATUS: CORRECTED

Define

$$
X_b=\operatorname{span}\{T_X^k\operatorname{ran}W:k\geq0\},\qquad X_c=X_b^\perp.
$$

The invariant space $X_c$ is exactly the sum of core eigenspaces annihilated by $W^*$. An eigenvector orthogonal to the span of the attachment vertices is already a cusp form; there is no additional class of such eigenvectors when $h>1$. An arbitrary vector orthogonal to the attachments need not remain so under $T_X$. Restricting to $X_c$ factors

$$
D_c(z)=\prod_t(1-tz+z^2)^{m_c(t)}
$$

out of both determinants. These eigenfunctions extend by zero on all rays.

On a physical decaying branch, a visible bound state satisfies

$$
(\lambda-T_X-\beta C)x=0,\quad
g_a(k)=c_ax(v_a)\beta^k,\quad 0<|\beta|<1.
\tag{0.4}
$$

Self-adjointness forces $\lambda$ real, hence $\beta$ real: $\operatorname{Im}(z+z^{-1})=(1-|z|^{-2})\operatorname{Im}z$. The matrix scattering poles are the visible bound states; their residues may have rank greater than one. Outside-band cusp forms remain invisible. An in-band $\ell^2$ solution has zero rays, hence is a cusp form. On $|z|=1$, $z\ne\pm1$, the imaginary part of $(\lambda-T_X-z^{-1}C)x=0$ forces $W^*x=0$, so all such roots come from $D_c$.

To justify the pole assertion without a determinant argument, Schur elimination of the decaying rays identifies $(\lambda-T_X-zC)^{-1}$ with the core compression of the physical resolvent and gives

$$
S=-I+(z^{-1}-z)W^*(\lambda-T_X-zC)^{-1}W.
$$

At a bound energy the resolvent has a simple spectral-projection pole. A visible bound vector has $W^*x\ne0$, so the sandwiched positive spectral projection is nonzero. Since $\lambda'(\beta)=1-\beta^{-2}\ne0$ and $\beta^{-1}-\beta\ne0$, this is a simple matrix pole, with rank the visible eigenspace dimension. Confined vectors give zero in this sandwich.

**A scalar gcd is insufficient for several exits.** Independent channels may have a zero and a pole at the same point. For example take $T_X=0_{2\times2}$, one exit at each vertex, and $C=\operatorname{diag}(5/4,5)$. Then

$$
S=\operatorname{diag}\left(-\frac{z^2-1/4}{1-z^2/4},
                          -\frac{z^2-4}{1-4z^2}\right),\qquad \det S=1.
$$

There are no cusp forms or thresholds, but $p=\widetilde p$ and the matrix still has resonance zeros and bound-state poles at $\pm1/2$ in different directions. Thus neither “all common factors are cusp forms or thresholds” nor “poles of $\det S$ enumerate all visible eigenvalues” generalises literally from one exit. Use the local matrix zero/pole orders (Smith--McMillan partial multiplicities), or the minimal inner model in T3. For D2 and D3 the displayed factorizations below establish that the only scalar common factors are the stated cusp and threshold factors.

For completeness the count, with bound and threshold **state multiplicities**, is

$$
N=2(n-m_c)-b-\tau,\qquad
w(\det S)=2(n-m_c)-2b-\tau=N-b.
\tag{0.5}
$$

Here $m_c=\dim X_c$, $b$ counts visible bound states, and $\tau$ counts nonconfined half-bound states at both thresholds. This is the matrix Levinson formula, `1203.6557:levinson2.tex:511`, with their $m=n$ internal core vertices. Equivalently factor out $D_c$: exterior numerator roots are reciprocal bound parameters, unit-circle roots are half-bound roots, and the remaining $2(n-m_c)-b-\tau$ roots are inside. At coincident disk zeros/poles, their exit directions are distinct: subtracting the two effective equations gives $x_{\rm bd}^*C x_{\rm res}=0$. Minimal matrix pole removal retains these zero directions. No extra deletion by a scalar gcd is justified.

At zero,

$$
p(0)=\det(I-C)=\prod_v(1-C_{vv}).
$$

Since $S$ is analytic at zero and $\widetilde p(0)=1$, a zero there is a genuine eigenvalue of the finite model, not a finite adjacency energy. Its generalized eigenspace is nilpotent and leaves in a bounded number of no-event steps. For $T_X=[0]$, $c=1$, $S=-z^2$ and the model is the two-dimensional truncated shift.

Here is a geometric multiplicity calculation. Write $U=\ker(I-C)$ and $V=U^\perp$, $A_V=(I-C)|_V$. If $T_{UU}=0$, Schur elimination gives

$$
p(z)=\det(A_V+O(z))\det\left[z^2\big(I_U-T_{UV}A_V^{-1}T_{VU}\big)+O(z^3)\right].
\tag{0.6}
$$

When the bracket is invertible, $\operatorname{ord}_0p=2\dim U$, not the defect rank or the number of rays. D2 has $U=\mathbb CB$, $\operatorname{rank}(I-C)=5$, and bracket $1-(3/2+1/2)=-1$: $p=-z^2+O(z^4)$. D3 has $U=\operatorname{span}(L1,Z)$, rank $7$, $\det A_V=-1$, and bracket $-I_2$: $p=-z^4+O(z^6)$. The double attachment at $Q$ contributes the invertible entry $-1$, not another vector in $U$. In general $T_{UU}\ne0$ can give order $\dim U$, and degeneracy of the bracket can give a larger order.

Both matrices are regular at thresholds. D2 has no half-bound state; D3 has two at each sign. In the symmetry basis of T2, at $z=\epsilon=\pm1$,

$$
S(\epsilon)=(-1)\oplus(1)\oplus
\begin{pmatrix}0&-\epsilon\\-\epsilon&0\end{pmatrix}.
\tag{0.7}
$$

There are two $+1$ and two $-1$ eigenvalues. Thus threshold multiplicity is compatible with a regular, nontrivial matrix limit. Equations (0.5) give $N_2=12-4-2=6$ and $N_3=18-4-2-4=8$; their windings are $4$ and $6$.

**Consistency check 2 — STATUS: PROVED.** For a weighted tree the determinant in (0.2) has the elementary matching expansion

$$
p(z)=\sum_{M\text{ matching}}(-z^2)^{|M|}
 \prod_{ij\in M}T_{ij}^2\prod_{v\text{ unmatched}}(1+z^2-C_{vv}).
\tag{0.8}
$$

This follows by expanding permutations: a forest permits only fixed points and disjoint edge transpositions. Substitution of the two matrices gives exactly T1(a) and T2(a). Thus if $F_2,F_3$ denote APW's displayed polynomials at `2603.26443:final_draft.tex:2008` and `:2056`, the actual determinants for these cores are

$$
\det H_2(z)=\frac{F_2(z)}{128z^4},\qquad
\det H_3(z)=-\frac{F_3(z)}{1536z^5}.
$$

The displayed polynomials specify the nonzero zero divisors, not those Laurent determinants with their constants and monomials.

# 1. T1. The one-cusp elliptic cavity

## T1(a). Exact determinant and reflection — STATUS: PROVED-CONDITIONAL (H-DIAG-2 for the arithmetic interpretation)

Applying (0.8), or eliminating leaves successively, gives

$$
p_2=\frac{z^2}{2}(z^2-2)(z^2+1)^2(2z^4-2z^2+1),
$$
$$
\widetilde p_2=-\frac12(z^2+1)^2(2z^2-1)(z^4-2z^2+2),
$$
$$
R_2(z)=\frac{z^2(z^2-2)(2z^4-2z^2+1)}{(2z^2-1)(z^4-2z^2+2)}.
\tag{1.1}
$$

For a compact independent elimination certificate, the nonzero edge squares in order are $(3/2,1/2,1,3/2,3/2)$, and the unmatched diagonal factors are $1+z^2$ except $B$, where it is $z^2$. Equation (0.8) with these five edges yields the first line; reversal yields the second, and $R=-p/\widetilde p$ yields the third.

## T1(b). Exact zeta identification — STATUS: PROVED-CONDITIONAL (H-DIAG-2)

There are no affine $\mathbb F_2$ points, so $N_1=1$, $a=q+1-N_1=2$ and $P(T)=1-2T+2T^2$. The standard genus-one zeta theorem gives

$$
\zeta_K(s)=\frac{P(2^{-s})}{(1-2^{-s})(1-2^{1-s})}.
$$

For $z=q^{s-1/2}$, set $t=z^{-2}$. Direct substitution, without a choice of logarithm, gives the useful general algebraic identity

$$
\frac{\zeta_K(2s-1)}{\zeta_K(2s)}
=\frac{P(t)}{P(t/q)}\frac{1-t/q}{1-qt}.
\tag{1.2}
$$

Using $q=2$ in (1.2) and simplifying proves exactly

$$
\boxed{\frac1{R_2(z)}=z^{-2}\frac{\zeta_K(2s-1)}{\zeta_K(2s)}}.
\tag{1.3}
$$

The equality is meromorphic, including its cancellations. Nagao instead has $1/R=q\,\zeta_{\mathbb F_q(T)}(2s-1)/\zeta_{\mathbb F_q(T)}(2s)$; see `prop:pure-cusp-scattering`, `report/sections/04i_cusp_graph_scattering.tex:100`. The pattern $q^{1-2gs}$ fits these two genus values. **OPEN (H-EIS):** these data do not prove that pattern for any other genus or cusp normalisation.

## T1(c). Spectrum, bipartiteness, and inverse Frobenius — STATUS: PROVED-CONDITIONAL (H-DIAG-2; H-LP only for the geometric compression)

The only visible bound poles are $\beta=\pm1/\sqrt2$, giving $\lambda=\pm3/\sqrt2$. They are $g(v)=1/\sqrt{S(v)}$ and its alternating twin. The core kernel is two-dimensional, with basis

$$
(1/\sqrt2,0,-\sqrt{3/2},0,1,0),\quad
(1/\sqrt2,0,-\sqrt{3/2},0,0,1).
$$

Both vanish at $B$. Thus there is one two-dimensional adjacency eigenspace at $\lambda=0$. Its two wave parameters are $\pm i$, each with multiplicity two; it is not four independent adjacency eigenfunctions. These account for $(z^2+1)^2$. There are no other $\ell^2$ eigenvalues, by C3 and (1.1).

The four nonzero disk resonances satisfy

$$
z^2=(1+i)/2\ \text{or}\ (1-i)/2=1/\alpha,
\qquad \alpha\in\{1-i,1+i\}.
$$

There are also two zero roots, forming one size-two Jordan block, proved explicitly in T4(a). There are no thresholds. Bipartite multiplication on the graph satisfies $\sigma T\sigma=-T$. In the scalar Hardy model below $\Theta$ is even, and $\sigma f(w)=-f(-w)$ satisfies $\sigma Z\sigma=-Z$ and interchanges the $z,-z$ modes.

Let $K_{\rm HW}$ be the invariant span of the four nonzero eigenvectors. Then

$$
\operatorname{spec}(Z^2|_{K_{\rm HW}})=\{(1-i)^{-1},(1+i)^{-1}\},
\quad\text{each twice}.
$$

Precisely: after complexifying a Frobenius representation with eigenvalues $1\pm i$, $Z^2|_{K_{\rm HW}}$ is **similar** to $F^{-1}\otimes I_2$. One can choose coordinates in which $Z$ is $\left(\begin{smallmatrix}0&F^{-1}\\I&0\end{smallmatrix}\right)$. This is a spectral similarity, not a canonical identification with étale cohomology, an isometry in the energy metric, or an arithmetically constructed square-root functor. Bipartite pairing is exactly the two square roots; it is not a further doubling.

## T1(d). The Weil circle — STATUS: PROVED-CONDITIONAL (H-DIAG-2)

All four Hasse--Weil resonances have

$$
|z|=2^{-1/4}=0.8408964152537145,
\quad \arg z\in\{\pi/8,-\pi/8,7\pi/8,-7\pi/8\}.
$$

This is the genus-one Weil/Hasse modulus $|\alpha|=\sqrt2$, also directly apparent from $\alpha=1\pm i$. It proves the notebook's equal-radius RH on $K_{\rm HW}$. It does **not** prove RH on the entire six-dimensional model: the two delay roots have modulus zero. Compare `def:cusp-diagram`, `report/sections/04i_cusp_graph_scattering.tex:25`, and APW's circle statement, `2603.26443:final_draft.tex:2030`.

## T1(e). The product objection — STATUS: CORRECTED

Review finding 7, `notes/reviews/cusp-graph-2026-09-20.md:105`, applies to one exit with $c^2=q+1$. D2 has $c^2=1$. Its constant product $p(0)=1-c^2=0$ gives no restriction on the nonzero resonances. The report already includes the necessary smaller-junction alternative in `prop:cusp-radius-product`, `report/sections/04j_cusp_graph_renewal.tex:110`.

There is a useful replacement. If a monic degree-$2n$ polynomial has $p(z)=a_mz^m+O(z^{m+1})$, $a_m\ne0$, then

$$
\prod_{z_i\ne0}z_i=(-1)^m a_m.
\tag{1.4}
$$

For one $c=1$ junction, write $T_X=\left(\begin{smallmatrix}a&b^*\\b&D_0\end{smallmatrix}\right)$ with the junction first. Schur elimination proves the exact coefficient formula

$$
p(z)=\det M_0(z)\left[z^2-az-z^2b^*M_0(z)^{-1}b\right],
\quad M_0=(1+z^2)I-zD_0.
\tag{1.5}
$$

If $a\ne0$, $m=1$ and the nonzero product is $a$. If $a=0$ and $\|b\|^2\ne1$, $m=2$ and the product is $1-\|b\|^2$. Degeneracy requires the next nonzero coefficient of (1.5). In D2, $\|b\|^2=2$, so the product is exactly $-1$: exterior pair $-2$, cusp-form factors $1$, Hasse--Weil quartet $1/2$. The nonzero disk product is therefore $1/2$, fully consistent with no additional bound state.

The corrected demand on an arithmetic diagram is to compute its actual stabiliser junctions and its zero multiplicity first, then remove cusp, threshold, and exterior factors from the first nonzero coefficient identity. A Nagao junction cannot be imposed on an arbitrary arithmetic core.

# 2. T2. The four-cusp elliptic cavity

## T2(a). Determinants — STATUS: PROVED-CONDITIONAL (H-DIAG-3 for the arithmetic interpretation)

Equation (0.8) gives

$$
p_3=\frac{z^4}{3}(z-1)^2(z+1)^2(z^2-3)(z^2+1)^2(3z^4+1),
$$
$$
\widetilde p_3=-\frac13(z-1)^2(z+1)^2(z^2+1)^2(3z^2-1)(z^4+3),
\qquad \det S=p_3/\widetilde p_3.
\tag{2.1}
$$

The symmetry factorisation in the next paragraph provides a second finite certificate.

## T2(b). All matrix entries in symmetry coordinates — STATUS: PROVED

Order exits $(L1,Z,Q_1,Q_2)$ and introduce the orthonormal vectors

$$
q_-=(Q_1-Q_2)/\sqrt2,\quad l_-=(L1-Z)/\sqrt2,
\quad l_+=(L1+Z)/\sqrt2,\quad q_+=(Q_1+Q_2)/\sqrt2.
$$

The two graph involutions commute with scattering, so in this constant basis

$$
S=(-1)\oplus z^2\oplus S_e(z).
\tag{2.2}
$$

For $q_-$, $Wq_-=0$, hence $\Gamma q_-=0$ and (0.1) gives $-1$: a Dirichlet end. For $l_-$ the core is the three-vertex path with edge weights $2/\sqrt3,\sqrt{2/3}$ and unit exit at its middle vertex. Its two leaf squares sum to $2$. A leaf rotation gives a dark zero vertex and a two-vertex core with coupling $\sqrt2$. Equivalently,

$$
p_o=z^2(z^2+1)(z^2-1),\qquad
\widetilde p_o=(z^2+1)(1-z^2),\qquad -p_o/\widetilde p_o=z^2.
\tag{2.3}
$$

This proves the exact transparency/delay claim, including its sign.

In the even core basis $((L1p+Zp)/\sqrt2,(L1+Z)/\sqrt2,(L2+Y)/\sqrt2,X,Xp,Q)$ the edges have weights $2/\sqrt3,\sqrt{2/3},\sqrt2,2/\sqrt3,\sqrt{2/3}$, with the last two joining $X$ to $Xp,Q$. The exit matrix has entries $W_{2,1}=1$, $W_{6,2}=\sqrt2$ (indices starting at one). Elimination in (0.1) gives, with

$$
\Delta=(3z^2-1)(z^4+3),\qquad F=(z^2-1)(3z^4-2z^2+3),
$$

$$
\boxed{S_e(z)=\frac1\Delta
\begin{pmatrix}z^2F&-4z^3(z^2+1)\\-4z^3(z^2+1)&F\end{pmatrix}}.
\tag{2.4}
$$

For direct verification of the elimination, its $2\times2$ resolvent matrix is

$$
\Gamma_{11}=\frac{3z(z^6-z^4-z^2+1)}{A},\quad
\Gamma_{12}=\frac{4z^4}{A},\quad
\Gamma_{22}=\frac{6z^9-8z^7+4z^5-8z^3+6z}{(1+z^2)A},
\quad A=3z^8-6z^6+2z^4-6z^2+3.
$$

Multiplying verifies $(z\Gamma-I)S_e=I-z^{-1}\Gamma$. The even core determinant is

$$
p_e=\frac{z^2}{3}(z^2-1)(z^2-3)(z^2+1)(3z^4+1),
$$

so $p_3=p_op_e$, proving (2.1) independently. Finally

$$
R_3(z):=\det S_e(z)=
\frac{z^2(z^2-3)(3z^4+1)}{(3z^2-1)(z^4+3)}
=z^2\frac{\zeta_K(2s)}{\zeta_K(2s-1)}.
\tag{2.5}
$$

The last equality follows from (1.2) with $q=3$, $P(T)=1+3T^2$. Enumeration gives affine points $(0,1),(0,2),(1,0)$, hence $N_1=4$, $a=0$. Doubling $(0,1)$ has slope $2$ and gives $(1,0)$, so it has order four. The usual identification $\operatorname{Pic}(E\setminus\{\infty\})=E(\mathbb F_3)$ gives $\mathbb Z/4$; the corresponding D2 group is trivial.

## T2(c). Spectral bookkeeping — STATUS: PROVED-CONDITIONAL (H-DIAG-3; H-LP for the geometric model)

The only nonzero disk resonance roots are those of $3z^4+1$: $|z|=3^{-1/4}$, angles $\pi/4,3\pi/4,5\pi/4,7\pi/4$. They all occur in (2.4). There are two zero modes there and two in $z^2$; the constant $-1$ contributes none. Near zero, $S_e$ has one invertible direction and one zero of order two: its lower-right entry is $1+O(z^2)$ and its determinant is $z^2+O(z^4)$. Pole-removal factors are invertible at zero, so the even model has one size-two zero Jordan block. The odd model also has one size-two block. There are eight modes in all.

At $\pm1$, (2.3) and $p_e$ each supply one half-bound state. There is no threshold cusp form, and (2.4) proves (0.7). APW's two topological resonances at each sign are therefore genuine half-bound states with removable scattering singularities; see `2603.26443:final_draft.tex:2058`.

The only visible bound parameters are $\pm1/\sqrt3$, with $\lambda=\pm4/\sqrt3$. The core kernel has dimension **three**, but only two vectors vanish at all exits. Indeed the leaf equations force $L1=Z=X=0$; the remaining equations read

$$
L2=-\sqrt2\,L1p,\quad Y=-\sqrt2\,Zp,\quad
-\sqrt2(L1p+Zp)+(2/\sqrt3)Xp+\sqrt{2/3}Q=0.
$$

Imposing $Q=0$ leaves dimension two, one reflection-even and one reflection-odd. These are exactly the cusp forms at $\lambda=0$, hence multiplicity two at each wave parameter $\pm i$. The third core zero eigenvector is not an eigenfunction after zero extension onto the rays. There is no further $\ell^2$ spectrum.

## T2(d). The height change works — STATUS: CORRECTED

The unrenormalised even block has no constant eigenbasis: writing its entries as $(a,b;b,d)$, the ratio $(a-d)/b$ equals

$$
-\frac{(z^2-1)^2(3z^4-2z^2+3)}{4z^3(z^2+1)},
$$

which is nonconstant. Its eigenvalues are not rational functions: the numerator of the discriminant, after the square denominator $\Delta^2$ is removed, is

$$
9z^{16}-48z^{14}+124z^{12}-144z^{10}+374z^8-144z^6+124z^4-48z^2+9;
$$

its gcd with its derivative is $1$, so it is not a rational square.

Nevertheless the proposed diagonal **congruence**, not similarity, does exactly what is wanted. Take

$$
D(z)=\operatorname{diag}(1,z),\qquad
H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$

Then direct multiplication of (2.4) gives

$$
\boxed{H^*D S_e D H=\operatorname{diag}(R_3(z),z^2)}.
\tag{2.6}
$$

For a general $\operatorname{diag}(z^a,z^b)$, a constant eigenbasis requires $a-b=-1$: otherwise the corresponding diagonal-difference/off-diagonal ratio has a pole at zero. Thus (2.6) is unique among these choices up to a common monomial. Taking $\operatorname{diag}(z^{-1},1)$ instead gives $\operatorname{diag}(R_3/z^2,1)$.

To perform the height shift on the actual four exits, multiply both $Q$ coordinates by $z$. Besides (2.6), this changes $q_-$ from $-1$ to $-z^2$ and leaves $l_-$ equal to $z^2$. There is one zeta factor and three monomial factors. This is consistent with the genus-one character prediction, although it does not identify these vectors with specific $\mathbb Z/4$ characters. The graph automorphisms are the stated Klein group with two cusp orbits; they are not a transitive class-group action.

The congruence changes delay counts: $\det(D S_e D)=z^2\det S_e$, adding two zero modes to that model. The full four-exit height shift adds four. T3 and T4 use the original ray origins, where $N_3=8$, throughout. Nonzero resonance positions are unaffected. **OPEN (H-CLASS):** the arithmetic interpretation and general character normalisation still need a global Eisenstein theorem.

# 3. T3. The model contraction and quantum renewal

## T3(a). Pole removal, defect, and Gram identity — STATUS: CORRECTED

The following model construction is proved under H-CORE; its identification with the geometric compression is conditional on H-LP.

Remove matrix poles on the **right**, retaining their directions. Here is a precise construction. If a simple pole at $\beta$ has residue $R_\beta$, choose the orthogonal projection $P$ onto $\operatorname{ran}R_\beta^*$ and multiply on the right by

$$
B_{\beta,P}(z)=I-P+b_\beta(z)P,\qquad
b_\beta(z)=\frac{z-\beta}{1-\bar\beta z}.
$$

Then $R_\beta(I-P)=0$ cancels that pole. Recompute residues after each multiplication and repeat, including partial orders if needed. This defines an **ordered**, minimal product $B_{\rm bd}$; its degree is the number $b$ of visible bound states. It is not in general a commuting product of scalar factors. Standard Blaschke--Potapov factorisation proves that

$$
\Theta(z)=\eta S(z)B_{\rm bd}(z)
$$

is rational inner. Take $\eta=I_h$ unless an explicitly stated constant unitary is used; such a left factor only gives a constant unitary equivalence of model spaces. No additional inner factors are inserted. For D2 we take $\eta=-1$ to obtain

$$
\Theta_2(z)=\frac{z^2(2z^4-2z^2+1)}{z^4-2z^2+2},\qquad
B_{\rm bd}=b_{1/\sqrt2}b_{-1/\sqrt2}.
\tag{3.1}
$$

For symmetry statements one may equivalently construct the analytic range $S H^2\cap H^2$ and choose its inner generator respecting the symmetry, rather than choosing incompatible intermediate pole bases.

Fix the **forward compressed shift** convention

$$
K=H^2(\mathbb C^h)\ominus\Theta H^2(\mathbb C^h),\qquad Z=P_KM_w|_K.
\tag{3.2}
$$

Standard finite inner model theory gives $\dim K=\deg\det\Theta=N$, spectrum equal to the disk matrix zeros retained after pole removal, and $Z^m\to0$. Eigenvalues and Jordan multiplicities, including zero, are those of this minimal model. This fixes the potential adjoint/conjugation ambiguity in the brief.

There is also a direct defect proof. For $f\in K$, $wf$ is perpendicular to $w\Theta H^2$, so its component outside $K$ lies in the wandering space $\Theta\mathbb C^h$. Define $Jf\in\mathbb C^h$ by

$$
(I-P_K)(wf)=\Theta Jf.
$$

Then

$$
I-Z^*Z=J^*J,\qquad \operatorname{rank}J\le h.
\tag{3.3}
$$

Telescoping gives $\sum_{m\ge0}Z^{*m}J^*JZ^m=I$. Thus no nonzero vector is decoupled from every cusp at every time; an individual vector can have zero instantaneous flux. For eigenvectors $Zk_n=z_nk_n$, $a_n=Jk_n$,

$$
(1-\bar z_nz_m)\langle k_n,k_m\rangle=a_n^*a_m.
\tag{3.4}
$$

In particular $a_n\ne0$. Formula (3.4) does not require distinct eigenvalues; generalized vectors satisfy its Jordan versions. In the scalar case one convenient eigenvector is $k_a(w)=\Theta(w)/(w-a)$, for which $Jk_a=1$ and $\|k_a\|^2=(1-|a|^2)^{-1}$.

## T3(b). CPTP renewal and its precise stationary criterion — STATUS: CORRECTED

Let $\Phi:\mathcal B(\mathbb C^h)\to\mathcal B(K)$ be CPTP, $\Phi(X)=\sum_\ell V_\ell XV_\ell^*$ with $\sum V_\ell^*V_\ell=I_h$. Define

$$
\mathcal E(\rho)=Z\rho Z^*+\Phi(J\rho J^*).
\tag{3.5}
$$

Its Kraus operators are $Z$ and $V_\ell J$, whose adjoint products sum to $I$. This proves CPTP, with no limiting Lindblad argument.

Write $\mathcal E_0(X)=ZXZ^*$ and $\Psi(X)=JXJ^*$. The holding instrument is the sequence of completely positive **superoperators**

$$
\mathcal M_m=\Psi\mathcal E_0^{m-1}\Phi\quad(m\ge1),\qquad
\mathcal R=\sum_{m\ge1}\mathcal M_m.
\tag{3.6}
$$

Thus it is an $h^2\times h^2$ transfer operator on exit matrices, not in general a single $h\times h$ transition matrix. For an exit density $\tau$, the next-time probability is $\operatorname{Tr}\mathcal M_m(\tau)$; the unnormalised output matrix records its exit state. Telescoping (3.3) proves total probability one, so $\mathcal R$ is CPTP. The mean is

$$
\mu(\tau)=\sum_{k\ge0}\operatorname{Tr}\mathcal E_0^k\Phi(\tau)<\infty.
$$

Finiteness follows from the exponential times polynomial bound on powers of a finite stable matrix, uniformly in $\tau$.

Put $\mathcal U=(I-\mathcal E_0)^{-1}\Phi$. A stationary exit density $\mathcal R\tau=\tau$ exists by compactness of the density matrices. Then

$$
\rho_\infty=\frac{\mathcal U\tau}{\operatorname{Tr}\mathcal U\tau}
=\frac1{\mu(\tau)}\sum_{k\ge0}Z^k\Phi(\tau)Z^{*k}
\tag{3.7}
$$

is stationary, since $\Psi\mathcal U\tau=\tau$ and $(I-\mathcal E_0)\mathcal U\tau=\Phi(\tau)$. Conversely any stationary density has nonzero exit flux (otherwise stability would force it to vanish), and $\tau=\Psi\rho/\operatorname{Tr}\Psi\rho$ reverses (3.7). This is a bijection between stationary densities.

Consequently uniqueness is equivalent to uniqueness of the stationary density of $\mathcal R$, **not** to irreducibility. Irreducibility is sufficient and gives a faithful stationary density; unique absorbing states give reducible counterexamples, including T4(a). With uniqueness, attraction of every density is equivalent to absence of other peripheral eigenvalues. In the irreducible case this is the usual aperiodicity criterion. A concrete transfer version follows from Sylvester's identity on operator spaces:

$$
\det(I-u\mathcal E)=\det(I-u\mathcal E_0)
\det(I-\widehat{\mathcal M}(u)),\quad
\widehat{\mathcal M}(u)=\sum_{m\ge1}u^m\mathcal M_m.
\tag{3.8}
$$

The first determinant never vanishes for $|u|=1$. Thus uniqueness and attraction amount to a simple zero at $u=1$ and no other circle zeros of the second determinant. Peripheral Jordan blocks are excluded by power boundedness of a channel. A scalar gcd of holding times does not replace (3.8) for a general quantum exit instrument.

The common-modulus renewal theorem requires a **fixed reset** $\Phi(X)=\operatorname{Tr}(X)\Omega$. In that case the previous scalar proof applies for any exit rank, giving a unique stationary density and

$$
\Omega=\sum_i p_i|e_i\rangle\langle e_i|,quad Ze_i=z_ie_i,quad\|e_i\|=1:
$$
$$
\mu=\sum_i\frac{p_i}{1-|z_i|^2},\qquad
\rho_\infty=\frac1\mu\sum_i\frac{p_i}{1-|z_i|^2}|e_i\rangle\langle e_i|.
\tag{3.9}
$$

Distinct eigenvectors are independent; their rank-one projectors are independent, by applying a dual eigenbasis on both sides. Thus every such mixture on a family is stationary iff all moduli coincide. At radius $r$ the holding law is $(1-r^2)r^{2(m-1)}$ and its mean is $(1-r^2)^{-1}$. This is `prop:cusp-modal-rh`, `report/sections/04j_cusp_graph_renewal.tex:48`. Positive weights on both a zero eigenvector and Hasse--Weil modes cannot give $\rho_\infty=\Omega$. Mixtures restricted to zero eigenvectors can be stationary; “arithmetic rebound” is a choice of the Hasse--Weil family, not a selection theorem.

For a general cusp-dependent $\Phi$, (3.9) is false. Even with equal moduli, stationarity of a proposed modal $\Omega$ requires $\Phi(J\Omega J^*)=(1-r^2)\Omega$. Conversely take $Z=\operatorname{diag}(r_1,r_2)$, $J=\operatorname{diag}(\sqrt{1-r_1^2},\sqrt{1-r_2^2})$ and $\Phi$ the identity between the two two-dimensional spaces. Every diagonal density is stationary, even when $r_1\ne r_2$.

The generic flag and protected-mode statements survive as well. A density $\rho$ can be stationary for some rebound iff $Q=\rho-Z\rho Z^*\ge0$: necessity follows from (3.5), and sufficiency follows by taking the fixed reset $\Omega=Q/\operatorname{Tr}Q$, since $\operatorname{Tr}Q=\operatorname{Tr}(J\rho J^*)>0$. If $V_j$ is a nested $Z$-invariant flag with orthogonal projections $P_j$, then $P_j-ZP_jZ^*\ge0$, because $Z|_{V_j}$ is a contraction. Thus for any decreasing probability list $p_j$, the density $\rho=\sum_j(p_j-p_{j+1})P_j$ has that spectrum and is attainable by a reset. This is the arbitrary-defect version of `thm:cusp-admissible-flags`, `report/sections/04j_cusp_graph_renewal.tex:61`.

Finally, on $\mathbb C\,\mathrm{vac}\oplus K$ prescribe $\widetilde Z=1\oplus Z$ and $\widetilde J=0\oplus J$, allowing the rebound to output anywhere in this enlarged space. On an odd coherence the exit matrix is zero, so

$$
\widetilde{\mathcal E}(|k_n\rangle\langle\mathrm{vac}|)
=z_n|k_n\rangle\langle\mathrm{vac}|,
\qquad
\widetilde{\mathcal E}(|\mathrm{vac}\rangle\langle k_n|)
=\bar z_n|\mathrm{vac}\rangle\langle k_n|.
$$

This protection is independent of $\Phi$; Jordan chains obey the corresponding statement. It is `prop:cusp-odd-protected`, `report/sections/04j_cusp_graph_renewal.tex:73`. This vacuum grading is distinct from the reflection-even/odd graph symmetry in T3(c).

## T3(c). Symmetry and what the extra exits add — STATUS: CORRECTED

A finite automorphism group acts unitarily on core, rays, and exits. With a compatible inner generator, $Z$ commutes with the model representation and $J$ intertwines it with the exit representation. Hence the **no-event model** is an orthogonal sum of isotypic components. In D3,

$$
K=K_e\oplus K_o,\quad \dim K_e=6,\quad\dim K_o=2.
$$

The even block has four Hasse--Weil modes and a length-two delay chain; the reflection-odd block is $K_{z^2}$, a length-two delay chain. There is no model space for $q_-$, whose scattering is constant. Within $K_e$, its Hasse--Weil and delay spectral subspaces are generally a nonorthogonal direct sum. The same caution applies to D2.

Covariance of a **channel** does not imply that it preserves these Hilbert-space blocks. It preserves isotypic components of the conjugation representation on operator space. In particular densities in two inequivalent one-dimensional symmetry types both transform trivially, so a covariant channel may transfer populations between them. For example resetting every exit to an invariant mixture of an even density and an odd density is covariant and mixes those populations. Block-preserving rebound Kraus maps require an extra restriction, such as each Kraus map itself intertwining the two representations. The stronger claim in the brief is therefore false.

For these genus-one examples the extra character channels add delay/constant factors and additional rebound choices, but no additional nonzero Hasse--Weil roots. They need not be dynamically irrelevant: they can carry populations and change the renewal channel.

# 4. T4. Does arithmetic select a rebound?

## T4(a). The canonical defect rebound is an absorbing zero mode — STATUS: CORRECTED

Use (3.1)--(3.2). Since $\Theta_2(0)=0$,

$$
j=J^*1=\Theta_2(w)/w,\quad\|j\|=1,\quad Zj=P_K\Theta_2=0.
\tag{4.1}
$$

Moreover $g=\Theta_2(w)/w^2$ belongs to $K$, is orthogonal to $j$, has norm one, and $Zg=j$. This proves the size-two zero block. The Hasse--Weil and delay generalized eigenspaces are complementary invariant spaces, not orthogonal sectors. In particular $\langle j,k_a\rangle=1$ for the scalar modes of T3(a).

The canonical choice in the question is therefore

$$
\Omega_J=J^*J/\operatorname{Tr}(J^*J)=|j\rangle\langle j|,
\quad \rho_\infty=\Omega_J,
\quad \operatorname{spec}\rho_\infty=(1,0,0,0,0,0).
\tag{4.2}
$$

It is the unique stationary state, because $Z$ is stable and this is a fixed reset. Its law and generating function are exactly

$$
m(m)=\frac{|\langle j,Z^{m-1}j\rangle|^2}{\|j\|^2}
=\delta_{m1},\qquad \widehat m(u)=u,\qquad\mu=1.
\tag{4.3}
$$

The law is aperiodic. The state is a **modal rebound at zero**, not a nonmodal Hasse--Weil rebound. It is not supported on $K_{\rm HW}$; its Hasse--Weil Riesz projection is zero, although its Hilbert-space overlaps with Hasse--Weil eigenvectors are nonzero. Convergence follows also directly: all trajectories are eventually reset with probability tending to one, and once reset they remain in $|j\rangle\langle j|$.

In particular the sentence in `thm:cusp-renewal-discrete`, `report/sections/04j_cusp_graph_renewal.tex:38`, making aperiodicity equivalent to $c\ne1$ when the rebound range contains an eigenvector, is incorrect. Every normalised eigenvector has immediate exit probability $1-|z_i|^2>0$, including $z_i=0$, so a modal mixture is aperiodic even when $c=1$. The earlier proof file already states this correctly in T3(c), `notes/cusp-graph/astra-proofs.md:449`.

For an entirely finite exact realization, in an orthonormal basis the model is

$$
Z=\begin{pmatrix}
0&2/3&0&-\sqrt5/6&0&0\\
1&0&0&0&0&0\\
0&\sqrt5/3&0&1/3&0&0\\
0&0&1&0&0&0\\
0&0&0&\sqrt3/2&0&0\\
0&0&0&0&1&0
\end{pmatrix},\qquad j=e_6.
\tag{4.4}
$$

Direct multiplication gives $I-Z^*Z=e_6e_6^*$ and characteristic polynomial $z^2(z^4-z^2+1/2)$. To obtain (4.4) from Hardy space, use the polynomial basis $w^k/(w^4-2w^2+2)$, $0\le k<6$. Its Gram matrix has entries $3/5$ on the diagonal, $2/5$ at distance two, $1/10$ at distance four, and zero at odd distance. Multiplication reduces $w^6$ to $w^4-w^2/2$ modulo the numerator of $\Theta_2$. Cholesky orthonormalisation gives (4.4). These Gram entries also follow by expanding the denominator's reciprocal in a geometric series and summing its two-step recurrence.

The characteristic transfer function in the question uses **opposite defect spaces**. Here $I-ZZ^*=kk^*$ with

$$
k=(\sqrt{15}/6,0,-1/\sqrt3,0,1/2,0)^T.
$$

The Sz.-Nagy--Foias formula, or direct inversion of (4.4), gives

$$
\langle k,[-Z+uD_{Z^*}(I-uZ^*)^{-1}D_Z]j\rangle
=u\langle k,(I-uZ^*)^{-1}j\rangle
=\Theta_2(u).
\tag{4.5}
$$

In contrast the amplitude for reinserting the **same** defect vector is $\langle j,(I-uZ)^{-1}j\rangle=1$, by (4.1). Squaring its time coefficients yields (4.3). Squaring the Taylor coefficients of $\Theta_2$ would describe a different preparation/readout. Thus (4.3), obtained from the factor $u^2\mid\Theta_2$, is the requested closed generating function; the characteristic formula does not impose a nontrivial holding law on $\Omega_J$.

## T4(b). Modal Hasse--Weil rebounds and the full Gram matrix — STATUS: PROVED

For any probability weights on the four normalised Hasse--Weil eigenvectors, (3.9) gives

$$
\rho_\infty=\Omega,\quad m(m)=\delta\,2^{-(m-1)/2},\quad
\mu=\delta^{-1}=2+\sqrt2,\quad\delta=1-1/\sqrt2.
$$

The general genus-one value is $(1-q^{-1/2})^{-1}$. The modular-surface value $2$ uses continuous time, as already distinguished in `prop:cusp-modal-rh`, `report/sections/04j_cusp_graph_renewal.tex:55`; see also `prop:mode-diagonal-rebound-rh`, `report/sections/04h_rebound_state.tex:160`.

Choose $a=\sqrt{(1+i)/2}$ with positive real and imaginary parts, and order the roots $(a,-a,\bar a,-\bar a)$. Take

$$
k_i(w)=\frac{\Theta_2(w)}{w-z_i},\quad Jk_i=1,\quad
e_i=\sqrt\delta\,k_i,\quad Je_i=\sqrt\delta.
$$

Thus the unnormalised Lax--Phillips/model Gram matrix is $G_{ij}=(1-\bar z_i z_j)^{-1}$, and the normalised one is

$$
O=\begin{pmatrix}
1&d&u&v\\d&1&v&u\\\bar u&\bar v&1&d\\\bar v&\bar u&d&1
\end{pmatrix},\quad
d=3-2\sqrt2,\quad u=\delta(1-i),\quad v=\delta(3+i)/5.
\tag{4.6}
$$

These are closed expressions in the inverse Frobenius roots $a^2=(1-i)^{-1}$ and $\bar a^2=(1+i)^{-1}$, with exit amplitudes determined above by $\Theta_2$. The parity matrix on the four modes is

$$
\Sigma=\begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix},
\quad \Sigma^*O\Sigma=O,\quad
\Sigma\operatorname{diag}(z_i)\Sigma=-\operatorname{diag}(z_i).
\tag{4.7}
$$

The density spectrum is $\operatorname{spec}(\operatorname{diag}(\sqrt p)O\operatorname{diag}(\sqrt p))$, not the list $p_i$; append two zeros for the full $K$. This is the Gram-spectrum correction of `report/sections/04h_rebound_state.tex:171`. For equal weights the four eigenvalues are approximately $0.11448581,0.16190739,0.29972775,0.42387905$, already far from four equal eigenvalues.

## T4(c). Metrics in which inverse Frobenius is unitary — STATUS: CORRECTED

On $K_{\rm HW}$, write a new inner product in the eigenbasis by a positive matrix $H$. Since the eigenvalues are distinct and have common modulus $r=2^{-1/4}$,

$$
Z^*HZ=r^2H
\quad\Longleftrightarrow\quad
(\bar z_i z_j-r^2)H_{ij}=0
\quad\Longleftrightarrow\quad H=\operatorname{diag}(h_1,h_2,h_3,h_4),\ h_i>0.
\tag{4.8}
$$

Here the middle $Z$ is its diagonal coordinate matrix and $*$ is conjugate transpose in those coordinates. Thus the cone has real dimension four, or three modulo common scale. Parity invariance requires $h_1=h_2$, $h_3=h_4$ (two-dimensional cone). Invariance under the real structure, which swaps $1\leftrightarrow3$ and $2\leftrightarrow4$, requires $h_1=h_3$, $h_2=h_4$. Imposing both leaves one ray: all four weights equal. These normalisations refer to the fixed, equally normalised vectors $e_i$ of (4.6).

The energy metric is outside this cone. The absolute overlaps, hence cosines of the projective angles between its modes, are

$$
|\langle e_a,e_{-a}\rangle|=3-2\sqrt2,
\quad |\langle e_a,e_{\bar a}\rangle|=\sqrt2-1,
\quad |\langle e_a,e_{-\bar a}\rangle|=(\sqrt2-1)/\sqrt5.
$$

The corresponding angles are approximately $80.120718^\circ,65.530199^\circ,79.324762^\circ$. In particular $q^{1/4}Z$ is not unitary for the Lax--Phillips energy metric. It is unitary for (4.8), and there is a unique parity-and-reality invariant ray of such metrics. This is the exact finite-dimensional common-radius/unitarisability statement; no equivalence to an independent global Ramanujan theorem follows.

The channel (3.5) uses the original metric and its adjoints. Its modal stationary state's spectrum is therefore (4.6), not the weights. If one changes metric, renormalises eigenvectors, rebuilds their bras and the exit defect, and defines the corresponding modal reset, then those new orthogonal projectors have eigenvalue weights. One cannot merely “read” the same density matrix in a new metric and assume its positivity, adjoints, or channel remain unchanged.

There is an additional concrete obstruction to identifying the two channels. In an arithmetic metric from (4.8), $I-Z^{*'}Z=(1-r^2)I$ on $K_{\rm HW}$ has rank four. It cannot factor through a one-dimensional cusp exit. The original energy metric gives rank one even after restriction to this invariant subspace. Therefore an arithmetic-metric renewal construction needs at least four exit coordinates on $K_{\rm HW}$ and is a different conservative completion of the same eigenvalue data.

## T4(d). Hecke and Bost--Connes — STATUS: OPEN (H-HECKE)

Stabiliser sizes specify adjacency, not the vertex/edge groups, embeddings, arithmetic representatives, or double cosets defining Hecke correspondences. Those data, together with their action on cusp asymptotics and the completed model, are needed to formulate a Hecke-invariant rebound. Commuting with adjacency and preserving cusp asymptotics does not by itself prove modal selection: joint eigenspaces may coincide, $Z^2$ already has doubled eigenvalues, and covariance of a CP map need not force its outputs to be diagonal. A sufficient selection theorem would require a specified Hecke action compatible with adjoints, simple separated joint characters, and an invariance/dephasing condition that actually removes off-diagonal terms. That theorem is H-HECKE; no canonical rebound or Bost--Connes dynamics is supplied by H-DIAG.

# 5. T5. Bound constants, the vacuum, and funnels

## T5(a). What finite volume proves — STATUS: CORRECTED

On a finite-volume stabiliser graph, $\mathbf1\in\ell^2(V,1/S)$, because its squared norm is $\sum_v1/S(v)$. Bounded degree makes adjacency bounded and self-adjoint, as in `2603.26443:final_draft.tex:445`. But $A\mathbf1=\deg(v)$: **regularity is necessary** to conclude that the constant is an eigenfunction. For a $(q+1)$-regular diagram it is an eigenfunction of eigenvalue $q+1$, and after normalisation its eigenvalue is $(q+1)/\sqrt q>2$ (for $q>1$). On each cusp it has nonzero tail $g(c_k)\propto q^{-k/2}$.

This is a bound state with no escaping scattering flux, not a cusp form invisible in the scattering matrix: it supplies the visible poles $z=\pm q^{-1/2}$ when the graph is bipartite. More importantly it is **not stationary under the notebook's discrete wave group**. For

$$
W(u,v)=(Tu-v,u),\qquad W(f,t^{-1}f)=t(f,t^{-1}f),
$$

the Perron time multipliers are $t=\sqrt q,q^{-1/2}$, neither equal to one. The bound wave block has indefinite energy; no positive invariant metric makes these multipliers unitary. This is precisely `obs:cusp-no-graph-vacuum`, `report/sections/04j_cusp_graph_renewal.tex:82`, rather than an exception to it. A Schrödinger eigenstate has a stationary density, and the Markov operator $A/(q+1)$ fixes the constant, but these are other dynamics.

In the H-LP model all bound data have been removed. If one extends it by the prescribed vacuum $\widetilde Z=1\oplus Z$, $\widetilde J=0\oplus J$, then every rebound leaves the vacuum without an exit. This follows from the zero exit map, independently of the number of cusps; it is `prop:graded-stationary-segment`, `report/sections/04h_rebound_state.tex:130`. No choice of $\Phi$ changes that defect. Thus the rigorous conclusion is that adding cusps supplies no vacuum exit in this construction. Finite volume alone does not prohibit designing a different dynamics or a different defect on bound states.

## T5(b). Funnel self-energy and the next candidate — STATUS: CORRECTED

The constant-type determinant below is proved from APW's stated outgoing conditions. The proposed vacuum-leak system remains open.

APW's outgoing constant-type cusp condition is $f(w)=\sqrt q\,f(v)/\mu$, whereas its funnel condition is $f(w)=f(v)/(\sqrt q\mu)$; see `2603.26443:final_draft.tex:1915`. With diagonal entries $c_v,f_v$ as defined at `:1901`, their unnormalised self-energies are $c_v\sqrt q/\mu$ and $f_v/(\sqrt q\mu)$. Dividing by $\sqrt q$ for the notebook gives

$$
\Sigma_{\rm cusp}(z)=C_{\rm cusp}/z,\qquad
\Sigma_{\rm funnel}(z)=C_{\rm funnel}/(qz),
$$

and consequently

$$
\boxed{p_{\rm funnel}(z)=\det\big((1+z^2)I-zT_X-C_{\rm cusp}-q^{-1}C_{\rm funnel}\big)}.
\tag{5.1}
$$

The same Laurent factor $(-1)^n(2z)^{-n}$ relates it to APW's $H$. This is their constant-type finite resonance matrix; it is not a proof that a funnel's full wave space is a single standard ray. The one-vertex $(q+1)$-funnel tree gives $p=z^2-q^{-1}$, agreeing with APW at `2603.26443:final_draft.tex:1928`.

On an infinite-volume funnel the constant function is not $\ell^2$, so the finite-volume bound-state argument no longer applies. A core with a cusp and a funnel is a small candidate for studying simultaneous arithmetic resonances and leakage. Whether it preserves the desired zeta factor and supplies the desired even exit is open. In particular a globally constant function is not automatically a resonance outgoing on both sorts of end: the cusp outgoing constant condition requires $z=\sqrt q$, while the funnel one requires $z=1/\sqrt q$. Formula (5.1) changes the determinant, and any redesign must also maintain the intended regularity data. “Zeros from the cusp, vacuum leak from the funnel” is a research target, not a proved decomposition.

# 6. T6. Genus, class number, and the number-field prediction

**T6 — STATUS: OPEN (H-CLASS, H-ARITH).** Under H-CLASS, a genus-$g$ curve with one removed rational point and $h=|\operatorname{Pic}(R)|$ cusps has one arithmetic character channel carrying its zeta numerator of degree $2g$, hence $4g$ nonzero square-root resonances; the $z\leftrightarrow-z$ bipartite pairing is this same doubling, not a second factor of two. Each nontrivial geometrically nontrivial unramified character has an $L$ polynomial of degree $2g-2$ and would supply $4g-4$ square-root resonances, subject to the specified scattering conventions and cancellations. At genus one the nontrivial polynomials are $1$: D3's height-normalised one-zeta/three-monomial decomposition is consistent with this prediction. At genus two the testable prediction is eight zeta resonances and four for each of the $h-1$ nontrivial character channels, all at $|z|=q^{-1/4}$, a total $4h+4$ before separate delay, bound, cusp-form, and threshold bookkeeping. These are character channels, not necessarily individual geometric spikes. For number fields the analogous properly normalised Eisenstein character factors are expected to involve Hecke $L$-functions; identifying every factor and its zero divisor requires the relevant theorem and conventions, not the graph automorphism group. Efrat's $\mathrm{PGL}_2(\mathbb F_q[T])$ result is not a number-field theorem, and the proposed Hejhal/Li inputs are not locally available. APW's expectation is stated at `2603.26443:final_draft.tex:2085` and `:2088`; the notebook's distinct $\Gamma_0(N)$/Dirichlet-$L$ direction remains exactly H-ARITH as recorded in `obs:cusp-arith-next`, `report/sections/04j_cusp_graph_renewal.tex:161`.

# Correction ledger

| No. | Draft claim or missing qualification | Correction |
|---:|---|---|
| 1 | The stabiliser figures establish the arithmetic quotient without an input theorem. | H-DIAG-2/3; the degree and determinant consistency checks are proved independently. |
| 2 | $T_X=D^{-1/2}A_XD^{-1/2}/\sqrt q$ for coordinate adjacency. | Use $D^{-1/2}A_XD^{1/2}/\sqrt q$; the two inverse factors apply to the measure kernel. |
| 3 | APW's displayed polynomial is literally $\det H$ for these cores. | The Laurent factors are $1/(128z^4)$ and $-1/(1536z^5)$. |
| 4 | APW and the model count the same resonances. | APW retain nonzero cusp/threshold/exterior parameters; the model retains disk zeros and delay modes. |
| 5 | Poles of $\det S$ always enumerate all bound states for $h>1$. | Matrix poles do; a determinant can hide a pole against a different channel's zero. Confined states are invisible. |
| 6 | A multichannel scalar gcd consists only of cusp and threshold factors. | Counterexample in C3; use matrix partial multiplicities. D2/D3 have only the stated scalar factors. |
| 7 | Orthogonality to all attachment vertices supplies an extra kind of core eigenvector. | For eigenvectors it is precisely the cusp-form condition; use the orthogonal complement of the full Krylov span. |
| 8 | Zero is excluded by the Weil-circle statement. | It is a model delay eigenvalue, excluded only from APW's nonzero parameter space and from the Hasse--Weil sector. |
| 9 | Zero multiplicity follows just from exit count or rank defect. | Use the Schur coefficient (0.6); D2 has order two and D3 order four, from one and two unit-diagonal attachments. |
| 10 | Threshold zeros might imply a singular D3 matrix. | All entries are removable; (0.7) has two $+1$ eigenvalues at each threshold, matching the half-bound count. |
| 11 | Two cusp-form wave parameters represent twice as many adjacency eigenfunctions. | Both $\pm i$ parametrise the same two-dimensional $\lambda=0$ eigenspace. |
| 12 | D3's entire core zero eigenspace consists of cusp forms. | Core nullity three; joint-attachment-vanishing nullity two. |
| 13 | Equal Weil modulus gives RH for the full diagram model. | Only for its four-dimensional Hasse--Weil sector; the full model also has zero roots. |
| 14 | A spectral square root canonically identifies the model with Frobenius cohomology. | Only a similarity of complex operators is proved; no canonical or energy-isometric identification. |
| 15 | Two prefactor examples establish a genus law. | $q^{1-2gs}$ is H-EIS, not a theorem here. |
| 16 | Review finding 7 forces extra bound spectrum in D2. | Its $c^2=q+1$ premise fails; D2 has $c^2=1$ and nonzero-root product $-1$. |
| 17 | The nonzero-root product has a normalisation/sign ambiguity. | Monicity fixes (1.4); D2 gives exactly $-1$. |
| 18 | The raw D3 even eigenvalues cannot be separated by a height change. | $D=\operatorname{diag}(1,z)$ gives exactly $(R_3,z^2)$ in a fixed basis. |
| 19 | The height congruence is an unchanged model or a similarity. | It changes zero/delay counts and individual eigenvalues; nonzero divisor positions survive. |
| 20 | The four cusps are transitively permuted by graph automorphisms/class characters. | The visible graph group is Klein with two cusp orbits; arithmetic character identification is H-CLASS. |
| 21 | Matrix bound factors can be multiplied without order or directions. | Use an ordered minimal right Blaschke--Potapov product, with updated pole spaces. |
| 22 | The Hardy model proves the geometric wave completion. | The model is proved; its geometric realisation remains H-LP. |
| 23 | “No decoupled mode” means all vectors have immediate flux. | No nonzero vector has zero flux at every time; some instantaneous fluxes vanish. |
| 24 | The holding law is simply an $h\times h$ matrix. | It is a CP instrument on $h\times h$ exit matrices, with an $h^2\times h^2$ transfer representation. |
| 25 | Stationary uniqueness iff irreducibility. | Uniqueness iff the exit renewal channel has one stationary density; irreducibility is sufficient, not necessary. |
| 26 | A scalar gcd/aperiodicity assertion handles every quantum rebound. | Use the peripheral spectrum or (3.8); the scalar gcd applies to fixed resets. |
| 27 | The common-radius stationary criterion holds for arbitrary exit-dependent $\Phi$. | It holds for the fixed-reset family; a general $\Phi$ has an additional flux-reinsertion condition. |
| 28 | Arithmetic singles out Hasse--Weil rebounds. | Such modal rebounds pass the equal-radius test; no selection or canonicity follows. |
| 29 | Covariant channels preserve Hilbert-space symmetry blocks. | They preserve operator-space representation types and can transfer populations between inequivalent Hilbert blocks. |
| 30 | Hasse--Weil and delay sectors are orthogonal. | They are invariant spectral summands, generally nonorthogonal; the graph-symmetry even/odd split is orthogonal. |
| 31 | The canonical D2 defect rebound is nonmodal and may see the Hasse--Weil sector. | It is a pure zero eigenmode with $\rho_\infty=\Omega_J$, $m=\delta_1$, and mean one. |
| 32 | The characteristic transfer directly generates the same-defect holding amplitudes. | It links opposite defects; (4.5) and (4.3) are different transfer experiments. |
| 33 | Modal weights are the density eigenvalues in the energy metric. | The eigenvalues are the weighted Gram spectrum. |
| 34 | Rescaled $Z$ is already unitary in the Lax--Phillips metric. | The positive diagonal metric cone (4.8) is different; parity and reality together select one ray. |
| 35 | Merely rereading a density in a new metric preserves the channel. | Adjoints, normalisations, defects, and positive rank-one states must be rebuilt. |
| 36 | Hecke commutation alone forces a mode-diagonal rebound. | Need arithmetic correspondences, adjoint-compatible action, spectral separation, and a selection condition: H-HECKE. |
| 37 | Finite volume and bounded degree alone make the constant an eigenfunction. | They give membership and boundedness; constant degree is also necessary. |
| 38 | The Perron bound mode is stationary under the notebook wave group and invisible to scattering. | Wave multipliers are $q^{\pm1/2}$; the mode gives a visible bound pole and no radiating flux. |
| 39 | Finite volume rules out every possible vacuum exit or rebound dynamics. | It gives no exit in the specified bound-deleted/$1\oplus Z$ construction; a different defect is a different model. |
| 40 | A funnel automatically leaks the same vacuum and preserves the zeta zeros. | (5.1) changes the resonance determinant; mixed cusp/funnel outgoing conditions for the constant disagree. The target is open. |
| 41 | Square root and bipartiteness each double the Hasse--Weil count. | They are the same doubling: degree $2g$ gives $4g$, not $8g$. |
| 42 | Each geometric spike individually carries a nontrivial $L$ divisor. | The prediction concerns arithmetic character channels after normalisation and cancellation; it is H-CLASS. |
| 43 | The report's modal aperiodicity criterion requires $c\ne1$. | Any modal mixture has positive one-step holding probability, including a pure zero mode at $c=1$. |
| 44 | The arithmetic metric can retain the same one-exit defect. | Its Hasse--Weil defect is $(1-r^2)I_4$, of rank four; a new completion needs at least four exit coordinates. |

# Numerical checks

All computations used `python3` in memory; no auxiliary file was written. The following compact reproduction records the essential code used in the exact determinant, transfer, and numerical checks. The longer intermediate resolvent and polynomial-coordinate Gram computations used the same matrices and are displayed explicitly above.

```python
# Author: codex:gpt-6-astra
import sympy as s
import numpy as np
z = s.symbols('z')
data = [
 (2, [6,2,2,1,3,3],
  [(0,1,2),(1,2,2),(2,3,1),(3,4,1),(3,5,1)], [1]),
 (3, [48,12,6,2,8,6,12,48,4],
  [(0,1,12),(1,2,6),(2,3,2),(3,4,2),(3,5,2),
   (3,8,2),(5,6,6),(6,7,12)], [1,6,8,8])]
for q, sv, edges, exits in data:
    n = len(sv); T = s.zeros(n); W = s.zeros(n,len(exits))
    for i,j,e in edges:
        T[i,j] = T[j,i] = s.sqrt(s.Rational(sv[i]*sv[j],q*e*e))
    for a,v in enumerate(exits): W[v,a] = 1
    p = s.factor(((1+z*z)*s.eye(n)-z*T-W*W.T).det())
    pt = s.factor(z**(2*n)*p.subs(z,1/z))
    print(q, p, pt, 'core nullity', len(T.nullspace()))

Z = s.zeros(6)
Z[0,1]=s.Rational(2,3); Z[0,3]=-s.sqrt(5)/6; Z[1,0]=1
Z[2,1]=s.sqrt(5)/3; Z[2,3]=s.Rational(1,3); Z[3,2]=1
Z[4,3]=s.sqrt(3)/2; Z[5,4]=1
j=s.eye(6)[:,5]
k=s.Matrix([s.sqrt(15)/6,0,-s.sqrt(3)/3,0,s.Rational(1,2),0])
assert s.simplify(s.eye(6)-Z.T*Z-j*j.T) == s.zeros(6)
assert Z*j == s.zeros(6,1)
print('characteristic transfer',s.factor((z*k.T*(s.eye(6)-z*Z.T).inv()*j)[0]))
print('holding probabilities',[(j.T*Z**m*j)[0]**2 for m in range(6)])

for w in [.4+.2j,.8+.1j,1.2+.3j]:
    P=lambda t: 1-2*t+2*t*t
    zet=lambda t: P(t)/((1-t)*(1-2*t))
    R=w*w*(w*w-2)*(2*w**4-2*w*w+1)/((2*w*w-1)*(w**4-2*w*w+2))
    rhs=w**(-2)*zet(w**(-2))/zet(w**(-2)/2)
    print('D2',w,1/R,rhs,abs(1/R-rhs))
    den=(3*w*w-1)*(w**4+3); f=(w*w-1)*(3*w**4-2*w*w+3)
    E=np.array([[w*w*f,-4*w**3*(w*w+1)],[-4*w**3*(w*w+1),f]])/den
    D=np.diag([1,w]); R3=w*w*(w*w-3)*(3*w**4+1)/den
    target=.5*np.array([[R3+w*w,R3-w*w],[R3-w*w,R3+w*w]])
    print('D3 odd, raw even eigenvalues',w*w,np.linalg.eigvals(E))
    print('renormalised even',R3,w*w,'error',np.linalg.norm(D@E@D-target))
```

Both exact determinant outputs are (1.1) and (2.1), including all prefactors and reversed signs; the core nullities are $2,3$. Exact model checks give $I-Z^*Z=e_6e_6^*$, $Zj=0$, characteristic transfer (3.1), and holding probabilities $(1,0,0,0,0,0)$. A separate $65536$-point Hardy-circle quadrature/Cholesky calculation gave defect error $2.26\cdot10^{-15}$, $\|Zj\|=2.60\cdot10^{-16}$, stationary spectrum $(1,0,0,0,0,0)$ within $2.3\cdot10^{-15}$, and holding probabilities $1.0000000000000036$ followed by errors below $3.4\cdot10^{-32}$ for times two through six. The exact stationary residual is zero. This tests the stationary state in the original Hardy metric, as well as in (4.4).

| $z$ | $1/R_2$ and $z^{-2}\zeta_K(2s-1)/\zeta_K(2s)$ | absolute discrepancy |
|---|---|---:|
| $0.4+0.2i$ | $2.33990999314517-4.40044109319584i$ | $3.21\cdot10^{-15}$ |
| $0.8+0.1i$ | $-0.931306791196057-0.483864702872824i$ | $1.12\cdot10^{-16}$ |
| $1.2+0.3i$ | $-0.390487639866608-0.228291810112627i$ | $1.58\cdot10^{-16}$ |

The three D3 symmetry channels are $q_-=-1$, $l_-=z^2$, and the even matrix. The latter's two raw eigenvalues and its renormalised zeta eigenvalue are:

| $z$ | $l_-$ | raw even eigenvalues | $R_3$ after (2.6) |
|---|---|---|---|
| $0.4+0.2i$ | $0.12+0.16i$ | $0.07100610+0.22451430i$, $0.93438072+0.34809315i$ | $-0.01180516+0.23449857i$ |
| $0.8+0.1i$ | $0.63+0.16i$ | $0.80004597+0.10679685i$, $-1.19996697+0.27726965i$ | $-0.98964026+0.09367577i$ |
| $1.2+0.3i$ | $1.35+0.72i$ | $-0.92159770+0.32690241i$, $1.17909435+0.30071498i$ | $-1.18495509+0.10831055i$ |

The other renormalised even eigenvalue is $z^2$ in every row; errors in the full matrix identity (2.6) were below $4.8\cdot10^{-16}$. The four D2 roots are $\pm(0.776886987015019+0.321797126452791i)$ and their conjugates; all have modulus $0.8408964152537145$. The uniform modal density eigenvalues are those reported after (4.7), not $(1/4,1/4,1/4,1/4)$.

An independent direct solve used $S=-I+(1-z^2)W^*[(1+z^2)I-zT_X-z^2WW^*]^{-1}W$ at the three table points and five unit-circle points. Its maximum discrepancy from (1.1)/(2.2)--(2.4) was $2.08\cdot10^{-15}$, and the maximum unitarity error was $1.69\cdot10^{-15}$. Symbolic substitution of (1.2) gave identically zero residual for both zeta identities. Exact Euclidean gcd of the D3 discriminant numerator and its derivative was $1$.

# What a refuter should attack first

* The directional pole removal in T3 and its geometric identification under H-LP; a determinant alone is insufficient.
* The distinction between height congruence (2.6), class characters, and the original model's delay count.
* The same-defect versus opposite-defect transfer calculation (4.3)--(4.5), which makes the canonical rebound trivial.
* The precise additional arithmetic and adjoint data required by H-CLASS and H-HECKE.
* Any claim that adding a funnel preserves the zeta divisor or makes the original bound wave mode stationary.
