# Resonances, transfer operators, and the missing Hermitian structure

Author: codex:gpt-6-astra  
Date: 2026-09-12  
Status: research notebook; mechanisms, counterexamples, and proposed tests, not proofs of RH.

Read against [HANDOFF](../../HANDOFF.md), [the ring/transfer dictionary](../what-rh-has-become.md), [the Riemann channel](../riemann-channel-note.md), [Weil positivity](../weil-positivity.md), [the Selberg dictionary](../selberg-dictionary.md), [Selberg T4–T5](../selberg/astra-proofs.md), [the SHW extract](../extract/shw-unbounded-generators-sources.md), and [today's worklog](../../docs/worklog/2026-09-12.md). No web access was used. A named literature check below is a task to check a theorem's hypotheses, not a claim to have fetched or verified it. Suzuki's formulas were checked directly in the existing [local TeX source](../../refs/src/2206.03682/screwz_15.tex).

## 0. Summary and ranking

**The resonance-to-transfer bridge already exists. What is missing is an arithmetic constraint on the coupling to the exit.** Compression, anisotropic spaces, and a return-map determinant can all turn resonances into spectral data. None generally makes their real parts equal. The useful question is which description exposes a relation between the primes and the cusp coupling that a generic open system does not satisfy.

Write a zero as \(\rho=\beta+i\gamma\), and its channel frequency and amplitude decay rate as

\[
a=\gamma/2,\qquad w=\beta/2,\qquad w_0=1/4.
\]

RH says \(w=w_0\); the functional equation pairs \(w\) with \(1/2-w\). Probability decays at rate \(2w\). Equal modal widths do **not** say that every state's norm decays exponentially at that rate: nonorthogonal modes interfere. Nor does RH alone give semisimplicity or an equivalent Hilbert norm making the infinite-dimensional generator normal.

My ranking is by potential to expose a missing identity, including the value of a decisive negative result:

| Rank | Mechanism | Leverage and present status |
|---:|---|---|
| 1 | §3: Mayer operator, cusp tail, and a Schur complement | An explicit arithmetic operator and an identifiable continuation problem; no width mechanism yet. |
| 2 | §1: one-port inverse scattering and the exit Gram matrix | Locates precisely how equal widths could coexist with rank-one loss; already gives useful obstructions. |
| 3 | §4: canonical systems and Suzuki's prime kernel | A concrete candidate for positive energy; positivity is currently an RH equivalent. |
| 4 | §5: time delay and removal of a common Poisson width | A measurable diagnostic and a numerical route to the same positivity question. |
| 5 | §6: Hecke symmetry and Ramanujan scattering | The strongest available arithmetic rigidity, but currently acting on the wrong spectral sector. |
| 6 | §2: Ruelle bands and a damping coboundary | A genuine mechanism for lines; the cusp extension is the missing step. |
| 7 | §7: SHW exit/reinsertion and critical BC renewal | A genuine new transfer process, but its reinsertion state is undetermined. |
| 8 | §9: isochronous graphs and uniform attenuation | Exact physical examples; their required equalities are absent from the prime circles. |
| 9 | §10: PT/Krein symmetry and a positive metric | Identifies the symmetry-breaking question; no arithmetic inequality supplied. |
| 10 | §11: noncommuting scattering chains and Thouless theory | Suggestive architecture; the actual local Euler phases are not local inner factors. |
| 11 | §14: graded transfer and relative cohomology | Explains the sign and cancellations; no modulus bound by itself. |
| 12 | §8: Feshbach reduction and complex scaling | Excellent bookkeeping for resonances; does not align widths. |
| 13 | §15: real-rootedness, interlacing, and heat flow | A known extremality technology with no identified prime ensemble. |
| 14 | §12: detailed balance and scalar-loss Lindbladians | Equal rates can be engineered, but usually for the wrong spectrum and exit multiplicity. |
| 15 | §13: conformal or thermal quasinormal modes | Real examples of width ladders, presently only an analogy for the archimedean part. |

**I would pursue §3 first**, using §1 as its diagnostic and §4 as its target. The task would be to isolate the Eisenstein/cusp part of Mayer's determinant with its exact Hurwitz-zeta tail, then identify the boundary pairing induced on that part. This uses \(ST^n\), the one cusp, and the actual scattering function together. Merely putting the known zeros into a Hermitian diagonal matrix would use none of that structure.

Two corrections govern the rest of the note. Positive canonical-system energy does not force every spatial transfer matrix to be elliptic. Also, equal-width poles with irregular positions can be realized by a one-channel passive system: the special information then lies in its couplings. Thus “GUE positions plus equal widths” is not uniquely a fingerprint of scalar physical loss.

## 1. A single exit, correlated couplings, and nonorthogonal modes

**1. Physics in elementary terms.** A cavity coupled to one lead loses amplitude through one boundary signal. Each closed-cavity mode couples differently to that signal, so its lifetime normally depends on its boundary amplitude. Equal lifetimes can nevertheless occur when the positions and boundary amplitudes obey a special collective relation.

**2. Which data this uses.** The scalar inner function \(S\), the one cusp, and the SHW exit map \(j\). The primes enter through the full scattering phase; a random-matrix cavity alone does not use them. Write the physical effective Hamiltonian as

\[
H_{\mathrm{eff}}=H-\frac{i}{2}vv^*,\qquad H=H^*.
\]

Then \(B=-iH_{\mathrm{eff}}\) is the convention \(B=iA_0-j^*j/2\) with \(A_0=-H\). The frequency sign is immaterial to the width question. In finite dimension its secular equation is

\[
1+\frac{i}{2}\sum_k\frac{|v_k|^2}{z-E_k}=0.
\]

The eigenvalues are not obtained by independently subtracting \(i|v_k|^2/2\) once resonances overlap. That formula is only weak-coupling perturbation theory.

**3. Where Hermitian structure could appear.** The closed \(H\) is already Hermitian. The new content would be an arithmetic formula for the spectral weights \(|v_k|^2\) that forces the secular roots to have the same imaginary part. Neither the scalar nature of the exit nor positivity of those weights forces it.

There is a useful inverse construction. Prescribe finitely many poles \(z_n=a_n-iw_n\), all below the real axis, and set

\[
P(z)=\prod_n(z-z_n)=U(z)+iV(z),
\]

where \(U,V\) have real coefficients. In the usual strictly stable polynomial setting, Hermite–Biehler interlacing gives real roots \(E_k\) of \(U\) and positive residues

\[
|v_k|^2=\frac{2V(E_k)}{U'(E_k)}.
\]

The matrix determinant lemma then recovers \(P\) as the characteristic polynomial of \(H-i vv^*/2\), with \(H=\operatorname{diag}E_k\). Thus an arbitrary finite collection of equal-width, non-lattice poles has a one-port realization. This is inverse design, not an explanation of why the arithmetic scattering data have that property.

The exit representation makes the price visible. For normalized eigenmodes \(u_n\) of \(B\), with eigenvalues \(-w_n+ia_n\), choose their phases so \(ju_n=\sqrt{2w_n}\). The integrated exit identity gives the Cauchy Gram matrix

\[
\langle u_n,u_m\rangle
=\frac{2\sqrt{w_nw_m}}
 {w_n+w_m-i(a_m-a_n)}.
\]

For equal widths, nearby frequencies give nearly parallel modes. In the physical cusp metric, equal widths therefore coexist naturally with substantial nonnormality. Scalar loss, \(B=-w_0I+iH\), would instead give \(B+B^*=-2w_0I\), which cannot be rank one on a space of dimension greater than one. Eigenvalue equality is much weaker than this operator identity.

**4. A concrete test.** An in-memory NumPy check prescribed

\[
a=(-2,-0.7,0.4,1.8),\qquad w_n=0.25.
\]

The inverse construction gave closed energies approximately
\((-2.089099,-0.730563,0.434737,1.884926)\), coupling squares
\((0.536036,0.463437,0.467190,0.533336)\), and the desired four poles to \(2.5\times10^{-15}\). Perturb these residues while holding the energies fixed; the equal widths should split. Compare weak coupling and overlapping resonances, rather than interpreting all deviations through first-order perturbation theory.

A second check used the cached ordinates, **assigned width \(1/4\)**, to form the Gram matrix above. For the first 24 ordinates its condition number was about \(9.88\); for the last 24 of the 3000-ordinate cache it was about \(701\). The largest neighboring overlap grew from about \(0.570\) to \(0.939\). These are checks of conditional mode geometry, not tests of RH.

**5. What kills it.** Choosing the residues after specifying equal-width poles merely rewrites RH. Random couplings do not supply the missing relation. At weak coupling, complex Gaussian boundary amplitudes give exponential partial-width statistics; the real-symmetry case gives the usual one-degree-of-freedom Porter–Thomas law. Calling all these laws “Porter–Thomas” hides the symmetry distinction. Strong coupling can instead produce one broad superradiant mode and many narrow modes. Nothing about one exit generically forbids that.

There is also a serious obstruction to a *bounded* change of metric on the existing \(K_S\). Under RH, fixed depth \(w_0\) and the increasing density of zero ordinates produce pairs of distinct frequencies with arbitrarily small separation, unless repeated zeros already create the Jordan issue. Their normalized kernel overlaps approach one. They cannot be images of mutually orthogonal eigenvectors under one bounded, boundedly invertible similarity. The relevant standard check is the Riesz-basis/interpolating-sequence theorem for model-space kernels. A new Hilbert–Pólya space could still exist, but an equivalent renorming of the entire physical model space is too strong a target. Finally, \(j\) is a boundary form in the infinite problem, not necessarily a bounded vector: finite trace identities such as \(\sum w_n=\|v\|^2/2\) must not be passed to infinity without a domain analysis.

## 2. Ruelle–Pollicott bands, uniform expansion, and a damping coboundary

**1. Physics in elementary terms.** A chaotic flow stretches a localized density into thin filaments, so smooth measurements lose memory even when microscopic motion is reversible. On spaces adapted to this stretching, the decay modes become eigenvectors of the transport generator. If the stretching and attenuation have sufficiently rigid averages, resonance bands can collapse to lines.

**2. Which data this uses.** Constant curvature of the modular surface, its geodesic flow, the transverse multipliers \(e^{\pm t}\), the Selberg tower, and the cusp. The primes enter only after identifying the scattering contribution, not by labeling every closed geodesic a prime.

The notebook's compact calculation has

\[
D(\sigma)=\prod_{j\geq1}Z_{\rm Sel}(\sigma+j),
\qquad
\Lambda_{\rm fl}=D'/D,
\]

and spectral locations \(-1/2-k\pm ir_j\). These are the flat-trace determinant's divisor under its stated compact hypotheses. T4 explicitly does not construct the anisotropic resolvent. For a modular scattering zero \(s_*=\rho/2\), the analogous tower bookkeeping would locate \(\sigma=s_*-j\), hence \(\operatorname{Re}\sigma=1/4-j\) under RH. This is a different family from the compact Laplace first band. It is not legitimate to replace one by the other.

**3. Where Hermitian structure could appear.** Uniform unstable expansion contributes a constant half-divergence to the effective damping in the familiar band picture. In constant curvature, representation theory relates appropriate bands to a self-adjoint Laplace problem. That explains the Laplace-derived lines; an outgoing Eisenstein state is not an \(L^2\) Laplace eigenfunction.

A more precise physical hope is a **cohomological attenuation identity**. If a weighted flow has potential \(V=c+Xf\), multiplication by \(e^f\), with the appropriate conjugation convention, removes its nonconstant part. The attenuation accumulated on any periodic orbit is then exactly \(c\) times its period. Livšic theory gives a standard test of this condition in compact hyperbolic settings. An arithmetic cusp analogue could be a genuine width mechanism if it were derived from the return dynamics and supplied a usable Hilbert metric.

However, constant curvature makes expansion uniform **per unit geodesic time**. It does not make cusp return times constant. Inducing the flow introduces an unbounded roof and boundary conditions, precisely where the missing information can reside.

**4. A concrete test.** Check Dyatlov–Faure–Guillarmou's constant-curvature resonance/Laplace correspondence, Faure–Tsujii's effective-damping band bounds, and the relevant Bonthonneau–Weich cusp resolvent theorem for their exact spaces, weights, thresholds, orbifold assumptions, and divisor statements. The first literature question is whether the modular scattering poles \(\rho/2\) are actual resonances of the particular scalar flow generator being used, or only appear in a related dynamical determinant after auxiliary factors and shifts.

For a computational test of a proposed coboundary, evaluate its integrated loss on periodic continued-fraction words. Already the fixed-digit words have geodesic lengths

\[
\ell_n=2\log\frac{n+\sqrt{n^2+4}}2.
\]

Compare total attenuation divided by \(\ell\) for words of lengths one, two, and three. One mismatch disproves that proposed periodic-orbit identity. Constant per-branch loss will fail because the roofs differ.

**5. What kills it.** Applying a compact theorem to the cusp without its domain and boundary terms. Even a valid cusp band estimate might give a strip, an asymptotic band, or only the discrete tempered sector. A spectral gap does not make every resonance sit on its boundary. An unbounded coboundary can also destroy bounded similarity, echoing §1. “Uniform curvature therefore RH” skips the entire scattering problem.

## 3. Mayer's operator as an induced cusp-return transfer operator

**1. Physics in elementary terms.** Record the system only when it returns to a cross-section. A long excursion is then one transition carrying both a return time and an amplitude. Summing over all excursions gives a transfer operator whose resolvent detects the same resonant feedback as the original open dynamics, provided the suspension and boundary bookkeeping are correct.

**2. Which data this uses.** The branches \(ST^n\), the continued-fraction/Gauss map, the one modular cusp, and

\[
(\mathcal L_s f)(z)
=\sum_{n\geq1}(n+z)^{-2s}
 f\!\left(\frac1{n+z}\right).
\]

The countable alphabet represents cusp excursions. The branch index \(n\) is an integer, not a prime. The prime data appear through the scattering determinant contained in the global Selberg object and through its logarithmic derivative.

The standard Mayer determinant identity, with the appropriate holomorphic space and meromorphic interpretation, is

\[
Z_{\rm Sel}(s)=\det(1-\mathcal L_s)\det(1+\mathcal L_s)
=\det(1-\mathcal L_s^2).
\]

A zero here is a solution of \(\lambda_j(s)=\pm1\), a **spectral-parameter-dependent pencil**. It is not the ordinary spectrum of one fixed \(\mathcal L_s\). Passing to a suspension generator, or explicitly linearizing a return-time problem, is part of the resonance-to-transfer bridge.

**3. Where Hermitian structure could appear.** This is the place to seek an adjoint identity involving orientation reversal, an Eisenstein pairing, and the cusp boundary form. The operator already contains the noncommuting modular branches. A factorization separating cusp forms from a boundary Schur complement could expose the arithmetic relation among the closed spectrum and exit weights sought in §1.

The tail is particularly concrete. For analytic \(f\), expanding near the cusp image \(0\) gives, initially in a convergence region,

\[
\sum_{n>M}(n+z)^{-2s}f((n+z)^{-1})
=\sum_{\ell\geq0}\frac{f^{(\ell)}(0)}{\ell!}
 \zeta(2s+\ell,M+1+z).
\]

The leading singular term at \(s=1/2\) factors through \(f(0)\), so its residue is rank one. The entire tail is not rank one. This distinction could connect one geometric exit with an infinite-dimensional return operator without inventing independent prime jump channels.

There is a plausible but unproved program: continue the tail exactly, identify the cusp boundary coordinate, and ask whether the remaining Schur complement admits a positive centered pairing that can be computed from its coefficients. If this works, it would turn an abstract positive kernel into a boundary-energy identity. That is the prospective mechanism; the determinant identity itself is only a bridge.

**4. A concrete test.** In the Taylor basis \((z-1)^k\), a finite section has explicit entries

\[
(L_s)_{mk}
=\frac{(-1)^m}{m!}
\sum_{\ell=0}^k(-1)^{k-\ell}\binom{k}{\ell}
(2s+\ell)_m\,\zeta(2s+\ell+m,2).
\]

This follows by expanding the branch functions; \((a)_m\) is the rising factorial. It is directly implementable with mpmath, with high precision needed for cancellations. Compare Taylor sizes 12, 20, and 32 near the first few \(s=\rho/2\), and increase precision independently of size. Track the \(+1\) and \(-1\) sectors and the corresponding near-null vectors. Extract their cusp evaluations and compare the local determinant divisor with \(\phi(s)\), allowing for zeros versus poles and nonzero analytic factors.

The named literature checks are Mayer's nuclear determinant theorem and the Lewis–Zagier/Chang–Mayer period-function correspondence, specifically its Eisenstein/resonance part and exceptional parameters. The worklog labels that latter identification as memory, so it remains to be checked.

**5. What kills it.** Cutting off branches and continuing the finite sum is not the same as continuing the infinite tail. At \(\operatorname{Re}s=1/4\), the leading branch sum no longer converges; a large integer cutoff can generate plausible-looking but spurious roots. A symmetric finite matrix obtained by ad hoc weights can also have no relationship to the original determinant. Finally, finding every tested root on a line says nothing about the required structural identity. The proposed result must identify a pairing or a constraint, not just redraw the known zeros.

## 4. Canonical systems, passive strings, and Suzuki's prime kernel

**1. Physics in elementary terms.** A one-dimensional wave can be propagated by multiplying small two-component transfer matrices. A positive local energy density gives a self-adjoint boundary-value problem and a passive response function. An inverse problem asks whether measured scattering data come from such positive local energy.

**2. Which data this uses.** The full completed scattering phase, the explicit formula, and the prime weights with their archimedean and pole terms. The canonical-system model is

\[
JY'(x,z)=z\,\mathsf H(x)Y(x,z),
\quad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\quad \mathsf H(x)\geq0.
\]

The Hamiltonian here is a matrix density, not the channel generator. Suitable endpoint conditions give a self-adjoint spectral problem; the Weyl function belongs to the Herglotz class.

There are **two different inverse problems**. A Cayley transform of the already-inner \(S\), with the half-plane convention chosen correctly, produces passive Herglotz data unconditionally. That construction cannot prove RH. The centered function

\[
Q_\xi(z)=i\frac{\xi'}{\xi}\!\left(\frac12-iz\right)
\]

is Herglotz exactly under RH, as recorded in Suzuki's local source through Lagarias's criterion. A positive canonical realization of this centered response is a much stronger statement than a passive realization of \(S\).

**3. Where Hermitian structure could appear.** The promising object would be a prime-defined positive energy density realizing \(Q_\xi\), obtained independently of zero locations. Suzuki gives a particularly concrete intermediate object. With \(g=-\Psi\), its kernel is

\[
G_g(t,u)=g(t-u)-g(t)-g(-u)+g(0)
=\Psi(t)+\Psi(u)-\Psi(t-u),
\]

where \(\Psi\) is even and \(\Psi(0)=0\). Global nonnegative definiteness is equivalent to RH. Under RH it is the Gram kernel of vectors with components
\((e^{i\gamma t}-1)/\gamma\). Off RH, the spectral coordinates called \(\gamma\) in Suzuki's source can be complex; replacing them by imaginary parts of zeros would silently assume the conclusion.

The physical opportunity is a local assembly law for this energy: a factorization, an increasing family of positive boundary energies, or a canonical-system reconstruction whose positive coefficients follow from arithmetic. Calling it “a positive-mass prime string” is currently a description of the desired extremal object. A general canonical system is broader than a scalar Krein string; a literal nonnegative string mass needs the additional Stieltjes/symmetry hypotheses of the relevant inverse theorem.

The seed's proposed implication about monodromy is false. Positive \(\mathsf H\) does not make every transfer matrix similar to a unitary. For real \(z\), the transfer preserves the flux form, equivalently the indefinite Hermitian form \(iJ\); periodic positive media still have forbidden bands. Take two constant slabs

\[
\mathsf H_1=\operatorname{diag}(4,1/4),\qquad
\mathsf H_2=\operatorname{diag}(1/4,4).
\]

At \(z=1\), each with length \(\pi/2\), the transfer is \(-J\mathsf H_j\). Their product is
\(\operatorname{diag}(-16,-1/16)\), manifestly off the unit circle. The relevant positivity must belong to the **spectral operator or its boundary response**, not to an arbitrary spatial monodromy. The inverse-pairing/adjoint-pairing analogy is useful only with that distinction.

**4. A concrete test.** Evaluate Suzuki's prime formula and form finite kernel matrices; §16 specifies the formula and a reproducible grid. Attempt a high-precision factorization and inspect how its coefficients change when the interval grows past \(\log p^k\). The first useful discovery would be an arithmetic recurrence for the factors, not another numerical positive matrix.

Literature checks: the precise de Branges inverse theorem for the chosen normalization of a Herglotz function, Krein–Langer's screw-function correspondence, and the narrower inverse string theorem if a scalar mass is claimed. Suzuki's local TeX already verifies the RH/positive-kernel equivalence; that part need not be fetched again.

**5. What kills it.** Reconstructing a positive Hamiltonian after assuming the centered function is Herglotz is circular. Positivity on one finite interval is insufficient, and Suzuki even has unconditional positivity on sufficiently small intervals. Positivity of the uncentered passive response is irrelevant to the missing bound. A failed Cholesky step at floating-point precision is also not a negative Weil vector until truncation and cancellation errors are controlled.

## 5. Wigner delay: common Lorentzian broadening and a width-sensitive observable

**1. Physics in elementary terms.** A resonance delays a reflected wave packet, producing a Lorentzian peak in the derivative of its scattering phase. A common resonance width means that every peak is the same broadening kernel placed at a different frequency. Removing that common broadening would reveal a positive sharp frequency spectrum if RH holds.

**2. Which data this uses.** Real-axis values of \(S\), its phase from the primes, the archimedean completion, and the explicit formula. Use the positive-delay convention for a lower-half-plane inner function,

\[
q_S(x)=-\frac{d}{dx}\arg S(x)
=4\operatorname{Re}\frac{\xi'}{\xi}(1+2ix).
\]

The Blaschke contribution of \(a-iw\) is

\[
\frac{2w}{(x-a)^2+w^2}.
\]

For the completed xi ratio, its algebraic large-depth behavior removes an additional exponential-inner delay term. The resulting pole sum is positive whether or not \(w=1/4\).

The completion matters physically. With \(\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)\), direct algebra gives

\[
S(x)=\frac{x+i/2}{x-i/2}\,
\phi\!\left(\frac12+ix\right),
\qquad
q_S(x)=q_\phi(x)+\frac1{x^2+1/4}.
\]

Thus positivity of the completed model delay is not an unconditional positivity assertion for every convention of physical cusp delay. In T5's convention, \(q_\phi=2m\); its Fourier transform has the prime dips, archimedean part, and the pole boundary constant. Those terms cannot be discarded when comparing signs.

**3. Where Hermitian structure could appear.** Under RH,

\[
q_S=2\pi P_{1/4}*\mu,
\qquad P_w(x)=\frac{w}{\pi(x^2+w^2)},
\qquad \mu=\sum_n\delta_{a_n}.
\]

The measure \(\mu\) would be the density of states of a Hermitian system. Ordinary passivity says only that the *broadened* delay is positive; the extra statement is positivity after removing precisely width \(1/4\). In Fourier variables this removal is multiplication by \(e^{|t|/4}\), hence exponentially ill-conditioned.

This is a useful observable formulation, but presently an RH reformulation. For the full infinite distribution, multiplication by \(e^{|t|/4}\) at its singular origin needs a specified regularization; it is not an automatic operation on arbitrary distributions. Integrating twice and using Suzuki's kernel is a cleaner way to implement the same question on compact test supports.

**4. A concrete test.** Direct mpmath differentiation at 40 decimal digits gave

| \(x\) | \(q_S(x)\), directly from xi | 3000 positive ordinates and their negatives, all given width \(1/4\) |
|---:|---:|---:|
| 0.3 | 0.0925432753 | 0.0912224065 |
| 7.1 | 8.0021824244 | 8.0008615362 |

The residual is approximately \(0.00132088\) in both cases, consistent with a slowly varying omitted high-frequency tail. This calibrates the normalization; it is not evidence beyond the zeros put into the comparison.

For a genuine sensitivity check, replace an equal-width pole pair in a finite synthetic model by widths \(1/4\pm\epsilon\), retaining the functional-equation pairing. The raw delay remains positive. Search for a negative direction only after common-width removal or in its integrated kernel. Compare how long a time interval is needed as \(\epsilon\) decreases.

**5. What kills it.** Treating \(q_S\geq0\) as Weil positivity. It holds for all passive inner models. A finite-window fit by equal Lorentzians is not unique enough to establish a global line, and deconvolution amplifies tiny errors. No fixed low-order delay moment should be expected to distinguish every possible distant off-line pair. An exact all-test-function criterion is again RH, unless its sign follows from a new prime identity.

## 6. Arithmetic quantum chaos, Hecke symmetry, and “Ramanujan for a lead”

**1. Physics in elementary terms.** Arithmetic symmetry can constrain transport much more strongly than generic chaotic mixing. In a closed expander those constraints can exclude modes outside the spectrum allowed by the infinite covering tree. Opening a lead changes the boundary-value problem, so the same symmetry need not control the continued scattering poles.

**2. Which data this uses.** The modular Hecke operators, Eisenstein series, the single cusp, and the notebook's exactly Ramanujan Weil–LPS channels. This is the most direct place to seek arithmetic input beyond the functional equation.

On an Eisenstein family, a common normalization gives the Hecke eigenvalue

\[
t_p(s)=p^{s-1/2}+p^{1/2-s}.
\]

On the physical line \(s=1/2+ir\), it is \(2\cos(r\log p)\), as expected from unitary principal series. At a Riemann scattering pole \(s=\rho/2\), even **under RH** the same expression is

\[
p^{-1/4+i\gamma/2}+p^{1/4-i\gamma/2},
\]

which is generically complex. Thus the continued cusp state cannot simply inherit the original self-adjoint Hecke action in a positive Hilbert space.

**3. Where Hermitian structure could appear.** A new boundary representation might have centered local parameters \(p^{\rho-1/2}\) and their inverses. Under RH these are unimodular. To make this a mechanism one must construct that representation and its positive form from the cusp data, rather than assign the desired parameters to its spectrum.

“Ramanujan for a lead” should consequently distinguish two questions. Temperedness of the physical continuous spectrum is already a unitary representation statement. A resonance Ramanujan property would be a bound on poles of its **continued boundary response**, after a specified centering and subtraction of trivial factors. The first does not imply the second. A complete graph-with-leads definition would have to specify the coupling, scattering variable, trivial poles, and reciprocal pairing before stating a bound.

The random-matrix language also needs restraint. Poisson-like statistics of arithmetic Laplace spectra and GUE-like statistics of zeta ordinates are different conjectural statistical statements; Hecke commutativity alone does not prove the former. Nor does GUE-like zero spacing establish that a physical cusp cavity literally belongs to a time-reversal-broken ensemble. In particular it supplies no prohibition of superradiance.

**4. A concrete test.** Use the Hermitian adjacency operator behind a small existing Weil–LPS example, attach one vector \(v\), and calculate \(H-i\eta vv^*/2\) as \(\eta\) varies. Compare a basis-vector attachment, a symmetry-adapted attachment, and a generic attachment. The closed Ramanujan bound should survive as a statement about \(H\), while the resonance widths generically vary and may segregate at strong opening.

For the modular system, evaluate \(t_p(\rho/2)\) for the first few verified critical zeros and two primes. This cheap calculation exposes why ordinary Hecke self-adjointness cannot simply be continued. The useful literature check is the Maass–Selberg relation and the normalized intertwining operator on principal series, including what becomes of its positive form off the unitary axis.

**5. What kills it.** Substituting Selberg's discrete \(1/4\) property for RH, or importing Deligne's bound from the compact finite-field object without identifying the cusp sector. A generic opening destroys the proposed width property while retaining the arithmetic closed operator. The notebook's \(S,T,T^{-1}\) channels already warn that even the choice of modular generators does not automatically give the required Ramanujan bound.

## 7. SHW renewal: exit at the cusp and reinsertion

**1. Physics in elementary terms.** An open-system trajectory evolves without an event until it reaches the exit. One can turn repeated exits into a conservative process by preparing a new state each time an exit occurs. The resulting renewal process has its own transfer spectrum, determined by the distribution of return times.

**2. Which data this uses.** The already-existing no-event semigroup \(Z(t)\), its one-dimensional exit space, SHW reinsertion, and a possible relation to the critical Bost–Connes process. On density operators, a finite-dimensional version is

\[
\mathcal L_\Omega(\rho)
=B\rho+\rho B^*
+\operatorname{tr}(j\rho j^*)\,\Omega,
\quad \Omega\geq0,\quad\operatorname{tr}\Omega=1.
\]

The scalar exit does not determine \(\Omega\). The arrival density is

\[
m_\Omega(t)=\operatorname{tr}
 \bigl(jZ(t)\Omega Z(t)^*j^*\bigr),
\]

and the nontrivial feedback denominator is \(1-\widehat m_\Omega(\lambda)\). A resolvent calculation must also track cancellations and modes not coupled to the reinsertion functional; the full spectrum is not simply a list of roots of that scalar equation.

**3. Where Hermitian structure could appear.** A distinguished arithmetic rebound state might make the renewal kernel satisfy a detailed-balance or reflection identity. That would be a new object built from the available exit, rather than an attempt to identify prime jumps inside a pure no-event evolution. Its missing input is precisely the rebound state and the reason for choosing it.

There are two caveats to today's informal discussion. First, jump representations have gauge freedoms, including dynamically trivial scalar jumps; the useful negative statement is that adding genuine reinsertion changes the no-event map, not that every displayed nonzero Kraus term must visibly mix every state. Second, in an unbounded problem, a trace-preserving formal reinsertion rule is not by itself a proof that the minimal semigroup is conservative for all times. Explosion and domains are exactly SHW's point.

At the BC threshold there is an additional difficulty. The measure

\[
\nu_\sigma=\sum_{p,k}\frac{p^{-k\sigma}}k\delta_{k\log p}
\]

has finite mass for \(\sigma>1\). At \(\sigma=1\), its divergence is at arbitrarily **large** jump lengths; the lengths are bounded below by \(\log2\). This is not ordinary infinite activity from small jumps satisfying the usual Lévy integrability condition. Indeed, the normalized characteristic function \(\zeta(\sigma-it)/\zeta(\sigma)\) tends to zero for fixed nonzero \(t\), and to one at \(t=0\): no continuous probability characteristic function on the same real dilation group results. A critical completion therefore needs a new state space or compactification, not just compensation of small jumps.

**4. A concrete test.** In the finite one-port model of §1, construct \(\mathcal L_\Omega\) explicitly on matrices. Compare a maximally mixed rebound, a closed-energy eigenstate, and a chosen coherent rebound. Check trace preservation and the renewal resolvent denominator, then compare their eigenvalues with the unchanged no-event poles. This can be implemented with NumPy Kronecker products and quadrature of \(m_\Omega\).

The genuinely arithmetic test is whether a cutoff BC state induces an \(\Omega\) on the cusp model that has a tight limit. Test normalization and escape of mass before testing any spectral conjecture. The relevant SHW statements are already locally available, including the caveat about infinitesimal trace preservation.

**5. What kills it.** Arbitrarily choosing \(\Omega\) can tune the renewal spectrum while leaving \(S\) fixed. That would explain a designed process, not RH. Under RH each individual eigenmode has the same exponential arrival-density rate \(1/2\), but a coherent superposition need not have an exponential waiting-time distribution. Confusing those two claims would build the desired renewal law into the assumptions. A non-tight critical BC limit can kill the proposed completion before the width question arises.

## 8. Feshbach reduction, complex scaling, and outgoing boundary conditions

**1. Physics in elementary terms.** Eliminate the lead from a self-adjoint system and the cavity acquires an energy-dependent complex boundary term. Alternatively, deform outgoing waves so that they become square-integrable; resonances then appear as eigenvalues of a deformed non-self-adjoint operator. Both constructions explain how real-energy unitary physics produces complex poles.

**2. Which data this uses.** The self-adjoint modular wave/Laplace problem, the cusp's zero Fourier mode, \(\phi(s)\), and the Lax–Phillips compression. In block notation, the effective operator is schematically

\[
H_{\mathrm{eff}}(z)
=PHP+PHQ(z-QHQ)^{-1}QHP.
\]

Its boundary value and continuation encode the outgoing self-energy. One propagating channel can make that boundary coupling scalar without making the self-energy constant in \(z\).

**3. Where Hermitian structure could appear.** The original total Hamiltonian is Hermitian, and this supplies a flux identity and adjoint relations between incoming and outgoing problems. The outgoing condition itself is not self-adjoint. To force equal widths, one would need a special arithmetic identity for the continued self-energy; a unitary dilation by itself supplies none.

There is a tempting but misleading Mellin association in the seed. In the cusp coordinate \(r=\log y\), \(y\mapsto e^{i\theta}y\) is \(r\mapsto r+i\theta\), a complex **translation**. It multiplies Mellin waves by a factor but is not automatically the exterior rotation \(r\mapsto e^{i\theta}r\) that rotates the kinetic continuous spectrum. Analytic dilation of an operator family, continuation in a spectral Mellin variable, and continuation in BC inverse temperature are three different operations.

**4. A concrete test.** Solve a one-dimensional interval attached to a half-line, with a real cavity potential and an outgoing Robin or Dirichlet-to-Neumann condition at the junction. Compare its resonance roots from direct matching, a Feshbach self-energy, and a complex-scaled discretization. The pole positions should agree in the permitted sector and be independent of the scaling angle, while widths vary with the cavity data.

For the modular cusp, derive the outgoing boundary form for the zero Fourier mode in \(r\), then check the exact Laplace-to-wave-to-\(\tau\) parameter changes. The named theorem to inspect is Aguilar–Balslev–Combes or an appropriate exterior-complex-scaling theorem for cusp ends; the Euclidean theorem cannot simply be quoted with no cusp hypotheses.

**5. What kills it.** Complex scaling exposes existing poles and does not move them onto a new line. Choosing a contour angle to make a numerical spectrum look horizontal changes its representation, not its physical widths. Identifying the deformation parameter with BC temperature without an intertwining formula is only a resemblance between Mellin variables.

## 9. Isochronous networks, one-way circulation, and uniform attenuation

**1. Physics in elementary terms.** A wave circulating around a loop encounters the same attenuator once per circuit. Every Fourier mode then loses the same fraction of amplitude in the same time. More generally, a unitary quantum map followed by a scalar attenuation has equal decay per step for all modes, however irregular their phases are.

**2. Which data this uses.** The notebook's prime circles, the distinction between an orbit trace and a transfer spectrum, and the intuition of one exit. A circle of length \(L\) with amplitude return factor \(r\), \(|r|<1\), has generator eigenvalues

\[
\lambda_n=\frac{\log r+2\pi i n}{L},
\qquad \operatorname{Re}\lambda_n=\frac{\log|r|}{L}.
\]

This is a genuine one-port equal-width mechanism. In a discrete map,
\(T=rU\), \(U^*U=I\), gives the same statement per iteration. The eigenphases of \(U\) need not be a lattice.

**3. Where Hermitian structure could appear.** A loss profile that is a coboundary plus a constant per unit travel time can be absorbed into a change of amplitude normalization. For a network, every periodic trajectory must have the same integrated loss divided by its travel time. Isochronous travel and scalar attenuation provide a sufficient realization; a single physical opening in a generic network does not.

The useful possibility is that the arithmetic return dynamics admit exactly such a cohomological attenuation identity, even though it is hidden in physical coordinates. This is the elementary counterpart of §2 and the residue constraint of §1. The circle example proves that one exit is not itself an obstruction.

**4. A concrete test.** Construct an equilateral quantum graph with unitary vertex scattering \(U\) and one-step propagation \(r e^{ikL}U\). Solve
\(\det(1-r e^{ikL}U)=0\), and then perturb one edge length or one attenuation. A common line persists only for perturbations respecting the loss-per-time identity. For prime circles, impose \(|r_p|=e^{-w_0L_p}\) and verify the equal-width lattice families explicitly.

Then compare the resulting determinant's divisor with xi. This last check matters more than the easy width check: the circle model still has local lattice modes, not zeta zeros.

**5. What kills it.** Picking \(r_p\) to produce the desired decay simply builds the answer into independent circles. Their direct sum remains side A and cannot supply the zero spectrum. With unequal return times, equal loss per branch is insufficient. With uniform loss in a quantum map, one must also explain why its trace is the prime measure with the explicit formula's signs and smooth terms. No such map is currently given.

## 10. PT symmetry, Krein signatures, and the transition to a positive metric

**1. Physics in elementary terms.** A system with paired amplification and attenuation can have real frequencies over part of its parameter range. When modes of opposite indefinite signature collide, they can leave the real axis as a conjugate pair. The symmetry protects the pairing, while an additional inequality determines whether the system remains in the real-frequency regime.

**2. Which data this uses.** The functional-equation reflection, the inverse-paired Kraus construction, and the finite-dimensional Hilbert–Pólya metric criterion proved this afternoon. Center the amplitude generator:

\[
C=B+w_0I,\qquad K=-iC.
\]

The functional equation produces conjugation pairing for the eigenvalues of \(K\), with the appropriate frequency/conjugation convention. It does not, merely as a statement about the divisor, construct an explicit operator \(P\), antiunitary symmetry, or indefinite form.

**3. Where Hermitian structure could appear.** If one could exhibit

\[
K^*G=GK,\qquad G>0,
\]

then \(K\) would be self-adjoint in that metric in the finite-dimensional setting. An indefinite \(G\) only gives a Krein-space problem, where complex eigenvalues are allowed. The missing physics would be an arithmetic bound that prevents the relevant signatures from colliding, or directly makes the boundary form definite.

The elementary example is

\[
K=\begin{pmatrix}ig&t\\t&-ig\end{pmatrix},
\qquad \operatorname{spec}K=\{\pm\sqrt{t^2-g^2}\}.
\]

The symmetry holds for all \(g\), but reality only for \(|g|\leq|t|\). At the nontrivial threshold there is a Jordan block, so reality alone does not give a positive metric. This is precisely why semisimplicity matters in the notebook's theorem.

**4. A concrete test.** Use finite sections of a candidate centered cusp operator and solve the linear equations \(K^*G=GK\). Examine whether the solution cone contains a positive matrix, and how the best achievable condition number grows with cutoff. Compare with the exit Gram matrix in §1 and with an explicit off-line paired perturbation. A numerical positive solution obtained only after fitting known critical zeros has no evidentiary value; the relevant input is a prime- or branch-defined operator.

The literature check is the precise finite-dimensional quasi-Hermitian criterion and its infinite-dimensional bounded-similarity limitations, not a generic claim that PT symmetry implies real spectrum.

**5. What kills it.** “Unbroken PT symmetry” can simply be another name for RH. Functional-equation symmetry supplies no analogue of \(|g|\leq|t|\). An indefinite invariant form is not a positive Weil form. Even positive metrics for all finite sections may become singular in the limit, and §1 gives a concrete reason to expect that for the physical model-space eigenvectors.

## 11. Factorized scattering, noncommuting chains, and a Thouless reading

**1. Physics in elementary terms.** Waves traveling through several scatterers acquire multiple-reflection amplitudes described by products of two-component transfer matrices. Their spectral growth can be related to a density of states through a logarithmic-potential identity. Scalar phase factors capture much less information because they have no noncommuting internal reflection structure.

**2. Which data this uses.** The Euler product, prime lengths, the BC phase, and the Hadamard product for xi. The local-factor convention in the seed needs correction. Put

\[
u_p=e^{-2i\tau\log p},\qquad a_p=p^{-1}.
\]

In the lower half-plane \(|u_p|<1\). The actual local factor in the zeta-phase ratio is

\[
R_p(\tau)=\frac{1-a_pu_p}{1-a_p/u_p}
=\frac{u_p}{b_p(\tau)},
\qquad
b_p(\tau)=\frac{u_p-a_p}{1-a_pu_p}.
\]

Here \(b_p\) is inner, with zeros on \(\operatorname{Im}\tau=-1/2\); **\(R_p\) is not inner** and instead has poles there. Its boundary values are unimodular. In this doubled variable the lattice period is \(\pi/\log p\), corresponding to time length \(2\log p\).

Thus the completed global \(S\) is not a straightforward convergent product of the local inner \(b_p\). The Euler expression is used in its convergence or boundary/Abel sense; continuation through the strip is a global operation involving the completion. A partial Euler product cannot be treated as a normal family converging to the continued inner function throughout that strip.

**3. Where Hermitian structure could appear.** A genuine noncommuting transfer chain might replace the scalar factors by matrices whose boundary determinant has the required phase. A self-adjoint Jacobi or canonical realization would then provide a positive density of states. In a standard ergodic Jacobi setting, the Thouless formula has the shape

\[
L(E)=\int\log|E-x|\,dN(x)-\mathbb E\log|a|.
\]

The analogy with Hadamard equals Euler is appealing: one side is assembled locally, the other reads a spectral logarithmic potential. But the theorem assumes an actual self-adjoint chain, an integrated density of states, and a controlled limiting process. Those objects do not come from relabeling the Euler product. If the measure in the logarithmic potential is already declared to live on real centered zero frequencies, RH has been assumed.

Factorized integrable S-matrices provide another warning. Factorization and unitarity do constrain poles and residues, but do not generally put all resonances at one distance from the physical axis. A Yang–Baxter relation would need explicit local internal spaces and scattering maps; scalar arithmetic phases alone satisfy no useful version of this missing structure.

**4. A concrete test.** A direct local check for \(p=2\), \(\tau=-iy\), gave

| \(y\) | \(|R_2|\) | \(|b_2|\) |
|---:|---:|---:|
| 0.25 | 2.20711 | 0.320377 |
| 0.49 | 54.2234 | 0.00934983 |
| 0.51 | 53.9735 | 0.00913627 |

This rules out the local-inner claim for the actual Euler phase convention. For any proposed matrix replacement, compute its finite-chain determinant, compare its boundary phase to the partial arithmetic phase, and check the dependence on ordering. Noncommutativity introduces new data: the order and reflection amplitudes must be specified arithmetically.

**5. What kills it.** Commuting factors retain the prime-circle spectrum. Arbitrary noncommuting factors add information not supplied by the primes. A Furstenberg Lyapunov exponent generally measures exponential growth, not exact unit-circle transfer eigenvalues; randomness can produce localization rather than a Ramanujan property. Invoking Thouless theory before constructing its self-adjoint chain only repackages the desired positive measure.

## 12. Detailed balance and scalar-loss quantum Markov models

**1. Physics in elementary terms.** A reversible Markov process has a symmetric dissipative part after weighting states by equilibrium probabilities. If the damping acts equally on every nonstationary mode, all relaxation rates coincide. Coherent Hamiltonian motion can then add oscillation frequencies without changing those rates.

**2. Which data this uses.** The channel/MPS language, the distinction between no-event and full dynamics, and BC KMS states. A finite-dimensional example is depolarization plus Hamiltonian motion:

\[
\mathcal L(\rho)=-i[H,\rho]
+\kappa\bigl(\operatorname{tr}(\rho)I/N-\rho\bigr).
\]

Coherences have eigenvalues \(-\kappa-i(E_m-E_n)\), and the traceless diagonal sector has eigenvalue \(-\kappa\). This is a real structural source of equal decay rates.

**3. Where Hermitian structure could appear.** Detailed balance supplies a positive equilibrium metric for a dissipator, while the Hamiltonian part is antisymmetric in a compatible metric. To get one common real part, the dissipator must be scalar on the relevant sector and commute appropriately with the coherent part. Detailed balance alone leaves arbitrary real relaxation rates.

The comparison also distinguishes two spectra that are easy to confuse. The amplitude generator \(B\) has one mode per zero. Its density-operator no-event lift has combinations \(\lambda_m+\overline{\lambda_n}\); under RH their real parts are \(-1/2\), not \(-1/4\), and their frequencies are differences. A depolarizing model naturally constructs this much larger kind of spectrum. It does not directly construct the desired amplitude frequencies.

**4. A concrete test.** Build the depolarizing example for an irregular Hermitian \(H\), then compare its full Liouville spectrum, the chosen no-event part in a specified jump gauge, and a one-port rank-one-loss model. Count multiplicities and exit dimensions as well as real parts. A proposed BC detailed-balance construction should be subjected to the same comparison, with the equilibrium state explicitly written.

**5. What kills it.** A KMS state or a symmetric dissipator does not impose scalar damping. A many-jump scalar-loss model may have the wrong exit multiplicity, and its density-operator spectrum has the wrong count and difference structure. The inner product from a channel's stationary state does not automatically make its subleading amplitude transfer generator Hermitian. The easy mechanism exists, but identifying it with the Riemann channel is the entire problem.

## 13. Thermal and conformal quasinormal modes

**1. Physics in elementary terms.** Near certain horizons or scale-invariant boundaries, wave propagation reduces to equations controlled by dilation symmetry. Thermal periodicity and representation theory then organize quasinormal poles into evenly spaced damping ladders. Their widths are fixed by temperature and scaling dimensions rather than by random boundary overlaps.

**2. Which data this uses.** The hyperbolic cusp, Mellin/dilation variables, the archimedean gamma factor, and the BC temperature parameter as a possible comparison. It currently uses almost none of the nontrivial arithmetic data.

**3. Where Hermitian structure could appear.** In suitable conformal examples, a thermal correlator involves a ratio of gamma functions and has pole families schematically of the form

\[
\omega=\omega_{\rm spatial}-i\,2\pi T(n+h).
\]

The exact coefficients, sectors, and cancellations depend on the model. The gamma-function pole ladder has a genuine representation-theoretic explanation. A positive underlying Hilbert space fixes allowed dimensions, while the outgoing or thermal prescription makes the observed frequencies complex.

This is suggestive for the archimedean towers and the half-divergence shifts in §2. It does not explain why the irregular arithmetic resonance set occupies one particular row. A positive Hilbert space for the underlying thermal system still permits many distinct widths.

**4. A concrete test.** Check one precise example: scalar quasinormal modes of the BTZ black hole, or the retarded two-point function of a specified two-dimensional conformal primary. Compare its exact gamma divisor with the gamma and rational factors of \(\phi\) and \(S\). Then divide those known factors out and ask whether any predicted pole structure survives in the zeta part. This is a specific divisor comparison, not a proposed identification of physical spacetimes.

**5. What kills it.** Matching the archimedean factor only explains poles already known to be non-arithmetic. Thermal poles usually form an infinite ladder, while RH specifies the widths of a different selected family. Equating a BC critical temperature with a horizon temperature without an operator or correlation-function identity supplies no mechanism. This ranks low because the primes have not entered.

## 14. Graded transfer, cohomology, and cancellation of resonance towers

**1. Physics in elementary terms.** In a graded system, bosonic and fermionic fluctuation modes contribute determinants with opposite signs. A symmetry can pair and cancel many modes, leaving a smaller effective spectral sector. This explains why an orbit-counting partition function can be governed by zeros of a reduced determinant rather than by the full microscopic spectrum.

**2. Which data this uses.** The minus sign of the nontrivial zeros in the explicit formula, the ring/transfer distinction, the Selberg tower, and the Ruelle quotient

\[
\zeta_R(s)=\frac{Z_{\rm Sel}(s)}{Z_{\rm Sel}(s+1)}
\]

in the notebook's direct-product convention. It also uses the finite-field analogy, where cohomological grading and weight bounds are distinct ingredients.

**3. Where Hermitian structure could appear.** A complex of transfer operators on differential forms can make the tower cancellations operator-theoretic. A relative or boundary complex for the cusp might isolate the scattering sector that a naive \(L^2\) Laplacian misses. If it also carried a positive pairing compatible with a centered evolution, that would be an actual candidate bond space.

But an outgoing resonant state has boundary flux. The positive \(L^2\) Hodge inner product and a residue pairing on boundary distributions are not interchangeable. Nilpotency or supersymmetric cancellation does not automatically turn the latter positive. The finite-field lesson is precisely that rationality, duality, and the sign are cheaper than the weight bound.

**4. A concrete test.** Starting from the notebook's flat-trace weights, compute the alternating exterior-power transverse traces and check exactly which factors of \(D\) cancel. Track the modular cusp divisor separately from the compact Laplace divisor. The literature check is the dynamical determinant/resonant-state complex for geodesic flow, followed by a cusp version with explicit boundary conditions. A valid reduction should reproduce the scattering factor and the corrected signed prime contribution, including the archimedean and pole terms.

**5. What kills it.** Cancellation can remove or retain poles but cannot move a surviving off-line pole onto a line. Grading explains the minus sign, not the modulus. A cohomological description that silently discards the cusp resonance sector proves a statement about the wrong object. SPT protection of signs and phases, already rejected in the worklog as a route to moduli, is not revived by changing its vocabulary to supersymmetry.

## 15. Real-rootedness, interlacing, and a heat-flow threshold

**1. Physics in elementary terms.** Some disordered systems have characteristic polynomials whose average remains real-rooted because the local randomness obeys a special interlacing structure. A heat deformation of an entire spectral function can likewise have a sharp threshold beyond which its zeros are all real. Such mechanisms turn spectral extremality into a stability question for a family of objects.

**2. Which data this uses.** The completed xi function, the suggestion in HANDOFF that an expected characteristic polynomial might provide the missing Hermitian structure, and the analogy with Marcus–Spielman–Srivastava. The primes would have to determine the local random operators or the deformation law; no such model is currently specified.

**3. Where Hermitian structure could appear.** A mixed characteristic polynomial built from independent positive rank-one data has special real-rootedness properties. If a regularized limit of such polynomials were the centered xi function and the limit preserved its divisor, the Hermitian structure would be explicit. This is a genuine type of mechanism in other problems.

It is emphatically not enough that every matrix in an ensemble be Hermitian. The equally weighted ensemble \(H=I_2\) or \(H=-I_2\) has average characteristic polynomial

\[
\tfrac12(x-1)^2+\tfrac12(x+1)^2=x^2+1,
\]

which has no real zeros. The special interlacing/independence assumptions carry the theorem.

The de Bruijn–Newman deformation is another useful framing: in a fixed normalization, multiply the Fourier kernel of xi by a Gaussian heat factor and ask when all transformed zeros become real. RH becomes an assertion about the location of the undeformed function relative to that threshold. Naming the threshold does not explain its value. The precise normalization and the de Bruijn, Newman, and Rodgers–Tao theorems are literature checks here, not ingredients imported without inspection.

**4. A concrete test.** First reproduce the \(\pm I_2\) counterexample and a small genuine MSS mixed characteristic example in SymPy. Then ask whether any finite prime construction gives the latter's algebraic form, with the correct trace coefficients and a controlled limit. Alternatively, inspect Jensen polynomials associated with xi as a diagnostic, while keeping their finite-degree and asymptotic implications distinct from all-real zeros of xi itself.

**5. What kills it.** A positive Fourier kernel alone need not have a Fourier transform with only real zeros. Finite Euler products and Taylor truncations do not automatically preserve the relevant zero geometry under continuation. Without an arithmetic ensemble or a monotonicity law fixing the heat threshold, both proposals reduce to another real-rootedness statement equivalent to RH. They remain worthwhile technologies to recognize, but not the first thing to compute here.

## 16. What I would compute tomorrow

These are **three proposed scripts or checks**, not additional files created in this session. They have different roles: isolate the operator sector, test its possible metric, and test prime-side positivity. A positive numerical result in any finite range is a calibration, never a proof of RH.

### 16.1. `mayer_cusp_tail.py`: continued transfer determinant and cusp residue

Implement the Taylor entries from §3 with mpmath. Use dimensions 12, 20, and 32 and at least two precision levels, for example 50 and 80 decimal digits. Compute \(\det(I-L_s)\) and \(\det(I+L_s)\) near the first three \(s=\rho/2\), tracking null vectors as well as determinants. Compare an exact Hurwitz tail with finite-branch approximations **in the convergence region first**, then demonstrate why the latter cannot be extrapolated directly to \(\operatorname{Re}s=1/4\).

The immediate deliverable is a divisor and boundary-coordinate comparison with \(\phi(s)\), including which parity sector sees the pole, exceptional factors, and whether cusp evaluation captures the relevant residue. After that, attempt a Schur complement separating an interior block from the cusp-tail coordinate. Do not call a fitted positive matrix a natural pairing until its entries have a formula independent of the zero locations.

**Expected under RH:** the correctly isolated Riemann scattering family has \(\operatorname{Re}s=1/4\). The Laplace-derived family is separately located on its appropriate line. Agreement near already-known low zeros is expected unconditionally from those particular zeros and is mainly a check of the implementation.

**Meaning of failure:** cutoff-sensitive roots, a missing divisor, or wrong residues first falsify the truncation or the claimed cusp identification. A numerical pole off the line is not a counterexample unless analytic continuation, residual/error bounds, and identification with an actual zero of xi are independently certified. Failure to find a positive boundary identity would weaken this proposed mechanism, not RH.

### 16.2. `one_port_width_metric.py`: realizability, robustness, and the cost of a metric

Build the inverse one-port model of §1 from arbitrary prescribed poles, and perturb its coupling residues. Sweep the opening strength in a closed Hermitian model to observe width splitting and possible superradiant segregation. Form the exit Gram matrices for windows of cached ordinates, increasing both the height and window size; also form synthetic examples with the paired widths \(1/4\pm\epsilon\).

The controls should include scalar physical loss \(-w_0I+iH\), a one-port equal-width inverse design, and a generic one-port opening. Compare pole widths, Gram conditioning, and the actual survival probability of a coherent superposition. Equal pole widths and a common survival law must be measured separately.

**Expected under RH:** the actual Riemann modes have width \(1/4\), but their physical cusp kernels need not be well conditioned and their coherent survival curves need not be pure exponentials. At sufficiently high density one should not expect a uniform bound on the condition numbers needed to orthogonalize the modes. The finite inverse design should work regardless of the chosen real pole positions.

**Meaning of failure:** inability to recover prescribed finite poles indicates an algebraic or numerical error. Width splitting under a generic residue perturbation confirms that equal widths require a constraint; it says nothing against RH. Deteriorating conditioning rules against a bounded metric change on \(K_S\), while leaving open a different Hilbert completion or a different bond space. A physical scalar-loss claim is falsified as soon as nontrivial interference survives in the supposed universal norm-decay law.

### 16.3. `prime_screw_kernel.py`: a positivity test that does not input critical zeros

Use Suzuki's prime-side definition, copied with its constants from the local source. For \(t\geq0\),

\[
\begin{aligned}
\Psi(t)={}&4(e^{t/2}+e^{-t/2}-2)
-\sum_{n\leq e^t}\frac{\Lambda(n)}{\sqrt n}(t-\log n)\\
&+\frac t2\left[\psi(1/4)-\log\pi\right]
+\frac14\left[C-e^{-t/2}\Phi(e^{-2t},2,1/4)\right],\\
C={}&\pi^2+8G_{\rm Catalan},
\end{aligned}
\]

with even extension, \(\Psi(0)=0\), and \(\Phi\) the Hurwitz–Lerch function. Form

\[
K_{ij}=\Psi(t_i)+\Psi(t_j)-\Psi(t_i-t_j).
\]

For nodes in \([-A,A]\), compute the prime sum exactly up to the required cutoff \(e^{2A}\), rather than treating a prematurely truncated sum as exact. Handle \(t=0\) by the limiting value. Refine arithmetic precision independently of the grid, and estimate the matrix perturbation from entrywise errors before interpreting a small eigenvalue. For example, an \(N\)-by-\(N\) matrix with each entry uncertain by at most \(\epsilon\) has operator-norm error at most \(N\epsilon\).

A small calibration was already run in memory at 40 decimal digits, with
\(t_j=j/8\), \(j=1,\ldots,16\). The prime-defined matrix had minimum and maximum eigenvalues approximately \(0.0223365\) and \(0.817350\). The matrix constructed from 3000 positive critical ordinates and their negatives had approximately \(0.0216643\) and \(0.806458\); the largest entrywise discrepancy was \(0.00132330\), from the omitted zero tail. The direct values included \(\Psi(1)\approx0.04400730524\) and \(\Psi(2)\approx0.05334112417\). This is an implementation sanity check on a small interval, where positivity is not surprising.

The new experiment should enlarge the interval, inspect the lowest eigenvectors, and study Schur complements as new prime-power breakpoints enter. Add synthetic off-line paired spectral terms only as a control of sensitivity; the actual test matrix must remain prime-defined. A negative direction should be converted into a smooth compactly supported test function and checked against the explicit formula before it is taken seriously.

**Expected under RH:** every exact finite kernel matrix is positive semidefinite, and the associated compact-support forms satisfy Suzuki's positive-definiteness conclusion. One should not expect a grid-independent strictly positive lower eigenvalue, since the continuum operator is compact and increasingly fine discretizations expose small eigenvalues.

**Meaning of failure:** a negative eigenvalue smaller than the error bound is numerical ambiguity. A certified negative kernel direction for the exact prime-defined function would contradict the global positivity criterion and hence RH. Even persistent numerical positivity does not explain it. The hoped-for mechanism would be a factorization or monotone boundary-energy law discovered from the prime formula and proved independently of RH.

## 17. Rewritings, not mechanisms

- **“There is a centered Hermitian zero operator.”** Putting the zero frequencies on a diagonal assumes they are real. For a prescribed finite transfer operator, asking for a positive metric additionally assumes semisimplicity; on the infinite cusp model, boundedness of that metric is a further substantive requirement.
- **“There is a positive centered canonical system or prime string.”** With the response fixed to \(Q_\xi\), the positivity is presently equivalent to RH. An unconditional passive system for the uncentered \(S\) is a different, weaker construction.
- **“The common-width-removed delay is a positive density of states.”** This is the spectral/Weil criterion in an experimentally recognizable form. It becomes a mechanism only if the removal preserves positivity for a reason visible in the prime data.
- **“The centered dynamics have unbroken PT symmetry.”** Without an explicit form and a bound ensuring its definiteness, this names the desired spectral reality and provides no cause.
- **“The cusp Ruelle band is an exact line.”** If its roots have already been identified with \(\rho/2\), the line assertion is RH. Constant-curvature control of the Laplace sector does not establish it.
- **“Inverse scattering reconstructs equal-width poles.”** That reconstruction succeeds because equal widths were prescribed. Its useful output is the constraint on residues, which would still have to be derived arithmetically.
- **“The continued Euler product is a Hermitian density-of-states determinant.”** Hadamard/Euler equality does not supply a positive density of states. A Thouless interpretation needs an independently constructed self-adjoint chain.
- **“Xi is a real-rooted expected characteristic polynomial,” or “the heat threshold has the RH value.”** Either is a target, until the prime ensemble or the threshold-fixing identity is exhibited.

There are genuine mechanisms in this notebook: uniform attenuation per travel time, an attenuation coboundary, arithmetic tempering in a constructed representation, a positive canonical energy obtained from local data, and the special interlacing structure of certain matrix ensembles. None is yet identified with the Riemann cusp sector. The next useful result would be an explicit arithmetic identity for the cusp transfer or its boundary pairing—even an obstruction showing that a proposed pairing cannot work—rather than one more general dilation of a function we already know.
