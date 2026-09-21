# Ideation ledger, 2026-09-19: ideas explored and leads obtained

Built from the four digests of 2026-09-19 (G1 founding/worklogs/shards a, G2 shards b and source
extracts, G3 prover campaigns, G4 sidequests and strategy review), which between them absorb 1509
lane entries into 492 items. Every line below carries the digest IDs it came from.

## 1. One page summary

The programme has a firm middle. Side A (the primes as a gas of rings) and side B (a transfer
operator whose subleading spectrum is the zeros) are joined by one identity, the explicit formula,
and three places now make that join exact. First, the quantum Ihara zeta of a channel: for unitary
Kraus letters closed under adjoint, Bass's proof goes through verbatim and RH for that zeta is
precisely Hastings' Ramanujan bound (G1-T3-1, G2-T7-4). Second, the sign: the zeros enter the
explicit formula negatively, no honest trace has a zeta numerator, so the bond must be `Z_2`-graded
with the pole even and the zeros odd, and the ring norm a supertrace (G1-T7-1, G1-T7-2, G1-T7-5).
Third, Weil positivity: for any operator with a declared trivial set and critical radius, positivity
of the rescaled trace sequence is exactly the one-sided bound, and a duality upgrades it to the
circle (G1-T13-2, G3-T9-1). Alongside these sit worked instances: Artin-Schreier curves, where RH is
manifest because the transfer matrix is a scaled unitary (G1-T11-1); one explicit graded tensor per
genus 0 to 3 (G1-T11-8); a qubit with Pauli letters whose ring norms count an elliptic curve over
`F_5` (G1-T8-5); the Weil-LPS channels, exactly Ramanujan because of Deligne (G1-T3-6); and a
certified implementation of the Connes-Consani-Moscovici chain that reproduces the first zero of
zeta to 249 digits from the primes below 50 (G4-T2-1).

What has been ruled out is large. Any prime-by-prime construction (circles, product states,
commuting dilations) is blind to the zeros (G1-T3-7). Detailed balance forces a real spectrum
(G1-T5-8). The vacuum rebound state is absorbing (G1-T5-7). `||Z_t|| = 1` for every `t` with or
without RH, so there is no worst-case mixing form of RH and no bounded renorming of the model space
(G1-T6-6, G4-T14-4). Arithmetic covariance alone does not force equal odd decay rates (G1-T10-7).
Symmetry, functional equation, positivity of ring norms and a unique fixed point are all mutually
independent of RH (G3-T18-1). And the obvious guess that the zeros are decay rates in the stationary
state's own metric is false: that Dirichlet form vanishes on a fermionic jump (G4-T12-14).

Live mechanism candidates are four. (a) The regular fermionic cMPS whose physical two-point function
selects a closed four-mode sector of equal width, separating observable closure from reflection from
coercivity (G1-T6-10, G4-T12-2). (b) The letters principle on Selberg: the letters give reality, the
functional equation and a positive form; one coercivity bound gives RH (G1-T12-4). (c) A parity jump
shifts every odd rate uniformly, which is the only known source of a common width (G1-T9-2). (d)
Positivity plus an operation under which eigenvalues multiply at fixed loss, in place of a Hermitian
form (G2-T6-6). The one sentence that states where the programme stands: the repository can
represent zeros as decay modes, but it has not found an arithmetic reason forcing equal decay rates
(G4-T10-1).

The ten leads I would act on first are ranks 1 to 10 of section 3.1.

## 2. Ideas explored, by theme

### 2.1 Foundations: permutations, shifts, and what RH has become

TJO's own entry point, rebuilt from scratch on 2026-09-14. For a finite permutation RH is free; the
content appears only for infinite permutations, where one asks for a different, small matrix with the
same power traces, and RH becomes a bound on the radii of its eigenvalues relative to the leading
one. For a regular graph that bound is exactly the Ramanujan condition. Status: registered, and it
is the reference frame every later formulation is translated back into.

Explored:
- **G1-T1-1** (registered) The permutation `(1 2)(3 4 5)`: one identity read as a gas of modes and a gas of rings; the notebook's minimal working model.
- **G1-T1-2** (registered) RH for a finite permutation is free; the content is the *other* small matrix, and its eigenvalues need not be unimodular.
- **G1-T1-3** (registered) Shifts of finite type: the 4-symbol cyclic rule satisfies the RH analogue, the golden-mean shift does not.
- **G1-T1-6** (negative) Side B is a Fourier dual, not a Wick rotation; the BC Hamiltonian has spectrum `{log n}` and the zeros are special *times*, with an absorption sign.
- **G1-T2-1** (registered) Existence of side B is cheap; the radius bound is the whole content, and it always comes from elsewhere (Weil, Deligne, Selberg).
- **G1-T2-2** (registered) The pairing is cheap, the degeneracy is hard; every adjacency matrix is symmetric and most graphs still fail.
- **G1-T2-3** (registered) The hierarchy primitivity / spectral gap / Ramanujan = PNT / zero-free region / RH, and the fluctuation slogan.
- **G1-T2-4** (registered) Ramanujan means tempered: no eigenvalue outside the universal cover's spectrum.
- **G1-T2-6** (registered) Erratum: `-log E` is not the entanglement Hamiltonian; the zeros live on the non-Hermitian transfer generator.

### 2.2 The Phantasm, side A as a gas, and the Bost-Connes reframe

TJO's central priority from 2026-09-12: dilation time is the one-dimensional space of a cMPS, the
bond carries a Riemann Lindbladian, its fixed point is the critical KMS state and the zeros are its
relaxation modes. The spectral half is forced and realised; the physical cMPS half is not. The two
halves that exist are complementary and neither is the object. Status: registered for the structural
facts, open for the identification.

Explored:
- **G1-T4-1** (registered) The channel IS an MPS transfer matrix; the zeta is the generating function of ring norms.
- **G1-T5-1** (registered) The free Riemann gas: one bosonic mode per prime with energy `log p`; the Euler product is the Fock-space product.
- **G1-T5-2** (registered) Bost-Connes as an MPO over the chain of primes; Dirichlet characters diagonalise every transfer matrix, with eigenvalues `L/zeta`.
- **G1-T5-3** (negative) Shor's `U_a` is the level-`N` Galois symmetry, not RH content.
- **G1-T5-5** (registered) The bond fixed point IS the entanglement spectrum; the level density is Hagedorn, not Cardy, so CFT scaling laws do not apply.
- **G1-T5-6** (registered) Normal KMS states exist only for `beta > 1`; at `beta = 1` the fixed point is not a normal density.
- **G1-T5-7** (negative) The vacuum-decay Lindbladian: zeros as odd coherences, but the stationary state is pure and the renewal integral diverges.
- **G1-T5-8** (negative) The prime-chain detailed-balance Lindbladian: right fixed point, real spectrum, no zeros.
- **G1-T10-8** (registered) No finite-dimensional representation of the full BC algebra retains the phases; the reset test is not a no-go for the full cone.
- **G2-T18-3** (negative) Same obstruction from the BC-symmetry side: `mu_n mu_n^* = I` forces `e(1/n) = I`.
- **G3-T11-1** (registered) Normal KMS only above the transition; the thermofield bond, exact entropy constants, Hagedorn growth with `beta_H = 1`.
- **G3-T11-2** (negative) The prime chain's spectrum is real on its weighted space; the zeros must live in a different bond. "Ergodicity breaking" is not established.
- **G3-T11-4** (registered) The annulus basis: `V_p` is a plain unilateral shift there, the vacuum is a geometric superposition, and the phase and shell pictures are genuinely different representations.
- **G3-T11-5** (registered) At criticality the right object is a normal semifinite *weight* on a completed configuration space, not a state; forward dynamics do not select Haar.
- **G4-T13-8** (registered) The BC finite-level obstruction is structural; our prime-level matrix extension is our own stipulation.
- **G4-T15-17** (registered) H-MM1 was handed over as an assumption and had to be proved, and only on a specified stationary weighted space.

### 2.3 Graded bonds, the sign, and fermionic zeros

The single most load-bearing structural argument in the book. A cMPS ring norm is a sum of squares
but the zeros enter negatively, so the bond must be graded, the ring norm a supertrace, and the
zeros interference between two parity blocks rather than negative probability. Two theorems make it
unavoidable (the numerator no-go and supertrace rigidity) and one proves the cMPS side (the twisted
ring norm really is a supertrace). Status: proved, with the infinite-parity case open.

Explored:
- **G1-T7-1** (registered) The minus sign forces a graded bond: pole bosonic, zeros fermionic, ring norm a supertrace.
- **G1-T7-2** (registered) The no-go: no ungraded honest trace has a zeta numerator; curves need the grading, graphs do not.
- **G1-T7-4** (registered) The Riemann graded generator `0 (+) B (+) diag(-(k+1/2))` has supertrace exactly `2 P_+`; spectral, not CP.
- **G1-T7-5** (registered) The fermion parity of a cMPS ring, proved: `str e^{LT}` is the periodic (Ramond) closure, `Tr e^{LT}` the antiperiodic one.
- **G1-T7-6** (registered) Grading a cycle odd is only half a specification: grading, parity insertion and holonomy are three separate knobs.
- **G1-T7-7** (negative) The Moebius function is a fermion parity, but "all primes odd" gives the wrong line; the grading must be transverse to the primes.
- **G2-T4-1** (registered) Bosonic species cannot pass genus one; `|Tr M^n|^2 <= s_+(n)s_-(n)` plus Cesaro forces `g <= 1` on the minimal bond.
- **G2-T4-3** (registered) The grading is forced by the *trace*, not by positivity; `(1-u)/(1-2u)` is an instance, not a counterexample.
- **G3-T1-2** (registered) Supertrace rigidity: the net signed multiplicity is determined, and a boson-fermion pair at one eigenvalue is invisible.
- **G3-T1-4** (registered) The prime part carries `-2`: `Tr_dist Z(t) = 1 - 2 P_+ - e^{-t/2}/(e^t-1)`, with the factor 2 a Jacobian.
- **G3-T2-1** (registered) Zeros require a bond grading *and* the periodic closure; an ungraded finite transfer has no finite zeros at all.
- **G3-T2-2** (negative) The residue argument: a numerator root needs a negative multiplicity, so curve counts of genus `>= 1` are never ordinary MPS ring norms.
- **G3-T2-4** (registered) The bosonic genus bound: the drafted proof was false (173 of 400 random counterexamples), the word-trace repair is load-bearing.
- **G3-T2-5** (negative) The infinite-bond bosonic no-go under explicit Hilbert-Schmidt hypotheses; and the ceiling on any finite bond.

### 2.4 Lindbladian candidates: letters, jumps, the BC symmetry cones, and the yolo guess

The search for the generator itself. What is known: the number of letters is the Kraus rank from
below and must be coarser than the grading from above; a parity jump is the only mechanism producing
a uniform odd rate; the admissible generators with the BC state stationary form a computable
positive cone whose dimensions symmetry alone cannot shrink. What failed: the bold phase-side guess,
audited by two codex lanes, on all three structural premises. Status: mostly negative, with the cone
machinery registered and reusable.

Explored:
- **G1-T9-1** (registered) The physical dimension principle: Kraus rank from below, coarser than the grading from above; choose the letters transverse to the grading.
- **G1-T9-2** (registered) A parity jump shifts every odd eigenvalue uniformly by `-2 gamma`; `2 gamma = 1/4` is the Riemann normalisation.
- **G1-T10-1** (negative) The yolo phase-side Lindbladian, TJO's requested bold guess; verdict negative overall.
- **G1-T10-2** (registered) What survived the audit: prime-jump kinematics, the Ramanujan-sum shells, and `1/zeta(w+1/2)` as an honest vacuum matrix element.
- **G1-T10-3** (negative) What failed, with exact counterexamples: grading not preserved, no Gibbs fixed point, prime cutoff is not a bond cutoff, parity closure is not the `Q^x` quotient.
- **G1-T10-5** (registered) The finite inverse problem: the cone of arithmetic-covariant generators, `Q C_L Q >= 0`, with exact dimension counts at `p = 3,5,7`.
- **G1-T10-7** (negative) Symmetry alone does not force a uniform odd rate; do not impose Weyl-translation covariance (it collapses the cone to the depolarizer).
- **G2-T18-4** (registered) The stationary covariant GKLS cone has an interior point (the reset generator), so positivity never shrinks the dimensions.
- **G2-T18-5** (negative) Full affine symmetry removes the oscillatory modes; the `p = 7` witness has full covariance and unequal odd rates.
- **G2-T18-6** (negative) Two prime levels: marginal compatibility does not select the coupling; the family `L_c` has identical one-prime restrictions.
- **G3-T12-1** (negative) The yolo guess's Galois structure survives; its grading does not, with explicit odd cross terms for every prime.
- **G3-T12-2** (negative) Rate `1/p` kills it: infinite no-jump quadratic form, no trace-norm limit at any positive time, no ordinary trace.
- **G3-T12-3** (negative) The zero hunt: exact resolvents, the irremovable shift `beta+1`, and a real spread instead of a line.
- **G3-T12-4** (registered) Exact by-products: the Gauss-vector eigenrelation, `log L - log zeta`, and BC as a compound-Poisson transfer.
- **G3-T13-1** (negative) Commuting jumps do not restore the Euler product; word multiplicities `Omega(n)!/prod k_p!` survive, and parity insertion does not remove them.
- **G4-T13-1** (registered) An exact finite cMPS/Lindblad realisation of the cusp Gram; admissible, but takes the pole list as input.
- **G4-T13-2** (registered) Three distinct spectra must be kept apart: the no-jump generator, the physical transfer, and the poles visible to insertions.
- **G4-T13-3** (registered) The finite inverse renewal criterion `M = -(B sigma + sigma B^*) >= 0`, with exact failures: reinsertion moves the physical spectrum, and only the uniform target works.
- **G4-T13-5** (negative) A stable graded bond with a rank-one homogeneous exit is impossible; one parity sector evolves unitarily.
- **G4-T13-10** (negative) The vacuum is absorbing: the renewal fixed point fails, and the vacuum-decay model realises the *double* of the forced datum.
- **G4-T15-24** (registered) The finite model's vacuum return function is independent of the shell cutoff, so the negative is not a truncation artefact.

### 2.5 Ring norms, curve counts and tensors genus by genus

TJO's five-item wish list: a natural tensor from the variety, the graded decomposition and why, a
theorem that ring norms give the counts, the Polya-Hilbert operator, the Ramanujan property. Genus 0
and 1 are one-liners, genus 2 needed a certified numerical tensor plus a nine-letter closed form
above a threshold, and every genus has a closed form on `C^{1|g}` once `q+1 >= 2g sqrt q`. The
standing limitation is blunt: the only input at every genus is the L-polynomial, so the construction
consumes the answer. Status: registered, with selection open.

Explored:
- **G1-T11-5** (registered) TJO's five-point wish list, and the Weil numerator as a P-closed ring norm; "circular unless the tensor comes from the curve".
- **G1-T11-6** (registered) Tier A: the ordinary elliptic curve, the lifted Frobenius as a toral endomorphism, everything present at genus one.
- **G1-T11-7** (registered) Tier B genus two: a false drafted bound, the correct genus bound, the nine-letter tensor, and the certified `F_5` tensor.
- **G1-T11-8** (registered) One explicit MPS per genus 0-3, with entanglement and parent Hamiltonians; "correlation length `2/log q` for every odd mode IS RH".
- **G1-T11-9** (registered) The zeta conditions imposed factor by factor (shard 06h): C1-C10, thirteen constructions, 461 checks, four orchestrator errors caught.
- **G2-T3-2** (registered) The obvious Polya-Hilbert Hamiltonian exists only in the supersingular world.
- **G2-T3-3** (registered) The natural genus-one tensor is the lifted Frobenius on the flat torus; the count is a Lefschetz number and an ideal index.
- **G2-T3-4** (registered) Hodge doubling is the ket/bra doubling, but the physical state has Schmidt rank one.
- **G2-T3-5** (negative) The infinite-label Fourier tensor: honest but redundant; every closed ring but the vacuum vanishes.
- **G2-T3-7** (registered) Gauge is the lattice basis; ideal classes and CM types are markings, not gauge, and complex spectral data forget them.
- **G2-T3-8** (negative) Base-`pi` digits: a finite carry automaton exists, but no nonnegative automaton counts the classes.
- **G2-T3-10** (dead) The literal geometric placement and the vacuum ansatz at genus two: both impossible.
- **G2-T3-11** (registered) The nine-letter closed-form tensor, its threshold `q+1 >= 4 sqrt q`, and base change into the closed-form regime.
- **G2-T5-2** (registered) Where the functional equation actually comes from: the involution `E -> q E^{-dag}`, and *not* from inverse-closed letters.
- **G2-T5-4** (registered) Four-letter elliptic channels with FE, RH and mixing by visible mechanisms; the notebook's best "all conditions at once" object.
- **G2-T5-5** (negative) FE, RH and mixing are mutually independent; positivity plus FE does not force RH.
- **G2-T5-9** (registered) What a finite bond cannot reach: no nonrational `Z`, no atomic prime comb, no infinitely many divisor points.
- **G3-T4-1** (registered) The natural elliptic tensor and why genus two breaks the rule; the non-product projector inside the Jacobian.
- **G3-T4-2** (registered) What a practitioner can build tonight: the pair shift, the four-letter elliptic channel, Kloosterman, supersingular with `U = Pi`.
- **G3-T4-3** (registered) Genus two: the certified `F_5` tensor by rational contraction, and the nine-letter family; fourteen ansatzes failed.
- **G3-T4-5** (registered) Tiny L-functions: Horner automata, Gauss sums, voltage covers, and honest character factorisation (which is not automatically Artin).
- **G3-T7-1** (registered) Counts as honest ring norms: `#E(F_{q^n})` is an ideal index, and one toral system realises both sides.
- **G3-T8-1** (registered) Rosati positivity derives Ramanujan at every place: the one place in the files where RH is proved rather than assumed.
- **G3-T18-1** (registered) FE, RH and mixing independent, with eight explicit families; "unique fixed point" is itself three conditions.
- **G4-T15-21** (dead) The genus-2 "polarisation trace line" ansatz is false; the true eigenvectors mix vacuum and trace line in ratio `+-sqrt 2`.
- **G4-T15-25** (negative) "Half entropy is RH" is C5 without C4: an RH-shaped spectrum with no functional equation selecting the centre.
- **G4-T15-26** (registered) C6curve versus C6projective cut different examples; even zero modes are free and move no divisor point.
- **G4-T15-27** (registered) Weighted MPS versus literal point count, and amplitude sum versus squared norm: say which is being asserted.

### 2.6 Artin-Schreier: the one exact prototype

The only place in the book where RH is manifest from the transfer matrix alone. In a self-dual
normal basis the quadratic trace form is local, so the curve is an MPS of bond dimension `q^J`, and
`E E^dag = q I` for a one-line reason. The transfer is a Clifford circuit implementing an explicit
symplectic map, the Weil bound saturates exactly when that map has finite order, and the sign law
took two wrong drafts before the exact form. The wall is sharp: cubic traces are non-local in this
basis. Status: registered and proved, family supersingular.

