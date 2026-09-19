# Riemann versus Selberg decay operators

Final status: saved at user-requested shutdown; see the completion/status section below. Earlier checkpoint status lines are historical.
Checkpoint started 2026-09-19. Owner: riemann_selberg_modes subagent. Work is continuously saved here; this first checkpoint precedes reading or remote work.

## Task and provisional distinctions

Audit exact generator/time/sign normalization relating geodesic-flow resonances to Laplace eigenvalues and to Eisenstein scattering poles. Separate compact Selberg, cofinite cuspidal spectrum, scattering resonances, complementary eigenvalues, and threshold Jordan phenomena. Determine why self-adjointness of the modular Laplacian does not establish RH; investigate the alleged common width 1/4 in the Riemann scattering sector. Independently check finite Gram bridge and sign correction in existing cusp lane. Produce precise next lemmas and counterexamples, without claiming RH.

Status: initializing; no mathematical conclusion yet. Primary local source indicated by parent: refs/src/1712.07832/preprint.tex. Required local notes/shards will be located next.

## Checkpoint 1 — verified local distinctions

Read HANDOFF's Selberg/Phantasm state, the full cusp-bridge note, the compact first-band theorem in shard 03e, modular subsection 03f, kernel-semigroup subsection 04, D6 in notes/selberg-letters/astra-proofs.md, and BW's introduction/theorem. All inputs are local and survive network loss.

1. Fix curvature -1 and geodesic arclength time t. The repository flow convention is A=-X, (X+lambda)u=0, exp(t A)u=exp(t lambda)u. The Casimir/Poisson relation is Delta f=-lambda(1+lambda)f and lambda=s-1. BW instead names the generator X and resolvent (X-s)^(-1); time reversal must be declared before importing its s into repo lambda. BW supplies global meromorphic continuation and finite-rank poles for the modular orbifold, but explicitly leaves the desired transfer/first-band identification to further research (refs/src/1712.07832/preprint.tex:143–172).
2. Compact Selberg first-band modes satisfy lambda=-1/2 +/- sqrt(1/4-mu), where mu is an L2 Laplace eigenvalue. Self-adjointness gives mu real/nonnegative, hence the vertical -1/2 line OR the real interval [-1,0]. Ruling out complementary modes still needs mu>=1/4. At mu=1/4, the doubled quadratic root can carry a Jordan block: the divisor lies on the line but centered unitarity on the full block fails.
3. Modular Riemann poles instead occur at s=rho/2 and have Laplace parameter mu=s(1-s), which is NONREAL even under RH: for rho=1/2+i gamma, mu=3/16+gamma^2/4+i gamma/4. Their Eisenstein Laurent eigenfunctions grow like y^(1-s), are outside L2, and do not lie in the self-adjoint operator domain. This single calculation makes the distinction especially sharp: RH would not move these states onto the self-adjoint Laplace spectrum.
4. Under RH the proposed corresponding geodesic exponent is lambda=-3/4+i gamma/2. The Hardy/cMPS exponent is b=-conj(rho)/2=-1/4+i gamma/2. These are different clocks/operators; the same t normalization does not make them the same decay observable. The FE relabelled scalar relation C=A+1/2 is correct, but is not yet a flow intertwiner.
5. I independently checked the Hardy sign algebra: exp(-it conj(tau)) with tau=gamma/2-i beta/2 grows as exp(+beta t/2), whereas the defined lower-half-plane compression has Z(t)k_tau=exp(it conj(tau))k_tau, decaying as exp(-beta t/2). The old shard's sign/adjoint is inconsistent; the cusp-lane correction is right.

Next: derive an explicit cusp flux identity, independently audit the Cauchy Gram bridge, and distinguish a generic one-channel passive realization from arithmetic equal-width rigidity.

## Checkpoint 2 — a primary model-theory source located and saved

A targeted live literature search found Yoichi Uetake, *The Lax–Phillips infinitesimal generator and the scattering matrix for automorphic functions*, Annales Polonici Mathematici 92 (2007), 99–122, DOI 10.4064/ap92-2-1. The primary publisher/archive abstract explicitly states algebraic-multiplicity agreement between modular LP generator spectrum and scattering poles, an explicit L2(R) operator model, and an RH-equivalent cyclicity condition. This is directly relevant to a repo gap, but the abstract alone does not verify our exact symbol or normalization. Search result + retrieval timestamp durably saved in riemann-vs-selberg-web-search.json; primary page(s) saved in riemann-vs-selberg-uetake-primary.json. Parent notified to archive the full PDF. No theorem is imported beyond the abstract pending inspection.

