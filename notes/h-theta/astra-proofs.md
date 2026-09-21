# H-THETA: proof ledger and corrections

Author: codex:gpt-6-astra  
Brief: H-THETA, notes/h-theta/astra-brief.md and the supplied research brief  
Date: 2026-09-21

The literal cyclic-space construction fails. There are stronger corrections than the brief anticipates: the outgoing half of the Gaussian theta vector is outer; Burnol's bad-zero defect is not his scattering model space; and ordinary kernels do not account for multiple zeros. No RH or simplicity assumption is made unless stated.

Source identifiers below mean files under refs/src/. Line numbers refer to the checked local TeX files. Short text in quotation marks attached to a citation is a verbatim source snippet (with line-break whitespace suppressed). General analytic tools used are Fourier–Plancherel, Hardy factorization, and Hadamard factorization. The nontrivial applications are supplied below. Burnol math/0001013/main.tex was read in full. An external primary source is identified explicitly in T5(b), because the repository contains only bibliographic references to Lax–Phillips 1976.

**Conventions checked.** Put \(X=\log y\), reserving \(x=\sqrt y\) for the real idele coordinate. Then

\[
 \widehat f(\tau)=\int_{\mathbb R}f(e^X)e^{i\tau X}\,dX,
 \qquad f(e^X)=\frac1{2\pi}\int_{\mathbb R}\widehat f(u)e^{-iuX}\,du.
\]

The measures are \(dX=dy/y\) and \(du/(2\pi)\). Thus \(y>1\) corresponds to \(H^2(\mathbb C_+)\), and \(U_t\) is multiplication by \(e^{it\tau}\). The brief's outgoing sign is correct and agrees with report/sections/04h_rebound_state.tex:25–40, which calls the **adjoint** compression “the backward translation”. With our boundary measure the inverse transform of \(k_w=(\tau-\bar w)^{-1}\) is \(-i e^{-i\bar wX}1_{X>0}\); the factor \(-i\sqrt{2\pi}\) at that source's line 32 uses boundary measure \(du\). We use \(Z_t=P_KU_t|_K\), \(C_t=Z_t^*\), and inner products linear in the first variable. Also \(JU_tJ=U_{-t}\) and \(\widehat{Jf}(\tau)=\widehat f(-\tau)\).

## T1. Weight, symmetry, membership

### T1(a)

**Statement.** \(\phi(1/y)=y^{1/2}\phi(y)\).

**Proof.** Poisson summation gives

\[
 \phi(1/y)=y^{1/2}\theta(y)-1-y^{1/2}
            =y^{1/2}\bigl(\theta(y)-1-y^{-1/2}\bigr).
\]

Thus “odd” is a proposed arithmetic grading, not oddness under inversion. The weighted vector in T1(b) is inversion-even.

**Status: PROVED.**

### T1(b)

**Statement.** \(y^a\phi(y)\in H\) exactly when \(0<a<1/2\); \(g=y^{1/4}\phi\) is the unique inversion-invariant member among these weights.

**Proof.** The defining series and T1(a) give

\[
 \phi(y)=-y^{-1/2}+O(e^{-\pi y})\quad(y\to\infty),\qquad
 \phi(y)=-1+O(y^{-1/2}e^{-\pi/y})\quad(y\downarrow0).
\]

The squared norm at zero has the same convergence as \(\int_0^1y^{2a-1}dy\), and at infinity as \(\int_1^\infty y^{2a-2}dy\). Both endpoints are excluded. Moreover

\[
 J(y^a\phi)(y)=y^{1/2-a}\phi(y).
\]

Since \(\phi\) is nonzero for large \(y\), equality with \(y^a\phi\) forces \(a=1/4\). In logarithmic coordinates \(g(e^X)\) is real, even, smooth, and asymptotic to \(-e^{-|X|/4}\).

**Status: PROVED.**

### T1(c)

**Statement.** Burnol's subtracted \(E\), not Connes's unsubtracted Gaussian sum, gives \(g\).

**Proof and normalization.** For \(f=e^{-\pi t^2}\otimes1_{\widehat{\mathbb Z}}\), the adelic additive integral is \(1\). On the positive real representative of the trivial compact-character sector,

\[
 E_B(f)(x)=x^{1/2}\sum_{n\ne0}e^{-\pi n^2x^2}-x^{-1/2}
          =g(x^2).
\]

This is exactly math/0001013:main.tex:204–207, whose defining subtraction is “- {\int_{\Aa_K} \varphi(x)\, dx \over \sqrt{|v|}}”. The Gaussian does not satisfy \(f(0)=\widehat f(0)=0\). Connes's formula, math/9811068:main.tex:773–777, is “\vert g \vert^{1/2} \sum_{q\in k^*} f(qg)” on his prescribed domain. Applied formally to this Gaussian without subtraction it is not the claimed \(L^2\) vector.

Pointwise \(x^{1/2}=y^{1/4}\). There is also a Hilbert-space normalization: since \(dy/y=2dx/x\), the unitary coordinate change is

\[
 (Wh)(y)=2^{-1/2}h(\sqrt y),\qquad WE_B(f)=2^{-1/2}g.
\]

For the Euclidean normalization \(E_0(f)(x)=\sum_{n\ge1}f(nx)-x^{-1}\int_0^\infty f\), one has \(E_B(f)=2\sqrt{x}\,E_0(f)\). The unitary map \(R:L^2(dx)\to H\) is

\[
 (Rf)(y)=2^{-1/2}y^{1/4}f(\sqrt y),\qquad RE_0(e^{-\pi x^2})=g/(2\sqrt2).
\]

The Euclidean definition is math/0001013:main.tex:464–480, beginning “We describe one more variation.”

**Status: PROVED.**

## T2. Mellin transforms, halves, and symbol

### T2(a)

**Statement.** On \(|\Im\tau|<1/4\), and then meromorphically,

\[
 \widehat g(\tau)=\Lambda(1/2+2i\tau)
   =-\frac{\xi_{\rm crit}(\tau)}{\tau^2+1/16}.
\]

It is even and real on the real axis. Its poles and residues are

\[
 \operatorname{Res}_{\tau=i/4}\widehat g=i\quad(s=0),\qquad
 \operatorname{Res}_{\tau=-i/4}\widehat g=-i\quad(s=1).
\]

Its zeros, with multiplicity, are \(a_\rho=\gamma/2-i(\sigma-1/2)/2\). **All** these zeros are real iff RH.

**Proof.** Substitute \(s=1/2+2i\tau\) in the Mellin identity. For completeness, set

\[
 A(s)=\int_1^\infty(\theta(y)-1)y^{s/2}\,\frac{dy}{y}.
\]

This is entire by exponential decay. Splitting at \(1\) and using Poisson gives

\[
 \int_0^\infty\phi(y)y^{s/2}\frac{dy}{y}
 =A(s)+A(1-s)+\frac2{s-1}-\frac2s=\Lambda(s),\quad0<\Re s<1.
\]

The last equality follows initially by termwise integration of \(\theta-1\) for \(\Re s>1\), followed by the same split and continuation. This also re-proves B4 rather than relying on its notation for the half-completed function. Now \(s(s-1)=-4(\tau^2+1/16)\), and the residue change divides by \(2i\).

The requested pure power-times-exponential asymptotic is false: the zeta factor oscillates and has real zeros. The correct Stirling statement is

\[
 |\widehat g(u)|=
 2\sqrt2\,\pi^{1/4}|u|^{-1/4}e^{-\pi|u|/2}
 |\zeta(1/2+2iu)|\bigl(1+O(|u|^{-1})\bigr).
\]

This means an asymptotic for the gamma prefactor; it remains an equality with a bounded relative error multiplying that prefactor at zeta zeros. An elementary bound is

\[
 |\widehat g(u)|\le C(1+|u|)^{1/4}e^{-\pi|u|/2}.
\]

Indeed Euler summation with cutoff \(N\asymp1+|t|\) bounds the finite Dirichlet sum at \(1/2+it\) by \(O(\sqrt N)\), its integral term by \(O(\sqrt N/(1+|t|))\), and its remainder by \(O((1+|t|)/\sqrt N)\). Thus \(\zeta(1/2+it)=O((1+|t|)^{1/2})\), which suffices. In particular

\[
 \widehat g(0)=-16\xi(1/2)=-7.9539324510130257586\ldots.
\]

**Status: PROVED** for the corrected statement; the fixed-\(C,c\) asymptotic in the brief is refuted.

### T2(b)

**Statement.** The two half transforms are

\[
 \Lambda_>(s)=\frac2{s-1}+A(s),\qquad
 \Lambda_<(s)=-\frac2s+A(1-s)=\Lambda_>(1-s).
\]

Their integral domains are respectively \(\Re s<1\) and \(\Re s>0\). Therefore

\[
 \widehat g_>(\tau)=\Lambda_>(1/2+2i\tau)\in H^2(\mathbb C_+),\qquad
 \widehat g_<(\tau)=\widehat g_>(-\tau)\in H^2(\mathbb C_-).
\]

The first is holomorphic on \(\Im\tau>-1/4\); its meromorphic extension has a pole at \(-i/4\), on the boundary of that larger half-plane. The second has the reflected properties. Their sum is \(\widehat g\).

**Proof of decay and logarithmic claims.** Put \(h(X)=g(e^X)\) for \(X\ge0\). Every derivative of \(h\) is integrable on this half-line. Integration by parts twice gives

\[
 \widehat g_>(u)=-\frac{h(0)}{iu}+O(|u|^{-2}),\qquad
 |\widehat g_>(u)|\sim\frac{2-\theta(1)}{|u|}.
\]

