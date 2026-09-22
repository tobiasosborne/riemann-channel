# Connes’s weighted topology and the arithmetic metric

Author: `codex:gpt-6-astra`

| Claim | Verdict | Statement |
|---|---|---|
| W1 | SHARPENED | Exact minimal closed domain; G₀eρ=bρ; derivative product and unbounded biorthogonals; nearest-gap equivalence false. |
| W2 | REFUTED / SHARPENED | Exact transported weight has X²/4; Gram tail is 1/gap; no upper or lower Riesz bound for any fixed δ; inequivalent to Q₀. |
| W3 | SHARPENED / REFUTED | Dual is the closed span of admitted uncut characters/jets; cut-and-damp is bounded and injective, is synthesis rather than evaluation inverse, and does not land wholly in D(Q₀). |
| W4 | SHARPENED / REFUTED | Energy instantaneous loss is all ones, arithmetic loss I/2; inverse history gives G₀; scalar-exit diagonal congruences are many and lie outside the C3 cone. |
| W5 | SHARPENED / OPEN | Three distinct metrics/topologies; C3 needs the diagonal arithmetic form; a zero-free construction identifying its minimal graph domain remains missing. |

## Correction ledger

Corrections C1–C18 are collected in §7; each is established in the corresponding W1–W5 proof. The proposed identification via the fixed named modes is REFUTED even on their common finite span; no claim is made against abstract Hilbert-space isomorphisms. A zero-free domain construction remains OPEN.

## 0. Conventions and scope — PROVED

Author: `codex:gpt-6-astra`

All inner products are linear in the first slot. We retain `notes/deninger-bond/astra-proofs.md:23–53`: \(X=\log y\), Fourier transform \(\widehat f(u)=\int f(X)e^{iuX}dX\), boundary measure \(du/(2\pi)\),
\[
\Theta(u)=\frac{\xi(1+2iu)}{\xi(1-2iu)},\quad K=H^2_+\ominus\Theta H^2_+,\quad
C_t=(P_KM_{e^{itu}}|_K)^*,\quad C_tf(X)=f(X+t).
\tag{0.1}
\]
For \(\rho=\sigma+i\gamma\), write
\[
w_\rho=\gamma/2+i(1-\sigma)/2,\quad d_\rho=-i\bar w_\rho,
\quad e_\rho(X)=e^{d_\rho X}1_{X>0},\quad k_\rho(u)=(u-\bar w_\rho)^{-1},
\quad\widehat e_\rho=ik_\rho.
\tag{0.2}
\]
The \(X\)-space and its Fourier image are identified unitarily; formulas involving \(\mathcal C_\Theta\) use the Fourier image. Here \(\mathcal C_\Theta F=\Theta\overline F\) is the model conjugation. The pure Blaschke property, full-jet completeness and minimality are retained from `report/sections/04q_h_theta.tex:82–105` and `report/sections/04r_h_theta_channels.tex:77–105`. No previously refuted theta cyclic-and-cut identification is reinstated. Unless explicitly stated otherwise, W1, W2's assertions about the entire zero system, and W4's arithmetic model assume **RH and simplicity**. Sums then run over all signed ordinates, once each. The counting input is Riemann–von Mangoldt, as recorded in `notes/deninger-bond/astra-proofs.md:53`; this is an input, not a new proof of that theorem.

Matrices \(M_{ij}=\langle e_i,e_j\rangle\) represent forms as \(a^TM\bar a\). Their transposes \(H=M^T\) represent the same norms as \(a^*Ha\). This distinction fixes every conjugation below.

## 1. W1: the unit-coefficient form — SHARPENED

Author: `codex:gpt-6-astra`

### 1.1 The biorthogonal constants — PROVED