The same search recovered compact/convex-cocompact quantum-classical correspondence papers, whose hypotheses do not automatically include a cusp. It did not establish a later cusp first-band/Eisenstein theorem. This is a search limitation, not a claim no such theorem exists.

## Checkpoint 3 — boundary flux and the finite Gram bridge independently derived

### Why the self-adjoint energy argument stops

Take Delta=-y^2(partial_x^2+partial_y^2) and dmu=dx dy/y^2. For a smooth mode f on the truncated fundamental domain D_Y, paired vertical sides cancel and integration by parts gives

`mu ||f||^2_(D_Y) = integral_(D_Y) (|f_x|^2+|f_y|^2) dx dy - integral_0^1 conj(f(x,Y)) f_y(x,Y) dx`.

For the leading Eisenstein Laurent mode, `f=c y^(1-s)+exponentially decreasing terms`, with s=sigma+i eta, the boundary term is `|c|^2(1-s)Y^(1-2sigma)` up to decreasing terms. Its imaginary part yields

`Im(mu) ||f||^2_(D_Y) = eta |c|^2 Y^(1-2sigma)+o(1)`,

consistent with `Im(mu)=eta(1-2sigma)` and `||f||^2_(D_Y)~|c|^2Y^(1-2sigma)/(1-2sigma)`. The nonzero cusp boundary flux exactly balances the nonreal spectral parameter. Dropping this term would manufacture a false reality proof. A self-adjoint domain requires the relevant boundary pairing to vanish in the limit; these generalized outgoing modes do not satisfy that condition.

### Independent audit of the finite bridge

For distinct leading poles s_i in `0<Re(s_i)<1/2`, extraction of the doubly leading Laurent coefficient in D6-MS gives, in the antilinear-first convention,

`<Lambda^Y e_i,Lambda^Y e_j> = conj(c_i)c_j Y^(1-conj(s_i)-s_j)/(1-conj(s_i)-s_j)`.

Normalize by `c_i Y^(1/2-s_i)` and put `C_i=s_i-1/2`. Then

`K_ij = -1/(conj(C_i)+C_j) = integral_0^infinity exp(conj(C_i)t) exp(C_j t) dt`.

This is a positive Gram matrix for the explicit output functions `g_i(t)=exp(C_i t)`. Independence of distinct exponentials makes it strictly positive. The map `v -> g_v(t)=sum_i v_i exp(C_i t)` is an isometry from `(C^N,K)` to their span in L2(0,infinity). The modal semigroup `exp(t C)` becomes the left translation `g(u)->g(u+t)` and obeys the exact observable flux law

`d/dt ||exp(t C)v||_K^2 = -|sum_i exp(t C_i)v_i|^2`.

Equivalently `C* K+K C=-11*`. This is a concrete causal output interpretation of the cusp Gram identity: stored energy equals future emitted energy, and decay is energy leaving through one channel. It is not dependent on RH.

For lower-half-plane `tau_i=i conj(C_i)` and boundary measure dx/(2 pi), direct contour integration gives Hardy kernels `k_i(x)=1/(x-conj(tau_i))` the same Gram `i/(conj(tau_j)-tau_i)=K_ij`. The kernels are eigenvectors of the defined compression with generator `i conj(tau_i)=C_i`. Thus the prior finite isometry is correct, with the indispensable caveats: it uses pole data, assigns a modal C on the truncated Eisenstein span, does not prove truncation intertwines geodesic flow, and does not prove a full Hilbert-space/domain map or completeness.

### Exact arithmetic symmetry and exact nonnormality

Riemann FE gives the scattering-pole partner `s' = 1/2-conj(s)`, whereas the geometric scattering identity is `phi(s)phi(1-s)=1`; the latter exchanges poles and zeros, and does not impose the former same-pole-set symmetry. Under `C=s-1/2`, FE becomes `C'=-1/2-conj(C)`. This is symmetry about Re(C)=-1/4, but allows two different widths summing to 1/2.

If all distinct finite C_i lie on Re(C)=-1/4, the physical pairing still satisfies `(C+1/4)*K+K(C+1/4)=(1/2)K-11*`, nonzero for dimension N>=2. Equal modal widths therefore do NOT mean the physical semigroup is a scalar exponential times a unitary group. A nonnormal one-channel system has interference-dependent survival energy even when every eigenmode has the same width. This resolves a potentially misleading strength difference between RH (divisor line) and an orthogonal-mode Hamiltonian realization in the physical norm.