Here \(h(0)=\theta(1)-2=-0.91356518878669\ldots\ne0\). Local logarithmic singularities at isolated zeros of an analytic function are integrable; T3(c) will in fact exclude all real zeros of this half transform. The asymptotic therefore proves

\[
 \int_{\mathbb R}\frac{|\log|\widehat g_>(u)||}{1+u^2}\,du<\infty.
\]

In contrast T2(a) gives, for large \(|u|\),

\[
 \log|\widehat g(u)|\le-\frac\pi2|u|+O(\log(2+|u|)).
\]

Its positive part is integrable against \((1+u^2)^{-1}du\), but its negative part has infinite integral. Hence its logarithmic integral is \(-\infty\), not a finite \(L^1\) integral. The incomplete-gamma expression, useful for independent checks, is

\[
 A(s)=2\sum_{n\ge1}(\pi n^2)^{-s/2}\Gamma(s/2,\pi n^2).
\]

The \(1/|u|\) tail comes from the endpoint \(X=0\); it cannot be replaced by the exponential tail of the complete gamma factor.

**Status: PROVED.**

### T2(c)

**Statement.** With \(r(\tau)=(\tau-i/2)/(\tau+i/2)\),

\[
 \Theta(\tau)=\frac{\xi(1+2i\tau)}{\xi(1-2i\tau)}
 =\frac{\Lambda(1+2i\tau)}{\Lambda(2i\tau)}r(\tau)
 =\frac{\widehat g(\tau-i/4)}{\widehat g(\tau+i/4)}r(\tau).
\]

These are meromorphic identities, including removable values. On the real line the pole-over-pole quotient at \(0\) is interpreted by continuation; it is \(-1\), while \(r(0)=-1\) and \(\Theta(0)=1\). Also

\[
 E(\tau)=\xi(1-2i\tau)=\xi(2i\tau)=\xi_{\rm crit}(\tau+i/4),\qquad
 E^\#(\tau)=\xi(1+2i\tau)=\xi_{\rm crit}(\tau-i/4).
\]

**Proof of quotient and unconditional innerness.** Insert \(\Lambda(s)=4\xi(s)/(s(s-1))\) and \(\xi(2i\tau)=\xi(1-2i\tau)\). Here is a product proof of innerness, avoiding an unproved Phragmén–Lindelöf step. Zeros of \(\xi\) are counted with multiplicity. Its order-one Hadamard factorization can be grouped in conjugate pairs:

\[
 \xi(s)=e^{a+bs}P(s),\qquad
 P(s)=\prod_{\substack{\xi(\rho)=0\\\Im\rho>0}}
       (1-s/\rho)(1-s/\bar\rho).
\]

This product converges locally uniformly: \(0<\Re\rho<1\), and each paired factor differs from \(1\) by \(O_R(|\rho|^{-2})\) on \(|s|\le R\); the sum converges by the order-at-most-one zero bound. To check the growth input, multiply the splitting formula in T2(a) by \(s(s-1)/4\). On \(|s|\le R\), the two entire integrals are bounded by a constant times
\(\int_1^\infty e^{-\pi y}y^{(R+1)/2}\,dy/y\).
The rational terms become a polynomial. Stirling therefore gives \(\max_{|s|\le R}|\xi(s)|\le\exp(O(R\log(R+2)))\), sufficient for the indicated Hadamard factorization. Pairing upper zeros also by \(\rho\mapsto1-\bar\rho\) gives the absolutely convergent identity