Explored:
- **G1-T11-1** (registered) The Artin-Schreier transfer matrix: rationality is finiteness, FE is `E -> q E^{-dag}`, and RH is manifest.
- **G1-T11-2** (registered) The sign law: two wrong drafts, then `S_n = (-1)^{n-1} delta_n Tr E_g^n` with `delta_n` a determinant on the radical.
- **G1-T11-3** (negative) Cubic traces are non-local and `n`-dependent; Dwork's `p`-adic operator gives rationality and FE but cannot see RH.
- **G1-T11-4** (registered) The quadratic Artin-Schreier family is supersingular in every characteristic; "finite tensors are supersingular" is nevertheless FALSE.
- **G2-T2-1** (negative) Dwork's operator is a coarse-graining tensor-network step, dead for RH, still a template for nuclear bond dimension.
- **G2-T2-3** (registered) The transfer unitary is a Weil-representation operator; `|S_n| = q^J q^{n/2}` iff `M_g^n = 1`.
- **G2-T2-4** (registered) The exact sign law and the two refuted universal laws, with the endpoint criteria `P_g(-1) != 0` and `P_g(-eta(-1)) != 0`.
- **G2-T2-5** (registered) The count is a supertrace with even = trivial character and odd = nontrivial, but for a geometric reason, not a theorem about group actions.
- **G3-T6-1** (registered) The corrected sign law and the fermionic sign as the sign of the Frobenius permutation; the reusable `A`-matrix trick.
- **G3-T6-2** (registered) RH for the prototype from scaled unitarity; the transfer is a Clifford circuit, hence free and efficiently simulable.
- **G3-T6-3** (registered) The character-sector grading and the root-of-unity filter: a constructive recipe for the Frobenius spectrum from the transfer spectrum.
- **G4-T15-14** (dead) The drafted sign law and the drafted super-transfer block were both false; centred exact Weyl covariance is required, not "up to a phase".
- **G4-T15-16** (registered) Positive-power traces are blind to zero eigenvalues and nilpotents; a concrete code fix in `artin_schreier_mps.py`.

### 2.7 The quantum Ihara zeta, quantum expanders, and the Weil-LPS channels

The theorem that made "RH is a Ramanujan property" precise, plus the general machine (Ihara-Bass for
an arbitrary Kraus family) and the one exactly-Ramanujan object the notebook owns. The honest last
row of the dictionary is that the Weil-LPS channels are Ramanujan because of Deligne, not because
they are channels. Status: registered; the channel-internal source of the bound is still missing.

Explored:
- **G1-T3-1** (registered) The quantum Ihara zeta: RH holds iff the channel is a Ramanujan quantum expander in Hastings' sense.
- **G1-T3-2** (registered) AKLT is `K_4`; a physical state with known entanglement structure is a Ramanujan object.
- **G1-T3-6** (registered) The Weil-LPS channel: exactly Ramanujan, commuting over `q`, joint spectra inside the box; the Weil-representation instance is ours.
- **G1-T3-7** (negative) Prime-by-prime constructions are blind to the zeros; zeros exist only in the infinite product.
- **G1-T3-8** (registered) The abelian obstruction: commuting dilations never give an expander, and the same obstruction sits inside Deligne's proof.
- **G1-T3-10** (negative) `PSL(2,Z)` generator channels are expanders, not Ramanujan; a presentation is not arithmetic.
- **G2-T1-4** (registered) The honest row: source of the bound is Deligne via LPS, and only the curve case is needed.
- **G2-T1-5** (registered) The quantum Ihara zeta of the Weil-LPS channel has poles only, and the quadratic settles every other admissible pair for free.
- **G2-T1-6** (registered) The finite model of the Riemann channel exists and self-checks, on the parent campaign's Hilbert space.
- **G2-T7-1** (registered) Theorem 1: Ihara-Bass for an arbitrary family of superoperators, with no invertibility, positivity or unitarity.
- **G2-T7-2** (registered) Which factor carries the spectrum, and the `D = 2` degeneration where the cancellation is total.
- **G2-T7-3** (registered) Side A is unconditionally positive: `Tr B^l = sum_gamma |Tr K_gamma|^2` with no pairing hypothesis, plus an Euler product.
- **G3-T7-3** (registered) MPS ring norms as an Ihara-type Euler product; Theorem 1 is a loop-admitting extension of Watanabe-Fukumizu, not a special case.
- **G4-T16-5** (registered) A bouquet is not a Watanabe-Fukumizu graph, and their own scalar specialisation is wrong there; the reversal/Sylvester argument closes the convention gap.

### 2.8 The graded Ramanujan property: definition, graded Harrow, and the continuum

TJO asked in September whether the Ramanujan property is understood in the graded case; the answer
was no, and the campaign built one. Everything is stated on the divisor of the periodic ring zeta,
so it passes to the continuum verbatim; graded Ihara-Bass holds sector by sector; index-two gradings
give graded quantum expanders; and in the continuum Ramanujan is temperedness. The recurring trap is
cancellation: the divisor is a difference, so it can hide modes outside the band. Status: registered
and prover-corrected; no third continuum example with an infinite critical-line divisor exists.

Explored:
- **G1-T8-1** (registered) TJO's quest item: every expander in the literature lives on an ungraded bond, so zeros require odd letters.
- **G1-T8-2** (registered) The definition on the divisor: (RH), (FE), (Ram), (HP), with signed trivial divisor and a supplied pair of reference rates.
- **G1-T8-3** (registered) Graded quantum Ihara-Bass sector by sector; band versus circle on the *net* divisor, with a degree-14 cancelling counterexample.
- **G1-T8-4** (registered) Graded Harrow expanders from index-two gradings, and the Artin factorisation over constituents.
- **G1-T8-5** (registered) A qubit with Pauli letters counts an elliptic curve over `F_5`: the smallest statement of the whole programme.
- **G1-T8-6** (registered) The P-mode is structural, not trivial; Ramanujan imposes a balance condition on the letters.
- **G1-T8-7** (negative) There is no odd-sector Alon-Boppana bound; the odd sector can be arbitrarily good.
- **G1-T8-8** (registered) Graded Weil-LPS in both sectors; in the `(13;5)` case the extremal Hecke eigenvalue lives in the odd sector.
- **G1-T8-9** (registered) Zeros need odd letters; the graded Weil-Hodge inequality `rho(E_1) <= rho(E_0)` is the only free constraint.
- **G1-T8-10** (registered) Graded Chernoff: in the continuum the grading lives in the jumps, there is no Hamiltonian odd letter, and aliasing must be checked.
- **G1-T8-11** (registered) Continuous Harrow: Ramanujan is temperedness, with gap exactly `1/2` on the K-invariant sector.
- **G1-T8-13** (negative) Which grading? The reflection and K-type gradings are both wrong; the right one is the transverse form-degree grading.
- **G3-T4-6** (registered) Graded quantum expanders exist and are abundant: Clifford theory, the Pauli qubit, LPS.
- **G3-T5-1** (registered) The definition and the four bookkeeping corrections it needs (trivial divisor, P-mode, reference rates, operator versus divisor FE).
- **G3-T5-2** (negative) Divisor statements are weaker than dynamical statements: three drafted upgrades all fail.
- **G3-T8-2** (registered) Band type versus circle type, and the finite Hashimoto-lift theorem with a letter-derived metric positive iff the band is *strict*.
- **G3-T16-1** (registered) Ramanujan = temperedness, the Lie-walk normalisation `1/(2d)`, and Repka's `3/4` explaining Selberg's `3/16`.
- **G3-T17-3** (registered) Continuum realisability: Poissonisation is lossy, singular transfers have no exponential, and the `1|1` half-entropy no-go.
- **G4-T12-6** (negative) No universal odd-sector Alon-Boppana floor, and why Hastings' word-counting argument cannot be split by sector.
- **G4-T15-28** (negative) The graded divisor cancels, so it can hide modes that violate the band; "band iff circle sector by sector" is false.
- **G4-T15-29** (negative) The LPS examples are not curves: the printed genus claims are wrong (degree 4, not 36) and one has uncancelled poles on the circle.
- **G4-T15-30** (dead) The cut `P = X` grading example: the same channel is mixing or period-two depending on which Pauli is called the parity.

### 2.9 Selberg as the worked infinite example, and the modular cusp