## Checkpoint 4 — Uetake supplies the actual wave model; an exact quadratic intertwiner

The parent has now archived the full primary PDF and text: `refs/src/uetake-2007/paper.pdf`, `paper.txt`, with receipt `notes/rh-strategy-2026-09-19/uetake-source-download.json`. Publisher URL: https://www.impan.pl/shop/en/publication/transaction/download/product/85177 . I inspected the local primary text, including pages 102–103, 109–114, 115–120.

**Verified theorem content.** Write p for Uetake's variable, to avoid confusing it with Selberg s. His causal scalar factor is `F(p)=xi(2p)/xi(-2p)`. Theorem 4.2 (p. 112) proves the generator A_c of the compressed wave semigroup has meromorphic resolvent, pole order agreement with F, and dense span of generalized eigenvectors. Theorem 4.4 (p. 114) identifies the eigenvalues of `-2 A_c` with nontrivial zeta zeros, with algebraic multiplicities; its imaginary-spectrum criterion for `2 A_c+1/2` is exactly RH. Read “basis” in 4.4 conservatively as the completeness statement actually proved in 4.2; no Riesz-basis bounds are provided by these lines. Theorem 5.1 (p. 118) gives explicit automorphic boundary profiles spanning a subspace of L2(R_-), on which A_c is the compressed left-translation generator. This source repairs much of the repo's old missing modal/completeness citation; it does not identify those modes with BW geodesic resonances.

**Normalization audit.** Repo `S(tau)=xi(1-2i tau)/xi(1+2i tau)` is exactly `F(i tau)` by xi's functional equation. Let `Lambda(z)=pi^(-z/2)Gamma(z/2)zeta(z)`. The raw Eisenstein coefficient is `phi(s)=Lambda(2s-1)/Lambda(2s)`. Therefore

`S(tau) = [(2i tau-1)/(2i tau+1)] phi(1/2+i tau)`.

It is the causal zeta factor, not literally the raw Eisenstein coefficient. Uetake's original LP scattering matrix on p. 110 is `-[(p-1/2)/(p+1/2)] F(p)` and has one extra generator pole at p=-1/2; his construction removes that one-dimensional factor. His alternative incoming/outgoing convention on p. 116 uses `F(p)(1/2+p)/(1/2-p)`. Thus raw Eisenstein, original LP, and factored Hardy scattering differ by explicit elementary factors. They agree on the nontrivial arithmetic modal set after the stated transformations; they are not interchangeable as whole symbols.

**A domain caution in applying the paper.** Define the compressed generator by its strong semigroup derivative. Do not blindly import the p. 110 assertion `dom(A_c)=dom(L) intersect K`: the generator of a compressed half-line translation ordinarily allows nonzero boundary traces, whose zero extension is not in the whole-line derivative domain. The elementary exponential resonant profile illustrates this. The model semigroup and spectral statements can be used with their correct half-line generator domain; deriving an unbounded Lindblad/no-event letter requires spelling out the boundary/exit domain separately. This is not a refutation of the meromorphic-model theorem, but a concrete warning against an invalid domain inference.

### The half shift is geometric, without proving equal widths

The physical automorphic wave equation is

`u_tt=(1/4-Delta)u`, with first-order `W=[[0,I],[1/4-Delta,0]]`.

For `Delta f=s(1-s)f`, its two wave exponents are `q=+/- (s-1/2)`. A scattering pole with Re(s)<1/2 selects the decaying outgoing exponent `q=s-1/2`; a putative first-band geodesic exponent is `lambda=s-1`, so **q=lambda+1/2**. This is a change of generator/observable, not a rescaling of t. Correcting the loose phrase “different clocks” in Checkpoint 1: both use the natural unit logarithmic-cusp / curvature-minus-one normalization, and the shift arises from the `1/4` in the wave equation.

Indeed set r=log y and let the zero Fourier mode be `u_0(y,t)=y^(1/2)v(r,t)`. Direct calculation gives `(1/4-Delta)u_0=y^(1/2) v_rr`, hence `v_tt=v_rr`. The leading residue profile becomes `v(r)=c exp((1/2-s)r)=c exp(-q r)`; the outgoing time-dependent solution `exp(q t)v(r)` travels in r-t. This is a physically natural escape mode down the cusp, not an arbitrary post-hoc damping convention.