\[
 \frac{P'(1/2)}{P(1/2)}
 =-\sum_{\Im\rho>0}\frac{2(\Re\rho-1/2)}{|\rho-1/2|^2}=0.
\]

Since \(\xi'(1/2)=0\), \(b=0\); since \(\xi(0)=1/2\), \(e^a=1/2\). Write \(\rho=\sigma+i\gamma\), \(\gamma>0\), and set

\[
 v_{\rho,-}=-\gamma/2+i\sigma/2,\qquad
 v_{\rho,+}=\gamma/2+i\sigma/2.
\]

Using \(\Theta(\tau)=\xi(-2i\tau)/\xi(2i\tau)\), the paired product becomes

\[
 \Theta(\tau)=\prod_{\Im\rho>0}
 \frac{(\tau-v_{\rho,-})(\tau-v_{\rho,+})}
      {(\tau-\bar v_{\rho,-})(\tau-\bar v_{\rho,+})}.
\]

Each factor has modulus at most \(1\) in \(\mathbb C_+\) and modulus \(1\) on \(\mathbb R\); the product is locally uniform there. It is nonconstant, so the maximum principle makes the inequality strict in \(\mathbb C_+\). Its zero set is equivalently

\[
 w_\rho=\gamma/2+i(1-\sigma)/2,
\]

by the functional-equation symmetry. The denominator \(E\) has no zeros in the closed upper half-plane. Thus \(E\) is Hermite–Biehler unconditionally.

With the de Branges norm normalized as \(\|F\|_E^2=\int|F(u)/E(u)|^2du/(2\pi)\), \(F\mapsto F/E\) is unitary onto \(K_\Theta\). Indeed the de Branges conditions are \(F/E,F^\#/E\in H^2_+\), and on the boundary \(F^\#/E=\Theta\overline{F/E}\). Hardy orthogonal decomposition identifies this condition with \(F/E\in H^2_+\ominus\Theta H^2_+\). Conversely these two Hardy functions glue \(Eh\) across the real axis to an entire function, giving surjectivity. The customary norm with \(du\) requires the corresponding factor \(\sqrt{2\pi}\).

The unshifted real entire function \(\xi_{\rm crit}\) is **never** Hermite–Biehler: it equals its own \(\#\)-transform. A correct RH equivalent is that \(\xi_{\rm crit}(\tau+ih)\) is Hermite–Biehler for **every** \(h>0\). Under RH this follows by pairing its real zeros; conversely zero-freeness in \(\mathbb C_+\) for every \(h>0\), and conjugation symmetry, force all zeros of \(\xi_{\rm crit}\) to be real.

The edge transforms are continuations of the Mellin transforms of \(y^{1/2}\phi\) and \(\phi\). The full ordinary integrals on those edge lines do not converge, even conditionally as one-sided improper integrals: their nondecaying logarithmic-coordinate tails are constants times \(e^{i\tau X}\).

**Status: PROVED.**

### T2(d)

**Statement.** \(\Theta\) is a pure Blaschke product, up to its normalization \(\Theta(0)=1\). It has no singular inner factor, including no positive delay factor.

**Proof.** The product just obtained is already a convergent Blaschke product: its zeros satisfy

\[
 \sum_\rho\frac{\Im w_\rho}{1+|w_\rho|^2}<\infty.
\]

Each conjugate-paired factor is normalized to \(1\) at \(0\), and the exact product equals \(\Theta\), leaving no additional factor. Independently, meromorphic continuation and nonvanishing across every finite real point exclude boundary singular measure. The remaining possible factor \(e^{ia\tau}\), \(a\ge0\), is excluded by

\[
 \Theta(iv)=\frac{\xi(2v)}{\xi(1+2v)}
 =\frac{2v-1}{2v+1}\sqrt\pi\,
   \frac{\Gamma(v)}{\Gamma(v+1/2)}
   \frac{\zeta(2v)}{\zeta(2v+1)}
 \sim\sqrt{\pi/v}\quad(v\to\infty).
\]

An inner factor \(e^{ia\tau}\) would force \(|\Theta(iv)|\le e^{-av}\), so \(a=0\). No Cartwright hypothesis is used: \(E(iv)=\xi(1+2v)\) has gamma growth and is not of exponential type.

**Status: PROVED.**

## T3. What the Gaussian theta vector generates

### T3(a)

**Statement.** The full dilation orbit of \(g\) spans \(H\).

**Proof.** If \(h\perp U_tg\) for every real \(t\), the Fourier transform of the \(L^1\) function \(\widehat g\,\overline{\widehat h}\) vanishes identically. Fourier uniqueness gives \(\widehat g\,\overline{\widehat h}=0\) almost everywhere. Since the real zeros of the nonzero analytic function \(\widehat g\) are discrete, \(h=0\).

This is a statement about the single Gaussian in the units-invariant sector, proved here. It is compatible with, but not a direct consequence of, Connes's statement math/9811068:main.tex:2549–2554, “defines a surjective isometry”, at \(\delta=0\), or Burnol's density lemma math/0001013:main.tex:218–223, “and is dense in it.” Those theorems concern the range of \(E\), not the orbit of one Gaussian. The unweighted completed bond contains no nonzero cokernel recording pointwise spectral zeros.

**Status: PROVED.**

### T3(b)

**Statement.** Even the forward orbit of \(g\) spans \(H\).

**Proof.** For \(h\in H\), the function

\[
 F(z)=\frac1{2\pi}\int_{\mathbb R}
       \widehat g(u)\overline{\widehat h(u)}e^{izu}\,du
\]

is holomorphic on \(|\Im z|<\pi/2\). T2(a), Cauchy–Schwarz, and its exponential bound justify absolute convergence and differentiation on compact substrips. If \(h\) is orthogonal to the forward orbit, \(F(t)=0\) for all \(t\ge0\). The identity theorem gives \(F=0\), and Fourier uniqueness gives \(h=0\), as above.

This also explains the Hardy obstruction in the brief: a nonzero \(H^2\) function has an absolutely integrable boundary logarithm with weight \((1+u^2)^{-1}\). Map the half-plane to the disk, apply Jensen's inequality to bound the negative logarithmic integral and the \(H^2\) bound to its positive part, and include the outer coordinate factor. Thus no simply invariant space \(qH^2_+\), \(|q|=1\), contains \(\widehat g\). The direct argument above avoids needing a classification of invariant subspaces of all of \(L^2\).

Compression to this orbit closure is just \(U_t\), a unitary group with absolutely continuous generator spectrum, not the Riemann contraction. If one then removes \(H_+=L^2(y>1)\), the compression to \(H_-=L^2(y<1)\), after inversion, is the full backward shift \(f(X)\mapsto f(X+t)\) on \(L^2(0,\infty)\). Contrary to the brief, it has eigenvectors \(e^{-aX}\) for **every** \(\Re a>0\), with eigenvalues \(e^{-at}\). These are not isolated zeta resonances. Keeping \(H_+\) instead gives the isometric forward shift. Neither is the proper model space \(K_\Theta\).

For a direct operator distinction, both \(C_t\) and \(Z_t\) on \(K_\Theta\) have strictly decaying eigenvectors: respectively \(k_w\) and \(\Theta(\tau)/(\tau-w)\), with eigenvalues \(e^{-it\bar w}\) and \(e^{itw}\). The latter identity follows by subtracting \(e^{itw}\) and observing that \((e^{it\tau}-e^{itw})/(\tau-w)\in H^2_+\). Thus neither operator is an isometry or coisometry, whereas the full forward/backward shifts are respectively an isometry/coisometry.

**Status: PROVED** for forward cyclicity and inequivalence; the brief's “no resonances” description of the backward shift is replaced by its explicit spectrum.

### T3(c)

**Statement, stronger than requested.** \(\widehat g_>\) is outer. In particular \(B_>=1\ne\Theta\) and \(K_{B_>}=\{0\}\). In fact \(\Lambda_>(s)\ne0\) throughout \(\Re s<1\).

**Proof.** For \(X\ge0\), set

\[
 r_0(X)=e^{X/2}\bigl(\theta(e^X)-1\bigr),\qquad p(X)=1-r_0(X).
\]

Every summand \(2e^{X/2}e^{-\pi n^2e^X}\) in \(r_0\) is strictly decreasing; \(r_0(\infty)=0\). Also

\[
 r_0(0)=\theta(1)-1
 \le\frac{2e^{-\pi}}{1-e^{-3\pi}}<\frac12,
 \qquad p(0)=2-\theta(1)>\frac12.
\]

Thus \(p'\ge0\) and \(\int_0^\infty p'=r_0(0)\). For \(z=(1-s)/2\), \(\Re z>0\), integration by parts yields

\[
 \Lambda_>(s)=-\int_0^\infty p(X)e^{-zX}\,dX,\qquad
 -z\Lambda_>(s)=p(0)+\int_0^\infty p'(X)e^{-zX}\,dX.
\]

The real part of the expression on the right is at least

\[
 p(0)-r_0(0)=3-2\theta(1)>0.
\]

This proves the zero-free assertion. In particular \(\widehat g_>\) has no zeros on or above the real axis. Its continuation through the real axis excludes any finite singular inner factor. A factor \(e^{ia\tau}\), \(a>0\), would force its inverse transform to vanish on \(0<X<a\); but \(g(e^X)\ne0\) arbitrarily near \(0\). Hence its inner factor is constant. Hardy factorization and Beurling–Lax now give

\[
 \overline{\operatorname{span}}\{U_tg_>:t\ge0\}=H_+.
\]

For orientation, the Hardy upper half-plane corresponds to \(\Re s<1/2\), not \(\Re s<1\); the latter is the larger convergence domain. At a channel zero \(w_\rho\), the relevant half-transform argument is \(\rho-1/2\), not \(1-\rho\). Both are zero-free in the relevant cases anyway. At the first zero,

\[
 \Lambda_>(1-\rho_1)=0.1305564167268266581\ldots\,i.
\]

This number is only a check; nonvanishing has an analytic proof above. On the critical line

\[
 \Lambda(1/2+it)=2\Re\Lambda_>(1/2+it)=2\Re\Lambda_<(1/2+it).
\]

A critical zeta zero therefore makes the half transforms nonzero, purely imaginary, and opposite. There are no incomplete-transform resonance modes for this particular outgoing half-vector.

**Status: PROVED.**

### T3(d)

**Statement and scope of refutation.** The printed statement at report/sections/04p_gl1_bond.tex:103–108, “the dilation-cyclic subspace of the odd part”, is not literally defined in \(H\): \(\phi\notin H\). Its natural inversion-symmetric \(L^2\) repair is false. Taking the full or forward cyclic space of \(g\) gives \(H\); subsequently removing the outgoing half gives the full backward shift. Cutting first to the outgoing half and taking its forward orbit gives \(H_+\), with zero orthogonal defect. None of these constructions gives \(K_\Theta\), which is nonzero and has the discrete zero modes of T6(a).

This failure is not confined to the symmetric weight. For every admissible \(0<a<1/2\), the transform of \(y^a\phi\) is \(\Lambda(2a+2i\tau)\), with the same exponential gamma decay and a polynomial zeta bound. T3(b)'s argument still gives full forward cyclicity. T3(c)'s zero-free half-plane and endpoint-support argument likewise make its outgoing half outer.

One cannot conclude that **every conceivable** theta-based construction inside this same abstract \(L^2\) bond fails. T5(c) constructs \(\Theta H^2_+\) by using the continued edge quotient explicitly. That is extra scattering data, not an implication of Gaussian cyclicity. Other orders of projection and orbit closure must be specified rather than bundled into an undefined “no reading” assertion. The compact-test-function construction is a different one, treated next.

**Status: REFUTED** for conj:h-theta under the specified literal/natural cyclic-and-cut readings.

## T4. Burnol causality and the bad-zero defect

### T4(a)

**Statement.** Burnol's \(D_+\) is outgoing for the brief's forward time. But \(V\overline{E(S_{\le1})}\) is an **incoming-half** subspace, not an outgoing-half subspace. Restriction to the trivial compact character reduces the criterion to RH for \(\zeta\).

**Source theorem.** The definitions of \(S_{\le1},D_\pm\) are math/0001013:main.tex:240–245. The outgoing/incoming axioms are at :247–255; the outgoing implication is “\(|\lambda|\geq 1 \Rightarrow U(\lambda){\cal D}_+\subset{\cal D}_+\)”. The causality criterion is :268–270, “if and only if \({\cal D}_-\perp{\cal D}_+\)”. The closure theorem is :290–293. Crucially his Hardy space is defined at :283–284 by “\(\mbox{\rm ess-supp}(f)\subset\{|u|\leq 1\}\)”, not \(|u|>1\). The stronger exact closure identity is :639: “\(V(\Delta)=B\cdot\HH^2\)”.

**Transcription and proof of orientation.** Let \(\Delta\subset H\) denote the closed span of the images of the unit-ball tests after T1(c)'s unitary coordinate change. For real \(\lambda>0\),

\[
 U_B(\lambda)h(x)=h(x/\lambda),\qquad
 WU_B(\lambda)W^{-1}=U_{2\log\lambda}.
\]

Thus \(\Delta\) is invariant under \(U_{-t}\), \(t\ge0\); \(D_+=\Delta^\perp\) is invariant under \(U_t\). Put

\[
 s_\pm(\tau)=\tfrac12\pm2i\tau,\qquad
 v_-(\tau)=\frac{s_+(\tau)-1}{s_+(\tau)}
          =\frac{\tau+i/4}{\tau-i/4},\qquad
 B_-(\tau)=B(s_+(\tau)).
\]

Here \(B\) is Burnol's Blaschke product in \(\Re s>1/2\), with bad zeros counted with multiplicity; its product and absence of singular factors are explained at math/0001013:main.tex:346–405, including “the product of an outer factor with the Blaschke product”. Both \(v_-\) and \(B_-\) are inner in \(\mathbb C_-\). Write \(V_y\) for multiplication by \(v_-\). Then

\[
 V_y\Delta=B_-H^2_-,\qquad
 D_+=V_y^{-1}B_-H^2_+,\qquad
 D_-=JD_+=V_yB_-^{-1}H^2_-.
\]

The chosen real-symmetric normalization of \(B\) gives \(JB_-J=B_-^{-1}\). This is the identity explicitly used in math/0001013:main.tex:713–716. Consequently \(V_yD_+=B_-H^2_+\); it is the plain outgoing half after \(V_y\) alone only when \(B=1\). The outgoing representation \(B_-^{-1}V_y\) sends \(D_+\) to \(H^2_+\) and \(D_-\) to \(V_y^2B_-^{-2}H^2_-\).

For clarity about measures, if \(F_L(s)=\int_0^\infty f(x)x^{s-1}dx\), then

\[
 \widehat{Rf}(\tau)=\sqrt2\,F_L(s_+(\tau)),\qquad
 \widehat{JRf}(\tau)=\sqrt2\,F_L(s_-(\tau)).
\]

These are isometries with the respective boundary measures. In particular \(JR\), not \(R\), takes Burnol's right-half-plane Hardy space to \(H^2_+\).

Finally \(C_{\mathbb Q}^1\cong\widehat{\mathbb Z}^{\,\times}\). Averaging over this compact group leaves its trivial isotypical sector. The \(L\)-factor in that sector is \(\zeta(s)\); the signs at the real place reduce the real test function to its even part. This is not a restriction to all Dirichlet characters. The subclass \(f_\infty\otimes1_{\widehat{\mathbb Z}}\), with \(f_\infty\) even and supported in \([-1,1]\), already yields exactly \(BH^2\), by math/0001013:main.tex:489–495, “the space of multiples of the Blaschke product”. Conversely all projected adelic tests have Tate transforms divisible by \(\zeta\) with a multiplier holomorphic at its nontrivial zeros (:617–624). Thus the larger adelic test class has the same closed subspace in this sector. Burnol's proof of causality therefore applies sector by sector, and here gives precisely RH for \(\zeta\).

**Status: PROVED.**

### T4(b)

**Corrected statement.** Define an outgoing invariant space by reflecting Burnol's incoming closure:

\[
 \mathcal N=JV_y\Delta,\qquad
 \widehat{\mathcal N}=B_{\rm bad}H^2_+,\qquad
 B_{\rm bad}(\tau)=B(s_-(\tau)).
\]

Its defect

\[
 K_{\rm bad}=H^2_+\ominus B_{\rm bad}H^2_+
\]

is a legitimate scalar model space and is zero iff RH. Calling it the **GL\(_1\) bad-zero defect channel** distinguishes it from Burnol's scattering system.

**Proof.** Apply \(J\) to T4(a). Since \(s_-(\mathbb C_+)=\{\Re s>1/2\}\), the result is an upper-half-plane inner function. Label its zeros using the conjugate bad zero \(\bar\rho\):

\[
 w^{(1)}_\rho=\gamma/2+i(\sigma-1/2)/2,\qquad
 s_-(w^{(1)}_\rho)=\bar\rho,\qquad \sigma>1/2.
\]

Equivalently the image of \(\rho\) itself under \(s_-^{-1}\) has real part \(-\gamma/2\). With the first labeling, the adjoint compressed semigroup has modes

\[
 C_t^{(1)}k_{w^{(1)}_\rho}
   =\exp\!\left(-\frac{\sigma-1/2}{2}t-\frac{i\gamma}{2}t\right)
      k_{w^{(1)}_\rho}.
\]

There is one Jordan chain of length \(m_\rho\) at a zero of multiplicity \(m_\rho\), not \(m_\rho\) independent eigenvectors. The decay is \((\sigma-1/2)/2\) in the \(y\)-clock and \(\sigma-1/2\) in the \(x\)-clock. The only way the pure Blaschke product can be constant is to have no bad zeros; functional-equation symmetry makes that equivalent to RH.

The brief's actual definition

\[
 M=\overline{\operatorname{span}}\{U_tE(\varphi):t\ge0,\ \varphi\in S_{\le1}\}
\]

does **not** have this defect: \(M=H\). Indeed, after the harmless coordinate normalization,

\[
 V_yM
 =B_-\,\overline{\operatorname{span}}_{t\ge0}e^{it\tau}H^2_-=H.
\]

In physical logarithmic coordinates the last span consists of functions supported in \(X<t\), whose union is dense in \(L^2(\mathbb R)\). The necessary repair is \(JV_y\Delta\), not a forward orbit of \(\Delta\) before reflection.

**Status: PROVED** for the corrected defect construction; the displayed \(VM=B_{\rm bad}H^2_+\) in the brief is refuted.

### T4(c)

**Statement.** There is an exact equivalence of RH criteria, but not an equality of the two scattering cavities:

\[
 K_{\rm bad}=0
 \quad\Longleftrightarrow\quad {\rm RH}
 \quad\Longleftrightarrow\quad
 \Im w_\rho=\tfrac14\ \hbox{for every zero }\rho.
\]

**Proof and scattering correction.** The outer equivalences follow from T4(b) and T2(c). Burnol's actual scattering multiplier, in the outgoing representation in T4(a), is

\[
 \mathcal S_{B,-}=v_-^2B_-^{-2}.
\]

This is exactly math/0001013:main.tex:509–514, “\(S=V^2B^{-2}\)”, and :694–699 in the adelic proof. Reflecting the spectral variable gives

\[
 \mathcal S_{B,+}(\tau)=v_+(\tau)^2B_{\rm bad}(\tau)^{-2},\qquad
 v_+(\tau)=\frac{\tau-i/4}{\tau+i/4}.
\]

This multiplier is inner in \(\mathbb C_+\) iff \(B_{\rm bad}=1\). If a bad zero has multiplicity \(m\), it is a pole of order \(2m\) of this scalar scattering multiplier; the factor \(v_+^2\) cannot cancel it. If RH holds, the multiplier is \(v_+^2\), not \(1\). It is “trivial” only in the sense of having no nontrivial zeta-zero data; after removing the elementary factor it is \(1\). Its causal model space under RH is \(K_{v_+^2}\), of dimension \(2\), whereas the bad-zero defect is zero. Off RH the actual pair fails causality, and an assertion that its standard causal model space is \(K_{B_{\rm bad}}\) is unjustified.

The dictionary is therefore:

| Zeta zero \(\rho=\sigma+i\gamma\) | GL\(_2\) reduced model | GL\(_1\) bad-zero defect | Connes weighted cokernel |
|---|---|---|---|
| Any nontrivial zero | \(w_\rho=\gamma/2+i(1-\sigma)/2\) | Present only if \(\sigma>1/2\) | Present only if \(\sigma=1/2\) |
| Bad zero | Decay \((1-\sigma)/2\) | \(w^{(1)}_\rho=\gamma/2+i(\sigma-1/2)/2\) | No such off-line spectral character |
| Critical zero | Decay \(1/4\) | No mode | Character, with the multiplicity restriction in T6(a) |

The criteria encode the same logical assertion RH. They do not provide an intertwining unitary between the GL\(_1\) and GL\(_2\) models.

**Status: PROVED.**

### T4(d)

**Statement.** In the unweighted bond the critical zeros are zeros of a cyclic vector's continuous spectral density, not missing spectral subspaces.

**Proof.** Plancherel gives

\[
 C(t)=\langle U_tg,g\rangle
 =\frac1{2\pi}\int_{\mathbb R}|\widehat g(u)|^2e^{itu}\,du.
\]

For finite \(c_j,t_j\), the sum \(\sum_{j,k}c_j\bar c_kC(t_j-t_k)\) is \(\|\sum_jc_jU_{t_j}g\|^2\ge0\). Thus \(C\) is positive definite; it is also continuous, real, and even. Its continuous spectral-density representative vanishes exactly at \(u=\gamma/2\) with \(\zeta(1/2+i\gamma)=0\). If that zero has multiplicity \(m\), the density vanishes to order \(2m\), not necessarily order \(2\). Burnol's Tate-transform assertion is math/0001013:main.tex:218–223; its proof ends at :569–572 with “\(\widehat{E(\varphi)}(\chi,s)=C(K)L(\varphi,\chi,s)\)”. Other test functions can have additional zeros in their Mellin multipliers, whereas the Gaussian has none besides the zeta zeros.

An isolated zero has spectral measure zero, and does not change the regular representation or contradict T3. Absorption becomes a nonzero cokernel only after Connes changes the topology; see T6(a).

There is no established equality here with the ring-norm distributional trace. The latter is a zero-counting trace, as specified in report/sections/04_riemann_channel.tex:176–184; \(C(t)\) is a single-vector matrix coefficient. Even substituting \(|\widehat g|^2\) directly into the usual analytic version of the Weil formula is invalid: its real-analytic continuation is \(\widehat g(\tau)^2\), with double poles at \(\pm i/4\), precisely the pole-evaluation points after the change \(r=2\tau\). A regularization and an operator identification would have to be specified. Connes's positive cutoff trace is another distinct object: math/9811068:main.tex:2589–2594 records “\(Q'_{\Lambda,0}\leq S_\Lambda\)” and the trace with \(S_\Lambda-Q'_{\Lambda,0}\).

For comparison with the notebook's grading, Meyer constructs a virtual representation with the two poles in \(\pi_+\) and the zeros in \(\pi_-\): math/0311468:main.tex:208–215, “The two poles occur in~\(\pi_+\), the zeros in~\(\pi_-\)”; the spectrum/multiplicity theorem is :4597–4601, “\(\mult(\omega,\pi)=\ord(\omega,L_\GF)\)”. Its character is the Weil distribution (:249–254). Thus “poles even, zeros odd, explicit formula as supertrace” has a precise representation-theoretic realization, but on Meyer's smaller function spaces, not as an inversion parity decomposition or an ordinary trace of this one \(L^2\) vector. He explicitly says at :234–235: “zeros on the critical line appear as above, but zeros off the critical line appear as resonances.” This describes Connes's situation, not additional eigencharacters in Connes's stated weighted cokernel.

**Status: PROVED** for the spectral-density and source comparisons. **Status: OPEN** for an identification of this autocorrelation with the notebook's ring-norm trace.

## T5. Two GL\(_1\) theta transforms in the GL\(_2\) constant term

### T5(a)

**Statement.** For \(y,t>0\),

\[
 \int_0^1\Theta_{x+iy}(t)\,dx
 =\theta(t/y)+\sqrt{y/t}\bigl(\theta(ty)-1\bigr).
\]

**Proof.** The \(m=0\) terms give \(\theta(t/y)\). For \(m\ne0\), the factor involving \(\Im z\) is \(e^{-\pi tm^2y}\). Since \(\sum_n e^{-\pi t(mx+n)^2/y}\) is periodic in \(mx\) with period \(1\), its integral over \(x\in[0,1]\) is

\[
 \int_{\mathbb R}e^{-\pi tu^2/y}\,du=\sqrt{y/t}.
\]

There are \(|m|\) periods and the substitution contributes \(1/|m|\). Positivity justifies all interchanges. Summing over \(m\ne0\) proves the formula.

The brief's subsequent Poisson rewrite has a wrong factor. The correct one is

\[
 \sqrt{y/t}\,\theta(ty)=t^{-1}\theta(1/(ty)),\qquad
 \int_0^1\Theta_{x+iy}(t)\,dx
 =\theta(t/y)+t^{-1}\theta(1/(ty))-\sqrt{y/t}.
\]

The exact involution at fixed \(y\) is the **weighted** inversion

\[
 (\mathcal W F)(t)=t^{-1}F(1/t),\qquad \mathcal W^2=1.
\]

It exchanges \(\theta(t/y)\) and \(\sqrt{y/t}\theta(ty)\), and fixes \(\sqrt{y/t}\). This follows by applying the one-dimensional Poisson equation once to each term. The map \(t\mapsto1/(y^2t)\) is an involution of the variable, but it does not exchange these two channels.

**Status: PROVED.**

### T5(b)

**Statement and normalization.** Let

\[
 E(z,s)=\frac12\sum_{\gcd(m,n)=1}
             \frac{y^s}{|mz+n|^{2s}},\qquad
 E^*(z,s)=\pi^{-s}\Gamma(s)\zeta(2s)E(z,s).
\]

Then \(c=1/2\) in the brief:

\[
 E^*(z,s)=\frac12\int_0^\infty(\Theta_z(t)-1)t^s\,\frac{dt}{t}
 \quad(\Re s>1),
\]

and its constant term is

\[
 \frac12\Lambda(2s)y^s+\frac12\Lambda(2s-1)y^{1-s}.
\]

**Proof.** Termwise Mellin integration of the lattice sum gives
\(\pi^{-s}\Gamma(s)\sum_{(m,n)\ne(0,0)}y^s/|mz+n|^{2s}\).
Grouping by the positive common divisor makes the last sum \(2\zeta(2s)E(z,s)\). Alternatively T5(a) and the substitutions \(u=t/y\), respectively \(u=ty\), give

\[
 \int_0^\infty(\theta(t/y)-1)t^s\frac{dt}{t}
       =y^s\Lambda(2s)\quad(\Re s>1/2),
\]
\[
 \int_0^\infty\sqrt{y/t}(\theta(ty)-1)t^s\frac{dt}{t}
       =y^{1-s}\Lambda(2s-1)\quad(\Re s>1).
\]

These calculations agree where both converge and then continue meromorphically. Thus the standard Eisenstein coefficient is

\[
 \varphi_E(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)},\qquad
 \varphi_E(1/2+i\tau)=r(\tau)S(\tau)=\frac{r(\tau)}{\Theta(\tau)}.
\]

In particular \(\varphi_E(1/2)=-1\) while \(S(0)=1\). The coefficient has the residual pole at \(s=1\), or \(\tau=-i/2\); \(S=\varphi_E/r\) removes it.

**Which wave scattering matrix?** A specification of the incoming/outgoing spaces is essential. [Uetake, *The Lax–Phillips infinitesimal generator and the scattering matrix for automorphic functions*, 2007](https://www.impan.pl/shop/en/publication/transaction/download/product/85177), pp. 104–105, 110–111, 116, explicitly distinguishes projected spaces \(D'_\pm\) from intersected spaces \(D''_\pm\), and the causal factor \(S_{c0}(p)=\xi(2p)/\xi(-2p)\). In his wave variable \(p=i\tau\), his formulas give

\[
 S'_{\rm wave}(\tau)=-\varphi_E(1/2+i\tau)=-r(\tau)S(\tau),
 \qquad
 S''_{\rm wave}(\tau)=-r(\tau)^{-1}S(\tau),\qquad
 S_{c0}(i\tau)=S(\tau).
\]

The minus signs reflect his translation normalization. The intersected-space generator has an additional eigenvalue \(-1/2\), removed in the \(S_{c0}\) model (p. 100). Thus the notebook's \(S\) is the **reduced causal factor**; deleting cusp forms alone does not specify this reduction. Lax–Phillips 1976, §§3, 6–7, supplies the wave construction; local math/0001013:main.tex:785–787 is only its bibliographic entry. The needed distinction also matches the warning in notes/reviews/cusp-graph-2026-09-20.md:100 about treating a choice of radiation-space repair as a derivation.

**Status: PROVED** for the theta/Eisenstein identities and exact factor relations; the wave-space interpretation is the cited primary-source result.

### T5(c)

**Statement.** The reduced symbol is the continued ratio of the two GL\(_1\) edge transforms in T2(c). This is an identity of scattering coefficients, not an identification of the GL\(_2\) cavity with a Gaussian orbit or with two Burnol defect spaces.

**Proof and precise weight dictionary.** For the zero Fourier mode of the cusp wave equation, writing \(u(y,t)=y^{1/2}v(\log y,t)\) gives

\[
 (y^2\partial_y^2+1/4)\bigl(y^{1/2}v(\log y,t)\bigr)
       =y^{1/2}v_{XX}(X,t).
\]

Thus the zero mode propagates freely in \(X\). In the Mellin transform, multiplying \(g\) by \(y^{1/4}\) changes \(\tau\) to \(\tau-i/4\), and multiplying by \(y^{-1/4}\) changes it to \(\tau+i/4\). Explicitly

\[
 y^{1/4}g=y^{1/2}\phi,\qquad y^{-1/4}g=\phi.
\]

The half-vector memberships are

| Vector | \(L^2(0,1;dy/y)\) | \(L^2(1,\infty;dy/y)\) |
|---|---|---|
| \(y^{1/2}\phi\) | Yes | No: tends to \(-1\) |
| \(\phi\) | No: tends to \(-1\) | Yes |
| \(g\) | Yes | Yes |

These follow from T1(b). Full edge transforms require continuation; taking only their convergent halves would instead give incomplete transforms and would not prove T2(c). The identity explains the \(i/4\) weight difference without claiming a bounded imaginary-shift operator on the whole bond.

There is an explicit spectral construction of a cyclic vector for the desired outgoing subspace. Define

\[
 \widehat h_\Theta(\tau)=\frac{\Theta(\tau)}{(\tau+i)^2},\qquad
 h_\Theta(e^X)=\frac1{2\pi}\int_{\mathbb R}
       \frac{\Theta(u)}{(u+i)^2}e^{-iuX}\,du.
\]

The integral is absolutely convergent. Since \((\tau+i)^{-2}\) is outer in \(H^2_+\), the inner factor of \(\widehat h_\Theta\) is exactly \(\Theta\). Paley–Wiener and Beurling–Lax give \(h_\Theta=0\) for \(X<0\) and

\[
 \overline{\operatorname{span}}\{U_th_\Theta:t\ge0\}
       =\mathcal M^{-1}(\Theta H^2_+),
\]

where \(\mathcal M\) denotes the fixed Mellin unitary. Inserting T2(c) makes this a theta-derived integral formula. It is not the original theta vector, either cut or weighted. No Jacobi-theta closed form for this inverse transform is established here; “closed form” without a specified class would not be a meaningful nonexistence claim. The construction uses the desired continued quotient and therefore does not rescue the literal cyclic conjecture.

**Status: PROVED** for the identity, weight dictionary, and explicit spectral generator.

## T6. The shift dictionary, multiplicities, and Sonine spaces

### T6(a)

**Statement.** The exact dictionary is \(w_\rho=a_\rho+i/4\). In the \(y\)-picture the ordinary kernel mode is

\[
 \mathcal M^{-1}k_{w_\rho}(y)
   =-i\,y^{-(1-\sigma)/2-i\gamma/2}1_{y>1}.
\]

With all multiplicities included the unconditional completeness statement is

\[
 \mathcal M^{-1}K_\Theta
  =\overline{\operatorname{span}}\left\{
    (\log y)^j y^{-(1-\sigma)/2-i\gamma/2}1_{y>1}:
    \xi(\rho)=0,\ 0\le j<m_\rho
    \right\}.
\]

The version omitting logarithmic powers is complete iff every zero is simple.

**Proof.** For \(\Im w>0\),

\[
 \int_0^\infty e^{-i\bar wX}e^{i\tau X}\,dX
       =\frac{i}{\tau-\bar w},\qquad
 \mathcal M^{-1}\frac1{(\tau-\bar w)^{j+1}}
       =\frac{(-i)^{j+1}}{j!}X^je^{-i\bar wX}1_{X>0}.
\]

The derivative kernels through order \(m_\rho-1\) belong to \(K_\Theta\) because \(\Theta\) vanishes to that order. A vector orthogonal to all these kernels vanishes at every zero to its full multiplicity. Dividing it by the pure Blaschke product of T2(d) leaves an \(H^2\) function with the same boundary norm. It therefore lies in both \(\Theta H^2\) and \(K_\Theta\), and is zero. This proves completeness. At a multiple zero \(w\), the nonzero function \(\Theta(\tau)/(\tau-w)\in K_\Theta\) vanishes at every distinct zero. It is orthogonal to every ordinary evaluation kernel, proving the necessity of simplicity for the shorter formula.

The eigenvalue and Jordan rule are transparent in the physical picture:

\[
 C_t e^{-i\bar wX}=e^{-it\bar w}e^{-i\bar wX},\qquad
 C_t(X^je^{-i\bar wX})
   =e^{-it\bar w}\sum_{\ell=0}^j\binom j\ell t^{j-\ell}
          X^\ell e^{-i\bar wX}.
\]

Under RH, these functions are \(X^je^{-X/4}\chi_\gamma(e^X)\), where \(\chi_\gamma(y)=y^{-i\gamma/2}\). Thus “cut to the outgoing half and damp by \(y^{-1/4}\)” is an exact formula for the ordinary modes under RH, with logarithmic powers for the generalized modes. The character transforms under \(U_t\) by \(e^{+it\gamma/2}\); the mode transforms under the **adjoint** compressed semigroup by \(e^{-it\gamma/2-t/4}\). This time reversal must not be suppressed in a proposed intertwining.

**Connes's precise theorem.** Math/9811068:main.tex:873–885 says the spectrum consists of zeros “which have real part equal to \({1\over2}\)” and gives multiplicity as “the largest integer \(n < {1+\delta\over2}\), \(n\leq\) multiplicity”. Accordingly a zero of order \(m\) contributes

\[
 n_\delta(m)=\max\{n\in\mathbb Z_{\ge0}:n\le m,\ 2n-1<\delta\}.
\]

A fixed \(\delta>1\) detects every critical zero but need not recover all multiplicities. Full multiplicity \(m\) requires \(\delta>2m-1\). These are spectral characters and generalized characters of a cokernel representation, not characters lying in the unweighted bond as \(L^2\) vectors. The weighted representation itself is not unitary; the source explains this at :761–765, “because of the weight”. For the dual critical evaluation of order \(j\), the squared dual norm has the same convergence as
\(\int_{\mathbb R}|X|^{2j}(1+X^2)^{-\delta/2}\,dX\), finite exactly when \(\delta>2j+1\). This gives the same strict multiplicity threshold.

For an off-line zero the formula still supplies a GL\(_2\) mode with damping \((1-\sigma)/2\), but Connes's stated cokernel theorem supplies no character indexed by that off-line zero. Coincidence of its ordinate with another critical zero would not identify the two zeros. No unitary map from Connes's weighted cokernel to \(K_\Theta\) has been proved by the cutoff-and-damping formula.

**Status: PROVED** for the multiplicity-corrected statements and the RH-conditional damping dictionary.

### T6(b)

**Statement.** All derivative kernels at all zeros form a complete minimal system. Ordinary kernels form a complete minimal system under the additional hypothesis that all zeros are simple. Under RH, the normalized ordinary kernels in the simple-zero case are not a Riesz basis. More generally the full natural derivative-kernel system is not a Riesz basis under RH.

**Proof of minimality.** At a zero \(w\) of order \(m\), the functions

\[
 \frac{\Theta(\tau)}{(\tau-w)^\ell},\qquad 1\le\ell\le m,
\]

belong to \(K_\Theta\): they are in \(H^2_+\), and after multiplication by \(\bar\Theta\) their boundary functions belong to \(H^2_-\). Their derivatives at \(w\) give an invertible triangular matrix of evaluations of orders \(0,\ldots,m-1\); their corresponding derivatives vanish at every other zero. Taking linear combinations produces a biorthogonal system to the derivative kernels. This proves minimality. Completeness was proved in T6(a). Merely repeating the identical ordinary kernel at a multiple zero does not give a minimal system.

**Proof of failure of a Riesz lower bound.** Under RH all \(w\)'s have height \(b=1/4\). For two normalized ordinary kernels the absolute inner product is

\[
 \left|\langle \widetilde k_{a+ib},\widetilde k_{a'+ib}\rangle\right|
 =\frac{2b}{\sqrt{(a-a')^2+4b^2}}.
\]

If distinct ordinates have arbitrarily small gaps, this tends to \(1\); after adjusting a phase, the difference of two unit vectors tends to zero, contradicting any uniform Riesz lower bound.

Here is a proof of the needed alternative that does not rely on an individual-gap asymptotic. If multiplicities are bounded and distinct ordinates have a uniform positive gap, their counting function is \(O(T)\). Under RH the even product is

\[
 \frac{\xi_{\rm crit}(z)}{\xi_{\rm crit}(0)}
   =\prod_{a>0}(1-z^2/a^2)^{m_a}.
\]

The counting bound, by integration by parts, gives
\(\sum_{a>0}m_a\log(1+v^2/a^2)=O(v)\).
But at \(z=iv\), Stirling and the functional equation give
\(\log|\xi_{\rm crit}(iv)|=v\log v+O(v)\), a contradiction. Thus bounded multiplicities force a sequence of distinct gaps tending to zero. The usual mean spacing \(\pi/\log T\) in the scaled ordinate \(a=\gamma/2\) is consistent with this; it is not a pointwise formula for consecutive gaps.

If instead multiplicities are unbounded, consecutive derivative kernels at one increasingly multiple zero, in the physical picture \(X^je^{-i\bar wX}\), have normalized inner product in absolute value

\[
 \frac{\Gamma(2j+2)}
 {\sqrt{\Gamma(2j+1)\Gamma(2j+3)}}
 =\sqrt{\frac{2j+1}{2j+2}}\ \longrightarrow 1.
\]

The same lower-bound obstruction applies. This covers both possibilities for multiplicities.

Completeness and minimality do not assert a Schauder basis, unconditional expansions, or bounded diagonalization in the mode coordinates. The finite-flag construction in report/sections/04h_rebound_state.tex:195–204 does not require an infinite Riesz basis; it cannot be upgraded to one by this argument. Nor does one kernel per zero mean independent exits: the model's exit is the single functional \(j f=f(0)\) in logarithmic coordinates. All ordinary exponential modes couple to it; higher powers \(X^j\), \(j>0\), can have zero instantaneous exit while their Jordan evolution remains observable.

The distinction matters for thm:arithmetic-metric. Report/sections/04l_elliptic_cavity_channel.tex:171–175 states that its arithmetic defect “has rank \emph{four}” and requires “at least four exit coordinates”. That is a different metric and completion. In the continuous analogue an orthonormal family evolving as \(e^{-t/4}e^{-itH_0}\), with \(H_0\) self-adjoint, has generator loss \(-(A+A^*)=\tfrac12 I\), not a scalar exit form on a space of dimension greater than one. Under RH and simplicity, no boundedly equivalent Hilbert norm can turn the complete ordinary \(K_\Theta\) modes into an orthonormal basis: that would make them a Riesz basis in the original norm, contradicting the result above. None of these arguments determines the exit rank of Burnol's Sonine evaluator system.

**Status: PROVED** for unconditional completeness/minimality with jets. **Status: PROVED-CONDITIONAL (RH)** for failure of the Riesz-basis property.

### T6(c)

**Statement of the source results.** On \(L^2(0,\infty;dx)\), let

\[
 (\mathcal F_+f)(u)=2\int_0^\infty\cos(2\pi ux)f(x)\,dx.
\]

The transform is defined first on suitable test functions and extended unitarily. Burnol's \(K_a\) consists of functions for which \(f\) and \(\mathcal F_+f\) vanish on \((0,a)\); his \(L_a\) allows an independent constant for each on that interval. The definitions are math/0203120:main.tex:413–428: “constant in \((0,a)\)” and “vanishing identically”. The cosine normalization is :305–306.

Use the unitary \(R\) from T1(c), and put \(\mathcal F_b=R\mathcal F_+R^{-1}\). On the bond, \(RK_a\) is the space in which both \(h\) and \(\mathcal F_bh\) vanish for \(0<y<a^2\). In \(RL_a\), both \(y^{-1/4}h(y)\) and \(y^{-1/4}(\mathcal F_bh)(y)\) are constant there. This Fourier involution is not the bare multiplicative inversion \(J\).

If \(F_R(s)=\int_0^\infty f(x)x^{-s}dx\) is Burnol's **right** Mellin transform, then

\[
 \widehat{Rf}(\tau)=\sqrt2\,F_R(1/2-2i\tau),\qquad
 M(f)(s)=\pi^{-s/2}\Gamma(s/2)F_R(s).
\]

The completed transform of \(K_a\) is entire, with continuous evaluation (math/0203120:main.tex:437–443, “is an entire function”). For \(L_a\), \(M(f)\) is meromorphic with at most poles at \(0,1\), with continuous derivative and residue evaluations (:460–469, “at most poles at \(0\) and at \(1\)”).

Burnol defines bilinear evaluators \(Y^a_{\rho,k}\) at :472–480 by \(\int fY=M(f)^{(k)}(\rho)\); the Hermitian representing vector in our linear-first convention is \(\overline{Y^a_{\rho,k}}\). His Theorem A, :516–525, states that this is “a minimal system” iff \(a\le1\), and “a complete system” iff \(a\ge1\). This includes every nontrivial zero, on or off the line, through \(0\le k<m_\rho\). For \(a<1\) the orthogonal complement is the co-Poisson space \(P_a\). Theorem B, :587–594, gives the complete minimal dual system generated by \(\zeta(s)/(s-\rho)^\ell\), \(1\le\ell\le m_\rho\). Thus the distinguished complete-and-minimal level is \(L_1\), not \(K_1\): Theorem A', :528–538, says the full evaluator system in the Sonine \(K_1\) is not minimal and becomes complete and minimal after two suitably chosen evaluators are omitted.

There are two limitations to the residue-series claim in the brief. Theorem main, math/0203120:main.tex:989–998, assumes the dense subspace “of functions with quick decrease in vertical strips”, not arbitrary \(G\in\widehat L_1\). Also :964–984 defines convergence by grouped height cutoffs; “absolutely convergent” uses grouped blocks of zeros, with higher-order residues when zeros are multiple. It is not a theorem asserting an ungrouped absolute basis expansion for every \(G\).

**Dilation does not move along the diagonal Sonine filtration.** Define the two-cutoff space

\[
 L_{a,b}=\{f:f\text{ is constant on }(0,a),\
                \mathcal F_+f\text{ is constant on }(0,b)\}.
\]

Thus \(L_a=L_{a,a}\). For \(D_\lambda f(x)=\lambda^{-1/2}f(x/\lambda)\), direct substitution gives

\[
 \mathcal F_+D_\lambda=D_{\lambda^{-1}}\mathcal F_+,\qquad
 D_\lambda L_{a,b}=L_{\lambda a,b/\lambda},\qquad
 U_tRL_{a,b}=RL_{ae^{t/2},be^{-t/2}}.
\]

The same holds for the spaces with both constants zero. One cutoff increases and the other decreases; their product is invariant. Therefore \(U_tRL_a\ne RL_{ae^{\pm t/2}}\) as a general covariance law. The strictly decreasing diagonal chain is real (math/0203120:main.tex:417–423), but it is not itself a Lax–Phillips time-translation filtration.

**What remains to construct.** Complete minimal evaluators give an arithmetic coordinate system, not a contraction semigroup, an exit form, or a unitary dilation. A precise version of the desired question is recorded below as H-THETA-1. It requires at least finite Gram-matrix inequalities for the proposed time evolution; minimality alone supplies no boundedness. The two-cutoff covariance above, rather than the false one-cutoff covariance, must guide any geometric construction.

**Status: PROVED** for the transcribed theorems and the dilation correction. **Status: OPEN** for a Sonine realization of the requested dynamics.

## Correction ledger against the brief

| Item | What the brief says | What is true |
|---|---|---|
| 0, T1(a) | The theta remainder is the “odd part”. | This may name an arithmetic grading. Its self-dual \(L^2\) weighting is \(J\)-even, not \(J\)-odd. |
| 0, T3(d) | The printed cyclic construction is defined in the unweighted bond. | \(\phi\notin H\); an \(L^2\) weighting or a distributional construction must first be specified. The symmetric weighting gives the refuted construction. |
| 1 | Outgoing \(y>1\) is \(H^2_+\). | Correct. The modes in that convention belong to the adjoint compression \(C_t\). The \(du/(2\pi)\) normalization changes 04h's inverse-kernel constant to \(-i\). |
| T1(c) | The Gaussian gives \(g\) by Connes's \(E\). | It gives \(g\) pointwise by Burnol's subtracted \(E\); Connes's stated Gaussian is outside his vanishing-test domain. The unitary \(x\)-to-\(y\) map also contributes \(1/\sqrt2\). |
| T2(a) | \(s=1\) corresponds to \(+i/4\). | It corresponds to \(-i/4\), residue \(-i\); \(s=0\) corresponds to \(+i/4\), residue \(+i\). |
| T2(a) | \(\lvert\widehat g(u)\rvert\sim C\lvert u\rvert^ce^{-\pi\lvert u\rvert/2}\). | The exact gamma asymptotic has power \(-1/4\) times \(\lvert\zeta(1/2+2iu)\rvert\). There is no such fixed positive asymptotic constant; an elementary upper bound has power \(1/4\). |
| T2(b) | Analytic on \(\Im\tau>-1/4\), with a pole “at” \(-i/4\). | The pole is on that domain's boundary, and belongs to its meromorphic extension. |
| T2(c) | The edge values are Mellin integrals. | They are meromorphic continuations, not convergent full edge integrals; \(\tau=0\) additionally requires a removable pole-over-pole limit. |
| T2(c) | Hermite–Biehler for unshifted \(\xi_{\rm crit}\) would be RH. | It is impossible for this real entire function. HB for every positive imaginary translate is an RH equivalent. |
| T2(c) | \(F\mapsto F/E\) is isometric without specifying the norm. | It is so with the normalized de Branges measure \(du/(2\pi)\); the usual \(du\) convention requires a constant adjustment. |
| T2(d) | Pure Blaschke character may require a further hypothesis. | It is unconditional. T2(c)–(d) prove it by a paired Hadamard product and also exclude a delay by \(\Theta(iv)\sim\sqrt{\pi/v}\). |
| T3(a) | Connes's surjectivity directly supplies the Gaussian cyclicity. | Surjectivity concerns all tests. Single-vector cyclicity needs, and has, the independent Fourier-uniqueness proof. |
| T3(b) | The full backward shift has no resonances. | Its generator has the whole open left half-plane as point spectrum. It has no discrete zeta-selected spectrum. |
| T3(c) | Zeros in \(\mathbb C_+\) correspond to \(\Re s<1\). | They would correspond to \(\Re s<1/2\); \(\Re s<1\) is the larger convergence half-plane. |
| T3(c) | The Gaussian half has an inner factor governed by incomplete-transform zeros, requiring a numerical distinction from \(\Theta\). | It is outer: \(\Lambda_>\) is zero-free throughout \(\Re s<1\). Its model-space defect is exactly zero. |
| T3(c) | Testing \(\Lambda_>(1-\rho)\) tests the \(\Theta\)-mode point. | The mode point gives \(\widehat g_>(w_\rho)=\Lambda_>(\rho-1/2)\). Nonvanishing holds at both points analytically. |
| T3(d) | No reading or construction inside the bond can give \(K_\Theta\). | The specified cyclic-and-cut readings fail. A construction using the continued edge quotient can give it; T5(c) supplies one. |
| T4 | \(V=1-A\) is the unitary convolution by \(a\). | \(A\) is convolution by \(a\); \(V=I-A\) is the unitary. |
| T4(a) | \(V\) turns the theta-test closure into the outgoing half. | It turns it into \(B_-H^2_-\), an incoming-half subspace. Reflection \(J\) is required for the upper-half-plane defect. |
| T4(a) | \(V\) by itself makes \(D_+\) the plain outgoing half. | \(V_yD_+=B_-H^2_+\). The outgoing representation is \(B_-^{-1}V_y\). Under RH, \(B_-=1\). |
| T4(b) | Forward saturation \(M\) gives \(VM=B_{\rm bad}H^2_+\). | That \(M\) is all of \(H\). The corrected space is \(\mathcal N=JV_y\Delta\). |
| 0, T4(b) | Burnol's scattering model space is \(K_B\), zero iff RH. | \(K_B\) is a bad-zero closure defect. Burnol's scattering is \(V^2B^{-2}\); under RH its elementary causal model has dimension \(2\), before elementary-factor removal. |
| 0, T4(c) | Scattering under RH is trivial. | Its arithmetic zero factor is trivial. The actual multiplier still contains \(V^2\). |
| T4(c) | Each bad zero gives a scattering pole without an order specification. | A zero of multiplicity \(m\) gives a pole of order \(2m\) in Burnol's stated scalar multiplier. The defect model uses multiplicity \(m\). |
| T4(b) | The bad-zero decay is \(\sigma-1/2\) in notebook time. | It is \((\sigma-1/2)/2\) in \(y\)-time; the larger rate uses idele \(x\)-time. |
| T4(c) | The two “cavities” are the same RH statement. | Their RH criteria are logically equivalent; no dynamical equivalence of their spaces follows. |
| T4(d) | Spectral density vanishes to second order at every critical zero. | Its order is twice the zeta multiplicity; exactly second order requires a simple zero. |
| T4(d) | A Weil trace connection for \(\lvert\widehat g\rvert^2\) can be used directly. | This is a vector spectral density, not a trace density. Its continuation has poles at the required Weil pole evaluations; a regularization is missing. |
| T5(a) | \(\sqrt{y/t}\theta(ty)=y\theta(1/(ty))\). | The prefactor is \(t^{-1}\), not \(y\). |
| T5(a) | The two channels are exchanged by \(t\mapsto1/(y^2t)\). | They are exchanged by the weighted involution \(F(t)\mapsto t^{-1}F(1/t)\). |
| T5(b) | \(S\) is simply the wave scattering matrix after deleting cusp forms. | \(\varphi_E=rS\); projected and intersected wave spaces give additional elementary factors. \(S\) is the reduced causal factor. |
| T5(c) | Weighting the Gaussian vector itself identifies the outgoing channel. | The weights explain the continued quotient. They do not make its divergent full edge integrals into Hilbert vectors or determine a cyclic-space equivalence. |
| T6(a) | Ordinary kernels span \(K_\Theta\), unconditionally. | Include derivative kernels/logarithmic powers for multiplicities. Ordinary kernels alone are complete iff all zeros are simple. |
| T6(a) | Every \(\delta>1\) recovers the full Connes multiplicity. | It recovers \(n\le m\) with \(n<(1+\delta)/2\); full \(m\) needs \(\delta>2m-1\). |
| T6(a) | The cutoff-damping dictionary is an identification of Hilbert representations. | It identifies mode formulas under RH, with adjoint time; it is not a unitary identification with the weighted cokernel. |
| T6(b) | RH makes the ordinary kernels complete and minimal. | Simplicity is additionally needed for that statement. Full jets are complete and minimal unconditionally. |
| T6(b) | Consecutive gaps are asymptotic to the mean gap. | Only the mean has that asymptotic. Arbitrarily close pairs suffice for the Riesz obstruction; unbounded multiplicities give a second obstruction. |
| T6(c) | \(L_a\) and \(K_a\) have interchangeable evaluator conclusions. | \(L_1\) has the complete minimal full system; the Sonine \(K_1\) has an excess of two evaluators in Theorem A'. |
| T6(c) | The residue expansion applies to every \(G\in\widehat L_1\), with ordinary absolute convergence. | The stated theorem applies to a dense rapidly decreasing subspace and uses grouped height-block convergence. |
| T6(c) | \(U_tL_a=L_{ae^{\pm t}}\), hence the diagonal filtration is a Lax–Phillips orbit. | In notebook time \(U_tRL_{a,b}=RL_{ae^{t/2},be^{-t/2}}\). The diagonal chain is not such an orbit. |
| T6(c) | Complete minimal evaluators supply “one exit per zero mode”. | They supply arithmetic coordinates. A generator, contractivity, exit rank, and minimal dilation remain to be constructed and checked. |

## Verdict on conj:h-theta

Conj:h-theta is ill-defined for its unweighted \(\phi\) and **refuted** by its natural symmetric \(L^2\) repair: \(g\)'s forward orbit is the entire bond, while its outgoing half is outer and leaves zero Hardy defect. The full backward shift obtained by removing the outgoing half has an unrestricted half-plane of eigenvalues, not the zeta model. What survives is an unconditional theorem identifying the reduced GL\(_2\) symbol with the continued ratio of the two GL\(_1\) theta edge transforms, and Burnol's separate theorem identifying RH with causality and with vanishing of the reflected bad-zero closure defect. Register those corrected theorems, with the elementary scattering factors and multiplicities explicit; retain a Sonine dynamics problem as open, without asserting that its evaluators or its diagonal filtration already form the desired channel.

## Restated conjectures to register

1. **H-THETA-EDGE — register as a theorem, not an open conjecture.** In the fixed Mellin convention the reduced upper symbol is the pure Blaschke inner function

   \[
   \Theta(\tau)=
   \frac{\widehat g(\tau-i/4)}{\widehat g(\tau+i/4)}
   \frac{\tau-i/2}{\tau+i/2}.
   \]

   The edge values are meromorphic continuations, its zero divisor is \(w_\rho=\gamma/2+i(1-\sigma)/2\), and the full root-vector system in its model space is given by T6(a). This does not assert that \(g\) generates its outgoing subspace.

   **Status: PROVED.**

2. **H-GL1-BAD — register as a corrected Burnol theorem.** For \(\Delta=\overline{E(S_{\le1})}\) in the units-invariant \(\mathbb Q\) sector, \(JV_y\Delta=B_{\rm bad}H^2_+\). Its model defect is zero iff RH; Burnol's scattering is separately \(v_+^2B_{\rm bad}^{-2}\), causal iff RH. This fixes both time orientation and the distinction between the defect model and the scattering cavity.

   **Status: PROVED.**

3. **H-THETA-1 — Sonine dynamics realization problem.** The following is a precise existence question, not a consequence of Burnol's basis theorems. In \(RL_1\), put

   \[
   e_{\rho,k}=R\overline{Y^1_{\rho,k}},\qquad
   \lambda_\rho=(\bar\rho-1)/2,
   \]
   \[
   T_t^0e_{\rho,k}
    =e^{\lambda_\rho t}
       \sum_{j=0}^k\binom kj(t/2)^{k-j}e_{\rho,j}.
   \]

   Does this densely defined algebraic semigroup extend to contractions on the **given** Sonine Hilbert norm, with a scalar exit form and minimal unitary dilation unitarily equivalent to the regular dilation \(U_t\) on the GL\(_1\) bond? The scalar-exit requirement means that the generator on this span, \(A_0e_{\rho,k}=\lambda_\rho e_{\rho,k}+(k/2)e_{\rho,k-1}\), satisfies

   \[
    -\langle A_0f,h\rangle-\langle f,A_0h\rangle
            =j_0(f)\overline{j_0(h)}
   \]

   for a scalar linear functional \(j_0\), with the appropriate closed generator/exit-form extension. The term with \(k-1\) is omitted when \(k=0\). Finite linear independence makes this definition unambiguous. If contractivity holds, density and decay on every finite root span already imply strong continuity and strong stability.

   This asks for a realization on a single GL\(_1\) dilation channel. It must be distinguished from thm:arithmetic-metric's proposal of independent exit coordinates per mode; that proposal would require a separately specified exit space and dilation multiplicity. This is a testable requirement on the Sonine evaluator Gram matrices. For simple zeros, writing \(G_{\rho\nu}=\langle e_{\rho,0},e_{\nu,0}\rangle\), a necessary scalar-exit condition is

   \[
   -(\lambda_\rho+\bar\lambda_\nu)G_{\rho\nu}
            =a_\rho\bar a_\nu
   \]

   for a single scalar family \(a_\rho\). Every finite matrix on the left must be positive and of rank one. More basically, without assuming a scalar exit, every finite matrix of
   \(\langle e_i,e_j\rangle-\langle T_t^0e_i,T_t^0e_j\rangle\)
   must be positive for every \(t\ge0\). These conditions are not supplied by completeness/minimality and have not been verified here. If the scalar-exit realization exists, its observation map gives the mode-preserving model realization; if these finite tests fail, the proposed one-exit conjecture is refuted in the given metric and must not be rescued by an unspecified change of norm. Any construction from support conditions must use the two-cutoff family \(L_{a,b}\), not the false dilation law for \(L_a\).

   **Status: OPEN.**

## What the numerics lane should check

The following decimal checks were computed in memory with python3/mpmath, at 55–60 decimal digits. They are checks of the identities, not substitutes for the proofs. The incomplete transform can be evaluated stably by the absolutely convergent incomplete-gamma series in T2(b); 12 terms suffice by a very large margin for the finite sample points below.

1. **Normalization at \(1\) and \(0\):**
   \(\theta(1)=1.08643481\),
   \(g(1)=-0.91356519\),
   \(\xi(1/2)=0.49712078\),
   \(\widehat g(0)=-7.95393245\),
   \(\widehat g_>(0)=-3.97696623\).

2. **Poles:** \((\tau-i/4)\widehat g(\tau)\to +i\), and
   \((\tau+i/4)\widehat g(\tau)\to-i\).
   Do not reverse the \(s=0,1\) correspondence.

3. **First zero and shifted points:** \(\gamma_1=14.13472514\),
   \(a_{\rho_1}=7.06736257\), and
   \(w_{\rho_1}=7.06736257+0.25000000i\).
   Check \(\widehat g(a_{\rho_1})=0\) and \(\Theta(w_{\rho_1})=0\) using high-precision zero data.

4. **Two different incomplete-transform checks:**
   \[
   \Lambda_>(1-\rho_1)=0.00000000+0.13055642i,
   \]
   \[
   \widehat g_>(w_{\rho_1})=\Lambda_>(i\gamma_1)
        =-0.00472327-0.13037495i.
   \]
   Also \(\Lambda_>(\rho_1)=-0.13055642i\), up to the zero-computation error.

5. **Other half values:**
   \(\Lambda_>(0)=-1.97818688\),
   \(\Lambda_>(-1)=-0.98031384\), and
   \(\widehat g_>(1)=-0.21322346-0.93622350i\).
   Direct logarithmic-coordinate quadrature agrees with the incomplete-gamma formula.

6. **Analytic zero-free bound:** on a sample grid \(\Re s<1\), check
   \(\Re[-(1-s)\Lambda_>(s)/2]\ge3-2\theta(1)=0.82713038\).
   The analytic proof holds for the whole half-plane, not just the grid.

7. **Different tail behavior:** for large real \(u\),
   \(u\widehat g_>(u)\to-0.91356519i\).
   The complete transform is exponentially small after a polynomial factor; it does not have the same tail.

8. **Edge quotient and elementary scattering factor:**
   \[
   \Theta(1)=0.99568001+0.09285107i,\qquad
   \varphi_E(1/2+i)=0.52312715-0.85225465i.
   \]
   Check \(\Theta=(\Lambda(1+2i\tau)/\Lambda(2i\tau))r\) and
   \(\varphi_E=r/\Theta\), including the removable values
   \(\Theta(0)=1\), \(\varphi_E(1/2)=-1\).

9. **Vertical behavior:** \(\Theta(i)=0.91228852\),
   \(\Theta(2i)=0.83502306\).
   The scaled quantities \(\Theta(iv)\sqrt{v/\pi}\) at \(v=10,100,1000\) are respectively
   \(0.91613809,\ 0.99128808,\ 0.99912538\).

10. **The two-dimensional theta constant term:** at \(y=2,t=3/4\), integration over \(x\in[0,1]\) should give \(1.66308355\). The second Poisson-rewritten channel is
    \(t^{-1}\theta(1/(ty))=1.66233249\);
    the brief's incorrect \(y\theta(1/(ty))\) is \(2.49349873\).
    Check the weighted involution \(t^{-1}C_y(1/t)=C_y(t)\), where \(C_y\) denotes the full constant term.

11. **Autocorrelation:** \(C(0)=\|g\|^2=3.91496941\),
    \(C(1)=3.82218144\), \(C(2)=3.58315109\).
    Stable physical-space evaluation uses \(g(e^X)\sim-e^{-|X|/4}\) to integrate the tails analytically. At a logarithmic cutoff \([-L,L]\), \(L>t\ge0\), their asymptotic contribution is \(4e^{-L/2}\cosh(t/4)\), with a super-exponentially small correction as \(L\to\infty\).

12. **Mode normalization:** for height \(1/4\), \(\|k_w\|^2=2.00000000\) with boundary measure \(du/(2\pi)\); at \(t=1\) the mode amplitude decays by \(e^{-1/4}=0.77880078\), and its squared norm by \(e^{-1/2}=0.60653066\). Include derivative kernels for a synthetic double zero when checking the Jordan rule.

13. **Burnol orientation and factor tests:** \(v_-(\tau)=(\tau+i/4)/(\tau-i/4)\), \(v_+=v_-^{-1}\). A synthetic zero \(\rho=\sigma+i\gamma\), \(\sigma>1/2\), maps to \(w_\rho^{(1)}=\gamma/2+i(\sigma-1/2)/2\) under the conjugate labeling. Check that \(v_+^2B_{\rm bad}^{-2}\) has twice the bad-zero pole order, while \(K_{B_{\rm bad}}\) uses the undoubled order. Synthetic off-line data are not evidence of actual off-line zeta zeros.

14. **Basis diagnostics:** the normalized-kernel overlap formula in T6(b) should approach \(1\) as a synthetic gap tends to zero; normalized consecutive derivative kernels have overlap \(\sqrt{(2j+1)/(2j+2)}\). Neither a well-conditioned small Gram matrix nor finitely many computed zeros proves an infinite Riesz-basis assertion.

15. **First falsification test for H-THETA-1:** if Sonine evaluator Gram data are available, test the finite contractivity matrices and the rank-one loss matrix in the restated problem, beginning with three distinct zeros. No positive answer is predicted here. A robust violation refutes that proposed realization in Burnol's norm, even though his completeness/minimality theorems remain true.