For a simple zero \(w_j\) of \(\Theta\),
\[
\boxed{\quad b_j(u)=\frac{\Theta(u)}{\Theta'(w_j)(u-w_j)}
=\frac1{\Theta'(w_j)}\mathcal C_\Theta k_j(u),\qquad
\langle e_i,b_j\rangle=\delta_{ij}.\quad}
\tag{1.1}
\]
Indeed \(ik_w\) is the actual evaluation kernel: \(\langle F,ik_w\rangle=F(w)\). The function in (1.1) has values \(b_j(w_i)=\delta_{ij}\), so conjugate symmetry proves the displayed biorthogonality. There is no extra \(i\) in (1.1); using \(k_j\), rather than \(ik_j\), as the named modes would change the constant. Antiunitarity and a one-pole integral give, with \(h_j=\Im w_j\),
\[
\|k_j\|^2=\int_{\mathbb R}\frac{du}{2\pi|u-\bar w_j|^2}=\frac1{2h_j},
\qquad \boxed{\ \|b_j\|^2=\frac1{2h_j|\Theta'(w_j)|^2}
=\frac{2}{|\Theta'(w_j)|^2}\quad\text{under RH}.\ }
\tag{1.2}
\]
Only simplicity is needed for (1.1); RH supplies the common height \(h=1/4\). The system \(b_j\) is complete because \(\mathcal C_\Theta\) is antiunitary and the ordinary kernels are complete under simplicity (`notes/deninger-bond/astra-proofs.md:168–173,311–317`).

### 1.2 Exact minimal closed domain; no implicit basis assertion — PROVED

Let \(\mathcal E=\operatorname{span}_{\rm fin}\{e_j\}\), and let \(S_0:c_{00}\subset\ell^2\to K\) and \(B_0:\mathcal E\subset K\to\ell^2\) be
\[
S_0a=\sum_j a_je_j,\qquad B_0S_0a=a.
\tag{1.3}
\]
Both are closable. For \(B_0\), convergence in \(K\) gives coordinate convergence through (1.1). For \(S_0\), if \(a^{(n)}\to0\) and \(S_0a^{(n)}\to f\), then \(\langle f,b_j\rangle=0\) for every \(j\), hence \(f=0\). Put \(B=\overline B_0\), \(S=\overline S_0\). Their graphs are reversals of one another, so \(S=B^{-1}\) with their actual domains. Explicitly,
\[
\begin{split}
\mathcal D(Q_0)=\mathcal D(B)=\{f\in K: &\exists a^{(n)}\in c_{00},\ a^{(n)}\to a\text{ in }\ell^2,\\
&S_0a^{(n)}\to f\text{ in }K\},\qquad
Bf&=(a_j(f))_j=(\langle f,b_j\rangle)_j,\\
Q_0(f,g)&=\langle Bf,Bg\rangle_{\ell^2},\qquad Q_0(f)=\sum_j|a_j(f)|^2.
\end{split}
\tag{1.4}
\]
The coefficient limit in (1.4) is unique. This is an exact domain description with a finite-sum graph core, not the unsupported assertion that every vector has an ordinarily convergent modal series. In particular, the notation \(f=\sum a_je_j\) means the joint approximation in (1.4). The maximal coefficient operator
\[
B_{\max}f=(\langle f,b_j\rangle)_j,\qquad
\mathcal D(B_{\max})=\{f\in K:(\langle f,b_j\rangle)_j\in\ell^2\}
\tag{1.5}
\]
is closed and extends \(B\). Equality with (1.4) is **not used or asserted**: it requires a graph-core/synthesis argument beyond completeness and minimality. Likewise partial sums in an arbitrarily prescribed enumeration are not asserted to converge.

The form is densely defined, closed for \((\|f\|_K^2+Q_0(f))^{1/2}\), and positive definite, since the \(b_j\)'s are complete. Its representing operator is
\[
\boxed{\quad G_0=B^*B,\qquad
\mathcal D(G_0)=\{f\in\mathcal D(B):Bf\in\mathcal D(B^*)\},\qquad G_0e_j=b_j.\quad}
\tag{1.6}
\]
Here \(Q_0(f,g)=\langle G_0f,g\rangle_K\) for \(f\in\mathcal D(G_0)\), \(g\in\mathcal D(B)\). A useful completely explicit adjoint criterion is
\[
h\in\mathcal D(B^*)\ \Longleftrightarrow\
\exists v\in K\quad \langle v,e_j\rangle=h_j\ \text{for every }j;
\qquad B^*h=v.
\tag{1.7}
\]
The vector is unique by completeness of the \(e_j\)'s. This follows by testing the adjoint identity on finite sums, which are a graph core. Taking \(h=\delta_j\) gives \(B^*\delta_j=b_j\), proving (1.6). Thus \(G_0\) does **not** have \(e_j\) as eigenvectors of eigenvalue one in the energy metric.

### 1.3 Similitude and the two completions — PROVED

Under RH, \(d_j=-1/4-i\gamma_j/2\). Boundedness of \(C_t\) on \(K\), boundedness of the diagonal multiplier on \(\ell^2\), and the approximants in (1.4) prove
\[
C_t\mathcal D(B)\subset\mathcal D(B),\quad
BC_tf=\operatorname{diag}(e^{td_j})Bf,\quad
Q_0(C_tf,C_tg)=e^{-t/2}Q_0(f,g),\qquad t\ge0.
\tag{1.8}
\]
RH is used for the common modulus; simplicity is used for the complete ordinary-mode model. On the **completion for \(Q_0\) alone**, \(B\) extends to a unitary identification with \(\ell^2\), since its range contains \(c_{00}\). There \(e^{t/4}C_t\) extends to a unitary group. This does not assert that negative time acts boundedly on \(K\), or that \(C_t\mathcal D(B)=\mathcal D(B)\). The form domain with its graph norm and the arithmetic completion are different spaces.

Both norm comparisons fail. Close pairs give \(Q_0(e_i-e_j)=2\) while \(\|e_i-e_j\|_K\to0\), so \(G_0\) is unbounded. In the other direction, every fixed sufficiently short ordinate interval contains arbitrarily large finite clusters somewhere on the line: partition \([T,2T]\) into intervals of that length and use \(N(2T)-N(T)\asymp T\log T\). For a cluster of \(n\) modes, \(\Re\langle e_i,e_j\rangle\ge1\) if all ordinate differences are at most one. Thus
\[
Q_0\Big(\sum_{j=1}^ne_j\Big)=n,\qquad
\Big\|\sum_{j=1}^ne_j\Big\|_K^2\ge n^2.
\tag{1.9}
\]
Consequently \(G_0\) has no positive lower spectral bound, although \(\ker G_0=0\); its inverse on its range is unbounded. In particular \(Q_0\) alone is not a complete norm on its domain inside \(K\).

### 1.4 Exact product and spacing estimates — PROVED; nearest-gap equivalence REFUTED

For a pure Blaschke product with simple zeros, removing the factor at \(w_j\) gives
\[
|\Theta'(w_j)|=\frac1{2h_j}\prod_{k\ne j}
\left|\frac{w_j-w_k}{w_j-\bar w_k}\right|.
\tag{1.10}
\]
Under RH the common-height formula is especially simple. With \(\Delta_{jk}=\gamma_j-\gamma_k\),
\[
|\Theta'(w_j)|=2\prod_{k\ne j}\frac{|\Delta_{jk}|}{\sqrt{1+\Delta_{jk}^2}},
\qquad
\boxed{\quad \|b_j\|=\frac1{\sqrt2}
\prod_{k\ne j}\sqrt{1+\Delta_{jk}^{-2}}.\quad}
\tag{1.11}
\]
The products converge to positive values at each fixed simple zero: the tail logarithms are summable by the counting input. No singular or delay factor may be silently inserted; the notebook's pure Blaschke theorem is used here.

Let \(r_j=\min_{k\ne j}|\Delta_{jk}|\). Then
\[
\|b_j\|\ge\frac1{\sqrt2}\sqrt{1+r_j^{-2}}.
\tag{1.12}
\]
This explicit lower bound proves unboundedness along a subsequence since simple-zero gaps tend to zero. More generally, for \(R>0\), set
\[
P_j(R)=\prod_{0<|\Delta_{jk}|\le R}\sqrt{1+\Delta_{jk}^{-2}},\qquad
T_j(R)=\sum_{|\Delta_{jk}|>R}\Delta_{jk}^{-2}.
\]
The inequalities \(x/(1+x)\le\log(1+x)\le x\) give the two-sided estimate
\[
\frac{P_j(R)}{\sqrt2}\exp\!\left(\frac{T_j(R)}{2(1+R^{-2})}\right)
\le\|b_j\|\le
\frac{P_j(R)}{\sqrt2}\exp\!\left(\frac{T_j(R)}2\right).
\tag{1.13}
\]
The nearest gap alone cannot supply a uniform two-sided asymptotic. Choose \(n\) zeros in an interval of any fixed length \(\varepsilon>0\), possible by the preceding density argument. For a member \(j\), remove its nearest-neighbour factor from (1.11). At least \(n-2\) of the remaining factors are at least \(\sqrt{1+\varepsilon^{-2}}\), whether or not its globally nearest neighbour belongs to the selected cluster. Therefore
\[
r_j\|b_j\|\ge 2^{-1/2}(1+\varepsilon^{-2})^{(n-2)/2}\longrightarrow\infty.
\tag{1.14}
\]
Thus \(\|b_j\|\asymp r_j^{-1}\) with zero-independent constants is false for this very zero system, under RH and simplicity. All nearby zeros matter. Non-Riesz alone would not imply unbounded biorthogonal norms for an arbitrary system; here (1.12) proves that stronger conclusion.

## 2. W2: Connes's norm transported to the bond — REFUTED identification; SHARPENED formulas

Author: `codex:gpt-6-astra`

### 2.1 Exact weight and Fourier meaning — PROVED

Connes defines the **square norm** by
\[
\|\xi\|_\delta^2=\int_{C_k}|\xi(g)|^2(1+\log^2|g|)^{\delta/2}\,d^*g
\tag{2.1}
\]
(`refs/src/math/9811068/main.tex:736–753`, equation (12)). His Appendix calls it a Sobolev space and says the weight is “comparable to” \((1+|u|)^\delta\) (`:3574–3588`). His regular representation is explicitly “not unitary” (`:755–766`). Restrict to the trivial compact-character sector over \(\mathbb Q\); normalize the compact factor to mass one. Put \(r=|g|\), \(v=\log r\), and **\(X=2v\)**, because the notebook has \(y=r^2\) (`notes/h-theta/astra-proofs.md:11–18`). The unitary change of density is
\[
f(X)=2^{-1/2}\xi(e^{X/2}),\qquad
\|\xi\|_\delta^2=\int_{\mathbb R}|f(X)|^2(1+X^2/4)^{\delta/2}\,dX.
\tag{2.2}
\]
Use the notation
\[
w_{\delta,c}(X)=(1+X^2/c^2)^{\delta/2},\qquad
\|f\|_{\delta,c}^2=\int |f(X)|^2w_{\delta,c}(X)dX.
\tag{2.3}
\]
The exact transported norm has \(c=2\); the brief's convenient equivalent norm has \(c=1\). For \(\delta\ge0\),
\[
2^{-\delta}w_{\delta,1}\le w_{\delta,2}\le w_{\delta,1}.
\tag{2.4}
\]
Thus changing \(c\) changes numerical Gram entries, but none of the equivalence obstructions. Under the notebook Fourier transform,
\[
\|f\|_{\delta,c}^2=
\big\|(1-c^{-2}\partial_u^2)^{\delta/4}\widehat f\big\|_{L^2(du/(2\pi))}^2.
\tag{2.5}
\]
The derivative order is \(\delta/2\), in the **frequency** variable \(u\). This is a weight in \(X\), not a smoothing operation on the cutoff exponential in \(X\).

For \(\delta\ge0\), its restriction to \(K\) is the closed form with domain
\[
\mathcal D(Q_{\delta,c}^{K})=K\cap L^2(w_{\delta,c}dX),\qquad
Q_{\delta,c}^{K}(f)=\|f\|_{\delta,c}^2.
\tag{2.6}
\]
Closedness follows from closedness of multiplication by \(w_{\delta,c}^{1/2}\) and closedness of \(K\) in energy. The domain is dense because it contains every finite full-jet sum. No assertion that these sums are a core for (2.6) is needed. In particular, the closure of its restriction to those sums agrees with their weighted-norm completion inside (2.6), regardless of whether this is the entire domain.

### 2.2 Exact Gram, special functions and the endpoint tail — PROVED

Under RH write \(\alpha=1/2\), \(\tau_{ij}=(\gamma_i-\gamma_j)/2\), and define, for \(\Re s>0\),
\[
F_{\delta,c}(s)=\int_0^\infty e^{-sX}(1+X^2/c^2)^{\delta/2}dX.
\]
Then
\[
\boxed{\quad M^{\delta,c}_{ij}=\langle e_i,e_j\rangle_{\delta,c}
=F_{\delta,c}(\alpha+i\tau_{ij}),\quad
\|e_j\|_{\delta,c}^2=N_{\delta,c}:=F_{\delta,c}(1/2).\quad}
\tag{2.7}
\]
Every diagonal is identical; off-diagonals are nonzero in general. RH is precisely what makes the real exponential decay independent of \(j\).

Here are explicit special-function formulas with specified branches. Put \(p=\delta/2\), \(\nu=p+1/2\). For \(\delta\ge0\),
\[
F_{\delta,c}(s)=c^{-2p}\frac{\sqrt\pi\,\Gamma(p+1)}2
\left(\frac{2c}{s}\right)^{p+1/2}
\big[\mathbf H_{p+1/2}(cs)-Y_{p+1/2}(cs)\big],
\tag{2.8}
\]
where \(\mathbf H\) is the Struve function, \(Y\) the Bessel function of the second kind, and all powers/functions are continued from real \(s>0\) through \(\Re s>0\). An alternative using only ordinary Tricomi confluent hypergeometric functions, valid for every real \(\delta\), is the absolutely convergent series
\[
\boxed{\quad F_{\delta,c}(s)=c\sum_{n=0}^\infty
(-2)^n\binom pn\Gamma(n+1)
U(n+1,\delta-n+2,cs).\quad}
\tag{2.9}
\]
For a direct proof of (2.9), substitute \(X=ct\), factor
\((1+t^2)^p=(1+t)^{2p}(1-2t/(1+t)^2)^p\), and use the binomial series. Its expansion variable lies in \([0,1/2]\), so termwise integration is absolutely justified with the exponential majorant. Each term is the defining integral
\(\Gamma(a)U(a,b,z)=\int_0^\infty e^{-zt}t^{a-1}(1+t)^{b-a-1}dt\).
This also supplies a convergent evaluation formula without delicate cancellation of special functions. Formula (2.8) is the Laplace–Struve form of the same integral: integration of the derivative of \(e^{-zt}(1+t^2)^{p+1}\) gives
\(zL''+(2p+2)L'+zL=1\) for \(L(z)=F_{\delta,c}(z/c)/c\); reduction by \(L=z^{-\nu}V\) gives the inhomogeneous Bessel equation. Its solution with the Laplace integral's nonoscillatory inverse-power asymptotic on the positive axis is the stated \(\mathbf H_\nu-Y_\nu\) combination. The remaining homogeneous solutions oscillate and cannot have that full asymptotic. Analytic continuation gives the right half-plane formula.

For even \(\delta=2m\), a useful finite formula avoiding special functions is
\[
F_{2m,c}(s)=\sum_{r=0}^m\binom mr\frac{(2r)!}{c^{2r}s^{2r+1}},\quad
F_{0,c}(s)=\frac1s,\quad F_{2,c}(s)=\frac1s+\frac{2}{c^2s^3}.
\tag{2.10}
\]
Repeated integration by parts, using integrability of every derivative after multiplication by \(e^{-\alpha X}\), proves for fixed \(\delta,c,\alpha>0\)
\[
F_{\delta,c}(\alpha+i\tau)=\frac1{\alpha+i\tau}
+\frac{\delta}{c^2(\alpha+i\tau)^3}+O_{\delta,c,\alpha}(|\tau|^{-5}),
\qquad |\tau|\to\infty.
\tag{2.11}
\]
The same statement holds for real \(\delta\), including zero. The leading boundary value is \(w_{\delta,c}(0)=1\); its first derivative is zero. Therefore
\[
|M^{\delta,c}_{ij}|\sim \frac2{|\gamma_i-\gamma_j|}.
\tag{2.12}
\]
**REFUTED:** the proposed \(|\gamma_i-\gamma_j|^{-1-\delta}\) decay and the claimed smoothing. The jump of \(e^{-X/2}w_{\delta,c}(X)1_{X>0}\) at zero preserves the \(1/|\tau|\) tail. A faster-decaying real part does not change the modulus estimate.

### 2.3 Neither Riesz bound exists, for any fixed exponent — PROVED

Set \(v_j=e_j/\sqrt{N_{\delta,c}}\) and \(R(\tau)=F_{\delta,c}(1/2+i\tau)/N_{\delta,c}\). The following proof works for **every fixed real** \(\delta\) and \(c>0\), although Connes's cokernel theorem uses \(\delta>1\).

1. **No lower bound.** Distinct simple-zero gaps tend to zero. Since \(|e^{-i\tau X}-1|\le|\tau|X\),
\[
\|v_i-v_j\|_{\delta,c}^2\le
\frac{\tau_{ij}^2}{N_{\delta,c}}
\int_0^\infty X^2e^{-X/2}w_{\delta,c}(X)dX\longrightarrow0.
\tag{2.13}
\]
The coefficient vector has squared \(\ell^2\)-norm two. This rules out a positive lower Gram bound.

2. **No upper bound either.** By continuity at zero choose \(\varepsilon>0\) with \(\Re R(\tau)\ge1/2\) for \(|\tau|\le\varepsilon\). Counting supplies arbitrarily large clusters of \(n\) ordinates in an interval of length \(2\varepsilon\). Then
\[
\left\|\sum_{j=1}^n v_j\right\|_{\delta,c}^2\ge n^2/2,
\qquad \sum_{j=1}^n|1|^2=n.
\tag{2.14}
\]
Thus the normalized weighted Gram defines no bounded operator on all \(\ell^2\); there is no Schur-test threshold in \(\delta\). Unbounded local density defeats an upper bound even for kernels with arbitrarily rapid off-diagonal decay. The matrix depends on frequency differences but is not a Toeplitz matrix in the zero index, because the frequencies are not a lattice.

Consequently neither \(Q_{\delta,c}^K\le C Q_0\) nor \(Q_0\le C Q_{\delta,c}^K\) holds even on \(\mathcal E\), for any finite constant \(C\). The two forms are neither equal nor boundedly equivalent. Taking form closures cannot change this failure on the shared finite-sum domain. Also a diagonal-conformal metric must make distinct frequencies orthogonal; (2.7) fails that condition. This decisively refutes the identification in the brief, not merely one proposed proof of it.

## 3. W3: the cokernel dual and the cut-and-damp map — SHARPENED

Author: `codex:gpt-6-astra`

### 3.1 What Connes's theorem actually realizes — PROVED using the cited theorem

Connes's map and its equivariance are
\[
E(f)(g)=|g|^{1/2}\sum_{q\in\mathbb Q^*}f(qg),\qquad
EU(a)=|a|^{1/2}V(a)E.
\tag{3.1}
\]
The domain is the completion of adelic Schwartz functions with \(f(0)=\int f=0\) for his pulled-back norm; \(E\) is an isometry, so its range is closed (`refs/src/math/9811068/main.tex:773–808,3760–3791`). These spaces are not the notebook's outgoing space merely because the source uses the letter \(X\). Its \(\delta>1\) cokernel is \(L^2_\delta(C_\mathbb Q)/\operatorname{Im}E\). Theorem 1 says the spectral multiplicity is the “largest integer” \(n<(1+\delta)/2\) not exceeding the zero order (`:873–885`). At \(\delta=0\), \(E\) is a surjective isometry (`:2549–2556`), so the cokernel disappears.

In bond coordinates put
\[
H_\delta=L^2(w_{\delta,2}dX),\qquad H_{-\delta}=L^2(w_{\delta,2}^{-1}dX).
\]
The Hilbert anti-dual of the cokernel is the closed annihilator
\[
\mathcal N_\delta=
\{h\in H_{-\delta}:\int (Ef)(X)\overline{h(X)}dX=0\text{ for every test }f\}.
\tag{3.2}
\]
Here \(E\) has been transported by (2.2). Connes uses the **bilinear** pairing \(\int\xi\eta\) (`:3656–3678,3795–3835`); replacing \(\eta\) by \(\bar h\) gives our first-slot-linear convention. Thus the signs of the following characters are fixed, not guessed.

For a critical zero \(1/2+i\gamma\) of multiplicity \(m_\gamma\), define the uncut functions
\[
\chi_{\gamma,r}(X)=\frac{X^r}{r!}e^{-i\gamma X/2},\qquad
0\le r<m_\gamma,\quad r<\frac{\delta-1}2.
\tag{3.3}
\]
Then
\[
\boxed{\quad\mathcal N_\delta=
\overline{\operatorname{span}\{\chi_{\gamma,r}\text{ satisfying (3.3)}\}}^{\ H_{-\delta}}.\quad}
\tag{3.4}
\]
This is a **closed span**, not an orthonormal or Schauder basis assertion. No RH is required: only the critical zeros occur.

**Proof, with the source's analytic input identified.** Connes's annihilator equation is \(L(1/2+it)\widehat\psi(t)=0\) (`:4012–4017`). Spectral localization therefore makes \(\widehat\psi\) a finite sum of derivatives of point masses supported at critical zeros, of order less than the zero multiplicity (`:4058–4087`). The inverse Fourier transforms are polynomial characters; the factors \(2^r,r!\) in (3.3) just normalize his \((\log|g|)^r\). Their membership is exactly
\[
\int_{\mathbb R}|X|^{2r}(1+X^2/4)^{-\delta/2}dX<\infty
\quad\Longleftrightarrow\quad 2r-\delta<-1.
\tag{3.5}
\]
Connes proves both annihilation and sufficiency by differentiated Tate distributions (`:4106–4136`). His approximate units with compactly supported Fourier transforms (`:3619–3652,3726–3732`) give density of the localized vectors in the annihilator, as explicitly used at `:4145–4149`. Equivalently, convolution with a Schwartz approximate identity acts boundedly and tends strongly to the identity in the reciprocal polynomial weight; the proof of his weight-ratio estimate works for that weight too. This proves (3.4).

There is a source typo worth recording: `refs/src/math/9811068/main.tex:4100` prints \(2k+\delta<-1\); the integral at `:4095–4098` and the stated conclusion require **\(2k-\delta<-1\)**. Our (3.5) uses the integral, not the typo. The multiplicity count is the number of allowed \(r\), namely the largest integer \(n\le m_\gamma\) with \(n<(1+\delta)/2\). At \(\delta=3\), \(r=1\) is still excluded; the threshold is strict.

The actual dual characters in the multiplicative Haar space are \(|g|^{\pm i\gamma}\), not \(|g|^{-1/2-i\gamma}\). The latter is the corresponding generalized vector in the **additive** \(L^2(dr)\) normalization: multiplication by \(r^{1/2}\) takes it to \(r^{-i\gamma}\) in \(L^2(dr/r)\), and then \(y=r^2\) gives \(y^{-i\gamma/2}\). Keeping \(-1/2\) after changing to logarithmic Haar measure would produce exponential growth at one end and violate (3.5). Also the orthogonal representative of the cokernel in \(H_\delta\) is \(w_{\delta,2}^{-1}h\), for \(h\in\mathcal N_\delta\), not \(h\) itself; this is the Riesz identification in `:3672–3678`.

### 3.2 A bounded comparison exists, but it is not an isometry — PROVED

Define a genuine multiplication-and-restriction operator on the whole weighted dual:
\[
(Th)(X)=1_{X>0}e^{-X/4}h(X).
\tag{3.6}
\]
For every finite real \(\eta\),
\[
\|Th\|_{\eta,2}^2\le
C_{\delta,\eta}\|h\|_{-\delta,2}^2,\qquad
C_{\delta,\eta}=\sup_{X\ge0}e^{-X/2}
(1+X^2/4)^{(\delta+\eta)/2}<\infty.
\tag{3.7}
\]
This is the pointwise weight comparison under the integral, so no distributional multiplication problem occurs: elements of the dual are weighted \(L^2\) functions. In particular \(T:H_{-\delta}\to L^2(0,\infty)\) is bounded. The chosen unit-amplitude characters satisfy exactly
\[
T\chi_{\gamma,r}=\frac{X^r}{r!}e^{-X/4-i\gamma X/2}1_{X>0}=e_{\rho,r}.
\tag{3.8}
\]
The right side belongs to \(K\) by `report/sections/04r_h_theta_channels.tex:77–91`. Equations (3.4) and (3.7) therefore prove
\[
T\mathcal N_\delta\subset K\cap\bigcap_{\eta\ge0}L^2(w_{\eta,2}dX).
\tag{3.9}
\]
Its energy-closed range is the span of precisely the critical jets admitted by (3.3). Under RH and simplicity this is all of \(K\) in the sense of **dense range**, for every \(\delta>1\). With a missing critical jet or any off-line zero it is a proper closed span, by minimality of the full model system. Formula (3.8) is not an identification of Hilbert norms or a statement of surjectivity.

For completeness \(T\) is injective on \(\mathcal N_\delta\). Indeed approximate \(h\) by finite admitted character sums. Pair their \(T\)-images with the global model biorthogonal jets; the resulting individual coefficients converge continuously in \(K\). The same coefficients converge in distributions, since \(H_{-\delta}\hookrightarrow\mathcal S'\) continuously. On a small frequency interval containing just one zero, a smooth test selecting the appropriate point-mass derivative reads precisely that coefficient. If \(Th=0\), all these coefficients vanish. The Fourier transform of \(h\), supported on the discrete critical divisor by the annihilator equation, is therefore zero locally everywhere, and \(h=0\). Under simplicity these model functionals are exactly (1.1); full-jet minimality supplies the finite triangular counterparts in the general case.

With \((R_th)(X)=h(X+t)\), the orientation and damping satisfy
\[
C_tTh=e^{-t/4}TR_th\qquad(t\ge0).
\tag{3.10}
\]
This identity holds directly for functions, and \(R_t\) preserves the annihilator. It compares the polynomially bounded weighted-dual translation representation with the damped model; it does not claim either is unitarized by the weight.

### 3.3 The evaluation inverse claim is false — REFUTED; exact adjoint relation PROVED

Assume RH and simplicity for the rest of this subsection. Keep the C5 map
\(\mathcal A f=(\langle f,k_j\rangle)_j\) on its maximal square-summability domain (`notes/deninger-bond/astra-proofs.md:382–400`). Define \(A_e f=(\langle f,e_j\rangle)_j\). Then as closed operators with their actual domains,
\[
A_e=-i\mathcal A=S_0^*,\qquad A_e^*=S,
\qquad B^*=A_e^{-1},\qquad
\mathcal A^{-1}\delta_j=-ib_j
=\frac1{\Theta'(w_j)}\mathcal C_\Theta e_j.
\tag{3.11}
\]
The inverse is only on the range of the evaluation operator. The first two equalities are the synthesis/analysis adjunction; the third is exactly (1.7). The last follows from (1.1) and antilinearity of \(\mathcal C_\Theta\). Thus the cut-and-damp map is **synthesis** on the finite character coordinates,
\[
T\Big(\sum a_j\chi_{\gamma_j,0}\Big)=S_0a,
\qquad
\mathcal A^{-1}a=-i\sum a_jb_j\quad(a\in c_{00}).
\tag{3.12}
\]
They are different even on a single named coordinate. Multiplying coordinates by nonzero scalars cannot turn \(e_j\) into \(b_j\): the latter vanishes at every other zero in the Fourier picture, whereas \(e_j=ik_j\) does not. Model conjugation, which is antilinear and exchanges the adjoint and forward compression, is the additional operation in (3.11). It cannot be suppressed as a normalization constant.

There is an actual **domain separation**, stronger than inequivalent norms. In \(H_{-\delta}\), for \(\delta>1\),
\[
\|\chi_{\gamma_i,0}-\chi_{\gamma_j,0}\|_{-\delta,2}\longrightarrow0
\quad\text{if }\gamma_i-\gamma_j\longrightarrow0,
\tag{3.13}
\]
by dominated convergence, while the arithmetic coefficient vector of their \(T\)-image always has norm \(\sqrt2\). Hence \(T\) does not extend boundedly into the arithmetic completion \(\ell^2\). Moreover
\[
\boxed{\quad T\mathcal N_\delta\not\subset\mathcal D(Q_0),
\quad\text{even though (3.9) holds}.\quad}
\tag{3.14}
\]
Otherwise the everywhere-defined operator \(BT:\mathcal N_\delta\to\ell^2\) would be closed, since \(T\) is bounded into \(K\) and \(B\) is closed. The closed graph theorem would make it bounded, contradicting (3.13). Thus membership in **every** polynomially weighted outgoing norm is still insufficient for membership in the unit-coefficient domain. This rules out the proposed domain description especially sharply.

### 3.4 Jets and other arithmetic realizations — SHARPENED

All cut-and-damped model jets belong to \(K\) unconditionally: each has exponential decay rate \((1-\sigma)/2>0\). They also belong to every fixed polynomially weighted outgoing space. In contrast the uncut dual jet in (3.3) requires \(\delta>2r+1\). To see all \(m\) jets at a critical zero requires \(\delta>2m-1\); no finite exponent sees unbounded multiplicities. For \(1<\delta\le3\) only the ordinary character survives, even if the zero is multiple. Therefore no multiple-zero full-jet unitarization follows from choosing a small weight. C3 still forbids a positive conformal metric on a retained nontrivial Jordan block (`notes/deninger-bond/astra-proofs.md:179–192`).

The neighboring source constructions do not change these conclusions. Burnol defines a regularized theta map and proves its image is “dense in it” in the unweighted idele-class \(L^2\) space (`refs/src/math/0001013/main.tex:204–228`), consistent with absorption rather than an unweighted cokernel. His Sonine theorem says the evaluators are “a minimal system” for \(a\le1\) and “a complete system” for \(a\ge1\) (`refs/src/math/0203120/main.tex:516–524`); these concern \(L_a\), with a different statement for \(K_a\) (`:528–538`). His explicit structure function identifies completed Mellin transforms of the Sonine space isometrically with its de Branges space (`refs/src/math/0208121/main.tex:243–255,393–402`), whose norm comes from the even \(L^2(\mathbb R)\) space (`:259–270`). None identifies that norm with (1.4) or (2.6). Meyer places poles in \(\pi_+\) and zeros in \(\pi_-\) (`refs/src/math/0311468/main.tex:208–225`) and explicitly works on a “nuclear bornological vector space” while recording the multiple/off-line-zero obstruction to unitarity (`:298–305`). These are distinct topologies and comparison problems.

## 4. W4: one scalar exit versus an exit coordinate per mode — SHARPENED

Author: `codex:gpt-6-astra`

### 4.1 The energy form and its observation history — PROVED

Write \(D_Kf=f'\) on \(\mathcal D(D_K)=K\cap H^1(0,\infty)\). Integration by parts, in our first-slot convention, gives
\[
-\langle D_Kf,g\rangle_K-\langle f,D_Kg\rangle_K
=j(f)\overline{j(g)},\qquad j(f)=f(0).
\tag{4.1}
\]
This is an identity of forms on the generator domain, not an everywhere-defined bounded-operator identity \( -(D_K+D_K^*)=j^*j\). It is `lem:exit-one-dimensional` in `report/sections/04h_rebound_state.tex:49–57`, with that section's Fourier normalization converted as in `notes/h-theta/astra-proofs.md:18`. In particular
\[
j(e_j)=1,\qquad j\Big(\sum a_je_j\Big)=\sum a_j\quad(a\in c_{00}).
\tag{4.2}
\]
The energy Gram and its generator loss are
\[
M_{ij}=\frac{i}{w_j-\bar w_i}=\frac1{-(d_i+\bar d_j)}
=\frac2{1+i(\gamma_i-\gamma_j)},
\qquad -(d_i+\bar d_j)M_{ij}=1.
\tag{4.3}
\]
The last equality in the Gram formula assumes RH; the first two and the loss identity do not. This is exactly the first-slot correction in `notes/h-theta-1/astra-proofs.md:59–80`.

The scalar exit becomes an isometric **history** map,
\[
(\mathcal Of)(s)=j(C_sf)=f(s),\qquad
\|f\|_K^2=\int_0^\infty|j(C_sf)|^2ds.
\tag{4.4}
\]
For a general \(L^2\) vector the history is interpreted by continuity in \(L^2(ds)\), not by claiming a trace value at each time. On finite modal coordinates, if \(D=\operatorname{diag}(d_j)\) and \(\ell a=\sum a_j\), this says
\[
S_0a(s)=\ell e^{sD}a,\qquad
H=M^T=\int_0^\infty e^{sD^*}\mathbf1\mathbf1^*e^{sD}ds,
\qquad D^*H+HD=-\mathbf1\mathbf1^*.
\tag{4.5}
\]
Integrals and matrix identities are first read on every finite subfamily; the closed history/synthesis operator on \(\ell^2\) is \(S\) from (1.3). The integral is the precise relation between the Cauchy metric and the all-ones exit. It uses the **entire time history**, not just the value \(\ell a\).

### 4.2 The arithmetic exit and the correct metric conversion — PROVED / REFUTED

On the arithmetic completion \(\ell^2\),
\[
D_{\rm ar}a=(d_ja_j)_j,\quad
\mathcal D(D_{\rm ar})=\{a:\sum |d_j|^2|a_j|^2<\infty\},\quad
D_{\rm ar}=-\tfrac14I+i\operatorname{diag}(-\gamma_j/2).
\tag{4.6}
\]
The imaginary diagonal is self-adjoint on its maximal domain. Therefore
\[
-\big(D_{\rm ar}+D_{\rm ar}^*\big)=\tfrac12I,
\quad L_{\rm ar}=2^{-1/2}I:\ell^2\to\ell^2,
\quad I-C_{t,\rm ar}^*C_{t,\rm ar}=(1-e^{-t/2})I.
\tag{4.7}
\]
The sum in (4.7), initially on the common generator domain, extends to the displayed bounded loss operator. These statements prove the remark at `notes/deninger-cusp/astra-proofs.md:544`. The minimal instantaneous exit space is now infinite dimensional: a scalar output would have loss rank at most one on every finite subspace, whereas (4.7) has rank \(n\) on \(n\) modes. The energy exit has one scalar per instant; the arithmetic exit retains an independent amplitude for each orthogonal mode, each with rate \(1/2\).

**REFUTED:** an instantaneous “conjugation by the exit” formula for the metric. The row \(\ell=(1,1,\ldots)\) is not injective and cannot be inverted. It is not even closable as a densely defined functional on arithmetic \(\ell^2\): the sequence with \(n\) coordinates equal to \(1/n\) tends to zero in \(\ell^2\), but \(\ell a^{(n)}=1\). Thus its formal all-ones matrix is not a bounded loss operator in that completion. The precise replacement is inverse **history synthesis**:
\[
\boxed{\quad G_0=(S^{-1})^*S^{-1}=B^*B,\qquad
Q_0(Sa)=\|a\|_{\ell^2}^2\quad(a\in\mathcal D(S)).\quad}
\tag{4.8}
\]
For a finite family \(S_F:\mathbb C^n\to K_F\), this is \(G_{0,F}=(S_F^{-1})^*S_F^{-1}\); it sends \(e_j\) to the **finite-family** biorthogonal, and its matrix as a linear map in modal coordinates is \(H_F^{-1}\). The global \(G_0e_j=b_j\) uses global biorthogonals, not those finite projections. If an operator formula on a single coordinate Hilbert space is desired, let \(H_S=S^*S\) and \(S=U H_S^{1/2}\) be the polar decomposition. Injectivity and dense range of \(S\) make \(U:\ell^2\to K\) unitary, and
\[
G_0=U H_S^{-1}U^*
\tag{4.9}
\]
as positive self-adjoint operators, with spectral-calculus inverse domains. Neither inverse in (4.8)–(4.9) is bounded.

There is no finite-time rank-one assertion in the energy metric either. On \(K\),
\[
\|f\|_K^2-\|C_tf\|_K^2=\int_0^t|f(s)|^2ds,
\quad
(M_t)_{ij}=\frac{1-e^{t(d_i+\bar d_j)}}{-(d_i+\bar d_j)}.
\tag{4.10}
\]
For \(t>0\) this is positive definite on every finite family of distinct modes: a finite exponential sum vanishing on an interval vanishes identically. Hence the full energy finite-time defect already has infinite rank. Rank one refers to the instantaneous boundary form only, as stressed in `notes/h-theta-1/astra-proofs.md:306–312`.

### 4.3 Classification: the two metric classes must not be conflated — PROVED

For any distinct stable eigenvalues \(d_i\), a positive Hermitian metric with a scalar generator exit must satisfy
\[
N_{ij}=-(d_i+\bar d_j)G_{ij}=c_i\bar c_j,
\qquad c_i\ne0,
\quad\Longrightarrow\quad
G^c_{ij}=\frac{c_i\bar c_j}{-(d_i+\bar d_j)}.
\tag{4.11}
\]
Necessity follows by applying the exit form to eigenvectors; its diagonal forces \(c_i\ne0\). Conversely the functions \(c_ie^{d_iX}\) have precisely this Gram and exit \(c_i\), so the Gram is strictly positive on every finite family and its completion supplies the scalar-exit semigroup. For a coherent infinite rank-one positive loss form, fix one index \(0\), choose \(c_0=\sqrt{N_{00}}\), and put \(c_i=N_{i0}/c_0\); rank-one minors give all entries. This proves the classification directly, agreeing with `notes/h-theta-1/astra-proofs.md:21–34,273–280`.

With \(D_c=\operatorname{diag}(c_i)\), the requested diagonal factorization is, in the \(a^*Ha\) convention,
\[
H^c=D_c^*HD_c,
\qquad H_{ij}=\frac1{-(\bar d_i+d_j)}.
\tag{4.12}
\]
In the first-slot Gram convention it is \(G^c=D_cM\overline{D_c}\). This diagonal congruence class contains **many** metrics on the fixed named modes: the family \(c\) is arbitrary up to one common unimodular factor. Prescribing the individual exit values \(j(e_i)=1\) makes the energy Gram unique; the rank-one condition alone does not. These are algebraic forms and their own observation completions; no bounded extension or equivalence on the original \(K\) follows for arbitrary \(c\).

But this is **not the C3 cone**. Under RH and simplicity the C3 all-time similitude condition forces
\[
G(e_i,e_j)=g_i\delta_{ij},\qquad g_i>0,
\qquad N_{ij}=\tfrac12g_i\delta_{ij}.
\tag{4.13}
\]
To prove it, apply the similitude to a cross entry: its extra factor is \(e^{it(\gamma_j-\gamma_i)/2}\), so distinct-frequency cross entries vanish. Conversely every positive diagonal form works. Its loss rank is the number of represented modes. Therefore **no C3 metric has rank-one generator loss when at least two modes are present**. The energy Cauchy metric and all its nondegenerate diagonal congruences lie outside that cone. In one complex dimension both descriptions reduce to the same ray; that exception does not apply to the Riemann channel.

For comparison the polynomially weighted outgoing metric has, on finite modal sums,
\[
-\langle f',g\rangle_{\delta,c}-\langle f,g'\rangle_{\delta,c}
=f(0)\overline{g(0)}+\int_0^\infty w'_{\delta,c}(X)f(X)\overline{g(X)}dX.
\tag{4.14}
\]
For \(\delta>0\) there is a positive bulk term as well as the boundary exit. In modal entries it is \(s_{ij}F_{\delta,c}(s_{ij})\), \(s_{ij}=-(d_i+\bar d_j)\). It is neither the energy all-ones loss nor the arithmetic \(I/2\). This is another direct way to distinguish all three metrics.

## 5. W5: the dictionary and the remaining problem — SHARPENED / OPEN

Author: `codex:gpt-6-astra`

| Structure | Energy model | Arithmetic unit-coefficient model | Connes's weighted realization |
|---|---|---|---|
| Hilbert space or domain | \(K\subset L^2(X>0,dX)\) | Closed form on \(\mathcal D(B)\subset K\); its own completion is \(\ell^2\) | \(H_\delta=L^2((1+X^2/4)^{\delta/2}dX)\), its theta-image quotient, and dual annihilator \(\mathcal N_\delta\subset H_{-\delta}\) |
| Named modes | Cut, exponentially damped characters and all jets | The same ordinary named modes made orthonormal, assuming RH and simplicity | Uncut critical characters/jets in the weighted dual; distinct from restricting \(H_\delta\)'s norm to cut modes |
| Modal Gram | Cauchy \(M_{ij}=2/(1+i(\gamma_i-\gamma_j))\) under RH | Identity | On cut modes, \(F_{\delta,2}(1/2+i(\gamma_i-\gamma_j)/2)\), with constant diagonal and nonzero cross entries |
| Instantaneous loss | One scalar boundary trace \(j(f)=f(0)\); modal loss all ones | \(I/2\), with minimal exit space \(\ell^2\) | The outgoing weighted restriction has boundary plus bulk loss (4.14); the original cokernel carries weighted translations |
| Time evolution | \(C_t\), a contraction in energy | \(e^{-t/4}\) times a unitary group in the arithmetic completion | Polynomially bounded, generally nonunitary translation representation |
| Comparison | Modes are complete/minimal, with neither uniform Riesz bound under RH and simplicity | Neither norm inequality with energy; representing \(G_0\) is unbounded and has no positive lower bound | No fixed polynomial weight is equivalent to \(Q_0\); bounded cut-and-damp maps its dual to energy, not continuously to arithmetic \(\ell^2\) |
| Multiplicity | Every actual jet, unconditionally | Nontrivial retained Jordan blocks obstruct positive similitude | At each critical zero retain precisely \(r<m_\gamma\), \(r<(\delta-1)/2\) |

**PROVED conclusion.** These are three different constructions. In particular, varying \(\delta\) controls the admissibility of **uncut dual jets at infinity**. It does not determine which cut-and-damped jets have a finite outgoing polynomial norm: all of them do. The inequivalence is already visible on finite sums, and (3.14) separates the infinite domains.

**SHARPENED interpretation for Deninger's programme.** If “positive Hodge metric” means a positive metric with the C3 conformal evolution, its required form is diagonal in the simple critical mode coordinates. With the particular normalized cup pairing and star of `notes/deninger-bond/astra-proofs.md:219–230`, it is specifically \(Q_0\). If that cup normalization is not fixed independently, the larger positive diagonal family remains; a trace formula does not select its weights (`:347–370`). Neither the energy metric nor Connes's polynomial norm satisfies this conformal metric requirement. Connes supplies a spectral cokernel topology, not this positive Hodge metric.

**OPEN task, stated without a false identification.** Give a construction from theta/adelic/geometric data, without listing the zero divisor or choosing its modal coordinates, of a densely defined closed operator or positive closed form on the actual outgoing model whose graph domain is exactly (1.4), whose pairing restricts to the specified cup-compatible unit form, and whose evolution obeys (1.8). A sufficient construction must prove the finite modal span is its graph core, or otherwise identify the minimal closure; merely showing coefficient square-summability, completeness, or polynomial Sobolev membership does not do this. Equating the minimal and maximal coefficient domains is not supplied by the present argument. The weighted cokernel does not solve this task: its cut-and-damp image even contains vectors outside (1.4). Establishing a positive geometric model independently of the RH/simplicity assumptions, and a canonical cup normalization if not stipulated, remains additional work. None of the conditional constructions proves RH or simplicity.

## 6. Numerical checks for the blind lane — PROVED identities; finite numerical verification

Author: `codex:gpt-6-astra`

Run `python3 notes/connes-weighted-metric/checks/check_metrics.py`; add `--matrices` to print every entry of all five \(10\times10\) Grams. The script computes the first ten positive zeros independently with 65-digit mpmath; `data/zeros3000.npy` is used only for the separate truncated-product check and contains positive ordinates. The matrices below use **ten positive modes**, not ten conjugate pairs. All decimals are rounded numerical evaluations, not interval certificates or assertions about the remaining zeros.

### 6.1 Biorthogonals: the factor \(\sqrt2\), and the product tail

At a simple zero, direct differentiation gives an independently evaluable formula
\[
\Theta'(w_\rho)=\frac{2i\xi'(\rho)}{\xi(2-\rho)},\qquad
\xi'(\rho)=\frac{\rho(\rho-1)}2\pi^{-\rho/2}\Gamma(\rho/2)\zeta'(\rho).
\tag{6.1}
\]
The script checks this against direct differentiation of the quotient defining \(\Theta\) to relative error below \(10^{-50}\). Numerical integration of the boundary pole norm gives \(\|k_{a+i/4}\|^2=2\), independently checking the factor in (1.2).

| \(j\) | \(\gamma_j\) | \(1/\lvert\Theta'(w_j)\rvert\) | \(\lVert b_j\rVert\) |
|---:|---:|---:|---:|
| 1 | 14.134725141734694 | 0.517139665394 | 0.731345928441 |
| 2 | 21.022039638771555 | 0.535360188984 | 0.757113640016 |
| 3 | 25.010857580145689 | 0.542267810764 | 0.766882492420 |
| 4 | 30.424876125859513 | 0.571011595037 | 0.807532341974 |
| 5 | 32.935061587739190 | 0.575803235049 | 0.814308744264 |
| 6 | 37.586178158825671 | 0.565315299070 | 0.799476562962 |
| 7 | 40.918719012147495 | 0.597084195817 | 0.844404567603 |
| 8 | 43.327073280915000 | 0.590475317272 | 0.835058201932 |
| 9 | 48.005150881167160 | 0.631215136035 | 0.892673006155 |
| 10 | 49.773832477672302 | 0.643292558677 | 0.909753061054 |

Every ratio of the last column to the preceding column is \(\sqrt2=1.414213562373\). These small initial norms need not be monotone. Formula (1.12), not this short table, proves unboundedness.

For the 3000 supplied positive ordinates **and their negatives**, the truncated product (1.11) gives \(0.731104461804\) at the first zero and \(0.909452640385\) at the tenth, both below the analytic values as required by the omitted factors being greater than one. The script prints all ten such comparisons. Their discrepancy is an omitted infinite tail, not a failure of (1.11); float64 data and that tail are not certified here. Equations (1.11)–(1.13) are the formulas for a lane wishing to enclose it.

### 6.2 The first-ten weighted Grams

The full matrices are explicitly specified by the ordinate table and
\[
s_{ij}=\frac12+\frac i2(\gamma_i-\gamma_j),\qquad
M^0_{ij}=s_{ij}^{-1},\quad
M^{1,c}_{ij}=F_{1,c}(s_{ij}),\quad
M^{2,c}_{ij}=s_{ij}^{-1}+\frac{2}{c^2s_{ij}^3}.
\tag{6.2}
\]
Use (2.8) or (2.9) for \(F_{1,c}\); the independent check uses oscillatory real quadrature. Normalized Grams are \(R^{\delta,c}=M^{\delta,c}/N_{\delta,c}\).

| \(\delta\) | \(c\) | Common diagonal \(N\) | \(\lambda_{\min}(M)\) | \(\lambda_{\max}(M)\) | \(\lambda_{\min}(R)\) | \(\lambda_{\max}(R)\) |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | either | 2.000000000000 | 0.799194120242 | 3.732838955670 | 0.399597060121 | 1.866419477835 |
| 1 | 1 | 4.786675510395 | 3.286682737088 | 6.287319610746 | 0.686631615189 | 1.313504455669 |
| 2 | 1 | 18.000000000000 | 16.061270131928 | 19.648651607487 | 0.892292785107 | 1.091591755971 |
| 1 | 2 | 3.077724569750 | 1.826820947857 | 4.697353403705 | 0.593562193905 | 1.526242292723 |
| 2 | 2 | 6.000000000000 | 4.761685465249 | 7.460857405104 | 0.793614244208 | 1.243476234184 |

The exact transport is \(c=2\); \(c=1\) records the brief's alternative convention. The value \(\delta=1\) is a valid norm check, but lies at the excluded endpoint of Connes's \(\delta>1\) cokernel theorem. Useful complex-entry sign checks are

| Gram | \(M_{1,2}\) | \(M_{1,10}\) |
|---|---|---|
| Unweighted | \(0.041292367714+0.284393522777i\) | \(0.001573383423+0.056073980690i\) |
| \(\delta=1,c=2\) | \(0.038405823133+0.278758425428i\) | \(0.001569659206+0.056029902200i\) |
| \(\delta=2,c=2\) | \(0.036318000719+0.273620056689i\) | \(0.001565964607+0.055986032445i\) |

Conjugate the entries when transposing to the \(a^*Ha\) convention. Quadrature, (2.8), and the even-weight rational formula agree to \(10^{-9}\) in the tested entries; the 35-term \(U\)-series at \((\delta,c,s)=(1,2,1/2)\) differs from direct high-precision quadrature by \(6.63\times10^{-14}\).

For an independent large-separation diagnostic, at \(\tau=100\), the values of \(|\tau F_{\delta,c}(1/2+i\tau)|\) for \((\delta,c)=(1,1),(1,2),(2,2)\) are respectively \(0.999887479\), \(0.999962501\), \(0.999937505\). The corresponding \(\tau^2|sF(s)-1|\) are \(1.000275422\), \(0.250012505\), \(0.499987500\), approaching \(\delta/c^2\) as (2.11) requires. These numbers refute a claimed \(1/|\tau|^{1+\delta}\) leading tail even before the endpoint proof. Good conditioning in this finite table does not contradict (2.13)–(2.14).

### 6.3 The all-ones loss versus \(I/2\)

With \(d_j=-1/4-i\gamma_j/2\) and the **unnormalized physical** modes in (0.2), form
\[
N^E_{ij}=-(d_i+\bar d_j)M^0_{ij}=1,\qquad
N^{\rm ar}_{ij}=-(d_i+\bar d_j)\delta_{ij}=\tfrac12\delta_{ij}.
\tag{6.3}
\]
The maximum residuals were \(2.23\times10^{-16}\) and zero. The exact coefficient-matrix eigenvalues are \((10,0,\ldots,0)\) and \((1/2,\ldots,1/2)\). Roundoff zero eigenvalues in the first matrix were at most \(1.75\times10^{-15}\) in magnitude. These are Euclidean eigenvalues of the **coordinate form matrices**, not spectral eigenvalues of a bounded instantaneous energy-loss operator on \(K\).

At \(t=1\), the energy coordinate defect matrix \((1-e^{-s_{ij}})/s_{ij}\) has computed extreme eigenvalues approximately \(2.93275\times10^{-11}\) and \(2.96525269\); positivity and full finite rank are already proved in (4.10). The arithmetic defect is exactly \((1-e^{-1/2})I\), with eigenvalue \(0.3934693402873666\). The near-zero energy eigenvalue is a finite conditioning diagnostic, not a certified spectral enclosure.

For synthetic falsification tests independent of actual zero data: let two ordinates coalesce in (2.13); let arbitrarily many distinct ordinates lie in a fixed tiny interval in (2.14); and retain a full jet of order one in the C3 similitude test. These respectively force the lower Gram eigenvalue to zero, an upper Gram eigenvalue to infinity, and polynomial growth incompatible with a positive conformal metric. Actual zero counting supplies the first two configurations under RH and simplicity; the synthetic double-zero test does not assert that zeta has such a zero.

## 7. Corrections to the brief

Author: `codex:gpt-6-astra`

| ID | Verdict | Correction |
|---|---|---|
| C1 / unit form | SHARPENED | The exact closed form has the minimal graph domain (1.4); ordinary modal series convergence and equality with the maximal coefficient domain are not consequences of completeness/minimality. |
| C2 / representing operator | PROVED | \(G_0e_\rho=b_\rho\), with \(b_\rho=\Theta'(w_\rho)^{-1}\mathcal C_\Theta k_\rho\) and \(\lVert b_\rho\rVert^2=2/\lvert\Theta'(w_\rho)\rvert^2\) at height \(1/4\). |
| C3 / spacing | REFUTED | A nearest gap supplies a sharp factor lower bound, but no uniform nearest-gap-only upper bound; the full local product matters. |
| C4 / transported weight | SHARPENED | Exact notebook transport gives \((1+X^2/4)^{\delta/2}\); replacing it by \((1+X^2)^{\delta/2}\) is equivalence, not literal equality. |
| C5 / Fourier decay | REFUTED | The cut at zero leaves a jump, so the weighted modal Gram has the same leading inverse-gap tail as energy. |
| C6 / Schur threshold | REFUTED | No fixed \(\delta\) gives an upper or lower \(\ell^2\) Gram bound; arbitrarily large local clusters preclude the upper bound. |
| C7 / metric identification | REFUTED | Neither norm inequality with \(Q_0\) holds on finite mode sums; taking closures cannot repair that. |
| C8 / cokernel vectors | SHARPENED | The dual contains uncut unitary characters and admitted polynomial jets; the cokernel's \(H_\delta\) orthogonal representatives include a reciprocal weight. |
| C9 / half-density | SHARPENED | The \(-1/2\) power belongs to additive \(dr\) normalization and disappears on conversion to multiplicative Haar measure; it must not remain in logarithmic dual characters. |
| C10 / comparison map | PROVED / REFUTED | Cut-and-damp is bounded from the weighted dual to energy and is injective on the annihilator; it is synthesis, not the inverse of kernel evaluation. |
| C11 / domains | PROVED | Some cut-and-damp images lie in every polynomially weighted outgoing space but outside \(\mathcal D(Q_0)\). |
| C12 / jet threshold | SHARPENED | The jet degree is \(r<(\delta-1)/2\), and the multiplicity count is \(n<(1+\delta)/2\); the first derivative requires \(\delta>3\), strictly. All cut-and-damped model jets have every finite polynomial norm. |
| C13 / source typo | PROVED | Connes's line 4100 needs \(2k-\delta<-1\), not its printed \(2k+\delta<-1\); the integral and final threshold in the source give the correct sign. |
| C14 / exits | SHARPENED | Instantaneous energy exit is scalar; both energy and arithmetic finite-time defects have infinite rank. Arithmetic instantaneous loss is \(I/2\). |
| C15 / conjugating by exit | REFUTED | The summation row is noninvertible and nonclosable on arithmetic \(\ell^2\); \(G_0\) is built from the inverse of the closed observation-history synthesis. |
| C16 / metric cones | REFUTED | Scalar-exit Cauchy congruences form a family of metrics, but none belongs to the C3 similitude cone in dimension greater than one. |
| C17 / meaning of unitary | SHARPENED | The rescaled flow is a unitary group on the arithmetic completion; only forward invariance of the form domain inside energy has been proved. |
| C18 / missing construction | OPEN | A zero-free, cup-compatible construction identifying the minimal graph domain remains missing; Connes's polynomial topology does not supply it. |

## 8. What this changes in the notebook

Author: `codex:gpt-6-astra`

| Claim | Status to register | One-sentence statement |
|---|---|---|
| W1 | SHARPENED | Unit modal weights define the positive closed form (1.4), represented by \(G_0e_\rho=b_\rho\), whose exact Blaschke-product norms see all neighbouring zeros. |
| W2 | REFUTED / PROVED replacement | Connes's transported polynomial norm has neither uniform Riesz bound and is not equivalent to the arithmetic form for any fixed exponent. |
| W3 | SHARPENED | Cut-and-damp is a bounded injective comparison of the weighted annihilator with the admitted model jets, not evaluation inversion or arithmetic-domain identification. |
| W4 | SHARPENED | The energy loss is one scalar boundary output, the arithmetic loss is \(I/2\), and scalar-exit Cauchy metrics belong to a different class from C3. |
| W5 | OPEN after refutation | The required Hodge metric is the diagonal arithmetic form once its cup normalization is fixed; an intrinsic zero-free realization of its graph domain is still missing. |

All W1–W5 sections, the correction ledger, and numerical checks are complete. Only this note, the mandated one-line progress record, and the Python check in this lane were authored; no other notebook file was edited.