There is an explicit **algebraic candidate intertwiner**. Assume a first-band Poisson pushforward P on a space where `Delta P=-P(A^2+A)` is valid, with A=-X. Put `C=A+1/2` and

`T u = (P u, P C u)`.

Then a direct block multiplication proves `W T=T C`. Thus the missing flow-to-wave bridge has a concrete map to test, not just a matching spectrum. It remains to show that this T respects the BW resonant domains, outgoing boundary conditions, pole multiplicities, and the LP quotient/projection. P alone lands in non-L2 Eisenstein data, so the identity is currently distributional/algebraic, not a bounded isometry.

## Checkpoint 5 — discriminating toy models and an observable distinction

### A two-state passive model distinguishes the missing theorem

Take a two-state excited space, one exit `j=(sqrt(2g),0)`, and Hermitian coupling `H=[[0,w],[w,0]]-Omega I`. Then

`B=-iH-(1/2)j*j = i Omega I + [[-g,-iw],[-iw,0]]`,

`b_+/- = -g/2+i Omega +/- sqrt(g^2/4-w^2)`.

For **g=1/2**, this has exactly the arithmetic center -1/4 and FE symmetry `b -> -1/2-conj(b)`. It is passive, has a single exit, and has a CPTP vacuum Lindblad/cMPS completion for every real w. Yet:

- `w>1/4`: both eigenmodes have amplitude width 1/4 (underdamped); centered B is diagonalizable with imaginary eigenvalues.
- `0<w<1/4`: there are two distinct positive widths whose sum is 1/2 (overdamped); both remain in the allowed Riemann strip. FE, CP, one exit, and strict stability all hold.
- `w=1/4`: equal width holds but centered B has a nonzero nilpotent part of square zero (Jordan threshold); matrix elements can contain `t exp((-1/4+i Omega)t)`.

With w=1/8, the unequal widths are exactly `1/4 +/- sqrt(3)/8`. This is a direct counterexample to deriving RH from generic cMPS/passivity/one-channel/FE properties. It also shows a constructive possibility: a letter-defined coercive coupling theorem could force an underdamped regime, just as a spectral-gap inequality selects the Selberg branch. The scalar toy inequality `w>g/2` is not currently available for the modular boundary operator; no analogy promotes it to a proof.

The toy can be written as an effective PT-symmetric Hamiltonian after centering. That symmetry alone permits both regimes; proving its unbroken regime is the difficult bound. No physical PT principle is asserted for the arithmetic system.

`riemann_selberg_toy_modes.py` is an offline reproducible diagnostic for these three cases, their exact FE symmetry, dissipative/cMPS gauge, threshold Jordan rank, and the wave/geodesic intertwiner. `riemann_selberg_toy_modes.json` records its passing output. The algebraic formulas above prove the examples; floating-point checks only catch sign/normalization errors.

### Which experiment actually sees which rate?

1. **Geodesic correlation:** for compactly supported smooth observables, poles of the meromorphic Laplace transform of `<f composed with geodesic_flow_t,g>` are flow resonances. A simple pole at lambda contributes a modal term proportional to exp(lambda t) when a valid inverse-Laplace resonance expansion exists; the coefficient can vanish for a particular test pair. BW gives meromorphic poles accessible as observables vary, but meromorphy alone does not supply every desired uniform remainder estimate. The Riemann scattering subset would have lambda=rho/2-1, hence width 3/4 under RH, only after the missing cusp first-band identification.
2. **Automorphic wave escape:** the shifted wave equation has outgoing semigroup modes q=s-1/2. Uetake's factored LP semigroup realizes the nontrivial arithmetic set with width 1/4 under RH. The physical norm loses outgoing energy; equal widths do not remove interference between nonorthogonal modes.
3. **Bond/cMPS coherence:** in a vacuum completion with excited generator B, a prepared coherence `|v><vac|` evolves by `exp(tB)|v><vac|`. Its response against `|vac><w|` is `<w,exp(tB)v>`, so the amplitude rates are the b's. Population survival of a single eigenmode has rate `2 Re(b)` (width 1/2 under RH), and coherence/population sectors must not be conflated.
4. **Stationary emitted field:** the finite vacuum-exit realization has a pure absorbing vacuum with no ongoing output. Its decay response is physically observable after excitation, but its stationary cMPS field can be trivial. A mixed critical BC stationary state or a nontrivial stationary ring construction is an additional requirement; it does not follow from the mere existence of the decay generator.