The 2026-09-16 campaign, chosen because Selberg is the one infinite object where the trace formula
is a theorem, the divisor is known and the source of reality is known. Result: the Selberg zeta is
the ring zeta of the *stable two-term* transverse complex; the letters give reality, the functional
equation and a positive branchwise form; one coercivity bound (Selberg's `1/4`) gives RH. The
obstacle is entirely the modular cusp, sharpened to H-CUSP-BRIDGE. Status: nine items promoted to
proved, one left open.

Explored:
- **G1-T12-1** (registered) Selberg is the one family where everything is realised, and its two mismatches (`T^2` versus `T log T`, emission versus absorption sign).
- **G1-T12-2** (registered) The most consequential step: derive the odd-block form from the letters, on an infinite object.
- **G1-T12-3** (registered) The Selberg zeta is the ring zeta of the stable two-term transverse complex; the Ruelle zeta and the all-odd tower both fail.
- **G1-T12-4** (registered) Reality from Haar, and the labelled-input theorem separating [HAAR]/[SL2]/[ANALYSIS]/[TRACE]/[BOUND]/[ENDPOINT].
- **G1-T12-5** (registered) Branchwise orthogonal pullbacks, the operator FE `J X J^{-1} = 1 - X`, and the Jordan block at Laplace eigenvalue `1/4`.
- **G1-T12-6** (registered) The finite Hashimoto-lift theorem with a letter-derived metric, in the inverse-paired setting only, with endpoint counterexamples.
- **G1-T12-8** (negative) No doubled-bond CP realisation of Selberg; both flat supertraces are negative distributions, and diffusion destroys the first band.
- **G2-T16-1** (negative) TJO's Lindblad question: the prime-circle picture cannot produce zeros. The missing ingredient is transverse expansion.
- **G2-T16-4** (registered) The flat trace, the tower `D = prod_j Z_S(.+j)` with `Lambda_fl = +D'/D`, and continuous Ramanujan as Selberg's `1/4`.
- **G2-T16-5** (registered) The cusp is the prime comb (in dips); the primes of zeta enter only through the cusp, not as closed geodesics.
- **G2-T16-6** (dead) The "damped Riemann channel trace" claim corrected to a statement about prime measures only.
- **G3-T14-1** (registered) Why Selberg, and the letters principle: separate what the letters force from what must be imported.
- **G3-T14-2** (registered) The two-term stable transverse complex and grading as cancellation; the parity-*exchanging* Ruelle symmetry is a second kind of FE.
- **G3-T14-3** (registered) The first-band manifest form, branch tags, and the `1/4` threshold where algebraic multiplicity doubles.
- **G3-T14-6** (negative) Prime circles give the prime comb with no zeros at all; the spectrum is the pole set of a finite Euler product.
- **G3-T15-1** (registered) The cusp scattering term is the prime comb in dips, with the `+1/2` boundary constant pinned.
- **G3-T15-5** (negative) Hecke rigidity is the strongest arithmetic input available but acts on the wrong spectral sector.
- **G4-T9-2** (negative) Even under RH the Riemann scattering Laplace parameter is nonreal; stop looking for a self-adjointness argument there.
- **G4-T9-3** (registered) The Cauchy Gram of Eisenstein Laurent states, its one-exit dissipativity identity, and why it does not select RH.
- **G4-T9-5** (registered) Which observable, which width: four numbers (3/4, 1/4, 1/4, 1/2) for the same zeros; fix one relabelling convention.
- **G4-T9-6** (registered) Two repository corrections recorded and deliberately not applied: the Hardy kernel sign and the scattering-symbol normalisation.
- **G4-T9-7** (registered) The cusp prime comb: negative atoms, the `+1/2` constant, and an identity of measures only.
- **G4-T9-8** (negative) Four corrections from the Selberg-letters lane: two shifted bands, a degenerate pullback, `1/4` known for `PSL_2(Z)`, and the weight-1 limit.
- **G4-T15-1** (dead) The Selberg tower dictionary was drafted upside down: the flat trace is `+D'/D` and the graph analogue is `det(1-uT)`.
- **G4-T15-2** (dead) The constant mode must be deleted on both sides of the dictionary.
- **G4-T15-3** (registered) `Omega = -Delta` exactly on right-K-invariant functions; the tensor Lindbladian is the Casimir *plus* `B_W^2/2`.
- **G4-T15-4** (registered) A flow generator is not a Lindbladian; and the prime circles' spectrum is disjoint from the zero set, which is the zero-free line in disguise.

### 2.10 Weil positivity and the Kraus pairings

For an arbitrary transfer operator with a declared trivial set and radius, positive definiteness of
the rescaled trace sequence is exactly the one-sided bound; a duality turns the Weil form into a
mode-pairing form and the bound becomes the circle. The Kraus dichotomy then sorts what a channel
can buy: inverse pairing buys the functional equation, adjoint pairing buys reality, both at once
forces unitarity. Two standing gaps: Weil positivity is blind to Jordan blocks, and the converse
needs a test-function class rich enough to separate the zeros. Status: registered and prover-checked.

Explored:
- **G1-T13-1** (negative) SPT protection is sign data, RH is modulus data, so cohomological protection cannot deliver RH; the mode-pairing reading survives.
- **G1-T13-2** (registered) Weil positivity for an arbitrary transfer operator (T1-T5), the inflow identity and the Kraus dichotomy.
- **G1-T13-3** (registered) Weil positivity is blind to Jordan blocks; Huang's `h_k = nu_0 - nu_k` is the boundedness form and a second cheap test.
- **G2-T8-1** (registered) "Every mode is its own partner": the finite Weil theorem and its arithmetic anchor in Connes and Connes-Consani.
- **G2-T8-2** (registered) The inflow identity: a duality turns the Weil form into the mode-pairing form; the continuous version needs the Dyson propagators.
- **G2-T8-3** (registered) The Kraus dichotomy in full, with the trivial-set bookkeeping and the two negatives (conjugation closure is free; some families have no partner at all).
- **G2-T8-10** (registered) Numerics caveat: finite-`L` positivity masks a mode just outside the circle, threshold approaching like `L^{-3/2}`.
- **G3-T9-1** (registered) The trivial set is not optional: with the unenlarged set the Hastings clause is false for *every* unitary family.
- **G3-T9-2** (registered) The dichotomy with corrections, plus the escape hatch `B_i = G U_i G^{-1}` and the exact FE/RH conditions on a graded tensor.
- **G3-T9-3** (registered) Jordan blindness with the explicit `r[[1,1],[0,1]]` witness; continuous ring norms from the Dyson expansion with free propagators.
- **G4-T11-1** (negative) Individual prime-power blocks of the Suzuki kernel are indefinite at first visibility; no sum-of-independent-blocks ansatz.
- **G4-T11-4** (negative) Amplification: the fixed-loss lemma, why ordinary tensoring fails, and that Deligne's loss is killed by *slicing*, not tensoring.
- **G4-T11-6** (negative) The prime kink no-go: `Psi` has first-derivative kinks at prime powers, so bounded-generator finite cMPS amplitude models are excluded.
- **G4-T15-7** (dead) The Kraus dichotomy corrected: unitarity on the nose, reality is free, and `mu -> r^2/mu` is not linear.
- **G4-T15-10** (dead) "Every zeta has side A, a nonnegative count of rings" is not a universal premise; the RH-relevant positivity is the Weil one.

### 2.11 The Riemann channel: Lax-Phillips, Stinespring, mixing, resonances

The repository's headline identification: compress the dilation semigroup, get Lax-Phillips on the
modular surface, and RH is uniform exponential decay of `Z(t)`. Two things are now known that
constrain it hard: the semigroup has no jumps at all (it is a no-event semigroup), and `||Z(t)|| = 1`
for every `t` regardless of RH, so no worst-case mixing statement and no bounded renorming can work.
The right form of a decay statement is one-sided and restricted to a regularity class. Status:
registered, with the central identification resting on unverified inputs.

Explored:
- **G1-T6-1** (registered) The Riemann channel and the two placements of the primes (jump semigroup for `sigma > 1`; resonances on `K_S`).
- **G1-T6-3** (negative) The Stinespring question answered negatively as literally stated: a no-event semigroup has no jump operators.
- **G1-T6-6** (negative) `||Z(t)|| = 1` for all `t`; and the Cauchy Gram condition number kills the Riesz-basis route to a metric.
- **G1-T6-7** (registered) For infinite bonds the divisor must be defined from regular data, not the `L^2` spectrum.
- **G1-T6-9** (registered) The 3000-zero ring-norm test matching every term of the explicit formula, and the prime-weight sign correction.
- **G3-T10-1** (registered) The absorbing-vacuum gadget: a general-purpose way to turn any strongly stable contraction semigroup into a channel carrying it as odd coherences.
- **G3-T10-2** (negative) The renewal equation fails, the bond is unentangled, and the complementary-halves statement.
- **G3-T19-5** (negative) The rewritings: eight statements that restate RH without causing it, plus four refuted analogies (Euler factors not inner, Thouless, complex scaling, depolarising detailed balance).
- **G4-T14-2** (registered) What Shang's reset Lindbladian actually shows: exact real spectrum, gap = mixing rate, and a ring-zeta factorisation.
- **G4-T14-6** (registered) Becker-Zworski: the correct form of a decay statement is one-sided and class-restricted; there is no gap on all of trace class.
- **G4-T14-7** (negative) Vectorised generators are generic, and the SUSY splitting is too clean: the Witten index cancels the whole nonzero spectrum.
- **G4-T14-9** (negative) Purified-Gibbs / Witten Lindbladians cannot carry the zeros; the coherence rates are real.
- **G4-T14-10** (negative) Neither Lindblad paper supplies expanders, Ramanujan graphs, a Hastings bound or cutoff.
- **G4-T15-5** (dead) Cut: the contour proof that each off-line mode contributes a Lorentzian of unit mass.
- **G4-T15-6** (dead) Cut: the continuous ring word `A_{j_1...j_k}`, and the drafted Dyson product that was false without free propagators.
- **G4-T15-9** (dead) The trivial set `S` has no arithmetic occupants: `xi` is entire, so take `S` empty.
- **G4-T15-11** (dead) Three resonance seeds refuted: the special information sits in the couplings, not in the loss operator.
- **G4-T15-12** (registered) Wigner time delay is convention-sensitive at the level of a rational function.
- **G4-T15-18** (dead) The population block's `|Tr Z|^2` is not a form factor; a product of distributional traces is undefined.

### 2.12 cMPS decay modes and the observable subquotient (the 2026-09-19 strategy review)

The most recent and, on the evidence, the most promising line. Instead of asking which operator has
the zeros as eigenvalues, ask which *observable* has them as poles. A regular fermionic cMPS with a
faithful mixed stationary bond has a physical two-point function selecting a closed four-mode sector
of equal width, with closure coming from the quadratic Majorana structure and the common width from
a reflection plus a coercivity inequality. The three requirements are independent, and none of them
is RH-sized except the last. Status: registered as a finite mechanism, explicitly not a Riemann
construction.

Explored:
- **G4-T10-2** (registered) Uniform width = uniform exit energy per stored modal energy; the modal identity `-Re lambda = ||Cv||^2 / 2<v,Gv>`.
- **G4-T10-3** (registered) Nonnormality is necessary, not a defect: uniform widths with a rank-one exit force it.
- **G4-T10-4** (registered) Any positivity claim must be *sensitive to the line*; existence of "some positive metric" is not a mechanism.
- **G4-T10-5** (registered) The letter-generated Krylov basis carries an explicit rational positive invariant metric, built with no eigenvectors and no zeta frequencies.
- **G4-T10-7** (negative) The two-state passive toy: CP, passivity, one channel and the FE together do not force a common width.
- **G4-T10-8** (registered) Multiple zeros are allowed and Jordan blocks are invisible to the usual bounds; never assume simple zeros quietly.
- **G4-T12-1** (registered) The relevant object is the observable odd *subquotient*, not the full odd transfer spectrum.
- **G4-T12-2** (registered) The regular `C^{2|2}` fermionic cMPS and its exact four-mode closure at width `1/4`, with a faithful mixed stationary state.
- **G4-T12-3** (registered) Three independent requirements: observable closure, reflection symmetry from a letter-derived involution, and an independent coercivity inequality.
- **G4-T12-4** (negative) What breaks the toy: `bd != 0` splits the widths, and a quartic term destroys the selection entirely.
- **G4-T12-5** (negative) The parity-jump budget, the Hilbert-Schmidt no-go, and the tight-frame identity `C_O^* C_O = 2c I` that replaces it.
- **G4-T12-7** (registered) Which transfer, which trace: the physical norm uses the plus-sign transfer, a fermionic two-point function the signed one.
- **G4-T12-8** (registered) The `C^{1|1}` witness with the correct two reference rates and an additive FE, but a *free* oscillation frequency.
- **G4-T12-9** (registered) Pre-registered failure criteria for the observable-subspace route, written before the work.
- **G4-T12-10** (negative) Finite positivity need not survive regulator removal: `lambda_min(G_n) = 1/(2n) -> 0`.
- **G4-T12-13** (registered) Kinetic regularity (`R_a R_b = (-1)^{p_a p_b} R_b R_a`, `R_f^2 = 0`) is an independent condition that narrows the generator cone.
- **G4-T12-15** (negative) Elementary odd modes and the full odd sector have different rates (`kappa/2` versus `3 kappa/2`), so one uniform rate on the whole odd sector is false.
- **G4-T12-16** (registered) How `J` and `G` were actually found: an exhaustive search over 384 signed permutations, then a linear Lyapunov solve.

### 2.13 Deligne-style positivity without Hermiticity

The expository backbone: Deligne's proof exhibits no Hermitian form, only a positivity plus an
operation under which eigenvalues multiply while the trivial loss stays fixed. Varieties have three
things graphs lack (products, slicing, the minus sign); zeta has the positivity and the sign but no
product. This is where the programme's steering statement lives. Status: registered as vocabulary,
never instantiated in the channel setting, and named "the largest standing gap".

Explored:
- **G1-T11-10** (registered) The three ingredients varieties have and graphs lack: products, slicing over a curve, and the sign.
- **G1-T11-11** (registered) The engine's three moves, and that Deligne's pointwise theorem is false for graphs (the two-loop bouquet).
- **G2-T6-1** (registered) What varieties have that graphs lack; zeta sits on the curve side of the table but has no `X x X`.
- **G2-T6-2** (registered) The abelian obstruction: any Ramanujan lift of the prime dilations must break commutativity by a quotient.
- **G2-T6-3** (registered) The sign: on the curve side positivity bounds the interesting eigenvalues; on the graph side it gives only the Perron bound.
- **G2-T6-4** (dead) Deligne's purity step is false for graphs, with an explicit counterexample satisfying all three hypotheses.
- **G2-T6-6** (registered) Ramanujan without Hermiticity: stop looking for a Hermitian form, look for positivity plus a multiplying operation.

### 2.14 The CCM window machine: `zst`, `ihz` and certified numerics

Two vertical implementations of the Connes-Consani-Moscovici chain, one for zeta and one for graphs.
What they establish: reality of the returned spectrum is unconditional and free, and RH enters in
exactly one place, the identification of the limit, which is Weil's criterion verbatim. The graph
side adds an exact critical window, a falsifiable instance where RH is false, and a new three-line
unitary key lemma. What a finite graph cannot test is the prolate step, which is exactly the step
that blocks CCM's own proof. Status: registered, benchmarked, partly unregistered in `db/`.

Explored:
- **G1-T13-4** (registered) CCM zeta spectral triples read as a machine from window explicit-formula data to a self-adjoint operator, plus two findings about their paper.
- **G1-T13-5** (registered) `zst`: the certified pipeline, the benchmark grid, the accuracy law, and seven defects with reusable lessons.
- **G1-T13-6** (registered) `ihz`: the linear algebra generalises verbatim and is classical; the analytic content does not.
- **G1-T13-7** (registered) Running the chain on a FALSE Riemann hypothesis; the mixed divisor is refused.
- **G1-T13-9** (registered) The windowed Weil form is an exact compression, and the extension disc; positivity alone cannot beat one Schur parameter per lag.
- **G2-T15-1** (registered) The window is an exact compression; the implicit model of the higher traces is Pisarenko's.
- **G2-T15-3** (negative) Integrality adds information positivity cannot see, but rescaling defeats it whenever the critical radius is not 1.
- **G2-T15-4** (negative) For zeta a better higher-trace estimator means more primes; the question is circular.
- **G4-T1-1** (registered) Reality is unconditional; positivity is the only place RH enters, and the perturbed shift is the companion matrix of the secular polynomial.
- **G4-T1-2** (registered) `eps_N` is Pisarenko's noise floor; every certified run is a windowed Weil-positivity instance, and the framing is new to the notebook.
- **G4-T1-3** (registered) The twelve "does not generalise" items, ranked; a graph gives the M3 archimedean derivation no free testing.
- **G4-T2-1** (registered) The three measured accuracy laws for zeta: 5.4 digits per unit of `x`, linear degradation in height with slope 0.37, and `N ~ 7.5 x`.
- **G4-T4-1** (registered) `IH-11`, the unitary key lemma: a new three-line theorem, kept as a certified cross-check while `corcar` is the backbone.
- **G4-T4-2** (registered) `IH-13`: the graph case is literally an instance of Connes-van Suijlekom, not an analogue.
- **G4-T4-3** (negative) Read `eta` off the displacement, never posit it; three variants look right and transport nothing.
- **G4-T5-1** (registered) Three regimes and the exact anchor `K = R+1`, with blind detection by exact rank.
- **G4-T5-5** (registered) TJO's own practice: falsify drafted universal claims on small graphs first.
- **G4-T6-1** (registered) No ungraded zeros; the `sign` field is the most likely silent error; mixed parity must be refused.
- **G4-T6-2** (registered) The curve instance gives CCM's sign back, but Hallouin-Perret got there first.
- **G4-T6-4** (negative) Irregular graphs: Weil positivity without duality; output exists but has no interpretation.
- **G4-T7-1** (registered) Certificates that failed at scale, and the exact-integer inertia route that would replace them.
- **G4-T7-2** (negative) FLINT/arb traps found by running them: the root finder hangs on repeated roots, and Rump's multiple-eigenvalue routine is not a primary truth route.

### 2.15 Simplicial complexes, buildings and higher rank

TJO's sidequest: does the Ihara-Bass picture survive when a graph becomes a complex, and does it
grade by cell dimension into fermionic zeros? The verdict is sharp. An Ihara-type zeta with a Bass
identity and an RH-iff-Ramanujan theorem exists for finite quotients of affine buildings and nowhere
else; what does survive on every complex is a universal rational Schur compression. Ramanujan
complexes give Ramanujan quantum expanders automatically, and the channel adds nothing. In higher
rank RH is a band, not a line, and there is no universal functional equation. Status: registered as
a testbed, explicitly not touching the Riemann side.

Explored:
- **G1-T14-1** (registered) Is there an Ihara zeta for a simplicial complex? Only for buildings; two competing higher-dimensional flows defined.
- **G1-T14-3** (registered) Prover corrections: opposition not non-incidence, the completed vertex L-function, no curve-weight dictionary, covariant weights pure gauge.
- **G1-T14-4** (registered) Ramanujan complexes give Ramanujan quantum expanders automatically; higher-rank RH is a band with the interior occupied.
- **G2-T9-1** (negative) The scope verdict: buildings only; the two near misses (hypergraph zeta, combinatorial Ruelle zeta) both degenerate.
- **G2-T9-4** (registered) The universal Bass-Schur compression: a rational compression by one dimension on *every* complex, with the delay-space trick.
- **G2-T9-7** (registered) The small exact test complexes, and vanishing orders with no topological meaning (`Z_ord(Delta^2) = 1` despite `chi = 1`).
- **G2-T9-9** (negative) Opposition, not non-incidence, is the building's successor rule; the colour-preserving part is exactly `L_E`.
- **G2-T9-12** (registered) The strategic verdict: a testbed, not a Phantasm.
- **G2-T10-1** (registered) The exact graded superdeterminant presentation with the `s_k^{m+1}` sign law.
- **G2-T10-2** (negative) "Fermionic zeros" names a *net* odd multiplicity that must be checked after cancellation; on the vertex side everything cancels.
- **G2-T10-3** (negative) The cell-dimension / cohomology dictionary is parity only, and one circle is not one parity sector.
- **G2-T10-4** (negative) The total object needs a Berezinian; cell chirality and flow superparity are distinct gradings.
- **G2-T10-5** (registered) The plus sign in `det(I + uL_B)` is a graded sign in disguise.
- **G2-T11-1** (registered) Arbitrary channel weights preserve the Schur compression exactly, and nothing else; the Euler/torsion factor needs flatness.
- **G2-T11-2** (negative) The full-cover connection is pure gauge; use voltage quotients. One unexplained chronological coincidence remains.
- **G2-T11-3** (registered) Artin bookkeeping traps: `a_hol` not `d_hol`, and simplex stabilisers break the fractional Euler exponent.
- **G2-T11-4** (negative) Ramanujan complexes give Ramanujan quantum expanders for free, and "it cannot fail" - the channel adds no new spectral values.
- **G2-T11-5** (registered) The converse needs *coverage*, not faithfulness; and one must remove the exceptional space, not just the fixed points.
- **G2-T11-7** (registered) The `A~_2` numerics: corrections, the degree audit `3chi + 3f_1 = 3f_0 + 3f_2`, and Cohn's criterion as a reusable technique.
- **G2-T12-1** (negative) Higher-rank RH is one-sided and the interior of the band is genuinely occupied; expect a band, not a line.
- **G2-T12-3** (negative) No universal functional equation in higher rank; outside type `A~` it degrades from circles to bands.
- **G2-T12-4** (registered) What is left in higher rank: Weil positivity as a bound, block by block.

### 2.16 Torsion, supertraces and the cohomological literature

Four literatures compute the same alternating-product shape and do not cite each other. The
notebook's own comparison is deliberately restricted to "alternating determinant structure". Two
warnings came out of the reading and they matter. Status: registered as warnings; the leads are in
section 3.2.

Explored:
- **G1-T7-8** (registered) Prior art for the graded picture: Deninger's grading with `H^1` carrying the zeros, and Connes's absorption sign.
- **G2-T13-2** (registered, a warning) The divisor is the degree-weighted Euler number, not the plain supertrace; the unweighted alternating sum vanishes identically.
- **G2-T13-3** (negative, a warning) The alternating count is not perturbation-stable: `m_R(0)` jumps from `4 - 2b_1` to `4 - b_1` under a generic conformal perturbation.

### 2.17 Prior art, novelty and citation hygiene

Three literature lanes plus byte-checked TeX. What is prior art: the `Ad(U)`-weighted Ihara zeta and
its Bass formula (Matsuura-Ohta), arbitrary-weight Bass for loopless graphs (Watanabe-Fukumizu),
representation-twisted zetas (Sunada), Ramanujan channels from LPS via Harrow, and the graded
fermionic cMPS bond itself. What was not found anywhere: a zeta attached to a quantum channel, the
reading "RH iff Ramanujan quantum expander", and the MPS/ring-norm reading. Status: registered, with
the absence claims resting on metadata-only searches.

Explored:
- **G1-T15-1** (registered) What is new and what is not; the prior-art verdict vocabulary; the standing preference for arXiv TeX over PDF.
- **G2-T14-3** (registered, novelty downgrade) The fermionic cMPS construction is not new; only the arithmetic reading can be claimed.
- **G2-T17-1** (registered) The prior-art verdict: no source attaches a zeta to a quantum channel, and the strongest explicit-Ramanujan paper never mentions a zeta.
- **G2-T17-3** (registered) The object is not literally a Stark-Terras L-function, because `Ad(U_i)` generates an infinite group.
- **G2-T19-4** (registered) Four citation hazards: Hastings' bound is only "in probability", the Kang-Li tarball, the Voros misidentification, the Eyler-Jun misattribution.
- **G4-T16-4** (registered) The AI-authorship statements in both Lindblad papers, as precedent for the repo's own prover-lane method.
- **G4-T16-6** (registered) Fifteen citation addresses that do not resolve, and two prior-art glosses needing rewording; no quoted string is misquoted.

### 2.18 Method, review discipline, tooling and reproducibility

The lab book is itself a research instrument: claims exist only as rows in `db/claims.tsv`, `proved`
requires a distinct reviewer, every quote needs a provenance row, and a local gate re-runs the fast
scripts. The productive pattern is to draft a little stronger than believed and let one xhigh prover
lane audit. The standing caveat is that both author and reviewer have so far been Claude models on
the review side. Status: registered and in force.

Explored:
- **G1-T15-2** (registered) Repo discipline as a research instrument, with the single-model-family caveat and the list of unreviewed shards.
- **G1-T15-3** (registered) Draft slightly too strong, let one xhigh lane audit, and what it caught (eleven, thirty-four and fourteen corrections in three campaigns).
- **G1-T15-4** (registered) No Fable subagents; killed agents leave usable transcripts, so do a cheap recovery pass before relaunching.
- **G1-T15-5** (registered) TJO's four standing working rules, including that length quantisation should come from a flatness-type condition.
- **G2-T19-1** (registered) The reproducibility discipline and its one exposed gap ("proved" means author != reviewer inside one model family).
- **G3-T20-1** (registered) Prove supplied hypotheses instead of citing them: four were provable in-file, and two had no quotable source at all.
- **G3-T20-2** (registered) Dependency rot: the printed status is derived from the deps, so a wrong dep list silently promotes a claim.
- **G3-T20-3** (registered) Provenance: the standing list of citations named but not byte-quoted.
- **G3-T20-4** (registered) Process and numerics discipline: undefined norms, shared RNG streams, missing scratch files, ledger rows reporting questions as errors.
- **G4-T16-1** (registered) Eight diagnostic scripts saved as regression oracles, explicitly not as evidence; one number is load-bearing.
- **G4-T16-2** (registered) Small normalisation and convention errors caught in flight (JSON export, gcd degree, the wrong trace space).
- **G4-T16-7** (registered) The Theorem 1 algebra review: six small repairs with wording supplied, including the pointwise-validity clause.
- **G4-T16-8** (registered) Discrimination controls: write a knowingly-wrong variant and confirm the test catches it.
- **G4-T16-9** (registered) Recovering a lost codex output by replaying `apply_patch` calls from the rollout log.
- **G4-T16-10** (registered) CAS strategy for cMPS checks: verify the Kraus identities symbolically, evaluate the norm numerically.
- **G4-T16-11** (registered) The four-lane design, including a parent audit lane that was erased from `SESSION.md` although it was executed.
- **G4-T16-12** (registered) The session's own lead lives outside the ledgered directory, in `HANDOFF.md`; and the claim-status baseline (357 rows).
- **G4-T16-13** (registered) Subagent shells had no network egress; route downloads through the parent.

## 3. Leads obtained

### 3.1 Ranked leads (top 40)

| # | Lead | Why it matters | Cost | Digest IDs |
|---|------|----------------|------|------------|
| 1 | Compute the `Gamma_0(N)` scattering determinant by Dirichlet character, check the Shor map acts on the bond as the level-`N` Galois symmetry, and settle the sector/character correspondence with nebentypus | It is a computation, not a theory problem, and if it works it identifies `K_S` with the Bost-Connes bond and unblocks the central conjecture | cheap computation + literature fetch | G1-T10-9, G4-T13-11, G2-T18-1 |
| 2 | Build prime-defined graded cMPS letters, compute the physical two-point function, read off its divisor; start by deforming the `2\|2` toy's letters under a finite-level character action | The only live mechanism explaining why all the odd modes would have the same width; the letters must come first and the zeros must come out | theory + cheap computation | G1-T6-10, G4-T12-11, G4-T17-6, G4-T10-1 |
| 3 | Supply H-CUSP-BRIDGE: a noncompact flow-resolvent realisation with finite-rank resonant data at `s_0 - 1`, a multiplicity-preserving first-band pushforward to Eisenstein Laurent data, and a positive modal pairing at the right centre | The single named missing hypothesis on the Selberg route, and now known not to be the eigenvalue bound but entirely the non-`L^2` scattering sector | theory | G1-T12-9, G3-T15-2, G4-T9-1, G4-T17-2 |
| 4 | Prove the four analytic conditions behind the flow-to-wave intertwiner `WT = TC`, joining Bonthonneau-Weich's meromorphic flow resolvent to Uetake's factored Lax-Phillips generator | It would derive the half-shift at operator level **without using RH**, and both endpoints are already cached locally | theory | G1-T6-11, G4-T9-4 |
| 5 | Prove the modewise cusp leakage estimate `\|\|jv\|\|^2 >= (1/2)\|\|v\|\|^2` on retained resonant modes, from automorphic cusp matching before knowing zero locations | The quantifier-correct form of the RH-sized inequality; combined with the FE pairing it forces width `1/4` | theory | G4-T10-9, G4-T10-6, G4-T10-2 |
| 6 | Compute Gram condition numbers of the zero eigenvectors at 3000, 10000 and 30000 ordinates, together with `sup_t e^{t/4}\|\|Z_t^{(N)}\|\|` and the integrated Gramian, and fit the growth | Cheap and decisive either way for the Riesz-basis metric route, and the same computation confirms or refutes the unreviewed `\|\|Z_t\|\| = 1` negative; ranked follow-up 1 in three separate lanes and never run | cheap computation | G3-T8-3, G4-T14-5, G4-T14-4, G1-T6-6 |
| 7 | Build the Schur complement of Mayer's transfer operator, separating the cusp coordinate, and look for a boundary pairing; the Hurwitz-zeta tail's leading residue at `s = 1/2` is rank one | The only operator in the notebook where the Riemann zeros appear at `rho/2` by a known mechanism, and the only place the postulated rank-one dissipation could be *derived* rather than assumed | cheap computation + theory | G1-T12-10, G3-T15-3 |
| 8 | Commit and run the prime-side screw-kernel test: build Suzuki's `Psi` from the primes alone, factor the Gram matrix, and look for an arithmetic recurrence in the Schur factors as the interval crosses `log p^k` | The one proposed experiment whose input contains no zeros, so it could discover structure rather than confirm RH; script fully specified and unwritten | cheap computation | G3-T19-3, G4-T11-7, G1-T6-8 |
| 9 | Solve the SHW rebound equations: `1 = mhat_Omega(lambda)` for an arithmetically natural `Omega`, invert `rho_infty ~ int Z(t) Omega Z(t)^* dt`, and test the invariant-sector condition `Tr(CX) = 0` on the zero-mode subspace | The vacuum choice is already excluded, so the rebound state is the named missing input; the invariant-sector test decides in an afternoon whether any reset completion can keep the zeros | cheap computation | G1-T6-5, G4-T13-12, G4-T17-4, G3-T10-2 |
| 10 | Write and prove the key lemma with a general displacement vector `eta`, and the Hermitian/complex-character version | One clean statement covers zeta and graphs at once and may remove CCM's own parity hypothesis; without the Hermitian case half of all L-functions are out of reach | theory | G4-T4-4 |
| 11 | Compute the extension-disc radius per window in `ihz`, and the Schur-complement radius of the window Loewner form in `zst`, against the measured `e^{-4 pi x}` convergence | It would distinguish a generic approximation-theoretic effect from genuine arithmetic; both proposed, neither run | cheap computation | G1-T13-9, G2-T15-5, G2-T15-2 |
| 12 | Search small regular graphs and window sizes for an anti-palindromic minimal eigenvector, i.e. decide whether "even-simple" is *equivalent* to Ramanujan | If it is an equivalence, CCM's auxiliary hypothesis is a restatement of the target, which changes how the whole CCM programme should be read | cheap computation | G4-T5-2 |
| 13 | Fit the under-resolved law on existing graph families, identify it as a discrete prolate/Slepian problem, and ask whether `1 - chi_4(lambda)` is its continuous limit | The one quantitative question a finite graph can transfer to zeta; the data is already collected and unfitted, and DPSS is the named candidate answer | cheap computation + literature fetch | G4-T3-3, G4-T3-2, G1-T13-8 |
| 14 | Settle the infinite parity question: can a conjugation-symmetric infinite flip set have atomic contribution above `-Lambda(n)` at every prime power (the "density at most 1/2" question)? | If positivity alone forces every parity, the grading of the whole divisor becomes *forced* rather than assumed, which is the difference between an ansatz and a theorem at the foundation of the fermionic programme | theory | G1-T7-3, G3-T1-3, G4-T15-15 |
| 15 | Use asymmetric Galois dephasing rates (which acquire an imaginary part) and an *even* Hamiltonian on the parity coherences as the source of the frequencies `gamma_n` | The book repeatedly says "neither jump family supplies the frequencies"; these are the only two mechanisms anywhere that do, and both sit unexploited in single paragraphs | cheap computation | G1-T9-4, G3-T17-1 |
| 16 | Build the family `B_i = G U_i G^{-1}`: inverse-paired, non-unitary, with a real `Sigma` spectrum, i.e. an unbroken PT symmetry | The smallest class where the functional equation and reality coexist *without* unitarity, which is exactly what a Phantasm transfer operator would need; and RH would read as "PT unbroken", where the PT literature has actual techniques | cheap computation | G2-T8-4, G4-T10-7 |
| 17 | Identify the Weil-LPS joint spectra with Hecke eigenvalues of weight-2 forms via LMFDB and Jacquet-Langlands; do the multiplicity prediction first, which needs no LMFDB | It would turn a numerical coincidence into an arithmetic identification and make the finite model's spectrum modular-form data; the publishable corner of that computation | literature fetch + cheap computation | G1-T3-6, G2-T1-1 |
| 18 | Assemble the Weil-LPS channels over all `p` into one object whose rings are the rational primes (the DG-GLOBAL question); the assembly must be non-product | The most direct route from the finite verified model to the infinite object, and the natural home for the "converging family of Ramanujan channels" strategy | theory | G1-T3-9, G2-T1-2 |
| 19 | Use the continuous-time Weil criterion: positive definiteness of every kernel `(nu(t_j - t_k))` for a generator, with `nu(t) = sum exp((lambda - kappa/2)t)` extended by conjugate reflection | Stated once and never used, yet it is the generator-side Weil condition the cMPS programme needs, and the only item on the tiny-Riemann checklist that does not presuppose knowing where the zeros are | theory + cheap computation | G3-T9-2, G3-T18-2, G2-T8-6 |
| 20 | Use Herglotz's representation `r(n) = C^* U^n C` as the *construction* of the Hilbert-Polya-like unitary once positive definiteness is established | The most direct available route from positivity to an operator, flagged in half a sentence and never taken; the distributional Bochner-Schwartz upgrade is what the continuous case needs | theory | G2-T8-9 |
| 21 | Reconcile Huang's termwise criterion with Toeplitz positive definiteness, exploit the "infinitely many even `k`" clause, and identify the test-function class that makes the Weil converse work | It determines whether the notebook has a new theorem or a repackaging, and the converse gap is the same gap the notebook inherits when it asserts "iff" | theory | G2-T8-7, G2-T8-8, G3-T9-4 |
| 22 | Pursue the exterior occupation parity: occupancies 0/1 with parity `(-1)^{sum k_p}` give `1/zeta(s)` as an absolutely convergent signed trace | The arithmetic wants a *different* grading from the one the programme uses, and this one gives "zeros = odd sector" an honest fermionic realisation with no boundary-functional games | theory | G3-T13-2 |
| 23 | Quantise Marcus-Spielman-Srivastava, or look for `xi` as an expected characteristic polynomial | The only known route to exact Ramanujan-ness with no arithmetic input, structurally the same shape of statement as "`H` is Hermitian", and never attempted | theory | G1-T3-5 |
| 24 | Find the analytic analogue of *slicing*: an operation on the Riemann channel under which eigenvalues multiply while the exponential loss stays sublinear in the degree, and exhibit its projector | Deligne's loss is killed by slicing over a one-dimensional base, not by tensoring; this is the missing "multiply" step and the programme's own steering statement made concrete | theory | G4-T11-4, G2-T6-1, G2-T6-6, G1-T11-12 |
| 25 | Build a bond-cutoff family of four-letter-type tensors whose divisor points accumulate | Named as "the only route to non-rational behaviour" from the finite-tensor side, and the bridge from the toy catalogue to an infinite object; never attempted | cheap computation | G1-T11-9, G2-T5-9 |
| 26 | Push the parity-dimension count `n_0 - n_1 = (D_+ - D_-)^2 >= 0` to a theorem | It may be the actual reason no CP realisation of the Artin-Schreier, Riemann or Selberg graded transfers has ever been found; one line, never pushed | theory | G3-T3-2, G1-T8-14 |
| 27 | Compute the divisor of the drift-plus-diffusion generator `L_kappa = -X + 2 kappa Cas + (kappa/2)W^2` for small `kappa` | A perturbed Selberg zeta; the one place the Selberg object and the Lindbladian picture could be joined, and the prover explicitly declined to assert either outcome | cheap computation | G3-T14-5, G1-T12-8 |
| 28 | Prove the global leafwise closed-range cohomology statement behind `df = (U_+ f) eta_+` | It would upgrade the Selberg determinant ratio from a divisor identity to an actual cohomological cancellation, the natural home for "zeros are fermionic" | theory | G3-T14-2 |
| 29 | Extend the cusp Gram/exit identity to generalized Laurent (Jordan) data at a synthetic double scattering pole, and track simplicity of the zeros as a separate hypothesis | Called "the quickest useful theorem" by its own lane; it avoids silently assuming simple zeros, which nobody in the notebook tracks, and a failure isolates a real obstruction | theory + cheap computation | G4-T17-1, G2-T8-5, G4-T10-8 |
| 30 | Define Kraus-weighted successor operators on the facets of a 2-complex by Kraus-weighting LLP's branching operator, and prove the alternating-product identity | The object appears to be genuinely open, is the natural home for the grading, and LLP's proof is combinatorial so it may survive operator weights | theory + cheap computation | G2-T9-11, G2-T9-2 |
| 31 | Prove `Z_X(u)^{-1} = SDet(...)` for a finite graph, joining Knill's graph torsion to the Ihara zeta, and state "`(1-u^2)^chi` is a Reidemeister torsion" as a theorem | It is exactly "zeta is a supertrace" on a graph, a publishable standalone result that would justify the notebook's central metaphor; Knill never mentions Ihara and the join is unclaimed | theory | G1-T14-2, G2-T13-5, G2-T13-1 |
| 32 | Redo the quantum Ihara-Bass as a Berezin integral over a chiral Dirac operator so the `chi` exponent comes out as an *index*, and reconcile the three origin stories of that exponent | It would make the grading structural rather than bookkeeping, and the off-by-one (`chi` versus `chi - 1`) would otherwise break any universal supertrace bookkeeping | theory | G2-T13-6, G2-T13-7 |
| 33 | Push the exact-rational `LDL^T` inertia route back into `zst` for every object with integer atoms, and rerun `x = 100` with the reworked memory footprint | It replaces the certificate step that failed at scale, and the headline would be "the primes up to 100 determine the first zero of zeta to 500 digits, certified" | cheap computation | G4-T7-1, G4-T2-2, G4-T2-3 |
| 34 | Implement `zst_weil_ab` once: one C struct for atoms, exponential-series kernels, pole terms and the identity shift, with the archimedean constants *derived* | Every new L-function then becomes a data builder rather than a new pipeline, and a graded transfer channel defined in the notebook could be run through certified code without new code | cheap computation | G4-T7-4, G1-T13-4, G4-T9-1 |
| 35 | Run the two endpoint Jordan witnesses (`K_3 box Q_3` and the ten-letter Pauli channel) through `ihz`, and compare CCM's positive form `tau - eps_N` with the letter-derived metric `G_C` on the same small graph | The one situation where Weil positivity holds but no Hilbert-Polya inner product exists; if the two forms agree up to congruence, CCM's construction and the notebook's metric are the same object | cheap computation | G4-T5-4, G1-T12-5, G1-T13-3 |
| 36 | Decide the cancellation question: construct a purely bosonic genus-two tensor on a larger bond with cancelling spectrum, or prove none exists | It decides whether "fermions are forced" is a theorem or an artefact of minimality, and the same question is the crux for the Riemann case | cheap computation | G3-T2-4, G2-T4-1, G4-T15-22 |
| 37 | Attack `conj:three-letter-universal` part (b): a natural selection rule for the genus-two tensor from the curve or its polarised CM data; solve the CM-diagonal ansatz symbolically | It is wish-list item (1) at genus two and would make the tensor a functor of the curve rather than of its L-polynomial; the CM-diagonal shape reduces to a 3x3 Gram matrix plus two rank-one couplings | cheap computation | G2-T3-12, G3-T4-4, G2-T3-1 |
| 38 | Run the periodic continued-fraction attenuation test: compare total attenuation per unit length for one-, two- and three-digit words | One mismatch disproves any proposed cusp coboundary identity; two sentences, cheap, never run | cheap computation | G3-T15-4 |
| 39 | Run a full-text prior-art search (Scholar full text, or a local grep over `refs/src`), and read the open-quantum-random-walk extension arXiv:2104.10287 in full | The whole novelty claim rests on metadata-only negatives, and that unread paper is the single cheapest place the "no quantum channel zeta exists" verdict could turn out to be wrong | literature fetch | G2-T17-2, G2-T17-4 |
| 40 | Byte-check Repka's decomposition of the tensor square of the complementary series | If true, "Ramanujan for the Lindbladian" is strictly weaker than temperedness and coincides exactly with Selberg's `3/16`, a striking and unexploited coincidence; currently "from memory, not to be cited" | literature fetch | G1-T8-12, G3-T16-1 |

### 3.2 All remaining leads, by theme

Every digest item of class LEAD-unpursued or PARTIAL appears below, grouped by the themes of section
2. Items that also carry a rank in 3.1 are marked `[rN]`.

**Foundations and what RH has become**
- **G1-T1-4** Realisability: which count sequences admit a side B at all (Manning, Dwork, Puri-Ward); a realisability criterion would say exactly which sequences have a finite side B.
- **G1-T1-5** The constraint table: one-dimensional, uniformly hyperbolic with exponent 1, infinitely many symbols, absorption sign - a five-line checklist, never systematically re-applied.
- **G1-T2-5** The master question: where does the unitarity come from, and must it? Deligne is the cleanest evidence that Hermiticity need not enter at all.
- **G1-T2-7** The elliptic curve over `F_2` as a cheap unit test for any side-B proposal; never formally applied.
- **G2-T19-3** The founding-session shift, `K_4` and prism numbers have no script in the repository; a three-line script would make them reproducible.

**The Phantasm and the Bost-Connes reframe**
- **G1-T4-2** Build the object as a necklace algebra intermediate between the Cuntz algebra `O_D` and Bost-Connes; made once, never used.
- **G1-T4-3** Find a model where a flat-connection / product-formula condition *forces* the ring lengths to be exactly `{log n}`; never attempted directly.
- **G1-T4-4** The Phantasm specification: the physical index is what is *not* determined, and the open problem is the inverse one (find the tensors from the ring spectrum).
- **G1-T5-4** The BC reframe itself: dilation time as the line of a cMPS, the critical KMS fixed point, the zeros as relaxation modes.
- **G1-T5-9** `conj:phantasm-both-halves`: a graded Lindbladian with the BC KMS state stationary and the zeros as odd relaxation modes; the notebook's central open conjecture, downgraded to `sketched`.
- **G1-T10-4** The Ramanujan-sum sector as the candidate `K_S`; ruled out with prime jumps alone, still a candidate, and item 0b' is unchanged.
- **G2-T14-4** Bost-Connes and the open identification with the Phantasm constructions; the `III_1 <-> II_infinity` type change across the critical temperature has never been used.
- **G2-T18-1** The BC inverse problem and its six named open sub-problems; build the map, do not fit an operator to known zeros. `[r1]`
- **G2-T18-2** The critical marginal is uniform and compatible under reduction, with a unique Weil-invariant matrix extension; compatibility is the hook for an adelic inverse limit.
- **G2-T18-7** Parity `P|x> = |-x>` is the only arithmetically natural `Z_2` grading on the BC side; identify it with the Phantasm's grading or rule it out.
- **G3-T1-1** The five-part audit template (what is forced, what cannot exist, what exists, what the prime chain gives, what the prototype shows) as the cheapest filter on any future candidate.
- **G3-T11-3** The Galois/cover test: a bond with supertrace `2P_+` carries only the zeta zeros while a Galois-symmetric one carries all Dirichlet L-zeros; cheap and decisive on any future Galois proposal.
- **G4-T13-4** The critical BC state is not a normal density; a type-III/GNS formulation with specified domains is required and has never been attempted.
- **G4-T13-11** The `Gamma_0(N)` scattering-sector / Dirichlet-character mismatch: counting sectors by characters is wrong without twisting. `[r1]`
- **G4-T13-13** Stage the BC limit: redo the cone calculation at `beta > 1` where the state is an honest density, and watch the dimensions as `beta -> 1+`.
- **G4-T13-14** Individual edge jumps restore Gibbs stationarity; write the generator out and ask whether any arithmetic content survives.

**Graded bonds, the sign and fermionic zeros**
- **G1-T7-3** Supertrace rigidity and the unrestricted infinite parity question. `[r14]`
- **G2-T4-2** The infinite-bond bosonic no-go: discharge or refute its analytic hypotheses for an actual Riemann cMPS; and a *sufficiency* construction is still missing.
- **G2-T14-1** Make the identification with Deninger precise (`H^0 = R`, `H^1` with the zeros, `H^2 = R`), then read his 2018 construction and ask whether it admits a channel description.
- **G2-T14-2** Connes: the Polya-Hilbert space appears from its *negative*; look for the zeros as missing lines in a continuum, not eigenvalues of a positive object.
- **G3-T1-3** Positivity forces the parities; the infinite flip set is the sharpest open problem. `[r14]`
- **G3-T2-3** What power traces cannot see: zero eigenvalues and nilpotent blocks are invisible to every trace criterion - an unexplored escape hatch from all the no-gos.
- **G3-T3-1** A supertrace is not a norm: the concrete missing object is a boundary condition turning a genuine Hilbert norm into a supertrace.
- **G3-T3-2** The parity-dimension obstruction to any doubled-bond realisation. `[r26]`
- **G3-T3-3** Zeta data do not determine the physical state; three tensors give identical ring norms, so something beyond the zeta must select the realisation.
- **G4-T15-15** Positivity does not fix the archimedean ladder's parity, and the infinite case needs a separation of atomic and diffuse parts. `[r14]`

**Lindbladian candidates, letters, the BC cones and the archimedean factor**
- **G1-T9-3** The ansatz: prime jumps + Galois dephasing at `2 gamma = 1/4` + an even-odd Hamiltonian; the most explicit shape ever written, with the missing piece named.
- **G1-T9-4** Asymmetric Galois dephasing rates produce a frequency with no Hamiltonian. `[r15]`
- **G1-T10-6** Matrix extensions of the BC phase marginal; the diagonal extension is Weil invariant *iff* `beta = 1`, and the coherent extension is unexplored.
- **G1-T10-9** The character-sector grading and the `Gamma_0(N)` computation (`conj:galois-graded-bond`). `[r1]`
- **G1-T10-10** The missing arithmetic map from the full BC algebra to the scattering bond, with five separately named construction tasks, none begun.
- **G3-T12-5** The reciprocal-zeta matrix element: three named steps would turn it into a spectral statement, and the conserved commutative family `{V_n}` was never explored as a structure.
- **G3-T12-6** The adelic route: make the substitution honestly (an actual adele-class orbit modulo the compact norm kernel) and tick the four missing ingredients in order.
- **G3-T12-7** The campaign's own hand-off list of four next computations, of which the boundary-functional item is the cheapest; no shard took any of it up.
- **G3-T13-2** The exterior occupation parity. `[r22]`
- **G3-T16-3** The archimedean completion: one pole versus two, and the Gamma-factor oscillator ladder that was never specified.
- **G4-T13-6** Siemon-Holevo-Werner's exit-space / reinsertion formalism, with the conservativity caveat, the nonstandard class, and one source sign error.
- **G4-T13-7** Arveson's "units" of a dynamical semigroup: a whole structural theory behind one quoted line, never looked at.
- **G4-T13-9** vom Ende on unique decompositions of generators: consulted, never used; it matters if one wants to claim an arithmetic generator's letters are *the* letters.
- **G4-T13-12** The missing invariant-sector argument for reinsertion. `[r9]`
- **G4-T15-23** The archimedean side of the yolo Lindbladian was never built, so every negative of 2026-09-14 is about the phase factor only.
- **G4-T17-7** An SDP feasibility test of the commutator-frame defect inside the BC cone, restricted to the *observable* subspace.

**Ring norms, curve counts and tensors genus by genus**
- **G2-T3-1** TJO's five-item wish list: item (1) is unanswered above genus 1, and the only input at every genus is the L-polynomial. `[r37]`
- **G2-T3-6** The genus-one Polya-Hilbert unitary is derived, but a self-adjoint logarithm needs a phase branch the curve does not specify.
- **G2-T3-9** The genus-two assumption bundle (CM type, polarised lift, Hodge adjunction, real closure): split it and discharge each item.
- **G2-T3-12** Three letters: a finite real feasibility problem, one certified curve, and `conj:three-letter-universal`. `[r37]`
- **G2-T3-13** Rosati positivity supplies the moduli and the PH metric; decide the gauge question for the certified `F_5` tensor.
- **G2-T3-14** The genus-two ring norms are Hilbert norms of fermionic ring states; upgrade `thm:cmps-twisted-supertrace` from sketched.
- **G2-T3-15** The curve sits inside the Jacobian as a non-product boundary: "bosonic product of tori plus a non-product boundary" is an undeveloped architecture for higher genus.
- **G2-T3-16** Cut rank, basis dependence and the restricted amplitude-locality conjecture; proving or refuting it would pin the exact boundary of the MPS formulation of the Weil conjectures.
- **G2-T3-17** RH as a single odd correlation length (`2/log q` for every fermionic mode), with entanglement and parent Hamiltonians; attackable with physics tools and never used.
- **G2-T3-18** The candidate Phantasm bond `C (+) H_{>0}`, and the trap that reading the FE as ket/bra exchange assumes RH.
- **G2-T5-1** The ten-condition ledger: a search for a tensor satisfying all ten simultaneously is now well posed and nobody ran it.
- **G2-T5-3** E0: a zero as the removal of a full subshift - a candidate mechanism for how fermionic zeros should arise generally, pushed nowhere.
- **G2-T5-6** Tiny L-functions as MPS; whether a genuine ring (trace) presentation of a Dirichlet L-function exists is open.
- **G2-T5-7** A literal count state needs 0/1 word traces; search for tensors whose configurations *are* the points.
- **G2-T5-8** The discrete-to-continuum passage is not free; making a cMPS whose zeta data live in the *state* rather than the normalisation is the open task.
- **G3-T4-4** The selection problem: no closed form without an extra principle; impose Hodge normality, Rosati self-adjointness or a physical-index normalisation as an extra equation. `[r37]`
- **G3-T7-2** The `pi`-adic carry automaton: what does it compute, and is there a weighted or graded version that also factors as `sum_s A_s (x) conj A_s`?
- **G3-T18-2** TJO's wish lists and the "tiny Riemann" checklist; item (4), Weil positivity plus symmetry, is the only route that does not presuppose knowing the zeros. `[r19]`
- **G4-T15-22** The `F_5` three-species rational contraction certificate, and the same machinery applied to `F_7..F_13`, the bosonic `C^{2|2}` case, and two-species infeasibility. `[r36]`

**Artin-Schreier**
- **G2-T2-2** A basis of `F_{q^n}` uniform in `n` making cubic traces local: "no candidate was found or searched for".
- **G2-T2-6** The even-`n` sign: two independent parity criteria, and a textbook-only gap; cite it or write the two-line proof.
- **G3-T6-4** The locality dichotomy and Conjecture T0.C; prove the growth half or find a non-quadratic trace function with bounded cut rank.

**Quantum Ihara-Bass, expanders and the Weil-LPS channels**
- **G1-T3-3** Side A of a quantum expander as free-group characters over long words - a possible *non-arithmetic* route to a Ramanujan bound, never followed.
- **G1-T3-4** Ihara-Bass for an arbitrary Kraus family, and what replaces Ramanujan without unitarity; four cheap unrun experiments, and levers 2 and 3 untouched.
- **G1-T3-5** The three known sources of Ramanujan-ness, and MSS as the one to watch. `[r23]`
- **G1-T3-9** Assembling the Weil-LPS channels over all `p`. `[r18]`
- **G2-T1-1** Hecke identification of the Weil-LPS joint spectra. `[r17]`
- **G2-T1-2** Assembly over all primes, the DG-GLOBAL question. `[r18]`
- **G2-T1-3** The exactly-Ramanujan claim rests on an uncited LPS source and numerically verified irreducibility; and the Ben-Aroya-Schwartz-Ta-Shma remark needs verifying.
- **G2-T6-5** A quantum expander is a Ramanujan twist of a bouquet; the global/pointwise eigenvalue distinction has never been exploited.
- **G2-T7-4** RH for the quantum Ihara zeta is exactly Hastings' bound - the load-bearing bridge, and it has had **no reviewer**.
- **G2-T7-5** What replaces `mu mu' = D-1` without inverse pairing; the decisive cheap experiment (random MPS, measure pole radii) has never been run.
- **G2-T7-6** Provenance of the general identity: do the shape-matching symbolically, fetch the NeurIPS supplement, and compare with Bordenave-Collins' "strongest form" operator identity.

**The graded Ramanujan property and the continuum**
- **G1-T8-12** The complementary-series threshold `3/4` versus Selberg's `3/16`. `[r40]`
- **G1-T8-14** Open items: a graded channel of *circle type* with a group-theoretic mechanism, a Kraus realisation of the graded spectral transfers, and a third continuum example with an infinite critical-line divisor. `[r26]`
- **G3-T5-3** The status table: which of the notebook's own objects satisfy the definition, with a minimal repair for each row, several never applied.
- **G3-T16-2** The reflection grading, the K-type grading, and whether the odd flow determinant *is* a Gamma factor - which would supply the Phantasm's archimedean factor from representation theory.
- **G3-T17-1** Odd letters must be jumps, and the even-Hamiltonian escape. `[r15]`
- **G3-T17-2** The divisor of an infinite bond: prove the compatibility theorem for a change of regular realisation, or accept the divisor is data-dependent.

**Selberg and the modular cusp**
- **G1-T12-7** Continuous Ihara-Bass in first-band operator form; a literal compression of the whole tower to one Laplacian determinant is still not supplied.
- **G1-T12-9** H-CUSP-BRIDGE and the `-3/4` versus `-1/4` centring, plus the unbuilt computational route (CCM on the modular surface). `[r3]`
- **G2-T16-2** The Lindbladian of the `sl_2` vector fields is the Casimir only on the K-invariant sector; extending beyond it is unresolved, and the Casimir reduction needs a quotable source.
- **G2-T16-3** The gap conjecture for the representation Lindbladian: decompose `pi (x) conj pi` for the Weil representation and read off the gap - the dilation-time version of the finite model.
- **G2-T16-7** Four open operator statements, of which writing the explicit formula for `Z_t` with all three bookkeeping terms is the prerequisite for any comparison with Selberg.
- **G2-T16-8** Six standard Selberg inputs carried as `assumed`, three convention hazards, and the instruction to fix one Laplacian sign convention before any computation.
- **G3-T14-4** The tower determinant and the missing continuous Ihara-Bass; build the anisotropic space so "resonance" means an eigenvalue of an actual operator.
- **G3-T14-5** The Lindbladian from the `sl_2` letters, and the perturbed Selberg zeta nobody computed. `[r27]`
- **G3-T15-2** The scattering sector: where the Selberg mechanism stops; a weighted-space form is *not* ruled out. `[r3]`
- **G3-T15-3** The Mayer transfer operator as the induced cusp-return operator, with the rank-one residue. `[r7]`
- **G3-T15-4** Uniform attenuation: coboundaries, the unbounded roof, isochronous loops, and the falsifiable continued-fraction test. `[r38]`
- **G4-T9-1** H-CUSP-BRIDGE, including its purely computational form through the CCM data model. `[r3]`
- **G4-T9-4** The flow-to-wave intertwiner `WT = TC`, with Bonthonneau-Weich and Uetake as the two endpoints and four analytic conditions to prove. `[r4]`
- **G4-T17-1** Cusp next test 1: extend the Gram/exit identity to generalized Laurent (Jordan) data. `[r29]`
- **G4-T17-2** Cusp next test 2: construct the actual noncompact first-band pushforward on regular data. `[r3]`
- **G4-T17-3** Cusp next test 3: derive the cMPS exit map `j` and `H` from a cusp boundary / Schur-complement / Mayer-tail construction - the only letters-first suggestion in that lane.
- **G4-T17-4** Cusp next test 4: SHW-style mixed rebound on the modal bond, the only route from the pure absorbing vacuum to a BC-style mixed stationary bond. `[r9]`

**Weil positivity and the Kraus pairings**
- **G2-T8-4** Weakened Hermiticity: inverse-paired non-unitary families as an unbroken PT symmetry, plus almost-normality as a third candidate substitute for self-adjointness. `[r16]`
- **G2-T8-5** Weil positivity is blind to Jordan blocks, so a Hilbert-Polya realisation needs *simple zeros* - an extra requirement nobody tracks. `[r29]`
- **G2-T8-6** The zeta dictionary entry, and the four things the passage to zeta needs (completed data, a distributional trace, the full explicit formula, the infinite converse). `[r19]`
- **G2-T8-7** Huang's Li-criterion: reconcile termwise nonnegativity with Toeplitz positive definiteness, and exploit "infinitely many even `k`". `[r21]`
- **G2-T8-8** The converse gap: which test functions separate the zeros; and "Li = Weil tested against triangular functions" is a recipe for generating new criteria. `[r21]`
- **G2-T8-9** Herglotz hands over the unitary for free. `[r20]`
- **G2-T8-11** Two unused positivity constructions: the Sonin projection ("positive definite by construction") and the graph explicit formula, never obtained.
- **G3-T9-4** The Riemann dictionary under Weil positivity and its four missing hypotheses; H-ZW is not available from finite interpolation or Bochner-Schwartz. `[r21]`
- **G4-T11-2** The increment Toeplitz reformulation and the sought sign-controlled Schur recurrence for the sum of archimedean and sparse prime pieces.
- **G4-T11-3** A two-line diagnostic (`Psi(2A)` and `4 Psi(A) - Psi(2A)`) that any claimed sum-of-squares factorization must pass; mentioned once, never used.
- **G4-T11-5** The exact bridge specification `<V(t), V(u)>_G = Psi(t) + Psi(u) - Psi(t-u)`, and its physical reading as time-bin Gram entries; it says which cMPS observable to calculate.
- **G4-T11-7** The prime-side screw-kernel positivity test, whose script exists only in a transcript. `[r8]`
- **G4-T17-5** The positivity lane's three ranked next tests, each with a pre-registered stop condition.

**The Riemann channel, Lax-Phillips, mixing and resonances**
- **G1-T6-2** The bridge Lax-Phillips = Bost-Connes at `beta = 1` + Sz.-Nagy-Foias: upgrade the boundary-phase identity to an operator identity and write the innerness argument in full.
- **G1-T6-4** The Holevo-Werner lift and the gauge lemma: it pinpoints that what is lost at the Sz.-Nagy-Foias step is *positivity*; the proposed computation was never run.
- **G1-T6-5** The SHW renewal generator: exit at the cusp, reinsert at a rebound state. `[r9]`
- **G1-T6-8** Fifteen resonance mechanisms ranked but never used, with Kotani's zeta string first (RH iff a positive-mass Krein string exists). `[r8]`
- **G3-T8-3** The metric converse: skew-adjointness, Riesz bases, and the Gram experiment nobody ran. `[r6]`
- **G3-T10-3** The model space is assumed, not constructed (H-LP); prove innerness and completeness of the mode system from the functional equation.
- **G3-T19-1** TJO's framing and the five genuine mechanisms, none yet identified with the Riemann cusp sector; the operative test is "which of our data does it use?".
- **G3-T19-2** One-exit inverse design: the missing arithmetic law for the residues `|v_k|^2` that would force equal imaginary parts.
- **G3-T19-3** Canonical systems, Krein strings and Suzuki's prime-defined kernel. `[r8]`
- **G3-T19-4** Wigner time delay and the removal of the common width; TJO's seed question (a physical quantity sensitive to equality of widths and computable from the primes) is still unanswered.
- **G4-T14-1** The Poisson-equation / mean-absorption-time certificate as the transferable item from the mixing literature.
- **G4-T14-3** Restricted mixing: find the initial-state class on which the argument does go through - the repair for the `||Z_t|| = 1` negative.
- **G4-T14-4** `||Z_t|| = 1` for every `t`, independently of RH; marked `[inferred]` and **unreviewed**, with a second reader explicitly requested. `[r6]`
- **G4-T14-5** The Gram / eigenvector condition number as a test statistic, not evidence. `[r6]`
- **G4-T14-8** The pure-fixed-point trace-norm reduction `||A - Pi||_1 <= 2||A - Pi||_2`, directly applicable to the vacuum-decay Lindbladian.
- **G4-T15-8** The abandoned scalar-weight non-backtracking laboratory: the cheapest model for "inverse pairing without Kraus".
- **G4-T15-13** Is there a Ramanujan property for a lead, or for continuous spectrum? Define it and test it on a Weil-LPS graph with one vertex opened.
- **G4-T17-9** A 3x3 non-normal toy: is a weighted-norm decay bound the same as a sectoral Lyapunov criterion?

**cMPS decay modes and the observable subquotient**
- **G1-T6-10** Ramanujan conditions in `Q` and `R`, and the four-mode sector: the most promising live candidate mechanism, unregistered. `[r2]`
- **G1-T6-11** Selberg's `L^2` Laplace mechanism versus Riemann's cusp leakage; the intertwiner and Uetake's completeness theorem are the concrete handles. `[r4]`
- **G1-T12-10** Mayer's transfer operator, the one place the zeros appear at `rho/2` by a known mechanism. `[r7]`
- **G4-T10-1** The target and the gap in one sentence: representation is solved, rigidity is not. `[r2]`
- **G4-T10-6** The minimal missing identity, stated cleanly: `A_obs^* G + G A_obs = -(1/2)G` plus an input/output divisor identity tying those poles to the zeros. `[r5]`
- **G4-T10-9** The modewise cusp leakage estimate. `[r5]`
- **G4-T12-11** The five-step arithmetic programme replacing "find a Lindbladian with the zeros as eigenvalues". `[r2]`
- **G4-T12-12** The boxed Ramanujan criterion for a boson-fermion cMPS, `A^dag G + G A = -2 Delta G` with `G > 0`; the open half is `G`, and the Weil/metaplectic representation is the natural candidate.
- **G4-T12-14** The `sigma`-metric dissipation identity: the GNS metric of the stationary state is the *wrong* metric.
- **G4-T17-6** Graded-channels priority 1: deform the *letters*, not the eigenvalues. `[r2]`
- **G4-T17-8** Graded-channels priority 4: a regulator theorem separating the four limits (bond dimension, prime cutoff, continuum spacing, temperature).
- **G4-T17-10** The four ranked tasks with nobody on them at shutdown, and one unverified citation path.

**Deligne-style positivity without Hermiticity**
- **G1-T11-12** Zeta has the positivity and the sign; it lacks the product. The Rankin-Selberg / symmetric-power route locates exactly what would have to be imported from the automorphic side. `[r24]`
- **G1-T11-13** The critical modulus `sqrt q` in three unrelated roles; making that coincidence a theorem would be the missing mechanism.
- **G2-T6-7** Rankin-Selberg, functoriality, and the three sources of Ramanujan-ness: any Phantasm must draw on one of them or introduce a fourth. `[r24]`

**The CCM window machine**
- **G1-T13-8** The `ihz` plan, the unanalysed Q-2 data, and what was not done; the under-resolved data is collected and unfitted. `[r13]`
- **G2-T15-2** The admissible next trace fills a disc and nothing beats it; the algebra is checked numerically rather than carried out. `[r11]`
- **G2-T15-5** Two cheap computations proposed and not run; (b) is the decisive one. `[r11]`
- **G4-T2-2** `x = 100`, the lost `x = 60` and `x = 80` tables, and the reference-zero ceiling above `k = 20`. `[r33]`
- **G4-T2-3** Scaling machinery: structured `O(N^2)` solvers, Chebyshev roots, free atoms, and LPS Cayley graphs as the target. `[r33]`
- **G4-T3-1** The prolate module: the part that touches CCM's missing proof; even a certified measurement of `||xi_lambda - k_lambda||` would be new data.
- **G4-T3-2** `Q-7`: is there any `Z`-side analogue of the prolate tower? DPSS and Terras-Wallace are the two named candidates. `[r13]`
- **G4-T3-3** `Q-2`: the under-resolved law, identified as a discrete prolate/Slepian problem. `[r13]`
- **G4-T4-4** `Q-8`: a key lemma with a general `eta`, and the complex-character case. `[r10]`
- **G4-T4-5** `Q-1`: is there a canonical `xi` in the over-resolved regime? The untested mechanism (perturb and let `delta -> 0+`) is named and cheap.
- **G4-T4-6** What is the continuous counterpart of using the lag one step outside the window? Asked of the theory lane, never answered.
- **G4-T5-2** `Q-3`: anti-palindromic minimal eigenvectors. `[r12]`
- **G4-T5-3** `Q-4`: the noise-floor growth law, its unrun inverse problem, and the precision needed near the Ramanujan boundary.
- **G4-T5-4** The invariant metric, endpoint Jordan blocks and multiplicity blindness; two verified endpoint witnesses have never been run through `ihz`. `[r35]`
- **G4-T6-3** `Q-6`: a Krein-space key lemma for mixed-parity divisors, the obstacle to running the chain on a graded quantum Ihara zeta.
- **G4-T7-3** Known bugs, test debt and library plumbing in `zst`/`ihz`.
- **G4-T7-4** One data model for every explicit formula, and the builders never written. `[r34]`
- **G4-T8-1** The graph has no Weil-style explicit formula in the literature, and the "graph gamma factor" reading is ours; a small publishable result sits here.
- **G4-T8-2** `U''` is a CMV/paraorthogonal object and the OPUC toolkit (Verblunsky, Szego, CMV) is sitting unused.
- **G4-T8-3** Verification gaps and unfetched sources, including Connes-Consani arXiv:2006.13771 on the single archimedean place.

**Simplicial complexes, buildings and higher rank**
- **G1-T14-2** The recommended object, a graded geodesic determinant; prove or disprove uniqueness, and join Knill's torsion to Ihara. `[r31]`
- **G2-T9-2** Kang-Yu's all-rank identity states no RH; proving a general-rank RH for its factors would be the first higher-rank RH-equals-Ramanujan theorem with a graded presentation. `[r30]`
- **G2-T9-3** "No zeta of a general complex" is a record of what was searched, not a theorem; inventing it is a legitimate contribution, endorsed at ICM level.
- **G2-T9-5** Finite cochain determinant cancellation holds for *any* degree `-1` map; the freedom in `h` is completely unexploited.
- **G2-T9-6** The tetrahedron obstruction and the vertex-collapse conjecture; compute `B_X` over a census of small 2-complexes and look for a non-building collapse.
- **G2-T9-8** The recommended object with specified data, uniqueness unproved.
- **G2-T9-10** Alternatives on general complexes: the combinatorial Ruelle zeta (the only object on an arbitrary complex with a Betti-number vanishing order), weighted complexes, and hyperedge size as a second grading axis.
- **G2-T9-11** The open object: a quantum (Kraus) zeta of a complex. `[r30]`
- **G2-T11-6** The `A~_2` anomaly: the identity holds where its hypothesis fails, and a descent theorem came out of it; how far it widens the class is unasked.
- **G2-T11-8** What the adversarial review explicitly did not check; two of the four items are load-bearing.
- **G2-T12-2** Kamber's `L_p` criterion: a continuum of Ramanujan notions with an iff spectral criterion - define `L_p`-expander for a quantum channel.
- **G2-T12-5** The hypothesis register of eight external theorems; H-STRONG means "Ramanujan complex" is ambiguous and every claim must say which.
- **G2-T12-6** Every determinant factor is a Langlands L-function, and `chi` vanishes at `q = 1` - a free `F_un` structural handle nobody has used.
- **G2-T12-7** The two-expression structure "surface versus curve"; ask whether Theorem 1's two forms line up with the vertex/edge dichotomy and whether a third is missing.
- **G4-T15-19** The drafted vertex-level Bass collapse, and the complexes never tested (the 7-vertex torus, the cone, the octahedron - seconds of compute).
- **G4-T15-20** Four literature routes for a complex zeta, handed over and never used, including the `eps_gamma`-signed geodesic zeta and the candidate role of the cyclic rotation `C_k` as `J`.

**Torsion, supertraces and the cohomological literature**
- **G2-T13-1** One shape, five categories: state the alternating-product-over-a-grading shape abstractly and ask what the notebook contributes as a fifth instance. `[r31]`
- **G2-T13-4** The special value is a torsion, and the `L^2` route is blocked; identify the notebook's analogue of the special value and ask what torsion it computes. Fetch Moscovici-Stanton.
- **G2-T13-5** Knill's super pseudodeterminant never meets the Ihara zeta - the unclaimed join. `[r31]`
- **G2-T13-6** The fermionic proof of Bass already exists (gamma-five, Witten index, sign-reversing involutions, `OSP(1|2)`); overlap fermions are a never-applied technology. `[r32]`
- **G2-T13-7** The `chi` exponent has three independent origin stories and an off-by-one; reconciling them is the only way to know whether it is universal. `[r32]`
- **G2-T13-8** A `+-1` sign carried by the orbit rather than by the coefficient space: try a per-orbit sign in the Euler product instead of a graded bond space.
- **G2-T13-9** Non-arXiv originals named but never obtained; Juhl's *Cohomological Theory of Dynamical Zeta Functions* is the single most relevant unread source.

**Prior art and novelty**
- **G2-T17-2** The search is metadata-only, so the absence claims are weak. `[r39]`
- **G2-T17-4** The quantum-walk line and the unread open-quantum-random-walk extension. `[r39]`

**Method, tooling and reproducibility**
- **G2-T19-2** Sixteen notation ambiguities, four of them substantive (channel normalisation, Ramanujan units, `q` versus `D-1`, what "Riemann channel" denotes).
- **G4-T16-3** Recovery snapshots, and the off-site copy that was never made.
- **G4-T16-14** The BLAS-thread CI fixture, the gate's thread pinning, and the maintenance-script exemption rule.

### 3.3 Small but consequential

Items raised once, in passing, or as an aside, that would change something if picked up.

1. **G1-T9-4** Asymmetric Galois dephasing rates acquire an imaginary part, i.e. a frequency, from a purely dissipative term. The book repeatedly says "neither family supplies the frequencies `gamma_n`"; this one does, and it is mentioned once.
2. **G3-T17-1** An *even* Hamiltonian can give odd coherences arbitrary oscillation frequencies. A prover aside that reopens the route "odd letters must be jumps" appeared to close.
3. **G1-T10-6** The diagonal BC residue extension is Weil invariant **iff** `beta = 1`. The critical temperature singled out by a finite symplectic requirement, unexploited.
4. **G1-T10-7** A two-prime coupling parameter invisible to all one-prime data: the natural slot for a global adelic constraint, never pushed past two primes.
5. **G1-T10-3** "Resolving each edge into its own jump `|pb><b|` restores a Gibbs fixed point but changes the model" - dismissed in half a sentence, and it is the exact trade-off between detailed balance and "the letters are the primes" (with **G3-T11-4**, **G4-T13-14**).
6. **G1-T8-8** In the `(13;5)` graded Weil-LPS case the extremal Hecke eigenvalue lives in the *odd* sector. One line of numerics tying graded parity to arithmetic extremality, never checked on another pair.
7. **G3-T4-6** The `(5;13)` reduced graded L-function `f_4 f_{-4}/(f_14 f_{-14})` fell out of an audit and was never identified arithmetically.
8. **G1-T14-2** Knill's graph torsion `SDet(D)` has never been joined to the Ihara zeta, although both compute the same shape; one paragraph of literature.
9. **G2-T13-8** A `Z_2` grading carried by the *orbit* rather than by the coefficient space: a per-orbit sign in the Euler product might be cheaper than a fermionic bond.
10. **G2-T12-6** `chi` vanishes at `q = 1`, so the `F_un` degeneration kills the torsion factor and leaves a purely combinatorial identity. A free structural handle nobody used.
11. **G2-T9-5** The cochain torsion cancellation holds for *any* degree `-1` map, not only `d^*`. A whole family of Bass-type identities is unexamined.
12. **G2-T11-2** On `Cay(Q_8, ...)` a totally non-flat chronological connection still reproduces the pure-gauge determinant to `1.1e-15`. Theorem or coincidence, nobody asked.
13. **G2-T9-9** The reviewer's sharpening (colour-preserving successors are exactly `L_E`) suggests an unbuilt colour-graded flow interpolating between the ordered and building rules.
14. **G3-T2-3** Zero eigenvalues and nilpotent blocks are invisible to every trace and supertrace criterion in the book - an unexplored escape hatch from all the no-gos.
15. **G3-T4-3** The genus-two threshold `q+1 >= 2g sqrt q` is *exactly* nonnegativity of the Weil lower bound on `N_1`: the construction dies precisely when the curve might have no points. Unexplained.
16. **G3-T12-5** The conserved commutative family `{V_n}`, indexed by the integers, was noticed only as an obstruction; what algebra it generates and what its joint spectrum is were never asked.
17. **G3-T15-1** The modular continuous term carries an extra `(K_0/4) h(1/4)` contact term sitting exactly at the spectral parameter `1/4` that the RH condition names. Never followed up.
18. **G2-T16-5** `phi(1/2) = -1`: a `-1` at the central point, precisely the kind of sign the grading is trying to explain; and `phi'/phi` folds into a `Lambda(n)/n` sum, the prime side reappearing inside the continuous spectral term.
19. **G3-T16-2** The McKean-Singer remainder `2(1 - e^{-2t}) Tr e^{-2t Delta_0}` is an explicit computable non-topological defect that *is* the Laplace spectral data; nobody asked what its zeta is.
20. **G3-T14-3** The negative-integer exceptional first-band parameters, where the tower divisor says genuine extra order sits at `-2, -3, ...`, are unexamined.
21. **G3-T14-2** The Ruelle divisor has a *parity-exchanging* reflection `nu(-s) = -nu(s)`, a second kind of functional equation that may be the more natural symmetry for a supersymmetric object; whether the Riemann side has an analogue is unexamined.
22. **G4-T12-14** The `sigma`-metric dissipation identity vanishes at `X = R_f`, so the stationary state's own metric can never certify uniform decay on a sector containing a fermionic jump. It contradicts the most obvious guess in the programme and has no evidence script.
23. **G4-T13-12** Whether reinsertion preserves the zero modes is a checkable linear condition, `Tr(CX) = 0` on that subspace. One afternoon decides whether any reset completion can keep the zeros.
24. **G4-T5-3** Recover the offending adjacency eigenvalue from the slope of `log(-eps_M)` alone: "if this works it is a genuinely new diagnostic". Never run.
25. **G4-T7-1** The secular function's tail roots cluster just past `N`, come in pairs and reach `31 N`; nobody asked what they are, yet completeness-by-count depends on accounting for them.
26. **G4-T5-4** `K_3 box Q_3` and the ten-letter Pauli channel are ready-made objects with verified Jordan blocks at the Ramanujan boundary - the one case where Weil positivity holds but no Hilbert-Polya inner product exists. Neither has been run through `ihz`.
27. **G4-T10-7** RH read as "the unbroken PT regime" for the arithmetic operator, where the PT literature has actual techniques for proving unbrokenness. Raised in one sentence and dropped.
28. **G4-T13-7** Arveson's "units" of a dynamical semigroup: a whole structural theory of no-event semigroups behind a single quoted line.
29. **G4-T11-3** The two-line diagnostic `Psi(2A)`, `4 Psi(A) - Psi(2A)` makes the cancellation mechanism visible before any large Gram matrix is built. Mentioned once, never used.
30. **G2-T8-9** Herglotz's `r(n) = C^* U^n C` hands over the unitary for free once positive definiteness is established. Flagged in half a sentence.
31. **G2-T8-7** Huang's "`h_k >= 0` for infinitely many even `k`" is a very weak hypothesis that might be far easier to verify for a channel, and nobody has used it.
32. **G2-T8-11** The Sonin projection gives `Tr(rho(f) S)` positive definite *by construction* - precisely the mechanism the positivity lane wants, and a concrete object nobody has touched.
33. **G2-T3-15** "Bosonic product of tori plus a non-product boundary" is an alternative architecture for higher genus, stated once and never developed.
34. **G2-T3-17** "Every fermionic mode has correlation length exactly twice the bosonic one" is RH in physics language, attackable with physics tools, written down once and never used.
35. **G3-T6-2** The Artin-Schreier transfer is a Clifford circuit, hence free and efficiently simulable - which may be exactly why the prototype is tractable and the zeta side is not. Nobody interpreted it.
36. **G3-T6-1** Is there a *zeta-side* permutation whose signature produces the minus sign, as the Frobenius permutation sign does for curves? The most TJO-shaped question in the campaigns, and nobody looked.
37. **G4-T16-12** `HANDOFF.md` is the paragraph a future session reads first, and the session's own main lead lives there rather than in any ledgered file.

## 4. Dead routes

Consolidated and deduplicated across the four digests, grouped by theme. One line each: the route,
the correction, and where it is recorded.

**Side A: prime-by-prime constructions**
- A Bose Fock space over `l^2(N)` with `h_0 = log n` as the Riemann gas: the `n = 1` mode has energy 0 and condenses at every temperature. (G1-T5-1)
- Wick-rotating the Bost-Connes Hamiltonian into Hilbert-Polya: `spec H = {log n}`; the relation is Fourier duality through the explicit formula. (G1-T1-6)
- Direct sums of circle rotations, product states, commuting dilations, the prime-chain Lindbladian: the spectrum is on the imaginary axis with decay rate 0, and for finite prime sets it is exactly the poles of the partial Euler product. Zeros exist only in the infinite product. (G1-T3-7, G2-T6-2, G3-T14-6)
- The prime circles' blindness is the zero-free line in disguise: `spec(A_S)` is disjoint from the zero set of the continued zeta. (G4-T15-4)
- Smearing the direct sum over prime circles to get a trace: never trace class, and the undamped comb is not tempered. (G2-T16-1)
- Commuting jumps restoring the Euler product: word multiplicities `Omega(n)!/prod k_p!` survive, and a parity insertion does not remove them. (G3-T13-1)
- The prime-chain detailed-balance Lindbladian as a source of zeros: real spectrum, Minkowski sums of M/M/1 bands, only on its specified weighted space. (G1-T5-8, G3-T11-2, G4-T15-17)
- Shell-diagonal Gibbs weights as stationary with reverse rate `u/p`: the rate is `u p^beta`, and the phase jumps still create coherences. (G3-T11-4, G4-T13-14)
- Forward phase dynamics selecting Haar: they converge weak-* to `delta_0`. And Haar is *not* the pure vector state of `e_0` on `C(Zhat)`. (G3-T11-5)
- A Levy-style small-jump completion of the BC measure at criticality: the divergence is at *large* jumps. (G3-T11-5)
- Shor's algorithm as carrying RH content: trivially rational zeta, and its periods are Dirichlet. (G1-T5-3)
- Exact finite-dimensional representations of the full BC algebra: `mu_n mu_n^* = I` forces `e(1/n) = I`. (G1-T10-8, G2-T18-3, G4-T13-8)

**The yolo phase-side Lindbladian**
- The guess as a whole: grading not preserved (explicit odd cross terms for every prime), no Gibbs fixed point, rates `1/p` give no normal semigroup, a prime cutoff is not a bond cutoff, a parity closure is not the `Q^x` quotient, and the vacuum generating functions have no singularity in the strip at any cutoff. (G1-T10-1, G1-T10-3, G3-T12-1, G3-T12-2, G3-T12-3)
- "The prime jump *is* the Shor/Galois map" unqualified; and Gauss-vector coherences as scalar Lindblad modes (an extra `1/p`, residual 0.61). (G3-T12-1, G3-T12-4)
- `c_b(1) = mu(b)` as a vacuum-to-shell jump overlap: all overlaps are nonnegative and put zeta in the *numerator*; evaluation at 1 is unbounded. (G3-T12-5)
- A shrinking ratio `F/(1/zeta_P)` as evidence of a hidden reciprocal-zeta factor: that is a partial Euler product outside its half-plane. (G3-T12-3)
- The Ramanujan-sum sector *with prime jumps alone* as the identification of `K_S`. (G1-T10-4)
- Connes 1999 as supplying an unconditional periodic-orbit trace for this ring norm: it proves a local cutoff formula and a finite-set-of-places formula only. (G3-T12-6)

**Symmetry as a source of rigidity**
- Imposing Weyl-translation covariance on the Phantasm: the cone collapses to the depolarizer and the oscillatory modes vanish. (G1-T10-7, G2-T18-5, G4-T17-7)
- Arithmetic covariance alone forcing a uniform odd rate: the `p = 7` witness has full Weil, Galois and parity covariance with unequal odd rates (and the assertion fails at `p = 5`). (G1-T10-7, G2-T18-5)
- Selecting the adelic coupling by marginal compatibility: the family `L_c` has identical one-prime restrictions. (G2-T18-6)
- The reset test `-(B sigma + sigma B^*) >= 0` as a no-go: it binds only a fixed no-event `B` with a scalar reset. (G1-T10-8, G2-T18-4)
- SPT / cohomological protection as a source of RH: protection is sign data, RH is modulus data. (G1-T13-1)

**The Riemann channel and Hilbert-Polya**
- A Stinespring form of `Z(t)` with prime dilations as jump operators: it is a no-event semigroup and has no jumps at all. (G1-T6-3)
- RH as a worst-case mixing-time statement: `||Z(t)|| = 1` for all `t`, with or without RH; the absorbing-vacuum channel has infinite worst-case mixing time. (G1-T6-6, G4-T14-4)
- A bounded renorming of `K_S` into a Hilbert-Polya space: the Cauchy Gram condition number grows from 10 to 700 across 3000 zeros; a Hilbert-Polya space must be a different completion. (G1-T6-6, G3-T8-3)
- A spectral line alone giving anti-Hermiticity, or formal skew-symmetry constraining the spectrum: Jordan counterexample, and `-d/dx` on the half-line. (G3-T8-3)
- The vacuum rebound state: the stationary state is pure, entanglement trivial, the renewal integral divergent, and the model realises the *double* of the forced datum. (G1-T5-7, G3-T10-2, G4-T13-10)
- A stable graded bond with a single homogeneous rank-one exit: one parity sector is forced to evolve unitarily. (G4-T13-5)
- Choosing the rebound state, or circle return factors, to tune the spectrum. (G3-T10-2, G3-T14-6)
- `|Tr Z(t)|^2` as a form factor or route to pair correlation: not a distribution; the pair list violates the growth condition. (G1-T5-7, G3-T10-1, G4-T15-18)
- The trivial set `S` taken as the poles of `xi` at 0 and 1: `xi` is entire, so `S` is empty and `{0, -1/2}` needs an artificial augmentation. (G3-T9-4, G4-T15-9)
- Purified-Gibbs / Witten Lindbladians: the coherence rates are the spectrum of a self-adjoint `H >= 0`, hence real. (G4-T14-9)
- A SUSY/Witten-index graded splitting as a ring-norm mechanism: the supertrace cancels the whole nonzero spectrum. (G4-T14-7)
- Mining the Lindblad-mixing literature for expanders, Ramanujan bounds or cutoff: neither paper contains any. (G4-T14-10)
- "GUE positions plus equal widths is the fingerprint of scalar loss": a tuned one-port realises equal widths at arbitrary positions; the information is in the *couplings*. (G1-T6-8, G3-T19-2, G4-T15-11)
- Positive canonical energy making a J-unitary monodromy elliptic; local Euler factors as inner functions; the Thouless reading of the Euler product; complex scaling as a width mechanism. (G3-T19-5, G4-T15-11)
- Deriving equal widths from Hecke self-adjointness continued to `rho/2`, or importing Deligne without identifying the cusp sector. (G3-T15-5)
- "Every matrix Hermitian therefore real-rooted average characteristic polynomial": `H = +-I_2` gives `x^2 + 1`. (G3-T19-5)

**The grading**
- The expectation of `(-1)^F` as the carrier of the supertrace sign: it is identically `+-1` for parity-homogeneous boundaries; the supertrace lives on the *doubled* bond. (G1-T7-5)
- "Fermionic primes give zeros on `Re s = 0`": true of the finite factors only. (G1-T7-7, G3-T13-2)
- Bosonic (ungraded) ring norms for genus `>= 1`, and any ungraded fixed-finite-bond MPS: excluded by the residue argument. (G1-T7-2, G3-T2-2)
- "Nonnegative coefficients forbid a numerator": false, `(1-u)/(1-2u)`; the operative hypothesis is "is an honest trace sequence". (G2-T4-3)
- The drafted odd-mode bound `sum_odd |mu|^2 <= 2 Tr(E_++) Tr(E_--)`: false, 173 of 400 random counterexamples; the script computed Hilbert-Schmidt norms while calling them traces. (G1-T11-7, G2-T4-1, G3-T2-4)
- The trace version `2 Tr S_+ Tr S_-` of the infinite-bond bound: it needs positivity of `S_+-` on Hilbert-Schmidt space, which complete positivity does not give. (G2-T4-2)
- A doubled-bond CP (cMPS) realisation of the Selberg flow: both flat supertraces are negative distributions; the object is a graded *spectral* transfer. (G1-T12-8, G3-T3-1)
- Closing the infinite-parity case by Landau on the diffuse part: blocked by negative prime atoms; proved only under domination. (G3-T1-3, G4-T15-15)

**Ring-norm tensors and curves**
- "Fixed finite lattice tensors give only supersingular zetas": explicitly false, refuted by the campaign's own ordinary tensors. (G2-T3-16, G3-T2-5)
- A nonnegative-weight automaton, finite weighted adjacency matrix or trace-class operator counting elliptic-curve points: impossible; and the failure of the carry automaton is *not* unbounded carries (they are bounded). (G1-T1-4, G2-T3-8, G3-T7-2)
- "The permutation `k -> M^T k`": not a permutation, injective of index `q`, only finite orbit `{0}`. (G2-T3-5, G3-T7-1)
- The literal geometric placement of genus-two cohomology, the vacuum ansatz `a_1=1, B_1=0, a_2=0`, and the polarisation-trace-line ansatz: all impossible. (G1-T11-7, G2-T3-10, G3-T4-3, G4-T15-21)
- "Only transcendental tensor entries work": refuted by real-closed-field transfer. (G3-T4-4)
- Integral ideal classes as complex MPS gauge orbits: complex tensors forget the ideal class. (G2-T3-7, G3-T4-4)
- Least-squares residuals and four-digit printouts as certificates; eigenvalue thresholds reading a nilpotent block as nonzero modes. (G2-T3-12, G3-T4-3)
- The minimal bond for genus `g` being `C^{1|g}`: the condition is `mk >= g`, and at `g = 4` the `2|2` bond wins. (G2-T4-1, G3-T2-4)
- Reading the functional equation as ket/bra exchange: conjugation equals `rho -> 1 - rho` only on the critical line, so it would assume RH. (G2-T3-18, G3-T10-3)
- Inverse-closed letters alone giving the functional equation for a raw doubled transfer: `B = diag(1,2)` counterexample; the mechanism lives in the non-backtracking construction. (G1-T11-9, G2-T5-2, G3-T9-2)
- Closing the Horner automaton into a trace: it imposes a residue-automaton return condition, not Frobenius orbits. (G2-T5-6, G3-T4-5)
- The swap L-function of the pair shift as an Artin factor: a *directed* voltage cover is. (G1-T11-9, G2-T5-6)
- "Even = trivial character, odd = nontrivial" as a general theorem: refuted by the Ihara cover, where every physical mode is even. (G2-T2-5, G3-T4-5)
- An individual exponential-sum L-factor (Kloosterman, Artin sign) as a positive norm: only the curve completion is. (G3-T4-2, G3-T4-5)
- Treating unique stationarity, whole-bond gauge and mixing as one condition: they are three. (G2-T5-2, G3-T18-1)
- Positivity plus a functional equation forcing RH: explicit CPTP counterexample with poles `{1, 1/16}` and odd eigenvalues `{8, 2}`. (G2-T5-5, G3-T18-1)
- A unique stationary state implying mixing: a printed periodic channel refutes it. (G3-T18-1)
- A finite bond giving a nonrational `Z`, an atomic prime comb, or infinitely many divisor points; and a single simple pole with an uncompleted self-reciprocal FE. (G2-T5-9, G3-T2-5, G3-T16-3)
- A matrix logarithm as a cMPS embedding, or a singular `E` having an exponential at positive time. (G3-T17-3)
- "Half entropy is RH": it is C5 without C4 - an RH-shaped spectrum with no functional equation selecting the centre, and not invariant under growth shifts. (G4-T15-25)
- On a `1|1` bond, kinetic regularity, Lindblad normalisation, uniqueness and the exact half difference cannot all hold. (G3-T17-3)

**Artin-Schreier**
- The founding sign law `alpha_i = -lambda_i(E)` and the orchestrator's conjugated replacement: both false, with exact endpoint criteria `P_g(-1) != 0` and `P_g(-eta(-1)) != 0`; and the drafted failure class "`q | n`" is wrong. (G1-T11-2, G2-T2-4, G3-T6-1, G4-T15-14)
- The drafted graded super-transfer block: supertrace `-2` where the projective count is 10; and the point at infinity is not a character sector. (G3-T6-3, G4-T15-14)
- "The entries are roots of unity" as the reason the transfer has finite order: insufficient (zero entries, normalisation). (G2-T3-2, G3-T6-2)
- "Up to a phase" Weyl covariance as characterising the Weil implementer: centred exact covariance is required. (G4-T15-14)
- The cut-rank bound `D` across a ring cut: it is `D^2` and sharp; the growing table was a basis artefact. (G2-T3-16, G3-T6-4)
- A fixed local tensor for cubic or higher Artin-Schreier traces in the shift basis: the trilinear form is non-local and `n`-dependent. (G1-T11-3, G2-T2-2)
- Dwork's `p`-adic operator as a route to RH: it sees Newton polygons, not complex absolute values. (G1-T11-3, G2-T2-1)
- Assuming a self-dual normal basis in the sign law: it does not exist for even `n`, which is the whole point. (G3-T6-1)

**Graded Ramanujan**
- Quantum expanders on ungraded bonds as candidates for zeros: ungraded ring zetas have poles only, and an all-even-letter channel has at least two stationary states. (G1-T8-1, G3-T2-1)
- An odd-sector Alon-Boppana bound: refuted; `rho(Phi_1) = 0` families with unbounded bond exist, and Hastings needs nonnegative word traces. (G1-T8-7, G3-T5-2, G4-T12-6)
- "Band bound iff divisor statement", sector by sector: false without a no-cancellation hypothesis; a degree-14 example cancels an out-of-band mode. (G1-T8-3, G3-T5-2, G4-T15-28)
- The direct (non-lifted) qubit transfer as a curve zeta: its zero at `-2` is off the circle. (G1-T8-5)
- "A circle numerator is a Weil polynomial or a curve": `N_P(1) = 16/3`, and `(1-3u)^4` over `F_9` would force `-2` points. (G3-T5-2, G4-T15-29)
- The Weil-LPS examples as curves: one reduces to numerator degree 4 (not 36), the other has uncancelled poles on the circle. (G4-T15-29)
- The reflection (`PGL_2(R)`) grading and the K-type grading as the Selberg/Riemann flow grading: the first puts the geodesics in the even sector, the second makes the flow generator odd and its graded heat trace strictly positive. (G1-T8-13, G3-T16-2, G4-T9-8)
- "Exact sampling makes divisor RH and FE mesh-independent": false without a no-aliasing hypothesis. (G1-T8-10, G3-T17-1)
- "Each odd letter has a fixed `sqrt(h) R` limit": only the collective Hilbert-Schmidt bound holds. (G3-T17-1)
- Equal spectral radii forcing net cancellation; every structural period mode being even; every odd constituent supplying a zero: all false with one-line counterexamples. (G3-T5-1, G3-T5-2)
- The Lie-walk threshold `1/2` (it is `1/(2d)`); "tempered iff every geodesic exponent has real part `-1/2`"; the odd ladder starting at `n/2`. (G3-T16-1, G3-T16-2)
- "The divisor is the union of scalar correlation poles", or a canonical scalar signed measure for continuous spectrum. (G3-T17-2)

**Selberg and the modular cusp**
- The Ruelle zeta (full transverse forms) and the all-odd tower as graded Ramanujan objects: two bands shifted by one, so FE and Ramanujan fail even under Selberg's `1/4`. (G1-T12-3, G3-T5-3, G4-T9-8)
- The single total pushforward form on the first band: degenerate on partner branches; branchwise orthogonalisation is required, on graphs too. (G1-T12-5, G3-T14-3, G4-T9-8)
- `Omega = X^2 + U_+U_- + X` and `J X J^{-1} = -1 - X`: wrong ordering and wrong sign. (G1-T12-5, G3-T14-3)
- The `e^{t/2}` rescaling to unitarise the modular scattering sector: impossible under any positive norm; under RH the flow centre is `-3/4`, not `-1/4`. (G1-T12-9, G3-T15-2)
- Truncated Maass-Selberg positivity as an RH criterion: positive throughout `0 < Re s_0 < 1/2`. (G1-T12-9, G3-T15-2, G4-T9-8)
- "First-band cusp states push forward to `E(z, rho/2)`": undefined at a pole, and the Laurent coefficient is not in `L^2`. (G3-T15-2)
- Hoping the Selberg `mu >= 1/4` gap settles the Riemann sector: `mu = 3/16 + gamma^2/4 + i gamma/4` is nonreal even under RH. (G4-T9-2)
- "Selberg's `1/4` is open for `PSL_2(Z)`": false, known (Booker-Lee-Strombergsson); what is open is the congruence case. (G3-T14-3, G4-T9-8)
- The drafted tower dictionary: the flat trace is `+D'/D`, and the graph analogue of `D` is `det(1-uT)`, not the zeta. (G3-T14-4, G4-T15-1)
- Including the constant mode `j = 0` in the first band: false on every compact connected surface. (G4-T15-2)
- Identifying trace resonances with Pollicott-Ruelle resonances; replacing the modular scattering band by the compact Laplace band; "uniform curvature therefore RH". (G3-T14-4, G3-T15-2)
- The Casimir as a global Lindbladian on the full quotient: it carries the compact direction with a minus sign; and squaring projected tangent vectors misses the drift. (G2-T16-2, G3-T14-5, G4-T15-3)
- A first-order flow generator called a Lindbladian: it is anti-self-adjoint; the dissipation must be constructed. (G4-T15-4)
- "The cusp term of the modular trace formula is the trace of the Riemann channel damped at rate 1/4": corrected to an identity of prime measures only, and the atoms are *dips* with a `+1/2` boundary constant. (G2-T16-6, G3-T15-1, G4-T9-7)
- Taking the discrete-series weight down to 1 in `D_k^+ (x) D_k^{+/-}`: needs a covering group or a projective representation. (G4-T9-8)

**Weil positivity and the Kraus pairings**
- "Both pairings iff a scalar multiple of a unitary": it is `B^dag B = I` on the nose; `B = 2I` disproves the drafted version. (G1-T13-2, G2-T8-3, G3-T9-2, G4-T15-7)
- An inverse-paired Kraus counterexample to conjugation closure: none exists - every `Ad`-family is conjugation-symmetric, so reality is free. (G2-T8-3, G3-T9-2, G4-T15-7)
- An `n = 1` adjoint-paired non-scalar-unitary example: logically impossible. (G4-T15-7)
- Hastings' bound with the *unenlarged* trivial set: false for every unitary family, since `Phi(I) = I` makes `D` an eigenvalue. (G3-T9-1)
- The Dyson product without free propagators between jumps: false for noncommuting `K` and `R_j`, visible from second order. (G2-T8-2, G3-T9-3, G4-T15-6)
- Deducing the infinite Weil converse from finite interpolation or Bochner-Schwartz: unavailable, `F(0) = infinity`. (G3-T9-4)
- Adjoint-paired non-unitary Kraus families having a functional equation: none exists; "Ramanujan" there can only be the one-sided bound. (G1-T3-4)
- "Every zeta has side A, a nonnegative count of rings" as a universal premise: true in the stated Kraus settings only, and logically independent of Weil positivity. (G4-T15-10)
- A sum of independent positive prime-power blocks for the Suzuki kernel: each block is indefinite at first visibility. (G4-T11-1)
- Re-proving `Psi(t) >= 0` as new: Suzuki already has `Psi >= 0` iff RH. (G4-T11-2)
- Ordinary tensor powers as Deligne-style amplification (`epsilon_k = kc`), and Rosati positivity as an independent proof (the moduli are an input). (G4-T11-4)
- Any bounded-generator, time-homogeneous, finite-dimensional cMPS amplitude model claiming the exact Suzuki covariance: real-analytic on the diagonal, but `Psi` has prime kinks. (G4-T11-6)
- Beating the extension disc, or using integrality to pin the next trace of a `q`-regular graph: one Schur parameter per lag, and rescaling defeats integrality. (G1-T13-9, G2-T15-2, G2-T15-3)
- Extrapolating the higher traces of zeta: the estimator question is circular - a better estimator means more primes. (G2-T15-4)

**Deligne, graphs and the product**
- Deligne's pointwise (purity) theorem for graph twists: false, with an explicit bouquet counterexample satisfying all three hypotheses. (G1-T11-11, G2-T6-4)
- Commuting holonomies or commuting Kraus unitaries as a source of expansion: uncontrolled invariants in tensor powers. (G1-T3-8, G2-T6-2)
- Kraus operators from `PSL(2,Z)` group generators (Jones, Thompson): expanders but not Ramanujan beyond `p = 7`; a presentation is not arithmetic. (G1-T3-10)
- Looking for an `X x X` with zeta as its slice: there is none. And Soule's zeta over `F_1` is the wrong small case (all zeros real). (G1-T11-12, G2-T6-1)
- Grothendieck's standard-conjectures route: open; the inner product making Frobenius normal is not known to exist above dimension one. (G1-T2-5, G2-T6-4)
- Self-adjointness as a route to the bound: every adjacency matrix is symmetric and `C_16 x K_2` still fails. (G1-T2-2)
- Kraus structure alone forcing degeneracy of the decay rates: some arithmetic rigidity has to enter. (G2-T6-7)
- Algebraic-integer recognition of the Weil-LPS joint eigenvalues from five-digit output: tautological, the matrix is integral by construction. (G1-T3-6)

**Simplicial complexes**
- A vertex-level polynomial Ihara identity for a general complex: a building phenomenon only; `partial Delta^3` forces poles at `u = -1, +-i`, and the octahedron repeats it. (G1-T14-3, G2-T9-6, G4-T15-19)
- "Links are generalised polygons of the same parameters" as the collapse class: explicitly declined. (G2-T9-6, G4-T15-19)
- The unrestricted ordered-cell flow as the building's successor rule: outdegree `2q^2+q` against `q^2`; opposition is strictly stronger than non-incidence. (G1-T14-3, G2-T9-9)
- "The total graded zeta equals Kang-Li's zeta": it is the completed vertex L-function. (G2-T9-9)
- Identifying the cochain product's Euler exponent with `chi`: it is `sum(-1)^i (i+1) f_i`, already wrong on one edge. (G2-T9-5)
- "The zeros are exactly the odd eigenvalues": false without the reciprocal, sign, multiplicity and cancellation qualifications; on the vertex side everything cancels. (G2-T10-1, G2-T10-2)
- `k`-cells literally realising `H^{k-1}` with Weil weight: only the parity exponents match, and one constituent can contribute to two circles. (G2-T10-3)
- One pure fermion determinant with flow parity equal to cell chirality: does not exist; the total is a Berezinian, and the building "Laplacian" is not `(d+delta)^2`. (G2-T10-4)
- Covariant weights on the full Cayley complex: pure gauge; use voltage quotients. (G1-T14-3, G2-T11-2)
- `R = pi (x) conj pi` embedding in a regular representation, or a scalar determinant identity restricting to every irreducible: only spectral support transfers. (G2-T11-3)
- Asserting a fractional Euler exponent when simplex stabilisers exist. (G2-T11-3)
- Removing only the channel fixed points in the Harrow transfer: remove the exceptional space; and one faithful `pi` does not detect Ramanujan. (G2-T11-5)
- Reading building zetas as curve zetas, or expecting higher-rank RH to have a duality: no honest curve-weight dictionary, and the type-(e) block has two radii at once. (G1-T14-3, G2-T12-3)
- Reading Kamber's bound as an upper bound on pole radii (it inverts), or `|s| = 1` as an invariant (`Im s` is defined mod `2pi/log b`). (G2-T12-2)
- Expecting factor-by-factor RH from Kang-Yu: that paper states no RH. (G2-T9-2)
- Arbitrary Kraus weights preserving the building Euler/Hecke formula: they preserve only the Schur identity; the cochain cancellation needs an invertible *flat* local system. (G2-T11-1)
- Expecting the quantum twist of a Ramanujan complex to *do* something: `Phi_1` is a sub-multiset of the untwisted adjacency spectrum, so Ramanujan complex implies Ramanujan quantum expander automatically and the channel adds no new spectral values. (G2-T11-4)
- Expecting higher-rank RH to be a single-circle statement, or the interior of the band to be empty: poles with `0 < |Re s| < 1/2` genuinely occur, and for `PGSp_4` the edge and chamber factors give only bands. (G2-T12-1)
- Treating the hypergraph zeta as a new object (`zeta_H(u) = Z_{B_H}(sqrt u)`), or expecting a Ramanujan notion from the combinatorial Ruelle zeta, or a Bartholdi zeta of a complex. (G2-T9-1, G2-T9-10)
- Knill's super pseudodeterminant as the `u -> 1` limit of the zeta or of the Euler factor: one edge gives three different numbers. (G2-T13-5)
- The `L^2`/Fuglede-Kadison route to a zeta formula: no direct relationship between `L^2`-torsion of a matrix and its entries. (G2-T13-4)
- A naive plain alternating Euler characteristic as the divisor: it vanishes identically; the degree weight is needed. (G2-T13-2)
- "The zeros are the odd cohomology" as a stable statement: the alternating count jumps under a generic conformal perturbation. (G2-T13-3)

**CCM sidequest: method**
- Interval `LDL^T` inertia certification at scale: input radii amplified by the squared condition number. Replaced by verified positive definiteness of a deflated matrix. (G1-T13-5, G4-T7-1)
- Global root isolation by ball arithmetic, and completeness by search range: the normalisation amplifies `xi` by 18-28 digits, and roots occur far beyond the last pole. Use point candidates plus tiny-interval Newton, and completeness by count. (G1-T13-5, G4-T7-1)
- Plain interval evaluation of the cancelling secular derivative: useless; a mean-value form is mandatory. (G1-T13-5, G4-T7-1)
- The QR candidate generator; `arb_mat_eig_enclosure_rump` for the eigenvector; the similarity `D T D^{-1}`; `nf_elem` exact arithmetic over `Q(sqrt q)`. All replaced or judged worthless. (G4-T7-1)
- `arb_fmpz_poly_complex_roots` on a raw characteristic polynomial: never terminates on a repeated root. `acb_mat_eig_multiple_rump` as a primary truth route: failed at `n = 24`. (G1-T13-6, G4-T7-2)
- Dyadic bisection of `[0, pi]`: split points land exactly on graph divisor angles. (G1-T13-6)
- The window heuristic "`M >= diameter`": superseded by the exact anchor `K = R + 1`. (G4-T5-1)
- The self-adjoint angle operator and the nilpotent truncated shift as the discrete `D`: measured commutator rank 3, and `spec(S) = {0}`. (G4-T4-3)
- `eta` as all-ones in either basis, and `CS` Proposition `finmain` taken literally: the determinant becomes `xi`-independent, or returns `xi` rotated by one. (G4-T4-3)
- A canonical `xi` in the over-resolved regime by minimal degree or minimum norm: both break the circle. (G4-T4-5)
- Interpreting the output for an irregular graph: structurally impossible; `pt.err` saturates near 0.20. (G4-T6-4)
- Running the chain on a mixed-parity retained divisor: indefinite by construction, independently of RH. (G1-T13-7, G4-T6-1, G4-T6-3)
- Expecting a finite graph to test CCM's missing step: a finite divisor has a critical window, and there is no theta function, self-dual Gaussian or prolate tower over `Z`. (G1-T13-6, G4-T1-3, G4-T3-2)
- Treating "not found" literature verdicts as nonexistence proofs: arXiv search is metadata-only. (G2-T9-3, G2-T17-2)

**cMPS decay modes**
- Deriving RH from CP, passivity, one channel and the functional equation: the two-state toy satisfies all of them with two distinct widths. (G4-T10-7)
- Inferring uniform decay from reflection symmetry alone: weak drive keeps the reflection with widths 0.0061 and 0.4939. (G4-T10-7)
- Assuming grading alone protects observable mode selection: a `0.01 P` quartic term makes the denominator degree eight, and `bd = 0` is necessary and implied by nothing. (G4-T12-4)
- Adding dissipative bistochastic noise to a parity jump on the *full* odd block in the Hilbert-Schmidt metric: forces all jumps scalar and the dissipator zero. (G4-T12-5)
- Demanding centered unitarity for every superposition in the physical norm: uniform widths with one rank-one exit *force* nonnormality. (G4-T9-3, G4-T10-3)
- The naive Hadamard finite-part cusp pairing: leaves the zero matrix. (G4-T9-3)
- Assuming a finite positive invariant metric survives a regulator limit: `lambda_min(G_n) = 1/(2n) -> 0`. (G4-T12-10)
- A biased diagonal BC cutoff state with a scalar reset: only the uniform target works, determinant `-(1-2p)^2`. (G4-T13-3)
- The `2|2` Pauli two-jump toy as a *regular* fermionic cMPS: `R_X^2 != 0` violates kinetic regularity. (G4-T12-8)
- A Ramanujan property demanding one uniform rate on the whole odd sector: the full odd space also carries `3 kappa/2` modes. (G4-T12-15)

**Provenance and bookkeeping corrections that closed a route**
- "Theorem 1 is the one-vertex case of Watanabe-Fukumizu's corollary": a bouquet is not a WF graph, and their own scalar specialisation is false there. (G3-T7-3, G4-T16-5)
- "Artin-Ihara L-function for a representation of *any* group": the source says finite groups, extended to `U(N_c)`. (G4-T16-6)
- Claiming the fermionic-cMPS graded bond as a novel construction: it is already in Haegeman-Cirac-Osborne-Verstraete. (G2-T14-3)
- `Tr_{M_n (x) M_n^*} e^{tL}`: wrong space; the intended trace is `Tr_{M_n}`. (G4-T16-2)
- Identifying Huang's termwise criterion with Toeplitz positive definiteness: different conditions, neither implying the other. (G2-T8-7)
- The cut contour proof of unit Lorentzian mass and the cut continuous ring word `A_{j_1...j_k}`: deleted from the final files and worth restoring if the continuous Weil form is ever normalised as a measure. (G4-T15-5, G4-T15-6)
- The cut `P = X` grading example and the abandoned scalar-weight non-backtracking laboratory: both dropped, both still useful as reminders. (G4-T15-30, G4-T15-8)
- The drafted vertex-level Bass identity, the drafted `Psi` seeds S2-S6, and the drafted "sub-system rule" and `Z/2` swap L-function: all shown false in transcript and recorded only there. (G4-T15-11, G4-T15-19, G4-T15-27)

## 5. Bookkeeping issues in the repo

Consolidated and deduplicated.

**Wrong signs and wrong formulas still in the shards or notes**
- `report/sections/04_riemann_channel.tex:71-75` and `notes/riemann-channel-note.md:59-64` write `Z(t)^* k_lambda = exp(-it conj lambda) k_lambda` and call it decaying; substituting gives *growth* `e^{+beta t/2}`. Found independently by two lanes and deliberately left unrepaired. (G4-T9-6)
- `report/sections/04_riemann_channel.tex:169-173` has the prime part of `Tr Z(t)` with the wrong sign and the damping applied twice; the shard must name its variable, since the factor 2 is a Jacobian. (G3-T1-4, G1-T6-9)
- `notes/riemann-channel-note.md` section 5 still carries `+Lambda(n) n^{-1/2}`, off by `-2` against the note's own explicit formula. (G1-T6-9)
- The scattering-symbol normalisation `S(tau) = [(2i tau - 1)/(2i tau + 1)] phi(1/2 + i tau)` is recorded and not applied; Uetake's own convention adds a further factor and a pole at `p = -1/2`. (G4-T9-6)
- Shard 05's closing paragraph calls the Weil-LPS divisor points "nontrivial zeros"; they are poles. (Fixed; G3-T2-1)
- Add "with periodic closure" to `cor:curve-counts-graded` when next touched. (G1-T11-5)
- Ledger item 5 of the ring-norm proofs still records the growing cut-rank table as evidence of unboundedness, after the self-dual-basis result superseded it. (G3-T20-4)
- Two condition names, C6curve and C6projective, cut different examples and both must stay in the ledger. (G4-T15-26)

**Dependency rot and status derivation in `db/claims.tsv`**
- `obs:complementary-halves` was `proved` while its first clause rested on a `sketched` input, and `prop:absorbing-vacuum-channel` had `deps = -` although its Riemann specialisation needs the Lax-Phillips hypothesis, which had disappeared from the dependency chain. In this book the printed status is *derived* from the deps, so a wrong dep list silently promotes a claim. Downgraded to `sketched`. (G1-T5-9, G3-T20-2)
- Suggested gate check, never added: flag any `proved` row whose text mentions "zeros" but whose deps contain no zeta input. (G3-T20-2)
- `thm:supertrace-rigidity` must record that the cut-offs are nonnegative and monotone in both parameters, or the unconditional pole-parity half cannot be reconstructed. (G3-T20-2)
- The statement column for `num:bc-entropy` still lacks the constants, and the gate will not catch the drift. (G3-T20-2)
- The H-TWIST hedge to all-even letters is conservative and can be dropped; H-DEG must stay split so the elliptic Polya-Hilbert theorem is visibly non-circular. (G3-T20-2)
- The `ihz` campaign touched nothing under `report/`, `db/`, top-level `notes/*.md` or `scripts/`, so none of its 31 proved theory claims is registered. (G1-T13-8)
- The 2026-09-19 four-mode cMPS mechanism is unregistered; the session's main lead lives only in `HANDOFF.md`. (G1-T6-10, G4-T16-12)

**Unreviewed load-bearing claims**
- `obs:rh-iff-ramanujan-channel` (RH for the quantum Ihara zeta iff Hastings' bound) is `sketched` because it has had **no reviewer**, and it is the bridge between zeta language and channel language. (G2-T7-4)
- `||Z_t|| = 1` for every `t` is marked `[inferred]` and unreviewed, with a second reader explicitly requested. (G4-T14-4)
- Shard 06h (the ten-condition ledger) is entirely unreviewed by a second model family; every row is `sketched` or `numerical`. (G2-T5-1)
- Both author and reviewer have so far been Claude models on the review side. Explicitly unreviewed by a second family: the `ihz` lane reports and theory claims, shard 04g, the cMPS parity rows (04e/04f), the graded permutation rows (03b), and shard 08g. (G1-T15-2, G2-T19-1)
- The 04f physical Fock-space half of the norm identity is only sketched; and "the D3 headline over-credits the letters" when quoting the Selberg campaign. (G1-T15-3)

**Unverified citations and undischarged assumptions**
- The Adamyan-Arov identification of the compressed semigroup with the Lax-Phillips semigroup is quoted with no local source, and the innerness argument (the Phragmen-Lindeloef step) is not written out. The repository's headline identification rests on both. (G1-T6-2)
- Eleven citations in the 2026-09-12 provenance set name a nonexistent file, two point past EOF, and two ranges exclude the quote they label - although no quoted string is misquoted. `refs/README.md` promises re-checkability against those paths. (G4-T16-6)
- `refs/src/1403.0256/RuelleResonForHn.tex` is cited as the compact first-band primary source and the agent was interrupted while verifying that the path exists. (G4-T17-10)
- H-repka (the complementary-series threshold `3/4`) is "from memory, not to be cited until byte-checked". (G1-T8-12, G3-T20-3)
- H-SZ (entireness, spectral divisor, trivial divisor, order at `s = 0`) and H-LAP have no byte-cited source, which blocks promoting the continuous-Ramanujan theorem past conditional; H-GUI swallows the Anosov nondegeneracy and wave-front conditions. Six standard Selberg inputs are carried as `assumed`. (G1-T12-7, G2-T16-8, G3-T20-3)
- Eight external theorems in the complex-zeta lane are `assumed`, and Kang-Yu's `thm:Phi-determinants` and its local factorisation were confirmed to exist but not checked line by line, although everything conditional on Kang-Yu rests on them. (G2-T11-8, G2-T12-5)
- `asm:weil-implementer-exact` (a genuine centred lift of `Sp(2J,F_q)`), `asm:as-lpolynomial`, `asm:deuring-lift`, `asm:cm-hodge-type` (whose eigenspace clause is "not quotable from the fetched TeX"), `asm:cm-polarised-lift` and `asm:kraus-hs-setting` ("not established for any Riemann cMPS") are all undischarged. (G2-T2-3, G2-T2-4, G2-T3-3, G2-T3-9, G2-T4-2, G3-T20-3)
- The Watanabe-Fukumizu shape-matching for Theorem 1 is checked numerically only; the NeurIPS 2009 supplement with a hypergraph-free proof was never fetched. (G2-T7-6, G4-T16-5)
- Eight literature items in the CCM sidequest are unverified from primary text, with Terras 2011's book content "the single biggest gap" and Makhoul 1981's exact hypotheses mathematically load-bearing; six staged arXiv ids were never fetched, including Connes-Consani 2006.13771. (G4-T8-3)
- Prior-art absence claims rest on metadata-only searches; no full-text search has ever been run. (G2-T17-2)
- The type `III_1` attribution overreached its byte-verified support (the source labels only the critical temperature); fixed in round two. (G3-T20-3)
- One very recent unrefereed preprint with typographic front matter is used for attribution only and must never be quoted as the authority for a proof. (G3-T20-3)
- Newly cached references are unused: Bonthonneau-Weich (`refs/src/1712.07832/`) and Uetake 2007 (`refs/src/uetake-2007/`). (G1-T6-11)
- `ihz` cites the notebook's own `report/sections/*.tex` for ground truth rather than a fetchable paper, so its correctness is only as good as the notebook's `stipulated` rows. (G4-T8-3)

**Novelty downgrades and citation hazards**
- The graded/fermionic cMPS bond structure is already in the literature (Bultinck et al.; Haegeman-Cirac-Osborne-Verstraete); only the arithmetic reading can be claimed. (G2-T14-3)
- Do not cite `lambda_H = 2 sqrt(D-1)/D` as a proved bound: Hastings proves only `sqrt(lambda_H)` rigorously. (G2-T19-4)
- `refs/src/0809.1401/` carries the Kang-Li title, not Kang-Li-Wang; quote Kang-Li-Wang from `0809.1401v1` only. (G2-T19-4)
- `math-ph/0404030` is not Voros (deleted); arXiv:2309.15873 is Eyler-Jun, not Kudo-Li (corrected). (G2-T19-4)
- Ben-Aroya-Schwartz-Ta-Shma's remark about improving to a quantum Ramanujan expander was read from a publisher PDF with no local TeX; if their construction reaches the bound the novelty claim needs adjusting. (G2-T1-3)
- The Pisarenko / Caratheodory-Fejer framing of the window form is net new to the notebook and must be registered as new, not as a corollary of shard 08b. (G4-T1-2)
- Hallouin-Perret got to the curve/Toeplitz instance first; read them before claiming anything on the curve side. (G4-T6-2)
- CCM's displayed correction constant `c(L)` is a typo (0.352 against the required 0.575); their code is right. (G1-T13-4, G4-T8-3)

**Conventions in conflict**
- Three vectorisation conventions are in use across the prior-art note, the theorem note and Matsuura-Ohta; conventions of this kind have already caused two sign errors. (G4-T16-6)
- Sixteen notation ambiguities, four substantive: channel normalisation (`Phi` / `D Phi` / `Sigma`); Ramanujan units, with one table mixing two in a single row; `q` versus `D-1`; and what "Riemann channel" denotes - no note gives a one-sentence definition, and "Bost-Connes system" is used but never defined. (G2-T19-2)
- Laplacian sign conventions clash across the Selberg sources; fix one before any computation or risk the same `-1/4` versus `-3/4` centring confusion. (G2-T16-8, G4-T9-5)
- Three candidate centres (`-1/2` Selberg, `-3/4` flow, `-1/4` model) belong to three different operators, and four observables give four widths for the same zeros; state which is meant before quoting any width. (G4-T9-5)
- "Stable" for the covector `eta_+` collides with the dual-bundle naming convention of the cited literature. (G3-T20-4)
- "Graded CP transfer" and "graded spectral transfer" must be distinguished; and every Ramanujan claim must say whether it is about the cancelled divisor or the uncancelled retained spectrum. (G1-T8-2, G4-T15-28)

**Code, CI and test debt**
- `scripts/qihara_general.py` prints a BLAS-thread-dependent rounding error (5.5e-12 at 2/4/8 threads, 3.7e-12 at one) into a committed fixture, and `scripts/ci_local.sh` does not pin the thread count: a live reproducibility bug in the repo's own gate. Fix by printing fewer digits, asserting a bound, or pinning threads to 2. (G4-T16-14)
- `outputs/graded_ramanujan.txt` was edited to turn `-0.0` into `0.0` during a shutdown rather than during review (display-only). (G4-T16-14)
- `zst/README.md` records two out-of-bounds reads inside uninstrumented FLINT calls that ASan cannot see, still unfixed; and `zst`'s mutation record covers only the pre-benchmark MVP although every `x >= 20` row came from changed code. (G1-T13-5, G4-T7-3)
- `ihz` was built with testing discipline relaxed at TJO's request: no fuzz, no mutation. Both passes found real bugs in `zst`. (G4-T7-3)
- The `k = 0` boundary term `t_0` is the audit's most likely silent bug and needs its own derivation and a red test; `eigmin.c` is duplicated verbatim between the two verticals. (G4-T7-3)
- Not done: the Q-2 fit, the anti-palindromic search, irregular graphs in C, the Cayley certified cross-check. (G1-T13-8)
- The `x = 60` and `x = 80` certified spectra were lost to a cleanup mistake before their tables were extracted. (G4-T2-2)
- `scripts/graded_ramanujan.py` passes 79 checks but none of them tests its own printed genus claims, which are wrong by a wide margin. (G4-T15-29)
- The quantum-Ihara note never defines its norm (the Neumann step needs submultiplicativity), its `exact_check` shares an RNG stream with the float checks, and the displayed identity `det(1 + D - A)` is never evaluated. (G3-T20-4, G4-T16-7)
- Both Selberg-side prover files used inline non-writing Python, leaving `notes/<lane>/scratch/` empty; the numbers are exact but not re-runnable. (G3-T20-4)
- Six rows of the Selberg-letters prover ledger report the draft's *questions* as errors found, and the lab book reads that ledger as a list of errors. (G3-T20-4)
- Script bugs since fixed, kept as warnings: sectors read off the diagonal of `Gamma_b` are valid only when `P` is diagonal; the script printed a raw odd count as a "genus"; the duality matrix `J` for the 06h elliptic tensor was wrong twice; the ported `eigmin` converged to the smallest-*modulus* eigenvalue. (G1-T13-5, G1-T13-6, G1-T8-8, G1-T11-9)
- The cusp diagnostic's three-mode centered defect norm was first written as "about 2.59" and silently corrected to "about 2.2544"; the number is load-bearing. (G4-T16-1)

**Session hygiene**
- Every inter-agent payload in the 2026-09-19 session is a Fernet token or an empty block, so the orchestrator's briefs and the subagents' reports are **unrecoverable**; any ideation in a brief that no subagent acted on is gone. Future fan-outs should have the parent write each brief to disk as it sends it. (G4 lane L17 coverage caveat, recorded under G4-T16-11)
- The recovery archives live on the same disk as the repository; the off-site copy the orchestrator flagged was never made. (G4-T16-3)
- Subagent shells had no network egress; route downloads through the parent from the start. (G4-T16-13)
- The brief's requested non-building tests were substituted, not run (the 7-vertex triangulated torus, the only case with `b_1 != 0`, was never computed). (G2-T9-7, G4-T15-19)
- Rationality bookkeeping is explicitly omitted from `notes/deligne-via-graphs.md`. (G1-T11-11)

## 6. Audit

**Digest items by class** (counted mechanically over the four digest files; 492 items, one `Class:`
line each):

| Class | Count |
|-------|-------|
| EXPLORED-registered | 209 |
| PARTIAL | 99 |
| LEAD-unpursued | 98 |
| EXPLORED-negative | 71 |
| DEAD | 15 |
| **Total** | **492** |

(Three of those lines carry a parenthetical qualifier in the digests: two
`EXPLORED-registered (a warning / a novelty downgrade)` and one `EXPLORED-negative (a warning)`;
they are counted with their base class.)

Per digest: G1 = 124 items, G2 = 139, G3 = 80, G4 = 149. Those 492 items absorb 1509 lane entries
(G1 446, G2 356, G3 357, G4 350), and each digest's own audit section states that every lane ID
appears in exactly one `Absorbs` list.

**Coverage check.** Run mechanically by extracting every `G<n>-T<i>-<j>` identifier from the digest
headings and grepping sections 2 to 5 of this file:

- all **492** digest item IDs appear somewhere in sections 2 to 5 (0 missing);
- all **295** items of class EXPLORED-registered, EXPLORED-negative or DEAD appear in section 2
  (0 missing);
- all **197** items of class LEAD-unpursued or PARTIAL appear in section 3.2 (0 missing);
- section 3.1 cites 97 distinct item IDs across its 40 rows, section 3.3 cites 39, section 4 cites
  224, and section 5 cites 63;
- section 4 accounts for all 15 DEAD items and all 71 EXPLORED-negative items.

**Merged groups.** The same idea reached two, three or four digests. The groups merged into one row
of section 3.1 or one line of section 4 are:

- The `Gamma_0(N)` scattering/character computation: G1-T10-9 + G4-T13-11 + G2-T18-1.
- The four-mode fermionic cMPS mechanism and the five-step arithmetic programme: G1-T6-10 + G4-T12-11 + G4-T17-6 + G4-T10-1.
- H-CUSP-BRIDGE: G1-T12-9 + G3-T15-2 + G4-T9-1 + G4-T17-2.
- The flow-to-wave intertwiner and the two cached endpoints: G1-T6-11 + G4-T9-4.
- The modewise leakage estimate and the minimal missing identity: G4-T10-9 + G4-T10-6 + G4-T10-2.
- `||Z_t|| = 1`, the Riesz-basis obstruction and the Gram condition-number test: G1-T6-6 + G3-T8-3 + G4-T14-4 + G4-T14-5.
- Mayer's operator: G1-T12-10 + G3-T15-3 (and G1-T6-8 ranks it first among fifteen mechanisms).
- Suzuki's screw kernel and the prime-side positivity test: G1-T6-8 + G3-T19-3 + G4-T11-7.
- The SHW rebound state and the invariant-sector test: G1-T6-5 + G3-T10-2 + G4-T13-12 + G4-T17-4.
- The extension disc and the two unrun window computations: G1-T13-9 + G2-T15-2 + G2-T15-5.
- The under-resolved law and the prolate/Slepian identification: G1-T13-8 + G4-T3-2 + G4-T3-3.
- Infinite parity rigidity: G1-T7-3 + G3-T1-3 + G4-T15-15.
- Asymmetric Galois rates and the even-Hamiltonian escape: G1-T9-4 + G3-T17-1.
- Weil-LPS Hecke identification and assembly over `p`: G1-T3-6 + G2-T1-1, and G1-T3-9 + G2-T1-2.
- The Kraus dichotomy and its corrections: G1-T13-2 + G2-T8-3 + G3-T9-2 + G4-T15-7.
- The bosonic genus bound and its false drafted proof: G1-T11-7 + G2-T4-1 + G3-T2-4.
- The numerator no-go / grading forced by the trace: G1-T7-2 + G2-T4-3 + G3-T2-2.
- The Artin-Schreier sign law and its two refuted drafts: G1-T11-2 + G2-T2-4 + G3-T6-1 + G4-T15-14.
- The prime-circle negative: G1-T3-7 + G2-T6-2 + G2-T16-1 + G3-T14-6 + G4-T15-4.
- The cusp prime comb with its `+1/2` constant and dip sign: G2-T16-5 + G2-T16-6 + G3-T15-1 + G4-T9-7.
- The Ruelle two-band failure and the degenerate pullback: G1-T12-3 + G1-T12-5 + G3-T5-3 + G3-T14-3 + G4-T9-8.
- The odd-sector Alon-Boppana refutation: G1-T8-7 + G3-T5-2 + G4-T12-6.
- The mixed-parity refusal in the CCM chain: G1-T13-7 + G4-T6-1 + G4-T6-3.
- Weil positivity blind to Jordan blocks, in its three appearances (Selberg `1/4`, Hashimoto endpoints, the model space): G1-T13-3 + G2-T8-5 + G4-T5-4 + G4-T10-8.
- Watanabe-Fukumizu provenance for Theorem 1: G2-T7-6 + G3-T7-3 + G4-T16-5.
- "Positivity plus a multiplying operation, not a Hermitian form": G1-T11-12 + G2-T6-1 + G2-T6-6 + G4-T11-4.
- No finite representation of the BC algebra: G1-T10-8 + G2-T18-3 + G4-T13-8.
- The BC generator cone and the symmetry collapse: G1-T10-5 + G1-T10-7 + G2-T18-4 + G2-T18-5 + G4-T17-7.
- The yolo phase-side audit: G1-T10-1 + G1-T10-2 + G1-T10-3 + G3-T12-1 + G3-T12-2 + G3-T12-3 + G4-T15-23 + G4-T15-24.
- Knill's torsion and the unclaimed join to Ihara: G1-T14-2 + G2-T13-1 + G2-T13-5.
- The vertex-collapse conjecture and the tetrahedron obstruction: G2-T9-6 + G4-T15-19.
- The `A~_2` numerics, anomaly and Euler bookkeeping: G1-T14-4 + G2-T11-3 + G2-T11-6 + G2-T11-7.

No digest item was dropped or silently folded away: every merge above is recorded on the line that
performs it, with all the merged IDs listed.