## Final comparison — exact sectors and normalization

All rates below are **amplitude** exponents for exp(t generator), curvature -1, and unit geodesic/logarithmic cusp time. Selberg parameter is s, Riemann parameter is rho, Laplace eigenvalue is mu. Set lambda=s-1 for the geodesic first band and q=s-1/2 for the decaying shifted-wave branch. No statement identifies all the listed spaces.

| Sector / object | Spectral parameters and time exponent | Positive structure available | What fixes / fails to fix the decay width |
|---|---|---|---|
| Compact Selberg, mu>1/4 | s=1/2+/-ir; lambda=-1/2+/-ir | Haar L2 norm of Laplace eigenfunctions, transported branchwise through Poisson map | Casimir relation plus mu>1/4 gives common **geodesic** width 1/2; the shifted wave itself has q=+/-ir and is conservative |
| Compact or cofinite complementary L2 eigenvalue 0<mu<1/4 | s=1/2+/-nu; lambda=-1/2+/-nu | Same self-adjoint positive Laplacian | Both flow branches decay but at different widths; self-adjointness alone does not exclude them |
| Compact threshold mu=1/4 | lambda=-1/2 is a doubled quadratic root | Positive Laplace eigenspace; generalized flow block may be Jordan | Divisor line statement survives; centered unitary realization of the full algebraic flow block fails |
| Cofinite cuspidal eigenfunctions | On modular surface mu>1/4; s=1/2+/-ir | Ordinary self-adjoint discrete spectrum, vanishing cusp constant term | This Selberg eigenvalue theorem concerns cusp forms, not Riemann zeros; LP scattering removes cusp forms |
| Cofinite residual spectrum, including constant | Real s in (1/2,1], mu=s(1-s); modular residual space is the constant | L2 eigenfunctions from physical-side Eisenstein residues | Separate finite-dimensional bound-state factor; its removal changes elementary scattering factors |
| Cofinite physical continuous spectrum | s=1/2+ir, mu=1/4+r^2 | Positive spectral direct integral / unitary Eisenstein transform | Generalized real-frequency waves; self-adjoint spectral measure says nothing about analytically continued complex resonances |
| Modular Riemann scattering poles | s=rho/2; mu=s(1-s); leading residue grows as y^(1-s) | Positive truncated Gram / nonzero boundary flux; no finite Haar norm | RH is Re(s)=1/4, so mu is still nonreal. This is arithmetic rigidity of resonance widths, not a Laplace lower bound |
| Putative geodesic realization of those poles | lambda=rho/2-1, width 1-Re(rho)/2; RH gives 3/4 | BW modular meromorphic resolvent exists; required first-band pole/pushforward correspondence still to establish | Correct center -3/4; compact rescaling exp(t/2) cannot unitarize this subset |
| Actual factored LP / Hardy wave model | q=(rho-1)/2 after outgoing pole label, or -rho'/2 after FE; repo kernel b=-conj(rho'')/2 | Contractive wave compression with positive energy/model norm; one-channel escape | RH gives common width 1/4; CP, contractivity, scalar scattering and FE all permit unequal widths |
| Multiple Riemann zero | Re(q)=-1/4 may hold with generalized kernel/Jordan chains | Model-space positivity accommodates multiplicity | RH alone allows polynomial times exponential decay; centered skew-adjointness would additionally impose semisimplicity and is stronger |

**Two different appearances of 1/4.** The `1/4` in `Delta-1/4` is the geometric threshold/half-density correction. It supplies the relation q=s-1/2 and makes the cusp zero mode a free one-dimensional wave. The assertion that **every arithmetic scattering pole** has Re(q)=-1/4 is extra arithmetic information. The geometry makes this a natural place to describe the decay modes; it does not set their common width by itself.

**Two different positive forms.** The physical output/Hardy metric obeys a rank-one loss law and has nonorthogonal modes. A separately manufactured diagonal modal metric can make centered eigenmodes unitary if the divisor lies on the line and the block is semisimple. Conflating them would exclude the natural one-channel physics. In infinite dimension a bounded invertible unitarizing similarity requires further uniform basis bounds; a formal algebraic modal completion is a weaker assertion.

## Two precise next lemmas

### Lemma target 1: cusp Poisson-to-wave intertwining with the correct domains

For a nonexceptional modular scattering pole s0=rho/2, construct a map from the generalized first-band Riesz range of the BW geodesic generator at lambda0=s0-1 into the outgoing generalized wave resonant data at q0=s0-1/2. Its distributional formula should be

`T=(P, P(A+1/2))`, with `WT=T(A+1/2)`.

Required conclusions: (a) the BW pole exists with the claimed finite multiplicity; (b) P matches the Eisenstein Laurent chain and is injective on that chain; (c) T satisfies the specified outgoing cusp asymptotics; (d) the LP regular-data projection/translation representation maps the chain into its genuine half-line generator domain and preserves chain length. For multiple poles use full Laurent/Jordan data, not merely leading coefficients. The identity is already algebraic; (a)–(d) are the actual analytic theorem. BW and Uetake supply the endpoint constructions, not their identification. A successful proof would derive the shift at operator level and connect two established resonance pictures without using RH.

### Lemma target 2: a modewise cusp leakage estimate from geometry/arithmetic

First formulate the boundary realization on a common dense core with a genuine trace map j and physical energy norm, satisfying the quadratic-form loss identity

`2 Re <v,Bv> = -||jv||^2`.

For a nonzero outgoing eigenmode Bv=bv this gives the exact relation

`-2 Re(b) = ||jv||^2/||v||^2`.

The arithmetic statement needed is the **modewise** estimate `||jv||^2 >= (1/2)||v||^2`, derived from automorphic cusp matching / arithmetic input before knowing zero locations. Together with the Riemann FE pair `b -> -1/2-conj(b)`, it forces equality and hence width 1/4 for each mode. It is an RH-equivalent hard estimate after the identification, not an independently proved inequality.

The quantifier matters: demanding this bound for *every* vector in a finite modal span is impossible for a one-row j when the dimension exceeds one; demanding a scalar dissipator is therefore the wrong target. The two-level toy shows exactly what a successful extra coupling/coercivity hypothesis must exclude. Uetake's Theorem 6.3 (p. 120) gives an alternative formulation through cyclicity of an explicitly augmented input-output system. Its explicit Poincare-series boundary profiles (Section 5) offer non-zero-defined data against which to test such an estimate or controllability argument. Neither bare cyclicity of the original minimal model nor generic positivity can prove it, as both hold for the unequal-width toys.

## Source checks, recovery, and status

- Primary local compact first-band input: `refs/src/1403.0256/RuelleResonForHn.tex` as quoted/checked in shard 03e and the reviewed prover notes; exact local source filename availability should be taken from `rg --files refs/src/1403.0256` if this catalog path differs. This lane relied on the already-reviewed local quotations for those compact formulas.
- Primary local Eisenstein/divisor input inspected via existing reviewed D6 proof: `refs/src/1607.08053/main.tex:370–401,592–601`; `refs/src/1108.5659/main.tex:2037–2049,2071–2079`.
- Primary small-level Selberg theorem directly checked: `refs/src/1803.06016/main.tex:121–122`.
- Primary cusp resonance theorem directly checked: `refs/src/1712.07832/preprint.tex:143–172`; https://doi.org/10.4171/JEMS/1103 . Gives finite-rank modular flow resolvent, with scope limitations described above.
- Primary LP model directly checked: Uetake, https://doi.org/10.4064/ap92-2-1 , complete local `refs/src/uetake-2007/paper.pdf` and `paper.txt`. Pages 110 and 114 were additionally rendered and visually inspected to confirm exact rational factor, domain wording, and Theorem 4.4 formulas. The full PDF is the durable source of those page images.
- All live searches and failed primary fetches were saved immediately with UTC retrieval times in the three `riemann-vs-selberg-*.json` web files. The successful full Uetake download and its checksum are recorded by the parent in the receipt named above. Failed fetch records have been retained rather than replacing them silently.
- All independent derivations are included in this note. Offline synthetic diagnostic: `python3 notes/rh-strategy-2026-09-19/riemann_selberg_toy_modes.py`; passing results saved beside it as JSON. No actual zeta zeros are inputs.
- Existing shards, HANDOFF, claim tables, and another agent's notes were not edited.

**Lane status: COMPLETE.** Conceptual comparison, source audit, finite Gram/sign audit, explicit wave intertwiner, three-regime passive toy, and two next lemma targets are saved. No RH claim; no assumption of zero simplicity, bounded eigenbasis, or a completed cusp geodesic identification.
